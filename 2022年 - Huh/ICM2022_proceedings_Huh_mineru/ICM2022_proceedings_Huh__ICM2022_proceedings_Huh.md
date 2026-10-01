# Combinatorics and Hodge theory

June Huh

## Abstract

I will tell two interrelated stories illustrating fruitful interactions between combinatorics and Hodge theory. The first is that of Lorentzian polynomials, based on my joint work with Petter Brändén. They link continuous convex analysis and discrete convex analysis via tropical geometry, and they reveal subtle information on graphs, convex bodies, projective varieties, Potts model partition functions, log-concave polynomials, and highest weight representations of general linear groups. The second is that of intersection cohomology of matroids, based on my joint work with Tom Braden, Jacob Matherne, Nick Proudfoot, and Botong Wang. It shows a surprising parallel between the theory of convex polytopes, Coxeter groups, and matroids. After giving an overview of the similarity, I will outline proofs of two combinatorial conjectures on matroids, the nonnegativity conjecture for their Kazhdan–Lusztig coefficients and the top-heavy conjecture for the lattice of flats.

Mathematics Subject Classification 2020

Primary 05E14; Secondary 05A20, 52B40

Keywords

Lorentzian polynomials, Hodge–Riemann relations, cohomology, matroid.

## 1. Introduction

One may seek unity in mathematics through the eyes of cohomology. Let$X$be a mathematical object of “dimension”$d$. The object may be analytic, arithmetic, geometric, or combinatorial, and the precise notion of dimension will depend on the context. Curiously, often it is possible to construct from$X$in a natural way a graded real vector space

$$
A (X) = \bigoplus_ {k = 0} ^ {d} A ^ {k} (X).
$$

The new object$A ( X )$, called the cohomology of$X$, often encodes essential information on$X$. When two objects$X$and$Y$of the same kind are related in a particular way, the relationship is often reflected on their cohomologies$A ( X )$and$A ( Y )$, and this property can be exploited to extend our understanding. Primary consumers of this viewpoint so far were topologists and geometers, and a great number of triumphs in topology and geometry are based on a construction of$A ( X )$from$X$. Interestingly, sometimes, satisfactory and equally useful cohomologies exist even when$X$does not have a geometric structure in the conventional sense. In particular, when$X$is a matroid, the study of$A ( X )$led to proofs of a few combinatorial conjectures that were beyond reach with traditional methods [1,6,12].

There are a few pieces of evidence for the unity in the above context. The list is short, but the pattern is remarkable. For example,$A ( X )$can be the ring of algebraic cycles modulo homological equivalence on a smooth projective variety [35], the combinatorial cohomology of a convex polytope [44], the Soergel bimodule of a Coxeter group element [26], the Chow ring of a matroid [1], the conormal Chow ring of a matroid [6], or the intersection cohomology of a matroid [12]. In these cases, the cohomology comes equipped with a symmetric bilinear pairing$P : A ^ { * } ( X ) \times A ^ { d - * } ( X ) \to \mathbb { R }$and a graded linear map$L : A ^ { * } ( X ) \to A ^ { * + 1 } ( X )$that are symmetric in the sense that

$$
P (x, y) = P (y, x) \text {   and   } P (x, L y) = P (L x, y) \text {   for   all   } x \text {   and   } y.
$$

The linear map$L$is allowed to vary in a family$K ( X )$, a convex cone in the space of linear operators on$A ( X )$. Here$P$is for Poincaré,$L$is for Lefschetz, and$K$is for Kähler, who first emphasized the importance of the respective objects in topology and geometry. In good cases,$A ^ { 0 } ( X )$has a distinguished generator 1, and one expects the following properties to hold for every nonnegative integer$\begin{array} { r } { k \leq \frac { d } { 2 } } \end{array}$

(1) The symmetric bilinear pairing

$$
A ^ {k} (X) \times A ^ {d - k} (X) \longrightarrow \mathbb {R}, \quad \left(x _ {1}, x _ {2}\right) \longmapsto P \left(x _ {1}, x _ {2}\right)
$$

is nondegenerate (Poincaré duality for$X$).

(2) For any$L _ { 1 } , \dots , L _ { d - 2 k } \in K ( X )$, the linear map

$$
A ^ {k} (X) \longrightarrow A ^ {d - k} (X), \qquad x \longmapsto \big (\prod_ {i = 1} ^ {d - 2 k} L _ {i} \big) x
$$

is an isomorphism (hard Lefschetz property for$X$).

(3) For any$L _ { 0 } , L _ { 1 } , \dots , L _ { d - 2 k } \in K ( X )$, the symmetric bilinear form

$$
A ^ {k} (X) \times A ^ {k} (X) \longrightarrow \mathbb {R}, \quad \left(x _ {1}, x _ {2}\right) \longmapsto (- 1) ^ {k} \mathrm{P} \left(x _ {1}, \left(\prod_ {i = 1} ^ {d - 2 k} L _ {i}\right) x _ {2}\right)
$$

is positive definite on the kernel of the linear map

$$
A ^ {k} (X) \longrightarrow A ^ {d - k + 1} (X), \qquad x \longmapsto \big (\prod_ {i = 0} ^ {d - 2 k} L _ {i} \big) x
$$

(Hodge–Riemann relations for$X$).

In the classical setting, $A ( X )$ is the cohomology of real$(p, q)$-forms on a compact Kähler manifold, and the three statements are consequences of Hodge theory [42, Chapter 3].1 All three statements are known to hold for$A ( X )$ listed above except the first one, which is the subject of Grothendieck’s standard conjectures on algebraic cycles [35]. In every case, the three statements for$A ( X )$ reveal a fundamental property of$X$: Weil conjectures on the number of solutions to a system of polynomial equations over finite fields when$X$is a smooth projective variety [35, 66], the generalized lower bound conjecture on the number of faces when$X$is a convex polytope [44,69], and Kazhdan–Lusztig’s nonnegativity conjecture when$X$is a Coxeter group element [26]. When$X$is a matroid, the hard Lefschetz property and the Hodge–Riemann relations for different choices of$A ( X )$ are used to settle Rota’s conjecture on the characteristic polynomial [1], Brylawski’s and Dawson’s conjectures on the ℎ-vectors of the broken circuit complex and the independence complex [6], and Dowling–Wilson’s top-heavy conjecture on the number of flats [12]. The known proofs of the Poincaré duality, the hard Lefschetz property, and the Hodge–Riemann relations for the objects listed above have certain structural similarities, but there is no known way of deducing one from the others. Could there be a Hodge-theoretic framework general enough to explain this miraculous coincidence?

A related goal is to produce a flexible analytic theory that would reflect certain basic features of the unified theory: If one postulates the existence of the satisfactory cohomology $A ( X )$, what can we say about$X$at an elementary and numerical level? This is a worthwhile question because, depending on$X$, the construction and the study of$A ( X )$ might be beyond the reach of our current understanding. A step in this direction is taken in a joint work with Petter Brändén on Lorentzian polynomials [17], where the difficult goal of finding$A ( X )$is replaced by an easier goal of producing a Lorentzian polynomial from$X$. Such a Lorentzian polynomial can be used to settle and generate conjectures on various$X$ (Section 2) and, sometimes, leads to a satisfactory theory of$A ( X )$ (Section 3).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1In [12, 26, 35, 42, 44], the hard Lefschetz property and the Hodge–Riemann relations are considered only in the “unmixed” case where$L = L _ { i }$for all$i$. According to [18], this special case implies the general case stated above.</span></small>

## 2. Lorentzian polynomials

Lorentzian polynomials link continuous convex analysis and discrete convex analysis via tropical geometry, and they reveal subtle information on graphs, convex bodies, projective varieties, Potts model partition functions, log-concave polynomials, and highest weight representations of general linear groups. Let$H _ { n } ^ { d }$be the space of degree$d$homogeneous polynomials in$n$variables with real coefficients. The members of$H _ { n } ^ { d }$will be written

$$
f = \sum_ {\alpha} c _ {\alpha} \frac {w ^ {\alpha}}{\alpha !},
$$

where the sum is over the nonnegative integral vectors$\alpha \in \mathbb { Z } _ { \geq 0 } ^ { n }$with$| \alpha | _ { 1 } = d$and

$$
\frac {w ^ {\alpha}}{\alpha !} := \frac {w _ {1} ^ {\alpha_ {1}}}{\alpha_ {1} !} \frac {w _ {2} ^ {\alpha_ {2}}}{\alpha_ {2} !} \dots \frac {w _ {n} ^ {\alpha_ {n}}}{\alpha_ {n} !}.
$$

Note that a polynomial$f$can be viewed as a function in at least two different ways. The continuous$f$is the function given by the evaluation

$$
f: \mathbb {R} _ {\geq 0} ^ {n} \longrightarrow \mathbb {R}, \quad w \longmapsto f (w),
$$

and the discrete$f$is the function given by the coefficients

$$
f: \mathbb {Z} _ {\geq 0} ^ {n} \longrightarrow \mathbb {R}, \quad \alpha \longmapsto c _ {\alpha}.
$$

Throughout we write supp($f$) for the support of the discrete$f$, the set of monomials appearing in$f$with nonzero coefficients. The theory of Lorentzian polynomials shows that the log-concavity of the continuous$f$is related to the log-concavity of the discrete$f$in an interesting way. Before defining Lorentzian polynomials in Definition 4, we list three applications of the theory to demonstrate the usefulness and ubiquity of Lorentzian polynomials. Each item below presents an elementary statement that is dificult to prove without the Lorentzian point of view.

Example 1 (Analysis). Let$f$be a homogeneous polynomial of degree$d$in$n$variables with nonnegative coefficients. Such a polynomial$f$is said to be strongly log-concave if, for al $\alpha \in \mathbb { Z } _ { \geq 0 } ^ { n }$, we have

$\partial ^ { \alpha } f$is identically zero or log$( \partial ^ { \alpha } f )$is concave on the positive orthant$\mathbb { R } _ { > 0 } ^ { n } .$

For bivariate polynomials, one can show that$\begin{array} { r } { f = \sum _ { k = 0 } ^ { d } c _ { k } w _ { 1 } ^ { k } w _ { 2 } ^ { d - k } } \end{array}$is strongly log-concave exactly when the sequence$\left\{ c _ { k } \right\}$has no internal zeros and is ultra log-concave:

$$
\frac {c _ {k} ^ {2}}{\binom {d} {k} ^ {2}} \geq \frac {c _ {k - 1}}{\binom {d} {k - 1}} \frac {c _ {k + 1}}{\binom {d} {k + 1}} \text {   for   all   } 0 <   k <   d.
$$

In [17, Corollary 2.32], the theory of Lorentzian polynomials is used to prove the following statement:

The product of strongly log-concave homogeneous polynomials is strongly log-concave.

This answers a question of Gurvits [36, Section 4.5] for homogeneous polynomials, and extends the following theorem of Liggett [49, Theorem 2]:

The convolution product of two ultra log-concave sequences with no internal zeros is an ultra log-concave sequence with no internal zeros.

