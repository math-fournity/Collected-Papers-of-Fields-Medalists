# Deformation Quantization of Poisson Manifolds

MAXIM KONTSEVICH

I.H.E.S., 35 route de Chartres, Bures-sur-Yvette 91440, France. e-mail: maxim@ihes.fr

(Received: 2 February 2004)

Abstract. I prove that every finite-dimensional Poisson manifold X admits a canonical deformation quantization. Informally, it means that the set of equivalence classes of associative algebras close to the algebra of functions on X is in one-to-one correspondence with the set of equivalence classes of Poisson structures on X modulo difeomorphisms. In fact, a more general statement is proven (the ‘Formality conjecture’), relating the Lie superalgebra of polyvector fields on X and the Hochschild complex of the algebra of functions on X. Coefficients in explicit formulas for the deformed product can be interpreted as correlators in a topological open string theory, although I do not explicitly use the language of functional integrals.

Mathematics Subject Classifications (2000). 53D55, 16E40, 18G55, 58A50.

Key words. deformation quantization, homotopy Lie algebras.

## Foreword

Here is the final version of the e-print ‘Deformation quantization of Poisson manifolds I’ [34] posted on the web archive as q-alg/9709040. The changes that have been made are mostly cosmetic, I have just corrected few mistakes and tried to make clear links between several lemmas and theorems proven in the Letter, and also straightened out some proofs.

Here follows a guide to a short and definitely not complete additional bibliography reflecting further development of the subject.

First of all, I have to mention the work of Dmitry Tamarkin (see [45] and a nice exposition in [23]), which gave a radically new approach to the formality theorem. One of main ideas is to consider the Lie algebras$T _ { \mathrm { p o l y } }$and$D _ { \mathrm { p o l y } }$not just as dg Lie algebras, but as homotopy Gerstenhaber algebras, which naturally explains the cup product on the tangent space. A very important related issue here is the so-called Deligne conjecture which says that on the Hochschild complex of an arbitrary associative algebra there is a natural action of the dg operad of chains of the little discs operad. The Deligne conjecture has now several proofs (see, e.g., [37, 38]), and a generalization to higher dimensions in [27]. Unfortunately, up to now, it is not clear how to extract explicit formulas from Tamarkin’s work, or even how to compare it with the formality morphism from [34]. Tamarkin’s proof is based on the Etingof– Kazhdan theorem about quantizations of Lie bialgebras, which is, in a sense, more complicated (and less explicit) than the Formality theorem itself! It seems that the

Etingof–Kazhdan theorem is a ‘degree zero’ part of a more general not yet established result of the formality of the diferential graded Lie algebra controlling deformations of the symmetric algebra SymðVÞ of a vector space, considered as an associative and coassociative bialgebra. On this Lie algebra there should be an action of the operad of chains of little three-dimensional cube operad and its formality should be considered as a natural generalization of the Formality theorem from [34]. Up to now there is no explicit complex of a ‘reasonable size’, controlling deformations of bialgebras, see [40] for some recent attempts. We should notice also that Tamarkin deduced (see [46]) the Etingof–Kazhdan theorem from Deligne’s conjecture and the formality of the little discs operad. Unfortunately some elements of his proof are too formal and it is not clear how to translate them into geometry.

In [35] I have tried to perform a shortcut in Tamarkin’s proof avoiding the reference to Etingof–Kazhdan’s result. Also I proposed a new formality morphism with complex coeficients, diferent from the one in [34]. Conjecturally, the new morphism behaves in a better way than the old one with respect to the arithmetic nature of the coeficients (weights of graphs) and should coincide with Tamarkin’s quasi-isomorphism up to homotopy.

In [47] another generalization of the Formality theorem was proposed. Namely, one should consider not only the cohomological Hochschild complex, but also the homological Hochschild complex which is a module in certain sense over the cohomological one. The related colored operad here consists of configurations of disjoint discs in a cylinder with two marked points on both boundary components. This is important for the study of traces in deformation quantization, see [16] for an approach to the quantization with traces.

In [2] the reader can find an explicit description of the signs of various terms in the Formality theorem, which is quite a nontrivial issue.

The program of identifying graphs in the formality morphism with Feynman diagrams for a topological sigma model (announced in [34]) was performed by Alberto S. Cattaneo and Giovanni Felder in a series of papers [8, 9].

In [5], a formality of the dg Lie algebra is established which is a global Dolbeault complex for holomorphic polyvector fields on a given Calabi–Yau manifold X. Morally, together with the Formality theorem of [34], this should mean that the extended moduli space of triangulated categories is smooth in a formal neighborhood of the derived category of coherent sheaves on X.

An alternative way for the passage from the local to global case in the Formality theorem was described in [10], (see also an appendix in [36]).

In [36], I proposed a way to use the results of [34] in the case of algebraic varieties. It seems that for rational Poisson varieties, deformation quantization is truly canonical in a very strong sense. For example, I believe that for arbitrary field k of characteristic zero there exists a certain canonical isomorphism between the automorphism group of the k-algebra of polynomial diferential operators on an afine n-dimensional space over k and the group of polynomial symplectomorphisms of the standard symplectic 2n-dimensional afine space over k. This is very surprising because the corresponding Lie algebras of derivations are not at all isomorphic.

Finally, repeating myself a bit, I comment on today’s state of the topics listed in Section 0.2 in [34]:

(1) The comparison with other deformation schemes is not yet performed.

(2) This is still a wishful thinking.

(3) See conjectures in [35], and also [36].

(4) This is not done yet and results from [5] should be used as an intermediate step.

(5) Done by Cattaneo and Felder.

(6) Not yet completed, see conjectures in [47].

(7) In [36] there is a recipe for a canonical quantization for quadratic brackets, see also the new conjecture from above about an isomorphism between two automorphisms groups.

## 0. Introduction

In this Letter it is proven that any finite-dimensional Poisson manifold can be canonically quantized (in the sense of deformation quantization). Informally, it means that the set of equivalence classes of associative algebras close to algebras of functions on manifolds is in one-to-one correspondence with the set of equivalence classes of Poisson manifolds modulo difeomorphisms. This is a corollary of a more general statement, which I proposed around 1993–1994 (the Formality conjecture, see [31, 44]).

For a long time the Formality conjecture resisted all approaches. The solution presented here uses, in an essential way, ideas of string theory. Our formulas can be viewed as a perturbation series for a topological two-dimensional quantum field theory coupled with gravity.

## 0.1. CONTENT OF THE LETTER

Section 1: an elementary introduction to the deformation quantization and precise formulation of the main statement concerning Poisson manifolds.

Section 2: an explicit formula for the deformation quantization written in coordinates.

Section 3: an introduction to the deformation theory in general, in terms of differential graded Lie algebras. The material of this section is basically standard.

Section 4: a geometric reformulation of the theory introduced in the previous section, in terms of odd vector fields on formal supermanifolds. In particular, we introduce convenient notions of an$L _ { \infty } { \mathrm { - m o r p h i s m } }$and of a quasi-isomorphism, which gives us a tool to identify deformation theories related with two diferential graded Lie algebras. Also in this section we state our main result, which is the existence of a quasi-isomorphism between the Hochschild complex of the algebra of polynomials and the graded Lie algebra of polyvector fields on afine space.

Section 5: tools for the explicit construction of the quasi-isomorphism mentioned above. We define compactified configuration spaces related to the Lobachevsky plane, a class of admissible graphs, diferential polynomials on polyvector fields related with graphs, and integrals over configuration spaces. Technically, the same constructions were used in generalizations of the perturbative Chern–Simons theory several years ago (see [30]). Compactifications of the configuration spaces are close relatives of Fulton–MacPherson compactifications of configuration spaces in algebraic geometry (see [17]).

Section 6: it is proven that the machinery introduced in the previous section gives a quasi-isomorphism and establishes the Formality conjecture for afine spaces. The proof is essentially an application of the Stokes formula, and a general result of vanishing of certain integral associated with a collection of rational functions on a complex algebraic variety.

Section 7: results of Section 6 are extended to the case of general manifolds. In order to do this, we recall basic ideas of formal geometry of Gelfand and Kazhdan, and the language of superconnections. In order to pass from the afine space to general manifolds, we have to find a nonlinear cocycle of the Lie algebra of formal vector fields. It turns out that such a cocycle can be almost directly constructed from our explicit formulas. In the course of the proof, we calculate several integrals and check their vanishing. Also, we introduce a general notion of direct image for certain bundles of supermanifolds.

Section 8: we describe an additional structure present in the deformation theory of associative algebras, the cup product on the tangent bundle to the super moduli space. The isomorphism constructed in Sections 6 and 7 is compatible with this structure. One of new results is the validity of Duflo–Kirillov formulas for Lie algebras in general rigid tensor categories, in particular for Lie superalgebras. Another application is an equality of two cup products in the context of algebraic geometry.

## 0.2. WHAT IS NOT HERE

Here is a list of further topics which are not touched in this Letter, but are worth mentioning:

(1) the comparison of the formality with various other known constructions of starproducts, the most notorious one are by De Wilde and Lecomte and by Fedosov for the case of symplectic manifolds (see [12, 15]), and by Etingof and Kazhdan for Poisson–Lie groups (see [14]),

(2) a reformulation of the Formality conjecture as an existence of a natural construction of a triangulated category starting from an odd symplectic supermanifold,

(3) a study of the arithmetic nature of coeficients in our formulas, and of the possibility to extend the main results for algebraic varieties over an arbitrary field of characteristic zero,

(4) an application to the Mirror Symmetry, which was the original motivation for the Formality conjecture (see [33]),

(5) a reformulation via a Lagrangian for a quantum field theory (from [1]) which seems to present our formulas as a perturbation expansion,

(6) a version of the formality morphism for cyclic homology,

(7) a canonical quantization of quadratic brackets, and more generally of algebraic Poisson manifolds.

## 1. Deformation Quantization

## 1.1. STAR PRODUCTS

Let$A = \Gamma ( X , { \mathcal { O } } _ { X } )$be the algebra over R of smooth functions on a finite-dimensional $C ^ { \infty }$-manifold X. A star product on A (see [6]) is an associative$\mathbb { R } [ [ \hbar ] ]$-linear product on$A [ [ \hbar ] ]$given by the following formula for$f , g \in A \subset A [ [ \hbar ] ]$

$$
(f, g) \mapsto f \star g = f g + \hbar B _ {1} (f, g) + \hbar^ {2} B _ {2} (f, g) + \dots \in A [ [ \hbar ] ],
$$

where h is the formal variable and$B _ { i }$are bidiferential operators (i.e. bilinear maps $A \times A \longrightarrow A$which are diferential operators with respect to each argument of globally bounded order). The product of arbitrary elements of$A [ [ \hbar ] ]$is defined by the condition of linearity over$\mathbb { R } [ [ \hbar ] ]$and h-adic continuity:

$$
\left(\sum_ {n \geqslant 0} f _ {n} \hbar^ {n}\right) \star \left(\sum_ {n \geqslant 0} g _ {n} \hbar^ {n}\right) := \sum_ {k, l \geqslant 0} f _ {k} g _ {l} \hbar^ {k + l} + \sum_ {k, l \geqslant 0, m \geqslant 1} B _ {m} (f _ {k}, g _ {l}) \hbar^ {k + l + m}.
$$

There is a natural gauge group acting on star products. This group consists of automorphisms of$A [ [ \hbar ] ]$considered as an$\mathbb { R } [ [ \hbar ] ]$-module (i.e. linear transformations $A \longrightarrow A$parametrized by h), of the following form:

$$
\begin{array}{l} f \mapsto f + \hbar D _ {1} (f) + \hbar^ {2} D _ {2} (f) + \dots \text {   for   } f \in A \subset A [ [ \hbar ] ], \\ \sum_ {n \geqslant 0} f _ {n}   \hbar^ {n} \mapsto \sum_ {n \geqslant 0} f _ {n}   \hbar^ {n} + \sum_ {n \geqslant 0, m \geqslant 1} D _ {m} (f _ {n})   \hbar^ {n + m}, \quad \text {   for   general   element   } f (\hbar) \\ = \sum_ {n \geqslant 0} f _ {n}   \hbar^ {n} \in A [ [ \hbar ] ], \end{array}
$$

where$D _ { i } : A \longrightarrow A$are diferential operators. If$\begin{array} { r } { D ( \hbar ) = 1 + \sum _ { m \geqslant 1 } D _ { m } \hbar ^ { m } } \end{array}$is such an automorphism, it acts on the set of star products as

