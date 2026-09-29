# LORENTZIAN POLYNOMIALS

## PETTER BRAND <sup>¨</sup> EN AND JUNE HUH<sup>´</sup>

ABSTRACT. We study the class of Lorentzian polynomials. The class contains homogeneous stable polynomials as well as volume polynomials of convex bodies and projective varieties. We prove that the Hessian of a nonzero Lorentzian polynomial has exactly one positive eigenvalue at any point on the positive orthant. This property can be seen as an analog of the Hodge–Riemann relations for Lorentzian polynomials.

Lorentzian polynomials are intimately connected to matroid theory and negative dependence properties. We show that matroids, and more generally M-convex sets, are characterized by the Lorentzian property, and develop a theory around Lorentzian polynomials. In particular, we provide a large class of linear operators that preserve the Lorentzian property and prove that Lorentzian measures enjoy several negative dependence properties. We also prove that the class of tropicalized Lorentzian polynomials coincides with the class of M-convex functions in the sense of discrete convex analysis. The tropical connection is used to produce Lorentzian polynomials from M-convex functions.

We give two applications of the general theory. First, we prove that the homogenized multi-variate Tutte polynomial of a matroid is Lorentzian whenever the parameter q satisfies 0$< q \leqslant 1$ Consequences are proofs of the strongest Mason’s conjecture from 1972 and negative dependence properties of the random cluster model in statistical physics. Second, we prove that the multivariate characteristic polynomial of an M-matrix is Lorentzian. This refines a result of Holtz who proved that the coefficients of the characteristic polynomial of an M-matrix form an ultra log-concave sequence.

## CONTENTS

1. Introduction 2  
2. Basic theory 6  
2.1. The space of Lorentzian polynomials 6  
2.2. Hodge-Riemann relations for Lorentzian polynomials 15  
2.3. Independence and negative dependence 17  
2.4. Characterizations of Lorentzian polynomials 22  
3. Advanced theory 26  
3.1. Linear operators preserving Lorentzian polynomials 26  
3.2. Matroids, M-convex sets, and Lorentzian polynomials 31  
3.3. Valuated matroids, M-convex functions, and Lorentzian polynomials 33

4. Examples and applications 42  
4.1. Convex bodies and Lorentzian polynomials 42  
4.2. Projective varieties and Lorentzian polynomials 45  
4.3. Potts model partition functions and Lorentzian polynomials 47  
4.4. M-matrices and Lorentzian polynomials 50  
4.5. Lorentzian probability measures 55  
References 57

## 1. INTRODUCTION

Let$\mathrm { H } _ { n } ^ { d }$be the space of degree d homogeneous polynomials in n variables with real coefficients. Inspired by Hodge’s index theorem for projective varieties, we introduce a class of polynomials with remarkable properties. Let$\mathring { \mathrm { L } } _ { n } ^ { 2 } \subseteq \mathrm { H } _ { n } ^ { 2 }$be the open subset of quadratic forms with positive coefficients that have the Lorentzian signature$( + , - , \ldots , - )$. For d larger than 2, we define an open subset$\mathring { \mathrm { L } } _ { n } ^ { d } \subseteq \mathrm { H } _ { n } ^ { d }$by setting

$$
\mathring {\mathrm{L}} _ {n} ^ {d} = \left\{f \in \mathrm{H} _ {n} ^ {d} \mid \partial_ {i} f \in \mathring {\mathrm{L}} _ {n} ^ {d - 1} \text {   for   all   } i \right\},
$$

where$\partial _ { i }$is the partial derivative with respect to the i-th variable. Thus$f$belongs to$\mathring { \mathrm { L } } _ { n } ^ { d }$if and only if all polynomials of the form$\partial _ { i _ { 1 } } \partial _ { i _ { 2 } } \cdot \cdot \cdot \partial _ { i _ { d - 2 } } f$belongs to${ \dot { \mathrm { L } } } _ { n } ^ { 2 }$. The polynomials in$\mathring { \mathrm { L } } _ { n } ^ { d }$are called strictly Lorentzian, and the limits of strictly Lorentzian polynomials are called Lorentzian. We show that the class of Lorentzian polynomials contains the class of homogeneous stable polynomials (Section 2.1) as well as volume polynomials of convex bodies and projective varieties (Sections 4.1 and 4.2).

Lorentzian polynomials link discrete and continuous notions of convexity. Let$\mathrm { L } _ { n } ^ { 2 } \subseteq \mathrm { H } _ { n } ^ { 2 }$be the closed subset of quadratic forms with nonnegative coefficients that have at most one positive eigenvalue, which is the closure of${ \bar { \mathrm { L } } } _ { n } ^ { 2 }$in$\mathrm { H } _ { n } ^ { 2 }$. We write supp$( f ) \subseteq \mathbb { N } ^ { n }$for the support of$f \in \mathrm { H } _ { n } ^ { d } ,$ the set of monomials appearing in$f$with nonzero coefficients. For d larger than 2, we define $\mathrm { L } _ { n } ^ { d } \subseteq \mathrm { H } _ { n } ^ { d }$by setting

$$
\mathrm{L} _ {n} ^ {d} = \left\{f \in \mathrm{M} _ {n} ^ {d} \mid \partial_ {i} f \in \mathrm{L} _ {n} ^ {d - 1} \text {   for   all   } i \right\},
$$

where$\mathrm { M } _ { n } ^ { d } \subseteq \mathrm { H } _ { n } ^ { d }$is the set of polynomials with nonnegative coefficients whose supports are Mconvex in the sense of discrete convex analysis [Mur03]: For any index i and any$\alpha , \beta \in \mathsf { s u p p } ( f )$ whose i-th coordinates satisfy$\alpha _ { i } > \beta _ { i . }$, there is an index$j$satisfying

$$
\alpha_ {j} <   \beta_ {j} \text {   and   } \alpha - e _ {i} + e _ {j} \in \operatorname{supp} (f) \text {   and   } \beta - e _ {j} + e _ {i} \in \operatorname{supp} (f),
$$

where$e _ { i }$is the i-th standard unit vector in$\mathbb { N } ^ { n }$. Since$f \in \mathbf { M } _ { n } ^ { d }$implies$\partial _ { i } f \in \mathrm { M } _ { n } ^ { d - 1 }$, we have

$$
\mathrm{L} _ {n} ^ {d} = \left\{f \in \mathrm{M} _ {n} ^ {d} \mid \partial_ {i _ {1}} \partial_ {i _ {2}} \dots \partial_ {i _ {d - 2}} f \in \mathrm{L} _ {n} ^ {2} \text {for all} i _ {1}, i _ {2}, \dots , i _ {d - 2} \right\}.
$$

Our central result states that$\mathrm { L } _ { n } ^ { d }$is the set of Lorentzian polynomials in$\mathrm { H } _ { n } ^ { d }$(Theorem 2.25). To show that$\mathrm { L } _ { n } ^ { d }$is contained in the closure of${ \overset { \circ } { \operatorname { L } } } { } _ { n } ^ { d } ,$we construct a Nuij-type homotopy for$\mathrm { L } _ { n } ^ { d }$in Section 2.1. The construction is used in Section 2.2 to prove that all polynomials in$\mathrm { L } _ { n } ^ { d }$satisfy a formal version of the Hodge–Riemann relations: The Hessian of any nonzero polynomial in$\mathrm { L } _ { n } ^ { d }$has exactly one positive eigenvalue at any point on the positive orthant. To show that $\mathrm { L } _ { n } ^ { d }$contains the closure of${ \overset { \circ } { \operatorname { L } } } { } _ { n } ^ { d } ,$we develop the theory of c-Rayleigh polynomials in Section 2.3. Since homogeneous stable polynomials are Lorentzian, the latter inclusion generalizes a result of Choe et$a l .$that the support of any homogenous multi-affine stable polynomial is the set of bases of a matroid [COSW04]. In Section 2.4, we use the above results to show that the classes of strongly log-concave [Gur09], completely log-concave [AOVI], and Lorentzian polynomials are identical for homogeneous polynomials (Theorem 2.30). This enables us to affirmatively answer two questions of Gurvits on strongly log-concave polynomials (Corollaries 2.31 and 2.32).

Lorentzian polynomials are intimately connected to matroid theory and discrete convex analysis. We show that matroids, and more generally M-convex sets, are characterized by the Lorentzian property. Let$\mathbb { P } \mathrm { H } _ { n } ^ { d }$be the projectivization of the vector space$\mathrm { H } _ { n . } ^ { d }$, and let$\mathrm { L _ { J } }$be the set of polynomials in$\mathrm { L } _ { n } ^ { d }$with nonempty support J. We denote the images of$\mathrm { L } _ { n } ^ { d } , \mathring { \mathrm { L } } _ { n } ^ { d } ,$, and$\mathrm { L _ { J } }$in$\mathbb { P } \mathrm { H } _ { n } ^ { d }$ by$\mathbb { P } \mathrm { L } _ { n } ^ { d } , \mathbb { P } \mathrm { L } _ { n } ^ { d }$, and$\mathbb { P } \mathrm { L } _ { \mathrm { J } }$respectively, and write

$$
\mathbb {P} \mathrm{L} _ {n} ^ {d} = \coprod_ {\mathrm{J}} \mathbb {P} \mathrm{L} _ {\mathrm{J}},
$$

where the union is over all nonempty M-convex subsets of the d-th discrete simplex in$\mathbb { N } ^ { n }$. The space$\mathbb { P } \mathrm { L } _ { n } ^ { d }$is homeomorphic to the intersection of$\mathrm { L } _ { n } ^ { d }$with the unit sphere in$\mathrm { H } _ { n } ^ { d }$for the Euclidean norm on the coefficients. We prove that$\mathbb { P } \mathrm { L } _ { n } ^ { d }$is a compact contractible set with contractible interior$\mathbb { P } \mathring { \mathrm { L } } _ { n } ^ { d }$(Theorem 2.28).<sup>1</sup> In addition, we show that$\mathbb { P } \mathrm { L } _ { \mathrm { J } }$is nonempty and contractible for every nonempty M-convex set J (Theorem 3.10 and Proposition 3.25). Similarly, writing$\underline { { \mathrm { H } } } _ { n } ^ { d }$ for the space of multi-affine degree d homogeneous polynomials in n variables and$\underline { { \mathrm { L } } } _ { n } ^ { d }$for the corresponding set of multi-affine Lorentzian polynomials, we have

$$
\mathbb {P} \underline {{\mathrm{L}}} _ {n} ^ {d} = \coprod_ {\mathrm{B}} \mathbb {P} \underline {{\mathrm{L}}} _ {\mathrm{B}},
$$

where the union is over all rank d matroids on the n-element set$[ n ]$. The space$\mathbb { P } \underline { { \mathrm { L } } } _ { n } ^ { d }$is compact and contractible, and$\mathbb { P } \underline { { \mathrm { L } } } _ { \mathrm { B } }$is nonempty and contractible for every matroid B (Remark 3.6). The latter fact contrasts the case of stable polynomials. For example, there is no stable polynomial whose support is the set of bases of the Fano plane [Bra07 ¨ ].

In Section 3.1, we describe a large class of linear operators preserving the class of Lorentzian polynomials, thus providing a toolbox for working with Lorentzian polynomials. We give a Lorentzian analog of a theorem of Borcea and Brand ¨ en for stable polynomials [ ´ BB09], who characterized linear operators preserving stable polynomials (Theorem 3.2). It follows from our result that any homogeneous linear operator that preserves stable polynomials and polynomials with nonnegative coefficients also preserves Lorentzian polynomials (Theorem 3.4).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">PL<sup>d</sup><sub>n</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>We conjecture that is homeomorphic to the closed Euclidean ball of the same dimension (Conjecture 2.29).</span></small>

In Section 3.3, we strengthen the connection between Lorentzian polynomials and discrete convex analysis. For a function$\nu : \mathbb { N } ^ { n }  \mathbb { R } \cup \{ \infty \}$, we write dom$. ( \nu ) \subseteq \mathbb { N } ^ { n }$for the effective domain of$\nu ,$the subset of$\mathbb { N } ^ { n }$where ν is finite. For a positive real parameter$q ,$we consider the generating function

$$
f _ {q} ^ {\nu} (w) = \sum_ {\alpha \in \operatorname{dom} (\nu)} \frac {q ^ {\nu (\alpha)}}{\alpha !} w ^ {\alpha}, \quad w = (w _ {1}, \dots , w _ {n}).
$$

The main result here is Theorem$3 . 1 4 ,$which states that$f _ { q } ^ { \nu }$is a Lorentzian polynomial for all $0 \textless q \textless 1$if and only if the function$\nu$is M-convex in the sense of discrete convex analysis [Mur03]: For any index i and any$\alpha , \beta \in \mathsf { d o m } ( \nu )$whose i-th coordinates satisfy$\alpha _ { i } > \beta _ { i }$, there is an index$j$satisfying

$$
\alpha_ {j} <   \beta_ {j} \text { and } \nu (\alpha) + \nu (\beta) \geqslant \nu (\alpha - e _ {i} + e _ {j}) + \nu (\beta - e _ {j} + e _ {i}).
$$

In particular,$\mathbf { J } \subseteq \mathbb { N } ^ { n }$is M-convex if and only if its exponential generating function$\textstyle \sum _ { \alpha \in \mathrm { J } } { \frac { 1 } { \alpha ! } } w ^ { \alpha }$is a Lorentzian polynomial (Theorem 3.10). Another special case of Theorem 3.14 is the statement that a homogeneous polynomial with nonnegative coefficients is Lorentzian if the natural logarithms of its normalized coefficients form an M-concave function (Corollary 3.16). Working over the field of formal Puiseux series$\mathbb { K } ,$we show that the tropicalization of any Lorentzian polynomial over K is an M-convex function, and that all M-convex functions are limits of tropicalizations of Lorentzian polynomials over K (Corollary 3.28). This generalizes a result of Brand ¨ en´ [Bra10¨ ], who showed that the tropicalization of any homogeneous stable polynomial over K is M-convex.<sup>2</sup> In particular, for any matroid M with the set of bases${ \mathrm { B } } ,$the Dressian of all valuated matroids on M can be identified with the tropicalization of the space of Lorentzian polynomials over K with support B.

In Sections 4.1 and$4 . 2 ,$we show that the volume polynomials of convex bodies and projective varieties are Lorentzian. It follows that, for any convex bodies$\mathrm { K } _ { 1 } , \ldots , \mathrm { K } _ { n }$in$\mathbb { R } ^ { d }$, the set of all $\alpha \in \mathbb { N } ^ { n }$satisfying the conditions

$$
\alpha_ {1} + \dots + \alpha_ {n} = d \text { and } V (\underbrace {\mathrm{K} _ {1} , \ldots , \mathrm{K} _ {1}} _ {\alpha_ {1}}, \ldots , \underbrace {\mathrm{K} _ {n} , \ldots , \mathrm{K} _ {n}} _ {\alpha_ {n}}) \neq 0
$$

is M-convex, where the symbol$V$stands for the mixed volume of convex bodies in$\mathbb { R } ^ { d }$. Similarly, for any d-dimensional projective variety$Y$and any nef divisors$\mathrm { H } _ { 1 } , \ldots , \mathrm { H } _ { n }$on$Y ,$the set of all $\alpha \in \mathbb { N } ^ { n }$satisfying the conditions

$$
\alpha_ {1} + \dots + \alpha_ {n} = d \text {and} (\underbrace {\mathrm{H} _ {1} \cdot \ldots \cdot \mathrm{H} _ {1}} _ {\alpha_ {1}} \cdot \ldots \cdot \underbrace {\mathrm{H} _ {n} \cdot \ldots \cdot \mathrm{H} _ {n}} _ {\alpha_ {n}}) \neq 0
$$

is M-convex, where the symbol ¨ stands for the intersection product of Cartier divisors on$Y .$ The problem of finding a Lorentzian polynomial that is not a volume polynomial remains open. For a precise formulation, see Question 4.9.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>In [Bra10 ¨ ], the field of formal Puiseux series with real exponents was used. The tropicalization used in [Bra10 ¨ ] differs from ours by a sign.</span></small>

In Section 4.3, we use the basic theory developed in Section 2 to show that the homogenized multivariate Tutte polynomial of any matroid is Lorentzian. We use the Lorentzian property to prove a conjecture of Mason from 1972 on the enumeration of independent sets [Mas72]: For any matroid M on rns and any positive integer$k ,$

$$
\frac {I _ {k} (\mathrm{M}) ^ {2}}{\binom {n} {k} ^ {2}} \geqslant \frac {I _ {k + 1} (\mathrm{M})}{\binom {n} {k + 1}} \frac {I _ {k - 1} (\mathrm{M})}{\binom {n} {k - 1}},
$$

where$I _ { k } ( \mathrm { M } )$is the number of k-element independent sets of M. More generally, the Lorentzian property reveals several inequalities satisfied by the coefficients of the classical Tutte polynomial

$$
\mathrm{T} _ {\mathrm{M}} (x, y) = \sum_ {A \subseteq [ n ]} (x - 1) ^ {\mathrm{rk} _ {\mathrm{M}} ([ n ]) - \mathrm{rk} _ {\mathrm{M}} (A)} (y - 1) ^ {| A | - \mathrm{rk} _ {\mathrm{M}} (A)},
$$

where$\mathbf { r k } _ { \mathrm { M } } : \{ 0 , 1 \} ^ { n }  \mathbb { N }$is the rank function of M. For example, if we write

$$
w ^ {\mathrm{rk} _ {\mathrm{M}} ([ n ])} \mathrm{T} _ {\mathrm{M}} \left(1 + \frac {q}{w}, 1 + w\right) = \sum_ {k = 0} ^ {n} c _ {q} ^ {k} (\mathrm{M}) w ^ {k},
$$

then the sequence$c _ { q } ^ { k } ( \mathrm { M } )$is ultra log-concave for every$0 \leqslant q \leqslant 1 . ^ { 3 }$

In Section 4.4, we show that the multivariate characteristic polynomial of any M-matrix is Lorentzian.<sup>4</sup> This strengthens a theorem of Holtz [Hol05], who proved that the coefficients of the characteristic polynomial of any M-matrix form an ultra log-concave sequence.

In Section 4.5, we define a class of discrete probability measures, called Lorentzian measures, properly containing the class of strongly Rayleigh measures studied in [BBL09]. We show that Lorentzian measures enjoy several negative dependence properties and prove that the class of Lorentzian measures is closed under the symmetric exclusion process. As an example, we show that the uniform measure$\mu _ { \mathrm { M } }$on$\{ 0 , 1 \} ^ { n }$concentrated on the independent sets of a matroid M on rns is Lorentzian (Proposition 4.25). A conjecture of Kahn [Kah00] and Grimmett–Winkler [GW04] states that, for any graphic matroid M and distinct elements i and$j ,$

$$
\operatorname * {P r} (F \text {   contains   } i \text {   and   } j) \leqslant \operatorname * {P r} (F \text {   contains   } i) \operatorname * {P r} (F \text {   contains   } j),
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Nima Anari, Kuikui Liu, Shayan Oveis Gharan and Cynthia Vinzant have independently developed methods that partially overlap with our work in a series of papers [AOVI, ALOVII, ALOVIII]. They study the class of completely log-concave polynomials. For homogenous polynomials this class agrees with the class of Lorentzian polynomials, see Theorem 2.30 in this paper. The main overlap is an independent proof of Mason’s conjecture in [ALOVIII]. The man uscript [BH], which is not intended for publication, contains a short self-contained proof of Mason’s conjecture which was published on arXiv simultaneously as [ALOVIII]. In addition, the authors of [AOVI] prove that the basis generating polynomial of any matroid is completely log-concave, using results of Adiprasito, Huh, and Katz [AHK18]. An equiva lent statement on the Hessian of the basis generating polynomial can be found in [HW17, Remark 15]. A self-contained proof of the complete log-concavity of the basis generating polynomial, based on an implication similar to ofp3q ñ p1q Theorem 2.30 in this paper, appears in [ALOVII, Section 5.1]. The authors of [ALOVII] apply these results to design an FPRAS to count the number of bases of any matroid given by an independent set oracle, and to prove the conjecture of Mihail and Vazirani that the bases exchange graph of any matroid has expansion at least 1.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>An nˆn matrix is an M-matrix if all the off-diagonal entries are nonpositive and all the principal minors are positive. The class of M-matrices shares many properties of hermitian positive definite matrices and appears in mathematical economics and computational biology [BP94].</span></small>

where$F$is an independent set of M chosen uniformly at random. The Lorentzian property of the measure$\mu _ { \mathrm { M } }$shows that, for any matroid M and distinct elements i and$j ,$4

$$
\operatorname * {P r} (F \text {   contains   } i \text {   and   } j) \leqslant 2 \operatorname * {P r} (F \text {   contains   } i) \operatorname * {P r} (F \text {   contains   } j),
$$

where F is an independent set of M chosen uniformly at random.

Acknowledgments. Petter Brand ¨ en is a Wallenberg Academy Fellow supported by the Knut ´ and Alice Wallenberg Foundation and Vetenskapsradet. June Huh was supported by NSF Grant ˚ DMS-1638352 and the Ellentuck Fund. Special thanks${ \bf g 0 }$to anonymous referees, Claus Scheiderer’s reading group, Jonathan Leake, and Yanxin Liu, whose valuable comments significantly improved the quality of the paper.

## 2. BASIC THEORY

2.1. The space of Lorentzian polynomials. Let n and d be nonnegative integers, and set$[ n ] =$ $\{ 1 , \ldots , n \}$. We write$\mathrm { H } _ { n } ^ { d }$for the set of degree d homogeneous polynomials in$\mathbb { R } [ w _ { 1 } , \dots , w _ { n } ]$ We define a topology on$\mathrm { H } _ { n } ^ { d }$using the Euclidean norm for the coefficients, and write$\mathrm { P } _ { n } ^ { d } \subseteq \mathrm { H } _ { n } ^ { d }$ for the open subset of polynomials all of whose coefficients are positive. The Hessian of$f \in$ $\mathbb { R } [ w _ { 1 } , \dots , w _ { n } ]$is the symmetric matrix

$$
\mathcal {H} _ {f} (w) = \left(\partial_ {i} \partial_ {j} f\right) _ {i, j = 1} ^ {n},
$$

where$\partial _ { i }$stands for the partial derivative$\frac { \partial } { { \partial } w _ { i } }$. For$\alpha \in \mathbb { N } ^ { n }$, we write

$$
\alpha = \sum_ {i = 1} ^ {n} \alpha_ {i} e _ {i} \text { and } | \alpha | _ {1} = \sum_ {i = 1} ^ {n} \alpha_ {i},
$$

where$\alpha _ { i }$is a nonnegative integer and$e _ { i }$is the standard unit vector in$\mathbb { N } ^ { n }$, and set

$$
w ^ {\alpha} = w _ {1} ^ {\alpha_ {1}} \dots w _ {n} ^ {\alpha_ {n}} \text { and } \partial^ {\alpha} = \partial_ {1} ^ {\alpha_ {1}} \dots \partial_ {n} ^ {\alpha_ {n}}.
$$

We define the d-th discrete simplex$\Delta _ { n } ^ { d } \subseteq \mathbb { N } ^ { n }$by

$$
\Delta_ {n} ^ {d} = \Bigl \{\alpha \in \mathbb {N} ^ {n} \mid | \alpha | _ {1} = d \Bigr \},
$$

and define the Boolean cube$\{ 0 , 1 \} ^ { n } \subseteq \mathbb { N } ^ { n }$by

$$
\{0, 1 \} ^ {n} = \left\{\sum_ {i \in S} e _ {i} \in \mathbb {N} ^ {n} \mid S \subseteq [ n ] \right\}.
$$

The intersection of the d-th discrete simplex and the Boolean cube will be denoted

$$
\left[ \begin{array}{c} n \\ d \end{array} \right] = \{0, 1 \} ^ {n} \cap \Delta_ {n} ^ {d}.
$$

The cardinality of$\textstyle { \left[ { \begin{array} { l } { n } \\ { d } \end{array} } \right] }$is the binomial coefficient$\textstyle { \binom { n } { d } }$. We often identify a subset S of$[ n ]$with the zero-one vector$\textstyle \sum _ { i \in S } e _ { i }$in$\mathbb { N } ^ { n }$. For example, we write$w ^ { S }$for the square-free monomial$\Pi _ { i \in S } w _ { i }$

Definition 2.1 (Lorentzian polynomials). We set$\mathring { \mathrm { L } } _ { n } ^ { 0 } = \mathrm { P } _ { n } ^ { 0 } , \mathring { \mathrm { L } } _ { n } ^ { 1 } = \mathrm { P } _ { n } ^ { 1 }$, and

$\mathring { \mathrm { L } } _ { n } ^ { 2 } = \{ f \in \mathrm { P } _ { n } ^ { 2 } \ | \ \mathcal { H } _ { f }$is nonsingular and has exactly one positive eigenvalue).

For d larger than 2, we define$\mathring { \mathrm { L } } _ { n } ^ { d }$recursively by setting

$$
\mathring {\mathrm{L}} _ {n} ^ {d} = \left\{f \in \mathrm{P} _ {n} ^ {d} \mid \partial_ {i} f \in \mathring {\mathrm{L}} _ {n} ^ {d - 1} \text {   for   all   } i \in [ n ] \right\}.
$$

The polynomials in$\mathring { \mathrm { L } } _ { n } ^ { d }$are called strictly Lorentzian, and the limits of strictly Lorentzian polynomials are called Lorentzian.

Clearly,$\mathring { \mathrm { L } } _ { n } ^ { d }$is an open subset of$\mathrm { H } _ { n } ^ { d } ,$and the space${ \dot { \mathrm { L } } } _ { n } ^ { 2 }$may be identified with the set of n$\times \ n$ symmetric matrices with positive entries that have the Lorentzian signature$( + , - , \ldots , - )$. Unwinding the recursive definition, we have

$$
\mathring {\mathrm{L}} _ {n} ^ {d} = \left\{f \in \mathrm{P} _ {n} ^ {d} \mid \partial^ {\alpha} f \in \mathring {\mathrm{L}} _ {n} ^ {2} \text {   for   every   } \alpha \in \Delta_ {n} ^ {d - 2} \right\}.
$$

Proposition 2.2 below on stable polynomials shows that$\mathring { \mathrm { L } } _ { n } ^ { d }$is nonempty for every n and d.

An important subclass of Lorentzian polynomials is homogeneous stable polynomials, which play a guiding role in many of our proofs. Recall that a polynomial$f$in$\mathbb { R } [ w _ { 1 } , \dots , w _ { n } ]$is stable if$f$is non-vanishing on$\mathcal { H } ^ { n }$or identically zero, where H is the open upper half plane in C. Let$\mathrm { S } _ { n } ^ { d }$be the set of degree d homogeneous stable polynomials in n variables with nonnegative coefficients. Hurwitz’s theorem shows that$\mathrm { S } _ { n } ^ { d }$is a closed subset of$\mathrm { H } _ { n } ^ { d }$[Wag11, Section 2]. When f is homogeneous and has nonnegative coefficients, the stability of$f$is equivalent to any one of the following statements on univariate polynomials in the variable x [BBL09, Theorem 4.5]:

– For any$u \in \mathbb { R } _ { > 0 } ^ { n } , f ( x u - v )$has only real zeros for all$v \in \mathbb { R } ^ { n }$

– For some u$\in \mathbb { R } _ { > 0 } ^ { n } , f ( x u - v )$has only real zeros for all$v \in \mathbb { R } ^ { n }$

– For any$u \in \mathbb { R } _ { \geqslant 0 } ^ { n }$with$f ( u ) > 0 , f ( x u - v )$has only real zeros for all$v \in \mathbb { R } ^ { n }$

– For some$u \in \mathbb { R } _ { \geqslant 0 } ^ { n }$with$f ( u ) > 0 , f ( x u - v )$has only real zeros for all$v \in \mathbb { R } ^ { n }$

We refer to [Wag11] and [Pem12] for background on the class of stable polynomials. We will use the fact that any polynomial$f \in \mathrm { S } _ { n } ^ { d }$is the limit of polynomials in the interior of$\mathrm { S } _ { n } ^ { d } ,$, that is, of strictly stable polynomials [Nui68].

Proposition 2.2. Any polynomial in$\mathrm { S } _ { n } ^ { d }$is Lorentzian.

Proof. We show that the interior of$\mathrm { S } _ { n } ^ { d }$is a subset of$\mathring { \mathrm { L } } _ { n } ^ { d }$by induction on d. When$d = 2 ,$, the statement follows from Lemma 2.5 below. The general case follows from the fact that$\partial _ { i }$is an open map sending$\mathrm { S } _ { n } ^ { d }$to$\mathrm { S } _ { n } ^ { d - 1 }$[Wag11, Lemma 2.4].□

All the nonzero coefficients of a homogeneous stable polynomial have the same sign [COSW04, Theorem 6.1]. Thus, any homogeneous stable polynomial is a constant multiple of a Lorentzian polynomial. For example, determinantal polynomials of the form

$$
f (w _ {1}, \ldots , w _ {n}) = \det (w _ {1} A _ {1} + \dots + w _ {n} A _ {n}),
$$

where$A _ { 1 } , \ldots , A _ { n }$are positive semidefinite matrices, are stable [BB08, Proposition 2.4], and hence Lorentzian.

Example 2.3. Consider the homogeneous bivariate polynomial with positive coefficients

$$
f = \sum_ {k = 0} ^ {d} a _ {k} w _ {1} ^ {k} w _ {2} ^ {d - k}.
$$

Computing the partial derivatives of$f$reveals that f is strictly Lorentzian if and only if

$$
\frac {a _ {k} ^ {2}}{\binom {d} {k} ^ {2}} > \frac {a _ {k - 1}}{\binom {d} {k - 1}} \frac {a _ {k + 1}}{\binom {d} {k + 1}} \text {   for   all   } 0 <   k <   d.
$$

On the other hand,$f$is stable if and only if the univariate polynomial$f | _ { w _ { 2 } = 1 }$has only real zeros. Thus, a Lorentzian polynomial need not be stable. For example, consider the cubic form

$$
f = 2 w _ {1} ^ {3} + 1 2 w _ {1} ^ {2} w _ {2} + 1 8 w _ {1} w _ {2} ^ {2} + \theta w _ {2} ^ {3},
$$

where θ is a real parameter. A straightforward computation shows that

f is Lorentzian if and only if$0 \leqslant \theta \leqslant 9$, and f is stable if and only if$0 \leqslant \theta \leqslant 8 .$

Example 2.4. Clearly, if f is in the closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$in$\mathrm { H } _ { n } ^ { d } ,$, then f has nonnegative coefficients and

$\partial ^ { \alpha } f$has at most one positive eigenvalue for every$\alpha \in \Delta _ { n } ^ { d - 2 }$

The bivariate cubic$f = w _ { 1 } ^ { 3 } + w _ { 2 } ^ { 3 }$shows that the converse fails. In this case,$\partial _ { 1 } f$and$\partial _ { 2 } f$are Lorentzian, but$f$is not Lorentzian.

We give alternative characterizations of${ \dot { \mathrm { L } } } _ { n } ^ { 2 }$. Similar arguments were given in [Gre81] and [COSW04, Theorem 5.3].

Lemma 2.5. The following conditions are equivalent for any$f \in  { \mathrm { P } } _ { n } ^ { 2 }$

(1) The Hessian of f has the Lorentzian signature$( + , - , \ldots , - )$, that is,$f \in \mathring { \mathrm { L } } _ { n } ^ { 2 }$

(2) For any nonzero u$\colon \mathbb { R } _ { \geqslant 0 } ^ { n } , ( u ^ { T } \mathcal { H } _ { f } v ) ^ { 2 } > ( u ^ { T } \mathcal { H } _ { f } u ) ( v ^ { T } \mathcal { H } _ { f } v )$for any$v \in \mathbb { R } ^ { n }$not parallel to u.

(3) For some u P$\mathbb { R } _ { \geqslant 0 } ^ { n } , ( u ^ { T } \mathcal { H } _ { f } v ) ^ { 2 } > ( u ^ { T } \mathcal { H } _ { f } u ) ( v ^ { T } \mathcal { H } _ { f } v )$for any$v \in \mathbb { R } ^ { n }$not parallel to u.

