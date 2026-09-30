# PERFECTOID SPACES by PETER SCHOLZE

## ABSTRACT

We introduce a certain class of so-called perfectoid rings and spaces, which give a natural framework for Faltings’ almost purity theorem, and for which there is a natural tilting operation which exchanges characteristic 0 and characteristic p. We deduce the weight-monodromy conjecture in certain cases by reduction to equal characteristic.

## CONTENTS

1. Introduction ..... 245
2. Adic spaces ..... 252
3. Perfectoid fields ..... 263
4. Almost mathematics ..... 267
5. Perfectoid algebras ..... 272
6. Perfectoid spaces: analytic topology ..... 283
7. Perfectoid spaces: etale topology ..... 295
8. An example: toric varieties ..... 303
9. The weight-monodromy conjecture ..... 307
Acknowledgements ..... 311
References ..... 312

## 1. Introduction

In commutative algebra and algebraic geometry, some ofthe most subtle problems arise in the context of mixed characteristic, i.e. over local fields such as$\mathbf { Q } _ { b }$which are of characteristic 0, but whose residue field$\mathbf { F } _ { \boldsymbol { \phi } }$is ofcharacteristic$\cdot \cdot \cdot \cdot \cdot$The aim ofthis paper is to establish a general framework for reducing certain problems about mixed characteristic rings to problems about rings in characteristic$\beta .$. We will use this framework to establish a generalization ofFaltings’s almost purity theorem, and new results on Deligne’s weightmonodromy conjecture.

The basic result which we want to put into a larger context is the following canonical isomorphism of Galois groups, due to Fontaine and Wintenberger [13]. A special case is the following result.

Theorem 1.1. — The absolute Galois groups of$\mathbf { \tilde { Q } } _ { \theta } ( \theta ^ { 1 / p ^ { \infty } } )$and$\mathbf { F } _ { \boldsymbol { p } } ( { \it \Delta \phi } ( t ) )$are canonically isomorphic.

In other words, after adjoining all p-power roots o$\dot { \boldsymbol { p } }$to a mixed characteristic field, it looks like an equal characteristic ring in some way. Let us first explain how one can prove this theorem. Let K be the completion of$\mathbf { Q } _ { \nu } ( \dot { p } ^ { 1 / p ^ { \infty } } )$and let$\mathrm { K } ^ { \flat }$be the completion of$\mathbf { F } _ { \boldsymbol { p } } ( \ r ( t ) ) ( t ^ { 1 / \boldsymbol { p } ^ { \infty } } )$; it is enough to prove that the absolute Galois groups of$\mathrm { K }$and$\mathrm { K } ^ { \flat }$are isomorphic. Let us first explain the relation between K and$\mathrm { K } ^ { \flat }$, which in vague terms consists in replacing the prime number$\boldsymbol { p }$by a formal variable t. Let$\mathrm { K } ^ { \circ }$and$\mathrm { K } ^ { \flat \circ }$be the subrings of integral elements. Then

$$
\mathrm{K} ^ {\circ} / p = \mathbf {Z} _ {p} \big [ p ^ {1 / p ^ {\infty}} \big ] / p \cong \mathbf {F} _ {p} \big [ t ^ {1 / p ^ {\infty}} \big ] / t = \mathrm{K} ^ {\flat \circ} / t,
$$

where the middle isomorphism sends$p ^ { 1 / p ^ { n } }$to$t ^ { 1 / \boldsymbol { p } ^ { n } }$. Using it, one can define a continuous multiplicative, but nonadditive, map$\mathrm { K } ^ { \flat }  \mathrm { K } , x \mapsto x ^ { \sharp } .$, which sends t to$\beta .$On$\mathrm { K } ^ { \flat \circ }$, it is given by sending x to$\scriptstyle \operatorname* { l i m } _ { n \to \infty } y _ { n } ^ { p ^ { n } }$, where$\mathcal { V } _ { n } \in \mathrm { K } ^ { \circ }$is any lift of the image of$x ^ { 1 / \beta ^ { n } }$in $\mathrm { K } ^ { \flat \circ } / t = \mathrm { K } ^ { \circ } / \boldsymbol { \rho }$. Then one has an identification

$$
\mathrm{K} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{K},   x \mapsto \big (x ^ {\sharp}, \big (x ^ {1 / p} \big) ^ {\sharp}, \ldots \big).
$$

In order to prove the theorem, one has to construct a canonical finite extension$\mathrm { L } ^ { \sharp }$of K for any finite extension L of$\mathrm { K } ^ { \flat }$. There is the following description. Say L is the splitting field of a separable polynomial$\mathrm { X } ^ { d } + a _ { d - 1 } \mathrm { X } ^ { d - 1 } + \cdot \cdot \cdot + a _ { 0 }$, which is also the splitting field of$\mathrm { X } ^ { d } + a _ { d - 1 } ^ { 1 / \hat { p } ^ { n } } \mathrm { X } ^ { d - 1 } + \cdots + a _ { 0 } ^ { 1 / { p } ^ { n } }$for all$n \geq 0$. Then$\mathrm { L } ^ { \sharp }$can be defined as the splitting field of$\mathbf { \partial } \cdot \mathbf { X } ^ { d } + ( a _ { d - 1 } ^ { 1 / p ^ { n } } ) ^ { \sharp } \mathbf { X } ^ { d - 1 } + \cdots + ( a _ { 0 } ^ { 1 / p ^ { n } } ) ^ { \sharp }$for n large enough: these fields stabilize as$n \to \infty$

In fact, the same ideas work in greater generality.

Definition 1.2. — A perfectoid field is a complete topological field K whose topology is induced by a nondiscrete valuation of rank 1, such that the Frobenius$\Phi$is surjective on$\mathrm { K } ^ { \circ } /  { p } .$

Here$\mathrm { K } ^ { \circ } \subset \mathrm { K }$denotes the set of powerbounded elements. Generalizing the example above, a construction of Fontaine associates to any perfectoid field K another perfectoid field$\mathrm { K } ^ { \flat }$ofcharacteristic$\beta ,$whose underlying multiplicative monoid can be described as

$$
\mathrm{K} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{K}.
$$

The theorem above generalizes to the following result.

## Theorem 1.3. — The absolute Galois groups of K and$\mathrm { K } ^ { \flat }$are canonically isomorphic.

Our aim is to generalize this to a comparison of geometric objects over K with geometric objects over$\mathrm { K } ^ { \flat }$. The basic claim is the following.

Claim 1.4. — The affine line$\mathbf { A } _ { \mathrm { K } ^ { \flat } } ^ { 1 }$‘is equal$t o ^ { \bullet }$the inverse limit lim$\mathbf { \Gamma } _ { \mathrm { T } \mapsto \mathrm { T } ^ { p } } \mathbf { A } _ { \mathrm { K } } ^ { 1 } .$, where T is the coordinate on${ \bf A } ^ { 1 }$

One way in which this is correct is the observation that it is true on$\mathrm { K } ^ { \flat _ { - } } ;$, resp.$\mathrm { K } \mathfrak { - } ,$ valued points. Moreover, for any finite extension L of K corresponding to an extension

L<sup>-</sup> of$\mathrm { K } ^ { \flat }$, we have the same relation

$$
\mathrm{L} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{L}.
$$

Looking at the example above, we see that the explicit description of the map between $\mathbf { A } _ { \mathrm { K } ^ { \flat } } ^ { 1 }$and$\varprojlim _ { \mathrm { \tiny { F }  T ^ { \flat } } } \mathbf { A } _ { \mathrm { K } } ^ { 1 }$involves a limit procedure. For this reason, a formalization of this isomorphism has to be of an analytic nature, and we have to use some kind of rigidanalytic geometry over K. We choose to work with Huber’s language of adic spaces, which reinterprets rigid-analytic varieties as certain locally ringed topological spaces. In particular, any variety X over K has an associated adic space$\mathrm { X ^ { a d } }$over K, which in turn has an underlying topological space$| \mathrm { X ^ { a d } } |$

Theorem 1.5. — There is a homeomorphism oftopological spaces

$$
\big|\big(\mathbf{A}_{\mathrm{K}^{\flat}}^{1}\big)^{\mathrm{ad}}\big|\cong \varprojlim_{\substack{\mathrm{T}\mapsto \mathrm{T}^{\flat}}} \big|\big(\mathbf{A}_{\mathrm{K}}^{1}\big)^{\mathrm{ad}}\big|.
$$

Note that both sides of this isomorphism can be regarded as locally ringed topological spaces. It is natural to ask whether one can compare the structure sheaves on both sides. There is the obvious obstacle that the left-hand side has a sheaf of characteristic$\boldsymbol { p }$ rings, whereas the right-hand side has a sheafofcharacteristic 0 rings. Fontaine’s functors make it possible to translate between the two worlds. There is the following result.

Definition 1.6. — Let K be a perfectoidfield. A perfectoid K-algebra is a Banach K-algebra R such that the set ofpowerbounded elements$\mathrm { R } ^ { \circ } \subset \mathrm { R }$is bounded, and such that the Frobenius  is surjective on$\mathrm { R } ^ { \circ } /  { p } .$

Theorem 1.7. — There is natural equivalence of categories, called the tilting equivalence, between the category ofperfectoid K-algebras and the category ofperfectoid K<sup>-</sup>-algebras. Here a perfectoid K-algebra R is sent to the perfectoid K<sup>-</sup>-algebra

$$
\mathrm{R} ^ {b} = \varprojlim_ {x \mapsto x ^ {b}} \mathrm{R}.
$$

We note in particular that for perfectoid K-algebras R, we still have a map $\mathbb { R } ^ { \flat } \to \mathbb { R } , f \mapsto f ^ { \sharp }$. An example of a perfectoid K-algebra is the algebra$\mathrm { R } = \mathrm { K } \langle \mathrm { T } ^ { 1 / p ^ { \infty } } \rangle$ for which$\mathrm { R } ^ { \circ } = \mathrm { K } ^ { \circ } \langle \mathrm { T } ^ { 1 / p ^ { \infty } } \rangle$is the p-adic completion of$\mathrm { K } ^ { \circ } [ \mathrm { T } ^ { 1 / p ^ { \infty } } ]$. This is the completion of an algebra that appears on the right-hand side of Theorem 1.5. Its tilt is given by $\mathrm { R } ^ { \flat } = \mathrm { K } ^ { \flat } \langle \mathrm { T } ^ { 1 / \flat ^ { \infty } } \rangle$, which is the completed perfection of an algebra that appears on the left-hand side of Theorem 1.5.

Now an affinoid perfectoid space is associated to a perfectoid affinoid K-algebra, which is a pair (R, R<sup>+</sup>), where R is a perfectoid K-algebra, and$\mathrm { R } ^ { + } \subset \mathrm { R } ^ { \circ }$is open and integrally closed (and often$\mathrm { R } ^ { + } = \mathrm { R } ^ { \circ } )$. There is a natural way to form the tilt$( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } )$

To such a pair$( \mathrm { R } , \mathrm { R } ^ { + } )$, Huber [19] associates a space$\mathrm { X = S p a ( R , R ^ { + } ) }$of equivalence classes of continuous valuations$\mathrm { R }  \Gamma \cup \{ 0 \} , f \mapsto | f ( x ) |$, which are$\leq 1$on$\mathrm { R ^ { + } }$. The topology on this space is generated by so-called rational subsets. Moreover, Huber defines presheaves$\mathcal { O } _ { \mathrm { X } }$and$\mathcal { O } _ { \mathrm { X } } ^ { + }$on X, whose global sections are R, resp.$\mathrm { R } ^ { + }$

Theorem 1.${ \bf 3 . } - L e t \left( { \bf R , R ^ { + } } \right)$be a perfectoid affinoid K-algebra, and let$\mathrm { X = S p a ( R , R ^ { + } ) }$, $\mathrm { X ^ { \flat } = S p a ( R ^ { \flat } , R ^ { \flat + } ) }$

(i) There is a homeomorphism$\mathrm { X } \cong \mathrm { X } ^ { \mathrm { b } }$, given by mapping$x \in \mathrm { X }$to the valuation$x ^ { \mathrm { { b } } } \in \mathrm { { X } } ^ { \mathrm { { b } } }$ defined by$| f ( x ^ { \flat } ) | = | f ^ { \sharp } ( x ) |$. This homeomorphism identifies rational subsets.

(ii) For any rational subset$\mathrm { ~ U ~ } \subset \mathrm { ~ X ~ }$with tilt$\mathrm { U } ^ { \mathrm { p } } \subset \mathrm { X } ^ { \mathrm { p } }$, the pair$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$is a perfectoid affinoid K-algebra with tilt$( \mathcal { O } _ { \mathrm { { X ^ { \flat } } } } ( \mathrm { { U ^ { \flat } } } ) , \mathcal { O } _ { \mathrm { { X ^ { \flat } } } } ^ { + } ( \mathrm { { U ^ { \flat } } } ) )$

(iii) The presheaves$\mathcal { O } _ { \mathrm { X } } , \mathcal { O } _ { \mathrm { X } } ^ { + }$are sheaves.

(iv) The cohomology group$\mathrm { H } ^ { i } ( \mathrm { X } , \mathcal { O } _ { \mathrm { X } } ^ { + } )$is m-torsionfor$i > 0$

Here m$\subset \mathrm { K } ^ { \circ }$is the subset of topologically nilpotent elements. Part$( \mathrm { i v } )$implies that $\mathrm { H } ^ { i } ( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } ) = 0$for$i > 0$, which gives Tate’s acyclicity theorem in the context ofperfectoid spaces. However, it says that this statement about the generic fibre extends almost to the integral level, in the language of Faltings’s so-called almost mathematics. In fact, this is a general property ofperfectoid objects: Many statements that are true on the generic fibre are automatically almost true on the integral level.

Using the theorem, one can define general perfectoid spaces by gluing affinoid perfectoid spaces$\mathrm { X = S p a ( R , R ^ { + } ) }$. We arrive at the following theorem.

Theorem 1.9. — The category ofperfectoid spaces over K and the category ofperfectoid spaces over$\mathrm { K } ^ { \flat }$are equivalent.

We denote the tilting functor by$\mathrm { X } \mapsto \mathrm { X } ^ { \flat }$. Our next aim is to define an étale topos ofperfectoid spaces. This necessitates a generalization ofFaltings’s almost purity theorem, cf. [11], [12].

Theorem 1.10. — Let R be a perfectoid K-algebra. Let$\mathrm { S } / \mathrm { R }$be finite étale. Then S is a perfectoid K-algebra, and$\mathrm { S } ^ { \circ }$is almost finite étale over$\mathrm { R } ^ { \circ }$

Remark 1.11. — Let us sketch the relation to Faltings’s almost purity theorem, in the way it is usually stated. For simplicity, we do only the smooth case. Assume that K is of characteristic 0. One starts with$\mathbf { \tilde { R } } _ { 0 } = \mathbf { \check { K } } ^ { \circ } \langle \mathbf { T } _ { 1 } ^ { \pm 1 } , \dots , \mathbf { \check { T } } _ { d } ^ { \pm 1 } \rangle$, and forms the ring

$$
\mathrm{R} _ {n} = \mathrm{K} ^ {\circ} \big \langle \mathrm{T} _ {1} ^ {\pm 1 / p ^ {n}}, \ldots , \mathrm{T} _ {d} ^ {\pm 1 / p ^ {n}} \big \rangle ,
$$

which are finite over$\mathrm { R _ { 0 } } .$, and finite étale after invertingp. Let$\mathrm { R } _ { \infty }$denote the direct limit of the$\mathrm { R } _ { n } ,$, and let$\hat { \mathrm { R } } _ { \infty }$be its p-adic completion. Then$\begin{array} { r } { \mathrm { R } = \hat { \mathrm { R } } _ { \infty } [ \frac { 1 } { \mathit { \Pi } _ { b } } ] } \end{array}$is a perfectoid K-algebra. Faltings’s almost purity theorem, [11, Theorem 3.1], says that if$\mathrm { S } _ { n }$is a finite normal $\mathrm { R } _ { n }$-algebra which is étale after inverting${ p , }$and one defines$\mathrm { S } _ { m }$as the integral closure of $\mathrm { R } _ { m }$in$( \mathrm { S } _ { n } \otimes _ { \mathrm { R } _ { n } } \mathrm { R } _ { m } ) [ { \boldsymbol { \rho } } ^ { - 1 } ]$for$m \geq n _ { \because }$, then the direct limit$\mathrm { S } _ { \infty }$of the$\mathrm { S } _ { m }$is almost finite étale over$\mathrm { R } _ { \infty }$. If one defines$\mathbf { S } = \mathbf { S } _ { n } \otimes _ { \mathbf { R } _ { n } } \mathbf { R }$, then S is finite étale over R, and our version of the almost purity theorem says that$\mathrm { S } ^ { \circ }$is almost finite étale over$\mathrm { R } ^ { \circ } = \hat { \mathrm { R } } _ { \infty }$. One deduces that $\mathrm { S } ^ { \circ } = \hat { \mathrm { S } } _ { \infty } ^ { \bar { } } .$, and that also$\mathrm { S } _ { \infty }$is almost finite étale over$\mathrm { R } _ { \infty }$

Similar results are known in log-smooth situations, cf. [12, §2b], and we refer to the book project of Gabber and Ramero [14] for the most general results along these lines. Our result is stronger in two ways: First, e.g. in applications to p-adic Hodge theory, one may get rid ofassumptions about the reduction type ofthe variety, such as semistable or just log-smooth. Some applications along these lines are given in [31]. Secondly, it applies in situations where the perfectoid algebra R is not a completed increasing union of certain distinguished topologically finitely generated subalgebras along nice transition maps.

Let us sketch the proof of the almost purity theorem. It is easy if K is of characteristic$\beta .$Moreover, as for perfectoid fields, it is easy to construct a fully faithful functor from the category of finite étale R<sup>-</sup>-algebras to finite étale R-algebras, and the problem becomes to show that this functor is essentially surjective. But locally on$\mathrm { X = S p a ( R , R ^ { + } ) }$, the functor is essentially surjective by the result for perfectoid fields; one deduces the general case by a gluing argument. The analytic theory of perfectoid spaces is precisely what is needed to make this localization argument.

In particular, we note that Theorem 1.10 is essentially equivalent to the comparison of finite étale covers of$\mathrm { X }$and its tilt$\mathrm { X } ^ { \flat }$. Slightly stronger, one proves the following theorem. Here,$\mathrm { X } _ { \mathrm { e t } }$denotes the étale site of a perfectoid space$\mathrm { X } ,$, and we denote by$\mathrm { X _ { \mathrm { e t } } ^ { \sim } }$ the associated topos.

Theorem 1.12. — Let X be a perfectoid space over K with tilt$\mathrm { X } ^ { \flat }$over K<sup>-</sup>. Then tilting induces an equivalence ofsites$\mathrm { X } _ { \mathrm { e t } } \cong \mathrm { X } _ { \mathrm { e t } } ^ { \flat }$

As a concrete application of this theorem, we have the following result. Here, we use the étale topoi of adic spaces, which are the same as the étale topoi of the corresponding rigid-analytic variety. In particular, the same theorem holds for rigid-analytic varieties.

Theorem 1.13. — The étale topos$( \mathbf { P } _ { \mathrm { K } ^ { \mathrm { p } } } ^ { n , \mathrm { a d } } ) _ { \mathrm { e t } } ^ { \sim }$is equivalent to the inverse limit$\varprojlim _ { \varphi } ( \mathbf { P } _ { \mathrm { K } } ^ { n , \mathrm { a d } } ) _ { \tilde { \mathrm { e t } } } ^ { \sim }$

Here, one has to interpret the latter as the inverse limit of a fibred topos in an obvious way, and$\varphi$is the map given on coordinates by$\varphi ( x _ { 0 } : \ldots : x _ { n } ) = ( x _ { 0 } ^ { \flat } : \ldots : x _ { n } ^ { \flat } )$ The same theorem stays true for proper toric varieties without change. We note that the theorem gives rise to a projection map

$$
\pi : \mathbf {P} _ {\mathrm{K} ^ {\flat}} ^ {n} \to \mathbf {P} _ {\mathrm{K}} ^ {n}
$$

defined on topological spaces and étale topoi of adic spaces, and which is given on coordinates by$\pi ( x _ { 0 } : \ldots : x _ { n } ) = ( x _ { 0 } ^ { \sharp } : \ldots : x _ { n } ^ { \sharp } )$. In particular, we see again that this isomorphism is of a deeply analytic and transcendental nature.

We note that$( \mathbf { P } _ { \mathrm { K } ^ { \mathrm { p } } } ^ { n } ) ^ { \mathrm { a d } }$is itself not a perfectoid space, but$\varprojlim _ { \varphi } ( \mathbf { P } _ { \mathrm { K } ^ { \flat } } ^ { n } ) ^ { \mathrm { a d } }$is, where $\varphi : \mathbf { P } _ { \mathrm { K } ^ { \flat } } ^ { n } \to \mathbf { P } _ { \mathrm { K } ^ { \flat } } ^ { n }$denotes again the${ \beta } ^ { \mathrm { - t h } }$power map on coordinates. However,$\varphi$is purely inseparable and hence induces an isomorphism on topological spaces and étale topoi, which is the reason that we have not written this inverse limit in Theorem 1.5 and The orem 1.13.

Finally, we apply these results to the weight-monodromy conjecture. Let us recall its formulation. Let$k$be a local field whose residue field is of characteristic$\beta ,$let$\mathbf { G } _ { k } =$ $\operatorname { G a l } ( { \bar { k } } / k )$, and let$q$be the cardinality of the residue field of$k .$. For any finite-dimensional Q<sup>¯</sup> -representation V of$\mathrm { G } _ { k } ,$we have the monodromy operator$\mathrm { N } : \mathrm { V } \to \mathrm { V } ( - 1 )$induced from the action of the -adic inertia subgroup. It induces the monodromy filtration $\mathrm { F i l } _ { i } ^ { \mathrm { N } } \mathrm { C } \mathrm { V } , i \in \mathbf { Z } .$characterized by the property that$\mathrm { N } ( \mathrm { F i l } _ { i } ^ { \mathrm { N } } \mathrm { V } ) \subset \mathrm { F i l } _ { i - 2 } ^ { \mathrm { N } } \mathrm { V } ( \dot { - } 1 )$for all $i \in \mathbf { Z }$and$\mathrm { g r } _ { i } ^ { \mathrm { N } } \mathrm { V } \cong \mathrm { g r } _ { - i } ^ { \mathrm { N } } \mathrm { V } ( - i )$via$\mathrm { N } ^ { i }$for all$i \geq 0$

Conjecture 1.14 (Deligne$[ 9 ] ) . - L e t \mathrm { ~ X ~ }$be a proper smooth variety over$k ,$and let$\mathrm { V } =$ H$( \mathrm { X } _ { \bar { k } } , \bar { \mathbf { Q } } _ { \ell } )$. Then for all$j \in \mathbf { Z }$andfor any geometric Frobenius$\Phi \in \mathrm { G } _ { k } ,$all eigenvalues of$\Phi$on $\mathrm { g r } _ { j } ^ { \mathrm { N } } \mathrm { V }$are Weil numbers ofweight$i + j$, i.e. algebraic numbers α such that$| \alpha | = q ^ { ( i + j ) / 2 }$for all complex absolute values.

Deligne [10], proved this conjecture if k is of characteristic$\beta ,$and the situation is already defined over a curve. The general weight-monodromy conjecture over fields k of characteristic$\boldsymbol { p }$can be deduced from this case, as done by Terasoma [35] and by Ito [27].

In mixed characteristic, the conjecture is wide open. Introducing what is now called the Rapoport-Zink spectral sequence, Rapoport and Zink [30] have proved the conjecture when X has dimension at most 2 and X has semistable reduction. They also show that in general it would follow from a suitable form of the standard conjectures, the main point being that a certain linear pairing on cohomology groups should be non-degenerate. Using de Jong’s alterations, [8], one can reduce the general case to the case of semistable reduction, and in particular the case of dimension at most 2 follows. Apart from that, other special cases are known. Notably, the case of varieties which admit p-adic uniformization by Drinfeld’s upper half-space is proved by Ito [26] by pushing through the argument of Rapoport-Zink in this special case, making use of the special nature of the components of the special fibre, which are explicit rational varieties.

On the other hand, there is a large amount of activity that uses automorphic arguments to prove results in cases of certain Shimura varieties, notably those of type $\mathrm { U } ( 1 , n - 1 )$used in the book of Harris-Taylor [16]. Let us only mention the work of Taylor and Yoshida [34] later completed by Shin [32] and Caraiani [6] as well as the independent work of Boyer [4, 5]. Boyer’s results were used by Dat [7] to handle the case ofvarieties which admit uniformization by a covering ofDrinfeld’s upper half-space, thereby generalizing Ito’s result.

Our last main theorem is the following.

Theorem 1.15. — Let k be a localfield ofcharacteristic 0. Let X be a geometrically connected proper smooth variety over k such that X is a set-theoretic complete intersection in a projective smooth toric variety. Then the weight-monodromy conjecture is truefor X.

Let us give a short sketch of the proof for a smooth hypersurface X in$\mathbf { P } ^ { n }$, which is already a new result. We have the projection

$$
\pi : \mathbf {P} _ {\mathrm{K} ^ {\flat}} ^ {n} \to \mathbf {P} _ {\mathrm{K}} ^ {n},
$$

and we can look at the preimage$\pi ^ { - 1 } ( \mathrm { X } )$. One has an injective map$\mathrm { H } ^ { i } ( \mathrm { X } )$ $\mathrm { H } ^ { i } ( \pi ^ { - 1 } ( \mathrm { X } ) )$, and if$\pi ^ { - 1 } ( \mathrm { X } )$were an algebraic variety, then one could deduce the result from Deligne’s theorem in equal characteristic. However, the map π is highly transcendental, and$\pi ^ { - 1 } ( \mathrm { X } )$will not be given by equations. In general, it will look like some sort of fractal, have infinite-dimensional cohomology, and will have infinite degree in the sense that it will meet a line in infinitely many points. As an easy example, let

$$
\mathbf {X} = \{x _ {0} + x _ {1} + x _ {2} = 0 \} \subset (\mathbf {P} _ {\mathrm{K}} ^ {2}) ^ {\mathrm{ad}}.
$$

Then the homeomorphism

$$
\big | \big (\mathbf {P} _ {\mathrm{K} ^ {\flat}} ^ {2} \big) ^ {\mathrm{ad}} \big | \cong \varprojlim_ {\varphi} \big | \big (\mathbf {P} _ {\mathrm{K}} ^ {2} \big) ^ {\mathrm{ad}} \big |
$$

means that$\pi ^ { - 1 } ( \mathrm { X } )$is topologically the inverse limit of the subvarieties

$$
\mathrm{X} _ {n} = \left\{x _ {0} ^ {p ^ {n}} + x _ {1} ^ {p ^ {n}} + x _ {2} ^ {p ^ {n}} = 0 \right\} \subset \left(\mathbf {P} _ {\mathrm{K}} ^ {2}\right) ^ {\mathrm{ad}}.
$$

However, we have the following crucial approximation lemma.

Lemma 1.$\mathbf { 1 6 . } \mathrm { ~ \_ ~ } L e t \tilde { \mathbf { X } } \subset ( \mathbf { P } _ { \mathrm { K } } ^ { n } ) ^ { \mathrm { a d } }$be a small open neighborhood of the hypersurface X. Then there is a hypersurface$\mathrm { Y } \subset \pi ^ { - 1 } ( \tilde { \mathrm { X } } )$

The proof of this lemma is by an explicit approximation algorithm for the homogeneous polynomial defining X, and is the reason that we have to restrict to complete intersections. Using a result of Huber, one finds some$\tilde { \mathrm { X } }$such that$\mathrm { H } ^ { i } ( \mathrm { X } ) = \mathrm { H } ^ { i } ( \tilde { \mathrm { X } } )$, and hence gets a map$\mathrm { H } ^ { i } ( \mathrm { X } ) = \mathrm { H } ^ { i } ( \tilde { \mathrm { X } } )  \mathrm { H } ^ { i } ( \mathrm { Y } )$). As before, one checks that it is injective and concludes.

After the results of this paper were first announced, Kiran Kedlaya informed us that he had obtained related results in joint work with Ruochuan Liu [28]. In particular, in our terminology, they prove that for any perfectoid K-algebra R with tilt$\mathrm { R } ^ { \flat }$, there is an equivalence between the finite étale R-algebras and the finite étale R<sup>-</sup>-algebras. However, the tilting equivalence, the generalization of Faltings’s almost purity theorem and the application to the weight-monodromy conjecture were not observed by them. This led to an exchange of ideas, with the following two influences on this paper. In the first version of this work, Theorem 1.3 was proved using a version of Faltings’s almost purity theorem for fields, proved in [15], Chapter 6, using ramification theory. Kedlaya observed that one could instead reduce to the case where$\mathrm { K } ^ { \flat }$is algebraically closed, which gives a more elementary proof of the theorem. We include both arguments here. Secondly, a certain finiteness condition on the perfectoid K-algebra was imposed at some places in the first version, a condition close to the notion of p-finiteness introduced below; in most applications known to the author, this condition is satisfied. Kedlaya made us aware of the possibility to deduce the general case by a simple limit argument.

## 2. Adic spaces

Throughout this paper, we make use of Huber’s theory of adic spaces. For this reason, we recall some basic definitions and statements about adic spaces over nonarchimedean local fields. We also compare Huber’s theory to the more classical language of rigid-analytic geometry, and to the theory of Berkovich’s analytic spaces. The material of this section can be found in [22], [20] and [19].

Definition 2.1. — A nonarchimedeanfield is a topologicalfield k whose topology is induced by a nontrivial valuation ofrank 1.

In particular, k admits a norm$| \cdot | : k \to \mathbf { R } _ { \geq 0 }$, and it is easy to see that$| \cdot |$is unique up to automorphisms$x \mapsto x ^ { \alpha } , 0 < \alpha < \infty .$, of$\mathbf { R } _ { \geq 0 }$

Throughout, we fix a nonarchimedean field k. Replacing k by its completion will not change the theory, so we may and do assume that k is complete.

The idea of rigid-analytic geometry, and the closely related theories of Berkovich’s analytic spaces and Huber’s adic spaces, is to have a nonarchimedean analogue of the notion of complex analytic spaces over C. In particular, there should be a functor

$$
\{\text {varieties} / k \} \to \{\text {adic spaces} / k \}: X \mapsto X ^ {\text {ad}},
$$

sending any variety over$k$to its analytification$\mathrm { X ^ { a d } }$. Moreover, it should be possible to define subspaces of$\mathrm { \Delta X ^ { \mathrm { a d } } }$by inequalities: For any$f \in \Gamma ( \mathrm { X } , \mathcal { O } _ { \mathrm { X } } )$, the subset

$$
\left\{x \in \mathrm{X} ^ {\mathrm{ad}} \mid | f (x) | \leq 1 \right\}
$$

should make sense. In particular, any point$x \in \mathrm { X } ^ { \mathrm { a d } }$should give rise to a valuation function $f \mapsto | f ( x ) |$. In classical rigid-analytic geometry, one considers only the maximal points of the scheme$\mathrm { X } .$. Each ofthem gives a map$\Gamma ( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } ) \to k ^ { \prime }$for some finite extension$k ^ { \prime }$of$\mathrm { \nabla } k ; \mathrm { \nabla }$ composing with the unique extension of the absolute value of k to$k ^ { \prime }$gives a valuation on $\Gamma ( \mathbf { X } , \mathcal { O } _ { \mathrm { X } } )$. In Berkovich’s theory, one considers norm maps$\Gamma ( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } ) \to \mathbf { R } _ { \geq 0 }$inducing a fixed norm map on k. Equivalently, one considers valuations of rank 1 on$\Gamma ( \mathbf { X } , \mathcal { O } _ { \mathrm { X } } )$ In Huber’s theory, one allows also valuations of higher rank.

Definition 2.2. — Let R be some ring. A valuation on R is given by a multiplicative map $| \cdot | : \mathbb { R } \to \Gamma \cup \{ 0 \}$, where  is some totally ordered abelian group, written multiplicatively, such that $| 0 | = 0 , | 1 | = 1$and$| x + y | \leq \operatorname* { m a x } ( | x | , | y | )$for all$x , y \in \mathrm { R }$

IfR is a topological ring, then a valuation$| \cdot |$on R is said to be continuous iffor all$\gamma \in \Gamma$, the subset$\{ x \in \mathbf { R } \mid | x | < \gamma \} \subset \mathbf { R }$is open.

Remark 2.3. — The term valuation is somewhat unfortunate: If$\Gamma = \mathbf { R } _ { > 0 } ,$, then this would usually be called a seminorm, and the term valuation would be used for (a constant multiple of) the map$x \mapsto - \log | x |$. On the other hand, the term higher-rank norm is much less commonly used than the term higher-rank valuation. For this reason, we stick with Huber’s terminology.

Remark 2.4. — Recall that a valuation ring is an integral domain R such that for any$x \neq 0$in the fraction field K ofR, at least one ofx and$x ^ { - 1 }$is in R. Any valuation |·| on a field K gives rise to the valuation subring$\mathrm { R } = \{ x \mid | x | \leq 1 \}$. Conversely, a valuation ring R gives rise to a valuation on K with values in$\Gamma = \mathrm { K ^ { \times } / R ^ { \times } }$, ordered by saying that$x \leq y$ if$x = y z$for some$z \in \mathrm { R }$. With respect to a suitable notion of equivalence of valuations defined below, this induces a bijective correspondence between valuation subrings of K and valuations on K.

$\operatorname { I f } | \cdot | : \mathbb { R } \to \Gamma \cup \{ 0 \}$is a valuation on R, let$\Gamma _ { | \cdot | } \subset \Gamma$denote the subgroup generated by all$| x | , x \in \mathrm { R }$, which are nonzero. The set supp$( | \cdot | ) = \{ x \in \mathbf { R } \mid | x | = 0 \}$is a prime ideal of R called the support of | · |. Let K be the quotient field of$\mathrm { R } / \operatorname { s u p p } ( | \cdot | )$. Then the valuation factors as a composite$\mathrm { R \to K \to \Gamma \cup \{ 0 \} }$. Let$\operatorname { R } ( | \cdot | ) \subset \operatorname { K }$be the valuation subring, i.e.$\mathrm { R } ( | \cdot | ) = \{ x \in \mathrm { K } | | x | \leq 1 \}$

Definition 2.5. — Two valuations$| \cdot | , | \cdot | ^ { \prime }$are called equivalent if the following equivalent conditions are satisfied.

(i) There is an isomorphism of totally ordered groups α :$\Gamma _ { | \cdot | } \cong \Gamma _ { | \cdot | ^ { \prime } }$such that$| \cdot | ^ { \prime } { = } \alpha \circ | \cdot |$

(ii) The supports$\operatorname { s u p p } ( | \cdot | ) = \operatorname { s u p p } ( | \cdot | ^ { \prime } )$and valuation rings$\operatorname { R } ( | \cdot | ) = \operatorname { R } ( | \cdot | ^ { \prime } )$agree.

(iii) For all$a , b \in \mathbf { R } , | a | \geq | b |$if and only${ j f | a | ^ { \prime } \geq | b | ^ { \prime } }$

In [19], Huber defines spaces of (continuous) valuations in great generality. Let us specialize to the case of interest to us.

Definition 2.6.

(i) A Tate k-algebra is a topological k-algebra R for which there exists a subring$\mathrm { R } _ { 0 } \subset \mathrm { R }$ such that aR${ \sf \Phi } _ { \sf ( 0 ) } , a \in k ^ { \sf \times }$, forms a basis of open neighborhoods of 0. A subset M$\subset \mathbf { R }$is called bounded$i f \mathbf { M } \subset a \mathbf { R } _ { 0 } .$for some$a \in k ^ { \times }$. An element$x \in \mathrm { R }$is calledpower-bounded if $\{ x ^ { n } \mid n \geq 0 \} \subset \mathbf { R }$is bounded. Let$\mathrm { R } ^ { \circ } \subset \mathrm { R }$denote the subring ofpowerbounded elements; it is an open and integrally closed subring of R.

(ii) An affinoid k-algebra is a pair$( \mathrm { R } , \mathrm { R } ^ { + } )$consisting of a Tate k-algebra R and an open and integrally closed subring$\mathrm { R } ^ { + } \subset \mathrm { R } ^ { \circ }$

(iii) An affinoid k-algebra (R, R<sup>+</sup>) is said to be of topologically finite type (tft for short) if R is a quotient o$^ { c } k \langle \mathrm { T } _ { 1 } , \dots , \mathrm { T } _ { n } \rangle$for some n, and$\mathrm { R } ^ { + } = \mathrm { R } ^ { \circ }$

Here,

