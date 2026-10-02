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
