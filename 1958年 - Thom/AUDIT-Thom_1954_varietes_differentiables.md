# AUDIT — Thom_1954_varietes_differentiables

- PDF: `1958年 - Thom/Thom_1954_varietes_differentiables.pdf` (70 PDF pages)
- MinerU Markdown: `1958年 - Thom/Thom_1954_varietes_differentiables_mineru/Thom_1954_varietes_differentiables__Thom_1954_varietes_differentiables.md`
- Review mode: scanned pages with an OCR text layer; 70-page visual review at 150 dpi (`pngmono`).
- Actor: Peer-P29
- Model: gpt-6-luna
- Reasoning effort: max
- Candidate base: `037602429d3b009f6fc468c732073eb3ddf9875f`
- Integration status: `CANDIDATE_NOT_CURRENT`; root `AUDIT-INDEX.md` and `AUDIT-PROGRESS.log` remain Master-owned.

## Page-by-page audit

### p.001 (PDF p.1 / printed p.17)

- PNG: `audit/Thom_1954_varietes_differentiables_p001.png` (150 dpi, 1-bit `pngmono`)
- Checked: journal running head and printed page number; title, author/affiliation, Introduction heading and first page of its opening paragraph; footnote 1 and its reference to bibliography item [28]. Compared against the matching opening text in the MinerU Markdown.
- Result: PASS± — article text, accents, author, note marker/text and paragraph continuation agree with print. Markdown omits the journal running head, page furniture and printed folio, and renders the page-spanning paragraph continuously; these are non-misleading layout omissions. The embedded OCR text layer misreads several characters on this page (for example `les` as `le8`, `existe` as `exi8te`, and `soit` as `80it`); the Markdown readings match the visible print.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.002 (PDF p.2 / printed p.18)

- PNG: `audit/Thom_1954_varietes_differentiables_p002.png` (150 dpi, 1-bit `pngmono`)
- Checked: continuation of the Introduction through its closing paragraph; Chapter I and section heading; notation paragraph and items 1–2 through the page break; footnotes 2 and 3. Compared the full printed page against the corresponding sequence in the MinerU Markdown.
- Result: PASS± — the mathematical notation and French prose on this page agree with print, including $M(SO(k))$, $M(O(k))$, $V^n$, $C^\infty$, the critical set/value definitions, the regular-value definition and both footnotes. The paragraph at the bottom continues on the next page as in print. Markdown omits the printed folio and page furniture; no content-level omission or misleading OCR reading was found.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.003 (PDF p.3 / printed p.19)

- PNG: `audit/Thom_1954_varietes_differentiables_p003.png` (150 dpi, 1-bit `pngmono`)
- Checked: continuation of section 2 from the preceding page; regular-value preimage and normal/transverse bundle discussion; concluding summary and Remark; opening of section 3 through its final line. Compared equations and prose with the corresponding passage in the MinerU Markdown.
- Result: PASS± — the page's equations and notation ($f^{-1}(y)$, $V_x/W_x$, $M_y$, $H_x$, $W^{n-p}$ and $M_y\approx\mathbb{R}^p$), statements and references agree with print. Markdown continues the page-spanning section without a content gap and omits only page furniture/printed folio.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.004 (PDF p.4 / printed p.20)

- PNG: `audit/Thom_1954_varietes_differentiables_p004.png` (150 dpi, 1-bit `pngmono`)
- Checked: continuation of Whitney's example; Theorems I.1–I.3 and their hypotheses; proof setup for Theorem I.3 through the final line; footnote 4 and its Sard reference. Compared theorem numbers, regularity indices, inequalities, names and prose with the print image and corresponding Markdown.
- Result: PASS± — the statements and proof setup agree with print, including $m\geq n$ in Theorems I.1–I.3 and the $C^n$ regularity in the proof setup. Footnote 4 is present and matches. Markdown omits the printed folio/page furniture; no content-level error was found.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.005 (PDF p.5 / printed p.21)

- PNG: `audit/Thom_1954_varietes_differentiables_p005.png` (150 dpi, 1-bit `pngmono`)
- Checked: end of the proof of Theorem I.3; compact exhaustion and meagre critical-value set argument; section 3 definition of a tubular neighborhood through the final line, including dimensions, fiber and structure group. Compared each displayed relation and statement with the page image and corresponding Markdown.
- Result: PASS± — the proof conclusion and tubular-neighborhood definition agree with print, including $\Sigma_i=K_i\cap\Sigma$, $p:T\to N^{p-q}$, the $q$-ball fibers, $(q-1)$-sphere boundary fibers and the subgroup of $O(q)$. Markdown omits the printed folio and page furniture; no content-level difference was found.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.006 (PDF p.6 / printed p.22)

- PNG: `audit/Thom_1954_varietes_differentiables_p006.png` (150 dpi, 1-bit `pngmono`)
- Checked: differentiable homeomorphisms of the closed ball and isotopies in $G$; definition/topology of tubular-neighborhood group $H$ and proof that $H$ is a Baire space; definition of a $t$-regular value through the page break. Compared set/fiber notation, differentiability orders, parameter interval and prose with the printed page.
- Result: PASS± — the page agrees with Markdown, including $B^q$, $S^{q-1}$, $A_0=A$, $A_1=\mathrm{id}$, the $C^n$ topology for $A$ and $A^{-1}$, and the Cauchy-limit argument for $J$ and $J^{-1}$. The definition continues on the following page as printed. Only page furniture/folio is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.007 (PDF p.7 / printed p.23)

