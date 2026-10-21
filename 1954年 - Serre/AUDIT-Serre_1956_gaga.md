<!-- actor=Peer-P09; model=gpt-6-luna; effort=max -->
# Serre 1956 — Géométrie algébrique et géométrie analytique

## Candidate identity and evidence

- Status: CANDIDATE_NOT_CURRENT; contributor=Peer-P09; canonical integrator=Master-Luna.
- Source base: `e04c4a9603818cfa2d71271942f696115783c33b`; integration target observed at start: `3dfa4a648c3b456057db96c5f6eece204e5bb1dd`.
- PDF: `1954年 - Serre/Serre_1956_gaga.pdf`; SHA-256 `9898f985dd6932496e26450bfe0beca8655a937032f545b97cebd88d1bc8eb98`; 43 PDF pages.
- MinerU Markdown: `1954年 - Serre/Serre_1956_gaga_mineru/Serre_1956_gaga__Serre_1956_gaga.md`; source SHA-256 `82ded987cca1b0e03fe200a8059cd17b7e86d9a42b86f222f205a1c4a2a4b339`; source commit `4e5d9aabe1bc05fbb69fe4f77c0e692470fd9935`.
- Text mode: born-digital. `pdfinfo` reports Producer `pdfTeX-1.40.16`; UTF-8 `pdftotext -layout` yields 87,978 bytes across 43 nonempty pages and 0 U+FFFD. PDF p.1 is the unnumbered journal cover; PDF p.2–43 are print pages 1–42.
- Existing export metadata: MinerU 3.4.4, 43 structured pages. A `doc_id` field is absent from the tracked `structured_content.json` and `middle_json.json`; no value is inferred.
- Review route: full PDF text-layer to MinerU Markdown page-by-page reconciliation; visual whole-page samples at the title page and two dense mathematical pages; glyph ambiguities, if found, require a committed 300 dpi crop. Text-layer absence is not treated as proof that a printed symbol is absent.
- The per-page records below identify the AI actor, model, and effort. Each page commit preserves its audit record and the page evidence available at that point; two supplementary 300 dpi crops found necessary during final readback are included with this closeout. Root progress/index files remain owned by the canonical integrator.

## Page records

### PDF p.001/43 — journal cover (unnumbered)

- Reviewed: 2026-10-01 15:54 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: PDF text layer page 1 compared with MinerU Markdown lines 1–13 (author, article title, AIF volume/year/pages and Numdam URL, copyright/archive terms, Numdam digitization notice).
- Result: PASS±. Bibliographic identity and copyright/archive content are present and consistent. The print's letter-spaced Annales masthead is not separately reproduced as a display line; the journal remains explicitly named in the citation and copyright text. This is a presentation omission, not a misleading bibliographic difference.
- Image: not individually rendered under the born-digital sample route; no glyph-level uncertainty on this cover page.

### PDF p.002/43 — print p.1 (title page and Introduction)

- Reviewed: 2026-10-01 15:56 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [150 dpi full page](audit/Serre_1956_gaga_p002_150dpi.png); [300 dpi name crop](audit/300dpi/Serre_1956_gaga_p002_chow_300dpi.png); PDF text layer compared with MinerU Markdown lines 15–25.
- Checked: article title and author; opening Introduction through the sentence continued on PDF p.3; theorem-of-Chow sentence.
- Result: FAIL. The print and PDF text layer read “CHOW” (300 dpi crop confirms the letters); Markdown line 23 reads “CNow”. The title, author, and remaining checked prose agree. Defer the single Markdown correction until all 43 PDF pages have been audited.

### PDF p.003/43 — print p.2

- Reviewed: 2026-10-01 15:59 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [150 dpi page](audit/Serre_1956_gaga_p003_150dpi.png); [300 dpi local-ring crop](audit/300dpi/Serre_1956_gaga_p003_local-rings_300dpi.png); PDF text layer compared with MinerU Markdown lines 27–35.
- Checked: Introduction continuation, the statements about coherent sheaves and cohomology, the local-ring comparison, cited authors, applications paragraph, and footnote (1).
- Result: PASS±. The content and footnote agree. PDF text extraction mangles the local-ring glyphs, while the 300 dpi crop confirms the printed O_x and H_x notation represented by Markdown as \mathcal{O}_x and \mathcal{H}_x. The running author and print page number are not represented in the Markdown.

### PDF p.004/43 — print p.3

- Reviewed: 2026-10-01 16:03 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [150 dpi page](audit/Serre_1956_gaga_p004_150dpi.png); [300 dpi inequality crop](audit/300dpi/Serre_1956_gaga_p004_geq_300dpi.png); PDF text layer and MinerU Markdown lines 37–55.
- Checked: end of Introduction, section/paragraph headings, definition of analytic subsets, and the restriction-map/faisceau notation through the definition of holomorphic maps.
- Result: PASS±. Checked prose and notation agree. The PDF text layer flattens the first bound to “n ^ 0”; the print crop confirms “n ≥ 0”, matching Markdown line 43. The running title and print page number are not represented in Markdown.

### PDF p.005/43 — print p.4

- Reviewed: 2026-10-01 16:04 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi sheaf-label crop](audit/300dpi/Serre_1956_gaga_p005_HV_300dpi.png); PDF text layer and MinerU Markdown lines 57–77.
- Checked: continuation of the holomorphic-map definition, analytic isomorphism criterion, product construction, Definition 1 and axioms (H1) and (HII).
- Result: FAIL. In the print, the isomorphism criterion says the morphism transforms the sheaf H_U into H_V. The 300 dpi crop confirms V; Markdown line 59 instead has \mathcal{H}_{\backslash}. Defer correction until the full PDF audit is complete. The remaining checked statements and formulas agree; the running author is omitted from Markdown.

### PDF p.006/43 — print p.5

- Reviewed: 2026-10-01 16:06 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [150 dpi page](audit/Serre_1956_gaga_p006_150dpi.png); [300 dpi subscript crop](audit/300dpi/Serre_1956_gaga_p006_AxY_300dpi.png); PDF text layer and MinerU Markdown lines 79–91.
- Checked: analytic-space product construction, analytic sheaf definitions and quotient, and Proposition 1(a)–(b).
- Result: FAIL. In the definition of A_x(Y), the print has f in H_{x,X}; the 300 dpi crop confirms subscript X. Markdown line 87 has H_{x,Y}. Defer the correction until all 43 pages have been audited. Other checked statements agree; the running title and print page number are omitted from Markdown.

### PDF p.007/43 — print p.6

- Reviewed: 2026-10-01 16:08 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [150 dpi page](audit/Serre_1956_gaga_p007_150dpi.png); [300 dpi series and prime-ideal crop](audit/300dpi/Serre_1956_gaga_p007_series-primes_300dpi.png); PDF text layer and MinerU Markdown lines 93–107.
- Checked: coherent-sheaf argument, local analytic ring description, convergent power-series algebras and quotient, regular-local criterion, and the minimal-prime intersection display.
- Result: FAIL. The print has C{z_1,...,z_n} for both power-series terms in this passage; the 300 dpi crop confirms subscript 1. Markdown line 99 has z_i in both places. The displayed 0 = intersection p_i agrees. Defer the two subscript corrections until the full audit is complete.

### PDF p.008/43 — print p.7

- Reviewed: 2026-10-01 16:09 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi series and Zariski crop](audit/300dpi/Serre_1956_gaga_p008_Zariski-series_300dpi.png); PDF text layer and MinerU Markdown lines 109–125.
- Checked: irreducible-component/local-dimension argument, finite extension of the convergent-series algebra, Zariski/usual topology distinction, and Lemma 1(a)–(d).
- Result: FAIL. The print has C{z_1,...,z_r} in the finite-extension clause; the crop confirms subscript 1. Markdown line 109 has z_i. The same line's formal-series completion and the Z-topology statements agree with print. Defer correction until the full audit is complete.

### PDF p.009/43 — print p.8

- Reviewed: 2026-10-01 16:11 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi transition-map crop](audit/300dpi/Serre_1956_gaga_p009_transition-map_300dpi.png); PDF text layer and MinerU Markdown lines 127–143.
- Checked: proof of Lemma 1(a)–(d), setup of the analytic structure on an algebraic variety, Proposition 2, and the transition-map paragraph.
- Result: PASS±. The checked statements agree. The print and Markdown both show a colon after V' before the arrow in the transition-map notation; the crop confirms it is a print quirk, so it is preserved. The running author is not represented in Markdown.

### PDF p.010/43 — print p.9

- Reviewed: 2026-10-01 16:13 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi ring-label crop](audit/300dpi/Serre_1956_gaga_p010_ring-label_300dpi.png); [300 dpi theta-map crop](audit/300dpi/Serre_1956_gaga_p010_theta_300dpi.png); [300 dpi Proposition 3 crop](audit/300dpi/Serre_1956_gaga_p010_hat-theta_300dpi.png); [300 dpi ideal-J crop](audit/300dpi/Serre_1956_gaga_p010_ideal-J_300dpi.png); PDF text layer and MinerU Markdown lines 143–164.
- Checked: direct definition of the analytic structure, X^h properties, local-ring comparison, the homomorphism and its completion, Proposition 3, and the ideal J_x(Y) setup.
- Result: FAIL. The print uses H_{x,X} and O_{x,X} in the direct-definition sentence; the crop confirms uppercase X, while Markdown line 145 uses lowercase x in both subscripts. Proposition 3 prints the completed map with theta; the crop confirms it matches the preceding theta map, while Markdown line 159 has zero. Defer both corrections until the full audit is complete.

### PDF p.011/43 — print p.10

- Reviewed: 2026-10-01 16:15 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi Proposition 4 and formal-series crop](audit/300dpi/Serre_1956_gaga_p011_prop4-formal-powers_300dpi.png); [300 dpi J-ideal crop](audit/300dpi/Serre_1956_gaga_p011_J-ideal_300dpi.png); PDF text layer and MinerU Markdown lines 164–180.
- Checked: Proposition 4, the affine-space formal-series case, the Nullstellensatz exponent, ideal products/intersections, and the quotient argument for Propositions 3 and 4.
- Result: FAIL. The print has theta in the generator statement, C[[z_1,...,z_n]] for formal power series, and f^r with r ≥ 0. The crops also show theta in “au moyen de theta” and J_x(Y) in the definition continuation and both completed-ideal terms; the audited Markdown instead had zero in that phrase and I_x(Y) in those three places. All identified differences are repaired in the final Markdown; see the closeout register.

### PDF p.012/43 — print p.11

- Reviewed: 2026-10-01 16:16 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: PDF text layer compared page-by-page with MinerU Markdown lines 182–204.
- Checked: completion of Proposition 4, injectivity/corollaries 1–3, the Zariski-density proposition and its remark.
- Result: PASS±. The checked assertions and notation agree; no distinct glyph-level discrepancy was found on this page. The running title and print page number are not represented in Markdown.
- Image: no per-page image; born-digital text layer is primary on this page, with separate 300 dpi adjudication reserved for unresolved glyph discrepancies.

### PDF p.013/43 — print p.12

- Reviewed: 2026-10-01 16:17 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: PDF text layer compared page-by-page with MinerU Markdown lines 206–220.
- Checked: Proposition 6, Chow's projective-cover argument, Lemma 2 on dense images, irreducible-component indexing, and the opening of Proposition 7.
- Result: PASS±. The checked prose, propositions and set-map notation agree. The running author and print page number are not represented in Markdown.
- Image: no per-page image; born-digital text-layer review found no separate glyph-level discrepancy requiring a crop.

### PDF p.014/43 — print p.13

- Reviewed: 2026-10-01 16:18 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi local-map crop](audit/300dpi/Serre_1956_gaga_p014_local-map_300dpi.png); PDF text layer and MinerU Markdown lines 226–244.
- Checked: end of Proposition 7, Propositions 8 and 9, the local-ring sheaf map induced by p, and footnote (2).
- Result: FAIL. The print says p transforms the sheaf O_X into O_T, while Markdown line 236 has O_x. The printed homomorphism is O_{x,X} → O_{t,T}; the crop confirms uppercase X, while Markdown line 239 uses lowercase x in the second subscript. Defer both corrections until the full audit is complete.

### PDF p.015/43 — print p.14

- Reviewed: 2026-10-01 16:21 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi local-ring and ideal crop](audit/300dpi/Serre_1956_gaga_p015_local-rings-ideals_300dpi.png); PDF text layer and MinerU Markdown lines 246–256.
- Checked: local-ring embeddings A, A', B and B', irreducible-component ideals, quotient rings, total fraction rings, the birationality argument and footnote (3).
- Result: FAIL. The print uses O_{x,X} and H_{x,X}; the crop confirms uppercase X, while Markdown line 246 has lowercase x as the second subscript in both labels. Markdown later renders the defined prime ideals in regular italic p_i where print uses fraktur; this is a non-misleading Fraktur loss, recorded as PASS±. Defer the case corrections until the full audit is complete.

### PDF p.016/43 — print p.15

- Reviewed: 2026-10-01 16:22 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: PDF text layer compared page-by-page with MinerU Markdown lines 258–278.
- Checked: conclusion of the birationality argument, Lemma 3, minimal primes and localization, the canonical product homomorphism, and the congruence elements proving surjectivity.
- Result: PASS±. The statements, exponent/prime labels, product map, and congruences agree. Markdown renders the defined fraktur prime ideals as regular italic p_i in some later prose; the referent is unchanged. The running title and print page number are not represented in Markdown.
- Image: no per-page image; this born-digital page showed no distinct glyph discrepancy requiring a crop.

### PDF p.017/43 — print p.16

- Reviewed: 2026-10-01 16:23 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi associated-sheaf crop](audit/300dpi/Serre_1956_gaga_p017_tensor_300dpi.png); PDF text layer and MinerU Markdown lines 284–308.
- Checked: associated topology F', analytic sheaf definition, tensor formula, scalar ring, canonical map, and extension of homomorphisms.
- Result: PASS±. The displayed print formula has no tensor subscript; the following print sentence specifies that the product is over O'. Markdown preserves the same equation and explicit scalar-ring sentence. No content difference was found in the checked maps.

### PDF p.018/43 — print p.17

