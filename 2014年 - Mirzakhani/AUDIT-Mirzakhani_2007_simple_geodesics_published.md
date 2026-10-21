# AUDIT — Mirzakhani_2007_simple_geodesics_published

- Actor: `Peer-P11`
- Model / effort: `gpt-6-luna / max`
- Candidate base: `037602429d3b009f6fc468c732073eb3ddf9875f`
- Source PDF: `Mirzakhani_2007_simple_geodesics_published.pdf` (44 pages)
- Source mode: born-digital; `Creator: dvipsk 5.58f`, `Producer: Acrobat Distiller 6.0.1`; `pdftotext -layout` produced 107,928 bytes with 0 U+FFFD characters.
- Initial MinerU Markdown SHA-256: `d91a12c0948a783abc2afb1700b5a9ab2bbfcfe7f81a4e9d1debeae7be860909` (1,694 lines; pre-audit complete read).
- Audit method: PDF text layer compared page by page with the MinerU Markdown. The title page and dense mathematical notation are checked against stored source-page PNGs; text extraction losses or ambiguous glyphs are adjudicated from PDF images/crops. The page review was completed before correction; repaired differences and final checks are registered below.
- Status: complete; the 44-page audit, all recorded FAIL repairs, and final Markdown reread are complete.

## Overall result and post-repair review

- Coverage and initial grades: all 44 PDF pages were audited in order; the original page grades were 29 FAIL, 15 PASS±, and 0 plain PASS. Page entries retain those initial judgments as evidence. All 29 FAIL pages were repaired.
- Source chain: the original MinerU Markdown is present from commit d351abbff700768968605937fac5c051de31bb0a; pre-repair SHA-256 d91a12c0948a783abc2afb1700b5a9ab2bbfcfe7f81a4e9d1debeae7be860909; independent repair commit 137f56547eb16cb3bfb35e8d1afe51591554a41f.
- Candidate integration state: contributor work is based on 037602429d3b009f6fc468c732073eb3ddf9875f. This candidate has not been integrated or pushed; root-level AUDIT-INDEX.md and AUDIT-PROGRESS.log were not changed.
- Final Markdown reread: after the repair commit, the complete final file was read from beginning to end (1,698 lines; 107,121 bytes). Final SHA-256: 65320689fcaaa8fcbdc4133f224bfba5e9d298c8f8056362e9770a2b5aa43527. Every repair below was rechecked against its cited PDF page image or crop during this reread; no additional content mismatch was found in the reviewed scope.
- PDF mode and evidence: born-digital; pdftotext -layout yielded 107,928 bytes and no U+FFFD. The per-page 150 dpi PNGs and cited 300 dpi crops are preserved under audit/.
- MinerU identity: the inspected existing structured_content.json and middle_json.json export metadata do not contain a doc_id or document_id; structured_content.json identifies MinerU 3.4.4, tier basic, parse mode txt.
- Line references in the page-difference entries identify the pre-repair 1,694-line Markdown. The final file adds the title-page journal citation and DOI.
- Print/OCR quirks remain as recorded in the page entries, including the printed wording “ordered paris” and repeated n₂ constraint on p.26, the p.43 reference-spacing artifact, and documented QED control-code artifacts. PASS± pages retain non-content artifacts such as omitted running heads.

### Registry scope

Each row records the manual correction, its PDF evidence, and the final-file check. “Full reread confirmed” means the corrected final Markdown was read after the repair commit and the changed expression matched the cited print evidence.

## p.001 (PDF p.1 / print p.179)

- Event time: `2026-10-01 16:09 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p001.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p001_Rdomain.png` (300 dpi source crop).
- Checked: running journal header, title, author, affiliation/e-mail, receipt dates, online publication date, contents, and the first two introductory paragraphs through the page break at “We”. The visible bibliographic running header gives *Invent. math.* 167, 179–222 (2007), DOI `10.1007/s00222-006-0013-2`; title-page identity and contents otherwise agree.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 24 adds an overbar to the volume notation, `\bar{V}_{g,n}`; PDF p.1 prints `V_{g,n}` without an overbar (300 dpi crop).
  - MinerU Markdown line 26 gives `\mathbb{R}_{>0}^n`; PDF p.1 prints `\mathbb{R}_{\ge 0}^n` (text layer and 300 dpi crop).
  - The Markdown omits the journal/volume/page/DOI running header. This is recorded as a bibliographic omission; the page grade remains FAIL because of the two mathematical-text differences above.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.



## p.002 (PDF p.2 / print p.180)

- Event time: `2026-10-01 16:12 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p002.png` (pngmono, 150 dpi).
- Checked: continuation of the introduction, Theorem 1.1 and its coefficient/exponent statements, the `V_{1,1}` example, Remark, and every row of Table 1. The printed running head is `180 / M. Mirzakhani`; it is omitted from the Markdown.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 47 reads `L ^ {2} / 2 4 + \pi^ {2} / 6`; PDF p.2 prints `L^2/24 + \pi^2/6`. Table 1 on the same page also prints `V_{1,1}(L)=\frac{1}{24}(L^2+4\pi^2)`, confirming the intended denominator; retain the mismatch for post-audit repair.
- Other checked theorem statements and Table 1 entries agree with the PDF text layer and the inspected page image. The missing running head is a non-content folio omission.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.003 (PDF p.3 / print p.181)

- Event time: `2026-10-01 16:14 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p003.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p003_Tbar.png` (300 dpi source crop).
- Checked: McShane identity (1.1), the pair-space/projection and length-function definitions, identity (1.2), the function `f`, and the Fenchel–Nielsen description through the quotient formula. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 181) are omitted in Markdown.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 107 adds an overbar to the Teichmüller-space symbol, `\bar{\mathcal T}_{1,1}`; PDF p.3 prints `\mathcal T_{1,1}` without an overbar (300 dpi crop).
- Text extraction emits a non-letter control glyph for several printed length symbols `\ell`; the p.3 page image confirms these as `\ell`, matching the Markdown in equations (1.1) and (1.2).
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.004 (PDF p.4 / print p.182)

- Event time: `2026-10-01 16:17 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p004.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p004_DR_signature.png` (300 dpi source crop).
- Checked: the Fenchel–Nielsen integration and `Vol(M_{1,1})` calculation, the two-step plan, and Theorem 1.3 with its sums and accompanying explanation through the cusp convention. The printed running head `182 / M. Mirzakhani` is omitted from the Markdown.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 133 gives the type signature for `\mathcal D, \mathcal R` as `\mathbb{R}_{+}^{3} \mathbb{R}_{+}`, omitting the map arrow. PDF p.4 prints `\mathcal D, \mathcal R : \mathbb{R}_{+}^{3} \to \mathbb{R}_{+}`; the 300 dpi crop confirms `\to`.
- The PDF text layer maps several printed length symbols to a non-letter control glyph; the page PNG confirms them as `\ell`, and the formulas in Markdown agree.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.005 (PDF p.5 / print p.183)

- Event time: `2026-10-01 16:19 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p005.png` (pngmono, 150 dpi; visually inspected).
- Checked: special case (1.4), the asymptotic formula for `\mathcal D`, the transition to integration over the moduli space, the length/orbit definitions, `f_\gamma`, the covering-space definition, and the length function. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 183) are omitted in Markdown.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 185 has broken delimiters in the definition of `\pi^\gamma` and omits the map arrow from `\mathcal M_{g,n}^{\gamma}` to `\mathcal M_{g,n}`. PDF p.5 prints the full covering-map definition with `\to`; the page image and text layer confirm the arrow.
- The text layer maps the printed length symbol `\ell` to a non-letter control glyph; the page image confirms `\ell`, matching the surrounding Markdown notation.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.006 (PDF p.6 / print p.184)

- Event time: `2026-10-01 16:23 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p006.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p006_Mdef.png` and `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p006_Mnotation.png` (300 dpi source crops).
- Checked: the push-forward integral, level-set integral, cutting and circle-bundle definitions, the `S^1` action, and quotient/volume statements. The running head `184 / M. Mirzakhani` is omitted from the Markdown.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 207 inserts bold `ξ` after `M` in the moduli-space notation; PDF p.6 prints only the calligraphic `ℳ` (300 dpi crop).
  - MinerU Markdown line 213 adds an overbar to the moduli-space symbol in `M(S_{g,n}(γ), ℓ_γ=t)`; PDF p.6 prints it unbarred (300 dpi crop).
- The text layer maps printed `ℓ` symbols to a non-letter control glyph; the page PNG and crops resolve them as `ℓ`. The other checked formulas and prose agree.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.007 (PDF p.7 / print p.185)

- Event time: `2026-10-01 16:25 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p007.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p007_breveL.png` (300 dpi source crop).
- Checked: the end of the covering-space argument and equation (1.5), the definition of `M(γ)`, the alternative proof paragraph, Applications, Notes and references, and the Acknowledgements text at the foot of the page. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 185) are omitted in Markdown.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 233 adds a breve accent to the argument `L` of `V_{g,n}`; PDF p.7 prints `L` with no breve (300 dpi crop).
- The other checked prose and equation (1.5) agree with the PDF text layer and inspected page image.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.008 (PDF p.8 / print p.186)

- Event time: `2026-10-01 16:27 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p008.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p008_Modnotation.png` (300 dpi source crop).
- Checked: the second Acknowledgements paragraph, Section 2 opening, Teichmüller-space and marking definitions, mapping-class-group action, moduli-space quotient, and cusp convention. The running head `186 / M. Mirzakhani` is omitted from the Markdown.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 249 writes the first marking map as `f:S X`, omitting the arrow; PDF p.8 prints `f:S → X` (text layer and page image).
  - MinerU Markdown line 261 has a superscript minus in `Mod_{g,n}^{-}=Mod(S_{g,n})`; PDF p.8 prints `Mod_{g,n}=Mod(S_{g,n})` without that superscript (300 dpi crop).
- The remaining checked definitions and quotient formula agree.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.009 (PDF p.9 / print p.187)

- Event time: `2026-10-01 16:28 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p009.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p009_notation.png` (300 dpi source crop).
- Checked: the disconnected-surface product, Weil-Petersson 2-form definition and induced volume form, Fenchel–Nielsen coordinates, and Theorem 2.1. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 187) are omitted from the Markdown.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 289 adds a dot over the membership symbol and a dot above `Ω`; PDF p.9 gives the 2-form statement as `ω ∈ Ω²(M)` with neither dot (300 dpi crop).
  - MinerU Markdown line 301 uses barred `k̄` and `n̄` in the pants-decomposition count; PDF p.9 prints `k = 3g − 3 + n` (300 dpi crop).
- The remaining checked product, coordinates, and symplectic-form equation agree with the printed page.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.010 (PDF p.10 / print p.188)

- Event time: `2026-10-01 16:30 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p010.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p010_multicurve.png` (300 dpi source crop). MinerU figure `images/page_9_image_8.jpg` was read-only and compared with Fig. 1.
- Checked: Hamiltonian circle-action definition, twisting/deformation and Dehn-twist relation, the symplectic-dual statement, Fig. 1, and the multicurve definition/start of the cut-surface description. The running head `188 / M. Mirzakhani` is omitted from the Markdown.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 345 renders the initial plain `γ` of the multicurve sentence as `γ_{:}`; PDF p.10 prints plain `γ,` with no colon subscript (300 dpi crop).
  - Minor punctuation: Markdown line 327 repeats the semicolon after `M` and inserts a comma after `id`; PDF p.10 has one semicolon and ends `ψ₁ = id.` The punctuation does not alter the statement.
- The PDF text layer maps length symbols to a non-letter control glyph; the inspected page image confirms them as `ℓ`, matching the Markdown. The checked mathematical statements otherwise agree.

- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.011 (PDF p.11 / print p.189)

- Event time: `2026-10-01 16:33 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p011.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p011_gamma.png` (300 dpi source crop).
- Checked: continuation of the multicurve/cut-surface paragraph, the boundary-set formula, definitions of Γ, L, and x, moduli-space and volume decompositions including (2.1), and the symmetry-group definitions/example. The running head `189 / Simple geodesics and Weil-Petersson volumes` is omitted from the Markdown.
- Result: **PASS±**.
- The Markdown paragraph begins earlier on PDF p.10; its PDF p.11 continuation beginning “Each connected component” agrees with the source. The 300 dpi crop confirms the multicurve notation in the symmetry-group discussion. No content-level difference was found on this page.
- Repair: none.


## p.012 (PDF p.12 / print p.190)

- Event time: `2026-10-01 16:34 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p012.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p012_symmetry.png` (300 dpi source crop).
- Checked: the symmetry-group conditions, the orbit of simple closed curves and its counting function, the example with the characteristic function, and the opening of Section 3 through the pair-of-pants construction. The running head `190 / M. Mirzakhani` is omitted from the Markdown.
- Result: **PASS±**.
- Minor evidence note: `pdftotext` drops the negation stroke in `|Sym(γ)| ≠ 1` on this page; the 300 dpi crop confirms the printed `≠`, matching the Markdown. Other length-symbol glyphs are confirmed from the page image. No Markdown content difference was found.
- Repair: none.

## p.013 (PDF p.13 / print p.191)

- Event time: `2026-10-01 16:36 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p013.png` (pngmono, 150 dpi; visually inspected). MinerU figure `images/page_12_image_0.jpg` was read-only and compared with printed Fig. 2.
- Checked: the Fig. 2 geodesic labels, pair-of-pants geodesic descriptions, definitions of R and D, the projection-length explanation, and the H function/type definition. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 191) are omitted from the Markdown.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 453 omits the map arrow in the type signature for H (`H : ℝ² ℝ`); PDF p.13 prints `H : ℝ² → ℝ`, confirmed on the page image.
- Minor OCR text artifact: Markdown line 451 reads `S 0 the function`; the print reads “So the function”. This does not change the mathematical content. Text-layer length-symbol glyphs are confirmed as `ℓ` from the page image.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.014 (PDF p.14 / print p.192)

- Event time: `2026-10-01 16:38 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p014.png` (pngmono, 150 dpi; visually inspected). MinerU figure `images/page_13_image_0.jpg` was read-only and compared with printed Fig. 3.
- Checked: Fig. 3 labels, the symmetry identities for D and R, Lemma 3.1 formulas (3.1) and (3.2), and the hyperbolic quadrilateral proof through the formula for R.
- Result: **PASS±**.
- Minor OCR spacing artifact: MinerU Markdown line 475 joins “The” and “functions” as `Thefunctions`; the source has a space. This does not affect the formulas, which match the printed page image.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 192) are omitted from the Markdown.
- Repair: none.

## p.015 (PDF p.15 / print p.193)

- Event time: `2026-10-01 16:40 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p015.png` (pngmono, 150 dpi); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p015_RandL32.png` (300 dpi source crop).
- Checked: the hexagon distance formula, simplification of `R(x₁,x₂,x₃)`, equations (3.3) and (3.4), and the derivative proof.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 516 omits the closing parenthesis after `d(β₁,β₃)` in the numerator before `+1`; it therefore places `+1` inside `cosh`. PDF p.15 prints `cosh(d(β₁,β₃)) + 1` (300 dpi crop).
 - MinerU Markdown line 525 omits the arrow in the function type signature; PDF p.15 prints `R₊ → R₊` (300 dpi crop).
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 193) are omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.016 (PDF p.16 / print p.194)

- Event time: `2026-10-01 16:42 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p016.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p016_F_and_Thm41.png` (300 dpi source crop).
- Checked: asymptotic formulas (3.5) and (3.6) and their limits, Section 4 opening, embedded-pants definitions, the sets Fᵢ/Fᵢ,ⱼ, and Theorem 4.1.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 569 omits the arrow in “as z → ∞”; PDF p.16 prints `z → ∞`.
  - MinerU Markdown line 583 adds an overbar to the initial 1 in the range `1 ≤ i ≠ j ≤ n`; PDF p.16 prints an unbarred 1 (300 dpi crop).
  - MinerU Markdown line 590 writes the length terms as `ℓ γ₁`, `ℓ γ₂`, and `ℓ γ`; PDF p.16 has `ℓ_{γ₁}`, `ℓ_{γ₂}`, and `ℓ_γ` in the exponent (300 dpi crop).
- The text layer renders the `≠` in the Fᵢ,ⱼ range as `=`; the 300 dpi crop confirms the printed `≠`, which agrees with the Markdown. The running head is omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.017 (PDF p.17 / print p.195)

- Event time: `2026-10-01 16:45 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p017.png` (pngmono, 150 dpi; visually inspected).
- Checked: the function-signature paragraph, Theorem 4.2 and identity (4.1), Corollary 4.3 and identity (4.2), the following remark, and the definition and proof of Lemma 4.4.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 593 omits the arrow in the D/R function signature; PDF p.17 prints `R₊³ → R₊`.
  - MinerU Markdown line 606 writes the exponent lengths as `ℓ γ₁`, `ℓ γ₂`, and `ℓ γ` without subscripts; PDF p.17 prints `ℓ_{γ₁}`, `ℓ_{γ₂}`, and `ℓ_γ` in (4.2), confirmed on the page image.
- Markdown line 623 ends with two control-code characters after the proof; the PDF page image shows a QED square. This is recorded as a minor end-marker OCR artifact.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 195) are omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.018 (PDF p.18 / print p.196)

- Event time: `2026-10-01 16:46 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p018.png` (pngmono, 150 dpi; visually inspected). MinerU figure fragments `images/page_17_image_12.jpg` and `images/page_17_image_13.jpg` were read-only and compared with printed Fig. 4.
- Checked: Theorems 4.5 and 4.6, the two classes of endpoint behavior, the embedded-pants correspondence, and Fig. 4.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown lines 641 and 643 insert `H` before `Ω(γₓ)` in cases (b) and (c) of Theorem 4.6. PDF p.18 prints `Ω(γₓ)` without a leading H; the source page image confirms it.
- The checked theorem statements otherwise agree. The running head `196 / M. Mirzakhani` is omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.019 (PDF p.19 / print p.197)

- Event time: `2026-10-01 16:47 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p019.png` (pngmono, 150 dpi; visually inspected). MinerU figure `images/page_18_chart_8.jpg` was read-only and compared with printed Fig. 5.
- Checked: the end of the simple-arc correspondence, proof of Theorem 4.6(a) through the universal-cover construction, and Fig. 5.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 669 adds a hat over `Σ` in “must leave Σ”; PDF p.19 prints plain `Σ` (page image).
- The text layer drops the negation stroke in `z ∉ {…}`; the page image confirms `∉`, matching the Markdown. Fig. 5 in the MinerU asset matches the source diagram.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 197) are omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.020 (PDF p.20 / print p.198)

- Event time: `2026-10-01 16:48 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p020.png` (pngmono, 150 dpi; visually inspected). MinerU figure `images/page_19_image_7.jpg` was read-only and compared with printed Fig. 6.
- Checked: the end of the proof of Theorem 4.6(a), the transition to part (b) and part (c), the quasi-geodesic definition, the limiting straightening statement, and Fig. 6.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 685 adds a colon subscript to `θ` (`θ_{:}`); PDF p.20 prints plain `θ`.
  - MinerU Markdown line 687 omits the arrow in the limiting statement `(L, θ) → (∞, 0)`.
- Markdown line 671 ends this proof paragraph with control-code characters; the PDF page image shows a QED square. This is recorded as a minor end-marker OCR artifact.
- The running head `198 / M. Mirzakhani` is omitted from the Markdown. Fig. 6 matches the MinerU embedded figure.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.021 (PDF p.21 / print p.199)

- Event time: `2026-10-01 16:50 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p021.png` (pngmono, 150 dpi; visually inspected). MinerU figure `images/page_20_image_0.jpg` was read-only and compared with printed Fig. 7.
- Checked: Fig. 7, the epsilon-good geodesic-arc conditions, both endpoint conditions, the arc-intersection equation, and the orientation definition.
- Result: **PASS±**.
- Minor OCR artifact: MinerU Markdown line 705 has a nonprinting control character in the text label before “-good”; PDF p.21 prints “ε-good”. The same definition states `ℓ(c) ≤ ε`, so the condition itself remains clear. Fig. 7 matches the embedded MinerU image.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 199) are omitted from the Markdown.
- Repair: none.

## p.022 (PDF p.22 / print p.200)

- Event time: `2026-10-01 16:52 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p022.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p022_Let_eta.png` (300 dpi source crop).
- Checked: complete-simple-geodesic setup, Lemma 4.7 assumptions and conclusion, the proof of Theorem 4.6(c), and the opening of its transverse-arc construction.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 749 mangles “Let η̂ denote…” as a barred capital L followed by separated `e t`; PDF p.22 prints the intact words “Let η̂ denote…” (300 dpi crop).
- MinerU Markdown line 769 omits the map arrow in the transverse-arc type `c:[−r,+r] → X`; PDF p.22 prints the arrow.
- Minor OCR artifact: lines 729 and 759 contain a nonprinting control character before “-good”; PDF p.22 prints `ε-good`. The adjacent bound `ℓ(c) ≤ ε` and following inequalities preserve the meaning.
- The running head `200 / M. Mirzakhani` is omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.023 (PDF p.23 / print p.201)

- Event time: `2026-10-01 16:54 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p023.png` (pngmono, 150 dpi; visually inspected). MinerU figure `images/page_22_image_0.jpg` was read-only and compared with printed Fig. 8.
- Checked: the continuation of the transverse-arc claim and construction of t₁/t₂, Fig. 8, the positive ε-good segment conclusion, the second step invoking Lemma 4.7, and the remaining conclusion/proof of Theorem 4.5.
- Result: **PASS±**.
- Minor OCR artifacts: the Markdown has nonprinting control characters in ε-good labels and after the proof paragraphs; the PDF page image shows `ε` and QED squares. The mathematical statements otherwise match.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 201) are omitted from the Markdown.
- Repair: none.

## p.024 (PDF p.24 / print p.202)

- Event time: `2026-10-01 16:55 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p024.png` (pngmono, 150 dpi; visually inspected).
- Checked: the connection between isolated intervals and embedded pairs of pants, the definition of Σₕ, the proof’s cases, and equations (4.3) and (4.4).
- Result: **PASS±**.
- Minor evidence note: the text layer renders the range condition as `j = i`; the PDF page image shows `j ≠ i`, matching MinerU Markdown. It also maps printed length glyphs poorly; the page image confirms the Markdown’s indexed length notation. The running head `202 / M. Mirzakhani` is omitted.
- No Markdown content difference was found on this page.
- Repair: none.

## p.025 (PDF p.25 / print p.203)

- Event time: `2026-10-01 16:57 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p025.png` (pngmono, 150 dpi; visually inspected).
- Checked: case 2 and equation (4.5), the rewrite of (4.3), Section 5 setup and base cases, and the recursive identity (5.1). The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 203) are omitted from the Markdown.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 888 writes the example as `L₁² / 2 4 + π²/6`; PDF p.25 prints `L₁²/24 + π²/6` (page image). The table on p.2 confirms the same denominator.
- Minor punctuation difference: line 893 separates the excluded pairs `(1,1)` and `(0,3)` without the comma printed on p.25.
- The other checked formulas, including equation (5.1), match the printed page.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.026 (PDF p.26 / print p.204)

- Event time: `2026-10-01 16:58 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p026.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p026_Iset.png` (300 dpi source crop).
- Checked: definitions (5.2)–(5.4), the function type declarations through the connected-case function, m(g,n), the connected-case integrand, and the ordered-pair setup and constraints.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 939 omits the arrow in the type signature for the connected-case function; PDF p.26 prints `R₊^{n+2} → R₊`.
  - MinerU Markdown line 945 calls the ordered-pair index set `τ_{g,n}`; PDF p.26 prints a script capital-I set name (300 dpi crop).
- Correction to the earlier page-local attribution: Markdown line 991 is on PDF p.27, after the page break, and will be audited there.
- Print-level notes retained as printed and transcribed: the prose says “ordered paris”; the first genus/partition constraint repeats `n₂` in `2 ≤ 2g₁+n₂` and `2 ≤ 2g₂+n₂`. No OCR correction is made to either source-level reading.
- The running head `204 / M. Mirzakhani` is omitted from the Markdown. Other checked formulas match.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.027 (PDF p.27 / print p.205)

- Event time: `2026-10-01 17:09 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p027.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p027_Iuse.png` (300 dpi source crop).
- Checked: notation for L_I, the ordered-pair set and V(a,x,y,L), the disconnected-case function, the B function and equation (5.5), the following remark, and the topology paragraph through the page break.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 991 omits the arrow in the type signature for the disconnected-case function; PDF p.27 prints `R₊^{n+2} → R₊` (page image).
  - MinerU Markdown line 1000 contains both a tag `(5)` and `(5.5)`; PDF p.27 displays only `(5.5)`.
  - The printed index-set glyph is the same in line 980's membership and line 994's sum, while the Markdown uses Fraktur I at line 980 and calligraphic I at line 994. The 300 dpi crop and page image show one repeated printed glyph.
- The earlier PDF p.26 definition of this set is also misread as τ in Markdown line 945; see the p.26 entry.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 205) are omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.028 (PDF p.28 / print p.206)

- Event time: `2026-10-01 17:10 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p028.png` (pngmono, 150 dpi; visually inspected).
- Checked: the end of the topology discussion, Theorem 6.1, the genus-one volume identity and derivative, and the integral setup for `V₁,₁`.
- Result: **PASS±**.
- Minor OCR spacing artifact: MinerU Markdown line 1011 joins “The function” and “a polynomial” as `Thefunction` and `apolynomial`; PDF p.28 separates these words. The mathematical statement matches.
- The page image confirms the printed length symbols where the text layer uses a non-letter glyph. The running head `206 / M. Mirzakhani` is omitted from the Markdown.
- Repair: none.

## p.029 (PDF p.29 / print p.207)

- Event time: `2026-10-01 17:13 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p029.png` (pngmono, 150 dpi; visually inspected).
- Checked: the changes of variables and integral evaluation, the reciprocal-exponential identity, equation (6.1), the remark, the derivative identity (5.1), and the definition of F.
- Result: **FAIL**.
- Difference:
  - MinerU Markdown line 1058 writes the initial volume term with `L² / 2 4`; PDF p.29 prints `L²/24 + π²/6` (page image). This is the same denominator transcription issue also recorded on p.2 and p.25.
- The other checked formulas and prose match. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 207) are omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.030 (PDF p.30 / print p.208)

- Event time: `2026-10-01 17:14 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p030.png` (pngmono, 150 dpi; visually inspected).
- Checked: the double-integral identity (6.2), beta-integral evaluation, change of variables, Lemma 6.2 polynomial and coefficient statement, and its leading-coefficient remark.
- Result: **PASS±**.
- The displayed formulas and prose agree with the PDF page image. The running head `208 / M. Mirzakhani` is omitted from the Markdown.
- Repair: none.

## p.031 (PDF p.31 / print p.209)

- Event time: `2026-10-01 17:16 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p031.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p031_Lsquared.png` (300 dpi source crop).
- Checked: the proof of Lemma 6.2 through its zeta-integral evaluation and F-polynomial formula, plus the induction setup for Theorem 6.1.
- Result: **FAIL**.
- Difference: MinerU Markdown line 1127 adds a dot above the exponent 2 in the powers of L; PDF p.31 has ordinary `L₂²,…,Lₙ²` (300 dpi crop).
- Page-boundary correction: Markdown line 1133 belongs to PDF p.32 and is audited there.
- Minor end-marker omission: PDF p.31 has a QED square after the displayed proof of Lemma 6.2; the Markdown omits this marker.
- The other checked formulas match. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 209) are omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.032 (PDF p.32 / print p.210)

- Event time: `2026-10-01 17:20 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p032.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p032_Lpowers.png` and `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p032_Theorems.png` (300 dpi source crops).
- Checked: the coefficient-in-powers claim and C_g definition, weighted tuple notation, Theorems 6.3 and 6.4, and the proof of Theorem 6.3 through the coefficient calculation.
- Result: **FAIL**.
- Differences:
  - MinerU Markdown line 1133 adds a dot over the exponent in `L₁²`; PDF p.32 prints the ordinary power `L₁²` (300 dpi crop).
  - MinerU Markdown line 1143 encodes the possessive `αᵢ’s` as a superscript star on αᵢ followed by `s`; PDF p.32 prints `αᵢ’s` with no star (300 dpi crop).
  - MinerU Markdown line 1161 adds a dot over `L₁` in the coefficient monomial; PDF p.32 prints `L₁^{2α₁}` without a dot (300 dpi crop).
- Minor end-marker artifact: Markdown line 1133 has control-code characters where the PDF displays a QED square.
- The other checked formulas match. The running head `210 / M. Mirzakhani` is omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.033 (PDF p.33 / print p.211)

- Event time: `2026-10-01 17:47 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p033.png` (pngmono, 150 dpi; visually inspected).
- Checked: the end of the coefficient comparison in the proof of Theorem 6.3, Theorem 6.4 consequences, Corollary 6.5, the intersection-number remark, and the opening of Section 7 through equation (7.1).
- Result: **PASS±**.
- The text layer maps several length symbols in equation (7.1) to a non-letter glyph; the page image confirms `ℓ`, matching the Markdown. No content-level difference was found.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 211) are omitted from the Markdown.
- Repair: none.

## p.034 (PDF p.34 / print p.212)

- Event time: `2026-10-01 18:07 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p034.png` (pngmono, 150 dpi; visually inspected).
- Checked: Theorem 7.1’s integral formula and notation, the component-volume identity, the symmetry remark, and the covering-map integration formulas (7.3)–(7.4).
- Result: **FAIL**.
- Difference: MinerU Markdown line 1233 defines M(γ) using γ without a component subscript; PDF p.34 specifies each γᵢ in the set `{i | γᵢ separates off a one-handle from S_{g,n}}`, confirmed on the page image.
- The text layer maps several length symbols to a non-letter glyph; the page image confirms the indexed ℓ notation in the corresponding Markdown formula. The running head `212 / M. Mirzakhani` is omitted.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.035 (PDF p.35 / print p.213)

- Event time: `2026-10-01 20:01 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p035.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p035_cover.png` and `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p035_Lnotation.png` (300 dpi source crops).
- Checked: the covering-space heading and ordered-pair definition, the stabilizer subgroup and projection, the induced symplectic form, the Hamiltonian twist action, and the length-vector definition.
- Result: **FAIL**.
- Differences:
  - The printed heading uses the possessive ending `M_{g,n}(L)'s`; MinerU Markdown line 1277 renders a bullet superscript and omits the trailing `s`. The high-resolution crop and text layer show the apostrophe-s.
  - MinerU Markdown line 1289 encodes `ηᵢ’s are closed geodesics` as an eta symbol with a superscript star followed by `s`; PDF p.35 prints the possessive `ηᵢ’s` (300 dpi crop).
  - MinerU Markdown line 1311 accents L in `M_{g,n}(L)^Γ`; PDF p.35 prints unaccented L (300 dpi crop).