$$
k \langle \mathrm{T} _ {1}, \dots , \mathrm{T} _ {n} \rangle = \left\{\sum_ {i _ {1}, \dots , i _ {n} \geq 0} x _ {i _ {1}, \dots , i _ {n}} \mathrm{T} _ {1} ^ {i _ {1}} \dots \mathrm{T} _ {n} ^ {i _ {n}} \mid x _ {i _ {1}, \dots , i _ {n}} \in k, x _ {i _ {1}, \dots , i _ {n}} \rightarrow 0 \right\}
$$

is the ring of convergent power series on the ball given by$| \mathrm { T } _ { 1 } | , \ldots , | \mathrm { T } _ { n } | \leq 1$. Often, only affinoid k-algebras of tft are considered; however, this paper will show that other classes of affinoid k-algebras are of interest as well. Also, we will often take$\mathrm { R } ^ { + } = \mathrm { R } ^ { \circ }$，but there are two important reasons for allowing more general subrings. One reason is that points of the adic space give rise to pairs$( \mathrm { L } , \mathrm { L } ^ { + } )$, where L is some nonarchimedean extension of$\mathrm { K } ,$and$\mathrm { L } ^ { + } \subset \mathrm { L } ^ { \circ }$is an open valuation subring, cf. Proposition 2.27. If the valuation corresponding to this point is not of height 1, we will have$\mathrm { L } ^ { + } \neq \mathrm { L } ^ { \circ }$. The other reason is that the condition$\mathrm { R } ^ { + } = \mathrm { R } ^ { \circ }$is not always preserved under passage to a rational subdomain.

We also note that any Tate k-algebra R, resp. affinoid k-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$, admits the completion$\hat { \mathrm { R } } ,$resp.$( \hat { \textmd R } , \hat { \textmd R } ^ { + } )$, which is again a Tate, resp. affinoid, k-algebra. Everything depends only on the completion, so one may assume that$( \mathrm { R } , \mathrm { R } ^ { + } )$is complete in the following.

Definition 2.7.$- \angle e t ( { \bf R } , { \bf R } ^ { + } )$be an affinoid k-algebra. Let

$$
\mathrm{X} = \operatorname{Spa} \left(\mathrm{R}, \mathrm{R} ^ {+}\right) = \left\{\mid \cdot \mid : \mathrm{R} \rightarrow \Gamma \cup \{0 \} \text { continuous   valuation } \mid \right.
$$

$$
\forall f \in \mathrm{R} ^ {+}: | f | \leq 1 \} / \cong .
$$

For any$x \in \mathrm { X }$, write$f \mapsto | f ( x ) | f o r$the corresponding valuation on R. We equip X with the topology which has the open subsets

$$
\mathrm{U} \left(\frac {f _ {1} , \dots , f _ {n}}{g}\right) = \left\{x \in \mathrm{X} \mid \forall i: | f _ {i} (x) | \leq | g (x) | \right\},
$$

called rational subsets, as basisfor the topology, where$f _ { 1 } , \ldots , f _ { n } \in \mathbb { R }$generate R as an ideal and$g \in \mathbb { R }$

Remark 2.8. — Let$\varpi \in k$be topologically nilpotent, i.e.$| \varpi | < 1$. Then$\mathrm { t o } f _ { 1 } , \ldots , f _ { n }$ one can add$f _ { n + 1 } = \varpi ^ { \mathrm { N } }$for some big integer N without changing the rational subspace. Indeed, there are elements$h _ { 1 } , \ldots , h _ { n } \in \mathbf { R }$such that$\sum h _ { i } f _ { i } = 1$. Multiplying by$\varpi ^ { \mathrm { N } }$for N sufficiently large, we have$\varpi ^ { \mathrm { N } } h _ { i } \in \mathrm { R } ^ { + } , \mathrm { a s ~ } \mathrm { R } ^ { + } \subset \mathrm { R }$is open. Now for any$x \in \operatorname { U } ( { \frac { f _ { 1 } , \ldots { } { } \mathcal { f } _ { n } } { g } } )$, we have

$$
\left| \varpi^ {\mathrm{N}} (x) \right| = \left| \sum \left(\varpi^ {\mathrm{N}} h _ {i}\right) (x) f _ {i} (x) \right| \leq \max \left| \left(\varpi^ {\mathrm{N}} h _ {i}\right) (x) \right| \left| f _ {i} (x) \right| \leq \left| g (x) \right|,
$$

as desired. In particular, we see that on rational subsets,$| g ( x ) |$is nonzero, and bounded from below.

The topological spaces$\mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$have some special properties reminiscent ofthe properties of Spec(A) for a ring A. In fact, let us recall the following result of Hochster [18].

Definition/Proposition 2.9. — A topological space X is called spectral ifit satisfies thefollowing equivalent properties.

(i) There is some ring A such that$\mathrm { { X } \cong \mathrm { { S p e c ( A ) } } }$

(ii) One can write X as an inverse limit offinite$\mathrm { { T _ { 0 } } }$spaces.

(iii) The space X is quasicompact, has a basis ofquasicompact open subsets stable underfinite intersections, and every irreducible closed subset has a unique generic point.

In particular, spectral spaces are quasicompact, quasiseparated and$\mathrm { { T _ { 0 } } }$. Recall that a topological space X is called quasiseparated ifthe intersection ofany two quasicompact open subsets is again quasicompact. In the following we will often abbreviate quasicompact, resp. quasiseparated, as qc, resp. qs.

Proposition 2.10 [19, Theorem 3.5]. — For any affinoid k-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$, the space $\mathrm { S p a } ( \mathbf { R } , \mathbf { R } ^ { + } )$is spectral. The rational subsets form a basis of quasicompact open subsets stable underfinite intersections.

Proposition 2.11 [19, Proposition$3 . 9 7 . \mathrm { ~ - ~ } L e t \left( \mathrm { R } , \mathrm { R } ^ { + } \right)$be an affinoid k-algebra with completion$( \hat { \textmd R } , \hat { \textmd R } ^ { + } )$. Then$\mathrm { S p a } ( \mathrm { R } , \bar { \mathrm { R } ^ { + } } ) \cong \mathrm { S p a } ( \hat { \mathrm { R } } , \hat { \mathrm { R } ^ { + } } )$), identifying rational subsets.

Moreover, the space$\mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$is large enough to capture important properties.

Proposition$2 . 1 2 . - L e t \left( \mathrm { R } , \mathrm { R } ^ { + } \right)$be an affinoid k-algebra,$\mathrm { X = S p a ( R , R ^ { + } ) }$

(i)$\begin{array} { r } { I f \mathrm { X } = \varnothing , t h e n \hat { \mathrm { R } } = 0 . } \end{array}$

(ii)$L e t f \in \mathbb { R }$be such that$| f ( x ) | \neq 0 f o r$all$x \in \mathrm { X } .$. IfR is complete, thenf is invertible.

(iii)$L e t f \in \mathbb { R }$be such that$| f ( x ) | \leq 1$for all$x \in \mathrm { X }$. Then$f \in \mathbb { R } ^ { + }$

Proof. — Part (i) is [19], Proposition 3.6(i). Part (ii) is [20], Lemma 1.4, and part (iii) follows from [19], Lemma 3.3(i).-

We want to endow$\mathrm { X = S p a ( R , R ^ { + } ) }$with a structure sheaf$\mathcal { O } _ { \mathrm { X } }$. The construction is as follows.

Definition 2.13. — Let$( \mathrm { R } , \mathrm { R } ^ { + } )$be an affinoid k-algebra, and let$\mathrm { U } = \mathrm { U } ( \frac { f _ { 1 } , \dots , f _ { n } } { g } ) \subset \mathrm { X } =$ $\mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$be a rational subset. Choose some$\mathrm { R } _ { 0 } \subset \mathrm { R }$such that$a \mathbf { R } _ { 0 } , a \in k ^ { \times }$, is a basis of open neighborhoods of 0 in R. Consider the subalgebra$\mathrm { R } [ \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } ]$of$\mathrm { R } [ g ^ { - 1 } ]$, and equip it with the topology making a$\mathsf { R } _ { 0 } [ \frac { f _ { 1 } } { g } , \dots , \frac { f _ { n } } { g } ] , a \in k ^ { \times }$, a basis ofopen neighborhoods of0. Let$\mathbf { B } \subset \mathbf { R } [ \textstyle { \frac { f _ { 1 } } { g } } , \dotsc , \textstyle { \frac { f _ { n } } { g } } ]$ be the integral closure of$\mathrm { R } ^ { + } [ \frac { \bar { f } _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } ]$in$\mathbb { R } [ \frac { f _ { 1 } } { g } , \dots , \frac { f _ { n } } { g } ]$. Then$( \mathbf { R } [ \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } ] , \mathbf { B } )$is an affinoid k-algebra. Let$( \mathbf { R } \langle \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } \rangle , \hat { \mathbf { B } } )$be its completion.

Obviously,

$$
\operatorname{Spa} \left(\mathrm{R} \left\langle \frac {f _ {1}}{g}, \dots , \frac {f _ {n}}{g} \right\rangle , \hat {\mathrm{B}}\right)\rightarrow \operatorname{Spa} \left(\mathrm{R}, \mathrm{R} ^ {+}\right)
$$

factors over the open subset$\mathrm { U } \subset \mathrm { X } .$

Proposition 2.14 [20, Proposition$I . 3 ] . - I n$the situation of the definition, the following universal property is satisfied. For every complete affinoid k-algebra$( \mathrm { S } , \mathrm { S } ^ { + } )$with a map$( \mathrm { R } , \mathrm { R } ^ { + } )$ $( \mathrm { S } , \mathrm { S } ^ { + } )$such that the induced map Spa$( \mathrm { S } , \mathrm { S } ^ { + } )  \mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$factors over U, there is a unique map

$$
\left(\mathrm{R} \left\langle \frac {f _ {1}}{g}, \dots , \frac {f _ {n}}{g} \right\rangle , \hat {\mathrm{B}}\right)\rightarrow (\mathrm{S}, \mathrm{S} ^ {+})
$$

making the obvious diagram commute.

In particular,$( \mathrm { \bar { R } } \langle \frac { f _ { 1 } } { g } , \dots , \frac { f _ { n } } { g } \rangle$, B<sup>ˆ</sup> ) depends only on U. Define

$$
\left(\mathcal {O} _ {\mathrm{X}} (\mathrm{U}), \mathcal {O} _ {\mathrm{X}} ^ {+} (\mathrm{U})\right) = \left(\mathrm{R} \left\langle \frac {f _ {1}}{g}, \dots , \frac {f _ {n}}{g} \right\rangle , \hat {\mathrm{B}}\right).
$$

For example,$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { X } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { X } ) )$is the completion$\varrho f ( \mathrm { R } , \mathrm { R } ^ { + } )$

The idea is that since$f _ { 1 } , \ldots , f _ { n }$generate R, not all$| f _ { i } ( x ) | = 0$for$x \in \mathrm { U } ;$in particular,$| g ( x ) | \neq 0$for all$x \in \mathrm { U }$. This implies that g is invertible in S in the situation of the proposition. Moreover,$| ( \frac { f _ { i } } { g } ) ( x ) | \leq 1$for all$x \in \mathrm { U }$, which means that$\textstyle { \frac { f _ { i } } { g } } \in \mathrm { S } ^ { + }$

We define presheaves$\mathcal { O } _ { \mathrm { X } }$and$\mathcal { O } _ { \mathrm { X } } ^ { + }$on X as above on rational subsets, and for general open$\mathrm { U } \subset \mathrm { X }$by requiring

$$
\mathcal {O} _ {\mathrm{X}} (\mathrm{W}) = \varprojlim_ {\mathrm{U} \subset \mathrm{Wrational}} \mathcal {O} _ {\mathrm{X}} (\mathrm{U}),
$$

and similarly for$\mathcal { O } _ { \mathrm { X } } ^ { + }$

Proposition 2.15 [20, Lemma 1.5, Proposition$I . 6 J . - F o r \ a n y \ x \in \mathrm { X } .$, the valuation f → $| f ( x ) |$extends to the stalk$\mathcal { O } _ { \mathrm { X } , x } ,$, and

$$
\mathcal {O} _ {\mathrm{X}, x} ^ {+} = \left\{f \in \mathcal {O} _ {\mathrm{X}, x} \mid | f (x) | \leq 1 \right\}.
$$

The ring${ \mathcal { O } } _ { \mathrm { X } , }$is a local ring with maximal ideal given by$\smash { \{ f \mid \lvert f ( x ) \rvert = 0 \} }$. The ring$\mathcal { O } _ { \mathrm { X } , x } ^ { + }$is a local ring with maximal ideal given by$\smash { \{ f \mid | f ( x ) | < 1 \} }$. Moreover,for any open subset$\mathrm { ~ U ~ C ~ X ~ }$

$$
\mathcal {O} _ {\mathrm{X}} ^ {+} (\mathrm{U}) = \left\{f \in \mathcal {O} _ {\mathrm{X}} (\mathrm{U}) \mid \forall x \in \mathrm{U}: | f (x) | \leq 1 \right\}.
$$

$H \mathrm { U } \subset \mathrm { X }$is rational, then$\mathrm { U } \cong \mathrm { S p a } ( { \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } ) , { \mathcal { O } } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$compatible with rational subsets, the presheaves$\mathcal { O } _ { \mathrm { X } }$and$\mathcal { O } _ { \mathrm { X } } ^ { + }$, and the valuations at all$x \in \mathrm { U }$

Unfortunately, it is not in general known<sup>1</sup> that$\mathcal { O } _ { \mathrm { X } }$is sheaf. We note that the proposition ensures that$\mathcal { O } _ { \mathrm { X } } ^ { + }$is a sheaf if$\mathcal { O } _ { \mathrm { X } }$is. The basic problem is that completion behaves in general badly for nonnoetherian rings.

Definition 2.16. — A Tate k-algebra R is called strongly noetherian if

$$
\mathrm{R} \langle \mathrm{T} _ {1}, \ldots , \mathrm{T} _ {n} \rangle = \left\{\sum_ {i _ {1}, \ldots , i _ {n} \geq 0} x _ {i _ {1}, \ldots , i _ {n}} \mathrm{T} _ {1} ^ {i _ {1}} \dots \mathrm{T} _ {n} ^ {i _ {n}}   \Big |   x _ {i _ {1}, \ldots , i _ {n}} \in \hat {\mathrm{R}}, x _ {i _ {1}, \ldots , i _ {n}} \to 0 \right\}
$$

is noetherianfor all$n \geq 0$

For example, if R is of tft, then R is strongly noetherian.

Theorem 2.17 [20, Theorem$2 . 2 ] . - I f ( { \bf R } , { \bf R } ^ { + } )$is an affinoid k-algebra such that R is strongly noetherian, then$\mathcal { O } _ { \mathrm { X } }$is a sheaf.

Later, we will show that this theorem is true under the assumption that R is a perfectoid k-algebra. We define perfectoid k-algebras later; let us only remark that except for trivial examples, they are huge and in particular not strongly noetherian.

Finally, we can define the category of adic spaces over k. Namely, consider the category (V) of triples$( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } , ( | \cdot ( x ) | | x \in \mathrm { X } ) )$) consisting of a locally ringed topological space$( \mathrm { X } , \mathcal { O } _ { \mathrm { X } } )$, where$\mathcal { O } _ { \mathrm { X } }$is a sheafofcomplete topological k-algebras, and a continuous valuation$f \mapsto | f ( x ) |$on${ \mathcal { O } } _ { \mathrm { X } , x }$for every$x \in \mathrm { X }$. Morphisms are given by morphisms of locally ringed topological spaces which are continuous k-algebra morphisms on${ \mathcal { O } } _ { \mathrm { X } } ,$, and compatible with the valuations in the obvious sense.

Any affinoid k-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$for which$\mathcal { O } _ { \mathrm { X } }$is a sheaf gives rise to such a triple $( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } , ( | \cdot ( x ) | \mid x \in \mathrm { X } ) )$). Call an object of (V) isomorphic to such a triple an affinoid adic space.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup> And probably not true.</span></small>

Definition 2.18. — An adic space over k is an object$( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } , ( | \cdot ( x ) | | x \in \mathrm { X } ) )$of (V) that is locally on X an affinoid adic space.

Proposition 2.19 [20, Proposition$2 . I ( i i ) ] . -$For any affinoid k-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$with$\mathrm { X = }$ $\mathrm { S p a } ( \mathbf { R } , \mathbf { R } ^ { + } )$such that$\mathcal { O } _ { \mathrm { X } }$is a sheaf, and any adic space Y over k, we have

$$
\mathrm{Hom} (\mathrm{Y}, \mathrm{X}) = \mathrm{Hom} \bigl (\bigl (\hat {\mathrm{R}}, \hat {\mathrm{R}} ^ {+} \bigr), \bigl (\mathcal {O} _ {\mathrm{Y}} (\mathrm{Y}), \mathcal {O} _ {\mathrm{Y}} ^ {+} (\mathrm{Y}) \bigr) \bigr).
$$

Here, the latter set denotes the set of continuous k-algebra morphisms$\hat { \mathrm { R } }  \mathcal { O } _ { \mathrm { Y } } ( \mathrm { Y } )$such that$\hat { \mathrm { R } } ^ { + } \mathrm { \Delta } _ { i s }$ mapped into$\mathcal { O } _ { \mathrm { Y } } ^ { + } ( \mathrm { Y } )$

In particular, the category of complete affinoid k-algebras for which the structure presheaf is a sheaf is equivalent to the category of affinoid adic spaces over k.

For the rest of this section, let us discuss an example, and explain the relation to rigid-analytic varieties [33] and Berkovich’s analytic spaces [1].

Example 2.20. — Assume that k is complete and algebraically closed. Let$\mathrm { R } = k \langle \mathrm { T } \rangle$, $\mathbf { R } ^ { + } = \mathbf { R } ^ { \circ } = k ^ { \circ } \langle \mathrm { T } \rangle$the subspace of power series with coefficients in$k ^ { \circ }$. Then$( \mathrm { R } , \mathrm { R } ^ { + } )$is an affinoid k-algebra of tft. We want to describe the topological space$\mathrm { X = S p a ( R , R ^ { + } ) }$ For convenience, let us fix the norm$| \cdot | : k \to \mathbf { R } _ { \geq 0 }$. Then there are in general points of 5 different types, of which the first four are already present in Berkovich’s theory.

![](images/page_13_image_7.jpg)

(1) The classical points: Let$x \in k ^ { \circ }$, i.e.$x \in k$with$| x | \le 1$. Then for any$f \in k \langle \mathrm { T } \rangle$, we can evaluatef at x to get a map$\begin{array} { r } { \mathrm { R }  k , f = \sum a _ { n } \mathrm { T } ^ { n } \mapsto \sum a _ { n } x ^ { n } } \end{array}$. Composing with the norm on$k ,$one gets a valuation$f \mapsto | f ( x ) |$on R, which is obviously continuous and$\leq 1$ for all$f \in \mathrm { R } ^ { + }$

(2), (3) The rays of the tree: Let$0 \leq r \leq 1$be some real number, and$x \in k ^ { \circ }$. Then

$$
f = \sum a _ {n} (T - x) ^ {n} \mapsto \sup | a _ {n} | r ^ {n} = \sup _ {y \in k ^ {\circ}: | y - x | \leq r} | f (y) |
$$

defines another continuous valuation on R which is$\leq 1$for all$f \in \mathbb { R } ^ { + }$. It depends only on the disk$\mathrm { D } ( x , r ) = \{ y \in k ^ { \circ } \mid \lfloor y - x \vert \leq r \} . \mathrm { I f } r = 0$, then it agrees with the classical point corresponding to x. For$r = 1$, the disk$\mathrm { D } ( x , 1 )$is independent of$x \in k ^ { \circ }$, and the corresponding valuation is called the Gaußpoint.

If$\dot { \boldsymbol { r } } \in | \boldsymbol { k } ^ { \times } |$, then the point is said to be of type (2), otherwise of type (3). Note that a branching occurs at a point corresponding to the disk$Ḋ \mathrm { Ḋ ( } x , r ) Ḍ Ḍ$if and only if$r \in | k ^ { \times } |$, i.e. a branching occurs precisely at the points of type (2).

(4) Dead ends ofthe tree: Let$\mathrm { D } _ { 1 } \supset \mathrm { D } _ { 2 } \supset \cdots$be a sequence ofdisks with$\cap \mathrm { D } _ { i } = \emptyset$ Such families exist if k is not spherically complete, e.g. if$k = \mathbf { C } _ { \rho }$. Then

$$
f \mapsto \inf _ {i} \sup _ {x \in \mathrm{D} _ {i}} \left| f (x) \right|
$$

defines a valuation on$\mathrm { R } ,$which again is$\leq 1$for all$f \in \mathbb { R } ^ { + }$

(5) Finally, there are some valuations of rank 2 which are only seen in the adic space. Let us first give an example, before giving the general classification. Consider the totally ordered abelian group$\Gamma = \mathbf { R } _ { > 0 } \times \boldsymbol { \gamma } ^ { \mathbf { Z } }$, where we require that$r < \gamma < 1$for all real numbers$r < 1$. It is easily seen that there is a unique such ordering. Then

$$
f = \sum a _ {n} (\mathrm{T} - x) ^ {n} \mapsto \max | a _ {n} | \gamma^ {n}
$$

defines a rank-2-valuation on R. This is similar to cases$( 2 ) , ( 3 )$, but with the variable r infinitesimally close to 1. One may check that this point only depends on the disc$\mathrm { D } ( x , <$ $1 ) = \{ y \in k ^ { \circ } \mid | y - x | < 1 \}$

Similarly, take any$x \in k ^ { \circ }$, some real number$0 < r < 1$and choose a sign$? \in$ $\{ < , > \}$. Consider the totally ordered abelian group$\Gamma _ { ? r } = \mathbf { R } _ { > 0 } \times \boldsymbol { \gamma } ^ { \mathbf { Z } }$, where$r ^ { \prime } < \gamma < r$for all real numbers$r ^ { \prime } < r \mathrm { i f } ? = <$, and$r ^ { \prime } > \gamma > r$for all real numbers$r ^ { \prime } > r \mathrm { i f } ? = >$. Then

$$
f = \sum a _ {n} (\mathrm{T} - x) ^ {n} \mapsto \max | a _ {n} | \gamma^ {n}
$$

defines a rank 2-valuation on R. If$? = <$, then it depends only on$\operatorname { D } ( x , < r ) = \{ y \in k ^ { \circ } \mid$ $\vert y - x \vert < r \} . \operatorname { I f } ^ { \mathrm { ? } } = >$, then it depends only on$Ḋ \mathrm { Ḋ ( } x , r ) Ḍ Ḍ$

One checks that ifr$\notin | k ^ { \times } |$, then these points are all equivalent to the corresponding point oftype (3). However, at each branching point, i.e. point oftype (2), this gives exactly one additional point for each ray starting from this point.

All points except those of type (2) are closed. Let κ be the residue field of k. Then the closure of the Gaußpoint is exactly the Gaußpoint together with the points of type (5) around it, and is homeomorphic to$\dot { \mathbf { A } _ { \kappa } ^ { 1 } }$, with the Gaußpoint as the generic point. At the other points of type (2), one gets$\mathbf { P } _ { \kappa } ^ { 1 }$

We note that in case (5), one could define a similar valuation

$$
f = \sum a _ {n} \mathrm{T} ^ {n} \mapsto \max | a _ {n} | \gamma^ {n},
$$

with$\gamma$having the property that$r > \gamma > 1$for all$r > 1$. This valuation would still be continuous, but it takes the value$\gamma > 1$on$\mathrm { T } \in \mathrm { R } ^ { + }$. This shows the relevance of the requirement$| f ( x ) | \leq 1$for all$f \in \mathbb { R } ^ { + }$, which is automatic for rank-1-valuations.

Theorem 2.21 [22, (1.1.11)]. — There is afullyfaithfulfunctor

$$
r: \{\text {rigid - analytic varieties} / k \} \to \{\text {adic spaces} / k \}: \mathrm{X} \mapsto \mathrm{X} ^ {\mathrm{ad}}
$$

sending Sp(R) to Spa(R, R<sup>+</sup>) for any affinoid k-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$of tft. It induces an equivalence

{qs rigid-analytic varieties/k} <sup>∼</sup>= {qs adic spaces locally of finite type/k},

where an adic space over k is called locally offinite type ifit is locally oftheform Spa(R, R<sup>+</sup>), where $( \mathrm { R } , \mathrm { R } ^ { + } )$is of tft. Let X be a rigid-analytic variety over k with corresponding adic space$\mathrm { X ^ { a d } }$. As any classical point defines an adic point, we have$\mathrm { \Delta X \subset X ^ { \mathrm { a d } } }$. If X is quasiseparated, then mapping a quasicompact open subset$\mathrm { U } \subset \mathrm { X } ^ { \mathrm { a d } } t o \mathrm { U } \cap \mathrm { X }$defines a bijection

{qc admissible opens in$\mathrm { X } \mathrm { \cong \{ q c \ o p e n s \ i n \mathrm { X ^ { a d } \} } }$

the inverse ofwhich is denoted U → U<sup>˜</sup> . Under this bijection afamily ofquasicompact admissible opens $\mathrm { U } _ { i } \subset \mathrm { X } .$forms an admissible cover if and only if the corresponding subsets$\tilde { \mathrm { U } } _ { i } \subset \bar { \mathrm { X } } ^ { \mathrm { a d } } c o v e r \mathrm { X } ^ { \mathrm { a d } }$

In particular,for any rigid-analytic variety X, the topos ofsheaves on the Grothendieck site associated to X is equivalent to the category ofsheaves on the sober topological space$\mathrm { X ^ { a d } }$

We recall that for abstract reasons, there is up to equivalence at most one sober topological space with the last property in the theorem. This gives the topological space underlying the adic space a natural interpretation.

In the example$\mathrm { X } = \mathrm { S p } ( { k } \langle \mathrm { T } \rangle )$discussed above, a typical example of a non-admissible cover is the cover of$\{ x \mid | x | \leq 1 \}$as

$$
\left\{x \mid | x | \leq 1 \right\} = \left\{x \mid | x | = 1 \right\} \cup \bigcup_ {r <   1} \left\{x \mid | x | \leq r \right\}.
$$

In the adic world, one can see this non-admissibility as being caused by the point of type (5) which gives |x| a value$\gamma < 1$bigger than any$r < 1$

![](images/page_15_image_12.jpg)

Moreover, adic spaces behave well with respect to formal models. In fact, one can define adic spaces in greater generality so as to include locally noetherian formal schemes as a full subcategory, but we will not need this more general theory here.

Theorem 2.22. — Let X be some admissibleformal scheme over$k ^ { \circ }$, let X be its genericfibre in the sense ofRaynaud, and let$\mathrm { X ^ { a d } }$be the associated adic space. Then there is a continuous specialization map

$$
\mathrm{sp}: \mathrm{X} ^ {\mathrm{ad}} \to \mathfrak {X},
$$

extending to a morphism oflocally ringed topological spaces$( \mathrm { X ^ { a d } } , \mathcal { O } _ { \mathrm { X ^ { a d } } } ^ { + } )  ( { \mathfrak { X } } , \mathcal { O } _ { \mathfrak { X } } )$

Now assume that X is afixed quasicompact quasiseparated adic space locally offinite type over$k .$ By Raynaud, there exist formal models X for X, unique up to admissible blowup. Then there is a homeomorphism

$$
\mathrm{X} \cong \varprojlim_ {\mathfrak {X}} \mathfrak {X},
$$

where$\mathfrak { X }$runs overformal models ofX, extending to an isomorphism oflocally ringed topological spaces $( \mathrm { X } , \mathcal { O } _ { \mathrm { X } } ^ { + } ) \cong \varprojlim _ { \mathfrak { X } } ( \mathfrak { X } , \mathcal { O } _ { \mathfrak { X } } )$, where the right-hand side is the inverse limit in the category oflocally ringed topological spaces.

Proof. — It is an easy exercise to deduce this from the previous theorem and the results of[3], Section 4, and [20], Section 4. Let us sketch the proofofthe last part. In the situation of the first part, the map sp :$\mathrm { X ^ { a d } } \to \mathfrak { X }$is a surjective spectral map of spectral spaces. It follows that the map

$$
\mathrm{X} \to \varprojlim_ {\mathfrak {x}} \mathfrak {X}
$$

is still a surjective map of spectral spaces. For this, note that$\mathrm { X }$is compact for the constructible topology, and use Tychonoff ’s theorem. But for any quasicompact open U of $\mathrm { X , }$one may find a formal model$\mathfrak { X }$of$\mathrm { X , }$such that U is the preimage under the specialization map of a quasicompact open subset of${ \mathfrak { X } } .$. This implies that the map is injective (as X is$\mathrm { T } _ { 0 } ) _ { \mathrm { : } }$, and then a homeomorphism. Moreover, if U is the preimage under specialization of an open affine formal subscheme$\mathfrak { U } = \mathrm { S p f R } \subset \mathfrak { X }$, and$\mathfrak { X }$is normal, then $\mathrm { U } = \mathrm { S p a } ( \mathrm { R } [ \textstyle { \frac { 1 } { \rho } } ]$, R) is still affinoid, and$\mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) = \mathrm { R } = \mathcal { \bar { O } } _ { \mathfrak { X } } ( \mathfrak { U } )$. Using that X is covered by such U, one deduces the assertion.-

In the example, one can start with$\mathfrak { X } = \operatorname { S p f } ( k ^ { \circ } \langle \mathrm { T } \rangle )$) as a formal model; this gives${ \bf A } _ { \kappa } ^ { 1 }$ as underlying topological space. After that, one can perform iterated blowups at closed points. This introduces additional$\mathbf { p } _ { \kappa } ^ { 1 } \mathrm { \tilde { s } ; }$the strict transform of each component survives in the inverse limit and gives the closure of a point of type (2). Note that the point of type (2) is given as the preimage of the generic point of the component in the formal model.

We note that in order to get continuity of sp, it is necessary to use nonstrict equalities in the definition of open subsets.

Now, let us state the following theorem about the comparison of Berkovich’s analytic spaces and Huber’s adic spaces. For this, we need to recall the following definition:

Definition 2.23. — An adic space X over k is called taut ifit is quasiseparated andfor every quasicompact open subset$\mathrm { ~ U ~ C ~ X ~ }$, the closure U ofU in X is still quasicompact.

Most natural adic spaces are taut, e.g. all affinoid adic spaces, or more generally all qcqs adic spaces, and also all adic spaces associated to separated schemes of finite type over k. However, in recent work of Hellmann [17], studying an analogue of Rapoport-Zink period domains in the context of deformations of Galois representations, it was found that the weakly admissible locus is in general a nontaut adic space.

We note that one can also define taut rigid-analytic varieties, and that one gets an equivalence of categories between the category of taut rigid-analytic varieties over k and taut adic spaces locally of finite type over k. Hence the first equivalence in the following theorem could be stated without reference to adic spaces.

Theorem 2.24 [22, Proposition 8.3.1, Lemma$\delta . l . \delta ] . - Tilde { T }$here is an equivalence ofcategories

{Hausdorff strictly k-analytic Berkovich spaces}

<sup>∼</sup>= {taut adic spaces locally of finite$\mathrm { { t y p e } } / k \}$

sending${ \mathcal { M } } ( { \mathrm { R } } )$to$\mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$for any affinoid k-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$of tft.

$L e t \mathrm { X ^ { B e r k } }$map to$\mathrm { X ^ { a d } }$under this equivalence. Then there is an injective map ofsets$\mathrm { X ^ { B e r k }  }$ $\mathrm { X ^ { a d } }$, whose image is precisely the subset of rank-1-valuations. This map is in general not continuous. It admits a continuous retraction$\mathrm { X ^ { a d } \to X ^ { B e r k } }$, which identifies$\mathrm { { X ^ { B e r k } } }$with the maximal Hausdorff quotient$\mathrm { \Gamma _ { \it 0 } f X ^ { \mathrm { a d } } }$

In the example above, the image of the map$\mathrm { X ^ { B e r k } \to X ^ { a d } }$consists of the points of type (1)–(4). The retraction$\mathrm { X ^ { a d } \to X ^ { B e r k } }$contracts each point of type (2) with all points of type (5) around it, mapping them to the corresponding point of type (2) in$\mathrm { { X ^ { B e r k } } }$. For any map from$\mathrm { X ^ { a d } }$to a Hausdorff topological space, any point of type (2) will have the same image as the points of type (5) around it, as they lie in its topological closure, which verifies the last assertion of the theorem in this case.

Let us end this section by describing in more detail the fibres of the map$\mathrm { X ^ { a d }  }$ $\mathrm { { X ^ { B e r k } } }$. In fact, this discussion is valid even for adic spaces which are not related to Berkovich spaces. As the following discussion is local, we restrict to the affinoid case.

Let (R, R<sup>+</sup>) be an affinoid$k { \mathrm { - a l g e b r a } } .$, and let$\mathrm { X = S p a ( R , R ^ { + } ) }$. We need not assume that$\mathcal { O } _ { \mathrm { X } }$is a sheaf in the following. For any$x \in \mathrm { X }$, we let k(x) be the residue field of$\mathcal { O } _ { \mathrm { X } , x } ,$, and$k ( x ) ^ { + } \subset k ( x )$be the image of$\mathcal { O } _ { \mathrm { X } , x } ^ { + }$. We have the following crucial property, surprising at first sight.

Proposition 2.25. — Let$\varpi \in k$be topologically nilpotent. Then the  -adic completion of $\mathcal { O } _ { \mathrm { X } , x } ^ { + }$is equal to the  -adic completion$\widehat { k ( x ) } ^ { + } \ o f k ( x ) ^ { + }$

Proof. — It is enough to note that kernel of the map$\mathcal { O } _ { \mathrm { X } , x } ^ { + } \to k ( x ) ^ { + }$, which is also the kernel of the map$\mathcal { O } _ { \mathrm { X } , x }  k ( x )$, is  -divisible.-

Definition 2.26. — An affinoid field is pair$( \mathrm { K } , \mathrm { K } ^ { + } )$consisting of a nonarchimedean field K and an open valuation subring$\mathrm { K } ^ { + } \subset \mathrm { K } ^ { \circ }$

In other words, an affinoid field is given by a nonarchimedean field K equipped with a continuous valuation (up to equivalence). In the situation above,$( k ( x ) , k ( x ) ^ { + } )$is an affinoid field. The completion of an affinoid field is again an affinoid field. Also note that affinoid fields for which$k \subset \mathrm { K }$are affinoid k-algebras. The following description of points is immediate.

Proposition$2 . 2 7 . \_ { L e t } ( \mathrm { R } , \mathrm { R } ^ { + } )$be an affinoid k-algebra. The points$g f \mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$are in bijection with maps$( \mathrm { R } , \mathrm { R } ^ { + } )  ( \mathrm { K } , \mathrm { K } ^ { + } )$to complete affinoidfields$( \mathrm { K } , \mathrm { K } ^ { + } )$such that the quotient field of the image of R in K is dense.

Definition 2.28. — For two points$x , y$in some topological space$\mathrm { X , }$, we say that x specializes toy (ory generalizes to x), written$x \succ y ( o r y \prec x ) .$, ify lies in the closure${ \overline { { \{ x \} } } } o f x .$

Proposition 2.29$\ [ 2 2 , ( { \cal I } . { \cal I } . \delta ) - ( { \cal I } . { \cal I } . { \cal I } 0 ) ] . - { \cal L } e t \ ( { \bf R } , { \bf R } ^ { + } )$be an affinoid k-algebra, and let $x , y \in \mathrm { { X = S p a ( R , R ^ { + } ) } }$correspond to maps$( \mathrm { R } , \mathrm { R } ^ { + } )  ( \mathrm { K } , \mathrm { K } ^ { + } )$, resp.$( \mathrm { R } , \mathrm { R } ^ { + } )  ( \mathrm { L } , \mathrm { L } ^ { + } )$ Then$x \succ y$if and only$i f \mathrm { K } \cong \mathrm { L }$as topological R-algebras and$\mathrm { L } ^ { + } \subset \mathrm { K } ^ { + }$

For any point$y \in \mathrm { X } ,$, the set$\{ x \mid x \succ y \}$ofgeneralizations ofy is a totally ordered chain oflength exactly the rank ofthe valuation corresponding$t o \ : y$

Note that in particular, for a given complete nonarchimedean field K with a map $\mathrm { R } \to \mathrm { K }$, there is the point$x _ { 0 }$corresponding to$( \mathrm { K } , \mathrm { K } ^ { \circ } )$. This corresponds to the unique continuous rank-1-valuation on$\mathrm { K }$. The point$x _ { 0 }$specializes to any other point for the same K.

## 3. Perfectoid fields

Definition 3.1. — A perfectoidfield is a complete nonarchimedeanfield K ofresidue characteristic $/ > 0$whose associated rank-1-valuation is nondiscrete, such that the Frobenius is surjective on$\mathrm { K } ^ { \circ } /  { p }$

We note that the requirement that the valuation is nondiscrete is needed to exclude unramified extensions of$\mathbf { Q } _ { b }$. It has the following consequence.

