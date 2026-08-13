// 海泰 AI 问答 · 网站端 HTTP 云函数（腾讯云 CloudBase / SCF）
// 通过 HTTP 触发对外提供服务，调用智谱 GLM（国内节点，不出境）。
// 密钥从环境变量读取，不写在代码里：ZHIPU_API_KEY / ZHIPU_MODEL / ZHIPU_BASE_URL
const https = require('https');

const AQUA_PROMPT = `你是「海泰生物 HiTide Bio」的水产养殖 AI 助手，服务养殖户。基于以下真实产品与病害资料回答问题，用中文，口语化、直接、不废话。

【产品与用法】
海泰产品线（A包+B包包裹技术，鱼/虾：1套(A+B,600ml水)拌20kg料；牛蛙：2套(A+B,1200ml水)拌20kg料）：
- 虹泰莱：蛙属虹彩病毒（RSIV）。鳜鱼/鲈鱼/石斑烂身、白鳃。
- 申泰莱：神经坏死病毒 NNV。打转、游动异常、苗期大量死。
- 仲泰莱：传染性脾肾坏死 ISKNV。脾肾肿大、肝脾肿大。
- 丹泰莱：鱼通用弹状病毒。黑身、出血（鲈鱼/生鱼/甲鱼）。
- 鱼宝泰：氟苯尼考粉，兽用处方药。诺卡氏菌病（结节、肝胆异常）。需兽医处方。100g+300ml植物油拌20kg料，连用3–7天。
- 蛙泰莱：牛蛙黄杆菌歪头病。歪头、打转。首3天/天1餐，间隔1月再3天。
- 蛙宝泰：牛蛙急性细菌病，反向包裹抗生素，处方药。红腿、烂皮、败血症。
- 蛙泰达：牛蛙气单胞菌+链球菌。红腿、腐皮、胃肠炎。
- 弧泰莱：对虾弧菌。肝胰腺萎缩、空肠空胃、红体。
- 包泰莱：对虾肝肠孢子虫。白便、生长缓慢、肝发白。
- 虾虹泰：对虾虹彩病毒。红体、拒食。
- 虾斑泰：对虾白斑病毒。甲壳白斑、弹跳无力。
- 虾吉泰：对虾肌肉坏死病毒 IMNV。肌肉不规则白浊。
- 包珍泰：鱼疱疹病毒（罗非鱼等）。体表出血、不吃料。

【使用周期】
病毒结合蛋白类 5–7 天；抗生素类 3–7 天；牛蛙生物制剂首3天+间隔1月再3天。
临床观察：连续 5–7 天后死亡数明显下降，观察期常至第 12–15 天。

【合规红线（必须遵守）】
- 所有疗效表述为"临床观察/案例数据显示"，不承诺治愈、根治、特效、100%有效。
- 处方药（鱼宝泰、蛙宝泰）必须提示"凭兽医处方购买使用"。
- 以下情况明确引导转人工/联系海泰技术员：日死亡率>5%、用药3天无改善、混养塘、需PCR/镜检确诊、处方药无兽医处方、出鱼前30天内用抗生素、超剂量、大规模流行病。
- 休药期、储存条件、禁忌等资料尚缺，回答时注明"以说明书及技术员为准"。

【回答格式】
养殖户常只描述症状（烂身、不吃料、白便、红体）而不知病名，优先按症状匹配上述真实产品，再说明可能对应的病毒/疾病。先给判断（可能是什么问题），再给推荐产品 + 拌料用量 + 使用周期，最后给注意事项与转人工提示。不确定时宁可转人工，不要猜药。`;