$$
\begin{array}{l} \star \mapsto \star^ {\prime}, \quad f (\hbar) \star^ {\prime} g (\hbar) \\ := D (\hbar) \Big (D (\hbar) ^ {- 1} (f (\hbar)) \star D (\hbar) ^ {- 1} (g (\hbar) \Big), \\ f (\hbar), g (\hbar) \in A [ [ \hbar ] ]. \end{array}
$$

We are interested in star products up to gauge equivalence.

## 1.2. FIRST APPROXIMATION: POISSON STRUCTURES

It follows from the associativity of ? that the bilinear map$B _ { 1 } \colon A \times A { \longrightarrow } A$satisfies the equation

$$
f B _ {1} (g, h) - B _ {1} (f g, h) + B _ {1} (f, g h) - B _ {1} (f, g) h = 0,
$$

i.e. the linear map$\widetilde { B } _ { 1 } \colon A \otimes A \longrightarrow$A associated with$B _ { 1 }$as$\widetilde { B } _ { 1 } ( f \otimes g ) : = B _ { 1 } ( f , g )$, is a 2- cocycle in the cohomological Hochschild complex of algebra A (the definition of this complex is given in Section 3.4.2).

Let us decompose$B _ { 1 }$into the sum of the symmetric part and of the anti-symmetric part:

$$
B _ {1} = B _ {1} ^ {+} + B _ {1} ^ {-}, \quad B _ {1} ^ {+} (f, g) = B _ {1} ^ {+} (g, f), \quad B _ {1} ^ {-} (f, g) = - B _ {1} ^ {-} (g, f).
$$

Gauge transformations

$$
B _ {1} \mapsto B _ {1} ^ {\prime}, \quad B _ {1} ^ {\prime} (f, g) = B _ {1} (f, g) - f D _ {1} (g) + D _ {1} (f g) - D _ {1} (f) g,
$$

where$D _ { 1 }$is an arbitrary diferential operator, afect only the symmetric part of$B _ { 1 }$, i.e.$B _ { 1 } ^ { - } = \left( B _ { 1 } ^ { \prime } \right) ^ { - }$. One can show that the symmetric part$B _ { 1 } ^ { + }$can be killed by a gauge transformation (and it is a coboundary in the Hochschild complex).

Also, one can show that the skew-symmetric part$B _ { 1 } ^ { - }$is a derivation with respect to both functionsfand$g .$Thus,$B _ { 1 } ^ { - }$comes from a bi-vector field a on$X \colon$

$$
B _ {1} ^ {-} (f, g) = \langle \alpha , \mathrm{d} f \otimes \mathrm{d} g \rangle , \alpha \in \Gamma (X, \wedge^ {2} T _ {X}) \subset \Gamma (X, T _ {X} \otimes T _ {X}).
$$

An analogous fact in algebraic geometry is that the second Hochschild cohomology group of the algebra of functions on a smooth afine algebraic variety is naturally isomorphic to the space of bi-vector fields (see [26] and also Section 4.6.1.).

The second term${ \mathrm { O } } ( \hbar ^ { 2 } )$in the associativity equation$f \star ( g \star h ) = ( f \star g ) \star h$implies that a gives a Poisson structure on$X ,$

$$
\forall f, g, h \{f, \{g, h \} \} + \{g, \{h, f \} \} + \{h, \{f, g \} \} = 0,
$$

where

$$
\{f, g \} := \frac {f \star g - g \star f}{\hbar} _ {| \hbar = 0} = 2 B _ {1} ^ {-} (f, g) = 2 \langle \alpha , \mathrm{d} f \otimes \mathrm{d} g \rangle .
$$

In other words,$[ \alpha , \alpha ] = 0 \in \Gamma ( X , \wedge ^ { 3 } T _ { X } )$, where the bracket is the Schouten–Nijenhuis bracket on polyvector fields (see Section 4.6.1 for the definition of this bracket).

Thus, gauge equivalence classes of star products modulo${ \mathrm { O } } ( \hbar ^ { 2 } )$are classified by Poisson structures on$X .$A priori, it is not clear whether a star product exists with the first term equal to a given Poisson structure and whether there exists a preferred choice of an equivalence class of star products. In this Letter we show that there is a canonical construction of an equivalence class of star products for any Poisson manifold.

## 1.3. DESCRIPTION OF <sub>Q</sub>UANTIZATIONS

THEOREM 1.1. The set of gauge equivalence classes of star products on a smooth manifold X can be naturally identified with the set of equivalence classes of Poisson structures depending formally on h:

$$
\alpha = \alpha (\hbar) = \alpha_ {1} \hbar + \alpha_ {2} \hbar^ {2} + \dots \in \Gamma (X, \wedge^ {2} T _ {X}) [ [ \hbar ] ], [ \alpha , \alpha ] = 0 \in \Gamma (X, \wedge^ {3} T _ {X}) [ [ \hbar ] ]
$$

modulo the action of the group offormal paths in the difeomorphism group of$X ,$ starting at the identity difeomorphism.

Any given Poisson structure$\alpha _ { ( 0 ) }$gives a path$\alpha ( \hbar ) : = \alpha _ { ( 0 ) } \cdot \hbar$and by the theorem from above, a canonical gauge equivalence class of star products. We will not give a proof of this theorem, as it is an immediate corollary of the Main Theorem of this paper in Section 4.6.2 and a general result from deformation theory (see Section 4.4).

## 1.4. EXAMPLES

## 1.4.1. Moyal Product

The simplest example of a deformation quantization is the Moyal product for the Poisson structure on$\mathbb { R } ^ { d }$with constant coeficients:

$$
\alpha = \sum_ {i, j} \alpha^ {i j} \partial_ {i} \wedge \partial_ {j}, \quad \alpha^ {i j} = - \alpha^ {j i} \in \mathbb {R},
$$

where$\partial _ { i } = \partial / \partial x ^ { i }$is the partial derivative in the direction of coordinate$x ^ { i } .$ $i = 1 , \cdots , d .$The formula for the Moyal product is

$$
\begin{array}{c} f \star g = f g + \hbar \sum_ {i, j} \alpha^ {i j} \partial_ {i} (f) \partial_ {j} (g) + \frac {\hbar^ {2}}{2} \sum_ {i, j, k, l} \alpha^ {i j} \alpha^ {k l} \partial_ {i} \partial_ {k} (f) \partial_ {j} \partial_ {l} (g) + \dots \\ = \sum_ {n = 0} ^ {\infty} \frac {\hbar^ {n}}{n !} \sum_ {i _ {1}, \dots , i _ {n}; j _ {1}, \dots ; j _ {n}} \prod_ {k = 1} ^ {n} \alpha^ {i _ {k} j _ {k}} \left(\prod_ {k = 1} ^ {n} \partial_ {i _ {k}}\right) (f) \times \left(\prod_ {k = 1} ^ {n} \partial_ {j _ {k}}\right) (g). \end{array}
$$

Here and later symbol$\times$denotes the usual product.

## 1.4.2. Deformation Quantization up to the Second Order

Let$\begin{array} { r } { \alpha = \sum _ { i , j } \alpha ^ { i j } \partial _ { i } \wedge \partial _ { j } } \end{array}$be a Poisson bracket with variable coeficients in an open domain of$\mathbb { R } ^ { d } \ ( \mathrm { i } . \mathrm { e } . \ \alpha ^ { i j }$is not a constant, but a function of coordinates), then the following formula gives an associative product modulo${ \mathrm { O } } ( \hbar ^ { 3 } )$

$$
\begin{array}{l} f \star g = f g + \hbar \sum_ {i, j} \alpha^ {i j} \partial_ {i} (f) \partial_ {j} (g) + \frac {\hbar^ {2}}{2} \sum_ {i, j, k, l} \alpha^ {i j} \alpha^ {k l} \partial_ {i} \partial_ {k} (f) \partial_ {j} \partial_ {l} (g) + \\ \qquad + \frac {\hbar^ {2}}{3} \left(\sum_ {i, j, k, l} \alpha^ {i j} \partial_ {j} (\alpha^ {k l}) (\partial_ {i} \partial_ {k} (f) \partial_ {l} (g) - \partial_ {k} (f) \partial_ {i} \partial_ {l} (g))\right) + \mathbf {O} (\hbar^ {3}). \end{array}
$$

The associativity up to the second order means that for any three functions$f , g , h$one has$( f \star g ) \star h = f \star ( g \star h ) + \mathrm { O } ( \hbar ^ { 3 } )$

## 1.5. REMARKS

In general, one should consider bidiferential operators$B _ { i }$with complex coeficients, as we expect to associate by quantization self-adjoint operators in a Hilbert space to real-valued classical observables. In this Letter we deal with purely formal algebraic properties of the deformation quantization and work mainly over the field R of real numbers.

Also, it is not clear whether the natural physical counterpart for the ‘deformation quantization’ for general Poisson brackets is the usual quantum mechanics. It is definitely true for the case of nondegenerate brackets, i.e. for symplectic manifolds, but our results show that in general a topological open string theory is more relevant.

## 2. Explicit Universal Formula

Here we propose a formula for the star product for arbitrary Poisson structure a in an open domain of the standard coordinate space$\mathbb { R } ^ { d }$. Terms of our formula modulo${ \mathrm { O } } ( \hbar ^ { 3 } )$are the same as in the previous section, plus a gauge-trivial term of order${ \mathrm { O } } ( \hbar ^ { 2 } )$, symmetric in$f$and$g .$Terms of the formula are certain universal polydiferential operators applied to coeficients of the bi-vector field$\mathscr { X }$and to functions$f , g$. All indices corresponding to coordinates in the formula appear once as lower indices and once as upper indices, i.e. the formula is invariant under afine transformations of$\mathbb { R } ^ { d }$

In order to describe terms proportional to$\hbar ^ { n }$for any integer$n \geqslant 0$, we introduce a special class$G _ { n }$of oriented labeled graphs.

All graphs considered in this Letter are finite, oriented$( { \mathrm { i . e . } }$. every edge carries an orientation), have no multiple edges and no loops. Such objects we will call here simply graphs without adding adjectives.

DEFINITION 2.1. A graph C is a pair$( V _ { \Gamma } , E _ { \Gamma } )$of two finite sets such that$E _ { \Gamma }$is a subset of$( V _ { \Gamma } \times V _ { \Gamma } ) \setminus V _ { \Gamma }$

Elements of$V _ { \Gamma }$are vertices of C, elements of$E _ { \Gamma }$are edges of C. If $e = ( \nu _ { 1 } , \nu _ { 2 } ) \in E _ { \Gamma } \subseteq V _ { \Gamma } \times V _ { \Gamma }$is an edge, then we say that e starts at$\nu _ { 1 }$and ends at v<sub>2</sub>. For any integer$n \geqslant 0 ,$, we define certain set$G _ { n }$of labeled graphs. We say that C (with some additional labels) belongs to$G _ { n }$if

(1) C has$n + 2$vertices and 2n edges,

(2) the set vertices$V _ { \Gamma }$is$\{ 1 , \ldots , n \} \sqcup \{ L , R \}$, where$L , R$are just two symbols (capital letters mean Left and Right),

(3) edges of C are labeled by symbols$e _ { 1 } ^ { 1 } , e _ { 1 } ^ { 2 } , e _ { 2 } ^ { 1 } , e _ { 2 } ^ { 2 } , \ldots , e _ { n } ^ { 1 } , e _ { n } ^ { 2 } .$

(4) for every$k \in \{ 1 , \ldots , n \}$edges labeled by$e _ { k } ^ { 1 }$and$e _ { k } ^ { 2 }$start at the vertex k.

Obviously, set$G _ { n }$is finite, it has$( n ( n + 1 ) ) ^ { n }$elements for$n \geqslant 1$and one element for $n = 0$

We associate a bidiferential operator

$$
B _ {\Gamma , \alpha}: A \times A \longrightarrow A, \quad A = C ^ {\infty} (\mathcal {V}), \mathcal {V} \text {   is   an   open   domain   in   } \mathbb {R} ^ {d}.
$$

with every labeled graph$\Gamma \in G _ { n } .$, which depends on the bi-vector field$\alpha \in \Gamma ( \mathcal { V } , \wedge ^ { 2 } T _ { \mathcal { V } } )$ which is not necessarily a Poisson one. We show one example, from which the general rule should be clear. In Figure 1, we have$n = 3$and the list of edges is

![](images/page_8_image_0.jpg)

Figure 1. An example of a graph.

$$
(e _ {1} ^ {1}, e _ {1} ^ {2}, e _ {2} ^ {1}, e _ {2} ^ {2}, e _ {3} ^ {1}, e _ {3} ^ {2}) = ((1, L), (1, R), (2, R), (2, 3), (3, L), (3, R)).
$$

In the picture of C we put independent indices$1 \leqslant i _ { 1 } , \ldots , i _ { 6 } \leqslant d$on edges, instead of labels$e _ { * } ^ { * } .$. The operator$B _ { \Gamma , \alpha }$corresponding to this graph is

$$
(f, g) \mapsto \sum_ {i _ {1}, \dots , i _ {6}} \alpha^ {i _ {1} i _ {2}} \alpha^ {i _ {3} i _ {4}} \partial_ {i _ {4}} \left(\alpha^ {i _ {5} i _ {6}}\right) \partial_ {i _ {1}} \partial_ {i _ {5}} (f) \partial_ {i _ {2}} \partial_ {i _ {3}} \partial_ {i _ {6}} (g).
$$

The general formula for the operator$B _ { \Gamma , \alpha }$is

$$
\begin{array}{l} B _ {\Gamma , \alpha} (f, g) := \sum_ {I: E _ {\Gamma} \longrightarrow \{1, \dots , d \}} \left[ \prod_ {k = 1} ^ {n} \left(\prod_ {e \in E _ {\Gamma}, e = (*, k)} \partial_ {I (e)}\right) \alpha^ {I (e _ {k} ^ {1}) I (e _ {k} ^ {2})} \right] \times \\ \qquad \times \left(\prod_ {e \in E _ {\Gamma}, e = (*, L)} \partial_ {I (e)}\right) f \times \left(\prod_ {e \in E _ {\Gamma}, e = (*, R)} \partial_ {I (e)}\right) g. \end{array}
$$

In the next step, we associate a weight$W _ { \Gamma } \in$R with each graph$\Gamma \in G _ { n }$. In order to define it we need an elementary construction from hyperbolic geometry.

Let$p , q , p \neq q$be two points in the upper half-plane$\mathcal { H } = \{ z \in \mathbb { C } | \mathrm { I m } ( z ) > 0 \}$endowed with the Lobachevsky metric. We denote by$\phi ^ { \mathrm { h } } ( p , q ) \in \mathbb { R } / 2 \pi \mathbb { Z }$the angle at$p$ formed by two lines,$l ( p , q )$and$l ( p , \infty )$passing through$p$and$q ,$and through$p$and the point$\infty \ 0 \mathrm { n }$the absolute. The direction of the measurement of the angle is counterclockwise from$l ( p , \infty )$to$l ( p , q )$. In the notation$\phi ^ { \mathrm { h } } ( p , q )$, h stands for harmonic (see Figure 2).

![](images/page_8_image_9.jpg)

Figure 2. Angle$\phi ^ { h }$.

An easy planimetry shows that one can express angle$\phi ^ { \mathrm { h } } ( p , q )$in terms of complex numbers:

$$
\phi^ {\mathrm{h}} (p, q) = \operatorname{Arg} ((q - p) / (q - \overline {{p}})) = \frac {1}{2 i} \log \left(\frac {(q - p) (\overline {{q}} - p)}{(q - \overline {{p}}) (\overline {{q}} - \overline {{p}})}\right).
$$

Superscript h in the notation$\phi ^ { \mathrm { h } }$refers to the fact that$\phi ^ { \mathrm { h } } ( p , q )$is a harmonic function in both variables$p , q \in \mathcal { H }$. Function$\phi ^ { \mathrm { h } } ( p , q )$can be defined by continuity also in the case$p , q \in \mathcal { H } \sqcup \mathbb { R } , p \neq q$

Denote by${ \mathcal { H } } _ { n }$the space of configurations of n numbered pairwise distinct points on${ \mathcal { H } } ;$

$$
\mathscr {H} _ {n} = \{(p _ {1}, \dots , p _ {n}) | p _ {k} \in \mathscr {H}, p _ {k} \neq p _ {l} \text {   for   } k \neq l \}.
$$

$\mathcal { H } _ { n } \subset \mathbb { C } ^ { n }$is a noncompact smooth 2n-dimensional manifold. We introduce orientation on${ \mathcal { H } } _ { n }$using the natural complex structure on it.

If$\Gamma \in G _ { n }$is a graph as above, and$( p _ { 1 } , \ldots , p _ { n } ) \in { \mathcal { H } } _ { n }$is a configuration of points, then we draw a copy of C on the plane$\mathbb { R } ^ { 2 } \simeq \mathbb { C }$by assigning point$p _ { k } \in \mathcal { H }$to the vertex$k , \ 1 \leqslant k \leqslant n ,$, point$0 \in \mathbb { R } \subset \mathbb { C }$to the vertex$L ,$and point$1 \in \mathbb { R } \subset \mathbb { C }$to the vertex R. Each edge should be drawn as a line interval in hyperbolic geometry. Every edge e of the graph C defines an ordered pair$( p , q )$of points on${ \mathcal { H } } \sqcup \mathbb { R }$, thus an angle $\phi _ { e } ^ { \mathrm { h } } : = \phi ^ { \mathrm { h } } ( p , q )$. If points$p _ { i }$move around, we get a function$\phi _ { e } ^ { \mathrm { h } }$on${ \mathcal { H } } _ { n }$with values in $\mathbb { R } / 2 \pi \mathbb { Z } .$

We define the weight of C as

$$
w _ {\Gamma} := \frac {1}{n ! (2 \pi) ^ {2 n}} \int_ {\mathscr {H} _ {n}} \bigwedge_ {i = 1} ^ {n} (\mathrm{d} \phi_ {e _ {k} ^ {1}} ^ {\mathrm{h}} \wedge \mathrm{d} \phi_ {e _ {k} ^ {2}} ^ {\mathrm{h}}).
$$

LEMMA 2.2. The integral in the definition of w<sub>C</sub> is absolutely convergent.

This lemma is a particular case of a more general statement proven in Section 6 (see the last sentence in Section 6.2).

THEOREM 2.3. Let a be a Poisson bi-vector field in a domain of$\mathbb { R } ^ { d } .$The formula

$$
f \star g := \sum_ {n = 0} ^ {\infty} \hbar^ {n} \sum_ {\Gamma \in G _ {n}} w _ {\Gamma} B _ {\Gamma , \alpha} (f, g)
$$

defines an associative product. If we change coordinates, we obtain a gauge equivalent star product.

The proof of this theorem is, in a sense, elementary, it only uses the Stokes formula and combinatorics of admissible graphs. We will not give here the proof of this theorem as it is a corollary of a general result proven in Section 6.

## 3. Deformation Theory via Diferential Graded Lie Algebras

## 3.1. TENSOR CATEGORIES SUPER AND GRADED

Here we make a comment about the terminology. This comment seems a bit pedantic, but it could help in the struggle with signs in formulas.

The main idea of algebraic geometry is to replace spaces by commutative associative rings (at least locally). One can further generalize this considering commutative associative algebras in general tensor categories (see [11]). In this way, one can imitate many constructions from algebra and diferential geometry.

The fundamental example is supermathematics, i.e. mathematics in the tensor category$\mathrm { S u p e r } ^ { \mathbf { k } }$of super vector spaces over a field k of characteristic zero (see Chapter 3 in [39]). The category$\mathrm { S u p e r ^ { k } }$is the category of$\mathbb { Z } / 2 \mathbb { Z } .$-graded vector spaces over k (representations of the group$\mathbb { Z } / 2 \mathbb { Z } )$endowed with the standard tensor product, with the standard associativity functor, and with a modified commutativity functor (the Koszul rule of signs). We denote by P the standard functor$\mathrm { S u p e r ^ { k } }$$\mathrm { S u p e r ^ { k } }$changing the parity. It is given on objects by the formula $\Pi { \cal V } = { \cal V } \otimes { \bf k } ^ { 0 | 1 }$. In the sequel we will consider the standard tensor category$\mathbf { V e c t ^ { k } }$of vector spaces over k as the full subcategory of$\mathrm { S u p e r ^ { k } }$consisting of pure even spaces.

The basic tensor category which appears everywhere in topology and homological algebra is a full subcategory of the tensor category of Z-graded super vector spaces. Objects of this category are infinite sums$\mathcal { E } = \oplus _ { n \in \mathbb { Z } } \mathcal { E } ^ { ( n ) }$such that$\boldsymbol { \mathcal { \bar { E } } } ^ { ( n ) }$is pure even for even$n ,$and pure odd for odd n. We will slightly abuse the language, calling this category the category of graded vector spaces, and denote it simply by Graded<sup>k</sup>. We denote by$\mathcal { E } ^ { n }$the usual k-vector space underlying the graded component$\boldsymbol { \mathcal { \delta } } ^ { ( n ) }$. If we forget about Z-grading on E 2 Objects$( \mathrm { G r a d e d } ^ { \mathbf { k } } )$Þ, then we obtain a supervector space$\bigoplus _ { n \in \mathbb { Z } } \Pi ^ { n } \mathcal { E } _ { n }$

Analogously, we will speak about graded manifolds. They are defined as supermanifolds endowed with Z-grading on the sheaf of functions obeying the same conditions on the parity as above.

The shift functor [1]:Graded<sup>k</sup> ! Graded<sup>k</sup> (acting from the right) is defined as the tensor product with graded space$\mathbf { k } [ 1 ]$where$\mathbf { k } [ 1 ] ^ { - 1 } \simeq \mathbf { k } , \mathbf { k } [ 1 ] ^ { \neq - 1 } = 0$. Its powers are denoted by ½n,$n \in \mathbb { Z }$. Thus, for graded space${ \mathcal { E } } ,$we have$\begin{array} { r } { \mathcal { E } = \bigoplus _ { n \in \mathbb { Z } } \mathcal { E } ^ { n } [ - n ] } \end{array}$ Almost all results in this paper formulated for graded manifolds, graded Lie algebras, etc., also hold for supermanifolds, super Lie algebras, etc.

## 3.2. MAURER–CARTAN E<sub>Q</sub>UATION IN DIFFERENTIAL GRADED LIE ALGEBRAS

This part is essentially standard (see [22, 24, 42]).

Let g be a diferential graded Lie algebra over field k of characteristic zero. Below we recall the list of structures and axioms:

$$
\mathbf {g} = \bigoplus_ {k \in \mathbb {Z}} \mathbf {g} ^ {k} [ - k ], \quad [, ]: \mathbf {g} ^ {k} \otimes \mathbf {g} ^ {l} \longrightarrow \mathbf {g} ^ {k + l}, \quad \mathrm{d}: \mathbf {g} ^ {k} \longrightarrow \mathbf {g} ^ {k + 1},
$$

$$
\begin{array}{l} \mathbf {d} (\mathbf {d} (\gamma)) = 0, \mathbf {d} [ \gamma_ {1}, \gamma_ {2} ] = [ \mathbf {d} \gamma_ {1}, \gamma_ {2} ] + (- 1) ^ {\overline {{\gamma_ {1}}}} [ \gamma_ {1}, \mathbf {d} \gamma_ {2} ], [ \gamma_ {2}, \gamma_ {1} ] = - (- 1) ^ {\overline {{\gamma_ {1}}} \cdot \overline {{\gamma_ {2}}}} [ \gamma_ {1}, \gamma_ {2} ], \\ [ \gamma_ {1}, [ \gamma_ {2}, \gamma_ {3} ] ] + (- 1) ^ {\overline {{\gamma_ {3}}} \cdot (\overline {{\gamma_ {1}}} + \overline {{\gamma_ {2}}})} [ \gamma_ {3}, [ \gamma_ {1}, \gamma_ {2} ] ] + (- 1) ^ {\overline {{\gamma_ {1}}} \cdot (\overline {{\gamma_ {2}}} + \overline {{\gamma_ {3}}})} [ \gamma_ {2}, [ \gamma_ {3}, \gamma_ {1} ] ] = 0. \end{array}
$$

In the formulas above, the symbols${ \overline { { \gamma _ { i } } } } \in \mathbb { Z }$mean the degrees of homogeneous elements$\gamma _ { i } ,$i.e.$\gamma _ { i } \in \mathbf { g } ^ { \overline { { \gamma _ { i } } } }$

In other words, g is a Lie algebra in the tensor category of complexes of vector spaces over k. If we forget about the diferential and the grading on g, we obtain a Lie superalgebra.

We associate with g a functor$\mathrm { D e f _ { \mathbf { g } } }$on the category of finite-dimensional commutative associative algebras over k, with values in the category of sets. First of all, let us assume that g is a nilpotent Lie superalgebra. We define the set$\mathcal { M } \mathcal { C } ( \mathbf { g } )$(the set of solutions of the Maurer–Cartan equation modulo the gauge equivalence) by the formula

$$
\mathcal {M C} (\mathbf {g}) := \left\{\gamma \in \mathbf {g} ^ {1} | \mathrm{d} \gamma + \frac {1}{2} [ \gamma , \gamma ] = 0 \right\} / \Gamma^ {0},
$$

where$\Gamma ^ { 0 }$is the nilpotent group associated with the nilpotent Lie algebra$\mathbf { g } ^ { 0 } .$. The group$\Gamma ^ { 0 }$acts by afine transformations of the vector space$\mathbf { g } ^ { 1 }$. The action of$\Gamma ^ { 0 }$is defined by the exponentiation of the infinitesimal action of its Lie algebra:

$$
\alpha \in \mathbf {g} ^ {0} \mapsto (\dot {\gamma} = \mathrm{d} \alpha + [ \alpha , \gamma ]).
$$

Now we are ready to introduce the functor$\mathrm { D e f _ { \mathbf { g } } }$. Technically, it is convenient to define this functor on the category of finite-dimensional nilpotent commutative associative algebras without unit. Let m be such an algebra,$\begin{array} { r } { \mathbf { m } ^ { \mathrm { d i m } ( \mathbf { m } ) + 1 } = 0 } \end{array}$. The functor is given (on objects) by the formula

$$
\operatorname{Def} _ {\mathbf {g}} (\mathbf {m}) = \mathcal {M C} (\mathbf {g} \otimes \mathbf {m}).
$$

In the conventional approach m is the maximal ideal in a finite-dimensional Artin algebra with unit$\mathbf { m } ^ { \prime } : = \mathbf { m } \oplus \mathbf { k } \cdot 1$: In general, one can think about commutative associative algebras without unit as about objects dual to spaces with base points. Algebra corresponding to a space with base point is the algebra of functions vanishing at the base point.

One can extend the definition of the deformation functor to algebras with linear topology which are projective limits of nilpotent finite-dimensional algebras. For example, in the deformation quantization we use the following algebra over R:

$$
\mathbf {m} := \hbar \mathbb {R} [ [ \hbar ] ] = \varprojlim (\hbar \mathbb {R} [ \hbar ] / \hbar^ {k} \mathbb {R} [ \hbar ]) \quad \text { as } k \to \infty .
$$

## 3.3. REMARK

Several authors, following a suggestion of Deligne, stressed that the set$\mathrm { D e f } _ { \mathbf { g } } ( \mathbf { m } )$ should be considered as the set of equivalence classes of objects of certain groupoid naturally associated with${ \bf g } ( { \bf m } )$. Almost always in deformation theory, diferential graded Lie algebras are supported in nonnegative degrees,$\mathbf { g } ^ { < 0 } = 0$. Our principal example here, the shifted Hochschild complex (see the next subsection), has a non-trivial component in degree 1, when it is considered as a graded Lie algebra. The set

De$\mathrm { f } _ { \mathbf { g } } ( \mathbf { m } )$in such a case has a natural structure of the set of equivalence classes for a 2-groupoid. In general, if one considers diferential graded Lie algebras with components in negative degrees, one immediately meets polycategories and nilpotent homotopy types. Still, it is only half of the story because one cannot say anything about$\mathbf { g } ^ { \geqslant 3 }$using this language. Maybe, a better way is to extend the definition of the deformation functor to the category of diferential graded nilpotent commutative associative algebras (see the last remark in Section 4.5.2).

## 3.4. EXAMPLES

There are many standard examples of diferential graded Lie algebras and related moduli problems.

## 3.4.1. Tangent Complex

Let X be a complex manifold. Define g over$\mathbb { C }$as

$$
\mathbf {g} = \bigoplus_ {k \in \mathbb {Z}} \mathbf {g} ^ {k} [ - k ]; \quad \mathbf {g} ^ {k} = \Gamma (X, \Omega_ {X} ^ {0, k} \otimes T _ {X} ^ {1, 0}) \quad \text { for } k \geqslant 0, \quad \mathbf {g} ^ {<   0} = 0
$$

with the diferential equal to${ \overline { { \partial } } } ,$and the Lie bracket coming from the cup product on @-forms and the usual Lie bracket on holomorphic vector fields.

The deformation functor related with$\mathbf { g }$is the usual deformation functor for complex structures on X. The set$\mathrm { D e f } _ { \mathbf { g } } ( \mathbf { m } )$can be naturally identified with the set of equivalence classes of analytic spaces Xe endowed with a flat map$p \colon \widetilde { X } \longrightarrow \ \mathrm { S p e c } ( \mathbf { m } ^ { \prime } )$，and an identification$i \colon { \widetilde { X } } \times _ { \operatorname { S p e c } ( \mathbf { m } ^ { \prime } ) } ~ \operatorname { S p e c } ( \mathbb { C } ) \simeq X$of the special fiber of$p$with X.

## 3.4.2. Hochschild Complex

Let A be an associative algebra over field k of characteristic zero. The graded space of Hochschild cochains of A with coeficients in A considered as a bimodule over itself is

$$
C ^ {\bullet} (A, A) := \bigoplus_ {k \geqslant 0} C ^ {k} (A, A) [ - k ], \quad C ^ {k} (A, A) := \operatorname{Hom} _ {\operatorname{Vect} ^ {\mathbf {k}}} (A ^ {\otimes k}, A).
$$

We define graded vector space g over k by the formula$\mathbf { g } : = C ^ { \bullet } ( A , A ) [ 1 ]$. Thus, we have

$$
\mathbf {g} = \bigoplus_ {k \in \mathbb {Z}} \mathbf {g} ^ {k} [ - k ]; \mathbf {g} ^ {k} := \operatorname{Hom} (A ^ {\otimes (k + 1)}, A) \text {   for   } k \geqslant - 1, \mathbf {g} ^ {<   (- 1)} = 0.
$$

The diferential in g is shifted by 1, the usual diferential in the Hochschild complex, and the Lie bracket is the Gerstenhaber bracket. The explicit formulas for the diferential and for the bracket are

$$
\begin{array}{l} (\mathrm{d} \Phi) (a _ {0} \otimes \dots \otimes a _ {k + 1}) \\ = a _ {0} \cdot \Phi (a _ {1} \otimes \dots \otimes a _ {k + 1}) - \\ - \sum_ {i = 0} ^ {k} (- 1) ^ {i} \Phi (a _ {0} \otimes \dots \otimes (a _ {i} \cdot a _ {i + 1}) \otimes \dots \otimes a _ {k + 1}) + \\ + (- 1) ^ {k} \Phi (a _ {0} \otimes \dots \otimes a _ {k}) \cdot a _ {k + 1}, \Phi \in \mathbf {g} ^ {k}, \end{array}
$$

and

$$
\left[ \Phi_ {1}, \Phi_ {2} \right] = \Phi_ {1} \circ \Phi_ {2} - (- 1) ^ {k _ {1} k _ {2}} \Phi_ {2} \circ \Phi_ {1}, \Phi_ {i} \in \mathbf {g} ^ {k _ {i}},
$$

where the (nonassociative) product  is defined as

$$
\begin{array}{l} (\Phi_ {1} \circ \Phi_ {2}) (a _ {0} \otimes \dots \otimes a _ {k _ {1} + k _ {2}}) \\ = \sum_ {i = 0} ^ {k _ {1}} (- 1) ^ {i k _ {2}} \Phi_ {1} (a _ {0} \otimes \dots \otimes a _ {i - 1} \otimes (\Phi_ {2} (a _ {i} \otimes \dots \otimes a _ {i + k _ {2}})) \otimes \\ \otimes a _ {i + k _ {2} + 1} \otimes \dots \otimes a _ {k _ {1} + k _ {2}}). \end{array}
$$

We would also like to give here an abstract definition of the diferential and of the bracket on g. Let F denote the free coassociative graded coalgebra with counit cogenerated by the graded vector space$A [ 1 ] : F = \bigoplus _ { n \geq 1 } \otimes ^ { n } ( A [ 1 ] )$

Graded Lie algebra g is the Lie algebra of coderivations of F in the tensor category Graded<sup>k</sup>. The associative product on A gives an element$m _ { A } \in { \mathbf { g } } ^ { 1 } , m _ { A } : A \otimes A \longrightarrow A$ satisfying the equation$[ m _ { A } , m _ { A } ] = 0$. The diferential d in g is defined as$\operatorname { a d } ( m _ { A } )$

Again, the deformation functor related to g is equivalent to the usual deformation functor for algebraic structures. Associative products on A correspond to solutions of the Maurer–Cartan equation in g. The set$\mathrm { D e f } _ { \mathbf { g } } ( \mathbf { m } )$is naturally identified with the set of equivalence classes of pairs$( \widetilde { A } , i )$where Ae is an associative algebra over $\mathbf { m } ^ { \prime } = \mathbf { m } \oplus \mathbf { k } \cdot \mathbf { l }$such that$\widetilde { A }$is free as an m<sup>0</sup>-module, and i an isomorphism of kalgebras$\widetilde { A } \otimes _ { \mathbf { m ^ { \prime } } } \mathbf { k } \simeq A$

The cohomology of the Hochschild complex are

$$
H H ^ {k} (A, A) = \mathrm{Ext} _ {A \text {-mod-} A} ^ {k} (A, A),
$$

the Ext-groups in the Abelian category of bimodules over A. The Hochschild complex without shift by 1 also has a meaning in deformation theory, it also has a canonical structure of diferential graded Lie algebra, and it controls deformations of A as a bimodule.

## 4. Homotopy Lie Algebras and Quasi-isomorphisms

In this section we introduce a language convenient for the homotopy theory of diferential graded Lie algebras and for the deformation theory. The ground field k for linear algebra in our discussion is an arbitrary field of characteristic zero, unless specified.

## 4.1. FORMAL MANIFOLDS

Let V be a vector space. We denote by$C ( V )$the cofree cocommutative coassociative coalgebra without counit cogenerated by V:

$$
C (V) = \bigoplus_ {n \geqslant 1} (\otimes^ {n} V) ^ {\Sigma_ {n}} \subset \bigoplus_ {n \geqslant 1} (\otimes^ {n} V).
$$

Intuitively, we think about$C ( V )$as about an object corresponding to a formal manifold, possibly infinite-dimensional, with base point:

$$
(V _ {\text { formal }}, \text {   base   point   }) := (\text {   Formal   neighborhood   of   zero   in   } V, 0).
$$

The reason for this is that if V is finite-dimensional, then$C ( V ) ^ { * }$(the dual space to $C ( V ) )$is the algebra of formal power series on V vanishing at the origin.

DEFINITION 4.1 A formal pointed manifold M is an object corresponding to a coalgebra C which is isomorphic to$C ( V )$for some vector space$V .$

The specific isomorphism between C and$C ( V )$is not considered as a part of the data. Nevertheless, the vector space V can be reconstructed from M as the space of primitive elements in coalgebra C. Here for a nonunital coalgebra$A = C ( V )$we define primitive elements as solutions of the equation$\Delta ( a ) = 0 \quad$, where $\Delta \colon A \longrightarrow A \otimes A$is the coproduct on A.

Speaking geometrically, V is the tangent space to M at the base point. A choice of an isomorphism between C and$C ( V )$can be considered as a choice of an afine structure on M.

If$V _ { 1 }$and$V _ { 2 }$are two vector spaces, then a map f between corresponding formal pointed manifolds is defined as a homomorphism of coalgebras (a kind of the pushforward map on distribution-valued densities supported at zero)

$$
f _ {*}: C (V _ {1}) \longrightarrow C (V _ {2}).
$$

By the universal property of cofree coalgebras, any such homomorphism is uniquely specified by a linear map$C ( V _ { 1 } ) \longrightarrow V _ { 2 }$. which is the composition of$f _ { * }$with the canonical projection$C ( V _ { 2 } ) \longrightarrow V _ { 2 }$. Homogeneous components of this map,

$$
f ^ {(n)}: \left(\otimes^ {n} (V _ {1})\right) ^ {\Sigma_ {n}} \longrightarrow V _ {2}, n \geqslant 1
$$

can be considered as Taylor coeficients of f. More precisely, Taylor coeficients are defined as symmetric polylinear maps

$$
\partial^ {n} f \colon \otimes^ {n} (V _ {1}) \longrightarrow V _ {2}, \partial^ {n} f (v _ {1} \dots v _ {n}) := \frac {\partial^ {n}}{\partial t _ {1} \cdots \partial t _ {n | t _ {1} = \cdots = t _ {n} = 0}} (f (t _ {1} v _ {1} + \dots + t _ {n} v _ {n})).
$$

Map$\partial ^ { n } f$goes through the quotient$\operatorname { S y m } ^ { n } ( V _ { 1 } ) : = ( \otimes ^ { n } V _ { 1 } ) _ { \Sigma _ { n } }$. Linear map$f ^ { ( n ) }$coincides with$\partial ^ { n } f$after the identification of the subspace$\left( \otimes ^ { n } V _ { 1 } \right) ^ { \Sigma _ { n } ^ { . . } } \subset \otimes ^ { n } V _ { 1 }$with the quotient space$\mathrm { { S y m } } ^ { n } \big ( V _ { 1 } \big )$

As in the usual calculus, there is the inverse mapping theorem: nonlinear map f is invertible if its first Taylor coeficient$f ^ { ( 1 ) } \colon V _ { 1 } \longrightarrow V _ { 2 }$is invertible.

Analogous definitions and statements can be made in other tensor categories, including$\mathrm { S u p e r } ^ { \mathbf { k } }$and Graded<sup>k</sup>.

The reader can ask why we speak about base points for formal manifolds, as such manifolds have only one geometric point. The reason is that later we will consider formal graded manifolds depending on formal parameters. In such a situation the choice of the base point is a nontrivial part of the structure.

## 4.2. PRE-<sub>L</sub> -MORPHISMS

Let${ \bf g } _ { 1 }$and${ \bf g } _ { 2 }$be two graded vector spaces.

DEFINITION 4.2. A pre-$L _ { \infty }$-morphism$\mathcal { F }$from${ \bf g } _ { 1 }$to${ \bf g } _ { 2 }$is a map of formal pointed graded manifolds

$$
\mathcal {F} \colon (({\bf g} _ {1} [ 1 ]) _ {\mathrm{formal}}, 0) \longrightarrow (({\bf g} _ {2} [ 1 ]) _ {\mathrm{formal}}, 0).
$$

Map$\mathcal { F }$is defined by its Taylor coeficients which are linear maps$\partial ^ { n } { \mathcal { F } }$of graded vector spaces:

$$
\partial^ {1} \mathcal {F}: \mathbf {g} _ {1} \longrightarrow \mathbf {g} _ {2},
$$

$$
\partial^ {2} \mathcal {F}: \wedge^ {2} (\mathbf {g} _ {1}) \longrightarrow \mathbf {g} _ {2} [ - 1 ],
$$

$$
\partial^ {3} \mathscr {F}: \wedge^ {3} (\mathbf {g} _ {1}) \longrightarrow \mathbf {g} _ {2} [ - 2 ].
$$

Here we use the natural isomorphism$\operatorname { S y m } ^ { n } ( \mathbf { g } _ { 1 } [ 1 ] ) \simeq ( \mathbb { \Lambda } ^ { n } ( \mathbf { g } _ { 1 } ) ) [ n ]$. In plain terms, we have a collection of linear maps between ordinary vector spaces

$$
\mathscr {F} _ {(k _ {1}, \dots , k _ {n})}: \mathbf {g} _ {1} ^ {k _ {1}} \otimes \dots \otimes \mathbf {g} _ {1} ^ {k _ {n}} \longrightarrow \mathbf {g} _ {2} ^ {k _ {1} + \dots + k _ {n} + (1 - n)}
$$

with the symmetry property

$$
\begin{array}{c} \mathcal {F} _ {(k _ {1}, \ldots , k _ {n})} (\gamma_ {1} \otimes \dots \otimes \gamma_ {n}) = - (- 1) ^ {k _ {i} k _ {i + 1}} \mathcal {F} _ {(k _ {1}, \ldots , k _ {i + 1}, k _ {i}, \ldots , k _ {n})} \\ (\gamma_ {1} \otimes \dots \otimes \gamma_ {i + 1} \otimes \gamma_ {i} \otimes \dots \otimes \gamma_ {n}). \end{array}
$$

One can write (slightly abusing notations)

$$
\partial^ {n} \mathscr {F} (\gamma_ {1} \wedge \dots \wedge \gamma_ {n}) = \mathscr {F} _ {(k _ {1}, \dots , k _ {n})} (\gamma_ {1} \otimes \dots \otimes \gamma_ {n})
$$

for$\gamma _ { i } \in \mathbf { g } _ { 1 } ^ { k _ { i } } , i = 1 , \ldots , n .$

In the sequel, we will denote$\partial ^ { n } { \mathcal { F } }$simply by${ \mathcal { F } } _ { n } .$

## 4.3. L<sub>1</sub>-ALGEBRAS AND L<sub>1</sub>-MORPHISMS

Suppose that we have an odd vector field$Q$of degree þ1 (with respect to$\mathbb { Z } { \cdot } \mathrm { g a r d i n g } )$ on formal graded manifold$( \mathbf { g } [ 1 ] _ { \mathrm { f o r m a l } } , 0 )$such that the Taylor series for coeficients of $\boldsymbol { Q }$has terms of polynomial degree 1 and 2 only (i.e. linear and quadratic terms). The first Taylor coeficient$Q _ { 1 }$gives a linear map${ \bf g } \longrightarrow { \bf g }$of degree þ1 (or, better, a map ${ \bf g } \longrightarrow { \bf g } [ 1 ] )$). The second coeficient$\mathcal { Q } _ { 2 } \colon \wedge ^ { 2 } \mathbf { g } \longrightarrow \mathbf { g }$gives a skew-symmetric bilinear operation of degree 0 on g.

