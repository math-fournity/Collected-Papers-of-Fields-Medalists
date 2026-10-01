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

### p.009 (PDF p.9 / print p.287)

- PNG: `audit/p009.png` (150-dpi `pngmono`); 300-dpi crops: `audit/300dpi/p009-complex-line.png`, `audit/300dpi/p009-harmonic-equality.png`
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:04:36 EDT
- Markdown segment: lines 299–327, from “We discuss first the reducible connections...” through the closing one-dimensional stabiliser criterion.
- Compared: reducibility criteria; splitting `E=L⊕L⁻¹`; Chern-class formula; count `n(Q)`; stabiliser action; harmonic-space vanishing and final converse.
- Result: **FAIL**. Markdown line 305 says “complex lie bundles”; the print reads “complex line bundles”. The 300-dpi phrase crop confirms the missing `n`, which changes the mathematical term. The harmonic equality `H¹(X;R)=𝒦⁻²(X)=0` also matches the print in its 300-dpi crop. The remaining checked formulas and prose match; the running header and folio `287` are absent.

### p.010 (PDF p.10 / print p.288)

- PNG: `audit/p010.png` (150-dpi `pngmono`); notation crop: `audit/300dpi/p010-norms.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:06:10 EDT
- Markdown segment: lines 329–372, from Theorem 6 through the definition of the smooth map `S(A+a,g)`.
- Compared: Theorem 6 local quotient statements; slice norm and group-action formulas; factorisation `g=γ\tilde g`; Sobolev estimate; proof of Hausdorffness and the map `S`.
- Result: **PASS±**. The mathematical statements and formulas match. The print says “a principle `𝒢/±1` bundle” (rather than “principal”); Markdown preserves the source wording. The prime after `L_3^2` in the norm of `b` is visible on the 300-dpi crop and is also preserved. The running author header and folio `288` are omitted.

### p.011 (PDF p.11 / print p.289)

- PNG: `audit/p011.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:07:45 EDT
- Markdown segment: lines 375–413, from the derivative of `S` through the Fredholm-operator discussion ending “compact manifolds are”.
- Compared: derivative and isomorphism claim; reducible-connection restriction and local quotient model; section II.2 map `Φ`; derivative of `Φ` and Fredholm statement.
- Result: **PASS±**. The equations, spaces, and prose match the page image. The Markdown omits the running header and printed folio `289`.

### p.012 (PDF p.12 / print p.290)

- PNG: `audit/p012.png` (150-dpi `pngmono`); notation crop: `audit/300dpi/p012-restriction.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:09:28 EDT
- Markdown segment: lines 415–459, from the Fredholm-index discussion through the regular-value sentence ending “for the”.
- Compared: index formula and dimension 5/6 conclusion; Lemma 7 statement and decomposition; proof construction of `\psi` and its inverse relation.
- Result: **FAIL**. Markdown line 443 gives `L|_E : E' → Im L`; the printed page has `L|_{E'} : E' → Im L`. The 300-dpi crop confirms the prime on the restriction domain, which is essential to the stated inverse. The remaining checked formulas and prose match; the running header and folio `290` are absent.

### p.013 (PDF p.13 / print p.291)

- PNG: `audit/p013.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:10:12 EDT
- Markdown segment: lines 461–491, from the finite-dimensional regular-value continuation through “The allowable perturbations σ are to”.
- Compared: Proposition 8 irreducible/reducible local models and dimensions; harmonic-space regularity interpretation; beginning of section II.3 and perturbation-bundle setup.
- Result: **PASS±**. The formulas and substantive statements match the page image. Markdown lines 468 and 474 split the printed conjunction “and” into `a n d` inside the two dimension clauses; this is a readability/formatting artifact with the numbers intact and is a candidate for post-audit Edit repair. The running author header and folio `291` are absent from the Markdown.
- Supplemental check: 2026-10-01 16:11:42 EDT; PDF p.13 image `audit/p013.png` shows ordinary “and” in both clauses. No 300-dpi crop was needed because the letter spacing, rather than a glyph identity, is the discrepancy.

### p.014 (PDF p.14 / print p.292)

- PNG: `audit/p014.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:12:24 EDT
- Markdown segment: lines 493–533, from “be smooth sections of `𝔖³`...” through the start of the three-open-sets argument ending “by applying”.
- Compared: perturbation norm and derivative setup; equivariant finite-dimensional perturbation near reducible connections; `\tilde Φ` replacement; Lemma 9 transversality statement and density setup.
- Result: **PASS±**. The mathematical content and displayed equations match the page image. The running author header and folio `292` are absent from the Markdown.