- PNG: `audit/Thom_1954_varietes_differentiables_p007.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of the $t$-regular-value definition and footnote 5; section 4 inverse-image statement, coordinate equations and normal-bundle relation; local products $D,D'$ and the opening of Lemma I.4. Compared all displayed symbols and dimensions with the print image and the matching Markdown passage.
- Result: PASS± — notation and statements agree, including $M_y/N_y$, $f^{-1}(N^{p-q})=W^{n-q}$, $D=p^{-1}(X)$, $D'=p^{-1}(X')$, and the products with $B^q$. Footnote 5 is present. The lemma continues on the following page as printed; only page furniture/folio is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.008 (PDF p.8 / printed p.24)

- PNG: `audit/Thom_1954_varietes_differentiables_p008.png` (150 dpi, 1-bit `pngmono`)
- Checked: Lemma I.4 statement and explanation of non-$t$-regularity; definition of $i$-critical maps and $σ_i$; proof that $σ_i$ is closed and the first two neighborhood conditions through the page break. Compared quantified bounds, Jacobian minors and compositions with the print image and Markdown.
- Result: PASS± — the proof text and notation agree with print, including the $3B$ lower bound, the $>2B$ bound on $J$, the $>B$ bound for nearby $A'$, and the maps $k\circ A\circ f$ and $k\circ A'\circ f$. The proof continues on the following page; Markdown omits only the printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.009 (PDF p.9 / printed p.25)

- PNG: `audit/Thom_1954_varietes_differentiables_p009.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p009_300dpi-formula.png`; formula crop: `audit/300dpi/Thom_1954_varietes_differentiables_p009_formula_crop.png`.
- Checked: end of the closed-set argument; proof that the exceptional set has no interior; construction of the isotopy-supported homeomorphism $E$ and its displayed formula; extension by identity, perturbation $A'=E\circ A$, meagreness conclusion and countable cover setup through the page break. Compared the construction and quantifiers with the print image and Markdown.
- Result: PASS± — the 300 dpi crop confirms the print formula $E(y_1,z)=(y_1,G_{d(y)}(z))$, matching the Markdown; the construction and conclusions otherwise agree, including $G_0=G$, $G_1=\mathrm{id}$ and the arbitrarily small perturbation. The countable-cover discussion continues on the next page as printed; only page furniture/folio is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.010 (PDF p.10 / printed p.26)

- PNG: `audit/Thom_1954_varietes_differentiables_p010.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of the paracompact covering argument; Theorem I.5 statement and both conclusions; opening of section 5 (isotopy theorem), including compactness assumptions, local normal coordinates, tubular-neighborhood setup and the $t$-regularity argument through the page break. Compared theorem labels, dimensions, bundle relation and hypotheses with print and Markdown.
- Result: PASS± — Theorem I.5 and the isotopy setup agree with print, including the $C^n$ hypothesis, $\dim W=n-q$, the induced normal-bundle isomorphism, compactness of $V$ and $N$, and the finite coordinate cover. The next-page continuation is preserved in Markdown; only printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.011 (PDF p.11 / printed p.27)

- PNG: `audit/Thom_1954_varietes_differentiables_p011.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p011_300dpi-inequality.png`; crop: `audit/300dpi/Thom_1954_varietes_differentiables_p011_inequality_crop.png`.
- Checked: proof of the isotopy theorem from the estimate on $L$ through the unique-point and isotopy conclusions; Theorem I.6 and its hypotheses/conclusion. Compared the estimate, coordinate-system subscript, degree and inverse-image statements with the print image and Markdown.
- Result: FAIL — the 300 dpi crop confirms two Markdown OCR errors on this page: print has $\|L(z)-z\|<\varepsilon$, while Markdown has $\|L(z)-z\|\leq\varepsilon$; print has the coordinate system $(y_j)$, while Markdown says $(y_f)$. The remainder of the proof and Theorem I.6 agrees with print. Leave both fixes until all 70 pages have been audited.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.012 (PDF p.12 / printed p.28)

- PNG: `audit/Thom_1954_varietes_differentiables_p012.png` (150 dpi, 1-bit `pngmono`)
- Checked: Chapter II heading; §1 Poincaré and Poincaré–Veblen duality statements, fundamental classes and realization question; §2 setup of the closed subgroup $G\subset O(k)$, universal sphere bundle, mapping cylinder $A_G$ and open-bundle complement $A'_G$. Compared group/coefficient notation, dimensions and definitions against the print image and Markdown.
- Result: PASS± — the prose and notation agree with print, including $H_{n-k}$/$H^k$, coefficients $\mathbb{Z}$ and $\mathbb{Z}_2$, $S^{k-1}$ and the boundary/complement descriptions of $A_G$ and $A'_G$. The printed folio and page furniture are omitted; no content-level difference was found.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.013 (PDF p.13 / printed p.29)

- PNG: `audit/Thom_1954_varietes_differentiables_p013.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p013_300dpi-H0.png`; crop: `audit/300dpi/Thom_1954_varietes_differentiables_p013_H0_crop.png`.
- Checked: definition of $M(G)$; compact-support/relative cohomology isomorphism and fundamental class $U$; §3 realizability definition, Theorem II.1 statement and beginning of its necessary-condition proof. Compared coefficient groups, degree shifts and class notation against the print image.
- Result: FAIL — the 300 dpi crop shows print $H^0(B_G)$, while MinerU Markdown has $H^{o}(B_G)$ (lowercase letter o). The rest of the checked definitions, degree shifts, theorem and proof opening agree with print.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.014 (PDF p.14 / printed p.30)

- PNG: `audit/Thom_1954_varietes_differentiables_p014.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p014_300dpi-diagram.png`; diagram crop: `audit/300dpi/Thom_1954_varietes_differentiables_p014_diagram_crop.png`; proof-formula crop: `audit/300dpi/Thom_1954_varietes_differentiables_p014-proof-equation-crop.png`; lower-proof context crop: `audit/300dpi/Thom_1954_varietes_differentiables_p014_equation_crop.png`.
- Checked: commutative cohomology diagram (1), including both vertical Thom isomorphisms and degree-zero groups; proof identity $f^*(U)$; sufficient-condition argument through the construction of $F^{-1}(B_G)$. Compared the diagram edges, superscripts, maps and displayed identity against the 300 dpi crops and Markdown.
- Result: FAIL — print contains the right vertical map $\varphi_G^*:H^0(B_G)\to H^k(A_G,E_G)$, which is missing from the Markdown diagram; the diagram's two print labels $H^0(W^{n-k})$ and $H^0(B_G)$ are also rendered as $H^o$ in Markdown. The proof identity $f^*(U)=f\varphi_G^*(\omega_G)=j_*\varphi^*(\omega)=u$ matches print; no other content discrepancy was found in the checked span.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.015 (PDF p.15 / printed p.31)

