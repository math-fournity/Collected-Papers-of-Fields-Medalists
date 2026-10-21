# Page-by-page audit — Lindenstrauss_2006_littlewood_exceptions

- Source PDF: `Lindenstrauss_2006_littlewood_exceptions.pdf` (48 PDF pages; born-digital text layer; printed pages 513–560)
- MinerU Markdown: `Lindenstrauss_2006_littlewood_exceptions_mineru/Lindenstrauss_2006_littlewood_exceptions__Lindenstrauss_2006_littlewood_exceptions.md`
- Base: `037602429d3b009f6fc468c732073eb3ddf9875f` (`main` at task start; this Peer worktree is detached)
- Actor: `Peer-P15`; model: `gpt-6-luna`; reasoning effort: `max`
- Status: `CANDIDATE_NOT_CURRENT` until Master-Luna integrates the exact candidate commit.

## Page entries

### p.001 (PDF p.1 / printed p.513)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p001.png` (pngmono, 150 dpi)
- Compared: journal citation, title, author line, arXiv line, abstract, support footnote, section heading and page-ending paragraph against the PDF text layer; visually inspected the complete title page.
- Print evidence: the abstract says “Hausdorff dimension zero” (PDF p.1, printed p.513; PDF text layer and PNG agree).
- Result: **FAIL** — MinerU has “Hausdorf dimension zero” in the abstract (Markdown line 7), dropping the second `f` in “Hausdorff”.
- Repair/recheck: with Edit, changed the abstract spelling to `Hausdorff`; reread PDF p.1/printed p.513 in the stored PNG and confirmed the final Markdown now matches. This was the one audited FAIL on p.1.

### p.002 (PDF p.2 / printed p.514)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p002.png` (pngmono, 150 dpi)
- Compared: continuation of §1.1 and §1.2 through the start of Furstenberg's semigroup example, including Conjecture 1.1, against the complete PDF text layer for this page.
- Print evidence: PDF p.2 text layer has “different” in “a different homogeneous action”; Markdown line 19 has “a diferent homogeneous action” and Markdown line 21 has “very diferent”. These are spelling-only OCR losses of one `f`; the surrounding statement and the Conjecture 1.1 content/notation align.
- Result: **PASS±** — two non-misleading spelling artifacts; no mathematical statement, name/reference numbering, or paragraph is missing in the page's text-layer comparison. `unipotents groups` appears in both the PDF text extraction and Markdown and is preserved as printed/source text pending any visual dispute.
- Repair: none required under the SOP default for non-misleading typography; no fix applied.

### p.003 (PDF p.3 / printed p.515)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p003.png` (pngmono, 150 dpi; visually inspected as a dense statement/formula sample)
- Compared: continuation of the Furstenberg example; the “intrinsic difference” paragraph; Conjecture 1.2 and equation (1.1); Theorem 1.3; Corollary 1.4; and the transition to the next result.
- Print evidence: the PDF text layer and 150 dpi PNG show “difference”; Markdown line 27 has “diference”, dropping one `f`. Equation (1.1), its nearest-integer definition, Theorem 1.3 hypotheses/conclusion, and Corollary 1.4 agree in their mathematical content.
- Result: **PASS±** — one spelling-only OCR artifact; no theorem, condition, equation, or paragraph loss found in the checked page content.
- Repair: none required under the SOP default for non-misleading typography; no fix applied.

### p.004 (PDF p.4 / printed p.516)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p004.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p004_theorem-1-6.png` (300 dpi crop)
- Compared: Theorem 1.5 and its set definition, the Cassels–Swinnerton-Dyer and Pollington–Velani discussion, the linear-forms definition, Theorem 1.6 and equation (1.3), against the PDF text layer; visually checked the page and used the 300 dpi crop to resolve the trailing-mark ambiguity after the quantified `m` clause.
- Print evidence: in Theorem 1.6, the PDF reads “so that for every m ∈ SL(k, R) minus Ξₖ,” and proceeds to display (1.3); the 300 dpi crop confirms there is no trailing footnote marker or numeral after the comma. Markdown line 75 has an extra bare `2` immediately after the closing math delimiter for `Xi_k` in that theorem clause.
- Result: **FAIL** — the unexplained `2` is extra text attached to Theorem 1.6's quantified clause and is absent from print. The displayed equation (1.3), theorem set, and supporting prose otherwise agree mathematically. Repeated `Hausdorf` spellings (one missing `f`), `efective`, and `tranversals` are logged as non-misleading spelling artifacts.
- Repair/recheck: with Edit, removed the stray `2` after `Ξ_k` in Theorem 1.6 and reread the theorem clause against the 300 dpi crop; also corrected the six `Hausdorf` spellings on this page to `Hausdorff` and confirmed them against the full-page PNG. Other source/spelling quirks noted above remain unchanged.

### p.005 (PDF p.5 / printed p.517)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p005.png` (pngmono, 150 dpi; visually inspected for the matrix display and source-level spelling quirks)
- Compared: Conjecture 1.7, the definitions of `U₁` and `U₂`, the lattice/intersection hypotheses, the Hilbert modular lattice conclusion and its footnote, Hee Oh's consequence, and §1.3's opening paragraphs.
- Print evidence: the 150 dpi source image itself prints “up to conjunction” and later “tranversals”; Markdown line 99 preserves “conjunction”, and line 101 preserves “tranversals”. These are print-level wording/spelling quirks and have not been silently corrected. The matrix forms, `n ≥ 2`, both subgroup intersections, and footnote 1 agree.
- Result: **PASS±** — no mathematical or structural mismatch found. The repeated MinerU spelling `Hausdorf` for printed “Hausdorff” in the dimensional claim is non-misleading typography.
- Repair/recheck: as a supplemental retrieval/search correction, with Edit changed the two `Hausdorf` spellings on this page to `Hausdorff`; checked both against the full-page source PNG. The printed “up to conjunction” and “tranversals” remain unchanged.

### p.006 (PDF p.6 / printed p.518)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p006.png` (pngmono, 150 dpi)
- Compared: the remainder of §1.3 on the two measure-rigidity approaches, the quantum unique ergodicity example, and the transition toward Part I against the PDF text layer.
- Print evidence: the PDF text layer reads “difficulty”, “A different approach”, and “Hausdorff dimension at most 1”; Markdown lines 115, 119, and 117 respectively have `dificulty`, `diferent`, and `Hausdorf`. The surrounding claims and references [3], [4], [20], [17], and [9] align.
- Result: **PASS±** — spelling-only artifacts; no paragraph or mathematical claim was found missing or changed in the text-layer comparison.
- Repair/recheck: as a supplemental retrieval/search correction, with Edit changed the one `Hausdorf` spelling on this page to `Hausdorff`; checked it against the full-page source PNG. Other spelling artifacts remain outside the repair scope.

### p.007 (PDF p.7 / printed p.519)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p007.png` (pngmono, 150 dpi)
- Compared: the end of the special-case `SL(2,R) × SL(2,R)` example; the complementarity of the two methods; the Ratner H-property discussion; acknowledgments; the “Part I. Measure rigidity” heading; and the opening framework paragraph through “implicitly”.
- Print evidence: PDF p.7 text layer and Markdown lines 119–137 have the same argument sequence and named references ([20], [3], [19], [26], [28], [39], [38]); the page ends after “We shall implicitly”, matching the Markdown continuation into the next page.
- Result: **PASS** — no content, mathematical notation, citation, heading, or boundary mismatch found in the complete text-layer comparison for this page.
- Repair: none.

### p.008 (PDF p.8 / printed p.520)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p008.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p008_measure-definitions.png` (300 dpi crop)
- Compared: the definition of `Σ` and the `A` action; unipotent, normalizer, and centralizer definitions; invariant foliations; Radon measure topology and proportionality; ball notation; induced metrics; and the heading/opening of §2.1.
- Print evidence: the 300 dpi crop shows the integral `ρ ↦ ∫_Y f(y)dρ(y)` and the applied-ball notation `B^H_ε(x) = B^H_ε · x`. Markdown line 155 instead has extra dot accents, `B^{\dot{H}}_ε(x) = \dot{B}^H_ε · x`; those accents are absent from print. The remainder of the displayed definitions and section boundary align.
- Result: **FAIL** — MinerU introduces dot accents on both `H` and `B` in the action-ball notation, changing the defined symbol. The lost integral glyph in the extracted PDF text was resolved from the stored 300 dpi crop and is present in Markdown.
- Repair/recheck: with Edit removed the two unsupported dot accents, restoring `B^H_ε(x) = B^H_ε · x`; reread the definition against the 300 dpi crop. The integral glyph was already present and remains intact.