The short proof in [17] is based on the following analytic characterization of Lorentzian polynomials [17, Theorem 2.30]:

A homogeneous polynomial with nonnegative coefficients is Lorentzian if and only if it is strongly log-concave.

It is interesting to compare the argument with the computational proof in [49] for bivariate polynomials.

Example 2 (Combinatorics). Let$\mathcal { A }$be a set of$n$vectors in a vector space. For any$k$, set

$f _ { k } ( \mathcal { A } ) :=$ the number of$k$element linearly independent subsets of$\mathcal { A }$.

For example, if$\mathcal { A }$ is the set of all seven nonzero vectors in a three-dimensional vector space over the field with two elements, then there are seven dependencies among the triples shown below, and hence

![](images/page_4_image_8.jpg)

$$
f _ {0} (\mathcal {A}) = 1, \quad f _ {1} (\mathcal {A}) = 7, \quad f _ {2} (\mathcal {A}) = 21, \quad f _ {3} (\mathcal {A}) = 28.
$$

Mason’s conjecture from [51] predicts that, for any$\mathcal { A }$ and any positive integer$k$,

$$
\frac {f _ {k} (\mathcal {A}) ^ {2}}{\binom {n} {k} ^ {2}} \geq \frac {f _ {k - 1} (\mathcal {A})}{\binom {n} {k - 1}} \frac {f _ {k + 1} (\mathcal {A})}{\binom {n} {k + 1}}.
$$

The same statement was conjectured more generally for all matroids (Definition 9), and the general statement is proved in [17, Theorem 4.14] using the theory of Lorentzian polynomials.2 The proof is based on the Lorentzian property of the Potts model partition function for matroids introduced in [67].

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant have independently developed methods that partly overlap with [17] in a series of papers [2–4]. They study the class of completely log-concave polynomials, which agrees with the class of Lorentzian polynomials in the homogeneous case. The main overlap is an independent proof of Mason’s conjecture in [4].</span></small>

Example 3 (Algebra). Schur polynomials are the characters of finite-dimensional irreducible polynomial representations of the general linear group${ \mathrm { G L } } _ { n } ( \mathbb { C } )$. Combinatorially, the Schur polynomial of a partition$\lambda$ in$n$variables is

$$
s _ {\lambda} (w _ {1}, \ldots , w _ {n}) = \sum_ {\alpha} K _ {\lambda \alpha} w ^ {\alpha},
$$

where$K _ { \lambda \alpha }$is the Kostka number counting Young tableaux of given shape$\lambda$ and weight$\alpha$. Correspondingly, the irreducible representation$V ( \lambda )$of the general linear group with the highest weight$\lambda$ has the weight space decomposition

$$
V (\lambda) = \bigoplus_ {\alpha} V (\lambda) _ {\alpha} \mathrm{with} \dim V (\lambda) _ {\alpha} = K _ {\lambda \alpha}.
$$

Schur polynomials were first studied by Cauchy, who defined them as ratios of alternants. The connection to the representation theory of${ \mathrm { G L } } _ { n } ( \mathbb { C } )$was found by Schur. For a gentle introduction to these remarkable polynomials, and for any undefined terms, we refer to [30].

In [39, Theorem 2], the authors use the Lorentzian property for normalized Schur polynomials to show that the sequence of weight multiplicities of$\mathrm { V } ( \lambda )$one encounters is always log-concave if one walks in the weight diagram along any root direction$e _ { i } - e _ { j }$. In other words, for any$\alpha \in \mathbb { Z } _ { \geq 0 } ^ { n }$and any$i , j \in [ n ]$

$$
K _ {\lambda \alpha} ^ {2} \geq K _ {\lambda \alpha - e _ {i} + e _ {j}} K _ {\lambda \alpha + e _ {i} - e _ {j}}.
$$

This verifies a special case of Okounkov’s conjecture from [60, Conjecture 1].3

We now define Lorentzian polynomials. As before, we write$H _ { n } ^ { d }$for the space of degree$d$homogeneous polynomials in$n$variables with real coefficients. Let$\mathring { L } _ { n } ^ { 2 } \subseteq H _ { n } ^ { 2 }$be the open subset of quadratic forms with positive coefficients that have the Lorentzian signature $( + , - , \ldots , - )$. For$d$ larger than 2, we define an open subset$\mathring { L } _ { n } ^ { d } \subseteq H _ { n } ^ { d }$by setting

$$
\mathring {L} _ {n} ^ {d} = \left\{f \in H _ {n} ^ {d} \mid \partial_ {i} f \in \mathring {L} _ {n} ^ {d - 1} \text {for all} i \in [ n ] \right\},
$$

where$\partial _ { i }$is the partial derivative with respect to the$i$-th variable. Thus$f$belongs to${ \mathring { L } } _ { n } ^ { d }$if and only if all quadratic polynomials of the form$\partial _ { i _ { 1 } } \partial _ { i _ { 2 } } \dots \partial _ { i _ { d - 2 } } f$belongs to${ \mathring { L } } _ { n } ^ { 2 }$

Definition 4 (Lorentzian polynomials). The polynomials in${ \mathring { L } } _ { n } ^ { d }$are called strictly Lorentzian, and the limits of strictly Lorentzian polynomials are called Lorentzian.

The prototypical examples of Lorentzian polynomials, which motivated Definition 4, are the ones obtained from the various examples of$A ( X )$in Section 1 in the following way. For any linear operators$L _ { 1 } , \ldots , L _ { d }$on$A ( X )$, we set

$$
\deg \Big (\prod_ {i = 1} ^ {d} L _ {i} \Big) := P \Big (1, \prod_ {i = 1} ^ {d} L _ {i} \cdot 1 \Big),
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3The general conjecture is that the discrete function$(\nu , \kappa , \lambda) \mapsto \log c _ { \kappa \lambda } ^ { \nu }$is concave, where$c _ { \kappa \lambda } ^ { \nu }$are the Littlewood–Richardson coefficients [60, Conjecture 1]. The conjecture holds in the “classical limit” [60, Section 3], but the general case is refuted in [19].</span></small>

where 1 is the distinguished generator of$A ^ { 0 } ( X )$defining$P ( 1 , - ) : A ^ { d } ( X ) \simeq \mathbb { R }$

Proposition 5. Let$L _ { 1 } , \ldots , L _ { n }$be members of the closure${ \overline { { K } } } ( X )$, and let$f$ the polynomial

$$
f (w _ {1}, \dots , w _ {n}) = \frac {1}{d !} \deg (w _ {1} L _ {1} + \dots + w _ {n} L _ {n}) ^ {d}.
$$

If$A ( X )$satisfies the Hodge–Riemann relations in degrees$\leq 1$, then$f$is Lorentzian.

Before deducing Proposition 5 from Theorem 12 below, we give two prominent cases.

Example 6 (Volume polynomials of convex bodies). For any collection of convex bodies $C = ( C _ { 1 } , \ldots , C _ { n } )$in$\mathbb { R } ^ { d }$, consider the function

$$
\operatorname{vol} _ {C}: \mathbb {R} _ {\geq 0} ^ {n} \longrightarrow \mathbb {R}, \quad w \longmapsto \frac {1}{d !} \operatorname{vol} (w _ {1} C _ {1} + \dots + w _ {n} C _ {n}),
$$

where$w _ { 1 } C _ { 1 } + \cdot \cdot \cdot + w _ { n } C _ { n }$is the Minkowski sum and vol is the Euclidean volume. Minkowski showed that${ \mathrm { v o l } } _ { C } ( w )$is a polynomial [65, Chapter 5]. One may approximate the convex bodies with convex polytopes to prove that vol is Lorentzian. Using Proposition 5, where$C$is the Minkowski sum of the approximating convex polytopes and$A ( X )$is the combinatorial cohomology in [44], we get the following statement:

The polynomial vol$_ { C } ( w )$ is Lorentzian for any convex bodies$C _ { 1 } , \ldots , C _ { n }$ in$\mathbb { R } ^ { d }$.

Alternatively, one can use Brunn–Minkowski theory to deduce the Lorentzian property of the volume polynomial [17, Section 4.1].

Example 7 (Volume polynomials of projective varieties). Let$X$be a$d$-dimensional irreducible projective variety over an algebraically closed field. A Cartier divisor on$X$is said to be nef if it intersects every irreducible curve in$X$ nonnegatively.4 For any collection of nef divisors$H = \left( H _ { 1 } , \ldots , H _ { n } \right)$ on$X$, consider the function

$$
\operatorname{vol} _ {H}: \mathbb {R} _ {\geq 0} ^ {n} \longrightarrow \mathbb {R}, \quad w \longmapsto \frac {1}{d !} \deg (w _ {1} H _ {1} + \dots + w _ {n} H _ {n}) ^ {d},
$$

where deg is the degree map on the Chow group of 0-dimensional cycles on$X$. When$X$admits a resolution of singularities$Y$, one can deduce the following statement from Proposition 5 and the Hodge–Riemann relations in degree$\leq 1$for the ring of algebraic cycles$A ( Y )$:

The polynomial vol$_ { H } ( w )$ is Lorentzian for any nef divisors$H _ { 1 } , \ldots , H _ { n }$ on$X$.

In general, one can use Bertini’s theorem to reduce the statement to the case of surfaces and apply Hodge’s index theorem [17, Section 4.2].

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4By Kleiman’s theorem [46, Section 1.4], any nef divisor on a projective variety is a limit of ample R-divisors, which form the convex cone in this setting</span></small>

Next we formulate the main structural results on Lorentzian polynomials. A central definition is that of generalized permutohedra. Let$E$be a finite set, and let$\{ e _ { i } \} _ { i \in E }$be the standard basis of$\mathbb { R } ^ { E }$.

Definition 8. A generalized permutohedron is a polytope in$\mathbb { R } ^ { E }$all of whose edges are in the direction$e _ { i } - e _ { j }$for some$i$and$j$in$E$.

For example, the standard permutohedron in$\mathbb { R } ^ { n }$, which is the convex hull of all permutations of$( 1 , 2 , \ldots , n )$, and the hyperoctahedron in$\mathbb { R } ^ { n }$, which is the convex hull of all permutations of$( \pm 1 , 0 , \dots , 0 )$, are generalized permutohedra. The following pictures show the two polytopes in$\mathbb { R } ^ { 4 }$:

![](images/page_7_image_3.jpg)

Generalized permutohedra are precisely the translates of the base polytopes ofpolymatroids [24], and they are obtained from the standard permutohedron by moving the vertices so that all the edge directions are preserved [62]. They lead to the central notion of M-convexity in the study of discrete convex analysis [58].

Definition 9. A subset$J \subseteq \mathbb { Z } _ { \geq 0 } ^ { E }$is M-convex if it is the set of all lattice points of an integral generalized permutohedron. A matroid on$E$is an M-convex subset of$\mathbb { Z } _ { \geq 0 } ^ { E }$consisting of zero-one vectors. The vectors in a matroid$\mathbf { M }$are called bases of$\mathbf { M }$.

