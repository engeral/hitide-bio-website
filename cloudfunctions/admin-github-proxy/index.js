/**
 * CloudBase HTTP 云函数:admin-github-proxy
 *
 * 作用:
 *  1. /login  用 ADMIN_PASSWORD 校验,返回 session token
 *  2. /load   拉 GitHub data/products.json
 *  3. /save   PUT GitHub data/products.json(用 GitHub PAT,环境变量注入)
 *
 * 环境变量(在 CloudBase 控制台 → 云函数 → 函数配置 → 环境变量 配):
 *  - ADMIN_PASSWORD   admin.html 单密码(默认 hitide2026,Stephen 自定)
 *  - SESSION_SECRET   用于签 session token 的密钥(任意长字符串)
 *  - GH_TOKEN         GitHub Fine-grained PAT,contents:read & write 范围 engeral/hitide-bio-website
 *  - GH_REPO          默认 'engeral/hitide-bio-website'
 *  - GH_FILE_PATH     默认 'data/products.json'
 *  - GH_COMMIT_NAME   commit 作者名,默认 'HiTide Admin'
 *  - GH_COMMIT_EMAIL  commit 作者邮箱,默认 '[email protected]'
 *
 * 部署:在 hitide-d4gbdg9472af41310 环境创建 HTTP 函数,选「Node.js 18+」运行时,
 *      把本目录上传 / 用 tcb 命令部署。设触发路径 '/admin-github-proxy'(URL 里就是这个路径)。
 */

const crypto = require('crypto');

// =====================================================
// 配置(从环境变量读)
// =====================================================
const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || 'hitide2026';
const SESSION_SECRET = process.env.SESSION_SECRET || 'hitide-default-secret-change-me';
const GH_TOKEN = process.env.GH_TOKEN || '';
const GH_REPO = process.env.GH_REPO || 'engeral/hitide-bio-website';
const GH_FILE_PATH = process.env.GH_FILE_PATH || 'data/products.json';
const GH_COMMIT_NAME = process.env.GH_COMMIT_NAME || 'HiTide Admin';
const GH_COMMIT_EMAIL = process.env.GH_COMMIT_EMAIL || '[email protected]';

const SESSION_TTL_MS = 8 * 3600 * 1000; // 8 小时

// =====================================================
// session token(简单 HMAC 签名,不依赖外部存储)
// =====================================================
function makeToken() {
  const payload = JSON.stringify({
    iat: Date.now(),
    exp: Date.now() + SESSION_TTL_MS,
    nonce: crypto.randomBytes(8).toString('hex'),
  });
  const sig = crypto
    .createHmac('sha256', SESSION_SECRET)
    .update(payload)
    .digest('hex');
  return Buffer.from(payload).toString('base64url') + '.' + sig;
}

function verifyToken(token) {
  if (!token || typeof token !== 'string') return false;
  const parts = token.split('.');
  if (parts.length !== 2) return false;
  let payload;
  try {
    payload = JSON.parse(Buffer.from(parts[0], 'base64url').toString('utf-8'));
  } catch {
    return false;
  }
  const expected = crypto
    .createHmac('sha256', SESSION_SECRET)
    .update(Buffer.from(parts[0], 'base64url').toString('utf-8')) // 注意:签的是 payload 字符串
    .digest('hex');
  if (expected !== parts[1]) return false;
  if (Date.now() > payload.exp) return false;
  return true;
}

// =====================================================
// GitHub API 封装
// =====================================================
const GH_API = 'https://api.github.com';

async function ghGetFile() {
  const url = `${GH_API}/repos/${GH_REPO}/contents/${GH_FILE_PATH}`;
  const res = await fetch(url, {
    headers: {
      Authorization: `Bearer ${GH_TOKEN}`,
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'User-Agent': 'hitide-admin-proxy',
    },
  });
  if (res.status === 404) return null;
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`GitHub GET ${res.status}: ${body.slice(0, 200)}`);
  }
  return res.json();
}

async function ghPutFile(content, sha, message) {
  const url = `${GH_API}/repos/${GH_REPO}/contents/${GH_FILE_PATH}`;
  const body = {
    message: message || 'update products via admin',
    content: Buffer.from(content, 'utf-8').toString('base64'),
    sha,
    committer: { name: GH_COMMIT_NAME, email: GH_COMMIT_EMAIL },
  };
  const res = await fetch(url, {
    method: 'PUT',
    headers: {
      Authorization: `Bearer ${GH_TOKEN}`,
      Accept: 'application/vnd.github+json',
      'Content-Type': 'application/json',
      'X-GitHub-Api-Version': '2022-11-28',
      'User-Agent': 'hitide-admin-proxy',
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const t = await res.text();
    throw new Error(`GitHub PUT ${res.status}: ${t.slice(0, 200)}`);
  }
  return res.json();
}

// =====================================================
// 主入口(CloudBase HTTP 函数约定 exports.main)
// =====================================================
exports.main = async (event /*, context*/) => {
  // CORS preflight
  if (event.method === 'OPTIONS') {
    return {
      statusCode: 200,
      headers: corsHeaders(),
      body: '',
    };
  }

  let payload = {};
  try {
    if (event.body && typeof event.body === 'string') {
      payload = JSON.parse(event.body);
    } else if (event.body && typeof event.body === 'object') {
      payload = event.body;
    }
  } catch (e) {
    return json({ ok: false, error: 'JSON 解析失败' }, 400);
  }

  const action = payload.action;

  try {
    // ========== login ==========
    if (action === 'login') {
      if (!payload.password || payload.password !== ADMIN_PASSWORD) {
        return json({ ok: false, error: '密码错误' }, 401);
      }
      return json({ ok: true, token: makeToken() });
    }

    // ========== 以下接口都要鉴权 ==========
    if (!verifyToken(payload.token)) {
      return json({ ok: false, error: '未登录或会话过期,请重新登录' }, 401);
    }

    // ========== load ==========
    if (action === 'load') {
      if (!GH_TOKEN) return json({ ok: false, error: '云函数未配置 GH_TOKEN' }, 500);
      const file = await ghGetFile();
      if (!file) return json({ ok: false, error: `GitHub 上找不到 ${GH_FILE_PATH},请先 commit 一份空 JSON []` }, 404);
      const content = Buffer.from(file.content, 'base64').toString('utf-8');
      let products;
      try {
        products = JSON.parse(content);
      } catch (e) {
        return json({ ok: false, error: 'JSON 解析失败: ' + e.message }, 500);
      }
      return json({ ok: true, products });
    }

    // ========== save ==========
    if (action === 'save') {
      if (!GH_TOKEN) return json({ ok: false, error: '云函数未配置 GH_TOKEN' }, 500);
      if (!Array.isArray(payload.products)) {
        return json({ ok: false, error: 'products 不是数组' }, 400);
      }
      const file = await ghGetFile();
      const sha = file ? file.sha : null;
      const newContent = JSON.stringify(payload.products, null, 2);
      const result = await ghPutFile(newContent, sha, payload.message || 'update products via admin');
      return json({ ok: true, commit_sha: (result.commit && result.commit.sha) || result.sha });
    }

    return json({ ok: false, error: '未知 action: ' + action }, 400);
  } catch (e) {
    console.error('[admin-github-proxy]', e);
    return json({ ok: false, error: e.message || String(e) }, 500);
  }
};

// =====================================================
// helpers
// =====================================================
function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json',
  };
}

function json(obj, status = 200) {
  return {
    statusCode: status,
    headers: corsHeaders(),
    body: JSON.stringify(obj),
  };
}