- Reviewed: 2026-10-01 16:25 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi exact-sequence prose crop](audit/300dpi/Serre_1956_gaga_p018_prime-prose_300dpi.png); [300 dpi exact-sequence formula crop](audit/300dpi/Serre_1956_gaga_p018_exact-sequence_300dpi.png); PDF text layer and MinerU Markdown lines 311–347.
- Checked: Proposition 10(a)–(c), the primed pullback sequence and tensor sequence, local presentations of coherent sheaves, and the opening setup for Proposition 11.
- Result: FAIL. In the prose sequence after “il en est évidemment de même,” the print has F_1' → F_2' → F_3'. The first crop confirms the prime on F_3'; Markdown line 319 omits it. The displayed tensor sequence on line 322 has the prime on all three terms and agrees with print.

### PDF p.019/43 — print p.18

- Reviewed: 2026-10-01 16:26 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi localization and tensor crop](audit/300dpi/Serre_1956_gaga_p019_localization-tensor_300dpi.png); PDF text layer and MinerU Markdown lines 347–371.
- Checked: Proposition 11, local ring labels A/A'/B/B'/E, the two associated-sheaf stalks, the quotient/base-change identity, and the canonical tensor-product isomorphism.
- Result: FAIL. The print labels the rings with second subscripts X and Y (O_{x,X}, O_{x,Y}, H_{x,X}, H_{x,Y}); Markdown line 354 uses lowercase x and y. The print also has B' = B/aB with an unaccented ideal symbol, while Markdown line 363 reads B/àB. The displayed tensor-product subscripts on line 360 agree with print.

### PDF p.020/43 — print p.19

- Reviewed: 2026-10-01 16:28 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi cohomology-diagram crop](audit/300dpi/Serre_1956_gaga_p020_cohomology-diagram_300dpi.png); [300 dpi Theorem 1–2 crop](audit/300dpi/Serre_1956_gaga_p020_theorem1_300dpi.png); PDF text layer and MinerU Markdown lines 395–435.
- Checked: induced cohomology maps, the connecting-homomorphism diagram, its coherent-sheaf condition, projective-space setup, and Theorems 1–2.
- Result: FAIL. The print says “where the sheaf C is coherent” (the sheaf \mathcal C from the exact sequence); Markdown line 413 has “où le faisceau à est cohérent.” The diagrams and theorem statements otherwise agree, including q ≥ 0.

### PDF p.021/43 — print p.20

- Reviewed: 2026-10-01 16:31 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi remark 2 crop](audit/300dpi/Serre_1956_gaga_p021_remark2_300dpi.png); [300 dpi Theorem 1 crop](audit/300dpi/Serre_1956_gaga_p021_theorem1_300dpi.png); [300 dpi constant-sheaf crop](audit/300dpi/Serre_1956_gaga_p021_constant-sheaf_300dpi.png); PDF text layer and MinerU Markdown lines 437–469.
- Checked: Theorem 3, both remarks, the factorization of epsilon, the constant rational-function sheaf example, Theorem 1 and Lemma 4.
- Result: PASS±. The crops confirm the factorization targets F' before F^h, the negative question concerns the F' map, the printed constant-sheaf term is K without a prime, and Theorem 1 uses q ≥ 0. These forms agree with Markdown; no content difference was found on this page.

### PDF p.022/43 — print p.21

- Reviewed: 2026-10-01 16:32 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi recurrence and q-bound crop](audit/300dpi/Serre_1956_gaga_p022_recurrence_300dpi.png); PDF text layer and MinerU Markdown lines 469–505.
- Checked: Lemmas 4 and 5, hyperplane exact sequences, the cohomology diagram, the five-lemma induction, the q-bound, and footnote (4).
- Result: PASS±. The print crop confirms the comparison map is bijective for q ≥ 0; the PDF text layer flattens that glyph to “> 0,” while Markdown has ≥. The remaining checked sequences and footnote agree; the running title/page number are omitted from Markdown.

### PDF p.023/43 — print p.22

- Reviewed: 2026-10-01 16:35 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi five-lemma diagram crop](audit/300dpi/Serre_1956_gaga_p023_five-lemma_300dpi.png); [300 dpi Lemma 6 crop](audit/300dpi/Serre_1956_gaga_p023_lemma6_300dpi.png); PDF text layer and MinerU Markdown lines 499–548.
- Checked: the direct-sum resolution by O(n), the long cohomology diagram and epsilon indices, the five-lemma argument, and Lemma 6's Hom/tensor comparison.
- Result: FAIL. The print says L is a direct sum of sheaves isomorphic to O(n); Markdown line 507 has L(n). The print diagram has five columns and maps epsilon_1 through epsilon_5, ending with H^{q+1}(X,L); Markdown line 512 omits that final column and epsilon_5. The prose afterward names epsilon_5, confirming the diagram omission.

### PDF p.024/43 — print p.23

- Reviewed: 2026-10-01 16:37 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi Theorem 2 Hom-map crop](audit/300dpi/Serre_1956_gaga_p024_hom-maps_300dpi.png); [300 dpi Theorem 3 extension-by-zero crop](audit/300dpi/Serre_1956_gaga_p024_extension-zero_300dpi.png); PDF text layer and MinerU Markdown lines 548–574.
- Checked: composition proving Theorem 2, kernel/cokernel uniqueness proof, and the reduction of Theorem 3 existence to projective space by extension by zero.
- Result: FAIL. The print's first Hom section is H^0(X,A), but Markdown line 554 has X^h. In the existence reduction, print uses M^X, f in the ideal sheaf I, and the stalk G_x^h = M_x^X; Markdown line 572 instead has M^x, J_x, G_{fx}^h, and M_x^x. The print also has I·G = 0 and M^X at the end of this passage, while line 574 has J·G and M_b^X. The crops confirm these object and case differences. Defer correction until the full audit is complete.

### PDF p.025/43 — print p.24

- Reviewed: 2026-10-01 16:39 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi twist-transition crop](audit/300dpi/Serre_1956_gaga_p025_twist-transition_300dpi.png); [300 dpi Lemma 8 crop](audit/300dpi/Serre_1956_gaga_p025_lemma8_300dpi.png); PDF text layer and MinerU Markdown lines 574–592.
- Checked: closing restriction step of the extension-by-zero argument, definition of M(n) and its transition maps, Lemma 7, and Lemma 8's global-generation bound.
- Result: FAIL. The print's closing phrase is that F^h is isomorphic to M, with no subscript on M; Markdown line 574 has M_b^X. The 300 dpi crop confirms the print. The twist t_j^n/t_i^n and Lemma 8 bound/generation statement otherwise agree.

### PDF p.026/43 — print p.25

- Reviewed: 2026-10-01 16:42 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [150 dpi full page](audit/Serre_1956_gaga_p026_150dpi.png); [300 dpi tensor-sequence crop](audit/300dpi/Serre_1956_gaga_p026_tensor-sequence_300dpi.png); [300 dpi equations (1)–(4) crop](audit/300dpi/Serre_1956_gaga_p026_equations1-4_300dpi.png); PDF text layer and MinerU Markdown lines 594–635.
- Checked: generation by global sections, hyperplane ideal sequence, tensoring by M, Tor_1 identification, and equations (1)–(4).
- Result: FAIL. The print identifies the hyperplane ideal as A(E), but line 602 has b(E). In the tensor sequence and its explanation, print uses M throughout; lines 613 and 616 instead use A in the tensor factors, target and Tor_1 arguments. Equation (2) prints M(n−1) → M(n), while line 625 has 1_0(n−1) → 1_0(n). The print has distinct exact sequences (3) and (4): line 630 contains only the bare label (3), and line 633 labels a corrupted copy of sequence (3) as (4), omitting the printed sequence (4) altogether. A full-page reread also showed that an extra untagged duplicate of sequence (4) later in the Markdown has no counterpart on the printed page; it was removed. Both crops confirm the displayed sequences and the extra display is absent from the full-page source. All differences are repaired in the final Markdown; see the closeout register.

### PDF p.027/43 — print p.26

- Reviewed: 2026-10-01 16:46 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi sequences (5)–(8) crop](audit/300dpi/Serre_1956_gaga_p027_sequences5-8_300dpi.png); [300 dpi equations (5)–(9) crop](audit/300dpi/Serre_1956_gaga_p027_equations5-9_300dpi.png); [300 dpi Theorem A tail crop](audit/300dpi/Serre_1956_gaga_p027_theorem-A_300dpi.png); PDF text layer and MinerU Markdown lines 636–670.
- Checked: exact cohomology sequences (5)–(6), vanishing and dimension inequalities (7)–(8), surjectivity (9), the global-generation step, and footnote (5).
- Result: FAIL. In (5), print has M(n−1) and L_n; line 643 has N(n−1) and X_n. In (7), print has L_n between the two M terms; line 653 has P_n. The dimension function in line 656 uses ℓ(n) instead of M(n). In (8), print uses H^1 and starts with M(n−1); line 659 has prime superscripts and M(n). The map after (8) in line 662 uses P_n where print has L_n. The footnote marker at line 662 is also (5), not the corrupted placeholder in Markdown. Equation (9) and the checked global-generation conclusion agree. All listed transcription differences are repaired in the final Markdown; see the closeout register.

### PDF p.028/43 — print p.27

- Reviewed: 2026-10-01 16:48 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi Theorem 3 resolution-proof crop](audit/300dpi/Serre_1956_gaga_p028_resolution-proof_300dpi.png); PDF text layer and MinerU Markdown lines 672–710.
- Checked: conclusion of Lemma 8, construction by successive coherent quotients, the exact sequences for Theorem 3 existence, and the opening of the Betti-number application.
- Result: FAIL. The print's first and final exact sequences contain the sheaf M; Markdown lines 679 and 702 instead have the garbled symbol “A b”. The print names the constructed algebraic sheaf L_1, while Markdown line 684 has L_i; the 300 dpi crop confirms numeral 1. The remaining checked maps and the homogeneous-coordinate list agree.

### PDF p.029/43 — print p.28

- Reviewed: 2026-10-01 16:50 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi sigma-action crop](audit/300dpi/Serre_1956_gaga_p029_sigma-action_300dpi.png); [300 dpi cohomology-map crop](audit/300dpi/Serre_1956_gaga_p029_cohomology-map_300dpi.png); PDF text layer and MinerU Markdown lines 708–740.
- Checked: conjugation of projective points and subvarieties, Proposition 12, Dolbeault sums, the induced semi-linear cohomology maps, and Weil's corollary.
- Result: FAIL. The print denotes the transformed variety by X^sigma; Markdown line 712 has X^circ. In the cohomology-map chain, the print's source is H^q(U, Omega^p(X)), while Markdown line 734 has Omega^p(X^sigma) on the source side. The remaining checked sums and statements agree.

### PDF p.030/43 — print p.29

- Reviewed: 2026-10-01 16:51 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi Chow Proposition 13 crop](audit/300dpi/Serre_1956_gaga_p030_chow-prop13_300dpi.png); PDF text layer and MinerU Markdown lines 742–758.
- Checked: transformation remark, Proposition 13 and its support argument, Proposition 14's compact analytic subset, and Proposition 15's statement.
- Result: PASS±. The print spells the Proposition 13 noun “sous-ense.nble” with a visible intrusive period; the 300 dpi crop confirms the print quirk and Markdown preserves it. No correction is warranted. Other checked statements agree.

### PDF p.031/43 — print p.30

- Reviewed: 2026-10-01 16:53 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi H^0/H^1 crop](audit/300dpi/Serre_1956_gaga_p031_H0-H1_300dpi.png); PDF text layer and MinerU Markdown lines 760–782.
- Checked: the end of Proposition 15, Corollary, section on algebraic/analytic principal bundles, nonabelian H^0/H^1 notation, and Proposition 16.
- Result: FAIL. The print defines the group H^0(X,A) and the pointed set H^1(X,A); the crop confirms superscript zero. Markdown line 768 has H^6(X,A). The subsequent H^1 classifications and Proposition 16 statement agree.

### PDF p.032/43 — print p.31

- Reviewed: 2026-10-01 17:44 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi group-action crop](audit/300dpi/Serre_1956_gaga_p032_group-action_300dpi.png); [300 dpi H^1 and vector-sheaf crop](audit/300dpi/Serre_1956_gaga_p032_H1-vector-sheaf_300dpi.png); PDF text layer and MinerU Markdown lines 784–802.
- Checked: the G×G action on G, Proposition 16 proof, nonabelian H^0/H^1 notation, and Propositions 17–18.
- Result: FAIL. The print action is (g,g')·h = g h g'^{-1}; Markdown line 787 has g h g^{-1}. The print uses H^1(X,G) and H^1(X^h,G^h); Markdown line 792 has H' in both exponents. The vector-sheaf criterion ends with F^h isomorphic to M, while line 802 has A. Proposition 17's sentence omits the symbol epsilon, but the immediately preceding sentence identifies the map, so that omission is non-misleading and recorded PASS±.

### PDF p.033/43 — print p.32

- Reviewed: 2026-10-01 20:43 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi H^1 divisor-class crop](audit/300dpi/Serre_1956_gaga_p033_H1-divisors_300dpi.png); PDF text layer and MinerU Markdown lines 804–812.
- Checked: completion of Proposition 18, the GL_1/C* remark, the divisor-class statement, and the setup for Proposition 19.
- Result: FAIL. The print identifies the divisor-class group as H^1(X,G); Markdown line 806 has H'(X,G). The crop confirms superscript 1. The surrounding group and divisor statements agree.

### PDF p.034/43 — print p.33

- Reviewed: 2026-10-01 23:54 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi fiber-product and diagram crop](audit/300dpi/Serre_1956_gaga_p034_fiber-diagram_300dpi.png); PDF text layer and MinerU Markdown lines 814–836.
- Checked: associated G/H spaces, the induced isomorphism and section, pullback P_1, the commutative fiber-product diagram, and the rational-section condition in Proposition 20.
- Result: PASS±. The displayed fiber products, transition maps and diagram agree with print; no content mismatch was found. The running title and print page number are not represented in Markdown.

### PDF p.035/43 — print p.34

- Reviewed: 2026-10-02 00:13 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi group examples crop](audit/300dpi/Serre_1956_gaga_p035_group-examples_300dpi.png); PDF text layer and MinerU Markdown lines 838–860.
- Checked: examples satisfying condition (R), the symplectic alternating-form reduction, the simply-connected conjecture, and the orthogonal-group counterexample condition.
- Result: PASS±. The crop confirms Sp_n with n=2m, the canonical alternating form, O_n^+ and n ≥ 3, and the H^1 map. These agree with Markdown; the running header/page number are omitted.

