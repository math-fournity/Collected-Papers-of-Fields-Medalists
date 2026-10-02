# AUDIT — Borcherds_1992_monstrous_moonshine

- Status: `CANDIDATE_NOT_CURRENT` (41/41 page entries recorded; post-audit repair and full reread committed; canonical integration pending).
- Actor: `Peer-P07`
- Model: `gpt-6-luna`
- Reasoning effort: `max`
- Base: `e04c4a9603818cfa2d71271942f696115783c33b`
- PDF: `Borcherds_1992_monstrous_moonshine.pdf` — 41 PDF pages; Creator `TeX`; Producer `pdfTeX-0.14a`; SHA-256 `dee2cb9c3121cf1bf8bddce952d952e0f478a39e497df8946e220e9ceffab501`.
- MinerU Markdown: `Borcherds_1992_monstrous_moonshine_mineru/Borcherds_1992_monstrous_moonshine__Borcherds_1992_monstrous_moonshine.md` — baseline SHA-256 `2d89f26db76e7e2187a916d82120cb40f2296092f636fc830c03f8373ea75b18`; last path commit `4e5d9aabe1bc05fbb69fe4f77c0e692470fd9935`.
- MinerU export identity: `Borcherds_1992_monstrous_moonshine/`; `structured_content.json` reports producer `mineru 3.4.4`, `is_full_document=true`, 41 page records. PDF text extraction is 141,476 bytes with 0 U+FFFD characters.
- Method: born-digital text-layer reconciliation against the MinerU page records/Markdown in PDF page order; 150 dpi `pngmono` visual samples for the title/abstract page and selected dense mathematics pages. Text extraction is a comparison channel; dropped or flattened symbols remain subject to original-page review when disputed.
- Scope note: the assigned expected count and direct PDF/JSON evidence agree at 41 pages. Root `README.md` describes this PDF as 44 pages; that asset-map count conflicts with the file and is left for the canonical integrator to reconcile. This peer does not edit root state.
- Original source chain: the PDF and raw MinerU Markdown are tracked at the assigned base. The raw Markdown remains recoverable; post-audit edits were made only after all 41 page audits and are isolated in the separate fix commit listed below.

## p.001 (PDF p.1 / printed p.1)

- Checked at: 2026-10-01 15:49 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: MinerU `structured_content.json` page_idx 0 contains the title page through the opening of Theorem 1.1; Markdown has the same sequence. PDF text layer and rendered page agree on title, journal citation, author, abstract, contents list, and theorem opening.
- Visual evidence: `audit/p001.png` (`pngmono`, 150 dpi); inspected title, author/address, abstract, contents, citation `[16,17]`, and printed page number 1.
- Result: `PASS±`.
- Differences for post-audit repair review: Markdown has `Cam bridge` for printed `Cam-bridge`/“Cambridge”; splits `representation` as `repre sentation`; reads printed `affine` as `afine`; encodes the printed Conway group `Co_1` in the abstract as `C o _ { 1 }`; and encodes the theorem citation `[16,17]` as `\lceil 1 6 , 1 7 \rceil`. The abstract spelling of `Co_1` was checked against `audit/p001.png`. No paragraph omission was found on this page. These are recorded now and will not be edited until the full 41-page audit is complete.

## p.002 (PDF p.2 / printed p.2)

- Checked at: 2026-10-01 15:56 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 1 continues Theorem 1.1, then covers the monster representation and Thompson series, ending in the definition of a Hauptmodul; the text layer and Markdown follow the same page boundary and paragraph sequence.
- Result: `FAIL`.
- Differences for post-audit repair review: the elliptic modular function is printed/extracted as `j(τ) - 744`, but Markdown encodes `j(\dot{\tau}) - 744`; the phrase “level 1” is encoded with an erroneous superscript `\mathfrak{s}`; `The Fischer-Griess` is joined as `TheFischer-Griess`; and `coefficient`, `difficulty`, and `difficult` appear as `coeficient`, `dificulty`, and `dificult`. No paragraph omission was found. The symbol change in `j(τ)` requires correction after the full audit; typographic OCR issues are recorded for the same repair pass.

## p.003 (PDF p.3 / printed p.3)

- Checked at: 2026-10-01 15:58 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 2 starts with the continuation “of j” and covers the formula for `j`, genus-0 Hauptmoduls, the `Γ₀(2)` example, and the Thompson-series discussion through the opening of the monster Lie algebra; page ending agrees.
- Visual evidence: `audit/p003.png` (`pngmono`, 150 dpi); inspected the displayed formula for `j`, `Γ₀(2)` product, the translation matrix, and printed page number 3.
- Result: `FAIL`.
- Differences for post-audit repair review: the printed translation matrix `\begin{pmatrix}1&1\\0&1\end{pmatrix}` is serialized in Markdown as `\textstyle { \binom { 1 } { 0 } } 1`, losing its second column structure. Several coefficients/powers are split into spaced digits in TeX (for example `240`, `24`, `276`, `2048`), reducing reliable plain-text searching. Markdown also has `dificulty`/`dificult` for printed `difficulty`/`difficult`, and typesets the article's “a function” as `\mathrm{a} function`. The source itself prints the duplicated words “to to work out”; this is a print quirk and must remain unchanged. No paragraph omission was found.

