# Freedman 1982 · The topology of four-dimensional manifolds

- Actor: `Peer-P39`
- Model / effort: `gpt-6-luna / max`
- Role: contributor; `Master-Luna` is the sole canonical integrator.
- Base: `037602429d3b009f6fc468c732073eb3ddf9875f` (main at dispatch; this worktree is detached at the same OID).
- PDF: `1986年 - Freedman/Freedman_1982_topology_4manifolds.pdf` (98 pages; Creator `ABBYY FineReader`; each page contains a full-page 600 dpi CCITT image and an OCR text layer). Audited as a scanned paper: render and inspect every PDF page at 150 dpi; use higher-resolution crops when a glyph remains uncertain.
- MinerU Markdown: `1986年 - Freedman/Freedman_1982_topology_4manifolds_mineru/Freedman_1982_topology_4manifolds__Freedman_1982_topology_4manifolds.md`
- Original Markdown SHA-256: `f8be278a441d83611b80b6fd2ab620dde07d3d4597ec37c23138478591a4e2bf`
- Scope: transcription fidelity against the printed pages. This audit does not certify the mathematical correctness of the paper's arguments.

## Page ledger

### 2026-10-01 20:09 UTC · PDF p.1/98 · print p.357
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p001.png` (pngmono 150 dpi)
- Markdown: opening title, author, dedication, Introduction through the broken phrase “link theoretic,” and footnotes 1–3 (current source lines 1–19).
- Checked: title, author, journal/volume/page header, opening prose, displayed handle notation, dedication, received/funding note, and footnotes 1–3 against the page image.
- Result: **PASS±** — title, author, body text, displayed notation, dedication, and footnotes 1–3 agree with print. The printed running header `J. Differential Geometry 17 (1982) 357–453` and print page number `357` are omitted from the MinerU Markdown; recorded as a layout/header omission, with no mathematical body-text correction made.

### 2026-10-01 20:11 UTC · PDF p.2/98 · print p.358
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p002.png` (pngmono 150 dpi)
- Markdown: continuation of the Introduction and footnotes 4–5 (current source lines 21–31).
- Checked: continuation from “or otherwise,” the Casson-handle comparison, the 1978 reimbedding statement, the parametrization/homeomorphism sequence, the concluding acknowledgement, and footnotes 4–5.
- Result: **PASS±** — body text and mathematical notation checked against the 150 dpi page image; no content-level omission or transcription error found. Running head/name and print page number `358` are omitted; `Siebenmann's[46]` also lacks the source's separating space.

### 2026-10-01 20:12 UTC · PDF p.3/98 · print p.359
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p003.png` (pngmono 150 dpi)
- Markdown: final acknowledgements and paper-organization paragraph, followed by the complete table of contents (current source lines 33–53).
- Checked: seminar dates, acknowledgements, theorem/section references, section titles, mathematical notation in the contents, and printed page references 357–435.
- Result: **PASS±** — body and all eleven table-of-contents entries agree with the page image. Running title and print page number `359` are omitted from the Markdown.

### 2026-10-01 20:15 UTC · PDF p.4/98 · print p.360
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p004.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p004_theorem31.png` (300 dpi crop) and `audit/300dpi/Freedman_1982_topology_4manifolds_p004_theorem31_detail.png` (600 dpi source-render crop used to resolve the theorem symbols)
- Markdown: end of the introductory overview and §1 through the Casson-handle definition (current source lines 55–69).
- Checked: unsolved-problems paragraph, §1 heading, theorem references, Casson Theorem 3.1 and surrounding Casson-handle description.
- Result: **FAIL** — Theorem 3.1's map is materially corrupted in Markdown line 65. Print shows the barred `d` map with the Π-shaped finite-disjoint-union glyphs, an embedding arrow into `(M, ∂)`, and the corresponding boundary-union notation. Markdown instead has `II` for those glyphs, `\Leftrightarrow` for the arrow, and `(M_1\partial)` for `(M, \partial)`. The surrounding prose agrees. Repair is deferred until all 98 pages have been audited.

### 2026-10-01 20:16 UTC · PDF p.5/98 · print p.361
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p005.png` (pngmono 150 dpi)
- Markdown: discussion of the six-stage bound, Theorem 1.1, the flex approximation discussion, Addendum A, and footnote 6 (current source lines 69–83).
- Checked: theorem statement and handle-pair notation, the maps and exceptional set in the approximation discussion, Addendum A, and the complete Gompf footnote.
- Result: **FAIL** — The printed footnote has a single `Wh_4` occurrence within footnote 6. Markdown contains the complete footnote at line 83 and also an isolated extra `Wh_4` block at line 81, not present as a separate item on the print page. Record for post-audit removal. The surrounding theorem, prose, and footnote text otherwise agree; running title and print page number `361` are omitted.

### 2026-10-01 20:18 UTC · PDF p.6/98 · print p.362
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p006.png` (pngmono 150 dpi)
- Markdown: Addendum A proof, Diagram 1.1, and the replacement quotient-map display (current source lines 85–100).
- Checked: smooth-cellularity argument and tower notation, the `CH/G` quotient discussion, the `S^1 × [0, ∞)` annulus, both linked MinerU diagram crops against the printed Diagram 1.1, and the displayed quotient-map arrows.
- Result: **PASS±** — prose, equation, and both diagram components agree with the 150 dpi source page. The printed running header/name and page number `362` are omitted.

### 2026-10-01 20:21 UTC · PDF p.7/98 · print p.363
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p007.png` (pngmono 150 dpi)
- Markdown: continuation of the Addendum A diagram argument, Theorems 1.2–1.3, and the opening proof of Theorem 1.2 (current source lines 103–119).
- Checked: the linked MinerU commutative diagram against the printed diagram, the homeomorphism argument, both theorem statements, boundary pairs, and the proof through the flatly embedded 2-handles.
- Result: **FAIL** — Markdown line 111 writes the source pair `(M^4, ∂)` as `(M^4∂)`, omitting the separating comma in the domain of `f`; print p.363 clearly includes the comma. This damages the theorem's displayed domain notation. The surrounding text agrees; running title and print page number `363` are omitted.

### 2026-10-01 20:22 UTC · PDF p.8/98 · print p.364
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p008.png` (pngmono 150 dpi)
- Markdown: verification of Theorem 1.2's addendum, proof of Theorem 1.3 through Diagram 1.2 (current source lines 121–131).
- Checked: hyperbolic-basis and Hopf-link notation, the flat 3-spheres and 4-cell construction, the normal-bordism fill-in, Whitney-trick paragraph, intersection count, and the linked Diagram 1.2 asset against the print image.
- Result: **PASS±** — text, formulas, and Diagram 1.2 agree. The print's phrase “ascending the descending manifolds” is retained literally. Running header/name and print page number `364` are omitted.

### 2026-10-01 20:23 UTC · PDF p.9/98 · print p.365
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p009.png` (pngmono 150 dpi)
- Markdown: Diagram 1.3 and its conclusion, Corollary 1.1, and Theorem 10.3 (current source lines 133–145).
- Checked: linked Diagram 1.3 against the print image, the boundary-connected-sum description and handle attachments, the intersection class `(p,q)`, and the proper h-cobordism statement.
- Result: **PASS±** — diagram, prose, and theorem/corollary statements agree. The prose uses plain `N` where print uses a fraktur neighborhood symbol; this is a notation-style loss without an identified content change. Running title and print page number `365` are omitted.

### 2026-10-01 20:25 UTC · PDF p.10/98 · print p.366
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p010.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p010_corollary12.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p010_embedding_theorem.png`, and `audit/300dpi/Freedman_1982_topology_4manifolds_p010_embedding_arrows.png` (300 dpi crops)
- Markdown: Corollary 1.2 and proof, the proof of Theorem 1.4, Theorem 1.4, its note, and the final embedding-separation paragraph (current source lines 147–159).
- Checked: the proper-homotopy equivalence notation and hypotheses, smoothing/h-cobordism argument, punctured homology-sphere construction, compactified embedding, and final separation statement.
- Result: **FAIL** — Markdown lines 153 and 159 use `\leftrightarrow` where print p.366 has one-way embedding/map arrows (`\hookrightarrow` for the compactified flat embedding and `\to` in the `P^-`/`\Sigma^-` separation sentence). The two-headed symbols change the relation. The high-resolution crops confirm the print glyphs. The `\rho`/congruence decoration in Corollary 1.2 agrees with print. Running header/name and page number `366` are omitted.

### 2026-10-01 20:27 UTC · PDF p.11/98 · print p.367
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p011.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p011_rochlin_mod8.png` (300 dpi crop)
- Markdown: Theorem 1.4′, Corollary 1.3 and its connected-sum proof, Corollary 1.3′ Steps 1–2 (current source lines 161–177).
- Checked: the double of the contractible 4-manifold, proper h-cobordism classes, mod-8 Rochlin calculation, end compactification and Schoenflies argument, and the flat-arc outline.
- Result: **PASS±** — formulas and prose match the page. The print spellings `Rochin` and `interiors/16 integers` are reproduced literally in Markdown and are recorded as source-level quirks; they are not corrected. Running header/name and print page number `367` are omitted.

### 2026-10-01 20:29 UTC · PDF p.12/98 · print p.368
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p012.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p012_step3.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p012_step4.png`, and `audit/300dpi/Freedman_1982_topology_4manifolds_p012_step4_text.png` (300 dpi crops)
- Markdown: Corollary 1.3′ outline Steps 3–4, Diagram 1.4, Definition 1.1, Theorem 1.5 and its existence/uniqueness statement, and the opening of its existence proof (current source lines 179–201).
- Checked: both linked Diagram 1.4 components against print, the `[01]` interval as printed, the boundary/thickening notation, intersection-form map, parity clauses, and the plumbing setup.
- Result: **PASS±** — no substantive text or formula mismatch found. Print itself shows `[01]` without a comma, faithfully reproduced in Markdown; the Step 4 possessive after `∂(Δ × [0,1])` is split outside the inline math delimiters in Markdown, a minor formatting defect without a changed statement. Running header/name and print page number `368` are omitted.