A subset$J \subseteq \mathbb { Z } _ { \geq 0 } ^ { E }$is M-convex exactly when it satisfies the symmetric basis exchange property [24, 38]: For any$\alpha$,$\beta \in J$ and an index$i$satisfying$\alpha _ { i } > \beta _ { i }$, there is an index$j$ that satisfies

$$
\alpha_ {j} <   \beta_ {j} \text { and } \alpha - e _ {i} + e _ {j} \in J \text { and } \beta - e _ {j} + e _ {i} \in J.
$$

In [58, Chapter 4], one can find several other equivalent characterizations of M-convexity. The above definition of matroids goes back to the study of moment map images of torus orbits in Grassmannians by Gelfand, Goresky, MacPherson, and Serganova in [32]. For a general introduction to matroids, and for any undefined matroid terms, we refer to [61]. Hereafter we identify the subsets of$E$with the zero-one vectors in$\mathbb { Z } _ { \geq 0 } ^ { E }$

Example 10 (Graphic matroids). For any finite connected graph$G$with the edge set$E$, consider the set of indicator vectors

$$
\mathscr {B} (G) := \left\{e _ {B} \mid B \text {   is   a   spanning   tree   of   } G \right\} \subseteq \mathbb {Z} _ {\geq 0} ^ {E}.
$$

The subset${ \mathcal { B } } ( G )$is M-convex for any$G$. Such matroids are said to be graphic.

Example 11 (Representable matroids). For any function$\varphi : E \to W$from a finite set$E$to a vector space$W$over a field F, consider the set of indicator vectors

$$
\mathscr {B} (\varphi) := \left\{e _ {B} \mid \varphi (B) \text {   is   a   bases   of   } W \right\} \subseteq \mathbb {Z} _ {\geq 0} ^ {E}.
$$

The subset$\mathcal { B } ( \boldsymbol { \varphi } )$is M-convex for any$\varphi : E \to W$. Such matroids are said to be representable over F, and the function$\varphi$is called a representation over F. One typically requires without loss of generality that the image of$\varphi$spans$W$. A graphic matroid is representable over every field [61, Section 5.1]. In general, a matroid may or may not have a representation over F:

![](images/page_8_image_1.jpg)

Among the three matroids pictured above, where the bases are given by all triples of points not on a line, the first is representable over F if and only if the characteristic of F is 2, the second is representable over F if and only if the characteristic of F is not 2, and the third is not representable over any field.

Let$L _ { n } ^ { 2 } \subseteq H _ { n } ^ { 2 }$be the closed subset of quadratic forms with nonnegative coefficients that have at most one positive eigenvalue. For$d$ larger than 2, we define$L _ { n } ^ { d } \subseteq H _ { n } ^ { d }$by setting

$$
L _ {n} ^ {d} = \left\{f \in \mathrm{M} _ {n} ^ {d} \mid \partial_ {i} f \in L _ {n} ^ {d - 1} \text {   for   all   } i \right\},
$$

where$\mathbf { M } _ { n } ^ { d } \subseteq H _ { n } ^ { d }$is the set of polynomials with nonnegative coefficients whose supports are M-convex. The following characterization in [17, Theorem 2.25] is central to the theory of Lorentzian polynomials.

Theorem 12.$L _ { n } ^ { d }$is the set of Lorentzian polynomials in$H _ { n } ^ { d }$

In other words,$L _ { n } ^ { d }$is the closure of${ \mathring { L } } _ { n } ^ { d }$in$H _ { n } ^ { d }$. Theorem 12 makes itpossible to decide whether a given polynomial is Lorentzian or not. For example, the following polynomials ar not Lorentzian because their supports are not M-convex:

$$
w _ {1} ^ {3} + w _ {2} ^ {3}, \quad w _ {1} w _ {2} ^ {2} + w _ {1} w _ {3} ^ {2} + w _ {2} w _ {3} ^ {2} + w _ {1} w _ {2} w _ {3}, \quad w _ {1} ^ {2} w _ {3} + w _ {2} ^ {3}.
$$

One can also use Theorem 12 to show that a given polynomial is Lorentzian. For example, the elementary symmetric polynomial of degree$d$in$n$variables is Lorentzian because its support is M-convex and all its associated quadratic forms are

$$
\left( \begin{array}{c c c c c} 0 & 1 & 1 & \dots & 1 \\ 1 & 0 & 1 & \dots & 1 \\ 1 & 1 & 0 & \dots & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 1 & 1 & \dots & 0 \end{array} \right),
$$

which have exactly one positive eigenvalue$n - d + 1$. One can also use Theorem 12 and the relevant Hodge–Riemann relations to show that the volume polynomials in Example 6 and Example 7 are Lorentzian. In particular, the supports of these volume polynomials must be M-convex for any collection of convex bodies and any collection of nef divisors.

ProofofProposition 5. We may suppose that$L _ { 1 } , \ldots , L _ { n }$are members of$K ( X )$. Under this assumption, all the coefficients of$f$are positive by the Hodge–Riemann relations in degree 0, so the support of$f$is M-convex. Choose any$d - 2$among the linear operators, say $L _ { 1 } , \dots , L _ { d - 2 }$, and observe that

$$
\partial_ {1} \dots \partial_ {d - 2} f (w _ {1}, \dots , w _ {n}) = \deg L _ {1} \dots L _ {d - 2} (w _ {1} L _ {1} + \dots + w _ {n} L _ {n}) ^ {2}.
$$

Thus, by Theorem 12, it is enough to observe that the symmetric bilinear pairing

$$
B ^ {1} (X) \times B ^ {1} (X) \longrightarrow \mathbb {R}, \quad \left(x _ {1}, x _ {2}\right) \longmapsto P \left(x _ {1}, L _ {1} \dots L _ {d - 2} \cdot x _ {2}\right)
$$

has the Lorentzian signature, where$B ^ { 1 } ( X )$is the span of$L _ { 1 } \cdot 1 , \ldots , L _ { n } \cdot 1$in$A ^ { 1 } ( X )$. This follows from the Hodge–Riemann relations in degrees$\leq 1 \colon$: For any$L$ in$K ( X )$, the pairing is positive on$L \cdot 1$by the Hodge–Riemann relations in degree 0, and it is negative definite on the orthogonal complement of$L \cdot 1$by the Hodge–Riemann relations in degree 1.

Example 13. Not all Lorentzian polynomials are volume polynomials of convex bodies. In fact, the basis generating polynomial of a matroid on [$n$] is the volume polynomial of$n$
convex bodies precisely when the matroid is representable over every field [17, Remark 4.3]. For example, the elementary symmetric polynomial

$$
w _ {1} w _ {2} + w _ {1} w _ {3} + w _ {1} w _ {4} + w _ {2} w _ {3} + w _ {2} w _ {4} + w _ {3} w _ {4}
$$

is not the volume polynomial of four convex bodies in$\mathbb { R } ^ { 2 }$because its support is not representable over the field$\mathbb { F } _ { 2 }$

Example 14. Not all Lorentzian polynomials are volume polynomials of nef divisors on a projective variety. For example, consider the cubic polynomial

$$
f = 14 w _ {1} ^ {3} + 6 w _ {1} ^ {2} w _ {2} + 24 w _ {1} ^ {2} w _ {3} + 12 w _ {1} w _ {2} w _ {3} + 3 w _ {2} w _ {3} ^ {2}.
$$

One can use Theorem 12 to check that$f$is Lorentzian. To see that$f$is not the volume polynomial of nef divisors, one can use the reverse Khovanskii–Teissier inequality [48, Theorem 5.7]: For any nef divisor$L _ { 1 } , L _ { 2 } , L _ { 3 }$on a$d$-dimensional projective variety and any$k \leq d$,

$$
\binom {d} {k} \left(L _ {2} ^ {k} \cdot L _ {1} ^ {d - k}\right) \left(L _ {1} ^ {k} \cdot L _ {3} ^ {d - k}\right) \geq \left(L _ {1} ^ {d}\right) \left(L _ {2} ^ {k} \cdot L _ {3} ^ {d - k}\right).
$$

The complex analytic proof of the inequality in [48] relies on the Calabi–Yau theorem [73]. The algebraic proof of the inequality in [43] using Okounkov bodies works over any algebraically closed field.

The space of Lorentzian polynomials has numerous surprising properties. For example, writing$\mathbb { P } L _ { n } ^ { d }$ for the image of$L \backslash 0 \subseteq H _ { n } ^ { d }$in the real projective space$\mathbb { P } H _ { n } ^ { d }$, one can show that

P$L _ { n } ^ { d }$is compact contractible subset with contractible interior P${ \mathring { L } } _ { n } ^ { d } .$

The contractibility follows from the following semigroup action [17, Theorem 2.10]:

Any nonnegative linear change of coordinates preserves$L _ { n } ^ { d } .$. More generally, when $f ( w ) \in L _ { n } ^ { d } ,$, then$f ( A v ) \in L _ { m } ^ { d } f o r$any$n \times m$matrix$A$with nonnegative entries

In fact, Brändén showed in [16] that$\mathbb { P } L _ { n } ^ { d }$is homeomorphic to a closed Euclidean ball, verifying a conjecture posed in [17, Conjecture 2.29]. The main feature of this Lorentzian ball is the following stratification labelled by M-convex sets [17, Theorem 3.10 and Proposition 3.25]:

The set$L _ { J }$ of Lorentzian polynomials with support$J$is nonempty if and only if$J$is M-convex. In this case,$\mathbb { P } L _ { J }$deformation retracts to the exponential generating function$\textstyle \sum _ { \alpha \in J } { \frac { 1 } { \alpha ! } } w ^ { \alpha }$

This supports the opinion that matroid theory provides the correct level of generality. Leaving out any one matroid, say not representable over any field, will make the Lorentzian ball noncompact.5

The connection between discrete convex analysis and Lorentzian polynomials can be strengthened as follows. For a function$\nu : \mathbb { Z } _ { \geq 0 } ^ { n } \to \mathbb { R } \cup \{ \infty \}$, we write dom$( \nu ) \subseteq \mathbb { Z } _ { \geq 0 } ^ { n }$for the subset on which$\nu$is finite, called the effective domain of$\nu$. For a positive real parameter$t$, consider the exponential generating function

$$
f _ {q} ^ {\nu} (w) = \sum_ {\alpha \in \mathrm{dom} (\nu)} \frac {q ^ {\nu (\alpha)}}{\alpha !} w ^ {\alpha}.
$$

By [17, Theorem 3.14], the polynomial$f _ { q } ^ { \nu }$is Lorentzian for all sufficiently small$q$if and only if the function$\nu$is M-convex in the sense of discrete convex analysis [58]: For any index$i$ and any$\alpha$,$\beta \in \mathrm { d o m } ( \nu )$whose$i$-th coordinates satisfy$\alpha _ { i } > \beta _ { i }$, there is an index$j$ satisfying

$$
\alpha_ {j} <   \beta_ {j} \text { and } \nu (\alpha) + \nu (\beta) \geq \nu (\alpha - e _ {i} + e _ {j}) + \nu (\beta - e _ {j} + e _ {i}).
$$

