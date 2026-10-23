"""Check a generated Jekyll site: python3 -m unittest discover -s tests -v.

Set SITE_DIR and SITE_BASEURL to check a production or preview build.
"""
import json
import os
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit
import unittest

ROOT = Path(os.environ.get('SITE_DIR', '_site'))
BASE = os.environ.get('SITE_BASEURL', '').rstrip('/')


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.links, self.assets, self.ids, self.nav = [], [], set(), []
        self.meta, self.canonical = {}, ''
        self.lang, self.h1, self.main = '', 0, False
        self.in_nav, self.in_json, self.json_text = False, False, ''
        self.schema = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag == 'html':
            self.lang = a.get('lang', '')
        if tag == 'main':
            self.main = True
        if tag == 'h1':
            self.h1 += 1
        if tag == 'nav':
            self.in_nav = True
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
            if self.in_nav:
                self.nav.append(a['href'])
        if tag in ('img', 'script') and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet':
            self.assets.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a['href']
        if tag == 'meta':
            self.meta[a.get('property', a.get('name', ''))] = a.get('content', '')
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_json, self.json_text = True, ''

    def handle_data(self, data):
        if self.in_json:
            self.json_text += data

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False
        if tag == 'script' and self.in_json:
            self.schema.append(json.loads(self.json_text))
            self.in_json = False


class SiteChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {p: Page(p) for p in ROOT.rglob('*.html')}
        if not cls.pages:
            raise RuntimeError(f'No generated HTML in {ROOT}; build Jekyll first')

    def test_local_links_assets_and_fragments_resolve(self):
        failures = []
        for path, page in self.pages.items():
            base = BASE + '/' + path.relative_to(ROOT).as_posix()
            for ref in page.links + page.assets:
                u = urlsplit(urljoin(base, ref))
                if u.scheme or u.netloc:
                    continue
                urlpath = unquote(u.path)
                if BASE:
                    if not (urlpath == BASE or urlpath.startswith(BASE + '/')):
                        failures.append(f'{path}: escapes preview base: {ref}')
                        continue
                    urlpath = urlpath[len(BASE):]
                target = ROOT / urlpath.lstrip('/')
                if target.is_dir():
                    target /= 'index.html'
                if not target.exists():
                    failures.append(f'{path}: missing {ref}')
                elif u.fragment and target in self.pages and unquote(u.fragment) not in self.pages[target].ids:
                    failures.append(f'{path}: missing fragment {ref}')
        self.assertEqual(failures, [])

    def test_navigation_has_no_duplicate_destinations(self):
        for path, page in self.pages.items():
            with self.subTest(page=path):
                self.assertEqual(len(page.nav), len(set(page.nav)))

    def test_chinese_pages_have_language_and_one_main_heading(self):
        for path, page in self.pages.items():
            if page.main:
                with self.subTest(page=path):
                    self.assertEqual(page.lang, 'zh-CN')
                    self.assertEqual(page.h1, 1)

    def test_sharing_uses_each_pages_url_and_an_absolute_image(self):
        for path, page in self.pages.items():
            if page.main:
                with self.subTest(page=path):
                    route = '/' + path.relative_to(ROOT).as_posix()
                    if route.endswith('index.html'):
                        route = route[:-10]
                    self.assertEqual(urlsplit(page.meta.get('og:url', '')).path, BASE + route)
                    self.assertEqual(page.canonical, page.meta['og:url'])
                    self.assertIn(urlsplit(page.meta.get('og:image', '')).scheme, ('http', 'https'))
                    self.assertEqual(page.meta['og:locale'], 'zh_CN')
                    self.assertTrue(page.meta.get('og:title'))

    def test_news_article_has_article_metadata(self):
        page = self.pages[ROOT / '2026/10/09/neurips-accepted-papers.html']
        self.assertEqual(page.meta.get('og:type'), 'article')
        self.assertEqual(page.schema[0]['@type'], 'BlogPosting')
        self.assertIn('2026-10-09', page.schema[0]['datePublished'])
        self.assertIn('/images/posts/cover.webp', page.meta['og:image'])

    def test_homepage_links_to_newest_news(self):
        page = self.pages[ROOT / 'index.html']
        self.assertIn(BASE + '/2026/10/09/neurips-accepted-papers.html', page.links)


if __name__ == '__main__':
    unittest.main()