### p.009 (PDF p.9 / printed p.521)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p009.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p009_footnote-2.png` (300 dpi footnote crop)
- Compared: the conditional-measure setup and properties (1)–(7), the positive-entropy explanation, and footnote 2; the footnote was checked against the 300 dpi source crop.
- Print evidence: the crop reads “the one taken in [17] and [13]” and “single orbits of U; in this approach”. Markdown line 191 omits `[17]` and `U;` from those locations; separate dangling `docvortex-page-footnote` spans on lines 185, 187, and 189 contain `U;`, `µx,U`, and `[17]` outside their printed footnote context.
- Result: **FAIL** — the explanatory footnote is fragmented: `[17]` and `U;` are displaced into standalone spans, the footnote sentence omits them, and an isolated `µx,U` span duplicates notation already present in the footnote. Properties (1)–(7) otherwise match the page's content and numbering.
- Repair/recheck: with Edit reconstructed footnote 2 in place to include `[17]` and `U;`, and removed the three detached spans (`U;`, `µx,U`, `[17]`). Reread the complete footnote against the 300 dpi crop; wording and citation now match print.

### p.010 (PDF p.10 / printed p.522)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p010.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p010_limsup-claim.png` (300 dpi crop)
- Compared: property (8) and its proof through the definition of `Uᵢⱼ`, the matrix action, and the opening conjugation identity.
- Print evidence: the 300 dpi crop shows the claim's set as `X′ ∩ ⋃_M limsup_{n→∞} α^{-nt}D_M`. Markdown line 203 renders the limit index as `n ∈ ∞`, omitting the printed arrow; the prose explanation below still says “for infinitely many n”. The following displayed conjugation identity and equation numbering align. Markdown line 211 also has the spelling artifact `suficiently` for printed “sufficiently”.
- Result: **FAIL** — the first `limsup` index is corrupted from `n → ∞` to `n ∈ ∞`, altering the limiting condition. A separate non-misleading spelling artifact is noted.
- Repair/recheck: with Edit restored `n → ∞` in the first `limsup` set expression; reread the displayed claim and adjacent explanation against the 300 dpi crop.

### p.011 (PDF p.11 / printed p.523)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p011.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p011_properties-9-10.png` (300 dpi crop)
- Compared: the `Uᵢⱼ` foliation notation; property (9) and its proof; the maximal ergodic inequality (10); and the opening of §2.2/Theorem 2.1.
- Print evidence: the 300 dpi crop shows `µ_x^{ij}` with no dot accent in the final sentence of the proof of (9), and (10) ends its parameter clause at `α > 0,` with no following `2`. Markdown line 241 accents `µ_x^{ij}` with a dot; line 245 adds a bare `2` after `α > 0`. The integral inequality, its `C‖f‖₁/α` bound, and the section transition otherwise align.
- Result: **FAIL** — the extraneous dot changes the conditional-measure symbol, and the bare `2` is absent from print. Markdown line 237 also spells “helpfu feature” for printed “helpful feature” (non-misleading spelling artifact).
- Repair/recheck: with Edit removed the dot accent from `µ_x^{ij}` and the bare `2` after `α > 0`; reread the end of the proof of (9) and all of (10) against the 300 dpi crop.

### p.012 (PDF p.12 / printed p.524)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p012.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p012-Hab-generated-group.png` (300 dpi crop)
- Compared: Theorem 2.1's alternatives (1)–(3), Remark (3′) and its explanation, the exceptional-returns discussion, the entropy criterion, and the opening high-entropy case.
- Print evidence: the 300 dpi crop gives `H_ab = ⟨U_ab, U_ba⟩`; Markdown line 259 uses invisible sizing delimiters around `U_ab, U_ba`, omitting the printed angle brackets that denote the subgroup generated by those two groups. The surrounding alternatives and Remark (3′) match.
- Result: **FAIL** — the generator brackets are lost in the definition of `H_ab`, changing its mathematical notation/meaning.
- Repair/recheck: with Edit restored `H_{ab} = ⟨U_{ab}, U_{ba}⟩`; reread Theorem 2.1 alternative (2) and its surrounding definition against the 300 dpi crop.

### p.013 (PDF p.13 / printed p.525)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p013.png` (pngmono, 150 dpi)
- Compared: Theorem 2.2 and its proof overview; the low-entropy case and Theorem 2.3 alternatives; the paragraph relating Theorem 2.3 to Corollary 3.4; and the start of §3.
- Print evidence: the PDF text layer and Markdown lines 271–307 retain the same hypotheses, conclusions, references, and section boundary. The source-level `H_{ab}` reference in these statements traces to the group definition recorded on p.12.
- Result: **PASS** — no page-specific content or numbering mismatch found in the text-layer comparison.
- Repair: none.

### p.014 (PDF p.14 / printed p.526)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p014.png` (pngmono, 150 dpi; visually inspected as a dense-formula sample)
- Compared: the entropy/conditional-measure discussion; Proposition 3.1 clauses (1)–(3) and equation (3.1); Corollary 3.2; equation (3.2); and Lemma 3.3.
- Print evidence: the page image confirms (3.1) is `h_µ(α^t)=Σ_{i,j}s_{ij}(µ)(t_i−t_j)^+`, (3.2) is `h_µ(α^t)=h_µ(α^{-t})`, and Lemma 3.3's non-atomicity/invariance conclusion is intact. Markdown lines 297 and 313 have only the spelling artifacts `difeomorphisms` and `diferent` for printed “diffeomorphisms” and “different”.
- Result: **PASS±** — the stated formulas, hypotheses, conclusion, and reference numbers match; two non-misleading spelling artifacts remain.
- Repair: none required under the SOP default for non-misleading typography.

### p.015 (PDF p.15 / printed p.527)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p015.png` (pngmono, 150 dpi)
- Compared: Figure 1 and its caption; the definitions of `C_ℓ`, `R_ℓ`, `C_ℓ^L`, and `R_ℓ^L`; and equations (3.3)–(3.4) in the proof of Theorem 2.2.
- Print evidence: the page PNG shows the labeled Figure 1 diagram and both entropy displays. The embedded MinerU Figure 1 image (`.../images/page_14_image_0.jpg`) has the same `u_{jk}(s)`, `u_{ij}(r)`, and `u_{ik}(rs)x` labels and path layout. Equations (3.3) and (3.4), set definitions, and indices agree with the PDF text layer.
- Result: **PASS** — no mathematical, diagram-label, reference, or equation-number mismatch found on this page.
- Repair: none.

### p.016 (PDF p.16 / printed p.528)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p016.png` (pngmono, 150 dpi)
- Compared: the end of the Theorem 2.2 argument and equation (3.5); Corollary 3.4; the §4 heading and subgroups `L_(ab)`, `U_(ab)`, `C_(ab)`; the metric convention; Definition 4.1; and Lemma 4.2 through the start of its proof.
- Print evidence: PDF p.16 text layer and Markdown agree on `s_ba(µ) ≥ s_ab(µ) > 0`, the two conditional-measure alternatives, subgroup generator notation, and the exceptional-return definition. The proof begins with the same `a=1, b=2` reduction and notation.
- Result: **PASS** — no page-specific mathematical, numbering, or text mismatch found.
- Repair: none.

### p.017 (PDF p.17 / printed p.529)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p017.png` (pngmono, 150 dpi)
- Compared: the block matrix (4.1), the characterizations of `L` and `C`, the sets `D_ℓ` and `E_{ℓ,s}`, the definition of `f(x)`, and the conjugation/recurrence argument through the null-set construction.
- Print evidence: the PDF text layer gives the same matrix entries, zero conditions, contraction factors, and rational-parameter argument. In Markdown the `g_{2*}` entry in the zero-condition sentence is split between math text and an HTML `<sub>∗</sub>` tag, but both the `2` and `*` components remain present and the condition is recoverable.
- Result: **PASS±** — one mixed math/HTML subscript formatting artifact; no matrix entry, hypothesis, or conclusion was omitted in the text-layer comparison.
- Repair: none required under the SOP default for non-misleading formatting.

### p.018 (PDF p.18 / printed p.530)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p018.png` (pngmono, 150 dpi)
- Compared: Proposition 4.3 conditions (1)–(2); the conditional-measure ergodic decomposition and equation (4.2); the proof of (1) ⇒ (2), including equations (4.3) and the `D_δ` definition.
- Print evidence: the PDF text layer and Markdown contain the same quantifiers, measure bounds, orbit condition, integral decomposition, and equation numbers through the page-ending proof step.
- Result: **PASS** — no mathematical statement, condition, or equation-number mismatch found in the text-layer comparison for this page.
- Repair: none.