It is easy to see that if$[ Q , Q ] _ { \mathrm { s u p e r } } = 2 Q ^ { 2 } = 0$, then g is a diferential graded Lie algebra, with diferential$Q _ { 1 }$and the bracket$Q _ { 2 } ,$, and vice-versa.

In [1], supermanifolds endowed with an odd vector field Q such that $[ Q , Q ] _ { \mathrm { s u p e r } } = 0$, are called Q-manifolds. By analogy, we can speak about formal graded pointed Q-manifolds.

DEFINITION 4.3. An$L _ { \infty } { \mathrm { - a l g e b r a } }$is a pair$( \mathbf { g } , Q )$where g is a graded vector space and$\boldsymbol { Q }$is a coderivation of degree þ1 on the graded coalgebra$C ( \mathbf { g } [ 1 ] )$such that $Q ^ { 2 } = 0$

Other names for$L _ { \infty } { \mathrm { - a l g e b r a s } }$are ‘(strong) homotopy Lie algebras’ and ‘Sugawara algebras’ (see, e.g., [25]).

Usually we will denote$L _ { \infty } \mathrm { { \ - } \mathrm { { a l g e b r a } \ ( \mathbf { g } , \boldsymbol { Q } ) } }$simply by g.

The structure of an$L _ { \infty } { \mathrm { - a l g e b r a } }$on a graded vector space$\mathbf { g }$is given by the infinite sequence of Taylor coeficients$Q _ { i }$of the odd vector field$Q$(coderivation of $C ( \mathbf { g } [ 1 ] )$

$$
\begin{array}{l} Q _ {1} \colon \mathbf {g} \longrightarrow \mathbf {g} [ 1 ], \\ Q _ {2} \colon \wedge^ {2} (\mathbf {g}) \longrightarrow \mathbf {g}, \\ Q _ {3} \colon \wedge^ {3} (\mathbf {g}) \longrightarrow \mathbf {g} [ - 1 ], \\ \dots \end{array}
$$

The condition$Q ^ { 2 } = 0$can be translated into an infinite sequence of quadratic constraints on polylinear maps$Q _ { i }$. First of these constraints means that$Q _ { 1 }$is the differential of the graded space g. Thus,$( \mathbf { g } , Q _ { 1 } )$is a complex of vector spaces over k. The second constraint means that$Q _ { 2 }$is a skew-symmetric bilinear operation on$\mathbf { g } ,$ for which$Q _ { 1 }$satisfies the Leibniz rule. The third constraint means that$Q _ { 2 }$satisfies the Jacobi identity up to homotopy given by$Q _ { 3 } ,$, etc. As we have seen, a diferential graded Lie algebra is the same as an$L _ { \infty }$-algebra with$Q _ { 3 } = Q _ { 4 } = \cdots = 0$

Nevertheless, we recommend to return to the geometric point of view and think in terms of formal graded Q-manifolds. This naturally leads to the following definition:

DEFINITION 4.4. An$L _ { \infty } { \mathrm { - m o r p h i s m } }$between two$L _ { \infty }$-algebras${ \bf g } _ { 1 }$and${ \bf g } _ { 2 }$is a pre-$L _ { \infty } \mathrm { - m o r p h i s m \ } \mathcal { F }$such that the associated morphism$\mathcal { F } _ { * } : C ( \mathbf { g } _ { 1 } [ 1 ] ) \longrightarrow C ( \mathbf { g } _ { 2 } [ 1 ] )$of graded cocommutative coalgebras, is compatible with coderivations.

In geometric terms, an$L _ { \infty } { \mathrm { - m o r p h i s m } }$gives a Q-equivariant map between two formal graded manifolds with base points.

For the case of diferential graded Lie algebras, a pre-$L _ { \infty }$-morphism$\mathcal { F }$is an$L _ { \infty } -$ morphism if it satisfies the following equation for any$n = 1 , 2 \dots$. and homogeneous elements$\gamma _ { i } \in { \bf g } _ { 1 } .$

$$
\begin{array}{l} \mathrm{d} \mathcal {F} _ {n} (\gamma_ {1} \wedge \gamma_ {2} \wedge \dots \wedge \gamma_ {n}) - \sum_ {i = 1} ^ {n} \pm \mathcal {F} _ {n} (\gamma_ {1} \wedge \dots \wedge \mathrm{d} \gamma_ {i} \wedge \dots \wedge \gamma_ {n}) \\ = \frac {1}{2} \sum_ {k, l \geqslant 1, k + l = n} \frac {1}{k ! l !} \sum_ {\sigma \in \Sigma_ {n}} \pm [ \mathcal {F} _ {k} (\gamma_ {\sigma_ {1}} \wedge \dots \wedge \gamma_ {\sigma_ {k}}), \mathcal {F} _ {l} (\gamma_ {\sigma_ {k + 1}} \wedge \dots \wedge \gamma_ {\sigma_ {n}}) ] + \\ + \sum_ {i <   j} \pm \mathcal {F} _ {n - 1} ([ \gamma_ {i}, \gamma_ {j} ] \wedge \gamma_ {1} \wedge \dots \wedge \hat {\gamma} _ {i} \wedge \dots \wedge \hat {\gamma} _ {j} \wedge \dots \wedge \gamma_ {n}). \end{array}
$$

Here are first two equations in the explicit form:

$$
\begin{array}{l} \mathrm{d} \mathcal {F} _ {1} (\gamma_ {1}) = \mathcal {F} _ {1} (\mathrm{d} \gamma_ {1}), \\ \mathrm{d} \mathcal {F} _ {2} (\gamma_ {1} \wedge \gamma_ {2}) - \mathcal {F} _ {2} (\mathrm{d} \gamma_ {1} \wedge \gamma_ {2}) - (- 1) ^ {\overline {{\gamma_ {1}}}} \mathcal {F} _ {2} (\gamma_ {1} \wedge \mathrm{d} \gamma_ {2}) \\ = \mathcal {F} _ {1} ([ \gamma_ {1}, \gamma_ {2} ]) - [ \mathcal {F} _ {1} (\gamma_ {1}), \mathcal {F} _ {1} (\gamma_ {2}) ]. \end{array}
$$

We see that$\mathcal { F } _ { 1 }$is a morphism of complexes. The same is true for the case of general$L _ { \infty }$-algebras. The graded space g for an$L _ { \infty } { - } i$algebra$( \mathbf { g } , Q )$can be considered as the tensor product of${ \bf k } [ - 1 ]$with the tangent space to the corresponding formal graded manifold at the base point. The diferential$Q _ { 1 }$on g comes from the action of $\boldsymbol { Q }$on the manifold.

Let us assume that${ \bf g } _ { 1 }$and${ \bf g } _ { 2 }$are diferential graded Lie algebras, and$\mathcal { F }$is an$L _ { \infty } -$ morphism from${ \bf g } _ { 1 }$to${ \bf g } _ { 2 }$. Any solution$\gamma \in { \bf g } _ { 1 } ^ { 1 } \otimes$m of the Maurer–Cartan equation where m is a nilpotent nonunital algebra, produces a solution of the Maurer–Cartan equation in$\mathbf { g } _ { 2 } ^ { 1 }$ m:

$$
\mathrm{d} \gamma + \frac {1}{2} [ \gamma , \gamma ] = 0 \Longrightarrow \mathrm{d} \widetilde {\gamma} + \frac {1}{2} [ \widetilde {\gamma}, \widetilde {\gamma} ] = 0, \text {   where   } \widetilde {\gamma} = \sum_ {n = 1} ^ {\infty} \frac {1}{n !} \mathscr {F} _ {n} (\gamma \wedge \dots \wedge \gamma) \in \mathbf {g} _ {2} ^ {1} \otimes \mathbf {m}.
$$

The same formula is applicable to solutions of the Maurer–Cartan equation depending formally on the parameter h:

$$
\begin{array}{l} \gamma (\hbar) = \gamma_ {1} \hbar + \gamma_ {2} \hbar^ {2} + \dots \in \mathbf {g} _ {1} ^ {1} [ [ \hbar ] ], \\ \mathrm{d} \gamma (\hbar) + \frac {1}{2} [ \gamma (\hbar), \gamma (\hbar) ] = 0 \Longrightarrow \widetilde {\mathrm{d} \gamma (\hbar)} + \frac {1}{2} [ \widetilde {\gamma (\hbar)}, \widetilde {\gamma (\hbar)} ] = 0. \end{array}
$$

The reason why it works is that the Maurer–Cartan equation in any diferential graded Lie algebra g can be understood as the collection of equations for the subscheme of zeroes of Q in formal manifold$\mathbf { g } [ 1 ] _ { \mathrm { f o r m a l } } .$

$$
\mathrm{d} \gamma + \frac {1}{2} [ \gamma , \gamma ] = 0 \Longleftrightarrow Q _ {| \gamma} = 0.
$$

$L _ { \infty }$-morphisms map zeroes of$\boldsymbol { Q }$to zeroes of Q because they commute with Q. We will see in Section 4.5.2 that$L _ { \infty }$-morphisms induce natural transformations of deformation functors.

## 4.4. <sub>Q</sub>UASI-ISOMORPHISMS

$L _ { \infty }$-morphisms generalize usual morphisms of diferential graded Lie algebras. In particular, the first Taylor coeficient of an$L _ { \infty } .$-morphism from${ \bf g } _ { 1 }$to${ \bf g } _ { 2 }$is a morphism of complexes$( \mathbf { g } _ { 1 } , \boldsymbol { Q } _ { 1 } ^ { ( \mathbf { g } _ { 1 } ) } ) \longrightarrow ( \mathbf { g } _ { 2 } , \boldsymbol { Q } _ { 1 } ^ { ( \mathbf { g } _ { 2 } ) } )$where$\boldsymbol { Q } _ { 1 } ^ { ( \mathbf { g } _ { i } ) }$are the first Taylor coeficients of vector fields$Q ^ { ( \mathbf { g } _ { i } ) }$(which we denoted before simply by Q).

DEFINITION 4.5. A quasi-isomorphism between$L _ { \infty }$-algebras${ \bf g } _ { 1 } , { \bf g } _ { 2 }$is an$L _ { \infty } -$ morphism$\mathcal { F }$such that the first component$\mathcal { F } _ { 1 }$induces isomorphism between cohomology groups of complexes$( \mathbf { g } _ { 1 } , Q _ { 1 } ^ { ( \mathbf { g } _ { 1 } ) } )$and$( \mathbf { g } _ { 2 } , \mathcal { Q } _ { 1 } ^ { ( \mathbf { g } _ { 2 } ) } )$

Similarly, we can define quasi-isomorphisms for formal graded pointed Q-manifolds, as maps inducing isomorphisms of cohomology groups of tangent spaces at base points (endowed with diferentials which are linearizations of the vector field $Q )$

The essence of the homotopy/deformation theory is contained in the following theorem:

THEOREM 4.6. Let${ \bf g } _ { 1 } , { \bf g } _ { 2 }$be two$L _ { \infty } { - } a l g e b r a s$and$\mathcal { F }$be an$L _ { \infty }$-morphismfrom${ \bf g } _ { 1 }$to $\mathbf { g } _ { 2 } .$. Assume that$\mathcal { F }$is a quasi-isomorphism. Then there exists an$L _ { \infty }$-morphismfrom${ \bf g } _ { 2 }$ to${ \bf g } _ { 1 }$inducing the inverse isomorphism between cohomology$o f$complexes $( \mathbf { g } _ { i } , \boldsymbol { Q } _ { 1 } ^ { ( \mathbf { g } _ { i } ) } ) \ i = 1 , 2$. Also, for the case of diferential graded algebras,$L _ { \infty }$-morphism$\mathcal { F }$ induces an isomorphism between deformation functors associated with${ \bf { g } } _ { i }$.

The first part of this theorem shows that if${ \bf g } _ { 1 }$is quasi-isomorphic to${ \bf g } _ { 2 }$then${ \bf g } _ { 2 }$is quasi-isomorphic to${ \bf g } _ { 1 }$, i.e. we get an equivalence relation.

The isomorphism between deformation functors at the second part of the theorem is given by the formula from the last part of Section 4.3.

This theorem is essentially standard (see related results in [22, 24, 42]). Our approach consists in the translation of all relevant notions to the geometric language of formal graded pointed Q-manifolds.

## 4.5. A SKETCH OF THE PROOF OF THEOREM 4<sub>.</sub>6

## 4.5.1. Homotopy Classification of$L _ { \infty } { - } a l g e b r a s$

Any complex of vector spaces can be decomposed into the direct sum of a complex with trivial diferential and a contractible complex. There is an analogous decomposition in the nonlinear case.

DEFINITION 4.7. An L -algebra$( \mathbf { g } , Q )$is called minimal if the first Taylor coefficient$Q _ { 1 }$of the coderivation$\boldsymbol { Q }$vanishes.

The property of being minimal is invariant under$L _ { \infty }$-isomorphisms. Thus, one can speak about minimal formal graded pointed$Q \cdot$-manifolds.

DEFINITION 4.8. An$L _ { \infty } { \mathrm { - a l g e b r a } }$$( \mathbf { g } , Q )$is called linear contractible if higher Taylor coeficients$Q _ { \geqslant 2 }$vanish and the diferential$Q _ { 1 }$has trivial cohomology.

The property of being linear contractible is not$L _ { \infty }$-invariant. One can call formal graded pointed Q-manifold contractible if the corresponding diferential graded coalgebra is$L _ { \infty }$-isomorphic to a linear contractible one.

LEMMA 4.9. Any$L _ { \infty }$-algebra$( \mathbf { g } , Q )$is$L _ { \infty }$-isomorphic to the direct sum of a minimal and of a linear contractible$L _ { \infty } { - } a l g e b r a s$

Proof. This lemma says that there exists an afine structure on a formal graded pointed manifold in which the odd vector field Q has the form of a direct sum of a minimal and a linear contractible one. This afine structure can be constructed by induction in the degree of the Taylor expansion. The base of the induction is the decomposition of the complex$( \mathbf { g } , Q _ { 1 } )$into the direct sum of a complex with vanishing diferential and a complex with trivial cohomology. We leave details of the proof of the lemma to the reader.(

As a side remark, we mention analogy between this lemma and a theorem from singularity theory (see, for example, the beginning of 11.1 in [2]): for every germ f of analytic function at critical point one can find local coordinates $( x ^ { 1 } , \ldots , x ^ { k } , y ^ { 1 } , \ldots , y ^ { l } )$such that f¼ constant$+ Q _ { 2 } ( x ) + Q _ { \geqslant 3 } ( y )$, where$Q _ { 2 }$is a nondegenerate quadratic form in x and$Q _ { \geqslant 3 } ( y )$is a germ of a function in y such that its Taylor expansion at$y = 0$starts at terms of degree at least 3.

Let g be an$L _ { \infty } { \mathrm { - a l g e b r a } }$and$\mathbf { g } ^ { \mathrm { m i n } }$be a minimal$L _ { \infty } { \mathrm { - a l g e b r a } }$as in the previous lemma. Then there are two L<sub>1</sub>-morphisms (projection and inclusion)

$$
(\mathbf {g} [ 1 ] _ {\text { formal }}, 0) \longrightarrow (\mathbf {g} ^ {\min} [ 1 ] _ {\text { formal }}, 0), \quad (\mathbf {g} ^ {\min} [ 1 ] _ {\text { formal }}, 0) \longrightarrow (\mathbf {g} [ 1 ] _ {\text { formal }}, 0),
$$

which are both quasi-isomorphisms. From this follows that if

$$
(\mathbf {g} _ {1} [ 1 ] _ {\text { formal }}, 0) \longrightarrow (\mathbf {g} _ {2} [ 1 ] _ {\text { formal }}, 0)
$$

is a quasi-isomorphism then there exists a quasi-isomorphism

$$
(\mathbf {g} _ {1} ^ {\min} [ 1 ] _ {\text { formal }}, 0) \longrightarrow (\mathbf {g} _ {2} ^ {\min} [ 1 ] _ {\text { formal }}, 0).
$$

Any quasi-isomorphism between minimal$L _ { \infty } { \mathrm { - a l g e b r a s } }$is invertible, because it induces an isomorphism of spaces of cogenerators (the inverse mapping theorem mentioned at the end of Section 4.1). Thus, we proved the first part of the theorem. Also, we see that the set equivalence classes of$L _ { \infty } { \mathrm { - a l g e b r a s } }$up to quasi-isomorphisms can be naturally identified with the set of equivalence classes of minimal$L _ { \infty } -$ algebras up to$L _ { \infty }$-isomorphisms.

## 4.5.2. Deformation Functors at Fixed Points of Q

The deformation functor can be defined in terms of a formal graded Q-manifold M with base point (denoted by 0). The set of solutions of the Maurer–Cartan equation with coeficients in a finite-dimensional nilpotent nonunital algebra m is defined as the set of m-points of the formal scheme of zeroes of Q:

$$
\text { Maps } ((\text { Spec } (\mathbf {m} \oplus \mathbf {k} \cdot 1), \text {   base   point   }), (\text { Zeroes } (Q), 0))
$$

$$
\subset \operatorname{Maps} ((\operatorname{Spec} (\mathbf {m} \oplus \mathbf {k} \cdot 1), \text {   base   point   }), (M, 0)).
$$

In terms of the coalgebra$\mathcal { C }$corresponding to M this set is equal to the set of homomorphisms of coalgebras${ \mathbf { m } } ^ { * } \longrightarrow \mathcal { C }$with the image annihilated by$Q .$Another way to say this is to introduce a global (i.e. not formal) pointed Q-manifold of maps from$( \mathrm { S p e c } ( \mathbf { m } \oplus \mathbf { k } \cdot 1 )$, base point) to ðM; 0Þ and consider zeroes of the global vector field Q on it.

Two solutions$p _ { 0 }$and$p _ { 1 }$of the Maurer–Cartan equation are called gauge equivalent if there exists (parametrized by$\mathrm { S p e c } ( \mathbf { m } \oplus \mathbf { k } \cdot 1 ) )$polynomial family of odd vector fields$\xi ( t )$on M (of degree 1 with respect to Z-grading) and a polynomial solution of the equation

$$
\frac {\mathrm{d} p (t)}{\mathrm{d} t} = ([ Q, \xi (t) ] _ {\text { super }}) _ {| p (t)}, \quad p (0) = p _ {0}, \quad p (1) = p _ {1},
$$

where$p ( t )$is a polynomial family of m-points of formal graded manifold M with base point.

In terms of$L _ { \infty } \mathrm { - a l g e b r a s . }$, the set of polynomial paths$\{ p ( t ) \}$is naturally identified with$\mathbf { g } ^ { 1 } \otimes \mathbf { m } \otimes \mathbf { k } [ t ]$. Vector fields$\xi ( t )$depending polynomially on t are not necessarily vanishing at the base point 0.

One can check that the gauge equivalence defined above is indeed an equivalence relation, i.e. it is transitive. For formal graded pointed manifold M we define set $\mathrm { D e f } _ { M } ( \mathbf { m } )$as the set of gauge equivalence classes of solutions of the Maurer–Cartan equation. The correspondence m$\longmapsto \mathrm { D e f } _ { M } ( \mathbf { m } )$extends naturally to a functor denoted also by$\mathrm { D e f } _ { M }$. Analogously, for$L _ { \infty } { \mathrm { - a l g e b r a } }$g, we denote by$\mathrm { D e f _ { \mathbf { g } } }$the corresponding deformation functor.

One can easily prove the following properties:

(1) for a diferential graded Lie algebra g the deformation functor defined as above for$( \mathbf { g } [ 1 ] _ { \mathrm { f o r m a l } } , 0 )$, is naturally equivalent to the deformation functor defined in Section 3.2,

(2) any$L _ { \infty } { \mathrm { - m o r p h i s m } }$gives a natural transformation of functors,

(3) the functor$\mathrm { D e f } _ { \mathbf { g } _ { 1 } \oplus \mathbf { g } _ { 2 } }$corresponding to the direct sum of two$L _ { \infty } \mathrm { - a l g e b r a s . }$, is naturally equivalent to the product of functors$\mathrm { D e f } _ { \mathbf { g } _ { 1 } } \times \mathrm { D e f } _ { \mathbf { g } _ { 2 } }$2

(4) the deformation functor for a linear contractible$L _ { \infty } { \mathrm { - a l g e b r a ~ } } \mathbf { g }$is trivial,$\mathrm { D e f } _ { \mathbf { g } } ( \mathbf { m } )$ is a one-element set for every m.

Properties (2)–(4) are just trivial, and (1) is easy. It follows from properties (1)–(4) that if an$L _ { \infty } { \mathrm { - m o r p h i s m } }$of diferential graded Lie algebras is a quasi-isomorphism, then it induces an isomorphism ofdeformation functors. Theorem 4.6 is proven.(

We would like to notice here that in the definition of the deformation functor one can consider just a formal pointed super Q-manifold$( M , 0 )$(i.e. not a graded one), and m could be a finite-dimensional nilpotent diferential super commutative associative nonunital algebra.

## 4.6. FORMALITY

## 4.6.1. Two Diferential Graded Lie Algebras

Let X be a smooth manifold. We associate with it two diferential graded Lie algebras over R. The first diferential graded Lie algebra$D _ { \mathrm { p o l y } } ( X )$is a subalgebra of the shifted Hochschild complex of the algebra A of functions on X (see Section 3.4.2). The space$D _ { \mathrm { p o l y } } ^ { n } ( X ) , n \geqslant - 1$consists of Hochschild cochains$A ^ { \otimes ( n + 1 ) } \longrightarrow A$given by polydiferential operators. In local coordinates$( x ^ { i } )$any element of$D _ { \mathrm { p o l y } } ^ { n }$can be written as

$$
f _ {0} \otimes \dots \otimes f _ {n} \mapsto \sum_ {\left(I _ {0}, \dots , I _ {n}\right)} C ^ {I _ {0}, \dots , I _ {n}} (x) \cdot \partial_ {I _ {0}} \left(f _ {0}\right) \dots \partial_ {I _ {n}} \left(f _ {n}\right),
$$

where the sum is finite,$I _ { k }$denote multi-indices,$\partial _ { I _ { k } }$denote corresponding partial derivatives, and$f _ { k }$and$C ^ { I _ { 0 } , \ldots , I _ { n } }$are functions in$( x ^ { i } )$

The second diferential graded Lie algebra,$T _ { \mathrm { p o l y } } ( X )$is the graded Lie algebra of polyvector fields on X:

$$
T _ {\text { poly }} ^ {n} (X) = \Gamma (X, \wedge^ {n + 1} T _ {X}), \quad n \geqslant - 1
$$

endowed with the standard Schouten–Nijenhuis bracket and with the diferential $d : = 0$. We recall here the formula for this bracket:

$$
k, l \geqslant 0
$$

$$
\begin{array}{l} \left[ \xi_ {0} \wedge \dots \wedge \xi_ {k}, \eta_ {0} \wedge \dots \wedge \eta_ {l} \right] \\ = \sum_ {i = 0} ^ {k} \sum_ {j = 0} ^ {l} (- 1) ^ {i + j + k} \left[ \xi_ {i}, \eta_ {j} \right] \wedge \xi_ {0} \wedge \dots \wedge \xi_ {i - 1} \wedge \xi_ {i + 1} \wedge \dots \wedge \\ \wedge \xi_ {k} \wedge \eta_ {0} \wedge \dots \wedge \eta_ {j - 1} \wedge \eta_ {j + 1} \wedge \dots \wedge \eta_ {l}, \end{array}
$$

where$\xi _ { i } , \eta _ { j } \in \Gamma ( X , T _ { X } )$

for$k \geqslant 0$

$$
\begin{array}{l} \left[ \xi_ {0} \wedge \dots \wedge \xi_ {k}, h \right] \\ = \sum_ {i = 0} ^ {k} (- 1) ^ {i} \xi_ {i} (h) \cdot \left(\xi_ {0} \wedge \dots \wedge \xi_ {i - 1} \wedge \xi_ {i + 1} \wedge \dots \wedge \xi_ {k}\right), \\ h \in \Gamma (X, \mathcal {O} _ {X}), \xi_ {i} \in \Gamma (X, T _ {X}). \end{array}
$$

In local coordinates$( x ^ { 1 } , \ldots , x ^ { d } )$, if one replaces$\partial / \partial x ^ { i }$by odd variables$\psi _ { i }$and writes polyvector fields as functions in$( x ^ { 1 } , \ldots , x ^ { d } | \psi _ { 1 } , \ldots , \psi _ { d } )$, the bracket is

$$
[ \gamma_ {1}, \gamma_ {2} ] = \gamma_ {1} \bullet \gamma_ {2} - (- 1) ^ {k _ {1} k _ {2}} \gamma \bullet \gamma_ {1},
$$

where we introduce the following notation:

$$
\gamma_ {1} \bullet \gamma_ {2} := \sum_ {i = 1} ^ {d} \frac {\partial \gamma_ {1}}{\partial \psi_ {i}} \frac {\partial \gamma_ {2}}{\partial x ^ {i}}, \quad \gamma_ {i} \in T ^ {k _ {i}} (\mathbb {R} ^ {d}).
$$

4.6.1.1. A map from$T _ { \mathrm { p o l y } } ( X ) \quad t o \quad D _ { \mathrm { p o l y } } ( X )$. We have an evident map $\mathcal { U } _ { 1 } ^ { ( 0 ) } : T _ { \mathrm { p o l y } } ( X ) \longrightarrow D _ { \mathrm { p o l y } } ( X )$. It is defined, for$n \geqslant 0$, by

$$
\mathcal {U} _ {1} ^ {(0)} \colon (\xi_ {0} \wedge \dots \wedge \xi_ {n}) \mapsto \left(f _ {0} \otimes \dots \otimes f _ {n} \mapsto \frac {1}{(n + 1) !} \sum_ {\sigma \in \Sigma_ {n + 1}} \operatorname{sgn} (\sigma) \prod_ {i = 0} ^ {n} \xi_ {\sigma_ {i}} (f _ {i})\right),
$$

and for$h \in \Gamma ( X , { \mathcal { O } } _ { X } )$by$h { \mapsto } ( 1 { \mapsto } h )$

THEOREM 4.10.$\mathcal { U } _ { 1 } ^ { ( 0 ) }$is a quasi-isomorphism of complexes.

This is a version of the Hochschild–Kostant–Rosenberg theorem which says that, for a smooth afine algebraic variety Y over a field k of characteristic zero, the Hochschild cohomology of algebra${ \mathcal { O } } ( Y )$coincides with the space $\oplus _ { k \geqslant 0 } \Gamma ( X , \wedge ^ { k } T _ { Y } ) [ - k ]$of algebraic polyvector fields on Y (see [26]). The analogous statement for$C ^ { \infty }$manifolds seems to be well known, although we were not able to find it in the literature (e.g. in [7] a similar statement was proven for Hochschild homology). In any case, we give here a proof.

Proof. First of all, one can immediately check that the image of$\mathcal { U } _ { 1 } ^ { ( 0 ) }$is annihilated by the diferential in$D _ { \mathrm { p o l y } } ( X )$, i.e. that$\dot { \mathcal { U } } _ { 1 } ^ { ( 0 ) }$is a morphism of complexes.

Complex$D _ { \mathrm { p o l y } } ( X )$is filtered by the total degree of polydiferential operators. Complex$T _ { \mathrm { p o l y } } ( X )$endowed with zero diferential also carries a very simple filtration (just by degrees), such that$\mathcal { U } _ { 1 } ^ { ( 0 ) }$is compatible with filtrations. We claim that

$$
\operatorname{Gr} \left(\mathcal {U} _ {1} ^ {(0)}\right): \operatorname{Gr} \left(T _ {\text {poly}} (X)\right) \longrightarrow \operatorname{Gr} \left(D _ {\text {poly}} (X)\right)
$$

is a quasi-isomorphism. In the graded complex$\mathrm { { G r } } ( D _ { \mathrm { { p o l y } } } ( X ) )$associated with the filtered complex$D _ { \mathrm { p o l y } } ( X )$all components are sections of some natural vector bundles on X, and the diferential is A-linear,$A = C ^ { \infty } ( X )$. The same is true by trivial reasons for$T _ { \mathrm { p o l y } } ( X )$. Thus, we have to check that the map$\mathrm { G r } ( \mathcal { U } _ { 1 } ^ { ( 0 ) } )$is a quasi-isomorphism fiberwise.

Let x be a point of X and T be the tangent space at x. Principal symbols of polydiferential operators at x lie in vector spaces

$$
\operatorname{Sym} (T) \otimes \dots \otimes \operatorname{Sym} (T) \quad (n \text { times }, n \geqslant 0),
$$

where$\mathrm { S y m } ( T )$is the free polynomial algebra generated by T. It is convenient here to identify SymðTÞ with the cofree cocommutative coassociative coalgebra with counit cogenerated by T:

$$
\mathscr {C} := C (T) \oplus (\mathbf {k} \cdot 1) ^ {*}.
$$

$\mathrm { S y m } ( T )$is naturally isomorphic to the space of diferential operators on T with constant coeficients. If D is such an operator, then it defines a continuous linear functional on the algebra of formal power series at$0 \in T \colon$

$$
f \mapsto (D (f)) (0),
$$

i.e. an element of coalgebra C.

We denote by D the coproduct in coalgebra C. It is easy to see that diferential in the complex$\mathrm { { G r } } ( D _ { \mathrm { { p o l y } } } ( X ) )$in the fiber at x is the following:

$$
d: \otimes^ {n + 1} \mathcal {C} \longrightarrow \otimes^ {n + 2} \mathcal {C},
$$

$$
d = 1 ^ {*} \otimes \mathrm{id} _ {\otimes^ {n + 1} \mathcal {C}} - \sum_ {i = 0} ^ {n} (- 1) ^ {i} \mathrm{id} \otimes \dots \otimes \Delta_ {i} \otimes \dots \otimes \mathrm{id} + (- 1) ^ {n} \mathrm{id} _ {\otimes^ {n + 1} \mathcal {C}} \otimes 1 ^ {*},
$$

where$\Delta _ { i }$is coproduct D applied to the ith argument.

LEMMA 4.11. Let C be the cofree cocommutative coassociative coalgebra with counit cogenerated by a finite-dimensional vector space T. Then the natural homomorphism of complexes

$$
(\wedge^ {n + 1} T, \text { differential } = 0) \longrightarrow (\otimes^ {n + 1} \mathscr {C}, \text { differential   as   above })
$$

is a quasi-isomorphism.

What we consider is one of the standard complexes in homological algebra. One of possible proofs is the following:

Proof. Let us decompose complex$( \otimes ^ { n + 1 } { \mathcal { C } } )$into the infinite direct sum of subcomplexes consisting of tensors of fixed total degrees (homogeneous components with respect to the action of the Euler vector field on T). Our statement means in particular that for only finitely many degrees these subcomplexes have nontrivial cohomology. Thus, the statement of the lemma is true if the analogous statement holds when infinite sums are replaced by infinite products in the decomposition of $( \boldsymbol { \otimes } ^ { n + 1 } \boldsymbol { \mathcal { C } } )$. Components of the completed complex are spaces Hom$\left( A ^ { \otimes ( n + 1 ) } , \mathbf { k } \right)$, where A is the algebra of polynomial functions on T. It is easy to see that the completed complex calculates groups$\operatorname { E x } t _ { A - \mathrm { m o d } } ^ { n + 1 } ( \mathbf { k } , \mathbf { k } ) = { \textstyle \bigwedge } ^ { n + 1 } T ,$, where the one-dimensional space k is considered as an A-module (via values of polynomial at$0 \in T )$and has a resolution

$$
\dots \longrightarrow A \otimes A \longrightarrow A \longrightarrow 0 \longrightarrow \dots
$$

by free A-modules.

As a side remark, we notice that the statement of the lemma also holds if one replaces C by CðTÞ (i.e. the free coalgebra without counit) and removes terms with 1<sup></sup> from the diferential. In the language of Hochschild cochains, it means that the subcomplex of reduced cochains is quasi-isomorphic to the total Hochschild complex.

The lemma implies that$\mathrm { G r } ( \mathcal { U } _ { 1 } ^ { ( 0 ) } )$is an isomorphism fiberwise. Applying the standard argument with spectral sequences, we obtain the proof of the theorem. (

## 4.6.2. Main Theorem

Unfortunately, map$\mathcal { U } _ { 1 } ^ { ( 0 ) }$does not commute with Lie brackets, the Schouten–Nijenhuis bracket does not go to the Gerstenhaber bracket. We claim that this defect can be cured:

MAIN THEOREM There exists an$L _ { \infty }$-morphism U from$T _ { \mathrm { p o l y } } ( X )$to$D _ { \mathrm { p o l y } } ( X )$such that$\mathcal { U } _ { 1 } = \mathcal { U } _ { 1 } ^ { ( 0 ) }$

In other words, this theorem says that$T _ { \mathrm { p o l y } } ( X )$and$D _ { \mathrm { p o l y } } ( X )$are quasi-isomorphic diferential graded Lie algebras. In analogous situation in rational homotopy theory (see [43]), a diferential graded commutative algebra is called formal if it is quasi-isomorphic to its cohomology algebra endowed with zero diferential. This explains the title of Section 4.6.

The quasi-isomorphism U in the theorem is not canonical. We will construct explicitly a family of quasi-isomorphisms parametrized in certain sense by a contractible space. It means that our construction is canonical up to (higher) homotopies.

Solutions of the Maurer–Cartan equation in$T _ { \mathrm { p o l y } } ( X )$are exactly Poisson structures on X:

$$
\alpha \in T _ {\mathrm{poly}} ^ {1} (X) = \Gamma (X, \wedge^ {2} T _ {X}), [ \alpha , \alpha ] = 0.
$$

Any such a defines also a solution formally depending on$\hbar ,$

$$
\gamma (\hbar) := \alpha \cdot \hbar \in T _ {\mathrm{poly}} ^ {1} (X) [ [ \hbar ] ] \quad [ \gamma (\hbar), \gamma (\hbar) ] = 0.
$$

The gauge group action is the action of the difeomorphism group by conjugation. Solutions of the Maurer–Cartan equation in$D _ { \mathrm { p o l y } } ( X )$formally depending on h are star products. Thus, we obtain as a corollary that any Poisson structure on X gives a canonical equivalence class of star products, and the Theorem 1.1.

The rest of the paper is devoted to the proof of the Main Theorem, and to the discussion of various applications, corollaries and extensions. In Section 5, we will make some preparations for the universal formula (Section 6) for an$L _ { \infty }$-morphism from$T _ { \mathrm { p o l y } } ( X )$to$D _ { \mathrm { p o l y } } ( X )$in the case of flat space$X = \mathbb { R } ^ { d }$. In Section 7 we extend our construction to general manifolds.

## 4.6.3. Nonuniqueness

There are other natural quasi-isomorphisms between$T _ { \mathrm { p o l y } } ( X )$and$D _ { \mathrm { p o l y } } ( X )$which difer essentially from the quasi-isomorphism$\boldsymbol { \mathcal U }$constructed in Sections 6 and$^ { 7 , }$i.e. not even homotopic in a natural sense to$\mathcal { U } .$By homotopy here we mean the following.$L _ { \infty }$-morphisms from one$L _ { \infty } { \mathrm { - a l g e b r a } }$to another can be identified with fixed points of$\boldsymbol { Q }$on infinite-dimensional supermanifold of maps. Mimicking constructions and definitions from Section 4.5.2, one can define an equivalence relation (homotopy equivalence) on the set of$L _ { \infty } \mathrm { { - m o r p h i s m s } }$

Firstly, the multiplicative group$\mathbb { R } ^ { \times }$acts by automorphisms of$T _ { \mathrm { p o l y } } ( X )$, multi-plying elements$\gamma \in T _ { \mathrm { p o l y } } ( X ) ^ { k }$by$\lambda ^ { k }$for$\lambda \in \mathbb { R } ^ { \times }$. Composing these automorphisms with U one get a one-parameter family of quasi-isomorphisms. Secondly, in [31] we constructed an exotic infinitesimal$L _ { \infty } { \mathrm { - a u t o m o r p h i s m } }$of$T _ { \mathrm { p o l y } } ( X )$for the case $X = \mathbb { R } ^ { d }$which probably extends to general manifolds. In particular, this exotic automorphism produces a vector field on the ‘space of Poisson structures’. The evolution with respect to time t is described by the following non linear partial diferential equation:

$$
\frac {\mathrm{d} \alpha}{\mathrm{d} t} := \sum_ {i, j, k, l, m, k ^ {\prime}, l ^ {\prime}, m ^ {\prime}} \frac {\partial^ {3} \alpha^ {i j}}{\partial x ^ {k} \partial x ^ {l} \partial x ^ {m}} \frac {\partial \alpha^ {k k ^ {\prime}}}{\partial x ^ {l ^ {\prime}}} \frac {\partial \alpha^ {l l ^ {\prime}}}{\partial x ^ {m ^ {\prime}}} \frac {\partial \alpha^ {m m ^ {\prime}}}{\partial x ^ {k ^ {\prime}}} (\partial_ {i} \wedge \partial_ {j}),
$$

where$\begin{array} { r } { \alpha = \sum _ { i , j } \alpha ^ { i j } ( x ) \partial _ { i } \wedge \partial _ { j } } \end{array}$is a bi-vector field on$\mathbb { R } ^ { d } .$

A priori, we can guarantee the existence of a solution of the evolution only for small times and real-analytic initial data. One can show that:

(1) this evolution preserves the class of (real-analytic) Poisson structures,

(2) if two Poisson structures are conjugate by a real-analytic difeomorphism, then the same will hold after the evolution.

Thus, our evolution operator is essentially intrinsic and does not depend on the choice of coordinates.

Combining it with the action of$\mathbb { R } ^ { \times }$as above we see that the Lie algebra a$\operatorname { f f } ( 1 , \mathbb { R } )$ of infinitesimal afine transformations of the line$\mathbb { R } ^ { 1 }$acts nontrivially on the space of homotopy classes of quasi-isomorphisms between$T _ { \mathrm { p o l y } } ( X )$and$D _ { \mathrm { p o l y } } ( X )$. Maybe, there are other exotic$L _ { \infty } { \mathrm { - a u t o m o r p h i s m s } }$, this possibility is not ruled out. It is not clear whether our quasi-isomorphism U is better than others.

## 5. Configuration Spaces and their Compactifications

## 5.1. DEFINITIONS

Let$n , m$be nonnegative integers satisfying the inequality$2 n + m \geqslant 2$. We denote by ${ \mathrm { C o n f } } _ { n , m }$the product of the configuration space of the upper half-plane with the configuration space of the real line:

$$
\begin{array}{c} \text {Conf} _ {n, m} = \{(p _ {1}, \ldots , p _ {n}; q _ {1}, \ldots , q _ {m}) \mid p _ {i} \in \mathscr {H}, q _ {j} \in \mathbb {R}, p _ {i _ {1}} \neq p _ {i _ {2}} \text {for} \\ i _ {1} \neq i _ {2}, q _ {j _ {1}} \neq q _ {j _ {2}} \text {for} j _ {1} \neq j _ {2} \}. \end{array}
$$

${ \mathrm { C o n f } } _ { n , m }$is a smooth manifold of dimension$2 n + m$The group$G ^ { ( 1 ) }$of holomorphic transformations of$\mathbb { C P } ^ { 1 }$preserving the upper half-plane and the point$\infty ,$, acts on${ \mathrm { C o n f } } _ { n , m }$. This group is a two-dimensional connected Lie group, isomorphic to the group of orientation-preserving afine transformations of the real line:

$$
G ^ {(1)} = \{z \mapsto a z + b \mid a, b \in \mathbb {R}, a > 0 \}.
$$

It follows from the condition$2 n + m \geqslant 2$that the action of$G ^ { ( 1 ) }$on${ \mathrm { C o n f } } _ { n , m }$is free. The quotient space$C _ { n , m } : = \mathrm { C o n f } _ { n , m } / G ^ { ( 1 ) }$is a manifold of dimension$2 n + m - 2$. If $P = ( p _ { 1 } , \ldots , p _ { n } ; q _ { 1 } , \ldots , q _ { m } )$is a point of${ \mathrm { C o n f } } _ { n , m }$, then we denote by ½P the corresponding point of$C _ { n , m }$

Analogously, we introduce simpler spaces Conf<sub>n</sub> and$C _ { n }$for any$n \geqslant 2$:

$$
\operatorname{Conf} _ {n} := \left\{\left(p _ {1}, \dots , p _ {n}\right) \mid p _ {i} \in \mathbb {C}, p _ {i} \neq p _ {j} \text {   for   } i \neq j \right\},
$$

$$
C _ {n} = \operatorname{Conf} _ {n} / G ^ {(2)}, \quad \dim (C _ {n}) = 2 n - 3,
$$

where$G ^ { ( 2 ) }$is a three-dimensional Lie group,

$$
G ^ {(2)} = \{z \mapsto a z + b \mid a \in \mathbb {R}, b \in \mathbb {C}, a > 0 \}.
$$

We will construct compactifications$\overline { { C } } _ { n , m }$of$C _ { n , m }$( and compactifications$\overline { { C } } _ { n }$of$C _ { n } )$ which are smooth manifolds with corners.

We recall that a manifold with corners (of dimension$d )$is defined analogously to a usual manifold with boundary, with the only diference being that the manifold with corners looks locally as an open part of the closed simplicial cone$( \mathbb { R } _ { \geqslant 0 } ) ^ { d }$. For example, the closed hypercube$[ 0 , 1 ] ^ { d }$is a manifold with corners. There is a natural smooth stratification by faces of any manifold with corners.

First of all, we give one of possible formal definitions of the compactification$\overline { { C } } _ { n }$ where$n \geqslant 2$. With any point$\left[ \left( p _ { 1 } , \ldots , p _ { n } \right) \right]$of$C _ { n } .$, we associate a collection of$n ( n - 1 )$Þ angles with values in$\mathbb { R } / 2 \pi \mathbb { Z } \colon ( \mathrm { A r g } ( p _ { i } - p _ { j } ) ) _ { i \neq j }$and$n ^ { 2 } ( n - 1 ) ^ { 2 }$ratios of distances.

$$
\left(\left| p _ {i} - p _ {j} \right| / \left| p _ {k} - p _ {l} \right|\right) _ {i \neq j, k \neq l}.
$$

It is easy to see that we obtain an embedding of$C _ { n }$into the manifold $( \mathbb { R } / 2 \pi \mathbb { Z } ) ^ { n ( n - 1 ) } \times \mathbb { R } _ { > 0 } ^ { n ^ { 2 } ( n - 1 ) ^ { 2 } }$. The space$\overline { { C } } _ { n }$is defined as the compactification of the image of this embedding in larger manifold

$$
(\mathbb {R} / 2 \pi \mathbb {Z}) ^ {n (n - 1)} \times [ 0, + \infty ] ^ {n ^ {2} (n - 1) ^ {2}}.
$$

For the space$C _ { n , m }$we use first its embedding to$C _ { 2 n + m }$which is defined on the level of configuration spaces as

$$
(p _ {1}, \dots , p _ {n}; q _ {1}, \dots , q _ {m}) \mapsto (p _ {1}, \dots , p _ {n}, \overline {{p}} _ {1}, \dots , \overline {{p}} _ {n}, q _ {1}, \dots , q _ {m})
$$

and then compactify the image in$\overline { { C } } _ { 2 n + m }$. The result is by definition the compactified space$\overline { { C } } _ { n , m }$

One can show that open strata of$\overline { { C } } _ { n , m }$are naturally isomorphic to products of manifolds of type$C _ { n ^ { \prime } , m ^ { \prime } }$and$C _ { n ^ { \prime } }$. In the next subsection we will describe explicitly $\overline { { C } } _ { n , m }$as a manifold with corners.

There is a natural action of the permutation group$\Sigma _ { n }$on$C _ { n } .$, and also of$\Sigma _ { n } \times \Sigma _ { m }$ on$C _ { n , m }$. This gives us a possibility to define spaces$C _ { A }$and$C _ { A , B }$for finite sets$A , B$ such that #$\Rightarrow 2$or$2 \# A + \# B \geqslant 2$, respectively. If$A ^ { \prime } \hookrightarrow A$and$B ^ { \prime } \hookrightarrow B$are inclusions of sets, then there are natural fibrations (forgetting maps)$C _ { A } \longrightarrow C _ { A ^ { \prime } }$and $C _ { A , B } \longrightarrow C _ { A ^ { \prime } , B ^ { \prime } }$

## 5.2. LOOKING THROUGH A MAGNIFYING GLASS

From the definition of the compactification given in the previous subsection, it is not clear what is exactly the point of the compactified space. We are going to explain an intuitive idea underlying a direct construction of the compactification$\overline { { C } } _ { n , m }$as a manifold with corners. For more formal treatment of compactifications of configuration spaces, we refer the reader to [17] (for the case of smooth algebraic varieties).

Let us try to look through a magnifying glass, or better through a microscope with arbitrary magnification, at diferent parts of the picture formed by points on ${ \mathcal { H } } \cup \mathbb { R } \subset \mathbb { C }$and by the line$\mathbb { R } \subset \mathbb { C }$. Here we use Euclidean geometry on$\mathbb { C } \simeq \mathbb { R } ^ { 2 }$ instead of Lobachevsky geometry.

Before doing this, let us first consider the case of a configuration on$\mathbb { R } ^ { 2 } \simeq \mathbb { C } .$, i.e. without the horizontal line$\mathbb { R } \subset \mathbb { C }$. We say that the configuration$( p _ { 1 } , \ldots , p _ { n } )$is in standard position if

(1) the diameter of the set$\{ p _ { 1 } , \ldots , p _ { n } \}$is equal to 1, and

(2) the center of the minimal circle containing$\{ p _ { 1 } , \ldots , p _ { n } \}$is$0 \in \mathbb { C }$

$$
^ 2 \bullet \quad \begin{array}{c} \bullet^ {3} \\ \bullet^ {4} \end{array}
$$

$$
_ 5 \cdot^ {6}
$$

Figure 3. Configuration of points close to the boundary of the compactified configuration space.

It is clear that any configuration of n pairwise distinct points in the case$n \geqslant 2$can be uniquely put to the standard position by a unique element of group$G ^ { ( 2 ) }$. The set of configurations in the standard position gives a continuous section$s ^ { \mathrm { c o n t } }$of the natural projection map${ \mathrm { C o n f } } _ { n } \longrightarrow C _ { n }$

For a configuration in the standard position there could be several domains where we will need magnification in order to see details. These domains are those where at least two points of the configuration come too close to each other.

After an appropriate magnification of any such domain, we again get a stable configuration (i.e. the number of points there are at least 2). Then we can put it again in the standard position and repeat the procedure.

In such a way, we get an oriented tree T with one root, and leaves numbered from 1 to n. For example, the configuration in Figure 3 gives the tree in Figure 4.

For every vertex of tree T except leaves, we denote by StarðvÞ the set of edges starting at v. For example, in the figure from above the set StarðrootÞ has three elements, and sets StarðvÞ for other three vertices all have two elements.

Points in$C _ { n }$close to one which we consider, can be parametrized by the following data:

(a) for each vertex v of T except leaves, a configuration$c _ { \nu }$in the standard position of points labeled by the set StarðvÞ,

![](images/page_27_image_10.jpg)

Figure 4. Tree corresponding the limiting point in the configuration space.

(b) for each vertex v except leaves and the root of the tree, the scale$s _ { \nu } > 0$with which we should put a copy of$c _ { \nu }$instead of the corresponding point$p _ { \nu } \in \mathbb { C }$on configuration$c _ { u }$where$u \in V _ { T }$is such that$( u , v ) \in E _ { T }$

More precisely, we act on the configuration$c _ { \nu }$by the element$\left( z \mapsto s _ { \nu } z + p _ { \nu } \right)$of$G ^ { ( 2 ) }$ Numbers$S _ { \nu }$are small but positive. The compactification$\overline { { C } } _ { n }$is achieved by formally permitting some of scales$S _ { \nu }$to be equal to 0.

In this way we get a compact topological manifold with corners, with strata$C _ { T }$ labeled by trees$T$(with leaves numbered from 1 to n). Each stratum$C _ { T }$is canonically isomorphic to the product$\prod _ { \nu } C _ { \mathrm { S t a r } ( \nu ) }$over all vertices v except leaves.

In the above description points of$C _ { T }$correspond to collections of configurations with all scales$S _ { \nu }$equal to zero. Let us repeat: as a set$\overline { { C } } _ { n }$coincides with

![](images/page_28_image_4.jpg)

In order to introduce a smooth structure on$\overline { { C } } _ { n } .$, we should choose a$\Sigma _ { n }$-equivariant smooth section$s ^ { \mathrm { s m o o t h } }$of the projection map${ \mathrm { C o n f } } _ { n } \longrightarrow C _ { n }$instead of the section$s ^ { \mathrm { c o n t } }$ given by configurations in the standard position. Local coordinates on$\overline { { C } } _ { n }$near a given point lying in stratum$C _ { T }$are scales$s _ { \nu } \in \mathbb { R } _ { \geqslant 0 }$close to zero and local coordinates in manifolds$C _ { \mathrm { S t a r } ( \nu ) }$for all$\nu \in V _ { T } \setminus \{ \mathrm { l e a v e s } \}$. The resulting structure of a smooth manifold with corners does not depend on the choice of the section$s ^ { \mathrm { s m o o t h } }$

The case of configurations of points on$\mathcal { H } \cup$[ R is not much harder. First of all we say that a finite nonempty set S of points on${ \mathcal { H } } \cup \mathbb { R }$is in the standard position if

(1) the projection of the convex hull of S to the horizontal line$\mathbb { R } \subset \mathbb { C } \simeq \mathbb { R } ^ { 2 }$is either the one-point set f0g, or it is an interval with the center at$0 ,$,

(2) the maximum of the diameter of S and of the distance from S to R is equal to 1.

It is easy to see that for$2 n + m \geqslant 2$(the stable case) any configuration of n points on $\mathcal { H }$and m points on R can be put uniquely in standard position by an element of$G ^ { ( 1 ) }$ In order to get a smooth structure, we repeat the same arguments as for the case of manifolds$C _ { n }$

Domains where we will need magnification in order to see details, are now of two types. The first case is when at least two points of the configuration come too close to each other. We want to know whether what we see is a single point or a collection of several points. The second possibility is when a point on$\mathcal { H }$comes too close to R. Here we also want to decide whether what we see is a point (or points) on$\mathcal { H }$or on R.

If the domain which we want to magnify is close to R, then after magnification we again get a stable configuration which we can put into the standard position. If the domain is inside${ \mathcal { H } } .$, then after magnification we get a picture without the horizontal line in it, and we are back in the situation concerning$\overline { { C } } _ { n ^ { \prime } }$for$n ^ { \prime } \leqslant n$

It is instructional to draw low-dimensional spaces$C _ { n , m }$. The simplest one, $C _ { 1 , 0 } = \overline { { C } } _ { 1 , 0 }$is just a point. The space$C _ { 0 , 2 } = \overline { { C } } _ { 0 , 2 }$is a two-element set. The space$C _ { 1 , 1 }$ is an open interval, and its closure$\overline { { C } } _ { 1 , 1 }$is a closed interval (the real line$\mathbb { R } \subset \mathbb { C }$is dashed in Figure 5).

![](images/page_29_image_0.jpg)

Figure 5. Space$C _ { 1 , 1 }$homeomorphic to an interval.

![](images/page_29_image_2.jpg)

Figure 6. Space$\overline { { C } } _ { 2 , 0 }$

The space$C _ { 2 , 0 }$is difeomorphic to${ \mathcal { H } } \setminus \{ 0 + 1 \cdot i \}$. The reason is that by the action of$G ^ { ( 1 ) }$we can put point$p _ { 1 }$to the position$i = \sqrt { - 1 } \in \mathcal { H }$. The closure$\overline { { C } } _ { 2 , 0 }$can be drawn as in Figure 6 or as in Figure 7.

Forgetting maps (see the end of Section 5.1) extend naturally to smooth maps of compactified spaces.

## 5.2.1. Boundary Strata

We give here a list of all strata in$\overline { { C } } _ { A , B }$of codimension 1:

(S1) points$p _ { i } \in \mathcal { H }$for$i \in S \subseteq A$; where$\# S \geqslant 2$, move close to each other but far from R,

(S2) points$p _ { i } \in \mathcal { H }$for$i \in S \subseteq A$and points$q _ { j } \in \mathbb { R }$for$j \in S ^ { \prime } \subseteq B ,$, where $2 \# S + \# S ^ { \prime } \geqslant 2$, all move close to each other and to R, with at least one point left outside S and S<sup>0</sup>, i.e.$\# S + \# S ^ { \prime } \leqslant \# A + \# B - 1$

The stratum of type (S1) is

$$
\partial_ {S} \overline {{C}} _ {A, B} \simeq C _ {S} \times C _ {(A \backslash S) \sqcup \{p t \}, B},
$$

where fptg is a one-element set, whose element represents the cluster$\left( \boldsymbol { p } _ { i } \right) _ { i \in S }$of points in H. Analogously, the stratum of type (S2) is

$$
\partial_ {S, S ^ {\prime}} \overline {{C}} _ {A, B} \simeq C _ {S, S ^ {\prime}} \times C _ {A \setminus S, (B \setminus S ^ {\prime}) \sqcup \{p t \}}.
$$

![](images/page_29_image_14.jpg)

Figure 7. The Eye.

## 6. Universal Formula

In this section we propose a formula for an L<sub>1</sub>-morphism$T _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } )  D _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } )$ generalizing a formula for the star product in Section 2. In order to write it, we need to make some preparations.

## 6.1. ADMISSIBLE GRAPHS

DEFINITION 6.1. Admissible graph C is a graph with labels such that

(1) the set of vertices V is$\{ 1 , \ldots , n \} \sqcup \{ { \overline { { 1 } } } , \ldots , { \overline { { m } } } \}$where n;$m \in \mathbb { Z } _ { \geqslant 0 } , 2 n + m - 2 \geqslant 0 ;$ vertices from the set$\{ 1 , \ldots , n \}$are called vertices of the first type, vertices from $\{ { \overline { { 1 } } } , \dots , { \overline { { m } } } \}$are called vertices of the second type,

(2) every edge$\left( \nu _ { 1 } , \nu _ { 2 } \right) \in E _ { \Gamma }$starts at a vertex of first type,$\nu _ { 1 } \in \{ 1 , \ldots , n \}$，

(3) for every vertex$k \in \{ 1 , \ldots , n \}$of the first type, the set of edges

$$
\operatorname{Star} (k) := \left\{\left(v _ {1}, v _ {2}\right) \in E _ {\Gamma} \mid v _ {1} = k \right\}
$$

starting from$k ,$is labeled by symbols$( e _ { k } ^ { 1 } , \ldots , e _ { k } ^ { \# \mathrm { S t a r } ( k ) } )$

The labeled graphs considered in Section$2$are exactly (after the identifications $L = \overline { { 1 } } , R = \overline { { 2 } } )$admissible graphs such that m is equal to$^ { 2 , }$and the number of edges starting at every vertex of first type is also equal to 2.

## 6.2. DIFFERENTIAL FORMS ON CONFIGURATION SPACES

The space$\overline { { C } } _ { 2 , 0 }$(the Eye) is homotopy equivalent to the standard circle$S ^ { 1 } \simeq \mathbb { R } / 2 \pi \mathbb { Z }$ Moreover, one of its boundary components, the space$C _ { 2 } = \overline { { C } } _ { 2 }$, is naturally identified with the standard circle$S ^ { 1 }$. The other component of the boundary is the union of two closed intervals (copies of$\overline { { C } } _ { 1 , 1 } )$with identified end points.

DEFINITION 6.2. An angle map is a smooth map$\phi \colon \overline { { C } } _ { 2 , 0 }  \mathbb { R } / 2 \pi \mathbb { Z } \simeq S ^ { 1 }$such that the restriction of / to$C _ { 2 } \simeq S ^ { 1 }$is the angle measured in the anti-clockwise direction from the vertical line, and / maps the whole upper interval$\overline { { C } } _ { 1 , 1 } \simeq [ 0 , 1 ]$of the Eye, to a point in$S ^ { 1 }$

We will denote$\phi ( [ ( x , y ) ] )$simply by$\phi ( x , y )$where$x , y \in { \mathcal { H } } \sqcup \mathbb { R } , x \neq y$. It follows from the definition that$\mathrm { d } \phi ( x , y ) = 0 { \mathrm { ~ i f ~ } } x$stays in R.

For example, the special map$\phi ^ { h }$used in the formula in Section 2, is an angle map. In the rest of the paper we can use any$\phi ,$, not necessarily harmonic.

We are now prepared for the analytic part of the universal formula. Let C be an admissible graph with n vertices of the first type, m vertices of the second type and with$2 n + m - 2$edges. We define the weight of graph C by the following formula:

$$
W _ {\Gamma} := \prod_ {k = 1} ^ {n} \frac {1}{(\# \operatorname{Star} (k)) !} \frac {1}{(2 \pi) ^ {2 n + m - 2}} \int_ {\overline {{C}} _ {n, m} ^ {+}} \wedge_ {e \in E _ {\Gamma}} \mathrm{d} \phi_ {e}.
$$

Let us explain what is written here. The domain of integration$\overline { { C } } _ { n , m } ^ { + }$is a connected component of$\overline { { C } } _ { n , m }$which is the closure of configurations for which points $q _ { j } , 1 \leqslant j \leqslant m$on R are placed in the increasing order$q _ { 1 } < \cdots < q _ { m }$

The orientation of${ \mathrm { C o n f } } _ { n , m }$is the product of the standard orientation on the coordinate space$\mathbb { R } ^ { m } \supset \{ ( q _ { 1 } , \dots , q _ { m } ) | q _ { j } \in \mathbb { R } \}$, with the product of standard orientations on the plane$\mathbb { R } ^ { 2 }$(for points$p _ { i } \in \mathcal { H } \subset \mathbb { R } ^ { 2 } )$. The group$G ^ { ( 1 ) }$is even-dimensional and naturally oriented because it acts freely and transitively on the complex manifold ${ \mathcal { H } } .$. Thus, the quotient space$\begin{array} { r } { C _ { n , m } = \mathbf { C o n f } _ { n , m } / G ^ { ( 1 ) } } \end{array}$again carries a natural orientation.

Every edge e of C defines a map from$\overline { { C } } _ { n , m }$to$\overline { { C } } _ { 2 , 0 }$or to$\overline { { C } } _ { 1 , 1 } \subset \overline { { C } } _ { 2 , 0 }$(the forgetting map). Here we consider inclusion$\overline { { C } } _ { 1 , 1 }$in$\overline { { C } } _ { 2 , 0 }$as the lower interval of the Eye. The pullback of the function$\phi$by the map$\overline { { C } } _ { n , m }  \overline { { C } } _ { 2 , 0 }$corresponding to edge e is denoted by$\phi _ { e }$

Finally, the ordering in the wedge product of 1-forms$d \phi _ { \epsilon }$is fixed by enumeration of the set of sources of edges and by the enumeration of the set of edges with a given source.

The integral giving$W _ { \Gamma }$is absolutely convergent because it is an integral of a smooth diferential form over a compact manifold with corners.

## 6.3. PRE-<sub>L1</sub>-MORPHISMS ASSOCIATED WITH GRAPHS

For any admissible graph C with n vertices of the first type, m vertices of the second type, and 2n$+ m - 2 + l$edges where$l \in \mathbb { Z } .$we define a linear map

$$
\mathcal {U} _ {\Gamma}: \otimes^ {n} T _ {\text { poly }} (\mathbb {R} ^ {d}) \to D _ {\text { poly }} (\mathbb {R} ^ {d}) [ 1 + l - n ].
$$

This map has only one nonzero graded component$( \mathcal { U } _ { \Gamma } ) _ { ( k _ { 1 } , \ldots , k _ { n } ) }$where $k _ { i } = \# \mathrm { S t a r } ( i ) - 1 , i = 1 , \dots , n$. If$l = 0$, then from$\mathcal { U } _ { \Gamma }$after anti-symmetrization, we obtain a pre-$L _ { \infty }$-morphism.

Let$\gamma _ { 1 } , \dots , \gamma _ { n }$be polyvector fields on$\mathbb { R } ^ { d }$of degrees$( k _ { 1 } + 1 ) , \ldots , ( k _ { n } + 1 )$and $f _ { 1 } , \ldots , f _ { m }$be functions on$\mathbb { R } ^ { d }$. We are going to write a formula for function$\Phi$on$\mathbb { R } ^ { n }$:

$$
\Phi := \left(\mathcal {U} _ {\Gamma} \left(\gamma_ {1} \otimes \dots \otimes \gamma_ {n}\right)\right) \left(f _ {1} \otimes \dots \otimes f _ {m}\right).
$$

The formula for U is the sum over all configurations of indices running from 1 to$d ,$ labeled by$E _ { \Gamma }$:

$$
\Phi = \sum_ {I: E _ {\Gamma} \rightarrow \{1, \dots , d \}} \Phi_ {I},
$$

where$\Phi _ { I }$is the product over all$n + m$vertices of C of certain partial derivatives of functions$f _ { j }$and of coeficients of$\gamma _ { i }$.

Namely, with each vertex$i , 1 \leqslant i \leqslant n$of the first type we associate a function$\psi _ { i }$on $\mathbb { R } ^ { d }$which is a coeficient of the polyvector field$\gamma _ { i } .$

$$
\psi_ {i} = \left\langle \gamma_ {i}, \mathrm{d} x ^ {I \left(e _ {i} ^ {1}\right)} \otimes \dots \otimes \mathrm{d} x ^ {I \left(e _ {i} ^ {k _ {i} + 1}\right)} \right\rangle .
$$

Here we use the identification of polyvector fields with skew-symmetric tensor fields as

$$
\xi_ {1} \wedge \dots \wedge \xi_ {k + 1} \rightarrow \sum_ {\sigma \in \Sigma_ {k + 1}} \operatorname{sgn} (\sigma) \xi_ {\sigma_ {1}} \otimes \dots \otimes \xi_ {\sigma_ {k + 1}} \in \Gamma (\mathbb {R} ^ {d}, T ^ {\otimes (k + 1)}).
$$

For each vertex$\bar { j }$of the second type, the associated function$\psi _ { \overline { { i } } }$is defined as$f _ { j } .$

Now, at each vertex of graph C we put a function on$\mathbb { R } ^ { d } \left( \mathrm { i } . \mathrm { e } . \mathrm { \Delta } \psi _ { i } ^ { d } \right)$or w ). Also, on the edges ofgraph C there are indices$I ( e )$which label coordinates in$\mathbb { R } ^ { d }$. In the next step we put into each vertex$\nu ,$instead of function$\psi _ { \nu } ,$, its partial derivative

$$
\left(\prod_ {e \in E _ {\Gamma}, e = (*, v)} \partial_ {I (e)}\right) \psi_ {v}
$$

and then take the product over all vertices v of C. The result is by definition the summand$\Phi _ { I }$

Construction of the function U from the graph C, polyvector fields$\gamma _ { i }$and functions$f _ { j } ,$is invariant under the action of the group of afine transformations of$\mathbb { R } ^ { d }$ because we contract upper and lower indices.

## 6.4. MAIN THEOREM FOR$X = \mathbb { R } ^ { d }$, AND THE PROOF

We define a pre-$L _ { \infty }$-morphism U :$T _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } )  D _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } )$by the formula for its nth Taylor coeficient$\mathcal { U } _ { n } , n \geqslant 1$considered as a skew-symmetric polylinear map (see Section 4.2) from$\otimes ^ { n } T _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } )$to$D _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } ) [ 1 - n ]$

