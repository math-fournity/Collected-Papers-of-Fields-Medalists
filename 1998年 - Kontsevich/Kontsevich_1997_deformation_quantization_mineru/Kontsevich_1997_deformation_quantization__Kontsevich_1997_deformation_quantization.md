# DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I

Maxim Kontsevich

## 0. Introduction

In this paper it is proven that any finite-dimensional Poisson manifold can be canonically quantized (in the sense of deformation quantization). Informally, it means that the set of equivalence classes of associative algebras close to algebras of functions on manifolds is in one-to-one correspondence with the set of equivalence classes of Poisson manifolds modulo difeomorphisms. This is a corollary of a more general statement, which I proposed around 1993-1994 (“Formality conjecture”) (see [Ko2], [V]).

For a long time the Formality conjecture resisted all approaches. The solution presented here uses in a essential way ideas of string theory. Our formulas can be viewed as a perturbation series for a topological two-dimensional quantum field theory coupled with gravity.

## 0.1. Content of the paper

Section 1: an elementary introduction to the deformation quantization, and precise formulation of the main statement concerning Poisson manifolds.

Section 2: an explicit formula for the deformation quantization written in coordinates.

Section 3: an introduction to the deformation theory in general, in terms of diferential graded Lie algebras. The material of this section is basically standard.

Section 4: a geometric reformulation of the theory introduced in the previous section, in terms of odd vector fields on formal supermanifolds. In particular, we introduce convenient notions of an$L _ { \infty }$-morphism and of a quasi-isomorphism, which gives us a tool to identify deformation theories related with two diferential graded Lie algebras. Also in this section we state our main result, which is an existence of a quasi-isomorphism between the Hochschild complex of the algebra of polynomials, and the graded Lie algebra of polyvector fields.

Section 5: tools for the explicit construction of the quasi-isomorphism mentioned above. We define compactified configuration spaces related with the Lobachevsky plane, a class of admissible graphs, diferential polynomials on polyvector fields related with graphs, and integrals over configuration spaces. Technically the same constructions were used in generalizations of the perturbative Chern-Simons theory several years ago (see [Ko1]). Compactifications of the configuration spaces are close relatives of Fulton-MacPherson compactifications of configuration spaces in algebraic geometry (see [FM]).

Section 6: it is proven that the machinery introduced in the previous section gives a quasi-isomorphism and establishes the Formality conjecture for afine spaces. The proof is essentially an application of the Stokes formula, and a general result of vanishing of certain integral associated with a collection of rational functions on a complex algebraic variety.

Section 7: results of section 6 are extended to the case of general manifolds. In order to do this we recall ideas of formal geometry of I. Gelfand and D. Kazhdan, and the language of superconnections. In order to pass from the afine space to general manifolds we have to find a non-linear cocycle of the Lie algebra of formal vector fields. It turns out that such a cocycle can be almost directly constructed from our explicit formulas. In the course of the proof we calculate several integrals and check their vanishing. Also, we introduce a general notion of direct image for certain bundles of supermanifolds.

Section 8: we describe an additional structure present in the deformation theory of associative algebras, the cup-product on the tangent bundle to the super moduli space. The isomorphism constructed in sections 6, 7 is compatible with this structure. As a corollary, we finally justify the orbit method in the representation theory. One of new results is the validity of Duflo-Kirillov formulas for Lie algebras in general rigid tensor categories, in particular for Lie superalgebras. Another application is an equality between two cup-products in the context of algebraic geometry.

## 0.2. Plans

I am going to write a complement to the present paper. It will contain

1) the comparison with various known constructions of star-products, the most notorious one are by De Wilde-Lecomte and by Fedosov for the case of symplectic manifolds (see [DL], [F]), and by Etingof-Kazhdan for Poisson-Lie groups (see [EK]),

2) a reformulation of the Formality conjecture as an existence of a natural construction of a triangulated category starting from an odd symplectic supermanifold,

3) discussion of the arithmetic nature of coeficients in our formulas, and of the possibility to extend main results for algebraic varieties over arbitrary field of characteristic zero,

4) an application to the Mirror Symmetry, which was the original motivation for the Formality conjecture (see [Ko4]),

5) a Lagrangian for a quantum field theory (from [AKSZ]) which seems to give our formulas after the perturbation expansion.

Also, I am going to touch other topics (a version of formality for cyclic homology, quantization of quadratic brackets, etc).

## 0.3. Acknowledgements

I am grateful to Y. Soibelman for many remarks.

## 1. Deformation quantization

## 1.1. Star-products

Let$A = \Gamma ( X , { \mathcal { O } } _ { X } )$be the algebra over R of smooth functions on a finite-dimensional$C ^ { \infty }$-manifold X. The star-product on A (see [BFFLS]) is an associative$\mathbf { R } [ [ \hbar ] ]$-linear product on$A [ [ \hbar ] ]$given by the following formula for$f , g \in A \subset A [ [ \hbar ] ]$

$$
(f, g) \mapsto f \star g = f g + \hbar B _ {1} (f, g) + \hbar^ {2} B _ {2} (f, g) + \dots \in A [ [ \hbar ] ],
$$

where ¯h is the formal variable, and$B _ { i }$are bidiferential operators (i.e. bilinear maps$A \times A { \longrightarrow } A$which are diferential operators with respect to each argument of globally bounded order). The product of arbitrary elements of$A [ [ \hbar ] ]$is defined by the condition of linearity over$\mathbf { R } [ [ \hbar ] ]$and ¯h-adic continuity:

$$
\left(\sum_ {n \geq 0} f _ {n} \hbar^ {n}\right) \star \left(\sum_ {n \geq 0} g _ {n} \hbar^ {n}\right) := \sum_ {k, l \geq 0} f _ {k} g _ {l} \hbar^ {k + l} + \sum_ {k, l \geq 0, m \geq 1} B _ {m} (f _ {k}, g _ {l}) \hbar^ {k + l + m}.
$$

There is a natural gauge group acting on star-products. This group consists of automorphisms of$A [ [ \hbar ] ]$ considered as an$\mathbf { R } [ [ \hbar ] ]$-module (i.e. linear transformations$A { \longrightarrow } A$parametrized by ¯h), of the following form:

$$
f \mapsto f + \hbar D _ {1} (f) + \hbar^ {2} D _ {2} (f) + \dots , \text { for } f \in A \subset A [ [ \hbar ] ],
$$

$$
\sum_ {n \geq 0} f _ {n} \hbar^ {n} \mapsto \sum_ {n \geq 0} f _ {n} \hbar^ {n} + \sum_ {n \geq 0, m \geq 1} D _ {m} (f _ {n}) \hbar^ {n + m}, \text { for   general   element } f (\hbar) = \sum_ {n \geq 0} f _ {n} \hbar^ {n} \in A [ [ \hbar ] ],
$$

where$D _ { i } : A { \longrightarrow } A$are diferential operators. If$\begin{array} { r } { D ( \hbar ) = 1 + \sum _ { m > 1 } D _ { m } \hbar ^ { m } } \end{array}$is such an automorphism, it acts on the set of star-products as

$$
\star \mapsto \star^ {\prime}, f (\hbar) \star^ {\prime} g (\hbar) := D (\hbar) \big (D (\hbar) ^ {- 1} (f (\hbar)) \star D (\hbar) ^ {- 1} (g (\hbar)), f (\hbar), g (\hbar) \in A [ [ \hbar ] ] .
$$

We are interested in star-products up to gauge equivalence.

## 1.2. First approximation: Poisson structures

It follows from the associativity of ⋆ that the bilinear map$B _ { 1 } : A \times A { \longrightarrow } A$satisfies the equation

$$
f B _ {1} (g, h) - B _ {1} (f g, h) + B _ {1} (f, g h) - B _ {1} (f, g) h = 0,
$$

i.e. the linear map${ \widetilde { B } } _ { 1 } : A \otimes A { \longrightarrow } A$associated with$B _ { 1 }$as$\widetilde { B } _ { 1 } ( f \otimes g ) : = B _ { 1 } ( f , g )$, is a 2-cocycle in the e ecohomological Hochschild complex of algebra A (the definition of this complex is given in 3.4.2).

Let us decompose$B _ { 1 }$into the sum of the symmetric part and of the anti-symmetric part:

$$
B _ {1} = B _ {1} ^ {+} + B _ {1} ^ {-}, \quad B _ {1} ^ {+} (f, g) = B _ {1} ^ {+} (g, f), \quad B _ {1} ^ {-} (f, g) = - B _ {1} ^ {-} (g, f).
$$

Gauge transformations

$$
B _ {1} \mapsto B _ {1} ^ {\prime}, \quad B _ {1} ^ {\prime} (f, g) = B _ {1} (f, g) - f D _ {1} (g) + D _ {1} (f g) - D _ {1} (f) g
$$

where$D _ { 1 }$is an arbitrary diferential operator, afect only the symmetric part of$B _ { 1 }$, i.e.$B _ { 1 } ^ { - } = ( B _ { 1 } ^ { \prime } ) ^ { - }$. One can show that the symmetric part$B _ { 1 } ^ { + }$can be killed by a gauge transformation (and it is a coboundary in the Hochschild complex).

Also one can show that the skew-symmetric part$B _ { 1 } ^ { - }$is a derivation with respect to both functions$f$ and$g .$Thus,$B _ { 1 } ^ { - }$comes from a bi-vector field α on$X { : }$

$$
B _ {1} ^ {-} (f, g) = \langle \alpha , d f \otimes d g \rangle , \alpha \in \Gamma (X, \wedge^ {2} T _ {X}) \subset \Gamma (X, T _ {X} \otimes T _ {X}).
$$

Analogous fact in algebraic geometry is that the second Hochschild cohomology group of the algebra of functions on a smooth afine algebraic variety (in characteristic zero) is naturally isomorphic to the space of bi-vector fields (see 4.6.1.1).

The second term$O ( \hbar ^ { 2 } )$in the associativity equation$f \star ( g \star h ) = ( f \star g ) \star h$implies that α gives a Poisson structure on$X$

$$
\forall f, g, h \quad \{f, \{g, h \} \} + \{g, \{h, f \} \} + \{h, \{f, g \} \} = 0,
$$

$$
\text {where} \{f, g \} := \frac {f \star g - g \star f}{\hbar} _ {| \hbar = 0} = 2   B _ {1} ^ {-} (f, g) = 2 \langle \alpha , d f \otimes d g \rangle .
$$

In other words,$[ \alpha , \alpha ] = 0 \in \Gamma ( X , \wedge ^ { 3 } T _ { X } )$, where the bracket is the Schouten-Nijenhuis bracket on polyvector fields (see 4.6.1 for the definition of this bracket).

Thus, gauge equivalence classes of star-products modulo$O ( \hbar ^ { 2 } )$are classified by Poisson structures on X. A priori it is not clear whether there exists a star-product with the first term equal to a given Poisson structure, and whether there exists a preferred choice of an equivalence class of star-products. We show in this paper that there is a canonical construction of an equivalence class of star-products for any Poisson manifold.

## 1.3. Description of quantizations

Theorem. The set of gauge equivalence classes of star products on a smooth manifold X can be naturally identified with the set of equivalence classes of Poisson structures depending formally on ¯h:

$$
\alpha = \alpha (\hbar) = \alpha_ {1} \hbar + \alpha_ {2} \hbar^ {2} + \ldots \in \Gamma (X, \wedge^ {2} T _ {X}) [ [ \hbar ] ], [ \alpha , \alpha ] = 0 \in \Gamma (X, \wedge^ {3} T _ {X}) [ [ \hbar ] ]
$$

modulo the action of the group of formal paths in the difeomorphism group of$X$, starting at the identity difeomorphism.

Any given Poisson structure$\alpha _ { ( 0 ) }$gives a path$\alpha ( \hbar ) : = \alpha _ { ( 0 ) } \cdot \hbar$and by the Theorem from above, a canonical gauge equivalence class of star products.

## 1.4. Examples

## 1.4.1. Moyal product

The simplest example of a deformation quantization is the Moyal product for the Poisson structure on $\mathbf { R } ^ { d }$with constant coeficients:

$$
\alpha = \sum_ {i, j} \alpha^ {i j} \partial_ {i} \wedge \partial_ {j}, \alpha^ {i j} = - \alpha^ {j i} \in \mathbf {R}
$$

where$\partial _ { i } = \partial / \partial x ^ { i }$is the partial derivative in the direction of coordinate$x ^ { i } , \ i = 1 , \ldots , d .$The formula for the Moyal product is

$$
\begin{array}{l} f \star g = f g + \hbar \sum_ {i, j} \alpha^ {i j}   \partial_ {i} (f)   \partial_ {j} (g) + \frac {\hbar^ {2}}{2} \sum_ {i, j, k, l} \alpha^ {i j} \alpha^ {k l}   \partial_ {i} \partial_ {k} (f)   \partial_ {j} \partial_ {l} (g) + \ldots = \\ = \sum_ {n = 0} ^ {\infty} \frac {\hbar^ {n}}{n !} \sum_ {i _ {1}, \ldots , i _ {n}; j _ {1}, \ldots j _ {n}} \prod_ {k = 1} ^ {n} \alpha^ {i _ {k} j _ {k}} \left(\prod_ {k = 1} ^ {n} \partial_ {i _ {k}}\right) (f) \times \left(\prod_ {k = 1} ^ {n} \partial_ {j _ {k}}\right) (g) . \end{array}
$$

Here and later symbol denotes the usual product.

## 1.4.2. Deformation quantization up to the second order

Let$\begin{array} { r } { \alpha = \sum _ { i , j } \alpha ^ { i j } \partial _ { i } \wedge \partial _ { j } } \end{array}$be a Poisson bracket with variable coeficients in an open domain of$\mathbf { R } ^ { d } ~ ( \mathrm { i . e }$ $\alpha ^ { i j }$is not a constant, but a function of coordinates), then the following formula gives an associative product modulo$O ( \hbar ^ { 3 } )$):

$$
\begin{array}{l} f \star g = f g + \hbar \sum_ {i, j} \alpha^ {i j} \partial_ {i} (f) \partial_ {j} (g) + \frac {\hbar^ {2}}{2} \sum_ {i, j, k, l} \alpha^ {i j} \alpha^ {k l} \partial_ {i} \partial_ {k} (f) \partial_ {j} \partial_ {l} (g) + \\ + \frac {\hbar^ {2}}{3} \left(\sum_ {i, j, k, l} \alpha^ {i j} \partial_ {j} (\alpha^ {k l}) (\partial_ {i} \partial_ {k} (f) \partial_ {l} (g) - \partial_ {k} (f) \partial_ {i} \partial_ {l} (g))\right) + O (\hbar^ {3}) \end{array}
$$

The associativity up to the second order means that for any 3 functions$f , g , h$one has

$$
(f \star g) \star h = f \star (g \star h) + O (\hbar^ {3}).
$$

## 1.5. Remarks

In general, one should consider bidiferential operators$B _ { i }$with complex coeficients, as we expect to associate by quantization self-adjoint operators in a Hilbert space to real-valued classical observables. In this paper we deal with purely formal algebraic properties of the deformation quantization and work mainly over the field R of real numbers.

Also, it is not clear whether the “deformation quantization” is natural for quantum mechanics. This question we will discuss in the next paper. A topological open string theory seems to be more relevant.

## 2. Explicit universal formula

Here we propose a formula for the star-product for arbitrary Poisson structure α in an open domain of the standard coordinate space$\mathbf { R } ^ { d }$. Terms of our formula modulo$O ( \hbar ^ { 3 } )$are the same as in the previous section, plus a gauge-trivial term of order$O ( \hbar ^ { 2 } )$, symmetric in$f$and$g .$Terms of the formula are certain universal polydiferential operators applied to coeficients of the bi-vector field α and to functions$f , g .$. All indices corresponding to coordinates in the formula appear once as lower indices and once as upper indices, i.e. the formula is invariant under afine transformations of$\mathbf { R } ^ { d }$

In order to describe terms proportional to$\hbar ^ { n }$for any integer$n \geq 0$, we introduce a special class$G _ { n }$of oriented labeled graphs.

Definition. An (oriented) graph Γ is a pair$( V _ { \Gamma } , E _ { \Gamma } )$of two finite sets such that$E _ { \Gamma }$is a subset of$V _ { \Gamma } \times V _ { \Gamma }$

Elements of$V _ { \Gamma }$are vertices of Γ, elements of$E _ { \Gamma }$are edges of Γ. If$e = ( v _ { 1 } , v _ { 2 } ) \in E _ { \Gamma } \subseteq V _ { \Gamma } \times V _ { \Gamma }$is an edge then we say that e starts at$v _ { 1 }$and ends at$v _ { 2 } .$

In the usual definition of graphs one admits infinite graphs, and also graphs with multiple edges. Here we will not meet such structures and use a simplified terminology.

We say that a labeled graph Γ belongs to$G _ { n } { \mathrm { ~ i f ~ } }$

1) Γ has$n + 2$vertices and 2n edges,

2) the set vertices$V _ { \Gamma }$is$\{ 1 , . . . , n \} \sqcup \{ L , R \}$, where$L , R$are just two symbols (capital roman letters, mean Left and Right),

3) edges of Γ are labeled by symbols$e _ { 1 } ^ { 1 } , e _ { 1 } ^ { 2 } , e _ { 2 } ^ { 1 } , e _ { 2 } ^ { 2 } , \ldots , e _ { n } ^ { 1 } , e _ { n } ^ { 2 }$

4) for every$k \in \{ 1 , \ldots , n \}$edges labeled by$e _ { k } ^ { 1 }$and$e _ { k } ^ { 2 }$start at the vertex$k ,$

5) for any$v \in V _ { \Gamma }$the ordered pair$( v , v )$is not an edge of Γ.

The set$G _ { n }$is finite, it has$\left( n ( n + 1 ) \right) ^ { n }$elements for$n \geq 1$and 1 element for$n = 0$

To each labeled graph$\Gamma \in G _ { n }$we associate a bidiferential operator

$$
B _ {\Gamma , \alpha}: A \times A \longrightarrow A, \quad A = C ^ {\infty} (\mathcal {V}), \mathcal {V} \text {is an open domain in} \mathbf {R} ^ {d}
$$

which depends on bi-vector field$\alpha \in \Gamma ( \mathcal { V } , \wedge ^ { 2 } T _ { \mathcal { V } } )$, not necessarily a Poisson one. We show one example, from which the general rule should be clear. Here$n = 3$and the list of edges is

$$
\left(e _ {1} ^ {1}, e _ {1} ^ {2}, e _ {2} ^ {1}, e _ {2} ^ {2}, e _ {3} ^ {1}, e _ {3} ^ {2}\right) = \left((1, L), (1, R), (2, R), (2, 3), (3, L), (3, R)\right).
$$

![](images/page_4_image_14.jpg)

In the picture of$\Gamma$we put independent indices$1 \leq i _ { 1 } , \ldots , i _ { 6 } \leq d$on edges, instead of labels$e _ { * } ^ { * }$. The operator$B _ { \Gamma , \alpha }$corresponding to this graph is

$$
(f, g) \mapsto \sum_ {i _ {1}, \dots , i _ {6}} \alpha^ {i _ {1} i _ {2}} \alpha^ {i _ {3} i _ {4}} \partial_ {i _ {4}} (\alpha^ {i _ {5} i _ {6}}) \partial_ {i _ {1}} \partial_ {i _ {5}} (f) \partial_ {i _ {2}} \partial_ {i _ {3}} \partial_ {i _ {6}} (g).
$$

The general formula for the operator$B _ { \Gamma , \alpha }$is

$$
\begin{array}{l} B _ {\Gamma , \alpha} (f, g) := \sum_ {I: E _ {\Gamma} \longrightarrow \{1, \ldots , d \}} \left[ \prod_ {k = 1} ^ {n} \left(\prod_ {e \in E _ {\Gamma}, e = (*, k)} \partial_ {I (e)}\right) \alpha^ {I (e _ {k} ^ {1}) I (e _ {k} ^ {2})} \right] \times \\ \qquad \qquad \qquad \times \left(\prod_ {e \in E _ {\Gamma}, e = (*, L)} \partial_ {I (e)}\right) f \times \left(\prod_ {e \in E _ {\Gamma}, e = (*, R)} \partial_ {I (e)}\right) g. \end{array}
$$

In the next step we associate a weight$W _ { \Gamma } \in \mathbf { R }$with each graph$\Gamma \in G _ { n }$. In order to define it we need an elementary construction from hyperbolic geometry.

Let$p , q , p \neq q$be two points on the standard upper half-plane$\mathcal { H } = \left\{ z \in \mathbf { C } | I m ( z ) > 0 \right\}$endowed with the Lobachevsky metric. We denote by$\phi ^ { h } ( p , q ) \in \mathbf { R } / 2 \pi \mathbf { Z }$the angle at$p$formed by two lines,$l ( p , q )$ and$l ( p , \infty )$passing through$p$and$q ,$and through p and the point  on the absolute. The direction of the measurement of the angle is counterclockwise from$l ( p , \infty )$to$l ( p , q )$. In the notation$\phi ^ { h } ( p , q )$letter h is for harmonic.

![](images/page_5_image_2.jpg)

An easy planimetry shows that one can express angle$\phi ^ { h } ( p , q )$in terms of complex numbers:

$$
\phi^ {h} (p, q) = A r g ((q - p) / (q - \overline {{p}})) = \frac {1}{2 i} L o g \left(\frac {(q - p) (\overline {{q}} - p)}{(q - \overline {{p}}) (\overline {{q}} - \overline {{p}})}\right).
$$

Function$\phi ^ { h } ( p , q )$can be defined by continuity also in the case$p , q \in \mathcal { H } \sqcup \mathbf { R } , \ p \neq q .$

Denote by$\mathcal { H } _ { n }$the space of configurations of n numbered pairwise distinct points on$\mathcal { H } \colon$

$$
\mathcal {H} _ {n} = \left\{\left(p _ {1}, \dots , p _ {n}\right) \mid p _ {k} \in \mathcal {H}, p _ {k} \neq p _ {l} \text {for} k \neq l \right\}.
$$

$\mathcal { H } _ { n } \subset \mathbf { C } ^ { n }$is a non-compact smooth 2n-dimensional manifold. We introduce orientation on$\mathcal { H } _ { n }$using the natural complex structure on it.

If$\Gamma \in G _ { n }$is a graph as above, and$( p _ { 1 } , \ldots , p _ { n } ) \in { \mathcal { H } } _ { n }$is a configuration of points, then we draw a copy of Γ on the plane$\mathbf { R } ^ { 2 } \simeq \mathbf { C }$by assigning point$p _ { k } \in \mathcal { H }$to the vertex k,$1 \leq k \leq n$, point$0 \in { \mathbf { R } } \subset { \mathbf { C } }$to the vertex$L ,$, and point$1 \in \mathbf { R } \subset \mathbf { C }$to the vertex R. Each edge should be drawn as a line interval in hyperbolic geometry. Every edge e of the graph Γ defines an ordered pair$( p , q )$of points on${ \mathcal { H } } \sqcup \mathbf { R }$, thus an angle $\phi _ { e } ^ { h } : = \phi ^ { h } ( p , q )$. If points$p _ { i }$move around, we get a function$\phi _ { e } ^ { h }$on$\mathcal { H } _ { n }$with values in$\mathbf { R } / 2 \pi \mathbf { Z }$

We define the weight of Γ as

$$
w _ {\Gamma} := \frac {1}{n ! (2 \pi) ^ {2 n}} \int_ {\mathcal {H} _ {n}} \bigwedge_ {i = 1} ^ {n} (d \phi_ {e _ {k} ^ {1}} ^ {h} \wedge d \phi_ {e _ {k} ^ {2}} ^ {h}) .
$$

Lemma. The integral in the definition of$w _ { \Gamma }$is absolutely convergent.

This lemma is a particular case of a more general statement proven in section 6.

Theorem. Let α be a Poisson bi-vector field in a domain of$\mathbf { R } ^ { d }$. The formula

$$
f \star g := \sum_ {n = 0} ^ {\infty} \hbar^ {n} \sum_ {\Gamma \in G _ {n}} w _ {\Gamma} B _ {\Gamma , \alpha} (f, g)
$$