### 2026-10-01 20:31 UTC · PDF p.13/98 · print p.369
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p013.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p013_plumbing.png` (300 dpi crop)
- Markdown: completion of the existence proof for Theorem 1.5, including the classifying-map lift diagram, then the uniqueness proof through its vanishing obstruction group (current source lines 203–219).
- Checked: plumbing cap and Mayer–Vietoris argument, both linked lift/fibration diagrams, the (H^4(W,\partial W;Z_2)) obstruction display, and the suspension isomorphism chain.
- Result: **PASS±** — the prose, displays, and linked diagrams match. Print appears to use a capital `W` in “intersection form W” after first naming the pairing `ω`; Markdown preserves that source glyph as a print-level quirk. No correction made. Running title and print page number `369` are omitted.

### 2026-10-01 20:33 UTC · PDF p.14/98 · print p.370
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p014.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p014_indefinite_form.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p014_chern_sum.png` (300 dpi crops)
- Markdown: end of the uniqueness proof for Theorem 1.5, even and odd form cases, Chern-manifold construction, nonsmoothability argument, and start of the definite odd case (current source lines 221–231).
- Checked: proper h-cobordism product, spin/Kirby–Siebenmann formula, odd indefinite quadratic-form decomposition, Chern construction, and the resulting connected-sum expressions.
- Result: **FAIL** — Markdown line 225 omits the closing parenthesis after the first `#_{n copies}(P^2)` group in the displayed model `H`; the printed p.370 formula closes that summand before the next `#`. The expression is therefore unbalanced in Markdown. The remaining checked statements match print; running header/name and page number `370` are omitted.

### 2026-10-01 20:35 UTC · PDF p.15/98 · print p.371
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p015.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p015_addendum.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p015_domain.png` (300 dpi crops)
- Markdown: definite odd-form construction, Theorem 1.5 Addendum, Theorem 1.6 with proof/note, Theorem 1.7, and the lead-in to Corollary 1.4 (current source lines 231–249).
- Checked: the Rochlin/Arf formula, self-homeomorphism addendum, 4-dimensional Poincaré statement, relative contractible-manifold note, and the `E_8` existence statement.
- Result: **PASS±** — the checked statements and formulas agree. Print writes `M_m \setminus pt` in the addendum immediately after `M_ω`; MinerU reproduces that visible subscript inconsistency and it is retained as a source-level quirk. Running title and print page number `371` are omitted.

### 2026-10-01 20:36 UTC · PDF p.16/98 · print p.372
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p016.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p016_kummer_form.png` (300 dpi crop)
- Markdown: Corollaries 1.4–1.6, Theorems 1.8–1.10 and their stated proof passages (current source lines 251–269).
- Checked: transversality exceptions, the `E_8` obstruction and homology group, homology-sphere link argument, quartic Kummer equation and intersection-form decomposition, and the non-straightenable handle statement.
- Result: **PASS±** — all checked text and notation match. Print writes the K-S obstruction group as `H_4(|E_8|; Z_2)` and spells the cited name `Siebermann`; Markdown preserves both source forms. Running header/name and print page number `372` are omitted.

### 2026-10-01 20:39 UTC · PDF p.17/98 · print p.373
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p017.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p017_cech.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p017_smoothing_symbol.png`, and `audit/300dpi/Freedman_1982_topology_4manifolds_p017_s3_end.png` (300 dpi crops)
- Markdown: Theorem 1.11 and proof, Theorem 1.12 and proof, and the opening knot-concordance paragraph (current source lines 271–281).
- Checked: Čech-homology spelling, tameness and cellularity conditions, the smoothing symbol `V_Γ`, the end-collar statement, and the final (S^3\times[0,\infty)) term.
- Result: **FAIL** — Markdown line 281 writes `S_3` where print p.373 has superscript `S^3` in the standard-end term; the 300 dpi crop confirms the superscript and the distinction changes the referenced space. Markdown spells `Cêch` rather than print's Čech accent; noted as a minor orthographic difference. Running title and print page number `373` are omitted.

### 2026-10-01 20:41 UTC · PDF p.18/98 · print p.374
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p018.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p018_pi1.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p018_theorem14.png` (300 dpi crops)
- Markdown: continuation of the knot-concordance paragraph, Theorems 1.13–1.14, and the opening of §2 “Handle calculus” through the sentence ending at “linking” (current source lines 283–303).
- Checked: contractible-manifold transition, both knot boundary maps, Theorem 1.13's meridian-group condition, Theorem 1.14's untwisted-double label and handle pair, and the §2 handle-body description.
- Result: **FAIL** — Markdown line 289 omits the closing parenthesis in `π₁(B⁴ − k̄(B²)) ≅ Z`; print p.374 closes the complement before `≅ Z`. Markdown line 291 also omits the printed `D(k)` label above the map `S¹ → S³` in Theorem 1.14. Both alter displayed statement notation. The surrounding prose and handle pair agree; running header/name and page number `374` are omitted.

### 2026-10-01 20:42 UTC · PDF p.19/98 · print p.375
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p019.png` (pngmono 150 dpi)
- Markdown: continuation of the handle-body notation and conventions, Example 0, and Example 1 through the positive/negative self-plumbing maps (current source lines 301–313).
- Checked: attaching-map and framing notation, unlink slice, bold/dashed diagram conventions, the Example 0 empty-link circle, and the two complex-coordinate plumbing identifications.
- Result: **PASS±** — prose, formulas, and the linked empty-link diagram agree with the source page. Running title and print page number `375` are omitted.

### 2026-10-01 20:44 UTC · PDF p.20/98 · print p.376
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p020.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p020_kinky_finite.png` (300 dpi crop)
- Markdown: Diagram 2.1 and Diagram 2.2 descriptions, the absolute-space/pair classification of kinky handles, and the opening geometric description of `(k, ∂⁻k)` (current source lines 313–335).
- Checked: both self-plumbing formulas, all four linked components of Diagrams 2.1–2.2 against print, the positive/negative kink counts, the boundary-linking definition, and the cautionary identification.
- Result: **FAIL** — Markdown line 325 transcribes the printed `\natural_{finite}` boundary-connected-sum symbol as `\mathbb{H}_{finite}` in the absolute-space description. The 300 dpi crop confirms the source glyph. The other checked prose and diagrams agree; running title and print page number `376` are omitted.

### 2026-10-01 20:46 UTC · PDF p.21/98 · print p.377
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p021.png` (pngmono 150 dpi)
- Markdown: completion of the core/attaching-region linking definition, the caution on the noncanonical boundary identification, the kinky-handle attachment convention, and Diagram 2.3 with the Hopf-link observation (current source lines 335–359).
- Checked: signed linking-number definition, `2 × (self plumbing counted by sign)`, the `1-handle pair` description, all three linked Diagram 2.3/inline Hopf-link assets against the page image, and the distinguished-torus equations.
- Result: **PASS±** — text, formulas, and linked figures agree with print. Running title and print page number `377` are omitted.

### 2026-10-01 20:50 UTC · PDF p.22/98 · print p.378
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p022.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p022_clasp_pair.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p022_clasp_figures.png`, and `audit/300dpi/Freedman_1982_topology_4manifolds_p022_clasp_symbols_tight.png` (300 dpi crops)
- Markdown: continuation of the Diagram 2.4 discussion, the clasp-sign sentence, Diagram 2.5, the multi-kink construction, and the tower definitions (current source lines 361–375).
- Checked: both linked main diagrams against print, the two sign-dependent clasp sketches, the boundary-connected-sum formula, and the one-/multi-stage tower definitions.
- Result: **FAIL** — Markdown line 365 substitutes two `\varnothing` symbols for the two small printed clasp diagrams that distinguish the positive and negative self-plumbing. The print crop shows the distinct clasp crossings; those figures are absent from the Markdown at this sentence. The surrounding linked Diagrams 2.4–2.5 and definitions agree. Running header/name and print page number `378` are omitted.

### 2026-10-01 20:52 UTC · PDF p.23/98 · print p.379
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p023.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p023_tower_indices.png` (300 dpi crop) and `audit/300dpi/Freedman_1982_topology_4manifolds_p023_tower_indices_detail.png` (600 dpi source-render crop)
- Markdown: Diagram 2.6, mapping-cylinder description, core/stage-index definitions, and the start of the Morse-cancellation discussion (current source lines 379–393).
- Checked: the linked Diagram 2.6 asset, boundary maps and indices, the range `0 ≤ i ≤ q − p − 1`, the stage formula, and the cancellation setup through the page break.
- Result: **PASS±** — text and Diagram 2.6 agree. Print itself reads `\overline{T_q - T_q}` in the interval defining the stage cores, and Markdown preserves that source notation; it is recorded as a print-level quirk without correction. Running title and print page number `379` are omitted.

### 2026-10-01 20:54 UTC · PDF p.24/98 · print p.380
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p024.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p024_tower_inclusions.png` (300 dpi crop)
- Markdown: end of the 1/2-handle cancellation setup, Rule, Diagrams 2.7–2.8, the cancellation isomorphism lead-in, and definition of the Casson-handle inclusion sequence (current source lines 395–415).
- Checked: the transverse-disk setup, twist/clasp cancellation steps, linked cancellation diagrams, attaching-map formula, and directed tower-inclusion arrows.
- Result: **FAIL** — Markdown line 415 uses `\Leftrightarrow` for both tower sequences, but print p.380 has one-way inclusion arrows `\to` throughout. Replacing the directed inclusions by two-headed arrows changes the stated construction. The 300 dpi crop confirms the source arrows; running header/name and page number `380` are omitted.

### 2026-10-01 20:58 UTC · PDF p.25/98 · print p.381
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p025.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p025_Hn_symbol.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p025_Hn_symbol_detail.png`, and `audit/300dpi/Freedman_1982_topology_4manifolds_p025_theorem31.png` (300 dpi crops)
- Markdown: Casson-handle definition closure, Theorem 2.1 and its zero-framing statement, §3 heading, Theorem 3.1, and its addendum (current source lines 417–435).
- Checked: the finite boundary-connected-sum symbol in `H_n`, the nested smooth-ball argument, the standard-handle pair, Theorem 3.1's map/domain/boundary symbols, and the “births of pairs of double points” addendum.
- Result: **FAIL** — Markdown line 421 uses `\mathfrak{h}` where print p.381 has `\natural` before the finite-copy term in `H_n`. Markdown line 431 repeats the Theorem 3.1 corruption recorded on p.4: print's union glyphs and embedding arrow are transcribed as `II` and `\Leftrightarrow`. The high-resolution crops confirm both mismatches. Running header/name and print page number `381` are omitted.

### 2026-10-01 21:01 UTC · PDF p.26/98 · print p.382
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p026.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p026_natural_section.png` (300 dpi crop) and `audit/300dpi/Freedman_1982_topology_4manifolds_p026_normal_section_detail.png` (600 dpi source-render crop)
- Markdown: Lemma 3.1 and its definition, note, terminology and addendum, plus the first half of the Whitney-disk proof (current source lines 437–459).
- Checked: the π₁-negligibility map, algebraic-dual intersection data, paired-point conditions, the normal-section formula, and the four listed Whitney-disk circumstances.
- Result: **FAIL** — Markdown line 453 gives the normal-subbundle term as `∂Θ ↔ x`; print p.382 shows lower-case `∂θ → x`. Both the Greek letter and arrow differ in the natural-section formula. The 600 dpi crop resolves the glyphs. Running header/name and print page number `382` are omitted.

