#!/usr/bin/env python3
"""Parse a CISA RSS feed (rendered to markdown by a browser-grade reader) into
one markdown file per advisory item.

Usage: parse_feed.py <feed.md> <outdir-root> <manifest.tsv append-path>
Input format (r.jina.ai rendering of the XML):
    ### [Title](https://www.cisa.gov/news-events/...)
    <body>
    [url](url)
    Day, DD Mon YY HH:MM:SS +0000
"""
import re
import sys
import os
from datetime import datetime

MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}

ITEM_RE = re.compile(
    r'^### \[(.+?)\]\((https://www\.cisa\.gov/news-events/[a-z0-9\-/]+)\)\s*$',
    re.M)
DATE_RE = re.compile(
    r'^(\w{3}), (\d{1,2}) (\w{3}) (\d{2}|\d{4}) [\d:]+ (EDT|EST|UTC|\+0000)', re.M)
TAIL_LINK_RE = re.compile(r'^\[(https?://\S+?)\]\(\1\)\s*$', re.M)

FOREIGN_PARTNERS = [
    (r'Australian Signals Directorate|\bASD\b|Australian Cyber Security Centre|\bACSC\b',
     'ASD-Australia'),
    (r'NCSC-UK|National Cyber Security Centre \(UK\)|United Kingdom.?s National Cyber',
     'NCSC-UK'),
    (r'Canadian Centre for Cyber Security|\bCCCS\b|Communications Security Establishment',
     'CCCS-Canada'),
    (r'New Zealand.{0,60}(NCSC|GCSB)|Government Communications Security Bureau',
     'NZ-GCSB/NCSC'),
    (r'\bBSI\b|Bundesamt f.r Sicherheit', 'BSI-Germany'),
    (r'NCSC-NL|Netherlands.{0,40}(Cyber|NCSC)', 'NCSC-NL'),
    (r'CERT-EU', 'CERT-EU'),
    (r'\bANSSI\b|CERT-FR', 'ANSSI-France'),
    (r'JPCERT', 'JPCERT-Japan'),
    (r'SingCERT|Cyber Security Agency of Singapore', 'CSA-Singapore'),
    (r'CERT-UA', 'CERT-UA'),
    (r'NCSC-FI', 'NCSC-FI'),
    (r'National Cyber Security Centre', 'NCSC (unspecified)'),
]


def iso_date(m):
    mon = MONTHS.get(m.group(3))
    if not mon:
        return None
    y = int(m.group(4))
    if y < 100:
        y += 2000
    return f"{y:04d}-{mon:02d}-{int(m.group(2)):02d}"


def classify(url, title):
    slug = url.rstrip('/').rsplit('/', 1)[-1].lower()
    m = re.match(r'^(aa|icsa|icsma|mar|ta)-?(\d\d)-', slug)
    if m:
        kind = {'aa': 'aa', 'icsa': 'ics', 'icsma': 'ics-med', 'mar': 'aa', 'ta': 'alert'}[m.group(1)]
        return kind, slug, slug.upper()
    if '/news-events/alerts/' in url:
        d = re.search(r'/alerts/(\d{4})/(\d{2})/(\d{2})/', url)
        fname = f"{d.group(1)}-{d.group(2)}-{d.group(3)}-{slug}" if d else slug
        return 'alert', fname, None
    return 'aa', slug, None


def detect_partners(lines):
    region = lines[:40]
    context = [l for l in lines if re.search(
        r'publish|co-seal|joint|co-author|contribut|partner|written in collaboration', l, re.I)]
    scan = "\n".join(region + context)
    found = []
    for pat, name in FOREIGN_PARTNERS:
        if re.search(pat, scan, re.I):
            if name not in found:
                found.append(name)
    return ", ".join(found)


def yamlq(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def main(feedfile, root, manifest):
    text = open(feedfile, encoding='utf-8').read()
    # drop reader header
    text = re.sub(r'^Title: .*?\nURL Source: .*?\nMarkdown Content:\n', '', text, count=1, flags=re.S)
    matches = list(ITEM_RE.finditer(text))
    rows = []
    stats = {'written': 0, 'empty': 0, 'big': []}
    for i, m in enumerate(matches):
        title, url = m.group(1).strip(), m.group(2).strip()
        chunk = text[m.end(): matches[i + 1].start() if i + 1 < len(matches) else len(text)]
        # trailing "[url](url)" line + pubDate line(s) at chunk tail
        dm = list(DATE_RE.finditer(chunk))
        rdate = iso_date(dm[-1]) if dm else None
        body = chunk
        if dm:
            # cut at the LAST tail-link line if it precedes the final date
            tails = list(TAIL_LINK_RE.finditer(body[:dm[-1].start()]))
            if tails:
                body = body[:tails[-1].start()]
            else:
                body = body[:dm[-1].start()]
        # strip repeated trailing pubDate-only lines
        body = DATE_RE.sub('', body)
        body = TAIL_LINK_RE.sub('', body)
        body = re.sub(r'\n{3,}', '\n\n', body).strip()

        kind, fname, adv_id = classify(url, title)
        if rdate:
            year = rdate[:4]
        else:
            ym = re.search(r'[a-z]+-(\d\d)-', fname)
            if ym:
                year = '20' + ym.group(1)
            else:
                ym2 = re.search(r'/(\d{4})/', url)
                year = ym2.group(1) if ym2 else 'unknown'
        subdir = 'ics' if kind in ('ics', 'ics-med') else 'alerts'
        outdir = os.path.join(root, subdir, year)
        os.makedirs(outdir, exist_ok=True)
        outpath = os.path.join(outdir, fname + '.md')

        if not body or len(body) < 80:
            stats['empty'] += 1
            rows.append((fname, 'EMPTY', url))
            continue

        partners = detect_partners(body.splitlines())
        rev = None
        rm = re.search(r'Last Revised:?\s*([A-Z][a-z]+ \d{1,2}, \d{4})', body)
        if rm:
            rev = rm.group(1)

        fm = ['---', f"title: {yamlq(title)}", f"type: {kind}"]
        if adv_id:
            fm.append(f"id: {adv_id.upper()}")
        if rdate:
            fm.append(f"date: {rdate}")
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

    with open(manifest, 'a', encoding='utf-8') as f:
        for p, k, u in rows:
            f.write(f"{p}\t{k}\t{u}\n")
    print(feedfile, stats)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