defines an associative product. If we change coordinates, we obtain a gauge equivalent star-product.

The proof of this theorem is elementary, it uses only the Stokes formula. Again, this theorem is a corollary of a more general statement proven in section 6.

## 3. Deformation theory via diferential graded Lie algebras

## 3.1. Tensor categories Super and Graded

Here we make a comment about the terminology. This comment looks a bit pedantic, but it could help in the struggle with signs in formulas.

The main idea of algebraic geometry is to replace spaces by commutative associative rings (at least locally). One can further generalize this considering commutative associative algebras in general tensor categories$\left( \mathrm { s e e } \left[ \mathrm { D e } \right] \right)$. In this way one can imitate many constructions from algebra and diferential geometry.

The fundamental example is supermathematics, i.e. mathematics in the tensor category$S u p e r ^ { \mathbf { k } }$of super vector spaces over a field k of characteristic zero (see Chapter 3 in [M]). The category$S u p e r ^ { \mathbf { k } }$is the category of$\mathbf { Z } / 2 \mathbf { Z }$-graded vector spaces over k (representations of the group$\mathbf { Z } / 2 \mathbf { Z } )$endowed with the standard tensor product, with the standard associativity functor, and with a modified commutativity functor (the Koszul rule of signs). We denote by Π the usual functor$S u p e r ^ { \mathbf { k } } { \longrightarrow } S u p e r ^ { \mathbf { k } }$changing the parity. It is given on objects by the formula$\Pi V = V \otimes \mathbf { k } ^ { 0 | 1 }$. In the sequel we will consider the standard tensor category$V e c t ^ { \mathbf { k } }$of vector spaces over k as the subcategory of$S u p e r ^ { \mathbf { k } }$consisting of pure even spaces.

The basic tensor category which appears everywhere in topology and homological algebra is a full subcategory of the tensor category of Z-graded super vector spaces. Objects of this category are infinite sums$\mathcal { E } = \oplus _ { n \in \mathbf { Z } } \mathcal { E } ^ { ( n ) }$such that$\bar { \mathcal { E } ^ { ( n ) } }$is pure even for even n, and pure odd for odd n. We will slightly abuse the language calling this category also the category of graded vector spaces, and denote it simply by$G r a d e d ^ { \mathbf { k } }$ We denote by${ \mathcal { E } } ^ { n }$the usual k-vector space underlying the graded component${ \mathcal { E } } ^ { ( n ) }$. The super vector space obtained if we forget about$\mathbf { Z } \mathbf { \cdot }$-grading on$\mathcal { E } \in O b j e c t s ( G r a d e d ^ { \mathbf { k } } )$is$\textstyle \bigoplus _ { n \in \mathbf { Z } } \Pi ^ { n } ( { \mathcal { E } } ^ { n } )$

Analogously, we will speak about graded manifolds. They are defined as supermanifolds endowed with Z-grading on the sheaf of functions obeying the same conditions on the parity as above.

The shift functor$[ 1 ] : G r a d e d ^ { \mathbf { k } } { \longrightarrow } G r a d e d ^ { \mathbf { k } }$(acting from the$\mathrm { r i g h t } )$is defined as the tensor product with graded space$\mathbf { k } [ 1 ]$where$\mathbf { k } [ 1 ] ^ { - 1 } \simeq \mathbf { k } , \mathbf { k } [ 1 ] ^ { \neq - 1 } = \dot { 0 }$. Its powers are denoted by [n],$\mathbf { \psi } _ { n } \in \mathbf { Z }$. Thus, for graded space$\mathcal { E }$we have

$$
\mathcal {E} = \bigoplus_ {n \in \mathbf {Z}} \mathcal {E} ^ {n} [ - n ].
$$

Almost all results in the present paper formulated for graded manifolds, graded Lie algebras etc., hold also for supermanifolds, super Lie algebras etc.

## 3.2. Maurer-Cartan equation in diferential graded Lie algebras

This part is essentially standard (see [GM], [HS1], [SS], ...).

Let g be a diferential graded Lie algebra over field k of characteristic zero. Below we recall the list of structures and axioms:

$$
\mathbf {g} = \bigoplus_ {k \in \mathbf {Z}} \mathbf {g} ^ {k} [ - k ], \quad [ , ]: \mathbf {g} ^ {k} \otimes \mathbf {g} ^ {l} \longrightarrow \mathbf {g} ^ {k + l}, \quad d: \mathbf {g} ^ {k} \longrightarrow \mathbf {g} ^ {k + 1},
$$

$$
d (d (\gamma)) = 0, d [ \gamma_ {1}, \gamma_ {2} ] = [ d \gamma_ {1}, \gamma_ {2} ] + (- 1) ^ {\overline {{\gamma_ {1}}}} [ \gamma_ {1}, d \gamma_ {2} ], [ \gamma_ {2}, \gamma_ {1} ] = - (- 1) ^ {\overline {{\gamma_ {1}}} \cdot \overline {{\gamma_ {2}}}} [ \gamma_ {1}, \gamma_ {2} ],
$$

$$
[ \gamma_ {1}, [ \gamma_ {2}, \gamma_ {3} ] ] + (- 1) ^ {\overline {{\gamma_ {3}}} \cdot (\overline {{\gamma_ {1}}} + \overline {{\gamma_ {2}}})} [ \gamma_ {3}, [ \gamma_ {1}, \gamma_ {2} ] ] + (- 1) ^ {\overline {{\gamma_ {1}}} \cdot (\overline {{\gamma_ {2}}} + \overline {{\gamma_ {3}}})} [ \gamma_ {2}, [ \gamma_ {3}, \gamma_ {1} ] ] = 0.
$$

In formulas above symbols${ \overline { { \gamma _ { i } } } } \in \mathbf { Z }$mean the degrees of homogeneous elements$\gamma _ { i } .$, i.e.$\gamma _ { i } \in \mathbf { g } ^ { \overline { { \gamma _ { i } } } } .$

In other words,$\mathbf { g }$is a Lie algebra in the tensor category of complexes of vector spaces over k. If we forget about the diferential and the grading on g, we obtain a Lie superalgebra.

We associate with g a functor$D e f _ { \mathbf { g } }$on the category of finite-dimensional commutative associative algebras over k, with values in the category of sets. First of all, let us assume that g is a nilpotent Lie superalgebra. We define set$\mathcal { M } \mathcal { C } ( \mathbf { g } )$(the set of solutions of the Maurer-Cartan equation modulo the gauge equivalence) by the formula

$$
\mathcal {M C} (\mathbf {g}) := \left\{\gamma \in \mathbf {g} ^ {1} | d \gamma + \frac {1}{2} [ \gamma , \gamma ] = 0 \right\} / \Gamma^ {0}
$$

where$\Gamma ^ { 0 }$is the nilpotent group associated with the nilpotent Lie algebra$\mathbf { g } ^ { 0 }$. The group Γ acts by afine transformations of the vector space$\mathbf { g } ^ { 1 }$. The action of$\Gamma ^ { 0 }$is defined by the exponentiation of the infinitesimal action of its Lie algebra:

$$
\alpha \in \mathbf {g} ^ {0} \mapsto (\dot {\gamma} = d \alpha + [ \alpha , \gamma ]) .
$$

Now we are ready to introduce functor$D e f _ { \mathbf { g } }$. Technically, it is convenient to define this functor on the category of finite-dimensional nilpotent commutative associative algebras without unit. Let m be such an algebra,$\mathbf { m } ^ { d i m ( \mathbf { m } ) + 1 } = 0$. The functor is given (on objects) by the formula

$$
D e f _ {\mathbf {g}} (\mathbf {m}) = \mathcal {M C} (\mathbf {g} \otimes \mathbf {m}).
$$

In the conventional approach m is the maximal ideal in a finite-dimensional Artin algebra with unit

$$
\mathbf {m} ^ {\prime} := \mathbf {m} \oplus \mathbf {k} \cdot 1.
$$

In general, one can think about commutative associative algebras without unit as about objects dual to spaces with base points. Algebra corresponding to a space with base point is the algebra of functions vanishing at the base point.

One can extend the definition of the deformation functor to algebras with linear topology which are projective limits of nilpotent finite-dimensional algebras. For example, in the deformation quantization we use the following algebra over R:

$$
\mathbf {m} := \hbar \mathbf {R} [ [ \hbar ] ] = \lim _ {\leftarrow} \left(\hbar \mathbf {R} [ \hbar ] / \hbar^ {k} \mathbf {R} [ \hbar ]\right) \text {as} k \to \infty .
$$

## 3.3. Remark

Several authors, following a suggestion of P. Deligne, stressed that the set$D e f _ { \mathbf { g } } ( \mathbf { m } )$should be considered as the set of equivalence classes of a natural groupoid. Almost always in deformation theory, diferential graded Lie algebras are supported in non-negative degrees,$\mathbf { g } ^ { < 0 } = 0 .$. Our principal example in the present paper, the shifted Hochschild complex (see the next subsection), has a non-trivial component in degree 1, when it is considered as a graded Lie algebra. The set$D e f _ { \mathbf { g } } ( \mathbf { m } )$in such a case has a natural structure of the set of equivalence classes of a 2-groupoid. In general, if one considers diferential graded Lie algebras with components in negative degrees, one meets immediately polycategories and nilpotent homotopy types. Still, it is only a half of the story because one can not say anything about$\mathbf { g } ^ { \geq 3 }$using this language. Maybe, the better way is to extend the definition of the deformation functor to the category of diferential graded nilpotent commutative associative algebras, see the last remark in 4.5.2.

## 3.4. Examples

There are many standard examples of diferential graded Lie algebras and related moduli problems.

## 3.4.1. Tangent complex

Let X be a complex manifold. Define g over C as

$$
\mathbf {g} = \bigoplus_ {k \in \mathbf {Z}} \mathbf {g} ^ {k} [ - k ]; \quad \mathbf {g} ^ {k} = \Gamma (X, \Omega_ {X} ^ {0, k} \otimes T _ {X} ^ {1, 0}) \text {for} k \geq 0, \quad \mathbf {g} ^ {<   0} = 0
$$

with the diferential equal to${ \overline { { \partial } } } ,$and the Lie bracket coming from the cup-product on$\overline { { \partial } } .$forms and the usual Lie bracket on holomorphic vector fields.

The deformation functor related with g is the usual deformation functor for complex structures on$X$ The set$D e f _ { \mathbf { g } } ( \mathbf { m } )$can be naturally identified with the set of equivalence classes of analytic spaces$\widetilde { X }$endowed with a flat map$p : \widetilde { X } \longrightarrow S p e c ( \mathbf { m } ^ { \prime } )$, and an identification$i : \tilde { X } \times _ { S p e c ( \mathbf { m } ^ { \prime } ) } S p e c ( \mathbf { C } ) \simeq X$eof the special fiber of $p$with X.

## 3.4.2. Hochschild complex

Let A be an associative algebra over field k of characteristic zero. The graded space of Hochschild cochains of A with coeficients in A considered as a bimodule over itself is

$$
C ^ {\bullet} (A, A) := \bigoplus_ {k \geq 0} C ^ {k} (A, A) [ - k ], C ^ {k} (A, A) := H o m _ {V e c t ^ {\mathbf {k}}} (A ^ {\otimes k}, A).
$$

We define graded vector space g over k by formula$\mathbf { g } : = C ^ { \bullet } ( A , A ) [ 1 ]$. Thus, we have

$$
\mathbf {g} = \bigoplus_ {k \in \mathbf {Z}} \mathbf {g} ^ {k} [ - k ]; \quad \mathbf {g} ^ {k} := H o m (A ^ {\otimes (k + 1)}, A) \text { for } k \geq - 1, \quad \mathbf {g} ^ {<   (- 1)} = 0.
$$

The diferential in$\mathbf { g }$is shifted by 1 the usual diferential in the Hochschild complex, and the Lie bracket is the Gerstenhaber bracket. The explicit formulas for the diferential and for the bracket are:

$$
\begin{array}{c} (d \Phi) (a _ {0} \otimes \ldots \otimes a _ {k + 1}) = a _ {0} \cdot \Phi (a _ {1} \otimes \ldots \otimes a _ {k + 1}) - \sum_ {i = 0} ^ {k} (- 1) ^ {i} \Phi (a _ {0} \otimes \ldots \otimes (a _ {i} \cdot a _ {i + 1}) \otimes \ldots \otimes a _ {k + 1}) + \\ + (- 1) ^ {k} \Phi (a _ {0} \otimes \ldots \otimes a _ {k}) \cdot a _ {k + 1}, \quad \Phi \in \mathbf {g} ^ {k}, \end{array}
$$

and

$$
\left[ \Phi_ {1}, \Phi_ {2} \right] = \Phi_ {1} \circ \Phi_ {2} - (- 1) ^ {k _ {1} k _ {2}} \Phi_ {2} \circ \Phi_ {1}, \quad \Phi_ {i} \in \mathbf {g} ^ {k _ {i}},
$$

where the (non-associative) product is defined as

$$
\begin{array}{c} (\Phi_ {1} \circ \Phi_ {2}) (a _ {0} \otimes \ldots \otimes a _ {k _ {1} + k _ {2}}) = \\ = \sum_ {i = 0} ^ {k _ {1}} (- 1) ^ {i k _ {2}} \Phi_ {1} (a _ {0} \otimes \ldots \otimes a _ {i - 1} \otimes (\Phi_ {2} (a _ {i} \otimes \ldots \otimes a _ {i + k _ {2}})) \otimes a _ {i + k _ {2} + 1} \otimes \ldots \otimes a _ {k _ {1} + k _ {2}}) . \end{array}
$$

We would like to give here also an abstract definition of the diferential and of the bracket on$\mathbf { g } .$Let$F$ denote the free coassociative graded coalgebra with counit cogenerated by the graded vector space A[1]:

$$
F = \bigoplus_ {n \geq 1} \otimes^ {n} (A [ 1 ]) .
$$

Graded Lie algebra$\mathbf { g }$is the Lie algebra of coderivations of$F$in the tensor category$G r a d e d ^ { \mathbf { k } }$. The associative product on$A$gives an element m$A \in { \bf g } ^ { 1 }$, m$\mathbf { \delta } _ { A } : A \otimes A { \longrightarrow } A$satisfying the equation$[ m _ { A } , m _ { A } ] = 0$ The diferential d in$\mathbf { g }$is defined as$a d ( m _ { A } )$

Again, the deformation functor related to g is equivalent to the usual deformation functor for algebraic structures. Associative products on A correspond to solutions of the Maurer- Cartan equation in$\mathbf { g } .$The set $D e f _ { \mathbf { g } } ( \mathbf { m } )$is naturally identified with the set of equivalence classes of pairs$( \widetilde { A } , i )$where$\widetilde { A }$is an associative algebra over$\mathbf { m } ^ { \prime } = \mathbf { m } \oplus \mathbf { k } \cdot \mathbf { \mathrm { 1 } }$such that$\widetilde { A }$e eis free as an m′-module, and i an isomorphism of k-algebras $\overset { \triangledown } { \boldsymbol { A } } \otimes _ { \mathbf { m ^ { \prime } } } \mathbf { k } \simeq \boldsymbol { A }$

The cohomology of the Hochschild complex are

$$
H H ^ {k} (A, A) = E x t _ {A - m o d - A} ^ {k} (A, A),
$$

the Ext-groups in the abelian category of bimodules over A. The Hochschild complex without shift by 1 also has a meaning in deformation theory, it is responsible for deformations of A as a bimodule.

## 4. Homotopy Lie algebras and quasi-isomorphisms

In this section we introduce a language convenient for the homotopy theory of diferential graded Lie algebras and for the deformation theory. The ground field k for linear algebra in our discussion is an arbitrary field of characteristic zero, unless specified.

## 4.1. Formal manifolds

Let V be a vector space. We denote by$C ( V )$the cofree cocommutative coassociative coalgebra without counit cogenerated by$V { : }$

$$
C (V) = \bigoplus_ {n \geq 1} \left(\otimes^ {n} V\right) ^ {\Sigma_ {n}} \subset \bigoplus_ {n \geq 1} \left(\otimes^ {n} V\right).
$$

Intuitively, we think about$C ( V )$as about an object corresponding to a formal manifold, possibly infinite-dimensional, with base point:

$$
\left(V _ {\text { formal }}, \text {   base   point }\right) := \left(\text { Formal   neighborhood   of   zero   in   } V, 0\right).
$$

The reason for this is that if V is finite-dimensional then$C ( V ) ^ { * }$(the dual space to$C ( V ) )$is the algebra of formal power series on V vanishing at the origin.

Definition. A formal pointed manifold M is an object corresponding to a coalgebra which is isomorphic to$C ( V )$for some vector space V.

The specific isomorphism between and$C ( V )$is not considered as a part of data. Nevertheless, the vector space V can be reconstructed from M as the space of primitive elements in coalgebra . Speaking geometrically, V is the tangent space to M at the base point. A choice of an isomorphism between$\mathcal { C }$and $C ( V )$can be considered as a choice of an afine structure on M.

If$V _ { 1 }$and$V _ { 2 }$are two vector spaces then a map$f$between corresponding formal pointed manifolds is defined as a homomorphism of coalgebras (the pushforward on distributions supported at zero)

$$
f _ {*}: C (V _ {1}) \longrightarrow C (V _ {2}).
$$

By the universal property of cofree coalgebras any such homomorphism is uniquely specified by a linear map

$$
C (V _ {1}) \longrightarrow V _ {2}
$$

which is the composition of$f _ { * }$with the canonical projection$C ( V _ { 2 } ) { \longrightarrow } V _ { 2 }$. Homogeneous components of this map,

$$
f ^ {(n)}: \left(\otimes^ {n} (V _ {1})\right) ^ {\Sigma_ {n}} \longrightarrow V _ {2}, n \geq 1
$$

can be considered as Taylor coeficients of$f .$. More precisely, Taylor coeficients are defined as maps

$$
\partial^ {n} f: S y m ^ {n} (V _ {1}) \longrightarrow V _ {2}, \quad \partial^ {n} f (v _ {1} \cdot \ldots \cdot v _ {n}) := \frac {\partial^ {n}}{\partial t _ {1} \ldots \partial t _ {n}}   | _ {t _ {1} = \ldots = t _ {n} = 0}   (f (t _ {1} v _ {1} + \ldots + t _ {n} v _ {n}))    .
$$

Linear map$f ^ { ( n ) }$coincides with$\partial ^ { n } f$after the identification of the subspace$\left( \otimes ^ { n } V _ { 1 } \right) ^ { \Sigma _ { n } } \subset \otimes ^ { n } V _ { 1 }$with the quotient space

$$
S y m ^ {n} (V _ {1}) := \otimes^ {n} V _ {1} / \{s t a n d a r d r e l a t i o n s \}
$$

As in the usual calculus, there is the inverse mapping theorem: non-linear map$f$is invertible if its first Taylor coeficient$f ^ { ( 1 ) } : V _ { 1 } { \longrightarrow } V _ { 2 }$is invertible.

Analogous definitions and statements can be made in other tensor categories, including$S u p e r ^ { \mathbf { k } }$and $G r a d e d ^ { \mathbf { k } }$

The reader can ask why we speak about base points for formal manifolds, as such manifolds have only one geometric point. The reason is that later we will consider formal graded manifolds depending on formal parameters. In such a situation the choice of the base point is an essential part of the structure.

## 4.2. Pre-L<sub>∞</sub>-morphisms

Let$\mathbf { g } _ { 1 }$and$\mathbf { g } _ { 2 }$be two graded vector spaces.

Definition.$A \ p r e - L _ { \infty } . _ { \mathit { m o r p h i s m } } \mathcal { F }$from g to g is a map of formal pointed graded manifolds

$$
\mathcal {F}: \big ((\mathbf {g} _ {1} [ 1 ]) _ {f o r m a l}, 0 \big) \longrightarrow \big ((\mathbf {g} _ {2} [ 1 ]) _ {f o r m a l}, 0 \big) .
$$

Map$\mathcal { F }$is defined by its Taylor coeficients which are linear maps$\partial ^ { n } { \mathcal { F } }$of graded vector spaces:

$$
\partial^ {1} \mathcal {F}: \mathbf {g} _ {1} {\longrightarrow} \mathbf {g} _ {2}
$$

$$
\partial^ {2} \mathcal {F}: \wedge^ {2} (\mathbf {g} _ {1}) \longrightarrow \mathbf {g} _ {2} [ - 1 ]
$$

$$
\partial^ {3} \mathcal {F}: \wedge^ {3} (\mathbf {g} _ {1}) {\longrightarrow} \mathbf {g} _ {2} [ - 2 ]
$$

Here we use the natural isomorphism$S y m ^ { n } ( \mathbf { g } _ { 1 } [ 1 ] ) \simeq \left( \wedge ^ { n } ( \mathbf { g } _ { 1 } ) \right) [ n ]$. In plain terms, we have a collection of linear maps between ordinary vector spaces

$$
\mathcal {F} _ {(k _ {1}, \dots , k _ {n})}: \mathbf {g} _ {1} ^ {k _ {1}} \otimes \dots \otimes \mathbf {g} _ {1} ^ {k _ {n}} \longrightarrow \mathbf {g} _ {2} ^ {k _ {1} + \dots + k _ {n} + (1 - n)}
$$

with the symmetry property

$$
\mathcal {F} _ {(k _ {1}, \ldots , k _ {n})} (\gamma_ {1} \otimes \ldots \otimes \gamma_ {n}) = - (- 1) ^ {k _ {i} k _ {i + 1}} \mathcal {F} _ {(k _ {1}, \ldots , k _ {i + 1}, k _ {i}, \ldots , k _ {n})} (\gamma_ {1} \otimes \ldots \otimes \gamma_ {i + 1} \otimes \gamma_ {i} \otimes \ldots \otimes \gamma_ {n}).
$$

One can write (slightly abusing notations)

$$
\partial^ {n} \mathcal {F} (\gamma_ {1} \wedge \dots \wedge \gamma_ {n}) = \mathcal {F} _ {(k _ {1}, \dots , k _ {n})} (\gamma_ {1} \otimes \dots \otimes \gamma_ {n})
$$

for$\gamma _ { i } \in \mathbf { g } _ { 1 } ^ { k _ { i } } , ~ i = 1 , \ldots , n .$

In the sequel we will denote$\partial ^ { n } { \mathcal { F } }$simply by${ \mathcal { F } } _ { n }$.

## 4.3. L<sub>∞</sub>-algebras and L<sub>∞</sub>-morphisms

Suppose that we have an odd vector field$Q$of degree +1 on formal graded manifold$( \mathbf { g } [ 1 ] _ { f o r m a l } , 0 )$such that the Taylor series for coeficients of Q has terms of degree 1 and 2 only. The first Taylor coeficient$Q _ { 1 }$ gives a linear map$\mathbf { g } \longrightarrow \mathbf { g }$of degree +1 (or, better, a map$\mathbf { g } { \longrightarrow } \mathbf { g } [ 1 ] )$. The second coeficien$Q ^ { 2 } : \wedge ^ { 2 } { \bf g } { \longrightarrow } { \bf g }$ gives a skew-symmetric bilinear operation of degree 0 on g.

It is easy to see that${ \mathrm { i f ~ } } [ Q , Q ] = 0$then g is a diferential graded Lie algebra, with diferential$Q _ { 1 }$and the bracket$Q _ { 2 }$, and vice versa.

In paper [AKSZ] supermanifolds endowed with an odd vector field$Q$such that$[ Q , Q ] = 0$, are called Q-manifolds. By analogy, we can speak about formal graded pointed Q-manifolds.

Definition. An$L _ { \infty }$-algebra is a pair$( \mathbf { g } , Q )$where g is a graded vector space and$Q$is a diferential of degree $+ 1$on the graded coalgebra$C ( \mathbf { g } )$

Other names for$L _ { \infty }$-algebras are “(strong) homotopy Lie algebras” and “Sugawara algebras” (see$\mathrm { e . g . }$ [HS2]).

