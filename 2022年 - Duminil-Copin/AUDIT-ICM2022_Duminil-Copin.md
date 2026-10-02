# ICM2022 proceedings — Martin Hairer and the ICM 2022 paper by Hugo Duminil-Copin

- Actor: `Peer-P14`
- Model: `gpt-6-luna`
- Reasoning effort: `max`
- Source PDF: `ICM2022_proceedings_Duminil-Copin.pdf` (46 pages; `pdfinfo`)
- MinerU Markdown: `ICM2022_proceedings_Duminil-Copin_mineru/ICM2022_proceedings_Duminil-Copin__ICM2022_proceedings_Duminil-Copin.md`
- Source mode: born-digital, produced by pdfTeX; the PDF text layer contains 134,265 characters, 46 page separators, and no U+FFFD. All 46 pages were reconciled against the PDF text layer and the corresponding retained 150 dpi pngmono page image; disputed symbols and figures were adjudicated against retained 300 dpi crops.
- MinerU doc_id: not found in the checked export; no doc_id/docId field was found in this paper’s current _mineru tree.
- Status: 46/46 page audits complete (42 FAIL, 4 PASS±); the Markdown repairs and final full-file reread are complete in this contributor candidate. Canonical integration remains pending.

## Overall review

- Result: 46 PDF pages audited; p.3, p.11, p.14, and p.17 are PASS±; the remaining 42 pages are FAIL. No page received PASS.
- Coverage: all 46 page images are retained under audit/; the page records link the 300 dpi arbitration crops, including source-derived Figure 1–3 crops. Born-digital text-layer comparison was used across the document, with visual adjudication for mathematical symbols and figures.
- Source-level quirks were preserved and are recorded in the page entries: equation (2.4) prints H_{G,β,h} after the p.4 definition of H_{G,h}; p.7 retains the printed wording “the fact that β large renders”; p.10 retains “represented more than for his physical relevance”; equation (4.7) retains the printed exponent d−2+δ; p.18 retains the printed μ_{G,β,0}/μ_{G,β,h} mismatch; and references [82] and [87] retain punctuation duplicated in print. PASS± ligature and line-break artifacts were not batch-cleaned.

## Page-by-page audit

### PDF p.001 / title page

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p001.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p001_dedication_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:11:47 EDT.
- Compared title, author, dedication, abstract, MSC classification, keywords, and publication footer against PDF p.1 text layer and the page image.
- Print evidence: the dedication reads “Dedicated to the memory of colleagues and friends Dmitry Ioffe and Vladas Sidoravicius”; the footer gives © 2022 International Mathematical Union, the preliminary-proceedings statement, and DOI `10.4171/ICM2022/204`.
- Result: **FAIL** — Markdown joins “of colleagues” and “and friends”, transcribes `Ioffe` as `Iofe`, and omits the publication footer including the DOI. Title, author, abstract, MSC classification, and keywords agree. “Iofe” is an OCR spelling error, not a print quirk; correct after the full page audit.

### PDF p.002 / printed p.2

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p002.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:13:52 EDT.
- Compared the complete PDF text layer for the remainder of §1 and the opening of §2.1 against the corresponding Markdown passage, including section sequence and the printed page break within the Curie sentence.
- Print evidence: the review-history paragraph names “Kadanoff’s scaling and universality hypotheses” and “differential inequalities”; the page ends with “when an external” and continues on printed p.3.
- Result: **FAIL** — Markdown has `Kadanof’s`, losing one `f` in the mathematician’s surname. It also has the non-misleading `diferent` and `diferential` spellings from the `ff` ligature; references `[20,86]` collapse a space. All prose and the page-break continuation are present. The running head/page number are absent from Markdown. Correct the surname after the full page audit; record the other typography artifacts as PASS± unless a later context makes them misleading.

### PDF p.003 / printed p.3

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p003.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:15:28 EDT.
- Compared the PDF text layer from the continuation of the Curie-temperature sentence through the account of Ising’s assumptions and the beginning of the consequence paragraph.
- Print evidence: the page contains the phase-transition continuation, Curie/Weiss account, Lenz’s two-direction assumption, and Ising’s nearest-neighbour and linear-chain assumptions; it ends after “irrespective of the tempera-”.
- Result: **PASS±** — prose is present in sequence, including the sentence crossing the page boundary. The clear `efficient`→`eficient` `ff`-ligature OCR spelling is non-misleading; retain as PASS± absent a content-critical context. Printed running head and page number are not represented in Markdown.

### PDF p.004 / printed p.4

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p004.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p004_equations_2_1-2_3_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:17:09 EDT.
- Compared the end of the Ising biography and §2.2 formal definition through equation (2.3), including the graph, spin, Hamiltonian, coupling, and partition-function notation. The page image and crop were visually inspected as a dense mathematics sample.
- Print evidence: the definition reads `G = (V,E)`, vertex-set `V`, edge-set `E`, edge endpoints `x,y`, spin `σ_x` at `x`, and all equation tags `(2.1)`–`(2.3)` are printed.
- Result: **FAIL** — Markdown replaces the occurrences of `V`, `E`, `x`, `y`, and `G` in the definition prose with `�`; it also transcribes “model” as “mode” and renders “Dr. Wolfgang Pauli” in the quotation as `$D r$Wolfgang Pauli`. The mathematical bodies and tags `(2.1)`–`(2.3)` otherwise agree. Repair the missing symbols and the two text errors after all pages have been audited.

### PDF p.005 / printed p.5

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p005.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p005_equations_2_4-2_7_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:18:30 EDT.
- Compared the remainder of §2.2 and equations (2.4)–(2.7), then the opening two paragraphs of §2.3. The page image/crop were visually inspected as a dense mathematics sample.
- Print evidence: the text says “the `d`-dimensional Ising model” and “`m(β,h)` decreases as `h` decreases”; equations `(2.4)`–`(2.7)` appear in sequence.
- Result: **FAIL** — Markdown replaces `d` in “the �-dimensional Ising model” and `m` in “�(β,h)” with U+FFFD. The equations and surrounding §2.3 prose otherwise match through the page break. In equation `(2.4)`, print has `H_{G,β,h}` although p.4 defined `H_{G,h}`; Markdown reproduces the p.5 print form, so retain it and list it as a source-level notation quirk (intent unknown). The printed running head/page number are omitted from Markdown.