### p.019 (PDF p.19 / printed p.531)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p019.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p019-prop4-3-symbols.png` (300 dpi crop)
- Compared: the end of the proof of Proposition 4.3; the `(2) ⇒ (1)` ergodic-component argument; and Lemma 4.4 statements (1)–(2) through the opening of its proof.
- Print evidence: the 300 dpi crop confirms the conditional measure superscript is `𝓔` in `µ_x^𝓔(B_{1/m}(z) ∩ K_ℓ)`, and the distance condition is `d(z,y_1) < δ`. Markdown line 461 uses `ε` instead of `𝓔` and adds an unsupported colon subscript to `δ`; line 475 has the spelling artifact `diferent` for “different”.
- Result: **FAIL** — the conditional-measure superscript and the distance-bound symbol are corrupted in the proof of Proposition 4.3; the separate spelling artifact is non-misleading.
- Repair/recheck: with Edit restored the conditional-measure superscript `𝓔` (including the `µ_x^𝓔`-a.e. qualifier) and removed the unsupported colon subscript from `δ`; reread the proof passage against the 300 dpi crop.

### p.020 (PDF p.20 / printed p.532)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p020.png` (pngmono, 150 dpi)
- Compared: the conclusion of Lemma 4.4(2); the §4.2 sketch; definitions of `A′` and `u(r)`; Poincaré recurrence; equations (4.4) and (4.5); and the H-property setup through the matrix-calculation transition.
- Print evidence: the PDF text layer and Markdown agree on `x′=α^s x=gx`, conditional-measure equalities (4.4)–(4.5), the unipotent-flow comparison, citations [38], [39], [29], and the transition to the matrix calculation.
- Result: **PASS** — no page-specific formula, hypothesis, reference, or paragraph mismatch found.
- Repair: none.

### p.021 (PDF p.21 / printed p.533)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p021.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p021-conditional-measure.png` (300 dpi crop)
- Compared: Figure 2 and caption; matrix identity (4.6); inequalities (4.7)–(4.8); compactness/continuity argument; and the transition to §4.3.
- Print evidence: the PDF page and MinerU Figure 2 image show matching `x`, `x′`, `x(r)`, and `x′(r)` paths. The 300 dpi crop shows plain `µ_z^{12}` in “By continuity of µ_z^{12} on X₁”; Markdown line 541 adds a dot accent to this measure symbol. The matrix entries and bounds otherwise agree. Caption spelling `noticably` is printed; `difer` and `diferent` in the nearby MinerU prose are spelling artifacts.
- Result: **FAIL** — the added dot accent changes `µ_z^{12}` to a different notation. The caption/source typo is retained, and the OCR spellings are non-misleading.
- Repair/recheck: with Edit removed the dot accent from `µ_z^{12}`; reread the continuity sentence against the 300 dpi crop.

### p.022 (PDF p.22 / printed p.534)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p022.png` (pngmono, 150 dpi)
- Compared: the null-set assumptions; constructions of `X₁`, `X₂`, and `X₃`; equations (4.9)–(4.11); and the opening of §4.4.
- Print evidence: the PDF text layer and Markdown agree on the measures of the compact sets (`1−ε⁴`, `1−C₁ε²`, and `1−C₂ε`), the interval bound in (4.10), both time-average inequalities in (4.11), and the page-ending transition to `z,z′ ∈ X₃`.
- Result: **PASS** — no mathematical, inequality, variable, or equation-number mismatch found in the text-layer comparison.
- Repair: none.

### p.023 (PDF p.23 / printed p.535)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p023.png` (pngmono, 150 dpi)
- Compared: equation (4.12); the choice of `r` and the cancellation discussion; the Figure 3 diagram/caption; the setup using Lemma 4.6; and estimate (4.13) with `S=e^{θ−ητ}`.
- Print evidence: the PDF text layer and page PNG match all four terms in `κ(z,z′)`, the exponent `1/2`, the `4T`–`6T` interval, the `1−9ε` density, equation (4.13), and Figure 3's path labels. The embedded MinerU Figure 3 image (`.../images/page_22_image_5.jpg`) matches the printed diagram. Markdown line 583 has the non-misleading spelling `diference` for printed “difference”.
- Result: **PASS±** — mathematical conditions, exponents, equation number, and diagram agree; one spelling artifact remains.
- Repair: none required under the SOP default for non-misleading typography.

### p.024 (PDF p.24 / printed p.536)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p024.png` (pngmono, 150 dpi)
- Compared: the Figure 4 diagram/caption; the proof of Lemma 4.5 using `Q₁`, `Q₂`, and `Q₃`; equation (4.13); and the setup of Lemma 4.6.
- Print evidence: the PDF text layer matches the definitions of `Q₁`–`Q₃`, the half-scaling formula for `v`, the `1−9ε` density, the ratio transformation by `e^{2w}`, and `S=e^{θ−ητ}`. The embedded MinerU Figure 4 image (`.../images/page_23_image_0.jpg`) matches the printed figure labels/layout.
- Result: **PASS** — no mathematical, inequality, figure-label, or equation-number mismatch found on this page.
- Repair: none.

### p.025 (PDF p.25 / printed p.537)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p025.png` (pngmono, 150 dpi; visually inspected for the matrix/equation displays)
- Compared: Lemma 4.6 statement; equations (4.14)–(4.16), including the conjugated matrix; and the definitions of `P_a` and `P_u` through the end of the page.
- Print evidence: the source page confirms both inequalities in (4.14), the `δ^{3/8}` and `κ^{3/4}` exponents, the matrix factors `e^{-2τ}`, `e^{-τ}`, `e^{2τ}`, and `e^{τ}`, and the bounds for `P_a`/`P_u`; these agree with the Markdown. The display spells the conjunction as letter-spaced `a n d` in MinerU.
- Result: **PASS±** — mathematical statements and matrix entries agree; `a n d` is a non-misleading spacing/OCR artifact.
- Repair: none required under the SOP default for non-misleading typography.

### p.026 (PDF p.26 / printed p.538)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p026.png` (pngmono, 150 dpi)
- Compared: completion of Lemma 4.6, the `P_a`, `P_u`, `P′_a`, `P′_u` density argument; the §4.5 construction of `x(r), x′(r)`; and the matrix identity and bounds (4.17)–(4.18).
- Print evidence: the PDF text layer and page PNG agree on the `1−36ε` density bound, `R=κ(x,x′)^{-1}`, the paired conditional-measure equality, every entry in `g̃(r)`, and the bounds in (4.17)–(4.18).
- Result: **PASS** — no mathematical condition, matrix entry, exponent, or equation-number mismatch found in the page comparison.
- Repair: none.

### p.027 (PDF p.27 / printed p.539)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p027.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p027-annulus-print.png` (300 dpi crop)
- Compared: the proof of (4.17)–(4.18), estimates (4.19)–(4.22), the interval choice for `r`, and the concluding compactness argument.
- Print evidence: the 300 dpi crop shows the printed interval as `[ρ^{-5}R, ρ^{-5}R] \ [ρ^{-4}R, ρ^{-4}R]`, with both endpoints repeated and no minus signs before the first endpoints. Markdown has the same endpoints. The remaining bounds and powers (`ρ^{-6}`, `ρ^{-5}`, `ρ^{-4}`) match.
- Result: **PASS±** — Markdown is faithful to the print. The repeated endpoints make singleton intervals; whether the source intended a different interval is unknown, so this is recorded as a print-level source quirk and left unchanged.
- Repair: none; print remains authoritative.

### p.028 (PDF p.28 / printed p.540)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p028.png` (pngmono, 150 dpi)
- Compared: the end of the proof of Theorem 1.3 for the low-entropy case; the §5 introduction; Theorem 5.1 and its three conditions; Proposition 5.2; its proof; and the statement of Lemma 5.3.
- Print evidence: the PDF text layer and Markdown agree on the three eigenvalue conditions, the contradiction using the characteristic polynomial, and Lemma 5.3's separation hypothesis and conclusion. Markdown line 793 has `coeficients` for printed “coefficients”; the word spacing in the following Lemma 5.3 statement is also an OCR artifact.
- Result: **PASS±** — the conditions and mathematical argument match; only non-misleading spelling/word-spacing artifacts remain.
- Repair: none required under the SOP default for non-misleading typography.

### p.029 (PDF p.29 / printed p.541)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p029.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p029-eigenvalue-exponents.png` (300 dpi crop)
- Compared: the opening of Lemma 5.3's proof, the diagonal matrix definition of `f`, the cone estimates, and the eigenvalue bounds through equation (5.1).
- Print evidence: the 300 dpi crop confirms that this page prints `f = diag(e_1^λ, e_2^λ, …, e_m^λ)`. The preceding page's Lemma 5.3 statement prints `diag(e^{λ_1}, e^{λ_2}, …, e^{λ_m})`; the source notation is internally inconsistent across the statement/proof. Markdown preserves the p.29 form; no OCR correction is made. The cones and bounds match the page.
- Result: **PASS±** — text fidelity holds, with a source-level eigenvalue-notation quirk spanning the Lemma 5.3 statement and proof; author intent is not inferred.
- Repair: none; both printed forms remain authoritative for their respective pages.