Usually we will denote L<sub>∞</sub>-algebra$( \mathbf { g } , Q )$simply by$\mathbf { g } .$

The structure of an$L _ { \infty }$-algebra on a graded vector space g is given by the infinite sequence of Taylor coeficients$Q _ { i }$of the odd vector field$Q$(coderivation of$C ( \mathbf { g } ) )$

$$
Q _ {1}: \mathbf {g} \longrightarrow \mathbf {g} [ 1 ]
$$

$$
\begin{array}{c} Q _ {2}: \wedge^ {2} (\mathbf {g}) \longrightarrow \mathbf {g} \\ Q _ {3}: \wedge^ {3} (\mathbf {g}) \longrightarrow \mathbf {g} [ - 1 ] \end{array}
$$

The condition$Q ^ { 2 } = 0$can be translated into an infinite sequence of quadratic constraints on polylinear maps$Q _ { i }$. First of these constraints means that$Q _ { 1 }$is the diferential of the graded space$\mathbf { g } .$. Thus,$( \mathbf { g } , Q _ { 1 } )$ is a complex of vector spaces over k. The second constraint means that$Q _ { 2 }$is a skew-symmetric bilinear operation on g, for which$Q _ { 1 }$satisfies the Leibniz rule. The third constraint means that$Q _ { 2 }$satisfies the Jacobi identity up to homotopy given by$Q _ { 3 }$, etc. As we have seen, a diferential graded Lie algebra is the same as an$L _ { \infty } { - } \mathrm { a }$lgebra with$Q _ { 3 } = Q _ { 4 } = . . . = 0$

Nevertheless, we recommend to return to the geometric point of view and think in terms of formal graded Q-manifolds. This naturally leads to the following

Definition. An$L _ { \infty }$-morphism between two$L _ { \infty }$-algebras$\mathbf { g } _ { 1 }$and$\mathbf { g } _ { 2 }$is a pre-$. L _ { \infty }$-morphism$\mathcal { F }$such that the associated morphism$\mathcal { F } _ { * } : C ( \mathbf { g } _ { 1 } [ 1 ] ) { \longrightarrow } C ( \mathbf { g } _ { 2 } [ 1 ] )$of graded cocommutative coalgebras, is compatible with codiferentials.

In geometric terms, an$L _ { \infty }$-morphism corresponds to a Q-equivariant map between two formal graded manifolds with base points.

For the case of diferential graded Lie algebras a pre-$. L _ { \infty }$-morphism$\mathcal { F }$is an$L _ { \infty }$-morphism if it satisfies the following equation for any$n = 1 , 2 \dots$. and homogeneous elements$\gamma _ { i } \in { \bf g } _ { 1 }$

$$
\begin{array}{c} d \mathcal {F} _ {n} (\gamma_ {1} \wedge \gamma_ {2} \wedge \ldots \wedge \gamma_ {n}) - \sum_ {i = 1} ^ {n} \pm \mathcal {F} _ {n} (\gamma_ {1} \wedge \ldots \wedge d \gamma_ {i} \wedge \ldots \wedge \gamma_ {n}) = \\ = \frac {1}{2} \sum_ {k, l \geq 1, k + l = n} \frac {1}{k ! l !} \sum_ {\sigma \in \Sigma_ {n}} \pm [ \mathcal {F} _ {k} (\gamma_ {\sigma_ {1}} \wedge \ldots \wedge \gamma_ {\sigma_ {k}}), \mathcal {F} _ {l} (\gamma_ {\sigma_ {k + 1}} \wedge \ldots \wedge \gamma_ {\sigma_ {n}}) ] + \sum_ {i <   j} \pm \mathcal {F} _ {n - 1} ([ \gamma_ {i}, \gamma_ {j} ] \wedge \gamma_ {1} \wedge \ldots \wedge \gamma_ {n}). \end{array}
$$

Here are first two equations in the explicit form:

$$
d \mathcal {F} _ {1} (\gamma_ {1}) = \mathcal {F} _ {1} (d \gamma_ {1}),
$$

$$
d \mathcal {F} _ {2} (\gamma_ {1} \wedge \gamma_ {2}) - \mathcal {F} _ {2} (d \gamma_ {1} \wedge \gamma_ {2}) - (- 1) ^ {\overline {{\gamma_ {1}}}} \mathcal {F} _ {2} (\gamma_ {1} \wedge d \gamma_ {2}) = \mathcal {F} _ {1} ([ \gamma_ {1}, \gamma_ {2} ]) - [ \mathcal {F} _ {1} (\gamma_ {1}), \mathcal {F} _ {1} (\gamma_ {2}) ] .
$$

We see that$\mathcal { F } _ { 1 }$is a morphism of complexes. The same is true for the case of general$L _ { \infty } \mathrm { - a l g e b r a s . }$. The graded space$\mathbf { g }$for an L<sub>∞</sub>-algebra$( \mathbf { g } , Q )$can be considered as the tensor product of$\mathbf { k } [ - 1 ]$with the tangent space to the corresponding formal graded manifold at the base point. The diferential$Q _ { 1 }$on g comes from the action of$Q$on the manifold.

Let us assume that$\mathbf { g } _ { 1 }$and$\mathbf { g } _ { 2 }$are diferential graded Lie algebras, and$\mathcal { F }$is an$L _ { \infty }$-morphism from g<sub>1</sub> to g . Any solution$\gamma \in { \bf g } _ { 1 }$m of the Maurer-Cartan equation where m is a nilpotent non-unital algebra, produces a solution of the Maurer-Cartan equation in$\mathbf { g } _ { 2 } \otimes \mathbf { m } \mathrm { . }$

$$
d \gamma + \frac {1}{2} [ \gamma , \gamma ] = 0 \Longrightarrow d \widetilde {\gamma} + \frac {1}{2} [ \widetilde {\gamma}, \widetilde {\gamma} ] = 0 \quad \text {where} \quad \widetilde {\gamma} = \sum_ {n = 1} ^ {\infty} \frac {1}{n !} \mathcal {F} _ {n} (\gamma \wedge \dots \wedge \gamma) \in \mathbf {g} _ {2} ^ {1} \otimes \mathbf {m}.
$$

The same formula is applicable to solutions of the Maurer-Cartan equation depending formally on parameter$\hbar \mathrm { : }$:

$$
\gamma (\hbar) = \gamma_ {1} \hbar + \gamma_ {2} \hbar^ {2} + \ldots \in \mathbf {g} _ {1} ^ {1} [ [ \hbar ] ], d \gamma (\hbar) + \frac {1}{2} [ \gamma (\hbar), \gamma (\hbar) ] = 0 \Longrightarrow d \widetilde {\gamma (\hbar)} + \frac {1}{2} [ \widetilde {\gamma (\hbar)}, \widetilde {\gamma (\hbar)} ] = 0.
$$

The reason why it works is that the Maurer-Cartan equation in any diferential graded Lie algebra g is the equation for the subscheme of zeroes of$Q$in formal manifold$\mathbf { g } [ 1 ] _ { f o r m a l }$$L _ { \infty } \mathrm { { - m o r p h i s m s } }$map zeroes of Q to zeroes of$Q$because they commute with Q. We will see in 4.5.2 that$L _ { \infty } \mathrm { { - m o r p h i s m s } }$induce natural transformations of deformation functors.

## 4.4. Quasi-isomorphisms

L -morphisms generalize usual morphisms of diferential graded Lie algebras. In particular, the first Taylor coeficient of an$L _ { \infty } \mathrm { { - m o r p h i s m } }$from$\mathbf { g } _ { 1 }$to$\mathbf { g } _ { 2 }$is a morphism of complexes$( { \bf g } _ { 1 } , Q _ { 1 } ^ { ( { \bf g } _ { 1 } ) } ) { \longrightarrow } ( { \bf g } _ { 2 } , Q _ { 1 } ^ { ( { \bf g } _ { 2 } ) } )$ where$Q _ { 1 } ^ { ( \mathbf { g } _ { i } ) }$are the first Taylor coeficients of vector fields$Q ^ { ( \mathbf { g } _ { i } ) }$(which we denoted before simply by$Q )$.

Definition. A quasi-isomorphism is an$L _ { \infty }$-morphism$\mathcal { F }$such that the first component$\mathcal { F } _ { 1 }$induces isomorphism between cohomology groups of complexes$( \mathbf { g } _ { 1 } , Q _ { 1 } ^ { ( \mathbf { g } _ { 1 } ) } )$and$( \mathbf { g } _ { 2 } , Q _ { 1 } ^ { ( \mathbf { g } _ { 2 } ) } )$.

The essence of the homotopy/deformation theory is contained in the following

Theorem. Let$\mathbf { g } _ { 1 } , \mathbf { g } _ { 2 }$be two$L _ { \infty } { \mathrm { - } } a l g e b r a s$and$\mathcal { F }$be an$L _ { \infty }$-morphism from$\mathbf { g } _ { 1 }$to$\mathbf { g } _ { 2 }$. Assume that$\mathcal { F }$is a quasi-isomorphism. Then there exists an$L _ { \infty } .$-morphism from$\mathbf { g } _ { 2 }$to$\mathbf { g } _ { 1 }$inducing the inverse isomorphism between cohomology of complexes$( \mathbf { g } _ { i } , Q _ { 1 } ^ { ( \mathbf { g } _ { i } ) } ) \ i = 1 , 2$Also, for the case of diferential graded algebras, $L _ { \infty } { \mathrm { - } m o r p h i s m ~ } \mathcal { F }$induces an isomorphism between deformation functors associated with$\mathbf { g } _ { i }$

The first part of this theorem shows that if$\mathbf { g } _ { 1 }$is quasi-isomorphic to$\mathbf { g } _ { 2 }$then$\mathbf { g } _ { 2 }$is quasi-isomorphic to $\mathbf { g } _ { 1 }$, i.e. we get an equivalence relation.

The isomorphism between deformation functors at the second part of the theorem is given by last formulas from 4.3.

This theorem is essentially standard (see related results in [GM], [HS1], [SS]). Our approach consists in the translation of all relevant notions to the geometric language of formal graded pointed Q-manifolds.

## 4.5. A sketch of the proof

## 4.5.1. Homotopy classification of$L _ { \infty } { \bf - a l g e b r a s }$

Any complex of vector spaces can be decomposed into the direct sum of a complex with trivial diferential and a contractible complex. There is an analogous decomposition in the non-linear case.

Definition. An$L _ { \infty } { \mathrm { - } a l g } \mathrm { e } b r a \left( \mathbf { g } , Q \right)$is called minimal if the first Taylor coeficient$Q _ { 1 }$of the coderivation Q vanishes.

The property of being formal is invariant under$L _ { \infty }$-isomorphisms. Thus, one can speak about minimal formal graded pointed Q-manifolds.

Definition. An$L _ { \infty } { \mathrm { - } a l g } \mathrm { e } b r a \left( \mathbf { g } , Q \right)$is called linear contractible if higher Taylor coeficients$Q _ { \geq 2 }$vanish and the diferential$Q _ { 1 }$has trivial cohomology.

The property of being linear contractible is not$L _ { \infty } { \mathrm { - i n v a r i a n t } }$. One can call formal graded pointed $Q { \mathrm { - m a n i f o l d } }$contractible if the corresponding diferential graded coalgebra is$L _ { \infty } \mathrm { - i s o m o r p h i c }$to a linear contractible one.

Lemma. Any$L _ { \infty } { \mathrm { - } a l g } \mathrm { e } b r a \left( \mathbf { g } , Q \right)$is$L _ { \infty }$-isomorphic to the direct sum ofa minimal and ofa linear contractible $L _ { \infty } { \mathrm { - } } a l g \mathrm { e } b r a s$

This lemma says that there exists an afine structure on a formal graded pointed manifold in which the odd vector field$Q$has the form of a direct sum of a minimal and a linear contractible one. This afine structure can be constructed by induction in the degree of the Taylor expansion. The base of the induction is the decomposition of the complex$( \mathbf { g } , Q _ { 1 } )$into the direct sum of a complex with vanishing diferential and a complex with trivial cohomology. We leave details of the proof of the lemma to the reader. Q.E.D.

As a side remark, we mention analogy between this lemma and a theorem from singularity theory (see, for example, the beginning of 11.1 in$\mathrm { [ A G V ] } )$: for every germ f of analytic function at critical point one can find local coordinates$( x ^ { 1 } , \ldots , x ^ { k } , y ^ { 1 } , \ldots , y ^ { l } )$such that$f = c o n s t a n t + Q _ { 2 } ( x ) + Q _ { \geq 3 } ( y )$where$Q _ { 2 }$is a nondegenerate quadratic form in x and$Q _ { \geq 3 } ( y )$is a germ of a function in y such that its Taylor expansion at$y = 0$starts at terms of degree at least 3.

Let g be an$L _ { \infty } .$-algebra and$\mathbf { g } ^ { m i n }$be a minimal L<sub>∞</sub>-algebra as in the previous lemma. Then there are two$L _ { \infty }$-morphisms (projection and inclusion)

$$
(\mathbf {g} [ 1 ] _ {\text { formal }}, 0) \longrightarrow (\mathbf {g} ^ {\text { min }} [ 1 ] _ {\text { formal }}, 0), (\mathbf {g} ^ {\text { min }} [ 1 ] _ {\text { formal }}, 0) \longrightarrow (\mathbf {g} [ 1 ] _ {\text { formal }}, 0)
$$

which are both quasi-isomorphisms. From this follows that if

$$
(\mathbf {g} _ {1} [ 1 ] _ {f o r m a l}, 0) \longrightarrow (\mathbf {g} _ {2} [ 1 ] _ {f o r m a l}, 0)
$$

is a quasi-isomorphism then there exists a quasi-isomorphism

$$
(\mathbf {g} _ {1} ^ {m i n} [ 1 ] _ {f o r m a l}, 0) \longrightarrow (\mathbf {g} _ {2} ^ {m i n} [ 1 ] _ {f o r m a l}, 0).
$$

Any quasi-isomorphism between minimal$L _ { \infty } { \mathrm { - a l g e b r a s } }$is invertible, because it induces an isomorphism of spaces of cogenerators (the inverse mapping theorem from 4.1). Thus, we proved the first part of the theorem. Also, we see that the set equivalence classes of$L _ { \infty } { - } \mathrm { a }$lgebras up to quasi-isomorphisms can be naturally identified with the set of equivalence classes of minimal$L _ { \infty }$-algebras up to$L _ { \infty }$-isomorphisms.

## 4.5.2. Deformation functors at fixed points of Q

The deformation functor can be defined in terms of a formal graded Q-manifold M with base point (denoted by 0). The set of solutions of the Maurer-Cartan equation with coeficients in a finite-dimensional nilpotent non-unital algebra m is defined as the set of m-points of the formal scheme of zeroes of$Q \colon$

$$
M a p s \left(\left(S p e c (\mathbf {m} \oplus \mathbf {k} \cdot 1), \text {   base   point }\right), \left(Z e r o e s (Q), 0\right)\right) \subset M a p s \left(\left(S p e c (\mathbf {m} \oplus \mathbf {k} \cdot 1), \text {   base   point }\right), \left(M, 0\right)\right).
$$

In terms of the coalgebra  corresponding to M this set is equal to the set of homomorphisms of coalgebras$\mathbf { m } ^ { * } { \longrightarrow } \mathcal { C }$with the image annihilated by Q. Another way to say is to introduce a global (i.e. not formal) pointed Q-manifold of maps from$( S p e c ( \mathbf { m } \oplus \mathbf { k } \cdot 1 )$, base point to$( M , 0 )$and consider zeroes of the global vector field Q on it.

Two solutions p<sub>0</sub> and p<sub>1</sub> of the Maurer-Cartan equation are called gauge equivalent if there exists (parametrized by$S p e c ( \mathbf { m } \oplus \mathbf { k } \cdot 1 ) )$polynomial family of odd vector fields ξ(t) on M (of degree 1 with respect to Z-grading) and a polynomial solution of the equation

$$
\frac {d p (t)}{d t} = [ Q, \xi (t) ] _ {| p (t)}, p (0) = p _ {0}, p (1) = p _ {1},
$$

where$p ( t )$is a polynomial family of m-points of formal graded manifold M with base point.

In terms of$L _ { \infty } \mathrm { - a l g e b r a s , }$the set of polynomial paths$\{ p ( t ) \}$is naturally identified with$\mathbf { g } ^ { 1 } \otimes \mathbf { m } \otimes \mathbf { k } [ t ]$ Vector fields$\xi ( t )$depending polynomially on t are not necessarily vanishing at the base point 0. The set of these vector fields is

$$
H o m _ {G r a d e d ^ {\mathbf {k}}} \left(C (\mathbf {g} [ 1 ]) \oplus (\mathbf {k} \cdot 1) ^ {*}, \mathbf {g}\right) \otimes (\mathbf {m} \oplus \mathbf {k} \cdot 1).
$$

One can check that the gauge equivalence defined above is an equivalence relation. Alternatively, one can define the equivalence relation as the transitive closure of the relation from above. For formal graded pointed manifold M we define set$D e f _ { M } ( \mathbf { m } )$as the set of gauge equivalence classes of solutions of the

Maurer-Cartan equation. The correspondence$\mathbf { m } \mapsto D e f _ { M } ( \mathbf { m } )$extends naturally to a functor denoted also by$D e f _ { M }$. Analogously, for$L _ { \infty } { \mathrm { - a l g e b r a ~ g } }$we denote by$D e f _ { \mathbf { g } }$the corresponding deformation functor.

One can easily prove the following properties:

1) for a diferential graded Lie algebra g the deformation functor defined as above for$( \mathbf { g } [ 1 ] _ { f o r m a l } , 0 )$, is naturally equivalent to the deformation functor defined in 3.2,

2) any$L _ { \infty }$-morphism gives a natural transformation of functors,

3) the functor$D e f _ { \mathbf { g } _ { 1 } \oplus \mathbf { g } _ { 2 } }$corresponding to the direct sum of two$L _ { \infty } { \mathrm { - a l g e b r a s } }$, is naturally equivalent to the product of functors$D e f _ { { \bf g } _ { 1 } } \times D e f _ { { \bf g } _ { 2 } }$，

4) the deformation functor for a linear contractible L -algebra g is trivial,$D e f _ { \mathbf { g } } ( \mathbf { m } )$is a one-element set for every m.

Properties 2)-4) are just trivial, and 1) is easy. It follows from properties 1)-4) that if an$L _ { \infty }$-morphism of diferential graded Lie algebras is a quasi-isomorphism, then it induces an isomorphism of deformation functors. The theorem is proven. Q.E.D.

We would like to notice here that in the definition of the deformation functor one can consider just a formal pointed super Q-manifold (M, 0) (i.e. not a graded one), and m could be a finite-dimensional nilpotent diferential super commutative associative non-unital algebra.

## 4.6. Formality

## 4.6.1. Two diferential graded Lie algebras

Let X be a smooth manifold. We associate with it two diferential graded Lie algebras over R. The first diferential graded Lie algebra$D _ { p o l y } ( X )$is a subalgebra of the shifted Hochschild complex of the algebra A of functions on X (see 3.4.2). The space$D _ { p o l y } ^ { n } ( X )$,$n \geq - 1$consists of local Hochschild cochains$A ^ { \otimes ( n + 1 ) } { \longrightarrow } A$ given by polydiferential operators. In local coordinates$( x ^ { i } )$any element of$D _ { p o l y } ^ { n }$can be written as

$$
f _ {0} \otimes \dots \otimes f _ {n} \mapsto \sum_ {\left(I _ {0}, \dots , I _ {n}\right)} C ^ {I _ {0}, \dots , I _ {n}} (x) \cdot \partial_ {I _ {0}} \left(f _ {0}\right) \dots \partial_ {I _ {n}} \left(f _ {n}\right)
$$

where the sum is finite,$I _ { k }$denote multi-indices,$\partial _ { I _ { k } }$denote corresponding partial derivatives, and$f _ { k }$and $C ^ { I _ { 0 } , \ldots , I _ { n } }$are functions in$( x _ { i } )$

The second diferential graded Lie algebra,$T _ { p o l y } ( X )$is the graded Lie algebra of polyvector fields on X:

$$
T _ {p o l y} ^ {n} (X) = \Gamma (X, \wedge^ {n + 1} T _ {X}), n \geq - 1
$$

endowed with the standard Schouten-Nijenhuis bracket and with the diferential$d : = 0$. We remind here the formula for this bracket:

$$
\text { for   } k, l \geq 0 \quad [ \xi_ {0} \wedge \dots \wedge \xi_ {k}, \eta_ {0} \wedge \dots \wedge \eta_ {l} ] =
$$

$$
= \sum_ {i = 0} ^ {k} \sum_ {j = 0} ^ {l} (- 1) ^ {i + j + k} [ \xi_ {i}, \eta_ {j} ] \wedge \xi_ {0} \wedge \dots \wedge \xi_ {i - 1} \wedge \xi_ {i + 1} \wedge \dots \wedge \xi_ {k} \wedge \eta_ {0} \wedge \dots \wedge \eta_ {j - 1} \wedge \eta_ {j + 1} \wedge \dots \wedge \eta_ {l}, \xi_ {i}, \eta_ {j} \in \Gamma (X, T _ {X}),
$$

$$
\text { for   } k \geq 0 \quad [ \xi_ {0} \wedge \dots \wedge \xi_ {k}, h ] =
$$

$$
= \sum_ {i = 0} ^ {k} (- 1) ^ {i} \xi_ {i} (h) \cdot \left(\xi_ {0} \wedge \dots \wedge \xi_ {i - 1} \wedge \xi_ {i + 1} \wedge \dots \wedge \xi_ {k}\right) h \in \Gamma (X, \mathcal {O} _ {X}), \xi_ {i} \in \Gamma (X, T _ {X}).
$$

In local coordinates$( x ^ { 1 } , \ldots , x ^ { d } )$, if one replaces$\partial / \partial x ^ { i }$by odd variables$\psi _ { i }$and writes polyvector fields as functions in$( x ^ { 1 } , \ldots , x ^ { d } | \psi _ { 1 } , \ldots , \psi _ { d } )$, the bracket is

$$
[ \gamma_ {1}, \gamma_ {2} ] = \gamma_ {1} \bullet \gamma_ {2} - (- 1) ^ {k _ {1} k _ {2}} \gamma \bullet \gamma_ {1}
$$

where introduce the following notation:

$$
\gamma_ {1} \bullet \gamma_ {2} := \sum_ {i = 1} ^ {d} \frac {\partial \gamma_ {1}}{\partial \psi_ {i}} \frac {\partial \gamma_ {2}}{\partial x ^ {i}}, \gamma_ {i} \in T ^ {k _ {i}} (\mathbf {R} ^ {d}).
$$

We have an evident map$\mathcal { U } _ { 1 } ^ { ( 0 ) } : T _ { p o l y } ( X ) { \longrightarrow } D _ { p o l y } ( X )$:

$$
\begin{array}{c} \mathcal {U} _ {1} ^ {(0)}: (\xi_ {0} \wedge \ldots \wedge \xi_ {n}) \mapsto \left(f _ {0} \otimes \ldots \otimes f _ {n} \mapsto \frac {1}{(n + 1) !} \sum_ {\sigma \in \Sigma_ {n + 1}} s g n (\sigma) \prod_ {i = 0} ^ {n} \xi_ {\sigma_ {i}} (f _ {i})\right), \text {for} n \geq 0, \\ h \mapsto (1 \mapsto h), h \in \Gamma (X, \mathcal {O} _ {X}). \end{array}
$$

## 4.6.1.1. It is a quasi-isomorphism

Theorem.$\mathcal { U } _ { 1 } ^ { ( 0 ) }$is a quasi-isomorphism of complexes.

This is a version of Kostant-Hochschild-Rosenberg theorem which says that for a smooth afine algebraic variety$Y$over field k of characteristic zero, the Hochschild cohomology of algebra$\mathcal { O } ( Y )$coincides with the space$\oplus _ { k \geq 0 } \Gamma ( X , \wedge ^ { k } T _ { Y } ) [ - k ]$of algebraic polyvector fields on$Y .$. Analogous statement for$C ^ { \infty }$manifolds seems to be well known, although we were not able to find it in the literature. In any case, we show here a proof.