### PDF p.006 / printed p.6

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p006.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p006_peierls_E_sigma_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:20:01 EDT.
- Compared the end of §2.3 and the opening of Peierls’ argument through the description of the edge set. The source text layer and 300 dpi crop show the same boundary passage.
- Print evidence: the argument associates a subset `E(σ)` of graph edges `{x,y}` for which `σ_x ≠ σ_y`; the page ends as it turns to drawing those edges in the planar context.
- Result: **FAIL** — Markdown renders that set as `�(�)`, losing both `E` and `σ`. It also joins `Rudolf` and `Peierls` in the name `RudolfPeierls`; the `different`→`diferent` spellings are non-misleading `ff`-ligature artifacts. Correct the missing notation and spacing after the full audit. Printed running head/page number are absent from Markdown.

### PDF p.007 / printed p.7

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p007.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p007_peierls_equations_footnote_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:22:17 EDT.
- Compared the remainder of the low-temperature expansion, equation `(2.8)`, Frame 1 through its flip bound, and footnote 1 against PDF p.7 text layer and the 300 dpi image crop.
- Print evidence: equation `(2.8)`, Frame 1 equation `(2.9)`, and the flip inequality are present. Footnote 1 defines `G*=(V*,E*)`, the dual-edge map `e ↦ e*`, the bijection `E ↔ E*`, and the square-lattice translation by `(1/2,1/2)`.
- Result: **FAIL** — Markdown inserts `\boldsymbol{\cdot}` before `β` in the prose (“the fact that β large renders…”), and footnote 1 is fragmented across docvortex spans with multiple defining symbols (`G`, `V`, `E`, `u`, `v`, `e`) replaced by `�` or omitted. Equation `(2.8)`, equation `(2.9)`, and the flip-bound formula match. Rebuild the footnote manually from the printed text after the full audit; remove the spurious bullet after checking the exact source. The printed running head/page number are omitted from Markdown.

### PDF p.008 / printed p.8

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p008.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:24:28 EDT.
- Compared the closing Peierls bound `(2.10)`, §3.1 opening, and equations `(3.1)`–`(3.3)` with the complete PDF p.8 text layer and page image.
- Print evidence: the section title reads “The integrability of the Ising model”; the three equations and their tags are printed in order, with the duality relation as the final content on p.8.
- Result: **FAIL** — Markdown changes `model` to `mode` in the §3 heading. The compared formulas `(2.10)` and `(3.1)`–`(3.3)` match print; the figure and caption referenced after `(3.3)` in Markdown belong to source PDF p.9, not this page. Printed running head/page number are omitted.