Lemma 3.2.$- L e t \mid \cdot \mid : \mathrm { K }  \Gamma \cup \{ 0 \}$be the unique rank-1-valuation on K, where$\Gamma =$ $| \mathrm { K } ^ { \times } | \ i s$chosen minimal. Then  is p-divisible.

Proof. — As$\Gamma \neq | p | ^ { \mathbf { Z } }$, the group  is generated by the set of all$| x |$for$x \in \mathrm { K }$with $| \boldsymbol { \mu } | < | \boldsymbol { x } | \leq 1$. For such$x ,$choose somey such that$| x - y ^ { p } | \leq | p |$. Then$\vert y \vert ^ { p } = \vert y ^ { p } \vert = \vert x \vert$, as desired.-

The class of perfectoid fields naturally separates into the fields of characteristic 0 and those of characteristic$\beta .$In characteristic$\beta ,$a perfectoid field is the same as a complete perfect nonarchimedean field.

Remark 3.3. — The notion of a perfectoid field is closely related to the notion of a deeply ramified field. Taking the definition of deeply ramified fields given in [15], we remark that Proposition 6.6.6 of [15] says that a perfectoid field K is deeply ramified, and conversely, a complete deeply ramified field with valuation of rank 1 is a perfectoid field.

Now we describe the process of tilting for perfectoid fields, which is a functor from the category of all perfectoid fields to the category of perfectoid fields in characteristic$\beta .$

For its first description, choose some element$\varpi \in \mathrm { K } ^ { \times }$such that$| \rho | \leq | \varpi | < 1$ Now consider

$$
\varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi ,
$$

where$\Phi$denotes the Frobenius morphism$x \mapsto x ^ { \rho }$. This gives a perfect ring of characteristic$\beta .$We equip it with the inverse limit topology; note that each$\mathrm { K } ^ { \circ } / \varpi$naturally has the discrete topology.

## Lemma 3.4.

(i) There is a multiplicative homeomorphism

$$
\varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{K} ^ {\circ} \stackrel {{\cong}} {{\to}} \varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi ,
$$

given by projection. In particular, the right-hand side is independent of$\dot { } _ { \varpi }$. Moreover, we get a map

$$
\varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi \to \mathrm{K} ^ {\circ}: x \mapsto x ^ {\sharp}.
$$

(ii) There is an element$\varpi ^ { \flat } \in \varprojlim _ { \Phi } \mathrm { K } ^ { \circ } / \varpi$with$| ( \varpi ^ { \flat } ) ^ { \sharp } | = | \varpi |$. Define

$$
\mathrm{K} ^ {\flat} = \Bigl (\varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi \Bigr) \bigl [ \bigl (\varpi^ {\flat} \bigr) ^ {- 1} \bigr ].
$$

(iii) There is a multiplicative homeomorphism

$$
\mathrm{K} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{K}.
$$

In particular, there is a map$\operatorname { K } ^ { \flat } \to \operatorname { K } , x \mapsto x ^ { \sharp }$. Then$\mathrm { K } ^ { \flat }$is a perfectoidfield ofcharacteristic$\rho ,$

$$
\mathrm{K} ^ {\flat \circ} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{K} ^ {\circ} \cong \varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi ,
$$

and the rank-1-valuation on$\mathrm { K } ^ { \flat }$can be defined by$| x | _ { \mathrm { K } ^ { \flat } } = | x ^ { \sharp } | _ { \mathrm { K } }$. We have$| \mathrm { K } ^ { \mathrm { p \times } } | = | \mathrm { K } ^ { \times } |$ Moreover,

$$
\mathrm{K} ^ {\flat \circ} / \varpi^ {\flat} \cong \mathrm{K} ^ {\circ} / \varpi , \quad \mathrm{K} ^ {\flat \circ} / \mathfrak {m} ^ {\flat} = \mathrm{K} ^ {\circ} / \mathfrak {m},
$$

where m, resp.${ \mathfrak { m } } ^ { \flat } .$, is the maximal ideal$o f \mathrm { K } ^ { \circ }$, resp.$\mathrm { K } ^ { \flat \circ }$.

(iv) IfK is ofcharacteristic$\beta ,$then$\mathrm { K } ^ { \flat } = \mathrm { K }$

We call$\mathrm { K } ^ { \flat }$the tilt of K.

Remark 3.5. — Obviously,$\varpi ^ { \flat }$in (ii) is not unique. As it is not harmful to replace with an element of the same norm, we will usually redefine$\varpi = ( \varpi ^ { \flat } ) ^ { \sharp }$, which comes equipped with a compatible system

$$
\varpi^ {1 / p ^ {n}} = \left(\left(\varpi^ {\flat}\right) ^ {1 / p ^ {n}}\right) ^ {\sharp}
$$

of$\beta ^ { n } \mathrm { \mathrm { ^ { - t h } } }$roots. Conversely,$\varpi$together with such a choice ofp<sup>n</sup>-th roots gives an element $\varpi ^ { \flat }$of

$$
\mathrm{K} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{K}.
$$

Proof. — (i) We begin by constructing a multiplicative continuous map

$$
\varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi \to \mathrm{K} ^ {\circ}: x \mapsto x ^ {\sharp}.
$$

Let$( \overline { { x } } _ { 0 } , \overline { { x } } _ { 1 } , . . . ) \in \varprojlim _ { \Phi } \mathrm { K } ^ { \circ } / \varpi$. Choose any lift$x _ { n } \in \mathrm { K } ^ { \circ }$of$\cdot _ { \overline { { x } } _ { n } }$. Then we claim that the limit

$$
x ^ {\sharp} = \lim _ {n \to \infty} x _ {n} ^ {p ^ {n}}
$$

exists and is independent of all choices. For this, it is enough to see that$x _ { n } ^ { p ^ { n } }$gives a welldefined element of$\mathrm { K } ^ { \circ } / \varpi ^ { n + 1 }$. But if$x _ { n } ^ { \prime }$is a second lift, then$x _ { n } - x _ { n } ^ { \prime }$is divisible by$\varpi$. One checks by induction on$i = 0 , 1 , \ldots , n$that

$$
\left(x _ {n} ^ {\prime}\right) ^ {p ^ {i}} - x _ {n} ^ {p ^ {i}} = \left(x _ {n} ^ {p ^ {i - 1}} + \left(\left(x _ {n} ^ {\prime}\right) ^ {p ^ {i - 1}} - x _ {n} ^ {p ^ {i - 1}}\right)\right) ^ {p} - x _ {n} ^ {p ^ {i}}
$$

gives a well-defined element of$\mathrm { K } ^ { \circ } / \varpi ^ { i + 1 }$, using that$\varpi | \boldsymbol { p } .$

It is clear from the definition that$x \mapsto x ^ { \sharp }$is multiplicative and continuous. Now the map$\varprojlim _ { \Phi } \mathrm { K } ^ { \circ } / \varpi  \varprojlim _ { x \mapsto x ^ { \beta } } \mathrm { K } ^ { \circ }$given by$x \mapsto ( x ^ { \sharp } , ( x ^ { 1 / \hbar } ) ^ { \sharp } , \ldots )$gives an inverse to the obvious projection map.

(ii) Pick some element$\varpi _ { 1 }$with$| \varpi _ { 1 } | ^ { p } = | \varpi |$. Then$\varpi _ { 1 }$defines a nonzero element of$\mathrm { K } ^ { \circ } / \varpi$. Choose any sequence

$$
\varpi^ {\flat} = (0, \varpi_ {1}, \ldots) \in \varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi ;
$$

this is possible by surjectivity of  on$\mathrm { K } ^ { \circ } / \varpi$. By the proof of part$\mathrm { ( i ) }$, we have$| ( \varpi ^ { \flat } ) ^ { \sharp } -$ $\varpi _ { 1 } ^ { \boldsymbol { p } } \vert \leq \vert \varpi \vert ^ { 2 }$. This gives$| ( \varpi ^ { \flat } ) ^ { \sharp } | = | \varpi |$, as desired.

(iii) As$x \mapsto x ^ { \sharp }$is multiplicative, it extends to a map

$$
\mathrm{K} ^ {\flat} \to \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{K}.
$$

One easily checks that it is a homeomorphism; in particular$\mathrm { K } ^ { \flat }$is a field. One also checks that the topology on$\varprojlim _ { \Phi } \mathrm { K } ^ { \circ } / \varpi$is induced by the norm$x \mapsto \vert x ^ { \sharp } \vert$. Hence the topology on$\mathrm { K } ^ { \flat }$is induced by the rank-1-valuation$x \mapsto \vert x ^ { \sharp } \vert$. Clearly,$\mathrm { K } ^ { \flat }$is perfect and complete, so$\mathrm { K } ^ { \flat }$is a perfectoid field of characteristic$\beta .$. One easily deduces all other claims.

(iv) This is clear since$\operatorname { K } ^ { \flat } \cong \varprojlim _ { x \mapsto x ^ { \flat } } \operatorname { K } .$

Recall that when working with adic spaces, it is important to understand the continuous valuations on K. Under the process of tilting, we have the following equivalence.

Proposition 3.6. — Let K be a perfectoidfield with tilt$\mathrm { K } ^ { \flat }$. Then the continuous valuations | · | ofK (up to equivalence) are mapped bijectively to the continuous valuations$| \cdot | ^ { \flat } g f \mathbf { K } ^ { \flat }$(up to equivalence) via$| x | ^ { \flat } = | x ^ { \sharp } |$

Proof. — First, we check that the map$| \cdot | \mapsto | \cdot | ^ { \flat }$maps valuations to valuations. All properties except$| x + y | ^ { \flat } \leq \operatorname* { m a x } ( | x | ^ { \flat } , | y | ^ { \flat } )$are immediate, using that$x \mapsto x ^ { \sharp }$is multiplicative. But

$$
\begin{array}{l} | x + y | ^ {\flat} = \lim _ {n \to \infty} \big | \big (x ^ {1 / p ^ {n}} \big) ^ {\sharp} + \big (y ^ {1 / p ^ {n}} \big) ^ {\sharp} \big | ^ {p ^ {n}} \\ \qquad \leq \max \Big (\lim _ {n \to \infty} \big | \big (x ^ {1 / p ^ {n}} \big) ^ {\sharp} \big | ^ {p ^ {n}}, \lim _ {n \to \infty} \big | \big (y ^ {1 / p ^ {n}} \big) ^ {\sharp} \big | ^ {p ^ {n}} \Big) = \max \big (\big | x ^ {\sharp} \big |, \big | y ^ {\sharp} \big | \big). \end{array}
$$

It is clear that continuity is preserved.

On the other hand, continuous valuations are in bijection with open valuation subrings$\mathrm { K } ^ { + } \subset \mathrm { K } ^ { \circ }$. They necessarily contain the topologically nilpotent elements m. We see that open valuation subrings$\dot { \mathrm { K } } ^ { + } \subset \mathrm { K } ^ { \circ }$are in bijection with valuation subrings in $\mathrm { K ^ { \circ } / m } = \mathrm { K ^ { \circ } / m ^ { \flat } }$. This implies that one gets a bijection with continuous valuations of K and continuous valuations of$\mathrm { K } ^ { \flat }$which is easily seen to be the one described.-

The main theorem about tilting for perfectoid fields is the following theorem. For many fields, this was known by the classical work of Fontaine-Wintenberger.

Theorem 3.7. — Let K be a perfectoidfield.

(i) Let L be a finite extension of K. Then L (with its natural topology as a finite-dimensional K-vector space) is a perfectoidfield.

(ii) Let K<sup>-</sup> be the tilt of K. Then the tilting functor$\mathrm { L } \mapsto \mathrm { L } ^ { \flat }$induces an equivalence of categories between the category of finite extensions of K and the category of finite extensions of K<sup>-</sup>. This equivalence preserves degrees.

It turns out that many of the arguments will generalize directly to the context of perfectoid K-algebras introduced later. For this reason, we defer the proofofthis theorem. Let us only prove the following special case here.

Proposition 3.8. — Let K be a perfectoidfield with tilt K<sup>-</sup>. IfK<sup>-</sup> is algebraically closed, then K is algebraically closed.

$P r o o f \mathrm { - } \mathrm { L e t } \mathrm { P } \mathrm { ( X ) } = \mathrm { X } ^ { d } + a _ { d - 1 } \mathrm { X } ^ { d - 1 } + \cdot \cdot \cdot + a _ { 0 } \in \mathrm { K } ^ { \circ } [ \mathrm { X } ]$be any monic irreducible polynomial of positive degree d. Then the Newton polygon of P is a line. Moreover, we may assume that the constant term of P has absolute value$| a _ { 0 } | = 1 , \mathrm { a s } | \mathrm { K } ^ { \times } | = | \mathrm { K } ^ { \flat \times } |$is a Q-vector space.

Now let$\operatorname { Q } ( \mathrm { X } ) = \mathrm { X } ^ { d } + b _ { d - 1 } \mathrm { X } ^ { d - 1 } + \cdot \cdot \cdot + b _ { 0 } \in \mathrm { K } ^ { \mathrm { b o } } [ \mathrm { X } ]$be any polynomial such that P and Qhave the same image in$\mathrm { K } ^ { \circ } / \varpi [ \mathrm { X } ] = \mathrm { K } ^ { \flat \circ } / \varpi ^ { \flat } [ \mathrm { X } ]$, and let$y \in \mathbf { K } ^ { \flat \circ }$be a root of$\mathrm { \Delta Q }$

Considering$\mathrm { P } ( \mathrm { X } + \boldsymbol { y } ^ { \sharp } )$, we see that the constant term$\mathrm { P } ( y ^ { \sharp } )$is divisible by  . As it is still irreducible, its Newton polygon is a line and hence the polynomial$\mathrm { { P } _ { 1 } ( X ) = }$ $c ^ { - d } \mathrm { P } ( c \mathrm { X } + y ^ { \sharp } )$has integral coefficients again, where$| c | ^ { d } = | \mathrm { P } ( y ^ { \sharp } ) | \le | \varpi |$. Repeating the arguments gives an algorithm converging to a root of P.-

Our proof of Theorem 3.7 will make use of Faltings’s almost mathematics. For this reason, we recall some necessary background in the next section.

## 4. Almost mathematics

We will use the book of Gabber-Ramero [15] as our basic reference.

Fix a perfectoid field K. Let${ \mathfrak { m } } = { \mathrm { K } } ^ { \circ \circ } \subset { \mathrm { K } } ^ { \circ }$be the subset of topologically nilpotent elements; it is also the set$\{ x \in \mathrm { K } \mid \lvert x \rvert < 1 \}$, and the unique maximal ideal of$\mathrm { K } ^ { \circ }$. The basic idea of almost mathematics is that one neglects m-torsion everywhere.

Definition 4.1. — Let M be a K<sup>◦</sup>-module. An element$x \in \mathbf { M }$is almost zero$i f \mathfrak { m } x = 0$. The module M is almost zero ifall ofits elements are almost zero; equivalently, m$\mathbf { M } = 0$

Lemma 4.2. — Thefull subcategory ofalmost zero objects in$\mathrm { K } ^ { \circ }$-mod is thick.

Proof. — The only nontrivial part is to show that it is stable under extensions, so let

$$
0 \to \mathrm{M} ^ {\prime} \to \mathrm{M} \to \mathrm{M} ^ {\prime \prime} \to 0
$$

be a short exact sequence of$\mathrm { K } ^ { \circ }$-modules, with$\mathrm { \ m M ^ { \prime } = m M ^ { \prime \prime } = 0 }$. In general, one gets that$\mathfrak { m } ^ { 2 } \mathbf { M } = 0$. But in our situation,${ \mathfrak { m } } ^ { 2 } = { \mathfrak { m } }$, so M is almost zero.-

We note that there is a sequence of localization functors

$$
\mathrm{K} ^ {\circ} \text {-mod} \rightarrow \mathrm{K} ^ {\circ} \text {-mod} / (\mathfrak {m} \text {-torsion}) \rightarrow \mathrm{K} \text {-mod}.
$$

Their composite is the functor of passing from an integral structure to its generic fibre. In this sense, the category in the middle can be seen as a slightly generic fibre, or as an almost integral structure. It will turn out that in perfectoid situations, properties and objects over the generic fibre will extend automatically to the slightly generic fibre, in other words the generic fibre almost determines the integral level. It will be easy to justify this philosophy if K has characteristic$\beta ,$by using the following argument. Assume that some statement is true over K. By using some finiteness property, it follows that there is some big N such that it is true up to$\varpi ^ { \mathrm { N } }$-torsion. But Frobenius is bijective, hence the property stays true up to$\varpi ^ { \mathrm { N } / { p } } \mathrm { - t o r s i o n }$. Now iterate this argument to see that it is true up to$\dot { \varpi } ^ { \mathrm { N } / \dot { p ^ { m } } }$-torsion for all$m ,$i.e. almost true.

Following these ideas, our proof of Theorem 3.7 will proceed as follows, using the subscript fet to denote categories of finite étale (almost) algebras.´

$$
\mathrm{K} _ {\mathrm {f \acute {e} t}} \cong \mathrm{K} _ {\mathrm {f \acute {e} t}} ^ {\circ a} \cong \left(\mathrm{K} ^ {\circ a} / \varpi\right) _ {\mathrm {f \acute {e} t}} = \left(\mathrm{K} ^ {\flat \circ a} / \varpi^ {\flat}\right) _ {\mathrm {f \acute {e} t}} \cong \mathrm{K} _ {\mathrm {f \acute {e} t}} ^ {\flat \circ a} \cong \mathrm{K} _ {\mathrm {f \acute {e} t}} ^ {\flat}.
$$

Our principal aim in this section is to define all intermediate categories.

Definition 4.3. — Define the category ofalmost$\mathrm { K } ^ { \circ }$-modules as

$$
\mathrm{K} ^ {\circ a} \text {-mod} = \mathrm{K} ^ {\circ} \text {-mod} / (\mathfrak {m} \text {-torsion}).
$$

In particular, there is a localization functor$\mathbf { M } \mapsto \mathbf { M } ^ { a }$from$\mathrm { K } ^ { \circ }$-mod to$\mathrm { K } ^ { \circ a }$-mod, whose kernel is exactly the thick subcategory ofalmost zero modules.

Proposition 4.4 [15, §2.2.2]. — Let M, N be two$\mathrm { K } ^ { \circ } .$-modules. Then

$$
\operatorname{Hom} _ {\mathrm{K} ^ {\circ a}} \left(\mathrm{M} ^ {a}, \mathrm{N} ^ {a}\right) = \operatorname{Hom} _ {\mathrm{K} ^ {\circ}} (\mathfrak {m} \otimes \mathrm{M}, \mathrm{N}).
$$

In particular,$\mathrm { H o m } _ { \mathrm { K } ^ { \circ a } } ( \mathrm { X } , \mathrm { Y } )$has a natural structure of$\mathrm { K } ^ { \circ }$-modulefor any two$\mathrm { K } ^ { \circ a }$-modules X and$\mathrm { Y }$. The module$\mathrm { H o m } _ { \mathrm { K } ^ { \circ a } } ( \mathrm { X } , \mathrm { Y } )$has no almost zero elements.

For two$\mathrm { K } ^ { \circ a }$-modules$\mathrm { { M } , N , }$we define alHom$\operatorname { ( X , Y ) } = \operatorname { H o m } ( \mathrm { X , Y } ) ^ { a }$

Proposition 4.5$[ I 5 , \{ 2 . 2 . 6 , \ S 2 . 2 . 1 2 \} . - \ T$he category$\mathrm { K } ^ { \circ a }$-mod is an abelian tensor category, where we define kernels, cokernels and tensor products in the unique way compatible with their definition in K<sup>◦</sup>-mod,$e . g .$

$$
\mathbf {M} ^ {a} \otimes \mathbf {N} ^ {a} = (\mathbf {M} \otimes \mathbf {N}) ^ {a}
$$

for any two$\mathrm { K } ^ { \circ }$-modules M, N. For any three$\mathrm { K } ^ { \circ a }$-modules L, M, N, there is afunctorial isomorphism

$$
\operatorname{Hom} \bigl (\mathrm{L}, \operatorname{alHom} (\mathrm{M}, \mathrm{N}) \bigr) = \operatorname{Hom} (\mathrm{L} \otimes \mathrm{M}, \mathrm{N}).
$$

This means that$\mathrm { K } ^ { \circ a }$-mod has all abstract properties of the category of modules over a ring. In particular, one can define in the usual abstract way the notion of a$\mathrm { K } ^ { \circ a } .$ algebra. For any$\mathrm { K } ^ { \circ a }$-algebra$\mathrm { A } ,$one also has the notion ofan A-module. Any$\mathrm { K } ^ { \circ }$-algebra R defines a$\mathrm { K } ^ { \circ a }$-algebra$\mathrm { R } ^ { a } ,$, as the tensor products are compatible. Moreover, localization also gives a functor from R-modules to$\mathbf { R } ^ { a }$-modules. For example,$\mathrm { K } ^ { \circ }$gives the$\mathrm { K } ^ { \circ a } .$ algebra$\mathrm { A } = \mathrm { K } ^ { \circ a }$, and then A-modules are$\mathrm { K } ^ { \circ a }$-modules, so that the terminology is consistent.

Proposition 4.6 [15, Proposition 2.2.$I 4 ] . - T$here is a right adjoint

$$
\mathrm{K} ^ {\circ a} \text {-mod} \rightarrow \mathrm{K} ^ {\circ} \text {-mod}: \mathrm{M} \mapsto \mathrm{M} _ {*}
$$

to the localizationfunctor$\mathbf { M } \mapsto \mathbf { M } ^ { a } .$, given by the functor of almost elements

$$
\mathrm{M} _ {*} = \operatorname{Hom} _ {\mathrm{K} ^ {\circ a}} \left(\mathrm{K} ^ {\circ a}, \mathrm{M}\right).
$$

The adjunction morphism$( \mathbf { M } _ { * } ) ^ { a } \to \mathbf { M }$is an isomorphism. If M is a$\mathrm { K } ^ { \circ }$-module, then$( \mathbf { M } ^ { a } ) _ { * } =$ Hom(m, M).

If A is a$\mathrm { K } ^ { \circ a } - { \acute { c } }$algebra, then$\mathrm { A } _ { * }$has a natural structure as$\mathrm { K } ^ { \circ }$-algebra and$\mathrm { A } _ { * } ^ { a } = \mathrm { A }$ In particular, any$\mathrm { K } ^ { \circ a }$-algebra comes via localization from a K<sup>◦</sup>-algebra. Moreover, the functor$\mathrm { M } \mapsto \mathrm { M } _ { * }$induces a functor from A-modules to$\mathrm { A } _ { * }$-modules, and one sees that also all A-modules come via localization from$\mathrm { A } _ { * }$-modules. We note that the category of A-modules is again an abelian tensor category, and all properties about the category of $\mathrm { K } ^ { \circ a } .$-modules stay true for the category of A-modules. We also note that one can equivalently define A-algebras as algebras over the category of A-modules, or as$\mathrm { K } ^ { \circ a }$-algebras B with an algebra morphism$\mathrm { A } \to \mathrm { B }$

Finally, we need to extend some notions from commutative algebra to the almost context.

Definition/Proposition 4.7. — Let A be any$\mathrm { K } ^ { \circ a }$-algebra.

(i) An A-module M isflat ifthefunctor$\mathrm { X } \mapsto \mathrm { M } \otimes _ { \mathrm { A } } \mathrm { X }$on A-modules is exact.$H \mathrm { R }$is a $\mathrm { K } ^ { \circ }$-algebra and N is an R-module, then the$\mathbf { R } ^ { a }$-module$\mathrm { N } ^ { a }$isflat ifand only iffor all R-modules X and all$i > 0 _ { i }$, the module$\mathrm { T o r } _ { i } ^ { \mathrm { R } } ( \mathrm { N } , \mathrm { X } )$is almost zero.

(ii) An A-module M is almost projective if the functor$\mathrm { X \mapsto a l H o m _ { A } ( M , X ) }$on A-modules is exact. IfR is a K<sup>◦</sup>-algebra and N is an R-module, then$\mathrm { N } ^ { a }$is almost projective over$\mathbf { R } ^ { a }$ ifand only iffor all R-modules X and all$i > 0$, the module$\mathrm { E x t } _ { \mathrm { R } } ^ { i } ( \mathrm { N } , \mathrm { X } )$is almost zero.

(iii) IfR is a K<sup>◦</sup>-algebra and N is an R-module, then$\mathrm { M } = \mathrm { N } ^ { a }$is said to be an almostfinitely generated (resp. almostfinitely presented) R<sup>a</sup>-module ifand only iffor all$\epsilon \in { \mathfrak { m } }$, there is some finitely generated (resp. finitely presented) R-module$\mathrm { N } _ { \epsilon }$with a map$f _ { \epsilon } : \mathrm { N } _ { \epsilon } \to \mathrm { N }$ such that the kernel and cokernel off are annihilated by . We say that M is uniformly almostfinitely generated ifthere is some integer n such that$\mathrm { N } _ { \epsilon }$can be chosen to be generated by n elements,for all .

Proof. — For parts (i) and$( \mathrm { i i } ) ,$cf. [15], Definition 2.4.4, §2.4.10 and Remark 2.4.12(i). For part (iii), cf. [15], Definition 2.3.8, Remark 2.3.9(i) and Corollary 2.3.13.-

Remark 4.8. — In (iii), we make the implicit statement that this property depends only on the$\mathbf { R } ^ { a } .$-module$\mathrm { N } ^ { a }$. There is also the categorical notion of projectivity saying that the functor$\mathrm { X } \mapsto$Hom(M, X) is exact, but not even$\mathrm { K } ^ { \circ a }$itself is projective in general: One can check that the map

$$
\mathrm{K} ^ {\circ} = \operatorname{Hom} \left(\mathrm{K} ^ {\circ a}, \mathrm{K} ^ {\circ a}\right)\rightarrow \operatorname{Hom} \left(\mathrm{K} ^ {\circ a}, \mathrm{K} ^ {\circ a} / \varpi\right) = \operatorname{Hom} \left(\mathfrak {m}, \mathrm{K} ^ {\circ} / \varpi\right)
$$

is in general not surjective, as the latter group contains sums of the form

$$
\sum_ {i \geq 0} \varpi^ {1 - 1 / p ^ {i}} x _ {i}
$$

for arbitrary$x _ { i } \in \mathrm { K } ^ { \circ } / \varpi$

Example 4.9. — As an example of an almost finitely presented module, consider the case that K is the p-adic completion of$\mathbf { Q } _ { \mathcal { \boldsymbol { P } } } ( \boldsymbol { \phi } ^ { 1 / \mathcal { P } ^ { \infty } } ) , \boldsymbol { \mathscr { p } } \neq 2$. Consider the extension $\mathrm { L } = \mathrm { K } ( \boldsymbol { \mu } ^ { 1 / 2 } )$. Then$\mathrm { L } ^ { \circ a }$is an almost finitely presented$\mathrm { K } ^ { \circ a }$-module. Indeed, for any$n \geq 1$, we have injective maps

$$
\mathrm{K} ^ {\circ} \oplus p ^ {1 / 2 p ^ {n}} \mathrm{K} ^ {\circ} \rightarrow \mathrm{L} ^ {\circ}
$$

whose cokernel is killed by$p ^ { 1 / 2 p ^ { n } }$. In fact, in this example$\mathrm { L } ^ { \circ a }$is even uniformly almost finitely generated.

Proposition 4.10 [15, Proposition 2.4.18]. — Let A be a K<sup>◦a</sup>-algebra. Then an A-module M isflat and almostfinitely presented ifand only ifit is almost projective and almostfinitely generated.

By abuse of notation, we call such A-modules M finite projective in the following, a terminology not used in [15]. If additionally, M is uniformly almost finitely generated, we say that M is uniformly finite projective.

For uniformly finite projective modules, there is a good notion of rank.

Theorem 4.11 [15, Proposition 4.3.27, Remark$4 . 3 . I O ( i ) ]$. — Let A be a$\mathrm { K } ^ { \circ a }$-algebra, and let M be a uniformly finite projective A-module. Then there is a unique decomposition$\mathrm { A } = \mathrm { A } _ { 0 } \times \mathrm { A } _ { 1 } \times$ $\cdots \times \mathrm { A } _ { k }$such thatfor each$i = 0 , \ldots , k ,$the A -module$\mathbf { M } _ { i } = \mathbf { M } \otimes _ { \mathbf { A } } \mathbf { A } _ { i }$has theproperty that${ \textstyle \bigwedge } ^ { i } \mathbf { M } _ { i }$is invertible, and$\Lambda ^ { i \breve { + } 1 } \mathbf { M } _ { i } = 0$. Here, an A-module L is called invertible ifL$\otimes _ { \mathrm { A } }$$\mathrm { { l H o m } _ { A } ( L , A ) = A }$

Finally, we need the notion of étale morphisms.

Definition 4.12. — Let A be$\iota \ K ^ { \circ a } - a l g e b r a ,$, and let B be an A-algebra. Let$\mu : \mathbf { B } \otimes _ { \mathrm { A } } \mathbf { B } \to \mathbf { B }$ denote the multiplication morphism.

(i) The morphism$\mathrm { A } \to \mathrm { B }$is said to be unramified ifthere is some element$e \in ( \mathbf { B } \otimes _ { \mathbf { A } } \mathbf { B } )$such that$e ^ { 2 } = e , \mu ( e ) = 1$and$x e = 0$for all$x \in \ker ( \mu ) ,$.

(ii) The morphism$\mathrm { A } \to \mathrm { B }$is said to be étale ifit is unramified and B is aflat A-module.

We note that the definition of unramified morphisms basically says that the diagonal morphism$\mu : \mathbf { B } \otimes _ { \mathrm { A } } \mathbf { B } \to \mathbf { B }$is a closed immersion in the geometric picture.

In the following, we will be particularly interested in almost finitely presented étale maps.

Definition 4.13. — A morphism A → B of K<sup>◦a</sup>-algebras is said to be finite étale if it is étale and B is an almostfinitely presented A-module. Write$\mathrm { \bf A } _ { \mathrm { f e t } }$for the category offinite étale A-algebras.

We note that in this case B is a finite projective A-module. Also, this terminology is not used in [15], but we feel that it is the appropriate almost analogue of finite étale covers.

There is an equivalent characterization of finite étale morphisms in terms of trace morphisms. If A is any${ \mathrm { K } } ^ { \circ a } { \mathrm { - a l g e b r a } } .$, and P is some finite projective A-module, we define$\mathrm { P ^ { * } } = \mathrm { a l H o m } ( \mathrm { P } , \mathrm { A } )$, which is a finite projective A-module again. Moreover,$\mathrm { P } ^ { \ast \ast } \cong \mathrm { P }$ canonically, and there is an isomorphism

$$
\operatorname{End} (\mathrm{P}) ^ {a} = \mathrm{P} \otimes_ {\mathrm{A}} \mathrm{P} ^ {*}.
$$

In particular, one gets a trace morphism$\mathrm { t r } _ { \mathrm { P / A } } : \mathrm { E n d } ( \mathrm { P } ) ^ { a }  \mathrm { A }$

Definition 4.14. — Let A be a$\mathrm { K } ^ { \circ a }$-algebra, and let B be an A-algebra such that B is afinite projective A-module. Then we define the traceform as the bilinearform

$$
t _ {\mathrm{B/A}}: \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{B} \to \mathrm{A}
$$

given by the composition of${ \bf { \dot { \boldsymbol { \mu } } } } : { \bf B } \otimes _ { \mathrm { A } } { \bf B } \to { \bf B }$and the map$\mathrm { B }  \mathrm { A }$sending any$b \in \mathrm { B }$to the trace of the endomorphism$b ^ { \prime } \mapsto b b ^ { \prime } \ g f { \bf B }$

Remark 4.15. — We should remark that the latter definition does not literally make sense, as one can not talk about an element b of some almost object B: There is no underlying set. However, one can define a map$\mathrm { B } _ { * }  \mathrm { E n d } _ { \mathrm { A } _ { * } } ( \mathrm { B } _ { * } )$in the way described, and we are considering the corresponding map of almost objects$\mathbf { B }  \mathrm { E n d _ { A _ { * } } ( B _ { * } ) ^ { \mathfrak { a } } = }$ $\operatorname { E n d } _ { \mathrm { A } } ( \mathrm { B } ) ^ { a }$

Theorem 4.16$[ I 5 ,$Theorem 4.1.14]. — In the situation ofthe definition, the morphism$\mathrm { A } \to$ B isfinite étale ifand only ifthe trace map is a perfect pairing, i.e. induces an isomorphism$\mathrm { B } \cong \mathrm { B } ^ { \ast }$

An important property is that finite étale covers lift uniquely over nilpotents.

Theorem 4.17. — Let A be a$\mathrm { K } ^ { \circ a } - a l g e b r a .$. Assume that A isflat over$\mathrm { K } ^ { \circ a }$and  -adically complete, i.e.

$$
\mathrm{A} \cong \varprojlim \mathrm{A} / \varpi^ {n}.
$$

Then thefunctor$\mathbf { B } \mapsto \mathbf { B } \otimes _ { \mathrm { A } } \mathrm { A } / \varpi$induces an equivalence ofcategories$\mathrm { A } _ { \mathrm { f e t } } \cong ( \mathrm { A } / \varpi ) _ { \mathrm { f e t } }$. Any$\mathrm { \bf B } \in \mathrm { \bf A } _ { \mathrm { f e t } }$ is againflat over$\mathrm { K } ^ { \circ a }$and  -adically complete. Moreover, B is a uniformlyfinite projective A-module if and only if$3 \otimes _ { \mathrm { A } } \mathrm { A } / \varpi$is a uniformlyfinite projective A/ -module.

Proof. — The first part follows from [15], Theorem 5.3.27. The rest is easy. -

Recall that we wanted to prove the string of equivalences

$$
\mathrm{K} _ {\mathrm {f \acute {e} t}} \cong \mathrm{K} _ {\mathrm {f \acute {e} t}} ^ {\circ a} \cong \left(\mathrm{K} ^ {\circ a} / \varpi\right) _ {\mathrm {f \acute {e} t}} = \left(\mathrm{K} ^ {\flat \circ a} / \varpi^ {\flat}\right) _ {\mathrm {f \acute {e} t}} \cong \mathrm{K} _ {\mathrm {f \acute {e} t}} ^ {\flat \circ a} \cong \mathrm{K} _ {\mathrm {f \acute {e} t}} ^ {\flat}.
$$

The identification in the middle is tautological as$\mathrm { K } ^ { \circ } / \varpi = \mathrm { K } ^ { \flat \circ } / \varpi ^ { \flat }$, and the corresponding almost settings agree. The previous theorem shows that the inner two functors are equivalences. For the other two equivalences, we feel that it is more convenient to study them in the more general setup of perfectoid K-algebras.

## 5. Perfectoid algebras

Fix a perfectoid field K.

Definition 5.1.

(i) A perfectoid K-algebra is a Banach K-algebra R such that the subset$\mathrm { R } ^ { \circ } \subset \mathrm { R }$of powerbounded elements is open and bounded, and the Frobenius morphism$\Phi : \mathrm { R } ^ { \circ } / \varpi  \mathrm { R } ^ { \circ } / \varpi$ is surjective. Morphisms between perfectoid K-algebras are the continuous morphisms ofKalgebras.

(ii) A perfectoid$\mathrm { K } ^ { \circ a }$-algebra is a  -adically completeflat$\mathrm { K } ^ { \circ a }$-algebra A on which Frobenius induces an isomorphism

$$
\Phi : \mathrm{A} / \varpi^ {\frac {1}{p}} \cong \mathrm{A} / \varpi .
$$

Morphisms between perfectoid$\mathrm { K } ^ { \circ a } .$-algebras are the morphisms ofK<sup>◦a</sup>-algebras.

(iii) A perfectoid K<sup>◦a</sup>/ -algebra is a flat$\mathrm { K } ^ { \circ a } / \varpi$-algebra$\overline { { \mathrm A } }$on which Frobenius induces an isomorphism

$$
\Phi : \overline {{\mathrm{A}}} / \varpi^ {\frac {1}{p}} \cong \overline {{\mathrm{A}}}.
$$

Morphisms are the morphisms ofK<sup>◦a</sup>/ -algebras.

Let K-Perf denote the category of perfectoid K-algebras, and similarly for $\mathrm { K } ^ { \circ a } { \ – } \mathrm { P e r f } , \ \dots$. Let$\mathrm { K } ^ { \flat }$be the tilt of K. Then the main theorem of this section is the following.

Theorem 5.2. — The categories ofperfectoid K-algebras andperfectoid$\mathrm { K } ^ { \flat }$-algebras are equivalent.$I n f a c t ,$we have thefollowing series ofequivalences ofcategories.

$$
\begin{array}{c} \text {K - Perf} \cong \text {K} ^ {\circ a} \text {-Perf} \cong \left(\text {K} ^ {\circ a} / \varpi\right) \text {-Perf} = \left(\text {K} ^ {\flat \circ a} / \varpi^ {\flat}\right) \text {-Perf} \cong \text {K} ^ {\flat \circ a} \text {-Perf} \\ \cong \text {K} ^ {\flat} \text {-Perf} \end{array}
$$

In other words, a perfectoid K-algebra, which is an object over the generic fibre, has a canonical extension to the almost integral level as a perfectoid K<sup>◦a</sup>-algebra, and perfectoid$\mathrm { K } ^ { \circ a } .$-algebras are determined by their reduction modulo$\varpi$

The following lemma expresses the conditions imposed on a perfectoid$\mathrm { K } ^ { \circ a . }$ algebra in terms of classical commutative algebra.

Lemma 5.3. — Let M be a$\mathrm { K } ^ { \circ a }$-module.

(i) The module M isflat over$\mathrm { K } ^ { \circ a }$ifand only$i f \mathrm { M } _ { \ast }$isflat over$\mathrm { K } ^ { \circ }$ifand only ifM has no -torsion.

(ii) If N is a flat K<sup>◦</sup>-module and$\mathrm { M } = \mathrm { N } ^ { a }$, then M is flat over$\mathrm { K } ^ { \circ a }$and we have$\mathrm { M } _ { * } =$ $\begin{array} { r } { \{ x \in \mathbf { N } [ \frac { 1 } { \pi } ] \ | \ \forall \epsilon \in \mathfrak { m } : \epsilon x \in \mathbf { N } \} } \end{array}$

(iii) If M is flat over$\mathrm { K } ^ { \circ a }$, then for all$x \in \mathrm { K } ^ { \circ }$, we have$( x \mathbf { M } ) _ { * } = x \mathbf { M } _ { * }$. Moreover, $\mathrm { M } _ { * } / x \mathrm { M } _ { * } \subset ( \mathrm { M } / x \mathrm { M } ) _ { * }$, and for all$\epsilon \in { \mathfrak { m } }$the image of$( \mathrm { M } / x \epsilon \mathrm { M } )$)in$( \mathrm { M } / x \mathrm { M } )$∗ is equal to$\mathrm { M } _ { * } / x \mathrm { M } _ { * }$