(4) For any nonzero$u \in \mathbb { R } _ { \geqslant 0 } ^ { n } ,$the univariate polynomial$f ( x u - v )$in x has two distinct real zeros for any$v \in \mathbb { R } ^ { n }$not parallel to u.

(5) For some$u \in \mathbb { R } _ { \geqslant 0 } ^ { n } ,$the univariate polynomial$f ( x u - v )$in x has two distinct real zeros for any$v \in \mathbb { R } ^ { n }$not parallel to u.

It follows that a quadratic form with nonnegative coefficients is strictly Lorentzian if and only if it is strictly stable. Thus, a quadratic form with nonnegative coefficients is Lorentzian if and only if it is stable.

Proof. We prove$( 1 ) \Rightarrow ( 2 )$. Since all the entries of$\mathcal { H } _ { f }$are positive,$u ^ { T } \mathcal { H } _ { f } u > 0$for any nonzero $u \in \mathbb { R } _ { \geqslant 0 } ^ { n }$. By Cauchy’s interlacing theorem, for any$v \in \mathbb { R } ^ { n }$not parallel to$u ,$the restriction of${ \mathcal { H } } _ { f }$ to the plane spanned by u, v has signature$( + , - )$. It follows that

$$
\det \left( \begin{array}{c c} u ^ {T} \mathcal {H} _ {f} u & u ^ {T} \mathcal {H} _ {f} v \\ u ^ {T} \mathcal {H} _ {f} v & v ^ {T} \mathcal {H} _ {f} v \end{array} \right) = (u ^ {T} \mathcal {H} _ {f} u) (v ^ {T} \mathcal {H} _ {f} v) - (u ^ {T} \mathcal {H} _ {f} v) ^ {2} <   0.
$$

We prove$( 3 ) \Rightarrow ( 1 )$. Let u be the nonnegative vector in the statement p3q. Then$\mathcal { H } _ { f }$is negative definite on the hyperplane$\{ v \in \mathbb { R } ^ { n } \mid u ^ { T } \mathcal { H } _ { f } v = 0 \}$. Since$f \in \mathrm { { P } } _ { n } ^ { 2 } ,$, we have$u ^ { T } \mathcal { H } _ { f } u > 0$, and hence $\mathcal { H } _ { f }$has the Lorentzian signature.

The remaining implications follows from the fact that the univariate polynomial${ \scriptstyle { \frac { 1 } { 2 } } } f ( x u - v )$ has the discriminant$( \boldsymbol { u } ^ { T } \mathbf { \mathcal { H } } _ { f } \boldsymbol { v } ) ^ { 2 } - ( \boldsymbol { u } ^ { T } \mathbf { \mathcal { H } } _ { f } \boldsymbol { u } ) ( \boldsymbol { v } ^ { T } \mathbf { \mathcal { H } } _ { f } \boldsymbol { v } )$□

Matroid theory captures various combinatorial notions of independence. A matroid M on rns is a nonempty family of subsets B of rns, called the set of bases of M, that satisfies the exchange property:

For any$B _ { 1 } , B _ { 2 } \in \mathrm { B }$and$i \in B _ { 1 } \backslash B _ { 2 }$, there is$j \in B _ { 2 } \backslash B _ { 1 }$such that$( B _ { 1 } \backslash i ) \cup j \in \mathrm { B }$

We refer to [Oxl11] for background on matroid theory. More generally, following [Mur03], we define a subset$\mathbf { J } \subseteq \mathbb { N } ^ { n }$to be M-convex if it satisfies any one of the following equivalent conditions<sup>5</sup>:

– For any$\alpha , \beta \in \mathrm { J }$and any index i satisfying$\alpha _ { i } > \beta _ { i }$, there is an index j satisfying

$$
\alpha_ {j} <   \beta_ {j} \text { and } \alpha - e _ {i} + e _ {j} \in J.
$$

– For any$\alpha , \beta \in \mathrm { J }$and any index i satisfying$\alpha _ { i } > \beta _ { i }$, there is an index j satisfying

$$
\alpha_ {j} <   \beta_ {j} \text { and } \alpha - e _ {i} + e _ {j} \in J \text { and } \beta - e _ {j} + e _ {i} \in J.
$$

The first condition is called the exchange property for M-convex sets, and the second condition is called the symmetric exchange property for M-convex sets. A proof of the equivalence can be found in [Mur03, Chapter 4]. Note that any M-convex subset of$\mathbb { N } ^ { n }$is necessarily contained in the discrete simplex$\Delta _ { n } ^ { d }$for some d. We refer to [Mur03] for a comprehensive treatment of M-convex sets.

Let f be a polynomial in$\mathbb { R } [ w _ { 1 } , \dots , w _ { n } ]$. We write f in the normalized form

$$
f = \sum_ {\alpha \in \mathbb {N} ^ {n}} \frac {c _ {\alpha}}{\alpha !} w ^ {\alpha}, \text {   where   } \alpha ! = \prod_ {i = 1} ^ {n} \alpha_ {i}!.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>The class of M-convex sets is essentially identical to the class of generalized polymatroids in the sense of [Fuj05]. Some other notions in the literature that are equivalent to M-convex sets are integral polymatroids [Wel76], discrete polymatroids [HH03], and integral generalized permutohedras [Pos09]. We refer to [Mur03, Section 1.3] and [Mur03, Section 4.7] for more details.</span></small>

The support of the polynomial$f$is the subset of$\mathbb { N } ^ { n }$defined by

$$
\operatorname{supp} (f) = \left\{\alpha \in \mathbb {N} ^ {n} \mid c _ {\alpha} \neq 0 \right\}.
$$

We write$\mathrm { M } _ { n } ^ { d }$for the set of all degree d homogeneous polynomials in$\mathbb { R } _ { \geqslant 0 } [ w _ { 1 } , \ldots , w _ { n } ]$whose supports are M-convex. Note that, in our convention, the empty subset of N<sup>n</sup> is an M-convex set. Thus, the zero polynomial belongs to$\mathrm { M } _ { n . } ^ { d }$, and$f \in \mathrm { M } _ { n } ^ { d }$implies$\partial _ { i } f \in \mathrm { M } _ { n } ^ { d - 1 }$. It follows from [Bra07¨ , Theorem 3.2] that$\mathrm { S } _ { n } ^ { d } \subseteq \mathrm { M } _ { n } ^ { d }$

Definition 2.6. We set$\mathrm { L } _ { n } ^ { 0 } = \mathrm { S } _ { n } ^ { 0 } , \mathrm { L } _ { n } ^ { 1 } = \mathrm { S } _ { n } ^ { 1 }$, and$\mathrm { L } _ { n } ^ { 2 } = \mathrm S _ { n } ^ { 2 }$. For d larger than 2, we define

$$
\mathrm{L} _ {n} ^ {d} = \left\{f \in \mathrm{M} _ {n} ^ {d} \mid \partial_ {i} f \in \mathrm{L} _ {n} ^ {d - 1} \text {for all} i \in [ n ] \right\} = \left\{f \in \mathrm{M} _ {n} ^ {d} \mid \partial^ {\alpha} f \in \mathrm{L} _ {n} ^ {2} \text {for every} \alpha \in \Delta_ {n} ^ {d - 2} \right\}.
$$

Clearly,$\mathrm { L } _ { n } ^ { d }$contains$\mathring { \mathrm { L } } _ { n } ^ { d }$. In Theorem 2.25, we show that$\mathrm { L } _ { n } ^ { d }$is the closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$in$\mathrm { H } _ { n } ^ { d }$. In other words,$\mathrm { L } _ { n } ^ { d }$is exactly the set of degree d Lorentzian polynomials in n variables. In this section, we show that$\mathring { \mathrm { L } } _ { n } ^ { d }$is contractible and its closure contains$\mathrm { L } _ { n } ^ { d }$. The following proposition plays a central role in our analysis of$\mathrm { L } _ { n } ^ { d }$. Analogous statements, in the context of hyperbolic polynomials and stable polynomials, appear in [Nui68] and [LS81]. We fix a degree d homogeneous polynomial$f$in n variables and indices$i , j$in rns.

Proposition 2.7. If$f \in \mathrm { L } _ { n } ^ { d } ,$, then$\left( 1 + \theta w _ { i } \partial _ { j } \right) f \in \mathrm { L } _ { n } ^ { d }$for every nonnegative real number$\theta .$

We prepare the proof of Proposition 2.7 with two lemmas.

Lemma 2.8. If$f \in \mathrm { M } _ { n } ^ { d }$, then$\left( 1 + \theta w _ { i } \partial _ { j } \right) f \in \mathrm { M } _ { n } ^ { d }$for every nonnegative real number θ.

Proof. We may suppose$\theta = 1$and$j = n$. We use two combinatorial lemmas from [KMT07]. Introduce a new variable$w _ { n + 1 }$, and set

$$
g (w _ {1}, \dots , w _ {n}, w _ {n + 1}) = f (w _ {1}, \dots , w _ {n} + w _ {n + 1}) = \sum_ {k = 0} ^ {d} \frac {1}{k !} w _ {n + 1} ^ {k} \partial_ {n} ^ {k} f (w _ {1}, \dots , w _ {n}).
$$

By [KMT07, Lemma$6 ] ,$the support of$g$is M-convex. In terms of [KMT07], the support of $g$is obtained from the support of$f$by an elementary splitting, and the operation of splitting preserves M-convexity. Therefore, g belongs to$\mathrm { M } _ { n + 1 } ^ { d }$. Since the intersection of an M-convex set with a cartesian product of intervals is M-convex, it follows that

$$
\left(1 + w _ {n + 1} \partial_ {n}\right) f \in \mathrm{M} _ {n + 1} ^ {d}.
$$

By [KMT07, Lemma 9], the above displayed inclusion implies

$$
\left(1 + w _ {i} \partial_ {n}\right) f \in \mathrm{M} _ {n} ^ {d}.
$$

In terms of [KMT07], the support of$\left( 1 + w _ { i } \partial _ { n } \right) f$is obtained from the support of$\left( 1 + w _ { n + 1 } \partial _ { n } \right) f$ by an elementary aggregation, and the operation of aggregation preserves M-convexity.□

For stable polynomials$f$and g in$\mathbb { R } [ w _ { 1 } , \ldots , w _ { n } ]$, we define a relation$f \prec g$by

$$
f \prec g \Longleftrightarrow g + w _ {n + 1} f \text {   is   a   stable   polynomial   in   } \mathbb {R} [ w _ {1}, \dots , w _ {n}, w _ {n + 1} ].
$$

If$f$and$g$are univariate polynomials with leading coefficients of the same sign, then$f \prec g$if and only if the zeros of f interlace the zeros of$g \ [ \mathrm { B B 1 0 } ]$, Lemma 2.2]. In general, we have

$$
f \prec g \Longleftrightarrow f (x u - v) \prec g (x u - v) \text {   for   all   } u \in \mathbb {R} _ {> 0} ^ {n} \text {   and   } v \in \mathbb {R} ^ {n}.
$$

For later use, we record here basic properties of stable polynomials and the relation$\prec .$

Lemma 2.9. Let$f , g _ { 1 } , g _ { 2 } , h _ { 1 } , h _ { 2 }$be stable polynomials satisfying$h _ { 1 } < f < g _ { 1 }$and$h _ { 2 } < f < g _ { 2 }$

(1) The derivative$\partial _ { 1 } f$is stable and$\hat { \sigma } _ { 1 } f \prec f$

(2) The diagonalization$f ( w _ { 1 } , w _ { 1 } , w _ { 3 } , \ldots , w _ { n } )$is stable.

(3) The dilation$f ( a _ { 1 } w _ { 1 } , \ldots , a _ { n } w _ { n } )$is stable for any$a \in \mathbb { R } _ { \geqslant 0 } ^ { n }$

(4) If f is not identically zero, then$f < \theta _ { 1 } g _ { 1 } + \theta _ { 2 } g _ { 2 }$for any$\theta _ { 1 } , \theta _ { 2 } \geqslant 0$

(5) If f is not identically zero, then$\theta _ { 1 } h _ { 1 } + \theta _ { 2 } h _ { 2 } < f$for any$\theta _ { 1 } , \theta _ { 2 } \geqslant 0 .$

The statement$\hat { o } _ { 1 } f \prec f$appears, for example, in [BBL09, Section 4]. It follows that, if$f$is stable, then$( 1 + \theta w _ { i } \partial _ { j } ) f$is stable for every nonnegative real number θ. The remaining proof of Lemma 2.9 can be found in [Wag11, Section 2] and [BB10, Section 2].

Proof of Proposition 2.7. When$d = 2 ,$Lemma 2.9 implies Proposition 2.7. Suppose d$\geqslant 3 ,$and set

$$
g = \left(1 + \theta w _ {i} \partial_ {j}\right) f.
$$

By Lemma$2 . 8 ,$the support of$g$is M-convex. Therefore, it is enough to prove that$\partial ^ { \alpha } g$is stable for all$\alpha \in \Delta _ { n } ^ { d - 2 }$. We give separate arguments when$\alpha _ { i } = 0$and$\alpha _ { i } > 0$. If$\alpha _ { i } = 0$, then

$$
\partial^ {\alpha} g = \partial^ {\alpha} f + \theta w _ {i} \partial^ {\alpha + e _ {j}} f.
$$

In this case, (1), (2), and (3) of Lemma 2.9 for$\partial ^ { \alpha } f$show that$\partial ^ { \alpha } g$is stable. If$\alpha _ { i } > 0$, then

$$
\begin{array}{l} \partial^ {\alpha} g = \partial^ {\alpha} f + \theta \alpha_ {i} \partial^ {\alpha - e _ {i} + e _ {j}} f + \theta w _ {i} \partial^ {\alpha + e _ {j}} f \\ \qquad = \partial_ {i} \Big (\partial^ {\alpha - e _ {i}} f \Big) + \theta \alpha_ {i} \partial_ {j} \Big (\partial^ {\alpha - e _ {i}} f \Big) + \theta w _ {i} \partial_ {i} \partial_ {j} \Big (\partial^ {\alpha - e _ {i}} f \Big). \end{array}
$$

In this case, (1) of Lemma 2.9 applies to the stable polynomials$\partial ^ { \alpha } f$and$\partial ^ { \alpha - \boldsymbol { e } _ { i } + \boldsymbol { e } _ { j } } f \colon$

$$
\partial_ {i} \partial_ {j} \left(\partial^ {\alpha - e _ {i}} f\right) \prec \partial_ {i} \left(\partial^ {\alpha - e _ {i}} f\right) \text {   and   } \partial_ {i} \partial_ {j} \left(\partial^ {\alpha - e _ {i}} f\right) \prec \partial_ {j} \left(\partial^ {\alpha - e _ {i}} f\right).
$$

Therefore, unless$\partial ^ { \alpha + e _ { j } } f$is identically zero,$\partial ^ { \alpha } g$is stable by (2) and (4) of Lemma 2.9.

It remains to prove that, whenever$\alpha _ { i }$is positive and$\partial ^ { \alpha + e _ { j } } f$is identically zero,

$\hat { \sigma } _ { i } \Big ( \hat { \sigma } ^ { \alpha - e _ { i } } f \Big ) + \phi \hat { \sigma } _ { j } \Big ( \hat { \sigma } ^ { \alpha - e _ { i } } f \Big )$is stable for every nonnegative real number$\phi .$

Since the cubic form$\hat { o } ^ { \alpha - e _ { i } } f$is in$\mathrm { L } _ { n } ^ { 3 } ,$, it is enough to prove the statement when d “ 3 and$\alpha = e _ { i }$

We show that, if f is in$\mathrm { L } _ { n } ^ { 3 }$and$\partial _ { i } \partial _ { j } f$is identically zero, then

$\partial _ { i } f + \phi \partial _ { j } f$is stable for every nonnegative real number$\phi .$

The statement is clear when$( \partial _ { i } f ) ( \partial _ { j } f )$is identically zero. If otherwise, there are monomials of the form$w _ { i } w _ { i ^ { \prime } } w _ { i ^ { \prime \prime } }$and$w _ { j } w _ { j ^ { \prime } } w _ { j ^ { \prime \prime } }$in the support of$f .$. We apply the symmetric exchange property to the support of$f ,$the monomials$w _ { i } w _ { i ^ { \prime } } w _ { i ^ { \prime \prime } } , w _ { j } w _ { j ^ { \prime } } w _ { j ^ { \prime \prime } }$, and the variable$w _ { i } \colon$We see that the monomial$w _ { j } w _ { i ^ { \prime } } w _ { i ^ { \prime \prime } }$must be in the support of$f ,$since no monomial in the support of$f$ is divisible by$w _ { i } w _ { j }$. For a positive real parameter$s ,$set

$$
h _ {s} = \left(1 + s w _ {i} \partial_ {i ^ {\prime}}\right) f.
$$

Since$\partial _ { i } \partial _ { i ^ { \prime } } f$is not identically zero, the argument in the first paragraph shows that$h _ { s }$is in$\mathrm { L } _ { n } ^ { 3 }$. Similarly, since$\partial _ { i } \partial _ { j } h _ { s }$is not identically zero, we have

$\big ( 1 + \phi w _ { i } \partial _ { j } \big ) h _ { s } \in \mathrm { L } _ { n } ^ { 3 }$for every nonnegative real number$\phi .$

Since stability is a closed condition, it follows that

$\operatorname* { l i m } _ { s  0 } \hat { \partial } _ { i } \Big ( h _ { s } + \phi w _ { i } \hat { \partial } _ { j } h _ { s } \Big ) = \hat { \partial } _ { i } f + \phi \hat { \partial } _ { j } f$is stable for every nonnegative real number$\phi .$. □

We use Proposition 2.7 to show that any nonnegative linear change of variables preserves$\mathrm { L } _ { n } ^ { d }$. Theorem 2.10. If$f ( w ) \in \operatorname { L } _ { n } ^ { d } ,$, then$f ( A v ) \in \mathrm { L } _ { m } ^ { d }$for any$n \times m$matrix A with nonnegative entries.

Proof. Fix$f = f ( w _ { 1 } , \dots , w _ { n } )$in$\mathrm { L } _ { n } ^ { d }$. Note that Theorem 2.10 follows from its three special cases:

(I) the elementary splitting$f ( w _ { 1 } , \dots , w _ { n - 1 } , w _ { n } + w _ { n + 1 } )$is in$\mathrm { L } _ { n + 1 } ^ { d }$

(II) the dilation$f ( w _ { 1 } , \dots , w _ { n - 1 } , \theta w _ { n } )$is in$\mathrm { L } _ { n } ^ { d }$for any$\theta \geqslant 0 ,$

(III) the diagonalization$f ( w _ { 1 } , \dots , w _ { n - 2 } , w _ { n - 1 } , w _ { n - 1 } )$is in$\mathrm { L } _ { n - 1 } ^ { d } ,$

As observed in the proof of Lemma 2.8, an elementary splitting preserves M-convexity:

$$
f (w _ {1}, \ldots , w _ {n - 1}, w _ {n} + w _ {n + 1}) \in \mathrm{M} _ {n + 1} ^ {d}.
$$

Therefore,<sup>6</sup> the first statement follows from Proposition 2.7:

$$
\lim _ {k \to \infty} \left(1 + \frac {w _ {n + 1} \partial_ {n}}{k}\right) ^ {k} f = f (w _ {1}, \ldots , w _ {n - 1}, w _ {n} + w _ {n + 1}) \in \mathrm{L} _ {n + 1} ^ {d}.
$$

For the second statement, note from the definition of M-convexity that

$$
f (w _ {1}, \dots , w _ {n - 1}, 0) \in \mathrm{M} _ {n} ^ {d}.
$$

Thus the second statement for$\theta = 0$follows from the case$\theta > 0 ,$, which is trivial to verify.

The proof of the third statement is similar to that of the first statement. As observed in the proof of Lemma 2.8, an elementary aggregation preserves M-convexity, and hence

$$
f (w _ {1}, \ldots , w _ {n - 1}, w _ {n - 1} + w _ {n}) \in \mathrm{M} _ {n} ^ {d}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Mdn+1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">t L<sup>d</sup><sub>n\`1</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>It is necessary to check the inclusion in M<sup>d</sup><sub>n\`1</sub> in advance because we have not yet proved tha is closed.</span></small>

Therefore, Proposition 2.7 implies that

$$
\lim _ {k \to \infty} \left(1 + \frac {w _ {n - 1} \partial_ {n}}{k}\right) ^ {k} f = f (w _ {1}, \ldots , w _ {n - 1}, w _ {n - 1} + w _ {n}) \in \mathrm{L} _ {n} ^ {d}.
$$

By the second statement, we may substitute$w _ { n }$in the displayed equation by zero.

Theorem 2.10 can be used to show that taking directional derivatives in nonnegative directions takes polynomials in$\mathrm { L } _ { n } ^ { d }$to polynomials in$\mathrm { L } _ { n } ^ { d - 1 }$

Corollary 2.11. If$f \in \mathrm { L } _ { n } ^ { d } .$, then$\textstyle \sum _ { i = 1 } ^ { n } a _ { i } \hat { \sigma } _ { i } f \in \operatorname { L } _ { n } ^ { d - 1 }$for any$a _ { 1 } , \ldots , a _ { n } \geqslant 0 .$

Proof. We apply Theorem 2.10 to f and the matrix with column vectors$e _ { 1 } , \ldots , e _ { n }$and$\scriptstyle \sum _ { i = 1 } ^ { n } a _ { i } e _ { i } :$

$$
g := f (w _ {1} + a _ {1} w _ {n + 1}, \ldots , w _ {n} + a _ {n} w _ {n + 1}) \in \mathrm{L} _ {n + 1} ^ {d}
$$

$$
\partial_ {n + 1} g \in \mathrm{L} _ {n + 1} ^ {d - 1}
$$

Applying Theorem 2.10 to$\partial _ { n + 1 } g$and the matrix with column vectors$e _ { 1 } , \ldots , e _ { n }$and 0, we get

$$
\partial_ {n + 1} g | _ {w _ {n + 1} = 0} = \sum_ {i = 1} ^ {n} a _ {i} \partial_ {i} f \in \mathrm{L} _ {n} ^ {d - 1}.
$$

Let θ be a nonnegative real parameter. We define a linear operator$T _ { n } ( \theta , - )$by

$$
T _ {n} (\theta , f) = \left(\prod_ {i = 1} ^ {n - 1} \left(1 + \theta w _ {i} \partial_ {n}\right) ^ {d}\right) f.
$$

By Proposition 2.7, if$f \in \mathrm { L } _ { n } ^ { d } .$, then$T _ { n } ( \theta , f ) \in \mathrm { L } _ { n } ^ { d }$. In addition, if$f \in \mathrm { P } _ { n } ^ { d } ,$, then$T _ { n } ( \theta , f ) \in \mathrm { P } _ { n } ^ { d }$ Most importantly, the operator$T _ { n }$satisfies the following Nuij-type homotopy lemma. For a similar argument in the context of hyperbolic polynomials, see the proof of the main theorem in [Nui68].

Lemma 2.12. If$f \in  { \mathrm { L } } _ { n } ^ { d } \cap  { \mathrm { P } } _ { n } ^ { d } ,$, then$T _ { n } ( \theta , f ) \in \mathring { \mathrm { L } } _ { n } ^ { d }$for every positive real number$\theta .$

Proof. Let$e _ { i }$be the i-th standard unit vector in$\mathbb { R } ^ { n }$, and let v be any vector in$\mathbb { R } ^ { n }$not parallel to $e _ { n } .$. From here on, in this proof, all polynomials are restricted to the line$x e _ { n } - v$and considered as univariate polynomials in x.

Let α be an arbitrary element of$\Delta _ { n } ^ { d - 2 }$. By Lemma 2.5, it is enough to show that the quadratic polynomial$\partial ^ { \alpha } T _ { n } ( \theta , f )$has two distinct real zeros. Using Proposition 2.7, we can deduce the preceding statement from the following claims:

(I) If$\partial ^ { \alpha } f$has two distinct real zeros, then$\hat { \sigma } ^ { \alpha } \big ( 1 + \theta w _ { i } \hat { \sigma } _ { n } \big ) f$has two distinct zeros.

(II) If$v _ { i }$is nonzero, then$\hat { v } ^ { \alpha } \big ( 1 + \theta w _ { i } \hat { \sigma } _ { n } \big ) ^ { d } f$has two distinct real zeros.

We first prove (I). Suppose$\partial ^ { \alpha } f$has two distinct real zeros, and set$g = \left( 1 + \theta w _ { i } \partial _ { n } \right) f$. Note that

$$
\partial^ {\alpha} g = \partial^ {\alpha} f + \theta \alpha_ {i} \partial^ {\alpha - e _ {i} + e _ {n}} f + \theta w _ {i} \partial^ {\alpha + e _ {n}} f.
$$

Let c be the unique zero of$\hat { o } ^ { \alpha + e _ { n } } f$. Since c strictly interlaces two distinct zeros of$\partial ^ { \alpha } f ,$, we have

$$
\partial^ {\alpha} f | _ {x = c} <   0.
$$

Similarly, since$\partial ^ { \alpha - e _ { i } + e _ { n } } f$has only real zeros and$\hat { \sigma } ^ { \alpha + e _ { n } } f < \hat { \sigma } ^ { \alpha - e _ { i } + e _ { n } } f ,$, we have

$$
\partial^ {\alpha - e _ {i} + e _ {n}} f | _ {x = c} \leqslant 0.
$$

Thus$\partial ^ { \alpha } g | _ { x = c } < 0$, and hence$\partial ^ { \alpha } g$has two distinct real zeros. This completes the proof of (I).

Before proving (II), we strengthen (I) as follows:

(III) A multiple zero of$\partial ^ { \alpha } g$is necessarily a multiple zero of$\partial ^ { \alpha } f .$

Suppose$\partial ^ { \alpha } g$has a multiple zero. Using (I), we know that$\partial ^ { \alpha } f$has a multiple zero, say c. Clearly, c must be also a zero of$\hat { o } ^ { \alpha + e _ { n } } f$. Since c interlaces the two (not necessarily distinct) zeros of $\partial ^ { \alpha - e _ { i } + e _ { n } } f ,$we have

$$
\partial^ {\alpha} g | _ {x = c} = \theta \alpha_ {i} \partial^ {\alpha - e _ {i} + e _ {n}} f | _ {x = c} \leqslant 0.
$$

Therefore, if c is not a zero of$\partial ^ { \alpha } g ,$, then$\partial ^ { \alpha } g$has two distinct zeros, contradicting the hypothesis that$\partial ^ { \alpha } g$has a multiple zero. This completes the proof of (III).

We prove (II). Suppose$\hat { v } ^ { \alpha } \big ( 1 + \theta w _ { i } \hat { \sigma } _ { n } \big ) ^ { d } f$has a multiple zero, say c. Using (III), we know that

the number c is a multiple zero of$\hat { v } ^ { \alpha } \big ( 1 + \theta w _ { i } \hat { \sigma } _ { n } \big ) ^ { k } f$for all$0 \leqslant k \leqslant d .$

Expanding the k-th power and using the linearity of$\partial ^ { \alpha }$, we deduce that

the number c is a zero of$\partial ^ { \alpha } w _ { i } ^ { k } \partial _ { n } ^ { k } f$for all$0 \leqslant k \leqslant d .$

However, since$f$has positive coefficients, the value of$\partial ^ { \alpha } w _ { i } ^ { \alpha _ { i } + 2 } \partial _ { n } ^ { \alpha _ { i } + 2 } f$at c is a positive multiple of$v _ { i \cdot } ^ { 2 }$, and hence$v _ { i }$must be zero. This completes the proof of (II).□

We use Lemma 2.12 to prove the main result of this subsection.

Theorem 2.13. The closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$in$\mathrm { H } _ { n } ^ { d }$contains$\mathrm { L } _ { n } ^ { d } .$

Proof. Let f be a polynomial in$\mathrm { L } _ { n } ^ { d }$that is not identically zero, and let$\theta$be a real parameter satisfying$0 \leqslant \theta \leqslant 1$. By Theorem 2.10, we have

$$
S (\theta , f) := \frac {1}{| f | _ {1}} f \left((1 - \theta) w _ {1} + \theta \left(w _ {1} + \dots + w _ {n}\right), \dots , (1 - \theta) w _ {n} + \theta \left(w _ {1} + \dots + w _ {n}\right)\right) \in \mathrm{L} _ {n} ^ {d},
$$

where$| f | _ { 1 }$is the sum of all coefficients of$f .$Since$S ( \theta , f )$belongs to$\mathrm { P } _ { n } ^ { d }$when$0 < \theta \leqslant 1$, Lemma 2.12 shows that we have a homotopy

$$
T _ {n} \Big (\theta , S (\theta , f) \Big) \in \mathring {\mathrm{L}} _ {n} ^ {d}, \quad 0 <   \theta \leqslant 1,
$$

that deforms$f$to the polynomial$T _ { n } \big ( 1 , ( w _ { 1 } + \cdot \cdot \cdot + w _ { n } ) ^ { d } \big )$. It follows that the closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$in$\mathrm { H } _ { n } ^ { d }$ contains$\mathrm { L } _ { n } ^ { d }$□

We show in Theorem 2.25 that the closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$in$\mathrm { H } _ { n } ^ { d }$is, in fact, equal to$\mathrm { L } _ { n } ^ { d }$.

2.2. Hodge–Riemann relations for Lorentzian polynomials. Let f be a nonzero degree d$\geqslant 2$ homogeneous polynomial with nonnegative coefficients in variables$w _ { 1 } , \ldots , w _ { n }$. The following proposition may be seen as an analog of the Hodge–Riemann relations for homogeneous stable polynomials.<sup>7</sup>

Proposition 2.14. If$f$is in$\mathrm { S } _ { n } ^ { d } \backslash 0 ,$then$\mathcal { H } _ { f } ( w )$has exactly one positive eigenvalue for all$w \in \mathbb { R } _ { > 0 } ^ { n }$ Moreover, if f is in the interior of$\mathrm { S } _ { n } ^ { d } ,$, then$\mathcal { H } _ { f } ( w )$is nonsingular for all$w \in \mathbb { R } _ { > 0 } ^ { n }$

Proof. Fix a vector w$\in \mathbb { R } _ { > 0 } ^ { n }$. By Lemma 2.5, the Hessian of$f$has exactly one positive eigenvalue at w if and only if the following quadratic polynomial in z is stable:

$$
z ^ {T} \mathcal {H} _ {f} (w) z = \sum_ {1 \leqslant i, j \leqslant n} z _ {i} z _ {j} \partial_ {i} \partial_ {j} f (w).
$$

The above is the quadratic part of the stable polynomial with nonnegative coefficients$f ( z + w )$ and hence is stable by [BBL09, Lemma 4.16].

Moreover, if$f$is strictly stable, then$f _ { \epsilon } = f \pm \epsilon ( w _ { 1 } ^ { d } + \cdot \cdot \cdot + w _ { n } ^ { d } )$is stable for all sufficiently small positive ϵ. Therefore, by the result obtained in the previous paragraph, the matrix

$$
\mathcal {H} _ {f _ {\epsilon}} (w) = \mathcal {H} _ {f} (w) \pm d (d - 1) \epsilon \operatorname{diag} (w _ {1} ^ {d - 2}, \ldots , w _ {n} ^ {d - 2})
$$

has exactly one positive eigenvalue for all sufficiently small positive$\epsilon ,$and hence$\mathcal { H } _ { f } ( w )$is nonsingular.□

In Theorem 2.16, we extend the above result to Lorentzian polynomials.

Lemma 2.15. If$\mathcal { H } _ { \partial _ { i } f } ( w )$has exactly one positive eigenvalue for every$i \in [ n ]$and$w \in \mathbb { R } _ { > 0 } ^ { n } ,$then

$$
\ker \mathcal {H} _ {f} (w) = \bigcap_ {i = 1} ^ {n} \ker \mathcal {H} _ {\partial_ {i} f} (w) \text {   for   every   } w \in \mathbb {R} _ {> 0} ^ {n}.
$$

Proof. We may suppose$d \geqslant 3$. Fix$w \in \mathbb { R } _ { > 0 } ^ { n } ,$and write$\mathcal { H } _ { f }$for$\mathcal { H } _ { f } ( w )$. We will use Euler$' _ { \mathrm { { S } } }$ formula for homogeneous functions:

