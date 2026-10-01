# 1986 — Donaldson, “An Application of Gauge Theory to Four-Dimensional Topology”

- Actor: `Peer-P03`
- Model / effort: `gpt-6-luna` / `max`
- Role: contributor; canonical integrator is `Master-Luna`
- Candidate base: `e04c4a9603818cfa2d71271942f696115783c33b`
- PDF: `Donaldson_1983_gauge_theory_4manifolds.pdf` — 38 pages; SHA-256 `5a5201ed38b870ec1ad183b697aa505830c5a35bf03d72614a5bb1667fe65080`
- MinerU Markdown: `Donaldson_1983_gauge_theory_4manifolds_mineru/Donaldson_1983_gauge_theory_4manifolds__Donaldson_1983_gauge_theory_4manifolds.md`
- Initial Markdown SHA-256: `572bdf3556bfe85b58518518583a14174e7af9ec88b6725b627dba889cff3913`
- Initial Markdown full-read: 1,454 lines, read before page audit; repair status will be re-read from byte 1 after edits.
- Export identity: nested `middle_json.json` reports MinerU 3.4.4, schema 2.0, `is_full_document=true`, and 38 page records (`page_idx` 0–37); its metadata has no `doc_id` field. The PDF page count and ordered page records agree.
- Source mode: scanned, not born-digital. `pdfimages -list` shows one approximately 3900×6000, 600-dpi, 1-bit page image on each of the 38 pages. The ABBYY OCR text layer is 76,730 bytes with no U+FFFD; it is a locator only, not authority over the printed page.
- Method: render each PDF page as a 150-dpi `pngmono`, inspect the complete page, compare its contents with the corresponding ordered Markdown segment and original page image, and use 300-dpi crops for glyph-level ambiguities. PDF print is authoritative. No MinerU service or parser was run.
- Markdown source chain at audit start: the file is clean at base `e04c4a9603818cfa2d71271942f696115783c33b`; its last touching commit is `0b0f3dd2`. The exact pre-repair parent will be recorded with any `fix(md)` commit.

## Page sign-offs

### p.001 (PDF p.1 / print p.279 inferred from the article range; opening page carries no separate page numeral)

- PNG: `audit/p001.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 15:50:42 EDT
- Markdown segment: lines 1–21, from title and author through the end of the introduction and the “Received December 31, 1982” footnote; `Theorem 1` at line 23 begins the next PDF page.
- Compared: journal/range header; title and author; section heading; opening-page prose, displayed cup-square, references [7], [8], [11], [12], closing introduction paragraph, and received-date footnote.
- Result: **PASS±**. The title, author, body text, and received date match the printed page. The Markdown omits the printed header `J. DIFFERENTIAL GEOMETRY 18 (1983) 279–315`; the opening page has no separate printed page numeral. The PDF text layer misreads the displayed `E₈` glyph as `£ 8`, while the Markdown has `E_8`; the page image confirms the Markdown reading. Header omission is logged as a retrieval/bibliographic limitation, not as a body-text error.

### p.002 (PDF p.2 / print p.280)

- PNG: `audit/p002.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 15:52:28 EDT
- Markdown segment: lines 23–51, from Theorem 1 through the paragraph ending “the disjoint”; line 53 continues the sentence on PDF p.3.
- Compared: theorem statement and diagonal-form equation; the `2mE₈+n[[0,1],[1,0]]` form; the smoothing discussion; the `π₁(X) → SU(2)` condition; acknowledgement; section I.2 and its moduli-space description through the page break.
- Result: **PASS±**. The body and displayed equations match the page image. The Markdown omits the running header and printed folio `280`. The print phrase “in some base” is retained verbatim in the Markdown; it is a source-level wording quirk, not an OCR discrepancy.