$$
\mathcal {U} _ {n} := \sum_ {m \geqslant 0} \sum_ {\Gamma \in G _ {n, m}} W _ {\Gamma} \times \mathcal {U} _ {\Gamma}.
$$

Here$G _ { n , m }$denotes the set of all admissible graphs with n vertices of the first type, m vertices in the second group and$2 n + m - 2$edges, where$n \geqslant 1 , m \geqslant 0$(and automatically$2 n + m - 2 \geqslant 0 )$.

## THEOREM 6.3. U is an$L _ { \infty }$-morphism, and also a quasi-isomorphism.

Proof. The condition that U is an$L _ { \infty }$-morphism (see Sections 4.3 and 3.4.2) can be written explicitly as

$$
\begin{array}{l} f _ {1} \cdot (\mathcal {U} _ {n} (\gamma_ {1} \wedge \dots \wedge \gamma_ {n})) (f _ {2} \otimes \dots \otimes f _ {m}) \pm (\mathcal {U} _ {n} (\gamma_ {1} \wedge \dots \wedge \gamma_ {n})) (f _ {1} \otimes \dots \otimes f _ {m - 1}) \cdot f _ {m} + \\ + \sum_ {i = 1} ^ {m - 1} \pm (\mathcal {U} _ {n} (\gamma_ {1} \wedge \dots \wedge \gamma_ {n})) (f _ {1} \otimes \dots \otimes (f _ {i} f _ {i + 1}) \otimes \dots \otimes f _ {m}) + \\ + \sum_ {i <   j} \pm \big (\mathcal {U} _ {n - 1} ([ \gamma_ {i}, \gamma_ {j} ] \wedge \gamma_ {1} \wedge \dots \wedge \gamma_ {n}) \big) (f _ {1} \otimes \dots \otimes f _ {m}) + \\ + \frac {1}{2} \sum_ {k, l \geqslant 1, k + l = n} \frac {1}{k ! l !} \sum_ {\sigma \in \Sigma_ {n}} \pm \\ \pm \left[ \mathcal {U} _ {k} (\gamma_ {\sigma_ {1}} \wedge \dots \wedge \gamma_ {\sigma_ {k}}), \mathcal {U} _ {l} (\gamma_ {\sigma_ {k + 1}} \wedge \dots \wedge \gamma_ {\sigma_ {n}}) \right] \times (f _ {1} \otimes \dots \otimes f _ {m}) = 0. \end{array}
$$