### PDF p.036/43 — print p.35

- Reviewed: 2026-10-02 00:19 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi Tor/Hom crop](audit/300dpi/Serre_1956_gaga_p036_Tor-Hom_300dpi.png); [300 dpi Hom-presentation crop](audit/300dpi/Serre_1956_gaga_p036_Hom-presentations_300dpi.png); PDF text layer and MinerU Markdown lines 878–918.
- Checked: the Tor criterion for flatness, localization example, canonical Hom-tensor map, Proposition 21 and the finite free presentation setup.
- Result: FAIL. The print uses Tor_1^A in the flatness criterion; Markdown line 878 has a fraktur i subscript, and the crop confirms numeral 1. Markdown line 896 also omits the map name after “L'homomorphisme”; this is non-misleading because the map is defined immediately above, but it is a recorded PASS± omission.

### PDF p.037/43 — print p.36

- Reviewed: 2026-10-02 00:41 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi T-diagram crop](audit/300dpi/Serre_1956_gaga_p037_T-diagram_300dpi.png); [300 dpi diagram endpoints crop](audit/300dpi/Serre_1956_gaga_p037_diagram-endpoints_300dpi.png); [300 dpi injection-map crop](audit/300dpi/Serre_1956_gaga_p037_E-tensor-B_300dpi.png); PDF text layer and MinerU Markdown lines 914–950.
- Checked: Proposition 21's T/T' diagram and five-lemma step; Proposition 22's definition of a flat pair, Tor exact sequences, and tensor-injection criterion.
- Result: PASS±. The print's rightmost T(L_1)/T'(L_1) diagram marks have incomplete/stray delimiters, and the injection sentence prints E → E⊗_A B*; the 300 dpi crops confirm these print quirks and Markdown preserves them. Markdown line 896 omits the name of the homomorphism in Proposition 21, but the preceding display defines it unambiguously.

### PDF p.038/43 — print p.37

- Reviewed: 2026-10-02 00:48 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi maximal-ideal crop](audit/300dpi/Serre_1956_gaga_p038_maximal-ideal_300dpi.png); PDF text layer and MinerU Markdown lines 952–982.
- Checked: Proposition 23's flat-pair transitivity argument, Remark, the local-ring setup, Proposition 24, and footnote (6).
- Result: FAIL. Print names the maximal ideal as fraktur lowercase m; Markdown line 976 gives uppercase M. Line 978 also renders m in regular rather than fraktur type, a non-misleading style loss. The subscript/variable identity in the setup is materially wrong at line 976.

### PDF p.039/43 — print p.38

- Reviewed: 2026-10-02 00:53 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi m-adic and Artin–Rees crop](audit/300dpi/Serre_1956_gaga_p039_m-adic-Artin-Rees_300dpi.png); PDF text layer and MinerU Markdown lines 986–1018.
- Checked: Proposition 24 and its corollary, the m-adic topology definition, Proposition 25(a)–(b), the Artin–Rees relation, and the completion map in Proposition 26.
- Result: FAIL. The print defines the neighborhood basis by the submodules m^n E; the crop confirms exponent n. Markdown line 996 has m°E. The Artin–Rees relation and completion map agree.

### PDF p.040/43 — print p.39

- Reviewed: 2026-10-02 00:57 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi completion diagram crop](audit/300dpi/Serre_1956_gaga_p040_completion-diagram_300dpi.png); PDF text layer and MinerU Markdown lines 1020–1048.
- Checked: completion of Proposition 26, the exact completion diagram, surjectivity/injectivity conclusion, and the opening of Proposition 27.
- Result: FAIL. In the top row of the diagram, the print tensors over A throughout. Markdown line 1029 uses Lambda as the tensor base in all three terms. The crop confirms A; the surrounding completion maps agree.

### PDF p.041/43 — print p.40

- Reviewed: 2026-10-02 01:03 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi local-ring maps crop](audit/300dpi/Serre_1956_gaga_p041_local-ring-maps_300dpi.png); PDF text layer and MinerU Markdown lines 1044–1064.
- Checked: Propositions 28–30, quotient-ring completion maps, the finite-module rank criterion, and the induced map between local rings.
- Result: FAIL. The print uses theta for the local-ring homomorphism; Markdown lines 1044, 1052, 1056 and 1058 use zero. Proposition 30 prints E' = E⊗_A A' and E' ≅ (A')^n, while line 1056 loses the tensor-base subscript and exponent. The crop confirms these formulas; the printed m ⊂ m' relation is also represented with a plain less-than sign in Markdown.

### PDF p.042/43 — print p.41

- Reviewed: 2026-10-02 01:09 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi full bibliography page](audit/300dpi/Serre_1956_gaga_p042_references_300dpi.png); [300 dpi references 11–14 crop](audit/300dpi/Serre_1956_gaga_p042_refs11-14_300dpi.png); PDF text layer and MinerU Markdown lines 1072–1113.
- Checked: final Proposition 30 proof and references [1]–[16] (authors, titles, journal/book names, volumes, years and pages).
- Result: FAIL. Reference [14] prints “Potenzreihenideale”; Markdown line 1109 has “Potenzreihendeale,” missing the i after “Potenzreihen.” The full page also includes the continuation of Proposition 30's proof at its top: print has A'^n where the Markdown had A'n. Both differences are repaired in the final Markdown; see the closeout register. Reference [11] has a period after “type” before the parenthetical subtitle in print; Markdown line 1103 omits it. That punctuation difference is PASS± and is left as a minor citation-format difference. The other checked bibliographic entries agree.

### PDF p.043/43 — print p.42

- Reviewed: 2026-10-02 01:15 EDT; actor=Peer-P09; model=gpt-6-luna; effort=max.
- Evidence: [300 dpi final references page](audit/300dpi/Serre_1956_gaga_p043_references_300dpi.png); PDF text layer and MinerU Markdown lines 1115–1121.
- Checked: references [17]–[20], including titles, author names, series/journal, place, and year.
- Result: PASS±. The checked reference text agrees with the print. The running author and print page number are not represented in Markdown.

## Audit closeout

- Comparison basis: original MinerU Markdown from commit `4e5d9aabe1bc05fbb69fe4f77c0e692470fd9935`, SHA-256 `82ded987cca1b0e03fe200a8059cd17b7e86d9a42b86f222f205a1c4a2a4b339`.
- The complete 43-page born-digital PDF text layer was compared page by page with the Markdown. `pdftotext -layout` produced 87,978 UTF-8 bytes over 43 nonempty pages with no U+FFFD. The visual review and glyph adjudications are cited in the page records; print page numbers 1–42 correspond to PDF pages 2–43, with PDF page 1 being the unnumbered journal cover.
- Pre-repair page grades: 15 PASS± and 28 FAIL. These grades record differences in the original Markdown snapshot, not the repaired file. All substantive FAIL differences identified in those page comparisons are listed below and corrected. The documented PASS± items are non-misleading omissions, layout/style losses, or print quirks retained faithfully.
- After the 43 page audits, the complete final Markdown was read from beginning to end. Each edit was made with `apply_patch`; the Markdown was not written, formatted, or repaired by a script. Final SHA-256: `f4ebe12f7a27be038319d2eb23db2f236b6dad7add13c26b9ed8d6224ed19408`.
- Markdown repair commit: `c270a3c2c4a35262210134fc22c20639cdeff0c4` (`fix(md): repair Serre GAGA transcription [Peer-P09 | gpt-6-luna/max]`). `git diff --check` passed before commit and on the closeout changes.
- The page records are ordered PDF p.001 through p.043. There is one `audit(page)` commit per PDF page; the separate Markdown repair commit follows the page audits. Two extra crops—`p010_ideal-J` and `p011_J-ideal`—were made during the complete final readback to resolve the ideal-symbol continuation; both are committed with this closeout. The final closeout commit follows the Markdown repair commit.
- No known substantive transcription discrepancy from the page audit remains unresolved. The citation punctuation difference noted for reference [11] on PDF p.042 is retained as PASS±; documented print quirks and non-misleading presentation omissions remain as recorded. No project progress/index files or other paper directories were modified. This candidate remains `CANDIDATE_NOT_CURRENT`; integration belongs to Master-Luna.

### Markdown repair register

The PDF page numbers below refer to the audited source page; evidence is linked in the corresponding page record above unless a crop is named here.

- PDF p.002: corrected “CNow” to “Chow.”
- PDF p.005: corrected the analytic sheaf subscript from `\mathcal{H}_{\backslash}` to `\mathcal{H}_{V}`.
- PDF p.006: corrected `H_{x,Y}` to `H_{x,X}`.
- PDF p.007: corrected both power-series subscripts `z_i` to `z_1`; PDF p.008: corrected the finite-extension subscript `z_i` to `z_1`.
- PDF p.010: corrected the second local-space subscripts to uppercase X in `\mathcal{H}_{x,X}` and `\mathcal{O}_{x,X}`, and corrected `\hat{0}` to `\hat{\theta}`.
- PDF p.011: corrected `\mathfrak I_x(Y)` to `\mathfrak J_x(Y)` in the definition continuation and both completed-ideal terms, as confirmed by the supplementary crops [p.010 ideal J](audit/300dpi/Serre_1956_gaga_p010_ideal-J_300dpi.png) and [p.011 ideal J](audit/300dpi/Serre_1956_gaga_p011_J-ideal_300dpi.png). Also corrected the Proposition 4 generator and “au moyen de” map from zero to `\theta`, restored formal-series brackets `[[...]]`, and changed `f'` to `f^r`.
- PDF p.014: corrected `O_x` to `O_X` and the second subscript in `O_{x,x}` to uppercase X. PDF p.015: corrected the second subscripts of the local `O` and `H` rings from lowercase x to uppercase X.
- PDF p.018: restored the missing prime on the final `\mathcal{F}_3'` in the prose exact sequence.
- PDF p.019: corrected local-space second subscripts to uppercase X/Y, replaced the accented `B/àB` with `B/aB`, and restored `B' = B/aB = B\otimes_A A'`.
- PDF p.020: restored the missing sheaf symbol C in “le faisceau C est cohérent.”
- PDF p.023: corrected `\mathcal{L}(n)` to `\mathcal{O}(n)` and restored the fifth column and `\varepsilon_5` in the long cohomology diagram.
- PDF p.024: corrected the first Hom section domain from `H^0(X^h,A)` to `H^0(X,A)`. Across PDF pp.024–025, corrected extension-by-zero notation to `\mathcal{M}^X`, the ideal from `\mathcal{J}_x` to `\mathcal{I}_x`, the stalk from `\mathcal{G}_{fx}` to `\mathcal{G}_x`, its analytic extension to `\mathcal{G}_x^h = \mathcal{M}_x^X`, the annihilation statement to `\mathcal{I}\cdot\mathcal{G}=0`, and the final `\mathcal{M}^X`.
- PDF p.026: corrected the hyperplane ideal from `\mathfrak b(E)` to `\mathcal{A}(E)`; changed the tensor sequence, kernel, Tor term, and twist terms from the garbled `\mathcal A`/`\mathbb 1_0` forms to `\mathfrak M`; restored the missing exact sequence (3), corrected sequence (4), and removed the extra untagged duplicate of (4) that was absent from the print. The 150 dpi full page and 300 dpi equations (1)–(4) crop show the printed pair.
- PDF p.027: corrected sequence (5) to use `\mathfrak M(n-1)` and `\mathfrak L_n`; corrected `\mathfrak P_n` to `\mathfrak L_n` in (7) and the following map; corrected the dimension function to `\mathfrak M(n)`; restored `H^1` and the `\mathfrak M(n-1)` term in (8); and restored the printed footnote marker `(5)` in place of the corrupted placeholder.
- PDF p.028: corrected the garbled sheaf symbol in both exact sequences to `\mathfrak M` and changed `L_i` to `L_1`.
- PDF p.029: corrected `X^\circ` to `X^\sigma` and restored `\Omega^p(X)` on the source side of the cohomology map.
- PDF p.031: corrected `H^6(X,A)` to `H^0(X,A)`.
- PDF p.032: corrected the group action to `(g,g')\cdot h = gh(g')^{-1}`, restored both `H^1` superscripts, and corrected the final sheaf from `\mathcal A` to `\mathfrak M`.
- PDF p.033: corrected `H'` to `H^1` in the divisor-class statement.
- PDF p.036: corrected both occurrences of the flatness criterion subscript from `\mathfrak i` to `1` in `\mathrm{Tor}_1`.
- PDF p.038: corrected uppercase M to the printed fraktur lowercase `\mathfrak m`.
- PDF p.039: corrected `m^\circ E` to `\mathfrak m^n E`.
- PDF p.040: corrected all three tensor bases in the completion diagram from `\Lambda` to A.
- PDF p.041: corrected the local-ring map glyph from zero to `\theta`; restored `E'=E\otimes_A A'` and `E'\simeq(A')^n`; and corrected the maximal-ideal relation from a plain `<` to `\mathfrak m\subset\mathfrak m'`.
- PDF p.042: corrected “Potenzreihendeale” to “Potenzreihenideale” and restored `A'^n` in the continuation of Proposition 30's proof at the page top.

## 逐页视觉复检（本块 PDF p.1–8，共 8 页）

<!-- actor=审计 serregaga; host=zcode; model=opencode-go-chat/space-bunny-free; effort=未知(自报) -->
- 范围：PDF p.1–8 = Numdam 封面（无印刷页码）+ 印刷 p.1–7。本节以下每条为独立逐页复检：一页一渲染、一页一眼、一页一条。
- 裁决源：150dpi pngmono 整页图 + 必要时 300dpi 裁片；`pdftotext` 文本层仅作辅助通道。二者冲突时以原页图为准。
- Markdown 基线 SHA-256：`a9cc959422149ae5fe33f28ce5efd4c72a7166e1926e9b650ebedc312155fcb6`（1119 行，含此前 Peer-P09/Wf-R-P09 两轮修复）。
- 工作目录：`/Users/aurolafly/.zcode/worktrees/cpf-redo-Serre_1956_gaga`（branch `cpf-redo/Serre_1956_gaga`，HEAD `97ae1712`）。本节不改动根级真值文件。