### p.015 (PDF p.15 / print p.293)

- PNG: `audit/p015.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:14:13 EDT
- Markdown segment: lines 535–567, from the end of the three-open-sets argument through the footnote on the smooth density of smooth connections.
- Compared: conclusion of Lemma 9; compactness/transversality proof; the KO-index family setup; the page's complete footnote.
- Result: **PASS±**. Mathematical statements and formulas match. Before the complete footnote, Markdown contains two extra page-footnote fragments, `$T_{A,\varepsilon}$` and `Q.` (lines 563–565); the page image has only the single integrated note, which is retained at line 567. These fragments add OCR clutter but do not remove the source note; they are candidates for post-audit cleanup. The running author header and folio `293` are absent.

### p.016 (PDF p.16 / print p.294)

- PNG: `audit/p016.png` (150-dpi `pngmono`); notation crop: `audit/300dpi/p016-exterior-power.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:15:04 EDT
- Markdown segment: lines 569–626, from the continuation of the KO-index property through Lemma 10's vanishing statement.
- Compared: restricted gauge group and associated bundles; family operator; fibration/orientability argument; `w₁` index class; homotopy of Fredholm operators; Lemma 10 statement.
- Result: **PASS±**. The formulas and mathematical statements match. The 300-dpi crop confirms the bundle term `λ²(T*X)` as transcribed. At Markdown line 575 the print has a period after `P_{x₀}`, while Markdown uses a comma before “Then”; this punctuation difference does not change the claim. The running author header and folio `294` are absent.

### p.017 (PDF p.17 / print p.295)

- PNG: `audit/p017.png` (150-dpi `pngmono`); formula crop: `audit/300dpi/p017-restriction-class.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:17:11 EDT
- Markdown segment: lines 629–671, from Lemma 10's proof through note (iii), ending “for any”.
- Compared: stable-range claim; restricted-adjoint representation; KO-class restriction; simple-connectedness reduction to `π₄(SU(n))`; notes (i)–(iii).
- Result: **FAIL**. Markdown line 655 omits the printed connective “to” between `H¹(\hat B(M,3,k); Z/2)` and `H¹(\hat B(M,2,k); Z/2)`, and concatenates the second group immediately after a `$$` delimiter. The 300-dpi crop confirms the complete source relation. The other checked statements match; the running author header and folio `295` are absent.

### p.018 (PDF p.18 / print p.296)

- PNG: `audit/p018.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:18:27 EDT
- Markdown segment: lines 673–707, from the continuation “spin manifold...” through Proposition 12's gauge condition and Sobolev estimate.
- Compared: end of note (iii); Theorem 11 and section III outline; Proposition 12 assumptions, energy bound, convergence conclusion, and conditions (i)–(ii).
- Result: **PASS±**. The statements and displayed equations match the page image. The running author header and folio `296` are absent from the Markdown.

### p.019 (PDF p.19 / print p.297)

- PNG: `audit/p019.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:19:24 EDT
- Markdown segment: lines 709–756, from the elliptic-system conclusion through the first bound `I(q,i) ≤ L` in the proof of Lemma 14.
- Compared: self-duality equation and elliptic-system claim; Theorem 13 alternatives; Lemma 14 hypotheses, covering property, and page-end integral bound.
- Result: **PASS±**. The mathematical statements and displayed formulas match the page image. The running author header and folio `297` are absent from the Markdown.

### p.020 (PDF p.20 / print p.298)

- PNG: `audit/p020.png` (150-dpi `pngmono`); notation crop: `audit/300dpi/p020-big-O.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:21:32 EDT
- Markdown segment: lines 759–801, from the diagonal-subsequence argument through the convergence over the conformal-chart cover.
- Compared: end of Lemma 14 proof; geodesic-coordinate expansion; rescaled metric and chart; action-density bound and conformal-chart convergence.
- Result: **FAIL**. In the coordinate and rescaled-metric formulas, Markdown uses digit `0` where the printed page has big-O `O`: lines 778 (`0|x|²`), 787 (`r²0|y|²`), and 787 (`0(r²)`). The 300-dpi crop confirms the order-symbol reading; all three positions are repair candidates. The other checked material matches; the running author header and folio `298` are absent.