- The running head `213 / Simple geodesics and Weil-Petersson volumes` is omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.036 (PDF p.36 / print p.214)

- Event time: `2026-10-01 20:20 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p036.png` (pngmono, 150 dpi; visually inspected).
- Checked: the descended length function and diagram, level-set and twist-flow definitions, closed-orbit statement, torus action, symplectic quotient, and the half-twist fundamental-region qualification.
- Result: **PASS±**.
- The text layer maps length symbols to a non-letter glyph; the inspected page image confirms the Markdown’s ℓ notation. The running head `214 / M. Mirzakhani` is omitted. No content-level difference was found.
- Repair: none.

## p.037 (PDF p.37 / print p.215)

- Event time: `2026-10-01 20:33 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p037.png` (pngmono, 150 dpi; visually inspected).
- Checked: the volume factor (7.5), the cutting map and equivariance, Lemma 7.2 symplectomorphism, the symplectic-quotient remark, and Lemma 7.3's integral formula.
- Result: **PASS±**.
- The text layer maps several length symbols to a non-letter glyph; the page image confirms the indexed ℓ notation in the Markdown. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 215) are omitted. No content-level difference was found.
- Repair: none.

## p.038 (PDF p.38 / print p.216)

- Event time: `2026-10-01 20:44 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p038.png` (pngmono, 150 dpi; visually inspected).
- Checked: the proof of Lemma 7.3, level-set volume factor, derivation of Theorem 7.1, and its resulting integral expression.
- Result: **PASS±**.
- Minor end-marker omission: PDF p.38 has a QED square after the expression for I(x); the Markdown omits the marker. The formulas agree with the inspected page image.
- The text layer maps length symbols to a non-letter glyph; the page image confirms the Markdown’s ℓ notation. The running head `216 / M. Mirzakhani` is omitted.
- Repair: none.

## p.039 (PDF p.39 / print p.217)

- Event time: `2026-10-01 20:58 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p039.png` (pngmono, 150 dpi; visually inspected).
- Checked: the end of Theorem 7.1’s proof, the orbit-count/symmetry identity, Section 8 opening, identities (8.1) and (8.2), and the definitions of the summed functions.
- Result: **PASS±**.
- Minor OCR spacing artifact: MinerU Markdown line 1517 breaks the possessive “R̃ⱼ’s” into a colon and separated `s`; the surrounding sentence remains clear. Length symbols in the formulas are confirmed from the page image.
- The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 217) are omitted. No content-level difference was found.
- Repair: none.

## p.040 (PDF p.40 / print p.218)

- Event time: `2026-10-01 21:22 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p040.png` (pngmono, 150 dpi; visually inspected). MinerU figure `images/page_39_image_0.jpg` was read-only and compared with printed Fig. 9.
- Checked: the end of the orbit-description paragraph, Fig. 9 and its caption, Theorem 8.1’s parameter exclusions and equation (8.3), and the opening proof equation.
- Result: **PASS±**.
- Minor evidence note: `pdftotext` drops the negation stroke in the Theorem 8.1 exclusion `(g,n) ≠ (1,1),(0,3)`; the page image confirms `≠`, matching the Markdown. Fig. 9 matches the MinerU image.
- The running head `218 / M. Mirzakhani` is omitted. No Markdown content difference was found.
- Repair: none.

## p.041 (PDF p.41 / print p.219)

- Event time: `2026-10-01 21:55 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p041.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p041_Rtilde.png` (300 dpi source crop).
- Checked: equation (8.4), the definitions of Rᵍ,ⁿⱼ and Dᵍ,ⁿ, the transitivity statement, the R integral and its derivative, and the Bᵍ,ⁿ identity (8.5).
- Result: **FAIL**.
- Difference: MinerU Markdown line 1568 places `(x)` in the subscript of the summed function, producing `R̃_{j(x)}(X)`; PDF p.41 prints `R̃ⱼ(X)` with a separate argument `(X)` (300 dpi crop).
- The text layer drops the negation stroke in the condition `1 ≠ j`; the page image confirms `≠`, matching the Markdown. The running head is omitted.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.042 (PDF p.42 / print p.220)

- Event time: `2026-10-01 22:22 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p042.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p042_Iset.png` (300 dpi source crop).
- Checked: the derivative identity (8.5), the D-integral setup, the connected and disconnected pair-of-pants families, orbit representatives, and equation (8.6).
- Result: **FAIL**.
- Difference: Markdown lines 1597, 1606, 1609, and 1612 use three spellings for the ordered-pair index set (`𝓘`, `τ`, and Fraktur I); PDF p.42 uses one repeated script-I glyph throughout (300 dpi crop).
- The running head `220 / M. Mirzakhani` is omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.043 (PDF p.43 / print p.221)

- Event time: `2026-10-01 22:43 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p043.png` (pngmono, 150 dpi; visually inspected); `audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p043_Adcon.png` (300 dpi source crop).
- Checked: the ordered-pair symmetry note and end of the Theorem 8.1 proof, followed by references [B] through [M] for author, title, venue, year, and page details.
- Result: **FAIL**.
- Difference: MinerU Markdown line 1631 places an overbar over the final `n` of the disconnected-case `dcon` superscript; PDF p.43 prints ordinary `dcon` (300 dpi crop).
- Minor OCR artifacts: the Markdown fuses “of Hyperbolic” as `ofHyperbolic` in the [CEG] title and retains control-code characters where the page image shows the proof-ending QED square.
- The other checked reference details agree. The running title and folio (`Simple geodesics and Weil-Petersson volumes`, 221) are omitted from the Markdown.
- Repair: completed in fix commit 137f56547eb16cb3bfb35e8d1afe51591554a41f; see the overall repair registry below.

## p.044 (PDF p.44 / print p.222)

- Event time: `2026-10-01 23:11 EDT`
- Actor / model / effort: `Peer-P11 / gpt-6-luna / max`
- Evidence: `audit/Mirzakhani_2007_simple_geodesics_published_p044.png` (pngmono, 150 dpi; visually inspected).
- Checked: every remaining reference entry from [Mirz1] through [Zo] for author, title, venue, volume/pages, year, and publication-status wording.
- Result: **PASS±**.
- All checked reference details agree with the PDF page. The running head `222 / M. Mirzakhani` is omitted from the Markdown.
- Repair: none.

### Repair registry
| PDF page | Manual correction | Print evidence | Post-edit check |
|---|---|---|---|
| p.001 | Removed the overbar from V_{g,n}; changed R_{>0}^n to R_{\ge 0}^n; restored the printed journal citation and DOI. | audit/Mirzakhani_2007_simple_geodesics_published_p001.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p001_Rdomain.png | Full reread confirmed. |
| p.002 | Changed the example denominator 2 4 to 24. | audit/Mirzakhani_2007_simple_geodesics_published_p002.png; Table 1 on p.2 | Full reread confirmed. |
| p.003 | Removed the spurious overbar from \mathcal T_{1,1}. | audit/Mirzakhani_2007_simple_geodesics_published_p003.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p003_Tbar.png | Full reread confirmed. |
| p.004 | Restored \to in the \mathcal D,\mathcal R function signature. | audit/Mirzakhani_2007_simple_geodesics_published_p004.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p004_DR_signature.png | Full reread confirmed. |
| p.005 | Reconstructed the \pi^\gamma covering-space definition, delimiters, projection map, and \to\mathcal M_{g,n} arrow. | audit/Mirzakhani_2007_simple_geodesics_published_p005.png | Full reread confirmed. |
| p.006 | Removed the spurious bold \xi after the moduli-space \mathcal M; removed the overbar from the second \mathcal M(S_{g,n}(\gamma),\ell_\gamma=t). | audit/Mirzakhani_2007_simple_geodesics_published_p006.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p006_Mdef.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p006_Mnotation.png | Full reread confirmed. |
| p.007 | Removed the breve accent from L in V_{g,n}(L). | audit/Mirzakhani_2007_simple_geodesics_published_p007.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p007_breveL.png | Full reread confirmed. |
| p.008 | Restored the arrow in f:S\to X; removed the superscript minus from Mod_{g,n}. | audit/Mirzakhani_2007_simple_geodesics_published_p008.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p008_Modnotation.png | Full reread confirmed. |
| p.009 | Restored \omega\in\Omega^2(M) without added dots; changed \bar k=3g-3+\bar n to k=3g-3+n. | audit/Mirzakhani_2007_simple_geodesics_published_p009.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p009_notation.png | Full reread confirmed. |
| p.010 | Replaced the corrupted \gamma_{:} with plain \gamma. | audit/Mirzakhani_2007_simple_geodesics_published_p010.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p010_multicurve.png | Full reread confirmed. |
| p.013 | Restored the missing \to in the type signature H:\mathbb R^2\to\mathbb R. | audit/Mirzakhani_2007_simple_geodesics_published_p013.png | Full reread confirmed. |
| p.015 | Closed the numerator’s \cosh(d(\beta_1,\beta_3)) before +1; restored \to in the function type. | audit/Mirzakhani_2007_simple_geodesics_published_p015.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p015_RandL32.png | Full reread confirmed. |
| p.016 | Restored z\to\infty; removed the overbar from the initial 1 in 1\le i\ne j\le n; restored the \gamma subscripts on all three length functions in (4.1). | audit/Mirzakhani_2007_simple_geodesics_published_p016.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p016_F_and_Thm41.png | Full reread confirmed. |
| p.017 | Restored \to in the \mathcal D,\mathcal R type signature and the \gamma subscripts on the length functions in (4.2). | audit/Mirzakhani_2007_simple_geodesics_published_p017.png | Full reread confirmed. |
| p.018 | Removed the spurious leading H before \Omega(\gamma_x) in cases (b) and (c). | audit/Mirzakhani_2007_simple_geodesics_published_p018.png | Full reread confirmed. |
| p.019 | Removed the spurious hat from \Sigma. | audit/Mirzakhani_2007_simple_geodesics_published_p019.png | Full reread confirmed. |
| p.020 | Removed the colon subscript from \theta; restored (L,\theta)\to(\infty,0). | audit/Mirzakhani_2007_simple_geodesics_published_p020.png | Full reread confirmed. |
| p.022 | Reconstructed “Let \widehat\eta denote…”; restored c:[-r,+r]\to X. | audit/Mirzakhani_2007_simple_geodesics_published_p022.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p022_Let_eta.png | Full reread confirmed. |
| p.025 | Changed L_1^2/2 4 to L_1^2/24; restored the comma between excluded cases (1,1) and (0,3). | audit/Mirzakhani_2007_simple_geodesics_published_p025.png | Full reread confirmed. |
| p.026 | Restored \to in the connected-case function type; replaced the misread \tau_{g,n} index set with the printed script-I symbol \mathcal I_{g,n}. | audit/Mirzakhani_2007_simple_geodesics_published_p026.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p026_Iset.png | Full reread confirmed. |
| p.027 | Restored \to in the disconnected-case function type; normalized the Fraktur-I index set to the printed script-I \mathcal I_{g,n}; removed the duplicate \tag{5} and retained (5.5). | audit/Mirzakhani_2007_simple_geodesics_published_p027.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p027_Iuse.png | Full reread confirmed. |
| p.029 | Changed L^2/2 4 to L^2/24 in (6.1). | audit/Mirzakhani_2007_simple_geodesics_published_p029.png | Full reread confirmed. |
| p.031 | Repaired the polynomial phrase to L_i^2’s, removing the corrupted exponent/apostrophe markup while preserving the printed apostrophe-s. | audit/Mirzakhani_2007_simple_geodesics_published_p031.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p031_Lsquared.png | Full reread confirmed. |
| p.032 | Removed the dot from the exponent L_1^2; restored the printed possessive \alpha_i’s; removed the dot from L_1 in the coefficient monomial. | audit/Mirzakhani_2007_simple_geodesics_published_p032.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p032_Lpowers.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p032_Theorems.png | Full reread confirmed. |
| p.034 | Corrected the set-builder definition so it counts \gamma_i components and restored the missing space in “off a one-handle”. | audit/Mirzakhani_2007_simple_geodesics_published_p034.png | Full reread confirmed. |
| p.035 | Restored the printed possessive heading \mathcal M_{g,n}(L)’s; changed the corrupted \eta_i^{*}s to \eta_i’s; removed the hat from L. | audit/Mirzakhani_2007_simple_geodesics_published_p035.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p035_cover.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p035_Lnotation.png | Full reread confirmed. |
| p.041 | Removed (x) from the subscript, yielding \tilde R_j(X). | audit/Mirzakhani_2007_simple_geodesics_published_p041.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p041_Rtilde.png | Full reread confirmed. |
| p.042 | Normalized all four ordered-pair index-set occurrences to the same printed script-I notation \mathcal I_{g,n}. | audit/Mirzakhani_2007_simple_geodesics_published_p042.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p042_Iset.png | Full reread confirmed. |
| p.043 | Removed the overbar from the final n in the dcon superscript. | audit/Mirzakhani_2007_simple_geodesics_published_p043.png; audit/300dpi/Mirzakhani_2007_simple_geodesics_published_p043_Adcon.png | Full reread confirmed. |

---

# 独立重做审计（第二轮 redo，PDF p.001–p.008）

- 性质：独立第二轮重做审计，逐页重新渲染 PNG 亲眼目检，不沿用 `.redo.md`（Wf-R-P11, GLM-5.3-Flash）
  的既有结论；下文每条判定均以本人所看原页 PNG + `pdftotext` 文本层双通道对账为据。
- Actor: `Wf-R-P11b`
- Host / model / effort: zcode / `opencode-go-chat-space-bunny-free` / effort 自报 UNKNOWN
- 日期：2026-10-05
- 被检 Markdown 基线：`Mirzakhani_2007_simple_geodesics_published_mineru/Mirzakhani_2007_simple_geodesics_published__Mirzakhani_2007_simple_geodesics_published.md`
  SHA-256 = `caed1c35240a77045b69c930f5fe442b10e0936c4137ff4f3dc2174a5bcd5c51`（1698 行；= HEAD `b3048fcb`，`git status` 工作树干净）
- PDF：`Mirzakhani_2007_simple_geodesics_published.pdf`（44 页）SHA-256 = `c19a088d97b2b3223481341d059ef7836ea9f575f580d3bf574d0b475e7615cf`
- 印刷页码换算：Invent. math. 167, 179–222 (2007)；PDF p.N = 印刷 p.(178+N)。
- 本节只覆盖 PDF p.1–p.8；上文 Peer-P11 的 p.001–p.044 记录作为历史证据原样保留，未改写。

## p.001（PDF p.1 / 印刷 p.179）
- PNG：/tmp/mirzakhanipub_audit_p001.png（pngmono 150dpi；`gs -q -dNOPAUSE -dBATCH -sDEVICE=pngmono -r150 -dFirstPage=1 -dLastPage=1`）
- 核对：题录——刊眉 `Invent. math. 167, 179–222 (2007)`、`DOI: 10.1007/s00222-006-0013-2`；标题
  `Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces`；
  作者 Maryam Mirzakhani；单位 `Department of Mathematics, Princeton University, Fine Hall, Washington Road, Princeton, NJ 08544, USA (e-mail: mmirzakh@math.princeton.edu)`；
  `Oblatum 19-VII-2005 & 17-VII-2006`；`Published online: 12 October 2006 – © Springer-Verlag 2006`；
  Contents 1–8 与页码 179/186/190/194/203/206/211/217；`1. Introduction` 节标题；§1 首段全句与行内式
  $V_{g,n}(L_1,\ldots,L_n)$、$\mathcal{M}_{g,n}(L_1,\ldots,L_n)$、$V_{g,n}(L)$、
  $(\mathbb{R}_{\ge0})^n$、$\mathbf{Mod}_{g,n}$、$\mathcal{T}_{g,n}(L)$；页末断在 `We`。
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - MD L27/L29 行内公式两侧空格被 MinerU 合并（`volume$V_{g,n}(L_1,\ldots,L_n)$of`、`Given$L=...$`），
    纯排版伪影，按 SOP「PASS± 排版级伪影默认不批量改」保留。
  - 刊眉 `Invent. math.` + DOI 在原页位于标题**之上**的页眉块，MD L3–L4 置于标题**之下**，属 MinerU
    阅读顺序伪影；两行内容与原页逐字一致，不改。
  - Contents 点线被简化为 `.....`（MD L16–L23），条目与页码均正确。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.001 修两处（补录刊眉/DOI、
  $R_{>0}^n\to R_{\ge0}^n$）；当前 MD L3–L4 与 L29 的 $(\mathbb{R}_{\ge0})^n$ 与本人所看原页一致，
  该两处旧修复正确保留，非回归。
- 备注：原页本页正文 `Mod` 为**粗体**，MD `\mathbf{Mod}` 对应无误（第 4、5 页原页该词为正体，
  系印刷原文自身混用，本轮如实对应，不作统一）。

## p.002（PDF p.2 / 印刷 p.180）
- PNG：/tmp/mirzakhanipub_audit_p002.png（pngmono 150dpi，gs -r150 -dFirstPage=2 -dLastPage=2）；
  仲裁裁剪：/tmp/mirzakhanipub_p002_tabcoef_300crop.png、/tmp/mirzakhanipub_p002_lastrow_300crop.png
  （300dpi 重渲本页后 PIL 裁切放大 Table 1 系数列与末行，仅裁图未写 Markdown）
- 核对：页眉 `180 / M. Mirzakhani`；页顶承接句 `study the Weil-Petersson volume of the quotient space`
  与展示式 $\mathcal{M}_{g,n}(L)=\mathcal{T}_{g,n}(L)/\mathrm{Mod}_{g,n}.$；`Our main result, obtained in Sect. 6, is:`；
  Theorem 1.1 全陈述（`The volume … is a polynomial in … ; namely we have:`）；展示式
  $V_{g,n}(L)=\sum_{\alpha,\,|\alpha|\le 3g-3+n}C_\alpha\cdot L^{2\alpha},$（求和下限/上限、系数 $C_\alpha$、$L^{2\alpha}$）；
  `where $C_\alpha>0$ lies in $\pi^{6g-6+2n-|2\alpha|}\cdot\mathbb{Q}$.`；多指标约定整句
  （$\alpha=(\alpha_1,\ldots,\alpha_n)$、$(\mathbb{Z}_{\ge0})^n$、$L^\alpha$、$|\alpha|=\sum_{i=1}^n\alpha_i$）；
  `Moreover, in Sect. 5 …`；$V_{1,1}(L)=L^2/24+\pi^2/6.$；Wolpert 段（$\pi^{6g-6+2n}$、[Wol2]）；
  [Zo] 段（$\mathrm{Vol}_{0,n}(0)$、$\mathcal{M}_{0,n}$）；Remark 整段；Table 1 表题与全部 6 行数值。
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格被 MinerU 合并（`volume$V_{g,n}…$is`、`where$C_\alpha>0$lies in`、`is a polynomial in$L_1^2,\ldots,L_n^2$; namely we have:`、
    `Here the exponent$\alpha=…$ranges over…`、`and$|\alpha|=\sum…$` 等），纯排版伪影，按 SOP 保留。
  - 页眉/页码 `180 / M. Mirzakhani` 未收录（全篇通例，登记一次）。