### p.030 (PDF p.30 / printed p.542)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p030.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p030-ordering-source.png` (300 dpi crop)
- Compared: the conclusion of Lemma 5.3; the block definition of `U₁`; recurrence and intersection construction in the proof of Theorem 5.1; condition (5.2); and the eigenvalue estimate for the lower-right block.
- Print evidence: the crop confirms the source itself prints `λ_i > λ_{i−1}+1` after the preceding assumption `λ₁ > λ₂ > … > λ_m`; Markdown line 855 matches this printed direction. This is an internal source-level inequality-direction inconsistency; author intent is unknown. The block entries, (5.2), and `3/4` estimate otherwise match.
- Result: **PASS±** — MinerU is faithful to the printed inequality and formulas; the source-level ordering inconsistency is recorded without correction.
- Repair: none; print remains authoritative.

### p.031 (PDF p.31 / printed p.543)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p031.png` (pngmono, 150 dpi), plus `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p031-Hab-generated-group.png`, `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p031-footnote-3.png`, and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p031-class-A-wording.png` (300 dpi crops)
- Compared: the two alternatives after Proposition 5.2; the equivalence relation and product decomposition of `H`; the Ratner/Margulis–Tomanov discussion; the class-A definition; Theorem 6.1; and footnote 3.
- Print evidence: the first crop confirms `H_ab = ⟨U_ab, U_ba⟩`; Markdown line 897 uses invisible sizing delimiters, omitting the generated-subgroup brackets. The footnote crop reads “Γ can be any closed subgroup of G,”; Markdown line 907 omits this `G`, while a detached `G,` span appears on line 905. The 300 dpi wording crop confirms the source itself says “g ∈ G in an element of class A”; that source wording is retained as printed.
- Result: **FAIL** — Theorem 6's referenced generated-group notation loses its angle brackets, and footnote 3's `G,` is displaced from the sentence into a standalone span. These are separate from the source-level grammar quirk.
- Repair/recheck: with Edit restored `H_{ab} = ⟨U_{ab}, U_{ba}⟩`, moved `G,` into footnote 3's “closed subgroup of G” sentence, and removed the detached `G,` span. Reread both locations against their 300 dpi crops; the print-level “g ∈ G in an element of class A” wording is unchanged.

### p.032 (PDF p.32 / printed p.544)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p032.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p032-block-matrix.png` (300 dpi crop)
- Compared: the `S N_G(L)` condition; Lemma 6.2 and its block matrix `h₀`; equation (6.1) and the rational subspace argument; the one-parameter scaling; and the continuation of the proof of Theorem 1.3.
- Print evidence: the 300 dpi crop shows `h₀ = [[h′₀, 0], [0, I_{k−k′}]]`. Markdown line 921 instead has a column-vector command followed by `I_{k−k′}` and a stray integral glyph, without the printed 2×2 block structure. The page also prints “conjunction by g” (Markdown line 911 preserves this source wording) and uses `R^n`/`Z^n` for `V_g` and `m` despite the surrounding ambient `R^k` lattice statement; those are recorded as source-level quirks, not silently repaired.
- Result: **FAIL** — the block matrix defining `h₀` is structurally lost in MinerU Markdown. The other displayed group/subspace formulas and the closing flow argument match the source at text-layer level.
- Repair/recheck: with Edit reconstructed `h₀ = [[h′₀, 0], [0, I_{k−k′}]]`; reread the matrix, equation (6.1), and adjacent argument against the 300 dpi crop. The printed “conjunction by g” and `R^n`/`Z^n` forms remain unchanged.

### p.033 (PDF p.33 / printed p.545)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p033.png` (pngmono, 150 dpi)
- Compared: the conclusion of the proof of Theorem 1.3; the proof of Corollary 1.4, including the reductive-group and congruence-class description; and the transition to Part 2/§7.
- Print evidence: the page image and PDF text layer match the subgroup, torus, congruence, and compact-orbit statements. The print itself says “This show” and “(i.e., since A ≅ R^{k−1}, compact)” in the Corollary 1.4 proof; Markdown preserves these source-level wording quirks.
- Result: **PASS±** — mathematical statements and transition match; the two awkward phrases are in the printed source, not MinerU substitutions.
- Repair: none; print remains authoritative.

### p.034 (PDF p.34 / printed p.546)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p034.png` (pngmono, 150 dpi)
- Compared: §7.1 definitions of Hausdorff and box dimension; equations (7.1)–(7.4); the product metric bound; and the definition of topological entropy (7.5).
- Print evidence: the PDF text layer and Markdown preserve the covering infimum/sum, separated-set condition, limsup in (7.2), countable-union formula (7.3), dimension inequality (7.4), and both expressions in (7.5). Several spellings lose an `f` in MinerU (`Hausdorf`, `diferent`, `suficient`), without changing these definitions.
- Result: **PASS±** — formulas, inequalities, and equation numbers match; spelling-only OCR artifacts remain.
- Repair/recheck: as a supplemental retrieval/search correction, with Edit changed all four `Hausdorf` spellings on this page to `Hausdorff`; checked them against the full-page source PNG. The separate `diferent` and `suficient` artifacts remain unchanged.

### p.035 (PDF p.35 / printed p.547)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p035.png` (pngmono, 150 dpi)
- Compared: finite-partition entropy; metric entropy definition and (7.6); entropy bounded by topological entropy and the variational principle (7.7); the §8 transition; and Lemma 8.1's metric equivalence.
- Print evidence: the PDF text layer and Markdown agree on the partition refinement, the join over `i=0,…,N−1`, both limits/suprema, and the two-sided `c₀` distance bound in Lemma 8.1.
- Result: **PASS** — no content, exponent, quantifier, or equation-number mismatch found in the page comparison.
- Repair: none.

### p.036 (PDF p.36 / printed p.548)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p036.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p036-identity-metric.png` (300 dpi crop)
- Compared: local-coordinate metric discussion; definitions of `U`, `V`, and `C`; decomposition and (8.1); Lemma 8.2; and its expansion estimate proof.
- Print evidence: the 300 dpi crop shows the identity symbol as plain `I_k` in `d(a^n f a^{-n}, I_k)`; Markdown line 1087 adds a dot over `I_k`. The full-page image also shows the prose “conjugation with a”; Markdown line 1081 instead renders a detached superscript-like `a,` after “conjugation with”. The expanding-norm inequality and Lemma 8.2 conclusion otherwise match.
- Result: **FAIL** — two print-absent marks distort the identity symbol and the action parameter in this proof.
- Repair/recheck: with Edit removed the dot over `I_k` and restored “conjugation with a”; reread the expansion estimate and the adjacent prose against the 300 dpi crop and full-page PNG.

### p.037 (PDF p.37 / printed p.549)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p037.png` (pngmono, 150 dpi)
- Compared: Proposition 8.3 alternatives and proof; the set `P_y` and entropy estimate; Lemma 8.4 statement; and the transition into its proof.
- Print evidence: PDF p.37 and Markdown agree on (8.2), the separated-set cardinality/exponents, `Lemma 8.4`'s quantifiers and distance bound, and the printed conclusion `h_top(α^t) ≥ b log λ > 0`. The source also uses `g x, h x` after defining `F_N ⊂ P_y` and phrases the conclusion as “> 0 is positive”; these are retained as printed wording. Markdown line 1111 has `diferent` for “different”.
- Result: **PASS±** — no MinerU-specific mathematical alteration found; one spelling artifact and source-level wording quirks are recorded.
- Repair: none; preserve the printed wording.

### p.038 (PDF p.38 / printed p.550)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p038.png` (pngmono, 150 dpi), `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p038-conjugation-bounds.png`, and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p038-entropy-variable.png` (300 dpi crops)
- Compared: the proof of Lemma 8.4 and estimate (8.3); the application in Lemma 8.5; and the entropy bound at the page end.
- Print evidence: the conjugation crop shows the radius as `B^G_{c₁^{-1}r}` and the second expansion as `a^{-1}fa`. Markdown line 1125 adds a prime to `c₁^{-1}`, a dot to `G`, and a dot to the final `a`. The lower crop confirms the source prints `½ d log λ`; it also prints `g,h ∈ H` in the Lemma 8.5 proof and uses `c₂` there after Lemma 8.4 stated `c₃`.
- Result: **FAIL** — the extra prime/dots alter the radius and conjugation symbols. The `d`/`b`, `H`, and `c₂`/`c₃` inconsistencies are present in print and remain source-level issues, not OCR corrections.
- Repair/recheck: with Edit restored the radius `B^G_{c₁^{-1}r}` and the conjugate `a^{-1}fa`; reread both conjugation bounds against the 300 dpi crops. The source-level `d`/`b`, `H`, and `c₂`/`c₃` forms remain unchanged.