### PDF p.009 / printed p.9

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p009.png` (150 dpi, pngmono).
- Figure 1 source crop: `audit/ICM2022_proceedings_Duminil-Copin_p009_Figure1.png` (300 dpi, grayscale; printed diagram only, caption excluded).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:26:21 EDT.
- Compared printed Figure 1 and caption, the duality continuation, and Frame 2 through equation `(3.4)`. The source page and figure crop were visually inspected; the existing nested MinerU JPEG depicts the same two diagrams but is not at the relative path used by the Markdown.
- Print evidence: the caption reads “The set `S(5,3)`…” and says `τ` and `\bar{τ}` are respectively constant at `−1` and `+1`. Frame 2 introduces “the quantity” before equation `(3.4)`.
- Result: **FAIL** — the Markdown caption truncates “set” to `se` and replaces both `τ` variables by `�`; the preceding word is truncated to `quantit`. Its image link `images/page_8_image_0.jpg` does not resolve beside the Markdown; the source MinerU JPEG exists under the nested `<base>/images/` directory. A source-derived Figure 1 crop is now in this Peer’s permitted audit prefix; repoint the Markdown image link to it after the full-page audit, preserving the caption as text. Equation `(3.4)` and the remaining compared text agree. Printed running head/page number are omitted from Markdown.

### PDF p.010 / printed p.10

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p010.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p010_transfer_matrix_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:27:49 EDT.
- Compared the transfer-matrix continuation and equation `(3.5)`, the limiting-parameter discussion, and §3.2 through the free-energy formula `(3.6)`. The transfer-matrix crop was visually inspected to resolve the lost parameters.
- Print evidence: the paragraph specifies “letting `M` and then `N` go to infinity” and calls the underlying space a `d`-dimensional torus; equations `(3.5)` and `(3.6)` are printed.
- Result: **FAIL** — Markdown replaces `M` and `N` in that limit statement and `d` in “the �-dimensional torus” with `�`. Equations `(3.5)` and `(3.6)` otherwise match. The sentence “represented more than for his physical relevance” is also printed as written and is retained as a source-level grammar quirk. The printed running head/page number are omitted from Markdown.

### PDF p.011 / printed p.11

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p011.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:28:48 EDT.
- Compared equations `(3.7)` and `(3.8)`, their explanatory text, and the following consequences through the end of the combinatorial-method paragraph.
- Print evidence: both equations and references `[105]`, `[33]`, and `[29]` are present and correspond; the page ends after the complete-account reference sentence.
- Result: **PASS±** — mathematical statements, subscripts, exponents, and tags match. Markdown preserves the print line-end hyphenation `open-ing` from a line break (`open-` / `ing`); this is a harmless typographic artifact. Running head and page number are not represented in Markdown.

### PDF p.012 / printed p.12

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p012.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p012_Pfaffian_G_KG_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:29:46 EDT.
- Compared the Pfaffian and quantum-spin-chain approaches, Yang–Baxter paragraph, and the opening of §4 through the postwar-development summary.
- Print evidence: the Pfaffian paragraph names a finite planar graph `G` and the related graph `K(G)`; the crop confirms both symbols. The page closes the section-4 opening with the Ising model’s role in the postwar era.
- Result: **FAIL** — Markdown replaces `G` and `K(G)` in the Pfaffian paragraph with `�`; the defining graph symbols are lost. The `dificulties`, `diferent`, and `ofered` spellings reflect non-misleading `ff`-ligature OCR artifacts. Repair `G` and `K(G)` after full audit; printed running head/page number are absent from Markdown.

### PDF p.013 / printed p.13

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p013.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p013_corr_ineq_4_1-4_4_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:31:13 EDT.
- Compared §4.1’s critical-parameter discussion, Griffiths’ inequalities `(4.1)`–`(4.2)`, GHS `(4.3)`, and Simon–Lieb `(4.4)` against the PDF text layer and crop.
- Print evidence: the Griffiths statement is quantified for every `A,B ⊂ V`; the Simon–Lieb statement refers to the model on `S` and sums over `y ∈ ∂S`.
- Result: **FAIL** — Markdown reads `oμ` where print has `of β`, replaces `A` in the `(4.1)` hypotheses with `�`, misspells `Griffiths’` as `Grifiths’`, and replaces the model domain `S` in the Simon–Lieb sentence with `�`. Formula bodies and tags `(4.1)`–`(4.4)` otherwise match. Repair the parameter, set, surname, and domain symbol after full audit; running head/page number are omitted.

### PDF p.014 / printed p.14

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p014.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:32:10 EDT.
- Compared the remaining correlation inequalities `(4.5)`–`(4.6)`, the full Lee–Yang-theory discussion, and the §4.2 transition against the PDF text layer.
- Print evidence: the Messager–Miracle–Solé and FKG inequalities, Lee–Yang zero condition `Re(h_x)=0`, and §4.2 opening are present in order.
- Result: **PASS±** — the equations, domains, variables, and section transition match. Minor `ff`-ligature spellings (`different`→`diferent`, `effect`→`efect`) are non-misleading. Running head/page number are absent from Markdown.

### PDF p.015 / printed p.15

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p015.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p015_scaling_exponents_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:33:50 EDT.
- Compared critical-exponent examples `(4.7)`, scaling relations `(4.8)`, and the opening definition of correlation length. The 300 dpi crop was used to distinguish bold critical-exponent symbols from regular inverse-temperature `β` and to inspect the printed exponent in `(4.7)`.
- Print evidence: the first exponent in `(4.7)` is bold `β`, while the inverse-temperature `β` is regular; the text explicitly says they are distinct. The correlation-length paragraph identifies exponent `ν`.
- Result: **FAIL** — Markdown flattens bold critical-exponent `β` to the same regular `β` used for inverse temperature, erasing the distinction explicitly stated in print. It also replaces `ν` in “the exponent ν” with `�`. The other scaling terms and equation `(4.8)` are present. Print visibly uses `δ` in the exponent `d−2+δ` in `(4.7)`; retain this as a source-level notation quirk rather than substituting a mathematically expected symbol. Restore the boldface distinction and `ν` after the full audit; printed running head/page number are omitted.

### PDF p.016 / printed p.16

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p016.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p016_off-critical_universality_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:35:03 EDT.
- Compared the correlation-length explanation through the universality-hypothesis bullets and its quotation, against the PDF p.16 text and crop.
- Print evidence: the text says “off-critical”; the universality list specifies lattice dimension `d`, spin-space symmetry, and coupling-constant decay. The crop confirms those glyphs and the printed names `Kadanoff` and `Griffiths`.
- Result: **FAIL** — Markdown changes “off-critical” to `of-critical`, loses `d` in “�-dimensional” and replaces the lattice-dimension bullet `d` with `�`; it repeatedly spells `Kadanoff` as `Kadanof` and `Griffiths` as `Grifiths`. The remaining prose and quote continuation agree. Correct the term, symbols, and names after the full audit; running head/page number are omitted.

### PDF p.017 / printed p.17

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p017.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:36:02 EDT.
- Compared the close of §4, the probabilistic-interpretation introduction, §5.1, and equation `(5.1)` through the opening discussion of random configurations.
- Print evidence: equation `(5.1)` defines `μ_{G,β,h}[{σ}] = Z(G,β,h)^{-1} exp[−βH_{G,h}(σ)]`; the following prose introduces correlations and the probability interpretation.
- Result: **PASS±** — the formula and explanatory prose match. Markdown places the word “or,” in “corroborate or, on the contrary” inside a superscript math wrapper and joins some adjacent words; no variable or prose content is lost. Running head/page number are omitted.

### PDF p.018 / printed p.18

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p018.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p018_Glauber_boundary_variables_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:37:38 EDT.
- Compared Frame 3’s Glauber-dynamics definition and §5.2 through equation `(5.3)` against the PDF page and high-resolution crop.
- Print evidence: the update rule refers to time `t`, vertex `x`, and the spin at `x`; §5.2 defines `W ⊂ V`, the induced graph `H`, and a configuration `τ` on `G`. Equations `(5.2)` and `(5.3)` appear on the page.
- Result: **FAIL** — Markdown replaces `t` and the spin-site `x` in Frame 3 with `�`; §5.2 loses the defining `V`, `W`, `H`, `G`, and `τ` symbols in its domain/conditioning prose. Equations `(5.2)` and `(5.3)` otherwise match. Print says the dynamics has invariant measure `μ_{G,β,0}` but later says its limit is sampled according to `μ_{G,β,h}`; Markdown preserves that source-level mismatch, so it is not corrected. Restore the lost prose symbols after full audit; running head/page number are omitted.

### PDF p.019 / printed p.19

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p019.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p019_DLR_Gibbs_variables_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:38:57 EDT.
- Compared the DLR definition `(5.4)`, its explanatory bullets, the Gibbs-measure existence/classification discussion, and the Dobrushin-state example.
- Print evidence: `(5.4)` conditions on `𝔉_{Z^d\V}` and the event `E_τ` that `σ` and `τ` agree on `G`’s exterior boundary; the bullets define `G` from `V` and the outside-spin σ-algebra. Gibbs-measure limits and the Dobrushin example use `G` and boundary configuration `τ`.
- Result: **FAIL** — Markdown replaces the boundary-agreement symbols and σ-algebra name with `�`/an unrecognized `�`-algebra, and loses `G` in the limit “as G tends to `Z^d`” and `τ` in the all-plus/all-minus boundary description for the Dobrushin measure. The DLR equation and remaining prose are present. Repair the omitted variables and σ-algebra name after full audit; running head/page number are omitted.

### PDF p.020 / printed p.20

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p020.png` (150 dpi, pngmono).
- Figure 2 source crop: `audit/ICM2022_proceedings_Duminil-Copin_p020_Figure2.png` (300 dpi, grayscale; simulation panels only, caption excluded).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:40:49 EDT.
- Compared the conclusion of the Gibbs-state classification, Figure 2 and its caption, and §5.3 through the Ornstein–Zernike introduction. The source crop and nested MinerU figure asset were visually compared; the diagrams match.
- Print evidence: Figure 2 is followed by its caption; §5.3 is titled “Phase coexistence and Wulff shape”. The triangular-lattice example uses the `x`-axis and an interface from `(−n,0)` to `(n,0)`.
- Result: **FAIL** — Markdown changes “Wulff” to `Wulf`, replaces `x` in `�-axis`, and loses `n` from the endpoint `(n,0)`. The Figure 2 link `images/page_19_image_0.jpg` does not resolve beside the Markdown; the matching original MinerU asset is nested under `<base>/images/`. A source-derived figure crop is stored in this Peer’s audit prefix; repoint the Markdown image link to it after full audit, keeping the caption as text. The minor `diferent` / `minuse` spellings are OCR artifacts. Running head/page number are omitted.