- **print quirk 忠实登记不改**：Table 1 的 $(g,n)=(0,4)$ 行印刷系数为 **1/2**——300dpi 裁剪
  （/tmp/mirzakhanipub_p002_tabcoef_300crop.png）与原页直读双证，分数字形为 `2`（与同表 `192`、`24`、
  `8` 的 `2` 同一字形）。注意 `pdftotext -f 2 -l 2` 文本层把该处误抽成 `1/3`，**文本层不可作裁决**，
  以原页图为准：印刷即 1/2。MD L68 `\frac{1}{2}` 与印刷一致，未按任何外部数值「纠正」。
  同表 $(1,2)$ 行印刷为 **1/192** 且第二因子为 $(12\pi^2+L_1^2+L_2^2)$；$(2,1)$ 行印刷分母 **2211840**
  （300dpi 裁剪 /tmp/mirzakhanipub_p002_lastrow_300crop.png 直证）。三处 MD 均与印刷吻合。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.002 把示例分母 `2 4` 修为 `24`
  （现 MD L50 `\frac{L^{2}}{24}`，与原页 $L^2/24+\pi^2/6$ 及 Table 1 $(1,1)$ 行的 1/24 一致，正确保留）；
  `.redo.md` 记录的 p.002 三处标点修复在当前 MD 中亦已生效（Theorem 1.1 的 `$L_n^2$; namely`、
  多指标约定句末逗号与句号），本轮目视确认与印刷一致。
- 备注：本页覆盖 MD L30–L74（Table 1 末行为本页最后内容，表格边框在原页闭合完整）；`We approach the calculation…`
  起属 p.3。

## p.003（PDF p.3 / 印刷 p.181）
- PNG：/tmp/mirzakhanipub_audit_p003.png（pngmono 150dpi，gs -r150 -dFirstPage=3 -dLastPage=3）；
  仲裁裁剪：/tmp/mirzakhanipub_p003_phi_300crop.png（Dehn 扭转符号）、/tmp/mirzakhanipub_p003_R_300crop.png（$\ell$ 的值域符号）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 181`；页顶段（`We approach the calculation…`
  全句、$X\in\mathcal{M}_{g,n}$、[M]、$\mathcal{M}_{g,n}=\mathcal{T}_{g,n}/\mathrm{Mod}_{g,n}$、Teichmüller）；
  `McShane identity.` 引导句与 [M]；Theorem 1.2 (McShane) 全陈述；展示式 (1.1)
  $\sum_\gamma(1+e^{\ell_\gamma(X)})^{-1}=\frac12$；求和说明句；`Calculation of Vol(M_{1,1}).` 段与
  $g=n=1$；$\mathcal{M}_{1,1}^*$ 定义展示式；$\pi:\mathcal{M}_{1,1}^*\to\mathcal{M}_{1,1}$ 与
  $\pi(X,\gamma)=X$；$\ell:\mathcal{M}_{1,1}^*\to\mathbb{R}$ 与 $\ell(X,\gamma)=\ell_\gamma(X)$；
  展示式 (1.2) $\sum_{\pi(Y)=X}f(\ell(Y))=\frac12$；$f(x)=(1+e^x)^{-1}$；Fenchel-Nielsen 整段
  （`once punctured` 无连字符、$\mathcal{M}^*_{1,1}=\mathcal{T}_{1,1}/\mathrm{Stab}(\alpha)$、
  $\phi_\gamma(\ell,\tau)=(\ell,\ell+\tau)$）；末行 $\mathcal{M}_{1,1}^*\cong\{(\ell,\tau)\mid 0\le\ell\le\tau\}/(x,0)\sim(x,x)$。
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`on$X\in…$.`、`geodesics γ on$X .$`、`Calculation of$\mathrm{Vol}…$`、
    `defined by$\pi(X,\gamma)=X$`、`define$\ell:…$by`、`where$f(x)=…$` 等），纯排版伪影，按 SOP 保留。
  - 原页 `Consider the space of pairs:` 起新段，MD 并入上一段（L84），段落切分信息丢失，不影响语义。
  - 平文字符 γ、α（MD L82/L110）未加数学斜体标记，字形与原页相同，不误导。
  - 页眉/页码未收录（全篇通例）。
- **字形仲裁（150dpi 误读纠正，以原图为准）**：Dehn 扭转映射符号在 150dpi 下我初读作 $\psi_\gamma$，
  但 `pdftotext -f 3 -l 3` 文本层作 $\phi_\gamma$；改用 300dpi 重渲并 PIL 裁切放大
  （/tmp/mirzakhanipub_p003_phi_300crop.png）直证原页印的是**圆圈加贯穿竖笔**的 loopy $\phi$，
  而非 $\psi$。MD L110 `\phi_\gamma` 与印刷一致，**无需改动**；本人 150dpi 判读错误已在此登记，不据其改稿。
- 另一字形仲裁：`\ell:\mathcal{M}_{1,1}^*\to\mathbb{R}` 的值域在 300dpi 裁剪
  （/tmp/mirzakhanipub_p003_R_300crop.png）中确证为**黑板粗体 ℝ**（双线 R），MD L96 `\mathbb{R}` 正确。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.003 去掉 $\mathcal{T}_{1,1}$ 上的伪横线
  （当前 MD L110 `=\mathcal{T}_{1,1}/\mathrm{Stab}(\alpha)` 与原页一致，正确保留）；`.redo.md` 记录的
  `McShane's` 拼合、句末句号、$\mathbb{R}$ 黑板体、$f(x)$ 句号、逗号补回等修复在当前 MD 中均已生效且与印刷一致。
- 备注：本页覆盖 MD L74–L114；`On the other hand, the Weil-Petersson symplectic form…` 起属 p.4。

## p.004（PDF p.4 / 印刷 p.182）
- PNG：/tmp/mirzakhanipub_audit_p004.png（pngmono 150dpi，gs -r150 -dFirstPage=4 -dLastPage=4）；
  仲裁裁剪：/tmp/mirzakhanipub_p004_Mod_300crop.png（Mod 字重）、/tmp/mirzakhanipub_p004_DR_300crop.png（𝒟/ℛ 与 ℝ₊³）
- 核对：页眉 `182 / M. Mirzakhani`；`On the other hand…` 全句与 $\pi^*(\omega_{wp})=d\ell\wedge d\tau$；
  三重积分展示式（$\int_{\mathcal{M}_{1,1}}\sum_{\pi(Y)=X}f(\ell(Y))dX=\int_{\mathcal{M}^*_{1,1}}f(\ell(Y))dY=\int_0^\infty f(x)\int_0^x 1\,dy\,dx.$，含两个上限 $\infty$/两个 $0$ 下限与内层上限 $x$）；
  `Integrating McShane's identity (1.2) …` 句；$\mathrm{Vol}(\mathcal{M}_{1,1})=2\int_0^\infty\ell f(\ell)d\ell=2\int_0^\infty\frac{\ell}{1+e^\ell}d\ell=\frac{\pi^2}{6}$；
  `Calculation of V_{g,n}.` 段；(I)/(II) 两条；`We now turn to…`；`(I): Generalized McShane's identity.` 整段
  （含 `each orbit of Mod_{g,n}`、$\mathcal{D},\mathcal{R}:\mathbb{R}_+^3\to\mathbb{R}_+$、pairs of pants、(Sect. 4)）；
  Theorem 1.3 全陈述；展示式 (1.3)（两个求和号、下标 $\{\gamma_1,\gamma_2\}$ / $i=2,\gamma$、两个 $\mathcal{D}$/$\mathcal{R}$ 实参、$=L_1.$、编号 (1.3)）；
  `Here, the first sum …` 整句；页末 `In the formula above … geodesic of length 0.`
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`given by$\pi^*(\omega_{wp})=…$`、`over$\mathcal{M}_{1,1}$against`、
    `Calculation of$V_{g,n}$.`、`for${ \mathcal{M}}_ {g,n}$we will:`、`functions$\mathcal{D}$, $\mathcal{R}:\mathbb{R}_+^3\to\mathbb{R}_+$related` 等），
    纯排版伪影，按 SOP 保留。
  - 平文字符 X、γ、α（MD L114/L144/L146）未加数学斜体标记，字形与原页相同，不误导。
  - 页眉/页码未收录（全篇通例）。
- 字形仲裁（300dpi 确认）：`each orbit of Mod_{g,n}` 中原页印的是**正体 roman** `Mod`
  （/tmp/mirzakhanipub_p004_Mod_300crop.png：笔画均匀、细衬线，与同页小写正体同粗细），
  MD L136 `\mathrm{M o d}_{g,n}` 正确——**不与 p.1 的粗体 $\mathbf{Mod}$ 混为一谈**，原页系自身混用。
  另：$\mathcal{D},\mathcal{R}$ 确为花体（calligraphic），$\mathbb{R}_+^3$ 确为黑板粗体，
  且原页 $\mathcal{R}:\mathbb{R}_+^3$ **冒号后确有箭头** $\to$（/tmp/mirzakhanipub_p004_DR_300crop.png 与文本层 `R3+ → R+` 双证），
  MD L136 箭头在位，正确。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.004 补回 $\mathcal{D},\mathcal{R}$ 签名中丢失的
  `\to`（当前 MD L136 箭头在位，与原页一致，正确保留）。`.redo.md` 记录的 $\mathrm{Mod}$ 正体、$\mathcal{D}$ 花体、
  `pair ofpants`→`pair of pants`、平文 γ→$\gamma$ 修复在当前 MD 中均已生效。
- 备注：本页覆盖 MD L116–L146（页末止于 `geodesic of length 0.`）；`As a special case, for any hyperbolic surface X of genus one…` 起属 p.5。

## p.005（PDF p.5 / 印刷 p.183）
- PNG：/tmp/mirzakhanipub_audit_p005.png（pngmono 150dpi，gs -r150 -dFirstPage=5 -dLastPage=5）；
  仲裁裁剪：/tmp/mirzakhanipub_p005_Modorbit_300crop.png（正文 Mod-orbit）、/tmp/mirzakhanipub_p005_Ogamma_300crop.png（𝒪_γ 展示式内 Mod）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 183`；`As a special case…` 句；展示式 (1.4)
  $\sum_\gamma\mathcal{D}(L,\ell_\gamma(X),\ell_\gamma(X))=L,$；`where the sum is over all non-peripheral…` 与
  `On the other hand, we have (Sect. 3)`；展示式 $\mathcal{D}(x,y,y)\sim\frac{2x}{1+e^y}$；
  `as x → 0. Therefore … implies the original McShane identity (1.1) when L → 0.`（`implies` 为印刷斜体强调）；
  `(II): Integration over the moduli space.` 整段（Sect. 7、(1.3)、$\mathcal{M}_{g,n}(L)$）；
  `Let S_{g,n} …` 整段（closed surface、$Y\in\mathcal{T}_{g,n}$、[γ]、$\ell_\gamma(Y)$）；
  `To each simple closed curve …` 句；展示式 $\mathcal{O}_\gamma=\{[\alpha]\mid\alpha\in\mathrm{Mod}_{g,n}\cdot\gamma\}$；
  `of homotopy classes … Mod_{g,n}-orbit … For any function f : ℝ₊ → ℝ₊,`；展示式
  $f_\gamma(X)=\sum_{[\alpha]\in\mathcal{O}_\gamma}f(\ell_\alpha(X))$；`defines a function` 与展示式
  $f_\gamma:\mathcal{M}_{g,n}\to\mathbb{R}_+$；`Our goal is to calculate…`（Theorem 7.1）；
  `First, consider the covering space…`；覆盖空间展示式
  $\pi^\gamma:\mathcal{M}^\gamma_{g,n}=\{(X,\alpha)\mid X\in\mathcal{M}_{g,n},\text{ and }\alpha\in\mathcal{O}_\gamma\text{ is a geodesic on }X\}\to\mathcal{M}_{g,n}$；
  `where π^γ(X,α) = X. The hyperbolic length function descends to the function` 与末行展示式
  $\ell:\mathcal{M}^\gamma_{g,n}\to\mathbb{R}_+$。
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`geodesics$\gamma$on$X$`、`as$x \to 0$`、`when$L \to 0$`、`over${ \mathcal{M}}_{g,n}(L)$`、
    `Let$S_{g,n}$be`、`on$S_{g,n}$`、`curve$\gamma$on`、`the$\mathrm{Mod}_{g,n}\mathrm{-orbit}$of$\gamma$on`、
    `function$f:\mathbb{R}_+\to\mathbb{R}_+$` 等），纯排版伪影，按 SOP 保留。
  - MD L172 把连字符词 `-orbit` 写成 `\mathrm{- o r b i t}`（字母间补空格），渲染结果仍为 `-orbit`，
    仅源码可读性伪影，语义与检索均不受影响，不改。
  - 平文字符 X、Y、γ、α（MD L148/L164/L172/L184/L194）未加数学斜体标记，字形与原页相同，不误导。
  - 页眉/页码未收录（全篇通例）。
- 字形仲裁（300dpi 确认）：本页两处 `Mod` 均为**正体 roman**——展示式 $\mathcal{O}_\gamma=\{\cdots\mid\alpha\in\mathrm{Mod}_{g,n}\cdot\gamma\}$ 内
  （/tmp/mirzakhanipub_p005_Ogamma_300crop.png，笔画均匀细衬线，非粗体）与正文 `Mod_{g,n}-orbit` 内
  （/tmp/mirzakhanipub_p005_Modorbit_300crop.png）；MD L169 `\operatorname{Mod}`、L172 `\mathrm{Mod}` 均正确。
  与 p.1 的粗体 $\mathbf{Mod}$ 差异属**印刷原文自身混用**，如实对应，不作统一。
  另确认 $\mathcal{O}_\gamma$ 中 $\mathrm{Mod}_{g,n}$ 与 $\gamma$ 之间为居中点 `·`（`\cdot`），MD 一致。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.005「重建 covering space 定义式、定界符、
  投影映射与 $\to\mathcal{M}_{g,n}$ 箭头」；当前 MD L188 该式与原页逐项吻合（含 `and` 一词与两处箭头），
  旧修复正确保留，非回归。`.redo.md` 记录的五处句号/逗号补回、$\mathrm{Mod}$ 正体、`pair of pants` 等修复
  在当前 MD 中均已生效。
- 备注：本页覆盖 MD L148–L192（页末为 $\ell:\mathcal{M}^\gamma_{g,n}\to\mathbb{R}_+$ 展示式）；
  `defined by ℓ(X,η) = ℓ_η(X). Therefore, we have` 起属 p.6。

## p.006（PDF p.6 / 印刷 p.184）
- PNG：/tmp/mirzakhanipub_audit_p006.png（pngmono 150dpi，gs -r150 -dFirstPage=6 -dLastPage=6）；
  仲裁裁剪：/tmp/mirzakhanipub_p006_bundle_300crop.png（圆丛箭头图）
- 核对：页眉 `184 / M. Mirzakhani`；`defined by ℓ(X,η) = ℓ_η(X). Therefore, we have`；
  展示式 $\int_{\mathcal{M}_{g,n}}f_\gamma(X)dX=\int_{\mathcal{M}^\gamma_{g,n}}f\circ\ell(Y)dY.$；
  `On the other hand, the function f is constant on each level set of ℓ and we have`；
  展示式 $\int_{\mathcal{M}^\gamma_{g,n}}f\circ\ell(Y)dY=\int_0^\infty f(t)\mathrm{Vol}(\ell^{-1}(t))dt,$（$\infty$/$0$ 限、$\mathrm{Vol}$ 正体）；
  `where the volume is taken with respect to the volume form induced on ℓ⁻¹(t).`；`The main idea for integrating over…` 整段；
  `Let S_{g,n}(γ) denote…` 整段（$S_{g,n}(\gamma)\cong S_{g,n}-U_\gamma$、$U_\gamma$、$\gamma\times(0,1)$、`n+2`、
  $\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t)$ 定义整句、末句 `We have a natural circle bundle`）；
  三行箭头图（$\ell^{-1}(t)\subset\mathcal{M}^\gamma_{g,n}$ / ↓ / $\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t).$）；
  `We will study the S¹-action…` 整段（$S^1$ 两处、$\ell^{-1}(t)/S^1$、Sect. 7）；
  展示式 $\ell^{-1}(t)/S^1\cong\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t)$；`as symplectic manifolds. So we expect to have`；
  展示式 $\mathrm{Vol}(\ell^{-1}(t))=t\,\mathrm{Vol}(\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t)).$（系数 $t$ 在位）；
  页末 `But as we will see in Sect. 7, the situation is different when γ separates off a one-handle in which case the length of the fiber of the S¹-action at a point`。
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`defined by$\ell(X,\eta)=\ell_\eta(X)$.`、`the function$f$is constant`、`level set of$\ell$and we have`、
    `integrating over$\mathcal{M}^\gamma_{g,n}$is`、`curve$\gamma$gives`、`description of $\mathcal{M}^\gamma_{g,n}$in terms`、
    `integral of$f_\gamma$in terms`、`$\gamma$separates off` 等），纯排版伪影，按 SOP 保留。
  - MD L210 把印刷 `along γ; that is` 的分号并入数学模式写作 `\gamma ;$`，数学模式内多一空格 + 分号外置，
    语义无歧义（同页 p.7 已按通例不逐处改），不改。
  - 原页 `The main idea…` 段与 `We have a natural circle bundle` 之间无空行，属排版细节，MD 一致。
  - 页眉/页码未收录（全篇通例）。
- 字形仲裁（300dpi 确认）：圆丛箭头图中间符号原页是**单笔长竖箭头**（细长杆 + 小箭头尖，
  /tmp/mirzakhanipub_p006_bundle_300crop.png），非双线 $\Downarrow$；`pdftotext -f 6 -l 6` 文本层把它抽成两段
  `⏐` 属文本层失真，不作依据。MD L213 `\Big\downarrow` 与原页相符；同式 $\mathcal{M}$ 为花体、$S_{g,n}$ 为斜体，
  下标 $\ell_\gamma=t$ 亦一致。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.006 去掉模空间 $\mathcal{M}$ 后的伪 $\boldsymbol\xi$
  并去掉第二个 $\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t)$ 上的伪横线；当前 MD L210/L213/L216/L219/L225 五处
  $\mathcal{M}$ 与 $\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t)$ 经本人逐处目视比对**均无** $\xi$、**均无**横线，
  与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L194–L228 前半（页末断在 `at a point`，`is in fact t/2 instead of t. Hence, …` 起属 p.7）。

## p.007（PDF p.7 / 印刷 p.185）
- PNG：/tmp/mirzakhanipub_audit_p007.png（pngmono 150dpi，gs -r150 -dFirstPage=7 -dLastPage=7）；
  仲裁裁剪：/tmp/mirzakhanipub_p007_riven_300crop.png（页脚致谢拼写）、/tmp/mirzakhanipub_p007_SL_300crop.png（$SL(n,\mathbb{R})$）、
  /tmp/mirzakhanipub_p007_bar1_300crop.png 与 /tmp/mirzakhanipub_p007_bar2_300crop.png（两处 $\overline{\mathcal{M}}_{g,n}$ 的横线）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 185`；跨页承接句
  `is in fact t/2 instead of t. Hence, for any connected simple closed curve γ on S_{g,n}, we have`；
  展示式 (1.5)（$\int_{\mathcal{M}_{g,n}}f_\gamma(X)dX$、指数 $2^{-M(\gamma)}$、$\int_0^\infty$、因子 $f(t)\,t\,\mathrm{Vol}(\mathcal{M}(S_{g,n}(\gamma),\ell_\gamma=t))dt$、编号 (1.5)）；
  $M(\gamma)$ 定义句；`An alternative proof of Theorem 1.1.` 整段（含 [Mirz2]、$\overline{\mathcal{M}}_{g,n}$、recursive algorithm）；
  `Applications.` 整段（[Mirz1]、[Mirz2]、Sect. 5、Virasoro、Witten-Kontsevich [K]、$\mathcal{M}_{g,n}$、$\mathrm{Hom}(\pi_1(S),G)/G$、
  [D]/[BL]/[JK]）；`In [LM], F. Labourie and G. McShane …` 段与 $SL(n,\mathbb{R})$；
  `Notes and references.` 整段（[KMZ]、[Zo]、[MaZ]、[Pen]、$V_{1,1}(L)$、[NN] 两处、[TWZ2]/[TWZ1]）；
  页脚小字 Acknowledgements 第一段（Curt McMullen、Said Akbari、Izzet Coskun、Chiu-Chu Melissa Liu、Andrei Okounkov、Igor Riven）。
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`fiber of the$S^1$-action`、`in fact$t/2$instead`、`$t/2$instead of t`、
    `curve$\gamma$on`、`show that$V_{g,n}(L)$is`、`formula for$V_{g,n}(L)$in terms`、`overline{M}_{g,n}$. However`、
    `polynomial$V_{g,n}(L)$with`、`$V_{g,n}(L)$to intersection`、`$\overline{\mathcal{M}}_{g,n}$ [Mirz2]. The`、
    `$\mathcal{M}_{g,n}$and the variety`、`$\mathcal{M}_{g,n}$ [MaZ]` 等），纯排版伪影，按 SOP 保留。
  - MD L234 把印刷的散文 `if` 摄入数学模式（`M(\gamma)=1\operatorname{if}\gamma`），渲染仍为 `if`，
    语义无歧义，不改。
  - 平文字符 γ、S、G（MD L234/L238/L240/L242）未加数学斜体标记，字形与原页相同，不误导。
  - 结构伪影：MD L244 把页脚致谢第一段包在
    `<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">…</span></small>`
    内（MinerU 导出伪影，对应原页小字页脚位置）；正文内容逐字与印刷一致，不动。
  - 页眉/页码未收录（全篇通例）。
- **print quirk 忠实登记不改（重要）**：页脚致谢印作 `… Andre**i** Okounkov, and Igor **Riven** for helpful discussions.`
  ——300dpi 裁剪（/tmp/mirzakhanipub_p007_riven_300crop.png）直证字形为 `R-i-v-e-n`（Riven），
  与 `pdftotext -f 7 -l 7` 文本层 `Igor Riven` 一致。该数学家通行拼写为 Igor Rivin，
  即**印刷原文自身 typo**。按 print-primacy，MD L244 保留 `Riven` **正确，不按文献常识改写**。
- 字形仲裁（300dpi 确认）：$SL(n,\mathbb{R})$ 中 R 为**黑板粗体 ℝ**（/tmp/mirzakhanipub_p007_SL_300crop.png），
  MD L240 `\mathbb{R}` 正确；两处 `$\overline{\mathcal{M}}_{g,n}$` 的横线在原页**确实存在**
  （bar1「classes **over** $\overline{\mathcal{M}}_{g,n}$.」、bar2「classes **on** $\overline{\mathcal{M}}_{g,n}$ [Mirz2].」），
  MD L236/L238 均带横线，正确；同段稍后「similarities between $\mathcal{M}_{g,n}$ and the variety」原页**无横线**，
  MD L238 该处亦无横线，一一对应正确。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.007 去掉 $V_{g,n}(L)$ 中 L 上的抑扬符
  （breve）；当前 MD L236 `V _ { g , n } ( L )` 与 L238 两处均无 breve，与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L228 后半–L244；致谢第二段（Greg McShane/Scott Wolpert/IPM/Clay fellowship，MD L246）起属 p.8。

## p.008（PDF p.8 / 印刷 p.186）
- PNG：/tmp/mirzakhanipub_audit_p008.png（pngmono 150dpi，gs -r150 -dFirstPage=8 -dLastPage=8）；
  仲裁裁剪：/tmp/mirzakhanipub_p008_mod1_300crop.png（`Let Mod(S)`）、/tmp/mirzakhanipub_p008_mod2_300crop.png（正文 $\mathbf{Mod}_{g,n}=\mathbf{Mod}(S_{g,n})$）、
  /tmp/mirzakhanipub_p008_mod3_300crop.png（展示式 `/Mod_{g,n}`）