### p.039 (PDF p.39 / printed p.551)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p039.png` (pngmono, 150 dpi)
- Compared: §9's upper-semicontinuity claim for metric entropy; the countably generated σ-algebra and atom definition; conditional entropy integral/addition/monotonicity/zero criteria; and the conditional formula for `h_µ(T,Q)`.
- Print evidence: PDF p.39 text layer and Markdown preserve the limsup inequality, weak-* setting, atom formula, all conditional-entropy identities, and the conditional metric-entropy formula with the same quantifiers.
- Result: **PASS** — no claim, set relation, integral, or cited theorem number was lost or changed in this page comparison.
- Repair: none.

### p.040 (PDF p.40 / printed p.552)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p040.png` (pngmono, 150 dpi)
- Compared: relative-entropy equations (9.1)–(9.2); Lemma 9.1; the construction and refinement properties of the finite partitions; and the opening of Proposition 9.2.
- Print evidence: PDF p.40 and Markdown agree on both relative-entropy formulas, the atom and conditional-measure definitions, and the Proposition 9.2 setup. Both print and Markdown give `Q_m = ⋁_{i=1}^m P_m`; this repeated-subscript formula appears inconsistent with the stated refinement construction, but it is the printed form and is left unchanged.
- Result: **PASS±** — MinerU is faithful; a source-level repeated-subscript quirk is recorded without correction.
- Repair: none; print remains authoritative.

### p.041 (PDF p.41 / printed p.553)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p041.png` (pngmono, 150 dpi)
- Compared: the proof that atoms of `𝒜` differ only along `C`; the relative-entropy vanishing argument; the recurrence family `B_{i,j,g_C,ℓ}`; and the concluding same-atom implication `i=j`.
- Print evidence: the PDF text layer and Markdown match the centralizer decomposition, fixed `c₁`/`c₃` bounds, recurrence-set definition, and sequence of implications through the page end.
- Result: **PASS** — no page-specific mathematical, set, inequality, or variable mismatch found in the text-layer comparison.
- Repair: none.

### p.042 (PDF p.42 / printed p.554)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p042.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p042-entropy-infimum.png` (300 dpi crop)
- Compared: Corollary 9.3 and its entropy-neighborhood proof; the infimum formula for `h_ν(a,P)`; and the start of §10, including the lattice shortest-vector function and Mahler criterion.
- Print evidence: the 300 dpi crop shows the infimum formula uses `⋁_{n=0}^{M−1} a^n P`; Markdown line 1281 has a barred `𝖵`-like token instead of the printed join. The page image prints “by Mahler’s criterion”; Markdown line 1293 inserts `Ω^{,}s` between “Mahler” and “criterion”. The surrounding bounds and lattice definitions match.
- Result: **FAIL** — the join operation in the entropy infimum is misrendered, and the Mahler attribution has extra nonprint text.
- Repair/recheck: with Edit restored `⋁_{n=0}^{M−1}` in the entropy infimum and removed the inserted `Ω^{,}s` from “Mahler’s criterion”; reread both locations against the 300 dpi crop and full-page PNG. Also corrected the single `Hausdorf` spelling on this page to `Hausdorff` and checked it against the source image.

### p.043 (PDF p.43 / printed p.555)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p043.png` (pngmono, 150 dpi)
- Compared: the cone definition; Theorem 10.1 and (10.1); the two-case argument using Proposition 8.3; the averaged measures `ν_N`; and the entropy/ergodic-decomposition conclusion.
- Print evidence: the PDF text layer and Markdown agree on the infimum over `Σ′`, the `D_{1/n}` exhaustion, the `N^{k−1}` normalization and `k−1` integrals, the averaged action, and the positive-entropy contradiction to Theorem 1.3. Markdown line 1283 has `Hausdorf` for printed “Hausdorff”.
- Result: **PASS±** — formulas and proof steps match; one non-misleading spelling artifact remains.
- Repair/recheck: as a supplemental retrieval/search correction, with Edit changed the one `Hausdorf` spelling on this page to `Hausdorff`; checked it against the full-page source PNG. Mathematical content and other wording remain unchanged.

### p.044 (PDF p.44 / printed p.556)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p044.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p044-psi-map.png` (300 dpi crop)
- Compared: the transversal box-dimension definition; Theorem 10.2 and bounded-orbit set; the product coordinates and metric; the map `ψ`; the `P′` reduction; and the start of §11.
- Print evidence: the crop reads `ψ: O → SL(k,R)` and `ψ(f_C,f_U,f_V)=f_C f_U f_V`. Markdown line 1345 has `ψ: O SL(k,R)` with the mapping arrow missing. The set `P`, its slice `P′`, and the ensuing entropy/box-dimension alternatives otherwise agree. The printed “Hausdorff” spelling is also reduced to `Hausdorf` in MinerU.
- Result: **FAIL** — the function signature loses the codomain arrow and its typed map relation.
- Repair/recheck: with Edit restored `ψ: O → SL(k,R)`; reread the map definition and adjacent `P`/`P′` definitions against the 300 dpi crop. Also corrected the single `Hausdorf` spelling on this page to `Hausdorff` and checked it against the full-page PNG.

### p.045 (PDF p.45 / printed p.557)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p045.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p045-dirichlet-estimate.png` (300 dpi crop)
- Compared: Proposition 11.1 and equation (11.1); the semigroup `A⁺`; both directions of the bounded-orbit equivalence; the lattice-vector product estimate; Dirichlet's step; and condition (11.2).
- Print evidence: the 300 dpi crop shows `|qn(qnu+qm₁)| < ε², and ...` with no additional numeral after the comma. Markdown line 1399 inserts a bare `2` after the `ε²` math expression and before “and”. The surrounding `ε⁴`, `ε²`, and `ε³` bounds and the choices of `r,s` otherwise agree. The source itself says “By the the properties” (Markdown preserves this).
- Result: **FAIL** — one extra bare `2` is inserted in the Dirichlet estimate; the duplicated “the” is source-level wording.
- Repair/recheck: with Edit removed the stray bare `2` after `ε²`; reread the Dirichlet estimate and its continuation against the 300 dpi crop. The source's duplicated “the” remains unchanged.

### p.046 (PDF p.46 / printed p.558)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNGs: `audit/Lindenstrauss_2006_littlewood_exceptions_p046.png` (pngmono, 150 dpi) and `audit/300dpi/Lindenstrauss_2006_littlewood_exceptions_p046-theorem-1-6-proof.png` (300 dpi crop)
- Compared: the proof of Theorem 1.5; the proof of Theorem 1.6; author affiliations/current address; and references [1]–[10].
- Print evidence: the 300 dpi crop shows `Suppose m ∉ Ξ_k;` with no closing brace after `Ξ_k`. Markdown line 1403 has a stray `}` immediately before the semicolon, leaving the math fragment malformed. The vector bound leading to (1.3) otherwise matches. Reference [10] also has the spelling artifact `difeomorphisms` for printed “diffeomorphisms”.
- Result: **FAIL** — an unmatched closing brace was added to the Theorem 1.6 proof condition. The reference spelling difference is non-misleading.
- Repair/recheck: with Edit removed the unmatched `}` after `Ξ_k`; reread the Theorem 1.6 condition and vector display against the 300 dpi crop. Corrected the two `Hausdorf` spellings on this page to `Hausdorff` and checked them against the full-page PNG. References [4], [7], and [10] were also corrected against the full-page citation image.

### p.047 (PDF p.47 / printed p.559)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p047.png` (pngmono, 150 dpi)
- Compared: bibliography entries [11]–[32], including authors, titles, journal/book data, volume/year, and page ranges.
- Print evidence: the PDF uses repeated-author em-dash markers for [16], [17], [24], [25], and [27], while Markdown lines 1443, 1445, 1459, 1461, and 1465 omit the author ditto marker (and [25] has only a bare em dash without the printed spacing). Entry [16] also has a detached acute accent after `Math.` instead of the printed `Math. 79`; [15] `Diferential` and [19] `difeomorphisms` are spelling artifacts for printed “Differential” and “diffeomorphisms”.
- Result: **FAIL** — five references lose the printed repeated-author marker, and [16]'s journal citation is malformed; the remaining listed metadata and page ranges align. Spelling-only title artifacts are noted separately.
- Repair/recheck: with Edit restored repeated-author em-dash markers in [16], [17], [24], [25], and [27] and corrected [16] to `Inst. Hautes Études Sci. Publ. Math. 79`; reread each entry against the full-page PNG. Also corrected the reference-title spellings `Diferential`→`Differential` in [15] and `difeomorphisms`→`diffeomorphisms` in [19], checked against print.

