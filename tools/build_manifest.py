#!/usr/bin/env python3
"""Dedup raw/manifest.tsv into the published MANIFEST.tsv and print counts."""
import os
from collections import Counter

ROOT = "/root/corpus-cisa-alerts"
by_url = {}
for line in open(f"{ROOT}/raw/manifest.tsv"):
    p, k, u = line.rstrip("\n").split("\t")
    p = os.path.normpath(p)
    if p.startswith(ROOT + "/"):
        p = p[len(ROOT) + 1:]
    if k in ("EMPTY", "MISSING"):
        by_url.setdefault(u, {"skip": k})
        continue
    e = by_url.setdefault(u, {})
    if p.startswith(("alerts/", "ics/")) and os.path.exists(os.path.join(ROOT, p)):
        e.update({"p": p, "k": k})

final = sorted((e["p"], e["k"], u) for u, e in by_url.items() if "p" in e)
skipped = [(u, e.get("skip")) for u, e in by_url.items() if "p" not in e]

with open(f"{ROOT}/MANIFEST.tsv", "w") as f:
    f.write("path\ttype\tsource_url\n")
    for p, k, u in final:
        f.write(f"{p}\t{k}\t{u}\n")

print("manifest rows:", len(final), "| skipped:", len(skipped), skipped[:10])
print("by type:", dict(Counter(k for _, k, _ in final)))
on_disk = sorted(
    os.path.join(dp, fn)[len(ROOT) + 1:]
    for dp, _, fns in os.walk(f"{ROOT}/alerts") for fn in fns
) + sorted(
    os.path.join(dp, fn)[len(ROOT) + 1:]
    for dp, _, fns in os.walk(f"{ROOT}/ics") for fn in fns
)
mset = set(p for p, _, _ in final)
print("files on disk:", len(on_disk))
print("in manifest not on disk:", len(mset - set(on_disk)))
print("on disk not in manifest:", sorted(set(on_disk) - mset)[:10])