$$
d f = \sum_ {i = 1} ^ {n} w _ {i} \partial_ {i} f.
$$

It follows that the Hessians of$f$and$\partial _ { i } f$satisfy the relation

$$
(d - 2) \mathcal {H} _ {f} = \sum_ {i = 1} ^ {n} w _ {i} \mathcal {H} _ {\partial_ {i} f},
$$

and hence the kernel of${ \mathcal { H } } _ { f }$contains the intersection of the kernels of$\mathcal { H } _ { \partial _ { i } f }$

For the other inclusion, let z be a vector in the kernel of$\mathcal { H } _ { f }$. By Euler’s formula again,

$$
(d - 2) e _ {i} ^ {T} \mathcal {H} _ {f} = w ^ {T} \mathcal {H} _ {\partial_ {i} f} \text {   for   every   } i \in [ n ],
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>We refer to [Huh18] for a survey of the Hodge–Riemann relations in combinatorial contexts.</span></small>

and hence$w ^ { T } \mathcal { H } _ { \partial _ { i } f } z = 0$for every$i \in [ n ]$. We have$w ^ { T } \mathcal { H } _ { \partial _ { i } f } w > 0$because$\partial _ { i } f$is nonzero and has nonnegative coefficients. Since$\mathcal { H } _ { \partial _ { i } f } ( w )$has exactly one positive eigenvalue, it follows that $\mathcal { H } _ { \partial _ { i } f }$is negative semidefinite on the kernel of$\boldsymbol { w } ^ { T } \mathcal { H } _ { \partial _ { i } f }$. In particular,

${ z } ^ { T } \mathcal { H } _ { \partial _ { i } f } { z } \leqslant 0 ,$, with equality if and only if$\mathcal { H } _ { \partial _ { i } f } z = 0$

To conclude, we write zero as the positive linear combination

$$
0 = (d - 2) \left(z ^ {T} \mathcal {H} _ {f} z\right) = \sum_ {i = 1} ^ {n} w _ {i} \left(z ^ {T} \mathcal {H} _ {\partial_ {i} f} z\right).
$$

Since every summand in the right-hand side is non-positive by the previous analysis, we must have$z ^ { T } \mathcal { H } _ { \partial _ { i } f } z = 0$for every$i \in [ n ]$, and hence$\mathcal { H } _ { \partial _ { i } f } z = 0$for every$i \in . [ n ]$□

We now prove an analog of the Hodge–Riemann relation for Lorentzian polynomials. When $f$is the volume polynomial of a projective variety as defined in Section 4.2, then the one positive eigenvalue condition for the Hessian of$f$at w is equivalent to the validity of the Hodge– Riemann relations on the space of divisor classes of the projective variety with respect to the polarization corresponding to w.

Theorem 2.16. Let$f$be a nonzero homogeneous polynomial in$\mathbb { R } [ w _ { 1 } , \dots , w _ { n } ]$of degree d$\geqslant 2$

(1) If$f$is in${ \overset { \circ } { \operatorname { L } } } _ { n } ^ { d } ,$then$\mathcal { H } _ { f } ( w )$is nonsingular for all$w \in \mathbb { R } _ { > 0 } ^ { n }$

(2) If f is in$\mathrm { L } _ { n } ^ { d } ,$then$\mathcal { H } _ { f } ( w )$has exactly one positive eigenvalue for all$w \in \mathbb { R } _ { > 0 } ^ { n } .$

Proof. By Theorem 2.13,$\mathrm { L } _ { n } ^ { d }$is in the closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$. Note that, for any nonzero polynomial$f$of degree d$\geqslant 2$with nonnegative coefficients,$\mathcal { H } _ { f } ( w )$has at least one positive eigenvalue for any $w \in \mathbb { R } _ { > 0 } ^ { n }$. Therefore, we may suppose$f \in \mathring { \mathrm { L } } _ { n } ^ { d }$in (2). We prove (1) and (2) simultaneously by induction on d under this assumption. The base case$d = 2$is trivial. We suppose that d$\ l \geqslant 3$and that the theorem holds for$\mathring { \mathrm { L } } _ { n } ^ { d - 1 }$

That (1) holds for$\mathring { \mathrm { L } } _ { n } ^ { d }$follows from induction and Lemma 2.15. Using Proposition 2.14, we see that (2) holds for stable polynomials in$\mathring { \mathrm { L } } _ { n } ^ { d }$. Since$\mathring { \mathrm { L } } _ { n } ^ { d }$is connected by Theorem 2.13, the continuity of eigenvalues and the validity of (1) together implies (2).□

Theorem 2.16, when combined with the following proposition, shows that all polynomials in $\mathrm { L } _ { n } ^ { d }$share a negative dependence property. The negative dependence property will be systematically studied in the following section.

Proposition 2.17.$\operatorname { I f } { \mathcal { H } } _ { f } ( w )$has exactly one positive eigenvalue for all$w \in \mathbb { R } _ { > 0 } ^ { n }$, then

$$
f (w) \partial_ {i} \partial_ {j} f (w) \leqslant 2 \left(1 - \frac {1}{d}\right) \partial_ {i} f (w) \partial_ {j} f (w) \text {   for   all   } w \in \mathbb {R} _ {\geqslant 0} ^ {n} \text {   and   } i, j \in [ n ].
$$

Proof. Fix$w \in \mathbb { R } _ { > 0 } ^ { n } ,$, and write H for$\mathcal { H } _ { f } ( w )$. By Euler’s formula for homogeneous functions,

$$
w ^ {T} \mathcal {H} w = d (d - 1) f (w) \text { and } w ^ {T} \mathcal {H} e _ {i} = (d - 1) \partial_ {i} f (w).
$$

Let t be a real parameter, and consider the restriction of H to the plane spanned by w and $\boldsymbol { v } _ { t } = \boldsymbol { e } _ { i } + t \boldsymbol { e } _ { j }$. By Theorem 2.16, H has exactly one positive eigenvalue. Therefore, by Cauchy’s interlacing theorem, the restriction of H also has exactly one positive eigenvalue. In particular, the determinant of the restriction must be nonpositive:

$$
\left(w ^ {T} \mathcal {H} v _ {t}\right) ^ {2} - \left(w ^ {T} \mathcal {H} w\right) \cdot \left(v _ {t} ^ {T} \mathcal {H} v _ {t}\right) \geqslant 0 \text {   for   all   } t \in \mathbb {R}.
$$

In other words, for all$t \in \mathbb { R } ,$we have

$$
(d - 1) ^ {2} (\partial_ {i} f + t \partial_ {j} f) ^ {2} - d (d - 1) f (\partial_ {i} ^ {2} f + 2 t \partial_ {i} \partial_ {j} f + t ^ {2} \partial_ {j} ^ {2} f) \geqslant 0.
$$

It follows that, for all$t \in \mathbb { R }$, we have

$$
(d - 1) ^ {2} (\partial_ {i} f + t \partial_ {j} f) ^ {2} - 2 t d (d - 1) f \partial_ {i} \partial_ {j} f \geqslant 0.
$$

Thus, the discriminant of the above quadratic polynomial in t should be nonpositive:

$$
f \partial_ {i} \partial_ {j} f - 2 \left(1 - \frac {1}{d}\right) \partial_ {i} f \partial_ {j} f \leqslant 0.
$$

This completes the proof of Proposition 2.17.

2.3. Independence and negative dependence. Let c be a fixed positive real number, and let$f$be a polynomial in R$\mathbb { \rho } [ w _ { 1 } , \dots , w _ { n } ]$. In this section, the polynomial$f$is not necessarily homogeneous. As before, we write$e _ { i }$for the i-th standard unit vector in$\mathbb { R } ^ { n }$

Definition 2.18. We say that$f$is c-Rayleigh if$f$has nonnegative coefficients and

$$
\partial^ {\alpha} f (w) \partial^ {\alpha + e _ {i} + e _ {j}} f (w) \leqslant c \partial^ {\alpha + e _ {i}} f (w) \partial^ {\alpha + e _ {j}} f (w) \text {   for   all   } i, j \in [ n ], \alpha \in \mathbb {N} ^ {n}, w \in \mathbb {R} _ {\geqslant 0} ^ {n}.
$$

When$f$is the partition function of a discrete probability measure$\mu ,$the c-Rayleigh condition captures a negative dependence property of$\mu .$. More precisely, when$f$is multi-affine, that is, when$f$has degree at most one in each variable, the c-Rayleigh condition for$f$is equivalent to

$$
f (w) \partial_ {i} \partial_ {j} f (w) \leqslant c \partial_ {i} f (w) \partial_ {j} f (w) \text {   for   all   distinct   } i, j \in [ n ], \text {   and   } w \in \mathbb {R} _ {\geqslant 0} ^ {n}.
$$

Thus the 1-Rayleigh property of multi-affine polynomials is equivalent to the Rayleigh property for discrete probability measures studied in [Wag08] and [BBL09].

Proposition 2.19. Any polynomial in$\begin{array} { r } { \mathrm { L } _ { n } ^ { d } \mathrm { i s 2 } \Big ( 1 - \frac { 1 } { d } \Big ) - \mathrm { R a y l e i g h } } \end{array}$

Proof. The statement follows from Theorem 2.16 and Proposition 2.17 because$2 \left( 1 - { \frac { 1 } { d } } \right)$is an increasing function of$d .$□

The goal of this section is to show that the support of any homogeneous c-Rayleigh polynomial is M-convex (Theorem 2.23). The notion of M<sup>6</sup>-convexity will be useful for the proof: A subset$\mathbf { J } ^ { \natural } \subseteq \mathbb { N } ^ { n }$is said to be M<sup>6</sup>-convex if there is an M-convex set J in$\mathbb { N } ^ { n + 1 }$such that

$$
\mathrm{J} ^ {\natural} = \left\{\left(\alpha_ {1}, \dots , \alpha_ {n}\right) \mid \left(\alpha_ {1}, \dots , \alpha_ {n}, \alpha_ {n + 1}\right) \in \mathrm{J} \right\}.
$$

The projection from J to$\mathrm { J ^ { \sharp } }$should be bijective for any such J, as the M-convexity of J implies that J is in$\Delta _ { n } ^ { d }$for some d. We refer to [Mur03, Section 4.7] for more on M<sup>6</sup>-convex sets.

We prepare the proof of Theorem 2.23 with three lemmas. Verification of the first lemma is routine and will be omitted.

Lemma 2.20. The following polynomials are c-Rayleigh whenever$f$is c-Rayleigh:

(1) The contraction$\partial _ { i } f$of$f .$.

(2) The deletion$f \backslash i$of$f ,$the polynomial obtained from f by evaluating$w _ { i } = 0$

(4) The dilation$f ( a _ { 1 } w _ { 1 } , \ldots , a _ { n } w _ { n } ) , { \mathrm { f o r } } ( a _ { 1 } , \ldots , a _ { n } ) \in \mathbb { R } _ { \geqslant 0 } ^ { n }$

(5) The translation$f ( a _ { 1 } + w _ { 1 } , \ldots , a _ { n } + w _ { n } ) , \mathrm { f o r } ( a _ { 1 } , \ldots , a _ { n } ) \in \mathbb { R } _ { \geqslant 0 } ^ { n } .$

Remark. Lemma 2.20 in the previous version of this manuscript contained the following incorrect statement:

(3) If$f ( w _ { 1 } , w _ { 2 } , w _ { 3 } , \ldots , w _ { n } )$is c-Rayleigh, then so is the diagonalization$f ( w _ { 1 } , w _ { 1 } , w _ { 3 } , \ldots , w _ { n } )$

This implies that the rank sequence of any Rayleigh measure is strongly log-concave, which is known to be not true [BBL09, Section$^ { 7 , }$Counterexample 1]. In fact, the rank sequence of a Rayleigh measure need not even be unimodal [KN10, Theorem 6]. Proof of Lemma 2.22 below is revised accordingly.

We introduce a partial order$\leqslant$on$\mathbb { N } ^ { n }$by setting

$$
\alpha \leqslant \beta \Longleftrightarrow \alpha_ {i} \leqslant \beta_ {i} \text {   for   all   } i \in [ n ].
$$

We say that a subset$\mathrm { J ^ { \natural } }$of$\mathbb { N } ^ { n }$is interval convex if the following implication holds:

$$
\left(\alpha \in \mathrm{J} ^ {\natural}, \beta \in \mathrm{J} ^ {\natural}, \alpha \leqslant \gamma \leqslant \beta\right) \Longrightarrow \gamma \in \mathrm{J} ^ {\natural}.
$$

The augmentation property for$\mathbf { J } ^ { \natural } \subseteq \mathbb { N } ^ { n }$is the implication

$$
\left(\alpha \in \mathrm{J} ^ {\natural}, \beta \in \mathrm{J} ^ {\natural}, | \alpha | _ {1} <   | \beta | _ {1}\right) \Longrightarrow \left(\alpha_ {j} <   \beta_ {j} \text {   and   } \alpha + e _ {j} \in \mathrm{J} ^ {\natural} \text {   for   some   } j \in [ n ]\right).
$$

Lemma 2.21. Let$\mathrm { J ^ { \natural } }$be an interval convex subset of$\mathbb { N } ^ { n }$containing 0. Then$\mathrm { J ^ { \natural } }$is M<sup>6</sup>-convex if and only if$\mathrm { J ^ { \natural } }$satisfies the augmentation property.

Therefore, a nonempty interval convex subset of$\{ 0 , 1 \} ^ { n }$containing 0 is M<sup>6</sup>-convex if and only if it is the collection of independent sets of a matroid on$[ n ]$

Proof. Let d be any sufficiently large positive integer, and set

$$
\mathrm{J} = \Big \{\big (\alpha_ {1}, \dots , \alpha_ {n}, d - \alpha_ {1} - \dots - \alpha_ {n} \big) \in \mathbb {N} ^ {n + 1} \mid \big (\alpha_ {1}, \dots , \alpha_ {n} \big) \in \mathrm{J} ^ {\natural} \Big \}.
$$

The “only$\mathrm { i f ^ { \prime \prime } }$direction is straightforward: If$\mathrm { J ^ { \natural } }$is M<sup>6</sup>-convex, then J is M-convex, and the augmentation property for$\mathrm { J ^ { \natural } }$is a special case of the exchange property for J.

We prove the$\prime \prime _ { \mathrm { i f } } \prime \prime$direction by checking the exchange property for J. Let α and$\beta$be elements of${ \mathrm { J } } ,$, and let i be an index satisfying$\alpha _ { i } > \beta _ { i }$. We claim that there is an index$j$satisfying

$$
\alpha_ {j} <   \beta_ {j} \text { and } \alpha - e _ {i} + e _ {j} \in J.
$$

By the augmentation property for${ \mathrm { J } } ^ { \natural } ,$, it is enough to justify the claim when$i \neq n + 1$. When $\alpha _ { n + 1 } < \beta _ { n + 1 }$, then we may take$j = n + 1 ,$, again by the augmentation property for$\mathrm { M } ^ { \sharp }$

Suppose$\alpha _ { n + 1 } \geqslant \beta _ { n + 1 }$. In this case, we consider the element$\gamma = \alpha - e _ { i } + e _ { n + 1 }$. The element$\gamma$ belongs to J, because$\mathrm { J ^ { \natural } }$is an interval convex set containing 0. We have$\gamma _ { n + 1 } > \beta _ { n + 1 }$, and hence the augmentation property for$\mathrm { J ^ { \natural } }$gives an index$j$satisfying

$$
\gamma_ {j} <   \beta_ {j} \text { and } \alpha - e _ {i} + e _ {j} = \gamma - e _ {n + 1} + e _ {j} \in \mathrm{J}.
$$

This index$\cdot j$is necessarily different from i because$\alpha _ { i } > \beta _ { i }$. It follows that$\alpha _ { j } = \gamma _ { j } < \beta _ { j }$, and the M-convexity of J is proved.□

Lemma 2.22. Let f be a c-Rayleigh polynomial in$\mathbb { R } [ w _ { 1 } , \dots , w _ { n } ]$

(1) The support of f is interval convex.

(2) If$f ( 0 )$is nonzero, then supppfq is M<sup>6</sup>-convex.

Proof. Suppose that the polynomial$f$and the vectors$\alpha \leqslant \gamma \leqslant \beta$constitute a minimal counterexample to (1) with respect to the degree and the number of variables of$f .$We may and will suppose that$| \beta | _ { 1 }$is minimal among all such$\alpha \leqslant \gamma \leqslant \beta$for the polynomial$f .$We have

$$
\alpha_ {j} = 0 \text { for   all } j,
$$

since otherwise some contraction$\partial _ { j } f$is a smaller counterexample to (1). Similarly, we have

$$
\beta_ {j} > 0 \text {   for   all   } j,
$$

since otherwise some deletion$f \backslash j$is a smaller counterexample to (1). In addition, we may assume that$\gamma$is a unit vector, say

$$
\gamma = e _ {i},
$$

since otherwise the contraction$\partial _ { j } f$for any$j$satisfying$\gamma _ { j } > 0$is a smaller counterexample to (1). Suppose$e _ { j }$is in the support of$f$for some$j .$In this case, we should have

$$
e _ {i} + e _ {j} \in \operatorname{supp} (f),
$$

since otherwise$\partial _ { j } f$is a smaller counterexample to (1). However, the above implies

$$
\partial_ {i} f (0) = 0 \text { and } f (0) \partial_ {i} \partial_ {j} f (0) > 0,
$$

contradicting the c-Rayleigh property of$f .$. Therefore, no$e _ { j }$is in the support of$f ,$and hence

$$
| \delta | _ {1} \geqslant | \beta | _ {1} \text {   for   all   } \delta \in \operatorname{supp} (f),
$$

by the minimality of$| \beta | _ { 1 }$<sub>1</sub>. Thus, for any indices k and l satisfying$\beta \geqslant e _ { k } + e _ { l }$, we have

$$
f (\epsilon , \dots , \epsilon) = a _ {1} + \text { higher   order   terms },
$$

$$
\partial_ {k} f (\epsilon , \dots , \epsilon) = a _ {2} \epsilon^ {| \beta | _ {1} - 1} + \text { higher   order   terms },
$$

$$
\partial_ {l} f (\epsilon , \dots , \epsilon) = a _ {3} \epsilon^ {| \beta | _ {1} - 1} + \text { higher   order   terms },
$$

$$
\partial_ {k} \partial_ {l} f (\epsilon , \dots , \epsilon) = a _ {4} \epsilon^ {| \beta | _ {1} - 2} + \text { higher   order   terms },
$$

for some positive constants$a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 }$. This contradicts the c-Rayleigh property of$f$for sufficiently small positive$\epsilon ,$proving (1).

Suppose$f$is a counterexample to (2) that is minimal with respect to the degree and the number of variables of$f .$By Lemma 2.21 and (1) of the current lemma, we know that the support of$f$fails to have the augmentation property. In other words, there are α and$\beta$in the support of$f$such that$| \alpha | _ { 1 } < | \beta | .$<sub>1</sub> and, for all$i ,$

$$
\alpha_ {i} <   \beta_ {i} \Longrightarrow \alpha + e _ {i} \notin \operatorname{supp} (f).
$$

We may and will suppose that$| \alpha | .$<sub>1</sub> is minimal among all such α and$\beta$for the polynomial$f .$For any$\gamma ,$, write$S ( \gamma )$for the set of indices i such that$\gamma _ { i } > 0$. If i is in the intersection of$S ( \alpha )$and $S ( \beta )$, then$\partial _ { i } f$is a counterexample to (2) that has degree less than that of$f ,$and hence

$$
S (\alpha) \cap S (\beta) = \varnothing .
$$

Similarly, if i is not in the union of$S ( \alpha )$and$S ( \beta )$, then$f \backslash i$is a counterexample to (2) that involves less than n variables, and hence

$$
S (\alpha) \cup S (\beta) = [ n ].
$$

Since$\operatorname { s u p p } ( f )$is interval convex by (1), there is an index i in$S ( \alpha )$. In addition, since$f ( 0 )$is nonzero, we have

$$
\alpha - e _ {i} \in \operatorname{supp} (f).
$$

The vectors$\alpha - e _ { i }$and$\beta$satisfy the augmentation property for$\operatorname { s u p p } ( f ) .$, by the minimality of $| \alpha | _ { 1 }$. Therefore, there is an index$j$such that

$$
(\alpha - e _ {i}) _ {j} <   \beta_ {j} \text { and } \alpha - e _ {i} + e _ {j} \in \operatorname{supp} (f).
$$

The first condition shows that the index$j$cannot be in$S ( \alpha ) .$, so it must be in$S ( \beta )$. The vectors $\alpha - e _ { i } + e _ { j }$and$\beta$satisfy the augmentation property for supppfq, since otherwise$\partial _ { j } f$is a smaller counterexample to (2). Therefore, there is an index k such that

$$
(\alpha - e _ {i} + e _ {j}) _ {k} <   \beta_ {k} \text { and } \alpha - e _ {i} + e _ {j} + e _ {k} \in \operatorname{supp} (f).
$$

The first condition shows that the index k cannot be in$S ( \alpha )$, so it must be in$S ( \beta )$. On the other hand, since$j$and k are in$S ( \beta )$and not in$S ( \alpha )$, the failure of the augmentation property for α and$\beta$implies

$$
\alpha + e _ {j} \notin \operatorname{supp} (f) \text {   and   } \alpha + e _ {k} \notin \operatorname{supp} (f).
$$

Note that the c-Rayleigh polynomial$g : = \partial ^ { \alpha - e _ { i } } f$satisfies

$$
e _ {i}, e _ {j} + e _ {k} \in \operatorname{supp} (g) \text { and } e _ {i} + e _ {j}, e _ {i} + e _ {k} \notin \operatorname{supp} (g).
$$

The first pair of conditions shows that$g ( w ) \hat { \sigma } _ { j } \hat { \sigma } _ { k } g ( w )$is a strictly increasing function of$w _ { i }$if we set all the variables other than$w _ { i }$equal to 1. On the other hand, the second pair of conditions shows that$\partial _ { j } g ( w ) \partial _ { k } g ( w )$is independent of$w _ { i } ,$by the interval convexity of$\operatorname { s u p p } ( g )$. This contradicts the c-Rayleigh property of$^ { g , }$proving (2).□

Theorem 2.23. If f is homogeneous and c-Rayleigh, then the support of$f$is M-convex.

Proof. By (5) of Lemma 2.20 and (2) of Lemma 2.22, the support of the translation

$$
g (w _ {1}, \dots , w _ {n}) = f (w _ {1} + 1, \dots , w _ {n} + 1)
$$

is$\mathrm { M ^ { \circ } - c o n v e x }$. In other words, the support J of the homogenization of$g$is M-convex. Since the intersection of an M-convex set with a coordinate hyperplane is M-convex, this implies the M-convexity of the support of$f .$.□

A multi-affine polynomial f is said to be strongly Rayleigh if

$$
f (w) \partial_ {i} \partial_ {j} f (w) \leqslant \partial_ {i} f (w) \partial_ {j} f (w) \text {   for   all   distinct   } i, j \in [ n ], \text {   and   } w \in \mathbb {R} ^ {n}.
$$

Clearly, any strongly Rayleigh multi-affine polynomial is 1-Rayleigh. Since a multi-affine polynomial is stable if and only if it is strongly Rayleigh [Bra07 ¨ , Theorem 5.6], Theorem 2.23 extends the following theorem of Choe et al. [COSW04, Theorem 7.1]: If$f$is a nonzero homogeneous stable multi-affine polynomial, then the support of$f$is the set of bases of a matroid.

Lastly, we show that the bound in Proposition 2.19 is optimal.

Proposition 2.24. When$n \leqslant 2 ,$all polynomials in$\mathrm { L } _ { n } ^ { d }$are 1-Rayleigh. When$n \geqslant 3 ,$we have

$$
\left(\text { all   polynomials   in } \mathrm{L} _ {n} ^ {d} \text { are } c \text {-Rayleigh}\right) \Longrightarrow c \geqslant 2 \left(1 - \frac {1}{d}\right).
$$

In other words, for any$n \geqslant 3$and any$\begin{array} { r } { c < 2 \Big ( 1 - \frac { 1 } { d } \Big ) } \end{array}$, there is$f \in \mathrm { L } _ { n } ^ { d }$that is not c-Rayleigh.

Proof. We first show by induction that, for any homogeneous bivariate polynomial$f = f ( w _ { 1 } , w _ { 2 } )$ with nonnegative coefficients, we have

$$
f (w) \left(\partial_ {1} \partial_ {2} f (w)\right) \leqslant \left(\partial_ {1} f (w)\right) \left(\partial_ {2} f (w)\right) \text {   for   any   } w \in \mathbb {R} _ {\geqslant 0} ^ {2}.
$$

We use the obvious fact that, for any homogeneous polynomial with nonnegative coefficients$h ,$,

$$
\left(\deg (h) + 1\right) h \geqslant \left(1 + w _ {i} \partial_ {i}\right) h \text {   for   any   } i \in [ n ] \text {   and   } w \in \mathbb {R} _ {\geqslant 0} ^ {n}.
$$

Since$f$is bivariate, we may write$f = c _ { 1 } w _ { 1 } ^ { d } + c _ { 2 } w _ { 2 } ^ { d } + w _ { 1 } w _ { 2 } g .$. We have

$$
\begin{array}{r l} & {\partial_ {1} f \partial_ {2} f - f \partial_ {1} \partial_ {2} f = d ^ {2} c _ {1} c _ {2} w _ {1} ^ {d - 1} w _ {2} ^ {d - 1}} \\ & {\qquad + d c _ {1} w _ {1} ^ {d} (1 + w _ {2} \partial_ {2}) g - c _ {1} w _ {1} ^ {d} (1 + w _ {1} \partial_ {1}) (1 + w _ {2} \partial_ {2}) g} \\ & {\qquad + d c _ {2} w _ {2} ^ {d} (1 + w _ {1} \partial_ {1}) g - c _ {2} w _ {2} ^ {d} (1 + w _ {1} \partial_ {1}) (1 + w _ {2} \partial_ {2}) g} \\ & {\qquad + w _ {1} w _ {2} (g + w _ {1} \partial_ {1} g) (g + w _ {2} \partial_ {2} g) - w _ {1} w _ {2} g (1 + w _ {1} \partial_ {1}) (1 + w _ {2} \partial_ {2}) g.} \end{array}
$$

The summand in the second line is nonnegative on$\mathbb { R } _ { \geq 0 } ^ { 2 }$by the mentioned fact for$( 1 + w _ { 2 } \partial _ { 2 } ) g$ The summand in the third line is nonnegative on$\mathbb { R } _ { \geqslant 0 } ^ { 2 }$by the mentioned fact for$( 1 + w _ { 1 } \partial _ { 1 } ) g$. The summand in the fourth line is nonnegative on$\mathbb { R } _ { \geq 0 } ^ { 2 }$by the induction hypothesis applied to$g .$

We next show that, for any bivariate Lorentzian polynomial$f = f ( w _ { 1 } , w _ { 2 } )$, we have

$$
f (w) \left(\partial_ {1} \partial_ {1} f (w)\right) \leqslant \left(\partial_ {1} f (w)\right) \left(\partial_ {1} f (w)\right) \text {   for   any   } w \in \mathbb {R} _ {\geqslant 0} ^ {2}.
$$

Since$f$is homogeneous, it is enough to prove the inequality when$w _ { 2 } = 1$. In this case, the inequality follows from the concavity of the function log$f$restricted to the line$w _ { 2 } = 1$. This completes the proof that any bivariate Lorentzian polynomial is 1-Rayleigh.

To see the second statement, consider the polynomial

$$
f = 2 \bigg (1 - \frac {1}{d} \bigg) w _ {1} ^ {d} + w _ {1} ^ {d - 1} w _ {2} + w _ {1} ^ {d - 1} w _ {3} + w _ {1} ^ {d - 2} w _ {2} w _ {3}.
$$

It is straightforward to check that$f$is in$\operatorname { L } _ { n } ^ { d } . \operatorname { I f } f$is c-Rayleigh, then, for any$w \in \mathbb { R } _ { \geq 0 } ^ { n } ,$

$$
w _ {1} ^ {2 d - 4} \left(2 \left(1 - \frac {1}{d}\right) w _ {1} ^ {2} + w _ {1} w _ {2} + w _ {1} w _ {3} + w _ {2} w _ {3}\right) \leqslant c w _ {1} ^ {2 d - 4} \left(w _ {1} + w _ {2}\right) \left(w _ {1} + w _ {3}\right).
$$

The desired lower bound for c is obtained by setting$w _ { 1 } = 1 , w _ { 2 } = 0 , w _ { 3 } = 0 .$

2.4. Characterizations of Lorentzian polynomials. We may now give a complete and useful description of the space of Lorentzian polynomials. As before, we write$\mathrm { H } _ { n } ^ { d }$for the space of degree d homogeneous polynomials in n variables.

Theorem 2.25. The closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$in$\mathrm { H } _ { n } ^ { d }$is$\mathrm { L } _ { n } ^ { d }$. In particular,$\mathrm { L } _ { n } ^ { d }$is a closed subset of$\mathrm { H } _ { n } ^ { d }$

Proof. By Theorem 2.13, the closure of$\mathring { \mathrm { L } } _ { n } ^ { d }$contains$\mathrm { L } _ { n } ^ { d }$. Since any limit of c-Rayleigh polynomials must be c-Rayleigh, the other inclusion follows from Theorem 2.23 and Proposition 2.19.□

Therefore, a degree d homogeneous polynomial$f$with nonnegative coefficients is Lorentzian if and only if the support of f is M-convex and$\partial ^ { \alpha } f$has at most one positive eigenvalue for every $\alpha \in \Delta _ { n } ^ { d - 2 }$. In other words, Definitions 2.1 and 2.6 define the same class of polynomials.

Example 2.26. A sequence of nonnegative numbers$a _ { 0 } , a _ { 1 } , \ldots , a _ { d }$is said to be ultra log-concave if

$$
\frac {a _ {k} ^ {2}}{\binom {d} {k} ^ {2}} \geqslant \frac {a _ {k - 1}}{\binom {d} {k - 1}} \frac {a _ {k + 1}}{\binom {d} {k + 1}} \quad \text { for   all } 0 <   k <   d.
$$

The sequence is said to have no internal zeros if

$$
a _ {k _ {1}} a _ {k _ {3}} > 0 \Longrightarrow a _ {k _ {2}} > 0 \quad \text {   for   all   } 0 \leqslant k _ {1} <   k _ {2} <   k _ {3} \leqslant d.
$$

Recall from Example 2.3 that a bivariate homogeneous polynomial$\scriptstyle \sum _ { k = 0 } ^ { d } a _ { k } w _ { 1 } ^ { k } w _ { 2 } ^ { d - k }$is strictly Lorentzian if and only if the sequence$a _ { k }$is positive and strictly ultra log-concave. Theorem 2.25 says that, in this case, the polynomial$\scriptstyle \sum _ { k = 0 } ^ { d } a _ { k } w _ { 1 } ^ { k } w _ { 2 } ^ { d - k }$is Lorentzian if and only if the sequence $a _ { k }$is nonnegative, ultra log-concave, and has no internal zeros.

Example 2.27. Using Theorem 2.25, it is straightforward to check that elementary symmetric polynomials are Lorentzian. In fact, one can show more generally that all normalized Schur polynomials are Lorentzian [HMMS, Theorem 3]. Any elementary symmetric polynomial is stable [COSW04, Theorem 9.1], but a normalized Schur polynomial need not be stable [HMMS, Example 9].

Let$\mathbb { P } \mathrm { H } _ { n } ^ { d }$be the projectivization of$\mathrm { H } _ { n } ^ { d }$equipped with the quotient topology. The image$\mathbb { P } \mathrm { L } _ { n } ^ { d }$ of$\mathrm { L } _ { n } ^ { d }$in the projective space is homeomorphic to the intersection of$\mathrm { L } _ { n } ^ { d }$with the unit sphere in $\mathrm { H } _ { n } ^ { d }$for the Euclidean norm on the coefficients.

Theorem 2.28. The space$\mathbb { P } \mathrm { L } _ { n } ^ { d }$is compact and contractible.