Proof: First of all, one can immediately check that the image of$\mathcal { U } _ { 1 } ^ { ( 0 ) }$is annihilated by the diferential in$D _ { p o l y } ( X )$, i.e. that$\mathcal { U } _ { 1 } ^ { ( 0 ) }$is a morphism of complexes.

Complex$D _ { p o l y } ( X )$is filtered by the total degree of polydiferential operators. Complex$T _ { p o l y } ( X )$endowed with zero diferential also carries a very simple filtration (just by degrees), such that$\mathcal { U } _ { 1 } ^ { ( 0 ) }$is compatible with filtrations. We claim that

$$
G r \big (\mathcal {U} _ {1} ^ {(0)} \big): G r \big (T _ {p o l y} (X) \big) \longrightarrow G r \big (D _ {p o l y} (X) \big)
$$

is a quasi-isomorphism. In the graded complex$G r \big ( D _ { p o l y } ( X ) \big )$associated with the filtered complex$D _ { p o l y } ( X )$ all components are sections of some natural vector bundles on$X$, and the diferential is A-linear,$A = C ^ { \infty } ( X )$ The same is true by trivial reasons for$T _ { p o l y } ( X )$. Thus, we have to check that the map$G r ( \mathcal { U } _ { 1 } ^ { ( 0 ) } )$is a quasi-isomorphism fiberwise.

Let x be a point of$X$and$T$be the tangent space at x. Principal symbols of polydiferential operators at$x$lie in vector spaces

$$
\operatorname{Sym} (T) \otimes \dots \otimes \operatorname{Sym} (T) \quad (n \text { times }, n \geq 0)
$$

where$S y m ( T )$is the free polynomial algebra generated by T. It better to identify$S y m ( T )$with the cofree cocommutative coassociative coalgebra with counit cogenerated by$T \colon$

$$
\mathcal {C} := C (T) \oplus (\mathbf {k} \cdot 1) ^ {*}.
$$

$S y m ( T )$is naturally isomorphic to the algebra of diferential operators on$T$with constant coeficients. If D is such an operator then it defines a linear functional on the algebra of formal power series at$0 \in T$

$$
f \mapsto (D (f)) (0).
$$

We denote by$\Delta$the coproduct in coalgebra$\mathcal { C } .$. It is easy to see that diferential in the complex $G r \big ( D _ { p o l y } ( X ) \big )$in the fiber at x is the following:

$$
d: \otimes^ {n + 1} \mathcal {C} \longrightarrow \otimes^ {n + 2} \mathcal {C}, d = 1 ^ {*} \otimes i d _ {\otimes^ {n + 1} \mathcal {C}} - \sum_ {i = 0} ^ {n} (- 1) ^ {i} i d \otimes \dots \otimes \Delta_ {i} \otimes \dots \otimes i d + (- 1) ^ {n} i d _ {\otimes^ {n + 1} \mathcal {C}} \otimes 1 ^ {*}
$$

where$\Delta _ { i }$is$\Delta$applied to the i-th argument.

Lemma. Let be the cofree cocommutative coassociative coalgebra with counit cogenerated by vector space T. Then the natural homomorphism of complexes

$$
\left(\wedge^ {n + 1} T, \text {   differential   } = 0\right) \longrightarrow \left(\otimes^ {n + 1} \mathcal {C}, \text {   differential   as   above }\right)
$$

is a quasi-isomorphism.

What we consider is one of standard complexes in homological algebra. One of possible proofs is the following:

Proof: first of all, we can safely assume that T is finite-dimensional. Let us decompose complex $\left( \otimes ^ { n + 1 } { \mathcal { C } } \right)$into the infinite direct sum of subcomplexes consisting of tensors of fixed total degrees (homogeneous components with respect to the action of the Euler vector fields on$T )$. Our statement means in particular that for only finitely many degrees these subcomplexes have non-trivial cohomology. Thus, the statement of the lemma is true if the analogous statement holds when infinite sums are replaced by infinite products in the decomposition of$( \otimes ^ { n + 1 } { \mathcal { C } } )$. Terms of the completed complex are spaces$\bar { H } o m ( A ^ { \diamondsuit ( n + 1 ) } , \mathbf { k } )$where A is the algebra of polynomial functions on T . It is easy to see that the completed complex calculates groups $E x t _ { A - m o d } ^ { n + 1 } ( { \bf k } , { \bf k } ) = \wedge ^ { n + 1 } T$where 1-dimensional space k is considered as A-module (via values of polynomial at$0 \in T )$and has a resolution

$$
\dots \longrightarrow A \otimes A \longrightarrow A \longrightarrow 0 \longrightarrow \dots
$$

by free A-modules. Q.E.D.

As a side remark, we notice that the statement of the lemma holds also if one replaces by$C ( T )$ $( { \mathrm { i . e . } }$the free coalgebra without counit) and removes terms with$1 ^ { * }$from the diferential. In the language of Hochschild cochains it means that the subcomplex of reduced cochains is quasi-isomorphic to the total Hochschild complex.

The lemma implies that$g r ( \mathcal { U } _ { 1 } ^ { ( 0 ) } )$is an isomorphism fiberwise, and the theorem is proven. Q.E.D.

## 4.6.2. Main theorem

Unfortunately, the map$\mathcal { U } _ { 1 } ^ { ( 0 ) }$does not commute with Lie brackets, the Schouten-Nijenhuis bracket does not go to the Gerstenhaber bracket. We claim that this defect can be cured:

Theorem. There exists an L<sub>∞</sub>-morphism  from$T _ { p o l y } ( X )$to$D _ { p o l y } ( X )$such that$\mathcal { U } _ { 1 } = \mathcal { U } _ { 1 } ^ { ( 0 ) }$

In other words, this theorem says that$T _ { p o l y } ( X )$and$D _ { p o l y } ( X )$are quasi-isomorphic diferential graded Lie algebras. In analogous situation in rational homotopy theory (see [Su]), a diferential graded commutative algebra is called formal if it is quasi-isomorphic to its cohomology algebra endowed with zero diferential. This explains the name of subsection 4.6.

The quasi-isomorphism in the theorem is not canonical. We will construct explicitly a family of quasi-isomorphisms parametrized in certain sense by a contractible space. It means that our construction is canonical up to (higher) homotopies.

Solutions of the Maurer-Cartan equation in$T _ { p o l y } ( X )$are exactly Poisson structures on$X { : }$

$$
\alpha \in T _ {p o l y} ^ {1} (X) = \Gamma (X, \wedge^ {2} T _ {X}), [ \alpha , \alpha ] = 0.
$$

Any such α defines also a solution formally depending on$\hbar ,$,

$$
\gamma (\hbar) := \alpha \cdot \hbar \in T _ {p o l y} ^ {1} (X) [ [ \hbar ] ], [ \gamma (\hbar), \gamma (\hbar) ] = 0.
$$

The gauge group action is the action of the difeomorphism group by conjugation. Solutions of the Maurer-Cartan equation in$D _ { p o l y } ( X )$formally depending on ¯h are star-products. Thus, we obtain as a corollary that any Poisson structure on X gives a canonical equivalence class of star-products, and the theorem from 1.3.

The rest of the paper is devoted to the proof of Theorem 4.6.2, and to the discussion of various applications, corollaries and extensions. In the next section (5) we will make some preparations for the universal formula (section 6) for an$L _ { \infty } \mathrm { - m o r p h i m }$from$T _ { p o l y } ( X )$to$D _ { p o l y } ( X )$in the case of flat space$X = \mathbf { R } ^ { d }$. In section$7$we extend our construction to general manifolds.

## 4.6.3. Non-uniqueness

There are other quasi-isomorphisms between$T _ { p o l y } ( X )$and$D _ { p o l y } ( X )$which difer essentially from the quasi-isomorphism$u ,$i.e. not even homotopic in a natural sense to . By homotopy here we mean the following. L<sub>∞</sub>-morphisms from one$L _ { \infty } \mathrm { - a l g e b r a }$to another can be identified with fixed points of$Q$on infinite-dimensional supermanifold of maps. Mimicking constructions and definitions form 4.5.2 one can define an equivalence relation (homotopy equivalence) on the set of L-morphisms.

Firstly, the multiplicative group$\mathbf { R } ^ { \times }$acts by automorphisms of$T _ { p o l y } ( X )$, multiplying elements$\gamma \in$ $T _ { p o l y } ( X ) ^ { k }$by const<sup>k</sup>. Composing these automorphisms with  one get a family of quasi-isomorphisms. Secondly, in$[ \mathrm { K o 2 } ]$we constructed an exotic infinitesimal$L _ { \infty }$-automorphism of$T _ { p o l y } ( X )$for the case$X = \mathbf { R } ^ { d }$ which probably extends to general manifolds. In particular, this exotic automorphism produces a vector field on the “set of Poisson structures”. The evolution with respect to time t is described by the following non-linear partial diferential equation:

$$
\frac {d \alpha}{d t} := \sum_ {i, j, k, l, m, k ^ {\prime}, l ^ {\prime}, m ^ {\prime}} \frac {\partial^ {3} \alpha^ {i j}}{\partial x ^ {k} \partial x ^ {l} \partial x ^ {m}} \frac {\partial \alpha^ {k k ^ {\prime}}}{\partial x ^ {l ^ {\prime}}} \frac {\partial \alpha^ {l l ^ {\prime}}}{\partial x ^ {m ^ {\prime}}} \frac {\partial \alpha^ {m m ^ {\prime}}}{\partial x ^ {k ^ {\prime}}} (\partial_ {i} \wedge \partial_ {j})
$$

where$\begin{array} { r } { \alpha = \sum _ { i , j } \alpha ^ { i j } ( x ) \partial _ { i } \wedge \partial _ { j } } \end{array}$is a bi-vector field on$\mathbf { R } ^ { d }$

A priori we can guarantee the existence of a solution of the evolution only for small times and realanalytic initial data. One can show that 1) this evolution preserves the class of (real-analytic) Poisson structures, 2) if two Poisson structures are conjugate by a real-analytic difeomorphism then the same will hold after the evolution. Thus, our evolution operator is essentially intrinsic and does not depend on the choice of coordinates.

Combining it with the action of$\mathbf { R } ^ { \times }$as above we see that the Lie algebra${ \bf { } } a f f ( 1 , { \bf { R } } )$of infinitesimal afine transformations of the line$\mathbf { R } ^ { 1 }$acts non-trivially on the space of homotopy classes of quasi-isomorphisms between$T _ { p o l y } ( X )$and$D _ { p o l y } ( X )$. Maybe, there are other exotic$L _ { \infty } \mathrm { { - a u t o m o r p h i s m s } , }$this possibility is not ruled out yet. The reader could ask why our quasi-isomorphism is better than others. Probably, the answer is that only (up to homotopy) preserves an additional structure present in the deformation quantization, the cup-product on the tangent cohomology (see section 8).

## 5. Configuration spaces and their compactifications

## 5.1. Definitions

Let n, m be non-negative integers satisfying the inequality$2 n + m \ge 2$. We denote by$C o n f _ { n , m }$the product of the configuration space of the upper half-plane with the configuration space of the real line:

$$
C o n f _ {n, m} = \{(p _ {1}, \ldots , p _ {n}; q _ {1}, \ldots , q _ {m}) | p _ {i} \in \mathcal {H}, q _ {j} \in \mathbf {R}, p _ {i _ {1}} \neq p _ {i _ {2}} \text {for} i _ {1} \neq i _ {2}, q _ {j _ {1}} \neq q _ {j _ {2}} \text {for} j _ {1} \neq j _ {2} \}
$$

$C o n f _ { n , m }$is a smooth manifold of dimension$2 n + m$. The group$G ^ { ( 1 ) }$of holomorphic transformations of$\mathbf { C } P ^ { 1 }$preserving the upper half-plane and the point , acts on$C o n f _ { n , m }$. This group is a 2-dimensional connected Lie group, isomorphic to the group of orientation-preserving afine transformations of the real line:

$$
G ^ {(1)} = \left\{z \mapsto a z + b | a, b \in \mathbf {R}, a > 0 \right\}.
$$

It follows from the condition 2n$+ m \ge 2$that the action of$G ^ { ( 1 ) }$on$C o n f _ { n , m }$is free. The quotient space $C _ { n , m } : = C o n f _ { n , m } / G ^ { ( 1 ) }$is a manifold of dimension$2 n + m - 2$. If$P = ( p _ { 1 } , \ldots , p _ { n } ; q _ { 1 } , \ldots , q _ { m } )$is a point of $C o n f _ { n , m }$then we denote by$[ P ]$the corresponding point of$C _ { n , m }$

Analogously, we introduce simpler spaces$C o n f _ { n }$and$C _ { n }$for any$n \geq 2 \mathrm { : }$

$$
\operatorname{Conf} _ {n} := \left\{\left(p _ {1}, \dots , p _ {n}\right) \mid p _ {i} \in \mathbf {C}, p _ {i} \neq p _ {j} \text { for } i \neq j \right\},
$$

$$
C _ {n} = C o n f _ {n} / G ^ {(2)}, d i m (C _ {n}) = 2 n - 3,
$$

where$G ^ { ( 2 ) }$is a 3-dimensional Lie group,

$$
G ^ {(2)} = \left\{z \mapsto a z + b | a \in \mathbf {R}, b \in \mathbf {C}, a > 0 \right\}.
$$

We will construct compactifications$\overline { { C } } _ { n , m }$of$C _ { n , m }$( and compactifications${ \overline { { C } } } _ { n } \ { \mathrm { o f } } \ C _ { n } )$which are smooth manifolds with corners.

We remind that a manifold with corners (of dimension$d )$is defined analogously to a usual manifold with boundary, with the only diference that the manifold with corners looks locally as an open part of closed simplicial cone$( { \bf R } _ { \geq 0 } ) ^ { d }$. For example, the closed hypercube$[ 0 , 1 ] ^ { d }$is a manifold with corners. There is a natural smooth stratification by faces of any manifold with corners.

First of all, we give one of possible formal definitions of the compactification$\overline { { C } } _ { n , m }$in the case$n \geq 1$ With any point$\left[ \left( p _ { 1 } , \ldots , p _ { n } ; q _ { 1 } , \ldots , q _ { m } \right) \right]$of$C _ { n , m }$we associate a collection of$2 n ( n - 1 ) +$nm angles with values in$\mathbf { R } / 2 \pi \mathbf { Z } \colon$

$$
\left(A r g (p _ {i} - p _ {j}), A r g (p _ {i} - \overline {{p}} _ {j}), A r g (p _ {i} - q _ {j})\right) .
$$

It is easy to see that we obtain an embedding of$C _ { n , m }$into the torus$( \mathbf { R } / 2 \pi \mathbf { Z } ) ^ { 2 n ( n - 1 ) + n m }$. The space$\overline { { C } } _ { r }$,m is defined as the compactification of the image of this embedding. Analogously, the compactification$\overline { { C } } _ { n }$is obtained using angles$A r g ( p _ { i } - p _ { j } )$.

One can show that open strata of$\overline { { C } } _ { n , m }$are naturally isomorphic to products of manifolds of type$C _ { n ^ { \prime } , m ^ { \prime } }$ and$C _ { n ^ { \prime } }$. In the next subsection we will describe explicitly$\overline { { C } } _ { n , m }$as a manifold with corners.

There is a natural action of the permutation group$\Sigma _ { n }$on$C _ { n } .$, and also of$\Sigma _ { n } \times \Sigma _ { m }$on$C _ { n , m }$. This gives us a possibility to define spaces$C _ { A }$and$C _ { A , B }$for finite sets$A , B$such that$\# A \geq 2$or$2 \# A + \# B \geq 2$ respectively. If$A ^ { \prime } { \hookrightarrow } A$and$B ^ { \prime } { \hookrightarrow } B$are inclusions of sets then there are natural fibrations (forgetting maps) $C _ { A } { \longrightarrow } C _ { A ^ { \prime } }$and$C _ { A , B } { \longrightarrow } C _ { A ^ { \prime } , B ^ { \prime } }$

## 5.2. Looking through a magnifying glass

The definition of the compactification given in the previous subsection is not descriptive. We are going to explain an intuitive idea underlying a direct construction of the compactification$\overline { { C } } _ { n , m }$as a manifold with corners. For more formal treatment of compactifications of configuration spaces we refer the reader to [FM] (for the case of smooth algebraic varieties).

Let us try to look through a magnifying glass, or better through a microscope with arbitrary magnification, on diferent parts of the picture formed by points on${ \mathcal { H } } \cup \mathbf { R } \subset \mathbf { C }$, and by the line$\mathbf { R } \subset \mathbf { C }$. Here we use Euclidean geometry on${ \bf C } \simeq { \bf R } ^ { 2 }$instead of Lobachevsky geometry.

Before doing this let us first consider the case of a configuration on$\mathbf { R } ^ { 2 } \simeq \mathbf { C } .$, i.e. without the horizontal line$\mathbf { R } \subset \mathbf { C }$. We say that the configuration$( p _ { 1 } , \ldots , p _ { n } )$is in standard position if

1) the diameter of the set$\{ p _ { 1 } , . . . , p _ { n } \}$is equal to 1, and,

2) the center of the minimal circle containing$\{ p _ { 1 } , . . . , p _ { n } \}$is$0 \in \mathbf { C }$

It is clear that any configuration of n pairwise distinct points in the case$n \geq 2$can be uniquely put to standard position by an element of group$G ^ { ( 2 ) }$. The set of configurations in standard position gives a continuous section$s ^ { c o n t }$of the natural projection map$C o n f _ { n } { \longrightarrow } C _ { n }$

For a configuration in standard position there could be several domains where we will need magnification in order to see details. These domains are those where at least two points of the configuration come too close to each other.

After an appropriate magnification of any such domain we again get a stable configuration (i.e.the number of points there is at least 2). Then we can put it again in standard position and repeat the procedure.

In such a way we get an oriented tree T with one root, and leaves numbered from 1 to n. For example, the configuration on the next figure

$$
^ 2 \bullet \quad^ {3} _ {4}
$$

gives the tree

![](images/page_19_image_2.jpg)

For every vertex of tree$T$except leaves, we denote by$S t a r ( v )$the set of edges starting at v. For example, in the figure from above the set$S t a r ( r o o t )$has three elements, and sets$S t a r ( v )$for other three vertices all have two elements.

Points in$C _ { n }$close to one which we consider, can be parametrized by the following data:

a) for each vertex v of$T$except leaves, a stable configuration$c _ { v }$in standard position of points labeled by the set$S t a r ( v )$，

b) for each vertex v except leaves and the root of the tree, the scale$s _ { v } > 0$with which we should put a copy of$c _ { v }$instead of the corresponding point$p _ { v } \in \mathbf { C }$on stable configuration$c _ { u }$where$u \in V _ { T }$is such that $( u , v ) \in E _ { T }$

More precisely, we act on the configuration$c _ { v }$by the element$( z \mapsto s _ { v } z + p _ { v } )$of$G ^ { ( 2 ) }$

Numbers$s _ { v }$are small but positive. The compactification$\overline { { C } } _ { n }$is achieved by formally permitting some of scales$s _ { v }$to be equal to 0.

In this way we get a compact topological manifold with corners, with strata$C _ { T }$labeled by trees$T$(with leaves numbered from 1 to n). Each stratum$C _ { T }$is canonically isomorphic to the product$\prod _ { v } C _ { S t a r ( v ) }$over all vertices v except leaves. In the description as above points of$C _ { T }$correspond to collections of configurations with all scales$s _ { v }$equal to zero. Let us repeat: as a set$\overline { { C } } _ { n }$coincides with

$$
\bigsqcup_ {\text { trees } T} \prod_ {v \in V _ {T} \setminus \{\text { leaves } \}} C _ {S t a r (v)} .
$$

In order to introduce a smooth structure on$\overline { { C } } _ { n }$, we should choose a$\Sigma _ { n }$-equivariant smooth section $s ^ { s m o o t h }$of the projection map$C o n f _ { n } { \longrightarrow } C _ { n }$instead of the section$s ^ { c o n t }$given by configurations in standard position. Local coordinates on$\overline { { C } } _ { n }$near a given point lying in stratum$C _ { T }$are scales$s _ { v } \in \mathbf { R } _ { \geq 0 }$close to zero and local coordinates in manifolds$C _ { S t a r ( v ) }$for all$v \in V _ { T } \mathrm { ~ } \backslash$leaves . The resulting structure of a smooth manifold with corners does not depend on the choice of section$s ^ { s m o o t h }$

The case of configurations of points on   R is not much harder. First of all, we say that a finite non-empty set S of points on${ \mathcal { H } } \cup \mathbf { R }$is in standard position if

1) the projection of the convex hull of S to the horizontal line${ \bf R } \subset { \bf C } \simeq { \bf R } ^ { 2 }$is either the one-point set 0 , or it is an interval with the center at 0,

2) the maximum of the diameter of S and of the distance from$S$to R is equal to 1.

It is easy to see that for$2 n + m \ge 2$(the stable case) any configuration of n points on and m points on R can be put uniquely in standard position by an element of$G ^ { \breve { ( 1 ) } }$. In order to get a smooth structure, we repeat the same arguments as for the case of manifolds$C _ { n }$

Domains where we will need magnification in order to see details, are now of two types. The first case is when at least two points of the configuration come too close to each other. We want to know whether what we see is a single point or a collection of several points. The second possibility is when a point on comes too close to R. Here we want also to decide whether what we see is a point (or points) on  or on R.

If the domain which we want to magnify is close to R, then after magnification we get again a stable configuration which we can put into the standard position. If the domain is inside${ \mathcal { H } } ,$then after magnification we get a picture without the horizontal line in it, and we are back in the situation concerning$\overline { { C } } _ { n ^ { \prime } }$for$n ^ { \prime } \leq n$

It is instructional to draw low-dimensional spaces$C _ { n , m }$. The simplest one,$C _ { 1 , 0 } = \overline { { C } } _ { 1 , 0 }$is just a point. The space$C _ { 0 , 2 } = \overline { { C } } _ { 0 , 2 }$is a two-element set. The space$C _ { 1 , 1 }$is an open interval, and its closure$\overline { { C } } _ { 1 , 1 }$is a closed interval (the real line$\mathbf { R } \subset \mathbf { C }$is dashed on the picture):

![](images/page_20_image_6.jpg)

The space$C _ { 2 , 0 }$is difeomorphic to$\mathcal { H } \setminus \{ 0 + 1 \cdot i \}$. The reason is that by action of$G ^ { ( 1 ) }$we can put point $p _ { 1 }$to the position$i = { \sqrt { - 1 } } \in { \mathcal { H } } .$. The closure$\overline { { C } } _ { 2 , 0 }$can be drawn like this:

![](images/page_20_image_8.jpg)

or like this:

![](images/page_20_image_10.jpg)

The Eye

Forgetting maps (see the end of 5.1) extend naturally to smooth maps of compactified spaces.

## 5.2.1. Boundary strata

We give here the list of all strata in$\overline { { C } } _ { A , B }$of codimension 1:

S1) points$p _ { i } \in \mathcal { H }$for$i \in S \subseteq A$where$\# S \geq 2$, move close to each other but far from R,

S2) points$p _ { i } \in \mathcal { H }$for$i \in S \subseteq A$and points$q _ { j } \in \mathbf { R }$for$j \in S ^ { \prime } \subseteq B$where$2 \# S + \# S ^ { \prime } \geq 2$, all move close to each other and to R, with at least one point left outside S and$S ^ { \prime }$, i.e.$\# S + \# S ^ { \prime } \leq \# A + \# B - 1$

The stratum of type S1 is

$$
\partial_ {S} \overline {{C}} _ {A, B} \simeq C _ {S} \times C _ {(A \setminus S) \sqcup \{p t \}, B}
$$

where$\{ p t \}$is a one-element set, whose element represents the cluster$( p _ { i } ) _ { i \in S }$of points in . Analogously, the stratum of type S2 is

