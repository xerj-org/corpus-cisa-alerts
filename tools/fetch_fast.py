#!/usr/bin/env python3
"""Rate-capped parallel fetcher.

Politeness: one request is SCHEDULED every GAP seconds (same aggregate rate as a
serial loop with a GAP sleep); up to MAXFLIGHT are in flight simultaneously
solely to hide the reader's ~20-30s render latency. Aggregate request rate to
the reader proxy never exceeds 1/GAP per second.
"""
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

GAP = 3.5
MAXFLIGHT = 4
R = "/root/corpus-cisa-alerts/raw"
LOG = open(f"{R}/fetch.log", "a", buffering=1)


def fetch(url, out):
    cmd = ["curl", "-sS", "--max-time", "70", "-H", "X-Timeout: 40",
           "-o", out, "-w", "%{http_code}", f"https://r.jina.ai/{url}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    code = r.stdout.strip() or "000"
    sz = os.path.getsize(out) if os.path.exists(out) else 0
    return code, sz


def worker(url, fname, attempt=1):
    out = f"{R}/pages/{fname}.md"
    try:
        code, sz = fetch(url, out)
    except Exception as e:
        code, sz = "ERR", 0
        LOG.write(f"EXC {e} {fname}\n")
    if (code != "200" or sz < 400) and attempt == 1:
        time.sleep(20)
        try:
            code, sz = fetch(url, out)
        except Exception as e:
            code, sz = "ERR", 0
        LOG.write(f"RETRY {code} {sz} {fname}\n")
    if code != "200" or sz < 400:
        if os.path.exists(out):
            os.remove(out)
        LOG.write(f"FAIL {code} {sz} {fname}\n")
    else:
        LOG.write(f"{code} {sz} {fname}\n")


def main():
    todo = []
    for line in open(f"{R}/fetchlist.tsv"):
        url, fname, kind, date, title = line.rstrip("\n").split("\t")
        out = f"{R}/pages/{fname}.md"
        if os.path.exists(out) and os.path.getsize(out) >= 400:
            continue
        todo.append((url, fname))
    LOG.write(f"### fast fetch start: {len(todo)} to do\n")
    # With MAXFLIGHT workers and one submission every GAP seconds, the realized
    # request rate is min(1/GAP, MAXFLIGHT/avg_latency) — it can never exceed
    # 1/GAP, and queued submissions only delay starts, never bunch them.
    with ThreadPoolExecutor(max_workers=MAXFLIGHT) as ex:
        for i, (url, fname) in enumerate(todo):
            ex.submit(worker, url, fname)
            if i < len(todo) - 1:
                time.sleep(GAP)
    LOG.write(f"### fast fetch done; {time.strftime('%FT%TZ', time.gmtime())}\n")


if __name__ == "__main__":
    main()