Proof. Since$\mathbb { P } \mathrm { H } _ { n } ^ { d }$is compact, Theorem 2.25 implies that$\mathbb { P } \mathrm { L } _ { n } ^ { d }$is compact. A deformation retract of$\mathbb { P } \mathrm { L } _ { n } ^ { d }$can be constructed using Theorem 2.10.□

We conjecture that$\mathbb { P } \mathrm { L } _ { n } ^ { d }$is homeomorphic to a familiar space.

Conjecture 2.29. The space$\mathbb { P } \mathrm { L } _ { n } ^ { d }$is homeomorphic to a closed Euclidean ball.

For other appearances of stratified Euclidean balls in the interface of analysis of combinatorics, see [GKL, GKL19] and references therein. Prominent examples are the totally nonnegative parts of Grassmannian and other partial$\mathrm { f l a g }$varieties.

Let$f$be a polynomial in n variables with nonnegative coefficients. In [Gur09], Gurvits defines$f$to be strongly log-concave${ \mathrm { i f } } ,$for all$\alpha \in \mathbb { N } ^ { n }$

$\partial ^ { \alpha } f$is identically zero or log$( \partial ^ { \alpha } f )$is concave on$\mathbb { R } _ { > 0 } ^ { n }$

In [AOVI], Anari et al. define$f$to be completely log-concave${ \mathrm { i f } } ,$for all m P N and any$m \times n$matrix $( a _ { i j } )$with nonnegative entries,

$$
\left(\prod_ {i = 1} ^ {m} D _ {i}\right) f \text {   is   identically   zero   or   } \log \left(\left(\prod_ {i = 1} ^ {m} D _ {i}\right) f\right) \text {   is   concave   on   } \mathbb {R} _ {> 0} ^ {n},
$$

where$D _ { i }$is the differential operator$\textstyle \sum _ { j = 1 } ^ { n } a _ { i j } { \widehat { \boldsymbol { O } } } _ { j }$. We show that the two notions agree with each other and with the Lorentzian property for homogeneous polynomials.<sup>8</sup>

Theorem 2.30. The following conditions are equivalent for any homogeneous polynomial$f .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p3q ñ p1q</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>An implication similar to of Theorem 2.30 can be found in [ALOVIII, Theorem 3.2].</span></small>

(1) f is completely log-concave.

(2) f is strongly log-concave.

(3) f is Lorentzian.

The support of any Lorentzian polynomial is M-convex by Theorem 2.25. Thus, by Theorem 2.30, the same holds for any strongly log-concave homogeneous polynomial. This answers a question of Gurvits [Gur09, Section 4.5 (iii)].

Corollary 2.31. The support of any strongly log-concave homogeneous polynomial is M-convex.

Similarly, we can use Theorem 2.30 to show that the class of strongly log-concave homogeneous polynomials is closed under multiplication. This answers another question of Gurvits [Gur09, Section 4.5 (iv)] for homogeneous polynomials.

Corollary 2.32. The product of strongly log-concave homogeneous polynomials is strongly logconcave.

Proof. Let$f ( w )$be an element of$\mathrm { L } _ { n } ^ { d } .$, and let$g ( w )$be an element of$\mathrm { L } _ { n } ^ { e }$. It is straightforward to check that$f ( w ) g ( u )$is an element of$\mathrm { L } _ { n + n } ^ { d + e } ,$where u is a set of variables disjoint from$w .$It follows that$f ( w ) g ( w )$is an element of$\mathrm { L } _ { n } ^ { d + e }$, since setting$u = w$preserves the Lorentzian property by Theorem 2.10.□

Corollary 2.32 extends the following theorem of Liggett$\mathrm { [ L i g 9 7 ] }$, Theorem$2 ] { \mathrm { : } }$: The convolution product of two ultra log-concave sequences with no internal zeros is an ultra log-concave sequence with no internal zeros.

To prove Theorem 2.30, we use the following elementary observation. Let$f$be a homogeneous polynomial in$n \geqslant 2$variables of degree d$\geqslant 2$

Proposition 2.33. The following are equivalent for any$w \in \mathbb { R } ^ { n }$satisfying$f ( w ) > 0$

(1) The Hessian of$f ^ { 1 / d }$is negative semidefinite at w.

(2) The Hessian of log f is negative semidefinite at w.

(3) The Hessian of f has exactly one positive eigenvalue at w.

The equivalence of (2) and (3) appears in [AOVI].

Proof. We fix w throughout the proof. For$n \times n$symmetric matrices A and B, we write$\mathrm { ~ A ~ } \prec \mathrm { ~ B ~ }$ to mean the following interlacing relationship between the eigenvalues of A and B:

$$
\lambda_ {1} (\mathrm{A}) \leqslant \lambda_ {1} (\mathrm{B}) \leqslant \lambda_ {2} (\mathrm{A}) \leqslant \lambda_ {2} (\mathrm{B}) \leqslant \dots \leqslant \lambda_ {n} (\mathrm{A}) \leqslant \lambda_ {n} (\mathrm{B}).
$$

Let$\mathcal { \mathrm { H } } _ { 1 } , \mathcal { \mathrm { H } } _ { 2 }$, and$\mathcal { H } _ { 3 }$for the Hessians of$f ^ { 1 / d }$, log$f ,$and$f ,$respectively. We have

$$
d f ^ {- 1 / d} \mathcal {H} _ {1} = \mathcal {H} _ {2} + \frac {1}{d} f ^ {- 2} (\operatorname{grad} f) (\operatorname{grad} f) ^ {T} \text {and} \mathcal {H} _ {2} = f ^ {- 1} \mathcal {H} _ {3} - f ^ {- 2} (\operatorname{grad} f) (\operatorname{grad} f) ^ {T}.
$$

Since$( \operatorname { g r a d } f ) ( \operatorname { g r a d } f ) ^ { T }$is positive semidefinite of rank one, Weyl’s inequalities for Hermitian matrices [Ser10, Theorem 6.3] show that

$$
\mathcal {H} _ {2} \prec \mathcal {H} _ {1} \text { and } \mathcal {H} _ {2} \prec \mathcal {H} _ {3} \text { and } \mathcal {H} _ {1} \prec \mathcal {H} _ {3}.
$$

Since$w ^ { T } \mathcal { H } _ { 3 } w = d ( d - 1 ) f , \mathcal { H } _ { 3 }$has at least one positive eigenvalue, and hence$( 1 ) \Rightarrow ( 2 ) \Rightarrow ( 3 )$

For$( 3 ) \Rightarrow ( 1 )$, suppose that$\mathcal { H } _ { 3 }$has exactly one positive eigenvalue. We introduce a positive real parameter ϵ and consider the polynomial

$$
f _ {\epsilon} = f - \epsilon (w _ {1} ^ {d} + \dots + w _ {n} ^ {d}).
$$

We write$\mathcal { \mathrm { H } } _ { 3 , \epsilon }$for the Hessian of$f _ { \epsilon } ,$, and write$\mathcal { \mathrm { H } } _ { 1 , \epsilon }$for the Hessian of$f _ { \epsilon } ^ { 1 / d }$.

Note that${ \mathcal { H } } _ { 3 } ,$<sub>ϵ</sub> is nonsingular and has exactly one positive eigenvalue for all sufficiently small positive ϵ. In addition, we have$\mathcal { H } _ { 1 , \epsilon } ~ \prec ~ \mathcal { H } _ { 3 , \epsilon } ,$, and hence$\mathcal { \mathrm { H } } _ { 1 , \epsilon }$has at most one nonnegative eigenvalue for all sufficiently small positive ϵ. However, by Euler’s formula for homogeneous functions, we have

$$
\mathcal {H} _ {1, \epsilon} w = 0,
$$

so that 0 is the only nonnegative eigenvalue of$\mathcal { \mathrm { H } } _ { 1 , \epsilon }$for any such ϵ. The implication$( 3 ) \Rightarrow ( 1 )$ now follows by limiting ϵ to 0.□

It follows that, for any nonzero degree d$\geqslant 2$homogeneous polynomial f with nonnegative coefficients, the following conditions are equivalent:

– The function$f ^ { 1 / d }$is concave on$\mathbb { R } _ { > 0 } ^ { n }$

– The function log f is concave on$\mathbb { R } _ { > 0 } ^ { n }$

– The Hessian of f has exactly one positive eigenvalue on$\mathbb { R } _ { > 0 } ^ { n } .$

Proof of Theorem 2.30. We may suppose that f has degree d$\geqslant 2 .$. Clearly, completely log-concave polynomials are strongly log-concave.

Suppose f is a strongly log-concave homogeneous polynomial of degree d. By Proposition 2.33, either$\partial ^ { \alpha } f$is identically zero or the Hessian of$\partial ^ { \alpha } f$has exactly one positive eigenvalue on $\mathbb { R } _ { > 0 } ^ { n }$for all$\alpha \in \mathbb { N } ^ { n }$. By Proposition 2.17, f is$2 \left( 1 - { \frac { 1 } { d } } \right)$-Rayleigh, and hence, by Theorem 2.23, the support of f is M-convex. Therefore, by Theorem 2.25, f is Lorentzian.

Suppose f is a nonzero Lorentzian polynomial. Theorem 2.16 and Proposition 2.33 together show that log f is concave on$\mathbb { R } _ { > 0 } ^ { n } .$. Therefore, it is enough to prove that$\textstyle { \bigl ( } \sum _ { i = 1 } ^ { n } a _ { i } { \hat { o } } _ { i } { \bigr ) } f$is Lorentzian for any nonnegative numbers$a _ { 1 } , \ldots , a _ { n }$. This is a direct consequence of Theorem 2.25 and Corollary 2.11.□

## 3. ADVANCED THEORY

3.1. Linear operators preserving Lorentzian polynomials. We describe a large class of linear operators that preserve the Lorentzian property. An analog was achieved for the class of stable polynomials in [BB09, Theorem 2.2], where the linear operators preserving stability were characterized. For an element κ of$\mathbb { N } ^ { n }$, we set

$$
\mathbb {R} _ {\kappa} \left[ w _ {i} \right] = \left\{\text { polynomials   in } \mathbb {R} \left[ w _ {i} \right] _ {1 \leqslant i \leqslant n} \text { of   degree   at   most } \kappa_ {i} \text { in } w _ {i} \text { for   every } i \right\},
$$

$$
\mathbb {R} _ {\kappa} ^ {\mathrm{a}} \left[ w _ {i j} \right] = \left\{\text { multi - affine   polynomials   in } \mathbb {R} \left[ w _ {i j} \right] _ {1 \leqslant i \leqslant n, 1 \leqslant j \leqslant \kappa_ {i}} \right\}.
$$

The projection operator$\Pi _ { \kappa } ^ { \downarrow } : \mathbb { R } _ { \kappa } ^ { \mathrm { a } } [ w _ { i j } ]  \mathbb { R } _ { \kappa } [ w _ { i } ]$is the linear map that substitutes each$w _ { i j }$by w<sub>i</sub>:

$$
\Pi_ {\kappa} ^ {\downarrow} (g) = g | _ {w _ {i j} = w _ {i}}.
$$

The polarization operator$\Pi _ { \kappa } ^ { \uparrow } : \mathbb { R } _ { \kappa } [ w _ { i } ]  \mathbb { R } _ { \kappa } ^ { \mathrm { a } } [ w _ { i j } ]$is the linear map that sends$w ^ { \alpha }$to the product