### PDF p.021 / printed p.21

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p021.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p021_euclidean_functionals_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:42:20 EDT.
- Compared the §5.3 close, the start of constructive quantum field theory, and equations `(6.1)`–`(6.2)` with the source text and 300 dpi crop.
- Print evidence: the smeared observable is `T_f(Φ)=∫ f(x)Φ(x) dx`; the Hamiltonian includes `(Φ,AΦ)+∫P(Φ(x))dx`; the polynomial order is `Φ(x)^{2k}`; equation `(6.2)` uses `∏ f_j(x_j)`.
- Result: **FAIL** — Markdown loses `dx` and the compact-support function `f` in the `T_f` definition; replaces `A` and `k` with `�` in the Hamiltonian explanation; omits `dx` after `∫P(Φ(x))`; and drops the subscript `j` from `f_j(x_j)` in `(6.2)`. The broader formulas `(6.1)`–`(6.2)` are present. Markdown also duplicates the closing angle bracket after the pointwise-correlation expression; this is a non-misleading markup artifact. Restore the missing factors and indices after full audit; running head/page number are omitted.

### PDF p.022 / printed p.22

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p022.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p022_CQFT_forms_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:45:19 EDT.
- Compared equation `(6.3)`, the `Φ^4` discussion, lattice regularisation and equations `(6.4)`–`(6.5)`, and the Griffiths–Simon-class passage through the page break.
- Print evidence: the Gaussian-field description says “`2n`-point Schwinger functions”; the lattice paragraph names cutoff parameters `a` and `R`; the class is attributed to Griffiths and Simon.
- Result: **FAIL** — Markdown replaces `n` in “`2�`-point” and both `a` and `R` in the cutoff-role sentence with `�`; it repeatedly spells `Griffiths` as `Grifiths`. Equations `(6.3)`–`(6.5)` otherwise match print. Restore the prose symbols and surnames after full audit; printed running head/page number are omitted.

### PDF p.023 / printed p.23

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p023.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p023_reflection_positivity_6_6-6_9_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:46:40 EDT.
- Compared the torus/reflection setup, equations `(6.6)`–`(6.9)`, and the Green-function and critical-decay statements.
- Print evidence: the torus is `d`-dimensional with even side length `L`; a reflection `ϑ` maps `T_L^+` to `T_L^-`; Gaussian domination quantifies `h:V→R`; the infrared bound assumes `d>2`; the pointwise estimate is for every `x,y ∈ Z^d`.
- Result: **FAIL** — Markdown replaces `d`, `L`, and `ϑ` in the setup with `�`, omits `→` from `h:V→R`, and loses `d` in “for d>2” and `x` in “every x,y”. Equations `(6.6)`–`(6.9)` otherwise match. Restore the setup/domain symbols after full audit; running head/page number are omitted.

### PDF p.024 / printed p.24

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p024.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p024_random_currents_6_10-6_13_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:47:57 EDT.
- Compared the random-current introduction, equations `(6.10)`–`(6.13)`, and the start of Frame 4.
- Print evidence: the opening term is `exp[βσ_xσ_y]`; a current source is a vertex `x` with odd `Δ_x(n)`; currents with `∂n=A` pair vertices of `A`.
- Result: **FAIL** — Markdown renders `exp` as spaced `s x p` text in a math wrapper, loses the source vertex `x`, and replaces the set `A` in “vertices of A” with `�`. Equations `(6.10)`–`(6.13)` otherwise match. Markdown also spells printed `Griffiths` as `Grifiths`. Correct the operator, symbols, and surname after full audit; running head/page number are omitted.

### PDF p.025 / printed p.25

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p025.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p025_high-temp_switching_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:49:33 EDT.
- Compared equation `(6.14)`, the current-remapping argument, and Frame 5’s switching-lemma statement `(6.15)` against the PDF page/crop.
- Print evidence: the high-temperature expansion is on graph `G` rather than `G*`; the remapping uses a path from `x` to `y`; Frame 5 defines `AΔB` and quantifies over sets `A,B ⊂ V`.
- Result: **FAIL** — Markdown replaces `G` in the comparison with the low-temperature expansion, loses both `x` and `y` in the remapping path and in the switching-lemma preamble, and corrupts `AΔB` to `�Δ�` plus the `A` in “sets of vertices `A,B`”. Equations `(6.14)` and `(6.15)` otherwise match. Restore these source and set variables after full audit; running head/page number are omitted.

### PDF p.026 / printed p.26

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p026.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p026_triviality_6_16-6_18_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:51:09 EDT.
- Compared the switching-lemma application `(6.16)`, the dimension threshold, smeared average `(6.17)`, variance definition, Gaussian estimate `(6.18)`, and its interpretation.
- Print evidence: §6.4 is “Triviality in dimension `d>4`”; the smearing function is `f`, and `Σ_L` is the variance over the box of size `L`.
- Result: **FAIL** — Markdown replaces `d` in the §6.4 heading, `f` in “where f ranges over…”, and `L` in “box of size L” with `�`. It also misspells printed `Griffiths’` as `Grifiths’` in the Frame 5 wrap-up. Equations `(6.16)`–`(6.18)` otherwise match. Restore the dimension, function, box-size symbols, and surname after the full audit; running head/page number are omitted.

### PDF p.027 / printed p.27

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p027.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p027_Ursell_random_walk_scales_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:52:22 EDT.
- Compared the Ursell identities `(6.19)`–`(6.20)`, the random-walk intersection discussion, and the §6.5 opening.
- Print evidence: the comparison length is `L` throughout the random-walk discussion; the paragraph names paths joining `x₁` to `x₂` in `n₁` and `x₃` to `x₄` in `n₂`.
- Result: **FAIL** — Markdown replaces the length `L` with `�` at multiple points and loses `x₂` in the path description (`x₁` and `�` in `n₁`). Equations `(6.19)`–`(6.20)` otherwise match. Restore the scale and vertex symbol after full audit; running head/page number are omitted.