$$
\partial_ {S, S ^ {\prime}} \overline {{C}} _ {A, B} \simeq C _ {S, S ^ {\prime}} \times C _ {A \setminus S, (B \setminus S ^ {\prime}) \sqcup \{p t \}}.
$$

## 6. Universal formula

In this section we propose a formula for an$L _ { \infty }$-morphism$T _ { p o l y } ( { \mathbf { R } } ^ { d } ) { \longrightarrow } D _ { p o l y } ( { \mathbf { R } } ^ { d } )$generalizing a formula for the star-product in section 2. In order to write it we need to make some preparations.

## 6.1. Admissible graphs

Definition. Admissible graph Γ is an oriented graph with labels such that 1) the set of vertices$V _ { \Gamma }$is$\{ 1 , \ldots , n \} \sqcup \{ { \overline { { 1 } } } , \ldots , { \overline { { m } } } \}$where$n , m \in { \bf Z } _ { > 0 }$, 2n$+ 2 - m \ge 0 ;$vertices from the set$\{ 1 , \ldots , n \}$are called vertices of the first type, vertices from$\{ \overline { { 1 } } , \ldots , \overline { { m } } \}$are called vertices of the second type,

2) every edge$( v _ { 1 } , v _ { 2 } ) \in E _ { \Gamma }$starts at a vertex of first type,$v _ { 1 } \in \{ 1 , \ldots , n \}$

3) there are no loops, i.e. no edges of the type$( \boldsymbol { v } , \boldsymbol { v } )$

4) for every vertex$k \in \{ 1 , \ldots , n \}$of the first type, the set of edges

$$
\operatorname{Star} (k) := \left\{\left(v _ {1}, v _ {2}\right) \in E _ {\Gamma} \mid v _ {1} = k \right\}
$$

starting from$s ,$is labeled by symbols$( e _ { k } ^ { 1 } , \ldots , e _ { k } ^ { \# S t a r ( k ) } )$

Labeled oriented graphs considered in section 2 are exactly (after the identifications$L = \overline { { 1 } } , R = \overline { { 2 } } )$ admissible graphs such that m is equal to 2, and the number of edges starting at every vertex of first type is also equal to 2.

## 6.2. Diferential forms on configuration spaces

The space$\overline { { C } } _ { 2 , 0 }$(the Eye) is homotopy equivalent to the standard circle$S ^ { 1 } \simeq \mathbf { R } / 2 \pi \mathbf { Z }$. Moreover, one of its boundary components, the space$C _ { 2 } = \overline { { C } } _ { 2 }$, is naturally$S ^ { 1 }$. The other component of the boundary is the union of two closed intervals (copies of$\overline { { C } } _ { 1 , 1 } )$with identified end points.

Definition. An angle map is a smooth map$\phi : \overline { { C } } _ { 2 , 0 } \longrightarrow \mathbf { R } / 2 \pi \mathbf { Z } \simeq S ^ { 1 }$such that the restriction of$\phi$to $C _ { 2 } \simeq S ^ { 1 }$is the angle measured in the anti-clockwise direction from the vertical line, and φ maps the whole upper interval$\overline { { C } } _ { 1 , 1 } \simeq [ 0 , 1 ]$of the$E y e ,$to a point in$S ^ { 1 }$

We will denote$\phi ( [ ( x , y ) ] )$) simply by$\phi ( x , y )$where$x , y \in \mathcal { H } \cup \mathbf { R } , \ x \neq y$. It follows from the definition that$d \phi ( x , y ) = 0$if x stays in R.

For example, the special map$\phi ^ { h }$used in the formula in section 2, is an angle map. In the rest of the paper (except of the comments 9.5 and 9.8) we can use any φ, not necessarily harmonic.

We are now prepared for the analytic part of the universal formula. Let Γ be an admissible graph with n vertices of the first type, m vertices of the second type and with$2 n + m - 2$edges. We define the weight of graph Γ by the following formula:

$$
W _ {\Gamma} := \prod_ {k = 1} ^ {n} \frac {1}{(\# S t a r (k)) !} \frac {1}{(2 \pi) ^ {2 n + m - 2}} \int_ {\overline {{\mathcal {C}}} _ {n, m} ^ {+}} \bigwedge_ {e \in E _ {G}} d \phi_ {e}.
$$

Let us explain what is written here. The domain of integration$\overline { { C } } _ { n , m } ^ { + }$is a connected component of$\overline { { C } } _ { n , m }$ which is the closure of configurations for which points$q _ { j } , \ 1 \leq j \leq m$on R are placed in the increasing order:

$$
q _ {1} <   \ldots <   q _ {m}.
$$

The orientation of$C o n f _ { n , m }$is the product of the standard orientation on the coordinate space$\mathbf { R } ^ { m } \supset$ $\{ ( q _ { 1 } , \ldots , q _ { m } ) | q _ { j } \in \mathbf { R } \}$, with the product of standard orientations on the plane$\mathbf { R } ^ { 2 }$(for points$p _ { i } \in \mathcal { H } \subset \mathbf { R } ^ { 2 } )$ The group$G ^ { ( 1 ) }$is even-dimensional and naturally oriented because it acts freely and transitively on complex manifold . Thus, the quotient space$C _ { n , m } = C o n f _ { n , m } / G ^ { ( 1 ) }$carries again a natural orientation.

Every edge e of Γ defines a map from$\overline { { C } } _ { n , m }$to$\overline { { C } } _ { 2 , 0 }$or to$\overline { { C } } _ { 1 , 1 } \subset \overline { { C } } _ { 2 , 0 }$(the forgetting map). Here we consider inclusion$\overline { { C } } _ { 1 , 1 }$in$\overline { { C } } _ { 2 , 0 }$as the lower interval of the Eye. The pullback of the function φ by the map $\overline { { C } } _ { n , m } { \longrightarrow } \overline { { C } } _ { 2 , 0 }$corresponding to edge e is denoted by$\phi _ { e }$

Finally, the ordering in the wedge product of 1-forms$d \phi _ { e }$is fixed by enumeration of the set of sources of edges and by the enumeration of the set of edges with a given source.

The integral giving$W _ { \Gamma }$is well-defined because it is an integral of a smooth diferential form over a compact manifold with corners.

## 6.3. Pre-$L _ { \infty } .$-morphisms associated with graphs

For any admissible graph Γ with n vertices of the first type, m vertices of the second type, and$2 n +$ $m - 2 + l$edges where$l \in \mathbf { Z } .$, we define a linear map$I _ { \Gamma } : \otimes ^ { n } T _ { p o l y } ( { \bf R } ^ { d } ) { \longrightarrow } D _ { p o l y } ( { \bf R } ^ { d } ) [ 1 + l - n ]$. This map has only one non-zero graded component$( \mathcal { U } _ { \Gamma } ) _ { ( k _ { 1 } , \dots , k _ { n } ) }$where$k _ { i } = \# S t a r ( i ) - 1 , \ i = 1 , \dots , n .$. If$l = 0$then from <sub>Γ</sub> after anti-symmetrization we obtain a pre-$L _ { \infty }$-morphism.

Let$\gamma _ { 1 } , \ldots , \gamma _ { n }$be polyvector fields on$\mathbf { R } ^ { d }$of degrees$( k _ { 1 } + 1 ) , \ldots , ( k _ { n } + 1 )$, and$f _ { 1 } , \ldots , f _ { m }$be functions on$\mathbf { R } ^ { d }$. We are going to write a formula for function Φ on$\mathbf { R } ^ { n }$:

$$
\Phi := \left(\mathcal {U} _ {\Gamma} \left(\gamma_ {1} \otimes \dots \otimes \gamma_ {n}\right)\right) \left(f _ {1} \otimes \dots \otimes f _ {m}\right).
$$

The formula for Φ is the sum over all configurations of indices running from 1 to$d ,$labeled by$\textstyle E _ { \Gamma } :$

$$
\Phi = \sum_ {I: E _ {\Gamma} \longrightarrow \{1, \dots , d \}} \Phi_ {I},
$$

where$\Phi _ { I }$is the product over all$n + m$vertices of Γ of certain partial derivatives of functions$g _ { j }$and of coeficients of$\gamma _ { i }$.

Namely, with each vertex$i , 1 \le i \le n$of the first type we associate function$\psi _ { i }$on$\mathbf { R } ^ { d }$which is a coeficient of the polyvector field$\gamma _ { i } \colon$

$$
\psi_ {i} = \left\langle \gamma_ {i}, d x ^ {I (e _ {i} ^ {1})} \otimes \dots \otimes d x ^ {I (e _ {i} ^ {k _ {i} + 1})} \right\rangle .
$$

Here we use the identification of polyvector fields with skew-symmetric tensor fields as

$$
\xi_ {1} \wedge \dots \wedge \xi_ {k + 1} \longrightarrow \sum_ {\sigma \in \Sigma_ {k + 1}} s g n (\sigma) \xi_ {\sigma_ {1}} \otimes \dots \otimes \xi_ {\sigma_ {k + 1}} \in \Gamma \left(\mathbf {R} ^ {d}, T ^ {\otimes (k + 1)}\right).
$$

For each vertex$\overline { { j } }$of second type the associated function$\psi _ { \overline { { j } } }$is defined as$f _ { j }$.

Now, at each vertex of graph Γ we put a function on$\mathbf { R } ^ { d }$(i.e. ψ<sub>i</sub> or$\psi _ { \overline { { j } } } )$. Also, on edges of graph Γ there are indices$I ( e )$which label coordinates in$\mathbf { R } ^ { d }$. In the next step we put into each vertex v instead of function$\psi _ { v }$its partial derivative

$$
\left(\prod_ {e \in E _ {\Gamma},   e = (*, v)} \partial_ {I (e)}\right) \psi_ {v},
$$

and then take the product over all vertices v of Γ. The result is by definition the summand$\Phi _ { I }$

Construction of the function Φ from the graph Γ, polyvector fields$\gamma _ { i }$and functions$f _ { j } ,$is invariant under the action of the group of afine transformations of$\mathbf { R } ^ { d }$because we contract upper and lower indices.

## 6.4. Main Theorem for$X = \mathbf { R } ^ { d }$, and the proof

We define an$L _ { \infty }$-morphism :$T _ { p o l y } ( \mathbf { R } ^ { d } ) \longrightarrow D _ { p o l y } ( \mathbf { R } ^ { d } )$by the formula for its n-th derivative$\textstyle { \mathcal { U } } _ { n } , \ n \geq 1$ considered as a skew-symmetric polylinear map (see 4.2) from$\otimes ^ { n } T _ { p o l y } ( \mathbf { R } ^ { d } )$to$D _ { p o l y } ( { \mathbf R } ^ { d } ) [ 1 - n ]$

$$
\mathcal {U} _ {n} = \sum_ {m \geq 0} \sum_ {\Gamma \in G _ {n, m}} W _ {\Gamma} \times \mathcal {U} _ {\Gamma}.
$$

Here$G _ { n , m }$denotes the set of all admissible graphs with n vertices of the first type, m vertices in the second group and$2 n + m - 2$edges, where$n \geq 1 , m \geq 0$(and automatically$2 n + m - 2 \geq 0 )$

Theorem. is an$L _ { \infty } – m o r p h i s m ,$, and also a quasi-isomorphism.

Proof: first of all, we should check that$\mathcal { U } _ { n }$is skew-symmetric, i.e. that is a pre-$L _ { \infty }$-morphism. For this see subsection 6.5.

The condition that is an$L _ { \infty }$-morhism (see 4.3 and 3.4.2) can be written explicitly as

$$
f _ {1} \cdot (\mathcal {U} _ {n} (\gamma_ {1} \wedge \dots \wedge \gamma_ {n})) (f _ {2} \otimes \dots \otimes f _ {m}) \pm (\mathcal {U} _ {n} (\gamma_ {1} \wedge \dots \wedge \gamma_ {n})) (f _ {1} \otimes \dots \otimes f _ {m - 1}) \cdot f _ {m} +
$$

$$
\begin{array}{l} + \sum_ {i = 1} ^ {m - 1} \pm (\mathcal {U} _ {n} (\gamma_ {1} \wedge \ldots \wedge \gamma_ {n})) (f _ {1} \otimes \ldots \otimes (f _ {i} f _ {i + 1}) \otimes \ldots \otimes f _ {m}) + \\ + \sum_ {i \neq j} \pm (\mathcal {U} _ {n - 1} ([ \gamma_ {i}, \gamma_ {j} ] \wedge \gamma_ {1} \wedge \ldots \wedge \gamma_ {n})) (f _ {1} \otimes \ldots \otimes f _ {m}) + \\ + \frac {1}{2} \sum_ {k, l \geq 1, k + l = n} \frac {1}{k ! l !} \sum_ {\sigma \in \Sigma_ {n}} \pm [ \mathcal {U} _ {k} (\gamma_ {\sigma_ {1}} \wedge \ldots \wedge \gamma_ {\sigma_ {k}}), \mathcal {U} _ {l} (\gamma_ {\sigma_ {k + 1}} \wedge \ldots \wedge \gamma_ {\sigma_ {n}}) ] (f _ {1} \otimes \ldots \otimes f _ {m}) = 0. \end{array}
$$

Here$\gamma _ { i }$are polyvector fields,$f _ { i }$are functions,$\mathcal { U } _ { n }$are homogeneous components of  (see 4.1). There is a way to rewrite this formula. Namely, we define$\mathcal { U } _ { 0 }$as the map$\bigotimes ^ { 0 } ( T _ { p o l y } ( { \mathbf { R } } ^ { d } ) ) \longrightarrow D _ { p o l y } ( { \mathbf { R } } ^ { d } ) [ 1 ]$which maps the generator 1 of${ \bf R } \simeq \otimes ^ { 0 } ( T _ { p o l y } ( { \bf R } ^ { d } ) )$to the product$m _ { A } \in D _ { p o l y } ^ { 1 } ( \mathbf { R } ^ { d } )$in the algebra$A : = C ^ { \infty } ( \mathbf { R } ^ { d } )$. Here $m _ { A } : f _ { 1 } \otimes f _ { 2 } \mapsto f _ { 1 } f _ { 2 }$is considered as a bidiferential operator.

The condition from above for  to be an$L _ { \infty }$-morphism is equivalent to the following one:

$$
\sum_ {i \neq j} \pm \left(\mathcal {U} _ {n - 1} ((\gamma_ {i} \bullet \gamma_ {j}) \wedge \gamma_ {1} \wedge \dots \wedge \gamma_ {n})\right) (f _ {1} \otimes \dots \otimes f _ {m}) +
$$

$$
+ \sum_ {k, l \geq 0, k + l = n} \frac {1}{k ! l !} \sum_ {\sigma \in \Sigma_ {n}} \pm \left(\mathcal {U} _ {k} (\gamma_ {\sigma_ {1}} \wedge \ldots \wedge \gamma_ {\sigma_ {k}}) \circ \mathcal {U} _ {l} (\gamma_ {\sigma_ {k + 1}} \wedge \ldots \wedge \gamma_ {\sigma_ {n}})\right) (f _ {1} \otimes \ldots \otimes f _ {m}) = 0.
$$

Here we use definitions of brackets in$D _ { p o l y }$and$T _ { p o l y }$via operations  (see 3.4.2) and  (see 4.6.1). We denote the l.h.s. of the expression above as (F).

$\mathcal { U } + \mathcal { U } _ { \mathrm { 0 } }$is not a pre-$L _ { \infty } .$-morphism because it maps 0 to a non-zero point$m _ { A }$. Still the equation$( F ) = 0$ makes sense and means that the map$( \mathcal { U } + \mathcal { U } _ { 0 } )$from formal Q-manifold$T _ { p o l y } ( { \mathbf { R } } ^ { d } ) [ 1 ] ) _ { f o r m a l }$to the formal neighborhood of point$m _ { A }$in super vector space$D _ { p o l y } ( \mathbf { R } ^ { d } ) [ 1 ]$is Q-equivariant, where the odd vector field$Q$ on the target is purely quadratic and comes from the bracket on$D _ { p o l y } ( \mathbf { R } ^ { d } )$, forgetting the diferential.

Also, the term$\mathcal { U } _ { \mathrm { 0 } }$comes from the unique graph$\Gamma _ { 0 }$which was missing in the definition of . Namely, $\Gamma _ { 0 }$has$n = 0$vertices of the first type, m = 2 vertices of the second$\mathrm { t y p e }$, and no edges at all. It is easy to see that$W _ { \Gamma _ { 0 } } = 1$and$\mathcal { U } _ { \Gamma _ { 0 } } = \mathcal { U } _ { 0 }$

We consider the expression$( F )$simultaneously for all possible dimensions d. It is clear that one can write (F) as a linear combination

$$
\sum_ {\Gamma} c _ {\Gamma} \cdot \mathcal {U} _ {\Gamma} \left(\gamma_ {1} \otimes \dots \otimes \gamma_ {n}\right)) \left(f _ {1} \otimes \dots \otimes f _ {m}\right)
$$

of expressions$\mathcal { U } _ { \Gamma }$for admissible graphs Γ with n vertices of the first type, m vertices of the second type, and $2 n + m - 3$edges where$n \geq 0 , m \geq 0 , 2 n + m - 3 \geq 0$. We assume that$c _ { \Gamma } = \pm c _ { \Gamma ^ { \prime } }$′ if graph$\Gamma ^ { \prime }$is obtained from Γ by a renumeration of vertices of first type and by a relabeling of edges in sets$S t a r ( v )$(see 6.5 where we discuss signs).

Coeficients c<sub>Γ</sub> of this linear combination are equal to certain sums with signs of weights$\mathcal { W } _ { \Gamma ^ { \prime } }$associated with some other graphs$\Gamma ^ { \prime }$, and of products of two such weights. In particular, numbers c do not depend on the dimension d in our problem. Perhaps it is better to use here the language of operads, but we will not do it.

We want to check that$c _ { \Gamma }$vanishes for each Γ.

The idea is to identify$c _ { \Gamma }$with the integral over the boundary$\partial \overline { { C } } _ { n , m }$of the closed diferential form constructed from Γ as in 6.2. The Stokes formula gives the vanishing:

$$
\int_ {\partial \overline {{C}} _ {n, m}} \bigwedge_ {e \in E _ {\Gamma}} d \phi_ {e} = \int_ {\overline {{C}} _ {n, m}} d \left(\bigwedge_ {e \in E _ {\Gamma}} d \phi_ {e}\right) = 0.
$$

We are going to calculate integrals of the form$\land _ { e \in E _ { \Gamma } } d \phi _ { e }$restricted to all possible boundary strata of $\partial \overline { { C } } _ { n , m }$, and prove that the total integral as above is equal to$c _ { \Gamma }$. At the subsection 5.2 we listed two groups of boundary strata, denoted by S1 and S2 and labeled by sets or pairs of sets. Thus,

$$
0 = \int_ {\partial \overline {{C}} _ {n, m}} \bigwedge_ {e \in E _ {\Gamma}} d \phi_ {e} = \sum_ {S} \int_ {\partial_ {S} \overline {{C}} _ {n, m}} \bigwedge_ {e \in E _ {\Gamma}} d \phi_ {e} + \sum_ {S, S ^ {\prime}} \int_ {\partial_ {S, S ^ {\prime}} \overline {{C}} _ {n, m}} \bigwedge_ {e \in E _ {\Gamma}} d \phi_ {e}.
$$

## 6.4.1. Case S1

Points$p _ { i } \in \mathcal { H }$for i from subset$S \subset \{ 1 , \ldots , n \}$where$\# S \geq 2 .$, move close to each other. The integral over the stratum$\partial _ { S } \overline { { C } } _ { n , m }$is equal to the product of an integral over$C _ { n _ { 1 } , m }$with an integral over$C _ { n _ { 2 } }$where $n _ { 2 } : = \# S , n _ { 1 } : = n - n _ { 2 } + 1$. The integral vanishes by dimensional reasons unless the number of edges of Γ connecting vertices from S is equal to$2 n _ { 2 } - 3$

There are several possibilities:

## 6.4.1.1. First subcase of S1:$n _ { 2 } = 2$

In this subcase two vertices from$S _ { 1 }$are connected exactly by one edge, which we denote by$e .$The integral over$C _ { 2 }$here gives number 1 (after division by 2π coming from the of the formula for weights$W _ { \Gamma } )$ The total integral over the boundary stratum is equal to the integral of a new graph$\Gamma _ { 1 }$obtained from Γ by the contraction of edge e. It is easy to see (up to a sign) that this corresponds to the first line in our expression (F), the one where the operation on polyvector fields appears.

![](images/page_25_image_0.jpg)

## 6.4.1.2. Second subcase of S1:$n _ { 2 } \geq 3$

This is the most non-trivial case. The integral corresponding to the corresponding boundary stratum vanishes because the integral of any product of$2 n _ { 2 } - 3$angle forms over$C _ { n _ { 2 } }$where$n _ { 2 } \geq 3$vanishes, as is proven later in 6.6.

![](images/page_25_image_3.jpg)

## 6.4.2. Case S2

Points$p _ { i }$for$i \in S _ { 1 } \subset \{ 1 , \ldots , n \}$and points$q _ { j }$for${ \overline { { j } } } \in S _ { 2 } \subset \{ { \overline { { 1 } } } , \dots , { \overline { { m } } } \}$move close to each other and to the horizontal line R. The condition is that$2 n _ { 2 } + m _ { 2 } - 2 \geq 0$and$n _ { 2 } + m _ { 2 } \leq n + m - 1$where$n _ { 2 } : = \# S _ { 1 }$, m<sub>2</sub> := $\# S _ { 2 }$. The corresponding stratum is isomorphic to$C _ { n _ { 1 } , m _ { 1 } } \times C _ { n _ { 2 } , m _ { 2 } }$where$n _ { 1 } : = n - n _ { 2 } , \ m _ { 1 } = m - m _ { 2 } + 1$ The integral of this stratum decomposes into the product of two integrals. It vanishes if the number of edges of Γ connecting vertices from$S _ { 1 } \sqcup S _ { 2 }$is not equal to$2 n _ { 2 } + m _ { 2 } - 2$

## 6.4.2.1. First subcase of S2: no bad edges

In this subcase we assume that there is no edge$( i , j )$in Γ such that$i \in S _ { 1 } , j \in \{ 1 , \dots , n \} \setminus S _ { 1 }$

The integral over the boundary stratum is equal to the product$W _ { \Gamma _ { 1 } } \times W _ { \Gamma _ { 2 } }$where$\Gamma _ { 2 }$is the restriction of Γ to the subset$S _ { 1 } \sqcup S _ { 2 } \subset \{ 1 , \ldots , n \} \sqcup \{ \overline { { 1 } } , \ldots , \overline { { m } } \} = V _ { \Gamma }$, and$\Gamma _ { 1 }$is obtained by the contraction of all vertices in this set to a new vertex of the second type. Our condition guarantees that$\Gamma _ { 1 }$is an admissible graph. This corresponds to the second line in (F), where the product  on polydiferential operators appears.

![](images/page_26_image_0.jpg)

## 6.4.2.2. Second subcase of S2: there is a bad edge

Now we assume that there is an edge$( i , j )$in Γ such that$i \in S _ { 1 } , j \in \{ 1 , . . . , n \} \setminus S _ { 1 }$. In this case the integral is zero because of the condition$d \phi ( x , y ) = 0$if x stays on the line R.

![](images/page_26_image_3.jpg)

The reader can wonder about what happens if after the collapsing the graph will have multiple edges. Such terms do not appear in$( F )$. Nevertheless, we ingore them because in this case the diferential form which we integrate vanishes as it contains the square of 1-form.

Thus, we see that we exhausted all possibilities and get contributions of all terms in the formula (F). We proved that$c _ { \Gamma } = 0$for any Γ, and that  is an$L _ { \infty } .$-morphism.

## 6.4.3. We finish the proof of the theorem from 6.4

In order to check that it is a quasi-isomorphism, we should show that its component$\mathcal { U } _ { 1 }$coincides with$\mathcal { U } _ { 1 } ^ { ( 0 ) }$introduced in 4.6.1. It follows from definitions that every admissible graph with$n = 1$vertex of first type and$m \geq 0$vertices of the second type, and with m edges, is the following tree:

![](images/page_26_image_8.jpg)

The integral corresponding to this graph is$( 2 \pi ) ^ { m } / m !$. The map$\widetilde { U } _ { \Gamma }$from polyvector fields to polydifferential operators is the one which appears in 4.6.1:

$$
\xi_ {1} \wedge \dots \wedge \xi_ {m} \longrightarrow \frac {1}{m !} \sum_ {\sigma \in \Sigma_ {m}} s g n (\sigma) \cdot \xi_ {\sigma_ {1}} \otimes \dots \otimes \xi_ {\sigma_ {m}}, \quad \xi_ {i} \in \Gamma (\mathbf {R} ^ {d}, T).
$$

The theorem is proven. Q.E.D.

## 6.4.4. Comparison with the formula from section 2

The weight w<sub>Γ</sub> defined in section 2 difer from$W _ { \Gamma }$defined in 6.2 by factor$2 ^ { n } / n !$. On the other hand, the bidiferential operator$B _ { \Gamma , \alpha } ( f , g )$is$2 ^ { - n }$times$\mathcal { U } _ { \Gamma } ( \alpha \wedge \dots \wedge \alpha ) ( f \otimes g )$. The inverse factorial$1 / n !$appears in the Taylor series (see the end of 4.3). Thus, we obtain the formula from section 2.

## 6.5. Grading, orientations, factorials, signs

Homogeneous components of  are maps of graded spaces

$$
S y m ^ {n} ((\bigoplus_ {k \geq 0} \Gamma (\mathbf {R} ^ {d}, \wedge^ {k} T) [ - k ]) [ 2 ]) \longrightarrow (\underline {{H o m}} (A [ 1 ] ^ {\otimes m}, A [ 1 ])) [ 1 ]
$$

where Hom denotes the internal Hom in the tensor category$G r a d e d ^ { \mathbf { k } }$. We denote the expression from above by (E). First of all, in the expression (E) each polyvector field$\gamma _ { i } \in \Gamma ( \mathbf { R } ^ { d } , \wedge ^ { k _ { i } } T )$appears with the shift $2 - k _ { i }$. In our formula for the same$\gamma _ { i }$gives$k _ { i }$edges of the graph, and thus$k _ { i }$1-forms which we have to integrate. Also, it gives 2 dimensions for the integration domain$\overline { { C } } _ { n , m }$. Secondly, every function$f _ { j } \in A$ appears with shift 1 in (E) and gives 1 dimension to the integration domain. We are left with two shifts by 1 in (E) which are accounted for 2 dimensions of the group$\bar { G } ^ { ( 1 ) }$. From this it is clear that our formula for is compatible with Z-grading.

Moreover, it is also clear that things responsible for various signs in our formulas:

1) the orientation of$\overline { { C } } _ { n , m } .$7