Here$\gamma _ { i }$are polyvector fields,$f _ { i }$are functions,$\textstyle { \mathcal { U } } _ { n }$are homogeneous components of U (see Section 4.1). There is a way to rewrite this formula. Namely, we define$\boldsymbol { \mathcal { U } } _ { 0 }$as the map$\otimes ^ { 0 } ( T _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } ) ) \longrightarrow D _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } ) [ 1 ]$which maps the generator 1 of R$\simeq \otimes ^ { 0 } ( T _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } ) )$ to the product$m _ { A } \in D _ { \mathrm { p o l y } } ^ { 1 } ( \mathbb { R } ^ { d } )$in the algebra$A : = C ^ { \infty } (  { \mathbb { R } } ^ { d } )$. Here$m _ { A } \colon f _ { 1 } \otimes f _ { 2 } { \longmapsto } f _ { 1 } f _ { 2 }$is considered as a bidiferential operator.

The condition from above for U to be an$L _ { \infty }$-morphism is equivalent to the following one:

$$
\begin{array}{l} \sum_ {i \neq j} \pm \big (\mathcal {U} _ {n - 1} ((\gamma_ {i} \bullet \gamma_ {j}) \wedge \gamma_ {1} \wedge \dots \wedge \gamma_ {n}) \big) (f _ {1} \otimes \dots \otimes f _ {m}) + \\ \quad + \sum_ {k, l \geqslant 0, k + l = n} \frac {1}{k ! l !} \sum_ {\sigma \in \Sigma_ {n}} \pm \\ \quad \pm \Big (\mathcal {U} _ {k} (\gamma_ {\sigma_ {1}} \wedge \dots \wedge \gamma_ {\sigma_ {k}}) \circ \mathcal {U} _ {l} (\gamma_ {\sigma_ {k + 1}} \wedge \dots \wedge \gamma_ {\sigma_ {n}}) \Big) (f _ {1} \otimes \dots \otimes f _ {m}) = 0. \end{array}
$$

Here we use all polylinear maps$\textstyle { \mathcal { U } } _ { n }$including the case$n = 0 ,$and definitions of brackets in$D _ { \mathrm { p o l y } }$and$T _ { \mathrm { p o l y } }$via operations  (see Section 3.4.2) and  (see Section $4 . 6 . 1 )$. We denote the left-hand side of the expression above by$( F )$

$\mathcal { U } + \mathcal { U } _ { 0 }$is not a pre-$. L _ { \infty }$-morphism because it maps 0 to a nonzero point$m _ { A }$. Still the equation$( F ) = 0$makes sense and means that the map$( \mathcal { U } + \mathcal { U } _ { 0 } )$from formal$Q \cdot$ manifold$T _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } ) [ 1 ] ) _ { \mathrm { f o r m a l } }$to the formal neighborhood of point$m _ { A }$in the graded vector space$D _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } ) [ 1 ] \operatorname { i s } Q$-equivariant, where the odd vector field Q on the target is purely quadratic and comes from the bracket on$D _ { \mathrm { p o l y } } ( \mathbb { R } ^ { d } )$, forgetting the diferential.

Also, the term$\boldsymbol { \mathcal { U } } _ { 0 }$comes from the unique graph$\Gamma _ { 0 }$which was missing in the definition of U. Namely,$\Gamma _ { 0 }$has$n = 0$vertices of the first type,$m = 2$vertices of the second type, and no edges at all. It is easy to see that$W _ { \Gamma _ { 0 } } = 1$and$\mathcal { U } _ { \Gamma _ { 0 } } = \mathcal { U } _ { 0 }$

We consider the expression ðFÞ simultaneously for all possible dimensions d. It is clear that one can write ðFÞ as a linear combination

$$
\sum_ {\Gamma} c _ {\Gamma} \cdot \mathcal {U} _ {\Gamma} (\gamma_ {1} \otimes \dots \otimes \gamma_ {n}) (f _ {1} \otimes \dots \otimes f _ {m})
$$

of expressions$\mathcal { U } _ { \Gamma }$for admissible graphs C with n vertices of the first type, m vertices of the second type, and$2 n + m - 3$edges where$n \geqslant 0 , m \geqslant 0 , 2 n + m - 3 \geqslant 0$. We assume that$c _ { \Gamma } = \pm c _ { \Gamma ^ { \prime } }$if graph$\Gamma ^ { \prime }$is obtained from C by a renumeration of vertices of the first type and by a relabeling of edges in sets$\mathrm { S t a r } ( \nu )$(see Section 6.5 where we discuss signs).

Coeficients$c _ { \Gamma }$of this linear combination are equal to certain sums with signs of weights$\mathcal { W } _ { \Gamma ^ { \prime } }$0 associated with some other graphs$\Gamma ^ { \prime } ,$and of products of two such weights. In particular, numbers$c _ { \Gamma }$do not depend on the dimension d in our problem. Perhaps it is better to use here the language of rigid tensor categories, but we will not do it.

We want to check that$c _ { \Gamma }$vanishes for each$\Gamma .$

The idea is to identify$c _ { \Gamma }$with the integral over the boundary$\partial \overline { { C } } _ { n , m }$of the closed diferential form constructed from C as in Section 6.2, with the only diference that now we consider graphs with$2 n + m - 3$edges. The Stokes formula gives the vanishing:

$$
\int_ {\partial \overline {{C}} _ {n, m}} \wedge_ {e \in E _ {\Gamma}} \mathrm{d} \phi_ {e} = \int_ {\overline {{C}} _ {n, m}} \mathrm{d} (\wedge_ {e \in E _ {\Gamma}} \mathrm{d} \phi_ {e}) = 0.
$$

We are going to calculate integrals of the form$\land _ { e \in E _ { \Gamma } } \mathrm { d } \phi _ { \epsilon }$restricted to all possible boundary strata of$\partial \overline { { C } } _ { n , m } .$, and prove that the total integral as above is equal to$c _ { \Gamma }$. In

Section 5.2.1 we have listed two groups of boundary strata, denoted by (S1) and (S2) and labeled by sets or pairs of sets. Thus,

$$
0 = \int_ {\partial \overline {{C}} _ {n, m}} \wedge_ {e \in E _ {\Gamma}} \mathrm{d} \phi_ {e} = \sum_ {S} \int_ {\partial_ {S} \overline {{C}} _ {n, m}} \wedge_ {e \in E _ {\Gamma}} \mathrm{d} \phi_ {e} + \sum_ {S, S ^ {\prime}} \int_ {\partial_ {S, S ^ {\prime}} \overline {{C}} _ {n, m}} \wedge_ {e \in E _ {\Gamma}} \mathrm{d} \phi_ {e}.
$$

## 6.4.1. Case (S1)

Points$p _ { i } \in \mathcal { H }$for i from subset$S \subset \{ 1 , \ldots , n \}$where$\# S \geqslant 2 ,$, move close to each other. The integral over the stratum$\partial _ { S } \overline { { C } } _ { n , m }$is equal to the product of an integral over $C _ { n _ { 1 } , m }$with an integral over$C _ { n _ { 2 } }$where$n _ { 2 } : = \# S , n _ { 1 } : = n - n _ { 2 } + 1$. The integral vanishes by dimensional reasons unless the number of edges of C connecting vertices from S is equal to$2 n _ { 2 } - 3$

There are several possibilities:

6.4.1.1. First subcase of$( S I ) \colon n _ { 2 } = 2 ( \mathrm { F i g u r e } 8 )$. In this subcase, two vertices from$S _ { 1 }$ are connected exactly by one edge, which we denote by$e .$The integral over$C _ { 2 }$here gives number$\pm 1$(after division by 2p coming from the formula for weights$W _ { \Gamma } )$. The total integral over the boundary stratum is equal to the integral of a new graph$\Gamma _ { 1 }$ obtained from C by the contraction of edge e. It is easy to see (up to a sign) that this term corresponds to the first line in our expression ðFÞ, the one where the operation on polyvector fields appears.

6.4.1.2. Second subcase of$( S I ) \colon n _ { 2 } \geqslant 3$(Figure 9). This is the most nontrivial case. The integral corresponding to this boundary stratum vanishes because the integral of any product of$2 n _ { 2 } - 3$angle forms over$C _ { n _ { 2 } }$where$n _ { 2 } \geqslant 3$vanishes, as is proven later in Section 6.6.

## 6.4.2. Case(S2)

Points$p _ { i }$for$i \in S _ { 1 } \subset \{ 1 , \ldots , n \}$and points$q _ { j }$for$\overline { { j } } \in S _ { 2 } \subset \{ \overline { { 1 } } , \dots , \overline { { m } } \}$move close to each other and to the horizontal line R. The condition is that$2 n _ { 2 } + m _ { 2 } - 2 \geqslant 0$and $n _ { 2 } + m _ { 2 } \leqslant n + m - 1$, where$n _ { 2 } : = \# S _ { 1 } , m _ { 2 } : = \# S _ { 2 }$. The corresponding stratum is isomorphic to$C _ { n _ { 1 } , m _ { 1 } } \times C _ { n _ { 2 } , m _ { 2 } }$where$n _ { 1 } : = n - n _ { 2 } , m _ { 1 } = m - m _ { 2 } + 1$. The integral of this stratum decomposes into the product of two integrals. It vanishes if the number of edges of C connecting vertices from$S _ { 1 } \sqcup S _ { 2 }$is not equal to$2 n _ { 2 } + m _ { 2 } - 2$

![](images/page_34_image_9.jpg)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Figure 8. Term corresponding to the operation .</span></small>

![](images/page_35_image_0.jpg)

Figure 9. Many points collapse together inside$\mathcal { H }$

![](images/page_35_image_2.jpg)

Figure 10. Many points collapse on R, no bad edges.

6.4.2.1. First subcase of (S2): no bad edges (Figure 10). In this subcase we assume that there is no edge$( i , j )$in C such that$i \in S _ { 1 } , j \in \{ 1 , \dots , n \} \backslash S _ { 1 }$

The integral over the boundary stratum is equal to the product$W _ { \Gamma _ { 1 } } \times W _ { \Gamma _ { 2 } }$where $\Gamma _ { 2 }$is the restriction of C to the subset$S _ { 1 } \sqcup S _ { 2 } \subset \{ 1 , \ldots , n \} \sqcup \{ \overline { { 1 } } , \ldots , \overline { { m } } \} = V _ { \Gamma }$, and $\Gamma _ { 1 }$is obtained by the contraction of all vertices in this set to a new vertex of the second type. Our condition guarantees that$\Gamma _ { 1 }$is an admissible graph. This corresponds to the second line in ðFÞ, where the product  on polydiferential operators appears.

6.4.2.2. Second subcase of(S2): there is a bad edge (Figure 11). Now we assume that there is an edge$( i , j )$in C such that$i \in S _ { 1 } , j \in \{ 1 , \dots , n \} \backslash S _ { 1 }$. In this case, the integral is zero because of the condition$\mathrm { d } \phi ( x , y ) = 0$if x stays on the line R.

The reader can wonder about what happens if, after the collapsing, the graph will have multiple edges. Such terms do not appear in ðFÞ. Nevertheless, we ignore them because in this case the diferential form which we integrate vanishes as it contains as a factor the square of a 1-form.

Thus, we see that we have exhausted all possibilities and get contributions of all terms in the formula ðFÞ. We just proved that$c _ { \Gamma } = 0$for any C, and that U is an$L _ { \infty } .$ morphism.

![](images/page_36_image_0.jpg)

Figure 11. Many points collapse on R, with a bad edge.

![](images/page_36_image_2.jpg)

Figure 12. A tree with one vertex in${ \mathcal { H } } .$

## 6.4.3. We Finish the Proof of Theorem 6.3

In order to check that U it is a quasi-isomorphism, we should show that its component$\mathcal { U } _ { 1 }$coincides with$\mathcal { U } _ { 1 } ^ { ( 0 ) }$introduced in Section 4.6.1.1. It follows from definitions that every admissible graph with$n = 1$vertex of the first type and$m \geqslant 0$ vertices of the second type, and with m edges, is the tree in Figure 12.

The integral corresponding to this graph is$( 2 \pi ) ^ { m } / m !$. The map$\widetilde { U } _ { \Gamma }$from polyvector fields to polydiferential operators is the one which appears in Section 4.6.1.1:

$$
\xi_ {1} \wedge \dots \wedge \xi_ {m} \rightarrow \frac {1}{m !} \sum_ {\sigma \in \Sigma_ {m}} \operatorname{sgn} (\sigma) \cdot \xi_ {\sigma_ {1}} \otimes \dots \otimes \xi_ {\sigma_ {m}}, \quad \xi_ {i} \in \Gamma (\mathbb {R} ^ {d}, T).
$$

Theorem 6.3 is proven.

## 6.4.4. Comparison with the Formula from Section 2

The weight w defined in Section 2 difer from$W _ { \Gamma }$defined in Section 6.2 by the factor$2 ^ { n } / n !$. On the other hand, the bidiferential operator$B _ { \Gamma , \alpha } ( f , g )$is 2<sup>n</sup> times $\mathcal { U } _ { \Gamma } ( \alpha \wedge \dots \wedge \alpha ) ( f \otimes g )$. The inverse factorial$1 / n !$appears in the Taylor series (see the end of Section 4.3). Thus, we obtain the formula from Section 2.

## <sup>6</sup>.<sup>5</sup>. GRADING, ORIENTATIONS, FACTORIALS, SIGNS

Taylor coeficients of$\mathcal { U } + \mathcal { U } _ { 0 }$are maps of graded spaces

$$
\operatorname{Sym} ^ {n} \left(\left(\bigoplus_ {k \geqslant 0} \Gamma \left(\mathbb {R} ^ {d}, \wedge^ {k} T\right) [ - k ]\right) [ 2 ]\right)\rightarrow \left(\underline {{\operatorname{Hom}}} (A [ 1 ] ^ {\otimes m}, A [ 1 ])\right) [ 1 ],
$$