- 核对：页眉 `186 / M. Mirzakhani`；页顶致谢第二段（Greg McShane、Scott Wolpert、Max Planck Institute of Mathematics in Leipzig、
  Institute for Studies in Theoretical Physics and Mathematics (IPM) in Tehran、referee、Clay fellowship）全句逐字；
  `2. Background material` 节标题；`In this section, we recall … See [IT] and [Bus] for more details.`；
  `Teichmüller space.` 段（$\mathcal{T}(S)$、$f:S\to X$、`The map f provides a marking on X by S.`、
  `$f:S\to X$ and $g:S\to Y$`、$f\circ g^{-1}:Y\to X$、`When ∂S is nonempty`、$A=\partial S$、
  $L=(L_\alpha)_{\alpha\in A}\in\mathbb{R}_+^{|A|}$（上标 $|A|$ 在位）、$X\in\mathcal{T}(S,L)$、$\beta\in\partial S$）；
  展示式 $\ell_\beta(X)=L_\beta.$；`Let S_{g,n} be an oriented connected surface … Then let` 与 $(\beta_1,\ldots,\beta_n)$；
  展示式 $\mathcal{T}_{g,n}(L_1,\ldots,L_n)=\mathcal{T}(S_{g,n},L_1,\ldots,L_n)$；
  `denote the Teichmüller space …` 整段（`Mod(S)`、isotopy classes、`set wise`、`$\mathbf{Mod}_{g,n}=\mathbf{Mod}(S_{g,n})$`、
  $\mathcal{T}_{g,n}(L)$、`The quotient space`）；展示式
  $\mathcal{M}_{g,n}(L)=\mathcal{M}(S_{g,n},\ell_{\beta_i}=L_i)=\mathcal{T}_{g,n}(L_1,\ldots,L_n)/\mathrm{Mod}_{g,n}$；
  `is the moduli space of Riemann surfaces … of length ℓ_{β_i} = L_i.`；`By convention, a geodesic of length zero is a cusp and we have`；
  展示式 $\mathcal{T}_{g,n}=\mathcal{T}_{g,n}(0,\ldots,0),$；`and`；末行展示式 $\mathcal{M}_{g,n}=\mathcal{M}_{g,n}(0,\ldots,0).$
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`Teichmüller space$\mathcal{T}(S)$is`、`diffeomorphism$f:S\to X$`、
    `Two marked surfaces$f:S\to X$and $g:S\to Y$define`、`same point in$\mathcal{T}(S)$if and only if$f\circ g^{-1}:Y\to X$ is`、
    `Let$A=\partial S$and$L=…$`、`A point$X\in\mathcal{T}(S,L)$ is`、`component$\beta\in\partial S$, we have`、
    `Let$S_{g,n}$be`、`on$S_{g,n}$with`、`$\mathbf{Mod}(S_{g,n})$ acts on$\mathcal{T}_{g,n}(L)$by`、
    `homeomorphic to$S_{g,n}$with` 等），纯排版伪影，按 SOP 保留。
  - MD L267/L275/L281 三处把印刷省略号写作 `\dots`，同页另几处用 `\ldots`；两者渲染相同，仅源码风格不一致，
    检索与语义均不受影响，不改。
  - 结构伪影：原页页顶致谢第二段是小字页脚续（接 p.7 脚注），MinerU 作普通正文段落（MD L246），
    字号/位置信息丢失，内容逐字一致，不补包装。
  - 页眉/页码未收录（全篇通例）。
- **print quirk 忠实登记不改**：原页印作 `leaving each boundary component *set wise* fixed.`
  ——`set wise` 分写（且为斜体强调），通行英文作 `setwise`。300dpi 字形与 `pdftotext -f 8 -l 8`
  文本层 `set wise fixed` 双通道一致；MD L264 原样保留 `set wise`，**不按英语正字法改写**。
- 字形仲裁（300dpi 确认，本页三处 `Mod` 字重各异且 MD 一一对应）：
  - `Let Mod(S) denote…` 为**常规正体**（/tmp/mirzakhanipub_p008_mod1_300crop.png，笔画与周围散文同细）→
    MD L264 该处为平文 `Mod(S)`，正确；
  - `The mapping class group Mod_{g,n} = Mod(S_{g,n})` 为**粗体正体**
    （/tmp/mirzakhanipub_p008_mod2_300crop.png，M/o/d 明显加粗）→ MD L264 `\mathbf{Mod}` 两处，正确；
  - 展示式 `/ Mod_{g,n}` 为**非粗体正体**（/tmp/mirzakhanipub_p008_mod3_300crop.png，与邻近数学斜体同细）→
    MD L267 `\operatorname{Mod}`，正确。
  三者并存系印刷原文自身混用（如实对应），不作统一。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.008 补回 $f:S\to X$ 的箭头并去掉
  $\mathrm{Mod}_{g,n}$ 上的伪上标负号；当前 MD L252 两处 $f:S\to X$（及 $g:S\to Y$）箭头均在位、
  L267 的 `\operatorname{Mod}_ {g,n}` **无**多余上标，与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L246–L282（页末为 $\mathcal{M}_{g,n}=\mathcal{M}_{g,n}(0,\ldots,0).$ 展示式）；
  `For a disconnected surface S = ⋃ S_i …` 起属 p.9。

## p.009（PDF p.9 / 印刷 p.187）
- PNG：/tmp/mirzakhanipub_audit_p009.png（pngmono 150dpi，gs -r150 -dFirstPage=9 -dLastPage=9）；
  仲裁裁剪：/tmp/mirzakhanipub_p009_Tbraces_300crop.png（$\mathcal{T}_{g,n}$ 后的定界符）、
  /tmp/mirzakhanipub_p009_Pset_300crop.png（$\mathcal{P}=\{\alpha_i\}_{i=1}^k$）、
  /tmp/mirzakhanipub_p009_Rsup_300crop.png（$\mathbb{R}_+^{\mathcal{P}}\times\mathbb{R}^{\mathcal{P}}$）、
  /tmp/mirzakhanipub_p009_omega2M_300crop.png（$\omega\in\Omega^2(M)$）、
  /tmp/mirzakhanipub_p009_omegawp_300crop.png（Theorem 2.1 的 $\omega_{wp}$ 式）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 187`；`For a disconnected surface…` 句与展示式
  $\mathcal{M}(S,L)=\prod_{i=1}^k\mathcal{M}(S_i,L_{A_i}),$（求和上下限 $k$/$i=1$）；`where L_{A_i} = (L_s)_{s∈A_i}.`；
  `The Weil-Petersson symplectic form.` 整段（$\omega\in\Omega^2(M)$、$\frac{1}{n!}\omega\wedge\cdots\wedge\omega$、
  Goldman [Gol]、$\mathcal{T}_{g,n}(L_1,\ldots,L_n)$、$\omega$ or $\omega_{wp}$、Note that when S is disconnected）；
  展示式 $\mathrm{Vol}(\mathcal{M}(S,L))=\prod_{i=1}^k\mathrm{Vol}(\mathcal{M}(S_i,L_{A_i})).$；
  `The Fenchel-Nielsen coordinates.` 整段（pants decomposition、$\mathcal{P}=\{\alpha_i\}_{i=1}^k$、$k=3g-3+n$、
  $X\in\mathcal{T}_{g,n}(L)$、FN 坐标 $2k$ 元组、twisting parameters、[Bus]）；展示式
  $\mathcal{T}_{g,n}(L)\cong\mathbb{R}_+^{\mathcal{P}}\times\mathbb{R}^{\mathcal{P}}$；`by the map` 与展示式
  $X\to(\ell_{\alpha_i}(X),\tau_{\alpha_i}(X)).$；`By work of Wolpert … [Wol1].`；Theorem 2.1 (Wolpert) 陈述与展示式
  $\omega_{wp}=\sum_{i=1}^k d\ell_{\alpha_i}\wedge d\tau_{\alpha_i}.$
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`surface$\textstyle S=\bigcup…$such that$A_i=\partial S_i\subset\partial S$, we have`、
    `where$L_{A_i}=(L_s)_{s\in A_i}$.`、`closed 2-form$\omega\in\Omega^2(M)$.`、`volume form on M.`、
    `the space$\mathcal{T}_{g,n}(L_1,\ldots,L_n)$carries`、`denoted by$\omega$or$\omega_{wp}$.`、
    `surface$X\in\mathcal{T}_{g,n}(L)$, the Fenchel-Nielsen coordinates`、`where$k=3g-3+n$.` 等），
    纯排版伪影，按 SOP 保留。
  - MD L304 把 FN 坐标元组拆成两个数学源片段（`…τ_{\alpha_1}(X)` ‖ `\dots,τ_{\alpha_k}(X)\}`），
    渲染结果与原页同一集合，不改。
  - MD L295 用 `\dots`（其余各处用 `\ldots`），渲染相同，不改。
  - 页眉/页码未收录（全篇通例）。
- **字形/定界符仲裁（本人 150dpi 初读有误，以 300dpi 原图为准，未据初读改稿）**：
  - 150dpi 下我把 `the space $\mathcal{T}_{g,n}(L_1,\ldots,L_n)$` 的圆括号误读为花括号；
    300dpi 裁剪（/tmp/mirzakhanipub_p009_Tbraces_300crop.png）直证原页印的是**圆括号**，
    与文本层一致，MD L298 `( L_1 , \ldots , L_n )` **正确**。
  - 150dpi 下我一度怀疑 $\mathcal{P}$ 的定义写作 $\{[\alpha_i]\}$（带方括号）；300dpi 裁剪
    （/tmp/mirzakhanipub_p009_Pset_300crop.png）直证原页**只有** `\{\alpha_i\}`、**无方括号**
    （对比 p.5 原页确实用 $[\gamma]$），MD L304 正确。
  - 300dpi 裁剪 /tmp/mirzakhanipub_p009_Rsup_300crop.png 直证两处上标是**花体 $\mathcal{P}$**（非 k、非 p），
    MD L307 `^ {\mathcal {P}}` 两处正确；$\mathbb{R}$ 为黑板粗体亦正确。
  - 300dpi 裁剪 /tmp/mirzakhanipub_p009_omega2M_300crop.png 直证 $\omega\in\Omega^2(M)$ 中 $\omega$ **无附加点**，
    MD L292 正确；/tmp/mirzakhanipub_p009_omegawp_300crop.png 直证 $\omega_{wp}$ 式中两个 $d$ 均为数学斜体、
    $\ell$ 与 $\tau$ 均带下标 $\alpha_i$、式末有句点，MD L321 逐项吻合。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 曾在 p.009 做两处修复——去掉 $\omega\in\Omega^2(M)$
  中的伪附加点、把 $\bar k=3g-3+\bar n$ 改回 $k=3g-3+n$；本轮 300dpi 双裁片复核确认两处修复**均正确**且当前 MD
  保持该状态（`caed1c35…`），**非回归**。
- 备注：本页覆盖 MD L284–L322（页末为 Theorem 2.1 的 $\omega_{wp}$ 展示式）；
  `Hamiltonian circle actions.` 起属 p.10。

## p.010（PDF p.10 / 印刷 p.188）
- PNG：/tmp/mirzakhanipub_audit_p010.png（pngmono 150dpi，gs -r150 -dFirstPage=10 -dLastPage=10）；
  仲裁裁剪：/tmp/mirzakhanipub_p010_Mglyph_300crop.png（`Let (𝓜, ω) … manifold (𝓜, ω).`）、
  /tmp/mirzakhanipub_p010_Hline_300crop.png（`H : 𝓜 → ℝ, the vector field X_H`）、
  /tmp/mirzakhanipub_p010_semic_300crop.png（`on 𝓜; in this case, ψ₁ = id`）
- 核对：页眉 `188 / M. Mirzakhani`；`Hamiltonian circle actions.` 段（$(𝓜,\omega)$ 两处、$H:𝓜→ℝ$、
  $\omega(X_H,\cdot)=dH(\cdot)$、`Hamiltonian vector field`、$\psi_t$、$S^1$ action on $𝓜$、
  $\psi_1=\mathrm{id}$、moment map、[McD]）；展示式 $\omega(X_H,\cdot)=dH(\cdot).$；
  `Twisting.` 段全句（$\alpha$、$X\in\mathcal{T}_{g,n}(L)$、$t\in\mathbb{R}$、$\mathrm{tw}^t_\alpha(X)$、
  Fenchel-Nielsen deformation、$t=\ell_\alpha(X)$）；展示式 $\mathrm{tw}^t_\alpha(X)=\phi_\alpha(X),$；
  `where φ_α ∈ Mod(S_{g,n}) is a right Dehn twist about α.`；`By Wolpert's result (Theorem 2.1) …` 段
  （$d\ell_\alpha$、Hamiltonian flow）；`Splitting along a multicurve.` 段
  （$\gamma=\textstyle\sum_{i=1}^k c_i\gamma_i$、$\gamma_i$'s、$c_i\geq0$、$1\leq i\leq k$、Fig. 1 与
  `![](images/page_9_image_8.jpg)`、$S_{g,n}(\gamma)$、$n+2k$、$s=s(\gamma)$）；页末 `Each`
- 结果：**FAIL**（已修，以原图为准）。
- 差异（5 处，均已用 Edit 逐处修复，证据 = 300dpi 裁剪 + pdftotext 文本层双证）：
  1. **MD L324**：原页两处 `Let (𝓜, ω) be a symplectic manifold (𝓜, ω).` 中的 $\mathcal{M}$
     被拍平成平文 `M`（/tmp/mirzakhanipub_p010_Mglyph_300crop.png 直证 300dpi 下为**花体 𝓜**，
     文本层无法区分）→ 改 `$(\mathcal{M},\omega)$` 两处；
  2. **MD L324**：原页 `manifold (𝓜, ω).` 句末**有句点**（文本层 `ω).` 与裁剪均可见），MinerU 丢失
     → 在第二个 `$(\mathcal{M},\omega)$` 后补 `.`；
  3. **MD L324**：`$H : M \to \mathbb{R}$` 的定义域 M 被拍平 → 改 `$H : \mathcal{M} \to \mathbb{R}$`
     （/tmp/mirzakhanipub_p010_Hline_300crop.png 直证）；
  4. **MD L330**：`action on$M ;;` 三处错误——定义域被拍平为 `M`、且分号**重复**为 `;;`
     （原页为单分号，/tmp/mirzakhanipub_p010_semic_300crop.png 直证 `on 𝓜; in this case, ψ₁ = id`，
     文本层亦为单 `M;`）→ 改 `on$\mathcal{M}$;`；
  5. **MD L330**：两处**词内粘连**——`Hamiltonian vectorfield`（原页为 `vector field` 两词，
     bbox 实测 `vector` x76.58–103.51 与 `field` x105.26–124.64 为两个独立 word）与
     `the integral ofthe vector field`（原页 `of the` 分写，bbox 实测 `of` / `the` 为两个 word）
     → 分别改为 `vector field` 与 `integral of the`。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`Let$…$be a symplectic`、`function$H : 𝓜→ℝ$, the vector field$X_H$determined by`、
    `vector field$X_H$. Here`、`case where$X_H$generates`、`geodesic α on$X\in\mathcal{T}_{g,n}(L)$and$t\in\mathbb{R}$`、
    `new surface by$\mathrm{tw}^t_\alpha(X)$.`、`is symplectically dual … form$d\ell_\alpha$.` 等），全篇通例。
  - 平文字符 X、α、t 未加数学斜体标记，字形同原页，不误导。
  - 图 `![](images/page_9_image_8.jpg)` + `Fig. 1`：原页 Fig. 1 为一幅 multicurve 切割示意图
    （标注 $\beta_1,\beta_2,\beta_3,\beta_4,\alpha,\alpha^1,\alpha^2$），MD 以图片 + 图题形式对应，内容不缺。
    **登记但不在本轮修**：该 jpg 实际位于
    `Mirzakhani_2007_simple_geodesics_published_mineru/Mirzakhani_2007_simple_geodesics_published/images/page_9_image_8.jpg`，
    而 MD 内引用为相对路径 `images/page_9_image_8.jpg`；这是 MinerU 套件目录层级与 MD 所在层级的**布局约定问题**，
    非本页内容缺陷，且修它需移动目录，超出本轮「只许改 Markdown 一个文件」的硬约束，交由集成者裁定。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本次判定为缺陷的 5 处均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。证据：
  `git cat-file -e d351abbff^:"2014年 - Mirzakhani/…__Mirzakhani_2007_simple_geodesics_published.md"` 返回
  `exists on disk, but not in 'd351abbff^'` —— 该 MD 文件**由 commit `d351abbff`（`mineru: 入库重试批次产出的 24 个导出…Mirzakhani×2…`）首次创建**；
  且 `git log -S "is called the Hamiltonian vectorfield" -- <md path>` 只命中 `d351abbff` 一个提交，
  父提交 `cf7…`（本轮基线 `cpf-redo/…^` = `7cf8cc12`）中 L324/L330 文本与修复前**逐字相同**
  （已 `git show cpf-redo/Mirzakhani_2007_simple_geodesics_published^:"…md"` 取出比对确认）。
  故不存在「后被某 peer 改坏」的回归情形，无需写「非导出缺陷」；原导出即不正确，本轮按原页修复。
- 备注：本页覆盖 MD L324–L348 前半（页末断在 `Each`）；`connected component γ_i of γ gives rise to 2 boundary components…`
  与 $\partial(S_{g,n}(\gamma))=\{\beta_1,\dots,\beta_n\}\cup\{\gamma_1^1,\gamma_1^2,\dots,\gamma_k^1,\gamma_k^2\}$
  及 (2.1) 起属 p.11。