## p.001（PDF p.1 / 印刷封面，无页码）
- PNG：/tmp/serregaga_audit_p001.png（pngmono 150dpi）
- 核对：题录页——报头、作者行、文章标题、期刊卷期页码行、Numdam item URL、版权行、存档使用条款段、NUMDAM 标识与三行数字化声明。
- 结果：PASS±。逐项吻合：作者 `JEAN-PIERRE SERRE`（MD 行 1，印刷小型大写）；标题 `Géométrie algébrique et géométrie analytique`（MD 行 2，印刷加粗）；`Annales de l'institut Fourier, tome 6 (1956), p. 1-42` 与 `<http://www.numdam.org/item?id=AIF_1956__6__1_0>`（MD 行 4，卷 6、年 1956、起止页 1-42、item id 四项全对）；`© Annales de l'institut Fourier, 1956, tous droits réservés.`（MD 行 6）；存档条款全段（MD 行 8，印刷断行连字符 gé-nérales / utilisa-tion / in-fraction / conte-nir 已正确合字）；`NUMDAM` + 三行数字化声明 + `http://www.numdam.org/`（MD 行 10–13）。差异（登记不改，均不误导）：①印刷顶部灰点带上的字距报头 `ANNALES DE L'INSTITUT FOURIER` 在 MD 无独立行——期刊名已在题录行与版权文字中明确出现，属呈现省略；②印刷中 item URL 单独占一行，MD 并入题录行（同一句，未改内容）；③MD 行 4 用 `&lt;…&gt;` 转义尖括号，渲染后与印刷一致。
- 备注：born-digital Numdam 封面；`pdftotext -f 1 -l 1 -layout` 辅助通道与 PNG 一致，未用于任何判读裁决。本页无需改 Markdown。

## p.002（PDF p.2 / 印刷 p.1）
- PNG：/tmp/serregaga_audit_p002.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p002_300.png 及其切片 /tmp/p002_title_300.png（标题带）、/tmp/p002_kahl_300.png（kählériennes）、/tmp/p002_chow_300.png（CHOW）
- 核对：题录页（文章标题带 + 作者行 + 分隔线 + INTRODUCTION 节标题）、INTRODUCTION 第 1 段（两种观点的对照段）、第 2 段（含 Chow 定理句）、第 3 段首句至页末断句「de façon précise, nous」。
- 结果：PASS±（已修 1 处）。修复项：Markdown 行 15 首词作 `GEOMÉTRIE`（缺尖音符），印刷原页两处均作 `GÉOMÉTRIE`——300dpi 标题带裁片 `/tmp/p002_title_300.png` 亲眼可见首词 E 上有尖音符、第二个 GÉOMÉTRIE 亦有，两处一致 → 已用 Edit 改为 `# GÉOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE`。**溯源**：非回归，`git show cpf-redo/Serre_1956_gaga^:…`（=14aeb874）第 15 行与原始导出 commit `4e5d9aab` 第 15 行均已是缺音符的 `GEOMÉTRIE`，即 MinerU 导出即缺，本次为首修。其余核对项全部吻合：作者行 `par Jean-Pierre SERRE.`、INTRODUCTION 标题、第 1 段逐词（含 « transcendant »、`variétés kählériennes`——300dpi 裁片确认为 ä 分音符 + é 尖音符，与 MD `kählériennes` 一致；文本层拍平为 `kàhlériennes`，以原图为准）、`non singulière`、`principaux rôle` 相关表述、第 2 段逐词（`« de première espèce »`、`CHOW` 定理句）、第 3 段断句位置。差异（登记不改，均不误导）：①印刷小型大写 `CHOW` 在 MD 作 `Chow`（大小写规范化，词形正确，300dpi 裁片确认为大 C+小 HOW 的小型大写）；②印刷小型大写标题在 MD 未反映；③印刷斜体（`algébrique`、`analytique`、`faisceaux cohérents`、`principaux` 等词条内斜体）未标——mineru 已知拍平；④印刷 `supposée non singulière) ;` 分号前细空格被拍平为 `)`;`。
- 备注：本页修复 1 处（行 15 首词补尖音符），依据 300dpi 裁片 `/tmp/p002_title_300.png`；Edit 工具可用，未使用任何脚本写 Markdown。

## p.003（PDF p.3 / 印刷 p.2）
- PNG：/tmp/serregaga_audit_p003.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p003_300.png 及其切片 /tmp/p003_Ox_only.png、/tmp/p003_OxHx_300.png（𝒪_x / ℋ_x 记号）
- 核对：正文页——页眉「JEAN-PIERRE SERRE」与印刷页码「2」、INTRODUCTION 续段（biunivoquement 句至页末）、§1–§4 内容综述段（含 H. CARTAN、W-L. CHOW 引用与「espaces analytiques」引号）、𝒪_x / ℋ_x 局部环句与「couple plat」、§3 段（含 [18]、[3] exp. XVIII-XIX）、§4 应用段（含 BETTI、CHOW、semi-simples、unimodulaire、symplectique）、脚注 (1) 全文、页末「Annexe」句。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：页眉与页码正确（Markdown 未含，属 MinerU 不录页眉页码，全文性惯例）；第 1 段 `biunivoquement`、`laiss[e] invariants les groupes de cohomologie`、`(voir n° 12 pour les énoncés)`、`espaces fibrés algébriques et espaces fibrés analytiques` 全部一致；综述段 `Les deux premiers paragraphes sont préliminaires`、`Au § 1`、`H. CARTAN dans [3]`、`à cela près`、`variétés normales`、`restriction inutile`、`W-L. CHOW`、`encore inédits`、`Dans le § 2`、`propriétés élémentaires` 一致；记号句「si 𝒪_x (resp. ℋ_x) désigne l'anneau local (resp. l'anneau des germes de fonctions holomorphes) de X au point x, les anneaux 𝒪_x et ℋ_x ont même complété, et, de ce fait, forment un « couple plat », au sens de l'Annexe, déf. 4.」逐词一致，且 300dpi 裁片亲眼确认 𝒪_x 为带花体下标 x 的花体 O、ℋ_x 为花体 H 配下标 x，与 MD 的 `$\mathcal{O}_x$`/`$\mathcal{H}_x$` 完全对应（文本层此处拍平为 `0^`、`<%y`、`C\`、`^` 等乱码，不作判读依据）；§3 段 `théorèmes A et B de [3], exp. XVIII-XIX`、`[18]` 一致；§4 段 `nombres de Betti`、`automorphisme du corps des complexes`、`théorème de Chow`、`de groupe structural un groupe algébrique donné`、`fort incomplets`、`groupes semi-simples`、`groupe linéaire unimodulaire`、`groupe symplectique` 一致；脚注 (1)「Nous avons laissé de côté les applications aux fonctions automorphes, pour lesquelles nous renvoyons à [3], exp. XX.」与印刷逐词一致。差异（登记不改，均不误导）：①印刷小型大写 `CHOW`（两处：W-L. CHOW、théorème de CHOW）、`BETTI`、`H. CARTAN`（两处）在 MD 作 `Chow`、`Betti`、`H. CARTAN`——小型大写被规范为普通词形（同 p.002 同类大小写扁平化，词形本身正确）；②印刷斜体（`normales`、`espaces analytiques` 等词条内斜体，以及 §4 整段列表的斜体强调）未标——mineru 已知拍平；③脚注标记印刷作 `( 1 )` 带细空格，MD 作 `(1)`；④页眉与印刷页码在 MD 中无对应行。
- 备注：本页无 md 修复；文本层在 𝒪_x/ℋ_x 处严重失真，已按 SOP 以 300dpi 裁片仲裁，结论与原页一致。

## p.004（PDF p.4 / 印刷 p.3）
- PNG：/tmp/serregaga_audit_p004.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p004_300.png 及其切片 /tmp/p004_geq_300.png（n ≥ 0）、/tmp/p004_CnCq_300.png（C^r/C^s）、/tmp/p004_eps_300.png（ε_x 显示式）、/tmp/p004_HU_300.png、/tmp/p004_AxU_300.png、/tmp/p004_quot2.png（ℋ_x/𝒜_x(U)）、/tmp/p004_AxU_def.png、/tmp/p004_phiV.png（φ:U→V）、/tmp/p004_phixV.png（f∈ℋ_{φ(x),V}）
- 核对：正文页——页眉「GÉOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE」与印刷页码「3」、页首「Annexe」续句、§ 1 节标题「Espaces analytiques.」、n° 1 标题「Sous-ensembles analytiques de l'espace affine.」、解析子集定义段（n ⩾ 0、C^n、f_1…f_k、U∩W、f_i(z)=0、i=1…k、localement fermé/compact）、𝒞(X) 与 [18] n° 3、ℋ 束定义、限制同态显示式 ε_x、ℋ_{x,U}/ℋ_U/𝒜_x(U)/商环段、[3] exp. VI + [18] n° 32、holomorphe 定义段（φ:U→V、f∈ℋ_{φ(x),V} ⟹ f∘φ∈ℋ_{x,U}）。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：`§ 1. — Espaces analytiques.` 与 `1. Sous-ensembles analytiques de l'espace affine.` 两个标题层级正确；定义段 300dpi 裁片确认印刷为斜体 n + 斜等号 `n ⩾ 0`（裁片 `/tmp/p004_geq_300.png` 亲眼可见 ≥ 号），与 MD `$\geqslant 0$` 一致（文本层拍平为 `^`，不作依据）；`$\mathbb{C}^{n}$`（上标 n）与印刷粗体 C^n 一致；`f_{1}, \ldots, f_{k}`、`i = 1, \ldots, k`、`U \cap` W、`z \in \mathrm{W}`、`localement fermé`、`c'est-à-dire intersection d'un ouvert et d'un fermé`、`localement compact` 均逐词一致；`$\mathcal{C}(\mathbf{X})$`（粗体 X）与印刷 𝒞(X) 一致；`à valeurs dans $\mathbb{C}$ (cf. [18], n° 3)` 一致；`$\mathcal{H}$` 束、`sous-faisceau de $\mathcal{C}(\mathbb{C}^n)$` 一致；显示式 ε_x 经 300dpi 裁片 `/tmp/p004_eps_300.png` 确认为 `ε_x : 𝒞(C^n)_x → 𝒞(U)_x.`，含花体 𝒞、粗体 C^n 上标、两处下标 x 与**句末句点**，与 MD 行 48（含尾句点）逐符对应；`$\mathcal{H}_{x,\mathrm{U}}$`、`$\mathcal{H}_{\mathrm{U}}$`、`$\mathcal{A}_x(\mathrm{U})$`、`$\varepsilon_x\colon \mathcal{H}_x\to \mathcal{H}_{x,\mathrm{U}}$` 经裁片 `/tmp/p004_HU_300.png`、`/tmp/p004_AxU_300.png`、`/tmp/p004_AxU_def.png` 逐一确认花体 ℋ 与下标 x,U；商环 `$\mathcal{H}_x / \mathcal{A}_x(\mathrm{U})$` 经裁片 `/tmp/p004_quot2.png` 确认为花体 ℋ_x / 花体 𝒜_x(U) 含尾句点；`$f\in\mathcal{H}_x$` 经裁片确认；`[3], exp. VI ainsi que [18], n° 32` 一致；末段 300dpi 裁片 `/tmp/p004_CnCq_300.png` 确认印刷为 `C^r` et `C^s`（150dpi 下曾误读为 n/q，300dpi 仲裁后确认 MD 行 55 的 `$\mathbb{C}^r$`/`$\mathbb{C}^s$` 正确），`$\varphi: \mathrm{U} \to \mathrm{V}$` 经 `/tmp/p004_phiV.png` 确认；`$f \in \mathcal{H}_{\varphi(x),\mathrm{V}}$ entraîne $f \circ \varphi \in \mathcal{H}_{x,\mathrm{U}}$` 经 `/tmp/p004_phixV.png` 确认下标 φ(x),V 与 x,U。差异（登记不改，均不误导）：①印刷显示式末尾句点已保留于 MD 行 48，本页无缺失；②印刷斜体（`analytique`、`faisceau des germes de fonctions holomorphes sur U`、`application holomorphe`、`topologie usuelle` 等词条内斜体）未标——mineru 已知拍平；③印刷正体 U/V/W 与 MD 数学模式 `\mathrm{U}`/`\mathrm{V}` 混排（语义正确，可辨识）；④页眉与印刷页码「3」在 MD 无对应行；⑤印刷断行连字符 `holo-morphe` 已由 MD 正确合字为 `holomorphe`（非缺陷，属正确处理）。
- 备注：本页无 md 修复；文本层在多处理论公式处失真（`0^`、`3€`、`C\` 等），全部判读以 300dpi 裁片为准。

## p.005（PDF p.5 / 印刷 p.4）
- PNG：/tmp/serregaga_audit_p005.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p005_300.png 及其切片 /tmp/p005_HI_300.png（公理 (H_I)）、/tmp/p005_HII_300.png（公理 (H_II)）、/tmp/p005_def1.png（Déf.1 的 ℋ_X/𝒞(X)）、/tmp/p005_prod.png（积显示式）、/tmp/p005_Cr.png（C^r/C^{r′}）、/tmp/p005_Crr.png（C^{r+r′}）、/tmp/p005_HV3.png 与 /tmp/p005_HV4.png（isomorphisme 判据句的 ℋ_U→ℋ_V）、/tmp/p005_continue.png（si elle continue 行）
- 核对：正文页——页眉「JEAN-PIERRE SERRE」与印刷页码「4」、§1 续段（s coordonnées / sections de ℋ_U）、复合与同构判据段（φ^{-1}、homéomorphisme、ℋ_U→ℋ_V）、乘积构造段（C^r / C^{r′} / C^{r+r′}、[18] n° 33、φ: U→V 与 φ′: U′→V′）、积显示式、拓扑乘积句、n° 2 标题「La notion d'espace analytique.」、DÉFINITION 1 全陈述、公理 (H_I) 与 (H_II) 全陈述、公理后段（ℋ_X、f∈ℋ_{φ(x),Y} ⟹ f∘φ∈ℋ_{x,X}、N. BOURBAKI）。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：`Il revient au même de dire que les s coordonnées de $\varphi(x)$, $x\in\mathbf{U}$… sections de $\mathcal{H}_{\mathbf{U}}$` 一致；`isomorphisme analytique`、`$\varphi$ et $\varphi^{-1}$`、`homéomorphisme` 一致；**isomorphisme 判据句**经 300dpi 裁片 `/tmp/p005_HV3.png`、`/tmp/p005_HV4.png` 确认印刷为「transforme le faisceau ℋ_U en le faisceau **ℋ_V**.」，下标为衬线 V（V 形清晰可辨，非反斜线）→ MD 行 59 的 `$\mathcal{H}_{V}$` 正确（**旧导出此处曾作 `\mathcal{H}_{\backslash}`，前轮 Peer 的修复与原页相符，本次复核维持，不属回归**）；乘积段 `C$^{r}$`、`C$^{r'}$`、`C$^{r+r'}$` 经裁片 `/tmp/p005_Cr.png`、`/tmp/p005_Crr.png` 确认三项指数全对；`[18], n° 33`、`sous-ensemble localement fermé`、`application régulière`/`application holomorphe` 一致；积显示式经 `/tmp/p005_prod.png` 确认为 `$\varphi \times \varphi^{\prime}: \mathrm{U} \times \mathrm{U}^{\prime} \rightarrow \mathrm{V} \times \mathrm{V}^{\prime}.$` 含尾句点，与 MD 行 63–65 一致；`topologie de U × U' est identique à la topologie produit` 一致；`## 2. La notion d'espace analytique.` 标题层级正确；DÉFINITION 1 陈述经 `/tmp/p005_def1.png` 确认 `$\mathcal{H}_{\mathrm{X}}$`（粗体正体 X 下标）与 `$\mathcal{C}(\mathrm{X})$`（粗体 X）与印刷一致，`ces données étant assujetties à vérifier les axiomes suivants:` 一致；公理标号经 300dpi 裁片 `/tmp/p005_HI_300.png`、`/tmp/p005_HII_300.png` 确认印刷为**衬线罗马数字**下标 `(H_I)` 与 `(H_II)`（与同页「n° 1.」的阿拉伯 1 字形明显不同）→ MD 行 73/75 的 `$(\mathrm{H}_{\mathrm{I}})$`/`$(\mathrm{H}_{\mathrm{II}})$` 正确；公理 (H_I) 的 `recouvrement ouvert $\{V_{i}\}$`、`chaque $V_{i}$`、`muni de la topologie et du faisceau induits par ceux de X`、`isomorphe à un sous-ensemble analytique $U_{i}$ d'un espace affine`、`définis au n° 1.` 全句一致；公理 (H_II) `La topologie de X est séparée.` 一致；末段 `$\mathcal{H}_{\mathrm{X}}$ sera appelé le faisceau des germes de fonctions holomorphes sur X`、`$\varphi: \mathrm{X} \to \mathrm{Y}$`、`$\mathcal{H}_{\varphi(x),\mathrm{Y}}$`、`$\mathcal{H}_{x,\mathrm{X}}$`、`famille de morphismes (au sens de N. BOURBAKI)` 一致。**print quirk 忠实登记（不按语法预期补词）**：300dpi 裁片 `/tmp/p005_continue.png` 确认印刷原文即作「si elle **continue**, et si f∈ℋ_{φ(x),Y} entraîne f∘φ∈ℋ_{x,X};」——「elle」与「continue」之间**无 « est »**，属印刷脱漏，MD 行 77 原样保留 `si elle continue`，不改正。差异（登记不改，均不误导）：①印刷斜体（`analytique`、`isomorphisme analytique`、`morphismes`、`espace affine` 等词条内斜体，及 DÉFINITION 1 与两条公理整段斜体）未标——mineru 已知拍平；②印刷正体 U/V/X 与 MD `\mathrm{U}`/`\mathrm{V}`/`\mathrm{X}` 混排（语义正确）；③页眉与印刷页码「4」在 MD 无对应行；④印刷断行连字符 `holo-morphe`/`appli-cations` 已由 MD 正确合字。
- 备注：本页无 md 修复；前轮 Peer 对 ℋ_{\backslash}→ℋ_V 的修复经本次 300dpi 独立复核与原页相符，非回归、非错修。

