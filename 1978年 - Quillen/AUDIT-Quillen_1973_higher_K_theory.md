# Peer audit — Quillen, “Higher algebraic K-theory: I”

- **Actor:** `Peer-P26`
- **Model / reasoning effort:** `gpt-6-luna / max` (task configuration)
- **Role:** contributor; `Master-Luna` is the sole canonical integrator.
- **Base:** `037602429d3b009f6fc468c732073eb3ddf9875f` (main at dispatch; this candidate remains unintegrated)
- **Source PDF:** `1978年 - Quillen/Quillen_1973_higher_K_theory.pdf` (63 PDF pages; SHA-256 `5d2db42d3fec06156da4e6f6d5a85fb9a04358df59141d3abe74a57b815bae04`)
- **MinerU Markdown:** `1978年 - Quillen/Quillen_1973_higher_K_theory_mineru/Quillen_1973_higher_K_theory__Quillen_1973_higher_K_theory.md`
- **Initial Markdown SHA-256:** `2997301e119ecea4ff88b9193f8869d0599ac520b70058bfea315efd8c1dd5d2`
- **Source mode:** scanned pages with an OCR text layer. `pdfinfo` reports Creator `85_1.tif` and Producer `Adobe Acrobat 8.0 Paper Capture Plug-in`; `pdfimages -list` reports 63 embedded 2010×3000, 1-bit CCITT page images. Per-page visual inspection uses 150dpi `pngmono` images. The OCR text layer is used only as a locator; the printed page is authoritative.
- **Scope:** one-page audit entries below and this paper's unique `audit/Quillen_1973_higher_K_theory_*` image prefix. No root progress/index file or sibling Peer asset is modified.

## Page-by-page audit

## p.001 (PDF p.1 / article p.1 / LNM p.85)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:10:20 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p001.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p001_exact_sequence.png` (short exact sequence); `audit/300dpi/Quillen_1973_higher_K_theory_p001_notation.png` (`K_0` sentence)
- **Checked:** title, author, first-page introduction through the opening of the ring applications, definition of `Q(M)`, displayed `K_i` definition, exact-category short-sequence notation, and the `K_0` Grothendieck-group statement.
- **Result: FAIL.** The printed title “Higher algebraic K-theory: I” is absent from the MinerU opening (`## Daniel Quillen*` begins the file). In the exact-sequence sentence, both printed zero endpoints in `0 → M' → M → M'' → 0` are transcribed as letter `O`. The printed subscript zero in `K_0(M)` is transcribed as lowercase `o` in `K_{o}(M)`. The 300dpi crops confirm the print glyphs are zeroes. The running head and page numerals are also omitted from Markdown; this is a non-content layout loss and is not itself graded as a mathematical error.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.002 (PDF p.2 / article p.2 / LNM p.86)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:12:04 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p002.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p002_spectral_sequence.png` (spectral-sequence target)
- **Checked:** the ring and scheme K-group definitions and formulas, spectral sequence in the introduction, Bloch formula, and continuation of the historical note and acknowledgments.
- **Result: FAIL.** In the introduction's spectral sequence, the printed target is `K'_{-n}(X)` with uppercase `X`; the MinerU formula ends in `K'_{-n}(x)` with lowercase `x`. The 300dpi crop confirms the capital. The running head and page numerals are omitted as layout metadata.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.003 (PDF p.3 / article p.3 / LNM p.87)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:13:16 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p003.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p003_proceedings.png` (closing paragraph of introduction)
- **Checked:** closing two paragraphs of the introduction, acknowledgments to Graeme Segal, references to the alternative proof approaches, and the 1973 preparation note.
- **Result: FAIL.** The printed final paragraph spells the proceedings reference `procedings`; the MinerU text normalizes it to `proceedings`. The 300dpi crop confirms the one-`e` print spelling. This is retained as a source-level print quirk and must not be “corrected” beyond a faithful transcription. The running head and page numerals are omitted as layout metadata.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.004 (PDF p.4 / contents page / LNM p.88)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:14:59 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p004.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p004_k_definition.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p004_scheme_k.png`
- **Checked:** full table of contents: section titles, subsection titles, ordering, and the displayed `K_1` entries.
- **Result: PASS±.** The table of contents agrees with the MinerU section list, including the printed `K_1(M)`, `K_1(X)`, and `K_1'(X)` labels; both 300dpi crops disambiguate the small subscript glyphs and agree with Markdown. Running heads and page numerals are omitted as layout metadata.
- **Disposition:** no content repair indicated on this page.

