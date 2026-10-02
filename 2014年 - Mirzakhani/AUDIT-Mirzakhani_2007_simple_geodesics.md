# Audit — Mirzakhani, “Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces”

- Actor: `Peer-P17`
- Model / reasoning effort: `gpt-6-luna` / `max`
- Base: `037602429d3b009f6fc468c732073eb3ddf9875f` (detached worktree at assignment start)
- Source PDF: `Mirzakhani_2007_simple_geodesics.pdf` (49 PDF pages; born-digital text layer)
- MinerU Markdown: `Mirzakhani_2007_simple_geodesics__Mirzakhani_2007_simple_geodesics.md`
- Markdown SHA-256 before repair: `8a25671e129778297a28a3bd960138a06e523fe6a1c6089558008ec379369c17`

## Overall assessment (in progress)

The page-by-page source comparison is in progress. The PDF has a 109,053-byte extractable text layer with no U+FFFD characters. Text extraction is the primary comparison channel; visual checks are recorded where performed. No Markdown repair will be made until all 49 PDF pages have been audited.

## Page-by-page audit

### p.001 (PDF p.1 / printed p.1)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p001.png` (pngmono, 150 dpi; title/contents page visually inspected)
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: title, author, date, contents entries 1–9, and the opening paragraph through the end of PDF p.1; compared the PDF text layer with the corresponding MinerU text.
- Result: `PASS±`. Title, author, date and contents match. In the opening paragraph, MinerU has `efective` for printed `effective` and `coeficients` for printed `coefficients`; the source page image and text layer confirm the printed spellings. These are OCR spelling artifacts with no change to the mathematical statement.

### p.002 (PDF p.2 / printed p.2)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p002.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_p002_epsilon-thin.png`; `audit/300dpi/Mirzakhani_2007_simple_geodesics_p002_boundary-domain.png`.
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: continuation of the introduction, the statement and formula of Theorem 1.1, its multi-index definitions, the `V_{1,1}(L)` example, and the following paragraph and normalization remark; compared the PDF text layer and both symbol crops with the corresponding MinerU text.
- Result: `FAIL`. MinerU drops the printed `ε` in “ε-thin part”; changes the boundary-length domain from `(R_{≥0})^n` to `(R_{>0})^n`; inserts an extraneous `9` after the multi-index domain; and splits the printed denominator `24` in `V_{1,1}(L)=L^2/24+π^2/6` as `2 4`. The 300 dpi crops confirm the ε and inclusive-boundary symbols. Minor `PASS±` artifacts on this page include the misspelling `diference` and a duplicated trailing `Q` after the coefficient field.

### p.003 (PDF p.3 / printed p.3)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p003.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_p003_table1.png`; `audit/300dpi/Mirzakhani_2007_simple_geodesics_p003_eq-1.1.png`.
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: Table 1 volume formulas, continuation of the normalization remark, and Theorem 1.2 / equation (1.1); compared the table and equation crop against MinerU, including symbols that the PDF text layer did not extract reliably.
- Result: `PASS±`. Table 1 and equation (1.1) agree with the print, including the `1/24` coefficient and exponent `\ell_\gamma(X)` in McShane's identity. The PDF text extraction renders the length symbol as a control character in (1.1); the 300 dpi crop confirms the printed `\ell_\gamma(X)`, which MinerU transcribes correctly. The continuation of the remark has the OCR misspelling `diferent` for printed `different`; it does not change a mathematical statement.

### p.004 (PDF p.4 / printed p.4)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p004.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_p004_eq-1.2.png`; `audit/300dpi/Mirzakhani_2007_simple_geodesics_p004_volume.png`.
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: equation (1.2), the once-punctured-torus covering and Fenchel–Nielsen coordinate statements, the Weil–Petersson form, the iterated integral, and the `Vol(M_{1,1})` evaluation; compared the PDF text layer and crops with the corresponding MinerU text.
- Result: `PASS±`. The formulas and relation `Vol(M_{1,1}) = π^2/6` match. The PDF text extraction emits a control character for several printed length symbols; the 300 dpi crops confirm the corresponding `\ell` terms and their MinerU transcription. MinerU renders printed blackboard-bold `\mathbb{R}` as plain `R` in the codomain, a font-style loss that does not change the stated set.

### p.005 (PDF p.5 / printed p.5)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p005.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_p005_aux-functions.png`; `audit/300dpi/Mirzakhani_2007_simple_geodesics_p005_eqs-1.3-1.4.png`.
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: outline of the two proof steps, auxiliary-function types, Theorem 1.3 / equations (1.3)–(1.4), and the `x → 0` asymptotic for `D`; compared the source page, text layer, crops, and corresponding MinerU text.
- Result: `FAIL`. The printed type is `\mathbb{R}_+^3 \to \mathbb{R}_+`, but MinerU omits the map arrow and leaves adjacent domain and codomain expressions. The 300 dpi crop confirms the arrow. Equations (1.3), (1.4), and the asymptotic formula otherwise match, including the length symbols rendered unreliably by the PDF text layer. Minor artifacts include lost section signs before references to Sections 3 and 4; the section numbers themselves match.

### p.006 (PDF p.6 / printed p.6)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p006.png` (pngmono, 150 dpi).
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: the orbit definition, the function `f_γ`, the covering-space length function, and the two integral identities on this page; compared the PDF text layer with the corresponding MinerU text.
- Result: `FAIL`. The PDF reads “the `Mod_{g,n}`-orbit of `γ`”; MinerU instead renders the group with an extraneous superscript `−0` and leaves `rbit`, omitting the initial `o`. This corrupts the stated mapping-class-group orbit. The PDF text extractor encodes several printed length symbols as a control character, while MinerU's `\ell` transcriptions match the surrounding formulas. The section sign before the reference to Section 8 is also omitted, but the section number is present.

### p.007 (PDF p.7 / printed p.7)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p007.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_p007_print-quirk-eq-1.5.png`.
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: the cutting/circle-bundle description, quotient and fiber-volume formulas, equation (1.5), and the definition of `M(γ)`; compared the PDF text layer and 300 dpi crop with the corresponding MinerU text.
- Result: `FAIL`. In two places the print says `seperates off a one-handle`, while MinerU has `seperates of a one-handle`, dropping the final `f` from `off`; this changes the condition defining `M(γ)` and the preceding topological case. The source print itself spells `seperates` (with `e`), which is recorded as a print quirk and will be preserved. Equation (1.5) and its `2^{-M(γ)}` factor otherwise match. A separate spelling artifact is `diferent` for printed `different`.

### p.008 (PDF p.8 / printed p.8)

- Evidence: `audit/Mirzakhani_2007_simple_geodesics_p008.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_p008_acknowledgment-name.png`.
- Actor / model / effort: `Peer-P17` / `gpt-6-luna` / `max`
- Checked: the alternative-proof continuation, applications, references, acknowledgments, and the start of Section 2 through the definition of a non-degenerate form; compared the PDF text layer and the 300 dpi name crop with MinerU.
- Result: `PASS±`. No mathematical-content difference was found on this page. MinerU has spelling artifacts `coeficients` and `diferent`, and drops the section sign before §5; the referenced numbers remain intact. The 300 dpi crop confirms the print-level forms `Pandharipandeh` and `dscussions`, both faithfully retained in MinerU; preserve these source quirks.