### PDF p.028 / printed p.28

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p028.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p028_phi4_lambda_authors_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:54:26 EDT.
- Compared §6.5’s weakly coupled `φ⁴` discussion and block-spin/GFF renormalisation paragraphs, plus the §6.6 opening, against PDF p.28 and the crop.
- Print evidence: the weak-coupling condition is “`λ` is small”; the text names Kadanoff and Bauerschmidt (the latter hyphenated across a print line break as `Bauer-` / `schmidt`).
- Result: **FAIL** — Markdown replaces `λ` with `�`, spells `Kadanoff` as `Kadanof`, and leaves a space in the line-broken surname as `Bauer schmidt` instead of rejoining `Bauerschmidt`. The remaining compared prose matches; the source’s line-break hyphen in `Gawed-` / `ski` is preserved as printed when reflowed. Correct the missing parameter and names after full audit; running head/page number are omitted.

### PDF p.029 / printed p.29

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p029.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p029_triviality_percolation_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:56:29 EDT.
- Compared the 4D triviality bound `(6.21)`, random-walk intersection scales, and the opening percolation definition.
- Print evidence: the bound uses `L ≤ ξ(β)` and denominator `(log L)^c`; the random walks are separated by distance of order `L`, and the percolation definition has vertex-set `V`.
- Result: **FAIL** — Markdown replaces `L` with `�` repeatedly in the random-walk scale discussion and replaces `V` in “vertex-set V” with `�`. Equation `(6.21)` itself matches. Restore the scale and graph-domain symbols after full audit; running head/page number are omitted.

### PDF p.030 / printed p.30

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p030.png` (150 dpi, pngmono).
- 300 dpi arbitration crops: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p030_percolation_exponential_decay_300dpi.png` and `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p030_inequality_7_2-7_3_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 16:58:20 EDT.
- Compared the percolation-connection description, exponential-decay statement `(7.1)`, differential inequality `(7.2)`, and the opening of `(7.3)`.
- Print evidence: the connectivity sentence asks whether `x` and `y` are connected; the exponential-decay bound quantifies over every `x,y ∈ Z^d`; `(7.3)` follows the clause `h=0` and `β<β_c` with no extra footnote marker.
- Result: **FAIL** — Markdown replaces the first `x` in “x and y are connected” with `�`, and appends a spurious `<sub>�</sub>` after `β_c` in the `(7.3)` precondition. Equations `(7.1)`–`(7.3)` otherwise match. Remove the stray subscript and restore `x` after full audit; running head/page number are omitted.

### PDF p.031 / printed p.31

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p031.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p031_FK_domain_omega_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 17:00:18 EDT.
- Compared equations `(7.4)`–`(7.5)`, the continuity result, and the FK Ising coupling description through the Figure 3 reference.
- Print evidence: `|ω|` counts open edges; `k(ω)` counts connected components of `ω`; the coupling chooses a spin for every component `C` of `ω` and yields the Ising law on `G`.
- Result: **FAIL** — Markdown replaces `ω` in the edge-count and component-count prose, in “component C of ω”, and in the even-component event with `�`; it also replaces graph `G` in “the Ising model on G” and loses `x` and `y` in the Figure 3 connectivity sentence. Equation `(7.5)` and the other compared formulas match. Restore the graph/configuration variables after full audit; running head/page number are omitted.

### PDF p.032 / printed p.32

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p032.png` (150 dpi, pngmono).
- Figure 3 source crop: `audit/ICM2022_proceedings_Duminil-Copin_p032_Figure3.png` (300 dpi, grayscale; diagrams only, caption excluded).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 17:43:28 EDT.
- Compared Figure 3/caption, the FK connectivity formula `(7.6)`, the component-parity event, and FKG inequality `(7.7)`. The source crop and nested MinerU JPEG were visually compared; all three diagrams match.
- Print evidence: the caption says `ω_e=1`; equation `(7.6)` uses connectivity in `ω`; the event `F_A` requires each component of `ω` to contain an even number of vertices from `A`.
- Result: **FAIL** — Markdown says “on th right” in the figure caption and replaces both `ω` and `A` with `�` in the component-parity definition. The relative image link `images/page_31_image_0.jpg` does not resolve beside the Markdown; the matching JPEG is nested under `<base>/images/`. The source-derived diagram crop is in this Peer’s audit prefix; repoint the Markdown link after full audit, keeping the caption as text. Equations `(7.6)`–`(7.7)` otherwise match; running head/page number are omitted.

### PDF p.033 / printed p.33

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p033.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 18:00:41 EDT.
- Compared the opening of §7.3 and the §8 conformal-invariance overview through the scaling-limit/domain setup.
- Print evidence: the §8.1 paragraph names Leo `Kadanoff` and begins the definition setup with the critical model on `Z^d` and rescaled lattices `aZ^d`.
- Result: **FAIL** — Markdown spells the mathematician’s surname as `Kadanof`, dropping an `f`. The compared percolation overview and conformal-invariance prose/symbols otherwise match through the simply connected-domain setup. Correct the name after full audit; running head/page number are omitted.

### PDF p.034 / printed p.34

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p034.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p034_scaling_limit_8_1-8_2_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 18:54:42 EDT.
- Compared the scaling-limit definitions for spin and energy correlations, equations `(8.1)`–`(8.2)`, and the interface-space setup.
- Print evidence: `[x]_a` is the vertex closest to `x`; `(x)_a` is the edge closest to `x`; the limits are taken as `a→0`.
- Result: **FAIL** — Markdown replaces `x` in both closest-point definitions and `a` in the limit-to-zero prose with `�`; it also truncates “plus” to `plu` in “plus and minus spins”. Equations `(8.1)`–`(8.2)` otherwise match. Restore the missing point/scale symbols and the word after full audit; running head/page number are omitted.

### PDF p.035 / printed p.35

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p035.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p035_conformal_covariance_Frame6_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 19:46:54 EDT.
- Compared covariance identities `(8.3)`–`(8.4)`, the interface-limit description, and Frame 6’s domain/vertex/face/cut setup through the order-disorder-correlation introduction.
- Print evidence: the interface limit is as `a→0`; Frame 6 uses the largest component `Ω` of `aZ²∩Ω`, `n` vertices and faces, and `n` disjoint cuts.
- Result: **FAIL** — Markdown replaces `a` in the interface limit with `�`; in Frame 6 it replaces the component/domain `Ω` throughout and `n` in “Choose n disjoint cuts” with `�`. It also spells `Kadanoff` as `Kadanof` in the preceding §8.2 paragraph. Equations `(8.3)`–`(8.4)` otherwise match. Restore the limit, domain, count, and name after full audit; running head/page number are omitted.