## p.011（PDF p.11 / 印刷 p.189）
- PNG：/tmp/mirzakhanipub_audit_p011.png（pngmono 150dpi，gs -r150 -dFirstPage=11 -dLastPage=11）；
  仲裁裁剪：/tmp/mirzakhanipub_p011_Sgn_comma_300crop.png（`on S_{g,n},` 的标点）、
  /tmp/mirzakhanipub_p011_gamma_comma_300crop.png（`group of γ,` 的标点）、
  /tmp/mirzakhanipub_p011_Stab_300crop.png（Stab(A) 展示式内 Mod 字重）、
  /tmp/mirzakhanipub_p011_lastperiod_300crop.png（页末句号）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 189`；跨页承接句
  `connected component γ_i of γ gives rise to 2 boundary components, γ_i^1 and γ_i^2 on S_{g,n}(γ), and we have`；
  展示式 $\partial(S_{g,n}(\gamma))=\{\beta_1,\ldots,\beta_n\}\cup\{\gamma_1^1,\gamma_1^2,\ldots,\gamma_k^1,\gamma_k^2\}$；
  `Given Γ = (γ_1,…,γ_k), L = (L_1,…,L_n) and x = (x_1,…,x_k) ∈ ℝ_+^k`（$\mathbf{x}$ 粗体、$\boldsymbol{\Gamma}$ 粗体）与
  展示式 $\mathcal{M}(S_{g,n}(\gamma),\ell_\Gamma=\mathbf{x},\ell_\beta=L)$；
  `…such that ℓ_{γ_i} = x_i and ℓ_{β_i} = L_i. Also, we define V_{g,n}(Γ, x, β, L) by` 与展示式
  $V_{g,n}(\Gamma,\mathbf{x},\beta,L)=\mathrm{Vol}(\mathcal{M}(S_{g,n}(\gamma),\ell_\Gamma=\mathbf{x},\ell_\beta=L)).$；
  `The surface S_{g,n}(γ) can be written as a union of its connected components` 与展示式 (2.1)
  $S_{g,n}(\gamma)=\bigcup_{i=1}^s S_{g_i,n_i},\ A_i=\partial S_i\subset\mathcal{B},$（编号 (2.1)、$\mathcal{B}$ 花体）；
  `and we have` 与展示式 $\mathcal{M}(\cdots)\cong\prod_{i=1}^s\mathcal{M}_{g_i,n_i}(\ell_{A_i}).$；
  `where ℓ_{A_i} = (ℓ_α)_{α∈A_i}. Hence we get` 与展示式 $V_{g,n}(\Gamma,\mathbf{x},\beta,L)=\prod_{i=1}^s V_{g_i,n_i}(\ell_{A_i}).$；
  `Symmetry group of a multicurve.` 段与 `Stab(A) is defined by`；展示式
  $\mathrm{Stab}(A)=\{h\in\mathrm{Mod}_{g,n}\mid h\cdot A=A\}\subset\mathrm{Mod}_{g,n}.$（两处 Mod、$\cdot$、$\subset$）；
  `Given a multicurve γ = Σ c_i γ_i … Sym(γ), by` 与展示式
  $\mathrm{Sym}(\gamma)=\mathrm{Stab}(\gamma)/\bigcap_{i=1}^k\mathrm{Stab}(\gamma_i).$（$\bigcap$ 求交号与上下限）；
  `If α is a connected simple closed curve, then |Sym(α)| = 1. If α = γ_1 ∪ γ_2 then` 与展示式
  $|\mathrm{Sym}(\gamma_1+\gamma_2)|=2$；页末 `if and only if S_{g,n}(γ_1) is homeomorphic to S_{g,n}(γ_2).
  Here we consider the homeomorphisms which fix each boundary component of ∂(S_{g,n}) setwise, and send γ_1 to γ_2.`
- 结果：**FAIL**（3 处已修，以原图为准）。
- 差异（3 处，均已用 Edit 逐处修复，证据 = 300dpi 裁剪 + `pdftotext -bbox` 分词坐标双证）：
  1. **MD L390**：`we define the symmetry group of$\gamma .$` —— 原页在 $\gamma$ 后是**逗号**
     （/tmp/mirzakhanipub_p011_gamma_comma_300crop.png 直证 `…group of γ,`，bbox 标点 token
     x384.98–387.71 宽度 2.74pt 且带下伸尾，与同页 `Sg,n ,` 的逗号同形），MinerU 误置**句点**
     → 改 `of$\gamma$,`；
  2. **MD L396**：`…= 1 . \mathrm { I f } \alpha = \gamma_1 \cup \gamma_2$ then` —— 原页散文为单词
     `If`（文本层 `If α = γ1 ∪ γ2 then`），MinerU 拍成 `\mathrm { I f }`（渲染成错误的「I f」）
     且把句点吞进数学模式（`1 .`）→ 改 `= 1$. If $\alpha = \gamma_1 \cup \gamma_2$ then`；
  3. **MD L402**：页末句 `…and send$\gamma _ { 2 }$` **缺句末句点**（原页有，
     /tmp/mirzakhanipub_p011_lastperiod_300crop.png 直证 `…to γ_2 .`，bbox 亦有独立标点 token
     x136.46–139.19）→ 补 `.`。
- **字形/标点仲裁（本人 150dpi 初读有误，以 300dpi 原图为准，未据初读改稿）**：
  150dpi 下我把 `For a given set A of homotopy classes … on $S_{g,n}$. Stab(A) is defined by`
  的标点读作**句点**，300dpi 裁剪（/tmp/mirzakhanipub_p011_Sgn_comma_300crop.png）直证是**逗号**
  （有下伸尾，非圆点），与文本层 `Sg,n ,` 一致；MD L384 本就写逗号，**正确，未改**。
  另 /tmp/mirzakhanipub_p011_Stab_300crop.png 直证 Stab(A) 展示式内两处 `Mod` 为**正体非粗体**，
  MD L387 `\operatorname{Mod}` 两处正确。
- **print quirk 忠实登记不改**：正文写 `If $\alpha=\gamma_1\cup\gamma_2$ then`，紧随的展示式却印作
  $|\mathrm{Sym}(\gamma_1+\gamma_2)|=2$——**并集 $\cup$ 与求和 $+$ 不一致**，系印刷原文自身前后不统一。
  MD L396 用 `\cup`、L399 用 `+`，与印刷逐处对应，**不按数学常识统一**。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`components$\gamma_i^1$and $\gamma_i^2$on`、`we consider the moduli space`、
    `homeomorphic to$S_{g,n}(\gamma)$such that`、`Also, we define$V_{g,n}(\Gamma,\mathbf{x},\beta,L)$by`、
    `curve$|\mathrm{Sym}(\alpha)|=1$.` 等），全篇通例。
  - MD L390 用 `\begin{array}{r}{…}\end{array}` 包一个简单公式、L360 用 `{\bf x}` 而 L363/L375/L381 用
    `\mathbf{x}`——渲染等价，仅源码风格不一，不改。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 3 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `group of$\gamma .$`、`\mathrm { I f }`、`setwise, and send$\gamma _ { 1 }$to$\gamma _ { 2 }$`
  三个字符串各自只命中 `d351abbff`（`mineru: 入库重试批次产出的 24 个导出…Mirzakhani×2…`）一个提交，
  该提交即本MD 的首次入库（`git cat-file -e d351abbff^:<md path>` 报 `exists on disk, but not in`）。
  原导出即不正确，本轮按原页修复，不存在「非导出缺陷」情形。
- 备注：本页覆盖 MD L348 后半–L402；`We remark that the condition |Sym(γ)| ≠ 1 …` 起属 p.12。

## p.012（PDF p.12 / 印刷 p.190）
- PNG：/tmp/mirzakhanipub_audit_p012.png（pngmono 150dpi，gs -r150 -dFirstPage=12 -dLastPage=12）；
  仲裁裁剪：/tmp/mirzakhanipub_p012_symk_300crop.png（`|Sym(γ)|=k!` 横线核验）、
  /tmp/mirzakhanipub_p012_where_300crop.png（`where f : ℝ → ℝ₊.` 句点）、
  /tmp/mirzakhanipub_p012_pants_300crop.png（`homeomorphic to S_{0,3},` 逗号）、
  /tmp/mirzakhanipub_p012_chi_300crop.png（$\chi_{[0,L)}$ 下标）
- 核对：页眉 `190 / M. Mirzakhani`；`We remark that the condition…` 段（$|\mathrm{Sym}(\gamma)|\neq 1$、
  $\gamma=\textstyle\sum_{i=1}^k c_i\gamma_i$、$c_i$'s、$|\mathrm{Sym}(\gamma)|=k!$、$c_1=c_2=\ldots=c_k$）；
  `In this paper, we are mostly interested…` 段与展示式 $S_{g,n}(\gamma)\cong S_{g_1,1}\cup S_{g_1,1}.$（两个下标均为 $g_1$）；
  `Simple closed curves on $X\in\mathcal{M}_{g,n}$.` 小节首段（$[\gamma]$、corresponding to $[\gamma]$）；
  展示式 $\mathcal{O}_\gamma=\{[\alpha]\mid\alpha\in\mathrm{Mod}\cdot\gamma\},$；`…the $\mathrm{Mod}_{g,n}$-orbit of γ on X, is determined by γ…`
  整段（$[\phi(\gamma)]$、$\phi:S_{g,n}\to X$、$\ell_\alpha(X)$）；两行展示式
  $f_\gamma:\mathcal{M}_{g,n}\to\mathbb{R}_+$ / $X\to\sum_{\alpha\in\mathcal{O}_\gamma}f(\ell_\alpha(X)),$；
  `where f : ℝ → ℝ₊.`；`As an example, for f = χ_[0,L), …` 段；
  `3. Geometry of pairs of pants` 节标题；`In this section we study infinite simple geodesic rays…` 段与 [Bus]；
  `A pair of pants is an oriented compact surface homeomorphic to S_{0,3}, …` 句；
  `Let 𝔠(x_1,x_2,x_3) be the unique hyperbolic pair of pants…` 段（$(\beta_i)_{i=1}^3$、$\ell_{\beta_i}(\mathfrak{C})=x_i$、`i = 1, 2, 3`、
  degenerate case）；`There are two canonical points…` 段；`On the other hand, we can construct…` 段
  （right angled geodesic hexagons、pairwise non-adjacent、$x_1/2, x_2/2$、$x_3/2$、reflection involution $\sigma$）；页末 `…the two hexagons.`
- 结果：**FAIL**（4 处已修，以原图为准）。
- 差异（4 处，均已用 Edit 逐处修复，证据 = 300dpi 裁剪 + `pdftotext` 文本层/bbox 双证）：
  1. **MD L404**：`if$| \operatorname { S y m } ( { \overline { { \gamma ) } } } | = k !$` —— 原页
     $|\mathrm{Sym}(\gamma)|=k!$ **无任何横线**（/tmp/mirzakhanipub_p012_symk_300crop.png 直证
     `…ple if |Sym(γ)| = k! then c_1 =`；同一行句首的 $|\mathrm{Sym}(\gamma)|\neq 1$ 在 MD 中本就无横线，
     自相矛盾可证系 MinerU 伪横线）→ 删除 `\overline`，改 `(\gamma)`；
  2. **MD L424**：`where$f : \mathbb { R } \to \mathbb { R } _ { + }$` **缺句末句点**（原页有，
     /tmp/mirzakhanipub_p012_where_300crop.png 直证 `where $f : ℝ → ℝ_+$.`，文本层亦有独立 `.`）→ 补 `.`；
  3. **MD L432**：两处错误——(a) `A pair ofpants` **词内粘连**，原页为 `A pair of *pants*`
     （bbox `pants` 独立成词、文本层 `A pair of pants`）；(b) 原页 `homeomorphic to $S_{0,3}$**、**` **有逗号**
     （/tmp/mirzakhanipub_p012_pants_300crop.png 直证 `…homeomorphic to $S_{0,3}$,`，文本层同）而 MD 丢失
     → 改为 `A pair of pants is an oriented compact surface homeomorphic to$S _ { 0 , 3 }$, a surface of genus 0 with three boundary components.`;
  4. **MD L426**：两处错误——(a) $f=\chi_{[0,L)}$ 的 `[0,L)` 是 $\chi$ 的**下标**
     （/tmp/mirzakhanipub_p012_chi_300crop.png 直证 `[0,L)` 明显下沉且字号更小），MD 写作
     `\chi [ 0 , L )` 把下标拍平为正文 → 改 `\chi_{ [ 0 , L ) }`；(b) 原页
     `the characteristic function of $[0,L)$**,** $f_\gamma(X)$` **有逗号**，MD 写成 `$ $` 空数学段致逗号丢失
     → 补 `,`。
- **print quirk 忠实登记不改**：展示式 $S_{g,n}(\gamma)\cong S_{g_1,1}\cup S_{g_1,1}$ 中**两片的下标都是 $g_1$**
  （按理第二片应为 $g-g_1$），系印刷原文如此；MD L409 逐字保留 `S _ {g _ {1}, 1} \cup S _ {g _ {1}, 1}`，**不按数学常识改写**。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`condition$|\mathrm{Sym}(\gamma)|\neq 1$for`、`$c_i\gamma_i$imposes`、
    `condition on the$c_i^{\prime}\mathbf{s};$for example`、`where$\gamma=\gamma_1+\gamma_2$bounds`、
    `$|\mathrm{Sym}(\gamma_1+\gamma_2)|=2$if and only if`、`$S_{g,n}(\gamma)$is connected`、
    `curves on$X\in\mathcal{M}_{g,n}$.`、`denote the hyperbolic length of α on X.` 等），全篇通例。
  - MD L436 用 `\mathscr{C}` 而 L434/L438 用 `\mathcal{C}` 指同一个「裤」符号——**MinerU 自身字体不一致**，
    原页同一符号统一为花体 $\mathcal{C}$；属渲染风格不统一、不改变含义，不逐处改（登记供集成者统一处理）。
  - MD L412 把散文 `Let` 拍成 `\operatorname { L e t }`（渲染成「L e t」），与 p.10 的 `\mathrm { I f }` 同类，
    本页仅此一处且位于小节标题句首、不影响检索，登记不修。
  - 图 `![](images/page_12_image_0.jpg)` + `Fig. 2` 属 p.13 内容（见下页）；页眉/页码未收录。
- 溯源（本页 4 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `overline { { \gamma ) } }`、`A pair ofpants`、`\chi [ 0 , L )`、
  `where$f : \mathbb { R } \to \mathbb { R } _ { + }$` 四个字符串各自只命中 `d351abbff` 一个提交
  （该提交即本 MD 首次入库）。原导出即不正确，本轮按原页修复。
- 备注：本页覆盖 MD L404–L438（页末止于 `…the two hexagons.`）；`![](images/page_12_image_0.jpg)` 与 `Fig. 2`
  起属 p.13。**移交下一段**：全篇另有一处 `ofpants` 粘连在 MD L584（`Embedded pairs ofpants.`）。
  **更正（2026-10-05，p.016 审计时）**：本条移交说明有误——L584 **就在本段 PDF p.9–16 范围之内**
  （对应 PDF p.16 / 印刷 p.194），并非「在本段范围外」。该处已于 p.016 审计中按原页证据修复为
  `Embedded pairs of pants.`，详见 p.016 条；本段收尾时全篇 `ofpants` 计数已为 0。

## p.013（PDF p.13 / 印刷 p.191）
- PNG：/tmp/mirzakhanipub_audit_p013.png（pngmono 150dpi，gs -r150 -dFirstPage=13 -dLastPage=13）；
  仲裁裁剪：/tmp/mirzakhanipub_p013_sigmay2_300crop.png（$\sigma(y_1)=y_2$ 后的句点）、
  /tmp/mirzakhanipub_p013_liftCH_300crop.png（$\mathcal{C}$）、/tmp/mirzakhanipub_p013_H_300crop.png（$\mathbb{H}$）、
  /tmp/mirzakhanipub_p013_So_300crop.png（`So` 与 $\beta_1.$）、/tmp/mirzakhanipub_p013_Hformula_300crop.png（$H$ 的指数结构）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 191`；`![](images/page_12_image_0.jpg)` + `Fig. 2`
  （图内标注 $w_2,y_2,x_2,\beta_1,y_1,x_1,w_1,\beta_3,\beta_2$）；`Complete geodesics on hyperbolic a pair of pants.` 段
  （5、$\beta_2,\beta_3$、$\beta_1$、$y_1,y_2$、$\beta_3$、$z_1,z_2$、$\beta_2$、$w_1,w_2$、
  $\sigma(w_1)=w_2,\sigma(z_1)=z_2,\sigma(y_1)=y_2$、See Fig. 2.）；`Definitions.` 段（$\mathcal{R}(x_1,x_2,x_3)$、
  $(y_1,y_2)$、$\beta_1$、$w_1,w_2$、universal cover of $\mathcal{C}(x_1,x_2,x_3)$）；展示式
  $x_1-\mathcal{R}(x_1,x_2,x_3)$；`is equal to … projection of β₃ on β₁. See Fig. 3. … lift of 𝔠 in ℍ.`；
  `Also, define 𝔇(x_1,x_2,x_3)…` 段（$(y_1,z_1)$、$(y_2,z_2)$、$(y_i,z_i)$、$w_i$、$\beta_1$、`So`、twice the geodesic distance、
  $\beta_2$ and $\beta_3$、universal cover of $\mathfrak{C}$、equals 2 times…on $\beta_1$）；
  `Define the function $H:\mathbb{R}^2\to\mathbb{R}$ by` 与展示式
  $H(x,y)=\frac{1}{1+e^{\frac{x+y}{2}}}+\frac{1}{1+e^{\frac{x-y}{2}}}.$（页末最后一行内容）
- 结果：**FAIL**（4 处已修，以原图为准）。
- 差异（4 处，均已用 Edit 逐处修复，证据 = 300dpi 裁剪 + `pdftotext -bbox` 分词坐标双证）：
  1. **MD L444**：`and$\sigma ( y _ { 1 } ) = y _ { 2 }$ See Fig. 2.` —— 原页在 $y_2$ 后**有句点**
     （/tmp/mirzakhanipub_p013_sigmay2_300crop.png 直证 `and σ(y₁) = y₂ .`；bbox 亦有独立标点 token
     x384.86–387.59, y333.13–343.16），MinerU 丢失 → 补 `.`；
  2. **MD L452**：`the choice of the lift of C in H.` —— 原页为**花体 $\mathcal{C}$** 与
     **黑板粗体 $\mathbb{H}$**（/tmp/mirzakhanipub_p013_liftCH_300crop.png 直证 `the lift of 𝔠`，
     /tmp/mirzakhanipub_p013_H_300crop.png 直证 `in ℍ.` 为双线 H），MinerU 双双拍平为平文
     → 改 `lift of$\mathcal{C}$in$\mathbb{H}$`；
  3. **MD L454**：`on$\beta _ { 1 } . S 0$the function` —— 原页 `on $\beta_1$**.** **So** the function`
     （/tmp/mirzakhanipub_p013_So_300crop.png 直证 `β₁. So the function 𝔇(x₁,x₂,x₃)`，`So` 为字母 S + 字母 o；
     bbox `So` 为 x90.85–102.45 的独立 word，文本层亦作 `So`），MinerU 既把句点吞进数学模式、
     又把 `So` 误识成 `S 0`（字母 S + 数字 0）→ 改为 `on$\beta _ { 1 }$. So the function`；
  4. **MD L454**：段末 `…on$\beta _ { 1 }$` **缺句末句点**（原页有，文本层 `on β1 .` 与上一裁片同一行直证）
     → 补 `.`。
- **指数结构仲裁（文本层误读纠正，MD 正确，未改）**：`pdftotext -f 13 -l 13` 把 $H$ 的指数抽成扁平的
  `1+e x+y 2`，易误读为 $e^{x+y}/2$。300dpi 裁剪（/tmp/mirzakhanipub_p013_Hformula_300crop.png）直证分数线、
  分子 $x\pm y$、分母 $2$ **整体处于 $e$ 的上标位置**，即 $e^{\frac{x+y}{2}}$ 与 $e^{\frac{x-y}{2}}$；
  bbox 亦显示 `x+y` 的 yMin 599.03 远高于主行基线而 `2` 的 yMin 605.39 更低（分数下标）。
  MD L459 `\frac {1}{1 + e ^ {\frac {x + y}{2}}} + \frac {1}{1 + e ^ {\frac {x - y}{2}}}.` 逐项吻合，**无需改动**。
- **print quirk 忠实登记不改**：小节标题印作 `Complete geodesics on hyperbolic **a** pair of pants.`
  ——`hyperbolic` 与 `a pair` 之间多一个冠词 `a`，系印刷原文如此；MD L444 原样保留，**不按英文正字法删改**。
  同段 `There is also a unique common geodesic perpendicular **from** $\beta_1$ **to itself** meeting
  $\beta_1$ perpendicularly at two points` 措辞亦属原文（如实保留，不改）。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`contains$5$complete`、`disjoint from$\beta_2,\beta_3$and`、
    `meet$\beta_1$respectively at$y_1$`、`at$z_1$and$z_2$and spiral`、`perpendicular from$\beta_1$to itself`、
    `Define$\mathcal{R}(x_1,x_2,x_3)$to be`、`length of$(y_1,y_2)$, the interval`、`Define$\mathcal{D}(x_1,x_2,x_3)$to be`、
    `Define the function$H:\mathbb{R}^2\to\mathbb{R}$by` 等），全篇通例。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 4 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `= y _ { 2 }$ See Fig. 2.`、`lift of C in H.`、`S 0$the function` 三个字符串各自只命中 `d351abbff`
  （本 MD 首次入库提交）。原导出即不正确，本轮按原页修复。
- 历史核验：Peer-P11 曾在 p.013 补回 `H:\mathbb{R}^2\to\mathbb{R}` 中丢失的 `\to`；当前 MD L456
  `\to` 在位且与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L440–L460（页末为 $H(x,y)$ 展示式）；`![](images/page_13_image_0.jpg)` 与
  `Basic properties of 𝔇 and ℛ.`（MD L462–L464）起属 p.14。

## p.014（PDF p.14 / 印刷 p.192）
- PNG：/tmp/mirzakhanipub_audit_p014.png（pngmono 150dpi，gs -r150 -dFirstPage=14 -dLastPage=14）；
  仲裁裁剪：/tmp/mirzakhanipub_p014_basicDR_300crop.png（小节标题的 𝔇/ℛ 字形）、
  /tmp/mirzakhanipub_p014_lemmaDR_300crop.png（Lemma 3.1 陈述句的 𝔇/ℛ 字形）
- 核对：页眉 `192 / M. Mirzakhani`；`![](images/page_13_image_0.jpg)` + `Fig. 3`（图内标注 $p_2,p_3,p_1,\beta_1,r_3,\beta_3,r_2,r_1$）；
  `Basic properties of 𝔇 and ℛ.` 小节标题与其引导句（`It can be easily checked that the functions 𝔇 and ℛ satisfy`）；
  展示式 $\mathcal{D}(x_1,x_2,x_3)=\mathcal{D}(x_1,x_3,x_2),$；`and` 与展示式
  $\mathcal{R}(x_1,x_2,x_3)+\mathcal{R}(x_1,x_3,x_2)=x_1+\mathcal{D}(x_1,x_2,x_3).$；
  `Moreover, one can explicitly calculate these functions and show that:`；Lemma 3.1 陈述句；
  展示式 (3.1) $\mathcal{D}(x,y,z)=2\log\left(\frac{e^{x/2}+e^{(y+z)/2}}{e^{-x/2}+e^{(y+z)/2}}\right),$（编号 (3.1)）；
  `and` 与展示式 (3.2) $\mathcal{R}(x,y,z)=x-\log\left(\frac{\cosh(y/2)+\cosh((x+z)/2)}{\cosh(y/2)+\cosh((x-z)/2)}\right).$（编号 (3.2)）；
  `Proof.` 整段（$\mathcal{R}(x,y,z)$、Theorem 2.3.1 of [Bus]、three right angles、$a,b$、`infinity and infinity`、
  boundary at infinity）；展示式 $\mathrm{Sinh}(a)\cdot\mathrm{Sinh}(b)=1.$；
  `In Fig. 3, … for geodesic quadrilateral r₁ r₃ p₃ p₁, and r₂ r₃ p₃ p₂. Hence, we obtain` 与页末展示式
  $\mathcal{R}(x_1,x_2,x_3)=x_1-2\operatorname{arcsinh}\left(\frac{1}{\sinh(d(\beta_1,\beta_3))}\right)$
- 结果：**FAIL**（2 行共 4 处已修，以原图为准）。
- 差异（均已用 Edit 逐处修复）：
  1. **MD L464**：`Basic properties of D and$\mathcal { R }$.` —— 原页两处均为**花体**
     （/tmp/mirzakhanipub_p014_basicDR_300crop.png 直证 `…properties of 𝔇 and ℛ. It can be easily c…`），
     首个 `D` 被拍平为平文 → 改 `of$\mathcal{D}$and$\mathcal{R}$`；
  2. **MD L464**：`the functions $\mathcal { D }$and R satisfy` —— 同句句末的 `R` 原页亦为**花体 ℛ** → 改 `functions$\mathcal{D}$and$\mathcal{R}$satisfy`；
  3. **MD L478**：`Lemma 3.1. Thefunctions$\mathcal { D }$and R are given by` —— 两处错误：
     (a) `Thefunctions` **词内粘连**（原页 `The *functions*` 为两个词，bbox `functions` 为 x130.10–169.75 独立 word）；
     (b) `and R` 的 `R` 原页为**花体 ℛ**（/tmp/mirzakhanipub_p014_lemmaDR_300crop.png 直证
     `tions 𝔇 and ℛ a`）→ 改为 `The functions$\mathcal{D}$and$\mathcal{R}$are given by`。
- **公式仲裁（150dpi 初读有误，以 bbox + 300dpi 为准，MD 正确未改）**：
  - **展示式 (3.2)**：150dpi 下我把两处 $\cosh$ 的参数读成 `x/2` 与 `(x+y)/2`、`(x−y)/2`，
    但 `pdftotext -bbox` 实测：首个 $\cosh$ 的分子在 x237.855 为 **`y`**（分子 yMin 442.75 / 分母 `2` yMin 451.63），
    第二个 $\cosh$ 的分子为 **`x+z`**（yMin 443.35）与 **`x−z`**（yMin 460.03）——即
    $\frac{\cosh(\frac{y}{2})+\cosh(\frac{x+z}{2})}{\cosh(\frac{y}{2})+\cosh(\frac{x-z}{2})}$。
    **MD L487 原本即正确**（`\cosh\left(\frac{y}{2}\right)+\cosh\left(\frac{x+z}{2}\right)` /
    `\cosh\left(\frac{y}{2}\right)+\cosh\left(\frac{x-z}{2}\right)`），**未改动**，本人 150dpi 误读在此登记。
  - **展示式 (3.1)**：bbox 实测分子依次为 `x`+`2`、`y+z`+`2`，分母为 `−x`+`2`、`y+z`+`2`，
    与 MD L481 `$e^{x/2}+e^{(y+z)/2}\over e^{-x/2}+e^{(y+z)/2}$` 逐项吻合，正确。
  - **四边形顶点标注**：bbox 实测下标为 `r_1 r_3 p_3 p_1` 与 `r_2 r_3 p_3 p_2`
    （x325.46/336.98/349.94/363.98 与 x69.02/80.54/93.50…），MD L496 正确，未改动。
- **print quirk 忠实登记不改**：`Proof.` 段中印刷写作 `consecutive sides of lengths a, b, **infinity and infinity**
  (when one vertex is on the boundary at infinity)`——以英文单词 `infinity` 代替 $\infty$ 符号，系原文如此；
  MD L490 原样保留 `infinity and infinity`，**不替换为 $\infty$**。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`It can be easily checked…`、`calculate$\mathcal{R}(x,y,z)$.`、
    `equation for geodesic quadrilateral$r_1 r_3 p_3 p_1$and$r_2 r_3 p_3 p_2$.` 等），全篇通例。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 4 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `Basic properties of D and$\mathcal { R }$.` 与 `Thefunctions$\mathcal { D }$and R are` 两个字符串
  各自只命中 `d351abbff`（本 MD 首次入库提交）。原导出即不正确，本轮按原页修复。
- 备注：本页覆盖 MD L462–L500（页末为 $\mathcal{R}(x_1,x_2,x_3)=x_1-2\operatorname{arcsinh}(\cdots)$ 展示式）；
  `On the other hand, by cutting the pairs of pants along the shortest geodesics…` 起属 p.15。

## p.015（PDF p.15 / 印刷 p.193）
- PNG：/tmp/mirzakhanipub_audit_p015.png（pngmono 150dpi，gs -r150 -dFirstPage=15 -dLastPage=15）；
  仲裁裁剪：/tmp/mirzakhanipub_p015_D_300crop.png（`functions 𝔇`）、/tmp/mirzakhanipub_p015_R_300crop.png（`and ℛ:`）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 193`；`On the other hand, by cutting the pairs of pants…` 整段
  （六个连续边长 $x_1/2,\,d(\beta_1,\beta_2),\,x_2/2,\,d(\beta_2,\beta_3),\,x_3/2,\,d(\beta_3,\beta_1)$、uniquely determine、
  Therefore, we get）；展示式
  $\cosh(d(\beta_1,\beta_3))=\frac{\cosh(x_2/2)+\cosh(x_3/2)\cosh(x_1/2)}{\sinh(x_3/2)\sinh(x_1/2)}$；
  `See Sect. 2 of [Bus] for more details.`；`Finally, we have` 与两行展示式
  $2\operatorname{arcsinh}\left(\frac{1}{\sinh\alpha}\right)=2\log\left(\frac{1}{\sinh\alpha}+\frac{\cosh\alpha}{\sinh\alpha}\right)$
  $=\log\left(\frac{\cosh\alpha+1}{\cosh\alpha-1}\right).$；`Hence,` 与展示式
  $\mathcal{R}(x_1,x_2,x_3)=x_1-\log\left(\frac{\cosh(d(\beta_1,\beta_3))+1}{\cosh(d(\beta_1,\beta_3))-1}\right),$；
  `which implies equation (3.2).` + 右端 QED 方块；`See [LM] …` 句；`Next lemma … functions 𝔇 and ℛ:`；
  Lemma 3.2 陈述句（$\mathcal{D},\mathcal{R}:\mathbb{R}_+\to\mathbb{R}_+$、following equations:）；
  展示式 (3.3) $\frac{\partial}{\partial x}\mathcal{D}(x,y,z)=H(y+z,x),$；`and` 与展示式 (3.4)
  $\frac{\partial}{\partial x}\mathcal{R}(x,y,z)=\frac12(H(z,x+y)+H(z,x-y)).$；`Proof. Using equation (3.1), we have` 与展示式
  $\frac{\partial}{\partial x}\mathcal{D}(x,y,z)=\frac{e^{x/2}}{e^{x/2}+e^{(y+z)/2}}+\frac{e^{-x/2}}{e^{-x/2}+e^{(y+z)/2}}=H(y+z,x).$；
  `Using Lemma 3.1 one can show that` 与展示式 $\mathcal{D}(x,y,z)+\mathcal{D}(x,-y,z)=2\mathcal{R}(x,y,z).$；
  页末 `Therefore, equation (3.3) implies equation (3.4).` + QED 方块
- 结果：**FAIL**（1 处已修，以原图为准）。
- 差异（已用 Edit 修复）：**MD L526** `Next lemma will allow us to simplify integrals involving functions D and R:`
  —— 原页两处均为**花体**（/tmp/mirzakhanipub_p015_D_300crop.png 直证 `…ons 𝔇`，
  /tmp/mirzakhanipub_p015_R_300crop.png 直证下一行 `, ℛ:`；bbox 亦显示两字形 yMax 365.93 / 377.93
  略高于同行正文的 365.72 / 377.72，与数学花体字一致），MinerU 拍平为平文 `D` 与 `R`
  → 改为 `functions$\mathcal{D}$and$\mathcal{R}$:`。
- **未改动的伪影（PASS± 登记，不修）**：
  - 两处证明收尾的 **QED 方块（□）** 未收录：原页在 `which implies equation (3.2).` 与
    `Therefore, equation (3.3) implies equation (3.4).` 行末右端各有一个空心方块；MD 无对应标记。
    属装饰性证明结束符，不影响数学内容，按 SOP 不逐处补，登记在案。
  - 行内公式两侧空格合并（`lengths$x_1/2,\,d(\beta_1,\beta_2),\,x_2/2$ $d(\beta_2,\beta_3),\,x_3/2$and$d(\beta_3,\beta_1)$.`、
    `numbers$x_1,x_2$and$x_3$uniquely determine`、`which implies equation (3.2).` 等），全篇通例。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 1 处缺陷已溯源）：**为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S
  'involving functions D and R:'` 只命中 `d351abbff`（本 MD 首次入库提交）。原导出即不正确，本轮按原页修复。