(iv) If M is flat over$\mathrm { K } ^ { \circ a }$, then M is  -adically complete if and only$i f \mathbf { M } _ { * }$is  -adically complete.

Remark 5.4. — The non-surjectivity in (iii) is due to elements as in Remark 4.8.

Proof. — (i) By definition, M is a flat$\mathrm { K } ^ { \circ a }$-module ifand only ifall To$\mathrm { r } _ { i } ^ { \mathrm { K } ^ { \circ } } ( \mathrm { M } _ { * } , \mathrm { N } )$are almost zero for all$i > 0$and all$\mathrm { K } ^ { \circ }$-modules N. Hence if$\mathrm { M } _ { * }$is a flat$\mathrm { K } ^ { \circ }$-module, then M is a flat$\mathrm { K } ^ { \circ a }$-module. Conversely, choosing$\mathrm { N } = \mathrm { K } ^ { \circ } / \varpi$and$i = 1$, we find that the kernel of multiplication by  on$\mathrm { M } _ { * }$is almost zero. But

$$
\mathrm{M} _ {*} = \operatorname{Hom} _ {\mathrm{K} ^ {\circ a}} \left(\mathrm{K} ^ {\circ a}, \mathrm{M}\right) = \operatorname{Hom} _ {\mathrm{K} ^ {\circ}} (\mathfrak {m}, \mathrm{M} _ {*})
$$

does not have nontrivial almost zero elements, hence has no  -torsion. But a$\mathrm { K } ^ { \circ }$-module N is flat if and only if it has no -torsion.

(ii) We have

$$
\mathrm{M} _ {*} = \operatorname{Hom} _ {\mathrm{K} ^ {\circ a}} \left(\mathrm{K} ^ {\circ a}, \mathrm{M}\right) = \operatorname{Hom} _ {\mathrm{K} ^ {\circ}} (\mathfrak {m}, \mathrm{N}).
$$

As N is flat over$\mathrm { K } ^ { \circ } { } _ { i }$, we can write the last term as the subset of those

$$
x \in \mathrm{Hom} _ {\mathrm{K}} \bigg (\mathrm{K}, \mathrm{N} \bigg [ \frac {1}{\varpi} \bigg ] \bigg) = \mathrm{N} \bigg [ \frac {1}{\varpi} \bigg ]
$$

satisfying the condition that for all$\epsilon \in { \mathfrak { m } }$, we have$\epsilon x \in \mathrm { N }$

(iii) Note that$( x \mathbf { M } _ { * } ) ^ { a } = x \mathbf { M } _ { \mathrm { \Omega } }$, and xM is a flat$\mathrm { K } ^ { \circ }$-module. Hence

$$
(x \mathrm{M}) _ {*} = \operatorname{Hom} (\mathfrak {m}, x \mathrm{M} _ {*}) = \left\{y \in \mathrm{M} _ {*} \left[ \frac {1}{\varpi} \right] \Big | \forall \epsilon \in \mathfrak {m}: \epsilon y \in x \mathrm{M} _ {*} \right\} = x \mathrm{M} _ {*}.
$$

Now using that is left-exact (since right-adjoint to$\mathbf { M } \mapsto \mathbf { M } ^ { a } ) ,$we get the inclusion$\mathrm { M } _ { * } / x \mathrm { M } _ { * } \subset ( \mathrm { M } / x \mathrm { M } ) ,$. If$m \in \left( \mathrm { M } / x \mathrm { M } \right)$lifts to$\tilde { m } \in ( \mathrm { M } / x \epsilon \mathrm { M } ) _ { * }$,then evaluate $\tilde { m } \in \mathrm { H o m } ( \mathfrak { m } , \mathrm { M } _ { * } / x \epsilon \mathrm { M } _ { * } )$on . This gives an element$n = \tilde { m } ( \epsilon ) \in \mathrm { M } _ { * } / x \epsilon \mathrm { M } _ { * }$, which we lift to$\tilde { n } \in \mathbf { M } _ { * }$. One checks that n˜ is divisible by$\epsilon :$It suffices to check that δn˜ is divisible by for any$\delta \in { \mathfrak { m } }$. But$\delta n = \delta \tilde { m } ( \epsilon ) = \epsilon \tilde { m } ( \delta )$lies in$\epsilon \mathrm { M } _ { * } / x \epsilon \mathrm { M } _ { * }$, hence$\delta \tilde { n } \in \epsilon \mathrm { M } _ { * }$

Then$\begin{array} { r } { m _ { 1 } = \frac { \tilde { n } } { \epsilon } \in \mathrm { M } _ { * } } \end{array}$is the desired lift of$m \in ( \mathrm { M } / x \mathrm { M } ) ,$: Multiplication by$\epsilon$induces an injection$( \mathrm { M } / x \mathrm { M } ) _ { * } \to ( \mathrm { M } / x \epsilon \mathrm { M } ) _ { * }$, because <sub>∗</sub> is left-exact, and the images agree:$\tilde { n }$ maps to$\epsilon m = \tilde { m } ( \epsilon ) = n$in$( \mathrm { M } / x \epsilon \mathrm { M } )$<sub>∗</sub>.

(iv) The functors$\mathrm { M } \mapsto \mathrm { M } _ { * }$and$\mathrm { N } \mapsto \mathrm { N } ^ { a }$between the category of$\mathrm { K } ^ { \circ a }$-modules and the category of K<sup>◦</sup>-modules admit left adjoints, given by$\mathrm { N } \mapsto \mathrm { N } ^ { a }$and$\mathbf { M } \mapsto \mathbf { M } _ { ! } =$ ${ \mathfrak { m } } \otimes \mathbf { M } _ { * }$, respectively, and hence commute with inverse limits. Now if M is  -adically complete, then

$$
\mathrm{M} _ {*} = \left(\varprojlim \mathrm{M} / \varpi^ {n} \mathrm{M}\right) _ {*} = \varprojlim \left(\mathrm{M} / \varpi^ {n} \mathrm{M}\right) _ {*} = \varprojlim \mathrm{M} _ {*} / \varpi^ {n} \mathrm{M} _ {*},
$$

using part (iii) in the last equality, hence$\mathrm { M } _ { * }$is  -adically complete. Conversely, if$\mathrm { M } _ { * }$is -adically complete, then

$$
\mathrm{M} = \left(\mathrm{M} _ {*}\right) ^ {a} = \left(\varprojlim \mathrm{M} _ {*} / \varpi^ {n} \mathrm{M} _ {*}\right) ^ {a} = \varprojlim \left(\mathrm{M} _ {*} / \varpi^ {n} \mathrm{M} _ {*}\right) ^ {a} = \varprojlim \mathrm{M} / \varpi^ {n} \mathrm{M}.
$$

Proposition 5.5. — Let R be a perfectoid K-algebra. Then  induces an isomorphism $\mathrm { R } ^ { \circ } / \varpi ^ { 1 / p } \cong \mathrm { R } ^ { \circ } / \varpi$, and$\mathbf { A } = \mathbf { R } ^ { \circ a }$is a perfectoid$\mathrm { K } ^ { \circ a }$-algebra.

Proof. — By assumption,$\Phi$is surjective. Injectivity is clear: If$x \in \mathrm { R } ^ { \circ }$is such that $x ^ { p } / \varpi$is powerbounded, then$x / \varpi ^ { 1 / p }$is powerbounded. Obviously,$\mathrm { R } ^ { \circ }$is  -adically complete and flat over$\mathrm { K } ^ { \circ } { } _ { ; }$; now the previous lemma shows that$\mathrm { R } ^ { \circ a }$is  -adically complete and flat over$\mathrm { K } ^ { \circ a }$-

Lemma 5.6. — Let A be a perfectoid$\mathrm { K } ^ { \circ a }$-algebra, and let$\mathrm { R } = \mathrm { A } _ { * } [ \varpi ^ { - 1 } ]$. Equip R with the Banach K-algebra structure making$\mathrm { A } _ { * }$open and bounded. Then$\mathrm { A } _ { * } = \mathrm { R } ^ { \circ }$is the set ofpower-bounded elements, R is perfectoid, and

$$
\Phi : \mathrm{A} _ {*} / \varpi^ {1 / p} \cong \mathrm{A} _ {*} / \varpi .
$$

Proof. — By definition,  is an isomorphism$\mathrm { A } / \varpi ^ { 1 / p } \cong \mathrm { A } / \varpi$, hence$\Phi$is an almost isomorphism$\mathrm { A } _ { * } / \varpi ^ { 1 / p }  \mathrm { A } _ { * } / \varpi$. It is injective:$\mathrm { I f } x \in \mathrm { A } _ { * }$and$x ^ { p } \in \varpi \mathrm { A } _ { * }$, then for all$\epsilon \in { \mathfrak { m } }$ $\epsilon x \in \varpi ^ { 1 / p } \mathrm { A } _ { * }$by almost injectivity, hence$x \in ( \varpi ^ { 1 / p } \mathrm { A } ) _ { * } = \varpi ^ { 1 / p } \mathrm { A } _ { * }$

Lemma 5.7. — Assume that$x \in \mathrm { R }$satisfies$x ^ { p } \in \mathrm { A } _ { * }$. Then$x \in \mathrm { A } _ { * }$

Proof. — Injectivity of$\Phi$says that if$y \in \mathrm { A } _ { * }$satisfies$y ^ { \boldsymbol { p } } \in \varpi \mathrm { A } _ { * } ,$then$y \in \varpi ^ { \frac { 1 } { p } } \mathrm { A } _ { * }$ There is some positive integer k such that$y = \varpi ^ { \frac { k } { p } } x \in \mathrm { A } _ { * } ,$, and as long as$k \geq 1 , y ^ { \flat } \in \varpi \mathrm { A } _ { * } ,$ so that$y \in \varpi ^ { \frac { 1 } { \beta } } \mathrm { A } _ { * }$. Because$\mathrm { A } _ { * }$has no -torsion, we get$\varpi ^ { \frac { k - 1 } { \beta } } \boldsymbol { x } \in \mathrm { A } _ { * } . \mathrm { B y }$induction, we get the result.-

Obviously,$\mathrm { A } _ { * }$consists of power-bounded elements. Now assume that$x \in \mathrm { R }$is power-bounded. Then x is topologically nilpotent for all$\epsilon \in { \mathfrak { m } }$. In particular,$( \epsilon x ) ^ { p ^ { \mathrm { N } } } \in \mathbf { A } _ { * }$ for N sufficiently large. By the last lemma, this implies$\epsilon x \in \mathrm { A } _ { * }$. This is true for all$\epsilon \in { \mathfrak { m } }$ so that by Lemma 5.3(ii), we have$x \in \mathrm { A } _ { * }$

Next,  is surjective: It is almost surjective, hence it suffices to show that the composition$\mathrm { A } _ { * } / \varpi ^ { 1 / p }  \mathrm { A } _ { * } / \varpi  \mathrm { A } _ { * } / \mathfrak { m }$is surjective. Let$x \in \mathrm { A } _ { * }$. By almost surjectivity,$\varpi ^ { 1 / p } x \equiv y ^ { p }$modulo$\varpi \mathrm { A } _ { * } ,$for some$y \in \mathrm { A } _ { * }$. Let$\begin{array} { r } { z = \frac { y } { \varpi ^ { 1 / p ^ { 2 } } } } \end{array}$. This implies$z ^ { p } \equiv x$modulo$\varpi ^ { ( p - 1 ) / P } \mathrm { A } _ { * }$, in particular$\tilde { z } ^ { p } \in \mathrm { A } _ { * }$. By the lemma, also$z \in \mathrm { A } _ { * }$. As$x \equiv \tilde { \mathcal { Z } } ^ { p }$modulo $\varpi ^ { ( \boldsymbol { p } - 1 ) / P } \mathrm { A } _ { * } ,$in particular modulo m$\mathrm { A } _ { * } ,$this gives the desired surjectivity.

Finally, we see that R is a Banach K-algebra such that$\mathrm { R } ^ { \circ } = \mathrm { A } _ { * }$is open and bounded, and such that$\Phi$is surjective on$\mathrm { R } ^ { \circ } / \varpi = \mathrm { A } _ { * } / \varpi$. This means that R is perfectoid, as desired.

In particular, we get the desired equivalence$\mathrm { K } ^ { \circ a } - \mathrm { P e r f } \cong \mathrm { K - P e r f }$. Let us note some further propositions.-

Proposition 5.8. — Let R be a perfectoid K-algebra. Then R is reduced.

Proof. — Assume$0 \neq x \in \mathbf { R }$is nilpotent. Then$\mathrm { K } x \subset \mathrm { R } ^ { \circ }$, contradicting the condition that$\mathrm { R } ^ { \circ }$is bounded.-

If K has characteristic$\beta ,$being perfectoid is basically the same as being perfect.

Proposition 5.9. — Let K be ofcharacteristic$\beta ,$and let R be a Banach K-algebra such that the set ofpowerbounded elements$\mathrm { R } ^ { \circ } \subset \mathrm { R }$is open and bounded. Then R is perfectoid ifand only ifR is perfect.

Proof. — Assume R is perfect. Then also$\mathrm { R } ^ { \circ }$is perfect, as an element x is powerbounded if and only if$\chi ^ { \boldsymbol { \rho } }$is powerbounded. In particular,$\Phi : \mathrm { R } ^ { \circ } / \varpi  \mathrm { R } ^ { \circ } / \varpi$is surjective.

Now assume that R is perfectoid, hence by Proposition 5.5,  induces an isomorphism$\mathrm { R } ^ { \circ } / \varpi ^ { \frac { 1 } { \beta } } \cong \mathrm { R } ^ { \circ } / \varpi$. By successive approximation, we see that$\mathrm { R } ^ { \circ }$is perfect, and then that R is perfect.-

In order to finish the proof of Theorem 5.2, it suffices to prove the following result.

Theorem 5.10. — The functor$\mathrm { A } \mapsto \overline { { \mathrm { A } } } = \mathrm { A } / \varpi$induces an equivalence of categories $\mathrm { K } ^ { \circ a } - \mathrm { P e r f } \cong ( \mathrm { K } ^ { \circ a } / \varpi )$-Perf.

In other words, we have to prove that a perfectoid$\mathrm { K } ^ { \circ a } / \varpi$-algebra admits a unique deformation to$\mathrm { K } ^ { \circ a }$. For this, we will use the theory of the cotangent complex. Let us briefly recall it here.

In classical commutative algebra, the definition of the cotangent complex is due to Quillen [29] and its theory was globalized on toposes and applied to deformation problems by Illusie [23, 24]. To any morphism$\mathrm { R } \to \mathrm { S }$of rings, one associates a complex $\mathbf { L } _ { \mathrm { S / R } } \in \mathbf { D } ^ { \leq 0 } ( \mathrm { S } )$, where D(S) is the derived category of the category of S-modules, and $\mathrm { D } ^ { \leq 0 } ( \mathrm { S } ) \subset \mathrm { D } ( \mathrm { S } )$denotes the full subcategory of objects which have trivial cohomology in positive degrees. The cohomology in degree 0 of$\mathbf { L } _ { \mathrm { S / R } }$is given by$\Omega _ { \mathrm { S / R } } ^ { 1 }$, and for any morphisms$\mathrm { R \to S \to T }$of rings, there is a triangle in D(T):

$$
\mathrm{T} \otimes_ {\mathrm{S}} ^ {\mathbf {L}} \mathbf {L} _ {\mathrm{S/R}} \rightarrow \mathbf {L} _ {\mathrm{T/R}} \rightarrow \mathbf {L} _ {\mathrm{T/S}} \rightarrow ,
$$

extending the short exact sequence

$$
\mathrm{T} \otimes_ {\mathrm{S}} \Omega_ {\mathrm{S/R}} ^ {1} \to \Omega_ {\mathrm{T/R}} ^ {1} \to \Omega_ {\mathrm{T/S}} ^ {1} \to 0.
$$

Let us briefly recall the construction. First, one uses the Dold-Kan equivalence to reinterpret$\mathrm { D } ^ { \leq 0 } ( \mathrm { S } )$as the category of simplicial S-modules modulo weak equivalence. Now one takes a simplicial resolution$\mathrm { S } _ { \bullet }$ofthe R-algebra S by free R-algebras. Then one defines$\mathbf { L } _ { \mathrm { S / R } }$as the object of$\mathrm { D } ^ { \leq 0 } ( \mathrm { S } )$associated to the simplicial S-module$\Omega _ { \mathrm { S } _ { \bullet } / \mathrm { R } } ^ { 1 } \otimes _ { \mathrm { S } _ { \bullet } } \mathrm { S }$

Just as under certain favorable assumptions, one can describe many deformation problems in terms of tangent or normal bundles, it turns out that in complete generality, one can describe them via the cotangent complex. In special cases, this gives back the classical results, as e.g. if$\mathrm { R }  \mathrm { S }$is a smooth morphism, then$\mathbf { L } _ { \mathrm { S / R } }$is concentrated in degree 0, and is given by the cotangent bundle.

Specifically, we will need the following results. Fix some ring R with an ideal$\mathrm { ~ I ~ C ~ R ~ }$ such that$\mathrm { { I } ^ { 2 } = 0 }$. Moreover, fix a flat$\mathrm { R _ { 0 } } = \mathrm { R } / \mathrm { I } \mathrm { - a l g e b r a }$$\mathrm { S } _ { 0 }$. We are interested in the obstruction towards deforming$\mathrm { S } _ { 0 }$to a flat R-algebra S.

Theorem 5.11 ([23, III.2.1.2.3], [15, Proposition 3.2.9]). — There is an obstruction class in$\mathrm { E x t ^ { 2 } ( { \bf L } _ { S _ { 0 } / R _ { 0 } } , S _ { 0 } \otimes _ { R _ { 0 } } I ) }$which vanishes precisely when there exists a flat R-algebra S such that $\mathrm { ~ S ~ } \otimes _ { \mathrm { R } } \mathrm { ~ R _ { 0 } = S _ { 0 } ~ }$. If there exists such a deformation, then the set of all isomorphism classes of such deformationsforms a torsor under$\mathrm { E x t } ^ { 1 } ( \mathbf { L } _ { \mathrm { S _ { 0 } / R _ { 0 } } } , \mathbf { S } _ { 0 } \otimes _ { \mathrm { R _ { 0 } } } \mathbf { I } )$, and every deformation has automorphism group$\mathrm { H o m } ( \mathbf { L } _ { \mathrm { S } _ { 0 } / \mathrm { R } _ { 0 } } , \mathbf { S } _ { 0 } \otimes _ { \mathrm { R } _ { 0 } } \mathrm { I } )$

Here, a deformation comes with the isomorphism$\mathrm { ~ S ~ } \otimes _ { \mathrm { { R } } } \mathrm { ~ R _ { 0 } ~ } \cong \mathrm { ~ S _ { 0 } ~ }$, and isomorphisms of deformations are required to act trivially on$\mathrm { S } \otimes _ { \mathrm { R } } \mathrm { R } _ { \mathrm { 0 } } = \mathrm { S } _ { \mathrm { 0 } }$

Now assume that one has two flat R-algebras S, S<sup></sup> with reduction$\mathrm { S } _ { 0 } , \mathrm { S } _ { 0 } ^ { \prime }$to$\mathrm { R _ { 0 } }$, and a morphism$f _ { 0 } : \mathrm { S } _ { 0 } \to \mathrm { S } _ { 0 } ^ { \prime }$. We are interested in the obstruction to lifting$f _ { 0 }$to a morphism $f : \mathrm { S } \to \mathrm { S } ^ { \prime }$

Theorem 5.12 ([23, III.2.2.2], [15, Proposition 3.2.16]). — There is an obstruction class in Ext<sup>1</sup>$( \mathbf { L } _ { \mathrm { S } _ { 0 } / \mathrm { R } _ { 0 } } , \mathbf { S } _ { 0 } ^ { \prime } \otimes _ { \mathrm { R } _ { 0 } } \mathrm { I } )$which vanishes precisely when there exists an extension off$t o f : \mathrm { S } \to \mathrm { S } ^ { \prime }$ Ifthere exists such a lift, then the set ofall liftsforms a torsor under Hom$( \mathbf { L } _ { \mathrm { S } _ { 0 } / \mathrm { R } _ { 0 } } , \mathbf { S } _ { 0 } ^ { \prime } \otimes _ { \mathrm { R } _ { 0 } } \mathbf { I } )$

We will need the following criterion for the vanishing of the cotangent complex. This appears as Lemma 6.5.13(i) in [15].

Proposition 5.13.

(i) Let R be a perfect F -algebra. Then$\mathbf { L } _ { \mathrm { R } / \mathbf { F } _ { b } } \cong 0$

(ii) Let$\mathrm { R }  \mathrm { S }$be a morphism of$\mathbf { F } _ { p }$-algebras. Let$\mathrm { R } _ { ( \Phi ) }$be the ring R with the R-algebra structure via$\Phi : \mathrm { R }  \mathrm { R } \ .$, and define$\mathrm { S } _ { ( \Phi ) }$similarly. Assume that the relative Frobenius $\Phi _ { \mathrm { S / R } }$induces an isomorphism

$$
\mathrm{R} _ {(\Phi)} \otimes_ {\mathrm{R}} ^ {\mathbf {L}} \mathrm{S} \rightarrow \mathrm{S} _ {(\Phi)}
$$

in D(R). Then$\mathbf { L } _ { \mathrm { S / R } } \cong 0$

Remark 5.14. — Of course, (i) is a special case of (ii), and we will only need part (ii). However, we feel that (i) is an interesting statement that does not seem to be very wellknown. It allows one to define the ring of Witt vectors W(R) of R simply by saying that it is the unique deformation of R to a flat p-adically complete$\mathbf { Z } _ { p }$-algebra. Also note that it is clear that$\Omega _ { \mathrm { R } / \mathbf { F } _ { \phi } } ^ { 1 } = 0$in part (i): Any$x \in \mathrm { R }$can be written as$y ^ { \flat } ,$, and then$d x = d y ^ { p } =$ $p y ^ { p - 1 } d y = 0$. This identity is at the heart of this proposition.

Proof. — We sketch the proof of part (ii), cf. proof of Lemma 6.5.13(i) in [15]. Let $\mathrm { S } ^ { \bullet }$be a simplicial resolution of S by free R-algebras. We have the relative Frobenius map

$$
\Phi_ {\mathrm{S} ^ {\bullet} / \mathrm{R}}: \mathrm{R} _ {(\Phi)} \otimes_ {\mathrm{R}} \mathrm{S} ^ {\bullet} \rightarrow \mathrm{S} _ {(\Phi)} ^ {\bullet}.
$$

Note that identifying$\mathrm { S } ^ { k }$with a polynomial algebra$\mathrm { R } [ \mathrm { X } _ { 1 } , \mathrm { X } _ { 2 } , \ldots ]$, the relative Frobenius map$\Phi _ { \mathrm { S } ^ { k } / \mathrm { R } }$is given by the$\mathrm { R _ { ( \Phi ) } } \mathrm { - a l g e b r a }$map sending$\mathrm { X } _ { i } \mapsto \mathrm { X } _ { i } ^ { p }$

The assumption says that$\Phi _ { \mathrm { S } ^ { \bullet } / \mathrm { R } }$induces a quasiisomorphism of simplicial$\mathrm { R } _ { ( \Phi ) } -$ algebras. This implies that$\Phi _ { \mathrm { S } ^ { \bullet } / \mathrm { R } }$gives an isomorphism

$$
\mathbf {R} _ {(\Phi)} \otimes_ {\mathrm{R}} ^ {\mathbf {L}} \mathbf {L} _ {\mathrm{S/R}} \cong \mathbf {L} _ {\mathrm{S} _ {(\Phi)} / \mathrm{R} _ {(\Phi)}}.
$$

On the other hand, the explicit description shows that the map induced by$\Phi _ { \mathrm { S } ^ { k } / \mathrm { R } }$on differentials will map$d \mathrm { X } _ { i }$to$d \mathrm { X } _ { i } ^ { p } = 0$, and hence is the zero map. This shows that $\mathbf { L } _ { \mathrm { S } _ { ( \Phi ) } / \mathrm { R } _ { ( \Phi ) } } \cong 0$, and we may identify this with$\mathbf { L } _ { \mathrm { S / R } }$-

In their book [15], Gabber and Ramero generalize the theory of the cotangent complex to the almost context. Specifically, they show that if$\mathrm { R } \to \mathrm { S }$is a morphism of$\mathrm { K } ^ { \circ } \cdot$ algebras, then${ \bf L } _ { \mathrm { S / R } } ^ { a }$as an element of$\mathrm { D } ( \mathrm { S } ^ { a } )$, the derived category of$\mathrm { \Delta S ^ { \it a } }$-modules, depends only the morphism$\mathrm { R } ^ { a } \to \mathrm { S } ^ { a }$of almost$\mathrm { K } ^ { \circ }$-algebras. This allows one to define$\mathbf { L } _ { \mathrm { B / A } } ^ { a } \in$ $\scriptstyle \mathrm { D } ^ { \leq 0 } ( \mathrm { B } )$for any morphism$\mathrm { A }  \mathrm { B }$of$\mathrm { K } ^ { \circ a }$-algebras. With this modification, the previous theorems stay true in the almost world without change.

Remark 5.15. — In fact, the cotangent complex$\mathbf { L } _ { \mathrm { B / A } }$is defined as an object of a derived category of modules over an actual ring in [15], but for our purposes it is enough to consider its almost version${ \bf L } _ { \mathrm { B / A } } ^ { a }$

Corollary 5.16. — Let$\overline { { \mathrm A } }$be a perfectoid K<sup>◦a</sup>/ -algebra. Then$\mathbf { L } _ { \mathrm { \overline { { A } } / ( K ^ { \circ a } / \varpi ) } } ^ { a } \cong 0$

Proof. — This follows from the almost version of Proposition 5.13, which can be proved in the same way. Alternatively, argue with${ \bf B } = ( \overline { { \Lambda } } \times \mathrm { K } ^ { \circ a } / \varpi ) _ { ! ! }$, which is a flat $\mathrm { K } ^ { \circ } / \varpi \mathrm { - a l g e b r a }$such that$\mathbf { B } / \varpi ^ { 1 / p } \cong \mathbf { B }$via . Here, we use the functor$\mathrm { C } \mapsto \mathrm { C } _ { ! ! }$from [15], §2.2.25.-

Now we can prove Theorem 5.10.

ProofofTheorem${ 5 . } I { 0 . } - \mathrm { { L e t } } \overline { { \mathrm { { A } } } }$be a perfectoid$\mathrm { K } ^ { \circ a } / \varpi \mathrm { - a l g e b r a }$. We see inductively that all obstructions and ambiguities in lifting inductively to a flat$( \mathrm { K } ^ { \circ } / \varpi ^ { n } ) ^ { a } { \mathrm { - a l g e b r a ~ } } \overline { { \mathrm { A } } } _ { n }$ vanish: All groups occurring can be expressed in terms of the cotangent complex by the theorems above, so that it suffices to show that${ \bf L } _ { \overline { { \mathrm { A } } } _ { n } / ( \mathrm { K } ^ { \circ } / \varpi ^ { n } ) ^ { a } } ^ { a } = 0$. But by Theorem 2.5.36 of [15], the short exact sequence

$$
0 \to \overline {{\mathrm{A}}} \stackrel {\varpi^ {n - 1}} {\to} \overline {{\mathrm{A}}} _ {n} \to \overline {{\mathrm{A}}} _ {n - 1} \to 0
$$

induces after tensoring with${ \bf L } _ { \overline { { \mathrm { A } } } _ { n } / ( \mathrm { K } ^ { \circ } / \varpi ^ { n } ) ^ { a } }$a triangle

$$
\mathbf {L} _ {\mathrm{A} / (\mathrm{K} ^ {\circ} / \varpi) ^ {a}} ^ {a} \rightarrow \mathbf {L} _ {\mathrm{A} _ {n} / (\mathrm{K} ^ {\circ} / \varpi^ {n}) ^ {a}} ^ {a} \rightarrow \mathbf {L} _ {\mathrm{A} _ {n - 1} / (\mathrm{K} ^ {\circ} / \varpi^ {n - 1}) ^ {a}} ^ {a} \rightarrow ,
$$

and the claim follows by induction.

This gives a unique system of flat$( \mathbf { K } ^ { \circ } / \varpi ^ { n } ) ^ { a }$-algebras${ \overline { { \mathbf { A } } } } _ { n }$with isomorphisms

$$
\overline {{\mathrm{A}}} _ {n} / \varpi^ {n - 1} \cong \overline {{\mathrm{A}}} _ {n - 1}.
$$

Let A be their inverse limit. Then A is  -adically complete with$\operatorname { A } / \varpi ^ { n } \mathrm { A } = { \overline { { \mathrm { A } } } } _ { n }$. This shows that A is perfectoid, and we get an equivalence between perfectoid$\mathrm { K } ^ { \circ a }$-algebras and perfectoid$\mathrm { K } ^ { \circ a } / \varpi \mathrm { - a l g e b r a s . }$, as desired.-

In particular, we also arrive at the tilting equivalence,$\mathrm { K } { \cdot } \mathrm { P e r f } \cong \mathrm { K } ^ { \flat } { \cdot } \mathrm { P e r f } .$. We want to compare this with Fontaine’s construction. Let R be a perfectoid K-algebra, with$\mathrm { A } =$ $\mathrm { R } ^ { \circ a }$. Define

$$
\mathrm{A} ^ {\flat} = \varprojlim_ {\Phi} \mathrm{A} / \varpi ,
$$

which we regard as a$\mathrm { K } ^ { \mathsf { b o } a }$-algebra via

$$
\mathrm{K} ^ {\flat \circ a} = \left(\varprojlim_ {\Phi} \mathrm{K} ^ {\circ} / \varpi\right) ^ {a} = \varprojlim_ {\Phi} \left(\mathrm{K} ^ {\circ} / \varpi\right) ^ {a} = \varprojlim_ {\Phi} \mathrm{K} ^ {\circ a} / \varpi ,
$$

and set$\mathrm { R } ^ { \flat } = \mathrm { A } _ { * } ^ { \flat } [ ( \varpi ^ { \flat } ) ^ { - 1 } ]$

Proposition 5.17. — This defines a perfectoid K<sup>-</sup>-algebra$\mathrm { R } ^ { \flat }$with corresponding perfectoid K<sup>-◦a</sup>-algebra$\mathrm { A } _ { ~ i } ^ { \flat }$, and$\mathrm { \sf R } ^ { \flat }$is the tilt of R. Moreover,

$$
\mathrm{R} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{R}, \quad \mathrm{A} _ {*} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {\flat}} \mathrm{A} _ {*}, \quad \mathrm{A} _ {*} ^ {\flat} / \varpi^ {\flat} \cong \mathrm{A} _ {*} / \varpi .
$$

In particular, we have a continuous multiplicative map$\mathbb { R } ^ { \flat } \to \mathbb { R } , x \mapsto x ^ { \sharp }$

Remark 5.18. — It follows that the tilting functor is independent of the choice of $\varpi$and$\varpi ^ { \flat }$. We note that this explicit description comes from the fact that the lifting from perfectoid$\mathrm { K } ^ { \flat \circ a } / \varpi ^ { \flat }$-algebras to perfectoid$\mathrm { K } ^ { \flat \circ a }$-algebras can be made explicit by means of the inverse limit over the Frobenius.

Proof. — First, we have

$$
\mathrm{A} _ {*} ^ {\flat} = \left(\varprojlim_ {\Phi} \mathrm{A} / \varpi\right) _ {*} = \varprojlim_ {\Phi} (\mathrm{A} / \varpi) _ {*} = \varprojlim_ {\Phi} \mathrm{A} _ {*} / \varpi ,
$$

because commutes with inverse limits and using Lemma 5.3(iii). Note that the image of$\Phi : ( \mathrm { A } / \varpi ) _ { * } \to ( \mathrm { A } / \varpi )$is$\mathrm { A } _ { * } / \varpi$, because it factors over$( \mathrm { A } / \varpi ^ { 1 / p } ) _ { \ast }$, and the image of the projection$( \mathrm { A } / \varpi ) _ { * } \to ( \mathrm { A } / \varpi ^ { 1 / p } )$) is$\mathrm { A } _ { \ast } / \varpi ^ { 1 / p }$. But

$$
\varprojlim_ {\Phi} \mathrm{A} _ {*} / \varpi = \varprojlim_ {x \mapsto x ^ {p}} \mathrm{A} _ {*},
$$

as in the proof of Lemma$3 . 4 ( \mathrm { { i } ) }$

This shows that$\mathrm { A } _ { * } ^ { \flat }$is a$\varpi ^ { \flat }$-adically complete flat$\mathrm { K } ^ { \flat \circ }$-algebra. Moreover, the projection$x \mapsto x ^ { \sharp }$of$\mathrm { A } _ { * } ^ { \flat }$onto the first component$x ^ { \sharp } \in \mathrm { A } ,$induces an isomorphism

$$
\mathrm{A} _ {*} ^ {\flat} / \varpi^ {\flat} \cong \mathrm{A} _ {*} / \varpi ,
$$

because of Lemma 5.6. Therefore$\mathrm { A } ^ { \flat }$is a perfectoid$\mathrm { K } ^ { \mathsf { b o } a }$-algebra.

To see that$\mathrm { R } ^ { \flat }$is the tilt of R, we go through all equivalences. Indeed, R has corresponding perfectoid$\mathrm { K } ^ { \circ a }$-algebra A, which reduces to the perfectoid$\mathrm { K } ^ { \circ a } / \varpi \mathrm { - a l g e b r a }$ $\mathrm { A } / \varpi$, which is the same as the perfectoid$\mathrm { K } ^ { \flat \circ a } / \varpi ^ { \flat } .$-algebra$\mathrm { A } ^ { \flat } / \varpi ^ { \flat }$, which lifts to the perfectoid$\mathrm { K } ^ { \flat \circ a }$-algebra$\mathrm { A } ^ { \flat }$, which in turn gives rise to$\mathrm { R } ^ { \flat }$-

Remark 5.19. — In fact, one can write down the functors in both directions. From characteristic 0 to characteristic$\beta ,$we have already given the explicit functor. The converse functor is given by${ \mathrm { R } } = { \mathrm { W } } ( { \mathrm { R } } ^ { \flat \circ } ) \otimes _ { \mathrm { W ( K ^ { \flat \circ } ) } } { \mathrm { K } }$, using the usual map$\theta : \mathrm { W } ( \mathrm { K } ^ { \flat \circ } )  \mathrm { K }$ We leave it as an exercise to the reader to give a direct proof of the theorem via this description, cf. [28]. This avoids the use of almost mathematics in the proof of the tilting equivalence. We stress however that in our proofwe never need to talk about big rings like $\operatorname { W } ( \mathbf { R } ^ { \flat \circ } )$, and that the point of view of the given proof will be useful in later arguments.

Let us give a prototypical example for the tilting process.

Proposition 5.20. — Let

