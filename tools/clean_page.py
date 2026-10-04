#!/usr/bin/env python3
"""Clean fetched advisory pages (reader markdown) into final corpus files.

Reads raw/fetchlist.tsv; for each row, if raw/pages/<fname>.md exists, strip the
reader header, extract front-matter fields, detect foreign co-publishers, and
write <alerts|ics>/<year>/<fname>.md. Appends rows to raw/manifest.tsv.
"""
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_feed import detect_partners, yamlq  # reuse

ROOT = "/root/corpus-cisa-alerts"
CUT_MARKERS = ["Return to top", "Was this helpful", "Website Feedback",
               "Give Feedback", "An official website of the U.S. Department"]


MONTHS = {m: i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"])}


def to_iso(s):
    m = re.match(r'([A-Z][a-z]+) (\d{1,2}), (\d{4})$', s or '')
    if m and m.group(1) in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"
    return s


def page_date(text, fallback):
    m = re.search(r'\*\*Original Release Date:\*\*\s*(\d{4}-\d{2}-\d{2})', text)
    if m:
        return m.group(1)
    for pat in [r'\|\s*Original Publication\s*\|\s*([A-Z][a-z]+ \d{1,2}, \d{4})',
                r'\*\*Update ([A-Z][a-z]+ \d{1,2}, \d{4}):?\*\*']:
        m = re.search(pat, text)
        if m:
            return to_iso(m.group(1))
    return fallback


def revision_of(text):
    # revision-history table rows with revision number >= 2
    best = None
    for m in re.finditer(r'^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\d+)\s*\|', text, re.M):
        if int(m.group(2)) >= 2:
            if not best or m.group(1) > best:
                best = m.group(1)
    if best:
        return best
    m = re.search(r'Last Revised:?\s*([A-Z][a-z]+ \d{1,2}, \d{4})', text)
    if m:
        return m.group(1)
    m = re.search(r'\*\*Update ([A-Z][a-z]+ \d{1,2}, \d{4}):?\*\*', text)
    if m:
        return m.group(1)
    return None


def main():
    stats = {'written': 0, 'missing': 0, 'empty': 0, 'big': [], 'restricted': 0}
    rows = []
    with open(f"{ROOT}/raw/fetchlist.tsv") as fh:
        fetch = [l.rstrip('\n').split('\t') for l in fh if l.strip()]
    for url, fname, kind_label, mdate, mtitle in fetch:
        rawp = f"{ROOT}/raw/pages/{fname}.md"
        if not os.path.exists(rawp):
            stats['missing'] += 1
            rows.append((fname, 'MISSING', url))
            continue
        text = open(rawp, encoding='utf-8').read()
        # strip reader header
        m = re.match(r'^Title: (.*?)\n+URL Source: \S+\n+Markdown Content:\n', text, re.S)
        title = None
        if m:
            title = m.group(1).strip()
            body = text[m.end():]
        else:
            body = text
        if title and title.endswith(' | CISA'):
            title = title[:-len(' | CISA')]
        # cut trailing site chrome if any
        for marker in CUT_MARKERS:
            i = body.find(marker)
            if i > 200:
                body = body[:i]
        body = re.sub(r'\n{3,}', '\n\n', body).strip()

        if len(body) < 80 or re.search(r'^(Access Denied|Page Not Found)', body[:60], re.I):
            stats['empty'] += 1
            rows.append((fname, 'EMPTY', url))
            continue

        kind, _ = classify_url(url)
        adv_id = None
        m = re.match(r'^(aa|icsa|icsma|mar|ar)-?(\d\d)-', fname)
        if m:
            adv_id = fname.upper()
        date = page_date(body, mdate)
        if date and re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            year = date[:4]
        elif m:
            year = '20' + m.group(2)
        elif mdate:
            year = mdate[:4]
        else:
            year = 'unknown'
        subdir = 'ics' if kind in ('ics', 'ics-med') else 'alerts'
        outdir = os.path.join(ROOT, subdir, year)
        os.makedirs(outdir, exist_ok=True)
        outpath = os.path.join(outdir, fname + '.md')

        title = title or mtitle
        partners = detect_partners(body.splitlines())
        rev = revision_of(body)

        fm = ['---', f"title: {yamlq(title)}", f"type: {kind}"]
        if adv_id:
            fm.append(f"id: {adv_id.upper()}")
        if date:
            fm.append(f"date: {date}")
        fm.append(f"source: {url}")
        if rev:
            fm.append(f"revision: \"{rev}\"")
        if partners:
            fm.append(f"co-published: {yamlq(partners)}")
        fm += ['---', '']
        doc = "\n".join(fm) + body + "\n"
        if len(doc.encode()) > 150_000:
            stats['big'].append(outpath)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(doc)
        stats['written'] += 1
        rows.append((outpath, kind, url))

    with open(f"{ROOT}/raw/manifest.tsv", 'a') as f:
        for p, k, u in rows:
            f.write(f"{p}\t{k}\t{u}\n")
    print(stats)


def classify_url(url):
    slug = url.rstrip('/').rsplit('/', 1)[-1].lower()
    m = re.match(r'^(aa|icsa|icsma|mar|ar)-?(\d\d)-', slug)
    if m:
        return {'aa': 'aa', 'icsa': 'ics', 'icsma': 'ics-med', 'mar': 'aa', 'ar': 'aa'}[m.group(1)], slug
    if '/news-events/alerts/' in url:
        d = re.search(r'/alerts/(\d{4})/(\d{2})/(\d{2})/', url)
        return 'alert', (f"{d.group(1)}-{d.group(2)}-{d.group(3)}-{slug}" if d else slug)
    return 'aa', slug


if __name__ == '__main__':
    main()