## p.005 (PDF p.5 / article p.5 / LNM p.89)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:17:34 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p005.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p005_zero_notation.png`
- **Checked:** §1 heading and opening paragraphs, nerve definition and diagram, ordered-set and group examples, and the homotopy-group/connected-component passage through “so far”.
- **Result: FAIL.** The body heading `§1. The classifying space of a small category` is omitted at the start of the section (it appears only in the earlier contents list). The printed `π_0(C,X)` and `π_0^C` are transcribed with letter `o` as `π_o`; the 300dpi crop confirms numeric-zero subscripts. The first glyph of printed `0-cell` versus `O-cell` remains visually ambiguous at the available 300dpi raster, so this is recorded as unresolved and is not treated as a confirmed error on this page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.006 (PDF p.6 / article p.6 / LNM p.90)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:18:46 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p006.png`
- **Checked:** end of the homotopy-group discussion, covering-space/fundamental-group heading and construction, the functor `F \ C`, both equivalences of categories, groupoid localization, Proposition 1, and the local-coefficient-system conclusion.
- **Result: PASS±.** The visible mathematical and prose content agrees with the corresponding MinerU passages; the source-page continuation and section transition are preserved. Running heads and page numerals are omitted as layout metadata.
- **Disposition:** no content repair indicated on this page.

## p.007 (PDF p.7 / article p.7 / LNM p.91)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:23:11 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p007.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p007_homology_formulas.png` (chain group and derived-limit equation); `audit/300dpi/Quillen_1973_higher_K_theory_p007_integral_formulas.png` (equations (1)–(2)); `audit/300dpi/Quillen_1973_higher_K_theory_p007_dual_category.png` (equation (3)); `audit/300dpi/Quillen_1973_higher_K_theory_p007_derived_limits.png` (lower-page context)
- **Checked:** homology heading and prose; `C_p(C,A)` chain-group display and indices; derived-colimit statement; singular homology comparison; displayed formulas (1)–(2); and the dual-category homeomorphism (3).
- **Result: FAIL.** The chain formula's printed indexed coproduct/sum sign is rendered as `\perp\perp`, and the printed chain index `X_0` is transcribed `X_o`. In the derived-colimit display, the category and degree indices are flattened into a `C/p` fraction; a detached `lim_*` fragment is also inserted as an extra display. The same index/arrow layout is corrupted in formulas (1)–(2), so the printed derived colimit and derived limit notation is not faithfully represented. In formula (3), the printed dual-category superscript is a small circle (`C^\circ`), while the MinerU formula uses digit zero (`C^0`); the 300dpi crop resolves the circle.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.008 (PDF p.8 / article p.8 / LNM p.92)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:25:54 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p008.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p008_product_map.png` (numbered equation (4)); `audit/300dpi/Quillen_1973_higher_K_theory_p008_prop3.png` (Proposition 3 limit formula)
- **Checked:** product-realization map and Proposition 2, homotopy-equivalence corollaries, filtered-colimit setup, Proposition 3 and its limit formula, proof, and following corollary.
- **Result: FAIL.** Printed equation (4) labels the product-realization map, but the corresponding MinerU display omits the equation tag. In Proposition 3, the printed first limit term is `π_n(C_i, X_i)`; the MinerU formula has `π_n(C, X_i)`, omitting the stage index `i` on the category. The 300dpi crop confirms `C_i`.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.009 (PDF p.9 / article p.9 / LNM p.93)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:27:30 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p009.png`
- **Checked:** Corollary 2 on filtering categories; the sufficient-conditions heading, definition of `Y\f` and `f/Y`, Theorem A and its dual form, simplicial-map example, fibred/cofibred-category definitions, and the concluding corollary.
- **Result: FAIL.** The printed “Corollary 2. Any filtering category is contractible” and its proof are absent from the MinerU text. Two detached displays (`I/i` and `i ↦ I/i`) remain where the proof belongs, without the explanatory sentence that connects them. In the later corollary, the MinerU algorithm block adds the unprinted and incorrect sentence “This follows from Eqn 2, Gen 1”; the print reads “This follows from Prop. 2, Cor. 1.” The intended latter sentence also survives separately as a footnote, leaving both a false extra line and a duplicate.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.010 (PDF p.10 / article p.10 / LNM p.94)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:28:52 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p010.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p010_dual_notation.png` (source/target functors and fibre categories)
- **Checked:** the arrow category `S(C)`, source and target functors and fibres, proof setup for Theorem A, realization of simplicial spaces, Lemma on bisimplicial realizations, and its proof through the representable case.
- **Result: FAIL.** In the printed fibre description, `t^{-1}(Y) = (C/Y)^\circ` uses the small-circle opposite-category symbol. The MinerU text writes `t^{-1}(Y) = (C/Y)^0` with digit zero. The 300dpi crop resolves the printed small circle.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.011 (PDF p.11 / article p.11 / LNM p.95)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:30:19 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p011.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p011_indices.png` (bisimplicial diagrams and zero subscripts)
- **Checked:** canonical presentation and end of the bisimplicial-realization lemma; construction of `S(f)` and projections; definition of `T(f)_{pq}`; both maps of bisimplicial sets and their realizations; and the homotopy-equivalence conclusions for `p_1` and `p_2`.
- **Result: FAIL.** The printed diagram indexes the initial objects `Y_0`, `fX_0`, and `X_0`; the MinerU diagram uses lowercase `o` (`Y_o`, `fX_o`, `X_o`). The 300dpi crop confirms numeric-zero subscripts. The remaining prose and the two projection arguments match the page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.012 (PDF p.12 / article p.12 / LNM p.96)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:33:28 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p012.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p012_fibre.png` (homotopy-fibre product); `audit/300dpi/Quillen_1973_higher_K_theory_p012_sequence.png` (exact sequence/basepoint); `audit/300dpi/Quillen_1973_higher_K_theory_p012_cartesian_map.png` (homotopy-cartesian map)
- **Checked:** proof of Theorem A diagram and conclusion; definition of the homotopy fibre; exact homotopy sequence and basepoint; canonical map from `B(Y\f)`; homotopy-cartesian square and its defining map; both MinerU diagram images were also visually compared with the printed page and agree.
- **Result: FAIL.** In the homotopy-fibre and homotopy-fibre-product formulas, printed product signs `×` are encoded as literal `x` in Markdown. The printed basepoint in the sequence is `\bar e` (overbar), while Markdown uses `\vec{e}` (vector arrow). The 300dpi crops confirm both glyph differences. Separately, the print itself says “homotopy-fibre of f over b” after introducing `g`; MinerU repeats that source-level wording and it is retained as a print quirk, not corrected.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.013 (PDF p.13 / article p.13 / LNM p.97)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:35:10 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p013.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p013_theoremB_sequence.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p013_corollary_sequence.png`
- **Checked:** homotopy-cartesian criterion, Theorem B square and sequence, dual corollary and its diagram/sequence, and the opening definition of quasi-fibration.
- **Result: FAIL.** In the corollary's exact homotopy sequence, both printed groups are based on `C'` (`π_{i+1}(C',Y)` and `π_i(C',Y)`). The MinerU sequence drops the prime and prints `C` in both places. The 300dpi crop confirms the primes. The embedded category-square image agrees with the PDF page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.014 (PDF p.14 / article p.14 / LNM p.98)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:37:49 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p014.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p014_lemma_objects.png` (lemma indices); `audit/300dpi/Quillen_1973_higher_K_theory_p014_proof_indices.png` (proof indices and dual-category notation)
- **Checked:** homotopy-cartesian square continuation; the realization lemma and its simplicial-space display; proof over the p-skeleton, including the face-index computation; and the opening of the proof of Theorem B.
- **Result: FAIL.** The printed lemma hypothesis is `X_i → X_{i'}`; the MinerU sentence writes `X_i → X_i`. Numeric-zero subscripts in the proof (`i_0`, `i_{j_0}`, and `X_{i_0}`) are rendered with lowercase `o`; the referenced MinerU crops `page_13_image_3.jpg` and `page_13_image_6.jpg` show the same `o`/`0` loss. At the end of the page, the printed opposite-category superscript on `C'` is a small circle (`C'^\circ`), while the MinerU text uses digit zero (`C'^0`). The 300dpi crop confirms these printed symbols.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.015 (PDF p.15 / article p.15 / LNM p.99)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:39:25 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p015.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p015_example_target.png`
- **Checked:** completion of the homotopy-cartesian diagram argument and §2 opening: exact-category definition, properties (a)–(c), and the base-change example setup.
- **Result: FAIL.** The final example line prints the target of `f` as `M''`; the MinerU text gives `M^n`. The 300dpi crop confirms the double-prime quotient-object notation. The embedded diagram `images/page_14_image_2.jpg` was visually compared with the PDF page and agrees.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.016 (PDF p.16 / article p.16 / LNM p.100)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:40:25 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p016.png`
- **Checked:** fibre-product example diagram, definition and examples of exact categories, left-exact functor category construction, and the start of the definition of `QM` via admissible epimorphism/monomorphism diagrams.
- **Result: PASS±.** The printed prose, exact-sequence notation, and opening `QM` diagram agree with the corresponding MinerU text; the embedded base-change diagram `images/page_15_image_0.jpg` also matches the print. Running heads and page numerals are omitted as layout metadata.
- **Disposition:** no content repair indicated on this page.

## p.017 (PDF p.17 / article p.17 / LNM p.101)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:42:23 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p017.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p017_morphisms.png` (zero-to-object passage and injective/surjective notation); `audit/300dpi/Quillen_1973_higher_K_theory_p017_zero_object.png` (zero-object glyph)
- **Checked:** admissible subobjects and layers, subquotients, morphisms in `QM`, injective/surjective maps and their factorizations, and the universal-property setup.
- **Result: FAIL.** The printed injective-followed-by-surjective factorization uses `u = i_! j^!`; the MinerU line transcribes the subscript `!` on `i_!` as the letter `j`, giving `u = i_j j^!`. The 300dpi crop resolves the exclamation-mark subscript. The zero-object glyph and the embedded bicartesian-square image `images/page_16_image_11.jpg` agree with the printed page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.018 (PDF p.18 / article p.18 / LNM p.102)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:45:32 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p018.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p018_fundamental_group.png` (Theorem 1 and zero-object notation)
- **Checked:** universal-property identities, dual-category isomorphism (5), the fundamental-group theorem and Grothendieck-group proof through the reduction to the full subcategory `F'`.
- **Result: FAIL.** The printed theorem identifies `π_1(B(QM), O)` with the Grothendieck group `K_0M`; the MinerU theorem uses numeral `0` for the printed capital `O` base object and omits the subscript `0` in `K_M`. In the proof setup, printed `F(O)` and `i_M: O → M` are likewise transcribed with numeral `0` in Markdown. The 300dpi crop confirms the printed `K_0` and capital-`O` glyphs.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.019 (PDF p.19 / article p.19 / LNM p.103)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:47:58 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p019.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p019_exact_sequence.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p019_definition.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p019_dual_product.png`
- **Checked:** construction of the `K_0M` action on `F(O)` and completion of Theorem 1; higher-K-group definition; exact-functor map (6); dual-category identity (7); and product identity (8).
- **Result: FAIL.** The exact-sequence quotient is printed `M''`, but the MinerU text writes `M^n`. The printed definition is `K_i M = π_{i+1}(B(QM),O)`; Markdown has `K_{i=M}`. The group-set line prints `K_0M`-set, while Markdown writes `K_0=M`-set. In (7), the printed opposite-category superscript is a small circle (`M^\circ`), rendered as digit zero (`M^0`). In (8), the print uses subscript `i` throughout; the MinerU display uses subscript `1` in place of `i`. The three 300dpi crops resolve the quotient prime, the definition/indices, the circle, and the product-formula subscripts.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.020 (PDF p.20 / article p.20 / LNM p.104)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:49:18 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p020.png`
- **Checked:** additive-functor sum, filtered-colimit identity (9), projective-module category for a ring, induced ring-homomorphism map (10), product formula (11), filtered-ring identity (12), opposite-ring identity (13), and remarks on `K_1`.
- **Result: PASS±.** The displayed formulas, indices, and prose agree with the page. The print itself repeats “by” across the line break (“defined by / by Bass and Milnor”); MinerU preserves that source-level print quirk. Running heads and page numerals are omitted as layout metadata.
- **Disposition:** no content repair indicated on this page.

## p.021 (PDF p.21 / article p.21 / LNM p.105)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:52:01 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p021.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p021_pushout.png` (short exact sequence and pushout diagram)
- **Checked:** §3 heading and exact-category-of-sequences construction; Theorem 2 statement and proof through the pushout defining `i_*E`.
- **Result: PASS±.** The prose, maps, and pushout diagram agree with the printed page. The round glyphs at the two ends of the printed short-sequence diagram remain ambiguous between `O` and `0` at 300dpi; Markdown uses `O`, so I record the uncertainty without treating it as a confirmed mismatch. Running heads and page numerals are omitted.
- **Disposition:** no confirmed content repair indicated on this page; retain the `O`/`0` glyph question for final residual-unknown reporting.

## p.022 (PDF p.22 / article p.22 / LNM p.106)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:55:38 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p022.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p022_sequences.png` (pushout/short-exact-sequence diagrams and additivity statement)
- **Checked:** completion and uniqueness of the pull-back adjoint construction; the initial-object argument finishing Theorem 2; Corollary 1 and its split-sequence proof; and the beginning of the pointwise-filtration discussion. The embedded pull-back diagram `images/page_21_image_2.jpg` was compared with the printed page and agrees.
- **Result: PASS±.** The prose, formulas, and diagrams agree with the page. The short-sequence endpoint glyphs match the MinerU `O` notation at the crop level. Running heads and page numerals are omitted.
- **Disposition:** no content repair indicated on this page.

## p.023 (PDF p.23 / article p.23 / LNM p.107)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 16:58:10 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p023.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p023_products.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p023_graded_ring.png`
- **Checked:** additivity corollaries 2–3, vector-bundle action and product (1), graded-ring notation and module statement, and the proposition/decomposition through the start of its proof.
- **Result: FAIL.** In the vector-bundle/graded-ring passages, printed `K_i` is transcribed `K_1`, printed `K_0` as `K_o`, and the printed `A_0`/`F_0` indices are rendered with lowercase `o`. The proposition's domain `K_i A_0` is flattened as `K_{iA_0}`. The graded-module decomposition's indexed direct-sum sign is rendered as `\prod`. The 300dpi crops confirm the indices, argument grouping, and operator-symbol difference.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.
- **Audit update (2026-10-01 17:01:29 -0400):** corrected the page allocation of the finite direct-sum/union discrepancy: it belongs to the page-24 proposition proof, not p.23; it is not part of this page's FAIL list.

## p.024 (PDF p.24 / article p.24 / LNM p.108)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 17:15:35 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p024.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p024_finite_sum.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p024_short_sequence.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p024_theorem3.png`
- **Checked:** graded-ring proposition proof and finite-layer sum; start of §4 and resolution setup; Theorem 3 hypotheses and conclusion.
- **Result: FAIL.** The finite-layer expression printed as an indexed direct sum is rendered `\bigcup` in Markdown. The printed exact sequence has numeric-zero endpoints `0`, but Markdown uses capital `O`. Theorem 3's printed assumption i) (“if `M` is in `P`, then `M'` is in `P`” for an exact sequence) is omitted entirely; the theorem conclusion also underlines the `i` in `K_i`, which is not underlined in print. The 300dpi crops confirm these differences.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.025 (PDF p.25 / article p.25 / LNM p.109)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 17:53:21 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p025.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p025_indices_factorization.png`
- **Checked:** Theorem 3 proof, the ordered set of admissible layers and its natural transformations, the factorization of a map in `QM`, and the dual-category fibre-product argument.
- **Result: FAIL.** The printed layer and quotient indices `M_0`, `P_0`, and `P_{i_0}` are transcribed as lowercase `o` in several displays. In the factorization `u = i_!j^!`, the exclamation-mark subscript on `i_!` is read as the letter `j`, producing `i_j`. The 300dpi crop resolves the numeral-zero and exclamation-mark glyphs.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.026 (PDF p.26 / article p.26 / LNM p.110)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 18:50:08 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p026.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p026_resolution_indices.png` (resolution-category indices and Corollary 2)
- **Checked:** projective-resolution lemma (1)–(3) and proof diagrams; the passage from `P_{=n}` to `P_{=n+1}`; the union category `P_\infty(A)`; and Corollary 2 for regular rings.
- **Result: FAIL.** The printed iteration is `K_i P_{=n} → K_i P_{=n+1}`; the MinerU line moves `=n` into the K index as `K_{i=n}`. The printed union is `P_\infty(A)=\bigcup_n P_{=n}(A)`, while Markdown has `P_{=00}(A)=\bigcup_{=n}P(A)`. Corollary 2 is stated for `K_i(P_{=n}(A))` for `0≤n≤∞`; Markdown drops the `=n` category index and gives `K_i(P(A))`. The proof also transcribes some printed `0` subscripts as `o` (for example `P_0` as `P_o`); the 300dpi crop confirms the zero indices.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.027 (PDF p.27 / article p.27 / LNM p.111)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 19:36:03 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p027.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p027_infinity.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p027_transfer_corollary.png`
- **Checked:** regular-ring consequence and scheme comparison, transfer maps (3)–(4), tensor product/projection formula (5), Corollary 3 and its acyclicity conclusion, and the start of the finite-Tor application.
- **Result: PASS.** On repair-phase recheck, the cited print crops and the Markdown agree on `P_\infty(A)=Modf(A)`, the indexed K-groups in (3)–(5), Corollary 3 and the finite-Tor transition. The earlier listed discrepancies were not present in the checked Markdown and are withdrawn. No content repair is indicated; running heads and page numerals are omitted.
- **Disposition:** no content repair indicated on this page after recheck; the earlier listed discrepancies are withdrawn.

## p.028 (PDF p.28 / article p.28 / LNM p.112)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 20:08:04 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p028.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p028_devissage.png` (Theorem 4 filtration endpoint)
- **Checked:** finite-Tor conclusion, §5 Devissage setup, Theorem 4 filtration and quotient condition, proof via layers `J(M)`, and the induced functors `r` and `s`.
- **Result: FAIL.** The printed filtration ends with `M_n = M`; the MinerU theorem statement ends with `M_n = N`. The 300dpi crop confirms the terminal object is `M`.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.029 (PDF p.29 / article p.29 / LNM p.113)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 20:32:14 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p029.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p029_localization_sequence.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p029_dedekind_sequence.png`
- **Checked:** end of the finite-Tor application; Theorem 5 localization sequence and explanatory note; Dedekind-domain example and residue-field terms; and the opening of the proof of Theorem 5.
- **Result: FAIL.** The printed localization sequence contains the indexed groups `K_{i+1}(A/B)`, `K_iB`, `K_iA`, and `K_i(A/B)` with their maps. The MinerU line collapses this to `s* K_1(A/B) → K_B e* K_A s* K_0(A/B) → O`, losing the intermediate group indices/maps and changing `i` to `1`/`0`. In the Dedekind example, the printed indexed coproduct/sum of `K_i(A/m)` is rendered `\bigsqcup_m`; the 300dpi crop preserves the source operator for manual reconstruction.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.030 (PDF p.30 / article p.30 / LNM p.114)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 20:51:30 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p030.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p030_categories_layers.png` (opposite-category notation and layer indices)
- **Checked:** reduction of condition (a) to injective maps; dual-category step; definition of `F_V` and Lemma 1; ordered-layer description and directedness; non-emptiness argument and transition to the auxiliary categories.
- **Result: FAIL.** The printed opposite-category superscripts in `Q((A/B)^\circ) = Q(A^\circ/B^\circ)` are small circles. The MinerU text uses digit zero in all three positions (`(A/B)^0`, `A^0`, and `B^0`). The 300dpi crop resolves the circles.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.031 (PDF p.31 / article p.31 / LNM p.115)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 21:35:49 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p031.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p031_auxiliary_category.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p031_layer_indices.png`
- **Checked:** Lemma 2 and the pushout construction; Lemma 3 and the ordered set of subobjects; Lemma 4 and its map on `E_N`; and the opening definition of `I_V`.
- **Result: PASS±.** The prose, displayed maps, indices, and auxiliary pushout diagram agree with the printed page. The embedded diagram `images/page_30_image_3.jpg` was checked against the PDF and agrees. Running heads and page numerals are omitted.
- **Disposition:** no content repair indicated on this page.

## p.032 (PDF p.32 / article p.32 / LNM p.116)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-01 22:43:48 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p032.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p032_image_subobject.png` (image notation); `audit/300dpi/Quillen_1973_higher_K_theory_p032_choice_phi.png` (φ choice); `audit/300dpi/Quillen_1973_higher_K_theory_p032_phi_choice.png` (lower-page context); `audit/300dpi/Quillen_1973_higher_K_theory_p032_graded_rings.png` (auxiliary lower-page context; despite the basename, this crop shows the Theorem 5 conclusion, not §6)
- **Checked:** the filtered indexing category `I_V`; functors `p(N,φ)` and the colimit/isomorphism argument; Lemma 5; and the final homotopy-commutative diagram completing the localization theorem.
- **Result: FAIL.** The printed choice is `(N, φ)` with a Greek phi; the MinerU text says `(N, \emptyset)`. In the object-equalization step, printed `Im(h-h')` (the image) is transcribed `I_m(h-h')`. The 300dpi crops resolve both the glyph and operator.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.033 (PDF p.33 / article p.33 / LNM p.117)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:10:27 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p033.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p033_graded_symbols.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p033_tensor_formula.png`
- **Checked:** §6 opening and graded-ring conventions; the `T_i` definition; `T_0(N)_n`, filtration `F_pN`, formulas (1)–(2); Lemma 1 hypotheses; and formulas (3)–(4) in its proof.
- **Result: FAIL.** Numeric-zero subscripts in `T_0`, `N_0`, and `F_0` are transcribed with lowercase `o` in the displayed graded-module formulas. In formula (4), the printed tensor product `B \otimes_k T_0(N)` is rendered as `B \oplus_k T_o(N)`. The 300dpi crops confirm the zero indices and tensor sign.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.034 (PDF p.34 / article p.34 / LNM p.118)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:14:44 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p034.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p034_tor_indices.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p034_theorem6.png`
- **Checked:** end of Lemma 1's Tor argument; graded-module K-group statement (5); Theorem 6 and its proof; and Lemma 2 through its finite-projective-resolution conclusion.
- **Result: FAIL.** The displayed Tor indices are printed `T_0` in formulas including `T_0(F_pN)_n` and `T_0(B(-p)⊗_k T_0(N)_p)`, but the MinerU text uses lowercase `o` (`T_o`) in these positions. The 300dpi crops confirm the numeric-zero subscripts; the surrounding sequence, theorem hypotheses, and proof steps otherwise agree on this page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.035 (PDF p.35 / article p.35 / LNM p.119)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:17:13 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p035.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p035_tor_zero.png`
- **Checked:** Lemma 2's finite graded-projective resolution proof; the filtered-ring definitions; Lemma 3's assertions (i)–(iii); and the filtered-module construction through exact-sequence (6).
- **Result: FAIL.** Printed degree-zero Tor subscripts (`T_0`) are rendered as lowercase letter `o` in Lemma 2's exact sequence, its `T_0(N_d)` statement, and the nearby filtration formulas. The 300dpi crop confirms these are numeric zeroes.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.036 (PDF p.36 / article p.36 / LNM p.120)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:19:29 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p036.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p036_tor_zero.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p036_theorem7.png`
- **Checked:** Lemma 3 parts (ii)–(iii) and exact Tor sequence; Lemma 4; Theorem 7 hypotheses and initial proof.
- **Result: FAIL.** Printed degree-zero Tor indices `T_0` in Lemma 3's sequence and conclusion are repeatedly transcribed with lowercase `o` (`T_o`) in Markdown. The 300dpi crop resolves these as numeric zeroes; the remaining displayed maps and theorem hypotheses match on this page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.037 (PDF p.37 / article p.37 / LNM p.121)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:22:15 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p037.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p037_associated_graded.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p037_localization_sequence.png`
- **Checked:** completion of the construction and proof for Theorem 7; the filtered subring `A'`; associated-graded formula; localization sequence (8); and the computation of `i_*` through the comparison diagram.
- **Result: FAIL.** The printed subring uses the filtration term `F_nA` in each `z^n` summand; the MinerU expression loses the `n` and writes `F_A`. The printed associated-graded formula is an indexed coproduct/sum over `p≤n`; the MinerU text renders it as a fraction with numerator `1` over `p≤n`. The 300dpi crops confirm the filtration index and sum operator.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.038 (PDF p.38 / article p.38 / LNM p.122)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:40:45 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p038.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p038_theorem8.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p038_localization_diagram.png`
- **Checked:** Examples on filtered enveloping and Heisenberg-Weyl algebras; Theorem 8 statements (i)–(ii); localization diagram and split exact-sequence argument; regular-ring corollary; twisted polynomial exercise and sequence (9); the transition to Example 1 through the definition of the twisted polynomial ring.
- **Result: PASS.** The displayed isomorphisms, map labels, primes, indices, direct-sum sign, diagram arrows, and sequence (9) agree with the print. The prose and opening of Example 1 through `q = p^d` also match; no material omission or transcription difference was found on this page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.039 (PDF p.39 / article p.39 / LNM p.123)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:42:53 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p039.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p039_frobenius_split.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p039_characteristic_sequences.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p039_phi_tensor.png`
- **Checked:** Example 1's quotient-category localization sequence (10); the canonical decomposition of `V`; the Frobenius-fixed-vector isomorphism and category equivalence; both characteristic exact sequences; the induced map on K-groups and the exact sequence from [Quillen 2]; and all formulas in (11).
- **Result: FAIL.** The print's `V_0` is transcribed as `V_o`; the isomorphism `k⊗_{F_q}V^F→V_1` has lowercase `v` in place of both printed `V`s; and `K_iF_q` in the devissage conclusion is rendered `K_iF_g`. The text adds a superscript `q` to `φ(V)`, absent from print. In the second characteristic sequence, the three printed tensor bases `F_q` are rendered without their `q` subscripts; both displayed sequences also use capital letter `O` at endpoints where print has numeric `0`. The category product `×` is written as plain `x`. The localization sequence and the final K-group formulas (11) otherwise match this page.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.040 (PDF p.40 / article p.40 / LNM p.124)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:45:08 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p040.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p040_example2_sequence.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p040_section7_definitions.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p040_maps_pairings.png`
- **Checked:** Example 2's localization short exact sequence and direct-sum index set; §7 definitions of `K_qX`, `K'_qX`, `P(X)`, and `M(X)`; comparison map (1.1) and regular-scheme explanation; pairing (1.2) and module statement; and the functoriality paragraph and map (2.1).
- **Result: FAIL.** The direct-sum sign in Example 2 is rendered as `\perp`. In the §7 definitions, the Markdown adds `=` in `K_{q=}P(X)` and `K_{q=}M(X)`, and adds `=` to `O_{=X}`. Formula (1.1) places `X` as a superscript on the K-groups rather than writing `K_qX→K'_qX`; formula (1.2) likewise has superscript `X` and renders the printed numeric-zero subscript in `K_0X` as lowercase `o`. The prose and map (2.1) match; no other omission was found in the checked section.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.041 (PDF p.41 / article p.41 / LNM p.125)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:47:22 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p041.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p041_prop22.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p041_prop25_tor.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p041_prop27.png`
- **Checked:** Proposition 2.2 and formulas (2.3)–(2.4), including its filtered-category proof; §2.5's finite-Tor-dimension condition and pullback map (2.6); and §2.7's proper-pushforward setup through the K-group isomorphism.
- **Result: FAIL.** Formula (2.3) drops the printed `q` indices from both K-groups. In the proof's concluding equality for 2.3, the Markdown changes both printed `K_q` indices to `K_{q=1}`. The Tor vanishing condition is encoded as `Tor_i` with malformed `\stackrel{0}{=}Y` and `\underset{\sim X}{0}` constructions rather than the printed `Tor_i^{O_Y}(O_X,F)`. Formula (2.6) places `Y` and `X` as superscripts on `K'_q`, instead of the printed `K'_qY→K'_qX`. At the start of §2.7, the isomorphism omits `q` from both `K_qF(X,f)` and `K'_qX`. The remaining checked proof prose and (2.4) agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.042 (PDF p.42 / article p.42 / LNM p.126)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:50:23 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p042.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p042_assumptions_29.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p042_projection_formula.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p042_derived_formula.png`
- **Checked:** completion of §2.7 and map (2.8); cases (i)–(ii), including the vector-bundle sequences (2.9); Proposition 2.10 and its hypotheses; its K-group class calculation, Tor-defined subcategory, resolution sequence, and the derived-category projection-formula line at the page end.
- **Result: FAIL.** A repair-phase recheck of the crop confirmed that formula (2.8) in the Markdown, `K'_qX→K'_qY`, matches print; the original discrepancy claim about superscript `X`/`Y` was mistaken and no edit is indicated there. In case (ii), the epimorphism uses printed `O_X` but Markdown has `Q_X`; the following vector-bundle sequence also has `O_X` rendered as `0_X`. The vanishing condition is `R^i f_*(F(n))=0` for `i>0`, but the Markdown changes the exponent to `1`. Proposition 2.10 uses `K_0X` and `K_0Y`, whereas the statement and induced homomorphism use superscript `X`/`Y`; the alternating resolution class is placed in `K_0X` instead of printed `K_0Y`. The Tor conditions defining `L` are malformed as `\stackrel{O}{=}Y` and `\underset{\equiv X}{O}` constructions. In the displayed resolution sequence, printed `P_0` is transcribed as `P_o`. The derived-category formula at the page end matches the print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.043 (PDF p.43 / article p.43 / LNM p.127)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:52:16 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p043.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p043_pushforward_formula.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p043_base_change.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p043_closed_subschemes.png`
- **Checked:** completion of Proposition 2.10's proof; Proposition 2.11's square, Tor-independence condition, induced map and sketch; §3 opening, Proposition 3.1, and Proposition 3.2 through the start of its proof. The embedded diagram `images/page_42_image_3.jpg` matches the printed square.
- **Result: FAIL.** In the displayed (R^qf_*) case formula, Markdown has `E⊗f^*E` where print has `E⊗f^*F`. The Tor-independence condition is encoded with malformed `\stackrel{\underline{O}}{=}Y,y` and related subscript constructions instead of the printed `Tor_i^{O_{Y,y}}(O_{Y',y'},O_{X,x})=0`. The map in Proposition 2.11 places `X` and `Y'` as superscripts on `K'_q`; print writes `K'_qX→K'_qY'`. In §3, the ideal sheaf is said to lie in `Q_X` rather than printed `O_X`. Proposition 3.1 omits `q` from both K-groups in the isomorphism and its `X_red` consequence. The checked exact sequence (3.3) and its displayed maps match the print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.044 (PDF p.44 / article p.44 / LNM p.128)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:54:39 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p044.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p044_mayer_spectral.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p044_homotopy_limit.png`
- **Checked:** completion of Proposition 3.2's proof; Remarks 3.4–3.5, including the Mayer–Vietoris sequence and spectral sequence; Gersten's K-group notation; and Proposition 4.1 and its reduction to the generic point and §6 Theorem 8.
- **Result: FAIL.** The Mayer–Vietoris middle term is printed `K'_qU ⊕ K'_qV`, but Markdown has a damaged `K'_q∪K'_qV` expression. Gersten's groups are printed with subscript `q`, but the Markdown uses `α`. Proposition 4.1 omits `q` from both K-groups in its isomorphism. In its generic-point reduction, the first colimit has `K'U` rather than `K'_qU`; the second writes `K'p_qU` rather than `K'_qP_U` and encodes `×_X` as `x_X`; the concluding left group `K'k` also omits `q`. The checked fibration, spectral-sequence display, and exact-sequence diagram otherwise agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.045 (PDF p.45 / article p.45 / LNM p.129)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:56:23 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p045.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p045_projective_formulas.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p045_koszul_sum.png`
- **Checked:** §4.2's Jouanolou comparison; Proposition 4.3, formulas (4.4)–(4.5); its projective-bundle proof, exact sequence (4.6), Theorem 6 square, Koszul resolution, and the resulting direct-sum isomorphism and functors.
- **Result: FAIL.** §4.2's concluding equality omits `q` from both printed groups `K_qX=K'_qX`. Formula (4.4) renders the numeric-zero subscripts in `K_0(PE)` and `K_0X` as lowercase `o`. The Koszul resolution ends in numeric `0`, but Markdown has capital `O`. In the final direct-sum isomorphism, the printed direct-sum operator is rendered as `Ⅱ`; the functor uses `Q(-1)^{\mathfrak M^1}` instead of printed `O(-1)^{\otimes i}`, and the printed bound `0≤i<r` is rendered with letter `O`. The checked formulas (4.5)–(4.6), square, and Koszul terms otherwise agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.046 (PDF p.46 / article p.46 / LNM p.130)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 00:58:30 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p046.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p046_radicial_map.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p046_tensor_filtration.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p046_support_filtration.png`
- **Checked:** Proposition 4.7 and its exact-sequence diagram; Proposition 4.8's two composites and filtered tensor-functor proof; and the §5 support-filtration definition and formula (5.1).
- **Result: FAIL.** Proposition 4.7 prints `radicial`, but Markdown says `radical`. Proposition 4.8 loses the superscript on the pullback stars in both composites, writing `f_* f*` and `f * f_*`; the tensor-functor display also inserts a comma before `V`. The associated-graded functor is a direct sum over `n` in print, but Markdown uses `\prod_n`. In §5, the printed double-underlined category notation `\underline{\underline M}_p(X)` is rendered as `\underset{=p}{M}(X)`; the surrounding prose correctly states the support-codimension condition `≥p`, but the displayed category symbol is corrupted. Formula (5.1) also omits `q` from the right-hand `K'_qZ`. The exact-sequence diagram and remaining checked terms match the print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.047 (PDF p.47 / article p.47 / LNM p.131)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:01:54 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p047.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p047_support_spectral.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p047_proof_sequence.png`
- **Checked:** formulas (5.2)–(5.3) and their codimension argument; Theorem 5.4's spectral-sequence statement and range; and the filtration, quotient-category equivalence, K-group identification, and first exact sequence in its proof.
- **Result: FAIL.** The printed double-underlined categories `\underline{\underline M}_p(X)` and `\underline{\underline M}_{p+1}(X)` are repeatedly encoded as `\underset{=p}{M}` / `\underset{=p+1}{M}`; the surrounding prose correctly gives the support condition `codimension ≥p`, but these displayed category symbols are corrupted. In (5.5), the printed direct sum `\bigoplus_{x\in X_p}` is rendered as a fraction with two vertical strokes over `x∈X_p`. The direct-sum operator in the proof's exact sequence is also rendered as a single vertical-stroke symbol. The checked codimension arguments, target group, and range conditions otherwise match print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.048 (PDF p.48 / article p.48 / LNM p.132)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:04:24 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p048.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p048_gersten_criterion.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p048_sheaf_resolution.png`
- **Checked:** completion of Theorem 5.4's proof; Proposition 5.6's equivalent conditions and sequence (5.7); Proposition 5.8's sheaf and cohomology statement, sheafified resolution (5.9), and proof through its asserted isomorphism; and Conjecture 5.10.
- **Result: FAIL.** In condition (ii) of Proposition 5.6, the printed edge map starts at `K'_{-q}X` and targets `E_2^{0q}(X)`; Markdown drops the minus sign and uses letter `O` in place of zero. Sequence (5.7) prints direct sums over `X_0` and `X_1`, but Markdown uses products and transcribes `X_0` as `X_o`. Proposition 5.8 changes uppercase `X` to lowercase `x` in `E_2^{pq}(X)=H^p(X,K'_{-q})`; its local-ring term is encoded as `O_{\underline{x},x}` instead of `O_{X,x}`. The presheaf in the definition omits the printed `n` from `U↦K'_nU`, and the sheaf index notation is rendered with a literal `=n` under `K'`. The checked spectral-sequence argument and Conjecture 5.10 otherwise match.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.049 (PDF p.49 / article p.49 / LNM p.133)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:07:09 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p049.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p049_base_extension.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p049_reduction_lemma.png`
- **Checked:** Theorem 5.11's reduction to the smooth case and finitely generated subfields; its filtered-colimit argument; the support-filtration reductions and zero-map goal; and Lemma 5.12 through its statement and the setup `B'=R/tR`, `R'=R⊗_B B'`.
- **Result: FAIL.** Each printed base extension uses `k'`—`R=k⊗_{k'}R'`, `A=k⊗_{k'}A'`, and `k_i⊗_{k'}A'` in the colimit for `A` and its K-groups. Markdown instead encodes these tensors with `\otimes_k,`, losing the prime on `k'` and inserting a comma. The reduction crop prints the functor `M_{p+1}(R)→M_p(A)`; the OCR category symbols are corrupted as literal `=p+1`/`=p` forms, but the target object `A` matches print. The same bad category markers occur in the displayed `K_*(M_{p+1}(R))`/`K_*(M_p(R/tR))` limit. The remaining checked reduction and Lemma 5.12 statements match the print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.050 (PDF p.50 / article p.50 / LNM p.134)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:09:02 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p050.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p050_exact_sequence.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p050_filtration_proof.png`
- **Checked:** Theorem 5.11's exact-functor sequence (*) and its zero-map consequence; the proof of Lemma 5.12, including the filtration, associated-graded dimension and parameter lifts; and the end of the lemma proof. The embedded diagram `images/page_49_image_0.jpg` matches the printed square.
- **Result: FAIL.** Sequence (*) prints the tensor bases `B'` in `I_f⊗_{B'}M` and `R'_f⊗_{B'}M`; Markdown writes `\otimes_{B,M}`, losing the prime and moving `M` into the subscript. In the projective closure formula, the printed graded direct sum `\bigoplus_n F_n(R/tR)` is rendered as `\coprod_n F_n(R/tR)`. The repair-phase recheck also found that the support-category subscripts `M_p(B')` and `M_p(R'_f)` are written with literal `=p` markers in Markdown; the crop shows subscript `p`. The remaining checked exact-sequence maps, dimension argument, parameter lifts, and final finiteness assertion agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.051 (PDF p.51 / article p.51 / LNM p.135)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:10:53 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p051.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p051_chow_groups.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p051_multiplicity.png`
- **Checked:** Theorem 5.13 and its power-series argument; the Chow-ring setup; Proposition 5.14's `d_1` map and Chow-group conclusion; and its proof through formula (5.15) and the definition of `ord_{yx}`.
- **Result: FAIL.** Theorem 5.13's hypothesis uses printed `0≠t`, but Markdown has capital `O`. Proposition 5.14 prints direct sums in all three terms of `d_1`; Markdown uses products. In the linear-equivalence proof, the printed `W_0` is rendered `W_o` in the cycle difference and intersection terms. In (5.15), `W_0` is again `W_o`, and the printed valuation index `yx` is rendered `vx`. The local-ring term in the valuation definition is also malformed as `\mathbb{O}_{\geq Y,X}` instead of printed `O_{Y,x}`. The checked prose and remaining terms of (5.15) agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.052 (PDF p.52 / article p.52 / LNM p.136)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:13:24 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p052.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p052_chow_differential.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p052_local_ring_boundary.png`
- **Checked:** the homomorphism identifying linearly equivalent cycles with the image of `d_1`; both commutative diagrams comparing the spectral sequences; and Lemma 5.16's exact sequence, valuation map, and proof through the flat polynomial-ring map.
- **Result: FAIL.** In the printed diagrams, the spectral-sequence terms are `E_1^{0,-1}(Y)` and `E_1^{0,-1}(O_{Y,x})`; Markdown uses capital letter `O` instead of numeric zero in these first indices. The remaining checked maps, valuation index `yx`, and exact sequence agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.053 (PDF p.53 / article p.53 / LNM p.137)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:16:39 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p053.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p053_boundary_calculation.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p053_chow_formula.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p053_boundary_diagram.png`
- **Checked:** completion of Lemma 5.16's proof and its boundary diagram; Remark 5.17; Theorem 5.19 and its `p=0,1,2` examples. The embedded boundary diagram `images/page_52_image_0.jpg` matches the printed maps and layout.
- **Result: FAIL.** A repair-phase check found no `0≠t` discrepancy on p.53; the single occurrence belongs to Theorem 5.13's passage on p.51 and is repaired there. In the `p=0,1` examples following Theorem 5.19, print has `H^1(X,O_X^*)=Pic(X)`, while Markdown substitutes `\mathbb{Q}_X^*` for `O_X^*`. The checked boundary-map computation, Remark 5.17, and remaining examples agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.054 (PDF p.54 / article p.54 / LNM p.138)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:18:22 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p054.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p054_lemma11.png`
- **Checked:** §8's introductory scope; subsection 1's canonical projective-bundle setup; Lemma 1.1 (a)–(d), including direct-image formula (c); and the regularity definition and example.
- **Result: FAIL.** The final sentence of Lemma 1.1(c) identifies the printed symbol `∨` as denoting the dual vector bundle, but Markdown uses `▼`. The surrounding direct-image cases, tensor factors, hypotheses, and regularity statement match the print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.055 (PDF p.55 / article p.55 / LNM p.139)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:21:19 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p055.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p055_z_sequence.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p055_resolution_tail.png`
- **Checked:** Lemma 1.2's regularity criteria and long exact sequence; Lemma 1.3's Koszul sequences and induction; Lemma 1.7's surjectivity proof; and the opening of the general resolution setup at the page end.
- **Result: FAIL.** In Lemma 1.3's split short exact sequences, print consistently uses uppercase `Z_p` and `Z_{p-1}`; Markdown writes lowercase `z_p` and `z_{p-1}`, despite retaining uppercase `Z_0` in the subsequent equality. The final displayed resolution on the page ends in numeric `0`, but Markdown has capital `O`. The SE-module map uses `\coprod` instead of print's `\bigoplus`; in this module category these denote the same direct-sum object.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.056 (PDF p.56 / article p.56 / LNM p.140)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:23:50 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p056.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p056_resolution_functor.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p056_derived_sequences.png`
- **Checked:** the acyclic resolution and sequences (1.8); the inductive definitions of `Z_n` and `T_n`; sequences (1.9)–(1.10); the higher-direct-image argument proving `Z_{r-1}=0`; and Proposition 1.11.
- **Result: FAIL.** The printed acyclic functor is `R^q f_*(O_X(n))`; Markdown substitutes `\ref{eq:0}` and omits `(n)`. The printed `T_0` is rendered `T_o` in the first applied resolution, sequence (1.8), and the final resolution in Proposition 1.11. In the exact sequence derived from (1.9), the last term is printed `R^q f_*(O_X(-q)⊗_S T_{n+q})`, but Markdown renders the tensor portion as `@ S^T n+q`. The remaining checked maps and resolution terms agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.057 (PDF p.57 / article p.57 / LNM p.141)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:26:21 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p057.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p057_lemma12.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p057_lemma13.png`
- **Checked:** Lemma 1.12's threshold and assertions (a)–(c), its proof through flatness and finite presentation; and Lemma 1.13's vanishing hypothesis, dual Koszul sequence, and decreasing-induction conclusion.
- **Result: FAIL.** Lemma 1.12's printed threshold is `n_0` in both occurrences; Markdown writes `n_\circ` initially and drops the subscript in `n≥n`. Assertions (a) and (b) replace printed tensor products `⊗_S` with `@`. In the proof, the quotient generator is printed `O_X(-n)^k`, but Markdown has `Q_X(-n)^k`. Lemma 1.13 assumes `R^q f_*(F(n))=0` for `q>0`; Markdown changes this to `q≥0`. The remaining checked proof steps and sequence terms match print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.058 (PDF p.58 / article p.58 / LNM p.142)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:29:28 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p058.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p058_theorem_statement.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p058_lemma22_proof.png`
- **Checked:** Lemma 1.14; Theorem 2.1 and its projective-bundle isomorphism; the definitions of `P_n` and `R_n`; Lemma 2.2, including sequence (2.3) and its inverse maps; and the injectivity/surjectivity argument for the main homomorphism through the displayed formula for `V_nU_m`.
- **Result: FAIL.** Across Lemma 2.2 and its proof, the printed category subscripts `R_n`, `P_n`, `P_0`, and the corresponding K-groups are rendered with missing subscripts or literal `=n`/`=0` forms (for example, `K_q(P=n)` and `K_q(R)=0`). In the exact functor for `p>0`, print has `F(p)⊗_S\Lambda^pE`, while Markdown writes `F(p)_S\wedge^pE`, losing the tensor operator. The projective-bundle theorem statement and its displayed map match print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.059 (PDF p.59 / article p.59 / LNM p.143)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:31:46 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p059.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p059_line_bundle_theorem.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p059_triple_sequence.png`
- **Checked:** completion of the projective-bundle theorem's surjectivity proof; the `R_0`/`P_0` K-group map; §3's projective-line-over-a-ring setup; Theorem 3.1's isomorphism and relation (3.2); and the noncommutative exact sequence and cohomology-complex definition.
- **Result: FAIL.** In the final projective-bundle proof, printed subscripts `R_0` and `P_0` are dropped or encoded as literal `=0` in the K-group homomorphism and inclusion. In Theorem 3.1, printed `h_0` is rendered `h_o`. In the noncommutative exact sequence and its defining morphisms, printed `X_0` is rendered `X_o` (including the map label `(X_1,-X_o)` and the term `X_o\,pr_1`). The remaining checked maps and relation (3.2) match print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.060 (PDF p.60 / article p.60 / LNM p.144)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:34:12 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p060.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p060_descent_square.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p060_azumaya_algebra.png`
- **Checked:** §4's Severi–Brauer definition; construction of the vector bundle `J`; the faithfully-flat cartesian square and its embedded diagram; and the definition and base-change calculation for the Azumaya algebra `A`, through the start of the `J_n`/`A_n` discussion. The embedded square `images/page_59_image_4.jpg` matches the printed diagram.
- **Result: FAIL.** The pullback identity printed as `g'^*J=O_{X'}(-1)⊗_{S'}E` is encoded as a malformed `\underset{=X,(-1)}{O}_{S'},E` construction. In the following calculation of `g^*(A)^{op}`, Markdown inserts commas into the `End_{X'}` and `⊗_{S'}` expressions, so the displayed pullback algebra identity is not faithfully transcribed. The checked Severi–Brauer setup, descent square, Azumaya rank, and `f^*A=End_X(J)^{op}` statement otherwise match.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.061 (PDF p.61 / article p.61 / LNM p.145)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:36:32 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p061.png`
- **300dpi print crops:** `audit/300dpi/Quillen_1973_higher_K_theory_p061_azumaya_functor.png`; `audit/300dpi/Quillen_1973_higher_K_theory_p061_resolution.png`
- **Checked:** the `J_n` module functor and Theorem 4.1; the comparison with projective bundles; resolution (4.2) and the recursive definitions of `T_n(F)` and `Z_n(F)`; the descended vector-bundle exact sequence; and the genus-zero Severi–Brauer example.
- **Result: FAIL.** In the recursive definition, the printed `Hom_{A_n}(J_n,Z_{n-1}(F))` is rendered as `\mathrm{nom}_X(J_n,Z_{n-1}(F))`, losing the initial `H` and changing the subscript from `A_n` to `X`. Resolution (4.2) uses printed `T_0(F)`, but Markdown has `T_o(F)`. The descended exact sequence ends in `O_X`, while Markdown encodes the term as `\underset{X}{\circ}`. The checked K-group decomposition and example otherwise match print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.

## p.062 (PDF p.62 / article p.62 / LNM p.146)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:38:43 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p062.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p062_references.png`
- **Checked:** References from H. Bass through the start of D. Quillen 3, including author names, titles, journal/book details, years, page ranges, and continuation markers.
- **Result: PASS.** The bibliographic entries and their order agree with print. The Quillen 3 reference continues from the final `Proc.` at the bottom of this page into the following page's `Amer. Math. Soc.`; the Markdown preserves the continuous citation.
- **Disposition:** no content edits indicated for this page.