## p.006（PDF p.6 / 印刷 p.5）
- PNG：/tmp/serregaga_audit_p006.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p006_300.png 及其切片 /tmp/p006_HIIref.png（公理交叉引用 (H_II)）、/tmp/p006_AxY_zoom2.png（𝒜_x(Y)）、/tmp/p006_HxX3.png（f∈ℋ_{x,X} 下标）、/tmp/p006_sheaf.png（𝒜_x(Y)/ℋ_X）、/tmp/p006_quot.png（商束 ℋ_X/𝒜(Y)）、/tmp/p006_HY.png（限制 ℋ_Y）、/tmp/p006_prop1a.png（l'identifier à ℋ_Y）、/tmp/p006_prop1b.png（Prop.1 a) 与 [18] n° 15）
- 核对：正文页——页眉「GÉOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE」与印刷页码「5」、carte 定义段（cartes、(H_?) 交叉引用、φ: V→U、φ(Y∩V)、induite、[18] n° 35）、乘积结构段（φ×φ′: V×V′→U×U′、coïncide）、[18] nos 34-35 句、n° 3 标题「Faisceaux analytiques.」、faisceau analytique 定义（ℱ、ℋ_X-modules、[18] n° 6）、𝒜_x(Y)/理想束/商束段、PROPOSITION 1 a) 与 b)（[18] n° 15、[18] n° 12）。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：`carte de V`、`isomorphisme analytique`、`(H$_{II}$) signifie qu'il est possible de recouvrir X par des ouverts possédant des cartes`、`$\varphi(Y \cap V)$`、`dites induites` 段 `[18], n° 35 pour le cas algébrique` 一致；乘积段 `si $\varphi: V \to U$ et $\varphi': V' \to U'$ sont des cartes`、`$\varphi \times \varphi': V \times V' \to U \times U'$`、`la topologie de X × X' coïncide avec la topologie produit` 一致；`[18], nos 34-35` 一致；`## 3. Faisceaux analytiques.` 层级正确；faisceau analytique 段 `[2], exp. XV`、`$\mathcal{F}$`、`$\mathcal{H}_{\mathrm{X}}$`、`$\mathcal{H}_{\mathrm{X}}$-modules`、`[18], n° 6` 一致；**𝒜_x(Y) 定义段**经 300dpi 裁片 `/tmp/p006_AxY_zoom2.png` 确认印刷为花体 𝒜 配下标 x 与参数 (Y)，与 `$\mathcal{A}_{x}(Y)$` 一致；**`f ∈ ℋ_{x,X}` 的第二下标**经裁片 `/tmp/p006_HxX3.png` 放大确认印刷下标为**小写斜体 x + 逗号 + 衬线大写 X**（X 字形与同页大写 X 一致，与小写 x 明显不同）→ MD 行 87 的 `$f \in H_{x,X}$` 正确（**旧导出此处曾作 `H_{x,Y}`，前轮 Peer 修复与原页相符，本次独立复核维持，非回归**）；**理想束段**经 `/tmp/p006_sheaf.png` 确认 `Les $\mathcal{A}_{x}(Y)$ forment un faisceau d'idéaux $\mathcal{A}(Y)$ du faisceau $H_{X}$` 一致；**商束**经 `/tmp/p006_quot.png` 确认 `$\mathcal{H}_{X}/\mathcal{A}(Y)$`，经 `/tmp/p006_HY.png` 确认 `sa restriction à Y n'est autre que $H_{Y}$`，经 `/tmp/p006_prop1a.png` 确认 `l'identifier à $H_{Y}$, cf. [18], n° 5.` 三处均与 MD 行 87 一致；PROPOSITION 1 经 `/tmp/p006_prop1b.png` 确认 `a) Le faisceau $\mathcal{H}_{\mathrm{X}}$ est un faisceau cohérent d'anneaux ([18], n° 15)` 一致；`b) Si Y est un sous-espace analytique fermé de X, le faisceau $\mathcal{A}(\mathrm{Y})$ est un faisceau analytique cohérent (c'est-à-dire un faisceau cohérent de $\mathcal{H}_{\mathrm{X}}$-modules, au sens de [18], n° 12)` 一致。**print quirk 忠实登记（不按数学/语义预期改正）**：300dpi 裁片 `/tmp/p006_HIIref.png` 确认印刷原文交叉引用即作 `L'axiome (H_II) signifie qu'il est possible de recouvrir X par des ouverts possédant des cartes`——下标为两个衬线罗马 II，语义上此处描述的是覆盖公理 (H_I)，属**印刷原文自身的交叉引用 quirk**；MD 行 79 作 `(H$_{II}$)` 忠实保留，不按语义改正。差异（登记不改，均不误导）：①MD 行 87 段内的 `$H_{x,X}$`、`$H_{X}$`、`$H_{Y}$` 用正体 H，而同段 `$\mathcal{H}_{X}/\mathcal{A}(Y)$`、`$\mathcal{A}(Y)$` 用花体——印刷一律花体 ℋ，属 minerU 花体/正体混排的全文性伪影，不妨碍辨识，按 SOP 不批量改；②印刷斜体（`carte`、`induite`、`produit`、`sous-espace analytique`、`faisceau cohérent` 等词条内斜体，及 Prop.1 整段斜体）未标；③印刷正体 X/Y 与 MD `\mathrm{X}`/`\mathrm{Y}` 混排；④页眉与印刷页码「5」在 MD 无对应行；⑤印刷断行连字符 `restric-tion` 等已由 MD 正确合字。
- 备注：本页无 md 修复；前轮 Peer 对 H_{x,Y}→H_{x,X} 的修复经本次 300dpi 独立复核与原页相符，非回归、非错修；本次另登记前两轮均未记录的 (H_II) 交叉引用印刷 quirk。

## p.007（PDF p.7 / 印刷 p.6）
- PNG：/tmp/serregaga_audit_p007.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p007_300.png 及其切片 /tmp/p007_top1.png、/tmp/p007_top2.png、/tmp/p007_top3.png（页首 Prop.1 证明段与 [1]/[2] 引用）、/tmp/p007_corps.png（l'idéal 𝔪 句）、/tmp/p007_next.png（ℋ_x/𝔪 句）、/tmp/p007_s1full.png、/tmp/p007_s2full.png、/tmp/p007_s3b.png（三处 C{z_1,…,z_n}）、/tmp/p007_cap2.png（显示式 0 = ∩𝔭_i）、/tmp/p007_ref15.png（[15] chap. iv § 2）
- 核对：正文页——页眉「JEAN-PIERRE SERRE」与印刷页码「6」、Prop.1 证明段（K. OKA/H. CARTAN、[1] ths. 1 et 2、[2] exp. XV-XVI、ℋ_X = ℋ_U/𝒜(X)、[18] n° 16、`L'assertion b) se démontre de la même manière.`）、相干解析束例段（cf. n° 20、[3] exp. XX）、n° 4 标题「Voisinage d'un point dans un espace analytique.」、局部环段（ℋ_x、唯一极大理想 𝔪、ℋ_x/𝔪、C、algèbre locale、algèbre 局部）、C{z₁,…,z_n} 三处、noethérien/analytique 段（[3] exp. VII、[16]）、正则局部判据段（régulier、dimension n、point simple、variété analytique）、nilpotent 段（[15], chap. iv, § 2）、显示式 0 = ∩𝔭_i。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：`K. OKA et H. CARTAN cf. [1], ths. 1 et 2 ainsi que [2], exp. XV-XVI` 一致（裁片 `/tmp/p007_top2.png` 确认印刷为小型大写 CARTAN）；`$\mathbb{C}^{n}$` 一致；`$\mathcal{H}_{\mathrm{X}} = \mathcal{H}_{\mathrm{U}} / \mathcal{A}(\mathrm{X})$`、`$\mathcal{H}_{\mathrm{U}}$`、`$\mathcal{A}(\mathrm{X})$`、`[18], n° 16`、`L'assertion $b$) se démontre de la même manière.` 一致；`faisceaux de germes de sections d'espaces fibrés à fibre vectorielle (cf. n° 20)`、`fonctions automorphes ([3], exp. XX)` 一致；`## 4. Voisinage d'un point dans un espace analytique.` 层级正确；`$x$ un point de X`、`$H_{x}$ l'anneau des germes de fonctions holomorphes sur X au point x`、`algèbre sur C`、`unique idéal maximal`、`formé des fonctions f nulles en x`、`$H_{x}/m$ n'est autre que C`、`algèbre locale sur C` 一致；**三处 C{z_1,…,z_n}** 经 300dpi 裁片 `/tmp/p007_s1full.png`（收敛级数句）、`/tmp/p007_s2full.png`（商代数 `C{z_1, …, z_n}/𝔞` 句）、`/tmp/p007_s3b.png`（正则局部判据句）逐一放大确认**首下标均为阿拉伯数字 1**（带衬线足笔）、**末下标均为斜体 n** → MD 行 99 两处与行 101 一处的 `z_{1}, \ldots, z_{n}` 正确（**旧导出三处均曾作 `z_i`，前轮 Peer 修复与原页相符，本次独立复核维持，非回归**）；`$[3]$, exp. VII`、`$[3]$, loc. cit.$`、`$[16]$`、`anneau noethérien`、`anneau analytique`、`H. CARTAN` 一致；正则局部判据段 `$\mathbb{C}\{z_{1},\ldots,z_{n}\}$`、`anneau local régulier de dimension n`、`point simple de dimension n`、`une variété analytique` 一致；**显示式**经 `/tmp/p007_cap2.png` 确认印刷为 `0 = ∩𝔭_i,`（fraktur 𝔭、下标 i、**尾逗号**）→ MD 行 106 `0 = \cap \mathfrak {p} _ {i},` 一致；`[15], chap. iv, § 2` 经 `/tmp/p007_ref15.png` 确认一致。差异（登记不改，均不误导，属全文性伪影类）：①印刷理想 **𝔪 为 fraktur（花体 m）**，MD 行 99 作斜体 `m`（两处：`l'idéal m`、`$H_{x}/m$`）——fraktur 拍平为普通斜体，与同段 ℋ→`H`、粗体 𝔠→`C` 属同一类 mineru 字形拍平伪影，全文一致，不妨碍辨识（该理想唯一确定，不致误读），按 SOP 不单点批量改；②印刷 `C{z₁,…,z_n}` 外的花体 𝒞 在 MD 作 `\mathbb{C}`，同段 `X=C^n` 作 `C^{n}`——同一类字形混排；③印刷小型大写 `K. OKA`、`H. CARTAN` 在 MD 作 `K. OKA`、`H. CARTAN`（已大写，一致）；④印刷斜体（`algèbre locale`、`anneau noethérien`、`anneau analytique`、`régulier`、`simple`、`variété analytique`、`cohérent` 等词条内斜体）未标；⑤页眉与印刷页码「6」在 MD 无对应行。
- 备注：本页无 md 修复；前轮 Peer 对三处 `z_i`→`z_1` 的修复经本次 300dpi 独立复核与原页相符，非回归、非错修。