## p.004 (PDF p.4 / printed p.4)

- Checked at: 2026-10-01 15:57 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 3 contains the monster Lie algebra degree chart and the introduction to generalized Kac-Moody algebras, ending at the sentence that introduces the product formula; page text follows the same order as the PDF.
- Result: `FAIL`.
- Differences for post-audit repair review: the printed “`Z₂`-orbifold” is malformed in Markdown as `Z _ { \mathrm { 2 ^ { - O r b i f o l d } } }`; the references to `sl₂` and `sl₂`'s are also broken into OCR/TeX fragments (`s l _ { 2 }` with spurious superscripts). The prose has `diference` and `afine` for printed `difference` and `affine`. The mathematical notation changes in the orbifold and Lie-algebra names need repair after the full audit; spelling defects are recorded for the same pass. No paragraph omission was found.

## p.005 (PDF p.5 / printed p.5)

- Checked at: 2026-10-01 15:57 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 4 begins with the `p,q` product formula for the monster Lie algebra and covers the alternating exterior/homology sum through its Weyl-group interpretation; the text-layer and Markdown page boundaries agree.
- Visual evidence: `audit/p005.png` (`pngmono`, 150 dpi); inspected the product identity, `Λ(E)=H(E)`, alternating terms, and printed page number 5.
- Result: `PASS±`.
- Differences for post-audit repair review: the product and homology formulas are substantively aligned. The possessive in printed `Λⁱ(E)'s` is encoded as a superscript-star TeX fragment (`\mathrm{ { ^ { * } s } }`), and Markdown spells `coefficients`/`difficult` as `coeficients`/`dificult`. No mathematical claim or paragraph was found missing on this page; repair the OCR text/markup after the full audit.

## p.006 (PDF p.6 / printed p.6)

- Checked at: 2026-10-01 15:57 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 5 continues the homology discussion, states the homology groups and trace identity, then covers the coefficient-recursion discussion, acknowledgments, and the start of the notation list. Paragraph order and page transition agree.
- Result: `PASS±`.
- Differences for post-audit repair review: the page repeatedly spells printed `coefficients` as `coeficients`. The `pdftotext` layout stream interleaves the phrase around “In section 8 we use this to work out the homology groups” with the nearby displayed equation; the page-indexed MinerU text and Markdown preserve the prose/equation sequence, so this is retained as an extraction-layout limitation rather than a confirmed print/OCR disagreement. No omitted paragraph or substantive formula difference was identified in the text-layer comparison.

## p.007 (PDF p.7 / printed p.7)

- Checked at: 2026-10-01 15:57 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 6 is the notation list from `C` through `p₂₄(n)` and its partition series; entries and page boundary match the PDF sequence.
- Result: `FAIL`.
- Differences for post-audit repair review: the printed Gram matrix for `II_{1,1}` is serialized as `\binom{0\ -1}{-1\ 0}` rather than a 2×2 matrix; `II_{25,1}` is corrupted to `II_{25,\cdot}`; and the Leech-lattice double cover is left as `Λ<sup>ˆ</sup>`. In the fake-monster partition series, Markdown inserts `324256 q^5` before the source's `1073720 q^5`, an unsupported extra coefficient. The description of `ε(α)` also has `of s generalized` for `of a generalized`. The notation entry also drops the superscript on the printed normalizer symbol `Γ₀(N)^+`; `audit/300dpi/p007-gamma-plus.png` shows the source placement. These mathematical/lattice and coefficient errors require correction after the full audit; no whole notation entry was omitted.

## p.008 (PDF p.8 / printed p.8)

- Checked at: 2026-10-01 15:57 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 7 completes the notation list (`q` through `ω`) and begins section 2, Introduction (continued); the page transition and paragraph order match the PDF.
- Result: `FAIL`.
- Differences for post-audit repair review: the Weyl-vector identity is printed as `(ρ,r)=−(r,r)/2`, but Markdown omits the equality sign; the definition of `T_g(q)` adds a dot over `c_g(n)` and omits the equality in `c_g(n)=Tr(g|V_n)`. The double-cover notation is also fragmented (`Λ<sup>ˆ</sup>`), and `V_Λ is the the fake monster vertex algebra` duplicates `the` relative to the PDF text layer. These alter mathematical notation or the stated definition and require post-audit correction.