- 历史核验：Peer-P11 曾在 p.015 做两处修复——「闭合分子中的 $\cosh(d(\beta_1,\beta_3))$ 后再 `+1`」与
  「补回函数类型中的 `\to`」。本轮复核：MD L519 的 $\frac{\cosh(d(\beta_1,\beta_3))+1}{\cosh(d(\beta_1,\beta_3))-1}$
  分子分母括号各自闭合无误；MD L528 的 `\mathbb{R}_+\to\mathbb{R}_+` 箭头在位。**两处旧修复均正确，非回归**。
- 备注：本页覆盖 MD L502–L552（页末为 `Therefore, equation (3.3) implies equation (3.4).`）；
  `Asymptotic behavior of 𝔇 and ℛ.`（MD L554）起属 p.16。

## p.016（PDF p.16 / 印刷 p.194）
- PNG：/tmp/mirzakhanipub_audit_p016.png（pngmono 150dpi，gs -r150 -dFirstPage=16 -dLastPage=16）；
  仲裁裁剪：/tmp/mirzakhanipub_p016_asymDR_300crop.png（小节标题与引导句的 𝔇/ℛ）、
  /tmp/mirzakhanipub_p016_ofpants_300crop.png（`pairs of pants.` 词界）、
  /tmp/mirzakhanipub_p016_bi1_300crop.png（`with β_i.` 句点）、
  /tmp/mirzakhanipub_p016_bij_300crop.png（`and β_j.` 句点）、
  /tmp/mirzakhanipub_p016_tau_300crop.png（`y, z → ∞` 的变量字形）
- 核对：页眉 `194 / M. Mirzakhani`；`Asymptotic behavior of 𝔇 and ℛ.` 整段
  （Functions 𝔇 and ℛ、$\mathbb{R}_+^3$、`0 < 𝔇(x,y,z) ≤ x`、`0 < ℛ(x,y,z) ≤ x`、both 𝔇 and ℛ go to zero when $x\to0$、
  Using Lemma 3.2）；展示式 (3.5) $\mathcal{D}(x,y,z)\sim x\,H(y+z,x)\sim\frac{2x}{1+e^{(y+z)/2}},$（编号 (3.5)）；
  展示式 (3.6) $\mathcal{R}(x,y,z)\sim x\left(\frac{1}{1+e^{(z+y)/2}}+\frac{1}{1+e^{(z-y)/2}}\right).$（编号 (3.6)）；
  `as x → 0.`；`Also, when x and y are fixed numbers, we have` 与 $\mathcal{R}(x,y,z)\to 0,$；
  `as z → ∞. Similarly, when x is a fixed number as` 与 $\mathcal{D}(x,y,z)\to 0,$；`y, z → ∞.`；
  `4. Generalized McShane identity for bordered surfaces` 节标题与其引导段；
  `Embedded pairs of pants.` 整段（$\alpha_1,\alpha_2,\alpha_3$、$S_{g,n}$、$\Sigma\subset S_{g,n}$、
  $\partial\Sigma=\{\alpha_1,\alpha_2,\alpha_3\}$、closed geodesic of length 0 is a cusp）；
  `The statement of Theorem 1.3 motivates…` 整段（$1\leq i\leq n$、$\mathcal{F}_i$、unordered、
  $\{\gamma_1,\gamma_2\}$、$\beta_i$.、$1\leq i\neq j\leq n$、$\mathcal{F}_{i,j}$、$\beta_i$ and $\beta_j$.）；
  `An identity for lengths of simple closed geodesics.` 段与 [M]；Theorem 4.1 陈述句
  （$\{p_1,\ldots,p_n\}$、$X\in\mathcal{T}_{g,n}$、Then we have）与页末展示式
  $\sum_{\{\gamma_1,\gamma_2\}\in\mathcal{F}_1}\frac{1}{1+e^{\frac{\ell_{\gamma_1}(X)+\ell_{\gamma_2}(X)}{2}}}+\sum_{i=2}^{n}\sum_{\gamma\in\mathcal{F}_{1,i}}\frac{1}{1+e^{\frac{\ell_\gamma(X)}{2}}}=\frac{1}{2}.$
- 结果：**FAIL**（4 行共 8 处已修，以原图为准）。
- 差异（均已用 Edit 逐处修复，证据 = 300dpi 裁剪 + `pdftotext -bbox` 分词坐标双证）：
  1. **MD L554**：小节标题与首句共 **4 处花体字被拍平**——原页 `Asymptotic behavior of 𝔇 and ℛ.`、
     `Functions 𝔇 and ℛ`、末句 `both 𝔇(x,y,z) and ℛ(x,y,z)` 中四处均为花体
     （/tmp/mirzakhanipub_p016_asymDR_300crop.png 直证
     `Asymptotic behavior of 𝔇 and ℛ. Functions 𝔇 and ℛ are continu…`），MinerU 仅保留了其中 2 处 $\mathcal{R}$
     而把 4 处平文化为 `D`/`R` → 全部改为 `\mathcal{D}` / `\mathcal{R}`；
  2. **MD L584**：`Embedded pairs ofpants.` —— **词内粘连**，原页为 `of *pants*` 两词
     （/tmp/mirzakhanipub_p016_ofpants_300crop.png 直证 `d pairs of pants. We say three isot…`；
     bbox `pants.` 为 x138.88–167.05 独立 word）→ 改 `of pants.`；
  3. **MD L584**：`isotopy classes ofconnected simple closed curves` —— **词内粘连**，原页 `of connected` 分写
     → 改 `of connected`；
  4. **MD L586**：两处**句末标点缺失**——原页 `…bounding a pair of pants with $\beta_i$**.** Similarly,`
     （/tmp/mirzakhanipub_p016_bi1_300crop.png 直证 `of pants with β_i .`）与段末
     `…containing $\beta_i$ and $\beta_j$**.**`（/tmp/mirzakhanipub_p016_bij_300crop.png 直证
     `pants containing β_i and β_j .`），MinerU 两处皆丢 → 各补 `.`。
- **字形仲裁（150dpi 初读有误，以 300dpi + bbox 为准，MD 正确未改）**：150dpi 下我把页末
  `y, τ → ∞` 的第二个变量读作 **τ（tau）**，一度疑为印刷把 `z` 误排成 `τ` 的 typo、准备按原页改回 τ。
  300dpi 裁剪（/tmp/mirzakhanipub_p016_tau_300crop.png）直证该字形为 **`z`**（平顶横画 + 斜下笔 + 底部衬线），
  且 bbox 度量与同页上一行 `as z → ∞` 的 `z` **完全一致**（均宽 4.26pt、高 9.90pt），
  文本层亦作 `y, z → ∞ .`。**原页无 typo，MD L578 `y, z → ∞.` 本就正确，未改动**；本人 150dpi 误读在此登记。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`continuous on$\mathbb{R}_+^3$.`、`both 𝔇(x,y,z) and ℛ(x,y,z)go to zero when$x\to0$.`、
    `let$\mathcal{F}_i$denote`、`curves$\{\gamma_1,\gamma_2\}$bounding`、`Similarly, for$1\leq i\neq j\leq n$, let`、
    `set of punctures of$X\in\mathcal{T}_{g,n}$.` 等），全篇通例。
  - 原页 `bound a pair of pants` 为**斜体强调**，MD 作平文（强调丢失，不误导），登记不修。
  - 原页 `$\Sigma\subset S_{g,n}$` 中 $\Sigma$ 为大写 Sigma（文本层 `Σ ⊂ Sg,n` 一致），MD `\Sigma` 正确。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 8 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `Asymptotic behavior of D and R. Functions D and`、`Embedded pairs ofpants.`、
  `classes ofconnected simple closed curves`、`pants with$\beta _ { i }$ Similarly.`、
  `containing$\beta _ { i }$and$\beta _ { j }$` 五个字符串各自只命中 `d351abbff`（本 MD 首次入库提交）。
  原导出即不正确，本轮按原页修复。
- 历史核验：Peer-P11 曾在 p.016 记录「去掉初始 `1` 上的伪横线」等修复；本轮未见该类伪影残留，
  L586 的 `$1 \leq i \neq j \leq n$` 首个 `1` 上**无**横线，与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L554–L594（页末为 Theorem 4.1 的展示式）；
  `We will use the properties of functions 𝔇, ℛ : ℝ₊³ → ℝ₊ …`（MD L596）与 Theorem 4.2 起属 p.17，
  不在本段范围。**本段（PDF p.9–16）到此结束**，共 8 页，全部已逐页落签。

---

# 独立重做审计（第二轮 redo，PDF p.017–p.024）

- 性质：独立第二轮重做审计，逐页重新渲染 PNG 亲眼目检，不沿用 `.redo.md`（Wf-R-P11）的既有结论；
  每条判定均以本人所看原页 PNG + `pdftotext -layout` 文本层 + `pdftotext -bbox` 分词坐标三通道对账为据。
- Actor: `Wf-R-P11b`；Host / model / effort: zcode / `opencode-go-chat-space-bunny-free` / effort 自报 UNKNOWN
- 日期：2026-10-05（第三段，承接 p.001–p.008、p.009–p.016 两段）
- 被检 Markdown 基线 SHA-256 = `f0cf319f2e6b2d0d73a36a6d9f213381b92dca5ec57f8237970413b1e603a88c`（1698 行）
  ——该值含前两段共 54 处已登记修复
- PDF SHA-256 = `c19a088d97b2b3223481341d059ef7836ea9f575f580d3bf574d0b475e7615cf`（44 页，未改动）
- 印刷页码换算：PDF p.N = 印刷 p.(178+N)。本段覆盖 PDF p.17–24 = 印刷 p.195–202。

## p.017（PDF p.17 / 印刷 p.195）
- PNG：/tmp/mirzakhanipub_audit_p017.png（pngmono 150dpi，gs -r150 -dFirstPage=17 -dLastPage=17）；
  仲裁裁剪：/tmp/mirzakhanipub_p017_eq42_300crop.png（公式 (4.2) 第二和式的两个指数）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 195`；`We will use the properties of functions 𝔇, ℛ : ℝ₊³ → ℝ₊, and the geometry…` 整段；
  Theorem 4.2 (Generalized McShane identity for bordered surfaces) 陈述句（$X\in\mathcal{T}_{g,n}(L_1,\ldots,L_n)$、$3g-3+n>0$）与展示式 (4.1)
  （编号 (4.1)、两个求和号、$\mathcal{D}(L_1,\ell_{\gamma_1}(X),\ell_{\gamma_2}(X))$、$\mathcal{R}(L_1,L_i,\ell_\gamma(X))$、$=L_1.$）；
  `We remark that as L₁ → 0 …` 整段；Corollary 4.3 陈述句（$\mathcal{T}_{g,n}(0,L_2,\ldots,L_n)$）与展示式 (4.2)
  （编号 (4.2)、首个指数 $\frac{\ell_{\gamma_1}(X)+\ell_{\gamma_2}(X)}{2}$、系数 $\frac12$ 与括号、两个指数、右端 $\frac12$）；
  `Note that Corollary 4.3 implies Theorem 4.1.`；`Remark.` 整段（[M]、[B]、hypersurfaces）；
  `Union of complete simple geodesics.` 整段（$E(X)\subset X$、perpendicularly、$E_i=E\cap\beta_i$、
  $x\in E_i$、$\gamma_x$、geodesic emanating from x、$x\in\gamma_x$、finite arc）；
  Lemma 4.4 陈述句（$E_i\subset\beta_i$、measure zero）；`Proof.` 整段（Birman and Series [BS]、Hausdorff dimension 1、
  Doubling、$\mu(E)=0$、$U_{\beta_i}$、$E\cap U_{\beta_i}$）；展示式 $\mu(E\cap U_{\beta_i})=\sinh r\times\mu(E_i),$；
  页末 `where r is the width of the collar neighborhood. So μ(E ∩ U_{β_i}) = 0 implies that μ(E_i) = 0.` + QED 方块
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`properties of functions$𝔇, ℛ:\mathbb{R}_+^3\to\mathbb{R}_+$, and`、
    `For any$X\in\mathcal{T}_{g,n}(L_1,\ldots,L_n)$with$3g-3+n>0$, we have`、
    `as$L_1\to 0$both sides`、`the union of all simple complete geodesics meeting… of X perpendicularly.`、
    `Let$E(X)\subset X$denote`、`Let$E_i=E\cap\beta_i$.`、`Given$x\in E_i$, let$\gamma_x$, the geodesic emanating from x, denote`、
    `perpendicular to$\beta_i$such that$x\in\gamma_x$.`、`Note that$\gamma_x$may be a finite arc`、
    `The set$E_i\subset\beta_i$, defined as above,`、`That is$\mu(E)=0$.`、`Let$U_{\beta_i}$denote`、
    `the set$E\cap U_{\beta_i}$has measure zero.`、`where r is the width`、
    `So$\mu(E\cap U_{\beta_i})=0$implies that$\mu(E_i)=0$` 等），全篇通例。
  - 证明收尾的 **QED 方块（□）** 未收录（与 p.15 同类，见该页登记），属装饰性结束符，不影响数学内容，不补。
  - 页眉/页码未收录（全篇通例）。
- **公式仲裁（150dpi 初读有误，以 300dpi + bbox 为准，MD 正确未改）**：展示式 (4.2) 第二个和式的两个指数，
  150dpi 下我读作 $\frac{\ell_{\gamma_1}(X)+L_i}{2}$ 与 $\frac{\ell_{\gamma_2}(X)-L_i}{2}$（下标 1/2），
  疑 MD 漏标下标。300dpi 裁剪（/tmp/mirzakhanipub_p017_eq42_300crop.png）直证两处均为**单下标 $\ell_\gamma$**
  （`ℓ_γ(X)+L_i` 与 `ℓ_γ(X)−L_i`，无 1/2 下标），第二项为**减号**；`pdftotext -bbox` 亦显示两处 `γ` 各宽 3.56pt
  （x258.50、x325.22）且其后直接接 `(X`，与带下标的写法度量不同。
  **MD L609 本就正确**（`\frac {\ell_ {\gamma} (X) + L _ {i}}{2}` 与 `\frac {\ell_ {\gamma} (X) - L _ {i}}{2}`），
  **未改动**；本人 150dpi 误读在此登记。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 的 p.017 不在其修复登记表内，
  本轮亦未见其引入的新伪影；本段起始基线 `f0cf319f…` 含前两段修复，未在本页产生连带影响。
- 备注：本页覆盖 MD L596–L626（页末为 Lemma 4.4 证明收尾）；`Later we show that [M]:`（MD L628）起属 p.18。

## p.018（PDF p.18 / 印刷 p.196）
- PNG：/tmp/mirzakhanipub_audit_p018.png（pngmono 150dpi，gs -r150 -dFirstPage=18 -dLastPage=18）；
  仲裁裁剪：/tmp/mirzakhanipub_p018_gammaperiod_300crop.png（`the closure of γ .` 句点）
- 核对：页眉 `196 / M. Mirzakhani`；`Later we show that [M]:`；Theorem 4.5 陈述句
  （$E_i$、Cantor set union countably many isolated points）；
  `Characterization of boundary and isolated points in $E_i$.` 小节首段全句
  （`spirals to a lamination`、$\Omega(\gamma)$、iff、in the closure of $\gamma$、when $\gamma$ is a ray、
  minimal lamination [CEG]、$x\in E_i$、$\gamma_x$、exactly one of the following two classes）；
  编号条目 1（compact minimal lamination、denoted by $\Omega(\gamma_x)$）与 2
  （$\beta_i$、$\gamma_x$ meets $\beta_i$ perpendicularly or spirals around it.）；
  `We will prove the following classification … [M]:`；Theorem 4.6 陈述句与 a)/b)/c) 三条
  （$\Omega(\gamma_x)$、simple closed curve、boundary point、isolated point、neither … nor …）；
  `Simple arcs in embedded pairs of pants.` 小节首段（one-to-one、$\beta_1$ and $\beta_j$ of $X$）；
  `As shown in Fig. 4, if γ is a simple arc … Conversely, if Σ is a pair of pants …` 段；
  图 `![](images/page_17_image_12.jpg)` + `![](images/page_17_image_13.jpg)` + `Fig. 4`（两幅裤子剖面示意图）
- 结果：**FAIL**（3 处已修，以原图为准）。
- 差异（3 处，均为**句末标点缺失**，已用 Edit 逐处修复，证据 = 300dpi 裁剪 + `pdftotext` 文本层双证）：
  1. **MD L632**：`…is in the closure of$\gamma$ It can be easily checked…` —— 原页在 $\gamma$ 后**有句点**
     （/tmp/mirzakhanipub_p018_gammaperiod_300crop.png 直证 `the closure of γ .`，句点位于行末 γ 的右下方；
     文本层 `is in the closure of γ .` 亦为独立 token）→ 补 `.`；
  2. **MD L634**：编号条目 1 末尾 `…which will be denoted by$\Omega ( \gamma _ { x } )$` —— 原页**有句点**
     （文本层 `by Ω(γx ).`）→ 补 `.`；
  3. **MD L646**：c) 条末尾 `…nor an isolated point in$E _ { i }$` —— 原页**有句点**
     （文本层 `nor an isolated point in E i .`）→ 补 `.`。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`boundary and isolated points in$E_i$.`、`a lamination$\gamma$spirals to a lamination$\Omega(\gamma)$iff$\Omega(\gamma)$is in`、
    `lamination [CEG]. Note that for$x\in E_i$, the corresponding … ray,$\gamma_x$falls into`、
    `denoted by$\Omega(\gamma_x)$`、`points in$E_i$in terms`、`For any$x\in E_i$, exactly one`、`then$x$is an isolated point of$E_i$.`、
    `then the point x is a boundary point of$E_i$.`、`components$\beta_1$and$\beta_j$of$X$, and`、
    `pants containing$\beta_1$and$\beta_j$ as follows.`、`if$\gamma$is a simple arc joining`、`containing$\gamma$and these`、
    `Conversely, if Σ is a pair of pants containing` 等），全篇通例。
  - 原页 `spirals to a lamination` 为斜体强调、`1.`/`2.` 与 a)/b)/c) 为悬挂缩进列表，MD 中缩进信息丢失，不误导。
  - 图 `Fig. 4` 由两个 jpg 拼成，MD 以两行 `![](…)` + 单一 `Fig. 4` 图题对应原页同一编号，内容不缺。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 3 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `closure of$\gamma$ It can be`、`denoted by$\Omega ( \gamma _ { x } )$`、
  `nor an isolated point in$E _ { i }$` 三个字符串各自只命中 `d351abbff`（本 MD 首次入库提交）。
  原导出即不正确，本轮按原页修复。
- 历史核验：Peer-P11 曾在 p.018「去掉 (b)(c) 两式中 $\Omega(\gamma_x)$ 前的伪 `H`」；本轮复核
  MD L644/L646 的 (b)(c) 两行**均无**前导 `H`，与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L628–L656（页末为 `Fig. 4` 图题）；`ProofofTheorem$4 . 6 ( a )$.`（MD L658）起属 p.19。

## p.019（PDF p.19 / 印刷 p.197）
- PNG：/tmp/mirzakhanipub_audit_p019.png（pngmono 150dpi，gs -r150 -dFirstPage=19 -dLastPage=19）；
  仲裁裁剪：/tmp/mirzakhanipub_p019_a1a2_300crop.png（`perpendicular to β̃ at a₁ and a₂`）、
  /tmp/mirzakhanipub_p019_gz2period_300crop.png（`z₂}.` 句点）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 197`；跨页承接句
  `arc in Σ joining β₁ and β_j perpendicularly; this is the shortest simple arc in Σ joining β₁ to β_j.`；
  `Proof of Theorem 4.6(a).` 段（$x_1\in E_1$、other end of $\gamma_{x_1}$ goes up to $\beta_1$、$x_2\in\beta_1$、
  `; so we have`、$\gamma_{x_1}\cap\beta_1=\{x_1,x_2\}$、Let $\Sigma$ denote、$\partial\Sigma=\{\beta_1,\alpha_1,\alpha_2\}$、
  both $\alpha_1$ and $\alpha_2$ are non-peripheral simple closed curves.）；
  `There are exactly four infinite geodesic rays in Σ meeting β₁ perpendicularly at one point (as in Fig. 1).` 段
  （$\gamma_{y_i}$ and $\gamma_{z_i}$、spiraling around $\alpha_i$、$i=1,2$、$x_1\in E_1\cap(y_1,y_2)$、
  $x_2\in E_1\cap(z_1,z_2)$、`We claim that`）；展示式 $E_1\cap(y_1,y_2)=x_1,$；`and` 与展示式
  $E_1\cap(z_1,z_2)=x_2.$；`Assume γ_z is a simple geodesic ray such that z ∉ {x₁,x₂,y₁,y₂,z₁,z₂}.` 段
  （must leave $\Sigma$、$\alpha_1\cup\alpha_2$、Without loss of generality、meets $\alpha_1$ first、
  let $\tilde\beta$ joining $s_1$ and $\infty$、let $\tilde\alpha_1$ joining $r_1$ and $r_2$、
  outermost lift of $\alpha_1$ meeting $\tilde\gamma_z$、$\psi_1$ and $\psi_2$、perpendicular to $\tilde\beta$ at $a_1$ and $a_2$、
  endpoints of $\tilde\alpha_1$、$\eta_1$ (resp. $\eta_2$)、piecewise geodesic path、from $\tilde z$ to $h$ along $\tilde\gamma_z$、
  from $h$ to $r_1$ (resp. $r_2$) along $\tilde\alpha_1$、simple on $X$、disjoint from both $\alpha_1$ and $\alpha_2$）；
  `Furthermore, η₁ (resp. η₂) is homotopic to ψ₁ (resp. ψ₂). … complete simple geodesics on Σ. Since`（页末断句）；
  图 `Fig. 5`（标注 $\alpha_2,\tilde x,\alpha_1,\tilde\beta,\tilde\alpha_1,h,r_2,r_1,s_1$）
- 结果：**FAIL**（5 处已修，以原图为准）。
- 差异（5 处，均已用 Edit 逐处修复，证据 = 300dpi 裁剪 + `pdftotext` 文本层/bbox 双证）：
  1. **MD L658**：`ProofofTheorem$4 . 6 ( a )$.` —— **词内粘连**，原页为 `Proof **of Theorem** 4.6(a).`
     （文本层 `Proof of Theorem 4.6(a).` 为三个独立 word）→ 改 `Proof of Theorem$4 . 6 ( a )$.`；
  2. **MD L658**：`$\gamma _ { x _ { 1 } } ;$; so we have` —— **分号重复**，原页为**单个**分号
     （文本层 `the other end of γx1 ; so we have γx1 ∩ β1 =`，一个分号 token）→ 改 `};$ so we have`；
  3. **MD L660**：`$x _ { 2 } \in E _ { 1 } \cap ( z _ { 1 } , z _ { 2 } )$ We claim that` —— 原页 $(z_1,z_2)$ 后
     **有句点**（bbox 该行末 token 为 `(z 1 , z 2 ).`，句点与闭括号同属一个 word）→ 补 `.`；
  4. **MD L672**：`$z \not \in \{ … , z _ { 2 } \}$ Then$\gamma _ { z }$` —— 原页集合右花括号后**有句点**
     （/tmp/mirzakhanipub_p019_gz2period_300crop.png 直证 `…, y₂, z₁, z₂}.`）→ 补 `.`；
  5. **MD L672**：段末 `…infinite simple geodesic rays on the pair of pants$\Sigma$` —— 原页**有句点**
     （文本层 `geodesic rays on the pair of pants Σ.`）→ 补 `.`。