### p.048 (PDF p.48 / printed p.560)

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`
- Evidence PNG: `audit/Lindenstrauss_2006_littlewood_exceptions_p048.png` (pngmono, 150 dpi)
- Compared: bibliography entries [33]–[49] and the received/revised dates.
- Print evidence: all titles, author names, publication data, volume/year/page ranges, and the two dates match the Markdown. Reference [39] is itself printed with the literal prefix `38,` in place of an author ditto mark; Markdown preserves that source form. The later ditto markers [40]–[43] and [47] are present.
- Result: **PASS±** — bibliography transcription matches; the anomalous [39] prefix is a print-level source quirk and is left unchanged.
- Repair: none; print remains authoritative.

## Final repair and recheck report

- Actor/model/effort: `Peer-P15 | gpt-6-luna/max`.
- Status: `CANDIDATE_NOT_CURRENT`; this worktree remains detached and awaits Master-Luna integration.
- Baseline: `037602429d3b009f6fc468c732073eb3ddf9875f` (`main` at task start). At final review, `refs/heads/main` is `dc234aee28ba87a6dff9bebf14ac2186733c06aa`; that later movement is not included in this candidate.
- Initial page signatures: 12 `PASS`, 18 `PASS±`, 18 `FAIL` (48 total). All 18 initial FAIL findings have now been corrected in the MinerU Markdown and rechecked against the cited page PNGs/crops. The separately logged print-level quirks and unrelated OCR spellings remain as described in their page entries.
- Supplemental spelling/search normalization: corrected the 18 additional exact `Hausdorf` occurrences on PDF pp.004–006, 034, 042–044, and 046 to `Hausdorff`, checking each affected full-page source PNG. Together with p.001's abstract correction, all 19 original `Hausdorf` occurrences in the target Markdown were repaired. No other non-misleading prose spelling was normalized in the body.
- Final Markdown: SHA-256 `aca45d5a32ad8846a41ffa9f5c781715f5827a8a200f52ae3dd39230fff5dd5f`; baseline SHA-256 `ad1dda207268ab0f1637f654cb684269ec80971ec6cca1ab2d48f5833f2129be`.
- Markdown fix commit: `d252350ca9f0c051adfcf5105e4073192d4261dd` (`fix(md): repair Lindenstrauss_2006_littlewood_exceptions transcription [Peer-P15 | gpt-6-luna/max]`). It changes only the target Markdown.
- Full-file reread: all 1,501 lines reread after edits in consecutive ranges 1–250, 251–500, 501–750, 751–1000, 1001–1250, and 1251–1501. Each repair was then compared to the corresponding stored PDF page image or 300 dpi crop; the p.019 conditional-measure superscript was additionally confirmed by the PDF text layer as `𝓔`.
- Read-only checks: `git diff --check` passes; exact `Hausdorf` search in the target Markdown returns no matches. No tests were run. No PDF, root `AUDIT-INDEX.md`, root `AUDIT-PROGRESS.log`, README, or MEMORY changes were made; no merge, push, or publication was performed.
- Page audit commit map (12-character commit IDs, in PDF-page order):
  - p.001–p.008: `b839f50fbb7d`, `507a06f16901`, `bf4eb8dc88d8`, `f2e90ffb67d5`, `5307f47ff66b`, `6202a2344256`, `02fda0644db2`, `12407e68346e`.
  - p.009–p.016: `9d8182eb7ff1`, `63d2a992b7fd`, `fd982e48384b`, `9ec9417940bc`, `4d5456d45434`, `6b8abf00774c`, `af8cbae949c7`, `b076fc9f09ed`.
  - p.017–p.024: `937b46382552`, `0ae3a5125cf2`, `f4ed20368229`, `6c1c9f3a86b4`, `75ff45bf06c0`, `28d33d7bdc16`, `a6bb2fd12ae4`, `3629b3109885`.
  - p.025–p.032: `db0735b069bf`, `a559bb10eed5`, `42357d9aad11`, `e7a0f384609e`, `8a66c1badfa0`, `bcf0e37f3398`, `2dc9861d625c`, `060882a850b3`.
  - p.033–p.040: `bb4094047d40`, `68356420a3bc`, `2d39f38ac6e5`, `b93d482a65b4`, `c6df14f1bf7d`, `71e0504cd28a`, `55a387047f25`, `56714a0f05b4`.
  - p.041–p.048: `097aeb42c11b`, `1cde1c80e546`, `602d67323390`, `2cb11f5563f5`, `24bdd4b198e9`, `3ca0beadab40`, `501be2b2ebbb`, `bb7978c7cb16`.

---

## 本块：linden06 独立复核 p.001–p.008

- Actor：workflow `审计 linden06`（Host zcode；模型/身份我无法自行核实，按 SOP 身份纪律如实登记为 `UNVERIFIED_SELF_REPORT`）。
- 范围：PDF p.1–p.8 / 印刷 p.513–p.520，共 8 页，一页一条说明，逐页渲染并亲眼观看 PNG 后判定。
- 被检 Markdown 基线 SHA-256：`2493dfdcd3ee6789d13eb849828ba59384877229c3315f589cb898c2ee12da42`（1501 行）。
- 与本文件上方 Peer-P15（gpt-6-luna）旧审计、以及 `AUDIT-Lindenstrauss_2006_littlewood_exceptions.redo.md` 中 `Wf-R-P15`（GLM-5.3-Flash）重做的关系：本块为**第三次独立复核**。前两轮结论仅作交叉参考，不代替原页判读；冲突时以本次原页所见为准。
- PNG 存放：按 SOP 一次一页渲染至 `/tmp/linden06_audit_pNNN.png`（pngmono 150dpi）；某字形 150dpi 判读不了时才以 `-r300` 重渲该页并用 PIL 裁切放大（PIL 只裁图，不写 Markdown）。

## p.001（PDF p.1 / 印刷 p.513）
- PNG：/tmp/linden06_audit_p001.png（pngmono 150dpi）
- 核对：题录（页眉刊名卷期页码行、标题、作者行与星号脚注标记）、Abstract 全段、§1 Introduction 标题、§1.1 节标题与三段正文、页脚脚注全文、左侧竖排 arXiv 水印。
- 结果：PASS±（差异列表：①页眉行 `Annals of Mathematics, 164 (2006), 513–560` 未保留——MinerU 全篇系统性丢页眉，非本页独有；②左侧竖排水印 `arXiv:math/0612721v1 [math.DS] 22 Dec 2006` 未保留；③印刷黑体 ℝ 在 MD 行 11 拍平为 `R<sup>k</sup>`，不误导）
- 备注：逐字核对——标题 `Invariant measures and the set of exceptions to Littlewood's conjecture`、作者行 `By Manfred Einsiedler, Anatole Katok, and Elon Lindenstrauss*`、Abstract 四句（含 `Hausdorff dimension zero`）、§1.1 三段（含 `[23]`、`A. Oppenheim in 1929`、`three space`、`deep number theoretical implications`、`M. S. Raghunathan`）与印刷逐项吻合；脚注（DMS-007133 / DMS-0140497 / DMS-0434403 / DMS-0222452、Clay Mathematics Institute Long Term Prize fellow、American Institute of Mathematics、University of Washington）与印刷逐字吻合、无缺字。本页无需 Edit。三处差异都是未保留的非语义载体或字体拍平，不构成数学内容错误，按「有瑕疵但不误导」记 PASS±。印刷页号 513 由本页页眉页码区间并结合 p.2 页眉交叉确认（见 p.002 条目）。

## p.002（PDF p.2 / 印刷 p.514）
- PNG：/tmp/linden06_audit_p002.png（pngmono 150dpi）
- 核对：页眉（514 + 作者行，并据此确认 p.1 = 印刷 513）、§1.1 末段（Ratner 引文 [41]/[42]/[40]/[43]/[28]、parabolic behavior、[8]）、§1.2 节标题与首段（`different`、k × k、split Cartan、[16]）、`k = 2` 段（`different`、`k > 2,`、`ℝ^{k−1}`-action、one–parameter、partially hyperbolic）、Conjecture 1.1 全句、Furstenberg 段（Σ_{m,n} display、`n, m`、`k.x = kx mod 1`）、引用号 [25]/[17]/[6]。
- 结果：PASS±（差异列表：①页眉 `514 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS` 未保留（MinerU 系统性丢页眉）；②印刷粗体 ℝ 拍平为 MD 行 21 `isomorphic to R`、行 25 `on$\mathbb { R } / \mathbb { Z }$`，不误导）
- 备注：**两处印刷怪癖按铁律三原样保留并登记，不改**——①印刷确为 `of general unipotents groups`（多一个 s），MD 行 15 一致；②印刷确为 `Raghunatan's conjecture`（少 h，与 p.1 同段的 `M. S. Raghunathan` 不一致，系印刷自身），MD 行 15 一致。两处均以 150dpi PNG 视觉确认，文本层同证。Conjecture 1.1（Margulis）全句与印刷逐字吻合：`X = SL(k,ℝ)/SL(k,ℤ)`、`k ≥ 3`、`closed, connected group L > A`、`a single, closed L-orbit`；Σ_{m,n} = {m^k n^l}_{k,l≥1} 的上下标与 `k.l` 索引条件正确，`where n, m` 的逗号次序与印刷一致（无重复逗号伪影），`different` 两处为印刷双 f。本页无需 Edit。