## p.009 (PDF p.9 / printed p.9)

- Checked at: 2026-10-01 15:57 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 8 continues the second-family discussion, presents denominator formulas (2.1)–(2.3) and the root-multiplicity explanation, and ends mid-example at “if N”; sequence and continuation match.
- Result: `PASS±`.
- Differences for post-audit repair review: the formulae (2.1)–(2.3), including the divisor condition and `g^s` trace term, agree with the PDF text layer. Markdown has `g_;` in the prose where the PDF has `g,`, repeats the spelling `coeficients`, and splits the Möbius-function superscript into residual HTML `<sup>` fragments. No formula term or paragraph omission was found.

## p.010 (PDF p.10 / printed p.10)

- Checked at: 2026-10-01 15:57 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 9 continues the squarefree-level example through formula (2.4), then gives the fake-monster denominator formula, root description, and the opening of the rank-10 superalgebra construction. All page sections and the final sentence continue at PDF p.11 as expected.
- Result: `PASS±`.
- Differences for post-audit repair review: the displayed product identities and the `p₂₄(1−r²/2)` root multiplicity agree with the page text. The printed `Γ₀(N)^+` in the normalized-generator sentence loses the superscript on `+`; `audit/300dpi/p010-gamma-plus.png` confirms the placement. Repeated coefficient spellings and spaced digits remain OCR search/markup defects, but no distinct formula-value mismatch or missing paragraph was found on this page.

## p.011 (PDF p.11 / printed p.11)

- Checked at: 2026-10-01 16:08 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 10 finishes the rank-10 fake-baby-monster construction and starts section 3, Vertex algebras; all paragraphs continue at the same boundary as the PDF.
- Result: `FAIL`.
- Differences for post-audit repair review: in the generating function defining `p_g(n)`, the PDF has `(1−q^{2n})^{-8}`, while Markdown encodes `(1−\dot q^{2n})^{-8}`. The same extra dot appears in the second factor of the later product defining `p_g`. This changes the stated series and must be repaired after the full audit. No paragraph was omitted.

## p.012 (PDF p.12 / printed p.12)

- Checked at: 2026-10-01 16:08 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 11 states the vertex-algebra axioms, Jacobi identity, vertex-operator definition, examples, the operator `D`, and the opening conformal-vector definition; page flow agrees.
- Result: `FAIL`.
- Differences for post-audit repair review: the printed vertex operator is `V(u,z)`, but Markdown renders it as a bold-`Π` expression; axiom (3) prints `v_{−1}1=v`, while Markdown breaks the subscript into `v<sub>−</sub>._{1}1=v`; and the conformal-vector clause adds a spurious `\Psi` before `c∈R`. These alter core notation/definition and require repair. The surrounding text and Jacobi identity are present.

## p.013 (PDF p.13 / printed p.13)

- Checked at: 2026-10-01 16:09 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 12 continues the conformal-vector definition, gives the Virasoro commutator and adjoint formula, and discusses vertex-operator algebras and tensor products; the page continues to p.14 as in the PDF.
- Result: `FAIL`.
- Differences for post-audit repair review: in the adjoint formula for `u_n`, the PDF summation begins at `j≥0`, while Markdown encodes `j>0`, dropping the `j=0` term. The expression for the bilinear-form adjoint is therefore incomplete. The remaining definitions and tensor-product formula align with the text layer.

## p.014 (PDF p.14 / printed p.14)

- Checked at: 2026-10-01 16:09 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 13 lists the three monster-vertex-algebra properties, the representation decompositions, and starts section 4 on generalized Kac-Moody algebras; page boundary matches.
- Result: `PASS±`.
- Differences for post-audit repair review: the opening reference to `V [3,16]` contains an extra closing parenthesis in Markdown, and `coefficients` is misspelled `coeficients`. The three properties and the listed character decompositions match the PDF text layer; no mathematical statement was found missing.

## p.015 (PDF p.15 / printed p.15)

- Checked at: 2026-10-01 16:09 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 14 covers the contravariant form, the universal generalized Kac-Moody generators and relations, and Theorem 4.1 through its final continuation sentence; the page sequence agrees.
- Result: `PASS±`.
- Differences for post-audit repair review: Markdown spells `affine` and `difference` as `afine` and `diference`. In the orthogonality condition, an extra OCR `i` precedes the printed `if i≠−j`; the condition remains identifiable. The generator relations and Theorem 4.1 statements otherwise agree with the PDF text layer; no condition or paragraph was omitted.

## p.016 (PDF p.16 / printed p.16)