2) the order in which we multiply 1-forms$d \phi _ { e }$

3) Z-gradings of vector spaces in (E),

are naturally decomposed into pairs. This implies that the enumeration of the set of vertices of Γ, and also the enumeration of edges in sets Star(v) for vertices v of the first type are not really used. Thus, we see that$\mathcal { U } _ { n }$is skew-symmetric.

Inverse factorials$1 / ( \# S t a r ( v ) ! )$kill the summation over enumerations of sets$S t a r ( v )$. The inverse factorial$1 / n !$is the final formula does not appear because we consider higher derivatives which are already multiplied by n!.

The last thing to check is that in our derivation of the fact that is an$L _ { \infty }$-morphism using Stokes formula we did not loose anywhere a sign. This is really hard to explain. How, for example, can one compare the standard orientation on C with shifts by 2 in$( E ) ?$As a hint to the reader we would like to mention that it is very convenient to$\mathrm { \Delta ^ { 6 6 } \mathrm { \ p u t } ^ { \mathrm { , 9 3 } } }$the resulting expression

$$
\Phi := \left(\mathcal {U} _ {\Gamma} \left(\gamma_ {1} \otimes \dots \otimes \gamma_ {n}\right)\right) \left(f _ {1} \otimes \dots \otimes f _ {m}\right)
$$

to the point$\infty$on the absolute. Also, we can not guarantee that we did not make errors when we write formulas in lines.

## 6.6. Vanishing of integrals

In this subsection we consider the space$C _ { n }$of$G ^ { ( 2 ) }$-equivalence classes of configurations of points on the Euclidean plane. Every two indices$i , j , \ i \neq j , 1 \leq i , j \leq n$give a forgetting map$C _ { n } { \longrightarrow } C _ { 2 } \simeq S ^ { 1 }$. We denote by$d \phi _ { i , j }$the closed 1-form on$C _ { n }$which is the pullback of the standard 1-form d(angle) on the circle. We use the same notation for the pullback of this form to Con$f _ { n }$

Lemma. Let$n \geq 3$be an integer. The integral over$C _ { n }$of the product of any$2 n - 3 = d i m ( C _ { n } )$closed 1-forms$d \phi _ { i _ { \alpha } , j _ { \alpha } } , \alpha = 1 , \ldots , 2 n - 3$, is equal to zero.

Proof: First of all, we identify$C _ { n }$with the subset$C _ { n } ^ { \prime }$of$C o n f _ { n }$consisting of configurations such that the point$p _ { i _ { 1 } }$is$0 \in \mathbf { C }$and$p _ { j _ { 1 } }$is on the unit circle$S ^ { 1 } \subset \mathbf { C }$. Also, we rewrite the form which we integrate as

$$
\bigwedge_ {\alpha = 1} ^ {2 n - 3} d \phi_ {i _ {\alpha}, j _ {\alpha}} = d \phi_ {i _ {1}, j _ {1}} \wedge \bigwedge_ {\alpha = 2} ^ {2 n - 3} d (\phi_ {i _ {\alpha}, j _ {\alpha}} - \phi_ {i _ {1}, j _ {1}}) .
$$

Let us map the space$C _ { n } ^ { \prime }$onto the space$C _ { n } ^ { \prime \prime } \subset C o n f _ { n }$consisting of configurations with$p _ { i _ { 1 } } = 0$and $p _ { j _ { 1 } } = 1$, applying rotations with the center at 0. Diferential forms$d ( \phi _ { i _ { \alpha } , j _ { \alpha } } - \phi _ { i _ { 1 } , j _ { 1 } } )$on$C _ { n } ^ { \prime }$are pullbacks of diferential forms$d \phi _ { i _ { \alpha } , j _ { \alpha } }$on$C _ { n } ^ { \prime \prime }$. The integral of a product of$2 n - 3$closed 1-forms$d \phi _ { i _ { \alpha } , j _ { \alpha } } , \ \alpha = 1 , \ldots , 2 n - 3$ over$C _ { n } ^ { \prime }$is equal to 2π times the integral of the product$2 n - 4$closed 1-forms$d \phi _ { i _ { \alpha } , j _ { \alpha } } , \alpha = 2 , \ldots , 2 n - 3$ over$C _ { n } ^ { \prime \prime }$

The space$C _ { n } ^ { \prime \prime }$is a complex manifold. We are calculating the absolutely converging integral of the type

$$
\int_ {C _ {n} ^ {\prime \prime}} \prod_ {\alpha} d A r g (Z _ {\alpha})
$$

where$Z _ { \alpha }$are holomorphic invertible functions on$C _ { n } ^ { \prime \prime }$(diferences between complex coordinates of points of the configuration). We claim that it is zero, because of the general result proven in 6.6.1. Q.E.D.

## 6.6.1. A trick using logarithms

Theorem. Let X be a complex algebraic variety ofdimension$N \geq 1$, and$Z _ { 1 } , \dots , Z _ { 2 N }$be rational functions on$X$, not equal identically to zero. Let U be any Zariski open subset ofX such that functions$Z _ { \alpha }$are defined and non-vanishing on$U _ { i }$and U consists of smooth points. Then the integral

$$
\int_ {U (\mathbf {C})} \wedge_ {\alpha = 1} ^ {2 N} d (A r g Z _ {\alpha})
$$

is absolutely convergent, and equal to zero.

This result seems to be new, although the main trick used in the proof is well-known. A. Goncharov told me that he also came to the same result in his study of mixed Tate motives.

Proof: First of all, we claim that the diferential form$\land _ { \alpha = 1 } ^ { 2 N } d A r g ( Z _ { \alpha } )$on$U ( \mathbf { C } )$coincides with the form $\Lambda _ { \alpha = 1 } ^ { 2 N } d L o g | Z _ { \alpha } |$(this is the trick).

We can replace$d A r g ( Z _ { \alpha } )$by the diference of a holomorphic an anti-holomorphic form

$$
\frac {1}{2 i} \left(d (L o g Z _ {\alpha}) - d (L o g \overline {{Z}} _ {\alpha})\right) .
$$

Thus, the form which we integrate over$U ( \mathbf { C } )$is a sum of products of holomorphic and of anti-holomorphic forms. The summand corresponding to a product of a non-equal number of holomorphic and of anti-holomorphic forms, vanishes identically because$U ( \mathbf { C } )$is a complex manifold. The conclusion is that the number of anti-holomorphic factors in non-vanishing summands is the same for all of them, it coincides with the complex dimension N of$U ( \mathbf { C } )$. The same products of holomorphic and of anti-holomorphic forms survive in the product

$$
\bigwedge_ {\alpha = 1} ^ {2 N} d \operatorname{Log} | Z _ {\alpha} | = \bigwedge_ {\alpha = 1} ^ {2 N} \frac {1}{2} \left(d (\operatorname{Log} Z _ {\alpha}) + d (\operatorname{Log} \overline {{Z}} _ {\alpha})\right).
$$

Let us choose a compactification$\overline { U }$of U such that${ \overline { { U } } } \setminus U$is a divisor with normal crossings. If$\phi$is a smooth diferential form on$U ( \mathbf { C } )$such that coeficients of φ are locally integrable on$\overline { { U } } ( \mathbf { C } )$, then we denote by$\mathcal { T } ( \phi )$corresponding diferential form on$\overline { { U } } ( \mathbf { C } )$with coeficients in the space of generalized functions.

Lemma. Let$\omega$be a form on$U ( \mathbf { C } )$which is a linear combination of products of functions$L o g \left| Z _ { \alpha } \right|$and of 1-forms d Log$| Z _ { \alpha } |$where$Z _ { \alpha } \in { \mathcal { O } } ^ { \times } ( U )$are regular invertible functions on U. Then coeficients of ω and of dω are locally$L ^ { 1 }$functions on$\overline { { U } } ( \mathbf { C } )$. Moreover,${ \mathcal { T } } ( d \omega ) = d ( { \mathcal { T } } ( \omega ) )$. Also, the integral$\textstyle \int \ \omega$is absolutely U(C)

convergent and equal to the integral (ω).

$$
\int_ {\overline {{U}} (\mathbf {C})} \mathcal {I} (\omega)
$$

The lemma is an elementary exercise in generalized functions, after passing to local coordinates on $\overline { { U } } ( \mathbf { C } )$. We leave details of the proof to the reader. Also, the statement of the lemma remains true without the condition that${ \overline { { U } } } \setminus U$is a divisor with normal crossings. Q.E.D.

The vanishing of the integral in the theorem is clear now by the Stokes formula:

$$
\begin{array}{l} \int_ {U (\mathbf {C})} \bigwedge_ {\alpha = 1} ^ {2 N} d   A r g \left(Z _ {\alpha}\right) = \int_ {U (\mathbf {C})} \bigwedge_ {\alpha = 1} ^ {2 N} d   L o g \left| Z _ {\alpha} \right| = \int_ {\overline {{U}} (\mathbf {C})} \mathcal {I} \left(d \left(L o g \left| Z _ {1} \right| \bigwedge_ {\alpha = 2} ^ {2 N} d   L o g \left| Z _ {\alpha} \right|\right)\right) = \\ = \int_ {\overline {{U}} (\mathbf {C})} d \left(\mathcal {I} \left(L o g \left| Z _ {1} \right| \bigwedge_ {\alpha = 2} ^ {2 N} d   L o g \left| Z _ {\alpha} \right|\right)\right) = 0. Q. E. D. \end{array}
$$

## 6.6.2. Remark

The vanishing of the integral in the lemma from 6.6 has higher-dimensional analogue which is crucial in the perturbative Chern-Simons theory in the dimension 3, and its generalizations to dimensions$\geq 4$(see $[ \mathrm { K o } 1 ] )$. However, the vanishing of integrals in dimensions$\geq 3$follows from a much simpler fact which is the existence of a geometric involution making the integral equal to minus itself. In the present paper we will use many times such kind of arguments involving involutions.

## 7. Formality conjecture for general manifolds

In this section we establish the formality conjecture for general manifolds, not only for open domains in $\mathbf { R } ^ { d }$. It turns out that that essentially all work is already done. The only new analytic result is vanishing of certain integrals over configuration spaces, analogous to the lemma from 6.6.

One can treat$\mathbf { R } _ { f o r m a l } ^ { d } ,$the formal completion of vector space$\mathbf { R } ^ { d }$at zero, in many respects as usual manifold. In particular, we can define diferential graded Lie algebras$D _ { p o l y } ( \mathbf { R } _ { f o r m a l } ^ { d } )$and$T _ { p o l y } ( \mathbf { R } _ { f o r m a l } ^ { d } )$ The Lie algebra$W _ { d } : = V e c t ( \mathbf { R } _ { f o r m a l } ^ { d } )$is the standard Lie algebra of formal vector fields. We consider$W _ { d }$as a diferential graded Lie algebra (with the trivial grading and the diferential equal to 0). There are natural homomorphisms of diferential graded Lie algebras:

$$
m _ {T}: W _ {d} \longrightarrow T _ {p o l y} (\mathbf {R} _ {f o r m a l} ^ {d}), m _ {D}: W _ {d} \longrightarrow D _ {p o l y} (\mathbf {R} _ {f o r m a l} ^ {d}),
$$

because vector fields can be considered as polyvector fields and as diferential operators.

We will use the following properties of the quasi-isomorphism from 6.4:

P1) can be defined for$\mathbf { R } _ { f o r m a l } ^ { d }$as well,

P2) for any$\xi \in W _ { d }$we have the equality

$$
\mathcal {U} _ {1} (m _ {T} (\xi)) = m _ {D} (\mathcal {U} _ {1} (\xi)),
$$

P3)  is$G L ( d , \mathbf { R } )$-equivariant,

P4) for any$k \ge 2 , \xi _ { 1 } , \ldots , \xi _ { k } \in W _ { d }$we have the equality

$$
\mathcal {U} _ {k} (m _ {T} (\xi_ {1}) \otimes \dots \otimes m _ {T} (\xi_ {k})) = 0
$$

P5) for any$k \ge 2 , \xi \in g l ( d , \mathbf { R } ) \subset W _ { d }$, and for any$\eta _ { 2 } , \mathbf { \eta } _ { 2 } , \mathbf { \eta } _ { 3 } , \mathbf { \eta } _ { 4 } , \eta _ { k } \in T _ { p o l y } ( \mathbf { R } _ { f o r m a l } ^ { d } )$we have

$$
\mathcal {U} _ {k} (m _ {T} (\xi) \otimes \eta_ {2} \otimes \dots \otimes \eta_ {k}) = 0.
$$

We will construct quasi-isomorphisms from$T _ { p o l y } ( X )$to$D _ { p o l y } ( X )$for arbitrary d-dimensional manifold X using only properties P1-P4 of the map . Properties P1,P2 and P3 are evident, and the properties P4,P5 will be established later (subsections 7.3.1.1 and 7.3.3.1).

It will be convenient to use in this section the geometric language of formal graded manifolds, instead of the algebraic language of$L _ { \infty } { \mathrm { - a l g e b r a s } }$. Let us fix the dimension d$\mathbf { \Xi } \in \mathbf { N }$. We introduce three formal graded Q-manifolds without base points:

$$
\mathcal {T}, \mathcal {D}, \mathcal {W}.
$$

These formal graded Q-manifolds are obtained in the usual way from diferential graded Lie algebras $T _ { p o l y } ( R _ { f o r m a l } ^ { d } ) , D _ { p o l y } ( R _ { f o r m a l } ^ { d } )$and$W _ { d }$forgetting base points.

In next two subsections (7.1 and 7.2) we present two general geometric constructions, which will used in 7.3 for the proof of formality of$D _ { p o l y } ( X )$

## 7.1. Formal geometry (in the sense of I. Gelfand and D. Kazhdan)

Let X be a smooth manifold of dimension d. We associate with X two infinite-dimensional manifolds, $X ^ { c o o r }$and$X ^ { a f f }$. The manifold$X ^ { c o o r }$consists of pairs$( x , f )$where x is a point of X and f is an infinite germ of a coordinate system on X at x,

$$
f: (\mathbf {R} _ {f o r m a l} ^ {d}, 0) \hookrightarrow (X, x).
$$

We consider$X ^ { c o o r }$as a projective limit of finite-dimensional manifolds (spaces of finite germs of coordinate systems). There is an action on$X ^ { c o o r }$of the (pro-Lie) group$G _ { d }$of formal difeomorphisms of$\mathbf { R } ^ { d }$preserving base point 0. The natural projection map$X ^ { c o o r } { \longrightarrow } \dot { X }$is a principal$G _ { d } { \mathrm { - b u n d l e } }$

The manifold$X ^ { a f f }$is defined as the quotient space$X ^ { c o o r } / G L ( d , \mathbf { R } )$. It can be thought as the space of formal afine structures at points of X. The main reason to introduce$X ^ { a f f }$is that fibers of the natural projection map$X ^ { a f f } { \longrightarrow } X$are contractible.

The Lie algebra of the group$G _ { d }$is a subalgebra of codimension d in$W _ { d }$. It consists of formal vector fields vanishing at zero. Thus,$L i e ( G _ { d } )$acts on$X ^ { c o o r }$. It is easy to see that in fact the whole Lie algebra $W _ { d }$acts on$X ^ { c o o r }$and is isomorphic to the tangent space to$X ^ { c o o r }$at each point. Formally, the infinitedimensional manifold$X ^ { c o o r }$looks as a principal homogeneous space of the non-existent group with the Lie algebra$W _ { d }$

The main idea of formal geometry (se [GK]) is to replace d-dimensional manifolds by “principal homogeneous spaces” of$W _ { d }$. Diferential-geometric constructions on$X ^ { c o o r }$can be obtained from Lie-algebraic constructions for$W _ { d }$. For a while we will work only with$X ^ { c o o r }$, and then at the end return to$X ^ { a f f }$. In terms of Lie algebras it corresponds to the diference between absolute and relative cohomology.

## 7.2. Flat connections and Q-equivariant maps

Let M be a$C ^ { \infty }$-manifold (or a complex analytic manifold, or an algebraic manifold, or a projective limit of manifolds,...). Denote by ΠTM the supermanifold which is the total space of the tangent bundle of M endowed with the reversed parity. Functions on the ΠTM are diferential forms on M. The de Rham diferential$d _ { M }$on forms can be considered as an odd vector field on ΠTM with the square equal to 0. Thus, ΠTM is a Q-manifold. It seems that the accurate notation for ΠTM considered as a graded manifold should be$T [ 1 ] M$(the total space of the graded vector bundle$T _ { M } [ 1 ]$considered as a graded manifold).

Let$N { \longrightarrow } M$be a bundle over a manifold M whose fibers are manifolds, or vector spaces, etc., endowed with a flat connection . Denote by E the pullback of this bundle to$B : = \Pi T M$. The connection gives a lift of the vector field$Q _ { B } : = d _ { M }$on B to the vector field$Q _ { E }$on E. This can be done for arbitrary connection, and only for flat connection the identity$[ Q _ { E } , Q _ { E } ] = 0$holds.

A generalization of a (non-linear) bundle with a flat connection is a Q-equivariant bundle whose total space and the base are Q-manifolds. In the case of graded vector bundles over$T [ 1 ] M$this notion was introduced Quillen under the name of a superconnection (see [Q]). A generalization of the notion of a covariantly flat morphism from one bundle to another is the notion of a Q-equivariant map.

Definition. A flat family over Q-manifold B is a pair$( p : E { \longrightarrow } B , \sigma )$where$p : E { \longrightarrow } B$is a Q-equivariant bundle whose fibers are formal manifolds, and a$\sigma : B { \longrightarrow } E$is a Q-equivariant section of this bundle.

In the case$B = \{ p o i n t \}$a flat family over B is the same a formal Q-manifold with base point. It is clear that flat families over a given Q-manifold form a category.

We apologize for the terminology. More precise name for “flat families” would be “flat families of pointed formal manifolds”, but it is too long.

One can define analogously flat graded families over graded Q-manifolds.

We refer the reader to a discussion of further examples of Q-manifolds in [Ko3].

## 7.3. Flat families in deformation quantization

Let us return to our concrete situation. We construct in this section two flat families over ΠTX (where X is a d-dimensional manifold), and a morphism between them. This will be done in several steps.

## 7.3.1. Flat families over

The first bundle over  is trivial as a Q-equivariant bundle,

$$
\mathcal {T} \times \mathcal {W} \longrightarrow \mathcal {W}
$$

but with a non-trivial section$\sigma _ { T }$. This section is not the zero section, but the graph of the Q-equivariant map$\mathcal { W } { \longrightarrow } \mathcal { T }$coming from the homomorphism of diferential graded Lie algebras$m _ { T } : W _ { d } { \longrightarrow } T _ { p o l y } ( { \bf R } _ { f o r m a l } ^ { d } )$ Analogously, the second bundle is the trivial Q-equivariant bundle

$$
\mathcal {D} \times \mathcal {W} \longrightarrow \mathcal {W}
$$

with the section$\sigma _ { \mathcal { D } }$coming from the homomorphism$m _ { D } : W _ { d } { \longrightarrow } D _ { p o l y } ( { \bf R } _ { f o r m a l } ^ { d } )$

Formulas from 6.4 give a Q-equivariant map$\mathcal { U } : \mathcal { T } \longrightarrow \mathcal { D }$

Lemma. The morphism$( \mathcal { U } \times i d _ { \mathcal { W } } ) : \mathcal { T } \times \mathcal { W } \longrightarrow \mathcal { D } \times \mathcal { W }$is a morphism of flat families over .

Proof: We have to check that$( \mathcal { U } \times i d \mathcal { w } )$maps one section to another, i.e. that

$$
\left(\mathcal {U} \times i d _ {\mathcal {W}}\right) \circ \sigma_ {\mathcal {T}} = \sigma_ {D} \in M a p s (\mathcal {W}, \mathcal {D} \times \mathcal {W}).
$$

We compare Taylor coeficients. The linear part$\mathcal { U } _ { 1 }$of maps a vector field (considered as a polyvector field) to itself, considered as a diferential operator (property P2). Components$\mathcal { U } _ { k } ( \xi _ { 1 } , \dots , \xi _ { k } )$for$k \geq 2 , \ \xi _ { i } \in$ $T ^ { 0 } ( { \dot { \mathbf { R } } } ^ { d } ) = \Gamma ( { \mathbf { R } } ^ { d } , T )$vanish, which is the property$\mathrm { P 4 } . \qquad Q . E . D .$

## 7.3.1.1. Proof of the property P4

Graphs appearing in the calculation of$\mathcal { U } _ { k } ( \xi _ { 1 } , \dots , \xi _ { k } )$have k edges, k vertices of the first type, and m vertices of the second type, where

$$
2 k + m - 2 = k.
$$

Thus, there are no such graphs for$k \geq 3$as m is non-negative. The only intersting case is$k = 2 , m = 0$ The graph is looking as

By our construction,$\boldsymbol { { \mathcal { U } } } _ { 2 }$restricted to vector fields is equal to the non-trivial quadratic map

$$
\xi \longmapsto \sum_ {i, j = 1} ^ {d} \partial_ {i} (\xi^ {j}) \partial_ {j} (\xi^ {i}) \in \Gamma (\mathbf {R} ^ {d}, \mathcal {O}), \quad \xi = \sum_ {i} \xi^ {i} \partial_ {i} \in \Gamma (\mathbf {R} ^ {d}, T)
$$

with the weight