## p.063 (PDF p.63 / article p.63 / LNM p.147)

- **Actor / time:** `Peer-P26 | gpt-6-luna/max` · 2026-10-02 01:41:40 -0400
- **150dpi page image:** `audit/Quillen_1973_higher_K_theory_p063.png`
- **300dpi print crop:** `audit/300dpi/Quillen_1973_higher_K_theory_p063_final_references.png`
- **Checked:** completion of the Quillen 3 reference; Roberts and Segal entries; Swan and Tornehave; the EGA/SGA source keys; and the final institutional imprint.
- **Result: FAIL.** The printed `SGA 6` entry carries forward `Lecture Notes in Math.` with a ditto line from `SGA 1`; Markdown gives only `SGA 6: 225 (1971)`, omitting the series. The printed `Segal 2` entry also has a continuation marker tying it to G. Segal, but Markdown writes only `2:`. The remaining checked reference details, including the MIT imprint and the continuation of the Quillen 3 citation, agree with print.
- **Disposition:** record only at this audit stage; content edits wait until the full 63-page audit is complete.
## Fix Register

- **Raw MinerU Markdown:** commit a33f22f3b0bcf430149ea06d98e65076266acc9e; SHA-256 2997301e119ecea4ff88b9193f8869d0599ac520b70058bfea315efd8c1dd5d2.
- **Markdown repair commit:** f0effd262cfe1b29def54821dba3a83a27e48553 (fix(md): Quillen Higher algebraic K-theory I [Peer-P26 | gpt-6-luna/max]); it changes only 1978年 - Quillen/Quillen_1973_higher_K_theory_mineru/Quillen_1973_higher_K_theory__Quillen_1973_higher_K_theory.md.
- **Final repaired Markdown:** SHA-256 e6eecd221a77a7edcd545d6442cea7fec1e4ef48b1a08fdbe474020c2841f4b7.
- **Source PDF:** 1978年 - Quillen/Quillen_1973_higher_K_theory.pdf; SHA-256 5d2db42d3fec06156da4e6f6d5a85fb9a04358df59141d3abe74a57b815bae04 (unchanged).
- **Post-repair review:** the full 2,417-line Markdown was reread after repair. Each entry below identifies the page-specific print image or crop used for comparison; the page audit records retain the original 150dpi page images and the listed 300dpi crops. The repair run recorded a changed-page crop recheck and a clean git diff --check. No automated test suite was run; the PDF page images are the content oracle for this transcription repair.