- **字形仲裁（150dpi 初读有误，以 300dpi + bbox 为准，MD 正确未改）**：`Consider ψ₁ and ψ₂, two geodesics
  perpendicular to $\tilde\beta$ at $a_1$ and $a_2$` 一句，150dpi 下我把 $a_1,a_2$ 读作 $\alpha_1,\alpha_2$
  （同页上文确有 $\alpha_1,\alpha_2$，易混）。300dpi 裁剪（/tmp/mirzakhanipub_p019_a1a2_300crop.png）
  直证两字形为**单层小写斜体 a**（而非鱼形 α）；bbox 亦证：此处 `a` 宽 5.47pt（x255.14、x285.50），
  而同页真正的 $\alpha$ 宽 6.25pt（x192.02），度量不同。
  **MD L672 `$a_1$` 与 `$a_2$` 本就正确，未改动**；且与同段稍后「$a_1$ and $a_2$ are actually pre-images of
  $z_1$ and $y_1$」的用法自洽。本人 150dpi 误读在此登记。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`Let$x_1\in E_1$be such that`、`the other end of$\gamma_{x_1}$goes up to$\beta_1$`、
    `be the other end of$\gamma_{x_1}$; so we have$\gamma_{x_1}\cap\beta_1=$`、
    `rays in Σ meeting$\beta_1$perpendicularly`、`Let$\gamma_{y_i}$and$\gamma_{z_i}$be the ones spiraling`、
    `Assume$\gamma_z$is a simple geodesic ray`、`must leave$\Sigma$and hence it meets$\alpha_1\cup\alpha_2$.`、
    `let$\tilde\beta$, joining$s_1$and$\infty$, be a lift of$\beta_1$.`、`Also, let $\tilde\alpha_1$`、
    `two geodesics perpendicular to$\tilde\beta$at$a_1$and$a_2$`、`And let$\eta_1$(resp.$\eta_2$)be`、
    `going from$\tilde z$to h along$\tilde\gamma_z$and from h to$r_1$(resp.$r_2$)along$\tilde\alpha_1$.`、
    `since$\tilde\alpha_1$is the outermost lift of$\alpha_1$meeting $\gamma_z$`、`is homotopic to$\psi_1$(resp.$\psi_2$).` 等），全篇通例。
  - `Σ` 用 Unicode 字符而非 `\Sigma`（MD L658/L660/L672），与原页字形等价，不改。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 5 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `ProofofTheorem`、`} ;$; so we have`、`cap ( z _ { 1 } , z _ { 2 } )$ We claim that`
  三个字符串各自只命中 `d351abbff`（本 MD 首次入库提交）；另两处为句末句点缺失，与本篇通例同源。
- 历史核验：Peer-P11 曾在 p.019「去掉 $\Sigma$ 上的伪 hat」；本轮复核 MD L658/L660/L672 三处 `Σ` 上
  **均无** hat，与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L658–L674 前半（页末断在 `Since`）。**移交下一段**：全篇另有一处 `;$;`（分号重复）
  在 MD L1624，不在本段 PDF p.17–24 范围内，本轮未动，请后续审计员按同一证据标准处理。

## p.020（PDF p.20 / 印刷 p.198）
- PNG：/tmp/mirzakhanipub_audit_p020.png（pngmono 150dpi，gs -r150 -dFirstPage=20 -dLastPage=20）；
  仲裁裁剪：/tmp/mirzakhanipub_p020_Hplane_300crop.png（`upper half plane ℍ.`）、
  /tmp/mirzakhanipub_p020_Hin_300crop.png（`in ℍ such that`）
- 核对：页眉 `198 / M. Mirzakhani`；跨页承接段
  `both ψ₁ and ψ₂ are asymptotic to a lift of α₁, their images spiral to α₁. Therefore a₁ and a₂ are actually pre-images of z₁ and y₁. Also, for any x ∈ [a₁, a₂] the curve γ_x meets α. Therefore, we have z ∈ [y₁, z₁].` + QED 方块；
  `Next, assume that γ_x spirals into a compact minimal lamination Ω(γ_x). The proof of part (b) …` 段与 [M]；
  `To prove part (c) of Theorem 4.6, we construct a sequence {x_j} ⊂ E_i …` 段
  （getting close to $x$、approximate $\gamma_x$ with simple complete geodesics $\gamma_{x_j}$、
  right (left) side of $x$ on $\beta_i$）；
  `Quasi-geodesics.` 段（$d(x,y)$、two points $x,y\in\mathbb{H}$、$\alpha(t)$、parameterized by arclength、
  upper half plane $\mathbb{H}$、quasi-geodesic、$k>0$）；展示式 $d(\alpha(s),\alpha(t))>k|s-t|$（不等号方向 `>` 与 $|s-t|$）；
  `for all s and t. Recall that any quasi-geodesic is a bounded distance away from a unique geodesic. If L is much bigger than θ then any (L, θ) polygon path α of segments of length at least L and bends at most θ < π is a quasi-geodesic. See [CEG] for more details.`；
  `Now assume that γ̃ is a geodesic perpendicular to a fixed geodesic β̃ in ℍ such that γ̃ ∩ β̃ = {x}. Let α̃ be an (L, θ) polygon path such that α̃ and β̃ also meet at x, and the straightening of α̃ meets γ̃ in x_α. Then as (L, θ) → (∞, 0) the distance from x_α to x tends to zero. Moreover, if the bending angles are all positive (negative), then x_α is on the right (left) side of x on β̃. See Fig. 6.`；
  图 `![](images/page_19_image_7.jpg)` + `Fig. 6`（标注 $x_\alpha$、$x$、$\tilde\beta$、$\tilde\alpha$、$\tilde\gamma$）
- 结果：**FAIL**（3 处已修，以原图为准）。
- 差异（3 处，均已用 Edit 逐处修复，证据 = 300dpi 裁剪 + `pdftotext` 文本层双证）：
  1. **MD L678**：`…compact minimal lamination$\Omega ( \gamma _ { x } )$ The proof of part (b)…`
     —— 原页 $\Omega(\gamma_x)$ 后**有句点**（文本层 `lamination Ω(γx ).` 为独立 token）→ 补 `.`；
  2. **MD L682**：`…arclength in the upper half plane H.` —— 原页为**黑板粗体 $\mathbb{H}$**
     （/tmp/mirzakhanipub_p020_Hplane_300crop.png 直证 `…ane ℍ .`，双线 H），MinerU 拍平为平文 `H`
     → 改 `half plane$\mathbb{H}$.`；
  3. **MD L690**：`…perpendicular to a fixed geodesic$\tilde{\beta}$ in H such that…` —— 原页亦为
     **黑板粗体 $\mathbb{H}$**（/tmp/mirzakhanipub_p020_Hin_300crop.png 直证 `in ℍ su…`）
     → 改 `in$\mathbb{H}$such that`。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`both$\psi_1$and$\psi_2$are asymptotic to a lift of$\alpha_1$`、
    `for any $x \in [a_1,a_2]$the curve$\gamma_x$meets$\alpha.$Therefore, we have$z\in[y_1,z_1]$`、
    `assume that$\gamma_x$spirals into`、`proof of part (b) is exactly the same`、`we construct a sequence$\{x_j\}\subset E_i$getting close to $x$.`、
    `Let$d(x,y)$denote`、`denote the hyperbolic distance between two points x,$y\in\mathbb{H}.$`、
    `Let$\alpha(t)$be a path parameterized by`、``We say α is a quasi-geodesic if there exists$k > 0$such that``、
    `for all $s$and $t$.`、`If L is much bigger than$\theta$then any$(L,\theta)$polygon path α`、
    `of segments of length at least L and bends at most$\theta < \pi$is a quasi-geodesic.`、
    `Now assume that$\tilde\gamma$is a geodesic perpendicular to`、`Let$\tilde\alpha$be an$(L,\theta)$polygon path`、
    `Then as $(L,\theta)\to(\infty,0)$the distance from$x_\alpha$to x tends to zero.`、
    `then$x_\alpha$is on the right (left) side of x on$\tilde\beta$.` 等），全篇通例。
  - 页首承上句末 `Therefore, we have $z\in[y_1,z_1]$.` 后的 **QED 方块** 未收录（与 p.15/p.17 同类），
    装饰性结束符，不补。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 3 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `lamination$\Omega ( \gamma _ { x } )$ The proof`、`arclength in the upper half plane H.`、
  `in H such that` 三个字符串各自只命中 `d351abbff`（本 MD 首次入库提交）。原导出即不正确，本轮按原页修复。
- 历史核验：Peer-P11 曾在 p.020 做两处修复——「去掉 $\theta$ 的冒号下标」与「补回 $(L,\theta)\to(\infty,0)$ 的箭头」。
  本轮复核：全篇 `\theta _ { :` 出现次数为 **0**（`grep -cF 'theta _ {'` = 0），且 MD L690 现为
  `Then as $(L,\theta)\to(\infty,0)$`，箭头在位。**两处旧修复均正确保留，非回归**。
- 备注：本页覆盖 MD L674–L694（页末为 `Fig. 6` 图题）；`![](images/page_20_image_0.jpg)` 与 `Fig. 7`（MD L696–698）起属 p.21。

## p.021（PDF p.21 / 印刷 p.199）
- PNG：/tmp/mirzakhanipub_audit_p021.png（pngmono 150dpi，gs -r150 -dFirstPage=21 -dLastPage=21）；
  仲裁裁剪：/tmp/mirzakhanipub_p021_epsgood_300crop.png（`is an ε-good geodesic arc iff` 的 ε 字形）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 199`；图 `![](images/page_20_image_0.jpg)` + `Fig. 7`
  （标注 $\alpha(t_0)$、$c$、$\alpha(t_1)$、$\alpha$）；`Finding quasi-geodesics.` 段与引导句；
  `I): Good geodesic segments.` 段（$\alpha(t)$、arc length parameterization of a simple geodesic segment on $X$、
  $c:[0,1]\to X$、differentiable arc transverse to $\alpha$）；展示式 $c(0)=\alpha(t_0),\ c(1)=\alpha(t_1),$；
  `where t₀ < t₁ ∈ ℝ. We say that (α, t₀, t₁, c) is an ε-good geodesic arc iff` 与**三条项目符号**：
  第一条 `ℓ(c) ≤ ε,`、第二条 `The arc c is almost perpendicular to α, that is` 与两行展示式
  $\left|\angle(c'(0),\alpha'(t_0))-\frac{\pi}{2}\right|\leq\epsilon,$ / $\left|\angle(c'(1),\alpha'(t_1))-\frac{\pi}{2}\right|\leq\epsilon,$
  （**绝对值竖线在位**、减号在位、`\frac{\pi}{2}` 在位）、`and`、第三条
  `The arc c meets the geodesic arc α in only two points, that is we have` 与展示式
  $c\cap\{\alpha(t)\mid t_0\leq t\leq t_1\}=\{\alpha(t_0),\alpha(t_1)\}.$；
  `Consider the vectors…` 整段（$\alpha'(t_0)$ and $c'(0)$ at point $c(0)=\alpha(t_0)$、$\alpha'(t_1)$ and $c'(1)$ at $c(1)=\alpha(t_1)$、
  two tangent vectors to $\alpha$ at $\alpha(t_1)$ and $\alpha(t_0)$、orientations of $(\alpha'(t_1),c'(1))$ and
  $(\alpha'(t_0),c'(0))$、positive (negative)）；展示式 $(\alpha'(t_0),c'(0))$；
  页末 `is the same as (different from) … independent of the parameterization of the path α.`
- 结果：**FAIL**（1 处已修，以原图为准）。
- 差异（已用 Edit 修复）：**MD L708** `…is an ␍-good geodesic arc iff $\ell ( c ) \leq \epsilon .$`
  —— 两处错误，(a) `ε-good` 的 **$\epsilon$ 丢失**：经 `od -c` 实测该位置是一个**裸控制字节 0x0F（SI）**
  （`i s ␣ a n ␣ 017 - g o o d`），既非 $\epsilon$ 也非空格，渲染为空；(b) 原页的**第一条项目符号
  `• ℓ(c) ≤ ε,` 被并入上一句**，项目符号标记与列表结构丢失，且句末逗号被改成句点。
  300dpi 裁剪（/tmp/mirzakhanipub_p021_epsgood_300crop.png）直证原页印作 `…c) is an **ε**-good geodesic arc iff`
  —— ε 清晰在位于 `-good` 之前。修复：还原为
  `…is an$\epsilon$-good geodesic arc iff` + 空行 + 独立项目符号行 `• $\ell ( c ) \leq \epsilon ,$`。
- **登记更正（影响本段此前各页的 QED 说明）**：我在 p.015/p.017/p.019/p.020 各页把证明收尾的
  **QED 方块（□）记为「未收录」**，这一说法不准确。实测本 MD 用**裸控制字节对 `0x0F 0x10`** 承载该方块：
  例如 MD L626 末尾为 `_ { i } ) = 0$␍␐`、L674 末尾为 `, z _ { 1 } ]$␍␐`，与原页 `μ(E_i) = 0. □`
  与 `z ∈ [y_1, z_1]. □` 的方块位置一一对应。即方块**并未缺失，而是以不可渲染的控制码形式存在**。
  本页不改动这些字节（超出「改内容」的范围，且属 MinerU 编码约定问题），仅更正前述表述；
  是否把 `0x0F 0x10` 统一替换为 `□` 或 `$\square$，留待集成者决定。
  **全篇 0x0F 计数**：修复前 12 处，修复本页 1 处后余 11 处；其中 L626、L674 落在本段页域内且为 QED 方块，
  L732 为下一页的同类 ε 丢失（见下），其余（L762 起及 L1136、L1640）在本段 PDF p.17–24 范围外。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`Let$\alpha(t)$be the arc length parameterization`、`Also let$c:[0,1]\to X$be a differentiable arc transverse to α`、
    `where$t_0<t_1\in\mathbb{R}$.`、`We say that$(\alpha,t_0,t_1,c)$is an$\epsilon$-good geodesic arc iff`、
    `Consider the vectors$\alpha'(t_0)$and$c'(0)$at point$c(0)=\alpha(t_0)$, and$\alpha'(t_1)$and $c'(1)$at the point$c(1)=\alpha(t_1)$.`、
    `If$(\alpha,t_0,t_1,c)$is a good geodesic segment`、`We say$(\alpha,t_0,t_1,c)$is` 等），全篇通例。
  - 平文字符 α、c 未加数学斜体标记，字形同原页，不误导。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页缺陷已溯源）：**为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S 'good geodesic arc iff'`
  只命中 `d351abbff`（本 MD 首次入库提交）；且 `git show cpf-redo/Mirzakhani_2007_simple_geodesics_published^:"…md"`
  的第 708 行仍含该 0x0F 字节（`grep -c $'\x0f'` = 1），证明该控制码自首次导出即在、其后未被任何 peer 改动。
- 备注：本页覆盖 MD L696–L730（页末为 `independent of the parameterization of the path α.`）；
  `II): Complete simple geodesics.`（MD L732）起属 p.22。**预告**：MD L732 存在与本页同型的
  0x0F 裸字节（`be an ␍-good geodesic segment`），将在 p.22 一并修复。

## p.022（PDF p.22 / 印刷 p.200）
- PNG：/tmp/mirzakhanipub_audit_p022.png（pngmono 150dpi，gs -r150 -dFirstPage=22 -dLastPage=22）
- 核对：页眉 `200 / M. Mirzakhani`；`II): Complete simple geodesics.` 段（Fix $x\in\beta_i$、
  $\epsilon$-good geodesic segment）；展示式 $\alpha\cap\gamma_x=\emptyset,\ \gamma_x\cap c[0,1]\neq\emptyset,$；
  `and let` 与展示式 $t_2=\inf\{t\mid\gamma_x(t)\in c[0,1]\}.$；
  `Let ψ(α, t₀, t₁, c) denote…` 整段（$\psi$、goes along $c$ from $\alpha(t_1)$ to $\alpha(t_0)$、
  goes back to $\alpha(t_1)$ along $\alpha$、complete simple curve $\eta$、goes along $\gamma(t)$ for $t\leq t_2$.、
  spirals around $\psi$、quasi-geodesic、bounded distance of a unique complete simple geodesic）；
  Lemma 4.7 陈述（`Assume that` + 展示式 $c\cap\{\gamma_x(t)\mid 0\leq t<t_2\}=\emptyset.$）；
  `For any ε > 0 there exist δ, L > 0 such that …` 段（$\delta$-good geodesic segment、$L\leq t_1-t_0$、
  simple quasi geodesic、`Let η̂ denote the geodesic representative of η and y = η̂ ∩ β_i. Then`）；
  展示式 $d(y,x)<\epsilon.$；`Furthermore, y lies on the right (left) side of x if and only if (α,t₀,t₁,c) is positive (negative).`；
  `Now we can prove that if Ω(γ_x) is not a simple closed curve, then x is not a boundary point of E_i.`；
  `Sketch of the proof of Theorem 4.6(c).` 整段（$\lambda=\Omega(\gamma_x)$、two steps、positive $\epsilon$-good geodesic segments）；
  编号条目 1 及其三条项目符号（$\phi_y$、arc length parameterization of the leaf of $\lambda$、
  $\phi_y(0)=y$、for any $\epsilon$, $L>0$、$0<t$、a transverse arc $c$、$y\in c\cap\lambda$；
  `(φ_y, 0, t, c) is a positive ε-good geodesic segment,` / `L ≤ |t|, and` /
  `the points y = φ_y(0) and φ_y(t) are not boundary points in λ ∩ c.`）；
  `To prove the claim…` 段（transverse almost perpendicular arc $c_1$、[HP]、$x_0$、$\phi=\phi_{x_0}$、
  `Choose a small transverse subarc c : [−r, +r] → X, r > 0, c(0) = x_0 such that for φ(a) ≠`）；页末断句
- 结果：**FAIL**（6 处已修，以原图为准）。
- 差异（6 处，均已用 Edit 逐处修复，证据 = 150dpi 原页目检 + `pdftotext -layout` 文本层 + `od -c` 字节实测）：
  1. **MD L734**：`Let$(…c)$be an <0x0F>-good geodesic segment such that` —— $\epsilon$ 处是**裸控制字节 0x0F**，
     渲染为空；原页印作 `be an **ε**-good geodesic segment` → 改 `an$\epsilon$-good`；
  2. **MD L764**：`…one can find positive <0x0F>-good geodesic segments inside λ` —— 同型 → 改 `positive$\epsilon$-good`；
  3. **MD L766**：`We claim that for any <0x0F>,$L > 0$` —— 同型 → 改 `for any$\epsilon$,`；
  4. **MD L768**：`$( \phi _ { y } , 0 , t , c )$is a positive <0x0F>-good geodesic segment,` —— 同型 ε 丢失，
     且原页该行为**项目符号条目**（文本层 `• (φy , 0, t, c) is a positive ε-good geodesic segment,`）
     而 MD **丢失 `•` 标记** → 改 `• $(…)$is a positive$\epsilon$-good geodesic segment,`；
  5. **MD L760**：`lies on the right$( l e f t )$side of x if and only$i f \left(…\right)$` —— 两处**散文词被摄入数学模式
     并逐字母加空格**，渲染成 `l e f t` 与 `i f`；原页均为普通散文 `left` 与 `if`
     → 改 `on the right (left) side of x if and only if $\left(…\right)$`；
  6. **MD L748**：`## Lemma 4.7. Assume that` —— 该行被 MinerU 误标为 **Markdown 二级标题**。
     实测全篇 `^## (Lemma|Theorem|Corollary)` **仅此一处**，而同级的 Theorem 1.1/1.2/1.3/2.1、
     Lemma 3.1/3.2/4.4/4.5/4.6、Corollary 4.3 全部为普通正文（`grep -nE '^(Lemma|Theorem) [0-9]'` 可证），
     原页亦仅为加粗句首而非节标题 → 去 `##`，改为 `Lemma 4.7. Assume that`，与全文同级陈述体例一致。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`Fix$x \in \beta_i$.`、`Let$(…c)$be`、`is the same as (different from) the orientation`、
    `Let$\psi(…)$denote`、`goes along c from$\alpha(t_1)$to$\alpha(t_0)$, and then goes back to$\alpha(t_1)$along α.`、
    `goes along$\gamma(t)$for$t \leq t_2$.`、`spins around$\psi(…)$.`、`by changing the direction of$\alpha,\eta$will be`、
    `For any$\epsilon > 0$there exist$\delta,L>0$such that`、`is a δ-good geodesic segment and$L \leq t_1-t_0$`、
    `if$\Omega(\gamma_x)$is not a simple closed curve`、`Let$\lambda = \Omega(\gamma_x)$.`、
    `Given$y \in \lambda,$, let$\phi_y$denote`、`such that$\phi_y(0) = y$.`、`a transverse arc c, and$y \in c\cap\lambda$such that:`、
    `choose a transverse almost perpendicular arc$c_1$`、`[HP].`、`Let$\phi = \phi_{x_0}$.` 等），全篇通例。
  - MD L766 的 `Given$y\in\lambda,$,` 把逗号放进数学模式（渲染为 `λ,`），语义无歧义，不改。
  - 原页条目 1 写作 `there exist 0 < t, a transverse arc c, …`（`0<t` 后直接逗号，语法上不完整），
    系印刷原文如此，MD 逐字保留，**不代为补成 `0 < t_1`**。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 6 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `be an ␍-good geodesic segment`、`positive ␍-good`、`for any ␍,$L > 0$`、`a positive ␍-good`、
  `## Lemma 4.7.`、`right$( l e f t )$side` 六个字符串各自只命中 `d351abbff`（本 MD 首次入库提交）。
  原导出即不正确，本轮按原页修复。
- 历史核验：Peer-P11 曾在 p.022 做两处修复——「重建 `Let η̂ denote …` 句」与「补回 $c:[-r,+r]\to X$ 的箭头」。
  本轮复核：MD L754 现为 `Let $\widehat{\eta}$ denote the geodesic representative of $\eta$ and $y = \widehat{\eta}\cap\beta_i$. Then`，
  句子完整；页末 `Choose a small transverse subarc c : [−r, +r] → X, r > 0, c(0) = x_0` 的箭头在位。
  **两处旧修复均正确保留，非回归**。
- 备注：本页覆盖 MD L734–L768 及其后续条目（页末断在 `such that for φ(a) ≠`）。
  **全篇 0x0F 现状**：本段修复前 12 处，已修 5 处（p.21 一处 + 本页四处），余 7 处；
  其中 L626、L674 为证明收尾的 QED 方块（见 p.021 条更正说明），其余 5 处（L762 起及 L1136、L1640）
  在本段 PDF p.17–24 范围外，移交后续审计员。

## p.023（PDF p.23 / 印刷 p.201）
- PNG：/tmp/mirzakhanipub_audit_p023.png（pngmono 150dpi，gs -r150 -dFirstPage=23 -dLastPage=23）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 201`；图 `![](images/page_22_image_0.jpg)` + `Fig. 8`
  （a) b) c) 三panel，标注 $C$、$0$、$\phi_{x_0}$、$t_2$、$t_1$、$-r$、$-r+\epsilon$）；
  跨页承接句 `φ(b) ∈ c[−r, r], we have |a − b| > L. Without loss of generality, we can assume that the orientation of the pair`；
  展示式 $(\phi_0',c_0')$；`agrees with the orientation of X. Let` 与展示式
  $t_1=\inf\{t>0\mid\phi(t)\in c[-r,0)\}.$；`Then there is a number x₁ such that…` 段
  （$\phi(t_1)=c(x_1)$、Similarly、as $\phi(t_1)$ is not boundary point、$t>t_1$、$\phi(t)\in c(x_1,0)$、Define）与展示式
  $t_2=\inf\{t>t_1\mid\phi(t)\in c(x_1,0)\}.$；`As in Fig. 8, at least one of…` 段与展示式
  $\min\{|t_1-t_2|,t_1,t_2\}\geq L.$；编号条目 2 整段（$(\alpha,t_1,t_2,c)$、$\epsilon$-good geodesic segment in $\lambda$、
  $\alpha(t_i)=c(r_i)$、$\alpha(t_1)$ is not a boundary point of $\lambda\cap c$.、$\gamma_x$ spirals to $\lambda$、
  $\gamma_x\cap c[r_1,r_2]$ is non-empty. Let）与展示式 $t_0=\inf\{t\mid\gamma_x(t)\in c[r_1,r_2]\}.$；
  `Now Lemma 4.7 implies the result.` + QED 方块；`A similar argument shows…` 段
  （complete simple geodesics approximating $\gamma_x$ from one side、$\Omega(\gamma_x)$ non-peripheral simple closed curve、
  by the proof of part (a)、$x$ is a boundary point of $E_i$.）；`As a result, the set of non-isolated points of $E_i$…`；
  `Proof of Theorem 4.5.` 段（perfect totally disconnected compact metric space、Cantor set、[HY]）；
  页末 `By Theorem 4.6, apart from countably many points, … perfect subset of β_i.` + QED 方块
- 结果：**FAIL**（4 处已修，以原图为准；另含 1 处属 p.22 的补修）。
- 差异（均已用 Edit 逐处修复，证据 = 150dpi 原页目检 + `pdftotext -layout` 文本层 + `od -c` 字节实测）：
  1. **MD L794**：`…is a positive <0x0F>-good geodesic segment. Also, we have` —— $\epsilon$ 处为**裸控制字节 0x0F**，
     原页印作 `a positive **ε**-good geodesic segment`（文本层 `a positive ε-good geodesic segment.`）
     → 改 `positive$\epsilon$-good`；
  2. **MD L800**：`…be an <0x0F>-good geodesic segment in λ such that…` —— 同型 → 改 `an$\epsilon$-good`；
  3. **MD L800**：段末 `…is not a boundary point of$\lambda\cap c$` **缺句点**
     （文本层 `…is not a boundary point of λ ∩ c.`）→ 补 `.`；
  4. **MD L810**：`…by the proof of part (a), x is a boundary point of$E _ { i }$` **缺句点**
     （文本层 `…is a boundary point of E i .`）→ 补 `.`；
  5. **补修（缺陷位于 PDF p.22 / MD L772）**：`• the points…are not boundary points in$\lambda\cap c$` **缺句点**
     （原页与 `pdftotext -f 22 -l 22` 文本层 `…in λ ∩ c.` 均作句点）。该行属 **p.22** 页域，
     我在 p.022 落签时未发现，**在本页复核时补记并修复**，特此声明以免该页出现两条落签。
- **字形仲裁（150dpi 初读有误，以文本层 + MD 一致性为准，MD 正确未改）**：条目 2 中
  `$\alpha(t_i)=c(r_i)$` 一处，150dpi 下我把下标读作 `1`，但 `pdftotext -f 23 -l 23` 文本层作
  `α(ti ) = c(ri )`（下标 i），且同段随后用 `c[r_1,r_2]`、`c(r_i)` 交叉印证——即 $\alpha(t_i)=c(r_i)$ 为**一般下标 i**
  而非 $t_1/r_1$。**MD L800 的 `t _ { i }` 与 `r _ { i }` 本就正确，未改动**。
  同理展示式 $\min\{|t_1-t_2|,t_1,t_2\}\geq L.$ 的第二项**无绝对值竖线**（文本层 `min{|t1 − t2 |, t1 , t2 } ≥ L.`），
  MD L797 正确，未改动。本人 150dpi 误读在此登记。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`φ(b) ∈ c[−r,r]$`段起、`the orientation of the pair`、
    `Then there is a number$x _ { 1 }$such that`、`Similarly, as$\phi(t_1)$is not boundary point`、
    `As in Fig. 8, at least one of$(…)$`、`Now let$(…)$be an$\epsilon$-good`、
    `approximating$\gamma_x$from one side if$\Omega(\gamma_x)$is a non-peripheral`、
    `points in$E_i$are limit points.`、`non-isolated points of$E_i$form a compact` 等），全篇通例。
  - MD L774 把跨页句拆成 `…such that for$\phi ( a ) \ \neq$` 与 `$\phi ( b ) \in c [ - r , r ]$，渲染连贯，无需合并。
  - MD L800 中 `such that $\alpha(t_i)=c(r_i)$` 两侧留有空格（原页无空格），属 MinerU 行内数学并排的空格伪影，不改。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 4 处 + 补修 1 处均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `is a positive ␍-good geodesic segment. Also`、`be an ␍-good geodesic segment in`、
  `points in$\lambda\cap c$`、`by the proof of part (a), x is a boundary point of$E_i$`
  四个字符串各自只命中 `d351abbff`（本 MD 首次入库提交）。原导出即不正确，本轮按原页修复。
