# PERFECTOID SPACES

## PETER SCHOLZE

Abstract. We introduce a certain class of so-called perfectoid rings and spaces, which give a natural framework for Faltings’ almost purity theorem, and for which there is a natural tilting operation which exchanges characteristic 0 and characteristic p. We deduce the weight-monodromy conjecture in certain cases by reduction to equal characteristic.

## Contents

1. Introduction 2  
2. Adic spaces 7  
3. Perfectoid fields 15  
4. Almost mathematics 18  
5. Perfectoid algebras 21  
6. Perfectoid spaces: Analytic topology 30  
7. Perfectoid spaces: Etale topology 39  
8. An example: Toric varieties 44  
9. The weight-monodromy conjecture 47  
References 50

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Date: November 27, 2024.</span></small>

## 1. Introduction

In commutative algebra and algebraic geometry, some of the most subtle problems arise in the context of mixed characteristic, i.e. over local fields such as$\mathbb { Q } _ { p }$which are of characteristic$0 ,$but whose residue field$\mathbb { F } _ { p }$is of characteristic$p .$. The aim of this paper is to establish a general framework for reducing certain problems about mixed characteristic rings to problems about rings in characteristic$p$. We will use this framework to establish a generalization of Faltings’s almost purity theorem, and new results on Deligne’s weight-monodromy conjecture.

The basic result which we want to put into a larger context is the following canonical isomorphism of Galois groups, due to Fontaine and Wintenberger, [13]. A special case is the following result.

Theorem 1.1. The absolute Galois groups of$\mathbb { Q } _ { p } ( p ^ { 1 / p ^ { \infty } } )$and$\mathbb { F } _ { p } ( ( t ) )$are canonically isomorphic.

In other words, after adjoining all p-power roots of$p$to a mixed characteristic field, it looks like an equal characteristic ring in some way. Let us first explain how one can prove this theorem. Let K be the completion of$\mathbb { Q } _ { p } ( p ^ { 1 / p ^ { \infty } } )$and let$K ^ { \flat }$be the completion of$\mathbb { F } _ { p } ( ( t ) ) ( t ^ { 1 / p ^ { \infty } } )$; it is enough to prove that the absolute Galois groups of$K$and$K ^ { \flat }$are isomorphic. Let us first explain the relation between$K$and$K ^ { \flat }$, which in vague terms consists in replacing the prime number$p$by a formal variable t. Let$K ^ { \circ }$and$K ^ { \flat \circ }$be the subrings of integral elements. Then

$$
K ^ {\circ} / p = \mathbb {Z} _ {p} [ p ^ {1 / p ^ {\infty}} ] / p \cong \mathbb {F} _ {p} [ t ^ {1 / p ^ {\infty}} ] / t = K ^ {\flat \circ} / t ,
$$

where the middle isomorphism sends$p ^ { 1 / p ^ { n } }$to$t ^ { 1 / p ^ { n } }$. Using it, one can define a continuous multiplicative, but nonadditive, map$K ^ { \flat } \to K , x \mapsto x ^ { \sharp }$, which sends t to$p .$. On$K ^ { \flat \circ }$, it is given by sending x to$\scriptstyle \operatorname* { l i m } _ { n \to \infty } y _ { n } ^ { p ^ { n } }$, where$y _ { n } \in K ^ { \circ }$is any lift of the image of$x ^ { 1 / p ^ { n } }$in $K ^ { \flat \circ } / t = K ^ { \circ } / p$. Then one has an identification

$$
K ^ {\flat} = \varprojlim_ {x \mapsto x ^ {p}} K , x \mapsto (x ^ {\sharp}, (x ^ {1 / p}) ^ {\sharp}, \ldots) .
$$