$$
\mathrm{R} = \mathrm{K} \big \langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \ldots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \big \rangle = \mathrm{K} ^ {\circ} \big [ \widehat {\mathrm{T} _ {1} ^ {1 / p ^ {\infty}} , \ldots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}}} \big ] \big [ \varpi^ {- 1} \big ].
$$

Then R is a perfectoid K-algebra, and its tilt$\mathrm { R } ^ { \flat }$is given by$\mathrm { K } ^ { \flat } \langle \mathrm { T } _ { 1 } ^ { 1 / \flat ^ { \infty } } , \ldots , \mathrm { T } _ { n } ^ { 1 / \flat ^ { \infty } } \rangle$

Proof. — One checks that$\mathbf { R } ^ { \circ } = \mathbf { K } ^ { \circ } [ \mathbf { T } _ { 1 } ^ { 1 / \rho ^ { \infty } } , \ldots , \mathbf { T } _ { n } ^ { 1 / \rho ^ { \infty } } ] _ { : }$, which is  -adically complete and flat over$\mathrm { K } ^ { \circ }$. Moreover, it reduces to$\mathbf { R } ^ { \circ } / \varpi = \mathbf { K } ^ { \circ } / \varpi [ \boldsymbol { \mathrm { T } } _ { 1 } ^ { 1 / \boldsymbol { \beta } ^ { \infty } } , \ldots , \boldsymbol { \mathrm { T } } _ { n } ^ { 1 / \boldsymbol { \beta } ^ { \infty } } ]$, on which Frobenius is surjective. This shows that R is a perfectoid K-algebra.

To see that its tilt has the desired form, we only have to check that$\mathrm { R } ^ { \circ } / \varpi =$ $\mathrm { R } ^ { \flat \circ } / \varpi ^ { \flat }$, by the proof of the tilting equivalence. But this is obvious.-

We note that under the process of tilting, perfectoid fields are identified.

Lemma 5.21. — Let R be a perfectoid K-algebra with tilt R<sup>-</sup>. Then R is a perfectoidfield if and only$i f { \bf R } ^ { \flat }$is a perfectoid field.

Proof. — Note that R is a perfectoid field if and only if it is a nonarchimedean field, i.e. a field whose topology is induced by a rank-1-valuation. This valuation is necessarily given by the spectral norm

$$
\| x \| _ {\mathrm{R}} = \inf \left\{\left| t \right| ^ {- 1} \mid t \in \mathrm{K} ^ {\times}, t x \in \mathrm{R} ^ {\circ} \right\}
$$

on$\mathrm { R } ,$and it is a rank-1-valuation if and only if it is multiplicative. It is easy to check that for$x \in \mathbf { R } ^ { \flat }$, we have$\| x \| _ { \mathrm { R } ^ { \flat } } = \| x ^ { \sharp } \| _ { \mathrm { R } }$. In particular,$\operatorname { i f } \parallel \cdot \parallel _ { \mathrm { R } }$is multiplicative, then so is$\Vert \cdot \Vert _ { \mathrm { R } ^ { \flat } }$ Also, if R is a field, then$\mathbf { R } ^ { \flat }$is a field, as$\mathbb { R } ^ { \flat } = \varprojlim _ { x \mapsto x ^ { \flat } } \mathbb { R }$as multiplicative monoids. Hence, if R is a perfectoid field, then so is$\mathrm { R } ^ { \flat }$

Conversely, assume that$\mathrm { \mathbf { R } } ^ { \flat }$is a perfectoid field. We have to check that the spectral norm$\Vert \cdot \Vert _ { \mathrm { R } }$on R is multiplicative. Let$x , y \in \operatorname { R } ;$after multiplication by elements of$\mathrm { K } .$, we may assume$x , y \in \mathrm { R } ^ { \circ }$, but not in$\varpi ^ { 1 / \ d p } \mathrm { R } ^ { \circ }$. We want to see that$\| x \| _ { \mathrm { R } } \| y \| _ { \mathrm { R } } = \| x y \| _ { \mathrm { R } }$. But we can find$x ^ { \mathrm { { b } } } , y ^ { \mathrm { { p } } } \in \mathbb { R } ^ { \mathrm { { b o } } }$with$x - ( x ^ { \flat } ) ^ { \sharp } , y - ( y ^ { \flat } ) ^ { \sharp } \in \varpi \mathrm { R } ^ { \circ }$. Then$\| x \| _ { \mathrm { R } } = \| x ^ { \flat } \| _ { \mathrm { R } ^ { \flat } } , \| y \| _ { \mathrm { R } } = \| y ^ { \flat } \| _ { \mathrm { R } ^ { \flat } }$ and$\| x y \| _ { \mathrm { R } } = \| x ^ { \flat } y ^ { \flat } \| _ { \mathrm { R } ^ { \flat } }$, and we get the claim.

Finally, to see that R is a field, choose x such that$x \in \mathrm { R } ^ { \circ }$, but not in$\varpi { \mathrm R } ^ { \circ }$, and take$x ^ { \mathrm { { b } } }$as before. Then by multiplicativity of$\begin{array} { r } { \| \cdot \| _ { \mathrm { R } } , \| 1 - \frac { x } { ( x ^ { \flat } ) ^ { \sharp } } \| _ { \mathrm { R } } < 1 } \end{array}$, and hence$\frac { x } { ( x ^ { \flat } ) ^ { \sharp } }$is invertible, and then also x.-

Finally, let us discuss finite étale covers of perfectoid algebras, and finish the proof of Theorem 3.7.

Proposition 5.22. — Let$\overline { { \mathrm A } }$be a perfectoid$\mathrm { K } ^ { \circ a } / \varpi - a l g e b r a .$, and let$\overline { { \mathrm B } }$be a finite étale ${ \overline { { \mathrm { A } } } } { - } a l g e b r a .$Then$\overline { { \mathrm B } }$is a perfectoid$K ^ { \circ a } / \varpi - a l g e b r a$

$P r o o f . - \mathrm { O b v i o u s l y , \ } \mathbf { \overline { { B } } }$is flat. The statement about Frobenius follows from Theorem 3.5.13(ii) of [15].-

In particular, Theorem 4.17 provides us with the following commutative diagram, where$\mathrm { R } , \mathrm { A } , \overline { { \mathrm { A } } } , \mathrm { A } ^ { \flat }$and$\mathrm { ~ R ~ } ^ { \flat }$form a sequence of rings under the tilting procedure.

$$
\begin{array}{c} R _ {\text {fet}} \xleftarrow {} A _ {\text {fet}} \xrightarrow {\cong} \overline {{A}} _ {\text {fet}} \xleftarrow {\cong} A _ {\text {fet}} ^ {\flat} \xrightarrow {} R _ {\text {fet}} ^ {\flat} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow \qquad \qquad \Biggl \downarrow \\ K - P e r f \xleftarrow {\cong} K ^ {\circ a} - P e r f \xrightarrow {\cong} (K ^ {\circ a} / \varpi) - P e r f \xleftarrow {\cong} K ^ {\flat o a} - P e r f \xrightarrow {\cong} K ^ {\flat} - P e r f \end{array}
$$

It follows from this diagram that the functors$\mathrm { A } _ { \mathrm { f e t } } \to \mathrm { R } _ { \mathrm { f e t } }$and$\mathrm { A } _ { \mathrm { f e t } } ^ { \flat } \to \mathrm { R } _ { \mathrm { f e t } } ^ { \flat }$are fully faithful. A main theorem is that both ofthem are equivalences: This amounts to Faltings’s almost purity theorem. At this point, we will prove this only in characteristic$\beta .$

Proposition 5.23. — Let K be ofcharacteristic$\beta ,$let R be a perfectoid K-algebra, and let$\mathrm { S } / \mathrm { R }$ befinite étale. Then S is perfectoid and$\mathrm { S } ^ { \circ a }$isfinite étale over$\mathrm { R } ^ { \circ a }$. Moreover,$\mathrm { S } ^ { \circ a }$is a uniformlyfinite projective$\mathbf { R } ^ { \circ a }$-module.

Remark 5.24. — We need to define the topology on S here. Recall that if A is any ring with$t \in \mathrm { A }$not a zero-divisor, then any finitely generated$\mathrm { A } [ t ^ { - 1 } ] { \mathrm { - m o d u l e ~ M } }$carries a canonical topology, which gives any finitely generated A-submodule of M the t-adic topology. Any morphism offinitely generated$\mathrm { A } [ t ^ { - 1 } ]$-modules is continuous for this topology, cf. [15], Definition 5.4.10 and 5.4.11. If A is complete and M is projective, then M is complete, as one checks by writing M as a direct summand of a finitely generated free A-module. In particular, if R is a perfectoid K-algebra and$\mathrm { S } / \mathrm { R }$a finite étale cover, then S has a canonical topology for which it is complete.

Proof. — This follows from Theorem 3.5.28 of [15]. Let us recall the argument. Note that S is a perfect Banach K-algebra. We claim that it is perfectoid. Let$\mathrm { S } _ { 0 } \subset \mathrm { S }$be some finitely generated R<sup>◦</sup>-subalgebra with$\mathrm { S } _ { 0 } \otimes \mathrm { K } = \mathrm { S }$. Let$\mathrm { S } _ { 0 } ^ { \perp } \subset \mathrm { S }$be defined as the set of all$x \in \mathrm { S }$such that$t _ { \mathrm { S / R } } ( x , \mathbf { S } _ { 0 } ) \subset \mathbf { R } ^ { \circ }$, using the perfect trace form pairing

$$
t _ {\mathrm{S/R}}: \mathrm{S} \otimes_ {\mathrm{R}} \mathrm{S} \to \mathrm{R};
$$

then$\mathrm { S } _ { 0 }$and$\mathrm { S } _ { 0 } ^ { \perp }$are open and bounded. Let Y be the integral closure of$\mathrm { R } ^ { \circ }$in S. Then $\mathrm { S } _ { 0 } \subset \mathrm { Y } \subset \mathrm { S } _ { 0 } ^ { \perp }$: Indeed, the elements of$\mathrm { S } _ { 0 }$are clearly integral over$\mathrm { R } ^ { \circ }$, and we have $t _ { \mathrm { S / R } } ( \mathrm { Y } , \mathrm { Y } ) \subset \mathrm { R } ^ { \circ }$. It follows that Y is open and bounded. As$\mathrm { S } ^ { \circ a } = \mathrm { Y } ^ { a }$, it follows that$\mathrm { S } ^ { \circ }$is open and bounded, as desired.

Next, we want to check that$\mathrm { S } ^ { \circ a }$is a uniformly finite projective$\mathrm { R } ^ { \circ a }$-module. For this, it is enough to prove that there is some n such that for any$\epsilon \in { \mathfrak { m } }$, there are maps $\mathbf { S } ^ { \circ }  \mathbf { R } ^ { \circ n }$and$\mathrm { R } ^ { \circ n } \to \mathrm { S } ^ { \circ }$whose composite is multiplication by .

Let$e \in \mathrm { S } \otimes _ { \mathrm { R } } \mathrm { S }$be the idempotent showing that S is unramified over R. Then${ \varpi ^ { \mathrm { N } } } _ { \ell }$ is in the image of$\mathrm { \Delta S ^ { \circ } \otimes _ { R ^ { \circ } } S ^ { \circ } }$in$\operatorname { S } \otimes _ { \operatorname { R } } \operatorname { S }$for some N. Write$\begin{array} { r } { { \bf \Phi } ^ { \mathrm { N } } e = \sum _ { i = 1 } ^ { n } x _ { i } \otimes y _ { i } } \end{array}$. As Frobenius is bijective, we have$\begin{array} { r } { \varpi ^ { \mathrm { N } / { p ^ { m } } } e = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 1 / { p ^ { m } } } \otimes y _ { i } ^ { 1 / { p ^ { m } } } } \end{array}$for all m. In particular, for any$\epsilon \in { \mathfrak { m } }$, we can write$\begin{array} { r } { \epsilon e = \sum _ { i = 1 } ^ { n } a _ { i } \otimes b _ { i } } \end{array}$for certain$a _ { i } , b _ { i } \in \mathrm { S } ^ { \circ }$, depending on .

We get the map$\mathbf { S } ^ { \circ }  \mathbf { R } ^ { \circ n }$

$$
s \mapsto \left(t _ {\mathrm{S} / \mathrm{R}} (s, b _ {1}), \dots , t _ {\mathrm{S} / \mathrm{R}} (s, b _ {n})\right),
$$

and the map$\mathrm { R } ^ { \circ n } \to \mathrm { S } ^ { \circ }$

$$
(r _ {1}, \dots , r _ {n}) \mapsto \sum_ {i = 1} ^ {n} a _ {i} r _ {i}.
$$

One easily checks that their composite is multiplication by , giving the claim.

It remains to see that$\mathrm { S } ^ { \circ a }$is an unramified$\mathrm { R } ^ { \circ a }$-algebra. But this follows from the previous arguments, which show that e defines an almost element of$\mathrm { S } ^ { \circ a } \otimes _ { \mathrm { R } ^ { \circ a } } \mathrm { S } ^ { \circ a }$with the desired properties.-

It follows that the diagram above extends as follows.

$$
\begin{array}{c} R _ {\text {fét}} \xleftarrow {} A _ {\text {fét}} \xrightarrow {\cong} \overline {{A}} _ {\text {fét}} \xleftarrow {\cong} A _ {\text {fét}} ^ {b} \xrightarrow {\cong} R _ {\text {fét}} ^ {b} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow \\ K - P e r f \xleftarrow {\cong} K ^ {\circ a} - P e r f \xrightarrow {\cong} (K ^ {\circ a} / \varpi) - P e r f \xleftarrow {\cong} K ^ {\flat o a} - P e r f \xrightarrow {\cong} K ^ {\flat} - P e r f \end{array}
$$

Moreover, using Theorem 4.17, it follows that all finite étale algebras over$\mathrm { A } , \overline { { \mathrm { A } } }$or$\mathrm { A } ^ { \flat }$are uniformly almost finitely presented. Let us summarize the discussion.

Theorem 5.25. — Let R be a perfectoid K-algebra with tilt$\mathrm { R } ^ { \flat }$. There is afullyfaithfulfunctor from$\mathrm { R } _ { \mathrm { f e t } } ^ { \flat }$to$\mathrm { R } _ { \mathrm { f e t } }$inverse to the tiltingfunctor. The essential image ofthisfunctor consists ofthefinite étale covers S ofR, for which S (with its natural topology) is perfectoid and$\mathrm { S } ^ { \circ a }$isfinite étale over$\mathrm { R } ^ { \circ a }$. In this case,$\mathrm { S } ^ { \circ a }$is a uniformlyfinite projective$\mathrm { R } ^ { \circ a }$-module.

In particular, we see that the fully faithful functor$\mathrm { R } _ { \mathrm { f e t } } ^ { \flat } \hookrightarrow \mathrm { R } _ { \mathrm { f e t } }$preserves degrees. We will later prove that this is an equivalence in general. For now, we prove that it is an equivalence for perfectoid fields, i.e. we finish the proof of Theorem 3.7.

ProofofTheorem 3.7. — Let K be a perfectoid field with tilt$\mathrm { K } ^ { \flat }$. Using the previous theorem, it is enough to show that the fully faithful functor$\mathrm { K } _ { \mathrm { f e t } } ^ { \flat } \to \mathrm { K } _ { \mathrm { f e t } }$is an equivalence.

Proof using ramification theory. — Proposition 6.6.2 (cf. its proof) and Proposition 6.6.6 of[15] show that for any finite extension L ofK, the extension$\mathrm { L } ^ { \circ a } / \mathrm { K } ^ { \circ a }$is étale. Moreover, it is finite projective by Proposition 6.3.6 of [15], giving the desired result.

Proofreducing to the case where$\mathrm { K } ^ { \flat }$is algebraically closed. — Let$\mathrm { M } = \overline { { \mathrm { K } ^ { \flat } } }$be the completion ofan algebraic closure of$\mathrm { K } ^ { \flat }$. Clearly, M is complete and perfect, i.e. M is perfectoid. Let M<sup></sup> be the untilt of M. Then by Lemma 5.21 and Proposition 3.8,$\mathbf { M } ^ { \sharp }$is an algebraically closed perfectoid field containing K. Any finite extension L ⊂ M of$\mathrm { K } ^ { \flat }$gives the untilt$\mathrm { L } ^ { \sharp } \subset \mathrm { M } ^ { \sharp }$, a finite extension of K. It is easy to see that the union$\mathrm { { N } = \mathrm { { U } _ { I } , \mathrm { { L } ^ { \sharp } \subset M ^ { \sharp } } } }$is a dense subfield. Now Krasner’s lemma implies that N is algebraically closed. Hence any finite extension F of K is contained in N; this means that there is some Galois extension L of K<sup>-</sup> such that F is contained in L<sup></sup>. Note that L<sup></sup> is still Galois, as the functor$\mathrm { L } \mapsto \mathrm { L } ^ { \sharp }$ preserves degrees and automorphisms. In particular, F is given by some subgroup H of $\mathrm { G a l ( L ^ { \sharp } / K ) = G a l ( L / K ^ { \flat } ) }$, which gives the desired finite extension$\mathrm { F } ^ { \mathrm { b } } = \mathrm { L } ^ { \mathrm { H } }$of$\mathrm { K } ^ { \flat }$that untilts to F: The equivalence of categories shows that$( { \mathrm { F } } ^ { \flat } ) ^ { \sharp } \subset ( { \mathrm { L } } ^ { \sharp } ) ^ { \mathrm { H } } = { \mathrm { F } } .$and as they have the same degree, they are equal.-

## 6. Perfectoid spaces: analytic topology

In the following, we are interested in the adic spaces associated to perfectoid algebras. Specifically, note that perfectoid K-algebras are Tate, and we will look at the following type of affinoid K-algebras.

Definition 6.1. — A perfectoid affinoid K-algebra is an affinoid K-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$such that R is a perfectoid K-algebra.

We note that in this case m$\mathbb { R } ^ { \circ } \subset \mathbb { R } ^ { + } \subset \mathbb { R } ^ { \circ }$, because all topologically nilpotent elements lie in$\mathrm { R } ^ { + }$, as$\mathrm { R } ^ { + }$is integrally closed. In particular,$\mathrm { R } ^ { + }$is almost equal to$\mathrm { R } ^ { \circ }$

Lemma 6.2. — The categories ofperfectoid affinoid K-algebras and perfectoid affinoid$\mathrm { K } ^ { \flat } .$ algebras are equivalent.$H ( \mathbb { R } , \mathbb { R } ^ { + } )$) maps to$( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } )$under this equivalence, then$x \mapsto x ^ { \sharp }$induces an isomorphism$\bar { \mathbf { R } } ^ { \flat + } / \varpi ^ { \flat } \cong \mathbf { R } ^ { + } / \varpi$. Also$\mathbb { R } ^ { + } = \varprojlim _ { x \mapsto x ^ { \rho } } \mathbb { R } ^ { + }$

Proof. — Giving an open integrally closed subring of$\mathrm { R } ^ { \circ }$is equivalent to giving an integrally closed subring of$\mathrm { ~ R ~ } ^ { \circ } / \mathfrak { m }$. This description is compatible with tilting. One easily checks the last identities.-

It turns out that also in this case, the presheaf$\mathcal { O } _ { \mathrm { X } }$is a sheaf. In fact, the main theorem of this section is the following.

Theorem 6.3.$- \angle e t ( { \bf R } , { \bf R } ^ { + } )$be a perfectoid affinoid K-algebra, and let$\mathrm { X = S p a ( R , R ^ { + } ) }$ with associated presheaves$\mathcal { O } _ { \mathrm { X } } , \mathcal { O } _ { \mathrm { X } } ^ { + }$. Also, let$( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } )$be the tilt given by Lemma$6 . 2 ,$and let $\mathrm { \mathbf { X } ^ { \flat } = \mathrm { S p a } ( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } ) }$etc.

(i) We have a homeomorphism$\mathrm { X } \cong \mathrm { X } ^ { \mathrm { b } } .$, given by mapping$x \in \mathrm { X }$to the valuation$x ^ { \mathrm { p } } \in \mathrm { X } ^ { \mathrm { b } }$ defined by$| f ( x ^ { \flat } ) | = | f ^ { \sharp } ( x ) |$. This homeomorphism identifies rational subsets.

(ii) For any rational subset$\mathrm { ~ U ~ } \subset \mathrm { ~ X ~ }$with tilt$\mathrm { U } ^ { \mathrm { p } } \subset \mathrm { X } ^ { \mathrm { p } }$, the complete affinoid K-algebra $( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$is perfectoid, with tilt$( \mathcal { O } _ { \mathrm { X } ^ { \flat } } ( \mathrm { U } ^ { \flat } ) , \mathcal { O } _ { \mathrm { X } ^ { \flat } } ^ { + } ( \mathrm { U } ^ { \flat } ) )$.

(iii) The presheaves$\mathcal { O } _ { \mathrm { X } } , \mathcal { O } _ { \mathrm { X } ^ { \flat } }$are sheaves.

(iv) The cohomology group$\mathrm { H } ^ { i } ( \mathrm { X } , \mathcal { O } _ { \mathrm { X } } ^ { + } )$is m-torsion for$i > 0$

We remark that we did not assume that$\mathrm { R } ^ { + }$is a K<sup>◦</sup>-algebra, although this is satisfied in all examples of interest to us. For this reason, it does not literally make sense to use the language of almost mathematics in the context of$\mathcal { O } _ { \mathrm { X } } ^ { + }$. In the following, the reader may safely assume that$\mathrm { R } ^ { + }$is a$\mathrm { K } ^ { \circ }$-algebra, which avoids some small extra twists.

Let us give an outline of the proof. First, we show that the map$\mathrm { X } \to \mathrm { X } ^ { \flat }$is continuous. Next, we prove a slightly weaker version of (ii), and give an explicit description of the perfectoid$\mathrm { K } ^ { \circ a } { - } \mathrm { a }$lgebra associated to${ \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } )$. This will be used to prove a crucial approximation lemma, dealing with the problem that the map$g \mapsto g ^ { \sharp }$is far from being surjective. Nonetheless, it turns out that one can approximate any function$f \in \mathrm { R }$by a function ofthe form$g ^ { \sharp }$such that the maps$x \mapsto | f ( x ) |$and$x \mapsto \vert g ^ { \sharp } ( x ) \vert$are identical except maybe at points x where both of them are very small. It is then easy to deduce part$( \mathrm { i } ) _ { - }$ and also part (ii). We note that the same approximation lemma will be used later in the proof of the weight-monodromy conjecture for complete intersections.

It remains to prove that$\mathcal { O } _ { \mathrm { X } }$is a sheaf with vanishing higher cohomology, and that the vanishing even extends to the almost integral level. The proof proceeds in several steps. First, we prove it in the case that K is of characteristic$\boldsymbol { p }$and$( \mathrm { R } , \mathrm { R } ^ { + } )$is the completed perfection of an affinoid K-algebra of tft. In that case, it is easy to deduce the result from Tate’s acyclicity theorem. Again, the direct limit over the Frobenius extends the vanishing of cohomology to the almost integral level. Next, we do the general characteristic$\boldsymbol { p }$case by writing an arbitrary perfectoid affinoid K-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$as the completed direct limit ofalgebras ofthe previous form. Finally, we deduce the case where K has characteristic 0 by using the result in characteristic$\beta ,$making use of parts (i) and (ii) already proved.

Proof. — First, we check that the map$\mathrm { X } \to \mathrm { X } ^ { \flat }$is well-defined and continuous: To check well-definedness, we have to see that it maps valuations to valuations. This was already verified in the proof of Proposition 3.6.

Moreover, the map$\mathrm { X } \to \mathrm { X } ^ { \flat }$is continuous, because the preimage of the rational subset$\operatorname { U } ( { \frac { f _ { 1 } , \dots , f _ { n } } { g } } )$is given by$\begin{array} { r } { \mathrm { U } ( \frac { f _ { 1 } ^ { \sharp } , \dots , f _ { n } ^ { \sharp } } { g ^ { \sharp } } ) } \end{array}$, assuming as in Remark 2.8 that$f _ { n }$is a power of$\varpi ^ { \flat }$ to ensure that$f _ { 1 } ^ { \sharp } , \ldots , f _ { n } ^ { \sharp }$still generate R.

We have the following description of$\mathcal { O } _ { \mathrm { X } }$.

Lemma 6.4. — Let$\operatorname { U } = \operatorname { U } ( { \textstyle \frac { f _ { 1 } , \dots , f _ { n } } { \rho } } ) \subset \operatorname { S p a } ( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } )$be rational, with preimage$\mathrm { U } ^ { \sharp } \subset$ $\mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$. Assume that all$f _ { i } , g \in \mathbb { R } ^ { \mathrm { b o } }$and that$f _ { n } = \varpi ^ { \mathrm { b N } }$for some$\mathrm { N } ;$this is always possible without changing the rational subspace.

(i) Consider the  -adic completion

$$
\mathrm{R} ^ {\circ} \left\langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right\rangle
$$

of the subring

$$
\mathrm{R} ^ {\circ} \left[ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right] \subset \mathrm{R} \left[ \frac {1}{g ^ {\sharp}} \right].
$$

Then$\begin{array} { r } { \mathrm { R } ^ { \circ } \langle ( \frac { f _ { 1 } ^ { \sharp } } { g ^ { \sharp } } ) ^ { 1 / p ^ { \infty } } , \dots , ( \frac { f _ { n } ^ { \sharp } } { g ^ { \sharp } } ) ^ { 1 / p ^ { \infty } } \rangle ^ { a } } \end{array}$is a perfectoid$\mathrm { K } ^ { \circ a }$-algebra.

(ii) The algebra${ \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } ^ { \sharp } )$is a perfectoid K-algebra, with associated perfectoid$\mathrm { K } ^ { \circ a }$-algebra

$$
\mathcal {O} _ {\mathrm{X}} \big (\mathrm{U} ^ {\sharp} \big) ^ {\circ a} = \mathrm{R} ^ {\circ} \Big \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \Big \rangle^ {a}.
$$

(iii) The tilt$o f { \mathcal { O } } _ { \mathrm { { X } } } ( \mathrm { { U } } ^ { \sharp } )$is given by$\mathcal { O } _ { \mathrm { X } ^ { \flat } } ( \mathrm { U } )$

$P r o o f . - \mathrm { ( i ) }$(K of characteristic$p )$. Assume that K has characteristic$\beta ,$and identify $\mathrm { K } ^ { \flat } = \mathrm { K }$; the general case is dealt with below. We see from the definition that

$$
\mathrm{R} ^ {\circ} \left\langle \left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \right\rangle
$$

is flat over$\mathrm { K } ^ { \circ }$and -adically complete.

We want to show that modulo$\varpi _ { : }$, Frobenius is almost surjective with kernel almost generated by$\varpi ^ { 1 / p }$. We have a surjection

$$
\mathrm{R} ^ {\circ} \left[ \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right]\rightarrow \mathrm{R} ^ {\circ} \left[\left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \right].
$$

Its kernel contains the ideal I generated by all$\mathrm { T } _ { i } ^ { 1 / p ^ { m } } g ^ { 1 / p ^ { m } } - f _ { i } ^ { 1 / p ^ { m } }$. We claim that the induced morphism

$$
\mathrm{R} ^ {\circ} \left[ \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right] / \mathrm{I} \rightarrow \mathrm{R} ^ {\circ} \left[\left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \right]
$$

is an almost isomorphism. Indeed, it is an isomorphism after inverting  , because this also inverts g. Iff lies in the kernel of this map, there is some k with$^ k f \in \operatorname { I }$. But then $( \varpi ^ { k / { p ^ { m } } } f ) ^ { { p ^ { m } } } \in \operatorname { I }$, and because I is perfect, also$\varpi ^ { k / p ^ { m } } f \in \operatorname { I }$. This gives the desired statement.

Reducing modulo$\varpi$, we have an almost isomorphism

$$
\mathrm{R} ^ {\circ} \left[ \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right] / (\mathrm{I}, \varpi) \rightarrow \mathrm{R} ^ {\circ} \left\langle\left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \right\rangle / \varpi .
$$

From the definition of$^ { \mathrm { ~ I ~ } , }$it is immediate that Frobenius gives an isomorphism

$$
\mathrm{R} ^ {\circ} \left[ \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right] / (\mathrm{I}, \varpi^ {1 / p}) \cong \mathrm{R} ^ {\circ} \left[ \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right] / (\mathrm{I}, \varpi).
$$

This finally shows that

$$
\mathrm{R} ^ {\circ} \left\langle \left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \right\rangle^ {a}
$$

is a perfectoid$\mathrm { K } ^ { \circ a }$-algebra, giving part (i) in characteristic$\beta .$

$( \mathrm { { i } ) \Rightarrow ( \mathrm { { i i } ) } }$(General K). We show that in general, (i) implies (ii). Note that$\mathrm { R } ^ { \circ } \subset \mathrm { R }$ is open and bounded, hence we may choose$\mathrm { R } _ { 0 } = \mathrm { R } ^ { \circ }$in Definition 2.13. We have the inclusions

$$
\mathrm{R} ^ {\circ} \left[ \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \dots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} \right] \subset \mathrm{R} ^ {\circ} \left[ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right] \subset \mathrm{R} \left[ \frac {1}{g ^ {\sharp}} \right].
$$

Moreover, we claim that

$$
\varpi^ {n \mathrm{N}} \mathrm{R} ^ {\circ} \bigg [ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \bigg ] \subset \mathrm{R} ^ {\circ} \bigg [ \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \ldots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} \bigg ].
$$

Indeed,$\begin{array} { r } { \frac { 1 } { g ^ { \sharp } } = \varpi ^ { - \mathrm { N } } \frac { f _ { n } ^ { \sharp } } { g ^ { \sharp } } } \end{array}$, and any element on the left-hand side can be written as a sum of terms on the right-hand side with coefficients in$\scriptstyle { \frac { 1 } { ( g ^ { \sharp } ) ^ { n } } } \mathbf { R } ^ { \circ }$

Now we may pass to the  -adic completion and get inclusions

$$
\mathrm{R} ^ {\circ} \left\langle \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \dots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} \right\rangle \subset \mathrm{R} ^ {\circ} \left\langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right\rangle
$$

$$
\subset \mathrm{R} \bigg \langle \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \ldots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} \bigg \rangle = \mathcal {O} _ {\mathrm{X}} (\mathrm{U}).
$$

Thus it follows from part (i) that

$$
\mathcal {O} _ {\mathrm{X}} (\mathrm{U}) = \mathrm{R} ^ {\circ} \left\langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right\rangle \left[ \varpi^ {- 1} \right]
$$

is perfectoid, with corresponding perfectoid$\mathrm { K } ^ { \circ a } { \mathrm { - a l g e b r a } }$

(i), (iii) (General$\mathrm { K } )$. Again, we see from the definition that

$$
\mathrm{R} ^ {\circ} \left\langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right\rangle
$$

is flat over$\mathrm { K } ^ { \circ }$and$\varpi$-adically complete. We have to show that modulo$\varpi$, Frobenius is almost surjective with kernel almost generated by$\varpi ^ { 1 / \rho }$. We still have the map

$$
\mathrm{R} ^ {\circ} \big [ \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \ldots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \big ] / \mathrm{I} \to \mathrm{R} ^ {\circ} \bigg [ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \bigg ],
$$

where I is the ideal generated by all$\mathrm { T } _ { i } ^ { 1 / p ^ { m } } ( g ^ { 1 / p ^ { m } } ) ^ { \sharp } - ( f _ { i } ^ { 1 / p ^ { m } } ) ^ { \sharp }$. Also, we may apply our results for the tilted situation. In particular, we know that$( \mathcal { O } _ { \mathrm { X ^ { \flat } } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X ^ { \flat } } } ^ { + } ( \mathrm { U } ) )$is a perfectoid affinoid$\mathrm { K } ^ { \flat }$-algebra. Let$( \mathrm { S } , \mathrm { S } ^ { + } )$be its tilt. Then$\mathrm { S p a } ( \mathrm { S } , \mathrm { S } ^ { + } )  \bar { \mathrm { X } }$factors over$\mathrm { U } ^ { \sharp }$, and hence we get a map$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ^ { \sharp } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ^ { \sharp } ) ) \to ( \mathrm { S } , \mathrm { S } ^ { + } )$. The composite map

$$
\begin{array}{c} \mathrm{R} ^ {\circ} \big \langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \ldots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \big \rangle^ {a} \to \mathrm{R} ^ {\circ} \Big \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \Big \rangle^ {a} \\ \to \mathcal {O} _ {\mathrm{X}} \big (\mathrm{U} ^ {\sharp} \big) ^ {\circ a} \to \mathrm{S} ^ {\circ a} \end{array}
$$

is a map of perfectoid${ \mathrm { K } } ^ { \circ a } { \mathrm { - a l g e b r a s , } }$, which is the tilt of the composite map

$$
\mathrm{R} ^ {\flat \circ} \left\langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right\rangle^ {a} \rightarrow \mathrm{R} ^ {\flat \circ} \left\langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right\rangle^ {a} / \mathrm{I} ^ {\flat} \rightarrow \mathcal {O} _ {\mathrm{X} ^ {\flat}} (\mathrm{U}) ^ {\circ a},
$$

where$\Gamma ^ { \flat }$is the corresponding ideal which occurs in the tilted situation. Note that

$$
\mathrm{R} ^ {\flat \circ} \left\langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right\rangle / \left(\mathrm{I} ^ {\flat}, \varpi^ {\flat}\right) = \mathrm{R} ^ {\circ} \left\langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right\rangle / (\mathrm{I}, \varpi)
$$

from the explicit description. Since

$$
\mathrm{R} ^ {\flat \circ} \left\langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \right\rangle^ {a} / \left(\mathrm{I} ^ {\flat}, \varpi^ {\flat}\right)\rightarrow \mathcal {O} _ {\mathrm{X} ^ {\flat}} (\mathrm{U}) ^ {\circ a} / \varpi^ {\flat}
$$

is an isomorphism, so is the composite map

$$
\begin{array}{c} \mathrm{R} ^ {\circ} \big \langle \mathrm{T} _ {1} ^ {1 / p ^ {\infty}}, \ldots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \big \rangle^ {a} / (\mathrm{I}, \varpi) \to \mathrm{R} ^ {\circ} \Big \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \Big \rangle^ {a} \Big / \varpi \\ \to \mathrm{S} ^ {\circ a} / \varpi , \end{array}
$$

as it identifies with the previous map under tilting. The first map being surjective, it follows that both maps are isomorphisms. In particular,

$$
\mathrm{R} ^ {\circ} \left\langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right\rangle^ {a} / \varpi \cong \mathrm{S} ^ {\circ a} / \varpi .
$$

This gives part (i), and hence part (ii), and then the latter isomorphism gives part (iii). -

We need an approximation lemma.

Lemma 6.5. — Let$\mathrm { R } = \mathrm { K } \langle \mathrm { T } _ { 0 } ^ { 1 / p ^ { \infty } } , \ldots , \mathrm { T } _ { n } ^ { 1 / p ^ { \infty } } \rangle$. Let$f \in \mathrm { R } ^ { \circ }$be a homogeneous element of degree$d \in \mathbf { Z } [ \textstyle { \frac { 1 } { \rho } } ]$. Thenfor any rational number$c \geq 0$and any$\epsilon > 0$, there exists an element

$$
g _ {c, \epsilon} \in \mathrm{R} ^ {\flat \circ} = \mathrm{K} ^ {\flat \circ} \bigl \langle \mathrm{T} _ {0} ^ {1 / p ^ {\infty}}, \ldots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \bigr \rangle
$$

homogeneous ofdegree d such thatfor all$x \in \mathrm { X = S p a ( R , R ^ { \circ } ) }$, we have

$$
\left| f (x) - g _ {c, \epsilon} ^ {\sharp} (x) \right| \leq | \varpi | ^ {1 - \epsilon} \max \bigl (\left| f (x) \right|, | \varpi | ^ {c} \bigr).
$$

Remark 6.6. — Note that for$\epsilon < 1$, the given estimate says in particular that for all $x \in \mathrm { X = S p a ( R , R ^ { \circ } ) }$, we have

$$
\max \left(\left| f (x) \right|, \left| \varpi \right| ^ {c}\right) = \max \left(\left| g _ {c, \epsilon} ^ {\sharp} (x) \right|, \left| \varpi \right| ^ {c}\right).
$$

Proof. — We fix$\epsilon > 0$, and assume$\epsilon < 1$and$\epsilon \in \mathbf { Z } [ \textstyle { \frac { 1 } { \rho } } ]$. We also fix$f .$Then we prove inductively that for any c one can find some$\epsilon ( c ) > 0$and some

$$
g _ {c} \in \mathrm{R} ^ {\flat \circ} = \mathrm{K} ^ {\flat \circ} \bigl \langle \mathrm{T} _ {0} ^ {1 / p ^ {\infty}}, \ldots , \mathrm{T} _ {n} ^ {1 / p ^ {\infty}} \bigr \rangle
$$