### PDF p.036 / printed p.36

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p036.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p036_fermionic_preholomorphic_8_5-8_6_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 20:22:55 EDT.
- Compared the order-disorder formula `(8.5)`, the fermionic-observable definition, the preholomorphic explanation, and equation `(8.6)` with the PDF page/crop.
- Print evidence: the formula `(8.5)` uses `F_Ω^(a)`; its definition uses edge endpoints `x,y` and limit parameter `a`; Frame 7 refers to a planar graph `G` and names the four corners `NW, SW, SE, NE`.
- Result: **FAIL** — Markdown replaces `Ω` in Frame 6 and `x,y` in the edge/face description with `�`, loses `a` in the limit statement, replaces graph `G` with `�`, and replaces all four corner names in the explanation of `(8.6)` with `��`. The formula bodies `(8.5)` and `(8.6)` otherwise match. Restore the missing domain/point/scale/corner symbols after full audit; running head/page number are omitted.

### PDF p.037 / printed p.37

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p037.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p037_isoradial_finite_range_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 20:42:28 EDT.
- Compared the remainder of Frame 7, the s-holomorphicity explanation, and §8.3 through the isoradial-graph coupling discussion.
- Print evidence: Smirnov’s strengthened condition is called `s`-holomorphicity; the limit is as `a→0`; the section heading says “the 2D Ising model”; the isoradial definition embeds graph `G`.
- Result: **FAIL** — Markdown loses `s` in “�-holomorphicity”, `a` in the limit-to-zero clause, and `G` in the planar-graph definition; it also changes the heading’s `model` to `mode`. The remaining compared graph/coupling discussion matches. Restore these symbols and the title word after full audit; running head/page number are omitted.

### PDF p.038 / printed p.38

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p038.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p038_finite_range_pfaffian_8_7_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 21:00:23 EDT.
- Compared the finite-range graph discussion, the two perturbative directions, and Pfaffian identity `(8.7)` with the PDF page/crop.
- Print evidence: the finite-range graph has vertices `Z²` and joins pairs at distance at most `R`; the argument concerns `n`-point correlations on a graph `G`; equation `(8.7)` is printed for `2n` boundary points.
- Result: **FAIL** — Markdown replaces `R` in the finite-range distance and `G` in “an embedding of a graph G” with `�`; it also replaces `n` in “the structure of n-point correlations” with `�`. Formula `(8.7)` and the remaining compared prose match. Restore the finite-range and correlation variables after full audit; running head/page number are omitted.

### PDF p.039 / printed p.39

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p039.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p039_bootstrap_formulas_8_8-8_9_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 21:46:15 EDT.
- Compared the §8.4 introduction, scalar two-/three-point formulas `(8.8)`–`(8.9)`, and the first four-point consistency setup through the page break.
- Print evidence: the coefficient family is written `f_{ABC}` with script `A`; formulas `(8.8)` and `(8.9)` state the displayed scaling dimensions and match the Markdown.
- Result: **FAIL** — Markdown reads the script `A` in the explanatory coefficient label as `R` (`f_{RBC}`), changing the coefficient’s identifier. The section otherwise matches through the page’s final phrase “`x₃` and”, which continues on p.40; formulas `(8.8)`–`(8.9)` match. Correct the coefficient label after full audit; running head/page number are omitted.

### PDF p.040 / printed p.40

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p040.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p040_bootstrap_x4_and_conclusion_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 22:24:25 EDT.
- Compared the conformal-block consistency sentence, critical-exponent estimates, closing paragraph of §8.4, §9, and acknowledgments.
- Print evidence: the sentence begun on p.39 continues with “`x₄`”; the following two decompositions are then equated. The 300 dpi crop confirms the point label and printed estimates.
- Result: **FAIL** — Markdown replaces `x₄` in “`x₃` and `x₄`” with `�`, leaving the four-point gluing example incomplete. The estimates and the subsequent §8.4/§9 prose otherwise match. Restore `x₄` after full audit; running head/page number are omitted.

### PDF p.041 / printed p.41

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p041.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 22:53:30 EDT.
- Compared the Funding statement and bibliography entries `[1]`–`[14]` directly against the PDF p.41 text layer and page image.
- Print evidence: reference `[3]` says “a general class of Ising-type models”; reference `[11]` says “4-dimensional n-component |φ⁴| spin model”.
- Result: **FAIL** — Markdown truncates `general` to `genera` in `[3]` and replaces the `n` in `n-component` in `[11]` with `�`. Other compared author/year/volume/page fields match; `[5]` punctuation and `[10]` spacing are minor bibliographic typography artifacts. Correct the two reference strings after full audit; running head/page number are omitted.

### PDF p.042 / printed p.42

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p042.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 23:23:47 EDT.
- Compared bibliography entries `[15]`–`[33]` against the full PDF p.42 text layer, checking names, titles, journal/volume/year/pages, and DOI/arXiv locators where present.
- Print evidence: `[17]` and `[24]` use “Wulff”; `[19]` reads “effect of thermal agitation on atomic arrangement”; `[23]` specifies “above `T_c`”; `[28]` has “conformal invariance”.
- Result: **FAIL** — Markdown misspells “Wulff” as `Wulf` in `[17]` and `[24]`, changes “effect”/“arrangement” to `efect`/`arrangemen` in `[19]`, replaces `T` in `[23]` with `�`, and truncates “conformal” to `conforma` in `[28]`. Several other references have joined word boundaries (e.g. `[16]` “ofcontemporary”, `[30]` “etfils”); repair the substantive title/variable errors and normalize those boundaries after full audit. Running head/page number are omitted.

### PDF p.043 / printed p.43

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p043.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-01 23:48:01 EDT.
- Compared bibliography entries `[34]`–`[50]` against the PDF p.43 text layer and page image, including title spellings and journal/year/page data.
- Print evidence: `[41]` spells `Simmons-Duffin`; `[43]` titles the work “Construction and Borel Summability…”.
- Result: **FAIL** — Markdown spells the author in `[41]` as `Simmons-Dufin` (one `f` missing) and truncates “Borel” to `Bore` in `[43]`. Other compared reference fields agree; the abbreviated journal punctuation in `[45]` is a minor formatting artifact. Correct the two reference strings after the full audit; running head/page number are omitted.

### PDF p.044 / printed p.44

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p044.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-02 00:10:53 EDT.
- Compared bibliography entries `[51]`–`[69]` against the PDF p.44 text and page image, checking author names and article/book titles.
- Print evidence: the page spells Jaffe, Ioffe, Griffiths, “difference” in `[68]`, and “Monodiffric” in `[69]` as shown in print.
- Result: **FAIL** — Markdown repeatedly misspells Jaffe (`Jafe`, `[54]`–`[55]`), Ioffe (`Iofe`, `[56]` and `[67]`), and Griffiths (`Grifiths`, `[57]`–`[60]`); it also has `diference` in `[68]` and `Monodifric` in `[69]`. Word-boundary spacing is additionally lost in `[55]` (“afunctional”, “point ofview”), `[61]` (`ofMath.`), `[63]` (`Zeitsch.für`), and `[65]` (`ofIsing`). Correct the names and titles after full audit; running head/page number are omitted.