In order to prove the theorem, one has to construct a canonical finite extension$L ^ { \sharp }$of $K$for any finite extension L of$K ^ { \flat }$<sup>[</sup>. There is the following description. Say L is the splitting field of a polynomial$X ^ { d } + a _ { d - 1 } X ^ { d - 1 } + \ldots + a _ { 0 }$, which is also the splitting field of$X ^ { d } + a _ { d - 1 } ^ { 1 / p ^ { n } } X ^ { d - 1 } + . . . + a _ { 0 } ^ { 1 / p ^ { n } }$for all$n \geq 0$. Then$L ^ { \sharp }$can be defined as the splitting field of$X ^ { d } + ( a _ { d - 1 } ^ { 1 / p ^ { n } } ) ^ { \sharp } X ^ { d - 1 } + \ldots + ( a _ { 0 } ^ { 1 / p ^ { n } } ) ^ { \sharp }$for n large enough: these fields stabilize as $n \to \infty$

In fact, the same ideas work in greater generality.

Definition 1.2. A perfectoid field is a complete topological field K whose topology is induced by a nondiscrete valuation of rank 1, such that the Frobenius$\Phi$is surjective on $K ^ { \circ } / p$

Here$K ^ { \circ } \subset K$denotes the set of powerbounded elements. Generalizing the example above, a construction of Fontaine associates to any perfectoid field K another perfectoid field$K ^ { \flat }$of characteristic$p ,$whose underlying multiplicative monoid can be described as

$$
K ^ {\flat} = \varprojlim_ {x \mapsto x ^ {p}} K  .
$$

The theorem above generalizes to the following result.

Theorem 1.3. The absolute Galois groups of K and$K ^ { \flat }$are canonically isomorphic.

Our aim is to generalize this to a comparison of geometric objects over K with geometric objects over$K ^ { \flat }$. The basic claim is the following.

Claim 1.4. The afine line$\mathbb { A } _ { K ^ { \flat } } ^ { 1 }$‘is equal$t o ^ { \prime }$the inverse limit$\underline { { \operatorname* { l i m } } } _ { T \mapsto T ^ { p } } \mathbb { A } _ { K } ^ { 1 }$, where$T$is the coordinate on$\mathbb { A } ^ { 1 }$

One way in which this is correct is the observation that it is true on$K ^ { \flat _ { - } }$, resp.$K \mathfrak { - }$ valued points. Moreover, for any finite extension L of K corresponding to an extension $L ^ { \flat }$of$K ^ { \flat }$, we have the same relation

$$
L^{\flat} = \varprojlim_{\substack{x\mapsto x^{p}}}L  .
$$

Looking at the example above, we see that the explicit description of the map between $\mathbb { A } _ { K ^ { \flat } } ^ { 1 }$and$\underline { { \operatorname* { l i m } } } _ { T \mapsto T ^ { p } } \mathbb { A } _ { K } ^ { 1 }$involves a limit procedure. For this reason, a formalization of this isomorphism has to be of an analytic nature, and we have to use some kind of rigid analytic geometry over$K$. We choose to work with Huber’s language of adic spaces, which reinterprets rigid-analytic varieties as certain locally ringed topological spaces. In particular, any variety X over K has an associated adic space$X ^ { \mathrm { a d } }$over$K$, which in turn has an underlying topological space$| X ^ { \mathrm { a d } } |$

Theorem 1.5. There is a homeomorphism of topological spaces

$$
| (\mathbb {A} _ {K ^ {\flat}} ^ {1}) ^ {\mathrm{ad}} | \cong \varprojlim_ {T \mapsto T ^ {p}} | (\mathbb {A} _ {K} ^ {1}) ^ {\mathrm{ad}} | .
$$

Note that both sides of this isomorphism can be regarded as locally ringed topological spaces. It is natural to ask whether one can compare the structure sheaves on both sides. There is the obvious obstacle that the left-hand side has a sheaf of characteristic p rings, whereas the right-hand side has a sheaf of characteristic 0 rings. Fontaine’s functors make it possible to translate between the two worlds. There is the following result.

Definition 1.6. Let K be a perfectoid field. A perfectoid K-algebra is a Banach$K \cdot$ algebra R such that the set of powerbounded elements$R ^ { \circ } \subset R$is bounded, and such that the Frobenius Φ is surjective on$R ^ { \circ } / p$

Theorem 1.7. There is natural equivalence of categories, called the tilting equivalence, between the category of perfectoid K-algebras and the category of perfectoid$K ^ { \bar { \flat } } .$-algebras. Here a perfectoid K-algebra R is sent to the perfectoid$K ^ { \flat } - a l g e b r a$

$$
R ^ {\flat} = \varprojlim_ {x \mapsto x ^ {p}} R  .
$$

We note in particular that for perfectoid K-algebras$R ,$we still have a map$R ^ { \flat } \to R$ $f \mapsto f ^ { \sharp }$. An example of a perfectoid K-algebra is the algebra$R = K \langle \bar { T } ^ { 1 / p ^ { \infty } } \rangle$for which$R ^ { \circ } = K ^ { \circ } \langle T ^ { 1 / \bar { p } ^ { \infty } } \rangle$is the p-adic completion of$K [ T ^ { 1 / p ^ { \infty } } ]$. This is the completion of an algebra that appears on the right-hand side of Theorem 1.5. Its tilt is given by $R ^ { \flat } = K ^ { \tilde { \flat } } \langle T ^ { 1 / p ^ { \infty } } \rangle$, which is the completed perfection of an algebra that appears on the left-hand side of Theorem 1.5.

Now an afinoid perfectoid space is associated to a perfectoid afinoid K-algebra, which is a pair$( R , R ^ { + } )$, where R is a perfectoid K-algebra, and$R ^ { + } \subset R ^ { \circ }$is open and integrally closed (and often$R ^ { + } = R ^ { \circ } )$. There is a natural way to form the tilt$( R ^ { \flat } , R ^ { \flat + } )$. To such a pair$( R , R ^ { + } )$, Huber, [18], associates a space$X = \operatorname { S p a } ( R , R ^ { + } )$of equivalence classes of continuous valuations$R \to \Gamma \cup \{ 0 \} , f \mapsto | f ( x ) |$, which are$\leq 1$on$R ^ { + }$. The topology on this space is generated by so-called rational subsets. Moreover, Huber defines presheaves ${ \mathcal { O } } _ { X }$and${ \mathcal { O } } _ { X } ^ { + }$on X, whose global sections are R, resp.$R ^ { + }$

Theorem 1.8. Let$( R , R ^ { + } )$be a perfectoid afinoid K-algebra, and let$X = \operatorname { S p a } ( R , R ^ { + } )$ $X ^ { \flat } = \operatorname { S p a } ( R ^ { \flat } , R ^ { \flat + } )$

(i) There is a homeomorphism$X \cong X ^ { \flat }$, given by mapping x$\in X$to the valuation$x ^ { \flat } \in X ^ { \flat }$ defined by$| f ( x ^ { \flat } ) | = | f ^ { \sharp } ( x ) |$. This homeomorphism identifies rational subsets.

(ii) For any rational subset$U \subset X$with tilt$U ^ { \flat } \subset X ^ { \flat }$, the pair$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is a perfectoid afinoid K-algebra with tilt$( { \mathcal { O } } _ { X ^ { \flat } } ( U ^ { \flat } ) , { \mathcal { O } } _ { X ^ { \flat } } ^ { + } ( U ^ { \flat } ) )$

(iii) The presheaves${ \mathcal { O } } _ { X } , { \mathcal { O } } _ { X } ^ { + }$are sheaves.

(iv) The cohomology group$H ^ { i } ( X , { \mathcal { O } } _ { X } ^ { + } )$is m-torsion for$i > 0$

Here m$\subset \ K ^ { \circ }$is the subset of topologically nilpotent elements. Part (iv) implies that$H ^ { i } ( X , { \mathcal { O } } _ { X } ) = 0$for$i > 0$, which gives Tate’s acyclicity theorem in the context of perfectoid spaces. However, it says that this statement about the generic fibre extends almost to the integral level, in the language of Faltings’s so-called almost mathematics. In fact, this is a general property of perfectoid objects: Many statements that are true on the generic fibre are automatically almost true on the integral level.

Using the theorem, one can define general perfectoid spaces by gluing afinoid perfectoid spaces$X = \operatorname { S p a } ( R , R ^ { + } )$. We arrive at the following theorem.

Theorem 1.9. The category of perfectoid spaces over K and the category of perfectoid spaces over$K ^ { \flat }$<sup>[</sup> are equivalent.

We denote the tilting functor by$X \mapsto X ^ { \flat }$. Our next aim is to define an ´etale topos of perfectoid spaces. This necessitates a generalization of Faltings’s almost purity theorem, cf. [11], [12].

Theorem 1.10. Let R be a perfectoid K-algebra. Let$S / R$be finite ´etale. Then$S$is a perfectoid K-algebra, and$S ^ { \circ }$is almost finite ´etale over$R ^ { \circ }$

In fact, as for perfectoid fields, it is easy to construct a fully faithful functor from the category of finite ´etale$R ^ { \flat } \mathrm { - a l g e b r a s }$to finite ´etale R-algebras, and the problem becomes to show that this functor is essentially surjective. But locally on$X = \operatorname { S p a } ( R , R ^ { + } )$), the functor is essentially surjective by the result for perfectoid fields; one deduces the general case by a gluing argument.

Using this theorem, one proves the following theorem. Here,$X _ { \mathrm { e t } }$denotes the ´etale site of a perfectoid space$X ,$, and we denote by$X _ { \mathrm { e t } } ^ { \sim }$the associated topos.

Theorem 1.11. Let X be a perfectoid space over K with tilt$X ^ { \flat }$over$K ^ { \flat }$<sup>[</sup>. Then tilting induces an equivalence of sites$X _ { \mathrm { e t } } \cong X _ { \mathrm { e t } } ^ { \flat }$

As a concrete application of this theorem, we have the following result. Here, we use the ´etale topoi of adic spaces, which are the same as the ´etale topoi of the corresponding rigid-analytic variety. In particular, the same theorem holds for rigid-analytic varieties.

Theorem 1.12. The ´etale topos$( \mathbb { P } _ { K ^ { \flat } } ^ { n , \mathrm { a d } } ) _ { \tilde { \mathrm { e t } } } ^ { \sim }$is equivalent to the inverse limit$\varprojlim _ { \varphi } ( \mathbb { P } _ { K } ^ { n , \mathrm { a d } } ) _ { \tilde { \mathrm { e t } } }$

Here, one has to interpret the latter as the inverse limit of a fibred topos in an obvious way, and$\varphi$is the map given on coordinates by$\varphi ( x _ { 0 } : \ldots : x _ { n } ) = ( x _ { 0 } ^ { p } : \ldots : x _ { n } ^ { p } )$. The same theorem stays true for proper toric varieties without change. We note that the theorem$\mathrm { g i }$ves rise to a projection map

$$
\pi : \mathbb {P} _ {K ^ {\flat}} ^ {n} \to \mathbb {P} _ {K} ^ {n}
$$

defined on topological spaces and ´etale topoi of adic spaces, and which is given on coordinates by$\pi ( x _ { 0 } : \ldots : x _ { n } ) = ( x _ { 0 } ^ { \sharp } : \ldots : x _ { n } ^ { \sharp } )$. In particular, we see again that this isomorphism is of a deeply analytic and transcendental nature.

We note that$( \mathbb { P } _ { K ^ { \flat } } ^ { n } ) ^ { \mathrm { a d } }$is itself not a perfectoid space, but$\varprojlim _ { \varphi } ( \mathbb { P } _ { K ^ { \flat } } ^ { n } ) ^ { \mathrm { a d } }$is, where$\varphi :$ $\mathbb { P } _ { K ^ { \flat } } ^ { n } \to \mathbb { P } _ { K ^ { \flat } } ^ { n }$denotes again the$p { \mathrm { - t h } }$power map on coordinates. However,$\varphi$is purely inseparable and hence induces an isomorphism on topological spaces and ´etale topoi, which is the reason that we have not written this inverse limit in Theorem 1.5 and Theorem 1.12.

Finally, we apply these results to the weight-monodromy conjecture. Let us recall its formulation. Let k be a local field whose residue field is of characteristic$p ,$let$G _ { k }$= $\operatorname { G a l } ( { \bar { k } } / k )$, and let$q$be the cardinality of the residue field of k. For any finite-dimensional Q<sup>¯</sup> <sub>\`</sub>-representation V of$G _ { k } .$, we have the monodromy operator$N : V \to V ( - 1 )$induced from the action of the \`-adic inertia subgroup. It induces the monodromy filtration $\operatorname { F i l } _ { i } ^ { N } V \subset V , i \in \mathbb { Z }$, characterized by the property that$N ( \mathrm { F i l } _ { i } ^ { N } V ) \subset \mathrm { F i l } _ { i - 2 } ^ { N } V \bar { ( - 1 ) }$) for all $i \in \mathbb { Z }$and$\mathrm { g r } _ { i } ^ { N } V \cong \mathrm { g r } _ { - i } ^ { N } V ( - i )$via$N ^ { i }$for all$i \geq 0$

Conjecture 1.13 (Deligne, [9]). Let X be a proper smooth variety over$k ,$and let $V = H ^ { i } ( X _ { \bar { k } } , \bar { \mathbb { Q } } _ { \ell } )$. Then for all$j \in \mathbb Z$and for any geometric Frobenius$\Phi \in G _ { k }$, all eigenvalues of Φ on$\mathrm { g r } _ { j } ^ { N } \dot { V }$are Weil numbers of weight$i + j , \ i . e$. algebraic numbers α such that$| \alpha | = q ^ { ( i + j ) / 2 }$for all complex absolute values.

Deligne, [10], proved this conjecture if$k$is of characteristic$p ,$and the situation is already defined over a curve. The general weight-monodromy conjecture over fields k of characteristic$p$can be deduced from this case, as done by Terasoma, [33], and by Ito, [26].

In mixed characteristic, the conjecture is wide open. Introducing what is now called the Rapoport-Zink spectral sequence, Rapoport and Zink, [29], have proved the conjecture when X has dimension at most 2 and X has semistable reduction. They also show that in general it would follow from a suitable form of the standard conjectures, the main point being that a certain linear pairing on cohomology groups should be nondegenerate. Using de Jong’s alterations, [8], one can reduce the general case to the case of semistable reduction, and in particular the case of dimension at most 2 follows. Apart from that, other special cases are known. Notably, the case of varieties which admit p-adic uniformization by Drinfeld’s upper half-space is proved by Ito, [25], by pushing through the argument of Rapoport-Zink in this special case, making use of the specia nature of the components of the special fibre, which are explicit rational varieties.

On the other hand, there is a large amount of activity that uses automorphic arguments to prove results in cases of certain Shimura varieties, notably those of type $U ( 1 , n - 1 )$used in the book of Harris-Taylor [15]. Let us only mention the work of Taylor and Yoshida, [32], later completed by Shin, [30], and Caraiani, [6], as well as the independent work of Boyer, [4], [5]. Boyer’s results were used by Dat, [7], to handle the case of varieties which admit uniformization by a covering of Drinfeld’s upper half-space, thereby generalizing Ito’s result.

Our last main theorem is the following.

Theorem 1.14. Let k be a local field of characteristic 0. Let X be a geometrically connected proper smooth variety over k such that X is a set-theoretic complete intersection in a projective smooth toric variety. Then the weight-monodromy conjecture is true for $X$

Let us give a short sketch of the proof for a smooth hypersurface in$X \subset \mathbb { P } ^ { n }$, which is already a new result. We have the projection

$$
\pi : \mathbb {P} _ {K ^ {\flat}} ^ {n} \to \mathbb {P} _ {K} ^ {n},
$$

and we can look at the preimage$\pi ^ { - 1 } ( X )$. One has an injective map$H ^ { i } ( X ) \to H ^ { i } ( \pi ^ { - 1 } ( X ) )$ and if$\pi ^ { - 1 } ( X )$were an algebraic variety, then one could deduce the result from Deligne’s theorem in equal characteristic. However, the map$\pi$is highly transcendental, and $\pi ^ { - 1 } ( X )$will not be given by equations. In general, it will look like some sort of fractal, have infinite-dimensional cohomology, and will have infinite degree in the sense that it will meet a line in infinitely many points. As an easy example, let

$$
X = \{x _ {0} + x _ {1} + x _ {2} = 0 \} \subset (\mathbb {P} _ {K} ^ {2}) ^ {\mathrm{ad}}.
$$

Then the homeomorphism

$$
| (\mathbb {P} _ {K ^ {\flat}} ^ {2}) ^ {\mathrm{ad}} | \cong \varprojlim_ {\varphi} | (\mathbb {P} _ {K} ^ {2}) ^ {\mathrm{ad}} |
$$

means that$\pi ^ { - 1 } ( X )$is topologically the inverse limit of the subvarieties

$$
X _ {n} = \{x _ {0} ^ {p ^ {n}} + x _ {1} ^ {p ^ {n}} + x _ {2} ^ {p ^ {n}} = 0 \} \subset (\mathbb {P} _ {K} ^ {2}) ^ {\mathrm{ad}}.
$$

However, we have the following crucial approximation lemma.

Lemma 1.15. Let$\tilde { X } \subset ( \mathbb { P } _ { K } ^ { n } ) ^ { \mathrm { a d } }$be a small open neighborhood of the hypersurface$X$ Then there is a hypersurface${ \overset { \cdot } { Y } } \subset \pi ^ { - 1 } ( { \overset { \cdot } { X } } )$

The proof of this lemma is by an explicit approximation algorithm for the homogeneous polynomial defining X, and is the reason that we have to restrict to complete intersections. Using a result of Huber, one finds some$\tilde { X }$such that$H ^ { i } ( X ) = H ^ { i } ( \tilde { X } )$, and hence gets a map$H ^ { i } ( X ) = H ^ { i } ( \tilde { X } )  H ^ { i } ( Y )$. As before, one checks that it is injective and concludes.

After the results of this paper were first announced, Kiran Kedlaya informed us that he had obtained related results in joint work with Ruochuan Liu, [27]. In particular, in our terminology, they prove that for any perfectoid K-algebra R with tilt$R ^ { \flat }$, there is an equivalence between the finite ´etale R-algebras and the finite ´etale$R ^ { \flat } .$-algebras. However, the tilting equivalence, the generalization of Faltings’s almost purity theorem and the application to the weight-monodromy conjecture were not observed by them. This led to an exchange of ideas, with the following two influences on this paper. In the first version of this work, Theorem 1.3 was proved using a version of Faltings’s almost purity theorem for fields, proved in [14], Chapter 6, using ramification theory. Kedlaya observed that one could instead reduce to the case where$K ^ { \flat }$is algebraically closed, which gives a more elementary proof of the theorem. We include both arguments here. Secondly, a certain finiteness condition on the perfectoid K-algebra was imposed at some places in the first version, a condition close to the notion of$\mathrm { p - }$finiteness introduced below; in most applications known to the author, this condition is satisfied. Kedlaya made us aware of the possibility to deduce the general case by a simple limit argument.

Acknowledgments. First, I want to express my deep gratitude to my advisor M. Rapoport, who suggested that I should think about the weight-monodromy conjecture, and in particular suggested that it might be possible to reduce it to the case of equal characteristic after a highly ramified base change. Next, I want to thank Gerd Faltings for a crucial remark on a first version of this paper. Moreover, I wish to thank all participants of the ARGOS seminar on perfectoid spaces at the University of Bonn in the summer term 2011, for working through an early version of this manuscript and the large number of suggestions for improvements. The same applies to Lorenzo Ramero, whom I also want to thank for his very careful reading of the manuscript. Moreover, I thank Roland Huber for answering my questions on adic spaces. Further thanks go to Ahmed Abbes, Bhargav Bhatt, Pierre Colmez, Laurent Fargues, Jean-Marc Fontaine, Ofer Gabber, Luc Illusie, Adrian Iovita, Kiran Kedlaya, Gerard Laumon, Ruochuan Liu, Wieslawa Niziol, Arthur Ogus, Martin Olsson, Bernd Sturmfels and Jared Weinstein for helpful discussions. Finally, I want to heartily thank the organizers of the CAGA lecture series at the IHES for their invitation. This work is the author’s PhD thesis at the University of Bonn, which was supported by the Hausdorf Center for Mathematics, and the thesis was finished while the author was a Clay Research Fellow. He wants to thank both institutions for their support. Moreover, parts of it were written while visiting Harvard University, the Universit´e Paris-Sud at Orsay, and the IHES, and the author wants to thank these institutions for their hospitality.

## 2. Adic spaces

Throughout this paper, we make use of Huber’s theory of adic spaces. For this reason, we recall some basic definitions and statements about adic spaces over nonarchimedean local fields. We also compare Huber’s theory to the more classical language of rigid analytic geometry, and to the theory of Berkovich’s analytic spaces. The material of this section can be found in [20], [19] and [18].

Definition 2.1. A nonarchimedean field is a topological field k whose topology is induced by a nontrivial valuation of rank 1.

In particular, k admits a norm$| \cdot | : k \to { \mathbb { R } } _ { \geq 0 } .$, and it is easy to see that$| \cdot |$is unique up to automorphisms$x \mapsto x ^ { \alpha } , 0 < \alpha < \infty$, of$\mathbb { R } _ { \geq 0 }$

Throughout, we fix a nonarchimedean field k. Replacing k by its completion will not change the theory, so we may and do assume that$k$is complete.

The idea of rigid-analytic geometry, and the closely related theories of Berkovich’s analytic spaces and Huber’s adic spaces, is to have a nonarchimedean analogue of the notion of complex analytic spaces over C. In particular, there should be a functor

$$
\left\{\text {varieties} / k \right\}\rightarrow \left\{\text {adic spaces} / k \right\}: X \mapsto X ^ {\mathrm{ad}},
$$

sending any variety over$k$to its analytification$X ^ { \mathrm { a d } }$. Moreover, it should be possible to define subspaces of$X ^ { \mathrm { a d } }$by inequalities: For any$f \in \Gamma ( X , { \mathcal { O } } _ { X } )$, the subset

$$
\{x \in X ^ {\mathrm{ad}} \mid | f (x) | \leq 1 \}
$$

should make sense. In particular, any point$x \in X ^ { \mathrm { a d } }$should give rise to a valuation function$f \mapsto | f ( x ) |$. In classical rigid-analytic geometry, one considers only the maximal points of the scheme$X .$. Each of them gives a map$\Gamma ( X , { \mathcal { O } } _ { X } ) \to k ^ { \prime }$for some finite extension$k ^ { \prime }$of$k ;$composing with the unique extension of the absolute value of k to$k ^ { \prime }$gives a valuation on$\Gamma ( X , { \mathcal { O } } _ { X } )$. In Berkovich’s theory, one considers norm maps $\Gamma ( X , { \mathcal { O } } _ { X } ) \to \mathbb { R } _ { \geq 0 }$inducing a fixed norm map on$k .$Equivalently, one considers valuations of rank 1 on$\Gamma ( X , { \mathcal { O } } _ { X } )$. In Huber’s theory, one allows also valuations of higher rank.

Definition 2.2. Let R be some ring. A valuation on R is given by a multiplicative map $| \cdot | : R  \Gamma \cup \{ 0 \}$, where Γ is some totally ordered abelian group, written multiplicatively, such that$| 0 | = 0 , | 1 | = 1$and$| x + y | \leq \operatorname* { m a x } ( | x | , | y | )$for all$x , y \in R$

If R is a topological ring, then a valuation | · | on R is said to be continuous if for all $\gamma \in \Gamma$, the subset$\{ x \in R \mid | x | < \gamma \} \subset R$is open.

Remark 2.3. The term valuation is somewhat unfortunate: If$\Gamma = \mathbb { R } _ { > 0 } .$, then this would usually be called a seminorm, and the term valuation would be used for (a constant multiple of) the map$x \mapsto - \log | x |$. On the other hand, the term higher-rank norm is much less commonly used than the term higher-rank valuation. For this reason, we stick with Huber’s terminology.

Remark 2.4. Recall that a valuation ring is an integral domain R such that for any x$\neq 0$ in the fraction field K of$R ,$at least one of x and$x ^ { - 1 }$is in R. Any valuation$| \cdot |$on a field K gives rise to the valuation subring$R = \{ x \mid | x | \leq 1 \}$Conversely, a valuation ring R gives rise to a valuation on$K$with values in$\Gamma = \dot { K } ^ { \times } / R ^ { \times }$, ordered by saying that$x \leq y { \mathrm { ~ i f ~ } } x = y z$for some$z \in R$. With respect to a suitable notion of equivalence of valuations defined below, this induces a bijective correspondence between valuation subrings of K and valuations on$K$

$\operatorname { I f } | \cdot | : R  \Gamma \cup \{ 0 \}$is a valuation on$R ,$let$\Gamma _ { | \cdot | } \subset \Gamma$denote the subgroup generated by all$| x | , x \in R$, which are nonzero. The set$\mathrm { s u p p } ( | \cdot | ) = \{ x \in R | | x | = 0 \}$is a prime ideal of R called the support of$| \cdot | .$. Let K be the quotient field of$R / \operatorname { s u p p } ( | \cdot | )$. Then the valuation factors as a composite$R \to K \to \Gamma \cup \{ 0 \}$. Let$R ( | \cdot | ) \subset K$be the valuation subring, i.e.$R ( | \cdot | ) = \{ x \in K | | x | \leq 1 \}$

Definition 2.5. Two valuations$| \cdot | , | \cdot | ^ { \prime }$are called equivalent if the following equivalent conditions are satisfied.

(i) There is an isomorphism of totally ordered groups α :$\Gamma _ { | \cdot | } \cong \Gamma _ { | \cdot | ^ { \prime } }$such that$| \cdot | ^ { \prime } = \alpha \circ | \cdot |$

(ii) The supports supp$( | \cdot | ) = \operatorname { s u p p } ( | \cdot | ^ { \prime } )$and valuation rings$R ( | \cdot | ) = R ( | \cdot | ^ { \prime } )$agree.

(iii) For all$a , b \in R , | a | \geq | b |$if and only$i f \left| a \right| ^ { \prime } \geq | b | ^ { \prime }$

In [18], Huber defines spaces of (continuous) valuations in great generality. Let us specialize to the case of interest to us.

Definition 2.6. (i) A Tate k-algebra is a topological k-algebra R for which there exists a subring$R _ { 0 } \subset R$such that aR ,$a \in k ^ { \times }$, forms a basis of open neighborhoods$o f 0$. A subset$M \subset R$is called bounded$i f M \subset a R _ { 0 }$for some$a \in k ^ { \times }$. An element$x \in R$is called power-bounded$i f \left\{ x ^ { n } \mid n \geq 0 \right\} \subset R$is bounded. Let$R ^ { \circ } \subset R$denote the subring of powerbounded elements.

(ii) An afinoid k-algebra is a pair$( R , R ^ { + } )$) consisting of a Tate k-algebra R and an open and integrally closed subring$R ^ { + } \subset R ^ { \circ }$

(iii) An afinoid k-algebra$( R , R ^ { + } )$is said to be of topologically finite type (tft for short) if R is a quotient of$k \langle T _ { 1 } , \dots , T _ { n } \rangle$for some n, and$R ^ { + } = R ^ { \circ }$

Here,

$$
k \langle T _ {1}, \dots , T _ {n} \rangle = \left\{\sum_ {i _ {1}, \dots , i _ {n} \geq 0} x _ {i _ {1}, \dots , i _ {n}} T _ {1} ^ {i _ {1}} \dots T _ {n} ^ {i _ {n}} \mid x _ {i _ {1}, \dots , i _ {n}} \in k, x _ {i _ {1}, \dots , i _ {n}} \rightarrow 0 \right\}
$$

is the ring of convergent power series on the ball given by$| T _ { 1 } | , \ldots , | T _ { n } | \leq 1$. Often, only afinoid k-algebras of tft are considered; however, this paper will show that other classes of afinoid k-algebras are of interest as well. We also note that any Tate k-algebra$R ,$ resp. afinoid k-algebra$( R , R ^ { + } )$, admits the completion${ \hat { R } } ,$resp.$( \hat { R } , \hat { R } ^ { + } )$, which is again a Tate, resp. afinoid, k-algebra. Everything depends only on the completion, so one may assume that$( R , R ^ { + } )$is complete in the following.

Definition 2.7. Let$( R , R ^ { + } )$be an afinoid k-algebra. Let

$X = \operatorname { S p a } ( R , R ^ { + } ) = \{ | \cdot | : R \to \Gamma \cup \{ 0 \}$continuous valuation$| \ \forall f \in R ^ { + } : | f | \leq 1 \} / \cong$

For any$x \in X$, write$f \mapsto | f ( x ) |$for the corresponding valuation on R. We equip X with the topology which has the open subsets

$$
U \left(\frac {f _ {1} , \dots , f _ {n}}{g}\right) = \{x \in X \mid \forall i: | f _ {i} (x) | \leq | g (x) | \},
$$

called rational subsets, as basis for the topology, where$f _ { 1 } , \dots , f _ { n } \in R$generate R as an ideal and$g \in R$

Remark 2.8. Let$\varpi \in k$be topologically nilpotent,$. . \mathrm { e } . \ | \varpi | < 1$. Then to$f _ { 1 } , \ldots , f _ { n }$one can add$f _ { n + 1 } = \varpi ^ { N }$for some big integer N without changing the rational subspace. Indeed, there are elements$h _ { 1 } , \ldots , h _ { n } \in R$such that$\textstyle \sum h _ { i } f _ { i } = 1$. Multiplying by$\varpi ^ { N }$ for N suficiently large, we have$\varpi ^ { N } h _ { i } \in R ^ { + }$, as$R ^ { + } \subset R$is open. Now for any$x \in$ $U { \left( \textstyle { \frac { f _ { 1 } , \ldots , f _ { n } } { g } } \right) }$, we have

$$
| \varpi^ {N} (x) | = | \sum (\varpi^ {N} h _ {i}) (x) f _ {i} (x) | \leq \max | (\varpi^ {N} h _ {i}) (x) | | f _ {i} (x) | \leq | g (x) |,
$$

as desired. In particular, we see that on rational subsets,$| g ( x ) |$is nonzero, and bounded from below.

The topological spaces$\operatorname { S p a } ( R , R ^ { + } )$have some special properties reminiscent of the properties of Spec(A) for a ring A. In fact, let us recall the following result of Hochster, [17].

Definition/Proposition 2.9. A topological space X is called spectral if it satisfies the following equivalent properties.

(i) There is some ring A such that$X \cong \operatorname { S p e c } ( A )$

(ii) One can write X as an inverse limit of finite$T _ { 0 }$spaces.

(iii) The space X is quasicompact, has a basis of quasicompact open subsets stable under finite intersections, and every irreducible closed subset has a unique generic point.

In particular, spectral spaces are quasicompact, quasiseparated and$T _ { 0 }$. Recall that a topological space X is called quasiseparated if the intersection of any two quasicompact open subsets is again quasicompact. In the following we will often abbreviate quasicompact, resp. quasiseparated, as qc, resp. qs.

Proposition 2.10 ([18, Theorem 3.5]). For any afinoid k-algebra$( R , R ^ { + } )$, the space $\operatorname { S p a } ( R , R ^ { + } )$is spectral. The rational subsets form a basis of quasicompact open subsets stable under finite intersections.

Proposition 2.11 ([18, Proposition 3.9]). Let$( R , R ^ { + } )$be an afinoid k-algebra with completion$( \hat { R } , \hat { R } ^ { + } )$. Then$\operatorname { S p a } ( R , R ^ { + } ) \cong \operatorname { S p a } ( \hat { R } , \hat { R } ^ { + } )$, identifying rational subsets.

Moreover, the space$\operatorname { S p a } ( R , R ^ { + } )$is large enough to capture important properties.

Proposition 2.12. Let$( R , R ^ { + } )$be an afinoid k-algebra,$X = \operatorname { S p a } ( R , R ^ { + } )$

(i) If$X = \emptyset$, then$\hat { R } = 0$

(ii) Let$f \in R$be such that$| f ( x ) | \neq 0$for all$x \in X$. If R is complete, then f is invertible. (iii) Let$f \in R$be such that$| f ( x ) | \leq 1$for all$x \in X$. Then$f \in R ^ { + }$

Proof. Part (i) is [18], Proposition 3.6 (i). Part (ii) is [19], Lemma 1.4, and part (iii) follows from [18], Lemma 3.3 (i).

We want to endow$X = \operatorname { S p a } ( R , R ^ { + } )$with a structure sheaf${ \mathcal { O } } _ { X }$. The construction is as follows.

Definition 2.13. Let$( R , R ^ { + } )$be an afinoid k-algebra, and let$\begin{array} { r } { U = U ( \frac { f _ { 1 } , \dots , f _ { n } } { q } ) \subset X = } \end{array}$ $\operatorname { S p a } ( R , R ^ { + } )$be a rational subset. Choose some$R _ { 0 } \subset R$such that a$R _ { 0 } , a \in \bar { k ^ { \times } }$, is a basis of open neighborhoods of 0 in R. Consider the subalgebra$R [ \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } ]$of$R [ g ^ { - 1 } ]$, and equip it with the topology making a$\textstyle R _ { 0 } [ { \frac { f _ { 1 } } { g } } , \dotsc , { \frac { f _ { n } } { g } } ] , a \in k ^ { \times }$, a basis of open neighborhoods of 0. Let$B \subset R [ { \frac { f _ { 1 } } { g } } , \dotsc , { \frac { f _ { n } } { g } } ]$be the integral closure of$R ^ { + } [ \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } ]$in$R [ \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } ]$ Then$( R [ \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } ] , B )$is an afinoid k-algebra. Let$( R \langle \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } \rangle , \bar { \hat { B } } )$be its completion.

Obviously,

$$
\operatorname{Spa} (R \langle \frac {f _ {1}}{g}, \dots , \frac {f _ {n}}{g} \rangle , \hat {B}) \to \operatorname{Spa} (R, R ^ {+})
$$

factors over the open subset$U \subset X .$

Proposition 2.14 ([19, Proposition 1.3]). In the situation of the definition, the following universal property is satisfied. For every complete afinoid k-algebra$( S , S ^ { + } )$with a map$( R , R ^ { + } )  ( S , S ^ { + } )$such that the induced map Spa$\varrho ( S , S ^ { + } )  \mathrm { S p a } ( R , R ^ { + } )$factors over U, there is a unique map

$$
(R \langle \frac {f _ {1}}{g}, \dots , \frac {f _ {n}}{g} \rangle , \hat {B}) \rightarrow (S, S ^ {+})
$$

making the obvious diagram commute.

In particular,$( R \langle \frac { f _ { 1 } } { g } , \ldots , \frac { f _ { n } } { g } \rangle , \hat { B } )$depends only on U. Define

$$
\left(\mathcal {O} _ {X} (U), \mathcal {O} _ {X} ^ {+} (U)\right) = \left(R \langle \frac {f _ {1}}{g}, \dots , \frac {f _ {n}}{g} \rangle , \hat {B}\right).
$$

For example,$( { \mathcal { O } } _ { X } ( X ) , { \mathcal { O } } _ { X } ^ { + } ( X ) )$is the completion$o f \left( R , R ^ { + } \right)$

The idea is that since$f _ { 1 } , \ldots , f _ { n }$generate R, not all$| f _ { i } ( x ) | = 0$for$x \in U$; in particular, $| g ( x ) | \neq 0$for all$x \in U$. This implies that g is invertible in S in the situation of the proposition. Moreover,$| ( \frac { f _ { i } } { q } ) ( x ) | \leq 1$for all$x \in U .$, which means that$\begin{array} { r } { \frac { f _ { i } } { g } \in S ^ { + } } \end{array}$

We define presheaves${ \mathcal { O } } _ { X }$and${ \mathcal { O } } _ { X } ^ { + }$on X as above on rational subsets, and for general open$U \subset X$by requiring

$$
\mathcal {O} _ {X} (W) = \varprojlim_ {U \subset W \text {   rational }} \mathcal {O} _ {X} (U)  ,
$$

and similarly for${ \mathcal { O } } _ { X } ^ { + }$

Proposition 2.15 ([19, Lemma 1.5, Proposition 1.6]). For any$x \in X$, the valuation $f \mapsto | f ( x ) |$extends to the stalk${ \mathcal { O } } _ { X , x }$, and

$$
\mathcal {O} _ {X, x} ^ {+} = \left\{f \in \mathcal {O} _ {X, x} \mid | f (x) | \leq 1 \right\}.
$$

The ring${ \mathcal { O } } _ { X , x }$is a local ring with maximal ideal given by$\{ f \mid f \mid f ( x ) | = 0 \}$. The ring $\mathcal { O } _ { X , x } ^ { + }$is a local ring with maximal ideal given by$\{ f \mid f \mid f ( x ) | < 1 \}$. Moreover, for any open subset$U \subset X$，

$$
\mathcal {O} _ {X} ^ {+} (U) = \left\{f \in \mathcal {O} _ {X} (U) \mid \forall x \in U: | f (x) | \leq 1 \right\}.
$$

If$U \subset X$is rational, then$U \cong \operatorname { S p a } ( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$compatible with rational subsets, the presheaves${ \mathcal { O } } _ { X }$and${ \mathcal { O } } _ { X } ^ { + }$, and the valuations at all$x \in U$

Unfortunately, it is not in general$\mathrm { k n o w n } ^ { 1 }$that${ \mathcal { O } } _ { X }$is sheaf. We note that the proposition ensures that${ \mathcal { O } } _ { X } ^ { + }$is a sheaf if${ \mathcal { O } } _ { X }$is. The basic problem is that completion behaves in general badly for nonnoetherian rings.

Definition 2.16. A Tate k-algebra R is called strongly noetherian if

$$
R \langle T _ {1}, \dots , T _ {n} \rangle = \{\sum_ {i _ {1}, \dots , i _ {n} \geq 0} x _ {i _ {1}, \dots , i _ {n}} T _ {1} ^ {i _ {1}} \dots T _ {n} ^ {i _ {n}} \mid x _ {i _ {1}, \dots , i _ {n}} \in \hat {R}, x _ {i _ {1}, \dots , i _ {n}} \rightarrow 0 \}
$$

is noetherian for all$n \geq 0$

For example, if R is of tft, then R is strongly noetherian.

Theorem 2.17 ([19, Theorem 2.2]).$H ( R , R ^ { + } )$is an afinoid k-algebra such that R is strongly noetherian, then${ \mathcal { O } } _ { X }$is a sheaf.

Later, we will show that this theorem is true under the assumption that R is a perfectoid k-algebra. We define perfectoid k-algebras later; let us only remark that except for trivial examples, they are huge and in particular not strongly noetherian.

Finally, we can define the category of adic spaces over k. Namely, consider the category (V) of triples$( X , { \mathcal { O } } _ { X } , ( | \cdot ( x ) | | x \in X ) )$consisting of a locally ringed topological space$( X , { \mathcal { O } } _ { X } )$, where${ \mathcal { O } } _ { X }$is a sheaf of complete topological k-algebras, and a continuous valuation$f \mapsto | f ( x ) |$on${ \mathcal { O } } _ { X , x }$for every$x \in X$. Morphisms are given by morphisms of locally ringed topological spaces which are continuous k-algebra morphisms on${ \mathcal { O } } _ { X }$, and compatible with the valuations in the obvious sense.

Any afinoid k-algebra$( R , R ^ { + } )$for which${ \mathcal { O } } _ { X }$is a sheaf gives rise to such a triple $( X , { \mathcal { O } } _ { X } , ( | \cdot ( x ) | | x \in X ) )$). Call an object of$( V )$isomorphic to such a triple an afinoid adic space.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>and probably not true</span></small>

Definition 2.18. An adic space over$k$is an object$( X , { \mathcal { O } } _ { X } , ( | \cdot ( x ) | \mid x \in X ) )$of (V ) that is locally on X an afinoid adic space.

Proposition 2.19 ([19, Proposition 2.1 (ii)]). For any afinoid k-algebra$( R , R ^ { + } )$with $X = \operatorname { S p a } ( R , R ^ { + } )$) such that${ \mathcal { O } } _ { X }$is a sheaf, and any adic space$Y$over$k ,$, we have

$$
\mathrm{Hom} (Y, X) = \mathrm{Hom} ((\hat {R}, \hat {R} ^ {+}), (\mathcal {O} _ {Y} (Y), \mathcal {O} _ {Y} ^ {+} (Y))) .
$$

Here, the latter set denotes the set of continuous k-algebra morphisms${ \hat { R } } \to { \mathcal { O } } _ { Y } ( Y )$such that$\hat { R } ^ { + }$is mapped into${ \mathcal { O } } _ { Y } ^ { + } ( Y )$

In particular, the category of complete afinoid k-algebras for which the structure presheaf is a sheaf is equivalent to the category of afinoid adic spaces over$k$

For the rest of this section, let us discuss an example, and explain the relation to rigid-analytic varieties, [31], and Berkovich’s analytic spaces, [1].

Example 2.20. Assume that k is complete and algebraically closed. Let$R = k \langle T \rangle$ $R ^ { + } = R ^ { \circ } = k ^ { \circ } \langle T \rangle$the subspace of power series with coeficients in$k ^ { \circ }$. Then$( R , R ^ { + } )$is an afinoid k-algebra of tft. We want to describe the topological space$X = \operatorname { S p a } ( R , R ^ { + } )$ For convenience, let us fix the norm$| \cdot | : k \to { \mathbb { R } _ { \geq 0 } }$. Then there are in general points of 5 diferent types, of which the first four are already present in Berkovich’s theory.

![](images/page_10_image_7.jpg)

(1) The classical points: Let$x \in k ^ { \circ }$, i.e.$x \in k$with$| x | \leq 1$. Then for any$f \in k \langle T \rangle$, we can evaluate$f$at x to get a map$\begin{array} { r } { R  k , f = \sum a _ { n } T ^ { n } \mapsto \sum a _ { n } x ^ { n } } \end{array}$. Composing with the norm on$k ,$one gets a valuation$f \mapsto | f ( x ) |$on$R ,$which is obviously continuous and $\leq 1$for all$f \in R ^ { + }$

(2), (3) The rays of the tree: Let$0 \leq r \leq 1$be some real number, and$x \in k ^ { \circ }$. Then

$$
f = \sum a _ {n} (T - x) ^ {n} \mapsto \sup | a _ {n} | r ^ {n} = \sup _ {y \in k ^ {\circ}: | y - x | \leq r} | f (y) |
$$

defines another continuous valuation on R which is$\leq 1$for all$f \in R ^ { + }$. It depends only on the disk$D ( x , r ) = \{ y \in k ^ { \circ } \mid | y - x | \leq r \}$. If$r = 0$, then it agrees with the classical point corresponding to$x .$. For$r = 1$, the disk$D ( x , 1 )$is independent of$x \in k ^ { \circ }$, and the corresponding valuation is called the Gaußpoint.

If$r \in | k ^ { \times } |$, then the point is said to be of type (2), otherwise of type (3). Note that a branching occurs at a point corresponding to the disk$D ( x , r )$if and only if$r \in | k ^ { \times } |$, i.e. a branching occurs precisely at the points of type (2).

(4) Dead ends of the tree: Let$D _ { 1 } \supset D _ { 2 } \supset . .$. be a sequence of disks with$\cap D _ { i } = \emptyset$ Such families exist if k is not spherically complete, e.g. if$k = \mathbb { C } _ { p }$. Then

$$
f \mapsto \inf _ {i} \sup _ {x \in D _ {i}} | f (x) |
$$

defines a valuation on R, which again is$\leq 1$for all$f \in R ^ { + }$

(5) Finally, there are some valuations of rank 2 which are only seen in the adic space. Let us first give an example, before giving the general classification. Consider the totally ordered abelian group$\Gamma = \mathbb { R } _ { > 0 } \times \gamma ^ { \mathbb { Z } }$, where we require that$r < \gamma < 1$for all real numbers$r < 1$. It is easily seen that there is a unique such ordering. Then

$$
f = \sum a _ {n} (T - x) ^ {n} \mapsto \max | a _ {n} | \gamma^ {n}
$$

defines a rank-2-valuation on R. This is similar to cases$( 2 ) , ( 3 )$, but with the variable r infinitesimally close to 1. One may check that this point only depends on the disc $D ( x , < 1 ) = \{ y \in k ^ { \circ } \mid | y - x | < 1 \}$

Similarly, take any$x \in k ^ { \circ }$, some real number$0 < r < 1$and choose a sign$\mathrm { ? } \in \{ < , > \}$ Consider the totally ordered abelian group$\Gamma _ { ? r } = \mathbb { R } _ { > 0 } \times \gamma ^ { \mathbb { Z } }$, where$r ^ { \prime } < \gamma < r$for all real numbers$r ^ { \prime } < r { \mathrm { ~ i f ~ } } ? = <$<, and$r ^ { \prime } > \gamma > r$for all real numbers$r ^ { \prime } > r \mathrm { ~ i f ~ } ? = >$. Then

$$
f = \sum a _ {n} (T - x) ^ {n} \mapsto \max | a _ {n} | \gamma^ {n}
$$

defines a rank 2-valuation on R. If$? = < .$, then it depends only on$D ( x , < r ) = \{ y \in k ^ { \circ } \mid$ $| y - x | < r \} . \ \mathrm { I f } \ ? = >$, then it depends only on$D ( x , r )$

One checks that if$r \not \in | k ^ { \times } |$, then these points are all equivalent to the corresponding point of type (3). However, at each branching point, i.e. point of type (2), this gives exactly one additional point for each ray starting from this point.

All points except those of type (2) are closed. Let κ be the residue field of k. Then the closure of the Gaußpoint is exactly the Gaußpoint together with the points of type (5) around it, and is homeomorphic to$\mathbb { A } _ { \kappa } ^ { 1 }$, with the Gaußpoint as the generic point. At the other points of type (2), one gets$\mathbb { P } _ { \kappa } ^ { 1 }$

We note that in case (5), one could define a similar valuation

$$
f = \sum a _ {n} T ^ {n} \mapsto \max | a _ {n} | \gamma^ {n},
$$

with$\gamma$having the property that$r > \gamma > 1$for all$r > 1$. This valuation would still be continuous, but it takes the value$\gamma > 1$on$T \in R ^ { + }$. This shows the relevance of the requirement$| f ( x ) | \leq 1$for all$f \in R ^ { + }$, which is automatic for rank-1-valuations.

Theorem 2.21 ([20, (1.1.11)]). There is a fully faithful functor

$$
r: \{\text { rigid   -   analytic   varieties } / k \} \to \{\text { adic   spaces } / k \}: X \mapsto X ^ {\mathrm{ad}}
$$

sending$\operatorname { S p } ( R )$to$\operatorname { S p a } ( R , R ^ { + } )$for any afinoid k-algebra$( R , R ^ { + } )$of tft. It induces an equivalence

$$
\left\{\text { qs   rigid } - \text { analytic   varieties } / k \right\} \cong \left\{\text { qs   adic   spaces   locally   of   finite   type } / k \right\},
$$

where an adic space over k is called locally of finite type if it is locally of the form $\operatorname { S p a } ( R , R ^ { + } )$, where$( R , R ^ { + } )$is of tft. Let X be a rigid-analytic variety over k with corresponding adic space$X ^ { \mathrm { a d } }$. As any classical point defines an adic point, we have $X \subset X ^ { \mathrm { a d } }$. If X is quasiseparated, then mapping a quasicompact open subset$U \subset X ^ { \mathrm { a d } }$ to$U \cap X$defines a bijection

{qc admissible opens in$X \} \cong \{ \mathrm { q c }$opens in$X ^ { \mathrm { a d } } \}$2

the inverse of which is denoted$U \mapsto { \tilde { U } }$. Under this bijection a family of quasicompact admissible opens$U _ { i } ~ \subset ~ X$forms an admissible cover if and only if the corresponding subsets${ \tilde { U } } _ { i } \subset X ^ { \mathrm { a d } }$cover$X ^ { \mathrm { a d } }$

In particular, for any rigid-analytic variety X, the topos ofsheaves on the Grothendieck site associated to X is equivalent to the category of sheaves on the sober topological space $X ^ { \mathrm { a d } }$

We recall that for abstract reasons, there is up to equivalence at most one sober topological space with the last property in the theorem. This gives the topological space underlying the adic space a natural interpretation.

In the example$X = \operatorname { S p } ( k \langle T \rangle )$discussed above, a typical example of a non-admissible cover is the cover of$\{ x \mid | x | \leq 1 \}$as

$$
\{x \mid | x | \leq 1 \} = \{x \mid | x | = 1 \} \cup \bigcup_ {r <   1} \{x \mid | x | \leq r \}.
$$

In the adic world, one can see this non-admissibility as being caused by the point of type (5) which gives |x| a value$\gamma < 1$bigger than any$r < 1$

![](images/page_12_image_4.jpg)

Moreover, adic spaces behave well with respect to formal models. In fact, one can define adic spaces in greater generality so as to include locally noetherian formal schemes as a full subcategory, but we will not need this more general theory here.

Theorem 2.22. Let X be some admissible formal scheme over$k ^ { \circ }$, let X be its generic fibre in the sense of Raynaud, and let$X ^ { \mathrm { a d } }$be the associated adic space. Then there is a continuous specialization map

$$
\mathrm{sp}: X ^ {\mathrm{ad}} \to \mathfrak {X},
$$

extending to a morphism of locally ringed topological spaces$( X ^ { \mathrm { a d } } , { \mathcal { O } } _ { X ^ { \mathrm { a d } } } ^ { + } )  ( { \mathfrak { X } } , { \mathcal { O } } _ { \mathfrak { X } } )$

Now assume that X is a fixed quasicompact quasiseparated adic space locally of finite type over k. By Raynaud, there exist formal models X for X, unique up to admissible blowup. Then there is a homeomorphism

$$
X \cong \varprojlim_ {\mathfrak {X}} \mathfrak {X}  ,
$$

where X runs over formal models of X, extending to an isomorphism of locally ringed topological spaces$( X , { \mathcal { O } } _ { X } ^ { + } ) \cong \varprojlim _ { \mathfrak { X } } ( { \mathfrak { X } } , { \mathcal { O } } _ { \mathfrak { X } } )$, where the right-hand side is the inverse limit in the category of locally ringed topological spaces.

Proof. It is an easy exercise to deduce this from the previous theorem and the results of [3], Section 4, and [19], Section 4.

In the example, one can start with${ \mathfrak { X } } = \operatorname { S p f } ( k ^ { \circ } \langle T \rangle )$as a formal model; this gives$\mathbb { A } _ { \kappa } ^ { 1 }$ as underlying topological space. After that, one can perform iterated blowups at closed points. This introduces additional$\mathbb { P } _ { \kappa } ^ { 1 } \mathrm { { ' s } } ;$the strict transform of each component survives in the inverse limit and gives the closure of a point of type (2). Note that the point of type (2) is given as the preimage of the generic point of the component in the formal model.

We note that in order to get continuity of sp, it is necessary to use nonstrict equalities in the definition of open subsets.

Now, let us state the following theorem about the comparison of Berkovich’s analytic spaces and Huber’s adic spaces. For this, we need to recall the following definition:

Definition 2.23. An adic space X over k is called taut if it is quasiseparated and for every quasicompact open subset$U \subset X$, the closure U of U in X is still quasicompact.

Most natural adic spaces are taut, e.g. all afinoid adic spaces, or more generally all qcqs adic spaces, and also all adic spaces associated to separated schemes of finite type over k. However, in recent work of Hellmann, [16], studying an analogue of Rapoport-Zink period domains in the context of deformations of Galois representations, it was found that the weakly admissible locus is in general a nontaut adic space.

We note that one can also define taut rigid-analytic varieties, and that one gets an equivalence of categories between the category of taut rigid-analytic varieties over k and taut adic spaces locally of finite type over k. Hence the first equivalence in the following theorem could be stated without reference to adic spaces.

Theorem 2.24 ([20, Proposition 8.3.1, Lemma 8.1.8]). There is an equivalence of categories

{hausdorf strictly k−analytic Berkovich spaces}

<sup>∼</sup><sub>= {taut adic spaces locally of finite</sub>$\mathrm { t y p e } / k \}$

sending${ \mathcal { M } } ( R )$to$\operatorname { S p a } ( R , R ^ { + } )$for any afinoid k-algebra$( R , R ^ { + } )$of$t f t .$

$L e t X ^ { \mathrm { B e r k } }$map to$X ^ { \mathrm { a d } }$under this equivalence. Then there is an injective map of sets $X ^ { \mathrm { B e r k } }  X ^ { \mathrm { a d } }$, whose image is precisely the subset of rank-1-valuations. This map is in general not continuous. It admits a continuous retraction$X ^ { \mathrm { a d } }  X ^ { \mathrm { B e r k } }$, which identifies $X ^ { \mathrm { B e r k } }$with the maximal hausdorf quotient of$X ^ { \mathrm { a d } }$

In the example above, the image of the map$X ^ { \mathrm { B e r k } }  X ^ { \mathrm { a d } }$consists of the points of type$( 1 ) \textrm { - } ( 4 )$. The retraction$X ^ { \mathrm { { \bar { a d } } } }  X ^ { \mathrm { { B e r k } } }$contracts each point of type (2) with all points of type (5) around it, mapping them to the corresponding point of type (2) in $X ^ { \mathrm { B e r k } }$. For any map from$X ^ { \mathrm { a d } }$to a hausdorf topological space, any point of type (2) will have the same image as the points of type (5) around it, as they lie in its topological closure, which verifies the last assertion of the theorem in this case.

Let us end this section by describing in more detail the fibres of the map$X ^ { \mathrm { a d } }  X ^ { \mathrm { B e r k } }$ In fact, this discussion is valid even for adic spaces which are not related to Berkovich spaces. As the following discussion is local, we restrict to the afinoid case.

Let$( R , R ^ { + } )$be an afinoid k-algebra, and let$X = \operatorname { S p a } ( R , R ^ { + } )$. We need not assume that${ \mathcal { O } } _ { X }$is a sheaf in the following. For any$x \in X$, we let$k ( x )$be the residue field of ${ \mathcal { O } } _ { X , x }$, and$k ( x ) ^ { + } \subset k ( x )$be the image of${ \mathcal { O } } _ { X , x } ^ { + }$. We have the following crucial property, surprising at first sight.

Proposition 2.25. Let$\varpi \in k$be topologically nilpotent. Then the \$-adic completion $o f { \mathcal { O } } _ { X , x } ^ { + }$is equal to the \$-adic completion$\widehat { k ( x ) } ^ { + } \ o f k ( x ) ^ { + }$

Proof. It is enough to note that kernel of the map$\mathcal { O } _ { X , x } ^ { + } \to k ( x ) ^ { + }$, which is also the kernel of the map$\mathcal { O } _ { X , x }  k ( x )$, is \$-divisible.

Definition 2.26. An afinoid field is pair$( K , K ^ { + } )$consisting of a nonarchimedean field K and an open valuation subring$K ^ { + } \subset K ^ { \circ }$

In other words, an afinoid field is given by a nonarchimedean field K equipped with a continuous valuation (up to equivalence). In the situation above,$( k ( x ) , k ( x ) ^ { + } )$is an afinoid field. The completion of an afinoid field is again an afinoid field. Also note that afinoid fields for which$k \subset K$are afinoid k-algebras. The following description of points is immediate.

Proposition 2.27. Let$( R , R ^ { + } )$be an$a f f _ { \mathit { n } }$noid k-algebra. The points of$\operatorname { S p a } ( R , R ^ { + } )$are in bijection with maps$( R , R ^ { + } )  ( K , K ^ { + } )$to complete afinoid fields$( K , K ^ { + } )$such that the quotient field of the image of R in K is dense.

Definition 2.28. For two points x, y in some topological space$X _ { \perp }$, we say that x specializes to y (or y generalizes to x), written$x \succ y \ ( o r \ y \prec x )$, if y lies in the closure ${ \overline { { \{ x \} } } } \ o f \ x$

Proposition${ \bf 2 . 2 9 \ ( [ 2 0 , ( 1 . 1 . 6 ) \cdot ( 1 . 1 . 1 0 ) ] ) }$. Let$( R , R ^ { + } )$be an afinoid$k \mathrm { - } a l g e b r a$, and $l e t \ x , y \in X = \operatorname { S p a } ( R , R ^ { + } )$correspond to maps$( R , R ^ { + } )  ( K , K ^ { + } )$, resp.$( R , R ^ { + } )$ $( L , L ^ { + } )$. Then$x \succ y$if and only if$K \cong L$as topological R-algebras and$L ^ { + } \subset K ^ { + }$

For any point$y \in X$, the set$\{ x \mid x \succ y \}$of generalizations of y is a totally ordered chain of length exactly the rank of the valuation corresponding to$y .$

Note that in particular, for a given complete nonarchimedean field K with a map $R \to K$, there is the point$x _ { 0 }$corresponding to$( K , K ^ { \circ } )$. This corresponds to the unique continuous rank-1-valuation on$K$. The point x<sub>0</sub> specializes to any other point for the same K.

## 3. Perfectoid fields

Definition 3.1. A perfectoid field is a complete nonarchimedean field K of residue characteristic$p > 0$whose associated rank-1-valuation is nondiscrete, such that the Frobenius is surjective on$K ^ { \circ } / p$

We note that the requirement that the valuation is nondiscrete is needed to exclude unramified extensions of$\mathbb { Q } _ { p }$. It has the following consequence.

Lemma 3.2. Let$| \cdot | : K \to \Gamma \cup \{ 0 \}$be the unique rank-1-valuation on$K$, where$\Gamma = | K ^ { \times } |$ is chosen minimal. Then Γ is$p \cdot$-divisible.

Proof. As$\Gamma \neq | p | ^ { \mathbb { Z } }$, the group Γ is generated by the set of all$| x |$for$x \in K$with $| p | < | x | \le 1$. For such$x ,$choose some y such that$| x - y ^ { p } | \leq | p |$. Then$| y | ^ { p } = | y ^ { p } | = | x | .$2 as desired.

The class of perfectoid fields naturally separates into the fields of characteristic 0 and those of characteristic$p .$. In characteristic$p ,$a perfectoid field is the same as a complete perfect nonarchimedean field.

Remark 3.3. The notion of a perfectoid field is closely related to the notion of a deeply ramified field. Taking the definition of deeply ramified fields given in [14], we remark that Proposition 6.6.6 of [14] says that a perfectoid field K is deeply ramified, and conversely, a complete deeply ramified field with valuation of rank 1 is a perfectoid field.

Now we describe the process of tilting for perfectoid fields, which is a functor from the category of all perfectoid fields to the category of perfectoid fields in characteristic $p .$

For its first description, choose some element$\varpi \in K ^ { \times }$such that$| p | \leq | \varpi | < 1$. Now consider

$$
\varprojlim_ {\Phi} K ^ {\circ} / \varpi ,
$$

where Φ denotes the Frobenius morphism$x \mapsto x ^ { p }$. This gives a perfect ring of characteristic$p .$We equip it with the inverse limit topology; note that each$K ^ { \circ } / \varpi$naturally has the discrete topology.

Lemma 3.4. (i) There is a multiplicative homeomorphism

$$
\varprojlim_ {x \mapsto x ^ {p}} K ^ {\circ} \stackrel {{\cong}} {{\to}} \varprojlim_ {\Phi} K ^ {\circ} / \varpi ,
$$

given by projection. In particular, the right-hand side is independent of \$. Moreover, we get a map

$$
\varprojlim_ {\Phi} K ^ {\circ} / \varpi \to K ^ {\circ}: x \mapsto x ^ {\sharp}.
$$

(ii) There is an element$\varpi ^ { \flat } \in \varprojlim _ { \Phi } K ^ { \circ } /$\$ with$| ( \varpi ^ { \flat } ) ^ { \sharp } | = | \varpi |$. Define

$$
K ^ {\flat} = (\varprojlim_ {\Phi} K ^ {\circ} / \varpi) [ (\varpi^ {\flat}) ^ {- 1} ] .
$$

(iii) There is a multiplicative homeomorphism

$$
K ^ {\flat} = \varprojlim_ {x \mapsto x ^ {p}} K.
$$

In particular, there is a map$K ^ { \flat } \ \to \ K , \ x \ \mapsto \ x ^ { \sharp }$. Then$K ^ { \flat }$is a perfectoid field of characteristic$p ,$

$$
K ^ {\flat \circ} = \varprojlim_ {x \mapsto x ^ {p}} K ^ {\circ} \cong \varprojlim_ {\Phi} K ^ {\circ} / \varpi ,
$$

and the rank-1-valuation on$K ^ { \flat }$can be defined by$| x | _ { K ^ { \flat } } = | x ^ { \sharp } | _ { K }$. We have$| K ^ { \flat \times } | = | K ^ { \times } |$ Moreover,

$$
K ^ {\flat \circ} / \varpi^ {\flat} \cong K ^ {\circ} / \varpi , K ^ {\flat \circ} / \mathfrak {m} ^ {\flat} = K ^ {\circ} / \mathfrak {m},
$$

where m, resp.${ \mathfrak { m } } ^ { \flat }$, is the maximal ideal of$K ^ { \circ }$, resp.$K ^ { \flat \circ }$

(iv) If K is of characteristic$p ,$then$K ^ { \flat } = K$

We call$K ^ { \flat }$the tilt of$K .$.

Remark 3.5. Obviously,$\varpi ^ { \flat }$in (ii) is not unique. As it is not harmful to replace$\varpi$with an element of the same norm, we will usually redefine$\varpi = ( \varpi ^ { \flat } ) ^ { \sharp }$, which comes equipped with a compatible system

$$
\varpi^ {1 / p ^ {n}} = ((\varpi^ {\flat}) ^ {1 / p ^ {n}}) ^ {\sharp}
$$

of$p ^ { n } .$-th roots. Conversely, \$ together with such a choice of$p ^ { n } .$-th roots gives an element $\varpi ^ { \flat }$of

$$
K ^ {\flat} = \varprojlim_ {x \mapsto x ^ {p}} K.
$$

Proof. (i) We begin by constructing a multiplicative continuous map

$$
\varprojlim_ {\Phi} K ^ {\circ} / \varpi \to K ^ {\circ}: x \mapsto x ^ {\sharp}.
$$

Let$( \overline { { x } } _ { 0 } , \overline { { x } } _ { 1 } , . . . ) \in \varprojlim _ { \Phi } K ^ { \circ } / \varpi$. Choose any lift$x _ { n } \in K ^ { \circ }$of$\overline { { x } } _ { n }$. Then we claim that the limit

$$
x ^ {\sharp} = \lim _ {n \to \infty} x _ {n} ^ {p ^ {n}}
$$

exists and is independent of all choices. For this, it is enough to see that$x _ { n } ^ { p ^ { n } }$gives a well-defined element of$K ^ { \circ } / \varpi ^ { n + 1 }$. But if$x _ { n } ^ { \prime }$is a second lift, then$x _ { n } - x _ { n } ^ { \prime }$is divisible by \$. One checks by induction on$i = 0 , 1 , \ldots , n$that

$$
(x _ {n} ^ {\prime}) ^ {p ^ {i}} - x _ {n} ^ {p ^ {i}} = (x _ {n} ^ {p ^ {i - 1}} + ((x _ {n} ^ {\prime}) ^ {p ^ {i - 1}} - x _ {n} ^ {p ^ {i - 1}})) ^ {p} - x _ {n} ^ {p ^ {i}}
$$

gives a well-defined element of$K ^ { \circ } / \varpi ^ { i + 1 }$, using that$\varpi | p .$

It is clear from the definition that$x \mapsto x ^ { \sharp }$is multiplicative and continuous. Now the map lim$\operatorname { \Pi } _ { \cdot \Phi } K ^ { \circ } / \varpi \to \varprojlim _ { x \mapsto x ^ { p } } K ^ { \circ }$given by$x \mapsto ( x ^ { \sharp } , ( x ^ { 1 / p } ) ^ { \sharp } , \dots )$gives an inverse to the obvious projection map.

(ii) Pick some element$\varpi _ { 1 }$with$| \varpi _ { 1 } | ^ { p } = | \varpi |$. Then$\varpi _ { 1 }$defines a nonzero element of $K ^ { \circ } / \varpi$. Choose any sequence

$$
\varpi^ {\flat} = (0, \varpi_ {1}, \ldots) \in \varprojlim_ {\Phi} K ^ {\circ} / \varpi ;
$$

this is possible by surjectivity of Φ on$K ^ { \circ } / \varpi$. By the proof of part (i), we have$| ( \varpi ^ { \flat } ) ^ { \sharp } - \qquad$ $\varpi _ { 1 } ^ { p } | \le | \varpi | ^ { 2 }$. This gives$| ( \varpi ^ { \flat } ) ^ { \sharp } | = | \varpi |$, as desired.

(iii) As$x \mapsto x ^ { \sharp }$is multiplicative, it extends to a map

$$
K ^ {\flat} \to \varprojlim_ {x \mapsto x ^ {p}} K  .
$$

One easily checks that it is a homeomorphism; in particular$K ^ { \flat }$is a field. One also checks that the topology on$\varprojlim _ { \Phi } K ^ { \circ } / \varpi$is induced by the norm$x \mapsto \left| x ^ { \sharp } \right|$. Hence the topology on$K ^ { \flat }$is induced by the rank-1-valuation$x \mapsto | x ^ { \sharp } |$. Clearly,$K ^ { \flat }$<sup>[</sup> is perfect and complete, so$K ^ { \flat }$is a perfectoid field of characteristic$p .$. One easily deduces all other claims.

(iv) This is clear since$K ^ { \flat } \cong \varprojlim _ { x \mapsto x ^ { p } } K .$

Recall that when working with adic spaces, it is important to understand the contin uous valuations on$K$. Under the process of tilting, we have the following equivalence.

Proposition 3.6. Let K be a perfectoid field with tilt$K ^ { \flat }$<sup>[</sup>. Then the continuous valuations | · | of K (up to equivalence) are mapped bijectively to the continuous valuations $| \cdot | ^ { \flat } o f K ^ { \flat }$(up to equivalence) via$| x | ^ { \flat } = | x ^ { \sharp } |$

Proof. First, we check that the map$| \cdot | \mapsto | \cdot | ^ { \flat }$maps valuations to valuations. All properties except$| x + y | ^ { \flat } \leq \operatorname* { m a x } ( | x | ^ { \flat } , | y | ^ { \flat } )$are immediate, using that$x \mapsto x ^ { \sharp }$is multiplicative. But

$$
| x + y | ^ {\flat} = \lim _ {n \rightarrow \infty} | (x ^ {1 / p ^ {n}}) ^ {\sharp} + (y ^ {1 / p ^ {n}}) ^ {\sharp} | ^ {p ^ {n}}
$$

$$
\leq \max (\lim _ {n \to \infty} | (x ^ {1 / p ^ {n}}) ^ {\sharp} | ^ {p ^ {n}}, \lim _ {n \to \infty} | (y ^ {1 / p ^ {n}}) ^ {\sharp} | ^ {p ^ {n}}) = \max (| x ^ {\sharp} |, | y ^ {\sharp} |).
$$

It is clear that continuity is preserved.

On the other hand, continuous valuations are in bijection with open valuation subrings $K ^ { + } \subset K ^ { \circ }$. They necessarily contain the topologically nilpotent elements m. We see that open valuation subrings$K ^ { + } ~ \subset ~ K ^ { \circ }$are in bijection with valuation subrings in $K ^ { \circ } / \mathfrak { m } = K ^ { \flat \circ } / \mathfrak { m } ^ { \flat }$. This implies that one gets a bijection with continuous valuations of K and continuous valuations of$K ^ { \flat }$<sup>[</sup> which is easily seen to be the one described.

The main theorem about tilting for perfectoid fields is the following theorem. For many fields, this was known by the classical work of Fontaine-Wintenberger.

Theorem 3.7. Let K be a perfectoid field.

(i) Let L be a finite extension of K. Then L (with its natural topology as a finitedimensional K-vector space) is a perfectoid field.

(ii) Let$K ^ { \flat }$be the tilt of K. Then the tilting functor$L \mapsto L ^ { \flat }$induces an equivalence $o f$categories between the category of finite extensions of K and the category of finite extensions of$K ^ { \flat }$. This equivalence preserves degrees.

It turns out that many of the arguments will generalize directly to the context of perfectoid K-algebras introduced later. For this reason, we defer the proof of this theorem. Let us only prove the following special case here.

Proposition 3.8. Let K be a perfectoid field with tilt$K ^ { \flat } . \textit { I f K } ^ { \flat }$is algebraically closed, then K is algebraically closed.

Proof. Let$P ( X ) = X ^ { d } + a _ { d - 1 } X ^ { d - 1 } + \ldots + a _ { 0 } \in K ^ { \circ } [ X ]$be any monic irreducible polynomial of positive degree d. Then the Newton polygon of$P$is a line. Moreover, we may assume that the constant term of$P$has absolute value$| a _ { 0 } | = 1$, as$| K ^ { \times } | = | K ^ { \flat \times } |$is a Q-vector space.

Now let$Q ( X ) = X ^ { d } + b _ { d - 1 } X ^ { d - 1 } + \ldots + b _ { 0 } \in K ^ { \mathfrak { p o } } [ X ]$be any polynomial such that P and$Q$have the same image in$K ^ { \circ } / \varpi [ X ] = K ^ { \flat \circ } / \varpi ^ { \flat } [ X ]$, and let$y \in K ^ { \flat \circ }$be a root of$Q .$

Considering$P ( X + y ^ { \sharp } )$, we see that the constant term$P ( y ^ { \sharp } )$is divisible by \$. As it is still irreducible, its Newton polygon is a line and hence the polynomial$P _ { 1 } ( X ) =$ $c ^ { - d } P ( c X + y ^ { \sharp } )$has integral coeficients again, where$| c | ^ { d } = | P ( y ^ { \sharp } ) | \leq | \varpi |$. Repeating the arguments gives an algorithm converging to a root of$P .$

Our proof of Theorem 3.7 will make use of Faltings’s almost mathematics. For this reason, we recall some necessary background in the next section.

## 4. Almost mathematics

We will use the book of Gabber-Ramero, [14], as our basic reference.

Fix a perfectoid field K. Let${ \mathfrak { m } } = K ^ { \circ \circ } \subset K ^ { \circ }$be the subset of topologically nilpotent elements; it is also the set$\{ x \in K \mid | x | < 1 \}$, and the unique maximal ideal of$K ^ { \circ }$. The basic idea of almost mathematics is that one neglects m-torsion everywhere.

Definition 4.1. Let M be a$K ^ { \circ }$-module. An element$x \in M$is almost zero$i f \mathfrak { m } x = 0$ The module M is almost zero if all of its elements are almost zero; equivalently, m$M = 0$

Lemma 4.2. The full subcategory of almost zero objects in$K ^ { \circ }$− mod is thick.

Proof. The only nontrivial part is to show that it is stable under extensions, so let

$$
0 \to M ^ {\prime} \to M \to M ^ {\prime \prime} \to 0
$$

be a short exact sequence of$K ^ { \circ } .$-modules, with m$M ^ { \prime } = \mathfrak { m } M ^ { \prime \prime } = 0$. In general, one gets that${ \mathfrak { m } } ^ { 2 } M = 0$. But in our situation,${ \mathfrak { m } } ^ { 2 } = { \mathfrak { m } }$, so M is almost zero.

We note that there is a sequence of localization functors

$$
K ^ {\circ} - \mathrm{mod} \rightarrow K ^ {\circ} - \mathrm{mod} / (\mathfrak {m} - \text {torsion}) \rightarrow K - \mathrm{mod}.
$$

Their composite is the functor of passing from an integral structure to its generic fibre. In this sense, the category in the middle can be seen as a slightly generic fibre, or as an almost integral structure. It will turn out that in perfectoid situations, properties and objects over the generic fibre will extend automatically to the slightly generic fibre, in other words the generic fibre almost determines the integral level. It will be easy to justify this philosophy if K has characteristic p, by using the following argument. Assume that some statement is true over K. By using some finiteness property, it follows that there is some big N such that it is true up to$\varpi ^ { N }$-torsion. But Frobenius is bijective, hence the property stays true up to$\varpi ^ { N / p } .$-torsion. Now iterate this argument to see that it is true up to$\dot { \varpi } ^ { N / p ^ { m } }$-torsion for all$m _ { \colon }$, i.e. almost true.

Following these ideas, our proof of Theorem 3.7 will proceed as follows, using the subscript f´et to denote categories of finite ´etale (almost) algebras.

$$
K _ {\mathrm{fét}} \cong K _ {\mathrm{fét}} ^ {\circ a} \cong (K ^ {\circ a} / \varpi) _ {\mathrm{fét}} = (K ^ {\flat \circ a} / \varpi^ {\flat}) _ {\mathrm{fét}} \cong K _ {\mathrm{fét}} ^ {\flat \circ a} \cong K _ {\mathrm{fét}} ^ {\flat}.
$$

Our principal aim in this section is to define all intermediate categories.

Definition 4.3. Define the category of almost$K ^ { \circ }$-modules as

$$
K ^ {\circ a} - \mathrm{mod} = K ^ {\circ} - \mathrm{mod} / (\mathfrak {m} - \text {torsion}).
$$

In particular, there is a localization functor$M \mapsto M ^ { a }$from$K ^ { \circ } - { \bmod { } }$to$K ^ { \circ a } - { \mathrm { m o d } }$1, whose kernel is exactly the thick subcategory of almost zero modules.

Proposition 4.4 ([14, §2.2.2]). Let M, N be two$K ^ { \circ }$-modules. Then

$$
\operatorname{Hom} _ {K ^ {\circ a}} \left(M ^ {a}, N ^ {a}\right) = \operatorname{Hom} _ {K ^ {\circ}} \left(\mathfrak {m} \otimes M, N\right).
$$

In particular, Hom$K ^ { \circ a } \left( X , Y \right)$has a natural structure of$K ^ { \circ }$-module for any two$K ^ { \circ a }$ modules X and Y. The module Hom$\operatorname { \delta } _ { K ^ { \circ a } } ( X , Y )$has no almost zero elements.

For two$K ^ { \circ a }$-modules M, N, we define alHom$( X , Y ) = \operatorname { H o m } ( X , Y ) ^ { a }$

Proposition 4.5 ([14, §2.2.6, §2.2.12]). The category$K ^ { \circ a } -$mod is an abelian tensor category, where we define kernels, cokernels and tensor products in the unique way compatible with their definition in$K ^ { \circ } -$mod,$e . g$

$$
M ^ {a} \otimes N ^ {a} = (M \otimes N) ^ {a}
$$

for any two$K ^ { \circ }$-modules M, N. For any three$K ^ { \circ a }$-modules$L , M , N$, there is a functorial isomorphism

$$
\operatorname{Hom} (L, \operatorname{alHom} (M, N)) = \operatorname{Hom} (L \otimes M, N) .
$$

This means that$K ^ { \circ a } -$mod has all abstract properties of the category of modules over a ring. In particular, one can define in the usual abstract way the notion of a $K ^ { \circ a }$-algebra. For any$K ^ { \circ a }$-algebra A, one also has the notion of an A-module. Any$K ^ { \circ } -$ algebra R defines a$K ^ { \circ a }$-algebra$R ^ { a }$, as the tensor products are compatible. Moreover, localization also gives a functor from R-modules to$R ^ { a }$-modules. For example,$K ^ { \circ }$ gives the$K ^ { \circ a }$-algebra$A = K ^ { \circ a }$, and then A-modules are$K ^ { \circ a }$-modules, so that the terminology is consistent.

Proposition 4.6 ([14, Proposition 2.2.14]). There is a right adjoint

$$
K ^ {\circ a} - \mathrm{mod} \rightarrow K ^ {\circ} - \mathrm{mod}: M \mapsto M _ {*}
$$

to the localization functor$M \mapsto M ^ { a }$, given by the functor of almost elements

$$
M _ {*} = \operatorname{Hom} _ {K ^ {\circ a}} (K ^ {\circ a}, M).
$$

The adjunction morphism$( M _ { * } ) ^ { a } \to M$is an isomorphism. If M is a$K ^ { \circ }$-module, then $( M ^ { a } ) _ { * } = \operatorname { H o m } ( \mathfrak { m } , M )$

If A is a$K ^ { \circ a }$-algebra, then$A _ { * }$has a natural structure as$K ^ { \circ } { \mathrm { - a l g e b r a } }$and$A _ { * } ^ { a } = A$ In particular, any$K ^ { \circ a }$-algebra comes via localization from a$K ^ { \circ } { \mathrm { - a l g e b r a } }$. Moreover, the functor$M \mapsto M ,$<sub>∗</sub> induces a functor from A-modules to A<sub>∗</sub>-modules, and one sees that also all A-modules come via localization from$A _ { * }$-modules. We note that the category of A-modules is again an abelian tensor category, and all properties about the category of$K ^ { \circ a }$-modules stay true for the category of A-modules. We also note that one can equivalently define A-algebras as algebras over the category of A-modules, or as$K ^ { \circ a } .$ algebras B with an algebra morphism$A  B$

Finally, we need to extend some notions from commutative algebra to the almost context.

Definition/Proposition 4.7. Let A be any$K ^ { \circ a } - a l g e b r a$

(i) An A-module M is flat if the functor$X \mapsto M \otimes _ { A } X$on A-modules is exact. If R is a $K ^ { \circ } { \circ } _ { - a l g }$ebra and N is an R-module, then the R<sup>a</sup>-module$N ^ { a }$is flat$i f$and only if for all R-modules X and all$i > 0$, the module$\mathrm { T o r } _ { i } ^ { R } ( N , X )$is almost zero.

(ii) An A-module M is almost projective if the functor$X \mapsto$alHom$_ A ( M , X )$on Amodules is exact. If R is a$K ^ { \circ }$-algebra and N is an R-module, then$N ^ { a }$is almost projective over$R ^ { a }$if and only if for all R-modules X and all$i > 0$, the module$\mathrm { E x t } _ { R } ^ { i } ( N , X )$ is almost zero.

(iii) If R is a K<sup>◦</sup>-algebra and N is an R-module, then$M = N ^ { a }$is said to be an almost finitely generated (resp. almost finitely presented)$R ^ { a }$-module if and only if for all$\epsilon \in$ m, there is some finitely generated (resp. finitely presented) R-module$N _ { \epsilon }$with a map $f _ { \epsilon } : N _ { \epsilon } \to N$such that the kernel and cokernel of$f _ { \epsilon }$are annihilated by . We say that M is uniformly almost finitely generated if there is some integer n such that$N _ { \epsilon }$can be chosen to be generated by n elements, for all .

Proof. For parts (i) and (ii), cf. [14], Definition 2.4.4, §2.4.10 and Remark 2.4.12 (i). For part (iii), cf. [14], Definition 2.3.8, Remark 2.3.9 (i) and Corollary 2.3.13.

Remark 4.8. In (iii), we make the implicit statement that this property depends only on the$R ^ { a }$-module$N ^ { a }$. There is also the categorical notion of projectivity saying that the functor$X \mapsto \operatorname { H o m } ( M , X )$is exact, but not even$K ^ { \circ a }$itself is projective in general: One can check that the map

$$
K ^ {\circ} = \operatorname{Hom} (K ^ {\circ a}, K ^ {\circ a}) \to \operatorname{Hom} (K ^ {\circ a}, K ^ {\circ a} / \varpi) = \operatorname{Hom} (\mathfrak {m}, K ^ {\circ} / \varpi)
$$

is in general not surjective, as the latter group contains sums of the form

$$
\sum_ {i \geq 0} \varpi^ {1 - 1 / p ^ {i}} x _ {i}
$$

for arbitrary$x _ { i } \in K ^ { \circ } / \varpi$

Example 4.9. As an example of an almost finitely presented module, consider the case that K is the p-adic completion of$\mathbb { Q } _ { p } ( p ^ { 1 / p ^ { \infty } } ) , ~ p ~ \neq ~ 2$. Consider the extension$L =$ $K ( p ^ { 1 / 2 } )$. Then$L ^ { \circ a }$is an almost finitely presented$K ^ { \circ a }$-module. Indeed, for any$n \geq 1$，we have injective maps

$$
K ^ {\circ} \oplus p ^ {1 / 2 p ^ {n}} K ^ {\circ} \to L ^ {\circ}
$$

whose cokernel is killed by$p ^ { 1 / 2 p ^ { n } }$. In fact, in this example$L ^ { \circ a }$is even uniformly almost finitely generated.

Proposition 4.10 ([14, Proposition 2.4.18]). Let A be a$K ^ { \circ a }$-algebra. Then an Amodule M is flat and almost finitely presented if and only if it is almost projective and almost finitely generated.

By abuse of notation, we call such A-modules M finite projective in the following, a terminology not used in [14]. If additionally, M is uniformly almost finitely generated, we say that M is uniformly finite projective.

For uniformly finite projective modules, there is a good notion of rank.

Theorem 4.11 ([14, Proposition 4.3.27, Remark 4.3.10 (i)]). Let A be a$K ^ { \circ a } - a l g e b r a$ and let M be a uniformly finite projective A-module. Then there is a unique decomposition$A = A _ { 0 } \times A _ { 1 } \times \cdot \cdot \cdot \times A _ { k }$such that for each$i = 0 , \ldots , k$, the$A _ { i } .$-module$M _ { i } = M \otimes _ { A } A _ { i }$ has the property that$\textstyle \bigwedge ^ { i } M _ { i }$is invertible, and$\Lambda ^ { i + 1 } M _ { i } = 0$. Here, an A-module L is called invertible if$L \otimes A$alHom$_ A ( L , A ) = A$

Finally, we need the notion of ´etale morphisms.

Definition 4.12. Let A be a$K ^ { \circ a } - a l g e b r a$, and let B be an A-algebra. Let$\mu : B \otimes _ { A } B \to$ B denote the multiplication morphism.

(i) The morphism$A  B$is said to be unramified if there is some element$e \in ( B \otimes _ { A } B )$∗ such that$e ^ { 2 } = e , \mu ( e ) = 1$and$x e = 0$for all$x \in \ker ( \mu ) _ { * }$

(ii) The morphism$A  B$is said to be ´etale if it is unramified and B is a flat A-module.

We note that the definition of unramified morphisms basically says that the diagonal morphism$\mu : B \otimes _ { A } B \to B$is a closed immersion in the geometric picture.

In the following, we will be particularly interested in almost finitely presented ´etale maps.

Definition 4.13. A morphism$A  B$of$K ^ { \circ a }$-algebras is said to be finite ´etale if it is ´etale and B is an almost finitely presented A-module. Write$A _ { \mathrm { { f e t } } }$for the category of finite ´etale A-algebras.

We note that in this case B is a finite projective A-module. Also, this terminology is not used in [14], but we feel that it is the appropriate almost analogue of finite ´etale covers.

There is an equivalent characterization of finite ´etale morphisms in terms of trace morphisms. If A is any$K ^ { \circ a }$-algebra, and$P$is some finite projective A-module, we define

$P ^ { * } = \mathrm { a l H o m } ( P , A )$, which is a finite projective A-module again. Moreover,$P ^ { * * } \cong P$ canonically, and there is an isomorphism

$$
\operatorname{End} (P) ^ {a} = P \otimes_ {A} P ^ {*}.
$$

In particular, one gets a trace morphism t$\cdot _ { P / A } : { \mathrm { E n d } } ( P ) ^ { a } \to A$

Definition 4.14. Let A be a$K ^ { \circ a }$-algebra, and let B be an A-algebra such that B is a finite projective A-module. Then we define the trace form as the bilinear form

$$
t _ {B / A}: B \otimes_ {A} B \to A
$$

given by the composition of$\mu : B \otimes _ { A } B \to B$and the map$B  A$sending any$b \in B$to the trace of the endomorphism$b ^ { \prime } \mapsto b b ^ { \prime } \ o f \ B$

Remark 4.15. We should remark that the latter definition does not literally make sense, as one can not talk about an element b of some almost object B: There is no underlying set. However, one can define a map$B _ { * } \to \operatorname { E n d } _ { A _ { * } } ( B _ { * } )$in the way described, and we are considering the corresponding map of almost objects$B  \operatorname { E n d } _ { A _ { * } } ( B _ { * } ) ^ { a } = \operatorname { E n d } _ { A } ( B ) ^ { a }$

Theorem 4.16 ([14, Theorem 4.1.14]). In the situation of the definition, the morphism $A  B$is finite ´etale if and only if the trace map is a perfect pairing, i.e. induces an isomorphism$B \cong B ^ { * }$

An important property is that finite ´etale covers lift uniquely over nilpotents.

Theorem 4.17. Let A be a$K ^ { \circ a }$-algebra. Assume that A is flat over$K ^ { \circ a }$and \$-adically complete, i.e.

$$
A \cong \varprojlim A / \varpi^ {n}.
$$

Then the functor$B \mapsto B \otimes _ { A } A / \varpi$induces an equivalence of categories$A _ { \mathrm { { f } \acute { e } t } } \cong ( A / \varpi ) _ { \mathrm { { f } \acute { e } t } }$ Any$B \in A _ { \mathrm { f e t } }$is again flat over$K ^ { \circ a }$and \$-adically complete. Moreover, B is a uniformly finite projective A-module if and only if$B \otimes _ { A } A /$\$ is a uniformly finite projective $A / \varpi \ – m o d u l e .$

Proof. The first part follows from [14], Theorem 5.3.27. The rest is easy.

Recall that we wanted to prove the string of equivalences

$$
K _ {\mathrm{fét}} \cong K _ {\mathrm{fét}} ^ {\circ a} \cong (K ^ {\circ a} / \varpi) _ {\mathrm{fét}} = (K ^ {\flat \circ a} / \varpi^ {\flat}) _ {\mathrm{fét}} \cong K _ {\mathrm{fét}} ^ {\flat \circ a} \cong K _ {\mathrm{fét}} ^ {\flat} .
$$

The identification in the middle is tautological as$K ^ { \circ } / \varpi = K ^ { \flat \circ } / \varpi ^ { \flat }$<sup>[</sup>, and the corresponding almost settings agree. The previous theorem shows that the inner two functors are equivalences. For the other two equivalences, we feel that it is more convenient to study them in the more general setup of perfectoid K-algebras.

## 5. Perfectoid algebras

Fix a perfectoid field K.

Definition 5.1. (i) A perfectoid K-algebra is a Banach K-algebra R such that the subset $R ^ { \circ } \subset R$of powerbounded elements is open and bounded, and the Frobenius morphism $\Phi : R ^ { \circ } / \varpi  R ^ { \circ } / \varpi$is surjective. Morphisms between perfectoid K-algebras are the continuous morphisms of K-algebras.

(ii) A perfectoid$K ^ { \circ a }$-algebra is$a \ { \varpi } { - } a d i c a l l y$complete flat$K ^ { \circ a }$-algebra A on which Frobenius induces an isomorphism

$$
\Phi : A / \varpi^ {\frac {1}{p}} \cong A / \varpi .
$$

Morphisms between perfectoid$K ^ { \circ a }$-algebras are the morphisms of$K ^ { \circ a }$-algebras.

(iii) A perfectoid$K ^ { \circ a } / \varpi { - } a l g e b r a$is a flat K<sup>◦a</sup>/\$-algebra$\overline { { A } }$on which Frobenius induces an isomorphism

$$
\Phi : \overline {{A}} / \varpi^ {\frac {1}{p}} \cong \overline {{A}}.
$$

Morphisms are the morphisms of$K ^ { \circ a } / \varpi \ – a l g e b r a s$

Let K−Perf denote the category of perfectoid K-algebras, and similarly for$K ^ { \circ a } { \mathrm { - P e r f } }$8... . Let$K ^ { \flat }$be the tilt of K. Then the main theorem of this section is the following.

Theorem 5.2. The categories of perfectoid K-algebras and perfectoid$K ^ { \flat } - a l g e b r a s$are equivalent. In$f a c t ,$we have the following series of equivalences of categories.

$$
K - \mathrm{Perf} \cong K ^ {\circ a} - \mathrm{Perf} \cong (K ^ {\circ a} / \varpi) - \mathrm{Perf} = (K ^ {\flat \circ a} / \varpi^ {\flat}) - \mathrm{Perf} \cong K ^ {\flat \circ a} - \mathrm{Perf} \cong K ^ {\flat} - \mathrm{Perf}
$$

In other words, a perfectoid K-algebra, which is an object over the generic fibre, has a canonical extension to the almost integral level as a perfectoid$K ^ { \circ a } { \mathrm { - a l g e b r a } } .$, and perfectoid$K ^ { \circ a }$-algebras are determined by their reduction modulo$\varpi$

The following lemma expresses the conditions imposed on a perfectoid$K ^ { \circ a }$-algebra in terms of classical commutative algebra.

Lemma 5.3. Let M be a$K ^ { \circ a }$-module.

(i) The module M is flat over$K ^ { \circ a }$if and only if M<sub>∗</sub> is flat over$K ^ { \circ }$if and only if$M _ { * }$ has no \$-torsion.

(ii) If N is a flat K<sup>◦</sup>-module and$M \ = \ N ^ { a }$, then M is flat over$K ^ { \circ a }$and we have $\begin{array} { r } { M _ { * } = \{ x \in N [ \frac { 1 } { \varpi } ] ~ | ~ \forall \epsilon \in \mathfrak { m } : \epsilon x \in N \} } \end{array}$

(iii) If M is flat over$K ^ { \circ a }$, then for all$x \in K ^ { \circ }$, we have$( x M ) _ { * } = x M _ { * }$. Moreover, $M _ { * } / x M _ { * } \subset ( M / x M ) _ { * }$, and for all$\epsilon \in { \mathfrak { m } }$the image of$( M / x \epsilon M )$in$( M / x M )$<sub>∗</sub> is equal to$M _ { * } / x M _ { * }$

(iv) If M is flat over$K ^ { \circ a }$, then M is \$-adically complete if and only if M is \$-adically complete.

Remark 5.4. The non-surjectivity in (iii) is due to elements as in Remark 4.8.

Proof. (i) By definition, M is a flat$K ^ { \circ a }$-module if and only if all$\mathrm { T o r } _ { i } ^ { K ^ { \circ } } ( M _ { * } , N )$are almost zero for all$i > 0$and all K<sup>◦</sup>-modules N. Hence if$M _ { * }$is a flat$K ^ { \circ } { \mathrm { - m o d u l e } } ,$then M is a flat$K ^ { \circ a }$-module. Conversely, choosing$N = K ^ { \circ } / \varpi$and$i = 1$, we find that the kernel of multiplication by$\varpi$on$M _ { * }$is almost zero. But

$$
M _ {*} = \operatorname{Hom} _ {K ^ {\circ a}} (K ^ {\circ a}, M) = \operatorname{Hom} _ {K ^ {\circ}} (\mathfrak {m}, M _ {*})
$$

does not have nontrivial almost zero elements, hence has no \$-torsion. But a$K ^ { \circ }$-module $N$is flat if and only if it has no \$-torsion.

(ii) We have

$$
M _ {*} = \operatorname{Hom} _ {K ^ {\circ a}} (K ^ {\circ a}, M) = \operatorname{Hom} _ {K ^ {\circ}} (\mathfrak {m}, N).
$$

As N is flat over$K ^ { \circ }$, we can write the last term as the subset of those$x \in { \mathrm { H o m } } _ { K } ( K , N [ { \frac { 1 } { \varpi } } ] ) =$ $N [ \textstyle { \frac { 1 } { \varpi } } ]$satisfying the condition that for all$\epsilon \in { \mathfrak { m } }$, we have$\epsilon x \in N$

(iii) Note that$( x M _ { * } ) ^ { a } = x M _ { ! }$, and$x M _ { * }$is a flat$K ^ { \circ }$-module. Hence

$$
(x M) _ {*} = \mathrm{Hom} (\mathfrak {m}, x M _ {*}) = \left\{y \in M _ {*} [ \frac {1}{\varpi} ] \mid \forall \epsilon \in \mathfrak {m}: \epsilon y \in x M _ {*} \right\} = x M _ {*}.
$$

Now using that is left-exact (since right-adjoint to$M \mapsto M ^ { a } )$, we get the inclusion $M _ { * } / x M _ { * } \subset ( M / x M ) _ { * }$. If$m \in ( M / x M )$.lifts to$\tilde { m } \in ( M / x \epsilon M ) _ { * }$, then evaluate$\tilde { m } \in$ Hom$( \mathfrak { m } , M _ { * } / x \epsilon M _ { * } )$on . This gives an element$n = \tilde { m } ( \epsilon ) \in M _ { * } / x \epsilon M _ { * }$, which we lift to $\tilde { n } \in M _ { * }$. One checks that ˜n is divisible by : It sufices to check that δn˜ is divisible by  for any$\delta \in { \mathfrak { m } }$. But$\delta \boldsymbol { n } = \delta \tilde { m } ( \epsilon ) = \epsilon \tilde { m } ( \delta )$lies in$\epsilon M _ { * } / x \epsilon M _ { * }$, hence$\delta \tilde { n } \in \epsilon M _ { * }$

Then$\begin{array} { r } { m _ { 1 } = \frac { \tilde { n } } { \epsilon } \in M _ { * } } \end{array}$is the desired lift of$m \in ( M / x M ) _ { * }$: Multiplication by  induces an injection$( { \cal M } / x { \cal M } ) _ { * }  ( { \cal M } / x \epsilon { \cal M } ) _ { * }$, because is left-exact, and the images agree: ˜n maps to$\epsilon m = \tilde { m } ( \epsilon ) = n$in$( M / x \epsilon M ) ,$<sub>∗</sub>.

(iv) The functors$M \mapsto M _ { * }$and$N \mapsto N ^ { a }$between the category of$K ^ { \circ a }$-modules and the category of$K ^ { \circ }$-modules admit left adjoints, given by$N \mapsto N ^ { a }$and$M \mapsto M _ { ! } = \mathfrak { m } \otimes M _ { * }$，respectively, and hence commute with inverse limits. Now if M is \$-adically complete, then

$$
M _ {*} = (\varprojlim M / \varpi^ {n} M) _ {*} = \varprojlim (M / \varpi^ {n} M) _ {*} = \varprojlim M _ {*} / \varpi^ {n} M _ {*}
$$

using part (iii) in the last equality, hence$M _ { * }$is \$-adically complete. Conversely, if$M _ { * }$ is \$-adically complete, then

$$
M = (M _ {*}) ^ {a} = (\varprojlim M _ {*} / \varpi^ {n} M _ {*}) ^ {a} = \varprojlim (M _ {*} / \varpi^ {n} M _ {*}) ^ {a} = \varprojlim M / \varpi^ {n} M.
$$

Proposition 5.5. Let R be a perfectoid K-algebra. Then Φ induces an isomorphism $R ^ { \circ } / \varpi ^ { 1 / p } \cong R ^ { \circ } / \varpi$, and$A = R ^ { \circ a }$is a perfectoid$K ^ { \circ a } - a l g e b r a$

Proof. By assumption, Φ is surjective. Injectivity is clear: If$x \in R ^ { \circ }$is such that$x ^ { p } / \varpi$ is powerbounded, then$x / \varpi ^ { 1 / p }$is powerbounded. Obviously,$R ^ { \circ }$is \$-adically complete and flat over$K ^ { \circ }$; now the previous lemma shows that$R ^ { \circ a }$is \$-adically complete and flat over$K ^ { \circ a }$

Lemma 5.6. Let A be a perfectoid$K ^ { \circ a }$-algebra, and let$R = A _ { * } [ \varpi ^ { - 1 } ]$. Equip R with the Banach K-algebra structure making A open and bounded. Then$A _ { * } = R ^ { \circ }$is the set of power-bounded elements, R is perfectoid, and

$$
\Phi : A _ {*} / \varpi^ {1 / p} \cong A _ {*} / \varpi .
$$

Proof. By definition, Φ is an isomorphism$A / \varpi ^ { 1 / p } \cong A / \varpi .$, hence Φ is an almost isomorphism$A _ { * } / \varpi ^ { 1 / p } \to A _ { * } / \varpi$. It is injective: If$x \in A _ { * }$and$x ^ { p } \in \varpi A _ { * }$, then for all$\epsilon \in { \mathfrak { m } } .$7 $\epsilon x \in \varpi ^ { 1 / p } A _ { * }$by almost injectivity, hence$x \in ( \varpi ^ { 1 / p } A ) _ { * } = \varpi ^ { 1 / p } A _ { * }$

Lemma 5.7. Assume that$x \in R$satisfies$x ^ { p } \in A _ { * }$. Then x$\in A _ { * }$

Proof. Injectivity of Φ says that if$y \in A _ { * }$satisfies$y ^ { p } \in \varpi A _ { * }$, then$y \in \varpi ^ { \frac { 1 } { p } } A _ { * }$. There is 1 some positive integer k such that$y = \varpi ^ { \frac { \kappa } { p } } x \in A _ { * }$, and as long as$k \geq 1 , y ^ { p } \in \varpi A _ { * }$, so that$y \in \varpi ^ { \frac { 1 } { p } } A _ { * }$. Because$A _ { * }$has no \$-torsion, we get$\varpi ^ { \frac { \ d S } { p } } x \in A _ { * }$k−1. By induction, we get the result.

Obviously,$A _ { * }$consists of power-bounded elements. Now assume that$x \in R$is powerbounded. Then x is topologically nilpotent for all$\epsilon \in { \mathfrak { m } }$. In particular,$( \epsilon x ) ^ { p ^ { N } } \in A _ { * }$for $N$suficiently large. By the last lemma, this implies$\epsilon x \in A _ { * }$. This is true for all$\epsilon \in { \mathfrak { m } }$, so that by Lemma 5.3 (ii), we have$x \in A _ { * }$

Next, Φ is surjective: It is almost surjective, hence it sufices to show that the composition$A _ { * } / \varpi ^ { 1 / p }  A _ { * } / \varpi  A _ { * } / \mathfrak { m }$is surjective. Let$x \in A _ { * }$. By almost surjectivity, $\varpi ^ { 1 / p } x \equiv y ^ { p }$modulo$\varpi A _ { * }$, for some$y \in A _ { * }$. Let$\begin{array} { r } { z = \frac { y } { \varpi ^ { 1 / p ^ { 2 } } } } \end{array}$. This implies$z ^ { p } \equiv x$modulo $\varpi ^ { ( p - 1 ) / p } A _ { * }$, in particular$z ^ { p } \in A _ { * }$. By the lemma, also$z \in A _ { * }$. As$x \equiv z ^ { p }$modulo $\varpi ^ { ( p - 1 ) / p } A _ { * }$, in particular modulo${ \mathfrak { m } } A _ { * }$, this gives the desired surjectivity.

Finally, we see that R is Banach K-algebra such that$R ^ { \circ } = A _ { * }$is open and bounded, and such that Φ is surjective on$R ^ { \circ } / \varpi = A _ { * } / \varpi$. This means that R is perfectoid, as desired.

In particular, we get the desired equivalence$K ^ { \circ a } - { \mathrm { P e r f } } \cong K - { \mathrm { P e r f } }$. Let us note some further propositions.

Proposition 5.8. Let R be a perfectoid K-algebra. Then R is reduced.

Proof. Assume$0 \neq x \in R$is nilpotent. Then$K x \subset R ^ { \circ }$, contradicting the condition that $R ^ { \circ }$is bounded.

If K has characteristic$p ,$being perfectoid is basically the same as being perfect.

Proposition 5.9. Let K be of characteristic p, and let R be a Banach K-algebra such that the set of powerbounded elements$R ^ { \circ } \subset R$is open and bounded. Then R is perfectoid $i f$and only if R is perfect.

Proof. Assume R is perfect. Then also$R ^ { \circ }$is perfect, as an element x is powerbounded if and only if$x ^ { p }$is powerbounded. In particular,$\Phi : R ^ { \circ } / \varpi  R ^ { \circ } / \varpi$is surjective.

Now assume that R is perfectoid, hence by Proposition 5.5, Φ induces an isomorphism $R ^ { \circ } / \varpi ^ { \frac { 1 } { p } } \cong R ^ { \circ } / \varpi$. By successive approximation, we see that$R ^ { \circ }$is perfect, and then that R is perfect.

In order to finish the proof of Theorem 5.2, it sufices to prove the following result.

Theorem 5.10. The functor$A \mapsto { \overline { { A } } } = A / \varpi$induces an equivalence of categories $K ^ { \circ a } - \mathrm { P e r f } \cong ( K ^ { \circ a } / \varpi ) - \mathrm { P e r f }$

In other words, we have to prove that a perfectoid$K ^ { \circ a } / \varpi \mathrm { - a l g e b r a }$admits a unique deformation to$K ^ { \circ a }$. For this, we will use the theory of the cotangent complex. Let us briefly recall it here.

In classical commutative algebra, the definition of the cotangent complex is due to Quillen, [28], and its theory was globalized on toposes and applied to deformation prob lems by Illusie, [22], [23]. To any morphism$R \to S$of rings, one associates a complex $\mathbb { L } _ { S / R } \in D ^ { \le 0 } ( S )$, where$D ( S )$is the derived category of the category of S-modules, and $D ^ { \leq 0 } ( S ) \subset D ( S )$denotes the full subcategory of objects which have trivial cohomology in positive degrees. The cohomology in degree 0 of$\mathbb { L } _ { S / R }$is given by$\Omega _ { S / R } ^ { 1 } ,$and for any morphisms$R \to S \to T$of rings, there is a triangle in$D ( T )$

$$
T \otimes_ {S} ^ {\mathbb {L}} \mathbb {L} _ {S / R} \to \mathbb {L} _ {T / R} \to \mathbb {L} _ {T / S} \to ,
$$

extending the short exact sequence

$$
T \otimes_ {S} \Omega_ {S / R} ^ {1} \to \Omega_ {T / R} ^ {1} \to \Omega_ {T / S} ^ {1} \to 0.
$$

Let us briefly recall the construction. First, one uses the Dold-Kan equivalence to reinterpret$D ^ { \leq 0 } ( S )$as the category of simplicial S-modules modulo weak equivalence. Now one takes a simplicial resolution$S _ { \bullet }$of the R-algebra S by free R-algebras. Then one defines$\mathbb { L } _ { S / R }$as the object of$D ^ { \leq 0 } ( S )$associated to the simplicial S-module$\Omega _ { S _ { \bullet } / R } ^ { 1 } \otimes _ { S _ { \bullet } } S$

Just as under certain favorable assumptions, one can describe many deformation problems in terms of tangent or normal bundles, it turns out that in complete generality, one can describe them via the cotangent complex. In special cases, this gives back the classical results, as e.g. if$R \to S$is a smooth morphism, then$\mathbb { L } _ { S / R }$is concentrated in degree 0, and is given by the cotangent bundle.

Specifically, we will need the following results. Fix some ring R with an ideal$I \subset R$ such that$I ^ { 2 } = 0$. Moreover, fix a flat$R _ { 0 } = R / I { \mathrm { - a l g e b r a ~ } } S _ { 0 }$. We are interested in the obstruction towards deforming$S _ { 0 }$to a flat R-algebra S.

Theorem 5.11 ([22, III.2.1.2.3], [14, Proposition 3.2.9]). There is an obstruction class in$\mathrm { E x t } ^ { 2 } ( \mathbb { L } _ { S _ { 0 } / R _ { 0 } } , S _ { 0 } \otimes _ { R _ { 0 } } I )$which vanishes precisely when there exists a flat R-algebra $S$such that$S \otimes _ { R } R _ { 0 } = S _ { 0 }$. If there exists such a deformation, then the set of all isomorphism classes of such deformations forms a torsor under$\mathrm { E x t } ^ { 1 } ( \mathbb { L } _ { S _ { 0 } / R _ { 0 } } , S _ { 0 } \otimes _ { R _ { 0 } } I )$ and every deformation has automorphism group Hom$( \mathbb { L } _ { S _ { 0 } / R _ { 0 } } , S _ { 0 } \otimes _ { R _ { 0 } } I )$

Here, a deformation comes with the isomorphism$S \otimes _ { R } R _ { 0 } \cong S _ { 0 }$, and isomorphisms of deformations are required to act trivially on$S \otimes _ { R } R _ { 0 } = S _ { 0 }$

Now assume that one has two flat R-algebras$S , S ^ { \prime }$with reduction$S _ { 0 } , S _ { 0 } ^ { \prime }$to$R _ { 0 }$, and a morphism$f _ { 0 } : S _ { 0 } \to S _ { 0 } ^ { \prime }$. We are interested in the obstruction to lifting$f _ { 0 }$to a morphism $f : S  S ^ { \prime }$

Theorem 5.12 ([22, III.2.2.2], [14, Proposition 3.2.16]). There is an obstruction class in$\mathrm { E x t } ^ { 1 } ( \mathbb { L } _ { S _ { 0 } / R _ { 0 } } , S _ { 0 } ^ { \acute { \prime } } \otimes _ { R _ { 0 } } I )$which vanishes precisely when there exists an extension of$f _ { 0 }$ to$f : S  { \dot { S } } ^ { \prime }$. If there exists such a$l i f t ,$, then the set of all lifts forms a torsor under Hom$( \mathbb { L } _ { S _ { 0 } / R _ { 0 } } , S _ { 0 } ^ { \prime } \otimes _ { R _ { 0 } } I )$

We will need the following criterion for the vanishing of the cotangent complex. This appears as Lemma 6.5.13 i) in [14].

Proposition 5.13. (i) Let R be a perfect$\mathbb { F } _ { p } .$-algebra. Then$\mathbb { L } _ { R / \mathbb { F } _ { p } } \cong 0$

(ii) Let$R \to S$be a morphism of$\mathbb { F } _ { p }$-algebras. Let$R _ { ( \Phi ) }$be the ring R with the R-algebra structure via$\Phi : R  R$, and define$S _ { ( \Phi ) }$similarly. Assume that the relative Frobenius $\Phi _ { S / R }$induces an isomorphism

$$
R _ {(\Phi)} \otimes_ {R} ^ {\mathbb {L}} S \to S _ {(\Phi)}
$$

in$D ( R )$. Then$\mathbb { L } _ { S / R } \cong 0$

Remark 5.14. Of course, (i) is a special case of (ii), and we will only need part (ii). However, we feel that (i) is an interesting statement that does not seem to be very well-known. It allows one to define the ring of Witt vectors$W ( R )$of R simply by saying that it is the unique deformation of R to a flat p-adically complete$\mathbb { Z } _ { p } { \mathrm { - a l g e b r a } }$. Also note that it is clear that$\Omega _ { R / \mathbb { F } _ { p } } ^ { 1 } = 0$in part (i): Any$x \in R$can be written as$y ^ { p }$, and then$d x = d y ^ { p } = p y ^ { p - 1 } d y = \dot { 0 }$. This identity is at the heart of this proposition.

Proof. We sketch the proof of part (ii), cf. proof of Lemma 6.5.13 i) in [14]. Let$S ^ { \bullet }$be a simplicial resolution of S by free R-algebras. We have the relative Frobenius map

$$
\Phi_ {S ^ {\bullet} / R}: R _ {(\Phi)} \otimes_ {R} S ^ {\bullet} \rightarrow S _ {(\Phi)} ^ {\bullet}.
$$

Note that identifying$S ^ { k }$with a polynomial algebra$R [ X _ { 1 } , X _ { 2 } , \ldots ]$, the relative Frobenius map$\Phi _ { S ^ { k } / R }$is given by the$R _ { ( \Phi ) } \mathrm { - a l g e b r a }$map sending$X _ { i } \mapsto X _ { i } ^ { p }$

The assumption says that$\Phi _ { S ^ { \bullet } / R }$induces a quasiisomorphism of simplicial$R _ { ( \Phi ) } -$ algebras. This implies that$\Phi _ { S ^ { \bullet } / R }$gives an isomorphism

$$
R _ {(\Phi)} \otimes_ {R} ^ {\mathbb {L}} \mathbb {L} _ {S / R} \cong \mathbb {L} _ {S _ {(\Phi)} / R _ {(\Phi)}}.
$$

On the other hand, the explicit description shows that the map induced by$\Phi _ { S ^ { k } / R }$on diferentials will map$d X _ { i }$to$d X _ { i } ^ { p } = 0$, and hence is the zero map. This shows that $\mathbb { L } _ { S _ { ( \Phi ) } / R _ { ( \Phi ) } } \cong 0$, and we may identify this with$\mathbb { L } _ { S / R }$

In their book [14], Gabber and Ramero generalize the theory of the cotangent complex to the almost context. Specifically, they show that if$R  S$is a morphism of$K ^ { \circ } \cdot$ algebras, then$\mathbb { L } _ { S / R } ^ { a }$as an element of$D ( S ^ { a } )$, the derived category of$S ^ { a }$-modules, depends only the morphism$R ^ { a }  S ^ { a }$of almost$K ^ { \circ }$-algebras. This allows one to define$\mathbb { L } _ { B / A } ^ { a } \in$ $D ^ { \leq 0 } ( B )$for any morphism$A  B$of$K ^ { \circ a }$-algebras. With this modification, the previous theorems stay true in the almost world without change.

Remark 5.15. In fact, the cotangent complex$\mathbb { L } _ { B / A }$is defined as an object of a derived category of modules over an actual ring in [14], but for our purposes it is enough to consider its almost version$\mathbb { L } _ { B / A } ^ { a } .$

Corollary 5.16. Let A be a perfectoid$K ^ { \circ a } / \varpi \ – a l g e b r a .$. Then$\mathbb { L } _ { \overline { { A } } / ( K ^ { \circ a } / \varpi ) } ^ { \underline { { a } } } \cong 0$

Proof. This follows from the almost version of Proposition 5.13, which can be proved in the same way. Alternatively, argue with$B = ( \overline { { A } } \times K ^ { \circ a } / \varpi ) _ { ! ! }$, which is a flat$K ^ { \circ } / \varpi -$ algebra such that$B / \varpi ^ { 1 / p } \cong B$via Φ. Here, we use the functor$C \mapsto C _ { ! ! }$from [14], §2.2.25.

Now we can prove Theorem 5.10.

Proof. (of Theorem 5.10) Let$\overline { { A } }$be a perfectoid$K ^ { \circ a } / \varpi \mathrm { - a l g e b r a }$. We see inductively that all obstructions and ambiguities in lifting inductively to a flat$( K ^ { \circ } / \varpi ^ { n } ) ^ { a }$-algebra ${ \overline { { A } } } _ { n }$vanish: All groups occuring can be expressed in terms of the cotangent complex by the theorems above, so that it sufices to show that$\mathbb { L } _ { \overline { { A } } _ { n } / ( K ^ { \circ } / \varpi ^ { n } ) ^ { a } } ^ { a } = 0$. But by Theorem 2.5.36 of [14], the short exact sequence

$$
0 \to \overline {{A}} \stackrel {\varpi^ {n - 1}} {\to} \overline {{A}} _ {n} \to \overline {{A}} _ {n - 1} \to 0
$$

induces after tensoring with$\mathbb { L } _ { \overline { { A } } _ { n } / ( K ^ { \circ } / \varpi ^ { n } ) ^ { a } }$a triangle

$$
\mathbb {L} \frac {a}{A} / (K ^ {\circ} / \varpi) ^ {a} \to \mathbb {L} \frac {a}{A _ {n}} / (K ^ {\circ} / \varpi^ {n}) ^ {a} \to \mathbb {L} \frac {a}{A _ {n - 1}} / (K ^ {\circ} / \varpi^ {n - 1}) ^ {a} \to ,
$$

and the claim follows by induction.

This gives a unique system of flat$( K ^ { \circ } / \varpi ^ { n } ) ^ { a } .$-algebras${ \overline { { A } } } _ { n }$with isomorphisms

$$
\overline {{A}} _ {n} / \varpi^ {n - 1} \cong \overline {{A}} _ {n - 1}.
$$

Let A be their inverse limit. Then A is \$-adically complete with$A / \varpi ^ { n } A = \overline { { A } } _ { n }$. This shows that A is perfectoid, and we get an equivalence between perfectoid$K ^ { \circ a }$-algebras and perfectoid$K ^ { \circ a } / \varpi \mathrm { - a l g e b r a s . }$, as desired.

In particular, we also arrive at the tilting equivalence,$K - \mathrm { P e r f } \cong K ^ { \flat } -$Perf. We want to compare this with Fontaine’s construction. Let R be a perfectoid K-algebra, with$A = R ^ { \circ a }$. Define

$$
A ^ {\flat} = \varprojlim_ {\Phi} A / \varpi ,
$$

which we regard as a$K ^ { \flat \circ a }$-algebra via

$$
K ^ {\flat \circ a} = (\varprojlim_ {\Phi} K ^ {\circ} / \varpi) ^ {a} = \varprojlim_ {\Phi} (K ^ {\circ} / \varpi) ^ {a} = \varprojlim_ {\Phi} K ^ {\circ a} / \varpi ,
$$

and set$R ^ { \flat } = A _ { * } ^ { \flat } [ ( \varpi ^ { \flat } ) ^ { - 1 } ]$

Proposition 5.17. This defines a perfectoid$K ^ { \flat } - a l g e b r a$$R ^ { \flat }$with corresponding perfectoid$K ^ { \flat \circ a } - a l g e b r a \ A ^ { \flat }$, and$R ^ { \flat }$is the tilt of R. Moreover,

$$
R ^ {\flat} = \varprojlim_ {x \mapsto x ^ {p}} R , A _ {*} ^ {\flat} = \varprojlim_ {x \mapsto x ^ {p}} A _ {*} , A _ {*} ^ {\flat} / \varpi^ {\flat} \cong A _ {*} / \varpi .
$$

In particular, we have a continuous multiplicative map$R ^ { \flat } \to R , x \mapsto x ^ { \sharp }$

Remark 5.18. It follows that the tilting functor is independent of the choice of$\varpi$and $\varpi ^ { \flat }$. We note that this explicit description comes from the fact that the lifting from perfectoid$K ^ { \flat \circ a } / \varpi ^ { \flat }$<sup>[</sup>-algebras to perfectoid$K ^ { \flat \circ a }$-algebras can be made explicit by means of the inverse limit over the Frobenius.

Proof. First, we have

$$
A _ {*} ^ {\flat} = (\varprojlim_ {\Phi} A / \varpi) _ {*} = \varprojlim_ {\Phi} (A / \varpi) _ {*} = \varprojlim_ {\Phi} A _ {*} / \varpi ,
$$

because <sub>∗</sub> commutes with inverse limits and using Lemma 5.3 (iii). Note that the image of$\Phi : ( A / \varpi ) _ { * } \to ( A / \varpi )$is$A _ { * } / \varpi$, because it factors over$( A / \varpi ^ { 1 / p } ) _ { * }$, and the image of the projection$( A / \varpi ) _ { * } \to ( A / \varpi ^ { 1 / p } ) .$<sub>∗</sub> is$A _ { * } / \varpi ^ { 1 / p }$. But

$$
\varprojlim_ {\Phi} A _ {*} / \varpi = \varprojlim_ {x \mapsto x ^ {p}} A _ {*},
$$

as in the proof of Lemma 3.4 (i).

This shows that$A _ { * } ^ { \flat }$is$\mathrm { ~ a ~ } \varpi ^ { \flat }$-adically complete flat$K ^ { \mathrm { { \circ } _ { - } } } \mathrm { { a l g e b r a } }$. Moreover, the projection$x \mapsto x ^ { \sharp }$of$A _ { * } ^ { \flat }$onto the first component$x ^ { \sharp } \in A ,$<sub>∗</sub> induces an isomorphism

$$
A _ {*} ^ {\flat} / \varpi^ {\flat} \cong A _ {*} / \varpi ,
$$

because of Lemma 5.6. Therefore$A ^ { \flat }$is a perfectoid$K ^ { \flat \circ a }$-algebra.

To see that$R ^ { \flat }$is the tilt of$R ,$we$_ \mathrm { g o }$through all equivalences. Indeed, R has corresponding perfectoid$K ^ { \circ a }$-algebra A, which reduces to the perfectoid$K ^ { \circ a } / \varpi \mathrm { - a l g e b r a }$ $A / \varpi$, which is the same as the perfectoid$K ^ { \flat \circ a } / \varpi ^ { \flat }$<sup>[</sup>-algebra$A ^ { \flat } / \varpi ^ { \flat }$, which lifts to the perfectoid$K ^ { \flat \circ a }$-algebra$A ^ { \flat } .$, which in turn gives rise to$R ^ { \flat }$

Remark 5.19. In fact, one can write down the functors in both directions. From characteristic 0 to characteristic$p ,$we have already given the explicit functor. The converse functor is given by$R = W ( R ^ { \flat \circ } ) \otimes _ { W ( K ^ { \flat \circ } ) } K$, using the usual map$\theta : W ( K ^ { \flat \circ } ) \to K$ We leave it as an exercise to the reader to give a direct proof of the theorem via this description, cf. [27]. This avoids the use of almost mathematics in the proof of the tilting equivalence. We stress however that in our proof we never need to talk about big rings like$W ( R ^ { \flat \circ } )$, and that the point of view of the given proof will be useful in later arguments.

Let us give a prototypical example for the tilting process.

Proposition 5.20. Let

$$
R = K \langle T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} \rangle = K ^ {\circ} [ T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} ] [ \varpi^ {- 1} ] .
$$

Then R is a perfectoid K-algebra, and its tilt$R ^ { \flat }$<sup>[</sup> is given by$K ^ { \flat } \langle T _ { 1 } ^ { 1 / p ^ { \infty } } , \ldots , T _ { n } ^ { 1 / p ^ { \infty } } \rangle$

Proof. One checks that$R ^ { \circ } = K ^ { \circ } [ T _ { 1 } ^ { 1 / p ^ { \infty } } , \dots , T _ { n } ^ { 1 / p ^ { \infty } } ]$, which is \$-adically complete and flat over$K ^ { \circ }$. Moreover, it reduces to$R ^ { \circ } / \varpi = K ^ { \circ } / \varpi [ T _ { 1 } ^ { 1 / p ^ { \infty } } , \ldots , T _ { n } ^ { 1 / p ^ { \infty } } ]$, on which Frobenius is surjective. This shows that R is a perfectoid K-algebra.

To see that its tilt has the desired form, we only have to check that$R ^ { \circ } / \varpi = R ^ { \flat \circ } / \varpi ^ { \flat } ;$, by the proof of the tilting equivalence. But this is obvious.

We note that under the process of tilting, perfectoid fields are identified.

Lemma 5.21. Let R be a perfectoid K-algebra with tilt$R ^ { \flat }$. Then R is a perfectoid field $i f$and only if$R ^ { \flat }$is a perfectoid field.

Proof. Note that R is a perfectoid field if and only if it is a nonarchimedean field, i.e. its topology is induced by a rank-1-valuation. This valuation is necessarily given by the spectral norm

$$
\left| \left| x \right| \right| _ {R} = \inf \left\{\left| t \right| ^ {- 1} \mid t \in K ^ {\times}, t x \in R ^ {\circ} \right\}
$$

on R. It is easy to check that for$x \in R ^ { \flat }$, we have$\vert \vert x \vert \vert _ { R ^ { \flat } } = \vert \vert x ^ { \sharp } \vert \vert _ { R }$. In particular, if $| | \cdot | | _ { R }$is multiplicative, then so is$| | \cdot | | _ { R ^ { \flat } }$, i.e. if R is a perfectoid field, then so is$R ^ { \flat }$

Conversely, assume that$R ^ { \flat }$is a perfectoid field. We have to check that the spectral norm$| | \cdot | | _ { R }$on R is multiplicative. Let$x , y \in R ;$after multiplication by elements of$K _ { i }$ we may assume$x , y \in R ^ { \circ }$, but not in$\varpi ^ { 1 / p } R ^ { \circ }$. We want to see that$| | x | | _ { R } | | y | | _ { R } = | | x y | | _ { R }$

But we can find$x ^ { \flat } , y ^ { \flat } \in R ^ { \flat \circ }$with$x - ( x ^ { \flat } ) ^ { \sharp } , y - ( y ^ { \flat } ) ^ { \sharp } \in \varpi R ^ { \circ }$. Then$\vert \vert x \vert \vert _ { R } = \vert \vert x ^ { \flat } \vert \vert _ { R ^ { \flat } }$7 $\vert \vert y \vert \vert _ { R } = \vert \vert y ^ { \flat } \vert \vert _ { R ^ { \flat } }$and$| | x y | | _ { R } = | | x ^ { \flat } y ^ { \flat } | | _ { R ^ { \flat } }$, and we get the claim.

To see that R is a field, choose x such that$x \in R ^ { \circ }$, but not in$\varpi R ^ { \circ }$, and take$x ^ { \flat }$as before. Then by multiplicativity of$| | \cdot | | _ { R } , | | 1 - \frac { x } { ( x ^ { \flat } ) ^ { \sharp } } | | _ { R } < 1$, and hence$\frac { x } { ( x ^ { \flat } ) ^ { \sharp } }$is invertible, and then also x.

Finally, let us discuss finite ´etale covers of perfectoid algebras, and finish the proof of Theorem 3.7.

Proposition 5.22. Let A be a perfectoid$K ^ { \circ a } / \varpi \ – a l g e b r a ,$and let$\overline { B }$be a finite ´etale A-algebra. Then B is a perfectoid$K ^ { \circ a } / \varpi { \cdot } a l g e b r a$

Proof. Obviously,$\overline { B }$is flat. The statement about Frobenius follows from Theorem 3.5.13 ii) of [14].

In particular, Theorem 4.17 provides us with the following commutative diagram, where$R , A , { \overline { { A } } } , A ^ { \flat }$and$R ^ { \flat }$form a sequence of rings under the tilting procedure.

![](images/page_27_image_6.jpg)

It follows from this diagram that the functors$A _ { \mathrm { { f e t } } } ~  ~ R _ { \mathrm { { f e t } } }$and$A _ { \mathrm { f e t } } ^ { \flat } \  \  R _ { \mathrm { f e t } } ^ { \flat }$are fully faithful. A main theorem is that both of them are equivalences: This amounts to Faltings’s almost purity theorem. At this point, we will prove this only in characteristic p.

Proposition 5.23. Let K be of characteristic p, let R be a perfectoid K-algebra, and let$S / R$be finite ´etale. Then S is perfectoid and$S ^ { \circ a }$is finite ´etale over$R ^ { \circ a }$. Moreover, $S ^ { \circ a }$is a uniformly finite projective$R ^ { \circ a } - m o d u l e .$

Remark 5.24. We need to define the topology on S here. Recall that if A is any ring with $t \in A$not a zero-divisor, then any finitely generated$A [ t ^ { - 1 } ]$-module M carries a canonical topology, which gives any finitely generated A-submodule of M the t-adic topology. Any morphism of finitely generated$\bar { A [ t ^ { - 1 } ] }$-modules is continuous for this topology, cf. [14], Definition 5.4.10 and 5.4.11. If A is complete and M is projective, then M is complete, as one checks by writing M as a direct summand of a finitely generated free A-module. In particular, if R is a perfectoid K-algebra and$S / R$a finite ´etale cover, then S has a canonical topology for which it is complete.

Proof. This follows from Theorem 3.5.28 of [14]. Let us recall the argument. Note that S is a perfect Banach K-algebra. We claim that it is perfectoid. Let$S _ { 0 } \subset S$be some finitely generated$R ^ { \circ }$-subalgebra with$S _ { 0 } \otimes K = S$. Let$S _ { 0 } ^ { \bot } \subset S$be defined as the set of all$x \in S$such that$t _ { S / R } ( x , S _ { 0 } ) \subset R ^ { \circ }$, using the perfect trace form pairing

$$
t _ {S / R}: S \otimes_ {R} S \to R;
$$

then$S _ { 0 }$and$S _ { 0 } ^ { \perp }$are open and bounded. Let Y be the integral closure of$R ^ { \circ }$in S. Then $S _ { 0 } \subset Y \subset S _ { 0 } ^ { \perp } ;$: Indeed, the elements of$S _ { 0 }$are clearly integral over$R ^ { \circ }$, and we have $t _ { S / R } ( Y , Y ) \subset \mathsf { \bar { R } } ^ { \circ }$. It follows that$Y$is open and bounded. As$S ^ { \circ a } = Y ^ { a }$, it follows that $S ^ { \acute { \circ } }$is open and bounded, as desired.

Next, we want to check that$S ^ { \circ a }$is a uniformly finite projective$R ^ { \circ a }$-module. For this, it is enough to prove that there is some n such that for any$\epsilon \in { \mathfrak { m } }$, there are maps $S ^ { \circ }  R ^ { \circ n }$and$R ^ { \circ n } \to S ^ { \circ }$whose composite is multiplication by .

Let$e \in S \otimes _ { R } S$be the idempotent showing that S is unramified over R. Then${ \varpi ^ { N } } _ { e }$ is in the image of$S ^ { \circ } \otimes _ { R ^ { \circ } } S ^ { \circ }$in$S \otimes _ { R } S$for some$N .$. Write$\begin{array} { r } { \varpi ^ { N } e = \sum _ { i = 1 } ^ { n } x _ { i } \otimes y _ { i } } \end{array}$. As

Frobenius is bijective, we have$\begin{array} { r } { \varpi ^ { N / p ^ { m } } e = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 1 / p ^ { m } } \otimes y _ { i } ^ { 1 / p ^ { m } } } \end{array}$for all m. In particular, for any$\epsilon \in { \mathfrak { m } }$, we can write$\begin{array} { r } { \epsilon e = \sum _ { i = 1 } ^ { n } a _ { i } \otimes \overline { { b _ { i } } } } \end{array}$for certain$a _ { i } , b _ { i } \in S ^ { \circ }$, depending on .

$$
S ^ {\circ} \to R ^ {\circ n}
$$

$$
s \mapsto (t _ {S / R} (s, b _ {1}), \ldots , t _ {S / R} (s, b _ {n})) ,
$$

and the map$R ^ { \circ n } \to S ^ { \circ }$2

$$
(r _ {1}, \dots , r _ {n}) \mapsto \sum_ {i = 1} ^ {n} a _ {i} r _ {i}.
$$

One easily checks that their composite is multiplication by , giving the claim.

It remains to see that$S ^ { \circ a }$is an unramified$R ^ { \circ a } { \mathrm { - a l g e b r a } }$. But this follows from the previous arguments, which show that e defines an almost element of$S ^ { \circ a } \otimes _ { R ^ { \circ a } } S ^ { \circ a }$with the desired properties.

It follows that the diagram above extends as follows.

![](images/page_28_image_8.jpg)

Moreover, using Theorem 4.17, it follows that all finite ´etale algebras over$A , { \overline { { A } } }$or$A ^ { \flat }$ are uniformly almost finitely presented. Let us summarize the discussion.

Theorem 5.25. Let R be a perfectoid K-algebra with tilt$R ^ { \flat }$. There is a fully faithful functor from$R _ { \mathrm { f e t } } ^ { \flat }$to$R _ { \mathrm { f e t } }$inverse to the tilting functor. The essential image of this functor consists of the finite ´etale covers S of$R ,$for which S (with its natural topology) is perfectoid and$S ^ { \circ a }$is finite ´etale over$R ^ { \circ a }$. In this case,$S ^ { \circ a }$is a uniformly finite projective$R ^ { \circ a }$-module.

In particular, we see that the fully faithful functor$R _ { \mathrm { f e t } } ^ { \flat } \hookrightarrow R _ { \mathrm { f e t } }$preserves degrees. We will later prove that this is an equivalence in general. For now, we prove that it is an equivalence for perfectoid fields, i.e. we finish the proof of Theorem 3.7.

Proof. (of Theorem 3.7) Let K be a perfectoid field with tilt$K ^ { \flat }$<sup>[</sup>. Using the previous theorem, it is enough to show that the fully faithful functor$K _ { \mathrm { f e t } } ^ { \flat } \to K _ { \mathrm { f e t } }$is an equivalence.

Proof using ramification theory. Proposition 6.6.2 (cf. its proof) and Proposition 6.6.6 of [14] show that for any finite extension L of$K ,$, the extension$L ^ { \circ a } / K ^ { \circ a }$is ´etale. Moreover, it is finite projective by Proposition 6.3.6 of [14], giving the desired result.

Proof reducing to the case where$K ^ { \flat }$is algebraically closed. Let$M = { \widehat { \overline { { K ^ { \flat } } } } }$be the completion of an algebraic closure of$K ^ { \flat }$<sup>[</sup>. Clearly, M is complete and perfect, i.e. M is perfectoid. Let$\bar { M ^ { \sharp } }$be the untilt of M. Then by Lemma 5.21 and Proposition 3.8, $M ^ { \sharp }$is an algebraically closed perfectoid field containing K. Any finite extension$L \subset M$ of$K ^ { \flat }$gives the untilt$L ^ { \sharp } \subset M ^ { \sharp }$, a finite extension of$K$. It is easy to see that the union$\begin{array} { r } { N = \bigcup _ { L } L ^ { \sharp } \subset M ^ { \sharp } } \end{array}$is a dense subfield. Now Krasner’s lemma implies that N is algebraically closed. Hence any finite extension F of K is contained in$N ;$this means that there is some Galois extension L of$K ^ { \flat }$such that F is contained in$L ^ { \sharp }$. Note that $L ^ { \sharp }$is still Galois, as the functor$L \mapsto L ^ { \sharp }$preserves degrees and automorphisms. In particular, F is given by some subgroup H of$\operatorname { G a l } ( L ^ { \sharp } / K ) = \operatorname { G a l } ( L / K ^ { \flat } )$, which gives the desired finite extension$F ^ { \flat } = L ^ { H }$of$K ^ { \flat }$that untilts to$F \colon$The equivalence of categories shows that$( F ^ { \flat } ) ^ { \sharp } \subset ( L ^ { \sharp } ) ^ { H } = F$, and as they have the same degree, they are equal. 

## 6. Perfectoid spaces: Analytic topology

In the following, we are interested in the adic spaces associated to perfectoid algebras. Specifically, note that perfectoid K-algebras are Tate, and we will look at the following type of afinoid K-algebras.

Definition 6.1. A perfectoid afinoid K-algebra is an afinoid K-algebra$( R , R ^ { + } )$such that R is a perfectoid K-algebra.

We note that in this case m$R ^ { \circ } \subset R ^ { + } \subset R ^ { \circ }$, because all topologically nilpotent elements lie in$R ^ { + }$, as$R ^ { + }$is integrally closed. In particular,$R ^ { + }$is almost equal to$R ^ { \circ }$

Lemma 6.2. The categories of perfectoid afinoid K-algebras and perfectoid afinoid $K ^ { \flat }$-algebras are equivalent. If$( R , R ^ { + } )$maps to$( R ^ { \flat } , R ^ { \flat + } )$under this equivalence, then $x \mapsto x ^ { \sharp }$induces an isomorphism$R ^ { \flat + } / \varpi ^ { \flat } \cong R ^ { + } / \varpi$. Also$R ^ { \flat + } = \varprojlim _ { x \mapsto x ^ { p } } R ^ { + }$

Proof. Giving an open integrally closed subring of$R ^ { \circ }$is equivalent to giving an integrally closed subring of$R ^ { \circ } / { \mathfrak { m } }$. This description is compatible with tilting. One easily checks the last identities.

It turns out that also in this case, the presheaf${ \mathcal { O } } _ { X }$is a sheaf. In fact, the main theorem of this section is the following.

Theorem 6.3. Let$( R , R ^ { + } )$be a perfectoid afinoid K-algebra, and let$X = \operatorname { S p a } ( R , R ^ { + } )$ with associated presheaves${ \mathcal { O } } _ { X } , { \mathcal { O } } _ { X } ^ { + }$. Also, let$( R ^ { \flat } , R ^ { \flat + } )$be the tilt given by Lemma$6 . 2 ,$ and let$X ^ { \flat } = \operatorname { S p a } ( R ^ { \flat } , R ^ { \flat + } )$etc. .

(i) We have a homeomorphism$X \ \cong \ X ^ { \flat }$<sup>[</sup>, given by mapping$x \in X$to the valuation $x ^ { \flat } \in X ^ { \flat }$defined by$| f ( x ^ { \flat } ) | = | f ^ { \sharp } ( x ) |$. This homeomorphism identifies rational subsets.

(ii) For any rational subset$U \subset X$with tilt$U ^ { \flat } \subset X ^ { \flat }$<sup>[</sup>, the complete afinoid K-algebra $( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is perfectoid, with tilt$( \mathcal { O } _ { X ^ { \flat } } ( U ^ { \flat } ) , \mathcal { O } _ { X ^ { \flat } } ^ { + } ( U ^ { \flat } ) )$

(iii) The presheaves${ \mathcal { O } } _ { X } , { \mathcal { O } } _ { X ^ { \flat } }$are sheaves.

(iv) The cohomology group$H ^ { i } ( X , { \mathcal { O } } _ { X } ^ { + } )$is m-torsion for$i > 0$

We remark that we did not assume that$R ^ { + }$is a$K ^ { \circ } { \mathrm { - a l g e b r a } }$, although this is satisfied in all examples of interest to us. For this reason, it does not literally make sense to use the language of almost mathematics in the context of${ \mathcal { O } } _ { X } ^ { + }$. In the following, the reader may safely assume that$R ^ { + }$is a$K ^ { \circ }$-algebra, which avoids some small extra twists.

Let us give an outline of the proof. First, we show that the map$X  X ^ { \flat }$is continuous. Next, we prove a slightly weaker version of (ii), and give an explicit description of the perfectoid$K ^ { \circ a } \mathrm { - a l g }$ebra associated to${ \mathcal { O } } _ { X } ( U )$. This will be used to prove a crucial approximation lemma, dealing with the problem that the map$g \mapsto g ^ { \sharp }$is far from being surjective. Nonetheless, it turns out that one can approximate any function$f \in R$by a function of the form$g ^ { \sharp }$such that the maps$x \mapsto | f ( x ) |$and$x \mapsto | g ^ { \sharp } ( x ) |$are identical except maybe at points x where both of them are very small. It is then easy to deduce part (i), and also part (ii). We note that the same approximation lemma will be used later in the proof of the weight-monodromy conjecture for complete intersections.

It remains to prove that${ \mathcal { O } } _ { X }$is a sheaf with vanishing higher cohomology, and that the vanishing even extends to the almost integral level. The proof proceeds in several steps. First, we prove it in the case that K is of characteristic$p$and$( R , R ^ { + } )$is the completed perfection of an afinoid K-algebra of tft. In that case, it is easy to deduce the result from Tate’s acyclicity theorem. Again, the direct limit over the Frobenius extends the vanishing of cohomology to the almost integral level. Next, we do the general characteristic$p$case by writing an arbitrary perfectoid afinoid K-algebra$( R , R ^ { + } )$as the completed direct limit of algebras of the previous form. Finally, we deduce the case where K has characteristic 0 by using the result in characteristic$p ,$making use of parts (i) and (ii) already proved.

Proof. First, we check that the map$X  X ^ { \flat }$is well-defined and continuous: To check welldefinedness, we have to see that it maps valuations to valuations. This was already verified in the proof of Proposition 3.6.

Moreover, the map$X  X ^ { \flat }$is continuous, because the preimage of the rational subset $U ( { \textstyle \frac { f _ { 1 } , \ldots , f _ { n } } { g } } )$is given by$U ( \frac { f _ { 1 } ^ { \sharp } , . . . , f _ { n } ^ { \sharp } } { g ^ { \sharp } } )$, assuming as in Remark 2.8 that$f _ { n }$is a power of$\varpi ^ { \flat }$ to ensure that$f _ { 1 } ^ { \sharp } , \ldots , f _ { n } ^ { \sharp }$still generate$R .$

We have the following description of${ \mathcal { O } } _ { X }$

Lemma 6.4. Let$\begin{array} { r } { U = U ( \frac { f _ { 1 } , \dots , f _ { n } } { a } ) \subset \mathrm { S p a } ( R ^ { \flat } , R ^ { \flat + } ) } \end{array}$be rational, with preimage$U ^ { \sharp } \subset$ $\operatorname { S p a } ( R , R ^ { + } )$. Assume that all$f _ { i } , g \in R ^ { \flat \circ }$and that$f _ { n } = \varpi ^ { \flat N }$for some$N _ { ; }$this is always possible without changing the rational subspace.

(i) Consider the \$-adic completion

$$
R ^ {\circ} \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \rangle
$$

of the subring

$$
R ^ {\circ} \left[ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right] \subset R \left[ \frac {1}{g ^ {\sharp}} \right].
$$

Then$\begin{array} { r } { R ^ { \circ } \langle \left( \frac { f _ { 1 } ^ { \sharp } } { g ^ { \sharp } } \right) ^ { 1 / p ^ { \infty } } , \dots , \left( \frac { f _ { n } ^ { \sharp } } { g ^ { \sharp } } \right) ^ { 1 / p ^ { \infty } } \rangle ^ { a } } \end{array}$is a perfectoid$K ^ { \circ a } - a l g e b r a$

(ii) The algebra${ \mathcal { O } } _ { X } ( U ^ { \sharp } )$is a perfectoid K-algebra, with associated perfectoid$K ^ { \circ a }$-algebra

$$
\mathcal {O} _ {X} (U ^ {\sharp}) ^ {\circ a} = R ^ {\circ} \left\langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right\rangle^ {a}.
$$

(iii) The tilt of${ \mathcal { O } } _ { X } ( U ^ { \sharp } )$is given by${ \mathcal { O } } _ { X ^ { \flat } } ( U )$

Proof. (i), (K of characteristic$p )$Assume that K has characteristic$p ,$and identify$K ^ { \flat } =$ $K ;$the general case is dealt with below. We see from the definition that

$$
R ^ {\circ} \langle \left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \rangle
$$

is flat over$K ^ { \circ }$and \$-adically complete.

We want to show that modulo$\varpi$, Frobenius is almost surjective with kernel almost generated by$\varpi ^ { 1 / p }$. We have a surjection

$$
R ^ {\circ} [ T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} ] \to R ^ {\circ} [ \left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} ].
$$

Its kernel contains the ideal I generated by all$T _ { i } ^ { 1 / p ^ { m } } g ^ { 1 / p ^ { m } } - f _ { i } ^ { 1 / p ^ { m } }$. We claim that the induced morphism

$$
R ^ {\circ} [ T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} ] / I \to R ^ {\circ} [ \left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} ]
$$

is an almost isomorphism. Indeed, it is an isomorphism after inverting$\varpi .$, because this also inverts g. If$f$lies in the kernel of this map, there is some k with$\varpi ^ { k } f \in I$. But then$( \varpi ^ { k / p ^ { m } } { \bar { f } } ) ^ { p ^ { m } } \in I$, and because I is perfect, also$\varpi ^ { k / p ^ { m } } f \in I$. This gives the desired statement.

Reducing modulo$\varpi .$, we have an almost isomorphism

$$
R ^ {\circ} [ T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} ] / (I, \varpi) \to R ^ {\circ} \langle \left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \rangle / \varpi .
$$

From the definition of$I ,$it is immediate that Frobenius gives an isomorphism

$$
R ^ {\circ} [ T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} ] / (I, \varpi^ {1 / p}) \cong R ^ {\circ} [ T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} ] / (I, \varpi)  .
$$

This finally shows that

$$
R ^ {\circ} \langle \left(\frac {f _ {1}}{g}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n}}{g}\right) ^ {1 / p ^ {\infty}} \rangle^ {a}
$$

is a perfectoid$K ^ { \circ a }$-algebra, giving part (i) in characteristic$p .$

$( \mathrm { i } ) { \Rightarrow } ( \mathrm { i } )$, (General K) We show that in general, (i) implies (ii). Note that$R ^ { \circ } \subset R$is open and bounded, hence we may choose$R _ { 0 } = R ^ { \circ }$in Definition 2.13. We have the inclusions

$$
R ^ {\circ} [ \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \ldots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} ] \subset R ^ {\circ} [ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} ] \subset R [ \frac {1}{g ^ {\sharp}} ].
$$

Moreover, we claim that

$$
\varpi^ {n N} R ^ {\circ} \left[ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \right] \subset R ^ {\circ} \left[ \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \dots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} \right]:
$$

Indeed,$\begin{array} { r } { \frac { 1 } { g ^ { \sharp } } = \varpi ^ { - N } \frac { f _ { n } ^ { \sharp } } { g ^ { \sharp } } } \end{array}$, and any element on the left-hand side can be written as a sum of terms on the right-hand side with coeficients in${ \frac { 1 } { ( g ^ { \sharp } ) ^ { n } } } R ^ { \circ }$

Now we may pass to the \$-adic completion and get inclusions

$$
R ^ {\circ} \langle \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \dots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} \rangle \subset R ^ {\circ} \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \rangle \subset R \langle \frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}, \dots , \frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}} \rangle = \mathcal {O} _ {X} (U).
$$

Thus it follows from part (i) that

$$
\mathcal {O} _ {X} (U) = R ^ {\circ} \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \rangle [ \varpi^ {- 1} ]
$$

is perfectoid, with corresponding perfectoid$K ^ { \circ a }$-algebra.

(i), (iii), (General K) Again, we see from the definition that

$$
R ^ {\circ} \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \rangle
$$

is flat over$K ^ { \circ }$and \$-adically complete. We have to show that modulo$\varpi .$, Frobenius is almost surjective with kernel almost generated by$\varpi ^ { 1 / p }$. We still have the map

$$
R ^ {\circ} [ T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} ] / I \to R ^ {\circ} [ \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \ldots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} ],
$$

where I is the ideal generated by all$T _ { i } ^ { 1 / p ^ { m } } ( g ^ { 1 / p ^ { m } } ) ^ { \sharp } - ( f _ { i } ^ { 1 / p ^ { m } } ) ^ { \sharp }$. Also, we may apply our results for the tilted situation. In particular, we know that$( \mathcal { O } _ { X ^ { \flat } } ( U ) , \mathcal { O } _ { X ^ { \flat } } ^ { + } ( U ) )$is a perfectoid afinoid$K ^ { \flat } \mathrm { - a l g e b r a }$. Let$( S , S ^ { + } )$be its tilt. Then$\operatorname { S p a } ( S , S ^ { + } ) \to X$factors over$U ^ { \sharp }$, and hence we get a map$( { \mathcal { O } } _ { X } ( U ^ { \sharp } ) , { \mathcal { O } } _ { X } ^ { + } ( U ^ { \sharp } ) ) \to ( S , S ^ { + } )$. The composite map

$$
R ^ {\circ} \langle T _ {1} ^ {1 / p ^ {\infty}}, \dots , T _ {n} ^ {1 / p ^ {\infty}} \rangle^ {a} \rightarrow R ^ {\circ} \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \rangle^ {a} \rightarrow \mathcal {O} _ {X} (U ^ {\sharp}) ^ {\circ a} \rightarrow S ^ {\circ a}
$$

is a map of perfectoid$K ^ { \circ a }$-algebras, which is the tilt of the composite map

$$
R ^ {\flat \circ} \langle T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} \rangle^ {a} \to R ^ {\flat \circ} \langle T _ {1} ^ {1 / p ^ {\infty}}, \ldots , T _ {n} ^ {1 / p ^ {\infty}} \rangle^ {a} / I ^ {\flat} \to \mathcal {O} _ {X ^ {\flat}} (U) ^ {\circ a},
$$

where$I ^ { \flat }$is the corresponding ideal which occurs in the tilted situation. Note that

$$
R ^ {\flat \circ} \langle T _ {1} ^ {1 / p ^ {\infty}}, \dots , T _ {n} ^ {1 / p ^ {\infty}} \rangle / (I ^ {\flat}, \varpi^ {\flat}) = R ^ {\circ} \langle T _ {1} ^ {1 / p ^ {\infty}}, \dots , T _ {n} ^ {1 / p ^ {\infty}} \rangle / (I, \varpi)
$$

from the explicit description. Since

$$
R ^ {\flat \circ} \langle T _ {1} ^ {1 / p ^ {\infty}}, \dots , T _ {n} ^ {1 / p ^ {\infty}} \rangle^ {a} / (I ^ {\flat}, \varpi^ {\flat}) \to \mathcal {O} _ {X ^ {\flat}} (U) ^ {\circ a} / \varpi^ {\flat}
$$

is an isomorphism, so is the composite map

$$
R ^ {\circ} \langle T _ {1} ^ {1 / p ^ {\infty}}, \dots , T _ {n} ^ {1 / p ^ {\infty}} \rangle^ {a} / (I, \varpi) \rightarrow R ^ {\circ} \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \rangle^ {a} / \varpi \rightarrow S ^ {\circ a} / \varpi ,
$$

as it identifies with the previous map under tilting. The first map being surjective, it follows that both maps are isomorphisms. In particular,

$$
R ^ {\circ} \langle \left(\frac {f _ {1} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}}, \dots , \left(\frac {f _ {n} ^ {\sharp}}{g ^ {\sharp}}\right) ^ {1 / p ^ {\infty}} \rangle^ {a} / \varpi \cong S ^ {\circ a} / \varpi .
$$

This gives part (i), and hence part (ii), and then the latter isomorphism gives part (iii).

We need an approximation lemma.

Lemma 6.5. Let$R = K \langle T _ { 0 } ^ { 1 / p ^ { \infty } } , . . . , T _ { n } ^ { 1 / p ^ { \infty } } \rangle$. Let$f \in R ^ { \circ }$be a homogeneous element of degree$d \in \mathbb { Z } [ \frac { 1 } { p } ]$. Then for any rational number$c \geq 0$and any$\epsilon > 0$, there exists an element

$$
g _ {c, \epsilon} \in R ^ {\flat \circ} = K ^ {\flat \circ} \langle T _ {0} ^ {1 / p ^ {\infty}}, \dots , T _ {n} ^ {1 / p ^ {\infty}} \rangle
$$

homogeneous of degree d such that for all$x \in X = \operatorname { S p a } ( R , R ^ { \circ } )$, we have

$$
| f (x) - g _ {c, \epsilon} ^ {\sharp} (x) | \leq | \varpi | ^ {1 - \epsilon} \max (| f (x) |, | \varpi | ^ {c}).
$$

Remark 6.6. Note that for$\epsilon < 1$, the given estimate says in particular that for all $x \in X = \operatorname { S p a } ( R , R ^ { \circ } )$, we have

$$
\max (| f (x) |, | \varpi | ^ {c}) = \max (| g _ {c, \epsilon} ^ {\sharp} (x) |, | \varpi | ^ {c}).
$$

Proof. We fix$\epsilon > 0$, and assume$\epsilon < 1$and$\epsilon \in \mathbb { Z } [ { \frac { 1 } { p } } ]$. We also fix$f .$Then we prove inductively that for any c one can find some$\epsilon ( c ) > 0$and some

$$
g _ {c} \in R ^ {\flat \circ} = K ^ {\flat \circ} \langle T _ {0} ^ {1 / p ^ {\infty}}, \dots , T _ {n} ^ {1 / p ^ {\infty}} \rangle
$$

homogeneous of degree d such that for all$x \in X = \operatorname { S p a } ( R , R ^ { \circ } )$, we have

$$
| f (x) - g _ {c} ^ {\sharp} (x) | \leq | \varpi | ^ {1 - \epsilon + \epsilon (c)} \max (| f (x) |, | \varpi | ^ {c}).
$$

We will need$\epsilon ( c )$, as each induction step will lose some small constant because of some almost mathematics involved. Now we argue by induction, increasing from c to$c ^ { \prime } = c + a ,$ where$0 < a < \epsilon$is some fixed rational number in$\mathbb { Z } [ \textstyle { \frac { 1 } { p } } ]$. The case$c = 0$is obvious: One may take$\epsilon ( 0 ) = \epsilon$. We are free to replace$\epsilon ( c )$by something smaller, so without loss of generality, we assume$\epsilon ( c ) \leq \epsilon - a$and$\epsilon ( c ) \dot { \in } \mathbb { Z } [ \frac { 1 } { p } ]$

Let$X = \mathrm { S p a } ( R , R ^ { + } )$, where$R ^ { + } = R ^ { \circ } = K ^ { \circ } \langle T _ { 0 } ^ { 1 / p ^ { \infty } } , \ldots , T _ { n } ^ { 1 / p ^ { \infty } } \rangle$. Let$U _ { c } \subset X ^ { \flat } \ : =$ $\mathrm { S p a } ( R ^ { \flat } , R ^ { \flat + } )$be the rational subset given by$| g _ { c } ( x ) | \leq | \varpi ^ { \flat } | ^ { c }$. Its preimage$U _ { c } ^ { \sharp } \subset X$is given by$| f ( x ) | \leq | \varpi | ^ { c }$. The condition implies that

$$
h = f - g _ {c} ^ {\sharp} \in \varpi^ {c + 1 - \epsilon + \epsilon (c)} \mathcal {O} _ {X} ^ {+} (U _ {c} ^ {\sharp}).
$$

The previous lemma shows that

$$
\mathcal {O} _ {X} (U _ {c} ^ {\sharp}) ^ {\circ a} = R ^ {\circ} \left\langle \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {\frac {1}{p ^ {\infty}}} \right\rangle^ {a}.
$$

But h is a homogeneous element, so that h lies almost in the \$-adic completion of

$$
\bigoplus_ {i \in \mathbb {Z} [ \frac {1}{p} ], 0 \leq i \leq 1} \varpi^ {c + 1 - \epsilon + \epsilon (c)} \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {i} R _ {\deg = d - d i} ^ {\circ}.
$$

This shows that we can find elements$r _ { i } \in R ^ { + }$homogeneous of degree$d - d i$, such that $r _ { i } \to 0$, with

$$
h = \sum_ {i \in \mathbb {Z} [ \frac {1}{p} ], 0 \leq i \leq 1} \varpi^ {c + 1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {i} r _ {i},
$$

where we choose some$0 < \epsilon ( c ^ { \prime } ) < \epsilon ( c ) , \epsilon ( c ^ { \prime } ) \in \mathbb { Z } [ \frac { 1 } { p } ]$. Choose$s _ { i } \in R ^ { \flat + }$homogeneous of degree$d - d i , s _ { i } \to 0$, such that \$ divides$r _ { i } - s _ { i } ^ { \sharp }$. Now set

$$
g _ {c ^ {\prime}} = g _ {c} + \sum_ {i \in \mathbb {Z} [ \frac {1}{p} ], 0 \leq i \leq 1} (\varpi^ {\flat}) ^ {c + 1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}}\right) ^ {i} s _ {i}.
$$

We claim that for all$x \in X$, we have

$$
| f (x) - g _ {c ^ {\prime}} ^ {\sharp} (x) | \leq | \varpi | ^ {1 - \epsilon + \epsilon (c ^ {\prime})} \max (| f (x) |, | \varpi | ^ {c ^ {\prime}}).
$$

Assume first that$| f ( x ) | > | \varpi | ^ { c }$. Then we have$| g _ { c } ^ { \sharp } ( x ) | = | f ( x ) | > | \varpi | ^ { c }$. It is enough to show that

$$
\left| \left((\varpi^ {\flat}) ^ {c + 1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}}\right) ^ {i} s _ {i}\right) ^ {\sharp} (x) \right| \leq | \varpi | ^ {1 - \epsilon + \epsilon (c ^ {\prime})} | f (x) |.
$$

Neglecting$| s _ { i } ^ { \sharp } ( x ) | \leq 1$, the left-hand side is maximal when$i \ = \ 1$, in which case it evaluates to the right-hand side, so that we get the desired estimate.

Now we are left with the case$| f ( x ) | \leq | \varpi | ^ { c }$. We claim that in fact

$$
| f (x) - g _ {c ^ {\prime}} ^ {\sharp} (x) | \leq | \varpi | ^ {c ^ {\prime} + 1 - \epsilon + \epsilon (c ^ {\prime})}
$$

in this case, which is clearly enough. For this, it is enough to see that$f - g _ { c ^ { \prime } } ^ { \sharp }$is an element of$\varpi ^ { c + 1 } \mathcal { O } _ { X } ( U _ { c } ^ { \sharp } ) ^ { \circ }$, because$c + 1 > c ^ { \prime } + 1 - \epsilon + \epsilon ( c ^ { \prime } )$. But we have

$$
\frac {g _ {c ^ {\prime}}}{(\varpi^ {\flat}) ^ {c}} = \frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}} + \sum_ {i} (\varpi^ {\flat}) ^ {1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c}}{(\varpi^ {\flat}) ^ {c}}\right) ^ {i} s _ {i},
$$

with all terms being in$\mathcal { O } _ { X ^ { \flat } } ( U _ { c } ) ^ { \circ }$. Hence we get that

$$
\frac {g _ {c ^ {\prime}} ^ {\sharp}}{\varpi^ {c}} = \frac {g _ {c} ^ {\sharp}}{\varpi^ {c}} + \sum_ {i} \varpi^ {1 - \epsilon + \epsilon (c ^ {\prime})} \left(\frac {g _ {c} ^ {\sharp}}{\varpi^ {c}}\right) ^ {i} r _ {i}
$$

in$\mathcal { O } _ { X } ( U _ { c } ^ { \sharp } ) ^ { \circ }$, modulo$\varpi$. Multiplying by$\varpi ^ { c }$, this rewrites as

$$
f - g _ {c ^ {\prime}} ^ {\sharp} = f - g _ {c} ^ {\sharp} - h = 0
$$

modulo$\varpi ^ { c + 1 }$. This gives the desired estimate.

Corollary${ \bf 6 . 7 . ~ } L e t ~ ( R , R ^ { + } )$be a perfectoid afinoid K-algebra, with$t i l t \left( R ^ { \flat } , R ^ { \flat + } \right)$, and let$X = \operatorname { S p a } ( R , R ^ { + } ) , X ^ { \flat } = \operatorname { S p a } ( R ^ { \flat } , R ^ { \flat + } )$

(i) For any$f \in R$and any$c \geq 0 , \epsilon > 0$, there exists$g _ { c , \epsilon } \in R ^ { \flat }$such that for all$x \in X$ we have

$$
| f (x) - g _ {c, \epsilon} ^ {\sharp} (x) | \leq | \varpi | ^ {1 - \epsilon} \max (| f (x) |, | \varpi | ^ {c}).
$$

(ii) For any$x \in X$, the completed residue field$\widehat { k ( x ) }$is a perfectoid field.

(iii) The morphism$X  X ^ { \flat }$induces a homeomorphism, identifying rational subsets.

Proof. (i) As any maximal point of$\operatorname { S p a } ( R , R ^ { + } )$is contained in$\operatorname { S p a } ( R , R ^ { \circ } )$, and it is enough to check the inequality at maximal points after increasing  slightly, it is enough to prove this if$R ^ { + } = R ^ { \circ }$. At the expense of enlarging c, we may assume that$f \in R ^ { \circ }$ and also assume that c is an integer. Further, we can write$f = g _ { 0 } ^ { \sharp } + \varpi g _ { 1 } ^ { \sharp } + \ldots + \varpi ^ { c } g _ { c } ^ { \sharp } +$ $\boldsymbol { \varpi } ^ { c + 1 } \boldsymbol { f } _ { c + 1 }$for certain$g _ { 0 } , \ldots , g _ { c } \in R ^ { \flat \circ }$and$f _ { c + 1 } \in R ^ { \circ }$. We can assume$f _ { c + 1 } = 0$. Now we have the map

$$
K \langle T _ {0} ^ {1 / p ^ {\infty}}, \dots , T _ {c} ^ {1 / p ^ {\infty}} \rangle \rightarrow R
$$

sending$T _ { i } ^ { 1 / p ^ { m } }$to$( g _ { i } ^ { 1 / { p ^ { m } } } ) ^ { \sharp }$, and f is the image of$T _ { 0 } + \varpi T _ { 1 } + \hdots + \varpi ^ { c } T _ { c } .$, to which we may apply Lemma 6.5.

(ii), (K of characteristic$p )$In this case, we know that${ \mathcal { O } } _ { X } ( U ) ^ { \circ a }$is perfectoid for any rational subset U. It follows that the \$-adic completion of$\mathcal { O } _ { X , x } ^ { \circ a }$is a perfectoid$K ^ { \circ a } .$ algebra, hence$\widehat { k ( x ) }$is a perfectoid K-algebra. As it is also a nonarchimedean field, the result follows.

(iii) First, part (i) immediately implies that any rational subset of X is the preimage of a rational subset of$X ^ { \flat }$. Because X is$T _ { 0 } .$, this implies that the map is injective. Now any$x \in X ^ { \flat }$factors as a composite$R ^ { \flat } \to \widehat { k ( x ) } \to \Gamma \cup \{ 0 \}$. As$\widehat { k ( x ) }$is perfectoid, we may untilt to a perfectoid field over$K$, and we may also untilt the valuation by Proposition 3.6. This shows that the map is surjective, giving part (iii). Now part (ii) follows in general with the same proof.

For any subset$M \subset X$, we write$M ^ { \flat } \subset X ^ { \flat }$for the corresponding subset of$X ^ { \flat }$<sup>[</sup>.

Corollary 6.8. Let$( R , R ^ { + } )$be a perfectoid afinoid K-algebra, with tilt$( R ^ { \flat } , R ^ { \flat + } )$, and let$X \ = \ \mathrm { S p a } ( R , R ^ { + } ) , \ X ^ { \flat } \ = \ \mathrm { S p a } ( R ^ { \flat } , R ^ { \flat } + )$Then for all rational$U ~ \subset ~ X$, the pair $( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is a perfectoid afinoid K-algebra with tilt$( \mathcal { O } _ { X ^ { \flat } } ( U ^ { \flat } ) , \mathcal { O } _ { X ^ { \flat } } ^ { + } ( U ^ { \flat } ) )$

Proof. Corollary 6.7 (iii) and Lemma 6.4 (ii) show that$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is a perfectoid afinoid K-algebra. It can be characterized by the universal property of Proposition 2.14 among all perfectoid afinoid K-algebras, and tilting this universal property shows that its tilt has the analogous universal property characterizing$( { \mathcal { O } } _ { X ^ { \flat } } ( U ^ { \flat } ) , { \mathcal { O } } _ { X ^ { \flat } } ^ { + } ( U ^ { \flat } ) )$among all perfectoid afinoid K<sup>[</sup>-algebras.

At this point, we have proved parts (i) and (ii) of Theorem 6.3.

To prove the sheaf properties, we start in characteristic$p ,$with a certain class of perfectoid rings which are particularly easy to access.

Definition 6.9. Assume K is of characteristic p. Then a perfectoid afinoid K-algebra $( R , R ^ { + } )$is said to be p-finite if there exists a reduced afinoid K-algebra$( S , S ^ { + } )$of topologically finite type such that$( R , R ^ { + } )$is the completed perfection of$( S , S ^ { + } )$, i.e.$R ^ { + }$ is the \$-adic completion of$\operatorname* { l i m } _ { \to \Phi } S ^ { + }$and$R = R ^ { + } [ \varpi ^ { - 1 } ]$

At this point, let us recall some facts about reduced afinoid K-algebras of topologically finite type.

Proposition 6.10. Let$( S , S ^ { + } )$be a reduced afinoid K-algebra of topologically finite type, and let${ X = \mathrm { S p a } ( S , S ^ { + } ) }$

(i) The subset$S ^ { + } = S ^ { \circ } \subset S$is open and bounded.

(ii) For any rational subset$U \subset X$, the afinoid K-algebra$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is reduced and of topologically finite type.

(iii) For any covering$X = \cup U _ { i }$by finitely many rational subsets$U _ { i } \subset X$, each cohomology group of the complex

$$
0 \to \mathcal {O} _ {X} (X) ^ {\circ} \to \prod_ {i} \mathcal {O} _ {X} (U _ {i}) ^ {\circ} \to \prod_ {i, j} \mathcal {O} _ {X} (U _ {i} \cap U _ {j}) ^ {\circ} \to \dots
$$

is annihilated by some power of \$.

Proof. Using [19], Proposition 4.3 and its proof, one sees that all statements are readily translated into the classical language of rigid geometry, and we use results from the book of Bosch-G¨untzer-Remmert, [2]. Part (i) is precisely their 6.2.4 Theorem 1, and part (ii) is 7.3.2 Corollary 10.

Moreover, Tate’s acyclicity theorem, 8.2.1 Theorem 1 in [2], says that

$$
0 \to \mathcal {O} _ {X} (X) \xrightarrow {d _ {0}} \prod_ {i} \mathcal {O} _ {X} (U _ {i}) \xrightarrow {d _ {1}} \prod_ {i, j} \mathcal {O} _ {X} (U _ {i} \cap U _ {j}) \xrightarrow {d _ {2}} \dots
$$

is exact. Then ker$d _ { i }$is a closed subspace of a K-Banach space, hence itself a K-Banach space, and$d _ { i - 1 }$is a surjection onto ker$d _ { i }$. By Banach’s open mapping theorem, the map$d _ { i - 1 }$is an open map to ker$d _ { i }$. This says that the subspace and quotient topologies on ker$d _ { i } = \operatorname { i m } d _ { i - 1 }$coincide. Now consider the sequence

$$
0 \to \mathcal {O} _ {X} (X) ^ {\circ} \xrightarrow {d _ {0} ^ {\circ}} \prod_ {i} \mathcal {O} _ {X} (U _ {i}) ^ {\circ} \xrightarrow {d _ {1} ^ {\circ}} \prod_ {i, j} \mathcal {O} _ {X} (U _ {i} \cap U _ {j}) ^ {\circ} \xrightarrow {d _ {2} ^ {\circ}} \dots .
$$

By parts (i) and (ii), the quotient topology on im$d _ { i - 1 }$has$\varpi ^ { n }$im$d _ { i - 1 } ^ { \circ } , n \in \mathbb { Z } .$, as a basis of open neighborhoods of 0, and the subspace topology of ker$d _ { i }$has$\varpi ^ { n } \mathrm { k e r } d _ { i } ^ { \circ } , n \in \mathbb { Z }$, as a basis of open neighborhoods of 0. That they agree precisely amounts to saying that the cohomology group is annihilated by some power of$\varpi$.

Proposition 6.11. Assume that K is of characteristic$p ,$and that$( R , R ^ { + } )$is p-finite, given as the completed perfection of a reduced afinoid K-algebra$( S , S ^ { + } )$of topologically finite type.

(i) The map$X = \operatorname { S p a } ( R , R ^ { + } ) \cong Y = \operatorname { S p a } ( S , S ^ { + } )$is a homeomorphism identifying rational subspaces.

(ii) For any$U \subset X$rational, corresponding to$V \subset Y$, the perfectoid afinoid K-algebra $( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is equal to the completed perfection of$( \mathcal { O } _ { Y } ( V ) , \mathcal { O } _ { Y } ^ { + } ( V ) )$.

(iii) For any covering$X = \cup _ { i } U _ { i }$by rational subsets, the sequence

$$
0 \to \mathcal {O} _ {X} (X) ^ {\circ a} \to \prod_ {i} \mathcal {O} _ {X} (U _ {i}) ^ {\circ a} \to \prod_ {i, j} \mathcal {O} _ {X} (U _ {i} \cap U _ {j}) ^ {\circ a} \to \dots
$$

is exact. In particular,${ \mathcal { O } } _ { X }$is a sheaf, and$H ^ { i } ( X , { \mathcal { O } } _ { X } ^ { o a } ) = 0 f o r i > 0$

Remark 6.12. The last assertion is equivalent to the assertion that$H ^ { i } ( X , { \mathcal { O } } _ { X } ^ { + } )$is annihilated by m.

Proof. (i) Going to the perfection does not change the associated adic space and rational subspaces, and going to the completion does not by Proposition 2.11.

(ii) The completed perfection of$( \mathcal { O } _ { Y } ( V ) , \mathcal { O } _ { Y } ^ { + } ( V ) )$is a perfectoid afinoid K-algebra. It has the universal property defining$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$among all perfectoid afinoid$K \mathfrak { - }$ algebras.

(iii) Note that the corresponding sequence for Y is exact up to some \$-power. Hence after taking the perfection, it is almost exact, and stays so after completion.

Lemma 6.13. Assume K is of characteristic$p .$

(i) Any perfectoid afinoid K-algebra$( R , R ^ { + } )$for which R<sup>+</sup> is a$K ^ { \circ } - a l g e b r a$is the completion of a filtered direct limit of p-finite perfectoid afinoid K-algebras$( R _ { i } , R _ { i } ^ { + } )$

(ii) This induces a homeomorphism$\operatorname { S p a } ( R , R ^ { + } ) \cong \varprojlim \operatorname { S p a } ( R _ { i } , R _ { i } ^ { + } )$, and each rational $U \subset X = \operatorname { S p a } ( R , R ^ { + } )$comes as the preimage of some rational$U _ { i } \subset X _ { i } = \operatorname { S p a } ( R _ { i } , R _ { i } ^ { + } )$

(iii) In this case$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is equal to the completion of the filtered direct limit of the$( \mathcal { O } _ { X _ { j } } ( U _ { j } ) , \mathcal { O } _ { X _ { i } } ^ { + } ( U _ { j } ) )$, where$U _ { j }$is the preimage of$U _ { i }$in$X _ { j } ~ f o r ~ j \geq i$

$\operatorname { ( i v ) } I f U _ { i } \subset X _ { i }$is some quasicompact open subset containing the image of$X$, then there is some j such that the image of$X _ { j }$is contained in$U _ { i }$

Proof. (i) For any finite subset$I \subset R ^ { + }$, we have the K-subalgebra$S _ { I } \subset R$given as the image of$K \langle T _ { i } | i \in I \rangle  R$. Then$S _ { I }$is a reduced quotient of$K \langle T _ { i } | i \in I \rangle$, and we give$S _ { I }$ the quotient topology. Let$S _ { I } ^ { + } \subset S _ { I }$be the set of power-bounded elements; it is also the set of elements integral over$\bar { K } ^ { \circ } \langle T _ { i } | i \in I \rangle$by [31], Theorem 5.2. In particular,$S _ { I } ^ { + } \subset R ^ { + }$ We caution the reader that$S _ { I } ^ { + }$is in general not the preimage of$R ^ { + }$in$S _ { I }$

Now let$( R _ { I } , R _ { I } ^ { + } )$be the completed perfection of$( S _ { I } , S _ { I } ^ { + } )$, i.e.$R _ { I } ^ { + }$is the \$-adic completion of${ \underline { { \operatorname* { l i m } } } } _ { \Phi } S _ { I } ^ { + }$, and$R _ { I } = R _ { I } ^ { + } [ \varpi ^ { - 1 } ]$. We get an induced map$\bar { ( } R _ { I } , R _ { I } ^ { + } )  ( R , R ^ { + } )$, and$( R _ { I } , R _ { I } ^ { + } )$is a p-finite perfectoid afinoid K-algebra. We claim that$R ^ { + } / \varpi ^ { n } =$ $\varinjlim _ { T } R _ { I } ^ { + } / \varpi ^ { n }$. Indeed, the map is clearly surjective. It is also injective, since if$f _ { 1 } , f _ { 2 } \in R _ { I } ^ { + }$ satisfy$f _ { 1 } - f _ { 2 } = \varpi ^ { n } g$for some$g \in R ^ { + }$, then for some larger$J \supset I$containing$^ { g , }$also $f _ { 1 } - f _ { 2 } \in \varpi ^ { n } R _ { J } ^ { + }$. This shows that$R ^ { + }$is the completed direct limit of the$R _ { I } ^ { + }$, i.e. $( R , R ^ { + } )$is the completed direct limit of the$( R _ { I } , R _ { I } ^ { + } )$

(ii) Let$( L , L ^ { + } )$be the direct limit of the$( R _ { I } , R _ { I } ^ { + } )$, equipped with the \$-adic topology. Then one checks by hand that$\operatorname { S p a } ( L , L ^ { + } ) \cong \varinjlim \operatorname { S p a } ( R _ { i } , R _ { i } ^ { + } )$, compatible with rational subspaces. But then the same thing holds true for the completed direct limit by Proposition 2.11.

(iii) The completion of the direct limit of the$( \mathcal { O } _ { X _ { j } } ( U _ { j } ) , \mathcal { O } _ { X _ { j } } ^ { + } ( U _ { j } ) )$is a perfectoid afinoid K-algebra, and it satisfies the universal property describing$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$

(iv) This is an abstract property of spectral spaces and spectral maps. Let$A _ { i }$be the closed complement of$U _ { i } .$, and for any$j \geq i ,$, let$A _ { j }$be the preimage of$A _ { i }$in$X _ { j }$. Then the$A _ { j }$are constructible subsets of$X _ { j } .$, hence spectral, and the transition maps between the$A _ { j }$are spectral. If one gives the$A _ { j }$the constructible topology, they are compact topological spaces, and the transition maps are continuous. If their inverse limit is zero, then one of them has to be zero.

Proposition 6.14. Let K be of any characteristic, and let$( R , R ^ { + } )$be a perfectoid afinoid K-algebra,$X = \mathrm { S p a } ( R , R ^ { + } )$. For any covering$X = \textstyle \bigcup _ { i } U _ { i }$by finitely many rational subsets, the sequence

$$
0 \to \mathcal {O} _ {X} (X) ^ {\circ a} \to \prod_ {i} \mathcal {O} _ {X} (U _ {i}) ^ {\circ a} \to \prod_ {i, j} \mathcal {O} _ {X} (U _ {i} \cap U _ {j}) ^ {\circ a} \to \dots
$$

is exact. In particular,${ \mathcal { O } } _ { X }$is a sheaf, and$H ^ { i } ( X , { \mathcal { O } } _ { X } ^ { o a } ) = 0 f o r i > 0$

Proof. Assume first that K has characteristic p. We may replace K by a perfectoid subfield, such as the \$-adic completion of$\mathbb { F } _ { p } ( ( \varpi ) ) ( \varpi ^ { 1 / p ^ { \infty } } ) ;$; this ensures that for any perfectoid afinoid K-algebra$( R , R ^ { + } )$, the ring$R ^ { + }$is a$K ^ { \circ }$-algebra. Then use Lemma

6.13 to write$X = \operatorname { S p a } ( R , R ^ { + } ) \cong \varinjlim X _ { i } = \operatorname { S p a } ( R _ { i } , R _ { i } ^ { + } )$as an inverse limit, with$( R _ { i } , R _ { i } ^ { + } )$ p-finite. Any rational subspace comes from a finite level, and a cover by finitely many rational subspaces is the pullback of a cover by finitely many rational subspaces on a finite level. Hence the almost exactness of the sequence follows by taking the completion of the direct limit of the corresponding statement for$X _ { i }$, which is given by Proposition 6.11. The rest follows as before.

In characteristic 0, first use the exactness of the tilted sequence, then reduce modulo $\varpi ^ { \flat }$(which is still exact by flatness), and then remark that this is just the original sequence reduced modulo \$. As this is exact, the original sequence is exact, by flatness and completeness. Again, we also get the other statements.

This finishes the proof of Theorem 6.3.

We see that to any perfectoid afinoid K-algebra$( R , R ^ { + } )$, we have associated an afinoid adic space$X = \operatorname { S p a } ( R , R ^ { + } )$. We call these spaces afinoid perfectoid spaces.

Definition 6.15. A perfectoid space is an adic space over K that is locally isomorphic to an afinoid perfectoid space. Morphisms between perfectoid spaces are the morphisms of adic spaces.

The process of tilting glues.

Definition 6.16. We say that a perfectoid space$X ^ { \flat }$over$K ^ { \flat }$is the tilt of a perfectoid space X over K if there is a functorial isomorphism Hom$( \mathrm { S p a } ( R ^ { \flat } , R ^ { \flat + } ) , X ^ { \flat } ) \ : =$ Hom$( \mathrm { S p a } ( R , R ^ { + } ) , X )$for all perfectoid afinoid K-algebras$( R , R ^ { + } )$with tilt$( R ^ { \flat } , R ^ { \flat + } )$

Proposition 6.17. Any perfectoid space X over K admits a tilt$X ^ { \flat }$<sup>[</sup>, unique up to unique isomorphism. This induces an equivalence between the category of perfectoid spaces over K and the category of perfectoid spaces over$K ^ { \flat }$. The underlying topological spaces of X and$X ^ { \flat }$are naturally identified. A perfectoid space X is afinoid perfectoid if and only if its tilt$X ^ { \flat }$is afinoid perfectoid. Finally, for any afinoid perfectoid subspace$U \subset X$, the pair$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$is a perfectoid afinoid K-algebra with tilt$( { \mathcal { O } } _ { X ^ { \flat } } ( U ^ { \flat } ) , { \mathcal { O } } _ { X ^ { \flat } } ^ { + } ( U ^ { \flat } ) )$).

Proof. This is a formal consequence of Theorem 5.2, Theorem 6.3 and Proposition 2.19. Note that to any open$U \subset X$, one gets an associated perfectoid space with underlying topological space U by restricting the structure sheaf and valuations to U, and hence its global sections are$( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$, so that if$U$is afinoid, then $U = \mathrm { S p a } ( { \mathcal { O } } _ { X } ( U ) , { \mathcal { O } } _ { X } ^ { + } ( U ) )$. This gives the last part of the proposition.

Let us finish this section by noting one way in which perfectoid spaces behave better than adic spaces (cf. Proposition 1.2.2 of [20]).

Proposition 6.18. If$X \right. Y \left. Z$are perfectoid spaces over K, then the fibre product $X \times _ { Y } Z$exists in the category of adic spaces over K, and is a perfectoid space.

Proof. As usual, one reduces to the afine case,$X = \operatorname { S p a } ( A , A ^ { + } ) , Y = \operatorname { S p a } ( B , B ^ { + } )$ and$Z = \mathrm { S p a } ( C , C ^ { + } )$, and we want to construct$W = X \times _ { Y } Z .$This is given by $W = \mathrm { S p a } ( D , D ^ { + } )$, where D is the completion of$A \otimes _ { B } C ,$and$D ^ { + }$is the completion of the integral closure of the image of$A ^ { + } \otimes _ { B ^ { + } } C ^ { + }$in D. Note that$A ^ { \circ a } \widehat { \otimes _ { B ^ { \circ a } } } C ^ { \circ a }$is a perfectoid$K ^ { \circ a } { \mathrm { - a l g e b r a : } }$It is enough to check that$A ^ { \circ a } \otimes _ { B ^ { \circ a } } C ^ { \circ a } / \varpi$is flat over$K ^ { \circ a } / \varpi$ hence one reduces to characteristic$p .$Here, it is enough to check that$A ^ { \circ a } \otimes _ { B ^ { \circ a } } C ^ { \circ a }$ is \$-torsion free; but if$\varpi f = 0$, then$\varpi ^ { 1 / p } f ^ { 1 / p } = 0$by perfectness, hence$\varpi ^ { 1 / p } f = 0$ Continuing gives the result. In particular,$( D , D ^ { + } )$is a perfectoid afinoid$K { \mathrm { - a l g e b r a } }$ One immediately checks that it satisfies the desired universal property.

## 7. Perfectoid spaces: Etale topology

In this section, we use the term locally noetherian adic space over k for the adic spaces over k considered in [20], i.e. they are locally of the form$\operatorname { S p a } ( A , A ^ { + } )$, were A is a strongly noetherian Tate k-algebra. If additionally, they are quasicompact and quasiseparated, we call them noetherian adic spaces.

Although perfectoid rings are always reduced, and hence a definition involving lifting of nilpotents is not possible, there is a good notion of ´etale morphisms. In the following definition, k can be an arbitrary nonarchimedean field.

Definition 7.1. (i) A morphism$( R , R ^ { + } )  ( S , S ^ { + } )$of afinoid k-algebras is called finite ´etale if S is a finite ´etale R-algebra with the induced topology, and$S ^ { + }$is the integral closure of$R ^ { + }$in S.

(ii) A morphism$f : X \to Y$of adic spaces over k is called finite ´etale if there is a cover $o f Y$by open afinoids$V \subset Y$such that the preimage$U = f ^ { - 1 } ( V )$is afinoid, and the associated morphism of afinoid k-algebras

$$
(\mathcal {O} _ {Y} (V), \mathcal {O} _ {Y} ^ {+} (V)) \to (\mathcal {O} _ {X} (U), \mathcal {O} _ {X} ^ {+} (U))
$$

is finite ´etale.

(iii) A morphism$f : X \to Y$of adic spaces over k is called ´etale if for any point$x \in X$ there are open neighborhoods U and V of x and$f ( x )$and a commutative diagram

![](images/page_38_image_8.jpg)

where$j$is an open embedding and p is finite ´etale.

For locally noetherian adic spaces over$k ,$this recovers the usual notions, by Example 1.6.6 ii) and Lemma 2.2.8 of [20], respectively. We will see that these notions are useful in the case of perfectoid spaces, and will not use them otherwise. However, we will temporarily need a stronger notion of ´etale morphisms for perfectoid spaces. After proving the almost purity theorem, we will see that there is no diference. In the following let K be a perfectoid field again.

Definition 7.2. (i) A morphism$( R , R ^ { + } ) \to ( S , S ^ { + } )$of perfectoid afinoid K-algebras is called strongly finite ´etale if it is finite ´etale and additionally$S ^ { \circ a }$is a finite ´etale $R ^ { \circ a }$-algebra.

(ii) A morphism$f : X \to Y$of perfectoid spaces over K is called strongly finite ´etale if there is a cover of Y by open afinoid perfectoids$V ~ \subset ~ Y$such that the preimage $U = f ^ { - 1 } ( V )$is afinoid perfectoid, and the associated morphism of perfectoid afinoid K-algebras

$$
(\mathcal {O} _ {Y} (V), \mathcal {O} _ {Y} ^ {+} (V)) \to (\mathcal {O} _ {X} (U), \mathcal {O} _ {X} ^ {+} (U))
$$

is strongly finite ´etale.

(iii) A morphism$f : X \to Y$of perfectoid spaces over K is called strongly ´etale if for any point$x \in X$there are open neighborhoods U and V of x and$f ( x )$and a commutative diagram

![](images/page_38_image_16.jpg)

where$j$is an open embedding and p is strongly finite ´etale.

From the definitions, Proposition 6.17, and Theorem 5.25, we see that$f : X \to Y$is strongly finite ´etale, resp. strongly ´etale, if and only if the tilt$f ^ { \flat } : X ^ { \flat } \to { \dot { Y } } ^ { \flat }$is strongly finite ´etale, resp. strongly ´etale. Moreover, in characteristic$p ,$anything (finite) ´etale is also strongly (finite) ´etale.

Lemma 7.3. (i) Let$f : X \to Y$be a strongly finite ´etale, resp. strongly ´etale, morphism of perfectoid spaces and let$g : Z \to Y$be an arbitrary morphism of perfectoid spaces. Then$X \times _ { Y } Z \to Z$is a strongly finite ´etale, resp. strongly ´etale, morphism of perfectoid spaces. Moreover, the map of underlying topological spaces$| X \times _ { Z } Y | \to | X | \times _ { | Z | } | Y |$is surjective.

(ii) If in$( i )$, all spaces$X = \operatorname { S p a } ( A , A ^ { + } ) , Y = \operatorname { S p a } ( B , B ^ { + } )$and$Z = \mathrm { S p a } ( C , C ^ { + } )$are afinoid, with$( A , A ^ { + } )$strongly finite ´etale over$( B , B ^ { + } )$, then$X \times _ { Y } Z = \operatorname { S p a } ( D , D ^ { + } )$ where$D = A \otimes _ { B } C$and$D ^ { + }$is the integral closure of$C ^ { + }$in$D _ { i }$, and$( D , D ^ { + } )$is strongly finite ´etale over$( C , C ^ { + } )$

(iii) Assume that K is of characteristic p.$I f f : X \to Y$is a finite ´etale, resp. ´etale, morphism of adic spaces over k and$g : Z \to Y$is a map from a perfectoid space$Z$ to$Y$, then the fibre product$X \times _ { Y } Z$exists in the category of adic spaces over$K$, is a perfectoid space, and the projection$X \times _ { Y } Z \to Z$is finite ´etale, resp. ´etale. Moreover, the map of underlying topological spaces$\vert X \times _ { Z } Y \vert \to \vert X \vert \times _ { \vert Z \vert } \vert Y \vert$is surjective.

(iv) Assume that in the situation of$( i i i )$, all spaces$X = \operatorname { S p a } ( A , A ^ { + } ) , Y = \operatorname { S p a } ( B , B ^ { + } )$ and$Z = \operatorname { S p a } ( C , C ^ { + } )$are afinoid, with$( A , A ^ { + } )$finite ´etale over$( B , B ^ { + } )$, then$X \times _ { Y } Z$ $\mathrm { S p a } ( D , D ^ { + } )$, where$D = A \otimes _ { B } C , D ^ { + }$is the integral closure of C<sup>+</sup> in D and$( D , D ^ { + } )$is finite ´etale over$( C , C ^ { + } )$

Proof. (ii) As$A \otimes _ { B } C$is finite projective over$C ,$it is already complete. One easily deduces the universal property. Also,$D ^ { \circ a }$is finite ´etale over$C ^ { \circ a }$, as base-change preserves finite ´etale morphisms.

(i) Applying the definition of a strongly finite ´etale map, one reduces the statement about strongly finite ´etale maps to the situation handled in part (ii). Now the statement for strongly ´etale maps follows, because fibre products obviously preserve open embeddings. The surjectivity statement follows from the argument of [19], proof of Lemma 3.9 (i).

(iv) Proposition 5.23 shows that$D = A \otimes _ { B } C$is perfectoid. Therefore$\mathrm { S p a } ( D , D ^ { + } )$is a perfectoid space. One easily checks the universal property.

(iii) The finite ´etale case reduces to the situation considered in part$( \mathrm { i v } )$. Again, it is trivial to handle open embeddings, giving also the ´etale case. Surjectivity is proved as before.

Let us recall the following statement about henselian rings.

Proposition 7.4. Let A be a flat$K ^ { \circ }$-algebra such that A is henselian along$( \varpi )$. Then the categories of finite ´etale$A [ \varpi ^ { - 1 } ]$and finite ´etale$\hat { A } [ \varpi ^ { - 1 } ]$]-algebras are equivalent, where$\hat { A }$is the \$-adic completion of A.

Proof. See$\mathrm { e . g . }$. [14], Proposition 5.4.53.

We recall that \$-adically complete algebras A are henselian along$( \varpi )$, and that if$A _ { i }$ is a direct system of K<sup>◦</sup>-algebras henselian along (\$), then so is the direct limit lim$K ^ { \circ }$$( \varpi )$$A _ { i }$ In particular, we get the following lemma.

Lemma 7.5. (i) Let$A _ { i }$be a filtered direct system of complete flat$K ^ { \circ } - a l g e b r a s .$, and let $A$be the completion of the direct limit, which is again a complete flat$K ^ { \circ } - a l g e b r a$. Then we have an equivalence of categories

$$
A [ \varpi^ {- 1} ] _ {\mathrm{fét}} \cong 2 - \varinjlim A _ {i} [ \varpi^ {- 1} ] _ {\mathrm{fét}} .
$$

In particular, if$R _ { i }$is a filtered direct system of perfectoid K-algebras and R is the completion of their direct limit, then$R _ { \mathrm { f e t } } \cong 2 - \varinjlim ( R _ { i } ) _ { \mathrm { f e t } }$

(ii) Assume that K has characteristic p, and let$( R , R ^ { + } )$be a p-finite perfectoid afinoid K-algebra, given as the completed perfection of the reduced afinoid K-algebra$( S , S ^ { + } )$ of topologically finite type. Then$R _ { \mathrm { f e t } } \cong S _ { \mathrm { f e t } }$

Proof. (i) Because finite ´etale covers, and morphisms between these, are finitely presented objects, we have

$$
(\varinjlim A _ {i} [ \varpi^ {- 1} ]) _ {\text {fét}} \cong 2 - \varinjlim A _ {i} [ \varpi^ {- 1} ] _ {\text {fét}}.
$$

On the other hand, lim A<sub>i</sub> is henselian along (\$), hence the left-hand side agrees with $A [ \varpi ^ { - 1 } ] _ { \mathrm { f e t } }$by Proposition 7.4.

(ii) From part (i), we know that

$$
R _ {\mathrm{fét}} \cong 2 - \varinjlim S _ {\mathrm{fét}} ^ {1 / p ^ {n}}.
$$

But the categories$S _ { \mathrm { f e t } } ^ { 1 / p ^ { n } }$are all equivalent to$S _ { \mathrm { f e t } }$

Proposition 7.6. If$f : X \to Y$is a strongly finite ´etale morphism of perfectoid spaces, then for any open afinoid perfectoid$V \subset Y$, its preimage U is afinoid perfectoid, and

$$
(\mathcal {O} _ {Y} (V), \mathcal {O} _ {Y} ^ {+} (V)) \to (\mathcal {O} _ {X} (U), \mathcal {O} _ {X} ^ {+} (U))
$$

is strongly finite ´etale.

Proof. Tilting the situation and using Theorem 5.25, we immediately reduce to the case that K is of characteristic p. Again, we replace K by a perfectoid subfield to ensure that$R ^ { + }$is a$K ^ { \circ }$-algebra in all cases.

We may assume$Y = V = \mathrm { S p a } ( R , R ^ { + } )$is afinoid. Writing$( R , R ^ { + } )$as the completion of the direct limit of p-finite perfectoid afinoid K-algebras$( R _ { i } , R _ { i } ^ { + } )$as in Lemma 6.13, we see that$Y$is already defined as a finite ´etale cover of some$Y _ { i } = \mathrm { \bar { S p a } } ( R _ { i } , R _ { i } ^ { + } )$: Indeed, there are finitely many rational subsets of Y over which we have a finite ´etale cover; by Lemma 7.5 (i), these are defined over a finite level, and because$Y$is quasi-separated, also the gluing data over intersections (as well as the cocycle condition) are defined over a finite level.

Hence by Lemma 7.3 (ii), we are reduced to the case that$( R , R ^ { + } )$is p-finite, given as the completed perfection of$( S , S ^ { + } )$. But then X is already defined as a finite ´etale cover of$Z = \mathrm { S p a } ( S , S ^ { + } )$by similar reasoning using Lemma 7.5 (ii), and we conclude by using the result for locally noetherian adic spaces, cf. [20], Example 1.6.6 (ii), and Lemma 7.3 (iv).

Using Proposition 5.23, this shows that if K is of characteristic$p ,$then the finite ´etale covers of an afinoid perfectoid space$X = \operatorname { S p a } ( R , R ^ { + } )$are the same as the finite ´etale covers of$R .$

The same method also proves the following proposition.

Proposition 7.7. Assume that K is of characteristic p. Let$f : X \to Y$be an ´etale map of perfectoid spaces. Then for any$x \in X$, there exist afinoid perfectoid neighborhoods $x \in U \subset X , f ( U ) \subset V \subset Y$, and an ´etale morphism of afinoid noetherian adic spaces $U ^ { 0 } \to V ^ { 0 }$over K, such that$U = U ^ { 0 } \times _ { V ^ { 0 } } V$

Proof. We may assume that X and Y afinoid perfectoid, and that X is a rational subdomain of a finite ´etale cover of Y. Then one reduces to the p-finite case by the same argument as above, and hence to noetherian adic spaces.

Corollary 7.8. Strongly ´etale maps of perfectoid spaces are open. If$f : X \to Y$and $g : Y  Z$are strongly$( f i n i t e )$´etale morphisms of perfectoid spaces, then the composite $g \circ f$is strongly (finite) ´etale.

Proof. We may assume that K has characteristic$p .$The first part follows directly from the previous proposition and the result for locally noetherian adic spaces, cf. [20], Proposition 1.7.8. For the second part, argue as in the previous proposition for both$f$and $g$to reduce to the analogous result for locally noetherian adic spaces, [20], Proposition 1.6.7 (ii).

The following theorem gives a strong form of Faltings’s almost purity theorem.

Theorem 7.9. Let$( R , R ^ { + } )$be a perfectoid afinoid K-algebra, and let$X = \operatorname { S p a } ( R , R ^ { + } )$ with tilt$X ^ { \flat }$

(i) For any open afinoid perfectoid subspace$U \subset X$, we have a fully faithful functor from the category of strongly finite ´etale covers of U to the category of finite ´etale covers of ${ \mathcal { O } } _ { X } ( U )$, given by taking global sections.

(ii) For any U, this functor is an equivalence of categories.

(iii) For any finite ´etale cover$S / R$, S is perfectoid and$S ^ { \circ a }$is finite ´etale over$R ^ { \circ a }$ Moreover,$S ^ { \circ a }$is a uniformly almost finitely generated$R ^ { \circ a } - m o d u l e$

Proof. (i) By Proposition 7.6 and Theorem 5.25, the perfectoid spaces strongly finite ´etale over$U$are the same as the finite ´etale$\mathcal { O } _ { X } ( U ) ^ { \circ a } \mathrm { - a l g e b r a s }$, which are a full subcategory of the finite ´etale${ \mathcal { O } } _ { X } ( U )$-algebras.

(ii) We may assume that$U = X$. Fix a finite ´etale R-algebra S. First we check that for any$x \in X$, we can find an afinoid perfectoid neighborhood$x \in U \subset X$and a strongly finite ´etale cover$V  U$which gives via (i) the finite ´etale algebra${ \mathcal { O } } _ { X } ( U ) \otimes _ { R } S$over ${ \mathcal { O } } _ { X } ( U )$

As a first step, note that we have an equivalence of categories between the direct limit of the category of finite ´etale${ \mathcal { O } } _ { X } ( U )$)-algebras over all afinoid perfectoid neighborhoods U of x and the category of finite ´etale covers of the completion$\widehat { k ( x ) }$of the residue field at$x ,$by Lemma 7.5 (i). The latter is a perfectoid field.

$\mathrm { B y }$Theorem 3.7, the categories$\widehat { k ( x ) } _ { \mathrm { f \acute { e } t } }$and$\widehat { k ( x ^ { \flat } ) } _ { \mathrm { f e t } }$are equivalent, where$k ( x ^ { \flat } )$is the residue field of$X ^ { \flat }$<sup>[</sup> at the point$x ^ { \flat }$corresponding to x. Combining, we see that

$$
2 - \varinjlim_ {x \in U} (\mathcal {O} _ {X} (U)) _ {\mathrm{fét}} \cong 2 - \varinjlim_ {x \in U} (\mathcal {O} _ {X ^ {\flat}} (U ^ {\flat})) _ {\mathrm{fét}} .
$$

In particular, we can find$V ^ { \flat }$finite ´etale over$U ^ { \flat }$for some U such that the pullbacks of $S$to$\widehat { k ( x ) }$resp. of the global sections of$V ^ { \flat }$to$\widehat { k ( x ^ { \flat } ) }$are tilts; but then, they are already identified over some smaller neighborhood. Shrinking U, we untilt to get the desired strongly finite ´etale$V  U$

This shows that there is a cover$X = \cup U _ { i }$by finitely many rational subsets and strongly finite ´etale maps$V _ { i } \to U _ { i }$such that the global sections of$V _ { i }$are$S _ { i } = \mathcal { O } _ { X } ( U _ { i } ) \otimes _ { R }$ S. Let$S _ { i } ^ { + }$be the integral closure of${ \mathcal { O } } _ { X } ^ { + } ( U _ { i } )$in$S _ { i } ;$then$V _ { i } = \mathrm { S p a } ( S _ { i } , S _ { i } ^ { + } )$

By Lemma 7.3 (ii), the pullback of$V _ { i }$to some afinoid perfectoid$U ^ { \prime } \subset U _ { i }$has the same description, involving$\mathcal { O } _ { X } ( U ^ { \prime } ) \otimes _ { R } S$, and hence the$V _ { i }$glue to some perfectoid space Y over$X$, and$Y  X$is strongly finite ´etale. By Proposition$7 . 6 , Y$is afinoid perfectoid, i.e.$Y = \operatorname { S p a } ( A , A ^ { + } )$, with$( A , A ^ { + } )$an afinoid perfectoid K-algebra. It sufices to show that$A = S$. But the sheaf property of$\mathcal { O } _ { Y }$gives us an exact sequence

$$
0 \to A \to \prod_ {i} \mathcal {O} _ {X} (U _ {i}) \otimes_ {R} S \to \prod_ {i, j} \mathcal {O} _ {X} (U _ {i} \cap U _ {j}) \otimes_ {R} S.
$$

On the other hand, the sheaf property for${ \mathcal { O } } _ { X }$gives an exact sequence

$$
0 \to R \to \prod_ {i} \mathcal {O} _ {X} (U _ {i}) \to \prod_ {i, j} \mathcal {O} _ {X} (U _ {i} \cap U _ {j}).
$$

Because S is flat over R, tensoring is exact, and the first sequence is identified with the second sequence after$\otimes _ { R } S$. Therefore$A = S$, as desired.

(iii) This is a formal consequence of part (ii), Proposition 7.6 and Theorem 5.25.

We see in particular that any (finite) ´etale morphism of perfectoid spaces is strongly (finite) ´etale. Now one can also pullback ´etale maps between adic spaces in characteristic 0.

Proposition 7.10. Parts (iii) and (iv) of Lemma 7.3 stay true in characteristic 0.

Proof. The same proof as for Lemma 7.3 works, using Theorem 7.9 (iii).

Finally, we can define the ´etale site of a perfectoid space.

Definition 7.11. Let X be a perfectoid space. Then the ´etale site of X is the category $X _ { \mathrm { e t } }$of perfectoid spaces which are ´etale over X, and coverings are given by topological coverings. The associated topos is denoted$X _ { \mathrm { e t } } ^ { \sim }$

The previous results show that all conditions on a site are satisfied, and that a morphism$f : X \to Y$of perfectoid spaces induces a morphism of sites$X _ { \mathrm { e t } }  Y _ { \mathrm { e t } }$. Also, a morphism$f : X \to Y$from a perfectoid space X to a locally noetherian adic space$Y$ induces a morphism of sites$X _ { \mathrm { e t } }  Y _ { \mathrm { e t } }$

After these preparations, we get the technical main result.

Theorem 7.12. Let X be a perfectoid space over K with tilt$X ^ { \flat }$over$K ^ { \flat }$<sup>[</sup>. Then the tilting operation induces an isomorphism of sites$X _ { \mathrm { e t } } \cong X _ { \mathrm { e t } } ^ { \flat }$. This isomorphism is functorial in X.

Proof. This is immediate.

The almost vanishing of cohomology proved in Proposition 6.14 extends to the ´etale topology.

Proposition 7.13. For any perfectoid space X over K, the sheaf$U \mapsto { \mathcal { O } } _ { U } ( U )$is a sheaf${ \mathcal { O } } _ { X }$on$X _ { \mathrm { e t } }$, and$H ^ { i } ( X _ { \mathrm { { \acute { e } t } } } , { \mathcal { O } } _ { X } ^ { o a } ) = 0 ~ f o r ~ i > 0$if X is afinoid perfectoid.

Proof. It sufices to check exactness of

$$
0 \to \mathcal {O} _ {X} (X) ^ {\circ a} \to \prod_ {i} \mathcal {O} _ {U _ {i}} (U _ {i}) ^ {\circ a} \to \prod_ {i, j} \mathcal {O} _ {U _ {i} \times_ {X} U _ {j}} (U _ {i} \times_ {X} U _ {j}) ^ {\circ a} \to \dots
$$

for any covering of an afinoid perfectoid X by finitely many ´etale$U _ { i } \to X$given as rational subsets of finite ´etale maps to rational subsets of X. Under tilting, this reduces to the assertion in characteristic$p ,$and then to the assertion for p-finite$( R , R ^ { + } )$. In that case, one uses that the analogous sequence for noetherian adic spaces is exact up to a bounded \$-power, and hence after taking the perfection almost exact.

To make use of the ´etale site of a perfectoid space, we have to compare the ´etale sites of perfectoid spaces with those of locally noetherian adic spaces. This is possible under a certain assumption, cf. Section 2.4 of [20] for an analogous result.

Definition 7.14. Let X be a perfectoid space. Further, let$X _ { i } , i \in I$, be a filtered inverse system of noetherian adic spaces over$K$, and let$\varphi _ { i } : X \to X _ { i } , i \in I$, be a map to the inverse system.

Then we write$X \sim$lim$X _ { i }$if the mapping of underlying topological spaces$| X |$ lim$| X _ { i } |$is a homeomorphism, and for any$x \in X$with images$x _ { i } ~ \in ~ X _ { i }$, the map of residue fields

$$
\varinjlim k (x _ {i}) \to k (x)
$$

has dense image.

Remark 7.15. We recall that by assumption all$X _ { i }$are qcqs. If$X \sim \varinjlim X _ { i }$, then$| X |$is an inverse limit of spectral spaces with spectral transition maps, hence spectral, and in particular qcqs again.

Proposition 7.16. Let the situation be as in Definition$7 . 1 4 ,$, and let$Y  X _ { i }$be an ´etale morphism of noetherian adic spaces. Then$Y \times _ { X _ { i } } X \sim \varprojlim _ { j \geq i } Y \times _ { X _ { i } } X _ { j }$

Proof. The same proof as for Remark 2.4.3 of [20] works. In particular, we note that in Definition$7 . 1 4 , { \mathrm { ~ i f ~ } } | X |  \varprojlim | X _ { i } |$is bijective and the condition on residue fields is satisfied, then already$X \sim \varprojlim { X _ { i } } , \ \mathrm { i . e . } \ | X |  \varprojlim | X _ { i } |$is a homeomorphism.

With this definition, we have the following analogue of Proposition 2.4.4 of [20].

Theorem 7.17. Let the situation be as in Definition$\ 7 . 1 \textmu$. Then$X _ { \mathrm { e t } } ^ { \sim }$is a projective limit of the fibred topos$( X _ { i , \mathrm { { \acute { e } t } } } ^ { \sim } ) _ { i }$

Proof. The same proof as for Proposition 2.4.4 of [20] works, except that one uses that any ´etale morphism factors locally as the composite of an open immersion and a finite ´etale map instead of appealing to Corollary 1.7.3 of [20] on the top of page 128. The latter kind of morphisms can be descended to a finite level because of Lemma 7.5. 

As in [20], Corollary 2.4.6, this gives the following corollary.

Corollary 7.18. Let the situation be as in Definition$7 . 1 4 ,$, and let$F _ { i }$be a sheaf of abelian groups on$X _ { i , \mathrm { { \acute { e } t } } }$, with preimages$F _ { j }$on$X _ { j , \mathrm { { \acute { e } t } } }$for$j \geq i$and F on$X _ { \mathrm { e t } }$. Then the natural mapping

$$
\varinjlim H ^ {n} (X _ {j, \text { ét }}, F _ {j}) \to H ^ {n} (X _ {\text { ét }}, F)
$$

is bijective for all$n \geq 0$

In some cases, one can even say more.

Corollary 7.19. Assume that in the situation of Definition 7.14 all transition maps $X _ { j } \to X _ { i }$induce purely inseparable extensions on completed residue fields and homeomorphisms$| X _ { j } | \to | X _ { i } |$. Then$X _ { \mathrm { e t } } ^ { \sim }$is equivalent to$X _ { i , \mathrm { { \acute { e } t } } } ^ { \sim }$for any i.

Proof. Use the remark after Proposition 2.3.7 of [20].

## 8. An example: Toric varieties

Let us recall the definition of a toric variety, valid over any field k.

Definition 8.1. A toric variety over k is a normal separated scheme X of finite type over k with an action of a split torus$T \cong \mathbb { G } _ { m } ^ { k }$on X and a point$x \in X ( k )$with trivial stabilizer in$T ,$such that the T-orbit$T \cong T x = U \subset X$of x is open and dense.

We recall that toric varieties may be described in terms of fans.

Definition 8.2. Let N be a free abelian group of finite rank.

(i) A strongly convex polyhedral cone σ in$N \otimes \mathbb { R }$is a subset of the form$\sigma = \mathbb { R } _ { \geq 0 } x _ { 1 } +$ $\ldots + \mathbb { R } _ { \geq 0 } x _ { n }$for certain$x _ { 1 } , \ldots , x _ { n } \in N$, subject to the condition that σ contains no line through the origin.

(ii) A fan Σ in$N \otimes \mathbb { R }$is a nonempty finite collection of strongly convex polyhedral cones stable under taking faces, and such that the intersection of any two cones in Σ is a face of both of them.

Let$M = \operatorname { H o m } ( N , \mathbb { Z } )$be the dual lattice. To any strongly convex polyhedral cone $\sigma \subset N \otimes \mathbb { R }$, one gets the dual$\sigma ^ { \vee } \subset M \otimes \mathbb { R }$, and we associate to σ the variety

$$
U _ {\sigma} = \operatorname{Spec} k [ \sigma^ {\vee} \cap M ].
$$

We denote the function on$U _ { \sigma }$corresponding to$u \in \sigma ^ { \vee } \cap$M by$\chi ^ { u }$. If$\tau$is a face of$\sigma ,$ then$\sigma ^ { \vee } \subset \tau ^ { \vee }$, inducing an open immersion$U _ { \tau } \to U _ { \sigma }$. These maps allow us to glue a variety$X _ { \Sigma }$associated to any fan Σ. Note that$T = U _ { \{ 0 \} } = \mathrm { S p e c } k [ M ]$is a torus, which acts on$X _ { \Sigma }$with open dense orbit$U _ { \{ 0 \} } \subset X _ { \Sigma }$. Also$T$has the base point$1 \in T$, giving a point$x \in X ( k )$, making$X _ { \Sigma }$a toric variety. Let us recall the classification of toric varieties.

Theorem 8.3. Any toric variety over k is canonically isomorphic to$X _ { \Sigma }$for a unique fan Σ in$X _ { \ast } ( T ) \otimes \mathbb { R }$

We also need to recall some statements about divisors on toric varieties.

Definition/Proposition 8.4. Let$\{ \tau _ { i } \} \subset \Sigma$be the 1-dimensional cones, and fix a generator$v _ { i } \in \tau _ { i } \cap N$of$\tau _ { i } \cap N$. Each$\tau _ { i }$gives rise to$U _ { \tau _ { i } } \cong \mathbb { A } ^ { 1 } \times \mathbb { G } _ { m } ^ { k - 1 }$, giving rise to a T-invariant Weil divisor$D _ { i } = D ( \tau _ { i } )$on$X _ { \Sigma }$, defined as the closure of$\{ 0 \} \times \mathbb { G } _ { m } ^ { k - 1 }$

A T-Weil divisor is by definition an element$o f \bigoplus _ { i } \mathbb { Z } D _ { i }$. Every Weil divisor is equivalent to a T-Weil divisor. If$D = \sum a _ { i } D _ { i }$is a$T \mathrm { - } W e i l$divisor, then

$$
H^{0}(X_{\Sigma},\mathcal{O}(D)) = \bigoplus_{\substack{u\in M\\ \langle u,v_{i}\rangle \geq -a_{i}}}k\chi^{u}  .
$$

Now we adapt these definitions to the world of usual adic spaces, and to the world of perfectoid spaces. Assume first that k is a complete nonarchimedean field, and let Σ be a fan as above. Then we can associate to Σ the adic space$\mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$of finite type over k which is glued out of

$$
\mathcal {U} _ {\sigma} ^ {\mathrm{ad}} = \operatorname{Spa} (k \langle \sigma^ {\vee} \cap M \rangle , k ^ {\circ} \langle \sigma^ {\vee} \cap M \rangle)  .
$$

We note that this is not in general the adic space$X _ { \Sigma } ^ { \mathrm { a d } }$over k associated to the variety $X _ { \Sigma } { \mathrm { : } }$: For example, if$X _ { \Sigma }$is just afine space, then$\bar { \chi } _ { \Sigma } ^ { \mathrm { a d } }$will be a closed unit ball. In general, let$X _ { \Sigma , k ^ { \circ } }$be the toric scheme over$k ^ { \circ }$associated to$\Sigma$. Let$\hat { X } _ { \Sigma , k ^ { \circ } }$be the formal completion of$X _ { \Sigma , k ^ { \circ } }$along its special fibre, which is an admissible formal scheme over $k ^ { \circ }$. Then$\mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$is the generic fibre$\hat { X } _ { \Sigma , k ^ { \mathrm { o } } } ^ { \mathrm { a d } }$associated to$\hat { X } _ { \Sigma , k ^ { \circ } }$. In particular, if$X _ { \Sigma }$is proper, then$X _ { \Sigma } ^ { \mathrm { a d } } = \mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$

Similarly, if K is a perfectoid field, we can associate a perfectoid space$\chi _ { \Sigma } ^ { \mathrm { p e r f } }$over K to$\Sigma ,$which is glued out of

$$
\mathcal {U} _ {\sigma} ^ {\mathrm{perf}} = \operatorname{Spa} \left(K \langle \sigma^ {\vee} \cap M [ p ^ {- 1} ] \rangle , K ^ {\circ} \langle \sigma^ {\vee} \cap M [ p ^ {- 1} ] \rangle\right).
$$

Note that on$\mathcal { X } _ { \Sigma } ^ { \mathrm { p e r f } }$, we have a sheaf$\mathcal { O } ( D )$for any$D \in \oplus \mathbb { Z } [ p ^ { - 1 } ] D _ { i }$. Moreover, $H ^ { 0 } ( \mathcal { X } _ { \Sigma } ^ { \mathrm { p e r f } } , \mathcal { O } ( D ) )$is the free Banach-K-vector space with basis given by$\{ \chi ^ { u } \}$, where u ranges over$u \in M [ p ^ { - 1 } ]$with$\left. u , v _ { i } \right. \geq - a _ { i }$

We have the following comparison statements. Note that any toric variety$X _ { \Sigma }$comes with a map$\varphi : X _ { \Sigma } \to X _ { \Sigma }$induced from multiplication by p on$M ;$the same applies to $\mathcal { X } _ { \Sigma } ^ { \mathrm { a d } }$, etc. . For clarity, we use subscripts to denote the field over which we consider the toric variety.

Theorem 8.5. Let K be a perfectoid field with tilt$K ^ { \flat }$

(i) The perfectoid space$\chi _ { \Sigma , K } ^ { \mathrm { p e r f } }$tilts to$\mathcal { X } _ { \Sigma , K ^ { \flat } } ^ { \mathrm { p e r f } }$

(ii) The perfectoid space$\chi _ { \Sigma , K } ^ { \mathrm { p e r f } }$can be written as

$$
\mathcal {X} _ {\Sigma , K} ^ {\mathrm{perf}} \sim \varprojlim_ {\varphi} \mathcal {X} _ {\Sigma , K} ^ {\mathrm{ad}} .
$$

(iii) There is a homeomorphism of topological spaces

$$
| \mathcal {X} _ {\Sigma , K ^ {\flat}} ^ {\mathrm{ad}} | \cong \varprojlim_ {\varphi} | \mathcal {X} _ {\Sigma , K} ^ {\mathrm{ad}} | .
$$

(iv) There is an isomorphism of ´etale topoi

$$
(\mathcal {X} _ {\Sigma , K ^ {\flat}} ^ {\mathrm{ad}}) _ {\text {ét}} ^ {\sim} \cong \varprojlim_ {\varphi} (\mathcal {X} _ {\Sigma , K} ^ {\mathrm{ad}}) _ {\text {ét}} ^ {\sim} .
$$

(v) For any open subset$U \subset { \mathcal { X } } _ { \Sigma , K } ^ { \mathrm { a d } }$with preimage$V \subset \mathcal { X } _ { \Sigma , K ^ { \flat } } ^ { \mathrm { a d } }$, we have a morphism of ´etale topoi$V _ { \mathrm { e t } } ^ { \sim }  U _ { \mathrm { e t } } ^ { \sim }$, giving a commutative diagram

![](images/page_45_image_8.jpg)

Proof. This is an immediate consequence of our previous results: Part (i) can be checked on afinoid pieces, where it is an immediate generalization of Proposition 5.20. Part (ii) can be checked one afinoid pieces again, where it is easy. Then parts (iii) and (iv) follow from Theorem 7.17, Corollary 7.19 and the preservation of topological spaces and ´etale topoi under tilting. Finally, part (v) follows from Proposition 7.16, using the previous arguments.

Let us denote by$\pi : \mathcal { X } _ { \Sigma , K ^ { \flat } } ^ { \mathrm { a d } } \ \to \ \mathcal { X } _ { \Sigma , K } ^ { \mathrm { a d } }$the projection, which exists on topological spaces and ´etale topoi. In the following, we restrict to proper smooth toric varieties for simplicity.

Proposition 8.6. Let$X _ { \Sigma }$be a proper smooth toric variety. Let$\ell \neq p$be prime. Assume that$K$, and hence$K ^ { \flat }$, is algebraically closed. Then for all$i \in \mathbb { Z }$, the projection map π induces an isomorphism

$$
H ^ {i} (X _ {\Sigma , K, \mathrm{et}} ^ {\mathrm{ad}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \cong H ^ {i} (X _ {\Sigma , K ^ {\flat}, \mathrm{et}} ^ {\mathrm{ad}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}).
$$

Proof. This follows from part$( \mathrm { i v } )$of the previous theorem combined with the observation that$\varphi : X _ { \Sigma , K } ^ { \mathrm { a d } } \to X _ { \Sigma , K } ^ { \mathrm { a d } }$induces an isomorphism on cohomology with$\mathbb { Z } / \ell ^ { m } \mathbb { Z }$-coeficients. Using proper base change, this can be checked on$X _ { \Sigma , \kappa } ,$, where κ is the residue field of$K .$ But here,$\varphi$is purely inseparable, and hence induces an equivalence of ´etale topoi. 

We need the following approximation property.

Proposition 8.7. Assume that$X _ { \Sigma , K }$is proper smooth. Let$Y \subset X _ { \Sigma , K }$be a hypersurface. Let$\tilde { Y } \subset X _ { \Sigma , K } ^ { \mathrm { a d } }$be a small open neighborhood of Y. Then there exists a hypersurface $Z \subset X _ { \Sigma , K ^ { \flat } }$<sub>[</sub> such that$Z ^ { \mathrm { a d } } \subset \pi ^ { - 1 } ( \tilde { Y } )$. One can assume that$Z$is defined over a given dense subfield of$K ^ { \flat }$

Proof. Let$D = \sum a _ { i } D _ { i }$be a T-Weil divisor representing$Y$. Let$f \in H ^ { 0 } ( X _ { \Sigma , K } , { \mathcal { O } } ( D ) )$ be the equation with zero locus Y. Consider the graded ring

$$
\bigoplus_ {j \in \mathbb {Z} [ p ^ {- 1} ]} H ^ {0} (\mathcal {X} _ {\Sigma , K} ^ {\mathrm{perf}}, \mathcal {O} (j D)) = \bigoplus_ {j \in \mathbb {Z} [ p ^ {- 1} ]} \widehat {\bigoplus_ {\substack {u \in M [ p ^ {- 1} ] \\ \langle u, v _ {i} \rangle \geq - j a _ {i}}} K \chi^ {u}}  ,
$$

and let R be its completion (with respect to the obvious$K ^ { \circ }$-submodule). Here$\widehat { \oplus }$ denotes the Banach space direct sum. Then as in Proposition 5.20, R is a perfectoid K-algebra whose tilt is given by the similar construction over$K ^ { \flat }$<sup>[</sup>. Note that$D$is given combinatorially and hence transfers to$K ^ { \flat }$

We may assume that$\tilde { Y }$is given by

$$
\tilde {Y} = \left\{x \in X _ {\Sigma , K} ^ {\mathrm{ad}} \mid | f (x) | \leq \epsilon \right\},
$$

for some . In order to make sense of the inequality$| f ( x ) | \leq \epsilon$, note that$X _ { \Sigma , K }$and $\mathcal { O } ( D )$have a tautological integral model over$K ^ { \circ }$(by applying the toric constructions over$K ^ { \circ } )$, which is enough to talk about absolute values: Trivialize the line bundle$\mathcal { O } ( D )$ locally on the integral model to interpret$f$as a function; any two diferent choices difer by a unit of$K ^ { \circ }$, and hence give the same absolute value.

Now the analogue of Lemma 6.5 holds true for$R ,$, with the same proof. This implies that we can find$g \in H ^ { 0 } ( \mathcal { X } _ { \Sigma , K ^ { \flat } } ^ { \mathrm { p e r f } } , \mathcal { O } ( D ) )$) such that

$$
\pi^ {- 1} (\tilde {Y}) = \left\{x \in \mathcal {X} _ {\Sigma , K ^ {\flat}} ^ {\mathrm{perf}} \mid | g (x) | \leq \epsilon \right\}.
$$

Let$k \subset K ^ { \flat }$be a dense subfield. Changing g slightly, we can assume that

$$
g\in \bigoplus_{\substack{u\in M[p^{-1}]\\ \langle u,v_{i}\rangle \geq -ja_{i}}}k\chi^{u}  .
$$

Replacing g by a large p-power gives a regular function h on$X _ { \Sigma , K ^ { \flat } }$, such that its zero locus$Z \subset X _ { \Sigma , K ^ { \flat } }$is contained in$\pi ^ { - 1 } ( \tilde { Y } )$, as desired.

By intersecting several hypersurfaces, one arrives at the following corollary.

Corollary 8.8. Assume that$X _ { \Sigma , K }$is projective and smooth. Let$Y \subset X _ { \Sigma , K }$be a set-theoretic complete intersection, i.e. Y is set-theoretically equal to an intersection $Y _ { 1 } \cap . . . \cap Y _ { c }$of hypersurfaces$Y _ { i } \subset X _ { \Sigma , K }$, where c is the codimension of Y. Let$\tilde { Y } \subset X _ { \Sigma , K } ^ { \mathrm { a d } }$ be a small open neighborhood of Y. Then there exists a closed subvariety$Z \subset X _ { \Sigma , K ^ { \flat } }$ such that$Z ^ { \mathrm { a d } } \subset \pi ^ { - 1 } ( \tilde { Y } )$with dim$Z = \dim Y$. One can assume that$Z$is defined over a given dense subfield of$K ^ { \flat }$

Proof. The only nontrivial point is to check that the intersection over$K ^ { \flat }$will be nonempty; if the dimension was too large, one can also just cut by further hypersurfaces. For nonemptiness, choose an ample line bundle to define a notion of degree of subvarieties; then the degree of a complete intersection is determined combinatorially. As Y has positive degree, so has the corresponding complete intersection over$K ^ { \flat }$<sup>[</sup>, and in particular is nonempty.

## 9. The weight-monodromy conjecture

We first recall some facts about \`-adic representations of the absolute Galois group $G _ { k } = \operatorname { G a l } ( \bar { k } / k )$of a local field k of residue characteristic$p ,$cf. [24]. Let$q$be the cardinality of the residue field of k. Recall that the maximal pro-\`-quotient of the inertia subgroup$I _ { k } \subset G _ { k }$is given by the quotient$t _ { \ell } : I _ { k } \to \mathbb { Z } _ { \ell } ( 1 )$, which is the inverse limit of the homomorphisms$t _ { \ell , n } : I _ { k } \to \mu _ { \ell ^ { n } }$defined by choosing a system of$\ell ^ { n } .$-th roots $\varpi ^ { 1 / \ell ^ { n } }$of a uniformizer$\varpi$of$k ,$and requiring

$$
\sigma (\varpi^ {1 / \ell^ {n}}) = t _ {\ell , n} (\sigma) \varpi^ {1 / \ell^ {n}}
$$

for all$\sigma \in I _ { k }$. Now recall Grothendieck’s quasi-unipotence theorem.

Proposition 9.1. Let V be a finite-dimensional Q<sup>¯</sup> <sub>\`</sub>-representation of$G _ { k }$, given by a map$\rho : G _ { k } \to { \mathrm { G L } } ( V )$. Then there is an open subgroup$I _ { 1 } \subset I _ { k }$such that for all$\sigma \in I _ { 1 }$ the element$\rho ( \sigma ) \in \operatorname { G L } ( V )$is unipotent, and in this case there is a unique nilpotent morphism$N : V \to V ( - 1 )$such that for all$\sigma \in I _ { 1 }$9

$$
\rho (\sigma) = \exp (N t _ {\ell} (g)).
$$

We fix an isomorphism$\mathbb { Q } _ { \ell } ( 1 ) \cong \mathbb { Q } _ { \ell }$in order to consider N as a nilpotent endomorphism of$V .$. Changing the choice of isomorphism$\mathbb { Q } _ { \ell } ( 1 ) \cong \mathbb { Q } _ { \ell }$replaces N by a scalar multiple, which will have no efect on the following discussion. From uniqueness of$N ,$ it follows that for any geometric Frobenius element$\Phi \in G _ { k }$, we have$N \Phi = q \Phi N$

Also recall the general monodromy filtration.

Definition/Proposition 9.2. Let V be a finite-dimensional vector space over any field, and let$N : V \to V$be a nilpotent morphism. Then there is a unique separated and exhaustive increasing filtration${ \mathrm { F i l } } _ { i } ^ { N } V \subset V , i \in \mathbb { Z } ,$, called the monodromy filtration, such that$N ( \mathrm { F i l } _ { i } ^ { N } V ) \subset \mathrm { F i l } _ { i - 2 } ^ { N } V$for all$i \in \mathbb { Z }$and$\mathrm { g r } _ { i } ^ { N } V \cong \mathrm { g r } _ { - i } ^ { N } V$via$N ^ { i }$for all$i \geq 0$

In fact, we have the formula

$$
\mathrm{Fil} _ {i} ^ {N} V = \sum_ {i _ {1} - i _ {2} = i} \ker N ^ {i _ {1} + 1} \cap \mathrm{im} N ^ {i _ {2}}
$$

for the monodromy filtration. Now we can formulate the weight-monodromy conjecture.

Conjecture 9.3 (Deligne, [9]). Let X be a proper smooth variety over$k ,$, and let$V =$ $H ^ { i } ( X _ { \bar { k } } , \bar { \mathbb { Q } } _ { \ell } )$. Then for all$j \in \mathbb Z$and for any geometric Frobenius$\Phi \in G _ { k }$, all eigenvalues of Φ on$\mathrm { g r } _ { i } ^ { N } V$are Weil numbers of weight$i + j$, i.e. algebraic numbers α such that $| \alpha | = q ^ { ( i + j ) / 2 }$for all complex absolute values.

We note that in order to prove this conjecture, one is allowed to replace k by a finite extension. Using the formalism of$\zeta -$and L-functions, the conjecture has the following interpretation. Let K be a global field, and let$X / \mathbb { K }$be a proper smooth variety. Choose some integer i. Recall that the L-function associated to the i-th \`-adic cohomology group$H ^ { i } ( X ) = H ^ { i } ( X _ { \bar { \mathbb { K } } } , \bar { \mathbb { Q } } _ { \ell } )$of X is defined as a product

$$
L (H ^ {i} (X), s) = \prod_ {v} L _ {v} (H ^ {i} (X), s),
$$

where the product runs over all places v of$K$. Let us recall the definition of the local factor at a finite prime v not dividing$\ell ,$whose local field is$k \mathbf { i }$

$$
L _ {v} (H ^ {i} (X), s) = \det (1 - q ^ {- s} \Phi | H ^ {i} (X) ^ {I _ {k}}) ^ {- 1}.
$$

At primes of good reduction, the Weil conjectures imply that all poles of this expression have real part$\frac { i } { 2 }$. Moreover, one checks in the usual way that hence the product defining $L ( H ^ { i } ( X ) , s )$is absolutely convergent when the real part of s is greater than$\textstyle { \frac { i } { 2 } } + 1$, except possibly for finitely many factors. The weight-monodromy conjecture implies that all other local factors will not have any poles of real part greater than$\frac { i } { 2 }$

Over equal characteristic local fields, Deligne, [10], turned this argument into a proof:

Theorem 9.4. Let C be a curve over$\mathbb { F } _ { q } , x \in C ( \mathbb { F } _ { q } )$, such that k is the local field of C at x. Let X be a proper smooth scheme over$C \setminus \{ x \}$. Then the weight-monodromy conjecture holds true for$X _ { k } = X \times _ { C \backslash \{ x \} } \operatorname { S p e c } k$

Let us give a brief summary of the proof. Let$f : X  C \backslash \{ x \}$be the proper smooth morphism. Possibly replacing C by a finite cover, we may assume that the action of$I _ { k }$ on$V = H ^ { i } ( X _ { \bar { k } } , \bar { \mathbb { Q } } _ { \ell } )$is unipotent. One considers the local system$R ^ { i } f _ { * } \mathbb { \ Q } _ { \ell }$on$C \backslash \{ x \}$. By the Weil conjectures, this sheaf is pure of weight i. From the formalism of L-functions for sheaves over curves, one deduces semicontinuity of weights, which in this situation means that on the invariantsV<sup>I</sup>k$V ^ { I _ { k } }$of$V = H ^ { i } ( X _ { \bar { k } } , \bar { \mathbb { Q } } _ { \ell } )$, all occuring weights are$\leq i .$. A similar property holds true for all tensor powers of V, and for all tensor powers of the dual$V ^ { \vee }$. Then one applies the following lemma from linear algebra, which applies for all local fields$k$

Lemma 9.5. Let V be an \`-adic representation of$G _ { k }$, on which$I _ { k }$acts unipotently. Then$\mathrm { g r } _ { j } ^ { N } V$is pure of weight$i + j$for all$j \in \mathbb Z$if and only if for all$j \geq 0$, all weights on$( V ^ { \otimes j } ) ^ { I _ { k } }$are at most$i j$, and all weights on$( ( V ^ { \vee } ) ^ { \otimes j } ) ^ { I _ { k } }$are at most$- i j$

Our main theorem is the following.

Theorem 9.6. Let k be a local field of characteristic 0. Let$Y$be a geometrically connected proper smooth variety over k such that$Y$is a set-theoretic complete intersection in a projective smooth toric variety$X _ { \Sigma }$. Then the weight-monodromy conjecture is true for Y.

Proof. Let$\varpi \in k$be a uniformizer, and let K be the completion of$k ( \varpi ^ { 1 / p ^ { \infty } } )$; then K is perfectoid. Let$K ^ { \flat }$be its tilt. Then$K ^ { \flat }$<sup>[</sup> is the completed perfection of$k ^ { \prime } = \mathbb { F } _ { q } ( \mathbf { \Sigma } ( t ) )$), where$t = \varpi ^ { \flat }$<sup>[</sup>. This gives an isomorphism between the absolute Galois groups of$K$ and$k ^ { \prime }$. The notion of weights and the monodromy operator N is compatible with this isomorphism of Galois groups.

$\mathrm { B y }$Theorem 3.6 a) of [21], there is some open neighborhood$\tilde { Y }$of$Y _ { K } ^ { \mathrm { a d } }$in$X _ { \Sigma , K } ^ { \mathrm { a d } }$such that$\tilde { Y } _ { \mathbb { C } _ { p } }$and$Y _ { \mathbb { C } _ { p } } ^ { \mathrm { a d } }$have the same$\mathbb { Z } / \ell \mathbb { Z }$-cohomology.$\mathrm { B y }$induction, they have the same $\mathbb { Z } / \ell ^ { m } \mathbb { Z }$-cohomology for all$m \geq 1$. Also recall the following comparison theorem.

Theorem 9.7 ([20, Theorem 3.8.1]). Let X be an algebraic variety over an algebraically closed nonarchimedean field$k ,$, with associated adic space$X ^ { \mathrm { a d } }$. Then

$$
H ^ {i} (X _ {\mathrm{et}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \cong H ^ {i} (X _ {\mathrm{et}} ^ {\mathrm{ad}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}).
$$

By Corollary 8.8, there is some closed subvariety$Z \subset X _ { \Sigma , K ^ { \flat } }$such that$Z ^ { \mathrm { a d } } \subset \pi ^ { - 1 } ( \tilde { Y } )$ and dim$Z =$dim Y. Moreover, we can assume that$Z$is defined over a global field and geometrically irreducible. Let$Z ^ { \prime }$be a projective smooth alteration of$Z .$. We get a commutative diagram of ´etale topoi of adic spaces

![](images/page_48_image_9.jpg)

There is a canonical action of the absolute Galois group$G = G _ { K } = G _ { K ^ { \flat } }$on this diagram such that all morphisms are G-equivariant. Using the comparison theorem, this induces a G-equivariant map

$$
f ^ {*}: H ^ {i} (Y _ {\mathbb {C} _ {p}, \mathrm{et}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) = H ^ {i} (\tilde {Y} _ {\mathbb {C} _ {p}, \mathrm{et}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \to H ^ {i} (Z _ {\mathbb {C} _ {p} ^ {\flat}, \mathrm{et}} ^ {\prime}, \mathbb {Z} / \ell^ {m} \mathbb {Z}),
$$

compatible with the cup product. Formally taking the inverse limit and tensoring with $\bar { \mathbb { Q } } _ { \ell }$, it follows that we get a G-equivariant map

$$
H ^ {i} (Y _ {\mathbb {C} _ {p}, \mathrm{et}}, \bar {\mathbb {Q}} _ {\ell}) \to H ^ {i} (Z _ {\mathbb {C} _ {p} ^ {\flat}, \mathrm{et}} ^ {\prime}, \bar {\mathbb {Q}} _ {\ell}) .
$$

Lemma 9.8. For$i = 2$dim$Y$, this is an isomorphism.

Proof. For all$m ,$we have a commutative diagram

$$
\begin{array}{c c} H ^ {2 \dim Y} (X _ {\Sigma , \mathbb {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \xleftarrow {\cong} H ^ {2 \dim Y} (X _ {\Sigma , \mathbb {C} _ {p}, \acute {\mathrm{et}}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \\ \Big \downarrow & \Big \downarrow \\ H ^ {2 \dim Y} (\pi^ {- 1} (\tilde {Y}) _ {\mathbb {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \longleftarrow H ^ {2 \dim Y} (\tilde {Y} _ {\mathbb {C} _ {p}, \acute {\mathrm{et}}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \\ \Big \downarrow & \Big \downarrow \cong \\ H ^ {2 \dim Y} (Z _ {\mathbb {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}} ^ {\prime}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) & H ^ {2 \dim Y} (Y _ {\mathbb {C} _ {p}, \acute {\mathrm{et}}}, \mathbb {Z} / \ell^ {m} \mathbb {Z}) \end{array}
$$

The isomorphism in the top row is from Proposition 8.6. We can pass to the inverse limit over m and tensor with$\bar { \mathbb { Q } } _ { \ell }$. If

$$
H ^ {2 \dim Y} (Y _ {\mathbb {C} _ {p}, \acute {\mathrm{et}}}, \bar {\mathbb {Q}} _ {\ell}) \to H ^ {2 \dim Y} (Z _ {\mathbb {C} _ {p} ^ {b}, \acute {\mathrm{et}}} ^ {\prime}, \bar {\mathbb {Q}} _ {\ell}) .
$$

is not an isomorphism, it is the zero map, and hence the diagram implies that the restriction map

$$
H ^ {2 \dim Y} (X _ {\Sigma , \mathbb {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}}, \bar {\mathbb {Q}} _ {\ell}) \to H ^ {2 \dim Y} (Z _ {\mathbb {C} _ {p} ^ {\flat}, \acute {\mathrm{et}}} ^ {\prime}, \bar {\mathbb {Q}} _ {\ell})
$$

is the zero map as well. But the dim Y -th power of the first Chern class of an ample line bundle on$X _ { \Sigma , \mathbb { C } _ { p } ^ { \flat } }$will have nonzero image in$H ^ { 2 \dim Y } ( Z _ { \mathbb { C } _ { p } ^ { \flat } , \dot { \mathrm { e t } } } ^ { \prime } , \bar { \mathbb { Q } } _ { \ell } )$

Now the Poincar´e duality pairing implies that$H ^ { i } ( Y _ { \mathbb { C } _ { p } , \mathrm { { \hat { e } t } } } , { \bar { \mathbb { Q } } } _ { \ell } )$is a direct summand of $H ^ { i } ( Z _ { \mathbb { C } _ { p } ^ { \flat } , \dot { \operatorname { e t } } } ^ { \prime } , \bar { \mathbb { Q } } _ { \ell } )$. By Deligne’s theorem,$H ^ { i } ( Z _ { \mathbb { C } _ { p } ^ { \flat } , \dot { \operatorname { e t } } } ^ { \prime } , \bar { \mathbb { Q } } _ { \ell } )$satisfies the weight-monodromy conjecture, and hence so does its direct summand$H ^ { i } ( Y _ { \mathbb { C } _ { p } , \mathrm { { \hat { e } t } } } , { \bar { \mathbb { Q } } } _ { \ell } )$

## References

[1] V. G. Berkovich. Spectral theory and analytic geometry over non-Archimedean fields, volume 33 of Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 1990.

[2] S. Bosch, U. G¨untzer, and R. Remmert. Non-Archimedean analysis, volume 261 of Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Springer-Verlag, Berlin, 1984. A systematic approach to rigid analytic geometry.

[3] S. Bosch and W. L¨utkebohmert. Formal and rigid geometry. I. Rigid spaces. Math. Ann., 295(2):291–317, 1993.

[4] P. Boyer. Monodromie du faisceau pervers des cycles ´evanescents de quelques vari´et´es de Shimura simples. Invent. Math., 177(2):239–280, 2009.

[5] P. Boyer. Conjecture de monodromie-poids pour quelques vari´et´es de Shimura unitaires. Compos. Math., 146(2):367–403, 2010.

[6] A. Caraiani. Local-global compatibility and the action of monodromy on nearby cycles. arXiv:1010.2188.

[7] J.-F. Dat. Th´eorie de Lubin-Tate non-ab´elienne et repr´esentations elliptiques. Invent. Math., 169(1):75–152, 2007.

[8] A. J. de Jong. Smoothness, semi-stability and alterations. Inst. Hautes Etudes Sci. Publ. Math.<sup>´</sup> , (83):51–93, 1996.

[9] P. Deligne. Th´eorie de Hodge. I. In Actes du Congr\`es International des Math´ematiciens (Nice, 1970), Tome 1, pages 425–430. Gauthier-Villars, Paris, 1971.

[10] P. Deligne. La conjecture de Weil. II. Inst. Hautes Etudes Sci. Publ. Math.<sup>´</sup> , (52):137–252, 1980.

[11] G. Faltings. p-adic Hodge theory. J. Amer. Math. Soc., 1(1):255–299, 1988.

[12] G. Faltings. Almost ´etale extensions. Ast´erisque, (279):185–270, 2002. Cohomologies p-adiques et applications arithm´etiques, II.

[13] J.-M. Fontaine and J.-P. Wintenberger. Extensions alg´ebrique et corps des normes des extensions APF des corps locaux. C. R. Acad. Sci. Paris S´er. A-B, 288(8):A441–A444, 1979

[14] O. Gabber and L. Ramero. Almost ring theory, volume 1800 of Lecture Notes in Mathematics. Springer-Verlag, Berlin, 2003.

[15] M. Harris and R. Taylor. The geometry and cohomology of some simple Shimura varieties, volume 151 of Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 2001. With an appendix by Vladimir G. Berkovich.

[16] E. Hellmann. On arithmetic families of filtered ϕ-modules and crystalline representations. 2011. arXiv:1010.4577.

[17] M. Hochster. Prime ideal structure in commutative rings. Trans. Amer. Math. Soc., 142:43–60, 1969.

[18] R. Huber. Continuous valuations. Math. Z., 212(3):455–477, 1993.

[19] R. Huber. A generalization of formal schemes and rigid analytic varieties. Math. Z., 217(4):513–551, 1994.

[20] R. Huber. Etale cohomology of rigid analytic varieties and adic spaces <sup>´</sup> . Aspects of Mathematics, E30. Friedr. Vieweg & Sohn, Braunschweig, 1996.

[21] R. Huber. A finiteness result for direct image sheaves on the ´etale site of rigid analytic varieties. J. Algebraic Geom., 7(2):359–403, 1998.

[22] L. Illusie. Complexe cotangent et d´eformations. I. Lecture Notes in Mathematics, Vol. 239. Springer-Verlag, Berlin, 1971.

[23] L. Illusie. Complexe cotangent et d´eformations. II. Lecture Notes in Mathematics, Vol. 283. Springer-Verlag, Berlin, 1972.

[24] L. Illusie. Autour du th´eor\`eme de monodromie locale. Ast´erisque, (223):9–57, 1994. P´eriodes padiques (Bures-sur-Yvette, 1988).

[25] T. Ito. Weight-monodromy conjecture for p-adically uniformized varieties. Invent. Math., 159(3):607–656, 2005.

[26] T. Ito. Weight-monodromy conjecture over equal characteristic local fields. Amer. J. Math., 127(3):647–658, 2005.

[27] K. Kedlaya and R. Liu. Relative p-adic Hodge theory, I: Foundations. http://math.mit.edu/∼kedlaya/papers/relative-padic-Hodge1.pdf.

[28] D. Quillen. On the (co-) homology of commutative rings. In Applications of Categorical Algebra (Proc. Sympos. Pure Math., Vol. XVII, New York, 1968), pages 65–87. Amer. Math. Soc., Providence, R.I., 1970.

[29] M. Rapoport and T. Zink. Uber die lokale Zetafunktion von Shimuravariet¨aten. Monodromiefiltra-<sup>¨</sup> tion und verschwindende Zyklen in ungleicher Charakteristik. Invent. Math., 68(1):21–101, 1982.

[30] S. W. Shin. Galois representations arising from some compact Shimura varieties. Ann. of Math. (2), 173(3):1645–1741, 2011.

[31] J. Tate. Rigid analytic spaces. Invent. Math., 12:257–289, 1971.

[32] R. Taylor and T. Yoshida. Compatibility of local and global Langlands correspondences. J. Amer. Math. Soc., 20(2):467–493, 2007.

[33] T. Terasoma. Monodromy weight filtration is independent of \`. 1998. arXiv:math/9802051.