homogeneous of degree d such that for all$x \in \mathrm { X = S p a ( R , R ^ { \circ } ) }$, we have

$$
\left| f (x) - g _ {c} ^ {\sharp} (x) \right| \leq | \varpi | ^ {1 - \epsilon + \epsilon (c)} \max \left(\left| f (x) \right|, | \varpi | ^ {c}\right).
$$

We will need$\epsilon ( c )$, as each induction step will lose some small constant because of some almost mathematics involved. Now we argue by induction, increasing from c to$c ^ { \prime } = c + a ,$ where$0 < a < \epsilon$is some fixed rational number in$\mathbf { Z } [ \textstyle { \frac { 1 } { \rho } } ]$. The case$c = 0$is obvious: One may take$\epsilon ( 0 ) = \epsilon$. We are free to replace$\epsilon ( c )$by something smaller, so without loss of generality, we assume$\epsilon ( c ) \leq \epsilon - a$and$\epsilon ( c ) \in \mathbf { Z } [ \textstyle { \frac { 1 } { \rho } } ]$

Let$\mathrm { \Delta X = \mathrm { S p a } ( R , R ^ { + } ) }$, where$\mathbf { R } ^ { + } = \mathbf { R } ^ { \circ } = \mathbf { K } ^ { \circ } \langle \mathbf { T } _ { 0 } ^ { 1 / \rho ^ { \infty } } , \ldots , \mathbf { T } _ { n } ^ { 1 / \rho ^ { \infty } } \rangle$. Let$\mathrm { U } _ { c } \subset \mathrm { X } ^ { \mathrm { p } } =$ $\mathrm { { S p a } ( R ^ { \flat } , R ^ { \flat + } ) }$be the rational subset given by$| g _ { c } ( x ) | \leq | \varpi ^ { \flat } | ^ { c }$. Its preimage$\mathrm { U } _ { c } ^ { \sharp } \subset \mathrm { X }$is given by$| f ( x ) | \leq | \varpi | ^ { c }$. The condition implies that

$$
h = f - g _ {c} ^ {\sharp} \in \varpi^ {c + 1 - \epsilon + \epsilon (c)} \mathcal {O} _ {\mathrm{X}} ^ {+} \left(\mathrm{U} _ {c} ^ {\sharp}\right).
$$

The previous lemma shows that

$$
\mathcal {O} _ {\mathrm{X}} \big (\mathrm{U} _ {c} ^ {\sharp} \big) ^ {\circ a} = \mathrm{R} ^ {\circ} \Bigg \langle \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {\frac {1}{p ^ {\infty}}} \Bigg \rangle^ {a}.
$$

But h is a homogeneous element, so that h lies almost in the  -adic completion of

$$
\bigoplus_ {i \in \mathbf {Z} [ \frac {1}{p} ], 0 \leq i \leq 1} \varpi^ {c + 1 - \epsilon + \epsilon (c)} \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {i} \mathrm{R} _ {\deg = d - d i} ^ {\circ}.
$$

This shows that we can find elements$r _ { i } \in \mathrm { R } ^ { + }$homogeneous of degree$d - d i$, such that $r _ { i } \to 0$, with

$$
h = \sum_ {i \in {\bf Z} [ \frac {1}{p} ], 0 \leq i \leq 1} \varpi^ {c + 1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {i} r _ {i},
$$

where we choose some$0 < \epsilon ( c ^ { \prime } ) < \epsilon ( c ) , \epsilon ( c ^ { \prime } ) \in \mathbf { Z } [ \frac { 1 } { \it \Delta \phi } ]$. Choose$s _ { i } \in \mathbb { R } ^ { \flat + }$homogeneous of degree$d - d i , s _ { i }  0$, such that$\varpi$divides$r _ { i } - s _ { i } ^ { \sharp }$. Now set

$$
g _ {c ^ {\prime}} = g _ {c} + \sum_ {i \in \mathbf {Z} [ \frac {1}{p} ], 0 \leq i \leq 1} \left(\varpi^ {\flat}\right) ^ {c + 1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}}\right) ^ {i} s _ {i}.
$$

We claim that for all$x \in \mathrm { X }$, we have

$$
\left| f (x) - g _ {c ^ {\prime}} ^ {\sharp} (x) \right| \leq | \varpi | ^ {1 - \epsilon + \epsilon \left(c ^ {\prime}\right)} \max \left(\left| f (x) \right|, \left| \varpi \right| ^ {c ^ {\prime}}\right).
$$

Assume first that$| f ( x ) | > | \varpi | ^ { c }$. Then we have$| g _ { c } ^ { \sharp } ( x ) | = | f ( x ) | > | \varpi | ^ { c }$. It is enough to show that

$$
\left| \left(\left(\varpi^ {\flat}\right) ^ {c + 1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}}\right) ^ {i} s _ {i}\right) ^ {\sharp} (x) \right| \leq | \varpi | ^ {1 - \epsilon + \epsilon (c ^ {\prime})} | f (x) |.
$$

Neglecting$| s _ { i } ^ { \sharp } ( x ) | \leq 1$, the left-hand side is maximal when$i = 1$, in which case it evaluates to the right-hand side, so that we get the desired estimate.

Now we are left with the case$| f ( x ) | \leq | \varpi | ^ { c }$. We claim that in fact

$$
\left| f (x) - g _ {c ^ {\prime}} ^ {\sharp} (x) \right| \leq | \varpi | ^ {c ^ {\prime} + 1 - \epsilon + \epsilon (c ^ {\prime})}
$$

in this case, which is clearly enough. For this, it is enough to see that$f - g _ { c ^ { \prime } } ^ { \sharp }$is an element of$\varpi ^ { c + 1 } \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } _ { c } ^ { \sharp } ) ^ { \circ }$, because$c + 1 > c ^ { \prime } + 1 - \epsilon + \epsilon ( c ^ { \prime } )$. But we have

$$
\frac {g _ {c ^ {\prime}}}{(\varpi^ {\flat}) ^ {c}} = \frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}} + \sum_ {i} \big (\varpi^ {\flat} \big) ^ {1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}}\right) ^ {i} s _ {i},
$$

with all terms being in$\mathcal { O } _ { \mathrm { X } ^ { \flat } } ( \mathrm { U } _ { c } ) ^ { \circ }$. Hence we get that

$$
\frac {g _ {c ^ {\prime}} ^ {\sharp}}{\varpi^ {c}} = \frac {g _ {c} ^ {\sharp}}{\varpi^ {c}} + \sum_ {i} \varpi^ {1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {i} r _ {i}
$$

in$\mathcal { O } _ { \mathrm { X } } ( \mathrm { U } _ { c } ^ { \sharp } ) ^ { \circ }$, modulo$\varpi$. Multiplying by$\varpi ^ { c }$, this rewrites as

$$
f - g _ {c ^ {\prime}} ^ {\sharp} = f - g _ {c} ^ {\sharp} - h = 0
$$

modulo$\varpi ^ { c + 1 }$. This gives the desired estimate.

Corollary${ \bf 6 . 7 . { \_ } } L e t \left( \mathrm { R , R ^ { + } } \right)$be a perfectoid affinoid K-algebra, with tilt$( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } )$, and let$\mathrm { X } = \mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } ) , \mathrm { X } ^ { \flat } = \mathrm { S p a } ( \mathrm { R } ^ { \flat } , \mathrm { R } ^ { \flat } + )$

(i) For any$f \in \mathbf { R }$and any$c \geq 0 , \epsilon > 0 .$, there exists$g _ { c , \epsilon } \in \mathbb { R } ^ { \flat }$such thatfor all$x \in \mathrm { X }$, we have

$$
\left| f (x) - g _ {c, \epsilon} ^ {\sharp} (x) \right| \leq | \varpi | ^ {1 - \epsilon} \max \bigl (\left| f (x) \right|, | \varpi | ^ {c} \bigr).
$$

(ii) For any$x \in \mathrm { X } ,$, the completed residuefield$\widehat { k ( x ) }$is a perfectoidfield.

(iii) The morphism$\mathrm { X } \to \mathrm { X } ^ { \flat }$induces a homeomorphism, identifying rational subsets.

Proof. — (i) As any maximal point of$\mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$is contained in$\operatorname { S p a } ( \mathrm { R } , \mathrm { R } ^ { \circ } )$, and it is enough to check the inequality at maximal points after increasing slightly, it is enough to prove this if$\mathrm { R } ^ { + } = \mathrm { R } ^ { \circ }$. At the expense of enlarging$^ { c , }$we may assume that$f \in \mathrm { R } ^ { \circ }$, and also assume that c is an integer. Further, we can write$\bar { f } = g _ { 0 } ^ { \sharp } + \varpi g _ { 1 } ^ { \sharp } + \cdot \cdot \cdot + \varpi ^ { c } g _ { c } ^ { \sharp } + \varpi ^ { c + 1 } f _ { c + 1 }$ for certain$g _ { 0 } , \ldots , g _ { c } \in \mathbf { R } ^ { \flat \circ }$and$f _ { c + 1 } \in \mathbb { R } ^ { \circ }$. We can assume$f _ { c + 1 } = 0$. Now we have the map

$$
\mathrm{K} \big \langle \mathrm{T} _ {0} ^ {1 / p ^ {\infty}}, \dots , \mathrm{T} _ {c} ^ {1 / p ^ {\infty}} \big \rangle \rightarrow \mathrm{R}
$$

sending$\mathrm { T } _ { i } ^ { 1 / { p ^ { m } } }$to$( g _ { i } ^ { 1 / \boldsymbol { p } ^ { m } } ) ^ { \sharp }$, andf is the image of$\mathrm { T } _ { 0 } + \varpi \mathrm { T } _ { 1 } + \cdot \cdot \cdot + \varpi ^ { c } \mathrm { T } _ { c } ,$to which we may apply Lemma 6.5.

(ii) (K of characteristic$p )$. In this case, we know that$\mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) ^ { \circ a }$is perfectoid for any rational subset U. It follows that the  -adic completion of$\mathcal { O } _ { \mathrm { X } , x } ^ { { o a } }$is a perfectoid$\mathrm { K } ^ { \circ a } .$ algebra, hence$\widehat { k ( x ) }$is a perfectoid K-algebra. As it is also a nonarchimedean field, the result follows.

(iii) First, part (i) immediately implies that any rational subset of X is the preimage of a rational subset of$\mathrm { \Delta X ^ { \flat } }$. Because X is$\mathrm { T _ { 0 } } .$, this implies that the map is injective. Now any $x \in \mathrm { X } ^ { \flat }$factors as a composite$\mathbb { R } ^ { \flat } \to { \widehat { k ( x ) } } \to \Gamma \cup \{ 0 \} . \mathbb { A } \operatorname { s } { \widehat { k ( x ) } }$is perfectoid, we may untilt to a perfectoid field over$\mathrm { K } ,$, and we may also untilt the valuation by Proposition 3.6. This shows that the map is surjective, giving part (iii). Now part (ii) follows in general with the same proof.-

For any subset$\mathrm { M } \subset \mathrm { X } .$, we write$\mathrm { M } ^ { \mathrm { p } } \subset \mathrm { X } ^ { \mathrm { b } }$for the corresponding subset of$\mathrm { \mathbf { X } } ^ { \mathrm { \flat } }$.

Corollary${ \bf 6 . 8 . { \mathcal { - } } } L e t \left( { \bf R , R ^ { + } } \right)$be a perfectoid affinoid K-algebra, with tilt$( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } )$, and let $\mathrm { X } = \mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } ) , \mathrm { X } ^ { \flat } = \mathrm { S p a } ( \mathrm { R } ^ { \flat } , \mathrm { R } ^ { \flat } + )$. Thenfor all rational$\mathrm { U } \subset \mathrm { X } .$, the pair$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$ is a perfectoid affinoid K-algebra with tilt$( \mathcal { O } _ { \mathrm { X } ^ { \flat } } ( \mathrm { U } ^ { \flat } ) , \mathcal { O } _ { \mathrm { X } ^ { \flat } } ^ { + } ( \mathrm { U } ^ { \flat } ) )$.

Proof. — Corollary 6.7(iii) and Lemma 6.4(ii) show that$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$is a perfectoid affinoid K-algebra. It can be characterized by the universal property of Proposition 2.14 among all perfectoid affinoid K-algebras, and tilting this universal property shows that its tilt has the analogous universal property characterizing $( \mathcal { O } _ { \mathrm { X } ^ { \flat } } ( \mathrm { U } ^ { \flat } ) , \mathcal { O } _ { \mathrm { X } ^ { \flat } } ^ { + } ( \mathrm { U } ^ { \flat } ) )$) among all perfectoid affinoid$\mathrm { K ^ { \mathrm { b } } \mathrm { - a l g e b r a s . } }$-

At this point, we have proved parts (i) and (ii) of Theorem 6.3.

To prove the sheaf properties, we start in characteristic$\beta ,$with a certain class of perfectoid rings which are particularly easy to access.

Definition 6.9. — Assume K is of characteristic$\beta .$Then a perfectoid affinoid K-algebra $( \mathrm { R } , \mathrm { R } ^ { + } )$is said to be p-finite if there exists a reduced affinoid K-algebra$( \mathrm { S } , \mathrm { S } ^ { + } )$of topologically finite type such that$( \mathrm { R } , \mathrm { R } ^ { + } )$is the completed perfection${ \cal O } f ( \mathrm { S } , \mathrm { S } ^ { + } )$, i.e.$\mathrm { R } ^ { + }$is the  -adic completion $g f \underline { { { \mathrm { l i m } } } } _ { \Phi } \mathrm { S } ^ { + }$and$\mathbf { R } = \mathbf { R } ^ { + } [ \boldsymbol { \varpi } ^ { - 1 } ]$

At this point, let us recall some facts about reduced affinoid K-algebras of topologically finite type.

Proposition 6.10. — Let$( \mathrm { S } , \mathrm { S } ^ { + } )$be a reduced affinoid K-algebra oftopologically finite type, and let$\mathrm { X = S p a ( S , S ^ { + } ) }$.

(i) The subset$\mathrm { S } ^ { + } = \mathrm { S } ^ { \circ } \subset \mathrm { S }$is open and bounded.

(ii) For any rational subset$\mathrm { ~ U ~ C ~ X ~ } _ { \mathfrak { i } }$, the affinoid K-algebra$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$) is reduced and of topologically finite type.

(iii) For any covering$\mathrm { X } = \cup \mathrm { U } _ { i }$byfinitely many rational subsets$\mathrm { U } _ { i } \subset \mathrm { X }$, each cohomology group ofthe complex

$$
0 \to \mathcal {O} _ {\mathrm{X}} (\mathrm{X}) ^ {\circ} \to \prod_ {i} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i}) ^ {\circ} \to \prod_ {i, j} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i} \cap \mathrm{U} _ {j}) ^ {\circ} \to \dots
$$

is annihilated by some power of$\cdot _ { \varpi }$.

Proof. — Using [20], Proposition 4.3 and its proof (cf. also [19, Corollary 4.3 and (4.7.1)]), one sees that all statements are readily translated into the classical language of rigid geometry, and we use results from the book of Bosch-Güntzer-Remmert [2]. Part (i) is precisely their 6.2.4 Theorem 1, and part (ii) is 7.3.2 Corollary 10.

Moreover, Tate’s acyclicity theorem, 8.2.1 Theorem 1 in [2], says that

$$
0 \to \mathcal {O} _ {\mathrm{X}} (\mathrm{X}) \xrightarrow {d _ {0}} \prod_ {i} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i}) \xrightarrow {d _ {1}} \prod_ {i, j} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i} \cap \mathrm{U} _ {j}) \xrightarrow {d _ {2}} \dots
$$

is exact. Then ker$d _ { i }$is a closed subspace of a K-Banach space, hence itself a K-Banach space, and$d _ { i - 1 }$is a surjection onto ker$d _ { i } . \mathrm { B y }$Banach’s open mapping theorem, the map $d _ { i - 1 }$is an open map to ker$d _ { i } .$. This says that the subspace and quotient topologies on ker$d _ { i } = \mathrm { i m } d _ { i - 1 }$coincide. Now consider the sequence

$$
0 \to \mathcal {O} _ {\mathrm{X}} (\mathrm{X}) ^ {\circ} \xrightarrow {d _ {0} ^ {\circ}} \prod_ {i} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i}) ^ {\circ} \xrightarrow {d _ {1} ^ {\circ}} \prod_ {i, j} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i} \cap \mathrm{U} _ {j}) ^ {\circ} \xrightarrow {d _ {2} ^ {\circ}} \dots .
$$

By parts$( \mathrm { i } )$and$( \ddot { \mathrm { 1 i } } )$, the quotient topology on im$d _ { i - 1 }$has$\varpi ^ { n }$im$d _ { i - 1 } ^ { \circ } , n \in \mathbf { Z } .$, as a basis of open neighborhoods of$0 ,$and the subspace topology of ker$d _ { i }$has$\varpi ^ { n } \mathrm { k e r } d _ { i } ^ { \circ } , n \in \mathbf { Z } .$, as a basis of open neighborhoods of 0. That they agree precisely amounts to saying that the cohomology group is annihilated by some power of$\varpi$.-

Proposition 6.11. — Assume that K is ofcharacteristic$\rho ,$and that$( \mathrm { R } , \mathrm { R } ^ { + } )$is p-finite, given as the completedperfection ofa reduced affinoid K-algebra$( \mathrm { S } , \mathrm { S } ^ { + } )$oftopologicallyfinite type.

(i) The map${ \mathrm { X } } = { \mathrm { S p a } } ( \mathrm { R } , \mathrm { R } ^ { + } ) \cong \mathrm { Y } = { \mathrm { S p a } } ( \mathrm { S } , \mathrm { S } ^ { + } )$is a homeomorphism identifying rational subspaces.

(ii) For any U ⊂ X rational, corresponding to${ \mathrm { ~ V ~ C ~ Y } } _ { 3 }$, the perfectoid affinoid K-algebra $( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$is equal to the completed perfection of$( \mathcal { O } _ { \mathrm { Y } } ( \mathrm { V } ) , \mathcal { O } _ { \mathrm { Y } } ^ { + } ( \mathrm { V } ) )$

(iii) For any covering$\mathrm { X } = \mathrm { U } _ { i } \mathrm { U } _ { i }$by rational subsets, the sequence

$$
0 \to \mathcal {O} _ {\mathrm{X}} (\mathrm{X}) ^ {\circ a} \to \prod_ {i} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i}) ^ {\circ a} \to \prod_ {i, j} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i} \cap \mathrm{U} _ {j}) ^ {\circ a} \to \dots
$$

is exact. In particular,$\mathcal { O } _ { \mathrm { X } }$is a sheaf, and H$^ i ( \mathrm { X } , \mathcal { O } _ { \mathrm { X } } ^ { \circ a } ) = 0 f o r i > 0 .$

Remark 6.12. — The last assertion is equivalent to the assertion that$\mathrm { H } ^ { i } ( \mathrm { X } , \mathcal { O } _ { \mathrm { X } } ^ { + } )$is annihilated by m.

Proof. — (i) Going to the perfection does not change the associated adic space and rational subspaces, and going to the completion does not by Proposition 2.11.

(ii) The completed perfection of$( \mathcal { O } _ { \mathrm { Y } } ( \mathrm { V } ) , \mathcal { O } _ { \mathrm { Y } } ^ { + } ( \mathrm { V } ) )$is a perfectoid affinoid$\mathrm { K } \cdot$ algebra. It has the universal property defining$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$among all perfectoid affinoid K-algebras.

(iii) Note that the corresponding sequence for Y is exact up to some$\varpi$-power. Hence after taking the perfection, it is almost exact, and stays so after completion. -

Lemma 6.13. — Assume K is ofcharacteristic$\beta .$

(i) Any perfectoid affinoid K-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$for which$\mathrm { R } ^ { + }$is a$\mathrm { K } ^ { \circ }$-algebra is the completion ofafiltered direct limit ofp-finite perfectoid affinoid K-algebras$( \mathrm { R } _ { i } , \mathrm { R } _ { i } ^ { + } )$

(ii) This induces a homeomorphism$\operatorname { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } ) \cong \varinjlim \operatorname { S p a } ( \mathrm { R } _ { i } , \mathrm { R } _ { i } ^ { + } )$, and each rational$\mathrm { U } \subset \mathrm { X } = \mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } )$comes as the preimage of some rational$\mathrm { U } _ { i } \subset \mathrm { X } _ { i } =$ $\mathrm { S p a } ( \mathbf { R } _ { i } , \mathbf { R } _ { i } ^ { + } )$

(iii) In this case$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$is equal to the completion ofthefiltered direct limit ofthe $( \mathcal { O } _ { \mathrm { X } _ { j } } ( \mathrm { U } _ { j } ) , \mathcal { O } _ { \mathrm { X } _ { i } } ^ { + } ( \mathrm { U } _ { j } ) )$), where$\mathrm { U } _ { j }$is the preimage of$\mathrm { \Delta T } _ { i }$in$\mathrm { X } _ { j } f o r j \geq i .$

(iv)${ I f \mathbf { U } } _ { i } \subset \mathbf { X } _ { i }$is some quasicompact open subset containing the image ofX, then there is some $j$such that the image ofX is contained in$\mathrm { U } _ { i }$

Proof. — (i) For any finite subset${ \mathrm { I } } \subset { \mathrm { R } } ^ { + }$, we have the K-subalgebra$\mathrm { S } _ { \mathrm { I } } \subset \mathrm { R }$given as the image of$\mathrm { K } \langle \mathrm { T } _ { i } | i \in \mathrm { I } \rangle  \mathrm { R }$. Then$\mathrm { S } _ { \mathrm { I } }$is a reduced quotient of$\mathrm { K } \langle \mathrm { T } _ { i } | i \in \mathrm { I } \rangle$, and we give $\mathrm { S } _ { \mathrm { I } }$the quotient topology. Let$\mathrm { S } _ { \mathrm { I } } ^ { + } \subset \mathrm { S } _ { \mathrm { I } }$be the set of power-bounded elements; it is also the set of elements integral over$\mathrm { K } ^ { \circ } \langle \mathrm { T } _ { i } | i \in \mathrm { I } \rangle$by [33], Theorem 5.2. In particular,$\mathrm { S } _ { \mathrm { I } } ^ { + } \subset \mathrm { R } ^ { + }$ We caution the reader that$\mathrm { S _ { I } ^ { + } }$is in general not the preimage of$\mathrm { R ^ { + } }$in$\mathrm { S } _ { \mathrm { I } }$

Now let$( \mathrm { R } _ { \mathrm { I } } , \mathrm { R } _ { \mathrm { I } } ^ { + } )$be the completed perfection of$( \mathrm { S } _ { \mathrm { I } } , \mathrm { S } _ { \mathrm { I } } ^ { + } )$, i.e.$\mathrm { R } _ { \mathrm { I } } ^ { + }$is the$\varpi \cdot$ adic completion of lim$_ \Phi ^ { \mathrm { \tiny ~ S _ { I } ^ { + } } }$, and$\mathbf { R } _ { \mathrm { I } } = \mathbf { R } _ { \mathrm { I } } ^ { + } [ \boldsymbol { \varpi } ^ { - 1 } ]$. We get an induced map$( \mathrm { R } _ { \mathrm { I } } , \mathrm { R } _ { \mathrm { I } } ^ { + } )$ $( \mathrm { R } , \mathrm { R } ^ { + } )$, and$( \mathrm { R } _ { \mathrm { I } } , \mathrm { R } _ { \mathrm { I } } ^ { + } )$is a p-finite perfectoid affinoid K-algebra. We claim that $\operatorname { R } ^ { + } / \varpi ^ { n } = \varinjlim _ { \mathrm { \tiny ~  ~ } } \operatorname { R } _ { \mathrm { I } } ^ { + } / \varpi ^ { n }$. Indeed, the map is clearly surjective. It is also injective, since $\mathrm { i f } f _ { 1 } , f _ { 2 } \in \mathrm { R } _ { \mathrm { I } } ^ { + }$satisfy$f _ { 1 } - f _ { 2 } = \varpi ^ { n } g$for some$g \in \mathbb { R } ^ { + }$, then for some larger$\mathrm { ~ J ~ } \supset \mathrm { { I } }$containing $g ,$also$f _ { 1 } - f _ { 2 } \in \varpi ^ { n } \mathbf { R } _ { \mathrm { J } } ^ { + }$. This shows that$\mathrm { R } ^ { + }$is the completed direct limit of the$\mathrm { R } _ { \mathrm { I } } ^ { + }$, i.e. $( \mathrm { R } , \mathrm { R } ^ { + } )$is the completed direct limit of the$( \mathrm { R } _ { \mathrm { I } } , \mathrm { R } _ { \mathrm { I } } ^ { + } )$

(ii) Let$( \mathrm { L } , \mathrm { L } ^ { + } )$be the direct limit of the$( \mathbf { R } _ { i } , \mathbf { R } _ { i } ^ { + } )$, equipped with the -adic topology. Then one checks by hand that$\mathrm { S p a ( L , L ^ { + } ) } \cong \operatorname* { l i m } _ { } \mathrm { S p a } ( \mathbf { R } _ { i } , \mathbf { R } _ { i } ^ { + } )$, compatible with rational subspaces. But then the same thing holds true for the completed direct limit by Proposition 2.11.

(iii) The completion of the direct limit of the$( \mathcal { O } _ { \mathrm { X } _ { j } } ( \mathrm { U } _ { j } ) , \mathcal { O } _ { \mathrm { X } _ { i } } ^ { + } ( \mathrm { U } _ { j } ) )$is a perfectoid affinoid K-algebra, and it satisfies the universal property describing$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$.

(iv) This is an abstract property of spectral spaces and spectral maps. Let$\mathbf { A } _ { i }$be the closed complement of$\mathrm { U } _ { i : }$, and for any$j \geq i ,$let$\mathrm { A } _ { j }$be the preimage of$\mathbf { A } _ { i }$in$\mathrm { X } _ { j }$. Then the $\operatorname { A } _ { j }$are constructible subsets of$\mathrm { X } _ { j } ,$hence spectral, and the transition maps between the$\mathrm { A } _ { j }$ are spectral. If one gives the$\operatorname { A } _ { j }$the constructible topology, they are compact topological spaces, and the transition maps are continuous. If their inverse limit is zero, then one of them has to be zero.-

Proposition 6.14. — Let K be ofany characteristic, and let$( \mathrm { R } , \mathrm { R } ^ { + } )$be a perfectoid affinoid ${ \mathrm { K } } { \cdot } a l g e b r a , { \mathrm { X } } = { \mathrm { S p a } } ( { \mathrm { R } } , { \mathrm { R } } ^ { + } )$. For any covering$\mathrm { X } = \mathrm { U } _ { i } \mathrm { U } _ { i }$by finitely many rational subsets, the

sequence

$$
0 \to \mathcal {O} _ {\mathrm{X}} (\mathrm{X}) ^ {\circ a} \to \prod_ {i} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i}) ^ {\circ a} \to \prod_ {i, j} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i} \cap \mathrm{U} _ {j}) ^ {\circ a} \to \dots
$$

is exact. In particular,$\mathcal { O } _ { \mathrm { X } }$is a sheaf, and$\mathrm { H } ^ { i } ( \mathrm { X } , { \mathcal { O } } _ { \mathrm { X } } ^ { o a } ) = 0 f o r i > 0$

Proof. — Assume first that K has characteristic p. We may replace K by a perfectoid subfield, such as the -adic completion of$\mathbf { F } _ { \boldsymbol { \phi } } ( ( \varpi ) ) ( \varpi ^ { 1 / \mathnormal { p } ^ { \infty } } ) ;$; this ensures that for any perfectoid affinoid K-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$, the ring$\mathrm { R } ^ { + }$is a$\mathrm { K ^ { \circ } - a l g e b r a }$. We note that the meaning of ’almost zero’ does not change under this substitution, as the maximal ideals are compatible. Then use Lemma 6.13 to write${ \mathrm { X } } = { \mathrm { S p a } } ( \mathrm { R } , \mathrm { R } ^ { + } ) \cong \operatorname* { l i m } _ { \bf \Pi } { \mathrm { X } } _ { i } = { \mathrm { S p a } } ( \mathrm { R } _ { i } , \mathrm { R } _ { i } ^ { + } )$ as an inverse limit, with$( \mathbf { R } _ { i } , \mathbf { R } _ { i } ^ { + } )$p-finite. Any rational subspace comes from a finite level, and a cover by finitely many rational subspaces is the pullback ofa cover by finitely many rational subspaces on a finite level. Hence the almost exactness of the sequence follows by taking the completion of the direct limit of the corresponding statement for$\mathrm { X } _ { i } ,$which is given by Proposition 6.11. The rest follows as before.

In characteristic 0, first use the exactness of the tilted sequence, then reduce modulo$\varpi ^ { \flat }$(which is still exact by flatness), and then remark that this is just the original sequence reduced modulo$\varpi$. As this is exact, the original sequence is exact, by flatness and completeness. Again, we also get the other statements.-

This finishes the proof of Theorem 6.3.

We see that to any perfectoid affinoid K-algebra$( \mathrm { R } , \mathrm { R } ^ { + } )$, we have associated an affinoid adic space$\mathrm { X = S p a ( R , R ^ { + } ) }$. We call these spaces affinoid perfectoid spaces.

Definition 6.15. — A perfectoid space is an adic space over K that is locally isomorphic to an affinoid perfectoid space. Morphisms between perfectoid spaces are the morphisms ofadic spaces.

The process of tilting glues.

Definition 6.16. — We say that a perfectoid space$\mathrm { X } ^ { \flat }$over$\mathrm { K } ^ { \flat }$is the tilt ofa perfectoid space X over K ifthere is afunctorial isomorphism Hom$( \mathrm { S p a } ( \mathrm { R } ^ { \flat } , \mathrm { R } ^ { \flat + } ) , \mathrm { X } ^ { \flat } ) = \mathrm { H o m } ( \mathrm { S p a } ( \mathrm { R } , \mathrm { R } ^ { + } ) ,$X) for all perfectoid affinoid K-algebras$( \mathrm { R } , \mathrm { R } ^ { + } )$with tilt$( \mathbf { R } ^ { \flat } , \mathbf { R } ^ { \flat + } )$

Proposition 6.17. — Any perfectoid space X over K admits a tilt$\mathrm { { X ^ { \flat } } } _ { . }$, unique up to unique isomorphism. This induces an equivalence between the category ofperfectoid spaces over K and the category ofperfectoid spaces over$\mathrm { K } ^ { \flat }$. The underlying topological spaces of X and$\mathrm { X } ^ { \flat }$are naturally identified. A perfectoid space X is affinoid perfectoid if and only if its tilt$\mathrm { X } ^ { \flat }$is affinoid perfectoid. Finally,for any affinoidperfectoid subspace$\mathrm { ~ U ~ C ~ X ~ } _ { \mathfrak { i } }$, the pair$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$is a perfectoid affinoid K-algebra with tilt$( \mathcal { O } _ { \mathrm { X } ^ { \flat } } ( \mathrm { U } ^ { \flat } ) , \mathcal { O } _ { \mathrm { X } ^ { \flat } } ^ { + } ( \mathrm { U } ^ { \flat } ) )$

Proof. — This is a formal consequence of Theorem 5.2, Theorem 6.3 and Proposition 2.19. Note that to any open$\mathrm { ~ U ~ } \subset \mathrm { ~ X ~ }$, one gets an associated perfectoid space with underlying topological space U by restricting the structure sheaf and valuations to U, and hence its global sections are$( \mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) , \mathcal { O } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$, so that if U is affinoid, then $\mathrm { U } = \mathrm { S p a } ( { \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } ) , { \mathcal { O } } _ { \mathrm { X } } ^ { + } ( \mathrm { U } ) )$. This gives the last part of the proposition.-

Let us finish this section by noting one way in which perfectoid spaces behave better than adic spaces (cf. Proposition 1.2.2 of [22]).

Proposition 6.18.$- \ : I f \mathrm { X } \right. \mathrm { Y } \left. \mathrm { Z }$are perfectoid spaces over$\mathrm { K } ,$then the fibre product $\mathrm { X } \times _ { \mathrm { Y } } \mathrm { Z }$exists in the category ofadic spaces over$\mathrm { K } ,$and is a perfectoid space.

Proof. — As usual, one reduces to the affine case,$\mathrm { X } = \mathrm { S p a } ( \mathrm { A } , \mathrm { A } ^ { + } ) , \mathrm { Y } = \mathrm { S p a } ( \mathrm { B } , \mathrm { B } ^ { + } )$ and$Z = \mathrm { S p a } ( \mathrm { C } , \mathrm { C } ^ { + } )$, and we want to construct$\mathrm { W } = \mathrm { X } \times _ { \mathrm { Y } } \mathrm { Z }$. This is given by$\mathrm { { W } } =$ $\mathrm { S p a ( D , D ^ { + } ) }$, where D is the completion of$\Nu \otimes _ { \mathrm { B } } \mathrm { C }$, and$\mathrm { D ^ { + } }$is the completion of the integral closure of the image of$\mathrm { A ^ { + } \otimes _ { B ^ { + } } C ^ { + } }$in D. Note that$\widehat { \mathbf { A } ^ { \circ a } \otimes _ { \mathbf { B } ^ { \circ a } } \mathbf { C } ^ { \circ a } }$is a perfectoid $\mathrm { K } ^ { \circ a } .$-algebra: It is enough to check that$\mathbf { A } ^ { \circ a } \otimes _ { \mathbf { B } ^ { \circ a } } \mathbf { C } ^ { \circ a } / \varpi$is flat over$\mathrm { K } ^ { \circ a } / \varpi$, hence one reduces to characteristic$\beta .$Here, it is enough to check that$\mathbf { A } ^ { \circ a } \otimes _ { \mathbf { B } ^ { \circ a } } \mathbf { C } ^ { \circ a }$is  -torsion free; but if$\varpi f = 0$, then$\varpi ^ { 1 / p } f ^ { 1 / p } = 0$by perfectness, hence$\varpi ^ { 1 / p } f = 0$. Continuing gives the result. In particular,$( \mathrm { D } , \mathrm { D } ^ { + } )$is a perfectoid affinoid K-algebra. One immediately checks that it satisfies the desired universal property.-

## 7. Perfectoid spaces: etale topology

In this section, we use the term locally noetherian adic space over k for the adic spaces over k considered in [22], i.e. they are locally of the form$\mathrm { S p a ( A , A ^ { + } ) }$, were$\mathrm { A }$is a strongly noetherian Tate k-algebra. If additionally, they are quasicompact and quasiseparated, we call them noetherian adic spaces.

Although perfectoid rings are always reduced, and hence a definition involving lifting of nilpotents is not possible, there is a good notion of étale morphisms. In the following definition, k can be an arbitrary nonarchimedean field.

Definition 7.1.

(i) A morphism$( \mathrm { R } , \mathrm { R } ^ { + } )  ( \mathrm { S } , \mathrm { S } ^ { + } )$) of affinoid k-algebras is called finite étale if S is a finite étale R-algebra with the induced topology, and$\mathrm { S ^ { + } }$is the integral closure of$\mathrm { \mathbf { R } } ^ { + }$in S.

(ii) A morphism$f : \mathrm { X } \to \mathrm { Y }$ofadic spaces over k is calledfinite étale ifthere is a cover ofY by open affinoids$\mathrm { \Delta V \subset Y }$such that the preimage${ \mathrm { U } } = f ^ { - 1 } ( { \mathrm { V } } )$is affinoid, and the associated morphism ofaffinoid k-algebras

$$
\left(\mathcal {O} _ {\mathrm{Y}} (\mathrm{V}), \mathcal {O} _ {\mathrm{Y}} ^ {+} (\mathrm{V})\right)\rightarrow \left(\mathcal {O} _ {\mathrm{X}} (\mathrm{U}), \mathcal {O} _ {\mathrm{X}} ^ {+} (\mathrm{U})\right)
$$

is finite étale.

(iii) A morphism f :$\mathrm { X } \to \mathrm { Y }$of adic spaces over k is called étale if for any point$x \in \mathrm { X }$there are open neighborhoods U and V ofx andf(x) and a commutative diagram

![](images/page_51_image_1.jpg)

wherej is an open embedding andp isfinite étale.

For locally noetherian adic spaces over$k ,$this recovers the usual notions, by Example 1.6.6(ii) and Lemma 2.2.8 of [22], respectively. We will see that these notions are useful in the case of perfectoid spaces, and will not use them otherwise. However, we will temporarily need a stronger notion of étale morphisms for perfectoid spaces. After proving the almost purity theorem, we will see that there is no difference. In the following let K be a perfectoid field again.

## Definition 7.2.

(i) A morphism$( \mathrm { R } , \mathrm { R } ^ { + } )  ( \mathrm { S } , \mathrm { S } ^ { + } )$ofperfectoid affinoid K-algebras is called stronglyfinite étale ifit isfinite étale and additionally$\mathrm { S } ^ { \circ a }$is afinite étale R<sup>◦a</sup>-algebra.