Considering the special case when$\nu$takes values in {0, ∞}, we see that$J$is an M-convex set if and only if its exponential generating function$\textstyle \sum _ { \alpha \in J } { \frac { 1 } { \alpha ! } } w ^ { \alpha }$is a Lorentzian polynomial [17, Theorem 3.10]. Another corollary is that a homogeneous polynomial with nonnegative coefficients is Lorentzian if the natural logarithms of its normalized coefficients form an M concave function [17, Corollary 3.16]. Working over the field of real Puiseux series K, we see that the tropicalization of any Lorentzian polynomial over K is an M-convex function, and that all M-convex functions are limits of tropicalizations of Lorentzian polynomials over K [17, Corollary 3.28]. This generalizes a result of Brändén [15], who showed that the tropicalization of any homogeneous stable polynomial over K is M-convex. In particular, for any matroid M with the set of bases ℬ, the Dressian of all valuated matroids on M can be identified with the tropicalization of the space of Lorentzian polynomials over K with support ℬ. For example, the tropicalization of the space of multiaffine Lorentzian quadrics in five variables is the tropical Grassmannian trop Gr(2, 5), a cone ove the Petersen graph in R${ . ^ { 10 } / \mathbb { R } \mathbf { 1 } }$:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">5Almost all matroids are not representable over any field. More precisely, the portion of matroids in$\mathbb { Z } _ { \geq 0 } ^ { n }$ that are representable over some field goes to zero as$n$goes to infinity [59]. For logical discussions of the “missing axiom” of matroid theory, see [52, 53, 72].</span></small>

![](images/page_11_image_1.jpg)

The figure shows a shadow of the Lorentzian ball$\mathbb { P } L _ { 5 } ^ { 2 }$over$\mathbb { K }$, highlighting its non-convexity. We refer to [50, Chapter 4] for a friendly introduction to Dressians and tropical Grassmannians.

The theory of Lorentzian polynomials is not only useful for proving conjectures but also for generating them. Once one has identified a combinatorial polynomial$f$that is either provably or conjecturally Lorentzian, it is natural to look for an algebraic object$A ( X )$ satisfying the Hodge–Riemann relations that explains the Lorentzian property of$f$. In good cases, one can further speculate that there is a projective variety$X$ that produces$f$as a volume polynomial for some choices of nef divisors on$X$

One such speculation concerns the basis generating polynomial for a morphism of matroids. Let M and N be matroids on finite sets$E$and$F$. The rank function of M is the function defined by

$$
\operatorname{rk} _ {\mathrm{M}}: 2 ^ {E} \longrightarrow \mathbb {Z}, \qquad \operatorname{rk} _ {\mathrm{M}} (S) = \max _ {B \in \mathcal {B}} | B \cap S |,
$$

where the maximum is taken over the set of bases of M. A morphism$g : { \bf M } \to { \bf N }$is a function$E \to F$that satisfies the rank inequalities

$$
\operatorname{rk} _ {\mathrm{N}} (g (S _ {2})) - \operatorname{rk} _ {\mathrm{N}} (g (S _ {1})) \leq \operatorname{rk} _ {\mathrm{M}} (S _ {2}) - \operatorname{rk} _ {\mathrm{M}} (S _ {1}) \text {   for   any   } S _ {1} \subseteq S _ {2} \subseteq E.
$$

A function between the ground sets is a morphism if and only if the preimage of a flat is a flat (Definition 22). A subset$S \subseteq E$is a basis of$g$ if$S$is contained in a basis of M and$g ( S )$ contains a basis of N. For a general discussion of morphisms of matroids, we refer to [45].

In [27, Corollary 4.6], the authors show that the homogenous basis generating polyno mial

$$
f _ {g} (w _ {0}, w _ {i}) _ {i \in E} := \sum_ {S \in \mathcal {B} (g)} w _ {0} ^ {| E | - | S |} \prod_ {i \in S} w _ {i}
$$

is Lorentzian for any morphism of matroids$\varphi : \mathbf { M } \to \mathbf { N }$, where$\mathcal { B } ( g )$is the set of bases of $g .$. When N is the rank zero matroid on one element, one recovers the Lorentzian property of the homogenous independent set generating polynomial of M in [17, Section 4.3]. Setting the variables$( w _ { i } ) _ { i \in E }$equal to each other, we get a bivariate Lorentzian polynomial witnessing the validity of Mason’s conjecture in Example 2. When$g$is the identity morphism, one recovers the Lorentzian property of the basis generating polynomial of a matroid [17, Section 3.2].

Example 15 (Continued from Example 10). A homomorphism from a graph$G _ { 1 }$to a graph $G _ { 2 }$is a function from the vertex set of$G _ { 1 }$to the vertex set of$G _ { 2 }$that maps adjacent vertices to adjacent vertices. The induced map from the edge set of$G _ { 1 }$to the edge set of$G _ { 2 }$is a morphism from the graphic matroid$\mathcal { B } ( G _ { 1 } )$to the graphic matroid$\mathcal { B } ( G _ { 2 } )$. Such morphisms of matroids are said to be graphic.

![](images/page_12_image_1.jpg)

The graphic morphism of matroids depicted above has 27 bases of cardinality two, 79 bases of cardinality three, 111 bases of cardinality four, and 75 bases of cardinality five.

Example 16 (Continued from Example 11). Let$\mathbf { M } _ { i }$be matroids on$E _ { i }$with representations $\varphi _ { i } : E _ { i } \to W _ { i }$over a field F. A function$g$from$E _ { 1 }$to$E _ { 2 }$is a morphism from$\mathbf { M } _ { 1 }$to${ { \bf { M } } _ { 2 } }$if it fits into a commutative diagram

$$
\begin{array}{c} E _ {1} \xrightarrow {\varphi_ {1}} W _ {1} \\ \Biggl \downarrow \\ E _ {2} \xrightarrow {\varphi_ {2}} W _ {2}, \end{array}
$$

where$W _ { 1 } \to W _ { 2 }$is a linear map between the vector spaces. Such morphisms of matroids are said to be representable over F. A graphic morphism of matroids is representable over every field.

Continuing Example 7, we say that a degree$d$ Lorentzian polynomial$f$in variables$w _ { 1 } , \ldots , w _ { n }$is a volume polynomial over F if there are nef divisors$H _ { 1 } , \ldots , H _ { n }$on a$d$-dimensional irreducible projective variety$X$ over$\mathbb { F }$that satisfy

$$
f = \frac {1}{d !} \deg (w _ {1} H _ {1} + \dots + w _ {n} H _ {n}) ^ {d}.
$$

The following existence conjecture was made in [27, Conjecture 5.6]. It strengthens the Lorentzian property of the homogeneous basis generating polynomial of$g$ when$g$is representable over F.

Conjecture 17. If$g$is a morphism of matroids that is representable over F, then the homogenous basis generating polynomial of$g$ is a volume polynomial over F.

Let M be a matroid on$E$ that is representable over F. In [5], the authors construct a collection of nef divisors$( L _ { i } ) _ { i \in E }$on an irreducible projective variety$X$ over F such that

$$
\sum_ {B \in \mathcal {B}} \prod_ {i \in B} w _ {i} = \frac {1}{d !} \deg \left(\sum_ {i \in E} w _ {i} L _ {i}\right) ^ {\dim X},
$$

where the first sum is over the set of bases$\mathcal { B }$of M. This verifies Conjecture 17 when$g$is the identity morphism. A detailed study of this$X$and its resolution of singularities in [40], in turn, was used to define the matroid intersection cohomology in [12]. It plays a central role in the resolution of two combinatorial conjectures on matroids, the top-heavy conjecture for the lattice of flats and the nonnegativity conjecture for the Kazhdan–Lusztig coefficients. We outline their proofs in Section 3.

Another speculation on Lorentzian polynomials is based on the Lorentzian property of the normalized Schur polynomial

$$
\mathrm{N} (s _ {\lambda} (w _ {1}, \ldots , w _ {n})) = \sum_ {\alpha} K _ {\lambda \alpha} \frac {w ^ {\alpha}}{\alpha !}.
$$

Here, as in Example 3,$\lambda$is a partition and$K _ { \lambda \alpha }$are the Kostka coefficients.

Definition 18. The normalization operator is the linear operator N defined on the space of Laurent generating functions defined by

$$
\mathrm{N} \left(\sum_ {\alpha \in \mathbb {Z} ^ {n}} c _ {\alpha} w ^ {\alpha}\right) = \sum_ {\alpha \in \mathbb {Z} _ {\geq 0} ^ {n}} c _ {\alpha} \frac {w ^ {\alpha}}{\alpha !}.
$$

For example, we have$\begin{array} { r } { \mathrm { N } \big ( \frac { 1 } { z ( 1 - z ) } \big ) = e ^ { z } } \end{array}$

In [17, Proposition 4.4], it was observed that the Alexandrov–Fenchel inequality for volume polynomials of convex bodies holds more generally for any Lorentzian polynomial in$n$variables:

$$
\text {   If   } \sum_ {\alpha} c _ {\alpha} \frac {w ^ {\alpha}}{\alpha !} \text {   is   Lorentzian,   then   } c _ {\alpha} ^ {2} \geq c _ {\alpha - e _ {i} + e _ {j}} c _ {\alpha + e _ {i} - e _ {j}} \text {   for   any   } \alpha \text {   and   any   } i, j \in [ n ].
$$

Since the Kostka coefficients are the weight multiplicities of the finite-dimensional irreducible representation$V ( \lambda )$of${ \mathrm { G L } } _ { n } ( \mathbb { C } )$, the Lorentzian property of$\mathrm { N } ( s _ { \lambda } )$thus implies

$$
\left(\dim V (\lambda) _ {\alpha}\right) ^ {2} \geq \dim V (\lambda) _ {\alpha - e _ {i} + e _ {j}} \dim V (\lambda) _ {\alpha - e _ {j} + e _ {i}} \text {   for   any   } i, j \in [ n ].
$$

Could this be a special case of a more general discrete log-concavity for weight multiplicities?

Let Λ be the integral weight lattice of the Lie algebra${ \mathfrak { s l } } _ { n } ( \mathbb { C } )$. For$\lambda \in \Lambda$, write$\mathrm { V } ( \lambda )$ for the irreducible${ \mathfrak { s l } } _ { n } ( \mathbb { C } )$-module with the highest weight$\lambda$ and consider its decomposition into finite-dimensional weight spaces

$$
\mathrm{V} (\lambda) = \bigoplus_ {\alpha} \mathrm{V} (\lambda) _ {\alpha}.
$$

We point to [41] for background on the representation theory of semisimple Lie algebras. The following conjecture was proposed in [39, Section 3.1].

Conjecture 19. For any$\lambda \in \Lambda$and any$\alpha \in \Lambda$, we have

$$
(\dim \mathrm{V} (\lambda) _ {\alpha}) ^ {2} \geq \dim \mathrm{V} (\lambda) _ {\alpha - e _ {i} + e _ {j}} \dim \mathrm{V} (\lambda) _ {\alpha - e _ {j} + e _ {i}} \text { for   any } i, j \in [ n ].
$$