### p.021 (PDF p.21 / print p.299)

- PNG: `audit/p021.png` (150-dpi `pngmono`); 300-dpi crops: `audit/300dpi/p021-points.png`, `audit/300dpi/p021-compatability.png`
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:24:41 EDT
- Markdown segment: lines 803–845, from the local connection matrices and transition law through the two alternatives in Theorem 13.
- Compared: transition-function compatibility equation; energy bounds (2) and (3); bundle extensions and limit maps; final `l=0`/`l=1` cases.
- Result: **PASS±**. The equations and main argument match. Markdown line 809 reads `comptatability`; the printed word is `compatability` (the source's own misspelling), confirmed in the 300-dpi crop. This is a minor OCR spelling difference and a candidate for Edit repair to match print. The print refers to “strict inequality in (3) above” before displaying (3); Markdown preserves that source quirk. The point set in Markdown line 829 is `κ₁,…,κ_l`, matching the printed crop, while the immediately preceding discussion uses `x_j`; this source-level inconsistency is recorded without normalization. The running author header and folio `299` are absent.

### p.022 (PDF p.22 / print p.300)

- PNG: `audit/p022.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:25:41 EDT
- Markdown segment: lines 847–889, from section III.3 through Definition 15(b)'s formula for `λ(A)`.
- Compared: moduli-space map; smoothed radius/position definition; bump-function scale; instanton action density and `R_I`; both properties and Definition 15.
- Result: **PASS±**. The mathematical statements and displayed formulas match the page image. The running author header and folio `300` are absent from the Markdown.

### p.023 (PDF p.23 / print p.301)

- PNG: `audit/p023.png` (150-dpi `pngmono`)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:26:34 EDT
- Markdown segment: lines 891–921, from the interpretation of `λ(A)` through Theorem 16's convergence proof and appendix pointer.
- Compared: conformal-chart map; rescaled metric; Theorem 16(i)–(ii) and curvature bound; instanton action estimate and subsequence argument.
- Result: **PASS±**. The definitions, formulas, and proof statements match the page image. The running author header and folio `301` are absent from the Markdown.

### p.024 (PDF p.24 / print p.302)

- PNG: `audit/p024.png` (150-dpi `pngmono`); notation crop: `audit/300dpi/p024-derivative-constant.png` (300-dpi page crop)
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:28:12 EDT
- Markdown segment: lines 923–955, Corollary 17 and its proof through the compact-complement statement.
- Compared: `p` parameterisation; derivative bound; uniqueness/smoothness proof; derivative estimates for `λ` and `x`; compactness conclusion.
- Result: **PASS±**. The formulas and prose match. In the derivative formula the print uses lowercase `k` in `k^{-1}` and `β_k`, as does Markdown; earlier Definition 15 uses uppercase `K` for the instanton minimum. This source-level notation inconsistency is preserved. The running author header and folio `302` are absent.

### p.025 (PDF p.25 / print p.303)

- PNG: `audit/p025.png` (150-dpi `pngmono`); 300-dpi crops: `audit/300dpi/p025-norm-squares.png`, `audit/300dpi/p025-vector-field.png`
- Actor / model / effort: `Peer-P03` / `gpt-6-luna` / `max`
- Checked at: 2026-10-01 16:31:26 EDT
- Markdown segment: lines 957–1006, from Proposition 18 through the vector-field definition in the proof of Theorem 19.
- Compared: Proposition 18(i)–(iii); eigenvalue and Sobolev estimates; Theorem 19 covering-map argument; tangent-space map and inequality (1); vector field defining `α`.
- Result: **FAIL**. Markdown line 967 omits the outer square on all three printed `L²` norms in the eigenvalue/Rayleigh inequalities. The 300-dpi crop confirms `\|d_A^*ω\|_{L²}²=μ(A)` and `\|d_θ^*ω'\|_{L²}²≥μ₁\|ω'\|_{L²}²`. Markdown line 1006 uses Greek `ν^i`; the 300-dpi print shows Latin `v^i`, matching the parameter `ξ=(v^i,φ)`. Both errors are repair candidates. The other checked content matches; the running author header and folio `303` are absent.
