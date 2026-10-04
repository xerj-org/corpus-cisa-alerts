# corpus-cisa-alerts

CISA cybersecurity advisories mirrored as plain markdown, built as a reference
corpus for retrieval evaluation. Unofficial mirror — not affiliated with CISA.
The authoritative source is always
[www.cisa.gov/news-events/cybersecurity-advisories](https://www.cisa.gov/news-events/cybersecurity-advisories).

## Download date

2026-10-04 (UTC).

## Scope — exactly what was fetched

1. **RSS feeds** (embedded full text, one file per item, dedup by URL):
   - `https://www.cisa.gov/cybersecurity-advisories/all.xml` — 29 items
   - `https://www.cisa.gov/cybersecurity-advisories/ics-advisories.xml` — 30 items
   - `https://www.cisa.gov/cybersecurity-advisories/ics-medical-advisories.xml` — 30 items
   - 20 ICSA items overlapped between `all.xml` and `ics-advisories.xml`, giving
     **69 unique documents from feeds**.
2. **Backfill by listing walk** (newest-first, dedup by URL against feed items):
   - Main listing `https://www.cisa.gov/news-events/cybersecurity-advisories?page=N`
     — pages **0 through 21** (22 pages).
   - ICS listing `https://www.cisa.gov/news-events/ics-advisories?page=N` — pages
     **0 through 17** (18 pages). CISA's current site splits ICS advisories
     (incl. ICS medical) into this separate listing; the main listing no longer
     contains them.
   - Every advisory URL discovered this way that was not already covered by a
     feed was fetched individually (**334 pages**).

**Total: 403 documents.** This is a bounded, recent-window mirror
(2025-05 … 2026-10), not the full ~5,000-advisory archive.

Non-advisory items encountered in the main listing walk (20 resource/fact-sheet
publication cards under `/resources-tools/`) were skipped — they are not
advisories. Zero advisories were skipped for empty or access-restricted bodies.

## Counts

| type | files | meaning |
| --- | --- | --- |
| `alert` | 192 | `/news-events/alerts/…` (KEV-catalog additions, vendor alerts) |
| `aa` | 11 | `AA*` joint cybersecurity advisories + `AR*` analysis reports (id field retains `AR…`) |
| `ics` | 170 | `ICSA-*` ICS advisories |
| `ics-med` | 30 | `ICSMA-*` ICS medical advisories |

By year: 329 files from 2026, 74 from 2025. Largest file 136,699 bytes
(`ics/2026/icsa-26-188-05.md`); total ≈ 3.5 MB. `MANIFEST.tsv` lists
`path → type → source URL` for every file.

## Layout

- `alerts/<year>/<id>.md` — alerts and AA/AR advisories. Alert filenames are
  `<YYYY-MM-DD>-<slug>.md` (daily KEV alerts repeat slugs); AA/AR filenames are
  the advisory id, e.g. `alerts/2026/aa26-222a.md`.
- `ics/<year>/<id>.md` — ICSA and ICSMA advisories, e.g.
  `ics/2026/icsa-26-274-01.md`, `ics/2025/icsma-25-121-01.md`.

Each file begins with a front-matter header followed by the full advisory body:

    ---
    title: "#StopRansomware: Gunra Ransomware"
    type: aa                  # alert | aa | ics | ics-med
    id: AA26-222A             # advisory id when one exists
    date: 2026-08-10          # release/publication date
    source: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a
    revision: "2026-09-01"    # only when the page shows a later revision
    co-published: "ASD-Australia, NCSC-UK, ..."   # only when foreign partners are visible (see licence)
    ---

Tables (CVSS, affected products, MITRE ATT&CK TTPs, revision history) are kept
as GFM pipe tables where the source HTML allowed it.

## Licence

Works of the United States federal government are not subject to copyright in
the United States (17 USC 105). CISA advisories are US government works and are
in the public domain on that basis.

**Caveat.** Some advisories are co-published with foreign partners
(ASD-Australia, NCSC-UK, CCCS-Canada, NZ NCSC/GCSB, BSI-Germany, and others).
Contributions authored by partner-nation governments may carry their own
copyright status, which differs by nation and is not resolved by 17 USC 105.
Files where a foreign co-publisher is visible on the page carry a
`co-published:` header line naming the detected partners (9 files in this
snapshot). No licence is asserted over those files beyond the US
public-domain basis of CISA's own contribution. Detection is heuristic
(byline/authoring-agency text); absence of the header is not a guarantee that
no foreign contribution exists.

## Regeneration

`tools/` holds the pipeline used to build this snapshot:

1. **Fetch feeds** (browser-grade fetch, see constraint below):
   `curl -H "X-No-Cache: true" "https://r.jina.ai/<feed-url>" > raw/feed-X.md`,
   then `python3 tools/parse_feed.py raw/feed-X.md . raw/manifest.tsv` writes
   one file per feed item from the embedded full text.
2. **Walk listings** for the inventory (dates, ids, titles, URLs). Must use a
   JS-executing fetcher — see constraint. Walk main listing `?page=0..21` and
   ICS listing `?page=0..17`, newest-first, until the deduped union with feed
   URLs reaches the target size.
3. `python3 tools/build_fetchlist.py` — the URLs needing individual page fetches
   (inventory minus feed-covered).
4. **Fetch pages**: `tools/fetch_fast.py` (rate-capped: one request scheduled
   every 3.5 s, ≤4 in flight only to hide ~30 s render latency; aggregate rate
   never exceeds ~17 req/min). `tools/fetch_loop.sh` is the strictly-serial
   equivalent.
5. `python3 tools/clean_page.py` — strips the reader header, extracts
   front-matter (title/id/date/revision/co-publishers), writes the final files.
6. `python3 tools/build_manifest.py` — dedups the run manifest into
   `MANIFEST.tsv` and prints the counts.

## Fetcher constraint (important)

`www.cisa.gov` serves **HTTP 403 to non-browser clients** (Akamai TLS
fingerprinting) — plain `curl` with a browser user-agent is still rejected, so
every fetch must go through a browser-grade fetcher. This snapshot used the
Jina reader (`r.jina.ai`) for feeds and advisory pages, and a JS-executing
fetch tool for listing pages (the current CISA listing paginates via
JavaScript; static fetches of `?page=N` silently return page 1 regardless of
`N`).

Two traps: the reader's own API uses a `page` query parameter, so a CISA URL
like `…advisories?page=3` collides with it — URL-encoding does not help and the
target URL must be passed in the request body; and the reader serves stale
cached copies unless `X-No-Cache: true` is sent (a cached July-2025 copy of the
listing was served in October 2026). `X-No-Cache` costs ~10× latency (~30 s per
page vs ~3 s cached); it was used for the three feeds, and per-page fetches
relied on the reader's fresh crawl of URLs not previously cached.

Politeness: all fetching was rate-capped (≤ ~17 requests/min, single upstream
crawl per document) and retried at most once per URL.