## p.008（PDF p.8 / 印刷 p.7）
- PNG：/tmp/serregaga_audit_p008.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p008_300.png 及其切片 /tmp/p008_top_p.png（𝔭_i = 𝒜_x(X_i) 行）、/tmp/p008_sr1.png 与 /tmp/p008_formal2.png（三处 C{z_1,…,z_r} 与 C[[z_1,…,z_r]]）、/tmp/p008_s2.png（§ 2 节标题）、/tmp/p008_n5h.png（n° 5 标题）、/tmp/p008_lem1a.png、/tmp/p008_lem1c1.png（LEMME 1 a)/c) 与 C^n、C^{n′}）
- 核对：正文页——页眉「GÉOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE」与印刷页码「7」、n° 4 续段（𝔭_i、𝔭_i = 𝒜_x(X_i)、ℋ_x/𝔭_i = ℋ_{x,X_i}、dimension 段、coïncide、Krull、anneau d'intégrité、r、[14] § 4、[3] exp. VIII、三处级数代数、[16] p. 18）、§ 2 节标题「Espace analytique associé à une variété algébrique.」、Z-拓扑约定段（usuelle、Zariski、Z-ouvert）、n° 5 标题「Définition de l'espace analytique associé à une variété algébrique.」、lemme 引入句、LEMME 1 a)–d) 四项。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：`$\mathfrak{p}_i$ désignant les idéaux premiers minimaux de $\mathcal{H}_x$` 经 `/tmp/p008_top_p.png` 确认 fraktur 𝔭_i 与花体 ℋ_x 一致；`Si l'on note $X_i$ les composantes irréductibles de X en $x$, on a $\mathfrak{p}_i = \mathcal{A}_x(X_i)$ et $\mathcal{H}_x / \mathfrak{p}_i = \mathcal{H}_{x,\mathrm{X}_i}$` 一致；`dimension (analytique — c'est-à-dire la moitié de la dimension topologique)`、`la borne supérieure des dimensions des $X_i$`、`coïncide avec la dimension (au sens de Krull)`、`$\mathcal{H}_x$ est un anneau d'intégrité`、`si l'on note $r$ la dimension analytique`、`[14], § 4 ainsi que [3], exp. VIII`、`[16], p. 18`、`ce qui démontre notre assertion` 全部一致；**三处级数代数**经 300dpi 裁片 `/tmp/p008_sr1.png`（`$\mathbb{C}\{z_{1},\dots,z_r\}$` 与 `comme $\mathbb{C}\{z_1,\dots,z_r\}$`）与 `/tmp/p008_formal2.png`（`$\mathbb{C}[[z_1,\dots,z_r]]$`）逐一放大确认**首下标均为阿拉伯 1、末下标均为斜体 r、双括号 [[ ]] 完整** → MD 行 109 三处正确（**旧导出此处曾作 `z_i`，前轮 Peer 修复与原页相符，本次独立复核维持，非回归**）；`a pour complété l'algèbre de séries formelles`、`sa dimension est $r$` 一致；`## § 2. — Espace analytique associé à une variété algébrique.` 经 `/tmp/p008_s2.png` 确认印刷为**粗体节标题**，`##` 层级正确；Z-拓扑约定段 `sur le corps C`、`la topologie « usuelle », et la topologie « de Zariski »`、`nous ferons précéder de la lettre Z`、`« Z-ouvert » signifiera « ouvert pour la topologie de Zariski »` 逐词一致；**n° 5 标题**经 `/tmp/p008_n5h.png` 确认印刷 `5. Définition de l'espace analytique associé à une variété algébrique.` 为**粗体**，与 n° 1–4 同式 → MD 行 115 的 `## 5. …` 层级正确（**旧 mineru 曾降为普通段落，前轮 Peer 升回 `##` 的结构修复与原页相符，本次复核维持，非回归**）；`La possibilité de munir toute variété algébrique d'une structure d'espace analytique résulte du lemme suivant :` 一致；LEMME 1 经 `/tmp/p008_lem1a.png` 确认 `a) La Z-topologie de $\mathbb{C}^{n}$ est moins fine que la topologie usuelle` 一致；`b) Tout sous-ensemble Z-localement fermé de $\mathbf{C}^n$ est analytique` 一致；**c)** 经 `/tmp/p008_lem1c1.png` 确认印刷指数为 **n** 与 **n′** 两处（`de $\mathbf{C}^n$ et de $\mathbf{C}^{n'}$`），`$f: \mathrm{U} \to \mathrm{U}'$`、`une application régulière`、`alors $f$ est holomorphe` 一致；`d) Dans les hypothèses de c), si l'on suppose en outre que f est un isomorphisme birégulier, c'est aussi un isomorphisme analytique.` 一致。差异（登记不改，均不误导，属全文性伪影类）：①印刷 `$\mathcal{H}_{x,\mathrm{X}_i}$` 的第二下标 X_i 为斜体，MD 行 109 作正体 `\mathrm{X}_i`；②fraktur 𝔭_i 与花体 ℋ 的混排、以及同段 ℋ→`H` 的拍平（同 p.007 类）；③印刷花体 𝒞 在 MD 作 `\mathbb{C}`/粗体 `C` 混排；④印刷斜体（`dimension`、`coïncide`、`Z-topologie`、`moins fine`、`régulière`、`birégulier` 等词条内斜体，及 LEMME 1 整段斜体）未标；⑤页眉与印刷页码「7」在 MD 无对应行；⑥印刷断行连字符 `al-gébrique`、`struc-ture` 已由 MD 正确合字。
- 备注：本页无 md 修复；前轮 Peer 对三处 `z_i`→`z_1` 与 n° 5 标题升 `##` 两项修复均经本次 300dpi 独立复核与原页相符，非回归、非错修。

## 本块收尾（p.001–p.008，PDF 第 1–8 页，共 8 页）

- 覆盖：PDF p.1–8 = Numdam 封面（无印刷页码）+ 印刷 p.1–7。8/8 页逐页执行「150dpi pngmono 整页渲染 → Read 亲眼目检 → 读对应 Markdown 段 → 五点比对 → 立即落签」，无跳页、无合并。
- 等级分布：**PASS± × 8**（p.001–p.008 全部 PASS±，无 FAIL，无纯 PASS）。其中 p.002 含 1 处已修缺陷；其余 7 页差异均为呈现级（斜体/小型大写/花体-fraktur 拍平/页眉页码/断行合字），不误导。
- 本块 md 改动合计 **1 处**：行 15 `# GEOMÉTRIE…` → `# GÉOMÉTRIE…`（补首词 E 上的尖音符）。溯源结论：**非导出回归**——`git show cpf-redo/Serre_1956_gaga^:…`（14aeb874）与原始 MinerU 导出 commit `4e5d9aab` 第 15 行均为缺音符的 `GEOMÉTRIE`，即导出即缺，本块首修。证据：300dpi 裁片 `/tmp/p002_title_300.png`。
- 前轮修复独立复核（本次 300dpi 逐项重验，全部与原页相符，均非回归、非错修）：p.002 CHOW→Chow；p.005 ℋ_{\backslash}→ℋ_V；p.006 H_{x,Y}→H_{x,X}；p.007 三处 C{z_i}→C{z_1}；p.008 三处 C{z_i}→C{z_r}；p.008 n° 5 标题升 `##`；p.005 公理标号 (H_1)→(H_I)。
- print quirk 忠实登记簿（保留未改，逐条以 300dpi 裁片为证）：①p.002/003 小型大写 CHOW/BETTI/CARTAN/OKA 在 MD 规范化；②p.005「si elle **continue**, et si」缺 « est »（印刷脱漏）；③p.006 交叉引用 `L'axiome (H_II) signifie qu'il est possible de recouvrir X…`（语义应指覆盖公理 (H_I)）；④p.007 理想 𝔪 为 fraktur、p.007/008 fraktur 𝔭 与花体 ℋ/𝒞 拍平为正体/斜体（全文性伪影，不误导，不批量改）；⑤p.002 标题小型大写、p.004 `n ⩾ 0` 斜等号（文本层拍平为 `^`，以原图为准）；⑥各页页眉与印刷页码在 MD 无对应行（全文惯例）。
- 范围声明：本块仅覆盖 PDF p.1–8；印刷 p.8 起（PDF p.9–43）及其余页块不在本次范围，留待后续。

## 本块复核（p.009–p.016，PDF 第 9–16 页，共 8 页）

<!-- actor=审计 serregaga; host=zcode; model=opencode-go-chat/space-bunny-free; effort=未知(自报) -->
- 范围：PDF p.9–16 = 印刷 p.8–15。本节以下每条为独立逐页复检：一页一渲染、一页一眼、一页一条。
- 裁决源：150dpi pngmono 整页图 + 必要时 300dpi 裁片；`pdftotext` 文本层仅作辅助通道。二者冲突时以原页图为准。
- Markdown 基线 SHA-256：`bb2b9d019f90f5d76c92e49fb73e7636dc7ea2e1b926af100bb6b6131e813801`（1119 行；已含 p.001–p.008 块的 1 处首词尖音符修复）。
- 工作目录：`/Users/aurolafly/.zcode/worktrees/cpf-redo-Serre_1956_gaga`（branch `cpf-redo/Serre_1956_gaga`，HEAD `97ae1712`，父提交 `14aeb874`）。本节不改动根级真值文件。

