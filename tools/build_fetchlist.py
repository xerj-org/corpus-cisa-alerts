#!/usr/bin/env python3
"""Build the page-fetch list: every inventory advisory URL not already written
from a feed. Output: raw/fetchlist.tsv  (url TAB fname TAB type TAB date TAB title)
"""
import csv
import re
import os

def classify(url):
    slug = url.rstrip('/').rsplit('/', 1)[-1].lower()
    m = re.match(r'^(aa|icsa|icsma|mar|ar)-?(\d\d)-', slug)
    if m:
        kind = {'aa': 'aa', 'icsa': 'ics', 'icsma': 'ics-med', 'mar': 'aa', 'ar': 'aa'}[m.group(1)]
        return kind, slug
    if '/news-events/alerts/' in url:
        d = re.search(r'/alerts/(\d{4})/(\d{2})/(\d{2})/', url)
        return 'alert', f"{d.group(1)}-{d.group(2)}-{d.group(3)}-{slug}" if d else slug
    return 'aa', slug

inv = {}
for f in ["/root/corpus-cisa-alerts/raw/listing_manifest.tsv",
          "/root/corpus-cisa-alerts/raw/ics_listing_manifest.tsv"]:
    with open(f) as fh:
        r = csv.reader(fh, delimiter='\t')
        next(r)
        for row in r:
            if len(row) >= 6 and '/news-events/' in row[5]:
                inv.setdefault(row[5], {'kind': row[2], 'id': row[3], 'title': row[4], 'date': row[1]})

done = set(l.split('\t')[2] for l in open("/root/corpus-cisa-alerts/raw/manifest.tsv").read().splitlines() if l)

out = []
for url, meta in inv.items():
    if url in done:
        continue
    kind, fname = classify(url)
    out.append((url, fname, meta['kind'], meta['date'], meta['title']))

out.sort(key=lambda x: x[0])
os.makedirs("/root/corpus-cisa-alerts/raw/pages", exist_ok=True)
with open("/root/corpus-cisa-alerts/raw/fetchlist.tsv", "w") as fh:
    for row in out:
        fh.write("\t".join(row) + "\n")
print("to fetch:", len(out))