When$\lambda$is dominant, the dimension of the weight space$\mathrm { V } ( \lambda ) _ { \alpha }$is the Kostka number$K _ { \lambda \alpha }$, and the Lorentzian property of the normalized Schur polynomial$\mathrm { N } ( s _ { \lambda } )$implies that Conjecture 19 holds in this case. When$\lambda$is antidominant, V($\lambda$) is the Verma module M($\lambda$), the universal highest weight module of highest weight$\lambda$. Using the connection between the Kostant partition function and the volumes of flow polytopes in [8], one can produce Lorentzian polynomials that witness the validity of the conjecture in this case [39, Proposition 11]. Figure 1 illustrates some cases of Conjecture 19 when$\lambda$is neither dominant nor antidominant.

![](images/page_14_image_0.jpg)

The figure shows some of the weight multiplicities of the irreducible${ \mathfrak { s l } } _ { 4 } ( \mathbb { C } )$-module with the highest weight$- 2 \varpi _ { 1 } - 3 \varpi _ { 2 }$. We start from the highlighted vertex$\varpi _ { 1 } - 6 \varpi _ { 2 } - 3 \varpi _ { 3 }$and walk along negative root directions in the hyperplane spanned by$e _ { 2 } - e _ { 1 }$and$e _ { 3 } - e _ { 2 }$. In the shown region, the sequence of weight multiplicities alon any line is log-concave, as predicted by Conjecture 19.

Conjecture 19 suggests the following existence statements of increasing strength.

There is a Lorentzian polynomial$f$ that implies the discrete log-concavity in Conjecture 19 for given$\lambda$and$\alpha$.

There is a cohomology$A$ satisfying the Hodge–Riemann relations that implies the Lorentzian property of$f$ for given$\lambda$and$\alpha$.

There is a projective variety$X$ that implies the Hodge–Riemann relations of$A$ for given$\lambda$and$\alpha$.

We give a precise formulation of the first prediction.

For$\lambda \in \Lambda$, consider the Laurent generating function

$$
\operatorname{ch} _ {\lambda} \left(w _ {1}, \dots , w _ {n}\right) := \sum_ {\alpha \in \Lambda} \dim \mathrm{V} (\lambda) _ {\alpha} w ^ {\alpha - \lambda}.
$$

Note that every monomial appearing in$\operatorname { c h } _ { \lambda }$is a product of degree zero monomials of the form$x _ { i } x _ { j } ^ { - 1 }$

Conjecture 20.$\mathbf { N } ( x ^ { \delta } \mathrm { c h } _ { \lambda } ( w _ { 1 } , \dots , w _ { n } ) )$ is Lorentzian for any$\lambda \in \Lambda$and$\delta \in \mathbb { Z } _ { \geq 0 } ^ { n }$

Conjecture 20 holds for any$\lambda$ when$\lambda$is either dominant or antidominant. In general, the homogeneous polynomial$\mathrm { N } ( x ^ { \delta } \mathrm { c h } _ { \lambda } )$can be computed using the Kazhdan–Lusztig theory [41, Chapter 8]. The authors of [39] tested Conjecture 20 for$\lambda = - \sigma \rho - \rho$and$\delta = ( 1 , \ldots , 1 )$, where$\rho$is the sum of all the fundamental weights, for all permutations$\sigma$in$S _ { n }$for$n \leq 6$. Conjecture 19 for$\lambda$and$\alpha$follows from Conjecture 20 for$\lambda$and any sufficiently large$\delta .$

Similar conjectures can be made for various other polynomials appearing in representation theory and symmetric function theory. For relevant definitions, we refer to [39, Section 3] and references therein.

Conjecture 21. The following polynomials are Lorentzian [39, Conjectures 15,19,20,22,23]:

(1) The normalized Schubert polynomial$\mathrm { N } ( { \mathfrak { S } } _ { \sigma } )$for any permutation$\sigma$

(2) The normalized skew Schur polynomial$\mathrm { N } ( s _ { \lambda / \nu } )$for any skew partition$\lambda / \nu$

(3) The normalized Schur P-polynomial$\mathrm { N } ( P _ { \lambda } )$for any strict partition$\lambda$.

(4) The normalized key polynomial$\mathrm { N } ( \kappa _ { \mu } )$for any composition$\mu$.

(5) The normalized homogeneous Grothendieck polynomial$\mathrm { N } ( { \widetilde { \mathfrak { G } } } _ { \sigma } )$for any permutation$\sigma$.

The M-convexity of the support is known for the Schubert polynomial [29, Corollary 8], the skew Schur polynomial [55, Proposition 2.9], the Schur P-polynomial [55, Proposition 3.5], and the key polynomial [29, Corollary 8]. The potential validity of each of these conjectures suggests the existence of certain Hodge–Riemann relations, or perhaps more strongly, projective varieties.

## 3. Intersection cohomology of matroids

The set of bases of a matroid M on a finite set$E$is a subset$\mathcal { B } \subseteq 2 ^ { E }$that satisfies the symmetric basis exchange property: For any$B _ { 1 } , B _ { 2 } \in \mathcal { B }$and any$i \in B _ { 1 } \ \backslash \ B _ { 2 }$, there is $j \in B _ { 2 } \ \backslash \ B _ { 1 }$such that

$$
(B _ {1} \setminus i) \cup j \in \mathscr {B} \text { and } (B _ {2} \setminus j) \cup i \in \mathscr {B}.
$$

Any two bases of M have the same cardinality$d = \operatorname { r k } \mathbf { M } .$, called the rank of M. When M has a representation$\varphi : E \to W$over a field F, the authors of [5] construct a collection of nef divisors$( L _ { i } ) _ { i \in E }$on a$d$-dimensional irreducible projective variety$Y$over$\mathbb { F }$whose volume polynomial is the basis generating polynomial of M:

$$
\frac {1}{d !} \deg \left(\sum_ {i \in E} w _ {i} L _ {i}\right) ^ {d} = \sum_ {B \in \mathcal {B}} \prod_ {i \in B} w _ {i}.
$$

The projective variety$Y$, called the matroid Schubert variety of$\varphi$, is the closure of the image of the dual map$\varphi ^ { \vee } : W ^ { \vee } \to \mathbb { F } ^ { E }$in the product of projective lines$( \mathbb { P } ^ { 1 } ) ^ { E }$. In view of Proposition 5, one can say that$Y$is a geometric source of the Lorentzian property of the basis generating polynomial. A detailed study of this$Y$and its resolution of singularities in [40] was used to define the intersection cohomology IH(M) of M in [12]. When M is not representable over any field, there is no known projective variety that explains the Lorentzian property of the basis generating polynomial of M. However, for any M, one can construct IH(M) as a graded

Q-vector space equipped with a symmetric pairing$P : { \mathrm { I H } } ^ { * } ( { \mathrm { M } } ) \times { \mathrm { I H } } ^ { d - * } ( { \mathrm { M } } ) \to \mathbb { Q }$and graded linear operators$L _ { i } : \mathrm { I H } ^ { * } ( \mathbf { M } ) \to \mathrm { I H } ^ { * + 1 } ( \mathbf { M } )$for each$i$in$E$. The main result of [12] is that IH(M) satisfies the Poincaré duality, the hard Lefschetz theorem, and the Hodge–Riemann relations with respect to any positive linear combination of$( L _ { i } ) _ { i \in E }$. When M is representable over the complex numbers, the intersection cohomology of M is the intersection cohomology of$X$with Q-coefficients. When M is representable over a finite field, the intersection cohomology of M is a rational form of the ℓ-adic étale intersection cohomology of$X$ for which the Hodge–Riemann relations hold.6 The existence of IH(M) plays a central role in the resolution of two combinatorial conjectures on M, the top-heavy conjecture for the lattice of flats and the nonnegativity conjecture for the Kazhdan-Lusztig coefficients. Below we outline the construction of IH(M) and explain its relation to the two conjectures.

The top-heavy conjecture was proposed by Dowling and Wilson in [22, 23]. It originates from the following theorem of de Bruĳn and Erdős [20]:

Every finite set of points$E$ in a projective plane determines at least$| E |$lines, unless$E$is contained in a line.

In other words, if$E$is not contained in a line, then the number of lines in the plane containing at least two points in$E$is at least |$E$|. The result is valid for any projective plane, not necessarily Desarguesian, and in this sense the statement is purely combinatorial. The figures below depict the two possibilities when$| E | = 4$

![](images/page_16_image_4.jpg)

![](images/page_16_image_5.jpg)

(4 points determining 6 lines)

(4 points determining 4 lines)

The following more general statement, conjectured by Motzkin in [56], was subsequentl proved by many in various settings:

Every finite set of points$E$ in a projective space determines at least |$E$| hyperplanes, unless$E$is contained in a hyperplane.

Motzkin proved the above for$E$ in real projective spaces in [57]. Basterfield and Kelly [9] showed the statement in general, and Greene [34] strengthened the result by showing that there is an order-matching from$E$ to the set of hyperplanes determined by$E$, unless$E$is contained in a hyperplane:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">6Since$\mathbb { Q } _ { \ell }$ is not ordered, there are no Hodge–Riemann relations for the ℓ-adic intersection cohomology. When M is representable over some field, we suspect that IH(M) is a Chow analogue of the intersection cohomology of$X$.</span></small>

For every point in$E$ one can choose a hyperplane containing the point in such a way that no hyperplane is chosen twice.

Mason [51] and Heron [37] obtained similar results by different methods.

Based on these and other known results, Dowling and Wilson formulated the topheavy conjecture in the generality of matroids, in terms of their flats.

Definition 22. A flat of a matroid M on a finite set$E$is a subset of$E$that is maximal for its rank.

In other words, a subset of$E$is a flat of M if the addition of any other element to the set increases its rank in M. Since the intersection of flats of M is a flat of M, the collection of all flats of M form a lattice$\mathcal { L } = \mathcal { L } ( \mathbf { M } )$, the lattice of flats of M. The lattice$\mathcal { L }$is graded, and the rank of a subset$S$ of$E$ in M is the height of the smallest flat of M containing$S$ in the graded lattice$\mathcal { L }$. Thus, one can recover the rank function of M, and hence the set of bases $\mathcal { B }$of M, from the lattice of flats$\mathcal { L }$of M.

We write$\mathcal L ^ { k }$for the set of rank$k$flats of M. When M has a representation$\varphi : E \to W$ over a field F, we have

$$
\mathscr {L} ^ {k} = \left\{\varphi^ {- 1} (V) \mid V \text {   is   a   } k \text {-dimensional   subspace   of   } W \right\}.
$$

When$\varphi$injects$E$ into the projective space$\mathbb { P } V$, there are bĳections

$\mathcal { L } ^ { 1 } \simeq$the set of points in$E$and$\mathcal { L } ^ { 2 } \simeq$the set of lines joining points in$E$.

