# -*- coding: utf-8 -*-
"""json_fetch.py — 读 data/products.json(海泰在 admin 改完后由 GitHub API commit 进来的)

数据源优先级（2026-08-27 起）
=============================
1. cms_fetch.fetch_products()   (CloudBase CMS,暂未启用,代码保留)
2. json_fetch.fetch_products()  (GitHub 来源,海泰在 admin.html 改后到这里)
3. md_fetch.fetch_products()    (TinaCMS,留作未来选项)
4. build.py 内置 add() 数据      (hardcoded final fallback)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / 'data' / 'products.json'


def _log(msg):
    print(f'[json_fetch] {msg}', file=sys.stderr)


def fetch_products():
    """从 data/products.json 读 41 个产品,返回 list[dict] 或 None。

    返回结构与 build.py add() 一致,字段顺序如下：
      id, name, en, cat, img, type, net, std, disease, tags(list), meta(list), lead
    """
    if not JSON_PATH.exists():
        _log(f'{JSON_PATH} 不存在 → 返回 None')
        return None
    try:
        items = json.loads(JSON_PATH.read_text(encoding='utf-8'))
    except Exception as e:
        _log(f'JSON 解析失败: {e} → 返回 None')
        return None
    if not isinstance(items, list):
        _log('JSON 顶层不是 list → 返回 None')
        return None
    # 兜底:tags/meta 应为 list
    for rec in items:
        if isinstance(rec.get('tags'), str):
            rec['tags'] = [t.strip() for t in rec['tags'].split(',') if t.strip()]
        if isinstance(rec.get('meta'), str):
            rec['meta'] = [m.strip() for m in rec['meta'].split('\n') if m.strip()]
        rec.setdefault('tags', [])
        rec.setdefault('meta', [])
        rec.setdefault('lead', '')
        rec.setdefault('img', '')
    _log(f'从 {JSON_PATH.name} 读到 {len(items)} 个产品')
    return items


if __name__ == '__main__':
    print(json.dumps(fetch_products() or [], ensure_ascii=False, indent=2))