- 备注：本页覆盖 MD L774–L816（页末为 Theorem 4.5 证明收尾 + QED 方块）；
  `Connection with embedded pairs of pants.`（MD L818）起属 p.24。
  **全篇 0x0F 现状更新**：本段累计已修 7 处（p.21 一处、p.022 四处、本页两处），余 **5** 处：
  L626、L674（本段内的 QED 方块，见 p.021 条更正）、L816（本页 Theorem 4.5 证明收尾的 QED 方块），
  以及 L1138、L1642（在本段 PDF p.17–24 范围外，移交后续审计员）。

## p.024（PDF p.24 / 印刷 p.202）
- PNG：/tmp/mirzakhanipub_audit_p024.png（pngmono 150dpi，gs -r150 -dFirstPage=24 -dLastPage=24）；
  仲裁裁剪：/tmp/mirzakhanipub_p024_eq44_300crop.png（公式 (4.4) 的 ℛ 字形）
- 核对：页眉 `202 / M. Mirzakhani`；`Connection with embedded pairs of pants.` 小节首段全句
  （$x\in E_i$、$\gamma_x$ spirals into $\alpha_1$、unique embedded pair of pants $\Sigma_x$ on $X$、
  $\gamma_x\subset\Sigma_x$、$\alpha_2$ bounding a pair of pants $\Sigma_x$ with $\beta_i$ and $\alpha_1$、
  The curve $\alpha_2$ could be peripheral.）；`Let I_i be the set of isolated points in E_i. Then we can write` 与展示式
  $I_i\cup(\beta_i-E_i)=\bigcup_{h\in H}(a_h,b_h),$（$\bigcup$ 下标 `h\inH`）；`where H is the set of connected components…` 段
  （end points of $h\in H$、both $a_h$ and $b_h$ are boundary points of $E_i$、correspondence）；
  `Fix h ∈ H, Theorem 4.6 implies…` 段与展示式 $\partial(\Sigma_h)=\{\beta_i,\Omega(\gamma_{a_h}),\alpha\}$；
  `We claim that γ_{b_h} ⊂ Σ_h. First, assume…` 段（$y\in(a_h,b_h)$、$\gamma_y\subset\Sigma_h$、
  $\alpha=\Omega(\gamma_{b_h})$、$\Omega(\gamma_{a_h}),\Omega(\gamma_{b_h})$ and $\beta_i$ bound a pair of pants.）；
  `Similarly the claim holds…` 段（$\alpha=\beta_j$、$\beta_i,\beta_j$、Lemma 4.4）；
  `Proof of Theorem 4.2.` 与展示式 $I_i\cup(\beta_i-E_i)=\bigcup_h(a_h,b_h),$（$\bigcup$ 下标仅 `h`）；
  `where a_h, b_h ∈ β_i. Then by Lemma 4.4 we have:` 与展示式 (4.3)
  $L_i=\ell_{\beta_i}(X)=\sum_{h\in H}|b_h-a_h|,$（编号 (4.3)、求和下限 `h∈H`、绝对值在位）；
  `where |a_h − b_h| is the geodesic distance…` 段；编号条目 1
  （$j\neq i$、$\gamma=\Omega(\gamma_{a_h})=\Omega(\gamma_{b_h})$、$\beta_j$ and $\beta_i$、In this case, we have）
  与页末展示式 (4.4) $\mathcal{R}(L_i,L_j,\ell_\gamma(X))=|a_h-b_h|.$（编号 (4.4)）
- 结果：**PASS±**。
- 差异（不误导，未改动）：
  - 行内公式两侧空格合并（`Let$x \in E_i$such that the ray $\gamma_x$spirals into a simple closed geodesic$\alpha_1$.`、
    `there is a unique embedded pair of pants$\Sigma_x$on$X$such that$\gamma_x\subset\Sigma_x$.`、
    `a unique simple closed geodesic$\alpha_2$bounding a pair of pants$\Sigma_x$with$\beta_i$and$\alpha_1$such that`、
    `Let$I_i$be the set`、`where$H$is the set of connected components of$I_i\cup(\beta_i-E_i)$, and$a_h,b_h$are the end points of$h\in H$;`、
    `both$a_h$and$b_h$are boundary points of$E_i$.`、`Fix$h\in H$, Theorem 4.6 implies that$\gamma_{a_h}$spirals into`、
    `Let$\Sigma_h$be the unique pair of pants containing$\gamma_{a_h}$such that`、
    `First, assume that$\alpha$is non-peripheral.`、`Then by Theorem 4.6,$\gamma_{b_h}\subset\Sigma_h$;`、
    `spirals into α which is not possible. So$\alpha=\Omega(\gamma_{b_h})$which means that`、
    `Similarly the claim holds when$\alpha=\beta_j$is a boundary component.`、
    `Using this correspondence and Lemma 4.4,`、`where$a_h,b_h\in\beta_i$.`、
    `where$|a_h-b_h|$is the geodesic distance between$a_h$and$b_h$along$\beta_i$.`、
    `There exists$j\neq i$such that the three curves$\gamma=\Omega(\gamma_{a_h})=\Omega(\gamma_{b_h}),\beta_j$and$\beta_i$bound a pair of pants in X.` 等），全篇通例。
  - MD L834 末尾 `spirals into α which is not possible.` 中的 `α` 为平文字符（原页为数学斜体），
    字形相同、不误导，登记不修。
  - MD L850 用 `\left| a_h - b_h \right|` 表达绝对值，与原页 `|a_h − b_h|` 等价，不改。
  - 页眉/页码未收录（全篇通例）。
- **字形仲裁（150dpi 初读有误，以文本层 + MD 一致性为准，MD 正确未改）**：
  - `otherwise we could find ? ∈ (a_h, b_h) such that γ_? ⊂ Σ_h` 一句，150dpi 下我把首个字母读作 $\gamma$，
    但 `pdftotext -f 24 -l 24` 文本层作 `find y ∈ (ah , bh ) such that γ y ⊂ Σh`，且句中「$y\in(a_h,b_h)$」与
    「$\gamma_y\subset\Sigma_h$」本就是两个不同对象（点 vs 其发出的射线），语义亦自洽。
    **MD L834 的 `$y \in ( a _ { h } , b _ { h } )$` 本就正确，未改动**。
  - 300dpi 裁剪（/tmp/mirzakhanipub_p024_eq44_300crop.png）直证展示式 (4.4) 首字母为**花体 ℛ**
    （`ℛ(L_i, L_j, ℓ_γ(X)) = |a_h − b_h| .`），与全文 $\mathcal{R}$ 用法一致；
    **MD L855 `\mathcal {R}` 正确，未改动**。
  - 展示式 $\partial(\Sigma_h)=\{\beta_i,\Omega(\gamma_{a_h}),\alpha\}$ 中 `Similarly … when α = β_j`
    与 `In this case β_i, β_j` 的下标顺序，MD 与原页逐字一致（前者 $\beta_j$、后者 $\beta_i,\beta_j$），
    未出现下标错位。
- 溯源：本页未判定任何缺陷，故无回归项。历史核验：Peer-P11 的修复登记表未含 p.024；
  本轮亦未见其引入的新伪影。
- 备注：本页覆盖 MD L818–L856（页末为展示式 (4.4)）。**本段（PDF p.17–24）到此结束**，共 8 页，全部已逐页落签。
  编号条目 2 与展示式 (4.5)（MD L858–L862）起属 p.25，不在本段范围。

---

# 独立重做审计（第二轮 redo，PDF p.025–p.032）

- 性质：独立第二轮重做审计，逐页重新渲染 PNG 亲眼目检；每条判定以本人所看原页 PNG +
  `pdftotext -layout` 文本层 + `pdftotext -bbox` 分词坐标三通道对账为据。
- Actor: `Wf-R-P11b`；Host / model / effort: zcode / `opencode-go-chat-space-bunny-free` / effort 自报 UNKNOWN
- 日期：2026-10-05（第四段，承接 p.001–p.008、p.009–p.016、p.017–p.024 三段）
- 被检 Markdown 基线 SHA-256 = `8a88afc94d0ee430e40a82bff7a1472167a031b0c73db0690117114f9f53f0b0`（1700 行；
  含前三段共登记修复；全篇 0x0F 裸控制字节 5 处）
- PDF SHA-256 = `c19a088d97b2b3223481341d059ef7836ea9f575f580d3bf574d0b475e7615cf`（44 页，未改动）
- 本段覆盖 PDF p.25–32 = 印刷 p.203–210（§5 递归公式陈述及其后续）。

## p.025（PDF p.25 / 印刷 p.203）
- PNG：/tmp/mirzakhanipub_audit_p025.png（pngmono 150dpi，gs -r150 -dFirstPage=25 -dLastPage=25）；
  仲裁裁剪：/tmp/mirzakhanipub_p025_icon_300crop.png（公式 (5.1) 第二项 𝒜 的上标字形）
- 核对：页眉 `Simple geodesics and Weil-Petersson volumes / 203`；跨页编号条目 2
  （$\gamma_1=\Omega(\gamma_{a_h})$、$\gamma_2=\Omega(\gamma_{b_h})$、distinct、bound a pair of pants containing $\beta_i$、
  Moreover, we have:）与展示式 (4.5) $\frac12\mathcal{D}(L_i,\ell_{\gamma_1}(X),\ell_{\gamma_2}(X))=|a_h-b_h|.$（编号 (4.5)）；
  `Note that as in Sect. 3, …` 段（another interval $(a_{h'},b_{h'})\in H$、$\Sigma_h=\Sigma_{h'}$、
  $|a_h-b_h|=|a_{h'}-b_{h'}|$、$\gamma_{a_{h'}}$ spirals around $\Omega(\gamma_{a_h})$ in a different direction.）；
  `Using equation (4.4) and equation (4.5), we can rewrite equation (4.3) as` 与展示式
  $L_i(X)=\sum_{\{\gamma_1,\gamma_2\}\in\mathcal{F}_i}\mathcal{D}(L_i,\ell_{\gamma_1}(X),\ell_{\gamma_2}(X))
  +\sum_{j\neq i}\sum_{\gamma\in\mathcal{F}_{i,j}}\mathcal{R}(L_i,L_j,\ell_\gamma(X)).$ + QED 方块；
  `5. Statement of the recursive formula for volumes` 节标题；`In this section we state…` 段（Sect. 8、$\mathcal{M}_{g,n}(L)$）；
  `Observe that the volume function…` 段（symmetric function、$A=\{a_1,\ldots,a_n\}$、define $V_{g,n}(A)$ by）与展示式
  $V_{g,n}(A)=V_{g,n}(a_1,\ldots,a_n).$；`Statement of the recursive formula.` 段（$2g-2+n>0$）；
  第一条项目符号 `For any $L_1,L_2,L_3\geq0$, set` 与展示式 $V_{0,3}(L_1,L_2,L_3)=1$、`and` 与展示式
  $V_{1,1}(L_1)=\frac{L_1^2}{24}+\frac{\pi^2}{6}.$；`The first equation holds…` 段；第二条项目符号
  `For $L=(L_1,\ldots,L_n)$, let $\widehat{L}=(L_2,\ldots,L_n)$. When $(g,n)\neq(1,1),(0,3)$, the volume $V_{g,n}(L)=\mathrm{Vol}(\mathcal{M}_{g,n}(L))$ satisfies`
  与展示式 (5.1) $\frac{\partial}{\partial L_1}L_1V_{g,n}(L)=\mathcal{A}^{con}_{g,n}(L_1,\widehat{L})+\mathcal{A}^{icon}_{g,n}(L_1,\widehat{L})+\mathcal{B}_{g,n}(L_1,\widehat{L}),$
- 结果：**FAIL**（2 处已修，以原图为准）。
- 差异（2 处，均已用 Edit 逐处修复）：
  1. **MD L901（数学记号缺陷）**：展示式 (5.1) 第二项原写作 `\mathcal{A}^{d c o n}_{g,n}`，
     原页印作 **`icon`**（/tmp/mirzakhanipub_p025_icon_300crop.png 300dpi 裁剪直证 `+ 𝒜^{icon}_{g,n}(L₁, L̂)`，
     上标为斜体 i-c-o-n，首字母有小圆点与下伸笔，非 d）。
     需注意 `pdftotext -bbox` 在此处**未抽出任何上标 token**（只给出 `A` 与 `g,n`），
     故文本层对此无发言权，**以 300dpi 裁片为裁决源** → 改为 `\mathcal{A}^{i c o n}_{g,n}`；
  2. **MD L876**：`Given a set A of positive numbers$A = \{a_1,\ldots,a_n\}$ define$V_{g,n}(A)$by`
     —— 原页集合 $A=\{\dots\}$ 后**有逗号**（文本层 `A = {a1 , . . . , an },` 与下一行 `define` 并列，
     且原页逗号位于行末换行处）而 MD 丢失 → 补 `,`。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`The two curves$\gamma_1=\Omega(\gamma_{a_h})$and$\gamma_2=\Omega(\gamma_{b_h})$are distinct;`、
    `in this case $\gamma_1$and$\gamma_2$bound a pair of pants containing$\beta_i$.`、
    `there is another interval$(a_{h'},b_{h'})\in H$such that`、`and$|a_h-b_h|=|a_{h'}-b_{h'}|$; the ray`、
    `state a recursive formula for$V_{g,n}(L)$, the Weil-Petersson volume of$\mathcal{M}_{g,n}(L)$.`、
    `volume function$V_{g,n}(L_1,\ldots,L_n)$is a symmetric function in$L_1,\ldots,L_n$.`、
    `For any$L_1,L_2,L_3\geq0$, set`、`the moduli space$\mathcal{M}_{0,3}(L_1,L_2,L_3)$consists of only one point.`、
    `For$L=(L_1,\ldots,L_n)$, let$\widehat{L}=(L_2,\ldots,L_n)$.`、`the volume$V_{g,n}(L)=\mathrm{Vol}(\mathcal{M}_{g,n}(L))$satisfies` 等），全篇通例。
  - 页眉/页码未收录（全篇通例）。
- **核对无误项（已目检确认，不改）**：展示式 (4.5) 的系数 $\frac12$、两个长度函数下标与 `\tag{4.5}`；
  改写式第一个求和的下标集为 **`\mathcal{F}_i`（带下标 i，非数字 1）**、第二和为 $\sum_{j\neq i}\sum_{\gamma\in\mathcal{F}_{i,j}}$；
  $V_{1,1}(L_1)=\frac{L_1^2}{24}+\frac{\pi^2}{6}$ 的**分母 24**；$V_{0,3}(L_1,L_2,L_3)=1$；三条项目符号标记均在位。
- 溯源（本页 2 处缺陷均已溯源）：**均为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S` 对
  `{c o n} (L _ {1}, \widehat {L}) + \mathcal {A} _ {g, n} ^ {d c o n}` 与 `a _ { n } \}$ define$V _ { g , n }`
  两个字符串各自只命中 `d351abbff`（本 MD 首次入库提交）。原导出即不正确，本轮按原页修复。
- 历史核验：Peer-P11 曾在 p.025 把示例分母 `2 4` 修为 `24`；本轮复核 MD L893 现为
  `\frac {L _ {1} ^ {2}}{24} + \frac {\pi^ {2}}{6}`，与原页一致，旧修复正确保留，非回归。
- 备注：本页覆盖 MD L858–L901（页末为展示式 (5.1)）。**遗留待核**：原页 (5.1) 用 `icon` 而同页之后
  定义的 (5.3) 用 `dcon`（MD L911 现为 `\mathcal{A}^{d c o n}`），二者若确系印刷自身不一致，
  将在 p.026 核实 (5.3) 原页字形后一并作为 print quirk 登记，不作统一。

## p.026（PDF p.26 / 印刷 p.204）
- PNG：/tmp/mirzakhanipub_audit_p026.png（pngmono 150dpi，gs -r150 -dFirstPage=26 -dLastPage=26）；
  仲裁裁剪：/tmp/mirzakhanipub_p026_mexp_300crop.png（$2^{m(g-1,n+1)}$ 的底数与指数）、
  /tmp/mirzakhanipub_p026_Iglyph_300crop.png（`Let 𝓘_{g,n} be the set of ordered …` 整行）
- 核对：页眉 `204 / M. Mirzakhani`；`where we have`；展示式 (5.2)
  $\mathcal{A}^{con}_{g,n}(L_1,\widehat{L})=\frac12\left(\int_0^\infty\int_0^\infty xy\,\widehat{\mathcal{A}}^{con}_{g,n}(x,y,L_1,\widehat{L})\,dx\,dy\right),$
  （编号 (5.2)、两个 $\int_0^\infty$、被积函数 $xy$、括号、尾随逗号）；展示式 (5.3)（同上结构，上标 `dcon`）；`and`；
  展示式 (5.4) $\mathcal{B}_{g,n}(L_1,\widehat{L})=\int_0^\infty x\cdot\widehat{\mathcal{B}}_{g,n}(x,L_1,\widehat{L})\,dx.$（编号 (5.4）；
  `Now we define the functions` 与三行定义式 $\widehat{\mathcal{A}}^{con}_{g,n}:\mathbb{R}_+^{n+2}\to\mathbb{R}_+,$ /
  $\widehat{\mathcal{A}}^{dcon}_{g,n}:\mathbb{R}_+^{n+2}\to\mathbb{R}_+,$ /（`and`）$\widehat{\mathcal{B}}_{g,n}:\mathbb{R}_+^{n+1}\to\mathbb{R}_+.$；
  `As in the introduction, let` 与展示式 $m(g,n)=\delta(g-1)\times\delta(n-1).$；`So $m(g,n)=0$ unless $g=1$ and $n=1$.`；
  `I): Definition of $\widehat{\mathcal{A}}^{con}_{g,n}$.` 段与展示式
  $\widehat{\mathcal{A}}^{con}_{g,n}(x,y,L_1,\ldots,L_n)=\frac{1}{2^{m(g-1,n+1)}}V_{g-1,n+1}(x,y,\widehat{L})\cdot H(x+y,L_1).$；
  `II): Definition of $\widehat{\mathcal{A}}^{dcon}_{g,n}$.` 段与 `Let $\mathcal{I}_{g,n}$ be the set of ordered pairs`（页末断句）
- 结果：**FAIL**（1 处已修，以原图为准）。
- 差异（已用 Edit 修复）：**MD L942** `So$m ( g , n ) = 0$unless$g = 1$and$n = 1$` —— 原页句末**有句点**
  （文本层 `So m(g, n) = 0 unless g = 1 and n = 1.`；原页目检亦见句点）而 MD 丢失 → 补 `.`。
- **print quirk 忠实登记不改（两处，均经双通道确认系印刷原文自身）**：
  1. **`icon` / `dcon` 前后不一致**：原页 (5.1)（印刷 p.203）第二项印作 $\mathcal{A}^{icon}_{g,n}$，
     而本页 (5.3) 与 `Now we define the functions` 后的第二行、以及 `II): Definition of` 标题
     （300dpi 裁剪 /tmp/mirzakhanipub_p026_Iglyph_300crop.png 直证 `𝒜^{dcon}_{g,n}`）均印作 $\mathcal{A}^{dcon}_{g,n}$。
     即原页自身前后不统一。**按 print-primacy 处理**：MD L901 现为 `icon`（依 (5.1) 原页），
     MD L911/L923/L927/L950 现为 `dcon`（依本页原页），二者**各自忠实、不作统一**，特此登记。
  2. **`ordered paris`**：`II): Definition of … Let $\mathcal{I}_{g,n}$ be the set of ordered **paris**`
     —— 300dpi 裁剪（/tmp/mirzakhanipub_p026_Iglyph_300crop.png）直证印作 `paris`（拼写错误，应为 pairs），
     文本层 `paris`（bbox x300.64–321.67 为独立 word）一致。
     **MD L950 保留 `ordered paris` 正确，不按英文正字法改写**。
- **核对无误项（已目检确认，不改）**：
  - I) 定义式的分母 $2^{m(g-1,n+1)}$ —— 300dpi 裁剪（/tmp/mirzakhanipub_p026_mexp_300crop.png）
    直证底数 **2**、指数 **$m(g-1,n+1)$**，MD L947 逐项吻合；
  - $\mathcal{I}_{g,n}$ 的字形为**花体 𝓘**（300dpi 裁片直证 CM calligraphic I 的卷曲衬线），
    MD L950 `\mathcal{I}_{g,n}` 正确——**该处正是 Peer-P11 修复过的「把误读的 $\tau_{g,n}$ 换成印刷的 𝓘」**，
    本轮复核旧修复保留完好；
  - (5.2)/(5.3) 的系数 $\frac12$、两个 $\int_0^\infty$、被积 $xy$、括号闭合与尾随逗号；(5.4) 的
    $x\cdot$ 与单个 $\int_0^\infty$；三行定义式的幂次 $n+2$/$n+1$ 与 `\to` 箭头，均与原页一致。
- **未改动的伪影（PASS± 登记，不修）**：
  - 行内公式两侧空格合并（`So$m(g,n)=0$unless`等已修；`Define$\widehat{\mathcal{A}}^{con}_{g,n}:\mathbb{R}_+^{n+2}\to\mathbb{R}_+$by`、
    `Let$\mathcal{I}_{g,n}$be the set of ordered paris` 等），全篇通例。
  - MD L917/L950 把帽号写作 `\widehat{\mathcal{B}_{g,n}}` / `\widehat{\mathcal{A}_{g,n}}`（罩住含下标的整体），
    而 L907/L911/L923 用 `\widehat{\mathcal{A}}_{g,n}`（只罩字母）；原页帽号跨 $\mathcal{A}$ 与下标 $g,n$，
    两种写法渲染近似，不误导，登记不修。
  - 页眉/页码未收录（全篇通例）。
- 溯源（本页 1 处缺陷已溯源）：**为原始 MinerU 导出缺陷，非 peer 回归**。`git log -S
  'unless$g = 1$and$n = 1$'` 只命中 `d351abbff`（本 MD 首次入库提交）。原导出即不正确，本轮按原页修复。
- 备注：本页覆盖 MD L904–L950（页末断在 `Let $\mathcal{I}_{g,n}$ be the set of ordered paris`）。
  定义式 $a=((g_1,I_1),(g_2,I_2))$、编号条目 1./2. 与 `g_1+g_2=g` 起属 p.27，不在本段首页范围。