The top-heavy conjecture extends the relation between$| \mathcal { L } ^ { 1 } |$and$| \mathcal { L } ^ { 2 } |$in de Bruĳn–Erdős theorem as follows.

Conjecture 23 (Top-heavy conjecture). Let$\mathcal { L }$be the lattice of flats of a rank$d$matroid

(1) For every nonnegative integer$k$ less than$\begin{array} { l } { { \frac { d } { 2 } } } \end{array}$

$$
| \mathcal {L} ^ {k} | \leq | \mathcal {L} ^ {d - k} |.
$$

In fact, there is an injective map$\iota : \mathcal { L } ^ { k } \to \mathcal { L } ^ { d - k }$satisfying$x \leq \iota ( x )$ for all$x$.

(2) For every nonnegative integer$k$ less than$\begin{array} { l } { { \frac { d } { 2 } } } \end{array}$,

$$
| \mathcal {L} ^ {k} | \leq | \mathcal {L} ^ {k + 1} |.
$$

In fact, there is an injective map$\iota : \mathcal { L } ^ { k } \to \mathcal { L } ^ { k + 1 }$satisfying$x \leq \iota ( x )$ for all$x$.

When$\mathcal { L }$is a finite Boolean lattice or a finite projective geometry, Conjecture 23 is a classical result; see for example [71, Corollary 4.8 and Exercise 4.4]. In these self-dual cases, the second statement of Conjecture 23 says that$\mathcal { L }$admits order-matchings

$$
\mathcal {L} ^ {0} \hookrightarrow \mathcal {L} ^ {1} \hookrightarrow \dots \hookrightarrow \mathcal {L} ^ {\lfloor \frac {d}{2} \rfloor} \leftrightarrow \mathcal {L} ^ {\lceil \frac {d}{2} \rceil} \hookleftarrow \dots \hookleftarrow \mathcal {L} ^ {d - 1} \hookleftarrow \mathcal {L} ^ {d}.
$$

These order-matchings partition$\mathcal { L }$into$| \mathcal { L } ^ { \lfloor \frac { d } { 2 } \rfloor } |$disjoint chains, and hence$\mathcal { L }$has the Sperner property:

The maximal number ofpairwise incomparable subsets of [$n$] is the maximum among the binomial coefficients$\binom { n } { k }$. Similarly, the maximal number ofpairwise incomparable subspaces of$\mathbf { F } _ { q } ^ { n }$ is the maximum among the$q$-binomial coefficients ${ \binom { n } { k } } _ { q } .$

Let M be a rank$d$ matroid on a finite set$E$. The proof of Conjecture 23 in [12] is based on a detailed analysis of the graded Möbius algebra

$$
\mathrm{H} (\mathrm{M}) := \bigoplus_ {F \in \mathscr {L} (\mathrm{M})} \mathbb {Q} y _ {F}.
$$

The grading is defined by declaring the degree of the element$y _ { F }$to be rk$F$, the rank of$F$ in M. The multiplication is defined by the formula