- Checked at: 2026-10-01 16:12 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 15 continues Theorem 4.1 and lists universal generalized Kac-Moody algebra properties (1)–(6), ending with the Cartan involution; list order and continuation match.
- Result: `PASS±`.
- Differences for post-audit repair review: `affine` is misspelled `afine` in the clause excluding affine Kac-Moody matrices. The grading, root-lattice, Weyl-vector, and involution statements otherwise match the PDF text layer; no property was omitted.

## p.017 (PDF p.17 / printed p.17)

- Checked at: 2026-10-01 16:12 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 16 completes the invariant-form property, gives the character formula for lowest-weight modules, and discusses roots as vectors in the Cartan subalgebra through the beginning of the multiset explanation.
- Result: `PASS±`.
- Differences for post-audit repair review: the character and denominator formulas, including `ε(α)` and `e^{α+λ}`, match the text layer. Markdown breaks the quoted prose word “set” into residual superscript fragments (`^{66}set^{9}`) in the multiset explanation; spelling/markup needs repair, but the mathematical multiplicity statement remains present.

## p.018 (PDF p.18 / printed p.18)

- Checked at: 2026-10-01 16:12 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 17 continues the multiset example, discusses the extension to superalgebras, and derives `Λ(E)=H(E)` and the generalized denominator formula through the continuation to p.19.
- Result: `FAIL`.
- Differences for post-audit repair review: the PDF uses `ε(α)` in the denominator sum, while Markdown writes `ε(\bar{α})`; the homology alternating sum has `Θ` in place of the printed minus operation between `H₀(E)` and `H₁(E)`; and the prose explaining `ε(ir)=\binom{n}{i}(-1)^i` says only `<sup>n</sup>` ways rather than the printed binomial count. The quoted word “set” is again fragmented into superscript markup. These change a formula argument/sign and its combinatorial count; correct after full audit.

## p.019 (PDF p.19 / printed p.19)

- Checked at: 2026-10-01 16:12 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 18 finishes the homology characterization, starts section 5, and states Theorem 5.1 through the beginning of its proof; the PDF/Markdown page break agrees.
- Result: `FAIL`.
- Differences for post-audit repair review: in Theorem 5.1, the printed subspace `V^i` is interrupted in Markdown by a spurious `\because` symbol; the lattice `II_{1,1}` is corrupted in the final proof sentence to `II_{1,\cdot}1`. These are part of the theorem's space and grading identifiers and require correction. The remaining theorem conditions and conclusion are present.

## p.020 (PDF p.20 / printed p.20)

- Checked at: 2026-10-01 16:12 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 19 defines the Virasoro and `K_i` operators, the spaces `H,P,S,N,T,K`, gives their inclusion diagram, and states Lemma 5.1 and its spanning vectors; page continuation agrees.
- Result: `FAIL`.
- Differences for post-audit repair review: the vertex algebra subscript `V_{II_{1,1}}` is corrupted in Markdown as `V_{II_{1,.}}1`; Lemma 5.1's printed opening “If `f` is a vector…” is serialized as `Lemma 5.1. _{If f}`, breaking the statement; and `differ` is misspelled `difer` in the paragraph on the two possible choices for `e^w`. The PDF text layer reads `differ`. The displayed commutator relations and spanning-vector formula otherwise match the page text. Repair the damaged identifiers/opening after full audit.
- Visual evidence: `audit/300dpi/p020-quotient-bracketing.png` (`pnggray`, 300 dpi). The print shows `P^1/N∩P^1` inline without parentheses; the following sentence identifies the target as the quotient of `P^1` by its nullspace `P^1∩N`. The Markdown repair writes `P^1/(N∩P^1)` to make that same quotient explicit.

## p.021 (PDF p.21 / printed p.21)

- Checked at: 2026-10-01 16:13 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 20 completes Lemmas 5.2–5.5 and the no-ghost conclusion, then starts Theorem 6.1 and its lattice setup; the page ends partway through property (2), matching the PDF.
- Result: `FAIL`.
- Differences for post-audit repair review: Lemma 5.5 states `P^1=T^1⊕N^1` in print, but Markdown inserts a dot before `T^1` and breaks the possessive after `L_i` with extra TeX fragments; the Lemma 5.4 condition `i<0` is letter-spaced as `i ~ < ~ 0`. In the opening of Theorem 6.1, the printed `II_{1,1}` grading and Gram matrix `[[0,−1],[−1,0]]` are corrupted: the lattice is marked with a stray superscript minus, and the Markdown matrix encoding omits the final `0`. These affect the lemma and lattice data and require repair.
- Supplemental visual evidence: `audit/300dpi/p021-no-ghost-quotient.png` (`pnggray`, 300 dpi) confirms the printed no-ghost conclusion says `T^1` is isomorphic to the quotient of `P^1` by its nullspace.

## p.022 (PDF p.22 / printed p.22)