### PDF p.045 / printed p.45

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p045.png` (150 dpi, pngmono).
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-02 00:13:12 EDT.
- Compared bibliography entries `[70]`–`[87]` against the PDF p.45 text layer and page image.
- Print evidence: `[72]` reads “Kadanoff … near `T_c`”; `[77]` names Kirchhoff; `[78]` names Simmons-Duffin; `[81]` cites *Phys. Rev.* volume `87`; `[85]` cites *J. of Chem. Phys.*
- Result: **FAIL** — Markdown truncates Kadanoff in `[72]`–`[74]`, replaces `T` in `[72]` with `�`, misspells Kirchhoff and Simmons-Duffin in `[77]`–`[78]`, and gives volume `8` instead of `87` in `[81]`. It also joins words in `[73]`, `[85]`, and `[86]` (including `Proceedings ofthe` and `Archivefor history ofexact sciences`). Other compared reference fields match; duplicated punctuation in `[82]` and `[87]` is present in print and is retained. Correct the cited names/number and spacing after full audit; running head/page number are omitted.

### PDF p.046 / printed p.46

- Page image: `audit/ICM2022_proceedings_Duminil-Copin_p046.png` (150 dpi, pngmono).
- 300 dpi arbitration crop: `audit/300dpi/ICM2022_proceedings_Duminil-Copin_p046_refs_94-104_300dpi.png`.
- Actor: `Peer-P14`; model: `gpt-6-luna`; effort: `max`.
- Signed: 2026-10-02 00:17:37 EDT.
- Compared bibliography entries `[88]`–`[105]` and the author-affiliation/contact block against PDF p.46, using the 300 dpi crop for math styling.
- Print evidence: `[94]` names `Simmons-Duffin`; `[98]` prints the field notation `φ_2^4`; `[104]` names Kadanoff. The final author and contact lines are also present.
- Result: **FAIL** — Markdown misspells `Simmons-Duffin` as `Simmons-Dufin` in `[94]`, replaces `φ` and the subscript `2` in `φ_2^4` in `[98]` with `�`/omits them, and spells `Kadanoff` as `Kadanof` in `[104]`. It also joins words in `[97]` (“of the”) and `[103]` (“of Vacuum”). Other compared reference data and the author-affiliation block match. Restore the missing bibliographic symbols, names, and spaces after full audit; running head/page number are omitted from Markdown.

## Repair registration

The PDF page entry above is the evidence locator for each repair below: it records the page image, text-layer comparison, print wording, and any 300 dpi arbitration crop. Corrections were made individually with Edit/apply_patch after the complete 46-page audit; the list below also records additional differences found during final rereading.

1. PDF p.001 — Print evidence: dedication word boundaries and Ioffe spelling, plus the footer © 2022 International Mathematical Union, preliminary-proceedings notice, and DOI. Corrected the dedication and added the exact footer text.
2. PDF p.002 — Print evidence: “Kadanoff’s scaling and universality hypotheses.” Corrected Kadanof’s surname. The non-misleading ff-ligature spellings remain PASS± artifacts.
3. PDF p.003 — PASS± page; no Markdown change. The reviewed ff-ligature artifact remains as recorded in the page entry.
4. PDF p.004 — Print evidence/crop: G=(V,E), vertex/edge sets V/E, endpoints x,y, spin at x, and the model on G. Restored V, E, x, y, G, corrected “mode” to “model,” and repaired the quoted “Dr. Wolfgang Pauli.”
5. PDF p.005 — Print evidence/crop: the d-dimensional model and m(β,h). Restored d and m. Equation (2.4) keeps the printed H_{G,β,h} notation and is registered above as a source-level quirk.
6. PDF p.006 — Print evidence/crop: Peierls’ edge set E(σ) and the name Rudolf Peierls. Restored E(σ) and the missing name space.
7. PDF p.007 — Print evidence/crop: the prose uses β, the limit uses n, the spin-flip region and loop count use C and k, and footnote 1 defines G*, the dual-edge map, E↔E*, and the (1/2,1/2) translation. Removed the spurious bold dot, restored n/C/k, and rebuilt the fragmented footnote from the printed text.
8. PDF p.008 — Print evidence: section heading “the integrability of the Ising model.” Corrected “mode” to “model.”
9. PDF p.009 — Print evidence/crop: Figure 1 caption says “The set S(5,3),” uses τ and τ̄, and introduces “quantity.” Restored those words/symbols and changed the broken image reference to the retained Figure 1 source crop.
10. PDF p.010 — Print evidence/crop: the limit lets M and then N tend to infinity and names a d-dimensional torus. Restored M, N, and d; retained the printed “represented more than for his physical relevance” wording.
11. PDF p.011 — PASS± page; no Markdown change. The page-entry note records the harmless printed line-end hyphenation.
12. PDF p.012 — Print evidence/crop: the Pfaffian paragraph names graph G and related graph K(G). Restored both graph symbols.
13. PDF p.013 — Print evidence/crop: the prose says “of β”; the hypotheses quantify over A,B⊂V; the model domain is S; the author is Griffiths. Restored β, A/B, S, and the surname.
14. PDF p.014 — PASS± page; no Markdown change.
15. PDF p.015 — Print evidence/crop: distinguishes bold critical-exponent β from regular inverse-temperature β, identifies ν, and shows x and 0 in the limiting clause. Restored boldface critical exponents in (4.7), the note, the exponent family, and (4.8), plus ν, x, and 0. Kept the printed δ in d−2+δ.
16. PDF p.016 — Print evidence/crop: “off-critical,” dimension d, Kadanoff, and Griffiths. Restored the term, both d occurrences, and the names.
17. PDF p.017 — PASS± page; no Markdown change.
18. PDF p.018 — Print evidence/crop: Glauber dynamics uses t and x; boundary prose uses G,V,W,H,τ. Restored those variables. Kept the printed μ_{G,β,0}/μ_{G,β,h} mismatch.
19. PDF p.019 — Print evidence/crop: DLR conditioning uses the 𝔉 sigma-algebra and event Eτ; limits use G and τ, and the consistency discussion varies τ and G. Restored the sigma-algebra label, boundary variables, G, and τ throughout.
20. PDF p.020 — Print evidence/crop: Wulff shape, x-axis, and interface endpoint (n,0). Corrected the spelling and symbols and repointed Figure 2 to the retained source crop.
21. PDF p.021 — Print evidence/crop: Φ(x), F(Φ), T_f with dx and compact-support f, Hamiltonian A and k, dx after the P integral, f_j(x_j), and a single closing angle bracket. Restored each item.
22. PDF p.022 — Print evidence/crop: H(Φ), 2n-point Schwinger functions, cutoffs a/R, and Griffiths. Restored the heading symbol, count, cutoff variables, and surname spellings.
23. PDF p.023 — Print evidence/crop: d-dimensional torus, even L, reflection ϑ, “for all,” h:V→R, d>2, and x,y. Restored each symbol and word.
24. PDF p.024 — Print evidence/crop: exp[βσxσy], source vertex x, set A, and Griffiths. Restored exp, x, A, and the surname.
25. PDF p.025 — Print evidence/crop: high-temperature expansion on G, path x→y, and switching-lemma sets AΔB and A,B⊂V. Restored these variables.
26. PDF p.026 — Print evidence/crop: the current measure is on G and the event pairs elements of A; §6.4 uses d>4, function f, and box size L. Restored G, A, Griffiths, d, f, and L.
27. PDF p.027 — Print evidence/crop: random-walk distances and limits use L, the first path joins x1 to x2, and the 4−ε expansion uses ε. Restored L, x2, and ε.
28. PDF p.028 — Print evidence/crop: weak coupling is λ-small; names are Kadanoff and Bauerschmidt. Restored λ and both surnames; retained the source line-break form of Gawedzki.
29. PDF p.029 — Print evidence/crop: random-walk scale uses L and percolation vertex set is V. Restored L and V.
30. PDF p.030 — Print evidence/crops: the connection question uses x and y; no subscript follows βc in the (7.3) precondition. Restored x and removed the spurious HTML subscript.
31. PDF p.031 — Print evidence/crop: ω counts open edges/components and defines the component event; the Ising model is on G and Figure 3 connectivity uses x,y. Restored ω, G, x, and y.
32. PDF p.032 — Print evidence/crop: caption reads “on the right”; the component-parity event uses ω and A; the prose following Figure 3 says “in G.” Corrected the caption and variables and repointed Figure 3 to the retained source crop.
33. PDF p.033 — Print evidence: Kadanoff in the conformal-invariance overview and the crossing preamble uses rectangle R, Cross(R), a path in ω, and sides of R. Corrected the name, restored those variables, and corrected the section-8 heading to “Ising model.”
34. PDF p.034 — Print evidence/crop: closest vertex/edge definitions use x, scaling limit uses a→0, and the prose says “plus and minus.” Restored x, a, and “plus.”
35. PDF p.035 — Print evidence/crop: interface limit uses a; Frame 6 uses Ω, n vertices/faces/cuts; the preceding paragraph spells Kadanoff. Restored a, Ω, n, and Kadanoff.
36. PDF p.036 — Print evidence/crop: Frame 6 uses Ω, edge endpoints x,y, and a; Frame 7 uses graph G and corners NW, SW, SE, NE. Restored those symbols and corrected the body spelling Kirchhoff.
37. PDF p.037 — Print evidence/crop: the term is s-holomorphicity, limit uses a, graph is G, the heading says “model,” and the embedding is an s-embedding. Restored these characters and words.
38. PDF p.038 — Print evidence/crop: finite-range distance is R, the graph is G, and the correlation family is n-point. Restored R, G, and n.
39. PDF p.039 — Print evidence/crop: coefficient family is f_{ABC}, not f_{RBC}. Corrected both explanatory prose labels; equations (8.8)–(8.9) were already present.
40. PDF p.040 — Print evidence/crop: the continuation of the four-point example names x4. Restored x4.
41. PDF p.041 — Print evidence: reference [3] says “general class,” and [11] says “n-component |φ4| spin model.” Restored “general,” n, and the word boundaries around the math notation.
42. PDF p.042 — Print evidence: Ioffe in [15]/[23], Wulff in [17]/[24]/[32], effect/arrangement in [19], Tc in [23], and conformal in [28]. Corrected those spellings/symbols and the joined word boundaries in [16], [19], and [30].
43. PDF p.043 — Print evidence: [41] spells Simmons-Duffin and [43] says Borel Summability. Corrected both.
44. PDF p.044 — Print evidence: [51] says “Control of a”; the references spell Jaffe, Ioffe, Griffiths, “difference,” and “Monodiffric.” Corrected those names/words and the recorded spacing in [55], [61], [63], and [65].
45. PDF p.045 — Print evidence: Kadanoff near Tc in [72], Kirchhoff [77], Simmons-Duffin [78], and Phys. Rev. volume 87 [81]. Corrected those strings and the recorded word boundaries in [73], [85], and [86]. The duplicated punctuation in [82] and [87] is source-faithful.
46. PDF p.046 — Print evidence/crop: Simmons-Duffin [94]/[97], φ2^4 and Griffiths [98], and Kadanoff [104]. Corrected those strings, rejoined the line-broken “soluble” in [95], and restored the word boundaries in [90], [92], [97], [99], and [103].

Repair commit: 5b55db0ba1145e4c42eaf620f09689760823c69d (parent: c51edc33b9083c054ffe0e6b95095be491661ffe). The raw MinerU Markdown source is preserved in commit d351abbff700768968605937fac5c051de31bb0a; its pre-repair SHA-256 was b8fc9a8804e1869e333b1b902959ad9677e3c19e8b2156bd22c6d2f7a563cd12.

Final Markdown SHA-256: 45dc4fbe37b30e01f57a7b288688b1803f4e97a8c9dad37102ae3a0f6a919898.

Final manual verification: the complete Markdown was reread from line 1 through line 1145 after the last edit. Each repair above was checked against its page entry and retained source evidence; no uncorrected FAIL item or new edit-induced discrepancy was found.

Read-only terminal verification: all 70 equation tags appear once in the expected sequence (2.1–2.10, 3.1–3.8, 4.1–4.8, 5.1–5.4, 6.1–6.21, 7.1–7.10, 8.1–8.9); U+FFFD count is 0; all three Markdown figure links resolve to the retained Figure 1–3 source crops; git diff --check passed.

This remains a contributor candidate. The page audit and repair registration are not integrated into the root AUDIT-INDEX.md or AUDIT-PROGRESS.log; those current-truth files remain for the Master integrator.