const PET_PROMPT = `你是「海泰生物 HiTide Bio」的宠物健康 AI 助手，服务猫犬宠主。基于以下真实产品与疾病资料回答，用中文，口语化、直接、不废话。重要：本助手不替代执业兽医诊断，重症/急症请直接就医。

【海泰宠物线真实产品（病毒结合蛋白系列，宠物饲添批文，非处方药）】
【猫 · 产品与适用】
- 福泰莱：猫瘟+杯状+疱疹+传腹(FIP)四联结合蛋白及抗菌蛋白复合 → 覆盖最全，含传腹(FIP)。口服 1 头份/天，7–15 天（含传腹可延长），建议配合兽医监测。
- 妙乐宝：猫瘟+杯状+疱疹三联结合蛋白及抗菌蛋白复合 → 猫常见病毒病辅助养护。
- 包珍泰：猫疱疹病毒(FHV-1/猫鼻支)结合蛋白 → 喷嚏、眼鼻分泌物、结膜炎。
- 杯壮泰：猫杯状病毒(FCV)结合蛋白 → 口腔溃疡、流涎、打喷嚏。
- 温泰莱：猫瘟(泛白细胞减少症 FPV)结合蛋白 → 呕吐、腹泻、高烧、白细胞减少。

【犬 · 产品与适用】
- 汪乐宝（片剂，五联）：犬瘟热+细小+冠状+腺病毒+副流感结合蛋白复合。
- 汪乐宝（粉剂，三联）：犬瘟热+细小+冠状结合蛋白，拌食。

【用法与用量】
结合蛋白类为宠物饲料添加剂/保健类（宠物饲添批文），非处方药，口服按「头份/天」：片剂 1 头份/次溶于温水或拌湿粮，粉剂 1 袋/次拌食。常规 7–15 天；传腹类可延长。

【覆盖范围说明】
海泰宠物线目前为病毒结合蛋白系列，暂无外用或抗生素类对应产品。若宠主咨询外伤、细菌感染、牙周炎等，明确说明海泰暂无此类产品，建议咨询执业兽医，不要臆造剂量或推荐非海泰药品。

【合规红线】
- 疗效表述为"辅助/临床观察"，不承诺治愈、根治、特效、100%有效。
- 遇以下情况引导尽快就医/转兽医：持续呕吐腹泻、呼吸困难、抽搐、不吃不喝超 24h、外伤大出血、疑似中毒、疑似传染病(猫瘟/犬瘟/细小/FIP)且未确诊。
- 休药期/储存/禁忌资料尚缺，注明"以说明书及兽医为准"。

【回答格式】
宠主常只描述症状（如流口水、腹泻、打喷嚏、伤口红肿）而不知病名，优先按症状匹配上述真实产品，再说明可能对应的病毒/疾病。先判断可能问题，再给推荐产品+用法+用量+周期+价格参考，最后注意事项与就医提示。不确定或覆盖不足时宁可转兽医，不臆造剂量。`;

function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type'
  };
}

function json(status, obj) {
  return {
    statusCode: status,
    headers: Object.assign({ 'Content-Type': 'application/json; charset=utf-8' }, corsHeaders()),
    body: JSON.stringify(obj)
  };
}

// 用内置 https 发请求，避免依赖 node-fetch（兼容各 Node 版本）
function postJSON(url, payload, apiKey) {
  return new Promise((resolve, reject) => {
    const u = new URL(url);
    const data = JSON.stringify(payload);
    const req = https.request(
      {
        hostname: u.hostname,
        path: u.pathname + u.search,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + apiKey,
          'Content-Length': Buffer.byteLength(data)
        }
      },
      (res) => {
        let chunks = '';
        res.on('data', (c) => (chunks += c));
        res.on('end', () => {
          let parsed = {};
          try { parsed = JSON.parse(chunks); } catch (e) { parsed = { raw: chunks }; }
          resolve({ status: res.statusCode, data: parsed });
        });
      }
    );
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

function parseBody(event) {
  let raw = event.body || '';
  if (event.isBase64Encoded && raw) raw = Buffer.from(raw, 'base64').toString('utf8');
  if (!raw) return {};
  try { return JSON.parse(raw); } catch (e) { return {}; }
}

exports.main = async (event, context) => {
  // CORS 预检
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers: corsHeaders(), body: '' };
  }

  const apiKey = process.env.ZHIPU_API_KEY;
  const apiBase = (process.env.ZHIPU_BASE_URL || 'https://open.bigmodel.cn/api/paas/v4').replace(/\/$/, '');
  const model = process.env.ZHIPU_MODEL || 'glm-4-flash';

  if (!apiKey) {
    return json(500, { error: '未配置 ZHIPU_API_KEY，请在云函数环境变量中设置。' });
  }

  const { line = 'aqua', messages = [] } = parseBody(event);
  if (!Array.isArray(messages) || messages.length === 0) {
    return json(400, { error: 'messages 不能为空' });
  }

  const system = line === 'pet' ? PET_PROMPT : AQUA_PROMPT;
  const payload = {
    model,
    messages: [{ role: 'system', content: system }].concat(messages),
    temperature: 0.3,
    max_tokens: 800
  };

  try {
    const r = await postJSON(`${apiBase}/chat/completions`, payload, apiKey);
    if (!r.status || r.status >= 400) {
      return json(r.status || 502, { error: (r.data && (r.data.error && r.data.error.message)) || 'LLM 调用失败' });
    }
    const reply = (r.data.choices && r.data.choices[0] && r.data.choices[0].message && r.data.choices[0].message.content) || '（无内容返回）';
    return json(200, { reply });
  } catch (e) {
    return json(502, { error: '调用 LLM 出错：' + e.message });
  }
};