### 2026-10-01 21:30 UTC · PDF p.27/98 · print p.383
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p027.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p027_theorem32.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p027_delta_map.png` (300 dpi crops)
- Markdown: end of Lemma 3.1 proof, Theorem 3.2 statement and notes, and the opening of its proof (current source lines 461–473).
- Checked: Whitney-circle cancellation conclusion, boundary map and disjoint-union notation in Theorem 3.2, tower inclusions, and the first immersed-disk map into (M_3).
- Result: **FAIL** — Markdown line 463 changes the printed one-way arrow in (f_i:(D^2,\partial)\to(M_1^4,\partial M_1)) to `\Leftrightarrow`, and misrenders the repeated finite disjoint-union glyph as `II`. Line 473 likewise writes `\Delta \leftrightarrow M_3` where print has the one-way map arrow `\Delta \to M_3`. These changes alter the maps/unions in the theorem statement and proof; the 300 dpi crops confirm the source notation. Running header/name and print page number `383` are omitted.

### 2026-10-01 21:58 UTC · PDF p.28/98 · print p.384
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p028.png` (pngmono 150 dpi)
- Markdown: continuation of the five-step tower construction proof, Diagram 3.1, the framing formula, geometric-dual step, and conclusion of Theorem 3.2 (current source lines 475–497).
- Checked: both linked Diagram 3.1 images, the Euler/framing change, the μ(τ) Wall-form condition, the half-framing correction, and final π₁-negligibility domain.
- Result: **PASS±** — prose, formulas, and both diagrams agree with print. Running title and print page number `384` are omitted.

### 2026-10-01 22:27 UTC · PDF p.29/98 · print p.385
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p029.png` (pngmono 150 dpi)
- Markdown: Addendum to Theorem 3.2, §4 reimbedding-theorem introduction, notation for tower/core ranges, and Theorems 4.1–4.3 (current source lines 499–525).
- Checked: the π₁-negligibility hypotheses/conclusion, tower-stage indices, core unions, theorem agreement/nullity conditions, and the no-linking clause.
- Result: **PASS±** — checked formulas and surrounding prose agree with print. Running title/name and print page number `385` are omitted.

### 2026-10-01 23:08 UTC · PDF p.30/98 · print p.386
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p030.png` (pngmono 150 dpi)
- Markdown: Theorem 4.4, the fundamental-group generator conventions, and Diagrams 4.1–4.2 (current source lines 529–547).
- Checked: the (T_7\subset T_6) conditions, free-group loop-intersection word description, (X/Y) dual-generator system, and both linked diagrams against print.
- Result: **PASS±** — formulas, prose, and diagrams agree. Running header/name and print page number `386` are omitted.

### 2026-10-01 23:43 UTC · PDF p.31/98 · print p.387
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p031.png` (pngmono 150 dpi)
- Markdown: Lemma 4.1 and handle-body calculation, Diagram 4.3 discussion, and the time-slice description of Diagram 4.4 (current source lines 549–575).
- Checked: the free-group/inclusion assertion, handle moves and zero-framing condition, the role of the distinguished solid tori, and all four linked diagram images against the printed page.
- Result: **PASS±** — mathematical prose and referenced diagrams agree. Running title/name and print page number `387` are omitted.

### 2026-10-02 00:09 UTC · PDF p.32/98 · print p.388
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p032.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p032_inclusion_sequence.png` (300 dpi crop)
- Markdown: final injectivity check for Lemma 4.1, Lemma 4.2 and its proof, proofs of Theorems 4.1–4.2, and the beginning of the Theorem 4.3 construction (current source lines 577–589).
- Checked: null-homotopy/injectivity arguments, distinguished-torus algebraic dual, commutator calculation, and the inclusion sequence defining the successive towers.
- Result: **FAIL** — Markdown line 589 uses double-headed arrows between `T_4^w`, intermediate towers, and `T_4^0`; print p.388 has single directed inclusion arrows throughout. The 300 dpi crop confirms their direction. Running header/name and print page number `388` are omitted.