where Hom denotes the internal Hom in the tensor category Graded<sup>k</sup>. We denote the expression from above by ðEÞ. First of all, in the expression ðEÞ each polyvector field $\gamma _ { i } \in \Gamma ( \mathbb { R } ^ { d } , \wedge ^ { k _ { i } } T )$appears with the shift$2 - k _ { i }$. In our formula for U the same$\gamma _ { i }$gives$k _ { i }$ edges of the graph, and thus$k _ { i }$1-forms which we have to integrate. Also, it gives two dimensions for the integration domain$\overline { { C } } _ { n , m } .$. Secondly, every function$f _ { j } \in A$appears with shift 1 in$( E )$and gives 1 dimension to the integration domain. We are left with two shifts by 1 in ðEÞ which are accounted for two dimensions of the group$G ^ { ( 1 ) }$. From this it is clear that our formula for U is compatible with$\mathbb { Z } \mathrm { - g r a d i n g }$

Moreover, it is also clear that things responsible for various signs in our formulas:

(1) the orientation of$\overline { { C } } _ { n , m }$

(2) the order in which we multiply 1-forms$\mathrm { d } \phi _ { e }$

(3) Z-gradings of vector spaces in ðEÞ,

are naturally decomposed into pairs. This implies that the enumeration of the set of vertices of C, and also the enumeration of edges in sets$\mathrm { S t a r } ( \nu )$for vertices v of the first type are not really used. Thus, we see that$\textstyle { \mathcal { U } } _ { n }$is skew-symmetric.

