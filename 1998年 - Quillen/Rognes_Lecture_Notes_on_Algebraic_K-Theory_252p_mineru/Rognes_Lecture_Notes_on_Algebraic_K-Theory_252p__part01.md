# Lecture Notes on Algebraic K-Theory

John Rognes

April 29th 2010

## Contents

1 Introduction 1
1.1 Representations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Symmetries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.4 Categories . . . . . . . . . . . . . . . . . . . . . 7
1.5 Classifying spaces . . . . Ries. 8
1.6 Monoid structures 11
1.7 Group completion 14
1.8 Loop space completion 16
1.9 Grothendieck-Riemann-Roch 17
1.10 Vector fields on spheres 18
1.11 Wall's finiteness obstruction 19
1.12 Homology of linear groups 22
1.13 Homology of symmetric groups 24
1.14 Ideal class groups 25
1.15 Automorphisms of manifolds 27
2 Categories and functors 29
2.1 Sets and classes 29
2.2 Categories 30
2.3 Functors 35
2.4 Isomorphisms and groupoids 39
2.5 Ubiquity 43
2.6 Correspondences 46
2.7 Representations of groups and rings 47
2.8 Few objects 49
2.9 Few morphisms 52
3 Transformations and equivalences 56
3.1 Natural transformations 56
3.2 Natural isomorphisms and equivalences 60
3.3 Tannaka-Krein duality 66
3.4 Adjoint pairs of functors 69
3.5 Decategorification 77

## CONTENTS

4 Universal properties 81
4.1 Initial and terminal objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Categories under and over . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.3 Colimits and limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.4 Cofibered and fibered categories. 96
5 Homotopy theory 99
5.1 Topological spaces 99
5.2 CW complexes 110
5.3 Compactly generated spaces 113
5.4 Cofibrations 113
5.5 The gluing lemma 120
5.6 Homotopy groups 125
5.7 Weak homotopy equivalences 126
5.8 Fibrations 127
6 Simplicial methods 130
6.1 Combinatorial complexes 130
6.2 Simplicial sets 138
6.3 The role of non-degenerate simplices 147
6.4 The role of degenerate simplices 156
6.5 Bisimplicial sets 159
6.6 The realization lemma 165
6.7 Subdivision 168
6.8 Realization of fibrations 168
7 Homotopy theory of categories 171
7.1 Nerves and classifying spaces 171
7.2 The bar construction 180
7.3 Quillen's theorem A 181
7.4 Theorem A\* 184
7.5 Quillen's theorem B 185
7.6 The simplex category 185
7.7 ∞-categories 190
8 Waldhausen K-theory 191
8.1 Categories with cofibrations 192
8.2 Categories of weak equivalences 202
8.3 The S.-construction 206
8.4 Algebraic K-groups 214
8.5 The additivity theorem 218
8.6 Delooping K-theory 224
8.7 The iterated S.-construction 227
8.8 The spectrum level rank filtration 229
8.9 Algebraic K-theory of finite sets 236
9 Abelian and exact categories 240
9.1 Additive categories 240
9.2 Abelian categories 240
9.3 Exact categories 242

## CONTENTS

10 Quillen $K$-theory 244  
10.1 The $Q$-construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244  
10.2 The cofinality theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244  
10.3 The resolution theorem . . . . . . . . . . . . . . . . . . . . . . . . . . 244  
10.4 The devissage theorem . . . . . . . . . . . . . . . . . . . . . 244  
10.5 The localization sequence . . . . . . . . . . . . . . . 244

## Foreword

These are notes intended for the author’s algebraic K-theory lectures at the University of Oslo in the spring term of 2010. The main references for the course will be:

• Daniel Quillen’s seminal paper “Higher algebraic K-theory. I” [55], sections 1 though 5 or 6, including his theorems A and B concerning the homotopy theory of categories, the definition of the algebraic K-theory of an exact category using the Q-construction, the additivity, resolution, devissage and localization theorems, and probably the fundamental theorem;

• Friedhelm Waldhausen’s foundational paper [68] “Algebraic K-theory of spaces”, sections 1.1 through 1.6 and 1.9, including the definition of the algebraic K-theory of a category with cofibrations and weak equivalences using the S -construction, the additivity, generic fibration and approximation theorems, and the relation with the Q-construction;

• Saunders Mac Lane’s textbook “Categories for the Working Mathematician” [40] on category theory, where parts of chapters I though IV, VII, VIII, XI and XII are relevant;

• Allen Hatcher’s textbook “Algebraic Topology” [26] on homotopy theory, drawing on parts of sections 4.1 on higher homotopy groups, 4.K on quasi-fibrations and the appendix;

• The author’s PhD thesis “A spectrum level rank filtration in algebraic Ktheory” [57], for the iterated S<sub>•</sub>-construction and a proof of the Barratt– Priddy–Quillen theorem.

Background material and other connective tissue will be provided in these notes. As the list above shows, the selection of material may be a bit subjective. Comments and corrections are welcome—please write to rognes@math.uio.no .

## Chapter 1

## Introduction

What is algebraic K-theory?

Here is a preliminary discussion, intended to lead the way into the subject and to motivate some of the constructions involved. Such a preamble may be useful, since modern algebraic K-theory relies on quite a large body of technical foundations, and it is easily possible to get sidetracked by developing one or more of these foundations to their fullest, such as the model category theory of simplicial sets, before reaching the natural questions to be studied by algebraic K-theory.

There may not even be a common agreement about what these natural questions are. Algebraic K-theory is in some sense a meeting ground for several other mathematical subjects, including number theory, geometric topology, algebraic geometry, algebraic topology and operator algebras, relating to constructions like the ideal class group, Whitehead torsion, coherent sheaves, vector bundles and index theory.

It is quite possible to give a course that outlines all of these neighboring subjects. However, the aim for this course will instead be to focus on algebraic K-theory itself, rather than on these applications of algebraic K-theory. In particular, we will focus directly on “higher algebraic K-theory”, the definition of which requires more categorical and homotopy theoretic subtlety than the simpler algebraic group completion process that is most immediately needed for some of the applications.

After giving a first overview of the subject matter, we will therefore spend some time on necessary background, starting with category theory and continuing with homotopy theory. The aim is to spend the minimal amount of time on this that is needed for an honest treatment, but not less. Then we turn to the construction and fundamental theorems of higher algebraic K-theory. Here we will reverse the historical order, at least as it is visible in the published record, by first working with Waldhausen’s simplicial construction of algebraic K-theory, called the S<sub>•</sub>-construction, and only later will we specialize this to Quillen’s purely categorical construction, known as the Q-construction.

The specialization may turn out to only be an apparent restriction, as ongoing work by Clark Barwick and the author extends the Q-construction to accept ∞-categories as input, but this is work in progress.

## 1.1 Representations

Many mathematical objects come to life through their representations by actions on other, simpler, mathematical objects. Historically this was very much so for groups, which were at first realized as permutation groups, with each group element acting by an invertible substitution on some fixed set. We now say that the group acts on the given set, and this gives a discrete representation of the group. Similarly, one may consider the action of a group through linear isomorphisms on a vector space, and this leads to the most standard meaning of a representation. Concentrating on the additive structure of the vector space, we may also consider actions of rings on abelian groups, which leads to the additive representations of a ring through its module actions.

[[Retractive spaces over X.]]

Example 1.1.1. In more detail, given a group G with neutral element e we may consider the class of left G-sets, which are sets X together with a function

$$
G \times X \to X
$$

taking$( g , x )$to$g \cdot x = g x .$, such that$( g h ) \cdot x = g \cdot ( h \cdot x )$and$e \cdot x = x$for all $g , h \in G$and$x \in X$. These are discrete representations of groups.

Example 1.1.2. Similarly, given a ring R with unit element 1 we may consider the class of left R-modules, which are abelian groups M together with a homomorphism

$$
R \otimes M \to M
$$

taking$r \otimes m$to$r \cdot m = r m$, such that$( r s ) \cdot m = r \cdot ( s \cdot m )$and$1 \cdot m = m$for all$r , s \in R$and$m \in M$. These are additive representations of rings.

Example 1.1.3. Given a group G and a field k, we can form the group ring $k [ G ]$, and a left$k [ G ]$-module M is then the same as a k-linear representation of $G ,$since the scalar action by$k \subseteq k [ G ]$on M makes M a k-vector space. Most of the time G and k will come with topologies, and it will then be natural to focus on topological modules with continuous actions.

Example 1.1.4. [[Retractive spaces over$X . ] ]$

## 1.2 Classification

A basic problem is to organize, or classify, the possible representations of a given mathematical object. This way, if such a representation appears “in nature”, perhaps arising from a separate mathematical problem or construction, then we may wish to understand how this representation fits into the classification scheme for these mathematical objects.

In this context, we are usually willing to view certain pairs of representations as being equivalent for all practical purposes. For example, two G-sets X and Y, with action functions$G \times X \to X$and$G \times Y \to Y$, are said to be isomorphic if there is an invertible function$f \colon X \to Y$such that$g \cdot f ( x ) = f ( g \cdot x )$in$Y$for all$g \in G$and$x \in X$. Functions respecting the given G-actions in this way are said to be$G \mathrm { - } e q u$ivariant. This way any statement about the elements of X and its G-action can be translated into a logically equivalent statement about the elements of Y and its G-action, by everywhere replacing each element$x \in X$by the corresponding element$f ( x ) \in Y$, and likewise replacing the G-action on$X$ by the G-action on$Y$. Since f is assumed to be invertible, we can equally well go the other way, replacing elements$y \in Y$by their images$f ^ { - 1 } ( y ) \in X$under the inverse function$f ^ { - 1 } \colon Y \to X$

We are therefore usually really asking for a classification of all the possible mathematical objects of a given kind, up to isomorphism. That is, we are asking for an understanding of the collection of isomorphism classes of the given mathematical object.

Example 1.2.1. If$G = \{ e \}$is the trivial group, then a G-set is the same thing as a set, and the classification of G-sets up to isomorphism is the same as the classification of sets up to one-to-one correspondence of their elements, i.e., up to bijection. More-or-less by definition, this classification problem is solved by the theory of cardinalities. As a key special case, if we are only interested in finite sets, then two finite sets X and$Y$can be put in bijective correspondence if and only if they have the same number of elements,${ \mathrm { i . e . , i f } } \# X = \# Y$, where $\# X \in \mathbb { N } _ { 0 } = \{ 0 , 1 , 2 , \dots \}$denotes the non-negative integer obtained by counting the elements of X. In this case the counting process establishes a one-to-one correspondence between the elements of X and the elements of the standard set

$$
\mathbf {n} = \{1, 2, \dots , n \}
$$

with n elements, so the classification of finite sets up to bijection is given by this identification between the collection of isomorphism classes and the set of non-negative integers.

Example 1.2.2. Returning to the case of a general group$G ,$, to each G-set X and each element$x \in X$, we can associate a subset

$$
G x = \{g \cdot x \in X \mid g \in G \}
$$

of X, called the G-orbit of$x \in X$, and a subgroup

$$
G _ {x} = \{g \in G \mid g \cdot x = x \}
$$

of$G ,$called the stabilizer subgroup of$x \in X$. There is a natural isomorphism

$$
f _ {x} \colon G / G _ {x} \stackrel {\cong} {\longrightarrow} G x
$$

from the set of left cosets$g G _ { x }$of$G _ { x }$in$G$to the G-orbit of$x ,$, taking the coset $g G _ { x }$to the element$g \cdot x \in X$. Here$G / G _ { x }$is a left G-set, with the G-action $G \times G / G _ { x } \to G / G _ { x }$that takes$( g , h G _ { x } )$to$g h G ,$and the isomorphism$f _ { x }$ respects the G-actions, as required for an isomorphism of G-sets.

Given two elements$x , y \in X$, the G-orbits Gx and Gy are either equal or disjoint, and in general the G-set X can be canonically decomposed as the disjoint union of its G-orbits. In the special case when there is only one$G \mathrm { - }$ orbit, so that$G x = X$for some$x \in X$, we say that the G-action is transitive. To classify G-sets we first classify the transitive G-sets, and then apply this classification one orbit at a time, for general G-sets.

If X is a transitive G-set, choosing an element$x \in X$we get an isomorphism $f _ { x } \colon G / G _ { x } \to G x = X$, as above. Hence we would like to say that X corresponds to the subgroup$G _ { x } \subseteq G$. However, the stabilizer subgroup$G _ { x }$will in general depend on the choice of element x. If$y \in X$is another element, then there is also an isomorphism$f _ { y } \colon G / G _ { y } \to G y = X$, so we should also say that X corresponds to the subgroup$G _ { y } .$What is the relation between$G _ { x }$and$G _ { y } ?$ Well, since the G-action is transitive, we know that$y \in G x$, so there must exist an element$h \in G$with$h \cdot x = y$. Then

$$
G _ {y} = h G _ {x} h ^ {- 1}
$$

since$g \cdot y = y$is equivalent to$g h \cdot x = h \cdot x$, hence also equivalent to$h ^ { - 1 } g h \in G _ { x }$ or$g \in h G _ { x } h ^ { - 1 }$. Hence it is the conjugacy class$\left( G _ { x } \right)$of$G _ { x }$as a subgroup of $G$that is a well-defined invariant of the transitive G-set X. Checking a few details, the conclusion is that the classification of transitive G-sets is given by this identification with the set of conjugacy classes of subgroups of$G .$The inverse identification takes the conjugacy class (H) of a subgroup$H \subseteq G$to the isomorphism class of the transitive left G-set$X = G / H$

For example, if$G = C _ { p }$is cyclic of prime order$p ,$the possible subgroups are $H = \{ e \}$and$H = G$, and the transitive G-sets are$G / \{ e \} \cong G$and$G / G \cong * \ ( \mathrm { a }$ one-point set).

Exercise 1.2.3. Let G be a finite group. Let$\operatorname { C o n j S u b } ( G )$be the set of conjugacy classes of subgroups of G. Show that the isomorphism classes of finite G-sets X are in one-to-one correspondence with the functions

$$
\nu \colon \operatorname{ConjSub} (G) \to \mathbb {N} _ {0}.
$$

The correspondence takes such a function ν to the isomorphism class of the G-set

$$
X (\nu) = \coprod_ {(H)} \coprod^ {\nu (H)} G / H.
$$

What about the case when G is not finite?

[[Classify k-linear G-representations, at least in the semi-simple case when G is finite and #G is invertible in k. Maybe focus on$k = \mathbb { R }$and C.]]

Example 1.2.4. For a general ring R, the classification of all R-modules up to R-linear isomorphism is a rather complicated matter. For later purposes we are at least interested in the finitely generated free R-modules M, with are isomorphic to the finite direct sums

$$
R ^ {n} = R \oplus \dots \oplus R
$$

with n copies of R on the right hand side, and the finitely generated projective Rmodules$P _ { : }$, which arise as direct summands of finitely generated free R-modules, so that there is a sum decomposition

$$
P \oplus Q \cong R ^ {n}
$$

of R-modules. Note that the composite R-linear homomorphism

$$
R ^ {n} \cong P \oplus Q \xrightarrow {p r} P \xrightarrow {i n} P \oplus Q \cong R ^ {n}
$$

is represented by an$n \times n$matrix B, which is idempotent in the sense that $B ^ { 2 } = B$. Projective modules are therefore related to idempotent matrices. We are also interested in finitely generated R-modules M, for which there exists a surjective R-linear homomorphism

$$
f \colon R ^ {n} \to M
$$

This notion is most interesting for Noetherian rings$R ,$since for such R the kernel$\ker ( f )$will also be a finitely generated R-module.

[[Reference to coherence for non-Noetherian$R . ] ]$

When$R = k$is a field, an R-module is the same as a k-vector space, and the notions of finitely generated, finitely generated free and finitely generated projective all agree with the condition of being finite dimensional. In this case the classification of finite dimensional vector spaces is given by the dimension function, establishing a one-to-one correspondence between isomorphism classes of finite dimensional vector spaces and non-negative integers.

When R is a PID (principal ideal domain), the classification of finitely generated R-modules is well known. In this case, a finitely generated R-module is projective if and only if it is free, so finitely generated projective R-modules are classified by their rank, again a non-negative integer.

When R is a Dedekind domain, e.g. the ring of integers in a number field, the classification of finitely generated projective R-modules is due [[Check]] to Ernst Steinitz, see John Milnor’s “Introduction to algebraic$K \mathrm { - t h e o r y ^ { \prime \prime } ~ [ 4 8 , \ S 1 ] }$ Every nonzero projective module$P$of rank n is isomorphic to a direct sum $R ^ { n - 1 } \oplus I$, where I is a non-zero ideal in$R ,$and$I \cong \Lambda ^ { n } P$is determined up to isomorphism by$P .$

Example 1.2.5. [[For retractive spaces over X, classification up to homotopy equivalence may be more realistic than classification up to topological isomorphism, or homeomorphism.]]

## 1.3 Symmetries

The classification question, as posed above, only asks about the existence of isomorphisms$f \colon X \to Y$between two mathematical objects X and$Y .$. Taken in isolation, this may be the question one is principally interested in, but as we shall see, when trying to relate several such classification questions to one another, it turns out also to be useful to ask about the degree of uniqueness of such isomorphisms. After all, if X is somehow built out of$X _ { 1 }$and$X _ { 2 }$along a common part$X _ { 0 }$, and similarly Y is built out of$Y _ { 1 }$and$Y _ { 2 }$along a common part$Y _ { 0 }$, then we might hope that having an isomorphism$f _ { 1 } \colon X _ { 1 } \to Y _ { 1 }$and an isomorphism$f _ { 2 } \colon X _ { 2 } \to Y _ { 2 }$will sufice to construct an isomorphism$f \colon X \to Y$ that extends$f _ { 1 }$and$f _ { 2 }$. In many cases, however, this will require that both$f _ { 1 }$ and$f _ { 2 }$restrict to isomorphisms from$X _ { 0 }$to$Y _ { 0 }$, along the common parts, and furthermore, that these restrictions agree, i.e., that

$$
f _ {1} | X _ {0} = f _ {2} | X _ {0} \colon X _ {0} \xrightarrow {\cong} Y _ {0}.
$$

This means that we do not just need to know that$X _ { 0 }$and$Y _ { 0 }$are isomorphic, by some unknown isomorphism, but we also need to be able to compare the diferent possible isomorphisms connecting these two objects.

The reader familiar with homological algebra may recognize that this classification of all possible isomorphisms between two objects X and Y is roughly a derived form of the initial problem of classification up to isomorphism.

The classification of isomorphisms can easily be reduced to a classification of self-isomorphisms, or automorphisms, which express the symmetries of a mathematical object. Given two isomorphic objects X and$Y ,$, choose an isomorphism $f \colon X \to Y$. Given any other isomorphism$g \colon X \to Y$between the same two objects, we can form the composite isomorphism$h = f ^ { - 1 } g \colon X \to X$, which is a self-isomorphism of X.

$$
h \bigcap X \xrightarrow [ g ]{f} Y
$$

Conversely, given any self-isomorphism$h \colon X \to X$we can form the composite isomorphism$g = f h \colon X \to Y$between the two given objects. This sets up a oneto-one correspondence between the diferent choices of isomorphisms$g \colon X \to Y$ and the self-isomorphisms$h \colon X \to X$. The correspondence does depend on the initial choice of isomorphism$f ,$but this is of lesser importance.

Hence we are led to ask the secondary classification problem, of understanding the symmetries, or self-isomorphisms$h \colon X \to X$of at least one object in each isomorphism class for the problem at hand. Note that two such symmetries can be composed, hence form a group$\operatorname { A u t } ( X )$, called the automorphism group of X.

Example 1.3.1. The automorphism group of a typical finite set$\mathbf { n } = \{ 1 , 2 , \dots , n \}$ is the group of invertible functions$\sigma \colon \{ 1 , 2 , \ldots , n \} \to \{ 1 , 2 , \ldots , n \}$, i.e., the symmetric group$\Sigma _ { n }$of permutations of n symbols.

Example 1.3.2. The automorphism group of a typical transitive G-set$G / H$ is the group of G-equivariant invertible functions$f \colon G / H \to G / H$. Any such function is determined by its value at the unit coset$e H .$, since$f ( g H ) = f ( g \cdot$ $e H ) = g \cdot f ( e H )$for all$g \in G$. Let us write w${ \cal H } = f ( e { \cal H } )$for this value in$G / H$ In general, not all$w \in G$are realized in this way: since$g H = g h H$for all$h \in H$ we must have$g \cdot w H = f ( g H ) = f ( g h H ) = g h \cdot w H$for all$g \in G , h \in H$, which means that$w ^ { - 1 } h w \in H$for all$h \in H$, i.e., that w is in the normalizer$N _ { G } ( H )$ of H in G. This condition is also suficient, so wH can be freely chosen in the quotient group

$$
W _ {G} (H) = N _ {G} (H) / H,
$$

called the Weyl group of H in G. The automorphism group of the transitive$G \mathrm { - }$ set$G / H$is thus the Weyl group$W _ { G } ( H )$. Note that$N _ { G } ( H ) = G$and$W _ { G } ( H ) =$ $G / H$precisely when H is normal in$G , \mathrm { e . g }$. when G is abelian.

Exercise 1.3.3. Let$\textstyle X = \operatorname { I } \operatorname { I } _ { i = 1 } ^ { n } G / H$be the disjoint union of$n \geq 0$copies of $G / H$. Show that the automorphism group of the G-set X is the semi-direct product

$$
\Sigma_ {n} \ltimes W _ {G} (H) ^ {n},
$$

where$\sigma \in \Sigma _ { n }$acts by permuting the n factors in$W _ { G } ( H ) ^ { n }$. Such a semi-direct product is also called a wreath product, and denoted$\Sigma _ { n } \wr W _ { G } ( H )$

What is the automorphism group of$\begin{array} { r } { X ( \nu ) = \coprod _ { ( H ) } \big [ \big ] ^ { \nu ( H ) } G / H } \end{array}$of the disjoint union, for H ranging over the conjugacy classes of subgroups of G, of$\nu ( H )$copies of$G / H ?$

Example 1.3.4. Consider a finitely generated free R-module$M = R ^ { n }$with n$\geq$ 0. The R-module homomorphisms$f \colon R ^ { n } \to R ^ { n }$can be expressed in coordinates by matrix multiplication by an$n \times n$matrix A with entries in R. For f to be an isomorphism is equivalent to$A$being invertible, so the automorphism group of$R ^ { n }$is the general linear group$G L _ { n } ( R )$of$n \times n$invertible matrices.

[[Describe automorphism group of a finitely generated projective R-module $P ,$given as the image of an idempotent$n \times n$matrix$B ,$as a subgroup of $G L _ { n } ( R ) . ] ]$

## 1.4 Categories

We now turn to the abstract notion of a category, which encodes the key properties of the examples of discrete or additive representations considered above. Our main reference for category theory is Mac Lane [40].

A category$\mathcal { C }$consists of a class$\operatorname { o b j } ( { \mathcal { C } } )$of objects, and for each pair X,$Y$of objects, a set$\mathcal { C } ( X , Y )$of morphisms from$X$to$Y _ { ; }$, usually denoted by arrows $X  Y$. Given three objects X, Y and$Z ,$and morphisms$f \colon X \to Y$and $g \colon Y \to Z$, there is defined a composite morphism$g f \colon X \to Z .$. Furthermore, for each object X there is an identity morphism$i d _ { X } \colon X \to X$These are required to satisfy associative and unital laws.

A morphism$f \colon X \to Y$is called an isomorphism if it admits an inverse $f ^ { - 1 } \colon Y \to X$, such that$f ^ { - 1 } f = i d _ { X }$and$f f ^ { - 1 } = i d _ { Y }$. A category where all morphisms are isomorphisms is called a groupoid.

Example 1.4.1. For each group G there is a category${ \cal G } { - } \mathbf { S e t }$with objects G-sets and morphisms$f \colon X \to Y$the$G \mathrm { . }$-equivariant functions. Here not every morphism is an isomorphism, but there is a smaller category iso$G \mathrm { - } \mathbf { S } \mathbf { e } \mathbf { t } )$with the same objects, and with only the invertible G-equivariant functions. That category is a groupoid.

Example 1.4.2. For each ring R there is a category R−Mod with objects Rmodules and morphisms$f \colon M \to N$the R-linear homomorphisms. Again not every morphism is an isomorphism, but there is a smaller category iso$\scriptstyle \left( R - \mathbf { M o d } \right)$ with the same objects, and with only the invertible R-linear homomorphisms. That category is a groupoid.

Note that the category$\mathcal { C }$contains all the information needed to ask the classification problem for the objects of${ \mathcal { C } } ,$up to the notion of isomorphism implicit in$\mathcal { C } .$. We can introduce an equivalence relation$\cong \mathrm { { \ o ~ o n } }$the objects of $\mathcal { C } _ { : }$, by saying that$X \cong Y$if there exists an isomorphism$f \colon X \to Y$in$\mathcal { C }$ and we can let$\pi _ { 0 } ( \mathcal { C } )$be the collection of equivalence classes for this relation. We often write$[ X ] \in \pi _ { 0 } ( \mathcal { C } )$for the equivalence class of an object X in$\mathcal { C }$ The classification problem is to determine$\pi _ { 0 } ( \mathcal { C } )$in more efectively understood terms.

Furthermore, given any object X in$\mathcal { C }$the set$\mathcal { C } ( X , X )$of morphisms$f \colon X \to$ X is a monoid (= group without inverses) under the given composition. The subset of invertible elements is precisely the subgroup$\operatorname { A u t } ( X )$of automorphisms, or symmetries, of X in$\mathcal { C }$. Hence also the refined classification problem, including not only the existence but also the enumeration of the isomorphisms between two given objects, is encoded in the category.

## 1.5 Classifying spaces

Following an idea of Alexander Grothendieck, it is possible to represent categories by topological spaces in a way that, especially for groupoids, retains all the essential information. These constructions are explained by Graeme Segal in [59].

The idea is to start with a category$\mathcal { C } _ { : }$, and to form a topological space$\lvert \mathcal { C } \rvert$ called the classifying space of$\mathcal { C }$, that amounts to a “picture” of the objects, morphisms and compositions of the category.

To visualize this space, start with drawing one point for each object X of the category. Then, for each morphism$f \colon X \to Y$in the category, draw an edge from the point corresponding to$X$to the point corresponding to$Y .$. If there are several such morphisms, there will be several such edges with the same end-points.

$$
X \xrightarrow {} Y
$$

(We do not actually draw in edges corresponding to the identity morphisms$i d _ { X }$ or more precisely, these edges are collapsed to the point corresponding to X.)

Now, for each pair of composable morphisms$f \colon X \to Y$and$g \colon Y \to Z$ with composite$g f \colon X \to Z ,$, we have already drawn three points, corresponding to$X , Y$and$Z ,$and connected them with three edges, between$X$and$Y , Y$ and Z and X and$Z .$The rule is now to insert a planar triangle, with boundary given by those three edges, for each such pair$( g , f )$

![](images/page_12_image_7.jpg)

(If$f$or$g$is an identity morphism, this triangle is actually collapsed to the edge corresponding to the other morphism.)

So far we have a 2-dimensional picture. Continuing, for each triple of composable morphisms$f \colon X \to Y , g \colon Y \to Z$and$h \colon Z \to W$, we have already drawn in four triangles, corresponding to the pairs$( g , f ) , \ ( h , g ) , \ ( h , g f )$and $( h g , f )$. These meet in the same way as the four faces of a tetrahedron, and the rule is to insert such a solid tetrahedron for each composable triple$( h , g , f )$

![](images/page_12_image_10.jpg)

(Again, if$f , g$or h is an identity morphism, then this solid shape is flattened down to the appropriate triangle.)

To generalize, we think of points, edges, triangles and tetrahedra as the cases $n = 0$though 3 of a family of convex spaces called simplices. The n-dimensional simplex$\Delta ^ { n }$can be taken to be the convex subspace

$$
\Delta^ {n} = \left\{\left(t _ {0}, \dots , t _ {n}\right) \in I ^ {n + 1} \mid \sum_ {i = 0} ^ {n} t _ {i} = 1 \right\}
$$

of the$( n { + } 1 )$-cube that is spanned by the$( n { + } 1 )$vertices$e _ { i } = ( 0 , \ldots , 0 , 1 , 0 , \ldots , 0 )$ for$0 \leq i \leq n$. Topologically,$\Delta ^ { n }$is an n-disc, with boundary$\partial \Delta ^ { n }$homeomorphic to an$( n - 1 )$-sphere.

At the n-th stage of the construction of${ \mathcal { C } } _ { : }$we insert an n-simplex$\Delta ^ { n }$for each n-tuple of composable morphisms$( f _ { n } , \ldots , f _ { 1 } )$in$\mathcal { C }$, along a copy of the boundary$\partial \Delta ^ { n }$of the n-simplex, which was already added at the$( n { - } 1 )$-th stage. If any one of the$f _ { i }$is an identity morphism, the n-simplex only appears in a squashed form, already contained in the previous stage. Taking the increasing union of this sequence of spaces, as$n \to \infty$, we obtain the classifying space$\lvert \mathcal { C } \rvert$

The precise definition goes in two steps: first one forms a simplicial set$N _ { \bullet } \mathcal { C }$ called the nerve of${ \mathcal { C } } _ { : }$, with n-simplices$N _ { n } \mathcal { C }$the set of n-tuples of composable morphisms$( f _ { n } , \ldots , f _ { 1 } )$in$\mathcal { C }$, and appropriate face and degeneracy maps. Then one defines the classifying space$\lvert \mathcal { C } \rvert$to be the topological realization of this simplicial set, given as an identification space

$$
| \mathcal {C} | = \coprod_ {n \geq 0} N _ {n} \mathcal {C} \times \Delta^ {n} / \simeq .
$$

We shall return to these constructions later.

A key point now is that if$\mathcal { C }$is a groupoid, so that all morphisms are isomorphisms, then the classification problem in$\mathcal { C }$becomes a homotopy theoretic question about the classifying space$\lvert \mathcal { C } \rvert$. For the isomorphism classes of objects in$\mathcal { C }$correspond bijectively to the path components of$\lvert \mathcal { C } \rvert$:

$$
\pi_ {0} (\mathcal {C}) \cong \pi_ {0} (| \mathcal {C} |)
$$

and the automorphism group$\operatorname { A u t } ( X ) \ = \ { \mathcal { C } } ( X , X )$of any object X in$\mathcal { C }$is isomorphic to the fundamental group of$\lvert \mathcal { C } \rvert$based at the point corresponding to$X { : }$:

$$
\mathscr {C} (X, X) \cong \pi_ {1} (| \mathscr {C} |, X).
$$

Hence an understanding of the homotopy type of the classifying space$\lvert \mathcal { C } \rvert$is suficient, and in some sense more-or-less equivalent, to an understanding of the refined classification problem in$\mathcal { C }$

To motivate these formulas, note that if X and$Y$are isomorphic in$\mathcal { C } _ { : }$ then the edge corresponding to any chosen isomorphism shows that the points corresponding to$X$and$Y$are in the same path component of$\lvert \mathcal { C } \rvert$. Also, if $f \colon X \to X$is an automorphism of$X$, then the edge corresponding to$f$is in fact a loop based at$X ,$, which determines an element in the fundamental group $\pi _ { 1 } ( | \mathcal { C } | , X )$). Given another automorphism$g \colon X \to X$, the loop corresponding to the composite morphism$g f$is not equal to the loop sum$g * f$of the loops corresponding to$g$and$f ,$but the two loops are homotopic, by a homotopy running over the triangle corresponding to$( g , f )$. Hence the two group structures agree.

![](images/page_13_image_13.jpg)

[[If C is not a groupoid, these formulas fail, but the homotopical data on the right hand side is still of categorical interest.]]

Example 1.5.1. Let iso(Fin) be the groupoid of finite sets and invertible functions. The classifying space | iso(Fin)| has one path component for each non-negative integer, with the n-th component containing the point corresponding to the object$\mathbf { n } = \{ 1 , 2 , \dots , n \}$. Each permutation$\sigma \in \Sigma _ { n }$specifies a loop in$\left| \operatorname { i s o } ( \mathbf { F i n } ) \right|$at n, and the fundamental group of that path component is isomorphic to$\Sigma _ { n }$. It turns out that the universal cover of that path component is contractible, so that the n-th path component is homotopy equivalent to a space called$B \Sigma _ { n } .$, given by the bar construction on the group$\Sigma _ { n }$. Hence there is a homotopy equivalence

$$
| \operatorname{iso} (\mathbf {F i n}) | \simeq \coprod_ {n \geq 0} B \Sigma_ {n}.
$$

[[Forward reference to bar construction BG for groups (or monoids) G.]]

Exercise 1.5.2. Let G be a finite group, and let iso(G−Fin) be the groupoid of finite G-sets and G-equivariant bijections. Convince yourself that there is a homotopy equivalence

$$
| \operatorname{iso} (G - \mathbf {F i n}) | \simeq \coprod_ {\nu} B \operatorname{Aut} (X (\nu)),
$$

where ν ranges over the functions$\mathrm { C o n j S u b } ( G ) \to \mathbb { N } _ { 0 }$. Using Exercise 1.3.3, can you see that there is a homotopy equivalence

$$
| \operatorname{iso} (G - \mathbf {F i n}) | \simeq \prod_ {(H)} \coprod_ {n \geq 0} B (\Sigma_ {n} \wr W _ {G} (H))
$$

where$( H )$in the product runs through ConjSub(G)? [[Forward reference to Segal–tom Dieck splitting.]]

[[Classifying space of real or complex vector spaces given in terms of Grassmannians. More elaborate spaces for k-linear G-representations.]]

Example 1.5.3. Let iso$\textstyle ( { \mathcal { F } } ( R ) )$be the groupoid of finitely generated free Rmodules and R-linear isomorphisms. Under a mild assumption on$R ,$satisfied e.g. if R is commutative or if$R = \mathbb { Z } [ \pi ]$is an integral group ring, the classifying space$| \operatorname { i s o } ( \mathcal { F } ( R ) ) |$has one path component for each non-negative integer, with the n-th component containing the point corresponding to the object$R ^ { n }$. Each invertible matrix$A \in G L _ { n } ( R )$specifies a loop in | iso($\mathcal { F } ( R ) ) |$at$R ^ { n }$, and the fundamental group of that path component is isomorphic to$G L _ { n } ( R )$. It again turns out that the universal cover of that path component is contractible, so that the n-th path component is homotopy equivalent to$B G L _ { n } ( R )$. Hence there is a homotopy equivalence

$$
| \operatorname{iso} (\mathscr {F} (R)) | \simeq \coprod_ {n \geq 0} B G L _ {n} (R).
$$

In general, for a discrete group G the bar construction BG is a space such that its (singular) homology equals the group homology of G, which again can be expressed as the Tor-groups of the group ring$\mathbb { Z } [ G ]$

$$
H _ {*} (B G) \cong H _ {*} ^ {g p} (G) = \mathrm{Tor} _ {*} ^ {\mathbb {Z} [ G ]} (\mathbb {Z}, \mathbb {Z}).
$$

To see this, arrange that BG is a CW-complex, and note that its universal cover $E G = { \widetilde { B G } }$is then a contractible CW-complex with a free, cellular G-action. The gcellular complex for BG can then be computed from that of EG, by

$$
C _ {*} (B G) \cong C _ {*} (E G) \otimes_ {\mathbb {Z} [ G ]} \mathbb {Z},
$$

and since$C _ { * } ( E G )$is a free$\mathbb { Z } [ G ]$-module resolution of$\mathbb { Z } ,$, the claim follows by passing to homology.

Hence, in the examples above, we have isomorphisms

$$
H _ {*} (| \operatorname{iso} (\mathbf {F i n}) |) \cong \bigoplus_ {n \geq 0} H _ {*} (B \Sigma_ {n})
$$

and

$$
H _ {*} (| \operatorname{iso} (\mathcal {F} (R)) |) \cong \bigoplus_ {n \geq 0} H _ {*} (B G L _ {n} (R)).
$$

Remark 1.5.4. As proposed by Jacques Tits in 1956, the symmetric group$\Sigma _ { n }$ might be interpreted as the general linear group$G L _ { n } ( \mathbb { F } _ { 1 } )$over the “field with one element”. From this perspective, Fin is a special case of${ \mathcal { F } } ( R )$. The idea has been carried further by Christophe Soul´e, Alain Connes and others, to define varieties, zeta-functions, etc. over this hypothetical field. This is apparently part of a take on the Riemann hypothesis.

## 1.6 Monoid structures

So far, the introduction of categorical language and the formation of the classifying space has only amounted to a process of rewriting. The original classification problem in a groupoid$\mathcal { C }$is basically equivalent to the problem of determining the homotopy type of |C|.

The basic idea of algebraic K-theory is to consider a modification of the classifying space$\lvert \mathcal { C } \rvert$to form a new space$K ( \mathcal { C } )$. On one hand the resulting space$K ( \mathcal { C } )$should be better-behaved, more strongly structured and possibly more easily analyzed than$\lvert \mathcal { C } \rvert$. On the other hand, the diference between the spaces |C | and$K ( \mathcal { C } )$should not be too great, so that any information we obtain about$K ( \mathcal { C } )$will also tell us something about |C | and the classification problem in$\mathcal { C }$

The kind of structure that we have in mind here, which is to be strengthened in$K ( \mathcal { C } )$as compared to$\lvert \mathcal { C } \rvert$, is usually some form of sum operation on the objects of$\mathcal { C }$. At the level of isomorphism classes, the strengthening consists of extending the resulting commutative monoid structure to an abelian group structure.

Example 1.6.1. In the groupoid iso(Fin) of finite sets and bijections, we can take two finite$X$and$Y$and form their disjoint union, to obtain a new finite set$X \sqcup Y$. This defines a pairing of categories

$$
\sqcup : \operatorname{iso} (\mathbf {F i n}) \times \operatorname{iso} (\mathbf {F i n}) \longrightarrow \operatorname{iso} (\mathbf {F i n}),
$$

or more precisely, a bifunctor, giving iso(Fin) a (symmetric) monoidal structure. In the larger category Fin of finite sets and arbitrary functions, the disjoint union$X \sqcup Y$, equipped with the two inclusions$X \to X \sqcup Y$and$Y  X \sqcup$ $Y$expresses$X \sqcup Y$as the categorical sum or coproduct of$X$and$Y .$The isomorphism class of$X \sqcup Y$only depends on the isomorphism classes of X and $Y ,$, so we get an induced pairing$+ \colon  { \mathbb { N } } _ { 0 } \times  { \mathbb { N } } _ { 0 } \to  { \mathbb { N } } _ { 0 }$on the set

$$
\pi_ {0} (\mathrm{iso} (\mathbf {F i n})) \cong \mathbb {N} _ {0}
$$

of isomorphism classes of finite sets. This is simply the usual addition of non-negative integers, since$\# ( X \sqcup Y ) = \# X + \# Y$. Hence the disjoint union pairing lifts the sum operation on${ \mathbb { N } } _ { 0 }$to a refined sum operation on$\operatorname { i s o } ( \mathbf { F i n } )$. Note that this structure makes both sides of the displayed equation into commutative monoids, and the isomorphism is now not just a one-to-one correspondence of sets, but an isomorphism of commutative monoids.

Passing to classifying spaces, there is also an induced pairing

$$
| \sqcup |: | \operatorname{iso} (\mathbf {F i n}) | \times | \operatorname{iso} (\mathbf {F i n}) | \longrightarrow | \operatorname{iso} (\mathbf {F i n}) |
$$

that makes$\left| \operatorname { i s o } ( \mathbf { F i n } ) \right|$into a topological monoid. It is not strictly commutative, since$X \sqcup Y$is isomorphic, but not identical, to$Y \sqcup X$. Still, it is homotopy commutative in a sense that we shall return to.

Under the homotopy equivalence$| \mathrm { i s o } ( \mathbf { F } \mathbf { i n } ) | \simeq \prod _ { n \geq 0 } B \Sigma _ { n }$, the above pairing can be identified as the map

$$
\left(\coprod_ {k \geq 0} B \Sigma_ {k}\right) \times \left(\coprod_ {l \geq 0} B \Sigma_ {l}\right) \longrightarrow \coprod_ {n \geq 0} B \Sigma_ {n}
$$

taking the$( k , l ) \ – \mathrm { t h }$component to the$( k + l ) \AA \cdot \mathrm { t h }$component, by the map

$$
B \Sigma_ {k} \times B \Sigma_ {l} \rightarrow B \Sigma_ {k + l}
$$

induced by the group homomorphism$\Sigma _ { k } \times \Sigma _ { l } \to \Sigma _ { k + l }$given by block sum of permutation matrices$( \sigma , \tau ) \mapsto [ _ { 0 } ^ { \sigma ~ 0 } \tau ]$. Associativity for the block sum pairing shows that this makes$\textstyle \prod _ { n \geq 0 } B \Sigma _ { n }$a topological monoid.

Remark 1.6.2. This process of lifting a structure from the set$\pi _ { 0 } ( \mathcal { C } )$to a the category$\mathcal { C }$is known as categorification, while the process of lowering a structure on$\mathcal { C }$to the set of isomorphism classes$\pi _ { 0 } ( \mathcal { C } )$is known as decategorification. It is the former process that requires creative thought.

Example 1.6.3. In the groupoid iso$\textstyle ( { \mathcal { F } } ( R ) )$of finitely generated free R-modules and R-linear isomorphisms, we can take two R-modules M and$N$and form their direct sum, to obtain a new R-module$M \oplus N$. This defines a pairing of categories

$$
\oplus \colon \operatorname{iso} (\mathscr {F} (R)) \times \operatorname{iso} (\mathscr {F} (R)) \longrightarrow \operatorname{iso} (\mathscr {F} (R)).
$$

In the larger category${ \mathcal { F } } ( R )$of finitely generated free R-modules and arbitrary R-linear homomorphisms, the direct sum$M \oplus N$, equipped with the two inclusions$M \to M \oplus N$and$N \to M \oplus N$expresses$M \oplus N$as the coproduct of $M$and N. The isomorphism class of$M \oplus N$only depends on the isomorphism classes of M and N, so under the same mild hypothesis on$R$as above, we get an induced pairing$+ \colon  { \mathbb { N } } _ { 0 } \times  { \mathbb { N } } _ { 0 } \to  { \mathbb { N } } _ { 0 }$on the set

$$
\pi_ {0} (\mathrm{iso} (\mathcal {F} (R))) \cong \mathbb {N} _ {0}
$$

of isomorphism classes of finitely generated free R-modules. Again, this is usual addition of non-negative integers, since rank$( M \oplus N ) = \operatorname { r a n k } ( M ) + \operatorname { r a n k } ( N )$ Hence the direct sum pairing lifts the sum operation on$\mathbb { N } _ { 0 } { \mathrm { ~ t o ~ i s o } } ( { \mathcal { F } } ( R ) )$.

Passing to classifying spaces, there is also an induced pairing

$$
| \oplus |: | \operatorname{iso} (\mathscr {F} (R)) | \times | \operatorname{iso} (\mathscr {F} (R)) | \longrightarrow | \operatorname{iso} (\mathscr {F} (R)) |
$$

that makes$| \operatorname { i s o } ( \mathcal { F } ( R ) )$| into a topological monoid. It is homotopy commutative, but not strictly commutative, since$M \oplus N$is isomorphic, but not identical, to $N \oplus M$

Under the homotopy equivalence$\begin{array} { r } { | \mathrm { i s o } ( \mathcal { F } ( R ) ) | \simeq \prod _ { n > 0 } B G L _ { n } ( R ) } \end{array}$, the above pairing can be identified as the map

$$
\left(\coprod_ {k \geq 0} B G L _ {k} (R)\right) \times \left(\coprod_ {l \geq 0} B G L _ {l} (R)\right) \longrightarrow \coprod_ {n \geq 0} B G L _ {n} (R)
$$

taking the (k, l)-th component to the$( k + l ) \AA \cdot \mathrm { t h }$component, by the map

$$
B G L _ {k} (R) \times B G L _ {l} (R) \rightarrow B G L _ {k + l} (R)
$$

induced by the group homomorphism$G L _ { k } ( R ) \times G L _ { l } ( R ) \to G L _ { k + l } ( R )$given by block sum of invertible matrices$( A , B ) \longmapsto [ { A \atop 0 } { \begin{array} { l } { 0 } \\ { B } \end{array} } ]$This makes$\begin{array} { r } { \prod _ { n \geq 0 } B G L _ { n } ( R ) } \end{array}$a topological monoid.

Example 1.6.4. Let${ \mathcal { P } } ( R )$be the category of finitely generated projective R-modules and R-linear homomorphisms, and let iso$\textstyle \cdot ( { \mathcal { P } } ( R ) )$be the groupoid where the morphisms are R-linear isomorphisms. Again the direct sum of$R -$ modules defines a pairing

$$
\oplus \colon \operatorname{iso} (\mathscr {P} (R)) \times \operatorname{iso} (\mathscr {P} (R)) \longrightarrow \operatorname{iso} (\mathscr {P} (R)),
$$

which induces a sum operation on the set

$$
\pi_ {0} (\mathrm{iso} (\mathcal {P} (R)))
$$

of isomorphism classes of finitely generated projective R-modules. This pairing makes$\pi _ { 0 } ( \operatorname { i s o } ( { \mathcal { P } } ( R ) ) )$a commutative monoid.

Passing to classifying spaces, there is also an induced pairing

$$
| \oplus |: | \operatorname{iso} (\mathscr {P} (R)) | \times | \operatorname{iso} (\mathscr {P} (R)) | \longrightarrow | \operatorname{iso} (\mathscr {P} (R)) |
$$

that makes$| \operatorname { i s o } ( \mathcal { P } ( R ) ) |$into a homotopy commutative topological monoid.

Example 1.6.5. When$R = C ( X )$is the ring of continuous complex functions on a (compact Hausdorf) topological space$X ,$there is a correspondence between the finite-dimensional complex vector bundles$E  X$and the finitely generated projective R-modules$P ,$taking$E$to the module of continuous sections$P = \Gamma ( E \downarrow X )$In this case the classification of isomorphism classes of finitely generated projective R-modules is the same as the classification of finite-dimensional complex vector bundles over$X$, so that

$$
\pi_ {0} (\mathrm{iso} (\mathcal {P} (R))) \cong \mathrm{Vect} (X),
$$

where Vect(X) denotes the set of isomorphism classes of such vector bundles. This is an isomorphism of commutative monoids, where the direct sum of$R -$ modules on the left corresponds to the Whitney sum of vector bundles on the right. For example, when$\dot { X } = S ^ { k + 1 }$，$\mathrm { V e c t } ( S ^ { k + 1 } )$is the disjoint union over$n \geq 0$ of the homotopy groups$\pi _ { k } ( U ( n ) )$, which are not all known. This shows that the structure of$\pi _ { 0 } ( \operatorname { i s o } ( { \mathcal { P } } ( R ) ) )$can in general be rather complicated. [[Reference to Serre and Swan?]]

## 1.7 Group completion

Note that the monoids${ \mathbb { N } } _ { 0 }$and$\pi _ { 0 } ( \operatorname { i s o } ( { \mathcal { P } } ( R ) ) )$are not groups, since most elements lack additive inverses, or negatives. After all, there are no sets with a negative number of elements, and no R-modules of negative rank.

A fundamental idea of Grothendieck was to strengthen the algebraic structure on commutative monoids, like$\pi _ { 0 } ( \mathcal { C } )$, by adjoining additive inverses to all its elements, so as to obtain an actual abelian group.

Algebraically, this is an easy construction. Given a commutative monoid $M ,$written additively with neutral element$0 ,$view elements$( a , b )$of$M \times M$as formal diferences$a - b .$, by introducing the equivalence relation$( a , b ) \sim ( c , d )$if there exists an$f \in M$such that$a + d + f = b + c + f .$. (If the cancellation law $x + f = y + f \implies x = y$holds in$M .$, one may omit all mention of$f . )$Then the set of equivalence classes

$$
K (M) = (M \times M) / \sim
$$

becomes an abelian group, with componentwise sum. The negative of the equivalence class [a, b] of$( a , b )$is$[ b , a ]$, and there is a monoid homomorphism

$$
\iota \colon M \to K (M)
$$

that takes a to$[ a , 0 ]$. In a precise sense this is the initial monoid homomorphism from M to any abelian group, so$K ( M )$is the group completion of M. For example,$K ( \mathbb { N } _ { 0 } ) \cong \mathbb { Z }$. We also call$K ( M )$the Grothendieck group of M.

Example 1.7.1. Let G be a finite group, and let$M ( G ) = \pi _ { 0 } ( \mathrm { i s o } ( \mathrm { G - F i n } ) )$ be the commutative monoid of isomorphism classes of finite G-sets, with sum operation$[ X ] + [ Y ] = [ X \sqcup Y ]$induced by disjoint union. Let$A ( G ) = K ( M ( G ) )$ be the associated Grothendieck group. The identification of$M ( G )$with the set of functions ν :$\mathrm { C o n j S u b } ( G ) \to \mathbb { N } _ { 0 }$is compatible with the sum operation (defined pointwise by$( \nu + \mu ) ( H ) = \nu ( H ) + \mu ( H ) )$, since$X ( \nu )$⊔$X ( \mu ) \ \cong$ $X ( \nu + \mu )$. Hence$A ( G ) = K ( M ( G ) )$is isomorphic to the abelian group of functions ν :$\operatorname { C o n j S u b } ( G ) \to \mathbb { Z } .$. From another point of view,$M ( G )$is the free commutative monoid generated by the isomorphism classes of transitive G-sets $G / H$, and$A ( G )$is the free abelian group generated by the same isomorphism classes.

The abelian group$A ( G )$has a natural commutative ring structure, and is therefore known as the Burnside ring. (Another common notation is$\Omega ( G ) . )$ The cartesian product$X \times Y$of two finite G-sets X and$Y$is again a finite G-set, with the diagonal G-action$g \cdot ( x , y ) = ( g \cdot x , g \cdot y )$, and this pairing $M ( G ) \times M ( G ) \to M ( G )$extends to the ring product$A ( G ) \times A ( G ) \to A ( G )$. By linearity, the ring product on$A ( G )$is determined by the product$[ G / H ] \cdot [ G / K ]$ of two transitive G-sets. Here

$$
G / H \times G / K \cong \coprod_ {x} G / (H \cap x K x ^ {- 1})
$$

as$G \mathrm { - s e t s }$, where x ranges over a set of representatives for the double coset decomposition$\textstyle G = \bigcup _ { x } H x K$, so

$$
[ G / H ] \cdot [ G / K ] = \sum_ {x} [ G / (H \cap x K x ^ {- 1}) ]
$$

in the Burnside ring.

For example, if$G = C _ { p }$is cyclic of order$p ,$the 1-element set$G / G = *$acts as the ring unit in$A ( C _ { p } )$, while the free G-set$G / \{ e \} = G$satisfies$G \times G \cong \coprod ^ { p } G$ hence

$$
A (C _ {p}) \cong \mathbb {Z} [ T ] / (T ^ {2} = p T)
$$

as a commutative ring. Here T denotes the class of$G .$

[[Reference to Segal’s Burnside ring conjecture on$\pi _ { S } ^ { 0 } ( B G _ { + } ) . ] ]$

[[Consider representation ring$R _ { k } ( G )$, the Grothendieck group of k-linear G-representations.]]

[[Reference to the Atiyah–Segal theorem on$K ^ { 0 } ( B G ) . ] ]$

Definition 1.7.2. Let R be any ring. The zero-th algebraic$K  \it - g r o u p$of$R$is defined to be the group completion

$$
K _ {0} (R) = K (\pi_ {0} (\mathrm{iso} (\mathcal {P} (R))))
$$

of the abelian monoid of isomorphism classes of finitely generated projective R-modules, under direct sum.

Remark 1.7.3. The use of the letter$\mathrm { \Phi ^ { \circ } K } '$here, and hence the name K-theory, appears to stem from the construction of the group completion in terms of equivalence classes of pairs, viewed as formal diferences. To refer to these classes Grothendieck might have used the letter$\mathbf { \nabla } ^ { \left. \mathbf { { C } } \right. }$, but since notations like$C ( X )$were already in use, he chose$\mathrm { \Phi ^ { \circ } K } '$for the German word ‘Klassen’. [[Reference?]]

Example 1.7.4. Consider a finite CW complex X, with cellular complex$C _ { * } ( X )$ and cellular (= singular) homology$H _ { * } ( X )$. In each degree n the n-th homology group$H _ { n } ( X )$is a finitely generated abelian group, or Z-module, whose rank $b _ { n } ( X )$is known as the n-th Betti number of X. This is obviously a non-negative integer. Knowledge of the number of n-cells in X for each n determines the rank of the cellular complex$C _ { * } ( X )$in each degree, but in order to determine the Betti numbers, knowledge of the ranks of the boundary maps$d _ { n } \colon C _ { n } ( X ) \to C _ { n - 1 } ( X )$ in the cellular complex is also needed. However, there is one relation between these numbers that does not depend upon the boundary maps. Namely, the Euler characteristic$\begin{array} { r } { \chi ( X ) = \sum _ { n > 0 } ( - 1 ) ^ { n } b _ { n } ( X ) } \end{array}$of X is given by both sides of the equation

$$
\sum_ {n \geq 0} (- 1) ^ {n} \operatorname{rank} H _ {n} (X) = \sum_ {n \geq 0} (- 1) ^ {n} \operatorname{rank} C _ {n} (X).
$$

Of course, this is now an equation that takes place in$\mathbb { Z } ,$not in$\mathbb { N } _ { 0 } .$, even if each individual rank is non-negative.

As a consequence, the Euler characteristic satisfies some useful relations in a number of cases. For example, if$Y \  X$is a k-fold covering space, then $\chi ( Y ) = k \cdot \chi ( X )$, since there are k n-cells in$Y$covering each n-cell in$X$, so rank$C _ { n } ( Y ) = k$· rank$C _ { n } ( X )$. More generally, if$F  E  B$is a fiber bundle (or fibration) with$F , E$and B finite CW complexes then$\chi ( E ) = \chi ( B ) \cdot \chi ( F )$ In general there is no equally simple relation between the Betti numbers, since there may be many diferentials in the Serre spectral sequence

$$
E _ {*, *} ^ {2} = H _ {*} (B; H _ {*} (F)) \Longrightarrow H _ {*} (E).
$$

The point to note is that in order to make use of the Euler characteristic, in place of Betti numbers, we have to work with integers instead of non-negative integers.

## 1.8 Loop space completion

The fundamental idea of higher algebraic K-theory, as created by Quillen, is to strengthen the algebraic structure on topological monoids, like$\lvert \mathcal { C } \rvert$, by topologically adjoining homotopy inverses in a systematic manner, along a map

$$
\iota \colon | \mathcal {C} | \to K (\mathcal {C}).
$$

The well-behaved way of specifying this is a topological process of loop space completion, since loop spaces have homotopy inverses realized by reversing the direction of travel around a loop. In this case the details of the definition require more topological sophistication than in the algebraic definition of$K _ { 0 }$ The algebraic construction and the higher, topological one, will be compatible after decategorification, in the sense that

$$
K (\pi_ {0} (\mathcal {C})) \cong \pi_ {0} (K (\mathcal {C})).
$$

[[Sometimes we give a sum structure on$\pi _ { 0 } ( \mathcal { C } )$by setting$[ X ] + [ Y ] = [ Z ]$ whenever there is a suitable extension$0  X  Z  Y  0$, not just when $Z = X \oplus Y$. Then the starting data on$\lvert \mathcal { C } \rvert$is more than just the monoid structure induced by | ⊕ |, and$K ( \mathcal { C } )$is not just the group completion of that monoid structure.]]

[[In the case of Waldhausen’s$S _ { \bullet }$construction, the starting data is given by a category with cofibrations and weak equivalences. In the case of Quillen’s Q-construction, this is specialized to an exact category.]]

In the examples discussed in Section 1.6, where a pairing$\oplus \colon { \mathcal { C } } \times { \mathcal { C } } \to { \mathcal { C } }$ makes$M = | \mathcal { C } |$a topological monoid, and we seek to group complete$\pi _ { 0 } ( \mathcal { C } )$ with respect to the induced sum operation, the algebraic K-theory space$K ( \mathcal { C } )$ can be constructed as a loop space using the bar construction BM for monoids:

$$
K (\mathcal {C}) = \Omega B | \mathcal {C} |.
$$

For any based space$X , \Omega X = \mathrm { M a p } _ { * } ( S ^ { 1 } , X )$denotes the loop space of$X$, defined as the space of based maps from$S ^ { 1 }$to X. There is an inclusion$\Sigma | \mathcal { C } |  B | \mathcal { C } |$ where$\Sigma X = X \wedge S ^ { 1 }$denotes the suspension of X. There is a natural map $X \to \Omega \Sigma X$that maps x to the loop$s \mapsto x \wedge s .$, and the group completion map $\iota \colon | \mathcal { C } |  K ( \mathcal { C } )$factors as$| \mathcal { C } | \to \Omega \Sigma | \mathcal { C } | \to \Omega B | \mathcal { C } |$

Definition 1.8.1. The higher algebraic K-groups of$\mathcal { C }$are in this case defined as the homotopy groups

$$
K _ {i} (\mathcal {C}) = \pi_ {i} (K (\mathcal {C}))
$$

of the loop space$K ( \mathcal { C } )$, for$i \geq 0$. In particular, for each ring$R$we let$K ( R ) =$ $K ( \operatorname { i s o } ( \mathcal { P } ( R ) ) )$and$K _ { i } ( R ) = \pi _ { i } ( K ( R ) )$.

Under similar hypotheses [[forward reference]], the amazing thing happens that$K ( \mathcal { C } )$is not just a loop space, i.e., a space of the form$\Omega X _ { 1 } .$but it is an infinite loop space, i.e., there is a sequence of spaces$X _ { n }$such that$X _ { n } \simeq \Omega X _ { n + 1 }$ for all$n \geq 0$, and$K ( \mathcal { C } ) = X _ { 0 }$. In particular,$K ( \mathcal { C } ) \simeq \Omega ^ { n } X _ { n } = \mathrm { M a p } _ { * } ( S ^ { n } , X _ { n } )$ is an n-fold loop space, for each$n \geq 0$. The sequence of spaces${ \bf K } ( \mathcal { C } ) = { \bf \Phi }$ $\{ X _ { n } \} _ { n \geq 0 }$form a spectrum in the sense of algebraic topology, or equivalently, an S-module, where S is the sphere spectrum. In this sense,$K ( \mathcal { C } )$is a much more strongly structured object than the classifying space$\lvert \mathcal { C } \rvert$, and this additional structure can often be brought to bear on the identification and the analysis of its homotopy type.

For this to be useful for the original classification question in${ \mathcal { C } } _ { : }$, we must of course know something about the group completion map ι. Here there is no general theorem, but in many special cases there are particular results about how close$\lvert \mathcal { C } \rvert$and$K ( \mathcal { C } )$are. We shall review some of these results in the rest of this chapter.

## 1.9 Grothendieck–Riemann–Roch

The zero-th K-groups were introduced by Grothendieck around 1956 in the context of sheaves over algebraic varieties, see [6] for the published exposition by Borel and Serre. In general there are two$K \cdot$-groups associated to a variety $X$, here denoted$K _ { 0 } ( X )$and$K _ { 0 } ^ { \prime } ( X )$, but they are isomorphic for X smooth and quasi-projective.

The abelian group$K _ { 0 } ^ { \prime } ( X )$is defined to be generated by the set$\pi _ { 0 } ( \mathbf { C o h } ( X ) )$ of isomorphism classes$[ \mathcal { F } ]$of coherent sheaves over$X$, subject to the relation

$$
[ \mathcal {F} ] = [ \mathcal {F} ^ {\prime} ] + [ \mathcal {F} ^ {\prime \prime} ]
$$

whenever

$$
0 \to \mathcal {F} ^ {\prime} \to \mathcal {F} \to \mathcal {F} ^ {\prime \prime} \to 0
$$

is a short exact sequence of coherent sheaves. Note that in this case, we may or may not have that$\mathcal { F }$is isomorphic to the direct sum$\mathcal { F } ^ { \prime } \oplus \mathcal { F } ^ { \prime \prime }$. Some authors write$G _ { 0 } ( X )$for the Grothendieck group$K _ { 0 } ^ { \prime } ( X )$

The abelian group$K _ { 0 } ( X )$is defined to be generated by the set of isomorphism classes$[ \mathcal { F } ]$of algebraic vector bundles over$X$, subject to the same relation as above. However, in this case each short exact sequence of vector bundles admits a splitting, so the relation may also be expressed as saying that $\left[ { \mathcal { F } } \right] = \left[ { \mathcal { F } } ^ { \prime } \right] + \left[ { \mathcal { F } } ^ { \prime \prime } \right]$whenever$\mathcal { F } \cong \mathcal { F } ^ { \prime } \oplus \mathcal { F } ^ { \prime \prime }$

Each vector bundle is a coherent sheaf, so there is a natural homomorphism$K _ { 0 } ( X )  K _ { 0 } ^ { \prime } ( X )$, and this is an isomorphism when$X$is smooth and quasi-projective, essentially because each coherent sheaf admits a finite length resolution by vector bundles. We shall generalize this in the resolution theorem [[forward reference]].

In the afine case, when$X = \operatorname { S p e c } ( R )$, the category$\mathbf { C o h } ( X )$of coherent sheaves over X is equivalent to the category$\mathcal { M } ( R )$of finitely generated$R -$ modules, and the category of vector bundles over X is equivalent to the category${ \mathcal { P } } ( R )$of finitely generated projective R-modules. In particular,$K _ { 0 } ( X ) =$ $K _ { 0 } ( R )$

Grothendieck proves the Riemann–Roch theorem in a relative form, starting with a proper morphism$f \colon X \to Y$of smooth and quasi-projective varieties. The direct image functor$f _ { * }$has right derived functors$R ^ { q } f _ { * }$for all$q \geq 0$, and Grothendieck shows that for each coherent sheaf$\mathcal { F }$over$X$, each derived direct image$( R ^ { q } f _ { * } ) ( \mathcal { F } )$is a coherent sheaf over$Y .$. The correct statement of the Riemann–Roch theorem is not just about the direct image homomorphism (of commutative monoids)

$$
f _ {*} \colon \pi_ {0} (\mathbf {C o h} (X)) \to \pi_ {0} (\mathbf {C o h} (Y))
$$

taking$[ \mathcal F ]$to$[ f _ { * } ( \mathcal { F } ) ]$], but about the total derived direct image homomorphism

$$
f _ {!} = \sum_ {q \geq 0} (- 1) ^ {q} (R ^ {q} f _ {*}).
$$

As in the case of Euler characteristics, the alternating sum$f _ { ! } ( \mathcal { F } )$cannot be assumed to take values in$\pi _ { 0 } ( { \bf C o h } ( Y ) )$, but it does make sense in the Grothendieck group$K _ { 0 } ^ { \prime } ( Y )$. Having done this, it is easy to see that$f _ { ! }$is additive on extensions of coherent sheaves, so that it defines a homomorphism (of abelian groups)

$$
f _ {!} \colon K _ {0} ^ {\prime} (X) \to K _ {0} ^ {\prime} (Y).
$$

This maneuver is therefore needed to even state the Grothendieck–Riemann– Roch theorem, which compares the total derived direct image$f _ { ! }$with the corresponding direct image$f _ { * } \colon A ( X ) \to A ( Y )$of Chow groups, via the Chern character ch:$K _ { 0 } ( X ) \to A ( X ) \otimes \mathbb { Q } .$. The direct images do not directly agree, but they do when multiplied by the so-called Todd class$t d ( X ) \in A ( X ) \otimes \mathbb { Q }$. The general formula reads:

$$
c h (f _ {!} (\mathcal {F})) \cdot t d (Y) = f _ {*} (c h (\mathcal {F}) \cdot t d (X))
$$

When X is smooth and projective of dimension n, the unique map$f \colon X \to Y =$ $\operatorname { S p e c } ( k )$is proper, and the formula specializes to

$$
\chi (X, \mathcal {F}) = (c h (\mathcal {F}) \cdot t d (X)) _ {n},
$$

where the subscript n refers to the degree n part. [[Explain, or use Kronecker pairing with fundamental class$\left[ X \right] ? ] ]$In the case$k = \mathbb { C }$of complex varieties, this is the Hirzebruch–Riemann–Roch theorem, and when$n = 1$, one recovers the classical Riemann–Roch theorem for complex algebraic curves.

## 1.10 Vector fields on spheres

For each$n \geq 1$, the following statements are equivalent:

(a) There is a division algebra over$\mathbb { R }$of dimension n;

(b) The sphere$S ^ { n - 1 }$admits$( n - 1 )$tangent vector fields that are everywhere linearly independent;

(c) There is a two-cell complex$X = S ^ { n } \cup _ { f } D ^ { 2 n }$in which the cup product square of a generator of$H ^ { n } ( X ; \mathbb { Z } / 2 )$is a generator of$H ^ { 2 n } ( X ; \mathbb { Z } / 2 )$

The division algebras R, C, H (the quaternions) and$\mathbb { O }$(the octonions) show that these statements are true for$n = 1 , 2 .$, 4 and 8.

It is a theorem of Frank Adams [1] from 1960 that the third statement is false for all other values of$n .$In particular, there are no higher-dimensional division algebras then the ones given. Adams’ original proof used a factorization of the Steenrod operations$S q ^ { n }$in singular cohomology (for n a power of two) using secondary cohomology operations, and is rather delicate.

Following Grothendieck’s ideas from algebraic geometry, Michael Atiyah and Friedrich Hirzebruch [4] introduced topological K-theory in 1959. For a finite CW complex X, the group

$$
K ^ {0} (X) = K (\operatorname{Vect} (X))
$$

is defined to be the Grothendieck group of the commutative monoid of isomorphism classes of finite-dimensional complex vector bundles over X. A few years later, Adams and Atiyah [2] found a quick and short, so-called “postcard proof”, of Adams’ theorem, replacing the use of singular cohomology, Steenrod operations and secondary cohomology operations by the use of topological K-theory and the much simpler Adams operations$\psi ^ { k } \colon K ^ { 0 } ( X ) \to K ^ { 0 } ( X )$

For expositions of the K-theory proof, see Husemoller [28, Ch. 14] or Section 2.3 of Allen Hatcher’s book project

http://www.math.cornell.edu/∼hatcher/VBKT/VBpage.html .

## 1.11 Wall’s finiteness obstruction

Here is a more elaborate version of Example 1.7.4. Suppose for simplicity that $X$is a path-connected CW complex, with universal covering space$p \colon \tilde { X } \to X$ Fix a base point in$X ,$and let$\pi = \pi _ { 1 } ( X )$ebe the fundamental group. Then π acts freely by deck transformations on$\widetilde { X }$. The CW structure on X lifts to a CW structure on$\widetilde { X }$e, and π permutes the cells of X freely. Hence the cellular complex $C _ { * } ( \widetilde { X } )$of$\widetilde { X }$eis a complex of free$\mathbb { Z } [ \pi ]$e-modules. Since X is the orbit space for the e efree π-action on$\widetilde { X }$, we have the isomorphism$C _ { * } ( X ) \cong \mathbb { Z } \otimes _ { \mathbb { Z } [ \pi ] } C _ { * } ( \widetilde X )$previously mentioned.

If X is a finite CW complex, then there are finitely many free π-orbits of cells in$\widetilde { X }$, and$C _ { * } ( \widetilde { X } )$is a bounded complex of finitely generated free$\mathbb { Z } [ \pi ]$]-modules. e eIn other words, each$C _ { n } ( { \widetilde { X } } )$is a finitely generated free$\mathbb { Z } [ \pi ]$-module, which is enonzero only for finitely many n. For each n the isomorphism class of$C _ { n } ( { \tilde { X } } )$ therefore defines an element in the commutative monoid

$$
\pi_ {0} (\mathrm{iso} (\mathcal {F} (\mathbb {Z} [ \pi ])))
$$

which we may map, by viewing free modules as projective, to the commutative monoid

$$
\pi_ {0} (\mathrm{iso} (\mathcal {P} (\mathbb {Z} [ \pi ]))).
$$

Now, the precise cellular modules$C _ { * } ( \widetilde { X } )$depend on the particular choice of CW estructure on X. However, as for the Euler characteristic above, the alternating sum

$$
[ X ] = \sum_ {n \geq 0} (- 1) ^ {n} [ C _ {n} (\widetilde {X}) ] \in K _ {0} (\mathbb {Z} [ \pi ])
$$

is in fact independent of the CW structure. Of course, in order to form this alternating sum [X], we had to go from the commutative monoid$\pi _ { 0 } ( \operatorname { i s o } ( { \mathcal { P } } ( \mathbb { Z } [ \pi ] ) ) )$1 to its group completion$K _ { 0 } ( \mathbb { Z } [ \pi ] )$.

In this case the added complexity does not tell us something new. After all, if X has$c _ { n }$n-cells, then$C _ { n } ( X )$is the free Z-module on$c _ { n }$generators and$C _ { n } ( { \widetilde { X } } )$is the free$\mathbb { Z } [ \pi ]$-module on equally many generators. Hence we can obtain$C _ { n } ( { \widetilde { X } } )$from$C _ { n } ( X )$by base change along the unique ring homomorphism $\mathbb { Z } \to \mathbb { Z } [ \pi ]$e. (This only works one degree at a time. The boundary maps in$C _ { * } ( \widetilde { X } )$ are usually not induced up from those in$C _ { * } ( X ) . \rfloor$e) It follows that the alternating sum$[ X ] \in K _ { 0 } ( \mathbb { Z } [ \pi ] )$is the image of the ordinary Euler characteristic$\chi ( X ) \in \mathbb { Z } .$ under the natural map

$$
\mathbb {Z} \cong K _ {0} (\mathbb {Z}) \to K _ {0} (\mathbb {Z} [ \pi ])
$$

that takes an integer c to the class of the Z-module$\mathbb { Z } ^ { c }$, and then to the$\mathbb { Z } [ \pi ] .$ module$\mathbb { Z } [ \pi ] ^ { c }$

Definition 1.11.1. Let R be any ring. The projective class group$\widetilde { K } _ { 0 } ( R )$is the cokernel of the natural homomorphism$K _ { 0 } ( \mathbb { Z } ) \to K _ { 0 } ( R )$e, or equivalently, the quotient of$K _ { 0 } ( R )$by the subgroup generated by R viewed as a finitely generated free, hence projective, R-module of rank 1.

Here is an extension of the previous example, due to Terry Wall [71] from 1965, which involves the projective class group$\widetilde { K } _ { 0 } ( \mathbb { Z } [ \pi ] )$in a much more esesential way. A first step towards the classification of compact manifolds is to determine which homotopy types of spaces are realized by manifolds. A second step is then to determine how many diferent manifolds there are of the same homotopy type, and a third step is to understand the symmetries of each of these manifolds.

Staying with the first step, every compact manifold M can be embedded in some Euclidean space$\mathbb { R } ^ { k }$, and is then a retract of some open neighborhood in$\mathbb { R } ^ { k }$ Such a space is called an Euclidean neighborhood retract, abbreviated$E N R$ Each compact ENR is a retract of a finite simplicial complex, hence of a finite CW complex. See [26, App. A] for proofs of these results. So when searching for manifolds, we need only consider those homotopy types of spaces that are homotopy equivalent to retracts of finite CW complexes. It is convenient to relax the ‘retraction’ condition as follows.

Definition 1.11.2. A space X is dominated by a space Y if there are maps d :$Y  X$and$s \colon X \to Y$such that ds :$X  X$is homotopic to the identity on X.

![](images/page_24_image_10.jpg)

In other words, X is a ‘retract up to homotopy’ of Y . We say that X is finitely dominated if it is dominated by a finite CW complex Y .

It is known that all compact manifolds are homotopy equivalent to finite CW complexes. This is clear for piece-wise linear manifolds (since these admit a triangulation as a finite simplicial complex), hence also for smooth manifolds, but is a deep fact due to Rob Kirby and Larry Siebenmann [34] for topological manifolds.

This leads to the question whether a finitely dominated space$X ,$, i.e., a space dominated by a finite CW complex, must itself be homotopy equivalent to a finite CW complex. The answer is ‘yes’ for simply-connected X, as follows from [26, Prop. 4C.1]. However, for general X the answer involves an element in the projective class group$\widetilde { K } _ { 0 } ( \mathbb { Z } [ \pi ] )$, known as Wall’s finiteness obstruction.

Example 1.11.3. Suppose that X is dominated by a finite CW complex$Y .$ We may assume that both$X$and$Y$are path connected, and that$X$has a universal covering space$p \colon \tilde { X }  X$. Let$d \colon Y  X$be the dominating map, with homotopy section$s \colon X \to Y$. Let$q \colon \widetilde { Y }  Y$be the pullback of p along d. The pullback of$q$ealong s is then the pullback of$p$along a map homotopic to the identity, hence is isomorphic to$p .$. We get a commutative diagram:

$$
\begin{array}{c} \widetilde {X} \xrightarrow {\tilde {s}} \widetilde {Y} \xrightarrow {\tilde {d}} \widetilde {X} \\ p \Biggl \downarrow \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad X \xrightarrow {s} Y \xrightarrow {d} X \end{array}
$$

Note that the fundamental group$\pi = \pi _ { 1 } ( X )$acts freely on both$\widetilde { X }$and$\widetilde { Y }$ e ethrough deck transformations, so that ˜d and ˜s are π-equivariant maps. Let $b \colon Y \to Y$be a cellular approximation to the composite map sd:$Y  Y$, i.e., a cellular map such that$b \simeq s d$. Since the composite$d s \colon X  X$is homotopic to the identity, it follows that$b ^ { 2 } = b b$is homotopic to b, i.e., that b is homotopy idempotent. Likewise, there is a π-equivariant cellular map$\tilde { b } \colon \widetilde { Y } \to \widetilde { Y }$covering $b ,$with$\tilde { b } \simeq \tilde { s } \tilde { d }$. The induced map of bounded chain complexes

$$
\tilde {b} _ {*} \colon C _ {*} (\widetilde {Y}) \to C _ {*} (\widetilde {Y})
$$

of finitely generated free$\mathbb { Z } [ \pi ] \mathrm { - m o d u l e s }$is then chain homotopy idempotent, in the sense that$( \tilde { b } _ { * } ) ^ { 2 } = \tilde { b } _ { * } \tilde { b } _ { * }$is chain homotopic to$\tilde { b } _ { * }$. Wall uses this to show that the singular chain complex of$\widetilde { X }$, as a complex of$\mathbb { Z } [ \pi ]$]-modules, is chain homoetopy equivalent to a bounded chain complex$P _ { * }$of finitely generated projective Z[π]-modules

$$
S _ {*} (\widetilde {X}) \simeq P _ {*}.
$$

(If$\tilde { b } _ { * }$were strictly idempotent, we could let$P _ { * }$be the image of$\tilde { b } _ { * }$in$C _ { * } ( \widetilde { Y } )$，with complementary summand$Q ,$<sub>∗</sub> the image of$i d - \tilde { b } _ { * }$. Since$\tilde { b } _ { * }$eis only chain homotopy idempotent, the precise construction is a bit more complicated.) Here each$P _ { n }$is a finitely generated projective$\mathbb { Z } [ \pi ]$-module, with an isomorphism class$\left[ P _ { n } \right]$in$\pi _ { 0 } ( { \mathcal { P } } ( \mathbb { Z } [ \pi ] ) )$, and only finitely many$P _ { n }$are nonzero. However, the interesting, well-defined, quantity is the alternating sum

$$
[ X ] = \sum_ {n \geq 0} (- 1) ^ {n} [ P _ {n} ] \in K _ {0} (\mathbb {Z} [ \pi ])
$$

and its image$\theta ( X ) \in \widetilde { K } _ { 0 } ( \mathbb { Z } [ \pi ] )$. If X is itself a finite CW complex, we saw in the eprevious example that this class [X] is in the image of$K _ { 0 } ( \mathbb { Z } )$in$K _ { 0 } ( \mathbb { Z } [ \pi ] )$, hence maps to zero in the projective class group$\widetilde { K } _ { 0 } ( \mathbb { Z } [ \pi ] )$. Wall’s theorem in this conetext is that the converse holds: a finitely dominated X is homotopy equivalent to a finite CW complex if and only if the class$\theta ( X )$is zero in$\widetilde { K _ { 0 } } ( \mathbb { Z } [ \overline { { \pi } } ] )$. This class is therefore called$W a l l \ ' s$e finiteness obstruction. For our purposes, the main thing to note is that this theorem requires the zero-th algebraic K-group to form the alternating sum [X], which maps to the finiteness obstruction$\theta ( X )$ in the projective class group. For further references, the survey [19] may be a good place to start.

## 1.12 Homology of linear groups

Recall the homotopy equivalence

$$
| \operatorname{iso} (\mathcal {F} (R)) | \simeq \coprod_ {n \geq 0} B G L _ {n} (R)
$$

and the induced isomorphism

$$
H _ {*} (| \operatorname{iso} (\mathcal {F} (R)) |) \cong \bigoplus_ {n \geq 0} H _ {*} (B G L _ {n} (R)).
$$

One way to understand the group homology of the general linear groups$G L _ { n } ( R )$ is thus to understand the homology of the classifying space of the groupoid ${ \mathcal { F } } ( R )$

There is a stabilization homomorphism$G L _ { n } ( R ) \to G L _ { n + 1 } ( R )$given by block sum$A \longmapsto \left[ { A \atop 0 } { \begin{array} { l } { 0 } \\ { 1 } \end{array} } \right]$with the$1 \times 1$matrix$[ 1 ] \in G L _ { 1 } ( R )$. We let$G L _ { \infty } ( R ) =$ colim$\mathfrak { i } _ { n } G L _ { n } ( R )$be the increasing union of all of the finite$G L _ { n } ( R )$. The elements of$G L _ { \infty } ( R )$are infinite matrices with entries in R, that agree with the identity matrix except in finitely many places. Applying bar constructions, there are stabilization maps$B G L _ { n } ( R ) \to B G L _ { n + 1 } ( R )$for all$n ,$and

$$
B G L _ {\infty} (R) = \underset {n} {\operatorname{colim}} B G L _ {n} (R)
$$

is the increasing union of all of these spaces.

After passage to loop space completion, along the map

$$
\iota \colon \coprod_ {n \geq 0} B G L _ {n} (R) \to K (\operatorname{iso} (\mathscr {F} (R))),
$$

the block sum with [1] becomes homotopy invertible. It follows that ι factors as a composite

$$
\coprod_ {n \geq 0} B G L _ {n} (R) \xrightarrow {\alpha} \mathbb {Z} \times B G L _ {\infty} (R) \xrightarrow {\beta} K (\mathrm{iso} (\mathcal {F} (R))),
$$

where α is the natural inclusion that takes$B G L _ { n } ( R )$to$\{ n \} \times B G L _ { \infty } ( R )$. By the homology fibration theorem of Dusa McDuf and Graeme Segal [46], or Quillen’s $^ { 6 6 } Q = + \ '$theorem, presented by Daniel Grayson in [23], the second map$\beta$is a homology isomorphism. Furthermore, each path component of$K ( \operatorname { i s o } ( { \mathcal { F } } ( R ) ) )$ is homotopy equivalent to the base point path component$K ( R ) _ { 0 }$of$K ( R ) =$ $K ( \operatorname { i s o } ( \mathcal { P } ( R ) ) )$). Hence

$$
\beta_ {*} \colon H _ {*} (B G L _ {\infty} (R)) \xrightarrow {\cong} H _ {*} (K (R) _ {0})
$$

is an isomorphism, This means that if we can identify the (infinite) loop space $K ( R )$and compute its homology, then we have also computed the homology of the infinite general linear group$G L _ { \infty } ( R )$

It then remains to understand the efect of α in homology. It turns out that, for many reasonable rings$R ,$, the stabilization$G L _ { n } ( R ) \to G L _ { n + 1 } ( R )$induces homomorphisms

$$
H _ {i} (B G L _ {n} (R)) \rightarrow H _ {i} (B G L _ {n + 1} (R))
$$

that are isomorphisms for i in a range that grows to infinity with n. See Charney [10] for one such result, which applies when R is a Dedekind domain. Hence, for i in this stable range, there are isomorphisms$H _ { i } ( B G L _ { n } ( R ) ) \cong H _ { i } ( K ( R ) _ { 0 } )$

Example 1.12.1.$[ [ R = \mathbb { C }$with the usual topology, with$B L _ { n } ( \mathbb { C } ) \simeq B U ( n )$ homotopy equivalent to the Grassmannian$\operatorname { G r } _ { n } ( \mathbb { C } ^ { \infty } )$) of complex n-dimensional subspaces in$\mathbb { C } ^ { \infty }$, and K-theory space$\mathbb { Z } \times B U . ] ]$

Example 1.12.2. This method was successfully applied by Quillen [54] in the case when$R = \mathbb { F } _ { q }$is a finite field with$q = p ^ { d }$elements, and his definition of the higher algebraic K-groups was motivated by this approach.

Quillen first relates the base point component$K ( \mathbb { F } _ { q } ) _ { 0 }$to the infinite Grassmannian$B U ,$and the homotopy fixed-points$F \psi ^ { q }$for the Adams operation $\psi ^ { q } \colon B U \to B U$. For each prime$\ell \neq p ,$this lets him calculate its homology algebra (implicitly with coeficients in$\mathbb { Z } / \ell )$as

$$
H _ {*} (B G L _ {\infty} (\mathbb {F} _ {q})) \cong P (\xi_ {1}, \xi_ {2}, \dots) \otimes E (\eta_ {1}, \eta_ {2}, \dots),
$$

where$\deg ( \xi _ { j } ) = 2 j r , \deg ( \eta _ { j } ) = 2 j r - 1 ,$r is the least natural number such that $\ell \mid q ^ { r } - 1$, and$P$and$E$denote the polynomial algebra and the exterior algebra on the given generators, respectively. Then he goes on to study$\alpha _ { * }$, and finds that it is injective, with image

$$
\bigoplus_ {n \geq 0} H _ {*} (B G L _ {n} (\mathbb {F} _ {q})) \cong P (\epsilon , \xi_ {1}, \xi_ {2}, \dots) \otimes E (\eta_ {1}, \eta_ {2}, \dots),
$$

where$\epsilon \in H _ { 0 } ( G L _ { 1 } ( \mathbb { F } _ { q } ) )$is the class of$[ 1 ] , \ \xi _ { j } \ \in \ H _ { 2 j r } ( G L _ { r } ( \mathbb { F } _ { q } ) )$and$\eta _ { j } ~ \in$ $H _ { 2 j r - 1 } ( G L _ { r } ( \mathbb { F } _ { q } ) )$. From this, each individual group$H _ { * } ( B G L _ { n } ( \mathbb { F } _ { q } ) )$can be extracted.

In the case of (implicit)$\mathbb { Z } / p \cdot$-coeficients, the results are less complete, but in the limiting case

$$
H _ {i} (B G L _ {\infty} (\mathbb {F} _ {q})) = 0
$$

for all$i > 0$, so it follows by homological stability that$H _ { i } ( B G L _ { n } ( \mathbb { F } _ { q } ) ; \mathbb { Z } / p ) = 0$ for all n suficiently large compared to i.

Example 1.12.3. When$R = \mathcal { O } _ { F }$is the ring of integers in a number field $F _ { ; }$Armand Borel [7] uses analysis on symmetric spaces to compute the rational cohomology algebra$\mathsf { \tilde { H } } ^ { * } ( B S L _ { n } ( R ) ; \mathbb { Q } )$in a range of degrees that grows to infinity with n. Hence he can determine the rational (co-)homology of$B G L _ { \infty } ( R )$and $K ( R )$, which in turn determines the rational algebraic K-groups$K _ { i } ( R ) \otimes \mathbb { Q }$ The conclusion is that

$$
\operatorname{rank} K _ {i} (\mathcal {O} _ {F}) \otimes \mathbb {Q} = \left\{ \begin{array}{l l} 0 & i \equiv 0 \mod 4 \\ r _ {1} + r _ {2} & i \equiv 1 \mod 4 \\ 0 & i \equiv 2 \mod 4 \\ r _ {2} & i \equiv 3 \mod 4 \end{array} \right.
$$

for$i \geq 2$, where$r _ { 1 }$and$r _ { 2 }$are the number of real and complex places of$F ,$ respectively. For example, when$F = \mathbb { Q } , R = \mathbb { Z }$and$i \geq 2$the rank of$K _ { i } ( \mathbb { Z } ) \otimes \mathbb { Q }$ is one for$i \equiv 1$mod 4 and zero otherwise.

Furthermore, by a theorem of Quillen [56], which rests on a duality theorem of Borel–Serre and finiteness theorems of Ragunathan, each group$K _ { i } ( { \mathcal { O } } _ { F } )$is finitely generated. Hence, for$i \geq 2$each group$K _ { i } ( \mathbb { Z } )$is the sum of a copy of Z and a finite group for$i \equiv 1$mod 4, and is a finite group otherwise.

[[Also results for rings of integers in local fields, group rings of finite groups.]]

Example 1.12.4. When$R = \mathcal { O } _ { F } [ 1 / p ]$is the ring of p-integers in a local or global number field F, Bill Dwyer and Steve Mitchell [15, §10] have been able to continue Quillen’s approach, to compute

$$
H _ {*} (B G L _ {\infty} (R); \mathbb {Z} / p)
$$

under the assumption that the so-called Lichtenbaum–Quillen conjecture [[References]] holds for R. This conjecture asserts that mod p algebraic K-theory satisfies ´etale descent in suficiently high degrees, and has been proved by Vladimir Voevodsky [66] for$p = 2$, and has been announced proved by Voevodsky and Markus Rost for all odd primes. Again, the stable computations lead to unstable results in a finite range, by homological stability. Similar results hold in the ‘geometric’ case of curves over finite fields, see [14].

## 1.13 Homology of symmetric groups

The case of symmetric groups is similar. The homotopy equivalence

$$
| \operatorname{iso} (\mathbf {F i n}) | \simeq \coprod_ {n \geq 0} B \Sigma_ {n}
$$

induces the isomorphism

$$
H _ {*} (| \operatorname{iso} (\mathbf {F i n}) |) \cong \bigoplus_ {n \geq 0} H _ {*} (B \Sigma_ {n}).
$$

There are stabilization homomorphisms$\Sigma _ { n }  \Sigma _ { n + 1 }$, and we let$\Sigma _ { \infty } = \operatorname { c o l i m } _ { n } \Sigma _ { n }$ be the union of all the finite$\Sigma _ { n }$. We can view elements of$\Sigma _ { \infty }$as permutations of N that fix all but finitely many elements. Let$B \Sigma _ { \infty } = \operatorname { c o l i m } _ { n } B \Sigma _ { n }$

The homology groups$H _ { * } ( B \Sigma _ { n } )$and$H _ { * } ( B \Sigma _ { \infty } )$were first determined by Minoru Nakaoka [49], [50]. The results can be collected in a more structured form by the use of loop space completion, using the homology operations of Kudo–Araki [36] (for p = 2) and Dyer–Lashof [16] (for p odd), as explained by Peter May in [11, Thm. I.4.1].

The loop space completion map

$$
\iota \colon \coprod_ {n \geq 0} B \Sigma_ {n} \to K (\text { iso } (\mathbf {F i n}))
$$

factors as the composite

$$
\coprod_ {n \geq 0} B \Sigma_ {n} \xrightarrow {\alpha} \mathbb {Z} \times B \Sigma_ {\infty} \xrightarrow {\beta} K (\text { iso } (\mathbf {F i n}))  ,
$$

and$\beta$is a homology isomorphism. Here, by the Barratt–Priddy–Quillen theorem [5],

$$
K (\mathrm{iso} (\mathbf {F i n})) \simeq Q (S ^ {0})
$$

where for a based space X we write

$$
Q (X) = \underset {m} {\operatorname{colim}}   \Omega^ {m} \Sigma^ {m} X  .
$$

[[Forward reference to our proof.]]

Now we can easily compute$H _ { * } ( Q ( S ^ { n } ) ) \cong H _ { * } ( S ^ { n } )$for$* < 2 n$by the Freudenthal suspension theorem, and then use the Serre spectral sequence for the loop– path fibration of$Q ( S ^ { n } )$, with$\Omega Q ( S ^ { n } ) \simeq Q ( S ^ { n - 1 } )$, to compute$H _ { * } ( Q ( S ^ { n - k } )$for $* < 2 n - k ,$, by a downward induction. For$k = n$this computes$H _ { * } ( Q ( S ^ { 0 } ) )$for $* < n$, so starting with n arbitrarily large, we can use these topological methods to compute

$$
\beta_ {*} \colon H _ {*} (\mathbb {Z} \times B \Sigma_ {\infty}) \cong H _ {*} (Q (S ^ {0})).
$$

After this is done, it is not too hard to show that$\alpha _ { * }$is injective, and to determine its image$\textstyle \bigoplus _ { n > 0 } H _ { * } ( B \Sigma _ { n } )$, from which each individual group$H _ { * } ( B \Sigma _ { n } )$ can be extracted. [[State outcome.]]

## 1.14 Ideal class groups

[[See Neukirch [51, Ch. I] for an introduction to algebraic number theory.]]

Let$F$be a number$~ f i e l d ,$i.e., a finite extension of the rational numbers$\mathbb { Q } .$ and let$\mathcal { O } _ { F }$be its ring of integers. For each nonzero$a \in { \mathcal { O } } _ { F }$the principal ideal $( a ) = a \mathcal { O } _ { F }$admits a unique factorization

$$
(a) = \prod_ {\mathfrak {p}} \mathfrak {p} ^ {\nu_ {\mathfrak {p}} (a)}
$$

as a finite product of prime ideals. For each nonzero fraction$a / b \in F ^ { \times }$, let $\nu _ { \mathfrak { p } } ( a / b ) = \nu _ { \mathfrak { p } } ( a ) - \nu _ { \mathfrak { p } } ( b )$. The rule that takes$a / b$to the of integers$\nu _ { \mathfrak { p } } ( a / b )$, as p ranges over all prime ideals, defines a homomorphism ν:

$$
0 \to \mathcal {O} _ {F} ^ {\times} \to F ^ {\times} \xrightarrow {\nu} \bigoplus_ {\mathfrak {p}} \mathbb {Z} \to \operatorname{Cl} (F) \to 0
$$

The kernel of$\nu$is the group of units in${ \mathcal { O } } _ { F } ,$, while the cokernel of$\nu$is the ideal class group of$F$. This is a finite group, which measures to what extent unique factorization into prime elements holds in the ring$\mathcal { O } _ { F }$. Its order,$h _ { F } = \# \operatorname { C l } ( F )$, is the class number of$F .$

Let$p$be a prime and let$\zeta _ { p }$be a primitive p-th root of unity. The$p { - } t h$ cyclotomic field is$F = \mathbb { Q } ( \zeta _ { p } )$, with ring of integers$\mathcal { O } _ { F } = \mathbb { Z } [ \zeta _ { p } ]$. Let A be the p-Sylow subgroup of the ideal class group$\operatorname { C l } ( \mathbb { Q } ( \zeta _ { p } ) )$. The prime$p$is said to be regular of$p$does not divide the class number$h _ { p }$of$\mathbb { Q } ( \zeta _ { p } )$, and is otherwise irregular. Of the primes less than 100, only 37, 59 and 67 are irregular. In 1850, Ernst Kummer proved Fermat’s last theorem, that$x ^ { p } + y ^ { p } = z ^ { p }$has no solutions in natural numbers, for all odd regular primes.

Let A be the p-Sylow subgroup of$\operatorname { C l } ( \mathbb { Q } ( \zeta _ { p } ) )$, which is trivial if and only if$p$ is regular. Consider the Galois group

$$
\Delta = \mathrm{Gal} (\mathbb {Q} (\zeta_ {p}) / \mathbb {Q}) \cong (\mathbb {Z} / p) ^ {\times},
$$

which is cyclic of order$( p - 1 )$. Here an automorphism$\sigma$of$\mathbb { Q } ( \zeta _ { p } )$corresponds to the unit$u \in ( \mathbb { Z } / p ) ^ { \times }$such that$\sigma ( \zeta ) = \zeta ^ { u }$for all roots of unity$\zeta .$

The Galois action on the p-th cyclotomic field induces an action of$\Delta$on $\operatorname { C l } ( \mathbb { Q } ( \zeta _ { p } ) )$and A. Since the order of$\Delta$is prime to$p ,$the latter action decomposes into eigenspaces

$$
A \cong \bigoplus_ {i = 0} ^ {p - 2} A ^ {[ i ]}
$$

where the Galois action on any x in the i-th summand satisfies$\sigma ( x ) = \omega ( u ) ^ { i } x$ for all$\sigma \in \Delta$, with u as above and$\omega \colon ( \mathbb { Z } / p ) ^ { \times } \to \mathbb { Z } _ { p } ^ { \times }$the Teichm¨uller character. For example,$A ^ { [ 0 ] }$is the part of A that is fixed by the ∆-action.

A classical conjecture, first made by Kummer but known as the Vandiver conjecture, asserts that all of the even-indexed eigenspaces$A ^ { [ i ] }$are trivial. A more recent conjecture, made by Kenkichi Iwasawa [29], is that all of the oddindexed eigenspaces$A ^ { [ i ] }$are (trivial or) cyclic. The Vandiver conjecture is known to imply Iwasawa’s conjecture.

[[See Kurihara [37] for more about the relation between the classical conjectures about cyclotomic fields and the algebraic$K \cdot$groups of the integers.]]

By Kummer theory there is a ∆-equivariant isomorphism

$$
A \cong H _ {e t} ^ {2} (\mathbb {Z} [ 1 / p, \zeta_ {p} ]; \mathbb {Z} _ {p} (1)),
$$

where the group on the right hand side an an ´etale cohomology group.$\mathrm { B y }$ Galois descent, there is an isomorphism

$$
A ^ {[ 1 - j ]} \cong H _ {e t} ^ {2} (\mathbb {Z} [ 1 / p ], \mathbb {Z} _ {p} (j))
$$

for all$j = 1 - i$. Dwyer and Friedlander have constructed a version of algebraic K-theory that is designed to satisfy ´etale descent, known as ´etale K-theory [13]. There is a natural homomorphism

$$
\rho \colon K _ {*} (\mathbb {Z}) \otimes \mathbb {Z} _ {p} \to K _ {*} ^ {e t} (\mathbb {Z} [ 1 / p ]; \mathbb {Z} _ {p})
$$

that is known to be surjective for all$* \geq 2$, and an isomorphism

$$
K _ {2 j - 2} ^ {e t} (\mathbb {Z} [ 1 / p ]; \mathbb {Z} _ {p}) \cong H _ {e t} ^ {2} (\mathbb {Z} [ 1 / p ], \mathbb {Z} _ {p} (j))
$$

for all$j \geq 2$. This is a consequence of the ´etale descent spectral sequence

$$
E _ {s, t} ^ {2} = H _ {e t} ^ {- s} (\mathbb {Z} [ 1 / p ]; \mathbb {Z} _ {p} (t / 2)) \Longrightarrow K _ {s + t} ^ {e t} (\mathbb {Z} [ 1 / p ]; \mathbb {Z} _ {p}),
$$

which collapses for$p$odd, and which is analogous to the Atiyah–Hirzebruch spectral sequence

$$
E _ {2} ^ {s, t} = H ^ {s} (X; K ^ {t} (*)) \Longrightarrow K ^ {s + t} (X)
$$

associated to the generalized cohomology theory of complex topological$K \mathfrak { - }$ theory.

Proposition 1.14.1. If$K _ { 4 k } ( \mathbb { Z } ) = 0$for all$k \geq 1$, then the Vandiver conjecture is true.

Proof. If$K _ { 4 k } ( \mathbb { Z } ) = 0$for all$k \geq 1$, then$K _ { 4 k } ^ { e t } ( \mathbb { Z } [ 1 / p ] ; \mathbb { Z } _ { p } ) = 0$for all$k \geq 1$, so $H _ { e t } ^ { 2 } ( \mathbb { Z } [ 1 / p ] ; \mathbb { Z } _ { p } ( j ) ) = 0$for all odd$j \geq 3$, which implies that$A ^ { [ 1 - j ] } = 0$for all odd$j \geq 3 ,$. Now$A ^ { [ i ] }$is$( p - 1 )$)-periodic in$i ,$so this implies that$A ^ { [ i ] } = 0$for all even i.□

According to the Lichtenbaum–Quillen conjecture for$\mathbb { Z } ,$the homomorphism $\rho$should be an isomorphism for all$* \geq 2$. This conjecture is claimed to have been proved by Rost and Voevodsky. Assuming this, the converse also holds: If the Vandiver conjecture holds then$K _ { 4 k } ( \mathbb { Z } ) = 0$for all$k \geq 1$

Lee–Szczarba [39], Soul´e and the author [58] proved that$K _ { 4 } ( \mathbb { Z } ) = 0$, corresponding to the case$k = 1$above, which implies that$A ^ { [ p - 3 ] } = 0$for all$p .$

[[Further work by Soul´e et al.]]

[[Finite generation of algebraic K-theory groups implies finite generation of ´etale cohomology groups.]]

## 1.15 Automorphisms of manifolds

Let M be a compact smooth manifold. The space of all manifolds difeomorphic to M is homotopy equivalent to the classifying space

## B Dif(M)

of the topological group of difeomorphisms$M \ { \stackrel { \cong } { \longrightarrow } } \ M$fixing the boundary, i.e., the group of smooth symmetries of M. In the refined classification of manifolds we are therefore interested in understanding the homotopy type of this topological group.

An isotopy of M is a smooth path$I \to \operatorname { D i f f } ( M )$, taking$t \in I$to a difeomorphism$\phi _ { t } \colon M \to M$. Letting$\Phi ( x , t ) = \phi _ { t } ( x )$, we can rewrite the path as a difeomorphism$\Phi \colon M \times I  M \times I$that commutes with the projections to$I , \mathrm { ~ A ~ }$ concordance$( =$pseudo-isotopy) of M is a difeomorphism Ψ :$M \times I  M \times I$ that fixes$M \times \{ 0 \}$and$\partial M \times I .$, but does not necessarily commute with the projections to I. Let$C ( M )$be the space of all concordances of M. There is a homotopy fiber sequence

$$
\operatorname{Diff} (M \times I) \longrightarrow C (M) \xrightarrow {r _ {1}} \operatorname{Diff} (M)
$$

where$r _ { 1 }$restricts$\Psi$to$M \times 1$, and a canonical involution on$C ( M )$that after inverting 2 decomposes$\pi _ { * } C ( M )$into (+1)- and (−1)-eigenspaces corresponding to$\pi _ { * } \operatorname { D i f f } ( M \times I )$and$\pi _ { * } \operatorname { D i f f } ( M )$. [[In what order?]]

There is also a stabilization map$C ( M ) \to C ( M \times I )$, and passing to the colimit one can form the stable concordance space

$$
\mathcal {C} (M) = \underset {n} {\operatorname{colim}} C (M \times I ^ {n}).
$$

By Kiyoshi Igusa’s stability theorem [30], the connectivity of the map$C ( M ) \to$ $\mathcal { C } ( M )$grows to infinity with the dimension of M, so that$\pi _ { j } C ( M ) \cong \pi _ { j } \mathcal { C } ( M )$ for all$j \ll n = \dim ( M )$

The relation to algebraic K-theory is as follows. Waldhausen’s algebraic Ktheory of the space$M ,$, denoted$A ( M )$, can be defined as the algebraic K-theory $K ( \mathbb { S } [ \Omega M ] )$of the spherical group ring$\mathbb { S } [ \Omega M ] = \Sigma ^ { \infty } ( \Omega M ) _ { + }$, where S is the sphere spectrum and ΩM is a group model for the loop space of M. According to the stable parametrized h-cobordism theorem, first claimed by Allen Hatcher [25], and later proved by Friedhelm Waldhausen, Bjørn Jahren and the author [70], there are homotopy equivalences

$$
A (M) \simeq Q (M _ {+}) \times \mathrm{Wh} ^ {\mathrm{Diff}} (M)
$$

and

$$
\Omega \operatorname{Wh} ^ {\operatorname{Diff}} (M) \simeq \operatorname{Wh} _ {1} (\pi) \times B \mathcal {C} (M),
$$

where$Q ( M _ { + } ) = \mathrm { c o l i m } _ { n } \Omega ^ { n } \Sigma ^ { n } ( M _ { + } )$and$\mathrm { W h } _ { 1 } ( \pi ) = K _ { 1 } ( \mathbb { Z } [ \pi ] ) / ( \pm \pi )$is the Whitehead group. Hence there are isomorphisms

$$
\pi_ {i} A (M) \cong \pi_ {i} ^ {S} (M _ {+}) \oplus \pi_ {i - 2} \mathcal {C} (M)
$$

for all$i \geq 2$

In the special case$M = *$, there is a rational equivalence$A ( * ) = K ( \mathbb { S } )$ $K ( \mathbb { Z } )$, so Borel’s calculation of$K _ { i } ( \mathbb { Z } ) \otimes \mathbb { Q }$gives a calculation of$\pi _ { j } \mathcal { C } ( * ) \otimes \mathbb { Q } _ { : }$ hence also a calculation of$\pi _ { j } C ( D ^ { n } ) \otimes \mathbb { Q }$for$j \ll n$. Taking the involution into account, one reaches the following conclusion:

Theorem 1.15.1.$F o r i \ll n ,$

$$
\pi_ {i} \operatorname{Diff} (D ^ {n}) \otimes \mathbb {Q} \cong \left\{ \begin{array}{l l} \mathbb {Q} & \text { for   } i = 4 k - 1 \text {   and   } n \text {   odd }, \\ 0 & \text { otherwise }. \end{array} \right.
$$

See [73] for a survey of this theory, and [70] for the proof of the stable parametrized h-cobordism theorem.

# Chapter 2

# Categories and functors

A reference for this chapter is Mac Lane [40, I,II].

## 2.1 Sets and classes

When studying classification problems, or algebraic K-theory, we are led to discuss sets, groups, topological spaces or other mathematical structures. Very quickly we are also led to consider all sets, all groups or all topological spaces. This leads to the question of what we really mean by all sets, all modules, and so on.

Does the collection of all sets have a mathematical meaning, as a mathematical object? In view of Bertrand Russell’s paradox (is the set R of all sets S that are not elements in themselves an element of itself?), the collection $R = \{ S \mid S \not \in S \}$cannot be a set. Then the collection A of all sets cannot be a set either, since R would be a subset of A, and thus a set.

We are therefore led to speak of collections more general than sets, which we call classes. For example, we will talk about the class of all sets, the class of all R-modules, and the class of all topological spaces.

The most common basis for set theory is the ZFC axiomatization of the notions of a set and the set membership relation ∈ due to Ernst Zermelo and Abraham Fraenkel (and concurrently, Thoralf Skolem), together with the axiom of choice.

Since ZFC is only an axiomatization of sets, it does not formalize the notion of a class. Instead, a class may be viewed as a label for the logical expression that characterizes its members, with the caveat that diferent logical expressions may characterize the same class. This way, we may say “for all sets” as part of a logical assertion, but the collection of all sets does not take on a set-theoretic meaning.

A diferent approach is formalized in the notion of a universe, discussed by Grothendieck and Jean-Louis Verdier in SGA4 [3, i.0].

Definition 2.1.1 (Universe). A Grothendieck universe is a nonempty set U such that

(a) If$X \in \mathbb { U }$and$Y \in X$then$Y \in \mathbb { U } ;$

(b) If$X , Y \in \mathbb { U }$then$\{ X , Y \} \in \mathbb { U }$;

(c) If$X \in \mathbb { U }$then${ \mathcal { P } } ( X ) \in \mathbb { U } ;$

(d) If$X _ { i } \in \mathbb { U }$for all$i \in I$and$I \in \mathbb { U } \ { \mathrm { t h e n } } \bigcup _ { i \in I } X _ { i } \in \mathbb { U } .$

Here${ \mathcal { P } } ( X ) = \{ Y \mid Y \subseteq X \}$is the power set of X and$\textstyle \bigcup _ { i \in I } X _ { i } = \{ Y \mid \exists i \in$ $I : Y \in X _ { i } \}$is the union of the sets$X _ { i }$for$i \in I$

A Grothendieck universe U provides a model for ZFC set theory. The sets in the model are precisely the elements of U, which are then called the U-small sets. These satisfy the axioms of ZFC. By a class we then mean a subset of U. Every set is a class, but not every class is a set. For example, the class of all U-small sets is U itself, which is not U-small. A proper class is a class that is not a set.

We hereafter assume that we have fixed a Grothendieck universe U containing the sets “we are interested in”, and use the terms set and class in the sense just explained.

The “axiom of universes”, asserting that every set is contained in some Grothendieck universe, is equivalent to the existence of arbitrarily large strongly inaccessible cardinals. This can then be taken as an additional axiom, together with ZFC. See [74].

Another approach is given by von Neumann–Bernays–G¨odel set theory, which axiomatizes both classes and sets.

## 2.2 Categories

The starting point for category theory is that for every kind of mathematical object, such as sets, groups or topological spaces, there is an preferred way of comparing two such objects, such as by functions, homomorphisms or continuous maps. In particular, two given objects may usefully be viewed as equivalent even if they are not identical, as in the case of sets of equal cardinality, isomorphic groups or homeomorphic spaces. The language of categories provides a framework for discussing these examples, and many more, in a uniform way.

Definition 2.2.1 (Category). A category$\mathcal { C }$consists of a class$\operatorname { o b j } ( { \mathcal { C } } )$of objects and, for each pair X, Y of objects, a set${ \mathcal { C } } ( X , Y )$of morphisms$f \colon X \to$ $Y$. For each object X there is an identity morphism$i d _ { X } \colon X \to X$. Furthermore, for each triple$X , Y , Z$of objects there is a composition law

$$
\circ \colon \mathcal {C} (Y, Z) \times \mathcal {C} (X, Y) \longrightarrow \mathcal {C} (X, Z),
$$

taking$( g , f )$to$g \circ f .$These must satisfy the left and right unit laws$i d _ { Y } \circ f = f$ and$f \circ i d _ { X } = f$for all$f \colon X \to Y$, and the associative law$( h \circ g ) \circ f = h \circ ( g \circ f )$ for all$f \colon X \to Y , g \colon Y \to Z$and$h \colon Z \to W$

The choice of identity morphisms and composition laws is part of the structure of the category. We say that X is the source and Y is the target of $f \colon X \to Y$. Each morphism$f$in the category is assumed to have a well-defined source and target, which means that the various sets${ \mathcal { C } } ( X , Y )$are assumed to be disjoint. When the source of$g$equals the target of$f$we call$g \circ f$the composite of$f$and$^ { g , }$in that order, and say that f and g are composable. We often abbreviate$g \circ f$to$g f .$. By the associative law, we can write$h \circ g \circ f$or$h g f$ for the common value of$( h \circ g ) \circ f$and$h \circ ( g \circ f )$). We often write$X \xrightarrow { = } X$to indicate an identity morphism.

Definition 2.2.2 (Commutative diagram). A diagram in a category$\mathcal { C }$is a collection of objects in$\mathcal { C }$and a collection of morphisms in$\mathcal { C }$between these objects. The diagram is said to be commutative if for any two objects X and $Y$in the diagram, and any two finite chains of composable morphisms in the diagram, both starting at$X$and ending at$Y$, then the two composite morphisms $X  Y$are equal in$\mathcal { C }$. For example, a square diagram

![](images/page_35_image_1.jpg)

is commutative precisely when$h f = i g$as morphisms$X  W$

Example 2.2.3. We can display the unit laws as the commutative triangles

![](images/page_35_image_4.jpg)

and the associative law as the commutative parallelogram

![](images/page_35_image_6.jpg)

Definition 2.2.4 (Small category). A category$\mathcal { C }$is small if ob$| ( \mathcal { C } )$is a set, rather than a proper class.

Example 2.2.5. Let Set be the category of sets and functions. Its objects are sets, so obj(Set) is the class of all sets. For each pair of sets X and$Y ,$, the set$\mathbf { S e t } ( X , Y )$of morphisms from X to Y is the set of functions$f \colon X \to Y$ The identity morphism of a set X is the identity function id$\chi \colon X \to X$, given by$i d _ { X } ( x ) = x$for all$x \in X$. The composite of two functions$f \colon X \to Y$ and$g \colon Y \to Z$is the function$g \circ f \colon X \to Z$given by$( g \circ f ) ( x ) = g ( f ( x ) )$1 for all$x \in X$. It is easy to verify that$( f \circ i d _ { X } ) ( x ) = f ( i d _ { X } ( x ) ) = f ( x )$ and$( i d _ { Y } \circ f ) ( x ) = i d _ { Y } ( f ( x ) ) = f ( x )$for all$x \in X$, so the unit laws hold. Furthermore,$( ( h \circ g ) \circ f ) ( x ) = ( h \circ g ) ( f ( x ) ) = h ( g ( f ( x ) ) )$equals$( h \circ ( g \circ f ) ) ( x ) =$ $h ( ( g \circ f ) ( x ) ) = h ( g ( f ( x ) ) )$for all$x \in X$, so the associative law holds. The class of all sets is not itself a set, so Set is not a small category.

Definition 2.2.6 (Finite sets n). For each non-negative integer n$\geq 0$let

$$
\mathbf {n} = \{1, 2, \dots , n \}.
$$

These are the finite initial segments of the natural numbers$\mathbb { N } = \{ 1 , 2 , 3 , . . . \}$ Note that$\mathbf { 0 } = \{ \} = \varnothing = \varnothing$is the empty set.

Remark 2.2.7. The boldface may serve as a reminder that this is not the set theorists’ notation, since they usually define n to be the set$\{ 1 , 2 , \ldots , n - 1 \}$

Example 2.2.8. Let$\mathcal { F }$be the skeleton category of finite sets. It is the category with objects the sets n for all$n \geq 0$, and morphisms$\mathcal { F } ( \mathbf { m } , \mathbf { n } )$the set of functions $f \colon \mathbf { m }  \mathbf { n }$, for each pair$m , n \geq 0$. More explicitly,$\mathcal { F } ( \mathbf { m } , \mathbf { n } )$is the set of functions

$$
f \colon \{1, 2, \dots , m \} \longrightarrow \{1, 2, \dots , n \}.
$$

There are$n ^ { m }$such functions. The identity functions and composition law in$\mathcal { F }$ are defined in the same way as in Set, and the unit and associative laws hold by the same arguments as above. The class of objects in$\mathcal { F }$is a set of subsets of N, hence is itself a set, so$\mathcal { F }$is a small category.

The term “skeleton category” will be explained in Definition 2.8.1, see also Definition 3.2.11.

Definition 2.2.9 (Subcategory). A subcategory of a category$\mathcal { D }$is a category $\mathcal { C }$such that$\operatorname { o b j } ( { \mathcal { C } } )$is a subclass of$\operatorname { o b j } ( \mathcal { D } )$, and for each pair of objects$X , Y$ in$\mathcal { C }$the morphism set$\mathcal { C } ( X , Y )$is a subset of the morphism set${ \mathcal { D } } ( X , Y )$ Furthermore, for each object X in$\mathcal { C }$the identity morphism$i d _ { X }$in$\mathcal { C }$is the same as the identity morphism in${ \mathcal { D } } .$and for each pair of composable morphisms $f$and g in$\mathcal { C } .$, the composite$g \circ f$in$\mathcal { C }$is the same as their composite in${ \mathcal { D } } .$

Definition 2.2.10 (Full subcategory). A subcategory$\mathcal { C } \subseteq \mathcal { D }$is said to be full if for each pair of objects X,$Y$in$\mathcal { C }$the morphism set$\mathcal { C } ( X , Y )$is equal to the morphism set${ \mathcal { D } } ( X , Y )$. A full subcategory$\mathcal { C }$of$\mathcal { D }$is thus determined by its class of objects obj(C ), as a subclass of${ \mathcal { D } } .$. We say that$\mathcal { C }$is the full subcategory generated by the subclass of objects$\operatorname { o b j } ( { \mathcal { C } } )$in$\operatorname { o b j } ( \mathcal { D } )$

Example 2.2.11. The small category$\mathcal { F }$of finite sets and functions is a full subcategory of the category Set of all sets and functions, namely the full subcategory generated by the objects$\mathbf { n } = \{ 1 , 2 , \dots , n \}$for$n \geq 0$

Example 2.2.12. Let$\mathbf { F i n } \subset \mathbf { S e t }$be the full subcategory generated by all finite sets, not necessarily of the form n. This is not a small category, since the class of all finite sets is not itself a set.

Definition 2.2.13 (Opposite category). Given a category$\mathcal { C }$, the opposite category$\mathcal { C } ^ { o p }$has the same class of objects as$\mathcal { C }$, but the morphisms in$\mathcal { C } ^ { o p }$from $X$to$Y$are the same as the morphisms in$\mathcal { C }$from$Y$to$X$. Hence

$$
\operatorname{obj} \left(\mathcal {C} ^ {o p}\right) = \operatorname{obj} (\mathcal {C})
$$

and

$$
\mathcal {C} ^ {o p} (X, Y) = \mathcal {C} (Y, X)
$$

for all pairs$X , ~ Y$of objects in$\mathcal { C } \ ( \mathrm { o r } \ \mathcal { C } ^ { o p } )$. For each object$X$, the identity morphism of X in$\mathcal { C } ^ { o p }$is equal to the identity morphism of X in$\mathcal { C } .$. For each triple$X , Y , Z$of objects the composition law

$$
\circ^ {o p} \colon \mathcal {C} ^ {o p} (Y, Z) \times \mathcal {C} ^ {o p} (X, Y) \longrightarrow \mathcal {C} ^ {o p} (X, Z)
$$

in$\mathcal { C } ^ { o p }$is equal to the function

$$
\mathcal {C} (Z, Y) \times \mathcal {C} (Y, X) \longrightarrow \mathcal {C} (Z, X)
$$

that takes a pair$( g , f )$of morphisms$g \colon Z \to Y$and$f \colon Y \to X$to their composite$f \circ g \colon Z \to X$in$\mathcal { C }$, with$f$and$g$appearing in the opposite of the usual order. Hence

$$
g \circ^ {o p} f = f \circ g.
$$

With this notation it is straightforward to verify that$\mathcal { C } ^ { o p }$is a category.

Lemma 2.2.14.$( \mathcal { C } ^ { o p } ) ^ { o p } = \mathcal { C }$

Proof. This is clear, since$g ( \circ ^ { o p } ) ^ { o p } f = f \circ ^ { o p } g = g \circ f .$

Example 2.2.15. To describe the opposite$\mathbf { S e t } ^ { o p }$of the category of sets, we must view a function$f \colon X \to Y$as a morphism$f$in$\mathbf { S e t } ^ { o p } ( Y , X )$One way to encode the function f is in terms of the preimage sets$f ^ { - 1 } ( y ) = \{ x \in X \mid$ $f ( x ) = y \}$for$y \in Y$. These are disjoint subsets of$X$that cover X. Hence a morphism$Y  X$in$\mathbf { S e t } ^ { o p }$can be defined to be a function$F \colon Y \to { \mathcal { P } } ( X )$ from$Y$to the power set${ \mathcal { P } } ( X )$of X, consisting of all subsets of X. We must demand that the values$\{ F ( y ) \mid y \in Y \}$form a disjoint cover of X. The identity morphism$Y  Y$is then the function$I \colon Y \to { \mathcal { P } } ( Y )$that takes$y \in Y$to the singleton set$\{ y \}$. Given another morphism$Z \to Y$in$\mathbf { S e t } ^ { o p }$, represented by a function$G \colon Z \to { \mathcal { P } } ( Y )$whose values form a disjoint cover of$Y _ { i \textrm { \scriptsize { F } } i }$, the composite morphism$Z \to X$in$\mathbf { S e t } ^ { o p }$is represented by the function$H \colon Z \to { \mathcal { P } } ( X )$given by

$$
H (z) = \bigcup_ {y \in G (z)} F (y)
$$

for$z \in Z$. This reflects the formula$\begin{array} { r } { ( g f ) ^ { - 1 } ( z ) = \bigcup _ { y \in g ^ { - 1 } ( z ) } f ^ { - 1 } ( y ) . } \end{array}$

Definition 2.2.16 (Product category). Given two categories$\mathcal { C } , \mathcal { C } ^ { \prime }$, the product category${ \mathcal { C } } \times { \mathcal { C } } ^ { \prime }$has as objects the pairs$( X , X ^ { \prime } )$where X is an object in$\mathcal { C }$and$X ^ { j }$is an object in$\mathcal { C } ^ { \prime }$:

$$
\operatorname{obj} \left(\mathcal {C} \times \mathcal {C} ^ {\prime}\right) = \operatorname{obj} (\mathcal {C}) \times \operatorname{obj} \left(\mathcal {C} ^ {\prime}\right).
$$

The morphisms in$\mathcal { C } \times \mathcal { C } ^ { \prime }$from$( X , X ^ { \prime } ) \ \mathrm { t o } \ ( Y , Y ^ { \prime } )$are the pairs$( f , f ^ { \prime } )$where $f \colon X \to Y$is a morphism in$\mathcal { C }$and$f ^ { \prime } \colon X ^ { \prime } \to Y ^ { \prime }$is a morphism in$\mathcal { C } ^ { \prime }$. Hence

$$
(\mathscr {C} \times \mathscr {C} ^ {\prime}) ((X, X ^ {\prime}), (Y, Y ^ {\prime})) = \mathscr {C} (X, Y) \times \mathscr {C} ^ {\prime} (X ^ {\prime}, Y ^ {\prime}).
$$

Given a second morphism$( g , g ^ { \prime } ) \colon ( Y , Y ^ { \prime } ) \to ( Z , Z ^ { \prime } )$, the composite in${ \mathcal { C } } \times { \mathcal { C } } ^ { \prime }$is given by

$$
(g, g ^ {\prime}) \circ (f, f ^ {\prime}) = (g \circ f, g ^ {\prime} \circ f ^ {\prime}).
$$

The identity morphism of$( X , X ^ { \prime } )$is$( i d _ { X } , i d _ { X ^ { \prime } } )$

Definition 2.2.17. More generally, suppose given a category$\mathcal { C } _ { i }$for each element i in a set I. The product category$\Pi _ { i \in I } { \mathcal { C } } _ { i }$has as objects families$( X _ { i } ) _ { i \in I }$ with$X _ { i }$an object in$\mathcal { C } _ { i }$for each$i \in I ,$, and the morphisms from$( X _ { i } ) _ { i \in I }$to $( Y _ { i } ) _ { i \in I }$are families$( f _ { i } ) _ { i \in I }$of morphisms$f _ { i } \colon X _ { i } \to Y _ { i }$for all$i \in I$. Composition is given by the formula

$$
(g _ {i}) _ {i \in I} \circ (f _ {i}) _ {i \in I} = (g _ {i} \circ f _ {i}) _ {i \in I}.
$$

The identity morphism of$( X _ { i } ) _ { i \in I } { \mathrm { ~ i s ~ } } ( i d _ { X _ { i } } ) _ { i \in I }$

When$I = \{ 1 , 2 \}$has two elements,$\Pi _ { i \in I } { \mathcal { C } } _ { i }$can be identified with the product$\mathcal { C } _ { 1 } \times \mathcal { C } _ { 2 }$defined above. When$I = \{ \bar { 1 } \}$has one element,$\Pi _ { i \in I } { \mathcal { C } } _ { i }$can be identified with the category$\mathcal { C } _ { 1 }$. When I is empty, the product$\textstyle \prod _ { i \in I } { \mathcal { C } } _ { i }$is the category ∗ with one object (an empty family of objects) and one morphism (an empty family of morphisms). We call ∗ the one-morphism category, since any other category with precisely one morphism will also have precisely one object.

[[Later see that these are the products in the category of small categories, and that ∗ is the terminal object. Needs mention of the projection functors $\begin{array} { r } { p r _ { j } \colon \prod _ { i \in I } \mathcal { C } _ { i } \longrightarrow \mathcal { C } _ { j } } \end{array}$for all$j \in I . ] ]$

Definition 2.2.18 (Coproduct category). Given two categories$\mathcal { C } , \mathcal { C } ^ { \prime }$, the coproduct category$\mathcal { C } \sqcup \mathcal { C } ^ { \prime }$has object class the disjoint union

$$
\operatorname{obj} \left(\mathcal {C} \sqcup \mathcal {C} ^ {\prime}\right) = \operatorname{obj} (\mathcal {C}) \sqcup \operatorname{obj} \left(\mathcal {C} ^ {\prime}\right)
$$

of the object classes of$\mathcal { C }$and$\mathcal { C } ^ { \prime }$, so an object of$\mathcal { C } \sqcup \mathcal { C } ^ { \prime }$is an object of$\mathcal { C }$or of $\mathcal { C } ^ { \prime } { } _ { ; }$, and$\operatorname { i f } \mathcal { C }$and$\mathcal { C } ^ { \prime }$have any objects in common, then we view them as being distinct in$\mathcal { C } \sqcup \mathcal { C } ^ { \prime }$. Given objects X, Y in$\mathcal { C }$and$X ^ { \prime } , Y ^ { \prime }$in$\mathcal { C } ^ { \prime }$, all viewed as objects in$\mathcal { C } \sqcup \mathcal { C } ^ { \prime }$, the morphisms in$\mathcal { C } \sqcup \mathcal { C } ^ { \prime }$from$X$to$Y$are the same as the morphisms$X  Y$in$\mathcal { C } _ { : }$, the morphisms from$X ^ { \prime }$to$Y ^ { \prime }$are the same as the morphisms$X ^ { \prime }  Y ^ { \prime }$in$\mathcal { C } ^ { \prime }$, and there are no morphisms$X  Y ^ { \prime }$or$X ^ { \prime }  Y$ In slightly diferent notation,

$$
(\mathcal {C} \sqcup \mathcal {C} ^ {\prime}) (X, Y) = \left\{ \begin{array}{l l} \mathcal {C} (X, Y) & \text {if X,Y\in obj(\mathcal {C})}, \\ \mathcal {C} ^ {\prime} (X, Y) & \text {if X,Y\in obj(\mathcal {C} ^{\prime})}, \\ \emptyset & \text {otherwise.} \end{array} \right.
$$

Composition and identities are given as in$\mathcal { C }$and$\mathcal { C } ^ { \prime }$.

The inclusions in:$\mathcal { C } \to \mathcal { C } \sqcup \mathcal { C } ^ { \prime }$and$i n ^ { \prime } \colon \mathcal { C } ^ { \prime } \to \mathcal { C } \sqcup \mathcal { C } ^ { \prime }$exhibit$\mathcal { C }$and$\mathcal { C } ^ { \prime }$as the full subcategories of$\mathcal { C } \sqcup \mathcal { C } ^ { \prime }$generated by$\operatorname { o b j } ( { \mathcal { C } } )$and$\mathrm { o b j } ( \mathcal { C } ^ { \prime } )$, respectively.

Definition 2.2.19. More generally, suppose given a category$\mathcal { C } _ { i }$for each element i in a set I. The coproduct category$\operatorname { I I } _ { i \in I } { \mathcal { C } } _ { i }$has object class the disjoint union of the object classes$\mathcal { C } _ { i }$. We may arrange that these object classes are disjoint by labeling each object with the index in$I { : }$

$$
\operatorname{obj} \left(\coprod_ {i \in I} \mathcal {C} _ {i}\right) = \bigcup_ {i \in I} \{i \} \times \operatorname{obj} \left(\mathcal {C} _ {i}\right)
$$

contained in$I \times \textstyle \bigcup _ { i \in I } { \mathrm { o b j } } ( \mathcal { C } _ { i } )$. This means that for each$i \in I$and$X \in \mathrm { o b j } ( \mathcal { C } _ { i } )$ we have an object$( i , X )$in$\operatorname { I I } _ { i \in I } { \mathcal { C } } _ { i }$, but we usually just write X for this object, if i is clear from the context. Given two elements$i , j \in I$and objects$X$in$\mathcal { C } _ { i }$ and$Y$in$\mathcal { C } _ { j }$, there are no morphisms$X  Y$in$\operatorname { I I } _ { i \in I } { \mathcal { C } } _ { i }$unless$i = j$, in which case the morphisms are the same as in$\mathcal { C } _ { i }$. The inclusion$i n _ { j } \colon \mathcal { C } _ { j }  \coprod _ { i \in I } \mathcal { C } _ { i }$ exhibits$\mathcal { C } _ { j }$as the full subcategory of$\operatorname { I I } _ { i \in I } { \mathcal { C } } _ { i }$generated by$\mathrm { o b j } ( \mathcal { C } _ { j } )$, for each $j \in I$

When$I = \{ 1 , 2 \}$has two elements,$\operatorname { I I } _ { i \in I } { \mathcal { C } } _ { i }$can be identified with the co-product$\mathcal { C } _ { 1 } \sqcup \mathcal { C } _ { 2 }$defined above. When$I = \langle \tilde { 1 } \tilde  \}$has one element,$\operatorname { I I } _ { i \in I } { \mathcal { C } } _ { i }$can be identified with the category$\mathcal { C } _ { 1 }$. When I is empty, the coproduct$\textstyle \prod _ { i \in I } { \mathcal { C } } _ { i }$is the empty category$\varnothing$with no objects and no morphisms.

[[Later see that these are the coproducts in the category of small categories, and that ∅ is the initial object.]]

## 2.3 Functors

There is a preferred way of comparing two categories, namely by a functor. Continuing the line of thought from the previous section, it follows that we should view categories as the objects of a new category, whose morphisms are the functors between these categories. More precisely, this turns out to work well for functors between small categories.

Definition 2.3.1 (Functor). Let$\mathcal { C }$and$\mathcal { D }$be categories. A functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$ from$\mathcal { C }$to D consists of two rules, one assigning to each object X of$\mathcal { C }$an object $F ( X )$of$\mathcal { D } .$, and a second one assigning to each morphism$f \colon X \to Y$in$\mathcal { C }$a morphism$F ( f ) \colon F ( X ) \to F ( Y )$in$\mathcal { D }$. We can write the rule$f \mapsto F ( f )$as a function

$$
F \colon \mathcal {C} (X, Y) \longrightarrow \mathcal {D} (F (X), F (Y))
$$

for each pair of objects X, Y in$\mathcal { C } .$. The rule on morphisms must satisfy

$$
F (i d _ {X}) = i d _ {F (X)}
$$

for each object$X$in$\mathcal { C } _ { : }$, and

$$
F (g \circ f) = F (g) \circ F (f)
$$

for each pair of composable morphisms$f$and$g$in$\mathcal { C }$. Note that the composite $g \circ f$is formed in${ \mathcal { C } } ,$while the composite$F ( g ) \circ F ( f )$is formed in$\mathcal { D }$

The functor$F$maps each commutative triangle in$\mathcal { C }$(as on the left)

![](images/page_39_image_10.jpg)

to a commutative triangle in$\mathcal { D }$(as on the right). Hence$F$maps any commutative diagram in$\mathcal { C }$to a commutative diagram in$\mathcal { D }$of the same shape. We often simplify notation by writing$f _ { * }$for$F ( f )$, in which case the conditions of functoriality appear as$( i d _ { X } ) _ { * } = i d _ { F ( X ) }$and$( g f ) _ { * } = g _ { * } f _ { * }$

Example 2.3.2. Let$F \colon { \mathcal { F } }$Set be the functor that takes each object n in$\mathcal { F }$ for$n \geq 0 .$, to the same set$\{ 1 , 2 , \ldots , n \}$, viewed as an object in Set. Furthermore, $F$takes each function$f \colon \mathbf { m }$n in$\mathcal { F } ( \mathbf { m } , \mathbf { n } )$to the same function, viewed as an element in$\mathbf { S e t } ( \mathbf { m } , \mathbf { n } )$. Since the identity morphisms and composition in$\mathcal { F }$ was defined in the same way as in Set, it is clear that$F$is a functor.

Definition 2.3.3 (Full, faithful functor). A functor$F \colon { \mathcal { C } }  { \mathcal { D } }$is full if for each pair of objects X, Y in$\mathcal { C } _ { : }$, the function${ \mathcal { C } } ( X , Y ) \to { \mathcal { D } } ( F ( X ) , F ( Y ) )$is surjective. The functor$F$is faithful if each function${ \mathcal { C } } ( X , Y ) \to { \mathcal { D } } ( F ( X ) , F ( Y ) )$ is injective, for each pair$X$, Y of objects in$\mathcal { C }$

Example 2.3.4. Let$\mathcal { C }$be a subcategory of$\mathcal { D }$. The inclusion functor$\mathcal { C } \to \mathcal { D }$ given by the inclusions$\mathrm { o b j } ( \mathcal { C } ) \subseteq \mathrm { o b j } ( \mathcal { D } )$and${ \mathcal { C } } ( X , Y ) \subseteq { \mathcal { D } } ( X , Y )$for all$X$ $Y$in${ \mathcal { C } } _ { : }$, is a faithful functor. It is full (and faithful) if and only if$\mathcal { C }$is a full subcategory of${ \mathcal { D } } .$. For instance, the functor$F \colon { \mathcal { F } }$Set of Example 2.3.2 is the full and faithful inclusion of$\mathcal { F }$as a full subcategory of Set.

Definition 2.3.5 (Identity, composition of functors). For each category$\mathcal { C }$ the inclusion functor of$\mathcal { C }$into itself specifies the identity functor$i d _ { \mathcal { C } } \colon \mathcal { C } \to \mathcal { C }$ Furthermore, given categories$\mathcal { C } , \mathcal { D } , \mathcal { E }$and functors$F \colon { \mathcal { C } } \to { \mathcal { D } }$and$G \colon { \mathcal { D } } \to { \mathcal { E } }$ there is a composite functor$G \circ F \colon \mathcal { C } \to \mathcal { E } .$, given by

$$
(G \circ F) (X) = G (F (X))
$$

for each object X in$\mathcal { C }$, and

$$
(G \circ F) (f) = G (F (f))
$$

for each morphism$f \colon X \to Y$in$\mathcal { C } .$. We often abbreviate$G \circ F$to$G F .$

It is easy to verify that$i d _ { \mathscr { C } }$and$G \circ F$are functors. For example, given another morphism$g \colon Y \to Z$in$\mathcal { C }$, we have$G ( F ( g \circ f ) ) = G ( F ( g ) \circ F ( f ) ) =$ $G ( F ( g ) ) \circ G ( F ( f ) ) , \mathrm { s o } \ ( G F ) ( g \circ f ) = ( G F ) ( g ) \circ ( G F ) ( f )$

Lemma 2.3.6. Let$\mathcal { C }$and$\mathcal { D }$be small categories. Then the collection of all functors$F \colon { \mathcal { C } } \to { \mathcal { D } }$is a set.

Proof. Since$\operatorname { o b j } ( { \mathcal { C } } )$and$\operatorname { o b j } ( \mathcal { D } )$are assumed to be sets, a functor consists of a function$F \colon \mathrm { { o b j } } ( \mathcal { C } ) \ \to \ \mathrm { { o b j } } ( \mathcal { D } )$and, for each pair of objects$X , Y$in$\mathcal { C } _ { : }$, a function$F \colon { \mathcal { C } } ( X , Y ) \to { \mathcal { D } } ( F ( X ) , F ( Y ) )$). There is a set of sets of sets of such, which is again a set. The collection of functors$\mathcal { C } \to \mathcal { D }$is a subset of this set, hence is also a set.□

Definition 2.3.7 (Category Cat). Let Cat be the category of small categories. Its objects are the small categories$\mathcal { C }$. The morphisms from$\mathcal { C }$to$\mathcal { D }$are the functors$F \colon \mathcal { C }  \mathcal { D }$. By the lemma above, the collection$\mathbf { C a t } ( \mathcal { C } , \mathcal { D } )$of all such functors is a set, since$\mathcal { C }$is small. The identity functor, and composition of functors, define the identities and composition in Cat.

Definition 2.3.8 (Contravariant functor). A contravariant functor F from $\mathcal { C }$to$\mathcal { D }$is the same as a functor$F \colon \mathcal { C } ^ { o p } \to \mathcal { D }$from the opposite category of$\mathcal { C }$to ${ \mathcal { D } } .$It thus consists of two rules, one assigning to each object X of$\mathcal { C }$an object $F ( X )$of${ \mathcal { D } } ,$, and another assigning to each morphism$f \colon X \to Y$in$\mathcal { C } .$, which is the same as a morphism$f \colon Y \to X$in$\mathcal { C } ^ { o p }$, a morphism$F ( f ) \colon F ( Y ) \to F ( X )$ in$\mathcal { D }$. (Note how the direction of the morphism$F ( f )$is reversed, compared to Definition 2.3.1.) We can write the rule$f \mapsto F ( f )$as a function

$$
F \colon \mathcal {C} (X, Y) \longrightarrow \mathcal {D} (F (Y), F (X))
$$

for each pair of objects$X , Y$in$\mathcal { C }$. The rule on morphisms satisfies

$$
F (i d _ {X}) = i d _ {F (X)}
$$

for each object X in$\mathcal { C } _ { : }$, and

$$
F (g \circ f) = F (f) \circ F (g)
$$

for each pair of composable morphisms$f$and$g$in$\mathcal { C }$.

We often simplify notation by writing$f ^ { * }$for$F ( f )$, so that the conditions for contravariant functoriality become$( i d _ { X } ) ^ { * } = i d _ { F ( X ) }$and$( g f ) ^ { * } = f ^ { * } g ^ { * }$

Remark 2.3.9. A functor as in Definition 2.3.1 is sometimes called a covariant functor, to distinguish it from contravariant functors. Sometimes it is more convenient to view a contravariant functor$F$from$\mathcal { C }$to$\mathcal { D }$as a functor$F \colon \mathcal { C }$ $\mathcal { D } ^ { o p }$. The rules and conditions are the same. We may even consider a covariant functor from$\mathcal { C }$to$\mathcal { D }$as a functor$F ^ { o p } \colon \mathcal { C } ^ { o p }  \mathcal { D } ^ { o p }$. This can be useful when considering a composite of covariant and contravariant functors.

Definition 2.3.10 (Corepresented functors). Fix an object$X$in a category $\mathcal { C } .$. We define a (covariant) functor

$$
\mathcal {Y} ^ {X}: \mathcal {C} \longrightarrow \mathbf {S e t}
$$

by taking each object$Y$in$\mathcal { C }$to the set$\mathcal { V } ^ { X } ( Y ) = \mathcal { C } ( X , Y )$of morphisms $f \colon X \to Y$in$\mathcal { C }$, from the fixed object$X$, and taking each morphism$g \colon Y \to Z$ in$\mathcal { C }$to the function

$$
g _ {*} = \mathcal {Y} ^ {X} (g) \colon \mathcal {Y} ^ {X} (Y) = \mathcal {C} (X, Y) \longrightarrow \mathcal {C} (X, Z) = \mathcal {Y} ^ {X} (Z)
$$

that maps$f \colon X \to Y$to the composite$g f \colon X \to Z$

![](images/page_41_image_6.jpg)

We call${ \mathcal { V } } ^ { X }$the set-valued functor corepresented by$X$in$\mathcal { C } .$. It may also be denoted$\mathcal { V } ^ { X } ( - ) = \mathcal { C } ( X , - )$

Definition 2.3.11 (Represented functors). Fix an object Z in a category $\mathcal { C } .$. We define a contravariant functor

$$
\mathcal {Y} _ {Z} \colon \mathcal {C} ^ {o p} \longrightarrow \mathbf {S e t}
$$

by taking each object$Y$in$\mathcal { C }$to the set$\mathcal { V } _ { Z } ( Y ) = \mathcal { C } ( Y , Z )$of morphisms$g \colon Y \to$ $Z$in$\mathcal { C }$, to the fixed object$Z ,$and taking each morphism$f \colon X \to Y$in$\mathcal { C }$to the function

$$
f _ {*} \colon \mathcal {Y} _ {Z} (f) \colon \mathcal {Y} _ {Z} (Y) = \mathcal {C} (Y, Z) \longrightarrow \mathcal {C} (X, Z) = \mathcal {Y} _ {Z} (X)
$$

that maps$g \colon Y \to Z$to the composite$g f \colon X \to Z$

![](images/page_41_image_13.jpg)

We call$\mathcal { V } _ { Z }$the contravariant set-valued functor represented by$Z$in$\mathcal { C }$. It may also be denoted$\mathcal { V } _ { Z } ( - ) = \mathcal { C } ( - , Z )$.

Remark 2.3.12. Functors of the form${ \mathcal { V } } ^ { X }$and$\mathcal { Y } _ { Z }$are called corepresentable and representable, respectively. The contravariant functor$\mathcal { Y } _ { Z }$represented by Z in$\mathcal { C }$is the same as the covariant functor${ \mathcal { P } } ^ { Z }$corepresented by$Z$in the opposite category,$\mathcal { C } ^ { o p }$. [[Forward reference to Yoneda embedding and Yoneda’s lemma.]] [[Example: The n-simplex$\Delta ^ { n }$is the representable functor$\Delta ( - , [ n ] ) \colon \Delta ^ { o p } \ \bar { \to }$ Set.]]

Definition 2.3.13 (Bifunctor). A bifunctor F from$\mathcal { C }$and$\mathcal { C } ^ { \prime }$to$\mathcal { D }$is the same as a functor$F \colon { \mathcal { C } } \times { \mathcal { C } } ^ { \prime } \to { \mathcal { D } }$from the product category of$\mathcal { C }$and$\mathcal { C } ^ { \prime }$to ${ \mathcal { D } } .$It associates to each pair of objects$( X , X ^ { \prime } )$, with X in$\mathcal { C }$and$X ^ { \prime }$in$\mathcal { C } ^ { \prime }$, an object$F ( X , X ^ { \prime } )$in${ \mathcal { D } } .$, and to each pair of morphisms$( f , f ^ { \prime } )$, with$f \colon X \to Y$ in$\mathcal { C }$and$f ^ { \prime } \colon X ^ { \prime } \to Y ^ { \prime }$in$\mathcal { C } ^ { \prime }$, a morphism$F ( f , f ^ { \prime } ) \colon F ( X , X ^ { \prime } ) \to F ( Y , Y ^ { \prime } )$in$\mathcal { D }$ We can write the rule$( f , f ^ { \prime } ) \mapsto F ( f , f ^ { \prime } )$as a function

$$
F \colon \mathcal {C} (X, Y) \times \mathcal {C} ^ {\prime} (X ^ {\prime}, Y ^ {\prime}) \longrightarrow \mathcal {D} (F (X, X ^ {\prime}), F (Y, Y ^ {\prime}))  .
$$

It satisfies

$$
F (i d _ {X}, i d _ {X ^ {\prime}}) = i d _ {F (X, X ^ {\prime})}
$$

for each object X in$\mathcal { C }$and each object$X ^ { \prime }$in$\mathcal { C } ^ { \prime } { } _ { \mathrm { ~ ; ~ } }$, and

$$
F (g \circ f, g ^ {\prime} \circ f ^ {\prime}) = F (g, g ^ {\prime}) \circ F (f, f ^ {\prime})
$$

for each composable pair$f$and$g$in$\mathcal { C }$and each composable pair$f ^ { \prime }$and$g ^ { \prime }$in$\mathcal { C } ^ { \prime }$. In view of the relation

$$
(f, i d _ {Y ^ {\prime}}) \circ (i d _ {X}, f ^ {\prime}) = (f, f ^ {\prime}) = (i d _ {Y}, f ^ {\prime}) \circ (f, i d _ {X ^ {\prime}})
$$

in$\mathcal { C } \times \mathcal { C } ^ { \prime }$it sufices to specify the rule on morphisms in the cases$F ( f , i d _ { X ^ { \prime } } )$ and$F ( i d _ { X } , f ^ { \prime } )$, for all morphisms$f \colon X \to Y$in$\mathcal { C } , f ^ { \prime } \colon X ^ { \prime } \to Y ^ { \prime }$in$\mathcal { C } ^ { \prime }$and all objects X in$\mathcal { C }$and$X ^ { \prime }$in$\mathcal { C } ^ { \prime }$, subject to the condition

$$
F (f, i d _ {Y ^ {\prime}}) \circ F (i d _ {X}, f ^ {\prime}) = F (i d _ {X}, f ^ {\prime}) \circ F (f, i d _ {X ^ {\prime}}).
$$

[[Proof?]]

Example 2.3.14. Let$\mathcal { C }$be any category. We define a bifunctor

$$
\mathcal {C} (-, -) \colon \mathcal {C} ^ {o p} \times \mathcal {C} \to \mathbf {S e t}
$$

by taking each object$( X , X ^ { \prime } )$in${ \mathcal { C } } ^ { o p } \times { \mathcal { C } }$to the set of morphisms$\mathcal { C } ( X , X ^ { \prime } )$ in$\mathcal { C }$. A morphism$( f , f ^ { \prime } ) \colon ( X , X ^ { \prime } ) \to ( Y , Y ^ { \prime } )$in$\mathcal { C } ^ { o p } \times \mathcal { C }$consists of a pair of morphisms$f \colon Y \to X$and$f ^ { \prime } \colon X ^ { \prime } \to Y ^ { \prime }$in C. The rule

$$
f _ {*} ^ {\prime} f ^ {*} = f ^ {*} f _ {*} ^ {\prime} = \mathscr {C} (f, f ^ {\prime}) \colon \mathscr {C} (X, X ^ {\prime}) \to \mathscr {C} (Y, Y ^ {\prime})
$$

maps$g \colon X \to X ^ { \prime }$to the composite$f ^ { \prime } \circ g \circ f \colon Y \to Y ^ { \prime }$

![](images/page_42_image_16.jpg)

In other words, the morphisms sets in a category define a bifunctor to Set, contravariant in the first factor (the source) and covariant in the second factor (the target).

Remark 2.3.15. A functor$\mathcal { C } \sqcup \mathcal { C } ^ { \prime } \to \mathcal { D }$is more-or-less the same as a pair of functors$\mathcal { C } \to \mathcal { D }$and$\mathcal { C } ^ { \prime } \to \mathcal { D }$. Likewise, a functor${ \mathcal { C } } \to { \mathcal { D } } \times { \mathcal { D } } ^ { \prime }$can be identified with a pair of functors$\mathcal { C } \to \mathcal { D }$and$\mathcal { C } \to \mathcal { D } ^ { \prime }$. We do not introduce special terminology for these cases. Functors$\mathcal { C } \to \mathcal { D } \sqcup \mathcal { D } ^ { \prime }$might call for specia terminology, but are rarely needed.

Definition 2.3.16 (Diagonal and fold functors). Let$\mathcal { C }$be any category. The diagonal functor

$$
\Delta \colon \mathcal {C} \longrightarrow \prod_ {i \in I} \mathcal {C}
$$

takes$X$to the family$\Delta ( X ) = ( X _ { i } ) _ { i \in I }$with each$X _ { i } = X$, and$f \colon X \to Y$to the family$\Delta ( f ) = ( f _ { i } ) _ { i \in I }$with each$f _ { i } = f$. The fold functor

$$
\nabla \colon \coprod_ {i \in I} \mathcal {C} \longrightarrow \mathcal {C}
$$

takes$( i , X )$to X and$( i , f ) \colon ( i , X ) \to ( i , Y )$to$f \colon X \to Y$, for each$i \in I .$

## 2.4 Isomorphisms and groupoids

Definition 2.4.1 (Isomorphism). Let$f \colon X \to Y$be a morphism in a category $\mathcal { C } . \mathrm { ~ I f ~ } g \colon Y \to X$satisfies$g \circ f = i d _ { X }$we say that$g$is a left inverse to$f .$If g satisfies$f \circ g = i d _ { Y }$we say that g is a right inverse to$f .$If$g$satisfies both $g \circ f = i d _ { X }$and$f \circ g = i d _ { Y }$, then we say that$f \colon X \to Y$is an isomorphism in$\mathcal { C }$, or that$f$is invertible, and we call$g \colon Y \to X$an inverse to$f .$We often write$f \colon X \xrightarrow { \cong } Y$to indicate that$f$is an isomorphism. If such an isomorphism $f$exists we say that X and Y are isomorphic in$\mathcal { C } .$, and write$X \cong Y$

Lemma 2.4.2. If$f \colon X \to Y$has a left inverse g :$Y  X$and a right inverse $h \colon Y \to X$, then$g \ = \ h$and$f$is an isomorphism. Hence an isomorphism $f \colon X \to Y$has a unique inverse, which we can denote by$f ^ { - 1 } \colon Y \to X$

Proof. If$g \circ f = i d _ { X }$and$f \circ h = i d _ { Y }$then$g = g \circ i d _ { Y } = g \circ ( f \circ h ) = ( g \circ f ) \circ h =$ $i d _ { X } \circ h \ : = \ : h$. Hence$g \ = \ h$is both a left and a right inverse to$f ,$so$f$is invertible.□

Lemma 2.4.3. Each identity morphism in a category is its own inverse,$i d _ { X } ^ { - 1 } =$ $i d _ { X }$, and the composite gf of two composable isomorphisms$f \colon X \to Y$and $g \colon Y \to Z$is an isomorphism, with inverse$( g f ) ^ { - 1 } = f ^ { - 1 } g ^ { - 1 }$. The inverse$f ^ { - 1 }$ of an isomorphism$f \colon X \to Y$is an isomorphism, with inverse$( f ^ { - 1 } ) ^ { - 1 } = { \dot { f } }$

Proof. It is clear that id$_ X \circ i d _ { X } = i d _ { X }$, so id is its own inverse. To see that $f ^ { - 1 } g ^ { - 1 }$is an inverse to$g f .$, we compute$f ^ { - 1 } g ^ { - 1 } ( g f ) = f ^ { - 1 } \circ i d _ { Y } \circ f = f ^ { - 1 } f =$ $i d _ { X }$and$( g f ) f ^ { - 1 } g ^ { - 1 } = g \circ i d _ { Y } \circ g ^ { - 1 } = g g ^ { - 1 } = i d _ { Z }$. The relations$f ^ { - 1 } f = i d _ { X }$ and$f f ^ { - 1 } = i d _ { Y }$exhibiting$f ^ { - 1 }$as an inverse to$f$also exhibit$f$as the inverse to$f ^ { - 1 }$□

Lemma 2.4.4. Let$f \colon X \ \to \ Y$and$g , h \colon Y \to X$be morphisms in$\mathcal { C }$. If $g f \colon X \to X$is an isomorphism, then$( g f ) ^ { - 1 } \circ g \colon Y \to X$is a left inverse to$f .$ $I f f h \colon Y \to Y$is an isomorphism, then$h \circ ( f h ) ^ { - 1 } \colon Y \to X$is a right inverse to $f .$. Hence if gf and$f h$are isomorphisms, then$f$is invertible.

Proof. (gf)<sup>−1</sup>◦g◦f = (gf)<sup>−1</sup>(gf) = id<sub>X</sub> and f ◦h◦(fh)<sup>−1</sup> = (fh)(fh)<sup>−1</sup> = id<sub>Y</sub>, so this is clear.□

Example 2.4.5. Let$f \colon X \to Y$be a morphism in Set, that is, a function. Then$f$admits a left inverse in Set if and only if$f$is injective$( = { \mathrm { o n e - t o - o n e } } )$2 and$f$admits a right inverse if and only if$f$is surjective$( = \mathrm { o n t o } )$. In most cases, these left and right inverses are not unique.$\mathrm { A }$function$f \colon X \to Y$is an isomorphism if and only if it is bijective (= one-to-one and onto).

Example 2.4.6. A morphism$f \colon \mathbf { m }  \mathbf { n }$in$\mathcal { F }$is an isomorphism if and only if it is a bijection. This can only happen if$m = n$, as can be proved by induction on n. A bijection

$$
f \colon \{1, 2, \dots , n \} \xrightarrow {\cong} \{1, 2, \dots , n \}
$$

is also known as a permutation of the set$\mathbf { n } = \{ 1 , 2 , \ldots , n \}$. There are n! such permutations. Let$\Sigma _ { n }$be the symmetric group of such permutations, with group operation given by composition and neutral element given by the identity permutation. In the language of Definition 2.8.11,$\Sigma _ { n }$is the automorphism group of n in$\mathcal { F }$

Exercise 2.4.7. How many injective functions$f \colon \mathbf { m }  \textbf { n }$are there? How many surjective functions$f \colon \mathbf { m }  \mathbf { n }$are there? (The first is easy, the second involves Stirling numbers of the second kind. Later, we shall be interested in the corresponding questions for order-preserving functions.) [[Forward reference.]]

Definition 2.4.8 (Isomorphic categories). We say that two categories$\mathcal { C }$ and$\mathcal { D }$are isomorphic if there exist functors$F \colon \mathcal { C }  \mathcal { D }$and$G \colon { \mathcal { D } } \to { \mathcal { C } }$such that$G \circ F = i d \mathcal { \epsilon }$and$F \circ G = i d _ { \mathcal { D } }$We then say that$F \colon { \mathcal { C } } \ \to \ { \mathcal { D } }$is an isomorphism of categories, and$G \colon { \mathcal { D } }  { \mathcal { C } }$is the inverse isomorphism. If$\mathcal { C }$ and$\mathcal { D }$are small, this is the same as saying that$\mathcal { C }$and$\mathcal { D }$are isomorphic as objects in the category Cat of small categories. Both functors$F$and$G$are then full and faithful, and on objects they induce a bijection between obj(C ) and obj(D).

Definition 2.4.9 (Groupoid). A groupoid is a category in which each morphism is an isomorphism. We write Gpd for the category of small groupoids and functors. It is the full subcategory of Cat generated by the small categories that are groupoids. Hence there is an inclusion functor$\mathbf { G p d } \subset \mathbf { C a t } .$

Definition 2.4.10 (Interior groupoid). Given a category$\mathcal { C } ,$let iso$( \mathcal { C } ) \subseteq$ $\mathcal { C }$be the subcategory with the same objects as$\mathcal { C }$, and with morphism set iso$( { \mathcal { C } } ) ( X , Y )$the subset of${ \mathcal { C } } ( X , Y )$consisting of the morphisms$f \colon X \to Y$ that are isomorphisms in$\mathcal { C } .$. Identity morphisms exist and composition is welldefined in$\operatorname { i s o } ( \mathcal { C } )$, by Lemma 2.4.3. The unit laws and associative law in iso$( \mathcal { C } )$ are inherited from those in$\mathcal { C } .$. Since the inverse of an isomorphism in$\mathcal { C }$is an isomorphism in${ \mathcal { C } } ,$, each morphism in$\operatorname { i s o } ( \mathcal { C } )$has an inverse in iso$( \mathcal { C } )$, so iso$( \mathcal { C } )$ is a groupoid.

Exercise 2.4.11. Let$\mathcal { C }$be a category such that each morphism has a left inverse. Show that$\mathcal { C }$is a groupoid. Similarly if each morphism has a right inverse.

Definition 2.4.12$( \pi _ { 0 }$of groupoid). When$\mathcal { C }$is small, Lemma 2.4.3 shows that isomorphism of objects is an equivalence relation on$\operatorname { o b j } ( { \mathcal { C } } )$. We write

$$
\pi_ {0} (\mathrm{iso} (\mathcal {C})) = \mathrm{obj} (\mathcal {C}) / \cong
$$

for the set of isomorphism classes of objects in$\mathcal { C }$, and denote the isomorphism class of an object$X$by

$$
[ X ] = \left\{Y \in \operatorname{obj} (\mathcal {C}) \mid X \cong Y \right\}.
$$

Example 2.4.13. By Example 2.4.5, iso(Set) is the groupoid of sets and bijective functions. By Example 2.4.6, the groupoid$\operatorname { i s o } ( \mathcal { F } )$has objects n for$n \geq 0 .$2 the morphism set$\mathrm { i s o } ( \mathcal { F } ) ( \mathbf { m } , \mathbf { n } )$is empty for m$\neq n .$, and$\mathrm { i s o } ( \mathcal { F } ) ( \mathbf { n } , \mathbf { n } ) = \Sigma _ { n }$for all$n \geq 0 .$. In particular, is$) ( \mathcal { F } )$is the full subcategory of iso(Set) generated by the objects n for$n \geq 0$

Lemma 2.4.14. iso$( \mathcal { C } ^ { o p } ) = ( \mathrm { i s o } \mathcal { C } ) ^ { o p }$

Proof. This is clear, since the opposite$g ^ { o p }$of a left inverse$g$of$f$is$\mathrm { a }$right inverse of$f ^ { o p }$, and similarly with left and right exchanged.□

Lemma 2.4.15. iso$( { \mathcal { C } } \times { \mathcal { C } } ^ { \prime } ) = \operatorname { i s o } ( { \mathcal { C } } ) \times \operatorname { i s o } ( { \mathcal { C } } ^ { \prime } )$, iso(C ⊔ C<sup>′</sup>) = iso(C) ⊔ iso(C<sup>′</sup>) and similarly for arbitrary set-indexed products and coproducts.

Proof. A family$( g _ { i } ) _ { i \in I }$is inverse in$\Pi _ { i \in I } { \mathcal { C } } _ { i }$to a given family$( f _ { i } ) _ { i \in I }$if and only if$g _ { i }$is inverse to$f _ { i }$for each$i \in I .$. This proves the case of products.$\mathrm { A }$ morphisms$f _ { j }$in$\mathcal { C } _ { j }$is invertible in$\mathcal { C } _ { j }$if and only if it is invertible in$\operatorname { I I } _ { i \in I } { \mathcal { C } } _ { i } .$ This proves the case of coproducts.□

Lemma 2.4.16. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be a functor.$I f f \colon X { \xrightarrow { \cong } } Y$is an isomorphism in${ \mathcal { C } } _ { z }$, then$F ( f ) \colon F ( X ) \ { \stackrel { \cong } { \longrightarrow } } F ( Y )$is an isomorphism in$\mathcal { D }$.

Proof. Let$g \colon Y \to X$be the inverse to$f .$Then$F ( g )$is inverse to$F ( f )$, since $F ( g ) \circ F ( f ) = F ( g \circ f ) = F ( i d _ { X } ) = i d _ { F ( X ) }$and$F ( f ) \circ F ( g ) = F ( f \circ g )$= $F ( i d _ { Y } ) = i d _ { F ( Y ) }$□

Lemma 2.4.17. Any functor$F \colon { \mathcal { D } }  { \mathcal { C } }$from a groupoid$\mathcal { D }$factors uniquely through the inclusion$\epsilon \colon \mathrm { i s o } ( \mathcal { C } ) \subseteq \mathcal { C } _ { }$, so iso$( \mathcal { C } )$is the maximal subgroupoid of $\mathcal { C }$

Proof. For each object X in${ \mathcal { D } } , F ( X )$is an object of$\mathcal { C } _ { : }$, hence also an object of$\operatorname { i s o } ( \mathcal { C } )$. Each morphism$f \colon X \ \to \ Y$in$\mathcal { D }$is an isomorphism, since$\mathcal { D }$is assumed to be a groupoid, so$F ( f )$is an isomorphism in$\mathcal { C }$by Lemma 2.4.16, hence a morphism in iso$( \mathcal { C } )$. Hence$F$factors in a unique way as a composite ${ \mathcal { D } } \to \operatorname { i s o } ( { \mathcal { C } } ) \subseteq { \mathcal { C } }$□

Lemma 2.4.18. The rule iso that takes a small category$\mathcal { C }$to its maximal subgroupoid iso(C) defines a functor

$$
\text { iso:   } \mathbf {C a t} \longrightarrow \mathbf {G p d}  .
$$

The composite functor Gpd ⊂ Cat <sup>iso</sup> −→ Gpd equals the identity.

Proof. We must explain how each functor$F \colon { \mathcal { C } }  { \mathcal { D } }$, which is a morphism in Cat, induces a functor i$\operatorname { s o } ( F ) \colon \operatorname { i s o } ( \mathcal { C } )  \operatorname { i s o } ( \mathcal { D } )$. Each morphism$f \colon X \xrightarrow { \cong }$ Y in$\operatorname { i s o } ( \mathcal { C } )$is an isomorphism in$\mathcal { C } _ { : }$, hence maps to an isomorphism$F ( f )$in$\mathcal { D }$ by Lemma 2.4.16. Hence$F ( f )$is a morphism in iso$( \mathcal { D } )$, which we define to be iso$( F ) ( f )$. It is immediate that iso$( F )$becomes a functor. The last claim is clear.□

Instead of restricting attention to the morphisms in$\mathcal { C }$that are already isomorphisms, one may extend$\mathcal { C }$so as to make all morphisms into isomorphisms, at least if$\mathcal { C }$is small.

Definition 2.4.19 (Localized groupoid). Given a small category${ \mathcal { C } } ,$let $\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$be the groupoid with the same objects as$\mathcal { C } .$, and with morphisms from $X$to$Y$in${ \mathcal { C } } [ { \mathcal { C } } ^ { - 1 } ]$the equivalence classes of chains$( f _ { m } ^ { \epsilon _ { m } } , \ldots , f _ { 1 } ^ { \epsilon _ { 1 } } )$of morphisms in$\mathcal { C } .$

$$
X = Z _ {0} \xleftarrow {f _ {1} ^ {\pm 1}} Z _ {1} \xleftarrow {f _ {2} ^ {\pm 1}} \dots \xleftarrow {f _ {m - 1} ^ {\pm 1}} Z _ {m - 1} \xleftarrow {f _ {m} ^ {\pm 1}} Z _ {m} = Y
$$

where m$\geq 1$and each$\epsilon _ { i } \in \{ \pm 1 \}$, that are composable in the sense that there are objects$Z _ { 0 } , \ldots , Z _ { m }$in$\mathcal { C }$, with$Z _ { 0 } = X , Z _ { m } = Y , f _ { i } \in \mathcal { C } ( Z _ { i - 1 } , Z _ { i } ) \mathrm { ~ i f ~ } \epsilon _ { i } = + 1$ and$f _ { i } \in \mathcal { C } ( Z _ { i } , Z _ { i - 1 } )$if$\epsilon _ { i } = - 1$, subject to the equivalence relation generated by the rules

$$
\begin{array}{l l} (g ^ {+ 1}, f ^ {+ 1}) \sim ((g f) ^ {+ 1}) & (f ^ {- 1}, g ^ {- 1}) \sim ((g f) ^ {- 1}) \\ (f ^ {+ 1}, f ^ {- 1}) \sim (i d ^ {+ 1}) & (f ^ {- 1}, f ^ {+ 1}) \sim (i d ^ {+ 1}), \end{array}
$$

in the sense that$( a , x , b ) \sim ( a , y , b )$for possibly empty words a and$b ,$whenever $x \sim y$

Composition in$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$is given by concatenation. The identity morphism of$X$is$( i d _ { X } ^ { + 1 } )$, and the inverse of$\left( f _ { m } ^ { \epsilon _ { m } } , \ldots , f _ { 1 } ^ { \epsilon _ { 1 } } \right) { \mathrm { i s ~ } } \left( f _ { 1 } ^ { - \epsilon _ { m } } , \ldots , f _ { m } ^ { - \epsilon _ { 1 } } \right)$. There is a functor

$$
\eta \colon \mathcal {C} \to \mathcal {C} [ \mathcal {C} ^ {- 1} ],
$$

which is the identity on objects and takes$f \colon X \to Y ~ \mathrm { t o } ~ ( f ^ { + 1 } )$. We call$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$ the localization of$\dot { \mathcal { C } }$with respect to all morphisms.

Remark 2.4.20. If$\mathcal { C }$is not small, there may be a proper class of diagrams $X \left. Z \right. Y$in$\mathcal { C }$, even if X and$Y$are fixed in advance. Hence the construction above may not provide a (small) set of morphisms from X to$Y$in$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$. If $\mathcal { C }$is small, there is only a set of morphisms in$\mathcal { C } .$, hence only a set of words $( f _ { m } ^ { \epsilon _ { m } } , \ldots , f _ { 1 } ^ { \epsilon _ { 1 } } )$, so$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$becomes an honest category.

Lemma 2.4.21. Any functor F :$\mathcal { C } \to \mathcal { D }$from a small category$\mathcal { C }$to a groupoid $\mathcal { D }$extends uniquely over$\eta \colon { \mathcal { C } } \to { \mathcal { C } } [ { \mathcal { C } } ^ { - 1 } ]$, so$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$is the initial groupoid under$\mathcal { C }$.

Proof. The extension must map$( f _ { m } ^ { \epsilon _ { m } } , \ldots , f _ { 1 } ^ { \epsilon _ { 1 } } )$in$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$to the composite

$$
F (f _ {m}) ^ {\epsilon_ {m}} \circ \dots \circ F (f _ {1}) ^ {\epsilon_ {1}}
$$

in${ \mathcal { D } } ,$, and this is well-defined.

Lemma 2.4.22. The rule L that takes a small category$\mathcal { C }$to the localization $L ( \mathcal { C } ) = \mathcal { C } [ \mathcal { C } ^ { - 1 } ]$defines a functor

$$
L \colon \mathbf {C a t} \longrightarrow \mathbf {G p d}.
$$

The composite functor Gpd$\subset \mathbf { C a t } { \overset { L } { \longrightarrow } } \mathbf { G p d }$is the identity.

Proof. We must explain how each functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$induces a functor

$$
L (F) \colon \mathcal {C} [ \mathcal {C} ^ {- 1} ] \to \mathcal {D} [ \mathcal {D} ^ {- 1} ].
$$

On objects,$L ( F )$takes$X$to$F ( X )$. On morphisms,$L ( F )$takes$( f _ { m } ^ { \epsilon _ { m } } , \ldots , f _ { 1 } ^ { \epsilon _ { 1 } } )$ in${ \mathcal { C } } [ { \bar { \mathcal { C } } } ^ { - 1 } ]$to$( F ( f _ { m } ) ^ { \epsilon _ { m } } , \ldots , F ( f _ { 1 } ) ^ { \epsilon _ { 1 } } )$in$\mathcal { D } [ \mathcal { D } ^ { - 1 } ]$□

## 2.5 Ubiquity

Practically all sorts of mathematical objects naturally occur as the objects of a category. Here are some common examples.

Definition 2.5.1 (Groups). Let Grp be the category of groups and group homomorphisms. Its object class obj(Grp) is the proper class of all groups. We write general groups multiplicatively, with neutral element e. For each pair of groups$G , H$, the morphism set$\mathbf { G r p } ( G , H )$is the set of group homomorphisms $f \colon G \to H$, i.e., the functions$f \colon G \to H$such that$f ( x y ) = f ( x ) f ( y )$for all x, $y \in G .$. It follows formally that$f ( e ) = e$and$f ( x ^ { - 1 } ) = f ( x ) ^ { - 1 }$. The identity function$i d _ { G } \colon G \to G$is a group homomorphism, and the composite of two group homomorphisms$f \colon G \to H$and$g \colon H  K$is a group homomorphism $g f \colon G \to K$, since$( g f ) ( x y ) = g ( f ( x y ) ) = g ( f ( x ) f ( y ) ) = g ( f ( x ) ) g ( f ( y ) ) =$ $( g f ) ( x ) ( g f ) ( y )$. The unit and associative laws hold as in Set, so Grp is a category. An isomorphism of groups has the usual meaning.

Definition 2.5.2 (Abelian groups). Let Ab be the category of abelian groups and group homomorphisms. This is the full subcategory of Grp generated by the proper class of all abelian groups. We usually write abelian groups additively, with neutral element 0. For each pair of abelian groups$A , B$, the morphism set$\mathbf { A b } ( A , B )$is the set of group homomorphisms$f \colon A \to B ,$i.e., the functions$f \colon A \to B$such that$f ( x + y ) = f ( x ) + f ( y )$for all$x , y \in A$. It follows formally that$f ( 0 ) = 0$and$f ( - x ) = - f ( x )$. An isomorphism of abelian groups has the usual meaning.

Remark 2.5.3. In this case, the morphism set$\mathbf { A } \mathbf { b } ( A , B ) = \mathrm { H o m } ( A , B )$is wellknown to have the additional structure of an abelian group. For example, the sum$f + g$of two group homomorphisms$f , g \colon A  B$is given by the formula $( f + g ) ( x ) = f ( x ) + g ( x )$for all$x \in A$. However, this abelian group structure is not part of the data when we say that Ab is a category. Categories with this kind of additional structure are called additive categories, or Ab-categories. [[Reference to the chapter on abelian and exact categories.]]

Example 2.5.4. Let$\mathbb { Z } / n$be the cyclic group of order n. For each abelian group $B ,$the abelian group${ \mathrm { H o m } } ( \mathbb { Z } / n , B )$of group homomorphisms$f \colon \mathbb { Z } / n \to B$can be identified with the subgroup$B [ n ] = \{ x \in B \mid n x = 0 \}$of elements of order dividing n in B. The rule$B \mapsto B [ n ]$defines a covariant functor$\mathbf { A b } \to \mathbf { A b } .$ which is corepresented by the object$\mathbb { Z } / n$in$\mathbf { A b } .$, viewed as an additive category.

Example 2.5.5. Let$\mathbb { T } = U ( 1 )$be the multiplicative group of complex numbers of absolute value 1. For each group A, the abelian group$A ^ { \# } = \operatorname { H o m } ( A , \mathbb { T } )$of group homomorphisms$f \colon A \to \mathbb { T }$is called the character group, or the Pontryagin dual of A. The rule$A \mapsto A ^ { \# }$defines a contravariant functor$\mathbf { A } \mathbf { b } ^ { o p }  \mathbf { A b } .$ which is represented by the object T in Ab, viewed as an additive category. There is a natural homomorphism$A  ( A ^ { \# } ) ^ { \# }$, which is an isomorphism for all finite groups A. [[Better to discuss Pontryagin duality theorem in the additive topological setting, between discrete abelian groups and compact Hausdorf abelian groups.]]

Definition 2.5.6 (Abelianization). Given a group G, the commutator subgroup$[ G , G ] \subseteq G$is the subgroup generated by the set of commutators$[ g , h ] =$ $g h g ^ { - 1 } h ^ { - 1 } \in G$, for all$g , h \in G$. In other words, the elements of$[ G , G ]$are all finite products of commutators in G. This is a normal subgroup, since $k [ g , h ] k ^ { - 1 } = [ k g k ^ { - 1 } , k h k ^ { - 1 } ]$is a commutator for all$k \in G$. The quotient group

$$
G ^ {a b} = G / [ G, G ]
$$

is called the abelianization of G. It is an abelian group, since$[ g ] [ h ] [ g ] ^ { - 1 } [ h ] ^ { - 1 } =$ $[ g h g ^ { - 1 } h ^ { - 1 } ] = e$is the neutral element in$G ^ { a b }$for any$g , h \in G$which implies $[ g ] [ h ] = [ h ] [ g ]$. Here$[ g ]$denotes the coset of$g _ { \mathrm { : } }$which is the image of$g \in G$under the canonical homomorphism$G \to G ^ { a b }$. Any group homomorphism$f \colon G \to A$ to an abelian group A factors uniquely through this canonical homomorphism, since$f ( [ g , h ] ) = 0$for any commutator.

Lemma 2.5.7. The rule taking G to$G ^ { a b }$defines a functor

$$
(-) ^ {a b} \colon \mathbf {G r p} \longrightarrow \mathbf {A b}.
$$

The composite functor Ab$\subset \mathbf { G r p } \stackrel { ( - ) ^ { g p } } { \longrightarrow }$Ab is the identity.

[[Discuss as adjunction later. Abelianization is left adjoint to the full embedding. The isomorphism$H _ { 1 } ^ { g p } ( G ) \cong G ^ { a b }$is generalized by Quillen [53], defining homology as left derived functors of abelianization, where abelianization is left adjoint to a forgetful functor from abelian group objects. The full embedding does not respect coproducts, hence has no right adjoint.]]

Proof. A homomorphism$f \colon G \to H$takes$[ G , G ]$into$[ H , H ]$, since$f ( [ g , h ] ) =$ $[ f ( g ) , f ( h ) ]$, hence induces a homomorphism$f ^ { a b } \colon G ^ { a b } \to H ^ { a b }$. Functoriality is easily verified. If G is already abelian,$[ G , G ] = \{ e \}$and we will identify $G ^ { a b } = { \cal { \dot { G } } } / \{ e \}$with G.□

Remark 2.5.8. For a related example of something that is not a functor, consider the rule taking a group G to its center

$$
Z (G) = \left\{g \in G \mid g h = h g \text {   for   all   } h \in G \right\}.
$$

This is a well-defined abelian group, and the group inclusion$Z ( G ) \subseteq G$is such that every group homomorphism$A  G$from an abelian group factors uniquely through$Z ( G )$. Still,$Z$is not a functor, since for a group homomorphism$f \colon G \to$ H there is not necessarily an induced homomorphism$Z ( f ) \colon Z ( G ) \to Z ( H )$. For example, with$G = \Sigma _ { 2 } , H = \Sigma _ { 3 }$and$f \colon \Sigma _ { 2 }  \Sigma _ { 3 }$the usual inclusion,$Z ( G ) = G$ while$Z ( H ) \cong \mathbb { Z } / 3$is generated by the cyclic permutation (123). Since$f$admits a left inverse the induced homomorphism$Z ( f ) \colon Z ( G ) \ \to \ Z ( H )$) should also admit a left inverse. But the only homomorphism$Z ( G ) \to Z ( H )$is the trivial one.

Example 2.5.9. For a group$G ,$the set of homomorphisms$G ^ { \# } = \mathbf { G r p } ( G , \mathbb { T } )$ forms an abelian group, under pointwise multiplication. Since any commutator in$G$must map to 1 under such a homomorphism, the projection$G  G ^ { a b }$ induces an isomorphism$( G ^ { a b } ) ^ { \# } \cong G ^ { \# }$. Hence, for each finite group$G , ( G ^ { \# } ) ^ { \# } \cong$ $G ^ { a b }$. To study non-abelian groups$G ,$, one can instead consider the category of unitary G-representations, or equivalently, the group homomorphisms$\rho \colon G \to$ $U ( n )$for varying$n \geq 1$, and then attempt to recover G from that category. See Section 3.3 for more about this.

Example 2.5.10. Let Top be the category of topological spaces and continuous functions. The morphism set$\mathbf { T o p } ( X , Y )$between two topological spaces X and $Y$is the set of continuous functions$f \colon X \to Y$. Recall that a function$f \colon X \to Y$ is continuous if$f ^ { - 1 } ( U ) = \{ x \in X \mid f ( x ) \in U \}$is open in X for each open subset$U \subseteq Y$. Continuous functions are usually called maps, and the elements $x \in X$in a topological space are usually called points. The identity function $i d _ { X }$is continuous, and the composite of two continuous functions$f \colon X \to Y$ and$g \colon Y \to Z$is continuous, since$g ^ { - 1 } ( V )$is open in$Y$, and$( g f ) ^ { - 1 } ( V ) =$ $f ^ { - 1 } ( g ^ { - 1 } ( V ) )$is open in X, for each open subset$V \subseteq Z$. The unit and associative laws hold as in Set, so Top is a category.

Remark 2.5.11. We might identify Set with the full subcategory of Top generated by the discrete topological spaces, since any function$f \colon X \to Y$is continuous when$X$(and$Y )$is given the discrete topology. In the language of Definition 2.4.8, Set is isomorphic to this full subcategory. For general topological spaces$X$and$Y$we might give the set$\mathbf { T o p } ( X , Y ) = \mathrm { M a p } ( X , Y )$a topology, for instance the compact–open topology. Under mild assumptions on Y , like local compactness, the composition Top$( Y , Z ) \times \mathbf { T o p } ( X , Y ) \to \mathbf { T o p } ( X , Z )$is then a continuous map, and we obtain a topological category. Since some assumptions are needed, we postpone the details to a later section. [[Forward reference.]]

Example 2.5.12. Let$S ^ { 1 }$be the circle. Given any space X the continuous maps$f \colon S ^ { 1 } \to X$are called free loops in X. When the set$\mathbf { T o p } ( S ^ { 1 } , X )$of free loops is given the compact–open topology, we call it the free loop space ${ \mathcal { L } } X = \mathrm { M a p } ( S ^ { 1 }$, X) of$X$. It can, for instance, be considered as the space of closed strings in X.

Definition 2.5.13 (Path components). Let$I \ = \ [ 0 , 1 ] \ \subset \ \mathbb { R }$be the unit interval on the real line, and let$X$be any topological space. A map α:$I \to X$ is called a path in$X ,$, from$\alpha ( 0 )$to$\alpha ( 1 )$. We say that two points$x , y \in X$are in the same path component of$X$, and write$x \simeq y .$, if there exists a path α in X from x to y. This defines an equivalence relation on the set of points in X, as we will verify in a moment. The set of equivalence classes for this relation will be called the set of path components of X, and is denoted

$$
\pi_ {0} (X) = X / \simeq .
$$

It remains to verify that ≃ is an equivalence relation on X. The constant path $\alpha ( s ) = x$for all$s \in I$shows that$x \simeq x$. If α is a path from x to y, so that $x \simeq y .$, then there is a path ¯α from y to x given by the formula$\bar { \alpha } ( s ) = \alpha ( 1 - s )$ for all$s \in I .$, so that$y \simeq x$. If α is a path from x to$y ,$and$\beta$is a path from y to z, so that$x \simeq y$and$y \simeq z$, then there is a path$\alpha * \beta$from x to z, given by

$$
(\alpha * \beta) (s) = \left\{ \begin{array}{l l} \alpha (2 s) & \text {for 0\leq s\leq 1 / 2}, \\ \beta (2 s - 1) & \text {for 1 / 2\leq s\leq 1}, \end{array} \right.
$$

so that$x \simeq z$. [[Should we write$\alpha * \beta$or$\beta$∗ α for this?]]

Lemma 2.5.14. The rule taking X to$\pi _ { 0 } ( X )$defines a functor

$$
\pi_ {0} \colon \mathbf {T o p} \longrightarrow \mathbf {S e t}.
$$

The composite functor Set$\subset \mathbf { T o p } \ { \xrightarrow { \pi _ { 0 } } }$Set is the identity.

[[Mention later that$\pi _ { 0 }$is left adjoint to the inclusion for reasonable (locally path-connected) X.]]

Proof. A continuous map$f \colon X \to Y$takes each path component of X into a path component of$Y$, since if$\alpha \colon I  X$is a path from x to y in X, so that $x \simeq y ,$then the composite$f \circ \alpha \colon I \to Y$is a path from$f ( x )$to$f ( y )$in$Y .$, so that$f ( x ) \simeq f ( y )$. Hence

$$
\pi_ {0} (f) \colon \pi_ {0} (X) \longrightarrow \pi_ {0} (Y)
$$

is well-defined by taking [x] to$[ f ( x ) ]$, where$[ x ] \in \pi _ { 0 } ( X )$denotes the equivalence class (= path component) of x under$\simeq$Functoriality is easily verified.□

## 2.6 Correspondences

Example 2.6.1. Given two sets X, Y, a correspondence C from X to Y is a subset$C \subseteq X \times Y$. We can think of$C$as a multi-valued function from$X$to ${ \cal Y } ,$whose values at x$\in \ X$is the set of$y \in Y$such that$( x , y ) \in C$. Let Cor be the category of sets and correspondences. Its objects are sets, so$\mathrm { \ o { o b j } ( C o r ) }$ is the class of all sets. For each pair of sets$X , ~ Y$, Cor$( X , Y )$is the set of correspondences from X to$Y , { \mathrm { i . e . } }$, the set of all subsets of$X \times Y$. The identity correspondence from X to X is the diagonal subset$\Delta ( X ) = \{ ( x , x ) \mid x \in X \}$of $X \times X$. Given sets$X , Y , Z$and correspondences$C \subseteq X \times Y$and$D \subseteq Y \times Z$, we define the composite correspondence$D \circ C \subseteq X \times Z$as the set of$( x , z ) \in X \times Z$ such that there exists at least one$y \in Y$with$( x , y ) \in C$and$( y , z ) \in D$. The unit and associative laws are easy to verify, so Cor is a category.

Remark 2.6.2. The last example shows that the morphisms in a category do not need to have preferred underlying functions. Similarly, there is no requirement that the objects of a category have preferred underlying sets. This example is also a little unusual in that we have chosen to label the category Cor by the name for its morphisms, rather than its objects. In many cases it is clear what the intended morphisms are once the objects are described, in which case it makes sense to refer to the category primarily by its objects. In other cases, where it is the morphisms that are unobvious, it seems sensible to emphasize them in the notation.

[[Define a concrete category.]]

Example 2.6.3. The opposite$\mathbf { C o r } ^ { o p }$of the category of correspondences can be identified with Cor itself, so this category is self-dual. The identification is the identity on objects, and for sets$X , Y$we identify$\mathbf { C o r } ( X , Y )$with

$$
\mathbf {C o r} ^ {o p} (X, Y) = \mathbf {C o r} (Y, X)
$$

by taking a correspondence$C \subseteq X \times Y$to the correspondence$\gamma C \subseteq Y \times X$2 where

$$
\gamma C = \{(y, x) \in Y \times X \mid (x, y) \in C \}.
$$

More precisely, this defines an isomorphism of categories$\gamma \mathrm { i }$: Cor$\cong \mathbf { C o r } ^ { o p }$, in the sense of Definition 2.4.8, since for$D \subseteq Y \times Z$the composite$D \circ C \subseteq X \times Z$ in Cor corresponds to$\gamma ( D \circ C ) = \gamma D \circ ^ { o p } \gamma C$in$\mathbf { C o r } ^ { o p }$

Example 2.6.4. Let$G \colon \mathbf { S e t } \ \to$Cor be the functor that is the identity on objects, so that$G ( X ) = X$for all sets X, and takes each function$f \colon X \to Y$ to its graph

$$
G (f) = \{(x, f (x)) \mid x \in X \} \subseteq X \times Y
$$

considered as a correspondence from X to Y. The rule$f \mapsto G ( f )$defines a function$\mathbf { S e t } ( X , Y ) \to \mathbf { C o r } ( X , Y )$for all sets$X , Y$. The graph of the identity function$i d _ { X } \colon X \to X$is the diagonal subset$G ( i d _ { X } ) = \Delta ( X ) \subseteq X \times X$, so G takes identities to identities. For G to be a functor, we must also check that G takes composites in Set to composites in Cor. Thus consider functions $f \colon X \to Y$and$g \colon Y \to Z$. The composite correspondence$G ( g ) \circ G ( f )$consists of the$( x , z ) \in X \times Z$such that there exists a$y \in Y$with$( x , y ) \in G ( f )$and $( y , z ) \in G ( g )$. Since$G ( f )$is the graph of the function$f ,$the only y satisfying the first condition is$y = f ( x )$. Then the only z satisfying the second condition is$z = g ( y ) = ( g \circ f ) ( x )$. Hence

$$
G (g) \circ G (f) = \{(x, z) \mid z = (g \circ f) (x) \} = G (g \circ f),
$$

and$G$is, indeed, a functor.

Example 2.6.5. The functor$G \colon \mathbf { S e t } \to \mathbf { C o r }$is faithful, since for every pair$X$ $Y$of sets the function

$$
G \colon \operatorname{Set} (X, Y) \longrightarrow \operatorname{Cor} (X, Y)
$$

is injective. A function$f \colon X \to Y$is after all determined by its graph. For most pairs$X , Y$there are more correspondences than functions between X and$Y _ { i \textrm { \scriptsize { F } } i }$, so G is not full.

Example 2.6.6. Let$\mathcal { C } \subset \mathbf { C o r }$be the subcategory of correspondences with all sets as objects, but with morphisms${ \mathcal { C } } ( X , Y )$only the correspondences$C \subseteq$ $X \times Y$that are graphs of functions, i.e., those having the property that for each $x \in X$there is one and only one$y \in Y$with$( x , y ) \in C .$The graph functor from Example 2.6.4 factors uniquely through$\mathcal { C }$, and induces an isomorphism of categories Set$\cong \mathcal { C }$

Remark 2.6.7. This example presumes that we think of a function$f \colon X \to Y$ as a rule that associates to each element$x \in X$a unique element$f ( x )$in$Y ,$ and that this is not exactly the same as the graph subset$G ( f ) \subseteq X \times Y$. If the reader prefers to define functions as graphs, then the isomorphism Set$\cong \mathcal { C }$ is an equality, and Set is a subcategory of Cor.

## 2.7 Representations of groups and rings

Definition 2.7.1 (G-sets). Let$G$be a group with neutral element$e . \mathrm { ~ A ~ } ( l e f t )$ G-set is a set X with a left action map

$$
G \times X \longrightarrow X
$$

taking$( g , x )$to$g \cdot x ,$such that$e \cdot x = x$and$g \cdot ( h \cdot x ) = g h \cdot x$for all$g , h \in G$4 $x \in X$. We often abbreviate$g \cdot x$to gx. A function$f \colon X \to Y$between two left G-sets is said to be G-equivariant if$g f ( x ) = f ( g x )$for all$g \in G , x \in X$

Definition 2.7.2 (Category$G \mathrm { - } \mathbf { S } \mathbf { e } \mathbf { t } )$. Let G−Set be the category of all (left) G-sets and G-equivariant functions. Each identity function is G-equivariant, and the composite of two G-equivariant functions is G-equivariant, so this defines a category. Let G−Fin be the full subcategory of G−Set generated by all finite G-sets, i.e., G-sets X such that X is a finite set.

Definition 2.7.3 (Orbits and fixed points). Let X be a G-set, and let $x \in X$. The orbit of x is the G-subset

$$
G x = \{g x \in X \mid g \in G \}
$$

of X, and the stabilizer group of x is the subgroup

$$
G _ {x} = \{g \in G \mid g x = x \}
$$

of X. We say that the G-action on X is transitive if$G x = X$for some (hence all)$x \in X$. We say that the G-action is free if$g x = x$only for$g = e$, so that the stabilizer group$G _ { x } = \{ e \}$is trivial for each$x \in X$. The G-action is trivial if$g x = x$for all$g \in G$and$x \in X$, so each stabilizer group$G _ { x } = G$equals the whole group. The orbit set$X / G = \{ G x \mid x \in X \}$is the set of orbits, and the fixed point set$X ^ { G } = \{ x \in X \mid G _ { x } = { \bar { G } } \}$is the set of x with$g x = x$for all$g .$

Lemma 2.7.4. Any G-set X decomposes as the disjoint sum of its orbits

$$
X \cong \coprod_ {x} G x
$$

where x ranges over one element in each orbit. Each orbit is a transitive$G \mathrm { - } s e t ,$ and there is an isomorphism

$$
G / G _ {x} \stackrel {\cong} {\longrightarrow} G x
$$

of G-sets taking the coset$g G _ { x }$to the element gx. Each G-set is therefore of the form

$$
X \cong \coprod_ {i \in I} G / H _ {i}
$$

where$H _ { i }$is a subgroup of G for each$i \in I$

Lemma 2.7.5. The G-equivariant functions$f \colon G / H \to G / K$can be uniquely written in the form$f ( g H ) = g w K$for an element w$K \in ( G / K ) ^ { H }$, [[Make $( G / K ) ^ { H }$explicit.]] Each G-equivariant function

$$
f \colon \coprod_ {i \in I} G / H _ {i} \longrightarrow \coprod_ {j \in J} G / K _ {j}
$$

has the form

$$
f (g H _ {i}) = g w _ {i} K _ {\phi (i)}
$$

for a unique function$\phi \colon I  J$and uniquely determined family of elements w$K _ { j } \in ( \bar { G } / \bar { K _ { j } } ) ^ { H _ { i } }$, with$j = \phi ( i )$

[[Discuss orbit category$\mathbf { O r } ( G )$of transitive G-sets$G / H$for$H \subseteq G ,$as a full subcategory of G−Set.]]

[[Discuss the isomorphism classes of G−Set or G−Fin. Decompose G-sets into orbits$G / H$, classified by the conjugacy class (H) of H in G. Form a skeleton category$G - \mathcal { F }$with objects$\mathrm { L I } _ { ( H ) } \mathrm { L I } ^ { \bar { n _ { H } } } \bar { G } / H$for some (class) function n from conjugacy classes of subgroups to${ \mathbb { N } } _ { 0 }$. Give criterion for finiteness. Specialize to G finite. Alternatively, consider group homomorphisms$G  \Sigma _ { n }$, which correspond to G-actions on n. These are permutation representations of$G .$ Conjugate group homomorphisms give isomorphic G-sets.]]

[[Categories of left and right R-modules, R−Mod and Mod−R, for R a ring. The full subcategory R−Coh of coherent = finitely generated R-modules for R left Noetherian, or the full subcategory R−Proj of finitely generated projective R-modules.]]

[[Exactness of Hom$\mathbf { \sigma } _ { \cdot R } ( - , - )$, projective and injective R-modules. Exactness of$( - ) \otimes _ { R } ( - )$, left and right flat R-modules.]]

[[Discuss the isomorphism classes of R−Mod or its various full subcategories.]]

[[Example: Let R be a commutative ring. Define$D \colon ( R - \mathbf { M o d } ) ^ { o p }  R -$ Mod by$D ( M ) = ( R - \mathbf { M o d } ) ( M , R ) . ] .$]

## 2.8 Few objects

To get more easily comprehended examples of categories, we may restrict the number of objects in a couple of ways. We have already discussed small categories, where obj(C ) is a set. Here is a mild condition on a category, already mentioned in the definition of$\mathcal { F }$

Definition 2.8.1 (Skeletal category). A category$\mathcal { C }$is skeletal if each isomorphism class of objects only contains one element, i.e., if$X \cong Y$in$\mathcal { C }$implies $X = Y$. Let SkCat be the full subcategory of Cat generated by the small skeletal categories, and let SkGpd be the full subcategory generated by the small skeletal groupoids.

A more drastic restriction is to only allow one object, altogether.

Definition 2.8.2 (Monoids). A monoid M is a set with a unit element$e \in M$ and a multiplication$\mu \colon M \times M \to M$, taking$( x , y )$to xy, satisfying the unit laws $e x = x = x e$and the associative law$( x y ) z = x ( y z )$. A monoid homomorphism $f \colon M \to N$is a function satisfying$f ( e ) = e$and$f ( x y ) = f ( x ) f ( y )$. Let Mon be the category of all (small) monoids and monoid homomorphisms.

Example 2.8.3. Let$\mathcal { C }$be a category with a single object ∗, so that$\operatorname { o b j } ( \mathcal { C } ) =$ $\{ * \}$. The only pair of objects in$\mathcal { C }$is then$* , * ,$and the only morphism set in$\mathcal { C }$is $M = \mathcal { C } ( * , * )$. The identity morphism of ∗ specifies an element$e = i d _ { * } \in M .$, and the composition law for the triple$^ { * , * , }$, ∗ of objects is a function$\mu \colon M \times M \to M .$ which we write as taking$( g , f )$to$g f$. The unit laws and associative law for$\mathcal { C }$ tell us that M is a monoid.

$\operatorname { L e t } \mathcal { C } , \mathcal { D }$be categories with${ \mathrm { o b j } } ( { \mathcal { C } } ) = { \mathrm { o b j } } ( { \mathcal { D } } ) = \{ * \}$, and let$M = \mathcal { C } ( * , * )$ $N = \mathcal { D } ( * , * )$be the corresponding monoids. A functor$F \colon \mathcal { C }  \mathcal { D }$defines a function$F \colon M = \mathcal { C } ( * , * )  \mathcal { D } ( * , * ) = N$, such that$F ( e ) = e$and$F ( g f ) =$ $F ( g ) F ( f )$, for all$f , g \in M$. Hence$F$is a monoid homomorphism. The functor $F \colon { \mathcal { C } } \to { \mathcal { D } }$is an isomorphism of categories if and only if$F \colon M \to N$is a monoid isomorphism.

Definition 2.8.4 (Category${ \mathcal { B } } M )$. Given any monoid$( M , e , \mu )$, let$\mathcal { B } M$be the category with one object ∗ and morphism set$\mathcal { B } M ( \ast , \ast ) = M$. The neutral element e and multiplication$\mu$specify the identity morphism id and composition law$^ { \circ , }$which make$\mathcal { C }$a category.

Each monoid homomorphism$f \colon M \to N$specifies a functor$\mathcal { B } f \colon \mathcal { B } M \to$ $\mathcal { B } N$, taking ∗ to ∗ and mapping$M = { \mathcal { B } } M ( * , * ) \to { \mathcal { B } } N ( * , * ) = N$by$f .$which is an isomorphism of categories if and only if$f$is a monoid isomorphism.

[[Consider writing [x] for the morphism in BM corresponding to$x \in M . ] ]$

Lemma 2.8.5. The rule taking a monoid M to the category$\mathcal { B } M$defines a full and faithful functor

$$
\mathscr {B} \colon \operatorname{Mon} \longrightarrow \operatorname{Cat}.
$$

It induces an equivalence between Mon and the full subcategory of Cat generated by categories with one object.

Proof. [[Clear. Forward reference to equivalence of categories.]]

Turning the tables, we may say that a category is a monoid with (potentially) many objects.

Lemma 2.8.6. Let$( M , e , \mu )$be a monoid. Then$\mathcal { B } ( M ^ { o p } ) = ( \mathcal { B } M ) ^ { o p }$, where $( M ^ { o p } , e , \mu ^ { o p } )$is the opposite monoid with multiplication$\mu ^ { o p } ( f , g ) = \mu ( g , f )$

Lemma 2.8.7. The homomorphisms$M \gets M { \times } N \to N$induce an identification

$$
\mathcal {B} (M \times N) \stackrel {=} {\longrightarrow} \mathcal {B} M \times \mathcal {B} N
$$

that views a morphism$( x , y )$on the left hand side as a pair of morphisms x and y on the right hand side.

[[Both proofs are trivial.]]

Example 2.8.8. Let$\mathcal { C }$be a groupoid with a single object$^ * { } { \cdot }$so that$\operatorname { o b j } ( \mathcal { C } ) =$ $\{ * \}$. The only morphism set in$\mathcal { C }$is$G = \mathcal { C } ( * , * )$, which we have already seen is a monoid. Furthermore, the assumption that$\mathcal { C }$is a groupoid means that each element$f \in G$admits an inverse$f ^ { - 1 }$with respect to the multiplication, so that $( G , e , \mu )$is in fact a group. For$f$can be viewed as a morphism$f \colon \ast  \ast$in the groupoid$\mathcal { C }$, hence an isomorphism, and the inverse$f ^ { - 1 } \colon * \to *$with respect to composition will then correspond to a group inverse in G.

Let$\mathcal { C } , \mathcal { D }$be groupoids with$\mathrm { o b j } ( { \mathcal C } ) = \mathrm { o b j } ( { \mathcal D } ) = \{ * \}$, and let$G = \mathcal { C } ( * , * )$), $H = \mathcal { D } ( * , * )$be the corresponding groups. A functor$F \colon { \mathcal { C } }  { \mathcal { D } }$defines a function$F \colon G \to H$, such that$F ( e ) = e$and$F ( g f ) = F ( g ) F ( f )$, for all$f ,$ $g \in G$. Hence$F$is a group homomorphism. The functor$F \colon \mathcal { C }  \mathcal { D }$is an isomorphism of groupoids if and only if$F \colon G \to H$is a group isomorphism.

Lemma 2.8.9. The rule taking a group G to the groupoid BG defines a full and faithful functor

$$
\mathscr {B} \colon \operatorname{Grp} \longrightarrow \operatorname{Gpd}.
$$

It induces an equivalence between Grp and the$f u l l$subcategory of Gpd generated by groupoids with one object.□

Proof. The thing to check is that BG is a groupoid, but each morphism$f \in$ $\mathcal { B } G ( * , * ) = G$has an inverse, precisely because G is a group.□

Reversing the perspective again, a groupoid is a group with many objects. We will explain the notation$\mathcal { B } G$later [[when?]], in relation to the classifying space$B G = | \mathcal { B } G |$of the group G.

Remark 2.8.10. We can organize these full subcategories of Cat in the following diagram:

![](images/page_55_image_3.jpg)

(2.1)

In the upper row all morphisms are isomorphisms, in the left hand column we have only one object, and in the middle column each isomorphism class contains only one object. See also diagram (2.2) below.

Definition 2.8.11 (Endomorphisms and automorphisms). A morphism $f \colon X \to X$in a category$\mathcal { C }$, with the same source and target, is called an endomorphism. I$\operatorname { f } f : X { \xrightarrow { \cong } } X$is also an isomorphism, it is called an automorphism. The identity morphism$i d _ { X }$, together with the composition of morphisms in$\mathcal { C } ,$ makes the set$M = \mathcal { C } ( X , X )$of endomorphisms of X into a monoid, called the endomorphism monoid of X in$\mathcal { C } .$. The same data, together with the existence of inverses, makes the set$G = \operatorname { i s o } ( { \mathcal { C } } ) ( X , X )$of automorphisms of X into a group, called the automorphism group of X in$\mathcal { C } .$. With this notation,$G = M ^ { \times }$ is the maximal submonoid of M that is a group, or equivalently, the maximal subgroup of$M ,$also known as the group of units in M.

Example 2.8.12. The full subcategory generated by a single object X in a category$\mathcal { C }$is isomorphic to the one-object category BM associated to the endomorphism monoid$M = \mathcal { C } ( X , X )$of$X$

Remark 2.8.13. The commutativity relation$g \circ f = f \circ g$only makes sense for morphisms$f , g$in a category$\mathcal { C }$when$f$and$g$are both endomorphisms of the same object. Is there a useful notion of a commutative monoid with many objects, or an abelian group with many objects?

From one point of view, a commutative monoid is a monoid object in Mon, i.e., a monoid M such that the multiplication map$\mu \colon M \times M \to M$is a monoid homomorphism. Here$M \times M$denotes the product monoid.

The many objects version of this is then to consider category objects in Cat, i.e., a pair of small categories$\mathcal { O }$and$\mathcal { M }$, with identity, source and target functors id :$\theta  \mathcal { M } , s \colon \mathcal { M }  \theta$and t:${ \mathcal { M } } \to { \mathcal { O } } ,$and a composition functor$\circ \colon \mathcal { M } \times \sigma$ $\mathcal { M }  \mathcal { M }$from the fiber product category$\mathcal { M } \times _ { \mathcal { O } } \mathcal { M }$, satisfying the unit and associativity laws. This structure is called a bicategory. See [67, §5] for more details. [[Discuss horizontal and vertical morphisms, and how they commute.]]

[[Give left adjoint functor Cat → Mon or$\mathbf { G p d } \ \to \ \mathbf { G r p } ?$To a small skeletal category$\mathcal { C }$we associate the monoid consisting of finite words of non-composable morphisms$( f _ { n } , \ldots , f _ { 1 } )$in$\mathcal { C } .$, with$n \geq 0$. The empty word$( )$is the neutral element. The product of$( g _ { m } , \ldots , g _ { 1 } )$and$( f _ { n } , \ldots , f _ { 1 } )$is the result of reducing$( g _ { m } , \ldots , g _ { 1 } , f _ { n } , \ldots , f _ { 1 } )$by composing all composables. If$\mathcal { C }$is a small skeletal groupoid, this produces a group. What happens if$\mathcal { C }$is not skeletal?]]

## 2.9 Few morphisms

In an orthogonal direction to that of the last section, we may instead restrict the number of morphisms between any two objects X and Y in a category, allowing only zero or one such morphism. What remains is one bit of information (true or false) about whether such a morphism exists or not, which amounts to a binary relation on the object class or set.

Definition 2.9.1 (Relations). A relation R on a set$P$is a subset$R \subseteq P \times P$ For elements$x , y \in P$we say that xRy is true if and only if$( x , y ) \in R$

Definition 2.9.2 (Orderings and relations). Let$P$be a set.

(a) A preordering (= quasi-ordering) on$P$is a relation$\leq$such that

$x \leq x$for all$x \in P ,$and

$( x \leq y$and$y \le z )$implies$x \leq z$for all x,$y , z \in P .$

The pair$( P , { \leq } )$is called a preorder.

(b) A partial ordering is a preordering$\leq$such that

$( x \leq y$and$y \leq x )$implies$x = y$for all$x , y \in P .$

The pair$( P , { \leq } )$is then called a partially ordered set, or a poset.

(c) A total ordering is a partial ordering$\leq$such that

$( x \leq y { \mathrm { ~ o r ~ } } y \leq x ) { \mathrm { ~ f o r ~ a n y ~ } } x , y \in P .$

The pair$( P , \leq )$is then called a totally ordered set. [[Are we interested in well-orderings?]]

(d) An equivalence relation on P is a preordering ≃ such that

$x \simeq y$implies$y \simeq x$for all$x , y \in P .$

(e) Let$( P , \leq )$and$( Q , \leq )$be preorders. A function$f \colon P  Q$is$\left( { \mathrm { w e a k l y } } \right)$ order-preserving if

$x \leq y$in P implies$f \left( x \right) \leq f \left( y \right)$in Q, for all$x , y \in P$

An order-preserving function$f \colon ( P , \simeq )  ( Q , \simeq )$between sets with equivalence relations is the same as a function respecting the equivalence relations.

Definition 2.9.3 (Categories of orderings or relations). Let PreOrd be the category of preorders and order-preserving functions. Its objects are the preorders$( P , \leq )$, and the morphisms from$( P , \leq )$to$( Q , \leq )$are the orderpreserving functions$f \colon P \ \to \ Q$. Identities and composition are defined as in Set.

Let Poset$\mathbf { \Sigma } \subset \mathbf { \nabla } \mathbf { P r e O r d }$be the full subcategory generated by the partially ordered sets, let Ord ⊂ Poset be the full subcategory generated by the totally ordered sets, and let$\mathbf { E q R e l } \subset \mathbf { P r e O r d }$be the full subcategory generated by the equivalence relations.

Definition 2.9.4 (Preorders as categories). Any preorder$( P , \leq )$may be viewed as a small category, also denoted$P ,$with objects the elements of$P$, and morphisms

$$
P (x, y) = \left\{ \begin{array}{l l} \{x \to y \} & \text { if } x \leq y, \\ \emptyset & \text { if } x \not \leq y, \end{array} \right.
$$

for any$x , y \in P$. In other words, there is a unique morphism$x \to y { \mathrm { ~ i f ~ } } x \leq y ,$ and no morphisms from x to$y$otherwise. Identity morphisms exist, since$x \leq x$ for all$x _ { i }$, and the composite of two morphisms$x  y$and$y  z$is the unique morphism$x \longrightarrow z$, which exists because$x \leq y$and$y \le z$implies$x \leq z$

Any order-preserving function$f \colon ( P , \leq )  ( Q , \leq )$may be viewed as a functor$f \colon P  Q$between the small categories associated to$( P , { \leq } )$and$( Q , \leq )$ The function

$$
f \colon P (x, y) \longrightarrow Q (f (x), f (y))
$$

takes the unique morphism$x  y$to the unique morphism$f ( x ) \to f ( y ) { \mathrm { ~ i f ~ } } x \leq y$ in$P ,$which makes sense, since then$f \left( x \right) \leq f \left( y \right)$in$Q .$. If$x \not \le y$in$P$then there is nothing to specify.

Lemma 2.9.5. The rule viewing a preorder$( P , { \leq } )$as a small category defines a full and faithful functor

## PreOrd −→ Cat .

Proof. Briefly, this functor identifies PreOrd with the full subcategory of Cat generated by the small categories$\mathcal { C }$for which each morphism set${ \mathcal { C } } ( X , Y )$is either empty or consists of a single arrow$X  Y$

Here is a more detailed argument. It is clear that the identity function $i d _ { P } \colon ( P , \underline { { < } } ) \to ( P , \underline { { < } } )$maps to the identity functor, and that the composite of two order-preserving functions goes to the composite of the two associated functors. Hence we have a functor. To see that it is full and faithful, we must consider any pair$( P , \leq ) , ( Q , \leq )$of preorders, and check that the function

$$
\operatorname{PreOrd} ((P, \leq), (Q, \leq)) \longrightarrow \operatorname{Cat} (P, Q)
$$

that takes an order-preserving function$f \colon P  Q$to the associated functor, is bijective. We can do this by exhibiting the inverse function, which takes a functor$f \colon P \to Q$to the function$f \colon P \to Q$whose value$f ( x )$at the element $x \in P$is the element of$Q$given by the object$f ( x )$in$Q .$This produces an order-preserving function$f ,$since if$x \leq y$in$( P , \leq )$then there is a morphism $x \to y$in$P ,$and the functor$f$will take this to a morphism$f ( x )  f ( y )$in$Q .$ There is such a morphism in$Q$if and only if$f ( x ) \leq f ( y )$in$( Q , \leq )$, which proves that$f$is order-preserving.□

[[Conversely, a functor Cat → PreOrd that only remembers the existence of morphisms. It takes a small category$\mathcal { C }$to the preorder$( \mathrm { o b j } ( \mathcal { C } ) , \leq )$, where $X \le Y$for$X , Y \in \mathrm { o b j } ( \mathcal { C } )$if and only if there exists a morphism$f \colon X \to Y$ in$\mathcal { C }$. This is left adjoint to the forgetful functor.]]

Remark 2.9.6. Each of the categories in diagram (2.1) has a full subcategory generated by the objects that are preorders. This gives the following diagram of full subcategories of PreOrd:

![](images/page_58_image_1.jpg)

(2.2)

In the lower row, a skeletal preorder is the same as a poset, and a preorder with only one element is isomorphic to the one-morphism category ∗. In the upper row, a preorder where each relation is invertible is the same as an equivalence relation. A skeletal equivalence relation is the same as the discrete equivalence relation$\delta ,$where each equivalence class consists of a single element. A set with such a relation can be identified with the underlying set.

Note that diagram (2.2) maps to diagram (2.1), yielding a$3 \times 2 \times 2$box of full subcategories of Cat. We often think of monoids and preorders as giving rise to small categories in this way, and similarly groups and equivalence relations give rise to small groupoids.

Definition 2.9.7 (The totally ordered set [n]). For each non-negative integer$n \geq 0$, let

$$
[ n ] = \{0 <   1 <   \dots <   n - 1 <   n \}
$$

be the set of integers i with$0 \leq i \leq n .$with the usual total ordering, so that $i \leq j$if and only if i is less than or equal to$j$as integers. As in the example above, we also view [n] as the small category

$$
[ n ] = \{0 \rightarrow 1 \rightarrow \dots \rightarrow n - 1 \rightarrow n \}
$$

with objects$i = 0 , 1 , \ldots , n { - } 1$, n the integers i with$0 \leq i \leq n ,$, a unique morphism$i  j$for each$i \leq j$, and no morphisms$i  j$for$i > j$. When$i \leq j$, the unique morphism$i  j$factors as the composite

$$
i \rightarrow i + 1 \rightarrow \dots \rightarrow j - 1 \rightarrow j
$$

of$( j - i )$morphisms of the form$k { - } 1 \to k ,$for$i < k \le j$

Let$m , n \geq 0$. An order-preserving function$\alpha \colon [ m ]  [ n ]$is determined by its values$\alpha ( i )$for$0 \leq i \leq m$, which must satisfy

$$
0 \leq \alpha (0) \leq \alpha (1) \leq \dots \leq \alpha (m - 1) \leq \alpha (m) \leq n,
$$

and conversely.

The following category plays a fundamental role in the theory of simplicial sets, to be discussed in Chapter 6.

Definition 2.9.8 (Category$\Delta )$. Let$\Delta$be the skeleton category of finite nonempty ordinals. It is the full subcategory$\Delta \subset \mathbf { O r d }$generated by the ordinals

$$
[ n ] = \{0 <   1 <   \dots <   n - 1 <   n \}
$$

for all integers$n \geq 0$. For example,$[ 0 ] = \{ 0 \}$and$[ 1 ] = \{ 0 < 1 \}$. Hence the morphism set$\Delta ( [ m ] , [ n ] )$is the set of order-preserving functions$\alpha \colon [ m ]  [ n ]$ Identities and composition are given as in Set.

[[Forward reference to categories of pointed sets, finite pointed sets, left and right G-sets, left and right R-modules, left and right G-spaces, simplicial sets, simplicial groups, simplicial abelian groups, simplicial spaces, bisimplicial sets, etc.]]

[[Forward reference to functors like homology, topological realization, singular simplicial set, etc.]]

Chapter 3

# Transformations and equivalences

A reference for this chapter is Mac Lane [40, I,II,IV].

## 3.1 Natural transformations

Definition 3.1.1 (Natural transformation). Let$\mathcal { C }$, D be categories and let $F , G \colon \mathcal { C } \to \mathcal { D }$be functors. A natural transformation φ:$F \Rightarrow G$from$F$to$G$is a rule that to each object X in$\mathcal { C }$associates a morphism

$$
\phi_ {X} \colon F (X) \longrightarrow G (X)
$$

in${ \mathcal { D } } ,$, such that for each morphism$f \colon X \to Y$in$\mathcal { C }$the square

$$
\begin{array}{c} F (X) \xrightarrow {\phi_ {X}} G (X) \\ F (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow G (f) \\ F (Y) \xrightarrow {\phi_ {Y}} G (Y) \end{array}
$$

commutes. In other words, the two diagonal morphisms$G ( f ) \circ \phi _ { X } , \phi _ { Y } \circ$ $F ( f ) \colon F ( X ) \to G ( Y )$must be equal. We sometimes call the morphisms φ<sub>X</sub> the components of the natural transformation$\phi .$

The natural transformation$\phi$maps each commutative triangle in$\mathcal { C }$(on the left) to a commutative prism in$\mathcal { D }$(on the right):

![](images/page_60_image_10.jpg)

More generally,$\phi$maps any commutative diagram in$\mathcal { C }$to a commutative diagram in${ \mathcal { D } } .$, shaped like a cylinder on the original shape. In symbols the naturality condition reads$\phi _ { Y } F ( f ) = G ( f ) \phi _ { X }$, or just φ<sub>Y</sub>$f _ { * } = f _ { * } \phi _ { X }$

[[Later it may be suggestive to include the diagonal arrows, to see the triangulations of the square and the prism.]]

Example 3.1.2. Let$\mathcal { C } = \mathcal { D } = \mathbf { G r p }$, let$F = i d$and let G be the composite of the abelianization functor$( - ) ^ { a b } \colon { \bf G r p }  { \bf A b }$and the inclusion$\mathbf { A b } \subset \mathbf { G r p } .$ The canonical homomorphism$\phi _ { H } \colon H \to H ^ { a b }$is then a natural transformation $\phi \colon i d \to G$, since for each group homomorphism$f \colon H \to K$the diagram

![](images/page_61_image_3.jpg)

commutes. We may also call it a natural homomorphism.

Example 3.1.3. Let$( P , { \leq } )$and$( Q , \leq )$be preorders, and let$f , g \colon P  Q$be order-preserving functions. If we view the preorders as small categories$P , Q ,$ and the order-preserving functions as functors$f , g \colon P  Q$, then there is a natural transformation φ:$f \Rightarrow g$if and only if f is bounded above by$^ { g , }$in the sense that$f ( x ) \ \leq \ g ( x )$in$( Q , \leq )$for all$x \in P$. In this case there is a unique morphism$\phi _ { x } \colon f ( x ) \to g ( x )$in$Q$for each object x in$P ,$so the natural transformation φ is unique, if it exists.

[[Example: An isomorphism$M \cong D ( M ) = ( R - \mathbf { M o d } ) ( M , R )$exists for each finitely generated free R-module$M ,$, but no natural choice. However, there is a natural homomorphism$\rho \colon M \to D ( D ( M ) )$), which is an isomorphism for M finitely generated and projective.]]

[[Example: For rings R, T and a homomorphism$P  Q$of R-T-bimodules, there is a natural transformation of functor T−Mod → R−Mod from$P \otimes _ { T } ( - ) )$ to$Q \otimes _ { T } ( - ) . ] .$]

Definition 3.1.4 (Identity, composition of natural transformations). Let$\mathcal { C } _ { : }$$\mathcal { D }$be categories and let$F , G , H \colon \mathcal { C } \to \mathcal { D }$be functors. The identity natural transformation$i d _ { F } \colon F \Rightarrow F$is the rule that associates to each object X in$\mathcal { C }$the identity morphism$( i d _ { F } ) _ { X } = i d _ { F ( X ) } \colon F ( X )  F ( X )$. This is a natural transformation, since the square

$$
\begin{array}{c} F (X) \xrightarrow {=} F (X) \\ F (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow F (f) \\ F (Y) \xrightarrow {=} F (Y) \end{array}
$$

commutes for each morphism$f \colon X \to Y \ \operatorname { i n } \mathcal { C } .$

Let$\phi \colon F \Rightarrow G$and$\psi \colon G \Rightarrow H$be natural transformations. The composite natural transformation$\psi \circ \phi \colon F \Rightarrow H$is the rule that to each object$X$in$\mathcal { C }$ associates the composite morphism

$$
(\psi \circ \phi) _ {X} = \psi_ {X} \circ \phi_ {X} \colon F (X) \to H (X)
$$

in${ \mathcal { D } } .$. This defines a natural transformation, since the outer rectangle

$$
\begin{array}{c} F (X) \xrightarrow {\phi_ {X}} G (X) \xrightarrow {\psi_ {X}} H (X) \\ F (f) \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow G (f) \qquad \Biggl \downarrow H (f) \\ F (Y) \xrightarrow {\phi_ {Y}} G (Y) \xrightarrow {\psi_ {Y}} H (Y) \end{array}
$$

commutes for each morphism$f \colon X \to Y$in$\mathcal { C }$.

Lemma 3.1.5. Let$\mathcal { C }$and$\mathcal { D }$be categories, and assume that$\mathcal { C }$is small. Let $F , G \colon \mathcal { C } \to \mathcal { D }$be functors. Then the collection of all natural transformations $\phi \colon F \Rightarrow G$is a set.

Proof. To specify φ, we must choose a morphism$\phi _ { X }$in the set${ \mathcal { D } } ( F ( X ) , G ( X ) )$ for each object$X$in$\mathcal { C } .$. Since$\mathcal { C }$is small, there is only a set of possible choices. □

Definition 3.1.6 (Functor category). Let$\mathcal { C } , \mathcal { D }$be categories and assume that$\mathcal { C }$is small. The functor category Fun$( \mathcal { C } , \mathcal { D } )$has as objects the functors $F \colon { \mathcal { C } }  { \mathcal { D } }$. Let$G \colon { \mathcal { C } } \to { \mathcal { D } }$be a second such functor. The morphisms from$F$ to$G$are the natural transformations φ :$F \Rightarrow G$. The collection$\mathbf { F u n } ( \mathcal { C } , \mathcal { D } )$of all such natural transformations is a set, by the lemma above. Identities and composition are defined as in Definition 3.1.4.

An alternative notation for the functor category is$\mathcal { D } ^ { \mathcal { C } } = \mathbf { F u n } ( \mathcal { C } , \mathcal { D } )$

Remark 3.1.7. When$\mathcal { C }$is small, we think of a functor$F \colon \mathcal { C }  \mathcal { D }$as a$\mathcal { C } .$ shaped diagram in$\mathcal { D }$. We call$\mathcal { C }$the indexing category of the diagram. For each object$X$of$\mathcal { C }$there is a vertex in the diagram with the object$F ( X )$in$\mathcal { D }$. For each morphism$f \colon X \to Y$in$\mathcal { C }$there is an edge in the diagram connecting$F ( X )$ to$F ( Y )$by the morphism$F ( f )$in${ \mathcal { D } } .$. Each commuting triangle in$\mathcal { C }$expresses a composition relation$g f = g \circ f$, and by functoriality the corresponding relation $F ( g f ) = F ( g ) \circ F ( f )$holds in the$\mathcal { C } \mathrm { - s h a p e d }$diagram in$\mathcal { D }$. Given a second functor$G \colon { \mathcal { C } } \to { \mathcal { D } }$and a natural transformation$\phi \colon F \Rightarrow G .$, we think of$G$as giving a second$\mathcal { C } .$-shaped diagram in$\mathcal { D }$, and$\phi$as specifying a cylinder-shaped diagram in${ \mathcal { D } } ,$with the C -shaped diagrams given by$F$and$G$at the top and bottom, respectively. [[Reference to more precise statement$\mathcal { D } \times [ 1 ]$and the cylinder.]]

Remark 3.1.8. When we view a functor$\mathcal { C } \to \mathcal { D }$, or a C -shaped diagram in$\mathcal { D }$ as an object in the functor category${ \bf F u n } ( \mathcal { C } , \mathcal { D } )$, we may wish to make a shift in the notation, calling this object in Fun$( \mathcal { C } , \mathcal { D } )$something like$X$or$Y ,$. To make room for this shift, we must first assign other notation for the objects of the indexing category$\mathcal { C }$. For generic$\mathcal { C }$we might call its objects$c , d ,$while for specific indexing categories$\mathcal { C }$other notations may be more suggestive.

Example 3.1.9. Recall the notation$[ n ] = \{ 0 \to 1 \to \cdots \to n { - } 1 \to n \}$from Definition 2.9.7. A functor$X \colon [ n ]  \mathcal { D }$amounts to a diagram

$$
X (0) \xrightarrow {\xi_ {1}} X (1) \longrightarrow \dots \longrightarrow X (n - 1) \xrightarrow {\xi_ {n}} X (n)
$$

in${ \mathcal { D } } ,$with each$X ( k )$an object of D for$0 \leq k \leq n$, and each$\xi _ { k } \colon X ( k { - } 1 ) \to$ $X ( k )$a morphism in D for$1 \leq k \leq n$. A second functor$Y \colon [ n ]  \mathcal { D }$amounts

to a diagram

$$
Y (0) \xrightarrow {\eta_ {1}} Y (1) \longrightarrow \dots \longrightarrow Y (n - 1) \xrightarrow {\eta_ {n}} Y (n)
$$

in${ \mathcal { D } } ,$and a natural transformation$\phi \colon X \Rightarrow Y$amounts to a commutative diagram

$$
\begin{array}{l} X (0) \xrightarrow {\xi_ {1}} X (1) \xrightarrow {} \dots \xrightarrow {} X (n - 1) \xrightarrow {\xi_ {n}} X (n) \\ \phi_ {0} \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow \phi_ {1} \qquad \qquad \qquad \Biggl \downarrow \phi_ {n - 1} \qquad \Biggl \downarrow \phi_ {n} \\ Y (0) \xrightarrow {\eta_ {1}} Y (1) \xrightarrow {} \dots \xrightarrow {} Y (n - 1) \xrightarrow {\eta_ {n}} Y (n) \end{array}
$$

in${ \mathcal { D } } _ { : }$, where the horizontal morphisms are as above. These are then the objects and morphisms of the functor category Fun$( [ n ] , \mathcal { D } ) = \mathcal { D } ^ { [ n ] }$. When$n = 0$there is an obvious isomorphism of categories$\mathbf { F u n } ( [ 0 ] , \mathcal { D } ) \cong \mathcal { D } .$

Definition 3.1.10 (Arrow category). The arrow category$\operatorname { A r } ( { \mathcal { D } } )$of a category$\mathcal { D }$has objects the morphisms$\xi \colon X _ { 0 } \to X _ { 1 }$in${ \mathcal { D } } _ { : }$, and morphisms$f \colon \xi  \eta$ from$\xi \colon X _ { 0 } \to X _ { 1 }$to$\eta \colon Y _ { 0 } \to Y _ { 1 }$the pairs$\boldsymbol { f } = \left( f _ { 0 } , f _ { 1 } \right)$of morphisms$f _ { 0 } \colon X _ { 0 } \to$ $Y _ { 0 } , f _ { 1 } \colon X _ { 1 }  Y _ { 1 }$in$\mathcal { D }$that make the square

$$
\begin{array}{c} X _ {0} \xrightarrow {\xi} X _ {1} \\ f _ {0} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow f _ {1} \\ Y _ {0} \xrightarrow {\eta} Y _ {1} \end{array}
$$

commute. There is an obvious isomorphism of categories Fun$( [ 1 ] , \mathcal { D } ) \cong \operatorname { A r } ( \mathcal { D } )$

Definition 3.1.11 (Inclusion, evaluation functors). For$t \in \{ 0 , 1 \}$, let

$$
i _ {t} \colon \mathcal {C} \to \mathcal {C} \times [ 1 ]
$$

be the functor that takes X to (X, t) and$f \colon X  Y { \mathrm { ~ t o ~ } } ( f , i d _ { t } )$, and let

$$
e _ {t} \colon \operatorname{Ar} (\mathcal {C}) \to \mathcal {C}
$$

be the functor that takes$\xi \colon X _ { 0 } \to X _ { 1 }$to$X _ { t }$and$f = ( f _ { 0 } , f _ { 1 } ) \colon \xi  \eta$to$f _ { t }$

Lemma 3.1.12. Let$F , G \colon \mathcal { C }  \mathcal { D }$be given functors. There are bijective correspondences between:

(a) the functors Φ:$\mathcal { C } \times [ 1 ]  \mathcal { D }$with$\Phi \circ i _ { 0 } = F$and$\Phi \circ i _ { 1 } = G _ { \mathrm { \colon } }$;

(b) the natural transformations φ:$F \Longrightarrow G$;

(c) the functors$\Psi : \mathcal { C } \to \mathrm { A r } ( \mathcal { D } )$with$e _ { 0 } \circ \Psi = F$and$e _ { 1 } \circ \Psi = G$

In particular, the identity functor of$\mathcal { C } \times [ 1 ]$corresponds to a universal natural transformation

$$
\phi \colon i _ {0} \Longrightarrow i _ {1}
$$

between the functors$i _ { 0 } , i _ { 1 } \colon \mathcal { C } \mathrm { ~  ~ } \mathcal { C } \mathrm { ~ \times ~ } [ 1 ]$, taking each object$X$in$\mathcal { C }$to the morphism$( i d _ { X } , 0  1 )$in${ \mathcal { C } } \times [ 1 ]$

Proof. The first correspondence takes a functor Φ to the natural transformation $\phi$with$\phi _ { X } = \Phi ( i d _ { X } , 0  1 )$Conversely, a natural transformation φ maps to the functor Φ given on objects by$\Phi ( X , 0 ) = F ( X ) , \Phi ( X , 1 ) = G ( X )$, and on morphisms by$\Phi ( f , i d _ { 0 } ) = F ( f ) , \Phi ( f , i d _ { 1 } ) = G ( f )$and$\Phi ( i d _ { X } , 0  1 ) = \psi _ { X }$ The commutation relation

$$
(i d _ {Y}, 0 \rightarrow 1) \circ (f, i d _ {0}) = (f, 0 \rightarrow 1) = (f, i d _ {1}) \circ (i d _ {X}, 0 \rightarrow 1)
$$

in the product category${ \mathcal { C } } \times [ 1 ]$corresponds precisely to the naturality condition on φ.

The second correspondence takes a natural transformation$\phi$to the functor $\Psi$given on objects by$\Psi ( X ) = ( \phi _ { X } \colon F ( X ) \to G ( X ) )$, and on morphisms by $\Psi ( f ) = ( F ( f ) , G ( f ) )$. Conversely, a functor Ψ maps to the natural transformation$\phi$with$\phi _ { X } = \Psi ( X )$. The commutation condition for morphisms in$\operatorname { A r } ( { \mathcal { D } } )$ corresponds precisely to the naturality condition on$\phi .$□

Lemma 3.1.13. Let$\mathcal { C } , \mathcal { D } , \mathcal { E }$be categories, with$\mathcal { C }$and$\mathcal { D }$small. There is a natural isomorphism

$$
\mathbf {F u n} (\mathcal {C} \times \mathcal {D}, \mathcal {E}) \cong \mathbf {F u n} (\mathcal {C}, \mathbf {F u n} (\mathcal {D}, \mathcal {E}))
$$

that takes a functor Φ:${ \mathcal { C } } \times { \mathcal { D } } \to { \mathcal { E } }$to the functor$\Psi \colon \mathcal { C }  \mathbf { F u n } ( \mathcal { D } , \mathcal { E } )$that takes$X$in$\mathcal { C }$to$\Psi ( X ) \colon { \mathcal { D } } \longrightarrow { \mathcal { E } }$given by$\Psi ( X ) ( Y ) = \Phi ( X , Y )$for all Y in$\mathcal { D }$.

Proof. [[Clear enough.]]

## 3.2 Natural isomorphisms and equivalences

Definition 3.2.1 (Natural isomorphism). Let$\mathcal { C } , \mathcal { D }$be categories and let $F , G \colon \mathcal { C }  \mathcal { D }$be functors. A natural isomorphism$\phi \colon F \stackrel { \cong } { \Longrightarrow } G$is a natural transformation such that the morphism

$$
\phi_ {X} \colon F (X) \xrightarrow {\cong} G (X)
$$

is an isomorphism in${ \mathcal { D } } _ { : }$, for each object X in$\mathcal { C }$. Alternatively we may write $\phi \colon F \cong G$

Example 3.2.2. Let$\mathcal { C } , \mathcal { D }$be categories with ob${ \mathfrak { j } } ( { \mathcal { C } } ) = { \mathrm { o b j } } ( { \mathcal { D } } ) = \{ * \}$, and endomorphism monoids$M = \mathcal { C } ( \ast , \ast ) , N = \mathcal { D } ( \ast , \ast )$, let$F , G \colon \mathcal { C }  \mathcal { D }$be functors with associated monoid homomorphisms$F , G \colon M \to N$, and let φ :$F \Rightarrow G$ be a natural transformation. Then φ associates to the object ∗ in$\mathcal { C }$a morphism$\phi _ { * } \colon * \ = \ F ( * ) \ \to \ G ( * ) \ = \ *$in$\mathcal { D }$, which we consider as an element $h = \phi _ { * } \in N = \mathcal { D } ( * , * )$The condition that φ is a natural transformation asks that$h F ( f ) = G ( f ) h$in$N$, for all$f \in M$. We say that$h \in N$acts as an intertwiner between the homomorphisms$F \colon M \to N$and$G \colon M \to N$. When$\phi$is a natural isomorphism,$h$must be invertible in$N$, so the naturality condition can be rewritten as$G ( f ) = h F ( f ) h ^ { - 1 }$for all$f \in M$. In other words,$G \colon M \to N$is the conjugate of$F \colon M \to N$by$h$

Similar remarks apply when$\mathcal { C } , \mathcal { D }$are one-object groupoids, and$\phi \colon F \Rightarrow G$ a natural transformation of functors$F , G \colon \mathcal { C } \to \mathcal { D }$. Since$\mathcal { D }$is a groupoid,$\phi$is automatically a natural isomorphism.

Lemma 3.2.3. The identity$i d _ { F } \colon F \stackrel { \cong } { \Longrightarrow } F$is a natural isomorphism, the inverse$\phi ^ { - 1 } \colon G \stackrel { \cong } { \Longrightarrow } F$of a natural isomorphism is a natural isomorphism, and the composite$\psi \circ \phi \colon F \stackrel { \cong } \implies$H of$\phi$and a natural isomorphism ψ :$G \xrightarrow { \cong }$is a natural isomorphism.

Proof. This is clear.

Lemma 3.2.4. A natural transformation$\phi \colon F \Rightarrow G$is a natural isomorphism if and only if there exists a natural transformation$\psi \colon G \Rightarrow F$such that$\psi \circ \phi =$ $i d _ { F }$and$\phi \circ \psi = i d _ { G }$. If C is small, this is the same as saying that$\phi$is an isomorphism from$F$to G in$\mathbf { F u n } ( \mathcal { C } , \mathcal { D } )$

Proof. Suppose that$\phi$is a natural isomorphisms, so that$\phi _ { X } \colon F ( X ) \to G ( X )$ is an isomorphism for each object X in$\mathcal { C }$. Let$\psi _ { X } = ( \phi _ { X } ) ^ { - 1 } \colon G ( X ) \to F ( X )$ be the inverse isomorphism, for each$X$. Then the square

$$
\begin{array}{c} G (X) \xrightarrow {\psi_ {X}} F (X) \\ G (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow F (f) \\ G (Y) \xrightarrow {\psi_ {Y}} F (Y) \end{array}
$$

commutes for each morphism$f \colon X \to Y$, because

$$
F (f) \circ \psi_ {X} = \psi_ {Y} \circ \phi_ {Y} F (f) \circ \phi_ {X} ^ {- 1} = \psi_ {Y} \circ G (f) \phi_ {X} \circ \phi_ {X} ^ {- 1} = \psi_ {Y} \circ G (f).
$$

Hence$\psi$is a natural transformation. It is clear that ψφ and$\phi \psi$are the respective identity transformations.□

Example 3.2.5. A natural isomorphism φ:$X \stackrel { \cong } { \implies } Y$between a pair of functors $X , Y \colon [ n ]  { \mathcal { D } }$amounts to a commutative diagram

$$
\begin{array}{c} X (0) \xrightarrow {\xi_ {1}} X (1) \xrightarrow {} \dots \xrightarrow {} X (n - 1) \xrightarrow {\xi_ {n}} X (n) \\ \phi_ {0} \Biggl \downarrow \cong \qquad \cong \Biggl \downarrow \phi_ {1} \qquad \qquad \cong \Biggl \downarrow \phi_ {n - 1} \qquad \cong \Biggl \downarrow \phi_ {n} \\ Y (0) \xrightarrow {\eta_ {1}} Y (1) \xrightarrow {} \dots \xrightarrow {} Y (n - 1) \xrightarrow {\eta_ {n}} Y (n) \end{array}
$$

in${ \mathcal { D } } .$, where the vertical arrows are isomorphisms.

[[Example: Natural transformation$\nu _ { M }$: Hom$_ { R } ( P , R ) \otimes _ { R } M \to \mathrm { H o m } _ { R } ( P , M )$ is a natural isomorphism when$P$is finitely generated and projective.]]

[[Natural transformation$\rho _ { M } \colon M \to { \mathrm { H o m } } _ { R } ( { \mathrm { H o m } } _ { R } ( M , R ) , R )$is a natural isomorphism when restricted to the full subcategory of finitely generated projective R-modules M]]

Remark 3.2.6. Recall that an isomorphism of categories is a functor$F \colon \mathcal { C }$ $\mathcal { D }$such that there exists an inverse functor$G \colon { \mathcal { D } } \to { \mathcal { C } }$with$G \circ F = i d _ { \mathcal { C } } \colon \mathcal { C } \to \mathcal { C }$ and$F \circ G = i d _ { \mathcal { D } } \colon \mathcal { D } \to \mathcal { D }$. Requiring equality of functors in these two cases is a very strict condition. It is more natural in the categorical context to ask for natural isomorphism of functors. This leads to the following notion, of equivalence of categories, which is a more flexible and useful condition.

Definition 3.2.7 (Equivalence of categories). Let$\mathcal { C } , \mathcal { D }$be categories. A functor$F \colon \mathcal { C }  \mathcal { D }$is an equivalence if there exists a functor$G \colon { \mathcal { D } } \to { \mathcal { C } }$and natural isomorphisms$\phi \colon G \circ F { \stackrel { \cong } { \longrightarrow } } i d \varphi$and ψ :$F \circ G { \stackrel { \cong } { \Longrightarrow } } i d _ { \mathcal { D } }$

In this case we say that$\mathcal { C }$and$\mathcal { D }$are equivalent categories, and that$G$is an inverse equivalence to$F .$Note that$G$is usually not uniquely determined by$F .$ It does of course not matter if we specify the natural isomorphisms$\phi$and$\psi$or their inverses.

Lemma 3.2.8. Equivalence of categories defines an equivalence relation on any set$o f$categories.

Proof. The identity$i d _ { \mathcal { C } } \colon \mathcal { C } \to \mathcal { C }$is clearly an equivalence of categories. If $F \colon { \mathcal { C } }  { \mathcal { D } }$and$G \colon { \mathcal { D } }  { \mathcal { C } }$satisfy$G F \stackrel { \cong } { \Longrightarrow } i d _ { \mathcal { C } }$and$F G \stackrel { \cong } { \Longrightarrow } i d _ { \mathcal { D } }$, so that $F$is an equivalence, then the same natural isomorphisms show that$G$is an equivalence. If furthermore$F ^ { \prime } \colon \mathcal { D }  \mathcal { E }$and$G ^ { \prime } \colon { \mathcal { E } } \to { \mathcal { D } }$satisfy$G ^ { \prime } F ^ { \prime } \stackrel { \cong } { \implies } i d _ { \mathcal { D } }$ and$F ^ { \prime } G ^ { \prime } \xrightarrow { \cong } i d _ { \mathcal { E } }$, so that$F$and$F ^ { \prime }$are equivalences, then$F ^ { \prime } F \colon \mathcal { C } \to \mathcal { E }$is also an equivalence, since there are composite natural isomorphisms

$$
(G G ^ {\prime}) (F ^ {\prime} F) = G (G ^ {\prime} F ^ {\prime}) F \stackrel {\cong} {\Longrightarrow} G (i d _ {\mathcal {D}}) F = G F \stackrel {\cong} {\Longrightarrow} i d _ {\mathcal {C}}
$$

and

$$
(F ^ {\prime} F) (G G ^ {\prime}) = F ^ {\prime} (F G) G ^ {\prime} \stackrel {\cong} {\Longrightarrow} F ^ {\prime} (i d _ {\mathcal {D}}) G ^ {\prime} = F ^ {\prime} G ^ {\prime} \stackrel {\cong} {\Longrightarrow} i d _ {\mathcal {E}}.
$$

Definition 3.2.9 (Essentially surjective functor). A functor$F \colon { \mathcal { C } }  { \mathcal { D } }$ is essentially surjective if for each object$Z$of$\mathcal { D }$there exists an object X of$\mathcal { C }$ and an isomorphism$F ( X ) \cong Z$in$\mathcal { D }$

Theorem 3.2.10. A functor$F \colon { \mathcal { C } }  { \mathcal { D } }$is an equivalence of categories$i f$and only if it is a full, faithful and essentially surjective.

Proof. For the forward implication, suppose that$F$is an equivalence. Then there exists a functor$G \colon { \mathcal { D } }  { \mathcal { C } }$and natural isomorphisms$\phi \colon G F \stackrel { \cong } { \Longrightarrow } i d \varphi$ and$\psi \colon F G \stackrel { \cong } { \Longrightarrow } i d _ { \mathcal { D } }$. Consider any pair of objects X, Y in$\mathcal { C } ,$and consider the function

$$
F \colon \mathcal {C} (X, Y) \longrightarrow \mathcal {D} (F (X), F (Y))
$$

taking$f$to$F ( f )$. We must prove that it is a bijection, so that$F$is full and faithful. First, consider two morphisms$f , g \colon X \to Y$in$\mathcal { C }$, and suppose that $F ( f ) = F ( g )$in$\mathcal { D }$. Then$G F ( f ) = G F ( g )$in$\mathcal { C }$, so we can combine the following two commutative squares:

$$
\begin{array}{c} X \xleftarrow {\stackrel {{\phi_ {X}}} {{\cong}}} G F (X) \xrightarrow {\stackrel {{\phi_ {X}}} {{\cong}}} X \\ f \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ Y \xleftarrow {\stackrel {{\phi_ {Y}}} {{\cong}}} G F (Y) \xrightarrow {\stackrel {{\phi_ {Y}}} {{\cong}}} Y \end{array}
$$

Hence$f = \phi _ { Y } \phi _ { Y } ^ { - 1 } \circ g \circ \phi _ { X } \phi _ { X } ^ { - 1 } = g$and the function$F$is injective. By the same argument, using ψ :$F G { \stackrel { \cong } { \Longrightarrow } } i d _ { \mathcal { D } }$, the function

$$
G \colon \mathscr {D} (Z, W) \longrightarrow \mathscr {C} (G (Z), G (W))
$$

is injective for all objects$Z ,$W in$\mathcal { D }$. Next, let$h \colon F ( X ) \to F ( Y )$be a morphism in${ \mathcal { D } } .$. Form the composite morphism$f = \phi _ { Y } \circ G ( h ) \circ \phi _ { X } ^ { - 1 }$in$\mathcal { C } .$. Then we have the following two commutative squares:

$$
\begin{array}{c} G F (X) \xrightarrow [ \cong ]{\phi_ {X}} X \xleftarrow [ \cong ]{\phi_ {X}} G F (X) \\ G (h) \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow f \qquad \qquad \Biggl \downarrow G F (f) \\ G F (Y) \xrightarrow [ \cong ]{\phi_ {Y}} Y \xleftarrow [ \cong ]{\phi_ {Y}} G F (Y) \end{array}
$$

Hence$G ( h ) = \phi _ { Y } ^ { - 1 } \phi _ { Y } \circ G F ( f ) \circ \phi _ { X } ^ { - 1 } \phi _ { X } = G F ( f )$. By injectivity of the function$G ,$, it follows that$h = F ( f )$. Since$h \colon F ( X ) \to F ( Y )$was arbitrary, this proves that the function$F$is surjective. Finally, given any object$Z$of$\mathcal { D }$let $X = G ( Z )$). Then$\psi _ { Z } \colon F G ( Z ) \xrightarrow { \cong } Z$is an isomorphism$F ( X ) \cong Z$. Hence$F$is essentially surjective.

For the reverse implication, suppose that F is full, faithful and essentially surjective. We must construct an inverse equivalence$G \colon { \mathcal { D } }  { \mathcal { C } }$. For each object$Z$in$\mathcal { D }$there exists an object X in$\mathcal { C }$such that$F ( X ) \cong Z _ { \ O }$, by the essential surjectivity of$F .$. For each$Z$we fix such an object$X$, and define $G ( Z ) = X$. This specifies G on objects. Furthermore, for each Z we choose an isomorphism$F ( X ) \stackrel { \cong } { \longrightarrow } Z .$, which we denote$\psi _ { Z } \colon F G ( Z ) \stackrel { \cong } { \longrightarrow } Z .$. This specifies a natural isomorphism ψ :$F G  i d _ { \mathcal { D } }$on objects. Now let$h \colon Z \to W$be a morphism in${ \mathcal { D } } .$. The composite$\psi _ { W } ^ { - 1 } \circ h \circ \psi _ { Z } \colon F G ( Z ) \to F G ( W )$in$\mathcal { D }$can be written as$F ( f )$for a unique morphism$f \colon G ( Z ) \to G ( W )$, since$F$is full and faithful. We define$G ( h ) = f$for this unique morphism. This specifies$G$on morphisms. It is straightforward to check that$G \colon { \mathcal { D } } \to { \mathcal { C } }$is a functor. The diagram

$$
\begin{array}{c} F G (Z) \xrightarrow [ \cong ]{\psi_ {Z}} Z \\ F G (h) \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow h \\ F G (W) \xrightarrow [ \cong ]{\psi_ {W}} W \end{array}
$$

commutes, since$F G ( h ) = F ( f ) = \psi _ { W } ^ { - 1 }$◦ h ◦ ψ , so ψ :$F G \xrightarrow { \cong } i d _ { \mathcal { D } }$is a natural isomorphism. It remains to construct a natural isomorphism$\phi \colon G F \stackrel { \cong } { \Longrightarrow } i d \varphi$ For each object X in$\mathcal { C }$, the isomorphism$\psi _ { F ( X ) } \colon F G F ( X ) \ { \stackrel { \cong } { \longrightarrow } } \ F ( X )$can be written as$F ( \phi _ { X } )$for a unique morphism$\phi _ { X } \colon \dot { G } \dot { F } ( X ) \to X$, since F is full and faithful. This specifies$\phi$on objects. Finally, let$f \colon X \to Y$be a morphism in$\mathcal { C } .$. We must verify that the square

$$
\begin{array}{c} G F (X) \xrightarrow [ \cong ]{\phi_ {X}} X \\ \Biggl \downarrow_ {G F (f)} \qquad \qquad \qquad \qquad \Biggl \downarrow_ {f} \\ G F (Y) \xrightarrow [ \cong ]{\phi_ {Y}} Y \end{array}
$$

commutes. Since$F$is faithful, it sufices to show that$F ( f \circ \phi _ { X } ) = F ( f ) \circ$ $F ( \phi _ { X } ) = F ( f ) \circ \psi _ { F ( X ) }$is equal to${ \cal F } ( \phi _ { Y } \circ G F ( f ) ) \ : = \ : F ( \phi _ { Y } ) \circ F G F ( f ) \ : =$ $\psi _ { F ( Y ) } \circ F G F ( f )$, but this is just the naturality condition for ψ :$F G \stackrel { \cong } { \Longrightarrow } i d _ { \mathcal { D } }$ with respect to the morphism$F ( f ) \colon F ( X ) \to F ( Y )$in${ \mathcal { D } } .$□

Elaborating on Definition 2.8.1, we use the following terminology.

Definition 3.2.11 (Skeletal subcategory). A skeleton of a category$\mathcal { C }$is a full subcategory${ \mathcal { C } } ^ { \prime } \subseteq { \mathcal { C } }$such that each object of$\mathcal { C }$is isomorphic in$\mathcal { C }$to one and only one object in$\mathcal { C } ^ { \prime }$. (We do not ask that the isomorphism is unique as a morphism in$\mathcal { C } . )$The subcategory$\mathcal { C } ^ { \prime }$is then skeletal, in the sense that two objects X, Y in$\mathcal { C } ^ { \prime }$are isomorphic in$\mathcal { C } ^ { \prime }$if and only if they are equal.$\mathrm { A }$ category$\mathcal { C }$is said to be skeletally small if it admits a skeleton$\mathcal { C } ^ { \prime }$that is small.

Lemma 3.2.12. The inclusion of a skeleton$\mathcal { C } ^ { \prime }$in a category$\mathcal { C }$is an equivalence of categories.

Proof. The inclusion functor$\mathcal { C } ^ { \prime } \subseteq \mathcal { C }$is full and faithful, since$\mathcal { C } ^ { \prime }$is a full subcategory. Furthermore, this functor is essentially surjective, by the definition of a skeleton. Hence it is an equivalence of categories, by Theorem 3.2.10.

Example 3.2.13. The category$\mathcal { F }$of Example 2.2.8 is a small skeleton of the category Fin of finite sets and functions. Similarly, the groupoid iso$( \mathcal { F } )$is a small skeleton of iso(Fin).

Lemma 3.2.14. Any two skeleta of the same category are isomorphic.

Proof. Let$\mathcal { C } ^ { \prime }$and$\mathcal { C } ^ { \prime \prime }$be skeleta of$\mathcal { C } .$For each object$X ^ { \prime }$of$\mathcal { C } ^ { \prime }$, there is a unique object$X ^ { \prime \prime }$in$\mathcal { C } ^ { \prime \prime }$such that$X ^ { \prime }$and$X ^ { \prime \prime }$are isomorphic in$\mathcal { C }$. Choose such an isomorphism$h _ { X ^ { \prime } } \colon X ^ { \prime } \xrightarrow { \cong } X ^ { \prime \prime }$. Define a functor$F \colon { \mathcal { C } } ^ { \prime } \to { \mathcal { C } } ^ { \prime \prime }$by$F ( X ^ { \prime } ) = X ^ { \prime \prime }$ on objects. For any morphism$f ^ { \prime } \colon X ^ { \prime } \to Y ^ { \prime }$in$\mathcal { C } ^ { \prime }$, let$F ( f ^ { \prime } ) \colon X ^ { \prime \prime } \to Y ^ { \prime \prime }$be the composite

$$
F (f ^ {\prime}) = h _ {Y ^ {\prime}} \circ f ^ {\prime} \circ h _ {X ^ {\prime}} ^ {- 1}.
$$

Then$F ( i d _ { X ^ { \prime } } ) = i d _ { X ^ { \prime \prime } }$′ and$F ( g ^ { \prime } f ^ { \prime } ) = F ( g ^ { \prime } ) F ( f ^ { \prime } )$whenever$f ^ { \prime }$and$g ^ { \prime } \colon Y ^ { \prime } \to Z ^ { \prime }$ are composable, so$F$is a functor.

Reversing the roles of$\mathcal { C } ^ { \prime }$and$\mathcal { C } ^ { \prime \prime }$, we can also define a functor$G \colon { \mathcal { C } } ^ { \prime \prime } \to$ $\mathcal { C } ^ { \prime }$. Then$G F ( X ^ { \prime } ) = X ^ { \prime }$and$F G ( X ^ { \prime \prime } ) = X ^ { \prime \prime }$. If we take care to choose the isomorphism$h _ { X ^ { \prime } } ^ { - 1 } \colon X ^ { \prime \prime } \xrightarrow { \cong } X ^ { \prime }$as the isomorphism$h _ { X ^ { \prime \prime } }$in the definition of$G$on morphisms, then we also get that$G F ( f ^ { \prime } ) = f ^ { \prime }$and$F G ( f ^ { \prime \prime } ) = f ^ { \prime \prime }$, so$F$and$G$ are inverse isomorphisms of categories.□

Definition 3.2.15 (Connected groupoid). We say that a groupoid$\mathcal { C }$is connected if it is non-empty, and any two objects$X , Y \in \mathrm { o b j } ( \mathcal { C } )$are isomorphic. A connected, skeletal groupoid has precisely one object.

Lemma 3.2.16. Let X be an object in a connected groupoid$\mathcal { C }$, with automorphism group$\operatorname { A u t } ( X ) = { \mathcal { C } } ( X , X )$. Then the inclusion

$$
\mathscr {B} \operatorname{Aut} (X) = \mathscr {B C} (X, X) \xrightarrow {\simeq} \mathscr {C}
$$

is an equivalence of categories.

Proof. We identify${ \mathcal { B C } } ( X , X )$with the full subgroupoid of$\mathcal { C }$generated by the object$X$. The inclusion functor is obviously full and faithful, and it is essentially surjective since$\mathcal { C }$is assumed to be connected. Hence the inclusion is an equivalence, by Theorem 3.2.10.□

Proposition 3.2.17. Let$\mathcal { C }$be a groupoid with a small skeleton$\mathcal { C } ^ { \prime }$, generated $b y$a set$\{ X _ { i } \} _ { i \in I }$of objects. The inclusion

$$
\coprod_ {i \in I} \mathcal {B} \operatorname{Aut} (X _ {i}) = \coprod_ {i \in I} \mathcal {B C} (X _ {i}, X _ {i}) \cong \mathcal {C} ^ {\prime} \xrightarrow {\simeq} \mathcal {C}
$$

is an equivalence of categories.

Proof. Let$\mathcal { C } _ { i } \subseteq \mathcal { C }$be the full subgroupoid of$\mathcal { C }$generated by the objects that are isomorphic to$X _ { i }$, for each$i \in I$. Then there is an isomorphism of categories

$$
\coprod_ {i \in I} \mathcal {C} _ {i} \cong \mathcal {C}.
$$

Each$\mathcal { C } _ { i }$is connected, so there is an equivalence B Aut$( X _ { i } ) = \mathcal { B C } ( X _ { i } , X _ { i } ) \simeq \mathcal { C } _ { i }$ by Lemma 3.2.16. The coproduct of these equivalences is the asserted equivalence.□

Example 3.2.18. Let$\mathcal { C }$be a non-empty groupoid such that any two objects are isomorphic by a unique isomorphism. Then$\operatorname { A u t } ( X ) = \{ i d _ { X } \}$for each object X in$\mathcal { C }$, and the unique functor

$$
\mathcal {C} \xrightarrow {\simeq} *
$$

to the terminal category is an equivalence.

Example 3.2.19. The groupoid iso(Fin) of finite sets has the small skeleton $\mathcal { F }$, generated by the objects$\mathbf { n } = \{ 1 , 2 , \dots n \}$for$n \in  { \mathbb { N } } _ { 0 }$, and$\operatorname { A u t } ( \mathbf { n } ) = \Sigma _ { n }$, so the inclusion

$$
\coprod_ {n \geq 0} \mathcal {B} \Sigma_ {n} \xrightarrow {\simeq} \operatorname{iso} (\mathbf {F i n})
$$

is an equivalence of categories.

Example 3.2.20. Let G be a finite group. The groupoid iso(G−Fin) of finite G-sets has a small skeleton generated by the objects

$$
X (\nu) = \coprod_ {(H)} \coprod_ {i = 1} ^ {\nu (H)} G / H
$$

where H ranges over a set of representatives for the conjugacy classes of subgroups of$G ,$and each$\nu ( H ) \in \mathbb { N } _ { 0 }$. The elements$x \in X ( \nu )$with stabilizer$G _ { x }$ conjugate to H lie in the summand indexed by (H). A G-equivariant bijection $f \colon X ( \nu )  X ( \nu )$preserves the stabilizers, in the sense that$G _ { x } = G _ { f ( x ) }$, hence it decomposes as a coproduct$\textstyle f = \operatorname { I } \operatorname { I } _ { ( H ) } f _ { H }$. For each$H ,$letting$n = \nu ( H )$, the restricted G-equivariant bijection

$$
f _ {H} \colon \coprod_ {i = 1} ^ {n} G / H \longrightarrow \coprod_ {i = 1} ^ {n} G / H
$$

takes the i’th copy of$G / H$to the$\sigma ( i ) \ – \mathrm { t h }$copy of$G / H$, for some permutation $\sigma \in \Sigma _ { n }$, and for each$1 \leq i \leq n$, the G-map$G / H \to G / H$is determined by taking eH to$w _ { i } H$for some element$w _ { i } \in W _ { G } ( H )$. [[Reference for Weyl group?]] We can write

$$
f _ {H} = (\sigma ; w _ {1}, \dots , w _ {n}) \in \Sigma_ {n} \ltimes W _ {G} (H) \times \dots \times W _ {G} (H) = \Sigma_ {n} \wr W _ {G} (H).
$$

[[Reference for wreath product?]] Hence

$$
\operatorname{Aut} (X (\nu)) \cong \prod_ {(H)} \Sigma_ {\nu (H)} \wr W _ {G} (H)
$$

and iso(G−Fin) is equivalent to the small skeleton

$$
\coprod_ {\nu} \mathscr {B} \operatorname{Aut} (X (\nu)) \cong \prod_ {(H)} \coprod_ {n \geq 0} \mathscr {B} \left(\Sigma_ {n} \wr W _ {G} (H)\right).
$$

Example 3.2.21. For$G \ = \ C _ { p }$of prime order, the possible subgroups are $H = G$and$H = \{ e \}$, with Weyl groups$W _ { G } ( G ) = \{ e \}$and$W _ { G } ( \{ e \} ) = G$, so

$$
\mathrm{iso} (C _ {p} - \mathbf {F i n}) \simeq \coprod_ {n \geq 0} \mathcal {B} \Sigma_ {n} \times \coprod_ {n \geq 0} \mathcal {B} (\Sigma_ {n} \wr G).
$$

[[Discuss functors$C _ { p } { - } \mathbf { F i n } \to \mathbf { F }$in taking X to$X , X ^ { G }$or$X / G$, and conversely. Give Segal–tom Dieck splitting.]]

## 3.3 Tannaka–Krein duality

We started by suggesting that we can study mathematical objects, such as groups G and rings R, by means of their categories of representations, such as the category${ \cal G } { - } { \bf S } { \bf e t }$of G-sets and the category R−Mod of R-modules. A natural question is then to what extent these representation categories determine the original object, i.e., can one recover the group G from the category G−Set, and can one recover the ring R from the category$R { \mathrm { - } } \mathbf { M o d } ?$

This discussion is not critical for the development of algebraic K-theory, but has played an important role in Grothendieck’s ideas about motives, and motivic cohomology is directly related to algebraic K-theory.

For compact abelian groups G, it sufices to consider the category of 1- dimensional complex G-representations$G \times \mathbb { C } \to \mathbb { C } ,$, or equivalently, the Pontryagin dual group$G ^ { \# } = \operatorname { H o m } ( G , \mathbb { T } )$. The group G is then recovered as the double dual group, since the natural homomorphism$\rho \colon G \to ( G ^ { \# } ) ^ { \# }$is an isomorphism.

For compact not-necessarily-abelian groups, a positive answer was given by Tadao Tannaka [64], showing that G can be recovered from the category G−Vec of complex G-representations, together with its forgetful functor ω to the category Vec of complex vector spaces. Conversely, Mark Grigorievich Krein [35] characterized the additional structures present on a category for it to be equivalent to a category of G-representations. The resulting equivalence, between compact groups$G$and such Tannakian categories is known as Tannaka–Krein duality.

We discuss the first part of this theory in the simpler case of discrete groups$G ,$ where it sufices to consider the category G−Set of discrete representations.

Definition 3.3.1 (Fiber functor). For a discrete group$G ,$, let the fiber functor

$$
\omega \colon G \text {- - Set} \to \text { Set }
$$

be the forgetful functor, that takes a G-set$X$(with implicit action$G \times X \to X )$ to the underlying set$\omega ( X )$. Let$\operatorname { A u t } ( \omega )$be the monoid of natural transformations

$$
\phi \colon \omega \Rightarrow \omega
$$

under composition. There is a homomorphism

$$
\tau \colon G \to \operatorname{Aut} (\omega)
$$

that takes$g \in G$to the natural transformation$\phi \ : = \ : \tau ( g )$with components $\phi _ { X } \colon \omega ( X ) \to \omega ( X )$given by the function$g \cdot ,$mapping$x \in \omega ( X )$to$g x \in \omega ( X )$ This is a natural transformation, since for each G-equivariant function$f \colon X \to$ $Y$the square

$$
\begin{array}{c} \omega (X) \xrightarrow {g \cdot} \omega (X) \\ \omega (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow \omega (f) \\ \omega (Y) \xrightarrow {g \cdot} \omega (Y) \end{array}
$$

commutes.

We can now recover$G$from the category G−Set, equipped with the fiber functor$\omega .$

Proposition 3.3.2. The homomorphism$\tau \colon G \to \operatorname { A u t } ( \omega )$is an isomorphism. In particular,$\operatorname { A u t } ( \omega )$is a group and every natural transformation$\phi \colon \omega \Rightarrow \omega$is a natural isomorphism.

Proof. We construct an inverse κ:$\operatorname { A u t } ( \omega )  G$to τ. Given a natural transformation$\phi \colon \omega \Rightarrow \omega .$, consider its component$\phi _ { G } \colon \omega ( G ) \to \omega ( G )$, at the G-set $X = G$, with the left action$G \times G \to G$given by the multiplication in$G .$. This component$\phi _ { G }$maps$e \in \omega ( G )$to some element$\phi _ { G } ( e ) \in \omega ( G )$. We define$\kappa ( \phi )$ to be this element:

$$
\kappa (\phi) = \phi_ {G} (e).
$$

For any$g \in G$it is clear that$\kappa \tau ( g ) = g e = g .$Conversely, consider any $\phi \in \operatorname { A u t } ( \omega )$. For each G-set$X ,$, and any element$x \in \omega ( X )$, there is a unique$G \mathrm { - }$ equivariant function$f \colon G \to X$with$f ( e ) = x$, given by the formula$f ( h ) = h x$ for$h \in G$. Chasing the element$e \in \omega ( G )$through the commutative diagram

$$
\begin{array}{c} \omega (G) \xrightarrow {\phi_ {G}} \omega (G) \\ \omega (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow \omega (f) \\ \omega (X) \xrightarrow {\phi_ {X}} \omega (X) \end{array}
$$

shows that$\phi _ { X } ( x ) = \phi _ { X } ( f ( e ) ) = f ( \phi _ { G } ( e ) ) = f ( g ) = g x$, so that$\phi _ { X } = g \cdot$·. Since this holds for all$X$, we see that$\phi = \tau \kappa ( \phi )$□

The terminology “fiber functor” is motivated by the following example.

Example 3.3.3. Let$\mathbf { C o v } ( X )$be the category of covering spaces$p \colon Y  X$ Given a point$x _ { 0 } \in X$, let the fiber functor

$$
\omega_ {x _ {0}} \colon \mathbf {C o v} (X) \to \mathbf {S e t}
$$

be the functor that takes$p \colon Y \to X$to the fiber$Y _ { x _ { 0 } } = p ^ { - 1 } ( x _ { 0 } )$over$x _ { 0 }$, and let $\mathrm { A u t } ( \omega _ { x _ { 0 } } )$be the monoid of natural transformations$\phi \colon \omega _ { x _ { 0 } } \Rightarrow \omega _ { x _ { 0 } }$. There is a homomorphism

$$
\tau \colon \pi_ {1} (X, x _ {0}) \to \mathrm{Aut} (\omega_ {x _ {0}})
$$

that takes the homotopy class$g = [ \gamma ]$of a based loop$\gamma \colon ( I , \partial I ) \to ( X , x _ { 0 } )$to the natural transformation$\phi = \tau ( g )$with components

$$
\phi_ {Y} \colon Y _ {x _ {0}} \to Y _ {x _ {0}}
$$

given as follows. For each point$y \in Y _ { x _ { 0 } }$let$\tilde { \gamma } \colon I  Y$be the unique path with $p \tilde { \gamma } = \gamma$and$\tilde { \gamma } ( 0 ) = y$. Then$\phi _ { Y } ( y ) = \tilde { \gamma } ( 1 )$. The endpoint of$\tilde { \gamma }$only depends on the homotopy class of$\gamma .$. This defines a natural transformation, since for another covering space$q \colon Z \to X$and a map$f \colon Y \to Z$with$q f = p$, the diagram

$$
\begin{array}{c} Y _ {x _ {0}} \xrightarrow {\phi_ {Y}} Y _ {x _ {0}} \\ f _ {x _ {0}} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow f _ {x _ {0}} \\ Z _ {x _ {0}} \xrightarrow {\phi_ {Z}} Z _ {x _ {0}} \end{array}
$$

commutes, since, with notation as above,$f { \tilde { \gamma } } \colon I \to Z$will be the unique lift of γ starting at$f ( y )$, and ends at$( f \tilde { \gamma } ) ( 1 ) = f ( \tilde { \gamma } ( 1 ) )$.

Proposition 3.3.4. Suppose that X at admits a simply-connected universal covering space${ \widetilde { X } } \to X$. Then the homomorphism$\tau \colon \pi _ { 1 } ( X , x _ { 0 } ) \to \mathrm { A u t } ( \omega _ { x _ { 0 } } )$is an isomorphism.

Proof. Fix a point$\tilde { x } _ { 0 } \in \tilde { X }$over$x _ { 0 } \in X$. The inverse κ :$\operatorname { A u t } ( \omega _ { x _ { 0 } } ) \to \pi _ { 1 } ( X , x _ { 0 } )$ etakes a natural transformation$\phi$to a group element$\kappa ( \phi ) \in \pi _ { 1 } ( X , x _ { 0 } )$defined as follows. Consider the component$\phi _ { \widetilde { X } } \colon \widetilde { X } _ { x _ { 0 } }  \widetilde { X } _ { x _ { 0 } }$of$\phi .$. It maps ˜x<sub>0</sub> to some point$\phi _ { \widetilde { X } } ( \tilde { x } _ { 0 } ) = \tilde { x }$e ein the same fiber. Choose a path$\tilde { \gamma }$in$\widetilde { X }$from$\tilde { x } _ { 0 }$to${ \tilde { x } } ,$and let$g = [ p \tilde { \gamma } ]$e be the homotopy class of its projection down to$X$. The choice of path ˜γ is unique up to homotopy, since$\widetilde { X }$is simply-connected.

[[Clear that$\kappa \tau ( g ) = g$e. Use existence of maps${ \widetilde { X } } \to Y$taking$\tilde { x } _ { 0 }$to any given point$y \in Y _ { x _ { 0 } }$to check that$\tau \kappa ( \phi ) = \phi . ] ]$□

[[Comparison with previous result. Dependence on$x _ { 0 } . ] ]$

Remark 3.3.5. By analogy, for a geometric point$x _ { 0 }$of a scheme$X ,$one can consider the category$\mathbf { E t } ( X )$of ´etale coverings$Y  X$, with fiber functor ω given by the pullback to$x _ { 0 }$. The (profinite) group of natural automorphisms of ω, is the ´etale fundamental group$\pi _ { 1 } ^ { e t } ( X , x _ { 0 } )$. [[Reference.]]

So far we have talked about ordinary categories and set-valued fiber functors. To cover the case of compact groups, Tannaka and Krein work with C-linear categories and a fiber functor to$\mathbb { C } \mathrm { - } \mathbf { V } \mathbf { e } \mathbf { c }$. In this form, the duality theory can be extended to algebraic groups, following Grothendieck.

We start with the so-called neutral case. For more details, including a sketch proof of the neutral duality theorem using the Barr–Beck theorem, see Breen [9].

Let$G$be an afine algebraic group defined over a field k. Let$\mathbf { R e p } ( G )$be the category of (finite-dimensional) of k-linear representations of$G .$. The tensor product$V \otimes _ { k } W$and internal Hom${ \mathrm { H o m } } _ { k } ( V , W )$of$G \mathrm { - }$-representations$V , W$ makes$\mathbf { R e p } ( G ) \mathrm { ~ a ~ }$“compact closed symmetric monoidal category”. The usual notion of a short exact sequence$0 \to V ^ { \prime } \to V \to V ^ { \prime \prime } \to 0$of G-representations makes$\mathbf { R e p } ( G )$an “abelian category”. Finally, the forgetful functor

$$
\omega \colon \operatorname{Rep} (G) \to k - \operatorname{Vec}
$$

respects the tensor structure. The k-linear tensor category$\mathbf { R e p } ( G )$, with this fiber functor$\omega ,$is then called a neutral Tannakian category. To recover$G$from $( \mathbf { R e p } ( G ) , \omega )$, one proves that the group$\operatorname { A u t } ( \omega )$of (tensor-preserving) natural transformations$\phi \colon \omega \Rightarrow \omega$is isomorphic to the group of k-valued points of$G ,$ and more generally there is an isomorphism

$$
G \cong \operatorname{Aut} (\omega)
$$

of group schemes.

In the more general, non-neutral case, one starts with a k-linear tensor category$\mathcal { C } .$, but with a fiber functor to$K \mathrm { - } \mathbf { V } \mathbf { e } \mathbf { c }$for some field extension K of$k .$ One is then instead to look at a gerbe G of all fiber functors, which is a stack, or sheaf of groupoids, of a particular kind. The automorphism group of the single fiber functor in the neutral case is now generalized to this groupoid. The duality theorem now asserts that a general Tannakian category$\mathcal { C }$is equivalent to a category of representations$\mathbf { R e p } ( \mathcal { G } )$of the corresponding gerbe$\mathcal { G }$

A key example of a Tannakian category is given by the category of motives over a finite field. [[How about motives over global fields?]] It is not neutral, and therefore corresponds to the category of representations of a gerbe, not just an algebraic group.

[[Motivic Galois group.]]

## 3.4 Adjoint pairs of functors

Dan Kan [33] recognized that there is a very useful generalization of a mutually inverse pair of equivalences$( F \colon \mathcal { C } \to \mathcal { D } , G \colon \mathcal { D } \to \mathcal { C } )$, called an adjoint pair of functors$( F \colon \mathcal { C } \to \mathcal { D } , G \colon \mathcal { D } \to \mathcal { C } )$. For example, this generalization gives a clear meaning to the notion of$\mathrm { a \ ^ { 6 6 } e e ^ { 9 } }$object in many contexts.

Definition 3.4.1 (Adjoint functors). Let$\mathcal { C } _ { : }$, D be categories and let$F \colon \mathcal { C }$ D and$G \colon { \mathcal { D } } \to { \mathcal { C } }$be functors. An adjunction between$F$and$G$is a natural bijection

$$
\phi_ {X, Y} \colon \mathcal {D} (F (X), Y) \xrightarrow {\cong} \mathcal {C} (X, G (Y))
$$

between the two set-valued bifunctors

$$
\mathscr {D} (F (-), -), \mathscr {C} (-, G (-)) \colon \mathscr {C} ^ {o p} \times \mathscr {D} \rightarrow \mathbf {S e t}.
$$

If such a natural bijection$\phi$exists, we say that$( F , G )$is an adjoint pair of functors.

We call$F$the left adjoint (or coadjoint), and G the right adjoint (or adjoint). Given morphisms$f \colon F ( X ) \to Y$in$\mathcal { D }$and$g \colon X \to G ( Y )$in$\mathcal { C } _ { : }$, related by $\phi _ { X , Y } ( f ) = g$, we say that$f$is left adjoint to g and$g$is right adjoint to$f .$

Naturality of the adjunction φ says that for morphisms c:$X ^ { \prime }  X , g \colon X$ $G ( Y )$in$\mathcal { C }$, and d:$Y  Y ^ { \prime } , f \colon F ( X )  Y$in$\mathcal { D }$, with$f$left adjoint to g, the composite d ◦$f \circ F ( c ) \colon F ( X ^ { \prime } ) \to Y ^ { \prime }$is left adjoint to the composite$G ( d ) \circ g$◦ c :$\bar { X ^ { \prime } }  G ( Y ^ { \prime } )$

$$
\begin{array}{c} \mathcal {D} (F (X), Y) \xrightarrow {\phi_ {X , Y}} \mathcal {C} (X, G (Y)) \\ c ^ {*} d _ {*} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow c ^ {*} d _ {*} \\ \mathcal {D} (F (X ^ {\prime}), Y ^ {\prime}) \xrightarrow {\phi_ {X ^ {\prime} , Y ^ {\prime}}} \mathcal {C} (X ^ {\prime}, G (Y ^ {\prime})) \end{array}
$$

Hence

$$
\phi_ {X ^ {\prime}, Y ^ {\prime}} (d \circ f \circ F (c)) = G (d) \circ \phi_ {X, Y} (f) \circ c.
$$

In particular,$\phi _ { X ^ { \prime } , Y } ( f \circ F ( c ) ) = \phi _ { X , Y } ( f )$◦ c and$\phi _ { X , Y ^ { \prime } } ( d \circ f ) = G ( d ) \circ \phi _ { X , Y } ( f )$

Remark 3.4.2. Note that the left adjoint$F$appears in the source in${ \mathcal { D } } ( F ( X ) , Y )$ while the right adjoint$G$appears in the target in${ \mathcal { C } } ( X , G ( Y ) )$. Given a functor $F \colon { \mathcal { C } } \to { \mathcal { D } } .$, for each object$Y$in$\mathcal { D }$the value$G ( Y )$of a right adjoint to$F$must be a representing object for the contravariant functor

$$
\mathscr {Y} _ {Y} \circ F \colon X \mapsto \mathscr {D} (F (X), Y)  ,
$$

which determines$G ( Y )$up to isomorphism. However, not every functor$F$ admits a right adjoint. Conversely, given a functor$G \colon { \mathcal { D } } \to { \mathcal { C } }$, for each object $X$in$\mathcal { C }$the value$F ( X )$of a left adjoint to$G$must be a corepresenting object for the (covariant) functor

$$
\mathcal {Y} ^ {X} \circ G \colon Y \mapsto \mathcal {C} (X, G (Y)),
$$

which determines$F ( X )$up to isomorphism. Again, not every functor$G$admits a left adjoint. In diagrams of adjoint pairs of functors, we put the left adjoint on the left hand side or on top:

$$
\begin{array}{c c c} \mathcal {C} & \mathcal {C} \xrightarrow [ G ]{F} \mathcal {D} \\ F \Biggl \downarrow \Biggl \uparrow G & \mathcal {D} \xleftarrow [ G ]{F} \mathcal {C} & \mathcal {D} \\ \mathcal {D} & \mathcal {D} \xrightarrow [ G ]{F} \mathcal {C} \end{array}
$$

The following examples show that a “free functor” can be interpreted as the left adjoint of a “forgetful functor”.

Example 3.4.3. The forgetful functor$U \colon \mathbf { G r p } \to \mathbf { S e t }$, taking a group$G$to its underlying set$U ( G )$, admits a left adjoint$F :$Set → Grp, taking a set$S$to the free group$F ( S ) = \langle s \in S \rangle$generated by S. The adjunction is the natural bijection

$$
\mathbf {G r p} (F (S), G) \cong \mathbf {S e t} (S, U (G))
$$

asserting that to give a group homomorphism$F ( S ) \to G$it is necessary and suficient to specify the function$S \to U ( G )$, saying where the group generators are sent.

$$
\text { Set } \xrightarrow [ U ]{F} \text { Grp }
$$

[[This forgetful functor does not admit a right adjoint.]]

Example 3.4.4. Let G be a group. The fiber functor$\omega \colon G { \mathrm { - } } \mathbf { S e t } \to \mathbf { S e t } .$, taking a G-set X to its underlying set$\omega ( X )$, admits a left adjoint G× : Set → G−Set, taking a set S to the free G-set$G \times S$generated by S, with the G-action given by$( g , ( h , s ) ) = ( g h , s )$. The adjunction is the natural bijection

$$
G - \mathbf {S e t} (G \times S, X) \cong \mathbf {S e t} (S, \omega (X))
$$

asserting that to give a G-equivariant function$G \times S \to X$it is necessary and suficient to specify the function$S \to \omega ( X )$, saying where the generators of the free G-set are sent.

The fiber functor ω also admits a left adjoint$\begin{array} { r } { \prod _ { G } \colon \mathbf { S e t } \longrightarrow G \mathrm { - } \mathbf { S e t } } \end{array}$, taking a set S to the G-set$\textstyle \prod _ { G } S = \mathbf { S e t } ( G , S )$, with the G-action given by$( g \cdot f ) ( k ) =$ $f ( k g )$for$k \in G$. The adjunction is the natural bijection

$$
\mathbf {S e t} (\omega (X), S) \cong G - \mathbf {S e t} (X, \prod_ {G} S)
$$

taking a function$\sigma \colon \omega ( X )  S$to the G-equivariant function$\tau \colon X \to \prod _ { G } S$ with values$\tau ( x ) \colon G \to S$given by$\tau ( x ) ( k ) = \sigma ( k \cdot x )$

$$
\mathbf {S e t} \xrightarrow [ \overrightarrow {\Pi_ {G}} ]{\stackrel {{G \times}} {{\longleftarrow \omega -}}} G \text {- - - Set}
$$

We generalize this example in Definition 3.4.19.

Example 3.4.5. Let R be a ring. The forgetful functor$U \colon R { \mathrm { - } } \mathbf { M o d } \$ Set, taking an R-module M its underlying set$U ( M )$, admits a left adjoint $R ( - ) \colon \mathbf { S e t } \to R { \mathrm { - } } \mathbf { M o d }$, taking a set S to the free R-module

$$
R (S) = R \{s \in S \} \cong \bigoplus_ {s \in S} R
$$

generated by S. The adjunction is the natural bijection

$$
R \text {- - } \mathbf {M o d} (R (S), M) \cong \mathbf {S e t} (S, U (M))
$$

asserting that to give an R-module homomorphism$R ( S )  M$it is necessary and suficient to specify the function$S \to U ( M )$, saying where the R-module generators are sent.

$$
\text { Set } \xrightarrow [ U ]{R (-)} R \text {- - Mod}
$$

[[This forgetful functor does not admit a right adjoint.]]

One may also forget less structure.

Example 3.4.6. The abelianization functor$( - ) ^ { a b } \colon { \bf G r p }  { \bf A b }$is left adjoint to the forgetful functor$U \colon \mathbf { A b }  \mathbf { G r p }$. This is because giving an (abelian) group homomorphism$G ^ { a b }  A$is equivalent to giving a group homomorphism $G \to U ( A )$. [[This forgetful functor U has no right adjoint.]]

Example 3.4.7. Let CMon be the full subcategory of Mon generated by the commutative monoids. The group completion functor$K \colon \mathbf { C M o n }  \mathbf { A }$b is left adjoint to the forgetful functor$U \colon \mathbf { A b } \to \mathbf { C M o n }$. This is because giving a group homomorphism$K ( M ) \to A$is equivalent to giving a monoid homomorphism $M \to U ( A )$

This forgetful functor U has a right adjoint$( - ) ^ { \times } \colon \mathbf { C M o n } \ \to \ \mathbf { A b }$, taking M to the submonoid$M ^ { \times }$of invertible elements in M, which forms an abelian group. Each monoid homomorphism$U ( A ) \to M$factors uniquely through a group homomorphism$A \to M ^ { \times }$

Definition 3.4.8 (Group completion, units). In the non-commutative case, the forgetful functor$U \colon \mathbf { G r p } \to$Mon also has a left adjoint$K \colon \mathbf { M o n }  \mathbf { G r p } .$ the group completion of non-commutative monoids. Given a monoid M we can describe the group$K ( M )$in terms of generators and relations as

$$
K (M) = \langle [ x ] \mid [ x ] [ y ] = [ x y ] \rangle .
$$

In words, we start with one generator$[ x ]$for each element$x \in M .$, and add the relation$[ x ] [ y ] = [ x y ]$for each pair of elements$x , y \in M$. Here$[ x ] [ y ]$is the product in the free group generated by the elements of$M$, and xy is the product in M. The relation$[ e ] = e$follows. The adjunction

$$
\mathbf {G r p} (K (M), G) \cong \mathbf {M o n} (M, U (G))
$$

takes a group homomorphism$f \colon K ( M ) \to G$to the monoid homomorphism $g \colon M \to U ( G )$given by$g ( x ) = f ( [ x ] )$, and conversely. Later, we shall see that $K ( M )$is topologically realized as$\pi _ { 1 } ( B M )$, where the classifying space BM contains a closed loop [x] for each$x \in M$, and a triangle$[ x | y ]$with edges [x], [y] and$[ x y ]$for each$x , y \in M$

This forgetful functor U also has a right adjoint$( - ) ^ { \times }$:$\mathbf { M o n } \longrightarrow \mathbf { G r p } ,$again taking a monoid M to the submonoid$M ^ { \times }$of invertible elements, which is a group.

Definition 3.4.9 ((Co-)reflective subcategory). A subcategory${ \mathcal { C } } \subseteq { \mathcal { D } }$is called reflective when the inclusion functor$U \colon { \mathcal { C } } \to { \mathcal { D } }$is a right adjoint,$\mathrm { i . e . }$ it admits a left adjoint$F \colon { \mathcal { D } }  { \mathcal { C } }$. It is called coreflective when$U$is a left adjoint, i.e., it admits a right adjoint$G \colon { \mathcal { D } } \to { \mathcal { C } }$

We often omit forgetful functors like U from the notation.

Example 3.4.10. CMon$\subset \mathbf { \Delta A b }$CMon ⊂ Mon,$\mathbf { A b } \subset \mathbf { G r p }$and Mon$\subset$ Grp are reflective subcategories.$\mathbf { C M o n } \subset \mathbf { A b }$and Mon${ \mathsf { \subset G r p } }$are also coreflective subcategories.

![](images/page_77_image_1.jpg)

Example 3.4.11. The full inclusion$\mathbf { G p d } \subset \mathbf { C a t }$is both reflective and coreflective. It has right adjoint the maximal subgroupoid functor iso: Cat → Gpd of Definition 2.4.10, left adjoint the localization functor L: Cat → Gpd of Definition 2.4.19, with$L ( \mathcal { C } ) = \mathcal { C } [ \mathcal { C } ^ { - 1 } ]$

$$
\mathrm{Cat} \xrightarrow [ \text {iso} ]{\stackrel {{L}} {\longrightarrow}} \mathrm{Gpd}
$$

since

$$
\mathbf {C a t} (\mathcal {D}, \mathcal {C}) \cong \mathbf {G p d} (\mathcal {D}, \mathrm{iso} (\mathcal {C})
$$

by Lemma 2.4.17 and

$$
\mathbf {G p d} (\mathcal {C} [ \mathcal {C} ^ {- 1} ], \mathcal {D}) \cong \mathbf {C a t} (\mathcal {C}, \mathcal {D})
$$

by Lemma 2.4.21, for small categories$\mathcal { C }$and groupoids${ \mathcal { D } } .$

Exercise 3.4.12. Which of the inclusions among the full subcategories of Cat displayed in diagrams (2.1) and (2.2) are (co-)reflective?

Lemma 3.4.13. Consider categories$\mathcal { C } , \mathcal { D } , \mathcal { E }$and functors$F , G , H , K$, as below:

$$
\mathcal {C} \xrightarrow [ G ]{F} \mathcal {D} \xrightarrow [ K ]{H} \mathcal {E}
$$

Let$\phi _ { X , Y } \colon { \mathcal { D } } ( F ( X ) , Y ) \cong { \mathcal { C } } ( X , G ( Y ) )$be an adjunction between$F$and$G _ { i }$, and let$\psi _ { Y , Z } \colon \mathcal { E } ( H ( Y ) , Z ) \cong \mathcal { D } ( Y , K ( Z ) )$be an adjunction between H and$K$. Then

$$
(\phi \psi) _ {X, Z} = \phi_ {X, K (Z)} \circ \psi_ {F (X), Z} \colon \mathcal {E} (H F (X), Z) \cong \mathcal {C} (X, G K (Z))
$$

is an adjunction between$H F$and$G K$, called the composite adjunction.

[[Proof omitted.]]

Definition 3.4.14 ((Co-)unit morphism). Associated to an adjunction

$$
\phi_ {X, Y} \colon \mathcal {D} (F (X), Y) \xrightarrow {\cong} \mathcal {C} (X, G (Y))
$$

there is a natural unit morphism

$$
\eta_ {X} \colon X \to G F (X)
$$

in$\mathcal { C }$, right adjoint to the identity morphism of$F ( X )$in${ \mathcal { D } } _ { : }$, and a natural counit morphism

$$
\epsilon_ {Y} \colon F G (Y) \to Y
$$

in${ \mathcal { D } } .$, left adjoint to the identity morphism of$G ( Y )$in$\mathcal { C }$. Hence$\eta _ { X } ~ =$ $\phi _ { X , F ( X ) } ( i d _ { F ( X ) } )$and$\epsilon _ { Y } = \phi _ { G ( Y ) , Y } ^ { - 1 } ( i d _ { G ( Y ) } )$

Remark 3.4.15. The use of the letters η and ǫ for units and counits of adjunctions is standard. We can reformulate an adjunction entirely in terms of its unit and counit.

Lemma 3.4.16. Given an adjunction$\phi ,$the unit morphisms$\eta _ { X }$for$X$in$\mathcal { C }$ define a natural transformation

$$
\eta \colon i d _ {\mathcal {C}} \Rightarrow G F
$$

of functors$\mathcal { C } \to \mathcal { C }$, while the counit morphisms$\epsilon _ { Y }$for$Y$in$\mathcal { D }$define a natural transformation

$$
\epsilon \colon F G \Rightarrow i d _ {\mathscr {D}}
$$

of functors$\mathcal { D }  \mathcal { D }$. The composite natural transformation

$$
\epsilon_ {F} \circ F \eta \colon F \Rightarrow F G F \Rightarrow F
$$

with components$\epsilon _ { F ( X ) } \circ F ( \eta _ { X } )$equals the identity transformation$i d _ { F }$, and the composite natural transformation

$$
G \epsilon \circ \eta_ {G} \colon G \Rightarrow G F G \Rightarrow G
$$

with components$G \bigl ( \epsilon _ { Y } \bigr ) \circ \eta _ { G ( Y ) }$equals the identity transformation$i d _ { G }$

Proof. To check that$\eta _ { X }$is natural in$X$, we must see that for each morphism $f \colon X \to X ^ { \prime }$in$\mathcal { C }$the square

$$
\begin{array}{c} X \xrightarrow {\eta_ {X}} G F (X) \\ f \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow_ {G F (f)} \\ X ^ {\prime} \xrightarrow {\eta_ {X ^ {\prime}}} G F (X ^ {\prime}) \end{array}
$$

commutes. By naturality of the adjunction$\phi ,$this is equivalent [[More details?]] to the commutativity of the square

$$
\begin{array}{c} F (X) \xrightarrow {i d _ {F (X)}} F (X) \\ F (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow F (f) \\ F (X ^ {\prime}) \xrightarrow {i d _ {F (X ^ {\prime})}} F (X), \end{array}
$$

which is clear. The proof that$\epsilon _ { Y }$is natural in$Y$is very similar.

For each$X$in$\mathcal { C }$, the composite map

$$
F (X) \stackrel {{F (\eta_ {X})}} {{\longrightarrow}} F G F (X) \stackrel {{\epsilon_ {F (X)}}} {{\longrightarrow}} F (X)
$$

has right adjoint the composite

$$
X \xrightarrow {\eta_ {X}} G F (X) \stackrel {i d _ {G F (X)}} {\longrightarrow} G F (X),
$$

$$
X \xrightarrow {\eta_ {X}} G F (X) \stackrel {{G (i d _ {F (X)})}} {{\longrightarrow}} G F (X),
$$

by naturality of$\phi$with respect to$\eta _ { X }$. We rewrite this as the composite

which has left adjoint the composite

$$
F (X) \stackrel {{i d _ {F (X)}}} {{\longrightarrow}} F (X) \stackrel {{i d _ {F (X)}}} {{\longrightarrow}} F (X)
$$

by naturality of$\phi$with respect to$i d _ { F ( X ) }$. Since the left adjoint of the right adjoint of a morphism is the original morphism, this proves that$\epsilon _ { F ( X ) } \circ F ( \eta _ { X } ) =$ $i d _ { F ( X ) }$. The proof that$G ( \epsilon _ { Y } ) \circ \eta _ { G ( Y ) } = i d _ { G ( Y ) }$is very similar.□

Lemma 3.4.17. Conversely, given functors$F \colon \mathcal { C } \to \mathcal { D } , G \colon \mathcal { D } \to \mathcal { C }$and natural transformations$\eta \colon i d _ { \mathcal { C } } \Rightarrow G F$, ǫ :$F G \Rightarrow i d _ { \mathcal { D } }$such that$\epsilon _ { F } \circ F \eta = i d _ { F }$，$G \epsilon \circ \eta _ { G } = i d _ { G }$, there is a unique adjunction

$$
\phi \colon \mathscr {D} (F (-), -) \stackrel {\cong} {\Longrightarrow} \mathscr {C} (-, G (-))
$$

with unit$\eta$and counit ǫ. For this adjunction, a map$f \colon F ( X ) \to Y$has right adjoint$\phi _ { X , Y } ( f ) \colon X \to G ( Y )$equal to the composite

$$
X \xrightarrow {\eta_ {X}} G F (X) \xrightarrow {G (f)} G (Y)
$$

and a map$g \colon X \to G ( Y )$has$l e f t$adjoint$\phi _ { X , Y } ^ { - 1 } ( g ) \colon F ( X ) \to Y$equal to the composite

$$
F (X) \xrightarrow {F (g)} F G (Y) \xrightarrow {\epsilon_ {Y}} Y.
$$

Proof. The right adjoint of$i d _ { F ( X ) }$must be$\eta _ { X } .$, and the formula for$\phi _ { X , Y } ( f )$ is then forced by naturality. Conversely the left adjoint of$i d _ { G ( Y ) }$must be$\epsilon _ { Y } .$ and$\phi _ { X , Y } ^ { - 1 } ( g )$is then determined by naturality. It remains to verify that the resulting functions$\phi _ { X , Y }$and$\phi _ { X , Y } ^ { - 1 }$are indeed mutual inverses. One composite takes$f \colon F ( X ) \to Y$to the composite

$$
F (X) \stackrel {{F (\eta_ {X})}} {{\longrightarrow}} F G F (X) \stackrel {{F G (f)}} {{\longrightarrow}} F G (Y) \stackrel {{\epsilon_ {Y}}} {{\longrightarrow}} Y,
$$

which by naturality of ǫ equals the composite

$$
F (X) \stackrel {F (\eta_ {X})} {\longrightarrow} F G F (X) \stackrel {\epsilon_ {F (X)}} {\longrightarrow} F (X) \stackrel {f} {\longrightarrow} Y,
$$

which in turn equals$f ,$since$\epsilon _ { F ( X ) } \circ F ( \eta _ { X } )$is assumed to be$i d _ { F ( X ) }$. The proof that the other composite takes$g \colon X \to G ( Y )$to itself is very similar.□

Example 3.4.18. Suppose that$( F , G )$is an adjoint pair of functors between two groupoids$\mathcal { C }$and$\mathcal { D }$. Then the unit and counit transformations$\eta \colon i d _ { \mathcal { C } } \Rightarrow$ $G F$and$\epsilon \colon F G \Rightarrow i d _ { \mathcal { D } }$are natural isomorphisms, hence$F$and$G$are inverse equivalences.

[[Mutually inverse equivalences of categories are adjoint.]] [[Uniqueness of adjoints.]]

Definition 3.4.19 ((Co-)induced G-sets). Let$\alpha \colon G \to H$be a group homomorphism. There is a functor$\alpha ^ { * } \colon H { \mathrm { - } } \mathbf { S e t } \longrightarrow G { \mathrm { - } } \mathbf { S e t }$that takes a (left) H-set Y to the (left) G-set$\alpha ^ { * } ( Y )$, with the same underlying set as$Y$, but with action the composite function$\boldsymbol { G } \times \boldsymbol { Y } \stackrel { \alpha \times i d } { \longrightarrow } \boldsymbol { H } \times \boldsymbol { Y } \longrightarrow \boldsymbol { Y }$. We view H as a left G-set, and as a right G-set, using α and the group multiplication in H. The functor $\alpha ^ { * }$has a left adjoint$\alpha _ { * } \colon G { \mathrm { - } } \mathbf { S e t } \longrightarrow H -$Set taking an G-set X to the H-set

$$
\alpha_ {*} (X) = H \times_ {G} X,
$$

with action the function$H \times H \times _ { G } X \stackrel { \mu \times _ { G } i d } { \longrightarrow } H \times _ { G } X$. Here$H \times _ { G } X$denotes the balanced product$( H \times X ) / { \sim }$, where$( h \cdot g , x ) \sim ( h , g \cdot x )$for$h \in H , g \in G$and $x \in X$. The functor$\alpha ^ { * }$also has a right adjoint$\alpha _ { ! } \colon G { \mathrm { - } } \mathbf { S e t } \longrightarrow H { \mathrm { - } } \mathbf { S e t }$taking an G-set X to the H-set

$$
\alpha_ {!} (X) = G \text {- - - } \mathbf {S e t} (H, X),
$$

of G-equivariant functions$f \colon H \to X$. The H-action

$$
H \times G - \operatorname{Set} (H, X) \longrightarrow G - \operatorname{Set} (H, X)
$$

on$\alpha _ { ! } ( X )$takes$( h , f )$for$h \in H , f \in G { - } \mathbf { S e t } ( H , X )$to the$G \mathrm { . }$-equivariant function$k \mapsto f ( k h )$, for$k \in H$

$$
G \text {- - - Set} \xrightarrow [ \alpha_ {!} ]{\alpha_ {*}} H \text {- - - Set}
$$

The adjunction bijections are:

$$
\begin{array}{l} H \text {- - Set} (\alpha_ {*} (X), Y) \cong G \text {- - Set} (X, \alpha^ {*} (Y)) \\ G \text {- - Set} (\alpha^ {*} (Y), X) \cong H \text {- - Set} (Y, \alpha_ {!} (X)) \end{array}
$$

Example 3.4.20. When$\alpha \colon \{ e \}  H$is the inclusion of the trivial subgroup, $\alpha ^ { * } \colon H { - } \mathbf { S e t } \ \to \ \mathbf { S e t }$is the forgetful functor, equal to the fiber functor ω of Definition 3.3.1, the left adjoint α takes a set X to the free H-set$\alpha _ { * } ( X ) =$ $H \times X$, and the right adjoint α takes a set X to the cofree H-set$\alpha _ { ! } ( X ) = \prod _ { H } X$2 as discussed in Example 3.4.4.

Example 3.4.21. When α:$G  \{ e \}$is the projection to the trivial group, $\alpha ^ { * } \colon \mathbf { S e t } \to G { \mathrm { - } } \mathbf { S e t }$takes a set$X$to the same set$\alpha ^ { * } ( X )$, with the trivial$G \mathrm { - }$ action. The left adjoint$\alpha _ { * }$takes an G-set Y to the orbit set

$$
\alpha_ {*} (Y) = \{e \} \times_ {G} Y \cong Y / G.
$$

The right adjoint α<sub>!</sub> takes$Y$to the fixed point set

$$
\alpha_ {!} (Y) = G - \mathbf {S e t} (\{e \}, Y) \cong Y ^ {G}.
$$

See Definition 2.7.3 for this terminology.

Definition 3.4.22 (Direct and exceptional direct image). Let$\phi \colon R \to T$ be a ring homomorphism. There is a functor$\phi ^ { * } \colon T { \bf - M o d } \longrightarrow R { \bf - M o d }$that takes a (left)$T -$-module N to the (left) R-module$\phi ^ { * } ( N )$, with the same underlying abelian group as N, but with module action the composite homomorphism $R \otimes N \stackrel { \phi \otimes i d } { \longrightarrow } T \otimes N \longrightarrow N$. We view$T$as a left R-module and as a right R-module using the homomorphism$\phi$and the ring multiplication$\mu \colon T \otimes T \to T$. The functor$\phi ^ { * }$has a left adjoint$\phi _ { * } \colon R { \mathrm { - M o d } } \longrightarrow T -$Mod taking an R-module M to the T-module

$$
\phi_ {*} (M) = T \otimes_ {R} M,
$$

with module action the homomorphism$T \otimes T \otimes _ { R } M \stackrel { \mu \otimes _ { R } i d } { \longrightarrow } T \otimes _ { R } M$. The functor $\phi ^ { * }$also has a right adjoint$\phi _ { ! } \colon R { \mathrm { - M o d } } \longrightarrow T { \mathrm { - M o d } }$taking an R-module M to the$T -$-module

$$
\phi_ {!} (M) = _ {R} \mathrm{Hom} (T, M),
$$

of R-module homomorphisms$f \colon T \to M$, where$T$is viewed as an R-module by the action$R \otimes T { \stackrel { \phi \otimes i d } { \longrightarrow } } T \otimes T { \stackrel { \mu } { \longrightarrow } } T$. The T-module structure

$$
T \otimes_ {R} \mathrm{Hom} (T, M) \longrightarrow {} _ {R} \mathrm{Hom} (T, M)
$$

on$\phi _ { ! } ( M )$takes$t \otimes f$for$t \in T , f \in _ { R } { \mathrm { H o m } } ( T , M )$to the R-module homomorphism$u \mapsto f ( u t )$, for$u \in T$

$$
R \text {- - Mod} \xrightarrow [ \phi_ {!} ]{\phi_ {*}} T \text {- - Mod}
$$

Both adjunctions

$$
\begin{array}{l} T \text {- - Mod} (\phi_ {*} (M), N) \cong R \text {- - Mod} (M, \phi^ {*} (N)) \\ R \text {- - Mod} (\phi^ {*} (N), M) \cong T \text {- - Mod} (N, \phi_ {!} (M)) \end{array}
$$

respect the additive structure, hence lift to group isomorphisms

$$
\begin{array}{c} _ {T} \mathrm{Hom} (T \otimes_ {R} M, N) \cong {} _ {R} \mathrm{Hom} (M, \phi^ {*} (N)) \\ _ {R} \mathrm{Hom} (\phi^ {*} (N), M) \cong {} _ {T} \mathrm{Hom} (N, _ {R} \mathrm{Hom} (T, M)). \end{array}
$$

[[Warning: For$R , ~ T$commutative,$\phi$defines a morphism$f \colon \mathrm { S p e c } ( T ) \$ ${ \mathrm { S p e c } } ( R )$of schemes, and the induced functors inverse image$f ^ { * } = \phi _ { * }$, direct image$f _ { * } = \phi ^ { * }$and exceptional inverse image$f ^ { ! } = \phi !$on quasi-coherent sheaves. Note the reversal in variance.]]

## 3.5 Decategorification

Definition 3.5.1. Let$\mathcal { C }$be a small groupoid. We can define an equivalence relation$\cong$on the set of objects,$\operatorname { o b j } ( { \mathcal { C } } )$, by saying that$X \cong Y$if there exists a morphism (= an isomorphism)$f \colon X \xrightarrow { \cong } Y$from$X$to$Y$in$\mathcal { C }$. The fact that this is an equivalence relation follows easily from Lemma 2.4.3. Let the set of equivalence classes

$$
\pi_ {0} (\mathcal {C}) = \mathrm{obj} (\mathcal {C}) / \cong
$$

be the set of isomorphism classes of objects in$\mathcal { C } .$. We write$[ X ] \in \pi _ { 0 } ( \mathcal { C } )$for the isomorphism class of an object$X$in$\mathcal { C }$. By definition,$[ X ] = \{ Y \in \mathrm { o b j } ( \mathcal { C } )$| $X \cong Y \}$

Remark 3.5.2. Since the equivalence relation$X \cong Y$only remembers the existence of isomorphisms from X to Y in$\mathcal { C }$, not the actual nonempty set of isomorphisms${ \mathcal { C } } ( X , Y )$, the set$\pi _ { 0 } ( \mathcal { C } )$of isomorphism classes in$\mathcal { C }$has lost track of part of the categorical structure. We therefore refer to$\pi _ { 0 } ( \mathcal { C } )$as the decategorification of$\mathcal { C }$. An important aspect of algebraic K-theory is a reversal of this process, attempting to lift set level structures to the category level, by a less well-defined process of categorification.

Example 3.5.3. Let$\mathbb { N } _ { 0 } = \{ 0 , 1 , 2 , \dots \}$be the set of non-negative integers. There is a bijection

$$
\pi_ {0} (\mathrm{iso} (\mathcal {F})) \xrightarrow {\cong} \mathbb {N} _ {0}
$$

that takes the object n to its cardinality$n ,$, for each$n \geq 0$

Remark 3.5.4. Under the bijection above, the disjoint union m ⊔ n and the cartesian product m × n give categorical models for the sum$m + n$and product mn of non-negative integers. In a sense, the need to count the number of elements in the sets arising from these operations must have been one of the initial reasons for introducing sums and products of natural numbers. Once bookkeeping developed, it proved convenient to also introduce negative numbers, extending the number system from${ \mathbb { N } } _ { 0 }$to the integers$\mathbb { Z } = \{ \dots , - 1 , 0 , 1 , \dots \}$ There are no sets with a negative number of elements, but what is a suitable extension the groupoid$\mathrm { i s o } ( \mathcal { F } )$, so that its$\pi _ { 0 }$is naturally the ring of integers? [[We will return to this in??]]

Definition 3.5.5. Let$\mathcal { C } , \mathcal { D }$be small groupoids, and$F \colon \mathcal { C }  \mathcal { D } :$a functor. We define a function

$$
\pi_ {0} (F) \colon \pi_ {0} (\mathcal {C}) \longrightarrow \pi_ {0} (\mathcal {D})
$$

by mapping the isomorphism class$[ X ]$to the isomorphism class$[ F ( X ) ]$]. This is well defined, since$F$maps isomorphic objects to isomorphic objects. It is clear that$\pi _ { 0 } ( i d \mathcal { \epsilon } ) = i d _ { \pi _ { 0 } ( \mathcal { C } ) }$and$\pi _ { 0 } ( G \circ F ) = \pi _ { 0 } ( G ) \circ \pi _ { 0 } ( F )$, if$G \colon { \mathcal { D } } \to { \mathcal { E } }$is a second functor between small groupoids, so we have defined a functor

$$
\pi_ {0} \colon \mathbf {G p d} \longrightarrow \mathbf {S e t}.
$$

Definition 3.5.6. We now generalize the above constructions to the case when $\mathcal { C }$is any small category. We define a relation ∼ on its set of objects by saying that$X \sim Y$if there exists a morphism$f \colon X \to Y$from X to$Y$in$\mathcal { C } .$. This relation is reflexive and transitive, but not symmetric. However, ∼ generates a well-defined equivalence relation$\simeq \mathrm { o n \ o b j } ( \mathcal { C } )$, namely the smallest equivalence relation (when viewed as a subset of$\mathrm { o b j } ( \mathcal { C } ) \times \mathrm { o b j } ( \mathcal { C } ) \rangle$that contains$\sim$. More explicitly, for two objects$X , Y$in$\mathcal { C }$, we have$X \simeq Y$if and only if there exists a finite sequence of objects

$$
X = Z _ {0}, Z _ {1}, \dots , Z _ {m - 1}, Z _ {m} = Y
$$

in$\mathcal { C } _ { : }$, with$m \geq 1$, where$Z _ { i - 1 } \sim Z _ { i }$or$Z _ { i } \sim Z _ { i - 1 }$(or both) for each$1 \leq i \leq m$ This makes ≃ an equivalence relation on$\operatorname { o b j } ( { \mathcal { C } } )$, and we define

$$
\pi_ {0} (\mathcal {C}) = \mathrm{obj} (\mathcal {C}) / \simeq
$$

to be the set of equivalence classes. In this generality we say that$X$and$Y$are homotopic when$X \simeq Y$, and we call$\pi _ { 0 } ( \mathcal { C } )$the set of path components of$\mathcal { C }$

Let$[ X ] = \{ Y \in \mathrm { o b j } ( { \mathcal { C } } ) | X \simeq Y \}$denote the (object level) path component of $X$in$\mathcal { C } .$. [[We may also refer to the full subcategory of$\mathcal { C }$generated by$[ X ]$as a path component of C .]] There is of course a relation between this notation and that of Definition 2.5.13, which we will make clear in ? [[Forward reference to nerve and classifying space of category.]]

Lemma 3.5.7. Two objects X, Y in$\mathcal { C }$represent the same element in$\pi _ { 0 } ( \mathcal { C } )$ $i f$and only if their images in$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$are isomorphic. Hence

$$
\pi_ {0} (\mathcal {C}) = \mathrm{obj} (\mathcal {C}) / \simeq
$$

is naturally identified with

$$
\pi_ {0} (\mathcal {C} [ \mathcal {C} ^ {- 1} ]) = \mathrm{obj} (\mathcal {C} [ \mathcal {C} ^ {- 1} ]) / {\cong}.
$$

Proof. If$X \simeq Y$, there exists a finite chain of objects$X = Z _ { 0 } , Z _ { 1 } , \ldots , Z _ { m } = Y$ and morphisms$f _ { i } \colon Z _ { i - 1 } \to Z _ { i }$or$f _ { i } \colon Z _ { i } \to Z _ { i - 1 }$for$1 \leq i \leq m$. Letting$\epsilon _ { i } = + 1$ $\mathrm { o r } \_ 1$according to the case, the resulting word$( f _ { m } ^ { \epsilon _ { m } } , \ldots , f _ { 1 } ^ { \epsilon _ { 1 } } )$determines an isomorphism in$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$from X to$Y$. Conversely, an isomorphism in$\mathcal { C } [ \mathcal { C } ^ { - 1 } ]$ from$X$to$Y$is determined by such a word, in which case the chain of relations $Z _ { i - 1 } \sim Z _ { i }$or$Z _ { i } \sim Z _ { i - 1 }$implies that$X \simeq Y$□

Definition 3.5.8. Let$\mathcal { C } , \mathcal { D }$be small categories, and let$F \colon \mathcal { C } \ \to \ \mathcal { D }$be a functor. We define a function

$$
\pi_ {0} (F) \colon \pi_ {0} (\mathcal {C}) \longrightarrow \pi_ {0} (\mathcal {D})
$$

by mapping$[ X ]$to$[ F ( X ) ]$, for each$X$in$\operatorname { o b j } ( { \mathcal { C } } )$. If$X \simeq Y$there exists a finite chain of morphisms in$\mathcal { C }$connecting X to$Y$, and applying$F$we obtain a finite chain of morphisms in$\mathcal { D }$connecting$F ( X )$to$F ( Y )$, so$F ( X ) \simeq F ( Y )$ Alternatively, we may note that$F$induces a functor$F \colon { \mathcal { C } } [ { \mathcal { C } } ^ { - 1 } ] \to { \mathcal { D } } [ { \mathcal { D } } ^ { - 1 } ]$of groupoids, and appeal to Definition 3.5.5. Either way,$\pi _ { 0 } ( F )$is well-defined, and defines a decategorification functor

$$
\pi_ {0} \colon \mathbf {C a t} \longrightarrow \mathbf {S e t}
$$

extending the previously defined functor on Gpd.

Lemma 3.5.9. Let C, D be small categories, let$F , G \colon \mathcal { C } \to \mathcal { D }$be functors, and let$\phi \colon F \Rightarrow G$be a natural transformation. Then the two functions

$$
\pi_ {0} (F), \pi_ {0} (G) \colon \pi_ {0} (\mathcal {C}) \longrightarrow \pi_ {0} (\mathcal {D})
$$

are equal.

Proof. The two functions$\pi _ { 0 } ( F )$and$\pi _ { 0 } ( G )$take$[ X ]$in$\pi _ { 0 } ( \mathcal { C } )$to$[ F ( X ) ]$and $\left[ G ( X ) \right]$in$\pi _ { 0 } ( \mathcal { D } )$, respectively. The natural morphism

$$
\phi_ {X} \colon F (X) \longrightarrow G (X)
$$

in$\mathcal { D }$tells us that$F ( X ) \sim G ( X )$, hence$F ( X ) \simeq G ( X )$and$[ F ( X ) ] = [ G ( X ) ] .$ In other words, the two functions$\pi _ { 0 } ( F )$and$\pi _ { 0 } ( G )$are equal.□

Lemma 3.5.10. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be an equivalence of small categories. Then

$$
\pi_ {0} (F) \colon \pi_ {0} (\mathcal {C}) \xrightarrow {\cong} \pi_ {0} (\mathcal {C})
$$

is a bijection.

Proof. Let$G \colon { \mathcal { D } } \to { \mathcal { C } }$be an inverse equivalence. Then there are natural isomorphisms φ :$G F { \stackrel { \cong } { \Longrightarrow } } i d _ { \mathcal { D } }$and$\psi \colon F G \stackrel { \cong } { \Longrightarrow } i d _ { \mathcal { C } } \mathrm { , s o } \pi _ { 0 } ( G ) \circ \pi _ { 0 } ( F ) = i d _ { \pi _ { 0 } ( \mathcal { C } ) }$and $\pi _ { 0 } ( F ) \circ \pi _ { 0 } ( G ) = i d _ { \pi _ { 0 } ( { \mathcal D } ) }$, by Lemma 3.5.9, hence$\pi _ { 0 } ( F )$is a bijection.□

Remark 3.5.11. For groupoids$\mathcal { C } , \mathcal { D }$this is a reasonable result, but for categories$\mathcal { C } , \mathcal { D }$less than an equivalence of categories is needed, since we might replace φ and$\psi$by (finite chains of) natural transformations. For example, it we get the same conclusion if$F$and G form an adjoint pair of functors.

Definition 3.5.12. Let$\mathcal { C }$be a category with a small skeleton$\mathcal { C } ^ { \prime }$. We define $\pi _ { 0 } ( \mathcal { C } )$to be the set$\pi _ { 0 } ( \mathcal { C } ^ { \prime } )$. Given a second choice of small skeleton$\mathcal { C } ^ { \prime \prime }$, there is a preferred bijection

$$
\pi_ {0} (\mathcal {C} ^ {\prime}) \stackrel {\cong} {\longrightarrow} \pi_ {0} (\mathcal {C} ^ {\prime \prime})
$$

taking$[ X ^ { \prime } ]$to$[ X ^ { \prime \prime } ] .$, where$X ^ { \prime \prime }$is the unique object in$\mathcal { C } ^ { \prime \prime }$that is isomorphic in$\mathcal { C }$to the object$X ^ { \prime }$in$\mathcal { C } ^ { \prime }$. If$\mathcal { C } ^ { \prime } = \mathcal { C } ^ { \prime \prime }$, the preferred bijection is the identity. Given a third choice of small skeleton$\mathcal { C } ^ { \prime \prime \prime }$, the composite of the pre-ferred bijections$\pi _ { 0 } ( \mathcal { C } ^ { \prime } ) \stackrel { \cong } { \longrightarrow } \pi _ { 0 } ( \mathcal { C } ^ { \prime \prime } ) \stackrel { \cong } { \longrightarrow } \pi _ { 0 } ( \mathcal { C } ^ { \prime \prime \prime } )$equals the preferred bijection $\pi _ { 0 } ( \mathcal { C } ^ { \prime } ) \stackrel { \cong } { \longrightarrow } \pi _ { 0 } ( \mathcal { C } ^ { \prime \prime \prime } )$. Hence the set$\pi _ { 0 } ( \mathcal { D } )$is well-defined up to a “coherently” unique isomorphism.

Let$\mathcal { C } , \mathcal { D }$be skeletally small categories, and let$F \colon \mathcal { C }  \mathcal { D }$be a functor. Choose small skeleta$\mathcal { C } ^ { \prime } \subseteq \mathcal { C }$and$\mathcal { D } ^ { \prime } \subseteq \mathcal { D }$. Then$\pi _ { 0 } ( \mathcal { C } ) = \pi _ { 0 } ( \mathcal { C } ^ { \prime } )$and$\pi _ { 0 } ( \mathcal { D } ) =$ $\pi _ { 0 } ( \mathcal { D } ^ { \prime } )$, and we define

$$
\pi_ {0} (F) \colon \pi_ {0} (\mathcal {C}) \longrightarrow \pi_ {0} (\mathcal {D})
$$

to be the function$\pi _ { 0 } ( \mathcal { C } ^ { \prime } ) \to \pi _ { 0 } ( \mathcal { D } ^ { \prime } )$that takes$[ X ^ { \prime } ]$to$[ Y ^ { \prime \prime } ]$, where$Y ^ { \prime \prime }$is the unique object in$\mathcal { D } ^ { \prime }$that is isomorphic in$\mathcal { D }$to the object$F ( X ^ { \prime } )$, for any object $X ^ { \prime } \mathrm { i n } \mathcal { C } ^ { \prime }$. This procedure extends$\pi _ { 0 }$to a functor from skeletally small categories to sets.

## Chapter 4

# Universal properties

A reference for this chapter is Mac Lane [40, III].

## 4.1 Initial and terminal objects

Definition 4.1.1. An object X of a category$\mathcal { C }$is initial if for each object $Y$in$\mathcal { C }$there is a unique morphism$X  Y$in$\mathcal { C } _ { : }$, i.e., if each morphism set ${ \mathcal { C } } ( X , Y )$consists of a single element. An object$Z$of a category$\mathcal { C }$is terminal if for each object$Y$in$\mathcal { C }$there is a unique morphism$Y  Z$in${ \mathcal { C } } _ { : }$i.e., if each morphism set${ \mathcal { C } } ( Y , Z )$consists of a single element.

Remark 4.1.2. Such existence and uniqueness conditions are often called universal properties.

Definition 4.1.3. Any property$P$formulated in terms of a category$\mathcal { C }$has a dual property$P ^ { o p } { } _ { ; }$, which is the same as the property$P$formulated in terms of the opposite category$\mathcal { C } ^ { o p }$. In other words, the definition of the opposite property$P ^ { o p }$is obtained by reversing all arrows in the definition of the property $P .$The dual property of$P ^ { o p }$is$P$again.

[[Example: Being a left inverse of$f$is dual to being a right inverse of$f . ] ]$

Lemma 4.1.4. An object X is initial in$\mathcal { C }$if and only if X is terminal in the opposite category$\mathcal { C } ^ { o p }$, and X is terminal in$\mathcal { C }$if and only$i f X$is initial in$\mathcal { C } ^ { o p }$ Hence being initial and being terminal are dual properties.

Proof. The object X is initial in$\mathcal { C }$if and only if for each object$Y$in$\mathcal { C }$the set ${ \mathcal { C } } ( X , Y )$has precisely one element. This is equivalent to the assertion that for each object$Y$in$\mathcal { C } ^ { o p }$the set${ \mathcal { C } } ^ { o p } ( Y , X )$has precisely one element, which says exactly that X is terminal in$\mathcal { C } ^ { o p }$

The second claim follows from the first applied to the category$\mathcal { C } ^ { o p }$, using the fact that$( \mathcal { C } ^ { o p } ) ^ { o p } = \mathcal { C }$□

Lemma 4.1.5. If X and$X ^ { \prime }$are initial objects in a category${ \mathcal { C } } ,$, then there are unique morphisms$f \colon X \to X ^ { \prime }$and$g \colon X ^ { \prime } \to X$, and these are mutually inverse isomorphisms.

$I f ~ Z$and$Z ^ { \prime }$are terminal objects in a category$\mathcal { C } _ { : }$, then there are unique morphisms$f \colon Z \to Z ^ { \prime }$and$g \colon Z ^ { \prime } \to Z$, and these are mutually inverse isomorphisms.

Proof. Suppose that X and$X ^ { \prime }$are initial. By the universal property of$X ,$ there is a unique morphism$f \colon X \to X ^ { \prime }$in$\mathcal { C } .$. By the universal property of $X ^ { \prime }$, there is a unique morphism$g \colon X ^ { \prime } \to X$in$\mathcal { C }$. Consider the composite $g f \colon X \to X$. By the universal property of X, the only endomorphism of X is the identity morphism$i d _ { X }$, so by uniqueness we must have$g f = i d _ { X }$. Next consider the composite fg :$X ^ { \prime }  X ^ { \prime }$. By the universal property of$X ^ { \prime }$, the only endomorphism of$X ^ { \prime }$is$i d _ { X ^ { \prime } } ,$so we must have$f g = i d _ { X ^ { \prime } }$. Hence$g$is left and right inverse to$f ,$so$f$is an isomorphism with inverse$f ^ { - 1 } = g .$. As already noted, these isomorphisms$f \colon X \to X ^ { \prime }$and$g \colon X ^ { \prime } \to X$are the only morphisms with the given source and target, hence they are unique.

The second claim follows from the first applied to the category$\mathcal { C } ^ { o p }$, using Lemma 4.1.4.□

Example 4.1.6. In the category Set, the empty set$\varnothing$is the unique initial object. Each singleton set {x} is a terminal object. There are of course unique bijections$\{ x \} \ { \stackrel { \cong } { \longrightarrow } } \ \{ y \}$between any two of the terminal objects. In the full subcategory$\mathcal { F }$, the empty set 0 is the unique initial object, while the singleton set$\mathbf { 1 } = \{ 1 \}$is the unique terminal object. The groupoids iso(Set) and$\mathrm { i s o } ( \mathcal { F } )$ do not have initial or terminal objects.

Definition 4.1.7. A zero object of a category is an object that is both initial and terminal. A pointed category is a category with a chosen zero object.

Lemma 4.1.8. Any two zero objects in a category$\mathcal { C }$are isomorphic, by a unique isomorphism.□

Example 4.1.9. Since the empty set is not a singleton set, neither Set nor$\mathcal { F }$ have zero objects.

Lemma 4.1.10. Let$\mathcal { C }$be a category with a terminal object Z. Let const$( Z ) \colon \mathcal { C } \to$ $\mathcal { C }$be the constant functor to$Z ,$taking each object to$Z$and each morphism to $i d _ { Z }$. The rule η that to each object$X$in$\mathcal { C }$associates the unique morphism $\eta _ { X } \colon X \to Z$in$\mathcal { C }$defines a natural transformation η :$i d \mathcal { C } \Rightarrow \mathrm { c o n s t } ( Z )$

Dually, for a category$\mathcal { C }$with initial object X, there is a natural transformation ǫ : const$( X ) \Rightarrow i d _ { \mathcal { C } }$from the constant functor to$X$to the identity functor.

Proof. The diagram

![](images/page_86_image_9.jpg)

commutes for all morphisms$f \colon X \to Y$in$\mathcal { C } _ { : }$, since there is only one morphism $X  Z .$□

## 4.2 Categories under and over

Definition 4.2.1. Let X be an object in a category$\mathcal { C }$. The undercategory$X / \mathcal { C }$ has as objects the class of morphisms i:$X  Y$in$\mathcal { C }$, where the source X is fixed, but the target$Y$ranges over all objects in$\mathcal { C }$. Given two objects$i \colon X \to Y$ and$i ^ { \prime } \colon X \to Y ^ { \prime }$in$X / \mathcal { C }$, the set of morphisms$( X / \mathcal { C } ) ( i \colon X \to \overleftarrow { Y } , i ^ { \prime } \colon X \to Y ^ { \prime } )$

is the set of morphisms$f \colon Y \to Y ^ { \prime }$in$\mathcal { C }$such that$f \circ i = i ^ { \prime } ,$i.e., such that the diagram

![](images/page_87_image_1.jpg)

commutes. The identity morphism from$i \colon X \to Y$to itself is given by the identity of$Y$in$\mathcal { C }$. The composition of$f \colon Y \to Y ^ { \prime }$and$g \colon Y ^ { \prime } \to \bar { Y ^ { \prime \prime } }$, viewed as morphisms from$i \colon X \to Y { \mathrm { ~ t o ~ } } i ^ { \prime } \colon X \to Y ^ { \prime }$and from$i ^ { \prime } \colon X \to Y ^ { \prime }$to$i ^ { \prime \prime } \colon X \to Y ^ { \prime \prime }$ is given by the composite$g f \colon Y \to Y ^ { \prime \prime }$in$\mathcal { C }$

We may refer to the object$i \colon X \to Y$as$i ,$, or just as$Y ,$, if the structure morphism i is understood from the context.

Definition 4.2.2. Let$Z$be an object in a category$\mathcal { C }$. The overcategory$\mathcal { C } / Z$ has as objects the class of morphisms$p \colon Y  Z$in$\mathcal { C }$, where the source$Y$ranges over all objects in$\mathcal { C } .$, but the target$Z$is fixed. Given two objects$p \colon Y  Z$ and$p ^ { \prime } \colon Y ^ { \prime } \to Z$in$X / \mathcal { C }$, the set of morphisms$( \mathcal { C } / Z ) ( p \colon Y \to Z , p ^ { \prime } \colon Y ^ { \prime } \to Z )$ is the set of morphisms$f \colon Y \to Y ^ { \prime }$in$\mathcal { C }$such that$p ^ { \prime } \circ f = p$, i.e., such that the diagram

![](images/page_87_image_5.jpg)

commutes. The identity morphism from$i \colon Y \to Z$to itself is given by the identity of$Y$in$\mathcal { C }$. The composition of$f \colon Y \to Y ^ { \prime }$and$g \colon Y ^ { \prime } \to \bar { Y ^ { \prime \prime } }$, viewed as morphisms from$p \colon Y \to Z { \mathrm { ~ t o ~ } } p ^ { \prime } \colon Y ^ { \prime } \to Z$and from$p ^ { \prime } \colon Y ^ { \prime } \to Z$to$p ^ { \prime \prime } \colon Y ^ { \prime \prime } \to Z$ is given by the composite$g f \colon Y \to Y ^ { \prime \prime }$in$\mathcal { C }$

Again, we may refer to the object$p \colon Y  Z$as$p ,$or just as$Y ,$if the structure morphism$p$is understood from the context.

Lemma 4.2.3. Let X be an object in$\mathcal { C }$. Then$( X / \mathcal { C } ) ^ { o p } \ = \ \mathcal { C } ^ { o p } / X$and $( \mathcal { C } / X ) ^ { o p } = X / \mathcal { C } ^ { o p }$so the under- and overcategories are dual constructions.

Proof. This is clear by inspection of the definitions.

Lemma 4.2.4. Let X be an object in$\mathcal { C } _ { \mathcal { b } }$. The identity morphism id :$X  X$ is an initial object in the undercategory$X / \mathcal { C }$, and a terminal object in the overcategory$\mathcal { C } / X$

Proof. For each object$i \colon X \to Y$in$X / \mathcal { C }$there is a unique morphism from $i d _ { X } \colon X \to X$to$i \colon X \to Y$in$X / \mathcal { C } ,$, namely the morphism given by$i \colon X \to Y$ This is clear, since a morphism$f \colon X \to Y \ \mathrm { i n } \ \mathcal { C }$gives such a morphism in$X / \mathcal { C }$ if and only if$f \circ i d _ { X } = i ,$which means that$f = i .$Hence$i d _ { X } \colon X \to X$is initial in$X / \mathcal { C }$

The other statement follows by duality.

Lemma 4.2.5. Let X be an initial object in$\mathcal { C }$. Then$i d _ { X } \colon X \to X$is a zero object in the overcategory$\mathcal { C } / X$. Dually, let$Z$be a terminal object in$\mathcal { C }$. Then $i d _ { Z } \colon Z \to Z$is a zero object in the under category$Z / \mathcal { C }$

Proof. We know that$i d _ { X }$is terminal in$\mathcal { C } / X$by Lemma 4.2.4. It remains to check that it is also initial in$\mathcal { C } / X$. For each object$p \colon Y  X$in$\mathcal { C } / X$there is a unique morphism$f \colon X \to { \dot { Y } }$in$\mathcal { C }$, since$X$is initial in$\mathcal { C } .$The composite $p \circ f \colon X \to X$must be equal to$i d _ { X } \colon X \to X .$, again since X is initial. Hence$f$ defines the unique morphism in$\mathcal { C } / X$from id$\mathbf { \xi } _ { X }$to$p .$

The other statement follows by duality.

Example 4.2.6. Let$\mathbf { S e t }$<sub>∗</sub> be the category of pointed sets, with objects all pairs $( X , x _ { 0 } )$, where X is a set and$x _ { 0 } \in X$an element in$X$, and morphisms from $( X , x _ { 0 } )$to$( Y , y _ { 0 } )$the functions$f \colon X \to Y$such that$f ( x _ { 0 } ) = y _ { 0 }$. We call$x _ { 0 }$the base point of$X ,$and say that f is base point preserving when$f ( x _ { 0 } ) = y _ { 0 }$

Fix a terminal object ∗ in Set, i.e., a one-element set. We can identify a pointed set$( X , x _ { 0 } )$with an object in the undercategory$\bf { * } / \bf { S e t }$, namely the object$i \colon * \to X$where i takes the single element of ∗ to the base point$x _ { 0 }$of $X$. Likewise, a base point preserving function$f \colon ( X , x _ { 0 } )  ( Y , y _ { 0 } )$corresponds to a morphism$f \colon X \to Y$from$i \colon * \to X$to$i ^ { \prime } \colon * \to Y$. Hence there is an identification

$$
\mathbf {S e t} _ {*} \cong * / \mathbf {S e t}.
$$

In particular, the one-element set ∗, with the unique choice of base point, is a zero object in$\mathbf { S e t } _ { * } .$as we saw more generally in Lemma 4.2.5.

Definition 4.2.7. Let$\alpha \colon X \to Z$be a fixed morphism in a category$\mathcal { C } .$. The under-and-overcategory$X / \mathcal { C } / Z$has as objects the triples$( Y , i , p )$where Y is an object in$\mathcal { C }$and$i \colon X \to Y , p \colon Y \to Z$are morphisms in$\mathcal { C }$, such that$p \circ i = \alpha$ A morphism from$( Y , i , p )$to$( Y ^ { \prime } , i ^ { \prime } , p ^ { \prime } )$is a morphism$f \colon Y \to Y ^ { \prime }$such that $f \circ i = i ^ { \prime }$and$p ^ { \prime } \circ f = p$

![](images/page_88_image_7.jpg)

When$\alpha = i d _ { X } \colon X \to X$, we call$X / \mathcal { C } / X$the category of retractive objects over X. Each object$( Y , i , r )$, with$i \colon X \to Y , r \colon Y \to X$and$r \circ i = i d _ { X }$exhibits X as a retract of Y. A morphism$f \colon ( Y , i , r ) \to ( Y ^ { \prime } , i ^ { \prime } , r ^ { \prime } )$restricts to the identity on$X ,$, and commutes with the retractions to$X$

Definition 4.2.8. Let$F \colon \mathcal { C } \ \to \ \mathcal { D }$be a functor, and fix an object$Y$in$\mathcal { D }$ The$l e f t$fiber category$F / Y$is the category with objects the pairs$( X , g )$where $X$is an object in$\mathcal { C }$and$g \colon F ( X ) \to Y$is a morphism in$\mathcal { D }$. The morphisms in$F / Y$from$( X , g )$to$( X ^ { \prime } , g ^ { \prime } )$are the morphisms$f \colon X \to X ^ { \prime }$in$\mathcal { C }$such that

$$
g = g ^ {\prime} \circ F (f).
$$

![](images/page_89_image_1.jpg)

Definition 4.2.9. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$and Y be as above. The right fiber category $Y / F$is the category with objects the pairs$( X , g )$where X is an object in$\mathcal { C }$ and$g \colon Y \to F ( X )$is a morphism in${ \mathcal { D } } .$. The morphisms in$Y / F$from$( X , g )$to $( X ^ { \prime } , g ^ { \prime } )$are the morphisms$f \colon X \to X ^ { \prime }$in$\mathcal { C }$such that$g ^ { \prime } = F ( f ) \circ g$

![](images/page_89_image_3.jpg)

Example 4.2.10. Let$F = i d _ { \mathcal { C } } \colon \mathcal { C } \to \mathcal { C }$. The left fiber category$i d _ { \mathcal { C } } / Y$is the same as the overcategory$\mathcal { C } / Y$. The right fiber category$Y / i d _ { \mathcal { C } }$is the same as the under category$Y / \mathcal { C }$

Lemma 4.2.11. Let$F ^ { o p } \colon \mathcal { C } ^ { o p } \ \longrightarrow \ \mathcal { D } ^ { o p }$be opposite to$F \colon \mathcal { C } \ \to \ \mathcal { D } .$. Then $( Y / F ) ^ { o p } = F ^ { o p } / Y$and$( F / Y ) ^ { o p } = Y / F ^ { o p }$, so the left and right fiber categories are dual constructions.

Proof. This is clear by inspection of the definitions.

Definition 4.2.12. Let$F \colon \mathcal { C }  \mathcal { D }$be a functor, and u:$Y  Y ^ { \prime }$a morphism in${ \mathcal { D } } .$. The induced functor of left fiber categories

$$
F / u \colon F / Y \longrightarrow F / Y ^ {\prime}
$$

takes$( X , g \colon F ( X ) \to Y )$to$( X , u g \colon F ( X ) \to Y ^ { \prime } )$. The induced functor of right fiber categories

$$
u / F \colon Y ^ {\prime} / F \longrightarrow Y / F
$$

takes$( X , g \colon Y ^ { \prime } \to F ( X ) )$to$( X , g u \colon Y \to F ( X ) )$

Definition 4.2.13. Let$F \colon { \mathcal { C } }  { \mathcal { D } }$and Y be as above. The fiber category $F ^ { - 1 } ( Y )$is the full subcategory of C generated by the objects X with$F ( X ) = Y .$ There are inclusions$F ^ { - 1 } \bar { ( Y ) } \stackrel { \cdot } {  } F / \bar { Y }$and$F ^ { - 1 } \dot { ( } Y )  \dot { Y } / F$, both of which map X to$( X , i d _ { Y } )$

Remark 4.2.14. The left and right fiber categories behave as homotopy fibers in the homotopy theory of categories. They play a key role in Quillen’s theorems A and B. [[Forward reference.]] The fiber category behaves more as a (strict) fiber, and only has homotopy theoretic meaning for particular kinds of functors. In general there are no natural functors$u _ { * } \colon F ^ { - 1 } ( Y ) \to F ^ { - 1 } ( Y ^ { \prime } )$or $u ^ { * } \colon F ^ { - 1 } ( Y ^ { \prime } ) \stackrel { \textstyle \cdot } {  } F ^ { - 1 } ( Y )$associated to a morphism u:$Y  Y ^ { \prime }$in${ \mathcal { D } } _ { : }$but there are special cases where such functors exist, as we shall discuss in section 4.4.

## 4.3 Colimits and limits

Definition 4.3.1. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be a functor, viewed as a C-shaped diagram in D. A colimit of$F$is an object$Y$of$\mathcal { D }$, and morphisms$i _ { X } \colon F ( X ) \to Y$in D for each object X in$\mathcal { C }$, such that$i _ { X } = i _ { X ^ { \prime } } \circ F ( f )$for each morphism f :$X  X ^ { \prime }$ in$\mathcal { C }$,

![](images/page_90_image_3.jpg)

with the property that for any object Z of${ \mathcal { D } } ,$and morphisms$j _ { X } \colon F ( X ) \to Z$ in$\mathcal { D }$for each$X$in$\mathcal { C }$, such that$j _ { X } = j _ { X ^ { \prime } } \circ F ( f )$for each$f \colon X \to X ^ { \prime }$in$\mathcal { C } _ { : }$ there exists a unique morphism$g \colon Y \to Z$in$\mathcal { D }$, such that$j _ { X } = g \circ i _ { X }$for each X in$\mathcal { C }$

![](images/page_90_image_5.jpg)

We then write

$$
Y = \underset {\mathcal {C}} {\operatorname{colim}} F = \underset {X \in \mathcal {C}} {\operatorname{colim}} F (X)
$$

and$i _ { X } \colon F ( X ) \to \operatorname { c o l i m } _ { X \in { \mathcal { C } } } F ( X )$

We say that D has all C-shaped colimits if there exists a colimit colim<sub>C</sub> F for each functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$. We say that$\mathcal { D }$has all small colimits, or is cocomplete, if it has all C -shaped colimits for all small categories$\mathcal { D }$

Lemma 4.3.2. Any two colimits$( Y , \{ i _ { X } \} _ { X } )$and$\left( Y ^ { \prime } , \{ i _ { X } ^ { \prime } \} _ { X } \right)$for$F \colon \mathcal { C }  \mathcal { D }$ are isomorphic by a unique isomorphism g :$Y \xrightarrow { \cong } Y ^ { \prime }$such that$i _ { X } ^ { \prime } = g \circ i _ { X }$for all X.

Proof. By the universal property of$( Y , \{ i _ { X } \} _ { X } )$there exists a unique morphism $g \colon Y \to Y ^ { \prime }$such that$i _ { X } ^ { \prime } = \textit { g o i } _ { X }$for all X. By the universal property of $\left( Y ^ { \prime } , \{ i _ { X } ^ { \prime } \} _ { X } \right)$there exists a unique morphism$g ^ { \prime } \colon Y ^ { \prime } \to Y$such that$i _ { X } = g ^ { \prime } \circ i _ { X } ^ { \prime }$ for all$X$. The composite$g ^ { \prime } g \colon Y \to Y$must then be$i d _ { Y }$, since this is the unique morphism$h \colon Y \to Y$such that$i _ { X } = h \circ i _ { X }$for all$X$. Likewise, the composite $g g ^ { \prime } \colon Y ^ { \prime } \to Y ^ { \prime }$must be$i d _ { X ^ { \prime } }$, since this is the unique morphism$h ^ { \prime } \colon Y ^ { \prime } \to Y ^ { \prime }$such that$i _ { X } ^ { \prime } = h ^ { \prime } \circ i _ { X } ^ { \prime }$for all$X$. Hence$g$is an isomorphism, with inverse$g ^ { \prime }$.□

We shall therefore speak of “the” colimit of a$\mathcal { C } .$-shaped diagram in$\mathcal { D }$, when it exists.

Definition 4.3.3. Given an object$Z$of${ \mathcal { D } } _ { : }$let cons$( Z ) : \mathcal { C }  \mathcal { D }$be the constant functor with value$Z$at each object$X$in$\mathcal { C }$, and value$i d _ { Z }$at each morphism$f \colon X \ \to \ X ^ { \prime }$in$\mathcal { C }$. Given any morphism$g \colon Y \ \to \ Z$in${ \mathcal { D } } .$, let const(g): cons$( Y ) \Rightarrow$const$( Z )$be the natural transformation of functors$\mathcal { C }$ $\mathcal { D }$with components$g$for each$X$in$\mathcal { C } .$

A colimit for$F \colon { \mathcal { C } }  { \mathcal { D } }$is then an object$Y$of$\mathcal { D }$and a natural transformation i :$F \Rightarrow \mathrm { c o n s t } ( Y )$of functors$\mathcal { C } \to \mathcal { D }$, such that for any object$Z$of$\mathcal { D }$and natural transformation$j \colon F \Rightarrow \mathrm { c o n s t } ( Z )$there is a unique morphism$g \colon Y \to Z$ such that$j = \mathrm { c o n s t } ( g ) \circ i$

Definition 4.3.4. Suppose that$\mathcal { C }$is small, and view functors$\mathcal { C } \to \mathcal { D }$as C-shaped diagrams in${ \mathcal { D } } .$. The constant diagrams define a functor

$$
\operatorname{const} \colon \mathscr {D} \longrightarrow \mathbf {F u n} (\mathscr {C}, \mathscr {D}).
$$

Given a$\mathcal { C } .$-shaped diagram$F$in$\mathcal { D }$, viewed as an object in${ \bf F u n } ( \mathcal { C } , \mathcal { D } )$, we can form the right fiber category

## F/ const

with objects pairs$( Z , j )$, where$Z$is in$\mathcal { D }$and$j \colon F \to \mathrm { c o n s t } ( Z )$is a morphism in Fun$( \mathcal { C } , \mathcal { D } )$. The morphisms in$F /$const from$( Y , i )$to$( Z , j )$are morphisms $g \colon Y \to Z$such that$j = \mathrm { c o n s t } ( g )$◦ i. A colimit for$F$is then an initial object $( Y , i )$in$F /$const. If such an initial$Y =$colim<sub>C</sub>$F$exists, there is a bijection

$$
\mathcal {D} (\underset {\mathcal {C}} {\operatorname{colim}} F, Z) \cong \mathbf {F u n} (\mathcal {C}, \mathcal {D}) (F, \operatorname{const} (Z)).
$$

From the description of colim<sub>C</sub>$F$as an initial object in a right fiber category, its essential uniqueness proved in Lemma 4.3.2 is seen as a special case of the essential uniqueness of initial objects.

Lemma 4.3.5. Suppose that$\mathcal { D }$admits all C-shaped colimits. Then a choice of object colim<sub>C</sub>$F$in${ \mathcal { D } } ,$, for each functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$, defines a functor

$$
\underset {\mathcal {C}} {\operatorname{colim}} \colon \mathbf {F u n} (\mathcal {C}, \mathcal {D}) \longrightarrow \mathcal {D}
$$

which is${ \it l e f t }$adjoint to the constant diagram functor const:$\begin{array} { r l } { \mathcal { D } \longrightarrow \mathbf { F u n } ( \mathcal { C } , \mathcal { D } ) } \end{array}$

Proof. [[Explain colim<sub>C</sub> on morphisms?]]

Definition 4.3.6. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be a functor, viewed as a C-shaped diagram in D. A limit of F is an object$Z$of$\mathcal { D }$, and morphisms$p _ { X } \colon Z \to F ( X )$in$\mathcal { D }$for each object$X$in$\mathcal { C }$, such that$p _ { X ^ { \prime } } = F ( f ) \circ p _ { X }$for each morphism$f \colon X \to X ^ { \prime }$ $\mathcal { C }$

![](images/page_91_image_15.jpg)

with the property that for any object Y of${ \mathcal { D } } .$, and morphisms$q _ { X } \colon Y \to F ( X )$ in$\mathcal { D }$for each$X$in$\mathcal { C } _ { : }$, such that$q _ { X ^ { \prime } } = F ( f ) \circ q _ { X }$for each$f \colon X \to X ^ { \prime }$in$\mathcal { C } _ { : }$ there exists a unique morphism$g \colon Y \to Z$in${ \mathcal { D } } _ { : }$such that$q _ { X } = p _ { X } \circ g$for each $X$in$\mathcal { C }$

![](images/page_92_image_1.jpg)

We then write

$$
Z = \lim _ {\mathcal {C}} F = \lim _ {X \in \mathcal {C}} F (X)
$$

and$p _ { X }$: lim$\mathfrak { i } _ { X \in \mathcal { C } } F ( X ) \to F ( X )$

We say that D has all C-shaped limits if there exists a limit lim<sub>C</sub>$F$for each functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$. We say that$\mathcal { D }$has all small limits, or is complete, if it has all$\mathcal { C } .$-shaped limits for all small categories$\mathcal { D }$

Remark 4.3.7. A limit of a functor$F \colon \mathcal { C }  \mathcal { D }$is the same a colimit of the opposite functor$F ^ { o p } \colon \mathcal { C } ^ { o p }  \mathcal { D } ^ { o p }$, and conversely a colimit of$F \colon { \mathcal { C } } \to { \mathcal { D } }$is the same as a colimit of$F ^ { o p } \colon \mathcal { C } ^ { o p }  \mathcal { D } ^ { o p }$. Proofs about colimits can therefore be dualized into proofs about limits, and conversely.

Lemma 4.3.8. Any two limits$( Z , \{ p _ { X } \} _ { X } )$and$\left( Z ^ { \prime } , \{ p _ { X } ^ { \prime } \} _ { X } \right)$for$F \colon { \mathcal { C } } \to { \mathcal { D } }$are isomorphic by a unique isomorphism$g \colon Z \xrightarrow { \cong } Z ^ { \prime }$such that$p _ { X } = p _ { X } ^ { \prime } \circ g$for all $X$

Proof. Dualize the proof of Lemma 4.3.2.

We therefore speak of “the” limit of a C-shaped diagram in${ \mathcal { D } } _ { : }$, when it exists.

Definition 4.3.9. A limit for$F \colon \mathcal { C }  \mathcal { D }$is an object$Z$of$\mathcal { D }$and a natural transformation$p { : }$const$( Z ) \Rightarrow F$of functors$\mathcal { C } \to \mathcal { D }$, such that for any object$Y$ of D and natural transformation q : const$( Y ) \Rightarrow F$there is a unique morphism $g \colon Y \to Z$such that$q = p \circ \operatorname { c o n s t } ( g )$

Definition 4.3.10. Suppose that$\mathcal { C }$is small. Given a C -shaped diagram$F$in ${ \mathcal { D } } _ { : }$viewed as an object in$\mathbf { F u n } ( \mathcal { C } , \mathcal { D } )$, we can form the left fiber category

## const /F

with objects pairs$( Y , q )$, where$Y$is in$\mathcal { D }$and$q \colon$const$( Y )  F$is a morphism in Fun$( \mathcal { C } , \mathcal { D } )$. The morphisms in const$/ F$from$( Y , q ) \ \mathrm { t o } \ ( Z , p )$are morphisms $g \colon Y \to Z$such that$q = p \circ$const(g). A limit for$F$is then a terminal object $( Z , p )$in const$/ F .$. If such a terminal$Z = \operatorname* { l i m } _ { \mathcal { C } } F$exists, there is a bijection

$$
\mathcal {D} (Y, \lim _ {\mathcal {C}} F) \cong \mathbf {F u n} (\mathcal {C}, \mathcal {D}) (\text { const } (Y), F)  .
$$

From the description of$\operatorname { l i m } _ { \mathcal { C } } F$as a terminal object in a left fiber category, its essential uniqueness is a special case of the essential uniqueness of terminal objects.

Lemma 4.3.11. Suppose that$\mathcal { D }$admits all C -shaped limits. Then a choice of object lim<sub>C</sub> F in${ \mathcal { D } } ,$for each functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$, defines a functor

$$
\lim _ {\mathcal {C}} \colon \mathbf {F u n} (\mathcal {C}, \mathcal {D}) \longrightarrow \mathcal {D}
$$

which is right adjoint to the constant diagram functor const:${ \mathcal { D } } \longrightarrow \mathbf { F u n } ( { \mathcal { C } } , { \mathcal { D } } )$ Proof. [[Explain lim<sub>C</sub> on morphisms?]]口

Lemma 4.3.12. Suppose that$\mathcal { D }$admits all C -shaped colimits and limits, with $\mathcal { C }$small. Then there are adjoint pairs (colim<sub>D</sub>, const) and (const, lim<sub>D</sub>).

$$
\mathbf {F u n} (\mathcal {C}, \mathcal {D}) \xrightarrow [ \begin{array}{c} \longleftarrow \text {const} \\ \longleftarrow \text {lim} _ {\mathcal {D}} \end{array} ]{\text {colim} _ {\mathcal {D}}} \mathcal {D}
$$

Example 4.3.13. If$\mathcal { C } = \emptyset$is the empty category, there is only one functor $F \colon \varnothing \to { \mathcal { D } }$and a colimit for it is the same as an initial object in C . Dually, a limit for this unique functor is the same as a terminal object in$\mathcal { C } .$

Definition 4.3.14. If$\mathcal { C } = \delta ( I )$is a small discrete category, with object set $\operatorname { o b j } ( \mathcal { C } ) = I$and only identity morphisms, then a functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$is the same as an I-indexed family$( F ( c ) ) _ { c \in I }$of objects in${ \mathcal { D } } ,$, and a colimit for it is the same as a coproduct

$$
\operatorname * {c o l i m} _ {\mathcal {C}} F = \coprod_ {c \in I} F (c)
$$

in$\mathcal { D }$of these objects, equipped with the inclusion morphisms$i _ { c } \colon F ( c ) \ \to$ $\operatorname { I I } _ { c } F ( c )$. Its universal property is that to give a morphism$\textstyle \prod _ { c } F ( c ) \to Z$is equivalent to give morphisms$F ( c )  Z$for all$c \in I$

Dually, a limit for$F \colon { \mathcal { C } } \to { \mathcal { D } }$is the same as a product

$$
\lim _ {\mathcal {C}} F = \prod_ {c \in I} F (c)
$$

in$\mathcal { D }$of these objects, equipped with the projection morphisms$p _ { c } \colon \prod _ { c } F ( c )$ $F ( c )$. Its universal property is that to give a morphism$\begin{array} { r } { Y \to \prod _ { c } F ( c ) } \end{array}$is equivalent to give morphisms$Y  F ( c )$for all$c \in I$

Example 4.3.15. When$\mathcal { C } = \{ 1 , 2 \}$is discrete with two objects, we can picture the coproduct and its universal property as

$$
F (1) \xrightarrow {i _ {1}} F (1) \sqcup F (2) \xleftarrow {i _ {2}} F (2)
$$

where the symbol ∃! indicates that there exists a unique arrow making the diagram commute. Dually, we picture the product and its universal property as

![](images/page_93_image_15.jpg)

Example 4.3.16. The coproduct in$\mathcal { D } = \mathbf { S } \mathbf { e } \mathbf { t }$is given by the disjoint union of sets. The product in Set is given by the cartesian product of sets.

Example 4.3.17. The coproduct in${ \mathcal { D } } = \mathbf { G r p }$is given by the free product of groups. The product in Grp is given by the cartesian product.

Example 4.3.18. The (co-)products of categories defined in Section 1.4 are the categorical (co-)products.

Definition 4.3.19. When$\mathcal { C } = \delta ( I )$is discrete and$F \colon { \mathcal { C } } \to { \mathcal { D } }$is the constant functor to an object X, then$( F ( c ) ) _ { c \in I } = ( X ) _ { c \in I }$is the constant family at X. If the coproduct$\operatorname { I I } _ { c \in I } X$exists, the identity maps$i d _ { X } \colon X \to X$combine to define the fold morphism

$$
\nabla \colon \coprod_ {c \in I} X \longrightarrow X
$$

such that$\nabla \circ i _ { c } = i d _ { X }$for all$c \in I$. If the product$\Pi _ { c \in I } X$exists, the identity maps$i d _ { X } \colon X \to X$combine to define the diagonal morphism

$$
\Delta \colon X \longrightarrow \prod_ {c \in I} X
$$

such that$p _ { c } \circ \Delta = i d _ { X }$for all$c \in I$

Example 4.3.20. The diagonal and fold functors of Definition 2.3.16 are special cases of these constructions.

Definition 4.3.21. Let$\mathcal { C } = \{ 0 \Longrightarrow 1 \}$be a category with “two parallel arrows”. A C-shaped diagram in$\mathcal { D }$has the form

$$
F (0) \xrightarrow [ g ]{f} F (1)  .
$$

A colimit for F is an object Y with morphisms$i _ { 0 } \colon F ( 0 ) \to Y$and$i _ { 1 } \colon F ( 1 ) \to Y$ such that$i _ { 1 } \circ f = i _ { 0 } = i _ { 1 } \circ g .$, or more succinctly, an object Y with a morphism $i _ { 1 } \colon F ( 1 ) \to Y$such that$i _ { 1 } f = i _ { 1 } g$. Such a colimit is called the coequalizer of$f$ and$g _ { ; }$, denoted

$$
\underset {\mathcal {C}} {\operatorname{colim}} F = \operatorname{coeq} (f, g)  .
$$

Its universal property is that to give a morphism coeq$_ 1 ( f , g ) \to Z$is equivalent to giving a morphism$j _ { 1 } \colon F ( 1 ) \to Z$such that$j _ { 1 } f = j _ { 1 } g$

Dually, a limit for F is an object Z with morphisms$p _ { 0 } \colon Z \to F ( 0 )$and $p _ { 1 } \colon Z \to F ( 1 )$such that$f \circ p _ { 0 } = p _ { 1 } = g \circ p _ { 0 }$, or equivalently, an object$Z$ with a morphism$p _ { 0 } \colon Z \to F ( 0 )$such that$f p _ { 0 } = g p _ { 0 }$. Such a limit is called the equalizer of$f$and$^ { g , }$denoted

$$
\lim _ {\mathcal {C}} F = \operatorname{eq} (f, g)  .
$$

Its universal property is that to give a morphism$Y \longrightarrow \mathrm { e q } ( f , g )$is equivalent to giving a morphism$q _ { 1 } \colon Y \to F ( 0 )$such that$f q _ { 1 } = g q _ { 1 }$

Example 4.3.22. We can picture the coequalizer and its universal property as:

![](images/page_95_image_1.jpg)

Dually, we picture the equalizer and its universal property as

![](images/page_95_image_3.jpg)

Example 4.3.23. The coequalizer in$\mathcal { D } = \mathbf { S } \mathbf { e } \mathbf { t }$of two functions$f , g \colon X \to Y$ is the quotient set

$$
\operatorname{coeq} (f, g) = Y / \sim
$$

of$Y$, where$\sim$is the equivalence relation generated by$f ( x ) \sim g ( x )$for all$x \in X$

The equalizer in Set of$f , g \colon X \to Y$is the subset

$$
\operatorname{eq} (f, g) = \{x \in X \mid f (x) = g (x) \}
$$

of$X , { \mathrm { i . e . } }$, the subset where the two functions are equal.

Example 4.3.24. The coequalizer in${ \mathcal { D } } = \mathbf { G r p }$of two group homomorphisms $f , g \colon G \to H$is the quotient group

$$
\operatorname{coeq} (f, g) = H / N
$$

of$H$, where N is the normal subgroup of$H$generated by the elements$f ( k ) ^ { - 1 } g ( k )$ for all$k \in G$

The equalizer in Grp of$f , g \colon G \to H$is the subgroup

$$
\operatorname{eq} (f, g) = \{k \in G \mid f (k) = g (k) \}
$$

of$G , { \mathrm { i . e . } }$, the subgroup where the two homomorphisms are equal.

Example 4.3.25. [[The coequalizer of two functors$F , G \colon \mathcal { C } \  \ \mathcal { D } ? ]$The equalizer$\operatorname { e q } ( F , G )$of two functors$F , G \colon \mathcal { C }  \mathcal { D }$is the subcategory of$\mathcal { C }$with objects the X in$\mathcal { C }$such that$F ( X ) = G ( X )$in$\mathcal { D }$, and morphisms the$f \colon X \to Y$ in$\mathcal { C }$such that$F ( f ) = G ( f )$in D.

In these examples there were isomorphisms$\mathcal { C } \cong \mathcal { C } ^ { o p }$, so that it was natural to treat colim<sub>C</sub> and lim<sub>C</sub> together. In the following examples$\mathcal { C }$is not self-dual.

Definition 4.3.26. Let$\mathcal { C } = \{ 1 \longleftarrow 0 \longrightarrow 2 \}$. A C -shaped diagram in$\mathcal { D }$ has the form

$$
F (1) \xleftarrow {f} F (0) \xrightarrow {g} F (2).
$$

A colimit for$F$is an object$Y$with morphisms$i _ { 1 } \colon F ( 1 ) \to Y$and$i _ { 2 } \colon F ( 2 ) \to Y$ such that$i _ { 1 } f = i _ { 2 } g$. Such a colimit is called the pushout of$f$and$^ { g , }$often somewhat imprecisely denoted

$$
\underset {\mathcal {C}} {\operatorname{colim}} F = F (1) \cup_ {F (0)} F (2).
$$

To give a morphism$F ( 1 ) \cup _ { F ( 0 ) } F ( 2 ) \to Z$is equivalent to giving morphisms $j _ { 1 } \colon F ( 1 ) \to Z$and$j _ { 2 } \colon F ( 2 ) \to { \dot { Z } }$with$j _ { 1 } f = j _ { 2 } g \colon F ( 0 )  Z \colon$

![](images/page_96_image_1.jpg)

Such a commutative square, with edges$f , g , i _ { 1 }$and$i _ { 2 }$is called a pushout square, or more precisely, the pushout square generated by$f$and$g .$The symbol$\langle \langle \Gamma ^ { - } \rangle ^ { \ast }$ indicates the part of the pushout square that determines the remaining corner. If$F ( 0 )$is initial in$\mathcal { D }$, then the pushout$F ( 1 ) \cup _ { F ( 0 ) } F ( 2 )$is equal to the coproduct $F ( 1 ) \sqcup F ( 2 )$

Definition 4.3.27. Let$\mathcal { C } = \{ 1 \longrightarrow 0 \longmapsto 2 \}$. A C -shaped diagram in$\mathcal { D }$ has the form

$$
F (1) \xrightarrow {f} F (0) \xleftarrow {g} F (2).
$$

A limit for$F$is an object$Z$with morphisms$p _ { 1 } \colon Z \to F ( 1 )$and$p _ { 2 } \colon Z \to F ( 2 )$ such that$f p _ { 1 } = g p _ { 2 }$. Such a limit is called the pullback of$f$and$^ { g , }$often somewhat imprecisely denoted

$$
\lim _ {\mathcal {C}} F = F (1) \times_ {F (0)} F (2).
$$

To give a morphism$Y  F ( 1 ) \times _ { F ( 0 ) } F ( 2 )$is equivalent to giving morphisms $q _ { 1 } \colon Y \to F ( 1 )$and$q _ { 2 } \colon Y \to F ( 2 )$with$f q _ { 1 } = g q _ { 2 } { \mathrm { : } }$

![](images/page_96_image_8.jpg)

Such a commutative square, with edges$p _ { 1 } , p _ { 2 } , f$and$^ { g , }$is called a pullback square, or more precisely, the pullback square generated by$f$and$g .$. The symbol $^ { 6 6 } \_ { ^ { \prime } }$indicates the part of the pullback square that determines the remaining corner. If$F ( 0 )$is terminal in${ \mathcal { D } } _ { : }$, then the pullback$F ( 1 ) \times _ { F ( 0 ) } F ( 2 )$is equal to the product$F ( 1 ) \times F ( 2 )$

Remark 4.3.28. Beware the potential ambiguity in the notation$X \times _ { B } E$for the pullback of$X  B$and$E  B$, compared to the notation$X \times _ { G } Y$for the balanced product of two G-spaces.

Example 4.3.29. The pushout in Set of two functions$f \colon X \to Y$and$g \colon X \to$ Z is the quotient set

$$
Y \cup_ {X} Z = (Y \sqcup Z) / \sim
$$

where ∼ is the equivalence relation generated by the identification of$f ( x ) \in$ $Y \subseteq Y \sqcup Z$with$g ( x ) \in Z \subseteq Y \sqcup Z$, for all$x \in X$. If$f \colon X \to Y$is injective, then the inclusion$Z \to Y \cup _ { X } Z$is injective, and each element in$Y \cup _ { X } Z$can be uniquely expressed either as an element in$Y \setminus f ( X )$, or as an element in$Z .$

The pullback in Set of two functions$f \colon X \to Z$and$g \colon Y \to Z$is the subset

$$
X \times_ {Z} Y = \left\{(x, y) \in X \times Y \mid f (x) = g (y) \right\},
$$

also known as the fiber product of X and$Y$over$Z .$For each x$\in X$the fiber of $X \times _ { Z } Y$over$x ,$meaning the preimage of x under the projection$X \times _ { Z } Y \to X$，can be identified with the fiber$g ^ { - 1 } ( f ( x ) )$of$Y$over$f ( x )$, meaning the preimage of$f ( x )$under the function$g \colon Y \to Z$

Example 4.3.30. The pushout in Grp of two homomorphisms$f \colon K \to H$and $g \colon K \to G$is the amalgamated free product

$$
\operatorname{colim} \{H \stackrel {f} {\leftarrow} K \stackrel {g} {\rightarrow} G \} = H * _ {K} G
$$

obtained as the quotient group of the free product$H * K$by the normal subgroup generated by the words$f ( k ) ^ { - 1 } g ( k )$for all$k \in K$

The pullback in Grp of two homomorphisms$f \colon H \to G$and$g \colon K \to G$is the subgroup

$$
H \times_ {G} K = \left\{(h, k) \in H \times K \mid f (h) = g (k) \right\},
$$

of the direct product$H \times G$

[[Pushout and pullback in Cat.]]

Definition 4.3.31. Let$\mathcal { C }$be a category with a terminal object ∗. A cofiber of a morphism$f \colon X \to Y$is a pushout of the diagram

$$
* \longleftarrow X \longrightarrow Y.
$$

We write$Y / X$or$Y / f ( X )$for this pushout$* \cup _ { X } Y$. There are preferred morphisms$* \to Y / X  Y$

Given a morphism$p \colon \ast  Y$, the fiber of a morphism$f \colon X \to Y$at$p$is a pullback of the diagram

$$
* \stackrel {p} {\longrightarrow} X \stackrel {f} {\longleftarrow} X.
$$

We write$f ^ { - 1 } ( p )$for this pullback. There is a preferred morphism$f ^ { - 1 } ( p ) \to X$ Example 4.3.32. In sSet, the cofiber of a function$f \colon X \to Y$is the quotient set$Y / f ( X ) = ( Y \sqcup \{ * \} ) / \sim$, where$f ( x ) \sim *$for each$x \in X$Note that $Y / \varnothing = Y _ { + } = Y \sqcup \{ * \}$. A morphism$\{ * \} \to Y$corresponds to a point$p \in Y$, and the fiber of$f \colon X \to Y$at p is the subset$f ^ { - 1 } ( p ) = \{ x \in X | f ( x ) = p \}$

[[Sequential colimit, sequential limit.]]

[[Also discuss finite categories, with finitely many morphisms, and finite colimits? Beware that the nerve of a finite category needs not be a finite simplicial set.]]

Lemma 4.3.33. Suppose that$\mathcal { D }$has all small coproducts and coequalizers. Then$\mathcal { D }$has all small colimits.

Dually, suppose that D has all small products and equalizers. Then$\mathcal { D }$has all small limits.

Proof. The colimit of$F \colon { \mathcal { C } }  { \mathcal { D } }$is given by the coequalizer of the two morphisms

$$
s, t \colon \coprod_ {f \colon X \to Y} F (X) \longrightarrow \coprod_ {X} F (X)
$$

where$f$ranges over all morphisms in$\mathcal { C }$and$X$ranges over all objects in$\mathcal { C }$ The morphism$s$is determined by its restrictions$s \circ i _ { f } = i _ { X }$for$f \colon X \to Y$ while the morphism t is determined by its restrictions$t \circ i _ { f } = i _ { Y } \circ F ( f )$

Dually, the limit of$F \colon { \mathcal { C } } \to { \mathcal { D } }$is given by the equalizer of the two morphisms

$$
s, t \colon \prod_ {X} F (X) \longrightarrow \prod_ {f: X \to Y} F (X)
$$

where$X$ranges over all objects in$\mathcal { C }$and$f$ranges over all morphisms in$\mathcal { C } .$The morphism s is determined by its projections$p _ { f } \circ s = F ( f ) \circ p _ { X }$for$f \colon X \to Y$ while the morphism t is determined by its projections$p _ { f } \circ t = p _ { Y }$

[[What remains to be verified?]]

Example 4.3.34. The colimit of a$\mathcal { C } .$-shaped diagram in sets,$X \colon { \mathcal { C } } \to \mathbf { S e t }$, is the quotient set

$$
\operatorname * {c o l i m} _ {\mathcal {C}} X = \coprod_ {c} X (c) / \sim
$$

where$\sim$is generated by$i _ { c } ( x ) \sim i _ { d } ( X ( a ) ( x ) )$for all$a \colon c \to d$and$x \in X ( c )$, or more concisely,$X ( c ) \ni x \sim a _ { * } ( x ) \in X ( d )$

Dually, its limit is the subset

$$
\lim _ {\mathcal {C}} X \subseteq \prod_ {c} X (c)
$$

of sequences$( x _ { c } ) _ { }$<sub>c</sub> with$x _ { c } \in X ( c )$for all$c$in${ \mathcal { C } } ,$, such that$X ( a ) ( x _ { c } ) = x _ { d }$for all$a \colon c \to d ,$or more briefly,$a _ { * } ( x _ { c } ) = x _ { d }$

Lemma 4.3.35. Let$F \colon \mathcal { C }  \mathcal { D }$have colimit colim<sub>C</sub>$F$and let Z be an object of D. There is a natural bijection

$$
\mathcal {D} (\underset {\mathcal {C}} {\operatorname{colim}} F, Z) \cong \lim _ {X \in \mathcal {C}} \mathcal {D} (F (X), Z)  .
$$

Dually, let$G \colon { \mathcal { C } } \to { \mathcal { D } }$have limit lim<sub>C</sub>$G$and let Z be an object of$\mathcal { D }$. There is a natural bijection

$$
\mathscr {D} (Z, \lim _ {\mathscr {C}} G) \cong \lim _ {X \in \mathscr {C}} \mathscr {D} (Z, G (X)).
$$

Proof. The first two sets are both identified with the families${ ( \phi _ { X } ) _ { X } }$of morphisms$\phi _ { X } \colon F ( X ) \to Z$in$\mathcal { D }$for all$X$in C, with$\phi _ { Y } \circ F ( f ) = \phi _ { X }$for all $f \colon X \to Y$in$\mathcal { C }$.

The last two sets are both identified with the families${ ( \psi _ { X } ) _ { X } }$of morphisms $\psi _ { X } \colon Z \to G ( X )$in$\mathcal { D }$for all$X$in$\mathcal { C }$, with$G ( f ) \circ \psi _ { X } = \psi _ { Y }$for all$f \colon X \to Y$in $\mathcal { C }$□

The following is a useful tool for checking that a functor respects (co-)limits, or for showing that is cannot be a (co-)adjoint.

Proposition 4.3.36. Let$F \colon \mathcal { C }  \mathcal { D }$and$G \colon { \mathcal { D } } \to { \mathcal { C } }$be an adjoint pair, and $\mathit { l e t } \ \mathcal { E }$be a small category.$I f X \colon { \mathcal { E } } \to { \mathcal { C } }$is an E -shaped diagram in$\mathcal { C }$, with colimit colim<sub>E</sub>$X$, then$F \circ X \colon { \mathcal { E } }  { \mathcal { D } }$has the colimit

$$
\underset {\mathcal {E}} {\operatorname{colim}} (F \circ X) = F (\underset {\mathcal {E}} {\operatorname{colim}} X).
$$

Dually,$i f Y \colon { \mathcal { E } }  { \mathcal { D } }$is an E-shaped diagram in$\mathcal { D }$, with limit lim<sub>E</sub>$Y _ { \mathrm { ~ . ~ } }$, then $G \circ Y \colon { \mathcal { E } } \longrightarrow { \mathcal { C } }$has the limit

$$
\lim _ {\mathcal {E}} (G \circ Y) = G (\lim _ {\mathcal {E}} Y).
$$

In other words, a left adjoint$( = \mathit { c o a d j o i n t } )$preserves colimits, and a right adjoint$( = a d j o i n t )$preserves limits.

Proof. For any object$Y$in$\mathcal { D }$there are natural bijections

$$
\begin{array}{r l} & {\mathcal {D} (F (\underset {\mathcal {E}} {\operatorname{colim}} X), Y) \cong \mathcal {C} (\underset {\mathcal {E}} {\operatorname{colim}} X, G (Y))} \\ & {\qquad \cong \underset {\mathcal {E}} {\lim} \mathcal {C} (X (-), G (Y))} \\ & {\qquad \cong \underset {\mathcal {E}} {\lim} \mathcal {D} (F (X (-)), Y)} \\ & {\qquad \cong \mathbf {F u n} (\mathcal {E}, \mathcal {D}) (F \circ X, \mathrm{const} (Y))} \end{array}
$$

which show that$F ( \operatorname { c o l i m } _ { \mathcal { E } } X )$is a colimit of$F \circ X$

Dually, for any object X in$\mathcal { C }$there are natural bijections

$$
\begin{array}{r l} & {\mathcal {C} (X, G (\lim _ {\mathcal {E}} Y)) \cong \mathcal {D} (F (X), \lim _ {\mathcal {E}} Y)} \\ & {\qquad \cong \lim _ {\mathcal {E}} \mathcal {D} (F (X), Y (-))} \\ & {\qquad \cong \lim _ {\mathcal {E}} \mathcal {C} (X, G (Y (-)))} \\ & {\qquad \cong \mathbf {F u n} (\mathcal {E}, \mathcal {C}) (\mathrm{const} (X), G \circ Y)} \end{array}
$$

which show that$G ( \operatorname* { l i m } _ { \mathcal { E } } Y )$is a limit of$G \circ Y$

Lemma 4.3.37. Suppose that$\mathcal { C }$has a terminal object$Z .$. Then each functor $F \colon { \mathcal { C } } \to { \mathcal { D } }$has a colimit

$$
\underset {\mathcal {C}} {\operatorname{colim}} F = F (Z)
$$

given by the object$F ( Z )$and the structure morphism$i _ { X } = F ( X \to Z ) \colon F ( X ) \to$ $F ( Z )$for all X in$\mathcal { C }$

Lemma 4.3.38. Suppose that$\mathcal { C }$has an initial object Y. Then each functor $F \colon { \mathcal { C } } \to { \mathcal { D } }$has a limit

$$
\lim _ {\mathcal {C}} F = F (Y)
$$

given by the object$F ( Y )$and the structure morphism$p _ { X } = F ( Y \to X ) \colon F ( Y ) \to$ $F ( X )$for all X in C.

[[Filtering (co-)limits?]]

Lemma 4.3.39. Let F :${ \mathcal { C } } \times { \mathcal { D } } \to { \mathcal { E } }$be a bifunctor.$/ / W h i c h$colimits need to exist?]] There are natural isomorphisms

$$
\operatorname * {c o l i m} _ {X \in \mathcal {C}} \bigl (\operatorname * {c o l i m} _ {Y \in \mathcal {D}} F (X, Y) \bigr) \cong \operatorname * {c o l i m} _ {\mathcal {C} \times \mathcal {D}} F \cong \operatorname * {c o l i m} _ {Y \in \mathcal {D}} \bigl (\operatorname * {c o l i m} _ {X \in \mathcal {C}} F (X, Y) \bigr).
$$

[[Which limits need to exist$\it { ? } \coprod \it { - }$There are natural isomorphisms

$$
\lim _ {X \in \mathcal {C}} \bigl (\lim _ {Y \in \mathcal {D}} F (X, Y) \bigr) \cong \lim _ {\mathcal {C} \times \mathcal {D}} F \cong \lim _ {Y \in \mathcal {D}} \bigl (\lim _ {X \in \mathcal {C}} F (X, Y) \bigr).
$$

[[Which colimits and limits need to exist?]] There is a natural colimit-limitexchange morphism

$$
\kappa \colon \operatorname * {c o l i m} _ {X \in \mathcal {C}} \bigl (\lim _ {Y \in \mathcal {D}} F (X, Y) \bigr) \longrightarrow \lim _ {Y \in \mathcal {D}} \bigl (\operatorname * {c o l i m} _ {X \in \mathcal {C}} F (X, Y) \bigr).
$$

Proof. [[Discuss first two cases.$\boldsymbol { \cdot } \big ] \big ]$The morphism κ corresponds to the compatible family of morphisms

$$
j _ {X} \colon \lim _ {Y \in \mathcal {D}} F (X, Y) \longrightarrow \lim _ {Y \in \mathcal {D}} \bigl (\operatorname * {c o l i m} _ {X \in \mathcal {C}} F (X, Y) \bigr)
$$

induced by passage to the limit over$Y$in$\mathcal { D }$from the colimit structure morphisms

$$
i _ {X} (Y) \colon F (X, Y) \longrightarrow \underset {X \in \mathcal {C}} {\operatorname{colim}} F (X, Y).
$$

Equivalently, κ corresponds to the compatible family of morphisms

$$
q _ {Y} \colon \operatorname * {c o l i m} _ {X \in \mathcal {C}} \bigl (\lim _ {Y \in \mathcal {D}} F (X, Y) \bigr) \longrightarrow \operatorname * {c o l i m} _ {X \in \mathcal {C}} F (X, Y)
$$

induced by passage to the colimit over$X$in$\mathcal { C }$from the limit structure morphisms

$$
p _ {Y} (X) \colon \lim _ {Y \in \mathscr {D}} F (X, Y) \longrightarrow F (X, Y).
$$

Remark 4.3.40. It is often an interesting question to decide when$\kappa$is an isomorphism. [[Example:$\mathcal { C }$filtering and$\mathcal { D }$finite.]]

## 4.4 Cofibered and fibered categories

[[The Grothendieck construction$\mathcal { C } \wr F$for functors$F \colon { \mathcal { C } } \to \mathbf { C a t }$, perhaps also pseudofunctors.]]$[ [ \sin \operatorname { p } ( X ) = \Delta \wr X$for$X \colon \Delta ^ { o p }  \mathbf { S e t . } | ]$]]

The following definitions are from SGA1 [24, Exp. VI] and [55, p. 93].

Definition 4.4.1. Let$F \colon { \mathcal { C } }  { \mathcal { D } }$be a functor. For each object$Y$of$\mathcal { D }$there is a (full and faithful) functor

$$
F ^ {- 1} (Y) \longmapsto F / Y
$$

from the fiber to the left fiber of$F$at$Y$, taking$X$in$\mathcal { C }$with$F ( X ) = Y$to $( X , i d _ { Y } \colon F ( X ) \to Y )$. We say that$\mathcal { C }$is a precofibered category over$\mathcal { D }$if this functor has a left adjoint. Denote the left adjoint

$$
F / Y \longrightarrow F ^ {- 1} (Y)
$$

by$( Z , g \colon F ( Z ) \to Y ) ) \mapsto g _ { * } ( Z )$, so that there is a natural bijection

$$
F ^ {- 1} (Y) \left(g _ {*} (Z), X\right) \cong \left(F / Y\right) \left(\left(Z, g\right), \left(X, i d _ {Y}\right)\right).
$$

This amounts to a correspondence between suitable dashed arrows in the following diagram:

![](images/page_101_image_3.jpg)

For each morphism u:$Y  Y ^ { \prime }$in$\mathcal { D }$there is then an associated cobase change functor

$$
u _ {*} \colon F ^ {- 1} (Y) \to F ^ {- 1} (Y ^ {\prime})
$$

taking$Z$with$F ( Z ) = Y$to$u _ { * } ( Z )$, the value of the right adjoint on$( Z , u \colon F ( Z ) \to$ $Y ^ { \prime } )$

![](images/page_101_image_7.jpg)

If$v \colon Y ^ { \prime } \to Y ^ { \prime \prime }$is a second morphism in$\mathcal { D }$, there is a natural transformation

$$
\phi \colon (v u) _ {*} \Rightarrow v _ {*} u _ {*}
$$

of functors$F ^ { - 1 } ( Y ) \to F ^ { - 1 } ( Y ^ { \prime \prime } )$. Given an object$Z$in$\mathcal { C }$with$F ( Z ) = Y$, the adjunction unit

$$
\eta_ {(Z, u)} \colon (Z, u \colon F (Z) \to Y ^ {\prime}) \longrightarrow (u _ {*} (Z), i d _ {Y ^ {\prime}})
$$

in$F / Y ^ { \prime }$maps under$F / v$to a natural map$( Z , v u ) \longrightarrow ( u _ { * } ( Z ) , v )$in$F / Y ^ { \prime \prime }$. Its image under the left adjoint is a natural map

$$
\phi_ {Z} \colon (v u) _ {*} (Z) \longrightarrow v _ {*} (u _ {*} (Z)),
$$

giving the component of$\phi$at$Z .$. We say that$\mathcal { C }$is a cofibered category over$\mathcal { D }$ if the natural transformation$\phi \colon ( v u ) _ { * } \Rightarrow v _ { * } u _ { * }$is a natural isomorphism.

Definition 4.4.2. Let$F \colon { \mathcal { C } }  { \mathcal { D } }$be a functor. For each object$Y$of$\mathcal { D }$there is a (full and faithful) functor

$$
F ^ {- 1} (Y) \longmapsto Y / F
$$

from the fiber to the right fiber of$F$at${ \cal Y } ,$taking X in$\mathcal { C }$with$F ( X ) = Y$to $( X , i d _ { Y } \colon Y \to F ( X ) )$. We say that$\mathcal { C }$is a prefibered category over$\mathcal { D }$if this functor has a right adjoint. Denote the right adjoint

$$
Y / F \longrightarrow F ^ {- 1} (Y)
$$

by$( Z , g \colon Y \to F ( Z ) ) \mapsto g ^ { * } ( Z )$, so that there is a natural bijection

$$
(Y / F) ((X, i d _ {Y}), (Z, g)) \cong F ^ {- 1} (Y) (X, g ^ {*} (Z)).
$$

This amounts to a correspondence between suitable dashed arrows in the following diagram:

![](images/page_102_image_5.jpg)

For each morphism$u \colon Y \to Y ^ { \prime }$in$\mathcal { D }$there is then an associated base change functor

$$
u ^ {*}: F ^ {- 1} (Y ^ {\prime}) \to F ^ {- 1} (Y)
$$

taking$Z$with$F ( Z ) = Y ^ { \prime } \mathrm { t o } u ^ { * } ( Z )$, the value of the right adjoint on$( Z , u \colon Y \to$ $F ( Z ) )$.

![](images/page_102_image_9.jpg)

If$v \colon Y ^ { \prime } \to Y ^ { \prime \prime }$is a second morphism in$\mathcal { D }$, there is a natural transformation

$$
\psi \colon u ^ {*} v ^ {*} \Longrightarrow (v u) ^ {*}
$$

of functors$F ^ { - 1 } ( Y ^ { \prime \prime } ) \to F ^ { - 1 } ( Y )$. Given an object W in$\mathcal { C }$with$F ( W ) = Y ^ { \prime \prime }$ the adjunction counit

$$
\epsilon_ {(W, v)} \colon (v ^ {*} (W), i d _ {Y ^ {\prime}}) \longrightarrow (W, v \colon Y ^ {\prime} \to F (W))
$$

in$Y ^ { \prime } / F$maps under$u / F$to a natural map$( v ^ { * } ( W ) , u ) \longrightarrow ( W , v u )$in$Y / F$. Its image under the right adjoint is a natural map

$$
\psi_ {W} \colon u ^ {*} (v ^ {*} (W)) \longrightarrow (v u) ^ {*} (W),
$$

giving the component of$\psi$at$W$. We say that$\mathcal { C }$is a fibered category over$\mathcal { D }$if the natural transformation ψ :$u ^ { * } v ^ { * } \Rightarrow ( v u ) ^ { * }$is a natural isomorphism.

# Chapter 5

# Homotopy theory

[[Topological spaces Top, CW complexes, compactly generated spaces$\boldsymbol { \mathcal U }$. Compare Hatcher [26, App. A], May [43, Ch. 5] and McCord [45, §2]. Kelleyfication.]] [[NOTE: Revise discussion of gluing lemma, following [26, 4.G].]]

## 5.1 Topological spaces

Recall that Top denotes the category of topological spaces X and continuous functions$f \colon X \to Y$, also known as maps.

Definition 5.1.1. Let Top be the category of based topological spaces$( X , x _ { 0 } )$，with$x _ { 0 } \in X$, and base point preserving maps (= based maps)$f \colon ( X , x _ { 0 } )$ $( Y , y _ { 0 } )$, which are maps$f \colon X \to Y$with$f ( x _ { 0 } ) = y _ { 0 }$. When the choice of base point is clear, we often simply write X for$( X , x _ { 0 } )$

Remark 5.1.2. Let ∗ be a fixed one-point space, a terminal object in Top. Each point$x _ { 0 } \in X$determines a unique map$* \to X$, taking the point in ∗ to $x _ { 0 }$, and conversely, so there is an isomorphism of categories Top<sub>∗</sub>$\cong \ast / \mathbf { T o p }$ Here$\mathbf { \boldsymbol { * } } / \mathbf { T o p }$denotes the undercategory of ∗ in Top, as in Definition 4.2.1.

Definition 5.1.3. Let Y be a topological space. A subset X of$Y$can be given the subspace topology, which is the coarsest topology making the inclusion map $i \colon X \to Y$continuous. Hence a subset of X is open if and only if it is of the form $X \cap U$for U open in Y. We then say that X is a subspace of Y. If$x _ { 0 } \in X$then $( X , x _ { 0 } )$is a based subspace of$( Y , x _ { 0 } )$. A map$i \colon X \to Y$is called an embedding (or an inclusion) if it induces a homeomorphism of X with the subspace$i ( X )$ of Y.

Definition 5.1.4. Let ∼ be an equivalence relation on a topological space X. The quotient set$X / \sim$of X can be given the quotient topology, which is the finest topology making the projection map$p \colon X \to X / { \sim }$continuous. Hence a subset U of$X / \sim$is open if and only if the preimage$p ^ { - 1 } ( U )$is open in X. We then say that$X / \sim$is a quotient space of X. If X is based at$x _ { 0 }$then$( X / { \sim } , p ( x _ { 0 } ) )$is a based quotient space of X. A map$p \colon X \to Y$is called an identification (or a proclusion) if it induces a homeomorphism of the quotient space$X / \sim$with$Y$ where$x \sim y$if and only if$p ( x ) = p ( y )$

Definition 5.1.5. Let X, Y be topological spaces. The disjoint union$X \sqcup Y$has the finest topology that makes both inclusions$i n _ { 1 } \colon X \to X \sqcup Y$and$i n _ { 2 } \colon Y$ $X \sqcup Y$continuous. Hence the open subsets are precisely those of the form $U \sqcup V$, with U open in X and V open in Y . The disjoint union is the categorical coproduct in Top. [[Define fold map$\nabla \colon X \sqcup X \to X ? ]$

If X is based at$x _ { 0 }$and Y is based at$y _ { 0 }$, the wedge sum$( X \lor Y , * )$is the quotient space

$$
X \vee Y = (X \sqcup Y) / (x _ {0} \sim y _ {0}),
$$

based at the common image of$x _ { 0 }$and$y _ { 0 }$. We write in<sub>1</sub>$: X \to X \lor Y$and $i n _ { 2 } \colon Y \to X \vee Y$for the inclusion maps. The wedge sum is the categorical coproduct in Top . [[Define based fold map$\nabla \colon X \vee X  X ? ]$

Lemma 5.1.6. The functor Top<sub>∗</sub> → Top that forgets the base point has a left adjoint$( - ) _ { + } ;$: Top → Top<sub>∗</sub> that takes a space X to the disjoint union $X _ { + } = X \sqcup \{ * \}$of X and a base point.

Proof. There is a natural bijection${ \bf T o p } _ { * } ( X _ { + } , Y ) \cong { \bf T o p } ( X , Y )$for any space X and based space$Y = ( Y , y _ { 0 } )$□

[[Any left adjoint preserves colimits, so$( X \sqcup Y ) _ { + } \cong X _ { + } \vee Y _ { + }$for X, Y in Top. Any right adjoint preserves limits, so$( X \times Y , ( * , * ) )$is the categorical product in Top , for$( X , * ) , ( Y , * )$in Top . The left adjoint is strong symmetric monoidal, so$( X \times Y ) _ { + } \cong X _ { + } \wedge Y _ { + }$. The right adjoint is lax symmetric monoidal, with respect to the natural map π :$X \times Y \to X \land Y . ] ]$

Definition 5.1.7. Let$i \colon X \to Y$and$j \colon X \to Z$be maps. The pushout$Y \cup _ { X } Z$ is the quotient space

$$
(Y \sqcup Z) / \sim
$$

where ∼ is generated by the relations$i ( x ) \sim j ( x )$for all$x \in X$. The square

![](images/page_104_image_10.jpg)

expresses$X \cup _ { X } Z$as the colimit in Top of the diagram$Y \overleftarrow { \mathrm { ~ \it ~ \chi ~ } } \overbrace { \mathrm { ~ \it ~ \chi ~ } } ^ { \mathrm { ~ \it ~ \it ~ { ~ j ~ } ~ } } \ne Z$ If$i \colon ( X , x _ { 0 } ) \to ( Y , y _ { 0 } )$and$j \colon ( X , x _ { 0 } )  ( Z , z _ { 0 } )$are based maps, then$X \cup _ { X } Z$ is based at the equivalence class ∗ of$y _ { 0 } \sim z _ { 0 }$. The square above is then a pushout square in Top<sub>∗</sub>.

Definition 5.1.8. Let X, Y be spaces. The cartesian product$X \times Y$has the coarsest topology that makes both projections$p r _ { 1 } \colon X \times Y \to X$and$p r _ { 2 } \colon X \times$ $Y  Y$continuous. It has a subbasis given by the subsets$U \times Y$and$X \times V$, for all open$U \subseteq X$and$V \subseteq Y$. It has a basis given by the subsets$U \times V$for all U open in X and V open in Y. The cartesian product is the categorical product in Top. [[Define diagonal map$\Delta \colon X \to X \times X ? ] ]$

Definition 5.1.9. Let$p \colon E  B$and$f \colon X \ \to \ B$be maps. The pullback $X \times _ { B } E$is the subspace

$$
X \times_ {B} E = \{(x, e) \in X \times E \mid f (x) = p (e) \}
$$

of$X \times E ,$, consisting of pairs$( x , e )$with equal images in B. The pullback square

![](images/page_105_image_1.jpg)

expresses$X \times _ { B } E$as the limit in Top of the diagram$X { \xrightarrow { \ f \ } } B \overbrace { \ F \ H ^ { \ } } ^ { \ p } \ H$

$\operatorname { I f } f \colon ( X , x _ { 0 } ) \to ( B , b _ { 0 } )$and$p \colon ( E , e _ { 0 } )  ( B , b _ { 0 } )$are based maps, then$X \times _ { B }$ E is based at$\ast = ( x _ { 0 } , e _ { 0 } )$. The square above is then a pullback square in$\mathbf { T o p } _ { * } .$

Lemma 5.1.10. Let$( X , x _ { 0 } ) , ( Y , y _ { 0 } )$be based spaces. The natural map$X \sqcup Y \to$ $X \times Y$, taking$x \in X$to$( x , y _ { 0 } )$and$y \in Y$to$( x _ { 0 } , y )$, induces a homeomorphism

$$
X \vee Y \cong X \times \{y _ {0} \} \cup \{x _ {0} \} \times Y,
$$

where$X \vee Y$has the quotient topology from$X \sqcup Y$and$X \times \{ y _ { 0 } \} \cup \{ x _ { 0 } \} \times Y$ has the subspace topology from$X \times Y$. Hence the induced map$X \vee Y  X \times Y$ is an embedding.

Proof. For brevity, let$L = X \times \{ y _ { 0 } \} \cup \{ x _ { 0 } \} \times Y$. The given maps$X  X \times Y$ and$Y  X \times Y$are continuous, so the induced bijection$h \colon X \vee Y  L$is continuous. Conversely, we must check that if$W \subseteq X \vee Y$is open, then so is its image$h ( W ) \subseteq L$. Let$U \sqcup V = p ^ { - 1 } ( W )$be the preimage of W under $p \colon X \sqcup Y \to X \vee Y$, so that U is open in X and V is open in Y. We divide into two cases. If$* \in W$then$x _ { 0 } \in U$and$y _ { 0 } \in V$. Then$U \times V$is open in$X \times Y$, and $h ( W ) = L \cap ( U \times V )$, so$h ( W )$is open in L. Otherwise$* \notin W .$, so$x _ { 0 } \notin U$and y<sub>0</sub>$\notin V .$. Then$U \times Y \cup X \times V$is open in$X \times Y$and$h ( W ) = L \cap ( U \times Y \cup X \times V ) .$ so$h ( W )$is again open in L.□

We hereafter identify X ∨ Y with its image in$X \times Y$

Definition 5.1.11. Let$( X , x _ { 0 } ) , ( Y , y _ { 0 } )$be based spaces. The smash product $( X \land Y , * )$is the quotient space of$X \times Y$by the subspace$X \vee Y$:

$$
X \wedge Y = \frac {X \times Y}{X \vee Y}.
$$

It has the finest topology making the canonical map$X \times Y \to X \land Y$continuous. We write x$\textstyle \bigwedge y \in X \wedge Y$for the image of$( x , y ) \in X \times Y$. [[Define based diagonal map$\Delta \colon X \to X \land X ? ] ]$

We may write$X \ltimes Y = X _ { + } \land Y$and$X \rtimes Y = X \land Y _ { + }$for the half-smash products of unbased and based spaces, resp. of based and unbased spaces. [[Define half-based diagonal maps$\Delta \colon X \to X \ltimes X$and$\Delta \colon X \to X \rtimes X ? ] ]$

To justify the definition of the smash product, we shall compare maps$X \times$ $Y  Z$with maps from X into a mapping space$\mathrm { M a p } ( Y , Z )$, and see that in the based case, based maps$X \wedge Y \to Z$will correspond to based maps from X into a based mapping space$\mathrm { M a p } _ { * } ( Y , Z )$, at least for locally compact spaces Y . See Proposition 5.1.28. Unlike the cartesian product in Top, the smash product is not the categorical product in$\mathbf { T o p } _ { * }$. There are no natural maps$X \wedge Y \to X$ and$X \wedge Y \to Y$

Definition 5.1.12. Let$X , Y$be topological spaces. The mapping space

$$
\operatorname{Map} (X, Y) = \{f \colon X \to Y \mid f \text {is continuous} \}
$$

has the compact-open topology, with a subbasis given by the subsets

$$
[ K, U ] = \{f \colon X \to Y \mid f (K) \subseteq U \}
$$

for$K \subseteq X$compact and$U \subseteq Y$open. A basis is given by all finite intersections $\left[ K _ { 1 } , U _ { 1 } \right] \cap \cdots \cap \left[ K _ { n } , U _ { n } \right]$of such subsets.

If X is based at$x _ { 0 }$and$Y$is based at$y _ { 0 }$, the based mapping space

$$
\operatorname{Map} _ {*} (X, Y) \subseteq \operatorname{Map} (X, Y)
$$

is the subspace of based maps, i.e., the maps$f \colon X \to Y$with$f ( x _ { 0 } ) = y _ { 0 }$. It is itself a based space, with base point ∗ the constant map to y<sub>0</sub>.

[[Note that [X, Y ] will be used with a completely diferent meaning later. Forward reference.]]

[[The restriction to locally compact$Y$suggests that these are not quite the right foundations for efective algebraic topology or homotopy theory. Indeed, we shall [[or may?]] instead work in the full subcategory of so-called compactly generated spaces, to be discussed in Section 5.3. However, for the following definitions, the classical foundations sufice. Our notations are based on [43].]]

Definition 5.1.13. Let$I = [ 0 , 1 ] \subset \mathbb { R }$. It is a compact Hausdorf space. The cylinder on a space X is the cartesian product$X \times I$. For each$t \in I$there is an inclusion map$i _ { t } \colon X \to X \times I$given by$i _ { t } ( x ) = ( x , t )$. A homotopy between maps$f , g \colon X \to Y$is a map$H \colon X \times I \to Y$such that$H i _ { 0 } = f$and$H i _ { 1 } = g$

![](images/page_106_image_11.jpg)

We then say that$f$and$g$are homotopic, and write$H \colon f \simeq g$or just$f \simeq g .$ This defines an equivalence relation on the set of maps$X  Y$. We write$[ f ]$ for the homotopy class of a map$f \colon X \to Y$

Let Ho(Top) be the homotopy category of topological spaces, with the same objects as Top, and with morphism sets

$$
\operatorname{Ho} (\mathbf {T o p}) (X, Y) = \mathbf {T o p} (X, Y) / \simeq ,
$$

the homotopy classes of maps X → Y. Composition is defined by$[ g ] \circ [ f ] = [ g f ]$2 and there is a canonical functor Top$\begin{array} { r l } { \mathbf { \Lambda } } & { { } \to \mathrm { ~ H o ( T o p ) } } \end{array}$, taking$\textit { f }  { t o } [ f ] . \quad \mathrm { A }$map $f \colon X \ \to \ Y$is called a homotopy equivalence if its homotopy class$[ f ]$is an isomorphism in$\mathbf { H o ( T o p ) }$, i.e., if there exists a map$g \colon Y \to X$and homotopies $g f \simeq i d _ { X }$and$f g \simeq i d _ { Y }$. Such a map$g$is called a homotopy inverse to$f .$ Any two homotopy inverses to$f$are homotopic, by uniqueness of inverses in Ho(Top).

Definition 5.1.14. Let$I = [ 0 , 1 ]$be based at 0. The (based) cylinder on a based space$( X , x _ { 0 } )$is the smash product

$$
X \wedge I _ {+} \cong X \times I / \{x _ {0} \} \times I.
$$

We write x$\wedge t$for the image of$( x , t )$. For each$t \in I$there is a based inclusion map$i _ { t } \colon X \to X \wedge I _ { + }$given by$i _ { t } ( x ) = x \wedge t . \mathrm { ~ A ~ }$(based) homotopy between based maps$f , g \colon ( X , x _ { 0 } ) \to ( Y , y _ { 0 } )$is a based map$H \colon X \wedge I _ { + } \to Y$such that$H i _ { 0 } = f$ and$H i _ { 1 } = g$

![](images/page_107_image_3.jpg)

We then say that$f$and$g$are (based) homotopic, and write$H \colon f \simeq g$or just $f \simeq g$. This defines an equivalence relation on the set of based maps$X  Y$

Let$\mathrm { H o } ( \mathbf { T o p } _ { * } )$be the homotopy category of based topological spaces, with the same objects as Top , and with morphism sets

$$
\operatorname{Ho} \left(\mathbf {T o p} _ {*}\right) \left(\left(X, x _ {0}\right), \left(Y, y _ {0}\right)\right) = \mathbf {T o p} _ {*} \left(\left(X, x _ {0}\right), \left(Y, y _ {0}\right)\right) / \simeq ,
$$

the based homotopy classes of based maps$( X , x _ { 0 } )  ( Y , y _ { 0 } )$. Composition is defined by$[ g ] \circ [ f ] = [ g f ]$, and there is a canonical functor$\mathbf { T o p } _ { \ast }  \mathrm { H o } ( \mathbf { T o p } _ { \ast } )$2 taking$f$to [f]. A map$f \colon ( X , x _ { 0 } )  ( Y , y _ { 0 } )$is called a based homotopy equivalence if its homotopy class$[ f ]$is an isomorphism in$\mathrm { H o } ( \mathbf { T o p } _ { * } )$, i.e., if there exists a based map$g \colon ( Y , y _ { 0 } )  ( X , x _ { 0 } )$and based homotopies$g f \simeq i d _ { ( X , x _ { 0 } ) }$ and$f g \simeq i d _ { ( Y , y _ { 0 } ) }$. Such a map g is called a based homotopy inverse to$f .$ Any two based homotopy inverses to$f$are based homotopic, by uniqueness of inverses in$\mathrm { H o } ( \mathbf { T o p } _ { * } )$

Definition 5.1.15. When$( X , x _ { 0 } )$has the based homotopy type of a CW complex, and$( Y , y _ { 0 } )$is any based space, we write

$$
[ X, Y ] = \operatorname{Ho} (\mathbf {T o p} _ {*}) ((X, x _ {0}), (Y, y _ {0}))
$$

for the based homotopy classes of maps from$( X , x _ { 0 } )$to$( Y , y _ { 0 } )$. [[If X does not have such a homotopy type, one should first replace X by a weakly equivalent CW complex ΓX.]]

Remark 5.1.16. Any based homotopy equivalence of based spaces is a homotopy equivalence of the underlying unbased spaces. If the spaces are cofibrantly based, meaning that the base point inclusions are cofibrations, then the converse also holds. See Proposition 5.4.17.

Definition 5.1.17. Let X be any space. The (unreduced) cone

$$
C X = X \times I / i _ {0} (X)
$$

is the pushout of$i _ { 0 } \colon X \to X \times I$and the unique map$X  *$. We write$[ x , t ]$ for the image of$( x , t )$in CX. There is an inclusion$i _ { 1 } \colon X \to C X$at the free end of the cone. The (unreduced) suspension

$$
\Sigma X = C X / i _ {1} (X)
$$

is the pushout of$i _ { 1 }$and the unique map$X  *$

For each map$f \colon X \to Y$we can form the mapping cylinder

$$
M f = Y \cup_ {f} X \times I,
$$

defined as the pushout of$f$and the inclusion$i _ { 1 } \colon X \to X \times I$. The inclusion $i _ { 0 } \colon X \to X \times I$induces an inclusion$i _ { 0 } \colon X \to M f$. The projection$p r _ { 1 } \colon X \times I$ X induces a cylinder projection map$\pi \colon M f \to Y$, making the following diagram commute:

![](images/page_108_image_4.jpg)

It is easy to see that$\pi$and the inclusion$Y  M f$are inverse homotopy equivalences. The composite$Y  Y$is the identity, while the composite$M f  M f$ is homotopic to the identity by a map that contracts the cylinder$X \times I$to the base$X \times \{ 1 \}$. We define the mapping cone, or homotopy cofiber, to be

$$
C f = Y \cup_ {f} C X \cong M f / i _ {0} (X).
$$

There is a canonical inclusion i:$Y  C f ;$

![](images/page_108_image_8.jpg)

Definition 5.1.18. Let$S ^ { 1 } = I / \partial I$be based at$0 \sim 1$, where$\partial I = \{ 0 , 1 \} \subset I$ Let$( X , x _ { 0 } )$be any based space. The (based) cone

$$
C X = X \wedge I \cong (X \wedge I _ {+}) / i _ {0} (X)
$$

is the pushout of$i _ { 0 } \colon X \to X \wedge I _ { + }$and$X \to *$. Again there is a based inclusion $i _ { 1 } \colon X \to C X$at the free end of the cone. The (based) suspension

$$
\begin{array}{c} \Sigma X = X \wedge S ^ {1} \cong C X / i _ {1} (X) \\ \cong X \times I / (X \times \{0, 1 \} \cup \{x _ {0} \} \times I) \end{array}\tag{5.1}
$$

(5.2)

is the pushout of$i _ { 1 }$and the map$X  *$

For each based map$f \colon ( X , x _ { 0 } )  ( Y , y _ { 0 } )$the (based) mapping cylinder

$$
M f = Y \cup_ {f} X \wedge I _ {+}
$$

is the based pushout of$f$and$i _ { 1 } \colon X \to X \wedge I _ { + }$. The based inclusion$i _ { 0 } \colon X \to$ $X \wedge I _ { + }$induces a based inclusion$i _ { 0 } \colon X \to M f$, and the (based) mapping cone of$f ,$or homotopy cofiber, is

$$
C f = Y \cup_ {f} C X \cong M f / i _ {0} (X).
$$

More explicitly,$C f$is the identification space$( Y \sqcup X \times I ) / { \sim }$, where$x \simeq f ( x )$ for all$x \in X$, and$X \times \{ 0 \} \cup \{ x _ { 0 } \} \times I$is collapsed to the base point.

There is a canonical based inclusion i:$Y  C f ,$, and a canonical based homotopy$( x , t ) \mapsto x \wedge t$from the constant map to the base point$^ { \ast } \ \mathrm { t o }$the composite map

$$
i f \colon X \xrightarrow {f} Y \xrightarrow {i} C f.
$$

Remark 5.1.19. The suspension ΣX equals the mapping cone of the unique map$X  *$. There is a canonical map

$$
C f = Y \cup_ {X} C X \rightarrow Y \cup_ {X} * = Y / f (X),
$$

from the homotopy cofiber to the categorical cofiber of$f \colon X \to Y$, which is the identity on$Y$and collapses$C X$to ∗. It is a homotopy equivalence if$f$is a cofibration, see Lemma 5.5.3.

Definition 5.1.20. The free path space of a space Y is the mapping space $\operatorname { M a p } ( I , Y )$. For each$t \in I$there is an evaluation map$e _ { t } \colon \mathrm { M a p } ( I , Y ) \to Y$given by$e _ { t } ( \alpha ) = \alpha ( t )$. [[Each$e _ { t }$is a proclusion.]] Given a point$y _ { 0 } \in Y$, the path space

$$
P _ {y _ {0}} Y = e _ {0} ^ {- 1} (y _ {0}) \subseteq \mathrm{Map} (I, Y)
$$

of$Y$at$y _ { 0 }$is the subspace consisting of paths α :$I  Y$with$\alpha ( 0 ) = y _ { 0 }$. It is the pullback of$e _ { 0 } \colon \mathrm { M a p } ( I , Y ) \to Y$and the inclusion$\{ y _ { 0 } \} \subseteq Y$. There is an evaluation map e<sub>1</sub> :$P _ { y _ { 0 } } Y  Y$. The loop space

$$
\Omega_ {y _ {0}} Y = e _ {1} ^ {- 1} (y _ {0}) \subseteq P _ {y _ {0}} Y
$$

of$Y$at$y _ { 0 }$is the pullback of$e _ { 1 } \colon P _ { y _ { 0 } } Y \to Y$and the inclusion$\{ y _ { 0 } \} \subseteq Y$. It is the subspace of$\operatorname { M a p } ( I , Y )$consisting of loops$\alpha \colon I  Y .$, with$\alpha ( 0 ) = \alpha ( 1 ) = y _ { 0 }$

The mapping path space of a map$f \colon X \to Y$is the pullback

$$
N f = X \times_ {Y} \operatorname{Map} (I, Y)
$$

of$f$and the evaluation map$e _ { 1 } \colon \mathrm { M a p } ( I , Y ) \to Y$. Its elements are pairs$( x , \alpha )$2 where$x \in X , \alpha \colon I \to Y$and$\alpha ( 1 ) = f ( x )$. The evaluation$e _ { 0 } \colon \mathrm { M a p } ( I , Y ) \to Y$ induces a map$e _ { 0 } \colon N f \to Y .$, taking$( x , \alpha )$to$\alpha ( 0 )$. [[This is a proclusion.]] The inclusion$Y  \mathrm { M a p } ( I , Y )$, taking$y \in Y$to the constant path$c _ { y } \colon s \mapsto y ,$ induces a map$\iota \colon X \to N f$that takes$x \in X$to$( x , c _ { f ( x ) } )$. The following diagram commutes:

![](images/page_109_image_13.jpg)

Again, it is easy to see [[Give proof]] that ι and the projection$N f  X$are inverse homotopy equivalences. Given a point$y _ { 0 } \in Y$, the homotopy fiber

$$
F _ {y _ {0}} f = X \times_ {Y} P _ {y _ {0}} Y = e _ {0} ^ {- 1} (y _ {0}) \subseteq N f
$$

of$f \colon X \to Y$at y is the subspace consisting of pairs$( x , \alpha )$where$x \in X , \alpha \colon I \to$ $Y , \alpha ( 0 ) = y _ { 0 }$and$\alpha ( 1 ) = f ( x )$. There is a canonical projection$p \colon F f \to X$

![](images/page_109_image_17.jpg)

Definition 5.1.21. For each based space$( Y , y _ { 0 } )$we identify the (based) free mapping space

$$
\operatorname{Map} _ {*} (I _ {+}, Y) \cong \operatorname{Map} (I, Y)
$$

with the free path space, but based at the constant map c :$I \to Y$to$y _ { 0 } \in I .$The evaluation maps$e _ { t }$:$\mathrm { M a p } _ { * } ( I _ { + } , Y ) \to Y$are base-point preserving. We identify the (based) path space

$$
P Y = \operatorname{Map} _ {*} (I, Y) \cong P _ {y _ {0}} Y
$$

with the (unbased) path space, but based at c. Likewise, we identify the (based) loop space

$$
\Omega Y = \operatorname{Map} _ {*} (S ^ {1}, Y) \cong \Omega_ {y _ {0}} Y
$$

with the (unbased) loop space, but based at c.

For each based map$f \colon ( X , x _ { 0 } )  ( Y , y _ { 0 } )$, the (based) mapping path space

$$
N f = X \times_ {Y} \operatorname{Map} _ {*} (I _ {+}, Y) \cong X \times_ {Y} \operatorname{Map} (I, Y)
$$

is based at$( x _ { 0 } , c )$, with c as above. The (based) homotopy fiber

$$
F f = X \times_ {Y} P Y \cong X \times_ {Y} P _ {y _ {0}} Y
$$

is based at$( x _ { 0 } , c )$. More explicitly,$F f$is the subspace of$X \times \operatorname { M a p } ( I , Y )$consisting of pairs$( x , \alpha )$with$x \in X$and$\alpha \colon I  Y$, such that$\alpha ( 0 ) = y _ { 0 }$and $\alpha ( 1 ) = f ( x )$, based at$( x _ { 0 } , c )$

There is a canonical based projection$p \colon F f \to X$, and a canonical homotopy $( ( x , \alpha ) , t ) \mapsto \alpha ( t )$from the constant map to y<sub>0</sub> to the composite map

$$
f p \colon F f \xrightarrow {p} X \xrightarrow {f} Y.
$$

Remark 5.1.22. The loop space$\Omega Y$of$( Y , y _ { 0 } )$equals the homotopy fiber of the inclusion$\{ y _ { 0 } \} \subseteq Y$. There is a canonical map

$$
f ^ {- 1} (y _ {0}) = X \times_ {Y} \left\{y _ {0} \right\}\rightarrow X \times_ {Y} P Y = F f,
$$

from the categorical fiber of a based map$f \colon ( X , x _ { 0 } )  ( Y , y _ { 0 } )$to the homotopy fiber, which takes x with$f ( x ) = y _ { 0 }$to$( x , c )$, where c is the constant path at y<sub>0</sub>. It is a homotopy equivalence if f is a fibration [[forward reference]]. More generally, it is a weak homotopy equivalence if$f$is a quasi-fibration [[forward reference]].

We now turn to the cartesian closed structure on Top, meaning the relation between$( - ) \times Y$and$\mathrm { M a p } ( Y , - )$, and similarly for$( - ) \wedge Y$and Map$( Y , - )$in Top<sub>∗</sub>.

Lemma 5.1.23. If$g \colon Y \to Z$is a map, then

$$
X \times g \colon X \times Y \to X \times Z
$$

sending$( x , y )$to$( x , g ( y ) )$, and

$$
\operatorname{Map} (X, g) \colon \operatorname{Map} (X, Y) \to \operatorname{Map} (X, Z)
$$

sending f to$g f ,$are continuous.

If$g \colon ( Y , y _ { 0 } )  ( Z , z _ { 0 } )$is a based map, then

$$
X \wedge g \colon X \wedge Y \to X \wedge Z
$$

sending$x \land y \ t o \ x \land g ( y )$, and

$$
\operatorname{Map} _ {*} (X, g) \colon \operatorname{Map} _ {*} (X, Y) \to \operatorname{Map} _ {*} (X, Z)
$$

sending f to$g f ,$, are continuous.

$$
[ [ A l s o f o r \operatorname{Map} (g, W)? ] ]
$$

Proof. The case of cartesian products is obvious, and the based case of smash products follows, since$X \wedge g$is continuous if and only if its composite with $\pi \colon X \times Y \to X \land Y$is continuous, which is clear.

Let$f \colon X \ \to \ Y$, and consider a subbasis neighborhood$[ K , U ]$of$g f =$ $\operatorname { M a p } ( X , g ) ( f ) : X \to Z$, with$K$compact in X and U open in$Z$. Then$g ^ { - 1 } ( U )$is open in$Y , [ K , g ^ { - 1 } ( U ) ]$is a neighborhood of$f _ { : }$and$\operatorname { M a p } ( X , g )$takes$[ K , g ^ { - 1 } ( \dot { U } ) ]$ into$[ K , U ]$. It follows that$\operatorname { M a p } ( X , g )$is continuous.

The based case follows, since$\operatorname { M a p } _ { * } ( X , g )$is continuous if and only if its composite with the inclusion$\mathrm { M a p } _ { * } ( X , Z ) \subseteq \mathrm { M a p } ( X , Z )$is continuous, which is clear from the unbased case.□

Lemma 5.1.24. Fix a space$Y$. Let$\eta _ { X } \colon X \to \operatorname { M a p } ( Y , X \times Y )$be given by $\eta _ { X } ( x ) = i _ { x } \in \operatorname { M a p } ( Y , X \times Y )$where$i _ { x } ( y ) = ( x , y )$. Then$\eta _ { X }$is continuous, so there is a natural transformation (of functors$\mathbf { T o p } ^ { o p } \times \mathbf { T o p }  \mathbf { S e t } )$

$$
\phi_ {X, Z} \colon \operatorname{Top} (X \times Y, Z) \longrightarrow \operatorname{Top} (X, \operatorname{Map} (Y, Z))
$$

that takes$f \colon X \times Y \to Z$to the composite map

$$
X \xrightarrow {\eta_ {X}} \operatorname{Map} (Y, X \times Y) \xrightarrow {\operatorname{Map} (Y , f)} \operatorname{Map} (Y, Z).
$$

$I f X , Y , Z$are based there is a natural based map$\eta _ { X } \colon X \to \mathrm { M a p } _ { * } ( Y , X \wedge Y )$ given by$\eta _ { X } ( x ) = \pi i _ { x } \in \operatorname { M a p } _ { * } ( Y , X \wedge Y )$. Also the based map η<sub>X</sub> is continuous, so there is a natural transformation (of functors$\mathbf { T o p } _ { * } ^ { o p } \times \mathbf { T o p } _ { * } \to \mathbf { S e t } _ { * } )$

$$
\phi_ {X, Z} \colon \operatorname{Top} _ {*} (X \wedge Y, Z) \longrightarrow \operatorname{Top} _ {*} (X, \operatorname{Map} _ {*} (Y, Z))
$$

that takes a based map$f \colon X \wedge Y \to Z$to the composite based map

$$
X \xrightarrow {\eta_ {X}} \operatorname{Map} _ {*} (Y, X \wedge Y) \xrightarrow {\operatorname{Map} _ {*} (Y , f)} \operatorname{Map} _ {*} (Y, Z).
$$

Proof. Let$x \in X$and consider a subbase neighborhood$[ K , W ]$of$i _ { x } ,$with $K \subseteq Y$compact and$W \subseteq X \times Y$open.$\mathrm { B y }$assumption$\{ x \} \times K \subseteq W$. For each$y \in K$we find a basis neighborhood$U _ { y } \times V _ { y }$of$( x , y )$contained in W. The $\{ V _ { y } \}$for$y \in K$cover$K ,$, so there is a finite set$y _ { 1 } , \dotsc , y _ { n } \in K$such that the $\{ V _ { y _ { i } } \} _ { i = 1 } ^ { n }$cover$K$. Let$U = U _ { y _ { 1 } } \cap \cdot \cdot \cdot \cap U _ { y _ { n } }$. Then$\eta _ { X }$maps U into$[ K , W ]$, so η is continuous.

The based case follows, since the based$\eta _ { X }$is continuous if and only if its composite with the inclusion$\mathrm { M a p } _ { * } ( Y , X \wedge Y ) \subseteq \mathrm { M a p } ( Y , X \wedge Y )$is continuous, and this follows from Lemma 5.1.23 applied to$\pi \colon X \times Y \to X \wedge Y$and the unbased case.口

Definition 5.1.25. A space Y is locally compact if for any point$y \in Y$and each open neighborhood$U \subseteq Y$of$y ,$there exists a smaller compact neighborhood $K \subseteq U$of$y$.

Remark 5.1.26. For example, each compact Hausdorf space is locally compact, since y and the closed complement of$U$can be separated by open neighborhoods. The complement of the open neighborhood of$U$is then a closed neighborhood of$y ,$which is compact.

Lemma 5.1.27. Fix a space Y. Let$\epsilon _ { Z } \colon \mathrm { M a p } ( Y , Z ) \times Y \to Z$be given by $\epsilon _ { Z } ( f , y ) ) = f ( y ) \in Z$where$f \colon Y \to Z$and$y \in Y , ~ I f Y$is locally compact, then $\epsilon _ { Z }$is continuous, so there is a natural transformation

$$
\psi_ {X, Z} \colon \operatorname{Top} (X, \operatorname{Map} (Y, Z)) \longrightarrow \operatorname{Top} (X \times Y, Z)
$$

that takes$g \colon X \to \operatorname { M a p } ( Y , Z )$to the composite map

$$
X \times Y \xrightarrow {g \times Y} \operatorname{Map} (Y, Z) \times Y \xrightarrow {\epsilon_ {Z}} Z.
$$

$I f X , Y , Z$are based there is a natural based map$\epsilon _ { Z } \colon \mathrm { M a p } _ { * } ( Y , Z ) \wedge Y  Z$ given by$\epsilon _ { Z } ( f \wedge y ) = f ( y ) \in Z$. If Y is locally compact then also the based map $\epsilon _ { Z }$is continuous, so there is a natural transformation

$$
\psi_ {X, Z} \colon \operatorname{Top} _ {*} (X, \operatorname{Map} _ {*} (Y, Z)) \longrightarrow \operatorname{Top} _ {*} (X \wedge Y, Z)
$$

that takes a based map$g \colon X \to \mathrm { M a p } _ { * } ( Y , Z )$to the composite based map

$$
X \wedge Y \xrightarrow {g \wedge Y} \operatorname{Map} _ {*} (Y, Z) \wedge Y \xrightarrow {\epsilon_ {Z}} Z.
$$

Proof. Let$( f , y ) \in \mathrm { M a p } ( Y , Z ) \times Y$, and consider any open neighborhood W of$f ( y ) \in Z .$. Then$f ^ { - 1 } ( W )$is an open neighborhood of$y \in Y$. By the key assumption that Y is locally compact there exists a compact neighborhood$K \subseteq$ $f ^ { - 1 } ( W )$) of y in Y. Then$[ K , W ] \times K$is a neighborhood of$( f , y )$in$\mathrm { M a p } ( Y , Z ) \times Y$ and$\epsilon _ { Z }$takes it into W. Hence$\epsilon _ { Z }$is continuous.

Finally, the based$\epsilon _ { Z }$is continuous if and only if its composite with the canonical map π$: \ \mathrm { M a p } _ { * } ( Y , Z ) \times Y  Z$is continuous, and this follows from the unbased case.□

Proposition 5.1.28. Let$Y$be a locally compact space. There is a natural bijection

$$
\phi_ {X, Z} \colon \mathbf {T o p} (X \times Y, Z) \cong \mathbf {T o p} (X, \operatorname{Map} (Y, Z))
$$

that exhibits the functors$X \mapsto X \times Y$and$Z \mapsto \operatorname { M a p } ( Y , Z )$as the left and right $a d j o i n t ,$respectively, in an adjoint pair.

$$
\text { Top } \xrightarrow [ \text { Map } (Y , -) ]{(-) \times Y} \text { Top }
$$

The adjunction unit and counit are$\eta _ { X } \colon X \to \operatorname { M a p } ( Y , X \times Y )$and$\epsilon _ { Z } \colon \mathrm { M a p } ( Y , Z ) \times$ $Y  Z$, respectively.

$I f X , Y , Z$are based and Y is locally compact, there is also a natural bijection

$$
\phi_ {X, Z} \colon \mathbf {T o p} _ {*} (X \wedge Y, Z) \cong \mathbf {T o p} _ {*} (X, \operatorname{Map} _ {*} (Y, Z))
$$

that exhibits the functors$X \mapsto X \wedge Y$and$Z \mapsto \mathrm { M a p } _ { * } ( Y , Z )$as the$l e f t$and right adjoint, respectively, in an adjoint pair.

$$
\mathbf {T o p} _ {*} \xrightarrow [ \text {Map} _ {*} (Y , -) ]{(-) \wedge Y} \mathbf {T o p} _ {*}
$$

The adjunction unit and counit are

$$
\begin{array}{r} \eta_ {X} \colon X \to \mathrm{Map} _ {*} (Y, X \wedge Y) \\ \epsilon_ {Z} \colon \mathrm{Map} _ {*} (Y, Z) \wedge Y \to Z \end{array}
$$

respectively.

Proof. The composite

$$
X \times Y \stackrel {{\eta_ {X} \times Y}} {{\longrightarrow}} \operatorname{Map} (Y, X \times Y) \times Y \stackrel {{\epsilon_ {X \times Y}}} {{\longrightarrow}} X \times Y
$$

takes$( x , y )$first to$( i _ { x } , y )$and then to$i _ { x } ( y ) = ( x , y )$, hence equals the identity. It follows that the composite$\psi _ { X , Z } \circ \phi _ { X , Z }$is the identity, since it takes$f \colon X \times$ $Y  Z$first to the composite$\operatorname* { M a p } ( Y , f ) \circ \eta _ { X }$, and then to the composite$\epsilon _ { Z } \circ$ $( ( \operatorname { M a p } ( Y , f ) \circ \eta _ { X } ) \times Y ) = \epsilon _ { Z } \circ ( \operatorname { M a p } ( Y , f ) \times Y ) \circ ( \eta _ { X } \times Y )$, which by naturality of ǫ equals$f \circ \epsilon _ { X \times Y } \circ ( \eta _ { X } \times Y ) ) = f \circ i d = f .$

Likewise, the composite

$$
\operatorname{Map} (Y, Z) \stackrel {{\eta_ {\operatorname{Map} (Y, Z)}}} {{\longrightarrow}} \operatorname{Map} (Y, \operatorname{Map} (Y, Z) \times Y) \stackrel {{\operatorname{Map} (Y, \epsilon_ {Z})}} {{\longrightarrow}} \operatorname{Map} (Y, Z)
$$

takes f first to$i _ { f } \colon y \mapsto ( f , y )$and then to$y \mapsto f ( y )$, hence equals the identity. It follows that the composite$\phi _ { X , Z } \circ \psi _ { X , Z }$is the identity, since it takes $g \colon X \to \operatorname { M a p } ( Y , Z )$first to the composite ǫ<sub>Z</sub>$\circ ( g \times Y )$, and then to the composite${ \mathrm { M a p } } ( Y , \epsilon _ { Z } \circ ( g \times Y ) ) \circ \eta _ { X } = { \mathrm { M a p } } ( Y , \epsilon _ { Z } ) \circ { \mathrm { M a p } } ( Y , g \times Y ) \circ \eta _ { X }$, which by naturality of η with respect to g equals Map$\begin{array} { r } { ( Y , \epsilon _ { Z } ) \circ \eta _ { \mathrm { M a p } ( Y , Z ) } \circ g = i d \circ g = g . } \end{array}$

The proof in the based case goes the same way.口

Corollary 5.1.29. There are natural bijections

$$
\begin{array}{r l} & {\mathbf {T o p} _ {*} (X \wedge I _ {+}, Z) \cong \mathbf {T o p} _ {*} (X, \mathrm{Map} _ {*} (I _ {+}, Z))} \\ & {\quad \mathbf {T o p} _ {*} (C X, Z) \cong \mathbf {T o p} _ {*} (X, P Z)} \\ & {\quad \mathbf {T o p} _ {*} (\Sigma X, Z) \cong \mathbf {T o p} _ {*} (X, \Omega Z)} \end{array}
$$

for based spaces$X , Z .$Hence each based homotopy$H \colon X \wedge I _ { + } \to Z$from f to g corresponds to a based map$K \colon X \to \operatorname { M a p } _ { * } ( I _ { + } , Z )$with$e _ { 0 } K = f$and$e _ { 1 } K = g _ { ; }$ and conversely.

The adjunction unit in the third case is$\eta _ { X } \colon X \to \Omega \Sigma X$taking x to the based loop$s \mapsto x \wedge s ~ f o r ~ s \in S ^ { 1 }$, and the counit is$\epsilon _ { Z } \colon \Sigma \Omega Z  Z$taking s ∧ α to$\alpha ( s )$，where$\alpha \colon S ^ { 1 } \to Z$is a based loop.

Proof. These are the special cases$Y = I _ { + } , Y = I$and$Y = S ^ { 1 }$of the previous proposition.□

## 5.2 CW complexes

The definition of a topological space is general enough to allow many quite ill-behaved examples. However, the classifying spaces of categories, and most of the other topological spaces that will be important for our study of higher algebraic K-theory, are rather more well-behaved, in that they can be built up from nothing by successive attachments of cells. More precisely they are CW complexes, which we review in this section.

Definition 5.2.1. For$n \geq 0$, let the$n { - } d i s k$

$$
D ^ {n} = \{(x _ {1}, \dots , x _ {n}) \in \mathbb {R} ^ {n} \mid \sum_ {i = 1} ^ {n} x _ {i} ^ {2} \leq 1 \}
$$

be the unit ball in Euclidean n-space, and let the (n − 1)-sphere

$$
S ^ {n - 1} = \left\{\left(x _ {1}, \dots , x _ {n}\right) \in \mathbb {R} ^ {n} \mid \sum_ {i = 1} ^ {n} x _ {i} ^ {2} = 1 \right\}
$$

be its boundary,$S ^ { n - 1 } = \partial D ^ { n }$. For$n \geq 1$we view$D ^ { n }$and$S ^ { n - 1 }$as being based at the point$e _ { 1 } = ( 1 , 0 , \ldots , 0 )$. Note that$D ^ { 0 }$is a point and$S ^ { - 1 } = \emptyset$

[[Note that we here index the coordinates of$\mathbb { R } ^ { n }$from 1 to$n . ] ]$

Definition 5.2.2. A CW complex is a space$Y$with a CW-structure, i.e., an increasing skeleton filtration

$$
\emptyset = Y ^ {(- 1)} \subseteq Y ^ {(0)} \subseteq \dots \subseteq Y ^ {(n - 1)} \subseteq Y ^ {(n)} \subseteq \dots \subseteq Y
$$

where for each$n \geq 0$the n-skeleton$Y ^ { ( n ) }$is obtained from the$( n - 1 )$)-skeleton by the adjunction of a set of n-cells along their boundaries, so that there is a pushout square:

$$
\begin{array}{c} \coprod_ {\alpha} S ^ {n - 1} \xrightarrow {\phi^ {n}} Y ^ {(n - 1)} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \\ \coprod_ {\alpha} D ^ {n} \xrightarrow {\Phi^ {n}} Y ^ {(n)} \end{array}
$$

Here α runs through the set$Y _ { n } ^ { \sharp }$of n-cells in$Y$, the map$\phi ^ { n }$is the coproduct of maps$\phi _ { \alpha } \colon S ^ { n - 1 } \to { \overline { { Y } } } ^ { ( n - 1 ) }$, called the attaching maps, and the map$\Phi ^ { n }$is the co-product of maps$\Phi _ { \alpha } \colon D ^ { n } \to Y ^ { ( n ) }$, called the characteristic maps. Furthermore, $Y$is the increasing union of its skeleta

$$
Y = \bigcup_ {n \geq 0} Y ^ {(n)} = \operatorname * {c o l i m} _ {n \geq 0} Y ^ {(n)}
$$

and is given the weak topology, meaning the finest topology such that each inclusion$Y ^ { ( n ) }  Y$is continuous. Equivalently, a subspace$U \subseteq Y$is open (resp. closed) if and only if each intersection$Y ^ { ( n ) } \cap U$is open (resp. closed) in$Y ^ { ( n ) }$, or equivalently, if each preimage$\Phi _ { \alpha } ^ { - 1 } ( U )$is open (resp. closed) in$D ^ { n }$

Definition 5.2.3. A CW complex Y is finite dimensional if there is an integer d such that Y has no n-cells for$n > d .$The minimal such d is then called the dimension of Y. A CW complex is of finite type if for each$n \geq 0$there are only finitely many n-cells in Y. It is finite if it is finite dimensional and of finite type, or equivalently, if the total number of cells in all dimensions is finite.

Lemma 5.2.4. A CW complex is finite if and only if it is compact as a topological space.

Proof. [[If there are infinitely many cells, choose a non-repeating sequence$( \alpha _ { i } ) _ { i = 1 } ^ { \infty }$1 of them. The center points$x _ { i }$in these cells then form a sequence in$Y$with no convergent subsequence.]]□

Definition 5.2.5. A map$f \colon X \to Y$of CW complexes is cellular if$f ( X ^ { ( n ) } ) \subseteq$ $Y ^ { ( n ) }$for all$n \geq 0$. CW complexes and cellular maps form a subcategory

$$
\mathbf {C W} \subset \mathbf {T o p}
$$

of topological spaces. Note that this subcategory is not full.

[[Based CW complexes: two interpretations!]]

Definition 5.2.6. A closed subspace X of a CW complex Y is a subcomplex if for each$n \geq 0$, the n-skeleton$\mathbf { \bar { \chi } } ^ { ( n ) } = X \cap Y ^ { ( n ) }$is obtained by adjoining a subset$X _ { n } ^ { \sharp } \subseteq Y _ { n } ^ { \sharp }$of the n-cells in Y to the$( n - 1 )$-skeleton$X ^ { ( n - 1 ) }$. We then say that$X \subseteq Y$or$( Y , X )$a CW pair.

Lemma 5.2.7. Let X be a subcomplex of a CW complex Y. Then the subspace topology on X equals the weak topology with respect to the subspaces$X ^ { ( n ) }$, so that X is itself a CW complex. The inclusion$X \subseteq Y$is a cellular map.

Proof. A subset$L \subseteq X$is closed in the weak topology if and only if each$X ^ { ( n ) } \cap L$ is closed in$X ^ { ( n ) }$. Each$X ^ { ( n ) }$is closed in$Y ^ { ( n ) }$, so this is equivalent to asking that each$Y ^ { ( n ) } \cap L$is closed in$Y ^ { ( n ) }$. This is the same as saying that L is closed in$Y .$. Since X is closed in${ \cal Y } ,$this is equivalent to$L \subseteq X$being closed in the subspace topology.□

Lemma 5.2.8. Let Y, Z be CW complexes,$X \subseteq Y$a subcomplex, and$f \colon X \to$ Z a cellular map. Then$Y \cup _ { X } Z$is a CW complex, with n-skeleton

$$
(Y \cup_ {X} Z) ^ {(n)} = Y ^ {(n)} \cup_ {X ^ {(n)}} Z ^ {(n)},
$$

one n-cell for each n-cell in Y that is not contained in X, and one n-cell for each n-cell in Z. The characteristic maps are the composites$D ^ { n } \to Y ^ { ( n ) } \to$ $( Y \cup _ { X } Z ) ^ { ( n ) }$and$D ^ { n } \to Z ^ { ( n ) } \to ( Y \cup _ { X } Z ) ^ { ( n ) }$, respectively. The square

![](images/page_115_image_13.jpg)

is a pushout in CW.

Definition 5.2.9. Let X and Y be CW complexes, with characteristic maps $\Phi _ { \alpha }$and$\Psi _ { \beta }$. The product CW complex$X \times Y$has n-skeleton

$$
(X \times Y) ^ {(n)} = \bigcup_ {i + j = n} X ^ {(i)} \times Y ^ {(j)}
$$

for each$n \geq 0 .$and one$( i + j )$-cell for each i-cell α in$X$and each j-cell$\beta$in$Y$, with characteristic map

$$
\Theta_ {\alpha , \beta} \colon D ^ {i + j} \cong D ^ {i} \times D ^ {j} \stackrel {\Phi_ {\alpha} \times \Psi_ {\beta}} {\longrightarrow} X ^ {(i)} \times Y ^ {(j)} \subseteq X ^ {(i + j)}  .
$$

Its restriction to the boundary

$$
S ^ {i + j - 1} = \partial D ^ {i + j} \cong \partial (D ^ {i} \times D ^ {j}) = S ^ {i - 1} \times D ^ {j} \cup D ^ {i} \times S ^ {j - 1}
$$

factors through the attaching map

$$
\begin{array}{c} \theta_ {\alpha , \beta} \colon S ^ {i + j - 1} \cong S ^ {i - 1} \cup D ^ {j} \cup D ^ {i} \times S ^ {j - 1} \\ \longrightarrow X ^ {(i - 1)} \times Y ^ {(j)} \cup X ^ {(i)} \times Y ^ {(j - 1)} \subseteq X ^ {(i + j - 1)}. \end{array}
$$

The product$X \times Y$has the weak topology with respect to the skeleton filtration, or equivalently, with respect to all of the characteristic maps$\Theta _ { \alpha , \beta }$

The projection maps pr<sub>1</sub> :$X \times Y  X$and pr<sub>2</sub> :$X \times Y  Y$are cellular, and$X \times Y$is the product in CW of X and Y.

Remark 5.2.10. Note that the weak topology on the product CW complex $X \times Y$is not always the same as the product topology on the cartesian product $X \times Y$, formed in Top. There is a map from the CW product with the weak topology, to the cartesian product with the product topology, but it is not in general a homeomorphism. [[Example?]] This suggests that the cartesian product topology, which is the coarsest topology making the projections to X and Y continuous, is too coarse, and that we should instead give$X \times Y \mathrm { ~ a ~ }$finer topology that agrees with the weak topology on a product of CW complexes in the case when X and$Y$are CW complexes. This is what is achieved with the compactly generated topology.

The following three lemmas are trivial to prove.

Lemma 5.2.11. Let$X \subseteq Y$be a CW pair and Z a CW complex. Then

$$
X \times Z \subseteq Y \times Z
$$

is a CW pair.

Lemma 5.2.12. Let X and$Y$be subcomplexes of a CW complex$Z .$Then $X \cap Y$and$X \cup Y$are also subcomplexes of Z.

Lemma 5.2.13. Let$X \subseteq Y$and$Z \subseteq W$be CW pairs. Then

$$
X \times W \cup_ {X \times Z} Y \times Z \subseteq Y \times W
$$

is a CW pair.

[[Cite Milnor on the homotopy type of$\operatorname { M a p } ( X , Y )$for X, Y CW complexes, with X finite?]]

## 5.3 Compactly generated spaces

[[Steenrod [62], McCord [45], May [43, Ch. 5].]]

[[Weak Hausdorf spaces, (Kelley) k-spaces, compactly generated spaces U and$\mathcal { T }$, closure under closed cobase change, closed sequential colimits, adjunction

$$
\operatorname{Map} (X \times Y, Z) \cong \operatorname{Map} (X, \operatorname{Map} (Y, Z))
$$

is a homeomorphism. Space = compactly generated space, based space = cofibrantly based compactly generated space.]]

## 5.4 Cofibrations

For more about cofibrations we refer to May [43, Ch. 6] and Hatcher$\left[ 2 6 , \mathrm { C h } . \mathrm { 0 } \right]$

Definition 5.4.1. A map$i \colon X \to Y$is said to have the homotopy extension property (HEP) with respect to a space T if for any commutative diagram of solid arrows

![](images/page_117_image_8.jpg)

there exists a dashed arrow making the whole diagram commute. The map i is called a cofibration if it has the homotopy extension property with respect to any space$T .$. We often use a feathered arrow$i \colon X \mapsto Y$to indicate that i is a cofibration.

Remark 5.4.2. In words and symbols, the homotopy extension property with respect to T asks that given a map$f \colon Y \to T$and a homotopy H :$X \times I  T$ starting with the composite map$f i \colon X \to T$, there exists a homotopy$F \colon Y \times$ $I  T$starting with$f ,$such that$F ( i \times i d ) = H$

Lemma 5.4.3. A map i:$X  Y$is a cofibration if and only if the induced map $j = i _ { 0 } \cup ( i \times i d ) \colon Y \cup _ { X } X \times I  Y \times I$admits a left inverse

$$
r \colon Y \times I \to Y \cup_ {X} X \times I.
$$

Proof. This is clear from the universal case$T = Y \cup _ { X } X \times I ,$with$f \colon Y \to T$ and$H \colon X \times I  T$the obvious inclusions.□

Here is a basic example.

Lemma 5.4.4. The inclusion$S ^ { n - 1 } \subset D ^ { n }$is a cofibration$f o r$each$n \geq 0$

Proof. View$D ^ { n } \times I$as a subspace of$\mathbb { R } ^ { n } \times \mathbb { R }$. There is a (deformation) retraction $r \colon D ^ { n } \times I \to D ^ { n } \times \{ 0 \} \cup S ^ { n - 1 } \times I$given by linear projection away from$( 0 , 2 ) \in$ $\mathbb { R } ^ { n } \times \mathbb { R }$, so$S ^ { n - 1 } \mapsto D ^ { n }$□

Lemma 5.4.5. Each cofibration$( i n \ : \mathcal { U } )$is a closed embedding.

Proof. Let$r$be left inverse to$j ,$as above. The composite

$$
X \stackrel {i} {\longrightarrow} Y \stackrel {i _ {1}} {\longrightarrow} Y \times I \stackrel {r} {\longrightarrow} Y \cup_ {X} X \times I
$$

equals the embedding$i _ { 1 } \colon X \to Y \cup _ { X } X \times I .$. Hence i must also be an embedding. (The open subsets of$X$are of the form$i _ { 1 } ^ { - 1 } ( U )$with$U$open in$Y \cup _ { X } X \times I .$, hence are also of the form$i ^ { - 1 } ( V )$with$V = \dot { ( r i _ { 1 } ) ^ { - 1 } } ( U )$open in$Y . )$The subspace

$$
B = \{x \in Y \mid j r (x, 1) = (x, 1) \}
$$

is equal to the image$i ( X )$of$i ,$and is closed in Y since Y is weak Hausdorf.

Lemma 5.4.6. A map i:$X  Y$is a cofibration$i f$and only if it has the$l e f t$ lifting property with respect to the free path fibration$e _ { 0 } \colon \mathrm { M a p } ( I , T ) \to T$for any space$T , i . e .$, given any commutative diagram of solid arrows

![](images/page_118_image_6.jpg)

there exists a dashed arrow making the whole diagram commute.

Proof. This is immediate from the isomorphism

$$
\mathbf {T o p} (Y \times I, T) \cong \mathbf {T o p} (Y, \operatorname{Map} (I, T))
$$

and its variants.

Lemma 5.4.7. Each homeomorphism is a cofibration, and the composite of two cofibrations is a cofibration, so the cofibrations form a subcategory of the category of topological spaces.

Proof. For the first claim, let${ \cal F } = H i ^ { - 1 }$, with notation as above.

If i :$X \ \mapsto \ Y$and$j \colon Y \mapsto Z$are cofibrations, then given a commutative diagram of solid arrows

![](images/page_118_image_14.jpg)

we use the left lifting property for i to find the dashed arrow$F ,$and then use the left lifting property for$j$to find the dashed arrow$G ,$making the whole diagram commute. Hence$j i \colon X \mapsto Z$is a cofibration.□

Lemma 5.4.8. (a) The coproduct$\begin{array} { r } { X = \coprod _ { \alpha } X _ { \alpha } \longmapsto \coprod _ { \alpha } Y _ { \alpha } = Y } \end{array}$of any set of cofibrations$i _ { \alpha } \colon X _ { \alpha } \to Y _ { \alpha }$is a cofibration.

(b) The pushout (= cobase change)$Z \longmapsto Y \cup _ { X } Z$of a cofibration i:$X \longmapsto Y$ along any map$j \colon X \to Z$is a cofibration.

(c) The composite$Y _ { - 1 }  Y$of a sequence of cofibrations$i _ { n } \colon Y _ { n - 1 } \longmapsto Y _ { n }$for $n \geq 0$, with$Y = \operatorname { c o l i m } _ { n } Y _ { n } ,$is a cofibration.

Proof. (a): Construct a lift$F _ { \alpha } \colon Y _ { \alpha } \to \operatorname { M a p } ( I , T )$for each$\alpha ,$and assemble these to a lift$F \colon Y \to \operatorname { M a p } ( I , T )$

(b): A left lifting problem for$Z \to Y \cup _ { X }$Z amounts to a diagram of solid arrows:

![](images/page_119_image_3.jpg)

The assumption that i is a cofibration gives the dashed arrow$F .$The fact that the left hand square is a pushout gives the dashed arrow$G ,$, making the whole diagram commute.

(c): A left lifting problem for$Y _ { - 1 }  Y$is given by the solid arrows in the following diagram, which is flipped over for typographical reasons.

![](images/page_119_image_6.jpg)

Assume inductively for$n \geq 0$that we have filled in the arrow$F _ { n - 1 } \colon Y _ { n - 1 } \to$ $\operatorname { M a p } ( I , T )$, starting the induction with$F _ { - 1 } = H$. Using the left lifting property for$i _ { n } ,$we can fill in the arrow$F _ { n } \colon Y _ { n } \to \operatorname { M a p } ( I , T )$, still keeping the diagram commutative. Now let$F \colon Y \to \operatorname { M a p } ( I , T )$be the colimit of the maps$F _ { n }$. It is continuous, because$Y = \mathrm { c o l i m } _ { n } Y _ { n }$is given the (weak) colimit topology.

Proposition 5.4.9. The inclusion$X \subseteq Y$of a subcomplex in a CW complex is a cofibration.

Proof. Let$Y _ { n } = X \cup Y ^ { ( n ) } \subseteq Y$, for each$n \geq - 1$. Hence there is a pushout square

![](images/page_119_image_10.jpg)

for each$n \geq 0$, where α ranges over the n-cells in Y that are not in X. By Lemmas 5.4.4 and 5.4.8, all the inclusions$S ^ { n - 1 } \to D ^ { n } , \operatorname { I I } _ { \alpha } S ^ { n - 1 } \to \operatorname { I I } _ { \alpha } D ^ { n }$, $i _ { n } \colon Y _ { n - 1 } \to Y _ { n }$and$X = Y _ { - 1 } \longrightarrow Y$are cofibrations.□

Lemma 5.4.10. Let$f \colon X \to Y$be any map. The inclusion

$$
X \times \{0 \} \sqcup Y \mapsto M f
$$

is a cofibration. Hence so are the inclusions$i _ { 0 } \colon X \to M f , Y \to M f$and $i \colon Y \to C f$

Proof. View$I \times I$as a subspace of$\mathbb { R } ^ { 2 }$. There is a (deformation) retraction

$$
I \times I \rightarrow I \times \{0 \} \cup \{0, 1 \} \times I
$$

given by linear projection away from$( 1 / 2 , 2 )$. The product with the identity of $X$is a retraction

$$
(X \times I) \times I \rightarrow (X \times I) \times \{0 \} \cup (X \times \{0, 1 \}) \times I.
$$

Taking the pushout with the identity map of$Y \times I$along$X \times \{ 1 \} \times I$, we get a retraction

$$
r \colon M f \times I \to M f \times \{0 \} \cup (X \times \{0 \} \sqcup Y) \times I
$$

which shows that$X \times \{ 0 \} \sqcup Y \to M f$is a cofibration.

Remark 5.4.11. The following three results generalize the easy lemmas listed for CW pairs and CW complexes to cofibrations and (compactly generated) spaces. [[Reference?]]

Lemma 5.4.12. The product$( i n \ : \mathcal { U } )$

$$
i \times i d _ {Z} \colon X \times Z \longmapsto Y \times Z
$$

of a cofibration with an identity map is a cofibration.

Proof. The map$i \times i d _ { Z }$has the homotopy extension property with respect to T if and only if i has the homotopy extension property with respect to $\mathrm { M a p } ( Z , T )$□

The following “union theorem” is less formal, and was proved by Joachim Lillig in his Diplomarbeit, supervised by Tammo tom Dieck and Rainer Vogt.

Proposition 5.4.13. If the inclusions$X \subseteq Z , Y \subseteq Z$and$X \cap Y \subseteq Z$are cofibrations$( i n \ : \mathcal { U } )$, then$X \cup Y \subseteq Z$is a cofibration.

Proof. [[See Lillig [38, Cor. 2].]]

Lemma 5.4.14.$I f i \colon X \longmapsto Y$and$j \colon Z \mapsto W$are cofibrations, then

$$
i \times i d \cup i d \times j: X \times W \cup_ {X \times Z} Y \times Z \longrightarrow Y \times W
$$

(in U ) is a cofibration.

Proof. [[There is a more direct proof, but we deduce this from the union theorem.]] We may assume that i and j are inclusions of closed subspaces. The inclusions$X \times W \subseteq Y \times W$and$Y \times Z \subseteq Y \times W$are cofibrations by Lemma 5.4.12, and likewise for$X \times Z \subseteq X \times W$. Hence the composite$i \times j \colon X \times Z \subseteq Y \times W$is a cofibration by Lemma 5.4.7. By Proposition 5.4.13, the inclusion into$Y \times W$, of the union of$X \times W$and$Y \times Z$along their intersection$X \times Z$, is a cofibration.

Definition 5.4.15. Fix a space X, and let$X / \mathcal { U }$be the category of spaces under X, i.e., of maps$i \colon X \to Y$. A morphism in$X / \mathcal { U }$from$i \colon X \to Y$to $j \colon X \to Z$is a map under X, i.e., a map$f \colon Y \to Z$such that the triangle

![](images/page_120_image_20.jpg)

commutes. We view$\mathrm { M a p } ( I , Z )$as a space under X, by mapping$x \in X$to the constant map$I  Z \tan j ( x )$. The evaluation maps$e _ { t } \colon \mathrm { M a p } ( I , Z ) \to Z$are then maps under X. A homotopy under X, from f to g, is a map$K \colon Y \to \operatorname { M a p } ( I , Z )$ under X such that$e _ { 0 } K = f$and$e _ { 1 } K = g$. In other words, it is a continuous family$k _ { t } = e _ { t } K \colon Y \to Z$of maps under X, for$t \in I .$, with$k _ { 0 } = f$and$k _ { 1 } = g$

As usual, we say that two maps$f , g \colon Y  Z$under X are homotopic under X, denoted$f \simeq ^ { X } g$or$f \simeq g$rel X, if there exists a homotopy under X from f to g, and$f \colon Y \to Z$under X is a homotopy equivalence under X, denoted $Y \simeq ^ { X } Z .$if there exists a map$g \colon Z \to Y$under X, a homotopy inverse under X, such that$g f \colon Y \to Y$is homotopic to$i d _ { Y }$under X, and$f g \colon Z  Z$is homotopic to$i d _ { Z }$under X.

Example 5.4.16. The case$X = \emptyset$, with$\emptyset / \mathcal { U } \cong \mathcal { U }$, recovers the usual notions of spaces, maps, homotopies and homotopy equivalences.

The case$X = *$, with$* / \mathcal { U } \cong \mathcal { T }$, recovers the category of based spaces and maps, based homotopies and based homotopy equivalences. [[Or do we ask that spaces in$\mathcal { T }$are cofibrantly based?]]

When the structure maps from X are cofibrations, the restriction to maps under X does not afect the notion of homotopy equivalence.

Proposition 5.4.17. Let$i \colon X \to Y$and$j \colon X \to Z$be cofibrations, and let $f \colon Y \to Z$be a map of spaces under X. Then f is a homotopy equivalence if and only if it is a homotopy equivalence under X.

In this situation we may call f a cofiber homotopy equivalence. This notion is dual to the more classical notion of fiber homotopy equivalence. [[Reference via G. Whitehead?]]

Proof. We elaborate on the concise proof given in May [43, p. 44].

It sufices to find a map$g \colon Z \to Y$under X and a homotopy$g \circ f \simeq ^ { X } i d _ { Y }$ under X to the identity.

![](images/page_121_image_9.jpg)

Then g will be a homotopy equivalence, and by the same argument there is a map$f ^ { \prime } \colon Y \to Z$under X and a homotopy$f ^ { \prime } \circ g \simeq ^ { X } i d _ { Z }$. It follows that $f ^ { \prime } \simeq ^ { \bar { X } } \ f \circ g \circ f ^ { \prime } \simeq ^ { X } \ f .$, so g is a homotopy inverse under X to$f .$[[Could put this in the diagram, too.]]

By hypothesis, there is a map$g ^ { \prime \prime } \colon Z \to Y$that is homotopy inverse to$f .$ Since$g ^ { \prime \prime } \circ f \simeq i d _ { Y }$, there is a homotopy$H \colon g ^ { \prime \prime } \circ j = g ^ { \prime \prime } \circ f \circ i \simeq i d _ { Y } \circ i = i$, so by the homotopy extension property for$j \colon X \to Z$, there is an extended homotopy

F :$g ^ { \prime \prime } \simeq g ^ { \prime }$of maps$Z \to Y$, where$g ^ { \prime } \circ j = i .$

![](images/page_122_image_1.jpg)

It sufices to prove that the map$g ^ { \prime } \circ f \colon Y \to Y$under X has a left homotopy inverse$e \colon Y  Y$under$X ,$, since$g = e \circ g ^ { \prime } \colon Z \to Y$will then satisfy$g \circ f =$ e ◦$g ^ { \prime } \circ f \simeq ^ { X } i d _ { Y }$. Note that$g ^ { \prime } \circ f \simeq g ^ { \prime \prime } \circ f \simeq i d _ { Y }$

![](images/page_122_image_3.jpg)

To simplify the notation, we replace the original map$f$by$g ^ { \prime } \circ f .$. The problem is then, given a map$f \colon Y \to Y$under X with$f \simeq i d _ { Y }$, to find a left homotopy inverse e:$Y  Y$under X, so that e ◦$f \simeq ^ { X } i d _ { Y }$

![](images/page_122_image_5.jpg)

Start by choosing a homotopy$H \colon f \simeq i d _ { Y }$, so that$H ( y , 0 ) = f ( y )$and $H ( y , 1 ) = y$for all$y \in Y$

![](images/page_122_image_7.jpg)

The restricted homotopy

$$
H | = H \circ (i \times i d) \colon X \times I \to Y
$$

from$f \circ i = i$to$i d _ { Y } \circ i = i$might not be homotopic (relative to the endpoints) to the constant homotopy at i. We therefore seek a homotopy$K \colon i d _ { Y } \simeq e ,$ such that the restricted homotopy$K | = K \circ ( i \times i d )$is equal to$H |$. Then $K f = K \circ ( f \times i d ) \colon f \simeq e \circ f$will also restrict to H|, so the composite homotopy H<sup>¯</sup> ∗$K f \colon i d _ { Y } \simeq f \simeq e \circ f$extends$\bar { H } | * H |$, which is homotopic (relative to the endpoints) to the constant homotopy. We will then use the homotopy extension property for$i \times i d \colon X \times I \to Y \times I$to deform the restricted homotopy to the constant one.

Hence we consider the homotopy extension problem

![](images/page_123_image_2.jpg)

where we keep$H | _ { \cdot }$, but replace$f$by$i d _ { Y }$. We define$e \colon Y \to Y$to be the end of a choice of extended homotopy K, so$K \colon i d _ { Y } \simeq e$and$K f = K \circ ( f \times i d ) \colon f \simeq e \circ f .$ Since$K \circ ( i \times i d ) = H \circ ( i \times i d )$, we see that$e \circ i = i ,$as desired. It remains to prove that$e \circ f \simeq ^ { X } i d _ { Y }$

We start by forming the “loop sum” homotopy$J = \bar { H } * K f \colon Y \times I \to Y$2 given by

$$
(\bar {H} * K f) (y, s) = \left\{ \begin{array}{l l} H (y, 1 - 2 s) & \text {for} 0 \leq s \leq 1 / 2, \\ K (f (y), 2 s - 1) & \text {for} 1 / 2 \leq s \leq 1. \end{array} \right.
$$

This is an s-parametrized homotopy from$i d _ { Y }$, via$f$for$s = 1 / 2$, to$e \circ f .$

Restricting J along$i \times i d \colon X \times I \to Y \times I ,$, we get the map

$$
J | = J \circ (i \times i d) \colon X \times I \to Y
$$

given by

$$
J | (x, s) = \left\{ \begin{array}{l l} H (i (x), 1 - 2 s) & \text { for } 0 \leq s \leq 1 / 2, \\ H (i (x), 2 s - 1) & \text { for } 1 / 2 \leq s \leq 1, \end{array} \right.
$$

since$K ( f ( i ( x ) , 2 s - 1 ) = K ( i ( x ) , 2 s - 1 ) = H ( i ( x ) , 2 s - 1 )$. Notice that this the loop sum$J | = \bar { H } | * H |$, given by following H<sup>¯</sup> from i to i, and then backtracking along H to i again.

There is a standard t-parametrized homotopy L from the path$J | = \bar { H } | * H |$ to the constant path$C ( x , s ) = i ( x )$at i, which at time$t \in I$follows the first part of H<sup>¯</sup> at t times the usual speed, and then backtracks along the last part of H at t times the usual speed.

$$
L (x, s, t) = \left\{ \begin{array}{l l} H (i (x), 1 - 2 s t) & \text { for } 0 \leq s \leq 1 / 2, \\ H (i (x), 1 - 2 (1 - s) t) & \text { for } 1 / 2 \leq s \leq 1. \end{array} \right.
$$

Note that$L \colon X \times I \times I \to Y$satisfies$L ( x , s , 0 ) = L ( x , 0 , t ) = L ( x , 1 , t ) = i ( x )$

and$L ( x , s , 1 ) = J | ( x , s )$for all$x \in X , s , t \in I$

![](images/page_124_image_1.jpg)

We now use that$i \times i d \colon X \times I \to Y \times I$is a cofibration, see Lemma 5.4.12, to extend the t-parametrized homotopy L of$J |$to a t-parametrized homotopy $M \colon Y \times I \times I \to Y$of J.

![](images/page_124_image_3.jpg)

Going around the three other edges of$I \times I$than the image of$i _ { 0 } , \mathrm { i . e . }$, along $\sqcup = \{ 0 \} \times I \cup I \times \{ 1 \} \cup \{ 1 \} \times I$within$\sqcup = \partial ( I \times I )$, the map M restricts to a homotopy

$$
y = M (y, 0, 0) \simeq M (y, 0, 1) \simeq M (y, 1, 1) \simeq M (y, 0, 1) = (e \circ f) (y)
$$

of maps$Y  Y$, from$i d _ { Y }$to$e \circ f .$Furthermore, this is a homotopy under$X ,$ since$M ( i ( x ) , s , t ) = L ( x , s , t ) = i ( x )$for$( s , t ) \in \sqcup$. Hence$i d _ { Y } \simeq ^ { X } \ e \circ f .$, as required.□

## 5.5 The gluing lemma

[[Might alternatively have followed Hatcher [26, App. 4.G].]]

Definition 5.5.1. Given maps i:$X  Y$and$j \colon X \to Z$, let the double mapping cylinder

$$
Y \cup_ {X} ^ {h} Z = M i \cup_ {X} M j
$$

be the union of$M i = Y \cup _ { X } X \times I$and$M j = Z \cup _ { X } X \times I$along the two cofibrations$i _ { 0 } \colon X \to M i$and$i _ { 0 } \colon X \to M j$. There is a natural map

$$
\Pi \colon Y \cup_ {X} ^ {h} Z \to Y \cup_ {X} Z
$$

to the pushout of i:$X  Y$and$j \colon X \to Z$, induced by the cylinder projections $\pi \colon M i \to Y , i d _ { X }$and$\pi \colon M j  Z$. We also call$Y \cup _ { X } ^ { h } Z$the homotopy pushout of i and$j$.

Remark 5.5.2. This is an instance of a more general construction, called the homotopy colimit. [[Forward reference.]]

![](images/page_125_image_0.jpg)

Lemma 5.5.3. Let$i \colon X \to Y$be a cofibration and let$j \colon X \to Z$be any map. Then the natural map

$$
\Pi \colon Y \cup_ {X} ^ {h} Z \to Y \cup_ {X} Z
$$

is a homotopy equivalence.

Proof. Reparametrizing$X \times I \cup _ { X } X \times I$as$X \times I .$we may rewrite$Y \cup _ { X } ^ { h } Z$as $M i \cup _ { X } Z$, and view Π as the map$\pi \cup i d _ { Z } \colon M i \cup _ { X } Z \to Y \cup _ { X } Z$induced by the cylinder projection$\pi \colon M i \to Y$and id<sub>Z</sub> along$i d _ { X }$

The inclusion$i _ { 0 } \colon X \to M i$is a cofibration by Lemma 5.4.10, and by assumption$i \colon X \to Y$is a cofibration. With these structure maps, the projection π :$M i  Y$is a map under X. It is also a homotopy equivalence, with homotopy inverse the inclusion$Y  M i$

![](images/page_125_image_6.jpg)

By Proposition$5 . 4 . 1 7 , \pi$is a homotopy equivalence under$X$, so there exists a map$g \colon Y  M i$under X, and homotopies πg$\simeq ^ { X } \ i d _ { Y }$and$g \pi \simeq ^ { X } ~ i d _ { M i }$under $X$

Forming pushouts with id<sub>Z</sub> along id<sub>X</sub>, we get a map$G = g \cup i d _ { Z } \colon Y \cup _ { X } Z$ $M i \cup _ { X } Z$and homotopies$\Pi G = \pi g \cup i d _ { Z } \simeq i d _ { Y \cup _ { X } Z }$and$G \Pi = g \pi \cup i d _ { Z } \simeq$ $i d _ { M i \cup _ { X } Z } .$. Hence Π is a homotopy equivalence.□

Lemma 5.5.4. Suppose given a commutative diagram

![](images/page_125_image_10.jpg)

where η and ζ are homotopy equivalences. Then the homotopy pushout map

$$
\eta \cup^ {h} \zeta \colon Y \cup_ {X} ^ {h} Z \xrightarrow {\simeq} Y ^ {\prime} \cup_ {X} ^ {h} Z ^ {\prime}
$$

is a homotopy equivalence.

Proof. We are considering the vertical map of horizontal pushouts induced by the commutative diagram

$$
\begin{array}{c} M i \xleftarrow {i _ {0}} X \xrightarrow {i _ {0}} M j \\ \eta^ {\prime} \Big \downarrow \simeq \qquad \qquad \Big \downarrow = \qquad \zeta^ {\prime} \Big \downarrow \simeq \\ M (\eta i) \xleftarrow {i _ {0}} X \xrightarrow {i _ {0}} M (\zeta j) \end{array}
$$

where$\eta ^ { \prime } = \eta \cup i d _ { X \times I }$and$\zeta ^ { \prime } = \zeta \cup i d _ { X \times I }$are maps under X. In view of the commutative squares

the maps$\eta ^ { \prime }$and$\zeta ^ { \prime }$are homotopy equivalences. By Proposition$5 . 4 . 1 7 , \eta ^ { \prime }$and $\zeta ^ { \prime }$are homotopy equivalences under$X ,$, so there are maps$g \colon M ( \eta i ) \ \to \ M i$ and$h \colon M ( \zeta j ) \to M j$under$X ,$, and homotopies$g \eta ^ { \prime } \simeq ^ { X } i d _ { M i } , \eta ^ { \prime } g \simeq ^ { X } i d _ { M ( \eta i ) }$ $h \zeta ^ { \prime } \simeq ^ { X } i d _ { M j }$and$\zeta ^ { \prime } \boldsymbol { h } \simeq ^ { X } \ i d _ { M ( \zeta j ) }$, all under$X$. Forming pushouts along$X$, we get a map g∪h:$Y ^ { \prime } \cup _ { X } Z ^ { \prime }  Y \cup _ { X } Z$and homotopies$( g \cup h ) ( \eta ^ { \prime } \cup \zeta ^ { \prime } ) = g \eta ^ { \prime } \cup h \zeta ^ { \prime } \simeq$ $i d _ { Y \cup _ { X } ^ { h } Z }$and$( \eta ^ { \prime } \cup \zeta ^ { \prime } ) ( g \cup h ) = \eta ^ { \prime } g \cup \zeta ^ { \prime } h \simeq i d _ { Y ^ { \prime } \cup _ { X } ^ { h } } z ^ { \prime }$. Hence$\eta ^ { \prime } \cup \zeta ^ { \prime } = \eta \cup ^ { h } \zeta$is a homotopy equivalence.□

## Lemma 5.5.5. Suppose given a commutative diagram

![](images/page_126_image_2.jpg)

where$\xi$is a homotopy equivalence. Then the homotopy pushout map

$$
i d \cup_ {\xi} ^ {h} i d \colon Y \cup_ {X} ^ {h} Z \xrightarrow {\simeq} Y \cup_ {X ^ {\prime}} ^ {h} Z
$$

is a homotopy equivalence.

Proof. More explicitly,

$$
i d \cup_ {\xi} ^ {h} i d = i d _ {Y} \cup (\xi \times i d) \cup i d _ {Z} \colon M (i \xi) \cup_ {X} M (j \xi) \to M i \cup_ {X ^ {\prime}} M j
$$

is induced by the identity on$Y$and$Z ,$and by$\xi \times i d _ { I }$on each of the two copies of$X \times I ,$one attached by$i \xi$to$Y$and one attached by$j \xi$to$Z .$.

Choose a homotopy inverse$g \colon X ^ { \prime } \to X$to$\xi ,$together with homotopies $H \colon X \times I \to X$from$g \xi$to$i d _ { X }$, and$K \colon X ^ { \prime } \times I  X ^ { \prime }$from$\xi g \ t o \ i d _ { X ^ { \prime } }$. We then have a homotopy commutative diagram

![](images/page_126_image_10.jpg)

with homotopies$i K \colon i \xi g \simeq i$and$j K \colon j \xi g \simeq j$as indicated. Let the map

$$
i ^ {\prime} = i d _ {Y} \cup (g * i K) \colon M i \to M (i \xi)
$$

be given by the identity on$Y$and the map

$$
(x ^ {\prime}, s) \mapsto \left\{ \begin{array}{l l} (g (x ^ {\prime}), 2 s) & \text { for } 0 \leq s \leq 1 / 2 \\ i K (x ^ {\prime}, 2 s - 1) & \text { for } 1 / 2 \leq s \leq 1 \end{array} \right.
$$

from$X ^ { \prime } \times I$. Likewise, let the map

$$
j ^ {\prime} = i d _ {Z} \cup (g * j K) \colon M j \to M (j \xi)
$$

by given by the identity on$Z$and the map

$$
(x ^ {\prime}, s) \mapsto \left\{ \begin{array}{l l} (g (x ^ {\prime}), 2 s) & \text { for } 0 \leq s \leq 1 / 2 \\ j K (x ^ {\prime}, 2 s - 1) & \text { for } 1 / 2 \leq s \leq 1 \end{array} \right.
$$

from$X ^ { \prime } \times I$. These both agree with$g$on$X ^ { \prime }$, and combine to a map

$$
i ^ {\prime} \cup_ {g} j ^ {\prime} \colon M i \cup_ {X ^ {\prime}} M j \to M (i \xi) \cup_ {X} M (j \xi)
$$

that we wish to show is homotopy inverse to id$\cup _ { \xi } ^ { h }$id.

The composite self-map

$$
(i ^ {\prime} \cup_ {g} j ^ {\prime}) (i d \cup_ {\xi} ^ {h} i d) \colon M (i \xi) \cup_ {X} M (j \xi) \longrightarrow M (i \xi) \cup_ {X} M (j \xi)
$$

is the identity on$Y , Z$and equals$g \xi$on the middle copy of$X ,$. Using the homotopy$H \colon g \xi \simeq i d _ { X }$, we can homotope the displayed self-map to the union $\eta \cup \zeta$along$X$of a self-map η of$M ( i \xi )$that is the identity on$Y$and$X$, and a self-map ζ of M(jξ) that is the identity on$Z$and$X ,$. In view of the commutative squares

![](images/page_127_image_6.jpg)

the self-maps$\eta$and$\zeta$are homotopy equivalences. Since they are also maps under$X ,$, and the inclusions$X \to M ( i \xi )$and$X \to M ( j \xi )$are cofibrations, they are also homotopy equivalences under X by Proposition 5.4.17. Gluing a pair of chosen homotopy inverses along$X$, we see that the union map$\eta \cup \zeta$is also a homotopy equivalence. This proves that$( i ^ { \prime } \cup _ { g } j ^ { \prime } ) ( i d \cup _ { \xi } ^ { h } i d )$is a homotopy equivalence.

Conversely, the composite self-map

$$
(i d \cup_ {\xi} ^ {h} i d) (i ^ {\prime} \cup_ {g} j ^ {\prime}) \colon M i \cup_ {X ^ {\prime}} M j \longrightarrow M i \cup_ {X ^ {\prime}} M j
$$

is the identity on$Y , Z$and equals$\xi g$on the middle copy of$X ^ { \prime }$. Using the homotopy$K \colon \xi g \ \simeq \ i d _ { X ^ { \prime } }$, it is homotopic to a union map$\eta ^ { \prime } \cup \zeta ^ { \prime }$along$X ^ { \prime }$ where$\eta ^ { \prime } \colon M i \to M i$is a map under$X ^ { \prime }$and a homotopy equivalence, hence a homotopy equivalence under$X ^ { \prime }$, and likewise for$\zeta ^ { \prime } \colon M j  M j$. Gluing along $X ^ { \prime }$, we see that$\eta ^ { \prime } \cup \zeta ^ { \prime }$and$( i d \cup _ { \xi } ^ { h } i d ) ( i ^ { \prime } \cup _ { g } j ^ { \prime } )$are homotopy equivalences.

We can now prove the following gluing lemma. It will be the basis for a realization lemma for simplicial spaces, which in turn leads to Quillen’s theorem$\mathrm { A }$ and the additivity theorem for algebraic K-theory.

Proposition 5.5.6 (Gluing lemma). Suppose given a commutative diagram

![](images/page_127_image_13.jpg)

where i and$i ^ { \prime }$are cofibrations and$\xi , \eta$and$\zeta$are homotopy equivalences. Then the induced map

$$
\eta \cup_ {\xi} \zeta \colon Y \cup_ {X} Z \xrightarrow {\simeq} Y ^ {\prime} \cup_ {X ^ {\prime}} Z ^ {\prime}
$$

of pushouts is a homotopy equivalence.

Proof. Since i and$i ^ { \prime }$are cofibrations, the natural maps Π and$\Pi ^ { \prime }$in the following commutative diagram are homotopy equivalences by Lemma 5.5.3.

$$
\begin{array}{c} Y \cup_ {X} ^ {h} Z \xrightarrow [ \simeq ]{\Pi} Y \cup_ {X} Z \\ \eta \cup_ {\xi} ^ {h} \zeta \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \eta \cup_ {\xi} \zeta \\ Y ^ {\prime} \cup_ {X ^ {\prime}} ^ {h} Z ^ {\prime} \xrightarrow [ \simeq ]{\Pi^ {\prime}} Y ^ {\prime} \cup_ {X ^ {\prime}} Z ^ {\prime} \end{array}
$$

Hence, to prove that the pushout$\eta \cup _ { \xi } \zeta$is a homotopy equivalence it sufices to prove that the homotopy pushout$\eta \dot { \cup _ { \xi } ^ { h } } \zeta$is one. By factoring this map as

$$
(i d \cup_ {\xi} ^ {h} i d) \circ (\eta \cup^ {h} \zeta),
$$

we may assume either that$\xi = i d _ { X }$, or that$\eta = i d _ { Y }$and$\zeta = i d _ { Z }$

![](images/page_128_image_5.jpg)

In the first case, it follows by Lemma 5.5.4 that η$\mathsf { J } ^ { h } \zeta$is a homotopy equivalence. In the second case, it follows by Lemma 5.5.5 that id$\cup _ { \xi } ^ { h }$id is a homotopy equivalence. Hence the composite map$\eta \cup _ { \xi } ^ { h } \zeta$is also a homotopy equivalence.

We also need a similar result for sequential colimits.

Lemma 5.5.7. Suppose given a commutative diagram

$$
\begin{array}{c} \dots \longrightarrow X _ {n - 1} \stackrel {{i _ {n}}} {{\longrightarrow}} X _ {n} \longrightarrow \dots \\ f _ {n - 1} \Biggl \downarrow \simeq \qquad \qquad f _ {n} \Biggl \downarrow \simeq \\ \dots \longmapsto Y _ {n - 1} \stackrel {{j _ {n}}} {{\longrightarrow}} Y _ {n} \longrightarrow \dots \end{array}
$$

where$n \geq 0$, each$i _ { n }$and$j _ { n }$is a cofibration, and each$f _ { n }$is a homotopy equivalence. Then the induced map

$$
\underset {n} {\operatorname{colim}} f _ {n} \colon \underset {n} {\operatorname{colim}} X _ {n} \xrightarrow {\simeq} \underset {n} {\operatorname{colim}} Y _ {n}
$$

is a homotopy equivalence.

[[Choose homotopy inverses$g _ { n } ^ { \prime } \colon Y _ { n } \ \to \ X _ { n }$, use the homotopy extension property to find maps$g _ { n } \colon Y _ { n } \to X _ { n }$commuting with the$i _ { n }$and$j _ { n } ,$and let $g = { \mathrm { c o l i m } } _ { n } g _ { n } .$Check that$g$is homotopy inverse to$f .$Alternatively, follow $\left[ 2 6 , \mathrm { A p p . ~ } 4 . \mathrm { G } \right] . ]$

## 5.6 Homotopy groups

[[Refer to [43, Ch. 9], [26, 4.1].]]

The homotopy groups$\pi _ { n } ( X )$will be the main algebraic invariants that we extract from a based space$X$. More precisely,$\pi _ { 0 } ( X )$is a based set,$\pi _ { 1 } ( X )$is a group, and$\pi _ { n } ( X )$is an abelian group for each$n \geq 2$

Definition 5.6.1. Let$( X , x _ { 0 } )$be a based topological space. For each non-negative integer$n \geq 0$we let

$$
\pi_ {n} (X) = [ S ^ {n}, X ]
$$

be the set of based homotopy classes of maps α:$S ^ { n } \to X$. We denote the homotopy class of α by$[ \alpha ] \in \pi _ { n } ( X )$. The constant map to$x _ { 0 }$in X specifies a base point in$\pi _ { n } ( X )$

Each based map$f \colon X \to Y$induces a function$\pi _ { n } ( f ) \colon \pi _ { n } ( X ) \to \pi _ { n } ( Y )$ taking the homotopy class of α to the homotopy class of the composite$f \circ \alpha =$ $f \alpha \colon S ^ { n } \to Y$. This function is well-defined, since a homotopy$H \colon \alpha \simeq \beta$induces a homotopy$f H \colon S ^ { n } \wedge I _ { + } \to Y$from$f \alpha$to$f \beta$. It also respects the base point. Hence$\pi _ { n }$for$n \geq 0$defines a functor

$$
\pi_ {n} \colon \mathbf {T o p} _ {*} \to \mathbf {S e t} _ {*}.
$$

Lemma 5.6.2. Let$p _ { 1 } \colon S ^ { 1 } \to S ^ { 1 } \vee S ^ { 1 }$be the pinch map. Under the identification $S ^ { 1 } = I / \partial I$, it takes$s \in [ 0 , 1 / 2 ]$to$i n _ { 1 } ( 2 s )$, and$s \in [ 1 / 2 , 1 ]$to$i n _ { 2 } ( 2 s - 1 )$. Its stabilization

$$
p _ {n} = p _ {1} \wedge i d _ {S ^ {n - 1}}: S ^ {n} \longrightarrow (S ^ {1} \vee S ^ {1}) \wedge S ^ {n - 1} \cong S ^ {n} \vee S ^ {n}
$$

induces a pairing

$$
\pi_ {n} (X) \times \pi_ {n} (X) \stackrel {*} {\longrightarrow} \pi_ {n} (X)
$$

for each$n \geq 1$, that takes$( [ \alpha ] , [ \beta ] )$to the class$[ \alpha ] * [ \beta ]$of the composite

$$
S ^ {n} \xrightarrow {p _ {n}} S ^ {n} \vee S ^ {n} \xrightarrow {\alpha \vee \beta} X \vee X \xrightarrow {\nabla} X.
$$

It induces a natural group structure on$\pi _ { n } ( X )$, which we call the n-th homotopy group of X. Hence$\pi _ { n } ~ f o r ~ n \ge 1 ~ l i f t s$to a functor

$$
\pi_ {n} \colon \mathbf {T o p} _ {*} \to \mathbf {G r p}.
$$

Proof. [[Discuss associativity, unit and inverse.]]

Lemma 5.6.3. For$n \geq 2$the group structure on$\pi _ { n } ( X )$is abelian. Hence$\pi _ { n }$ for$n \geq 2$lifts to a functor

$$
\pi_ {n} \colon \mathbf {T o p} _ {*} \to \mathbf {A b}.
$$

[[This is the Eckmann–Hilton argument. Picture with little squares?]]

Proof. For$n \geq 2 ,$, the map

$$
q _ {n} = i d \wedge p _ {1} \wedge i d \colon S ^ {n} \to S ^ {1} \wedge (S ^ {1} \vee S ^ {1}) \wedge S ^ {n - 2} \cong S ^ {n} \vee S ^ {n}
$$

induces a second pairing

$$
\pi_ {n} (X) \times \pi_ {n} (X) \stackrel {\star} {\longrightarrow} \pi_ {n} (X)
$$

that takes$( [ \alpha ] , [ \beta ] )$to the class$[ \alpha ] \star [ \beta ]$of the composite

$$
S ^ {n} \xrightarrow {q _ {n}} S ^ {n} \vee S ^ {n} \xrightarrow {\alpha \vee \beta} X \vee X \xrightarrow {\nabla} X.
$$

Let$c \colon S ^ { n } \to X$be the constant map to ∗, so that [c] is the identity element in$\pi _ { n } ( X )$. Then

$$
[ \alpha ] * [ \beta ] = ([ \alpha ] \star [ c ]) * ([ c ] \star [ \beta ]) = ([ \alpha ] * [ c ]) \star ([ c ] * [ \beta ]) = [ \alpha ] \star [ \beta ]
$$

and

$$
[ \alpha ] * [ \beta ] = ([ c ] \star [ \alpha ]) * ([ \beta ] \star [ c ]) = ([ c ] * [ \beta ]) \star ([ \alpha ] * [ c ]) = [ \beta ] \star [ \alpha ]
$$

so the two pairings ∗ and ⋆ are equal, and both are commutative.

[[Based homotopic maps induce same functions on$\pi _ { n }$. Factor$\pi _ { n }$through $\mathrm { H o } ( \mathbf { \ddot { T o p } } _ { * } ) . ] \big ]$

[[Discuss (in-)dependence of$\pi _ { n } ( X , x _ { 0 } )$on the choice of base point.]]

## 5.7 Weak homotopy equivalences

Definition$\mathbf { 5 . 7 . 1 . ~ A }$map$f \colon X \to Y$of spaces is a weak homotopy equivalence if$\pi _ { 0 } ( f ) \colon \pi _ { 0 } ( X ) \to \pi _ { 0 } ( Y )$is a bijection, and if for each point$x _ { 0 } \in X$and each $n \geq 1$the homomorphism$\pi _ { n } ( f ) \colon \pi _ { n } ( X , x _ { 0 } ) \to \pi _ { n } ( Y , f ( x _ { 0 } ) )$is an isomorphism. We often write$f \colon X \xrightarrow { \simeq } Y$to indicate that f is a weak homotopy equivalence.

Remark 5.7.2. It is not quite correct to restate this definition as saying that $\pi _ { n } ( f ) \colon \pi _ { n } ( X , x _ { 0 } ) \ \to \ \pi _ { n } ( Y , f ( x _ { 0 } ) )$is a bijection for all$x _ { 0 } ~ \in ~ X$and$n \geq 0 .$ since this would make any map$\emptyset  Y$a weak equivalence. However, if$X$is nonempty, then this is an acceptable rewording. In this case it sufices to verify that$\pi _ { n } ( f )$is a bijection for one point$x _ { 0 }$in each path component of$X ,$and for all$n \geq 0 .$

Lemma 5.7.3. Each homotopy equivalence$f \colon X \to Y$is a weak homotopy equivalence.

[[Relative Hurewicz theorem?]]

[[Topological realization of singular complex$\Gamma X = | \operatorname { s i n g } ( X ) |$defines a cellular approximation to X by the adjunction counit$\epsilon \colon | \operatorname { s i n g } ( X ) | \to X$, which is a weak homotopy equivalence.]]

[[Weak homotopy equivalence is an equivalence relation. Dold–Thom [12, $\mathrm { p . 2 4 4 . } \ ] . \mathrm { ] }$

Theorem 5.7.4 (J.H.C. Whitehead). Let X and Y each be of the homotopy type of a CW complex. Then a map$f \colon X \to Y$is a weak homotopy equivalence if and only if it is a homotopy equivalence.

[[Reference, proof in Hatcher [26, 4.5].]]

## 5.8 Fibrations

Definition 5.8.1 (Hurewicz fibration). A map$f \colon X \to Y$is said to have the homotopy lifting property (HLP) with respect to a space T if for any commutative diagram of solid arrows

![](images/page_131_image_2.jpg)

there exists a dashed arrow making the whole diagram commute. The map$f$is called a (Hurewicz) fibration if it has the homotopy lifting property with respect to any space T. For each point$y \in Y$, the preimage$f ^ { - 1 } ( y ) = X \times _ { Y } \{ y \}$is called the fiber of f at y.

Definition 5.8.2 (Serre fibration). A map$f \colon X \to Y$is a Serre fibration if it has the homotopy lifting property with respect to$D ^ { n }$for each$n \geq 0$. Any Hurewicz fibration is a Serre fibration.

Lemma 5.8.3. A Serre fibration has the homotopy lifting property with respect to any CW complex T.

[[Proof by induction over cells and skeleta of$T . ] ]$

Lemma 5.8.4. Let$f \colon X \to Y$be a Serre fibration, and choose base points $y \in Y , x \in f ^ { - 1 } ( y ) \subseteq X$. Then there is a long exact sequence of homotopy groups

$$
\begin{array}{c} \dots \to \pi_ {n} (f ^ {- 1} (y), x) \to \pi_ {n} (X, x) \xrightarrow {f _ {*}} \pi_ {n} (Y, y) \xrightarrow {\partial} \pi_ {n - 1} (f ^ {- 1} (y), x) \to \ldots \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \to \pi_ {0} (f ^ {- 1} (y), x) \to \pi_ {0} (X, x) \xrightarrow {f _ {*}} \pi_ {0} (Y, y). \end{array}
$$

[[See [26, Thm. 4.41] for a proof.]]

Let$f \colon X \to Y$be any map. The mapping path space

$$
N f = X \times_ {Y} \operatorname{Map} (I, Y)
$$

consists of pairs$( x , \alpha )$with$f ( x ) = \alpha ( 1 )$. There is an evaluation map$e _ { 0 } \colon N f \to$ Y, taking (x, α) to$\alpha ( 0 )$

Lemma 5.8.5. The map e<sub>0</sub> :$N f \to Y$is a (Hurewicz) fibration.

Let$\iota \colon X \to N f$be the embedding taking$x \in X$to the pair$( x , \alpha ) \in N f$ where α is the constant path at$f ( x )$. It is a homotopy equivalence, with a homotopy inverse given by the projection$N f  X$taking$( x , \alpha )$to x. [[The composite$X \to N f \to X$is the identity, while the composite$N f  X  N f$is homotopic to the identity, via a homotopy deforming the path α to the constant path at its endpoint.]]

Given a base point$y \in Y$, the homotopy fiber of f at$y ,$

$$
F _ {y} f = X \times_ {Y} \operatorname{Map} (I, Y) \times_ {Y} \left\{y \right\},
$$

equals the fiber of$e _ { 0 } \colon N f \to Y$at y. It consists of pairs$( x , \alpha )$, with$x \in X$and α :$I  Y$such that$\alpha ( 0 ) = y$and$\alpha ( 1 ) = f ( x )$. Under the embedding$\iota ,$the fiber$f ^ { - 1 } ( y )$is identified with a subspace of the homotopy fiber$F _ { y } f$, and there is a commutative diagram

![](images/page_132_image_1.jpg)

Lemma$\mathbf { 5 . 8 . 6 }$. Let$f \colon X \to Y$be any map, and choose base points$y \in Y$ $x \in f ^ { - 1 } ( y ) \subseteq X$. Then there is a long exact sequence

$$
\begin{array}{c} \dots \to \pi_ {n} (F _ {y} f, \iota (x)) \to \pi_ {n} (X, x) \xrightarrow {f _ {*}} \pi_ {n} (Y, y) \xrightarrow {\partial} \pi_ {n - 1} (F _ {y} f, x) \to \ldots \\ \dots \to \pi_ {0} (F _ {y} f, \iota (x)) \to \pi_ {0} (X, x) \to \pi_ {0} (Y, y). \end{array}
$$

Proof. This is the long exact sequence associated to the (Hurewicz, hence Serre) fibration$F _ { y } f \to N f \to Y$, with$\pi _ { n } ( X , x )$replacing its isomorphic image under $\iota _ { * } .$, that is$\pi _ { n } ( N f , \iota ( x ) )$□

The following definition is due to Dold, see [12].

Definition 5.8.7 (Quasi-fibration). A map$f \colon X \to Y$is a quasi-fibration if for each point$y \in Y$the inclusion

$$
\iota \colon f ^ {- 1} (y) \xrightarrow {\simeq} F _ {y} f
$$

is a weak homotopy equivalence.

Lemma 5.8.8. Let$f \colon X \ \to \ Y$be a quasi-fibration, and choose base points $y \in Y , x \in f ^ { - 1 } ( y ) \subseteq X$. Then there is a long exact sequence

$$
\begin{array}{c} \dots \to \pi_ {n} (f ^ {- 1} (y), x) \to \pi_ {n} (X, x) \xrightarrow {f _ {*}} \pi_ {n} (Y, y) \xrightarrow {\partial} \pi_ {n - 1} (f ^ {- 1} (y), x) \to \ldots \\ \qquad \qquad \qquad \dots \to \pi_ {0} (f ^ {- 1} (y), x) \to \pi_ {0} (X, x) \to \pi_ {0} (Y, y). \end{array}
$$

Proof. This is the long exact sequence above, with$\pi _ { n } ( f ^ { - 1 } ( y ) , x )$replacing its isomorphic image$\pi _ { n } ( F _ { y } f , \iota ( x ) )$□

Lemma 5.8.9. Any Serre fibration$f \colon X \to Y$is a quasi-fibration.

Proof. Let$y \in Y$. If$f ^ { - 1 } ( y )$is empty, then so is$F _ { y } f ;$, by the homotopy lifting property. Otherwise, for each choice of base point$x \in f ^ { - 1 } ( y )$, the five-lemma applied to the diagram

$$
\begin{array}{c} \pi_ {n + 1} (X, x) \xrightarrow {f _ {*}} \pi_ {n + 1} (Y, y) \xrightarrow {\partial} \pi_ {n} (f ^ {- 1} (y), x) \xrightarrow {} \pi_ {n} (X, x) \xrightarrow {f _ {*}} \pi_ {n} (Y, y) \\ = \Biggl \downarrow \qquad \qquad = \Biggl \downarrow \qquad \qquad \Biggl \downarrow \qquad \qquad = \Biggl \downarrow \qquad \qquad = \Biggl \downarrow \\ \pi_ {n + 1} (X, x) \xrightarrow {f _ {*}} \pi_ {n + 1} (Y, y) \xrightarrow {\partial} \pi_ {n} (F _ {y} f, \iota (x)) \xrightarrow {} \pi_ {n} (X, x) \xrightarrow {f _ {*}} \pi_ {n} (Y, y) \end{array}
$$

implies that the middle vertical map is an isomorphism. (Some special care is needed for$n = 0 , \mathrm { s e e } [ 1 2 ] . )$□

Proposition 5.8.10. Let$f \colon X \to Y$be a map, let$U , V \subset Y$be open subsets covering${ \cal Y } ,$, and assume that all three$o f$the restricted maps$f ^ { - 1 } ( U ) \to U$ $f ^ { - 1 } ( V ) { \overset { } { \to } } V$and$f ^ { - 1 } ( U \cap V ) \to U \cap V$are quasi-fibrations.

![](images/page_133_image_1.jpg)

Then$f \colon X \to Y$is a quasi-fibration.

[[Cite [12], [26] for proof.]]

[[Dold–Lashof/Dold–Thom criteria for quasi-fibrations.]]

[[Homotopy cartesian squares.]]

# Chapter 6

# Simplicial methods

## 6.1 Combinatorial complexes

General references for combinatorial complexes are Eilenberg–Steenrod [17, Ch. 2] and Fritsch–Piccinini [20, Ch. 3].

Definition 6.1.1. For each$n \geq 0$, the standard n-simplex$\Delta ^ { n }$is the convex span

$$
\Delta^ {n} = \{(t _ {0}, \dots , t _ {n}) \in \mathbb {R} ^ {n + 1} \mid \sum_ {i = 0} ^ {n} t _ {i} = 1, t _ {i} \geq 0 \}
$$

of the (n + 1) points

$$
\begin{array}{c} e _ {0} = (1, 0, \ldots , 0) \\ e _ {1} = (0, 1, \ldots , 0) \\ \vdots \\ e _ {n} = (0, 0, \ldots , 1) \end{array}
$$

in$\mathbb { R } ^ { n + 1 }$. Note that

$$
(t _ {0}, t _ {1}, \ldots , t _ {n}) = \sum_ {i = 0} ^ {n} t _ {i} e _ {i}.
$$

A Euclidean n-simplex σ in$\mathbb { R } ^ { N }$is the convex span

$$
\sigma = \left\{\sum_ {i = 0} ^ {n} t _ {i} v _ {i} \mid (t _ {0}, \dots , t _ {n}) \in \Delta^ {n} \right\}
$$

of$( n + 1 )$points$v _ { 0 } , v _ { 1 } , \ldots , v _ { n } \in \mathbb { R } ^ { N }$in general position, meaning that the n vectors

$$
v _ {1} - v _ {0}, \dots , v _ {n} - v _ {0}
$$

are linearly independent. The points$v _ { 0 } , v _ { 1 } , \ldots , v _ { n }$are called the vertices of$\sigma .$ We say that an n-simplex σ has dimension n.

When the total ordering of the vertices is fixed, the presentation of each point in σ as a sum$\textstyle \sum _ { i = 0 } ^ { n } t _ { i } v _ { i }$is unique, and the numbers$\left( t _ { 0 } , t _ { 1 } , \ldots , t _ { n } \right)$are called the barycentric coordinates of the point. A Euclidean simplex τ is a face of a Euclidean simplex σ if τ is the convex span of a non-empty subset of the vertices of σ. It is a proper face${ \mathrm { i f ~ } } \tau \neq \sigma$

For simplicity, we only deal with finite complexes in the following. To handle infinite complexes, some additional point-set topological care is required.

Definition 6.1.2. A Euclidean precomplex is a finite set$K = \{ \sigma \in K \}$of Euclidean simplices in some$\mathbb { R } ^ { N }$, with the property that the intersection σ ∩ τ of any two simplices$\sigma , \tau$in K is either empty or a face of both σ and τ. If furthermore any face$\tau \subset \sigma$of a simplex$\sigma \in K$is a simplex in$K ,$, then we call K a Euclidean complex. Given a Euclidean precomplex$K$, let$K ^ { a } = \{ \tau \ |$ $\tau$is a face of a$\sigma \in K \}$denote the associated Euclidean complex.

The subspace$\begin{array} { r } { | K | = \bigcup _ { \sigma \in K } \sigma \subseteq \mathbb { R } ^ { N } } \end{array}$is called a polyhedron. A triangulation of a space$X$is a pair$( K , h )$where$K$is a Euclidean complex and h is a homeomorphism$h \colon | K | \cong X$. A subcomplex of a Euclidean complex K is a subset$L \subseteq K$that is itself a Euclidean complex. The dimension of an Euclidean complex is the maximal dimension of its simplices.

Example 6.1.3. For each$n \geq 0$, let

$$
\sigma^ {n} = \left\{\left(u _ {1}, u _ {2}, \dots , u _ {n}\right) \mid 1 \geq u _ {1} \geq u _ {2} \geq \dots \geq u _ {n} \geq 0 \right\}.
$$

This is the convex span in$\mathbb { R } ^ { n }$of the vertices

$$
f _ {0} = (0, 0, \dots , 0), f _ {1} = (1, 0, \dots , 0), \dots , f _ {n} = (1, 1, \dots , 1)
$$

hence is a Euclidean n-simplex in$\mathbb { R } ^ { n }$. The faces of$\sigma ^ { n }$can be described by adding relations of the form$1 = u _ { 1 } , u _ { i } = u _ { i + 1 }$for$1 \leq i < n$or$u _ { n } = 0$. We abuse notation, and also write$\sigma ^ { n }$for the Euclidean complex$\{ \sigma ^ { n } \} ^ { a }$consisting of$\sigma ^ { n }$and all of its faces, with underlying polyhedron$\sigma ^ { n }$homeomorphic to$D ^ { n }$

![](images/page_135_image_8.jpg)

The$u _ { i }$are related to the barycentric coordinates$\left( t _ { 0 } , \ldots , t _ { n } \right)$by$( u _ { 1 } , \ldots , u _ { n } ) =$ $\textstyle \sum _ { i = 0 } ^ { n } t _ { i } f _ { i }$, so that

$$
u _ {i} = t _ {i} + \dots + t _ {n}
$$

for$1 \leq i \leq n$

Example 6.1.4. Let$\partial \sigma ^ { n } \subset \sigma ^ { n }$be the subcomplex consisting of all of the proper faces of$\sigma ^ { n }$. Its underlying polyhedron$| \partial \sigma ^ { n } |$is the topological boundary of$\sigma ^ { n } \subseteq \mathbb { R } ^ { n }$, homeomorphic to$S ^ { n - 1 }$

Remark 6.1.5. One dificulty with the category of Euclidean complexes, as well as the categories of (ordered) simplicial complexes to be discussed below, is that colimits can be badly behaved or fail to exist. For example, the quotient $K / L$of a Euclidean complex K by a subcomplex L is usually not defined as a Euclidean complex. The reader might consider the case when$K = \sigma ^ { 2 }$and$L$is either a 1-dimensional face of K or the whole boundary$\scriptstyle \partial \sigma ^ { 2 }$

Example 6.1.6. Let$\Sigma _ { n }$act on$\mathbb { R } ^ { n }$by permuting the coordinates, with$\pi \in \Sigma _ { n }$ taking$( u _ { 1 } , u _ { 2 } , \ldots , u _ { n } )$to

$$
\pi \cdot (u _ {1}, u _ {2}, \dots , u _ {n}) = (u _ {\pi^ {- 1} (1)}, u _ {\pi^ {- 1} (2)}, \dots , u _ {\pi^ {- 1} (n)}).
$$

The set

$$
C ^ {n} = \left\{\pi (\sigma^ {n}) \mid \pi \in \Sigma_ {n} \right\} ^ {a}
$$

is then a Euclidean complex in$\mathbb { R } ^ { n }$. To prove that$\pi _ { 1 } ( \sigma ^ { n } ) \cap \pi _ { 2 } ( \sigma ^ { n } )$is a face of both$\pi _ { 1 } ( \sigma ^ { n } )$and$\pi _ { 2 } ( \sigma ^ { n } )$, for$\pi _ { 1 } , \pi _ { 2 } \in \Sigma _ { n } .$, it sufices to check that$\sigma ^ { n } \cap \pi ( \sigma ^ { n } )$is the face of$\sigma ^ { n }$where$u _ { \pi ( i ) } = u _ { \pi ( j ) }$for all$i < j$with$\pi ( i ) > \pi ( j )$, for any$\pi \in \Sigma _ { n } .$To see this, note that$( { \dot { u } } _ { 1 } , \dots , { \tilde { u } } _ { n } ) \in \sigma ^ { n }$has the form$\pi ( v _ { 1 } , \ldots , v _ { n } ) \in \pi ( \sigma ^ { n } )$only if $( v _ { 1 } , \ldots , v _ { n } ) = \pi ^ { - 1 } ( u _ { 1 } , \ldots , u _ { n } ) = ( u _ { \pi ( 1 ) } , \ldots , u _ { \pi ( n ) } )$, so that$u _ { \pi ( 1 ) } \geq \cdot \cdot \cdot \geq u _ { \pi ( n ) }$ The underlying polyhedron of$C ^ { n }$is the n-cube

$$
| C ^ {n} | = \bigcup_ {\pi \in \Sigma_ {n}} \pi (\sigma^ {n}) = I ^ {n}
$$

since any point$( w _ { 1 } , \ldots , w _ { n } )$in$I ^ { n }$has the form$\pi \cdot ( u _ { 1 } , \ldots , u _ { n } )$for some$\pi \in \Sigma _ { r }$n and$( u _ { 1 } , \ldots , u _ { n } ) \in \sigma ^ { n }$

Definition 6.1.7. A permutation$\pi \in \Sigma _ { m + n }$is called an (m, n)-shufle if

$$
\pi (1) <   \dots <   \pi (m), \pi (m + 1) <   \dots <   \pi (m + n).
$$

An$( m , n )$-shufle$\pi$is uniquely determined by the subset$\{ \pi ( 1 ) , \ldots , \pi ( m ) \}$of $\{ 1 , \ldots , m + n \}$, so altogether there are precisely$( m , n ) = ( m + n ) ! / m ! n !$diferent $( m , n ) { \mathrm { - s h u f f e s } }$. The inverse of an$( m , n )$-shufle is not necessarily an$( m , n ) .$ shufle.

Lemma 6.1.8. The product$\sigma ^ { m } \times \sigma ^ { n } \subseteq I ^ { m } \times I ^ { n } = I ^ { m + n }$is triangulated by the Euclidean complex

$$
P ^ {m, n} = \left\{\pi^ {- 1} \left(\sigma^ {m + n}\right) \mid \pi \text {   is   an   } (m, n) \text {-shuffle} \right\} ^ {a}.
$$

Hence

$$
| P ^ {m, n} | = \bigcup_ {(m, n) \text {-shuffles} \pi} \pi^ {- 1} (\sigma^ {m + n}) = \sigma^ {m} \times \sigma^ {n}.
$$

Proof.$P ^ { m , n }$is a subcomplex of$C ^ { m + n }$, hence is a Euclidean complex. The polyhedron$| P ^ { m , n } |$consists of the points of the form

$$
(w _ {1}, \ldots , w _ {m + n}) = \pi^ {- 1} \cdot (u _ {1}, \ldots , u _ {m + n}) = (u _ {\pi (1)}, \ldots , u _ {\pi (m + n)})
$$

with π an (m, n)-shufle and$1 \geq u _ { 1 } \geq \cdot \cdot \cdot \geq u _ { m + n } \geq 0 .$, which precisely means that$1 \geq w _ { 1 } \geq \cdot \cdot \cdot \geq w _ { m } \geq 0$and$1 \geq w _ { m + 1 } \geq \cdot \cdot \cdot \geq w _ { m + n } \geq 0$. These are exactly the points in the product$\sigma ^ { m } \times \sigma ^ { n }$□

Definition 6.1.9. Let K be a Euclidean complex. Let the n-skeleton

$$
K ^ {(n)} = \{\sigma \in K \mid \dim (\sigma) \leq n \}
$$

be the subcomplex of simplices of dimension$\leq n$. Let

$$
K _ {n} ^ {\sharp} = \{\sigma \in K \mid \dim (\sigma) = n \}
$$

be the set of n-simplices in$K .$

Lemma 6.1.10. The polyhedron$| K |$of a Euclidean complex is a finite CW complex, with n-skeleton

$$
\left| K \right| ^ {(n)} = \left| K ^ {(n)} \right| \subset \left| K \right|
$$

and characteristic maps

$$
\Phi_ {\sigma} \colon D ^ {n} \cong \sigma \to | K |.
$$

for σ ∈ K<sup>♯</sup><sub>n</sub>.

[[Clear?]]

Definition 6.1.11. An afine linear map$\mathbb { R } ^ { N } \to \mathbb { R } ^ { M }$is the composite of a linear map and a translation. Let$\sigma \subset \mathbb { R } ^ { N } , \tau \subset \mathbb { R } ^ { M }$be Euclidean simplices. A map $\sigma  \tau$that is the restriction of an afine linear map, and takes the vertices of$\sigma$ to the vertices of$\tau .$, is called a simplicial map.

Let K, L be Euclidean complexes.$\mathrm { A }$simplicial map$f \colon K \to L$is a map $f \colon | K | \to | L |$such that for each simplex$\sigma \in K$there is a simplex$\tau \in L$such that the restriction f|σ factors as the composite of a simplicial map$\sigma \to \tau$and the inclusion$\tau \subset | L |$

![](images/page_137_image_8.jpg)

Euclidean complexes and simplicial maps form a category EuCx. A simplicial isomorphism of Euclidean complexes is an invertible simplicial map.

Example 6.1.12. The efect of a simplicial map on barycentric coordinates is as follows. Let$f \colon \sigma  \tau$be a simplicial map, where σ is spanned by the vertices$v _ { 0 } , \ldots , v _ { m }$and τ is spanned by the vertices$w _ { 0 } , \ldots , w _ { n }$. Then$f$takes the point$\textstyle \sum _ { i = 0 } ^ { m } u _ { i } v _ { i }$with barycentric coordinates$( u _ { 0 } , \ldots , u _ { m } ) \in \Delta ^ { m }$to the point$\Sigma _ { j = 0 } ^ { n } t _ { j } w _ { j }$with barycentric coordinates$( t _ { 0 } , \ldots , t _ { n } ) \in \Delta ^ { n }$, where

$$
t _ {j} = \sum_ {f (v _ {i}) = w _ {j}} u _ {i}.
$$

It sufices to check this formula for each vertex$v _ { i }$of$\sigma$, with barycentric coordinates$e _ { i }$, which maps to the vertex$f ( v _ { i } ) = w _ { j }$of τ, with barycentric coordinates $e _ { j }$

Since each Euclidean simplex is determined (as the convex span) of its vertices, and each simplicial map is determined (as an afine linear map on each simplex) by its efect on the vertex sets, we can encode the key data in a Euclidean complex in terms of the set of vertices and the subsets that span simplices. This leads to the following abstract version of a Euclidean complex, made independent of the specific embedding in some$\mathbb { R } ^ { N }$

Definition 6.1.13. A simplicial precomplex is a set$K = \{ \sigma \in K \}$of finite non-empty sets$\sigma _ { \mathrm { { i } } }$, called the simplices of$K$. It is called a simplicial complex if each non-empty subset$\tau \subset \sigma$of a simplex in K is again a simplex in$K$. Given a simplicial precomplex$K$, let$K ^ { a } = \{ \bar { \tau } | \emptyset \neq \tau \subseteq \sigma \}$be the associated simplicial complex.

For a simplicial complex K, let$\begin{array} { r } { K _ { 0 } = \bigcup _ { \sigma \in K } \sigma , } \end{array}$, so that each simplex is a subset of$K _ { 0 }$. The elements of$K _ { 0 }$are called the vertices of$K$. A simplex with $( n + 1 )$elements is called an n-simplex. The 0-simplices of K are precisely the singleton sets$\{ v \}$for all vertices v.

A simplicial complex K is finite if the set of simplices K is finite, or equivalently, if the set of vertices$K _ { 0 }$is finite.

Example 6.1.14. To a Euclidean complex K in$\mathbb { R } ^ { N }$we can associate a finite simplicial complex$s K$, with simplices sσ equal to the sets of vertices$\{ v _ { 0 } , \ldots , v _ { n } \}$ of the Euclidean simplices$\sigma$in K. The set$s K _ { 0 } ~ \subset ~ \mathbb { R } ^ { N }$is then the set of all vertices in all of the Euclidean simplices of K. A non-empty subset$s \sigma =$ $\{ v _ { 0 } , \ldots , v _ { n } \} \subseteq s K _ { 0 }$is a simplex in$s K$if and only if the points$v _ { 0 } , \ldots , v _ { n }$are the vertices of a Euclidean simplex$\sigma$in$K$

Example 6.1.15. To a finite simplicial complex$K$we can associate a Euclidean complex eK. First, enumerate the elements of$K _ { 0 }$as$( v _ { 0 } , \ldots , v _ { N } )$. Then, to each simplex$\sigma \in K$, viewed as a subset$\sigma \subseteq K _ { 0 }$, associate the Euclidean simplex eσ in$\mathbb { R } ^ { N }$with vertices the$f _ { j } \in \mathbb { R } ^ { N }$such that$v _ { j } \in \sigma$. The Euclidean complex $e K = \{ e \sigma \mid \sigma \in K \}$is the set of all these Euclidean simplices eσ. Note that all of the vertices$f _ { 0 } , \ldots , f _ { N }$are in general position within$\mathbb { R } ^ { N }$, and that two Euclidean simplices eσ and eτ in${ } _ { \mathcal { A } }$, corresponding to simplices$\sigma , \tau \in K$, meet at the Euclidean simplex$e \sigma \cap e \tau = e ( \sigma \cap \tau )$corresponding to the intersection $\sigma \cap \tau \in K _ { 0 }$, unless that intersection is empty. The resulting Euclidean complex eK is a subcomplex of the Euclidean complex$\sigma ^ { N }$, so$| e K | \subseteq \sigma ^ { N }$

[[Define a simplicial map of simplicial complexes, and the associated category SCx.]]

Remark 6.1.16. Starting with a Euclidean complex$K ,$forming a finite simplicial complex sK as above, and then forming a Euclidean complex$e ( s K )$, there is a simplicial isomorphism$e ( s K ) \cong K$. Conversely, given a finite simplicial complex$K$, forming the Euclidean complex$e K$and the simplicial complex $s ( e K )$, there is a simplicial isomorphism$K \cong s ( e K )$. These two notions of combinatorial complexes are therefore efectively equivalent.

To have well-defined barycentric coordinates in a Euclidean simplex, we needed to fix a total ordering of its vertices. When considering products$K \times L$ of simplicial complexes, it is likewise essential to work with ordered simplices. We follow Eilenberg–Steenrod [17, II.8.7].

Definition 6.1.17. An ordered simplicial complex$( K , \leq )$is a simplicial complex$K = \{ \sigma \in K \}$together with a partial ordering$( K _ { 0 } , \leq )$on its set of vertices, such that

(a) the partial ordering$\leq$restricts to a total ordering on each simplex$\sigma \subseteq K _ { 0 }$ and

(b) two vertices$v _ { 0 } , v _ { 1 } \in K _ { 0 }$are unrelated if$\{ v _ { 0 } , v _ { 1 } \}$is not a simplex in$K$

A simplicial map$f \colon ( K , \leq )  ( L , \leq )$of ordered simplicial complexes is an order-preserving function$f \colon ( K _ { 0 } , \leq )  ( L _ { 0 } , \leq )$between the vertex sets, such that for each simplex$\sigma \subseteq K _ { 0 }$in K the image$f ( \sigma ) \subseteq L _ { 0 }$is a simplex in$L .$ [[The rule$\sigma \mapsto f ( \sigma )$then defines a function$f \colon K \to L . ] ]$We write OSCx for the category of ordered simplicial complexes and simplicial maps.

Example 6.1.18. Each simplicial complex K can be ordered, by first choosing a total ordering on its vertex set$K _ { 0 } .$, and then defining the partial ordering ≤ to agree with the total ordering for pairs$v _ { 0 } , v _ { 1 }$with$\{ v _ { 0 } , v _ { 1 } \}$a simplex in$K ,$ and otherwise making$v _ { 0 } , v _ { 1 }$unrelated.

Example 6.1.19. For each$n \geq 0 .$, let$( \Delta [ n ] , \leq )$be the ordered simplicial complex with vertices$\Delta [ n ] _ { 0 } = [ n ] = \{ 0 < 1 < \cdots < n \}$, given the usual total ordering, and with simplices all non-empty subsets$\varnothing \neq \sigma \subseteq [ n ]$. The corresponding Euclidean complex is$e \Delta [ n ] = \sigma ^ { n }$

Example 6.1.20. For each$n \geq 0$, let$( \partial \Delta [ n ] , \leq ) \subset ( \Delta [ n ] , \leq )$be the ordered simplicial subcomplex with simplices all proper, non-empty subsets$\emptyset \neq \sigma \subset [ n ]$ The corresponding Euclidean complex is$e \partial \Delta [ n ] = \partial \sigma ^ { n }$

Definition 6.1.21. Let$( K , \leq )$and$( L , \leq )$be ordered simplicial complexes. The product$( K \times L , \leq )$has vertex set

$$
(K \times L) _ {0} = K _ {0} \times L _ {0}
$$

with the product partial ordering, so that$( v _ { 0 } , w _ { 0 } ) \leq ( v _ { 1 } , w _ { 1 } )$if and only if$v _ { 0 } \leq$ $v _ { 1 }$in$( K _ { 0 } , \leq )$and$w _ { 0 } \leq w _ { 1 }$in$( L _ { 0 } , \leq ) . \mathrm { ~ A ~ }$finite, nonempty subset$\sigma \subseteq K _ { 0 } \times L _ { 0 }$ is a simplex in$K \times L$if and only if

(a) the restriction of$\leq$to σ is a total ordering,

(b) the projection$p r _ { K } ( \sigma ) \subseteq K _ { 0 }$is a simplex in$K ,$and

(c) the projection$p r _ { L } ( \sigma ) \subseteq L _ { 0 }$is a simplex in L.

Lemma 6.1.22. The product$( K \times L , \leq )$, with the two projection maps$p r _ { K } \colon ( K \times$ $L , \leq )  ( K , \leq )$and$p r _ { L } \colon ( K \times L , \leq ) \to ( L , \leq )$, is the categorical product of $( K , \leq )$and$( L , \leq )$in OSCx.

Proof. Given any ordered simplicial complex$( M , \leq )$and simplicial maps$f \colon M \to$ K and$g \colon M \to L .$, the function$( f , g ) \colon M _ { 0 } \to K _ { 0 } \times L _ { 0 }$defines the unique simplicial map$h \colon M \to K \times L$with$p r _ { K } ( h ) = f , p r _ { K } ( h ) = g . \ [ [ \mathrm { S a y \ m o r e ? } ] ]$□

Example 6.1.23. The product$( \Delta [ m ] \times \Delta [ n ] , \leq )$is the ordered simplicial complex with vertex set

$$
(\Delta [ m ] \times \Delta [ n ]) _ {0} = [ m ] \times [ n ]
$$

given the product partial ordering, so that$( i , j ) \le ( i ^ { \prime } , j ^ { \prime } )$if and only${ \mathrm { i f ~ } } i \leq i ^ { \prime }$ and$j \le j ^ { \prime }$

![](images/page_139_image_14.jpg)

The simplices of$\Delta [ m ] \times \Delta [ n ]$are the finite, nonempty subsets of$[ m ] \times [ n ]$that are totally ordered in the inherited ordering. In other words, the p-simplices are the linear chains

$$
(i _ {0}, j _ {0}) <   (i _ {1}, j _ {1}) <   \dots <   (i _ {p}, j _ {p})
$$

in$[ m ] \times [ n ]$. Note that the projection of such a p-simplex to$\Delta [ m ]$is the simplex $\{ i _ { 0 } , i _ { 1 } , \ldots , i _ { p } \}$, and its projection to$\Delta [ n ]$is the simplex$\{ j _ { 0 } , j _ { 1 } , \dots , j _ { p } \}$. Even if there is no repetition in the linear chain in$[ m ] \times [ n ]$, there may be repetitions in the sequences$i _ { 0 } \leq i _ { 1 } \leq \cdots \leq i _ { p }$and$j _ { 0 } \leq j _ { 1 } \leq \cdots \leq j _ { p } ,$so the projected simplices in$\Delta [ m ]$and$\Delta [ n ]$may well be of lower dimension than$p .$

![](images/page_140_image_1.jpg)

![](images/page_140_image_2.jpg)

The following is a special case of [17, Lem. I.8.9].

Proposition 6.1.24. There is an isomorphism of simplicial complexes

$$
s P ^ {m, n} \cong \Delta [ m ] \times \Delta [ n ].
$$

(The ordering on$\Delta [ m ] \times \Delta [ n ]$thus determines an ordering on$s P ^ { m , n }$, making this an isomorphism in$\mathbf { O S C x . } )$The simplicial maps$\Delta [ m ] \times \Delta [ n ]  \Delta [ m ]$and $\Delta [ m ] \times \Delta [ n ]  \Delta [ n ]$induce a homeomorphism

$$
| e (\Delta [ m ] \times \Delta [ n ]) | \cong | e (\Delta [ m ]) | \times | e (\Delta [ n ]) |.
$$

Proof. There is a bijective correspondence between$( m , n )$-shufles$\pi$and linear chains

$$
(0, 0) = \left(i _ {0}, j _ {0}\right) <   \dots <   \left(i _ {s}, j _ {s}\right) <   \dots <   \left(i _ {m + n}, j _ {m + n}\right) = (m, n)
$$

of length$( m + n )$in$[ m ] \times [ n ]$. It takes a shufle π to the chain with

$$
\begin{array}{l} i _ {s} = \# (\{1, \ldots , s \} \cap \{\pi (1), \ldots , \pi (m) \}) \\ j _ {s} = \# (\{1, \ldots , s \} \cap \{\pi (m + 1), \ldots , \pi (m + n) \}) \end{array}
$$

for$0 \leq s \leq m + n$. Conversely, it takes such a linear chain to the$( m , n )$-shufle $\pi$with

$$
\pi (i) = \min \{s \mid i _ {s} \geq i \}
$$

for$1 \leq i \leq m$, and

$$
\pi (m + j) = \min \{s \mid j _ {s} \geq j \}
$$

for$1 \leq j \leq n$. Going up the linear chain,$( i _ { s } , j _ { s } ) = ( i _ { s - 1 } + 1 , j _ { s - 1 } )$precisely if $s \in \{ \pi ( 1 ) , \ldots , \pi ( m ) \}$, and$( i _ { s } , j _ { s } ) = ( i _ { s - 1 } , j _ { s - 1 } + 1 )$otherwise.

The isomorphism of simplicial complexes takes (the$( m + n )$-simplex corresponding to) the Euclidean$( m + n )$-simplex$\pi ^ { - 1 } ( \sigma ^ { m + n } ) \in P ^ { m , n }$to the$( m + n )$ simplex

$$
(i _ {0}, j _ {0}) <   \dots <   (i _ {s}, j _ {s}) <   \dots <   (i _ {m + n}, j _ {m + n})\tag{6.1}
$$

in$\Delta [ m ] \times \Delta [ n ]$, where π and the$( i _ { s } , j _ { s } )$correspond as above. For example, the Euclidean$( m + n )$-simplex$\sigma ^ { m + n }$corresponds to the chain

$$
(0, 0) <   (1, 0) <   \dots <   (m, 0) <   (m, 1) <   \dots <   (m, n).
$$

A check of definitions shows that two Euclidean$( m + n )$-simplices$\pi _ { 1 } ^ { - 1 } ( \sigma ^ { m + n } )$ and$\pi _ { 2 } ^ { - 1 } ( \sigma ^ { m + n } )$intersect in the face corresponding to intersection of the two corresponding chains, as required for a simplicial isomorphism. [[Elaborate?]]

The projection map$\Delta [ m ] \times \Delta [ n ]  \Delta [ m ]$takes the$( m + n )$-simplex (6.1) to the m-simplex$0 < 1 < \cdots < m$, mapping the elements$( i _ { s } , j _ { s } )$with$\pi ( i ) \leq$ $s < \pi ( i + 1 )$to i. (The elements with$0 \leq s < \pi ( 1 )$map to 0, and the elements with$\pi ( m ) \leq s \leq m + n$map to m.) At the level of polyhedra, it takes the point with barycentric coordinates$\left( t _ { 0 } , t _ { 1 } , \ldots , t _ { m + n } \right)$in the$( m + n )$-simplex (6.1) to the point with barycentric coordinates

$$
\left(t _ {0} + \dots + t _ {\pi (1) - 1}, t _ {\pi (1)} + \dots + t _ {\pi (2) - 1}, \dots , t _ {\pi (m)} + \dots + t _ {m + n}\right)
$$

in the m-simplex$0 < 1 < \cdots < m$. See Example 6.1.12. The resulting map

$$
\sigma^ {m} \times \sigma^ {n} = | P ^ {m, n} | \cong | e (\Delta [ m ] \times \Delta [ n ]) | \rightarrow | e (\Delta [ m ]) | = \sigma^ {m}
$$

takes a point$( w _ { 1 } , \ldots , w _ { m + n } ) = \pi ^ { - 1 } ( u _ { 1 } , \ldots , u _ { m + n } ) = ( u _ { \pi ( 1 ) } , \ldots , u _ { \pi ( m + n ) } )$in $\pi ^ { - 1 } ( \sigma ^ { m + n } ) \subset | { \overline { { P ^ { m , n } } } } |$, which has barycentric coordinates

$$
\left(1 - u _ {1}, u _ {1} - u _ {2}, \dots , u _ {m + n}\right),
$$

to the point with barycentric coordinates

$$
(1 - u _ {\pi (1)}, u _ {\pi (1)} - u _ {\pi (2)}, \dots , u _ {\pi (m)})
$$

in$\sigma ^ { m }$, i.e., the point

$$
\left(u _ {\pi (1)}, \dots , u _ {\pi (m)}\right) = \left(w _ {1}, \dots , w _ {m}\right).
$$

This proves that the composite map$\sigma ^ { m } \times \sigma ^ { n } \to \sigma ^ { m }$equals the projection on the first coordinate, and similarly for the map to$\sigma ^ { n }$. Hence the natural map

$$
| e (\Delta [ m ] \times \Delta [ n ]) | \rightarrow | e (\Delta [ m ]) | \times | e (\Delta [ n ]) |
$$

is a homeomorphism.

[[It may be simpler to discuss the combinatorics of this isomorphism for $m = 1$, then use induction to get an isomorphism with$\Delta [ 1 ] ^ { m } \times \Delta [ n ]$, and then use that$\Delta [ m ]$is a retract of$\Delta [ 1 ] ^ { m }$to get the general case.]]

Example 6.1.25. The product$\sigma ^ { 2 } \times \sigma ^ { 2 }$is a union of six 4-simplices$\pi ^ { - 1 } ( \sigma ^ { 4 } ) \subset$ $I ^ { 4 }$, corresponding to the six (2, 2)-shufles taking (1, 2, 3, 4) to (1, 2, 3, 4), (1, 3, 2, 4), (1, 3, 4, 2), (3, 1, 2, 4), (3, 1, 4, 2) or$( 3 , 4 , 1 , 2 )$. These correspond to the six maximal paths from (0, 0) to (2, 2) in$[ 2 ] \times [ 2 ]$

![](images/page_142_image_1.jpg)

The 4-simplices meet along 3-simplices according to the edges of following graph:

![](images/page_142_image_3.jpg)

The central four 4-simplices all meet along the 2-simplex$( 0 , 0 ) < ( 1 , 1 ) < ( 2 , 2 )$ All 4-simplices meet along the 1-simplex$( 0 , 0 ) < ( 2 , 2 )$

## 6.2 Simplicial sets

Simplicial sets are models for topological spaces, assembled from sets of simplices of varying dimensions. The vertices of each simplex are totally ordered, and the possible identifications between diferent simplices are given by order-preserving functions among the vertex sets, extended (afine) linearly over the simplices. The sets of simplices are assumed to be complete, in the sense that each orderpreserving function to the vertex set of a simplex is assumed to be realized by a map of simplices. This leads to a well-behaved category of models for topological spaces, with all colimits and limits.

General references for simplicial sets are May [42], Fritsch–Piccinini [20, Ch. 4] and Goerss–Jardine [22].

Definition 6.2.1. Let$\Delta$be the skeleton category of finite, nonempty ordinals, with objects

$$
[ n ] = \{0 <   1 <   2 <   \dots <   n \}
$$

for each non-negative integer$n \geq 0 .$, and morphisms$\Delta ( [ m ] , [ n ] )$for$m , n \geq 0$ the set of order-preserving functions

$$
\alpha \colon [ m ] \to [ n ],
$$

i.e., functions α such that$i \leq j$implies$\alpha ( i ) \leq \alpha ( j )$, for$i , j \in [ m ]$

The following indecomposable morphisms$\delta _ { i }$and$\sigma _ { j }$play a special role in$\Delta .$ since they generate all morphisms in$\Delta$under composition.

Definition 6.2.2. For$n \geq 1$and$0 \leq i \leq n$, the i-th coface morphism

$$
\delta_ {i} = \delta_ {i} ^ {n} \colon [ n - 1 ] \to [ n ]
$$

is given by

$$
\delta_ {i} (j) = \left\{ \begin{array}{l l} j & \text { for } j <   i, \\ j + 1 & \text { for } j \geq i. \end{array} \right.
$$

It is the unique injective, order-preserving function$[ n - 1 ] \to [ n ]$such that i is not in its image, or equivalently, such that the preimage of i is empty.

For$n \geq 0$and$0 \leq j \leq n$, the$j - t h$codegeneracy morphism

$$
\sigma_ {j} = \sigma_ {j} ^ {n}: [ n + 1 ] \rightarrow [ n ]
$$

is given by

$$
\sigma_ {j} (i) = \left\{ \begin{array}{l l} i & \text { for } i \leq j, \\ i - 1 & \text { for } i > j. \end{array} \right.
$$

It is the unique surjective, order-preserving function$[ n + 1 ]  [ n ]$such that the preimage of$j$contains two elements (namely$j$and$j + 1 )$

Lemma 6.2.3 (Cosimplicial identities). The coface and codegeneracy morphisms satisfy the following commutation rules:

$$
\left\{ \begin{array}{l l} \delta_ {j} \delta_ {i} = \delta_ {i} \delta_ {j - 1} & f o r i <   j, \\ \sigma_ {j} \delta_ {i} = \delta_ {i} \sigma_ {j - 1} & f o r i <   j, \\ \sigma_ {j} \delta_ {i} = i d & f o r j \leq i \leq j + 1, \\ \sigma_ {j} \delta_ {i} = \delta_ {i - 1} \sigma_ {j} & f o r j + 1 <   i, \\ \sigma_ {j} \sigma_ {i} = \sigma_ {i} \sigma_ {j + 1} & f o r i \leq j. \end{array} \right.
$$

Proof. Let$0 \leq i < j \leq n$. Then both$\delta _ { j } \delta _ { i }$and$\delta _ { i } \delta _ { j - 1 }$map$k \in [ n - 2 ]$to k for $0 \leq k \leq i - 1$, to$k + 1$for$i \le k \le j - 2 .$and to$k + 2$for$j - 1 \leq k \leq n - 2$ Hence the two functions are equal. The proofs in the other cases are similar, and are left as an exercise.□

Lemma 6.2.4. A general morphism α:$[ m ]  [ n ]$in ∆ factors uniquely as the composite of a surjective, order-preserving function$\rho \colon [ m ]  [ p ]$and an injective, order-preserving function$\mu \colon [ p ]  [ n ]$

![](images/page_143_image_15.jpg)

$$
\mu = \delta_ {i _ {r}} \dots \delta_ {i _ {1}}
$$

Furthermore, µ factors uniquely as the composite of$r = n - p$coface morphisms subject to the conditions$0 \leq i _ { 1 } < \cdot \cdot \cdot < i _ { r } \leq n$, and$\rho$factors uniquely as the composite of$s = m - p$codegeneracy morphisms

$$
\rho = \sigma_ {j _ {1}} \dots \sigma_ {j _ {s}}
$$

subject to the conditions$0 \leq j _ { 1 } < \cdot \cdot \cdot < j _ { s } < m$. Hence

$$
\alpha = \mu \rho = \delta_ {i _ {r}} \dots \delta_ {i _ {1}} \sigma_ {j _ {1}} \dots \sigma_ {j _ {s}}.
$$

Proof. We list the elements in [n] that are in the image of$\alpha$in increasing order, as

$$
\mu (0) <   \dots <   \mu (p)
$$

and this defines the injective morphism$\mu ,$with the same image as$\alpha$. The surjective morphism$\rho$is uniquely determined by the condition$\alpha = \mu \rho .$

We list the elements in [n] that are not in the image of$\mu$in increasing order, as

$$
i _ {1} <   \dots <   i _ {r}.
$$

Then the composite injective morphism$\delta _ { i _ { r } } \dots \delta _ { i _ { 1 } } \colon [ p ] \to [ n ]$has the same image as$\mu ,$hence is equal to$\mu$.

We list the elements$j$in$\{ 0 , 1 , \ldots , m - 1 \}$that have the same image under $\rho$as their successor$j + 1$, in increasing order as

$$
j _ {1} <   \dots <   j _ {s}.
$$

Then the composite surjective morphism$\sigma _ { j _ { 1 } } \cdot \cdot \cdot \sigma _ { j _ { s } } \colon [ m ]  [ p ]$identifies$j$and $j + 1$for the same$0 \leq j < m$as$\rho ,$hence is equal to$\rho .$□

Remark 6.2.5. Any finite composable chain of coface and codegeneracy morphisms can be brought to the standard form of Lemma 6.2.4, using only the cosimplicial identities. First all codegeneracies can be brought to the right of all cofaces, using the three expressions for$\sigma _ { j } \delta _ { i }$. Next all cofaces can be brought in order of descending indices, by replacing$\delta _ { i } \delta _ { j - 1 }$by$\delta _ { j } \delta _ { i }$whenever$j - 1 \geq i$ Finally all codegeneracies can be brought in order of increasing indices, by replacing$\sigma _ { j } \sigma _ { i }$by$\sigma _ { i } \sigma _ { j + 1 }$whenever$j \geq i .$

Definition 6.2.6. A simplicial set$X _ { \bullet }$is a contravariant functor$X \colon \Delta ^ { o p }  \mathbf { S e t }$ from$\Delta$to sets. For each object$[ n ]$in$\Delta$we write

$$
X _ {n} = X ([ n ])
$$

for the set of n-simplices in$X _ { \bullet }$. For each morphism$\alpha \colon [ m ] \to [ n ]$in$\Delta$we write

$$
\alpha^ {*} = X (\alpha) \colon X _ {n} \to X _ {m}
$$

for the associated simplicial operator. In particular, for$n \geq 1$and$0 \leq i \leq n$ the$_ { i - t h }$face operator in$X _ { \bullet }$is the function

$$
d _ {i} = \delta_ {i} ^ {*} \colon X _ {n} \to X _ {n - 1},
$$

and for$n \geq 0$and$0 \leq j \leq n$, the$j - t h$degeneracy operator in$X _ { \bullet }$is the function

$$
s _ {j} = \sigma_ {j} ^ {*} \colon X _ {n} \to X _ {n + 1}.
$$

Lemma 6.2.7 (Simplicial identities). The face and degeneracy operators in a simplicial set$X _ { \bullet }$satisfy the following commutation rules:

$$
\left\{ \begin{array}{l l} d _ {i} d _ {j} = d _ {j - 1} d _ {i} & \text { for } i <   j, \\ d _ {i} s _ {j} = s _ {j - 1} d _ {i} & \text { for } i <   j, \\ d _ {i} s _ {j} = i d & \text { for } j \leq i \leq j + 1, \\ d _ {i} s _ {j} = s _ {j} d _ {i - 1} & \text { for } j + 1 <   i, \\ s _ {i} s _ {j} = s _ {j + 1} s _ {i} & \text { for } i \leq j. \end{array} \right.
$$

Proof. This is clear from Lemma 6.2.3 and the contravariance of$X ,$□

The following converse holds.

Lemma 6.2.8. To specify a simplicial set X<sub>•</sub> it is necessary and suficient to specify

(a) a sequence of sets$X _ { n } ~ f o r ~ n \ge 0 .$

(b) functions$d _ { i } \colon X _ { n } \to X _ { n - 1 }$for all$0 \leq i \leq n \geq 1$, and

(c) functions$s _ { j } \colon X _ { n } \to X _ { n + 1 }$for all$0 \leq j \leq n ,$such that

(d) the$d _ { i }$and$s _ { j }$satisfy the simplicial identities.

Proof. For each morphism$\alpha \colon [ m ] \to [ n ]$, the simplicial operator$\alpha ^ { * } \colon X _ { n } \to X _ { m }$ can only be defined as the composite

$$
\alpha^ {*} = s _ {j _ {s}} \dots s _ {j _ {1}} d _ {i _ {1}} \dots d _ {i _ {r}}
$$

where$\alpha = \delta _ { i _ { r } } \ldots \delta _ { i _ { 1 } } \sigma _ { i _ { 1 } } \ldots \sigma _ { i _ { s } }$. The main thing to verify is that this specifies a well-defined functor, so that$( \alpha \beta ) ^ { * } = \beta ^ { * } \alpha ^ { * }$. Since the composite of the standard forms for$\beta$and α can be brought to the standard form for$\alpha \beta$using only the cosimplicial identities, and the$d _ { i }$and$s _ { i }$are assumed to satisfy the simplicial identities, the two functions$( \alpha \beta ) ^ { * }$and$\beta ^ { * } \alpha ^ { * }$will, indeed, be equal.□

Definition$\mathbf { 6 . 2 . 9 . ~ A }$map of simplicial sets$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$is a natural transformation$f \colon X \Rightarrow Y$of functors$\Delta ^ { o p }  \mathrm { \bf ~ S e t }$. Let sSet be the category of simplicial sets and maps, with the obvious notions of identity and composition.

Equivalently, a simplicial map$f _ { \bullet }$amounts to a function

$$
f _ {n} \colon X _ {n} \to Y _ {n}
$$

for each object$[ n ]$in$\Delta .$such that for each morphism$\alpha \colon [ m ]  [ n ]$in$\Delta$the square

$$
\begin{array}{c} X _ {n} \xrightarrow {f _ {n}} Y _ {n} \\ \alpha^ {*} \Biggl \downarrow \\ X _ {m} \xrightarrow {f _ {m}} Y _ {m} \end{array} \Biggl \downarrow \alpha^ {*}
$$

commutes. It sufices to verify this condition for the face and degeneracy operators, meaning that$d _ { i } f _ { n } = f _ { n - 1 } d _ { i }$for$0 \leq i \leq n \geq 1$, and$s _ { j } f _ { n } = f _ { n + 1 } s _ { j }$for $0 \leq j \leq n _ { \cdot }$, since these operators generate all morphisms in$\Delta$

We say that$X _ { \bullet }$is a simplicial subset of$Y _ { \bullet }$if each$X _ { n }$is a subset of$Y _ { n }$and the inclusion$X _ { \bullet } \subseteq Y _ { \bullet }$is a simplicial map.

[[This terminology is imprecise, since we are not talking about a simplicial object in a category of subsets. Saying a “sub simplicial set” might be better, but how to hyphenate this?]]

Lemma 6.2.10. A map$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$of simplicial sets is an isomorphism in sSet if and only if each function$f _ { n } \colon X _ { n } \to Y _ { n }$is bijective.

A degreewise injective map$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$of simplicial sets induces an isomorphism of X<sub>•</sub> with its image$f _ { \bullet } ( X _ { \bullet } )$, as a simplicial subset$o f Y _ { \bullet }$

Proof. The inverse functions$g _ { n } \ = \ f _ { n } ^ { - 1 } \colon Y _ { n } \ \to \ X _ { n }$define a simplicial map $g _ { \bullet } \colon Y _ { \bullet } \to X _ { \bullet } . \operatorname { I f } \ f _ { \bullet }$is simplicial, then the subsets$f _ { n } ( X _ { n } ) \subseteq Y _ { n }$are closed under the simplicial operators. Hence the simplicial structure on$Y _ { \bullet }$restricts to a simplicial structure on$f _ { \bullet } ( X _ { \bullet } )$□

Definition 6.2.11. Recall that for each$n \geq 0$, the standard n-simplex is the convex subspace

$$
\Delta^ {n} = \left\{\left(t _ {0}, \dots , t _ {n}\right) \mid \sum_ {i = 0} ^ {n} t _ {i} = 1, t _ {i} \geq 0 \right\}
$$

of$\mathbb { R } ^ { n + 1 }$spanned by the$( n + 1 )$vertices$e _ { 0 } , e _ { 1 } , \ldots , e _ { n } .$

For each order-preserving function α :$[ m ]  [ n ]$, let$\alpha _ { * } \colon \Delta ^ { m } \to \Delta ^ { n }$be the linear map given by$\alpha _ { * } ( e _ { j } ) = e _ { \alpha ( j ) }$for all$0 \leq j \leq m$. In formulas,

$$
\alpha_ {*} (\sum_ {j = 0} ^ {m} u _ {j} e _ {j}) = \sum_ {j = 0} ^ {m} u _ {j} e _ {\alpha (j)}
$$

for$( u _ { 0 } , u _ { 1 } , \dots , u _ { m } ) \in \Delta ^ { m }$, or equivalently,

$$
\alpha_ {*} (u _ {0}, u _ {1}, \ldots , u _ {m}) = (t _ {0}, t _ {1}, \ldots , t _ {n})
$$

where

$$
t _ {i} = \sum_ {\alpha (j) = i} u _ {j} = \sum_ {j \in \alpha^ {- 1} (i)} u _ {j}.
$$

Example 6.2.12. For each$0 \leq i \leq n \geq 1 , \delta _ { i * } \colon \Delta ^ { n - 1 } \to \Delta ^ { n }$is the embedding

$$
\delta_ {i *} (u _ {0}, u _ {1}, \dots , u _ {n - 1}) = (u _ {0}, \dots , u _ {i - 1}, 0, u _ {i}, \dots , u _ {n - 1})
$$

onto the face of$\Delta ^ { n }$where$t _ { i } = 0$, known as the i-th face. It is opposite to the i-th vertex$e _ { i } ,$where$t _ { i } = 1$

We write

$$
\partial \Delta^ {n} = \bigcup_ {i = 0} ^ {n} \delta_ {i *} (\Delta^ {n - 1})
$$

for the boundary of$\Delta ^ { n }$.

For each$0 \leq j \leq n , \sigma _ { j * } \colon \Delta ^ { n + 1 } \to \Delta ^ { n }$is the identification map a

$$
\sigma_ {j *} (u _ {0}, u _ {1}, \dots , u _ {n + 1}) = (u _ {0}, \dots , u _ {j - 1}, u _ {j} + u _ {j + 1}, u _ {j + 1}, \dots , u _ {n + 1})
$$

that collapses the edge between$e _ { j }$and$e _ { j + 1 }$to one point.

Lemma 6.2.13. The rules$[ n ] \mapsto \Delta ^ { n } , \alpha \mapsto \alpha _ { * }$define a (covariant) functor

$$
\Delta^ {(-)} \colon \Delta \longrightarrow \mathbf {T o p}.
$$

Proof. For α:$[ m ]  [ n ] , \beta \colon [ n ]  [ p ]$the composite$\beta _ { * } \alpha _ { * } \colon \Delta ^ { m } \to \Delta ^ { p }$is given on vertices by$\beta _ { * } \alpha _ { * } ( e _ { j } ) = \beta _ { * } e _ { \alpha ( j ) } = e _ { \beta \alpha ( j ) }$, hence agrees with$( \beta \alpha ) _ { * }$. The relation $( i d _ { [ n ] } ) _ { * } = i d _ { \Delta ^ { n } }$is also clear.口

We view simplicial sets as models for topological spaces by way of the following construction, which is also known as “geometric realization”.

Definition 6.2.14. Let$X _ { \bullet }$be a simplicial set. The topological realization$| X _ { \bullet } |$ is the identification space

$$
\left| X _ {\bullet} \right| = \coprod_ {n \geq 0} X _ {n} \times \Delta^ {n} / \sim
$$

where$\sim$is the equivalence relation generated by the identifications

$$
(x, \alpha_ {*} (\xi)) \sim (\alpha^ {*} (x), \xi)
$$

for all$\alpha \colon [ m ] \to [ n ]$in$\Delta , x \in X _ { n }$and$\xi \in \Delta ^ { m }$. Here we view$( x , \alpha ^ { * } ( \xi ) ) \in X _ { n } \times$ $\Delta ^ { n }$as lying in the n-th summand of the coproduct, while$( \alpha ^ { * } ( x ) , \xi ) \in X _ { m } \times \Delta ^ { m }$ lies in the m-th summand. The same equivalence relation is generated by the identifications

$$
(x, \delta_ {i *} (\xi)) \sim (d _ {i} (x), \xi)
$$

for all$0 \leq i \leq n \geq 1 , x \in X _ { n }$and$\xi \in \Delta ^ { n - 1 }$, and the identifications

$$
(x, \sigma_ {j *} (\xi)) \sim (s _ {j} (x), \xi)
$$

for all$0 \leq j \leq n , x \in X _ { n }$and$\xi \in \Delta ^ { n + 1 }$

Remark 6.2.15. Note how each element$x \in X _ { n } ,$an “abstract” n-simplex, gives rise to a Euclidean n-simplex$\{ x \} \times \Delta ^ { n }$in$\textstyle \prod _ { n \geq 0 } X _ { n } \times \Delta ^ { n }$, that maps to $| X _ { \bullet } |$

Each point in the boundary$\partial \Delta ^ { n } \subset \Delta ^ { n }$of the Euclidean n-simplex lies in some face, say the$i \mathrm { - t h } .$, and can then be written as$\delta _ { i * } ( \xi )$for some$\xi \in \Delta ^ { n - 1 }$ The relation$( x , \delta _ { i * } ( \xi ) ) \sim ( d _ { i } ( x ) , \xi )$tells us that that boundary point of the $x ' \mathrm { t h }$Euclidean n-simplex is identified with a point in the Euclidean$( n - 1 )$ simplex$\{ d _ { i } ( x ) \} \times \Delta ^ { n - 1 }$associated to the abstract$( n - 1 )$-simplex$d _ { i } ( x )$. The face operators$d _ { i } \colon X _ { n } \to X _ { n - 1 }$therefore specify how the boundary faces of each n-simplex are to be identified as$( n - 1 ) { \mathrm { - s i m p l i c e s } }$

Some abstract n-simplices are of the form$s _ { j } ( x )$, for$0 ~ \leq ~ j ~ \leq ~ n$. Here $x \in X _ { n - 1 } ,$and$n \geq 1$. The corresponding Euclidean n-simplex$\{ s _ { j } ( x ) \} \times \Delta ^ { n }$ is then identified with the Euclidean$( n - 1 )$)-simplex$\{ x \} \times { \bar { \Delta } } ^ { n - 1 }$associated to $x ,$via the map$\sigma _ { i * } \colon \Delta ^ { n } \to \Delta ^ { n - 1 }$that collapses the edge from$e _ { j }$to$e _ { j + 1 }$to a point. These Euclidean n-simplices$\{ s _ { j } ( x ) \} \times \Delta ^ { n }$do therefore not contribute any new points to$| X _ { \bullet } |$

Lemma 6.2.16. Let$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$be any map of simplicial sets. The maps

$$
\coprod_ {n \geq 0} f _ {n} \times i d \colon \coprod_ {n \geq 0} X _ {n} \times \Delta^ {n} \longrightarrow \coprod_ {n \geq 0} Y _ {n} \times \Delta^ {n}
$$

descend to a unique map

$$
\left| f _ {\bullet} \right|: \left| X _ {\bullet} \right| \longrightarrow \left| Y _ {\bullet} \right|.
$$

The rules$X _ { \bullet } \mapsto | X _ { \bullet } | , f _ { \bullet } \mapsto | f _ { \bullet } |$define the topological realization functor

$$
| - |: \mathrm{sSet} \longrightarrow \mathrm{Top}.
$$

Proof. For each identification$( x , \alpha _ { * } ( \xi ) ) \sim ( \alpha ^ { * } ( x ) , \xi )$made in$| X _ { \bullet } | ,$we have the identification

$$
(f _ {n} (x), \alpha_ {*} (\xi)) \sim (\alpha^ {*} (f _ {n} (x)), \xi) = (f _ {m} (\alpha^ {*} (x)), \xi)
$$

between the image points, made in$| Y _ { \bullet } | , \mathrm { s o } \ | f _ { \bullet } |$is well-defined. Given a second map$g _ { \bullet } \colon Y _ { \bullet } \to Z _ { \bullet }$of simplicial sets, the maps$| g _ { \bullet } f _ { \bullet } |$and$| g _ { \bullet } | | f _ { \bullet } |$are both induced by

$$
\coprod_ {n \geq 0} g _ {n} f _ {n} \times i d = (\coprod_ {n \geq 0} g _ {n} \times i d) \circ (\coprod_ {n \geq 0} f _ {n} \times i d),
$$

hence are equal.

Remark 6.2.17. We shall later show that$| X _ { \bullet } |$is a CW complex and that $| f _ { \bullet } |$is a cellular map. We may then think of$| - |$as a functor to CW. This afects our interpretation of the topology of products like$| X _ { \bullet } | \times | Y _ { \bullet } |$, since in CW we use the weak (compactly generated) topology on this product, rather than the cartesian product topology. [[If we replace Top by$\boldsymbol { \mathcal U }$, this makes no diference.]]

Definition 6.2.18. Let Y be any topological space. The singular simplicial set sing(Y) is the simplicial set with n-simplices

$$
\mathrm{sing} (Y) _ {n} = \mathbf {T o p} (\Delta^ {n}, Y)
$$

the set of maps$\sigma \colon \Delta ^ { n }  Y$, and with simplicial operators

$$
\alpha^ {*} = \mathbf {T o p} (\alpha_ {*}, Y) \colon \operatorname{sing} (Y) _ {n} \to \operatorname{sing} (Y) _ {m}
$$

for all$\alpha \colon [ m ] \ \to \ [ n ]$in$\Delta .$, taking a singular n-simplex$\sigma \colon \Delta ^ { n } \  \ Y$to the composite$\alpha ^ { * } ( \sigma ) = \sigma \circ \alpha _ { * } \colon \Delta ^ { m }  Y$

For example,$d _ { i } ( \sigma ) ~ = ~ \sigma \circ ~ \delta _ { i * }$is the restriction of$\sigma$to the i-th face of $\Delta ^ { n }$, composed with the identification of that face with$\Delta ^ { n - 1 }$. It is clear that sing$( Y ) \colon \Delta ^ { o p } \$Set is a (contravariant) functor, since$( \beta \alpha ) ^ { * } ( \sigma ) \ = \ \sigma \beta \alpha \ =$ $\alpha ^ { * } \beta ^ { * } ( \sigma )$for all composable α, β and σ.

Lemma 6.2.19. Let$f \colon X \to Y$be any map of topological spaces. The functions $f _ { n } \colon \operatorname { s i n g } ( X ) _ { n } \to \operatorname { s i n g } ( Y ) _ { n }$, that take$\sigma \colon \Delta ^ { n } \to X$to$f _ { n } ( \sigma ) = f \sigma \colon \Delta ^ { n }  Y$2 define a simplicial map

$$
f _ {\bullet} \colon \operatorname{sing} (X) _ {\bullet} \longrightarrow \operatorname{sing} (Y) _ {\bullet}.
$$

The rules$X \mapsto \operatorname* { s i n g } ( X ) _ { \bullet } , ~ f \mapsto f _ { * }$define a functor

$$
\mathrm{sing:Top} \longrightarrow \mathrm{sSet}.
$$

Proof. To define a simplicial map, the functions$f _ { n }$for$n \geq 0$must satisfy $\alpha ^ { * } f _ { n } = f _ { m } \alpha ^ { * }$for all$\alpha \colon [ m ] \to [ n ]$, but for each$\sigma \colon \Delta ^ { n } \to X$we have$\alpha ^ { * } ( f _ { n } ( \sigma ) ) =$ $f \sigma \alpha _ { * } = f _ { m } ( \alpha ^ { * } ( \sigma ) )$), so this is clear.

$$
\Delta^ {m} \xrightarrow {\alpha_ {*}} \Delta^ {n} \xrightarrow {\sigma} X \xrightarrow {f} Y
$$

Given a second map$g \colon Y \to Z ,$it is clear that$( g f ) _ { \bullet } = g _ { \bullet } f _ { \bullet } .$, since$( g f ) _ { n } ( \sigma )$= $g f \sigma = g _ { n } ( f _ { n } ( \sigma ) )$for all$n \geq 0$and$\sigma \colon \Delta ^ { n } \to X$. Also$( i d _ { X } ) _ { \bullet } = i d _ { \mathrm { s i n g } ( X ) } .$is clear.□

These two constructions are adjoint.

Proposition 6.2.20. There is natural bijection

$$
\operatorname{Top} \left(\left| X _ {\bullet} \right|, Y\right) \cong \mathrm{sSet} \left(X _ {\bullet}, \operatorname{sing} (Y) _ {\bullet}\right),
$$

making topological realization left adjoint to the singular simplicial set functor.

$$
\text { sSet } \xrightarrow [ \text { sing } (-) _ {\bullet} ]{| - |} \text { Top }
$$

Proof. Each map$f \colon | X _ { \bullet } | \to Y$corresponds to maps$f _ { n } \colon X _ { n } \times \Delta ^ { n } \to Y$for all$n \geq 0 ,$, compatible for all morphisms α in$\Delta$, which in turn correspond to functions$g _ { n } \colon X _ { n } \to \mathbf { T o p } ( \Delta ^ { n } , Y ) = \mathrm { s i n g } ( Y ) _ { n }$for all$n \geq 0$, satisfying similar compatibilities. This is the same as a map$g _ { \bullet } \colon X _ { \bullet } \to \operatorname { s i n g } ( Y )$<sub>•</sub> of simplicial sets.□

All small colimits and limits of simplicial sets exist, and are constructed degreewise.

Lemma 6.2.21. Let$X _ { \bullet } \colon \mathcal { C }$sSet be a$\mathcal { C } .$-shaped diagram of simplicial sets, with$\mathcal { C }$small. The colimit$Y _ { \bullet } = \mathrm { c o l i m } _ { \mathcal { C } } X _ { \bullet }$exists, with n-simplices

$$
Y _ {n} = \underset {\mathcal {C}} {\operatorname{colim}} X _ {n}  .
$$

Dually, the limit$Z _ { \bullet } = \operatorname* { l i m } _ { \mathcal { C } } X _ { \bullet }$<sub>•</sub> exists, with n-simplices

$$
Z _ {n} = \lim _ {\mathcal {C}} X _ {n}.
$$

Proof. For each$\alpha \colon [ m ] \to [ n ]$in$\Delta$, the functions

$$
\alpha_ {c} ^ {*} \colon X _ {n} (c) \to X _ {m} (c)
$$

for objects c in$\mathcal { C }$define a natural transformation$\alpha ^ { * } \colon X _ { n } \Rightarrow X _ { m }$of functors $\mathcal { C } \to \mathbf { S e t }$, and induce a function of colimits

$$
\alpha^ {*} \colon Y _ {n} = \underset {c \in \mathcal {C}} {\operatorname{colim}} X _ {n} (c) \longrightarrow \underset {c \in \mathcal {C}} {\operatorname{colim}} X _ {m} (c) = Y _ {m}  .
$$

It is straightforward to check that this makes$Y _ { \bullet }$a simplicial set, with the universal property of the colimit.

The limit case is dual.

Corollary 6.2.22. The topological realization functor$| - | \colon$: sSet → Top commutes with all small colimits:

$$
\underset {c \in \mathcal {C}} {\mathrm{colim}} | X _ {\bullet} (c) | \cong | \underset {c \in \mathcal {C}} {\mathrm{colim}} X _ {\bullet} (c) |
$$

Proof. This is clear from Propositions 4.3.36 and 6.2.20.

Definition 6.2.23. A based simplicial set is a pair$( X _ { \bullet } , x _ { 0 } )$, where$X _ { \bullet }$is a simplicial set and$x _ { 0 } \in X _ { 0 }$is a chosen 0-simplex. For each$n \geq 0$the set of n-simplices is then viewed as based at$s _ { 0 } ^ { n } ( x _ { 0 } ) \in X _ { n } ,$where$\sigma _ { 0 } ^ { n } \colon [ n ] \ \to \ [ 0 ]$is the unique morphism and$s _ { 0 } ^ { n } = ( \sigma _ { 0 } ^ { n } ) ^ { * }$. A based simplicial map$f _ { \bullet } \colon ( X _ { \bullet } , x _ { 0 } )$ $( Y _ { \bullet } , y _ { 0 } )$is a simplicial map$f _ { \bullet }$such that$f _ { 0 } ( x _ { 0 } ) = y _ { 0 }$. Note that$f _ { n } ( s _ { 0 } ^ { n } ( x _ { 0 } ) ) =$ $s _ { 0 } ^ { n } ( y _ { 0 } )$for all$n \geq 0$. These objects and morphisms define a category sSet<sub>∗</sub>.

The topological realization$| X _ { \bullet } |$is based at the image of$\{ x _ { 0 } \} \times \Delta ^ { 0 }$, also denoted$x _ { 0 }$. It defines a functor$\mathbf { s S e t } _ { * } \to \mathbf { T o p } _ { * }$. The smash product$X _ { \bullet } \wedge Y _ { \bullet }$is given in simplicial degree n by

$$
(X _ {\bullet} \wedge Y _ {\bullet}) _ {n} = X _ {n} \wedge Y _ {n}
$$

and there is a canonical simplicial isomorphism$( X _ { \bullet } \times Y _ { \bullet } ) / ( X _ { \bullet } \vee Y _ { \bullet } ) \cong ( X _ { \bullet } \wedge Y _ { \bullet } )$

Definition 6.2.24. Let$( - ) ^ { o p } \colon \Delta  \Delta$be the (covariant) functor reversing the total ordering of the objects, taking [n] to$[ n ]$, but taking$\alpha \colon [ m ]  [ n ]$to $\alpha ^ { o p } \colon [ m ] \to [ n ]$given by

$$
\alpha^ {o p} (i) = n - \alpha (m - i)
$$

for$i \in [ m ]$. For example,$\delta _ { i } ^ { o p } = \delta _ { n - i } \colon [ n - 1 ] \to [ n ]$and$\sigma _ { j } ^ { o p } = \sigma _ { n - j } ^ { o p } : [ n + 1 ] \to [ n ]$ The composite$( - ) ^ { o p } \circ ( - ) ^ { o p }$is the identity.

For a simplicial set$X _ { \bullet }$, given by a functor$X \colon \Delta ^ { o p }  \mathbf { S e t }$, let the opposite simplicial set$X _ { \bullet } ^ { o p }$be given by the composite functor

$$
X \circ ((-) ^ {o p}) ^ {o p} \colon \Delta^ {o p} \longrightarrow \Delta^ {o p} \longrightarrow X.
$$

It takes$[ n ]$to$X _ { n } ^ { o p } = X _ { n }$on objects, but takes$\alpha \colon [ m ]  [ n ]$to$( \alpha ^ { o p } ) ^ { * } \colon X _ { n } \to$ $X _ { m }$on morphisms. Hence the i-th face operator$d _ { i } ^ { o p } \colon X _ { n } ^ { o p } \ \to \ X _ { n - 1 } ^ { o p }$equals $d _ { n - i } \colon X _ { n } \to X _ { n - 1 }$, and the$j \mathrm { - t h }$degeneracy operator$s _ { j } ^ { o p } \colon \ddot { X } _ { n } ^ { o p } \longrightarrow \ddot { X _ { n + 1 } ^ { o p } }$equals $s _ { n - j } \colon X _ { n } \to X _ { n + 1 }$

Lemma 6.2.25. There is a natural cellular homeomorphism

$$
o \colon | X _ {\bullet} ^ {o p} | \cong | X _ {\bullet} |
$$

such that the composite$o ^ { 2 } \colon | ( X _ { \bullet } ^ { o p } ) ^ { o p } | \cong | X _ { \bullet } ^ { o p } | \cong | X _ { \bullet } |$is the identity.

Proof. Let$o _ { n } \colon \Delta ^ { n } \to \Delta ^ { n }$be the homeomorphism reversing the order of the barycentric coordinates, taking$\left( t _ { 0 } , t _ { 1 } , \ldots , t _ { n } \right)$to$\left( t _ { n } , \ldots , t _ { 1 } , t _ { 0 } \right)$. It takes the i-th vertex$e _ { i }$to the$( n - i ) – \mathrm { t h }$vertex$e _ { n - i }$. The maps

$$
\coprod_ {n \geq 0} i d \times o _ {n} \colon \coprod_ {n \geq 0} X _ {n} ^ {o p} \times \Delta^ {n} \longrightarrow \coprod_ {n \geq 0} X _ {n} \times \Delta^ {n},
$$

taking$( x , \xi ) \in X _ { n } \times \Delta ^ { n } = X _ { n } ^ { o p } \times \Delta ^ { n } { \mathrm { ~ t o ~ } } ( x , o _ { n } ( \xi ) ) \in X _ { n } \times \Delta$, descend to a unique map

$$
o \colon | X _ {\bullet} ^ {o p} | \longrightarrow | X _ {\bullet} |
$$

since$\alpha _ { * } ^ { o p } \circ o _ { m } = o _ { n } \circ \alpha _ { * } \colon \Delta ^ { m }  \Delta ^ { n }$. [[Elaborate?]] Clearly$o ^ { 2 } = i d$, so o is a homeomorphism.□

## 6.3 The role of non-degenerate simplices

Example 6.3.1. Let$( K , \leq )$be an ordered simplicial complex. There is an associated simplicial set$X _ { \bullet } ,$, with n-simplices the linear chains

$$
x = (v _ {0} \leq v _ {1} \leq \dots \leq v _ {n})
$$

in the partially ordered vertex set$( K _ { 0 } , \leq )$, such that$\{ v _ { 0 } , v _ { 1 } , \ldots , v _ { n } \}$is a simplex in$K ,$, necessarily of dimension less than or equal to n. In particular,$X _ { 0 } = K _ { 0 }$ For each morphism$\alpha \colon [ m ] \to [ n ]$], the function$\alpha ^ { * } \colon X _ { n } \to X _ { m }$maps an n-simplex x as above to the m-simplex

$$
\alpha^ {*} (x) = \left(v _ {\alpha (0)} \leq v _ {\alpha (1)} \leq \dots \leq v _ {\alpha (m)}\right).
$$

For example, when$\alpha = \delta _ { i } \colon [ n - 1 ] \to [ n ]$, the face operator$d _ { i } \colon X _ { n } \to X _ { n - 1 }$ omits the i-th vertex$v _ { i }$in the linear chain defining$x \in X _ { n }$

$$
d _ {i} (x) = \left(v _ {0} \leq \dots \leq v _ {i - 1} \leq v _ {i + 1} \leq \dots \leq v _ {n}\right)
$$

When$\alpha = \sigma _ { j } \colon [ n + 1 ] \to [ n ]$the degeneracy operator$s _ { j } \colon X _ { n } \to X _ { n + 1 }$repeats the j-th vertex$v _ { j }$in the linear chain.

$$
s _ {j} (x) = \left(v _ {0} \leq \dots \leq v _ {j - 1} \leq v _ {j} = v _ {j} \leq v _ {j + 1} \leq \dots \leq v _ {n}\right)
$$

Let$( K , \leq ) , ( L , \leq )$be ordered simplicial complexes with associated simplicial sets$X _ { \bullet }$and$Y _ { \bullet } .$, and let$f \colon ( K , \leq )  ( L , \leq )$be a simplicial map of ordered simplicial complexes, given by the order-preserving function$f \colon ( K _ { 0 } , \leq )  ( L _ { 0 } , \leq )$ There is an associated map of simplicial sets$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$, with components $f _ { n } \colon X _ { n } \to Y _ { n }$taking an n-simplex x as above to the n-simplex

$$
f _ {n} (x) = \left(f \left(v _ {0}\right) \leq f \left(v _ {1}\right) \leq \dots \leq f \left(v _ {n}\right)\right).
$$

We therefore have a functor

$$
\mathrm{OSCx} \longrightarrow \mathrm{sSet}.
$$

[[Explain why$| X _ { \bullet } |$is homeomorphic to the underlying polyhedron$| e K |$of an associated Euclidean complex?]]

Remark 6.3.2. An n-simplex$\sigma \subseteq K _ { 0 }$in an ordered simplicial set is determined by its$( n + 1 )$vertices, since$\sigma = \{ v \in \sigma \}$. A simplex$x \in X _ { n }$of a simplicial set also has vertices, namely the elements$v _ { i } = \epsilon _ { i } ^ { * } ( x ) \in X _ { 0 }$for$0 \leq i \leq n .$, where $\epsilon _ { i } \colon [ 0 ]  [ n ]$is given by$\epsilon _ { i } ( 0 ) = i$. However, these$( n + 1 )$elements do not need to be distinct. Furthermore, the n-simplex X is not necessarily determined by its vertices$( v _ { 0 } , \ldots , v _ { n } )$We can identify OSCx with the full subcategory of sSet generated by the simplicial sets X such that each simplex$x$is uniquely determined by its set of vertices$\{ \epsilon _ { i } ^ { * } ( x ) \} _ { i }$. [[Elaborate?]] [[If each non-degenerate n-simplex has$( n + 1 )$distinct vertices, we say that X is non-singular.]]

Definition 6.3.3. For each$n \geq 0$, let the simplicial n-simplex$\Delta _ { \bullet } ^ { n }$be the contravariant functor$\Delta ( - , [ n ] ) = { \mathcal { Y } } _ { [ n ] } \colon \Delta ^ { o p } \to$Set represented by the object [n] in$\Delta .$It has p-simplices

$$
\Delta_ {p} ^ {n} = \Delta ([ p ], [ n ]) = \{\text { all   order - preserving   functions } \zeta : [ p ] \to [ n ] \}
$$

and simplicial structure maps

$$
\beta^ {*} \colon \Delta_ {p} ^ {n} \to \Delta_ {q} ^ {n}
$$

taking$\zeta \colon [ p ]  [ n ]$to$\beta ^ { * } ( \zeta ) = \zeta \circ \beta \colon [ q ] \to [ n ]$, for each morphism$\beta \colon [ q ]  [ p ]$ in$\Delta$.

For each morphism$\alpha \colon [ m ] \to [ n ]$in$\Delta$, there is a map of simplicial sets

$$
\alpha_ {\bullet} \colon \Delta_ {\bullet} ^ {m} \longrightarrow \Delta_ {\bullet} ^ {n},
$$

which on p-simplices is given by the function

$$
\Delta ([ p ], \alpha) \colon \Delta ([ p ], [ m ]) \longrightarrow \Delta ([ p ], [ n ])
$$

taking$\zeta \colon [ p ]  [ m ]$to$\alpha \circ \zeta \colon [ p ]  [ n ]$

Lemma 6.3.4. For each$n \geq 0$there is a natural bijective correspondence

$$
\mathbf {s S e t} (\Delta_ {\bullet} ^ {n}, X _ {\bullet}) \xrightarrow {\cong} X _ {n}
$$

taking a simplicial map$f \colon \Delta _ { \bullet } ^ { n }  X .$<sub>•</sub> to the n-simplex$f _ { n } ( i d _ { [ n ] } ) \ \in { \cal X } _ { n }$. Here $i d _ { [ n ] } \in \Delta _ { n } ^ { n }$. The inverse takes an n-simplex$x \in X _ { n }$to the characteristic map

$$
x _ {\bullet} \colon \Delta_ {\bullet} ^ {n} \to X _ {\bullet},
$$

given in simplicial degree$p$by$x _ { p } ( \zeta ) = \zeta ^ { * } ( x ) \ f o r \ \zeta \colon [ p ] \to [ n ] \ \ i$in$\Delta _ { p } ^ { n }$

Proof. It is clear that$x _ { \bullet }$is simplicial, and that the two constructions are mutually inverse.□

[[Could have discussed Yoneda embedding$\mathcal { Y } : \mathcal { C } \to \mathbf { F u n } ( \mathcal { C } ^ { o p } , \mathbf { S e t } )$earlier, specializing to$\Delta$sSet in this case.]]

Remark 6.3.5. This notation is consistent with the notation$\alpha _ { \bullet } \colon \Delta _ { \bullet } ^ { m } \to \Delta _ { \bullet } ^ { n }$ for the simplicial map induced by a morphism$\alpha \colon [ m ] \to [ n ]$in$\Delta$, when viewed as a simplex$\alpha \in \Delta _ { m } ^ { n }$

Lemma 6.3.6. The simplicial set associated to the ordered simplicial complex $( \Delta [ n ] , \leq )$is (isomorphic to) the simplicial n-simplex$\Delta _ { \bullet } ^ { n }$

Proof. Recall from Example 6.1.19 that the vertex set of$\Delta [ n ]$is the totally ordered set$( [ n ] , \leq )$, so the p-simplices of the associated simplicial set are the linear chains

$$
(z _ {0} \leq z _ {1} \leq \dots \leq z _ {p})
$$

in [n], which we can identify with the order-preserving functions$\zeta \colon [ p ]  [ n ]$ with values$\zeta ( i ) = z _ { i }$. By definition,$\alpha ^ { * }$takes the linear chain to

$$
\left(\zeta_ {\alpha (0)} \leq \zeta_ {\alpha (1)} \leq \dots \leq \zeta_ {\alpha (q)}\right),
$$

which is identified with the composite function$\zeta \circ \alpha = \alpha ^ { * } ( \zeta )$. Hence the two simplicial sets are isomorphic.□

Lemma 6.3.7. The rules$[ n ] \mapsto \Delta _ { \bullet } ^ { n }$, α 7→ α<sub>•</sub> define a (covariant) functor

$$
\Delta_ {\bullet} ^ {(-)} \colon \Delta \longrightarrow \mathbf {s S e t}.
$$

Proof. It is clear that$( \beta \alpha ) _ { \bullet } = \beta _ { \bullet } \alpha _ { \bullet }$

Lemma 6.3.8. There is a natural homeomorphism$| \Delta _ { \bullet } ^ { ( - ) } | \cong \Delta ^ { ( - ) }$of functors $\Delta$Top. In other words, there is a homeomorphism

$$
| \Delta_ {\bullet} ^ {n} | \cong \Delta^ {n}
$$

for each$n \geq 0$, such that$| \alpha _ { \bullet } | : | \Delta _ { \bullet } ^ { m } |  | \Delta _ { \bullet } ^ { n } |$corresponds to$\alpha _ { * } \colon \Delta ^ { m } \to \Delta ^ { n }$, for all$\alpha \colon [ m ] \to [ n ]$in$\Delta$.

Proof. The map

$$
\coprod_ {p \geq 0} \Delta_ {p} ^ {n} \times \Delta^ {p} \longrightarrow \Delta^ {n}
$$

taking$( \zeta , \xi ) \in \Delta _ { \upsilon } ^ { n } \times \Delta ^ { p }$to$\zeta _ { * } ( \xi ) \in \Delta ^ { n }$sends both$( \alpha ^ { * } ( \zeta ) , \xi )$and$( \zeta , \alpha _ { * } ( \xi ) )$to the same point, hence induces a map$| \Delta _ { \bullet } ^ { n } | \longrightarrow \Delta ^ { n }$. An inverse map takes$\xi \in \Delta ^ { n }$ to the image of$( i d _ { [ n ] } , \xi ) \in \Delta _ { n } ^ { n } \times \Delta ^ { n }$. One composite takes ξ to$i d _ { [ n ] * } ( \xi ) = \xi .$ The other composite takes the equivalence class of$( \zeta , \xi )$in$| \Delta _ { \bullet } ^ { n } |$to the class of $( i d _ { [ n ] } , \zeta _ { * } ( \xi ) )$, but these are the same, since$\zeta ^ { * } ( i d _ { [ n ] } ) = \zeta$. Hence the two maps are mutually inverse homeomorphisms.

To check naturality with respect to$\alpha \colon [ m ] \to [ n ]$, note that$( \zeta , \xi ) \in \Delta _ { \upsilon } ^ { m } \times \Delta ^ { p }$ corresponds to$\zeta _ { * } ( \xi ) \in \Delta ^ { m }$, which maps to$\alpha _ { * } ( \zeta _ { * } ( \xi ) )$in$\Delta ^ { n }$. On the other hand, $( \zeta , \xi )$maps to$( \alpha \zeta , \xi ) \in \Delta _ { p } ^ { n } \times \Delta ^ { p }$, which corresponds to$( \alpha \zeta ) _ { * } ( \xi )$in$\Delta ^ { m }$. These points are equal.□

Definition 6.3.9. For each$n \geq 0$the simplicial boundary (n − 1)-sphere$\partial \Delta _ { \bullet } ^ { n }$ is the simplicial subset of$\Delta _ { \bullet } ^ { n }$with$p \mathrm { - }$simplices

$$
\partial \Delta_ {p} ^ {n} = \{\zeta \in \Delta_ {p} ^ {n} \mid \zeta : [ p ] \rightarrow [ n ] \text {   is   not   surjective } \}
$$

the set of order-preserving functions$\zeta \colon [ p ]  [ n ]$with$\zeta ( [ p ] ) \neq [ n ]$, i.e., the non-surjective order-preserving functions.

Lemma 6.3.10. The simplicial set associated to the ordered simplicial complex $( \partial \Delta [ n ] , \leq )$is (isomorphic to) the simplicial boundary$( n - 1 )$-sphere$\partial \Delta _ { \bullet } ^ { n }$

Proof. The p-simplices of the associated simplicial set are the linear chains

$$
(z _ {0} \leq z _ {1} \leq \dots \leq z _ {p})
$$

in [n] such that$\{ z _ { 0 } , z _ { 1 } , \ldots , z _ { p } \}$are the vertices of a simplex in$\partial \Delta [ n ]$, which is equivalent to asking that$\{ z _ { 0 } , z _ { 1 } , \dotsc , z _ { p } \}$is a (non-empty) proper subset of$[ n ] _ { \cdot }$ which in turn is equivalent to the condition that the order-preserving function $\zeta \colon [ p ]  [ n ]$with$\zeta ( i ) = z _ { i }$is not surjective.□

Lemma 6.3.11. The inclusion$\partial \Delta _ { \bullet } ^ { n } \subset \Delta _ { \bullet } ^ { n }$induces the embedding$\partial \Delta ^ { n } \subset \Delta ^ { n }$ upon topological realization.

Proof. Let$\mathcal { C }$be the subcategory of the overcategory$\Delta / [ n ]$, consisting of pairs $( p , \mu )$where$\mu \colon [ p ]  [ n ]$in$\Delta$is injective but not the identity. We can identify it with the partially ordered set of proper, non-empty subsets$\emptyset \neq S \subset [ n ]$, by taking$\mu$to its image. In this way is also corresponds to the category of proper faces of$\Delta ^ { n }$

Let$F \colon \mathcal { C } \ \to \ \mathbf { s S e t }$be the functor$F ( [ p ] , \mu ) ~ = ~ \Delta _ { \bullet } ^ { p }$, taking a morphism $\beta \colon [ q ]  [ p ]$from$( q , \beta \mu )$to$( p , \mu )$, to the simplicial map$\beta _ { \bullet } \colon \Delta _ { \bullet } ^ { q } \to \Delta _ { \bullet } ^ { p }$. Then the compatible maps$j _ { ( p , \mu ) } = \mu _ { \bullet } \colon \Delta _ { \bullet } ^ { p } \to \Delta _ { \bullet } ^ { n }$induce a map

$$
\underset {\mathcal {C}} {\operatorname{colim}} F = \underset {(p, \mu) \in \mathcal {C}} {\operatorname{colim}} \Delta_ {\bullet} ^ {p} \longrightarrow \Delta_ {\bullet} ^ {n},
$$

which identifies the colimit with$\partial \Delta _ { \bullet } ^ { n }$inside of the target. This can be checked degreewise, as an identity of sets. By Corollary 6.2.22, we get a homeomorphism

$$
\operatorname * {c o l i m} _ {(p, \mu) \in \mathscr {C}} \Delta^ {p} = \operatorname * {c o l i m} _ {(p, \mu) \in \mathscr {C}} | \Delta_ {\bullet} ^ {p} | \cong | \operatorname * {c o l i m} _ {(p, \mu) \in \mathscr {C}} \Delta_ {\bullet} ^ {p} | \cong | \partial \Delta_ {\bullet} ^ {n} |
$$

and it is clear that coli$\mathrm { { ( } } p , \mu ) \in \mathcal { C } \Delta ^ { p } = \partial \Delta ^ { n }$

Exercise 6.3.12. Enumerate the n-simplices of$\Delta _ { \bullet } ^ { 1 }$as

$$
\Delta_ {n} ^ {1} = \{\zeta_ {0} ^ {n}, \ldots , \zeta_ {n + 1} ^ {n} \}
$$

where$\zeta _ { k } ^ { n } \colon [ n ] \to [ 1 ]$maps$\{ 0 , \ldots , k - 1 \}$to 0 and$\{ k , \ldots , n \}$to 1, for$0 \leq k \leq$ $n + 1$. Show that

$$
d _ {i} (\zeta_ {k} ^ {n}) = \left\{ \begin{array}{l l} \zeta_ {k - 1} ^ {n - 1} & \text {for} 0 \leq i <   k \\ \zeta_ {k} ^ {n - 1} & \text {for} k \leq i \leq n \end{array} \right.
$$

for$n \geq 1$, and

$$
s _ {j} (\zeta_ {k} ^ {n}) = \left\{ \begin{array}{l l} \zeta_ {k + 1} ^ {n + 1} & \text { for } 0 \leq j <   k \\ \zeta_ {k} ^ {n + 1} & \text { for } k \leq j \leq n \end{array} \right.
$$

for$n \geq 0$. Show that the nondegenerate simplices of$\Delta _ { \bullet } ^ { 1 }$(see Definition 6.3.15) are$\zeta _ { 0 } ^ { 0 } , \zeta _ { 1 } ^ { 0 }$and$\zeta _ { 1 } ^ { 1 }$.

With notation as above, the n-simplices of$\partial \Delta _ { \bullet } ^ { 1 }$are

$$
\partial \Delta_ {n} ^ {1} = \{\zeta_ {0} ^ {n}, \zeta_ {n + 1} ^ {n} \}.
$$

Enumerate the n-simplices of$S _ { \bullet } ^ { 1 } = \Delta _ { \bullet } ^ { 1 } / \partial \Delta _ { \bullet } ^ { 1 }$as

$$
S _ {n} ^ {1} = \{\zeta_ {0} ^ {n}, \dots , \zeta_ {n} ^ {n} \},
$$

where now$\zeta _ { 0 } ^ { n } = \zeta _ { n + 1 } ^ { n }$. Obtain formulas for$d _ { i } ( \zeta _ { k } ^ { n } )$and$s _ { j } ( \zeta _ { k } ^ { n } )$in$S _ { \bullet } ^ { 1 }$, for all$0 \leq$ $i , j , k \le n$. Note in particular that$d _ { n } ( \zeta _ { n } ^ { n } ) = \zeta _ { 0 } ^ { n - 1 }$. What are the nondegenerate simplices of$S _ { \bullet } ^ { 1 \cdot } ?$

[[Relate$S _ { \bullet } ^ { 1 }$to the Hochschild complex of a ring$R . ] ]$

Remark 6.3.13. We can identify$\Delta _ { n } ^ { 1 } \cong [ n + 1 ]$as sets, taking$\zeta _ { k } ^ { n } \in \Delta _ { n } ^ { 1 }$to $k \in [ n + 1 ]$. Then d :$\Delta _ { n } ^ { 1 }  \Delta _ { n - 1 } ^ { 1 }$corresponds to$\sigma _ { i } \colon [ n + 1 ] \to [ n ]$in$\Delta ,$and $s _ { j } \colon \dot { \Delta } _ { n } ^ { 1 }  \mathbf { \bar { \Delta } } _ { n + 1 } ^ { 1 }$corresponds to$\delta _ { j + 1 } \colon [ n + 1 ] \to [ n + 2 ]$. We get a (contravariant) functor$\Delta ^ { 1 } \colon \dot { \Delta ^ { o p } }  \Delta \subset \mathbf { S e t }$, taking [n] to$[ n + 1 ]$

Remark 6.3.14. We have at least three useful simplicial models for the topological n-sphere$S ^ { n }$. One is the simplicial boundary n-sphere$\partial \Delta _ { \bullet } ^ { n + 1 }$with $| \partial \bar { \Delta } _ { \bullet } ^ { n + 1 } | \cong \partial \Delta ^ { n + 1 }$. This is the source of the attaching map of$( n + 1 )$-cells in the CW structure on the topological realization of a simplicial set.

Another is the quotient n-sphere$\Delta _ { \bullet } ^ { n } / \partial \Delta _ { \bullet } ^ { n }$with$| \Delta _ { \bullet } ^ { n } / \partial \Delta _ { \bullet } ^ { n } | \cong \Delta ^ { n } / \partial \Delta ^ { n }$. This is the minimal model for$S ^ { n }$as a based space, and can be used in the description of simplicial homotopy groups.

A third is the n-fold smash product$S _ { \bullet } ^ { 1 } \wedge \cdots \wedge S _ { \bullet } ^ { 1 }$where$S _ { \bullet } ^ { 1 } = \Delta _ { \bullet } ^ { 1 } / \partial \Delta _ { \bullet } ^ { 1 }$, with $| S _ { \bullet } ^ { 1 } \wedge \cdot \cdot \cdot \wedge S _ { \bullet } ^ { 1 } | = \Delta ^ { 1 } / \partial \Delta ^ { 1 } \wedge \cdot \cdot \cdot \wedge \Delta ^ { 1 } / \partial \Delta ^ { 1 }$. This model has a natural action by $\Sigma _ { n } .$permuting the order of the n smash factors, and appears in the definition of symmetric spectra.

Definition 6.3.15. Let$X _ { \bullet }$be a simplicial set. An n-simplex$x \in X _ { n }$is said to be degenerate if$x = s _ { j } ( y )$for some$( n - 1 )$-simplex$y \in X _ { n - 1 }$and some degeneracy operator$s _ { j } \colon X _ { n - 1 } \to X _ { n }$, for$0 \leq j < n$. Otherwise, x is said to be non-degenerate. Let

$$
s X _ {n} = \bigcup_ {0 \leq j <   n} s _ {j} (X _ {n - 1}) \subseteq X _ {n}
$$

be the set of degenerate n-simplices, and let$X _ { n } ^ { \sharp } = X _ { n } \setminus s X _ { n }$be the set of non-degenerate n-simplices.

Example 6.3.16. Let$X _ { \bullet }$be the simplicial set associated to an ordered simplicial complex$( K , \leq )$. An n-simplex$x = ( v _ { 0 } \leq \cdot \cdot \cdot \leq v _ { n } )$is non-degenerate if and only if$v _ { j } \neq v _ { j + 1 }$for all$0 \leq j < n ,$, or equivalently, if$\sigma = \{ v _ { 0 } , \ldots , v _ { n } \}$ has$( n + 1 )$distinct elements, so that σ is an n-simplex in K. Conversely, any n-simplex$\sigma = \{ v _ { 0 } , \ldots , v _ { n } \}$in$K$can be totally ordered as$x = ( v _ { 0 } \leq \cdot \cdot \cdot \leq v _ { n } )$，and thus determines a non-degenerate n-simplex in$X _ { \bullet }$. We get a one-to-one correspondence

$$
K _ {n} ^ {\sharp} \cong X _ {n} ^ {\sharp}
$$

between the n-simplices of$( K , \leq )$and the non-degenerate n-simplices of$X _ { \bullet }$

We shall prove that$| X _ { \bullet } |$is a CW complex with one n-cell for each non-degenerate n-simplex in$X _ { \bullet }$. The key fact is the following Eilenberg–Zilber lemma from [18, (8.3)], see also [20, Thm. 4.2.3].

Proposition 6.3.17 (Eilenberg–Zilber). Let$X _ { \bullet }$be a simplicial set, and$x \in$ $X _ { m }$any m-simplex. There exists a surjective morphism$\rho \colon [ m ]  [ p ]$and a non-degenerate p-simplex$y \in X _ { p }$such that$x = \rho ^ { * } ( y )$. Moreover, the pair$( \rho , y )$ is uniquely determined by x.

Proof. The existence part follows easily by induction on m: If x is non-degenerate, we can let$\rho = i d _ { [ m ] }$and$y = x$. Otherwise$x = s _ { j } ( x _ { 1 } )$for some$( m - 1 )$-simplex $x _ { 1 }$. By induction on m we may assume that$x _ { 1 } = \rho _ { 1 } ^ { * } ( y )$for some surjective $\rho _ { 1 } \colon [ m - 1 ] \to [ p ]$and$y \in X _ { p }$non-degenerate. Then$\rho = \rho _ { 1 } \sigma _ { j } \colon [ m ]  [ p ]$is surjective and$x = \rho ^ { * } ( y ) = ( \rho _ { 1 } \sigma _ { j } ) ^ { * } ( y )$, as required.

Suppose that$x = \rho ^ { * } ( y ) = \tau ^ { * } ( z )$for non-degenerate simplices$y \in X _ { p } , z \in X _ { q }$ and surjective morphisms$\rho \colon [ m ]  [ p ] , \tau \colon [ m ]  [ q ]$. We must show that$y = z$ and$\rho = \tau$

![](images/page_155_image_11.jpg)

Consider any section$\mu \colon [ p ]  [ m ]$to$\rho ,$with$\rho \mu = i d$. We get

$$
y = \mu^ {*} \rho^ {*} (y) = \mu^ {*} \tau^ {*} (z) = (\tau \mu) ^ {*} (z).
$$

We can factor$\tau \mu$as a composite

$$
\tau \mu = \delta_ {i _ {r}} \dots \delta_ {i _ {1}} \sigma_ {j _ {1}} \dots \sigma_ {j _ {s}}
$$

as in Lemma 6.2.4, so that

$$
(\tau \mu) ^ {*} (z) = s _ {j _ {s}} \dots s _ {j _ {1}} d _ {i _ {1}} \dots d _ {i _ {r}} (z).
$$

Since$y = ( \tau \mu ) ^ { * } ( z )$is non-degenerate, we must have$s = 0$, so that$\tau \mu \colon [ p ]  [ q ]$ is injective. Hence$p \leq q .$. By symmetry,$q \leq p ,$so$p = q$. For$\tau \mu \colon [ p ]  [ p ]$ to be order-preserving and injective, it must be the identity, so$\tau \mu = i d$and $\mu$is also a section$\tan { \tau }$. Hence$y = ( \tau \mu ) ^ { * } ( z ) = z$, proving the uniqueness of the non-degenerate y. Two order-preserving surjections$\rho , \tau \colon [ m ]  [ p ]$have the same set of sections$\mu \colon [ p ]  [ m ]$if and only if they are equal [[Exercise!]], hence $\rho = \tau$, proving the uniqueness of the order-preserving surjection$\rho .$□

Corollary 6.3.18. The set of m-simplices of a simplicial set$X _ { \bullet }$decomposes as

$$
X _ {m} \cong \coprod_ {p \geq 0} X _ {p} ^ {\sharp} \times (\Delta_ {m} ^ {p} \setminus \partial \Delta_ {m} ^ {p}),
$$

with$x \in X _ { m }$corresponding to the unique pair$( y , \rho )$with$x = \rho ^ { * } ( y ) , \rho \colon [ m ] \to [ p ]$ surjective (and order-preserving), and$y \in X _ { p }$non-degenerate.

Definition 6.3.19. Given a simplicial set$X _ { \bullet }$, and a set$S$of simplices in$X _ { \bullet }$ let the simplicial subset of$X _ { \bullet }$generated by$S _ { ☉ }$,

$$
\langle S \rangle_ {\bullet} \subseteq X _ {\bullet},
$$

be the minimal simplicial subset of$X _ { \bullet }$that contains all the elements of$S .$It has m-simplices

$$
\langle S \rangle_ {m} = \{\alpha^ {*} (y) \in X _ {m} \mid \alpha \in \Delta ([ m ], [ n ]), y \in S _ {n} \},
$$

where$S _ { n } = S \cap X _ { n }$is the set of n-simplices in$S$

Definition 6.3.20. Let the simplicial n-skeleton$X _ { \bullet } ^ { ( n ) } \subseteq X .$be the simplicial subset generated by the set$\textstyle S = \bigcup _ { p \leq n } X _ { p }$of simplices of dimension$\leq n$in$X _ { \bullet }$ There are natural inclusions

$$
\emptyset = X _ {\bullet} ^ {(- 1)} \subseteq X _ {\bullet} ^ {(0)} \subseteq \dots \subseteq X _ {\bullet} ^ {(n - 1)} \subseteq X _ {\bullet} ^ {(n)} \subseteq \dots
$$

with$\textstyle \bigcup _ { n > 0 } X _ { \bullet } ^ { ( n ) } = X _ { \bullet }$, called the simplicial skeleton filtration of$X _ { \bullet }$

Example 6.3.21. The simplicial boundary$( n - 1 )$)-sphere$\partial \Delta _ { \bullet } ^ { n }$is the$( n - 1 )$ skeleton of the simplicial n-simplex$\Delta _ { \bullet } ^ { n }$

Lemma 6.3.22. The set of m-simplices of$X _ { \bullet } ^ { ( n ) }$decomposes as

$$
X _ {m} ^ {(n)} \cong \coprod_ {0 \leq p \leq n} X _ {p} ^ {\sharp} \times (\Delta_ {m} ^ {p} \setminus \partial \Delta_ {m} ^ {p}),
$$

with$x \in X _ { m } ^ { ( n ) }$corresponding to the unique pair$( y , \rho )$with$x = \rho ^ { * } ( y ) , \rho \colon [ m ] \to$ $[ p ]$surjective and$y \in X _ { p } ^ { \sharp }$non-degenerate in$X _ { \bullet }$, with$0 \leq p \leq n$

Proof. Every simplex in$X _ { m } ^ { ( n ) }$has the form$x = \alpha ^ { * } ( y )$with$\alpha \colon [ m ] \to [ q ] , y \in X _ { q }$ and$q \leq n .$. Factoring$\alpha = \mu \rho$with$\rho \colon [ m ]  [ p ]$surjective and$\mu \colon [ p ]  [ q ]$ injective, we have$x = \rho ^ { * } ( \mu ^ { * } ( y ) )$with$\mu ^ { \ast } ( y ) \in X _ { p } .$We can write$\mu ^ { * } ( y ) = \tau ^ { * } ( z )$ for some surjective$\tau \colon [ p ]  [ r ]$and non-degenerate$z \in X _ { r } ^ { \sharp }$, so$x = ( \tau \rho ) ^ { * } ( z )$ with$\tau \rho \colon [ m ]  [ r ]$surjective, z non-degenerate, and$r \leq p \leq q \leq n$. Hence x corresponds to an element on the right hand side.

![](images/page_157_image_1.jpg)

Conversely, every element$\rho ^ { * } ( y )$with$\rho \colon [ m ]  [ p ]$surjective,$y \in X _ { p } ^ { \sharp }$and$p \leq n$ lies in the n-skeleton of$X _ { \bullet }$, since$y$has dimension n or less.□

Lemma 6.3.23. Let$X _ { \bullet }$be a simplicial set. For each$n \geq 0$there is a pushout square

![](images/page_157_image_4.jpg)

in sSet.

Here$X _ { n } \times \partial \Delta _ { \bullet } ^ { n } \cup s X _ { n } \times \Delta _ { \bullet } ^ { n }$denotes the union of$X _ { n } \times \partial \Delta _ { \bullet } ^ { n }$and$s X _ { n } \times \Delta _ { \bullet } ^ { n }$ as simplicial subsets in$X _ { n } \times \Delta _ { \bullet } ^ { n }$, meeting in$s X _ { n } \times \partial \Delta _ { \bullet } ^ { n }$

Proof. The characteristic maps$x _ { \bullet } \colon \Delta _ { \bullet } ^ { n } \to X _ { \bullet }$for$x \in X _ { n }$combine to a simplicial map

$$
\Psi_ {\bullet} \colon X _ {n} \times \Delta_ {\bullet} ^ {n} \to X _ {\bullet} ^ {(n)}.
$$

Here$X _ { n }$can be viewed as a constant simplicial set, equal to$X _ { n }$in each simplicial degree, with all face and degeneracy maps equal to the identity. Then$X _ { n } \times \Delta _ { \bullet } ^ { n }$ is the product simplicial set, with m-simplices${ X _ { n } } \times { \Delta _ { m } ^ { n } }$. In simplicial degree m, the map$\Psi _ { \bullet }$takes$( x , \zeta ) \in X _ { n } \times \Delta _ { m } ^ { n } { \mathrm { ~ t o ~ } } \zeta ^ { * } ( x ) \in X _ { m }$. This gives a simplex in the n-skeleton$X _ { m } ^ { ( n ) }$, since$x \in X _ { n }$is a simplex of dimension$\leq n$in$X _ { \bullet }$

The simplicial map$\Psi _ { \bullet }$takes the union

$$
X _ {n} \times \partial \Delta_ {\bullet} ^ {n} \cup s X _ {n} \times \Delta_ {\bullet} ^ {n}
$$

into the$( n - 1 )$-skeleton$X _ { \bullet } ^ { ( n - 1 ) }$. For, if$\zeta \in \partial \Delta _ { m } ^ { n } \subseteq \Delta _ { m } ^ { n }$, then$\zeta \colon [ m ]  [ n ]$ factors through some$\delta _ { i } \colon [ n - 1 ] \ \to \ [ n ]$, as$\zeta = \delta _ { i } \beta _ { : }$, and$\zeta ^ { * } ( x ) = \beta ^ { * } ( \delta _ { i } ^ { * } ( x ) )$ lies in the$( n - 1 )$-skeleton of$X _ { \bullet }$, since$\delta _ { i } ^ { * } ( x ) = d _ { i } ( x )$has dimension$( n - 1 )$ Otherwise, if$x \in s X _ { n } \subseteq X _ { n } .$, then$x = s _ { j } ( y ) = \sigma _ { j } ^ { * } ( y )$for some$\sigma _ { j } \colon [ n ] \longrightarrow [ n - 1 ]$ and$\zeta ^ { * } ( x ) = \zeta ^ { * } ( \sigma _ { j } ^ { * } ( y ) ) = ( \sigma _ { j } \zeta ) ^ { * } ( y )$lies in the$( n - 1 )$)-skeleton of$X _ { \bullet }$, since y has dimension$( n - 1 )$

To check that the resulting square is a pushout, it sufices to verify this in each simplicial degree$m .$, since colimits of simplicial sets are constructed degreewise. Hence it sufices to check that the set complement

$$
X _ {n} \times \Delta_ {m} ^ {n} \setminus (X _ {n} \times \partial \Delta_ {m} ^ {n} \cup s X _ {n} \times \Delta_ {m} ^ {n}) = (X _ {n} \setminus s X _ {n}) \times (\Delta_ {m} ^ {n} \setminus \partial \Delta_ {m} ^ {n})
$$

maps bijectively under$\Psi _ { m }$to the set complement$X _ { m } ^ { ( n ) } \backslash X _ { m } ^ { ( n - 1 ) }$. By Lemma 6.3.22 the latter set decomposes as

$$
X _ {m} ^ {(n)} \setminus X _ {m} ^ {(n - 1)} \cong X _ {n} ^ {\sharp} \times (\Delta_ {m} ^ {p} \setminus \partial \Delta_ {m} ^ {p}).
$$

The function$\Psi _ { m }$takes$( x , \zeta )$on the left, with

$$
x \in X _ {n} \setminus s X _ {n} = X _ {n} ^ {\sharp}
$$

and

$$
\zeta \in \Delta_ {m} ^ {n} \setminus \partial \Delta_ {m} ^ {n},
$$

to$\zeta ^ { * } ( x )$, which corresponds to the same pair$( x , \zeta )$on the right, since ζ is surjective and x is non-degenerate.□

Lemma 6.3.24. Let$X _ { \bullet }$be a simplicial set. For$n \geq 0$there is a pushout square

$$
\begin{array}{c} X _ {n} ^ {\sharp} \times \partial \Delta_ {\bullet} ^ {n} \longrightarrow X _ {n} \times \partial \Delta_ {\bullet} ^ {n} \cup s X _ {n} \times \Delta_ {\bullet} ^ {n} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ X _ {n} ^ {\sharp} \times \Delta_ {\bullet} ^ {n} \longmapsto X _ {n} \times \Delta_ {\bullet} ^ {n} \end{array}
$$

in sSet.

Proof. The horizontal maps are induced by the inclusion$X _ { n } ^ { \sharp } \subseteq X _ { n }$. In simplicial degree m, the set complement

$$
X _ {n} ^ {\sharp} \times \Delta_ {m} ^ {n} \setminus X _ {n} ^ {\sharp} \times \partial \Delta_ {m} ^ {n} \cong X _ {n} ^ {\sharp} \times (\Delta_ {m} ^ {n} \setminus \partial \Delta_ {m} ^ {n})
$$

maps bijectively to the set complement

$$
(X _ {n} \setminus s X _ {n}) \times (\Delta_ {m} ^ {n} \setminus \partial \Delta_ {m} ^ {n}),
$$

so the square is a pushout.

We now get to the main result of this section, proved in [47, Thm. 1].

Proposition 6.3.25 (Milnor). Let$X _ { \bullet }$be a simplicial set. The topological realization$| X _ { \bullet } | ^ { ( n ) } = | X _ { \bullet } ^ { ( n ) } |$of the simplicial skeleton filtration of$X _ { \bullet }$defines the skeleton filtration

$$
\emptyset = | X _ {\bullet} ^ {(- 1)} | \subseteq | X _ {\bullet} ^ {(0)} | \subseteq \dots \subseteq | X _ {\bullet} ^ {(n - 1)} | \subseteq | X _ {\bullet} ^ {(n)} | \subseteq \dots \subseteq | X _ {\bullet} |
$$

of a$C W$structure on$| X _ { \bullet } |$. The pushout square

$$
\begin{array}{c} \coprod_ {X _ {n} ^ {\sharp}} \partial \Delta^ {n} \cong | X _ {n} ^ {\sharp} \times \partial \Delta_ {\bullet} ^ {n} | \longrightarrow | X _ {\bullet} ^ {(n - 1)} | \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \\ \coprod_ {X _ {n} ^ {\sharp}} \Delta^ {n} \cong | X _ {n} ^ {\sharp} \times \Delta_ {\bullet} ^ {n} | \xrightarrow {\Phi} | X _ {\bullet} ^ {(n)} | \end{array}
$$

in Top exhibits the n-skeleton as being obtained from the$( n - 1 )$-skeleton by attaching one n-cell for each element of$X _ { n } ^ { \sharp }$. Hence$| X _ { \bullet } |$has a canonical structure as a$C W$complex, with one n-cell for each non-degenerate n-simplex in$X _ { \bullet }$

Proof. It is clear that$| X _ { \bullet } | \cong \mathrm { c o l i m } _ { n } | X _ { \bullet } ^ { ( n ) } |$has the weak (colimit) topology, since topological realization commutes with colimits. Combining Lemmas 6.3.23 and 6.3.24, we get a pushout square

![](images/page_159_image_1.jpg)

in sSet, which gives the required pushout square in Top upon topological realization.□

Lemma 6.3.26. Each simplicial map$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$induces a cellular map $| f _ { \bullet } | \colon | X _ { \bullet } | \to | Y _ { \bullet } |$upon topological realization. Hence topological realization factors as a$( f a i t h f u l )$CW realization functor

$$
| - |: \mathrm{sSet} \longrightarrow \mathrm{CW}
$$

followed by the inclusion$\mathbf { C W } \subset \mathbf { T o p }$

Proof. The simplicial map$f _ { \bullet }$takes simplices of dimension$\leq n$in$X _ { \bullet }$to simplices of dimension$\leq n$in$Y _ { \bullet } .$hence maps the n-skeleton of$X _ { \bullet }$into the n-skeleton of $Y _ { \bullet }$. Thus$| f _ { \bullet } |$maps$| X _ { \bullet } | ^ { ( n ) }$into$| \bar { Y } _ { \bullet } | ^ { ( n ) }$, as required.□

Definition 6.3.27. A degreewise injective simplicial map$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$is called a cofibration.

Lemma 6.3.28. If$X _ { \bullet } \subseteq Y _ { \bullet }$is a simplicial subset, then$| X _ { \bullet } |$is a subcomplex $o f \mid Y _ { \bullet } \mid$. More generally, a cofibration$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$(of simplicial sets) induces an isomorphism of$| X _ { \bullet } |$with its image, as a subcomplex$o f \left| Y _ { \bullet } \right|$. In particular, $| f _ { \bullet } | \colon | X _ { \bullet } | \to | Y _ { \bullet } |$is a cofibration (of topological spaces).

Proof. If$X _ { \bullet } \subseteq Y _ { \bullet }$, then$X _ { n } ^ { \sharp } \subseteq Y _ { n } ^ { \sharp }$for each$n \geq 0 .$, since if$x = s _ { j } ( y ) \in X _ { n }$with $y \in Y _ { n - 1 }$then$s _ { j } d _ { j } ( x ) = s _ { j } d _ { j } s _ { j } ( y ) = s _ { j } ( y ) = x$with$d _ { j } ( x ) \in X _ { n - 1 }$, using the simplicial identities. Thus x is degenerate in$X _ { \bullet }$if and only if it is degenerate in $Y _ { \bullet }$. Hence$| X _ { \bullet } |$is the subcomplex of$| Y _ { \bullet } |$whose n-cells correspond to the subset $X _ { n } ^ { \sharp } \subseteq Y _ { n } ^ { \sharp }$of the n-cells of$| Y _ { \bullet } |$

A degreewise injective simplicial map$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$factors as an isomorphism of simplicial sets$X _ { \bullet } \cong f _ { \bullet } ( X _ { \bullet } )$followed by the simplicial subset inclusion $f _ { \bullet } ( X _ { \bullet } ) \subseteq Y _ { \bullet }$, hence induces an isomorphism of CW complexes$| X _ { \bullet } | \cong | f _ { \bullet } ( X _ { \bullet } ) |$ followed by the subcomplex inclusion$| f _ { \bullet } ( X _ { \bullet } ) | \subseteq | Y _ { \bullet } |$□

Definition 6.3.29. A simplicial set$X _ { \bullet }$is finite if it is generated by finitely many simplices, or equivalently, if the set of all non-degenerate simplices$X ^ { \sharp } =$ $\textstyle \bigcup _ { n \geq 0 } X _ { n } ^ { \sharp }$is finite. This is equivalent to asking that$| X _ { \bullet } |$is a finite CW complex.

Recall Whitehead’s Theorem 5.7.4 on (weak) homotopy equivalences between CW complexes.

Definition 6.3.30. A map$f _ { \bullet } : X _ { \bullet } \to Y _ { \bullet }$of simplicial sets is called a weak homotopy equivalence if the induced map of CW realizations

$$
| f _ {\bullet} |: | X _ {\bullet} | \longrightarrow | Y _ {\bullet} |
$$

is a homotopy equivalence. We then write$f _ { \bullet } : X _ { \bullet } \xrightarrow { \simeq } Y _ { \bullet }$

Lemma 6.3.31. Let$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$and$g _ { \bullet } \colon Y _ { \bullet } \to Z _ { \bullet }$be simplicial maps.$I f$two $o f$the simplicial maps$f _ { \bullet } , \ g _ { \bullet }$and$g _ { \bullet } f _ { \bullet } \colon X _ { \bullet } \to Z _ { \bullet }$are weak homotopy equivalences, then so is the third.

Proof. This follows from the two-out-of-three property for homotopy equivalences, since$| g _ { \bullet } f _ { \bullet } | = | g _ { \bullet } | | f _ { \bullet } |$□

## 6.4 The role of degenerate simplices

Recall that limits of simplicial sets are constructed degreewise, so that the product$X _ { \bullet } \times Y _ { \bullet }$of two simplicial sets has n-simplices$X _ { n } \times Y _ { n }$for all$n \geq 0 .$, and simplicial operators$\alpha ^ { * } \times \alpha ^ { * } \colon X _ { n } \times Y _ { n } \to X _ { m } \times Y _ { m }$for all α$: [ m ]  [ n ]$in$\Delta$.

In general, a left adjoint like topological realization will not commute with limits like products. However, due to the presence of degenerate simplices, topological realization does commute with finite products, as was shown by Milnor [47, Thm. 2]. We shall deduce this from the case when$X _ { \bullet }$and$Y _ { \bullet }$are simplicial simplices, using the following isomorphism.

Lemma 6.4.1. There is a natural isomorphism

$$
\coprod_ {n \geq 0} X _ {n} \times \Delta_ {\bullet} ^ {n} / \sim \xrightarrow {\cong} X _ {\bullet}
$$

where$( x , \alpha _ { \bullet } ( \zeta ) ) \sim ( \alpha ^ { * } ( x ) , \zeta )$for all α :$[ m ] \to [ n ] , x \in X _ { n }$and$\zeta \in \Delta _ { \bullet } ^ { m }$

Proof. The simplicial maps$\Psi _ { \bullet } \colon X _ { n } \times \Delta _ { \bullet } ^ { n } \to X _ { \bullet } ,$taking$( x , \zeta )$to$\zeta ^ { * } ( x )$for$n \geq 0 .$ are compatible under$\sim ,$since$\Psi _ { \bullet } ( x , \alpha _ { \bullet } ( \zeta ) ) \ : = \ : ( \alpha \zeta ) ^ { * } ( x )$and$\Psi _ { \bullet } ( \alpha ^ { * } ( x ) , \zeta ) \ =$ $\zeta ^ { * } ( \alpha ^ { * } ( x ) )$. Hence there is an induced map of simplicial sets, as displayed.

It sufices to check that this map is a bijection in each simplicial degree p. An inverse map takes$y \in X _ { p }$to the equivalence class of$( y , i d _ { [ p ] } ) \in X _ { p } \times \Delta _ { p } ^ { p }$. One composite takes y to$i d _ { [ p ] } ^ { * } ( y ) = y$. The other composite takes the equivalence class of$( x , \zeta )$, with$x \in X _ { n }$and$\zeta \colon [ p ]  [ n ]$, to the class of$( \zeta ^ { * } ( x ) , i d _ { [ p ] } )$. Now $( \zeta ^ { * } ( x ) , i d _ { [ p ] } ) \sim ( x , \zeta _ { \bullet } ( i d _ { [ p ] } ) ) = ( x , \zeta )$, so this composite is also the identity.

[[Discuss compatibility of this lemma with Definition 6.2.14.]]

Corollary 6.4.2. There is a coequalizer diagram

$$
\coprod_ {\alpha : [ m ] \to [ n ]} X _ {n} \times \Delta_ {\bullet} ^ {m} \xrightarrow [ t ]{\stackrel {{s}} {{\longrightarrow}}} \coprod_ {n \geq 0} X _ {n} \times \Delta_ {\bullet} ^ {n} \longrightarrow X _ {\bullet}
$$

in sSet, where s maps$X _ { n } \times \Delta _ { \bullet } ^ { m } \to X _ { m } \times \Delta _ { \bullet } ^ { m }$by$\alpha ^ { * } \times i d ,$, and t maps$X _ { n } \times \Delta _ { \bullet } ^ { m }$ $X _ { n } \times \Delta _ { \bullet } ^ { n }$by id$\times \alpha _ { \bullet }$

Proof. The coequalizer in sSet is computed degreewise, and equals the identification space$\textstyle \prod _ { n > 0 } X _ { n } \times \Delta _ { \bullet } ^ { n } / \sim$where ∼ identifies$s ( x , \zeta ) = ( \alpha ^ { * } ( x ) , \zeta )$with $t ( x , \zeta ) = ( x , \alpha _ { \bullet } ( \zeta ) )$, just as in the previous lemma.□

See also Lemma 7.6.4 below.

Proposition 6.4.3 (Milnor). Let$X _ { \bullet } , Y _ { \bullet }$be simplicial sets. The projections

$$
X _ {\bullet} \xleftarrow {p r _ {1}} X _ {\bullet} \times Y _ {\bullet} \xrightarrow {p r _ {2}} Y _ {\bullet}
$$

in sSet induce a natural homeomorphism

$$
\left(\left| p r _ {1} \right|, \left| p r _ {2} \right|\right) \colon \left| X _ {\bullet} \times Y _ {\bullet} \right| \xrightarrow {\cong} \left| X _ {\bullet} \right| \times \left| Y _ {\bullet} \right|,
$$

where the target is topologized as the product$o f$CW complexes.

Proof. In the special case$X _ { \bullet } = \Delta _ { \bullet } ^ { m } , Y _ { \bullet } = \Delta _ { \bullet } ^ { n }$, the projections$p r _ { 1 } \colon \Delta _ { \bullet } ^ { m } \times \Delta _ { \bullet } ^ { n }$ $\Delta _ { \bullet } ^ { m } , p r _ { 2 } \colon \Delta _ { \bullet } ^ { m } \times \Delta _ { \bullet } ^ { n }  \Delta _ { \bullet } ^ { n }$induce a homeomorphism

$$
(| p r _ {1} |, | p r _ {2} |) \colon | \Delta_ {\bullet} ^ {m} \times \Delta_ {\bullet} ^ {n} | \stackrel {\cong} {\longrightarrow} | \Delta_ {\bullet} ^ {m} | \times | \Delta_ {\bullet} ^ {n} |
$$

by Proposition 6.1.24, for each$m , n \geq 0$. In the general case,

$$
| \big (\coprod_ {m \geq 0} X _ {m} \times \Delta_ {\bullet} ^ {m} / \sim \big) \times \big (\coprod_ {n \geq 0} Y _ {n} \times \Delta_ {\bullet} ^ {n} / \sim \big) | \xrightarrow {\cong} | X _ {\bullet} \times Y _ {\bullet} |
$$

is a homeomorphism by Lemma 6.4.1 for$X _ { \bullet }$and$Y _ { \bullet }$. By naturality, its composite with$( | p r _ { 1 } | , | p r _ { 2 } | )$factors as the chain of homeomorphisms

$$
\begin{array}{l} | \big (\coprod_ {m \geq 0} X _ {m} \times \Delta_ {\bullet} ^ {m} / \sim \big) \times \big (\coprod_ {n \geq 0} Y _ {n} \times \Delta_ {\bullet} ^ {n} / \sim \big) | \\ \cong | \coprod_ {m, n \geq 0} X _ {m} \times Y _ {n} \times \Delta_ {\bullet} ^ {m} \times \Delta_ {\bullet} ^ {n} / \approx | \\ \cong \coprod_ {m, n \geq 0} X _ {m} \times Y _ {n} \times | \Delta_ {\bullet} ^ {m} \times \Delta_ {\bullet} ^ {n} | / \approx \\ \cong \coprod_ {m, n \geq 0} X _ {m} \times Y _ {n} \times | \Delta_ {\bullet} ^ {m} | \times | \Delta_ {\bullet} ^ {n} | / \approx \\ \cong | (\coprod_ {m \geq 0} X _ {m} \times \Delta_ {\bullet} ^ {m} / \sim) | \times | (\coprod_ {n \geq 0} Y _ {n} \times \Delta_ {\bullet} ^ {n} / \sim) | \\ \xrightarrow {\cong} | X _ {\bullet} | \times | Y _ {\bullet} | \end{array}
$$

by Corollary 6.2.22, the special case of simplicial simplices, and Lemma 6.4.1. Hence$( | p r _ { 1 } | , | p r _ { 2 } | )$is a homeomorphism.□

Corollary 6.4.4. CW realization$| - | \colon \mathbf { s S e t } \ \to \ \mathbf { C W }$commutes with finite products.

Proof. This is clear by induction from the previous proposition.

[[Discuss realization and equalizers or finite limits. Failure to commute with infinite products.]]

Definition 6.4.5. Let$f _ { \bullet } , g _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$be simplicial maps. A simplicial homotopy from$f _ { \bullet }$to$g _ { \bullet }$is a simplicial map

$$
H _ {\bullet} \colon X _ {\bullet} \times \Delta_ {\bullet} ^ {1} \to Y _ {\bullet}
$$

such that$H _ { \bullet } \circ \delta _ { 1 \bullet } = f _ { \bullet }$and$H _ { \bullet } \circ \delta _ { 0 \bullet } = g _ { \bullet }$. When such an$H _ { \bullet }$exists, we say that$f _ { \bullet }$and$g _ { \bullet }$are simplicially homotopic, and write$H _ { \bullet } \colon f _ { \bullet } \simeq g _ { \bullet }$

Remark 6.4.6. Existence of a simplicial homotopy is not in general an equivalence relation on simplicial maps$X _ { \bullet }  Y _ { \bullet }$. However, simplicial homotopy does of course generate an equivalence relation on the set of such simplicial maps. $[ \mathrm { I f ~ } Y _ { \bullet }$is Kan (= fibrant), then simplicial homotopy is an equivalence relation on simplicial maps to$Y _ { \bullet \cdot \rbrack \rbrack }$

Lemma 6.4.7. A simplicial homotopy$H _ { \bullet } \colon f _ { \bullet } \simeq g _ { \bullet }$of simplicial maps$X _ { \bullet }  Y _ { \bullet }$ induces a homotopy$| H _ { \bullet } | \colon | f _ { \bullet } | \simeq | g _ { \bullet } |$of maps$| X _ { \bullet } | \to | Y _ { \bullet } |$

Proof. The homotopy is given by the composite

$$
| X _ {\bullet} | \times | \Delta_ {\bullet} ^ {1} | \cong | X _ {\bullet} \times \Delta_ {\bullet} ^ {1} | \stackrel {| H _ {\bullet} |} {\longrightarrow} | Y _ {\bullet} |,
$$

where we identify$| \Delta ^ { 1 } | \cong I = [ 0 , 1 ]$so that the maps$| \delta _ { 1 \bullet } |$and$| \delta _ { 0 \bullet } |$correspond to the end-point inclusions$i _ { 0 }$and$i _ { 1 } ,$respectively.□

Lemma 6.4.8. A simplicial homotopy$H _ { \bullet } \colon f _ { \bullet } \simeq g _ { \bullet }$corresponds to a collection of functions

$$
h _ {n} ^ {k} \colon X _ {n} \longrightarrow Y _ {n}
$$

for$n \geq 0 , 0 \leq k \leq n + 1$, such that

$$
d _ {i} (h _ {n} ^ {k} (x)) = \left\{ \begin{array}{l l} h _ {n - 1} ^ {k - 1} (d _ {i} (x)) & \text { for } 0 \leq i <   k \\ h _ {n - 1} ^ {k} (d _ {i} (x)) & \text { for } k \leq i \leq n \end{array} \right.
$$

for$n \geq 1$

$$
s _ {j} (h _ {n} ^ {k} (x)) = \left\{ \begin{array}{l l} h _ {n + 1} ^ {k + 1} (s _ {j} (x)) & \text { for } 0 \leq j <   k \\ h _ {n + 1} ^ {k} (s _ {j} (x)) & \text { for } k \leq j \leq n \end{array} \right.
$$

for$n \geq 0$, and$h _ { n } ^ { n + 1 } ( x ) = f _ { n } ( x ) , h _ { n } ^ { 0 } ( x ) = g _ { n } ( x )$for all$n \geq 0$and$x \in X _ { n }$

Proof. The components of$H _ { \bullet }$are functions

$$
H _ {n} \colon X _ {n} \times \Delta_ {n} ^ {1} \longrightarrow Y _ {n}.
$$

We enumerate$\Delta _ { n } ^ { 1 } = \{ \zeta _ { 0 } ^ { n } , \ldots , \zeta _ { n + 1 } ^ { n } \}$where$\zeta _ { k } ^ { n } \colon [ n ] \to [ 1 ]$maps$\{ 0 , \ldots , k - 1 \}$to 0 and$\{ k , \ldots , n \}$to 1, see Exercise 6.3.12. Let

$$
h _ {n} ^ {k} (x) = H _ {n} (x, \zeta_ {k} ^ {n})
$$

for$x \in X _ { n } , 0 \leq k \leq n + 1$. The naturality conditions

$$
\begin{array}{l} d _ {i} (H _ {n} (x, \zeta_ {k} ^ {n})) = H _ {n - 1} (d _ {i} (x), d _ {i} (\zeta_ {k} ^ {n})) \\ s _ {j} (H _ {n} (x, \zeta_ {k} ^ {n})) = H _ {n + 1} (s _ {j} (x), s _ {j} (\zeta_ {k} ^ {n})) \end{array}
$$

then translate to the displayed relations.

[[Relate to$\mathrm { M a y ^ { \prime } s }$formulation in terms of functions$X _ { n } \to Y _ { n + 1 }$[42, Def.$5 . 1 ] . ]$ Waldhausen [68, p. 335] gives the following reformulation of the data describing a simplicial homotopy. It is often convenient for defining simplicial homotopies in a categorical context.

Definition 6.4.9. Let$\Delta / [ 1 ]$be the category of objects in ∆ over$[ 1 ]$, with objects$( [ n ] , \zeta \colon [ n ] \to [ 1 ] )$and morphisms$\alpha \colon [ m ] \to [ n ]$from$( [ m ] , \zeta \alpha ) \ \mathrm { t o } \ ( [ n ] , \zeta )$ For each simplicial set$X _ { \bullet }$, let$X ^ { * } \colon ( \Delta / [ 1 ] ) ^ { o p } \bigcup$Set be the composite functor

$$
X ^ {*} \colon (\Delta / [ 1 ]) ^ {o p} \longrightarrow \Delta^ {o p} \stackrel {X} {\longrightarrow} \mathbf {S e t}
$$

taking$( [ n ] , \zeta )$to$X _ { n }$and α to$\alpha ^ { * } \colon X _ { n } \to X _ { m }$

Lemma 6.4.10. A simplicial homotopy$H _ { \bullet } \colon X _ { \bullet } \times \Delta _ { \bullet } ^ { 1 } \to Y _ { \bullet }$, from$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$ to$g \colon X _ { \bullet } \to Y _ { \bullet }$, is equivalent to a natural transformation

$$
h \colon X ^ {*} \Longrightarrow Y ^ {*}
$$

of functors$( \Delta / [ 1 ] ) ^ { o p } \to \mathbf { S e t }$, such that$h _ { ( [ n ] , 0 ) } = f _ { n } \colon X _ { n } \to Y _ { n }$and$h _ { \left( [ n ] , 1 \right) } =$ $g _ { n } \colon X _ { n } \to Y _ { n } ~ f o r$all$n \geq 0$, where 0 and 1 denote the constant morphisms to $0 \in [ 1 ]$and$1 \in [ 1 ]$, respectively.

Proof. A simplicial homotopy$H _ { \bullet } \colon X _ { \bullet } \times \Delta _ { \bullet } ^ { 1 } \to Y _ { \bullet }$consists of functions

$$
H _ {n} \colon X _ {n} \times \Delta_ {n} ^ {1} \longrightarrow Y _ {n}
$$

for$n \geq 0$, such that

$$
\alpha^ {*} (H _ {n} (x, \zeta)) = H _ {m} (\alpha^ {*} (x), \alpha^ {*} (\zeta))
$$

for all$\alpha \colon [ m ]  [ n ] , x \in X _ { n }$and$\zeta \colon [ n ]  [ 1 ]$in$\Delta _ { n } ^ { 1 } .$. Note that$\alpha ^ { * } ( \zeta ) = \zeta \alpha$ With these notations, let$h _ { \zeta } ( x ) = H _ { n } ( x , \zeta )$. The functions$H _ { n }$correspond to functions

$$
h _ {\zeta} \colon X _ {n} \longrightarrow Y _ {n}
$$

for all$\zeta \colon [ n ]  [ 1 ]$, such that

$$
\alpha^ {*} (h _ {\zeta} (x)) = h _ {\zeta \alpha} (\alpha^ {*} (x))
$$

for all α :$( [ m ] , \zeta \alpha ) \to ( [ n ] , \zeta )$and$x \in X _ { n }$

$$
\begin{array}{c} X _ {n} \xrightarrow {h _ {\zeta}} Y _ {n} \\ \alpha^ {*} \Biggl \downarrow \\ X _ {m} \xrightarrow {h _ {\zeta \alpha}} Y _ {m} \end{array}
$$

These correspond precisely to the components$h _ { ( [ n ] , \zeta ) }$of a natural transformation$h \colon X ^ { * } \Rightarrow Y ^ { * }$of functors$( \Delta / [ 1 ] ) ^ { o p } \longrightarrow \mathbf { S e t } .$, as claimed.□

## 6.5 Bisimplicial sets

Definition 6.5.1. Let$\mathcal { D }$be any category. A simplicial object$X _ { \bullet }$in$\mathcal { D }$is a contravariant functor

$$
X \colon \Delta^ {o p} \longrightarrow \mathcal {D}.
$$

For each$n \geq 0$we write$X _ { n } = X ( [ n ] )$for the object of n-simplices, and for each morphism$\alpha \colon [ m ]  [ n ]$in ∆ we write$\alpha ^ { * } \colon X _ { n } \to X _ { m }$for the simplicial structure morphism in$\mathcal { D }$. It sufices to specify the face and degeneracy morphisms$d _ { i } \colon X _ { n } \to X _ { n - 1 }$and$s _ { j } \colon X _ { n } \to X _ { n + 1 }$, subject to the simplicial identities of Lemma 6.2.7. We may write

$$
[ n ] \longmapsto X _ {n}
$$

for such a functor.

A map$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$of simplicial objects in$\mathcal { D }$is a natural transformation

$$
f \colon X \Longrightarrow Y.
$$

It is determined by its components$f _ { n } \colon X _ { n } \to Y _ { n }$for$n \geq 0$, which are morphisms in$\mathcal { D }$such that$\alpha ^ { * } f _ { n } = f _ { m } \alpha ^ { * }$for$\alpha \colon [ m ] \to [ n ]$]. It sufices to check that$d _ { i } f _ { n } =$ $f _ { n - 1 } d _ { i }$and$s _ { j } f _ { n } = f _ { n + 1 } s _ { j }$for all i and j. We may write

$$
[ n ] \longmapsto (f _ {n} \colon X _ {n} \to Y _ {n})
$$

for such a natural transformation.

We write

$$
s \mathcal {D} = \operatorname{Fun} (\Delta^ {o p}, \mathcal {D})
$$

for the category of simplicial objects in$\mathcal { D }$

Example 6.5.2. Quoting [67, p. 163], if the objects of$\mathcal { D }$are called things, then the simplicial objects in$\mathcal { D }$are called simplicial things.

(a) A simplicial set is a simplicial object in Set.

(b) A based simplicial set is the same as a simplicial based set, i.e., a simplicial object in Set<sub>∗</sub>.

(c) A simplicial space$Y _ { \bullet }$is a simplicial object in Top, with a space$Y _ { n }$of n-simplices for each$n \geq 0$, and a map$\alpha ^ { * } \colon Y _ { n } \to Y _ { m }$for each$\alpha \colon [ m ] \to [ n ]$ in$\Delta$.

(d) A simplicial category$\mathcal { C } _ { \bullet }$is a simplicial object in Cat, with a category $\mathcal { C } _ { n }$of n-simplices for each$n \geq 0$, and a functor$\alpha ^ { * } \colon \mathcal { C } _ { n } \to \mathcal { C } _ { m }$for each morphism α in$\Delta$

Example 6.5.3. An object X of a category$\mathcal { D }$can be viewed as a constant simplicial object in$s { \mathcal { D } } _ { : }$, given by the constant functor$X \colon \Delta ^ { o p }  { \mathcal { D } }$taking each object$[ n ]$to X and each morphism α to$i d _ { X }$. [[No change in the notation?]] Given a simplicial object$Y _ { \bullet }$in${ \mathcal { D } } .$, we may view its degree zero part$Y _ { 0 }$as a constant simplicial object. There is then a unique simplicial map

$$
\rho^ {*} \colon Y _ {0} \longrightarrow Y _ {\bullet}
$$

that is the identity in degree$0 ,$called the inclusion of the zero-simplices. It is given in simplicial degree n by the simplicial operator$\rho _ { n } ^ { * } \colon Y _ { 0 } \to Y _ { n }$, where $\rho \colon [ n ]  [ 0 ]$is the unique morphism in$\Delta$. For each morphism$\alpha \colon [ m ]  [ n ]$in $\Delta$the simplicial operators$\alpha ^ { * } = i d \colon Y _ { 0 }  Y _ { 0 }$and$\alpha ^ { * } \colon Y _ { n } \to Y _ { m }$commute with $\rho ^ { * }$, in the sense that$\alpha ^ { * } \circ \rho _ { n } ^ { * } = \rho _ { m } ^ { * }$◦ id, since$\rho _ { n } \circ \alpha = \rho _ { m } \colon [ m ] \to [ 0 ]$. Hence $\rho ^ { * }$is a simplicial map. The “constant simplicial object” functor$\mathcal { D } \to s \mathcal { D }$is left adjoint to the “degree zero part” functor$s \mathcal { D }  \mathcal { D }$, with$\rho ^ { * }$as adjunction counit.

Definition 6.5.4. A bisimplicial set$X _ { \bullet , \bullet }$is a contravariant functor

$$
X \colon \Delta^ {o p} \times \Delta^ {o p} \longrightarrow \mathbf {S e t}.
$$

We write$X _ { m , n } = X ( [ m ] , [ n ] )$for the set of$( m , n )$-bisimplices, and may display X as

$$
[ m ], [ n ] \longmapsto X _ {m, n}.
$$

A map$f _ { \bullet , \bullet } \colon X _ { \bullet , \bullet } \to Y _ { \bullet , \bullet }$is a natural transformation$f \colon X \Rightarrow Y$. Its components are functions$f _ { m , n } \colon X _ { m , n } \to Y _ { m , n }$for all$m , n \geq 0$, commuting with the bisimplicial structure maps$( \alpha , \beta ) ^ { * }$for all$\alpha \colon [ p ]  [ m ]$and$\beta \colon [ q ]  [ n ]$

Lemma 6.5.5. The category ssSet of bisimplicial sets is identified with the category ssSet of simplicial objects in simplicial sets, via the isomorphism

$$
\mathbf {s s S e t} = \mathbf {F u n} (\Delta^ {o p} \times \Delta^ {o p}, \mathbf {S e t}) \cong \mathbf {F u n} (\Delta^ {o p}, \mathbf {F u n} (\Delta^ {o p}, \mathbf {S e t})) = s s \mathbf {S e t}.
$$

A bisimplicial set$X _ { \bullet , }$<sub>•</sub> then corresponds to the simplicial simplicial set

$$
[ m ] \longmapsto X _ {m, \bullet}  ,
$$

with m-simplices the simplicial set$X _ { m , \bullet } \colon [ n ] \longmapsto X _ { m , n }$having simplicial structure maps the functions$\beta ^ { * } = ( i d _ { [ m ] } , \beta ) ^ { * }$. The simplicial structure maps of $[ m ] \mapsto X _ { m } ,$are simplicial maps$\alpha _ { \bullet } ^ { * }$with n-th component$\alpha _ { n } ^ { * } = ( \alpha , i d _ { [ n ] } ) ^ { * }$

Proof. See Lemma 3.1.13.

Remark 6.5.6. In a bisimplicial set$X _ { \bullet , \bullet }$<sub>•</sub> we may refer to the first and second simplicial directions as the left hand and right hand simplicial directions, respectively. Under the identification of Lemma 6.5.5, we can think of these as external and internal simplicial directions, respectively.

Remark 6.5.7. The algebraic K-theory of a Waldhausen category will be defined as the (total) topological realization of a bisimplicial set associated to a simplicial category. We shall therefore need to be able to manipulate bisimplicial sets and certain associated simplicial spaces.

Definition 6.5.8. The degreewise topological realization of a bisimplicial set $X _ { \bullet , \bullet }$is the simplicial space

$$
[ m ] \longmapsto | X _ {m, \bullet} | = \coprod_ {n \geq 0} X _ {m, n} \times \Delta^ {n} / \sim_ {r}
$$

given by the composite functor

$$
\Delta^ {o p} \xrightarrow {X} \mathbf {s S e t} \xrightarrow {| - |} \mathbf {T o p}.
$$

Here$\sim _ { r }$refers to the identifications$( x , \beta _ { * } ( \eta ) ) \sim ( \beta ^ { * } ( x ) , \eta )$involving the right hand (= internal) simplicial structure of$X _ { \bullet , \bullet }$, for$\beta \colon [ q ] \to [ n ] , x \in X _ { m , n }$and $\eta \in \Delta ^ { q }$

Definition 6.5.9. The topological realization of a simplicial space$Z _ { \bullet }$is the identification space

$$
| Z _ {\bullet} | = \coprod_ {m \geq 0} Z _ {m} \times \Delta^ {m} / \sim
$$

where$Z _ { m } \times \Delta ^ { m }$is given the product topology,$\begin{array} { r } { \prod _ { m > 0 } Z _ { m } \times \Delta ^ { m } } \end{array}$is the coproduct, and ∼ is generated by$( z , \alpha _ { * } ( \xi ) ) \sim ( \alpha ^ { * } ( z ) , \xi )$\` <sub>for</sub>$\dot { \alpha } \colon [ p ]  [ m ] , z \in Z _ { m }$and $\xi \in \Delta ^ { p }$

For general simplicial spaces, this can be a badly behaved identification space. However, for simplicial spaces arising by degreewise topological realization of bisimplicial sets, there is no dificulty.

Definition 6.5.10. The total topological realization of a bisimplicial set$X _ { \bullet , }$• is the identification space

$$
\| X _ {\bullet , \bullet} \| = \coprod_ {m, n \geq 0} X _ {m, n} \times \Delta^ {m} \times \Delta^ {n} / \approx
$$

where$S _ { m , n } \times \Delta ^ { m } \times \Delta ^ { n }$is homeomorphic to the disjoint union of one copy of the product$\Delta ^ { m } \times \Delta ^ { n }$for each element in$X _ { m , n } ,$, and ≈ is the equivalence relation generated by

$$
(x, (\alpha , \beta) _ {*} (\xi , \eta)) \approx ((\alpha , \beta) ^ {*} (x), (\xi , \eta))
$$

for$\alpha \colon [ p ] \to [ m ] , \beta \colon [ q ] \to [ n ] , x \in X _ { m , n } , \xi \in \Delta ^ { p } , \eta \in \Delta ^ { q } .$

Lemma 6.5.11. There is a natural homeomorphism

$$
\left\| X _ {\bullet , \bullet} \right\| \cong | [ m ] \mapsto \left| X _ {m, \bullet} \right|.
$$

Proof. All terms in

$$
\begin{array}{l} | [ m ] \mapsto | X _ {m, \bullet} | | = \coprod_ {m \geq 0} | X _ {m, \bullet} | \times \Delta^ {m} / \sim \\ \qquad = \coprod_ {m \geq 0} \big (\coprod_ {n \geq 0} X _ {m, n} \times \Delta^ {n} / \sim_ {r} \big) \times \Delta^ {m} / \sim \\ \qquad \cong \coprod_ {m, n \geq 0} X _ {m, n} \times \Delta^ {m} \times \Delta^ {n} / \approx \\ \qquad = \| X _ {\bullet , \bullet} \| \end{array}
$$

are obtained from$\begin{array} { r } { \prod _ { m , n > 0 } X _ { m , n } \times \Delta ^ { m } \times \Delta ^ { n } } \end{array}$by the same identifications. [[Some explanation of the interaction of products and identification spaces might be appropriate. Alternatively, consider realization to CW instead of Top.]]

Definition 6.5.12. A map$f _ { \bullet , \bullet } \colon X _ { \bullet , \bullet } \to Y _ { \bullet , }$of bisimplicial sets is a weak homotopy equivalence if the total topological realization

$$
\| f _ {\bullet , \bullet} \|: \| X _ {\bullet , \bullet} \| \to \| Y _ {\bullet , \bullet} \|
$$

is a homotopy equivalence.

Definition 6.5.13. The simplicial realization of a bisimplicial set$X _ { \bullet , \bullet }$is the simplicial set

$$
\coprod_ {m \geq 0} X _ {m, \bullet} \times \Delta_ {\bullet} ^ {m} / \sim_ {l}
$$

where$X _ { m , \bullet } \times \Delta _ { \bullet } ^ { m }$is the product simplicial set, with n-simplices$X _ { m , n } \times \Delta _ { n } ^ { m }$，$\begin{array} { r } { \prod _ { m > 0 } X _ { m , \bullet } \times \Delta _ { \bullet } ^ { m } } \end{array}$is the coproduct of simplicial sets, and$\sim _ { l }$is the equivalence relation generated in each simplicial degree n by the relations$( x , \alpha _ { \bullet } ( \zeta ) )$∼<sub>l</sub> $( \alpha _ { \bullet } ^ { * } ( x ) , \zeta )$for$\alpha \colon [ p ] \to [ m ] , x \in X _ { m , n }$and$\zeta \in \Delta _ { n } ^ { p }$, coming from the left hand (= external) simplicial structure on$X _ { \bullet , \bullet }$

Lemma 6.5.14. The topological realization of the simplicial realization of a bisimplicial set is naturally homeomorphic with the total topological realization.

Proof.

$$
\begin{array}{r l} | \prod_ {m \geq 0} X _ {m, \bullet} \times \Delta_ {\bullet} ^ {m} / \sim_ {l} | & \cong \prod_ {m \geq 0} | X _ {m, \bullet} \times \Delta_ {\bullet} ^ {m} | / \sim \\ & \cong \prod_ {m \geq 0} | X _ {m, \bullet} | \times | \Delta_ {\bullet} ^ {m} | / \sim \\ & \cong \prod_ {m \geq 0} | X _ {m, \bullet} | \times \Delta^ {m} / \sim \\ & \cong \| X _ {\bullet , \bullet} \| \end{array}
$$

by Corollary 6.2.22, Proposition 6.4.3, Lemma 6.3.8 and Lemma 6.5.11.

Definition 6.5.15. The diagonal of a bisimplicial set$X _ { \bullet , \bullet }$is the simplicial set diag(X)<sub>•</sub>, with n-simplices

$$
\operatorname{diag} (X) _ {n} = X _ {n, n}
$$

for all$n \geq 0$, and simplicial structure maps$\alpha ^ { * } = ( \alpha , \alpha ) ^ { * } \colon \mathrm { d i a g } ( X ) _ { n } \to \mathrm { d i a g } ( X ) _ { m }$ for all$\alpha \colon [ m ] \to [ n ]$in$\Delta .$. It equals the composite functor

$$
\Delta^ {o p} \xrightarrow {\Delta} \Delta^ {o p} \times \Delta^ {o p} \xrightarrow {X} \mathbf {S e t},
$$

where ∆ denotes the diagonal functor. Any map$f _ { \bullet , \bullet } \colon X _ { \bullet , \bullet } \to Y _ { \bullet , \bullet }$of bisimplicial sets induces a map diag($f ) _ { \bullet } \colon \mathrm { d i a g } ( X ) _ { \bullet } \to \mathrm { d i a g } ( Y )$of diagonal simplicial sets, and

$$
\operatorname{diag}: \mathbf {s s S e t} \rightarrow \mathbf {s S e t}
$$

is a functor.

Proposition 6.5.16. The diagonal of a bisimplicial set is naturally isomorphic to the simplicial realization:

$$
\operatorname{diag} (X) _ {\bullet} \cong \coprod_ {m \geq 0} X _ {m, \bullet} \times \Delta_ {\bullet} ^ {m} / \sim_ {l}
$$

Hence there is a natural homeomorphism

$$
| \operatorname{diag} (X) _ {\bullet} | \cong \| X _ {\bullet , \bullet} \|.
$$

Proof. For each$m \geq 0$there is a simplicial map

$$
\Psi_ {\bullet} \colon X _ {m, \bullet} \times \Delta_ {\bullet} ^ {m} \longrightarrow \operatorname{diag} (X) _ {\bullet}
$$

given in simplicial degree n by

$$
(x, \zeta) \mapsto \zeta_ {n} ^ {*} (x) = (\zeta , i d _ {[ n ]}) ^ {*} (x),
$$

for$x \in X _ { m , n } , \zeta \in \Delta _ { n } ^ { m }$. This is a simplicial map, since for$\beta \colon [ q ]  [ n ]$

$$
\beta^ {*} (x, \zeta) = (\beta^ {*} (x), \beta^ {*} (\zeta)) = ((i d _ {[ m ]}, \beta) ^ {*} (x), \zeta \beta)
$$

maps to

$$
(\zeta \beta , i d _ {[ n ]}) ^ {*} ((i d _ {[ m ]}, \beta) ^ {*} (x)) = (\beta , \beta) ^ {*} (\zeta , i d _ {[ n ]}) ^ {*} (x) = (\beta , \beta) ^ {*} (\zeta_ {n} ^ {*} (x)).
$$

The maps$\Psi _ { \bullet }$are compatible under the relation$\sim \iota ,$since for$\alpha \colon [ p ]  [ m ]$2 $x \in X _ { m , n }$and$\zeta \in \Delta _ { p } ^ { n }$the class$( x , \alpha _ { \bullet } ( \zeta ) ) = ( x , \alpha \zeta )$maps to$( \alpha \zeta ) _ { n } ^ { * } ( x )$, while the class$( \alpha _ { n } ^ { * } ( x ) , \zeta )$maps to$\zeta _ { n } ^ { * } ( \alpha _ { n } ^ { * } ( x ) )$, and these values are equal. Hence there is a well-defined simplicial map

$$
\coprod_ {m \geq 0} X _ {m, \bullet} \times \Delta_ {\bullet} ^ {m} / \sim_ {l} \longrightarrow \operatorname{diag} (X) _ {\bullet}.
$$

There is also a simplicial map the other way, taking$x \in$diag$X ) _ { n } = X _ { n , n }$to the equivalence class of the n-simplex$( x , i d _ { [ n ] } )$in$X _ { n , \bullet } \times \Delta _ { \bullet } ^ { n }$This is simplicial, since for$\beta \colon [ q ] \ \to \ [ n ]$the q-simplex$( \beta , \beta ) ^ { * } ( x )$in diag$( X ) _ { q } ~ = ~ X _ { q , q }$ maps to$( ( \beta , \beta ) ^ { * } ( x ) , i d _ { [ q ] } )$, while$\beta ^ { * } ( x , i d _ { [ n ] } ) = ( ( i d _ { [ n ] } , \beta ) ^ { * } ( x ) , \beta )$is equivalent to$\beta _ { q } ^ { * } ( ( i d _ { [ n ] } , \beta ) ^ { * } ( x ) , i d _ { [ q ] } ) = ( ( \beta , \beta ) ^ { * } ( x ) , i \dot { d _ { [ q ] } } )$

The composite self-map of diag(X)<sub>•</sub> takes$x \in X _ { n , n }$to$i d _ { [ n ] } ^ { * } ( x ) = x$, hence equals the identity.

The other composite takes the class of$( x , \zeta )$to the class of$( \zeta _ { n } ^ { * } ( x ) , i d _ { [ n ] } )$ which under$\sim _ { l }$is identified with$( x , \zeta _ { n } )$, so also this composite is the identity.

The natural homeomorphism is now obtained by passing to topological realization, and using Lemma 6.5.14.□

Remark 6.5.17. This proposition may seem surprising, since it exhibits a homeomorphism between the diferent-looking identification spaces

$$
\coprod_ {p \geq 0} X _ {p, p} \times \Delta^ {p} / \sim
$$

and

$$
\coprod_ {m, n \geq 0} X _ {m, n} \times \Delta^ {m} \times \Delta^ {n} / \approx .
$$

It provides a key simplifying tool in the theory of bisimplicial sets, since for the purposes of homotopy theory, the topological realization of$X _ { \bullet , \bullet }$is the same as that of the diagonal simplicial set diag(X)<sub>•</sub>. The additional simplicial direction does therefore not contribute essentially to the form of the topological realization. More generally, for multi-simplicial sets given by contravariant functors

$$
X \colon \Delta^ {o p} \times \dots \times \Delta^ {o p} \to \mathbf {S e t},
$$

the total topological realization is naturally homeomorphic to the topological realization of the diagonal simplicial set$X \circ \Delta$, where

$$
\Delta \colon \Delta^ {o p} \to \Delta^ {o p} \times \dots \times \Delta^ {o p}
$$

is the diagonal functor.

Corollary 6.5.18. A map$f _ { \bullet , \bullet } \colon X _ { \bullet , \bullet } \to Y _ { \bullet , }$<sub>•</sub> of bisimplicial sets is a weak homotopy equivalence if and only if the diagonal map dia$\operatorname { g } ( f ) \bullet : \operatorname { d i a g } ( X ) \bullet \to$ diag(Y) of simplicial sets is a weak homotopy equivalence.

Proof. This is clear from the commutative square

![](images/page_169_image_1.jpg)

expressing naturality in Proposition 6.5.16.

[[External product of simplicial sets,$( X _ { \bullet } \boxtimes Y _ { \bullet } ) \colon [ m ] , [ n ] \mapsto X _ { m } \times Y _ { n } . ] ]$

[[Isomorphism of bisimplicial sets$\begin{array} { r } { X _ { \bullet , \bullet } \cong \coprod _ { m , n > 0 } X _ { m , n } \times \Delta _ { \bullet } ^ { m } \boxtimes \Delta _ { \bullet } ^ { n } / \approx . ] \} } \end{array}$

[[May interchange left and right, and consider$[ \bar { n } ] \mapsto X _ { \bullet , n } , \mathrm { e t c . } ] ]$

## 6.6 The realization lemma

The following useful result is stated in [67, Lem. 5.1].

Proposition 6.6.1 (Realization lemma). Let$f _ { \bullet , \bullet } \colon X _ { \bullet , \bullet } \longrightarrow Y _ { \bullet } \quad$<sub>,•</sub> be a map of bisimplicial sets, such that for each$m \geq 0$the map

$$
f _ {m, \bullet} \colon X _ {m, \bullet} \longrightarrow Y _ {m, \bullet}
$$

of simplicial sets is a weak homotopy equivalence. Then$f _ { \bullet , \bullet }$<sub>•</sub> is a weak homotopy equivalence.

The naming of this result is perhaps clearer from the following restatement.

Corollary 6.6.2. Let$f _ { \bullet , \bullet } \colon X _ { \bullet , \bullet } \longrightarrow Y _ { \bullet , \bullet }$be a map of bisimplicial sets, and let $Z _ { m } = | X _ { m , \bullet } | , W _ { m } = | Y _ { m , \bullet } | \ a n d \ g _ { m } = | f _ { m , \bullet } |$, so that$g _ { \bullet } \colon Z _ { \bullet } \to W .$<sub>•</sub> is a map of simplicial spaces. If

$$
g _ {m} \colon Z _ {m} \xrightarrow {\simeq} W _ {m}
$$

is a homotopy equivalence for each$m \geq 0 ,$, then the induced map of topological realizations

$$
| g _ {\bullet} |: | Z _ {\bullet} | \xrightarrow {\simeq} | W _ {\bullet} |
$$

is a homotopy equivalence.

Proof. This is clear by the realization lemma and Lemma 6.5.11.

[[More general statement, cite Segal [60].]]

Remark 6.6.3. The roles of the left and right simplicial directions may of course be interchanged: If$f _ { \bullet , n }$is a weak homotopy equivalence for each$n \geq 0 .$ then$f _ { \bullet , \bullet }$is a homotopy equivalence.

As a first step towards proving the realization lemma, we analyze the simplicial subsets of degenerate simplices. We follow the notation of [22, ??].

Definition 6.6.4. Let$k \geq 0$. For each$0 \le j < k$let$s _ { j } ( X _ { k - 1 , \bullet } ) \subseteq X _ { k , \bullet }$be the simplicial subset given by the image of$s _ { j , \bullet } = ( \sigma _ { j } , i d ) ^ { * } \colon X _ { k - 1 , \bullet } \to X _ { k , \bullet }$. For each$- 1 \leq \ell < k$let

$$
s _ {[ \ell ]} X _ {k, \bullet} = \bigcup_ {0 \leq j \leq \ell} s _ {j} (X _ {k - 1, \bullet}),
$$

and let

$$
s X _ {k, \bullet} = s _ {[ k - 1 ]} X _ {k, \bullet} = \bigcup_ {0 \leq j <   k} s _ {j} (X _ {k - 1, \bullet})
$$

be the simplicial subset of degenerate k-simplices.

Lemma 6.6.5. For each$0 \leq \ell <$< k there is a pushout square

$$
\begin{array}{c} s _ {[ \ell - 1 ]} X _ {k - 1, \bullet} \xrightarrow {} s _ {[ \ell - 1 ]} X _ {k, \bullet} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ X _ {k - 1, \bullet} \xrightarrow {s _ {\ell , \bullet}} s _ {[ \ell ]} X _ {k, \bullet} \end{array}
$$

in sSet.

Proof. Since$s _ { [ \ell ] } X _ { k , \ell }$is defined as the union of$s _ { [ \ell - 1 ] } X _ { k } ,$and the image of$s \ell$ on$X _ { k - 1 , \bullet }$, it sufices to show that$s _ { [ \ell - 1 ] } X _ { k - 1 , \bullet }$is the preimage of$s _ { [ \ell - 1 ] } X _ { k , \bullet }$ under$s _ { \ell } .$Suppose that$y \in X _ { k - 1 } .$<sub>,•</sub> satisfies$s _ { \ell } ( y ) = s _ { j } ( z )$for some$0 \leq \dot { j } < \ell$ and$z \in X _ { k - 1 , \bullet } .$. Then by the simplicial identities,

$$
y = d _ {\ell + 1} (s _ {\ell} (y)) = d _ {\ell + 1} (s _ {j} (z)) = s _ {j} (d _ {\ell} (z)),
$$

so$y \in s _ { [ \ell - 1 ] } X _ { k - 1 , \bullet } .$. Conversely, suppose that$y = s _ { j } ( w )$for some$0 \leq j < \ell$and w$\prime \in X _ { k - 2 , \bullet }$. Then, by another case of the simplicial identities,

$$
s _ {\ell} (y) = s _ {\ell} (s _ {j} (w)) = s _ {j} (s _ {\ell - 1} (w))
$$

and$s _ { \ell } ( y ) \in s _ { [ \ell - 1 ] } X _ { k , \bullet }$

Corollary 6.6.6. Let$f _ { \bullet , \bullet } \colon X _ { \bullet , \bullet } \longrightarrow Y _ { \bullet , }$<sub>•</sub> be such that

$$
f _ {m, \bullet} \colon X _ {m, \bullet} \longrightarrow Y _ {m, \bullet}
$$

is a weak homotopy equivalence for each$m \geq 0$. Then the restricted map

$$
s f _ {k, \bullet} \colon s X _ {k, \bullet} \longrightarrow s Y _ {k, \bullet}
$$

is a weak homotopy equivalence for each$k \geq 0$

Proof. We prove by induction on$k \geq 0$and$- 1 \leq \ell < k$that$s _ { [ \ell ] } f _ { k , \bullet } \colon s _ { [ \ell ] } X _ { k , \bullet } \longrightarrow$ $s _ { [ \ell ] } Y _ { k , \bullet }$is a weak homotopy equivalence. This is clear for$\ell = - 1$. For$0 \leq \ell <$k it follows by the gluing lemma, Lemma 6.6.5, and the inductive hypothesis.

Definition 6.6.7. For each$k \geq - 1$, let the external k-skeleton

$$
X _ {\bullet , \bullet} ^ {(k)} \subseteq X _ {\bullet , \bullet}
$$

be the bisimplicial subset generated by the$( m , q )$-bisimplices with$m \leq k$. It is the image of the canonical map

$$
\coprod_ {m \leq k} X _ {m, \bullet} \times \Delta_ {\bullet} ^ {m} \longrightarrow X _ {\bullet , \bullet}.
$$

Then$X _ { \bullet , q } ^ { ( k ) }$is the simplicial k-skeleton of$X _ { \bullet , q }$for each$q \geq 0$. Let diag$\ u _ { \ u { \colon } } ( X ^ { ( k ) } ) _ { \bullet } \subseteq$ diag$( X )$<sub>•</sub> be the diagonal simplicial set, with q-simplices diag$( X ^ { ( k ) } ) _ { q } = X _ { q , q } ^ { ( k ) } \subseteq$ $X _ { q , q }$

Proof of the realization lemma. We shall prove by induction that the restricted map

$$
\operatorname{diag} \left(f ^ {(k)}\right) _ {\bullet}: \operatorname{diag} \left(X ^ {(k)}\right) _ {\bullet} \longrightarrow \operatorname{diag} \left(Y ^ {(k)}\right) _ {\bullet}
$$

is a weak homotopy equivalence, for each k$\geq - 1$. This is clear for$k = - 1$，since all (−1)-skeleta are empty. Applying topological realization, and using Lemma 5.5.7 to pass to the colimit as$k  \infty .$, it then follows that

$$
| \operatorname{diag} (f) _ {\bullet} |: | \operatorname{diag} (X) _ {\bullet} | \longrightarrow | \operatorname{diag} (Y) _ {\bullet} |
$$

is a homotopy equivalence, which by Corollary 6.5.18 is what we need to prove.

By Lemma 6.3.23 applied to the simplicial set$X _ { \bullet , q }$there is a pushout square

$$
\begin{array}{c} X _ {k, q} \times \partial \Delta_ {\bullet} ^ {k} \cup s X _ {k, q} \times \Delta_ {\bullet} ^ {k} \longrightarrow X _ {\bullet , q} ^ {(k - 1)} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ X _ {k, q} \times \Delta_ {\bullet} ^ {k} \xrightarrow {} X _ {\bullet , q} ^ {(k)} \end{array}
$$

in sSet for each$q \geq 0$, hence also a pushout square

$$
\begin{array}{c} X _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \cup s X _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \longrightarrow \mathrm{diag} (X ^ {(k - 1)}) _ {\bullet} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ X _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \longrightarrow \mathrm{diag} (X ^ {(k)}) _ {\bullet} \end{array}\tag{6.2}
$$

in sSet. The vertical maps are inclusions, hence cofibrations.

By assumption, each map$X _ { m , \bullet } \to Y _ { m , \bullet }$is a weak homotopy equivalence, so by Corollary 6.6.6, each restricted map$s X _ { k , \bullet } \to s Y _ { k , \bullet }$is a weak homotopy equivalence. It follows, from the commutation of products with topological realization, that the four maps

$$
\begin{array}{c} X _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \longrightarrow Y _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \\ X _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \longrightarrow Y _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \\ s X _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \longrightarrow s Y _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \\ s X _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \longrightarrow s Y _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \end{array}
$$

are weak homotopy equivalences. By the gluing lemma applied to the pushout square

$$
\begin{array}{c} s X _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \xrightarrow {} s X _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ X _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \xrightarrow {} X _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \cup s X _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \end{array}
$$

the union map

$$
X _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \cup s X _ {k, \bullet} \times \Delta_ {\bullet} ^ {k} \longrightarrow Y _ {k, \bullet} \times \partial \Delta_ {\bullet} ^ {k} \cup s Y _ {k, \bullet} \times \Delta_ {\bullet} ^ {k}
$$

is a weak homotopy equivalence.

By another application of the gluing lemma, using the pushout square (6.2) and the inductive hypothesis that di$\arg \big ( f ^ { ( k - 1 ) } \big )$<sub>•</sub> is a weak homotopy equivalence, it follows that$\mathrm { d i a g } ( \bar { f } ^ { ( k ) } )$) is a weak homotopy equivalence. This completes the inductive proof.□

Example 6.6.8. Let$Y _ { \bullet , \bullet }$be a bisimplicial set, such that each degeneracy map

$$
\rho_ {m} ^ {*} \colon Y _ {0, \bullet} \longrightarrow Y _ {m, \bullet}
$$

is a weak homotopy equivalence. Then the inclusion of zero-simplices (see Example 6.5.3)

$$
\rho^ {*} \colon Y _ {0, \bullet} \longrightarrow Y _ {\bullet , \bullet}
$$

is a weak homotopy equivalence, by the realization lemma.

## 6.7 Subdivision

[[Segal’s edgewise subdivision.]]

[[The B¨okstedt–Hsiang–Madsen edgewise subdivision.]] [[Barycentric subdivision and Kan normal subdivision.]]

## 6.8 Realization of fibrations

The following is a special case of the Bousfield–Friedlander fibration theorem [8, B.4]. We outline Waldhausen’s argument [67, 5.2], which in turn extends a one-line proof of a special case due to Dieter Puppe.

Definition 6.8.1. A diagram$V  X  Y$of topological spaces is a fibration up to homotopy if the composite map$V  Y$is constant [[to a point$z _ { 0 } \in Y ] ]$ and if the induced map from V to the homotopy fiber of$X  Y \ [ [ \mathrm { a t } \ z _ { 0 } ] ]$is a homotopy equivalence.

A diagram of simplicial sets$V _ { \bullet }  X _ { \bullet }  Y _ { \bullet }$is a fibration up to homotopy if the diagram$\vert V _ { \bullet } \vert  \vert X _ { \bullet } \vert  \vert Y _ { \bullet } \vert$obtained by topological realization has this property, and similarly for multi-simplicial sets, categories, etc.

Proposition 6.8.2. Let$V _ { \bullet , \bullet } \to X _ { \bullet , \bullet } \to Y _ { \bullet , \bullet }$be a diagram of bisimplicial sets such that$V _ { \bullet , \bullet } \to Y _ { \bullet , \bullet }$is constant. Suppose that

$$
V _ {m, \bullet} \longrightarrow X _ {m, \bullet} \longrightarrow Y _ {m, \bullet}
$$

is a fibration up to homotopy, for each$m \geq 0$. Suppose furthermore that$Y _ { m , \astrosun }$ is connected, for each$m \geq 0$. Then

$$
V _ {\bullet , \bullet} \longrightarrow X _ {\bullet , \bullet} \longrightarrow Y _ {\bullet , \bullet}
$$

is a fibration up to homotopy.

Proof. Consider first the special case when there is a bisimplicial group$G _ { \bullet , \bullet }$ that acts from the right on a bisimplicial set$W _ { \bullet , \bullet } ,$and the diagram has the form

$$
W _ {m, \bullet} \longrightarrow W _ {m, \bullet} \times_ {G _ {m, \bullet}} E _ {\bullet} G _ {m, \bullet} \longrightarrow B _ {\bullet} G _ {m, \bullet},
$$

(balanced product over$G _ { m , \bullet } )$compatibly for each$m \geq 0$. [[Reference for bar constructions. Implicitly pass to diagonal in$B _ { \bullet } G _ { m , \bullet \cdot ] ] }$The topological realization can then be written as

$$
W \longrightarrow W \times_ {G} E G \longrightarrow B G
$$

where$G = \| G _ { \bullet , \bullet } \|$is a (cofibrantly based) topological group acting on the right on the space$W = \left\| W _ { \bullet , \bullet } \right\|$. This is the fiber bundle associated to the principal G-bundle$G  E G  B G$, see [63] and also [41, 1.5]. In particular it is a homotopy fiber sequence, since the base is numerable [[Reference]].

To handle the general case, we will the Kan loop group functor, which to each connected pointed simplicial set$Z _ { \bullet }$associates a (degreewise free) simplicial group$G ( Z _ { \bullet } )$, such that$| G ( Z _ { \bullet } ) | \simeq \Omega | Z _ { \bullet } |$. More precisely, there is a principal $G ( Z _ { \bullet } ) \ – \mathrm { b u n d l e }$

$$
\tilde {\Gamma} Z _ {\bullet} \longrightarrow \Gamma Z _ {\bullet}
$$

with$\tilde { \Gamma } Z _ { \bullet }$weakly contractible, and a pointed weak equivalence$z _ { \bullet } \ { \stackrel { \simeq } { \longrightarrow } } \ \Gamma Z _ { \bullet }$ all of which depend functorially on$Z _ { \bullet }$. See Kan’s original article [32] and Waldhausen’s remake [69]. [[Discuss preferred base points in$\tilde { \Gamma } Z _ { \bullet }$and$\Gamma Z _ { \bullet \cdot \mathrm { J } } ]$

For each$m \geq 0 .$, form the Kan loop group$G _ { m , \bullet } = G ( Y _ { m , \bullet } )$and the principal $G _ { m , \bullet }$-bundle$\tilde { \Gamma } Y _ { m , \bullet }  \Gamma Y _ { m , \bullet }$. Let

$$
W _ {m, \bullet} = X _ {m, \bullet} \times_ {\Gamma Y _ {m, \bullet}} \tilde {\Gamma} Y _ {m, \bullet}
$$

denote the pullback along the composite map$X _ { m , \bullet } \to Y _ { m , \bullet } \to \Gamma Y _ { m , \bullet }$. Here the subscript indicates the pullback with respect to the maps to$\Gamma Y _ { m , \bullet }$. We get a commutative diagram

![](images/page_173_chart_7.jpg)

The middle row is a fibration up to homotopy since$Y _ { m , \bullet } \xrightarrow { \simeq } \Gamma Y _ { m , \bullet }$is a weak homotopy equivalence, so that the homotopy fibers of$| X _ { m , \bullet } | \to | Y _ { m , \bullet } |$and $| X _ { m , \bullet } |  | \Gamma Y _ { m , \bullet } |$are homotopy equivalent.

The free right$G _ { m , \bullet }$-action on$\tilde { \Gamma } Y _ { m , \bullet }$pulls back to a free action on$W _ { m , \bullet } ,$, and the map labeled$\tilde { f }$is equivariant. Applying the Borel construction$( - ) \times _ { G _ { m , } }$ $E _ { \bullet } G _ { m , \bullet }$(where the subscript now denotes the balanced product with respect to the$G _ { m , \bullet ^ { - } \mathrm { a c t i o n s } } )$, we get the upper part of the following commutative diagram.

![](images/page_173_chart_10.jpg)

The right hand vertical map is induced by the collapse map$\tilde { \Gamma } Y _ { m , \bullet }  \ast$, and the lower row is the fiber bundle associated to the$G _ { m , \bullet ^ { - } \mathrm { a c t i o n } }$on$W _ { m , \bullet }$

The maps in the middle and right hand columns are weak equivalences, since$W _ { m , \bullet } \to X _ { m , \bullet } , \tilde { \Gamma } Y _ { m , \bullet } \to \Gamma Y _ { m , }$<sub>•</sub> and$E _ { \bullet } G _ { m , \bullet } \to B _ { \bullet } G _ { m , }$<sub>•</sub> are principal $G _ { m , \bullet ^ { - } } \mathrm { b u n d l e s } .$, and$E _ { \bullet } G _ { m , \bullet }$<sub>•</sub> and$\tilde { \Gamma } Y _ { m , \bullet }$are contractible.

It follows that the middle row is a fibration up to homotopy. By comparing the long exact sequences in homotopy for the middle and lower rows, and using the five-lemma, it follows that the left hand vertical map$V _ { m , \bullet } \to W _ { m , \bullet }$is a weak homotopy equivalence.

By functoriality of the Kan loop group construction, we now have a diagram of bisimplicial sets

![](images/page_174_image_3.jpg)

where all vertical maps are weak equivalences, by the the discussion above for each$m \geq 0$and the realization lemma, and all horizontal composites are constant. By the first special case, the lower row is a fibration up to homotopy. It follows that also the upper row is a fibration up to homotopy, as desired.

Chapter 7

# Homotopy theory of categories

We now turn to the first chapter of Quillen’s paper [55], on the classifying space of a small category.

## 7.1 Nerves and classifying spaces

Recall from Definition 2.9.4 that we view the totally ordered set

$$
[ n ] = \{0 <   1 <   \dots <   n \}
$$

as a small category.

Definition 7.1.1. The nerve of a small category$\mathcal { C }$is the simplicial set$N _ { \bullet } \mathcal { C }$ with n-simplices

$$
N _ {n} \mathcal {C} = \mathbf {C a t} ([ n ], \mathcal {C})
$$

for$n \geq 0$, and structure maps

$$
\alpha^ {*} = \mathbf {C a t} (\alpha , \mathcal {C}) \colon N _ {n} \mathcal {C} = \mathbf {C a t} ([ n ], \mathcal {C}) \longrightarrow \mathbf {C a t} ([ m ], \mathcal {C}) = N _ {m} \mathcal {C}
$$

for each morphism$\alpha \colon [ m ] \to [ n ]$in$\Delta$. Here$\alpha ^ { * }$takes an n-simplex$x \colon [ n ] \to \mathcal { C }$ to the composite

$$
\alpha^ {*} (x) = x \circ \alpha \colon [ m ] \longrightarrow \mathscr {C}.
$$

In other words,$N _ { n } \mathcal { C }$is the set of all diagrams

$$
X _ {0} \xrightarrow {f _ {1}} X _ {1} \xrightarrow {f _ {2}} \dots \xrightarrow {f _ {n}} X _ {n}
$$

of n composable morphisms in$\mathcal { C }$. The i-th face operator$d _ { i } \colon N _ { n } \mathcal { C } \to N _ { n - 1 } \mathcal { C }$ for$0 \leq i \leq n \geq 1$, takes the n-simplex above to the$( n - 1 )$)-simplex

$$
X _ {1} \xrightarrow {f _ {2}} \ldots \xrightarrow {f _ {n}} X _ {n}
$$

for$i = 0 ,$

$$
X _ {0} \stackrel {f _ {1}} {\longrightarrow} \dots \stackrel {f _ {i - 1}} {\longrightarrow} X _ {i - 1} \stackrel {f _ {i + 1} f _ {i}} {\longrightarrow} X _ {i + 1} \stackrel {f _ {i + 2}} {\longrightarrow} \dots \stackrel {f _ {n}} {\longrightarrow} X _ {n}
$$

for$0 < i < n ,$and

$$
X _ {0} \xrightarrow {f _ {1}} \dots \xrightarrow {f _ {n - 1}} X _ {n - 1}
$$

for$i = n$. The j-th degeneracy operator$s _ { j } \colon X _ { n } \to X _ { n + 1 }$, for$0 \leq j \leq n$, takes the n-simplex above to the$( n + 1 )$)-simplex

$$
X _ {0} \xrightarrow {f _ {1}} \dots \xrightarrow {f _ {j}} X _ {j} \xrightarrow {i d _ {X _ {j}}} X _ {j} \xrightarrow {f _ {j + 1}} \dots \xrightarrow {f _ {n}} X _ {n}.
$$

Definition 7.1.2. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be a functor between small categories. The induced map of nerves

$$
N _ {\bullet} F \colon N _ {\bullet} \mathcal {C} \longrightarrow N _ {\bullet} \mathcal {D}
$$

is the map of simplicial sets given in degree n by the function

$$
N _ {n} F = \mathbf {C a t} ([ n ], F) \colon N _ {n} \mathscr {C} = \mathbf {C a t} ([ n ], \mathscr {C}) \longrightarrow \mathbf {C a t} ([ n ], \mathscr {D}) = N _ {n} \mathscr {D}.
$$

Here$N _ { n } F$takes an n-simplex x:$[ n ] \to \mathcal { C }$to the composite

$$
(N _ {n} F) (x) = F \circ x \colon [ n ] \longrightarrow \mathcal {D}.
$$

In other words, this is the function taking the diagram

$$
X _ {0} \xrightarrow {f _ {1}} X _ {1} \xrightarrow {f _ {2}} \dots \xrightarrow {f _ {n}} X _ {n}
$$

of n composable morphisms in$\mathcal { C }$to the diagram

$$
F (X _ {0}) \stackrel {{F (f _ {1})}} {{\longrightarrow}} F (X _ {1}) \stackrel {{F (f _ {2})}} {{\longrightarrow}} \dots \stackrel {{F (f _ {n})}} {{\longrightarrow}} F (X _ {n})
$$

of n composable morphisms in$\mathcal { D }$.

Example 7.1.3.$N _ { \bullet } [ n ] = \Delta _ { \bullet } ^ { n }$for all$n \geq 0$, and$N _ { \bullet } \alpha = \alpha _ { \bullet }$for all α in$\Delta .$. In particular,$N _ { \bullet } [ 1 ] = \Delta _ { \bullet } ^ { 1 }$, where [1] is the category$\{ 0 < 1 \}$

Definition 7.1.4. We will use the bar notation$[ f _ { n } | \ldots | f _ { 1 } ] X _ { 0 }$for the n-simplex

$$
X _ {0} \xrightarrow {f _ {1}} \dots \xrightarrow {f _ {n}} X _ {n}
$$

in$N _ { \bullet } \mathcal { C }$. Then

$$
d _ {i} ([ f _ {n} | \ldots | f _ {1} ] X _ {0}) = \left\{ \begin{array}{l l} [ f _ {n} | \ldots | f _ {2} ] X _ {1} & \text { for } i = 0, \\ [ f _ {n} | \ldots | f _ {i + 1} f _ {i} | \ldots | f _ {1} ] X _ {0} & \text { for } 0 <   i <   n, \\ [ f _ {n - 1} | \ldots | f _ {1} ] X _ {0} & \text { for } i = n, \end{array} \right.
$$

and

$$
s _ {j} ([ f _ {n} | \ldots | f _ {1} ] X _ {0}) = [ f _ {n} | \ldots | i d _ {X _ {j}} | \ldots | f _ {1} ] X _ {0}
$$

for$0 \leq j \leq n$, while

$$
(N _ {n} F) ([ f _ {n} | \dots | f _ {1} ] X _ {0}) = [ F (f _ {n}) | \dots | F (f _ {1}) ] F (X _ {0})
$$

for$n \geq 0$

Definition 7.1.5. For$0 \leq i \leq n ,$, let the i-th vertex morphism$\epsilon _ { i } \colon [ 0 ]  [ n ]$in $\Delta$be given by$\epsilon _ { i } ( 0 ) = i$. For$1 \leq i \leq n$let the i-th edge morphism$\eta _ { i } \colon [ 1 ] \to [ n ]$ in$\Delta$be given by$\eta _ { i } ( 0 ) = i - 1$and$\eta _ { i } ( 1 ) = i$. In the nerve$N _ { \bullet } \mathcal { C }$of a category we can recover the objects and morphisms in a diagram

$$
X _ {0} \xrightarrow {f _ {1}} \dots \xrightarrow {f _ {n}} X _ {n}
$$

corresponding to an n-simplex$\sigma = [ f _ { n } | \ldots | f _ { 1 } ] X _ { 0 }$by the formulas$X _ { i } = \epsilon _ { i } ^ { * } ( \sigma )$ for$0 \leq i \leq n$and$f _ { i } = \eta _ { i } ^ { * } ( { \boldsymbol \sigma } )$for$1 \leq i \leq n$

Lemma 7.1.6. The rules$\mathcal { C } \mapsto N _ { \bullet } \mathcal { C }$and$F \mapsto N _ { \bullet } F$define a full and faithful functor

$$
N _ {\bullet}: \mathbf {C a t} \longrightarrow \mathbf {s S e t}.
$$

Proof. Functoriality is clear. Given small categories$\mathcal { C }$and${ \mathcal { D } } .$, we must prove that

$$
N _ {\bullet}: \operatorname{Cat} (\mathcal {C}, \mathscr {D}) \longrightarrow \mathrm{sSet} (N _ {\bullet} \mathcal {C}, N _ {\bullet} \mathscr {D})
$$

is bijective.

Suppose given a simplicial map$h _ { \bullet } \colon N _ { \bullet } \mathcal { C } \to N _ { \bullet } \mathcal { D }$For each X in$\operatorname { o b j } ( \mathcal { C } ) =$ $N _ { 0 } \mathcal { C }$, let$H ( X ) = h _ { 0 } ( X )$in$\mathrm { o b j } ( \mathcal { D } ) = N _ { 0 } \mathcal { D } .$. For each$f \colon X \to Y$in${ \mathcal { C } } ( X , Y )$ view$f = [ f ] X$as an element in$N _ { 1 } \mathcal { C }$with$d _ { 0 } ( f ) = Y$and$d _ { 1 } ( f ) = X$, and let $H ( f ) = \bar { h _ { 1 } ( f ) } \in N _ { 1 } \mathcal { D }$. Then$d _ { 0 } ( H ( f ) ) = d _ { 0 } ( h _ { 1 } ( f ) ) = h _ { 0 } ( d _ { 0 } ( f ) ) = h _ { 0 } ( Y ) =$ $H ( Y )$and$d _ { 1 } ( H ( f ) ) = d _ { 1 } ( h _ { 1 } ( f ) ) = h _ { 0 } ( d _ { 1 } ( f ) ) = h _ { 0 } ( X ) = H ( X )$, since$h _ { \bullet }$is a simplicial map, so$H ( f ) \colon H ( X ) \to H ( Y )$lies in${ \mathcal { D } } ( H ( X ) , H ( Y ) )$

We check that the rules$X \mapsto H ( X )$and$f \mapsto H ( f )$define a functor. If $f = i d _ { X } \in N _ { 1 } { \mathcal { C } }$then$f \ = \ s _ { 0 } ( X )$for$X ~ \in ~ N _ { 0 } \mathcal { C }$, so$H ( f ) = h _ { 1 } ( s _ { 0 } ( X ) ) =$ $s _ { 0 } ( h _ { 0 } ( X ) ) = s _ { 0 } ( H ( X ) ) = i d _ { H ( X ) } . \mathrm { ~ I f ~ } g \colon Y  Z$in$\mathcal { C }$then we view

$$
X \stackrel {f} {\longrightarrow} Y \stackrel {g} {\longrightarrow} Z
$$

as a 2-simplex$\sigma = [ g | f ] X \in N _ { 2 } \mathcal { C }$, with$d _ { 0 } ( \sigma ) = g , d _ { 1 } ( \sigma ) = g f$and$d _ { 2 } ( \sigma ) = f$in $N _ { 1 } \mathcal { C }$. Applying the simplicial map$h _ { \bullet }$we get a 2-simplex$\tau = h _ { 2 } ( [ g | f ] X ) \in N _ { 2 } \mathcal { D }$ with$d _ { 0 } ( \tau ) ) = h _ { 1 } ( g ) = H ( g ) , d _ { 1 } ( \tau ) ) = h _ { 1 } ( g f ) = H ( g f )$and$d _ { 2 } ( \tau ) ) = h _ { 1 } ( f ) =$ $H ( f )$. Hence τ is the 2-simplex

$$
H (X) \stackrel {H (f)} {\longrightarrow} H (Y) \stackrel {H (g)} {\longrightarrow} H (Z)
$$

in$N _ { \bullet } \mathcal { D } _ { \mathrm { : } }$, denoted$[ H ( g ) | H ( f ) ] H ( X )$, with the property that$H ( g ) \circ H ( f ) =$ $d _ { 1 } ( \tau ) = H ( g f )$

Starting with a functor$F \colon \mathcal { C }  \mathcal { D }$and applying this construction to$h _ { \bullet } =$ $N _ { \bullet } F ,$, it is clear that the resulting functor H agrees with$F$on objects and morphisms, so that$F = H$

Conversely, starting with a simplicial map$h _ { \bullet } \colon N _ { \bullet } \mathcal { C } \to N _ { \bullet } \mathcal { D }$, we claim that $h _ { \bullet }$equals the nerve map$N _ { \bullet } H$of the associated functor H. To see this, consider an n-simplex

$$
X _ {0} \xrightarrow {f _ {1}} \dots \xrightarrow {f _ {n}} X _ {n}
$$

$$
H (X _ {0}) \stackrel {{H (f _ {1})}} {{\longrightarrow}} \dots \stackrel {{H (f _ {n})}} {{\longrightarrow}} H (X _ {n})
$$

in$N _ { \bullet } \mathcal { C }$, say$\sigma = [ f _ { n } | \ldots | f _ { 1 } ] X _ { 0 }$. It is mapped under$N _ { \bullet } H$to the n-simplex in$N _ { \bullet } \mathcal { D }$, say$\tau = [ H ( f _ { n } ) | \dots | H ( f _ { 1 } ) ] F ( X _ { 0 } )$. We need to compare$\tau$with the image$h _ { n } ( \sigma )$of$\sigma$under$h _ { \bullet }$. Suppose that$h _ { n } ( \sigma )$is the simplex

$$
Y _ {0} \xrightarrow {g _ {1}} \dots \xrightarrow {g _ {n}} Y _ {n}.
$$

We now use naturality of$h _ { \bullet }$with respect to the vertex morphisms$\epsilon _ { i }$and the edge morphisms$\eta _ { i }$. For each$0 \leq i \leq n$the i-th vertex$Y _ { i }$of$h _ { n } ( \sigma )$equals$h _ { 0 }$ applied to the i-th vertex$X _ { i }$of σ, which equals$H ( X _ { i } )$, by construction of H on objects. And for each$1 \leq i \leq$n the edge$g _ { i } \colon Y _ { i - 1 } \to Y _ { i }$of$h _ { n } ( \sigma )$equals$h _ { 1 }$ applied to the edge$f _ { i } \colon X _ { i - 1 } \to X _ { i }$of$\sigma _ { \mathrm { { : } } }$, which equals$H ( f _ { i } )$, by construction of H on morphisms. Hence$\tau = h _ { n } ( \sigma )$, as required.□

Remark 7.1.7. The nerve functor induces an equivalence from Cat to the full subcategory of sSet generated by the simplicial sets$X _ { \bullet }$that satisfy the following Segal condition: The function

$$
X _ {n} \longrightarrow X _ {1} \times_ {X _ {0}} X _ {1} \times_ {X _ {0}} \dots \times_ {X _ {0}} X _ {1} \times_ {X _ {0}} X _ {1}
$$

sending$x \in X _ { n }$to the n-tuple$( \eta _ { n } ^ { * } ( x ) , \ldots , \eta _ { 1 } ^ { * } ( x ) )$is a bijection for each$n \geq$ $0 .$Here the right hand side is the limit of the diagram obtained by applying $X \colon \Delta ^ { o p }$Set to the lower part of the diagram

![](images/page_178_image_6.jpg)

in$\Delta ,$, and the function from$X _ { n }$is determined by the universal property of the limit.

Equivalently, let$E _ { \bullet } ^ { n } \subseteq \Delta _ { \bullet } ^ { n }$be the simplicial subset generated by the n edges $( = 1$-simplices)$\eta _ { i } \in \Delta _ { 1 } ^ { n }$for$1 \leq i \leq n$. The Segal condition for$X _ { \bullet }$asserts that the restriction map

$$
\mathbf {s S e t} \left(\Delta_ {\bullet} ^ {n}, X _ {\bullet}\right) \longrightarrow \mathbf {s S e t} \left(E _ {\bullet} ^ {n}, X _ {\bullet}\right)
$$

is a bijection, for each$n \geq 0$

[[This is not the same as being 1-coskeletal, which amounts to asking that the restriction map along$( \Delta _ { \bullet } ^ { n } ) ^ { ( 1 ) } \subseteq \Delta _ { \bullet } ^ { n }$is a bijection for each$n \geq 0 . 7 ]$

[[Alternatively, consider horns$\Lambda _ { i } ^ { n } ~ \subset ~ \Delta _ { \bullet } ^ { n }$, and ask that sSet$( \Delta _ { \bullet } ^ { n } , X _ { \bullet } )$ sSet$( \Lambda _ { i } ^ { n } , X _ { \bullet } )$is bijective for all$0 < i < n$(inner horns. Forward reference to ∞-categories.]]

[[Likewise, bicategories embed in bisimplicial sets.]]

Lemma 7.1.8. The nerve respects small limits, including products, as well as coproducts: There are natural simplicial isomorphisms

$$
N _ {\bullet} (\lim _ {c \in \mathcal {C}} F (c)) \cong \lim _ {c \in \mathcal {C}} N _ {\bullet} F (c)
$$

for each diagram$F \colon { \mathcal { C } } \to \mathbf { C a t }$, and

$$
N _ {\bullet} (\prod_ {i \in I} \mathcal {C} _ {i}) \cong \prod_ {i \in I} N _ {\bullet} \mathcal {C} _ {i}
$$

$$
N _ {\bullet} (\coprod_ {i \in I} \mathcal {C} _ {i}) \cong \coprod_ {i \in I} N _ {\bullet} \mathcal {C} _ {i}
$$

for each family$( \mathcal { C } _ { i } ) _ { i \in I }$of small categories.

Proof. Functors$[ n ]  \operatorname* { l i m } _ { c \in \mathcal { C } } F ( c )$correspond to families of functors$[ n ] \to F ( c )$ for c in${ \mathcal { C } } _ { : }$, compatible under the morphisms of$\mathcal { C } .$. Each functor$[ n ] \to \coprod _ { i \in I } \mathcal { C } _ { i }$ factors through a unique$\mathcal { C } _ { i }$□

Remark 7.1.9. The nerve$N _ { \bullet }$admits a left adjoint,$\mathcal { L }$: sSet → Cat, taking a simplicial set$X _ { \bullet }$to a coequalizer

$$
\coprod_ {\alpha : [ m ] \to [ n ]} X _ {n} \times [ m ] \xrightarrow [ t ]{\stackrel {{s}} {{\longrightarrow}}} \coprod_ {n \geq 0} X _ {n} \times [ n ] \longrightarrow \mathscr {L} (X _ {\bullet})
$$

in Cat. Here$X _ { n } \times [ n ]$denotes$\operatorname { U } _ { X _ { n } } [ n ]$, and so on. Functors$F \colon \mathcal { L } ( X _ { \bullet } )  \mathcal { D }$ correspond to compatible families of functors$F _ { n } \colon X _ { n } \times [ n ] \to { \mathcal { D } }$for$n \geq 0$, or equivalently, to compatible functions$G _ { n } \colon X _ { n } \to N _ { n } { \mathcal { D } }$. These are the same as simplicial maps$G _ { \bullet } \colon X _ { \bullet } \to N _ { \bullet { \mathcal { D } } }$

Remark 7.1.10. The nerve does not preserve general colimits. For example, for suitable functors s and t, the coequalizer of the nerve of the diagram

$$
[ 1 ] \sqcup [ 1 ] \xrightarrow [ t ]{s} [ 2 ] \sqcup [ 2 ]
$$

is not the nerve of a category. [[Elaborate?]]

Lemma 7.1.11. The nerve of the opposite category is the opposite simplicial set of the nerve:

$$
N _ {\bullet} (\mathcal {C} ^ {o p}) = N _ {\bullet} (\mathcal {C}) ^ {o p}
$$

[[Proof]]

Definition 7.1.12. The classifying space of a small category$\mathcal { C }$is the topological realization

$$
| \mathcal {C} | = | N _ {\bullet} \mathcal {C} |
$$

of its nerve. It is a CW complex with one n-cell for each non-degenerate nsimplex in$N _ { \bullet } { \mathcal { C } } , { \mathrm { i . e . } }$, for each chain

$$
X _ {0} \xrightarrow {f _ {1}} \ldots \xrightarrow {f _ {n}} X _ {n}
$$

of n composable, non-identity morphisms in$\mathcal { C }$.

Each functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$of small categories induces a cellular map

$$
| F | = | N _ {\bullet} F |: | \mathcal {C} | \longrightarrow | \mathcal {D} |
$$

of classifying spaces. The classifying space defines a functor

$$
| - |: \mathbf {C a t} \longrightarrow \mathbf {C W} \subset \mathbf {T o p}.
$$