## p.003（PDF p.3 / 印刷 p.515）
- PNG：/tmp/linden06_audit_p003.png（pngmono 150dpi）
- 核对：页眉（`THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 515`）、Furstenberg 段收尾、intrinsic difference 段（M. Rees [44]、[3, §9]、`X = SL(k,ℝ)/Γ`、Γ=SL(k,ℤ)、[21]/[25]/[48]）、Conjecture 1.2 (Littlewood (c. 1930)) 全句、式 (1.1)、⟨w⟩ 定义、Theorem 1.3 全句、Corollary 1.4 全句、末段过渡句、引用号 [24, §2]。
- 结果：PASS±（差异列表：①页眉 `THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 515` 未保留（MinerU 系统性丢页眉）；②印刷粗体 ℝ 拍平为 MD 行 31/37/45 的 `$\mathbb { R }$`，不误导；③MD 行 37 `\operatorname* { m i n }` 为 MinerU 对印刷 `min` 的字距展开伪影，渲染仍读作 min，不误导。**已修复 1 处**：MD 行 31 Conjecture 1.2 的 `For every$u , v \in \mathbb { R }$` 缺印刷句末逗号 → 补为 `$\mathbb { R }$,`）
- 备注：**print quirk 忠实保留（不改）**：印刷确为 `come from A invariant homogeneous subspaces`（A 后无连字符），MD 行 27 一致。**式 (1.1) 与 ⟨w⟩ 定义逐项核验**：`liminf`（未被 MinerU 误分为 `lim inf`）、下标 `n → ∞`、`n⟨nu⟩⟨nv⟩ = 0` 的两个因子与 `\tag{1.1}` 编号、⟨w⟩ = min_{n∈ℤ}|w − n| 的下标与绝对值均与印刷一致，数学内容无错。Theorem 1.3（`k ≥ 3`、`one-parameter subgroup of A`、`positive entropy` → `μ is algebraic`）与 Corollary 1.4（`not compactly supported`、`if k is prime` → `unique SL(k,ℝ)-invariant measure on X`）全句与印刷逐字吻合。修复依据：p.3 PNG 中 `For every u, v ∈ ℝ,` 逗号在 150dpi 下清晰可辨，文本层 `For every u, v ∈ R,` 同证。MD 行 49 起的 Theorem 1.5 属 p.4 内容，本页不判。

## p.004（PDF p.4 / 印刷 p.516）
- PNG：/tmp/linden06_audit_p004.png（pngmono 150dpi）；300dpi 仲裁裁片 `/tmp/linden06_p004_dimH.png`（Theorem 1.5 结论行）、`/tmp/linden06_p004_thm16.png`（Theorem 1.6 首行），均由 `-r300` 重渲本页后用 PIL 裁切放大（PIL 只裁图）。
- 核对：页眉（516 + 作者行）、Theorem 1.5 的 Ξ display 与结论行、Cassels–Swinnerton-Dyer [1] 段（含 `[K : ℚ] = 3`）、badly approximable 段与 `liminf` 两处、式 (1.2)、Pollington–Velani [35] 与 `effective`、线性形式 m_i 定义与 Σ_{j=1}^k、f_m 乘积 display、Theorem 1.6 全句与式 (1.3)、`Indeed` 段、Section 10/11 段、Hee Oh [32] 行。
- 结果：PASS±（差异列表：①页眉 `516 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS` 未保留（MinerU 系统性丢页眉）；②MD 行 62 `\text {   satisfies   }`、行 67 `\begin{array} { r } { … } \end{array}`、行 59 第二处 `\liminf _ { n \longrightarrow \infty }`（长箭头变体）为 MinerU 排版伪影，渲染语义不变，不误导；③印刷粗体 ℝ/ℤ 拍平为 MD 的 `\mathbb { R }`/`\mathbb { Z }`，不误导）
- 备注：**本页独立复核未发现新缺陷，无需 Edit**。两处关键字形已按 SOP 用 300dpi 亲自仲裁：①300dpi 裁片确认 Theorem 1.5 结论印刷为 `dim_H Ξ = 0. In fact, Ξ is a countable union of…`，H 为下标、Ξ 非粗体，MD 行 55 `\dim _ { H } \Xi = 0` 忠实（redo 所称旧伪影 `dim$. \boldsymbol{H} \boldsymbol{\Xi} = 0$. In$f a c t , \Xi$` 确已修复，本轮复核确认修复在位）；②300dpi 裁片确认 Theorem 1.6 印刷为 `of Hausdorff dimension k − 1`，**k 后无上标 2**，与 150dpi 整页图、`pdftotext -layout`（「dimension k−1」）及 `-raw`（「Hausdorff dimension k−1」）三通道一致；同页 p.2 印刷 ℝ^{k−1} 在同一提取中显式保留上标 2，说明文本层不丢上标，故 MinerU 原始输出中 Theorem 1.6 句尾的游离 `2` **无印刷来源**——Luna 删除该 `2` 判定正确，非回归，予以确认。式 (1.3) 的 300dpi 观察：inf 下标中 `x` 与 `{0}` 为**粗体**，MD 行 78 `\mathbf { x }`/`\mathbf {0}` 正确；而 p.4 末段印刷 `ℤ^k \ {0}` 的 0 **非粗体**，MD 行 83 `\mathbb { Z } ^ { k } \setminus \{ 0 \}` 亦为非粗体，粗细区分与印刷一致。线性形式 `m_i(x_1,…,x_k) = Σ_{j=1}^k m_{ij}x_j` 的双重指标方向（下标 i、上标 k）正确，未见 i/j 互换。

## p.005（PDF p.5 / 印刷 p.517）
- PNG：/tmp/linden06_audit_p005.png（pngmono 150dpi）；300dpi 仲裁裁片 `/tmp/linden06_p005_conjunction.png`（Conjecture 1.7 末句）、`/tmp/linden06_p005_tranversals.png`（Hee Oh 段末），由 `-r300` 重渲本页后 PIL 裁切（PIL 只裁图）。
- 核对：页眉（`THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 517`）、Conjecture 1.7 (Margulis, 1993) 全句、U₁/U₂ 两个 2×2 矩阵 display、Γ < G 条件段与脚注上标 1、Hee Oh [33] 段（含 [32]、[33, Thm. 1.5]、Theorem 10.2、§10、set 𝒟、`𝒟 has Hausdorff dimension n`、Section 7/10）、§1.3 Measure rigidity 前两段、脚注 1 全文、引用号 [22]/[45]/[12]/[33]/[32]/[17]/[13]。
- 结果：PASS±（差异列表：①页眉未保留（MinerU 系统性丢页眉）；②印刷花体 𝒟（集合 D）在 MD 行 101 拍平为普通斜体 `D`，语义无歧义，不误导）
- 备注：**两处印刷怪癖按铁律三原样保留并登记，不改**——本轮**亲自**以 300dpi 裁片复核，未沿用 redo 的裁片结论：①300dpi 确认印刷即 `up to conjunction in GL(2,ℝ) × ⋯ × GL(2,ℝ).`（按数学预期应为 conjugation），MD 行 99 忠实；②300dpi 确认印刷即 `regarding Hausdorff dimension and tranversals, and [33], [32]…`（缺 s），MD 行 101 忠实。两处均有 300dpi 裁片 + `pdftotext -layout` 双通道互证。**U₁/U₂ 矩阵 display 逐元素核验**：U₁ 两个因子均为上三角 `(1 *; 0 1)`、U₂ 两个因子均为下三角 `(1 0; * 1)`，中间 `⋯` 连接、U₂ 句末句点，与印刷一致（未发生上下三角互换）。Conjecture 1.7 的 `n ≥ 2`、`for both i = 1 and 2`、`Γ∩N∩U_i is trivial`、`Hilbert modular lattice^1` 上标与正文斜体（redo 已把旧的整词粗体伪影 `\boldsymbol { l a t t i c e ^ { 1 } }` 改为 `lattice$^ { 1 }$`，本轮确认修复在位）均正确。脚注 1 `For a definition of Hilbert modular lattices, see [33].` 与印刷逐字吻合。本页无需 Edit。MD 行 109 起（conditional measures 段）属 p.6 内容，本页不判。