- Checked at: 2026-10-01 16:13 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 21 finishes Theorem 6.1, its construction/proof, Theorem 6.2, and the remarks on lattice vertex algebras; paragraph order and ending match.
- Result: `FAIL`.
- Differences for post-audit repair review: both the PDF text layer and Markdown use `v≠0`/`v=0` in the no-ghost conclusion here, although Theorem 6.1 is phrased in terms of the degree pair; this is the printed notation and is not an OCR difference. The equality `1−(m,n)^2/2=1−mn` is serialized as `1−−mn`, and a `V_{II_{1,1}}` reference is malformed as `V_{II_{1,:}}`. These latter sign/identifier errors require correction after full audit.

## p.023 (PDF p.23 / printed p.23)

- Checked at: 2026-10-01 16:13 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 22 gives the construction motivation for the monster Lie algebra, then states Theorem 7.1 and its denominator identity, proving it by logarithmic expansion through the Hecke-operator argument.
- Result: `FAIL`.
- Differences for post-audit repair review: the motivating tensor-product explanation uses the lattice vertex algebra `V_{II_{1,1}}` in print, but Markdown corrupts its subscript as `V_{II_{1,}}` (the terminal `1` is missing). The denominator identity and the logarithmic/Hecke expansion otherwise align with the PDF text layer; restore the lattice identifier after the full audit.

## p.024 (PDF p.24 / printed p.24)

- Checked at: 2026-10-01 16:13 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 23 proves Theorem 7.2 from the denominator formula, computes `S`, compares the two right-hand sides, and starts section 8; the argument is present in the same order.
- Result: `FAIL`.
- Differences for post-audit repair review: the printed `e^ρ=e^{(−1,0)}=p^{−1}` is encoded with a dot over `e` and a bar over the first coordinate; the graded root lattice `II_{1,1}` is also broken as `II_{1,}` in the closing remark. These misstate key Weyl/group-ring identifiers and require repair. The `c(mn)` multiplicity conclusion agrees with the PDF.

## p.025 (PDF p.25 / printed p.25)

- Checked at: 2026-10-01 16:13 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 24 derives the homology groups `H_i(E)`, summarizes their graded characters, and explains why only `H_0`, `H_1`, and `H_2` are nonzero; all paragraphs are represented.
- Result: `FAIL`.
- Differences for post-audit repair review: Markdown corrupts the `II_{1,1}` grading label in the summary as `II_{1,1^{-g}}`-like TeX fragments, so the graded-vector-space type is not faithfully represented. Several `coefficients` are also spelled `coeficients`. The homology-space formulas and character expressions otherwise match the PDF text layer.

## p.026 (PDF p.26 / printed p.26)

- Checked at: 2026-10-01 16:15 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 25 derives (8.2), states the finite/infinite-dimensional splitting-principle conditions, derives (8.3), and closes with the complete-replicability discussion; page boundary matches.
- Result: `FAIL`.
- Differences for post-audit repair review: the printed alternating sum `Σ(−1)^i H_i(E)` is serialized as `\mathbb{\phi}(−1)^iH_i(E)`, and the printed `II_{1,1}`-graded module label has an extra HTML `<sub>1</sub>`. Equations (8.2) and (8.3) otherwise match the PDF text layer. Correct the damaged alternating-sum and grading notation after full audit.

## p.027 (PDF p.27 / printed p.27)

- Checked at: 2026-10-01 16:15 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 26 begins section 9 and gives the recursion relations (9.1), the coefficient-determination argument, and the start of the comparison with known Hauptmoduls.
- Result: `FAIL`.
- Differences for post-audit repair review: the PDF states the recursion degenerates as `c_g(5)=c_g(5)`, but Markdown writes the second occurrence with an overbar, `c_g(\bar{5})`. The recursion formulas themselves align with the PDF text layer; the extra bar changes this explicit identity and needs correction. Repeated `coeficients` spelling errors are also present.

## p.028 (PDF p.28 / printed p.28)

- Checked at: 2026-10-01 16:15 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 27 continues the recursion argument, determines the needed irreducible-character data, and gives formula (9.2) and the eta-function description; all material is present.
- Result: `FAIL`.
- Differences for post-audit repair review: the PDF determinant is `35672555520`, while Markdown gives `3567255552` before a stray closing parenthesis, omitting a zero. This changes the reported nonzero character-table determinant. Formula (9.2) and the eta-product definition match the text layer; correct the determinant after full audit.

## p.029 (PDF p.29 / printed p.29)

- Checked at: 2026-10-01 16:15 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 28 concludes the character-table argument and theorem 1.1 proof, then starts section 10 and defines the superalgebra family; sequence and page transition match.
- Result: `PASS±`.
- Differences for post-audit repair review: the page has recurring `coefficients` → `coeficients` spelling defects; the printed odd-order group names `Co_1` are fragmented as `C o _ { 1 }`; and the final Thompson-series formula has a malformed trace expression. The PDF p.29 text layer gives `Co1` and `Tr(g|V_n)q^n`. The 150 dpi title-page image `audit/p001.png` confirms the Co₁ subscript form. The 3B/5B/7B/9B/13B/15D class list, formula for `T_g(q)`, superdimension convention, and root-multiplicity definition otherwise agree with the PDF text layer.