(ii) A morphism$f : \mathrm { X } \to \mathrm { Y }$of perfectoid spaces over K is called strongly finite étale if there is a cover of Y by open affinoid perfectoids$\mathrm { ~ V ~ C ~ Y ~ }$such that the preimage${ \mathrm { U } } = f ^ { - 1 } ( { \mathrm { V } } )$is affinoid perfectoid, and the associated morphism of perfectoid affinoid K-algebras

$$
\left(\mathcal {O} _ {\mathrm{Y}} (\mathrm{V}), \mathcal {O} _ {\mathrm{Y}} ^ {+} (\mathrm{V})\right)\rightarrow \left(\mathcal {O} _ {\mathrm{X}} (\mathrm{U}), \mathcal {O} _ {\mathrm{X}} ^ {+} (\mathrm{U})\right)
$$

is stronglyfinite étale.

(iii) A morphism$f : \mathrm { X } \to \mathrm { Y }$ofperfectoid spaces over K is called strongly étale iffor any point $x \in \mathrm { X }$there are open neighborhoods U and V ofx andf(x) and a commutative diagram

![](images/page_51_image_10.jpg)

wherej is an open embedding and p is stronglyfinite étale.

From the definitions, Proposition 6.17, and Theorem 5.25, we see that$f : \mathrm { X } \to \mathrm { Y }$ is strongly finite étale, resp. strongly étale, if and only if the tilt$f ^ { \flat } : \mathbf { X } ^ { \flat }  \mathbf { Y } ^ { \flat }$is strongly finite étale, resp. strongly étale. Moreover, in characteristic$\beta ,$anything (finite) étale is also strongly (finite) étale.

## Lemma 7.3.

(i) Let$f : \mathrm { X } \to \mathrm { Y }$be a stronglyfinite étale, resp. strongly étale, morphism ofperfectoid spaces and$l e t g : Z \to \mathrm { Y }$be an arbitrary morphism ofperfectoid spaces. Then$\mathrm { X } \times _ { \mathrm { Y } } \mathrm { Z } \to \mathrm { Z }$is a stronglyfinite étale, resp. strongly étale, morphism ofperfectoid spaces. Moreover, the map ofunderlying topological spaces$| \mathrm { X } \times _ { \mathrm { Z } } \mathrm { Y } | \to | \mathrm { X } | \times _ { | \mathrm { Z } | } | \mathrm { Y } |$is surjective.

(ii) If in (i), all spaces$\mathrm { X } = \mathrm { S p a } ( \mathrm { A } , \mathrm { A } ^ { + } ) , \mathrm { Y } = \mathrm { S p a } ( \mathrm { B } , \mathrm { B } ^ { + } )$and$Z = \mathrm { S p a } ( \mathrm { C } , \mathrm { C } ^ { + } )$are affinoid, with$( \mathrm { A } , \mathrm { A } ^ { + } )$) stronglyfinite étale over$( \mathrm { B } , \mathrm { B } ^ { + } )$, then$\mathrm { X } \times _ { \mathrm { Y } } \mathrm { Z } = \mathrm { S p a ( D , D ^ { + } ) }$, where$\mathrm { D } = \mathrm { A } \otimes _ { \mathrm { B } } \mathrm { C }$and$\mathrm { D ^ { + } }$is the integral closure$\scriptstyle { g f \mathbf { C } ^ { + } }$in D, and$( \mathrm { D } , \mathrm { D ^ { + } } )$is strongly finite étale over$\mathrm { ( C , C ^ { + } ) }$

(iii) Assume that K is ofcharacteristic$p . { \cal I f f } : \mathrm { X \to Y }$is afinite étale, resp. étale, morphism of adic spaces over k and$g : Z \to \mathrm { Y }$is a map from a perfectoid space Z to Y, then the fibre product$\mathrm { X } \times _ { \mathrm { Y } } \mathrm { Z }$exists in the category of adic spaces over K, is a perfectoid space, and the projection$\mathrm { X } \times _ { \mathrm { Y } } \mathrm { Z } \to \mathrm { Z }$isfinite étale, resp. étale. Moreover, the map ofunderlying topological spaces$| \mathrm { X } \times _ { \mathrm { Z } } \mathrm { Y } | \to | \mathrm { X } | \times _ { | \mathrm { Z } | } | \mathrm { Y } |$is surjective.

(iv) Assume that in the situation of(iii), all spaces$\mathrm { X } = \mathrm { S p a } ( \mathrm { A } , \mathrm { A } ^ { + } ) , \mathrm { Y } = \mathrm { S p a } ( \mathrm { B } , \mathrm { B } ^ { + } )$and ${ \cal Z } = \mathrm { S p a } ( \mathrm { C } , \mathrm { C } ^ { + } )$are affinoid, with$( \mathrm { A } , \mathrm { A } ^ { + } )$finite étale over$( \mathrm { B } , \mathrm { B } ^ { + } )$, then$\mathbf { X } \times _ { \mathrm { Y } } { Z } =$ Spa$( \mathrm { D } , \mathrm { D } ^ { + } )$, where$\mathrm { D } = \mathrm { A } \otimes _ { \mathrm { B } } \mathrm { C } , \mathrm { D } ^ { + }$is the integral closure${ \mathfrak { o f } } \mathrm { C } ^ { + }$in D and$( \mathrm { D } , \mathrm { D ^ { + } } )$ is finite étale over$\mathrm { ( C , C ^ { + } ) }$

Proof. — (ii) As$\mathbf { A } \otimes _ { \mathbf { B } } \mathbf { C }$is finite projective over$\mathrm { C } ,$it is already complete. One easily deduces the universal property. Also,$\mathbf { D } ^ { \circ a }$is finite étale over$\mathrm { C } ^ { \circ a }$, as base-change preserves finite étale morphisms.

(i) Applying the definition of a strongly finite étale map, one reduces the statement about strongly finite étale maps to the situation handled in part (ii). Now the statement for strongly étale maps follows, because fibre products obviously preserve open embeddings. The surjectivity statement follows from the argument of [20], proof of Lemma 3.9(i).

(iv) Proposition 5.23 shows that$\mathrm { D } = \mathrm { A } \otimes _ { \mathrm { B } } \mathrm { C }$is perfectoid. Therefore$\mathrm { S p a ( D , D ^ { + } ) }$ is a perfectoid space. One easily checks the universal property.

(iii) The finite étale case reduces to the situation considered in part (iv). Again, it is trivial to handle open embeddings, giving also the étale case. Surjectivity is proved as before.-

Let us recall the following statement about Henselian rings.

Proposition 7.4. — Let A be a flat$\mathrm { K } ^ { \circ } - a l g e b r a$such that A is Henselian along$( \varpi )$. Then the categories offinite étale$\mathrm { A } [ \varpi ^ { - 1 } ]$andfinite étale$\hat { \mathrm { A } } [ \varpi ^ { - 1 } ]$-algebras are equivalent, where$\hat { \mathrm { A } }$is the -adic completion ofA.

Proof. — See e.g. [15], Proposition 5.4.53.

We recall that  -adically complete algebras A are Henselian along (), and that if$\mathbf { A } _ { i }$is a direct system of$\mathrm { K } ^ { \circ }$-algebras Henselian along (), then so is the direct limit lim$\mathbf { A } _ { i }$. In particular, we get the following lemma.

## Lemma 7.5.

(i) Let$\mathrm { A } _ { i }$be afiltered direct system ofcompleteflat K<sup>◦</sup>-algebras, and let A be the completion of the direct limit, which is again a completeflat K<sup>◦</sup>-algebra. Then we have an equivalence of categories

$$
\mathrm{A} \big [ \varpi^ {- 1} \big ] _ {\text {fét}} \cong 2 - \varinjlim \mathrm{A} _ {i} \big [ \varpi^ {- 1} \big ] _ {\text {fét}}.
$$

In particular,$i f \mathrm { R } _ { i }$is afiltered direct system ofperfectoid K-algebras and R is the completion oftheir direct limit, then$\mathrm { R } _ { \mathrm { f e t } } \cong 2 - \operatorname* { l i m } _ { } ( \mathrm { R } _ { i } ) _ { \mathrm { f e t } }$

(ii) Assume that K has characteristic$\rho ,$and let$( \mathrm { R } , \mathrm { R } ^ { + } )$be a p-finite perfectoid affinoid K-algebra, given as the completed perfection of the reduced affinoid K-algebra$( \mathrm { S } , \mathrm { S } ^ { + } )$of topologicallyfinite type. Then$\mathrm { R } _ { \mathrm { f e t } } \cong \mathrm { S } _ { \mathrm { f e t } }$

Proof. — (i) Because finite étale covers, and morphisms between these, are finitely presented objects, we have

$$
\left(\varinjlim \mathrm{A} _ {i} \big [ \varpi^ {- 1} \big ]\right) _ {\text { f\'et}} \cong 2 - \varinjlim \mathrm{A} _ {i} \big [ \varpi^ {- 1} \big ] _ {\text { f\'et}}.
$$

On the other hand, lim$\mathbf { A } _ { i }$is Henselian along (), hence the left-hand side agrees with $\mathrm { A } [ \varpi ^ { - 1 } ] _ { \mathrm { f e t } }$by Proposition 7.4.

(ii) From part (i), we know that

$$
\mathrm{R} _ {\text {fét}} \cong 2 - \varinjlim \mathrm{S} _ {\text {fét}} ^ {1 / p ^ {n}}.
$$

But the categories$\mathrm { S } _ { \mathrm { f e t } } ^ { 1 / p ^ { n } }$are all equivalent to$\mathrm { S _ { f e t } }$.

Proposition 7$\mathbf { \delta } . 6 . - I f f : \mathrm { X \to Y }$is a stronglyfinite étale morphism ofperfectoid spaces, then for any open affinoidperfectoid$\mathrm { ~ V ~ C ~ Y ~ } _ { i }$, its preimage U is affinoidperfectoid, and

$$
\left(\mathcal {O} _ {\mathrm{Y}} (\mathrm{V}), \mathcal {O} _ {\mathrm{Y}} ^ {+} (\mathrm{V})\right)\rightarrow \left(\mathcal {O} _ {\mathrm{X}} (\mathrm{U}), \mathcal {O} _ {\mathrm{X}} ^ {+} (\mathrm{U})\right)
$$

is strongly finite étale.

Proof. — Tilting the situation and using Theorem 5.25, we immediately reduce to the case that K is of characteristic p. Again, we replace K by a perfectoid subfield to ensure that$\mathrm { R } ^ { + }$is a$\mathrm { K } ^ { \circ }$-algebra in all cases.

We may assume$\mathrm { Y = V = S p a ( R , R ^ { + } ) }$is affinoid. Writing$( \mathrm { R } , \mathrm { R } ^ { + } )$as the completion of the direct limit of p-finite perfectoid affinoid K-algebras$( \mathbf { R } _ { i } , \mathbf { R } _ { i } ^ { + } )$as in Lemma 6.13, we see that Y is already defined as a finite étale cover of some$\mathrm { Y } _ { i } =$ $\mathrm { S p a } ( \mathbf { R } _ { i } , \mathbf { R } _ { i } ^ { + } )$: Indeed, there are finitely many rational subsets of Y over which we have a finite étale cover; by Lemma 7.5(i), these are defined over a finite level, and because Y is quasi-separated, also the gluing data over intersections (as well as the cocycle condition) are defined over a finite level.

Hence by Lemma$7 . 3 ( \mathrm { i i } )$, we are reduced to the case that$( \mathrm { R } , \mathrm { R } ^ { + } )$is p-finite, given as the completed perfection of$( \mathrm { S } , \mathrm { S } ^ { + } )$. But then X is already defined as a finite étale cover of$Z = \mathrm { S p a } ( \mathrm { S } , \mathrm { S } ^ { + } )$by similar reasoning using Lemma 7.5(ii), and we conclude by using the result for locally noetherian adic spaces, cf. [22], Example 1.6.6(ii), and Lemma$7 . 3 ( \mathrm { i v } )$-

Using Proposition 5.23, this shows that if K is of characteristic$\beta ,$then the finite étale covers of an affinoid perfectoid space$\mathrm { X = \mathrm { S p a } ( R , R ^ { + } ) }$are the same as the finite étale covers of R.

The same method also proves the following proposition.

Proposition 7.7. — Assume that K is of characteristic p. Let f$: \mathrm { X }  \mathrm { Y }$be an étale map ofperfectoid spaces. Then for any$x \in \mathrm { X }$, there exist affinoid perfectoid neighborhoods$x \in \mathrm { U } \subset \mathrm { X } ,$ $f \mathrm { ( U ) } \subset \mathrm { V } \subset \mathrm { Y } .$, and an étale morphism ofaffinoid noetherian adic spaces$\mathrm { U } ^ { 0 } \to \mathrm { V } ^ { 0 }$over K, such that $\mathrm { U } = \mathrm { U } ^ { 0 } \times _ { \mathrm { V } ^ { 0 } } \mathrm { V }$

Proof. — We may assume that X and Y affinoid perfectoid, and that X is a rational subdomain of a finite étale cover of Y. Then one reduces to the p-finite case by the same argument as above, and hence to noetherian adic spaces.-

Corollary 7.8. — Strongly étale maps ofperfectoid spaces are open.${ \cal I } f f : \mathrm { X } \to \mathrm { Y } a n d g : \mathrm { Y } \to$ Z are strongly (finite) étale morphisms of perfectoid spaces, then the composite$g \circ f$is strongly (finite) étale.

Proof. — We may assume that K has characteristic$\beta .$. The first part follows directly from the previous proposition and the result for locally noetherian adic spaces, cf. [22], Proposition 1.7.8. For the second part, argue as in the previous proposition for bothf and $g$to reduce to the analogous result for locally noetherian adic spaces, [22], Proposition 1.6.7(ii).-

The following theorem gives a strong form of Faltings’s almost purity theorem.

Theorem${ \bf 7 . 9 . { - } } L e t \left( { \bf R , R ^ { + } } \right)$be a perfectoid affinoid K-algebra, and let$\mathrm { X = S p a ( R , R ^ { + } ) }$ with tilt X<sup>-</sup>.

(i) For any open affinoid perfectoid subspace$\mathrm { ~ U ~ C ~ X ~ } ,$, we have afullyfaithfulfunctorfrom the category of strongly finite étale covers of U to the category of finite étale covers of${ \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } )$, given by taking global sections.

(ii) For any U, thisfunctor is an equivalence ofcategories.

(iii) For any finite étale cover$\mathrm { S } / \mathrm { R } , \mathrm { S }$is perfectoid and$\mathrm { S } ^ { \circ a }$is finite étale over$\mathrm { R } ^ { \circ a }$. Moreover, $\mathrm { S } ^ { \circ a }$is a uniformly almostfinitely generated$\mathrm { R } ^ { \circ a }  – m o d u l e .$

Proof. — (i) By Proposition 7.6 and Theorem 5.25, the perfectoid spaces strongly finite étale over U are the same as the finite étale$\mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) ^ { \circ a } .$-algebras, which are a full subcategory of the finite étale$\mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) { \cdot } \mathrm { a l g e b r a s } .$

(ii) We may assume that$\mathrm { U } = \mathrm { X }$. Fix a finite étale R-algebra S. First we check that for any$x \in \mathrm { X }$, we can find an affinoid perfectoid neighborhood$x \in \mathrm { U } \subset \mathrm { X }$and a strongly finite étale cover$\mathrm { V }  \mathrm { U }$which gives via (i) the finite étale algebra$\mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ) \otimes _ { \mathrm { R } } \mathrm { S }$over ${ \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } )$

As a first step, note that we have an equivalence of categories between the direct limit of the category of finite étale${ \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } )$-algebras over all affinoid perfectoid neighborhoods U of x and the category of finite étale covers of the completion$\widehat { k ( x ) }$of the residue field at x, by Lemma 7.5(i). The latter is a perfectoid field.

By Theorem 3.7, the categories$\widehat { k ( x ) } _ { \mathrm { f e t } }$and$\widehat { k ( x ^ { \flat } ) } _ { \mathrm { f e t } }$are equivalent, where$k ( x ^ { \flat } )$is the residue field of$\mathrm { X } ^ { \flat }$at the point$x ^ { \mathrm { { b } } }$corresponding to x. Combining, we see that

$$
2 - \varinjlim_ {x \in \mathrm{U}} \bigl (\mathcal {O} _ {\mathrm{X}} (\mathrm{U}) \bigr) _ {\text {fet}} \cong 2 - \varinjlim_ {x \in \mathrm{U}} \bigl (\mathcal {O} _ {\mathrm{X} ^ {\flat}} \bigl (\mathrm{U} ^ {\flat} \bigr) \bigr) _ {\text {fet}}.
$$

In particular, we can find$\mathrm { V } ^ { \flat }$finite étale over$\mathrm { U } ^ { \flat }$for some U such that the pullbacks ofS to $\widehat { k ( x ) }$resp. ofthe global sections of$\mathrm { \Delta V ^ { \flat } }$to$\widehat { k ( x ^ { \flat } ) }$are tilts; but then, they are already identified over some smaller neighborhood. Shrinking U, we untilt to get the desired strongly finite étale$\mathrm { V }  \mathrm { U }$

This shows that there is a cover${ \mathrm { X } } = \cup { \mathrm { U } } _ { i }$by finitely many rational subsets and strongly finite étale maps$\mathrm { V } _ { i } \to \mathrm { U } _ { i }$such that the global sections of$\mathrm { V } _ { i }$are$\mathrm { S } _ { i } = { \mathcal { O } } _ { \mathrm { X } } ( \mathrm { U } _ { i } ) \otimes _ { \mathrm { R } }$ S. Let${ \mathrm { S } } _ { i } ^ { + }$be the integral closure of${ \mathcal { O } } _ { \mathrm { X } } ^ { + } ( \mathrm { U } _ { i } )$in$\mathrm { S } _ { i } \mathrm { ; }$then$\mathrm { V } _ { i } = \mathrm { S p a } ( \mathrm { S } _ { i } , \mathrm { S } _ { i } ^ { + } )$

By Lemma 7.3(ii), the pullback of$\mathrm { V } _ { i }$to some affinoid perfectoid$\mathrm { U } ^ { \prime } \subset \mathrm { U } _ { i }$has the same description, involving$\mathcal { O } _ { \mathrm { X } } ( \mathrm { U } ^ { \prime } ) \otimes _ { \mathrm { R } } \mathrm { S }$, and hence the$\mathrm { V } _ { i }$glue to some perfectoid space Y over X, and$\mathrm { Y }  \mathrm { X }$is strongly finite étale.$\mathrm { B y }$Proposition 7.6, Y is affinoid perfectoid, i.e.$\mathrm { Y = S p a ( A , A ^ { + } ) }$, with$( \mathrm { A } , \mathrm { A } ^ { + } )$an affinoid perfectoid K-algebra. It suffices to show that$\mathrm { A } = \mathrm { S }$. But the sheaf property of$\mathcal { O } _ { \mathrm { Y } }$gives us an exact sequence

$$
0 \to \mathrm{A} \to \prod_ {i} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i}) \otimes_ {\mathrm{R}} \mathrm{S} \to \prod_ {i, j} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i} \cap \mathrm{U} _ {j}) \otimes_ {\mathrm{R}} \mathrm{S}.
$$

On the other hand, the sheaf property for$\mathcal { O } _ { \mathrm { X } }$gives an exact sequence

$$
0 \to \mathrm{R} \to \prod_ {i} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i}) \to \prod_ {i, j} \mathcal {O} _ {\mathrm{X}} (\mathrm{U} _ {i} \cap \mathrm{U} _ {j}).
$$

Because S is flat over R, tensoring is exact, and the first sequence is identified with the second sequence after$\otimes _ { \mathbb { R } } \mathrm { S }$. Therefore$\mathrm { A } = \mathrm { S }$, as desired.

(iii) This is a formal consequence of part (ii), Proposition 7.6 and Theorem 5.25. -

We see in particular that any (finite) étale morphism of perfectoid spaces is strongly (finite) étale. Now one can also pullback étale maps between adic spaces in characteristic 0.

Proposition 7.10. — Parts (iii) and (iv) ofLemma 7.3 stay true in characteristic 0.

Proof. — The same proof as for Lemma 7.3 works, using Theorem 7.9(iii). -

Finally, we can define the étale site of a perfectoid space.

Definition 7.11. — Let X be a perfectoid space. Then the étale site of X is the category$\mathrm { X } _ { \mathrm { e t } }$of perfectoid spaces which are étale over$\mathrm { X } ,$and coverings are given by topological coverings. The associated topos is denoted$\mathrm { X } _ { \mathrm { e t } } ^ { \sim }$

The previous results show that all conditions on a site are satisfied, and that a morphism$f : \mathrm { X } \to \mathrm { Y }$of perfectoid spaces induces a morphism of sites$\mathrm { X } _ { \mathrm { e t } } \to \mathrm { Y } _ { \mathrm { e t } }$. Also, a morphism$f : \mathrm { X } \to \mathrm { Y }$from a perfectoid space X to a locally noetherian adic space Y induces a morphism of sites$\mathrm { X } _ { \mathrm { e t } } \to \mathrm { Y } _ { \mathrm { e t } }$

After these preparations, we get the technical main result.

Theorem 7.12. — Let X be a perfectoid space over K with tilt$\mathrm { X } ^ { \flat }$over$\mathrm { K } ^ { \flat }$. Then the tilting operation induces an isomorphism of sites$\mathrm { X } _ { \mathrm { e t } } \cong \mathrm { X } _ { \mathrm { e t } } ^ { \flat }$. This isomorphism isfunctorial in X.

Proof. — This is immediate.

The almost vanishing of cohomology proved in Proposition 6.14 extends to the étale topology.

Proposition 7.13. — For any perfectoid space X over K, the sheaf$\mathrm { \Delta U } \mapsto { \mathcal { O } } _ { \mathrm { U } } ( \mathrm { U } )$is a sheaf $\mathcal { O } _ { \mathrm { X } }$on$\mathrm { X } _ { \mathrm { e t } } ,$, and$\mathrm { H } ^ { i } ( \mathrm { X } _ { \mathrm { e t } } , \mathcal { O } _ { \mathrm { X } } ^ { o a } ) = 0 f o r i > 0$ifX is affinoidperfectoid.

Proof. — It suffices to check exactness of

$$
0 \to \mathcal {O} _ {\mathrm{X}} (\mathrm{X}) ^ {\circ a} \to \prod_ {i} \mathcal {O} _ {\mathrm{U} _ {i}} (\mathrm{U} _ {i}) ^ {\circ a} \to \prod_ {i, j} \mathcal {O} _ {\mathrm{U} _ {i} \times_ {\mathrm{X}} \mathrm{U} _ {j}} (\mathrm{U} _ {i} \times_ {\mathrm{X}} \mathrm{U} _ {j}) ^ {\circ a} \to \dots
$$

for any covering of an affinoid perfectoid X by finitely many étale$\mathrm { U } _ { i } \to \mathrm { X }$given as rational subsets of finite étale maps to rational subsets of X. Under tilting, this reduces to the assertion in characteristic${ p , }$and then to the assertion for p-finite$( \mathrm { R } , \mathrm { R } ^ { + } )$. In that case, one uses that the analogous sequence for noetherian adic spaces is exact up to a bounded  -power, and hence after taking the perfection almost exact.-

To make use of the étale site of a perfectoid space, we have to compare the étale sites of perfectoid spaces with those of locally noetherian adic spaces. This is possible under a certain assumption, cf. Section 2.4 of [22] for an analogous result.

Definition 7.14. — Let X be a perfectoid space. Further, let$\mathrm { X } _ { i } , i \in \mathrm { I } ,$be afiltered inverse system ofnoetherian adic spaces over K, and let$\varphi _ { i } : \mathrm { X } \to \mathrm { X } _ { i } , i \in \mathrm { I }$, be a map to the inverse system.

Then we write X ∼ lim X ifthe mapping ofunderlying topological spaces$| { \mathrm { X } } | \to \varprojlim | { \mathrm { X } } _ { i } |$is a homeomorphism, andfor any$x \in \mathrm { X }$with images$x _ { i } \in \mathrm { X } _ { i } .$, the map ofresiduefield

$$
\varinjlim k (x _ {i}) \to k (x)
$$

has dense image.

Remark 7.15. — We recall that by assumption all$\mathrm { X } _ { i }$are qcqs. If$\mathrm { \Delta X } \sim \mathrm { l i m } \mathrm { X } _ { i }$, then |X| is an inverse limit ofspectral spaces with spectral transition maps, hence spectral, and in particular qcqs again.

Proposition 7.16. — Let the situation be as in Definition$7 . I 4 ,$and let$\mathrm { Y }  \mathrm { X } _ { i }$be an étale morphism ofnoetherian adic spaces. Then$\mathrm { Y } \times _ { \mathrm { X } _ { i } } \mathrm { X } \sim \varprojlim _ { j \geq i } \mathrm { Y } \times _ { \mathrm { X } _ { i } } \mathrm { X } _ { j }$

Proof. — The same proof as for Remark 2.4.3 of [22] works. In particular, we note that in Definition$7 . 1 4 , { \mathrm { i f ~ } } | { \mathrm { X } } |  { \mathrm { l i m } } | { \mathrm { X } } _ { i } |$is bijective and the condition on residue fields is satisfied, then already$\mathrm { X } \sim \varprojlim _ { i } \bar { \mathrm { X } } _ { i } , \mathrm { i . e . } \ | \mathrm { X } |  \varprojlim _ { i } | \mathrm { X } _ { i } |$is a homeomorphism. To check this, assume that$\mathrm { U } \subset \mathrm { X }$is a quasicompact open subset,$x \in \mathrm { U } , y \notin \mathrm { U }$. Let$x _ { i } , y _ { i } \in \mathrm { X } _ { i }$be their images. It is enough to find some i and$\mathrm { U } _ { i } \subset \mathrm { X } _ { i }$open such that$x _ { i } \in \mathrm { U } _ { i } ,$but$y _ { i } \notin \mathrm { U } _ { i }$ If$x _ { i }$and$y _ { i }$do not have the same maximal generalization for all$i ,$this is immediate. Otherwise, the situation is easily described in terms of the residue field at this maximal generalization.-

With this definition, we have the following analogue of Proposition 2.4.4 of [22]. We refer to SGA IV, Exposé VI, §8, for generalities concerning projective limits of fibred topoi.

Theorem 7.17. — Let the situation be as in Definition 7.14. Then$\mathrm { X } _ { \mathrm { e t } } ^ { \sim }$is a projective limit of the fibred topos$( \mathrm { X } _ { i , \mathrm { e t } } ^ { \sim } ) _ { i }$<sub>i</sub>.

Proof. — The same proof as for Proposition 2.4.4 of [22] works, except that one uses that any étale morphism factors locally as the composite of an open immersion and a finite étale map instead of appealing to Corollary 1.7.3 of [22] on the top of page 128. The latter kind ofmorphisms can be descended to a finite level because ofLemma 7.5. -

As in [22], Corollary 2.4.6, this gives the following corollary.

Corollary 7.18. — Let the situation be as in Definition 7.14, and let$\mathrm { F } _ { i }$be a sheafofabelian groups on$\mathbf { X } _ { i , \mathrm { e t } } ,$, with preimages$\mathrm { F } _ { j }$on$\mathrm { X } _ { j , \mathrm { e t } } f o r j \ge i$and F on$\mathrm { X } _ { \mathrm { e t } }$. Then the natural mapping

$$
\varinjlim \mathrm{H} ^ {n} (\mathrm{X} _ {j, \text { ét }}, \mathrm{F} _ {j}) \rightarrow \mathrm{H} ^ {n} (\mathrm{X} _ {\text { ét }}, \mathrm{F})
$$

is bijectivefor all$n \geq 0$

In some cases, one can even say more.

Corollary 7.19. — Assume that in the situation ofDefinition 7.14 all transition maps$\mathrm { X } _ { j } \to \mathrm { X } _ { i }$ induce purely inseparable extensions on completed residuefields and homeomorphisms$| \mathrm { X } _ { j } | \to | \mathrm { X } _ { i } |$. Then $\mathrm { X } _ { \mathrm { e t } } ^ { \sim }$is equivalent to$\mathrm { X } _ { i , \mathrm { e t } } ^ { \sim } { f o r }$any i.

Proof. — Use the remark after Proposition 2.3.7 of [22].

## 8. An example: toric varieties

Let us recall the definition of a toric variety, valid over any field k.

Definition 8.1. — A toric variety over$k$is a normal separated scheme X offinite type over k with an action ofa split torus$\mathrm { T } \cong \mathbf { G } _ { m } ^ { k }$on X and a point$x \in \mathrm { X } ( k )$with trivial stabilizer in T, such that the T-orbit$\mathrm { T } \cong \mathrm { T } x = \mathrm { U } \subset \mathrm { X }$of x is open and dense.

We recall that toric varieties may be described in terms of fans.

Definition 8.2. — Let N be afree abelian group offinite rank.

(i) A strongly convex polyhedral cone σ in N ⊗ R is a subset oftheform$\sigma = \mathbf { R } _ { \geq 0 } x _ { 1 } + \cdot \cdot \cdot +$ ${ \bf R } _ { \geq 0 } x _ { n } f o r$certain$x _ { 1 } , \ldots , x _ { n } \in \mathrm { N } _ { \cdot }$, subject to the condition that σ contains no line through the origin.

(ii) Afan  in$\mathbf { N } \otimes \mathbf { \mathbf { R } }$is a nonemptyfinite collection ofstrongly convex polyhedral cones stable under takingfaces, and such that the intersection ofany two cones in$\Sigma$is aface ofboth of them.

Let$\mathbf { M } = \mathrm { H o m } ( \mathrm { N } , \mathbf { Z } )$be the dual lattice. To any strongly convex polyhedral cone $\sigma \subset \mathbf { N } \otimes \mathbf { R }$, one gets the dua$\sigma ^ { \vee } \subset \operatorname { M } \otimes \mathbf { R }$, and we associate to σ the variety

$$
\mathrm{U} _ {\sigma} = \operatorname{Spec} k \left[ \sigma^ {\vee} \cap \mathrm{M} \right].
$$

We denote the function on$\mathrm { U } _ { \sigma }$corresponding to$u \in \sigma ^ { \vee } \cap \mathbf { M }$by$\chi ^ { u }$. If τ is a face of$\sigma$, then$\sigma ^ { \vee } \subset \tau ^ { \vee } ,$, inducing an open immersion$\mathrm { U } _ { \tau } \to \mathrm { U } _ { \sigma }$. These maps allow us to glue a variety$\mathrm { X } _ { \Sigma }$associated to any fan . Note that$\mathrm { T } = \mathrm { U } _ { \{ 0 \} } = \mathrm { S p e c } k [ \mathrm { M } ]$is a torus, which acts on$\mathrm { X } _ { \Sigma }$with open dense orbit$\mathrm { U } _ { \{ 0 \} } \subset \mathrm { X } _ { \Sigma }$. Also T has the base point$1 \in \mathrm { T } .$, giving a point$x \in \mathrm { X } ( k )$, making$\mathrm { X } _ { \Sigma }$a toric variety. Let us recall the classification of toric varieties.

Theorem 8.3. — Any toric variety over$k$is canonically isomorphic to$\mathrm { X } _ { \Sigma } f o r$a uniquefan  in$\mathbf { X } _ { \ast } ( \mathrm { T } ) \otimes \mathbf { R }$

We also need to recall some statements about divisors on toric varieties.

Definition/Proposition$8 . 4 . \mathrm { ~ - ~ } L e t \left\{ \tau _ { i } \right\} \subset \Sigma$be the 1-dimensional cones, andfix a generator $\begin{array} { r } { v _ { i } \in \tau _ { i } \cap \mathrm { N } \varrho f \tau _ { i } \cap \mathrm { N } . } \end{array}$. Each τ gives rise to$\mathbf { U } _ { \tau _ { i } } \cong \mathbf { A } ^ { 1 } \times \mathbf { G } _ { m } ^ { k - 1 }$, giving rise to a T-invariant Weil divisor $\mathrm { D } _ { i } = \mathrm { D } ( \tau _ { i } )$on$\mathrm { X } _ { \Sigma } .$, defined as the closure${ \bf { \Lambda } } _ { o f } \{ 0 \} \times { \bf { G } } _ { m } ^ { k - 1 }$

A T-Weil divisor is by definition an element${ \mathfrak { o f } } \bigoplus _ { i } \mathbf { Z } \mathbf { D } _ { i }$. Every Weil divisor is equivalent to a T-Weil divisor.$\begin{array} { r } { I f \mathrm { D } = \sum a _ { i } \mathrm { D } _ { i } } \end{array}$is a T-Weil divisor, then

$$
\mathrm{H}^{0}\bigl (\mathrm{X}_{\Sigma},\mathcal{O}(\mathrm{D})\bigr) = \bigoplus_{\substack{u\in \mathrm{M}\\ \langle u,v_{i}\rangle \geq -a_{i}}}k\chi^{u}.
$$

Now we adapt these definitions to the world of usual adic spaces, and to the world of perfectoid spaces. Assume first that$k$is a complete nonarchimedean field, and let$\Sigma$ be a fan as above. Then we can associate to  the adic space$\mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$of finite type over$k$ which is glued out of

$$
\mathcal {U} _ {\sigma} ^ {\mathrm{ad}} = \operatorname{Spa} \bigl (k \bigl \langle \sigma^ {\vee} \cap \mathrm{M} \bigr \rangle , k ^ {\circ} \bigl \langle \sigma^ {\vee} \cap \mathrm{M} \bigr \rangle \bigr).
$$

We note that this is not in general the adic space$\mathrm { X } _ { \Sigma } ^ { \mathrm { a d } }$over k associated to the variety$\mathrm { X } _ { \Sigma }$: For example, if$\mathrm { X } _ { \Sigma }$is just affine space, then$\mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$will be a closed unit ball. In general, let $\mathrm { X } _ { \Sigma , k ^ { \circ } }$be the toric scheme over$k ^ { \circ }$associated to . Let$\hat { \mathrm { X } } _ { \Sigma , k ^ { \circ } }$be the formal completion of $\mathrm { X } _ { \Sigma , k ^ { \circ } }$along its special fibre, which is an admissible formal scheme over$k ^ { \circ }$. Then$\mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$is the generic fibre$\hat { \mathrm { X } } _ { \Sigma , k ^ { \circ } } ^ { \mathrm { a d } }$associated to$\hat { \mathrm { X } } _ { \Sigma , k ^ { \circ } }$. In particular, if$\mathrm { \Delta X _ { \Sigma } }$is proper, then$\mathrm { X } _ { \Sigma } ^ { \mathrm { a d } } = \mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$

Similarly, if K is a perfectoid field, we can associate a perfectoid space$\mathcal { X } _ { \Sigma } ^ { \mathrm { p e r f } }$over K to$\Sigma _ { i }$, which is glued out of

$$
\mathcal {U} _ {\sigma} ^ {\text { perf }} = \operatorname{Spa} \left(\mathrm{K} \left\langle \sigma^ {\vee} \cap \mathrm{M} [ p ^ {- 1} ] \right\rangle , \mathrm{K} ^ {\circ} \left\langle \sigma^ {\vee} \cap \mathrm{M} [ p ^ {- 1} ] \right\rangle\right).
$$

Note that on$\mathcal { X } _ { \Sigma } ^ { \mathrm { p e r f } } :$, we have a sheaf$\mathcal { O } ( \mathrm { D } )$for any$\mathbf { D } \in \oplus \mathbf { Z } [ \boldsymbol { p } ^ { - 1 } ] \mathbf { D } _ { i }$. Moreover, $\mathrm { H } ^ { \mathrm { 0 } } ( \mathcal { X } _ { \Sigma } ^ { \mathrm { p e r f } } , \mathcal { O } ( \mathrm { D } ) )$is the free Banach-K-vector space with basis given by$\{ \chi ^ { u } \}$, where u ranges over$u \in \mathbf { M } [ \boldsymbol { \phi } ^ { - 1 } ]$with$\left. u , v _ { i } \right. \geq - a _ { i }$

We have the following comparison statements. Note that any toric variety$\mathrm { X } _ { \Sigma }$ comes with a map$\varphi : { \mathrm { X } } _ { \Sigma } \to { \mathrm { X } } _ { \Sigma }$induced from multiplication by$\boldsymbol { p }$on$\operatorname { M } ;$the same applies to$\mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$, etc. For clarity, we use subscripts to denote the field over which we consider the toric variety.

Theorem 8.5. — Let K be a perfectoidfield with tilt$\mathrm { K } ^ { \flat }$.

(i) The perfectoid space$\mathcal { X } _ { \Sigma , \mathrm { K } } ^ { \mathrm { p e r f } }$tilts to$\mathcal { X } _ { \Sigma , \mathrm { K } ^ { \flat } } ^ { \mathrm { p e r f } }$