$\frac { 1 } { { \binom { \kappa } { \alpha } } } \prod _ { i = 1 } ^ { n }$\`elementary symmetric polynomial of degree$\alpha _ { i }$in the variables$\{ w _ { i j } \} _ { 1 \leqslant j \leqslant \kappa _ { i } } )$，

where$\binom { \kappa } { \alpha }$stands for the product of binomial coefficients$\textstyle \prod _ { i = 1 } ^ { n } { \binom { \kappa _ { i } } { \alpha _ { i } } }$. Note that

– for every$f ,$we have$\Pi _ { \kappa } ^ { \downarrow } \circ \Pi _ { \kappa } ^ { \uparrow } ( f ) = f ,$, and

– for every$f$and every$i ,$the polynomial$\Pi _ { \kappa } ^ { \uparrow } ( f )$is symmetric in the variables$\{ w _ { i j } \} _ { 1 \leqslant j \leqslant \kappa _ { i } }$

The above properties characterize$\Pi _ { \kappa } ^ { \uparrow }$among the linear operators from$\mathbb { R } _ { \kappa } [ \boldsymbol { w } _ { i } ]$to$\mathbb { R } _ { \kappa } ^ { \mathrm { a } } [ w _ { i j } ]$

Proposition 3.1. The operators$\Pi _ { \kappa } ^ { \downarrow }$and$\Pi _ { \kappa } ^ { \uparrow }$preserve the Lorentzian property.

In other words,$\Pi _ { \kappa } ^ { \uparrow } ( f )$is a Lorentzian polynomial for any Lorentzian polynomial$f \in \mathbb { R } _ { \kappa } [ w _ { i } ] ,$ and$\Pi _ { \kappa } ^ { \downarrow } ( g )$is a Lorentzian polynomial for any Lorentzian polynomial$g \in \mathbb { R } _ { \kappa } ^ { \mathrm { a } } [ w _ { i j } ]$

Proof. The statement for$\Pi _ { \kappa } ^ { \downarrow }$follows from Theorem 2.10. We prove the statement for$\Pi _ { \kappa } ^ { \uparrow }$. It is enough to prove that$\Pi _ { \kappa } ^ { \uparrow } ( f )$is Lorentzian when$f \in \mathring { \mathrm { L } } _ { n } ^ { d } \cap \mathbb { R } _ { \kappa } [ w _ { i } ]$for d$\geqslant 2 .$

Set$k = | { \boldsymbol { \kappa } } | _ { 1 }$, and identify$\mathbb { N } ^ { k }$with the set of all monomials in$w _ { i j }$. Since$f \in \mathring { \mathrm { L } } _ { n } ^ { d } ,$, we have

$$
\operatorname{supp} \bigl (\Pi_ {\kappa} ^ {\uparrow} (f) \bigr) = \left[ \begin{array}{c} k \\ d \end{array} \right],
$$

which is clearly M-convex. Therefore, by Theorem 2.25, it remains to show that the quadratic form$\partial ^ { \beta } \Pi _ { \kappa } ^ { \uparrow } ( f )$is stable for any$\beta \in \left[ { k ^ { \atop d - 2 } } \right]$

Define α by the equality$\Pi _ { \kappa } ^ { \downarrow } ( w ^ { \beta } ) = w ^ { \alpha }$. Note that, after renaming the variables if necessary, the$\beta \mathrm { - t h }$partial derivative of$\Pi _ { \kappa } ^ { \uparrow } ( f )$is a positive multiple of a polarization of the α-th partial derivative of$f \colon$

$$
\partial^ {\beta} \Pi_ {\kappa} ^ {\uparrow} (f) = \frac {(\kappa - \alpha) !}{\kappa !} \Pi_ {\kappa - \alpha} ^ {\uparrow} (\partial^ {\alpha} f).
$$

Since the operator$\Pi _ { \kappa - \alpha } ^ { \uparrow }$preserves stability [BB09, Proposition$3 . 4 ] ,$the conclusion follows from the stability of the quadratic form$\partial ^ { \alpha } f$□

Let κ be an element of$\mathbb { N } ^ { n }$, let γ be an element of$\mathbb { N } ^ { m }$, and set$k = | { \boldsymbol { \kappa } } | _ { 1 }$. In the remainder of this section, we fix a linear operator

$$
T: \mathbb {R} _ {\kappa} [ w _ {i} ] \to \mathbb {R} _ {\gamma} [ w _ {i} ],
$$

and suppose that the linear operator$T$is homogeneous of degree ℓ for some$\ell \in \mathbb { Z } :$

$$
\left(0 \leqslant \alpha \leqslant \kappa \text {   and   } T (w ^ {\alpha}) \neq 0\right) \Longrightarrow \deg T (w ^ {\alpha}) = \deg w ^ {\alpha} + \ell .
$$

The symbol of T is a homogeneous polynomial of degree$k + \ell$in$m + n$variables defined by

$$
\mathbf {s y m} _ {T} (w, u) = \sum_ {0 \leqslant \alpha \leqslant \kappa} {\binom {\kappa} {\alpha}} T (w ^ {\alpha}) u ^ {\kappa - \alpha}.
$$

We show that the homogeneous operator$T$preserves the Lorentzian property if its symbol sym is Lorentzian.

Theorem 3.2. If sy$\mathbf { m } _ { T } \in \mathrm { L } _ { m + n } ^ { k + \ell }$and$f \in \mathrm { L } _ { n } ^ { d } \cap \mathbb { R } _ { \kappa } [ w _ { i } ] , \mathrm { t h e n } T ( f ) \in \mathrm { L } _ { m } ^ { d + \ell } .$

When$n = 2 ,$Theorem 3.2 provides a large class of linear operators that preserve the ultra logconcavity of sequences of nonnegative numbers with no internal zeros. We prepare the proof of Theorem 3.2 with a special case.

Lemma 3.3. Let$T = T _ { w _ { 1 } , w _ { 2 } } : \mathbb { R } _ { ( 1 , \ldots , 1 ) } [ w _ { i } ] \to \mathbb { R } _ { ( 1 , \ldots , 1 ) } [ w _ { i } ]$be the linear operator defined by

$$
T (w ^ {S}) = \left\{ \begin{array}{c l} w ^ {S \setminus 1} & \text { if } 1 \in S \text { and } 2 \in S, \\ w ^ {S \setminus 1} & \text { if } 1 \in S \text { and } 2 \notin S, \\ w ^ {S \setminus 2} & \text { if } 1 \notin S \text { and } 2 \in S, \\ 0 & \text { if } 1 \notin S \text { and } 2 \notin S, \end{array} \right. \text { for   all } S \subseteq [ n ].
$$

Then$T$preserves the Lorentzian property.

Proof. It is enough to prove that$T ( f ) \in { \mathrm { L } } _ { n } ^ { d }$when$f \in \mathring { \mathrm { L } } _ { n } ^ { d + 1 } \cap \mathbb { R } _ { ( 1 , \dots , 1 ) } [ w _ { i } ]$for d$\geqslant 2 .$. In this case,

$$
\operatorname{supp} (T (f)) = \left\{d \text {-element subsets of} [ n ] \text { not   containing } 1 \right\},
$$

which is clearly M-convex. Therefore, by Theorem 2.25, it suffices to show that the quadratic form$\partial ^ { S } T ( f )$is stable for any$S \in \left[ { n \atop d - 2 } \right]$not containing 1. We write h for the Lorentzian polynomial$f | _ { w _ { 1 } = 0 }$. Since$f$is multi-affine, we have

$$
f = h + w _ {1} \partial_ {1} f \text { and } T (f) = \partial_ {2} h + \partial_ {1} f.
$$

We give separate arguments when$2 \in S$and$2 \notin S$. If S contains 2, then

$$
\partial^ {S} T (f) = \partial^ {S \cup 1} f,
$$

and hence$\partial ^ { S } T ( f )$is stable. If S does not contain 2, then

– the linear form$\hat { \sigma } ^ { S } \hat { o } _ { 1 } \hat { o } _ { 2 } f = \hat { \sigma } ^ { S \cup 1 \cup 2 } f$is not identically zero, because$f \in \mathring { \mathrm { L } } _ { n } ^ { d + 1 }$

– we have$\partial ^ { S \cup 1 \cup 2 } f < \partial ^ { S \cup 2 } h$, because$\partial ^ { S \cup 2 } f$is stable, and

– we have$\begin{array} { r } { \hat { \mathcal { O } } ^ { S \cup 1 \cup 2 } f < \hat { \mathcal { O } } ^ { S \cup 1 } f , } \end{array}$by Lemma 2.9 (1).

Therefore, by Lemma 2.9 (4), the quadratic form$\partial ^ { S } T ( f ) = \partial ^ { S \cup 2 } h + \partial ^ { S \cup 1 } f$is stable.

Proof of Theorem 3.2. The polarization of$T : \mathbb { R } _ { \kappa } [ w _ { i } ]  \mathbb { R } _ { \gamma } [ w _ { i } ]$is the operator$\Pi ^ { \uparrow } ( T )$defined by

$$
\Pi^ {\uparrow} (T) = \Pi_ {\gamma} ^ {\uparrow} \circ T \circ \Pi_ {\kappa} ^ {\downarrow}.
$$

We write$\gamma \bigoplus \kappa$for the concatenation of$\gamma$and κ in$\mathbb { N } ^ { m + n }$. By [BB09, Lemma 3.5], the symbol of the polarization is the polarization of the symbol<sup>9</sup>:

$$
\operatorname{sym} _ {\Pi^ {\uparrow} (T)} = \Pi_ {\gamma \oplus \kappa} ^ {\uparrow} (\operatorname{sym} _ {T}).
$$

Therefore, by Proposition 3.1, the proof reduces to the case$\kappa = ( 1 , \ldots , 1 )$and$\gamma = ( 1 , \ldots , 1 )$

Suppose$f ( v )$is a multi-affine polynomial in$\mathrm { L } _ { n } ^ { d }$and$\mathsf { s y m } _ { T } ( w , u )$is a multi-affine polynomial in$\mathrm { L } _ { m + n } ^ { \ell + n }$. Since the product of Lorentzian polynomials is Lorentzian by Corollary 2.32, we have

$$
\mathbf {s y m} _ {T} (w, u) f (v) = \sum_ {S \subseteq [ n ]} T (w ^ {S}) u ^ {[ n ] \setminus S} f (v) \in \mathrm{L} _ {m + n + n} ^ {d + \ell + n}.
$$

Applying the operator in Lemma 3.3 for the pair of variables$( u _ { i } , v _ { i } )$for$i = 1 , \ldots , n ,$we have

$$
\prod_ {i = 1} ^ {n} T _ {u _ {i}, v _ {i}} \bigl (\mathsf {s y m} _ {T} (w, u) f (v) \bigr) = \sum_ {S \subseteq [ n ]} T (w ^ {S}) (\partial^ {S} f) (v) \in \mathrm{L} _ {m + n} ^ {d + \ell}.
$$

We substitute every$v _ { i }$by zero in the displayed equation to get

$$
\Big [ \sum_ {S \subseteq [ n ]} T (w ^ {S}) (\partial^ {S} f) (v) \Big ] _ {v = 0} = T \big (f (w) \big).
$$

Theorem 2.10 shows that the right-hand side belongs to$\mathrm { L } _ { m } ^ { d + \ell } .$, completing the proof.□

We remark that there are homogeneous linear operators$T$preserving the Lorentzian property whose symbols are not Lorentzian. This contrasts the analog of Theorem 3.2 for stable polynomials [BB09, Theorem 2.2]. As an example, consider the linear operator$T : \mathbb { R } _ { ( 1 , 1 ) } [ w _ { 1 } , w _ { 2 } ] \to$ $\mathbb { R } _ { ( 1 , 1 ) } [ w _ { 1 } , w _ { 2 } ]$defined by

$$
T (1) = 0, \quad T (w _ {1}) = w _ {1}, \quad T (w _ {2}) = w _ {2}, \quad T (w _ {1} w _ {2}) = w _ {1} w _ {2}.
$$

The symbol of$T$is not Lorentzian because its support is not M-convex. The operator T preserves Lorentzian polynomials but does not preserve (non-homogeneous) stable polynomials.

Theorem 3.4. If T is a homogeneous linear operator that preserves stable polynomials and polynomials with nonnegative coefficients, then$T$preserves Lorentzian polynomials.

Proof. According to [BB09, Theorem 2.2], T preserves stable polynomials if and only if either

(I) the rank of$T$is not greater than two and$T$is of the form

$$
T (f) = \alpha (f) P + \beta (f) Q,
$$

where$\alpha , \beta$are linear functionals and$P , Q$are stable polynomials satisfying$P \prec Q$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">m = n</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>The statement was proved in [BB09, Lemma 3.5] when m “ n. Clearly, this special case implies the general case.</span></small>

(II) the polynomial$\mathsf { s y m } _ { T } ( w , u )$is stable, or

(III) the polynomial$\mathrm { s y m } _ { T } ( w , - u )$is stable.

Suppose one of the three conditions, and suppose in addition that T preserves polynomials with nonnegative coefficients.

Suppose (I) holds. In this case, the image of T is contained in the set of stable polynomials [BB10, Theorem 1.6]. By Proposition 2.2, homogeneous stable polynomials with nonnegative coefficients are Lorentzian. Since T preserves polynomials with nonnegative coefficients,$T ( f )$ is Lorentzian whenever$f$is a homogeneous polynomial with nonnegative coefficients.

Suppose (II) holds. Since T preserves polynomials with nonnegative coefficients, sym$\boldsymbol { \mathbf { \rho } } _ { T } ( w , u )$ is Lorentzian by Proposition 2.2. Therefore, by Theorem$3 . 2 , T ( f )$is Lorentzian whenever$f$is Lorentzian.

Suppose (III) holds. Since all the nonzero coefficients of a homogeneous stable polynomial have the same sign [COSW04, Theorem 6.1], we have

$$
\mathbf {s y m} _ {T} (w, - v) = \mathbf {s y m} _ {T} (w, v) \text {or} \mathbf {s y m} _ {T} (w, - v) = - \mathbf {s y m} _ {T} (w, v).
$$

In both cases,$\mathsf { s y m } _ { T } ( w , v )$is stable and has nonnegative coefficients. Thus$\mathsf { s y m } _ { T } ( w , v )$is Lorentzian, and the conclusion follows from Theorem 3.2.□

In the remainder of this section, we record some useful operators that preserves the Lorentzian property. The multi-affine part of a polynomial$\textstyle \sum _ { \alpha \in \mathbb { N } ^ { n } } c _ { \alpha } w ^ { \alpha }$is the polynomial$\textstyle \sum _ { \alpha \in \{ 0 , 1 \} ^ { n } } c _ { \alpha } w ^ { \alpha }$

Corollary 3.5. The multi-affine part of any Lorentzian polynomial is a Lorentzian polynomial.

Proof. Clearly, taking the multi-affine part is a homogeneous linear operator that preserves polynomials with nonnegative coefficients. Since this operator also preserves stable polynomials [COSW04, Proposition 4.17], the proof follows from Theorem 3.4.□

Remark 3.6. Corollary 3.5 can be used to obtain a multi-affine analog of Theorem 2.28. Write$\underline { { \mathrm { H } } } _ { n } ^ { d }$ for the space of multi-affine degree d homogeneous polynomials in n variables, and write$\underline { { \mathrm { L } } } _ { n } ^ { d }$for the corresponding set of multi-affine Lorentzian polynomials. Let$\mathbb { P } \underline { { \mathrm { H } } } _ { n } ^ { d }$be the projectivization of the vector space$\underline { { \mathrm { H } } } _ { n } ^ { d } ,$, and let$\underline { { \mathrm { L } } } _ { \mathrm { B } }$be the set of polynomials in$\underline { { \mathrm { L } } } _ { n } ^ { d }$with support B. We identify a rank d matroid M on rns with its set of bases$\mathrm { B } \subseteq [ _ { d } ^ { n } ]$. Writing$\mathbb { P } \underline { { \mathrm { L } } } _ { n } ^ { d }$and$\mathbb { P } \underline { { \mathrm { L } } } _ { \mathrm { B } }$for the images of $\underline { { \mathrm { L } } } _ { n } ^ { d } \backslash 0$and$\underline { { \mathrm { L } } } _ { \mathrm { B } }$in$\mathbb { P } \underline { { \mathrm { H } } } _ { n } ^ { d }$respectively, we have

$$
\mathbb {P} \underline {{\mathrm{L}}} _ {n} ^ {d} = \coprod_ {\mathrm{B}} \mathbb {P} \underline {{\mathrm{L}}} _ {\mathrm{B}},
$$

where the union is over all rank d matroids on rns. By Theorem 2.10 and Corollary 3.5, P$\underline { { \underline { { d } } } } _ { n } ^ { d }$ is a compact contractible subset of$\mathbb { P } \underline { { \mathrm { H } } } _ { n } ^ { d }$. By Theorem$3 . 1 0 , \mathbb { P } \underline { { \mathrm { L } } } _ { \mathrm { B } }$is nonempty for every matroid $\mathrm { B } \subseteq [ _ { d } ^ { n } ]$. In addition, by Proposition$3 . 2 5 , \mathbb { P } \underline { { \mathrm { L } } } _ { \mathrm { B } }$is contractible for every matroid$\mathrm { B } \subseteq [ _ { d } ^ { n } ]$

Let N be the linear operator defined by the condition$\begin{array} { r } { N ( w ^ { \alpha } ) = \frac { w ^ { \alpha } } { \alpha ! } } \end{array}$. The normalization operator N turns generating functions into exponential generating functions.

Corollary 3.7. If f is a Lorentzian polynomial, then$N ( f )$is a Lorentzian polynomial.

It is shown in [HMMS, Theorem 3] that the normalized Schur polynomial$N ( s _ { \lambda } ( w _ { 1 } , \dots , w _ { n } ) )$ is Lorentzian for any partition λ. Note that the converse of Corollary 3.7 fails in general. For example, complete symmetric polynomials, which are special cases of Schur polynomials, need not be Lorentzian.

Proof. Let κ be any element of$\mathbb { N } ^ { n }$. By Theorem 3.2, it suffices to show that the symbol

$$
\operatorname{sym} _ {N} (w, u) = \sum_ {0 \leqslant \alpha \leqslant \kappa} \binom {\kappa} {\alpha} \frac {w ^ {\alpha}}{\alpha !} u ^ {\kappa - \alpha} = \prod_ {j = 1} ^ {n} \left(\sum_ {0 \leqslant \alpha_ {j} \leqslant \kappa_ {j}} \binom {\kappa_ {j}} {\alpha_ {j}} \frac {w _ {j} ^ {\alpha_ {j}}}{\alpha_ {j} !} u _ {j} ^ {\kappa_ {j} - \alpha_ {j}}\right)
$$

is a Lorentzian polynomial. Since the product of Lorentzian polynomials is Lorentzian by Corollary 2.32, the proof is reduced to the case when the symbol is bivariate. In this case, using the characterization of bivariate Lorentzian polynomials in Example 2.26, we get the Lorentzian property from the log-concavity of the sequence$1 / k !$□

Corollary 3.8 below extends the classical fact that the convolution product of two log-concave sequences with no internal zeros is a log-concave sequence with no internal zeros. For early proofs of the classical fact, see [Kar68, Chapter 8] and [Men69].

Corollary 3.8. If$N ( f )$and$N ( g )$are Lorentzian polynomials, then$N ( f g )$is a Lorentzian polynomial.

Note that the analogous statement for stable polynomials fails to hold in general. For example, when$f = x ^ { 3 } + x ^ { 2 } y + x y ^ { 2 } + y ^ { 3 }$, the polynomial$N ( f )$is stable but$N ( f ^ { 2 } )$is not.

Proof. Suppose that$f$and g belong to$\mathbb { R } _ { \kappa } [ \boldsymbol { w } _ { i } ]$. We consider the linear operator

$$
T: \mathbb {R} _ {\kappa} [ w _ {i} ] \longrightarrow \mathbb {R} [ w _ {i} ], \quad N (h) \longmapsto N (h g).
$$

By Theorem 3.2, it is enough to show that its symbol

$$
\operatorname{sym} _ {T} (w, u) = \kappa ! \sum_ {0 \leqslant \alpha \leqslant \kappa} N \left(w ^ {\alpha} g\right) \frac {u ^ {\kappa - \alpha}}{(\kappa - \alpha) !}
$$

is a Lorentzian polynomial in$2 n$variables. For this, we consider the linear operator

$$
S: \mathbb {R} _ {\kappa} [ w _ {i} ] \longrightarrow \mathbb {R} [ w _ {i}, u _ {i} ], \qquad N (h) \longmapsto \sum_ {0 \leqslant \alpha \leqslant \kappa} N (w ^ {\alpha} h) \frac {u ^ {\kappa - \alpha}}{(\kappa - \alpha) !}.
$$

By Theorem 3.2, it is enough to show that its symbol

$$
\operatorname{sym} _ {S} (w, u, v) = \kappa ! \sum_ {0 \leqslant \beta \leqslant \kappa} \sum_ {0 \leqslant \alpha \leqslant \kappa} \frac {w ^ {\alpha + \beta}}{(\alpha + \beta) !} \frac {u ^ {\kappa - \alpha}}{(\kappa - \alpha) !} \frac {v ^ {\kappa - \beta}}{(\kappa - \beta) !}
$$

is a Lorentzian polynomial in 3n variables. The statement is straightforward to check using Theorem 2.25. See Theorem 3.10 below for a more general statement.□

The symmetric exclusion process is one of the main models considered in interacting particle systems. It is a continuous time Markov chain which models particles that jump symmetrically between sites, where each site may be occupied by at most one particle [Lig10]. A problem that has attracted much attention is to find negative dependence properties that are preserved under the symmetric exclusion process. In [BBL09, Theorem 4.20], it was proved that strongly Rayleigh measures are preserved under the symmetric exclusion process. In other words, if $f = f ( w _ { 1 } , w _ { 2 } , \dots , w _ { n } )$is a stable multi-affine polynomial with nonnegative coefficients, then the multi-affine polynomial$\Phi _ { \theta } ^ { 1 , 2 } ( f )$defined by

$$
\Phi_ {\theta} ^ {1, 2} (f) = (1 - \theta) f (w _ {1}, w _ {2}, w _ {3}, \ldots , w _ {n}) + \theta f (w _ {2}, w _ {1}, w _ {3}, \ldots , w _ {n})
$$

is stable for all$0 \leqslant \theta \leqslant 1$. We prove an analog for Lorentzian polynomials.

Corollary 3.9. Let$f = f ( w _ { 1 } , w _ { 2 } , \dots , w _ { n } )$be a multi-affine polynomial with nonnegative coefficients. If the homogenization of$f$is a Lorentzian polynomial, then the homogenization of $\Phi _ { \theta } ^ { 1 , 2 } ( f )$is a Lorentzian polynomial for all$0 \leqslant \theta \leqslant 1$

Proof. Recall that a polynomial with nonnegative coefficients is stable if and only if its homogenization is stable [BBL09, Theorem 4.5]. Clearly,$\Phi _ { \theta } ^ { 1 , 2 }$is homogeneous and preserves polynomials with nonnegative coefficients. Since$\Phi _ { \theta } ^ { 1 , 2 }$preserves stability of multi-affine polynomials by [BBL09, Theorem 4.20], the statement follows from Theorem 3.4.□

3.2. Matroids, M-convex sets, and Lorentzian polynomials. The generating function of a subset $\mathbf { J } \subseteq \mathbb { N } ^ { n }$is, by definition,

$$
f _ {\mathrm{J}} = \sum_ {\alpha \in \mathrm{J}} \frac {w ^ {\alpha}}{\alpha !}, \text { where } \alpha ! = \prod_ {i = 1} ^ {n} \alpha_ {i}!.
$$

We characterize matroids and M-convex sets in terms of their generating functions.

Theorem 3.10. The following are equivalent for any nonempty$\mathbf { J } \subseteq \mathbb { N } ^ { n }$

(1) There is a Lorentzian polynomial whose support is J.

(2) There is a homogeneous 2-Rayleigh polynomial whose support is J.

(3) There is a homogeneous c-Rayleigh polynomial whose support is J for some$c > 0$

(4) The generating function$f _ { \mathrm { { J } } }$is a Lorentzian polynomial.

(5) The generating function$f _ { \mathrm { J } }$is a homogeneous 2-Rayleigh polynomial.

(6) The generating function$f _ { \mathrm { { J } } }$is a homogeneous c-Rayleigh polynomial for some$c > 0$

(7) J is M-convex.

When$\operatorname { J } \subseteq \{ 0 , 1 \} ^ { n }$, any one of the above conditions is equivalent to

(8) J is the set of bases of a matroid on$[ n ]$

The statement that the basis generating polynomial$f _ { \mathrm { { J } } }$is log-concave on the positive orthant can be found in [AOVI, Theorem 4.2]. An equivalent statement that the Hessian$f _ { \mathrm { { J } } }$has exactly one positive eigenvalue on the positive orthant has been noted earlier in [HW17, Remark 15]. The equivalence of the conditions (4) and (7) will be generalized to M-convex functions in Theorem 3.14.

We prepare the proof of Theorem 3.10 with an analysis of the quadratic case.

Lemma 3.11. The following conditions are equivalent for any$n \times n$symmetric matrix A with entries in t0, 1u.

(1) The quadratic polynomial$w ^ { T }$Aw is Lorentzian.

(2) The support of the quadratic polynomial$w ^ { T }$Aw is M-convex.

Proof. Theorem 2.25 implies$( 1 ) \Rightarrow ( 2 )$. We prove$( 2 ) \Rightarrow ( 1 )$. We may and will suppose that no column of A is zero. Let J be the M-convex support of$w ^ { T } A w ,$, and set

$$
S = \left\{i \in [ n ] \mid 2 e _ {i} \in J \right\}.
$$

The exchange property for J shows that$e _ { i } + e _ { j } \in \mathrm { J }$for every$i \in S$and$j \in [ n ]$. In addition, again by the exchange property for J,

$$
\mathrm{B} := \left\{e _ {i} + e _ {j} \in \mathrm{J} \mid i \notin S \text {   and   } j \notin S \right\}
$$

is the set of bases of a rank 2 matroid on$[ n ] \backslash S$without loops. Writing$S _ { 1 } \cup \cdots \cup S _ { k }$for the decomposition of$[ n ] \backslash S$into parallel classes in the matroid, we have

$$
w ^ {T} A w = \Big (\sum_ {j \in [ n ]} w _ {j} \Big) ^ {2} - \Big (\sum_ {j \in S _ {1}} w _ {j} \Big) ^ {2} - \dots - \Big (\sum_ {j \in S _ {k}} w _ {j} \Big) ^ {2},
$$

and hence$w ^ { T }$Aw is a Lorentzian polynomial.

Proof of Theorem 3.10. Theorem 2.23, Theorem 2.25, and Proposition 2.19 show that

$$
(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (7) \text { and } (4) \Rightarrow (5) \Rightarrow (6) \Rightarrow (7).
$$

Since$( 4 ) \Rightarrow ( 1 )$, we only need to prove$( 7 ) \Rightarrow ( 4 )$

If J is an M-convex subset of$\mathbb { N } ^ { n }$, then$f _ { \mathrm { { J } } }$is a homogeneous polynomial of some degree d. Suppose$d \geqslant 2 ,$and let α be an element of$\Delta _ { n } ^ { d - 2 }$. Note that, in general, the support of$\partial ^ { \alpha } f _ { \mathrm { J } }$is M-convex whenever the support of$f _ { \mathrm { { J } } }$is M-convex. Therefore,$\partial ^ { \alpha } f _ { \mathrm { J } }$is Lorentzian by Lemma 3.11, and hence$f _ { \mathrm { J } }$is Lorentzian by Theorem 2.25.□

Let J be the set of bases of a matroid M on rns. If M is regular [FM92], if M is representable over the finite fields$\mathbb { F } _ { 3 }$and$\mathbb { F } _ { 4 }$[COSW04], if the rank of M is at most 3 [Wag05], or if the number of elements n is at most 7 [Wag05], then$f _ { \mathrm { { J } } }$is 1-Rayleigh. Seymour and Welsh found the first example of a matroid whose basis generating function is not 1-Rayleigh [SW75]. We propose the following improvement of Theorem 3.10.

Conjecture 3.12. The following conditions are equivalent for any nonempty$\boldsymbol { \mathrm { J } } \subseteq \{ 0 , 1 \} ^ { n }$

(1) J is the set of bases of a matroid on rns.

(2) The generating function$f _ { \mathrm { { J } } }$is a homogeneous$\scriptstyle { \frac { 8 } { 7 } } - \mathrm { R a y l e i g h }$polynomial.

The constant$\frac { 8 } { 7 }$is best possible: For any positive real number$c < \frac { 8 } { 7 }$, there is a matroid whose basis generating function is not c-Rayleigh [HSW, Theorem 7].

3.3. Valuated matroids, M-convex functions, and Lorentzian polynomials. Let ν be a function from$\mathbb { N } ^ { n }$to$\mathbb { R } \cup \lbrace \infty \rbrace$. The effective domain of ν is, by definition,

$$
\operatorname{dom} (\nu) = \left\{\alpha \in \mathbb {N} ^ {n} \mid \nu (\alpha) <   \infty \right\}.
$$

The function ν is said to be M-convex if satisfies the symmetric exchange property:

(1) For any$\alpha , \beta \in \mathsf { d o m } ( \nu )$and any i satisfying$\alpha _ { i } > \beta _ { i } ,$there is j satisfying

$$
\alpha_ {j} <   \beta_ {j} \text { and } \nu (\alpha) + \nu (\beta) \geqslant \nu (\alpha - e _ {i} + e _ {j}) + \nu (\beta - e _ {j} + e _ {i}).
$$

Note that the effective domain of an M-convex function on$\mathbb { N } ^ { n }$is an M-convex subset of$\mathbb { N } ^ { n }$. In particular, the effective domain of an M-convex function on$\mathbb { N } ^ { n }$is contained in$\Delta _ { n } ^ { d }$for some d. In this case, we identify ν with its restriction to$\Delta _ { n } ^ { d }$. When the effective domain of ν is is M-convex, the symmetric exchange property for ν is equivalent to the following local exchange property:

(2) For any$\alpha , \beta \in \mathsf { d o m } ( \nu )$with$| \alpha - \beta | _ { 1 } = 4 _ { \ L }$, there are i and j satisfying

$$
\alpha_ {i} > \beta_ {i}, \alpha_ {j} <   \beta_ {j} \text { and } \nu (\alpha) + \nu (\beta) \geqslant \nu (\alpha - e _ {i} + e _ {j}) + \nu (\beta - e _ {j} + e _ {i}).
$$

A proof of the equivalence of the two exchange properties can be found in [Mur03, Section 6.2].

Example 3.13. The indicator function of$\mathbf { J } \subseteq \mathbb { N } ^ { n }$is the function$\nu _ { \mathrm { J } } : \mathbb { N } ^ { n }  \mathbb { R } \cup \{ \infty \}$defined by

$$
\nu_ {\mathrm{J}} (\alpha) = \left\{ \begin{array}{l l} 0 & \text { if } \alpha \in \mathrm{J}, \\ \infty & \text { if } \alpha \notin \mathrm{J}. \end{array} \right.
$$

Clearly,$\mathbf { J } \subseteq \mathbb { N } ^ { n }$is M-convex if and only if the indicator function$\nu _ { \mathrm { J } }$is M-convex.

A function$\nu : \mathbb { N } ^ { n } \to \mathbb { R } \cup \{ - \infty \}$is said to be M-concave$\mathrm { i f } - \nu$is M-convex. The effective domain of an M-concave function is

$$
\operatorname{dom} (\nu) = \left\{\alpha \in \mathbb {N} ^ {n} \mid \nu (\alpha) > - \infty \right\}.
$$

A valuated matroid on rns is an M-concave function on$\mathbb { N } ^ { n }$whose effective domain is a nonempty subset of$\{ 0 , 1 \} ^ { n }$. The effective domain of a valuated matroid ν on rns is the set of bases of a matroid on rns, the underlying matroid of$\nu .$

In this section, we prove that the class of tropicalized Lorentzian polynomials coincides with the class of M-convex functions. The tropical connection is used to produce Lorentzian polynomials from M-convex functions. First, we state a classical version of the result. For any function $\nu : \Delta _ { n } ^ { d }  \mathbb { R } \cup \{ \infty \}$and a positive real number$q ,$we define

$$
f _ {q} ^ {\nu} (w) = \sum_ {\alpha \in \operatorname{dom} (\nu)} \frac {q ^ {\nu (\alpha)}}{\alpha !} w ^ {\alpha} \text { and } g _ {q} ^ {\nu} (w) = \sum_ {\alpha \in \operatorname{dom} (\nu)} \binom {\delta} {\alpha} q ^ {\nu (\alpha)} w ^ {\alpha},
$$

where$\delta = ( d , \ldots , d )$and$\binom { \delta } { \alpha }$is the product of binomial coefficients$\textstyle \prod _ { i = 1 } ^ { n } { \binom { d } { \alpha _ { i } } }$. When$\nu$is the indicator function of$\mathbf { J } \subseteq \mathbb { N } ^ { n }$, the polynomial$f _ { q } ^ { \nu }$is independent of$q$and equal to the generating function$f _ { \mathrm { { J } } }$considered in Section 3.2.

Theorem 3.14. The following conditions are equivalent for$\nu : \Delta _ { n } ^ { d }  \mathbb { R } \cup \{ \infty \}$

(1) The function ν is M-convex.

(2) The polynomial$f _ { q } ^ { \nu } ( w )$is Lorentzian for all$0 < q \leqslant 1$

(3) The polynomial$g _ { q } ^ { \nu } ( w )$is Lorentzian for all$0 < q \leqslant 1$

The proof of Theorem 3.14, which relies on the theory of phylogenetic trees and the problem of isometric embeddings of finite metric spaces in Euclidean spaces, will be given at the end of this subsection.

Example 3.15. A function$\mu$from$\mathbb { N } ^ { n }$to$\mathbb { R } \cup \lbrace \infty \rbrace$is said to be$\mathrm { M } ^ { \natural . }$-convex${ \mathrm { i f } } ,$for some positive integer$d ,$the function$\nu$from$\mathbb { N } ^ { n + 1 }$to R$\cup \\\left\{ \infty \right\}$defined by

$$
\nu (\alpha_ {0}, \alpha_ {1}, \ldots , \alpha_ {n}) = \left\{ \begin{array}{c l} \mu (\alpha_ {1}, \ldots , \alpha_ {n}) & \text {if} \alpha \in \Delta_ {n + 1} ^ {d}, \\ \infty & \text {if} \alpha \notin \Delta_ {n + 1} ^ {d}, \end{array} \right.
$$

is M-convex. The condition does not depend on$d ,$and M<sup>6</sup>-concave functions are defined similarly. We refer to [Mur03, Chapter 6] for more on$\mathrm { M } ^ { \natural } .$-convex and$\mathrm { M } ^ { \sharp }$-concave functions.

It can be shown that every matroid rank function${ \mathrm { \mathbf { r k } } _ { \mathrm { M } } } .$, viewed as a function on$\mathbb { N } ^ { n }$with the effective domain$\{ 0 , 1 \} ^ { n }$, is$\mathrm { M } ^ { \natural } .$-concave. See [Shi12, Section 3] for an elementary proof and other related results. Thus, by Theorem$3 . 1 4 ,$the normalized rank generating function

$$
\sum_ {A \subseteq [ n ]} \frac {1}{c (A) !} q ^ {- \mathrm{rk} _ {\mathrm{M}} (A)} w ^ {A} w _ {0} ^ {c (A)}, \text {where} w = (w _ {1}, \dots , w _ {n}) \text {and} c (A) = n - | A |,
$$

is Lorentzian for all$0 < q \leqslant 1$. We will obtain a sharper result on$\mathbf { r k } _ { \mathrm { { M } } }$in Section 4.3.

Theorem 3.14 provides a useful sufficient condition for a homogeneous polynomial to be Lorentzian. Let$f$be an arbitrary homogeneous polynomial with nonnegative real coefficients written in the normalized form

$$
f = \sum_ {\alpha \in \Delta_ {n} ^ {d}} \frac {c _ {\alpha}}{\alpha !} w ^ {\alpha}.
$$

We define a discrete function$\nu _ { f }$using natural logarithms of the normalized coefficients:

$$
\nu_ {f}: \Delta_ {n} ^ {d} \longrightarrow \mathbb {R} \cup \{- \infty \}, \quad \alpha \longmapsto \log (c _ {\alpha}).
$$

Corollary 3.16. If$\nu _ { f }$is an M-concave function, then$f$is a Lorentzian polynomial.

Proof. By Theorem 3.14, the polynomial$\begin{array} { r } { \sum _ { \alpha \in \mathrm { d o m } ( \nu _ { f } ) } \frac { q ^ { - \nu _ { f } ( \alpha ) } } { \alpha ! } w ^ { \alpha } } \end{array}$is Lorentzian when$q = e ^ { - 1 }$□

We note that the converse of Corollary 3.16 does not hold. For example, the polynomial

$$
f = \prod_ {i = 1} ^ {n - 1} (w _ {i} + w _ {n})
$$

is Lorentzian, being a product of Lorentzian polynomials. However,$\nu _ { f }$fails to be M-concave when$n > 2 .$

We formulate a tropical counterpart of Theorem 3.14. Let$\mathbb { C } ( ( t ) ) _ { \mathrm { c o n v } }$be the field of Laurent series with complex coefficients that have a positive radius of convergence around 0. By definition, any nonzero element of$\mathbb { C } ( ( t ) ) _ { \mathrm { c o n v } }$is a series of the form

$$
s (t) = c _ {1} t ^ {a _ {1}} + c _ {2} t ^ {a _ {2}} + c _ {3} t ^ {a _ {3}} + \dots ,
$$

where$c _ { 1 } , c _ { 2 } , \ldots$. are nonzero complex numbers and$a _ { 1 } < a _ { 2 } < \cdots$are integers, that converges on a punctured open disk centered at 0. Let R$( ( t ) ) _ { \mathrm { c o n v } }$be the subfield of elements that have real coefficients. We define the fields of real and complex convergent Puiseux series<sup>10</sup> by

$$
\mathbb {K} = \bigcup_ {k \geqslant 1} \mathbb {R} ((t ^ {1 / k})) _ {\text { conv }} \text {   and   } \overline {{\mathbb {K}}} = \bigcup_ {k \geqslant 1} \mathbb {C} ((t ^ {1 / k})) _ {\text { conv }}.
$$

Any nonzero element of K is a series of the form

$$
s (t) = c _ {1} t ^ {a _ {1}} + c _ {2} t ^ {a _ {2}} + c _ {3} t ^ {a _ {3}} + \dots ,
$$

where$c _ { 1 } , c _ { 2 } , \ldots$are nonzero complex numbers and$a _ { 1 } < a _ { 2 } < \cdots$are rational numbers that have a common denominator. The leading coefficient of$s ( t )$is$c _ { 1 } ,$, and the leading exponent of$s ( t )$ is$a _ { 1 }$. A nonzero element of K is positive if its leading coefficient is positive. The valuation map is the function

$$
\operatorname{val}: \overline {{\mathbb {K}}} \longrightarrow \mathbb {R} \cup \{\infty \},
$$

that takes the zero element to 8 and a nonzero element to its leading exponent. For a nonzero element$s ( t ) \in \mathbb { K } .$, we have

$$
\operatorname{val} \bigl (s (t) \bigr) = \lim _ {t \to 0 ^ {+}} \log_ {t} \bigl (s (t) \bigr).
$$

The field K is algebraically closed, and the field K is real closed. See [Spe05, Section 1.5] and references therein. Since the theory of real closed fields has quantifier elimination [Mar02, Section 3.3], for any first-order formula$\varphi ( x _ { 1 } , \ldots , x _ { m } )$in the language of ordered fields and any $s _ { 1 } ( t ) , \ldots , s _ { m } ( t ) \in \mathbb { K } ,$, we have

$$
\begin{array}{l} \Big (\varphi (s _ {1} (t), \ldots , s _ {m} (t)) \text { holds   in } \mathbb {K} \Big) \Longleftrightarrow \\ \qquad \qquad \qquad \Big (\varphi (s _ {1} (q), \ldots , s _ {m} (q)) \text { holds   in } \mathbb {R} \text { for   all   sufficiently   small   positive   real   numbers } q \Big). \end{array}
$$

In particular, Tarski’s principle holds for K: A first-order sentence in the language of ordered fields holds in K if and only if it holds in R.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>10</sup>The main statements in this section are valid over the field of formal Puiseux series as well.</span></small>

Definition 3.17. Let$\begin{array} { r } { f _ { t } = \sum _ { \alpha \in \Delta _ { n } ^ { d } } s _ { \alpha } ( t ) w ^ { \alpha } } \end{array}$be a nonzero homogeneous polynomial with coefficients in$\mathbb { K } _ { \geqslant 0 }$. The tropicalization of$f _ { t }$is the discrete function defined by

$$
\operatorname{trop} \left(f _ {t}\right): \Delta_ {n} ^ {d} \longrightarrow \mathbb {R} \cup \{\infty \}, \quad \alpha \longmapsto \operatorname{val} \left(s _ {\alpha} (t)\right).
$$

We say that$f _ { t }$is log-concave on$\mathbb { K } _ { > 0 } ^ { n }$if the function$\log ( f _ { q } )$is concave on$\mathbb { R } _ { > 0 } ^ { n }$for all sufficiently small positive real numbers$q .$

Note that the support of$f _ { t }$is the effective domain of the tropicalization of$f _ { t } .$. We write $\mathrm { M } _ { n } ^ { d } ( \mathbb { K } )$for the set of all degree d homogeneous polynomials in$\mathbb { K } _ { \geqslant 0 } [ w _ { 1 } , \ldots , w _ { n } ]$whose support is M-convex.

Definition 3.18 (Lorentzian polynomials over K). We set$\operatorname { L } _ { n } ^ { 0 } ( \mathbb { K } ) = \operatorname { M } _ { n } ^ { 0 } ( \mathbb { K } ) , \operatorname { L } _ { n } ^ { 1 } ( \mathbb { K } ) = \operatorname { M } _ { n } ^ { 1 } ( \mathbb { K } )$, and

$\mathrm { L } _ { n } ^ { 2 } ( \mathbb { K } ) = \Big \{ f _ { t } \in \mathrm { M } _ { n } ^ { 2 } ( \mathbb { K } )$| The Hessian of$f _ { t }$has at most one eigenvalue in${ \mathbb K } _ { > 0 } \Bigg \}$

For d$\geqslant 3 .$, we define$\operatorname { L } _ { n } ^ { d } ( \mathbb { K } )$by setting

$$
\mathrm{L} _ {n} ^ {d} (\mathbb {K}) = \left\{f _ {t} \in \mathrm{M} _ {n} ^ {d} (\mathbb {K}) \mid \partial^ {\alpha} f _ {t} \in \mathrm{L} _ {n} ^ {2} (\mathbb {K}) \text {for all} \alpha \in \Delta_ {n} ^ {d - 2} \right\}.
$$

The polynomials in$\operatorname { L } _ { n } ^ { d } ( \mathbb { K } )$will be called Lorentzian.

By Proposition 2.33, the log-concavity of homogeneous polynomials can be expressed in the first-order language of ordered fields. It follows that the analog of Theorem 2.30 holds for any homogeneous polynomial$f _ { t }$with coefficients in$\mathbb { K } _ { \geqslant 0 }$

Theorem 3.19. The following conditions are equivalent for$f _ { t } .$

(1) For any m P N and any$m \times n$matrix$( a _ { i j } )$with entries in$\mathbb { K } _ { \geqslant 0 }$

${ \Big ( } \prod _ { i = 1 } ^ { m } D _ { i } { \Big ) } f _ { t }$is identically zero or${ \Big ( } \prod _ { i = 1 } ^ { m } D _ { i } { \Big ) } f _ { t }$is log-concave on$\mathbb { K } _ { > 0 } ^ { n } ,$

where$D _ { i }$is the differential operator$\textstyle \sum _ { j = 1 } ^ { n } a _ { i j } \partial _ { j }$

(2) For any$\alpha \in \mathbb { N } ^ { n }$, the polynomial$\partial ^ { \alpha } f _ { t }$is identically zero or log-concave on$\mathbb { K } _ { > 0 } ^ { n }$

(3) The polynomial$f _ { t }$is Lorentzian.

The field K is real closed, and the field$\overline { { \mathbb { K } } }$is algebraically closed [Spe05, Section 1.5]. Any element$s ( t )$of K can be written as a sum

$$
s (t) = p (t) + i q (t),
$$

where$p ( t ) \in \mathbb { K }$is the real part of$s ( t )$and$q ( t ) \in \mathbb { K }$is the imaginary part of$s ( t )$. The open upper half plane in$\overline { { \mathbb { K } } }$is the set of elements in$\overline { { \mathbb { K } } }$with positive imaginary parts. A polynomial$f _ { t }$in $\mathbb { K } [ w _ { 1 } , \dots , w _ { n } ]$is stable if$f _ { t }$is non-vanishing on$\mathcal { H } _ { \mathbb { K } } ^ { n }$or identically zero, where$\mathcal { H } _ { \overline { { \mathbb { K } } } }$is the open upper half plane in$\overline { { \mathbb { K } } } .$According to [Bra10 ¨ , Theorem 4], tropicalizations of homogeneous stable polynomials over K are M-convex functions.<sup>11</sup> Here we prove that tropicalizations of Lorentzian polynomials over K are M-convex, and that all M-convex functions are limits of tropicalizations of Lorentzian polynomials over K.<sup>12</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">R{t}</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>11</sup>In [Bra10 ¨ ], the field of formal Puiseux series with real exponents Rttu containing K was used. The tropicalizationK used in [Bra10 ¨ ] differs from ours by a sign</span></small>

Theorem 3.20. The following conditions are equivalent for any function$\nu : \Delta _ { n } ^ { d } \to \mathbb { Q } \cup \{ \infty \}$

(i) The function ν is M-convex.

(ii) There is a Lorentzian polynomial in$\mathbb { K } [ w _ { 1 } , \dots , w _ { n } ]$whose tropicalization is$\nu .$

Let M be a matroid with the set of bases B. The Dressian of$\mathrm { M } ,$denoted$\mathrm { D r } ( \mathrm { M } )$, is the tropical variety in$\mathbb { R } ^ { \mathrm { B } }$obtained by intersecting the tropical hypersurfaces of the Plucker relations in ¨$\mathbb { R } ^ { \mathrm { B } }$ [MS15, Section 4.4]. Since DrpMq is a rational polyhedral fan whose points bijectively correspond to the valuated matroids with underlying matroid$\mathrm { M } ,$Theorem 3.20 shows that

$$
\operatorname{Dr} (M) = \text { closure } \left\{- \operatorname{trop} \left(f _ {t}\right) \mid f _ {t} \text {   is   a   Lorentzian   polynomial   with   } \operatorname{supp} \left(f _ {t}\right) = B \right\}.
$$

We note that the corresponding statement for stable polynomials fails to hold. For example, when M is the Fano plane, there is no stable polynomial whose support is B [Bra07 ¨ , Section 6].

We prove Theorems 3.14 and 3.20 together after reviewing the needed results on the space of phylogenetic trees and the isometric embeddings of finite metric spaces in Euclidean spaces. A phylogenetic tree with n leaves is a tree with n labelled leaves and no vertices of degree 2. A function d$: \left[ { \binom { n } { 2 } } \right] \to \mathbb { R }$is a tree distance if there is a phylogenetic tree$\tau$with n leaves and edge weights$\ell _ { e }$P R such that

$$
\mathrm{d} (i, j) = \left(\text { the   sum   of   all } \ell_ {e} \text { along   the   unique   path   in } \tau \text { joining   the   leaves } i \text { and } j\right).
$$

The space of phylogenetic trees$\mathcal { T } _ { n }$is the set of all tree distances in$\mathbb { R } ^ { \binom { n } { 2 } }$. The Fundamental Theorem of Phylogenetics shows that

$$
\mathfrak {T} _ {n} = \mathrm{Dr} (2, n),
$$

where$\operatorname { D r } ( 2 , n )$is the Dressian of the rank 2 uniform matroid on rns [MS15, Section 4.3].

We give a spectral characterization of tree distances. For any function d$: [ { n } ]$R and any positive real number$q ,$we define an$n \times n$symmetric matrix$\mathrm { H } _ { q } ( \mathrm { d } )$by

$$
\mathrm{H} _ {q} (\mathrm{d}) _ {i j} = \left\{ \begin{array}{c l} 0 & \text {if} i = j, \\ q ^ {\mathrm{d} (i, j)} & \text {if} i \neq j. \end{array} \right.
$$

We say that an$n \times n$symmetric matrix H is conditionally negative definite if

$$
(1, \dots , 1) w = 0 \Longrightarrow w ^ {T} \mathrm{H} w \leqslant 0.
$$

Basic properties of conditionally negative definite matrices are collected in [BR97, Chapter 4].

Lemma 3.21. The following conditions are equivalent for any function d :$[ { \bf \Pi } _ { 2 } ^ { n } ]  \mathbb { R } .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">K,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ν.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">R Y t8u</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f<sub>t</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">supppf<sub>t</sub>q “ B,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^ { 1 2 } \mathrm { { I f } \ \mathbb { R } \{ t \} }$is used instead of  then all M-convex functions are tropicalizations of Lorentzian polynomials. More precisely, a discrete function ν with values in is M-convex if and only if there is a Lorentzian polynomial over Rttu whose tropicalization is  In this setting, the Dressian of a matroid M can be identified with the set of tropicalized Lorentzian polynomials with where B is the set of bases of M.</span></small>

(1) The matrix$\mathrm { H } _ { q } ( \mathrm { d } )$has exactly one positive eigenvalue for all$q \geqslant 1$

(2) The function d is a tree distance.

Lemma 3.21 is closely linked to the problem of isometric embeddings of ultrametric spaces in Hilbert spaces. Let d be a metric on rns. Since$\mathrm { d } ( i , i ) = 0$and$\mathrm { d } ( i , j ) = \mathrm { d } ( j , i )$for all$i ,$we may identify d with a function$[ { \bf \Pi } _ { 2 } ^ { n } ]  \mathbb { R }$. We define an$n \times n$symmetric matrix$\mathrm { E ( d ) }$by

$$
\mathrm{E} (\mathrm{d}) _ {i j} = \mathrm{d} (i, j) ^ {2}.
$$

We say that d admits an isometric embedding into$\mathbb { R } ^ { m }$if there is$\phi : [ n ]  \mathbb { R } ^ { m }$such that

$$
\mathrm{d} (i, j) = | \phi (i) - \phi (j) | _ {2} \text {   for   all   } i, j \in [ n ],
$$

where$| \cdot | _ { 2 }$is the standard Euclidean norm on$\mathbb { R } ^ { m }$. The following theorem of Schoenberg [Sch38] characterizes metrics on rns that admit an isometric embedding into some$\mathbb { R } ^ { m }$

Theorem 3.22. A metric d on rns admits an isometric embedding into some$\mathbb { R } ^ { m }$if and only if the matrix Epdq is conditionally negative semidefinite.

Recall that an ultrametric on rns is a metric d on$[ n ]$such that

$$
\mathrm{d} (i, j) \leqslant \max \left\{\mathrm{d} (i, k), \mathrm{d} (j, k) \right\} \text {   for   any   } i, j, k \in [ n ].
$$

Equivalently, d is an ultrametric if the maximum of$\mathrm { d } ( i , j ) , \mathrm { d } ( i , k ) , \mathrm { d } ( j , k )$is attained at least twice for any$i , j , k \in [ n ]$. Any ultrametric is a tree distance given by a phylogenetic tree [MS15, Section 4.3]. In [TV83], Timan and Vestfrid proved that any separable ultrametric space is isometric to a subspace of$\ell _ { 2 }$. We use the following special case.

Theorem 3.23. Any ultrametric on rns admits an isometric embedding into$\mathbb { R } ^ { n - 1 }$

Proof of Lemma 3.21. We prove$( 1 ) \Rightarrow ( 2 )$. We may suppose that d takes rational values. If (1) holds, then the quadratic polynomial$w ^ { T } \mathrm { H } _ { q } ( \mathrm { d } ) w$is stable for all$q \geqslant 1$. Therefore, by the quantifier elimination for the theory of real closed fields, the quadratic form

$$
\sum_ {i <   j} t ^ {- \mathrm{d} (i, j)} w _ {i} w _ {j} \in \mathbb {K} [ w _ {1}, \ldots , w _ {n} ]
$$

is stable. By [Bra10 ¨ , Theorem$^ { 4 ] , }$tropicalizations of stable polynomials are$\mathrm { M - c o n v e x } ^ { 1 3 } ,$, and hence the function ´d is M-convex. In other words, we have

$$
\mathrm{d} \in \operatorname{Dr} (2, n) = \mathfrak {T} _ {n}.
$$

For$( 2 ) \Rightarrow ( 1 )$, we first consider the special case when d is an ultrametric on rns. In this case, $q ^ { \mathrm { d } }$is also an ultrametric on$[ n ]$for all$q \geqslant 1$. It follows from Theorems 3.22 and 3.23 that$\mathrm { H } _ { q } ( \mathrm { d } )$ is conditionally negative definite for all$q \geqslant 1$, and Cauchy’s interlacing theorem shows that conditionally negative definite matrices have at most one positive eigenvalue. In the general case, we use that$\mathcal { T } _ { n }$is the sum of its linearity space with the space of ultrametrics on rns [MS15,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>13</sup>The tropicalization used in [Bra10 ¨ ] differs from ours by a sign.</span></small>

Lemma 4.3.9]. Thus, for any tree distance d on rns, there is an ultrametric d on rns and real numbers$c _ { 1 } , \ldots , c _ { n }$such that

$$
\mathrm{d} = \underline {{\mathrm{d}}} + \sum_ {i = 1} ^ {n} c _ {i} \left(\sum_ {i \neq j} e _ {i j}\right) \in \mathbb {R} ^ {\binom {n} {2}}.
$$

Therefore, the symmetric matrix$\mathrm { H } _ { q } ( \mathrm { d } )$is congruent to$\mathrm { H } _ { q } ( \underline { { \mathrm { d } } } )$, and the conclusion follows from the case of ultrametrics.□

We start the proof of Theorems 3.14 and 3.20 with a linear algebraic lemma. Let$( a _ { i j } )$be an $n \times n$symmetric matrix with entries in$\mathbb { R } _ { > 0 }$

Lemma 3.24. If$( a _ { i j } )$has exactly one positive eigenvalue, then$( a _ { i j } ^ { p } )$has exactly one positive eigenvalue for$0 \leqslant p \leqslant 1$

Proof. If$( v _ { i } )$is the Perron eigenvector of$( a _ { i j } )$, then$\Big ( \frac { a _ { i j } } { v _ { i } v _ { j } } \Big )$is conditionally negative definite [BR97, Lemma 4.4.1]. Therefore,$\Big ( \frac { a _ { i j } ^ { p } } { v _ { i } ^ { p } v _ { j } ^ { p } } \Big )$is conditionally negative definite [BCR84, Corollary 2.10], and the conclusion follows.□

Let$f$be a degree d homogeneous polynomial written in the normalized form

$$
f = \sum_ {\alpha \in \operatorname{supp} (f)} \frac {c _ {\alpha}}{\alpha !} w ^ {\alpha}.
$$

For any nonnegative real number$p ,$we define

$$
R _ {p} (f) = \sum_ {\alpha \in \operatorname{supp} (f)} \frac {c _ {\alpha} ^ {p}}{\alpha !} w ^ {\alpha}.
$$

We use Lemma 3.24 to construct a homotopy from any Lorentzian polynomial to the generating function of its support. The following proposition was proved in [ALOVII] for strongly logconcave multi-affine polynomials.

Proposition 3.25. If f is Lorentzian, then$R _ { p } ( f )$is Lorentzian for all$0 \leqslant p \leqslant 1$

Proof. Using the characterization of Lorentzian polynomials in Theorem 2.25, the proof reduces to the case of quadratic polynomials. Using Theorem 2.10, the proof further reduces to the case $f \in  { \mathrm { P } } _ { n } ^ { 2 }$. In this case, the assertion is Lemma 3.24.□

Set$m = n d ,$and let$\nu : \Delta _ { n } ^ { d }  \mathbb { R } \cup \{ \infty \}$and$\mu : \Delta _ { m } ^ { d } \to \mathbb { R } \cup \{ \infty \}$be arbitrary functions. Write $e _ { i j }$for the standard unit vectors in$\mathbb { R } ^ { m }$with$1 \leqslant i \leqslant$n and$1 \leqslant j \leqslant d ,$and let$\phi$be the linear map

$$
\phi : \mathbb {R} ^ {m} \longrightarrow \mathbb {R} ^ {n}, \quad e _ {i j} \longmapsto e _ {i}.
$$

We define the polarization of$\nu$to be the function Π<sup>Ò</sup>$\nu : \Delta _ { m } ^ { d } \to \mathbb { R } \cup \{ \infty \}$satisfying

$$
\operatorname{dom} \bigl (\Pi^ {\uparrow} \nu \bigr) \subseteq \left[ \begin{array}{c} m \\ d \end{array} \right] \text {   and   } \Pi^ {\uparrow} \nu = \nu \circ \phi \text {   on   } \left[ \begin{array}{c} m \\ d \end{array} \right].
$$

We define the projection of$\mu$to be the function$\Pi ^ { \downarrow } \mu : \Delta _ { n } ^ { d }  \mathbb { R } \cup \{ \infty \}$satisfying

$$
\Pi^ {\downarrow} \mu (\alpha) = \min \Big \{\mu (\beta) \mid \phi (\beta) = \alpha \Big \}.
$$

It is straightforward to check the symmetric exchange properties of$\Pi ^ { \uparrow }$ν and$\Pi ^ { \downarrow } \mu$from the symmetric exchange properties of ν and$\mu . ^ { 1 4 }$

Lemma 3.26. Let$\nu : \Delta _ { n } ^ { d }  \mathbb { R } \cup \{ \infty \}$and$\mu : \Delta _ { m } ^ { d } \to \mathbb { R } \cup \{ \infty \}$be arbitrary functions.

(1) If ν is an M-convex function, then Π<sup>Ò</sup>ν is an M-convex function.

(2) If$\mu$is an M-convex function, then$\Pi ^ { \downarrow } \mu$is an M-convex function.

As a final preparation for the proof of Theorems 3.14 and 3.20, we show that any M-convex function on$\Delta _ { n } ^ { d }$can be approximated by M-convex functions whose effective domain is$\Delta _ { n } ^ { d }$

Lemma 3.27. For any M-convex function$\nu : \Delta _ { n } ^ { d } \to \mathbb { R } \cup \{ \infty \}$, there is a sequence of M-convex functions$\nu _ { k } : \Delta _ { n } ^ { d } \to$R such that

$$
\lim _ {k \to \infty} \nu_ {k} (\alpha) = \nu (\alpha) \mathrm{forall} \alpha \in \Delta_ {n} ^ {d}.
$$

The sequence$\nu _ { k }$can be chosen so that$\nu _ { k } = \nu$in dompνq and$\nu _ { k } < \nu _ { k + 1 }$outside dompνq.

Proof. It is enough to prove the case when ν is not the constant function$\infty .$. Write$e _ { i j }$for the standard unit vectors in$\mathbb { R } ^ { n ^ { 2 } }$. Let$\varphi : \Delta _ { n ^ { 2 } } ^ { d } \to \Delta _ { n } ^ { d }$and$\psi : \Delta _ { n ^ { 2 } } ^ { d } \to \Delta _ { n } ^ { d }$be the restrictions of the linear maps from$\mathbb { R } ^ { n ^ { 2 } }$to$\mathbb { R } ^ { n }$given by

$$
\varphi (e _ {i j}) = e _ {i} \text { and } \psi (e _ {i j}) = e _ {j}.
$$

For any function$\mu : \Delta _ { n } ^ { d } \to \mathbb { R } \cup \{ \infty \}$, we define the function$\varphi ^ { * } \mu : \Delta _ { n ^ { 2 } } ^ { d } \to \mathbb { R } \cup \{ \infty \}$by

$$
\varphi^ {*} \mu (\beta) = \mu (\varphi (\beta)).
$$

For any function$\mu : \Delta _ { n ^ { 2 } } ^ { d } \to \mathbb { R } \cup \{ \infty \}$, we define the function$\psi _ { * } \mu : \Delta _ { n } ^ { d }  \mathbb { R } \cup \{ \infty \}$by

$$
\psi_ {*} \mu (\alpha) = \min \Bigl \{\mu (\beta) \mid \psi (\beta) = \alpha \Bigr \}.
$$

Recall that the operations of splitting [KMT07, Section 4] and aggregation [KMT07, Section 5] preserve M-convexity of discrete functions. Therefore,$\varphi ^ { * }$and$\psi _ { * }$preserve M-convexity. Now, given$\nu ,$set

$$
\nu_ {k} = \psi_ {*} (\ell_ {k} + \varphi^ {*} \nu),
$$

where$\ell _ { k }$is the restriction of the linear function on$\mathbb { R } ^ { n ^ { 2 } }$defined by

$$
\ell_ {k} (e _ {i j}) = \left\{ \begin{array}{l l} 0 & \text { if } i = j, \\ k & \text { if } i \neq j. \end{array} \right.
$$

The existence theorem for nonnegative matrices with given row and column sums shows that the restriction of$\psi$to any fiber of$\varphi$is surjective [Bru06, Corollary 1.4.2]. Thus, the assumption that ν is not identically 8 implies that$\nu _ { k } < \infty$for every k. It is straightforward to check that the sequence$\nu _ { k }$has the other required properties for large enough k.□

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">µ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>14</sup>In the language of [KMT07], the polarization of ν is obtained from ν by splitting of variables and restricting to “<sup>m</sup><sub>d</sub> ‰, and the projection of is obtained from µ by aggregation of variables.</span></small>

Proof of Theorem$3 . 2 0 , ( i i ) \Rightarrow ( i )$. Let$f _ { t }$be a polynomial in$\operatorname { L } _ { n } ^ { d } ( \mathbb { K } )$whose tropicalization is ν. We show the M-convexity of ν by checking the local exchange property: For any$\alpha , \beta \in \mathsf { d o m } ( \nu )$with $| \alpha - \beta | _ { 1 } = 4 ,$, there are i and j satisfying

$$
\alpha_ {i} > \beta_ {i}, \alpha_ {j} <   \beta_ {j} \text { and } \nu (\alpha) + \nu (\beta) \geqslant \nu (\alpha - e _ {i} + e _ {j}) + \nu (\beta - e _ {j} + e _ {i}).
$$

Since$| \alpha - \beta | _ { 1 } = 4 ,$we can find$\gamma$in$\Delta _ { n } ^ { d - 2 }$and indices$p , q , r ,$s in rns such that such that

$$
\alpha = \gamma + e _ {p} + e _ {q} \text { and } \beta = \gamma + e _ {r} + e _ {s} \text { and } \{p, q \} \cap \{r, s \} = \varnothing .
$$

Since$\partial ^ { \gamma } f _ { t }$is stable, the tropicalization of$\partial ^ { \gamma } f _ { t }$is M-convex by [Bra10 ¨ , Theorem 4]. The conclusion follows from the local exchange property for the tropicalization of$\partial ^ { \gamma } f _ { t }$□

Proof of Theorem 3.14. We prove$( 1 ) \Rightarrow ( 3 )$. We first show the implication in the special case

$$
\operatorname{dom} (\nu) = \left[ \begin{array}{c} n \\ d \end{array} \right].
$$

Since dompνq is M-convex, it is enough to prove that$\partial ^ { \alpha } g _ { q } ^ { \nu }$is has exactly one positive eigenvalue for all$\alpha \in \left[ \begin{array} { c } { { n } } \\ { { d - 2 } } \end{array} \right]$and all$0 < q \leqslant 1$. Since$\mathcal { T } _ { n } = \mathrm { D r } ( 2 , n )$by [MS15, Theorem 4.3.5] and [MS15, Definition 4.4.1], the desired statement follows from Lemma 3.21. This proves the first special case. Now consider the second special case

$$
\operatorname{dom} (\nu) = \Delta_ {n} ^ {d}.
$$

By Lemma 3.26, the polarization$\Pi ^ { \uparrow } \nu$is an M-convex function with effective domain$\textstyle { \left[ { \begin{array} { l } { n d } \\ { d } \end{array} } \right] }$, and hence we may apply the known implication$( 1 ) \Rightarrow ( 3 )$for$\Pi ^ { \uparrow } \nu .$. Therefore,

$$
\Pi_ {\delta} ^ {\uparrow} (g _ {q} ^ {\nu}) = \frac {1}{d ^ {d}} g _ {q} ^ {\Pi^ {\uparrow \nu}} \text {   is   a   Lorentzian   polynomial   for   } 0 <   q \leqslant 1,
$$

where$\delta = ( d , \ldots , d )$. Thus, by Proposition 3.1, the polynomial$g _ { q } ^ { \nu }$is Lorentzian for all$0 < q \leqslant 1$ and the second special case is proved. Next consider the third special case

$$
\operatorname{dom} (\nu) \text {   is   an   arbitrary   M - convex   set   and   } q = 1.
$$

By Lemma 3.26, the effective domain of$\Pi ^ { \uparrow } \nu$is an M-convex set. Therefore, by Theorem 3.10,

$$
\Pi_ {\delta} ^ {\uparrow} (g _ {1} ^ {\nu}) = \frac {1}{d ^ {d}} g _ {1} ^ {\Pi^ {\uparrow} \nu} \text {   is   a   Lorentzian   polynomial. }
$$

Thus, by Proposition 3.1, the polynomial$g _ { 1 } ^ { \nu }$is Lorentzian, and the the third special case is proved. In the remaining case when$q < 1$and the effective domain of ν is arbitrary, we express ν as the limit of M-convex functions$\nu _ { k }$with effective domain$\Delta _ { n } ^ { d }$using Lemma 3.27. Since $q < 1 \AA$, we have

$$
g _ {q} ^ {\nu} = \lim _ {k \to \infty} g _ {q} ^ {\nu_ {k}}.
$$

Thus the conclusion follows from the second special case applied to each$g _ { q } ^ { \nu _ { k } }$.

We prove$( 1 ) \Rightarrow ( 2 )$. Introduce a positive real number$p ,$and consider the M-convex function ${ \frac { \nu } { p } } .$. Applying the known implication$( 1 ) \Rightarrow ( 3 )$, we see that the polynomial$g _ { q } ^ { \nu / p }$is Lorentzian for all$0 < q \leqslant 1$. Therefore, by Proposition 3.25,

$$
R _ {p} (g _ {q} ^ {\nu / p}) = \sum_ {\alpha \in \operatorname{dom} (\nu)} (\alpha !) ^ {p} \binom{\delta}{\alpha} ^ {p} \frac {q ^ {\nu (\alpha)}}{\alpha !} w ^ {\alpha}
$$

is Lorentzian for all$0 < p \leqslant 1$. Taking the limit$p$to zero, we have (2).

We prove$( 2 ) \Rightarrow ( 1 )$and$( 3 ) \Rightarrow ( 1 )$. By the quantifier elimination for the theory of real closed fields, the polynomial$f _ { t } ^ { \nu }$with coefficients in$\mathbb { K }$is Lorentzian if (2) holds. Similarly, the polynomial$g _ { t } ^ { \nu }$is Lorentzian if (3) holds. Since

$$
\nu = \operatorname{trop} (f _ {t} ^ {\nu}) = \operatorname{trop} (g _ {t} ^ {\nu}),
$$

the conclusion follows from$( \mathrm { i i } ) \Rightarrow ( \mathrm { i } )$of Theorem 3.20.

Proof of Theorem$3 . 2 0 , ( i ) \Rightarrow ( i i )$. By Theorem 3.14,$f _ { q } ^ { \nu }$is Lorentzian for all sufficiently small positive real numbers$q .$Therefore, by the quantifier elimination for the theory of real closed fields, the polynomial$f _ { t } ^ { \nu }$is Lorentzian over K. Clearly, the tropicalization of$f _ { t } ^ { \nu }$is$\nu .$□

Corollary 3.28. Tropicalizations of Lorentzian polynomials over$\mathbb { K }$are M-convex, and all Mconvex functions are limits of tropicalizations of Lorentzian polynomials over K.

Proof. By Theorem 3.20, it is enough to show that any M-convex function$\nu : \Delta _ { n } ^ { d }  \mathbb { R } \cup \{ \infty \}$is a limit of M-convex functions$\nu _ { k } : \Delta _ { n } ^ { d } \to \mathbb { Q } \cup \{ \infty \}$. By Lemma 3.27, we may suppose that

$$
\operatorname{dom} (\nu) = \Delta_ {n} ^ {d}.
$$

In this case, by Lemma 3.26, the polarization$\Pi ^ { \uparrow } \nu$is M-convex function satisfying

$$
\operatorname{dom} \bigl (\Pi^ {\uparrow} \nu \bigr) = \left[ \begin{array}{c} n d \\ d \end{array} \right].
$$

In other words,$- \Pi ^ { \uparrow } \nu$is a valuated matroid whose underlying matroid is uniform of rank d on nd elements. Since the Dressian of the matroid is a rational polyhedral fan [MS15, Section$4 . 4 ] ,$ there are M-convex functions$\mu _ { k } : \Delta _ { n d } ^ { d } \to \mathbb { Q } \cup \{ \infty \}$satisfying

$$
\Pi^ {\uparrow} \nu = \lim _ {k \to \infty} \mu_ {k}.
$$

By Lemma 3.26,$\nu = \Pi ^ { \downarrow } \Pi ^ { \uparrow } \nu$is the limit of M-convex functions$\Pi ^ { \downarrow } \mu _ { k } : \Delta _ { n } ^ { d } \to \mathbb { Q } \cup \{ \infty \}$

## 4. EXAMPLES AND APPLICATIONS

4.1. Convex bodies and Lorentzian polynomials. For any collection of convex bodies$\textrm { K } =$ $( \mathrm { K } _ { 1 } , \ldots , \mathrm { K } _ { n } )$in$\mathbb { R } ^ { d }$, consider the function

$$
\operatorname{vol} _ {\mathrm{K}}: \mathbb {R} _ {\geqslant 0} ^ {n} \longrightarrow \mathbb {R}, \quad w \longmapsto \operatorname{vol} (w _ {1} \mathrm{K} _ {1} + \dots + w _ {n} \mathrm{K} _ {n}),
$$

where$w _ { 1 } \mathrm { K } _ { 1 } + \cdot \cdot \cdot + w _ { n } \mathrm { K } _ { n }$is the Minkowski sum and vol is the Euclidean volume. Minkowski noticed that the function vol<sub>K</sub> is a degree d homogeneous polynomial in$w = ( w _ { 1 } , \ldots , w _ { n } )$with nonnegative coefficients. We may write

$$
\operatorname{vol} _ {\mathrm{K}} (w) = \sum_ {1 \leqslant i _ {1}, \dots , i _ {d} \leqslant n} V (\mathrm{K} _ {i _ {1}}, \dots , \mathrm{K} _ {i _ {d}}) w _ {i _ {1}} \dots w _ {i _ {d}} = \sum_ {\alpha \in \Delta_ {n} ^ {d}} \frac {d !}{\alpha !} V _ {\alpha} (\mathrm{K}) w ^ {\alpha},
$$

where$V _ { \alpha } ( \mathrm { K } )$is, by definition, the mixed volume

$$
V _ {\alpha} (\mathrm{K}) = V (\underbrace {\mathrm{K} _ {1} , \ldots , \mathrm{K} _ {1}} _ {\alpha_ {1}}, \ldots , \underbrace {\mathrm{K} _ {n} , \ldots , \mathrm{K} _ {n}} _ {\alpha_ {n}}) := \frac {1}{d !} \partial^ {\alpha} \mathrm{vol} _ {\mathrm{K}}.
$$

For any convex bodies$\mathrm { C } _ { 0 } , \mathrm { C } _ { 1 } , \ldots , \mathrm { C } _ { d }$in$\mathbb { R } ^ { d } ,$, the mixed volume$V ( \mathrm { C } _ { 1 } , \mathrm { C } _ { 2 } , \ldots , \mathrm { C } _ { d } )$is symmetric in its arguments and satisfies the relation

$$
V \left(\mathrm{C} _ {0} + \mathrm{C} _ {1}, \mathrm{C} _ {2}, \dots , \mathrm{C} _ {d}\right) = V \left(\mathrm{C} _ {0}, \mathrm{C} _ {2}, \dots , \mathrm{C} _ {d}\right) + V \left(\mathrm{C} _ {1}, \mathrm{C} _ {2}, \dots , \mathrm{C} _ {d}\right).
$$

We refer to [Sch14] for background on mixed volumes.

Theorem 4.1. The volume polynomial$\mathrm { v o l _ { K } }$is a Lorentzian polynomial for any$\operatorname { K } = \left( \operatorname { K } _ { 1 } , \ldots , \operatorname { K } _ { n } \right)$

When combined with Theorem 2.25, Theorem 4.1 implies the following statement.

Corollary 4.2. The support of$\mathrm { v o l _ { K } }$is an M-convex for any$\operatorname { K } = \left( \operatorname { K } _ { 1 } , \ldots , \operatorname { K } _ { n } \right)$

In other words, the set of all$\alpha \in \Delta _ { n } ^ { d }$satisfying the non-vanishing condition

$$
V (\underbrace {\mathrm{K} _ {1} , \ldots , \mathrm{K} _ {1}} _ {\alpha_ {1}}, \ldots , \underbrace {\mathrm{K} _ {n} , \ldots , \mathrm{K} _ {n}} _ {\alpha_ {n}}) \neq 0
$$

is M-convex for any convex bodies$\mathrm { K } _ { 1 } , \ldots , \mathrm { K } _ { n }$in$\mathbb { R } ^ { d }$

Remark 4.3. The mixed volume$V ( \mathrm { C } _ { 1 } , \ldots , \mathrm { C } _ { d } )$is positive precisely when there are line segments $\ell _ { i } \subseteq \mathrm { C } _ { i }$with linearly independent directions [Sch14, Theorem 5.1.8]. Thus, when K consists of n line segments in$\mathbb { R } ^ { d } .$, Corollary 4.2 states the familiar fact that, for any configuration of n vectors ${ \mathcal { A } } \subseteq \mathbb { R } ^ { d }$, the collection of linearly independent d-subsets of A is the set of bases of a matroid.

The same reasoning shows that, in fact, the basis generating polynomial of a matroid on rns is the volume polynomial of n convex bodies precisely when the matroid is regular. In particular, not every Lorentzian polynomial is a volume polynomial of convex bodies. For example, the elementary symmetric polynomial

$$
w _ {1} w _ {2} + w _ {1} w _ {3} + w _ {1} w _ {4} + w _ {2} w _ {3} + w _ {2} w _ {4} + w _ {3} w _ {4}
$$

is not the volume polynomial of four convex bodies in the plane. By the compactness theorem of Shephard for the affine equivalence classes of n convex bodies [She60, Theorem 1], the image of the set of volume polynomials of convex bodies in$\mathbb { P } \mathrm { L } _ { n } ^ { d }$is compact. Thus, the displayed elementary symmetric polynomial is not even the limit of volume polynomials of convex bodies.

On the other hand, a collection$\mathrm { ~ J ~ } \subseteq \left[ { n \atop d } \right]$is the support of a volume polynomial of n convex bodies in$\mathbb { R } ^ { d }$if and only if J is the set of basis of a rank d matroid on rns that is representable over R. For example, there are no seven convex bodies in$\mathbb { R } ^ { 3 }$whose volume polynomial has the support given by the set of bases of the Fano matroid.

Proof of Theorem 4.1. By continuity of the volume functional [Sch14, Theorem 1.8.20], we may suppose that every convex body in K is d-dimensional. In this case, every coefficient of vol<sub>K</sub> is positive. Thus, by Theorem 2.25, it is enough to show that$\partial ^ { \alpha } \mathbf { v o l _ { H } }$is Lorentzian for every $\alpha \in \Delta _ { n } ^ { d - 2 }$. For this we use a special case of the Brunn-Minkowski theorem [Sch14, Theorem 7.4.5]: For any convex bodies$\mathrm { C } _ { 3 } , \ldots , \mathrm { C } _ { d }$in$\mathbb { R } ^ { d }$, the function

$$
w \longmapsto V \left(\sum_ {i = 1} ^ {n} w _ {i} \mathrm{K} _ {i}, \sum_ {i = 1} ^ {n} w _ {i} \mathrm{K} _ {i}, \mathrm{C} _ {3}, \dots , \mathrm{C} _ {d}\right) ^ {1 / 2}
$$

is concave on$\mathbb { R } _ { > 0 } ^ { n }$. In particular, the function

$$
\Big (\frac {2 !}{d !} \partial^ {\alpha} \mathrm{vol} _ {\mathrm{K}} (w) \Big) ^ {1 / 2} = V \Bigg (\sum_ {i = 1} ^ {n} w _ {i} \mathrm{K} _ {i}, \sum_ {i = 1} ^ {n} w _ {i} \mathrm{K} _ {i}, \underbrace {\mathrm{K} _ {1} , \ldots , \mathrm{K} _ {1}} _ {\alpha_ {1}}, \ldots , \underbrace {\mathrm{K} _ {n} , \ldots , \mathrm{K} _ {n}} _ {\alpha_ {n}} \Bigg) ^ {1 / 2}
$$

is concave on$\mathbb { R } _ { > 0 } ^ { n }$for every$\alpha \in \Delta _ { n } ^ { d - 2 }$. The conclusion follows from Proposition 2.33.□

The Alexandrov–Fenchel inequality [Sch14, Section 7.3] states that

$$
V \left(\mathrm{C} _ {1}, \mathrm{C} _ {2}, \mathrm{C} _ {3}, \dots , \mathrm{C} _ {d}\right) ^ {2} \geqslant V \left(\mathrm{C} _ {1}, \mathrm{C} _ {1}, \mathrm{C} _ {3}, \dots , \mathrm{C} _ {d}\right) V \left(\mathrm{C} _ {2}, \mathrm{C} _ {2}, \mathrm{C} _ {3}, \dots , \mathrm{C} _ {d}\right).
$$

We show that an analog holds for any Lorentzian polynomial.

Proposition 4.4. If$\begin{array} { r } { f = \sum _ { \alpha \in \Delta _ { n } ^ { d } } \frac { c _ { \alpha } } { \alpha ! } w ^ { \alpha } } \end{array}$is a Lorentzian polynomial, then

$$
c _ {\alpha} ^ {2} \geqslant c _ {\alpha + e _ {i} - e _ {j}} c _ {\alpha - e _ {i} + e _ {j}} \text {   for   any   } i, j \in [ n ] \text {   and   any   } \alpha \in \Delta_ {n} ^ {d}.
$$

Proof. Consider the Lorentzian polynomial${ \hat { o } } ^ { \alpha - e _ { i } - e _ { j } } f .$. Substituting$w _ { k }$by zero for all k other than i and$j ,$we get the bivariate quadratic polynomial

$$
\frac {1}{2} c _ {\alpha + e _ {i} - e _ {j}} w _ {i} ^ {2} + c _ {\alpha} w _ {i} w _ {+} \frac {1}{2} c _ {\alpha - e _ {i} + e _ {j}} w _ {j} ^ {2}.
$$

The displayed polynomial is Lorentzian by Theorem 2.10, and hence$c _ { \alpha } ^ { 2 } \geqslant c _ { \alpha + e _ { i } - e _ { j } } c _ { \alpha - e _ { i } + e _ { j } } ,$. □

We may reformulate Proposition 4.4 as follows. Let f be a homogeneous polynomial of degree d in n variables. The complete homogeneous form of$f$is the multi-linear function$F _ { f } : ( \mathbb { R } ^ { n } ) ^ { d } \to$ R defined by

$$
F _ {f} \left(v _ {1}, \dots , v _ {d}\right) = \frac {1}{d !} \frac {\partial}{\partial x _ {1}} \dots \frac {\partial}{\partial x _ {d}} f \left(x _ {1} v _ {1} + \dots + x _ {d} v _ {d}\right).
$$

Note that the complete homogeneous form of$f$is symmetric in its arguments. By Euler’s formula for homogeneous functions, we have

$$
F _ {f} (w, w, \dots , w) = f (w).
$$

Proposition 4.5. If$f$is Lorentzian, then, for any$v _ { 1 } \in \mathbb { R } ^ { n }$and$v _ { 2 } , \ldots , v _ { d } \in \mathbb { R } _ { \geq 0 } ^ { n } ,$

$$
F _ {f} (v _ {1}, v _ {2}, v _ {3}, \dots , v _ {d}) ^ {2} \geqslant F _ {f} (v _ {1}, v _ {1}, v _ {3}, \dots , v _ {d}) F _ {f} (v _ {2}, v _ {2}, v _ {3}, \dots , v _ {d}).
$$

Proof. For every$k = 1 , \ldots , d ,$we write$v _ { k } = ( v _ { k 1 } , v _ { k 2 } , \ldots , v _ { k n } )$, and set

$$
D _ {k} = v _ {k 1} \frac {\partial}{\partial w _ {1}} + v _ {k 2} \frac {\partial}{\partial w _ {2}} + \dots + v _ {k n} \frac {\partial}{\partial w _ {n}}.
$$

By Corollary 2.11, the quadratic polynomial$D _ { 3 } \cdots D _ { d } f$is Lorentzian. We may suppose that the Hessian H of the quadratic polynomial is not identically zero and$v _ { 2 } ^ { T } \mathcal { H } v _ { 2 } > 0$. Note that

$$
v _ {i} ^ {T} \mathcal {H} v _ {j} = D _ {i} D _ {j} D _ {3} \dots D _ {d} f = d! F _ {f} (v _ {i}, v _ {j}, v _ {3}, \dots , v _ {d}) \text {   for   any   } i \text {   and   } j.
$$

Since H has exactly one positive eigenvalue, the conclusion follows from Cauchy’s interlacing theorem.□

4.2. Projective varieties and Lorentzian polynomials. Let Y be a d-dimensional irreducible projective variety over an algebraically closed field F. If$\mathrm { D } _ { 1 } , \ldots , \mathrm { D } _ { d }$are Cartier divisors on$Y ,$ the intersection product$\left( \operatorname { D } _ { 1 } \cdot \ldots \cdot \operatorname { D } _ { d } \right)$is an integer defined by the following properties:

– the product$\left( \operatorname { D } _ { 1 } \cdot \ldots \cdot \operatorname { D } _ { d } \right)$is symmetric and multilinear as a function of its arguments,

– the product$\left( \operatorname { D } _ { 1 } \cdot \ldots \cdot \operatorname { D } _ { d } \right)$depends only on the linear equivalence classes of the$D _ { i } ,$, and

$- \ \mathrm { i f } \ \mathrm { D } _ { 1 } , \ldots , \mathrm { D } _ { n }$are effective divisors meeting transversely at smooth points of$Y _ { \iota }$, then

$$
\left(\mathrm{D} _ {1} \cdot \dots \cdot \mathrm{D} _ {d}\right) = \# \mathrm{D} _ {1} \cap \dots \cap \mathrm{D} _ {d}.
$$

Given an irreducible subvariety$X \subseteq Y$of dimension$k ,$the intersection product

$$
\left(\mathrm{D} _ {1} \cdot \dots \cdot \mathrm{D} _ {k} \cdot X\right)
$$

is then defined by replacing each divisor D<sub>i</sub> with a linearly equivalent Cartier divisor whose support does not contain X and intersecting the restrictions of$\mathrm { D } _ { i }$in$X$. The definition of the intersection product linearly extends to$\mathbb { Q } \mathrm { . }$-linear combination of Cartier divisors, called Q-divisors [Laz04, Section 1.3]. If D is a Q-divisor on$Y ,$, we write$( \mathrm Ḋ ) ^ Ḋ d Ḍ$for the self-intersection$\left( \mathrm { D } \cdot \ldots \cdot \mathrm { D } \right)$q For a gentle introduction to Cartier divisors and their intersection products, we refer to [Laz04, Section 1.1]. See [Ful98] for a comprehensive study.

Let$\mathrm { H } = \left( \mathrm { H } _ { 1 } , \ldots , \mathrm { H } _ { n } \right)$be a collection of$\mathbb { Q } \mathrm { . }$-divisors on$Y .$. We define the volume polynomial of H by

$$
\operatorname{vol} _ {\mathrm{H}} (w) = \left(w _ {1} H _ {1} + \dots + w _ {n} H _ {n}\right) ^ {d} = \sum_ {\alpha \in \Delta_ {n} ^ {d}} \frac {d !}{\alpha !} V _ {\alpha} (\mathrm{H}) w ^ {\alpha},
$$

where$V _ { \alpha } ( \mathrm { H } )$is the intersection product

$$
V _ {\alpha} (\mathrm{H}) = (\underbrace {\mathrm{H} _ {1} \cdot \ldots \cdot \mathrm{H} _ {1}} _ {\alpha_ {1}} \cdot \ldots \cdot \underbrace {\mathrm{H} _ {n} \cdot \ldots \cdot \mathrm{H} _ {n}} _ {\alpha_ {n}}) = \frac {1}{d !} \partial^ {\alpha} \mathrm{vol} _ {\mathrm{H}}.
$$

A Q-divisor D on$Y$is said to be nef if$\left( \mathrm { D } \cdot C \right) \geqslant 0$for every irreducible curve C in$Y \ [ \mathrm { L a z 0 4 }$ Section 1.4].

Theorem 4.6. If$\mathrm { H } _ { 1 } , \ldots , \mathrm { H } _ { n }$are nef divisors on$Y _ { \iota }$, then${ \mathrm { v o l } } _ { \mathrm { H } } ( w )$is a Lorentzian polynomial.

When combined with Theorem 2.25, Theorem 4.6 implies the statement.

Corollary 4.7. If$\mathrm { H } _ { 1 } , \ldots , \mathrm { H } _ { n }$are nef divisors on$Y ,$then the support of${ \mathrm { v o l } } _ { \mathrm { H } } ( w )$is M-convex.

In other words, the set of all$\alpha \in \Delta _ { n } ^ { d }$satisfying the non-vanishing condition

$$
(\underbrace {\mathrm{H} _ {1} \cdot \ldots \cdot \mathrm{H} _ {1}} _ {\alpha_ {1}} \cdot \ldots \cdot \underbrace {\mathrm{H} _ {n} \cdot \ldots \cdot \mathrm{H} _ {n}} _ {\alpha_ {n}}) \neq 0
$$

is M-convex for any d-dimensional projective variety$Y$and any nef divisors$\mathrm { H } _ { 1 } , \ldots , \mathrm { H } _ { n }$on$Y$ Corollary$4 . 7$implies a result of Castillo et al. [CRLMZ, Proposition 5.4], which says that the support of the multidegree of any irreducible mutiprojective variety is a discrete polymatroid.

Remark 4.8. Let$\mathcal { A } = \{ v _ { 1 } , \ldots , v _ { n } \}$be a collection of n vectors in$\mathbb { F } ^ { d }$. In [HW17, Section$^ { 4 ] , }$one can find a d-dimensional projective variety$Y _ { A }$and nef divisors$\mathrm { H } _ { 1 } , \ldots , \mathrm { H } _ { n }$on$Y _ { A }$such that

$$
\operatorname{vol} _ {\mathrm{H}} (w) = \sum_ {\alpha \in \left[ \begin{array}{c} n \\ d \end{array} \right]} c _ {\alpha} w ^ {\alpha},
$$

where$c _ { \alpha } = 1$if α corresponds to a linearly independent subset of A and$c _ { \alpha } = 0$if otherwise. Thus, in this case, Corollary 4.7 states the familiar fact that the collection of linearly independent d-subsets of$\mathcal { A } \subseteq \mathbb { F } ^ { d }$is the set of bases of a matroid.

Proof of Theorem 4.6. By Kleiman’s theorem [Laz04, Section 1.4], every nef divisor is a limit of ample divisors, and we may suppose that every divisor in H is very ample. In this case, every coefficient of$\mathrm { \ v o l _ { H } }$is positive. Thus, by Theorem 2.25, it is enough to show that$\partial ^ { \alpha } \mathrm { v o l _ { H } }$is Lorentzian for every$\alpha \in \Delta _ { n } ^ { d - 2 }$. Note that

$$
\frac {2 !}{d !} \partial^ {\alpha} \mathrm{vol} _ {\mathrm{H}} (w) = \left(\sum_ {i = 1} ^ {n} w _ {i} \mathrm{H} _ {i} \cdot \sum_ {i = 1} ^ {n} w _ {i} \mathrm{H} _ {i} \cdot \underbrace {\mathrm{H} _ {1} \cdot \ldots \cdot \mathrm{H} _ {1}} _ {\alpha_ {1}} \cdot \ldots \cdot \underbrace {\mathrm{H} _ {n} \cdot \ldots \cdot \mathrm{H} _ {n}} _ {\alpha_ {n}}\right).
$$

By Bertini’s theorem [Laz04, Section 3.3], there is an irreducible surface$S \subseteq Y$such that

$$
\frac {2 !}{d !} \partial^ {\alpha} \mathrm{vol} _ {\mathrm{H}} (w) = \left(\sum_ {i = 1} ^ {n} w _ {i} \mathrm{H} _ {i} \cdot \sum_ {i = 1} ^ {n} w _ {i} \mathrm{H} _ {i} \cdot S\right).
$$

If S is smooth, then the Hodge index theorem [Har77, Theorem V.1.9] shows that the displayed quadratic form has exactly one positive eigenvalue. In general, the Hodge index theorem applied to any resolution of singularities of S implies the one positive eigenvalue condition, by the projection formula [Ful98, Example 2.4.3].□

How large is the set of volume polynomials of projective varieties within the set of Lorentzian polynomials? We formulate various precise versions of this question. Let$\mathrm { V } _ { n } ^ { d } ( \mathbb { F } )$be the set of volume polynomials of n nef divisors on a d-dimensional projective variety over$\mathbb { F } ,$and let $\begin{array} { r } { \mathrm { V } _ { n } ^ { d } = \bigcup _ { \mathbb { F } } \mathrm { V } _ { n } ^ { d } ( \mathbb { F } ) } \end{array}$, where the union is over all algebraically closed fields.

Question 4.9. Fix any algebraically closed field F.

(1) Is there a polynomial in$\mathrm { L } _ { n } ^ { d }$that is not in the closure of$\mathrm { V } _ { n } ^ { d } ?$

(2) Is there a polynomial in$\mathrm { L } _ { n } ^ { d }$that is not in the closure of${ \mathrm { V } } _ { n } ^ { d } ( \mathbb { F } ) ?$

(3) Is there a polynomial in$\operatorname { L } _ { n } ^ { d } \cap \mathbb { Q } [ w ]$that is not in$\mathrm { V } _ { n } ^ { d } ?$

(4) Is there a polynomial in$\operatorname { L } _ { n } ^ { d } \cap \mathbb { Q } [ w ]$that is not in${ \mathrm { V } } _ { n } ^ { d } ( \mathbb { F } ) ?$

Shephard’s construction in [She60, Section 3] shows that every polynomial in L<sup>d</sup><sub>2</sub>$\cap \mathbb { Q } [ w ]$is the volume polynomial of a pair of d-dimensional convex polytopes with rational vertices. Thus, by [Ful93, Section 5.4], we have

$$
\mathrm{L} _ {2} ^ {d} \cap \mathbb {Q} [ w ] = \mathrm{V} _ {2} ^ {d} = \mathrm{V} _ {2} ^ {d} (\mathbb {F}) \text {   for   any   } d \text {   and   any   } \mathbb {F}.
$$

A similar reasoning based on the construction of [Hei38, Section I] shows that

$$
\mathrm{L} _ {3} ^ {2} \cap \mathbb {Q} [ w ] = \mathrm{V} _ {3} ^ {2} = \mathrm{V} _ {3} ^ {2} (\mathbb {F}) \text {   for   any   } \mathbb {F}.
$$

When n$\geqslant 4 ,$, not every Lorentzian polynomial is the limit of a sequence of volume polynomials of rational convex polytopes (Remark 4.3), and we do not know how to answer any of the above questions.<sup>15</sup>

4.3. Potts model partition functions and Lorentzian polynomials. The q-state Potts model, or the random-cluster model, of a graph is a much studied class of measures introduced by Fortuin and Kasteleyn [FK72]. We refer to [Gri06] for a comprehensive introduction to random-cluster models.

Let M be a matroid on rns, and let$\mathrm { r k _ { M } }$be the rank function of M. For a nonnegative integer k and a positive real parameter$q ,$consider the degree k homogeneous polynomial in n variables

$$
Z _ {q, \mathrm{M}} ^ {k} (w) = \sum_ {A \in \left[ \begin{array}{c} n \\ k \end{array} \right]} q ^ {- \operatorname{rk} _ {\mathrm{M}} (A)} w ^ {A}, \quad w = (w _ {1}, \ldots , w _ {n}).
$$

We define the homogeneous multivariate Tutte polynomial of M by

$$
\mathrm{Z} _ {q, \mathrm{M}} (w _ {0}, w _ {1}, \ldots , w _ {n}) = \sum_ {k = 0} ^ {n} \mathrm{Z} _ {q, \mathrm{M}} ^ {k} (w) w _ {0} ^ {n - k},
$$

which is a homogeneous polynomial of degree n in$n + 1$variables. When M is the cycle matroid of a graph G, the polynomial obtained from$\mathrm { Z } _ { q , \mathrm { M } }$by setting$w _ { 0 } = 1$is the partition function of the q-state Potts model associated to$G \left[ { \mathrm { S o k 0 } } 5 \right]$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">V3(F)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L3</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">V<sup>3</sup><sub>3</sub>pFq.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f “ 14x<sup>3</sup> \` 6x<sup>2</sup>y \` 24x<sup>2</sup>z \` 12xyz \` 6xz<sup>2</sup> \` 3yz<sup>2</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">V<sup>3</sup><sub>3</sub>pFq</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>15</sup>After the completion of this paper, we noticed that the closure of V<sup>3</sup><sub>3</sub>pFq is strictly smaller than L<sup>3</sup><sub>3</sub> for any F. This answers Question 4.9. Specifically, the Lorentzian cubic is not in the closure of That f is not in the closure of can be shown using the reverse Khovanskii-Teissier inequality [LX17, Theorem 5.7]: For any nef divisors H<sub>1</sub>, H<sub>2</sub>, H<sub>3</sub> on a d-dimensional projective variety and any k ď d, we haveH1, H2, H3k ≤ d,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">´<sup>d</sup><sub>k</sub>¯ pH<sup>k</sup><sub>2</sub> ¨ H<sup>d´k</sup><sub>1</sub> q pH<sup>k</sup><sub>1</sub> ¨ H<sup>d´k</sup><sub>3</sub> q ě pH<sup>d</sup><sub>1</sub>q pH<sup>k</sup><sub>2</sub> ¨ H<sup>d´k</sup><sub>3</sub> q.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">The complex analytic proof of the inequality in [LX17] relies on the Calabi-Yau theorem [Yau78]. The algebraic proof of the inequality in [JL] using Okounkov bodies works over any algebraically closed field. The theory of toric varieties shows that the volume polynomial of any set of convex bodies is the limit of a sequence of volume polynomials of nef divisors on projective varieties [Ful93, Section 5.4]. Thus, the Lorentzian cubic f provides a counterexample to Gurvits conjecture that a strongly log-concave homogeneous polynomial in three variables with nonnegative coefficients is the volume polynomial of three convex bodies [Gur09, Conjecture 4.1].</span></small>

Since the rank function of a matroid is$\mathrm { M } ^ { \natural . }$-concave, the normalized rank generating function of M is Lorentzian when the parameter q satisfies$0 < q \leqslant 1$, see Example 3.15. In this subsection, we prove the following refinement.

Theorem 4.10. For any matroid M and$0 < q \leqslant 1$, the polynomial$\mathrm { Z } _ { q , \mathrm { M } }$is Lorentzian.

We prepare the proof with two simple lemmas.

Lemma 4.11. The support of$\mathrm { Z } _ { q , \mathrm { M } }$is M-convex for all$0 < q \leqslant 1$

Proof. Writing$\mathrm { Z } _ { q , \mathrm { M } } ^ { \natural }$for the polynomial obtained from$\mathrm { Z } _ { q , \mathrm { M } }$by setting$w _ { 0 } = 1$, we have

$$
\operatorname{supp} \left(\mathrm{Z} _ {q, \mathrm{M}} ^ {\natural}\right) = \{0, 1 \} ^ {n}.
$$

It is straightforward to verify the augmentation property in Lemma 2.21 for$\{ 0 , 1 \} ^ { n }$□

For a nonnegative integer k and a subset$S \subseteq [ n ]$, we define a degree k homogeneous polynomial$e _ { S } ^ { k } ( w )$by the equation

$$
\sum_ {k = 0} ^ {n} e _ {S} ^ {k} (w) = \sum_ {A \subseteq S} w ^ {A}.
$$

In other words,$e _ { S } ^ { k } ( w )$is the k-th elementary symmetric polynomial in the variables$\{ w _ { i } \} _ { i \in S }$

Lemma 4.12. If$S _ { 1 } \sqcup \ldots \sqcup S _ { m }$is a partition of$[ n ]$into m nonempty parts, then

$$
\frac {1}{n} e _ {[ n ]} ^ {1} (w) ^ {2} \leqslant e _ {S _ {1}} ^ {1} (w) ^ {2} + \dots + e _ {S _ {m}} ^ {1} (w) ^ {2} \text {   for   all   } w \in \mathbb {R} ^ {n}.
$$

Proof. Since m ď$n ,$it is enough to prove the statement when$m = n$. In this case, we have

$$
(w _ {1} + \dots + w _ {n}) ^ {2} \leqslant n (w _ {1} ^ {2} + \dots + w _ {n} ^ {2}),
$$

by the Cauchy-Schwarz inequality for the vectors$( 1 , \ldots , 1 )$and$( w _ { 1 } , \ldots , w _ { n } ) \mathrm { i n } \mathbb { R } ^ { n }$

Proof of Theorem 4.10. Let α be an element of$\Delta _ { n + 1 } ^ { n - 2 }$. By Theorem 2.25 and Lemma 4.11, the proof reduces to the statement that the quadratic form$\partial ^ { \alpha } \mathrm { Z } _ { q , \mathrm { M } }$is stable. We prove the statement by induction on n. The assertion is clear when$n = 1 .$, so suppose$n \geqslant 2$. When$i \neq 0 ,$, we have

$$
\partial_ {i} \mathrm{Z} _ {q, \mathrm{M}} = q ^ {- \mathrm{rk} _ {\mathrm{M}} (i)} \mathrm{Z} _ {q, \mathrm{M} / i},
$$

where$\mathrm { M } / i$is the contraction of M by i [Oxl11, Chapter 3]. Thus, it is enough to prove that the following quadratic form is stable:

$$
\frac {n !}{2} w _ {0} ^ {2} + (n - 1)! \mathrm{Z} _ {q, \mathrm{M}} ^ {1} (w) w _ {0} + (n - 2)! \mathrm{Z} _ {q, \mathrm{M}} ^ {2} (w).
$$

Recall that a homogeneous polynomial f with nonnegative coefficients in$n + 1$variables is stable if and only if the univariate polynomial$f ( x u - v )$has only real zeros for all$v \in \mathbb { R } ^ { n + 1 }$for some$u \in \mathbb { R } _ { \geqslant 0 } ^ { n + 1 }$satisfying$f ( u ) > 0$. Therefore, it suffices to show that the discriminant of the displayed quadratic form with respect to$w _ { 0 }$is nonnegative:

$$
\mathrm{Z} _ {q, \mathrm{M}} ^ {1} (w) ^ {2} \geqslant 2 \frac {n}{n - 1} \mathrm{Z} _ {q, \mathrm{M}} ^ {2} (w) \text {   for   all   } w \in \mathbb {R} ^ {n}.
$$

We prove the inequality after making the change of variables

$$
w _ {i} \longmapsto \left\{ \begin{array}{l l} w _ {i} & \text {if i is a loop in M,} \\ q w _ {i} & \text {if i is not a loop in M.} \end{array} \right.
$$

Write$L \subseteq [ n ]$for the set of loops and$P _ { 1 } , \ldots , P _ { \ell } \subseteq [ n ] \backslash L$for the parallel classes in M [Oxl11, Section 1.1]. The above change of variables gives

$$
Z _ {q, \mathrm{M}} ^ {1} (w) = e _ {[ n ]} ^ {1} (w) \text {and} Z _ {q, \mathrm{M}} ^ {2} (w) = e _ {[ n ]} ^ {2} (w) - (1 - q) \bigl (e _ {P _ {1}} ^ {2} (w) + \dots + e _ {P _ {\ell}} ^ {2} (w) \bigr).
$$

When$q = 1 .$, the desired inequality directly follows from the case$m = n$of Lemma 4.12. Therefore, when proving the desired inequality for an arbitrary$0 < q \leqslant 1$, we may assume that

$$
e _ {P _ {1}} ^ {2} (w) + \dots + e _ {P _ {\ell}} ^ {2} (w) <   0.
$$

Therefore, exploiting the monotonicity of$\mathrm { Z } _ { q , \mathrm { M } } ^ { 2 }$in$q ,$the desired inequality reduces to

$$
(n - 1) e _ {[ n ]} ^ {1} (w) ^ {2} - 2 n \left(e _ {[ n ]} ^ {2} (w) - e _ {P _ {1}} ^ {2} (w) - \dots - e _ {P _ {\ell}} ^ {2} (w)\right) \geqslant 0.
$$

Note that the left-hand side of the above inequality simplifies to

$$
n \Big (e _ {P _ {1}} ^ {1} (w) ^ {2} + \dots + e _ {P _ {\ell}} ^ {1} (w) ^ {2} + \sum_ {i \in L} w _ {i} ^ {2} \Big) - e _ {[ n ]} ^ {1} (w) ^ {2}.
$$

The conclusion now follows from Lemma 4.12.

Mason [Mas72] offered the following three conjectures of increasing strength. Several authors studied correlations in matroid theory partly in pursuit of these conjectures [SW75, Wag08, BBL09, KN10, KN11].

Conjecture 4.13. For any matroid M on rns and any positive integer$k ,$

(1)$I _ { k } ( \mathrm { M } ) ^ { 2 } \geqslant I _ { k - 1 } ( \mathrm { M } ) I _ { k + 1 } ( \mathrm { M } ) ,$

(2)$\begin{array} { r } { I _ { k } ( \mathrm { M } ) ^ { 2 } \geqslant \frac { k + 1 } { k } I _ { k - 1 } ( \mathrm { M } ) I _ { k + 1 } ( \mathrm { M } ) . } \end{array}$

(3)$\begin{array} { r } { I _ { k } ( \mathrm { M } ) ^ { 2 } \geqslant \frac { k + 1 } { k } \frac { n - k + 1 } { n - k } I _ { k - 1 } ( \mathrm { M } ) I _ { k + 1 } ( \mathrm { M } ) _ { \mathrm { \Omega } } } \end{array}$

where$I _ { k } ( \mathrm { M } )$is the number of k-element independent sets of$\mathrm { M }$

Conjecture 4.13 (1) was proved in [AHK18], and Conjecture 4.13 (2) was proved in [HSW]. Note that Conjecture 4.13 (3) may be written

$$
\frac {I _ {k} (\mathrm{M}) ^ {2}}{\binom {n} {k} ^ {2}} \geqslant \frac {I _ {k + 1} (\mathrm{M})}{\binom {n} {k + 1}} \frac {I _ {k - 1} (\mathrm{M})}{\binom {n} {k - 1}},
$$

and the equality holds when all$( k + 1 )$-subsets of$[ n ]$are independent in M. Conjecture 4.13 (3) is known to hold when n is at most 11 or k is at most 5 [KN11]. See [Sey75, Dow80, Mah85, Zha85, HK12, HS89, Len13] for other partial results.

Theorem 4.14. For any matroid M on rns and any positive integer$k ,$

$$
\frac {I _ {k} (\mathrm{M}) ^ {2}}{\binom {n} {k} ^ {2}} \geqslant \frac {I _ {k + 1} (\mathrm{M})}{\binom {n} {k + 1}} \frac {I _ {k - 1} (\mathrm{M})}{\binom {n} {k - 1}},
$$

where$I _ { k } ( \mathrm { M } )$is the number of k-element independent sets of M.

In [BH], direct proofs of Theorems 4.10 and 4.14 were given.<sup>16</sup> Here we deduce Theorem 4.14 from the Lorentzian property of

$$
f _ {\mathrm{M}} (w _ {0}, w _ {1}, \ldots , w _ {n}) = \sum_ {A \in \mathcal {I} (\mathrm{M})} w ^ {A} w _ {0} ^ {n - | A |}, \quad w = (w _ {1}, \ldots , w _ {n}),
$$

where IpMq is the collection of independent sets of M.

Proof of Theorem 4.14. The polynomial$f _ { \mathrm { M } }$is Lorentzian by Theorem 4.10 and the identity

$$
f _ {\mathrm{M}} (w _ {0}, w _ {1}, \dots , w _ {n}) = \lim _ {q \to 0} Z _ {q, \mathrm{M}} (w _ {0}, q w _ {1}, \dots , q w _ {n}).
$$

Therefore, by Theorem 2.10, the bivariate polynomial obtained from$f _ { \mathrm { M } }$by setting$w _ { 1 } = \cdot \cdot \cdot = w _ { n }$ is Lorentzian. The conclusion follows from the fact that a bivariate homogeneous polynomial with nonnegative coefficients is Lorentzian if and only if the sequence of coefficients form an ultra log-concave sequence with no internal zeros.□

The Tutte polynomial of a matroid M on rns is the bivariate polynomial

$$
\mathrm{T} _ {\mathrm{M}} (x, y) = \sum_ {A \subseteq [ n ]} (x - 1) ^ {\mathrm{rk} _ {\mathrm{M}} ([ n ]) - \mathrm{rk} _ {\mathrm{M}} (A)} (y - 1) ^ {| A | - \mathrm{rk} _ {\mathrm{M}} (A)}.
$$

Theorem 4.10 reveals several nontrivial inequalities satisfied by the coefficients of the Tutte polynomial. For example, if we write

$$
w ^ {\mathrm{rk} _ {\mathrm{M}} ([ n ])} \mathrm{T} _ {\mathrm{M}} \left(1 + \frac {q}{w}, 1 + w\right) = \sum_ {k = 0} ^ {n} \left(\sum_ {A \in \left[ \begin{array}{c} n \\ k \end{array} \right]} q ^ {\mathrm{rk} _ {\mathrm{M}} ([ n ]) - \mathrm{rk} _ {\mathrm{M}} (A)}\right) w ^ {k} = \sum_ {k = 0} ^ {n} c _ {q} ^ {k} (\mathrm{M}) w ^ {k},
$$

then the sequence$c _ { q } ^ { k } ( \mathrm { M } )$is ultra log-concave whenever$0 \leqslant q \leqslant 1$. This and other results in this subsection are recently extended to flag matroids in [EH20].

4.4. M-matrices and Lorentzian polynomials. We write$\mathrm { I } _ { n }$for the$n \times n$identity matrix,${ \mathrm { J } } _ { n }$for the$n \times n$matrix all of whose entries are 1, and$1 _ { n }$for the$n \times 1$matrix all of whose entries are 1. Let$A = \left( a _ { i j } \right)$be an$n \times n$matrix with real entries. The following conditions are equivalent if $a _ { i j } \leqslant 0$for all$i \neq j \ [ \mathrm { B P } 9 4$, Chapter 6]:

– The real part of each nonzero eigenvalue of A is positive.

– The real part of each eigenvalue of A is nonnegative.

– All the principal minors of A are nonnegative.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>16</sup>An independent proof of 4.14 was given by Anari et al. in [ALOVIII].</span></small>

– Every real eigenvalue of A is nonnegative.

– The matrix$\mathrm { A } + \epsilon \mathrm { I } _ { n }$is nonsingular for every$\epsilon > 0$

– The univariate polynomial det$( x \mathrm { I } _ { n } + \mathrm { A } )$has nonnegative coefficients.

The matrix A is an M-matrix if$a _ { i j } ~ \leqslant ~ 0$for all$i \ \ne \ j$and if it satisfies any one of the above conditions. One can find 50 different characterizations of nonsingular M-matrices in [BP94, Chapter 6]. Among others, we will use the 29-th condition:

– There are positive diagonal matrices$D$and$D ^ { \prime }$such that$D A D ^ { \prime }$has all diagonal entries 1 and all row sums positive.

For a discussion of M-matrices in the context of ultrametrics and potentials of finite Markov chains, see [DMS14].

We define the multivariate characteristic polynomial of A by the equation

$$
\mathrm{p} _ {\mathrm{A}} \left(w _ {0}, w _ {1}, \dots , w _ {n}\right) = \det \left(w _ {0} \mathrm{I} _ {n} + \operatorname{diag} \left(w _ {1}, \dots , w _ {n}\right) \mathrm{A}\right).
$$

In [Hol05, Theorem$^ { 4 ] , }$Holtz proved that the coefficients of the characteristic polynomial of an M-matrix form an ultra log-concave sequence. We will strengthen this result and prove that the multivariate characteristic polynomial of an M-matrix is Lorentzian.

Theorem 4.15. If A is an M-matrix, then$\mathrm { p } _ { \mathrm { A } }$is a Lorentzian polynomial.

Using Example 2.26, we may recover the theorem of Holtz by setting$w _ { 1 } = \cdot \cdot \cdot = w _ { n }$

Corollary 4.16. If A is an M-matrix, then the support of$\mathrm { p } _ { \mathrm { A } }$is M-convex.

Since every M-matrix is a limit of nonsingular M-matrices, it is enough to prove Theorem 4.15 for nonsingular M-matrices.

Lemma 4.17. If A is a nonsingular M-matrix, the support of$\mathrm { p _ { A } }$is M-convex.

Proof. It is enough to prove that the support of$\mathrm { p _ { A } ^ { \natural } }$is$\mathrm { M } ^ { \natural . }$-convex, where

$$
\mathrm{p} _ {\mathrm{A}} ^ {\natural} (w _ {1}, \dots , w _ {n}) = \mathrm{p} _ {\mathrm{A}} (1, w _ {1}, \dots , w _ {n}).
$$

If A is a nonsingular M-matrix, then all the principal minors of A are positive, and hence

$$
\operatorname{supp} \left(\mathrm{p} _ {\mathrm{A}} ^ {\natural}\right) = \{0, 1 \} ^ {n}.
$$

It is straightforward to verify the augmentation property in Lemma 2.21 for$\{ 0 , 1 \} ^ { n }$□

We prepare the proof of Theorem 4.15 with a proposition on doubly sub-stochastic matrices. Recall that an$n \times n$matrix$\mathrm { B } = \left( b _ { i j } \right)$with nonnegative entries is said to be doubly sub-stochastic if

$$
\sum_ {j = 1} ^ {n} b _ {i j} \leqslant 1 \text {   for   every   } i \quad \text { and } \quad \sum_ {i = 1} ^ {n} b _ {i j} \leqslant 1 \text {   for   every   } j.
$$

A partial permutation matrix is a zero-one matrix with at most one nonzero entry in each row and column. We use Mirsky’s analog of the Birkhoff-von Neumann theorem for doubly substochastic matrices [HJ94, Theorem 3.2.6]: The set of$n \times n$doubly sub-stochastic matrix is equal to the convex hull of the$n \times n$partial permutation matrices.

Lemma 4.18. For n$\geqslant 2 ,$define$n \times n$matrices$\mathrm { M } _ { n }$and$\mathrm { N } _ { n }$by

$$
\mathrm{M} _ {n} = \left( \begin{array}{c c c c c c} 2 & 1 & 0 & \dots & 0 & 1 \\ 1 & 2 & 1 & \dots & 0 & 0 \\ 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 1 \\ 1 & 0 & 0 & \dots & 1 & 2 \end{array} \right), \quad \mathrm{N} _ {n} = \left( \begin{array}{c c c c c c} 2 & 1 & 0 & \dots & 0 & 0 \\ 1 & 2 & 1 & \dots & 0 & 0 \\ 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 1 \\ 0 & 0 & 0 & \dots & 1 & 2 \end{array} \right).
$$

Then the matrices$\mathrm { M } _ { n } - { \textstyle \frac { 2 } { n } } \mathrm { J } _ { n }$and$\mathrm { N } _ { n } - { \frac { 2 } { n } } \mathrm { J } _ { n }$are positive semidefinite. Equivalently,

$$
\underline {{\mathrm{M}}} _ {n + 1} := \left( \begin{array}{c c} \mathrm{M} _ {n} & 1 _ {n} \\ 1 _ {n} ^ {T} & \frac {n}{2} \end{array} \right), \quad \underline {{\mathrm{N}}} _ {n + 1} := \left( \begin{array}{c c} \mathrm{N} _ {n} & 1 _ {n} \\ 1 _ {n} ^ {T} & \frac {n}{2} \end{array} \right)
$$

are positive semidefinite.

Proof. We define symmetric matrices$\mathrm { L } _ { n + 1 }$and$\mathrm { K } _ { n + 1 }$by

$$
\mathrm{L} _ {n + 1} = \left( \begin{array}{c c c c c c c} 1 & 1 & 0 & \dots & 0 & 0 & \frac {1}{2} \\ 1 & 2 & 1 & \dots & 0 & 0 & 1 \\ 0 & 1 & 2 & \dots & 0 & 0 & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 1 & 1 \\ 0 & 0 & 0 & \dots & 1 & 1 & \frac {1}{2} \\ \frac {1}{2} & 1 & 1 & \dots & 1 & \frac {1}{2} & \frac {n}{2} \end{array} \right), \quad \mathrm{K} _ {n + 1} = \left( \begin{array}{c c c c c c c} 1 & 1 & 0 & \dots & 0 & 0 & \frac {1}{2} \\ 1 & 2 & 1 & \dots & 0 & 0 & 1 \\ 0 & 1 & 2 & \dots & 0 & 0 & 1 \\ \vdots & \vdash & \vdash & \ddots & \vdash & \vdash & \vdash \\ 0 & 0 & 0 & \dots & 2 & 1 & 1 \\ 0 & 0 & 0 & \dots & 1 & 2 & 1 \\ \frac {1}{2} & 1 & 1 & \dots & 1 & 1 & \frac {n}{2} \end{array} \right).
$$

As before, the subscript indicates the size of the matrix. We show, by induction on$n ,$that the matrices$\mathrm { L } _ { n + 1 }$<sub>1</sub> and$\mathrm { K } _ { n + 1 }$are positive semidefinite. It is straightforward to check that$\mathrm { L _ { 3 } }$and $\mathrm { K _ { 3 } }$are positive semidefinite. Perform the symmetric row and column elimination of$\mathrm { L } _ { n + 1 }$and $\mathrm { K } _ { n + 1 }$based on their$1 \times 1$entries, and notice that

$$
\mathrm{L} _ {n + 1} \simeq \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & \dots & 0 & 0 & 0 \\ 0 & 1 & 1 & \dots & 0 & 0 & \frac {1}{2} \\ 0 & 1 & 2 & \dots & 0 & 0 & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 1 & 1 \\ 0 & 0 & 0 & \dots & 1 & 1 & \frac {1}{2} \\ 0 & \frac {1}{2} & 1 & \dots & 1 & \frac {1}{2} & \frac {n}{2} - \frac {1}{4} \end{array} \right), \quad \mathrm{K} _ {n + 1} \simeq \left( \begin{array}{c c c c c c c} 1 & 0 & 0 & \dots & 0 & 0 & 0 \\ 0 & 1 & 1 & \dots & 0 & 0 & \frac {1}{2} \\ 0 & 1 & 2 & \dots & 0 & 0 & 1 \\ \vdots \\ 0 & 0 & 0 & \dots & 2 & 1 & 1 \\ 0 & 0 & 0 & \dots & 1 & 1 & 1 \\ 0 & \frac {1}{2} & 1 & \dots & 1 & 1 & \frac {n}{2} - \frac {1}{4} \end{array} \right),
$$

where the symbol » stands for the congruence relation for symmetric matrices. Since$\mathrm { L } _ { n }$is positive semidefinite,$\mathrm { L } _ { n + 1 }$is congruent to the sum of positive semidefinite matrices, and hence $\mathrm { L } _ { n + 1 }$is positive semidefinite. Similarly, since$\mathrm { K } _ { n }$is positive semidefinite,$\mathrm { K } _ { n + 1 }$is congruent to the sum of positive semidefinite matrices, and hence$\mathrm { K } _ { n + 1 }$is positive semidefinite.

We now prove that the symmetric matrices$\textstyle { \mathrm { { M } } _ { n + 1 } }$and${ \underline { { \mathrm { N } } } } _ { n + 1 }$are positive semidefinite. Perform the symmetric row and column elimination of$\textstyle { \mathrm { { M } } _ { n + 1 } }$and${ \underline { { \mathrm { N } } } } _ { n + 1 }$based on their$1 \times 1$entries, and notice that

$$
\underline {{\mathrm{M}}} _ {n + 1} \simeq \left( \begin{array}{c c c c c c c} 2 & 0 & 0 & \dots & 0 & 0 & 0 \\ 0 & \frac {3}{2} & 1 & \dots & 0 & - \frac {1}{2} & \frac {1}{2} \\ 0 & 1 & 2 & \dots & 0 & 0 & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 1 & 1 \\ 0 & - \frac {1}{2} & 0 & \dots & 1 & \frac {3}{2} & \frac {1}{2} \\ 0 & \frac {1}{2} & 1 & \dots & 1 & \frac {1}{2} & \frac {n - 1}{2} \end{array} \right), \quad \underline {{\mathrm{N}}} _ {n + 1} \simeq \left( \begin{array}{c c c c c c c} 2 & 0 & 0 & \dots & 0 & 0 & 0 \\ 0 & \frac {3}{2} & 1 & \dots & 0 & 0 & \frac {1}{2} \\ 0 & 1 & 2 & \dots & 0 & 0 & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 2 & 1 & 1 \\ 0 & 0 & 0 & \dots & 1 & 2 & 1 \\ 0 & \frac {1}{2} & 1 & \dots & 1 & 1 & \frac {n - 1}{2} \end{array} \right).
$$

Since$\mathrm { L } _ { n }$is positive semidefinite,, Mn+$\textstyle \mathrm { { M } } _ { n + 1 }$is congruent to the sum of two positive semidefinite matrices, and hence$\underline { { \mathrm { M } } } _ { n + 1 }$is positive semidefinite. Similarly, since$\mathrm { K } _ { n }$is positive semidefinite, ${ \underline { { \mathrm { N } } } } _ { n + 1 }$is congruent to the sum of two positive semidefinite matrices, and hence$\underline { { \mathrm { N } } } _ { n + 1 }$is positive semidefinite.□

Proposition 4.19. If B is an$n \times n$doubly sub-stochastic matrix, then$\begin{array} { r } { 2 \mathrm { I } _ { n } + \mathrm { B } + \mathrm { B } ^ { T } - \frac { 2 } { n } \mathrm { J } _ { n } } \end{array}$is positive semidefinite.

Proof. Let$\mathrm { C } _ { n }$be the symmetric matrix$2 \mathrm { I } _ { n } + \mathrm { B } + \mathrm { B } ^ { T }$, and let$\underline { { \mathrm { C } } } _ { n + 1 }$be the symmetric matrix

$$
\underline {{\mathrm{C}}} _ {n + 1} := \left( \begin{array}{c c} \mathrm{C} _ {n} & 1 _ {n} \\ 1 _ {n} ^ {T} & \frac {n}{2} \end{array} \right).
$$

It is enough to prove that$\underline { { \mathrm { C } } } _ { n + 1 }$is positive semidefinite. Since the convex hull of the partial permutation matrices is the set of doubly sub-stochastic matrix, the proof reduces to the case when B is a partial permutation matrix. We use the following extension of the cycle decomposition for partial permutations: For any partial permutation matrix${ \mathrm { B } } ,$there is a permutation matrix P such that$\mathrm { P B P } ^ { T }$is a block diagonal matrix, where each block diagonal is either zero, identity,

$$
\left( \begin{array}{c c c c c c} 0 & 0 & 0 & \dots & 0 & 1 \\ 1 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 0 & 0 \\ 0 & 0 & 0 & \dots & 1 & 0 \end{array} \right)
$$

or

$$
\left( \begin{array}{c c c c c c} 0 & 0 & 0 & \dots & 0 & 0 \\ 1 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 0 & 0 \\ 0 & 0 & 0 & \dots & 1 & 0 \end{array} \right).
$$

Using the cyclic decomposition for${ \mathrm { B } } ,$we can express the matrix$\underline { { \mathrm { C } } } _ { n + 1 }$as a sum, where each summand is positive semidefinite by Lemma 4.18.□

The remaining part of the proof of Theorem 4.15 parallels that of Theorem 4.10.

Proof of Theorem 4.15. Since every M-matrix is a limit of nonsingular M-matrices, we may suppose that A is a nonsingular M-matrix. For$k = 0 , 1 , \ldots , n ,$we set

$$
\mathrm{p} _ {\mathrm{A}} ^ {k} (w) = \sum_ {\alpha \in \left[ \begin{array}{c} n \\ k \end{array} \right]} \mathrm{A} _ {\alpha} w ^ {\alpha}, \quad w = (w _ {1}, \ldots , w _ {n}),
$$

where$\mathrm { A } _ { \alpha }$is the principal minor of A corresponding to$\alpha ,$so that

$$
\mathrm{p} _ {\mathrm{A}} (w _ {0}, w _ {1}, \dots , w _ {n}) = \sum_ {k = 0} ^ {n} \mathrm{p} _ {\mathrm{A}} ^ {k} (w) w _ {0} ^ {n - k}.
$$

Lemma 4.17 shows that the support of$\mathrm { p } _ { \mathrm { A } }$is M-convex. Therefore, by Theorem 2.25, it is enough to prove that$\partial _ { i } ( \mathrm { p _ { A } } )$is Lorentzian for$i = 0 , 1 , \ldots , n$. We prove this statement by induction on n. The assertion is clear when$n = 1 .$, so suppose$n \geqslant 2$

When$i \neq 0 ,$write B for the inverse of A and$\mathrm { B } / i$for the matrix obtained from B by deleting the i-th row and column. We observe that the i-th partial derivative of$p _ { \mathrm { A } }$is given by

$$
\begin{array}{l} \partial_ {i} \mathrm{p} _ {\mathrm{A}} (w _ {0}, w _ {1}, \ldots , w _ {n}) = \partial_ {i} \det \Big (w _ {0} \mathrm{I} _ {n} + \mathrm{diag} (w _ {1}, \ldots , w _ {n}) \mathrm{A} \Big) \\ \qquad = \det (\mathrm{A})   \partial_ {i} \det \Big (w _ {0} \mathrm{B} + \mathrm{diag} (w _ {1}, \ldots , w _ {n}) \Big) \\ \qquad = \det (\mathrm{A}) \det \Big (w _ {0} (\mathrm{B} / i) + \mathrm{diag} (w _ {1}, \ldots , \hat {w _ {i}}, \ldots , w _ {n}) \Big) \\ \qquad = \det (\mathrm{A}) \det (\mathrm{B} / i) \det \Big (w _ {0} \mathrm{I} _ {n - 1} + \mathrm{diag} (w _ {1}, \ldots , \hat {w _ {i}}, \ldots , w _ {n}) (\mathrm{B} / i) ^ {- 1} \Big). \end{array}
$$

By [Mar72, Theorem 3.1], the matrix$B / i$has positive determinant and its inverse is an$M -$ matrix, so the induction hypotheis applies to the right-hand side. Thus, to conclude, it is enough to prove that the following quadratic form is stable:

$$
\frac {n !}{2} w _ {0} ^ {2} + (n - 1)! \mathrm{p} _ {\mathrm{A}} ^ {1} (w) w _ {0} + (n - 2)! \mathrm{p} _ {\mathrm{A}} ^ {2} (w).
$$

As in the proof of Theorem 4.10 it suffices to show that the discriminant of the displayed quadratic form with respect to$w _ { 0 }$is nonnegative:

$$
\mathrm{p} _ {\mathrm{A}} ^ {1} (w) ^ {2} \geqslant \frac {2 n}{n - 1} \mathrm{p} _ {\mathrm{A}} ^ {2} (w) \text {for all} w \in \mathbb {R} ^ {n}.
$$

In terms of the entries of A, the displayed inequality is equivalent to the statement that the matrix$\begin{array} { r } { \left( a _ { i j } a _ { j i } - \frac { 1 } { n } a _ { i i } a _ { j j } \right) } \end{array}$is positive semidefinite. According to the 29-th characterization of nonsingular M-matrices in [BP94, Chapter 6], there are positive diagonal matrices D and$D ^ { \prime }$ such that$D A D ^ { \prime }$has all diagonal entries 1 and all row sums positive. Therefore, we may suppose that A has all diagonal entries 1 and all the row sums of A are positive. Under this assumption,

$$
\left(a _ {i j} a _ {j i} - \frac {1}{n} a _ {i i} a _ {j j}\right) = \mathrm{I} _ {n} - \mathrm{B} - \frac {1}{n} \mathrm{J} _ {n},
$$

where ´B is a symmetric doubly sub-stochastic matrix all of whose diagonal entries are zero. The conclusion follows from Proposition 4.19.□

4.5. Lorentzian probability measures. There are numerous important examples of negatively dependent “repelling” random variables in probability theory, combinatorics, stochastic processes, and statistical mechanics. See, for example, [Pem00]. A theory of negative dependence for strongly Rayleigh measures was developed in [BBL09], but the theory is too restrictive for several applications. Here we introduce a broader class of discrete probability measures using the Lorentzian property.

A discrete probability measure$\mu$on$\{ 0 , 1 \} ^ { n }$is a probability measure on$\{ 0 , 1 \} ^ { n }$such that all subsets of$\{ 0 , 1 \} ^ { n }$are measurable. The partition function of$\mu$is the polynomial

$$
Z _ {\mu} (w) = \sum_ {S \subseteq [ n ]} \mu (\{S \}) \prod_ {i \in S} w _ {i}.
$$

The following notions capture various aspects of negative dependence:

– The measure$\mu$is pairwise negatively correlated (PNC) if for all distinct i and$j$in rns,

$$
\mu (\mathcal {E} _ {i} \cap \mathcal {E} _ {j}) \leqslant \mu (\mathcal {E} _ {i}) \mu (\mathcal {E} _ {j}),
$$

where$\mathcal { E } _ { i }$is the collection of all subsets of$[ n ]$containing i.

– The measure$\mu$is ultra log-concave (ULC) if for every positive integer$k < n ,$

$$
\frac {\mu \left(\left[ \begin{array}{c} n \\ k \end{array} \right]\right) ^ {2}}{\binom {n} {k} ^ {2}} \geqslant \frac {\mu \left(\left[ \begin{array}{c} n \\ k - 1 \end{array} \right]\right)}{\binom {n} {k - 1}} \frac {\mu \left(\left[ \begin{array}{c} n \\ k + 1 \end{array} \right]\right)}{\binom {n} {k + 1}}.
$$

– The measure$\mu$is strongly Rayleigh if for all distinct i and$j$in rns,

$$
\mathrm{Z} _ {\mu} (w) \partial_ {i} \partial_ {j} \mathrm{Z} _ {\mu} (w) \leqslant \partial_ {i} \mathrm{Z} _ {\mu} (w) \partial_ {j} \mathrm{Z} _ {\mu} (w) \text {   for   all   } w \in \mathbb {R} ^ {n}.
$$

Let$\mathrm { P }$be a property of discrete probability measures. We say that$\mu$has property$\underline { { \mathrm { ~ P ~ i f ~ } } } ,$for every $x \in \mathbb { R } _ { > 0 } ^ { n } ,$the discrete probability measure on$\{ 0 , 1 \} ^ { n }$with the partition function

$$
\mathrm{Z} _ {\mu} (x _ {1} w _ {1}, \ldots , x _ {n} w _ {n}) / \mathrm{Z} _ {\mu} (x _ {1}, \ldots , x _ {n})
$$

has property P. The new discrete probability measure is said to be obtained from$\mu$by applying the external field$x \in \mathbb { R } _ { > 0 } ^ { n }$. For example, the property PNC for$\mu$is equivalent to the 1-Rayleigh property

$\mathrm { Z } _ { \mu } ( w ) \hat { \sigma } _ { i } \hat { \sigma } _ { j } \mathrm { Z } _ { \mu } ( w ) \leqslant \hat { \sigma } _ { i } \mathrm { Z } _ { \mu } ( w ) \hat { \sigma } _ { j } \mathrm { Z } _ { \mu } ( w )$for all distinct$i , j$in rns and all$w \in \mathbb { R } _ { > 0 } ^ { n }$

More generally, for a positive real number$c ,$we say that$\mu$is c-Rayleigh if

$\mathrm { Z } _ { \mu } ( w ) \hat { \sigma } _ { i } \hat { \sigma } _ { j } \mathrm { Z } _ { \mu } ( w ) \leqslant c \hat { \sigma } _ { i } \mathrm { Z } _ { \mu } ( w ) \hat { \sigma } _ { j } \mathrm { Z } _ { \mu } ( w )$for all distinct$i , j$in rns and all$w \in \mathbb { R } _ { > 0 } ^ { n }$

Definition 4.20. A discrete probability measure$\mu$on$\{ 0 , 1 \} ^ { n }$is Lorentzian if the homogenization of the partition function$w _ { 0 } ^ { n } \mathrm { Z } _ { \mu } ( w _ { 1 } / w _ { 0 } , \dots , w _ { n } / w _ { 0 } )$is a Lorentzian polynomial.

For example, if A is an M-matrix of size$n ,$the probability measure on$\{ 0 , 1 \} ^ { n }$given by

$$
\mu (\{S \}) \propto \left(\text { the   principal   minor   of   A   corresponding   to } S\right), \quad S \subseteq [ n ],
$$

is Lorentzian by Theorem 4.15. Results from the previous sections reveal basic features of Lorentzian measures, some of which may be interpreted as negative dependence properties.

Proposition 4.21. If$\mu$is Lorentzian, then$\mu$is 2-Rayleigh.

Proof. Lemma 2.20 and Proposition 2.19 show that$\mathrm { Z } _ { \mu }$is a$\textstyle 2 { \left( 1 - { \frac { 1 } { n } } \right) }$-Rayleigh polynomial. □

Proposition 4.22. If$\mu$is Lorentzian, then$\mu$is ULC.

Proof. Since any probability measure obtained from a Lorentzian probability measure by applying an external field is Lorentzian, it suffices to prove that$\mu$is ULC. By Theorem 2.10, the bivariate homogeneous polynomial$w _ { 0 } ^ { n } \mathrm { Z } _ { \mu } ( w _ { 1 } / w _ { 0 } , \dots , w _ { 1 } / w _ { 0 } )$is Lorentzian. Therefore, by Example 2.26, its sequence of coefficients must be ultra log-concave.□

Proposition 4.23. The class of Lorentzian measures is preserved under the symmetric exclusion process.

Proof. The statement is Corollary 3.9 for homogenized partition functions of Lorentzian probability measures.□

Proposition 4.24. If$\mu$is strongly Rayleigh, then$\mu$is Lorentzian.

Proof. A multi-affine polynomial is stable if and only if it is strongly Rayleigh [Bra07 ¨ , Theorem $5 . 6 ] ,$, and a polynomial with nonnegative coefficients is stable if and only if its homogenization is stable [BBL09, Theorem 4.5]. By Proposition 2.2, homogeneous stable polynomials with nonnegative coefficients are Lorentzian.□

For a matroid M on$[ n ] ,$we define probability measures$\mu _ { \mathrm { M } }$and$\nu _ { \mathrm { M } }$on$\{ 0 , 1 \} ^ { n }$by

$\mu _ { \mathrm { M } } =$the uniform measure on$\{ 0 , 1 \} ^ { n }$concentrated on the independent sets of$\mathrm { M } ,$

$\nu _ { \mathrm { M } }$“ the uniform measure on$\{ 0 , 1 \} ^ { n }$concentrated on the bases of M.

Proposition 4.25. For any matroid M$\mathrm { o n } [ n ] ,$the measures$\mu _ { \mathrm { M } }$and$\nu _ { \mathrm { M } }$are Lorentzian.

Proof. Note that the homogenized partition function$f _ { \mathrm { M } }$of$\mu _ { \mathrm { M } }$satisfies

$$
f _ {\mathrm{M}} (w _ {0}, w _ {1}, \dots , w _ {n}) = \lim _ {q \rightarrow 0} Z _ {q, \mathrm{M}} (w _ {0}, q w _ {1}, \dots , q w _ {n}).
$$

Since a limit of Lorentzian polynomials is Lorentzian,$\mu _ { \mathrm { M } }$is Lorentzian by Theorem 4.10. The partition function of$\nu _ { \mathrm { M } }$is Lorentzian by Theorem 3.10.□

Let G be an arbitrary finite graph and let i and$j$be any distinct edges of G. A conjecture of Kahn [Kah00] and Grimmett–Winkler [GW04] states tha$\mathbf { t , }$if$F$is a forest in$G$chosen uniformly at random, then

$$
\operatorname * {P r} (F \text {   contains   } i \text {   and   } j) \leqslant \operatorname * {P r} (F \text {   contains   } i) \operatorname * {P r} (F \text {   contains   } j).
$$

The conjecture is equivalent to the statement that$\mu _ { \mathrm { M } }$is 1-Rayleigh for any graphic matroid M. Propositions 4.21 and 4.25 show that$\mu _ { \mathrm { M } }$is 2-Rayleigh for any matroid M.

## REFERENCES

[AHK18] Karim Adiprasito, June Huh, and Eric Katz, Hodge theory for combinatorial geometries. Ann. of Math. (2) 188 (2018), no. 2, 381–452. 5, 49

[AOVI] Nima Anari, Shayan Oveis Gharan, and Cynthia Vinzant, Log-Concave Polynomials I: Entropy and a Deterministic Approximation Algorithmfor Counting Bases ofMatroids. arXiv:1807.00929. 3, 5, 23, 24, 32

[ALOVII] Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant, Log-Concave Polynomials II: High dimensional walks and an FPRASfor counting bases ofa matroid. arXiv:1811.0181. 5, 39

[ALOVIII] Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant, Log-Concave Polynomials III: Mason’s Ultra-Log-Concavity Conjecturefor Independent Sets ofMatroids. arXiv:1811.01600. 5, 23, 50

[BR97] Ravindra Bapat and Tirukkannamangai Raghavan, Nonnegative matrices and applications. Encyclopedia of Math ematics and its Applications 64. Cambridge University Press, Cambridge, 1997. 37, 39

[BCR84] Christian Berg, Jens Christensen, and Paul Ressel, Harmonic analysis on semigroups. Theory of positive definite and relatedfunctions. Graduate Texts in Mathematics 100. Springer-Verlag, New York, 1984. 39

[BP94] Abraham Berman, and Robert Plemmons, Nonnegative matrices in the mathematical sciences. Revised reprint of the 1979 original. Classics in Applied Mathematics 9. Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA, 1994 5, 50, 51, 54

[BB08] Julius Borcea and Petter Brand ¨ en, ´ Applications of stable polynomials to mixed determinants: Johnson’s conjectures, unimodality, and symmetrized Fischer products, Duke Math. J. 143 (2008), 205–223. 8

[BB09] Julius Borcea and Petter Brand ¨ en, ´ The Lee–Yang and P´olya–Schur programs. I. Linear operators preserving stability. Invent. Math. 177 (2009), 541–569. 3, 26, 28

[BB10] Julius Borcea and Petter Brand ¨ en, ´ Multivariate P´olya–Schur classification problems in the Weyl algebra. Proc. Lond. Math. Soc. 101 (2010), no. 1, 73–104. 11, 29

[BBL09] Julius Borcea, Petter Brand ¨ en, and Thomas Liggett, ´ Negative dependence and the geometry of polynomials. J. Amer. Math. Soc. 22 (2009), no. 2, 521–567. 5, 7, 11, 15, 17, 18, 31, 49, 55, 56

[Bra07] ¨ Petter Brand ¨ en, ´ Polynomials with the half-plane property and matroid theory. Adv. Math. 216 (2007), no. 1, 302–320. 3, 10, 21, 37, 56

[Bra10] ¨ Petter Brand ¨ en, ´ Discrete concavity and the half-plane property, Siam J. Discrete Math. 24 (2010), 921–933. 4, 36, 38, 41

[BH] Petter Brand ¨ en and June Huh, ´ Hodge–Riemann relations for Potts model partition functions. arXiv:1811.01696. 5, 50

[Bru06] Richard Brualdi, Combinatorial matrix classes. Encyclopedia of Mathematics and its Applications 108. Cambridge University Press, Cambridge, 2006. 40

[CRLMZ] Federico Castillo, Yairon Cid Ruiz, Binglin Li, Jonathan Montano, and Naizhen Zhang, ˜ When are multidegree positive? arXiv:2005.07808. 46

[COSW04] Youngbin Choe, James Oxley, Alan Sokal, and David Wagner, Homogeneous multivariate polynomials with th half-plane property. Adv. in Appl. Math. 32 (2004), no. 1-2, 88–187. 3, 7, 8, 21, 23, 29, 32

[DMS14] Claude Dellacherie, Servet Martinez, and Jaime San Martin, Inverse M-matrices and ultrametric matrices. Lecture Notes in Mathematics 2118. Springer, Cham, 2014. 51

[Dow80] Thomas Dowling, On the independent set numbers of a finite matroid. Combinatorics 79 (Proc. Colloq., Univ. Montral, Montreal, Que., 1979), Part I. Ann. Discrete Math.´ 8 (1980), 21–28. 49

[EH20] Christopher Eur and June Huh, Logarithmic concavityfor morphisms ofmatroids. Adv. in Math. 367 (2020), 107094. 50

[FM92] Tomas Feder and Milena Mihail, ´ Balanced matroids, Proceedings of the 24th Annual ACM Symposium on Theory of Computing, 26–38, ACM Press, 1992. 32

[FK72] Cornelius Fortuin and Pieter Kasteleyn, On the random-cluster model. I. Introduction and relation to other models. Physica 57 (1972), 536–564. 47

[Fuj05] Satoru Fujishige, Submodular functions and optimization. Second edition. Annals of Discrete Mathematics 58. Elsevier, Amsterdam, 2005. 9

[Ful93] William Fulton, Introduction to toric varieties. Annals of Mathematics Studies 131. The William H. Roever Lec tures in Geometry. Princeton University Press, Princeton, NJ, 1993. 47

[Ful98] William Fulton, Intersection theory. Second edition. Ergebnisse der Mathematik und ihrer Grenzgebiete 3, A Series of Modern Surveys in Mathematics 2. Springer-Verlag, Berlin, 1998. 45, 46

[GKL] Pavel Galashin, Steven N. Karp, and Thomas Lam, The totally nonnegative Grassmannian is a ball. arXiv:1707.02010. 23

[GKL19] Pavel Galashin, Steven N. Karp, and Thomas Lam, The totally nonnegative part of G{P is a ball. Adv. in Math. 351 (2019), 614–620. 23

[Gre81] Jirˇ´ı Gregor, On quadratic Hurwitzforms. I. Apl. Mat. 26 (1981), no. 2, 142–153. 8

[Gri06] Geoffrey Grimmett, The random-cluster model. Springer-Verlag, Berlin, 2006. 47

[GW04] Geoffrey Grimmett and Stephan Winkler, Negative association in uniform forests and connected graphs. Random Structures Algorithms 24 (2004), no. 4, 444–460. 5, 56

[Gur09] Leonid Gurvits, On multivariate Newton-like inequalities. Advances in combinatorial mathematics, 61–78, Springer, Berlin, 2009. 3, 23, 24, 47

[HS89] Yahya Ould Hamidoune and Isabelle Salaun,¨ On the independence numbers ofa matroid. J. Combin. Theory Ser. B 47 (1989), no. 2, 146–152. 49

[Har77] Robin Hartshorne, Algebraic geometry. Graduate Texts in Mathematics 52. Springer-Verlag, New York Heidelberg, 1977. 46

[Hei38] Rudolf Heine, Der Wertvorrat der gemischten Inhalte von zwei, drei und vier ebenen Eibereichen. Math. Ann. 115 (1938), no. 1, 115–129. 47

[HH03] Jurgen Herzog and Takayuki Hibi, ¨ Discrete polymatroids. J. Algebraic Combin. 16 (2002), no. 3, 239–268. 9

[Hol05] Olga Holtz, M-matrices satisfy Newton’s inequalities. Proc. Amer. Math. Soc. 133 (2005), no. 3, 711–717. 5, 51

[HJ94] Roger Horn and Charles Johnson, Topics in matrix analysis. Cambridge University Press, Cambridge, 1994. 52

[Huh18] June Huh, Combinatorial applications of the Hodge–Riemann relations. Proceedings of the International Congress of Mathematicians 3 (2018), 3079-3098. 15

[HK12] June Huh and Eric Katz, Log-concavity of characteristic polynomials and the Bergman fan of matroids. Math. Ann. 354 (2012), 1103–1116. 49

[HSW] June Huh, Benjamin Schroter and Botong Wang, ¨ Correlation bounds for fields and matroids. arXiv:1806.02675. 33, 49

[HW17] June Huh and Botong Wang, Enumeration ofpoints, lines, planes, etc. Acta Math. 218 (2017), no. 2, 297–317. 5, 32, 46

[HMMS] June Huh, Jacob P. Matherne, Karola Mesz´ aros, and Avery St. Dizier,´ Logarithmic concavity of Schur and related polynomials. arXiv:1906.09633. 23, 30

[JL] Chen Jiang and Zhiyuan Li, Algebraic reverse Khovanskii–Teissier inequality via Okounkov bodies. arXiv:2112.02847. 47

[Kah00] Jeff Kahn, A normal law for matchings. Combinatorica 20 (2000), no. 3, 339–391. 5, 56

[KN10] Jeff Kahn and Michael Neiman, Negative correlation and log-concavity. Random Structures Algorithms 37 (2010), no. 3, 367–388. 18, 49

[KN11] Jeff Kahn and Michael Neiman, A strong log-concavity propertyfor measures on Boolean algebras. J. Combin. Theory Ser. A 118 (2011), no. 6, 1749–1760. 49

[Kar68] Samuel Karlin, Total positivity. Vol. I. Stanford University Press, Stanford, 1968. 30

[KMT07] Yusuke Kobayashi, Kazuo Murota, and Ken’ichiro Tanaka, Operations on M-convex functions on jump systems. SIAM. J. Discrete Math. 21 (2007), no.1, 107–129. 10, 40

[Laz04] Robert Lazarsfeld, Positivity in algebraic geometry. I. Classical setting: line bundles and linear series. Ergebnisse der Mathematik und ihrer Grenzgebiete 3. A Series of Modern Surveys in Mathematics 48. Springer-Verlag, Berlin, 2004. 45, 46

[LX17] Brian Lehmann and Jian Xiao, Correspondences between convex geometry and complex geometry. Epijournal de<sup>´</sup> Geom´ etrie Alg´ ebrique´ 1 (2017), Article 6. 47

[Len13] Matthias Lenz, The f-vector of a representable-matroid complex is log-concave. Adv. in Appl. Math. 51 (2013), no. 5, 543–545. 49

[LS81] Elliott Lieb and Alan Sokal, A general Lee–Yang theorem for one-component and multicomponent ferromagnets. Comm. Math. Phys. 80 (1981), no. 2, 153–179. 10

[Lig97] Thomas Liggett, Ultra log-concave sequences and negative dependence. J. Comb. Th. A 79 (1997), 315–325. 24

[Lig10] Thomas Liggett, Continuous time Markov processes. An introduction. Graduate Studies in Mathematics 113. Amer ican Mathematical Society, Providence, RI, 2010. 31

[MS15] Diane Maclagan and Bernd Sturmfels, Introduction to tropical geometry. Graduate Studies in Mathematics 161. American Mathematical Society, Providence, RI, 2015. 37, 38, 39, 41, 42

[Mah85] Carolyn Mahoney, On the unimodality of the independent set numbers of a class of matroids. J. Combin. Theory Ser. B 39 (1985), no. 1, 77–85. 49

[Mar02] David Marker, Model theory: An introduction. Graduate Texts in Mathematics 217. Springer, New York, 2002. 35

[Mar72] Thomas Markham, Nonnegative matrices whose inverses are M-matrices. Proc. Amer. Math. Soc. 36 (1972), 326–330. 54

[Mas72] John Mason, Matroids: unimodal conjectures and Motzkin’s theorem. Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), 207–220, Inst. Math. Appl., Southend-on-Sea, 1972. 5, 49

[Men69] Korandattil Venugopalan Menon, On the convolution of logarithmically concave sequences. Proc. Amer. Math. Soc. 23 (1969), 439–441. 30

[Mur03] Kazuo Murota, Discrete convex analysis. SIAM Monographs on Discrete Mathematics and Applications. Society for Industrial and Applied Mathematics (SIAM), Philadelphia, 2003. 2, 4, 9, 18, 33, 34

[Nui68] Wim Nuij, A note on hyperbolic polynomials. Math. Scand. 23 (1968), 69–72. 7, 10, 13

[Oxl11] James Oxley, Matroid theory. Second edition. Oxford Graduate Texts in Mathematics 21. Oxford University Press, Oxford, 2011. 9, 48, 49

[Pem00] Robin Pemantle, Towards a theory of negative dependence. J. Math. Phys., 41, No. 3, (2000), 1371–1390. 55

[Pem12] Robin Pemantle, Hyperbolicity and stable polynomials in combinatorics and probability. Current developments in mathematics, 2011, 57–123, Int. Press, Somerville, MA, 2012. 7

[Pos09] Alexander Postnikov, Permutohedra, associahedra, and beyond. Int. Math. Res. Not. IMRN 2009, no. 6, 1026–1106. 9

[Sch14] Rolf Schneider, Convex bodies: the Brunn–Minkowski theory. Second expanded edition. Encyclopedia of Mathe matics and its Applications 151. Cambridge University Press, Cambridge, 2014. 43, 44

[Sch38] Isaac Jacob Schoenberg, Metric spaces and positive definite functions. Trans. Amer. Math. Soc. 44 (1938), 522–536. 38

[Ser10] Denis Serre, Matrices. Theory and applications. Graduate Texts in Mathematics 216. Springer, New York, 2010. 25

[Sey75] Paul Seymour, Matroids, hypergraphs, and the max-flow min-cut theorem. Thesis, University of Oxford, 1975. 49

[SW75] Paul Seymour and Dominic Welsh, Combinatorial applications of an inequality from statistical mechanics. Math. Proc. Cambridge Philos. Soc. 77 (1975), 485–495. 32, 49

[She60] Geoffrey Shephard, Inequalities between mixed volumes ofconvex sets. Mathematika 7 (1960), 125–138. 43, 47

[Shi12] Akiyoshi Shioura, Matroid rankfunctions and discrete concavity. Jpn. J. Ind. Appl. Math. 29 (2012), no. 3, 535–546. 34

[Sok05] Alan Sokal, The multivariate Tutte polynomial (alias Potts model) for graphs and matroids. Surveys in combinatorics 2005, 173–226, London Math. Soc. Lecture Note Ser. 327, Cambridge University Press, Cambridge, 2005. 47

[Spe05] David Speyer, Horn’s problem, Vinnikov curves and hives. Duke Math. J. 127 (2005), 395–428. 35, 36 [TV83] Aleksandr Timan and Igor Vestfrid, Any separable ultrametric space is isometrically embeddable in$\ell _ { 2 } .$Funktsional. Anal. i Prilozhen. 17 (1983), no. 1, 85–86. 38

[Wag05] David Wagner, Rank-three matroids are Rayleigh. Electron. J. Combin. 12 (2005), Note 8, 11 pp. 32

[Wag08] David Wagner, Negatively correlated random variables and Mason’s conjecture for independent sets in matroids. Ann. Comb. 12 (2008), no. 2, 211–239. 17, 49

[Wag11] David Wagner, Multivariate stable polynomials: theory and applications. Bull. Amer. Math. Soc. (N.S.) 48 (2011), no. 1, 53–84. 7, 11

[Wel76] Dominic Welsh, Matroid theory. London Mathematical Society Monographs 8. Academic Press, London-New York, 1976. 9

[Yau78] Shing Tung Yau, On the Ricci curvature of a compact K¨ahler manifold and the complex Monge–Amp\`ere equation. I. Comm. Pure Appl. Math. 31 (1978), no. 3, 339–411. 47

[Zha85] Cui Kui Zhao, A conjecture on matroids. Neimenggu Daxue Xuebao 16 (1985), no. 3, 321–326. 49

DEPARTMENT OF MATHEMATICS, KTH, ROYAL INSTITUTE OF TECHNOLOGY, STOCKHOLM, SWEDEN.

Email address: pbranden@kth.se

INSTITUTE FOR ADVANCED STUDY AND PRINCETON UNIVERSITY, PRINCETON, NJ, USA.

KOREA INSTITUTE FOR ADVANCED STUDY, SEOUL, KOREA.

Email address: junehuh@ias.edu