## p.030 (PDF p.30 / printed p.30)

- Checked at: 2026-10-01 16:15 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 29 gives the definition of root multiplicities, denominator identities (10.1)–(10.5), Möbius inversion, and the start of the squarefree-level example; the continuation to p.31 matches.
- Result: `FAIL`.
- Differences for post-audit repair review: formulas (10.1)–(10.5) align with the PDF text layer. The following example's exact group notation is badly serialized: `Γ₀(N)^+` with its `d|N₁` condition and the conjugating matrix are broken into a dotted plus, `\binom` fragments, and stray overbars/TeX delimiters. Because this changes the stated modular-group condition, repair from the printed page after full audit.

## p.031 (PDF p.31 / printed p.31)

- Checked at: 2026-10-01 16:17 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 30 continues the squarefree-level example, derives (10.6)–(10.8), and discusses the `N₂=1` and `N₂=2` cases through the sign pattern of root multiplicities.
- Result: `FAIL`.
- Differences for post-audit repair review: the `N₂=2` hypothesis names the group `Γ₀(2N₁)^+` with the `d|N₁` Atkin–Lehner condition, but Markdown flattens the superscript/condition into `Γ₀(2N₁)+ d|N₁`, leaving the actual group notation ambiguous; `audit/300dpi/p031-n2-condition.png` preserves that printed notation. The `N₂=1` discussion also flattens the superscript on `Γ₀(N)^+` in three mentions; `audit/300dpi/p031-group-plus.png` confirms the printed superscript. The phrase `we get are` is split as `we g e t are`. The multiplicity equations (10.6)–(10.8) match the PDF text layer. `coefficients` is repeatedly misspelled.

## p.032 (PDF p.32 / printed p.32)

- Checked at: 2026-10-01 16:17 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 31 begins section 11, defines the groups `Γ(2)` and `Γ₀(4)`, lists weight-4 modular forms, and states Lemma 11.1 with its proof.
- Result: `FAIL`.
- Differences for post-audit repair review: both defining matrix sets are serialized with `\binom` stacks where the PDF has 2×2 matrices, so the congruence conditions for `Γ(2)` and `Γ₀(4)` are not faithfully represented. The range of Fourier coefficients also contains a stray overbar/mark after `q^0`; repair these matrix and range notations after full audit. The displayed theta/eta coefficients and Lemma 11.1 identities otherwise align.

## p.033 (PDF p.33 / printed p.33)

- Checked at: 2026-10-01 16:17 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 32 gives the weight-8 theta/eta expansions and Lemma 11.2, then begins section 12 and introduces the fake-monster root lattice.
- Result: `FAIL`.
- Differences for post-audit repair review: in the root norm, the PDF has `λ²−2mn`, while Markdown inserts a dot on `m` as `λ²−2\dot m n`, changing the lattice quadratic form. The PDF sets the Barnes–Wall normalizer as `Γ₀(2)^+`; Markdown loses the superscript on `+`, confirmed by `audit/300dpi/p033-group-plus.png`. The PDF print also sets the lemma heading as `Lemma 11. 2.`, and Markdown retains this source spacing, confirmed by `audit/300dpi/p033-lemma-heading.png`. The theta/eta series coefficients and Lemma 11.2 identities otherwise match the PDF; correct the norm symbol after full audit.

## p.034 (PDF p.34 / printed p.34)

- Checked at: 2026-10-01 16:17 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 33 describes the fake-monster root system and group action, gives an explicit graded construction of `V_Λ`, and states Lemma 12.1 through its hypotheses.
- Result: `FAIL`.
- Differences for post-audit repair review: the partition series is printed as `1/Δ(q)` but Markdown uses `1/\bar{Δ}(q)`; the action of `2^{24}Aut(Λ)` is written with `Aut(\dot{Λ})`; and `Λ`-graded labels acquire stray multiplication dots. These alter the generating function and lattice/group identifiers. The surrounding construction is present and must be repaired from the PDF after full audit.

## p.035 (PDF p.35 / printed p.35)

- Checked at: 2026-10-01 16:17 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 34 proves Lemma 12.1, gives its involution examples, describes `H(E)` for `M_Λ`, and starts section 13.
- Result: `FAIL`.
- Differences for post-audit repair review: the proof's product `vσ(v)…` is interrupted by a spurious multiplication dot; the graded type is printed as `II_{25,1}` but serialized with fragments after `II_{25,1}`; and section 13 calls `L′` the dual lattice and the automorphism order `N`, whereas Markdown writes `L<sup>0</sup>` and `N_*`. These symbols identify the lattice dual/order parameter and must be corrected from the page text after full audit.

