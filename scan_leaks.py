# -*- coding: utf-8 -*-
"""Scan rendered HTML for Chinese text that would remain visible in EN mode.
Whitelisted (handled by CSS/JS in EN mode):
 - text inside <span class="t-zh"> (hidden via body.lang-en .t-zh{display:none})
 - text inside elements with data-i18n (swapped by applyLang)
 - <title> text (swapped by applyLang reading data-en-title)
 - <script> contents
 - elements with class 'cn' (brand/footer .cn hidden in EN)
 - lang toggle buttons (id langZh / langEn) — intentionally Chinese
"""
import os, re, glob
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))

class Scanner(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []   # bool per element: suppress?
        self.leaks = []

    def _suppress(self, tag, attrs):
        d = dict(attrs)
        cls = d.get('class', '') or ''
        if tag == 'script':
            return True
        if tag == 'title':
            return True
        if 't-zh' in cls.split():
            return True
        if 'cn' in cls.split():
            return True
        if d.get('data-i18n'):
            return True
        if d.get('id') in ('langZh', 'langEn'):
            return True
        return False

    def handle_starttag(self, tag, attrs):
        sup = (self.stack[-1] if self.stack else False) or self._suppress(tag, attrs)
        self.stack.append(sup)

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if self.stack and self.stack[-1]:
            return
        for m in re.finditer(r'[\u4e00-\u9fff]+', data):
            self.leaks.append(m.group())

def scan_file(path):
    html = open(path, encoding='utf-8').read()
    s = Scanner()
    s.feed(html)
    return s.leaks

def main():
    files = glob.glob(os.path.join(ROOT, '*.html')) + glob.glob(os.path.join(ROOT, 'products', '*.html'))
    total = 0
    report = []
    for f in sorted(files):
        leaks = scan_file(f)
        if leaks:
            total += len(leaks)
            report.append((os.path.relpath(f, ROOT), leaks))
    if not report:
        print('CLEAN — no Chinese leaked in EN mode across', len(files), 'pages.')
    else:
        print(f'LEAKS: {total} Chinese runs in {len(report)} files (of {len(files)}):')
        for rel, leaks in report:
            print(f'\n  {rel}  ({len(leaks)}):')
            seen = {}
            for r in leaks:
                seen[r] = seen.get(r, 0) + 1
            print('    ' + ', '.join(f'{k}({v})' for k, v in sorted(seen.items(), key=lambda kv: -kv[1])[:25]))

if __name__ == '__main__':
    main()