## p.009（PDF p.9 / 印刷 p.8）
- PNG：/tmp/serregaga_audit_p009.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p009_300.png 及其切片 /tmp/p009_phi_display.png（显示式 φ : V → U,）、/tmp/p009_HI_lbl2.png（公理 (H_I)）、/tmp/p009_HII_VA2.png（公理 (H_II)）、/tmp/p009_VA.png（公理 (VA′_II)）、/tmp/p009_Vprime4.png（V′ :→ U′）、/tmp/p009_Tij.png、/tmp/p009_Zfermes.png（graphes T_ij / Z-fermés）
- 核对：正文页——页眉「JEAN-PIERRE SERRE」与印刷页码「8」、Z-闭集定义段（a)/b)/c)/d) 与 f^{-1}）、carte 设置段（[18] n° 34、Z-ouvert）、显示式 φ : V → U,、D'après le lemme 1, b) 句、PROPOSITION 2 全陈述、括号补充段（Plus brièvement）、唯一性/存在性证明段（recouvrir、φ^{-1}、V ∩ V′、a fortiori、(H_I)、(H_II)、(VA′_II)、[18] n° 34、T_ij、U_i × U_j、séparé）、Remarque 段。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：`Par définition, un sous-ensemble Z-fermé de $\mathbb{C}^n$ est défini par l'annulation d'un certain nombre de polynômes`、`(resp. holomorphe)`、`on en déduit bien $a$) (resp. $b$)`、`Pour démontrer $c$), on peut supposer que $\mathrm{U}' = \mathbb{C}$`、`$\mathrm{U}' = \mathbb{C}$`、`$d$) est conséquence immédiate de $c$) appliqué à $f^{-1}$` 一致；`X une variété algébrique sur le corps C (au sens de [18], n° 34, donc non nécessairement irréductible)`、`Soit V un sous-ensemble Z-ouvert de X, possédant une carte (algébrique)` 一致；**显示式**经 `/tmp/p009_phi_display.png` 确认印刷为 `φ : V → U,`（**含尾逗号**）→ MD 行 131–133 的 `$\varphi : \quad \mathrm{V} \rightarrow \mathrm{U},$` 一致；`sur un sous-ensemble Z-localement fermé U d'un espace affine. D'après le lemme 1, b), U peut être muni d'une structure d'espace analytique.` 一致；PROPOSITION 2 陈述（`Il existe sur X une structure d'espace analytique et une seule telle que, pour toute carte $\varphi: V \to U$, l'ensemble Z-ouvert V soit ouvert, et $\varphi$ soit un isomorphisme analytique de V (muni de la structure analytique induite par celle de X) sur U (muni de la structure analytique définie au n° 1)`）与 `(Plus brièvement : toute carte algébrique doit être une carte analytique)` 逐词一致；唯一性/存在性段 `L'unicité est évidente`、`au moyen de $\varphi^{-1}$`、`$V \cap V'$ par V et par V'$`、`en vertu du lemme 1, $d$)`、`en vertu du lemme 1, $a$)`、`Par recollement`、`un faisceau $\mathcal{H}_X$ qui vérifient visiblement l'axiome`、`$T_{ij}$`、`$U_i$`、`$U_j$`、`$U_i \times U_j$`、`a fortiori`、`X est séparé` 一致；`Remarque. — On peut donner une définition directe de la structure analytique de X, sans passer par les cartes $\varphi: V \to U$.` 一致。**公理标号（罗马数字）**：经 300dpi 裁片 `/tmp/p009_HI_lbl2.png`、`/tmp/p009_HII_VA2.png`、`/tmp/p009_VA.png` 逐一确认印刷为 `(H_I)`（衬线罗马 I）、`(H_II)`（衬线罗马 II）、`(VA′_II)`（斜体 VA + A 右上撇 + 罗马 II 下标）→ MD 行 141 的 `($H_I$)`、`($H_{II}$)`、`($VA_{II}'$)` 三项全对。差异（登记不改，均不误导）：**print quirk 忠实保留**——300dpi 裁片 `/tmp/p009_Vprime4.png` 亲眼确认印刷原文即作 `Si $\varphi': V': \to U'$`，**V′ 与箭头之间多一个冒号**（φ′ 后已有冒号，此处为重复），属印刷脱漏；MD 行 141 原样保留 `\varphi': V': \to U'`，**不按数学/排版预期删去该冒号**。另有呈现级差异：①印刷斜体（Prop. 2 陈述整段、括号补充段、`Plus brièvement`、`a fortiori`、`Remarque`、`étant de caractère` 等词条内斜体）未标；②印刷正体 U/V/X 与 MD `\mathrm{U}`/`\mathrm{V}` 混排（语义正确）；③页眉与印刷页码「8」在 MD 无对应行；④印刷断行连字符 `holomor-phe`、`struc-ture` 已由 MD 正确合字。
- 备注：本页无 md 修复；V′ 后多冒号经 300dpi 独立确认为印刷原文自身 quirk，两轮旧审计均已登记、MD 忠实保留，维持不改。

## p.010（PDF p.10 / 印刷 p.9）
- PNG：/tmp/serregaga_audit_p010.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p010_300.png 及其切片 /tmp/p010_HxX2.png（ℋ_{x,X}）、/tmp/p010_HxX.png（𝒪_{x,X}）、/tmp/p010_XYh.png（(X×Y)^h 恒等式）、/tmp/p010_n6.png 与 /tmp/p010_n6b.png（n° 6 标题两行）、/tmp/p010_thetahat3.png（θ̂ : Ô_x → Ĥ_x）、/tmp/p010_prop3.png（PROPOSITION 3）、/tmp/p010_JxY.png（𝔍_x(Y) / 𝔍_x(Y,X)）
- 核对：正文页——页眉「GÉOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE」与印刷页码「9」、拓扑/ℋ_{x,X} 定义段（[3] exp. VIII）、X^h 约定段（dénombrable à l'infini）、性质列举段（(X×Y)^h = X^h × Y^h、Y^h 解析子集、coïncide、f holomorphe）、n° 6 标题、局部环比较段（𝒪_x、ℋ_x）、θ 同态段（θ(f)、θ : 𝒪_x → ℋ_x、θ̂ : Ô_x → Ĥ_x、Annexe n° 24）、PROPOSITION 3 陈述、𝔍_x(Y) 理想段（含 𝔍_x(Y,X) 与 X 区分）、页末断句「l'idéal de 𝒪_x」。
- 结果：PASS±（已修 1 处结构缺陷）。**修复项**：Markdown 行 153 的 n° 6 标题 `6. Relations entre l'anneau local d'un point et l'anneau des fonctions holomorphes en ce point.` 原为**普通段落**，印刷为与 n° 1–5 同式的**粗体节标题**（300dpi 裁片 `/tmp/p010_n6.png`、`/tmp/p010_n6b.png` 两行均可见明显加粗，与我在 p.004/p.005/p.008 逐页确认的 n° 1–5 标题字重一致）→ 已用 Edit 升为 `## 6. …`。**溯源**：非回归，`git show cpf-redo/Serre_1956_gaga^:…`（14aeb874）与原始导出 commit `4e5d9aab` 第 153 行均为普通段落，即 MinerU 导出即漏标；与前轮 Peer 已修的 n° 5（现为 `## 5.`）属同一类结构性漏标，本次补修。其余核对项全部吻合：`On définit la topologie comme la moins fine rendant continues`、`le sous-anneau analytique de $\mathcal{C}(\mathrm{X})_x$ engendré par $\mathcal{O}_{x,\mathrm{X}}$ (au sens de [3], exp. VIII)` 一致；**ℋ_{x,X} 与 𝒪_{x,X} 的第二下标**经裁片 `/tmp/p010_HxX2.png`、`/tmp/p010_HxX.png` 确认印刷为**小写斜体 x + 逗号 + 正体大写 X** → 行 145 的 `$\mathcal{H}_{x,\mathrm{X}}$`、`$\mathcal{O}_{x,\mathrm{X}}$` 正确；`$X^{h}$`、`topologie de $X^{h}$ est plus fine`、`localement compact dénombrable à l'infini` 一致；`Les propriétés suivantes résultent immédiatement de la définition de $X^{h}$ :` 一致；`(X × Y)^h = X^h × Y^h` 经 `/tmp/p010_XYh.png` 确认三处上标 h 与乘号、等号均对，与行 151 一致；`$Y^{h}$ est un sous-ensemble analytique de $X^{h}$`、`coïncide avec la structure analytique induite sur Y par $X^{h}$`、`$f: X \to Y$`、`$X^{h}$ dans $Y^{h}$` 一致；`Soit X une variété algébrique, et soit $x$ un point de X`、`l'anneau local $O_{x}$ des fonctions régulières sur X au point $x`、`l'anneau local $H_{x}$ des fonctions holomorphes sur $X^{h}$ au voisinage de $x` 一致；`$f\in\mathcal{O}_{x}$ définit un germe de fonction holomorphe en $x$, que nous désignerons par $\theta(f)$`、`$\theta:\mathcal{O}_{x}\to\mathcal{H}_{x}$`、`elle se prolonge donc par continuité en un homomorphisme`、`du complété de $\mathcal{O}_{x}$ dans celui de $\mathcal{H}_{x}$ (cf. Annexe, n° 24)` 一致；**θ̂ 同态**经 `/tmp/p010_thetahat3.png` 确认印刷为 `θ̂ : Ô_x → Ĥ_x`（θ 上带帽、两个花体字母上均带帽、两处下标 x）→ 行 157 的 `$\hat{\theta}:\hat{\mathcal{O}}_{x}\to\hat{\mathcal{H}}_{x}$` 正确；**PROPOSITION 3** 经 `/tmp/p010_prop3.png` 确认 `L'homomorphisme $\hat{\theta}:\hat{\mathcal{O}}_{x}\to\hat{\mathcal{H}}_{x}$ est bijectif.` 一致；`Nous démontrerons la proposition précédente en même temps qu'un autre résultat :` 一致；**𝔍_x(Y)** 经 `/tmp/p010_JxY.png` 确认印刷为 fraktur 𝔍_x(Y) 与 𝔍_x(Y, **X**) 两种形式（第二式含正体大写 X）→ 行 162 的 `\mathfrak{J}_{x}(\mathrm{Y})`（ou `\mathfrak{J}_{x}(\mathrm{Y},\mathrm{X})`）正确。差异（登记不改，均不误导，属全文性伪影类）：①行 155 的 `$O_{x}$`、`$H_{x}$` 用斜体 O/H，同句其余处用花体 `$\mathcal{O}_{x}$`/`$\mathcal{H}_{x}$`——印刷一律花体 𝒪/ℋ，属 mineru 花体拍平与混排的全文性伪影（同 p.006/p.007 类），不妨碍辨识，不单点改；②印刷斜体（`plus fine`、`dénombrable à l'infini`、`coïncide`、`Z-localement fermé`、PROPOSITION 3 陈述整段等）未标；③印刷正体 X/Y/U 与 MD `\mathrm{X}` 混排；④页眉与印刷页码「9」在 MD 无对应行；⑤页末签名标记「2」在 MD 无对应行（版面元素，非正文）；⑥印刷断行连字符 `fonc-tions`、`homomor-phisme` 已由 MD 正确合字。
- 修复登记：本页 1 处 md 结构修复（行 153 升 `## 6.` 标题），依据 300dpi 裁片 `/tmp/p010_n6.png`、`/tmp/p010_n6b.png`。

## p.011（PDF p.11 / 印刷 p.10）
- PNG：/tmp/serregaga_audit_p011.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p011_300.png 及其切片 /tmp/p011_disp1.png（显示式 f^r ∈ 𝔞.Ĥ_x = 𝔍_x(Y).Ĥ_x = 𝔍_x(Y).Ô_x.）、/tmp/p011_d2a.png 与 /tmp/p011_f1.png（第一分式 𝒪_x = 𝒪_{x,U}/𝔍_x(X,U)）、/tmp/p011_f2.png（第二分式 ℋ_x = ℋ_{x,U}/𝔩_x(X,U)）、/tmp/p011_Ieq_wide.png（𝔩_x(X, U) = θ̂(𝔍_x(X, U)) 的两个 fraktur 字母对比）、/tmp/p011_Czz.png（PROPOSITION 4 的 𝔍_x(Y)）、/tmp/p011_chev2.png（CHEVALLEY 段 𝔍_x(Y).Ô_x）、/tmp/p011_cap_zoom.png（𝔞.Ĥ_x ∩ ℋ_x = 𝔞 的带帽差异）、/tmp/p011_theta_line.png（L'application θ : 𝒪_x → ℋ_x）、/tmp/p011_Iline2.png（θ̂ : Ô_{x,U} → Ĥ_{x,U}）
- 核对：正文页——页眉「JEAN-PIERRE SERRE」与印刷页码「10」、𝔍_x(Y) 续段（[18] n° 39、𝒜_x(Y)）、PROPOSITION 4 陈述、C^n 特例段（Ô_x/Ĥ_x、C[[z_1,…,z_n]]、[1] n° 3、[3] exp. VI p. 6、[14] p. 278、[2] exp. XIV p. 3、[3] exp. VIII p. 9、r ≥ 0、f^r ∈ 𝔞）、显示式①、CHEVALLEY 段（[16] p. 40、[17] p. 67、intersection d'idéaux premiers、𝔍_x(Y).Ô_x、noethérien、𝔞.Ĥ_x ∩ ℋ_x = 𝔞、[15] Chap. IV / Annexe prop. 27）、一般情形段（sous-variété、U）、显示式②（𝒪_x 与 ℋ_x 两式）、θ 应用段（passage au quotient、θ̂ : Ô_{x,U} → Ĥ_{x,U}、bijectif、𝔩_x(X,U) = θ̂(𝔍_x(X,U))·ℋ_{x,U}、proposition 29 de l'Annexe）、页末断句。
- 结果：PASS±（已修 2 处 fraktur 字母错误）。**修复项（2 处）**：Markdown 行 177 显示式第一个分母与行 180 `θ(...)` 内的理想，原均作 `\mathfrak{I}`（𝔦）；印刷实为 fraktur **𝔍**（宽体圆碗 + 左侧长撇），证据 `/tmp/p011_f1.png`（第一分式分母清晰可辨为 𝔍）与 `/tmp/p011_Ieq_wide.png`（同行内 `θ̂(𝔍_x(X, U))` 的括号内字母为 𝔍，与左端字母明显不同）→ 已用 Edit 改为 `\mathfrak{J}`（两处）。**溯源**：非回归，`git show cpf-redo/Serre_1956_gaga^:…`（14aeb874）与原始导出 `4e5d9aab` 第 177/180 行均已是 `\mathfrak{I}`，即 MinerU 导出即误判。**登记不改项**：印刷在显示式②第二分母与等式左端另用 fraktur **𝔩**（窄体 + 横杠 + 钩状下伸，与 𝔍 字形明确不同），MD 该两处仍作 `\mathfrak{I}`——因标准 LaTeX/MathJax `\mathfrak` 无对应 𝔩 字形，改用其它字母会引入新的不实，故按 SOP 如实登记、不臆造字形；语义上该理想（解析侧）与其余 𝔍（代数侧）的区别已在本条登记。**其余核对项全部吻合**：`L'image de $\mathfrak{J}_{x}(\mathbf{Y})$ par $\theta$ est évidemment contenue dans l'idéal $\mathcal{A}_{x}(\mathbf{Y})$ de $\mathcal{H}_{x}$ défini au n° 3` 一致；**PROPOSITION 4** 经 `/tmp/p011_Czz.png` 确认 fraktur 𝔍_x(Y) 与行 166 一致；`car $\hat{\mathcal{O}}_{x}$ et $\hat{\mathcal{H}}_{x}$ ne sont autres que l'algèbre $\mathbb{C}[[z_{1},\ldots,z_{n}]]$ des séries formelles en $n$ indéterminées` 经 `/tmp/p011_Czz4.png` 确认**双括号完整**、首下标 1、末下标 n（**旧 mineru 曾丢双括号，前轮 Peer 修复与原页相符，本次复核维持**）；`soit a l'idéal de $\mathcal{H}_{x}$ engendré par $\mathfrak{J}_{x}(\mathbf{Y})$`、`Tout idéal de $\mathcal{H}_{x}$ définit un germe`、`cf. [1], n° 3 ou [3], exp. VI, p. 6`、`le germe défini par a n'est autre que Y`、`$\mathfrak{a}$`、`$\mathbb{C}[[z_{1},\ldots,z_{n}]]$`、`$\mathbb{C}[[z_{1},\ldots,z_{n}]]$ des séries formelles`、`$f^{r}\in\mathfrak{a}$` 一致；**显示式①**经 `/tmp/p011_disp1.png` 确认 `f^r ∈ 𝔞. Ĥ_x = 𝔍_x(Y). Ĥ_x = 𝔍_x(Y). Ô_x.`（两处 ℋ 均带帽、𝔍 两处、尾句点）→ 行 169 逐符对应；**CHEVALLEY 段**经 `/tmp/p011_chev2.png` 确认 `[17], p. 67`、`l'idéal 𝔍_x(Y).Ô_x`、行 172 的 `$\mathfrak{J}_x(\mathbf{Y})$. $\hat{\mathcal{O}}_x$` 三处一致；**交集式**经 `/tmp/p011_cap_zoom.png` 确认印刷为 `𝔞. Ĥ_x ∩ ℋ_x = 𝔞`——**首个 ℋ 带帽、第二个不带** → 行 172 的 `$\mathfrak{a}$. $\hat{\mathcal{H}}_x \cap \mathcal{H}_x = \mathfrak{a}$` 正确；`Puisque $\mathcal{H}_x$ est un anneau local noethérien`、`[15], Chap. IV, ou Annexe, prop. 27`、`$f \in \mathfrak{a}$` 一致；`X est une sous-variété d'un espace affine que nous désignerons par U. Par définition, on a :` 一致；**显示式②**经 `/tmp/p011_f1.png`、`/tmp/p011_f2.png` 确认两式分子分母下标（x,U）与参数 (X, U) 全对；`L'application $\theta: \mathcal{O}_x \to \mathcal{H}_x$ est obtenue par passage au quotient` 经 `/tmp/p011_theta_line.png` 确认为 θ（非 0）；`$\hat{\theta}: \hat{\mathcal{O}}_{x,\mathrm{U}} \to \hat{\mathcal{H}}_{x,\mathrm{U}}$ est bijectif` 经 `/tmp/p011_Iline2.png` 确认两端均带帽；`La proposition 3 en résulte immédiatement, en appliquant la proposition 29 de l'Annexe` 一致。差异（登记不改，均不误导）：①印刷 fraktur **𝔩**（解析侧理想）两处在 MD 仍作 `\mathfrak{I}`，理由如上，标准 LaTeX 无该字形，不臆造；②行 180 左端 `$\mathcal{A}_x(\mathrm{X}, \mathrm{U})$` 用花体 𝒜，而印刷同处为 fraktur 𝔩——花体/fraktur 拍平类伪影（同 p.006–p.008 类），登记不改；③印刷斜体（`d'intégrité`、`noethérien`、`isomorphe`、`théorème des zéros`、`A fortiori`、`sous-ensemble analytique` 等，及 PROPOSITION 4 陈述整段斜体）未标；④印刷正体 X/Y/U 与 MD `\mathrm{X}` 混排；⑤页眉与印刷页码「10」在 MD 无对应行；⑥印刷断行连字符 `cor-respondent`、`puis-que` 已由 MD 正确合字。
- 修复登记：本页 2 处 md 修复（行 177 第一分母分母、行 180 `θ(𝔍_x(X,U))` 内字母，均 `\mathfrak{I}`→`\mathfrak{J}`），依据 300dpi 裁片 `/tmp/p011_f1.png` 与 `/tmp/p011_Ieq_wide.png`。