## p.036 (PDF p.36 / printed p.36)

- Checked at: 2026-10-01 16:18 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 35 derives the trace and multiplicity formulas (13.1)–(13.2), describes the reflection group `W^g`, and states the twisted denominator formula (13.3); all sections are present.
- Result: `FAIL`.
- Differences for post-audit repair review: in the generalized cycle-shape notation used to define `η_g(q)`, the PDF has `a₁^{b₁}a₂^{b₂}…`, while Markdown adds an overbar to the first exponent (`a₁^{\bar b₁}`). This changes the cycle-shape parameter and must be corrected. The formula (13.3) and the appended May 1999 note are otherwise represented.

## p.037 (PDF p.37 / printed p.37)

- Checked at: 2026-10-01 16:18 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 36 identifies the simple roots and their multiplicities for the superalgebra, then begins section 14 and Example 1, the rank-18 fake baby monster algebra.
- Result: `FAIL`.
- Differences for post-audit repair review: the opening says the twisted formula is evaluated for elements of `Aut(\hat{Λ})`, but Markdown drops the hat and states `Aut(Λ)`. The named group acts on the central extension, so restore the double-cover notation after full audit. The simple-root multiplicity sum and first-example setup otherwise follow the PDF.

## p.038 (PDF p.38 / printed p.38)

- Checked at: 2026-10-01 16:18 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 37 finishes the rank-18 denominator formula, gives the prime-order family, and begins the rank-10 fake Conway superalgebra example.
- Result: `FAIL`.
- Differences for post-audit repair review: the PDF names the dual of the even-vector sublattice as `I_{9,1}`, but Markdown renders it as a calligraphic `\mathcal I_{9,1}`. This changes the lattice identifier in the rank-10 construction. The p.38 prose glyph for the primitive root of unity is also replaced in Markdown by control character U+000F; `audit/300dpi/p038-epsilon.png` confirms the print is `ε`. The theta-coset and eta-product formulas on this page otherwise align with the text layer.

## p.039 (PDF p.39 / printed p.39)

- Checked at: 2026-10-01 16:18 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 38 completes the fake Conway multiplicity generating function and lists open questions (1)–(8), ending with the comparison of `E₈` and `E₈⊕E₈` lattices.
- Result: `PASS±`.
- Differences for post-audit repair review: the rank-3 product identity, its index conditions, and the generating function for `c(n)` agree with the PDF text layer. Markdown has `difficult` as `dificult` and repeats other OCR spelling artifacts; no mathematical term or open question was omitted.

## p.040 (PDF p.40 / printed p.40)

- Checked at: 2026-10-01 16:18 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 39 closes open question (8) and begins the References section, listing references [1]–[20]; entries and page transition correspond to the PDF.
- Result: `PASS±`.
- Differences for post-audit repair review: the reference list is present in sequence and matches the PDF text layer on authors, titles, journals/books, dates, volumes, and page numbers. Residual differences are typographic casing/line-wrap artifacts; no missing or additional reference was found on this page.

## p.041 (PDF p.41 / printed p.41)

- Checked at: 2026-10-01 16:18 EDT
- Actor: `Peer-P07`; model: `gpt-6-luna`; effort: `max`.
- PDF/Markdown page alignment: page_idx 40 contains the concluding References [21]–[31] and printed page number 41; all eleven entries are present in the same order.
- Result: `PASS±`.
- Differences for post-audit repair review: reference [22] prints `Princeton` across a line-end hyphen (`Prince-` / `ton`), while Markdown has `Prince ton`; this should be joined to `Princeton` for searchability. Reference details [21]–[31] otherwise match the PDF text layer.

## Post-audit repair registration and final reread

- Page-audit scope: all 41 PDF pages have page entries above. The page grades are the initial pre-repair findings: 28 `FAIL`, 13 `PASS±`; they remain historical page verdicts and were not rewritten to imply a fresh post-fix page audit.
- Raw MinerU Markdown at the assigned source snapshot: SHA-256 `2d89f26db76e7e2187a916d82120cb40f2296092f636fc830c03f8373ea75b18`, last path commit `4e5d9aabe1bc05fbb69fe4f77c0e692470fd9935`.
- Post-audit Markdown repair commit: `01fe4a35f8075d3a8a30a56c159660e51045f0d2`; final Markdown SHA-256: `b09bb557b3f70e02088f4a542d370fd530749b086fc6c3773151f897a639cbb1`.
- Final reread: after the last Markdown edit, I reread the complete final file from line 1 through line 1,055, including references [1]–[31], against the 41-page PDF/text-layer sequence. Every registered repair was checked at its source page; no new page-level omission or edit-introduced discrepancy was found.
- Read-only verification: `git diff --check` passed before the fix commit; the final control-character scan found no non-whitespace C0 controls. Targeted residual searches found none of the repaired OCR spellings, the unsupported `324256 q^5` coefficient, the p.31 spaced inequality, or the p.38 U+000F glyph. Remaining HTML superscript/subscript fragments are the Kronecker-delta relation, \(R^2\), and \(E_{10}\) in reference [24].