### Page-by-page repairs

- **p.001** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p001_exact_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p001_notation.png. Restored the paper title; corrected both exact-sequence endpoint glyphs from letter O to numeric 0 and corrected K₀(M).
- **p.002** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p002_spectral_sequence.png. Restored uppercase X in the spectral-sequence target K′₋ₙ(X).
- **p.003** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p003_proceedings.png. Transcribed the printed spelling “procedings,” preserving the source’s print quirk.
- **p.005** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p005_zero_notation.png. Restored the body §1 heading and numeric-zero subscripts in π₀(C,X) and π₀ᶜ.
- **p.007** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p007_homology_formulas.png; audit/300dpi/Quillen_1973_higher_K_theory_p007_integral_formulas.png; audit/300dpi/Quillen_1973_higher_K_theory_p007_dual_category.png; audit/300dpi/Quillen_1973_higher_K_theory_p007_derived_limits.png. Reconstructed the indexed chain coproduct and X₀; restored derived-limit/colimit indices and arrows; corrected C° (circle) in the dual-category formula.
- **p.008** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p008_product_map.png; audit/300dpi/Quillen_1973_higher_K_theory_p008_prop3.png. Restored equation label (4) and the missing stage index in Cᵢ.
- **p.009** — Evidence: audit/Quillen_1973_higher_K_theory_p009.png. Restored Corollary 2 and its proof; replaced the spurious “Eqn 2, Gen 1” sentence with the printed “Prop. 2, Cor. 1” wording and removed the duplicate.
- **p.010** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p010_dual_notation.png. Corrected the opposite-category superscript from digit 0 to the printed small circle in (C/Y)°.
- **p.011** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p011_indices.png. Corrected Y₀, fX₀, and X₀ indices from letter o to numeric zero.
- **p.012** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p012_fibre.png; audit/300dpi/Quillen_1973_higher_K_theory_p012_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p012_cartesian_map.png. Restored product signs × in the fibre formulas and the overbar on the sequence basepoint ē.
- **p.013** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p013_theoremB_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p013_corollary_sequence.png. Restored primes on C′ in both groups of the corollary sequence.
- **p.014** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p014_lemma_objects.png; audit/300dpi/Quillen_1973_higher_K_theory_p014_proof_indices.png. Corrected Xᵢ′, numeric-zero indices, and C′°; replaced two corrupted embedded image references with manual LaTeX diagrams. The original image assets were left untouched.
- **p.015** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p015_example_target.png. Corrected the final example target from Mⁿ to M″.
- **p.017** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p017_morphisms.png; audit/300dpi/Quillen_1973_higher_K_theory_p017_zero_object.png. Restored the exclamation-mark subscript in i₍!₎.
- **p.018** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p018_fundamental_group.png. Corrected the zero object from numeral 0 to capital O and restored K₀M and related O-based expressions.
- **p.019** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p019_exact_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p019_definition.png; audit/300dpi/Quillen_1973_higher_K_theory_p019_dual_product.png. Restored M″, KᵢM and K₀M notation, corrected M° (circle), and restored i subscripts in formula (8).
- **p.023** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p023_products.png; audit/300dpi/Quillen_1973_higher_K_theory_p023_graded_ring.png. Corrected Kᵢ/K₀, A₀/F₀, and argument grouping; restored the indexed direct-sum operator.
- **p.024** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p024_finite_sum.png; audit/300dpi/Quillen_1973_higher_K_theory_p024_short_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p024_theorem3.png. Restored the indexed direct sum and numeric-zero endpoints; restored Theorem 3 condition (i) and removed the spurious underline on i.
- **p.025** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p025_indices_factorization.png. Corrected M₀, P₀, and Pᵢ₀ and restored i₍!₎ in the factorization.
- **p.026** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p026_resolution_indices.png. Restored P₍=n₎ category indices, the P∞ union formula and corollary scope, and numeric-zero subscripts.
- **p.028** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p028_devissage.png. Corrected the filtration endpoint from Mₙ=N to Mₙ=M.
- **p.029** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p029_localization_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p029_dedekind_sequence.png. Reconstructed the indexed localization sequence and its intermediate groups/maps; restored the indexed direct sum in the Dedekind sequence.
- **p.030** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p030_categories_layers.png. Corrected all three opposite-category superscripts from digit 0 to small circles.
- **p.032** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p032_choice_phi.png; audit/300dpi/Quillen_1973_higher_K_theory_p032_image_subobject.png; audit/300dpi/Quillen_1973_higher_K_theory_p032_phi_choice.png. Corrected the chosen Greek φ and Im(h−h′) image notation.
- **p.033** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p033_graded_symbols.png; audit/300dpi/Quillen_1973_higher_K_theory_p033_tensor_formula.png. Corrected T₀, N₀, and F₀, and restored ⊗ in formula (4).
- **p.034** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p034_tor_indices.png; audit/300dpi/Quillen_1973_higher_K_theory_p034_theorem6.png. Corrected the degree-zero Tor subscripts T₀.
- **p.035** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p035_tor_zero.png. Corrected the T₀ subscripts in Lemma 2 and adjacent filtration formulas.
- **p.036** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p036_tor_zero.png; audit/300dpi/Quillen_1973_higher_K_theory_p036_theorem7.png. Corrected the T₀ subscripts in Lemma 3.
- **p.037** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p037_associated_graded.png; audit/300dpi/Quillen_1973_higher_K_theory_p037_localization_sequence.png. Restored Fₙ in the filtered subring and the indexed coproduct over p≤n.
- **p.039** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p039_frobenius_split.png; audit/300dpi/Quillen_1973_higher_K_theory_p039_characteristic_sequences.png; audit/300dpi/Quillen_1973_higher_K_theory_p039_phi_tensor.png. Corrected V₀, V terms, KᵢFq, φ(V), Fq tensor bases, numeric-zero endpoints, and the product sign ×.
- **p.040** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p040_example2_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p040_section7_definitions.png; audit/300dpi/Quillen_1973_higher_K_theory_p040_maps_pairings.png. Restored the direct-sum sign and corrected §7 K-group and OX notation, indices, and map targets.
- **p.041** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p041_prop22.png; audit/300dpi/Quillen_1973_higher_K_theory_p041_prop25_tor.png; audit/300dpi/Quillen_1973_higher_K_theory_p041_prop27.png. Restored missing Kq indices, the printed Tor condition, and the K′qY→K′qX map notation.
- **p.042** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p042_assumptions_29.png; audit/300dpi/Quillen_1973_higher_K_theory_p042_projection_formula.png; audit/300dpi/Quillen_1973_higher_K_theory_p042_derived_formula.png. Corrected OX/QX and OX/0X, the higher-direct-image exponent from 1 to i, K₀X/K₀Y placement, Tor conditions, and P₀. Formula (2.8) was rechecked and left unchanged.
- **p.043** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p043_pushforward_formula.png; audit/300dpi/Quillen_1973_higher_K_theory_p043_base_change.png; audit/300dpi/Quillen_1973_higher_K_theory_p043_closed_subschemes.png. Corrected E to F in the pushforward formula, the Tor base to OY,y, the K′qX→K′qY′ notation, OX, and missing Kq indices.
- **p.044** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p044_mayer_spectral.png; audit/300dpi/Quillen_1973_higher_K_theory_p044_homotopy_limit.png. Restored the Mayer–Vietoris direct sum and K′q indices in Gersten’s sequence and Proposition 4.1, including the generic-point colimit terms and product ×X.
- **p.045** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p045_projective_formulas.png; audit/300dpi/Quillen_1973_higher_K_theory_p045_koszul_sum.png. Restored Kq and K₀ indices, the numeric-zero endpoint and bound, the direct-sum sign, and the O(−1) tensor power indexed by i in the final isomorphism.
- **p.046** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p046_radicial_map.png; audit/300dpi/Quillen_1973_higher_K_theory_p046_tensor_filtration.png; audit/300dpi/Quillen_1973_higher_K_theory_p046_support_filtration.png. Corrected “radicial,” pullback stars, tensor punctuation, the indexed direct sum, the double-underlined Mp(X) category, and K′qZ.
- **p.047** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p047_support_spectral.png; audit/300dpi/Quillen_1973_higher_K_theory_p047_proof_sequence.png. Reconstructed the double-underlined Mp(X)/Mp+1(X) categories and indexed direct sums in the spectral sequence and proof.
- **p.048** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p048_gersten_criterion.png; audit/300dpi/Quillen_1973_higher_K_theory_p048_sheaf_resolution.png. Restored the minus sign and zero index in the edge map, direct sums and X₀, K′nU and sheaf indices, and OX,x.
- **p.049** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p049_base_extension.png; audit/300dpi/Quillen_1973_higher_K_theory_p049_reduction_lemma.png. Corrected the base-extension tensor subscript to k′ and category subscripts in Mp+1(R)→Mp(A) and its displayed limit. The printed target object A was already correct and remains A.
- **p.050** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p050_exact_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p050_filtration_proof.png. Restored B′ in tensor subscripts, the indexed direct sum, and p category subscripts in Mp(B′) and Mp(R′f).
- **p.051** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p051_chow_groups.png; audit/300dpi/Quillen_1973_higher_K_theory_p051_multiplicity.png. Corrected 0≠t, direct sums in d₁, W₀, ordyx, and the local-ring term OY,x.
- **p.052** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p052_chow_differential.png; audit/300dpi/Quillen_1973_higher_K_theory_p052_local_ring_boundary.png. Corrected the first spectral-sequence indices from capital O to numeric zero in E₁⁰,⁻¹(Y) and E₁⁰,⁻¹(OY,x).
- **p.053** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p053_boundary_calculation.png; audit/300dpi/Quillen_1973_higher_K_theory_p053_chow_formula.png; audit/300dpi/Quillen_1973_higher_K_theory_p053_boundary_diagram.png. Corrected OX* in H¹(X,OX*)=Pic(X), replacing the OCR form ℚX*. No 0≠t repair belongs to this page.
- **p.054** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p054_lemma11.png. Corrected the dual-bundle symbol from ▼ to ∨.
- **p.055** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p055_z_sequence.png; audit/300dpi/Quillen_1973_higher_K_theory_p055_resolution_tail.png. Corrected Zp and Zp−1 capitalization, the final numeric-zero endpoint, and the printed direct-sum operator.
- **p.056** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p056_resolution_functor.png; audit/300dpi/Quillen_1973_higher_K_theory_p056_derived_sequences.png. Restored Rqf*(OX(n)), T₀, and the ⊗S term in the sequence derived from (1.9).
- **p.057** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p057_lemma12.png; audit/300dpi/Quillen_1973_higher_K_theory_p057_lemma13.png. Corrected n₀ and both occurrences of its threshold, restored ⊗S, corrected QX to OX, and restored q>0.
- **p.058** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p058_theorem_statement.png; audit/300dpi/Quillen_1973_higher_K_theory_p058_lemma22_proof.png. Restored Rn, Pn, P₀ and corresponding K-group subscripts; corrected the functor’s tensor product from ∧ to ⊗.
- **p.059** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p059_line_bundle_theorem.png; audit/300dpi/Quillen_1973_higher_K_theory_p059_triple_sequence.png. Restored R₀/P₀, h₀, and X₀ indices in the K-group map and noncommutative exact-sequence terms.
- **p.060** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p060_descent_square.png; audit/300dpi/Quillen_1973_higher_K_theory_p060_azumaya_algebra.png. Reconstructed g′*J=OX′(−1)⊗S′E and the EndX′ and ⊗S′ terms without inserted OCR commas.
- **p.061** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p061_azumaya_functor.png; audit/300dpi/Quillen_1973_higher_K_theory_p061_resolution.png. Corrected HomAn, T₀(F), and the final OX term.
- **p.063** — Evidence: audit/300dpi/Quillen_1973_higher_K_theory_p063_final_references.png. Restored the Lecture Notes in Math. series on SGA 6 and the ditto marker identifying Segal 2.

### Reconciliation and unresolved print glyphs

- **p.027:** The earlier FAIL was withdrawn after the cited print crops and Markdown were rechecked. There was no Markdown edit; the page is now PASS.
- **p.042:** Formula (2.8), K′qX→K′qY, matches print and was not edited. The separate p.042 discrepancies listed above remain the basis for the page’s FAIL grade.
- **p.049:** Print has M₍p+1₎(R)→Mₚ(A); A was the correct printed target. Only the malformed category subscripts were repaired.
- **p.053:** The 0≠t occurrence is on p.051 in Theorem 5.13 and was repaired there. It is not a p.053 discrepancy; the remaining H¹(X,OX*) discrepancy is the p.053 failure.
- **Unresolved:** p.005’s printed 0-cell/O-cell glyph and p.021’s two short-sequence endpoint glyphs remain ambiguous at the available 300dpi crops. The Markdown was not changed for those glyphs.
- **Boundary:** The source PDF and audit image assets are unchanged. This is a branch-local candidate; the canonical main worktree’s root README/MEMORY/AUDIT indexes and progress log remain owned by Master-Luna and were not edited here.