- PNG: `audit/Thom_1954_varietes_differentiables_p015.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of the sufficient-condition proof for Theorem II.1; extension to noncompact paracompact varieties and Theorem II.1'; §4 trivial-normal-bundle/spherical-class discussion and Theorem II.2 through the final printed line. Compared the induced normal structure, $\Phi$-proper condition, sphere/cohomology notation and hypotheses against print and Markdown.
- Result: PASS± — the proof continuation, Theorem II.1', definition of a spherical class and Theorem II.2 agree with print. The page ends after the statement that no general necessary-and-sufficient condition is known; Markdown preserves the continuation and omits only the printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.016 (PDF p.16 / printed p.32)

- PNG: `audit/Thom_1954_varietes_differentiables_p016.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p016_300dpi-grassmannian.png`; Grassmannian/punctuation crop: `audit/300dpi/Thom_1954_varietes_differentiables_p016_grassmannian-crop.png`; punctuation detail: `audit/300dpi/Thom_1954_varietes_differentiables_p016_punctuation-crop.png`; lower-page context crop: `audit/300dpi/Thom_1954_varietes_differentiables_p016-theorem-reference-crop.png`.
- Checked: Theorems II.3–II.5'; hypotheses and coefficient groups; definitions/classifying spaces $G_k$, $\widehat G_k$, $B_{O(k)}$, $B_{SO(k)}$; double-cover statement; and the universal $E_{SO(k)}$ bundle construction through the page break. Compared notation and bounds with the print image and Markdown.
- Result: PASS± — theorem statements and dimensions agree with print. The 300 dpi punctuation crop confirms that the source itself prints a centered dot between $SO(k)$ and $\widehat G_k$; Markdown preserves that printed mark. The final word is divided across the page break in both source and Markdown; only folio/page furniture is otherwise omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.017 (PDF p.17 / printed p.33)

- PNG: `audit/Thom_1954_varietes_differentiables_p017.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p017_300dpi-formulas.png`; formula crops: `audit/300dpi/Thom_1954_varietes_differentiables_p017-cohomology-sequence-crop.png`, `audit/300dpi/Thom_1954_varietes_differentiables_p017-even-k-crop.png`, `audit/300dpi/Thom_1954_varietes_differentiables_p017-conclusion-crop.png`, and `audit/300dpi/Thom_1954_varietes_differentiables_p017-closing-formula-crop.png`.
- Checked: cohomology exact sequence (2); mod-2 Stiefel–Whitney calculation; odd/even $k$ mod-$p$ cases and the induced Pontrjagin-class map; final relative-cohomology conclusions and transition to $M(O(k))$. Compared superscripts, hats, parentheses, generators and bounds with the print images and Markdown.
- Result: FAIL — three OCR differences are confirmed: print has $H^{*}(\widehat G_k,\widehat G_{k-1})$ where Markdown omits the $*$; print has $H^{*}(\widehat G_k;Z_p)$ in the even-$k$ case while Markdown omits the hat; and print has $H^{*}(M(SO(k)))$ in the odd-$k$ conclusion while Markdown is missing the final closing parenthesis. The remaining checked statements and symbols agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.018 (PDF p.18 / printed p.34)

- PNG: `audit/Thom_1954_varietes_differentiables_p018.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p018_300dpi-ideals.png`; crops: `audit/300dpi/Thom_1954_varietes_differentiables_p018-mod2-ideal-crop.png`, `audit/300dpi/Thom_1954_varietes_differentiables_p018-ideal-symbol-crop.png`, and `audit/300dpi/Thom_1954_varietes_differentiables_p018-even-k-crop.png`.
- Checked: mod-2 relative-cohomology ideal and generators; mod-$p$ action of the deck transformation on Pontrjagin/fundamental classes; odd/even $k$ cases and ideals; fundamental groups and first nonzero homotopy groups. Compared symbol shape, pair notation and group subscripts with print and Markdown.
- Result: FAIL — the 300 dpi crop shows an uppercase $J$-shaped printed label for the mod-2 ideal, whereas Markdown has lowercase $\mathfrak{f}$. The relative-cohomology notation in the even-$k$ conclusion is printed with a semicolon and Markdown retains it. Remaining checked statements, including the $\pi_1$/$\pi_k$ conclusions, agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.019 (PDF p.19 / printed p.35)

- PNG: `audit/Thom_1954_varietes_differentiables_p019.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p019_300dpi-exact-sequence.png`; crop: `audit/300dpi/Thom_1954_varietes_differentiables_p019-sequence-crop.png`.
- Checked: Theorem II.6 and its exact sequence; relative homology/Hurewicz argument; Theorem II.7 suspension range; construction with $A'_{O(k-1)}\otimes I$ and the induced map through the page break. Compared the first sequence arrow label, degree/range inequalities, skeletons and bundle notation with print and Markdown.
- Result: PASS± — the sequence arrow is labeled $f$ in print and Markdown, and the hypotheses, $r\leq k$ bounds, vanishing ranges and suspension conclusion agree. The construction continues onto the next page as printed; only page furniture/folio is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.020 (PDF p.20 / printed p.36)

- PNG: `audit/Thom_1954_varietes_differentiables_p020.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p020_300dpi-suspension.png`; crop: `audit/300dpi/Thom_1954_varietes_differentiables_p020-suspension-sequence-crop.png`.
- Checked: transfer of the homotopy-range result; suspension construction and Freudenthal range; displayed chain of isomorphisms; §6 heading and Eilenberg–Mac Lane definition/finite-skeleton argument through the page break. Compared indices, parentheses, maps and ranges with print and Markdown.
- Result: FAIL — the 300 dpi crop confirms the final term of the displayed chain is $\pi_{k+i}(M(O(k)))$ in print, but Markdown is missing the final closing parenthesis after $M(O(k))$. The suspension bounds and remaining checked text agree; defer the edit until the complete 70-page audit is signed.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.021 (PDF p.21 / printed p.37)

- PNG: `audit/Thom_1954_varietes_differentiables_p021.png` (150 dpi, 1-bit `pngmono`)
- Checked: continuation of the finite-skeleton construction; Eilenberg–Mac Lane cohomology and Steenrod-square basis; odd-prime generators; Stiefel–Whitney description of $H^*(G_k;Z_2)$ and formula (3); footnote 6.
- Result: PASS± — the statements, inequalities, operations and displayed formula agree with print. Markdown contains the footnote text, but also an orphan standalone `N.` block after the complete footnote; the print has `N.` only once within “N. E. Steenrod.” This is a non-misleading OCR artifact. Printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.022 (PDF p.22 / printed p.38)

- PNG: `audit/Thom_1954_varietes_differentiables_p022.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p022_300dpi-lemma.png`; lemma/proof crop: `audit/300dpi/Thom_1954_varietes_differentiables_p022-lemma-proof-crop.png`; statement crop: `audit/300dpi/Thom_1954_varietes_differentiables_p022-lemma-statement-crop.png`; class-label detail: `audit/300dpi/Thom_1954_varietes_differentiables_p022-Hk-label-crop.png`.
- Checked: Lemma II.8 statement; lexicographic monomial order; leading-term induction; Cartan formula expansion and inequality bounds through the final line. Compared the class/cohomology labels, multiplication marks and operation indices with print and Markdown.
- Result: PASS± — formulae and inequalities agree. The high-resolution crop confirms the print's class label $W_k\in H^k(W_k;Z_2)$, matching Markdown; the source ideal label is a script/capital-$J$ glyph while Markdown uses $\mathcal{J}$, a non-misleading styling difference. Printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.023 (PDF p.23 / printed p.39)

- PNG: `audit/Thom_1954_varietes_differentiables_p023.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p023_300dpi-symbols.png`; ideal/formula crop: `audit/300dpi/Thom_1954_varietes_differentiables_p023-ideal-formula-crop.png`.
- Checked: linear-independence conclusion for Lemma II.8; symmetric-polynomial interpretation and ideal description; monomial sums (4)–(5); essential-permutation convention; opening definition of a dyadic variable through the page break. Compared the ideal label and exponent/monomial notation with print and Markdown.
- Result: FAIL — the 300 dpi crop shows the ideal label as an uppercase script/J-shaped $J$ in print, while Markdown uses $\mathcal{F}$. The stated cohomology group, generator $W_k$, formulas (4)–(5), and remaining checked text agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.024 (PDF p.24 / printed p.40)

- PNG: `audit/Thom_1954_varietes_differentiables_p024.png` (150 dpi, 1-bit `pngmono`)
- Checked: dyadic-variable definition and Lemma II.9; binomial-coefficient implication; preorder $(Q)$; classes and monomial formulas (6)–(8), including admissible-square indices and permutation convention through the final line. Compared exponents, summation ranges and symbols with the print image and Markdown.
- Result: PASS± — statements and formulas (6)–(8) agree with print. Formula (8) continues onto the next page as in the source; Markdown omits only the printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.025 (PDF p.25 / printed p.41)

- PNG: `audit/Thom_1954_varietes_differentiables_p025.png` (150 dpi, 1-bit `pngmono`)
- Checked: top-term argument for sums (8)–(9); dyadic/non-dyadic factor reasoning; extraction of the fixed non-dyadic factor; application of Lemma II.8' and the $h\geq2r$ bound through the page break. Compared index, exponent and summation notation with print and Markdown.
- Result: PASS± — the displayed terms, inequalities, permutation argument and linear-independence conclusion agree with print. The sentence invoking Lemma II.8' continues across the page break; Markdown preserves it and omits only folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.026 (PDF p.26 / printed p.42)

- PNG: `audit/Thom_1954_varietes_differentiables_p026.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p026_300dpi-product.png`; product/detail crop: `audit/300dpi/Thom_1954_varietes_differentiables_p026-product-crop.png`.
- Checked: completion of the independence argument; partition identity; product $Y$ and formula (10); mod-$p$ cohomology comparison; inverse map, Theorem II.10 and Corollary II.11. Compared factor exponents, product symbols, range bounds and homotopy indices against print and Markdown.
- Result: PASS± — theorem statements, indices and product factors agree. Formula (10)'s continuation begins with a printed `+ …`, and Markdown preserves that source mark; no correction inferred. Page furniture/folio is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.027 (PDF p.27 / printed p.43)

- PNG: `audit/Thom_1954_varietes_differentiables_p027.png` (150 dpi, 1-bit `pngmono`)
- Checked: Corollaries II.12–II.13; the $k=1$ projective-space description; the $k=2$ cohomology classes in dimensions 2–5; and the induced cohomology values of $F^*$ through the mapping-cylinder setup. Compared maps, coefficients, Steenrod operations and products against the page image and Markdown.
- Result: PASS± — the corollaries, low-dimensional class descriptions and displayed $F^*$ values agree with print. The mapping-cylinder argument continues onto the following page; Markdown omits only printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.028 (PDF p.28 / printed p.44)

- PNG: `audit/Thom_1954_varietes_differentiables_p028.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p028_300dpi-hurewicz.png`; crops: `audit/300dpi/Thom_1954_varietes_differentiables_p028-relative-hurewicz-crop.png` and `audit/300dpi/Thom_1954_varietes_differentiables_p028-hurewicz-crop.png`.
- Checked: relative cohomology/homology vanishing and Hurewicz conclusions; obstruction class and kernel statement; Pontrjagin-square and Bockstein calculation through the final mod-2 identity. Compared group indices, coefficients, signs and operations with print and Markdown.
- Result: PASS± — the calculations and conclusions agree. The print itself has the relative-group line in the visible form $\pi_4 K,M)=0$ (without an opening parenthesis), and Markdown preserves that source form. One coboundary formula renders $p$ bold in Markdown where the print is italic; this is a non-misleading style difference. No source content was normalized.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.029 (PDF p.29 / printed p.45)

- PNG: `audit/Thom_1954_varietes_differentiables_p029.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p029_300dpi-generators.png`; generator crop: `audit/300dpi/Thom_1954_varietes_differentiables_p029-generator-crop.png`.
- Checked: image of $F^*$ and Theorem II.14/necessary condition; the $k=3$ calculation of $F^*$ in dimensions 3–8; Theorem II.15 and the closing remark. Compared class labels, exponents, obstruction relation and dimension bound with print and Markdown.
- Result: PASS± — the displayed generators, obstruction relation and theorem bound agree. The 300 dpi crop confirms the printed superscript form $X^{22}$ as transcribed in Markdown; the page omits only folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.030 (PDF p.30 / printed p.46)

- PNG: `audit/Thom_1954_varietes_differentiables_p030.png` (150 dpi, 1-bit `pngmono`)
- Checked: nonexistence of a homotopy inverse for $k>1$; §8 stable-case discussion; Zilber complex construction, fiber/base, $k$-invariant and extension criterion. Compared ranges, coefficient groups, Steenrod-operation indices and theorem references with print and Markdown.
- Result: PASS± — the statements and notation agree with print through the final line. Markdown omits only running/page furniture; no content-level difference was found.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.031 (PDF p.31 / printed p.47)

- PNG: `audit/Thom_1954_varietes_differentiables_p031.png` (150 dpi, 1-bit `pngmono`)
- Checked: cohomology of the Zilber complex modulo 2, primes $p\geq5$ and $p=3$; induced map $F^3$, spectral-sequence differentials/transgression and listed generators; footnote 7. Compared coefficient groups, operation indices and degree shifts with print and Markdown.
- Result: PASS± — all stated generators, vanishing claims, maps and degrees agree with print through the page break. Markdown omits only printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.032 (PDF p.32 / printed p.48)

- PNG: `audit/Thom_1954_varietes_differentiables_p032.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p032_300dpi-mod2-table.png`; $i=1$ row crop: `audit/300dpi/Thom_1954_varietes_differentiables_p032-i1-row-crop.png`.
- Checked: construction of $F:M(SO(k))\to Y$; the cohomology product decomposition; the full mod-2 table for $i=0$ through $8$ and its coefficients/classes. Compared operation indices, products and all displayed row labels with print and Markdown.
- Result: PASS± — the table entries and displayed identities agree. The 300 dpi crop confirms the printed $i=1$ entry is literally $F^*(0)=0$, matching Markdown; this source wording is retained without reinterpretation. Only page furniture/folio is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.033 (PDF p.33 / printed p.49)

- PNG: `audit/Thom_1954_varietes_differentiables_p033.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p033_300dpi-mod5.png`; crop: `audit/300dpi/Thom_1954_varietes_differentiables_p033-mod5-footnote-crop.png`.
- Checked: mod-2 independence/basis conclusion; Steenrod operations for mod 3 and mod 5; coefficients and degree ranges; Theorems II.16–II.17; opening of §9 and footnote 8. Compared the end of the mod-5 formula with its footnote marker.
- Result: FAIL — print has $F^*(St_5^8\iota)=U\cdot((P_4)^2-2P_8)$ followed by superscript footnote marker $8)$ referring to the note below. Markdown instead absorbs that marker as an exponent and writes $U\cdot((P_4)^2-2P_8)^8$. Leave the correction until all 70 pages are audited.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.034 (PDF p.34 / printed p.50)

- PNG: `audit/Thom_1954_varietes_differentiables_p034.png` (150 dpi, 1-bit `pngmono`)
- Checked: small-$k$ cases $k=1,2,3$; projective-space descriptions; Zilber complex/invariant for $k=3$; mod-2/mod-3/$p\geq5$ image tables; Theorem II.18 through the page break. Compared group/class labels, dimensions, operations and coefficient fields with print and Markdown.
- Result: PASS± — the cases, formulas and theorem hypotheses agree with print through the page break; Markdown omits only running/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.035 (PDF p.35 / printed p.51)

- PNG: `audit/Thom_1954_varietes_differentiables_p035.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of the $k=3$ case and Theorem II.18; $k=4$ mod-2/mod-3/mod-$p$ image tables and Theorem II.19; multiplicative theorem II.20 and its Steenrod-power condition; definition of $F_N$ through the final printed line. Compared dimensions, coefficients and operation indices with print and Markdown.
- Result: PASS± — the cases, bounds, operation powers and hypotheses agree with print. The following-page continuation begins with Lemma II.21 in Markdown; only folio/page furniture is omitted here.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.036 (PDF p.36 / printed p.52)

