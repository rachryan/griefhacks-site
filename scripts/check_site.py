"""Check static pages and local links using only Python's standard library."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids, self.links, self.tags = [], [], Counter()
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.tags[tag] += 1
        if 'id' in values:
            self.ids.append(values['id'])
        for attribute in ('href', 'src'):
            if values.get(attribute):
                self.links.append(values[attribute])


pages = {path: Page(path.read_text()) for path in ROOT.rglob('*.html')}
errors, links = [], 0
for path, page in pages.items():
    label = path.relative_to(ROOT)
    for tag in ('html', 'head', 'body', 'main', 'h1', 'title'):
        if page.tags[tag] != 1:
            errors.append(f'{label}: expected one {tag}, found {page.tags[tag]}')
    if len(page.ids) != len(set(page.ids)):
        errors.append(f'{label}: duplicate IDs')
    for target in page.links:
        url = urlsplit(target)
        if url.scheme or url.netloc:
            continue
        links += 1
        resolved = (path.parent / unquote(url.path)).resolve() if url.path else path
        if resolved.is_dir():
            resolved /= 'index.html'
        if not resolved.exists():
            errors.append(f'{label}: missing {target}')
        elif url.fragment and resolved in pages and unquote(url.fragment) not in pages[resolved].ids:
            errors.append(f'{label}: missing anchor {target}')
    source = path.read_text()
    if 'YOUR_NEWSLETTER' in source or 'href="#"' in source:
        errors.append(f'{label}: placeholder link or form')

print(f'Checked {len(pages)} pages and {links} internal links/assets.')
print('\n'.join(errors) if errors else 'All checks passed.')
raise SystemExit(bool(errors))