Inverse factorials$1 / ( \# \mathbf { S } \mathrm { t a r } ( \nu ) ! )$kill the summation over enumerations of sets $\mathrm { S t a r } ( \nu )$. The inverse factorial$1 / n !$in the final formula does not appear because we consider higher derivatives which are already multiplied by n!.

The last thing to check is that in our derivation of the fact that U is an$L _ { \infty } -$ morphism using the Stokes formula, we did not loose a sign anywhere. This is a bit hard to explain. How, for example, can one compare the standard orientation on C with shifts by 2 in ðEÞ? As a hint to the reader, we would like to mention that it is very convenient to ‘place’ the resulting expression

$$
\Phi := (\mathcal {U} _ {\Gamma} (\gamma_ {1} \otimes \dots \otimes \gamma_ {n})) (f _ {1} \otimes \dots \otimes f _ {m})
$$

at the point 1 on the absolute.

## 6.6. VANISHING OF INTEGRALS OVER$C _ { n } , n \geqslant 3$

In this subsection we consider the space$C _ { n }$of$G ^ { ( 2 ) }$- equivalence classes of configurations of points on the Euclidean plane. Every two indices$i , j , i \neq j , 1 \leqslant i , j \leqslant n$give a forgetting map$C _ { n } \longrightarrow C _ { 2 } \simeq S ^ { 1 }$. We denote by$\mathrm { d } \phi _ { i , j }$the closed 1-form on$C _ { n }$which is the pullback of the standard 1-form$\mathrm { d } ( a n g l e )$on the circle. We use the same notation for the pullback of this form to Conf<sub>n</sub>.

LEMMA 6.4. Let nP3 be an integer. The integral over$C _ { n }$of the product of any $2 n - 3 = \dim ( C _ { n } )$closed 1-forms$\mathrm { d } \phi _ { i _ { \tau , i \tau } } , \alpha = 1 , \ldots , 2 n - 3$, is equal to zero.

Proof. First of all, we identify$C _ { n }$with the subset$C _ { n } ^ { \prime }$of$\operatorname { C o n f } _ { n }$consisting of configurations such that the point$p _ { i _ { 1 } }$is$0 \in \mathbb { C }$and$p _ { j _ { 1 } }$is on the unit circle$S ^ { 1 } \subset \mathbb { C }$. Also, we rewrite the form which we integrate as

$$
\bigwedge_ {\alpha = 1} ^ {2 n - 3} \mathrm{d} \phi_ {i _ {\alpha}, j _ {\alpha}} = \mathrm{d} \phi_ {i _ {1, j _ {1}}} \wedge \bigwedge_ {\alpha = 2} ^ {2 n - 3} \mathrm{d} (\phi_ {i _ {\alpha}, j _ {\alpha}} - \phi_ {i _ {1}, j _ {1}}).
$$

Let us map the space$C _ { n } ^ { \prime }$onto the space$C _ { n } ^ { \prime \prime } \subset \mathbf { C o n f } _ { n }$consisting ofconfigurations with $p _ { i _ { 1 } } = 0$and$p _ { j _ { 1 } } = 1$, applying rotations with the center at 0. Diferential forms $\mathsf { d } ( \phi _ { i _ { \alpha } , j _ { \alpha } } - \phi _ { i _ { 1 } , j _ { 1 } } )$on$C _ { n } ^ { \prime }$are pullbacks of diferential forms$\mathrm { d } \phi _ { i _ { \alpha } , j _ { \alpha } }$on$C _ { n } ^ { \prime \prime } .$The integral of a product of$? n - 3$closed 1-forms$\mathrm { d } \phi _ { i _ { x } , j _ { x } } , \alpha = 1 , \ldots , 2 n - 3$over$C _ { n } ^ { \prime }$is equal to 2p times the integral of the product$2 n - 4$closed 1-forms$\mathrm { d } \phi _ { i _ { \alpha } , j _ { \alpha } } , \alpha = 2 , \ldots , 2 n - 3$over$C _ { n } ^ { \prime \prime }$

The space$C _ { n } ^ { \prime \prime }$is a complex manifold. We are calculating an absolutely converging integral of the type

$$
\int_ {C _ {n} ^ {\prime \prime}} \prod_ {\alpha} \mathrm{d} \operatorname{Arg} (Z _ {\alpha}),
$$

where$Z _ { \alpha }$are holomorphic invertible functions on$C _ { n } ^ { \prime \prime }$(diferences between complex coordinates of points of the configuration). We claim that it is zero because of the general result proven in Section 6.6.1.(

## 6.6.1. A Trick Using Logarithms

THEOREM 6.5. Let X be a complex algebraic variety of dimension$N { \geqslant } 1$and $Z _ { 1 } , \dots , Z _ { 2 N }$be rational functions on$X ,$not equal identically to zero. Let U be any Zariski open subset of X such that functions$Z _ { \alpha }$are defined and nonvanishing on$U ,$, and U consists of smooth points. Then the integral

$$
\int_ {U (\mathbb {C})} \wedge_ {\alpha = 1} ^ {2 N} \mathrm{d} (\operatorname{Arg} Z _ {\alpha})
$$

is absolutely convergent, and equal to zero.

This result seems to be new, although the main trick used in the proof is well known. Goncharov told me that he also came to the same result in his study of mixed Tate motives.

Proof. First of all, we claim that the diferential form$\Lambda _ { \alpha = 1 } ^ { 2 N } \mathrm { d } \mathrm { A r g } ( Z _ { \alpha } )$on$U ( \mathbb { C } )$ coincides with the form$\Lambda _ { \alpha = 1 } ^ { 2 N } \mathrm { d } \log | Z _ { \alpha } |$(this is the trick).

We can replace d$\mathrm { A r g } ( Z _ { \alpha } )$by the linear combination of a holomorphic and an anti-holomorphic form

$$
\frac {1}{2 i} \big (\mathrm{d} (\mathrm{Log} Z _ {\alpha}) - \mathrm{d} (\mathrm{Log} \overline {{Z}} _ {\alpha}) \big).
$$

Thus, the form which we integrate over$U ( \mathbb { C } )$is a sum of products of holomorphic and of anti-holomorphic forms. The summand corresponding to a product of a nonequal number of holomorphic and of anti-holomorphic forms, vanishes identically because$U ( \mathbb { C } )$is a complex manifold. The conclusion is that the number of anti-holomorphic factors in nonvanishing summands is the same for all of them, it coincides with the complex dimension$N$of$U ( \mathbb { C } )$. The same products of holomorphic and of anti-holomorphic forms survive in the product

$$
\bigwedge_ {\alpha = 1} ^ {2 N} \mathrm{d} \operatorname{Log} | Z _ {\alpha} | = \bigwedge_ {\alpha = 1} ^ {2 N} \frac {1}{2} \left(\mathrm{d} (\operatorname{Log} Z _ {\alpha}) + \mathrm{d} (\operatorname{Log} \overline {{Z}} _ {\alpha})\right).
$$

Let us choose a compactification$\overline { { U } }$of$U$such that${ \overline { { U } } } \backslash U$is a divisor with normal crossings.$\operatorname { I f } \phi$is a smooth diferential form on$U ( \mathbb { C } )$such that coeficients of$\phi$are locally integrable on${ \overline { { U } } } ( \mathbb { C } )$, then we denote by${ \mathcal { I } } ( \phi )$corresponding diferential form on${ \overline { { U } } } ( \mathbb { C } )$with coeficients in the space of distributions.

LEMMA 6.6. Let x be a form on$U ( \mathbb { C } )$which is a linear combination ofproducts of functions$\mathrm { L o g } | Z _ { \alpha } |$and of 1-forms d Log$Z _ { \alpha } |$where$Z _ { \alpha } \in { \mathcal { O } } ^ { \times } ( U )$are regular invertible functions on$U .$Then coeficients of x and of dx are locally L<sup>1</sup> functions on${ \overline { { U } } } ( \mathbb { C } )$ Moreover,${ \mathcal { I } } ( \mathrm { d } \omega ) = \mathrm { d } ( { \mathcal { I } } ( \omega ) )$. Also, the integral$\int _ { U ( \mathbb { C } ) }$x is absolutely convergent and equal to the integra$\textstyle \int _ { \overline { { U } } ( \mathbb { C } ) } { \mathcal { I } } ( \omega )$

The lemma is an elementary exercise in the theory of distributions, after passing to local coordinates on${ \overline { { U } } } ( \mathbb { C } )$. We leave details of the proof to the reader. Also, the statement of the lemma remains true without the condition that${ \overline { { U } } } \backslash U$is a divisor with normal crossings.(

The vanishing of the integral in the theorem is clear now by the Stokes formula:

$$
\begin{array}{l} \int_ {U (\mathbb {C})} \bigwedge_ {\alpha = 1} ^ {2 N} \mathrm{d} \operatorname{Arg} (Z _ {\alpha}) = \int_ {U (\mathbb {C})} \bigwedge_ {\alpha = 1} ^ {2 N} \mathrm{d} \operatorname{Log} | Z _ {\alpha} | = \int_ {\overline {{U}} (\mathbb {C})} \mathscr {I} \left(\mathrm{d} \left(\operatorname{Log} | Z _ {1} | \bigwedge_ {\alpha = 2} ^ {2 N} \mathrm{d} \operatorname{Log} | Z _ {\alpha} |\right)\right) \\ = \int_ {\overline {{U}} (\mathbb {C})} \mathrm{d} \left(\mathscr {I} \left(\operatorname{Log} | Z _ {1} | \bigwedge_ {\alpha = 2} ^ {2 N} \mathrm{d} \operatorname{Log} | Z _ {\alpha} |\right)\right) = 0. \end{array}
$$

In fact, the convergence and the vanishing of the integral$\begin{array} { r } { \int _ { U ( \mathbb { C } ) } \wedge _ { \alpha = 1 } ^ { 2 N } \mathrm { d } \operatorname { L o g } | Z _ { \alpha } | } \end{array}$is a purely geometric fact. Namely, the image of$U ( \mathbb { C } )$in$\mathbb { R } ^ { 2 N }$under the map $x \mapsto ( \mathrm { L o g } | Z _ { 1 } ( x ) | , \dots , \mathrm { L o g } | Z _ { 2 N } ( x ) | )$has finite volume and every noncritical point in this image appears zero times, when points in the pre-image are counted with signs arising from the comparison of canonical orientations on$U ( \mathbb { C } )$and$\mathbb { R } ^ { 2 N }$

## 6.6.2. Remark

The vanishing of the integral in Lemma 6.4. has a higher-dimensional analogue which is crucial in the perturbative Chern–Simons theory in the dimension 3, and its generalizations to dimensions P4 (see [30]). However, the vanishing of integrals in dimensions${ \geqslant } 3$follows from a much simpler fact which is the existence of a geometric involution making the integral to be equal to minus itself. In the present paper, we will use several times similar arguments involving involutions.

## 7. Formality Conjecture for General Manifolds

In this section we establish the formality conjecture for general manifolds and not only for open domains in$\mathbb { R } ^ { d }$. It turns out that that essentially all the work has been done already. The only new analytic result is vanishing of certain integrals over configuration spaces, analogous to Lemma 6.4.

One can treat$\mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } ,$the formal completion of vector space$\mathbb { R } ^ { d }$at zero, in many respects as a usual manifold. In particular, we can define diferential graded Lie algebras$D _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$and$T _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$. The Lie algebra$W _ { d } : = \mathrm { V e c t } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$is the standard Lie algebra offormal vector fields. We consider$W _ { d }$as a diferential graded Lie algebra (with the trivial grading and the diferential equal to 0). There are natural homomorphisms of diferential graded Lie algebras:

$$
m _ {T} \colon W _ {d} \to T _ {\mathrm{poly}} (\mathbb {R} _ {\mathrm{formal}} ^ {d}), m _ {D} \colon W _ {d} \to D _ {\mathrm{poly}} (\mathbb {R} _ {\mathrm{formal}} ^ {d}),
$$

because vector fields can be considered as polyvector fields and as diferential operators.

We will use the following properties of the quasi-isomorphism U from Section$6 . 4 \colon$

(P1)$\boldsymbol { \mathcal U }$can be defined for$\mathbb { R } _ { \mathrm { f o r m a l } } ^ { d }$as well,

(P2) for any$\xi \in W _ { d }$we have the equality

$$
\mathcal {U} _ {1} (m _ {T} (\xi)) = m _ {D} (\mathcal {U} _ {1} (\xi)),
$$

(P3) U is GLðd; RÞ-equivariant,

(P4) for any$k \geqslant 2 , \xi _ { 1 } , \ldots , \xi _ { k } \in W _ { d }$we have the equality

$$
\mathcal {U} _ {k} \left(m _ {T} \left(\xi_ {1}\right) \otimes \dots \otimes m _ {T} \left(\xi_ {k}\right)\right) = 0,
$$

(P5) for$\mathrm { a n y } k \geqslant 2 , \xi \in g l ( d , \mathbb { R } ) \subset W _ { d } ,$, and for any$\eta _ { 2 } , \dots , \eta _ { k } \in T _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$we have $\begin{array} { r } { \mathcal { U } _ { k } ( m _ { T } ( \xi ) \otimes \eta _ { 2 } \otimes \cdots \otimes \eta _ { k } ) = 0 . } \end{array}$

We will construct quasi-isomorphisms from$T _ { \mathrm { p o l y } } ( X )$to$D _ { \mathrm { p o l y } } ( X )$for arbitrary ddimensional manifold X using only properties$( \mathrm { P l } ) \mathrm { - } ( \mathrm { P } 5 )$of the map U. Properties (P1), (P2) and (P3) are evident, and the properties (P4), (P5) will be established later in Sections 7.3.1.1 and 7.3.3.1.

It will be convenient to use in this section the geometric language of formal graded manifolds instead of the algebraic language of$L _ { \infty } { \mathrm { - a l g e b r a s } }$. Let us fix the dimension $d \in \mathbb { N }$. We introduce three formal graded Q-manifolds without base points: $\mathcal { T } , \mathcal { D } , \mathcal { W }$: These formal graded Q-manifolds are obtained in the usual way from diferential graded Lie algebras$T _ { \mathrm { p o l y } } ( R _ { \mathrm { f o r m a l } } ^ { d } ) , D _ { \mathrm { p o l y } } ( R _ { \mathrm { f o r m a l } } ^ { d } )$and$W _ { d }$forgetting base points.

In Sections 7.1 and 7.2, we present two general geometric constructions which will used in Section 7.3 for the proof of formality of$D _ { \mathrm { p o l y } } ( X )$

## 7.1. FORMAL GEOMETRY (IN THE SENSE OF GELFAND AND KAZHDAN)

Let X be a smooth manifold of dimension d. We associate with X two infinitedimensional manifolds,$X ^ { \mathrm { c o o r } }$and$X ^ { \mathrm { a f f } }$. The manifold$X ^ { \mathrm { c o o r } }$consists of pairs$( x , f )$ where x is a point of X and f is an infinite germ of a coordinate system on X at$x ,$

$$
f \colon (\mathbb {R} _ {\text { formal }} ^ {d}, 0) \hookrightarrow (X, x).
$$

We consider$X ^ { \mathrm { c o o r } }$as a projective limit of finite-dimensional manifolds (spaces of finite germs of coordinate systems). There is an action on$X ^ { \mathrm { c o o r } }$of the (pro-Lie) group $G _ { d }$of formal difeomorphisms of$\mathbb { R } ^ { d }$preserving base point 0. The natural projection map$X ^ { \mathrm { c o o r } }  X$is a principal$G _ { d } .$-bundle.

The manifold$X ^ { \mathrm { a f f } }$is defined as the quotient space$X ^ { \mathrm { c o o r } } / G L ( d , \mathbb { R } )$. It can be thought of as the space of formal afine structures at points of X. The main reason to introduce$X ^ { \mathrm { a f f } }$is that fibers of the natural projection map$X ^ { \mathrm { a f f } }  X$are contractible.

The Lie algebra of the group$G _ { d }$is a subalgebra of codimension d in$W _ { d } .$. It consists of formal vector fields vanishing at zero. Thus,$\operatorname { L i e } ( G _ { d } )$acts on$X ^ { \mathrm { c o o r } }$. It is easy to see that in fact the whole Lie algebra$W _ { d }$acts on$X ^ { \mathrm { c o o r } }$and is isomorphic to the tangent space to$X ^ { \mathrm { c o o r } }$at each point. Formally, the infinite-dimensional manifold$X ^ { \mathrm { c o o r } }$looks as a principal homogeneous space of the nonexistent group with the Lie algebra$W _ { d } .$

The main idea of formal geometry (see [18]) is to replace d-dimensional manifolds by ‘principal homogeneous spaces’ of$W _ { d } .$Diferential-geometric constructions on $X ^ { \mathrm { c o o r } }$can be obtained from Lie-algebraic constructions for$W _ { d } .$. For a while we will work only with$X ^ { \mathrm { c o o r } }$, and then at the end return to$X ^ { \mathrm { a f f } }$. In terms of Lie algebras, it corresponds to the diference between absolute and relative cohomology.

## 7.2. FLAT CONNECTIONS AND Q-EQUIVARIANT MAPS

Let M be a$C ^ { \infty }$-manifold (or a complex analytic manifold, or an algebraic manifold, or a projective limit of manifolds, etc.). Denote by PTM the supermanifold which is the total space of the tangent bundle of M endowed with the reversed parity. Functions on the PTM are diferential forms on M. The de Rham diferential${ \mathrm { d } } _ { M }$on forms can be considered as an odd vector field on PTM with the square equal to 0. Thus, PTM is a Q-manifold. It seems that the accurate notation for PTM considered as a graded manifold should be$T [ 1 ] M$(the total space of the graded vector bundle$T _ { M } [ 1 ]$considered as a graded manifold).

Let$N \to M$be a bundle over a manifold M whose fibers are manifolds, or vector spaces, etc., endowed with a flat connection r. Denote by E the pullback of this bundle to$B : = \Pi T M$. The connection r gives a lift of the vector field$Q _ { B } : = \mathrm { d } _ { M }$on B to the vector field$Q _ { E }$on E. This can be done for arbitrary connection, and only for flat connection the identity$[ Q _ { E } , Q _ { E } ] = 0$holds.

A generalization of a (nonlinear) bundle with a flat connection is a Q-equivariant bundle whose total space and the base are Q-manifolds. In the case of graded vector bundles over$T [ 1 ] M$this notion was introduced Quillen under the name of a superconnection (see [41]). A generalization of the notion of a covariantly flat morphism from one bundle to another is the notion of a Q-equivariant map.

DEFINITION 7.1. A flat family over Q-manifold B is a pair$\left( p \colon E \to B , \sigma \right)$where $p \colon E \to B$is a Q-equivariant bundle whose fibers are formal manifolds, and a $\sigma \colon B \to E$is a Q-equivariant section of this bundle.

In the case$B = \{ p o i n t \}$a flat family over B is the same a formal Q-manifold with base point. It is clear that flat families over a given Q-manifold form a category.

We apologize for the terminology. More precise name for ‘flat families’ would be ‘flat families of pointed formal manifolds’, but it is too long.

One can define analogously flat graded families over graded Q-manifolds.

We refer the reader to a discussion of further examples of Q-manifolds in [32].

## 7.3. FLAT FAMILIES IN DEFORMATION <sub>Q</sub>UANTIZATION

Let us return to our concrete situation. We construct in this section two flat families over PTX (where X is a d-dimensional manifold), and a morphism between them. This will be done in several steps.

## 7.3.1. Flat Families over$\mathcal { W }$

The first bundle over$\mathcal { W }$is trivial as a Q-equivariant bundle,$\mathcal { T } \times \mathcal { W }  \mathcal { W }$but with a nontrivial section$\sigma { \mathcal { T } }$. This section is not the zero section, but the graph of the$Q \cdot$ equivariant map$\mathcal { W }  \mathcal { T }$coming from the homomorphism of diferential graded Lie algebras m<sub>T</sub>:$W _ { d } \to T _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$. Analogously, the second bundle is the trivial Q-equivariant bundle$\mathcal { D } \times \mathcal { W }  \mathcal { W }$with the section$\sigma _ { \mathcal { D } }$coming from the homomorphism$m _ { D } \colon W _ { d } \to D _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$

Formulas from Section 6.4 give a Q-equivariant map$\mathcal { U } : \mathcal { T }  \mathcal { D }$

LEMMA 7.2. The morphism$( \mathcal { U } \times \mathrm { i d } _ { \mathcal { W } } ) \colon \mathcal { T } \times \mathcal { W } \to \mathcal { D } \times \mathcal { W }$is a morphism of flat families over$\mathcal { W }$

Proof. We have to check that$( \mathcal { U } \times i d \mathcal { \scriptscriptstyle { W } } )$maps one section to another, i.e. that

$$
\left(\mathcal {U} \times \mathrm{id} _ {\mathcal {W}}\right) \circ \sigma_ {\mathcal {T}} = \sigma_ {D} \in \operatorname{Maps} (\mathcal {W}, \mathcal {D} \times \mathcal {W}).
$$

We compare Taylor coeficients. The linear part$\mathcal { U } _ { 1 }$of$\boldsymbol { \mathcal U }$maps a vector field (considered as a polyvector field) to itself, considered as a diferential operator (property (P2)). Components$\mathcal { U } _ { k } ( \xi _ { 1 } , \dots , \xi _ { k } )$for$k \geqslant 2 , \xi _ { i } \in T ^ { 0 } (  { \mathbb { R } } ^ { d } ) = \Gamma (  { \mathbb { R } } ^ { d } , T )$vanish, which is the property (P4).(

7.3.1.1. Proof of the property$( P 4 )$. Graphs appearing in the calculation of $\mathcal { U } _ { k } ( \xi _ { 1 } , \dots , \xi _ { k } )$have k edges, k vertices of the first type, and m vertices of the second type, where$2 k + m - 2 = k$: Thus, there are no such graphs for$k \geqslant 3$as m is nonnegative. The only interesting case is$k = 2 , m = 0$which is represented in Figure 13.

By our construction,$\textstyle { \mathcal { U } } _ { 2 }$restricted to vector fields is equal to the nontrivial quadratic map

$$
\xi \mapsto \sum_ {i, j = 1} ^ {d} \partial_ {i} (\xi^ {j}) \partial_ {j} (\xi^ {i}) \in \Gamma (\mathbb {R} ^ {d}, \mathcal {O}), \qquad \xi = \sum_ {i} \xi^ {i} \partial_ {i} \in \Gamma (\mathbb {R} ^ {d}, T)
$$

with the weight

$$
\int_ {C _ {2, 0}} \mathrm{d} \phi_ {(1 2)} \mathrm{d} \phi_ {(2 1)} = \int_ {\mathscr {H} \backslash \{z _ {0} \}} \mathrm{d} \phi (z, z _ {0}) \wedge \mathrm{d} \phi (z _ {0}, z),
$$

where$z _ { 0 }$is an arbitrary point of$\mathcal { H }$.

![](images/page_43_image_0.jpg)

Figure 13. The only graph for property (P4).

LEMMA 7.3. For arbitrary angle map the integral$\begin{array} { r } { \int _ { \mathcal { H } \backslash \{ z _ { 0 } \} } \mathrm { d } \phi ( z , z _ { 0 } ) \wedge \mathrm { d } \phi ( z _ { 0 } , z ) } \end{array}$is equal to zero.

Proof. We have a map$\overline { { { C } } } _ { 2 , 0 } { \longrightarrow } S ^ { 1 } \times S ^ { 1 } , \ [ ( x , y ) ] { \longmapsto } ( \phi ( x , y ) , \phi ( y , x ) )$Þ. We calculate the integral of the pullback of the standard volume element on two-dimensional torus. It is easy to see that the integral does not depend on the choice of map $\phi : \overline { { { C } } } _ { 2 , 0 } \longrightarrow S ^ { 1 }$. The reason is that the image of the boundary of the integration domain$\partial \overline { { C } } _ { 2 , 0 }$in$S ^ { 1 } \times S ^ { 1 }$cancels with the reflected copy of itself under the involution $\left( \phi _ { 1 } , \phi _ { 2 } \right) \mapsto \left( \phi _ { 2 } , \phi _ { 1 } \right)$of the torus$S ^ { 1 } \times S ^ { 1 }$. Let us assume that$\phi = \phi ^ { h }$and $z _ { 0 } = 0 + 1 \cdot i$. The integral vanishes because the involution$z \mapsto - { \overline { { z } } }$reverses the orientation of$\mathcal { H }$and preserves the form$\mathrm { d } \phi ( z , z _ { 0 } ) \wedge \mathrm { d } \phi ( z _ { 0 } , z )$(

## 7.3.2. Flat Families over$\Pi T ( X ^ { \mathrm { c o o r } } )$

If X is a d-dimensional manifold, then there is a natural map of Q-manifolds (the Maurer–Cartan form)$\Pi T ( X ^ { \mathrm { c o o r } } ) { \longrightarrow } { \mathcal { W } }$: It follows from following general reasons. If G is a Lie group, then it acts freely by left translations on itself, and also on PTG. The quotient Q-manifold$\Pi T G / G$is equal to Pg where$\mathbf { g } = \operatorname { L i e } ( G )$. Thus, we have a Q-equivariant map$\Pi T G { \longrightarrow } \Pi \mathbf { g }$: Analogous construction works for any principal homogeneous space over G. We apply it to$X ^ { \mathrm { c o o r } }$considered as a principal homogeneous space for a nonexistent group with the Lie algebra$\begin{array} { r } { { \bf g } = { \cal W } _ { d } , } \end{array}$

The pullbacks of flat families of formal manifolds over$\mathcal { W }$constructed in Section 7.3.1, are two flat families over$\Pi T ( X ^ { \mathrm { c o o r } } )$. As Q-equivariant bundles these families are trivial bundles

$$
\mathcal {T} \times \Pi T (X ^ {\text { coor }}) \longrightarrow \Pi T (X ^ {\text { coor }}), \mathscr {D} \times \Pi T (X ^ {\text { coor }}) \longrightarrow \Pi T (X ^ {\text { coor }}).
$$

Pullbacks of sections$\sigma { \mathcal { T } }$and$\sigma _ { \mathcal { D } }$gives sections in the bundles above. These sections we denote again by$\sigma { \mathcal { T } }$and$\sigma _ { \mathcal { D } }$. The pullback of the morphism$\mathcal { U } \times \mathrm { i d } _ { \mathcal { W } }$is also a morphism of flat families.

## 7.3.3. Flat Families over$\Pi T ( X ^ { \mathrm { a f f } } )$

Recall that$X ^ { \mathrm { a f f } }$is the quotient space of$X ^ { \mathrm { c o o r } }$by the action of$\operatorname { G L } ( d , \mathbb { R } )$. Thus, from functorial properties of operation$\Pi T \left( = \underline { { \mathbf { M a p s } } } ( \mathbb { R } ^ { 0 | 1 } , \cdot ) \right)$follows that$\Pi T ( X ^ { \mathrm { a f f } } )$is the quotient of$Q \cdot$-manifold$\Pi T ( X ^ { \mathrm { c o o r } } )$by the action of Q-group$\Pi T ( \mathrm { \bf G L } ( d , \mathbb { R } ) )$. We will construct an action of$\Pi T ( \mathrm { \bf G L } ( d , \mathbb { R } ) )$on flat families$\mathcal { T } \times \Pi T ( X ^ { \mathrm { c o o r } } )$and $\mathcal { D } \times \Pi T ( X ^ { \mathrm { c o o r } } )$over$\Pi T ( X ^ { \mathrm { c o o r } } )$. We claim that the morphism between these families is invariant under the action of$\Pi T ( G L ( d , \mathbb { R } ) )$. Flat families over$\Pi T ( X ^ { \mathrm { a f f } } )$will be defined as quotient families. The morphism between them will be the quotient morphism.

The action of$\Pi T ( \mathrm { \bf G L } ( d , \mathbb { R } ) )$on$\mathcal { T }$and on$\mathcal { W }$is defined as follows. First of all, if$G$ is a Lie group with the Lie algebra g, then PTG acts Q-equivariantly on Q-manifold Pg, via the identification$\Pi \mathbf { g } = \Pi T G / G$. Analogously, if g is a subalgebra of a larger Lie algebra$\mathbf { g } _ { 1 } ,$, and an action of$G$on${ \bf g } _ { 1 }$is given in a way compatible with the inclusion${ \bf g } { \hookrightarrow } { \bf g } _ { 1 }$, then PTG acts on$\Pi { \bf g } _ { 1 }$. We apply this construction to the case $G = \mathbf { G L } ( n , \mathbb { R } )$and$\mathbf { g } _ { 1 } = T _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$or$\mathbf { g } _ { 1 } = D _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$ One can check easily that sections$\sigma _ { \mathcal { T } }$and$\sigma _ { \mathcal { D } }$over$\Pi T ( X ^ { \mathrm { c o o r } } )$are$\Pi T ( G L ( d , \mathbb { R } ) ) \cdot$ equivariant. Thus, we get two flat families over$\Pi T ( X ^ { \mathrm { a f f } } )$

The last thing we have to check is that the morphism$\mathscr { U } \times \mathrm { i d } _ { \Pi T ( X ^ { \mathrm { c o o r } } ) }$of flat families

$$
\mathcal {T} \times \Pi T (X ^ {\text { coor }}) \longrightarrow \mathscr {D} \times \Pi T (X ^ {\text { coor }})
$$

is$\Pi T ( G L ( d , \mathbb { R } ) )$-equivariant. After the translation of the problem to the language of Lie algebras, we see that we should check that U is$G L ( d , \mathbb { R } )$-invariant (property (P3), that is clear by our construction), and that if we substitute an element of $\mathrm { g l } ( d , \mathbb { R } ) \subset W _ { d }$in${ \mathcal { U } } _ { > 2 }$, we get zero (property (P5), see Section 7.3.3.1).

CONCLUSION. We constructed two flat families over$\Pi T ( X ^ { \mathrm { a f f } } )$and a morphism between them. Fibers of these families are isomorphic to$\mathcal { T }$and to${ \mathcal { D } } .$

7.3.3.1. Property (P5). This is again reduces to the calculation of an integral. Let v be a vertex of C to which we put an element of$\mathrm { g l } ( d , \mathbb { R } )$. There is exactly one edge starting at v because we put a vector field here. If there are no edges ending at v, then the integral is zero because the domain of integration is foliated by lines along which all forms vanish. These lines are level sets of the function$\phi ( z , w )$where$w \in \mathcal { H } \sqcup$R is fixed and z is the point on$\mathcal { H }$corresponding to v (see Figure 14).

If there are at least two edges ending at v, then the corresponding polydiferential operator is equal to zero, because second derivatives of coeficients of a linear vector field vanish.

The only relevant case is when there is only one edge starting at$\nu ,$and only one edge ending there. If these two edges connect our vertex with the same vertex of$\Gamma _ { \ast }$ then the vanishing follows from Lemma 7.3. If our vertex is connected with two diferent vertices as in Figure. 15, then we apply the following two lemmas:

$$
\int_ {z \in \mathscr {H} \backslash \{z _ {1}, z _ {2} \}} \mathrm{d} \phi (z _ {1}, z) \wedge \mathrm{d} \phi (z, z _ {2})
$$

LEMMA 7.4. Let$z _ { 1 } \neq z _ { 2 } \in \mathcal { H }$be two distinct points on$\mathcal { H }$. Then the integral

vanishes.

![](images/page_45_image_0.jpg)

Figure 14. Level sets for function$\varphi ( z , w )$for fixed w (dashed lines).

![](images/page_45_image_2.jpg)

Figure 15. Two graphs for property (P5).

LEMMA 7.5. Let$z _ { 1 } \in \mathcal { H } , ~ z _ { 2 } \in$R be two points on${ \mathcal { H } } \sqcup \mathbb { R }$. Then the integral

$$
\int_ {z \in \mathscr {H} \backslash \{z _ {1}, z _ {2} \}} \mathrm{d} \phi (z _ {1}, z) \wedge \mathrm{d} \phi (z, z _ {2})
$$

vanishes.

Proof. One can prove analogously to Lemma 7.3 that the integral does not depend on the choice of an angle map, and also on points$z _ { 1 } , \ z _ { 2 }$. In the case of$\phi = \phi ^ { \mathrm { h } }$and both points$z _ { 1 } , z _ { 2 }$are pure imaginary, the vanishing follows from the anti-symmetry of the integral under the involution$z { \mapsto } - { \overline { { z } } }$(

## 7.3.4. Flat Families over X

Let us choose a section$s ^ { \mathrm { a f f } }$of the bundle$X ^ { \mathrm { a f f } } { \longrightarrow } X .$Such section always exists because fibers of this bundle are contractible. For example, any torsion-free connection r on the tangent bundle to X gives a section$X { \longrightarrow } X ^ { \mathrm { a f f } }$. Namely, the exponential map for r gives an identification of a neighborhood of each point$x \in X$with a neighborhood of zero in the vector space$T _ { x } X ,$, i.e. an afine structure on$X$near$x ,$ and a point of$X ^ { \mathrm { a f f } }$over$x \in X .$

The section$s ^ { \mathrm { a f f } }$defines a map of formal graded Q-manifolds$\Pi T X { \longrightarrow } \Pi T ( X ^ { \mathrm { a f f } } )$. After taking the pullback we get two flat families$\mathcal { T } _ { s ^ { \mathrm { a f f } } }$and$\mathcal { D } _ { s ^ { \mathrm { a f f } } }$over PTX and an morphism$m _ { s ^ { \mathrm { a f f } } }$from one to another.

We claim that these two flat families admit definitions independent of$s ^ { \mathrm { a f f } }$. Only the morphism$m _ { s ^ { \mathrm { a f f } } }$depends on$s ^ { \mathrm { a f f } }$

Namely, let us consider infinite-dimensional bundles of diferential graded Lie algebras$\mathrm { j e t s } _ { \infty } T _ { \mathrm { p o l y } }$and$\mathrm { j e t s } _ { \infty } D _ { \mathrm { p o l y } }$over X whose fibers at$x \in X$are spaces of infinite jets of polyvector fields or polydiferential operators at x respectively. These two bundles carry natural flat connections (in the usual sense, not as in Section 7.2) as any bundle of infinite jets. Thus, we have two flat families (in generalized sense) over PTX.

LEMMA 7.6. Flat families$\mathcal { T } _ { s ^ { \mathrm { a f f } } }$and$\mathcal { D } _ { s ^ { \mathrm { a f f } } }$are canonically isomorphic to flat families described just above.

Proof. It follows from definitions that pullbacks of bundles$\mathrm { j e t s } _ { \infty } T _ { \mathrm { p o l y } }$and jet$\mathsf { s } _ { \infty } D _ { \mathrm { p o l y } }$from X to$X ^ { \mathrm { c o o r } }$are canonically trivialized. The Maurer–Cartan 1-forms on$X ^ { \mathrm { c o o r } }$with values in graded Lie algebras$T _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$or$D _ { \mathrm { p o l y } } ( \mathbb { R } _ { \mathrm { f o r m a l } } ^ { d } )$come from pullbacks of flat connections on bundles of infinite jets. Thus, we identified our flat families over$\Pi T ( X ^ { \mathrm { c o o r } } )$with pullbacks. The same is true for$X ^ { \mathrm { a f f } }$(

## 7.3.5. Passing to Global Sections

If in general$( p \colon E { \longrightarrow } B , \sigma )$is a flat family, then one can make a new formal pointed Q-manifold:

$$
\left(\Gamma (E \longrightarrow B) _ {\text { formal }}, \sigma\right)
$$

This is an infinite-dimensional formal super manifold, the formal completion of the space of sections of the bundle$E { \longrightarrow } B$at the point r. The structure of Q-manifold on $\Gamma ( E { \longrightarrow } B )$is evident because the Lie supergroup$\mathbb { R } ^ { 0 | 1 }$acts on$E { \longrightarrow } B ,$

LEMMA 7.7. Formally completed spaces of global sections offlat families$\mathcal { T } _ { s ^ { \mathrm { a f f } } }$and $\mathcal { D } _ { s ^ { \mathrm { a f f } } }$a naturally quasi-isomorphic to$T _ { \mathrm { p o l y } } ( X )$and$D _ { \mathrm { p o l y } } ( X )$; respectively.

Proof. It is well known that if$E { \longrightarrow } X$is a vector bundle then de Rham cohomology of X with coeficients in formally flat infinite-dimensional bundle$\mathrm { j e t s } _ { \infty } E$are concentrated in degree 0 and canonically isomorphic to the vector space$\Gamma ( X , E )$ Moreover, the natural homomorphism of complexes

ðCðX; EÞ½0; differential$= 0 ) { \longrightarrow } ( \Omega ^ { * } ( X , \mathrm { j e t s } _ { \infty } ( E ) )$; de Rham differential is quasi-isomorphism.

Using this fact, the lemma from the previous subsection, and appropriate filtrations (for spectral sequences) one sees that that the natural Q-equivariant map from the formal Q-manifold$( T _ { \mathrm { p o l y } } ( X ) _ { \mathrm { f o r m a l } } [ 1 ] , 0 )$to$( \Gamma ( \mathcal { T } _ { s ^ { \mathrm { a f f } } } \longrightarrow T [ 1 ] X ) _ { \mathrm { f o r m a l } } , \sigma _ { \mathcal { T } } )$(and analogous map for$D _ { \mathrm { p o l y } } )$is a quasi-isomorphism.(

It follows from the lemma above and the result of Section 4.6.1.1 that we have a chain of quasi-isomorphisms

$$
\begin{array}{c} T _ {\text { poly }} (X) [ 1 ] _ {\text { formal }} \longrightarrow \Gamma (\mathcal {T} _ {s ^ {\text { aff}}} \longrightarrow T [ 1 ] X) _ {\text { formal }} \longrightarrow \\ \longrightarrow \Gamma (\mathcal {D} _ {s ^ {\text { aff}}} \longrightarrow T [ 1 ] X) _ {\text { formal }} \longleftarrow T _ {\text { poly }} (X) [ 1 ] _ {\text { formal}}. \end{array}
$$

Thus, diferential graded Lie algebras$T _ { \mathrm { p o l y } } ( X )$and$D _ { \mathrm { p o l y } } ( X )$are quasi-isomorphic. The Main Theorem stated in Section 4.6.2. is proven.(

The space of sections of the bundle$X ^ { \mathrm { a f f } } { \longrightarrow } X$is contractible. From this fact one can conclude that the quasi-isomorphism constructed above is well-defined homotopically.

## 8. Cup Products

## 8.1. CUP PRODUCTS ON TANGENT COHOMOLOGY

The diferential graded Lie algebras$T _ { \mathrm { p o l y } } , \ D _ { \mathrm { p o l y } }$and (more generally) shifted by ½1 Hochschild complexes of arbitrary associative algebras, all carry an additional structure. We do not know at the moment a definition, it should be something close to so called homotopy Gerstenhaber algebras (see [19, 20]), although definitely not precisely this. At least, a visible part of this structure is a commutative associative product of degree$+ 2$on cohomology of the tangent space to any solution of the Maurer–Cartan equation. Namely, if g is one of differential graded Lie algebras listed above and$\boldsymbol { \gamma } \in \left( \mathbf { g } \otimes \mathbf { m } \right) ^ { 1 }$satisfies$\begin{array} { r } { \mathrm { d } \gamma + \frac { 1 } { 2 } [ \gamma , \gamma ] = 0 } \end{array}$ where m is a finite-dimensional nilpotent nonunital diferential graded commutative associative algebra, the tangent space$T _ { \gamma }$is defined as complex$\mathbf { g } \otimes \mathbf { m } [ 1 ]$ endowed with the diferential$\mathrm { d } + [ \gamma , \cdot ] .$. Cohomology space$H _ { \gamma }$of this diferential is a graded module over graded algebra$H ( \mathbf { m } )$(the cohomology space of m as a complex).$\mathrm { ~ I f ~ } \gamma _ { 1 }$and$\gamma _ { 2 }$are two gauge equivalent solutions, then$H _ { \gamma _ { 1 } }$and$H _ { \gamma _ { 2 } }$are (non-canonically) isomorphic HðmÞ-modules.

We define now cup products for all three diferential graded Lie algebras listed at the beginning of this section. For$T _ { \mathrm { p o l y } } ( X )$the cup product is defined as the usual cup product of polyvector fields (see Section 4.6.1). One can check directly that this cup product is compatible with the diferential$\mathrm { d } + [ \gamma , \cdot ]$, and is a graded commutative associative product. For the Hochschild complex of an associative algebra$A ,$the cup product on$H _ { \gamma }$is defined in a more tricky way. It is defined on the complex by the formula

$$
\begin{array}{l} (t _ {1} \cup t _ {2}) (a _ {0} \otimes \dots \otimes a _ {n}) \\ := \sum_ {0 \leq k _ {1} \leq k _ {2} \leq k _ {3} \leq k _ {4} \leq n} \pm \gamma^ {n - (k _ {2} - k _ {1} + k _ {4} - k _ {3})} (a _ {0} \otimes \dots \\ \quad \otimes t _ {1} (a _ {k _ {1}} \otimes \dots) \otimes a _ {k _ {2}} \otimes \dots \otimes t _ {2} (a _ {k _ {3}} \otimes \dots) \otimes a _ {k _ {4}} \otimes \dots), \end{array}
$$

where$\gamma ^ { l } \in \operatorname { H o m } ( A ^ { \otimes ( l + 1 ) } , A ) \otimes \left( \mathbf { k } [ 0 ] \cdot 1 \oplus \mathbf { m } \right) ^ { 1 - l }$is homogeneous component of $\left( \gamma + m _ { A } \otimes 1 \right)$

It is not a trivial check that the cup product on the Hochschild complex is compatible with diferentials, and also is commutative, associative and gaugeequivariant on the level of cohomology. Formally, we will not use this fact. The proof is a direct calculation with Hochschild cochains. Even if one replaces formulas by appropriate pictures, the calculation is still quite long, about four or five pages of tiny drawings. Alternatively, there is a simple abstract explanation using the interpretation of the deformation theory related with the shifted Hochschild complex as a deformation theory of triangulated categories (or, better,$A _ { \infty }$-categories, see [33]).

We define the cup product for$D _ { \mathrm { p o l y } } ( X )$by the restriction of formulas for the cupproduct in$C ( A , A )$

## 8.2. COMPATIBILITY OF U WITH CUP PRODUCTS

THEOREM 8.1. The quasi-isomorphism U constructed in Section 6 maps the cupproduct for$T _ { \mathrm { p o l y } } ( X )$to the cup product for$D _ { \mathrm { p o l y } } ( X )$

Sketch of the Proof. We translate the statement of the theorem to the language of graphs and integrals. The tangent map is given by integrals where one of vertices of the first type is marked. This is the vertex where we put a representative t for the tangent element$[ t ] \in H _ { \gamma }$. We put copies of$\gamma$(which is a polyvector field with values in m) into all other vertices of the first type. The rule which we just described follows directly from the Leibniz formula applied to the Taylor series for$\boldsymbol { \mathcal U }$

Now we are interested in the behavior of the tangent map with respect to a bilinear operation on the tangent space. It means that we now have two marked vertices of the first type.

The statement of the theorem is an identity between two expressions corresponding to cup products for$T _ { \mathrm { p o l y } } ( X )$and$D _ { \mathrm { p o l y } } ( X )$respectively.

## 8.2.1. Pictures for the Cup Product in Polyvector Fields

We claim that the side of identity with the cup product for the case$T _ { \mathrm { p o l y } } ( X )$, corresponds to pictures of two points (say,$p _ { 1 } , p _ { 2 } )$, where we put representatives of elements of$H _ { \gamma }$which we want to multiply, are infinitely close points on$\mathcal { H }$. Precisely, this means that we integrate products of copies of the form d/ over preimages$P _ { \alpha }$of some point a in$\mathbb { R } / 2 \pi \mathbb { Z } \simeq C _ { 2 } \subset \overline { { C } } _ { 2 , 0 }$with respect to the forgetting map$\overline { { C } } _ { n , m } \longrightarrow \overline { { C } } _ { 2 , 0 }$ It is easy to see that$P _ { \alpha }$has codimension$2$in$\overline { { C } } _ { n , m }$and contains no strata$C _ { T }$of codimension 2. It implies that as a singular chain,$P _ { \alpha }$is equal to the sum of closures of noncompact hypersurfaces

$$
P _ {\alpha} \cap \partial_ {S} (\overline {{{C}}} _ {n, m}), P _ {\alpha} \cap \partial_ {S _ {1}, S _ {2}} (\overline {{{C}}} _ {n, m}).
$$

in boundary strata of$\overline { { C } } _ { n , m } .$. It is easy to see that intersections$P _ { \alpha } \cap \partial _ { S _ { 1 } , S _ { 2 } } ( \overline { { C } } _ { n , m } )$are empty and intersection$P _ { \alpha } \cap \partial _ { S } ( \overline { { C } } _ { n , m } )$is nonempty if$S \supseteq \{ 1 , 2 \}$. In general pictures, which can potentially contribute with a nonzero weight something like the one in Figure 16.

In other words, we have a collision of several points in$\mathcal { H }$including both points$p _ { 1 }$ and$p _ { 2 }$. These points should not be connected by an edge because otherwise the integral vanishes (remember that the direction from$p _ { 1 }$to$p _ { 2 }$is fixed). Also, if $\# S \geq 3$, then the integral vanishes by Lemma 6.6. The only nontrivial case which is left is when$S = \{ 1 , 2 \}$and points$p _ { 1 } , \ p _ { 2 }$are not connected. Figure 17 represents a nonvanishing term corresponding to the cup product in$T _ { \mathrm { p o l y } } ( X )$

![](images/page_49_image_0.jpg)

Figure 16. A priori picture for terms for the cup-product in$T _ { \mathrm { p o l y } }$

![](images/page_49_image_2.jpg)

Figure 17. Nonzero terms for the cup-product in$T _ { \mathrm { p o l y } }$

## 8.2.2. Pictures for the Cup Product in the Hochschild Complex

The cup product for$D _ { \mathrm { p o l y } } ( X )$is given by pictures where two marked points are separated and infinitely close to R. Again, the precise definition is that we integrate products of copies of d/ over the pre-image$P _ { 0 , 1 }$of the point$[ ( 0 , 1 ) ] \in \overline { { C } } _ { 0 , 2 } \subset \overline { { C } } _ { 2 , 0 }$ Analysis analogous to the one from the previous subsection shows that$P _ { 0 , 1 }$does not intersect any boundary stratum of$\overline { { C } } _ { n , m } .$. Thus, as a chain of codimension 2, this pre-image$P _ { 0 , 1 }$coincides with the union of closures of strata$C _ { T }$of codimension 2 such that$C _ { T } \subseteq P _ { 0 , 1 }$. It is easy to see that any such stratum gives pictures like the one in Figure 18 where there is no arrow going from the circled regions outside (as in Figure 11), and we get exactly the cup product in the tangent cohomology of the Hochschild complex as was described above.

## 8.2.3. Homotopy Between Two Pictures

Choosing a path from one (limiting) configuration of two points on$\mathcal { H }$to another configuration (see Figure 19), we see that two products coincide on the level of cohomology.(

![](images/page_50_image_0.jpg)

Figure 18. Cup product in the Hochschild complex.

![](images/page_50_image_2.jpg)

Figure 19. Path in the configuration space of two points in${ \mathcal { H } } .$. Dashed lines are trajectories of two points.

## 8.3. FIRST APPLICATION: DUFLO-KIRILLOV ISOMORPHISM

## 8.3.1. Quantization of the Kirillov–Poisson Bracket

Let g be a finite-dimensional Lie algebra over R. The dual space to g endowed with the Kirillov–Poisson bracket is naturally a Poisson manifold (see [29]). We recall here the formula for this bracket: if$p \in \mathbf { g } ^ { * }$is a point and$f , g$are two functions on$\mathbf { g }$then the value$\{ f , g \} _ { | p }$is defined as$\langle p , [ \mathrm { d } f _ { | p } , \mathrm { d } g _ { | p } ] \rangle$where the diferentials of functions$f , g$at $p$are considered as elements of${ \bf g } \simeq ( { \bf g } ^ { * } ) ^ { * }$. One can consider$\mathbf { g } ^ { * }$as an algebraic Poisson manifold because coeficients of the Kirillov–Poisson bracket are linear functions on$\mathbf { g } ^ { * }$

THEOREM 8.2 The canonical quantization of the Poisson manifold$\mathbf { g } ^ { * }$is isomorphic to the family of algebras${ \mathcal { U } } _ { \hbar } ( \mathbf { g } )$defined as universal enveloping algebras of g endowed with the bracket$\hbar [ , ]$

Proof. In Section 6.4 we have constructed a canonical star product on the algebra of functions on arbitrary finite-dimensional afine space endowed with a Poisson structure. Therefore we obtain a canonical star product on$C ^ { \infty } ( \mathbf { g } ^ { * } )$. We claim that the product of any two polynomials on$\mathbf { g } ^ { * }$is a polynomial in$\hbar$with coeficients which are polynomials on$\mathbf { g } ^ { * }$. The reason is that the star product is constructed in invariant way, using the contraction of indices. Let us denote by$\beta \in \mathbf { g } ^ { * } \otimes \mathbf { g } ^ { * } \otimes \mathbf { g }$the tensor giving the Lie bracket on g. All nonzero natural operations$\mathrm { S y m } ^ { k } ( \mathbf { g } ) \otimes \mathrm { S y m } ^ { l } ( \mathbf { g } ) \longrightarrow \mathrm { S y m } ^ { m } ( \mathbf { g } )$ which can be defined by contraction of indices with the tensor product of several copies of$\dot { \boldsymbol { { \beta } } } ,$exist only for m$\leqslant k + l ,$and for every given$m ,$there are only finitely many ways to contract indices. Thus, it makes sense to put h equal to 1 and obtain a product on$\mathrm { S y m } ( \mathbf { g } ) = \oplus _ { k \geqslant 0 } \mathrm { S y m } ^ { k } ( \mathbf { g } )$. We denote this product also by ?.

It is easy to see that for$\gamma _ { 1 } , \gamma _ { 2 } \in \mathbf { g }$the following identity holds:

$$
\gamma_ {1} \star \gamma_ {2} - \gamma_ {2} \star \gamma_ {1} = [ \gamma_ {1}, \gamma_ {2} ].
$$

Moreover, the top component of the star product which maps$\mathbf { S y m } ^ { k } ( \mathbf { g } ) \otimes \mathbf { S y m } ^ { l } ( \mathbf { g } )$to $\mathbf { S y m } ^ { k + l } ( \mathbf { g } )$, coincides with the standard commutative product on SymðgÞ. From this two facts one concludes that there exists a unique isomorphism of algebras

$$
I _ {a l g}: (\mathscr {U} \mathbf {g}, \cdot) \longrightarrow (\operatorname{Sym} (\mathbf {g}), \star)
$$

such that$I _ { \mathrm { a l g } } ( \gamma ) = \gamma$for$\gamma \in { \bf g } .$, where  denotes the universal enveloping algebra of g with the standard product.

One can easily recover variable h in this description and get the statement of the theorem.(

COROLLARY 8.3 The center of the universal enveloping algebra is canonically isomorphic as an algebra to the algebra$( \mathrm { S y m } ( \mathbf { g } ) ) ^ { \mathbf { g } }$of g-invariant polynomials on$\mathbf { g } ^ { * }$

Proof. The center of$\boldsymbol { \mathcal { U } } \mathbf { g }$is the 0th cohomology for the (local) Hochschild complex of$\mathcal { U } \mathbf { g }$endowed with the standard cup product. The algebra$( \mathrm { S y m } ( \mathbf { g } ) ) ^ { \mathbf { g } }$is the 0th cohomology of the algebra of polyvector fields on$\mathbf { g } ^ { * }$endowed with the diferential $\left[ \alpha , . \right]$where a is the Kirillov–Poisson bracket. From Theorem$8 . 1$, we conclude that by applying the tangent map to$\mathcal { U } ,$, we get an isomorphism of algebras.(

## 8.3.2. Three Isomorphisms

In the proof of Theorem 8.2 we introduced an isomorphism$I _ { \mathrm { a l g } }$of algebras.

We denote by$I _ { \mathrm { P B W } }$the isomorphism of vector spaces$\operatorname { S y m } ( \mathbf { g } ) \longrightarrow { \mathcal { U } } \mathbf { g }$(subscript from the Poincare´ –Birkhof–Witt theorem), which is defined as

$$
\gamma_ {1} \gamma_ {2} \dots \gamma_ {n} \longrightarrow \frac {1}{n !} \sum_ {\sigma \in \Sigma_ {n}} \gamma_ {\sigma_ {1}} \cdot \gamma_ {\sigma_ {2}} \dots \gamma_ {\sigma_ {n}}.
$$

Analogously to the arguments above, one can see that the tangent map from polyvector fields on$\mathbf { g } ^ { * }$to the Hochschild complex of the quantized algebra can be defined for$\hbar = 1$and for polynomial coeficients. We denote by$I _ { T }$its component which maps polynomial 0-vector fields on${ \bf g } ^ { * } \left( \mathrm { i } . \mathrm { e } \right.$. elements of$\operatorname { S y m } ( \mathbf { g } ) )$) to 0-cochains of the Hochschild complex of the algebra$( \mathrm { S y m } ( \mathbf { g } ) , \star )$. Thus,$I _ { T }$is an isomorphism of vector spaces

$$
I _ {T}: \operatorname{Sym} (\mathbf {g}) \longrightarrow \operatorname{Sym} (\mathbf {g})
$$

and the restriction of$I _ { T }$to the algebra of$a d ( \mathbf { g } ) ^ { * }$-invariant polynomials on$\mathbf { g } ^ { * }$is an isomorphism of algebras

$$
\operatorname{Sym} (\mathbf {g}) ^ {\mathbf {g}} \longrightarrow \operatorname{Center} ((\operatorname{Sym} (\mathbf {g}), \star)).
$$

Combining all facts from above we get a sequence of isomorphisms of vector spaces:

$$
\operatorname{Sym} (\mathbf {g}) \xrightarrow {I _ {T}} \operatorname{Sym} (\mathbf {g}) \xleftarrow {I _ {\mathrm{alg}}} \mathscr {U} \mathbf {g} \xleftarrow {I _ {\mathrm{PBW}}} \operatorname{Sym} (\mathbf {g}).
$$

These isomorphisms are ad${ \bf \Pi } ( { \bf g } ) \cdot { \bf \Pi }$-invariant. Thus, one get isomorphisms

$$
(\operatorname{Sym} (\mathbf {g})) ^ {\mathbf {g}} \xrightarrow {I _ {T _ {| \dots}}} \operatorname{Center} (\operatorname{Sym} (\mathbf {g}), \star) \xleftarrow {I _ {\mathrm{alg} _ {| \dots}}} \operatorname{Center} (\mathcal {U} \mathbf {g}) \xleftarrow {I _ {\mathrm{PBW} _ {| \dots}}} (\operatorname{Sym} (\mathbf {g})) ^ {\mathbf {g}},
$$

where the subscript j    denotes the restriction to subspaces of$\operatorname { a d } ( \mathbf { g } )$-invariants. Moreover, first two arrows are isomorphism of algebras. Thus, we have proved the following theorem:

THEOREM 8.4. The restriction of the map

$$
\left(I _ {\mathrm{alg}}\right) ^ {- 1} \circ I _ {T} \colon \operatorname{Sym} (\mathbf {g}) \longrightarrow \mathscr {U} \mathbf {g}
$$

to$( \mathrm { S y m } ( \mathbf { g } ) ) ^ { \mathbf { g } }$is an isomorphism of algebras$( \mathrm { S y m } ( \mathbf { g } ) ) ^ { \mathbf { g } } { \longrightarrow } \mathrm { C e n t e r } \ ( \mathcal { U } \mathbf { g } )$

## 8.3.3. Automorphisms of SymðgÞ

Let us calculate the automorphisms$I _ { T }$and$I _ { \mathrm { a l g } } \circ I _ { \mathrm { P B W } }$of the vector space$\operatorname { S y m } ( \mathbf { g } )$ We claim that both these automorphisms are translation invariant operators on the space$\operatorname { S y m } ( \mathbf { g } )$of polynomials on$\mathbf { g } ^ { * }$

The algebra of translation invariant operators on the space of polynomials on a vector space$V$is canonically isomorphic to the algebra of formal power series generated by$V .$Generators of this algebra acts as derivations along constant vector fields in$V .$Thus, any such operator can be seen as a formal power series at zero on the dual vector space$V ^ { * }$. We apply this formalism to the case$V = \mathbf { g } ^ { * }$

THEOREM 8.5. Operators$I _ { T }$and$I _ { \mathrm { a l g } } \circ$I<sub>PBW</sub> respectively, are translation invariant operators associated with formal power series$S _ { 1 } ( \gamma )$and$S _ { 2 } ( \gamma )$at zero in g of the form

$$
\begin{array}{l} S _ {1} (\gamma) = \exp \biggl (\sum_ {k \geq 1} c _ {2 k} ^ {(1)} \operatorname{Trace} (\operatorname{ad} (\gamma) ^ {2 k}) \biggr), \\ S _ {2} (\gamma) = \exp \biggl (\sum_ {k \geq 1} c _ {2 k} ^ {(2)} \operatorname{Trace} (\operatorname{ad} (\gamma) ^ {2 k}) \biggr), \end{array}
$$

where$c _ { 2 } ^ { ( 1 ) } , c _ { 4 } ^ { ( 1 ) } , \cdots$ and$c _ { 2 } ^ { ( 2 ) } , c _ { 4 } ^ { ( 2 ) }$;    are two infinite sequences of real numbers indexed $b y$even natural numbers.

Proof. We will study separately two cases.

8.3.3.1. Isomorphism$I _ { T } .$The isomorphism$I _ { T }$is given by the sum over terms corresponding to admissible graphs C with no vertices of the second type, one special vertex v of the first type such that no edge starts at$\nu ,$and such that at any other vertex starts with two edges and ends no more than one edge. Vertex v is the marked vertex where we put an element of$\operatorname { S y m } ( \mathbf { g } )$considered as an element of tangent cohomology. At other vertices we put the Poisson–Kirillov bi-vector field on$\mathbf { g } ^ { * }$, i.e. the tensor of commutator operation in g. As the result we get 0-diferential operator, i.e. an element of algebra SymðgÞ.

It is easy to see that any such graph is isomorphic to a union of copies of ‘wheels’ $\mathrm { { W h } } _ { n } , n \geqslant 2$represented in Figure 20 with identified central vertex v. Figure 21 shows a typical graph of the union.

In the integration, we may assume that the point corresponding to v is fixed, say that it is$i \cdot 1 + 0 \in \mathcal { H }$, because group$G ^ { ( 1 ) }$acts simply transitively on${ \mathcal { H } } .$. First of all, the operator$\mathrm { S y m } ( \mathbf { g } ) \longrightarrow \mathrm { S y m } ( \mathbf { g } )$corresponding to the individual wheel$\mathrm { W h } _ { n }$is the diferential operator on$\mathbf { g } ^ { * }$with constant coeficients, and it corresponds to the polynomial$\gamma \mapsto$Trace$( \operatorname { a d } ( \gamma ) ^ { n } )$on g. The operator corresponding to the joint of several wheels is the product of operators associated with individual wheels. Also, the integral corresponding to the joint is the product of integrals. Thus, with the help of symmetry factors, we conclude that the total operator is equal to the exponent of the sum of operators associated with wheels$\mathrm { W h } _ { n } , \ n \geqslant 2$with weights equal to corresponding integrals. By the symmetry argument used several times before$( z \mapsto - { \overline { { z } } } )$ we see that integrals corresponding to wheels with odd n vanish. The first statement of Theorem 8.5 is proven.(

![](images/page_53_image_3.jpg)

Figure 20. Wheel graph.

![](images/page_53_image_5.jpg)

Figure 21. A union of wheels.

8.3.3.2. Isomorphism$I _ { \mathrm { a l g } } \circ I _ { \mathrm { P B W } }$: The second case, for the operator$I _ { \mathrm { a l g } } \circ I _ { \mathrm { P B W } }$, is a bit more tricky. Let us write a formula for this map:

$$
I _ {\mathrm{alg}} \circ I _ {\mathrm{PBW}}: \gamma^ {n} \mapsto \gamma \star \gamma \star \gamma \star \dots \star \gamma^ {\star} (n \text {   copies   of   } \gamma).
$$

This formula defines the map unambiguously because elements$\gamma ^ { n } , \ \gamma \in { \bf g } , n \geqslant 0$ generate$\operatorname { S y m } ( \mathbf { g } )$as a vector space.

In order to multiply several (say, m, where$m \geqslant 2 )$elements of the quantized algebra, we should put these elements at mfixed points in increasing order on R and take the sum over all possible graphs with m vertices of the second type of corresponding expressions with appropriate weights. The result does not depend on the position of fixed points on R because the star product is associative. Moreover, if we calculate a power of a given element with respect to the ? product, we can put all these points in arbitrary order. It follows that we can take an average over configurations of$m$points on R where each point is random, distributed independently from other points, with a certain probability density on R. We choose a probability distribution on R with a smooth symmetric (under transformation$x \mapsto - x )$density $\rho ( x )$. We assume also that$\rho ( x ) \mathrm { d } x$is the restriction to$\mathbb { R } \simeq C _ { 1 , 1 }$of a smooth 1-form on${ \overline { { C } } } _ { 1 , 1 } \simeq \{ - \infty \} \sqcup \mathbb { R } \sqcup \{ + \infty \}$. With probability 1, our m points will be pairwise distinct. One can check easily that the interchanging of order of integration (i.e. for the taking mean value from the probability theory side, and for the integration of diferential forms over configuration spaces) is valid operation in our case.

The conclusion is that the mth power of an element of quantized algebra can be calculated as a sum over all graphs with m vertices of the second type, with weights equal to integrals over configuration spaces where we integrate products of forms d/ and 1-forms$\rho ( x _ { i } ) \mathrm { d } x _ { i }$where$x _ { i }$are points moving along R.

The basic element of pictures in our case are ‘wheels without axles’ (Figure 22) and the K-graph (Figure 23) which gives 0 for symmetry reasons. The typical total picture is something like (with$m = 1 0 )$the one drawn in Figure 24.

Again, it is clear from all this that the operator$I _ { \mathrm { a l g } } \circ I _ { \mathrm { P B W } }$is a diferential operator with constant coeficients on SymðgÞ, equal to the exponent of the sum of operators corresponding to individual wheels. These operators are again proportional to operators associated with power series on g

![](images/page_54_image_7.jpg)

Figure 22. One of basic elements in the formula for$\gamma \star \cdots \star \gamma .$

![](images/page_55_image_0.jpg)

Figure 23. Another potential basic element, it vanishes for symmetry reasons.

![](images/page_55_image_2.jpg)

Figure 24. A term in the formula for$\gamma \star \cdots \star \gamma .$

c ! Trace ðadðcÞ<sup>n</sup>Þ:

By the same symmetry reasons as above we see that integrals corresponding to odd n vanish. The second part of Theorem 8.5 is proven.(

## 8.3.4. Comparison with the Duflo–Kirillov Isomorphism

For the case of semi-simple g, there is so-called Harish-Chandra isomorphism between algebras$( \mathrm { S y m } ( \mathbf { g } ) ) ^ { \mathbf { g } }$and$\operatorname { C e n t e r } ( { \mathcal { U } } \mathbf { g } )$. A. Kirillov realized that there is a way to rewrite the Harish-Chandra isomorphism in a form which makes sense for arbitrary finite-dimensional Lie algebra, i.e. without using the Cartan and Borel subalgebras, the Weyl group, etc. Later M. Duflo (see [13]) proved that the map proposed by Kirillov is an isomorphism for all finite-dimensional Lie algebras.

The explicit formula for the Duflo–Kirillov isomorphism is the following:

$$
I _ {\mathrm{DK}}: (\operatorname{Sym} (\mathbf {g})) ^ {\mathbf {g}} \simeq \operatorname{Center} (\mathcal {U} (\mathbf {g})), \quad I _ {\mathrm{DK}} = I _ {\mathrm{PBW} | (S y m (\mathbf {g})) ^ {\mathbf {g}}} \circ I _ {\text { strange } | (\operatorname{Sym} (\mathbf {g})) ^ {\mathbf {g}}},
$$

where$I _ { \mathrm { s t r a n g e } }$is an invertible translation invariant operator on$\operatorname { S y m } ( \mathbf { g } )$associated with the following formal power series on g at zero, reminiscent of the square root of the Todd class:

$$
\gamma \mapsto \exp \left(\sum_ {k \geqslant 1} \frac {B _ {2 k}}{4 k (2 k) !} \operatorname{Trace} \left(\operatorname{ad} (\gamma) ^ {2 k}\right)\right),
$$

where$B _ { 2 } , B _ { 4 } , \ldots$. are Bernoulli numbers. Formally, one can write the right-hand side as$\operatorname* { d e t } ( q ( \operatorname { a d } ( \gamma ) ) )$where

$$
q (x) := \sqrt {\frac {\mathrm{e} ^ {x / 2} - \mathrm{e} ^ {- x / 2}}{x}}.
$$

The fact that the Duflo–Kirillov isomorphism is an isomorphism of algebras is highly nontrivial. All proofs known before (see [13, 21]) used certain facts about finite-dimensional Lie algebras which follow only from the classification theory. In particular, the fact that the analogous isomorphism for Lie superalgebras is compatible with products, was not know.

We claim that our isomorphism coincides with the Duflo–Kirillow isomorphism. Let us sketch the argument. In fact, we claim that

$$
I _ {\mathrm{alg}} ^ {- 1} \circ I _ {T} = I _ {\mathrm{PBW}} \circ I _ {\mathrm{strange}}.
$$

If it is not true then we get a nonzero series E$\mathbf { r } \in t ^ { 2 } \mathbb { R } [ [ t ^ { 2 } ] ]$such that the translation invariant operator on$\operatorname { S y m } ( \mathbf { g } )$associated with$\gamma \longmapsto I _ { \mathrm { d e t } ( \mathrm { e x p } ( \mathrm { E r r } ( \mathrm { a d } ( \gamma ) ) ) ) } \mathrm { g i v e s }$an automorphism of algebra$( \mathrm { S y m } ( \mathbf { g } ) ) ^ { \mathbf { g } }$. Let$2 k > 0$be the degree of the first nonvanishing term in the expansion of Err. Then it is easy to see that the operator on$\operatorname { S y m } ( \mathbf { g } )$associated with the polynomial$\gamma \mapsto \mathrm { T r a c e } ( \mathrm { a d } ( \gamma ) ^ { \overset { } { 2 } k }$is a derivation when restricted to$( \mathrm { S y m } ( \mathbf { g } ) ) ^ { \mathbf { g } }$ One can show that it is not true using Lie algebras$\mathbf { g } = \mathrm { g l } ( n )$for large n. Thus, we get a contradiction and proved that$\mathrm { E r r } = 0$(

As a remark, we would like to mention that if one replaces series$q ( x )$above just by the inverse to the square root of the series related to the Todd class

$$
\left(\frac {x}{1 - \mathrm{e} ^ {- x}}\right) ^ {- \frac {1}{2}},
$$

then one still gets an isomorphism of algebras. The reason is that the one-parameter group of automorphisms of$\operatorname { S y m } ( \mathbf { g } )$associated with the series

$$
\gamma \longrightarrow \exp (\text { const } \cdot \text { Trace } (\text { ad } (\gamma)))
$$

preserves the structure of Poisson algebra on g<sup></sup>. This one-parameter group also acts by automorphisms of$\mathcal { U } \mathbf { g }$. It is analogous to the Tomita–Takesaki modular automorphism group for von Neumann algebras.

## 8.3.5. Results in Rigid Tensor Categories

Many proofs from this paper can be transported to a more general context of rigid Q-linear tensor categories (i.e. Abelian symmetric monoidal categories with the duality functor imitating the behavior of finite-dimensional vector spaces). We will be very brief here.

First of all, one can formulate and prove the Poincare´–Birkhof–Witt theorem in a great generality, in Q-linear additive symmetric monoidal categories with infinite sums and kernels of projectors. For example, it holds in the category of A-modules where A is an arbitrary commutative associative algebra over Q. Thus, we can speak about universal enveloping algebras and the isomorphism$I _ { \mathrm { P B W } }$

One can define the Duflo–Kirillow morphism for Lie algebra in a k-linear rigid tensor category where k is a field of characteristic zero, because Bernoulli numbers are generality as well. It cannot hold for infinite-dimensional Lie algebras because we use traces of products of oprators in adjoint representation.

In [28] a conjecture was made in the attempt to prove that that Duflo–Kirillov formulas give a morphism of algebras. It seems plausible our results can help one to prove this conjecture. Also, there is another related conjecture concerning two products in the algebra of chord diagrams (see [4]) which seems to be a corollary of our results.

## 8.4. SECOND APPLICATION: ALGEBRAS OF EXT-S

Let X be complex manifold, or a smooth algebraic variety of field k of characteristic zero. We associate with it two graded vector spaces. The first space$H T ^ { \bullet } ( X )$is the direct sum$\begin{array} { r } { \bigoplus _ { k , l } H ^ { k } ( X , \wedge ^ { l } T _ { X } ) [ - k - l ] } \end{array}$. The second space$H H ^ { \bullet } ( X )$is the space $\circled { \pmb { \mathscr { D } } _ { k } \mathrm { E x t } _ { \mathrm { C o h } ( X \times X ) } ^ { k } } ( \mathcal { O } _ { \mathrm { d i a g } } , \mathcal { O } _ { \mathrm { d i a g } } ) [ - k ]$of Ext-groups in the category of coherent sheaves on$X \times X$from the sheaf of functions on the diagonal to itself. The space$H H ^ { \bullet } ( X )$ can be thought as the Hochschild cohomology of the space X. The reason is that the Hochschild cohomology of any algebra A can be also defined as$\mathrm { E x t } _ { A - \mathrm { m o d } - A } ^ { \bullet } ( A , A )$in the category of bimodules.

Both spaces,$H H ^ { \bullet } ( X )$and$H T ^ { \bullet } ( X )$carry natural products. For$H H ^ { \bullet } ( X )$it is the Yoneda composition, and for$H T ^ { \bullet } ( X )$it is the cup-product of cohomology and of polyvector fields.

CLAIM Graded algebras$H H ^ { \bullet } ( X )$and$H T ^ { \bullet } ( X )$are canonically isomorphic. The isomorphism between them is functorial with respect to e´tale maps.

This statement (important for the Mirror Symmetry, see [33]) is again a corollary of Theorem 8.1. Here we will not give the proof.

## Acknowledgements

I am grateful to G. Dito, Y. Soibelman, and D. Sternheimer for many useful remarks and comments.

## References

1. Alexandrov, M., Kontsevich, M., Schwarz, A. and Zaboronsky, O.: The geometry of the master equation and topological quantum field theory, Internat. J. Modern$P h y s$. A 12(7) (1997), 1405–1429.

2. Arnal, D., Manchon, D. and Masmoudi, M.: Choix des signes pour la formalite´ de M. Kontsevich. Pacific. J. Math. 203 (2002), 23–66.

3. Arnold, V.I., Gusein-Zade, S.M. and Varchenko, A.N.: Singularities of Diferentiable Maps, Vol. I: The Classification of Critical Points, Caustics and Wave Fronts, Birkha¨user, Boston, 1985.

4. Bar-Natan, D., Garoufalidis, S., Rozansky, L. and Thurston, D.: Wheels, wheeling, and the Kontsevich integral of the unknot, Israel J. Math. 119 (2000), 217–237.

5. Barannikov, S. and Kontsevich, M.: Frobenius manifolds and formality of Lie algebras of polyvector fields, Internat. Math. Res. Notices 1998(4) (1998), 201–215.

6. Bayen, F., Flato, M., Fr-nsdal, C., Lichnerowicz, A. and Sternheimer, D.: Deformation theory and quantization. I. Deformations of symplectic structures, Ann. Phys. 111(1) (1978), 61–110.

7. Cahen, M., Gutt, S. and De Wilde, M.: Local cohomology of the algebra of$C ^ { \infty }$functions on a connected manifold, Lett. Math. Phys. 4 (1980), 157–167.

8. Cattaneo, A. and Felder, G.: On the AKSZ formulation of the Poisson sigma model, Lett. Math. Phys. 56(2) (2001), 163–179.

9. Cattaneo, A. and Felder, G.: A path integral approach to the Kontsevich quantization formula, Comm. Math. Phys. 212(3) (2000), 591–611.

10. Cattaneo, A., Felder, G. and Tomassini, L.: From local to global deformation quantization of Poisson manifolds, Duke Math. J. 115(2) (2002), 329–352.

11. Deligne, P.: Cate´ gories tannakiennes, In: The Grothendieck Festschrift, Vol. II, Progr. in Math. 87, Birkha¨user, Boston, 1990, pp. 111–195.

12. De Wilde, M. and Lecomte, P.B.A.: Existence ofstar-products and offormal deformations in Poisson Lie algebra of arbitrary symplectic manifolds, Lett. Math. Phys. 7 (1983), 487–496.

13. Duflo, M.: Caracte\` res des alge\` bres de Lie re´ solubles, C.R. Acad. Sci. Se´r. A 269 (1969), 437–438.

14. Etingof, P. and Kazhdan, D.: Quantization of Lie Bialgebras, I, Selecta Math. (New Ser.) 2(1) (1996), 1–41.

15. Fedosov, B.: A simple geometric construction of deformation quantization, J. Diferential Geom. 40(2) (1994), 213–238.

16. Felder, G. and Shoikhet, B.: Deformation quantization with traces, Lett. Math. Phys. 53(1) (2000), 75–86.

17. Fulton, W. and MacPherson, R.: Compactification of configuration spaces, Ann. ofMath. (2) 139(1) (1994), 183–225.

18. Gelfand, I. M. and Kazhdan D. A.: Some problems of diferential geometry and the calculation of cohomologies of Lie algebras of vector fields, Soviet Math. Dokl. 12(5) (1971), 1367–1370.

19. Gerstenhaber, M. and Voronov, A.: Homotopy G-algebras and moduli space operad, Internat. Math. Res. Notices 1995(3) (1995), 141–153.

20. Getzler, E. and Jones, J. D. S.: Operads, homotopy algebra and iterated integrals for double loop spaces, 1994, hep-th/9403055.

21. Ginzburg, V.: Method of orbits in the representation theory of complex Lie groups, Funct. Anal. Appl. 15(1) (1981), 18–28.

22. Goldman, W. and Millson, J.: The homotopy invariance of the Kuranishi space, Illinois. J. Math. 34(2) (1990), 337–367.

23. Hinich, V.: Tamarkin’s proof of Kontsevich formality theorem, Forum Math. 15(4) (2003), 591–614.

24. Hinich, V. and Schechtman, V.: Deformation theory and Lie algebra homology, I. II., Algebra Colloq. 4(2) (1997), 213–240, and 4(3) (1997), 291–316.

25. Hinich, V. and Schechtman, V.: Homotopy Lie algebras, In: I. M. Gelfand Seminar, Adv. Soviet Math. 16(2), Amer. Math. Soc., Providence, RI, 1993, pp. 1–28.

26. Hochschild, G., Kostant, B. and Rosenberg, A.: Diferential forms on regular afine algebras, Trans. Amer. Math. Soc. 102 (1962), 383–408.

27. Hu, P., Kriz, I. and Voronov, A.: On Kontsevich’s Hochschild cohomology conjecture, 2003, math.AT/0309369.

28. Kashiwara, M. and Vergne, M.: The Campbell-Hausdorf formula and invariant hyperfunctions, Invent. Math. 47 (1978), 249–272.

29. Kirillov, A.: Elements of the Theory of Representations, Springer-Verlag, Berlin, 1976.

30. Kontsevich, M.: Feynman diagrams and low-dimensional topology, In: First European Congress of Mathematics (Paris, 1992), Vol. II, Progr. in Math. 120, Birkha¨user, Basel, 1994, pp. 97–121.

31. Kontsevich, M.: Formality conjecture, In: D. Sternheimer et al. (eds), Deformation Theory and Symplectic Geometry, Kluwer, Dordrecht, 1997, pp. 139–156.

32. Kontsevich, M.: Rozansky–Witten invariants via formal geometry, Compositio Math. 115(1) (1999), 115–127.

33. Kontsevich, M.: Homological algebra of mirror symmetry, In: Proceedings of ICM, (Zu¨rich 1994) Vol. I, Birkha¨user, Basel, 1995, pp. 120–139.

34. Kontsevich, M.: Deformation quantization of Poisson manifolds, I., 1997, q-alg/9709040.

35. Kontsevich, M.: Operads and motives in deformation quantization, Lett. Math. Phys. 48(1) (1999), 35–72.

36. Kontsevich, M.: Deformation quantization of algebaric varieties, Lett. Math. Phys. 56(3) (2001), 271–294.

37. Kontsevich, M. and Soibelman, Y.: Deformations of algebras over operads and the Deligne conjecture, In: G. Dito and D. Sternheimer (eds), Confe´rence Moshe´ Flato 1999, Vol. I (Dijon 1999), Kluwer Acad. Publ., Dordrecht, 2000, pp. 255–307.

38. McClure, M. and Smith, J.: A solution of Deligne’s Hochschild cohomology conjecture, In: Recent Progress in Homotopy Theory (Baltimore, MD, 2000), Contemp. Math. 293, Amer. Math. Soc., Providence, RI, 2002, pp. 153–193,

39. Manin, Y.I.: Gauge Field Theory and Complex Geometry, Springer-Verlag, Berlin, 1988.

40. Markl, M. and Voronov, A.: PROPped up graph cohomology, 2000, math.QA/0307081.

41. Quillen, D.: Superconnections and the Chern character, Topology 24 (1985), 89–95.

42. Schlessinger, M. and Stashef, J.: The Lie algebra structure on tangent cohomology and deformation theory, J. Pure Appl. Algebra 38 (1985), 313–322.

43. Sullivan, D.: Infinitesimal computations in topology, Inst. Hautes E<sup>´</sup>tudes Sci. Publ. Math. (1977) No. 47, (1978), 269–331.

44. Voronov, A.: Quantizing Poisson manifolds, In: Perspectives on Quantization (South Hadley, MA, 1996), Contemp. Math. 214, Amer. Math. Soc., Providence, RI, 1998, pp. 189–195.

45. Tamarkin, D.: Another proof of M. Kontsevich formality theorem, 1998, math.QA/9803025.

46. Tamarkin, D.: Quantization of Lie bialgebras via the formality of the operad of little disks, in: G.Halbout (ed.), Deformation Quantization (Strasbourg 2001), IRMA Lectures in Math. Theoret. Phys. Vol. I, Walter de Gruyter, Berlin, 2002, pp. 203–236.

47. Tamarkin, D. and Tsygan, B.: Noncommutative diferential calculus, homotopy BV algebras and formality conjectures, Methods Funct. Anal. Topology 6(2) (2000), 85–100.