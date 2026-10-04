#!/bin/bash
# Serial, polite fetcher for advisory pages through the reader proxy.
R=/root/corpus-cisa-alerts/raw
LOG=$R/fetch.log
while IFS=$'\t' read -r url fname kind date title; do
  out=$R/pages/$fname.md
  if [ -s "$out" ] && [ "$(wc -c < "$out")" -ge 400 ]; then
    echo "SKIP $fname" >> "$LOG"
    continue
  fi
  code=$(curl -sS --max-time 60 -H "X-Timeout: 30" -o "$out" -w "%{http_code}" "https://r.jina.ai/$url" 2>>"$LOG")
  sz=$(wc -c < "$out" 2>/dev/null || echo 0)
  echo "$code $sz $fname" >> "$LOG"
  if [ "$code" != "200" ] || [ "$sz" -lt 400 ]; then
    sleep 15
    code=$(curl -sS --max-time 60 -H "X-Timeout: 30" -o "$out" -w "%{http_code}" "https://r.jina.ai/$url" 2>>"$LOG")
    sz=$(wc -c < "$out" 2>/dev/null || echo 0)
    echo "RETRY $code $sz $fname" >> "$LOG"
    if [ "$code" != "200" ]; then rm -f "$out"; fi
  fi
  sleep 2
done < $R/fetchlist.tsv
echo "DONE $(date -u +%FT%TZ)" >> "$LOG"