- PNG: `audit/Thom_1954_varietes_differentiables_p036.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p036_300dpi-lemma21.png`; crop: `audit/300dpi/Thom_1954_varietes_differentiables_p036-lemma21-crop.png`.
- Checked: Lemmas II.21–II.23; exact-sequence maps and the $N',N''$ annihilation parameters; finite-group and torsion arguments; multiplication-by-$N$ sequence through the page break. Compared each domain/codomain and map index against the 300 dpi text and Markdown.
- Result: FAIL — print uses $(F_{N'})^*$ on $H^*(Z,k;G')$ and $(F_{N''})^*$ on $H^*(Z,k;G'')$. Markdown uses $(F_{N'})^*$ for both groups, replacing the second parameter $N''$ with $N'$. The remaining checked statements agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.037 (PDF p.37 / printed p.53)

- PNG: `audit/Thom_1954_varietes_differentiables_p037.png` (150 dpi, 1-bit `pngmono`)
- Checked: end of Lemma II.23; Lemma II.24 and its inductive obstruction-killing construction; application to $\widehat G_k$/$A_{SO(k)}$ and the real-cohomology $\mathcal{C}$-isomorphism/product description through the final line. Compared indices, maps, finite-type/finite-group conditions and class generators with print and Markdown.
- Result: PASS± — Lemma II.24, its induction, the Grassmannian application and product factors agree with print. The displayed product continues beyond the page; Markdown omits only folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.038 (PDF p.38 / printed p.54)

- PNG: `audit/Thom_1954_varietes_differentiables_p038.png` (150 dpi, 1-bit `pngmono`)
- Checked: application of Lemma II.24 to $\widehat G_k$; finite-type/cohomology hypotheses; construction of $G_q$ and the composite map; $N$-multiple realization Theorem II.25; extension to complex/symplectic Grassmannians; opening of §11. Compared ranges, coefficient/class labels and maps with print and Markdown.
- Result: PASS± — the hypotheses, maps, integers and theorem statement agree with print through the page break. Markdown omits only folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.039 (PDF p.39 / printed p.55)

- PNG: `audit/Thom_1954_varietes_differentiables_p039.png` (150 dpi, 1-bit `pngmono`)
- Checked: §§11 summary results; Theorems II.26–II.29 and their dimension/coefficient bounds; the printed main-text reference to note 9. Compared the homology groups, inequalities and theorem references against print and Markdown.
- Result: FAIL — the printed main text identifies $H_4(V^6;Z)$ as the simplest undecided group after Corollary II.28, while Markdown says $H_6(V^9;Z)$. The source’s following note is separate; this page’s main-text discrepancy must be corrected without moving the note’s content.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.040 (PDF p.40 / printed p.56)

- PNG: `audit/Thom_1954_varietes_differentiables_p040.png` (150 dpi, 1-bit `pngmono`)
- Checked: Corollary II.30; remarks on realizability/addition/intersection; differentiability-hypothesis discussion; footnote 9’s later dimension-6 result and $H_7(V^{10};Z)$ case. Compared theorem statements, operations and the footnote against print and Markdown.
- Result: PASS± — the checked prose and footnote agree with print. Markdown repeats $H_7(V^{10};Z)$ in a separate small block after the full footnote; this is a non-misleading OCR artifact. The main-text discrepancy from p.39 remains recorded there. Printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.041 (PDF p.41 / printed p.57)

- PNG: `audit/Thom_1954_varietes_differentiables_p041.png` (150 dpi, 1-bit `pngmono`)
- Checked: topological obstruction discussion and example; Chapter III Steenrod problem statement; definition/construction of neighborhoods $M^n,T^{n-1}$ and the associated variety through the $F_a$ embedding formula. Compared dimensions, homology maps and formula coordinates with print and Markdown.
- Result: PASS± — the problem statement, neighborhood construction, regular-value conditions and $F_a(x,t)$ formula agree with print through the page break. The printed folio/running furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.042 (PDF p.42 / printed p.58)

- PNG: `audit/Thom_1954_varietes_differentiables_p042.png` (150 dpi, 1-bit `pngmono`)
- Checked: deformation-retract remark; doubling construction and associated variety; induced homology/cohomology map; Theorem III.1 and sufficient-condition proof; necessary-condition setup with embeddings and mapping cylinder. Compared domains, dimensions, maps and segment parameter with print and Markdown.
- Result: PASS± — the construction, theorem statement and proof setup agree with print. The mapping-cylinder argument continues onto the next page; Markdown omits only page furniture/folio.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.043 (PDF p.43 / printed p.59)

- PNG: `audit/Thom_1954_varietes_differentiables_p043.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p043_300dpi-map.png`; map-formula crop: `audit/300dpi/Thom_1954_varietes_differentiables_p043-map-equation-crop.png`.
- Checked: mapping-cylinder embedding $F_a$ and its restriction to $K$; Theorems III.2–III.4; opening definition of the operators $\vartheta_i^p$. Compared coordinates, dimension bounds and theorem statements with print and Markdown.
- Result: PASS± — the maps and statements agree. The 300 dpi crop confirms the source literally prints $F_a(y)=(0,i(y),at)$; Markdown preserves that source form. The final definition continues on the next page; folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.044 (PDF p.44 / printed p.60)

- PNG: `audit/Thom_1954_varietes_differentiables_p044.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi terminal evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p044_300dpi-Q0.png`; crop: `audit/300dpi/Thom_1954_varietes_differentiables_p044-Q0-crop.png`.
- Checked: Poincaré-duality operator definition; even/odd-index operator relations; topological/naturality properties; dual $Q$ operators, summation formula and examples; footnote 10. Compared indices, domains/codomains and Bockstein notation with print and Markdown.
- Result: FAIL — the 300 dpi crop reads the identity convention as $Q^0=\mathrm{id}$ in print, while Markdown has $Q^{\circ}=\mathrm{id}$. The remaining checked maps, operations and formulas agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.045 (PDF p.45 / printed p.61)

- PNG: `audit/Thom_1954_varietes_differentiables_p045.png` (150 dpi, 1-bit `pngmono`)
- Checked: Poincaré-duality definition of $\vartheta_i^p$; Bockstein definition for odd indices; topological/naturality properties; dual $Q_p^i$ relations and examples; footnote 10. Compared operation indices, coefficients and Bockstein notation with print and Markdown.
- Result: PASS± — the operators, formulas and examples agree. Markdown has standalone small-text fragments $St_p^{2k(p-1)}$ and $P_p^k$ after the complete footnote, while print contains these tokens only within footnote 10; these are non-misleading OCR artifacts. Printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.046 (PDF p.46 / printed p.62)

- PNG: `audit/Thom_1954_varietes_differentiables_p046.png` (150 dpi, 1-bit `pngmono`)
- Checked: Corollary II.7; Lemma III.8 on the Steenrod composite; the product-of-lens-spaces computation; Theorem III.9 and the start of the $L^7$ example. Compared operation order, class degrees, coefficient groups and nonzero relation with print and Markdown.
- Result: PASS± — the lemma, displayed computation, dimension threshold and example setup agree with print. The example continues onto the next page; printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.047 (PDF p.47 / printed p.63)

- PNG: `audit/Thom_1954_varietes_differentiables_p047.png` (150 dpi, 1-bit `pngmono`)
- Checked: lens-space product example; class $X$ and its Steenrod/Bockstein pairing; non-realizability conclusion; Theorem III.10 and the topological-manifold question. Compared coefficient groups, products, operation indices and dimension statements with print and Markdown.
- Result: PASS± — the example, calculations, conclusions and open question agree with print. Markdown omits only printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.048 (PDF p.48 / printed p.64)

- PNG: `audit/Thom_1954_varietes_differentiables_p048.png` (150 dpi, 1-bit `pngmono`)
- Checked: Chapter IV opening definitions of an oriented boundary and cobordant varieties; induced boundary orientation; equivalence relation and addition setup through the page break. Compared dimensions, orientation reversal, boundary operator and quotient/identification language with print and Markdown.
- Result: PASS± — definitions and orientation conventions agree with print. The addition definition continues onto the next page; Markdown omits only running/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.049 (PDF p.49 / printed p.65)

- PNG: `audit/Thom_1954_varietes_differentiables_p049.png` (150 dpi, 1-bit `pngmono`)
- Checked: cobordism addition and ring structure; mod-2 cobordism classes; signature and Pontrjagin-number invariants (Theorems IV.1–IV.2) through the final line. Compared orientation reversal, group/ring notation, indices and characteristic numbers with print and Markdown.
- Result: PASS± — definitions, invariants and algebraic statements agree with print. The tensor-product explanation continues onto the next page; printed folio/running furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.050 (PDF p.50 / printed p.66)

- PNG: `audit/Thom_1954_varietes_differentiables_p050.png` (150 dpi, 1-bit `pngmono`)
- Checked: Theorem IV.3; definition of $t$-regular maps from a manifold with boundary; inverse-image manifold/boundary argument and local coordinate system. Compared the defining equations, coordinate count and boundary relation with print and Markdown.
- Result: FAIL — print defines the inverse image locally by $y_1=y_2=\cdots=y_q=0$ (and adds $t=0$ for the boundary), while Markdown says only $y_1=y_2=y_q=0$, omitting the intermediate equations. The remaining checked statements agree; defer the edit until the full audit is complete.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.051 (PDF p.51 / printed p.67)

- PNG: `audit/Thom_1954_varietes_differentiables_p051.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of the local half-space argument; induced orientation via the cap product; orientation compatibility of the preimage cobordism; Theorem IV.4 and its homotopy/cobordism conclusion. Compared coordinate domains, operators and hypotheses with print and Markdown.
- Result: PASS± — the continuation and orientation/cobordism statements agree with print. The preceding page’s omitted intermediate coordinate equations remain recorded as p.50’s FAIL and are not counted again here; printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.052 (PDF p.52 / printed p.68)

- PNG: `audit/Thom_1954_varietes_differentiables_p052.png` (150 dpi, 1-bit `pngmono`)
- Checked: mod-2 cobordism consequence; Lemma IV.5 smoothing of a continuous homotopy; piecewise reparameterization and variable-radius smoothing; application of the generic perturbation and isotopy theorems to prove Theorem IV.4 through the page break. Compared interval bounds, regularity claims and preimage/bordism relations with print and Markdown.
- Result: PASS± — the homotopy construction, intervals, regularity argument and cobordism conclusion agree with print. The proof continues on the next page; only folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.053 (PDF p.53 / printed p.69)

- PNG: `audit/Thom_1954_varietes_differentiables_p053.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of Theorem IV.4 proof; §4 construction of the canonical map $g:W^{n-k}\to\widehat G_k$, tubular map $F:N\to A_{SO(k)}$, its commutative diagram and extension to $f:V^n\to M(SO(k))$; homotopy invariance under embedding/metric changes. Compared all diagram objects and arrows with the print image and Markdown.
- Result: FAIL — print's commutative diagram contains both vertical fibrations: $p:N\to W^{n-k}$ and $p':A_{SO(k)}\to\widehat G_k$. The Markdown diagram includes only the left-hand $p$ arrow and omits the right-hand $p'$ arrow, although the adjacent prose names both fibrations. Other checked prose and maps agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.054 (PDF p.54 / printed p.70)

- PNG: `audit/Thom_1954_varietes_differentiables_p054.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p054-300dpi.png` (full page).
- Checked: Lemma IV.5' and its collar reparameterization; the isotopy between two embeddings; the tubular neighborhood and canonical map $F:N\to A_{SO(k)}$; extension over $V^n\times I$. Compared hypotheses, map notation, dimensions and the final paragraph against print and Markdown.
- Result: FAIL — the printed line-break word is “parallélisme” (“par paral- / lélisme —:”), while Markdown has “parallèlement.” in “Formons l'application canonique — par parallèlement.” The full-page 300 dpi scan resolves the word; the other checked statements and formulas agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.055 (PDF p.55 / printed p.71)

- PNG: `audit/Thom_1954_varietes_differentiables_p055.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of the embedding homotopy; definition of oriented $L$-equivalence, its boundary/orientation equations, mod-2 classes, the homology/cobordism implications and the addition law under the dimension bounds. Compared the displayed intersections, boundary sign, indices and concluding $[W]+[-W]$ argument with print and Markdown.
- Result: PASS± — the definition, equations and group-law discussion agree with print. Markdown omits the printed folio and running/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.056 (PDF p.56 / printed p.72)

- PNG: `audit/Thom_1954_varietes_differentiables_p056.png` (150 dpi, 1-bit `pngmono`)
- Checked: construction of the map $J$ from $L$-equivalence classes to homotopy classes; the homotopy induced by a bordism; injectivity via Theorem IV.4; the cohomotopy group condition and footnote 11 through the sum-preimage formula. Compared maps, inverse images, dimensions and cited footnote details with print and Markdown.
- Result: PASS± — the maps, hypotheses, injectivity argument and footnote agree with print. The final sum-preimage statement continues on the next page; Markdown omits printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.057 (PDF p.57 / printed p.73)

- PNG: `audit/Thom_1954_varietes_differentiables_p057.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p057-300dpi.png` (full page).
- Checked: surjectivity setup for $J$; the normalized representative, tubular neighborhood and two bundle-classification diagrams; homotopy lifting and the new embedding $i'$. Compared symbols, map labels, indices and the statement introducing the extension lemma with print and Markdown.
- Result: FAIL — in the first commutative diagram, print labels the lower-right space $\widehat G_k$, while Markdown has $\widehat G_{\kappa}$. The 300 dpi full-page scan confirms the printed subscript is Latin $k$; the other checked maps and hypotheses agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.058 (PDF p.58 / printed p.74)

- PNG: `audit/Thom_1954_varietes_differentiables_p058.png` (150 dpi, 1-bit `pngmono`)
- Checked: extension-lemma proof; the embedding $i'$ and induced map; Theorem IV.6 and its mod-2 analogue; applications to dimensions $n-1$ and $n-2$. Compared the extension dimension bound, map formulas, group-structure hypothesis, cohomology data and final equivalence statement with print and Markdown.
- Result: PASS± — the lemma, theorem, formulas and application agree with print. Markdown omits only printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.059 (PDF p.59 / printed p.75)

- PNG: `audit/Thom_1954_varietes_differentiables_p059.png` (150 dpi, 1-bit `pngmono`)
- Checked: the corollary and stable-skeleton consequence; §5 and Lemma IV.7 identifying $L_k(S^n)$ with $\Omega^k$; the surjectivity/injectivity proof and Theorem IV.8 statement. Compared dimension inequalities, boundary sign, cobordism group and stable homotopy indices with print and Markdown.
- Result: PASS± — the corollary, dimension bounds, cobordism argument and stable-group statement agree with print. The proof of Theorem IV.8 continues on the next page; Markdown omits printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.060 (PDF p.60 / printed p.76)

- PNG: `audit/Thom_1954_varietes_differentiables_p060.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p060-300dpi.png`; basis-index crop: `audit/300dpi/Thom_1954_varietes_differentiables_p060-index-crop.png`.
- Checked: completion of Theorem IV.8; the mod-2 cobordism group product and Theorem IV.9; the maps $F_\omega$, characteristic-class formulas $X_\omega$ and $Y_\omega$, and the basis notation at the page end. Compared indices, exponents, dimensions and coefficients with print and Markdown.
- Result: PASS± — the displayed product, characteristic-class formulas and basis label $f_{\omega^1}$ agree with print. The duality formula continues on the next page; printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.061 (PDF p.61 / printed p.77)

- PNG: `audit/Thom_1954_varietes_differentiables_p061.png` (150 dpi, 1-bit `pngmono`)
- Checked: dual-basis pairing and normal characteristic classes; equation (2); the converse of Pontrjagin's theorem, Theorem IV.10, Corollary IV.11 and the count of independent tangent characteristic numbers. Compared partition indices, pullbacks, Whitney relation and dimension/degree statements with print and Markdown.
- Result: PASS± — the pairings, characteristic-class relation and cobordism conclusions agree with print. The remark about Wu relations continues on the next page; Markdown omits printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.062 (PDF p.62 / printed p.78)

- PNG: `audit/Thom_1954_varietes_differentiables_p062.png` (150 dpi, 1-bit `pngmono`)
- Checked: completion of the Wu-relation remark; multiplicative structure of mod-2 cobordism; characteristic-number behavior of the product varieties; formulas (3) and (4), the Whitney-duality relation and the degree-filtering argument. Compared partition indices, factor dimensions and symmetric-polynomial terms with print and Markdown.
- Result: FAIL — Markdown inserts the standalone formula `$X_{\text{max}} = \sum_{n=1}^{N} (X_n)/(X_{n-1})$` between the sentence introducing a formula and printed formula (3). The printed page proceeds directly to $Y_\omega=\sum_{(\omega_1,\omega_2)}(Y_{\omega_1})(Y_{\omega_2})$ and contains no $X_{\text{max}}$ expression. The remaining checked formulas agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.063 (PDF p.63 / printed p.79)

- PNG: `audit/Thom_1954_varietes_differentiables_p063.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p063-300dpi.png`; Theorem IV.12 notation crop: `audit/300dpi/Thom_1954_varietes_differentiables_p063-theorem12-crop.png`.
- Checked: uniqueness of the partition decomposition and formula (5); Theorem IV.12 and its product corollary; the generators and characteristic numbers for dimensions 2–4. Compared partition indices, cobordism classes, ring/group symbols and representative manifolds with print and Markdown.
- Result: FAIL — Theorem IV.12 prints the ring and its graded groups using the script symbol $\mathfrak{N}$, but Markdown renders both occurrences as plain $N$ (“L'anneau N des groupes N^k”). The 300 dpi crop confirms the printed script glyph. The remaining checked formulas and examples agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.064 (PDF p.64 / printed p.80)

- PNG: `audit/Thom_1954_varietes_differentiables_p064.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p064-300dpi.png`; normal-characteristic, exception, and summand-index crops: `audit/300dpi/Thom_1954_varietes_differentiables_p064-normal-class-crop.png`, `audit/300dpi/Thom_1954_varietes_differentiables_p064-normal-exception-crop.png`, `audit/300dpi/Thom_1954_varietes_differentiables_p064-summand-index-crop.png`.
- Checked: examples in dimensions 5–8; the construction of a primitive class in every even dimension; its normal characteristic numbers and selected decomposable summands. Compared dimensions, generators and indices in the normal-characteristic formulas with print and Markdown.
- Result: FAIL — in the final construction, print uses $PR(n)+\bigcup_i V_{\omega_i}^{n}$, with indices $\omega_i$ for the selected non-dyadic partitions, while Markdown has $PR(n)+\bigcup_i V_{c_i}^{n}$. Print also gives the sole surviving normal characteristic number as $\Sigma(\bar t)^n$, while Markdown has $\Sigma(t)^n$ without the bar. The 300 dpi crops confirm both glyphs; the other checked examples and formulas agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.065 (PDF p.65 / printed p.81)

- PNG: `audit/Thom_1954_varietes_differentiables_p065.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p065-300dpi.png`; normal-character crop: `audit/300dpi/Thom_1954_varietes_differentiables_p065-normal-char-crop.png`; Stiefel–Whitney polynomial crop: `audit/300dpi/Thom_1954_varietes_differentiables_p065-stiefel-whitney-polynomial-crop.png`.
- Checked: normal/tangent characteristic-number duality; the Whitney relation and projective-space Stiefel–Whitney polynomial; Theorem IV.13 and Corollary IV.14. Compared bars on normal variables, polynomial terms, bordism groups and the Pontrjagin-number/index relation with print and Markdown.
- Result: FAIL — the printed normal characteristic number is $\Sigma(\bar t)^n$, while Markdown has $\Sigma(t)^n$ without the overbar. The 300 dpi crop confirms the bar; the duality relation, polynomial coefficients and cobordism statements otherwise agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.066 (PDF p.66 / printed p.82)

- PNG: `audit/Thom_1954_varietes_differentiables_p066.png` (150 dpi, 1-bit `pngmono`)
- 300 dpi evidence: `audit/300dpi/Thom_1954_varietes_differentiables_p066-300dpi.png`; torsion-definition, bottom-formula/footer, and footnote 12 crops: `audit/300dpi/Thom_1954_varietes_differentiables_p066-torsion-definition-crop.png`, `audit/300dpi/Thom_1954_varietes_differentiables_p066-torsion-crop.png`, `audit/300dpi/Thom_1954_varietes_differentiables_p066-footnote12-crop.png`.
- Checked: the rational cohomology product and map; Theorems IV.15 and IV.16; the torsion ideal and quotient; the order-2 bordism generator and footnote 12. Compared group symbols, the torsion definition, Betti-number/rank statement and Pontrjagin conclusion with print and Markdown.
- Result: FAIL — print ends the torsion-subgroup definition after “of $\Omega$.” and starts a new sentence “$\Omega^T$ is an ideal”; Markdown joins these as “of $\Omega\cdot\Omega^T$,” changing the sentence into a product. Footnote 12 also prints the script group symbol $\mathfrak N^4$, while Markdown has plain $N^4$. The 300 dpi crops confirm both differences; the other checked statements and formulas agree.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.067 (PDF p.67 / printed p.83)

- PNG: `audit/Thom_1954_varietes_differentiables_p067.png` (150 dpi, 1-bit `pngmono`)
- Checked: the rational cohomology identification and characteristic-number pairing; existence of a common integer multiple for prescribed values; the Pontrjagin-class basis and product formula (3') for characteristic numbers. Compared rational coefficients, dimensions, partition degrees and normal/tangent classification statements with print and Markdown.
- Result: PASS± — the pairings, integer-multiple claim, symmetric-polynomial basis and product formula agree with print. The decomposition argument continues on the next page; printed folio/page furniture is omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.068 (PDF p.68 / printed p.84)

- PNG: `audit/Thom_1954_varietes_differentiables_p068.png` (150 dpi, 1-bit `pngmono`)
- Checked: Theorem IV.17 and Corollary IV.18; the Chern-polynomial calculation for complex projective space and the primitive rational bordism generator; the opening remark on the dimension-8 Pontrjagin-number relations. Compared polynomial coefficients, characteristic-number sign, projective-space dimensions and congruence/equality formulas with print and Markdown.
- Result: PASS± — the generator argument, normal/tangent sign, integral-multiple conclusion and dimension-8 relations agree with print. The remark continues on the next page; Markdown omits printed folio/page furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.069 (PDF p.69 / printed p.85)

- PNG: `audit/Thom_1954_varietes_differentiables_p069.png` (150 dpi, 1-bit `pngmono`)
- Checked: continuation of the dimension-8 bordism argument and equation; bibliography entries [1]–[15]; footnote 13. Compared theorem symbols, coefficients, citation data and footnote wording with print and Markdown.
- Result: PASS± — the continuation, references and footnote agree in substance. Markdown has a minor punctuation difference in reference [15] (`Nederl, Akad.` versus printed `Nederl. Akad.`); the citation remains identifiable. The footnote appears inline in Markdown at the page/list break; printed folio and page furniture are omitted.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

### p.070 (PDF p.70 / printed p.86)

- PNG: `audit/Thom_1954_varietes_differentiables_p070.png` (150 dpi, 1-bit `pngmono`)
- Checked: bibliography entries [16]–[35] and the final publication information. Compared author names, titles, journal/volume/page data and the received date with print and Markdown.
- Result: FAIL — the bibliography entries match in substance, but the printed final line “(Reçu le 16 mai 1953)” is absent from Markdown. This is the paper's received date, not running or folio furniture.
- Actor: Peer-P29; model=gpt-6-luna; effort=max.

## Manual repair and final reread

The per-page FAIL grades above record the pre-repair comparison. The following register records the corrections made afterward.

- Target Markdown SHA-256 before repair: f9629851b3ef07022f07344aad94d370e3c5ad3ace3f9b5ea6d7b5ed4acbff4c.
- Repair commit: a67853c36e2ee23ef916234b259ebe00cde60c05.
- Target Markdown SHA-256 after repair: a68352fec8e7a531e5f35dde74220d9124f3e1f8e39d6441c8c9d0e40eaa4b0f.
- The final Markdown was reread from beginning to end and compared with the page audit findings and their cited print images. git diff --check passed, and a read-only search found none of the audited erroneous fragments.

| PDF page | Manual correction |
| --- | --- |
| 11 | Changed $\leq\varepsilon$ to $<\varepsilon$ and coordinate $(y_f)$ to $(y_j)$. |
| 13 | Corrected $H^{o}(B_G)$ to $H^0(B_G)$. |
| 14 | Corrected both $H^o$ labels to $H^0$ and restored the right vertical map $\varphi_G^*$. |
| 17 | Restored the relative-cohomology superscript $*$, the hat on $\widehat G_k$, and the closing parenthesis in $H^*(M(SO(k)))$. |
| 18 | Corrected the mod-2 ideal label from $\mathfrak f$ to $\mathcal J$. |
| 20 | Restored the closing parenthesis in the final homotopy-group term. |
| 23 | Corrected the mod-2 ideal label from $\mathcal F$ to $\mathcal J$. |
| 33 | Removed the false exponent 8 and represented 8) as a separate footnote marker. |
| 36 | Changed the second map's parameter from $N'$ to $N''$. |
| 39 | Corrected the undecided group from $H_6(V^9;Z)$ to $H_4(V^6;Z)$. |
| 44 | Corrected $Q^{\circ}$ to $Q^0$. |
| 50 | Restored the omitted intermediate local equations: $y_1=y_2=\cdots=y_q=0$. |
| 53 | Restored the right vertical fibration $p':A_{SO(k)}\to\widehat G_k$ in the diagram. |
| 54 | Corrected “parallèlement” to “parallélisme”. |
| 57 | Corrected the diagram's lower-right space from $\widehat G_{\kappa}$ to $\widehat G_k$. |
| 62 | Removed the standalone $X_{\text{max}}$ formula absent from print. |
| 63 | Restored the script notation $\mathfrak N$ for the ring and graded groups in Theorem IV.12. |
| 64 | Corrected $V_{c_i}^{n}$ to $V_{\omega_i}^{n}$ and restored the bar in $\Sigma(\bar t)^n$. |
| 65 | Restored the bar in the normal characteristic number $\Sigma(\bar t)^n$. |
| 66 | Separated the sentence after $\Omega$ and restored $\mathfrak N$ notation in footnote 12. |
| 70 | Added the printed received date, “Reçu le 16 mai 1953”. |

- Actor: Peer-P29; model=gpt-6-luna; effort=max.
- The PASS± punctuation note on p.69 remains a nonmisleading bibliographic abbreviation difference; it was not changed.