### Repairs by PDF page

- pp.1–4: joined “Cambridge” and “representation”; corrected “affine”/“difficulty” spellings; restored citation [16,17], \(Co_1\), \(j(\tau)\), the level-1 wording, the \(SL_2(\mathbb Z)\) translation matrix, coefficient typography and “a function”; repaired the \(\mathbb Z_2\)-orbifold and \(sl_2\) notation. The printed “to to work out” on p.3 remains unchanged.
- pp.5–10: repaired the \(\Lambda^i(E)\) possessive and recurring “coefficients” spellings; restored the \(II_{1,1}\) Gram matrix, \(II_{25,1}\), \(\hat\Lambda\), and the fake-monster partition series (removed unsupported \(324256q^5\)); restored the Weyl-vector equality and \(c_g(n)=\operatorname{Tr}(g\mid V_n)\); corrected the normalizer \(\Gamma_0(N)^+\), related product notation, and OCR punctuation.
- pp.11–18: removed spurious dots from \(p_g\); restored \(V(u,z)\), \(v_{-1}\mathbf1=v\), and the conformal-vector condition; restored the \(j=0\) term in the adjoint sum; repaired citation punctuation, affine/difference spellings, multiset “set”, \(\epsilon(\alpha)\), the homology minus sign, and the binomial coefficient count.
- pp.19–25: restored \(V^i\), \(II_{1,1}\) and \(V_{II_{1,1}}\) identifiers, \(P^1=T^1\oplus N^1\), the Gram-matrix entries and the quotient grouping; corrected the p.20 “differ” spelling and p.21 \(L_i\)'s/\(i<0\); restored the equality in \(1-(m,n)^2/2=1-mn\), \(e^\rho=e^{(-1,0)}\), and the \(II_{1,1}\)-graded homology labels.
- pp.26–29: restored \(\sum(-1)^iH_i(E)\) and the grading label; removed the overbar from \(c_g(5)\); restored the determinant \(35672555520\); normalized the \(Co_1\) and trace-series notation.
- pp.30–33: repaired the modular-group matrix encodings, Atkin–Lehner condition, and superscripted \(\Gamma_0(N)^+\) notation; restored the \(\Gamma(2)\)/\(\Gamma_0(4)\) matrix sets and coefficient range; corrected \(\lambda^2-2mn\), \(1/\Delta(q)\), \(\operatorname{Aut}(\hat\Lambda)\), and the Barnes–Wall normalizer. The printed heading “Lemma 11. 2.” on p.33 is retained as printed.
- pp.34–38: restored the fake-monster product, \(II_{25,1}\), \(L'\), automorphism order \(N\), the unmarked cycle-shape exponent \(b_1\), \(\operatorname{Aut}(\hat\Lambda)\), \(I_{9,1}\), and \(\epsilon\) in place of U+000F.
- pp.39–41: corrected the remaining “difficult” spelling and joined reference [22]'s split “Prince-ton” to “Princeton”; other references and the open-question statements were retained where they matched the PDF.

### Supplemental visual evidence

- Existing 150 dpi samples: `audit/p001.png`, `audit/p003.png`, `audit/p005.png`.
- Previously committed 300 dpi no-ghost/quotient adjudication: `audit/300dpi/p020-quotient-bracketing.png`, `audit/300dpi/p021-no-ghost-quotient.png` (commit `d584603ba0a48df7d6bad28de0e2ea1b17851bf1`).
- Added with this final audit receipt: `audit/300dpi/p007-gamma-plus.png`, `p010-gamma-plus.png`, `p031-group-plus.png`, `p031-n2-condition.png`, `p033-group-plus.png`, `p033-lemma-heading.png`, and `p038-epsilon.png`.

### Remaining scope conflict and candidate boundary

- The direct PDF `pdfinfo` result and MinerU `structured_content.json` each report 41 pages; root `README.md` still calls this PDF 44 pages. This contributor leaves the root asset map for the canonical integrator to reconcile.
- This is a peer candidate at base `e04c4a9603818cfa2d71271942f696115783c33b`, not canonical project state. Root `AUDIT-INDEX.md`, root `AUDIT-PROGRESS.log`, root `README.md`, and root `MEMORY.md` were not changed; no push or integration was performed.
