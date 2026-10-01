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

### p.003 (PDF p.3 / print p.281)

- PNG: `audit/p003.png` (150-dpi `pngmono`); glyph crop: `audit/300dpi/p003-bundle-map.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 15:54:31 EDT
- Markdown segment: lines 53–101, from the continuation “union of X...” through the line ending “The curvature F(A) of any”.
- Compared: end of the moduli-space boundary description; Lemma 2 and its two displayed decompositions and signature calculation; start of section I.3; bundle notation, connection-space definition, and differential-operator formula.
- Result: **FAIL**. At Markdown line 89 the source diagram `P ↓ X` identifying the total space and base of the principal bundle is reduced to `\downarrow`; both labels `P` and `X` are lost. The 300-dpi crop confirms the printed diagram. The other checked mathematical statements match. The printed running header and folio `281` are absent from the Markdown.

### p.004 (PDF p.4 / print p.282)

- PNG: `audit/p004.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 15:55:44 EDT
- Markdown segment: lines 103–153, from “connection is an element of” through the decomposition `Ω² = Ω⁺² ⊕ Ω⁻²`.
- Compared: curvature expansion; gauge-group action; `SU(2)` and `U(1)` bundle classification; Proposition 3 and its curvature formula; the `c₂` and relative `Tc₂` formulas; start of the self-dual/anti-self-dual decomposition.
- Result: **PASS±**. The mathematical text and displayed formulas match the page image. The Markdown omits the running author header and printed folio `282`.

### p.005 (PDF p.5 / print p.283)

- PNG: `audit/p005.png` (150-dpi `pngmono`); glyph crop: `audit/300dpi/p005-bundle-map.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 15:56:44 EDT
- Markdown segment: lines 155–199, from the definition of the self-dual and anti-self-dual subspaces through the bundle assumption at the end of the page.
- Compared: equation (1); curvature splitting; Yang–Mills action and Chern-class identities; flat-connection conclusion; `d⁻` and `d_A⁻`; Laplacians, harmonic spaces, and the elliptic complex.
- Result: **FAIL**. At Markdown line 199 the printed diagram `P ↓ X` is reduced to `\downarrow`, omitting the bundle total space `P` and base `X`. The 300-dpi crop confirms the labels. The remaining checked equations and prose match; the running header and printed folio `283` are absent from the Markdown.

### p.006 (PDF p.6 / print p.284)

- PNG: `audit/p006.png` (150-dpi `pngmono`); diagram crop: `audit/300dpi/p006-bundle-maps.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 15:57:45 EDT
- Markdown segment: lines 201–229, from section I.4 through the final word “conformal”.
- Compared: instanton action and equation (2); Proposition 4 and finite-action integral; classification of the S⁴ instanton orbit and its moduli space.
- Result: **FAIL**. The 300-dpi crop shows the first printed `P` above the arrow after “connection on”; Markdown line 229 retains only `\downarrow`. It also shows the following fibration diagram `S⁷ ↓ S⁴`, whose two labels are absent from the Markdown's lone `\downarrow`. The Markdown additionally attaches `S⁷` as a subscript in `SO(5)^{S^4}_{S^7}`; on the printed page `S⁷` labels the following fibration diagram, while `S⁴` is the superscript on `SO(5)`. The other checked statements and formulas match. The running header and folio `284` are omitted.

### p.007 (PDF p.7 / print p.285)

- PNG: `audit/p007.png` (150-dpi `pngmono`); 300-dpi crops: `audit/300dpi/p007-curvature-formula.png`, `audit/300dpi/p007-bundle-map.png`
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:00:56 EDT
- Markdown segment: lines 231–259, from “group acts by translations...” through Proposition 5 ending “the”.
- Compared: instanton connection matrix and curvature; compactification/moduli-space description; Hodge decomposition and quadratic-form integral; Taubes statement and Proposition 5 opening.
- Result: **FAIL**. Proposition 5's printed bundle diagram is `P ↓ X`, but Markdown line 259 retains only `\downarrow`, omitting both labels; the 300-dpi bundle crop confirms this. The 300-dpi curvature crop confirms the printed denominator `(λ² + |x|)²` in `F(I_{0,λ})`; Markdown has the same expression. This is a print-level formula quirk and is deliberately preserved, not silently corrected to a mathematically expected variant. The other checked material matches; the running header and folio `285` are omitted.

### p.008 (PDF p.8 / print p.286)

- PNG: `audit/p008.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:02:39 EDT
- Markdown segment: lines 261–297, from Proposition 5's `L³`-norm continuation through the quotient-space notation and explanatory paragraph.
- Compared: Proposition 5's hypotheses, δ expression and estimates; Taubes' concentration construction; the `U(1)` uniqueness observation; Sobolev-space definition and norm; the moduli-space quotient and map notation.
- Result: **PASS±**. The mathematical text and formulas match. Markdown lines 279 and 281 split the single printed II.1 heading across two `##` headings, leaving “and properties of the space B” as a stray heading; this impairs section navigation and is a candidate for the post-audit Edit repair. The running author header and folio `286` are absent.