## p.006（PDF p.6 / 印刷 p.518）
- PNG：/tmp/linden06_audit_p006.png（pngmono 150dpi）
- 核对：页眉（`518 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS`）、conditional measures/foliations 段、δ-measure 例外段（`three torus`、[17]）、[17] 附加假设段（singular direction、`sufficient`、weak<sup>∗</sup> limits）、`two new methods` 过渡句、first method 段（[3]、[4]、Haar measure、`Hausdorff dimension at most 1`）、third author 段开头（quantum unique ergodicity [20]、Host [9]、末句 `Let A be an ℝ-split`）。
- 结果：PASS±（差异列表：①页眉未保留（MinerU 系统性丢页眉）；②印刷粗体 ℝ 在 MD 行 117/119 的 `R-split`（两处）拍平，不误导）
- 备注：**本页独立复核未发现新缺陷，无需 Edit**。redo 在本页的 4 处修复本轮逐一确认**在位且与印刷一致**（以 `pdftotext -f 6 -l 6 -layout` 与整页 PNG 双通道互证）：①MD 行 111 `about$\mu$. Hence` 为单句点，旧双句点伪影 `$\mu .$.` 已消除（印刷 `information about μ. Hence`）；②MD 行 113 `hypothesis is sufficient` 双 f 正确（旧 `suficient` 已修）；③MD 行 115 `overcome this difficulty` 双 f 正确（旧 `dificulty` 已修）；④MD 行 119 `A different approach` 双 f 正确（旧 `diferent` 已修）。`weak<sup>∗</sup> limits` 的上标星与印刷 `weak∗ limits` 一致；`Haar measure`、`Hausdorff dimension at most 1`、引用号 [17]/[3]/[4]/[20]/[9] 均与印刷吻合。**越界观察（如实登记，不在本块范围故未改）**：全篇 MD 中仍存 `suficiently`（行 205）、`diferent`（行 307/469/535/677/971）、`dificulty`（行 537）等 OCR 单 f 残留，对应 PDF p.9 及以后页面，**不在本块 p.1–p.8 范围**，应由相应页段审计块处理；本块不越界修改。

## p.007（PDF p.7 / 印刷 p.519）
- PNG：/tmp/linden06_audit_p007.png（pngmono 150dpi）
- 核对：页眉（`THE SET OF EXCEPTIONS TO LITTLEWOOD'S CONJECTURE 519`）、third author 段后半（SL(2,ℝ)×SL(2,ℝ) Cartan、irreducible lattice、`do commute`、[3] 不适用）、two methods 互补段（[3]/[20]、Theorem 2.1 预告）、[20] 方法段（Ratner [39]/[38]、H-property、[28] §1.5、`a priori`、非 quasi-invariant）、Ledrappier-Young [19] 与 Tomanov–Margulis [26] 段、Acknowledgment 全段、`Part I. Measure rigidity` 标题、Part I 开篇约定（G=SL(k,ℝ)、k≥3、Γ 离散、X=G/Γ、A<G 为 k×k 正对角阵）。
- 结果：PASS±（差异列表：①页眉未保留（MinerU 系统性丢页眉）；②印刷粗体 ℝ 拍平为 MD 的 `SL(k, R)`/`\mathbb { R }`，不误导）
- 备注：**两处印刷怪癖按铁律三原样保留并登记，不改**——①印刷确为 `many one-parameter subgroup have positive entropy`（subgroup 用单数），MD 行 123 一致；②印刷确为 `measures with"low" (but positive)`（`with` 与 `"low"` 之间无空格，而同句 `with "high"` 有空格），MD 行 123 一致。两处均由 150dpi 整页图 + `pdftotext -layout`（「with“high”」有空格 vs「with“low”」无空格）双通道确认。**跨页句完整性核验**：p.6 末句 `Let A be an ℝ-split` 与本页首句 `Cartan subgroup of SL(2,ℝ) × SL(2,ℝ).` 属同一句，MD 在行 119→121 的合并中**句点保留正确**（行 121 末尾 `…\mathrm { S L } ( 2 , \mathbb { R } ).`），本轮确认 redo 的该处补点修复在位。Acknowledgment 段 9 处人名/机构（Dave Morris Witte、Barak Weiss、Sanju Velani、M. Ratner、Newton Institute for Mathematical Sciences in Cambridge in the spring of 2000、ETH Zurich、University of Washington、Center for Dynamical Systems at the Pennsylvania State University、Stanford University）与印刷逐字吻合，无缺句；`Section 1.5 of [28]`、[19]/[26]/[39]/[38]/[20]/[3] 引用号一致。本页无需 Edit。MD 行 135 起的 Σ 定义 display 属 p.8 内容，本页不判。

## p.008（PDF p.8 / 印刷 p.520）
- PNG：/tmp/linden06_audit_p008.png（pngmono 150dpi）
- 核对：页眉（`520 MANFRED EINSIEDLER, ANATOLE KATOK, AND ELON LINDENSTRAUSS`）、Σ 定义 display、α 记法与 ℝ^{k−1} flow、unipotent/normalizer/centralizer 定义段、U<G 被 A 正规化段（a(Ux)=Uax、Ad(a) expands）、ℳ_∞(Y) Radon/weak* 拓扑段、ν₁∝ν₂ display、B_ε^Y/B_ε^H 球记号段、右不变 Riemannian 度量段、§2 标题与 §2.1 开头、引用号 [17]/[45]/[20, §3]。
- 结果：PASS±（差异列表：①页眉未保留（MinerU 系统性丢页眉）；②印刷花体 ℳ / 粗体 ℝ 拍平为 MD 的 `$M _ { \infty } ( Y )$` 与 `\mathbb { R }`，不误导。**已修复 1 处**：MD 行 161 引用 `[ 1 7 , \ S 4 ]` 丢失印刷的 § 符号，渲染为 `[17, S4]` → 改为 `[17, §4]`）
- 备注：**唯一一处内容级缺陷及其实证**：印刷 §2.1 段为 `A discussion can be found in [17, §4], and a fairly general construction is presented in [20, §3].`；MinerU 输出行 161 把前一处写成 `$[ 1 7 , \ S 4 ]$`。其中 `\ ` 是 LaTeX/KaTeX 的**显式空格控制符**（反斜杠+空格为单字符控制符），印刷的 § 未被编码，其后的 `S` 成为普通字母。我用 matplotlib mathtext 实渲该串做实证（`python3` 渲 `r"$[ 1 7 , \ S 4 ]$"` → `/tmp/lt_test2.png`），亲眼确认渲染结果为 `[17, S4]`——§ 变成字母 **S**，读者会把「第 4 节」误读为「S4」。据原页改为纯文本 `[17, §4]`，与印刷及同句姊妹引用 `[20, §3]` 一致。`grep -n '\\ S'` 确认这是全篇**唯一**一处该伪影，不存在同型未修项。**其余逐项核验通过**：Σ display 的 `\{\mathbf{t} \in \mathbb{R}^k : t_1+\dots+t_k=0\}`、α 记法上标为**粗体 t**（`\alpha ^ { \mathbf { t } }` 与印刷一致）、ℝ^{k−1}、`(g - I_k)^n = 0`、`gHg^{-1} = H`、`N(H)`、`C(H)`、`Ad(a)`、`B_\varepsilon^H(I)`、`B_\varepsilon^H \cdot x`、`X = G/\Gamma`、§2 标题三行、§2.1 全部文字均与印刷吻合；印刷 `all locally finite Borel measures` 在 MD 中正确（`pdftotext` 输出的游离 `R` 为文本层伪影，非 MD 缺陷）。redo 在本页的 4 处修复（`normalized$b y \ g \in G$`→`normalized by$g \in G$`、`continuous$f .$.`→`continuous$f$.`、`around$y \in Y ;$;`→`around$y \in Y ;$`、`metric on$G .$.`→`metric on$G$.`）本轮逐一确认**在位且与印刷一致**。
- **溯源（按任务要求对每处缺陷执行）**：①行 161 的 `[ 1 7 , \ S 4 ]` 与 ②p.003 行 31 的缺逗号，两处**均非导出后被 peer 改坏的回归，而是原始 MinerU 导出的既有缺陷（前两轮审计漏检）**。证据：`git show cpf-redo/Lindenstrauss_2006_littlewood_exceptions^:<md>`（= `1a0c341c` integrate(audit): harvest Peer-P15）两处缺陷已原样存在；进一步取 Luna 修复提交 `d252350c` 的父提交 `d252350c^:<md>`（即 Luna 动手前的原始导出），两处缺陷同样原样存在；`git show d252350c -- <md>` 的 diff 未触及这两行；redo 的 p.003 提交 `ef7239b4` 与 p.008 提交 `140cc7a7` 的 diff 亦未触及这两行（两次 grep 均无输出）。故原导出在此两处不正确，Peer-P15 与 Wf-R-P15 均未引入亦未修复，本块按印刷原文补正。