(ii) The perfectoid space$\mathcal { X } _ { \Sigma , \mathrm { K } } ^ { \mathrm { p e r f } }$can be written as

$$
\mathcal {X} _ {\Sigma , \mathrm{K}} ^ {\text { perf }} \sim \varprojlim_ {\varphi} \mathcal {X} _ {\Sigma , \mathrm{K}} ^ {\text { ad }}.
$$

(iii) There is a homeomorphism of topological spaces

$$
\left| \mathcal {X} _ {\Sigma , \mathrm{K} ^ {\flat}} ^ {\mathrm{ad}} \right| \cong \varprojlim_ {\varphi} \left| \mathcal {X} _ {\Sigma , \mathrm{K}} ^ {\mathrm{ad}} \right|.
$$

(iv) There is an isomorphism ofétale topoi

$$
\bigl (\mathcal {X} _ {\Sigma , \mathrm{K} ^ {\flat}} ^ {\mathrm{ad}} \bigr) _ {\acute {\mathrm{et}}} ^ {\sim} \cong \varprojlim_ {\varphi} \bigl (\mathcal {X} _ {\Sigma , \mathrm{K}} ^ {\mathrm{ad}} \bigr) _ {\acute {\mathrm{et}}} ^ {\sim}.
$$

(v) For any open subset$\mathrm { ~ U ~ C ~ } \mathcal { X } _ { \Sigma , \mathrm { K } } ^ { \mathrm { a d } }$with preimage$\mathrm { { V } } \subset { \mathcal { X } } _ { \Sigma , \mathrm { K } ^ { \flat } } ^ { \mathrm { { a d } } }$, we have a morphism ofétale topoi$\mathrm { V } _ { \mathrm { e t } } ^ { \sim }  \mathrm { U } _ { \mathrm { e t } } ^ { \sim }$, giving a commutative diagram

![](images/page_60_image_7.jpg)

Proof. — This is an immediate consequence of our previous results: Part (i) can be checked on affinoid pieces, where it is an immediate generalization of Proposition 5.20. Part (ii) can be checked one affinoid pieces again, where it is easy. Then parts (iii) and (iv) follow from Theorem 7.17, Corollary 7.19 and the preservation oftopological spaces and étale topoi under tilting. Finally, part (v) follows from Proposition 7.16, using the previous arguments.-

Let us denote by$\pi : \mathcal { X } _ { \Sigma , \mathrm { K } ^ { \flat } } ^ { \mathrm { a d } } \to \mathcal { X } _ { \Sigma , \mathrm { K } } ^ { \mathrm { a d } }$the projection, which exists on topological spaces and étale topoi. In the following, we restrict to proper smooth toric varieties for simplicity.

Proposition 8.6. — Let$\mathrm { X } _ { \Sigma }$be a proper smooth toric variety. Let$\ell \neq p$be prime. Assume that K, and hence K<sup>-</sup>, is algebraically closed. Then for all$i \in \mathbf { Z } _ { \cdot }$, the projection map π induces an isomorphism

$$
\mathrm{H} ^ {i} \big (\mathrm{X} _ {\Sigma , \mathrm{K}, \acute {\mathrm{et}}} ^ {\mathrm{ad}}, \mathbf {Z} / \ell^ {m} \mathbf {Z} \big) \cong \mathrm{H} ^ {i} \big (\mathrm{X} _ {\Sigma , \mathrm{K} ^ {\flat}, \acute {\mathrm{et}}} ^ {\mathrm{ad}}, \mathbf {Z} / \ell^ {m} \mathbf {Z} \big).
$$

Proof. — This follows from part$( \mathrm { i v } )$of the previous theorem combined with the observation that$\varphi : \mathrm { X _ { \Sigma , K } ^ { a d } } \to \mathrm { X _ { \Sigma , K } ^ { a d } }$induces an isomorphism on cohomology with$\mathbf { Z } / \ell ^ { m } \mathbf { Z } \mathbf { \cdot }$ coefficients. Using proper base change, this can be checked on$\mathrm { X } _ { \Sigma , \kappa }$, where κ is the residue field of K. But here,$\varphi$is purely inseparable, and hence induces an equivalence of étale topoi.-

We need the following approximation property.

Proposition 8.7. — Assume that$\mathrm { X } _ { \Sigma , \mathrm { K } }$is proper smooth. Let$\mathrm { Y } \subset \mathrm { X } _ { \Sigma , \mathrm { K } }$be a hypersurface. Let $\tilde { \mathrm { Y } } \subset \mathrm { X ^ { a d } _ { \Sigma , K } } ^ { \mathrm { * } }$be a small open neighborhood ofY. Then there exists a hypersurface$\mathrm { Z } \subset \mathrm { X } _ { \Sigma , \mathrm { K } ^ { \flat } }$such that $Z ^ { \mathrm { a d } } \subset \pi ^ { - 1 } ( \tilde { \mathrm { Y } } )$. One can assume that Z is defined over a given dense subfield of$\mathrm { K } ^ { \flat }$

Proof. — Let$\mathrm { D } = \sum { a _ { i } \mathrm { D } } _ { i }$be a T-Weil divisor representing Y. Let$f \in { \bf H } ^ { 0 } ( { \bf X } _ { \Sigma , \mathrm { K } }$, O(D)) be the equation with zero locus Y. Consider the graded ring

$$
\bigoplus_{j\in \mathbf{Z}[p^{-1}]}H^{0}\big(\mathcal{X}_{\Sigma ,K}^{\text{perf}},\mathcal{O}(jD)\big) = \bigoplus_{j\in \mathbf{Z}[p^{-1}]}\widehat{\bigoplus}_{\substack{u\in M[p^{-1}]\\ \langle u,v_{i}\rangle \geq -ja_{i}}}\mathrm{K}\chi^{u},
$$

and let R be its completion (with respect to the obvious$\mathrm { K } ^ { \circ }$-submodule). Here$\widehat { \oplus }$denotes the Banach space direct sum. Then as in Proposition 5.20, R is a perfectoid K-algebra whose tilt is given by the similar construction over$\mathrm { K } ^ { \flat }$. Note that D is given combinatori ally and hence transfers to$\mathrm { K } ^ { \flat }$

We may assume that$\tilde { \mathrm { Y } }$is given by

$$
\tilde {\mathrm{Y}} = \left\{x \in \mathrm{X} _ {\Sigma , \mathrm{K}} ^ {\mathrm{ad}} \mid | f (x) | \leq \epsilon \right\},
$$

for some . In order to make sense of the inequality$| f ( x ) | \leq \epsilon .$, note that$\mathrm { X } _ { \Sigma , \mathrm { K } }$and$\mathcal { O } ( \mathrm { D } )$ have a tautological integral model over$\mathrm { K } ^ { \circ }$(by applying the toric constructions over$\mathrm { K } ^ { \circ } )$ which is enough to talk about absolute values: Trivialize the line bundle$\mathcal { O } ( \mathrm { D } )$locally on the integral model to interpretf as a function; any two different choices differ by a unit of$\mathrm { K } ^ { \circ }$, and hence give the same absolute value.

Now the analogue of Lemma 6.5 holds true for R, with the same proof. This implies that we can find$g \in \mathrm { H } ^ { \mathrm { 0 } } ( \mathcal { X } _ { \Sigma , \mathrm { K } ^ { \flat } } ^ { \mathrm { p e r f } } , \mathcal { O } ( \mathrm { D } ) )$such that

$$
\pi^ {- 1} (\tilde {\mathrm{Y}}) = \left\{x \in \mathcal {X} _ {\Sigma , \mathrm{K} ^ {\flat}} ^ {\text { perf }} \mid | g (x) | \leq \epsilon \right\}.
$$

Let$k \subset \mathrm { K } ^ { \flat }$be a dense subfield. Changing g slightly, we can assume that

$$
g\in \bigoplus_{\substack{u\in \operatorname{M}[p^{-1}]\\ \langle u,v_{i}\rangle \geq -ja_{i}}}k\chi^{u}.
$$

Replacing g by a large p-power gives a regular function h on$\mathrm { X } _ { \Sigma , \mathrm { K } ^ { \flat } }$, such that its zero locus$\mathrm { Z } \subset \mathrm { X } _ { \Sigma , \mathrm { K } ^ { \flat } }$is contained in$\bar { \pi } ^ { - 1 } ( \tilde { \mathrm { Y } } )$, as desired.-

By intersecting several hypersurfaces, one arrives at the following corollary.

Corollary 8.8. — Assume that$\mathrm { X } _ { \Sigma , \mathrm { K } }$is projective and smooth. Let$\mathrm { Y } \subset \mathrm { X } _ { \Sigma , \mathrm { K } }$be a set-theoretic complete intersection, i.e. Y is set-theoretically equal to an intersection$\mathrm { Y } _ { 1 } \cap \cdots \cap \mathrm { Y } _ { c }$ofhypersurfaces $\mathrm { Y } _ { i } \subset \mathrm { X } _ { \Sigma , \mathrm { K } }$, where c is the codimension ofY. Let$\tilde { \mathrm { Y } } \subset \mathrm { X ^ { a d } _ { \Sigma , K } }$be a small open neighborhood ofY. Then there exists a closed subvariety$\mathrm { Z } \subset \mathrm { X } _ { \Sigma , \mathrm { K } ^ { \flat } }$such that$Z ^ { \mathrm { a d } } \subset \pi ^ { - 1 } ( \tilde { \mathrm { Y } } )$with dim${ \boldsymbol { Z } } = \dim { \boldsymbol { \mathrm { Y } } }$. One can assume that Z is defined over a given dense subfield ofK<sup>-</sup>.

Proof. — The only nontrivial point is to check that the intersection over$\mathrm { K } ^ { \flat }$will be nonempty; if the dimension was too large, one can also just cut by further hypersurfaces. For nonemptiness, choose an ample line bundle to define a notion of degree of subvarieties; then the degree of a complete intersection is determined combinatorially. As Y has positive degree, so has the corresponding complete intersection over$\mathrm { K } ^ { \flat }$, and in particular is nonempty.-

## 9. The weight-monodromy conjecture

We first recall some facts about -adic representations ofthe absolute Galois group $\mathrm { G } _ { k } = \mathrm { G a l } ( \bar { k } / k )$of a local field k of residue characteristic${ p , }$cf. [25]. Let$q$be the cardinality of the residue field of k. Recall that the maximal pro--quotient of the inertia subgroup$\mathrm { I } _ { k } \subset \mathrm { G } _ { k }$is given by the quotient$t _ { \ell } : \mathrm { I } _ { k } \to \mathbf { Z } _ { \ell } ( 1 )$, which is the inverse limit of the homomorphisms$t _ { \ell , n } : \mathrm { I } _ { k } \to \mu _ { \ell ^ { n } }$defined by choosing a system of$\ell ^ { n } .$-th roots$\varpi ^ { 1 / \ell ^ { n } }$of a uniformizer$\varpi$of$\mathrm { ~  ~ \cdot ~ } { \boldsymbol { k } } ,$and requiring

$$
\sigma \left(\varpi^ {1 / \ell^ {n}}\right) = t _ {\ell , n} (\sigma) \varpi^ {1 / \ell^ {n}}
$$

for all$\sigma \in \mathrm { I } _ { k }$. Now recall Grothendieck’s quasi-unipotence theorem.

Proposition 9.1. — Let V be a finite-dimensional$\bar { \mathbf { Q } } _ { \ell }$-representation of$\mathrm { G } _ { k } ,$given by a map $\rho : { \mathrm { G } } _ { k } \to { \mathrm { G L } } ( \mathrm { V } )$. Then there is an open subgroup$\mathrm { I } _ { 1 } \subset \mathrm { I } _ { k }$such that for all$\sigma \in \operatorname { I } _ { 1 }$, the element $\rho ( \sigma ) \in \mathrm { G L } ( \mathrm { V } )$is unipotent, and in this case there is a unique nilpotent morphism N :$\mathrm { V } \to \mathrm { V } ( - 1 )$ such thatfor all$\sigma \in \operatorname { I } _ { 1 }$

$$
\rho (\sigma) = \exp \bigl (\mathrm{N} t _ {\ell} (g) \bigr).
$$

We fix an isomorphism$\mathbf { Q } _ { \ell } ( 1 ) \cong \mathbf { Q }$in order to consider N as a nilpotent endomorphism ofV. Changing the choice ofisomorphism$\mathbf { Q } _ { \ell } ( 1 ) \cong \mathbf { Q } _ { \ell }$replaces N by a scalar multiple, which will have no effect on the following discussion. From uniqueness of$\mathrm { N } ,$it follows that for any geometric Frobenius element$\Phi \in \mathrm { G } _ { k } ,$, we have$\mathrm { N } \Phi = q \Phi \mathrm { N }$

Also recall the general monodromy filtration.

Definition/Proposition 9.2. — Let V be a finite-dimensional vector space over any$~ f u e l d ,$and let$\mathrm { { N } : \mathrm { { V } \to \mathrm { { V } } } }$be a nilpotent morphism. Then there is a unique separated and exhaustive increasing filtration$\mathrm { F i l } _ { i } ^ { \mathrm { N } } \mathrm { V } \subset \mathrm { V } , i \in { \bf Z } .$called the monodromyfiltration, such that$\mathrm { N } ( \mathrm { F i l } _ { i } ^ { \mathrm { N } } \mathrm { V } ) \subset \mathrm { F i l } _ { i - 2 } ^ { \mathrm { N } } \mathrm { V }$for all $i \in \mathbf { Z }$and$\mathrm { g r } _ { i } ^ { \mathrm { N } } \mathrm { V } \cong \mathrm { g r } _ { - i } ^ { \mathrm { N } } \mathrm { V }$via N<sup>i</sup> for all$i \geq 0$

In fact, we have the formula

$$
\mathrm{Fil} _ {i} ^ {\mathrm{N}} \mathrm{V} = \sum_ {i _ {1} - i _ {2} = i} \ker \mathrm{N} ^ {i _ {1} + 1} \cap \operatorname{im} \mathrm{N} ^ {i _ {2}}
$$

for the monodromy filtration. Now we can formulate the weight-monodromy conjecture.

Conjecture 9.3 (Deligne$\mathit { 2 9 7 } ) . \mathrm { - }$Let X be a proper smooth variety over$k ,$and let$\mathrm { V } =$ $\mathrm { H } ^ { i } ( \mathrm { X } _ { \bar { k } } , \bar { \mathbf { Q } } _ { \ell } )$. Then for all$j \in \mathbf { Z }$andfor any geometric Frobenius$\Phi \in \mathrm { G } _ { k } .$, all eigenvalues$\varrho f \Phi$on $\mathrm { g r } _ { j } ^ { \mathrm { N } } \mathrm { V }$are Weil numbers ofweight$i + j ,$, i.e. algebraic numbers α such that$| \alpha | = q ^ { ( i + \bar { j } ) / 2 }$for all complex absolute values.

We note that in order to prove this conjecture, one is allowed to replace k by a finite extension. Using the formalism of$\zeta -$- and L-functions, the conjecture has the following interpretation. Let K be a global field, and let$\mathbf { X } / \mathbf { K }$be a proper smooth variety. Choose some integer i. Recall that the L-function associated to the i-th -adic cohomology group $\mathrm { H } ^ { i } ( \mathrm { X } ) = \mathrm { H } ^ { i } ( \mathrm { X } _ { \bar { \bf K } } , \bar { \bf Q } _ { \ell } )$of X is defined as a product

$$
\mathrm{L} \big (\mathrm{H} ^ {i} (\mathrm{X}), s \big) = \prod_ {v} \mathrm{L} _ {v} \big (\mathrm{H} ^ {i} (\mathrm{X}), s \big),
$$

where the product runs over all places v of$\mathrm { K }$. Let us recall the definition of the local factor at a finite prime v not dividing$\ell ,$whose local field is$k \mathrm { : }$

$$
\mathrm{L} _ {v} \big (\mathrm{H} ^ {i} (\mathrm{X}), s \big) = \det \big (1 - q ^ {- s} \Phi \mid \mathrm{H} ^ {i} (\mathrm{X}) ^ {\mathrm{I} _ {k}} \big) ^ {- 1}.
$$

At primes of good reduction, the Weil conjectures imply that all poles of this expression have real part$\frac { i } { 2 } .$. Moreover, one checks in the usual way that hence the product defining $\mathrm { L } ( \mathrm { H } ^ { i } ( \mathrm { X } ) , s )$is absolutely convergent when the real part of s is greater than$\textstyle { \frac { i } { 2 } } + 1$, except possibly for finitely many factors. The weight-monodromy conjecture implies that all other local factors will not have any poles of real part greater than$\frac { i } { 2 } .$

Over equal characteristic local fields, Deligne [10] turned this argument into a proof:

Theorem 9.4. — Let C be a curve over$\mathbf { F } _ { q } , x \in \mathrm { C } ( \mathbf { F } _ { q } )$, such that k is the localfield ofC at x. Let X be a proper smooth scheme over$\mathrm { ~ C ~ } \backslash \{ x \}$. Then the weight-monodromy conjecture holds truefor $\mathrm { X } _ { k } = \mathrm { X } \times _ { \mathrm { C } \backslash \{ x \} }$Spec k.

Let us give a briefsummary ofthe proof. Let$f : \mathrm { X } \to \mathrm { C } \setminus \{ x \}$be the proper smooth morphism. Possibly replacing C by a finite cover, we may assume that the action of$\mathrm { T } _ { k }$on $\mathrm { V } = \bar { \mathrm { H } } ^ { i } ( \mathrm { X } _ { \bar { k } } , \bar { \mathbf { Q } } _ { \ell } )$is unipotent. One considers the local system$\mathrm { R } ^ { i } f _ { \ast } \bar { \mathbf { Q } } _ { \ell }$on$\mathrm { C } \setminus \{ x \} . \ \mathrm { { B y } }$the Weil conjectures, this sheaf is pure of weight i. From the formalism of L-functions for sheaves over curves, one deduces semicontinuity ofweights, which in this situation means that on the invariants${ \mathrm { V } } ^ { \mathrm { I } _ { k } }$of$\mathrm { V } = \mathrm { H } ^ { i } ( \mathrm { X } _ { \bar { k } } , \bar { \mathbf { Q } } _ { \ell } )$, all occurring weights are$\leq i .$. A similar property holds true for all tensor powers of${ \mathrm { V } } ,$and for all tensor powers of the dual$\mathrm { V } ^ { \vee }$ Then one applies the following lemma from linear algebra, which applies for all local fields k.

Lemma 9.5. — Let V be an -adic representation$o f \mathrm { G } _ { k } .$, on which$\mathrm { I } _ { k }$acts unipotently. Then $\mathrm { g r } _ { j } ^ { \mathrm { N } } \mathrm { V }$is pure ofweight$i + j .$for$a l l j \in \mathbf { Z }$ifand only iffor all$j \geq 0$, all weights on$( \mathrm { V } ^ { \otimes j } ) ^ { \mathrm { I } _ { k } }$are at most$i j ,$, and all weights on$( ( \nabla ^ { \vee } ) ^ { \otimes j } ) ^ { \mathrm { I } _ { k } }$are at most$- i j$

Our main theorem is the following.

Theorem 9.6. — Let k be a localfield ofcharacteristic 0. Let Y be a geometrically connected proper smooth variety over k such that Y is a set-theoretic complete intersection in a projective smooth toric variety$\mathrm { X } _ { \Sigma }$. Then the weight-monodromy conjecture is truefor Y.

Proof. — Let$\varpi \in k$be a uniformizer, and let K be the completion of$k ( \varpi ^ { 1 / p ^ { \infty } } )$; then K is perfectoid. Note that after restricting to the action ofthe absolute Galois group of K, one can still see whether the weight-monodromy conjecture is true. Indeed, the extension is totally ramified, so that there are still geometric Frobenii giving the weight decomposition, and the extension is pro-p, so that one still sees the action of the pro--inertia subgroup. Let$\mathrm { K } ^ { \flat }$be its tilt. Then$\mathrm { K } ^ { \flat }$is the completed perfection of$k ^ { \prime } = \mathbf { F } _ { q } ( ( t ) )$, where $t = \varpi ^ { \flat }$. This gives an isomorphism between the absolute Galois groups of K and$k ^ { \prime }$. The notion of weights and the monodromy operator N is compatible with this isomorphism of Galois groups.

By Theorem$3 . 6 ( \mathrm { a } )$of [21], there is some open neighborhood$\tilde { \mathrm { Y } }$of$\mathrm { Y _ { K } ^ { a d } }$in${ \mathrm { X } } _ { \Sigma , \mathrm { K } } ^ { \mathrm { a d } }$ such that$\tilde { \mathrm { Y } } _ { \mathbf { c } _ { \boldsymbol { \phi } } }$and$\mathrm { Y } _ { \mathbf { C } _ { \hbar } } ^ { \mathrm { a d } }$have the same$\mathbf { Z } / \ell \mathbf { Z } .$-cohomology. By induction, they have the same$\mathbf { Z } / \ell ^ { m } \mathbf { Z } \cdot$-cohomology for all$m \geq 1$. Also recall the following comparison theorem.

Theorem 9.7 ([22, Theorem$3 . 8 . I J . - L e t \mathrm { X }$be an algebraic variety over an algebraically closed nonarchimedeanfield k, with associated adic space$\mathrm { X ^ { a d } }$. Then

$$
\mathrm{H} ^ {i} \left(\mathrm{X} _ {\text { ét }}, \mathbf {Z} / \ell^ {m} \mathbf {Z}\right) \cong \mathrm{H} ^ {i} \left(\mathrm{X} _ {\text { ét }} ^ {\text { ad }}, \mathbf {Z} / \ell^ {m} \mathbf {Z}\right).
$$

$\mathrm { B y }$Corollary 8.8, there is some closed subvariety$\mathrm { ~ Z ~ } \subset \mathrm { X } _ { \Sigma , \mathrm { K } ^ { \flat } }$such that${ \cal Z } ^ { \mathrm { a d } } \subset$ $\pi ^ { - 1 } ( \tilde { \mathrm { Y } } )$and dim$\mathrm { Z } = \mathrm { d i m } \mathrm { Y }$. Moreover, we can assume that Z is defined over a global field and geometrically irreducible. Let$Z ^ { \prime }$be a projective smooth alteration of Z. We get a commutative diagram of étale topoi of adic spaces

![](images/page_65_image_1.jpg)

There is a canonical action of the absolute Galois group$\mathrm { G } = \mathrm { G } _ { \mathrm { K } } = \mathrm { G } _ { \mathrm { K } ^ { \flat } }$on this diagram such that all morphisms are G-equivariant. Using the comparison theorem, this induces a G-equivariant map

$$
f ^ {*}: \mathrm{H} ^ {i} \big (\mathrm{Y} _ {\mathbf {c} _ {p}, \acute {\mathrm{et}}}, \mathbf {Z} / \ell^ {m} \mathbf {Z} \big) = \mathrm{H} ^ {i} \big (\tilde {\mathrm{Y}} _ {\mathbf {c} _ {p}, \acute {\mathrm{et}}}, \mathbf {Z} / \ell^ {m} \mathbf {Z} \big) \to \mathrm{H} ^ {i} \big (\mathrm{Z} _ {\mathbf {c} _ {p}, \acute {\mathrm{et}}} ^ {\prime}, \mathbf {Z} / \ell^ {m} \mathbf {Z} \big),
$$

compatible with the cup product. In order to check compatibility with the cup product, use the following lemma.

Lemma$9 . 8 . \mathrm { ~ - ~ } L e t f : \mathrm { T } _ { 1 }  \mathrm { T } _ { 2 }$be any morphism of sites. Let A be any ring, and let 0$x \in \mathrm { H } ^ { i } ( \mathrm { T } _ { 2 } , \mathrm { A } ) , \beta \in \mathrm { H } ^ { j } ( \mathrm { T } _ { 2 } , \mathrm { A } )$. Then

$$
\left(f ^ {*} \alpha\right) \cup \left(f ^ {*} \beta\right) = f ^ {*} (\alpha \cup \beta) \in \mathrm{H} ^ {i + j} \left(\mathrm{T} _ {1}, \mathrm{A}\right).
$$

Proof. — Note thatf induces a functor between the derived categories ofsheaves of A-modules on$\mathrm { T _ { 2 } }$and$\mathrm { T } _ { 1 }$. Interpreting α as a morphism$\mathrm { A } \to \mathrm { A } [ i ]$and$\beta$as a morphism $\mathrm { A } [ i ]  \mathrm { A } [ i + j ]$, the cup product corresponds to composition of morphisms.$\operatorname { A s } f$is a functor, we get the conclusion.-

Note that for the map from$\mathrm { Y } _ { \mathbf { C } _ { \boldsymbol { \rho } , \mathrm { e t } } } ^ { \mathrm { a d } }$to$\tilde { \mathrm { Y } } _ { \mathbf { c } _ { p } , \mathrm { e t } } ,$, the functor goes the other way, and a priori one knows compatibility of the cup product in the other direction. However, as the map on cohomology is an isomorphism, one can also go the other way.

Formally taking the inverse limit and tensoring with$\bar { \bf Q } _ { \ell }$, it follows that we get a G-equivariant map

$$
\mathrm{H} ^ {i} (\mathrm{Y} _ {\mathbf {c} _ {p}, \acute {\mathrm{et}}}, \bar {\mathbf {Q}} _ {\ell}) \to \mathrm{H} ^ {i} \big (\mathrm{Z} _ {\mathbf {c} _ {p} ^ {\flat}, \acute {\mathrm{et}}} ^ {\prime}, \bar {\mathbf {Q}} _ {\ell} \big).
$$

Lemma 9.9. — For$i = 2$dim${ \mathrm { Y } } ,$this is an isomorphism.

Proof. — For all m, we have a commutative diagram

$$
\begin{array}{c c} \mathrm{H} ^ {2   \dim Y} (\mathrm{X} _ {\Sigma , \mathbf {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}}, \mathbf {Z} / \ell^ {m} \mathbf {Z}) \xleftarrow {\cong} & \mathrm{H} ^ {2   \dim Y} (\mathrm{X} _ {\Sigma , \mathbf {C} _ {p}, \acute {\mathrm{et}}}, \mathbf {Z} / \ell^ {m} \mathbf {Z}) \\ \Big \downarrow & \Big \downarrow \\ \mathrm{H} ^ {2   \dim Y} (\pi^ {- 1} (\tilde {\mathrm{Y}}) _ {\mathbf {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}}, \mathbf {Z} / \ell^ {m} \mathbf {Z}) \xleftarrow {} & \mathrm{H} ^ {2   \dim Y} (\tilde {\mathrm{Y}} _ {\mathbf {C} _ {p}, \acute {\mathrm{et}}}, \mathbf {Z} / \ell^ {m} \mathbf {Z}) \\ \Big \downarrow & \Big \downarrow \cong \\ \mathrm{H} ^ {2   \dim Y} (\mathrm{Z} _ {\mathbf {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}} ^ {\prime}, \mathbf {Z} / \ell^ {m} \mathbf {Z}) & \mathrm{H} ^ {2   \dim Y} (\mathrm{Y} _ {\mathbf {C} _ {p}, \acute {\mathrm{et}}}, \mathbf {Z} / \ell^ {m} \mathbf {Z}) \end{array}
$$

The isomorphism in the top row is from Proposition 8.6. We can pass to the inverse limit over m and tensor with$\bar { \mathbf { Q } } _ { \ell }$. If

$$
\mathrm{H} ^ {2 \dim \mathrm{Y}} (\mathrm{Y} _ {\mathbf {c} _ {p}, \acute {\mathrm{et}}}, \bar {\mathbf {Q}} _ {\ell}) \to \mathrm{H} ^ {2 \dim \mathrm{Y}} \big (\mathrm{Z} _ {\mathbf {c} _ {p}, \acute {\mathrm{et}}} ^ {\prime}, \bar {\mathbf {Q}} _ {\ell} \big).
$$

is not an isomorphism, it is the zero map, and hence the diagram implies that the restriction map

$$
\mathrm{H} ^ {2 \dim \mathrm{Y}} (\mathrm{X} _ {\Sigma , \mathbf {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}}, \bar {\mathbf {Q}} _ {\ell}) \to \mathrm{H} ^ {2 \dim \mathrm{Y}} \big (Z _ {\mathbf {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}} ^ {\prime}, \bar {\mathbf {Q}} _ {\ell} \big)
$$

is the zero map as well. But the dim Y-th power of the first Chern class of an ample line bundle on$\mathrm { X } _ { \Sigma , \mathbf { C } _ { \boldsymbol { \mu } } ^ { \flat } }$will have nonzero image in$\mathrm { H } ^ { 2 \mathrm { d i m Y } } ( \mathrm { Z } _ { \mathbf { c } _ { p } ^ { \flat } , \vec { \mathrm { e t } } } ^ { \prime } , \bar { \mathbf { Q } } _ { \ell } )$-

Now Poincaré duality implies that$\mathrm { H } ^ { i } ( \mathrm { Y } _ { \mathbf { C } _ { p } , \mathrm { \bar { e t } } } , \bar { \mathbf { Q } } _ { \ell } )$is a direct summand of$\mathrm { H } ^ { i } ( Z _ { \mathbf { c } _ { \rho } ^ { \flat } , \vec { \operatorname { e t } } } ^ { \prime } ,$ $\bar { \bf Q } _ { \ell } )$. By Deligne’s theorem, H$( Z _ { \mathbf { c } _ { p } ^ { \flat } , \flat } ^ { \prime } , \bar { \mathbf { Q } } _ { \ell } )$satisfies the weight-monodromy conjecture, and hence so does its direct summand$\mathrm { H } ^ { i } ( \mathrm { Y } _ { \mathbf { C } _ { p } , \mathrm { \bar { e t } } } , \bar { \mathbf { Q } } _ { \ell } )$-

## Acknowledgements

First, I want to express my deep gratitude to my advisor M. Rapoport, who suggested that I should think about the weight-monodromy conjecture, and in particular suggested that it might be possible to reduce it to the case of equal characteristic after a highly ramified base change. Next, I want to thank Gerd Faltings for a crucial remark on a first version ofthis paper. Moreover, I wish to thank all participants ofthe ARGOS seminar on perfectoid spaces at the University ofBonn in the summer term 2011, for working through an early version of this manuscript and the large number of suggestions for improvements. The same applies to Lorenzo Ramero, whom I also want to thank for his very careful reading of the manuscript. Moreover, I thank Roland Huber for answering my questions on adic spaces. Further thanks go to Ahmed Abbes, Bhargav Bhatt, Pierre Colmez, Laurent Fargues, Jean-Marc Fontaine, Ofer Gabber, Luc Illusie, Adrian Iovita, Kiran Kedlaya, Gerard Laumon, Ruochuan Liu, Wieslawa Niziol, Arthur Ogus, Martin Olsson, Bernd Sturmfels and Jared Weinstein for helpful discussions. Finally, I want to heartily thank the organizers of the CAGA lecture series at the IHES for their invitation. This work is the author’s PhD thesis at the University of Bonn, which was supported by the Hausdorff Center for Mathematics, and the thesis was finished while the author was a Clay Research Fellow. He wants to thank both institutions for their support. Moreover, parts of it were written while visiting Harvard University, the Université Paris-Sud at Orsay, and the IHES, and the author wants to thank these institutions for their hospitality.

## REFERENCES

1. V. G. BERKOVICH, Spectral Theory and Analytic Geometry Over Non-Archimedean Fields, Mathematical Surveys and Monographs, vol. 33, Am. Math. Soc., Providence, 1990.

2. S. BOSCH, U. GÜNTZER, and R. REMMERT, Non-Archimedean Analysis, Grundlehren der Mathematischen Wissenschaften, vol. 261, Springer, Berlin, 1984. A systematic approach to rigid analytic geometry.

3. S. BOSCH and W. LÜTKEBOHMERT, Formal rigid geometry. I. Rigid spaces, Math. Ann., 295 (1993), 291–317.

4. P. BOYER, Monodromie du faisceau pervers des cycles évanescents de quelques variétés de Shimura simples, Invent. Math., 177 (2009), 239–280.

5. P. BOYER, Conjecture de monodromie-poids pour quelques variétés de Shimura unitaires, Compos. Math., 146 (2010), 367–403.

6. A. CARAIANI, Local-global compatibility and the action of monodromy on nearby cycles, Duke Math. J., to appear, arXiv:1010.2188.

7. J.-F. DAT, Théorie de Lubin-Tate non-abélienne et représentations elliptiques, Invent. Math., 169 (2007), 75–152.

8. A.J. deJ<sub>ONG</sub>, Smoothness, semi-stability and alterations, Inst. Hautes Études Sci. Publ. Math., 83 (1996), 51–93.

9. P. D , Théorie de Hodge. I, in Actes du Congrès International des Mathématiciens (Nice, 1970), Tome 1, pp. 425–430, Gauthier-Villars, Paris, 1971.

10. P. D<sub>ELIGNE</sub>, La conjecture de Weil. II, Inst. Hautes Études Sci. Publ. Math., 52 (1980), 137–252.

11. G. FALTINGS, p-adic Hodge theory, J. Amer. Math. Soc., 1 (1988), 255–299.

12. G. FALTINGS, Cohomologies p-adiques et applications arithmétiques, II, in Almost étale extensions. Astérisque, vol. 279, pp. 185–270, 2002.

13. J.-M. F and J.-P. W , Extensions algébrique et corps des normes des extensions APF des corps locaux, C. R. Acad, Sci, Paris Sér, A-B. 288 (1979), A441−A444

14. O. GABBER and L. RAMERO, Foundations of almost ring theory, http://math.univ-lille1.fr/\~ramero/hodge.pdf.

15. O. GABBER and L. RAMERO, Almost Ring Theory, Lecture Notes in Mathematics, vol. 1800, Springer, Berlin, 2003.

16. M. HARRIS and R. TAYLOR, The Geometry and Cohomology ofsome Simple Shimura Varieties, Annals of Mathematics Studies, vol. 151, Princeton University Press, Princeton, 2001. With an appendix by Vladimir G. Berkovich.

17. E. HELLMANN, On arithmetic families of filtered ϕ-modules and crystalline representations, arXiv:1010.4577, 2011.

18. M. H , Prime ideal structure in commutative rings, Trans. Amer. Math. Soc., 142 (1969), 43–60.

19. R. HUBER, Continuous valuations, Math. Z., 212 (1993), 455–477.

20. R. HUBER, A generalization of formal schemes and rigid analytic varieties, Math. Z., 217 (1994), 513–551.

21. R. HUBER, A finiteness result for direct image sheaves on the étale site of rigid analytic varieties, J. Algebraic Geom., 7 (1998), 359–403.

22. R. H<sub>UBER</sub>, Étale cohomology of rigid analytic varieties and adic spaces, Aspects of Mathematics, vol. E30, Vieweg, Braunschweig, 1996.

23. L. ILLUSIE, Complexe cotangent et déformations. I, Lecture Notes in Mathematics, vol. 239, Springer, Berlin, 1971.

24. L. ILLUSIE, Complexe cotangent et déformations. II, Lecture Notes in Mathematics, vol. 283, Springer, Berlin, 1972.

25. L. ILLUSIE, Autour du théorème de monodromie locale, in Périodes p-adiques. Astérisque, vol. 223, pp. 9–57, 1994.

26. T. ITO, Weight-monodromy conjecture for p-adically uniformized varieties, Invent. Math., 159 (2005), 607–656.

27. T. ITO, Weight-monodromy conjecture over equal characteristic local fields, Amer. J. Math., 127 (2005), 647–658.

28. K. KEDLAYA and R. LIU, Relative p-adic Hodge theory, I: Foundations, http://math.mit.edu/\~kedlaya/papers/relative-padic-Hodge1.pdf.

29. D. QUILLEN, On the (co-) homology ofcommutative rings, in Applications ofCategoricalAlgebra, Proc. Sympos. Pure Math, vol. XVII, pp. 65–87, Am. Math. Soc., Providence, 1970.

30. M. RAPOPORT and Th. ZINK, Über die lokale Zetafunktion von Shimuravarietäten. Monodromiefiltration und verschwindende Zyklen in ungleicher Charakteristik, Invent. Math., 68 (1982), 21–101.

31. P. SCHOLZE, p-adic Hodge theory for rigid-analytic varieties, arXiv:1205.3463, 2012.

32. S. W. SHIN, Galois representations arising from some compact Shimura varieties, Ann. ofMath. (2), 173 (2011), 1645–1741.

33. J. T , Rigid analytic spaces, Invent. Math., 12 (1971), 257–289.

34. R. TAYLOR and T. YOSHIDA, Compatibility oflocal and global Langlands correspondences,J. Amer. Math. Soc., 20 (2007), 467–493.

35. T. TERASOMA, Monodromy weight filtration is independent of , arXiv:math/9802051, 1998.

Mathematisches Institut, Universität Bonn, 53115 Bonn, Germany scholze@math.uni-bonn.de

## P. S.

Manuscrit reçu le 11 décembre 2011 Manuscrit accepté le 17juillet 2012 publié en ligne le 10 août 2012.