$$
\int_ {C _ {2, 0}} d \phi_ {(1 2)} d \phi_ {(2 1)} = \int_ {\mathcal {H} \backslash \{z _ {0} \}} d \phi (z, z _ {0}) \wedge d \phi (z _ {0}, z)
$$

where$z _ { \mathrm { 0 } }$is an arbitrary point of$\mathcal { H } .$

Lemma. For arbitrary angle map the integral$\underset { \mathcal { H } \backslash \{ z _ { 0 } \} } { \int } d \phi ( z , z _ { 0 } ) \wedge d \phi ( z _ { 0 } , z )$is equal to zero.

Proof: We have a map$\overline { { C } } _ { 2 , 0 } { \longrightarrow } S ^ { 1 } \times S ^ { 1 } , [ ( x , y ) ] \mapsto ( \phi ( x , y ) , \phi ( y , x ) )$. We calculate the integral of the pullback of the standard volume element on two-dimensional torus. It is easy to see that the integral does not depend on the choice of map$\phi : \overline { { { C } } } _ { 2 , 0 } \mathrm { - } \varDelta S ^ { 1 }$. The reason is that the image of the boundary of the integration domain$\partial \overline { { C } } _ { 2 , 0 }$in$S ^ { 1 } \times S ^ { 1 }$cancels with the reflected copy of itself under the involution$\left( \phi _ { 1 } , \phi _ { 2 } \right) \mapsto \left( \phi _ { 2 } , \phi _ { 1 } \right)$of the torus$S ^ { 1 } \times S ^ { 1 }$. Let us assume that$\phi = \phi ^ { h }$and$z _ { 0 } = 0 + 1 \cdot i$. The integral vanishes because the involution $z \mapsto - { \overline { { z } } }$reverses the orientation of and preserves the form$d \phi ( z , z _ { 0 } ) \wedge d \phi ( z _ { 0 } , z ) . \qquad Q . E . D .$

## 7.3.2. Flat families over$\Pi T ( X ^ { c o o r } )$

If X is a d-dimensional manifold, then there is a natural map of Q-manifolds (the Maurer-Cartan form)

$$
\Pi T (X ^ {c o o r}) \longrightarrow \mathcal {W}.
$$

It follows from following general reasons. If G is a Lie group, then it acts freely by left translations on itself, and also on ΠTG. The quotient Q-manifold Π$\mathrm { ? } G / G$is equal to Πg where$\mathbf { g } = L i e ( G )$. Thus, we have a Q-equivariant map

$$
\Pi T G \longrightarrow \Pi \mathbf {g}.
$$

Analogous construction works for any principal homogeneous space over G. We apply it to$X ^ { c o o r }$considered as a principal homogeneous space for a non-existent group with the Lie algebra$W _ { d }$

The pullbacks of flat families of formal manifolds over$\mathcal { W }$constructed in 7.3.1, are two flat families over $\Pi T ( X ^ { c o o r } )$. As Q-equivariant bundles these families are trivial bundles

$$
\mathcal {T} \times \Pi T (X ^ {c o o r}) {\longrightarrow} \Pi T (X ^ {c o o r}), \mathcal {D} \times \Pi T (X ^ {c o o r}) {\longrightarrow} \Pi T (X ^ {c o o r}).
$$

Pullbacks of sections$\sigma _ { T }$and$\sigma _ { \mathcal { D } }$gives sections in the bundles above. These sections we denote again by$\sigma _ { T }$ and$\sigma _ { \mathcal { D } }$. The pullback of the morphism${ \mathcal { U } } \times i d { \boldsymbol { \omega } }$is also a morphism of flat families.

## 7.3.3. Flat families over$\Pi T ( X ^ { a f f } )$

Recall that$X ^ { a f f }$is the quotient space of$X ^ { c o o r }$by the action of$G L ( d , \bf R )$. Thus, from functorial properties of operation$\Pi T ~ ( = M a p s ( { \bf R } ^ { 0 | 1 } , \cdot ) )$follows that$\Pi T ( X ^ { a f f } )$is the quotient of Q-manifold$\Pi T ( X ^ { c o o r } )$ by the action of Q-group$\overline { { \Pi T ( G } } L ( d , { \bf R } ) )$. We will construct an action of$\Pi T ( G L ( d , { \bf R } ) )$on flat families $\mathcal { T } \times \Pi T ( X ^ { c o o r } )$and$\mathcal { D } \times \Pi T ( X ^ { c o o r } )$over$\Pi T ( X ^ { c o o r } )$. We claim that the morphism between these families is invariant under the action of$\Pi T ( G L ( d , { \bf R } ) )$. Flat families over$\Pi T ( X ^ { a f f } )$will be defined as quotient families. The morphism between them will be the quotient morphism.

The action of$\Pi T ( G L ( d , { \bf R } ) )$on$\tau$and on$\mathcal { W }$is defined as follows. First of all, if G is a Lie group with the Lie algebra g, then ΠTG acts Q-equivariantly on Q-manifold Πg, via the identification$\Pi \mathbf { g } = \Pi T G / G$ Analogously, if$\mathbf { g }$is a subalgebra of a larger Lie algebra$\mathbf { g } _ { 1 } .$, and an action of$G$on$\mathbf { g } _ { 1 }$is given in a way compatible with the inclusion$\mathbf { g } { \hookrightarrow } \mathbf { g } _ { 1 }$, then ΠTG acts on Πg<sub>1</sub>. We apply this construction to the case ${ \cal G } = { \cal G } L ( n , { \bf R } )$and${ \bf g } _ { 1 } = T _ { p o l y } ( { \bf R } _ { f o r m a l } ^ { d } )$or${ \bf g } _ { 1 } = D _ { p o l y } ( { \bf R } _ { f o r m a l } ^ { d } )$

One can check easily that sections$\sigma _ { T }$and$\sigma _ { \mathcal { D } }$over$\Pi T ( X ^ { c o o r } )$are$\Pi T ( G L ( d , { \bf R } ) )$)-equivariant. Thus, we get two flat families over$\Pi T ( X ^ { a f f } )$

The last thing we have to check is that the morphism$\mathcal { U } \times i d _ { \Pi T ( X ^ { c o o r } ) }$of flat families

$$
\mathcal {T} \times \Pi T (X ^ {\text { coor }}) \longrightarrow \mathcal {D} \times \Pi T (X ^ {\text { coor }})
$$

is$\Pi T ( G L ( d , { \bf R } ) )$)-equivariant. After the translation of the problem to the language of Lie algebras, we see that we should check that${ \mathcal { U } } \operatorname { i s } G L ( d , \mathbf { R } )$-invariant (property$\mathrm { P 3 } .$that is clear by our construction), and that if we substitute an element of${ \mathfrak { g l } } ( d , \mathbf { R } ) \subset W _ { d }$$\boldsymbol { \mathcal { U } } _ { \ge 2 }$, we get zero (property$\mathrm { P 5 }$, see 7.3.3.1).

Conclusion. We constructed two flat families over$\Pi T ( X ^ { a f f } )$and a morphism between them. Fibers of these families are isomorphic to and to .

## 7.3.3.1. Property P5

This is again reduces to the calculation of an integral. Let v be a vertex of Γ to which we put element of${ \mathbf { } } g l ( d , \mathbf { R } )$. There is exactly one edge starting at v because we put a vector field here. If there are no edges ending at$v ,$then the integral is zero because the domain of integration is foliated by lines along which all forms vanish. These lines are level sets of the function$\phi ( z , w )$where$w \in \mathcal { H } \sqcup \mathbf { R }$is fixed and z is the point on corresponding to v.

![](images/page_33_image_9.jpg)

If there are at least 2 edges ending at$v ,$then the corresponding polydiferential operator is equal to zero, because second derivatives of coeficients of a linear vector field vanish.

The only relevant case is when there is only one edge starting at$v ,$and only one edge ending there. If these two edges connect our vertex with the same vertex of Γ, then the vanishing follows from the lemma in the section 7.3.2.1. If our vertex is connected with two diferent vertices,

![](images/page_34_image_0.jpg)

then we apply the following two lemmas:

Lemma. Let$z _ { 1 } \neq z _ { 2 } \in \mathcal { H }$be two distinct points on . Then the integral

$$
\int_ {z \in \mathcal {H} \backslash \{z _ {1}, z _ {2} \}} d \phi (z _ {1}, z) \wedge d \phi (z, z _ {2})
$$

vanishes.

Lemma. Let$z _ { 1 } \in \mathcal { H } , z _ { 2 } \in \mathbf { R }$be two points on${ \mathcal { H } } \sqcup \mathbf { R }$. Then the integral

$$
\int_ {z \in \mathcal {H} \backslash \{z _ {1}, z _ {2} \}} d \phi (z _ {1}, z) \wedge d \phi (z, z _ {2})
$$

vanishes.

Proof: One can prove analogously to the lemma in 7.3.1.1 that the integral does not depend on the choice of an angle map, and also on points$z _ { 1 } , \ z _ { 2 }$. In the case of$\phi = \phi ^ { h }$and both points$z _ { 1 } , z _ { 2 }$are pure imaginary, the vanishing follows from the anti-symmetry of the integral under the involution$z \mapsto - { \overline { { z } } }$ $Q . E . D .$

## 7.3.4. Flat families over X

Let us choose a section$s ^ { a f f }$of the bundle$X ^ { a f f } { \longrightarrow } X$. Such section always exists because fibers of this bundle are contractible. For example, any torsion-free connection  on the tangent bundle to X gives a section$X { \longrightarrow } X ^ { a f f }$. Namely, the exponential map for gives an identification of a neighborhood of each point$x \in X$with a neighborhood of zero in the vector space$T _ { x } X$, i.e. an afine structure on X near x, and a point of$X ^ { a f f }$over$x \in X$

The section$s ^ { a f f }$defines a map of formal graded Q-manifolds$\Pi T X { \longrightarrow } \Pi T ( X ^ { a f f } )$. After taking the pullback we get two flat families$\mathcal { T } _ { s ^ { a f f } }$and$\mathcal { D } _ { s ^ { a f f } }$over ΠTX and an morphism$m _ { s ^ { a f f } }$from one to another.

We claim that these two flat families admit definitions independent of$s ^ { a f f }$. Only the morphism$m _ { s ^ { a f f } }$ depends on$s ^ { a f f }$

Namely, let us consider infinite-dimensional bundles of diferential graded Lie algebras$j e t s _ { \infty } T _ { p o l y }$and $j e t s _ { \infty } D _ { p o l y }$over X whose fibers at$x \in X$are spaces of infinite jets of polyvector fields or polydiferential operators at x respectively. These two bundles carry natural flat connections (in the usual sense, not as in 7.2) as any bundle of infinite jets. Thus, we have two flat families (in generalized sense) over ΠTX.

Lemma. Flat families$\mathcal { T } _ { s ^ { a f f } }$and$\mathcal { D } _ { s ^ { a f f } }$are canonically isomorphic to flat families described just above.

Proof: it follows from definitions that pullbacks of bundles$j e t s _ { \infty } T _ { p o l y }$and$j e t s _ { \infty } D _ { p o l y }$from X to $X ^ { c o o r }$are canonically trivialized. The Maurer-Cartan 1-forms on$X ^ { c o o r }$with values in graded Lie algebras $T _ { p o l y } ( \mathbf { R } _ { f o r m a l } ^ { d } )$or$D _ { p o l y } ( \mathbf { R } _ { f o r m a l } ^ { d } )$come from pullbacks of flat connections on bundles of infinite jets. Thus, we identified our flat families over$\Pi T ( X ^ { c o o r } )$with pullbacks. The same is true for$X ^ { a f f } . \qquad Q . E . D$

## 7.3.5. Passing to global sections

If in general$( p : E { \longrightarrow } B , \sigma )$is a flat family, then one can make a new formal pointed Q-manifold:

$$
\left(\Gamma (E \longrightarrow B) _ {f o r m a l}, \sigma\right).
$$

This is an infinite-dimensional formal super manifold, the formal completion of the space of sections of the bundle$E { \longrightarrow } B$at the point σ. The structure of Q-manifold on$\Gamma ( E { \longrightarrow } B )$is evident because the Lie supergroup$\mathbf { R } ^ { 0 | 1 }$acts on$E { \longrightarrow } B$

Lemma. Formally completed spaces of global sections of flat families$\mathcal { T } _ { s ^ { a f f } }$and$\mathcal { D } _ { s ^ { a f f } }$a naturally quasi-isomorphic to$T _ { p o l y } ( X )$and$D _ { p o l y } ( X )$respectively.

Proof: It is well-known that if$E { \longrightarrow } X$is a vector bundle then de Rham cohomology of X with coeficients in formally flat infinite-dimensional bundle$j e t s _ { \infty } E$are concentrated in degree 0 and canonically isomorphic to the vector space$\Gamma ( X , E )$. Moreover, the natural homomorphism of complexes

$$
\bigl (\Gamma (X, E) [ 0 ], \text {   differential   } = 0 \bigr) \longrightarrow \bigl (\Omega^ {*} (X, j e t s _ {\infty} (E)), \text {   de   Rham   differential   } \bigr)
$$

is quasi-isomorphism.

Using this fact, the lemma from the previous subsection, and appropriate filtrations (for spectral sequences) one sees that that the natural Q-equivariant map from the formal Q-manifold$( T _ { p o l y } ( X ) _ { f o r m a l } [ 1 ] , 0 )$ to$( \Gamma ( \overrightharpoon { T _ { s ^ { a f f } } } \overrightarrow { \longrightarrow } T [ 1 ] X ) _ { f o r m a l } , \sigma _ { T } )$(and analogous map for$D _ { p o l y } )$is a quasi-isomorphism.$Q . E . D .$

It follows from the lemma above and the result of 4.6.1.1 that we have a chain of quasi-isomorphisms

$$
T _ {p o l y} (X) [ 1 ] _ {f o r m a l} \longrightarrow \Gamma (\mathcal {T} _ {s ^ {a f f}} \longrightarrow T [ 1 ] X) _ {f o r m a l} \longrightarrow \Gamma (\mathcal {D} _ {s ^ {a f f}} \longrightarrow T [ 1 ] X) _ {f o r m a l} \longleftarrow T _ {p o l y} (X) [ 1 ] _ {f o r m a l}.
$$

Thus, diferential graded Lie algebras$T _ { p o l y } ( X )$and$D _ { p o l y } ( X )$are quasi-isomorphic. The theorem from 4.6.2. is proven.$Q . E . D$

The space of sections of the bundle$X ^ { a f f } { \longrightarrow } X$is contractible. From this fact one can conclude that the quasi-isomorphism constructed above is well-defined homotopically.

## 8. Cup-products

## 8.1. Cup-products on tangent cohomology

Diferential graded Lie algebras$T _ { p o l y } , D _ { p o l y }$and (more generally) shifted by [1] Hochschild complexes of arbitrary associative algebras, all carry an additional structure. We do not know at the moment a definition, it should be something close to so called homotopy Gerstenhaber algebras (see [GV], [GJ]), although definitely not precisely this. At least, a visible part of this structure is a commutative associative product of degree +2 on cohomology of the tangent space to any solution of the Maurer-Cartan equation. Namely, if g is one of diferential graded Lie algebras listed above and$\gamma \in ( \mathbf { g } \otimes \mathbf { m } ) ^ { 1 }$satisfies$\begin{array} { r } { d \gamma + \frac { 1 } { 2 } [ \gamma , \gamma ] = 0 } \end{array}$where m is a finite-dimensional nilpotent non-unital diferential graded commutative associative algebra, the tangent space$T _ { \gamma }$is defined as complex$\gamma \otimes \mathbf { m } [ 1 ]$endowed with the diferential$d + [ \gamma , \cdot ]$. Cohomology space$H _ { \gamma }$of this diferential is a graded module over graded algebra$H ( \mathbf { m } )$(the cohomology space of m as a complex).$\operatorname { I f } \gamma _ { 1 }$ and$\gamma _ { 2 }$are two gauge equivalent solutions, then$H _ { \gamma _ { 1 } }$and$H _ { \gamma _ { 2 } }$are (non-canonically) equivalent m-modules.

We define now cup-products for all three diferential graded Lie algebras listed at the beginning of this section. For$T _ { p o l y } ( X )$the cup-product is defined as the usual cup-product of polyvector fields (see 4.6.1). One can check directly that this cup-product is compatible with the diferential$d + [ \gamma , \cdot ]$, and is a graded commutative associative product. For the Hochschild complex of an associative algebra A the cup-product on$H _ { \gamma }$is defined in a more tricky way. It is defined on the complex by the formula

$$
(t _ {1} \cup t _ {2}) (a _ {0} \otimes \dots \otimes a _ {n}) :=
$$

$$
\sum_ {0 \leq k _ {1} \leq k _ {2} \leq k _ {3} \leq k _ {4} \leq n} \pm \gamma^ {n - (k _ {2} - k _ {1} + k _ {4} - k _ {3})} (a _ {0} \otimes \dots \otimes t _ {1} (a _ {k _ {1}} \otimes \dots) \otimes a _ {k _ {2}} \otimes \dots \otimes t _ {2} (a _ {k _ {3}} \otimes \dots) \otimes a _ {k _ {4}} \otimes \dots)
$$

where$\gamma ^ { l } \in ( \mathbf { k } [ 0 ] \cdot 1 \oplus \mathbf { m } ) ^ { 1 - l } \otimes H o m ( A ^ { \otimes ( l + 1 ) } , A )$is homogeneous component of$\left( \gamma + 1 \otimes m _ { A } \right)$

It is not a trivial check that the cup-product on the Hochschild complex is compatible with diferentials, and also is commutative, associative and gauge-equivariant on the level of cohomology. Formally, we will not use this fact. The proof is a direct calculation with Hochschild cochains. Even if one replaces formulas by appropriate pictures the calculation is still quite long, about 4-5 pages of tiny drawings. Alternatively, there is a simple abstract explanation using the interpretation of the deformation theory related with the shifted Hochschild complex as a deformation theory of triangulated categories (or, better,$A _ { \infty } .$-categories, see [Ko4]). We will discuss it in more details in the sequel to the present paper.

We define the cup-product for$D _ { p o l y } ( X )$by the restriction of formulas for the cup-product in$C ^ { \bullet } ( A , A )$

## 8.2. Compatibility of  with cup-products

Theorem. The quasi-isomorphism  constructed in section 6 maps the cup-product for$T _ { p o l y } ( X )$to the cup-product for$D _ { p o l y } ( X )$.

Sketch of the proof: we translate the statement of the theorem to the language of graphs and integrals. The tangent map is given by integrals where one of vertices of the first type is marked. This is the vertex where we put a representative t for the tangent element$[ t ] \in H _ { \gamma }$. We put copies of$\gamma$(which is a polyvector field with values in m) into all other vertices of the first type. The rule which we just described follows directly from the Leibniz formula applied to the Taylor series for$\mathcal { U } .$

Now we are interested in the behavior of the tangent map with respect to a bilinear operation on the tangent space. It means that we have now two marked vertices of the first type.

## 8.2.1. Pictures for the cup-product in polyvector fields

We claim that the cup-product for the case$T _ { p o l y } ( X )$corresponds to pictures where two points (say, $p _ { 1 } , p _ { 2 } )$where we put representatives of elements of$H _ { \gamma }$which we want to multiply, are infinitely close points on . Precisely, it means that we integrate over preimages$P _ { \alpha }$of some point α in${ \bf R } / 2 \pi { \bf Z } \simeq C _ { 2 } \subset \overline { { C } } _ { 2 , 0 }$with respect to the forgetting map

$$
\overline {{{C}}} _ {n, m} \longrightarrow \overline {{{C}}} _ {2, 0}.
$$

It is easy to see that$P _ { \alpha }$has codimension 2 in$\overline { { C } } _ { n , m }$and contains no strata$C _ { T }$of codimension 2. It implies that as a singular chain$P _ { \alpha }$is equal to the sum of closures of non-compact hypersurfaces

$$
P _ {\alpha} \cap \partial_ {S} (\overline {{C}} _ {n, m}), P _ {\alpha} \cap \partial_ {S _ {1}, S _ {2}} (\overline {{C}} _ {n, m})
$$

in boundary strata of$\overline { { C } } _ { n , m }$. It is easy to see that intersections$P _ { \alpha } \cap \partial _ { S _ { 1 } , S _ { 2 } } ( \overline { { C } } _ { n , m } )$are empty, and intersection $P _ { \alpha } \cap \partial _ { S } ( \overline { { C } } _ { n , m } )$is non-empty if$S \supseteq \{ 1 , 2 \}$. The picture is something like

![](images/page_36_image_13.jpg)

Points$p _ { 1 }$and$p _ { 2 }$should not be connected by an edge because otherwise the integral vanishes, there is no directions over which we can integrate form$d \phi ( p _ { 1 } , p _ { 2 } )$. Also, if$\sharp S \geq 3$then the integral vanishes by lemma from 6.6. The only non-trivial case which is left is when$S = \{ 1 , 2 \}$and points$p _ { 1 } , p _ { 2 }$are not connected:

![](images/page_37_image_0.jpg)

This figure exactly corresponds to the cup-product in$T _ { p o l y } ( X )$

## 8.2.2. Pictures for the cup-product in the Hochschild complex

The cup-product for$D _ { p o l y } ( X )$is given by pictures where these two points are separated and infinitely close to R. Again, the precise definition is that we integrate of the preimage$P _ { 0 , 1 }$of point$[ ( 0 , 1 ) ] \in \overline { { C } } _ { 0 , 2 } \subset$ $\overline { { C } } _ { 2 , 0 } .$Analysis analogous to the one from the previous subsection shows that$P _ { 0 , 1 }$does not intersect any boundary stratum of$\overline { { C } } _ { n , m }$. Thus, as a chain of codimension 2 this preimage$P _ { 0 , 1 }$coincides with the union of closures of strata$C _ { T }$of codimension 2 such that$C _ { T } \subseteq P _ { 0 , 1 }$. It is easy to see that any such stratum give pictures like the one below where there is no arrow going from circled regions outside (as in the picture in 6.4.2.2),

![](images/page_37_image_4.jpg)

and we get exactly the cup-product in the tangent cohomology of the Hochschild complex as was described above.

## 8.2.3. Homotopy between two pictures

Choosing a path form one (limiting) configuration of two points on  to another configuration,

![](images/page_38_image_0.jpg)

we see that two products coinside on the level of cohomology. Q.E.D.

## 8.3. First application: Duflo-Kirillov isomorphism

## 8.3.1. Quanization of the Kirillov-Poisson bracket

Let g be a finite-dimensional Lie algebra over R. The dual space to g endowed with the Kirillov-Poisson bracket is naturally a Poisson manifold (see [Ki]). We remind here the formula for this bracket: if$p \in \mathbf { g } ^ { * }$is a point and$f , g$are two functions on g then the value$\{ f , g \} _ { | p }$is defined as$\langle p , [ d f _ { | p } , d g _ { | p } ] \rangle$where diferentials of functions$f , g$at$p$are considered as elements of${ \bf g } \simeq ( { \bf g } ^ { * } ) ^ { * }$. One can consider$\mathbf { g } ^ { * }$as an algebraic Poisson manifold because coeficients of the Kirillov-Poisson bracket are linear functions on$\mathbf { g } ^ { * }$

Theorem. The canonical quantization of the Poisson manifold$\mathbf { g } ^ { * }$is isomorphic to the family of algebras $\mathcal { U } _ { \hbar } ( \mathbf { g } )$defined as universal enveloping algebras of g endowed with the bracket$\hbar [ , ]$

Proof: in 6.4 we constructed a canonical star-product on the algebra of functions on a afine space for a given Poisson structure. Thus, we have canonical star-product on$C ^ { \infty } ( \mathbf { g } ^ { * } )$. We claim that the product of any two polynomials on$\mathbf { g } ^ { * }$is a polynomial in ¯h with coeficients which are polynomials on$\mathbf { g } ^ { * }$. The reason is that the star-product is constructed using contraction of indices. Let us denote by$\beta \in \mathbf { g } ^ { * } \otimes \mathbf { g } ^ { * } \otimes \mathbf { g }$the tensor giving the Lie bracket on g. All natural operations$S y m ^ { k } ( \mathbf { g } )$$S y m ^ { l } ( \mathbf { g } ) { \longrightarrow } S y m ^ { m } ( \mathbf { g } )$which can be defined by contractions of indices with several copies of$\beta ,$exist only for$m \leq k + l ,$, and for every given m there are only finitely many ways to contract indices. Thus, it makes sense to put ¯h equal to 1 and obtain a product on$S y m ( \mathbf { g } ) = \oplus _ { k \geq 0 } S y m ^ { k } ( \mathbf { g } )$. We denote this product also by ⋆.