### 2026-10-02 00:42 UTC · PDF p.33/98 · print p.389
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p033.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p033_annuli.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p033_disks.png` (300 dpi crops)
- Markdown: annulus construction in the Theorem 4.3 proof and the first singular-Norman-trick step (current source lines 591–595).
- Checked: stage/boundary indices, intermediate annuli and distinguished-torus intersections, the claimed π₁-negligibility condition, and the connected-sum disk construction.
- Result: **FAIL** — Markdown line 593 writes `π_i` and malformed `$$…$` delimiters in the condition on the union of annuli; print p.389 has a single-subscript `π_1`-negligibility condition. The 300 dpi crop confirms the subscript. Other checked formulas agree; running header/name and print page number `389` are omitted.

### 2026-10-02 01:18 UTC · PDF p.34/98 · print p.390
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p034.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p034_framing_formula.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p034_framing_formula_full.png` (300 dpi crops)
- Markdown: dual-generator conclusion, the framing problem/formula, zero-framing correction, π₁-negligibility step, and start of the remaining-generator construction (current source lines 597–617).
- Checked: distinguished-torus generators, relative framing formula including the signed-double-point count, normal-bundle triviality, Casson-move argument, and the linked Example 4.5 diagram.
- Result: **PASS±** — the line break beneath `+ 2` in the framing formula corresponds to the centered “(# double points counted by sign)” text on the print page. The remaining checked text and diagram agree; running header/name and print page number `390` are omitted.

### 2026-10-02 01:49 UTC · PDF p.35/98 · print p.391
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p035.png` (pngmono 150 dpi)
- Markdown: conclusion of the singular-Norman-trick construction, framing correction, null-homotopy attachment argument, and opening of the Theorem 4.4 proof (current source lines 619–629).
- Checked: null-homotopy collection and attaching curves, (V_5^1) and extended tower construction, free-group dual-generator criterion, zero-framing cancellation argument, and the theorem continuation at the page break.
- Result: **PASS±** — checked prose and formulas agree with print. Running header/name and print page number `391` are omitted.

### 2026-10-02 02:30 UTC · PDF p.36/98 · print p.392
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p036.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p036_mitosis_indices.png` (300 dpi crop)
- Markdown: completion of the Theorem 4.4 argument, Theorem 4.5 and its explanation, Diagram 4.6, and the seven-step construction outline (current source lines 629–651).
- Checked: zero-map staging, Mitosis theorem conditions and arithmetic `13 = 6 + 6 + 1`, the linked diagram, and the sequence of subtower indices.
- Result: **PASS±** — Markdown follows print. Print p.392 itself ends with `T_{7-3}^{3}` in the final union after the preceding sentence states `T_{7-13}^{7}`; the high-resolution crop confirms this source inconsistency, which is preserved without correction. Running header/name and print page number `392` are omitted.

### 2026-10-02 02:31 UTC · PDF p.37/98 · print p.393
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p037.png` (pngmono 150 dpi)
- Markdown: conclusion of the Mitosis proof, §5 opening, Theorem 5.1 and its geometric-control conditions, and the beginning of the labeled-tree construction/footnote 7 (current source lines 651–663).
- Checked: the control/closure claims, frontier decomposition of the S–B handle, boundary-imbedding conditions, agreement of the first four spines, and the Shapiro–Bing footnote.
- Result: **PASS±** — the checked statements agree with the print page. Running header/name and print page number `393` are omitted.

### 2026-10-02 03:32 UTC · PDF p.38/98 · print p.394
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p038.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p038_framing_notation.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p038_print_footnotes.png` (300 dpi crops)
- Markdown: tree-to-Casson-handle construction, preferred framing, nested Whitehead-link sequence, Whitehead decomposition, and footnotes 8–9 (current source lines 665–709).
- Checked: labeled-edge recursion, the normal-framing notation, the nested solid-torus inclusions, `Wh_Q`/`Wh_Q*`, and both printed footnotes.
- Result: **FAIL** — Markdown lines 681–689 and 693–705 contain isolated footnote fragments already included in the complete footnote 8/9 blocks at lines 691 and 707; print p.394 has only the two complete notes, as shown in the footer crop. These duplicate fragments are extra OCR content. Minor differences also include the absent superscript 9 marker after “set” and print's Greek `ν` rendered as Latin `v` in the framing label. Print spellings such as `Whitelead` are reproduced literally. Running header/name and print page number `394` are omitted.

### 2026-10-02 04:01 UTC · PDF p.39/98 · print p.395
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p039.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p039_compactification.png` (300 dpi crop)
- Markdown: end of the Whitehead-decomposition definition, its defining sequence and compactification, Theorem 2.2, and the proof through the Diagram 5.1 lead-in (current source lines 709–719).
- Checked: `Wh_Q`/`Wh_Q*` definitions, nested `X_n` inclusions, quotient/compactification pairs, and the cancellation description of the 2-handlebody.
- Result: **PASS±** — the formulas and prose match. Print p.395 uses a dash-like mark in `∂⁻K – ∂D² × D²`, which Markdown preserves; the Markdown reference `Diagram|2.3` has an extra vertical bar compared with print's `Diagram 2.3`. These are recorded as minor notation/text artifacts. Running header/name and print page number `395` are omitted.

### 2026-10-02 04:11 UTC · PDF p.40/98 · print p.396
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p040.png` (pngmono 150 dpi)
- Markdown: Theorem 5.3 and its frontier formula, followed by the first stages of the geometric-control construction and Diagram 5.1 (current source lines 721–731).
- Checked: frontier quotient notation, the mitosis iteration from (T_6^0), the first (T_{12}^1) split, and Diagram 5.1 against the printed page.
- Result: **FAIL** — Markdown line 723 contains the delimiter sequence `D^2\times$$\partial D^2` in the last frontier formula, splitting the inline expression with an unmatched display-math opener. The printed source has one continuous (D^2\times\partial D^2/Wh_Q) expression. This damages formula rendering; the page image and embedded Diagram 5.1 were otherwise consistent.

### 2026-10-02 04:16 UTC · PDF p.41/98 · print p.397
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p041.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p041_sequence.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p041_tower_count.png`, and `audit/300dpi/Freedman_1982_topology_4manifolds_p041_frontier.png` (300 dpi crops)
- Markdown: general stage recursion, construction of the S–B handle from the nested towers, the limit-set/homeomorphism argument, and the frontier discussion (current source lines 733–741).
- Checked: index ranges and radius bound, (K/Y/L) construction, the map extending (d), and the stated frontier.
- Result: **FAIL** — Markdown line 735 includes (k=0) in the general recursion, while print p.397 states (k>0); this changes the stated range of the inductive step. The high-resolution crop confirms the strict inequality. Other unusual forms, including `ε/k + 1`, `n = m(k + 1)`, and `S^{-1}`, are reproduced from print and not corrected.

### 2026-10-02 04:20 UTC · PDF p.42/98 · print p.398
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p042.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p042_design_tuple.png` (300 dpi crop)
- Markdown: frontier/compactification discussion, design triad and map, thought experiment, labeled-tree definition, and Diagram 5.2 (current source lines 741–751).
- Checked: the isotopy/Schoenflies argument, all three design boundary components, the one-to-one/dyadic tree description, and Diagram 5.2 against print.
- Result: **FAIL** — Markdown line 743 labels the design in the first triad as `𝔇_q`, while print p.398 has `𝔇_Q` (capital Q), consistent with the surrounding occurrences. The 300 dpi crop confirms the subscript. Running header/name and print page number `398` are omitted.

### 2026-10-02 04:24 UTC · PDF p.43/98 · print p.399
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p043.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p043_embedding_constraint.png` (300 dpi crop)
- Markdown: final edge-labeling constraints, associated-tree definition, simultaneous embedding consequence, and Theorem 5.2 with the start of its induction (current source lines 753–767).
- Checked: decimal-edge and component-count rules, the top branch label, the finite-segment S–B handle, and the embedding constraint from Theorem 5.1.
- Result: **FAIL** — Markdown line 757 places the `e` subscript after the boundary-term parentheses and uses a two-headed arrow for the required embedding. Print p.399 subscripts both components of the pair by `e` and has a one-way arrow into `τ_e`. The 300 dpi crop confirms the grouping and direction. Running header/name and print page number `399` are omitted.

### 2026-10-02 04:24 UTC · PDF p.44/98 · print p.400
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p044.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p044_nested_embeddings.png` (300 dpi crop)
- Markdown: completion of Theorem 5.2, Theorem 5.3's nested-embedding statement, and the start of its proof (current source lines 767–781).
- Checked: branch-labeling induction, indices in the nested family of embeddings, normalization along ∂⁻, universal ε choice, and agreement of the initial 6-stage layers.
- Result: **FAIL** — Markdown line 771 writes `i_{c'}(K_{Q_c})` where print p.400 has `i_{c'}(K_{Q_{c'}})`; it also writes `i_c k_{Q_c}` in the stage-agreement clause where print has `i_c K_{Q_c}`. The subscript and upper/lowercase differences change the indexed spaces. The 300 dpi crop confirms the printed labels. Running header/name and print page number `400` are omitted.

### 2026-10-02 04:41 UTC · PDF p.45/98 · print p.401
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p045.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p045_frontier_addendum.png` (300 dpi crop) and `audit/300dpi/Freedman_1982_topology_4manifolds_p045_branch_indices_detail.png` (600 dpi source-render crop)
- Markdown: end of the Theorem 5.3 proof, its frontier-matching addendum, and the initial compact-design/radial-coordinate setup through Diagram 5.3 (current source lines 777–793).
- Checked: limit-set/disjointness argument, stage-by-stage frontier matching, the quotient/design coordinates, and Diagram 5.3.
- Result: **FAIL** — Markdown line 785 omits the `c′` label on the first stage tower in the right-hand side of the frontier identity (`T_{6(n+1)}′`); print p.401 has `T_{6(n+1)}^{c′}`. This loses the branch identity in the boundary description. The 300 dpi crop confirms the subscript. Running header/name and print page number `401` are omitted.

### 2026-10-02 04:45 UTC · PDF p.46/98 · print p.402
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p046.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p046_middle_thirds.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p046_third_intervals.png` (300 dpi crops)
- Markdown: radial-coherence defining sequence, middle-third interval names, the thickened X_n^e sequence, the box union, and Diagram 5.4 (current source lines 795–811).
- Checked: interval endpoints in the first/second complements, stage thickening, the middle-third box definition, and Diagram 5.4 against print.
- Result: **FAIL** — Markdown line 801 writes the second-complement interval as `[.02.1]`; print p.402 has `[.02,.1]`, with a comma separating the endpoints. The 300 dpi crop confirms the comma. Print's `[.2,.2]` interval is reproduced literally. Running header/name and print page number `402` are omitted.

### 2026-10-02 04:51 UTC · PDF p.47/98 · print p.403
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p047.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p047_design_formula.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p047_map_inverse.png` (300 dpi crops), and `audit/300dpi/Freedman_1982_topology_4manifolds_p047_definition_of_Delta.png` (600 dpi source-render crop)
- Markdown: completion of the design-embedding proof, including the definition of Δ and the extension from the noncompact part to the compact design (current source lines 823–831).
- Checked: the explicit decomposition formula for Δ, the construction of E and its frontier, the limit-point correspondence, and the final extension map.
- Result: **FAIL** — Markdown line 824 replaces most of the printed Δ-decomposition (the collar term and successive `X̄_k` minus extreme-third terms) with long runs of blank `\qquad` spacing and a stray `qend`. The source p.403 formula explicitly supplies those union terms; the 300 dpi crop confirms the missing content. Markdown line 818 also renders `Fr^+` as `F_r^+`. These formula losses affect the definition of the design and its frontier map. Running header/name and print page number `403` are omitted.

### 2026-10-02 04:55 UTC · PDF p.48/98 · print p.404
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p048.png` (pngmono 150 dpi)
- Markdown: Diagram 5.5 and its surrounding description, followed by §6 and Theorem 1.1 (current source lines 833–839).
- Checked: the linked Diagram 5.5 against the page image, the decomposition-space reduction heading, and the theorem's Casson-handle/open-2-handle pair statement.
- Result: **PASS±** — figure, text, and pair notation agree. Running header/name and print page number `404` are omitted.

### 2026-10-02 04:59 UTC · PDF p.49/98 · print p.405
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p049.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p049_hatA_gapterms.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p049_gap_notation.png` (300 dpi crops)
- Markdown: §6 setup, the maps (j,pi,g) and proposed homeomorphism, the unexplored-region/gap quotient, and the map-pair diagram (current source lines 841–857).
- Checked: the deleted-boundary notation, the compact/design map composition, the domain removed as unexplored, the gap definition/quotient, and both linked diagrams.
- Result: **FAIL** — Markdown line 851 writes `g^{𝔇}` where print p.405 has `g(\dot{𝔇})`; line 853 likewise writes `g(𝔔)` rather than `g(\dot{𝔇})`. These alter the domain whose complement is declared unknown. The 300 dpi crop confirms the dotted design symbol and parentheses. Running header/name and print page number `405` are omitted.

### 2026-10-02 05:02 UTC · PDF p.50/98 · print p.406
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p050.png` (pngmono 150 dpi)
- Markdown: point-inverse obstruction discussion, the holes/gaps quotient maps, disk-description introduction, and the diagonal-box hierarchy through the level intersections (current source lines 859–881).
- Checked: the noncellular point-inverse group claim, α/β quotient display, first/second third-complement context, box indexing, and the odd dyadic level parameter.
- Result: **PASS±** — the checked text and formulas match print. Running header/name and print page number `406` are omitted.

### 2026-10-02 05:05 UTC · PDF p.51/98 · print p.407
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p051.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p051_disk_conditions.png` (300 dpi crop)
- Markdown: clasp simplification of the immersed disks, annulus/collar setup, disk-translation function, four inductive disjointness conditions, and the beginning of the induction (current source lines 883–907).
- Checked: null-homotopy of the inclusions, signed-clasp preparation, θ-function domain/range, the four disk-intersection conditions, and the thickened middle-third neighborhood.
- Result: **PASS±** — the checked notation matches. Print condition (2) itself states `j = k′` after `k = k′` (rather than repeating a j-index); the 300 dpi crop confirms this visible source form, which Markdown preserves without correction. Running header/name and print page number `407` are omitted.

### 2026-10-02 05:11 UTC · PDF p.52/98 · print p.408
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p052.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p052_theta_function.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p052_projection.png` (300 dpi crops)
- Markdown: Diagram 6.1, the piecewise `θ`-function requirements, construction of the first translated disks, and the sub-induction hypothesis (current source lines 912–920).
- Checked: the source diagram, the product/index notation defining `θ⁰_{k+1}`, values on hatched disks, the projection interval, and the indexed disk-family conditions.
- Result: **FAIL** — Markdown line 916 moves the `0` into the product index (`Π_{j0}θ`) instead of print's `Π_j θ^j = {}_0θ`; line 920 also loses the `j < q` range in the indexed family and drops the final `n_{k+1}` subscript from the distinct radial values. The 300 dpi crops confirm the indices. Running header/name and print page number `408` are omitted.

### 2026-10-02 05:14 UTC · PDF p.53/98 · print p.409
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p053.png` (pngmono 150 dpi)
- Markdown: completion of the sub-induction, limit-point injectivity argument, assembled disk family, conversion from holes/gaps to the quotient map, and Diagram 6.2 (current source lines 920–946).
- Checked: uniform convergence and radial separation, the limit-set injection argument, the combined projection/embedding map, and the linked Diagram 6.2 against print.
- Result: **PASS±** — this page's continuation agrees with the source. The indexed-family differences at the page boundary are recorded under p.52. Running header/name and print page number `409` are omitted.

### 2026-10-02 05:19 UTC · PDF p.54/98 · print p.410
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p054.png` (pngmono 150 dpi)
- Markdown: Diagram 6.2 recap, the Diagram 6.3 description of threaded disks in the diagonal/upper-diagonal boxes, and the radial-coordinate/depth explanation (current source lines 942–950).
- Checked: the diagram-6.2 reference, hole/box labels, both directions assigned to radial/depth coordinates, interval levels, and the linked Diagram 6.3 asset against print.
- Result: **PASS±** — text and Diagram 6.3 match the page image. Running header/name and print page number `410` are omitted.

### 2026-10-02 05:21 UTC · PDF p.55/98 · print p.411
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p055.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p055_abh_corollary_footnotes.png` (300 dpi crop)
- Markdown: literal interpretation of Diagram 6.3's curves, ABH definition, Corollary 7.1, and footnotes 10–12 (current source lines 954–970).
- Checked: `θ_k^j` graph statement, metric definition/bound, relative homeomorphism hypothesis and conclusion, and the printed footnote set.
- Result: **FAIL** — Markdown line 960 changes the corollary's final approximation bound from print's `dist(π,h) < ε` to `dist(π,h) < ∞`, removing the required arbitrary-ε estimate. The footer also has two extra standalone `§7` fragments at lines 962 and 966; print has only the three complete footnotes 10–12. The 300 dpi crop confirms both discrepancies.

### 2026-10-02 05:27 UTC · PDF p.56/98 · print p.412
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p056.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p056_collar_epsilon.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p056_countable_null.png` (300 dpi crops)
- Markdown: the end of Theorem 9.1′ and the opening proof of Theorem 1.1, including the product collar, countable-null estimate, singular-set comparison, and footnote 13 (current source lines 972–1000).
- Checked: the collar parameter and attaching boundary, quotient-complement map, disks in the Casson-handle complement, singular-set notation, and footnote text against print p.412.
- Result: **FAIL** — Markdown line 980 gives the first collar interval as `[0, \in]`; print has `[0, ε]`. Line 986 writes `CH\{i∘π(d_k^j)\}` without the printed set-difference operator, changing the stated disks from lying in the complement to lying in the image set. The page footer also inserts standalone `C ⊂ Sⁿ` and `f` fragments at lines 994 and 996 before repeating the complete footnote 13 at line 998. The 300 dpi crops confirm the mathematical-symbol discrepancies and the 150 dpi page image shows the duplicated footer fragments. Running header/name and print page number `412` are omitted.

### 2026-10-02 05:30 UTC · PDF p.57/98 · print p.413
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p057.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p057_gluing_proof.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p057_abha_definitions.png` (300 dpi crops)
- Markdown: the end of the Theorem 1.1 gluing proof and the start of §7, through Bing-topology Definitions (1)–(2) and their metric equivalence (current source lines 1000–1016).
- Checked: the limit-point complement, half-open collar and compactification, restricted homeomorphism domains, final glued map, ABH definitions, and the strict approximation bounds against print p.413.
- Result: **FAIL** — Markdown line 1004 changes the second gluing map's domain from print's `CH \\setminus ∂⁻CH` to the pair `(CH, ∂⁻CH)`. In the final map on the same line, print has a single-barred `\\bar h` and restricts to `S⁴ \\setminus {∞}`; Markdown has `\\bar{\\bar h}` and moves the deletion sign into the exponent as `S^{4-}\\{∞}`. These alter the stated map and its domain. The 300 dpi gluing crop confirms the print forms; the definition crop confirms the approximation inequalities on this page. Running header/name and print page number `413` are omitted.

### 2026-10-02 05:33 UTC · PDF p.58/98 · print p.414
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p058.png` (pngmono 150 dpi)
- Markdown: the compact-space note, decomposition and quotient definitions, the conditions table, the shrinkability definition, and Theorem 7.1 (current source lines 1018–1036).
- Checked: the nondegenerate subcollection and its topology, all three table relationships, the diameter and quotient-map inequalities in shrinkability, and the ABH/shrinkability equivalence against print p.414.
- Result: **PASS±** — the checked statements, arrows, and formulas match print. The table text at line 1024 joins “a saturated” as “asaturated,” a spacing defect that does not change the statement. The running header/name and print page number `414` are omitted.

### 2026-10-02 05:37 UTC · PDF p.59/98 · print p.415
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p059.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p059_Ei_formula.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p059_cellularity_proof.png` (300 dpi crops)
- Markdown: the Bing shrinking-criterion proof, Observation 7.1 on metric choice, the definition of cellularity, and Observation 7.2 with its recursive neighborhood construction (current source lines 1038–1060).
- Checked: the complete metric on the map space, the sets `E_i` and their threshold, the two metric-neighborhood comparison, and the indexed recursive conditions defining the cellular preimage.
- Result: **FAIL** — Markdown line 1046 writes `(1/i) \in (x)` in the defining threshold for `E_i`; print p.415 has `(1/i) ε(x)`. The membership symbol changes the pointwise bound that defines the dense open subsets. The 300 dpi `E_i` crop confirms the epsilon factor; the second crop confirms the page's cellularity recursion, which agrees. Running header/name and print page number `415` are omitted.

### 2026-10-02 05:39 UTC · PDF p.60/98 · print p.416
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p060.png` (pngmono 150 dpi)
- Markdown: the cellular-but-not-shrinkable Bing example, its countable-null definition, Diagram 7.1, and the two-fold-cover argument (current source lines 1062–1078).
- Checked: the two embedded solid tori and their labels `i_0`,`i_2`, the nested `i_{20}`/`i_{22}` indexing, essential disk labels, and the contradiction at the limiting decomposition element against print p.416.
- Result: **PASS±** — text and the linked Diagram 7.1 match the source page. The original phrases “only countable many” and “there exists a only finitely many” are preserved as printed. The running header/name and print page number `416` are omitted.

### 2026-10-02 05:41 UTC · PDF p.61/98 · print p.417
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p061.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p061_star_like_definition.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p061_lemma_application.png` (300 dpi crops)
- Markdown: Theorem 7.2, the generalized star-like-equivalence definitions, the proof strategy and Lemma 7.1, through the conclusion by the Bing shrinking criterion (current source lines 1080–1092).
- Checked: theorem hypotheses and equivalence, cone/open-set notation, countable-null condition, Lemma 7.1 support and disk bounds, and the final epsilon-close homeomorphism construction against print p.417.
- Result: **FAIL** — Markdown line 1092 places two consecutive dollar signs between the barred `h` and the `ε`-close qualifier, breaking the math/text boundary. Print p.417 has a single barred `h` followed by “ε-close.” Both 300 dpi crops confirm the source notation. Running header/name and print page number `417` are omitted.

### 2026-10-02 05:44 UTC · PDF p.62/98 · print p.418
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p062.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p062_uniform_continuity.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p062_nullity_bound.png` (300 dpi crops)
- Markdown: the reduction to the cone model, the metric properties, the nested star-like neighborhoods, and the definition of the radial homeomorphism g with Claim 1 (current source lines 1094–1106).
- Checked: the diameter-transfer inequality, the compactum term as printed, the `δ/2` nullity threshold, the nested-neighborhood indices, and the movement bound in Claim 1 against print p.418.
- Result: **FAIL** — Markdown line 1096 leaves both terms in the diameter-transfer implication unclosed: it has `diam_d(k(compaction) < δ` and `diam_Δ(compaction < ε`, whereas print has `diam_d(k(compaction)) < δ` and `diam_Δ(compaction) < ε`. The missing right parentheses break the displayed implication. The nullity crop confirms the page's threshold is `≥ δ/2`, matching the Markdown. The running header/name and print page number `418` are omitted.

### 2026-10-02 05:46 UTC · PDF p.63/98 · print p.419
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p063.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p063_case3_coordinates.png` (300 dpi crop)
- Markdown: Cases 1–3 in the diameter estimate for `g(k_i)`, the conclusion of Lemma 7.1/Theorem 7.2, and Diagram 7.2 (current source lines 1108–1134).
- Checked: all three case estimates, the radial ordering in Case 3, the polar coordinates of `u` and `v`, the final diameter bound, and Diagram 7.2 against print p.419.
- Result: **FAIL** — Markdown line 1128 omits a closing parenthesis in the radial comparison, writing `ρ(g(x) ≤ ρ(g(y))` instead of print's `ρ(g(x)) ≤ ρ(g(y))`. It also writes `u` with first coordinate `ρ(g(x), z(g(y)))` rather than the printed pair `(ρ(g(x)), z(g(y)))`. These alter the coordinate expressions used in Case 3. The 300 dpi crop confirms both forms. The running header/name and print page number `419` are omitted.

### 2026-10-02 05:49 UTC · PDF p.64/98 · print p.420
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p064.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p064_theorem73.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p064_footer.png` (300 dpi crops)
- Markdown: Diagram 7.3, the majorant shrinking principle/Theorem 7.3 statement, the definitions of A, B, C, C⁺, C⁻, D, and footnote 14 (current source lines 1136–1172).
- Checked: Diagram 7.3 labels, the theorem's map restriction and hypotheses, all six inverse-image interval families, the open neighborhood D⁺, and the printed footnote.
- Result: **FAIL** — Markdown line 1170 contains a standalone `8),` fragment; print p.420 has only the complete footnote 14, confirmed by the 300 dpi footer crop. The apparent phrase “Assume that if is ABH” at line 1140 is also visible in print and is preserved as a source-level quirk. Diagram 7.3 and the remaining checked notation match. Running header/name and print page number `420` are omitted.

### 2026-10-02 05:56 UTC · PDF p.65/98 · print p.421
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p065.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p065_msp_construction.png` (300 dpi crop) and `audit/300dpi/Freedman_1982_topology_4manifolds_p065_restriction_arrow_600dpi.png` (600 dpi crop)
- Markdown: the completion of the majorant shrinking construction, Corollary 7.1 and its proof, Fact 7.1, and the following sentence that its proof is easy (current source lines 1174–1192).
- Checked: the A/C and B/C region notation, the restricted map and its codomain, the gluing homeomorphism G, the piecewise definition of H, the relative approximation corollary, and the map-composition fact.
- Result: **FAIL** — Markdown lines 1174 and 1181 write the printed set unions `A ∪ C`, `B ∪ C`, and `A ∪ C⁺` as ordinary roman strings `AUC`, `BUC`, and `AUC⁺`. Line 1176 uses two parallel right arrows where print has a double-line right arrow with one head. The 600 dpi crop confirms the arrow and union forms. The slash notation in the closeness expression at line 1174 matches the printed source. Running header/name and print page number `421` are omitted.

### 2026-10-02 05:59 UTC · PDF p.66/98 · print p.422
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p066.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p066_fact72_proof.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p066_whitehead_intersection.png` (300 dpi crops)
- Markdown: Fact 7.2 and its proof, the Whitehead-continuum setup and end obstruction, Theorem 7.4, and the historical paragraph through 1965 (current source lines 1194–1208).
- Checked: the commutative diagram and linked image, approximation estimate and composition formula, the nested solid-torus intersection, the quotient boundary notation, and the product-with-`R` statement.
- Result: **FAIL** — Markdown line 1200 inserts an extra `$` before each `δ`/`ε`-close qualifier (`Y$$δ` and `p'^{-1}$$ε`), breaking the math/text delimiters. Line 1202 omits the `i` in the nesting condition, writing `T_{i+1} ⊂ interior T` instead of print's `T_{i+1} ⊂ interior T_i`. The printed proof text says `p ∘ r = q`, which Markdown preserves; the diagram's arrows `X → Y`, `X → Z`, and `Y → Z` imply `r ∘ p = q`, so this is an internal source inconsistency rather than a transcription discrepancy. The crops confirm the formula and index. Running header/name and print page number `422` are omitted.

### 2026-10-02 06:01 UTC · PDF p.67/98 · print p.423
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p067.png` (pngmono 150 dpi)
- Markdown: the opening of the Theorem 7.4 proof, Diagram 7.4, Addendum A, and the opening construction in Addendum B (current source lines 1210–1222).
- Checked: the support and `h=T∘L` construction, the `r`, `r₀`, and `r₁` clasp coordinates, the fixed rod and boundary taper, Diagram 7.4's Lift/Twist labels, the nested Whitehead-decomposition sequence, and the thickened defining sequence.
- Result: **PASS±** — the checked text, formulas, indices, and diagram agree with print p.423. The running header/name and print page number `423` are omitted.

### 2026-10-02 06:04 UTC · PDF p.68/98 · print p.424
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p068.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p068_addendum_c_diagram.png`, `audit/300dpi/Freedman_1982_topology_4manifolds_p068_addendum_d.png`, and `audit/300dpi/Freedman_1982_topology_4manifolds_p068_addendum_e_relation.png` (300 dpi crops)
- Markdown: the end of Addendum B, Addenda C and D, and the statement of Addendum E (current source lines 1224–1236).
- Checked: the Addendum C projection and fiber-set definition, the three-map diagram, Addendum D's relative shrinkability notation and double overbar, and the coordinate relation in Addendum E.
- Result: **FAIL** — Markdown line 1229 reduces Addendum C's triangular diagram to repeated literal backslash commands; the printed diagonal arrows `b` and `π` and their endpoints are not represented by that array. Line 1236 changes the printed single-headed double-line arrow `⇒` to a bidirectional equivalence arrow. The 300 dpi crops confirm both. Addendum D's double-overbar notation and remaining checked statements match. Running header/name and print page number `424` are omitted.

### 2026-10-02 06:06 UTC · PDF p.69/98 · print p.425
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p069.png` (pngmono 150 dpi)
- Markdown: the end of Addendum E, the pair version of the Bing Shrinking Criterion, the start of §8, and its type I/type II Whitehead-decomposition elements (current source lines 1240–1252).
- Checked: the factoring diagram's objects and arrows, the quantified pair criterion and both inequalities, the section heading and decomposition notation, and the type-II disk/solid-torus incidence.
- Result: **PASS±** — the checked diagram, statements, and notation agree with print p.425. The running header/name and print page number `425` are omitted.

### 2026-10-02 06:10 UTC · PDF p.70/98 · print p.426
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p070.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p070_alpha_extension.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p070_factoring_sets.png` (300 dpi crops)
- Markdown: Diagram 8.1, the type-III exceptional element, the reduction to `D(α⁻)`, the three-stage factoring, and the definitions of Set 1/Set 2 (current source lines 1254–1270).
- Checked: the linked hairy-cell diagram, the collar extension argument and its domains, the orientation and endpoint of each factoring arrow, and the two sets formed from Whitehead elements and spanning disks.
- Result: **FAIL** — Markdown line 1265 places `α₃` as a horizontal arrow on a second row; print p.426 shows it as the downward arrow from the rightmost intermediate quotient to `D² × S¹ × (0,1)/D(α⁻)`. This changes the factorization diagram's map direction and endpoints. The apparently unusual `D′` product in the `h_i` domain is visible in print and is preserved. Both 300 dpi crops confirm these checks. Running header/name and print page number `426` are omitted.

### 2026-10-02 06:15 UTC · PDF p.71/98 · print p.427
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p071.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p071_factorization_proof.png` (300 dpi crop)
- Markdown: the staged decomposition data, Steps 1–2, Lemma 8.1, and the proof of the relative approximation statement (current source lines 1273–1288).
- Checked: the nondegenerate pieces of the three quotient maps, the α_{1/3}/α_{2/3} factorization and arrow labels, the definition sequence for S, and the relative-boundary agreement in Lemma 8.1.
- Result: **FAIL** — Markdown line 1286 inserts an extra `$` between the Whitehead-set notation and `S`, breaking the math/text boundary. It also leaves the first arrow in the factorization unlabeled and labels the second arrow `α_{1/3}`; print p.427 labels them α_{1/3} and α_{2/3}, respectively. The 300 dpi crop confirms the arrow labels. Running header/name and print page number `427` are omitted.

### 2026-10-02 06:16 UTC · PDF p.72/98 · print p.428
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p072.png` (pngmono 150 dpi)
- Markdown: the two views of Diagram 8.2, its explanatory sentence, and the diagram caption (current source lines 1290–1296).
- Checked: both linked images against the printed two-stage isotopy illustration, the labels `w`, `x`, `y`, `z`, `d`, and `S_n`, the fixed-neighborhood caption, and the explanatory sentence.
- Result: **PASS±** — the linked images, labels, sentence, and Diagram 8.2 caption agree with print p.428. The running header/name and print page number `428` are omitted.

### 2026-10-02 06:18 UTC · PDF p.73/98 · print p.429
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p073.png` (pngmono 150 dpi)
- Markdown: the conclusion of Lemma 8.1's preceding argument, Step 3's introduction, Stage 1 with Diagram 8.3 and its three properties, and the start of Stage 2 (current source lines 1298–1312, through the print-page ending “that”).
- Checked: the three-step quotient context, the mapping-cylinder objects `S³`, `d`, and `S¹ × D² × I`, Diagram 8.3, each of the three stated structural properties, and the opening of the image-in-`Y/D(α₁)` argument.
- Result: **PASS±** — the checked text and linked Diagram 8.3 match print p.429. The page ends mid-sentence after “It follows from Theorem 7.4, Addendum C, that”; the rest of Markdown line 1312 belongs to the next printed page and is audited there. Running header/name and print page number `429` are omitted.

### 2026-10-02 06:21 UTC · PDF p.74/98 · print p.430
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p074.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p074_pair_homeomorphism_diagram.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p074_stage4_triangle.png` (300 dpi crops)
- Markdown: Step 2's outward product extension and pair-map factoring, the end of Stage 2, Stage 3, Stage 4, and the beginning of its Corollary 7.1 argument (current source lines 1312–1330, through the print-page cutoff).
- Checked: the product quotient notation, the Addendum E/C path of pair homeomorphisms, the α_{4/3}/α_{5/3} stage factorization, the Stage 4 quotient objects and arrow directions, and the page-end continuation.
- Result: **FAIL** — Markdown line 1315 preserves one left arrow but omits the printed Addendum E/C-labeled path and its intermediate pair in the pair-homeomorphism diagram. Line 1327 renders the Stage 4 α_{4/3} and α_{5/3} diagonal arrows as a vertical arrow and a literal backslash rather than the two printed diagonal maps with arrowheads. These change the diagrammed factorizations. The 300 dpi crops confirm the missing path and arrow geometry. The remainder of the page's prose and indices agrees through print p.430; the sentence continues on the next page.

### 2026-10-02 06:23 UTC · PDF p.75/98 · print p.431
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p075.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p075_mutual_separation.png` (300 dpi crop)
- Markdown: the end of the Stage 4 argument, Theorem 8.1 and its relative-boundary note, the opening of §9, and the definitions of singularity, mutual separation, and tame-zero-dimensionality (current source lines 1332–1348).
- Checked: the final composition of `α⁻`, the quotient target in Theorem 8.1, the singular-set filtration threshold, the mutually separated condition, and the flat-ball boundary condition.
- Result: **PASS±** — the checked text and formulas match print p.431. The print itself repeats `Q_j` on both sides of the intersection in the mutual-separation formula while also stating `i ≠ j`; the Markdown preserves this source-level repeated-index quirk. The 300 dpi crop confirms the printed indices. Running header/name and print page number `431` are omitted.

### 2026-10-02 06:25 UTC · PDF p.76/98 · print p.432
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p076.png` (pngmono 150 dpi)
- Markdown: the ABH definition, Theorem 9.1, its context and range remark, Lemma 9.1, and the admissible-diagram definition through conditions (1)–(4) (current source lines 1350–1374).
- Checked: the uniform approximation bound, theorem hypotheses, singular-set terminology, flat-cell boundary condition, diagram arrows and labels, relation-inverse/composition rule, and the three-way singular-set partition.
- Result: **PASS±** — the checked text, formulas, and admissible diagram agree with print p.432. The page ends after condition (4); condition (5) starts on the next print page and is audited there. Running header/name and print page number `432` are omitted.

### 2026-10-02 06:28 UTC · PDF p.77/98 · print p.433
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p077.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p077_Qepsilon_threshold.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p077_Rprime_definition.png` (300 dpi crops)
- Markdown: condition (5), the setup and proof of Lemma 9.2, conditions (A)–(B), the cell choices, the extension map `j`, and the piecewise definition of `R′` (current source lines 1376–1395).
- Checked: the restriction homeomorphism, the `Q_ε` diameter threshold, the containments controlling `B` and `U`, the boundary extension for `j`, and all three branches in the `R′` definition.
- Result: **PASS±** — the checked conditions and branches match print p.433. In the printed first branch the exponent appears as `−` without a superscript `1` in `r⁻(B)`; Markdown preserves this source-level form. The 300 dpi crops confirm both that notation and the `≥ ε` threshold. Running header/name and print page number `433` are omitted.

### 2026-10-02 06:31 UTC · PDF p.78/98 · print p.434
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p078.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p078_compatibility_sets.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p078_lemma93.png` (300 dpi crops)
- Markdown: the compatibility check, definitions of `S′`, `r′` and the new singular-set pieces, Lemma 9.2 completion/Diagram 9.1, and Lemma 9.3 (current source lines 1398–1416).
- Checked: the boundary composition identity, the α/β/γ set updates, Diagram 9.1, both diameter estimates in Lemma 9.3, and the proof-of-Theorem-9.1 setup.
- Result: **FAIL** — Markdown line 1398 omits the leading `s` in the right-hand side `s⁻¹ ∘ r` of the compatibility identity. Line 1407 writes `Q′ = Q − U` and uses `Q ∩ U` for `C′`; print has `A′ = A − U` and `C′ = C ∪ (A ∩ U)`. Line 1416 leaves the first maximum's set brace unclosed; print closes that set before `< ε`. The printed second maximum itself is `maximum {M⁻¹(y)}` without `diam`, and Markdown preserves this source-level omission. The 300 dpi crops confirm these differences; the linked Diagram 9.1 matches. Running header/name and print page number `434` are omitted.

### 2026-10-02 06:35 UTC · PDF p.79/98 · print p.435
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p079.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p079_symmetry.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p079_theorem103.png` (300 dpi crops)
- Markdown: the symmetry step and alternating inverse-diameter construction in the proof of Theorem 9.1, followed by §10 and Theorem 10.3 (current source lines 1422–1434).
- Checked: the exchanged roles of the three singular-set pieces, the (N^k/S^{even}/R^{odd}) nesting and diameter bounds, the intersection relation defining `h`, and the proper h-cobordism hypotheses/product conclusion.
- Result: **FAIL** — Markdown line 1424 writes `\mathcal{Q} \leftrightarrow \mathcal{B}`; print p.435 has `\mathcal{A} \leftrightarrow \mathcal{B}`. The 300 dpi symmetry crop confirms the first set is calligraphic A. The remaining checked proof formulas and Theorem 10.3 match. Running header/name and print page number `435` are omitted.

### 2026-10-02 06:37 UTC · PDF p.80/98 · print p.436
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p080.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p080_main_section_condition.png` (300 dpi crop)
- Markdown: the simple-connectivity-at-infinity note, Lemma 10.1, its main-section addendum and proof, through the first two normalization conditions (current source lines 1436–1450).
- Checked: the compactum/loop quantifiers, the paired intersection hypothesis and Casson-move conclusion, the main-section patch and relative disk condition, the geometric-dual interpretation, and conditions (1)–(2) in the addendum proof.
- Result: **PASS±** — the checked statements and symbols match print p.436. In the main-section definition the print visibly uses `⊂` after “a single point”; Markdown preserves that source-level set-inclusion form. The 300 dpi crop confirms it. Running header/name and print page number `436` are omitted.

### 2026-10-02 06:40 UTC · PDF p.81/98 · print p.437
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p081.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p081_framing_notation.png` (300 dpi crop)
- Markdown: conditions (3)–(4) from the main-section addendum, Whitney circle/disk terminology, the normal-bundle framing condition and its two interpretations, Diagram 10.1, and the linking-number conclusion (current source lines 1452–1468).
- Checked: the two remaining addendum conditions, the framed normal-bundle notation, the section extending over the disk, the choice used to cancel double points, and the two linking circles and their signs.
- Result: **FAIL** — Markdown line 1456 uses Latin `v_{Δ↔M}` in two places where print has Greek `ν_{Δ↔M}` for the normal bundle. Line 1460 writes `\bar{0}` instead of print's `\bar{θ}` in “the choice of θ-bar,” changing the section named in the framing argument. The 300 dpi crop confirms both glyphs. Diagram 10.1 matches the linked source figure. Running header/name and print page number `437` are omitted.

### 2026-10-02 06:43 UTC · PDF p.82/98 · print p.438
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p082.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p082_framing_theorem101.png` (300 dpi crop)
- Markdown: the Whitney-tower motivation and definition, attachment and framing conditions, Theorem 10.1, the π₁-hypothesis, and its addendum (current source lines 1470–1485).
- Checked: the framed normal bundle, the annulus boundary circles and parallel copy, the linking-number condition, the theorem's dual-sphere/intersection hypotheses, and the inclusion chain in the π₁-hypothesis.
- Result: **FAIL** — Markdown line 1476 writes the natural annulus boundary as `γ ⊔ γ`, while print p.438 has `γ ∪ γ′`: the operator and the prime on the parallel copy differ. The 300 dpi crop confirms the printed second-circle prime. The pair notation `(T₆, ∂)` later in the theorem is also printed without a minus and is preserved as source text. Running header/name and print page number `438` are omitted.

### 2026-10-02 06:46 UTC · PDF p.83/98 · print p.439
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p083.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p083_handle_proof.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p083_section_end.png` (300 dpi crops)
- Markdown: the proof of Theorem 10.1, the compact h-cobordism Theorem 10.2 and its handle argument, and the opening of the proper h-cobordism proof through the printed page cutoff (current source lines 1487–1495).
- Checked: the first-stage framing discussion, the even geometric-dual pairing, the π₁-negligibility statement, the handle-cancellation formula, the product conclusion, and the dimension threshold at the page end.
- Result: **FAIL** — Markdown line 1493 inserts a second `$` between `\{d_i\}` and the `π₁`-negligible qualifier, breaking the math/text boundary. The 300 dpi proof crop confirms the print has an ordinary space there. The page-end dimension condition is `≥ 6` in print and is preserved. Markdown line 1495 ends at “interesting that the”; the sentence continues on the next print page and is audited there. Running header/name and print page number `439` are omitted.

### 2026-10-02 06:49 UTC · PDF p.84/98 · print p.440
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p084.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p084_regular_values.png` (300 dpi crop)
- Markdown: the continuation of §10's introduction, proper deformation retractions, Morse-function tail estimates, the sequence of triples, and Improvements 1–2 through the page-end clause about connecting frontiers (current source lines 1497–1507).
- Checked: the dimension threshold, retraction endpoints and time interval, the `y₁`/`y₂`/`y₃`/`y₄` choices, the reparameterization, and the component-injectivity argument.
- Result: **PASS±** — the checked formulas and statements agree with print p.440. The print uses `y` (without subscript 1) in the first tail inclusion after introducing `y₁`, and uses `0 ≤ t ≤ 1`; Markdown preserves both source forms. The page ends mid-sentence after “frontiers”; the continuation is audited on the next print page. Running header/name and print page number `440` are omitted.

### 2026-10-02 06:52 UTC · PDF p.85/98 · print p.441
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p085.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p085_relative_pi1.png` (300 dpi crop)
- Markdown: the end of Improvement 2, Diagram 10.2, Improvements 3–4, the asymmetry in the boundary decomposition, and the start of the homology argument (current source lines 1507–1523, through the print-page cutoff).
- Checked: the handle-pair illustration and label, the end-space map, the relative fundamental-group vanishing condition, its arc/homotopy construction, and the parity-dependent boundary pieces.
- Result: **FAIL** — Markdown line 1515 drops the `n` subscripts in both ends spaces, writing `End(V^{(')}) → End(W)` instead of print's `End(V_n^{(')}) → End(W_n)`. At the opening of line 1517, Markdown omits the comma in the relative-group pair `π₁(W_n, V_n^{(')})`; the concluding occurrence on that line includes the comma. The 300 dpi crop confirms the end-space indices and pair separator. Diagram 10.2 and the printed “dimension = (5.4)” quirk are preserved. Running header/name and print page number `441` are omitted.

### 2026-10-02 06:55 UTC · PDF p.86/98 · print p.442
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p086.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p086_homology_sequence.png` (300 dpi crop)
- Markdown: completion of the fourth-improvement finiteness argument, its excision sequence, Improvement 5 and Diagram 10.3, and the opening of the sixth-improvement discussion (current source lines 1523–1539 through the print-page cutoff).
- Checked: the relative homology terms and maps, the category-C vanishing notation, the frontier fundamental-group conclusion, Diagram 10.3, and the dimension-five Whitney-tower limitation.
- Result: **FAIL** — Markdown line 1526 uses lowercase `v′` in the first relative homology term; print p.442 has uppercase `V′` in `\overline{V′ \setminus V_n′}`. The 300 dpi sequence crop confirms the capitalization. Diagram 10.3 and the remaining checked statements match. The page ends after “topological 2-handles (= topological Whitney disks)”; the continuation is audited next page. Running header/name and print page number `442` are omitted.

### 2026-10-02 06:58 UTC · PDF p.87/98 · print p.443
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p087.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p087_boundaries_diagrams.png` (300 dpi crop)
- Markdown: the continuation of the h-cobordism argument, the definitions of `z_n` and its signed boundary portions, Diagrams 10.4–10.5, and the introduction of slabs/blocks (current source lines 1537–1559, through the print-page cutoff).
- Checked: the closure/intersection definition of `z_n`, the parity-dependent `∂⁺/∂⁻` formulas, the levels in both diagrams, and the block/slab description.
- Result: **FAIL** — Markdown line 1543 writes `∂⁺a_n` in the even-index boundary formula; print p.443 has `∂⁺z_n`. The 300 dpi crop confirms the `z_n` subscript. The linked Diagrams 10.4 and 10.5 match. The printed page ends after “slabs and blocks use up”; the continuation is audited next page. Running header/name and print page number `443` are omitted.

### 2026-10-02 07:03 UTC · PDF p.88/98 · print p.444
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p088.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p088_specifications.png` (300 dpi crop) and `audit/300dpi/Freedman_1982_topology_4manifolds_p088_specs34_600dpi.png` (600 dpi crop)
- Markdown: Specifications 0–5 for the Diagram 10.6 block/slab model, including the relative homology sequence and three indexed fundamental-group maps (current source lines 1571–1599).
- Checked: the incidence and slab rules, vertical-side product structure, all boundary fundamental-group maps, the zero boundary homomorphism in the 2/3-handle chain complex, the `X_i` complement closure, and each barred vertex-string inclusion.
- Result: **PASS±** — the checked statements, indices, and vertex strings agree with print p.444. The source visibly prints `1π₁` after the arrows in Specifications 3–4, which the Markdown preserves. The prose beginning “are all seven-fold maps” continues on the next print page. Running header/name and print page number `444` are omitted.

### 2026-10-02 07:06 UTC · PDF p.89/98 · print p.445
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p089.png` (pngmono 150 dpi)
- Markdown: the seven-fold inclusions, the first specification analysis, Diagram 10.7, the slab-induced boundary maps, and the exact sequence for the 2/3-handle structure (current source lines 1601–1623 through the print-page cutoff).
- Checked: the successive-zero-map condition, the compact region and odd/even boundary definitions, the two slab additions and induced fundamental-group maps, the diagram labels, and the homology sequence.
- Result: **PASS±** — the checked statements, formulas, and Diagram 10.7 agree with print p.445. The page ends at “Let B be the handle”; the continuation is audited on the next print page. Running header/name and print page number `445` are omitted.

### 2026-10-02 07:08 UTC · PDF p.90/98 · print p.446
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p090.png` (pngmono 150 dpi)
- Markdown: the completion of handle body `B`, Improvements 3–5, Diagram 10.8, and the resulting 2/3-handle structure on `X` (current source lines 1625–1641).
- Checked: the boundary-isomorphism consequences of deleting 3-handles, the zero intersection condition, the odd/even slab additions and indices, Diagram 10.8 labels, and the fundamental-group maps for `X`.
- Result: **PASS±** — the checked text, indices, maps, and linked Diagram 10.8 agree with print p.446. Running header/name and print page number `446` are omitted.

### 2026-10-02 07:13 UTC · PDF p.91/98 · print p.447
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p091.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p091_fractional_indices.png` (300 dpi crop)
- Markdown: the final slab specifications, the three zero-map conditions, the stepwise construction of `S₁¹` and `S₁⁵`, and the repeated seven-step slab pattern (current source lines 1645–1669).
- Checked: the map words and vertex indices in conditions (1)–(3), the 1/7 terminus progression, the endpoints of `∂⁻S₁¹`, the seven collars, and the repeated slab-count arithmetic.
- Result: **FAIL** — Markdown line 1655 uses `8_{9i}^{1/7}`; print p.447 has `8_{0i}^{1/7}` in condition (3). Line 1659 also changes the first fraction in `∂⁻S₁¹` from `7₁^{1/7}` to `7₁^{1/2}`. The 300 dpi crop confirms both vertex/fraction indices. Running header/name and print page number `447` are omitted.

### 2026-10-02 07:15 UTC · PDF p.92/98 · print p.448
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p092.png` (pngmono 150 dpi)
- Markdown: the fractional-slab notation and middle-level construction, Lemma 10.2's dual-class statement and proof, through the independence argument at the print-page cutoff (current source lines 1671–1691).
- Checked: the 1/7 slab pieces, the descending/ascending sphere pairings, the intersection equations, the relative homology group and its torsion quotient, and the proof's boundary between the paired spheres and a capped 3-cycle.
- Result: **PASS±** — the checked formulas, fractions, and indices agree with print p.448. The page ends after “Thus the [d_k]’s are linearly independent. The”; the continuation is audited on the next print page. Running header/name and print page number `448` are omitted.

### 2026-10-02 07:18 UTC · PDF p.93/98 · print p.449
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p093.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p093_negligibility.png` (300 dpi crop)
- Markdown: the mod-p summand argument, the pairing obstruction, Diagram 10.9, and the construction of the middle-level collections through the integer-pairing setup (current source lines 1693–1707).
- Checked: the relative 3-cycle obstruction, diagram labels, the `K⁺/K⁻` surgeries, component incidences, the ascending/descending sphere collections, and the claimed pairing setup.
- Result: **PASS±** — the checked text, indices, and Diagram 10.9 agree with print p.449. The source itself says “π-negligible” without a subscript in its description of `K_{i+1}⁻`; Markdown preserves that source form. The page ends after the handle-pass setup; the verification continues on the next print page. Running header/name and print page number `449` are omitted.

### 2026-10-02 07:27 UTC · PDF p.94/98 · print p.450
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p094.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p094_middle_pairing.png` and `audit/300dpi/Freedman_1982_topology_4manifolds_p094_correspondences.png` (300 dpi crops)
- Markdown: the extended-middle-level pairing, its nonsingularity verification via `W × I`, the natural dual correspondences, and the opening of the final Whitney-isotopy step (current source lines 1709–1715).
- Checked: the fractional slab indices, the group-ring pairing and its integer lift, the 3/2-handle chunk correspondence, the 1–1 dual-set correspondences, and the page-end continuation.
- Result: **FAIL** — Markdown line 1711 splits the 1–1 correspondences between the barred/unbarred D-sets and A-sets across multiple malformed dollar spans, including `$$`, so the paired-set relation does not render as on print. The print's earlier middle-pairing token visibly reads `A's, D, s`, which Markdown preserves without normalizing. The 300 dpi crops confirm both forms. The page ends at “When”; the continuation is audited next page. Running header/name and print page number `450` are omitted.

### 2026-10-02 07:32 UTC · PDF p.95/98 · print p.451
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p095.png` (pngmono 150 dpi)
- High-resolution evidence: `audit/300dpi/Freedman_1982_topology_4manifolds_p095_final_proof.png` (300 dpi crop)
- Markdown: the sixth-improvement completion and product conclusion, followed by references [1]–[14] (current source lines 1717–1751).
- Checked: the constructed 6-dimensional chunk and its barred notation, dual-sphere collections and intersection pairing, the product conclusion, and the author/title/journal/volume/page/year fields in references [1]–[14].
- Result: **FAIL** — Markdown line 1717 uses an underline on `Z_i` where print has an overbar on `\bar Z_i`. Lines 1719 and 1721 also drop overbars from the constructed `Z_i` and the corresponding `A`/`D` sphere collections. These bars distinguish the modified chunks and transported dual families. The 300 dpi proof crop confirms the print bars. References [1]–[14] match the page's printed forms. Running header/name and print page number `451` are omitted.

### 2026-10-02 07:34 UTC · PDF p.96/98 · print p.452
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p096.png` (pngmono 150 dpi)
- Markdown: bibliography entries [15]–[44] (current source lines 1753–1811).
- Checked: each printed author or ditto mark, title, journal/book/conference, volume/issue, year, and page range through [44].
- Result: **PASS±** — the listed entries match print p.452. The source spellings “Farrel,” “Wagnor,” “Haupvermutung,” “Hirsh,” and “Laudenbath” are retained. Running header/name and print page number `452` are omitted.

### 2026-10-02 07:36 UTC · PDF p.97/98 · print p.453
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p097.png` (pngmono 150 dpi)
- Markdown: references [45]–[53] and the closing University of California at San Diego line (current source lines 1813–1831).
- Checked: author/ditto marks, titles, journal or book details, years, volumes, page ranges, and the final institutional line.
- Result: **PASS±** — the references and closing line match print p.453. Running header/name and print page number `453` are omitted.

### 2026-10-02 07:38 UTC · PDF p.98/98 · blank final page
- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`
- PNG: `audit/Freedman_1982_topology_4manifolds_p098.png` (pngmono 150 dpi)
- Markdown: no body segment; PDF p.97 contains the final printed text and the PDF p.98 source page is blank.
- Checked: the full p.98 raster and page-specific `pdftotext` output for printed text or figures.
- Result: **PASS±** — PDF p.98 is a blank trailing page, so there is no printed content to transcribe. It has no print page number or running header.

## Repair register · 2026-10-02

This register records the post-audit correction of the 51 page-ledger **FAIL** findings above. The original per-page findings remain unchanged as the historical audit record; this section records their repair.

- Actor/model/effort: `Peer-P39 | gpt-6-luna/max`.
- Markdown source baseline: commit `2ff32170aff06c35e9829c2ecb5c52d20adccf30`; original SHA-256 `f8be278a441d83611b80b6fd2ab620dde07d3d4597ec37c23138478591a4e2bf`.
- Markdown repair commit: `db28a3e6be30448790d5c418e42b55a498e083e1` (`fix(md): repair Freedman transcription mismatches`). It changes only the audited MinerU Markdown.
- Final Markdown SHA-256: `331429d7be6d6e054baef9dc26178761802633af75de0d02cb66cb0c74813f5f`.
- Verification: the complete final Markdown was reread from start to end after the repair. `git diff --check` passed, and each of the five newly referenced print-crop images resolves from the Markdown path. No tests were run; this work verifies transcription fidelity only and does not assess the paper's mathematical arguments.
- The repair commit preserves the paper's print-level quirks recorded in the page ledger. Image crops are used only where the OCR omitted or destroyed a printed diagram or long display.

| PDF page | Markdown repair recorded |
|---:|---|
| 4 | Restored Casson Theorem 3.1's disjoint-union notation, embedding arrow, and `(M, ∂)` domain. |
| 5 | Removed the extra standalone `Wh₄` fragment; the complete footnote 6 remains. |
| 7 | Restored the comma in `(M⁴, ∂)` in Theorem 1.2. |
| 10 | Restored the one-way compactified embedding and separation arrows. |
| 14 | Closed the parenthesis in the odd indefinite form decomposition. |
| 17 | Restored the superscript in `S³`. |
| 18 | Closed the `π₁` complement expression and restored the `D(k)` map label. |
| 20 | Restored the finite boundary-connected-sum symbol `\natural`. |
| 22 | Replaced the two missing clasp sketches with the committed source crop. |
| 24 | Restored directed arrows in the tower-inclusion sequences. |
| 25 | Restored `\natural` in `H_n` and corrected the repeated Casson Theorem 3.1 notation. |
| 26 | Restored lower-case `θ` and the one-way arrow in the normal-section formula. |
| 27 | Restored disjoint-union and one-way-map notation in Theorem 3.2 and its proof. |
| 32 | Restored one-way arrows in the succession of tower inclusions. |
| 33 | Restored the single `π₁` subscript and repaired the annulus-negligibility delimiters. |
| 38 | Removed isolated fragments duplicated by complete footnotes 8–9; restored the footnote 9 marker and Greek `ν`. |
| 40 | Rejoined the printed `D² × ∂D² / Wh_Q` frontier formula. |
| 41 | Restored the condition `k > 0`. |
| 42 | Restored the uppercase tree label in `\mathfrak{D}_Q`. |
| 43 | Corrected the pair subscript placement and restored the one-way embedding arrow. |
| 44 | Corrected the nested-embedding branch subscripts, parentheses, and casing. |
| 45 | Restored the branch label `T_{6(n+1)}^{c'}`. |
| 46 | Restored the comma in the printed interval `[.02,.1]`. |
| 47 | Restored `Fr⁺` notation and represented the lost `Δ` display with the committed source crop. |
| 49 | Restored `g(\dot{\mathfrak{D}})` in the unexplored-region terms. |
| 52 | Corrected the product-index notation, restored `j < q`, and restored the terminal `n_{k+1}` index. |
| 55 | Restored `ε` and removed stray `§7` footnote fragments. |
| 56 | Restored the collar endpoint `ε`, the set difference, and removed isolated `C ⊂ Sⁿ` / `f` fragments. |
| 57 | Restored the domain of `\bar h` and the punctured-sphere notation `S⁴ \setminus {∞}`. |
| 59 | Restored `ε(x)` in the `E_i` bound and separated the `ε`-close qualifier from the codomain. |
| 61 | Removed the duplicate math delimiter before the `ε`-close qualifier. |
| 62 | Closed the parentheses in the diameter-transfer implication. |
| 63 | Corrected `ρ(g(x)) ≤ ρ(g(y))` and the coordinates of `u`. |
| 64 | Removed the orphan `8),` fragment. |
| 65 | Restored `\mathcal{A} \cup C`, `\mathcal{B} \cup C`, `\mathcal{A} \cup C⁺`, and the source implication arrow. |
| 66 | Removed extra math delimiters and restored the subscript `i` in `T_{i+1} ⊂ interior T_i`. |
| 68 | Restored the Addendum C three-map diagram with its source crop and the printed implication arrow. |
| 70 | Reconstructed the `α₁`, `α₂`, `α₃` quotient chain and composite `α⁻` with named quotient objects. |
| 71 | Repaired the adjacent `Wh`/`S` math delimiters and restored the `α₁/₃`, `α₂/₃` map labels. |
| 74 | Restored the Addendum E/C pair diagram and the Stage 4 factoring triangle with committed source crops. |
| 78 | Restored `s⁻¹ ∘ r`, the `\mathcal{A}'` / `\mathcal{C}'` set formulas, and the missing maximum-set brace. |
| 79 | Restored `\mathcal{A} \leftrightarrow \mathcal{B}` in the symmetry tuple. |
| 81 | Restored Greek `ν`, the one-way bundle arrows, and `\bar{θ}`. |
| 82 | Restored the printed `γ \cup γ'` boundary notation. |
| 83 | Removed the extra math delimiter before `π₁`-negligible. |
| 85 | Restored the `V_n` / `W_n` end-space indices and the comma in `π₁(W_n, V_n^{(')})`. |
| 86 | Restored uppercase `V'` in the relative homology pair. |
| 87 | Restored `∂⁺z_n` in the even-index boundary formula. |
| 91 | Restored `8_{0i}^{1/7}` and `7_1^{1/7}`. |
| 94 | Repaired the barred/unbarred `D` and `A` correspondence math spans, preserving the source's visible apostrophe-s forms. |
| 95 | Restored the overbars on the modified `Z_i` chunks and corresponding `A`/`D` sphere collections. |