## p.012（PDF p.12 / 印刷 p.11）
- PNG：/tmp/serregaga_audit_p012.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p012_300.png 及其切片 /tmp/p012_canonique.png（𝔩_x(Y,U) 与 θ(𝔍_x(Y,U)) 的字母对比）、/tmp/p012_n7.png（n° 7 标题）、/tmp/p012_injectif.png（COROLLAIRE 1）、/tmp/p012_cor2.png（COROLLAIRE 2）、/tmp/p012_cor3b.png 与 /tmp/p012_cor3c.png（COROLLAIRE 3 与 X^h）、/tmp/p012_prop5.png（PROPOSITION 5）、/tmp/p012_dou.png（d'où 𝔩_x(Y) = 0）、/tmp/p012_IxY0.png（Comme 𝔩_x(Y) contient θ(𝔍_x(Y))）
- 核对：正文页——页眉「GÉOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE」与印刷页码「11」、𝔩/𝔍 理想续段（canonique、θ(𝔍_x(Y,U))）、θ injectif 段（sous-anneau θ(𝒪_x)）、COROLLAIRE 1 陈述与证明句（[16]/prop. 28）、COROLLAIRE 2 陈述与说明句（[16] p. 26）、n° 4 结果引用句、COROLLAIRE 3 陈述（dimension r、X^h）、n° 7 标题、PROPOSITION 5 陈述、证明段（complémentaire、Z-fermée、adhérent、𝔩_x(Y) = 0、n° 6、θ(𝔍_x(Y))、prop. 3、𝔍_x(Y) = 0、Z-voisinage、cqfd）、Remarque 段、末段引出句。
- 结果：PASS±（已修 2 处）。**修复项（2 处）**：①Markdown 行 182 `$\theta(\mathfrak{I}_{x}(\mathbf{Y},\mathbf{U}))$` 原作 `\mathfrak{I}`，印刷为 fraktur **𝔍**——300dpi 裁片 `/tmp/p012_canonique.png` 同一行内左侧 `𝔩_x(Y, U)`（窄体钩状）与 `θ(𝔍_x(Y, U))` 括号内字母（宽体圆碗）字形明确不同 → 已用 Edit 改为 `\mathfrak{J}`。**溯源**：非回归，`git show cpf-redo/Serre_1956_gaga^:…`（14aeb874）与原始导出 `4e5d9aab` 第 182 行同为 `\mathfrak{I}`，即 MinerU 导出即误判。②Markdown 行 196 的 n° 7 标题 `7. Relations entre la topologie usuelle et la topologie de Zariski d'une variété algébrique.` 原为**普通段落**，印刷为与 n° 1–6 同式的**粗体节标题**（300dpi 裁片 `/tmp/p012_n7.png` 字重明显加粗，与我在 p.004/p.005/p.008/p.010 逐页确认的 n° 标题一致）→ 已用 Edit 升为 `## 7. …`。**溯源**：非回归，父提交与原始导出 `4e5d9aab` 第 196 行均已是普通段落（与本块 p.010 的 n° 6 同类结构性漏标）。**其余核对项全部吻合**：`canonique de l'idéal`、`lequel est engendré par`、`d'après ce qui précède` 一致；`La proposition 3 montre en particulier que $\theta: \mathcal{O}_x \to \mathcal{H}_x$ est injectif`、`d'identifier $\mathcal{O}_x$ au sous-anneau $\theta(\mathcal{O}_x)$ de $\mathcal{H}_x$`、`Compte tenu de cette identification, on a :` 一致；**COROLLAIRE 1** 经 `/tmp/p012_injectif.png` 确认 `Le couple d'anneaux ($\mathcal{O}_{x}$, $\mathcal{H}_{x}$) est un couple plat (au sens de l'Annexe, déf. 4)` 一致，`C'est une conséquence immédiate de la proposition 3 et de la proposition 28 de l'Annexe.` 一致；**COROLLAIRE 2** 经 `/tmp/p012_cor2.png` 确认 `Les anneaux $\mathcal{O}_{x}$ et $\mathcal{H}_{x}$ ont même dimension`、`la dimension d'un anneau local noethérien est égale à celle de son complété (cf. [16], p. 26)` 一致；`Compte tenu des résultats énoncés au n° 4, on obtient le résultat suivant (où nous supposons X irréductible pour simplifier l'énoncé) :` 一致；**COROLLAIRE 3** 经 `/tmp/p012_cor3b.png`、`/tmp/p012_cor3c.png` 确认 `Si X est une variété algébrique irréductible de dimension r, l'espace analytique $X^{h}$ est de dimension analytique r en chacun de ses points`（上标 h 与两处 r 均对）一致；**PROPOSITION 5** 经 `/tmp/p012_prop5.png` 确认 `Soient X une variété algébrique, et U une partie de X. Si U est Z-ouverte et Z-dense dans X, alors U est dense dans X.` 一致；**证明段**经 `/tmp/p012_dou.png`、`/tmp/p012_IxY0.png` 确认 `Soit Y le complémentaire de U dans X; c'est une partie Z-fermée de X`、`si x n'était pas adhérent à U, on aurait Y = X au voisinage de x, d'où 𝔩_x(Y) = 0, avec les notations du n° 6`、`Comme 𝔩_x(Y) contient θ(𝔍_x(Y)), et que θ est injectif (prop. 3), on aurait alors 𝔍_x(Y) = 0`、`Y = X dans un Z-voisinage de X`、`contrairement à l'hypothèse que U est Z-dense dans X, cqfd` 全部一致，且行 200 的两处 𝔍（`$\theta(\mathfrak{J}_{x}(\mathbf{Y}))$`、`$\mathfrak{J}_{x}(\mathbf{Y}) = 0$`）已正确为 `\mathfrak{J}`；`Remarque. — On voit facilement que la proposition 5 équivaut au fait que $\theta : \mathcal{O}_x \to \mathcal{H}_x$ est injectif`、`démontrer par réduction au cas d'une courbe` 一致；`Nous allons maintenant donner deux applications simples de la proposition 5.` 一致。差异（登记不改，均不误导）：①印刷 fraktur **𝔩**（解析侧理想）在本页三处（行 182 的 `$\mathcal{A}_{x}(\mathbf{Y},\mathbf{U})$`、行 200 的两处 `$\mathcal{A}_{x}(\mathbf{Y})$`）在 MD 作花体 `\mathcal{A}`——fraktur/花体拍平类伪影（同 p.006–p.008 及 p.011 同类），登记不改；②印刷斜体（`injectif`、`couple plat`、`même dimension`、`Z-ouverte`、`Z-dense`、`Z-fermée`、`équivaut`、`cqfd` 等词条内斜体，及三条 COROLLAIRE 与 PROPOSITION 5 陈述整段斜体）未标；③页眉与印刷页码「11」在 MD 无对应行；④印刷断行连字符 `simpli-fier`、`analy-tique`、`signe-rait`、`élémen-taire`、`démon-trer` 已由 MD 正确合字。
- 修复登记：本页 2 处 md 修复（行 182 `θ(𝔍_x(Y,U))` 内字母 `\mathfrak{I}`→`\mathfrak{J}`，依据 `/tmp/p012_canonique.png`；行 196 升 `## 7.` 标题，依据 `/tmp/p012_n7.png`）。

## p.013（PDF p.13 / 印刷 p.12）
- PNG：/tmp/serregaga_audit_p013.png（pngmono 150dpi）；仲裁裁片 /tmp/serregaga_audit_p013_300.png 及其切片 /tmp/p013_prop6.png（PROPOSITION 6）、/tmp/p013_chow.png（CHOW 小型大写）、/tmp/p013_graphe.png（graphe T / f: U→X）、/tmp/p013_recip.png（X × Y 倒证段）、/tmp/p013_lem2.png（LEMME 2）、/tmp/p013_Uj.png（U_j ⊂ f(X_j)）、/tmp/p013_union.png（Y_k, k∈J, k≠j）、/tmp/p013_union2.png（U = ∪_{j∈J} U_j）、/tmp/p013_prop7.png（PROPOSITION 7）
- 核对：正文页——页眉「JEAN-PIERRE SERRE」与印刷页码「12」、PROPOSITION 6 陈述（complète/compacte）、CHOW 结果段（[7]、[19] n° 4、variété projective Y、Z-ouverte/Z-dense、f: U → X surjective、graphe T、Z-fermé dans X × Y、U = Y ssi X complète）、双向证明段（X = f(Y)、projective compacte、Réciproquement、projection de T dans Y、proposition 5）、CHEVALLEY 归属句、LEMME 2 陈述、一般情形归约段（X_i, i≤I、Y_i、Z-adhérence、Y = ∪Y_i、J ⊂ I、Y_j j∈J、U_j ⊂ f(X_j)、Z-ouverte/Z-dense dans Y_j、Y_k k∈J k≠j、U = ∪_{j∈J} U_j、propriétés requises）、PROPOSITION 7 陈述、证明段起首（lemme 2、T、U ⊂ f(X)）。
- 结果：PASS±。全部核对项与原页吻合，无缺陷需改。逐项：`PROPOSITION 6. — Pour qu'une variété algébrique X soit complète, il faut et il suffit qu'elle soit compacte.` 经 `/tmp/p013_prop6.png` 逐词确认一致；`Rappelons d'abord un résultat de CHOW (cf. [7], ainsi que [19], n° 4)` 一致；`pour toute variété algébrique X, il existe une variété projective Y, une partie U de Y, Z-ouverte et Z-dense dans Y` 一致；**graphe T 句**经 `/tmp/p013_graphe.png` 确认印刷为 `et une application régulière surjective f : U → X dont le graphe T soit Z-fermé dans X × Y. On a U = Y si et seulement si X est complète.` → 行 208 一致；证明段 `Ceci étant, supposons d'abord X complète; on a alors $X = f(Y)$`、`comme toute variété projective est compacte pour la topologie usuelle, on en conclut bien que X est compacte`、`Réciproquement, supposons X compacte` 经 `/tmp/p013_recip.png` 确认为 `même de T qui est fermé dans X × Y, donc de U puisque c'est…` 一致，`la proposition 5 montre que U = Y, ce qui achève la démonstration` 一致；`Le lemme suivant est essentiellement dû à CHEVALLEY :` 一致（大写与印刷一致）；**LEMME 2** 经 `/tmp/p013_lem2.png` 确认 `LEMME 2. — Soit $f\colon X\to Y$ une application régulière d'une variété algébrique X dans une variété algébrique Y, et supposons que $f(X)$ soit Z-dense dans Y. Il existe alors une partie $U\subset f(X)$ qui est Z-ouverte et Z-dense dans Y.` 逐词一致；一般情形段 `Lorsque X et Y sont irréductibles, ce résultat est bien connu, cf. [4], exp. 3 ou [17], p. 15`、`$\mathbf{X}_i$, $i \in \mathbf{I}$`、`la Z-adhérence de $f(\mathbf{X}_i)$ dans Y`、`$\mathbf{Y} = \cup \mathbf{Y}_i$`、`$\mathbf{J} \subset \mathbf{I}$`、`$\mathbf{Y}_j$, $j \in \mathbf{J}$`、`pour tout $j \in \mathbf{J}$` 一致；**U_j ⊂ f(X_j)** 经 `/tmp/p013_Uj.png` 确认印刷为 `une partie U_j ⊂ f(X_j) qui est Z-ouverte et Z-dense`（粗体 X_j 下标）→ 行 216 的 `$\mathbf{U}_j \subset f(\mathbf{X}_j)$` 一致；**Y_k, k∈J, k ≠ j** 经 `/tmp/p013_union.png` 确认 `tre aucun des Y_k, k∈J, k ≠ j. En posant`（粗体 Y_k、斜体 k）一致；**并集式**经 `/tmp/p013_union2.png` 确认印刷为 `U = ⋃_{j∈J} U_j`（大号并号 + 下标 j∈J + U_j）→ 行 216 的 `$\mathbf{U} = \bigcup_{j \in \mathbf{J}} \mathbf{U}_j$` 逐符对应；`on obtient un sous-ensemble de Y qui jouit de toutes les propriétés requises` 一致；**PROPOSITION 7** 经 `/tmp/p013_prop7.png` 确认 `Si $f\colon X \to Y$ est une application régulière d'une variété algébrique X dans une variété algébrique Y, l'adhérence et la Z-adhérence de $f(X)$ dans Y coïncident` 一致；`Soit T la Z-adhérence de $f(X)$ dans Y. En appliquant le lemme 2 à $f\colon X\to T$, on voit qu'il existe une partie $U\subset f(X)$` 一致。差异（登记不改，均不误导）：①印刷小型大写 **CHOW**（Rappelons d'abord un résultat de CHOW）在 MD 作 `Chow`——小型大写规范化（同 p.002/p.003 同类，词形正确，300dpi 裁片 `/tmp/p013_chow.png` 确认为大 C + 小 HOW）；②印刷 `U_j`、`X_j`、`Y_j`、`Y_k`、`X_i`、`Y_i`、`J`、`I`、`U` 在 MD 用 `\mathbf{}` 加粗，与印刷粗体一致（此项一致，非差异）；③印刷斜体（`Z-ouverte`、`Z-dense`、`Z-fermé`、`régulière surjective`、`irréductibles`、`complète`、`compacte`、`coïncident`、`a fortiori` 等词条内斜体，及 PROPOSITION 6 / LEMME 2 / PROPOSITION 7 三段陈述整段斜体）未标——mineru 已知拍平；④页眉与印刷页码「12」在 MD 无对应行；⑤印刷断行连字符 `simpli-fier`、`démons-tration`（实为 `démontra-tion`）等已由 MD 正确合字。
- 备注：本页无 md 修复；本页与 p.011/p.012 同篇内 fraktur 𝔍/𝔩 区分的延续（X_i、Y_i、U_j 均为粗体正体字母，非 fraktur），与该区分无冲突，已逐处核对。