It is easy to see that for$\gamma _ { 1 } , \gamma _ { 2 } \in \mathbf { g }$the following identity holds:

$$
\gamma_ {1} \star \gamma_ {2} - \gamma_ {2} \star \gamma_ {1} = [ \gamma_ {1}, \gamma_ {2} ].
$$

Moreover, the top component of ⋆-product which maps$S y m ^ { k } ( \mathbf { g } ) \otimes S y m ^ { l } ( \mathbf { g } )$to$S y m ^ { k + l } ( \mathbf { g } )$, coincides with the product on$S y m ( \mathbf { g } )$. From this two facts one concludes that there exists a unique isomorphism of algebras

$$
I _ {a l g}: (\mathcal {U} \mathbf {g}, \cdot) \longrightarrow (S y m (\mathbf {g}), \star)
$$

such that$I _ { a l g } ( \gamma ) = \gamma ~ \mathrm { f o r } ~ \gamma \in { \bf g } .$, where denotes the universal enveloping algebra of g with the standard product.

One can easily recover variable ¯h in this description and get the statement of the theorem. Q.E.D.

Corollary. The center of the universal enveloping algebra is canonically isomorphic as an algebra to the algebra$\mathbf { \mu } ( S y m ( \mathbf { g } ) ) ^ { \mathbf { g } }$of g-invariant polynomials on$\mathbf { g } ^ { * }$.

Proof: The center of g is 0-th cohomology for the (local) Hochschild complex of g endowed with the standard cup-product. The algebra$( S y m ( \mathbf { g } ) ) ^ { \mathbf { g } }$is the 0-th cohomology of the algebra of polyvector fields on$\mathbf { g } ^ { * }$endowed with the diferential$[ \alpha , \cdot ]$where α is the Kirillov-Poisson bracket. From the theorem 8.2 we conclude that applying the tangent map to  we get an isomorphism of algebras.

## 8.3.2. Three isomorphisms

In the proof of theorem 8.3.1 we introduced an isomorphism$I _ { a l g }$of algebras.

We denote by$I _ { P B W }$the isomorphism of vector spaces

$$
S y m (\mathbf {g}) \longrightarrow \mathcal {U} \mathbf {g}
$$

(subscript from the Poincar´e-Birkhof-Witt theorem, see 8.3.5.1), which is defined as

$$
\gamma_ {1} \gamma_ {2} \dots \gamma_ {n} \longrightarrow \frac {1}{n !} \sum_ {\sigma \in \Sigma_ {n}} \gamma_ {\sigma_ {1}} \cdot \gamma_ {\sigma_ {2}} \cdot \dots \cdot \gamma_ {\sigma_ {n}}.
$$

Analogously to arguments from above, one can see that the tangent map from polyvector fields on$\mathbf { g } ^ { * }$ to the Hochschild complex of the quantized algebra can be defined for$\hbar = 1$and for polynomial coeficients. We denote by$I _ { T }$its component which maps polynomial 0-vector fields on$\mathbf { g } ^ { * } \left( \mathrm { i . e . } \right.$. elements of$S y m ( \mathbf { g } ) )$ to 0-cochains of the Hochschild complex of the algebra$( S y m ( \mathbf { g } ) , \star )$. Thus,$I _ { T }$is an isomorphism of vector spaces

$$
I _ {T}: S y m (\mathbf {g}) \longrightarrow S y m (\mathbf {g})
$$

and the restriction of$I _ { T }$to the algebra of$a d ( \mathbf { g } ) ^ { \prime }$<sup>∗</sup>-invariant polynomials on$\mathbf { g } ^ { * }$is an isomorphism of algebras

$$
\operatorname{Sym} (\mathbf {g}) ^ {\mathbf {g}} \longrightarrow \operatorname{Center} ((\operatorname{Sym} (\mathbf {g}), \star)).
$$

Combining all facts from above we get a sequence of isomorphisms of vector spaces:

$$
S y m (\mathbf {g}) \xrightarrow {I _ {T}} S y m (\mathbf {g}) \xleftarrow {I _ {a l g}} \mathcal {U} \mathbf {g} \xleftarrow {I _ {P B W}} S y m (\mathbf {g}).
$$

These isomorphisms are$a d ( \mathbf { g } )$-invariant. Thus, one get isomorphisms

$$
(S y m (\mathbf {g})) ^ {\mathbf {g}} \xrightarrow {I _ {T | \dots}} C e n t e r (S y m (\mathbf {g}), \star) \xleftarrow {I _ {a l g | \dots}} C e n t e r (\mathcal {U} \mathbf {g}) \xleftarrow {I _ {P B W | \dots}} (S y m (\mathbf {g})) ^ {\mathbf {g}},
$$

where the subscript$| \dots \rrangle$. denotes the restriction to subspaces of$a d ( \mathbf { g } )$-invariants . Moreover, first two arrows are isomorphism of algebras. Thus, we proved the following

Theorem. The restriction of the map

$$
\left(I _ {a l g}\right) ^ {- 1} \circ I _ {T}: S y m (\mathbf {g}) \longrightarrow \mathcal {U} \mathbf {g}
$$

to$( S y m ( \mathbf { g } ) ) ^ { \mathbf { g } }$is an isomorphism of algebras$( S y m ( \mathbf { g } ) ) ^ { \mathbf { g } } { \longrightarrow } C e n t e r \left( \mathcal { U } \mathbf { g } \right)$

$$
Q. E. D.
$$

## 8.3.3. Automorphisms of$S y m ( \mathbf { g } )$

Let us calculate automorphisms$I _ { T }$and$I _ { a l g } \circ I _ { P B W }$of the vector space$S y m ( \mathbf { g } )$. We claim that both these automorphisms are translation invariant operators on the space$S y m ( \mathbf { g } )$of polynomials on$\mathbf { g } ^ { * }$

The algebra of translation invariant operators on the space of polynomials on a vector space V is canonically isomorphic to the algebra of formal power series generated by V. Generators of this algebra acts as derivations along constant vector fields in$V .$. Thus, any such operator can be seen as a formal power series at zero on the dual vector space$V ^ { * }$. We apply this formalism to the case$V = \mathbf { g } ^ { * }$

Theorem. Operators$I _ { T }$and${ \cal I } _ { a l g } \circ$I respectively are translation invariant operators associated with formal power series$S _ { 1 } ( \gamma )$and$S _ { 2 } ( \gamma )$at zero in g of the form

$$
S _ {1} (\gamma) = \exp \left(\sum_ {k \geq 1} c _ {2 k} ^ {(1)} \operatorname{Trace} \left(a d (\gamma) ^ {2 k}\right)\right), S _ {2} (\gamma) = \exp \left(\sum_ {k \geq 1} c _ {2 k} ^ {(2)} \operatorname{Trace} \left(a d (\gamma) ^ {2 k}\right)\right)
$$

where$c _ { 2 } ^ { ( 1 ) } , c _ { 4 } ^ { ( 1 ) } , \ldots$. and$c _ { 2 } ^ { ( 2 ) } , c _ { 4 } ^ { ( 2 ) } , \dots$. are two infinite sequences of real numbers indexed by even natural numbers.

Proof: we will study separately two cases.

## 8.3.3.1. Isomorphism$I _ { T }$

The isomorphism$I _ { T }$is given by the sum over terms corresponding to admissible graphs Γ with no vertices of the second type, one special vertex v of the first type such that no edge start at v, and such that at any other vertex start two edges and ends no more than one edge. Vertex v is the marked vertex where we put an element of$S y m ( \mathbf { g } )$considered as an element of tangent cohomology. At other vertices we put the Poisson-Kirillov bi-vector field on$\mathbf { g } ^ { * }$, i.e. the tensor of commutator operation in g. As the result we get 0-diferential operator, i.e. an element of algebra$S y m ( \mathbf { g } )$

It is easy to see that any such graph is isomorphic to a union of copies of “wheels”$W h _ { n } , \ n \geq 2 \colon$

![](images/page_40_image_7.jpg)

with identified central vertex v. The following picture shows a typical graph:

![](images/page_40_image_9.jpg)

In the integration we may assume that the point corresponding to v is fixed, say that it is$i \cdot 1 + 0 \in { \mathcal { H } } .$ because group$\bar { G } ^ { ( 1 ) }$acts simply transitively on . First of all, the operator$S y m ( \mathbf { g } ) { \longrightarrow } S y m ( \mathbf { g } )$corresponding to the individual wheel$W h _ { n }$is the diferential operator on$\mathbf { g } ^ { * }$with constant coeficients, and it corresponds to the polynomial γ Trace$( a d ( \gamma ) ^ { n } )$on g. The operator corresponding to the joint of several wheels is the product of operators associated with individual wheels. Also, the integral corresponding to the joint is the product of integrals. Thus, with the help of symmetry factors, we get that the total operator is equal to the exponent of the sum of operators associated with wheels$W h _ { n } , \ n \geq 2$with weights equal to corresponding integrals. By the symmetry argument used several times before$( z \mapsto - { \overline { { z } } } )$, we see that integrals corresponding to wheels with odd n vanish. We proved the first statement of our theorem. Q.E.D.

## 8.3.3.2. Isomorphism$I _ { a l g } \circ I _ { P B W }$

The second case, for the operator$I _ { a l g } \circ I _ { P B W }$, is a bit more tricky. Let us write a formula for this map:

$$
I _ {a l g} \circ I _ {P B W}: \gamma^ {n} \mapsto \gamma \star \gamma \star \gamma \dots \star \gamma (n \mathrm{copiesof} \gamma).
$$

This formula defines the map unambiguously because elements$\gamma ^ { n } , \ \gamma \in { \bf g } , \ n \ge 0$generate$S y m ( \mathbf { g } )$as a vector space.

In order to multiply several (say, m, where$m \geq 2 )$elements of the quantized algebra we should put these elements at m fixed points in increasing order on R and take the sum over all possible graphs with m vertices of the second type of corresponding expressions with appropriate weights. The result does not depend on the position of fixed points on R because the star-product is associative. Moreover, if we calculate a power of a given element with respect to the ⋆-product, we can put all these points in arbitrary order. It follows that we can take an average over configurations of m points on R where each point is random, distributed independently from other points, with certain probability density on R. We choose a probability distribution on R with a smooth symmetric (under transformation$x \mapsto - x )$density ρ(x). We assume also that$\rho ( x ) d x$is the restriction to${ \bf R } \simeq C _ { 1 , 1 }$of a smooth 1-form on$\overline { { C } } _ { 1 , 1 } \simeq \{ - \infty \} \sqcup \mathbf { R } \sqcup \{ + \infty \}$. With probability 1 our m points will be pairwise distinct. One can check easily that the interchanging of order of integration (i.e. for the taking mean value from the probability theory side, and for the integration of diferential forms over configuration spaces) is valid operation in our case.

The conclusion is that the m-th power of an element of quantized algebra can be calculated as a sum over all graphs with m vertices of the second type, with weights equal to integrals over configuration spaces where we integrate products of forms dφ and 1-forms$\rho ( x _ { i } ) d x _ { i }$where$x _ { i }$are points moving along R.

The basic element of pictures in our case are “wheels without axles”:

![](images/page_41_image_8.jpg)

and the$\Lambda { \mathrm { - g r a p h } }$(which gives 0 by symmetry reasons):

![](images/page_42_image_0.jpg)

The typical total picture is something like (with$m = 1 0 )$

![](images/page_42_image_2.jpg)

Again, it is clear from all this that the operator$I _ { a l g } \circ I _ { P B W }$is a diferential operator with constant coeficients on$S y m ( \mathbf { g } )$, equal to the exponent of the sum of operators corresponding to individual wheels These operators are again proportional to operators associated with power series on g

$$
\gamma \longrightarrow T r a c e (a d (\gamma) ^ {n}).
$$

By the same symmetry reasons as above we see that integrals corresponding to odd n vanish. The second part of the theorem is proven. Q.E.D.

## 8.3.4. Comparison with the Duflo-Kirillov isomorphism

For the case of semi-simple g there is so called Harish-Chandra isomorphism between algebras$\mathbf { \xi } ( S y m ( \mathbf { g } ) ) ^ { \mathbf { g } }$ and Center( g). A. Kirillov realized that there is a way to rewrite the Harish-Chandra isomorphism in a form which has sense for arbitrary finite-dimensional Lie algebra, i.e. without using the Cartan and Borel subalgebras, the Weyl group etc. Later M. Duflo (see [D]) proved that the map proposed by Kirillov is an isomorphism for all finite-dimensional Lie algebras.

The explicit formula for the Duflo-Kirillov isomorphism is the following:

$$
I _ {D K}: \big (S y m (\mathbf {g}) \big) ^ {\mathbf {g}} \simeq C e n t e r (\mathcal {U} (\mathbf {g})), I _ {D K} = I _ {P B W | (S y m (\mathbf {g})) ^ {\mathbf {g}}} \circ I _ {s t r a n g e | (S y m (\mathbf {g})) ^ {\mathbf {g}}},
$$

where$I _ { s t r a n g e }$is an invertible translation invariant operator on$S y m ( \mathbf { g } )$associated with the following formal power series on g at zero, reminiscent of the square root of the Todd class:

$$
\gamma \mapsto \exp \left(\sum_ {k \geq 1} \frac {B _ {2 k}}{4 k (2 k) !} \operatorname{Trace} \left(a d (\gamma) ^ {2 k}\right)\right)
$$

where$B _ { 2 } , B _ { 4 } , \ldots$. are Bernoulli numbers. Formally, one can write the r.h.s. as$d e t ( q ( a d ( \gamma ) ) )$where

$$
q (x) := \sqrt {\frac {e ^ {x / 2} - e ^ {- x / 2}}{x}}.
$$

The fact that the Duflo-Kirillov isomorphism is an isomorphism of algebras is highly non-trivial. All proofs known before (see$[ \mathrm { D u } ] , [ \mathrm { G i } ] )$used certain facts about finite-dimensional Lie algebras which follow only from the classification theory. In particular, the fact that the analogous isomorphism for Lie superalgebras is compatible with products, was not known.

We claim that our isomorphism coincides with the Duflo-Kirillov isomorphism. Let us just sketch the argument. In fact, we claim that

$$
I _ {a l g} ^ {- 1} \circ I _ {T} = I _ {P B W} \circ I _ {s t r a n g e}.
$$

If it is not true then we get a non-zero series$E r r \in t ^ { 2 } \mathbf { R } [ [ t ^ { 2 } ] ]$such that the translation invariant operator on$S y m ( \mathbf { g } )$associated with$\gamma \mapsto I _ { d e t ( e x p ( a d \gamma ) ) } )$gives an automorphism of algebra$( S y m ( \mathbf { g } ) ) ^ { \mathbf { g } }$. Let$2 k > 0$be the degree of first non-vanishing term in the expansion of$E r r$. Then it is easy to see that the operator on $S y m ( \mathbf { g } )$associated with the polynomial$\gamma \mapsto \bar { T r a c e } ( a d ( \gamma ) ^ { 2 k }$is a derivation when restricted to$( S y m ( \mathbf { g } ) ) ^ { \mathbf { g } }$ One can show that it is not true using Lie algebras$\mathbf { g } = g l ( n )$for large n. Thus, we get a contradiction and proved that$E r r = 0 . \quad \ Q . E . D .$

As a remark we would like to mention that if one replaces series$q ( x )$above just by

$$
\left(\frac {x}{1 - e ^ {- x}}\right) ^ {- \frac {1}{2}}
$$

then one still get an isomorphism of algebras. The reason is that the one-parameter group of automorphisms of$S y m ( \mathbf { g } )$associated with series

$$
\gamma \longrightarrow \exp (c o n s t \cdot T r a c e (a d (\gamma)))
$$

preserves the structure of Poisson algebra on$\mathbf { g } ^ { * }$. This one-parameter group also acts by automorphisms of g. It is analogous to the Tomita-Takesaki flow of weights for von Neumann factors.

## 8.3.5. Results in rigid tensor categories

Many proofs from this paper can be transported to a more general context of rigid Q-linear tensor categories (i.e. abelian symmetric monoidal categories with the duality functor imitating the behavior of finite-dimensional vector spaces). We will be very brief here.

First of all, one can formulate and prove the Poincar´e-Birkhof-Witt theorem in a great generality, in Q-linear additive symmetric monoidal categories with infinite sums and kernels of projectors. For example, it holds in the category of A-modules where A is arbitrary commutative associative algebra over Q. Thus, we can speak about universal enveloping algebras and the isomorphism$I _ { P B W }$

One can define Duflo-Kirillov morphism for a Lie algebra in a k-linear rigid tensor category where k is a field of characteristic zero, because Bernoulli numbers are rational. Our result from 8.3.4 saying that it is a morphism of algebras, holds in this generality as well. It does not hold for infinite-dimensional Lie algebras because we use traces of products of operators in the adjoint representation.

In [KV] a conjecture was made in the attempt to prove that that Duflo-Kirillov formulas give a morphism of algebras. It seems that using our result one can prove this conjecture. Also, there is another related conjecture concerning two products in the algebra of chord diagrams (see [BGRT]) which seems to follow from our results too.

## 8.4. Second application: algebras of$E x t - \mathbf { s } .$

Let X be complex manifold, or a smooth algebraic variety of field k of characteristic zero. We associate with it two graded vector spaces. The first space$H T ^ { \bullet } ( X )$is the direct sum$\begin{array} { r l } {  { \bigoplus _ { k , l } H ^ { k } ( X , \wedge ^ { l } T _ { X } ) [ - k - l ] . } } & { { } } \end{array}$

The second space$H H ^ { \bullet } ( X )$is the space$\oplus _ { k } E x t _ { C o h ( X \times X ) } ^ { k } ( \mathcal { O } _ { d i a g } , \mathcal { O } _ { d i a g } ) [ - k ]$of Ext-groups in the category of coherent sheaves on$X \times X$from the sheaf of functions on the diagonal to itself. The space$H H ^ { \bullet } ( X )$can be thought as the Hochschild cohomology of the space X. The reason is that the Hochschild cohomology of any algebra A can be also defined as$E x t _ { A - m o d - A } ^ { \bullet } ( A , A )$in the category of bimodules.

Both spaces,$H H ^ { \bullet } ( X )$and$H T ^ { \bullet } ( X )$carry natural products. For$H H ^ { \bullet } ( X )$it is the Yoneda composition, and for$H T ^ { \bullet } ( X )$it is the cup-product of cohomology and of polyvector fields.

Claim. Graded algebras$H H ^ { \bullet } ( X )$and$H T ^ { \bullet } ( X )$are canonically isomorphic. The isomorphism between them is functorial with respect to ´etale maps.

This statement is again a corollary of the theorem from 8.2. We will give the proof of it, and explain an application to the Mirror Symmetry (see [Ko4]) in the next paper.

## Bibiliography

[AKSZ] M. Alexandrov, M. Kontsevich, A. Schwarz, O. Zaboronsky, The Geometry of the Master Equation and Topological Quantum Field Theory, Intern. Jour. of Mod. Phys., 12 (1997), no. 7, 1405 - 1429, and hep-th/9502010.

[AGV] V. I. Arnold, S. M. Gusein-Zade, A. N. Varchenko, Singularities of Diferentiable Maps, Vol. I, Birkh¨auser 1985.

[BGRT] , D. Bar-Natan, S. Garoufalidis, L. Rozansky, D. Thurston, Wheels, wheeling, and the Kontsevich integral of the unknot, q-alg/9703025.

[BFFLS] F. Bayen, M. Flato, C. Frønsdal, A. Lichnerowicz, D. Sternheimer, Deformation theory and quantization. I. Deformations of symplectic structures, Ann. Physics 111 (1978), no. 1, 61 - 110.

[De] P. Deligne, Cat´egories tannakiennes, The Grothendieck Festschrift, Vol. II, Progress in Mathematics 87, Birkh¨auser 1990, 111 - 195.

[DL] M. De Wilde, P. B. A. Lecomte, Existence of star-products and of formal deformations in Poisson Lie algebra of arbitrary symplectic manifolds, Let. math. Phys., 7 (1983), 487 - 496.

[Du] M. Duflo, Caract´eres des alg\`ebres de Lie r´esolubles, C. R. .Acad. Sci., 269 (1969), s´erie a, p. 437 - 438.

[EK] P. Etingof, D. Kazhdan, Quantization of Lie Bialgebras, I, Selecta Math., New Series, 2 (1996), no. 1, 1 - 41.

[Fe] B. Fedosov, A simple geometric construction of deformation quantization, J. Dif. Geom., 40 (1994) 2, 213 - 238.

[FM] W. Fulton, R. MacPherson, Compactification of configuration spaces, Ann. Math. 139 (1994), 183 - 225.

[GK] I. M. Gelfand, D. A. Kazhdan, Some problems of diferential geometry and the calculation of cohomologies of Lie algebras of vector fields, Soviet Math. Dokl., 12 (1971), no. 5, 1367 - 1370.

[GV] M. Gerstenhaber, A. Voronov, Homotopy G-algebras and moduli space operad, Intern. Math. Res. Notices (1995), No. 3, 141 - 153.

[GJ] E. Getzler, J. D. S. Jones, Operads, homotopy algebra and iterated integrals for double loop spaces, hep-th/9403055.

[Gi] V. Ginzburg, Method of Orbits in the Representation Theory of Complex Lie Groups, Funct. Anal. and appl., 15 (1981), no. 1, 18 - 28.

[GM] W. Goldman, J. Millson, The homotopy invariance of the Kuranishi space, Ill. J. Math., 34 (1990), no. 2, 337 - 367.

[HS1] V. Hinich, V. Schechtman, Deformation theory and Lie algebra homology, alg-geom/9405013.

[HS2] V. Hinich, V. Schechtman, Homotopy Lie algebras, I. M. Gelfand Seminar, Adv. Sov. Math., 16 (1993), part 2, 1 - 28.

[KV] M. Kashiwara, M. Vergne, The Campbell-Hausdorf formula and invariant hyperfunctions, Invent. Math., 47 (1978), 249 - 272.

[Ki] A. Kirillov, Elements of the Theory of Representations, Springer-Verlag 1975.

[Ko1] M. Kontsevich, Feynman diagrams and low-dimensional topology, First European Congress of Mathematics (Paris, 1992), Vol. II, Progress in Mathematics 120, Birkh¨auser (1994), 97 - 121.

I.H.E.S., 35 Route de Chartres,

[Ko2] M. Kontsevich, Formality Conjecture, D. Sternheimer et al. (eds.), Deformation Theory and Symplectic Geometry, Kluwer 1997, 139 - 156.

[Ko3] M. Kontsevich, Rozansky-Witten invariants via formal geometry, dg-ga/9704009, to appear in Compos. Math.

[Ko4] M. Kontsevich, Homological algebra of mirror symmetry, Proceedings of ICM, Z¨urich 1994, vol. I, Birkh¨auser (1995), 120 - 139.

[M] Yu. I. Manin, Gauge Field theory and Complex Geometry, Springer-Verlag 1988.

[Q] D. Quillen, Superconnections and the Chern character, Topology 24 (1985), 89 - 95.

[SS] M. Schlessinger, J. Stashef, The Lie algebra structure on tangent cohomology and deformation theory, J. Pure Appl. Algebra 89 (1993), 231 - 235.

[Su] D. Sullivan, Infinitesimal computations in topology, I. H. E. S. Publ. Math., no. 47 (1977), 269 - 331.

[V] A. Voronov, Quantizing Poisson Manifolds, q-alg/9701017.

Bures-sur-Yvette 91440, FRANCE

email: maxim@ihes.fr