$$
y _ {F} y _ {G} := \left\{ \begin{array}{l l} y _ {F \vee G} & \text { if } \operatorname{rk} F + \operatorname{rk} G = \operatorname{rk} (F \vee G), \\ 0 & \text { if } \operatorname{rk} F + \operatorname{rk} G > \operatorname{rk} (F \vee G), \end{array} \right.
$$

where ∨ stands for the join in the lattice of flats of M. Unlike its ungraded counterpart, which is isomorphic to the product of$\mathbb { Q } ^ { \bullet }$as a Q-algebra [68, Theorem 1], the graded Möbius algebra has a nontrivial algebra structure.

There is a straightforward relation between the basis generating polynomial of M and the graded Möbius algebra of M. For each$i$ in$E$, we associate a degree 1 element

$$
L _ {i} := \left\{ \begin{array}{l l} y _ {\bar {i}} & \text { if   the   smallest   flat   } \bar {i} \text {   containing   } i \text {   has   rank   1 }, \\ 0 & \text { if   the   smallest   flat   } \bar {i} \text {   containing   } i \text {   has   rank   0 }. \end{array} \right.
$$

Writing deg for the isomorphism$\mathbf { H } ^ { d } ( \mathbf { M } ) \simeq \mathbb { Q }$with$\mathrm { d e g } ( y _ { E } ) = 1$, we have

$$
\frac {1}{d !} \deg \left(\sum_ {i \in E} w _ {i} L _ {i}\right) ^ {d} = \sum_ {B \in \mathcal {B}} \prod_ {i \in B} w _ {i}.
$$

For the top-heavy conjecture, of central importance is the element$\textstyle L : = \sum _ { i \in E } L _ { i }$. The following elementary statement on H(M), proposed in [40, Conjecture 7], is one of the main conclusions of [12]. Its analogue for Weyl groups and for general Coxeter groups can b found in [11] and [54].

Theorem 24. For every nonnegative integer$\begin{array} { r } { k \leq \frac { d } { 2 } } \end{array}$, the multiplication map

$$
\mathrm{H} ^ {k} (\mathrm{M}) \longrightarrow \mathrm{H} ^ {d - k} (\mathrm{M}), \qquad x \longmapsto L ^ {d - 2 k} x
$$

is injective (the injective hard Lefschetz property for M).

To deduce Conjecture 23 from Theorem 24, consider the matrix of the multiplication map with respect to the standard bases of the source and the target. Entries of this matrix are labeled by pairs of elements of$\mathcal { L }$, and all the entries corresponding to incomparable pairs are zero. The matrix has full rank by Theorem 24, so there is a maximal square submatrix with a nonzero determinant. In the standard expansion of this determinant, there must be a nonzero term, and the permutation corresponding to this term produces the injective map$\iota$ in Conjecture 23.

It seems dificult to prove Theorem 24 directly. One possible reason for this is the lack of Poincaré duality for H(M): Typically, for small$d$, a matroid has much more corank$d$flats than rank$d$flats. In known settings where the hard Lefschetz property is the main statement needed for applications [12, 26, 44], it was necessary to prove Poincaré duality, the hard Lefschetz property, and the Hodge–Riemann relations together as a single package.

The intersection cohomology IH(M) is an H(M)-module that repairs the failure of Poincaré duality of H(M) in an eficient way. The construction of IH(M) is inspired by the Kazhdan–Lusztig theory of matroids developed in [25]. For any flat$F$ of M, we define the localization of M at$F$to be the matroid$\mathbf { M } ^ { F }$ on the ground set$F$ whose flats are the flats of M contained in$F$. Similarly, we define the contraction of M at$F$to be the matroid$\mathbf { M } _ { F }$ on the ground set$E \backslash F$whose flats are$G \backslash F$for flats$F$ of M containing$F . ^ { 7 }$According to [14, Theorem 2.2], there is a unique way to assign a polynomial$P _ { \mathrm { M } } ( t )$to each matroid M, called the Kazhdan–Lusztig polynomial of M, subject to the following three conditions:

(1) If rk$\mathbf M = 0$, then$P _ { \mathrm { M } } ( t )$is the constant polynomial 1.

(2) If rk$\mathbf M > 0$, then the degree of$P _ { \mathrm { M } } ( t )$is strictly less than rk$\mathbf { M } / 2$

(3) We have$Z _ { \mathrm { M } } ( t ) = t ^ { \mathrm { r k M } } Z _ { \mathrm { M } } ( t ^ { - 1 } )$, where$Z _ { \mathrm { M } } ( t ) : = \sum _ { F \in \mathcal { L } ( \mathrm { M } ) } t ^ { \mathrm { r k _ { \mathrm { M } } } F } P _ { \mathrm { M } _ { F } } ( t ) .$

The polynomial$Z _ { \mathrm { M } } ( t )$, called the$Z$-polynomial of M, was introduced in [64] using a different but equivalent definition of$P _ { \mathrm { M } } ( t )$

Example 25. It is straightforward to check that the Kazhdan–Lusztig polynomial is 1 for matroids of rank at most two. Thus, when the rank of M is three, we should have

$$
P _ {\mathrm{M}} (t) + | \mathcal {L} ^ {1} | t + | \mathcal {L} ^ {2} | t ^ {2} + t ^ {3} = t ^ {3} P _ {\mathrm{M}} (t ^ {- 1}) + | \mathcal {L} ^ {1} | t ^ {2} + | \mathcal {L} ^ {2} | t + 1.
$$

Since the degree of$P _ { \mathrm { M } } ( t )$is at most 1, it follows that$P _ { \mathrm { M } } ( t ) = 1 + | \mathcal { L } ^ { 2 } | t - | \mathcal { L } ^ { 1 } | t$

Example 26. When the rank of M is four, computing as in Example 25, we get$P _ { \mathrm { M } } ( t ) =$ $1 + | \mathcal { L } ^ { 3 } | t - | \mathcal { L } ^ { 1 } | t$. When the rank of M is five [25, Proposition 2.16], we have

$$
P _ {\mathrm{M}} (t) = 1 + | \mathcal {L} ^ {4} | t - | \mathcal {L} ^ {1} | t + | \mathcal {L} ^ {3} | t ^ {2} - | \mathcal {L} ^ {2} | t ^ {2} + | \mathcal {L} ^ {1, 2} | t ^ {2} - | \mathcal {L} ^ {1, 4} | t ^ {2} + | \mathcal {L} ^ {2, 4} | t ^ {2} - | \mathcal {L} ^ {2, 3} | t ^ {2},
$$

where$\vert \mathcal { L } ^ { i , j } \vert$is the number of incidences between the flats of rank$i$ and rank$j$. For example, if M is the uniform matroid of rank 5 on 6 elements,$P _ { \mathrm { M } } ( t ) = 1 + 9 t + 5 t ^ { 2 }$

The following nonnegativity conjecture was proposed in [25, Conjecture 2.8], where it was proved for matroids representable over some field using ℓ-adic étale intersection cohomology theory of [10]. For sparse paving matroids, a combinatorial proof of the nonnegativity was given in [47]. The general case of the conjecture is proved in [12, Theorem 1.3] using the intersection cohomology of matroids.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">7In [25], as well as several other references on Kazhdan–Lusztig polynomials of matroids, the localization is denoted$\mathbf { M } ^ { F }$ and the contraction is denoted$\mathbf { M } _ { F }$. Our notational choice here is consistent with [1] and [12, 13].</span></small>

Conjecture 27 (Nonnegativity conjecture).$P _ { \mathrm { M } } ( t )$has nonnegative coefficients for any M

Kazhdan–Lusztig polynomials of matroids are special cases of Kazhdan–Lusztig– Stanley polynomials [63,70]. Several important families of Kazhdan–Lusztig–Stanley polynomials turn out to have nonnegative coefficients, including classical Kazhdan–Lusztig polynomials associated with Bruhat intervals [26] and $Z$-polynomials of convex polytopes [44]. Each of the known proofs of the nonnegativity of the three Kazhdan–Lusztig–Stanley polynomials involves numerous details that are unique to that specific case.

The following existence result of [12] implies Conjecture 23 and Conjecture 27. Let $K ( \mathbf { M } )$be the open convex cone of degree 1 elements

$$
K (\mathrm{M}) = \left\{\sum_ {F \in \mathscr {L} ^ {1}} c _ {F} y _ {F} \mid c _ {F} \text {   is   positive } \right\} \subseteq \mathrm{H} ^ {1} (\mathrm{M}).
$$

The elements of$K$(M) act as linear operators by multiplication on any H(M)-module.

Theorem 28. There is a graded H(M)-module IH(M) and a symmetric bilinear pairing

$$
P: \mathrm{IH} ^ {*} (\mathbf {M}) \times \mathrm{IH} ^ {d - *} (\mathbf {M}) \to \mathbb {Q}
$$

that satisfies the following properties for any nonnegative integer$\begin{array} { r } { k \leq \frac { d } { 2 } } \end{array}$

(1) The symmetric bilinear pairing

$$
\mathrm{IH} ^ {k} (\mathrm{M}) \times \mathrm{IH} ^ {d - k} (\mathrm{M}) \longrightarrow \mathbb {Q}, \quad (x _ {1}, x _ {2}) \longmapsto P (x _ {1}, x _ {2})
$$

is nondegenerate (Poincaré duality theorem for M).

(2) For any$L _ { 1 } , \ldots , L _ { d - 2 k } \in K ( \mathbf { M } )$, the multiplication map

$$
\mathrm{IH} ^ {k} (\mathrm{M}) \longrightarrow \mathrm{IH} ^ {d - k} (\mathrm{M}), \quad x \longmapsto \left(\prod_ {i = 1} ^ {d - 2 k} L _ {i}\right) x
$$

is an isomorphism (hard Lefschetz theorem for M).

(3) For any$L _ { 0 } , L _ { 1 } , \dots , L _ { d - 2 k } \in K ( X )$, the symmetric bilinear form

$$
\mathrm{IH} ^ {k} (\mathrm{M}) \times \mathrm{IH} ^ {k} (\mathrm{M}) \longrightarrow \mathbb {Q}, \quad (x _ {1}, x _ {2}) \longmapsto (- 1) ^ {k} \mathrm{P} (x _ {1}, \left(\prod_ {i = 1} ^ {d - 2 k} L _ {i}\right) x _ {2})
$$

is positive definite on the kernel of the linear map

$$
\mathrm{IH} ^ {k} (\mathrm{M}) \longrightarrow \mathrm{IH} ^ {d - k + 1} (\mathrm{M}), \qquad x \longmapsto \big (\prod_ {i = 0} ^ {d - 2 k} L _ {i} \big)   x
$$

(Hodge–Riemann relations for M).

(4) Writing$\mathrm { I H } _ { \varnothing }$for the graded vector space$\operatorname { I H } ( \mathbf { M } ) \otimes _ { \operatorname { H } ( \mathbf { M } ) } \mathbb { Q } .$, we have

$$
P _ {\mathrm{M}} (t) = \sum_ {k \geq 0} \dim \left(\mathrm{IH} _ {\emptyset} ^ {k}\right) t ^ {k} \text {and} Z _ {\mathrm{M}} (t) = \sum_ {k \geq 0} \dim \left(\mathrm{IH} ^ {k} (\mathrm{M})\right) t ^ {k}
$$

(Kazhdan–Lusztig identities for M).

(5)$\mathrm { I H } ^ { 0 } ( \mathbf { M } )$generates a submodule isomorphic to H(M) (Purity for M).

Since injective maps restrict to injective maps, the injective hard Lefschetz property for M in Theorem 24, and hence the top-heavy conjecture for M, follows from the hard Lefschetz theorem and the purity for M. The nonnegativity conjecture for M follows from the Kazhdan–Lusztig identities for M. More generally, when a finite group$\Gamma$acts on M, one can define the equivariant Kazhdan–Lusztig polynomial$P _ { \mathrm { M } } ^ { \Gamma } ( t )$as in [31]. This is a polynomial with coefficients in the ring of virtual representations of Γ, with the property that taking dimensions recovers the ordinary polynomial$P _ { \mathrm { M } } ( t )$. The authors of [12] show that$\Gamma$acts naturally on IH(M) and that

$$
P _ {\mathrm{M}} ^ {\Gamma} (t) = \sum_ {k \geq 0} \left[ \Gamma \curvearrowright \mathrm{IH} _ {\emptyset} ^ {k} \right] t ^ {k} \in \mathrm{VRep} (\Gamma) [ t ].
$$

This proves the equivariant nonnegativity conjecture proposed in [31, Conjecture 2.13]. Conjecture 27 is the special case when Γ is trivial.

The construction of$\mathrm { I H } ( \mathbf { M } )$is inspired by geometry in the representable case. Consider the case when M has a representation$\varphi : E \to W$over C, and recall that the matroid Schubert variety$Y$ of$\varphi$is the closure of$W ^ { \vee }$in the product of projective lines$( \mathbb { P } ^ { 1 } ) ^ { E }$. The additive group$W ^ { \vee }$ acts on$Y$ with finitely many orbits, each of which is isomorphic to an affine space. The poset of cells in this stratification of$Y$is isomorphic to the poset of cells is isomorphic to the lattice of flats of M, and, in fact, the singular cohomology$\mathrm { H } ^ { 2 \ast } ( Y , \mathbb { Q } )$is isomorphic to the graded Möbius algebra$\mathbf { H } ^ { * } ( \mathbf { M } )$[40, Theorem 14].8

The Schubert variety admits a distinguished resolution of singularities$f : X \to Y$ obtained by blowing up all the strata in the order of increasing dimension. The resulting smooth projective variety$X$ is the augmented wonderful variety of$M$ studied in [13]. Adopting the computations in [21, 28], one can show that its singular cohomology and Chow rings are isomorphic to the augmented Chow ring

$\mathbf { C H } ( \mathbf { M } ) : = \mathbb { Q } [ y _ { i } , x _ { F } \mid i$is an element of$E$ and$F$is a proper flat of$\mathrm { M } ] / \left( I _ { \mathrm { M } } + J _ { \mathrm { M } } \right)$

where$I _ { \mathbf { M } }$is the ideal generated by the linear forms

$$
y _ {i} - \sum_ {i \notin F} x _ {F}, \text {   for   every   element   } i \text {   of   } E,
$$

and$J _ { \mathbf { M } }$is the ideal generated by the quadratic monomials

$x _ { F _ { 1 } } x _ { F _ { 2 } }$, for every pair of incomparable proper flats$F _ { 1 }$and$F _ { 2 }$of M, and

$y _ { i } x _ { F } .$, for every element$i$ of$E$ and every proper flat$F$ of M not containing$i$.

As expected from the identification with$\operatorname { H } ^ { 2 * } ( X , \mathbb { Q } )$in the representable case, for any M, the augmented Chow ring of M vanishes in degrees larger than$d$. Furthermore, there is a unique linear map

$$
\deg \colon \mathrm{CH} ^ {d} (\mathrm{M}) \longrightarrow \mathbb {Q}, \quad \prod_ {F \in \mathscr {F}} x _ {F} \longmapsto 1,
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">8All the cohomology rings and intersection cohomology groups of varieties in this paper vanish in odd degrees, and our isomorphisms double degrees.</span></small>

where$\mathcal { F }$is any complete flag of proper flats of M, defining a symmetric pairing on CH(M).

The main observation is that the pullback homomorphism in singular cohomology

$$
f ^ {*}: \mathrm{H} ^ {*} (Y, \mathbb {Q}) \longrightarrow \mathrm{H} ^ {*} (X, \mathbb {Q})
$$

only depends on M and not on$\varphi .$. In terms of the graded Möbius algebra and the augmented Chow ring of M, the pullback homomorphism is given by

$$
f ^ {*}: \mathrm{H} (\mathrm{M}) \longrightarrow \mathrm{CH} (\mathrm{M}), \quad L _ {i} \longmapsto y _ {i}.
$$

Applying the decomposition theorem of Beilinson–Bernstein–Deligne–Gabber [10] to$f ,$, we find that the intersection cohomology$\mathrm { I H } ^ { * } ( Y )$is isomorphic as a graded$\mathrm { H } ^ { * } ( Y )$-module to a direct summand of$\mathrm { H } ^ { * } ( X )$. Furthermore, a slight extension of an argument of Ginzburg [33] shows that$\mathrm { I H } ^ { * } ( Y )$is indecomposable as an$\mathrm { H } ^ { * } ( Y )$-module. This motivates the following definition.

Definition 29. The intersection cohomology IH(M) of a matroid M is the unique indecomposable graded H(M)-module direct summand of CH(M) that is nonzero in degree zero

The above defines the intersection cohomology of M up to isomorphism of graded H(M)-modules, where the uniqueness is given by the general Krull–Schmidt theorem [7, Theorem 1]. The intersection cohomology inherits a symmetric pairing$P$ from CH(M). In [12], the authors construct a canonical submodule$\mathrm { I H } ( \mathbf { M } ) \subseteq \mathbf { C H } ( \mathbf { M } )$that is preserved by all the symmetries of M. The construction of IH(M) as an explicit submodule of CH(M), or more generally the construction of the canonical decomposition of CH(M) as a graded H(M)- module, is essential in inductively proving Poincaré duality, the hard Lefschetz theorem, and the Hodge–Riemann relations for IH(M).

## Acknowledgments

I thank my past and current collaborators: Karim Adiprasito, Federico Ardila, Farhad Babaee, Tom Braden, Petter Brändén, Graham Denham, Chris Eur, Eric Katz, Matt Larson, Jacob Matherne, Karola Mészáros, Nick Proudfoot, Benjamin Schröter, Avery St. Dizier, Bernd Sturmfels, and Botong Wang. It was a privilege to have connected with your minds, and I am grateful for our mathematical adventures together.

## Funding

This work was partially supported by Simons Investigator Grant and NSF Grant DMS-2053308.

## References

[1]K. Adiprasito, J. Huh, and E. Katz, Hodge theory for combinatorial geometries. Ann. of Math. (2) 188 (2018), no. 2, 381–452

[2]N. Anari, S. O. Gharan, and C. Vinzant, Log-concave polynomials, I: entropy and a deterministic approximation algorithm for counting bases of matroids. Duke Math. J. 170 (2021), no. 16, 3459–3504

[3]N. Anari, K. Liu, S. O. Gharan, and C. Vinzant, Log-concave polynomials II: High-dimensional walks and an FPRAS for counting bases of a matroid. In STOC’19—Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, pp. 1–12, ACM, New York, 2019

[4]N. Anari, K. Liu, S. Oveis Gharan, and C. Vinzant, Log-concave polynomial III: Mason’s ultra-log-concavity conjecture for independent sets of matroids. arXiv:1811.01600

[5]F. Ardila and A. Boocher, The closure of a linear space in a product of lines. J. Algebraic Combin. 43 (2016), no. 1, 199–235

[6]F. Ardila, G. Denham, and J. Huh, Lagrangian geometry of matroids. J. Amer. Math. Soc., to appear. DOI: https://doi.org/10.1090/jams/1009

[7]M. Atiyah, On the Krull-Schmidt theorem with application to sheaves. Bull. Soc. Math. France 84 (1956), 307–317

[8]W. Baldoni and M. Vergne, Kostant partitions functions and flow polytopes. Transform. Groups 13 (2008), no. 3-4, 447–469

[9]J. G. Basterfield and L. M. Kelly, A characterization of sets of$n$points which determine$n$hyperplanes. Proc. Cambridge Philos. Soc. 64 (1968), 585–588

[10] A. A. Be˘ılinson, J. Bernstein, and P. Deligne, Faisceaux pervers. In Analysis and topology on singular spaces, I (Luminy, 1981), pp. 5–171, Astérisque 100, Soc. Math. France, Paris, 1982

[11] A. Björner and T. Ekedahl, On the shape of Bruhat intervals. Ann. ofMath. (2) 170 (2009), no. 2, 799–817

[12] T. Braden, J. Huh, J. Matherne, N. Proudfoot, and B. Wang, Singular Hodge theory for combinatorial geometries. arXiv:2010.06088

[13] T. Braden, J. Huh, J. P. Matherne, N. Proudfoot, and B. Wang, A semi-smal decomposition of the Chow ring of a matroid. arXiv:2002.03341

[14] T. Braden and A. Vysogorets, Kazhdan-Lusztig polynomials of matroids under deletion. Electron. J. Combin. 27 (2020), no. 1, Paper No. 1.17, 17

[15] P. Brändén, Discrete concavity and the half-plane property. SIAM J. Discrete Math. 24 (2010), no. 3, 921–933

[16] P. Brändén, Spaces of Lorentzian and real stable polynomials are Euclidean balls. Forum Math. Sigma 9 (2021), Paper No. e73, 8

[17] P. Brändén and J. Huh, Lorentzian polynomials. Ann. of Math. (2) 192 (2020), no. 3, 821–891

[18] E. Cattani, Mixed Lefschetz theorems and Hodge-Riemann bilinear relations. Int. Math. Res. Not. IMRN (2008), no. 10, Art. ID rnn025, 20

[19] C. Chindris, H. Derksen, and J. Weyman, Counterexamples to Okounkov’s logconcavity conjecture. Compos. Math. 143 (2007), no. 6, 1545–1557

[20] N. G. de Bruĳn and P. Erdös, On a combinatorial problem. Nederl. Akad. Wetensch., Proc. 51 (1948), 1277–1279 = Indagationes Math. 10, 421–423 (1948)

[21] C. De Concini and C. Procesi, Wonderful models of subspace arrangements. Selecta Math. (N.S.) 1 (1995), no. 3, 459–494

[22] T. A. Dowling and R. M. Wilson, The slimmest geometric lattices. Trans. Amer. Math. Soc. 196 (1974), 203–215

[23] T. A. Dowling and R. M. Wilson, Whitney number inequalities for geometric lattices. Proc. Amer. Math. Soc. 47 (1975), 504–512

[24] J. Edmonds, Submodular functions, matroids, and certain polyhedra. In Combinatorial Structures and their Applications (Proc. Calgary Internat. Conf., Calgary, Alta., 1969), pp. 69–87, Gordon and Breach, New York, 1970

[25] B. Elias, N. Proudfoot, and M. Wakefield, The Kazhdan-Lusztig polynomial of a matroid. Adv. Math. 299 (2016), 36–70

[26] B. Elias and G. Williamson, The Hodge theory of Soergel bimodules. Ann. of Math. (2) 180 (2014), no. 3, 1089–1136

[27] C. Eur and J. Huh, Logarithmic concavity for morphisms of matroids. Adv. Math. 367 (2020), 107094, 19

[28] E. M. Feichtner and S. Yuzvinsky, Chow rings of toric varieties defined by atomic lattices. Invent. Math. 155 (2004), no. 3, 515–536

[29] A. Fink, K. Mészáros, and A. St. Dizier, Schubert polynomials as integer point transforms of generalized permutahedra. Adv. Math. 332 (2018), 465–475

[30] W. Fulton, Young tableaux. London Mathematical Society Student Texts 35, Cambridge University Press, Cambridge, 1997

[31] K. Gedeon, N. Proudfoot, and B. Young, The equivariant Kazhdan-Lusztig polynomial of a matroid. J. Combin. Theory Ser. A 150 (2017), 267–294

[32] I. M. Gelfand, R. M. Goresky, R. D. MacPherson, and V. V. Serganova, Combinatorial geometries, convex polyhedra, and Schubert cells. Adv. in Math. 63 (1987), no. 3, 301–316

[33] V. Ginsburg, Perverse sheaves and C<sup>∗</sup>-actions. J. Amer. Math. Soc. 4 (1991), no. 3, 483–490

[34] C. Greene, A rank inequality for finite geometric lattices. J. Combinatorial Theory 9 (1970), 357–364

[35] A. Grothendieck, Standard conjectures on algebraic cycles. In Algebraic Geometr (Internat. Colloq., Tata Inst. Fund. Res., Bombay, 1968), pp. 193–199, Oxford Univ. Press, London, 1969

[36] L. Gurvits, On multivariate Newton-like inequalities. In Advances in combinatorial mathematics, pp. 61–78, Springer, Berlin, 2009

[37] A. P. Heron, Matroid polynomials. In Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 164–202, 1972

[38] J. Herzog and T. Hibi, Discrete polymatroids. J. Algebraic Combin. 16 (2002), no. 3, 239–268 (2003)

[39]J. Huh, J. Matherne, K. Mészáros, and A. St. Dizier, Logarithmic concavity of Schur and related polynomials. Trans. Amer. Math. Soc., to appear. DOI: https://doi.org/10.1090/tran/8606

[40] J. Huh and B. Wang, Enumeration of points, lines, planes, etc. Acta Math. 218 (2017), no. 2, 297–317

[41] J. E. Humphreys, Representations ofsemisimple Lie algebras in the BGG category$\mathcal { O }$. Graduate Studies in Mathematics 94, American Mathematical Society, Providence, RI, 2008

[42] D. Huybrechts, Complex geometry. Universitext, Springer-Verlag, Berlin, 2005

[43] C. Jiang and Z. Li, Algebraic reverse Khovanskii–Teissier inequality via Okounkov bodies. arXiv:2012.02847

[44] K. Karu, Hard Lefschetz theorem for nonrational polytopes. Invent. Math. 157 (2004), no. 2, 419–447

[45] J. P. S. Kung, Strong maps. In Theory of matroids, pp. 224–253, Encyclopedia Math. Appl. 26, Cambridge Univ. Press, Cambridge, 1986

[46]R. Lazarsfeld, Positivity in algebraic geometry. I. Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Result in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics] 48, Springer-Verlag, Berlin, 2004

[47] K. Lee, G. D. Nasr, and J. Radclife, A combinatorial formula for Kazhdan– Lusztig polynomials of sparse paving matroids. arXiv:2002.03341

[48] B. Lehmann and J. Xiao, Correspondences between convex geometry and complex geometry. Épĳournal Géom. Algébrique 1 (2017), Art. 6, 29

[49] T. M. Liggett, Ultra logconcave sequences and negative dependence. J. Combin. Theory Ser. A 79 (1997), no. 2, 315–325

[50] D. Maclagan and B. Sturmfels, Introduction to tropical geometry. Graduate Studies in Mathematics 161, American Mathematical Society, Providence, RI, 2015

[51]J. H. Mason, Matroids: unimodal conjectures and Motzkin’s theorem. In Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 207–220, 1972

[52] D. Mayhew, M. Newman, and G. Whittle, Yes, the ‘missing axiom’ of matroid theory is lost forever. Trans. Amer. Math. Soc. 370 (2018), no. 8, 5907–5929

[53] D. Mayhew, G. Whittle, and M. Newman, Is the missing axiom of matroid theory lost forever? Q. J. Math. 65 (2014), no. 4, 1397–1415

[54] G. Melvin and W. Slofstra, Soergel bimodules and the shape of Bruhat intervals. 2020, preprint

[55] C. Monical, N. Tokcan, and A. Yong, Newton polytopes in algebraic combinatorics. Selecta Math. (N.S.) 25 (2019), no. 5, Paper No. 66, 37

[56] T. Motzkin, Beiträge zur theorie der linearen ungleichungen. Buchdr. Azriel, Jerusalem, 1936

[57] T. Motzkin, The lines and planes connecting the points of a finite set. Trans. Amer. Math. Soc. 70 (1951), 451–464

[58] K. Murota, Discrete convex analysis. SIAM Monographs on Discrete Mathematics and Applications, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA, 2003

[59] P. Nelson, Almost all matroids are nonrepresentable. Bull. Lond. Math. Soc. 50 (2018), no. 2, 245–248

[60] A. Okounkov, Why would multiplicities be log-concave? In The orbit method in geometry and physics (Marseille, 2000), pp. 329–347, Progr. Math. 213, Birkhäuser Boston, Boston, MA, 2003

[61] J. Oxley, Matroid theory. Second edn., Oxford Graduate Texts in Mathematics 21, Oxford University Press, Oxford, 2011

[62] A. Postnikov, Permutohedra, associahedra, and beyond. Int. Math. Res. Not. IMRN (2009), no. 6, 1026–1106

[63] N. Proudfoot, The algebraic geometry of Kazhdan-Lusztig-Stanley polynomials. EMS Surv. Math. Sci. 5 (2018), no. 1-2, 99–127

[64] N. Proudfoot, Y. Xu, and B. Young, The$Z$-polynomial of a matroid. Electron. J. Combin. 25 (2018), no. 1, Paper 1.26, 21

[65]R. Schneider, Convex bodies: the Brunn-Minkowski theory. expanded edn., Encyclopedia of Mathematics and its Applications 151, Cambridge University Press, Cambridge, 2014

[66] J.-P. Serre, Analogues kählériens de certaines conjectures de Weil. Ann. of Math. (2) 71 (1960), 392–394

[67] A. D. Sokal, The multivariate Tutte polynomial (alias Potts model) for graphs and matroids. In Surveys in combinatorics 2005, pp. 173–226, London Math. Soc. Lecture Note Ser. 327, Cambridge Univ. Press, Cambridge, 2005

[68] L. Solomon, The Burnside algebra of a finite group. J. Combinatorial Theory 2 (1967), 603–615

[69] R. P. Stanley, The number of faces of a simplicial convex polytope. Adv. in Math. 35 (1980), no. 3, 236–238

[70] R. P. Stanley, Subdivisions and local ℎ-vectors. J. Amer. Math. Soc. 5 (1992), no. 4, 805–851

[71] R. P. Stanley, Algebraic combinatorics. Undergraduate Texts in Mathematics, Springer, Cham, 2018

[72] P. Vámos, The missing axiom of matroid theory is lost forever. J. London Math. Soc. (2) 18 (1978), no. 3, 403–408

[73] S. T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I. Comm. Pure Appl. Math. 31 (1978), no. 3, 339–411

June Huh

Princeton University and Korea Institute for Advanced Study, huh@princeton.edu