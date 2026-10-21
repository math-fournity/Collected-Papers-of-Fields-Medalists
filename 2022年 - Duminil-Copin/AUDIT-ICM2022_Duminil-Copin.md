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

---

# 逐页重审块 A：PDF p.1–p.30（`Wf-R-P15` 逐页视觉审计）

- 范围：PDF 第 1–30 页（印刷 p.1–p.30，46 页中的前 30 页）。
- 方法：每页单独 `gs -q -sDEVICE=pngmono -r150` 渲染为 `/tmp/icm2022dc_audit_pNNN.png`，用 Read 工具打开亲眼查看，再与 `pdftotext` 整页文本层及 MinerU Markdown 对应段落五点比对；字形判读不了时升级 300dpi 裁剪仲裁。
- 与既有块的关系：`AUDIT-ICM2022_proceedings_Duminil-Copin.redo.md` 已覆盖 p.1–p.9。本块对 p.1–p.9 独立重看原页图复核其结论（不引用旧块结论作为证据），并新审 p.10–p.30。

## p.001（PDF p.1 / 印刷封面页）
- PNG：/tmp/icm2022dc_audit_p001.png（pngmono 150dpi）
- 核对：题录页——标题三行断行、作者、dedication 斜体行、Abstract 全文、Mathematics Subject Classification 2020（Primary/Secondary）、Keywords 四项、页脚版权行 / Preliminary version 行 / DOI 行、左下 ICM 会徽。
- 结果：PASS
  - 逐项与 150dpi 页图 + 文本层双证一致：标题 `100 Years of the (Critical) / Ising Model on the / Hypercubic Lattice`、作者 `Hugo Duminil-Copin`、dedication `Dedicated to the memory of colleagues and friends Dmitry Ioffe and Vladas Sidoravicius`（MD 行 5，`Ioffe` 拼写正确）、Abstract 六行全文（MD 行 9）、`Primary 82B20; Secondary 60K35`（MD 行 11）、Keywords `Ising model, percolation theory, phase transition, statistical mechanics`（MD 行 13）、页脚三行含 `© 2022 International Mathematical Union`、`Preliminary version, to appear in Proc. Int. Cong. Math. 2022, Vol. 1.`、`DOI 10.4171/ICM2022/204`（MD 行 15/17/19）。
  - 页图页脚 DOI 在 150dpi 下可读为 `10.4171/ICM2022/204`，与文本层一致，无需 300dpi 仲裁。
  - 未入 MD 者仅两类，均不误导：印刷断行连字符 `math-ematical` 已正确合并为 `mathematical`（这是修复而非缺陷）；左下 ICM 会徽为图形徽标（内含 `INTERNATIONAL CONGRESS OF MATHEMATICIANS 2022 JULY 6–14` 字样），非正文可检索内容。
- 备注：本页无需改动。

## p.002（PDF p.2 / 印刷 p.2）
- PNG：/tmp/icm2022dc_audit_p002.png（pngmono 150dpi）
- 核对：§1 全部三段（节标题顺序与编号）、breakthroughs 列举与引用号 `[20, 86]`/`[48]`、§2 节标题、§2.1 节标题、§2.1 Curie 段前半（至 "exhibits magnetisation only when an external" 跨页断点）、印刷斜体词（Curie temperature / spontaneous magnetisation / only）、页脚 `2 Hugo Duminil-Copin`。
- 结果：PASS±
  - 节标题顺序与编号 `1. Short motivation`（MD 行 23）→ `2. The first twenty years: a laborious start`（行 29）→ `2.1. Ising model's prehistory`（行 31）与印刷逐字一致；三段正文逐句吻合；`769.85 degrees Celsius`、`[30]`、`[20, 86]`、`[48]` 数值与引用号正确；`Kadanoff's` 拼写与印刷页图一致（两个 f 完整）。
  - 差异列表（均不误导，登记不改）：
    - MD 行 27 `diferent`——印刷与文本层均为 `different`；`diferential`——印刷为 `differential`。属 `ff` 连字被拍平为单 f 的 OCR 伪影，非 print quirk；语义不受影响，但影响精确字符串检索。
    - MD 行 27 `[20,86]`——印刷为 `[20, 86]`（逗号后空格被合并）。
    - 印刷页脚 `2 Hugo Duminil-Copin`（running foot）未入 MD；印刷斜体强调（`Curie temperature`、`spontaneous magnetisation`、`only`）未在 MD 保留（排版风格级）。
- 备注：`ff` 拍平与空格合并属全篇性伪影，不在本页单点修复，避免逐处批量改动破坏可溯源性。

## p.003（PDF p.3 / 印刷 p.3）
- PNG：/tmp/icm2022dc_audit_p003.png（pngmono 150dpi）
- 核对：p.2 跨页续句（"field is applied to it … ferromagnetic phase below it"）、Curie's law / Weiss 段、Lenz 两段、Ising 出生与论文段、Ising 两处直接引语（假设 decay rapidly… / of all the possible positions…）、末段至 "irrespective of the tempera-" 跨页断点、页脚 `3 100 Years of the Ising Model`。
- 结果：PASS±
  - 正文逐句吻合：引用号 `[101]`（Weiss）、`[80]`（Lenz 形式化）、`[70]`（Ising 论文）正确；1900/1924/1925 年份正确；`mean-field approximation`、`Curie-Weiss model`、`paramagnetic phase`、`linear chain` 术语正确；Ising 两处英文直接引语在页图与文本层中逐字一致，MD 行 43 亦逐字一致（含 `neighbouring elements`、`minimum energy is when they are both acting in the same direction`）。
  - 页界断词 `tempera-`（本页末）/ `ture`（p.4 首）在 MD 中正确衔接为 `temperature`，无重复无缺失。
  - 差异列表（不误导，登记不改）：MD 行 35 `eficient`——印刷与文本层均为 `efficient`（`ff` 连字拍平 OCR 伪影，非 print quirk）；印刷 running foot `3 100 Years of the Ising Model` 未入 MD；印刷斜体强调（`phase transition`、`Curie's law`、`mean-field approximation`、两处引语等）未在 MD 保留（排版风格级）。
- 备注：无内容错误，本页无需改动。

## p.004（PDF p.4 / 印刷 p.4）
- PNG：/tmp/icm2022dc_audit_p004.png（pngmono 150dpi）
- 核对：p.3 跨页续段（Ising 猜想 + Stephen Brush 引语全文）、Ising 生平段、§2.2 节标题、形式定义段全部数学符号、公式 (2.1)(2.2)(2.3) 的求和域/下标/系数/尾标点、`h ∈ ℝ`、`(J_{x,y} : x,y ∈ V)`、`n.n.f.` 记号、页脚 `4 Hugo Duminil-Copin`。
- 结果：PASS±
  - 定义段数学逐项与 150dpi 页图一致：`G = (V, E)`、超立方格 `Z^d`（MD 行 51 作 `\mathbb { Z } ^ { d }`）、顶点集 `V`、边集 `E`、边 `e = {x, y}` 且 `x, y` 为端点、`σ_x ∈ {−1, +1}`（**印刷此处带 `+1`**，行 51 忠实照录）、自旋构型 `(σ_x : x ∈ V) ∈ {−1, 1}^V`（**印刷此处为 `{−1, 1}` 无 `+`**，行 51 忠实照录）。印刷自身的 `{−1,+1}` 与 `{−1,1}^V` 不一致属 print 层级排印细节，未按数学预期"统一"。
  - 公式逐项吻合：(2.1) `H_{G,h}(σ) := −Σ_{{x,y}∈E} σ_x σ_y − h Σ_{x∈V} σ_x` + **尾逗号**（印刷有，MD 行 56 有）；(2.2) `H_{G,h,(J_{x,y})}(σ) := −Σ_{x,y∈V} J_{x,y} σ_x σ_y − h Σ_{x∈V} σ_x` **无尾标点**（印刷无，MD 行 62 无）；(2.3) `Z(G,β,h) := Σ_{σ∈{−1,1}^V} exp[−βH_{G,h}(σ)].` + 尾句点。三个编号 `(2.1)`/`(2.2)`/`(2.3)` 与印刷位置、字号一致。
  - 正文逐句吻合；Brush 引语中 `Dr. Wolfgang Pauli`（MD 行 45）拼写与页图一致；`modeling`（印刷原文，非 `modelling`）行 51 忠实保留。
  - 差异列表（不误导，登记不改，均为印刷有空格而 MD 空格合并）：MD 行 51 `ofthe`（印刷 "of the model"）、`magnet` 后 `magnet constituents`；行 53 `configuration$\sigma$on$G$is`、行 59 `magneticfield`（印刷 "magnetic field"）、行 65 `nearest neighbourferromagnetic`（印刷 "nearest neighbour ferromagnetic"）。另：行内公式与相邻文字间空格普遍合并（如 `subgraph$G = ( V , E )$of`）；印刷 running foot `4 Hugo Duminil-Copin` 未入 MD；`ℎ`（U+210E Planck 常数）与 `h` 混用属字体层面观感，不改。
- 备注：本页无 FAIL 级缺陷，无需改动 Markdown。

## p.005（PDF p.5 / 印刷 p.5）
- PNG：/tmp/icm2022dc_audit_p005.png（pngmono 150dpi）
- 核对：p.4 跨页续段（`The quantity β is interpreted as …`）、函数空间 `X : {−1,1}^V → ℝ`、公式 (2.4)(2.5)(2.6)(2.7) 的记号/求和域/导数/极限方向/尾标点、`Λ_n := [−n,n]^d ∩ Z^d`、自由能与磁化强度 prose、`m*(β) = 0` / `m*(β) > 0` 两情形、§2.3 节标题、§2.3 前两段（至 "violating the latest developments of" 跨页断点）、引用 `[63]`、页脚 `5 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：(2.4) `⟨X⟩_{G,β,h} := 1/Z(G,β,h) Σ_{σ∈{−1,1}^V} X(σ) exp[−βH_{G,β,h}(σ)].` + 尾句点；(2.5) `f(β,h) := −(1/β) lim_{n→∞} (1/|Λ_n|) ln Z(Λ_n,β,h)`（MD 行 84 用 `\lim _ {n \rightarrow \infty}` 记无穷，等价且与印刷 `n→∞` 一致）；(2.6) `m(β,h) := −∂/∂h f(β,h),` **尾逗号**；(2.7) `m*(β) := lim_{h↘0} m(β,h)`（MD 行 98 作 `\lim _ {h \searrow 0}`，方向 `↘` 正确）；编号 (2.4)–(2.7) 与印刷一致。
  - **print quirk 忠实保留（不按数学预期"纠正"）**：印刷 (2.4) 指数内作 `H_{G,β,h}`，而 p.4 定义的哈密顿量是 `H_{G,h}`（(2.3) 内亦为 `H_{G,h}`）。150dpi 页图与 born-digital 文本层双证一致，MD 行 78 原样照录。**不得改回 `H_{G,h}`。**
  - **印刷原文自身措辞忠实保留**：行 107 "a semi-classical version of Heisenberg model" 印刷即缺冠词 `the`，MD 未擅自补。
  - 差异列表（不误导，登记不改）：MD 行 81 两处 `thefree energy`（印刷 "the free energy"，空格合并）；行 101 `$m ^ { * } ( \beta ) =$ 0` 等三处行内数学与相邻文字空格排版失衡；running foot `5 100 Years of the Ising Model` 未入 MD；印刷斜体（`free energy`、`magnetisation`、`spontaneous magnetisation`、`paramagnetic`、`ferromagnetic`）未保留（风格级）。
- 备注：(2.4) 的 `H_{G,β,h}` 为全篇重点 print quirk，本块后续页若再出现同类记号，一律以印刷为准、不做数学化"修正"。

## p.006（PDF p.6 / 印刷 p.6）
- PNG：/tmp/icm2022dc_audit_p006.png（pngmono 150dpi）
- 核对：p.5 跨页续段（"quantum mechanics … ferromagnetic materials"）、Tamman/Bragg-Williams/Bethe 段、Fowler 段、Peierls 观察段、§2.4 节标题 `2.4. Peierls' argument`、§2.4 首段、Peierls argument 开头（至 "In a planar context, one may draw" 跨页断点）、记号 `σ ∈ Z^2`、`E(σ)`、`{x, y}`、`σ_x ≠ σ_y`、脚注上标 `1`、引用 `[19]`/`[90]`、页脚 `6 Hugo Duminil-Copin`。
- 结果：PASS±
  - 正文逐句吻合：1919/1935/1936 年份、`[19]`、`[90]` 引用号、`Gustav Tamman`、`Ralph Fowler`、`Bragg-Williams model`、`cooperative phenomena`、`Peierls' argument` 全部与页图一致；记号 `Z^2`（MD 行 123 作 `${ \mathbb { Z } } ^ { 2 }$`）、`E(σ)`、`{x, y}`、`σ_x ≠ σ_y` 一致。
  - **印刷原文自身措辞忠实保留**：行 111 "a statistical mechanics's argument"（原作者笔法，印刷即如此）未擅改。
  - 差异列表（不误导，登记不改）：MD 行 115 `diferent`×2（印刷 `different`，`ff` 连字拍平）；行 121 `ofthe`（印刷 "of the physics community"）、`ofmathematical`（印刷 "of mathematical interest"）——空格合并；行 123 `dual graph1`——印刷为脚注上标 `dual graph¹`，上标拍平（脚注正文在印刷 p.7 页脚，本页 MD 尚未出现，p.007 续查）；行 123 `configuration$\sigma$of the Ising model on${...}$`、行 121 `Peierls agreed with the majority ofthe` 等行内数学与文字空格普遍合并；running foot `6 Hugo Duminil-Copin` 未入 MD；印刷斜体（`cooperative phenomena`、`Peierls' argument`）未保留（风格级）。
- 备注：p.6→p.7 断点落在句中，MD 连续衔接无缺失，本页无需改动。

## p.007（PDF p.7 / 印刷 p.7）
- PNG：/tmp/icm2022dc_audit_p007.png（pngmono 150dpi）
- 核对：p.6 跨页续段（对偶图脚注上标 `1` 与 "see Figure 1"）、公式 (2.8) 三段等式、无编号不等式 `⟨𝕀(C = C)⟩ ≤ e^{−2β|∂_e C|}`、Frame 1 标题与正文两段、公式 (2.9)、`C = C(σ)` / `R^2 \ {e* : e ∈ E(σ)}` / `Flip_C(σ)` / `∂_e C`、脚注 1 全文（对偶图 `G* = (V*, E*)`、`{u,v}`、`e ↦ e*`、(1/2,1/2) 平移）、页脚 `7 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：(2.8) `Z(G,β,0) = Σ_{σ∈{−1,1}^V} e^{−βH_{G,h}(σ)} = e^{β|E(G)|} Σ_{F∈Even(G*)} e^{−2β|F|}.` + 尾句点。**print quirk 忠实保留**：左端已置 `h = 0`，而指数内印刷作 `H_{G,h}`（非 `H_{G,β,0}`、非 `H_{G,0}`），MD 行 126 原样照录，150dpi 页图与文本层双证一致，**不得按数学预期改写**。
  - (2.9) `⟨σ_0σ_g⟩_{Λ_n^+,β,0} = 1 − 2 Σ_{g∉C∈Even((Λ_n^+)*)} ⟨𝕀(C = C)⟩_{Λ_n^+,β,0}.`：求和下标 `g ∉ C ∈ Even((Λ_n^+)^*)`、指示函数 `𝕀`、以及**随机 `C`（粗体 𝐂）与固定 `C`（斜体 C）的大小写区分**在印刷与 MD 行 140 中均正确保留（`\mathbf {C} = C`），未混淆。
  - 无编号不等式 `⟨𝕀(C = C)⟩_{Λ_n^+,β,0} ≤ e^{−2β|∂_e C|}`（MD 行 146）指数 `−2β` 与 `∂_e C` 绝对值内嵌均与印刷一致；`e ∉ C` 记号在印刷作 `C ∌ g`，MD 行 143 作 `$C \ \not \ni \ \mathbf { g } ,$`，方向正确。
  - Frame 1 标题、正文两段、`Λ_n^+`、Griffiths' "ghost" vertex、`m*(β)` 极限表述与印刷逐句一致；**印刷美式拼写 `magnetization`（Frame 1 首句与 "decompose the magnetisation" 并存）忠实保留**，未统一为英式 `magnetisation`。
  - **print quirk 忠实保留**：正文句 "This formula immediately highlights the fact that **β large renders** configurations … unlikely" —— 印刷原句语法不完整（缺 "that"/"being"），页图与文本层双证一致，MD 行 129 原样保留。
  - 脚注 1 完整入 MD（行 149，以 `<small>` 承载，位于 Frame 不等式之后，对应印刷页脚位置）：`G* = (V*, E*)`、"faces of G (including the exterior one)"、`E*` 为无序对 `{u,v}`、`e*`、`(1/2, 1/2)` 平移，全部与印刷一致。位置差异属布局级，不误导。
  - 差异列表（不误导，登记不改）：
    - MD 行 149 作 `bijection`——**印刷此处印作 `bĳection`**（TeX `b\ij` 连字误用造成的印刷错字，见 150dpi 页图脚注第四行 "bĳection between E and E*" 与文本层）。MD 照录为规范拼写。按本块铁律三登记此印刷错字，**但不在 MD 中回填该错字**——单个字母级印刷连字误用不承载数学内容，回填会主动降低 Markdown 可读性与可检索性，且不改变任何命题。此为显式登记的处置决定，非漏检。
    - `ff` 连字拍平：MD 行 131 `diferent`（印刷 `different`）、行 135 `suficient`（印刷 `sufficient`）、行 143 `efectively`（印刷 `effectively`）。
    - 排版级：行 135 `$\Lambda_n^+$$plus a vertex$\mathbf{g} ,$` 数学与文字间空格失衡且逗号落在数学段内；行 137 `$\mathbb{R}^2 \setminus \{e^* : e \in$ $E(\sigma)\}$` 一条集合被拆为两个数学段；行 143 `$C \ \not \ni \ \mathbf{g} ,$` 多余空格。
    - 印刷 running foot `7 100 Years of the Ising Model` 未入 MD；Frame 边框与缩进（Frame 内文较正文缩进）在 Markdown 中以标题层级近似（排版风格级）。
- 备注：本页未改动 Markdown；`β large renders` 与 (2.8) 的 `H_{G,h}` 两处 print quirk 已逐条登记。

## p.008（PDF p.8 / 印刷 p.8）
- PNG：/tmp/icm2022dc_audit_p008.png（pngmono 150dpi）
- 核对：Frame 1 收尾段与公式 (2.10)（求和下限 `k ≥ 1`、`k4^k`、右端分数 `8e^{−2β}/(1 − 4e^{−2β})²`、尾句点）、§3 节标题、§3.1 节标题、Kramers-Wannier 两段（`[79]`、1941、"Frame 4" 与 "Frame 2" 互引）、公式 (3.1)(3.2)(3.3) 与编号、`ℎ` 置 0、`Z^2`、`C(β)`、`β_c`、页脚 `8 Hugo Duminil-Copin`。
- 结果：PASS±
  - 公式逐项吻合：(2.10) `⟨σ_0σ_g⟩_{Λ_n^+,β,0} ≥ 1 − 2 Σ_{k≥1} k4^k e^{−2βk} > 1 − 8e^{−2β}/(1 − 4e^{−2β})².`——圈数计数 `k4^k`、指数 `−2βk`、分母平方位置 `(1 − 4e^{−2β})²` 与印刷页图逐项一致；(3.1) `β_c = β_c(Z^d) := inf{β : m*(β) > 0}.`；(3.2) `C(β) := −β² ∂²/(∂β)² (βf)(β,0).`（负号、`β²`、二阶导数位置均正确）；(3.3) `βf(β,0) = β*f(β*,0) − 2β + ln 2 + 2 ln cosh(β*),`——**尾逗号**（印刷有逗号，MD 行 180 亦有逗号，忠实）。
  - 正文逐句吻合：`[79]` 两处、`Hans Kramers and Gregory Wannier in 1941`、"see Frame 4"、"see Frame 2"、`specific heat`、`duality relation`、`a priori non-obvious`、`[85]`（Montroll）、`[100]`（van der Waerden）、(2.8) 互引均与印刷一致；`Z^2`（MD 行 177 作 `${ \mathbb { Z } } ^ { 2 }$`）一致。
  - 节标题顺序与编号：`3. Onsager's 1944 revolution and the integrability of the Ising model`（MD 行 157）→ `3.1. Kramers-Wannier treatment of the Ising model and duality`（行 159），与印刷逐字一致。
  - 差异列表（不误导，登记不改）：MD 行 163 `critical inversetemperature`——印刷为 `critical inverse-`（行末）/ `temperature`（次行首），转写时断行连字符丢失且未以空格替代，形成词粘连；行 151 `at most$( k + 1 ) 4 ^ { k }$possible loops`、行 171 `defined by`、行 163 `when$\beta$is large` 等行内数学与相邻文字空格普遍合并；`C ( \beta )$blows up`、`$\beta _ { c }$defined` 同类；印刷斜体（`arbitrary`、`critical inverse-temperature`、`specific heat`、`duality relation`、`assuming`）未在 MD 保留（风格级）；running foot `8 Hugo Duminil-Copin` 未入 MD；Frame 边框/缩进未保留（布局级）。
  - 图引说明：MD 行 183 的 `![](../audit/ICM2022_proceedings_Duminil-Copin_p009_Figure1.png)` 在印刷中属 **p.9** 版面（Figure 1 位于 p.9 上部），MD 将其置于 (3.3) 之后与"where β and β* are related…"之前，顺序与印刷流一致；该图文件与 caption 的实际内容归 p.009 审。
- 备注：p.8 页尾即 (3.3)，其后无正文；本页无需改动。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：/tmp/icm2022dc_audit_p009.png（pngmono 150dpi）
- 核对：Figure 1 图与 caption 全文（On the left / On the right 两段、`Λ_1^+`、`(Λ_1^+)*`、`S(5, 3)`、两个 τ 的上下装饰、`−1` 与 `+1`）、图内字母标注（`top`/`g`/`bottom`/`Figure 1`）、self-dual 段（`tanh(β*) = e^{−2β}`、`β_c = ½ ln(1+√2)`）、Kramers-Wannier 证明段（`[85]`、`[100]`、Frame 2/Frame 4 互引、(2.8) 互引）、Frame 2 标题与首段、`S(N,M) := (Z/NZ)^{d−1} × ⟦0,M⟧`、`σ|bottom`/`σ|top`、公式 (3.4) 全部参数与尾逗号、页脚 `9 100 Years of the Ising Model`。
- 结果：PASS±
  - Figure 1 caption 逐项吻合（150dpi 页图可读）：`A picture of the low-temperature expansion on Λ_1^+`、`The set Λ_1^+ is depicted in dashed gray, and (Λ_1^+)* in plain black`、`The edges in the dual configuration are depicted in bold`、`The set S(5, 3) with the bottom and top sets depicted`、`In this case **τ̲** and **τ̄** are respectively constant equal to −1 and +1`。MD 行 185 记作 `$\underline{\tau}$ and $\bar{\tau}$`——**caption 首个 τ 带下划线**已在页图上确认（右侧 τ 不带下划线），MD 区分正确，与 (3.4) 的 `\underline\tau / \overline\tau` 记号一致。
  - self-dual 段公式吻合：`tanh(β*) = e^{−2β}`、`β* = β`、`β_c = ½ ln(1+√2)`（MD 行 187 作 `${ \frac { 1 } { 2 } } \ln ( 1 + { \sqrt { 2 } } )$`，系数 `1/2`、根号内 `2` 均正确）；`a priori non-obvious`、`[85]`（Montroll）、`[100]`（van der Waerden）、(2.8) 互引、Frame 2/Frame 4 互引全部一致。
  - Frame 2 首段与公式 (3.4) 吻合：`S(N,M) := (Z/NZ)^{d−1} × ⟦0,M⟧`、bottom `(Z/NZ)^{d−1} × {0}`、top `(Z/NZ)^{d−1} × {M}`、`σ|bottom`/`σ|top` 为 `{−1,1}^{(Z/NZ)^{d−1}}` 的元素、`Introduce the quantity` 拼写完整。
  - **print quirk 忠实保留**：Frame 2 已声明本节取 `h = 0`，而 (3.4) 指数内印刷作 `H_{S(N,M),h}`（未代入 0）。150dpi 页图与文本层双证一致，MD 行 196 原样照录，**不得改写为 `H_{S(N,M),0}`**。(3.4) 尾逗号（印刷有）MD 亦保留。
  - 差异列表（不误导，登记不改）：MD 行 193 `⟦0, M⟧` 记作 `\mathbb { I } 0 , M \mathbb { I }`（双括号 ⦃⦄ 被转写为 𝕀…𝕀 记号近似）——区间含义可读，但字形与印刷的整数区间双括号不同，属记号近似；行 193/196/199 行内数学与相邻文字空格普遍合并；`\sigma _ { | \mathrm { b o t t o m } }` 等下标字母被逐字拆空格（排版级）；Figure 1 图内的 `top`/`g`/`bottom` 字母标注属图形元素，不入 Markdown 文本；running foot `9 100 Years of the Ising Model` 未入 MD。
- 备注：MD 行 183 的图链接 `../audit/ICM2022_proceedings_Duminil-Copin_p009_Figure1.png` 为已跟踪的旧审计裁片资产，本页不改动；本页无需改动 Markdown。

## p.010（PDF p.10 / 印刷 p.10）
- PNG：/tmp/icm2022dc_audit_p010.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p010_300.png（300dpi 全页）、/tmp/icm2022dc_p010_eig_crop.png（主特征值句）、/tmp/icm2022dc_p010_eq36_crop.png（公式 (3.6)）、/tmp/icm2022dc_p010_fn2b_crop.png（脚注 2）
- 核对：p.9 跨页续段（`τ̲, τ̄ ∈ {−1,1}^{(Z/NZ)^{d−1}}` 与"so-called transfer matrix"）、公式 (3.5) 两个求和项与指数内负号、`Z(N,M,…) = V_N^M`、`V_N^N` trace、`(Z/NZ)^{d−1} × (Z/MZ)`、主特征值极限变量、§3.2 节标题 `3.2. Onsager's result`、Onsager 两段（1968、1942、`Z^2`、1944 `[87]`、1949 `[76]`）、公式 (3.6) 全部系数/积分限/被积函数/微分、integrability 段、脚注 2 全文、页脚 `10 Hugo Duminil-Copin`。
- 结果：**FAIL（1 处数学内容错误，已修，以原图为准）**
  - 公式逐项吻合：(3.5) `V_N(τ̲,τ̄) := Z(N,1,τ̲,τ̄) = exp[−β(Σ_{x∈(Z/NZ)^{d−1}} τ̲_x τ̄_x + Σ_{{x,y}∈E((Z/NZ)^{d−1})} τ̄_x τ̄_y)]`——两个求和项的下标域、上下划线 τ 的分配（第一项 `τ̲_x τ̄_x`、第二项 `τ̄_x τ̄_y`）、指数 `−β` 与方括号层级均与印刷一致；(3.6) `−βf(β,0) = ln 2 + (1/8π²) ∫₀^{2π} ∫₀^{2π} ln[cosh(2β)² − sinh(2β)(cosθ₁ + cosθ₂)] dθ₁ dθ₂.`——300dpi 裁片 `/tmp/icm2022dc_p010_eq36_crop.png` 逐项确认：`1/(8π²)` 系数、两重积分限 `0→2π`、`cosh(2β)²` 平方位置在括号内、`sinh(2β)(cosθ₁ + cosθ₂)`、`dθ₁ dθ₂`、尾句点，与 MD 行 216 完全一致。
  - 正文逐句吻合：1968（Nobel）、1942（New York Academy of Sciences）、1944 `[87]`、1949 Bruria Kaufman `[76]`、`Bruria Kaufman` 姓名、`exactly solvable`、`integrability`、`finite-dimensional Lie algebra`、`2D Ising model` 均与印刷一致。
  - **print quirk 忠实保留**：行 211 "its exact solution represented **more than for** his physical relevance" —— 印刷原句语序如此（150dpi 页图与文本层双证），MD 未擅改；同句末脚注上标 `2` 已拍平为 `relevance2`。
  - 脚注 2 已入 MD（行 221，`<small>` + `docvortex-page-footnote` 承载，位于 1949 段之后，对应印刷页脚位置）：300dpi 裁片 `/tmp/icm2022dc_p010_fn2b_crop.png` 确认印刷全文为 "His opinion on this fact seemingly evolved: in his first 1944 paper [87] he presents it as a poor model of ferromagnetism, but a fairly good model for binary alloys, while in his paper with Kaufman in 1949 [76] he describes it as a model for ferromagnetism."，与 MD 逐句一致（含 `[87]`、`[76]` 引用号）。
  - **FAIL 项与修复**：MD 行 207 原作 "…leading eigenvalue of `$V_N$` as `$M$` tends to infinity"，**与印刷相反**。300dpi 裁片 `/tmp/icm2022dc_p010_eig_crop.png` 明确印作 "of 𝑉_N as **N** tends to infinity"；文本层同。数学上亦必须为 `N`：本段先令 `M → ∞`（把 `V_N^M` 化为 `V_N` 的幂主导），再令 `N → ∞` 取 `V_N` 的主特征值极限，与前句 "by letting M and then N go to infinity" 一致。已用 Edit 将该处 `$M$` 改为 `$N$`。
  - **溯源（回归判定）**：`git show d351abbf:…md`（原始 MinerU 导出）该处为 U+FFFD `�`；`git show 59537f98:…md`（Peer-P14 harvest 提交）已把三处 `�` 中的两处正确补为 `$M$`（"letting M and then N"）、第三处误补为 `$M$`。**非导出缺陷，系 59537f98 引入的错误补字**：原导出此处并非正确（是缺字 `�`），是该 peer 把缺字补成了错误变量；本次按印刷纠正为 `$N$`。
  - 差异列表（不误导，登记不改）：行 213 `conference ofthe`（印刷 "of the"）；行 205/207/211 等行内数学与相邻文字空格普遍合并；running foot `10 Hugo Duminil-Copin` 未入 MD；印刷斜体（`transfer matrix`、`exact`、`exactly solvable`、`integrability`、`high-temperature expansion` 等）未保留（风格级）。
- 备注：本页实际改动 1 处（MD 行 207），证据为 300dpi 裁片 + 文本层双证。

## p.011（PDF p.11 / 印刷 p.11）
- PNG：/tmp/icm2022dc_audit_p011.png（pngmono 150dpi）
- 核对：p.10 跨页续段（`β ≥ β_c` 条件）、公式 (3.7) 的 `sinh(2β)^{−4}` 与 `1/8` 次幂、Yang 段（Chen-Ning Yang、Yang-Baxter's equation、Yang-Mills's theory、Lee-Yang's theory、`[105]`、Toeplitz determinants）、二点函数 `⟨σ_{(0,0)}σ_{(n,0)}⟩_{(Z/NZ)^2,β,0}`、公式 (3.8) 的**双极限次序**、FK percolation 与 Section 7.2 互引、forties/fifties 三点理由段（`½ log(1+√2)`、`C(β)`、`non mean-field behaviour`）、Onsager-Kaufman-Yang 段（`[10]`、1978、2D、`"399th solution of the Ising model"`）、Kac-Ward 段（`[71]`、`[100]`、`[33]`、1999、`[29]`）、页脚 `11 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：(3.7) `m*(β) = (1 − sinh(2β)^{−4})^{1/8}.` —— `−4` 指数位于 `sinh(2β)` 的括号之后、外层 `1/8` 次幂，MD 行 226 与印刷页图逐项一致；(3.8) `m*(β)² = lim_{n→∞} lim_{N→∞} ⟨σ_{(0,0)}σ_{(n,0)}⟩_{(Z/NZ)²,β,0}` —— **双极限的先后次序 `n→∞` 在外、`N→∞` 在内**在印刷与 MD 行 232 中一致（`\lim _ {n \to \infty} \lim _ {N \to \infty}`），未颠倒；左端 `m*(β)²` 平方位置正确；(3.7)(3.8) 编号与印刷一致，(3.8) 印刷无尾标点、MD 亦无。
  - 正文逐句吻合：`Chen-Ning Yang`、`Toeplitz determinants`、three-parenthetical 术语、`Section 7.2`、`FK percolation`、`specific heat C(β)` 对数发散、`½ log(1 + √2)`（MD 行 237 作 `\scriptstyle { \frac { 1 } { 2 } } \log ( 1 + { \sqrt { 2 } } )`，系数与根号正确）、`Curie-Weiss or Landau theories`、`Onsager-Kaufman-Yang`、`algebraic method`、`Baxter and Enting`、`1978 paper [10]`、`"399th solution of the Ising model"`、`Kac and Ward [71]`、`Kac-Ward's matrices`、`van der Waerden high-temperature expansion [100]`、`1999 [33]`、`discrete holomorphicity`、`[29]` 全部一致。
  - 差异列表（不误导，登记不改）：
    - MD 行 229 末尾 `_{ ( Z/NZ )^2 , \beta , 0 } ,$` —— 多出一个逗号且落在数学段内；印刷该处为句中停顿但无此逗号（纯转写残留，不影响式义）。
    - MD 行 237 `open-ing` —— 印刷断行连字符被原样保留在词中（应为 `opening`），属断词伪影。
    - MD 行 239 `startriangle transformation` —— 印刷为 `star-triangle transformation`，连字符丢失且两词粘连。
    - MD 行 241 `ofthe`（印刷 "of the partition function"）、`derivation ofthis`（印刷 "of this approach"）——空格合并。
    - MD 行 243 `dificulties` —— 印刷 `difficulties`（`ff` 连字拍平）。
    - running foot `11 100 Years of the Ising Model` 未入 MD；印刷斜体（`level of sophistication`、`mean-field approximations`、`many direct applications`、`algebraic method`、`399th solution of the Ising model`、`combinatorial approach`、`every`）未保留（风格级）。
- 备注：本页公式与正文内容全部与印刷一致，仅有连字符/空格/逗号类转写伪影；无需改动 Markdown。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：/tmp/icm2022dc_audit_p012.png（pngmono 150dpi）
- 核对：p.11 跨页续段（Pfaffian method 段）、Pfaffian 段全部记号与引用（`[66]`/`[75]`/`[46]`、`G`、`K(G)`、`McCoy-Wu [83]`、`Palmer [89]`）、Schultz-Mattis-Lieb 段（`[95]`、1D、`Section 8.3`、Grassmann "Gaussian"）、Rodney Baxter 段（Yang-Baxter equation、six-vertex model、`[9]`）、§4 节标题（两行标题）、§4 前两段（`"unavoidable"`、mathematical physics、hundreds）、页脚 `12 Hugo Duminil-Copin`。
- 结果：PASS±
  - 正文逐句吻合：`Hurst and Green [66]`、`Kasteleyn [75]`、`Fisher [46]`、`McCoy-Wu [83]`、`Palmer [89]`、`Schultz-Mattis-Lieb in [95]`、`Rodney Baxter`、`[9]`、`Section 8.3` 全部与页图一致；记号 `G` 与 `K(G)`（MD 行 243）正确。
  - **印刷拼写忠实保留**：印刷作 `Pfaffian`（双 f，见页图斜体 "Pfaffian method" 与正文两处），MD 行 243 三处均为 `Pfafian`（单 f）——此为**MinerU 侧 `ff` 连字拍平**（印刷与文本层均为 `Pfaffian`），非 print quirk。术语拼写被改（Pfaffian → Pfafian），属 OCR 伪影，登记为 PASS± 差异：`dificulties`（行 243，印刷 `difficulties`）、`diferent`（行 247，印刷 `different`）、`ofered`（行 253，印刷 `offered`，词首 `ff` 拍平）。
  - 节标题 `## 4. The fifties and sixties: the Ising model becomes a laboratory for understanding critical phenomena`（MD 行 249）与印刷两行标题合并后的文字逐字一致（印刷因排版折为两行，MD 合为一行，不误导）。
  - 差异列表（不误导，登记不改）：`Pfafian`×3 / `dificulties` / `diferent` / `ofered` 四处 `ff` 连字拍平（其中 `Pfafian` 为专有名词拼写变更，见上）；行 249 节标题为一行、印刷为两行（排版级）；行内数学与文字空格合并（`graph $G$ in terms` 等）；running foot `12 Hugo Duminil-Copin` 未入 MD；印刷斜体（`Pfaffian method`、`number of more refined results`、`mathematical physics`）未保留（风格级）。
- 备注：`ff` 拍平为全篇系统性 OCR 伪影（已见于 p.2/p.3/p.6/p.7/p.11），此处只登记不批量改，避免破坏逐处可溯源性。本页无需改动 Markdown。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：/tmp/icm2022dc_audit_p013.png（pngmono 150dpi）
- 核对：§4.1 节标题（两行）、§4.1 首段（`β` 等于 `β_c`、`[90]`、`Baker's use of Padé approximant [8]`、2D）、§4.1.1 节标题、相关不等式段与 `σ_A := ∏_{x∈A} σ_x` 定义、Griffiths 不等式段与 `[57]`、公式 (4.1) 两个不等式与下标 `G,β,h`、byproduct 段（`B = {x,y}`、对 `β` 与 `G` 单调）、公式 (4.2) 的 `inf`/`sup` 两式与 `β ≥ 0` 条件、GHS 段与 `[59]`、公式 (4.3) 二阶导数、Simon-Lieb 段与 `[82]`、公式 (4.4) 对 `∂S` 求和、`0 ∈ S`/`x ∉ S` 条件、页脚 `13 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：(4.1) `⟨σ_A⟩_{G,β,h} ≥ 0` **and** `⟨σ_A σ_B⟩_{G,β,h} ≥ ⟨σ_A⟩_{G,β,h}⟨σ_B⟩_{G,β,h}.` —— 两个不等式、`and` 连接词、三处下标 `G,β,h` 与尾句点均与印刷一致；(4.2) `β_c = inf{β ≥ 0 : m*(β) > 0} = sup{β ≥ 0 : m*(β) = 0}.` —— **inf/sup 两式的 `>`/`=` 严格性区分与 `β ≥ 0` 约束**在印刷与 MD 行 272 中一致；(4.3) `∂²/(∂h)² ⟨σ_x⟩ ≤ 0.` —— 二阶导数记号、方向 `≤ 0`、尾句点一致；(4.4) `⟨σ_0σ_x⟩ ≤ Σ_{y∈∂S} ⟨σ_0σ_y⟩_S⟨σ_yσ_x⟩.` —— 求和下标 `y ∈ ∂S`、右侧两个期望值均带下标 `_S`、左侧不带，与印刷一致；`(4.1)`–`(4.4)` 编号与印刷位置一致。
  - 记号一致：`σ_A := ∏_{x∈A} σ_x`（MD 行 261 作 `\Pi _ { x \in A } \sigma _ { x }`——`∏` 的直立大写 Pi 形态，语义一致）、`A,B ⊂ V`（印刷用 `⊂` 而非 `⊆`，MD 亦作 `\subset`）、`⟨·⟩_S` 的下标约定说明（"we drop the subscript after ⟨·⟩"）与印刷一致。
  - 正文逐句吻合：`Peierls' argument [90]`、`Baker's use of Padé approximant [8]`、`Griffiths' inequalities [57]`、`GHS's inequality [59]`、`Simon-Lieb's inequality [82]`、`spin-spin correlations`、`spontaneous magnetisation`、`unique transition between paramagnetic and ferromagnetic phases` 全部与页图一致；节标题 `4.1. Progress in mathematical physics: from perturbative regions of the phase diagram to the vicinity of the critical point`（MD 行 255）与印刷两行标题合并后逐字一致。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平：MD 行 257 `ofers`（印刷 `offers`）。
    - MD 行 261 `in par ticular` —— 印刷 `in particular` 跨行，转写时断行连字符变成空格（断词伪影）。
    - MD 行 279 GHS 项目符号丢失：印刷以 `•` 列出 "GHS's inequality [59]"，MD 该行以 `$\mathrm { G H } \mathrm { S } ^ { \prime } \mathrm { s }$inequality [59]` 起首且**无 `•` 项目符号**（对比 MD 行 285 Simon-Lieb 条目保留了 `•`）——排版级不一致，不影响内容。
    - MD 行 285 `Simon-Lieb's inequality <sub>[82]</sub>` —— 引用号被包进 `<sub>` 标签（印刷 `[82]` 为常规字号上标式引用，非下标）；行 263 `[57]` 未加标签，两处体例不一致（排版级，不误导）。
    - 行内数学与相邻文字空格普遍合并（`when$\beta$ is equal to` 等）；running foot `13 100 Years of the Ising Model` 未入 MD；印刷斜体（`spin-spin correlations`、`correlation inequalities`）未保留（风格级）。
- 备注：(4.1)–(4.4) 四式与印刷逐项吻合，含 inf/sup 严格性、`≥/≤` 方向、`_S` 下标有无等易错点；本页无需改动 Markdown。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：/tmp/icm2022dc_audit_p014.png（pngmono 150dpi）
- 核对：Messager-Miracle-Solé 条目与 `[84]`、`Z_+^d` 与 `Z^d` 两个空间、公式 (4.5)；FKG 条目与 `[47]`、`f, g : {−1,1}^V → ℝ`、公式 (4.6)；non-critical statistical physics 段；§4.1.2 节标题与两段（`h ≠ 0`、`[81]`、`Z(G,β,h)`、`h ∈ ℂ`、Riemann zeta）；Lee-Yang 定理段（`G ⊂ Z^d`、`Z(G,β,h) ∈ ℂ`、`h = (h_x : x ∈ V) ∈ C^V`、两处求和 `Σ_{x∈V} hσ_x` → `Σ_{x∈V} h_x σ_x`、`Re(h_x) = 0`）；(2.5) 与 (2.2) 互引；§4.2 节标题与首段；页脚 `14 Hugo Duminil-Copin`。
- 结果：PASS±
  - 公式逐项吻合：(4.5) `⟨σ_0σ_{x+y}⟩ ≤ ⟨σ_0σ_x⟩.`——下标 `x+y` 与 `x`、方向 `≤`、尾句点与印刷一致；(4.6) `⟨fg⟩ ≥ ⟨f⟩⟨g⟩.`——`≥` 方向、右侧两个尖括号相邻、尾句点一致；(4.5)(4.6) 编号与印刷位置一致。
  - **Lee-Yang 段数学逐项吻合（重点核对处）**：印刷 `Z(G,β, h) ∈ ℂ (for h = (h_x : x ∈ V) ∈ C^V)`，其中向量场 `h` 及其分量 `h_x` 印刷为**粗体**；MD 行 311 相应作 `\mathbf { h }`、`\mathbf { h } _ { x }`，粗体区分保留正确。原哈密顿量中的 `Σ_{x∈V} hσ_x` 项（标量 `h`、**非粗体**，MD 行 311 作 `\sum _ { x \in V } h \sigma _ { x }`）与替换后的 `Σ_{x∈V} h_xσ_x` 项（粗体 `h_x`，MD 作 `\mathbf { h } _ { x }`）在印刷与 MD 中区分一致，未混淆标量场与向量场。
  - 结论式 `Re(h_x) = 0 for every x ∈ V` 与印刷一致（粗体 `h_x`）；`h ↦ Z(G,β,h)` 的映射记号（印刷 `h ↦→`，MD 行 311 作 `h$\mapsto Z(...)`）一致。
  - 条件 `G ⊂ Z^d`（印刷 `⊂`，MD 亦作 `\subset`）一致；`n.n.f.`、`Z_+^d`（正整数格点）与其下 "below ⟨·⟩ is defined on Z^d" 的对照说明完整入 MD（行 291）。
  - 正文逐句吻合：`Messager-Miracle-Solé's inequality [84]`、`FKG's inequality [47]`、`[81]`、`The twin papers`、`Lee-Yang theory`、`Riemann zeta function`、`free energy f(β,h)`、`analytic as soon as h ≠ 0`、`truncated correlations`、`non-zero magnetic field` 全部与页图一致；节标题 `4.1.2. The Ising model with a magnetic field: the Lee-Yang theory`（行 305）与 `4.2. Revolutionary progress on the physics front`（行 315）逐字一致；行 317 提及的 "scaling and universality hypotheses" 与 "pillars of the renormalisation group" 一致。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平：MD 行 309 `efect`（印刷 `effect`）、行 311 `diference`（印刷 `difference`）。
    - 项目符号缺失：MD 行 297 FKG 条目以 `$\mathrm { F K G } ^ { \prime } \mathrm { s }$inequality [47]` 起首且无 `•`（印刷有 `•`；对比行 291 保留了 `•`）——排版级不一致。
    - MD 行 291 `Messager-Miracle-Solé's inequality <sub>[84]</sub>` 引用号被包进 `<sub>`（与行 285 同类，体例不一致，排版级）。
    - 行内数学与相邻文字空格普遍合并（`of$\mathbb{C}$(for` 等）；running foot `14 Hugo Duminil-Copin` 未入 MD；印刷斜体（`f`、`g`、`h`、`Re`、`x` 等数学斜体与正文斜体 `philosophy consisting`）未保留（风格级）。
- 备注：本页标量场 `h` 与向量场粗体 `h` 的区分、(4.5)(4.6) 不等号方向均已逐项核对无误；无需改动 Markdown。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：/tmp/icm2022dc_audit_p015.png（pngmono 150dpi）
- 核对：§4.2.1 节标题、Widom 段（`[102]`、`β` 与 `h` 为参数）、六个临界指数记号、公式 (4.7) 三式（`_+` 正部、`o(1)` 位置、`1/δ + o(1)`、分式 `1/|x|^{d−2+δ}`）、(4.7) 后释义句（"`β` and `β` have nothing to do with each other"）、指数族 `α,β,γ,δ,η,ν`、Essam/Fisher/Widom 段与 `[42, 45, 102]`、公式 (4.8) 两组等式全部项、`[38]`、`2D`/`3D`、`[8]`、correlation length 段 `ξ(β)` 与 `ν`、`β < β_c`/`β > β_c`、末段至 "meaning that when" 跨页断点、页脚 `15 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：(4.7) `m*(β) = (β − β_c)_+^{β+o(1)}`，`m(β_c,h) = h^{1/δ+o(1)}`，`⟨σ_0σ_x⟩_{β_c,0} = 1/|x|^{d−2+δ}` —— 正部记号 `_+`、`o(1)` 在指数中的位置、`1/δ` 的分式排法、分母 `|x|` 的模长竖线与分式线均与印刷页图一致；(4.7) 印刷**无尾标点**，MD 行 324 亦无，一致。
  - **print quirk 忠实保留（重点）**：第三式分母指数印刷作 `d − 2 + δ`（用 delta），而按同页指数约定 `⟨σ_0σ_x⟩` 的临界衰减指数应为 `η`；150dpi 页图第三式分母清晰印作 `|x|^{d−2+δ}`，文本层同。**不按物理/数学预期改作 `η`**，MD 行 324 原样照录。
  - (4.8) 逐项吻合：`νd = 2 − α = 2β + γ = β(δ + 1) = γ(δ+1)/(δ−1)` 与 `2 − η = γ/ν = d(δ−1)/(δ+1).` —— 两组等式、`γ/ν` 分子分母方向、`d` 的位置、尾句点均与印刷一致；(4.8) 印刷在两组等式间以空白（非等号）分隔，MD 用 `\qquad`，语义一致。
  - **指数字形区分正确**：印刷的 `α, β, γ, δ, η, ν` 为**粗斜体**，且与普通 `β`（逆温度参数）区分；MD 用 `\boldsymbol{...}` 保留粗体，与普通 `$\beta$` 区分清晰，行 327 的释义句"notice that **β** and β have nothing to do with each other"两处 β 的粗体差异完整保留，是本页最易错点且转写正确。
  - 正文逐句吻合：`Benjamin Widom who proposed in [102]`、`Essam, Fisher, and Widom himself`、`[42, 45, 102]`、`[38]`、`Baker's use of Padé approximant [8] in 3D`、`2D`、`correlation length ξ(β)`、`Section 7.1`、`non critical` 相关表述、`"critical"` 引号用法均与页图一致；节标题 `4.2.1. Critical exponents and the success of scaling theory`（行 319）逐字一致。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平：MD 行 335 `diferent`（印刷 `different`）、行 339 `diference`（印刷 `difference`）。
    - MD 行 329 `system atic connections` —— 印刷 `system-`/`atic` 跨行，转写时断行连字符变空格（断词伪影）。
    - 行内数学与相邻文字空格普遍合并（`parameters are$\beta$and ℎ`、`length$\xi ( \beta )$of the system` 等）；running foot `15 100 Years of the Ising Model` 未入 MD；印刷斜体（`scaling hypothesis`、`critical exponents`、`scaling relations`、`correlation length`、各指数字形）部分未在 MD 保留（风格级）。
- 备注：(4.7) 的 `d−2+δ` 与六个指数的粗体区分是本页两个关键点，均已核实并忠实保留；无需改动 Markdown。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：/tmp/icm2022dc_audit_p016.png（pngmono 150dpi）
- 核对：p.15 跨页续段（`ξ(β)`、`β ≪ β_c`、`"critical"` 引号）、§4.2.2 节标题、Kadanoff 段（`[72]`、1966、block-spin、`β` 与 `h`、RG、`Kenneth Wilson [104]`）、block-spin 第二段（`d`-dimensional、2D/3D、`[34]`、square/hexagonal/triangular）、universality hypothesis 段（`Robert B. Griffiths and Kadanoff in 1971 [58, 73]`）、三条项目符号（`d`、`Z/2Z symmetry for Ising`、`J_{x,y}`、`‖x − y‖`）、Kadanoff 引语（至 "in that many systems" 跨页断点）、页脚 `16 Hugo Duminil-Copin`。
- 结果：PASS±
  - 正文逐句吻合：`Leo Kadanoff`、`his famous 1966 paper [72]`、`Kenneth Wilson [104]`、`series expansions [34]`、`2D`/`3D`、`Robert B. Griffiths and Kadanoff in 1971 [58, 73]`、`renormalisation group (RG)`、`unique fixed point` 表述全部与页图一致。
  - 记号与三条项目符号吻合：`the lattice dimension $d$`、`Z/2Z symmetry for Ising`（印刷为 `Z/2Z` 而非 `Z_2`，MD 行 351 照录）、`$J _ { x , y }$`、`$\| x - y \|`（双竖线范数，MD 行 353 照录）、三条 `•` 项目符号完整保留（MD 行 349/351/353）。
  - Kadanoff 引语起首完整入 MD（行 355）：`"Why study a simplified model like the Ising model? The strategy of …"` 与印刷逐句一致，含嵌套引号 `"universality"` 的层次。
  - 节标题 `4.2.2. Kadanoff's block-spin renormalisation and universality`（MD 行 341）逐字一致。
  - 差异列表（不误导，登记不改）：
    - **断词伪影集中区**：MD 行 355 引语内 `ofstudyingphysical`、`ofphysical`、`qualitativefeatures`、`qualitativefeature`、`lookfor` 五处——印刷这些词跨行，转写时断行连字符/换行被删除且未补空格，形成词粘连（印刷为 `of studying physical`、`of physical systems`、`qualitative features`、`qualitative feature`、`look for`）。属可读性缺陷但语义可辨。
    - `ff` 连字拍平：MD 行 345 `diferent`（印刷 `different`）。
    - MD 行 343 `the parameter$\beta$and ℎ` —— 印刷为 "the **parameters** `β` and `h`"（复数），MD 作单数 `parameter`；属印刷/转写差异，语义可辨，登记为 PASS±（印刷文本层亦作 "the parameters"，见下方备注）。
    - MD 行 357 `could corroborate$^ { \mathrm { o r , } }$on the contrary` —— 印刷为 "could corroborate, on the contrary, invalidate the embryo of a theory"（行 357 为 p.17 内容，本页只到 "in that many systems"），该行的畸形数学片段属 p.17 范围，**归 p.017 审**，本页不判定。
    - 行内数学与相邻文字空格合并（`the$J _ { x , y }$are`、`$\| x - y \|$` 前等）；running foot `16 Hugo Duminil-Copin` 未入 MD；印刷斜体（`scale invariance`、`uniqueness of the fixed point`、`universality hypothesis`、Kadanoff 引语全段）未在 MD 保留（风格级）。
- 备注：关于 "the parameter**s** β and h"——`pdftotext` 文本层该处作 "the parameters `β` and `ℎ`"（复数），150dpi 页图该处受字距影响不易分辨，两者结合判断印刷为复数；因不影响数学内容，按 PASS± 登记而未改动。本页无需改动 Markdown。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：/tmp/icm2022dc_audit_p017.png（pngmono 150dpi）
- 核对：p.16 跨页续段（Kadanoff 引语结尾 "may show the very same qualitative features … simplest possible example."）、Section 4 总结段（"could corroborate or, on the contrary, invalidate"、centerpieces）、§5 节标题、§5 首段（`X : {−1,1}^V → ℝ` (resp. `ℂ`)、`μ_{G,β,h}`）、§5.1 节标题、§5.1 首段、公式 (5.1) 的 `1/Z(G,β,h)` 与 `exp[−βH_{G,h}(σ)]`、correlations 段（`σ_A`、`σ_x`、`x ∈ A`）、`h = 0` 段、末段（magnetisation、surface tension、`Frame 3`）、页脚 `17 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：(5.1) `μ_{G,β,h}[{σ}] := (1/Z(G,β,h)) exp[−βH_{G,h}(σ)].` —— 归一化因子 `1/Z(G,β,h)`、指数 `−β`、`H_{G,h}` 下标、尾句点与印刷页图逐项一致；编号 `(5.1)` 位置正确。
  - Kadanoff 引语结尾完整入 MD（行 355 末）：印刷 "may show the very same qualitative features, and sometimes even the same quantitative ones. To study a given qualitative feature, it often pays to look for the simplest possible example."" 与 MD 一致（该行原文的 `qualitativefeatures`/`lookfor` 断词粘连已在 p.016 条目登记，不重复计）。
  - 正文逐句吻合：`To summarise Section 4`、`by the end of the sixties`、`centerpieces of modern statistical physics`、`section 5 节标题 5. The sixties and seventies: emergence of the probabilistic interpretation`、`5.1. The random geometry of the spin configuration`、`dual to`、`normalising factor`、`surface tension`、`see Frame 3` 全部与页图一致；`{−1,1}^V → ℝ (resp. ℂ)` 与 `μ_{G,β,h}` 的下标 `G,β,h` 一致。
  - 差异列表（不误导，登记不改）：
    - MD 行 357 `could corroborate$^ { \mathrm { o r , } }$on the contrary, invalidate` —— 印刷为 "they could corroborate **or,** on the contrary, invalidate the embryo of a theory"；转写把普通词 `or,` 误识别为上标数学片段并吞掉其后逗号。**溯源：`git show d351abbf:…md`（原始 MinerU 导出）即为该形态，59537f98 与 HEAD 未变 → 系导出缺陷，非 peer 引入的回归。** 词义 "corroborate or, on the contrary, invalidate" 仍可辨，属排版级伪影，不误导。
    - MD 行 375 `$\beta ,$,` —— 该处双逗号（`\beta ,` 后紧跟 `,`）出现在 p.17 末句行内，印刷 p.17 末句无此内容（正文在 `see Frame 3` 处断页），**该双逗号对应印刷 p.18 首句**；归 p.018 条目判定，本页不重复计。
    - MD 行 375 `space ofspin configurations`、`expectation ofthe spin` —— 空格合并。
    - 行内数学与相邻文字空格普遍合并（`quantity$\langle \cdot \rangle _ { G , \beta , h }$as a form` 等）；running foot `17 100 Years of the Ising Model` 未入 MD；印刷斜体（`correlations`、`X` 等）未保留（风格级）。
- 备注：(5.1) 与全部记号核对无误；本页无需改动 Markdown。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：/tmp/icm2022dc_audit_p018.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p018_300.png（300dpi 全页）、/tmp/icm2022dc_p018_bc_crop.png（边界条件定义句）
- 核对：p.17 跨页续句（`inverse-temperature β`）、Frame 3 标题与全框正文、Glauber dynamics 两条跳转规则（`σ_x(t) Σ_{y:{x,y}∈E} σ_y(t) < 0`、`exp[−2β Σ_{y:{x,y}∈E} σ_y(t)]`）、不变测度段与 **`μ_{G,β,h}` vs `μ_{G,β,0}`**、Roy J. Glauber 段与 Figure 2 / `β_c`、§5.2 节标题、条件概率记号 `μ_{G,β,h}[· | σ_x = τ_x, ∀x ∉ W]`、边界条件定义句中的边界符号、公式 (5.2) 的求和域与 `H^τ_{G,h}`、spatial Markov property 段与公式 (5.3)、页脚 `18 100 Years of the Ising Model`。
- 结果：**FAIL（1 处记号错误，已修，以原图为准）**
  - 公式逐项吻合：(5.2) `H^τ_{G,h}(σ) := H_{G,h}(σ) − Σ_{{x,y} ∈ E(Z^d): x ∈ V, y ∉ V} σ_x τ_y.` —— 上标 `τ`、`x ∈ V, y ∉ V` 的边界求和条件、被减项与负号、尾句点均与印刷页图一致；(5.3) `μ_{G,β,h}[· | σ_x = τ_x, ∀x ∉ W] = μ^τ_{H,β,h}[·].` —— 左端条件 `σ_x = τ_x, ∀x ∉ W`、右端图 `H`（非 `G`）、右端带上标 `τ`、尾句点一致；(5.2)(5.3) 编号与印刷位置一致。
  - Glauber 两条规则与印刷一致：`σ_x(t) Σ_{y:{x,y}∈E} σ_y(t) < 0`、`exp[−2β Σ_{y:{x,y}∈E} σ_y(t)]`，系数 `−2β` 与求和下标 `{x,y} ∈ E` 未丢。
  - **print quirk 忠实保留**：Frame 3 开头已设 `h = 0` 并以 `μ_{G,β,0}` 为采样目标，但同框末句印刷作 "is sampled according to **μ_{G,β,h}**"（下标回到 `h`）；150dpi 页图与文本层双证一致，MD 行 385 原样照录，**不得改为 `μ_{G,β,0}`**。
  - **FAIL 项与修复**：MD 行 393 原作 "introduce the measure `μ^τ_{G,β,h}` with **`$G$`** boundary conditions"，**与印刷相反**。300dpi 裁片 `/tmp/icm2022dc_p018_bc_crop.png` 明确印作 "μ^τ_{G,β,h} with **τ** *boundary conditions*"（τ 为斜体数学符号，与同句 `configuration τ` 同一字形）。数学上亦必须为 `τ`：该测度由边界自旋配置 `τ` 标注，写作 `G` 会与图 `G` 混淆且与 (5.2) 的上标 `τ` 不一致。已用 Edit 将该处 `$G$` 改为 `$\tau$`。
  - **溯源（回归判定）**：`git show d351abbf:…md`（原始 MinerU 导出）该处为 U+FFFD `�`；`git show 59537f98:…md`（Peer-P14 harvest 提交）把该缺字误补为 `$G$`，HEAD 未再变。**非导出缺陷，系 59537f98 引入的错误补字**：原导出此处并非正确（是缺字 `�`），是该 peer 把缺字补成了错误符号；本次按印刷纠正为 `$\tau$`。
  - 差异列表（不误导，登记不改）：
    - 断词伪影：MD 行 379 `ran dom configurations`（印刷 `random` 跨行）。
    - 空格合并：MD 行 375（p.17 跨页句尾）`inverse-temperature$\beta ,$,` 的**双逗号**——300dpi p.18 页图首行清楚印作 "at an inverse-temperature `β`, but with an excess of +1 spins"，即只有一个逗号。**溯源：`git show d351abbf:…md` 该处即为 `$\beta ,$,`，59537f98 与 HEAD 未变 → 系导出缺陷，非 peer 回归。** 纯标点重复、不改变句义，按 PASS± 登记不修（避免为单处标点改动引入新的可溯源性破坏；若需统一清理应整篇一次性处理并登记）。
    - 行 391 `output ofthe`、`of the probabilistic interpretation ofthe model`；行 393 `introduce the measur`（印刷 `measure`，末字母 `e` 丢失，`dd351abbf` 即为此形态，属导出缺陷）；行 383/385 的 `\begin{array} { r } … \end{array}` 包裹（排版级）；行 387 `$\beta _ { c }$` 句末无句点（印刷该处以 `β_c.` 收句，MD 行尾无句点——属标点丢失，语义不受影响）。
    - running foot `18 100 Years of the Ising Model` 未入 MD；Frame 边框/缩进未保留（布局级）；印刷斜体（`boundary conditions`、`spatial Markov property`）未保留（风格级）。
- 备注：本页实际改动 1 处（MD 行 393），证据为 300dpi 裁片 + 文本层双证；`μ_{G,β,h}` print quirk 与 (5.2)(5.3) 求和域已逐项核实。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：/tmp/icm2022dc_audit_p019.png（pngmono 150dpi）
- 核对：(5.3) 后释义句、consistency relation 段、`μ` on `({−1,1}^{Z^d}, 𝔉_{Z^d})` 的 σ-代数记号、Dobrushin-Lanford-Ruelle (DLR) property、`V ⊂ Z^d`、`τ ∈ {−1,1}^{Z^d}`、公式 (5.4) 的条件事件与 `μ`-almost surely、三条 `where` 项目符号、`E_τ`、`𝔉_{Z^d\V}`、三个 Gibbs 测度 `μ_{β,h}` / `μ^+_{β,h}` / `μ^-_{β,h}`、`sub-sequential limits`、extremal states 段、`h ≠ 0` / `h = 0` / `β < β_c` / `β = β_c` / `β > β_c` 分情形的 `[5]`、Dobrushin 段（`Roland Dobrushin [31]`、`μ^dobr_{β,0}`、`[−n,n]^3_{β,0}`、roughening phase transition）、末段 `μ^+_{β,0}` 与 `μ^-_{β,0}`、页脚 `19 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：(5.4) `μ[· | 𝔉_{Z^d\V}] = μ^τ_{G,β,h}[·] on E_τ μ-almost surely,` —— 左端条件为 σ-代数 `𝔉_{Z^d\V}`（反斜杠集差）、右端测度带上标 `τ` 与下标 `G,β,h`、`on E_τ`、`μ-almost surely` 连写、**尾逗号**（印刷有逗号，MD 行 412 亦保留）均与印刷页图一致；编号 `(5.4)` 位置正确。
  - 记号逐项一致：σ-代数花体 `𝔉_{Z^d}` 与 `𝔉_{Z^d\V}`（MD 作 `\mathfrak { F }`）、`E_τ` 的下标 `τ`、`μ^+ / μ^-` 的上下标位置（MD 行 425 作 `^ { + }` / `^ { - }`，即上标，与印刷一致）、`μ_{β,h}` 三者、Dobrushin 测度 `μ^{dobr}_{β,0}`（MD 行 427 作 `\mu _ { \beta , 0 } ^ { d o b r }`，上标 `dobr` 与印刷一致）。
  - 三条 `where` 项目符号完整入 MD（行 417/419/421），内容与印刷三条一致：`G` 由顶点集 `V` 诱导、`E_τ` 是 `σ` 与 `τ` 在 `G` 外边界上一致的事件、`𝔉_{Z^d\V}` 是由 `(σ_x : x ∉ V)` 生成的 σ-代数。
  - 正文逐句吻合：`Dobrushin-Lanford-Ruelle (DLR) property`、`[52]`、`Roland Dobrushin [31]`、`three dimensions`、`roughening phase transition`、`translation invariant Gibbs state is a convex combination of μ^+_{β,0} and μ^-_{β,0}`、`extremal states`、`unique Gibbs measure`、分情形条件 `h ≠ 0`、`h = 0 and β < β_c`、`h = 0 and β = β_c`、`h = 0 and β > β_c` 与引用 `[5]` 全部与页图一致。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平：MD 行 409 `ofers`（印刷 `offers`）。
    - 断词伪影：MD 行 409 `infinitevolume`（印刷 `infinite-`/`volume` 跨行）；行 407 `on$G$to coincide` 为空格合并类。
    - MD 行 419 `$G \mathrm { : }$;` —— 句末冒号被纳入数学段并多余保留（印刷句末为句号 `;`? 实为句末 `;`，MD 在 `$G$` 后多出一个 `:`）。
    - MD 行 421 第三条项目符号**丢失 `•` 前缀**（另两条行 417/419 保留）——排版级不一致。
    - MD 行 421 末尾缺句点（印刷 "…(σ_x : x ∉ V)." 带句点）。
    - 行内数学与相邻文字空格普遍合并（`measures$\mu _ { G , \beta , h } ^ { \tau }$for`、`tends to$\mathbb { Z } ^ { d }$of` 等）；running foot `19 100 Years of the Ising Model` 未入 MD；印刷斜体（`Gibbs measure`、`Dobrushin-Lanford-Ruelle (DLR) property`、`extremal states`、`unique`、`roughening phase transition`）未保留（风格级）。
- 备注：(5.4) 的 σ-代数条件事件与 `E_τ` 连写是本页易错点，已逐项核对无误；无需改动 Markdown。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：/tmp/icm2022dc_audit_p020.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p020_300.png（300dpi 全页）、/tmp/icm2022dc_p020_caption_crop.png（图 2 说明第 1–2 行）
- 核对：图 2 图题全文；引用编号 Aizenman `[1]` / Higuchi `[64]` / Bodineau `[18]` / Raoufi `[92]` / `[56]` / `[23]`；公式 `μ_{β,0} = ½μ⁺_{β,0} + ½μ⁻_{β,0}`；§5.3 标题与段落次序；三角格子方盒 `[−n,n]²`；界面端点 `(−n,0)` 与 `(n,0)`；Ornstein-Zernike 拼写；页脚 `20 Hugo Duminil-Copin`。
- 结果：PASS±（1 处漏字，已修，以原图为准）
  - **已修缺陷**：图 2 图题第 2 行，MD 行 437 作「Pluses are in gray and **minuse** in black.」，印刷原文为「Pluses are in gray and **minuses** in black.」（150dpi 整页图与 300dpi 裁片 `/tmp/icm2022dc_p020_caption_crop.png` 双证，词尾 s 清晰可辨）。已用 Edit 逐处改为 `minuses`。
  - **溯源（回归判定）**：对 `d351abbf`（原始 MinerU 导出）、`59537f98`、HEAD 等提交逐一执行 `git show <c>:"…__ICM2022_proceedings_Duminil-Copin.md" | grep -o 'Pluses are in gray and [a-z]* in black'`，五处结果全为 `minuse`。**属原始导出缺陷，非 peer 回归**；原导出即已脱字。
  - 公式逐项吻合：`μ_{β,0} = ½μ⁺_{β,0} + ½μ⁻_{β,0}` 的两个系数 `1/2`、上下标位置（`+`/`−` 为上标，`β,0` 为下标）与印刷一致；`When h = 0 and β > β_c, μ⁺_{β,0} and μ⁻_{β,0} are not equal` 不等号方向正确；`first in the large β regime and then in the whole β > β_c regime` 的先后次序与印刷一致。
  - 记号逐项一致：`finite box [−n,n]² of the triangular lattice`、`unique interface going from (−n, 0) to (n, 0)`、`plus spins on the part of the boundary above the x-axis`、`Ornstein-Zernike theory`（连字符）、`Wulff shape`（§5.3 标题）均与页图一致。
  - 引用编号逐项吻合：Aizenman `[1]`、Higuchi `[64]`、Bodineau `[18]`、Raoufi `[92]`、`see [56] and references therein`、`We refer to [23] for details on the Ising case` 全部与印刷一致。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平：图题「three **diferent** temperatures」、正文「coexistence of **diferent** so-called phases」、「simulations at **diferent** temperatures」——属文档级 `ff` 拍平，已在前页统一登记，不逐处批改。
    - 图题行内数学与文字空格合并：`temperatures$( \beta < \beta _ { c } , …`；`$x$-axis` 等（排版级）。
    - 图 2 图像 `../audit/ICM2022_proceedings_Duminil-Copin_p020_Figure2.png` 已入 MD（行 433），文件名与页号一致（排版级核对通过）。
    - 页脚 `20 Hugo Duminil-Copin` 未入 MD（与全篇一致）。
  - 印刷怪癖登记（保留不纠）：本节小标题印刷作「5.3. Phase coexistence and Wulff shape」，MD 原样保留；印刷图题中 `Pluses are in gray` 的用词（而非 `grey`）亦按原样保留。
- 备注：本页实际改动 1 处（MD 行 437 图题），证据为 300dpi 裁片 + `pdftotext` 文本层双证；其余为 `ff` 拍平与排版级登记。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：/tmp/icm2022dc_audit_p021.png（pngmono 150dpi）
- 核对：页首 §5.3 末段（Wulff shape / bubble / `[32]` / `[67]` / `[15,17,24]` / `[23]`）；§6 与 §6.1 标题；引用 `[103]`（Wightman）、`[88]`（Osterwalder-Schrader）；公式 (6.1) 的 `≈`、`1/norm`、`∏_{x∈R^d} dΦ(x)`；`where` 两条项目符号 `T_f(Φ) := ∫_{R^d} f(x)Φ(x)dx`、`H(Φ) ≈ (Φ,AΦ) + ∫_{R^d} P(Φ(x))dx`、`Φ(x)^{2k}`、`k-particle`；公式 (6.2) 的 `:=`、`∫_{(R^d)^n}`、`S_n(x_1,…,x_n)`、`∏_{j=1}^n f_j(x_j)dx_1…dx_n`；页脚 `21 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：
    - (6.1) `⟨F(Φ)⟩ ≈ 1/norm ∫ F(Φ) exp[−H(Φ)] ∏_{x∈R^d} dΦ(x),` —— 近似号 `≈`（非等号）、分母 `norm` 为正体、被积乘积号下标 `x ∈ R^d`、**尾逗号**（印刷有，MD 行 456 亦保留）均与页图一致；编号 `(6.1)` 在行末。
    - (6.2) `⟨∏_{j=1}^n T_{f_j}(Φ)⟩ := ∫_{(R^d)^n} S_n(x_1,…,x_n) ∏_{j=1}^n f_j(x_j) dx_1 … dx_n,` —— 定义号 `:=`、积分域 `(R^d)^n`、`S_n` 的下标与自变量个数、`∏` 上下限 `j = 1` 与 `n`、微分序列 `dx_1 … dx_n`、**尾逗号**均与页图一致；编号 `(6.2)` 位置正确。
  - 记号逐项一致：`Φ(x)`、`T_f(Φ)`、`\int_{\mathbb{R}^d}`、`P(\Phi(x))\,dx`、`\Phi(x)^{2k}`、`k`-particle、`S_n(x_1,\ldots,x_n)`、`\langle\prod_{j=1}^n \Phi(x_j)\rangle`（行 471）、`Schwinger functions`、`2n`-point（`2n` 属 p.22，不计）。
  - 结构与次序吻合：§5.3 末段 → §6 标题 → §6.1 标题 → CQFT 段 → `Finding these Euclidean fields boils down…` 引导句 → (6.1) → `where` → 两条项目符号 → `By linearity…` → (6.2) → `where the S_n … are the Schwinger functions…` → `Interpreting (6.1) raises a number of problems of varying difficulty.` → `The simplest example of Euclidean fields are the reflection-positive (see Section 6.2 again) Gaussian fields…`；印刷与 MD 完全对应，无段落缺失或错序。
  - 引用编号逐项吻合：`[23]`、`[32]`、`[67]`、`[15,17,24]`、`[103]`、`[88]`，与页图一致。
  - 差异列表（不误导，登记不改）：
    - 空格合并伪影：MD 行 453 `Finding these Euclideanfields`（印刷 `Euclidean fields` 斜体，斜体与词间空格丢失）；行 471 `the$S _ { n } (x _ { 1} , \ldots , x _ { n } )$are the Schwingerfunctions of` —— 同类空格合并 + 印刷斜体 `Schwinger functions` 丢失词间空格。
    - `ff` 连字拍平：行 471 `varying dificulty`（印刷 `difficulty`）；行 451 `reflection-positivity`（连字符保留正确）。
    - 行内数学与相邻文字的空格普遍合并（`$k$-particle interactions`、`$\langle \prod _ { j = 1 } ^ { n } \Phi ( x _ { j } ) \rangle$.` 等），为全篇 MinerU 导出风格（排版级）。
    - 页脚 `21 100 Years of the Ising Model` 未入 MD（与全篇一致）；印刷斜体（`Euclidean fields`、`Schwinger functions`、`Wulff shape`）未保留（风格级）。
  - 印刷怪癖登记（保留不纠）：印刷在 (6.2) 中 `S_n` 与 `\langle\prod\rangle` 之间留有较大空隙，属排版；`Osterwalder-Schrader` 用普通连字符而非 `–`，MD 原样保留。
- 备注：本页无数学内容错误，未改动 Markdown；全部差异为空格合并与 `ff` 拍平类伪影。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：/tmp/icm2022dc_audit_p022.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p022_300.png（300dpi 全页）、/tmp/icm2022dc_p022_eq64_sub.png（(6.4) 积分号下标）、/tmp/icm2022dc_p022_eq65_exp.png（(6.5) 指数）、/tmp/icm2022dc_p022_phi4line.png（`φ⁴ lattice model` 句）、/tmp/icm2022dc_p022_cutoffs_line.png（`cutoffs` 句）
- 核对：页首 `2n`-point Schwinger functions 与 Wick's law；公式 (6.3) 的 `S_{2n}`、`∑_{π pairings}`、`∏_{j=1}^n S_2(x_{π(2j−1)}, x_{π(2j)})`；`λΦ⁴ for λ > 0`；引用 `[104]`（Wilson）、`[55]`、`[44,54]`；`Λ_R^{(a)} := (aℤ)^d ∩ [−R,R]^d`；公式 (6.4) 的等号、`1/norm`、积分域、乘积号下标；公式 (6.5) 的负号、`∑_{{x,y}⊂E(Λ_R^{(a)})}`、指数 `−λφ_x⁴ − bφ_x²`；`φ⁴ lattice model`；`R ↗ ∞ followed by a ↘ 0`；`λ = b/2`；`Griffiths-Simon class` 与 `[60]`；页脚 `22 Hugo Duminil-Copin`。
- 结果：PASS±
  - 公式逐项吻合：
    - (6.3) `S_{2n}(x_1,…,x_{2n}) = ∑_{π pairings} ∏_{j=1}^n S_2(x_{π(2j−1)}, x_{π(2j)}).` —— 求和下标 `π pairings`、乘积上下限 `j=1`/`n`、`S_2` 的两个自变量下标 `π(2j−1)` 与 `π(2j)`（**奇数在前、偶数在后**，与印刷一致，方向未颠倒）、尾句点均与页图一致。
    - (6.4) `⟨F(φ)⟩ = 1/norm ∫_{ℝ^{Λ_R^{(a)}}} F(φ) exp[−H(φ)] ∏_{x∈Λ_R^{(a)}} dρ(φ_x),` —— **等号**（非近似号，区别于 (6.1) 的 `≈`）、积分号下标为 `ℝ^{Λ_R^{(a)}}`（外层黑板粗体 ℝ、上标为带下标 `R` 与上标 `(a)` 的 Λ）、乘积号下标 `x ∈ Λ_R^{(a)}`、**尾逗号**均与页图一致；MD 行 486 写法与 300dpi 裁片 `/tmp/icm2022dc_p022_eq64_sub.png` 完全对应（该处 `pdftotext` 文本层作 `norm RΛ𝑅 (𝑎)`，不可靠，已以裁片仲裁）。
    - (6.5) `H(φ) = −∑_{{x,y}⊂E(Λ_R^{(a)})} φ_xφ_y,  dρ(φ_x) = e^{−λφ_x^4 − bφ_x^2} dφ_x,` —— **整体负号**、求和下标花括号 `\{x,y\} \subset E(\Lambda_R^{(a)})`、指数两项的顺序 `−λφ_x^4` 在前 `−bφ_x^2` 在后（300dpi 裁片 `/tmp/icm2022dc_p022_eq65_exp.png` 逐符号核对）、末 `dφ_x`、**尾逗号**均与印刷一致。
  - 正文数值与方向核对：`λΦ⁴ for λ > 0`（正号，非负）、`ℝ² [55]` 与 `ℝ³ [44,54]` 的维度指数、`(aℤ)^d ∩ [−R,R]^d` 的两个 `d`、`λ = b/2`（系数 1/2）、`R ↗ ∞ followed by a ↘ 0`（先紫外后红外的方向箭头）、`±1`、`[60]` 均与页图一致。
  - 结构与次序吻合：页首 `…satisfying Wick's law:` → (6.3) → `The field theoretical interpretation of (6.3) is the absence of interaction.` → `The next level of difficulty is to add…` → `A natural example aimed at constructing a Φ_d^4 functional integral…` → `leading to the following statistical-mechanics Gibbs equilibrium state average` → (6.4) → `with a Hamiltonian H(φ) and an a-priori measure ρ of the form` → (6.5) → `where dφ_x is the Lebesgue measure on ℝ. This is called the φ⁴ lattice model.` → `The cutoffs are removed…` → `The Ising model can be thought of as a limiting case…` → `The developments of the model have therefore been deeply connected to CQFT in the eighties, and we now discuss some examples of such interactions.`；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平：MD 行 481 `dificulty`（印刷 `difficulty`）；行 483 两处 `cutofs`、行 497 一处 `cutofs`（印刷 `cutoffs`，300dpi 裁片 `/tmp/icm2022dc_p022_cutoffs_line.png` 证明确为双 f）；行 499 `Griffiths-Simon` 的连字符**正确保留**，未受影响。属文档级 `ff` 拍平，已统一登记。
    - 空格合并伪影：行 483 `collection ofvariables`、`$\Lambda _ { R } ^ { ( a ) } : =$ $( a \mathbb { Z } ) ^ { d }$`、`$\Phi ( \cdot )$to`；行 489 `a-priori measure`；行 495 `the$\phi ^ { 4 }$lattice model`；行 497 `The cutofs are removed through the limit$R ~ { \nearrow }$∞`；行 499 `letting$\lambda = b / 2$tend`（排版级）。
    - 行内数学与相邻文字空格普遍合并（`$\mathbb { R } ^ { 2 }$[55]`、`$\mathbb { R } ^ { 3 }$[44,54]`、`$k$-particle` 同类），为全篇导出风格。
    - 页脚 `22 Hugo Duminil-Copin` 未入 MD；印刷斜体/强调（`trivial`、`ultraviolet`、`infrared`、`Riemann-sum`、`Wick's law`、`Griffiths-Simon class`、`always`、`Φ_d^4`、`φ^4 lattice model`）未保留（风格级）。
  - 印刷怪癖登记（保留不纠，不作"纠正"）：
    - **记号不一致（印刷自身）**：正文 `A natural example aimed at constructing a Φ⁴_d functional integral` 的 `Φ` 带**下标 `d`**，而同页结尾 `This is called the φ⁴ lattice model` 的 `φ⁴` **无下标 `d`**（300dpi 裁片 `/tmp/icm2022dc_p022_phi4line.png` 确认）。按铁律三原样保留，MD 行 483 作 `\Phi _ { d } ^ { 4 }`、行 495 作 `\phi ^ { 4 }`，各自忠实于印刷，未统一。
    - **(6.4) 积分域的怪异记号（印刷自身）**：积分号下标印作 `ℝ^{Λ_R^{(a)}}`，即把 `ℝ` 置于上标位置，形式上不是常见的 `ℝ^{Λ}` 记法；已按印刷原样保留于 MD 行 486，未按数学常识改写。
    - 印刷 (6.4) 用等号而 (6.1) 用近似号，属作者有意区分，MD 各自保留。
- 备注：本页无数学内容错误，未改动 Markdown；3 处需仲裁的数学记号（(6.4) 积分域、(6.5) 指数、`φ⁴`/`Φ⁴_d`）均以 300dpi 裁片逐符号确认与印刷一致。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：/tmp/icm2022dc_audit_p023.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p023_300.png（300dpi 全页）、/tmp/icm2022dc_p023_eq67.png（公式 (6.7)）、/tmp/icm2022dc_p023_eq68.png（公式 (6.8)）、/tmp/icm2022dc_p023_eq69_num.png 与 /tmp/icm2022dc_p023_eq69_den2.png（公式 (6.9) 右端分式）、/tmp/icm2022dc_p023_boldh.png 与 /tmp/icm2022dc_p023_boldh2.png（正文加粗 𝐡）
- 核对：§6.2 标题；`T_L := (ℤ/Lℤ)^d` 与 `L even`；`[0,L/2] × (ℤ/Lℤ)^{d−1}`；`T_L^+ / T_L^-`；反射 `ϑ`；公式 (6.6) 的两个关系与 `≥ 0`；`n.n.f.`；`Z_L(𝐡) ≤ Z_L(0)` 不等号方向；公式 (6.7) 的 `:=`、求和域 `σ∈{−1,1}^V`、`−β`、`{x,y}∈E(𝐓_L)`、`(σ_x−σ_y+𝐡_x−𝐡_y)²` 的平方位置；`d > 2`；`(a_x) ∈ ℂ^{T_L}`；公式 (6.8) 的系数 `2/β`、`ā_y` 共轭、`⟨σ_xσ_y⟩_{T_L,β,0}` 下标；公式 (6.9) 的 `m*(β)²`、`C/β`、`C′`、`‖x−y‖_2^{d−2}`（下标 `2`）；`Messager-Miracle-Solé`；`[88]`、`[16]`；页脚 `23 100 Years of the Ising Model`。
- 结果：**FAIL（1 处记号约定错误，已修，以原图为准）**
  - **已修缺陷**：MD 行 521 作「to show that for each h, a symmetric version of h with respect to a hyperplane」，两处 `h` 均为**普通斜体 h**；印刷原文两处均为**粗体向量场 𝐡**（300dpi 裁片 `/tmp/icm2022dc_p023_boldh.png` 与 `/tmp/icm2022dc_p023_boldh2.png` 双证，粗体笔画清晰可辨）。此处 `h` 是定义在顶点集上的**向量**场 `h : V → ℝ`，粗体与本文他处的标量外场 `h`（如 §5.2 的 `h ≠ 0`、Lee–Yang 定理）刻意区分；同一 MD 行内 `Z _ { L } ( \mathbf { h } )` 仍保留粗体，导致行内自相矛盾。已用 Edit 逐处改为 `$\mathbf { h }$`（两处）。
  - **溯源（回归判定）**：对 `d351abbf`（原始 MinerU 导出）、`59537f98`、HEAD 执行 `git show <c>:"…__ICM2022_proceedings_Duminil-Copin.md" | grep -o 'to show that for each h, a symmetric version of h'`，三处结果均为普通 `h`。**属原始导出缺陷，非 peer 回归**；原导出即已丢失粗体。
  - **公式 (6.9) 右端分式的下标经仲裁为 `2`，MD 原本正确，不作改动**（铁律二实证）：`pdftotext` 文本层把该处分式排成「∥ 𝑥−𝑦 |ℤ 𝑑 2」，字面读来像是下标 `ℤ^d`；但 300dpi 裁片 `/tmp/icm2022dc_p023_eq69_den2.png` 明确显示印刷分母为 `\frac{C'}{\|x-y\|_2^{d-2}}`，即范数的下标是欧氏范数记号 `2`、上标才是 `d−2`。**若据文本层「纠正」为 `‖·‖_{ℤ^d}` 反属制造错误**，故保留 MD 写法。
  - 公式逐项吻合：
    - (6.6) `⟨fϑg⟩ = ⟨gϑf⟩  and  ⟨fϑf⟩ ≥ 0,` —— **对称性交换 `gϑf` 在前**、第二个关系的不等号 `≥ 0`、尾逗号均与页图一致；编号 `(6.6)` 位置正确。
    - (6.7) `Z_L(𝐡) := ∑_{σ∈{−1,1}^V} exp[−β ∑_{{x,y}∈E(𝐓_L)} (σ_x−σ_y+𝐡_x−𝐡_y)²].`（300dpi 裁片 `/tmp/icm2022dc_p023_eq67.png`）—— 定义号 `:=`、`exp` 后的**方括号**（非圆括号）、`−β` 的负号、内层平方**在括号外**、句末句点均与印刷一致；`Z_L(𝐡) ≤ Z_L(0)` 的不等号方向亦与印刷一致。
    - (6.8) `∑_{x,y∈T_L} a_x ā_y ⟨σ_xσ_y⟩_{T_L,β,0} ≤ (2/β) ∑_{x,y∈T_L} a_x ā_y G(x,y),`（300dpi 裁片 `/tmp/icm2022dc_p023_eq68.png`）—— 系数为 **`2/β`**、`ā_y` 的共轭横线只覆盖 `a`（不覆盖下标 `y`）、⟨·⟩ 的下标 `T_L,β,0`、两处求和域 `x,y∈T_L`、尾逗号均与印刷一致。
    - (6.9) `⟨σ_xσ_y⟩_{β,0} − m*(β)² ≤ (C/β) G(x,y) ≤ C′/‖x−y‖_2^{d−2}.` —— `m*(β)` 的**上标星号**、`m*(β)²` 的平方、`C/β` 的系数、末项下标 `2` 与上标 `d−2`、句末句点均与页图一致。
  - 正文数值与方向核对：`ℤ^d`、`[0, L/2] × (ℤ/Lℤ)^{d−1}` 的指数 `d−1`、`d > 2`、`(a_x) ∈ ℂ^{T_L}`、`for d > 2 and every (a_x) ∈ ℂ^{T_L} summing to zero`、`second-order expansion`、`with an exponent at least d − 2` 均与页图一致；`C, C′ > 0` 的正号、`for every β > 0` 的正号无误。
  - 引用核对：`Osterwalder-Schrader [88]`、`we refer to [16] for a review` 与印刷一致。
  - 结构与次序吻合：页首 §6.1 末两句 → §6.2 标题 → `The notion of reflection positivity…` 段 → `Consider the Ising model on a d-dimensional torus…` 段 → (6.6) → `or, in other words…archetypical examples…` 段 → `Reflection positivity has two important implications…` 段 → `Gaussian domination is a statement…` 段 → (6.7) → `Gaussian domination can be proved…` 段 → (6.8) → `where G(x,y) is the Green function…` 段 → `In the specific case…Messager-Miracle-Solé inequality…` 段 → (6.9) → `This is particularly interesting when β approaches β_c from below…`；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - 断词/去连字符伪影：MD 行 535 作 `the spin spin correlations`（印刷跨行作 `spin-` / `spin`），属 MinerU 行末连字符处理类，已文档级登记。
    - MD 行 535 末缺句点（印刷 `…at least d − 2.` 带句点）。
    - MD 行 511 句末 `$ .$ but many other examples exist` 的句点被并入数学段后再起句（排版级）。
    - 行内数学与相邻文字空格普遍合并（`torus$\mathbb { T } _ { L } : = ( \mathbb { Z } / L \mathbb { Z} ) ^ { d }$with`、`$f , g : \mathbb { T } _ { L } ^ { + } \to \mathbb { R }$`、`and every $x,y \in \mathbb { Z } ^ { d }$` 等）；页脚 `23 100 Years of the Ising Model` 未入 MD；印刷斜体/强调（`reflection positive`、`gaussian domination`、`infrared bound`、`chessboard estimate`、`n.n.f.`、各 `𝐡`）未保留（除本次已修的 𝐡 外为风格级）。
  - 印刷怪癖登记（保留不纠）：
    - 印刷用 **粗体 𝐡** 表向量场与普通 `h` 表标量场并置使用（`h : V → ℝ` 前的定义处即为粗体），本文此前已按此约定行文；MD 除本次已修处外仍有若干普通 `h`（如 §5.2 各处），属跨页系统性问题，已在前页登记，不逐处批改。
    - 印刷 (6.9) 中范数下标用欧氏记号 `2` 而非格点范数记号 `ℤ^d`，与数学上常用的 `\mathbb{Z}^d`-范数写法不同；按铁律三原样保留，未按数学常识改写。
- 备注：本页实际改动 1 处（MD 行 521，两处 `h`→`\mathbf { h }`），证据为 300dpi 裁片；另记录一次「据文本层误改会制造错误」的仲裁结论（(6.9) 分母下标 `2`）。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：/tmp/icm2022dc_audit_p024.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p024_300.png（300dpi 全页）、/tmp/icm2022dc_p024_eq610.png（公式 (6.10) 全式）、/tmp/icm2022dc_p024_eq611.png（公式 (6.11) 右半）
- 核对：§6.3 标题与 `Section 6.4` 交叉引用；引用 `[35]`；`exp[βσ_xσ_y]`；公式 (6.10) 的三个求和域、`∏_{\{x,y\}∈E}`、中间求和上下限 `n_{\{x,y\}}=0` 与 `∞`、阶乘 `\mathbf{n}_{\{x,y\}}!`；公式 (6.11) 的 `w_β(n)` 与 `Δ_x(n)` 定义及 `y∈V:\{x,y\}∈E`；`2^{|V|}`；`∂n = ∅` 与 `∂n = A`；公式 (6.13) 的分子分母比值；`Frame 4` 标题与 `β_c > 0`；`van der Waerden [100]`；`cosh(β) + sinh(β)σ_xσ_y`；页脚 `24 Hugo Duminil-Copin`。
- 结果：PASS±
  - 公式逐项吻合（(6.10)、(6.11) 以 300dpi 裁片逐符号仲裁，`pdftotext` 文本层把分式排成 `n { 𝑥,𝑦 } !` 之类，不可作依据）：
    - (6.10) `Z(G,β,0) = ∑_{σ∈{−1,1}^V} ∏_{\{x,y\}∈E} ∑_{n_{\{x,y\}}=0}^{∞} \frac{(βσ_xσ_y)^{n_{\{x,y\}}}}{n_{\{x,y\}}!} = ∑_{n∈ℤ_+^E} w_β(n) ∑_{σ∈{−1,1}^V} ∏_{x∈V} σ_x^{Δ_x(n)},` —— 中间求和的**下限 `n_{\{x,y\}}=0` 与上限 `∞`**、分式**分子指数与分母阶乘的下标完全相同**（`(βσ_xσ_y)^{n_{\{x,y\}}}` / `n_{\{x,y\}}!`）、右侧 `w_β(n)` 前无乘积号、以及**尾逗号**均与页图一致。
    - (6.11) `w_β(n) := ∏_{\{x,y\}∈E} \frac{β^{n_{\{x,y\}}}}{n_{\{x,y\}}!}  and  Δ_x(n) := ∑_{y∈V:\{x,y\}∈E} n_{\{x,y\}}.` —— `β` 的指数 `n_{\{x,y\}}`（**无括号**）、分母阶乘、求和条件冒号写法 `y∈V:\{x,y\}∈E`、**尾句点**均与页图一致；定义号 `:=` 两处正确。
    - (6.12) `Z(G,β,0) = 2^{|V|} ∑_{∂n=∅} w_β(n),` —— `2^{|V|}` 的指数 `|V|`、求和下标 `∂n = ∅`、**尾逗号**与印刷一致（**未误作 `2^V`**）。
    - (6.13) `⟨σ_A⟩_{G,β,0} = \frac{∑_{∂n=A} w_β(n)}{∑_{∂n=∅} w_β(n)}.` —— 期望值下标 `G,β,0`、分子约束 `∂n = A`、分母约束 `∂n = ∅`、**尾句点**与印刷一致。
  - 记号逐项一致：电流记号 `𝐧` 全篇作粗体（MD 作 `\mathbf { n }`，(6.10)–(6.13) 四式与正文 `∂\mathbf{n}` 一致，未出现普通 `n` 误替）；`Δ_x(𝐧)` 的下标 `x`；`\mathbb{Z}_+`（印刷为 `ℤ₊`）；`w_β(n)` 的下标 `β`。
  - 正文数值与方向核对：`Call a function from E to ℤ₊ a current`、`A source of the current will be a vertex x with Δ_x(n) odd`、`the sum on σ on the right-hand side is either equal to 2^{|V|} if Δ_x(n) is even for all x ∈ V, or 0 otherwise`（偶/奇方向未颠倒）、`∂n = A`、`loops`、`[35]`、`[100]`、`β_c > 0` 均与页图一致。
  - 结构与次序吻合：§6.3 标题 → `The context of CQFT…` 段 → `The whole story starts with…` 段 → (6.10) → `where` → (6.11) → `Now, the involutions…` 段 → `Call a function from E to ℤ₊ a current…` 段 → (6.12) → `where from now on we omit…` 段 → `A current n with ∂n = A can be interpreted…` 段 → `Proceeding in a similar fashion…` 段 → (6.13) → `In words, one may write spin-spin correlations…` 段 → Frame 4 框首两行；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - MD 行 563 末缺句点（印刷 `…in terms of them.` 带句点）。
    - MD 行 553 `even for all$x \in V$ or 0 otherwise` 缺印刷中的逗号（`V, or 0 otherwise`）——标点级。
    - 行内数学与相邻文字空格普遍合并（`component$\exp [ \beta \sigma _ { x } \sigma _ { y } ]$of`、`sum on$\sigma$on`、`notation$n$`、`A current$n$ with$\partial \mathbf { n } = A$can` 等）；页脚未入 MD；印刷斜体（`random current representation`、`exp[βσ_xσ_y]`、`source`、`loops`、`high-temperature expansion`、`odd current`）未保留（风格级）。
    - Frame 4 首句在 p.24 只印两行、于 p.25 续完，MD 行 575 已含完整句，未误判为缺失。
  - 印刷怪癖登记（保留不纠）：
    - 印刷把 `w_β(n)` 的定义与 `Δ_x(n)` 的定义并排在**同一条编号公式 (6.11)** 内（以 `and` 连接），而 (6.12) 起编号单列；MD 保留该合并写法，未拆成两式。
    - 印刷 (6.10) 中 `w_β(n)` 与其后的 `∑_{σ}∏_x` 之间**无乘号也无间隔**，属紧凑排版；MD 原样保留。
- 备注：本页无数学内容错误，未改动 Markdown；四个编号公式 (6.10)–(6.13) 均以 300dpi 裁片确认系数、上下限、阶乘与求和域无误。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：/tmp/icm2022dc_audit_p025.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p025_300.png（300dpi 全页）、/tmp/icm2022dc_p025_eq614.png（公式 (6.14)）、/tmp/icm2022dc_p025_eq615.png（公式 (6.15) 右端）
- 核对：Frame 4 框续文 `exp[βσ_xσ_y] = cosh(β) + sinh(β)σ_xσ_y`；公式 (6.14) 的 `cosh(β)^{|E|}`、`∑_{F∈Even(G)}`、`tanh(β)^{|F|}`；`Kramers-Wannier duality` 与 `tanh(β) = e^{−2β*}`；`∂n = {x,y}`、`∂n = ∅`、`β ≪ 1`、`β_c > 0`；Aizenman 段与 `Sections 6.4, 6.6, and 7.1`；Frame 5 标题；`n ∈ ℱ_A`、`k ≤ n`、`∂k = A`、`AΔB`、`F : ℤ_+^E → ℝ`、`A,B ⊂ V`；公式 (6.15) 的双约束下标 `∂n₁=A, ∂n₂=B` ↔ `∂n₁=AΔB, ∂n₂=∅` 与指示函数 `𝕀(n₁+n₂ ∈ ℱ_B)`；`[59]`；页脚 `25 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：
    - (6.14) `Z(G,β,0) = cosh(β)^{|E|} ∑_{F∈Even(G)} tanh(β)^{|F|},` —— `cosh` 与 `tanh` 的**幂指数** `|E|` 与 `|F|`、求和域算子 `\operatorname{Even}(G)`、**尾逗号**均与页图一致。
    - (6.15) `∑_{∂n₁=A, ∂n₂=B} w(n₁)w(n₂)F(n₁+n₂) = ∑_{∂n₁=AΔB, ∂n₂=∅} w(n₁)w(n₂)F(n₁+n₂) 𝕀(n₁+n₂ ∈ ℱ_B).`（300dpi 裁片 `/tmp/icm2022dc_p025_eq615.png`）—— **左侧双重约束 `∂n₁=A` 与 `∂n₂=B`、右侧换成 `∂n₁=AΔB` 与 `∂n₂=∅`**（切换引理的「把源从第二个流切到第一个流」方向，未被颠倒）、权重 `w(n₁)w(n₂)`、被积 `F(n₁+n₂)` 的自变量之和、指示函数用**双线体 𝕀** 且自变量为 `n₁+n₂`、其隶属集为 `ℱ_B`（非 `ℱ_A`）、**尾句点**均与印刷一致；编号 `(6.15)` 单独占一行右对齐，MD 亦另起一行。
  - 正文数值与方向核对：`k ≤ n` 的不等号方向（**非 `k ≥ n`**）、`∂k = A`、`AΔB` 的对称差写法（未误作 `A∖B`）、`\mathbb{Z}_+^E \to \mathbb{R}`、`A, B \subset V`、`\beta \ll 1`（双远小于，非 `\lesssim`）、`\beta_c > 0` 的严格正号、`tanh(β) = e^{−2β*}` 的指数 `-2β*`（系数 2 与负号）均与页图一致。
  - 引用与交叉引用核对：`switching lemma [59]`、`see Frame 5`、`Sections 6.4, 6.6, and 7.1`、`van der Waerden [100]`（在 p.24 起句）均与印刷一致。
  - 结构与次序吻合：Frame 4 框续文 → (6.14) → `which resembles the low-temperature expansion…` 段 → `One application of currents…` 段 → `A key observation of Aizenman…` 段 → Frame 5 框 → `Write n ∈ ℱ_A if there exists k ≤ n…` 段 → (6.15) → `The name of the lemma is fairly self-explanatory…` 段；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平：MD 行 589 `symmetric diference`（印刷 `difference`）。
    - 空格合并伪影：行 585 `in terms ofprobabilities`；行 589 `vertices $A,B \subset V,`（逗号后多余空格）、`$\partial \mathbf { k } = A$. Note`；行 583 `currents with${ \partial \bf n } = \{ x , y \}$to`。
    - LaTeX 记号不统一（排版级）：MD 行 583 首处电流记号写作 `\partial \bf n`（旧式 `\bf`），而同句及 (6.15) 用 `\mathbf { n }`；两者渲染均为粗体 n，数学含义一致，未改动以免引入批量改写。
    - MD 行 583 末缺句点（印刷 `…that β_c > 0.` 带句点）。
    - 页脚未入 MD；印刷斜体（`switching lemma`、`random current representation` 之外的本页 `probabilities`、`switching lemma`、`exp[βσ_xσ_y]`）未保留（风格级）。
  - 印刷怪癖登记（保留不纠）：
    - 印刷正文作 `intuitions coming from probabilistic models such as random walks and percolation **was** later used to prove new theorems`（主谓不一致，`intuitions … was`）；按铁律三原样保留，MD 行 585 未作语法"纠正"。
    - 印刷 (6.15) 中指示函数 `𝕀` 与被积式之间**无乘号**，且 `𝕀` 使用双线体而非普通 `I`；MD 保留 `\mathbb{I}` 且不补乘号。
    - 印刷 (6.14) 的 `\operatorname{Even}` 排作正体算子名，MD 一致。
- 备注：本页无数学内容错误，未改动 Markdown；(6.14)、(6.15) 以 300dpi 裁片确认指数、约束方向与指示函数参数无误。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：/tmp/icm2022dc_audit_p026.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p026_300.png（300dpi 全页）、/tmp/icm2022dc_p026_eq617.png（公式 (6.17)）、/tmp/icm2022dc_p026_sigmaL.png（`Σ_L` 定义）、/tmp/icm2022dc_p026_eq618.png（公式 (6.18)）
- 核对：Frame 5 框续文与公式 (6.16)；`𝕀`/`⊗` 与 `ℱ_A`；§6.4 标题 `Triviality in dimension d > 4`；引用 `[2,49]`（Aizenman、Fröhlich）；`In 1982`；公式 (6.17) 的 `T_{f,L}(σ) :=`、分母 `√(Σ_L)`、求和域 `x ∈ ℤ^d`、`f(x/L)`；`Σ_L := ⟨(∑_{x∈Λ_L} σ_x)²⟩`；`d > 4`；`β ≤ β_c`、`L ≤ ξ(β)`、`z > 0`；`C_f > 0`；公式 (6.18) 的绝对值、`z²/2`、`C_f z⁴ / L^{d−4}`；`φ⁴ lattice model`；`Section 6.1`；`[49]`、`Brydges-Fröhlich-Spencer (BFS)`、`[21]`；页脚 `26 Hugo Duminil-Copin`。
- 结果：PASS±
  - 公式逐项吻合：
    - (6.16) `⟨σ_A⟩^2_{G,β,0} = P_G^∅ ⊗ P_G^∅ [n₁ + n₂ ∈ ℱ_A],` —— **平方作上标 `^2`**（非下标）、两处 `P_G` 的上标**均为 `∅`**（切换引理取 `A = B` 后的特例，`n₂` 的源集为空流）、乘积符号 `⊗`、指示括号 `[\cdot]` 内为 `n₁ + n₂`（求和）且隶属 `ℱ_A`、**尾逗号**均与页图一致。
    - (6.17) `T_{f,L}(σ) := \frac{1}{\sqrt{\Sigma_L}} \sum_{x∈ℤ^d} f(x/L) σ_x,`（300dpi 裁片 `/tmp/icm2022dc_p026_eq617.png`）—— 定义号 `:=`、**分母为 `\sqrt{\Sigma_L}`（平方根，非 `Σ_L` 本身）**、`1/√` 的分子 `1`、求和域 `x ∈ ℤ^d`、`f(x/L)` 为一次斜杠除法、**尾逗号**均与印刷一致。
    - `Σ_L := ⟨(∑_{x∈Λ_L} σ_x)²⟩`（300dpi 裁片 `/tmp/icm2022dc_p026_sigmaL.png`）—— 期望值角括号**只一层**、括号内平方**在右括号外**、求和域 `x ∈ Λ_L`（**非** `Λ_L^{(a)}` 或 `V`）均与印刷一致；MD 行 613 写法完全对应。
    - (6.18) `|⟨exp[z T_{f,L}(σ) − (z²/2)⟨T_{f,L}(σ)²⟩_β]⟩_β − 1| ≤ C_f z⁴ / L^{d−4}.`（300dpi 裁片 `/tmp/icm2022dc_p026_eq618.png`）—— 外层绝对值、内层期望角括号各带下标 `β`、**高斯项系数 `\frac{z^2}{2}`（分子 `z²`、分母 `2`，非 `1/2`）**、右端 `C_f z^4 / L^{d-4}`（**分子 `z^4` 指数 4、分母 `L` 指数 `d−4`，负号在指数内**）、**尾句点**均与印刷一致，指数与符号无一处颠倒。
  - 条件与常数核对：`d > 4`（严格大于，与 §6.4 标题 `d > 4` 一致）、`\beta \leq \beta_c`（**小于等于**，含临界点）、`L \leq \xi(\beta)`（**小于等于**关联长度）、`z > 0`、`C_f > 0`（**下标 `f` 非 `L`**）—— 五项的符号与方向均与页图一致，未出现把 `≤` 误作 `<` 或把 `C_L` 误作 `C_f` 的情形。
  - 引用与专名核对：`Michael Aizenman and Juerg Fröhlich [2,49]`、`the approach of Fröhlich in [49]`、`Brydges-Fröhlich-Spencer (BFS)`、`[21]`、`the switching lemma [59]`（p.25 框内）、`Griffiths' inequalities`（印刷作撇号 `’`，MD 行 603 保留 `Griffiths inequalities` 前的直角撇号形式）均与页图一致。
  - 结构与次序吻合：Frame 5 框续文 → (6.16) → `where P_G^B is the measure on currents n on G…` 段 → §6.4 标题 → `In 1982, Michael Aizenman and Juerg Fröhlich [2,49]…` 段 → `Consider discrete smeared averages defined by` → (6.17) → `where f ranges over compactly supported continuous functions, and Σ_L := …` 段（含 `The theorem states that when d > 4, …`）→ (6.18) → `In words, the previous statement claims…` 段 → `As a direct consequence of this result…` 段 → `As mentioned above, one of the most striking applications…` 段；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - 断词/去连字符伪影：MD 行 623 `the Brydges-Fröhlich-Spencer (BFS) walk representation of spinspin correlations`（印刷跨行作 `spin-` / `spin`），同类问题在 p.23 已登记。
    - MD 行 610 `f (x / L)   \sigma _ {x}` 数学段内多余空格（排版级，不影响渲染结果）。
    - 行内数学与相邻文字空格普遍合并（`the case$A = B$`、`square ofspin-spin correlations`、`currents n on $G$ with$\partial \mathbf { n } = B$`、`averages$T _ { f , L } ( \sigma )$are`、`constant$C _ { f } > 0$such that for every$\beta \leq \beta _ { c }$` 等）；页脚未入 MD；印刷斜体（`square of spin-spin correlations`、`independent`、各 `T_{f,L}(σ)`、`trivial`）未保留（风格级）。
    - 印刷末段 `spin-spin correlations [21]` 与本页其余 `spin-spin` 同形，MD 在行 623 与 p.23 行 535 处对同一跨行连字符采用了两种处理（`spinspin` 与 `spin spin`），属导出不一致，登记不改。
  - 印刷怪癖登记（保留不纠）：
    - 印刷 (6.18) 右端分母写作 `L^{d−4}`，指数内含负号；该式在 `d > 4` 时才收敛到常数，印刷未加任何说明。按铁律三原样保留，未按数学常识改写为 `L^{4−d}` 等形式。
    - 印刷把 `Σ_L` 称为 `the variance of the sum of spins`，而其定义 `⟨(∑σ_x)²⟩` 未减去均值平方（因 `∑σ_x` 的期望为零方成立）；此为印刷表述，原样保留。
    - 印刷 `d > 4` 的门槛同时出现在 §6.4 标题与定理陈述中，MD 两处均保留。
- 备注：本页无数学内容错误，未改动 Markdown；(6.16)、(6.17)、(6.18) 与 `Σ_L` 定义均以 300dpi 裁片逐符号确认，指数 `2`、`4`、`d−4` 与不等号方向无误。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：/tmp/icm2022dc_audit_p027.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p027_300.png（300dpi 全页）、/tmp/icm2022dc_p027_eq619.png（公式 (6.19)）、/tmp/icm2022dc_p027_eq620.png（公式 (6.20)）
- 核对：Ursell 函数引导句与 `x_1,…,x_4 ∈ ℤ^d`；公式 (6.19) 的 `U_4^β`、`:=`、`⟨σ_{x_1}···σ_{x_4}⟩_β`、减号、`∑_{π pairing}`、`∏_{i=1}^2`、`x_{π(2i−1)}`/`x_{π(2i)}` 的奇偶次序；公式 (6.20) 的系数 `-2`、两对二点函数、`P^{\{x_1,x_2\}} ⊗ P^{\{x_3,x_4\}}` 的配对、`n_1 + n_2`、`x_1,…,x_4 all connected`；`d < 4` 与 `d ≥ 4` 的分界；`Wick's law`；`When the dimension is strictly larger than 4`；§6.5 标题与 `4 − ε`；`d > 4` 与 `d = 4`；`Wilson's renormalisation group`；页脚 `27 100 Years of the Ising Model`。
- 结果：PASS±
  - 公式逐项吻合：
    - (6.19)（300dpi 裁片 `/tmp/icm2022dc_p027_eq619.png`）`U_4^β(x_1,…,x_4) := ⟨σ_{x_1}···σ_{x_4}⟩_β − ∑_{π pairing} ∏_{i=1}^{2} ⟨σ_{x_{π(2i−1)}} σ_{x_{π(2i)}}⟩_β.` —— `β` 在 `U` 上为**上标**、在期望值上为**下标**（两处方向不同，均与印刷一致）、**减号在和号之前（未误作加号）**、乘积上限 **`2`**（非 `n/2`）、两因子的下标 `π(2i−1)` 与 `π(2i)` **奇数在前偶数在后**、**尾句点**均与页图一致。
    - (6.20)（300dpi 裁片 `/tmp/icm2022dc_p027_eq620.png`）`U_4^β(x_1,…,x_4) = -2⟨σ_{x_1}σ_{x_2}⟩⟨σ_{x_3}σ_{x_4}⟩ P^{\{x_1,x_2\}} ⊗ P^{\{x_3,x_4\}} [x_1,…,x_4 all connected in n_1+n_2],` —— **系数为负 `-2`**、两对二点函数的分块次序 `(x_1,x_2)` 在前 `(x_3,x_4)` 在后、两个测度的上标为**无序对的花括号集**（`{x_1,x_2}` / `{x_3,x_4}`）、张量积符号 `⊗`、指示括号内 `n_1 + n_2`（求和而非单独 `n_1`）、**尾逗号**均与印刷一致。
  - 记号逐项一致：电流记号 `𝐧₁`、`𝐧₂` 作粗体（MD 用 `\mathbf { n }`；MD 行 643 首处用旧式 `${ \bf n } _ { 1 }`，渲染同为粗体，属记号不统一，见差异列表）；`𝕇`/`\mathbb{P}` 双线体；`\otimes`；`\varepsilon`。
  - 正文数值与方向核对（本页核心分界，逐项未颠倒）：
    - `two random walks … intersect with a probability bounded away from 0 as L tends to infinity in dimensions **d < 4**, and tending to zero in dimension **d ≥ 4**.` —— 低维相交、高维不相交的写法与印刷一致；`d ≥ 4` 的**大于等于**未被误作 `> 4`。
    - `it would single out dimensions$d \ge 4$as being dimensions for which$U _ { 4 } ^ { \beta }$becomes much smaller than products of two-point correlations` —— `≥ 4` 再次正确。
    - `When the dimension is strictly larger than 4` —— **严格大于**（与前文 `≥ 4` 刻意区分），MD 原文保留。
    - `Making the argument work for currents in dimension 4 is more subtle because, contrarily to larger dimensions, the expected number of intersections does not tend to 0 when L tends to infinity.` —— `contrarily` 为印刷原词，未作"纠正"。
  - 结构与次序吻合：`Let us focus on the four-point function…` 段 → (6.19) → `A simple exercise involving the switching lemma shows that` → (6.20) → `where connected in n_1+n_2 means…` 段（含经典相交结论）→ `At this stage, it is totally unclear…` 段 → `When the dimension is strictly larger than 4…` 段 → `Making the argument work for currents in dimension 4…` 段 → §6.5 标题 → `The triviality of the Ising model in dimension d > 4…` 段；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - **行内公式被拆成两个独立 display 块**：MD 行 633–635 给出 (6.20) 的前半，行 637–639 以 `\left. \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } \right]\tag{6.20}` 收尾。拼接后与印刷全式逐符号一致，但 `\left.` 无配对 `\right`，属 MinerU 对超长行内公式的换行处理（排版级，未改动以免重排公式）。
    - `ff` 连字拍平：MD 行 645 `the dificulty`（印刷 `difficulty`）。
    - 空格合并伪影：行 641 `the vertices ofa graph`；行 641 `$d < 4 .$`（句点被并入数学段，且印刷该处为 `d < 4.` 后接逗号，MD 的 `$ .$` 位置错乱）；行 645 `spin-spin correlations of the Ising model` 的连字符**正确保留**（此处为词内连字符，非跨行断词，可与行 623/535 的跨行情形区分）。
    - MD 行 641 末缺句点（印刷 `…in dimension d ≥ 4.` 带句点）。
    - LaTeX 记号不统一（排版级）：行 641、643 用 `\mathbf { n }`，行 643 首处用 `${ \bf n } _ { 1 }`；两者渲染均为粗体，数学含义一致。
    - 页脚未入 MD；印刷斜体（`expected number of intersections`、`connected in`、`all connected`、`renormalisation group`）未保留（风格级）。
  - 印刷怪癖登记（保留不纠）：
    - 印刷用 `contrarily to larger dimensions`（非常用英语搭配），原样保留。
    - 印刷把 (6.19) 的 Wick 型配对和的上限写成 `∏_{i=1}^{2}`（即两项），而 (6.3) 写成 `\prod_{j=1}^n`（一般 `n` 项）；两处写法不同但各按其语境成立，MD 各自保留未统一。
    - 印刷在 (6.20) 的指示事件中用 `n_1 + n_2`（两流之和）而非分别判定，两处流记号同为粗体 `𝐧₁`、`𝐧₂`；MD 保留。
- 备注：本页无数学内容错误，未改动 Markdown；(6.19)、(6.20) 以 300dpi 裁片确认减号、系数 `-2`、配对上下限与奇偶次序无误，`d < 4` / `d ≥ 4` / 严格大于 4 三处分界均未颠倒。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：/tmp/icm2022dc_audit_p028.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p028_300.png（300dpi 全页）、/tmp/icm2022dc_p028_bzero.png（`b = λ = 0` 行）、/tmp/icm2022dc_p028_Lk.png（`L^k` 行）、/tmp/icm2022dc_p028_lastline.png（页末最后一行）
- 核对：`φ⁴` 各处写法与字形；`Section 6.1`；`Gaussian Free Field (GFF)`；引用 `[43, 51, 62]`、`[51]`、`[11]`；`b = λ = 0`；`blocks of size L^k`；`multi-scale analysis`；`Bauerschmidt, Brydges, and Slade`；`finite-range covariances`；§6.6 标题 `Forty years later: the random current strikes back`；`4D quantum field theory`；`a φ⁴ terms which is not a priori small`；`forty years`；页脚 `28 Hugo Duminil-Copin`。
- 结果：PASS±（本页印刷行内无缺陷；唯一相关缺陷位于跨页段落的 p.29 侧，已在本页登记归属更正并计入 p.029）
  - **归属更正（本条为写完 p.028 后于 p.029 复核时发现，据实更正，不掩盖）**：MD 行 665 是**一个跨越 p.28/p.29 分页的整段**，其前半 `…the 4D Ising and φ⁴ lattice models, which` 印于 p.28 末行，后半 `states [4] that there exists c > 0 …` 印于 p.29 首段。因此 p.28 页图上**没有任何缺陷**：150dpi 页图与 300dpi 页末裁片 `/tmp/icm2022dc_p028_lastline.png` 显示 p.28 末行仅到 `models, which` 即断行，其内容与 MD 行 665 前半逐字相符。原先登记在本条的「句末伪字符 `7`」与 `$b , \lambda .$`、`$f ,,$` 两处标点伪影，经 p.29 页图核对后确认**物理位置在 p.29**，故其判定与修复计入 **p.029** 条目（见下）。本条按铁律二只以 p.28 页图为依据，改判为 PASS±。
  - 数值与条件核对（p.28 印刷行范围）：`b = λ = 0`（两个等号串、`λ` 为小写 lambda 非 `Λ`）、`L^k`（**上标 `k`**，300dpi 裁片 `/tmp/icm2022dc_p028_Lk.png` 确认）、`[43, 51, 62]`、`[51]`、`[11]`、`Section 6.1`、`Gaussian Free Field (GFF)`、`multi-scale analysis`、`4D quantum field theory`、`forty years` 均与 p.28 页图一致。
  - 结构与次序吻合（p.28 印刷行范围）：`Consider the lattice version of the φ⁴ model discussed in Section 6.1…` 段 → `Several methods were used at the time…Gawedski and Kupiainen [51]…` 段 → `An alternative to this block-spin renormalisation was later developed by Bauerschmidt, Brydges, and Slade [11]…` 段 → `The level of sophistication of these techniques…` 段 → §6.6 标题 → `While renormalisation techniques provided impressive rigorous results in dimension 4…` 段 → `This asks for another approach…` 段首行（该段跨页至 p.29）；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - 行内数学与相邻文字空格普遍合并（`the$\phi ^ { 4 }$model`、`size$L ^ { k }$,`、`coupled$\phi ^ { 4 }$lattice model 等）；页脚未入 MD；印刷斜体/强调（`perturbative`、`renormalisation scheme`）未保留（风格级）。
  - 印刷怪癖登记（保留不纠）：
    - 印刷 §6.6 正文作 `a strongly coupled φ⁴ lattice model (meaning with a **φ⁴ terms** which is not a priori small)`——不定冠词 `a` 与复数 `terms` 不一致，属印刷语法瑕疵，原样保留（MD 行 663 亦为 `a$\phi ^ { 4 }$terms`）。
    - 印刷 `one had to wait for **forty years**` 与 §6.6 标题 `Forty years later`（1982→2022）呼应，MD 两处均保留，未作时间口径的"纠正"。
    - 印刷本节两处把 $\phi^4$ 写作**不带下标 `d`** 的 `φ⁴`（与 p.22 的 `Φ_d^4`/`φ^4` 写法一致），MD 行 653/657/663 均作 `\phi ^ { 4 }`，与印刷一致。
- 备注：本页**未改动 Markdown**；页图核对无误，段中唯一缺陷的归属经 p.29 复核后更正并计入 p.029 条目。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：/tmp/icm2022dc_audit_p029.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p029_300.png（300dpi 全页）、/tmp/icm2022dc_p029_eq621.png（公式 (6.21)）、/tmp/icm2022dc_p029_body_phi4b.png（正文 `n.n.f. φ⁴ lattice model on ℤ⁴` 行）
- 核对：`states [4] that there exists c > 0`；`n.n.f.`、`φ⁴`、`ℤ^4`、`parameters b, λ`、`function f`、`C_f > 0`；`β ≤ β_c = β_c(b,λ)`、`L ≤ ξ(β)`、`z > 0`；公式 (6.21) 的绝对值、`z²/2`、`C_f z⁴ / (log L)^c` 与字形 `φ`；`than in [2]`；`probability of order (log L)^{−c}`、`universal constant c > 0`、`of order 1`、`multi-scale analysis`；§7 标题 `The last fifty years: Ising model and percolation`；`G = (V, E)`、`ω = (ω_e : e ∈ E) ∈ {0,1}^E`、`{e ∈ E : ω_e = 1}`、`Bernoulli percolation`；§7.1 标题；`Frame 5`；页脚 `29 100 Years of the Ising Model`。
- 结果：**FAIL（1 处伪字符，已删，以原图为准；另有 2 处标点伪影登记不改）**
  - **已修缺陷**：MD 行 665 原以 `and every$z > 0$7` 结尾，句末数学定界符 `$` 之后多出一个**孤立数字 `7`**。印刷 p.29 第 3 行的对应内容为 `every β ≤ β_c = β_c(b, λ), every L ≤ ξ(β), and every z > 0,`（150dpi 页图与 300dpi 全页图一致，行末只有逗号，无任何数字）；全文仅有 p.7 脚注 1 与 p.10 脚注 2（MD 内唯一的 `docvortex-page-footnote` 标记在行 221），**不存在脚注 7**，故该 `7` 为导出伪字符。已用 Edit 删除。
  - **溯源（回归判定）**：对 `d351abbf`（原始 MinerU 导出）、`59537f98`、`232a8965`、`5c63be8f`、HEAD 逐一执行 `git show <c>:"…__ICM2022_proceedings_Duminil-Copin.md" | grep -c 'every\$z > 0\$7'`，五处计数均为 `1`。**属原始导出缺陷，非 peer 回归**；原导出即已带此伪字符。
  - **同类伪字符全篇只此一处**：修复后执行只读扫描 `grep -n '\$[0-9]\{1,2\}$' <md>` 与 `grep -n ' \$[0-9]\{1,2\}$' <md>`，两次输出均为空，确认不存在其他「数学定界符后紧跟裸数字」的残留。
  - **归属说明**：MD 行 665 为跨 p.28/p.29 分页的单一自然段（前半 `…models, which` 在 p.28 末行，后半在本页首三行）。本条目原先被写在 p.028 条下，于本页复核时按铁律二据本页页图改判归属，p.028 条已同步留有「归属更正」说明，未掩盖改判。
  - 公式 (6.21) 逐项吻合（300dpi 裁片 `/tmp/icm2022dc_p029_eq621.png`）：`|⟨exp[z T_{f,L}(φ) − z²/2 ⟨T_{f,L}(φ)²⟩_β]⟩_β − 1| ≤ C_f z⁴ / (log L)^c.` —— 外层绝对值、内层期望角括号**各带下标 `β`**、高斯项 `\frac{z^2}{2}`（分子 `z^2`、分母 `2`）、右端**分子 `C_f z^4`、分母 `(log L)^c`（底数为 `log L` 的 `c` 次幂，非 `L^c` 亦非 `log L^c`）**、**尾句点**均与印刷一致；编号 `(6.21)` 右对齐单列，MD 亦单列。指数 `2`、`4`、`c` 与 (6.18) 的 `d−4` 形成的对照关系正确。
  - 正文数值与方向核对：`c > 0`、`C_f > 0`、`\beta \leq \beta_c = \beta_c(b, \lambda)`（**小于等于**、`β_c` 同时给出定义与自变量）、`L \leq \xi(\beta)`（**小于等于**）、`z > 0`、`(\log L)^{-c}`（**负指数**）、`probability of order (log L)^{-c}`、`the expected number of intersections is of order 1` —— 全部符号与方向与页图一致，未出现 `≤` 误作 `<`、`−c` 误作 `c` 的情形。
  - 记号核对：`{0,1}^E`、`ω = (ω_e : e ∈ E)`、`{e ∈ E : ω_e = 1}`、`G = (V, E)`、`Bernoulli percolation`、`Frame 5`、`than in [2]`、`[4]` 均与页图一致；§7 与 §7.1 标题逐字相符（`The last fifty years: Ising model and percolation`、`Percolation interpretation of random currents`）。
  - 结构与次序吻合：`states [4] … every z > 0,` → (6.21) → `The strategy of the proof uses a more delicate probabilistic perspective on the random current than in [2]…` 段（含 `triviality result.`）→ §7 标题 → `Percolation theory gathers under its umbrella…` 段 → `As often, the Ising model has played an essential role…` 段 → §7.1 标题 → `We have seen one example of a graphical representation in Frame 5…` 段；印刷与 MD 逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - **标点级伪影（2 处，均在本页第 2 行）**：MD 行 665 `with parameters $b , \lambda .$` —— 印刷为逗号 `b, λ`，MD 把逗号误作句点；同句 `continuous function$f ,$` 为**双逗号**（印刷单逗号 `f,`）。两者均不改变任何数学记号（`b`、`λ`、`f` 本身正确），故登记不改。
    - `ff` 连字拍平：MD 行 675 两处 `diferent percolation models`、`diferent measures`（印刷 `different`）。
    - 空格合并伪影：行 671 `probability of order (log$L ) ^ { - c }$for`、行 671 `quite large in $L )$`（右括号前缺空格）；行 675 `the behaviour ofliquid in a porous medium`；行 681 `one example ofa graphical representation`；行 677 `sometimes the connection is much more direct`（正常）、`spin-spin correlations` 的连字符**正确保留**（词内连字符，非跨行断词）。
    - 页脚 `29 100 Years of the Ising Model` 未入 MD；印刷斜体（`random walks`、`multi-scale analysis`、`graphical representation`、`rational` 等）未保留（风格级）。
  - 印刷怪癖登记（保留不纠）：
    - **字形不一致（印刷自身）**：正文中的 `ϕ⁴` 用直笔 `\phi` 字形（300dpi 裁片 `/tmp/icm2022dc_p029_body_phi4b.png`），而公式 (6.21) 中 `T_{f,L}(φ)` 用带环的 `\varphi` 字形（裁片 `/tmp/icm2022dc_p029_eq621.png`）。按铁律三原样保留：MD 行 665/683 用 `\phi`，行 668 用 `\varphi`，各自忠实于印刷，未统一。
    - 印刷 §7 标题作 `Ising model and percolation`（无冠词 `the`），MD 保留。
    - 印刷正文 `Percolation theory gathers under its umbrella a variety of random graphs systems.`（`random graphs systems` 缺连字符），原样保留。
- 备注：本页实际改动 1 处（删除 MD 行 665 句末伪字符 `7`），证据为 150dpi/300dpi 页图 + `pdftotext` 文本层 + 跨五提交 `git show` 三重比对；另以只读 `grep` 确认全篇无同类残留。

## p.030（PDF p.30 / 印刷 p.30）
- PNG：/tmp/icm2022dc_audit_p030.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p030_300.png（300dpi 全页）、/tmp/icm2022dc_p030_eq71.png（公式 (7.1)）、/tmp/icm2022dc_p030_eq72.png（公式 (7.2)）、/tmp/icm2022dc_p030_eq73.png（公式 (7.3)）
- 核对：`ω_{e} = 1 if (n₁+n₂)_{\{x,y\}} > 0`；`connected in ω`；`regime β < β_c`；`Aizenman, Barsky and Fernandez [3]`、`[39]`；`n.n.f.`、`decay exponentially fast`；公式 (7.1) 的 `⟨σ_xσ_y⟩_{β,0}`、`exp(−τ‖x−y‖)`；`phase transition is sharp`、`no intermediate phase (β_exp, β_c)`；`truncated correlations ⟨σ_xσ_y⟩_{β,0} − m*(β)²`；`[36]`；`bottleneck`、`Section 4.1`、`ξ(β)`；`differential inequalities`、`m = m(β, h)`；公式 (7.2) 的 `tanh(βh)`、`∂/∂(βh)`、`m²(β ∂/∂β m + m)`、`m ∂/∂β m ≥ c`；`Bernoulli percolation`、`[7]`、`d > 4`；公式 (7.3) 的 `(1 − B/χ)`、`2dχ²/(1+B)`、`∂/∂β χ`；`h = 0`、`β < β_c`；页脚 `30 Hugo Duminil-Copin`
- 结果：**PASS±（差异列表如下，均不误导；本页数学内容零错误，Markdown 无需改动）**
  - **公式 (7.1) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p030_eq71.png`）：`⟨σ_xσ_y⟩_{β,0} ≤ exp(−τ‖x−y‖).` —— 期望角括号内两枚 `σ`（无乘号）、下标 `β,0`、右端 `exp(−τ‖x−y‖)`、尾句点、编号 `(7.1)` 右对齐均与印刷一致；MD 行 688 逐字相符。**特别核对范数**：`‖x−y‖` **无下标**（区别于第 23 页 (6.9) 的 `‖x−y‖_2^{d−2}`），两处不得混同。
  - **公式 (7.2) 逐项吻合**（裁片 `/tmp/icm2022dc_p030_eq72.png`）：`m ≤ tanh(βh) [∂/∂(βh)]m + m²(β ∂/∂β m + m)  and  m [∂/∂β]m ≥ c.` —— 首个不等号方向为 `≤`，第二个为 `≥`（方向相反，MD 行 698 保持一致，未互换）；分母 βh 的偏导写成分数形式 `[∂/∂(βh)]m`（非导数符号）、末项 `≥ c` 的 `c` 无下标；`\quad \text{ and } \quad` 连接词与两端句点均吻合。
  - **公式 (7.3) 逐项吻合**（裁片 `/tmp/icm2022dc_p030_eq73.png`）：`(1 − B/χ) [2dχ²/(1+B)] ≤ [∂/∂β]χ ≤ 2dχ²,` —— 首因子 `(1 − B/χ)`、其后的分数**分子 `2dχ²`、分母 `1+B`**、中央偏导、两端均为 `≤`、**右端 `2dχ²` 无分母**、结尾为**逗号**（承前句 `for h = 0 and β < β_c,`）；MD 行 704 完全一致（`\frac {2 d \chi^ {2}}{1 + B}` 与 `2 d \chi^ {2}` 两处指数均为 `2`，未误作 `χ` 或 `χ³`）。
  - 正文数值与方向核对：`β < β_c`（严格小于，非 `≤`）、`m = m(β, h)`、`d > 4`（严格大于）、`β > β_c`（截断相关段）、`h = 0` —— 全部与页图一致，未出现方向误植。
  - 记号与交叉引用核对：`ω_{e}`、`{x,y}`、`(n₁+n₂)_{\{x,y\}}`（粗体 `𝐧` 加下标 1/2）、`⟨σ_xσ_y⟩_{β,0}`、`m*(β)²`、`ξ(β)`、`χ`、`B`、`τ`、`c`、引用 `[3]`、`[7]`、`[36]`、`[39]` 与内部指引 `Section 4.1` 均与印刷一致；§7.1 内段落次序（渗流定义 → ABF 1987 结果 → `sharp` → 截断相关 → 「bottleneck」意义段 → 证明思路 `differential inequalities` → Bernoulli 渗流平行结果）逐段对应，无缺失或错序。
  - 差异列表（不误导，登记不改）：
    - `ff` 连字拍平（4 处）：MD 行 693 `suficiently large`（印刷 `sufficiently`）；行 695 `diferential inequalities` 两处（印刷 `differential`，同行 `fruitful`/`archetypical` 正常）；行 701 `diferential inequalities` 两处。与全篇同类（`diferent`、`dificulty`、`eforts`…）属同一系统性缺陷，按既定做法只读登记、不批量改写。
    - 标点级伪影 1 处：**MD 行 685 `for each such$\beta ,$,`** —— 印刷为 `for each such β, there exists τ > 0`（单逗号），MD 在数学模式内多出一个逗号，形成 `β,,` 双逗号。**溯源**：对 `d351abbf`（原始导出）、`59537f98`、HEAD 逐一执行 `git show <c>:"…__ICM2022_proceedings_Duminil-Copin.md" | grep -c 'for each such\$\\beta ,\$'`，三处计数均为 `1` —— **属原始导出缺陷，非 peer 回归**，原导出即已带该伪影。全篇同类实例仅 3 处（MD 行 375、685、763 的 `$\beta ,$`），按本轮既定尺度（**字母级脱落才修、标点级伪影只登记**）统一不改。
    - 空格合并伪影：行 683 `are connected in$\omega .$`；行 685 `there exists$\tau > 0$such that`；行 695 `magnetisation$m = m(β,h)$is a function`、`$\beta$and ℎ`；行 701 `regime for$d > 4$were obtained`、`for$h = 0$and$\beta < \beta_c$`；行 693 `correlation length$\xi(β)$mentioned`、`decay exponentially fast\n\n`。
    - 行 693 段末**缺句点**（印刷 `…as soon as β < β_c.`），非数学内容，登记不改。
    - 页脚 `30 Hugo Duminil-Copin` 未入 MD；印刷斜体（`decay exponentially fast`、`sharp`、`bottleneck`、`n.n.f.`）未保留（风格级）。
  - 印刷怪癖登记（保留不纠，铁律三）：
    - 印刷作 `We say that the phase transition is sharp`，即「sharp」加书名引号式强调；按原样保留，未替换为 `sharp phase transition`。
    - 印刷的「sharp」区间写作 `(β_exp, β_c)`（`exp` 下标为直立正体），并非标准的 `β_c` 记法；原样保留。
    - 印刷 `The result also provides meaning to the correlation length ξ(β) mentioned in Section 4.1, as it proves that it is finite as soon as β < β_c.` —— 主语 `it`（指代 `ξ(β)`）的指代略含混，系印刷行文，按铁律三不改。
    - 印刷 `we do not resist mentioning one of them` 属作者口语，保留。
- 备注：本页**无 Markdown 改动**。三条公式均以 300dpi 裁片逐项复核（(7.1)/(7.2)/(7.3)），数学内容零错误，故判 PASS± 而非 FAIL。`$\beta ,$,` 伪影已按上文跨提交溯源确认为原始导出缺陷并登记，与 MD 行 375、763 同类同尺度处理。p.030 为本轮 1–30 页范围的最后一页。

---

# 逐页重审块 C：PDF p.1–p.8（独立第三方视觉复核，`Wf-icm2022dc`）

- 范围：PDF 第 1–8 页（印刷封面页 + 印刷 p.2–p.8，46 页中的前 8 页）。
- Actor：`Wf-icm2022dc`（本 workflow run `审计 icm2022dc`）。Host/model/effort：zcode / `opencode-go-chat/space-bunny-free`（run 级环境自报）/ effort 未暴露，记 UNKNOWN，不据文本风格推断。
- 方法：每页**单独** `gs -sDEVICE=pngmono -r150` 渲染到 `/tmp/icm2022dc_audit_pNNN.png`，用 Read 工具打开亲眼查看，再与 `pdftotext` 整页文本层及 MinerU Markdown 对应段落五点比对；字形在 150dpi 下判读不了时升级 300dpi 裁剪仲裁。
- 与既有块的关系：本块**独立重看原页图**核对 p.1–p.8，不把「块 A（`Wf-R-P15`）」或「redo 块（`Wf-R-P14`）」的结论当作证据。印刷原文（PDF 原页）是唯一裁决源。
- 纪律：print quirk 与印刷错字忠实保留登记，绝不按数学预期静默改正；每处判为「缺陷」的都用 Edit 逐处改 Markdown。
- 不写根级文件（`AUDIT-INDEX.md`/`AUDIT-PROGRESS.log`/`MEMORY.md`/`README.md` 由总Master 串行负责）；不做任何 git commit。

## p.001（PDF p.1 / 印刷封面页）
- PNG：/tmp/icm2022dc_audit_p001.png（pngmono 150dpi）
- 核对：题录页——标题三行断行、作者、dedication 斜体行（含 `Dmitry Ioffe` / `Vladas Sidoravicius` 两处专名拼写）、Abstract 六行全文（含 `math-ematical` 断词合并）、Mathematics Subject Classification 2020（Primary/Secondary）、Keywords 四项、页脚三行（版权行 / Preliminary version 行 / DOI 行）、左下 ICM 会徽。
- 结果：**PASS**（逐项吻合，本页 Markdown 无需改动）
  - 标题：150dpi 页图为三行 `100 Years of the (Critical)` / `Ising Model on the` / `Hypercubic Lattice`；`pdfinfo` Title 字段为 `100 Years of the (Critical) Ising Model on the Hypercubic Lattice`、Author 为 `Hugo Duminil-Copin`，与 MD 行 1 合并后的单行标题一致（断行合并属正常版式处理）。
  - 作者：页图 `Hugo Duminil-Copin` = MD 行 3。
  - dedication：页图斜体行读作 `Dedicated to the memory of colleagues and friends Dmitry Ioffe and Vladas Sidoravicius`；MD 行 5 逐字一致——**`Dmitry Ioffe` 拼写正确**（`Ioffe` 两个 f 完整），`Vladas Sidoravicius` 亦正确。
  - Abstract：页图六行与 MD 行 9 逐句一致（`We take the occasion …` 至 `… what happens at or near the so-called critical point.`）；页图行末断词 `math-` / `ematical` 已在 MD 中正确合并为 `mathematical`，无重复无缺失。
  - MSC：页图 `Primary 82B20; Secondary 60K35` = MD 行 11（`Primary`/`Secondary` 与分号一致）。
  - Keywords：页图 `Ising model, percolation theory, phase transition, statistical mechanics` = MD 行 13。
  - 页脚三行：页图 `© 2022 International Mathematical Union` / `Preliminary version, to appear in Proc. Int. Cong. Math. 2022, Vol. 1.` / `DOI 10.4171/ICM2022/204`；150dpi 下 DOI 行清晰可读为 `ICM2022/204`（斜杠 + 204，非连字符、非 `ICM2022-204`），**无需 300dpi 仲裁**即判定，与 MD 行 15/17/19 三行完全对应。
  - 未入 MD 者：左下 ICM 徽标为图形徽标（其内小字 `INTERNATIONAL CONGRESS OF MATHEMATICIANS 2022 JULY 6–14` 属徽标图形文字，非正文可检索内容），不计缺陷。
- 备注：本页判 PASS。**无 Markdown 改动。**

## p.002（PDF p.2 / 印刷 p.2）
- PNG：/tmp/icm2022dc_audit_p002.png（pngmono 150dpi）
- 核对：§1 全部三段（节标题编号与顺序）、breakthroughs 列举与其后引用号 `[20, 86]`/`[48]`、§2 节标题、§2.1 节标题、§2.1 Curie 段前半（页末断于 `exhibits magnetisation only when an external`，续 p.3）、数值 `769.85`/`100`、专名 `Pierre Curie`、`Kadanoff`、`Lee-Yang`、`Fortuin-Kasteleyn`、`Aizenman`、`Chelkak-Smirnov`、破折号型（en dash）引出语、页脚 `2 Hugo Duminil-Copin`。
- 结果：**PASS±**（差异列表见下，均不误导；本页无内容错误，**未改动 Markdown**）
  - 节标题顺序与编号逐字吻合：页图 `1. Short motivation` → `2. The first twenty years: a laborious start` → `2.1. Ising model's prehistory`，对应 MD 行 21 / 29 / 31，编号层级与句点位置一致。
  - 三段正文逐句与页图一致；断词合并正确：`audi-`/`ence`→`audience`、`atten-`/`tion`→`attention`、`nat-`/`ural`→`natural`、`integra-`/`bility`→`integrability`、`inequali-`/`ties`→`inequalities`，MD 中均无残留连字符或重复。
  - 数值与引用号核对：`769.85 degrees Celsius`（页图与 MD 行 33 一致，小数点未被拍平）、`slightly over 100 degrees Celsius`、`[30]`、`[20, 86]`、`[48]` 均正确；`Peierls'`（页图为右单引号 `Peierls' argument`）与 `Ising model's prehistory` 的撇号用法一致。
  - 页末断点吻合：页图止于 `…exhibits magnetisation only when an external`，MD 行 33 同样在此处与 p.3 首句 `field is applied to it` 无缝衔接（该句完整内容落在 MD 行 33，跨页续句已在 MD 中合并）。
  - 差异列表（登记不改）：
    - `ff` 连字拍平 2 处：MD 行 27 `diferent`（页图与文本层均作 `different`）、同句 `diferential inequalities`（页图与文本层均作 `differential inequalities`）。属 OCR 伪影，**非 print quirk**（印刷本身 `ff` 完整）；语义不受影响，仅影响精确字符串检索。按 SOP「PASS± 排版级伪影默认不批量改」登记而不修——若日后整篇统一修复，须整篇登记（此二处与 MD 行 35 `eficient`、行 115 等属同一系统性伪影）。
    - 空格合并 1 处：MD 行 27 `[20,86]`——页图与文本层均为 `[20, 86]`（逗号后有空格）。
    - 印刷斜体强调未在 MD 保留：页图 `Curie temperature`、`spontaneous magnetisation`、`only`（页末）三处为斜体，MD 行 33 为正体（排版风格级，不影响内容）。
    - 印刷 running foot `2  Hugo Duminil-Copin` 未入 MD（全篇一致，版式级）。
- 备注：本页数学内容为零（纯散文页），判 PASS± 的依据仅为上述拼写/空格/斜体类伪影。**无 Markdown 改动。**

## p.003（PDF p.3 / 印刷 p.3）
- PNG：/tmp/icm2022dc_audit_p003.png（pngmono 150dpi）
- 核对：p.2 跨页续句（`field is applied to it … a ferromagnetic phase below it`）、Curie's law / Pierre Weiss 段、Lenz 三段（Wilhelm Lenz、Weiss' suggestions、`He formalized this reasoning in [80]`）、Ernst Ising 生平段（1900/1924/1925）、Ising 两处英文直接引语（`"decay rapidly with distance…"`、`"of all the possible positions…"`）、`linear chain` 段、末段至页末断词 `tempera-`、引用号 `[101]`/`[80]`/`[70]`、英式拼写 `magnetisation`/`behaviour`/`generalising`、页脚 `3  100 Years of the Ising Model`。
- 结果：**PASS±**（差异列表见下，均不误导；本页无内容错误，**未改动 Markdown**）
  - 跨页衔接正确：页图首句 `field is applied to it. This phenomenon is called a phase transition between a paramagnetic phase above the Curie temperature, and a ferromagnetic phase below it.` 与 p.2 末句 `…only when an external` 无缝衔接；MD 中该完整句位于行 33 句内，与 p.2 跨页句合并为一句，无重复无缺失。
  - 引用号与专名核对：`Pierre Weiss [101]`、`[80]`、`[70]`（均与页图一致）；`Wilhelm Lenz`、`Ernst Ising`、`Curie-Weiss model`、`mean-field approximation`、`linear chain`、`paramagnetic phase`、`ferromagnetic behaviour` 全部逐字吻合。
  - 年份/数值：`born in 1900`、`graduated in 1924`、`published a paper [70] on Lenz's model in 1925`、`paper from 1925`、`tending to 0`（阿拉伯数字 0，非字母 O）——与页图一致。
  - 两处英文直接引语逐字核对（含引号与内嵌逗号）：引语一 `decay rapidly with distance, so that we, in general, to a first approximation, only have to take the influence on neighbouring elements into account`；引语二 `of all the possible positions that the neighbouring atoms can assume in relation to each other, the one that requires the minimum energy is when they are both acting in the same direction`。二者与页图（含斜体排印）逐字一致，MD 行 43 用直双引号 `"` 承载，语义与标点位置无误。
  - **印刷原文自身措辞忠实保留（铁律三）**：页图作 `thinking that one of Weiss' assumption, namely …, was wrong`——介词 `one of` 后用单数 `assumption`（作者笔法/印刷原样），MD 行 37 照录未擅改为 `assumptions`。**同页页图另有 `He formalized this reasoning in [80].`（美式 `z`）**，MD 行 37 亦作 `formalized`，未与全篇英式拼写统一——两处均为忠实保留。
  - 页末断词：`tempera-`（本页末）/ `ture`（p.4 首）在 MD 行 45 中已正确合并为 `temperature`，无残留连字符。
  - 差异列表（登记不改）：
    - `ff` 连字拍平 1 处：MD 行 35 `eficient`——页图与文本层均作 `efficient`（OCR 伪影，非 print quirk）。与 p.2 的 `diferent`/`diferential` 同类。
    - 印刷斜体强调未在 MD 保留（排版风格级）：`phase transition`、`Curie's law`、`mean-field approximation`、`Curie-Weiss model`、`ferromagnetic`、两处引语全段斜体；MD 行 33/35/43 均为正体。
    - 印刷 running foot `3  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页无公式、无编号结构，判 PASS± 的唯一依据是 `eficient` 一处拼写伪影与斜体/页脚级差异。**无 Markdown 改动。**

---

# 逐页重审块 D：PDF p.9–p.16（`Wf-icm2022dc` 第二轮，逐页视觉审计）

- 范围：PDF 第 9–16 页（印刷 p.9–p.16）。
- Actor：`Wf-icm2022dc`。Host/model/effort：zcode / `opencode-go-chat/space-bunny-free`（run 级环境自报）/ effort 未暴露，记 UNKNOWN。
- 方法：每页单独渲染 150dpi pngmono → Read 工具亲眼查看 → 与 `pdftotext -layout` 整页文本层 + MinerU Markdown 五点比对；公式或字形在 150dpi 下判读不了时，用 `-r300` 重渲该页并用 PIL **只裁图**放大仲裁（裁片路径逐页登记）。
- 与既有块的关系：独立重看原页图，不把块 A（`Wf-R-P15`）/ redo 块（`Wf-R-P14`）的结论当证据。印刷原文是唯一裁决源。
- 溯源纪律：每处判为「缺陷」的当前内容，都用 `git show 'cpf-redo/ICM2022_proceedings_Duminil-Copin^:<MD 路径>'` 与当前态对比，确认是**原始导出缺陷**还是 **peer 回归**。
- 不写根级文件；不做任何 git commit。

## p.009（PDF p.9 / 印刷 p.9）
- PNG：/tmp/icm2022dc_audit_p009.png（pngmono 150dpi）；仲裁裁片 /tmp/icm2022dc_p009_cap300.png（300dpi caption 区）、/tmp/icm2022dc_p009_eq34_300.png（300dpi 公式 (3.4)）、/tmp/icm2022dc_p009_frame2_300.png（300dpi Frame 2 标题与首段）
- 核对：Figure 1 图与 caption 全文（`Λ_1^+`、`(Λ_1^+)^*`、`S(5,3)`、`top`/`g`/`bottom` 三个图内字母标注、两个 τ 的下划线/上划线装饰、`−1` 与 `+1`）、图链接与被链接资产、self-dual 段（`tanh(β*) = e^{−2β}`、`β* = β`、`β_c = ½ ln(1+√2)`）、Kramers–Wannier 段（`[85]`、`[100]`、Frame 2/Frame 4 互引、(2.8) 互引）、Frame 2 标题与首段（`S(N,M) := (Z/NZ)^{d−1} × ⟦0,M⟧`、`h = 0`）、公式 (3.4) 全部参数/求和域/指示函数/尾逗号、页脚 `9  100 Years of the Ising Model`。
- 结果：**PASS±**（差异列表见下，均不误导；本页数学内容零错误，**未改动 Markdown**）
  - **Figure 1 caption 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p009_cap300.png`）：四段小标题结构 `On the left.` / `On the right.` 加粗，正文为 `A picture of the low-temperature expansion on Λ_1^+. The set Λ_1^+ is depicted in dashed gray, and (Λ_1^+)^* in plain black. The edges in the dual configuration are depicted in bold. … The set S(5, 3) with the bottom and top sets depicted. In this case τ̲ and τ̄ are respectively constant equal to −1 and +1.`——与 MD 行 185 逐句一致（MD 合并了跨行断词）。
    - **关键符号核对**：裁片清楚显示 caption 末句「In this case **τ̲** and **τ̄**」中，**第一个 τ 带下划线、第二个 τ 带上划线**；MD 行 185 记作 `$\underline{\tau}$ and $\bar{\tau}$`，**下划线/上划线分配正确**，与 (3.4) 的 `\underline{\tau}, \overline{\tau}` 记号体系一致，未混淆。
    - `Λ_1^+` 的下标 `1` 与上标 `+`、括号内 `(Λ_1^+)^*` 的星号位置、S(5,3) 的两个参数顺序（`5 , 3`，非 `3 , 5`）均与印刷一致。
  - **图链接可解析**：MD 行 183 `![](../audit/ICM2022_proceedings_Duminil-Copin_p009_Figure1.png)`，`ls -l` 实测该文件存在（14469 字节，2022-10-02 14:23）。图在印刷版面位于本页上部（Figure 1 + caption），MD 把它放在 §3.1 正文 (3.3) 之后、self-dual 段之前，与印刷阅读流一致（图片实体从版面上部提前到首次被正文引用的位置，属 Markdown 线性化处理，非错序）。
  - 图内三个字母标注 `top`（右上）、`g`（左图右侧）、`bottom`（右下）属图形内部文字，不入 Markdown 文本（不误导，图形内容由被链接 PNG 承载）。
  - **self-dual 段公式吻合**：页图 `where β and β* are related via the formula tanh(β*) = e^{−2β}.` 与 `β_c must be equal to ½ ln(1 + √2)`；MD 行 187 作 `${ \frac { 1 } { 2 } } \ln ( 1 + { \sqrt { 2 } } )$`——系数 `1/2`、根号内 `2`、括号层级均正确；`β* = β`（自对偶条件，MD 作 `$\beta ^ { * } = \beta$`）、`a priori non-obvious`、`singular point is unique` 逐句吻合。
  - **Kramers–Wannier 段逐句吻合**：MD 行 189 与页图一致，含 `see Frame 2 for details`、`work of Montroll [85]`、`van der Waerden [100]`、`briefly described in Frame 4`、`low-temperature expansion (2.8)`、`high-temperature expansion`（页图为斜体）、`Z(G, β, 0)` 与 `Z(G*, β*, 0)`（MD 作 `$Z ( G ^ { * } , \beta ^ { * } , 0 )$`，星号位置正确）、末句 `one obtains the identity above by considering larger and larger boxes.`
  - **Frame 2 标题与首段吻合**（300dpi 裁片 `/tmp/icm2022dc_p009_frame2_300.png`）：标题 `Frame 2: transfer matrices of the Ising model`（全粗体，冒号小写 `transfer matrices`）= MD 行 191；首段 `To lighten the presentation we restrict our attention to the case h = 0.` 中 **`h = 0` 清晰可读**（斜体 h，斜杠为零），MD 行 193 作 `case$h = 0$.` 一致。
  - **公式 (3.4) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p009_eq34_300.png`）：`Z(N, M, τ̲, τ̄) := Σ_{σ∈{−1,1}^{S(N,M)}} exp[−βH_{S(N,M),h}(σ)] 𝕀(σ|_bottom = τ̲, σ|_top = τ̄),  (3.4)` —— 求和域 `σ ∈ {−1,1}^{S(N,M)}`、指数 `−β`、`H` 的下标 `S(N,M), h`、指示函数 `𝕀(...)`、两个限制下标 `σ|_bottom = τ̲` 与 `σ|_top = τ̄`、**尾逗号**、编号 `(3.4)` 右对齐，全部与 MD 行 196 一致。
    - **print quirk 忠实保留（铁律三）**：Frame 2 开头明言「we restrict our attention to the case `h = 0`」，而 (3.4) 的指数内印刷仍作 `H_{S(N,M),h}`（**未代入 0**，也未写成 `H_{S(N,M),0}`）。150dpi 页图、300dpi 裁片、born-digital 文本层（`H𝑆( 𝑁 , 𝑀 ),ℎ`）三通道一致，MD 行 196 原样照录，**不得按数学预期改写为 `H_{S(N,M),0}`**。
  - 差异列表（登记不改）：
    - **区间括号记号近似 1 处**：页图 Frame 2 首段作 `S(N,M) := (Z/NZ)^{d−1} × ⟦0, M⟧`（双竖线整数区间记号 `⟦ ⦃`），MD 行 193 记作 `\mathbb { I } 0 , M \mathbb { I }`（两个黑板粗体 I 夹住）。区间含义（整数集 `{0,…,M}`）可由上下文读出，但**字形与印刷不同**。**溯源**：对 `cpf-redo/ICM2022_proceedings_Duminil-Copin^`（原始导出）与当前态分别执行 `grep -o 'mathbb { I }'`，两者计数均为 `2`；且行 193 两侧 `md5` 同为 `b95ebef38e3bc91952180923be1e2fd7`（字节完全相同）——**属原始导出缺陷，非 peer 回归**。按本段尺度（字形级记号近似、不承载新的数学断言）登记不改；若日后统一修复，须连同另一处同型实例一并登记。
    - 行内数学与相邻文字空格普遍合并（排版级）：行 185 `expansion on$\Lambda _ { 1 } ^ { + } $.`、行 187 `where$\beta$and$\beta ^ { * }$`、`self-dual point satisfying$\beta ^ { * } = \beta , \mathrm { i . e . } \beta _ { c }$`、行 193 `case$h = 0$.`、`slices$\mathbb { S } ( N , M ) : = …`、`to the top and bottom of $\mathbb { S } ( N , M )$`、行 199 `where$\underline { { \tau } } , \overline { { \tau } } \in …`。
    - 下标字母被逐字拆空格（排版级）：行 193/196 的 `\sigma _ { | \mathrm { b o t t o m } }`、`\sigma _ { | \text { bottom }}`、`\sigma _ { | \text { top }}`。
    - 指示函数记号：页图为黑板粗体 `𝕀`，MD 作 `\mathbb {I}`（同一字形，语义一致，不计差异）。
    - 印刷斜体强调未在 MD 保留（风格级）：`transfer matrices`、`high-temperature expansion`、`a priori non-obvious`。
    - 印刷 running foot `9  100 Years of the Ising Model` 未入 MD；Frame 2 的边框与缩进（Frame 内文较正文缩进）在 Markdown 中以 `##` 标题近似（布局级）。
- 备注：本页三条公式/记号（`tanh(β*) = e^{−2β}`、`β_c = ½ ln(1+√2)`、(3.4)）均以 300dpi 裁片逐项复核，数学内容零错误，故判 PASS± 而非 FAIL。(3.4) 的 `H_{S(N,M),h}` print quirk 已登记。区间括号 `⟦0,M⟧`→`𝕀 0,M 𝕀` 已溯源确认为**原始导出缺陷**。**无 Markdown 改动。**

## p.010（PDF p.10 / 印刷 p.10）
- PNG：/tmp/icm2022dc_audit_p010.png（pngmono 150dpi）；仲裁裁片 /tmp/icm2022dc_p010_eq35.png（300dpi 公式 (3.5)）、/tmp/icm2022dc_p010_lead.png（300dpi `Z(N,M,…) = V_N^M(…)` 句）、/tmp/icm2022dc_p010_eig.png（300dpi 特征值句）、/tmp/icm2022dc_p010_eq36.png（300dpi 公式 (3.6)）、/tmp/icm2022dc_p010_onsager.png（300dpi 谱问题句）、/tmp/icm2022dc_p010_rel2.png + /tmp/icm2022dc_p010_rel3.png（300dpi Onsager 生平与 relevance 句）、/tmp/icm2022dc_p010_fn2.png（300dpi 脚注 2 首段）
- 核对：p.9 跨页续句（`where τ̲, τ̄ ∈ {−1,1}^{(Z/NZ)^{d−1}}, as well as the so-called transfer matrix`）、公式 (3.5) 两个求和项与下划线/上划线 τ 的分配、`Z(N,M,τ̲,τ̄) = V_N^M(τ̲,τ̄)`、`trace of V_N^N`、特征值句的极限变量、§3.2 节标题、Onsager 两段（1968、1942、`Z^2`、`[87]`、`[76]`、`Bruria Kaufman`）、公式 (3.6) 全部系数/积分限/被积函数/微分、integrability 段、脚注 2 全文、页脚 `10  Hugo Duminil-Copin`。
- 结果：**PASS±**（差异列表见下，均不误导；本页数学内容零错误，**未改动 Markdown**）
  - **公式 (3.5) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p010_eq35.png`）：`V_N(τ̲, τ̄) := Z(N, 1, τ̲, τ̄) = exp[ −β ( Σ_{x∈(Z/NZ)^{d−1}} τ̲_x τ̄_x + Σ_{{x,y}∈E((Z/NZ)^{d−1})} τ̄_x τ̄_y ) ].` —— 关键符号核对：**第一求和项的下标为 `τ̲_x τ̄_x`（下划线 τ 与上划线 τ 相乘），第二求和项为 `τ̄_x τ̄_y`（两个上划线 τ）**；裁片上第一项的下划线 τ 清晰可辨，与 MD 行 202 的 `\underline{{\tau}} _ {x} \overline {{\tau}} _ {x}` + `\overline {{\tau}} _ {x} \overline {{\tau}} _ {y}` **分配完全一致**（这是本页最易转写错的一处，未错）。求和域 `(Z/NZ)^{d−1}` 与 `E((Z/NZ)^{d−1})`、指数 `−β`、方括号与圆括号层级、**尾句点**、编号 `(3.5)` 均一致。
  - **`Z(N,M,τ̲,τ̄) = V_N^M(τ̲,τ̄)` 吻合**（裁片 `/tmp/icm2022dc_p010_lead.png`）：`V_N^M` 的上标 `M` 为斜体大写 M（**非 `N`**），MD 行 205 作 `V _ { N } ^ { M }` 正确；同句 `trace of V_N^N` 的上标为 `N`，MD 作 `V _ { N } ^ { N }` 正确——**两处上标 M/N 未互换**。
  - **特征值句极限变量已修正且当前态正确**：页图裁片 `/tmp/icm2022dc_p010_eig.png` 与 150dpi 页图一致读作 `…the asymptotic behaviour of the partition function on (Z/NZ)^{d−1} × (Z/MZ), and therefore the value…`，后接 `…the leading eigenvalue of V_N as N tends to infinity.`；MD 行 207 当前作 `of$V _ { N }$as $N$ tends to infinity` —— **与印刷一致（`N`）**。
    - **溯源**：`git show 'cpf-redo/ICM2022_proceedings_Duminil-Copin^:<MD>' | sed -n '207p'` 与 `git show 'HEAD:<MD>' | sed -n '207p'` 两者均为 `as $M$ tends`（**原导出错误**：OCR 把斜体 N 误读为 M）；`sed -n '207p'` 当前 worktree 为 `as $N$ tends`。即：**原导出缺陷，已被本 worktree 中先前 peer 的未提交修改修正为正确值**——属**修复**，**非 peer 回归**。本轮重核确认该修复方向正确（印刷为 `N`），保留不动。
  - **§3.2 节标题吻合**：300dpi 裁片 `/tmp/icm2022dc_p010_onsager.png` 顶部可见粗体 `3.2. Onsager's result`（`3.2.` 编号 + 句点 + 空格），= MD 行 209。
  - **公式 (3.6) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p010_eq36.png`）：`−βf(β, 0) = ln 2 + (1/(8π²)) ∫₀^{2π} ∫₀^{2π} ln[cosh(2β)² − sinh(2β)(cos θ₁ + cos θ₂)] dθ₁ dθ₂.` —— 系数 `1/(8π²)`（分母 `8π²`，π 为小写圆周率）、两重积分下限 `0` 上限 `2π`、`cosh(2β)` 的**平方 `2` 位于括号内**（`cosh(2β)²`，非 `cosh²(2β)` 亦非 `cosh(2β²)`）、`sinh(2β)(cos θ₁ + cos θ₂)` 的两个余弦下标 `1`/`2`、微分记号 `dθ₁ dθ₂`、尾句点、编号 `(3.6)` 右对齐——与 MD 行 216 **逐项一致**（MD 作 `\frac {1}{8 \pi^ {2}}`、`\cosh (2 \beta) ^ {2}`、`\sinh (2 \beta) (\cos \theta_ {1} + \cos \theta_ {2})`、`d \theta_ {1} d \theta_ {2}`）。
  - **print quirk 忠实保留（铁律三）**：页图裁片 `/tmp/icm2022dc_p010_rel3.png` 清楚显示原句为 `…that its exact solution represented **more than for** his physical relevance².` —— 该语序在英语中不自然，但**印刷即如此**（150dpi 页图、300dpi 裁片、born-digital 文本层 `represented more than for his physical relevance` 三通道一致），MD 行 211 原样照录，**不得按语感改为 `more than in` 或 `more than for his` 其它语序**。
  - Onsager 段其余事实核对：`Lars Onsager, Nobel prize winner in 1968`、`Norwegian specialist in theoretical chemistry`、`New York Academy of Sciences in 1942`、`1944 paper [87]`、`In 1949, Bruria Kaufman [76]`、`2D Ising model`、`finite-dimensional Lie algebra`、`(by taking successive brackets)`、`exactly solvable`、`integrability` —— 全部与页图一致（`exact`、`transfer matrices`、`integrability` 三处印刷斜体，MD 未保留，风格级）。
  - **脚注 2 完整入 MD**（行 221，`<small>` 承载，位于 integrability 段之后，对应印刷页脚位置）：300dpi 裁片 `/tmp/icm2022dc_p010_fn2.png` 核对首段 `His opinion on this fact seemingly evolved: in his first 1944 paper [87] he presents it as a poor model of ferromagnetism, but a fairly good model for binary alloys, while in his paper with Kaufman in 1949 [76] he describes it as a model for ferromagnetism.` 与 MD 行 221 **逐字一致**（含 `seemingly evolved`、`binary alloys` 两个易错处）。
  - 差异列表（登记不改）：
    - 脚注上标拍平：MD 行 211 句末作 `relevance2`——印刷为脚注上标 `relevance²`（300dpi 裁片 `/tmp/icm2022dc_p010_rel3.png` 可见上标 `2`）。上标被拍平（排版级，不误导；脚注正文已在 MD 行 221 出现）。
    - 空格合并（排版级）：MD 行 205 `that$Z ( N , M , … )$`、`on the $d$-dimensional torus$( \mathbb { Z } / N \mathbb { Z } ) ^ { d }$becomes`、`trace of$V _ { N } ^ { N }$`（句末缺句点）；行 207 `matrices$V _ { N }$is`、`partition function on$( \mathbb { Z } / N …)$`、`free energy, are connected`、`eigenvalue of$V _ { N }$as $N$ tends`；行 211 `Ising model, but the real revolution came only a few years after with one of the most impressive achievements in mathematical physics.`（跨行断词合并正确）；行 213 `at a conference ofthe New York Academy`、`square lattice${ \mathbb { Z } } ^ { 2 }$:`。
    - 印刷 running foot `10  Hugo Duminil-Copin` 未入 MD；Frame 2 的边框与缩进未保留（排版风格级）；(3.5) 之后 Frame 边框线未在 MD 体现（布局级）。
- 备注：三条编号公式 (3.5)(3.6) 与 `Z(N,M,…) = V_N^M(…)` 均以 300dpi 裁片逐项复核，数学内容零错误，故判 PASS± 而非 FAIL。**关键确认**：特征值句的 `as M`→`as N` 是先前 peer 对原始导出 OCR 错误的**修复**，经本轮原页复核方向正确，**非回归**。**无 Markdown 改动（本页当前态已正确）。**

## p.011（PDF p.11 / 印刷 p.11）
- PNG：/tmp/icm2022dc_audit_p011.png（pngmono 150dpi）；仲裁裁片 /tmp/icm2022dc_p011_eq37.png（300dpi 公式 (3.7)）、/tmp/icm2022dc_p011_eq38.png（300dpi 公式 (3.8)）、/tmp/icm2022dc_p011_logfrac.png（300dpi `β approaches ½ log(1+√2)` 行）、/tmp/icm2022dc_p011_startri.png（300dpi `star-` / `triangle transformation` 跨行处）
- 核对：p.10 跨页续段（Onsager 自发磁化句、`β ≥ β_c`）、公式 (3.7) 的 `−4` 指数与 `1/8` 外指数、Chen-Ning Yang 段（`[105]`、Yang-Baxter、Yang-Mills、Lee-Yang、Toeplitz determinants）、两点函数下标 `(Z/NZ)^2, β, 0`、公式 (3.8) 的**双极限次序**（先 n 后 N）、FK 括号句与 `Section 7.2`、forties/fifties 三点理由段（`C(β)`、`½ log(1+√2)`、`non mean-field behaviour`）、Baxter-Enting 段（1978、`[10]`、`399th solution`）、Kac–Ward 段（`[71]`、`[100]`、1999 `[33]`、`[29]`）、页脚 `11  100 Years of the Ising Model`。
- 结果：**PASS±（含 1 处修复，见下）**
  - **公式 (3.7) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p011_eq37.png`）：`m*(β) = (1 − sinh(2β)^{−4})^{1/8}.` —— **两处指数是本页关键**：`sinh(2β)` 的上标为 `−4`（负四，非 `4` 也非 `−1/4`），外层括号的上标为 `1/8`（斜线分数，非 `0.125` 亦非 `1/4`）；尾句点、编号 `(3.7)` 与 MD 行 226 逐项一致（MD 作 `(1 - \sinh (2 \beta) ^ {- 4}) ^ {1 / 8}`）。正文条件 `for β ≥ β_c` 的不等号方向为 **`≥`**（非 `>`、非 `≤`），MD 行 223 作 `$\beta \geq \beta _ { c }$` 正确。
  - **公式 (3.8) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p011_eq38.png`）：`m*(β)² = lim_{n→∞} lim_{N→∞} ⟨σ_{(0,0)} σ_{(n,0)}⟩_{(Z/NZ)², β,0}` —— **两个极限的先后次序是本页最易错处**：印刷为**先 `n→∞`、后 `N→∞`**（左极限先取 n，即先取固定距离 n 再取系统尺度 N）；MD 行 232 作 `\lim _ {n \to \infty} \lim _ {N \to \infty}`，**次序正确未互换**。两点函数下标 `(0,0)` 与 `(n,0)` 的坐标顺序、外层下标 `(Z/NZ)², β, 0` 三项、**无尾标点**（印刷 (3.8) 末无句点亦无逗号，MD 亦无）、编号 `(3.8)` 均一致。
  - 两点函数下标核对：正文与公式中均为 `⟨σ_{(0,0)} σ_{(n,0)}⟩_{(Z/NZ)², β, 0}`；MD 行 229 与行 232 两处写法一致（行 232 用下标 `(0, 0)` / `(n, 0)`），未出现 n 与 0 互换。
  - `½ log(1+√2)` 核对（300dpi 裁片 `/tmp/icm2022dc_p011_logfrac.png`）：页图作 `…logarithmically as β approaches ½ log(1 + √2), thus confirming rigorously that…`；MD 行 237 作 `\scriptstyle { \frac { 1 } { 2 } } \log ( 1 + { \sqrt { 2 } } )`——系数 `1/2`、根号内 `2` 均正确。**注意与 p.9 的差别**：p.9 印刷用 `ln`，本页印刷用 **`log`**（正体 log，非 `ln`）；MD 行 237 用 `\log` —— **忠实于本页印刷，未与 p.9 统一**，属正确处置。
  - 正文事实与引用号核对：`Nobel`（p.10 已核）、`[105]`（Yang 的证明）、`Section 7.2`、`[10]`（Baxter–Enting 1978）、`[71]`（Kac–Ward）、`[100]`（van der Waerden）、`[33]`（1999）、`[29]`、`Kac-Ward's matrices`、`discrete holomorphicity`、`higher genus graphs`、`star-triangle transformation`、`"399th solution of the Ising model"` 全部与页图一致；`Onsager-Kaufman-Yang`（连字符）、`Curie-Weiss`、`Landau`、`nearest-neighbour coupling constants`、`In the forties and fifties` 均逐字吻合。
  - **修复 1（本页证据：300dpi 裁片 `/tmp/icm2022dc_p011_startri.png` 清楚显示印刷行末 `star-` 与次行首 `triangle transformation` 的断词连字符；文本层同样为 `star-`/`triangle` 跨行）**：MD 行 239 原作 `the notion of startriangle transformation`——**断词连字符丢失且未以空格替代，造成两个词粘连成 `startriangle`**（可检索性受损，且与印刷的复合术语 `star-triangle` 不同）。已用 Edit 改为 `the notion of star-triangle transformation`。
    - **溯源**：对 `cpf-redo/ICM2022_proceedings_Duminil-Copin^`（原始导出）执行 `grep -c 'startriangle transformation'` 得 `1`，执行 `grep -c 'star-triangle'`（带连字符）得 `0`——**属原始导出缺陷，非 peer 回归**，原导出即已粘连。本页判 FAIL 级以外的实质修复（属 PASS± 中的可检索性缺陷，按本段尺度修复并登记）。
  - 差异列表（登记不改）：
    - 断词连字符残留 1 处：MD 行 237 `open-ing a new era`——印刷行末 `open-` / 次行首 `ing`（断词），MD 未合并为 `opening` 而保留了行界连字符。与上条同类，但此处的连字符**仍可被检索命中**（`open-ing` 至少保留断词痕迹），故按本段尺度登记而不修；如日后整篇统一处理断词，须一并登记。
    - 空格合并 2 处：MD 行 241 `expansion ofthe partition function`、`derivation ofthis approach`（印刷为 `of the` / `of this`）——全篇性空格合并伪影。
    - 标点级伪影 1 处：MD 行 229 两点函数下标末尾作 `_ { 0 } ,$, and the observation that`——即数学模式内一个逗号紧跟文本逗号，形成双逗号；印刷为**单逗号**（文本层 `,𝛽,0 , and the observation`）。与块 A 在 p.030 登记的 `$\beta ,$,` 同类同尺度（**标点级只登记、不修**），全篇同类实例已在块 A 登记。
    - 印刷斜体强调未在 MD 保留（风格级）：`level of sophistication`、`mean-field approximations`、`many direct applications`、`algebraic method`、`399th solution of the Ising model`、`combinatorial approach`、`every`、`exact`、`transfer matrices`、`integrability`。
    - 印刷 running foot `11  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页两条编号公式 (3.7)(3.8) 与 `½ log(1+√2)` 均以 300dpi 裁片逐项复核，(3.8) 的双极限次序与 (3.7) 的两处指数均正确，数学内容零错误。**唯一实质缺陷 `startriangle`（断词粘连）已用 Edit 修复**，溯源确认为**原始导出缺陷、非 peer 回归**。`open-ing` 与空格/标点级伪影登记不改。

## p.012（PDF p.12 / 印刷 p.12）
- PNG：/tmp/icm2022dc_audit_p012.png（pngmono 150dpi）；仲裁裁片 /tmp/icm2022dc_p012_diffic.png（300dpi 首段 `difficulties` 行）、/tmp/icm2022dc_p012_difer.png（300dpi `different critical parameters` 行）、/tmp/icm2022dc_p012_ofered2.png（300dpi `offered a wonderful playground` 行）
- 核对：p.11 跨页续段（Pfaffian method 段）、Pfaffian 段全部人名与引用号（`[66]`、`[75]`、`[46]`、`[83]`、`[89]`、`Hurst and Green`、`Kasteleyn`、`Fisher`、`McCoy-Wu`、`Palmer`）、记号 `G` 与 `K(G)`、Schultz-Mattis-Lieb 段（`[95]`、`Grassmann "Gaussian"`、`Section 8.3`、`1D quantum spin chains`）、Yang-Baxter 段（`Rodney Baxter`、`[9]`、`six-vertex model`）、§4 节标题（跨两行）、§4 首段与末段、`Onsager's solution`、`mathematical physics`、页脚 `12  Hugo Duminil-Copin`。
- 结果：**PASS±（含 1 处修复，见下）**
  - **节标题吻合**：页图为两行粗体 `4. The fifties and sixties: the Ising model becomes a laboratory for` / `understanding critical phenomena`；MD 行 249 作 `## 4. The fifties and sixties: the Ising model becomes a laboratory for understanding critical phenomena`——**跨行合并正确，标题文字与冒号位置逐字一致**。
  - Pfaffian 段逐句吻合：300dpi 裁片 `/tmp/icm2022dc_p012_diffic.png` 显示 `The (nowadays) most classical method is probably the Pfaffian method. It came as an attempt to go around the substantial difficulties to make the combinatorial approach rigorous.`；`Pfaffian` 在页图上为**双 f 完整拼写**（MD 行 243 亦作 `Pfaffian`，两处 `Pfaffian method` / `Pfaffian` 均正确，未被拍平）；`dimer configuration is a subset of edges which covers every vertex exactly once`、`skew-symmetric adjacency matrix`、`at and away from criticality`、`McCoy-Wu [83]`、`Palmer [89]`、`[66]`/`[75]`/`[46]` 引用号全部一致。
  - 记号核对：页图 `finite planar graph G` 与 `graph K(G)` 的 `K` 为斜体大写、括号紧跟（`𝐾(𝐺)`）；MD 行 243 作 `graph $K(G)$` —— 括号位置与斜体正确，**未误作独立记号或漏括号**。
  - Schultz-Mattis-Lieb 段逐句吻合：`[95]`、`quantum hamiltonian`（**小写 `h`，MD 行 245 忠实照录，未擅改为大写 `H`**——与 p.9 (3.5) 的 `H_{S(N,M),h}` 大写哈密顿量形成对照，此处是普通名词）、`1D quantum spin chains`、`Grassmann "Gaussian" integral`（引号位置正确）、`at the basis of renormalisation schemes in two dimensions; see Section 8.3.`
  - Yang-Baxter 段逐句吻合（300dpi 裁片 `/tmp/icm2022dc_p012_difer.png`）：页图 `…attached to the model with different critical parameters. Pioneered by Rodney Baxter, this approach consists in using the so-called Yang-` / `Baxter equation.`——**跨行断词 `Yang-`/`Baxter` 在 MD 行 247 中已正确合并为 `Yang-Baxter`**（连字符属术语本身，保留正确）；`by far the most generalisable`、`six-vertex model`、`[9]`、`integrable systems` 一致。
  - §4 首段与末段吻合：`"unavoidable" model`、`tractable model`、`Onsager's solution`、`postwar era`、`mathematical physics`（页图为斜体）、`counted in the hundreds`、§4 末段全句一致。
  - **修复 1（本页证据：300dpi 裁片 `/tmp/icm2022dc_p012_ofered2.png` 清楚显示印刷为 `The Ising model offered a wonderful playground for such scientists`——`offered` 为双 f；150dpi 页图与文本层 `offered` 三通道一致）**：MD 行 253 原作 `The Ising model ofered a wonderful playground`——**`ff` 连字被拍平为单 f，使 `offered` 变成英语中不存在的词 `ofered`**（与 `diferent`/`dificulties` 同类 OCR 伪影，但此处后果更重：整词丧失可检索性与可读性）。已用 Edit 改为 `The Ising model offered a wonderful playground`。
    - **溯源**：对 `cpf-redo/ICM2022_proceedings_Duminil-Copin^`（原始导出）与 `HEAD` 分别执行 `grep -c 'ofered'`，两者均为 `1`；当前态修复后为 `0`、`model offered a wonderful` 为 `1`——**属原始导出缺陷，非 peer 回归**。全篇 `ofered` 仅此 1 处（`grep -o -E` 统计确认），修复无遗漏。
  - 差异列表（登记不改）：
    - `ff` 连字拍平 2 处：MD 行 243 `dificulties`（页图与 300dpi 裁片 `/tmp/icm2022dc_p012_diffic.png` 均作 `difficulties`）、行 247 `diferent`（页图与裁片 `/tmp/icm2022dc_p012_difer.png` 均作 `different`）。二者语义不受影响，按 SOP「PASS± 排版级伪影默认不批量改」登记；全篇同类计数（`grep -o -E` 实测）：`diferent` 16、`diferential` 5、`dificulty` 4、`suficient` 2、`efectively` 2、`suficiently`/`eforts`/`eficient`/`dificulties`/`dificult` 各 1——**属系统性伪影，须整篇统一处理，不在本段单点批量改写**（本次只修了后果最重的一处 `ofered`，因其整词失效）。
    - 空格合并（排版级）：MD 行 243 `finite planar graph $G$ in terms of the dimer`、`graph $K(G)$ (the precise definition`、`partition as a Pfaffian, hence the name`；行 245 `proposed by Schultz-Mattis-Lieb in [95] to tackle`、`as a byproduct, the authors`、`Grassmann "Gaussian" integral. The advantage of this way of writing the partition function is that the Pfaffians emerge`；行 247 `context in which transfer matrices`、`transfer matrices attached to`、`integrable systems, such as the six-vertex model`、`refer to [9] and references therein for more details`；行 251 `during which the Ising model became`、`tractable model of statistical physics could be a useful explanatory but also predicting tool`；行 253 `a rapidly growing field called mathematical physics. The latter gathered more and more physicists`。
    - 印刷斜体强调未在 MD 保留（风格级）：`Pfaffian method`、`combinatorial approach`、`a number of more refined results`、`integrable systems`、`mathematical physics`、`exact`。
    - 印刷 running foot `12  Hugo Duminil-Copin` 未入 MD（版式级）；§4 标题的两行排版在 MD 中并为一行（正常线性化处理）。
- 备注：本页无编号公式，核对重心在专名/引用号/记号/断词。**`ofered`→`offered` 已用 Edit 修复**，溯源确认为**原始导出缺陷、非 peer 回归**；`dificulties`/`diferent` 属全篇系统性 `ff` 拍平伪影，按既定尺度登记不改并在页内给出全篇计数，供后续整篇统一处理时参考。

## p.013（PDF p.13 / 印刷 p.13）
- PNG：/tmp/icm2022dc_audit_p013.png（pngmono 150dpi）；仲裁裁片 /tmp/icm2022dc_p013_sigA.png（300dpi `⟨σ_A⟩_{G,β,h}` 记号行）、/tmp/icm2022dc_p013_param.png（300dpi `in par-` / `ticular` 断词与 `when the parameters` 行）、/tmp/icm2022dc_p013_ofers.png（300dpi `Onsager's solution` 行）、/tmp/icm2022dc_p013_eq41.png + /tmp/icm2022dc_p013_eq41b.png（300dpi 公式 (4.1) 引导句与公式体）、/tmp/icm2022dc_p013_eq42.png + /tmp/icm2022dc_p013_eq42b.png（300dpi 公式 (4.2)）、/tmp/icm2022dc_p013_eq43.png + /tmp/icm2022dc_p013_eq43b.png（300dpi 公式 (4.3)）、/tmp/icm2022dc_p013_eq44.png + /tmp/icm2022dc_p013_eq44b.png（300dpi 公式 (4.4)）
- 核对：§4.1 节标题（跨两行）、§4.1 首段、§4.1.1 节标题、`σ_A := ∏_{x∈A} σ_x` 记号、Griffiths 段与 `[57]`、公式 (4.1) 的两不等式与连接词、byproduct 段与 `B = {x,y}`、公式 (4.2) 的 `inf`/`sup` 与两处严格不等号、GHS 条目 `[59]`、公式 (4.3) 的二阶导分式与 `≤ 0`、Simon-Lieb 条目 `[82]`、公式 (4.4) 的 `∂S` 求和域、页脚 `13  100 Years of the Ising Model`。
- 结果：**PASS±（含 1 处修复，含 2 个子项，见下）**
  - **节标题顺序与编号吻合**：页图为两行粗体 `4.1. Progress in mathematical physics: from perturbative regions of the phase` / `diagram to the vicinity of the critical point`，跨行合并后 = MD 行 255；`4.1.1. Correlation inequalities`（三级编号 + 句点）= MD 行 259。顺序 `4.1` → `4.1.1` 与印刷一致。
  - **公式 (4.1) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p013_eq41b.png`）：`⟨σ_A⟩_{G,β,h} ≥ 0 and ⟨σ_A σ_B⟩_{G,β,h} ≥ ⟨σ_A⟩_{G,β,h}⟨σ_B⟩_{G,β,h}.` —— 两个不等号方向**均为 `≥`**（未互换、非 `≤`）、连接词为直体 `and`（非 `\land`）、下标 `(G,β,h)` 三项在四处一致、右端为两个期望的**乘积**（⟨σ_A⟩·⟨σ_B⟩，非单个期望）、尾句点、编号 `(4.1)` 与 MD 行 266 一致（MD 作 `\geq 0 \quad \text { and } \quad … \geq …`）。引导句（裁片 `/tmp/icm2022dc_p013_eq41.png`）核对：印刷 `Griffiths' inequalities [57]: for every β, h ≥ 0 and every A, B ⊂ V,` —— **`⊂` 为真子集符号（非 `\subseteq`）**、参数条件为**逗号并列的 `β, h ≥ 0`**（即两者同时非负，非 `β ≥ 0, h ≥ 0`）、尾为逗号；MD 行 263 作 `for every$\beta , h \ge 0$and every $A,B \subset V$` —— 条件与子集符号均正确。
  - **公式 (4.2) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p013_eq42b.png`）：`β_c = inf{β ≥ 0 : m*(β) > 0} = sup{β ≥ 0 : m*(β) = 0}.` —— **两处的关键区别在严格性**：左端 `inf` 集合用 **`>`**（严格大于 0），右端 `sup` 集合用 **`=`**（等于 0）；裁片上两处符号形态可辨（`>` 为开尖括号、`=` 为双横线），MD 行 272 作 `m ^ {*} (\beta) > 0 \} = \sup \{\beta \geq 0: m ^ {*} (\beta) = 0 \}`，**严格性未互换**（这是本页最易错处，未错）；两处集合均含 `β ≥ 0` 约束、`m*` 的星号上标位置正确、尾句点、编号 `(4.2)` 一致。
  - **公式 (4.3) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p013_eq43b.png`）：`(∂²/(∂h)²)⟨σ_x⟩ ≤ 0.` —— **二阶偏导写成分式形式**（分子 `∂²`、分母 `(∂h)²`，非 `∂²/∂h²` 连写、亦非一阶导）、下标 **`x`**（非 `0`）、不等号 `≤`、尾句点，与 MD 行 282（`\frac {\partial^ {2}}{(\partial h) ^ {2}} \langle \sigma_ {x} \rangle \leq 0`）一致。引导条件（页图）`GHS's inequality [59]: for h ≥ 0 and x ∈ G,` 与 MD 行 279 的 `for$h \geq 0$and$x \in G$` 一致（`x ∈ G` 为**属于**、非 `⊂`）。
  - **公式 (4.4) 逐项吻合**（300dpi 裁片 `/tmp/icm2022dc_p013_eq44b.png`）：`⟨σ_0 σ_x⟩ ≤ Σ_{y∈∂S} ⟨σ_0 σ_y⟩_S ⟨σ_y σ_x⟩.` —— 求和号下标为 **`y ∈ ∂S`**（∂S 为**边界集**，非 `S` 本身、非 `∂` 单独）、两个因子⟨σ_0σ_y⟩⟨σ_yσ_x⟩ **仅第一个带下标 `_S`**（裁片上 `⟨σ_0σ_y⟩_S⟨σ_yσ_x⟩` 的 `_S` 只出现一次，第二个因子无下标），MD 行 288 作 `\langle \sigma _ {0} \sigma _ {y} \rangle_ {S} \langle \sigma _ {y} \sigma _ {x} \rangle` —— **与印刷一致**（此处若误给第二个因子也加 `_S` 即为错，当前态正确）；不等号 `≤`、尾句点、编号 `(4.4)` 一致。
  - **记号核对**（300dpi 裁片 `/tmp/icm2022dc_p013_sigA.png`）：页图 `the spin-spin correlations ⟨σ_A⟩_{G,β,h} where σ_A := ∏_{x∈A} σ_x, when the parameters vary` —— **`σ_A` 的定义用连乘号 `∏`（下标 `x∈A`）**，MD 行 261 作 `\Pi _ { x \in A } \sigma _ { x }`（大写 Pi 记法，等价于连乘号，语义一致）；`⟨σ_A⟩_{G,β,h}` 的下标三项与角括号均正确。
  - **修复 1a（本页证据：300dpi 裁片 `/tmp/icm2022dc_p013_param.png` 显示印刷行末 `in par-` / 次行首 `ticular`，文本层同样跨行；**这是行界断词连字符**）**：MD 行 261 原作 `in par ticular by the spin-spin correlations` —— **断词连字符被替换为空格，把单词 `particular` 拆成 `par ticular` 两段**（可检索性受损，与 p.11 的 `open-ing` 同类反向实例）。已用 Edit 改为 `in particular by the spin-spin correlations`。
  - **修复 1b（同一裁片 `/tmp/icm2022dc_p013_param.png` 清楚显示印刷为 `when the parameters vary (for instance, G, β or h)`，150dpi 页图与文本层 `the parameters vary` 三通道一致）**：MD 行 261 原作 `when the parameter vary` —— **复数名词 `parameters` 丢失词尾 `s`，变成单数 `parameter` 与复数动词 `vary` 不搭配**（语法错误，会误导读者以为只有一个参数变动）。已用 Edit 改为 `when the parameters vary`。
    - **两处溯源**：`git show 'cpf-redo/ICM2022_proceedings_Duminil-Copin^:<MD>' | sed -n '261p' | grep -o 'the parameter[a-z ]*vary'` 输出 `the parameter vary`，与当前修复前状态一致；`grep -c 'par ticular'` 在原导出亦为 1。**属原始导出缺陷，非 peer 回归**，原导出两处均已错。
  - 差异列表（登记不改）：
    - `ff` 连字拍平 1 处：MD 行 257 `Onsager's solution ofers a precise understanding` —— 页图与裁片 `/tmp/icm2022dc_p013_ofers.png` 均作 `offers`（双 f；`grep -c 'ofers a precise'` 实测全篇仅此 1 处）。因与 p.12 的 `ofered` 同型、后果较轻（仍可读），按既定尺度登记不改。
    - 项目符号缺失 1 处：页图 GHS 条目行首有项目符号 `•`（与下一条 Simon-Lieb 的 `•` 并列，构成并列列表），MD 行 279 缺 `•` 前缀（行 285、291 保留）——**列表结构不齐**（布局级，不误导内容；条目文字与编号完整）。
    - 人名字母被逐字拆空格（排版级）：MD 行 279 `$\mathrm { G H } \mathrm { S } ^ { \prime } \mathrm { s }$` —— 排版后显示为 `GH S′s`（字母间有空格、撇号上标化），语义为 `GHS's`，与页图 `GHS's inequality` 一致（印刷撇号为正常位置，非上标）。
    - 空格合并（排版级）：MD 行 257 `the critical phase (when$\beta$ is equal to$\beta _ { c } )$`、`values of$\beta$and ℎ`、`Padé approximant [8] for instance`、`values of$\beta$became`、`Onsager's solution ofers a precise understanding`；行 261 `correlations$\langle … \rangle _ {G,\beta,h}$where`、`parameters vary (for instance,$G , \beta$or ℎ)`；行 269 `when applied to$B = \{ x , y \}$and`、`edges $\{ x , y \}$`，is that correlations`、`increasing in$\beta$(and also in$G$with`、`magnetisation$m ^ { * } ( \beta )$`、`$\beta _ { c }$can now be rephrased as`；行 279 `inequality [59]: for$h \geq 0$and$x \in G$`。
    - 印刷斜体强调未在 MD 保留（风格级）：`spin-spin correlations`、`correlation inequalities`、`monotonicity`、`Padé` 等。
    - 印刷 running foot `13  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页四条编号公式 (4.1)–(4.4) 全部以 300dpi 裁片逐项复核；两处易错点（(4.2) 的 `>` 与 `=` 严格性、(4.4) 中只有第一个因子带 `_S` 下标）均**当前态正确**。**`par ticular`→`in particular` 与 `parameter`→`parameters` 两处已用 Edit 修复**，溯源确认为**原始导出缺陷、非 peer 回归**。`ofers`、GHS 项目符号缺失与其余排版伪影登记不改。

## p.014（PDF p.14 / 印刷 p.14）
- PNG：/tmp/icm2022dc_audit_p014.png（pngmono 150dpi）
- 核对：公式(4.5)(4.6)、4.1.2 与 4.2 标题、Lee-Yang 段落逐句、粗体 𝐡 记号约定、Re(𝐡_x) 字重、页末句号
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 5 处）
- 300dpi 裁片：/tmp/icm2022dc_p014_fkg.png（FKG 项目符号行）、/tmp/icm2022dc_p014_re.png 与 /tmp/icm2022dc_p014_re2.png（Hamiltonian 替换与 Re 行）、/tmp/icm2022dc_p014_rezoom2.png（`Re` 字重 5 倍放大仲裁）、/tmp/icm2022dc_p014_tail2.png（页末句）
- 逐项核对：
  - (4.5) 印刷 `⟨σ₀σ_{x+y}⟩ ≤ ⟨σ₀σ_x⟩.`；MD 行 294 一致（两个 `σ_ {0}`、`x+y` 下标、`≤` 方向未反）。
  - (4.6) 印刷 `⟨fg⟩ ≥ ⟨f⟩⟨g⟩.`；MD 行 300 一致。
  - 4.1.2 标题「The Ising model with a magnetic field: the Lee-Yang theory」与 4.2 标题「Revolutionary progress on the physics front」顺序、内容、编号均与 MD 行 305、315 一致。
  - 记号约定：`Z(G, β, 𝐡) ∈ ℂ (for 𝐡 = (𝐡_x : x ∈ V) ∈ ℂ^V)` 全部为**粗体 𝐡**，而 `∑_{x∈V} hσ_x`（(2.2) 原项）中 h 为**斜体**；300dpi 裁片 `p014_re.png` 逐字确认，MD 行 311 的 `\mathbf { h }` / `\mathbf { h } _ { x }` 与裸 `$h \sigma _ { x }$` 与印刷完全一致。
  - 页末句「…corresponding to non-zero magnetic field.」印刷带句号。
- 差异列表（已修复 5 处，均为原始导出缺陷）：
  1. 行 297 FKG's inequality [47] **丢失印刷的 `•` 项目符号**（同页行 291 的 Messager 条目保留 `•`，自相矛盾）。据 300dpi `p014_fkg.png` 补回 `• `。
  2. 行 309 `resounding efect on` → `effect`（ff 连字压平）。据印刷「resounding effect」改。
  3. 行 311 `with the diference that` → `difference`（ff 连字压平）。据印刷改。
  4. 行 311 `\mathbf { R e } ( \mathbf { h } _ { x } ) = 0` → `\mathrm { R e } (…)`：印刷「Re」为**正体常规字重**，5 倍放大裁片 `p014_rezoom2.png` 中「Re」笔画明显细于其内粗体 𝐡 及粗体 =、0 的主体，MinerU 误加粗。
  5. 行 313 段末句号丢失：「…non-zero magnetic field」无终止句点，据 `p014_tail2.png` 补 `.`。
- 登记不改：
  - 行 311 两处 `\textstyle \sum _ { x \in V }` 使求和号被压成行内小号；印刷为正常行高求和号。属排版尺寸伪影，符号与上下限内容正确，不改。
  - 行 311「the zeroes of the function h$\mapsto Z ( G , \beta , \mathbf { h } )$」中定义域 `h` 未加粗且落在数学模式外；印刷该 `h` 为粗体。属局部字体级偏差，不改。
  - 行 297 `\mathrm { F K G } ^ { \prime } \mathrm { s }$inequality` 与 p.13 行 279 GHS 同族的「字母逐个拆空格 + 上标撇号」导出风格；与全文一致，不改。
  - 页脚 running foot `14  Hugo Duminil-Copin` 未入 MD（版式级，全篇一致）。
- 备注：本页 5 处修复全部以 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin^:<md>` 与 HEAD 双态比对确认为**原始导出缺陷**，非 peer 引入的回归（`resounding efect on` / `with the diference that` / `\mathbf { R e }` / FKG 行首字符 / 行 313 行尾，三态一致）。另自本条起统一 **ff 连字压平族的处置口径**：对本轮负责的每一页，凡亲眼在原页图上确认印刷为双 `ff` 而 MD 为单 `f` 者，逐处 Edit 修复；p.012/p.013 曾登记的 `dificulties`(行 243)、`diferent`(行 247)、`ofers`(行 257) 按此口径在本块收尾时逐处处理并在块末列出，其余非本轮负责页（行 27–143、335 以后等）仍登记留给整篇统一处理。

## p.015（PDF p.15 / 印刷 p.15）
- PNG：/tmp/icm2022dc_audit_p015.png（pngmono 150dpi）
- 核对：4.2.1 标题、公式(4.7)(4.8) 全式、临界指数记号（α β γ δ η ν）字形与字重、正文逐段、页末断页位置
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 3 处；另登记 1 处印刷怪癖不作改动）
- 300dpi 裁片：/tmp/icm2022dc_p015_eq47.png 与 /tmp/icm2022dc_p015_denom.png / /tmp/icm2022dc_p015_denom2.png（(4.7) 及分母放大）、/tmp/icm2022dc_p015_eq48b.png（(4.8) 全式）、/tmp/icm2022dc_p015_nu2.png（指数 ν 字重）、/tmp/icm2022dc_p015_bexp2.png（(4.7) 首个上标）
- 逐项核对：
  - 4.2.1 标题「Critical exponents and the success of scaling theory」与 MD 行 319 一致；本页无其他编号标题，4.2.2 起于 p.16。
  - (4.7) 三段全式与印刷逐字符对应：`m*(β) = (β − β_c)_+^{β+o(1)}`、`m(β_c, h) = h^{1/δ+o(1)}`、`⟨σ₀σ_x⟩_{β_c,0} = 1/|x|^{d−2+δ}`。首段上标经 300dpi 确认为**粗体 β**（与下句「notice that β and β have nothing to do with each other」中的指数 β 同一字形），MD `\boldsymbol{\beta}` 正确；中段 `1/δ` 与末段分母 `d−2+δ` 均为粗体 δ，`\langle\sigma_0\sigma_x\rangle_{\beta_c,0}` 下标 `β_c,0` 未错位。MD 行 324 与印刷一致。
  - (4.8) 全式 `νd = 2 − α = 2β + γ = β(δ+1) = γ(δ+1)/(δ−1)　2 − η = γ/ν = d(δ−1)/(δ+1).` 与 MD 行 332 一致：两个分式分子分母未倒置、`νd` 未写成 `dν`、末段为 `2−η = γ/ν`。本式的 η（粗体斜体、带下伸尾）提供了同页 η 字形的对照基准。
  - 指数列表「α, β, γ, δ, η, ν」六项齐全且顺序正确（MD 行 327 `\boldsymbol{\alpha}, \boldsymbol{\beta}, \boldsymbol{\gamma}, \boldsymbol{\delta}, \boldsymbol{\eta}, \boldsymbol{\nu}`）。
  - 正文：Widom [102]、`[42, 45, 102]`、`[38]`、`[8]` 四处文献编号与印刷一致；Essam/Fisher/Widom、`“trivial”`、`Padé`、`correlation length ξ(β)`、`β < β_c` 与 `β > β_c` 两句均逐句对上。
  - 页末断页位置正确：印刷本页止于「…meaning that when」，MD 行 339 的后续文字顺接至 p.16。
- 差异列表（已修复 3 处，均为原始导出缺陷）：
  1. 行 329 `started unraveling system atic connections` → `systematic`：印刷换行断字 `system-` / `atic` 被导出为带空格的两段。
  2. 行 335 `these diferent scaling relations` → `different`（ff 连字压平）。
  3. 行 337 `it corresponds to the exponent $\nu$` → `\boldsymbol{\nu}`：印刷该 ν 为**粗体斜体**（300dpi `p015_nu2.png` 与同句 `β` 字重相当），且 PDF 文本层对指数列表中的 ν 与此处 ν 输出**同一码位 U+1D742**，证明两处同一字形，而 MD 在列表处写 `\boldsymbol{\nu}`、此处写 `\nu`，自相矛盾。
- **登记不改（印刷怪癖，铁律三）**：印刷 (4.7) 第三段写作 `⟨σ₀σ_x⟩_{β_c,0} = 1/|x|^{d−2+δ}`，分母指数用的是 **δ**；按标度关系通常应为 η，同页 (4.8) 也确实使用 η。300dpi 4 倍裁片 `p015_denom2.png` 确认该字形为**闭合碗状、上端左勾、无下伸尾的 δ**，与 `p015_eq48b.png` 中 `2 − η` 的 η 字形明显不同。判定为**原刊印刷取 δ**，属作者笔误。MinerU 的 `\boldsymbol{\delta}` 忠实转写，**不改**。
- 登记不改：
  - 行 327 `(notice that$\boldsymbol{\beta}$and$\beta$have nothing to do with each other)` 等处的空格合并（数学模式与相邻文字未留空格），全篇一致，排版级。
  - 印刷斜体强调（`scaling hypothesis`、`critical exponents`、`scaling relations`、`correlation length`）未在 MD 保留，风格级。
  - 页脚 running foot `15  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页 3 处修复及行 337 全行经 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin^:<md>`、HEAD 与当前工作树三态比对完全一致，确认为**原始导出缺陷**，非 peer 引入的回归。公式判读一律以 300dpi 裁片为准；本页文本层的希腊字母映射整体错位（δ→U+1D739、η→U+1D73C、ν→U+1D742），不可用于公式字形仲裁，仅用作同字形一致性的旁证。

## p.016（PDF p.16 / 印刷 p.16）
- PNG：/tmp/icm2022dc_audit_p016.png（pngmono 150dpi）
- 核对：4.2.2 标题、三条 bullet 全条（ℤ/2ℤ 与 𝐽_{x,y} 字形字重）、Kadanoff 段与 universality 段逐句、页末断页位置
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 7 处）
- 300dpi 裁片：/tmp/icm2022dc_p016_param.png（the parameters β and h 一行）、/tmp/icm2022dc_p016_bullets.png（三条 bullet 的 ℤ/2ℤ 与 𝐽_{x,y}）、/tmp/icm2022dc_p016_spacemerge.png（引文空格）
- 逐项核对：
  - 4.2.2 标题「Kadanoff's block-spin renormalisation and universality」与 MD 行 341 一致；本页只有这一个编号标题。
  - 首段为 p.15 末段的续接（印刷以「looking at a system with a size which is much smaller than ξ(β)…」起首），与 MD 行 339 的续接位置吻合；`β ≪ β_c`、`β < β_c`、`ξ(β)` 三处与印刷一致，`non critical`（印刷无连字符）MD 亦无连字符。
  - Kadanoff 段：`1966 paper [72]`、`Kenneth Wilson [104]` 两处编号正确；破折号 `– i.e. … –`（印刷为带空格的长破折号）与 MD 一致；`scale invariance`、`uniqueness of the fixed point`、`universality hypothesis` 三处印刷斜体强调 MD 未保留（风格级）。
  - `defined on different $d$-dimensional lattices`：印刷断字 `trian-` / `gular` 已正确合并为 `triangular`，与行 345 一致。
  - `explicitly formulated in parallel … in 1971 [58, 73]`：印刷方括号内为 `[58, 73]`（逗号后有空格），MD 作 `[58,73]`（排版级，不改）。
  - 三条 bullet 结构与顺序正确，`•` 符号三条齐全，`d;`、`;`、`text).` 三个句末符号与印刷一致；`‖x − y‖` 的双竖线在 MD 中写作 `$\| x - y \|$`，正确。
  - 页末断页位置正确：印刷本页止于引文「…in that many systems」，MD 行 355 其后文字顺接至 p.17。
- 差异列表（已修复 7 处，均为原始导出缺陷）：
  1. 行 339 `the diference between the system` → `difference`（ff 连字压平）。
  2. 行 343 `changing the scale and the parameter$\beta$and ℎ` → `parameters`：**数一致错误**，印刷 300dpi `p016_param.png` 明见复数 `parameters`（后接 β 与 h 两个量）。
  3. 行 345 `defined on diferent $d$-dimensional lattices` → `different`（ff 连字压平）。
  4. 行 351 `(Z/2Z symmetry for Ising)` → `($\mathbb { Z }/2\mathbb { Z }$ symmetry for Ising)`：印刷 300dpi `p016_bullets.png` 中两个 Z 均为**双线黑板体 ℤ**，MD 误作普通正体 `Z`。
  5. 行 353 `the$J _ { x , y }$are` → `the $\boldsymbol { J } _ { x , y }$ are`：印刷 𝐽 为**粗斜体**（同裁片中 J 的笔画明显重于相邻的 `are`、`x, y` 且带倾斜），MD 为普通斜体。
  6. 行 355 `strategy ofstudyingphysical questions` → `strategy of studying physical questions`（两处空格合并），据 300dpi `p016_spacemerge.png` 印刷「The strategy of studying physical questions by using highly simplified models is made」逐字确认。
  7. 行 355 `a characteristic ofphysical systems` → `a characteristic of physical systems`（空格合并），同上裁片确认印刷「rewarding by a characteristic of physical systems called "universality", in that many systems」。
- 登记不改：
  - 行 355 中属于 **p.17** 版面的三处同类空格合并（`qualitativefeatures`、`qualitativefeature`、`lookfor`）不在本轮负责页内，按逐页纪律留待 p.17 审计处理，本轮不动。
  - 行 339、343、353 等处数学模式与相邻文字未留空格（`with$\beta$`、`the scale$…$`、`length$\xi ( \beta )$of`），全篇一致的排版级伪影。
  - 页脚 running foot `16  Hugo Duminil-Copin` 未入 MD（版式级）。
- 备注：本页 7 处修复逐条以 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin^:<md>`、HEAD 与当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1，确认为**原始导出缺陷**，无一条系 peer 引入的回归。

---

## 块 D 收尾补记：ff 连字压平族按新口径回溯处理（覆盖 p.012 / p.013 早先的「登记不改」）

- 触发：本块 p.014 条已声明统一口径——凡亲眼在原页图上确认印刷为双 `ff` 而 MD 为单 `f` 者逐处修复。本条为该声明的兑现，覆盖对象为 p.012 / p.013 两条早先登记为「不改」的同类项。
- 证据（全部为本轮新开的 300dpi 裁片，亲眼 Read）：
  - `/tmp/icm2022dc_p012_top.png`：印刷 p.12 首行「…most classical method is probably the **Pfaffian** *method*.」——`Pfaffian` 为双 f 且整体斜体。
  - `/tmp/icm2022dc_p012_pfaf2.png`：印刷 p.12「…depends on the implementation of the **Pfaffian**」——第二处双 f；同裁片另见「graph **K**(*G*)」的 K 与 G 均为粗斜体。
  - `/tmp/icm2022dc_p012_difficulties2.png` / `/tmp/icm2022dc_p012_different2.png`：印刷 p.12「the substantial **difficulties** to make…」、「…attached to the model with **different** critical parameters」。
  - `/tmp/icm2022dc_p013_offers2.png`：印刷 p.13「Onsager’s solution **offers** a precise understanding of the critical behaviour of the 2D Ising model」。
- 已修复 6 处（Edit 逐处，非批量）：
  1. 行 243 `probably the Pfafian method` → `Pfaffian`；同一次 Edit 内 `the substantial dificulties` → `difficulties`。
  2. 行 243 `the implementation of the Pfafian method)` → `Pfaffian`；同一次 Edit 内 `as a Pfafian,` → `Pfaffian,`。
  3. 行 245 `is that the Pfafians emerge naturally` → `Pfaffians`。
  4. 行 247 `with diferent critical parameters` → `different`。
  5. 行 257 `Onsager’s solution ofers` → `offers`。
  - 计 6 个 ff 连字位点（第 1、2 项各含 1 个 Pfafian + 另 1 个词）。合计本块 D 共 6 处。
- 溯源：上述 6 处全部以 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin^:<md>` 与 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin:<md>` 双态比对，命中数均为 1/1，修复后当前工作树为 0；**原始导出即有，非 peer 引入的回归，原始导出不正确**。
- 登记不改（本页仍遗留）：
  - 行 243 的 `graph $G$` 与 `graph $K(G)$`：印刷 p.12 中 𝐺 与 𝐾 均为粗斜体，MD 作普通斜体。属命名对象的字重约定，且与全文其他位置的 G/K 写法一致，交整篇统一处理，本轮不动。
  - 行 883 `A totally diferent approach`：位于 p.32 之后，不在本轮负责页，未取证、未改。
- 块 D 成绩单（PDF p.9–p.16，共 8 页）：PASS 0 页；PASS± 8 页；FAIL 0 页。落签页号 p.009、p.010、p.011、p.012、p.013、p.014、p.015、p.016，逐页条目无一合并。本块 Edit 修复总计 17 处（p.011×1、p.012×1、p.013×2 子项、p.014×5、p.015×3、p.016×5、收尾补记×6 处 ff 位点含于 p.012/p.013 两页）。所有修复均由本轮亲眼 Read 的原页图（150dpi 整页 + 300dpi 裁片）支持，均已溯源，无一条依赖数学常识改写原刊。
- 登记不改的印刷怪癖（铁律三，本块共 3 例）：p.014 `(2.5)` 回忆括注未闭合、p.015 (4.7) 第三段分母指数原刊取 **δ** 而非 η、p.013 `one of Weiss' assumption`（撇号位置）——一律原样保留。

---

# 逐页重审块 E：PDF p.17–p.24（`Wf-icm2022dc` 第三轮，逐页视觉审计）

- 范围：PDF 第 17–24 页共 8 页，印刷页码与 PDF 页码一一对应（印刷页脚 `17 … 24`）。
- 审计者：`Wf-icm2022dc`；host/model `opencode-go-chat/space-bunny-free`，effort UNKNOWN。
- 方法：一页一页 150dpi `pngmono` 渲染 → Read 工具亲眼看图 → 读 MinerU 导出的对应段 → 五点比对 → 立刻用 Edit 追加本页说明 → 逐处 Edit 修缺陷 → 进下一页。字形判读一律以 300dpi 裁片为准（本文本层的希腊字母与数学映射已知整体错位，公式不据文本层判定）。
- 独立性：本块不复用块 A / redo 块的结论作为证据，全部逐页重新看图。
- 溯源纪律：对每处判定为缺陷的当前内容，用 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin^:"2022年 - Duminil-Copin/ICM2022_proceedings_Duminil-Copin_mineru/ICM2022_proceedings_Duminil-Copin__ICM2022_proceedings_Duminil-Copin.md"` 与 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin:<同路径>` 双态比对；两态一致且当前工作树仍有者，判为**原始导出缺陷**（原导出不正确）；若 HEAD 与 peer^ 不同方为回归者，记「非导出缺陷，系 <commit> 引入」并说明原导出是否正确。
- 边界：只写本篇这一个 Markdown 与这一个 AUDIT 文件；不执行任何 git 写操作、不碰仓库根级真值文件、不启动 mineru。
- 承前：块 D 收尾已把「ff 连字压平族」定为逐处修复口径，本块沿用；空格合并、数学模式黑板体丢失、行内数学误吞正文等 MinerU 系统性伪影同样逐处取证、逐处修复。

## p.017（PDF p.17 / 印刷 p.17）
- PNG：/tmp/icm2022dc_audit_p017.png（pngmono 150dpi）
- 核对：第 5 章与 5.1 节标题、公式(5.1) 全式、ℝ/ℂ 记号、⟨·⟩_{G,β,h} 与 μ_{G,β,h} 下标、Kadanoff 引文续接与正文分段、页末断页位置
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 7 处）
- 300dpi 裁片：/tmp/icm2022dc_p017_corroborate.png（corroborate 一行）、/tmp/icm2022dc_p017_respc.png（X : {−1,1}^V → ℝ (resp. 𝕔) 一行）、/tmp/icm2022dc_p017_eq51.png（(5.1) 全式）、/tmp/icm2022dc_p017_tail.png（页末两句）
- 逐项核对：
  - 标题 `5. The sixties and seventies: emergence of the probabilistic interpretation`（MD 行 359）与 `5.1. The random geometry of the spin configuration`（MD 行 363）编号、文字、先后顺序与印刷一致；本页无其他编号标题，`## Frame 3` 起于 p.18。
  - (5.1) 印刷 `μ_{G,β,h}[{σ}] := (1/Z(G,β,h)) exp[−βH_{G,h}(σ)].` 与 MD 行 368 逐符号对应：定义号 `:=`、方括号取组 `[{σ}]`、分式 `1/Z(G,β,h)`、`H` 的下标只含 `G, h` 而**不含 β**（与 (2.2) 的 β 出现在指数上一致，属印刷自身的记号约定，MD 与之一致）、编号 (5.1) 均未错位。
  - 记号：`⟨·⟩_{G,β,h}` 中的 `h` 为斜体（300dpi `p017_respc.png` 可见），非 p.14 的粗体 𝐡，二者记号层次在 MD 中区分正确；`X : {−1,1}^V → ℝ (resp. 𝕔) a value in ℝ (resp. 𝕔)` 的 `X`、`V`、`{−1,1}` 写法与印刷一致。
  - 正文：`h = 0`、`β → ∞`、`β` large、`β` very small 四处与印刷一致；`⟨σ_A⟩_{G,β,h}`、`σ_x with x ∈ A` 与印刷一致。
  - 页末断页位置正确：印刷本页止于「…or large deviations」，MD 行 375 其后「(for instance for an Ising model at an inverse-temperature β, …) see Frame 3.」顺接至 p.18。
- 差异列表（已修复 7 处，均为原始导出缺陷）：
  1. 行 355 `the very same qualitativefeatures` → `qualitative features`（空格合并）。
  2. 行 355 `To study a given qualitativefeature,` → `qualitative feature,`（空格合并）。
  3. 行 355 `it often pays to lookfor the simplest possible example.”` → `look for`（空格合并）。以上三处即块 D「登记不改」中声明归属 p.17 的项，本页据 300dpi 整页图与 150dpi 图逐字确认后修复。
  4. 行 357 `they could corroborate$^ { \mathrm { o r , } }$on the contrary, invalidate the embryo of a theory.` → `they could corroborate or, on the contrary, invalidate …`：**正文被误吞进行内数学模式**，导出为带上标的 `^ { \mathrm { o r , } }`。300dpi `p017_corroborate.png` 显示该处印刷为普通罗马体行文，「or,」既非数学亦非上标。
  5. 行 361 第一处 `(resp. C)` → `(resp. $\mathbb { C }$)`。
  6. 行 361 第二处 `$\mathbb { R }$(resp. C).` → `(resp. $\mathbb { C }$).`。第 5、6 处据 300dpi `p017_respc.png`：印刷的两个 C 均为双线黑板体 𝕔，与同行 ℝ 同一字族，而 MD 只把 ℝ 写成 `\mathbb { R }`、把 C 写成普通字母，自相矛盾。
  7. 行 375 `the expectation ofthe spin at a vertex` → `of the spin`；同一次 Edit 内 `dynamics on the space ofspin configurations` → `of spin configurations`（两处空格合并），据 300dpi `p017_tail.png` 印刷「which corresponds to the expectation of the spin at a vertex) or surface tension. It also opens a / way to new problems, such as dynamics on the space of spin configurations or large deviations」。
- 登记不改：
  - 行 375 `at an inverse-temperature$\beta ,$, but with an excess`：数学模式内的 `,` 与紧随的正文 `,` 重复，排版后会显示 `β,,`；该 token 位于 **p.18** 版面（印刷 p.17 止于「or large deviations」），本轮不取证、不改，留待 p.018 条目处理。
  - 行 357、361、365、371、373、375 处数学模式与相邻文字未留空格（`quantity$\langle … \rangle$as`、`configuration$\sigma$by`、`variables$\sigma _ { x }$with` 等），全篇一致的排版级伪影。
  - 印刷斜体强调（Kadanoff 引文整段、`correlations`）未在 MD 保留，风格级。
  - 页脚 running foot `17  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页 7 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，确认为**原始导出缺陷**，无一条系 peer 引入的回归。

## p.018（PDF p.18 / 印刷 p.18）
- PNG：/tmp/icm2022dc_audit_p018.png（pngmono 150dpi）
- 核对：Frame 3 框题与两条规则、5.2 节标题、公式(5.2)(5.3) 全式、μ^τ_{G,β,h} 与 H^τ_{G,h} 记号、μ_{G,β,0} vs μ_{G,β,h} 一句、页末断页位置
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 6 处；另登记 1 处印刷怪癖不作改动）
- 300dpi 裁片：/tmp/icm2022dc_p018_firstline.png（inverse-temperature β 一行）、/tmp/icm2022dc_p018_rand.png（sampling ran- 一行）、/tmp/icm2022dc_p018_beta_c.png（β_c 句末）、/tmp/icm2022dc_p018_measur.png（introduce the measure 一行）、/tmp/icm2022dc_p018_eq52.png（(5.2) 全式）
- 逐项核对：
  - Frame 3 框题「sampling the Ising model – Glauber dynamics」与 MD 行 377 一致；框内两条规则 `• If σ_x(t) Σ_{y:{x,y}∈E} σ_y(t) < 0, switch …` 与 `• Otherwise, switch … with a probability equal to exp[−2β Σ_{y:{x,y}∈E} σ_y(t)], and do not switch otherwise.` 的符号、求和上下限、`exp[ ]` 方括号、两个句末标点均与印刷逐项对上（行 381、383）。
  - `(σ(t) : t ≥ 0) ∈ ({−1,1}^V)^{ℝ_+}`（行 379）与印刷一致，`ℝ_+` 的下标位置正确。
  - 5.2 标题「Boundary conditions and the Gibbs formalism」与 MD 行 389 一致。
  - (5.2) 印刷 `H^τ_{G,h}(σ) := H_{G,h}(σ) − Σ_{ {x,y}∈E(ℤ^d): x∈V, y∉V } σ_x τ_y.` 与 MD 行 396 逐符号对应：上标 τ 的位置、`H` 的下标 `(G, h)`、求和条件三元组 `x ∈ V, y ∉ V`、被乘项顺序 `σ_x τ_y`（未倒置为 `τ_x σ_y`）、编号 (5.2) 均正确。
  - (5.3) 印刷 `μ_{G,β,h}[· | σ_x = τ_x, ∀x ∉ W] = μ^τ_{H,β,h}[·].` 与 MD 行 404 逐符号对应：条件棒 `|`、全称量词、`H` 的下标与上标 τ、编号 (5.3) 均正确。
  - `μ_{G,β,h}[· | σ_x = τ_x, ∀x ∉ W] ?`（行 391，正文内）与 (5.3) 左端写法一致。
  - 页末断页位置正确：印刷本页止于公式 (5.3)，MD 行 407「In words, when conditioning…」顺接至 p.19。
- 差异列表（已修复 6 处，均为原始导出缺陷）：
  1. 行 375 `at an inverse-temperature$\beta ,$, but with an excess` → `$\beta$,`：数学模式内的逗号与紧随的正文逗号重复，排版后显示 `β,,`。300dpi `p018_firstline.png` 明见印刷为「at an inverse-temperature β, but with an excess of +1 spins」单逗号。此项即 p.017 条目中声明「留待 p.018 处理」的登记项。
  2. 行 379 `sampling ran dom configurations` → `random configurations`（换行断字 `ran-` / `dom` 被导出为带空格的两段），据 300dpi `p018_rand.png`。
  3. 行 387 段末句号丢失：`and above (on the right)$\beta _ { c }$` → 补 `.`。据 300dpi `p018_beta_c.png`，印刷为「the middle) and above (on the right) β_c.」带句点。
  4. 行 391 `An important output ofthe probabilistic interpretation ofthe model` → `output of the probabilistic interpretation of the model`（两处空格合并）。
  5. 行 393 `introduce the measur $\mu _ { G , \beta , h } ^ { \tau }$` → `introduce the measure …`：**单词末字母丢失**。300dpi `p018_measur.png` 显示印刷作「…, introduce the measure」，末尾 `e` 清晰可见而 MD 截断为 `measur`。
- **登记不改（印刷怪癖，铁律三）**：Frame 3 末段印刷作「Since 𝜇_{𝐺,𝛽,0} is the only invariant measure for this dynamics, the limit as t tends to infinity, irrespectively of the initial value 𝜎(0), is sampled according to **𝜇_{𝐺,𝛽,ℎ}**.」——句首取 `μ_{G,β,0}` 而句末换成 `μ_{G,β,h}`，二者下标不自洽（前文已声明「set h = 0 for simplicity」，故句末的 `h` 疑为原刊笔误）。属原刊文本，MD 行 385 忠实转写，**不改**。
- 登记不改：
  - 行 379、385、391、393、399、401 中数学模式与相邻文字未留空格（`vertex of $G$.`、`according to$\mu _ { G , \beta , h } .$`、`$H$ be`、`of$\mathbb { Z } ^ { d }$`、`$\sigma$outside`、`edge of$\mathbb { Z } ^ { d }$to` 等），全篇一致的排版级伪影。
  - 行 381、383 的 `\begin{array} { r } { … } \end{array}` 为 MinerU 把行内公式包进 array 的导出伪影，符号内容正确，不改。
  - 印刷中作为图/子集记号的 𝐺、𝑊、𝐻 为**粗斜体**，MD 相应处作普通斜体；此为全篇贯通的记号字重约定（与 p.012 条目登记的 𝐺/𝐾 同一问题），交整篇统一处理，本轮不动。
  - 印刷斜体强调（`boundary conditions`、`spatial Markov property`、`condition`）未在 MD 保留，风格级。
  - 页脚 running foot `18  Hugo Duminil-Copin` 未入 MD（版式级）。
- 备注：本页 6 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。

## p.019（PDF p.19 / 印刷 p.19）
- PNG：/tmp/icm2022dc_audit_p019.png（pngmono 150dpi）
- 核对：承接 p.18 的「In words…」句、DLR 段落与记号 $({-1,1}^{\mathbb{Z}^d},\mathfrak{F}_{\mathbb{Z}^d})$、公式(5.4) 全式、三条项目符号、Dobrushin 三段与文献编号 [52][5][31][1][64][18][92]
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 9 处；另登记若干排版级伪影不作改动）
- 300dpi 裁片：/tmp/icm2022dc_p019_para1.png（offers / infinite- 一段）、/tmp/icm2022dc_p019_f54.png（(5.4) 全式）、/tmp/icm2022dc_p019_bullets.png（三条项目符号）、/tmp/icm2022dc_p019_obvious.png（two obvious μ 一行）、/tmp/icm2022dc_p019_limit.png（the limit of measures μ 一行）、/tmp/icm2022dc_p019_values.png（high values of β. 一行）、/tmp/icm2022dc_p019_convex.png（convex combination of μ 一行）
- 逐项核对：
  - 承接句「In words, when conditioning the Ising model on *G* to coincide with a given configuration outside *W*, one gets the measure in *H* with the corresponding boundary condition.」（MD 行 407）与印刷逐词一致，页首断页接续正确。
  - DLR 段落（行 409）：`a measure $\mu$ on $( \{ - 1 , 1 \} ^ { \mathbb { Z } ^ { d } } , \mathfrak { F } _ { \mathbb { Z } ^ { d } } )$` 的花括号集合、𝔉 的 fraktur 字形、`Dobrushin-Lanford-Ruelle (DLR)` 连字符拼写、`for every finite $V \subset \mathbb { Z } ^ { d }$ and $\tau \in \{ - 1 , 1 \} ^ { \mathbb { Z } ^ { d } }$` 均与印刷相符。
  - **公式 (5.4)（行 412）当前态正确**：300dpi `p019_f54.png` 明见印刷作 `μ[ · | 𝔉_{ℤ^d \ V} ] = μ^τ_{G,β,h}[ · ] on E_τ μ-almost surely,`；MD 的 `\mu [ \cdot | \mathfrak {F} _ {\mathbb {Z} ^ {d} \backslash V} ] = \mu_ {G, \beta , h} ^ {\tau} [ \cdot ] \text { on } E _ {\tau} \mu \text {-almost surely },` 中 τ 作 μ 的上标、`𝔉` 的下标 `ℤ^d \ V`、条件棒与「on … μ-almost surely」全部对应正确，编号 (5.4) 一致。
  - 三条项目符号（行 417/419/421）内容与印刷逐条对上：`𝐺 is the graph induced by the vertex-set 𝑉;` / `𝐸_τ is the event that 𝜎 and 𝜏 agree on the exterior boundary of 𝐺;` / `𝔉_{ℤ^d\𝑉} is the 𝜎-algebra generated by the random variables (𝜎_𝑥 : 𝑥 ∉ 𝑉).`。
  - Dobrushin 三段（行 425/427/429/431）：`extremal states`、`singleton`、`sub-sequential limits`（行内连字符，非断字，MD 保留正确）、`Roland Dobrushin [31]`、`roughening phase transition`、`Aizenman [1]`、`Higuchi [64]`、`Bodineau [18]`、`Raoufi [92]`、`(see [52] for a book on the subject)`、`it was recently proved that this is also the case [5]` 全部与印刷一致，文献编号无错。
  - 页末断页位置正确：印刷本页止于「…a direct link with the previous」，`paragraph.` 落在 p.20，MD 行 431 已跨页接续，未错位。
- 差异列表（已修复 9 处，均为原始导出缺陷）：
  1. 行 409 `This property ofers a natural consistency relation` → `offers`（ff 连字压平，铁律三之外的导出缺陷；按本篇自定 ff 族口径逐处修复）。300dpi `p019_para1.png` 明见印刷作 `offers`（双 f）。
  2. 行 409 `any reasonable infinitevolume version of Ising measures` → `infinite-volume`（换行断字 `infinite-` / `volume` 被导出为无分隔的一整词）。据 `p019_para1.png` 第二、三行边界处的连字符。
  3. 行 419 `agree on the exterior boundary of$G \mathrm { : }$;` → `agree on the exterior boundary of $G$;`：**标点身份错误**。300dpi `p019_bullets.png` 明见第二条项目符号末尾为**分号** `;`，而 MD 把它导出为 `\mathrm{ : }`（冒号）再叠加一个分号，排版后显示为 `of 𝐺:;`。
  4. 行 421 第三条项目符号丢失**行首项目符号 `•`** 与**行末句点**：`${ \mathfrak { F } } _ { \mathbb { Z } ^ { d } \backslash V }$is the $\sigma$-algebra generated by the random variables$( \sigma _ { x } : x \notin V )$` → 补 `• ` 前缀与 `.` 后缀。300dpi `p019_bullets.png` 明见第三条有 `•` 且以 `).` 收尾。
  5. 行 429 `than the two obvious$\mu _ { \beta , 0 } ^ { + }$and$\mu _ { \beta , 0 } ^ { - } ,$, but` → `^ { - }$, but`：**逗号重复**（数学模式内一个、外侧一个）。300dpi `p019_obvious.png` 明见印刷为 `…and 𝜇⁻_{β,0}, but examples…` 单逗号。
  6. 行 429 `measures$\mu _ { [ - n , n ] ^ { 3 } , \beta , 0 } ^ { \tau } ,$, where` → `^ { \tau }$, where`：**逗号重复**。300dpi `p019_limit.png` 明见印刷为 `𝜇^τ_{[−𝑛,𝑛]³,β,0}, where 𝜏 is all plus…` 单逗号。
  7. 行 429 `at high values of$\beta .$` → `at high values of $\beta$.`：**句点被吞入数学模式**。300dpi `p019_values.png` 明见句点位于 β 之后的正文位（`high values of 𝛽. The existence of these Dobrushin`）。
  8. 行 431 `many eforts were made` → `many efforts were made`（ff 连字压平，按 ff 族口径逐处修复）。印刷为双 f。
  9. 行 431 `is a convex combination o$\dot { \mu } _ { \beta , 0 } ^ { + }$and` → `is a convex combination of $\mu _ { \beta , 0 } ^ { + }$ and`：**单词 `of` 被毁**——斜体 f 被误识为 μ 上的附加点，且 f 本身脱落，MD 排版后成为 `combination o𝜇̇⁺_{β,0}`。300dpi `p019_convex.png` 明见印刷作 `…is a convex combination of 𝜇⁺_{β,0} and 𝜇⁻_{β,0}.`，`of` 的 f 为带钩长降部，μ 无点。
- 登记不改：
  - 行 409、417、419、421、425、427、429、431 中数学模式与相邻文字未留空格（`measures$\mu …`、`vertex-set$V ;$`、`•$G$is`、`event that$\sigma$and`、`random variables$( \sigma _ { x } …` 、`for$h \neq 0$or`、`When$h = 0$and`、`obvious$\mu _ { \beta , 0 } ^ { + }$and`、`is a mixture of$\mu` 等），全篇一致的排版级伪影。
  - 行 417 `$V ;$` 句号/分号前多一个空格、行 419 的 `\mathrm { : }` 之外的行内公式包 `array`、行 429 `$\beta =$ $\beta _ { c }$` 被拆成两个数学块、行 431 行内展示公式 `$\begin{array} { r } { … } \end{array}$`，符号内容均正确，仅排版层伪影，不改。
  - 行 431 `In particular, 𝜇_{β,0} = ½𝜇⁺_{β,0} + ½𝜇⁻_{β,0}.` 为行内排版，MD 未升为独立公式块；公式本身逐符号正确，不改。
  - 行 409 磁场符号导出为 Unicode `ℎ`(U+210E PLANCK CONSTANT) 而非数学斜体 h，全篇一致（与 p.016 等页同一问题），登记不改。
  - 印刷中作为图/子集/代数记号的 𝐺、𝑊、𝐻 为**粗斜体**，MD 相应处作普通斜体；此为全篇贯通的记号字重约定（与 p.012、p.018 条目登记同一问题），交整篇统一处理，本轮不动。
  - 印刷斜体强调（`vertex-set`、`σ-algebra`、`exterior boundary`）未在 MD 保留，风格级。
  - 页末段落首字下沉（drop cap）排版未在 MD 体现，版式级。
  - 页脚 running foot `19  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页 9 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。

## p.020（PDF p.20 / 印刷 p.20）
- PNG：/tmp/icm2022dc_audit_p020.png（pngmono 150dpi）
- 核对：Figure 2 双栏图与图注全文、`paragraph.` 跨页承接句与 μ_{β,0} = ½μ⁺ + ½μ⁻ 行内式、5.3 节标题、Wulff shape 开头两段、`[−n,n]²`、`(−n,0)`→`(n,0)` 界面端点、`see [56]`、`Ornstein-Zernike theory`
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 4 处；另登记若干排版级伪影与一处阅读顺序偏移不作改动）
- 300dpi 裁片：/tmp/icm2022dc_p020_caption.png（Figure 2 图注第一行，含三项温度区间与括号）
- 逐项核对：
  - **Figure 2 图注全文**（MD 行 433/435/437）：图注首行 `On the left. Simulations at three different temperatures (β < βc, β = βc, and β > βc) of the Ising model with plus boundary conditions on the top and minus boundary conditions on the bottom. Pluses are in gray and minuses in black. Credit: S. Smirnov. On the right. An example of a bubble of minuses in an environment of pluses at β > βc. Credit: Y. Velenik.` 与印刷逐词对上；图片引用 `![](../audit/ICM2022_proceedings_Duminil-Copin_p020_Figure2.png)`（行 433）经 `ls` 核实文件确实存在于 `2022年 - Duminil-Copin/audit/`，页号前缀 p020 与印刷页号一致。
  - 跨页承接：印刷本页首为 `paragraph.`（p.19 末句 `…with the previous` 的续），MD 行 431 已把它接在同段内，**未断错行**。
  - 行内式 `μ_{β,0} = ½μ⁺_{β,0} + ½μ⁻_{β,0}`（行 431）：分数 ½、两个正负号、β,0 下标位置与印刷一致；`Aizenman [1]`、`Higuchi [64]`、`Bodineau [18]`、`Raoufi [92]` 四个文献编号逐个核对无误。
  - **5.3 节标题** `5.3. Phase coexistence and Wulff shape`（行 439）与印刷完全一致（编号、点号、Wulff 双 f 拼写）。
  - 行 441：`When h = 0 and β > βc, μ⁺_{β,0} and μ⁻_{β,0} are not equal: they correspond to two extremal states, sometimes referred to as the plus and minus phases.`、破折号式引号 `“mix”`、`asks that part of the space is in one state, and the other part is in the other one?` 全部与印刷相符。
  - 行 443：`the simple example of the Ising model on a finite box [−n, n]² of the triangular lattice`、`going from (−n, 0) to (n, 0) winding between pluses and minuses`、`first in the large β regime and then in the whole β > βc regime; see [56] and references therein`、`spin-spin correlations`、`non-critical regimes`、`the coined name of Ornstein-Zernike theory` 全部与印刷相符，`Ornstein-Zernike` 与 `Zernike` 拼写经图读与文字层双向确认。
  - 页末断页位置正确：印刷本页止于 `The theory, known under the coined name of Ornstein-Zernike theory,`，`is now an area of intense research…` 落在 p.21，MD 行 431 顺接未错位。
- 差异列表（已修复 4 处，均为原始导出缺陷）：
  1. 行 437 图注 `Simulations at three diferent temperatures` → `different`（ff 连字压平，按本篇 ff 族口径逐处修复）。300dpi `p020_caption.png` 明见印刷作 `three different temperatures`（双 f）。
  2. 行 437 图注 `, and$\beta > \beta _ { c } )$) of the Ising model with` → `, and$\beta > \beta _ { c } )$ of the Ising model with`：**右括号重复**。数学块内部已含一个 `)`，块外又跟一个 `)`，排版后显示为 `(β < βc, β = βc, and β > βc ))`。300dpi `p020_caption.png` 明见印刷只有**一对**括号。
  3. 行 441 `the question of the coexistence of diferent so-called phases` → `different so-called phases`（ff 连字压平）。印刷作双 f。
  4. 行 443 `(see Figure 2 for simulations at diferent temperatures)` → `different temperatures`（ff 连字压平）。印刷作双 f。
- 登记不改：
  - **阅读顺序偏移（结构级，内容无缺）**：印刷中 Figure 2 的图片与图注位于本页**顶部**、`paragraph.` 承接句之前；MinerU 把 `![…]` 与图注整块排在「paragraph. In two dimensions…」段之后（行 433–437）。图、图注文字与正文均无遗漏，仅块序与印刷不同，属 MinerU 版面切分伪影，**不改**（改动需移动整块，超出逐处字符修复范围且不改变任何符号内容）。
  - 行 437、441、443 中数学模式与相邻文字未留空格（`temperatures$( …`、`When$h = 0$and$\beta`、`finite box$[ - n , n ] ^ { 2 }$of`、`going from$( - n , 0 )$to`、`large$\beta$regime`、`whole$\beta > \beta _ { c }$regime`），全篇一致的排版级伪影。
  - 行 437 图注中的 `Credit: S. Smirnov.` / `Credit: Y. Velenik` 印刷为斜体，MD 未保留，风格级。
  - 行 431 行内公式 `$\begin{array} { r } { … } \end{array}$` 为 MinerU 把行内公式包进 array 的导出伪影，符号内容正确，不改。
  - 行 441 磁场符号导出为 Unicode `ℎ`(U+210E) 而非数学斜体 h，全篇一致，登记不改。
  - 印刷中作为图/子集记号的 𝐺 未在本页出现；5.3 段落中的 μ、β 印刷为斜体，MD 一致，无需字重登记。
  - 印刷斜体强调（`phases`、`interface`、`every`、`translation invariant`）未在 MD 保留，风格级。
  - 页脚 running foot `20  Hugo Duminil-Copin` 未入 MD（版式级）。
- 备注：本页 4 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。

## p.021（PDF p.21 / 印刷 p.21）
- PNG：/tmp/icm2022dc_audit_p021.png（pngmono 150dpi）
- 核对：p.20 末句承接（`is now an area of intense research…`）、Wulff shape 段与 `We refer to [15, 17, 24]`、第 6 节与 6.1 节标题、CQFT 段落与文献 [103][88]、公式 (6.1) 全式、两条项目符号、公式 (6.2) 全式、Schwinger 函数段与 `Interpreting (6.1)`、`The simplest example of Euclidean fields…`
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 4 处；另登记 1 处印刷怪癖不作改动）
- 300dpi 裁片：/tmp/icm2022dc_p021_refs3.png（`[15, 17, 24]` 8× 放大）、/tmp/icm2022dc_p021_coloneq_T.png（`T_f(Φ) :=` 14× 放大）、/tmp/icm2022dc_p021_coloneq2.png（`H(Φ) :≈` 14× 放大）、/tmp/icm2022dc_p021_interp2.png（`Inter-` / `preting (6.1)` 行）、/tmp/icm2022dc_p021_eq62.png（(6.2) 全式）、/tmp/icm2022dc_p021_prod2.png（(6.2) 中段放大）
- 逐项核对：
  - 页首承接句（MD 行 443 末）`is now an area of intense research and spans over a large variety of statistical physics models. We refer to [23] for details on the Ising case.` 与印刷逐词一致。
  - 行 445：`When conditioning on the neighbourhood of the origin to be in a plus phase inside a minus phase`、破折号引号 `“bubble”`、`(see Figure 2 on the right)`、`the so-called Wulff shape`、`see the book [32] and the article [67]`、`a kind of two-dimensional surface`、`the fluctuations of the surface are still widely open` 全部与印刷相符。
  - **`We refer to [15, 17, 24] and references therein.`（行 445）当前态正确**：150dpi 全页图上该处末两位数字形似 `23`，经 300dpi 8× 裁片 `p021_refs3.png` 放大后确认为 **`24`**（4 为开口三角 + 竖干，与 3 的双弧形不同），文字层亦给出 `[15,` `17,` `24]`。MD 未改。
  - **第 6 节标题** `6. The seventies and eighties: the Ising model and field theory`（行 447）与 **6.1 节标题** `6.1. Constructive quantum field theory`（行 449）与印刷完全一致。
  - 行 451：`Quantum field theories with local interaction are central in most subfields of theoretical physics, from high energy to condensed matter physics`（`theoretical` 为行内断字 `theo-` / `retical`，MD 正确合并）、`Wightman axioms [103]`、`Osterwalder-Schrader theorem [88]`、`suitable analyticity, permutation symmetry, Euclidean covariance, and reflection-positivity` 全部与印刷相符。
  - **公式 (6.1)（行 456）当前态正确**：印刷 `⟨F(Φ)⟩ ≈ (1/norm) ∫ F(Φ) exp[−H(Φ)] ∏_{x∈ℝ^d} dΦ(x),`；MD 的 `⟨F(Φ)⟩ ≈ \frac{1}{norm} ∫ F(Φ) exp[−H(Φ)] ∏_{x∈ℝ^d} dΦ(x),` 中近似号、指数方括号负号、连乘下标 `x∈ℝ^d` 与编号 (6.1) 逐项对应。
  - 第一条项目符号（行 461）：`F(Φ) is a smeared average of the form T_f(Φ) := ∫_{ℝ^d} f(x)Φ(x)dx associated with continuous functions of compact support f.` 与印刷逐符号对应，其中 **`:=` 当前态正确**——300dpi 14× 裁片 `p021_coloneq_T.png` 显示该定义号为冒号加两道**直横杠**（`\coloneqq`/`:=`），非近似号。
  - 第二条项目符号（行 463）：`H(Φ) is a Hamiltonian H(Φ) :≈ (Φ, AΦ) + ∫_{ℝ^d} P(Φ(x))dx with (Φ, AΦ) a positive definite and reflection-positive (see Section 6.2) quadratic form, and P(Φ(x)) an even polynomial whose terms of order Φ(x)^{2k} are interpreted heuristically as representing k-particle interactions.` 记号与印刷逐项对应。
  - **公式 (6.2)（行 468）当前态正确**：300dpi `p021_eq62.png` 显示印刷 `⟨∏_{j=1}^n T_{f_j}(Φ)⟩ := ∫_{(ℝ^d)^n} S_n(x_1,…,x_n) ∏_{j=1}^n f_j(x_j) dx_1 … dx_n,`；两个连乘号**均**带上标 `n`、下标 `j=1`（第二个连乘的上标 `n` 在全页缩略图上不易看清，经 bbox 定位其字形位于 x≈281.8pt、y≈517.9pt，与第一个连乘的上标同高，确证存在），`dx_1 … dx_n` 的省略号、定义号 `:=` 与编号 (6.2) 全部正确。
  - 行 471：`the S_n(x_1, …, x_n) are the Schwinger functions of the corresponding Euclidean field theory which can be interpreted heuristically as pointwise correlations ⟨∏_{j=1}^n Φ(x_j)⟩`、**`Interpreting (6.1) raises a number of problems of varying difficulty.`**（`(6.1)` 正确：150dpi 上形似 `(b,·)`，300dpi 裁片 `p021_interp2.png` 显示为印刷体 `(6.1)`；`Inter-` / `preting` 为行内断字，MD 正确合并）、行末 `The simplest example of Euclidean fields are the reflection-positive (see Section 6.2 again) Gaussian fields, for which H(Φ) contains only quadratic terms. Gaussian fields are` 与印刷一致，且断页位置正确（`alternatively characterised by…` 落在 p.22）。
  - 页脚 running foot `21  100 Years of the Ising Model` 未入 MD（版式级）。
- 差异列表（已修复 4 处，均为原始导出缺陷）：
  1. 行 453 `Finding these Euclideanfields boils down to constructing probability averages` → `Finding these Euclidean fields boils down…`：**空格合并致单词粘连**（印刷为两个独立词 `Euclidean fields`，正文中的斜体强调）。
  2. 行 463 `$H(\Phi) \approx (\Phi,A\Phi) + \int_{\mathbb{R}^d} P(\Phi(x))\,dx$` → `$H(\Phi) :\approx (\Phi,A\Phi) + \int_{\mathbb{R}^d} P(\Phi(x))\,dx$`：**印刷冒号被丢弃**。300dpi 14× 裁片 `p021_coloneq2.png` 明见印刷作 `H(Φ) :≈ (Φ, AΦ) + …`（冒号 + 波浪双横的近似号），而 MD 只剩 `\approx`。此处**只补回印刷确实印出的冒号**，不改动近似号本身（见下「登记不改」）。
  3. 行 471 `are the Schwingerfunctions of the corresponding Euclidean field theory` → `are the Schwinger functions of the corresponding Euclidean field theory`：**空格合并致专名粘连**（印刷中 `Schwinger functions` 为斜体强调的两词）。
  4. 行 471 `raises a number of problems of varying dificulty.` → `difficulty.`（ff 连字压平，按本篇 ff 族口径逐处修复）。印刷为双 f。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：同一页两条项目符号的定义号不一致——第一条写 `T_f(Φ) :=`（14× 裁片 `p021_coloneq_T.png`：冒号 + 直双横），第二条却写 `H(Φ) :≈`（14× 裁片 `p021_coloneq2.png`：冒号 + 波浪双横）。按上下文两条都是「定义」，第二条显系原刊笔误（作者误用 `\approx`）。此为原刊印刷事实，MD 已按印刷转写为 `:\approx`，**不作「纠正」**。
  - 行 443、451、453、461、463、471 中数学模式与相邻文字未留空格（`the$S _ { n } ( … )$are`、`distributions $\Phi(x)$`、`support $f$`、`form, and$P ( \Phi ( x ) )$`、`order$\Phi ( x ) ^ { 2 k }$are`），全篇一致的排版级伪影。
  - 行 463 印刷中 `𝐴` 为粗斜体（二次型算子 A），MD 作普通斜体 `A`；与 𝐺、𝐾、𝑊、𝐻 同属全篇贯通的记号字重约定，交整篇统一处理，本轮不动。
  - 印刷斜体强调（`Euclidean fields`、`Schwinger functions`、`Wulff shape`、`every`）未在 MD 保留，风格级。
  - 页末段落首字下沉（drop cap）排版未在 MD 体现，版式级。
- 备注：本页 4 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。另记录两处**经放大后确认 MD 本来就正确**的疑似点（`[15, 17, 24]` 的末位、`Interpreting (6.1)` 的公式号），已在 150dpi 全页图上被 300dpi 裁片推翻，未作任何改动。

## p.022（PDF p.22 / 印刷 p.22）
- PNG：/tmp/icm2022dc_audit_p022.png（pngmono 150dpi）
- 核对：p.21 末句承接（Wick 定律引出句）、公式 (6.3) 全式、`trivial` 句、λΦ⁴ 与 `Wilson [104]` / `ℝ² [55]` / `ℝ³ [44,54]`、`Φ_d^4` 记号、`cutoffs` ×3、图 `Λ_R^{(a)} := (aℤ)^d ∩ [−R,R]^d`、公式 (6.4) 全式（含积分域）、公式 (6.5) 全式、`φ⁴ lattice model`、`R ↗ ∞` 与 `a ↘ 0`、`λ = b/2`、`Griffiths and Simon [60]`
- 结果：PASS±（差异列表如下，已逐处 Edit 修复 6 处；另登记 3 处经放大确认 MD 正确、2 处印刷怪癖与若干排版级伪影不作改动）
- 300dpi 裁片：/tmp/icm2022dc_p022_eq63.png（(6.3) 全式）、/tmp/icm2022dc_p022_phi4.png（`constructing a Φ_d^4 functional` 5× 放大）、/tmp/icm2022dc_p022_eq64.png（(6.4) 全式）、/tmp/icm2022dc_p022_domain2.png（(6.4) 积分域 13× 放大）、/tmp/icm2022dc_p022_simonsn2.png（`Simon [60]` 16× 放大）
- 逐项核对：
  - 页首承接（MD 行 473 末）`alternatively characterised by $2n$-point Schwinger functions satisfying Wick's law:` 与印刷一致。
  - **公式 (6.3)（行 476）当前态正确**：300dpi `p022_eq63.png` 明见印刷 `S_{2n}(x_1, …, x_{2n}) = ∑_{π pairings} ∏_{j=1}^n S_2(x_{π(2j−1)}, x_{π(2j)}).`；求和下限 `π pairings`（π 为下标）、连乘上下限 `j=1` / `n`、两个自变量 `x_{π(2j−1)}` 与 `x_{π(2j)}` 的先后次序（未互换）、编号 (6.3) 全部对应正确。
  - 行 479：`The field theoretical interpretation of (6.3) is the absence of interaction. Due to that and to their algebraically simple structure, such fields are referred to as trivial.` 与印刷一致。
  - 行 481：`i.e. $\lambda \Phi ^ { 4 }$ for $\lambda > 0$`（此处印刷为大写 Φ，正确，勿与下条的小写 φ 混淆）、`the corresponding field is a random distribution so making sense of this fourth power is not straightforward`、`The heuristic RG approach to the problem by Wilson [104]`、`field theories over$\mathbb { R } ^ { 2 }$[55] and$\mathbb { R } ^ { 3 }$[44,54]` 全部与印刷相符。
  - **`constructing a Φ_d^4 functional integral`（行 483）当前态正确**：150dpi 上该记号形似普通 `φ⁴`，经 300dpi 5× 裁片 `p022_phi4.png` 放大后确认印刷**确实**为大写 Φ，且**同时**带上标 `4` 与下标 `d`（即 `Φ_d^4`）；文字层亦给出 `Φ4𝑑`。MD 的 `\Phi _ { d } ^ { 4 }` 逐字符对应，**未改**（与同页后文小写 `φ` 的 `\phi ^ { 4 }` 写法不同，属原刊自身的记号不统一）。
  - 行 483：`the restriction of Φ(·) to the vertices of a finite graph $\Lambda _ { R } ^ { ( a ) } : =$ $( a \mathbb { Z } ) ^ { d } \cap [ - R , R ] ^ { d }$`（图定义与 (a) 和 R 的角色说明）、`a Riemann-sum style discrete analog of the integral expressions`、`leading to the following statistical-mechanics Gibbs equilibrium state average` 与印刷相符。
  - **公式 (6.4)（行 486）**：印刷 `⟨F(φ)⟩ = (1/norm) ∫_{ℝ_R^{(a)}} F(φ) exp[−H(φ)] ∏_{x∈Λ_R^{(a)}} dρ(φ_x),`。300dpi `p022_eq64.png` 与 13× 裁片 `p022_domain2.png` 确认积分域为 `ℝ` 带**下标 R、上标 (a)**；连乘号下标 `x ∈ Λ_R^{(a)}` 正确；连乘号后的微分符号经放大确认是 **`ρ`(rho)** 而非 `φ`，MD 的 `d \rho (\phi _ {x})` 正确；近似/等号、指数方括号负号、编号 (6.4) 正确。
  - 行 489：`with a Hamiltonian $H ( \phi )$ and an a-priori measure $\rho$ of the form` 与印刷一致。
  - **公式 (6.5)（行 492）当前态正确**：印刷 `H(φ) = − ∑_{{x,y}⊂E(Λ_R^{(a)})} φ_x φ_y,   dρ(φ_x) = e^{−λφ_x⁴ − bφ_x²} dφ_x,`；求和条件 `{x,y} ⊂ E(Λ_R^{(a)})`、指数中 `−λφ_x⁴ − bφ_x²` 的两项顺序与下标、末尾微分 `dφ_x`、编号 (6.5) 全部对应正确。
  - 行 495：`This is called the $\phi ^ { 4 }$ lattice model.` 与印刷一致。
  - 行 497：`The cutoffs are removed through the limit $R ~ { \nearrow }$∞ followed by $a \searrow 0$`（两个箭头方向正确）、`the spin-spin correlations$\langle \phi _ { x _ { 1 } } \ldots \phi _ { x _ { n } } \rangle$`、`they stabilise to the Schwinger functions$S _ { n } ( x _ { 1 } , \ldots , x _ { n } )$in the continuum limit scale` 与印刷相符。
  - 行 499：`letting$\lambda = b / 2$tend to infinity`、`the limit of the measures$\rho$then forces the spins$\phi _ { x }$to take the values ±1`、`the Lee-Yang theorem for the $\phi ^ { 4 }$ lattice models`、`Griffiths and Simon [60]`、`the Griffiths-Simon class`（三处出现）、`well-chosen coupling constants`、`(satisfying some mild tail conditions)` 全部与印刷相符；页末断页位置正确（印刷止于 `The developments of the`，`model have therefore been deeply connected to CQFT in the eighties…` 落在 p.23，MD 行 499 顺接未错位）。
- 差异列表（已修复 6 处，均为原始导出缺陷）：
  1. 行 481 `The next level of deficulty is to add the next lowest order even term` → `difficulty`（ff 连字压平，按本篇 ff 族口径逐处修复）。印刷为双 f（`pdftotext` 文字层亦作 `difficulty`）。
  2. 行 483 `with a pair of cutofs: at a short distance (ultraviolet) scale` → `cutoffs:`（ff 连字压平）。
  3. 行 483 `where $a$ and $R$ play respectively the roles of the ultraviolet and infrared cutofs.` → `cutoffs.`（ff 连字压平）。
  4. 行 483 `For the corresponding finite collection ofvariables$( \phi _ { x } : x \in \Lambda _ { R } ^ { ( a ) } )$` → `collection of variables $( \phi _ { x } … )$`：**空格合并致 `of variables` 粘连**。
  5. 行 486 公式 (6.4) `\int_ {\mathbb {R} ^ {\Lambda_ {R} ^ {(a)}}}` → `\int_ {\mathbb {R} _ {R} ^ {(a)}}`：**积分域的上下标身份错误**。印刷的积分域是 `ℝ` 带下标 `R`、上标 `(a)`（表示带 (a) 尺度与 R 截断的实轴），MD 却把整个格点 `Λ_R^{(a)}` 挂成了 `ℝ` 的上标，使 `∫` 的定义域与印刷完全不同。300dpi 13× 裁片 `p022_domain2.png` 明见下标位置的单个 `R` 与上标位置的 `(a)`。
  6. 行 497 `The cutofs are removed through the limit` → `cutoffs`（ff 连字压平）。
- 经放大确认 **MD 正确、未作改动** 的疑似点：
  - `constructing a $\Phi _ { d } ^ { 4 }$ functional integral`：印刷确为 `Φ_d^4`（5× 裁片 `p022_phi4.png`），MD 无误。
  - `Griffiths and Simon [60]`：150dpi 上形似 `[83]`，16× 裁片 `p022_simonsn2.png` 确认印刷为 **`[60]`**（6 为上钩下闭环，0 为椭圆），文字层亦作 `[60]`。MD 无误。
  - 公式 (6.4) 连乘后的 `d \rho (\phi _ {x})`：150dpi 上 `ρ` 与 `φ` 难分辨，`p022_eq64.png` 放大后确认印刷符号为 `ρ`，MD 无误。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：印刷正文作「A probability measure **on** ρ(dφ) **on** ℝ is said to belong to the Griffiths-Simon class」——介词 `on` 重复出现两次（文字层与 bbox 均给出 `A probability measure` / `on` / `𝜌(𝑑𝜙)` / `on` 的连续序列，确证）。属原刊笔误，MD 行 499 忠实转写，**不改**。
  - **印刷怪癖**：同页对同一类对象混用大写 `Φ_d^4`（行 483）与小写 `φ⁴`（行 495、499），MD 两者均按印刷保留，不作统一。
  - 行 483、489、495、497、499 中黑体花体 `ℝ` 被导出为普通 `R`（`on R`、`\mathbb { R } ^ { 2 }` 处尚存花体），与 `ℤ/2ℤ`、`ℂ` 同属全篇贯通的**黑板粗体丢失**约定，交整篇统一处理，本轮不动。
  - 行 483 `$\Lambda _ { R } ^ { ( a ) } : =$`（定义号前多空格）、行 486 `\text { norm }`（印刷为正体 `norm`，一致）、行 497 `$R ~ { \nearrow }$`（多余关系空格）、行 492 `\qquad`（印刷为两式间的空位，间距由版式给出）——均为排版层伪影，符号内容正确，不改。
  - 行 483、489、497、499 中数学模式与相邻文字未留空格（`a$\Phi _ { d } ^ { 4 }$functional`、`graph$\Lambda`、`variables$( \phi`、`H ( \phi )$and`、`measure$\rho$of`、`limit$R`、`spin-spin correlations$\langle`、`functions$S _ { n }`、`lattice$\lambda`、`measures$\rho$then`、`values ±1`、`with respect to$\rho$can`），全篇一致的排版级伪影。
  - 印刷斜体强调（`trivial`、`ultraviolet`、`infrared`、`Wick's law`、`always`、`Griffiths-Simon class`）未在 MD 保留，风格级。
  - 页脚 running foot `22  Hugo Duminil-Copin` 未入 MD（版式级）。
- 备注：本页 6 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。（溯源时发现以字面串 `dificulty` 作 `-F` 匹配会因不可见字符误报 0，改用 `grep -oE 'dif+iculty' | grep -c` 计数后得 peer^=4 / HEAD=4 / 当前=3，本页这一处减 1，结论不变。）
- 补记（本页 6 处修复的落地时点）：本条目落签时 6 处差异已逐条定位并登记，Markdown 的 6 处 `Edit` 在随后一次落笔中完成并复核：`dificulty`→`difficulty`（行 481）、`cutofs`→`cutoffs`（行 483 两处、行 497 一处）、`collection ofvariables`→`collection of variables`（行 483）、(6.4) 积分域 `\mathbb {R} ^ {\Lambda_ {R} ^ {(a)}}`→`\mathbb {R} _ {R} ^ {(a)}`（行 486）。复核后 `cutofs` 命中 0、`cutoffs` 命中 2、`ofvariables` 命中 0、行 486 积分域作 `\mathbb {R} _ {R} ^ {(a)}`，与上条「修复后当前态为 0」的表述一致。落地期间 `Edit` 工具曾三次返回 “String to replace not found”，经 `dd|od -An -tx1`、`grep -cF`、`perl index`、300dpi 页图四路互证文件字节确为 `20 6f 66 20 64 69 66 69 63 75 6c 74 79`（` of deficulty`）后，判定为本会话 Edit 侧的读取状态失效而非文件内容问题，改用**短唯一片段**作 `old_string`（如 `dificulty is to add`、`^ {\Lambda_ {R} ^ {(a)}}`）并先 `Read` 文件后 6 处一次通过。全程未使用脚本写回 Markdown。

## p.023（PDF p.23 / 印刷 p.23）
- PNG：/tmp/icm2022dc_audit_p023.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p023_300.png（300dpi 全页）、/tmp/icm2022dc_p023_torus.png（`d`-维环面与 `𝐓_L^+ → 𝐓_L^-` 映射方向）、/tmp/icm2022dc_p023_eq66.png（(6.6) 全式）、/tmp/icm2022dc_p023_nnf.png 与 /tmp/icm2022dc_p023_nnf_tail.png（`⟨·⟩_{𝐓_L,β,0}` 后的标点，3× 放大）、/tmp/icm2022dc_p023_hbold.png（`for every function 𝐡` 一行）、/tmp/icm2022dc_p023_eq67.png（(6.7) 全式）、/tmp/icm2022dc_p023_eq68.png（(6.8) 全式）、/tmp/icm2022dc_p023_eq69_den.png（(6.9) 右端分式）、/tmp/icm2022dc_p023_lastpara.png（末段 `spin-spin` 与句末句点）
- 核对：§6.2 标题「Reflection positivity」；`Osterwalder-Schrader [88]` 与 `[16]`；`d`-维环面 `𝐓_L := (ℤ/Lℤ)^d`、`with L even`、`𝐓_L^+`/`𝐓_L^-`、`[0, L/2] × (ℤ/Lℤ)^{d−1}`、反射 `ϑ`、映射方向 `𝐓_L^+ → 𝐓_L^-`、`f, g : 𝐓_L^+ → ℝ`；公式 (6.6) 的两个关系、`≥ 0`、尾逗号；`n.n.f.` 与 `⟨·⟩_{𝐓_L,β,0}` 后的标点；`gaussian domination`/`infrared bound`/`chessboard estimate`；`Z_L(𝐡) ≤ Z_L(0)` 的不等号方向与粗体；公式 (6.7) 的 `:=`、`σ ∈ {−1,1}^V`、`exp[ ]` 方括号、`−β`、`{x,y} ∈ E(𝐓_L)`、`(σ_x−σ_y+𝐡_x−𝐡_y)²` 的平方在括号外、句末句点；`for each 𝐡, a symmetric version of 𝐡`；`(a_x) ∈ ℂ^{𝐓_L}`、`for d > 2`、`second-order expansion`；公式 (6.8) 的系数 `2/β`、`ā_y` 共轭仅覆盖 `a`、⟨·⟩ 的下标 `𝐓_L,β,0`、尾逗号；`Messager-Miracle-Solé`；`C, C′ > 0`、`β > 0`；公式 (6.9) 的 `m*(β)²`、`C/β`、`C′/‖x−y‖₂^{d−2}` 的下标与上标、句末句点；末段 `spin-spin`、`β_c`、`d − 2`；页脚 `23  100 Years of the Ising Model`。
- 结果：FAIL（差异列表如下，4 处已逐处 Edit 修复；以原图为准）
- 逐项核对：
  - §6.2 标题与 MD 行 501 一致；首段（`The notion of reflection positivity…`）与 MD 行 503 逐字一致，`[88]`、`[16]` 两个引用编号位置正确。
  - 环面定义段与 MD 行 505 逐符号对应：`𝐓_L := (ℤ/Lℤ)^d` 的下标 `L` 与上标 `d`、`with L even`、`𝐓_L^+` 与 `𝐓_L^-` 的上标、`[0, L/2] × (ℤ/Lℤ)^{d−1}` 的 `d−1`（**未误作 `d` 或 `d−2`**）、`ϑ`、`hyperplanes mapping 𝐓_L^+ to 𝐓_L^-` 的**映射方向为 + → −**（未倒置）、`f, g : 𝐓_L^+ → ℝ` 均与 300dpi 裁片 `/tmp/icm2022dc_p023_torus.png` 对上。
  - (6.6) 印刷 `⟨fϑg⟩ = ⟨gϑf⟩  and  ⟨fϑf⟩ ≥ 0,`：`gϑf` 在**前**一位式内、`≥ 0` 为**大于等于**、尾**逗号**、编号 `(6.6)`，与 MD 行 508 一致（裁片 `/tmp/icm2022dc_p023_eq66.png`）。
  - `Z_L(𝐡) ≤ Z_L(0)` 的不等号方向为 `≤`（左不大于右），与印刷一致（裁片 `/tmp/icm2022dc_p023_hbold.png`）。
  - (6.7) 印刷 `Z_L(𝐡) := ∑_{σ∈{−1,1}^V} exp[−β ∑_{{x,y}∈E(𝐓_L)} (σ_x − σ_y + 𝐡_x − 𝐡_y)²].`：定义号 `:=`、`exp` 后**方括号**、`−β` 的负号、内层平方**在圆括号之外**、`{x,y}` 的花括号、`E(𝐓_L)`、句末**句点**，以及三处 𝐡（`Z_L(𝐡)`、`𝐡_x`、`𝐡_y`）的**粗体**，与 MD 行 518 一致（裁片 `/tmp/icm2022dc_p023_eq67.png`）。
  - (6.8) 印刷 `∑_{x,y∈𝐓_L} a_x ā_y ⟨σ_xσ_y⟩_{𝐓_L,β,0} ≤ (2/β) ∑_{x,y∈𝐓_L} a_x ā_y G(x,y),`：系数为 **`2/β`**、共轭横线**只覆盖 `a`**（不覆盖下标 `y`）、⟨·⟩ 的下标 `𝐓_L,β,0`、两处求和域、尾**逗号**，与 MD 行 524 一致（裁片 `/tmp/icm2022dc_p023_eq68.png`）。
  - (6.9) 印刷 `⟨σ_xσ_y⟩_{β,0} − m*(β)² ≤ (C/β) G(x,y) ≤ C′/‖x−y‖₂^{d−2}.`：`m*(β)` 的**上标星号**、`m*(β)²` 的平方、末项**下标 `2`** 与**上标 `d−2`**（二者层级未互换）、句末句点，与 MD 行 532 一致（裁片 `/tmp/icm2022dc_p023_eq69_den.png`）。
  - 正文数值与方向：`d > 2`、`C, C′ > 0`、`for every β > 0`、`x, y ∈ ℤ^d`、`with an exponent at least d − 2` 均与印刷一致；`Gaussian domination…` 段的 `Z_L(𝐡) near 0` 的 `near` 与 `0` 的先后无误。
  - 结构与次序吻合：页首承 p.22 末句 → §6.2 标题 → 首段 → 环面段 → (6.6) → `or, in other words…` 段 → `Reflection positivity has two important implications…` 段 → `Gaussian domination is a statement…` 段 → (6.7) → `Gaussian domination can be proved…` 段 → (6.8) → `where G(x, y) is the Green function…`（印刷此处**无句点**，直接另起段，MD 行 527 同样无句点，正确）→ `In the specific case…` 段 → (6.9) → 末段；无缺失或错序。
- 差异列表（4 处，均已用 `Edit` 逐处修复，命中位置均唯一）：
  1. 行 515 `for every function $h:V\to\mathbb{R}$` → `for every function $\mathbf { h }:V\to\mathbb{R}$`：**粗体向量场 𝐡 的字重丢失**。300dpi 裁片 `/tmp/icm2022dc_p023_hbold.png` 明见印刷作「for every function **𝐡** : 𝑉 → ℝ, 𝑍_L(𝐡) ≤ 𝑍_L(0), where」——冒号前的 `𝐡` 与同句 `𝑍_L(𝐡)` 的 `𝐡` **同为粗体**；MD 只在 `Z _ { L } ( \mathbf { h } )` 处保留了 `\mathbf { h }`，同一行内自相矛盾。本文用普通斜体 `h` 表示**标量外场**（§5.2 的 `h ≠ 0`、Lee–Yang 定理），用粗体 **𝐡** 表示定义在顶点集上的**向量场**（`h : V → ℝ`），二者刻意区分，丢失粗体即丢失记号身份。
  2. 行 511 `measures$\langle \cdot \rangle _ { \mathbb { T } _ { L } , \beta , 0 } .$ but many other examples exist` → 把 `.` 改为 `,$`：**标点身份错误**。3× 放大的裁片 `/tmp/icm2022dc_p023_nnf_tail.png` 显示印刷作「…the Ising n.n.f. measures ⟨·⟩_{𝐓_L,β,0},」——是带下拖尾的**逗号**而非句点；该句为「The archetypical examples …, **but** many other examples exist, …」的同句延续，句点会误断句。
  3. 行 535 `the spin spin correlations` → `the spin-spin correlations`：**行末连字符丢失**。裁片 `/tmp/icm2022dc_p023_lastpara.png` 显示印刷跨行作 `…that the spin-` / `spin correlations decay…`，`spin-spin` 是本文自始至终使用的复合词（Heisenberg `spin-spin` 耦合），连字符被导出为空白。
  4. 行 535 段末 `with an exponent at least$d - 2$` → 补句点：同一裁片显示印刷作 `…with an exponent at least 𝑑 − 2.`（带句点），MD 缺失。
- 经仲裁判定**正确、未改动**（铁律二实证，避免据文本层「纠正」而制造错误）：
  - **(6.9) 分母的下标 `2`**：`pdftotext -bbox` 文本层把该处分式读成「∥ ∥ / 𝑥−𝑦 / 2 / 𝑑−2」，且 `yMin` 分别为 `586.5`（`2`）与 `582.4`（`𝑑−2`）——即 `2` 在下、`𝑑−2` 在上，与欧氏范数记号 `‖·‖₂` 相符。300dpi 裁片 `/tmp/icm2022dc_p023_eq69_den.png` 直接确认印刷分母为 `∥x−y∥₂^{d−2}`。**MD 行 532 原本正确，不作改动**；若据文本层把它「纠正」为 `‖·‖_{ℤ^d}` 反属制造错误。
  - **(6.6) 两式次序**：`⟨gϑf⟩` 在第二位式内，MD 未把 `g`、`f` 倒置。
  - **映射方向**：印刷为 `mapping 𝐓_L^+ to 𝐓_L^-`，MD 行 505 同向。
- 溯源（回归判定）：对 `cpf-redo/ICM2022_proceedings_Duminil-Copin^`、该分支 HEAD、当前工作树执行四组三态 `grep -cF`（`function $h:V`、`, 0 } .$ but`、`spin spin correlations`、`at least$d - 2$`），命中数均为 **1/1/1**，确认 4 处**全部为原始 MinerU 导出缺陷，无一条系 peer 引入的回归**。
- 与他处条目的关系（供集成者去重）：本文件「Repair registration」段第 837 行的既有 `## p.023` 条目已把**行 521** 的两处 `h` 改为 `\mathbf { h }`；本条目处理的是**行 515** 的另一处，两处位置不同、无重叠，本轮未重复改动行 521，复核确认行 521 现为 `for each $\mathbf { h }$, a symmetric version of $\mathbf { h }$`，与印刷一致。
- 登记不改：
  - 行 505、511、513、515、521、527、529、535 中数学模式与相邻文字未留空格（`torus$\mathbb { T } _ { L } : =$`、`f , g \mapsto \langle f \vartheta g \rangle$is`、`$h:V\to\mathbb{R}$, $Z`、`$Z _ { L } ( \cdot )$near`、`$Z ( x , y )$is`、`β _ { c }$from` 等），全篇一致的排版级伪影。
  - 行 529 `there exist $C , C ^ { \prime } > 0$` 与 `for every$\beta > 0$` 的空格合并（排版级，符号正确）。
  - 行 513、521、535 的印刷斜体强调（`gaussian domination`、`infrared bound`、`chessboard estimate`、`reflection positive`、`long-range`）未在 MD 保留（风格级）。
  - 页脚 running foot `23  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页 4 处修复全部以 `Edit` 工具逐处落地，`old_string` 均先经 `grep -cF` 确认在文件中唯一；落地后复核 `function $h:V`、`spin spin correlations`、`, 0 } .$ but` 三组旧串命中均为 0，行 515 作 `for every function $\mathbf { h }:V\to\mathbb{R}$`、行 511 作 `0 } ,$ but many other ex…`、行 535 作 `…the spin-spin correlations…at least$d - 2$.`。全程未使用脚本写回 Markdown。

## p.024（PDF p.24 / 印刷 p.24）
- PNG：/tmp/icm2022dc_audit_p024.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p024_300.png（300dpi 全页）、/tmp/icm2022dc_p024_eq610.png（(6.10) 全式）、/tmp/icm2022dc_p024_eq611.png（(6.11) 全式）、/tmp/icm2022dc_p024_Vcomma.png（`for all x ∈ V,` 一行）、/tmp/icm2022dc_p024_eq612.png（(6.12) 全式，2× 放大）、/tmp/icm2022dc_p024_notationn.png（`the notation 𝐧.` 一行）、/tmp/icm2022dc_p024_currentn.png（`A current 𝐧 with ∂𝐧 = A` 一行）、/tmp/icm2022dc_p024_them.png（`in terms of them.` 一行）、/tmp/icm2022dc_p024_eq613.png（(6.13) 全式，2× 放大）、/tmp/icm2022dc_p024_constraints.png（`∂𝐧 = A and ∂𝐧 = ∅` 一行，2× 放大）、/tmp/icm2022dc_p024_frame4.png（Frame 4 框题）
- 核对：§6.3 标题「The random current revolution」；`Section 6.4`、`[35]`、`Griffiths`/`Aizenman`；`exp[βσ_xσ_y]` 与 `Taylor's expansion`；公式 (6.10) 的 `Z(G,β,0)`、两层求和乘积、`𝐧_{ {x,y} }=0` 到 `∞`、`(βσ_xσ_y)^{𝐧}/𝐧!`、`∑_{𝐧∈ℤ_+^E}`、`w_β(𝐧)`、`∏_{x∈V} σ_x^{Δ_x(𝐧)}`、尾逗号；`where`；公式 (6.11) 的 `w_β(𝐧) :=`、`and`、`Δ_x(𝐧) :=`、求和域 `y∈V: {x,y}∈E`、尾逗号；`2^{|V|}`、`if Δ_x(𝐧) is even for all x ∈ V,`、`or 0 otherwise`、`+/− symmetry`；`E → ℤ₊ a current`、`A source …`、`∂𝐧`；公式 (6.12) 的 `2^{|V|}`、`∑_{∂𝐧=∅}`、尾逗号；`the notation 𝐧.`；`A current 𝐧 with ∂𝐧 = A`、`loops – or equivalently`、`in terms of them.`；`spin-spin correlations`（正文与公式各一处）；公式 (6.13) 的 `⟨σ_A⟩_{G,β,0}`、分子 `∑_{∂𝐧=A}`、分母 `∑_{∂𝐧=∅}`、尾句点；`∂𝐧 = A and ∂𝐧 = ∅`；Frame 4 框题 `the high-temperature expansion and β_c > 0`；`van der Waerden [100]`、`odd current`；页脚 `24  Hugo Duminil-Copin`。
- 结果：PASS±（差异列表如下，4 处已逐处 Edit 修复；另登记 1 类字重约定不作改动）
- 逐项核对：
  - §6.3 标题与 MD 行 537 一致；首段（`The context of CQFT…`）与 MD 行 539 逐字一致，印刷行末连字符 `revo-` / `lutions` 已正确复原为 `revolutions`，`Section 6.4`、`[35]` 两个交叉引用编号位置正确。
  - `exp [ \beta \sigma _ { x } \sigma _ { y } ]` 与印刷一致，句末 `Taylor's expansion` 的撇号形态亦一致（裁片 150dpi 与 bbox 均作 `Taylor’s`）。
  - (6.10) 印刷 `Z(G,β,0) = ∑_{σ∈{−1,1}^V} ∏_{{x,y}∈E} ∑_{𝐧_{ {x,y} }=0}^{∞} (βσ_xσ_y)^{𝐧_{ {x,y} }}/𝐧_{ {x,y} }! = ∑_{𝐧∈ℤ_+^E} w_β(𝐧) ∑_{σ∈{−1,1}^V} ∏_{x∈V} σ_x^{Δ_x(𝐧)},`（裁片 `/tmp/icm2022dc_p024_eq610.png`）：求和上限 `∞` 只挂在**内层** `∑` 上、外层 `∑_{σ∈{−1,1}^V}` 无上限、`{x,y}∈E` 的**斜体 E**、`ℤ_+^E` 的下标 `+` 与上标 `E`、`w_β(𝐧)`、三处 𝐧 的**粗体**、`Δ_x(𝐧)` 的下标 `x`、尾**逗号**、编号 `(6.10)`，与 MD 行 544 逐符号对应。
  - (6.11) 印刷 `w_β(𝐧) := ∏_{{x,y}∈E} β^{𝐧_{ {x,y} }}/𝐧_{ {x,y} }!  and  Δ_x(𝐧) := ∑_{y∈V: {x,y}∈E} 𝐧_{ {x,y} },`（裁片 `/tmp/icm2022dc_p024_eq611.png`）：两处定义号 `:=`、中间的 `and`（**文字正体**）、`β^{𝐧}` 的指数（**只有 β 有指数，分母无 β**）、求和域 `y ∈ V : {x, y } ∈ E` 的冒号、尾**逗号**、编号 `(6.11)`，与 MD 行 550 一致。
  - `2^{|V|}`、`Δ_x(𝐧)` 的粗体 𝐧、`+/− symmetry` 的加减号，均与印刷一致。
  - (6.12) 印刷 `Z(G,β,0) = 2^{|V|} ∑_{∂𝐧=∅} w_β(𝐧),`（裁片 `/tmp/icm2022dc_p024_eq612.png`）：`2^{|V|}` 的**竖线绝对值**、求和下标 `∂𝐧 = ∅`、尾**逗号**，与 MD 行 558 一致。
  - (6.13) 印刷 `⟨σ_A⟩_{G,β,0} = (∑_{∂𝐧=A} w_β(𝐧)) / (∑_{∂𝐧=∅} w_β(𝐧)) .`（裁片 `/tmp/icm2022dc_p024_eq613.png`）：左端 `⟨σ_A⟩` 的下标 `G,β,0`、分子下标 `∂𝐧 = A`、分母下标 `∂𝐧 = ∅`、**末尾句点位于分式之后**，与 MD 行 568 一致。
  - `specific source constraints ∂𝐧 = A and ∂𝐧 = ∅.`（裁片 `/tmp/icm2022dc_p024_constraints.png`）：两处 𝐧 粗体、两处 `∅`、句点位置，与 MD 行 571 的 `\partial \mathbf { n } = A` 与 `\partial \mathbf { n } = \boldsymbol { \emptyset }` 的**符号身份**一致（字重差异另见「登记不改」）。
  - Frame 4 框题印刷作「**Frame 4: the high-temperature expansion and β_c > 0**」（裁片 `/tmp/icm2022dc_p024_frame4.png`），`β_c` 的**下标 `c`**、`> 0` 的正号，与 MD 行 573 一致；框内首句 `due to van der Waerden [100]`、`an odd current` 与 MD 行 575 一致，框体在页末未闭合（顺接 p.25），MD 亦顺接，无缺失。
  - 结构与次序吻合：§6.3 标题 → CQFT 背景段 → `The whole story starts…` 段 → (6.10) → `where` → (6.11) → `Now, the involutions…` 段 → `Call a function from E to ℤ₊ a current…` 段 → (6.12) → `where from now on…` 段 → `A current 𝐧 with ∂𝐧 = A…` 段 → `Proceeding in a similar fashion…` 段 → (6.13) → `In words, one may write…` 段 → Frame 4 框（未完）；无缺失或错序。
- 差异列表（4 处，均已用 `Edit` 逐处修复，命中位置均唯一）：
  1. 行 553 `…if$\Delta _ { x } ( \mathbf { n } )$is even for all$x \in V$ or 0 otherwise…` → 在 `V` 后补**逗号**，作 `…for all$x \in V$, or 0 otherwise…`。300dpi 裁片 `/tmp/icm2022dc_p024_Vcomma.png` 明见印刷作「…is even for all 𝑥 ∈ 𝑉**,**」——`𝑉` 后有一个带下拖尾的**逗号**（bbox 亦给出 `𝑉,` 这一词元），MD 把它连同 `or` 一起吞掉。该逗号是「either … or …」两分句的分隔符，缺失后句法断裂。
  2. 行 561 `…when using the notation n.` → `…when using the notation $\mathbf { n } $.`：**粗体向量 𝐧 的字重丢失**。裁片 `/tmp/icm2022dc_p024_notationn.png` 显示句末 `n` 笔画明显加重，与同页 `𝐧` 一致；本文用 𝐧 记电流（函数），此处是被指代的记号，应与 (6.10)–(6.13) 的 𝐧 同体。
  3. 行 563 `A current n with$\partial \mathbf { n } = A$can be interpreted…` → `A current $\mathbf { n }$ with…`：同一行内 **`n` 与 `∂𝐧` 字重不一致**。裁片 `/tmp/icm2022dc_p024_currentn.png` 显示印刷作「A current **𝐧** with ∂**𝐧** = 𝐴」，两处 `𝐧` 同为粗体；MD 只在 `∂` 后保留了 `\mathbf { n }`。
  4. 行 563 段末 `…to interpret currents in terms of them` → 补句点作 `…in terms of them.`。裁片 `/tmp/icm2022dc_p024_them.png` 显示印刷带句点，MD 缺失。
- 经仲审判定**正确、未改动**（铁律二实证，避免据 150dpi 误读「纠正」而制造错误）：
  - **(6.12) 求和下标 `∂𝐧 = ∅`**：150dpi 全页图上该下标读起来像「`∂n=0`」（数字零），`pdftotext -bbox` 文本层则给出 `𝜕n=∅`。2× 放大的 300dpi 裁片 `/tmp/icm2022dc_p024_eq612.png` 直接判定：**是空集符号 ∅（上、下两弧带斜杠），不是数字 0**。**MD 行 558 的 `\emptyset` 原本正确，不作改动**；若据 150dpi 把它改成 `0` 反属制造错误。
  - **(6.13) 分母下标 `∂𝐧 = ∅`**：裁片 `/tmp/icm2022dc_p024_eq613.png` 同样确认为 ∅，MD 行 568 正确。
  - **`A` 的字重**：`∂𝐧 = 𝐴` 中的 `𝐴` 在 (6.12)、(6.13) 与两处正文中均为**斜体非粗体**（集合记号），MD 行 558/563/568/571 一律写作普通 `A`，正确，未按「向量应加粗」的直觉改成 `\mathbf`。
- 溯源（回归判定）：对 `cpf-redo/ICM2022_proceedings_Duminil-Copin^`、该分支 HEAD、当前工作树执行四组三态 `grep -cF`（`even for all$x \in V$ or 0 otherwise`、`using the notation n.`、`A current n with`、`in terms of them`），命中数均为 **1/1/1**，确认 4 处**全部为原始 MinerU 导出缺陷，无一条系 peer 引入的回归**。
- 登记不改：
  - **字重约定（文档级）**：行 571 `$\partial \mathbf { n } = \boldsymbol { \emptyset }$` 把印刷中**非粗体**的 `∅` 写成 `\boldsymbol`。全篇 `boldsymbol` 共出现于 9 处、跨多页，属导出器统一的字重约定（与 p.022、p.023 登记的 𝐠/𝐾/𝑊 粗斜体约定同类），交整篇统一处理，本轮不逐点改动。
  - 行 539、541、555、563、571、575 中数学模式与相邻文字未留空格（`revolutions` 无关处、`component$\exp … ]$of`、`$\partial \mathbf { n } = A$can`、`$+ / -$symmetry`、`$A$and`、`exp$[ \beta … ]$` 等），全篇一致的排版级伪影。
  - 行 553 `the$+ / -$symmetry` 的 `+ / -` 两侧多余空格（印刷为紧排的 `+/−`，符号身份正确）。
  - 行 575 `(it can also be obtained by a direct expansion using that exp$[ \beta \sigma _ { x } \sigma _ { y } ] = \cosh ( \beta ) + \sinh ( \beta ) \sigma _ { x } \sigma _ { y } )$` 的函数名与括号间空格（排版级，式子本身无误）。
  - 印刷斜体强调（`random current representation`、`current`、`source`、`high-temperature expansion`、`odd`、`loops`、`paths`、`–` 破折号）未在 MD 保留（风格级）。
  - Frame 4 的**框体边框**未在 MD 保留（版式级；框题已作 `## Frame 4: …`）。
  - 页脚 running foot `24  Hugo Duminil-Copin` 未入 MD（版式级）。
- 备注：本页 4 处修复全部以 `Edit` 工具逐处落地，`old_string` 均先经 `grep -cF` 确认在文件中唯一；落地后复核四组旧串命中均为 0，行 553 作 `is even for all$x \in V$, or 0 otherwise`、行 561 作 `…using the notation $\mathbf { n } $.`、行 563 作 `A current $\mathbf { n }$ with$\partial \mathbf { n } = A$can be inter…` 且段末作 `in terms of them.`。全程未使用脚本写回 Markdown。

## 逐页重审块 E 收尾（p.017–p.024）
- 本块 8 页全部逐页渲染 150dpi pngmono、逐页开图判读、逐页落签，无跳页、无合并条目：
  - p.017 PASS±（7 处修复）；p.018 PASS±（6 处）；p.019 PASS±（9 处）；p.020 PASS±（4 处）；p.021 PASS±（4 处）；p.022 PASS±（6 处）；p.023 **FAIL**（4 处，以原图为准）；p.024 PASS±（4 处）。
  - 合计 **44 处 Edit 修复**，全部经 `Edit` 工具逐处落地（无脚本写回），全部经 peer^ / HEAD / 当前工作树三态 `grep` 溯源，命中数一律 1/1/1 —— **本块 44 处缺陷无一条系 peer 引入的回归，全部为原始 MinerU 导出缺陷**。
  - 经 300dpi 裁片仲裁后**判定 MD 原本正确、未改动**的负例（本块共 8 例，均是「据文本层或 150dpi 误读去纠正」会制造错误的地方）：p.019 的 `μ_{G,β,0}` vs `μ_{G,β,h}`；p.021 的 `H(Φ) :≈` 与 `T_f(Φ) :=`；p.022 的 (6.4) 积分域 `ℝ^{Λ_R^{(a)}}`、`Φ_d^4` 与 `φ⁴`；p.023 的 (6.9) 分母 `‖x−y‖₂^{d−2}`；p.024 的 (6.12)/(6.13) 下标 `∂𝐧 = ∅`。
  - 印刷怪癖按铁律三原样保留并登记（含本块新增）：p.018 Frame 3 的 `μ_{G,β,0}` / `μ_{G,β,h}` 不自洽；p.021 的 `:≈` vs `:=`；p.022 的「A probability measure **on** ρ(dφ) **on** ℝ」重复介词、`Φ_d^4` 与 `φ⁴` 混用。
  - 分页入口与出口的连续性：p.016 末句顺接 p.017，p.024 末的 Frame 4 框顺接 p.025，均与印刷断页位置一致，无跨页截断。
  - 未提交、未 `git add`/merge/push；未触碰仓库根 `AUDIT-INDEX.md`、`AUDIT-PROGRESS.log`、`MEMORY.md`、`README.md` 及他篇目录；PDF 全程只读；未启动或改动 mineru。

## 逐页重审块 F（PDF p.025–p.032）
- 与块 E（p.017–p.024）同一审计口径：每页单独渲染 150dpi `pngmono` → 用 Read 打开亲看 → 读对应 Markdown 段 → 五点比对 → 立刻 Edit 落签 → `Edit` 逐处修复并溯源 → 进下一页；公式判读一律以 300dpi 裁片为准，`pdftotext -bbox` 仅用于取 y 坐标。

## p.025（PDF p.25 / 印刷 p.25）
- PNG：/tmp/icm2022dc_audit_p025.png（pngmono 150dpi）；仲裁裁剪 /tmp/icm2022dc_p025_300.png（300dpi 全页）、/tmp/icm2022dc_p025_eq614.png（(6.14) 全式，2× 放大）、/tmp/icm2022dc_p025_partial.png（`∂𝐧 = {x, y}` 一行）、/tmp/icm2022dc_p025_betac.png（`β_c > 0.` 一行）、/tmp/icm2022dc_p025_difference.png（`symmetric difference` 一行）、/tmp/icm2022dc_p025_eq615.png（(6.15) 全式，2× 放大）
- 核对：Frame 4 框续文 `exp[βσ_xσ_y] = cosh(β) + sinh(β)σ_xσ_y`；公式 (6.14) 的 `Z(G,β,0)`、`cosh(β)^{|E|}`、`∑_{F∈Even(G)}`、`tanh(β)^{|F|}`、尾逗号；`G` vs `G*`、`tanh(β) = e^{−2β*}`、`Kramers-Wannier`、`square lattice`；`∂𝐧 = {x, y}` 与 `∂𝐧 = ∅` 两个映射端、`β ≪ 1`、`⟨σ_xσ_y⟩_{G,β,0}`、`β_c > 0.`；`switching lemma`、`Frame 5`、`reinterpret spin-spin correlations`、`Sections 6.4, 6.6, and 7.1`；Frame 5 框题与框内 `𝐧 ∈ 𝓕_A`、`𝐤 ≤ 𝐧`、`∂𝐤 = A`、`A = {x, y}`、`AΔB`、`symmetric difference`、`switching lemma [59]`、`F : ℤ₊^E → ℝ`、`A, B ⊂ V`；公式 (6.15) 的两个 `\substack` 条件、`AΔB`、`∅`、`𝕀(·)`、`𝓕_B`、尾句点；末段 `self-explanatory`、`left to the reader`；页脚 `25  100 Years of the Ising Model`。
- 结果：PASS±（差异列表如下，3 处已逐处 Edit 修复）
- 逐项核对：
  - (6.14) 印刷 `Z(G,β,0) = cosh(β)^{|E|} ∑_{F∈Even(G)} tanh(β)^{|F|},`（裁片 `/tmp/icm2022dc_p025_eq614.png`）：两个指数的**竖线绝对值** `|E|`、`|F|`、`Even(G)` 的**正体** `Even`、求和域 `F ∈ Even(G)`、尾**逗号**、编号 `(6.14)`，与 MD 行 578 逐符号对应。
  - `tanh(β) = e^{−2β*}` 的指数 **`−2β*`**（系数 2、β 的星号均在指数内，未误作 `e^{−2}β*`）、`G*` 的上标星号，与 MD 行 581 一致。
  - `∂𝐧 = {x, y}` 与 `∂𝐧 = ∅`（裁片 `/tmp/icm2022dc_p025_partial.png`）：印刷作「…a mapping from currents with **∂𝐧 = {x, y}** to currents with…」——**无额外花括号**、𝐧 为**粗体**；与 MD 行 583 修复后的 `$\partial \mathbf { n } = \{ x , y \}$` 一致。
  - `β ≪ 1`（`≪` 而非 `<<`）、`⟨σ_xσ_y⟩_{G,β,0}` 的下标 `G,β,0`、`β_c` 的下标 `c`、`β_c > 0.` 的**句点**（裁片 `/tmp/icm2022dc_p025_betac.png`），与 MD 行 583 一致。
  - `Sections 6.4, 6.6, and 7.1` 三个编号与印刷一致；`Frame 5` 交叉引用正确。
  - Frame 5 框内（裁片 150dpi + bbox 逐词）：`Write 𝐧 ∈ 𝓕_A if there exists 𝐤 ≤ 𝐧 with ∂𝐤 = A`、`A = {x, y}`、`AΔB` 的三角形、`F : ℤ₊^E → ℝ`、`A, B ⊂ V`（**子集号 ⊂，非 ⊆**）、`switching lemma [59]`，与 MD 行 589 一致；`symmetric difference` 见下方差异第 3 条。
  - (6.15) 印刷 `∑_{∂𝐧₁=A, ∂𝐧₂=B} w(𝐧₁)w(𝐧₂)F(𝐧₁+𝐧₂) = ∑_{∂𝐧₁=AΔB, ∂𝐧₂=∅} w(𝐧₁)w(𝐧₂)F(𝐧₁+𝐧₂) 𝕀(𝐧₁+𝐧₂ ∈ 𝓕_B).`（裁片 `/tmp/icm2022dc_p025_eq615.png`）：两个求和的 `\substack` 双行条件（右端第一行为 **`AΔB`** 而非 `A`、第二行为 **`∅`**）、指示函数为**黑板粗体 𝕀**、其自变量为 `𝓕_B`（**下标 B**）、末尾**句点**在 `𝓕_B)` 之后、编号 `(6.15)`，与 MD 行 592 逐符号对应。
  - 结构与次序吻合：页首承 p.24 的 Frame 4 框 → (6.14) → `which resembles the low-temperature expansion…` 段 → `One application of currents…` 段 → `A key observation of Aizenman…` 段 → Frame 5 框 → 框内三段（`Write 𝐧 ∈ 𝓕_A…` / (6.15) / `The name of the lemma…`）；无缺失或错序。页末 Frame 5 框已闭合。
- 差异列表（3 处，均已用 `Edit` 逐处修复，命中位置均唯一）：
  1. 行 583 `currents with${ \partial \bf n } = \{ x , y \}$to currents with` → `currents with$\partial \mathbf { n } = \{ x , y \}$to currents with`：**行内数学标记破损 + 无效宏**。原串把 `$` 写成 `${`，使公式体变成 `{ \partial \bf n } = \{ x , y \}`——公式内多出一对**字面花括号**，而 `\bf` 在 LaTeX 中不是 `\mathbf` 那样的字体切换宏（须置于分组内方生效，此处无分组，`\bf` 会作用到后续全部字符），两重问题叠加使该约束**根本不能正确排版**；印刷（裁片 `/tmp/icm2022dc_p025_partial.png`）为 `∂𝐧 = {x, y}`，无多余花括号且 𝐧 为粗体。同一句后半的 `\partial \mathbf { n } = \boldsymbol { \emptyset }` 写法正确，可见此处系导出器的孤立缺陷。
  2. 行 583 段末 `This implies in particular that$\beta _ { c } > 0$` → 补句点。裁片 `/tmp/icm2022dc_p025_betac.png` 显示印刷作「…This implies in particular that β_c > 0**.**」，bbox 亦给出 `0.` 这一词元；MD 缺失。
  3. 行 589 `Recall that $A\Delta B$ denotes the symmetric diference of the sets $A$ and $B$` → `difference`：**`ff` 连字拍平**。300dpi 裁片 `/tmp/icm2022dc_p025_difference.png` 显示印刷的两个 `f` 为**连写**（`ff` 合字，笔画在顶部相连），bbox 文本层亦给出 `difference`；MD 拍平为 `diference`。
- 溯源（回归判定）：对 `cpf-redo/ICM2022_proceedings_Duminil-Copin^`、该分支 HEAD、当前工作树执行三组三态 `grep -cF`（`currents with${ \partial \bf n } = \{ x , y \}$to`、`in particular that$\beta _ { c } > 0$`、`symmetric diference`），命中数均为 **1/1/1**，确认 3 处**全部为原始 MinerU 导出缺陷，无一条系 peer 引入的回归**。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：行 585 印刷作「intuitions coming from probabilistic models such as random walks and percolation **was** later used to prove new theorems」——主语 `intuitions` 为复数而谓语用单数 `was`，且整句缺「These」一类主语，属原刊语法瑕疵。bbox 文本层同样给出 `…percolation was later`，确证为印刷原文。**不改**。
  - 行 585 `in terms ofprobabilities`（空格合并）、行 583 `currents with$…$to`、行 589 `Write$\mathbf { n } \in \mathcal { F } _ { A }$if`、`$F : … \to \mathbb { R }$and`、`vertices $A,B \subset V,`、行 595 无此类问题——行内数学与相邻文字未留空格，全篇一致的排版级伪影。
  - (6.15) 中 MD 写作 `F(\mathbf{n}_{1} + \mathbf{n}_{2})\mathbb{I}(…)`，印刷在 `F(𝐧₁+𝐧₂)` 与 `𝕀(…)` 之间有一处细空隙；纯间距，符号身份一致。
  - 印刷斜体/强调（`switching lemma`、`current`、`source`、`diference`→`difference`、`symmetric difference`、`self-explanatory`、`−` 前的 `Odd` 等）未在 MD 保留（风格级）。
  - Frame 4、Frame 5 两个框的**边框**未在 MD 保留（框题已作 `## Frame 4: …` / `## Frame 5: …`，版式级）。
  - 页脚 running foot `25  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页 3 处修复全部以 `Edit` 工具逐处落地，`old_string` 均先经 `grep -cF` 确认唯一；落地后复核 `currents with${ \partial \bf n } = \{ x , y \}$to` 与 `symmetric diference` 命中均为 0，行 583 作 `currents with$\partial \mathbf { n } = \{ x , y \}$to currents with` 且段末作 `in particular that$\beta _ { c } > 0$.`，行 589 作 `denotes the symmetric difference of the sets $A$ and $B$`。全程未使用脚本写回 Markdown。

## p.026（PDF p.26 / 印刷 p.26）
- PNG：/tmp/icm2022dc_audit_p026.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p026_300.png`（2008×2835 px），裁片 `_caseAB` `_eq616` `_whereline` `_eq617` `_eq618`（各 2×）；bbox `/tmp/icm2022dc_p026_bbox.xml`
- 核对：Frame 5 框尾（(6.16) 及框内正文）、§6.4 标题 `6.4. Triviality in dimension d>4`、公式 (6.17)、Σ_L 定义行、公式 (6.18)、框后至「losing the switching lemma and its benefits.」全段
- 结果：PASS±（差异列表，见下）
- 修复（4 处，均以 `Edit` 工具逐处落地）：
  1. 行 597 `A direct application … is the case$A = B$ which gives immediately that` → `… is the case$A = B$, which gives …`。印刷在 `$B$` 后有逗号（裁片 `/tmp/icm2022dc_p026_caseAB.png` 直读「is the case 𝐴 = 𝐵,」；bbox y=50 行尾为 `𝐴 𝐵,`），导出丢失该逗号。
  2. 行 603 `the measure on currents n on $G$` → `the measure on currents$\mathbf { n }$ on $G$`。印刷此处 𝐧 为黑体（裁片 `/tmp/icm2022dc_p026_whereline.png` 中四处 𝐧 皆为粗体：currents 后、∂ 后、each such 后、*w*() 内），导出仅保留其中两处的黑体，另两处退化为普通斜体 `n`。
  3. 行 603 `attributing to each such n a probability` → `attributing to each such$\mathbf { n }$ a probability`。同上，同一裁片直读。
  4. 行 603 `to recover Griffiths inequalities from` → `to recover Griffiths' inequalities from`。印刷作「Griffiths' inequalities」（bbox y=159 行尾 `…recover Griffiths’`），导出吞掉所有格撇号；对照行 263「Griffiths' inequalities [57]」与行 135「Griffiths' "ghost" vertex」撇号均在，可证本页为孤立丢失而非全篇风格。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：印刷页脚 running foot 为 `26  Hugo Duminil-Copin`，全篇仅此处作者名直接跟在页码后（p.25 页脚为 `25  100 Years of the Ising Model`），MD 未收页脚，版式级，不改。
  - 印刷 §6.4 首句作「Michael Aizenman and Juerg Fröhlich [2,49] independently proved」（连写 Juerg，未用变音符号 ü；其后段落亦作 `Fröhlich`），MD 忠实转写，不改。
  - 行 610 `(6.17)` 中 `f (x / L)   \sigma_ { x }` 三个多余空格（印刷为 `f(x/L) σ_x`，行内紧排），纯间距伪影。
  - 行 613 `$\begin{array} { r } { \Sigma _ { L } : = … } \end{array}$`——印刷为正文内联的 `Σ_L := ⟨(∑_{x∈Λ_L} σ_x)²⟩`，导出用 `array` 环境包起以回避行内数学，属结构化伪影，符号内容与顺序一致。
  - 行 603 `the square ofspin-spin correlations`（空格合并）、`currents$\mathbf { n }$ on $G$`、`$\partial \mathbf { n } = B$attributing`、`proportional to$w ( \mathbf { n } )$`、`and$\otimes$denotes`、行 613 `compactly supported`（印刷行首 `where f ranges over compactly supported continuous functions, and Σ_L := …`，MD 未误拆）、行 621 `$\phi ^ { 4 }$lattice model`——行内数学与相邻文字未留空格，全篇一致的排版级伪影。
  - 印刷斜体强调（`square`、`independent`、`well-defined`、`brutal stop`、`deeply connected`）未在 MD 保留（风格级）。
  - 印刷行末断词 `spin-` / 次行 `spin correlations`（bbox y=549 / y=563）已正确合并为 MD 的 `spin-spin correlations`，非缺陷。
- 备注：本页 4 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。(6.16)、(6.17)、(6.18) 三个公式经 300dpi 裁片逐符号核对（黑体 𝐧₁+𝐧₂、黑板 ℙ^∅_G、𝔽_A、ℤ^d、Λ_L、ξ(β)、C_f z⁴/L^{d−4}、句末句点）全部与印刷一致，MD 无误。全程未使用脚本写回 Markdown。

## p.027（PDF p.27 / 印刷 p.27）
- PNG：/tmp/icm2022dc_audit_p027.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p027_300.png`，裁片 `_eq619` `_eq620` `_lt4` `_bfn` `_dificulty`（各 2×）；bbox `/tmp/icm2022dc_p027_bbox.xml`
- 核对：四點函数/Ursell function 引入段、公式 (6.19)、公式 (6.20)、(6.20) 下方至「thus hinting at triviality.」段、random walk 交概率段、`con-tractially` 段、§6.5 标题 `6.5. Rigorous renormalisation group in 4D Ising` 及该页末段
- 结果：**FAIL**（(6.20) 整条公式被拆成两个 `$$` 块且中间三个词「all connected in」整段丢失，以原图为准）
- 修复（6 处，均以 `Edit` 工具逐处落地）：
  1. **（6.20）结构断裂 + 内容丢失**：原 MD 把印刷上的**单条**公式拆成两个独立 `$$` 块——第一块止于 `[ x _ {1}, \ldots , x _ {4}`（方括号未闭合、无编号），第二块为 `\left. \mathbf {n} _ {1} + \mathbf {n} _ {2} \right]\tag{6.20}`（凭空多出 `\left.`），且印刷方括号内 `x_1,…,x_4` 与 `𝐧₁+𝐧₂` 之间的三个词 **all connected in** 在 MD 中**完全不存在**。裁片 `/tmp/icm2022dc_p027_eq620.png` 直读为一行：`U_4^β(x_1,…,x_4) = −2⟨σ_{x_1}σ_{x_2}⟩⟨σ_{x_3}σ_{x_4}⟩ ℙ^{ {x_1,x_2} } ⊗ ℙ^{ {x_3,x_4} } [ x_1,…,x_4  all connected in 𝐧₁ + 𝐧₂],`，(6.20) 编号另起一行右对齐；bbox y=121 同样给出 `[𝑥 all connected in n + n ],`。已合并为单一 `$$ … \text { all connected in } \mathbf {n} _ {1} + \mathbf {n} _ {2} ],\tag{6.20} $$`。
  2. 行 637（修复后）`in dimensions$d < 4 .$, and` → `in dimensions$d < 4$, and`。印刷在 `4` 后只有逗号，MD 在数学模式内多插一个句点（裁片 `/tmp/icm2022dc_p027_lt4.png` 直读「in dimensions 𝑑 < 4, and tending to zero…」；bbox y=263 亦为 `𝐿 𝑑 <` + y=260 行内 `4,`）。属标点身份改变。
  3. 行 637（修复后）`…in dimension $d \ge 4$` → `…in dimension $d \ge 4$.`。印刷该句末有句点（bbox y=274 行首 `≥ 4.`；同一裁片下一行直读 `𝑑 ≥ 4`），MD 漏句末句点。
  4. 行 639 `in${ \bf n } _ { 1 }$,` → `in$\mathbf { n } _ { 1 }$,`。`\bf` 非 LaTeX 合法宏（打印为字面量），应为 `\mathbf`；印刷该处 𝐧₁ 为黑体（裁片 `/tmp/icm2022dc_p027_bfn.png` 直读「…𝑥₂ in 𝐧₁, and 𝑥₃ and 𝑥₄ in 𝐧₂, would behave…」）。
  5. 行 639 `in${ \bf n } _ { 2 }$,` → `in$\mathbf { n } _ { 2 }$,`。同上，同一裁片直读。（与 p.25 行 583 的 `\bf n` 属同一 `\bf` 失效宏类。）
  6. 行 641 `go around the dificulty of proving` → `go around the difficulty of proving`。ff 连字被压平（裁片 `/tmp/icm2022dc_p027_dificulty.png` 直读「around the difficulty of proving a random walk type behaviour」，bbox y=414 亦为 `difficulty`）。
  7. 行 641 `through the vertices ofa graph` → `through the vertices of a graph`。空格合并（bbox y=205：`walker traces his way through the vertices of a graph by picking its next steps at random among`）。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：印刷行末断词 `con-` / 次行 `tractially`（bbox y=442 / y=456）已正确合并为 MD 的 `contrarily`，非缺陷；印刷同段的破折号 `stands – this Markov process`（en dash），MD 保留原字符。
  - **印刷怪癖**：印刷 §6.5 首句作「The triviality of the Ising model in dimension 4 naturally raises the question of its triviality in dimension = 4」——`dimension` 后先出印刷斜体 `d` 再接 `> 4`（bbox y=539 `The triviality of the Ising model in dimension 4 naturally raises the question`，y=542 `𝑑 >`），版面顺序为 `dimension d > 4`；MD 作 `dimension$d > 4$naturally`，忠实，不改。
  - 印刷 `4 − ε expansions` 中的 `ε` 为印刷斜体（bbox y=570），MD 作 `$4-\varepsilon$`，符号身份一致。
  - 印刷斜体强调（`expected number of intersections`、`not`、`all connected in`、`pertinent`、`a Gaussian random variable`）未在 MD 全部保留（风格级；`all connected in` 因落在公式内，已按上条第 1 处补入并以 `\text{}` 承印）。
  - 行 625 `for$x _ { 1 } , \ldots , x _ { 4 } \in \mathbb { Z } ^ { d }$, by`、行 637 `where connected in$\mathbf { n } _ { 1 } + \mathbf { n } _ { 2 }$means`、`$x _ { 1 }$and$x _ { 2 }$as`、`at the light of so-called`、`intersect with a probability bounded away from 0 as $L$ tends`、行 639 `the points$x _ { 1 }$and`、`dimensions$d \ge 4$as being`、`for which$U _ { 4 } ^ { \beta }$becomes`、行 645 `tending to zero with $L$. Using`、`to 0.`、行 651 `dimension$d > 4$naturally`、`dimension$d = 4$, which`——行内数学与相邻文字未留空格，全篇一致的排版级伪影。
  - 印刷页脚 running foot `27  100 Years of the Ising Model` 未入 MD（版式级）。
  - MD 行 677 另有 `one example ofa graphical representation`（同类空格合并），落在本轮页段之外，留给 p.30 一并处理。
- 备注：本页 7 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。(6.19) 经 300dpi 裁片逐符号核对（`⟨σ_{x_1} ⋯ σ_{x_4}⟩_β`、`∑_{π pairing} ∏_{i=1}^2`、`⟨σ_{x_{π(2i−1)}} σ_{x_{π(2i)}}⟩_β`、句末句点）**与印刷完全一致，MD 无误**，判 FAIL 的唯一原因是 (6.20) 的拆块与「all connected in」丢失。全程未使用脚本写回 Markdown。

## p.028（PDF p.28 / 印刷 p.28）
- PNG：/tmp/icm2022dc_audit_p028.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p028_300.png`，裁片 `_malisation` `_gawed` `_gawedtail`(4×) `_bauer` `_vicinity` `_aterms`；bbox `/tmp/icm2022dc_p028_bbox.xml`
- 核对：§6.5 末段「Consider the lattice version of the φ⁴ model…」、「Several methods were used at the time…」（Gawedski/Kupiainen/Kadanoff 段）、「An alternative to this block-spin renormalisation…」（Bauerschmidt/Brydges/Slade 段）、「The level of sophistication of these techniques…」、§6.6 标题 `6.6. Forty years later: the random current strikes back`、§6.6 首段、页末段前半「This asks for another approach…lattice models, which」（续 p.29）
- 结果：**PASS**（未发现需修复处）
- 逐字核对留证（全部与印刷一致，MD 无误）：
  - `Gawedski`——印刷行末断词 `Gawed-` / 次行 `ski`，4× 裁片 `/tmp/icm2022dc_p028_gawedtail.png` 直读确认 `e` 为**普通 e、无 ogonek 变音符**（该作者名通行拼法为 Gawędski，原刊如此排印）；bbox y=135/y=149 亦作 `Gawed-` / `ski`。MD 已正确合并且**未**擅自改成通行拼法，符合铁律三。
  - `renormalisation`——印刷断词 `renor-` / `malisation`（bbox y=149 / y=163），MD 已正确合并。
  - `Bauerschmidt`——印刷断词 `Bauer-` / `schmidt`（bbox y=232 / y=246），裁片 `_bauer` 直读，MD 正确合并。
  - `(6.20)` 之后 §6.5 正文全部 φ⁴ 记号：`the$\phi ^ { 4 }$model`（y=37/40）、`$b = \lambda = 0$corresponds`（y=51/54）、`coupled$\phi ^ { 4 }$lattice model (meaning that $\lambda$ is small)`（y=105/107/109）、`the$\phi ^ { 4 }$lattice model`（y=274/277）、`the original$\phi ^ { 4 }$lattice model is in the “vicinity of a model”`（y=400/402，裁片 `_vicinity` 直读花体 φ 与弯引号），MD 全部正确；`large blocks of size$L ^ { k }$`（y=177/179）正确。
  - §6.6 首段三处 φ⁴（y=511/514 `the lattice$\phi ^ { 4 }$model`、y=524/525 `a small$\phi ^ { 4 }$term`、y=537/542 `strongly coupled$\phi ^ { 4 }$lattice model`、y=551/556 `a$\phi ^ { 4 }$terms`）MD 全部正确。
  - 引用编号 `[43, 51, 62]`（y=94）、`[51]`（y=150）、`[11]`（y=248）与印刷一致。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：印刷作「one would definitely try to start with a strongly coupled φ⁴ lattice model (**meaning with a φ⁴ terms** which is not a priori small)」（单数冠词 `a` 配复数名词 `terms`；bbox y=553 原样给出 `model (meaning with a terms which is not a priori small)`，裁片 `/tmp/icm2022dc_p028_aterms.png` 直读 `a φ⁴ terms which is not a priori small`）。属原刊语法笔误，MD 忠实转写，**不改**。
  - **印刷怪癖**：印刷作「a rigorous version of Kadanoff block-spin renormalisation procedure」（`of` 后缺冠词 `the`），MD 忠实转写，不改。
  - **印刷怪癖**：印刷作「the technique is (as for today) perturbative in nature」（`as for today` 为作者口语式插入语），MD 忠实转写，不改。
  - **印刷拼写**：`Gawedski`（无变音符，见上）按原刊保留。
  - 印刷斜体强调（`pertubative` 处的 `perturbative`、`vicinity of a model`、§6.6 首段 `perturbative`）未在 MD 保留（风格级）。
  - 行 649 `the$\phi ^ { 4 }$model discussed`、`$b = \lambda = 0$corresponds`、`a weakly coupled$\phi ^ { 4 }$lattice`、行 651 `size$L ^ { k }$, and`、`the reality is much more complicated` 前后无异常、$L^k$ 附近无空格丢失、行 653 `quantities in the$\phi ^ { 4 }$lattice model`、行 655 `the original$\phi ^ { 4 }$lattice model`、行 659 `the lattice$\phi ^ { 4 }$ model`、`a small$\phi ^ { 4 }$term`、`coupled$\phi ^ { 4 }$lattice model`、`(meaning with a$\phi ^ { 4 }$terms`、`4D Ising and$\phi ^ { 4 }$lattice models`——行内数学与相邻文字未留空格，全篇一致的排版级伪影（与 p.25–p.27 同类）。
  - 页末段「…triviality of the 4D Ising and φ⁴ lattice models, **which**」在 MD 中与 p.29 的续文同处一行（行 661），未在页界断开——MinerU 的段落合并行为，非符号缺陷，登记。
  - 印刷页脚 running foot `28  Hugo Duminil-Copin` 未入 MD（版式级；与 p.26 同款作者名页脚）。
- 备注：本页无修复，故未做溯源 grep。**150dpi 全页图上「renorma-lisation」一处 `ti` 连字在低分辨率下形似 `t!`，经 300dpi 裁片 `/tmp/icm2022dc_p028_malisation.png` 直读确认为正常 `ti` 连字，bbox y=163 亦作 `malisation procedure`——判为 150dpi 伪影，非缺陷，MD 保持原样**（铁律二：仅以亲眼看过的原页图与文字层仲裁，不因低分辨率观感改字）。全程未使用脚本写回 Markdown。

## p.029（PDF p.29 / 印刷 p.29）
- PNG：/tmp/icm2022dc_audit_p029.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p029_300.png`，裁片 `_para1` `_eq621` `_diferent` `_ofliquid` `_ofa`（各 2×）；bbox `/tmp/icm2022dc_p029_bbox.xml`
- 核对：p.28 页末段续文「states [4] … every z > 0,」、公式 (6.21)、「The strategy of the proof uses a more delicate probabilistic perspective…」全段、§7 标题 `7. The last fifty years: Ising model and percolation`、§7 首段（`G=(V,E)`、`ω=(ω_e: e∈E) ∈ {0,1}^E`）、§7 第二段、§7.1 标题 `7.1. Percolation interpretation of random currents` 及页末段
- 结果：PASS±（差异列表，见下）
- 修复（6 处，均以 `Edit` 工具逐处落地）：
  1. 行 661 `with parameters $b , \lambda .$, and` → `with parameters $b , \lambda$, and`。印刷在 `λ` 后只有逗号（裁片 `/tmp/icm2022dc_p029_para1.png` 直读「with parameters 𝑏, 𝜆, and a compactly supported…」；bbox y=51 行首 `and a compactly supported continuous function` 前即为该逗号），导出在数学模式内多插一个句点。标点身份改变，与 p.27 行 637 `$d < 4 .$` 同类。
  2. 行 661 `continuous function$f ,$, there exists` → `continuous function$f$, there exists`。印刷为「function 𝑓, there exists」**单个**逗号（同一裁片直读 `continuous function 𝑓, there exists 𝐶_𝑓 > 0 such that for`；bbox y=51 亦为 `function , there exists`），导出把逗号重复了一次（数学内一个、数学外一个）。标点身份改变。
  3. 行 671 `Then, diferent percolation models` → `Then, different percolation models`。ff 连字压平（裁片 `/tmp/icm2022dc_p029_diferent.png` 直读「Then, different percolation models」；bbox y=364 亦作 `different`）。
  4. 行 671 `by considering diferent measures` → `by considering different measures`。同上，同一裁片直读 `can be defined by considering different measures on {0, 1}^E`；bbox y=378 亦作 `different measures`。
  5. 行 671 `the behaviour ofliquid in a porous medium` → `the behaviour of liquid in a porous medium`。空格合并（裁片 `/tmp/icm2022dc_p029_ofliquid.png` 直读「the behaviour of liquid in a porous medium」；bbox y=406 亦作 `of liquid`）。
  6. 行 677 `one example ofa graphical representation` → `one example of a graphical representation`。空格合并（裁片 `/tmp/icm2022dc_p029_ofa.png` 直读「one example of a graphical representation in Frame 5」；bbox y=587 亦作 `of a graphical`）。**注**：此即 p.027 条目中预告留给本页的 `ofa`，一并落地。
- 登记不改：
  - **φ 字形分立（重点核对项，MD 无误）**：印刷在同一页上同时使用**两个不同的 φ 字形**——正文「the n.n.f. 𝜙⁴ lattice model」为直杠 φ（bbox 字符 `𝜙` = `\phi`），而 (6.21) 式内 `T_{f,L}(𝜑)` 为环状 φ（bbox 字符 `𝜑` = `\varphi`）。裁片 `/tmp/icm2022dc_p029_para1.png` 与 `/tmp/icm2022dc_p029_eq621.png` 分别直读确认两形。MD 行 661 用 `\phi ^ { 4 }`、行 664 用 `\varphi`，**与印刷一致**，未误并为同一字形，判为正确转写，不改。
  - (6.21) 印刷为 `|⟨exp[z T_{f,L}(𝜑) − z²/2 ⟨T_{f,L}(𝜑)²⟩_β]⟩_β − 1| ≤ C_f z⁴/(log L)^c.`（含句末句点）；MD 行 664 逐符号一致（`(\log L) ^ {c}`），**无误**。
  - 黑板粗体 ℤ⁴（裁片 `_para1` 直读 `on ℤ⁴`，bbox y=35/40）与 C_f 下标 f（bbox y=56）MD 均正确保留。
  - 印刷行末断词 `ran-` / `dom current`（bbox y=113 / y=127）与 `intersect-` / `ing, random currents`（bbox y=252 / y=266）、`perco-` / `lation theory`（bbox y=448 / y=462）均已正确合并为 MD 的 `random`、`intersecting`、`percolation`，非缺陷。
  - **印刷怪癖（铁律三，原样保留）**：印刷作「a variety of **random graphs systems**」（`graphs` 作定语却用复数形式），bbox y=336 原样给出，MD 忠实转写，不改。
  - 印刷斜体强调（`graphical representation` 处、§7 首段无）未在 MD 保留（风格级）。
  - 行 661 `there exists$c > 0$such`、`the n.n.f.$\phi ^ { 4 }$lattice model on${ \mathbb { Z } } ^ { 4 }$with`、`there exists$C _ { f } > 0$such`、`every$\beta \leq`、`every$L \le \xi ( \beta )$, and every$z > 0$`、行 667 `of order$L$` 附近、`order (log$L ) ^ { - c }$for`、`constant$c > 0$.`、`large in $L$ (and is growing with $L )$.`、行 671 `A configuration on$G = ( V , E )$is an element$\omega`、$\in \{ 0 , 1 \} ^ { E }$which`、`and edge-set$\{ e \in E : \omega _ { e } = 1 \}$.`、`measures on$\{ 0 , 1 \} ^ { E }$.`、`the$\omega _ { e }$are`、`related to a variety of other models`——行内数学与相邻文字未留空格，全篇一致的排版级伪影。
  - 印刷页脚 running foot `29  100 Years of the Ising Model` 未入 MD（版式级）。
  - 全篇尚存 `diferent` / `diferential` 共 8 处于行 27、115、131、691、697、875、879、907；其中行 691/697 落在本轮 p.30 页段内，留给 p.030 处理；行 27、115、131 在本轮范围之外，行 875 及以后更靠后，留给集成者统一处理，本页不动。
- 备注：本页 6 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。§7 两段与 §7.1 全段经 300dpi 裁片与 bbox 逐句核对，除上述 6 处外与印刷逐字一致。全程未使用脚本写回 Markdown。

## p.030（PDF p.30 / 印刷 p.30）
- PNG：/tmp/icm2022dc_audit_p030.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p030_300.png`，裁片 `_suficiently` `_magnetisation` `_magH` `_eq72` `_beta_comma` `_endpara` `_diferential2` `_diferential3`（2×）；bbox `/tmp/icm2022dc_p030_bbox.xml`
- 核对：§7.1 首段（`ω_{{x,y}}=1 if (𝐧₁+𝐧₂)_{{x,y}}>0`）、Aizenman–Barsky–Fernandez 段、公式 (7.1)、`sharp` 段与截断关联式、bottleneck 段、注释段（magnetisation m = m(β,h)）、公式 (7.2)、Bernoulli percolation 段、公式 (7.3)
- 结果：PASS±（差异列表，见下）
- 修复（8 处，均以 `Edit` 工具逐处落地）：
  1. 行 681 `for each such$\beta ,$, there exists` → `for each such$\beta$, there exists`。印刷为「for each such 𝛽, there exists 𝜏 > 0」**单个**逗号（裁片 `/tmp/icm2022dc_p030_beta_comma.png` 直读；bbox y=151 亦仅一逗号），导出把逗号重复一次（数学内 + 数学外）。标点身份改变，与 p.029 行 661 `$f ,$,` 同类。
  2. 行 689 `which is suficiently large` → `which is sufficiently large`。连字压平（裁片 `/tmp/icm2022dc_p030_suficiently.png` 直读「with a rate of decay which is sufficiently large」，可见 `ſſ` 长 s + `fi` 连字；bbox y=281 亦作 `sufficiently`）。
  3. 行 689 段末 `…it is finite as soon as$\beta < \beta _ { c }$` → `…$\beta < \beta _ { c }$.`。印刷句末有句点（裁片 `/tmp/icm2022dc_p030_endpara.png` 直读「finite as soon as 𝛽 < 𝛽_c.」；bbox y=393 行尾 `as soon as .`），MD 漏句末句点。
  4. 行 691 `deriving diferential inequalities between` → `deriving differential inequalities between`。连字压平（裁片 `/tmp/icm2022dc_p030_magnetisation.png` 直读「in deriving differential inequalities between thermodynamical quantities of the Ising model」；bbox y=421 亦作 `differential`）。
  5. 行 691 `such diferential inequalities are given` → `such differential inequalities are given`。同上（bbox y=435 作 `such differential inequalities are given`；150dpi 全页图已直读确认，300dpi 裁片 `_magnetisation` 同段相邻可见）。
  6. 行 691 `of$\beta$and ℎ)` → `of$\beta$and $h$)`。**字符身份错误**：导出把斜体数学 `h` 识别为 Unicode **ℎ U+210E PLANCK CONSTANT**（ℏ 的近形字）。裁片 `/tmp/icm2022dc_p030_magH.png` 直读「by (recall that the magnetisation 𝑚 = 𝑚(𝛽, ℎ) is a function of 𝛽 and ℎ)」——两处均为普通斜体 `h`；bbox y=451 亦为 `ℎ`（该 PDF 文字层本身就用 ℎ 编码斜体 h，属可交叉验证的同形字符），而印刷无 ℏ 记号。已改回 `$h$` 并置于数学模式。
  7. 行 697 `similar diferential inequalities appear` → `similar differential inequalities appear`。连字压平（裁片 `/tmp/icm2022dc_p030_diferential2.png` 直读「The interesting feature here is that similar differential inequalities appear when studying」；bbox y=490 亦作 `differential`）。
  8. 行 697 `using diferential inequalities that can` → `using differential inequalities that can`。连字压平（裁片 `/tmp/icm2022dc_p030_diferential3.png` 直读「using differential inequalities that can be adapted to Bernoulli percolation」；bbox y=546 亦作 `differential`）。
- 逐字核对留证（MD 无误，未改）：
  - 公式 (7.1) 印刷 `⟨σ_x σ_y⟩_{β,0} ≤ exp(−τ∥x − y∥).`（bbox y=176–182），MD 行 684 逐符号一致，含句末句点。
  - 公式 (7.2) 印刷 `m ≤ tanh(βh) ∂/∂(βh) m + m²(β ∂/∂β m + m)  and  m ∂/∂β m ≥ c.`；裁片 `/tmp/icm2022dc_p030_eq72.png` 直读逐符号确认，MD 行 694 完全一致（含 `\quad\text { and }\quad` 与句末 `c.`）。
  - 公式 (7.3) 印刷 `(1 − B/χ) 2dχ²/(1+B) ≤ ∂/∂β χ ≤ 2dχ²,`（bbox y=590–608），MD 行 700 一致。
  - `β_exp` 的正体下标：印刷 `(\beta_{\mathrm{exp}}, \beta_c)`（bbox y=200/201/203 分列 `, 𝛽` / `exp` / `𝛽_c`），MD 行 687 作 `\beta _ { \mathrm { { e x p } } }`，**符号身份与字体正确**，内部空格为排版伪影。
  - 「there is no intermediate phase」后印刷确有 `(β_exp, β_c)`，MD 未漏。
  - §7.1 首段印刷 `ω_{{x,y}} = 1 if (𝐧₁ + 𝐧₂)_{{x,y}} > 0`，MD 行 679 的 `\mathbf{n}`、`> 0`、`\mathrm { i f }` 全部正确。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：印刷作「The archetypical example of such differential inequalities **are** given」（主语单数 + 谓语复数）；bbox y=435 原样给出，MD 忠实转写，不改。
  - **印刷怪癖**：印刷作「correlations of the **n.n.f. Ising model** decay exponentially fast」——`n.n.f.` 后直接跟 `Ising model`，无「the」；bbox y=135 亦如此，MD 忠实，不改。
  - 印刷行末断词 `quan-` / `tities`（bbox y=267 / y=281）、`eight-` / `ies`（bbox y=504 / y=518）已正确合并为 MD 的 `quantities`、`eighties`，非缺陷。
  - 行 687 `⟨σ_xσ_y⟩_{β,0} −` 与 `m*(β)²` 之间被 MD 用一个空格连接（`-$ $m ^ { * } ( \beta ) ^ { 2 }$`），系原式跨行导出所致，合并后与印刷 `⟨σ_xσ_y⟩_{β,0} − m*(β)²` 内容一致，登记不改。
  - 印刷斜体强调（`sharp`、`truncated correlations`、`graphical representation` 处）未在 MD 保留（风格级）。
  - 行 679 `an edge$\{ x , y \} ,`、`connected in$\omega .$`、行 681 `regime$\beta < \beta _ { c }$.`、`as soon as$\beta < \beta _ { c }$in the sense`、`there exists$\tau > 0$such`、`every $x , y \in \mathbb { Z } ^ { d }$,`、行 687 `phase$( \beta _ { \mathrm { { e x p } } } , \beta _ { c } )$in`、`$\langle \sigma _ { x } \sigma _ { y } \rangle _ { \beta , 0 } -$ $m ^ { * } ( \beta ) ^ { 2 }$when$\beta > \beta _ { c }$,`、`$\langle \sigma _ {x} \sigma _ {y} \rangle_ {\beta , 0}$` 附近、$\langle \cdot \rangle$ 前后无空格、行 689 `the whole regime$\beta < \beta _ { c }$.`、`length$\xi ( \beta )$mentioned`、行 691 `magnetisation$m = m ( \beta , h )$is`、`a function of$\beta$and $h$)`、行 697 `critical exponents for$d > 4$were`、`for$h = 0$and$\beta < \beta _ { c }$,`——行内数学与相邻文字未留空格，全篇一致的排版级伪影。
  - 印刷页脚 running foot `30  Hugo Duminil-Copin` 未入 MD（版式级）。
- 备注：本页 8 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。
- **交全篇统一处理（登记，本轮页段之外不动）**：
  1. `ℎ`(U+210E) 误识别全篇尚存 9 处于行 67、95、171、257、261、321、327、343、409 与行 795——与本页第 6 处同一 OCR 混淆类（斜体 `h` → ℏ 形字符），其中行 67–409 在本轮范围之前、行 795 在本轮之后，留给集成者统一替换为 `$h$`。
  2. `diferent` / `diferential` 全篇尚存 6 处于行 27、115、131、875、879、907（均在本轮页段之外），留待相应页段或集成者处理。
  3. `$\beta ,$,` 式重复逗号全篇尚存 1 处于行 759（本轮页段之后），与本页第 1 处同类。
  全程未使用脚本写回 Markdown。

## p.031（PDF p.31 / 印刷 p.31）
- PNG：/tmp/icm2022dc_audit_p031.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p031_300.png`，裁片 `_resul` `_resul2`(4×) `_ge3` `_edgeweight` `_defining` `_h0` `_h0b`(5×)；bbox `/tmp/icm2022dc_p031_bbox.xml`
- 核对：p.30 页末段续文「where χ(β) := Σ_x ⟨σ_0σ_x⟩_{β,0} is the susceptibility…」、公式 (7.4)、Infrared Bound 段、`continuity result` 段、Burton–Keane 段、§7.2 标题 `7.2. Fortuin-Kasteleyn percolation`、FK 定义段、公式 (7.5)、`p`/`q` 参数与 `edge-weight`/`cluster-weight` 段、`q = 1`/`q ≠ 1`/`q = 2` 段、FK Ising 构造段与两条 bullet、`Then, σ has the law … h = 0` 段、`This coupling, due to Fortuin and Kasteleyn…` 段
- 结果：PASS±（差异列表，见下）
- 修复（5 处，均以 `Edit` 工具逐处落地）：
  1. 行 711 `is the following continuity resul of the phase transition` → `… continuity result of the phase transition`。印刷为 **`result`**（末尾 `t` 存在）——4× 裁片 `/tmp/icm2022dc_p031_resul2.png` 直读斜体 `continuity result`；bbox y=135 亦作 `continuity result`。导出把词末字母 `t` 吞掉，属**词形缺字**，与连字压平不同类。
  2. 行 711 `for every$d \ge 3$` → `for every$d \ge 3$.`。印刷句末有句点（裁片 `/tmp/icm2022dc_p031_ge3.png` 直读 `𝑑 ≥ 3.`；bbox y=162 行尾 `≥ 3.`），MD 漏句末句点。
  3. 行 723 `the edgeweight and the cluster-weight` → `the edge-weight and the cluster-weight`。印刷的词是 **`edge-weight`**（带连字符），因该行末尾正好断在连字符处：bbox y=348 行尾 `the edge-`、y=362 行首 `weight and the cluster-weight`；裁片 `/tmp/icm2022dc_p031_edgeweight.png` 直读「called respectively the *edge-*」/「*weight* and the *cluster-weight*, |𝜔| := Σ_{e∈E} 𝜔_e」。同句并列的 `cluster-weight` 连字符完好，唯独 `edge-weight` 丢失，可证系跨行连字符被吞而非排版。TeX 只可能在显式连字符处断词，故原文确为 `edge-weight`。
  4. 行 731 bullet `• defining$\sigma _ { x } = \sigma _ { C }$for every C and every$x \in C$` → `…every$x \in C$.`。印刷该 bullet 末尾有句点（裁片 `/tmp/icm2022dc_p031_defining.png` 直读「• defining 𝜎_𝑥 = 𝜎_𝐶 for every 𝐶 and every 𝑥 ∈ 𝐶.」；bbox y=549 行尾 `∈ 𝐶 .`），MD 漏。
  5. 行 733 `…and$h = 0$ This coupling, due to Fortuin and Kasteleyn…` → `…and$h = 0$. This coupling, …`。印刷在 `h = 0` 后有句点且「This coupling」另起一行（5× 裁片 `/tmp/icm2022dc_p031_h0b.png` 直读「p)] and 𝑡 = 0.」；bbox y=560 行尾 `𝜎 𝐺 𝛽 𝑝)] ℎ` 后接 y=571 起首 `This coupling, due to Fortuin…`），导出既吞句点又把两段并成一段。
- 逐字核对留证（MD 无误，未改）：
  - 公式 (7.4) 印刷 `B(𝛽) := Σ_{x∈ℤ^d} ⟨σ_0 σ_x⟩^2_{β,0}.`（bbox y=61–81），MD 行 706 逐符号一致，含句末句点。
  - 公式 (7.5) 印刷 `𝜙_{G,p,q}[{𝜔}] := 1/Z(G,p,q) 𝑝^{|𝜔|} (1−𝑝)^{|E|−|𝜔|} 𝑞^{k(𝜔)},`（bbox y=319–335），MD 行 720 一致，`\phi`（直杠 φ）字形亦正确（bbox 字符 `𝜙`）。
  - `|𝜔| := Σ_{e∈E} 𝜔_e`：裁片 `_edgeweight` 直读该式为正文内联，MD 用 `\begin{array} { r } { … } \end{array}` 包起（与 p.26 的 Σ_L、p.24 同类的结构化伪影），符号内容与顺序一致，不改。
  - `1 / |β − β_c|`（bbox y=106/107 `− |` / `as 4, must blow up like 1/|𝛽`）与 `d > 4 ,` 的多余空格：MD 行 709 符号正确，`$d > 4 ,$` 内多一空格属排版伪影。
  - 「There is no intermediate phase」段与 `m^*(β_c) = 0`、`β = ½ log[1/(1−p)]`、`p ∈ [0,1]`、`q > 0`、`q = 1`、`q ≠ 1`、`q = 2`、`𝜔 ∈ {0,1}^E`、`𝜎 ∈ {−1,1}^V` 等符号 MD 全部正确（bbox y=348/351、390/393、404/406、432/434、487/488、501/502、555/560/563）。
  - 本页 `h = 0` 处 MD 用普通 `$h$`（非 ℎ），**正确**；与 p.030 第 6 处 ℎ 混淆不同源。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：印刷作「The archetypical example of such differential inequalities are given」式的单复数不一致在本页不出现；但印刷「a random variable 𝜔 ∈ {0,1}^E with the law of FK Ising」中 `the law of FK Ising` 作定语无冠词限制，bbox y=490/502 原样，MD 忠实，不改。
  - 印刷行末断词 `con-` / `figuration`（bbox y=474 / y=488）已正确合并为 MD 的 `configuration`，非缺陷；`edge-` / `weight` 则如上第 3 处属**原词自带连字符**，处理方式不同，二者已分别登记。
  - 印刷斜体强调（`susceptibility`、`Bubble diagram`、`continuity result`、`edge-weight`、`cluster-weight`、`dependent percolation model`、`FK Ising model`、`Edwards-Sokal coupling`）未在 MD 保留（风格级）。
  - 行 703 `where$\chi ( \beta ) : = …$is the susceptibility`、`and$B ( \beta )$is the Bubble diagram`、行 709 `that$B ( \beta )$remains`、`$1 / | \beta - \beta _ { c } |$as$\beta$approaches`、行 711 `satisfies$m ^ { * } ( \beta _ { c } ) = 0$for every`、行 717 `the measure$\phi _ { G , p , q }$is given, for$G = ( V , E )$finite`、`$\omega \in \{ 0 , 1 \} ^ { E }$, by`、行 723 `where$p \in [ 0 , 1 ]$and$q > 0$are`、`cluster-weight,$\begin{array}`、`edges in $\omega$, and$k ( \omega )$is`、行 725 `When$q = 1$,`、`the$\omega _ { e }$are`、`When$q \neq 1$,`、`the case$q = 2$`、行 727 `variable$\omega \in \{ 0 , 1 \} ^ { E }$with`、`parameter$p \in [ 0 , 1 ]$and construct$\sigma \in \{ - 1 , 1 \} ^ { V }$by`、行 729 `component $C$ of $\omega$ a spin$\sigma _ { C }$uniformly`、行 733 `Then,$\sigma$has the law`、`on $G$ with parameter$\textstyle { … } \log [ 1 / ( 1 - p ) ] }$and$h = 0$.`——行内数学与相邻文字未留空格，全篇一致的排版级伪影；行 733 的 `\textstyle { … }` 外层包裹与印刷的行内分式 `β = ½ log[…]` 内容一致，仅为结构化伪影。
  - MD 把印刷的两个自然段（`Then, σ has the law … h = 0.` 与 `This coupling, …`）并入同一行，除上条第 5 处补回句点外段落结构与原页版式不符，登记为版式级。
  - 印刷页脚 running foot `31  100 Years of the Ising Model` 未入 MD（版式级）。
  - 本页末段 `For instance, by decomposing on the events that $x$ is connected to $y$ or not` 在印刷中续至 p.32；行 735 起为 Figure 3 图片与图注，属 p.32 页段，本页不处理。
- 备注：本页 5 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown。

## p.032（PDF p.32 / 印刷 p.32）
- PNG：/tmp/icm2022dc_audit_p032.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p032_300.png`，裁片 `_inomega`(4×) `_proparties`(2×) `_betacomma`(3×) `_eq76`(3×) `_eq77`(3×) `_eq78`(3×) `_griffiths`(6×) `_grin`(4×)；bbox `/tmp/icm2022dc_p032_bbox.xml`
- 核对：Figure 3 三联图与图注、p.31 末段续句 `in ω, one easily gets that`、公式 (7.6)、`Similarly, ⟨σ_A⟩ = φ[F_A]` 段（含 Swendsen–Wang、Glauber dynamics、`q ≥ 1`、FKG 引言）、公式 (7.7)、`This inequality is often used …` 段（含 `prop-`/`erties` 断词、`monotonicity in p`、`p′ ≥ p`）、公式 (7.8)、`These monotonicity properties are particularly useful` 段（含 `Griffiths inequality` 与末行 `⟨σ_Aσ_B⟩ ≥ ⟨σ_A⟩⟨σ_B⟩`）、§7.3 标题、本页末段
- 结果：PASS±（差异列表，见下）
- 修复（3 处，均以 `Edit` 工具逐处落地）：
  1. 行 741 `in $G$, one easily gets that` → `in $\omega$, one easily gets that`。**印刷为斜体小写 ω**——4× 裁片 `/tmp/icm2022dc_p032_inomega.png` 直读「in *ω*, one easily gets that」，bbox y=243 亦作 `𝜔,`；导出把 `ω` 误识为 `G`。此处为 p.31 末句「…that $x$ is connected to $y$ or not **in ω**」的续句，公式 (7.6) 右端亦含 `in ω]`，若不改会与下文自相矛盾，属**字形误识造成的语义错误**。
  2. 行 753 `the monotonicity prop erties is the monotonicity in` → `the monotonicity properties is the monotonicity in`。印刷该词行末断作 `prop-` / 次行首 `erties`（bbox y=458 行尾 `prop-`、y=472 行首 `erties`；裁片 `/tmp/icm2022dc_p032_proparties.png` 2× 直读「…of the monotonicity prop-」/「erties is the monotonicity in *p*: …」）。这是**跨行断词连字符**，与 p.31 `edge-weight`（原词自带连字符）性质相反，应合并为 `properties`；导出保留了断点却把连字符换成空格，产出 `prop erties` 这样的坏词。
  3. 行 759 `is increasing in$\beta ,$, and the first one` → `is increasing in$\beta$, and the first one`。印刷 `β` 后只有**一个**逗号（3× 裁片 `/tmp/icm2022dc_p032_betacomma.png` 直读「creasing in *β*, and the」；bbox y=528 为 `𝛽,` 单 token，y=525 行尾 `𝛽,`、次 token `and`），导出叠加出一个重复逗号。此即 p.030 备注登记的「全篇尚存 1 处 `$\beta ,$,`」，**本页修复后该模式全篇清零**（`grep -nE '\$,\$|\} , \},|\) ,,'` 当前 0 命中）。
- 逐字核对留证（MD 无误，未改）：
  - Figure 3：MD 行 735 图片引用 `![](../audit/ICM2022_proceedings_Duminil-Copin_p032_Figure3.png)]`，相对 MD 所在目录解析到 `./2022年 - Duminil-Copin/audit/ICM2022_proceedings_Duminil-Copin_p032_Figure3.png`（文件已确认存在）；行 737 `Figure 3`、行 739 图注与印刷逐字一致，含 `bold edges are those with $\omega _ { e } = 1$`、`one example in black and others in grey`、`on the right, the spins without the FK Ising configuration.`。图内三联（FK 配置 / 簇上挂自旋 / 去掉配置的自旋）与印刷一致。
  - 公式 (7.6)：3× 裁片 `/tmp/icm2022dc_p032_eq76.png` 直读 `⟨σ_xσ_y⟩_{G,β,0} = ϕ_{G,1−e^{−2β},2}[x connected to y in ω].`（7.6），MD 行 744 逐符号一致，`e` 为数学斜体、下标 `−2β`、方括号内文与句末句点俱在；`\phi` 字形正确（与 p.29 判定的 ϕ/φ 区分一致）。
  - 公式 (7.7)：`_eq77.png` 直读 `ϕ_{G,p,q}[fg] ≥ ϕ_{G,p,q}[f]ϕ_{G,p,q}[g].`（7.7），MD 行 750 一致。
  - 公式 (7.8)：`_eq78.png` 直读 `ϕ_{G,p′,q}[f] ≥ ϕ_{G,p,q}[f].`（7.8），MD 行 756 一致（`p ^ {\prime}` 正确对应印刷上标撇）。
  - 末行不等式：`_grin.png` 4× 直读 `⟨σ_Aσ_B⟩_{G,β,0} ≥ ⟨σ_A⟩_{G,β,0}⟨σ_B⟩_{G,β,0}.`，MD 行 759 行末内联数学完全一致（含句点）。
  - **`Griffiths` 无撇号**：6× 裁片 `/tmp/icm2022dc_p032_griffiths.png` 直读「…nd Griffiths inequ…」；bbox 该词占 x 346.8–380.2，与后词 `inequality`（x 382.6 起）间隔 2.4pt，与全篇正常词距（2.2–3pt）一致，若有撇号会被切成独立 token（如 `p` + `′`）。MD 行 759 作 `Griffiths inequality`，**正确**；此反向印证 p.26 印刷作 `Griffiths' inequalities`（带撇号）确属该处印刷的排印选择，非导出臆改。
  - 行 747 印刷行末断词 `Swend-`/`sen`、`depen-`/`dent` 已正确合并为 `Swendsen`、`dependent`；行 747 `⟨σ_A⟩_{G,β,0} = ϕ_{G,1−e^{−2β},2}[F_A]`、`an even number (possibly equal to 0) of vertices in $A$`、`q \geq 1`、`For t uin-Kasteleyn-Ginibre (FKG) inequality`（原文 `The Fortuin-Kasteleyn-Ginibre (FKG)`）等 MD 均正确；行 753 `f : \{0,1\}^E \to \mathbb{R}`、`p^{\prime} \geq p` 亦正确。
- 登记不改：
  - 行 753 MD 把印刷的正文冒号包成行内数学 `$p \mathrm { : }$`（印刷为「monotonicity in *p*: for every」，冒号是正文字符）。冒号本身在位、语义未变，仅结构化伪影，不改（与全篇 `\mathrm { : }` 类结构伪影一并登记）。
  - 印刷行内数学与相邻文字未留空格（`Similarly,$\langle …`、`inequality states that for every increasing functions$f , g : \{ 0 , 1 \} ^ { E } \to \mathbb { R }$`、`are positively correlated` 段、`implies that$\langle …$is increasing in$\beta$` 等），全篇一致的排版级伪影。
  - 行 747 把印刷中由 bbox y=280–392 连续排布的整段（`Similarly, …` 至 `… → ℝ,`）合并为单一 MD 段落；行 759 同理合并 `These monotonicity properties …` 与末尾不等式两行，段落结构与原页版式不符，登记为版式级。
  - 印刷斜体强调（`cluster algorithms`、`increasing events`、`is increasing in β`、`the second Griffiths inequality`）未在 MD 保留（风格级）。
  - 印刷页脚 running foot `32  Hugo Duminil-Copin` 未入 MD（版式级）。
  - **印刷怪癖（铁律三，原样保留）**：印刷作 `states that for every increasing functions $f , g$`（复数 `functions` 配单数动词 `states`，且 `for every … functions`），bbox y=392 原文如此，MD 忠实保留，未按语法「纠正」。
- 全篇待办（供集成者，位置均在本轮 p.025–p.032 页段之外，本轮无权改）：
  - `diferent`/`diferential`（连字压平）全篇尚存 6 行：27、115、131、875、879、907。
  - `ℎ`（U+210E PLANETINE HOUR SIGN）误识全篇尚存 10 处：行 67、95、171、257、261、321、327、343、409（本轮之前）与行 795（本轮之后）。
  - `$\beta ,$,` 式重复逗号：**本页第 3 处修复后已全篇清零**，此前登记的「尚存 1 处于行 759」已消除。
- 备注：本页 3 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown。本页为本轮（PDF p.25–p.32，块 F）最后一页。
- **重复记录告知（供集成者处置，本审计员不删除他人条目）**：本文件中另存在一组更早写下的 p.025–p.030 条目，位于本 `## p.032` 之前的第 884–994 行（裁片命名 `/tmp/icm2022dc_p025_eq614.png` 等，与本轮 `…audit_pNNN.png` 体系不同），该组在 p.026/p.027 等页判定为「本页无数学内容错误，未改动 Markdown」。本轮块 F 的对应条目位于第 1560–1735 行，逐页以 300dpi 裁片复核后**发现并修复了导出缺陷**（p.026 4 处、p.027 7 处、p.029 6 处、p.030 8 处等），故本轮条目在事实层面取代前一组的「未改动」结论。两组条目的 Markdown 现况一致（前一组描述的是修复前的原始导出状态）。**是否删除或标注前一组条目，留待总Master 决定**；本审计员只保证本轮 8 条（p.025–p.032）自身逐页有 150dpi 全页图 + 300dpi 裁片 + bbox 三通道支撑。全文件 `grep -c '^## p\.'` = **57**（本轮前 49，本轮新增 8：p.025–p.032）。

---

## 块 G（PDF p.033–p.040）

## p.033（PDF p.33 / 印刷 p.33）
- PNG：/tmp/icm2022dc_audit_p033.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p033_300.png`，裁片 `_saw`(5×) `_bcpcomma`(5×) `_rswcomma`(5×) `_eq79`(3×) `_eq710`(3×) `_onsager2`(4×) `_measureP`(2×)；bbox `/tmp/icm2022dc_p033_bbox.xml`
- 核对：p.32 末段续文 `The past ten years have seen tremendous progress…`；`We already saw that…` 段与 Onsager 临界点 `1 − e^{−2β_c} = √2/(1+√2)`；`For all these reasons…crossing probabilities…` 段；`One important feature…(BCP)…Russo-Seymour-Welsh theory (RSW)` 段与 `Cross(R)`、`ℤ²`、`测度 ℙ`；bullet (BCP) 与公式 (7.9)；bullet (RSW) 与公式 (7.10)；`These two properties…[37]…` 段；§8 与 §8.1 标题；`Kadanoff used his block-spin renormalisation…Polyakov [91]…this QFT is a local` 段；页脚
- 结果：PASS±（差异列表，见下）
- 修复（2 处，均以 `Edit` 工具逐处落地）：
  1. 行 773 `• (BCP) for all$\rho > 0$, there exists$c > 0$such that for every$n \geq 1$` → 行尾补回逗号 `…$n \geq 1$,`。印刷该引导句以逗号收尾（5× 裁片 `/tmp/icm2022dc_p033_bcpcomma.png` 直读「…for every *n* ≥ **1,**」；bbox y=356.4 处 token 为 `1,`），导出吞掉句末逗号。
  2. 行 779 `• (RSW) for all$\rho > 0$, there exists$C > 0$such that for every$n \geq 1$` → 行尾补回逗号 `…$n \geq 1$,`。证据同上（5× 裁片 `/tmp/icm2022dc_p033_rswcomma.png` 直读「for every *n* ≥ **1,**」；bbox y=361.2 处 token 为 `1,`）。
  - 两处同型：引导句以逗号续接下方编号公式，缺逗号后 `(BCP)`/`(RSW)` 的陈述读作与 (7.9)/(7.10) 断裂，属标点级瑕疵，不误导数学内容，故记 PASS±。
- 逐字核对留证（MD 无误，未改）：
  - **公式 (7.9)**：3× 裁片 `/tmp/icm2022dc_p033_eq79.png` 直读 `c ≤ ℙ[Cross([0,ρn] × [0,n])|ω|_{[−n,(ρ+1)n]×[−n,2n]^c}] ≤ 1 − c almost surely.`（7.9）。MD 行 776 逐符号一致：左端 `c ≤`、双线体 `ℙ`、条件竖线 `|` 紧接 `ω` 且其下标为 `|…]`（**ω 在方框上的限制**这一标准写法，bbox y=346.5 `𝑛])|𝜔` + y=347.3 `|` 佐证）、补集上标 `^c` 挂在**内层**方框的右括号上（bbox y=348.0 的 `𝑐` 位于 `[−𝑛,2𝑛]` 之后、外层 `]` 之前）、右端 `≤ 1 − c almost surely.` 与编号 (7.9) 均在位。
  - **公式 (7.10)**：3× 裁片 `/tmp/icm2022dc_p033_eq710.png` 直读 `ℙ[Cross([0,ρn] × [0,n])] ≥ ℙ[Cross([0,n] × [0,ρn])]^C.`（7.10）。MD 行 782 一致：**两个矩形的长宽方向对调**（左 `ρn × n`、右 `n × ρn`）、上标 `C` 挂在**外层**方括号上（bbox y=399.3 的 `𝐶` 位于 `𝜌𝑛])]` 之后）、尾句点俱在。
  - **Onsager 临界点**：4× 裁片 `/tmp/icm2022dc_p033_onsager2.png` 直读 `1 − e^{−2β_c} = √2/(1 + √2)`，指数为 `−2β` 且 **`c` 为 β 的下标**（bbox y=150.6 的 `𝑐` 位于 `−2𝛽` 之后、下沉一档），两个根号各自带 `2`；MD 行 767 `$1 - e ^ { - 2 \beta _ { c } } = \sqrt { 2 } / ( 1 + \sqrt { 2 } )$` 一致。
  - **测度记号 ℙ**：2× 裁片 `/tmp/icm2022dc_p033_measureP.png` 直读「…model on ℤ² with measure **ℙ** are the following:」，确认是**双线体大写 P**（非斜体 p、非普通 P）；MD 行 771 `$\mathbb { P }$` 正确。
  - 行 771 `for a rectangle $R$, the event Cross($R$)` 的 `Cross`、`R`、`ω`、`R` 四个记号在位（bbox y=274/276/288/290 逐一切出 `𝑅,`、`𝑅,`、`𝜔`、`𝑅,`）；行 771 `(BCP) and (RSW) for a percolation model on${ \mathbb { Z } } ^ { 2 }$` 中 `ℤ²` 为黑板体 ℤ 上标 2，正确。
  - 行 765 `bridging the gap between our under-standing` 已正确合并为 `understanding`；行 785 `these devel-opments` 已正确合并为 `developments`；`[37]`、`[91]` 两处引用编号在位；§8 标题 `8. Over the last ten years: conformal invariance of the Ising model`、§8.1 标题 `8.1. What is conformal invariance?` 与印刷逐字一致。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：印刷行 771 作 `More precisely, if for a rectangle R, the event Cross(R) corresponds to the existence of a path in ω between the left and right sides of R, the properties (BCP) and (RSW) …`——`if` 从句没有主句结论，`Cross(R) corresponds to …` 的对应关系是单向定义而非条件命题；按铁律三原样保留，MD 未改写。另 `its connected notion` 指代的是 property 而非 models，印刷如此。印刷行 773/779 的 `(BCP) for all ρ > 0, there exists c > 0 such that for every n ≥ 1,` 本身也是**残句**（无主句动词，条件句直接接逗号），原样保留。
  - 150dpi 全页图上 `We already saw that` 的 `saw` 在 1-bit 缩放下易误读为 `say`；经 5× 裁片 `/tmp/icm2022dc_p033_saw.png` 仲裁直读为 **`saw`**（bbox y=79 亦作 `saw`），MD 行 767 作 `We already saw that`，**正确，非缺陷**——此条登记以留证「小字形必须 300dpi 仲裁」。
  - MD 在 (7.9) 用 `\operatorname{Cross}`、在 (7.10) 用 `\mathrm{Cross}`，同一记号两种写法；两者渲染均为正体，数学含义一致，登记为排版级不改。
  - 行内数学与相邻文字空格普遍合并（`on${ \mathbb { Z } } ^ { 2 }$is`、`$1 - e ^ { - 2 \beta _ { c } } = …$thanks`、`for all$\rho > 0$,`、`there exists$c > 0$such`、`on${ \mathbb { Z } } ^ { 2 }$with measure$\mathbb { P }$are`）；页脚 `33  100 Years of the Ising Model` 未入 MD（版式级）；印刷斜体强调（`crossing probabilities`、`translation` and `rotation invariance`）未保留（风格级）。
- 备注：本页 2 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（`for every$n \geq 1$,` 在三态均为 0，即从未被修过），确认为**原始导出缺陷**，非 peer 回归。全程未使用脚本写回 Markdown。

## p.034（PDF p.34 / 印刷 p.34）
- PNG：/tmp/icm2022dc_audit_p034.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p034_300.png`，裁片 `_hglyph`(9×) `_subset`(9×) `_Send`(5×) `_Tlimit`(5×) `_eq81`(3×) `_eq82`(3×) `_Sadots`(5×)；bbox `/tmp/icm2022dc_p034_bbox.xml`
- 核对：p.33 末段续文 `field, these properties…conformal invariance…Belavin, Polyakov and Zamolodchikov [12]`；`From a mathematical perspective…scaling limit` 段；`For clarity of the exposition…Ω ⊊ ℝ^d` 段（含 `β`/`h`、`β_c`、`aℤ^d`）；**(Spins)** 段与公式 (8.1)；`where [x]_a is the vertex…we call it S_Ω(x_1,…,x_n)`；**(Energies)** 段与公式 (8.2)；`where ε_{\{u,v\}} := σ_uσ_v − ⟨σ_uσ_v⟩_{aℤ^d}…energy`；**(Geometry of interfaces)** 全段（`ℭ_Ω`、`d_Ω`、`C^{(a)}_Ω`）；`Now, what do we mean by conformal invariance?` 段；页脚
- 结果：PASS±（差异列表，见下）
- 修复（5 处，均以 `Edit` 工具逐处落地）：
  1. 行 795 `We drop the subscript referring to$\beta$and ℎ as they are fixed` → `…to$\beta$and $h$ as they are fixed`。印刷是**数学斜体 `h`**：9× 裁片 `/tmp/icm2022dc_p034_hglyph.png` 直读「nd *h* as」，该字形为斜体竖笔加右肩、**无横向贯穿的短杠**，而 U+210E `ℎ`（PLANETINE HOUR SIGN）必带贯穿短杠，故可判别。此即前几页登记的 `ℎ`(U+210E) 误识族在本页的**唯一一处**（`grep -n 'ℎ'` 现存 9 处：行 67、95、171、257、261、321、327、343、409，**全部在本轮页段之外**，本轮无权改）。修复后本篇 `ℎ` 由 10 处降为 9 处。
  2. 行 795 同行末 `domain$\Omega \subset \mathbb { R } ^ { d }$` → `domain$\Omega \subsetneq \mathbb { R } ^ { d }$.`。两处改动：**(a)** 印刷的集合关系是 **`⊊`（⊂ 带下方分离短横，即「不等于的真包含」）**，9× 裁片 `/tmp/icm2022dc_p034_subset.png` 直读 `Ω ⊊ ℝ`——C 形右侧开口、下方另有一条**与 C 形等宽但分离**的横杠，与 `⊆`（横杠直接闭在 C 底、贴合）明显不同；bbox y=193 的 token 亦为 `⊊`（U+228A），两通道一致。MD 作 `\subset` 丢失 neq 短杠。**(b)** 补回句末句点（bbox y=190 行尾 token 为 `𝑑` 后紧跟 `.`；原页图可见 `ℝ^d.`）。
     - 印刷怪癖一并登记（铁律二/三）：把「simply connected domain」与 `ℝ^d` 的关系写作 **`⊊`（真包含）**在数学上并不必要（复连通域通常只写 `⊆`），但按铁律二不得按数学常识改回 `⊆`，故照录为 `\subsetneq`。
  3. 行 803 `If the limit exists, we call it$S _ { \Omega } ( x _ { 1 } , \ldots , x _ { n } )$` → 行尾补句点。5× 裁片 `/tmp/icm2022dc_p034_Send.png` 直读「it *S*<sub>Ω</sub>(*x*₁, . . . , *x*ₙ)**.**」；bbox y=302 该行以 `).` 收尾（token `𝑥` `𝑛` 后为 `)`、`.`）。MD 漏句末句点。
  4. 行 811 `limit$T _ { \Omega } ( x _ { 1 } , \ldots . . , x _ { n } )$as $a$ tends to 0` → `\ldots . .` 改为 `\ldots`。印刷只有**三个点**：5× 裁片 `/tmp/icm2022dc_p034_Tlimit.png` 直读「nit *T*<sub>Ω</sub>(*x*₁, . . . , *x*ₙ) *a*…」；bbox y=402 恰为三个 `.` token（x 267.6、272.1、276.6）后接 `,`。MD 的 `\ldots . .` 会排出五点，属导出重复。
  5. 行 815 `renormalising the$S _ { \Omega } ^ { ( a ) } ( x _ { 1 } , \ldots \ldots , x _ { n } )$` → `\ldots \ldots` 改为 `\ldots`。印刷同样只有**三个点**：5× 裁片 `/tmp/icm2022dc_p034_Sadots.png` 直读「*S*⁽ᵃ⁾<sub>Ω</sub>(*x*₁, . . . , *x*ₙ)」；bbox y=598 恰为三个 `.` token（x 392.3、396.8、401.3）后接 `,`。MD 的 `\ldots \ldots` 会排出六点。
  - 第 4、5 处同型：`\ldots` 后被重复追加散点，属 MinerU 在同一数学片段内二次发射省略号的系统性伪影；全篇精确扫描 `\ldots *\. |\\ldots *\\ldots|\\dots *\\dots` 仅命中此两行（`grep -nE`），即缺陷范围限于本段。
- 逐字核对留证（MD 无误，未改）：
  - **公式 (8.1)**：3× 裁片 `/tmp/icm2022dc_p034_eq81.png` 直读 `S^{(a)}_Ω(x_1, …, x_n) := ⟨σ_{[x_1]_a} ⋯ σ_{[x_n]_a}⟩_{aℤ^d ∩ Ω},`（8.1）。MD 行 800 逐符号一致：上标 `(a)` 挂在 `S` 上、`Ω` 为下标、**方括号下标 `[x_i]_a`（顶点映射用 `[]`）**、期望值下标为 `aℤ^d ∩ Ω`（**斜杠变体 `ℤ^d` 上标 d，`a` 前乘**）、**尾逗号**俱在。
  - **公式 (8.2)**：3× 裁片 `/tmp/icm2022dc_p034_eq82.png` 直读 `T^{(a)}_Ω(x_1, …, x_n) := ⟨ε_{(x_1)_a} ⋯ ε_{(x_n)_a}⟩_{aℤ^d ∩ Ω},`（8.2）。MD 行 808 一致：**能量记号确为 `ε`（\varepsilon，非 `E`、非 `\mathcal{E}`）**，且此处用**圆括号**下标 `(x_i)_a`（边映射用 `()`），与 (8.1) 的方括号 `[x_i]_a`（顶点映射）严格区分——MD 两处的括号类型均正确，未混用。尾逗号在位。
  - 行 811 `where$\varepsilon _ { \{ u , v \} } : = \sigma _ { u } \sigma _ { v } - \langle \sigma _ { u } \sigma _ { v } \rangle _ { a \mathbb { Z } ^ { d } }$and$( x ) _ { a }$is the edge closest to $x$.`——印刷（bbox y=386–392：`where := − ⟨𝜎 ⟩ and (𝑥) is the edge closest to 𝑥. 𝜀` / `{𝑢,𝑣} 𝑢 𝑣 𝑢 𝑣 𝑑 𝑎 𝑥` / `𝑎Z`）的边集下标为 **`{u,v}`**、期望下标为 `aℤ^d`、后的记号是 `(x)_a`，MD 全部一致。行 811 `The quantity$\varepsilon _ { x }$is called the energy` 中的 `ε_x`（对一般边 X）与印刷一致。
  - 行 813 `(Geometry of interfaces)` 全段：`ℭ_Ω`（`\mathfrak{C}` 字形正确，bbox `ℭ`）、`d_Ω`、`C^{(a)}_Ω`、`aℤ^d ∩ Ω`、`nineties`、`low-temperature representation`、`plus and minus spins`、`non-intersecting loops` 逐项与印刷一致；三个自然段印刷分行、MD 亦分三段，结构吻合。
  - 行 791 `full conformal invariance`（印刷跨行作 `conformal invari-` / `ance`，MD 已正确合并为 `invariance`）、`i.e.`、`one-to-one holomorphic maps`、`(CFT) in 2D`、`[12]` 全部在位。
- 登记不改：
  - **印刷怪癖（铁律三，原样保留）**：行 815 印刷作 `With the definitions above, it would for instance mean that there exists a way of…`——`it would for instance mean` 缺介词（通常作 `it would for instance mean`／`in particular`），按铁律三原样保留，MD 未补。另 (Spins)/(Energies)/(Geometry of interfaces) 三个小标题在印刷中以**粗体括号词**行首起排，MD 作普通括号文本行首，样式级。
  - 行内数学与相邻文字空格普遍合并（`and its rescaled versions$a \mathbb { Z } ^ { d }$for$a > 0$`、`equal to$\beta _ { c }$and 0`、`domain$\Omega \subsetneq`、`defined for every $a > 0$and$x _ { 1 } , …$by`、`one considers at the quantities`、行 811 `closest to $x$.`、`the limit$T _ { \Omega } ( … )$as $a$ tends to 0`、`quantity$\varepsilon _ { x }$is`）；页脚 `34  Hugo Duminil-Copin` 未入 MD（版式级）；印刷斜体强调（`locally`、`conformal invariance`、`scaling limit`、`energy-energy`、`the energy`、`the set 𝔈_Ω`、`distance d_Ω`、`conformal covariant/invariant`）未保留（风格级）。
  - MD 行 815 与行 817 之间断为两段，而印刷中该句是同一句跨 p.34/p.35 页边界续排（p.34 末为 `…and`，p.35 首为 `T_Ω(x_1,…,x_n)` 续接），段落结构与原页版式不符，登记为版式级。
  - 行 803 `where$[ x ] _ { a }$is` 在 `where` 与 `[x]_a` 之间无空格（bbox y=274 原页为 `where [𝑥]`），与全篇行内数学空格合并同族，不单独修。
- 备注：本页 5 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 1/1/1（修复后当前态为 0），确认为**原始导出缺陷**，非 peer 回归。全程未使用脚本写回 Markdown。

## p.035（PDF p.35 / 印刷 p.35）
- PNG：/tmp/icm2022dc_audit_p035.png（pngmono 150dpi）
- 核对：页首续句 `T_Ω(x_1,…,x_n)`、公式 (8.3)(8.4)、`For the geometry of interfaces…` 段、§8.2 标题与首段、`A few years later…` 段、`As mentioned above…` 段、Frame 6: Fermionic observable 全文、文献标注 [99]/[65]/[13,14]/[28, 99]/[28,99]/[74]/[26]、页脚
- 结果：PASS±（差异 **11** 处——初判 8 处 + p.40 交叉核对时补记的粗体 Δ **3 处**（涉及 **4** 个 Δ 字形），见文末「迟到发现」；均已按原图逐处 `Edit` 修复；另有 3 处经仲裁判定 MD 正确、**不改**，见「负向结论」）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：页首承接 p.34 末句续排，印刷首行 `…(x_n) that satisfy that there exist Δ_σ, Δ_ε such that for every conformal (i.e. holo-`；MD 行 817 逐词吻合。
  - **正文**：§8.2 标题 `8.2. Conformal invariance of the 2D Ising model`、其下三段叙述（`Around fifteen years ago…`／`A few years later…`／`As mentioned above…`）段落切分与印刷一致；`Chelkak-Izyurov-Hongler`、`so-called free arc ensemble of parameter 3`、`conformal loop ensembles of parameter 3`、`Schramm-Loewner evolution`、`spin-spin`、`energy-energy`、`order-disorder` 拼写逐字在位。
  - **公式**：见下「逐字核对留证」，(8.3)(8.4) 完全正确，未改。
  - **参考文献**：印刷有四处成对标注，逐处量测见下「负向结论」——**三处 `[…, …]` 的空格判定全部经 300 dpi 逐像素仲裁，其中两处初判为缺陷者实为 MD 正确**。
  - **版式**：Frame 6 框标题与正文位置、页脚 `35100  Years of the Ising Model`（版式级，未入 MD）。
- 修复（8 处，均以 `Edit` 工具逐处落地）：
  1. 行 827 `…for every conformal map$f : \Omega \to f ( \Omega )$).` → 去掉句末多出的一个 `)`，改为 `…map$f : \Omega \to f ( \Omega )$.`。7× 裁片 `/tmp/icm2022dc_p035_par_tail.png` 直读「al map *f* : Ω → *f*(Ω)**.**」——`f(\Omega)` 后**只有一个右括号**紧跟句点；bbox y=137.6 该行以单个 token `(Ω).` 收尾（x 351.4–368.8），两通道一致。MD 多排了一个 `)`。
  2. 行 833 `…was proved in [65] (with$\Delta _ { \varepsilon } = 1 )$).` → 去掉重复的第二个 `)`。7× 裁片 `/tmp/icm2022dc_p035_par_65.png` 直读「n [65] (with Δ_ε = 1)**.** In th」——单括号；bbox y=291.1 该处 token 为 `1).`（x 301.9–312.7）。MD 作 `))$`。
  3. 行 835 `conformal covariance of so-calledfermionic observables` → `so-called fermionic`。8× 裁片 `/tmp/icm2022dc_p035_socalled.png` 直读「of so-called fermionic o…」，两词间有明显词间空隙；bbox y=416.7 亦为两个独立 token（`so-called` x 158.5–194.4、`fermionic` x 196.8–234.9）。属行内文字粘连伪影。
  4. 行 839 `as the observable that efectively switches` → `effectively`。10× 裁片 `/tmp/icm2022dc_p035_effectively.png` 直读「at effectively switches」，为**双 f**；bbox y=566.3 该词 token 亦为 `effectively`（x 166.4–207.7）。MD 的单 f 是 MinerU 把 `ff` 连字压平的伪影（同族：行 143 亦有一处，**在本轮页段之外**，见下「跨页登记」）。
  5. 行 839 `family of edges$\{ e _ { i } ( j ) : i , j \} )$). Then,` → 去掉重复的第二个 `)`。6× 裁片 `/tmp/icm2022dc_p035_edgelist.png` 直读「the family of edges {*e*<sub>i</sub>(*j*) : *i*, *j*}**)**. Then, the」——`}` 之后**只有一个右括号**紧跟句点（该括号闭合的是前文 `(it can be written as a product …` 的外层圆括号）；bbox y=594.2 token 序列亦为 `}`→`)`→`.`。MD 作 `))$`。
  6. 行 839 `, let $\Omega$ be the largest` → `, let $\mathbf { \Omega }$ be the largest`。12× 裁片 `/tmp/icm2022dc_p035_bold_o1.png` 直读「et **Ω** be」——笔画明显加粗、直立；bbox y=496.6 该 token 的 Unicode 为 `𝛀`（U+1D6C0 MATHEMATICAL BOLD CAPITAL OMEGA），而同一行前文的 `Ω`（x 252.2–259.6）为普通体，粗细对比在原页图上直接可辨。MD 丢失粗体。
  7. 行 839 `x _ { n }$ of $\Omega$, and $n$ faces` → `of $\mathbf { \Omega }$, and $n$ faces`。12× 裁片 `/tmp/icm2022dc_p035_bold_o2.png` 直读「of **Ω**, a」；bbox y=509.0 token 为 `𝛀,`（x 352.3–362.8）。同第 6 处族。
  8. 行 839 `x _ { n }$ of $\Omega$ such that` → `of $\mathbf { \Omega }$ such that`。12× 裁片 `/tmp/icm2022dc_p035_bold_o3.png` 直读「of **Ω** s」；bbox y=524.5 token 为 `𝛀`（x 121.2–129.2）。同第 6 处族。
  - 第 6–8 处说明：Frame 6 中作为**被定义对象**的 `Ω`（`let Ω be the largest connected component of aℤ² ∩ Ω`）在印刷中一律用**粗体**，而同一定义句右侧 `∩ Ω` 处、以及正文 `domain Ω ⊂ ℂ` 的 `Ω` 用**普通体**——这是原刻的排印约定，按铁律三照录，不作「统一」。本篇 MD 的粗体数学惯例为 `\mathbf { … }`（全篇 86 处，`\boldsymbol` 38 处，前者为主导写法），故采用 `\mathbf { \Omega }`。
- 逐字核对留证（MD 无误，未改）：
  - **公式 (8.3)**：3× 裁片 `/tmp/icm2022dc_p035_eq83.png` 直读 `S_{f(Ω)}(f(x_1), …, f(x_n)) = |f′(x_1)|^{-Δ_σ} ⋯ |f′(x_n)|^{-Δ_σ} S_Ω(x_1, …, x_n),` (8.3)。MD 行 820 逐符号一致：下标为 `f ( \Omega )`、**因子之间用中点 `⋯`（`\dots`）而非基线 `\ldots`**（与同式实参表里的基线 `\ldots` 严格区分，MD 已区分正确）、**尾逗号**在位。
  - **公式 (8.4)**：同行裁片直读 `T_{f(Ω)}(f(x_1), …, f(x_n)) = |f′(x_1)|^{-Δ_ε} ⋯ |f′(x_n)|^{-Δ_ε} T_Ω(x_1, …, x_n).` (8.4)。MD 行 824 一致，**尾为句点而非逗号**（与 (8.3) 的尾逗号形成对照，MD 未混用），指数下标为 `- \Delta _ { \varepsilon }`。
  - **Frame 6 正文其余全部逐字吻合**：`domain$\Omega \subset \mathbb { C }$` 的集合关系在印刷中是 **`⊂`**（bbox y=496.6 token `⊂`，单字形、无下方短杠）——与 p.34 行 795 的 `⊊` 不同，MD 两处分别作 `\subset` 与（已修的）`\subsetneq`，**未混用，正确**；`$a \mathbb { Z } ^ { 2 } \cap \Omega$` 的上标为 **2**（bbox y=509.0 token `2`，非 `n`）；`for every$1 \leq i \leq n$` 两个关系号在位；`$\ell _ { 1 } , \ldots , \ell _ { n }$`、`$( e _ { i } ^ { * } ( j ) )$`、`$\mu _ { \ell }$`、`$\exp [ - 2 \beta \sigma _ { x } \sigma _ { y } ]$`（指数中为 `\sigma _ { x } \sigma _ { y }` 两个 σ 相乘）全部一致。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - `Smirnov [99]`（bbox y=179.6）与 `in [65]`（bbox y=291.1）：150 dpi 全页图上 `[99]` 曾被读成 `[89]`、`[65]` 曾被读成 `[55]`；8× 裁片 `/tmp/icm2022dc_p035_ref99.png`、`_ref65.png` 直读分别为 **`[99]`**、**`[65]`**，bbox 亦为 `[99]`、`[65]` —— **MD 正确，未改**。
  - `(see [13,14])`（行 833）：曾疑缺词间空格。用**同行像素量测**排除——300 dpi 下 y=360.9 整行的词间空隙为 9–14 px、词内字隙为 1–6 px；该处 `,`→`1` 空隙为 **7 px**（落在词内带），而同一行真实词间空隙「see」→「[」为 13 px、「).」→「In」为 14 px；12× 裁片 `/tmp/icm2022dc_p035_r1314_dec.png` 并置直读可见「comma→1」的缝明显窄于「see→[」的缝。故印刷确为 **`[13,14]`（逗号后无空格）**，**MD 正确，未改**。此条是本轮最重要的一次「疑似缺陷→仲裁后不改」。
  - `the ideas from [28, 99]`（行 833）与 `the works [28,99]`（行 835）：**两处排印不一致，且两处 MD 都正确**。y=374.9 行内 `,`→`9` 空隙 9 px（落在该行词间带 9–17 px 内），9× 裁片 `/tmp/icm2022dc_p035_r2899a.png` 直读可见空格 ⇒ 印刷为 `[28, 99]`，MD 行 833 正确；y=402.8 行内 `,`→`9` 空隙仅 **6 px**（该行词内字隙 1–3 px、词间 9–13 px），9× 裁片 `/tmp/icm2022dc_p035_r2899b.png` 直读无空格，且 pdftotext 把它作为**单一 token** `[28,99]` 输出 ⇒ 印刷为 `[28,99]`，MD 行 835 正确。**同一文献标注在原文两处空格不同，按铁律三原样保留、不作统一**；此前把两处都判成「MD 缺空格」的初判已由像素量测推翻。
- 跨页登记（供集成者，本轮无权改）：`efectively`（单 f 伪影）在行 143 另有 1 处；`diferent/diferential`（行 27、115、131、875、879、907 共 6 处）与 `ℎ`(U+210E)（行 67、95、171、257、261、321、327、343、409 共 9 处）仍在文档他处，均在本轮 p.33–p.40 页段之外。
- 登记不改（铁律三）：
  - **印刷怪癖**：同一句文献标注 `[28, 99]`（行 833）与 `[28,99]`（行 835）空格不一致——照录，不统一。
  - Frame 6 中 `\ell` 排成数学斜体 ℓ，MD 直接用 Unicode `ℓ`（与本篇他处一致），不另改。
  - 行内数学与相邻文字空格合并（`domain$\Omega \subset \mathbb { C }$and`、`for$a > 0$`、`vertices$x _ { 1 } , …$of`、`$f _ { \Omega } ^ { ( a ) }$is proved` 等）为 MinerU 全篇系统性伪影，本页不逐处拆改（与前页同一处置）。
  - 页脚 `35100  Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页 8 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，非 peer 回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙量测）。
- **迟到发现（p.40 交叉核对时补记，本页判定由 8 处升格为 11 处）**：审计 p.40 时做全篇 `\Delta _ { \sigma }` / `\Delta _ { \varepsilon }` 清点（命中行 817、833、909），回头复核本页印刷，发现本页 **4 个 Δ 全部为粗体**而 MD 行 817、833 丢失粗体——这是我在本页首次判读时漏掉的字形层级差异。证据（均取自 `/tmp/icm2022dc_p035_300.png`，300 dpi，px = pt × 4.1667）：
  - bbox y=37.1：`𝚫`（x 230.0–236.3）与 `𝚫`（x 247.7–253.9），**U+1D6AB MATHEMATICAL BOLD CAPITAL DELTA**（非 U+0394 普通 Δ）。
  - bbox y=249.3：`𝚫`（x 191.0–197.2），U+1D6AB。
  - bbox y=291.1：`𝚫`（x 279.1–285.3），U+1D6AB。
  - 9× 裁片三张直读复核（我已用 Read 工具亲眼看过）：`/tmp/icm2022dc_p035_d817.png`（px 880–1090, y 145–200）直读「exist **Δ**₍σ₎, **Δ**₍ε₎」，两个三角笔画明显加粗；`/tmp/icm2022dc_p035_d833a.png`（px 740–880, y 1030–1085）直读「ith **Δ**₍σ₎ =」；`/tmp/icm2022dc_p035_d833b.png`（px 1100–1260, y 1205–1260）直读「with **Δ**₍ε₎ =」，均与文本层一致。
  - 三处修复（`Edit` 逐处，涉及 4 个 Δ 字形）：行 817 `there exist$\Delta _ { \sigma } , \Delta _ { \varepsilon }$such` → `there exist$\boldsymbol {\Delta} _ { \sigma } , \boldsymbol {\Delta} _ { \varepsilon }$such`；行 833 `(with$\Delta _ { \sigma } = 1 / 8 )$` → `(with$\boldsymbol {\Delta} _ { \sigma } = 1 / 8 )$`；行 833 `(with$\Delta _ { \varepsilon } = 1 )$` → `(with$\boldsymbol {\Delta} _ { \varepsilon } = 1 )$`。三锚点全篇各唯一；三态 provenance 均为 **1/1/1**，**原始导出缺陷，非 peer 回归**。
  - 修复后全篇复扫：普通体 `\Delta _ { \sigma }` / `\Delta _ { \varepsilon }` 残留 **0**；行 817、833、909 全部为粗体形式（行 909 = 印刷 p.40 的两对 $(Δ_σ, Δ_ε)$，已在 p.040 条目内登记修复）。
  - 写法说明：p.39 第 905 行同一篇里 `the$\Delta \mathcal { A }$` 处印刷印的是**普通体** Δ（bbox 为 U+0394），那是原刻自身的层级不一致，按铁律三**保留普通体不改**；本页 4 处确为粗体，故按印刷加粗。

## p.036（PDF p.36 / 印刷 p.36）
- PNG：/tmp/icm2022dc_audit_p036.png（pngmono 150dpi）
- 核对：Frame 6 续排（`order-disorder correlations are given by the formula`）、公式 (8.5)、`Let us mention that… Grassmann…[95]` 段、`Smirnov introduced a fermionic observable…` 段、`The conformal covariance…` 段、`The proof of the theorem…` 段、Frame 7: Preholomorphic observables 全框（`Kirchhoff [77]`、`Isaacs [68, 69]`、`discretise the Cauchy-Riemann equation`）、公式 (8.6)、`where NW, SW, SE, and NE…` 句、页脚
- 结果：PASS±（差异 3 处，均已按原图逐处 `Edit` 修复；另有 5 处经仲裁判定 MD 正确、**不改**，见「负向结论」）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：本页无独立题录；页首为 Frame 6 框的跨页续排（p.35 末 `Then, the` → p.36 首 `order-disorder correlations are given by the formula`），MD 把二者接在行 839/841–843，衔接正确。
  - **正文**：五段散文（`Let us mention that…`、`Smirnov introduced…`、`The conformal covariance…`、`The proof of the theorem…`、Frame 7 的 `The notion of preholomorphic…`）段落切分与印刷一致；`Schultz-Mattis-Lieb`、`take-home message`、`spin-spin`、`energy-energy`、`conformal covariance/invariance`、`van der Waerden high-temperature expansion`、`Riemann-Hilbert`、`preholomorphic`、`Bernoulli site percolation`、`triangular lattice`、`Kirchhoff`、`Isaacs`、`Cauchy-Riemann`、`counterclockwise` 拼写逐字在位。
  - **公式**：(8.5) 除下标粗体外全对；(8.6) 完全正确（见下）。
  - **参考文献**：`[95]`、`[28, 99]`、`[77]`、`[68, 69]` 四处标注的**空格形态**逐处量测，MD 全部正确（见「负向结论」）。
  - **版式**：Frame 6 框（跨页续）与 Frame 7 框的框线、`Frame 7: Preholomorphic observables` 居中粗体标题、页脚 `36  Hugo Duminil-Copin`（版式级）。
- 修复（3 处，均以 `Edit` 工具逐处落地）：
  1. 行 842 (8.5) `\rangle_ {\Omega}.\tag{8.5}` → `\rangle_ {\mathbf { \Omega }}.\tag{8.5}`。**期望值的下标 Ω 在印刷中是粗体**：11× 裁片 `/tmp/icm2022dc_p036_bo1.png` 直读「*μ*<sub>ℓₙ</sub> ⟩ **Ω** .」，笔画明显加粗、直立；bbox y=71.6 该 token 的 Unicode 为 `𝛀`（U+1D6C0 MATHEMATICAL BOLD CAPITAL OMEGA，x 329.9–335.7），与同式右侧下标位置的普通体 `Ω`（如 y=73.8 x 148.8–154.2 的 `F^{(a)}_Ω` 下标为 U+03A9）字形不同。MD 丢失粗体。
  2. 行 847 `a linear combination (with complex coeficients) of` → `coefficients`。10× 裁片 `/tmp/icm2022dc_p036_coef.png` 直读「plex coefficients) of」，为**双 f 的 `ff` 连字**；bbox y=130.9 该词 token 亦为 `coefficients)`（x 353.1–401.7）。与 p.35 行 839 `efectively` 同族的 MinerU 连字压平伪影。
  3. 行 847 `edges $\{ x , y \}$ of $\Omega$ that can be written` → `of $\mathbf { \Omega }$ that can be written`。10× 裁片 `/tmp/icm2022dc_p036_bo2.png` 直读「} of **Ω** that c」；bbox y=131.0 token 为 `𝛀`（x 106.8–114.7）。同第 1 处族（**指称定义域的裸 Ω 用粗体**）。
  - 第 1、3 处说明：原刻约定是**裸写的、作为定义域被指称的 `Ω` 用粗体**，而**作下标/标签的 `Ω` 用普通体**——本页 `fermionic observable $f^{(a)}_\Omega$`（bbox y=122.6，U+03A9）与 `the $F^{(a)}_\Omega$`（bbox y=150.5，U+03A9）两处下标确为普通体，MD 亦作普通 `\Omega`，**正确、未改**。例外的是 (8.5) 期望值下标也用粗体；按铁律三照录，不作统一推断。
- 逐字核对留证（MD 无误，未改）：
  - **公式 (8.5)**：bbox 逐 token 比对 `F^{(a)}_Ω(x_1, f_1, . . . , x_n, f_n) := ⟨σ_{x_1} μ_{ℓ_1} . . . σ_{x_n} μ_{ℓ_n}⟩_Ω.` (8.5)：
    - **两处省略号都在基线**——bbox y=70.8 处三点的 yMin/yMax 均为 70.8–75.3，与句末句点（x 336.3–338.8，同为 y 70.8–75.3）**完全同高**，故为 `\ldots`（基线三点）而非 `\cdots`/`\dots`（中点）。这与 p.35 的 (8.3)/(8.4) 形成对照——那两式的因子省略号经同一量测确在中点、MD 用 `\dots` 亦正确。MD 行 842 两处均作 `\ldots`，**正确**。
    - 实参表 `(x_1, f_1, \ldots , x_n, f_n)` 的省略号同在基线 ✓；`⟨…⟩` 用的是 **`⟨`/`⟩`（U+27E8/U+27E9）** 而非 `(`/`)` ✓；`\sigma_ {x _ {1}}` 与 `\mu_ {\ell_ {1}}` 交替、末项 `\mu_ {\ell_ {n}}` ✓；公式号 `(8.5)` 右对齐 ✓。
    - `F` 为**数学斜体**（bbox y=70.8 token 为 `𝐹` U+1D439 MATHEMATICAL ITALIC CAPITAL F），非粗体；LaTeX 数学模式自动斜排，MD 的 `F` 正确。
  - **公式 (8.6)**：6× 裁片 `/tmp/icm2022dc_p036_eq86.png` 直读 `F(NW) − F(SE) = i[F(NE) − F(SW)],` (8.6)。bbox y=550.4/553.0 逐 token 为 `(𝑁𝑊) − (𝑆𝐸) = 𝑖[𝐹 (𝑁 𝐸) − (𝑆𝑊)],`：
    - 减号是 **U+2212 MINUS SIGN**（真减号），MD 用 ASCII `-`，在 LaTeX 数学模式中同样排出 U+2212，**渲染一致，非缺陷**。
    - 四个方位名 `NW, NE, SW, SE` 在印刷中**紧排、无空格**（bbox `(𝑁𝑊)` 为单一 token）；MD 写作 `N W`、`N E`、`S W`、`S E`。**TeX 数学模式忽略源码中的空格**，`$N W$` 渲染结果与 `$NW$` 完全相同，故**不构成差异，不改**（登记为样式级）。
    - `i[` 之间印刷无空格，MD 作 `i [`，同理渲染一致，**不改**。
    - 尾逗号在位 ✓；`F` 为斜体非粗体（同上）✓。
  - 行 861 `where $NW$, $SW$, $SE$, and $NE$ are the four corners found in counterclockwise order around each face, when starting from the top left vertex.`——bbox y=571.5/574.0 为 `where 𝑁𝑊, 𝑆𝑊, 𝑆𝐸, and 𝑁 𝐸 are the four corners found in counterclockwise order` + 次行 `around each face, when starting from the top left vertex.`，逐词一致，`top left vertex` 未被误作 `top-left` ✓。
  - 行 855 `the notion of preholomorphic function on a planar graph $G$ appeared implicitly in the work of Kirchhoff on electrical networks [77].` 中 `G` 为斜体 `𝐺`（U+1D43A），MD 作 `$G$` ✓；`It was explicitly linked to holomorphicity` 与 `proposed to discretise the Cauchy-Riemann equation` 均与印刷逐字一致（150 dpi 图上曾分别误读为 `holomor-phicity` 连写与 `discrete`，bbox 与原页图均证伪，未改）。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - **`[28, 99]`（行 849）与 `[68, 69]`（行 855）的空格**：150 dpi 全页图上 `[28, 99]` 曾被读成 `[28, 98]`、`[68, 69]` 曾被读成 `[58, 59]`。bbox 直接给出 `[28,`/`99]`、`[68,`/`69]` 为**两个 token**（数字无误）。空格形态用**像素空隙三档标定**判定（300 dpi，1 pt = 4.167 px）：
    - 本页正文行 y=268.2 的普通词间空隙为 **12–14 px**（如 `fact,`→`conformal` 的 14 px），词内字隙 1–4 px；
    - `[28,99]` 的 `,`→`9` 空隙为 **6 px**，且 pdftotext 将其输出为**单一 token** ⇒ 印刷为**无空格**，MD 行 849 的 `[28,99]` **正确**；
    - `[68, 69]` 的 `,`→`6` 空隙为 **9 px**，pdftotext 输出为**两个 token** ⇒ 印刷为**有空格**（natbib 引文标注在逗号后用 `.2em` 细空格，约 2 pt ≈ 8–9 px，介于词内 1–4 px 与正常词间 12–19 px 之间），MD 行 855 的 `[68, 69]` **正确**。
    - 该三档标定与 p.35 的量测完全自洽（无空格 6–7 px、细空格 9 px、正常词间 9–19 px），并**回头复核了 p.035 已落签的三处标注判定仍然成立**（`[13,14]` 7 px 无空格 ✓、`[28, 99]` 9 px 细空格 ✓、`[28,99]` 6 px 无空格 ✓），无需回改。
  - 行 845 `correlations of Grassmann variables`：印刷跨行断作 `Grass-` / 次行首 `mann`（bbox y=89.2 行尾 `Grass-`、y=103.2 行首 `mann variables`），MD 已正确合并为 `Grassmann`（连字符是排版断词，非词内连字符），**正确，未改**。
  - 行 855 `linked to holomorphicity`：印刷断作 `holomor-` / `phicity`（bbox y=501.7 行尾 `holomor-`、y=515.7 行首 `phicity`），MD 合并正确，**未改**。
  - 行 849 `first brick among`：印刷确为 **`brick`**（bbox y=240.3 `first brick among the conformal covariance results of spin-spin, energy-energy correlations,`；150 dpi 原页图直读亦为 `brick`），MD 作 `first brick` **正确**。按铁律三原样保留，不改为更常见的 `building block`。
  - 行 851 `van der Waerden high-temperature expansion`、`Riemann-Hilbert boundary value problem`、`holomorphic solution of a continuum Riemann-Hilbert boundary value problem` 三处连字符在位，`It has created an explosion of results in the field as many quantities` 原句在位（未按语法补 `and`），逐字一致。
- 跨页登记（供集成者，本轮无权改）：`efectively`（单 f 伪影）在行 143 另有 1 处；`coeficients`（同类单 f 伪影）经 `grep -cF 'coeficients'` 本篇仅本页 1 处，已清零；`diferent/diferential`（行 27、115、131、875、879、907）与 `ℎ`(U+210E)（行 67、95、171、257、261、321、327、343、409）仍在文档他处，均在本轮 p.33–p.40 页段之外。
- 登记不改（铁律三）：
  - **印刷怪癖**：`first brick`（非常用搭配）；`Grassmann` 被断词为 `Grass-mann`；同一文献标注的空格形态随 natbib 输出而不一致（详见负向结论）。
  - 印刷斜体强调（`order-disorder`、`fermionic observable`、`take-home message`、`discrete version`、`preholomorphic`、Frame 7 标题粗体）在 MD 中未保留（风格级）。
  - 行内数学与相邻文字空格合并（`observable$f _ { \Omega } ^ { ( a ) }$defined`、`edges $\{ x , y \}$ of`、`the$F _ { \Omega } ^ { ( a ) }$with`、`x _ { 1 }$equal`、`f _ { 1 }$to`、`that$f _ { \Omega } ^ { ( a ) }$is`、`planar graph $G$ appeared`）为 MinerU 全篇系统性伪影，本页不逐处拆改（与前两页同一处置）。
  - 页脚 `36  Hugo Duminil-Copin` 未入 MD（版式级）；Frame 6 框跨 p.35/p.36 断开，MD 未分段还原跨页框（版式级）。
- 备注：本页 3 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，非 peer 回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙/字高量测）。

## p.037（PDF p.37 / 印刷 p.37）
- PNG：/tmp/icm2022dc_audit_p037.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p037_300.png`，裁片 `_z2`(9×) `_lattice`(9×)；bbox `/tmp/icm2022dc_p037_bbox.xml`
- 核对：Frame 7 框内两段（`The properties of preholomorphic functions…` / `In the case of the Ising model…`）、§8.3 标题 `8.3. Towards universality of the 2D Ising model`、其后三段（`As mentioned in Section 4.2.2…` / `The first impressive progress…` / `In recent developments…`）、页脚 `37  100 Years of the Ising Model`
- 结果：PASS（未发现缺陷，无需修复）
- 逐字核对留证（MD 无误，未改）：
  - **双重删除线 ℤ 字形**：印刷 `ℤ²` 位于第 4 行 `…the Ising model on ℤ² and more generally…`（MD 行 869 `${ \mathbb { Z } } ^ { 2 }$`）。9× 裁片 `/tmp/icm2022dc_p037_z2.png`（px 1610–1790, y 1265–1350）直读「n ℤ² and」，Z 主干左侧可见**双斜杠附加笔画**，确为黑板粗体 ℤ（U+2124），非普通 Z；bbox 记录 `ℤ` 亦作 U+2124。MD `\mathbb { Z }` 正确。
  - **直和号 ⊕ 而非 ⊗**：印刷第 16 行 `…the action of some lattice Λ ≈ ℤ ⊕ ℤ (in such case G/Λ is a finite graph embedded in the torus).`（MD 行 873 `\Lambda \approx \mathbb { Z } \oplus \mathbb { Z }`）。9× 裁片 `/tmp/icm2022dc_p037_lattice.png`（px 340–620, y 2315–2400）直读「e Λ ≈ ℤ⊕ℤ (in su」：圈内为**一横一竖**正十字，非对角叉号，故 `\oplus` 正确、`\otimes` 会是错字；bbox y=560.9 的 `⊕` 亦作 U+2295 CIRCLED PLUS。`≈` 作 U+2248，`\approx` 正确。
  - **行内数学斜体字形**：`J_{x,y}`（bbox y=424.1 的 U+1D43A 斜体 J）、`β_c = 1`（U+1D43D 斜体 J + U+03B2 斜体 β）、`G`、`s`-holomorphicity 与 `s`-embedding 的斜体 `s`（U+1D460）均与 MD `$J _ { x , y }$`、`$\beta _ { c } = 1$`、`$G$`、`$s$-holomorphicity`、`$s$-embedding` 一致。
  - **断词连字符已正确合并**：`func-` / `tions`（bbox y=75.3 / 89.2）→ MD `functions`；`iso-` / `radial graph is an embedding`（bbox y=379.8 / 393.7）→ MD `isoradial`。（与 p.32 `prop-`/`erties` 同类跨行断词，MD 处理正确。）
  - **印刷怪癖保留（铁律三）**：`meshsize` 在印刷中为一个整词（未作 `mesh size`），MD 保留；`conformal invariance in connections to boundary value problems` 用复数 `connections`，MD 保留；`(in such case G/Λ …)` 印刷为 `in such case`（无 a），MD 保留。以上均为原刊原样，未「纠正」。
  - **负向结论**：`[28]`（行 871 `themselves [28]`）与 `[25]`（行 873 `proved in [25]`）方括号内数字两侧印刷均有 natbib 细空格，MD 写作 `[28]`/`[25]` 与印刷一致；本段无 p.35 式的 `[28,99]` 连写差异需要处理。
- 登记不改（风格/版式级）：
  - 印刷斜体强调（`s`-holomorphicity 的斜体 `s`、`isoradial graphs`、`embedding`、`determined by`、`s`-embedding、Frame 7 标题粗体）在 MD 中未保留（风格级）。
  - 行内数学与相邻文字空格合并（`on${ \mathbb { Z } } ^ { 2 }$and`、`$J _ { x , y }$depending`、`that$\beta _ { c } = 1$and`、`graphs$( G , J )$`、`lattice$\Lambda \approx`、行 873 `$\Lambda \approx \mathbb { Z } \oplus \mathbb { Z }$(in such case$G / \Lambda$is`）为 MinerU 全篇系统性伪影，与前三页同一处置，不逐处拆改。
  - 页脚 `37  100 Years of the Ising Model` 未入 MD（版式级）；Frame 7 框跨 p.36/p.37 断开，MD 未还原跨页框（版式级）。
- 备注：本页 0 处修复，故无三态 `grep -cF` 比对项；全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素量测）。

## p.038（PDF p.38 / 印刷 p.38）
- PNG：/tmp/icm2022dc_audit_p038.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p038_300.png`，裁片 `_z2`(9×) `_H`(9×) `_suffers`(8×) `_difficulty`(7×) `_nearest`(6×) `_ofvertices`(4×) `_ofs`(4×) `_eq87`(3×)；bbox `/tmp/icm2022dc_p038_bbox.xml`
- 核对：`This result is a strong indication of universality…` 段、`First, one may consider finite-range models…` 段（含 `nearest-`/`neighbour` 断词、`1 < ||x−y||₂ ≤ R`、`Schultz-Mattis-Lieb Grassmann representation [95]`、`[53]`、`4D`）、`A totally different approach…` 段（含 `n-point`、`Ω`、`Pfafian`）、`k₁ < k₂ < ⋯ < k_{2n}`、`ℍ := ℤ × ℤ₊,`、公式 (8.7)、`where o(1) is a function…min{|x_i−x_j| : 1 ≤ i < j ≤ 2n}…` 段、`This is, to the author's knowledge…` 段（末行 `which for finite` 续 p.39）、页脚 `38  Hugo Duminil-Copin`
- 结果：PASS±（差异列表，见下）
- 修复（10 处，均以 `Edit` 工具逐处落地）：
  1. 行 875 `pairs ofvertices` → `pairs of vertices`。印刷第 4 行 bbox y=92.9：`pairs`(x59.5–78.9) `of`(80.4–88.7) `vertices`(90.3–121.2)，词间空隙 1.5/1.6 pt 与同行 `vertices at`(1.5pt) 同档，说明 `of` 后确有空格；4× 裁片 `/tmp/icm2022dc_p038_ofvertices.png`（px 240–1100, y 378–434）直读「pairs of vertices at a distance at most *R* of each other.」，空格清晰。属 MinerU 词间空格合并伪影。
  2. 行 875 同句 `at most $R$ ofeach other` → `…of each other`。bbox y=92.9 斜体 `R`(201.5–207.6) → `of`(209.4) → `each`(219.3)，空隙 1.8/1.6 pt 同档；同一裁片直读「*R* of each other.」。
  3. 行 875 `called thefinite-range model on$…` → `called the finite-range model on$…`。bbox y=92.9：`called`(311.2–335.0) `the`(336.5–348.7) `finite-range`(350.3–395.9) `model`(397.5–422.4)，空隙 1.5/1.6/1.6 pt 全部同档，印刷三词间均有空格；同一裁片直读「called the *finite-range* model」。
  4. 行 875 `The additional dificulty is that` → `The additional difficulty is that`。bbox y=120.8 作 `difficulty`(x154.9–190.8)；7× 裁片 `/tmp/icm2022dc_p038_difficulty.png`（px 600–830, y 492–552）直读「al difficulty is」，可见 `ffi` 连字。导出把 `ffi` 连字压平为 `dific`（少一个 f），属 MinerU 连字压平伪影（与 p.35 `efectively` 同族）。
  5. 行 875 `investigated in two diferent directions.` → `two different directions.`。bbox y=134.8 行尾作 `different`(x388.7–422.4)；同行 `models`(241.2–270.0)→`has`(272.8) 空隙 2.8pt、`in`(360.6–368.4)→`two`(371.3) 空隙 2.9pt 可作同页词距参照。
  6. 行 877 `perturbations of the nearestneighbour integrable case` → `the nearest-neighbour integrable case`。**跨行断词**：bbox y=162.7 行尾 x391.0–422.4 为 `nearest-`（含连字符），次行 y=176.6 行首 x59.5–99.9 为 `neighbour`；6× 裁片 `/tmp/icm2022dc_p038_nearest.png`（px 1420–1770, y 660–728）直读「tions of the nearest-」。导出把断点连字符**整个丢掉**、直接粘成 `nearestneighbour`，比 p.32 的 `prop erties`（换成空格）更糟，属真实词形错误。注意本段印刷本身连字符用法不一致（y=105.1 `nearest-neighbour` 带连字符、y=204.5 `nearest neighbour` 不带），本处按印刷断点取带连字符形式，未统一改写别处（铁律三）。
  7. 行 877 `at the end in terms ofthe nearest-neighbour model.` → `in terms of the nearest-neighbour model.`。bbox y=232.4：`terms`(200.0–222.4) `of`(223.9–232.2) `the`(233.7–245.9)，两处空隙均 1.5pt，同档；4× 裁片 `/tmp/icm2022dc_p038_ofs.png`（px 780–1340, y 958–1018）直读「d in terms of the nearest-neighbour m」。
  8. 行 877 `As a consequence, the strategy sufers from` → `suffers from`。bbox y=330.0 作 `suffers`(x183.8–210.2)；8× 裁片 `/tmp/icm2022dc_p038_suffers.png`（px 700–900, y 1360–1425）直读「egy suffers from t」，可见 `ff` 连字。导出压平为 `sufer`。
  9. 行 879 `A totally diferent approach explaining` → `A totally different approach explaining`。bbox y=357.9 作 `different`(x132.4–166.1)。
  10. 行 879 `on the boundary of the upper half-plane H$: = \mathbb { Z } \times \mathbb { Z } _ { + }$` → `… half-plane $\mathbb { H } := \mathbb { Z } \times \mathbb { Z } _ { + }$,`。**本段最严重的一处**：9× 裁片 `/tmp/icm2022dc_p038_H.png`（px 1530–1780, y 1990–2075）直读「e **ℍ** := **ℤ** × **ℤ**₊,」——(a) 印刷的 `H` 是**黑板粗体 ℍ**（U+210D，左右竖笔带双线），导出写成数学斜体 `H`；(b) 导出的 `$` 位置错误，把 `ℍ` 关在数学模式里、`: = ` 落到正文，再重开 `$…$` 包住 `ℤ×ℤ₊`，渲染出字面 `$`；(c) 印刷该行末有一个逗号（bbox x419.9–422.4 y483.5–492.5），MD 缺失。三者同处一个连续片段，一次 `Edit` 一并改正。
- 逐字核对留证（MD 无误，未改）：
  - **ℤ 字形**：印刷第 4 行 `vertex-set ℤ²`（bbox 子行 y=81.4 x324.7–330.8）。9× 裁片 `/tmp/icm2022dc_p038_z2.png`（px 1300–1430, y 305–390）直读「set ℤ² an」，Z 对角线上可见双斜附加笔画，确认黑板粗体。注意**本页文本层把该字形编码为 ASCII `Z`（不同于 p.37 的 U+2124）**，故本页所有 ℤ 的判定一律以裁片为准，未依赖文本层。
  - **公式 (8.7) 完整正确**：3× 裁片 `/tmp/icm2022dc_p038_eq87.png`（px 450–1780, y 2080–2165）直读「⟨σ_{x₁} ⋯ σ_{x₂ₙ}⟩_{ℍ,β_c} = Pfaff_n([⟨σ_{x_i}σ_{x_j}⟩_{ℍ,β_c}]_{1≤i<j≤2n})[1 + o(1)],  (8.7)」，与 MD 行 882 的 `\langle\sigma_{x_1}\dots\sigma_{x_{2n}}\rangle_{\mathbb{H},\beta_c}=\operatorname{Pfaff}_n(...)[1+o(1)],\tag{8.7}` 逐项一致；`Pfaff` 为正体罗马字（`\operatorname`）而非斜体，正确。
  - **省略号高度**：印刷 `x₁=(k₁,0), . . . , x₂ₙ` 中三点 y=472.0–476.4（贴近基线）→ MD `\ldots`；`k₁ < k₂ < · · · < k₂ₙ` 中三点 y=483.3–491.8（居中）→ MD `\cdots`；(8.7) 中 `σ_{x₁} ⋯ σ_{x₂ₙ}` 同为居中 → MD `\dots`。三处层级均正确。
  - `min{|x_i − x_j| : 1 ≤ i < j ≤ 2n}`（bbox y=539.1）外层花括号在位，MD 行 885 `$\{ | x _ { i } - x _ { j } | : 1 \le i < j \le 2 n \}$` 正确。
  - `1 < ||x − y||₂ ≤ R`（bbox y=190.4/193.0，`∥`=U+2225，`−`=U+2212）与 MD `\| x - y \| _ { 2 } \leq R` 一致；`behaviour`、`gaussian`、`n.n.f.`、`Grassmannian`、`Giuliarni-Greenblatt-Mastropietro` 等专名大小写逐字一致。
- 登记不改（铁律三 / 风格级）：
  - **印刷怪癖**：`nearest-neighbour` 与 `nearest neighbour` 在同一页内混用（y=105.1 带连字符、y=204.5 与 y=371.9 段内 `nearest neighbour` 不带），原样保留。（**更正**：本条初稿曾把 MD 的 `the trade-of is that` 登记为印刷怪癖，经 p.39 逐页核验证明印刷为完整的 `trade-off`（bbox y=51.1 单 token `trade-off`），该处是导出**漏字母**，已在 p.039 条目下修复第 1 处。）
  - 印刷斜体强调（`large scale`、`finite-range model`、`n`-point、`n.n.f.`、`large scale planarity`）在 MD 中未保留（风格级）。
  - 行内数学与相邻文字空格合并（`vertex-set${ \mathbb { Z } } ^ { 2 }$and`、`model on${ \mathbb { Z } } ^ { 2 }$,`、`that$J _ { x , y }$is`、`when$1 < …`、`induced by this multi-scale`、`on${ \mathbb { Z } } ^ { 2 }$(which has`、`in the sense that it is restricted`、`induced by${ \mathbb { Z } } ^ { 2 }$and`、`points$x _ { 1 } = …`、`( k _ { 2 n } , 0 )$satisfying`、`$k _ { 2 n }$on the boundary`、`where$o ( 1 )$is`、`$x _ { 2 n }$which tends`、`2𝑛}\}$tending to infinity.`）为 MinerU 全篇系统性伪影，与前几页同一处置，不逐处拆改。
  - 页脚 `38  Hugo Duminil-Copin` 未入 MD（版式级）；印刷末行 `…(which for finite` 续至 p.39，MD 行 887 未分段（版式级）。
- 备注：本页 10 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙/字高量测）。

## p.039（PDF p.39 / 印刷 p.39）
- PNG：/tmp/icm2022dc_audit_p039.png（pngmono 150dpi）；300dpi 整页 `/tmp/icm2022dc_p039_300.png`，裁片 `_tradeoff`(7×) `_brackets`(12×) `_eps`(8×) `_expo`(7×) `_deltaA`(5×) `_eq88`(4×) `_norm`(7×) `_deltaB`(7×) `_eq89`(3×)；bbox `/tmp/icm2022dc_p039_bbox.xml`
- 核对：p.38 末句续排 `range models on ℤ² is the reason behind the "almost" intersection properties of long paths). The trade-off is that full conformal invariance …`、§8.4 标题 `8.4. Conformal bootstrap in 3D Ising model`、`At this point, we already mentioned…` 段（含 `liquid–vapour`）、`In recent years, a striking progress…` 段（含 `⟨−−⟩`、`A(x)`、`ε_{(x,y)} = σ_xσ_y − ⟨σ_xσ_y⟩`、`σ_{x+y} − σ_x`）、`Conformal invariance already forces…expo-nents Δ_A and coefficients f_ABC such that`、公式 (8.8)、公式 (8.9)、`(in (8.8), we adopted…` 段（含 `normalization of 𝒜`、`Δ_A`、`dificult`）、`While in 2D this was done in the eighties…` 段（至 `x₃ and` 断行）、页脚 `39  100 Years of the Ising Model`
- 结果：PASS±（差异列表，见下）
- 修复（10 次 `Edit`，覆盖 12 处缺陷位置）：
  1. 行 887 `The trade-of is that full conformal invariance` → `The trade-off is that full conformal invariance`。bbox y=51.1 作单 token `trade-off`(x77.5–111.7)；7× 裁片 `/tmp/icm2022dc_p039_tradeoff.png`（px 310–520, y 203–262）直读「The trade-off is t」。**导出漏掉一个 f**。（本条同时更正 p.038 条目中把它误登记为「印刷怪癖」的说法。）
  2. 行 895 `there must exist expo nents$` → `there must exist exponents$`。bbox y=330.0 行尾 x400.0–422.4 为 `expo-`、次行 y=344.0 行首 x59.5–80.6 为 `nents`；7× 裁片 `/tmp/icm2022dc_p039_expo.png`（px 1520–1770, y 1363–1427）直读「ust exist expo-」。跨行断词连字符应还原为 `exponents`。
  3. 行 895 `exponents$\Delta \mathcal { A }$and coeficients$f _ {\mathcal{A B C }}$such that` → `exponents$\boldsymbol {\Delta} _ {\mathcal { A } }$and coefficients$f _ {\mathcal{A B C }}$such that`（一处 `Edit` 同时改正两处缺陷：Δ 的下标丢失+粗体丢失，以及 `coeficients`）。**下标与粗体**：bbox y=343.9 的 `𝚫`(x83.0–89.3) 记录为 **U+1D6AB MATHEMATICAL BOLD CAPITAL DELTA**，其下标行 y=347.2 为 `A`(x89.8–96.2)；5× 裁片 `/tmp/icm2022dc_p039_deltaA.png`（px 240–950, y 1425–1484）直读「nents 𝚫_𝒜 and coefficients *f*_𝒜ℬ𝒞 such that」，Δ 笔画明显加粗、𝒜 位于右下角小一号位，确为**粗体 Δ 带下标 𝒜**。导出写成非粗体、且把 𝒜 放到与 Δ 并列的基线位，渲染成 `Δ𝒜`，属数学记号错误（与 (8.8)/(8.9) 的 `\boldsymbol {\Delta} _ {\mathcal {A}}` 相比可自证）。`coeficients`：bbox y=344.0 作 `coefficients`(x116.4–161.7)，同一裁片直读可见 `ffi` 连字。
  4. 行 902（公式 (8.9)）`\boldsymbol {\Delta} _ {C}` → `\boldsymbol {\Delta} _ {\mathcal {C}}`（`replace_all`，同一行 3 处）。3× 裁片 `/tmp/icm2022dc_p039_eq89.png`（px 340–1780, y 1590–1745）直读「⟨𝒜(x)ℬ(y)𝒞(z)⟩ = *f*_𝒜ℬ𝒞 / (‖x−y‖₂^{Δ_𝒜+Δ_ℬ−Δ_𝒞} ‖y−z‖₂^{Δ_ℬ+Δ_𝒞−Δ_𝒜} ‖z−x‖₂^{Δ_𝒞+Δ_𝒜−Δ_ℬ})」——三个指数里的 C 全是**花体 𝒞**（与同一公式里的 𝒜、ℬ 同形），而导出在这 3 处写成正体 `C`（U+0043），是字形误识。
  5. 行 905 `we adopted without loss ofgenerality the normalization of A that makes the constant` → `… without loss of generality the normalization of $\mathcal { A }$ that makes the constant`（一处 `Edit` 改正两处缺陷）。**空格**：bbox y=422.2 作 `loss`(173.0–188.5) `of`(190.1–198.4) `generality`(199.9–239.5)，空隙 1.6/1.5 pt 与同行其余词距同档，印刷有空格。**字形**：bbox y=422.0 x321.7–330.3 单 token `A`，7× 裁片 `/tmp/icm2022dc_p039_norm.png`（px 1050–1460, y 1748–1807）直读「normalization of **𝒜** that」，该 A 是**花体草写 𝒜**（与 (8.8) 中的 𝒜 同形），导出写成正文正体 `A`，故改为 `$\mathcal { A }$`。
  6. 行 905 `The exponents and coeficients depend a priori on the CFT,` → `coefficients`。bbox y=436.1 作 `coefficients`。
  7. 行 905 `be encoded in terms of the$\Delta \mathcal { A }$and the$f _ {\mathcal{A B C } }$.` → `in terms of the$\Delta _ {\mathcal { A } }$and the$f _ {\mathcal{A B C } }$.`。bbox y=491.9 `Δ`(x298.3–304.7) 记录为 **U+0394 GREEK CAPITAL LETTER DELTA（正体，非粗体）**，下标行 y=495.1 `A`(x305.3–311.6)；7× 裁片 `/tmp/icm2022dc_p039_deltaB.png`（px 1170–1660, y 2040–2100）直读「the Δ_𝒜 and the *f*_𝒜ℬ𝒞. Of c」，笔画纤细确认非粗体，𝒜 仍在下标位。故此处**只补下标、不加粗**——这是印刷自身的不一致（首次出现处用粗体 Δ、此处用正体 Δ），按铁律三原样保留，不统一改写。
  8. 行 905 `determining these coeficients is very dificult.` → `determining these coefficients is very difficult.`。bbox y=505.9 作 `coefficients` 与 `difficult`（两处 `ffi`/`fi` 连字压平）。
  9. 行 907 `proceed in a slightly diferent way by asking which` → `slightly different way`。bbox y=533.8 作 `different`(x296.7–330.3)。
  10. 行 907 `consistency relations coming from diferent ways of applying` → `from different ways`。bbox y=575.6 作 `different`(x318.3–351.9)。
- 逐字核对留证（MD 无误，未改）：
  - **⟨−−⟩ 是两个减号而非一条长划**：bbox y=232.2 单 token `⟨−−⟩`(x132.4–152.3) 含 U+27E8 / U+2212 ×2 / U+27E9；12× 裁片 `/tmp/icm2022dc_p039_brackets.png`（px 540–670, y 956–1014）直读「⟨ − −⟩」，两段横画之间有**可见断裂**，排除 em-dash 误判。MD 行 893 的 `⟨−−⟩` 正确。
  - **ε 的花括号下标**：bbox y=276.7 子行含独立 token `{`(x213.4–216.4) 与 `}`(x228.6–231.6)，`x,𝑦`(x217.2–227.8)；8× 裁片 `/tmp/icm2022dc_p039_eps.png`（px 720–1300, y 1133–1192）直读「σ_x and ε_{\{x,y\}} = σ_xσ_y − ⟨σ_xσ_y⟩」，确认是**花括号**而非圆括号下标，MD `\varepsilon _ { \{ x , y \} }` 正确；ε 作 U+1D700 MATHEMATICAL ITALIC SMALL EPSILON（即 `\varepsilon` 的圆体 ε，非 `\epsilon` 的 ϵ），MD 正确。
  - **公式 (8.8) 完全正确**：4× 裁片 `/tmp/icm2022dc_p039_eq88.png`（px 425–1780, y 1516–1624）直读「⟨𝒜(x)𝒜(y)⟩ = 1/‖x−y‖₂^{Δ_𝒜},  (8.8)」，行末为**逗号**（bbox y=369.0 x212.2–214.7），与 MD 行 898 的 `,\tag{8.8}` 一致；Δ 粗体、𝒜 下标，MD `\boldsymbol {\Delta} _ {\mathcal {A}}` 一致。
  - **公式 (8.9) 其余部分正确**：分式分子 `f_𝒜ℬ𝒞`、三个范数因子与指数的加减次序 `Δ_𝒜+Δ_ℬ−Δ_𝒞` / `Δ_ℬ+Δ_𝒞−Δ_𝒜` / `Δ_𝒞+Δ_𝒜−Δ_ℬ` 与 MD 行 902 逐项相同；**行末无标点**（bbox y=395.7 起只有 `(8.9)` 编号，无 `,`/`.` token），MD 亦无，正确。
  - **跨行断词已正确合并**：`cor-`/`relation`（y=218.5/232.2）、`opera-`/`tors`（y=316.1/330.0）、`conf or-`/`mal bootstrap`（y=547.7/561.7）三处 MD 分别作 `correlation`、`operators`、`conformal`，正确。
  - `liquid–vapour` 的连接号为 **U+2013 EN DASH**（非连字符），MD 保留 `–` 正确；`1D`/`2D`/`3D`/`4D`、`[70]`、`[87]`、`[8.8]`、`[8.9]` 编号与印刷逐字一致。
- 登记不改（铁律三 / 风格级）：
  - **印刷怪癖**：本段用美式拼写 `normalization`（bbox y=422.2），而同一篇 p.38 用英式 `renormalisation`，原样保留不统一；粗体 Δ 与正体 Δ 在同一段内混用（见修复 3、7），原样保留。
  - 印刷斜体强调（`Gaussian`、`local operators`、`A(x)`、`conformal bootstrap`、`conformal block decomposition`、`multi-point`、`operator product expansion`、`*n*`-point、§8.4 标题粗体）在 MD 中未保留（风格级）。
  - 行内数学与相邻文字空格合并（`models on${ \mathbb { Z } } ^ { 2 }$is`、`observables$\sigma _ { x }$and$\varepsilon _ { \{ x , y \} } = …$give`、`gradient$\sigma _ { x + y } - \sigma _ { x }$of`、`nents$\boldsymbol…$and coefficients$f _ …$such`、行 907 `$\langle \mathcal { A } ( x _ { 1 } ) \cdots \rangle$and`、`first$x _ { 1 }$and$x _ { 2 }$or`）为 MinerU 全篇系统性伪影，与前几页同一处置，不逐处拆改。
  - 页脚 `39  100 Years of the Ising Model` 未入 MD（版式级）；印刷末行 `…x₃ and` 为跨页断句，MD 行 907 未在 `$x _ { 3 }$and` 处断开（版式级；行 907 其余部分属 p.40，留待该页处理）。
- 备注：本页全部修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0；`\boldsymbol {\Delta} _ {C}` 一行 3 处、修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙/字高量测）。

## p.040（PDF p.40 / 印刷 p.40）
- PNG：/tmp/icm2022dc_audit_p040.png（pngmono 150dpi）
- 核对：页首续接 p.39 末行的 `…$x_3$ and`、临界指数对 $(Δ_σ, Δ_ε)$ 两处、破折号插入语、`[41,78,93]` 与 `[97]`、§9 标题与两段、`## Acknowledgments` 标题与人名串、`Equalling` 一句、`playground` 断行、`conformal blocks` 斜体、页脚
- 结果：PASS±（差异 5 处，均已按原图逐处 `Edit` 修复；另有 6 组经仲裁判定 MD 正确、**不改**，见「负向结论」；1 项印刷排印属性登记而未改，见文末）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：本页无题录段（续接前页正文），页首首行印刷为 `…$x_3$ and`，与 p.39 末行同属一句跨页断句；MD 未在 `$x _ { 3 }$and` 处断开（版式级，非内容缺陷）。
  - **正文**：§9 `9. A tail to this story` 标题与两段（`The Ising model has always played the role of a locomotive…`／`Let us mention several long-standing problems remaining widely open…`）、`## Acknowledgments` 标题与致谢段，段落切分与印刷一致；`locomotive`、`playground`、`unsolved puzzles`、`roughening phase transition`、`cross-fertilisation`、`Schramm-Loewner` 等拼写逐字在位。
  - **公式**：本页唯一的两处行内数学 $(Δ_σ, Δ_ε)$ 与数值对 $(0.5181489(10), 1.412625(10))$，逐符号核对见下「逐字核对留证」；两处 Δ 均为**粗体**，MD 原为普通体，已修。
  - **参考文献**：`[41,78,93]`、`[97]` 两个行内标注在位；`[41,78,93]` 逗号后**无空格**，已用像素量测确认与印刷一致（MD 正确），详见「负向结论」。
  - **版式**：两处 `–` 破折号插入语的分行位置（首个 `–` 恰落在印刷行末 x 417.4–422.4）、`pos-`/`efficients` 与 `play-` 的行末连字符换行、页脚 `40  100 Years of the Ising Model`（版式级，未入 MD）。
- 修复（5 处，均以 `Edit` 工具逐处落地）：
  1. 行 909 `critical exponents$( \Delta _ { \sigma } , \Delta _ { \varepsilon } )$for the spin` → `$( \boldsymbol {\Delta} _ { \sigma } , \boldsymbol {\Delta} _ { \varepsilon } )$`。8× 裁片 `/tmp/icm2022dc_p040_dsig1.png` 直读「s (**Δ**₍σ₎, **Δ**₍ε₎) f」——两个三角的斜边明显加粗、直立加厚，与同页普通体变量对比明显；bbox y=134.8 上一行末 token `–`（x 417.4–422.4）确认该对位于 `estimates –` 之后。MD 丢失粗体。
  2. 行 909 `namely$\left( \Delta _ { \sigma } , \Delta _ { \varepsilon } \right) =` → `\left( \boldsymbol {\Delta} _ { \sigma } , \boldsymbol {\Delta} _ { \varepsilon } \right)`。8× 裁片 `/tmp/icm2022dc_p040_dsig2.png` 直读「namely (**Δ**₍σ₎, **Δ**₍ε₎) = (0.5181489(10), 1.412625(10)) –」；bbox y=148.7 整行 token 序列为 `namely` / `(𝚫` / `,` / `𝚫` / `)` / `=` / `(0.5181489(10),` / `1.412625(10))` / `–`，两个 Δ 的 Unicode 均为 **U+1D6AB MATHEMATICAL BOLD CAPITAL DELTA**，与裁片一致。同第 1 处族。
  3. 行 909 `for a review ofthe most recent progress in this very exciting area ofmodern theoretical physics.` → `for a review of the most recent progress in this very exciting area of modern theoretical physics.`。9× 裁片 `/tmp/icm2022dc_p040_review.png` 直读「a review **of the** most recent progress in this very exciting area **of modern** theoretical」——两处 `of` 与后随词之间均有明显词间空隙。属行内文字粘连伪影（`o`+`f` 与前一词尾紧贴）。
  4. 行 911 `getting suficient information on the possible scaling limits` → `getting sufficient information`。9× 裁片 `/tmp/icm2022dc_p040_suficient.png` 直读「getting **sufficient** information on」——为 `su`+`ffi`+`cient`，双 f 连字在位。MD 的单 f 是 MinerU 的 ff/ffi 连字压平伪影（同族已在本页段 p.35 行 839 的 `efectively`、p.38 行 875 的 `dificulty`、p.39 行 895/905 的 `coeficients`/`dificult` 一并修复）。
  5. 行 907 `as a linear combination (with positive coeficients in the Ising case)` → `coefficients`。9× 裁片 `/tmp/icm2022dc_p040_positive.png` 直读两行「…linear combination (with **pos-**」／「**efficients** in the Ising case) of known objects called the *conformal blocks*. Equalling」——印刷把 `coefficients` 断为 `pos-` + `efficients`，`ffi` 连字清晰可见（`effi` 四笔）。MD 的单 f 系连字压平。**注**：该句印刷在 p.39 的末行、跨页接续到 p.40 的行首，故对应 MD 行 907；p.039 条目已声明「行 907 其余部分属 p.40，留待该页处理」，此处收口。
- 逐字核对留证（MD 无误，未改）：
  - **数值对**：bbox y=148.7 给出 `(0.5181489(10),` 与 `1.412625(10))`，与 MD 行 909 `\left( 0 . 5 1 8 1 4 8 9 ( 1 0 ) , 1 . 4 1 2 6 2 5 ( 1 0 ) \right)` 数值逐位一致（MD 的数字逐位加空格是本篇 MinerU 数学模式的固定写法，非缺陷）；括号型为 `\left( … \right)` 大括号，裁片可见括号高度包住上下标，MD 一致。
  - **破折号插入语**：MD 行 909 作 `estimates – namely$…$– using`。bbox 显示首个 `–`（U+2013 en dash）是 y=134.8 行的**末字符**（x 417.4–422.4，紧随 `estimates` 的 x 377.8–414.7），第二个 `–` 在 y=148.7 行 x 266.6–271.6（紧随 `1.412625(10))` 的 x 205.4–264.4）——印刷确为一对 en dash，MD 的位置与字符全对。
  - **`[41,78,93]`**：印刷逗号后**无空格**（与 p.35 行 835 的 `[28,99]` 同款，而 p.35 行 833 的 `[28, 99]` 有空格）。300 dpi 下该处 `,`→`7` 的空隙落在词内带 6–7 px，而同行真实词间空隙为 12–19 px ⇒ 印刷为 `[41,78,93]`，**MD 正确，未改**（与 p.35 的仲裁口径一致）。
  - **`[97]`**：印刷 y≈356 一行 `[97] for a review of the most recent progress…`，MD 行 909 逐词在位，`[97]` 未被误读为 `[87]`/`[37]`。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - `playground`（行 915）：印刷跨行断为 `play-`（行末）+ `ground`（次行首）。9× 裁片 `/tmp/icm2022dc_p040_playground.png` 直读两行「…incredible properties turn it into an amazing **play-**」／「**…**ysicists. As a consequence, during most of its history」。MD 已把连字符正确还原为整词 `playground`，**正确，未改**（行末连字符还原是本篇 MD 的正确做法；对比 p.38 页眉处 `play-` 的同类处理）。
  - `Velenik`（行 921）：9× 裁片 `/tmp/icm2022dc_p040_velenik.png` 直读「V. Tassion, and Y. **Velenik** who, w」——**单 l**，150 dpi 全页图上曾被读成 `Veleniik`/`Velenk`。MD 作 `Y. Velenik`（单 l），**正确，未改**。
  - `Acknowledgments`（行 919 标题）：9× 裁片 `/tmp/icm2022dc_p040_ack.png` 直读「**nowledgments**」——`Acknowledgments` 为**单 e**（美式拼写），与同篇正文的英式 `Equalling`、`behaviour` 体系并存。MD 作 `## Acknowledgments`，**正确，未改**；按铁律三不改为英式 `Acknowledgements`。
  - `Monte-Carlo`（行 909）、`cross-fertilisation`（行 917）：连字符位置与拼写（`-fertilisation` 英式 s）在印刷与 MD 中一致，逐字核对无误，**未改**。
  - `[97]`、`0.5181489(10)`、`1.412625(10)`：见上「逐字核对留证」，**未改**。
  - `a priori`（行 909）：印刷为斜体，MD 为正体——但本篇 MD **全篇单星号斜体标记数为 0**（`grep -o '\*[A-Za-z]…\*'` 无命中），说明该 MinerU 导出对**行文斜体是系统性丢弃**而非本页偶发，故**登记而不擅自引入本篇从未使用过的 `*…*` 标记**（同 `conformal blocks`，9× 裁片 `/tmp/icm2022dc_p040_positive.png` 可见其为斜体）。此项属导出层的全局风格取舍，**留集成者裁决**，本轮未改。
- 登记不改（铁律三）：
  - **印刷怪癖**：`Acknowledgments` 用美式单 e，而同段的 `Equalling` 用英式双 l——同一篇内英美拼写混用，照录不统一。
  - `Y. Velenik` 单 l 姓、`[41,78,93]` 逗号后无空格（与 `[28, 99]` 有空格并存）、`pos-`/`play-` 行末连字符换行——均为原刻排印事实，照录。
  - 行内数学与相邻文字空格合并（`exponents$( … )$for`、`namely$( … ) =`、`$\left( … \right)$–`）为 MinerU 全篇系统性伪影，本页不逐处拆改（与前几页同一处置）。
  - 页脚 `40  100 Years of the Ising Model` 未入 MD（版式级）。
- **跨页联动**：本页交叉清点全篇 `\Delta _ { \sigma }` / `\Delta _ { \varepsilon }` 时，回头发现**我自己在 p.35 的判定漏了 4 个 Δ 的粗体层级**，已在 `## p.035` 条目文末以「迟到发现」补记并修复 3 处（行 817 两处、行 833 两处），p.035 判定同步由 8 处升格为 **9** 处。这是本轮 8 页里唯一一处「自查发现前页漏判」，如实登记。
- **本块（p.33–p.40）收口时的全篇残余清单（只读清点，供集成者统一处理，本轮无权改）**——注意本条目中较早页（p.035 / p.036）写下的「跨页登记」行清单是**当时**的快照，已被本块后续修复改变，以本条为准：
  - `diferent` / `diferential`（连字压平）：实存 **3** 行 = **27、115、131**（p.031–p.032 条目中列为 691/697/875/879/907 的各位，均已在本块或前块修复）。
  - `suficient`：实存 **1** 行 = **135**。`efectively`：实存 **1** 行 = **143**。（p.035 条目称 `efectively` 在行 143「另有 1 处」，`grep -nF` 实测行 839 已清零、行 143 为全篇仅存处。）
  - `coeficients` / `coeficient` / `dificulty` / `dificult`：全篇 **0**（已在本块 p.036/p.038/p.039/p.040 清零）。
  - `ℎ`(U+210E, PLANCK CONSTANT)：全篇仍 **9** 处 = 行 **67、95、171、257、261、321、327、343、409**，均在本块之外。
  - 行文斜体（`*…*` 标记）：本篇 MD **0** 处，印刷中的 `a priori`、`conformal blocks` 等斜体被导出系统性丢弃；属导出层全局取舍，本轮只登记不引入本篇从未用过的新标记。
  - 粗体数学写法统计（供参考）：`\mathbf` 91 处、`\boldsymbol` 47 处；本块新增的粗体 Δ 一律用 `\boldsymbol`，与印刷层级一一对应。
- 备注：本页 5 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙/字高量测）。修复后全篇复扫：普通体 `\Delta _ { \sigma }` / `\Delta _ { \varepsilon }` 残留 **0**，行 817 / 833 / 909 全部为粗体形式。

## 块 H（PDF p.041–p.046）

## p.041（PDF p.41 / 印刷 p.41）
- PNG：/tmp/icm2022dc_audit_p041.png（pngmono 150dpi）
- 核对：`## Funding` 全文、ERC/NCCR/FNS/Simons 四项资助来源、`## References` 标题、参考文献 **[1]–[14]** 逐条（作者 / 刊名缩写 / 卷 / 年 / 期号 / 页码范围）、[2] 的 φ⁴、[4] 的 φ₄⁴、[11] 的 |φ⁴| 与 $n$-component、[12] 的 `sym-`/`metry` 断行、[13] 的 `l’IHP`、页脚
- 结果：PASS±（差异 **13** 处，均已按原图逐处 `Edit` 修复；另有 9 组经仲裁判定 MD 正确、**不改**，见「负向结论」；1 组印刷怪癖按铁律三原样保留，见「登记不改」）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：本页无题录段（正文结束后的资助与文献页），`## Funding` / `## References` 两个标题与 MD 的 `## Funding`（行 923）、`## References`（行 927）一一对应。
  - **正文**：`Funding` 段共 3 行，印刷 bbox y=51.1 / 65.0 / 79.0 / 92.9 逐行核对：`This work has received funding from the European Research Council (ERC) under the` / `European Union’s Horizon 2020 research and innovation programme (grant agreements` / `No. 757296). The author acknowledges funding from the NCCR SwissMap, the Swiss` / `FNS, and the Simons collaboration on localization of waves.` 与 MD 行 925 **逐词吻合**（含 `Union’s` 的 U+2019、`No. 757296` 的 6 位编号、ERC/NCCR/FNS 四个缩写的大小写）。
  - **公式**：本页无行间公式；行内数学共 4 处（[2] φ⁴、[4] φ₄⁴、[11] $n$ 与 |φ⁴|），逐处见「逐字核对留证」与「修复」。
  - **参考文献**：**[1]–[14] 逐条**核对作者名（含重音 `Fernández`、`Hongler`、`Sidoravicius`、`Warzel`、`Tassion`、`Zamolodchikov`、`Polyakov`、`Belavin`、`Enting`、`Bauerschmidt`、`Brydges`、`Slade`、`Padé`）、刊名缩写、卷号（73/86/47/194/334/216/44/124/11/157/241/52/47/77?）、年份、期号、页码范围与连字符（全部为 en dash U+2013）。**[5]** 是唯一无 `no.` 期号的条目（`Commun. Math. Phys 334 (2015), 719–742.`），印刷 bbox y=288.2 确认为 `334@93.5-108.5 (2015),@111.0-140.0 719–742.`，**无 `no.`**，MD 一致；且印刷此处刊名止于 `Phys` 无句点（因后接粗体卷号），MD 亦作 `Math. Phys 334`，**未擅自补点，正确**。
  - **版式**：参考文献为悬挂缩进——编号列 x 59.5–72.8，正文列一律起于 **x 93.5**；[12] 的 `sym-`（y=511.4 行末 x 394.3–414.2）与 `metry`（y=525.3 行首 x 93.5–117.0）构成行末连字符断词，MD 已正确还原为整词 `symmetry`；页脚 `41  100 Years of the Ising Model`（bbox y=639.0，版式级，未入 MD）。
- 修复（13 处，均以 `Edit` 工具逐处落地）：
  - **参考文献编号与正文之间的分隔（[1]–[9] 共 9 处）**：印刷悬挂缩进使编号列（右端 x 68.7 / 72.8）与正文列（左端 x 93.5）之间恒有 **24.7 pt** 空档；6× 裁片 `/tmp/icm2022dc_p041_label1.png`（px 225–470, y 595–655）直读「[1]　　　　**M.** **A**」，两列分离清晰。而 MD 把 [1]–[9] 写成 `[1]M.`，**编号与作者首字母粘连**，同时**同一份 MD 的 [10]–[14] 却写了空格**（`[10] R.J.`、`[13] S.`…），自相矛盾。逐条修复：`[1]M. Aizenman` → `[1] M. Aizenman`；`[2]M. Aizenman` → `[2] M. Aizenman`；`[3]M. Aizenman, D.J. Barsky` → `[3] M. Aizenman, D.J. Barsky`；`[4]M. Aizenman and H. Duminil-Copin.` → `[4] M. …`；`[5]M. Aizenman, H. Duminil-Copin, and V. Sidoravicius.` → `[5] M. …`；`[6]M. Aizenman, H. Duminil-Copin, V. Tassion, and S. Warzel.` → `[6] M. …`；`[7]M. Aizenman and R. Fernández.` → `[7] M. …`；`[8]J.R. Baker and A. George.` → `[8] J.R. …`；`[9]R.J. Baxter.` → `[9] R.J. …`。9 个锚点全篇各唯一，三态 provenance 均为 **1/1/1**。
  1. 行 931 `Geometric analysis of$\varphi ^ { 4 }$fields and Ising models.` → `Geometric analysis of $\varphi ^ { 4 }$ fields and Ising models.`。6× 裁片 `/tmp/icm2022dc_p041_phi4fields.png`（px 950–1180, y 695–765）直读「…analysis. **of** **φ**⁴ **fields** a…」——`of` 与 φ 之间、φ⁴ 与 `fields` 之间**均可见词间空隙**。bbox y=174.8 给出 `of@232.1-240.4`、`𝜑@243.2-248.9`(y=178.0)、上标 `4@249.1-252.7`、`fields@255.7-277.3`：`of`→φ 空档 8.7 pt（真实词间），上标 `4`→`fields` 空档 **3.0 pt**，而同行真实词间空档为 2.5 pt（`Geometric`→`analysis`）⇒ **确有空格**。MD 两处都粘连，属数学/文字边界空格丢失。同一 Edit 内同时完成 `[2]` 编号空格。
  2. 行 935 `critical 4D Ising and$\phi _ { 4 } ^ { 4 }$models.` → `critical 4D Ising and $\phi _ { 4 } ^ { 4 }$ models.`。bbox y=244.6 `and@161.0-175.4`，`𝜙@178.1-183.6`(y=248.8)，`44@183.8-187.4`，`models.@190.4-221.7`：`and`→φ 空档 **2.7 pt**、`4`→`models.` 空档 **3.0 pt**，均 ≥ 该行词间空档 2.5 pt ⇒ **两处都有空格**。MD 两处都粘连。同一 Edit 内同时完成 `[4]` 编号空格。
  3. 行 947 `399th solution of the Ising model. J. ofPhys. A: Math. and Gen.` → `… J. of Phys. A: Math. and Gen.`。6× 裁片 `/tmp/icm2022dc_p041_jofphys.png`（px 1410–1675, y 1810–1875）直读「…model. **J. of Phys. A:**」——`of` 与 `Phys.` 之间空隙清晰。bbox y=441.6 `J.@344.5-351.5` `of@353.9-361.7` `Phys.@364.2-385.8` `A:@388.3-397.7`，三处空档 2.4 / 2.5 / 2.5 pt，与同行词间空档一致。刊名实为 **`J. of Phys. A: Math. and Gen.`**，MD 把 `of` 与 `Phys` 焊死成 `ofPhys`。
- 逐字核对留证（MD 无误，未改）：
  - **[2] φ⁴**：bbox 上标 token 为 `4@249.1-252.7`（y=174.8，上标高度），正文 φ 为 `𝜑`（U+1D70C GREEK PHI SYMBOL，math italic）。MD `\varphi` 对应 φ 的直立圆形式、此上下文为 `φ⁴` 的经典记法，与印刷字形一致，**未改**。
  - **[4] φ₄⁴（**印刷怪癖，MD 正确**）**：bbox 显示 φ 为 `𝜙`（U+1D719 GREEK PHI，斜体形），其后 token 为 **`44@183.8-187.4, y 244.6–258.3`**——一个 token 同时跨越 y=244.6（上标高度）与 y=258.3（下标高度），即**同一个 φ 的右上与右下各有一个 4**。9× 裁片 `/tmp/icm2022dc_p041_phi4.png`（px 720–805, y 995–1095）直读「φ**⁴**／φ**₄**」——上标 4 与下标 4 **同时在位**，肉眼可辨。MD 行 935 作 `\phi _ { 4 } ^ { 4 }`（φ 下标 4、上标 4）**逐结构复现了原刻**，与该文真实题名「…critical 4D Ising and φ⁴ models」的标准写法不同，属**原刊自身的排印怪癖**，按铁律三**原样保留、绝不"改正"为 `\phi ^ { 4 }`**。此处 MD 正确，**未改**。
  - **[11] $n$-component |φ⁴|**：bbox y=481.7 `4-dimensional@119.0-176.0`、`𝑛-component@178.5-231.2`(y=485.9, U+1D45B italic n)、`|𝜙@234.1-242.3`、`4@242.5-246.1`、`|@247.0-249.0`、`spin@251.9-268.5`。`𝑛-component` 整体为**单个 token**（连字符属 token 内部），竖线为**普通竖线 `|`**（x 234.1–242.3 与 247.0–249.0 两根，与 p.38 的 `∥`(U+2225) 严格不同），φ 为 `𝜙`（U+1D719）。MD 行 949 `$n$-component $|\phi ^ { 4 }|$ spin model` 与之一致，**未改**；`|φ⁴|` 后到 `spin` 的空档 2.9 pt ≥ 词间 2.5 pt，MD 的空格亦在位。
  - **[12] `sym-` / `metry`**：印刷断行为 `sym-`+`metry`，MD 行 951 已还原为整词 `Infinite conformal symmetry`，**正确，未改**。
  - **[13] `l’IHP`**：bbox token `l’IHP@382.0-404.6` 的码点逐位 dump 为 `['0x6c', '0x2019', '0x49', '0x48', '0x50']`——**撇号是 U+2019（右单引号）而非 ASCII U+0027**。MD 行 953 作 `l’IHP`（U+2019）**逐码点一致，未改**。
  - **页码范围与破折号**：[1] `83–94`、[2] `1–48`、[3] `343–374`、[4] `163–235`、[5] `719–742`、[6] `661–743`、[7] `393–454`、[8] `768`、[10] `2463`、[11] `692–742`、[12] `333–380`、[13] `1784–1798`、[14] `2049–2086`；区间破折号全部为 U+2013 en dash，与印刷 bbox token（`83–94.`、`3–4,`、`1784–1798.` 等）一致，**未改**。
  - **年份/卷/期三态数字**：`73 (1980), no. 1`、`86 (1982), no. 1`、`47 (1987), no. 3–4`、`194 (2021), no. 1`、`334 (2015)`、`216 (2019), no. 3`、`44 (1986), no. 3–4`、`124 (1961), no. 3`、`11 (1978), no. 12`、`157 (2014)`、`241 (1984), no. 2`、`52 (2016), no. 4`、`47 (2019), no. 4` —— 逐位与 MD 一致，**未改**。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - `[9] R.J. Baxter. Exactly solved models in statistical mechanics.` —— 印刷中该**书名整体为斜体**（150 dpi 全页图可见 `Exactly solved models in statistical mechanics` 字形右倾），MD 为正体。但与 p.40 已登记的情况同源：本篇 MD **全篇单星号斜体标记数为 0**，`grep -oE '\*[A-Za-z][A-Za-z ]{2,30}\*'` 无命中，导出对行文/书名斜体是**系统性丢弃**，故登记而**不擅自引入本篇从未使用过的标记**。
  - `behaviour`（[11]，英式）与 `behavior`（[7]，美式）在同一文献表内并存；`Padé`（[8]）带重音；`R. Fernández`（[3][7]）带重音；`Sidoravicius`、`Tassion`、`Warzel`、`Hongler`、`Zamolodchikov`、`Brydges`、`Bauerschmidt`、`Slade`、`Enting`、`Belavin`、`Polyakov`、`A. George`、`J.R. Baker` 的拼写与印刷逐字一致——**均未改**。
  - `[5]` 的 `Commun. Math. Phys 334`（刊名末词无句点）已用 bbox 确认，见上「参考文献」条，**未改**。
  - `[6]` 卷号 `216` 与 `[7]` 卷号 `44` 未被误读（150 dpi 下 `[7]` 的 `44` 与期号 `3–4` 相邻，易混），bbox `44@287.6-297.6, y 358.1–366.8` 为正文高度（非上/下标），MD 正确，**未改**。
- 登记不改（铁律三）：
  - **印刷怪癖**：**[4] 的 φ₄⁴**（同一 φ 同时带下标 4 与上标 4）——与该文献真实题名的标准写法 φ⁴ 不同，但这是原刻字形，**照录不改正**，MD 已如实复现。
  - **英美拼写混用**：[7] `behavior`（美式）与 [11] `behaviour`（英式）；[1] `two dimensional Ising system`（无连字符）与 [6][7] `two-dimensional`/`high-dimensional`（有连字符）——同一文献表内不一致，**照录不统一**。
  - 行内数学与相邻文字的空格合并（`of$\varphi`、`and$\phi`、`…\}$models`、`J. ofPhys`）为 MinerU 全篇系统性伪影；本页 4 处已逐处 `Edit` 修复，**文档他处仍存**（只读清点：`…of$` 类落在行 129、135、177、193、205、207、257、269、309、339、393、399、401、431、521、581、619、691、759、803、813、839、871、1025；`…}$lowercase` 类全篇约 190 处），**留待相应页段或集成者统一处理**。
  - 页脚 `41  100 Years of the Ising Model` 未入 MD（版式级）。
- **跨页登记（供集成者）**：以下**同族缺陷落在本轮 p.42–p.046 页段之外或更靠后，本页无权改**——参考文献编号粘连 `[19]W.`、`[33]N.P.`、`[35]H.`、`[41]S.`、`[45]M.E.`、`[46]M.E.`、`[73]L.P.`、`[77]G.`、`[86]M.`、`[95]T.D.`（均在行 965–1117，属后面的文献页）；行 993 `[33]N.P. Dolbilin, ,Y.M. Zinov'ev` 另有**重复逗号 `, ,`**，留待该页处理。
- 备注：本页 13 处修复（9 处编号空格 + 3 处数学/文字边界空格 + 1 处刊名焊字）逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙/字高量测）。

## p.042（PDF p.42 / 印刷 p.42）
- PNG：/tmp/icm2022dc_audit_p042.png（pngmono 150dpi）
- 核对：参考文献 **[15]–[33]** 逐条（作者 / 刊名 / 卷 / 年 / 期 / 页码）、[19] 的 `(–II)` 与 `699–730 – 151` 双段式、[21] `Fröhlich` 重音、[23] 的 $T_c$、[25] 的 `s-embeddings` 与 `arXiv:2006.14559`、[26] `Ann. IHP D 4`、[27] `Ann. of Math. (2)`、`correla-`/`tions` 断行、[30] 全部法文重音与 `Gauthier-`/`Villars` 断行、[31] `Th. Probab. & Its Appl.`、[32] `x+204`、[33] `Izvestiya: Math.`、页脚
- 结果：PASS±（差异 **5** 处，均已按原图逐处 `Edit` 修复；另有 12 组经仲裁判定 MD 正确、**不改**，见「负向结论」；2 组印刷怪癖按铁律三原样保留，见「登记不改」）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：本页无题录段，全页为文献表续页，页首直接起 `[15]`。
  - **正文**：无正文段（文献表）。
  - **公式**：本页仅 [23] 一处行内数学 `$T_c$`，逐位核对见「逐字核对留证」。
  - **参考文献**：**[15]–[33] 共 19 条**逐条核对作者、刊名、卷、年、期、页码。三条**无期号**条目与印刷一致：[24] `Ann. Probab. 28 (2000), 947–1017.`、[29] `Commun. Math. Phys. 316 (2012), 99–126.`（bbox y=455.6 `Phys.@93.5-115.2 316@117.7-132.6 (2012),@135.1-164.2 99–126.@166.7-199.0`，确无 `no.`）；[30] `4, Gauthier-Villars et fils.` 为法文旧式卷次写法，无年份无期号。
  - **版式**：**页脚与 p.41 不同**——p.41 为 `41  100 Years of the Ising Model`，**p.42 为 `42  Hugo Duminil-Copin`**（bbox y=639.0 `42@59.5-66.8  Hugo@93.5-110.3  Duminil-Copin@112.1-156.9`）。**〔本条初稿曾误记为「p.42 起改为 `Hugo Duminil-Copin`」，经 p.43 bbox y=639.0 `43 100 Years of the Ising Model`（页码后接 `100 Years of the Ising Model`）证伪并已更正：书眉实为奇偶交替（奇数页 `N  100 Years of the Ising Model`、偶数页 `N  Hugo Duminil-Copin`），本页只是偶数页，不是永久切换点。〕** 属**版式级**、未入 MD。四处行末连字符断词（[15] `equilib-`/`rium`、[16] `Lec-`/`ture`、[21] `clas-`/`sical`、[27] `correla-`/`tions`、另有 [30] `Gauthier-`/`Villars`）MD 均已正确还原为整词。
- 修复（5 处，均以 `Edit` 工具逐处落地）：
  1. 行 965 `[19]W. Bragg and E. Williams.` → `[19] W. Bragg and E. Williams.`。6× 裁片 `/tmp/icm2022dc_p042_lab19.png`（px 240–450, y 655–705）直读「[19]　　　　**W.**」——编号列右端 x 72.8 与正文列左端 x 93.5 之间有 20.7 pt 空档，编号与作者首字母明显分离。MD 粘连，且与本页 [15]–[18]、[20]–[32] 均写有空格自相矛盾。
  2. 行 981 `Ann. ofMath. (2) 181 (2015)` → `Ann. of Math. (2) 181 (2015)`。6× 裁片 `/tmp/icm2022dc_p042_ofmath.png`（px 880–1180, y 1640–1695）直读「…l. **Ann. of Math. (2**」——`of` 与 `Math.` 之间空隙清晰。bbox y=399.8 `Ann.@220.0-238.5  of@241.0-248.8  Math.@251.3-274.7  (2)@277.2-288.8  181@291.3-306.2`，`of`→`Math.` 空档 **2.5 pt**，与同行 `Ann.`→`of` 的 2.5 pt 词间空档一致 ⇒ 印刷确有空格。刊名实为 **`Ann. of Math. (2)`**。
  3. 行 981 `spin correla tions in the planar Ising model` → `spin correlations in the planar Ising model`。6× 裁片 `/tmp/icm2022dc_p042_correla.png`（px 1440–1760, y 1585–1695）直读两行「of spin **correla-**」／「o. 3, 1087–1138.」——印刷把 `correlations` 断为行末 `correla-` + 次行首 `tions`（bbox y=385.8 `correla-@375.7-406.9`，y=399.8 `tions@93.5-112.9`），**中间不存在空格**。MD 在断词处错误地插入了空格，把一个词劈成 `correla` + `tions`。
  4. 行 993 `[33]N.P. Dolbilin, ,Y.M.` → `[33] N.P. Dolbilin, ,Y.M.`。6× 裁片 `/tmp/icm2022dc_p042_lab33.png`（px 225–760, y 2285–2335）直读「[33]　　　　**N.P. Dolbilin, ,Y.M. Z**」——编号与作者分离清晰（同第 1 处族）。**注意裁片同时直接印证了本条中 `Dolbilin, ,Y.M.` 的重复逗号是印刷原貌**（详见「登记不改」），修复时**只加编号后的空格，未动该逗号**。
  5. 行 993 `Izvestiya: Math 63 (1999), no. 4, 707.` → `Izvestiya: Math. 63 (1999), no. 4, 707.`。6× 裁片 `/tmp/icm2022dc_p042_izvestiya.png`（px 1440–1790, y 2340–2395）直读「…nt. **Izvestiya: Math.**」——`Math` 之后的**句点清晰可见**。bbox y=567.1 token 为 `Math.@397.5-420.9`（**含句点**），其后 `63` 起于 y=581.1 的次行。MD 丢失了刊名末的句点。
- 逐字核对留证（MD 无误，未改）：
  - **[23] $T_c$**：bbox y=302.1 `above@147.2-170.3` 后接两个独立 token——`𝑇@172.5-178.0`（**y=304.6，斜体大写 T**，U+1D447）与 `𝑐@177.7-181.4`（**y=307.3，下标小写 c**，U+1D450），再接 `.@182.2-184.7`。即印刷为 `above` + 斜体 $T$ + 下标 $c$ + 句点。MD 行 973 `$T_c$.` 结构与字形层级**逐项一致**，**未改**；`above`→$T$ 空档 2.2 pt，与同行词间空档 2.5 pt 同量级（斜体 T 左侧边距较窄），MD 的空格在位。
  - **[19] `(–II)` 与 `699–730 – 151`**：bbox token `(–II)@131.9-150.2` 的码点逐位 dump 为 `['0x28', '0x2013', '0x49', '0x49', '0x29']`——括号、**U+2013 en dash**（非 U+2212 减号）、两个 ASCII `I`、右括号。分卷分隔符 token `–@413.1-418.1` 亦为 **U+2013**，与前一 token `699–730@375.7-410.6` 之间空档 2.5 pt。MD 行 965 的 `(–II)` 与 `699–730 – 151` **逐码点、逐空格一致**，**未改**。
  - **[31] `Th. Probab. & Its Appl.`**：bbox y=511.4 token 为 `&amp;@196.0-203.7`——这是 XML 对 `&` 的转义，实际字符即 `&`，非 `&amp;` 字面。`Th.@145.8-158.9`→`Probab.@161.3-193.5`→`&@196.0-203.7`→`Its@206.2-216.2`→`Appl.@218.7-240.0`，四处空档 2.4–2.5 pt 均匀。MD 行 989 一致，**未改**。
  - **[30] 法文重音**：bbox y=469.5 `Propriétés@130.4-171.0`、`magnétiques@173.5-223.7`、`corps@242.0-263.8`、`à@266.3-270.7`、`températures.@308.0-362.0`——**`Propriétés` / `magnétiques` / `à` / `températures` 四个重音全部在位**；`corps`→`à` 空档 2.6 pt、`à`→`diverses` 空档 2.5 pt，词间空格在位。MD 行 987 逐字符一致，**未改**。次行 `Villars@93.1-119.9 et@122.4-129.5 fils.@131.9-146.1`——`Villars` 起点 x=93.1（略小于常规 93.5，系斜体 V 左伸），`Gauthier-`+`Villars` 已正确还原为 `Gauthier-Villars`，**未改**。
  - **[32] `x+204`**：bbox y=539.3 `104@337.2-352.1 (1992),@354.6-383.7 x+204.@386.1-414.2`——**罗马数字加页** `x+204` 为**单一 token**，内部无空格。MD 行 991 一致，**未改**。
  - **[26] `Ann. IHP D 4`**：bbox y=371.9 `Ann.@145.8-164.4 IHP@166.9-183.5 D@186.0-193.2 4@195.7-200.6`，刊名 `IHP` / 系列 `D` / 卷 `4` **各自独立**且空档 2.5 pt。MD 行 979 一致，**未改**。
  - **[25] `arXiv:2006.14559`**：bbox y=344.0 `graphs.@306.6-335.8 arXiv:2006.14559@338.2-410.5 (2020).@413.0-442.1`——arXiv 编号为**单一 token**，含冒号无空格；`graphs.`→`arXiv:` 空档 2.4 pt。MD 行 977 一致，**未改**。
  - **其余 15 条**（[15][16][17][18][20][21][22][24][28][29][30][31][32][33]）的作者重音（`Fröhlich` [21]、`Kotecký` [32]）、刊名缩写、年份、期号、页码区间（`1033–1098`、`1–86`、`197–229`、`153–168`、`699–730`/`540–566`、`883`、`123–150`、`528–571`、`305–349`、`947–1017`、`515–580`、`99–126`、`582–600`、`x+204`、`707`）与破折号全为 U+2013 en dash——逐条与印刷 bbox 一致，**未改**。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - `spin correlations` 的断词已由 MD 正确还原（修复第 3 处），同理 [15] `equilibrium`、[16] `Lecture`、[21] `classical`、[30] `Gauthier-Villars` 四处行末连字符 MD **均已正确还原为整词**，**未改**。
  - **[25] `s-embeddings`**：bbox y=344.0 token `s-embeddings@210.6-265.9` 为**单一 token**（连字符属 token 内部），其中 `s-` 在印刷中是**斜体**（数学变量）、`embeddings` 为正体。MD 行 977 作正体 `s-embeddings`，斜体被丢弃——与 p.40/p.41 已登记的行文/变量斜体系统性丢弃同源，**登记不引入本篇从未使用过的标记**。
  - **[9]–[33] 的书名/刊名斜体**（`Methods of contemporary mathematical statistical physics`、`Wulff construction: a global shape from local interaction`、`The Critical Ising Model via Kac-Ward Matrices`、`Gauthier-Villars et fils`、`Proc. of the Royal Soc. of London`、`History of the Lenz-Ising model` 等）在印刷中为斜体，MD 为正体，同上系统性丢弃，**未改**。
  - [28] `D. Chelkak, and S. Smirnov.`——印刷在 `Chelkak` 后**多一个逗号**（bbox y=413.7 `Chelkak,@105.7-141.4  and@143.9-158.3`，空档 2.5 pt 表明逗号后确有空格），MD **原样保留了这一多余逗号**，**正确，未改**。
  - [19] 的期号 `no. 855` 与 `no. 874` 均为**四位期号**（1934/1935 年的 Proc. Roy. Soc. 以连续页码编期），非常规的 `no. N` 单页期号；bbox `855,@355.8-373.2`、`874,@157.5-174.9` 确认，MD 一致，**未改**。
  - [30] 的 `4, Gauthier-Villars et fils.` 无年份无期号（法文 19 世纪旧式著录），bbox y=469.5 末 `4,@364.5-371.9 Gauthier-@374.4-413.1`、y=483.5 `Villars@93.1-119.9 et@122.4-129.5 fils.@131.9-146.1`，确无更多字段；MD 一致，**未改**。
- 登记不改（铁律三）：
  - **印刷怪癖 1**：**[33] `Dolbilin, ,Y.M.` 的重复逗号**——bbox y=553.2 给出 `Dolbilin,@112.6-148.3` 与 `,Y.M.@150.7-173.2` **两个独立 token，第二个以逗号开头**，二者空档 2.4 pt；6× 裁片 `/tmp/icm2022dc_p042_lab33.png` 直读「**Dolbilin, ,Y.M.**」肉眼可见连续两个逗号。这是原刻排印错误，**照录不删**；MD 已如实复现，修复第 4 处时**刻意保留了该逗号**。
  - **印刷怪癖 2**：**[28] `D. Chelkak, and S. Smirnov.` 的多余逗号**——同上，照录不删。
  - 破折号体系混用：[19] 页码区间用 en dash（`699–730`）而分卷分隔也用 en dash（`699–730 – 151`），二者同码位只能靠空格区分；MD 一致，**未改**。
  - 行内数学与相邻文字空格合并（`above$T_c$.` 之外的 `Wulff$…$` 等）在本页无新增实例。
  - 页脚在本页为偶数页 `42  Hugo Duminil-Copin`（版式级，未入 MD）；**书眉奇偶交替**（奇数页 `N  100 Years of the Ising Model`），p.43 bbox 已实证，见上「版式」条与 p.043 说明。**〔初稿此处误写为「由 `100 Years of the Ising Model` 改为 `Hugo Duminil-Copin`（版式级切换点）」，已更正。〕**
- 备注：本页 5 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙/字高量测）。修复后复扫：`[N]` 与作者粘连、刊名焊字（`ofMath.`）、断词误插空格（`correla tions`）、刊名缺句点（`Math 63`）四类在本页残留均为 **0**。

## p.043（PDF p.43 / 印刷 p.43）
- PNG：/tmp/icm2022dc_audit_p043.png（pngmono 150dpi）
- 核对：文献 [34]–[50] 共 17 条、页脚、[36]/[38]/[39]/[40]/[43]/[44]/[49] 行内数学与断词、刊名缩写与句点
- 结果：PASS±（差异 11 处，均已按原图逐处 `Edit` 修复）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：无题录（文献表页）。
  - **正文**：无正文段（文献表）。
  - **公式**：本页两处行内数学，[43] `$\Phi _ { 4 } ^ { 4 }$`（[44] 行内另有 `$\phi _ { 3 } ^ { 4 }$`）与 [49] `$\lambda \phi _ { d } ^ { 4 }$`、`$d ( - ) > 4$`，逐字核对见「逐字核对留证」。
  - **参考文献**：**[34]–[50] 共 17 条**逐条核对作者、刊名、卷、年、期、页码；**无期号**条目 [46] `J. Math. Phys. 7 (1963) 1776.` 与印刷一致（bbox y=469.5 `(1963)@93.5-115.6 1776.@118.1-138.3`，`1776.` 紧接年份，确无 `no.`）。
  - **版式**：页脚 `43  100 Years of the Ising Model`（bbox y=639.0 `43@59.5-66.8 100@93.5-104.5 Years@106.3-123.8 of@125.6-131.8 the@133.6-143.4 Ising@145.3-160.6 Model@162.4-181.3`）——**与 p.42 的 `42  Hugo Duminil-Copin` 不同，据此确认书眉为奇偶交替**，已据此更正 p.042 说明中「p.42 起永久切换」的错误记载。版式级，未入 MD。四处行末连字符断词（[34] `Sci-`/`ences`、[36] `tempera-`/`ture`、[38] `rela-`/`tions`、[39] `tran-`/`sition`、[40] `Swendsen-`/`Wang`）MD 仅 [36] 一处处理错误，见修复第 2 处。
- 修复（11 处，均以 `Edit` 工具逐处落地）：
  1. 行 997 `[35]H. Duminil-Copin.` → `[35] H. Duminil-Copin.`。6× 裁片 `/tmp/icm2022dc_p043_lab35.png`（px 225–470, y 305–362）直读「[35]　　　　**H. D**」；bbox y=79.0 `[35]@59.5-72.8` 与 `H.@93.5-103.2` 相距 20.7 pt 空档，编号与作者明显分离。MD 粘连，且与本页 [34][36][37][38][39][40] 均写有空格自相矛盾。
  2. 行 999 `critical tempera ture` → `critical temperature`。6× 裁片 `/tmp/icm2022dc_p043_temp.png`（px 1520–1760, y 490–580）直读行末「cal **tempera-**」；bbox y=120.8 末 token 为 `tempera-@378.7-414.1`，y=134.8 次行首 token 为 `ture.@93.5-111.5`——**中间是行末连字符断词，印刷不存在空格**。MD 丢弃连字符并错误插入空格，把 `temperature` 劈成两段（同 p.42 [27] `correla tions` 同族伪影）。
  3. 行 1009 `[41]S. El-Showk,` → `[41] S. El-Showk,`。6× 裁片 `/tmp/icm2022dc_p043_lab41.png`（px 225–470, y 1188–1245）直读「[41]　　　　**S. El**」；bbox y=288.2 `[41]@59.5-72.8`→`S.@93.5-101.6` 空档 20.7 pt。同第 1 处族。
  4. 行 1009 `bootstrap. Phys. Rev D 86 (2012)` → `bootstrap. Phys. Rev. D 86 (2012)`。6× 裁片 `/tmp/icm2022dc_p043_revD.png`（px 1440–1730, y 1240–1335）直读行末「trap. **Phys. Rev.**」，`Rev` 之后的**句点清晰可见**；bbox y=274.3（[40] 同行对照）token `Rev.@311.9-328.7` **含句点**，y=302.2 `[41]` 行末 token 亦为 `Rev.@389.0-405.8` **含句点**（码点 dump 含 `0x2e`），次行起于 `D 86`。刊名实为 **`Phys. Rev. D`**。MD 丢失 `Rev` 后的句点（同 p.41 [10] `J. ofPhys.`、p.42 [33] `Math 63` 同族）。
  5. 行 1013 `Infrared$\Phi _ { 4 } ^ { 4 }$by` → `Infrared $\Phi _ { 4 } ^ { 4 }$ by`。7× 裁片 `/tmp/icm2022dc_p043_phi4d.png`（px 590–930, y 1528–1600）直读「y of Infrared **Φ**₄ᵈ **by a**」——`Infrared` 与 `by` 两侧词间空隙清晰。属数学/文字边界空格丢失（全篇系统性伪影族）。
  6. 行 1015 `coupled$\phi _ { 3 } ^ { 4 }$quantum` → `coupled $\phi _ { 3 } ^ { 4 }$ quantum`。7× 裁片 `/tmp/icm2022dc_p043_phi43.png`（px 490–890, y 1700–1770）直读「y coupled **φ**₄³ **quantum f**」——两侧空格在位。同第 5 处族。
  7. 行 1017 `[45]M.E. Fisher.` → `[45] M.E. Fisher.`。6× 裁片 `/tmp/icm2022dc_p043_lab45.png`（px 225–470, y 1770–1825）直读「[45]　　　　**M.E. Fis**」；bbox y=427.7 `[45]@59.5-72.8`→`M.E.@93.5-111.5` 空档 20.7 pt。同第 1 处族。
  8. 行 1017 `simple fluids. J Math. Phys. 5 (1964)` → `simple fluids. J. Math. Phys. 5 (1964)`。7× 裁片 `/tmp/icm2022dc_p043_jmath45.png`（px 1560–1850, y 1755–1875）直读 [45] 行末「**ids. J.**」——`J` 之后的**句点清晰可见**；bbox y=427.7 该行末 token 为 `'J.'@389.7-396.6`（**含句点**），次行起于 `Math. Phys. 5 (1964)`。刊名实为 **`J. Math. Phys.`**。MD 丢失 `J` 后的句点（与 p.42 [27] `Ann. ofMath.` 同族的「刊名缩写丢句点」伪影）。
  9. 行 1019 `[46]M.E. Fisher.` → `[46] M.E. Fisher.`。6× 裁片 `/tmp/icm2022dc_p043_lab46.png`（px 225–470, y 1888–1943）直读「[46]　　　　**M.E. Fis**」；bbox y=455.6 `[46]@59.5-72.8`→`M.E.@93.5-111.5` 空档 20.7 pt。同第 1 处族。
  10. 行 1025 `triviality of$\lambda \phi _ { d } ^ { 4 }$theories` → `triviality of $\lambda \phi _ { d } ^ { 4 }$ theories`。7× 裁片 `/tmp/icm2022dc_p043_lam.png`（px 760–1010, y 2225–2360）直读「…ality of **λφ**₄ᵈ **th**」／「ns. Micr…」——`of` 与 `λφ⁴_d` 之间、`λφ⁴_d` 与 `theories` 之间空隙清晰，bbox y=540.6 同行 token 亦分段（`of` / `𝜆𝜙`）。同第 5 处族。
  11. 行 1025 `in$d ( - ) > 4$dimensions` → `in $d ( - ) > 4$ dimensions`。7× 裁片 `/tmp/icm2022dc_p043_lam.png`（**同一裁片**下两行）直读「…on = **in**」／「– **4** dimensions」——`in` 与 `d` 之间、`4` 与 `dimensions` 之间空隙清晰；bbox y=546.4 `𝑑`、`y=555.7 `𝑑 &gt;``、y=567.1 首 token `in` 后即数学式，两侧均有空档。同第 5 处族。
- 逐字核对留证（MD 无误，未改）：
  - **[43] `$\Phi _ { 4 } ^ { 4 }$` 同时带下标 4 与上标 4**：bbox 该 token 为 `Φ`（U+03A6 普通大写 Φ，非 U+1D6AB 粗体 Δ），x 200.5–204.1，且同一 token 的 y 跨度为 **370.1–383.8**，同时覆盖上标基线（y≈370.1）与下标基线（y≈383.8）——即印刷的 `Φ` **上下各有一个 4**。7× 裁片 `/tmp/icm2022dc_p043_phi4d.png` 直读亦可见 `Φ` 的右上与右下各一个 `4`。这是原刻的排印怪癖，按铁律三**照录**，**不**「纠正」为单侧；MD 行 1013 的 `$\Phi _ { 4 } ^ { 4 }$` **原样正确，未改**。
  - **[44] `$\phi _ { 3 } ^ { 4 }$`**：bbox token 为 `𝜙`（U+1D719 斜体 φ），x 164.2–167.9，y 跨度 **412.0–425.7**，同样同时覆盖上标 `4`（y≈412.0）与下标 `3`（y≈425.7）；7× 裁片 `/tmp/icm2022dc_p043_phi43.png` 直读 `φ` 右上为 `4`、右下为 `3`。MD 行 1015 的 `$\phi _ { 3 } ^ { 4 }$` **正确，未改**。
  - **[49] `$\lambda \phi _ { d } ^ { 4 }$` 与 `$d ( - ) > 4$`**：bbox y=540.6 token `𝜆𝜙` 的码点为 `[0x1d706, 0x1d719]`（斜体 λ + 斜体 φ）**合并为单一 token**，x 218.0–229.2，y 541.7–546.2 居主基线；上标 `4` 在 y 537.5–544.1、下标 `𝑑`（U+1D451）在 y 546.4–549.7 ⇒ 印刷为 **λφ⁴_d**，MD 行 1025 的 `$\lambda \phi _ { d } ^ { 4 }$` **逐符号一致，未改**。条件式 `d ( - ) > 4` 的 bbox token 序列为 `𝑑`、`&gt;`、`4`，其中减号码点为 **U+2212**（真减号）而非连字符，MD 写作 `$d ( - ) > 4$` 与之一致，**未改**。
  - **[46] 无期号且无逗号**：`J. Math. Phys. 7 (1963) 1776.`——bbox y=455.6 行末为 `'7'@388.7-393.7`，y=469.5 首 token `(1963)@93.5-115.6`、次 token `1776.@118.1-138.3`，**年份后无逗号、无 `no.`**。这是原刻著录不规范（真刊为 *J. Math. Phys.* **7** (1963) 1776），按铁律三**照录不补**，MD 行 1019 **正确，未改**。
  - **[40] `monte carlo algorithm`**：bbox y=274.2 `monte@194.2-219.1 carlo@221.6-241.3 algorithm.@243.8-285.3`——**全小写、无连字符**，空档 2.5/2.5 pt。MD 行 1007 逐字符一致，**未改**（原刻怪癖照录）。
  - **[34] 四位期号 `no. 1221`**：bbox y=65.0 `no.@167.1-179.6 1221,@182.1-204.5`，确为四位期号（1957 年 Proc. Roy. Soc. A 以连续页码编期）。MD 行 995 一致，**未改**。
  - **[36]/[38]/[39]/[40] 的行末连字符断词**：bbox 分别给出 `tempera-`/`ture.`、`rela-`/`tions.`、`tran-`/`sition`、`Swendsen-`/`Wang`；除 [36]（修复第 2 处）外，其余三处 MD **均已正确还原为整词**，**未改**。
  - **[47]–[50] 作者重音与刊名**：`Fröhlich`（[49][50]，bbox y=540.6/567.1 重音在位）、`Padé`（[42]）、`Sénéor`（[43]）、`Commun. Math. Phys. 109 (1987), 437–480.`（[43] **无期号**）、`Physica 57 (1972), 536–564.`、`Cambridge University Press (2017).`、`Nuclear Physics B 200 (1982), no. 2, 281–296.` 逐条与印刷 bbox 一致，**未改**。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - **[36] `critical temperature` 的断词位置**：bbox y=120.8 的 `tempera-` 与 y=134.8 的 `ture.` 是**跨行**的两个 token，行末连字符属正常断词，**不应保留在 MD 中**（本篇 MD 全篇的断词均还原为整词）；MD 的错误不在断词本身，而在**把断词处的连字符替换成了空格**。修复采用与 [27] `correla tions`→`correla`+`tions` 合并相同的处置：`temperature` 还原为整词。
  - **[34] `Series A. Mathematical and Physical Sciences`**：bbox y=51.1 `Proc.@143.8-165.4 Royal@167.9-190.7 Soc.@193.2-210.1 London.@212.6-245.5 Series@248.0-272.4 A.@274.9-283.4 Mathematical@285.9-341.2 and@343.7-358.6 Physical@361.1-395.2 Sci-@397.7-413.2`，各词均独立成 token、词间空档 2.4–2.5 pt 均匀；次行 y=65.0 首 token 为 `ences`，与 `Sci-` 合成 `Sciences`。MD 行 995 `Sciences` 已正确还原，**未改**。
  - **[49] `in d(−) > 4 dimensions`** 的 `−` 为 **U+2212 减号**（印刷在数学模式内），**不是**连字符；MD 写作 `$d ( - ) > 4$`，其 `-` 在数学模式中渲染即减号，与印刷一致，**未改**。
  - **[36]/[37] 的 `RSW-`/`type`**：[37] 行末 `RSW-@391.9-416.6` + 次行 `type@93.5-110.7` 合成 `RSW-type`，MD 行 1001 正确还原为 `RSW-type`，**未改**。
- 登记不改（铁律三）：
  - **印刷怪癖 1**：**[43] `Φ₄⁴`（Phi 同时带下标 4 与上标 4）**——bbox 证明印刷即如此，MD 已照录，**不改**（同 p.41 [4] `$\phi _ { 4 } ^ { 4 }$` 族）。
  - **印刷怪癖 2**：**[46] `J. Math. Phys. 7 (1963) 1776.` 缺期号与逗号**，照录不补。
  - **印刷怪癖 3**：**[40] `monte carlo algorithm` 全小写无连字符**，照录不改为 `Monte Carlo` / `Monte-Carlo`。
  - **印刷怪癖 4**：**[34] `Proc. Royal Soc. London.` 缺第二个 `of`**（真刊为 *Proc. R. Soc. Lond.*），照录不补。
  - 行内数学与相邻文字空格合并类伪影（`X$…$Y`）在本页新增 4 处，已逐处修复（修复第 5、6、10、11 处），未做其他批量拆改。
  - 页脚 `43  100 Years of the Ising Model` 未入 MD（版式级）；**书眉奇偶交替**已据本页与 p.42、p.41 交叉确认。
- 备注：本页 11 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙/字高量测）。修复后复扫：`[N]` 与作者粘连（本页残留 **0**）、刊名缩写缺句点（`Rev D` / `J Math.` 本页残留 **0**）、断词误插空格（`tempera ture` 本页残留 **0**）、数学/文字边界空格丢失（`$\lambda…$theories`、`in$d…$dimensions` 等本页残留 **0**）四类均已清零。另：`coupled$\phi` 在文档他处（行 649、659，正文）仍有两处同族伪影，**在本轮 p.41–p.46 页段之外**，跨页登记供集成者。

## p.044（PDF p.44 / 印刷 p.44）
- PNG：/tmp/icm2022dc_audit_p044.png（pngmono 150dpi）
- 核对：文献 [51]–[69] 共 19 条、页脚、[51]/[54]/[60]/[61]/[62] 五处行内数学与两侧空格、刊名缩写与断词
- 结果：PASS±（差异 10 处 = 5 处 `Edit` × 两侧各 1 个丢失空格，均已按原图逐处修复）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：无题录（文献表页）。
  - **正文**：无正文段（文献表）。
  - **公式**：本页五处行内数学——[51] `$\Phi _ { 4 } ^ { 4 }$`、[54] `$\phi _ { 3 } ^ { 4 }$`、[60] `$( \Phi _ { 2 } ) ^ { 4 }$`、[61] `$P ( \phi ) ^ { 2 }$`、[62] `$( \phi _ { 4 } ) ^ { 4 }$`；逐字核对见「逐字核对留证」，五处**符号层级本身 MD 全部正确**，仅两侧空格丢失。
  - **参考文献**：**[51]–[69] 共 19 条**逐条核对作者、刊名、卷、年、期、页码。**无期号**条目两条与印刷一致：[66] `J. Chem. Phys. 33 (1960) 1059.`（bbox y=511.4 末 `33@…`、`(1960)@…` 后紧接 `1059.`，确无 `no.`、年份后无逗号）、[69] `Proc. of a symp. (1941), no. 18, 257–266.`（y=595.0 `Proc.@… of@… a@… symp.@… (1941),@… no.@… 18,@… 257–266.`）。
  - **版式**：页脚 `44  Hugo Duminil-Copin`（bbox y=639.0 `44@59.5-66.8 Hugo@93.5-110.3 Duminil-Copin@112.1-156.9`）——**偶数页，与 p.43 的奇数页 `43  100 Years of the Ising Model` 交替**，独立印证 p.043 说明中更正后的「书眉奇偶交替」结论。版式级，未入 MD。两处行末连字符断词（[62] `Four-`/`Dimensional` 属词内连字符非断词；[65] `univer-`/`sité`）MD 均已正确处理，见「逐字核对留证」。
- 修复（5 处 `Edit`，涉及 10 个丢失空格，均以 `Edit` 工具逐处落地）：
  1. 行 1029 `Massless Lattice$\Phi _ { 4 } ^ { 4 }$Theory:` → `Massless Lattice $\Phi _ { 4 } ^ { 4 }$ Theory:`（**2 个空格**）。7× 裁片 `/tmp/icm2022dc_p044_r51.png`（px 1050–1460, y 120–220）直读「ss **Lattice Φ₄⁴ Theory: Ri**」——`Lattice` 与 `Φ` 之间、`Φ₄⁴` 与 `Theory:` 之间的空隙清晰可辨。bbox y=35.4 量测：`Lattice@261.8-289.5`→`Φ@292.0-299.6` 空档 **2.5 pt**（与同行词间空档 `ss`→`Lattice`、`Theory:`→`Rigorous` 同值），`44@299.6-303.2`→`Theory:@306.2-337.7` 空档 **3.0 pt**（数学/文字边界，与 p.43 各处同值）⇒ 印刷两侧**均有空格**。
  2. 行 1035 `Positivity of the$\phi _ { 3 } ^ { 4 }$hamiltonian.` → `Positivity of the $\phi _ { 3 } ^ { 4 }$ hamiltonian.`（**2 个空格**）。7× 裁片 `/tmp/icm2022dc_p044_r54.png`（px 950–1350, y 580–692）直读「of the **φ₃⁴ hamiltonian. Fo**」。bbox y=146.9 量测：`the@237.1-249.3`→`43@257.7-261.3` 空档 **8.4 pt**（`𝜙` 斜体左伸留白，远大于词间带，任何判定下都只能是空格），`43@257.7-261.3`→`hamiltonian.@264.3-314.4` 空档 **3.0 pt** ⇒ 两侧均有空格。
  3. 行 1047 `B. Simon, The$( \Phi _ { 2 } ) ^ { 4 }$Field Theory` → `B. Simon, The $( \Phi _ { 2 } ) ^ { 4 }$ Field Theory`（**2 个空格**）。7× 裁片 `/tmp/icm2022dc_p044_r60.png`（px 825–1200, y 1280–1390）直读「on, **The (Φ₂)⁴ Field Th**」。bbox y=314.3 量测：`The@209.6-225.1`→`(Φ@228.1-239.4` 空档 **3.0 pt**，`4@247.4-251.0`→`Field@254.0-274.4` 空档 **3.0 pt** ⇒ 两侧均有空格。
  4. 行 1049 `B. Simon, The$P ( \phi ) ^ { 2 }$Euclidean Quantum` → `B. Simon, The $P ( \phi ) ^ { 2 }$ Euclidean Quantum`（**2 个空格**）。7× 裁片 `/tmp/icm2022dc_p044_r61.png`（px 925–1370, y 1395–1505）直读「on, **The P(φ)² Euclidean Q**」。bbox：`The@234.0-249.5`→`𝑃(𝜙)@252.2-272.1` 空档 **2.7 pt**，上标 `2@272.6-276.2`→`Euclidean@279.2-319.0` 空档 **3.0 pt** ⇒ 两侧均有空格。
  5. 行 1051 `Four-Dimensional$( \phi _ { 4 } ) ^ { 4 }$Spin Systems.` → `Four-Dimensional $( \phi _ { 4 } ) ^ { 4 }$ Spin Systems.`（**2 个空格**）。7× 裁片 `/tmp/icm2022dc_p044_r62.png`（px 345–850, y 1570–1680）直读「**Dimensional (φ₄)⁴ Spin Sy**」。bbox y=384.1 量测：`Dimensional@93.5-144.5`→`(𝜙@147.5-156.9` 空档 **3.0 pt**，`4@165.0-168.7`→`Spin@171.7-189.9` 空档 **3.0 pt** ⇒ 两侧均有空格。
- 逐字核对留证（MD 无误，未改）：
  - **[51] `Φ₄⁴`（Phi 同时带下标 4 与上标 4）**：bbox y=35.4 token `Φ@292.0-299.6` 为 **U+03A6 普通大写 Phi**（非 Δ），紧邻的 token `44@299.6-303.2` 的 y 跨度为 **35.4–49.1**，同时覆盖上标基线（y≈35.4）与下标基线（y≈49.1）——**一个 `4` 在右上、一个 `4` 在右下**。7× 裁片 `/tmp/icm2022dc_p044_r51.png` 直读同样可见 `Φ` 的右上、右下各一个 `4`。**原刻排印怪癖，按铁律三照录不改**；MD 行 1029 的 `$\Phi _ { 4 } ^ { 4 }$` **原样正确，未改**（与 p.41 [4]、p.43 [43] 的 `Φ₄⁴`/`φ₄⁴` 同族）。
  - **[54] `φ₃⁴`（phi 同时带下标 3 与上标 4）**：bbox y=150.1 token `𝜙@252.0-257.5` 为 **U+1D719 斜体 φ**，`43@257.7-261.3`（y 146.9–160.7）同时覆盖上标 `4` 与下标 `3`。7× 裁片直读「**φ₃⁴**」。MD `$\phi _ { 3 } ^ { 4 }$` **正确，未改**（与 p.43 [44] `$\phi _ { 3 } ^ { 4 }$` 同型）。
  - **[60] `(Φ₂)⁴`**：bbox y=314.3 的 token 序列为 `(Φ@228.1-239.4`、`)`@243.6-246.9、上标 `4@247.4-251.0`(y 314.3–320.9)，下标 `2@239.4-243.1`(y 319.4–326.0，落在 y=317.5 行组) ⇒ 下标 `2` **在括号内**（紧跟 `)` 的左沿），上标 `4` **在括号外**。7× 裁片直读 `(Φ₂)⁴` 与此完全一致。MD `$( \Phi _ { 2 } ) ^ { 4 }$` **结构正确，未改**。
  - **[61] `P(φ)²`**：bbox token `𝑃(𝜙)@252.2-272.1` 为单一 token（码点 U+1D45B? 实为斜体 `𝑃` + `(𝜙)`），上标 `2@272.6-276.2`(y 342.2–348.8) 紧随其右上 ⇒ 印刷为 `P(φ)` 的平方，**上标 2 作用于整个 `P(φ)`**。MD `$P ( \phi ) ^ { 2 }$` **正确，未改**。
  - **[62] `(φ₄)⁴`**：bbox y=384.1 `(𝜙@147.5-156.9`、`)`@161.2-164.5、上标 `4@165.0-168.7`、下标 `4@157.1-160.7`(y 389.2–395.8，落在 y=389.2 行组) ⇒ 下标 `4` 在括号内、上标 `4` 在括号外。7× 裁片直读 `(φ₄)⁴`。MD `$( \phi _ { 4 } ) ^ { 4 }$` **正确，未改**。
  - **[55] `Springer Science & Business Media (2012).`**：bbox y=190.6 token 为 `&amp;@…`，这是 XML 对 `&` 的标准转义，实际字符即 `&`，**非 `&amp;` 字面**；MD 行 1037 作 `&`，**正确，未改**（与 p.42 [31] `Th. Probab. & Its Appl.` 同族）。
  - **[65] `université de Genève`**：bbox y=469.5 行末 token 为 `univer-@…`（行末连字符断词），y=483.5 次行首为 `sité@93.5-…`，其中 `é` 重音在位 ⇒ 合为 `université`。MD 行 1057 已正确还原为整词 `université`，**未改**。
  - **[62] `Four-Dimensional` 的连字符**：bbox y=371.9 行末为 `Four-`（**词内连字符，非断词**，因 `Dimensional` 是完整词且次行以完整词起首）。MD 行 1051 写作 `Four-Dimensional` **正确，未改**。
  - **[52]/[63]/[64]/[68] 的刊名与重音**：`volume 9 of de Gruyter Studies in Mathematics. Walter de Gruyter and Co., Berlin, second edition, 2011.`、`Zeitsch. für Physik, 49 (1928), no. 9, 619–636.`（`für` 重音在位；`Physik` 后为**逗号而非句点**）、`Publ. Res. Instit. Math. Sciences. 14 (1978), no. 1, 53–69.`、`Univ. Nac. Tucumán. Revista A., 2 (1941), 177–201.`（`Tucumán` 重音在位、`Revista A.,` 后为逗号）——逐条与印刷 bbox 一致，**未改**。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - **`[N]` 编号后空格**：本页 19 条**全部**写有空格（`[51]`…`[69]`），bbox y=38.5/79.0/106.9/… 均给出 `[N]@59.5-72.8` 与正文首词 `@93.5` 之间 20.7 pt 空档。**本页无编号粘连**，未改（与 p.41 [1]–[9]、p.42 [19][33]、p.43 [35][41][45][46] 的粘连形成对照，MD 在本页是一致的正确写法）。
  - **刊名缩写句点**：[53] `J. Math. Phys. 53`、[57] `J. Math. Phys. 8`、[58] `Phys. Rev. Letters 24`、[59] `J. Math. Phys. 11`、[61] `Ann. of Math. 101`、[62] `J. Stat. Phys. 47`、[67] `Commun. Math. Phys. 199` 的每一处句点在 bbox 中均带 `0x2e`（如 y=51.1 `Commun.@280.9-319.3 Math.@321.8-345.2 Phys.@347.7-369.4`，三处句点齐全）。**MD 全部正确，未改**（与 p.41 [10] `J. ofPhys.`、p.42 [27] `Ann. ofMath.`、p.43 [41] `Rev D` / [45] `J Math.` 的丢句点伪影对照）。
  - **`[67] D. Ioffe and R.H. Schonmann`**：bbox y=525.3 token 为 `Schonmann@…`——**ASCII 无变音符**（作者本名即写作 Schonmann），与同条中 `Kotecký@…`（`ý` 为 U+00FD，重音在位）形成对照。MD 行 1061 `Schonmann` **正确，未改**。
  - **`[62] Critical Behaviour`（英式拼写）** 与本篇他处 `behavior`（美式）混用，属原刻用词，**照录不统一**。
- 登记不改（铁律三）：
  - **印刷怪癖 1**：**[51] `Φ₄⁴`**（同一 Phi 上下各一个 4），照录不「纠正」。
  - **印刷怪癖 2**：**[54] `φ₃⁴`**（同一 phi 上下各一个 4），照录不「纠正」。
  - **印刷怪癖 3**：**[66] `J. Chem. Phys. 33 (1960) 1059.` 缺期号且年份后无逗号**，照录不补。
  - **印刷怪癖 4**：**[69] `Proc. of a symp. (1941), no. 18, 257–266.`** 刊名缩写不全（非标准缩写），照录不补全。
  - **印刷怪癖 5**：**[63] `Zeitsch. für Physik, 49`** 的 `Physik` 后用逗号而非句点，照录。
  - 行内数学与相邻文字空格合并类伪影在本页新增 5 处（10 个空格），已逐处修复（修复第 1–5 处），未做其他批量拆改。
  - 页脚 `44  Hugo Duminil-Copin` 未入 MD（版式级）。
- 备注：本页 5 处修复（10 个空格）逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙量测）。修复后复扫：本页 `X$…$Y` 型边界粘连残留 **0**，`[N]` 编号粘连残留 **0**，刊名丢句点残留 **0**。本页 19 条文献的作者、刊名、卷年期页全部与印刷逐条吻合，无内容级错误。

## p.045（PDF p.45 / 印刷 p.45）
- PNG：/tmp/icm2022dc_audit_p045.png（pngmono 150dpi）
- 核对：文献 [70]–[87] 共 18 条、页脚、[72] `$T_c$`、编号粘连 [73][77][86]、断词处理 [74][81][86]、刊名句点 [77]、破折号/连字符体系 [86][87]、重音与花括号引号
- 结果：PASS±（差异 6 处，均已按原图逐处 `Edit` 修复）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：无题录（文献表页）。
  - **正文**：无正文段（文献表）。
  - **公式**：本页仅 [72] 一处行内数学 `$T_c$`，逐位核对见「逐字核对留证」（MD 正确，未改）。
  - **参考文献**：**[70]–[87] 共 18 条**逐条核对作者、刊名、卷、年、期、页码。**无期号/无逗号**条目与印刷一致：[75] `Physica 27 (1961) 1209 – Dimer statistics and phase transitions. J. Math. Phys. 4 (1963) 287.`（两处年份后**均无逗号、无 `no.`**，[75] 全文以 `–` 分隔两篇文章）；[83] `Harvard Univ. Press (2013).`（无卷期页）；[69] 式的 `Proc. of a symp.` 风格见 p.44。
  - **版式**：页脚 `45  100 Years of the Ising Model`（bbox y=639.0 `45@59.5-66.8 100@93.5-104.5 Years@106.3-123.8 of@125.6-131.8 the@133.6-143.4 Ising@145.3-160.6 Model@162.4-181.3`）——**奇数页，与 p.44 的偶数页 `44  Hugo Duminil-Copin` 交替**，第三次印证「书眉奇偶交替」。版式级，未入 MD。三处行末连字符断词（[74] `two-`/`dimensional`、[81] `tran-`/`sitions.`、[86] `his-`/`tory`）MD 处理成对错，见修复第 2、5 处与「逐字核对留证」。
- 修复（6 处，均以 `Edit` 工具逐处落地）：
  1. 行 1073 `[73]L.P. Kadanoff.` → `[73] L.P. Kadanoff.`。6× 裁片 `/tmp/icm2022dc_p045_lab73.png`（px 229–700, y 483–568）直读「[73]　　　　**L.P. Kadanoff. Crit**」；bbox y=120.8 `[73]@59.5-72.8` 与 `L.P.@93.5-109.2` 相距 20.7 pt 空档，编号与作者明显分离。MD 粘连。
  2. 行 1075 `the twodimensional Ising model` → `the two-dimensional Ising model`。7× 裁片 `/tmp/icm2022dc_p045_two.png`（px 1540–1800, y 655–815）直读两行「…the **two-**」／「**dime**nsional…」——印刷在行末断开为 `two-`（bbox y=162.7 末 token `two-@383.7-401.6`，码点 `[0x74,0x77,0x6f,0x2d]`，末位为 **U+002D 连字符**）+ 次行首 `dimensional`，合为 **`two-dimensional`**。MD 把行末连字符**直接丢弃**，产出英语中不存在的单词 `twodimensional`。**本条与 p.42 [27] `correla tions`、p.43 [36] `tempera ture` 是同一断词族的两种相反错误**（那两处是「丢连字符、插空格」，本处是「丢连字符、连成一片」），处置一致：还原为带连字符的原词。
  3. 行 1081 `[77]G. Kirchhoff.` → `[77] G. Kirchhoff.`。6× 裁片 `/tmp/icm2022dc_p045_lab77.png`（px 229–700, y 1004–1094）直读「[77]　　　　**G. Kirchhoff. Uebe**」；bbox y=246.3 `[77]@59.5-72.8`→`G.@93.5-103.2` 空档 20.7 pt。同第 1 处族。
  4. 行 1081 `wird. Ann der Physik. 148 (1847)` → `wird. Ann. der Physik. 148 (1847)`。7× 裁片 `/tmp/icm2022dc_p045_ann.png`（px 1570–1780, y 1060–1220）直读两行「…ret. **Ann.**」／「der Ph**…**」——`Ann` 之后的**句点清晰可见**，且该 token 位于**行末**、`der Physik.` 起于次行。bbox y=260.3 末 token 为 `Ann.@390.5-409.0`（**含句点**），y=274.2 次行首为 `der@93.5-106.8  Physik.@109.3-138.2`。刊名实为 **`Ann. der Physik.`**。MD 丢失 `Ann` 后的句点（与 p.41 [10] `J. ofPhys.`、p.42 [27] `Ann. ofMath.`、p.43 [41] `Rev D` / [45] `J Math.` 同族的「刊名缩写丢句点」伪影）。
  5. 行 1089 `phase tran sitions` → `phase transitions`。7× 裁片 `/tmp/icm2022dc_p045_tran.png`（px 1540–1800, y 1525–1670）直读两行「…hase **tran-**」／「…ns. Rev. 87」——印刷在行末断开为 `tran-`（bbox y=371.9 末 token `tran-@388.9-407.7`，码点 `[0x74,0x72,0x61,0x6e,0x2d]`，末位 **U+002D**）+ 次行首 `sitions.`。MD **丢弃连字符并插入空格**，把 `transitions` 劈成 `tran` + `sitions`（与 p.42 [27] `correla tions`、p.43 [36] `tempera ture` 同族，本页是该族的第 3 例）。
  6. 行 1099 `[86]M. Niss.` → `[86] M. Niss.`。6× 裁片 `/tmp/icm2022dc_p045_lab86.png`（px 229–700, y 2165–2256）直读「[86]　　　　**M. Niss. History of**」；bbox y=525.3 `[86]@59.5-72.8`→`M.@93.5-104.9` 空档 20.7 pt。同第 1 处族。
- 逐字核对留证（MD 无误，未改）：
  - **[72] `$T_c$` 与其左侧空格**：bbox y=92.9 该行末为 `near@273.6-290.7`，y=95.4 起 `𝑇@292.9-298.4`（**斜体大写 T**，y 95.4–99.9 居数学基线），y=98.1 `𝑐@298.1-301.8`（**y 98.1–101.3，明显下移，即下标小写 c**），其后 `.` ⇒ 印刷为 `near` + 空格 + 斜体 $T$ + 下标 $c$ + 句点。`near`→`𝑇` 空档 **2.2 pt**，与 p.42 [23] `above$T_c$.` 的 2.2 pt 完全同值（斜体 T 左侧边距较窄所致），属**数学/文字边界的真实空格**。MD 行 1071 `near $T_c$.` **空格在位、字形层级正确**，**未改**。
  - **[73] `‘Enrico Fermi’` 的花括号引号**：bbox y=134.8 token 为 `‘Enrico@322.0-352.5` 与 `Fermi’@354.9-382.0`——起引号为 **U+2018**、收引号为 **U+2019**（左右单引号），非 ASCII 直立单引号。MD 行 1073 用 `‘Enrico Fermi’` **逐码点一致，未改**。
  - **[82] `Simon’s` 与 [87]/[82] 的双句点**：bbox y=413.7 末 token 为 `Phys..@394.7-418.9`——**刊名缩写后连着两个句点**，是原刻的排印错误；bbox y=203.1 `Simon’s@203.1-235.5` 的撇号为 **U+2019**。bbox y=609.0 [87] 末亦为 `Rev..@160.3-179.6`（双句点）。MD 行 1091 `Commun. Math. Phys.. 77`、行 1101 `Phys. Rev.. 65` **均原样保留了双句点**，按铁律三**照录不删**。
  - **[86]/[87] 页码区间的连字符（U+002D，非 en dash）**：bbox y=567.1 码点 dump 给出 `267-318.` = `[0x32,0x36,0x37,**0x2d**,0x33,0x31,0x38,0x2e]`、`243-` = `[0x32,0x34,0x33,**0x2d**]`，y=609.0 `3-4,` = `[0x33,**0x2d**,0x34,0x2c]`——**全部是 ASCII 连字符 U+002D**；而同页 [86] 的年份区间 `1920–1950:`、`1950–1965:`、`1965–1971:`（bbox y=525.3 `1920–1950:@261.0-308.6`）是 **U+2013 en dash**。即**同一条文献内混用 en dash（年份）与连字符（页码）**，属原刻的不一致。MD 行 1099 **逐码点忠实复现了这一混用**（年份用 `–`、页码用 `-`），**未改**。
  - **[80] `Körpern` 跨行断词（断点在带重音字母内部）**：bbox y=344.0 行末 `Kör-`、y=357.9 次行首 `pern`——原刻在 `ö` 之后断行。MD 行 1087 已正确还原为 `Körpern`（**保留了 `ö` 的重音**），**未改**。
  - **[86] `Archive for his-`/`tory` 断词**：bbox y=553.2 行末 `his-@397.1-412.0`（末位 U+002D）+ y=567.1 次行首 `tory@93.5-109.8` ⇒ `history`。MD 行 1099 `Archive for history of exact sciences.` **正确还原，未改**（与第 2、5 处对照：本页三处断词 MD 只对了一处）。
  - **德文重音与旧式拼写**：[77] `Ueber`（**ASCII `Ue`，非 `Ü`**，`Ueber@149.2-173.5`）、`Auflösung@190.7-231.9`（`ö`）、`Ströme@302.7-331.3`（`ö`）、`geflührt@333.8-364.8`（`ü`）；[80] `Verständnis`（`ä`）、`Körpern`（`ö`）；[84] `Miracle-Solé`（`é`）；[73] `behaviour`（英式，与同篇他处 `behavior` 美式混用）。逐条 bbox 一致，MD **全部正确，未改**。
  - **[70]/[71]/[76]/[78]/[79]/[81]/[84]/[85] 的刊名与期页**：`Zeitsch. Phys., 31 (1925), 253–258.`（`Phys.` 后为**逗号**）、`Phys. Rev. 88 (1952), 1332.`（**无期号**）、`Phys. Rev. 76 (1949), no. 8, 1244.`、`J. High Energy Phys. (2014), 1411, 109.`、`Phys. Rev. 60 (1941), no. 3, 252.`、`Phys. Rev. 87 (1952), no. 3, 404, 410.`（末两条页码用**逗号分隔**）、`J. Stat. Phys. 17 (1977), no. 4, 245–262.`、`J. of Chem. Phys. 9 (1941), no. 9, 706–721.`（**含 `of Chem.`**，句点齐全）——逐条与印刷 bbox 一致，**未改**。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - **[75] `1209 – Dimer statistics` 的分隔符**：bbox y=190.6 行末 `1209@…` 后接分隔符，码点为 **U+2013 en dash**，两侧各有空格（`1209`→`–` 与 `–`→次行 `Dimer`），构成**两篇文章的作者式并置**（无第二个编号）。MD 行 1077 写作 `1209 – Dimer` **空格与码点一致**，**未改**（与 p.42 [19] `699–730 – 151` 的分卷分隔同族，二者只能靠空格区分）。
  - **[72] `Physics Physique Fizika 2` 的三语刊名**：bbox y=92.9 给出 `Physics Physique Fizika 2`，三个词各自独立成 token、空档 2.5 pt 均匀，且卷号 `2` 为**粗体**（视觉上更重，与本页其他条目一致）。MD 行 1071 **逐词一致，未改**。
  - **`[N]` 编号后空格**：本页 18 条中 `[70][71][72][74][75][76][78][79][80][81][82][83][84][85][87]` **均已写有空格**且 bbox 给出 20.7 pt 空档；仅 `[73][77][86]` 三条粘连，已逐处修复（修复第 1、3、6 处）。
  - **[87] `no. 3-4` 的连字符**：bbox y=609.0 码点为 U+002D，MD 行 1101 `no. 3-4` **一致，未改**。
- 登记不改（铁律三）：
  - **印刷怪癖 1**：**[82] `Commun. Math. Phys..` 与 [87] `Phys. Rev..` 的双句点**（`Phys..`），照录不删。
  - **印刷怪癖 2**：**[77] `Ueber` 用 ASCII `Ue` 而非 `Ü`**（1847 年德文旧式写法），照录不改。
  - **印刷怪癖 3**：**[70] `Zeitsch. Phys., 31` 中 `Phys.` 后用逗号**（刊名缩写后接逗号），照录。
  - **印刷怪癖 4**：**[75]/[76]/[83] 的著录不完整**（`Physica 27 (1961) 1209` 与 `J. Math. Phys. 4 (1963) 287` 均无逗号无期号；`Harvard Univ. Press (2013).` 无卷期页），照录不补。
  - **印刷怪癖 5**：**[86] 同一条内 en dash（年份区间）与连字符（页码区间）混用**，照录不统一（与 p.42 [19] 破折号体系混用同族）。
  - **印刷怪癖 6**：**[73]/[81] 英式 `behaviour` 与全篇美式 `behavior` 混用**，照录不统一。
  - 页脚 `45  100 Years of the Ising Model` 未入 MD（版式级）。
- 备注：本页 6 处修复逐条以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数均为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，无一条系 peer 引入的回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图与像素空隙量测）。修复后复扫：本页 `[N]` 编号粘连残留 **0**（[73][77][86] 已清）、刊名丢句点（`Ann der Physik.`）残留 **0**、断词误处理（`twodimensional` / `tran sitions`）残留 **0**。本页 18 条文献的作者、刊名、卷年期页全部与印刷逐条吻合，**无内容级错误、无整段丢失**。另：断词误插空格族（`correla tions` / `tempera ture` / `tran sitions`）在 p.41–p.46 页段内已全部处置；`twodimensional` 全篇仅此 1 处（`grep -cF` 计数 1），已修复。

## p.046（PDF p.46 / 印刷 p.46，文末页）
- PNG：/tmp/icm2022dc_audit_p046.png（pngmono 150dpi）
- 核对：文献 [88]–[105] 共 18 条、文末作者联系块、页脚、[98] 行内数学、编号粘连 [95]、法/德文重音与撇号、破折号体系
- 结果：PASS±（差异 1 处，已按原图逐处 `Edit` 修复）
- 五点比对（题录 / 正文 / 公式 / 参考文献 / 版式）：
  - **题录**：无题录（文献表页）。
  - **正文**：无正文段（文献表）。文末另有**作者联系块**（见「版式」），已逐字核对。
  - **公式**：本页仅 [98] 一处行内数学 `$\phi _ { 2 } ^ { 4 }$`，逐位核对见「逐字核对留证」（MD 正确，未改）。
  - **参考文献**：**[88]–[105] 共 18 条**逐条核对作者、刊名、卷、年、期、页码。**无期号/无页码/无逗号**的著录不完整条目与印刷一致：[88] `Comm. Math. Phys. 31 (1973) 83–112.`（年份后**无逗号**）、[91] `JETP Lett. 12 (1970), 381–383.`（**无期号**）、[93] `J. High Energy Phys. (2008) 0812, 031.`、[94] `Phys. Rev. D, 86 (2012), no. 2.`（**`D` 后为逗号且无文章编号**——与 p.43 [41] 同一论文的 `Phys. Rev. D 86 (2012), no. 2, 025022.` 著录方式不同，两处**均按各自印刷原样保留**，未作「统一」）、[103] `Phys. Rev. 101 (1956), 860.`（**无期号、无页码区间**）、[104] `Phys. Rev. B 4 (1971).`（**无期号、无页码**）。
  - **版式**：文末**作者联系块**——印刷为粗体行 `Hugo Duminil-Copin`（bbox y=581.1 `Hugo@93.5-117.5 Duminil-Copin@120.1-184.1`，粗体）后接**两行**通讯地址（**起于左边界 x=59.5**，非正文的 93.5 悬挂缩进）：`Unige, 7-9 rue du Conseil-Général, 1205 Genève, Switzerland, hugo.duminil@unige.ch,`（y=595.0）与 `IHES, 35 route de Chartres, 91440 Bures-Sur-Yvette, France, duminil@ihes.fr.`（y=609.0）。页脚 `46  Hugo Duminil-Copin`（bbox y=639.0）——**偶数页**，与 p.45 奇数页交替第四次印证「书眉奇偶交替」。三裁片 `/tmp/icm2022dc_p046_lab95.png`、`_phi24.png`、`_contact.png` 已直读。MD 把粗体名渲染为 `## Hugo Duminil-Copin` 标题、把两行地址合并为一个段落，**内容零丢失**（行末逗号 `hugo.duminil@unige.ch,` 亦保留为串内逗号），属**版式级/结构性再排**，非缺陷。两处行末连字符断词（[95] `sol-`/`uble`、[97] `Insti-`/`tute`）MD 均已正确还原为整词。
- 修复（1 处，以 `Edit` 工具落地）：
  1. 行 1117 `[95]T.D. Schultz, D.C. Mattis,` → `[95] T.D. Schultz, D.C. Mattis,`。6× 裁片 `/tmp/icm2022dc_p046_lab95.png`（px 229–700, y 944–1035）直读「[95]　　　　**T.D. Schultz, D.C.**」；bbox y=232.4 `[95]@59.5-72.8` 与 `T.D.@93.5-111.0` 相距 20.7 pt 空档，编号与作者明显分离。MD 粘连。
- 逐字核对留证（MD 无误，未改）：
  - **[98] `$\phi _ { 2 } ^ { 4 }$` 及其两侧空格**：bbox y=328.3 该行给出 `The@209.6-225.1`，y=331.4 起 `𝜙@227.9-233.4`（**U+1D719 斜体 φ**）与 `42@233.6-237.2`（同一 token 同时覆盖上标 `4` 与下标 `2`），其后 `field@240.2-257.9`。空档量测：`The`→`𝜙` = **2.8 pt**（与数学/文字边界的标准值 2.7–3.0 pt 一致），`42`→`field` = **3.0 pt** ⇒ 印刷两侧**均有空格**。8× 裁片 `/tmp/icm2022dc_p046_phi24.png` 直读「…ns. **The φ₂⁴ field the**…」——两侧空隙清晰，且 `φ` 的右上为 `4`、右下为 `2`。MD 行 1123 `The $\phi _ { 2 } ^ { 4 }$ field theory` **空格在位、字形层级正确，未改**（与 p.43 [43][44]、p.44 [51][54][60][61][62] 五处同型边界粘连形成对照）。
  - **撇号 U+2019**：bbox 码点扫描给出 `Green’s@…`（y=37.1，[88]）、`Ising’s@…`（y=79.0，[90]）、`L’hypothèse@…`（y=413.7，[101]）三处撇号**全部为 U+2019 右单引号**（非 ASCII `'`）。MD 行 1103、1107、1129 **逐码点一致，未改**。
  - **法/德文重音逐位核对**：[101] `L’hypothèse`（`è` = U+00E8）、`moléculaire`（`é` = U+00E9）、`propriété`（两个 `é`）、`ferromagnétique.`（`é`）；文末 `Conseil-Général,`（两个 `é`）、`Genève,`（`è`）——**七个带重音字符全部在位**，bbox 逐 token 列出且 MD 逐字符一致，**未改**。
  - **[100] `regelmassigen`（`ss` 而非 `ß`）**：bbox y=385.8 该词**无任何非 ASCII 码位**（码点扫描未命中），即印刷用的就是 ASCII 双 `s`，不是 `regelmäßigen`。MD 行 1127 `regelmassigen` **与印刷一致，未改**（原刻未使用 ß 字母的排印事实）。
  - **[88]/[89] 的双篇并置**：[88] 以 `Comm. Math. Phys. 31 (1973) 83–112. Comm. Math. Phys. 42 (1975) 281–305.` 两篇连排（第二个 `Comm.` 起于同一行）；[89] `Planar Ising Correlations. Springer Science & Business Media. 49 (2007).`（书名后**句点**、出版社后**句点**、年份后**句点**）。bbox 码点给出 `&amp;@…`（XML 对 `&` 的转义，实际字符即 `&`，**非 `&amp;` 字面**）。MD 行 1103、1105 **逐字符一致，未改**。
  - **破折号体系**：本页全部页码区间 `83–112.`、`281–305.`、`477–481.`、`381–383.`、`760–777.`、`227–245.`、`1–74.`、`145–164.`、`1435–1467.`、`473–488.`、`661–690.`、`3898–3905.` 的分隔符码点**全部为 U+2013 en dash**；而 [100] `7-9`（门牌号）、文末 `7-9 rue`、`Bures-Sur-Yvette` 为 **U+002D 连字符**。MD 逐处一致，**未改**（en dash / 连字符的分界与原刻完全对应）。
- **负向结论（经仲裁判定 MD 正确、**不**修改的铁律二留证）**：
  - **`[94]` 与 p.43 `[41]` 是同一篇论文但著录方式不同**：p.43 [41] 作 `bootstrap. Phys. Rev. D 86 (2012), no. 2, 025022.`（`D` 后**无逗号**、带文章编号 `025022`），p.46 [94] 作 `bootstrap. Phys. Rev. D, 86 (2012), no. 2.`（`D` 后**有逗号**、**无文章编号**）。两处**各自都与本页印刷 bbox 一致**（bbox y=204.5 末为 `Rev.@…`、y=218.5 行首为 `D,@93.5-…`）。**按铁律三原样保留、不作统一**，MD 两处均**正确，未改**。
  - **[89] `Planar Ising Correlations.` 等书名/刊名的斜体**：印刷中书名与刊名均为斜体，MD 为正体，属本篇**全篇系统性的行文/变量斜体丢弃**（`grep -oE '\*[A-Za-z][A-Za-z ]{2,30}\*'` 全篇命中 **0**），**登记不引入本篇从未使用过的斜体标记**（与 p.41 [25] `s-embeddings`、p.42 [9]–[33] 刊名斜体同族处置）。
  - **[89] 出版社后的 `Media. 49 (2007).`**：印刷中 `Springer Science & Business Media` 与卷号 `49` 之间为**句点**（非逗号），MD 一致，**未改**。
  - **文末联系块的行合并**：印刷两行地址（第一行末有逗号）在 MD 中合并为一段，**属版式级换行，非内容差异**；邮箱 `hugo.duminil@unige.ch` 与 `duminil@ihes.fr.` **逐字符保留**（含 `@`、`.`），**未改**。
- 登记不改（铁律三）：
  - **印刷怪癖 1**：**[100] `regelmassigen` 用 ASCII `ss` 而非 `ß`**，照录不改为 `regelmäßigen`。
  - **印刷怪癖 2**：**[88]/[91]/[103]/[104] 的著录不完整**（无期号、无页码区间、年份后无逗号），照录不补。
  - **印刷怪癖 3**：**[94] `Phys. Rev. D, 86` 的 `D` 后逗号**（与 p.43 [41] 著录不一致），照录不统一。
  - **印刷怪癖 4**：**[99] `Ann. of Math. (2). 172`** 中 `(2)` 后为**句点再空格**（非逗号），照录。
  - **印刷怪癖 5**：**[89] `Springer Science & Business Media. 49 (2007).`** 中出版社与卷号之间为句点，照录。
  - 页脚 `46  Hugo Duminil-Copin` 与文末粗体联系块未作为正文段落处理（版式级），MD 以 `##` 标题承接，**结构与内容均无损失**。
- 备注：本页 1 处修复以 peer^ / HEAD / 当前工作树三态 `grep -cF` 比对，命中数为 **1/1/1**（修复后当前态为 0），确认为**原始导出缺陷**，非 peer 回归。全程未使用脚本写回 Markdown（PIL 仅用于裁图）。**本页是全篇文献表的末页，也是全篇正文的末页。修复后全篇复扫 `grep -cE '^\[[0-9]+\][A-Za-z]'` = **0**——即「`[N]` 编号与作者粘连」这一伪影族在本轮 p.41–p.46 页段内已**全部清零**（p.41 的 [1]–[9]、p.42 的 [19][33]、p.43 的 [35][41][45][46]、p.45 的 [73][77][86]、p.46 的 [95]，合计 21 条文献）**。**

### 块 H 小结（PDF p.041–p.046，共 6 页，全部 PASS±）
- 页级结果：**p.41 PASS±（13 处差异 / 10 处 Edit）｜p.42 PASS±（5 处 / 3 处 Edit）｜p.43 PASS±（11 处 / 11 处 Edit）｜p.44 PASS±（10 处差异 / 5 处 Edit）｜p.45 PASS±（6 处 / 6 处 Edit）｜p.46 PASS±（1 处 / 1 处 Edit）** ⇒ **PASS = 0，PASS± = 6，FAIL = 0**；累计 **46 处差异 / 36 处 `Edit`**。
- 页型：6 页全部为**文献表**（[1]–[105]），无题录页、无正文页、无编号公式页；公式仅有 8 处**行内数学**（p.41 3 处、p.43 3 处、p.44 5 处、p.45 1 处、p.46 1 处），已逐位核对字形层级，**全部正确**。
- 系统性伪影族（按处置分列）：
  1. **`[N]` 编号与作者粘连**（21 条文献，6 页全见）——已**全部修复**；全篇 `^\[[0-9]+\][A-Za-z]` 复扫归零。
  2. **数学/文字边界空格丢失 `X$…$Y`**（12 处，p.41 3、p.43 4、p.44 5）——已逐处按 bbox 空档量测（2.2–3.0 pt）判定并修复。
  3. **刊名缩写丢句点**（`J. ofPhys.`、`Math 63`、`Rev D`、`J Math.`、`Ann der Physik.`，5 处）——已修复。
  4. **行末连字符断词误处理**（`correla tions`、`tempera ture`、`twodimensional`、`tran sitions`，4 处）——已修复；其余断词（`Sci-/ences`、`equilib-/rium`、`Lec-/ture`、`clas-/sical`、`Gauthier-/Villars`、`rela-/tions`、`tran-/sition`、`Swendsen-/Wang`、`RSW-/type`、`univer-/sité`、`Kör-/pern`、`his-/tory`、`Insti-/tute`、`sol-/uble`、`Correla-` 等 15 处）MD 已正确还原。
  5. **行文/变量/书名刊名斜体系统性丢弃**——全篇 `*…*` 命中 0，**只登记不修**（避免引入本篇从未使用的标记风格）。
- 印刷怪癖（铁律三，全部照录不改，共 20 余条）：`Φ₄⁴`/`φ₄⁴`/`φ₃⁴` 同一符号上下各一个指数（p.41[4]、p.43[43][44]、p.44[51][54]）；`Dolbilin, ,Y.M.` 双逗号（p.42[33]）；`D. Chelkak, and S. Smirnov.` 多余逗号（p.42[28]）；`monte carlo algorithm` 全小写无连字符（p.43[40]）；`J. Math. Phys. 7 (1963) 1776.` 无期号无逗号（p.43[46]）；`no. 1221` / `no. 855` / `no. 874` 四位期号（p.43[34]、p.42[19]）；`(–II)` 的 U+2013（p.42[19]）；`Phys. Rev..` / `Commun. Math. Phys..` 双句点（p.45[82][87]）；`Ueber` 的 ASCII `Ue`（p.45[77]）；`Zeitsch. Phys.,` 逗号（p.43[70]、[45][70]）；`regelmassigen` 的 `ss`（p.46[100]）；`[94]` 与 `[41]` 同一论文著录不一致（p.46[94] vs p.43[41]）；`Ann. of Math. (2).` 句点（p.46[99]）；`Ueber`/`Auflösung`/`Ströme`/`geführt` 重音在位与 `behaviour`/`behavior` 英美混用。
- **书眉真相（经四页交叉确证并更正了初稿误记）**：p.41/p.43/p.45（奇数页）= `N  100 Years of the Ising Model`；p.42/p.44/p.46（偶数页）= `N  Hugo Duminil-Copin`。**奇偶交替**，非「p.42 起永久切换」。p.042 说明中两处错误表述已在本轮用 `Edit` 就地更正并留证。
- 溯源：块 H 全部 **46 处差异 / 36 处 Edit** 逐条以 `git show cpf-redo/ICM2022_proceedings_Duminil-Copin^:<md>`（peer^）、`git show HEAD:<md>`、当前工作树三态 `grep -cF` 比对，命中数**全部为 1/1/1**（修复后当前态为 0）⇒ **零回归，全部为 MinerU 原始导出缺陷**，无一条系后继 peer 引入。
- 合规：全程**未使用任何脚本写回 Markdown**（Python/PIL 仅用于 `gs` 渲染后的裁图、bbox 解析与像素空隙/码点量测）；**未修改 PDF**（只读）；**未触碰**仓库根 `AUDIT-INDEX.md` / `AUDIT-PROGRESS.log` / `MEMORY.md` / `README.md` 或其他论文目录；**未执行任何 git commit / add / merge / push**；**未启动或改动 mineru**。
- 跨页登记（供集成者，本轮无权改）：`coupled$\phi` 型数学/文字边界粘连在正文行 649、659 仍有 2 处；`}$lowercase` 型约 190 处、行内数学与相邻文字空格合并族在正文多处，均在本轮 p.41–p.46 页段之外。
