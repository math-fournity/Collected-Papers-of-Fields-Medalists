# Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions

Hong Wang<sup>∗</sup>

Joshua Zahl <sup>†</sup>

February 26, 2025

## Abstract

We study sets of$\delta$tubes in$\mathbb { R } ^ { 3 }$, with the property that not too many tubes can be contained inside a common convex set$V .$We show that the union of tubes from such a set must have almost maximal volume. As a consequence, we prove that every Kakeya set in$\mathbb { R } ^ { 3 }$has Minkowski and Hausdorf dimension 3.

## Contents

1 Introduction 3
1.1 Theorem 1.2 and multi-scale analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Unions of convex sets, and non-clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 From Assertions $\mathcal{D}$ and $\mathcal{E}$ to the Kakeya set conjecture. 7
1.4 Proof philosophy, and previous work on the Kakeya set conjecture in $\mathbb{R}^3$ 8
1.5 A vignette of the proof. 9
1.6 Tube doubling and Keleti's line segment extension conjecture 14
1.7 Thanks 15
2 A sketch of the proof 15
2.1 Proposition 1.6: Assertions $\mathcal{D}$ and $\mathcal{E}$ are equivalent 15
2.2 A two-scale grains decomposition 19
2.3 Refined induction on scales 21
2.4 Multi-scale structure, Nikishin-Stein-Pisier factorization, and Sticky Kakeya 22
3 Notation 23
3.1 Convex sets and shadings 23
3.2 Table of notation 24

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>∗</sup>Courant Institute of Mathematical Sciences, New York University. New York, NY, USA.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>†</sup>Department of Mathematics, The University of British Columbia. Vancouver, BC, Canada.</span></small>

4 Wolff Axioms and Factoring Convex Sets 25
4.1 Definitions: Wolff axioms and covers 25
4.2 Factoring Convex Sets 26
4.3 Convex Sets and the Frostman Slab Wolff Axioms 31
4.4 The Frostman Slab Wolff Axioms and Covers 34

5 Factoring tubes into flat prisms 36
5.1 A few frequently used Cordoba-type $L^2$ arguments 38
5.1.1 A volume estimate for slabs 38
5.1.2 Tangential vs transverse prism intersection 39
5.2 Assertions $\mathcal{F},\mathcal{E}$, and $\tilde{\mathcal{E}}$ are equivalent 42
5.3 Proof of Proposition 5.1: Tubes that factor through flat boxes 46
5.4 Proof of Proposition 5.2: Factoring at two scales 49
5.5 Tubes organized into to slabs 49

6 Assertions $\mathcal{D}$ and $\mathcal{E}$ are equivalent 51
6.1 Proof of Proposition 6.3: A factoring trichotomy 56

7 A two-scale grains decomposition for tubes in $\mathbb{R}^3$ 60
7.1 Broadness 63
7.2 Broadness and the Frostman Slab Wolff axioms 66
7.3 The iteration base case: Guth's grains decomposition 69
7.4 Moves #1, #2, #3: Parallel structure 70
7.5 Using Moves #1, #2, #3 to prove Proposition 7.5 72

8 Moves #1, #2, and #3 74
8.1 Move #1: Replacing grains with longer grains to ensure $c\geq \delta \zeta \frac{\rho}{\delta} (\# \mathbb{T}_{\rho}) / (\# \mathbb{T})$ 74
8.2 Move #2: Replacing square grains with longer grains 74
8.3 Move #3: Replacing grains with wider grains with small $C_{KT - CW}^{\mathrm{loc}}$ 85

9 A refined induction-on-scales argument 100

10 Sticky Kakeya for tubes satisfying the Katz-Tao Convex Wolff Axioms at every Scale 103
10.1 Nikishin-Stein-Pisier Factorization and the Convex Wolff Axioms 105

11 Multi-scale analysis and the proof of Proposition 1.7 110
12 Tube Doubling 114

A A grains decomposition for tubes in<sub>R</sub><sup>3</sup>

B Wolf’s hairbrush argument and the proof of Proposition 1.8

## 1 Introduction

A Kakeya set is a compact subset of$\mathbb { R } ^ { n }$that contains a unit line segment pointing in every direction. The Kakeya set conjecture asserts that every Kakeya set in R<sup>n</sup> has Minkowski and Hausdorf dimension n. This conjecture was proved by Davies [5] when$n = 2$, and is open in three and higher dimensions. See [17, 28] for an introduction to the Kakeya conjecture and a survey of historical progress on the problem. See [15, 16, 18, 20, 21, 27, 31] for current progress towards the conjecture in three and higher dimensions.

The purpose of this paper is to obtain lower bounds on the volume of unions of δ-tubes (i.e. the $\delta$neighbourhoods of unit line segments) in$\mathbb { R } ^ { 3 }$that satisfy certain non-clustering conditions. As a consequence, we resolve the Kakeya set conjecture in three dimensions.

Theorem 1.1. Every Kakeya set in$\mathbb { R } ^ { 3 }$has Minkowski and Hausdorf dimension${ \mathcal { B } } .$

Theorem 1.1 is a corollary of the following slightly more technical result.

Theorem 1.2. For all$\varepsilon > 0$, there exists$K > 1$so that the following holds for all$\delta > 0$suficiently small. Let T be a set of δ-tubes contained in the unit ball in$\mathbb { R } ^ { 3 }$, and suppose that every rectangular prism of dimensions$a \times b \times 2$contains at most$1 0 0 a b \delta ^ { - 2 }$tubes from T (this is true, for example, if the tubes in T point in δ-separated directions). For each$T \in \mathbb { T }$, let$Y ( T ) \subset T$be a measurable set with$| Y ( T ) | \geq \lambda | T |$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \delta^ {\varepsilon} \lambda^ {K} \sum_ {T \in \mathbb {T}} | T |.\tag{1.1}
$$

The Kakeya maximal function conjecture asserts that for each$\varepsilon > 0 ,$, Inequality (1.1) is true for $K = 3$. The Kakeya maximal function conjecture in$\mathbb { R } ^ { 2 }$was proved by Cordoba [6]. While we do not resolve the Kakeya maximal function conjecture in$\mathbb { R } ^ { 3 }$, the weaker statement given in Theorem 1.2 is nonetheless suficient to obtain Theorem 1.1.

The hypothesis that each$a \times b \times 2$rectangular prism contains at most$1 0 0 a b \delta ^ { - 2 }$tubes from T is a type of non-clustering condition. A close variant of this hypothesis was first introduced by Wolf in [27], and sets of tubes that satisfy this hypothesis are said to satisfy the Wolf axioms.

## 1.1 Theorem 1.2 and multi-scale analysis

In [25, 26], the authors showed that Theorem 1.2 is true when the set$\mathbb { T }$has a property called stickiness (see Figure 1 (left)). Roughly speaking,$\mathbb { T }$is sticky if it satisfies the non-clustering condition from Theorem 1.2; has cardinality roughly$\delta ^ { - 2 }$; and for every intermediate scale$\delta \le \rho \le 1$ the tubes in$\mathbb { T }$can be covered by a set of$\rho$tubes that satisfy the non-clustering condition from Theorem 1.2 with$\rho$in place of δ.

Unfortunately, not every set of tubes is sticky — see Figure 1 (right) for an example. The arrangement illustrated in Figure 1 (right) is challenging to analyze, because the$\rho$tubes intersect with large multiplicity (i.e. many$\rho$tubes pass through a typical point), but the arrangement of

![](images/page_3_image_0.jpg)

Figure 1: Left: The tubes at scale$\rho$(black) satisfy the non-concentration hypothesis of Theorem 1.2, as do the (rescaled)$\delta$tubes (blue) inside each$\rho$tube. Multi-scale analysis is straightforward in this setting. This is sometimes called the “sticky” case. For clarity, not all$\delta$tubes have been drawn.

Right: The tubes at scale$\rho$do not satisfy the non-concentration hypothesis of Theorem 1.2. The tubes at scale$\rho$intersect with high multiplicity, while the$\delta$tubes inside each$\rho$tube are sparse.

$\delta$tubes inside each$\rho$tube is sparse (i.e. the union of$\delta$tubes inside each$\rho$tube only fill out a small fraction of that$\rho$tube). To help us analyze this type of arrangement, in Section 1.2 we will introduce two variants of the non-clustering hypothesis from Theorem 1.2, and two variants of the volume estimate (1.1).

## 1.2 Unions of convex sets, and non-clustering

In what follows, we say a pair of sets$U , V \subset \mathbb { R } ^ { n }$are essentially distinct if$\begin{array} { r } { | U \cap V | \leq \frac { 1 } { 2 } } \end{array}$max(|U|, |V|). $\mathbb { T }$will denote a set of essentially distinct δ-tubes contained in the unit ball in$\mathbb { R } ^ { 3 }$, and$| T |$will denote the volume of a δ-tube, i.e.$| T |$has size about$\delta ^ { 2 }$

Definition 1.3. Let T be a set of δ-tubes in$\mathbb { R } ^ { 3 }$

(A) We define$C _ { K T - C W } ( \mathbb { T } )$to be the infimum of all$C > 0$such that

#{T ∈ T : T ⊂ W} ≤ C|W||T|<sup>−1</sup> for all convex sets$W \subset \mathbb { R } ^ { 3 }$

We say that$\mathbb { T }$obeys the Katz-Tao Convex Wolf Axioms with error$C _ { K T - C W } ( \mathbb { T } )$

(B) We define$C _ { F - S W } ( \mathbb { T } )$to be the infimum of all$C > 0$such that

$$
\# \{T \in \mathbb {T} \colon T \subset W \} \leq C | W | (\# \mathbb {T}) \quad \text { for   all   slabs } W \subset \mathbb {R} ^ {3},
$$

where a$\mathrm { \Delta ^ { 6 } s l a b ^ { \prime } }$is the intersection of the unit ball with the thickened neighbourhood of a (hyper) plane. We say that T obeys the Frostman Slab Wolf Axioms with error$C _ { F - S W } ( \mathbb { T } )$

Remark 1.4.

(A) A note on etymology. The terms “Katz-Tao” and “Frostman” refer to diferent types of non-concentration conditions; they are the analogues of the well-studied non-concentration conditions $| E \cap B | \leq ( r / \delta ) ^ { 2 }$and$| E \cap B | \leq r ^ { 2 } | E |$, where$E \subset \mathbb { R } ^ { n }$is a δ-separated set and B is a ball of radius r. An arrangement of tubes arising from a Kakeya set, i.e. a set of δ-tubes with one tube pointing in each δ-separated direction, obeys both the Katz-Tao Convex Wolf Axiom and Frostman Slab Wolf Axiom with error$\lesssim 1$. The terms “convex” and “slab” refer to the class of sets for which the non-clustering condition is imposed. The term “Wolf axioms” suggests that the above definition is an analogue of the Wolf axioms from [27].

(B) The above definitions are two special cases of a non-clustering condition (Definition$1 . 3 ^ { \prime } )$that will be defined in Section 4.2. In Definition$1 . 3 ^ { \prime }$, both tubes and convex sets (resp. slabs) are replaced by more general objects.

(C) If T is non empty, then by taking W to be a$\delta \times 1 \times$1-slab containing a tube of T, we can see $C _ { F - S W } ( \mathbb { T } ) \leq C$implies$\# \mathbb { T } \geq C ^ { - 1 } \delta ^ { - 1 }$

Next, we introduce two Kakeya-type volume estimates for unions of tubes in$\mathbb { R } ^ { 3 }$. These are analogues of Inequality (1.1) that are carefully formulated to be amenable to induction on scale. In what follows, we use the notation$( \mathbb { T } , Y ) _ { \delta }$to denote a collection T of essentially distinct δ-tubes in$\mathbb { R } ^ { 3 }$, and a shading of these tubes, i.e. for each$T \in \mathbb { T } , Y ( T )$is a subset of$T$. For$\lambda > 0$, we say $( \mathbb { T } , Y ) _ { \delta }$is λ dense if$\begin{array} { r } { \sum _ { T \in \mathbb { T } } | Y ( T ) | \ge \lambda \sum _ { T \in \mathbb { T } } | T | } \end{array}$

Definition 1.5. Let$\sigma , \omega \geq 0$

• We say that Assertion$\mathcal { D } ( \sigma , \omega )$is true if the following holds: 0.718

For all$\varepsilon > 0$, there exists$\kappa , \eta > 0$such that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$ be$\delta ^ { \eta }$dense and obey the Katz-Tao Convex Wolf Axioms and Frostman Slab Wolf Axioms, both with error at most$\delta ^ { - \eta }$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega + \varepsilon} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.\tag{1.2}
$$

• We say that Assertion$\mathcal { E } ( \sigma , \omega )$is true if the following holds:

For all$\varepsilon > 0$, there exists$\kappa , \eta > 0$such that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be $\delta ^ { \eta }$dense. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega + \varepsilon} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 3 / 2} \ell (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma},\tag{1.3}
$$

where$m = C _ { K T - C W } ( \mathbb { T } )$and$\ell = C _ { F - S W } ( \mathbb { T } )$

Let us examine the numerology in the estimates (1.2) and (1.3). First, in the special case$\sigma = \omega$5 Assertion$\mathcal { D } ( \sigma , \sigma )$yields the estimate

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\varepsilon} (\# \mathbb {T}) ^ {- \sigma} \sum_ {T \in \mathbb {T}} | T |,
$$

i.e. it says that there are$\lesssim \delta ^ { - \varepsilon } ( \# \mathbb { T } ) ^ { \sigma }$tubes passing through a typical point of the union$\cup Y ( T )$ (for general σ and$\omega ,$this quantity is about$\delta ^ { \sigma - \omega - \varepsilon } ( \# \mathbb { T } ) ^ { \sigma } )$. For$\sigma > 0$small, this means that the tubes in the union$\cup Y ( T )$are almost disjoint. In the arguments that follow, it will be helpful to consider situations where$\sigma$and$\omega$are not necessarily equal.

The shape of the estimate (1.2) is motivated in part by the following consideration. To begin our induction on scale argument, we would like to prove that$\mathcal { E } ( \sigma , 0 )$holds for some$\sigma \in ( 0 , 2 / 3 ]$ When$\sigma = 1 / 2$and$\omega = 0$, Inequality (1.2) becomes the estimate

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {1 / 2 + \varepsilon} (\delta^ {2} \# \mathbb {T}) ^ {1 / 2}.
$$

This is essentially Wolf’s hairbrush bound from [27] (here we make use of the fact that$\mathbb { T }$obeys the Frostman Slab Wolf Axioms with small error; see Appendix B for details).

Assertion$\mathcal { D } ( \sigma , \omega )$is a special case of Assertion$\mathcal { E } ( \sigma , \omega )$. We will explain the shape of the final bracketed term of Inequality (1.3). To understand the term ℓ, it is helpful to consider the following scenario. Suppose we know that Assertion$\mathcal { D } ( \sigma , \omega )$is true. Let$\delta < \rho < 1$, and let$\mathbb { T }$be a set of$\delta$ tubes of cardinality$( \rho / \delta ) ^ { 2 }$that are contained inside a common$\rho$tube, which we will denote by$T _ { \rho }$ Suppose that the tubes in T obey the Katz-Tao Convex Wolf Axioms with error roughly 1. This implies that$C _ { F - S W } ( \mathbb { T } ) \sim \rho ^ { - 1 }$

For$T \in \mathbb { T }$(and hence$T \subset T _ { \rho } )$, we will write$T ^ { T _ { \rho } }$to denote the image of$T$under the afine transformation that anisotropically dilates$T _ { \rho }$by a factor of$\rho ^ { - 1 }$in its two “short” directions, and translates the image to the unit ball. After this rescaling and translation, the tubes in$\mathbb { T }$become $\delta / \rho$tubes that satisfy the Katz-Tao Convex Wolf Axioms and Frostman Slab Wolf Axioms, both with error roughly 1. Applying Assertion$\mathcal { D } ( \sigma , \omega )$to this rescaled collection of tubes, we obtain the volume bound

$$
\Big | \bigcup_ {T \in \mathbb {T}} T ^ {T _ {\rho}} \Big | \geq \kappa (\delta / \rho) ^ {\varepsilon} (\# \mathbb {T}) | T ^ {T _ {\rho}} | \big ((\# \mathbb {T}) | T ^ {\rho} | ^ {1 / 2} \big) ^ {- \sigma}.
$$

Undoing the anisotropic rescaling and translation (which distorted volumes by a factor of$\rho ^ { 2 } )$and noting that$| T ^ { T _ { \rho } } | \sim \rho ^ { 2 } | T |$, we can rewrite this as

$$
\Big | \bigcup_ {T \in \mathbb {T}} T \Big | \gtrsim \kappa \delta^ {\varepsilon} (\# \mathbb {T}) | T | \big (\ell (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}, \quad \text { where } \ell = C _ {F - S W} (\mathbb {T}) \sim \rho^ {- 1}.
$$

As a second justification for the term$\ell ,$note that for every set$\mathbb { T }$of$\delta$tubes, we must always have$C _ { F - S W } ( \mathbb { T } ) ( \# \mathbb { T } ) | T | ^ { 1 / 2 } \geq 1$. This is because we can always select a slab W of thickness$| T | ^ { 1 / 2 }$ that contains at least one tube from$\mathbb { T } .$. This observation also explains the choice to write$| T | ^ { 1 / 2 }$ rather than$\delta ;$any convex set$S \subset \mathbb { R } ^ { 3 }$of diameter 1 can be contained in a slab of thickness$| S | ^ { 1 / 2 }$ Later in the proof we will consider generalizations of Assertion$\mathcal { E } ( \sigma , \omega )$in which tubes are replaced by more general families of convex sets.

To understand the terms$m ^ { - 1 }$and$m ^ { - 3 / 2 }$in Inequality (1.3), it is helpful to consider the following scenario. Suppose we know that Assertion$\mathcal { D } ( \sigma , \omega )$is true. Let T be a set of$\delta$tubes that obey the Frostman Slab Wolf Axioms with error roughly 1, and the Katz-Tao Convex Wolf Axioms with error m >> 1. Let$\rho = m ^ { 1 / 2 } \delta$, and suppose that there exists a set$\mathbb { T } _ { \rho }$of$\rho$tubes, each of which contains$m \vert T _ { \rho } \vert \vert T \vert ^ { - 1 } = m ^ { 2 }$tubes from T. Observe that this is the maximum number of essentially distinct$\delta$tubes that can fit inside a$\rho$tube. In particular, the union of the$\delta$tubes inside each $\rho$tube fill out essentially all of the$\rho$tube. We have$\# \mathbb { T } _ { \rho } = m ^ { - 2 } ( \# \mathbb { T } ) = m ^ { - 1 } ( | T | / | T _ { \rho } | ) ( \# \mathbb { T } )$, i.e.$( \# \mathbb { T } _ { \rho } ) | T _ { \rho } | = m ^ { - 1 } ( \# \mathbb { T } ) | T |$. It is straightforward to compute that$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) \lesssim 1$. Applying Assertion$\mathcal { D } ( \sigma , \omega )$and using the fact that the union of$\delta$tubes inside each$\rho$tube fill out most of

the$\rho$tube, we obtain the volume bound

$$
\begin{array}{c} \Big | \bigcup_ {T \in \mathbb {T}} T \Big | \sim \Big | \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} T _ {\rho} \Big | \geq \kappa \rho^ {\omega + \varepsilon} (\# \mathbb {T} _ {\rho}) | T _ {\rho} | \big (\# \mathbb {T} _ {\rho}) | T _ {\rho} | ^ {1 / 2} \big) ^ {- \sigma} \\ = \kappa \rho^ {\omega + \varepsilon} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 3 / 2} (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}. \end{array}
$$

## 1.3 From Assertions D and E to the Kakeya set conjecture

Clearly$\mathcal { E } ( \sigma , \omega ) \implies \mathcal { D } ( \sigma , \omega )$. In Section 6, we will show that the reverse implication also holds:

Proposition 1.6. Let$0 \leq \sigma \leq 2 / 3 , \ \omega \geq 0$. Then$\mathcal { E } ( \sigma , \omega ) \longleftrightarrow \mathcal { D } ( \sigma , \omega )$

As mentioned above, our proof uses induction on scale. In brief, if$\mathcal { E } ( \sigma , \omega )$is true, then we will use this fact at many locations and scales to prove that$\mathcal { D } ( \sigma , \omega ^ { \prime } )$is true for some$\omega ^ { \prime } < \omega$(observe that smaller values of ω are better). The precise statement is as follows.

Proposition 1.7. There exists a function g :$[ 0 , 2 / 3 ] \times ( 0 , 1 ]  ( 0 , 1 ]$so that the following is true. Let$0 \leq \sigma \leq 2 / 3 , \ \omega > 0$. Then${ \mathcal E } ( \sigma , \omega ) \implies { \mathcal D } ( \sigma , \omega - g ( \sigma , \omega ) )$

Propositions 1.6 and 1.7 lead to a self-improving property for$\mathcal { E } ( \sigma , \omega )$(or equivalently, for $\mathcal { D } ( \sigma , \omega ) )$. Since the collections of tubes in the definitions of E and$\mathcal { D }$are essentially distinct and are contained in the unit ball, we always have$\# \mathbb { T } \lesssim \delta ^ { - 4 }$, and thus we can$\mathrm { \bar { \ t r a d e } } ^ { \prime \prime }$an improvement in ω for an improvement in σ. In particular, Proposition 1.7 tells us that${ \mathcal { E } } ( \sigma , \omega ) ~ \Longrightarrow ~ { \mathcal { D } } ( \sigma -$ $g ( \sigma , \omega ) / 4 , \omega )$

By applying Propositions 1.6 and 1.7, we can upgrade an initial estimate$\mathcal { D } ( \sigma , \omega )$to the improved estimate$\mathcal { D } ( \sigma - g ( \sigma , \omega ) / 4 , \omega )$. We can then iterate this process. In order to begin the iteration, we must prove that$\mathcal { D } ( \sigma , \omega )$is true for some$\omega > 0$and$0 \leq \sigma \leq 2 / 3$. In [27], Wolf proved that every Kakeya set in$\mathbb { R } ^ { n }$has Hausdorf dimension at least$\textstyle { \frac { n + 2 } { 2 } }$. In Appendix B, we will use a similar argument to show that$\mathcal { D } ( 1 / 2 , 0 )$is true:

Proposition 1.8.$\mathcal { D } ( 1 / 2 , 0 )$is true.

Beginning with Proposition 1.8 and then iterating Propositions 1.6 and 1.7, we conclude the following.

Theorem 1.9. The statements$\mathcal { D } ( 0 , 0 )$and$\mathcal { E } ( 0 , 0 )$are true.

Proof. Fix$\omega > 0$. By Proposition 1.8, we have that$\mathcal { D } ( 1 / 2 , 0 )$and hence$\mathcal { D } ( 1 / 2 , \omega )$is true. If $\mathcal { D } ( \sigma , \omega )$is true for some$\sigma \in [ 0 , 2 / 3 ]$, then so is$\mathcal { D } ( \sigma ^ { \prime } , \omega )$for all$\sigma ^ { \prime } \in [ \sigma , 2 / 3 ]$. Using Propositions 1.6 and 1.7, we conclude that the set$\{ \sigma \in [ 0 , 2 / 3 ] \colon { \mathcal { D } } ( \sigma , \omega )$is true} is relatively open in the metric space$[ 0 , 2 / 3 ]$. On the other hand, it is straightforward to verify from Definition 1.5 that this set is also relatively closed in$[ 0 , 2 / 3 ]$. We conclude that$\mathcal { D } ( \sigma , \omega )$is true for all$\sigma \in [ 0 , 2 / 3 ]$, so in particular $\mathcal { D } ( 0 , \omega )$is true.

A similar argument shows that$\mathcal { D } ( 0 , 0 )$is true; we have shown that$\mathcal { D } ( 0 , \omega )$is true for every $\omega > 0$. On the other hand, the set$\{ \omega \ge 0 \colon { \mathcal { D } } ( 0 , \omega )$is true} is relatively closed in the metric space $[ 0 , \infty )$. We conclude that$\mathcal { D } ( 0 , 0 )$is true. By Proposition 1.6 we have that$\mathcal { E } ( 0 , 0 )$is true.□

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">The conclusion of Theorem 1.9 can be rephrased as follows</span></small>

Corollary 1.10. For all$\varepsilon > 0$, there exists K so that the following holds for all$\delta > 0$suficiently small. Let$( \mathbb { T } , Y ) _ { \delta }$be λ-dense. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \delta^ {\varepsilon} \lambda^ {K} m ^ {- 1} (\# \mathbb {T}) | T |, \quad \text { where } m = C _ {K T - C W} (\mathbb {T}).\tag{1.4}
$$

Theorem 1.2 is now a special case of Corollary 1.10 — the hypotheses of Theorem 1.2 ensure that$C _ { K T - C W } ( \mathbb { T } ) \le 1 0 0 0$

## 1.4 Proof philosophy, and previous work on the Kakeya set conjecture in$\mathbb { R } ^ { 3 }$

In [16], Katz, Laba, and Tao proved that every Kakeya set in$\mathbb { R } ^ { 3 }$has upper Minkowski dimension at least$5 / 2 + c$for a (small) absolute constant$c > 0$. To do this, they analyzed the structure of a (hypothetical) Kakeya set in$\mathbb { R } ^ { 3 }$that has upper Minkowski dimension close to$5 / 2$. They proved that such a Kakeya set, or more precisely, the set of δ tubes arising from such a Kakeya set, must have three structural properties that they named “planiness,” “graininess,” and “stickiness.” Katz, Laba, and Tao then showed that a Kakeya set possessing these structural properties must have dimension at least$5 / 2 + c .$

In a talk and accompanying blog post [24] in 2014, Tao described a potential approach developed by Katz and Tao for solving the Kakeya problem. The Katz-Tao program proceeds as follows. First, one must show that a (hypothetical) counter-example to the Kakeya conjecture in$\mathbb { R } ^ { 3 }$, i.e. a Kakeya set with dimension strictly less than 3, must have the structural properties planiness, graininess, and stickiness. Second, these properties are used to obtain increasingly precise statements about the multi-scale structure of the Kakeya set. Third, results from discretized sum-product theory, in the spirit of Bourgain’s discretized sum-product theorem [4], are used to show that a Kakeya set with this type of multi-scale structure cannot exist.

When Tao shared the Katz-Tao program for solving the Kakeya conjecture in$\mathbb { R } ^ { 3 }$, some progress had already been made towards the first step described above. The Bennett-Carbery-Tao multilin ear Kakeya theorem [1] implied that every (hypothetical) counter-example to the Kakeya conjecture in$\mathbb { R } ^ { 3 }$must be plany. In [9], Guth proved that every (hypothetical) counter-example to the Kakeya conjecture in$\mathbb { R } ^ { 3 }$must be grainy. Stickiness, however, appeared to be more challenging.

The trilogy of papers [25, 26], and the present paper, can be thought of as a realization of the Katz-Tao program. In [25], the authors sidestepped the First step of the Katz-Tao program, and tackled the Second and Third steps. More precisely, the authors showed that every sticky Kakeya set in$\mathbb { R } ^ { 3 }$(i.e. a Kakeya set possessing the structural property of stickiness) must have Hausdorf dimension 3. This result is called the Sticky Kakeya Theorem. See [25, §1.1] for a discussion of the proof of this theorem, and how this proof compares to the strategy outlined in the Katz-Tao program.

In [26], the authors showed that every (hypothetical) Kakeya set in$\mathbb { R } ^ { 3 }$with Assouad dimension strictly less than 3 must be sticky. More precisely, they showed that if there exists a Kakeya set K with dim$_ A ( K ) < 3 ,$, then there must also exist a Kakeya set$K ^ { \prime }$with dim$_ { A } ( K ^ { \prime } ) < 3$that possesses a multi-scale self-similarity property similar to stickiness. The authors then used (a mild generalization of) the Sticky Kakeya Theorem to conclude that such a Kakeya set cannot exist. In particular, the Sticky Kakeya theorem from [25] assumed that the tubes from a Kakeya set point in diferent directions; in [26] the authors generalized this theorem to the weaker assumption that the tubes satisfy the Wolf axioms at every scale (a precise definition is given in Section 6). Note that since the Assouad dimension of a set can be larger than its Minkowski or Hausdorf dimension, the results in [26] did not resolve the Kakeya set conjecture in$\mathbb { R } ^ { 3 }$

In the present paper, we take this line of reasoning to its conclusion. We show that if T is a set of δ tubes that makes the estimate (1.2) from Assertion$\mathcal { D } ( \sigma , \omega )$tight for some σ and$\omega ,$then T must have a multi-scale self-similarity property similar to stickiness. Specifically, at many scales$\rho$ between$\delta$and 1, it is possible to cover T by a family of$\rho$tubes that obey Katz-Tao Convex Wolf Axioms (recall Definition 1.3) with small error. We then use a generalization of the Sticky Kakeya Theorem to show that the estimate (1.2) from Assertion$\mathcal { D } ( \sigma , \omega )$can only be tight for such a set T if$\sigma$and$\omega$are both 0. As we have already seen in Section 1.2, this implies that every Kakeya set in$\mathbb { R } ^ { 3 }$(and indeed, every set satisfying the Wolf axioms) must have Minkowski and Hausdorf dimension 3.

## 1.5 A vignette of the proof

Proposition 1.7 is the most important step in the proof of Theorem 1.9 (which in turn implies Theorems 1.1 and 1.2). In this section we will discuss some of the ideas used to prove this proposition in the key special case where the tubes are arranged as in Figure 1 (right). In Section 2 we will give a more thorough proof sketch that mirrors the structure of the actual proof.

To simply our exposition, we will disregard factors of the form$\delta ^ { \varepsilon }$or$\delta ^ { - \varepsilon }$, and we will (somewhat informally) write$A \lessapprox B$to mean that$A \le C \delta ^ { - \varepsilon } B$, for some constant C that is independent of δ and some small parameter$\varepsilon > 0$that we will ignore for the purposes of this sketch.

Fix a choice of$\sigma > 0$and$\omega > 0$, and suppose that Assertions$\mathcal { D } ( \sigma , \omega )$and$\mathcal { E } ( \sigma , \omega )$are true (roughly speaking, this says that the union of tubes has “dimension” at least$3 - \sigma - \omega )$. Let T be a set of$\delta$tubes of cardinality roughly$\delta ^ { - 2 }$that obeys the hypotheses of Assertion$\mathcal { D } ( \sigma , \omega )$. Our goal is to prove that$\bigcup _ { \mathbb { T } } T$has volume substantially larger than what is guaranteed by the estimate (1.2), i.e. we wish to obtain an inequality of the form

$$
\Big | \bigcup_ {T \in \mathbb {T}} T \Big | \gtrsim \delta^ {\sigma + \omega - \alpha},\tag{1.5}
$$

for some$\alpha = \alpha ( \sigma , \omega ) > 0$

Let us suppose that there exists a multiplicity$\mu$with the property that there are about$\mu$tubes from T passing through each point of$\cup _ { \mathbb { T } } T$. One way to obtain our desired volume bound (1.5) is to instead prove the multiplicity bound

$$
\mu \lessapprox \delta^ {- \sigma - \omega + \alpha}.\tag{1.6}
$$

A second way to obtain (1.5) is to show there exists some scale$\tau \gg \delta$such that the union$\cup _ { \mathbb { T } } T$ has larger than expected density at scale$\tau .$. More specifically, to obtain (1.5) it sufices to show that for a typical ball$B _ { \tau }$of radius$\tau$that intersects$\cup _ { \mathbb { T } } T$, we have a density estimate of the form

$$
\left| B _ {\tau} \cap \bigcup_ {T \in \mathbb {T}} T \right| \gtrsim \delta^ {- \alpha} (\delta / \tau) ^ {\sigma + \omega} | B _ {\tau} |.\tag{1.7}
$$

This will be discussed in greater detail in “Step 2, Case$2 ^ { \mathfrak { s } }$below.

If T is sticky, then for each scale$\delta < \rho < 1$, it is possible to find a set$\mathbb { T } _ { \rho }$consisting of about $\rho ^ { - 2 }$essentially distinct$\rho$tubes, each of which contain about$( \delta / \rho ) ^ { 2 }$tubes from T. We will suppose instead that$\mathbb { T }$is not sticky, i.e. T resembles the arrangement in Figure 1 (right). We will call this Simplifying Assumption A. More precisely, there exists a scale$\delta \ll \rho \ll 1$, and a set of essentially distinct$\rho$tubes$\mathbb { T } _ { \rho }$so that each$T \in \mathbb { T }$is contained in at least one tube from$\mathbb { T } _ { \rho } ,$and each$T _ { \rho } \in \mathbb { T } _ { \rho }$ contains about$\delta ^ { \nu } ( \rho / \delta ) ^ { 2 }$tubes from T, for some (small)$\nu > 0$. We will try to establish Inequality (1.6) with some small improvement$\alpha > 0$

## A fine-scale estimate.

For each$T _ { \rho } \in \mathbb { T } _ { \rho }$, define

$$
\mathbb {T} [ T _ {\rho} ] = \{T \in \mathbb {T}: T \subset T _ {\rho} \} \quad \text { and } \quad \mathbb {T} ^ {T _ {\rho}} = \{T ^ {T _ {\rho}}: T \in \mathbb {T} [ T _ {\rho} ] \}.\tag{1.8}
$$

(Recall that$T ^ { T _ { \rho } }$is defined in the discussion following Definition 1.5). Suppose that for each $T _ { \rho } \in \mathbb { T } _ { \rho } ,$the tubes in$\mathbb { T } ^ { T _ { \rho } }$satisfy the hypotheses of Assertion$\mathcal { D } ( \sigma , \omega )$; we will call this Simplifying Assumption B. We define$\mu _ { \mathrm { f i n e } }$to be the number of tubes from$\mathbb { T } ^ { T _ { \rho } }$passing through a typical point of$\textstyle \bigcup _ { \mathbb { T } ^ { T _ { \rho } } } T ^ { T _ { \rho } }$(it is harmless to suppose that this number is the same for each$\rho$tube in$\mathbb { T } _ { \rho } )$. Applying Assertion$\mathcal { D } ( \sigma , \omega )$to each set$\mathbb { T } ^ { T _ { \rho } }$and recalling the discussion following Definition 1.5, we conclude that

$$
\mu_ {\mathrm{fine}} \lessapprox \left(\frac {\delta}{\rho}\right) ^ {\sigma - \omega} (\# \mathbb {T} [ T _ {\rho} ]) ^ {\sigma} \leq \left(\frac {\delta}{\rho}\right) ^ {\sigma - \omega} \Bigl (\delta^ {\nu} \frac {\rho^ {2}}{\delta^ {2}} \Bigr) ^ {\sigma} = \delta^ {\nu \sigma} \Bigl (\frac {\rho}{\delta} \Bigr) ^ {\sigma + \omega},\tag{1.9}
$$

where the second inequality used our assumption that$\# \mathbb { T } [ T _ { \rho } ] \leq \delta ^ { \nu } ( \rho / \delta ) ^ { 2 }$

Inequality (1.9) bounds the typical intersection multiplicity of the δ tubes inside a common$\rho$ tube. Next, we define the quantity$\mu _ { \mathrm { c o a r s e } }$as follows: for a typical point$x \in \bigcup _ { \mathbb { T } } T$, there are about µ<sub>coarse</sub> distinct$\rho$tubes$T _ { \rho } \in \mathbb { T } _ { \rho }$with the property that$x \in \bigcup _ { \mathbb { T } [ T _ { \rho } ] } T$. With this definition, we have

$$
\mu \sim \mu_ {\mathrm{fine}} \mu_ {\mathrm{coarse}}.\tag{1.10}
$$

In the past, researchers have considered a weaker variant of (1.10) of the form$\mu \lesssim \mu _ { \mathrm { f i n e } } \mu _ {  { \mathbb { T } } _ { \rho } } ,$ where$\mu _ { \mathbb { T } _ { \rho } }$is the number of tubes from$\mathbb { T } _ { \rho }$passing through a typical point of$\cup _ { \mathbb { T } _ { \rho } } T _ { \rho }$. Our use of the more refined estimate (1.10) is a key new ingredient in the proof.

In light of (1.9), our desired multiplicity bound (1.6) will follow if we can establish the estimate

$$
\mu_ {\mathrm{coarse}} \lesssim \rho^ {- \sigma - \omega}.\tag{1.11}
$$

Naively, we might attempt to obtain (1.11) by observing that$\mu _ { \mathrm { c o a r s e } } \leq \mu _ { \mathbb { T } _ { \rho } }$, and then bounding the latter using Assertion$\mathcal { E } ( \sigma , \omega )$. However, this approach does not yield (1.11) because the cardinality of$\mathbb { T } _ { \rho }$(in this proof vignette) is substantially larger than$\rho ^ { - 2 }$

## A coarse-scale estimate Step 1: a grains decomposition.

Fix a tube$T _ { \rho } \in \mathbb { T } _ { \rho } .$Using a variant of Guth’s grains decomposition from [9], we can suppose that the$\delta / \rho$tubes in$\mathbb { T } ^ { T _ { \rho } }$arrange themselves into “grains,” i.e. rectangular prisms of dimensions $\delta / \rho \times c \times c$, with$\begin{array} { r } { c \ge \frac { \rho } { \delta } ( \# \mathbb { T } [ T _ { \rho } ] ) ^ { - 1 } } \end{array}$(Note that our hypotheses on the size of$\# \mathbb { T } [ T _ { \rho } ]$guarantees that $c \gg \delta / \rho )$. Here and throughout, we will adopt the convention that when referring to a rectangular prism of dimensions$a \times b \times c ,$we will always have$a \leq b \leq c$

This means that we can cover$\begin{array} { r } { E _ { T _ { \rho } } = \bigcup _ { \mathbb { T } ^ { T _ { \rho } } } T ^ { T _ { \rho } } } \end{array}$by a set of (mostly) disjoint rectangular prisms of dimensions$\delta / \rho \times c \times c ,$each of which have large intersection with$E _ { T _ { \rho } }$, in the sense that$| G \cap E _ { T _ { \rho } } | \gtrapprox$ |G|, for each such prism$G ;$see Figure 2 (left).

Undoing the anisotropic rescaling associated to$T _ { \rho }$that was described above, we have that $\mathsf { U } _ { \mathbb { T } [ T _ { \rho } ] } T$can be covered by a set of (mostly) disjoint rectangular prisms of dimensions$\delta \times \rho c \times c ;$

![](images/page_10_image_0.jpg)

![](images/page_10_image_1.jpg)

Figure 2: Left: The set of tubes$\mathbb { T } ^ { T _ { \rho } }$and the grains$\{ G \}$. For clarity, we have only drawn the grains and tubes that intersect the black tube (and even most of these have been omitted; the set of red tubes passing through the red grain fill out a substantial portion of the red grain, and similarly for the other grains); the situation is similar for each tube in$\mathbb { T } ^ { T _ { \rho } }$

Right: The image of Figure 2 (left) after undoing the anisotropic rescaling associated to$T _ { \rho }$. The dimensions of each grain have changed from$\delta / \rho \times c \times c$to$\delta \times \rho c \times c$

see Figure 2 (right). The same statement is true for each$T _ { \rho } \in \mathbb { T } _ { \rho }$. Let$\mathcal { P }$denote the set of all such $\delta \times \rho c \times c$prisms, from all$\rho$tubes in$\mathbb { T } _ { \rho }$. In order to bound$\mu _ { \mathrm { c o a r s e } }$, it sufices to bound the typical intersection multiplicity of the prisms in$\mathcal { P }$.

A coarse-scale estimate Step 2: intersection multiplicity of the grains.

Each$\delta \times \rho c \times c$prism in$\mathcal { P }$has an associated tangent plane, which is well-defined up to accuracy $\delta / ( \rho c )$. Suppose that the prisms in$\mathcal { P }$intersect “tangentially,” in the sense that whenever two prisms$P , P ^ { \prime } \in \mathcal { P }$intersect, their corresponding tangent planes agree up to accuracy$\delta / ( \rho c )$. We will call this Simplifying Assumption C. This means that for each point$x ,$the set of prisms from $\mathcal { P }$containing$x$are contained in a common prism of dimensions roughly$\delta / \rho \times c \times c$Thus we can partition$\mathcal { P }$into sets,$\mathcal { P } = \cup \mathcal { P } _ { i }$, with the property that if two prisms intersect then they are contained in a common set, and the$\delta \times \rho c \times c$prisms in each set$\mathcal { P } _ { i }$are contained in a common prism$\Pi _ { i }$of dimensions roughly$\delta / \rho \times c \times c ;$see Figure 3 (left).

Fix a set${ \mathcal { P } } ^ { \prime }$from the partition of P described above, and let □ be the associated$\delta / \rho \times c \times c$ prism. The image of each$P \in \mathcal { P } ^ { \prime }$under the anisotropic rescaling sending □ to the unit cube will be a prism of dimensions roughly$\rho \times \rho \times 1$(see Figure 3 (right)). Since a$\rho \times \rho \times 1$prism is comparable to a$\rho$tube, we will abuse notation slightly and pretend that this set of prisms is actually a set of$\rho$ tubes; we will call this set$\tilde { \mathbb { T } }$. Our task of estimating$\mu _ { \mathrm { c o a r s e } }$now reduces to estimating the typical intersection multiplicity of the tubes in$\tilde { \mathbb { T } }$

A priori, we do not know anything about the structure of the set$\tilde { \mathbb { T } } .$. A key new idea of our paper

![](images/page_11_image_0.jpg)

Figure 3: Left: two sets of$\delta \times \rho c \times c$prisms from the partition of$\mathcal { P }$(blue and red, respectively), and the associated$\delta / \rho \times c \times c$prisms □ and □ that contain them.

Right: The anisotropic rescaling that maps the blue$\delta / \rho \times c \times c$prism □ to the unit cube maps each blue$\delta \times \rho c \times c$prism to a$\rho \times \rho \times 1$prism (this is comparable to a$\rho$tube).

is a structure theorem that finds a set$\mathcal { W }$of convex sets such that W obeys (a suitable analogue of) the Katz-Tao Convex Wolf Axioms with error$\lessapprox 1$, and for each$W \in { \mathcal { W } }$, the set

$$
\tilde {\mathbb {T}} [ W ] = \{\tilde {T} \in \tilde {\mathbb {T}}: \tilde {T} \subset W \}
$$

satisfies the following key properties:

1. The cardinality estimate$\# \tilde { \mathbb { T } } [ W ] \approx C _ { K T - C W } ( \tilde { \mathbb { T } } ) \cdot | W | / | \tilde { T } |$(here$| \tilde { T } | \sim \rho ^ { 2 }$denotes the volume of a tube from$\tilde { \mathbb { T } } )$

2. For every convex set$U \subset W$, we have$\# \tilde { \mathbb { T } } [ U ] \lessapprox \frac { | U | } { | W | } \# \tilde { \mathbb { T } } [ W ]$

See Figure 5 for an illustration of this process, and Proposition 4.6 for a precise statement.

Let’s analyze a special case to see what these two properties mean. Suppose for a moment that W is$\mathrm { ~ a ~ } \tau$tube for some$\rho < \tau < 1$, then Item 1 says that after rescaling W to a unit cube, $\tilde { \mathbb { T } } [ W ]$becomes a set of$\rho / \tau { - } \mathrm { t u b e s }$of cardinality$\gtrapprox C _ { K T - C W } ( \tilde { \mathbb { T } } ) ( \tau / \rho ) ^ { 2 }$. Item 2 is a non-concentration condition on these tubes that was first introduced in [26]; families of tubes obeying this non-concentration condition are said to satisfy the Frostman Convex Wolf Axioms. For example, Items 1 and 2 are satisfied if the following holds: in each$\rho / \tau { \mathrm { - s e p a r a t e d } }$direction, we have roughly $C _ { K T - C W } ( \tilde { \mathbb { T } } )$many parallel$\rho / \tau \mathrm { - t u b e s } .$This type of tube arrangement was previously considered by Wolf [29], and volume estimates for unions of tubes satisfying these properties are called Xray estimates. The Assertion$\mathcal { E } ( \sigma , \omega )$, in particular$\mathcal { E } ( 1 / 2 , 0 )$, is a generalization of Wolf’s X-ray estimate from [29]. As a consequence, we should expect$\cup _ { \tilde { \mathbb { T } } [ W ] } \tilde { T }$to have a large volume if$C _ { K T - C W } ( \tilde { \mathbb { T } } )$ is substantially greater than 1. See Case 2 below for more details.

Our argument now splits into three cases.

Case 1:$C _ { K T - C W } ( \tilde { \mathbb { T } } ) \lessapprox 1$. In this case, W consists of a single convex set, which is comparable to the unit ball. To simplify this proof vignette, we will suppose that$\tilde { \mathbb { T } }$satisfies the Frostman Slab Wolf

Axioms with error$\lessapprox 1$, and thus$\tilde { \mathbb { T } }$satisfies the hypothesis of Assertion$D ( \sigma , \omega )$; this simplification can be justified using certain rescaling arguments that we will not detail here. In particular, this means that$\# \tilde { \mathbb { T } } \lessapprox \rho ^ { - 2 }$, and thus we can apply Assertion$D ( \sigma , \omega )$to obtain the desired estimate

$$
\mu_ {\mathrm{coarse}} \lessapprox \rho^ {\sigma - \omega} (\# \tilde {\mathbb {T}}) ^ {\sigma} \lessapprox \rho^ {- \sigma - \omega}.
$$

Case$\mathcal { Q } \colon \ C _ { K T \cdot C W } ( \tilde { \mathbb { T } } ) \gg 1$, and each$W \in \mathcal { W }$has thickness$t \gg \delta$. To handle this case, we will consider the following analogy. Suppose that T is a set of$\delta$tubes of cardinality$m \delta ^ { - 2 }$, for some $m \gg 1$. Suppose furthermore that$\mathbb { T }$satisfies the Katz-Tao Convex Wolf Axioms with error$m$ and the Frostman Slab Wolf Axioms with error$\sim 1$. Then Assertion$\mathcal { E } ( \sigma , \omega )$says that$\cup _ { \mathbb { T } } T$has volume$\gtrapprox m ^ { \sigma / 2 } \delta ^ { \sigma + \omega }$, which is substantially larger than$\delta ^ { \sigma + \omega }$. We apply a similar argument to the set of tubes$\tilde { \mathbb { T } } [ W ]$to conclude that for each$W \in { \mathcal { W } }$, the union$\cup _ { \tilde { \mathbb { T } } [ W ] } \tilde { T }$has large volume (see also the discussion of the two properties above). Undoing the re-scaling described in the previous step (and illustrated in Figure 3), we obtain a scale$\delta \ll \tau \ll \delta / \rho \geq ( \mathrm { h e r e } \ \tau$depends on t and the orientation of$W$with respect to$\boxed { \begin{array} { r l } \end{array} }$with the property that for a typical point$x \in \bigcup _ { \mathbb { T } } T$, the ball $B _ { \tau } = B ( x , \tau )$has a large intersection with$\cup _ { \mathbb { T } } T$. This means that we obtain an inequality of the following form:

$$
\left| B _ {\tau} \bigcap (\bigcup_ {T \in \mathbb {T}} T) \right| \gtrsim C _ {K T - C W} (\tilde {\mathbb {T}}) ^ {\sigma / 2} (\delta / \tau) ^ {\sigma + \omega} | B _ {\tau} |.\tag{1.12}
$$

This is precisely (1.7), provided$C _ { K T - C W } ( \tilde { \mathbb { T } } ) \geq \delta ^ { - 2 \alpha / \sigma }$(this is what we mean by$C _ { K T - C W } ( \mathbb { T } ) \gg 1 )$

Next, let$\mathbb { T } _ { \tau }$be a set of essentially distinct$\tau$tubes with the property that each$T \in \mathbb { T }$is contained in some tube from$\mathbb { T } _ { \tau }$, and suppose that each$T _ { \tau } \in \mathbb { T } _ { \tau }$contains about$( \# \mathbb { T } ) / ( \# \mathbb { T } _ { \tau } )$tubes from T. It is straightforward to compute that$C _ { F - S W } ( \mathbb { T } _ { \tau } ) \lessapprox 1$(indeed, this is inherited from T), and that$C _ { K T - C W } ( \mathbb { T } _ { \tau } ) \approx ( \# \mathbb { T } _ { \tau } ) | T _ { \tau } |$(this latter quantity is$\geq 1$, since$C _ { K T - C W } ( \mathbb { T } ) \lessapprox 1$and thus at least$| T _ { \tau } | ^ { - 1 }$essentially distinct$\tau$tubes are needed to cover the tubes in T). Applying the estimate $\mathcal { E } ( \sigma , \omega )$to$\mathbb { T } _ { \tau } .$, we conclude that

$$
\Big | \bigcup_ {T _ {\tau} \in \mathbb {T} _ {\tau}} T _ {\tau} \Big | \gtrsim \tau^ {\omega} \Big ((\# \mathbb {T} _ {\tau}) | T _ {\tau} | ^ {2} \Big) ^ {\sigma / 2} \gtrsim \tau^ {\omega + \sigma}.
$$

For the last inequality, we used the estimate$\# \mathbb { T } _ { \tau } \gtrapprox | T _ { \tau } | ^ { - 1 }$, which follows from the hypotheses $C _ { K T - C W } ( \mathbb { T } ) \ \lessapprox \ 1$and$\# \mathbb { T } \sim \delta ^ { - 2 }$. Pairing this scale−τ estimate with our previously discussed estimate (1.12) inside balls of radius$\tau _ { \ast }$we obtain (1.5):

$$
\begin{array}{c} \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \Big | \bigcup_ {T _ {\tau} \in \mathbb {T} _ {\tau}} T _ {\tau} \Big | \cdot C _ {K T - C W} (\tilde {\mathbb {T}}) ^ {\sigma / 2} \left(\frac {\delta}{\tau}\right) ^ {\sigma + \omega} \\ \gtrsim \delta^ {\omega + \sigma} C _ {K T - C W} (\tilde {\mathbb {T}}) ^ {\sigma / 2}. \end{array}
$$

Case$\mathcal { S } \colon C _ { K T \cdot C W } ( \tilde { \mathbb { T } } ) \gg 1$, and each$W \in { \mathcal { W } }$has$t h i c k n e s s \approx \delta$. In this case, the grains in$\mathcal { P }$can be replaced by larger prisms—these are the (rescaled) convex sets coming from W. This process may change$\rho$and also change the dimensions of the grains. We iterate the argument described above with our new$\rho$and larger grains. If we repeatedly find ourselves in Case 3 with each iteration, then the grains become wider and wider. Suppose for the moment that after a suficient number of iterations, both$\rho$and$c$have size ≈ 1. Then$\cup _ { \mathbb { T } } T$is organized into a union of$\delta \times 1 \times 1 { \mathrm { - s l a b s } }$. From here, a straightforward geometric argument (analogous to Cordoba’s proof of the Kakeya maximal function conjecture in the plane) shows that$| \cup _ { \mathbb { T } } T | \approx 1$. If instead$c \ll 1$, then a diferent Cordoba type geometric argument and the assumption that$\mu \gg 1$(if this assumption fails, then we are done) allows us to enlarge c, and we iterate the argument again.

## Justifying the simplifying assumptions.

We will briefly justify Simplifying Assumptions$\mathrm { ~ A ~ - ~ C ~ }$. First, if Simplifying Assumption A fails, then we can directly prove (1.5) by using the sticky Kakeya theorem; see Section 10 for details. In general, Simplifying Assumption B might not hold, but if it fails, then either it is possible to directly prove (1.5), or else it is possible to find an intermediate scale between δ and$\rho$at which the assumption holds; this introduces additional steps and complexity to the argument, but does not fundamentally change the flavor of the proof.

If Simplifying Assumption C fails, then we can use a straightforward Cordoba-type geometric argument to show that for a typical prism$P _ { 0 } \in \mathcal { P }$, the union of prisms$P \in { \mathcal { P } }$that intersect$P _ { 0 }$fill out (most of) a thickened neighbourhood of$P _ { 0 }$. This in turn means that for a typical tube$T _ { 0 } \in \mathbb { T }$ the union$\cup _ { \mathbb { T } } T$fills out (most of) a thickened neighbourhood of$T _ { 0 }$. We can then argue as in Case 2 (described above) to obtain (1.6).

In the table below, we summarize some of the geometric objects that appeared in the arguments from Section 1.5.

| object | cardinality | dimensions | bounding box | union size | desired union size | multiplicity | desired multiplicity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\mathbb{T}$ | $\delta^{-2}$ | $\delta \times \delta \times 1$ | $1 \times 1 \times 1$ | $\gtrsim \delta^{\sigma+\omega}$ | $\gtrsim \delta^{\sigma+\omega-\alpha}$ | $\lessapprox \delta^{-\sigma-\omega}$ | $\lessapprox \delta^{-\sigma-\omega+\alpha}$ |
| $\mathbb{T}[T_{\rho}]$ | $\delta^{\nu}(\delta/\rho)^{-2}$ | $\delta \times \delta \times 1$ | $\rho \times \rho \times 1$ |  |  | $\lessapprox \delta^{\nu\sigma}\left(\frac{\delta}{\rho}\right)^{-\sigma-\omega}$ |  |
| $\mathcal{P}$ |  | $\delta \times c\rho \times c$ | $\frac{\delta}{\rho} \times c \times c$(if tangential) |  |  | $\mu_{\text{coarse}}$ | $\lessapprox \rho^{-\sigma-\omega}$ |
| $\tilde{\mathbb{T}}$ |  | $\rho \times \rho \times 1$ | $1 \times 1 \times 1$ |  |  | $\mu_{\text{coarse}}$ | $\lessapprox \rho^{-\sigma-\omega}$ |

## 1.6 Tube doubling and Keleti’s line segment extension conjecture

In this section we will discuss further consequences of Theorem 1.9. We begin by introducing the Tube Doubling Conjecture (see e.g. [10, Conjecture 15.19]). In what follows, if$T$is a δ tube in$\mathbb { R } ^ { n }$ then$\tilde { T }$denotes the 2-fold dilate of T. Besicovitch constructed a set$\mathbb { T }$of roughly$\delta ^ { - 1 }$tubes in$\mathbb { R } ^ { 2 }$ for which

$$
\Big | \bigcup_ {T \in \mathbb {T}} \tilde {T} \Big | \gtrsim \frac {\log (1 / \delta)}{\log \log (1 / \delta)} \Big | \bigcup_ {T \in \mathbb {T}} T \Big |.\tag{1.13}
$$

This construction was adapted by Feferman [8] to show that the ball multiplier is unbounded on $L ^ { p }$for$p \neq 2$. The Tube Doubling Conjecture asserts that up to sub-polynomial factors, Inequality (1.13) is tight. One formulation is as follows.

Conjecture 1.11. Let$n \geq 2$and$\varepsilon > 0$. Then the following is true for all$\delta > 0$suficiently small. Let T be a set of δ tubes in$\mathbb { R } ^ { n }$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} \tilde {T} \Big | \leq \delta^ {- \varepsilon} \Big | \bigcup_ {T \in \mathbb {T}} T \Big |.\tag{1.14}
$$

Conjecture 1.11 is known in dimension two, and open in three and higher dimensions. As a consequence of Theorem 1.9, we resolve Conjecture 1.11 in$\mathbb { R } ^ { 3 }$

Theorem 1.12. The Tube Doubling Conjecture is true in$\mathbb { R } ^ { 3 }$

We will discuss the proof of Theorem 1.12 in Section 12. The Tube Doubling Conjecture is closely related to Keleti’s Line Segment Extension Conjecture [22]. In the statement that follows, if ℓ is a line segment (by definition, line segments have positive length), then$\tilde { \ell }$denotes the line containing ℓ.

Conjecture 1.13. Let L be a set of line segments in$\mathbb { R } ^ { n }$. Then

$$
\dim \left(\bigcup_ {\ell \in L} \tilde {\ell}\right) = \dim \left(\bigcup_ {\ell \in L} \ell\right).
$$

In [23], Keleti and M´ath´e proved that the Kakeya set conjecture in$\mathbb { R } ^ { n }$implies Conjecture 1.13 in$\mathbb { R } ^ { n }$. As a consequence, Theorem 1.1 has the following corollary.

Theorem 1.14. Conjecture 1.13 is true in$\mathbb { R } ^ { 3 }$.

## 1.7 Thanks

The authors would like to thank Ciprian Demeter, Larry Guth, Nets Katz, Izabella Laba, Tuomas Orponen, Keith Rogers, Pablo Shmerkin, and Terence Tao for comments, suggestions, and corrections to an earlier version of this manuscript. Hong Wang would like to thank Guido de Philippis for interesting conversations. Hong Wang is supported by NSF CAREER DMS-2238818 and NSF DMS-2055544. Joshua Zahl is supported by a NSERC Discovery Grant and a NSERC Alliance Grant.

## 2 A sketch of the proof

Our goal in this section is to briefly outline the major steps in the proofs of Propositions 1.6 and 1.7. To simplify the exposition in this proof sketch, we will gloss over many technical details and make a number of white lies. For example, we will pretend that every shading$Y ( T ) \subset T$is just the trivial shading$Y ( T ) = T$. At the same time, we will pretend that each point$x \in \cup _ { T \in \mathbb { T } } T$is always contained in the same number of tubes from T, and similarly for other collections of tubes, rectangular prisms, etc. In the same spirit as in Section 1.5, we will disregard factors of the form $\delta ^ { \varepsilon }$or$\delta ^ { - \varepsilon } .$, and we will (somewhat informally) write$A \lessapprox B$to mean that$A \le C \delta ^ { - \varepsilon } B$, for some constant C that is independent of δ and some small parameter$\varepsilon > 0$that we will ignore for the purposes of this sketch (in Section 3 we will give a precise definition of the relation$\lessapprox$which will be used for the remainder of the proof). In the actual proof there are myriad parameters (of which ε is an example), and navigating the precise interplay between these parameters is a major technical challenge in the paper. This issue will be entirely ignored in the proof sketch.

Finally, in this proof sketch it will be helpful to introduce “informal versions” of certain definitions and theorems that occur later in the paper. These informal versions are intentionally imprecise, and often are not literally true. These informal statements will be superseded by their formal counterparts that occur later in the paper. With these caveats, we now proceed as follows.

## 2.1 Proposition 1.6: Assertions D and E are equivalent

Our first goal is to prove Proposition 1.6. To do this, we will iterate the following lemma:

Lemma 6.4, informal version. Let$0 < \omega < \omega ^ { \prime }$, and suppose that both$\mathcal { D } ( \sigma , \omega )$and$\mathcal { E } ( \sigma , \omega ^ { \prime } )$are true. Then$\mathcal { E } ( \sigma , \omega ^ { \prime } - \alpha )$is true, where$\alpha > 0$depends only on the quantities ω and$\omega ^ { \prime } - \omega$

To prove Proposition 1.6, we fix$\omega$and$\sigma$and suppose that$\mathcal { D } ( \sigma , \omega )$is true. The statement $\mathcal { E } ( \sigma , 2 )$is trivially true, since the volume of$\bigcup _ { \mathbb { T } } T$is bounded below by the volume of a single tube. We then iterate Lemma 6.4 multiple times to conclude that$\mathcal { E } ( \sigma , \omega + \varepsilon )$is true for every$\varepsilon > 0$, and thus$\mathcal { E } ( \sigma , \omega )$is true.

The idea behind Lemma 6.4 is as follows. Given a set T of δ tubes, our goal is to establish the estimate

$$
\Big | \bigcup_ {T \in \mathbb {T}} T \Big | \gtrsim \delta^ {\omega^ {\prime} - \alpha} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 3 / 2} \ell (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma},\tag{2.1}
$$

with$m = C _ { K T - C W } ( \mathbb { T } )$and$\ell = C _ { F - S W } ( \mathbb { T } )$. For simplicity we will pretend that every collection of tubes always satisfies$C _ { F - S W } ( \mathbb { T } ) \lessapprox 1$. Removing this assumption introduces a few additional dificulties that we will not discuss here.

If$C _ { K T - C W } ( \mathbb { T } ) \lessapprox 1$, then T satisfies the hypotheses of$\mathcal { D } ( \sigma , \omega )$, and thus we can apply the estimate $\mathcal { D } ( \sigma , \omega )$to T and immediately obtain (2.1). Suppose instead that$C _ { K T - C W } ( \mathbb { T } ) = m \gg 1$. This means that there is a convex set W that contains at least$m | W | \delta ^ { - 2 }$tubes from T. The convex set$W$ must have diameter$\geq 1$(since it contains at least one tube), and wlog we can suppose that it has diameter$\sim 1$(since the tubes in$\mathbb { T }$are contained in the unit ball). Thus we may suppose that$W$is comparable to a rectangular prism of dimensions$a \times b \times 1$, for some$\delta \leq a \leq b \leq 1$. We will focus on the most interesting case, which is when a and b have similar size, i.e. W is comparable to a$\rho$ tube for some$\delta \le \rho \le 1$

Motivated by the above discussion, let us explore what happens when$C _ { K T - C W } ( \mathbb { T } ) = m$>> 1; there is a scale$\delta \ll \rho \ll 1 ;$and a set$\mathbb { T } _ { \rho }$of$\rho$tubes, each of which contains about$m ( \rho / \delta ) ^ { 2 }$tubes from T. It is straightforward to verify that$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) = O ( 1 )$: if a convex set W contains$N$ tubes from$\mathbb { T } _ { \rho } ,$then it contains about$N m ( \rho / \delta ) ^ { 2 }$tubes from T. On the other hand, W can contain at most$m | W | / \delta ^ { 2 }$tubes from$\mathbb { T } ;$see Figure 4. Note that this situation is in some sense the opposite of the problematic situation described in Section 1.1 (and illustrated in Figure 1 (right)); in that Section, we considered the scenario where there are many (i.e. far more than$\rho ^ { - 2 } ) \ \rho$tubes, each of which contains few (i.e. far fewer than$( \rho / \delta ) ^ { 2 } )$δ tubes.

We have just shown that$\mathbb { T } _ { \rho }$satisfies the hypotheses of$\mathcal { D } ( \sigma , \omega )$, and thus

$$
\Big | \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} T _ {\rho} \Big | \gtrsim \rho^ {\omega} (\# \mathbb {T} _ {\rho}) | T _ {\rho} | \Big ((\# \mathbb {T} _ {\rho}) | T _ {\rho} | ^ {1 / 2} \Big) ^ {- \sigma}.\tag{2.2}
$$

(In the above, we write$\vert T _ { \rho } \vert \sim \rho ^ { 2 }$to denote the volume of$\mathrm { ~ a ~ } \rho$tube). On the other hand, for each $T _ { \rho } \in \mathbb { T } _ { \rho } .$, the (re-scaled) δ tubes inside$T _ { \rho }$will satisfy the Katz-Tao Convex Wolf Axioms with error about$m ,$i.e.$C _ { K T - C W } ( \mathbb { T } ^ { T _ { \rho } } ) \lesssim m = C _ { K T - C W } ( \mathbb { T } )$

Applying the estimate (1.3) from Assertion$\mathcal { E } ( \sigma , \omega ^ { \prime } )$, we conclude that

$$
\Big | \bigcup_ {T ^ {T _ {\rho}} \in \mathbb {T} ^ {T _ {\rho}}} T ^ {T _ {\rho}} \Big | \gtrsim \Big (\frac {\delta}{\rho} \Big) ^ {\omega^ {\prime}} m ^ {- 1} (\# \mathbb {T} [ T _ {\rho} ]) | T ^ {T _ {\rho}} | \Big (m ^ {- 3 / 2} (\# \mathbb {T} [ T _ {\rho} ]) | T ^ {T _ {\rho}} | ^ {1 / 2} \Big) ^ {- \sigma}.
$$

(2.3)

Inequality (2.2) says that about$\rho ^ { - 3 + \omega } ( \# \mathbb { T } _ { \rho } ) | T _ { \rho } | \Big ( ( \# \mathbb { T } ) _ { \rho } | T _ { \rho } | ^ { 1 / 2 } \Big ) ^ { - \sigma }$distinct$\rho$balls are needed to cover$\bigcup _ { \mathbb { T } } T$, and the RHS of (2.3) gives a lower bound for the density of$\cup _ { \mathbb { T } } T$inside a typical $\rho$ball from this collection. Combining these estimates and noting that$( \# \mathbb { T } _ { \rho } ) ( \# \mathbb { T } [ T _ { \rho } ] ) = \# \mathbb { T }$and $| T _ { \rho } | | T ^ { T _ { \rho } } | = | T |$, we conclude that

![](images/page_16_image_0.jpg)

Figure 4:$\mathbb { T } _ { \rho }$(black), and$\mathbb { T }$(blue). For clarity, we have only drawn the tubes from$\mathbb { T }$inside two $\rho$tubes. Note that the$\rho$tubes are (comparatively) sparse, while the tubes in$\mathbb { T } [ T _ { \rho } ]$are densely packed. The situation is similar to that in Figure 1 (left), except that the set of (rescaled) δ tubes inside each$\rho$tube are very dense, and thus$C _ { K T - C W } ( \mathbb { T } ^ { T _ { \rho } } )$is large.

$$
\Big | \bigcup_ {T \in \mathbb {T}} T \Big | \gtrsim \rho^ {\omega - \omega^ {\prime}} \delta^ {\omega^ {\prime}} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 3 / 2} (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma}.\tag{2.4}
$$

If$\rho < \delta ^ { \zeta }$for some$\zeta > 0$bounded away from 0, then (2.4) is precisely (2.1), with$\alpha = \zeta ( \omega ^ { \prime } - \omega )$

This concludes the proof of Lemma 6.4 and hence Proposition 1.6, except that in our proof we assumed the existence of a set of$\rho$tubes that satisfies the following properties:

(a)$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) = O ( 1 )$

(b) Each$\rho$tube$T _ { \rho }$contains about m$| T _ { \rho } | / | T |$tubes from$\mathbb { T } _ { : }$where$m = C _ { K T - C W } ( \mathbb { T } )$

(c) The sets in$\mathbb { T } _ { \rho }$are tubes, i.e. they have dimensions$\rho \times \rho \times 1$

(d)$\rho \ll 1$, in the sense that$\rho = \delta ^ { \zeta }$for some$\zeta > 0$bounded away from 0.

Unfortunately, given a set of δ tubes T, it need not be the case that such a set of$\rho$tubes satisfying the above properties will always exist. Consider, for example, the case where$\mathbb { T }$is an arrangement of$\delta$tubes of cardinality$\delta ^ { - 5 / 2 }$, we define$s \ = \ \delta ^ { 5 / 8 }$, and each of the roughly$s ^ { - 4 }$ essentially distinct s tubes in$B ( 0 , 1 ) \subset \mathbb { R } ^ { 3 }$contains one$\delta$tube from$\mathbb { T } .$. Examples of this type are called the well-spaced case. For such a set T, there does not exist a scale$\rho$satisfying Items$\mathrm { ( a ) \_ - }$ (d) above. Note, however, that a slightly diferent statement is true for this arrangement: There are scales$\delta \leq \tau \leq \rho ,$and sets of$\tau$and$\rho$tubes$\mathbb { T } _ { \tau }$and$\mathbb { T } _ { \rho }$that satisfy the following:

(i) T has cardinality about$m | T | ^ { - 1 }$, where$m = C _ { K T - C W } ( \mathbb { T } )$

(ii)$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) \lesssim ( \# \mathbb { T } _ { \rho } ) | T _ { \rho } |$

(iii) Each$\rho$tube$T _ { \rho }$satisfies$C _ { K T - C W } ( \mathbb { T } _ { \tau } ^ { T _ { \rho } } ) = O ( 1 )$, and$\# \mathbb { T } _ { \tau } ^ { T _ { \rho } } \sim | T _ { \tau } ^ { T _ { \rho } } | ^ { - 1 } = ( \rho / \tau ) ^ { 2 }$

(iv) Each$\tau$tube$T _ { \tau }$satisfies$C _ { K T - C W } ( \mathbb { T } ^ { T _ { \tau } } ) \lesssim ( \# \mathbb { T } [ T _ { \tau } ] ) | T ^ { T _ { \tau } } |$

(v)$\tau \ll \rho ,$in the sense that$\tau = \delta ^ { \zeta } \rho$for some$\zeta > 0$bounded away from$0 .$.

For the well-spaced example described above, we would have$m = \delta ^ { - 1 / 2 } , \tau = \delta , \rho = \delta ^ { 1 / 4 } , \mathbb { T } _ { \tau } = \mathbb { T }$2 and$\mathbb { T } _ { \rho }$is a maximal set of$\rho ^ { - 4 }$essentially distinct$\rho$tubes.

The arguments described above can be adapted to this situation: By Item (ii), the$\rho$tubes satisfy the hypothesis of Assertion$\mathcal { E } ( \sigma , \omega )$, and thus we obtain the volume estimate

$$
\Big | \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} T _ {\rho} \Big | \gtrsim \rho^ {\omega^ {\prime}} (\# \mathbb {T} _ {\rho}) ^ {\sigma / 2} | T _ {\rho} | ^ {\sigma}.\tag{2.5}
$$

Note that the RHS of (2.5) is precisely the estimate (1.3) from Assertion$\mathcal { E } ( \sigma , \omega ^ { \prime } )$(ignoring the multiplicative constant$\kappa )$, with$m = ( \# \mathbb { T } _ { \rho } ) | T _ { \rho } |$and$\ell = O ( 1 )$

By Item (iii), the$\tau$tubes inside each$\rho$tube satisfy the hypotheses of Assertion$\mathcal { D } ( \sigma , \omega )$, and thus for each$\rho$tube$T _ { \rho }$we obtain the volume estimate

$$
\Big | \bigcup_ {T _ {\tau} ^ {T _ {\rho}} \in \mathbb {T} _ {\tau} ^ {T _ {\rho}}} T _ {\tau} ^ {T _ {\rho}} \Big | \gtrsim \left(\frac {\tau}{\rho}\right) ^ {\omega} | T _ {\tau} ^ {T _ {\rho}} | ^ {\sigma / 2}.\tag{2.6}
$$

Note that the RHS of (2.6) is precisely the estimate (1.2) from Assertion$\mathcal { D } ( \sigma , \omega )$, with$\# \mathbb { T } _ { \tau } ^ { T _ { \rho } } =$ $| T _ { \tau } ^ { T _ { \rho } } | ^ { - 1 }$

Finally, by Item$( \mathrm { i v } )$, the$\delta$tubes inside each τ tube satisfy the hypothesis of Assertion$\mathcal { E } ( \sigma , \omega ^ { \prime } )$，and thus for each$\tau$tube$T _ { \tau }$we obtain the volume estimate

$$
\Big | \bigcup_ {T ^ {T _ {\tau}} \in \mathbb {T} ^ {T _ {\tau}}} T ^ {T _ {\tau}} \Big | \gtrsim \Big (\frac {\delta}{\tau} \Big) ^ {\omega^ {\prime}} (\# \mathbb {T} [ T _ {\tau} ]) ^ {\sigma / 2} | T ^ {T _ {\tau}} | ^ {\sigma}.\tag{2.7}
$$

If the$\tau$tubes are evenly distributed among$\rho$tubes, and the$\delta$tubes are evenly distributed among the$\tau$tubes, then we may suppose that for each$\tau$tube$T _ { \tau }$and each$\rho$tube$T _ { \rho } ,$we have $( \# \mathbb { T } ^ { T _ { \tau } } ) ( \# \mathbb { T } _ { \tau } ^ { T _ { \rho } } ) ( \# \mathbb { T } _ { \rho } ) = \# \mathbb { T }$. Thus we can combine (2.5), (2.6), and (2.7) to obtain the following analogue of (2.4):

$$
\begin{array}{r l} & {\Big | \bigcup_ {T \in \mathbb {T}} T \Big | \gtrsim \Big (\frac {\tau}{\rho} \Big) ^ {\omega - \omega^ {\prime}} \delta^ {\omega^ {\prime}} (\# \mathbb {T}) ^ {\sigma / 2} | T | ^ {\sigma}} \\ & {\qquad = \Big (\frac {\tau}{\rho} \Big) ^ {\omega - \omega^ {\prime}} \delta^ {\omega^ {\prime}} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 3 / 2} (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma},} \end{array}\tag{2.8}
$$

where the second equality used Item (i). By Item$\mathrm { ( v ) }$we have$\tau / \rho < \delta ^ { \zeta }$, and thus we obtain (2.1) with$\alpha = \zeta ( \omega ^ { \prime } - \omega )$, as desired.

To prove Lemma 6.4 (and hence Proposition 1.6), we show that for every arrangement of$\delta$ tubes, at least one of the following must hold.

(A) There is a set of$\rho$tubes satisfying Items$\mathrm { ( a ) \mathrm { ~ - ~ } \mathrm { ( d ) } }$above.

(B) There are sets of$\tau$and$\rho$tubes satisfying Items${ \mathrm { ( i ) \mathrm { \Omega } - \mathrm { ( v ) } } }$above.

(C) The tubes in$\mathbb { T }$can be eficiently packed inside rectangular prisms of dimensions$s \times t \times 1$，with$s \ll t$

(D) The tubes in T satisfy the Frostman Convex Wolf Axioms at every scale (see Definition 6.1).

To establish the above polychotomy, in Section 4 we develop a general theory for “factoring” collections of convex sets in$\mathbb { R } ^ { n }$. Given a set of$\delta$tubes T, this allows us to find a collection of convex sets W that satisfies the analogues of Items (a) and (b) above with W in place of$\mathbb { T } _ { \rho } .$If these convex sets have dimensions$s \times t \times 1$with$s \ll t .$, then this gives us Item (C). If instead$s \sim t ,$ then the convex sets in W are almost tubes. We apply arguments of this type at several carefully chosen scales to show that at least one of Items$\mathrm { ( A ) - ( D ) }$must hold.

The arguments described thus far establish the desired inequality (2.1) in the case where$\mathrm { ( A ) }$ or (B) holds. In Section 5 we show that Inequality (2.1) holds in Case (C); this is done using a careful rescaling argument. Finally, Case (D) is precisely the setting where we can apply the Sticky Kakeya Theorem (as generalized in [26]) to immediately conclude that T satisfies (2.1).

This concludes the proof sketch of Proposition 1.6. We now turn to Proposition 1.7.

## 2.2 A two-scale grains decomposition

In Sections 7 and 8, we study the structure of arrangements of$\delta$tubes for which the estimate (1.2) from Assertion$\mathcal { D } ( \sigma , \omega )$is (almost) tight, i.e. sets of$\delta$tubes that satisfy the hypotheses of Assertion $\mathcal { D } ( \sigma , \omega )$, and also satisfy an inequality of the form

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \lesssim \delta^ {\omega} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.
$$

We will assume for now that such a set$\mathbb { T }$exists, and at the end of Section 2 we will arrive at a contradiction. With care, this contradiction will remain when the term$\delta ^ { \omega }$is replaced by$\delta ^ { \omega - \nu }$for $\nu > 0$a small positive number.

In [9], Guth proved that under mild “broadness” hypotheses, every union of δ tubes$\cup _ { \mathbb { T } } T$in $\mathbb { R } ^ { 3 }$can be written as a disjoint union of rectangular prisms of dimensions$\delta \times c \times c ,$with$c \geq$ $( ( \# \mathbb { T } ) | T | ^ { 1 / 2 } ) ^ { - 1 }$; see Figure 2 (left). This lower bound on$c$is interesting when #T is substantially smaller than$| T | ^ { - 1 }$(recall that |T| has size roughly$\delta ^ { 2 } )$. At the opposite extreme, if$\# \mathbb { T }$has size about$| T | ^ { - 1 / 2 }$(this is the smallest possible cardinality for T that is allowable, given the broadness hypotheses mentioned above), then grains have dimensions roughly$\delta \times 1 \times 1$. We remark that Guth’s methods also yield a stronger bound of the form$c \geq \mu ( ( \# \mathbb { T } ) | T | ^ { 1 / 2 } ) ^ { - 1 }$, where$\mu$is the number of tubes from T that pass through a typical point, but this stronger bound won’t be needed here.

First, we show that there exists a scale$\delta \ll \rho \ll 1$and a set of$\rho$tubes$\mathbb { T } _ { \rho }$so that both$\mathbb { T } _ { \rho }$and the rescaled sets$\mathbb { T } ^ { T _ { \rho } }$(recall (1.8)) satisfy the hypotheses of Assertion$\mathcal { D } ( \sigma , \omega )$. In addition, each rescaled set$\mathbb { T } ^ { T _ { \rho } }$satisfies the broadness hypotheses needed to apply (a variant of) Guth’s result. Thus we can write$\mathsf { U } _ { \mathbb { T } [ T _ { \rho } ] } T ^ { T _ { \rho } }$as a disjoint union of rectangular prisms of dimensions$\delta / \rho \times c \times c ,$ where$c \geq ( ( \# \mathbb { T } [ T _ { \rho } ] ) | \bar { T } ^ { \bar { T } _ { \rho } } | ^ { 1 / 2 } ) ^ { - 1 }$. Note that the grains become larger as$\# \mathbb { T } [ T _ { \rho } ]$becomes smaller; this numerology will be important later in the argument. Undoing the scaling, we obtain a partition of$\cup _ { \mathbb { T } [ T _ { o } ] } T$into disjoint$\delta \times \rho c \times c$rectangular prisms; we will refer to these as grains (see Figure 2 (right)), and we refer to this set of grains as$\mathcal { G } _ { T _ { \rho } }$. Let$\begin{array} { r } { \mathcal { G } = \bigcup _ { \mathbb { T } _ { \rho } } \mathcal { G } _ { T _ { \rho } } } \end{array}$. In our discussion below, we will call G the “two scale Guth grains decomposition” of T.

Recall that in the proof vignette outlines in Section 1.5, we made Simplifying Assumption D. We will now dicuss the technical steps needed to justify this assumption. The main goal of Section 7 is to define three “Moves,” which we will briefly describe below. After these moves have been applied, we obtain a new scale$\rho$with$\delta \ll \rho \ll 1 ;$a new set of$\rho$tubes$\mathbb { T } _ { \rho }$that cover$\mathbb { T } ;$and a new collection$\mathcal { G }$of grains that have the following properties:

(i) Each grain has dimensions$\delta \times \rho c \times c ,$with$c \geq ( ( \# \mathbb { T } [ T _ { \rho } ] ) | T ^ { T _ { \rho } } | ^ { 1 / 2 } ) ^ { - 1 }$

(ii) Each grain$G \in { \mathcal { G } }$is associated to a unique tube$T _ { \rho } \in \mathbb { T } _ { \rho }$, where$G \subset T _ { \rho }$, and both$G$and$T _ { \rho }$ point in the same direction (up to uncertainty$\rho )$

(iii) Distinct grains from$\mathcal { G }$associated to the same$\rho$tube are disjoint.

(iv) For each$\rho$tube$T _ { \rho } ,$, we have$\begin{array} { r } { \bigcup G = \bigcup _ { T \in \mathbb { T } [ T _ { \rho } ] } T } \end{array}$, where the former union is taken over the set of grains associated to$T _ { \rho }$

(v) Grains associated to diferent$\rho$tubes can intersect, but this intersection must be tangential; i.e. the tangent planes of intersecting grains must agree up to uncertainty$\delta / ( \rho c )$.

Item (v) means that we can cover$\mathbb { R } ^ { 3 }$by boxes of dimensions$\begin{array} { r } { \frac { \delta } { \rho } \times \boldsymbol { c } \times \boldsymbol { c } , } \end{array}$so that each grain is contained $O ( 1 )$boxes, and two grains intersect only if they are contained in a common box. If we re-scale a box to become the unit cube, then the grains inside this box become$\rho \times \rho \times 1$rectangular prisms, i.e.$\rho$tubes (see Figure 2). We introduce the following notation: If □ is a$\frac { \delta } { \rho } \times c \times c$box, then$\mathcal { G } ^ { \boxed { \varPsi } }$will denote the set of ρ-tubes obtained by re-scaling the grains from$\mathcal { G }$inside$\bigsqcup$. With this notation, we can state one final property for$\mathcal { G } \mathrm { : }$

(vi) For each box$\sqsubseteq ,$the$\rho$tubes in$\mathcal { G } ^ { \boxed { \varPsi } }$satisfy the hypotheses of$\mathcal { E } ( \sigma , \omega )$, and$C _ { K T - C W } ( \mathcal { G } ^ { \perp } ) \lessapprox 1$

In a moment, we will describe the Moves needed to find a scale$\rho ;$a set of$\rho$tubes$\mathbb { T } _ { \rho } ;$and a set of grains$\mathcal { G }$that satisfy Items$\mathrm { ( i ) ~ - ~ ( v i ) }$. We begin by letting$\mathcal { G }$be the two scale Guth grains decomposition of$\mathbb { T } _ { : }$as described above. Items (i), (ii), (iii), and (iv) hold for this choice of$\mathcal { G }$, and properties$( \mathrm { i i } ) { - } ( \mathrm { i v } )$are preserved throughout the process.

If Item (v) fails at any point in the process, then we argue by contradiction as follows. Using a $L ^ { 2 }$argument similar to Cordoba’s proof of the Kakeya maximal function conjecture in the plane, we can show that there exists some scale$\tilde { \delta } \gg \delta$so that the “hairbrush” of a typical grain G $( \mathrm { i . e . }$. the union of the grains$G ^ { \prime } \in { \mathcal { G } }$with$G ^ { \prime } \cap G \neq \emptyset )$fills out (most of) the <sup>˜</sup>δ-neighbourhood of $G$. Let us pretend that the hairbrush fills out all of the$\tilde { \delta }$neighbourhood of$G .$. Then for each$\delta$ tube$T \in \mathbb { T }$, the corresponding$\tilde { \delta }$tube$\tilde { \cal T } = { \cal N } _ { \tilde { \delta } } ( T )$satisfies$\tilde { T } \subset \bigcup _ { T ^ { \prime } \in \mathbb { T } } T ^ { \prime }$. Thus we can replace our original collection of$\delta$tubes with a new collection$\tilde { \mathbb { T } }$of fatter$\tilde { \delta }$tubes, and$\textstyle \bigcup _ { \mathbb { T } } T = \bigcup _ { \tilde { \mathbb { T } } } { \tilde { T } } .$. The new collection of fatter tubes will satisfy the hypotheses of$\mathcal { E } ( \sigma , \omega )$(with favorable values of$C _ { K T - C W } ( \tilde { \mathbb { T } } )$ and$C _ { F - S W } ( \tilde { \mathbb { T } } ) ) ,$, and hence we can apply the estimate$\mathcal { E } ( \sigma , \omega )$to T<sup>˜</sup> and obtain a volume estimate for$\left| \bigcup _ { \mathbb { T } } T \right|$that is superior to the estimate coming from Assertion$\mathcal { D } ( \sigma , \omega )$. But this contradicts the assumption that the volume estimate from Assertion$\mathcal { D } ( \sigma , \omega )$was sharp for$\mathbb { T } .$

We will now describe the three Moves alluded to above. For ease of exposition, it will be helpful to introduce these Moves in the opposite order that they are defined in Section$8 .$

Move #3 handles the situation when Item (vi) fails (recall the Assertion$\mathcal { D } ( \sigma , \omega )$is sharp for $\mathbb { T } )$. Using an$L ^ { 2 }$argument, we show that the hairbrush of each grain$G \in { \mathcal { G } }$fills out (most of) a wider grain${ \tilde { G } } \supset G ;$these wider grains have the same “length”$c ,$but a substantially larger value of$\rho .$See Figure 14 for a visual depiction of this step.

Unfortunately, after applying Move$\# 3$, it might be the case that$\rho$has become so large that the inequality$\rho \ll 1$is no longer true. Move$\# 2$handles this situation. Move$\# 2$uses a$L ^ { 2 }$argument to find a new set of grains with a new (substantially larger) length$^ { c , }$and a new$\rho$that satisfies $\delta \ll \rho \ll 1$. See Figure 10 for a visual depiction of this step.

Finally, whenever the value of$\rho$changes, so does the quantity$( ( \# \mathbb { T } [ T _ { \rho } ] ) | T ^ { T _ { \rho } } | ^ { 1 / 2 } ) ^ { - 1 }$. Thus after applying Moves #2 or #3, it might be the case that$( ( \# \mathbb { T } [ T _ { \rho } ] ) | T ^ { T _ { \rho } } | ^ { 1 / 2 } ) ^ { - \mathrm { i } }$has become much larger than$^ { c , }$and hence Item (i) fails. Move #1 handles this case: we throw away our set$\mathcal { G }$and replace it with the two scale Guth grains decomposition of T that was described above (both Moves #2 and $\# 3$maintain the broadness condition needed to invoke the two scale Guth grains decomposition of T). This gives us a new grains decomposition with the same value of$\rho$and a substantially larger value of c.

Each of Moves #1, #2, and #3 can be applied to ensure that$\mathcal { G }$satisfies (some of) the Properties $\mathrm { ( i ) ~ - ~ ( v i ) }$described above. Unfortunately, the application of Move #1, #2, or #3 might destroy other Properties. However, each Move either substantially increases the “length” c of the grains, or maintains the length and substantially increases the value of$\rho .$Since c and$\rho$are bounded above by 1, the process of applying Moves #1, #2, and #3 must halt after a bounded number of steps. The resulting grains decomposition satisfies Properties$( \mathrm { i } ) - ( \mathrm { v i } )$

## 2.3 Refined induction on scales

In Section 9 we use the two-scale grains decomposition from Section$7$to apply the estimate from Assertion$\mathcal { E } ( \sigma , \omega )$at two diferent scales — once to the (rescaled) δ tubes inside each$\rho$tube, and once to the$\rho$tubes arising as the re-scaled grains inside each box □, i.e. to each arrangement$\mathcal { G } ^ { \boxed { \varPsi } }$ This is a critical step in the proof of Proposition 1.7, and the entire proof up to this point was carefully structured in order to allow us to apply the estimate$\mathcal { E } ( \sigma , \omega )$to$\mathcal { G } ^ { \boxed { \varPsi } }$

The argument is as follows. Suppose that T is a set of$\delta$tubes for which the estimate from Assertion$\mathcal { D } ( \sigma , \omega )$is tight, and let$\mathbb { T } _ { \rho }$and$\mathcal { G }$be the grains decomposition described in the previous section. Employing a small white lie, we can suppose that there is a number$\mu$so that each point $x \in \bigcup _ { \mathbb { T } } T$is contained in$\sim \mu$tubes from T. We have$| \mathsf { U _ { \mathbb { T } } } T | \sim \mu ^ { - 1 } ( \# \mathbb { T } ) | T |$, so our goal is to obtain an upper bound for$\mu .$. We will suppose there is a number$\mu _ { \mathrm { f i n e } }$so that for each$T _ { \rho }$, each point$x \in \textstyle \bigcup _ { \mathbb { T } [ T _ { \rho } ] } T$is contained in$\sim \mu _ { \mathrm { { f i n e } } }$tubes from$\mathbb { T } [ T _ { \rho } ]$. Finally, we will suppose there is a number$\mu _ { \mathrm { c o a r s e } }$so that each point$x \in \bigcup _ { \mathbb { T } } T = \bigcup _ { G \in \mathcal { G } } G$is contained in about$\mu _ { \mathrm { c o a r s e } }$grains from${ \mathcal { G } } .$. By Items (ii) and$( \mathrm { i v } )$from Section 2.2, we have$\mu \lesssim \mu _ { \mathrm { f i n e } } \mu _ { \mathrm { c o a r s e } }$, and thus our task is to estimate the latter two quantities.

Since each rescaled set$\mathbb { T } ^ { T _ { \rho } }$satisfies the hypotheses of Assertion$\mathcal { D } ( \sigma , \omega )$, we have the estimate

$$
\mu_ {\text { fine }} \lesssim (\delta / \rho) ^ {- \omega} \left(\# \mathbb {T} [ T _ {\rho} ] | T ^ {T _ {\rho}} | ^ {1 / 2}\right) ^ {\sigma},\tag{2.9}
$$

where$\# \mathbb { T } [ T _ { \rho } ]$has size roughly$( \# \mathbb { T } ) / ( \# \mathbb { T } _ { \rho } )$and$| T ^ { T _ { \rho } } | = | T | / | T _ { \rho } |$

Our next task is to estimate$\mu _ { \mathrm { c o a r s e } }$. We apply$\mathcal { E } ( \sigma , \omega )$to each set of$\rho$tubes$\mathcal { G } ^ { \boxed { \varPsi } }$. (We must use the estimate$\mathcal { E } ( \sigma , \omega )$rather than$\mathcal { D } ( \sigma , \omega )$, since$C _ { F - S W } ( \mathcal { G } ^ { \sharp } )$might be large, which entails a separate argument. We will gloss over this issue.) Doing so gives the estimate

$$
\mu_ {\mathrm{coarse}} \lesssim \rho^ {- \omega} \big ((\# \mathcal {G} ^ {\square}) | T _ {\rho} | ^ {1 / 2} \big) ^ {\sigma} \lesssim \rho^ {- \omega} | T _ {\rho} | ^ {- \sigma / 2}.\tag{2.10}
$$

The second inequality in (2.10) follows from the fact that$C _ { K T - C W } ( \mathcal { G } ^ { \perp } ) \lessapprox 1$, and hence$\# \mathcal { G } ^ { \perp } \lessapprox$ $| T _ { \rho } | ^ { - 1 }$. Combining (2.9) and (2.10), we conclude that

$$
\mu \lessapprox \left[ \delta^ {- \omega} \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {\sigma} \right] \left[ | T _ {\rho} | (\# \mathbb {T} _ {\rho}) \right] ^ {- \sigma}.\tag{2.11}
$$

The first term in square brackets is the estimate that would follow from applying Assertion $\mathcal { D } ( \sigma , \omega )$directly to T. Thus (2.11) yields a superior estimate precisely when$\# \mathbb { T } _ { \rho } \gg | T _ { \rho } | ^ { - 1 }$. Since we assumed that T is a set of tubes for which$\mathcal { D } ( \sigma , \omega )$is tight, we conclude that$\# \mathbb { T } _ { \rho } \lessapprox | T _ { \rho } | ^ { - 1 }$

The above step was simplified to highlight the main ideas. In reality, we actually need (and prove) a slightly stronger statement: rather than concluding that$\# \mathbb { T } _ { \rho } \lessapprox | T _ { \rho } | ^ { - 1 }$, we must instead arrive at the estimate$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) \lessapprox 1$. This more dificult estimate is obtained as follows. Suppose to the contrary that$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) \gg 1$. Then we can find a convex set$W$so that$\mathbb { T } _ { \rho } [ W ]$has cardinality much larger than$| W | / | T _ { \rho } |$(in fact, we can find many such sets W—see Proposition 4.6). The argument described above is the special case when$W$is comparable to the unit ball. The general case introduces technical challenges, but in light of the techniques already developed in Sections 4 and 5 to prove Proposition 1.6 (see the discussion at the end of Section 2.1), it does not require any additional new ideas.

## 2.4 Multi-scale structure, Nikishin-Stein-Pisier factorization, and Sticky Kakeya

Let us summarize the conclusion of the previous steps: if$\mathbb { T }$is a set of$\delta$tubes for which the estimate $\mathcal { D } ( \sigma , \omega )$is tight, then there is a scale$\delta \ll \rho \ll 1$and a set of$\rho$tubes$\mathbb { T } _ { \rho }$with$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) \lessapprox 1$ so that both$\mathbb { T } _ { \rho }$and each (rescaled) set$\mathbb { T } [ T _ { \rho } ]$satisfy the hypotheses of Assertion$\mathcal { D } ( \sigma , \omega )$, and furthermore, the estimate$\mathcal { D } ( \sigma , \omega )$is tight for all of these arrangements of tubes.

This last conclusion means that we can iteratively apply the same argument to both$\mathbb { T } _ { \rho }$and each (rescaled) set$\mathbb { T } [ T _ { \rho } ]$. After some pruning, we conclude that there is a sequence of closely spaced scales$\delta = \rho _ { N } < \rho _ { N - 1 } < . . . < \rho _ { 0 } = 1$and sets$\{ \mathbb { T } _ { \rho _ { i } } \} _ { i = 1 } ^ { N }$covering T, with$C _ { K T - C W } ( \mathbb { T } _ { \rho _ { i } } ) \lessapprox 1$for each index i.

We would like to apply the Sticky Kakeya Theorem to conclude that$| \cup _ { \mathbb { T } } T |$is almost as large as$\sum _ { \mathbb { T } } | T |$. Indeed, the situation described above almost matches the setup of the Sticky Kakeya Theorem, as generalized in [26, Theorem 1.8]. Specifically, T would satisfy the hypotheses of [26, Theorem 1.8]$\mathrm { i f } \# \mathbb { T } \approx \delta ^ { - 2 }$. Since$C _ { K T - C W } ( \mathbb { T } ) \lessapprox 1$, we know that$\# \mathbb { T } \lessapprox \delta ^ { - 2 }$. Unfortunately, however, it could be the case that$\# \mathbb { T }$is much smaller than$\delta ^ { - 2 }$

In Section 10 we use a Nikishin-Stein-Pisier factorization argument to show that if$\# \mathbb { T } \ll \delta ^ { - 2 }$ then we can construct a new set$\hat { \mathbb T }$consisting of a union of about$\delta ^ { - 2 } ( \# \mathbb { T } ) ^ { - 1 }$randomly translated and rotated copies of$\mathbb { T } .$. This new set$\hat { \mathbb T }$will have cardinality about$\delta ^ { - 2 }$. Just like the original set$\mathbb { T } ,$ the new set$\hat { \mathbb T }$will have a sequence of covers$\{ \hat { \mathbb { T } } _ { \rho _ { i } } \} _ { i = 1 } ^ { N }$with$C _ { K T - C W } ( \hat { \mathbb { T } } _ { \rho _ { i } } ) \lessapprox 1$1 for each index i. Hence we can apply the Sticky Kakeya Theorem to$\hat { \mathbb T }$to conclude that$| \cup _ { T \in \hat { \mathbb { T } } } T | \gtrapprox 1$. Since the volume of $\cup _ { \mathbb { T } } T$is invariant under translation and rotation (this is a key ingredient for Nikishin-Stein-Pisier factorization), we conclude that

$$
\big | \bigcup_ {T \in \mathbb {T}} T \big | \gtrsim (\# \mathbb {T}) | T |.\tag{2.12}
$$

But if$\sigma , \omega > 0$, then (2.12) contradicts the assumption that the estimate$\mathcal { D } ( \sigma , \omega )$is tight for $\mathbb { T } .$We conclude that when$\sigma , \omega > 0$, there does not exist any set$\mathbb { T }$satisfying the hypotheses of Assertion$\mathcal { D } ( \sigma , \omega )$for which the estimate$\mathcal { D } ( \sigma , \omega )$is tight. The quantitative version of this statement is Proposition 1.7.

## 3 Notation

In the arguments that follow,$\delta > 0$will denote a small positive quantity. Overriding the (informal) notation from Sections 1 and 2, we write$A ( \delta ) \lessapprox \delta B ( \delta )$if for all$\varepsilon > 0$, there exists$K _ { \varepsilon } \ > \ 0$so that$A ( \delta ) \leq K _ { \varepsilon } \delta ^ { - \varepsilon } B ( \delta )$. If the role of$\delta$is apparent from context, we will often write$A \lessapprox B$. For example if K is a constant independent of$\delta ,$then$\log ( 1 / \delta ) ^ { K } \lessapprox 1$. Similarly,$e ^ { \sqrt { \log { 1 / \delta } } } \lessapprox 1$

In some sections of the paper, it will ease notation to fix certain variables (for example the values of$\sigma$and$\omega$from Definition 1.5). In such cases, we will clearly state which variables are fixed, and use bold font throughout that section to denote these fixed variables, and also to denot quantities that depend only on fixed variables. For example we might define$\beta = \sigma \omega / 1 0 0$

## 3.1 Convex sets and shadings

In the introduction, we defined a δ-tube to be the δ neighbourhood of a unit line segment. There are several other types of convex sets that will make frequent appearances in our arguments. A prism is a rectangular prism in$\mathbb { R } ^ { n }$(usually$\mathbb { R } ^ { 3 } )$; we will denote the dimensions by$\quad a \times b \times c \times \ldots ,$ with the convention that$a \leq b \leq c \leq . . . .$Informally, we say a prism in$\mathbb { R } ^ { 3 }$is$\mathrm { ^ { 6 6 } f l a t } ^ { 9 }$if it has dimensions$a \times b \times c$with$a \ll b .$, and we say it is “square” if b and c have comparable size. Finally, we will sometimes refer to the quantities$a , b ,$and c respectively as the “thickness,” “width,” and “length” of a prism.

Rather than working with rectangular prisms, it will sometimes be convenient to work with ellipsoids, or more general convex sets. This motivates the following definition, which generalizes the definition of$( \mathbb { T } , Y ) _ { \delta }$from the introduction.

Definition 3.1. For$0 < a \leq b \leq c .$we write$( { \mathcal { P } } , Y ) _ { a \times b \times c }$to denote the following pair: P is a set of essentially distinct convex subsets of$\mathbb { R } ^ { 3 } \colon$; for each$P \in { \mathcal { P } }$, the outer John ellipsoid of P has axes of lengths comparable to$a , b ,$, and c respectively.$Y$is a shading on$\mathcal { P }$, i.e. for each$P \in \mathcal { P }$, we have $Y ( P ) \subset P$

For example, we could write$( \mathbb { T } , Y ) _ { \delta }$as$( \mathbb { T } , Y ) _ { \delta \times \delta \times 1 }$. Finally, we say$( { \mathcal { P } } , Y ) _ { a \times b \times c }$is λ dense if $\begin{array} { r } { \sum _ { P \in \mathcal { P } } | Y ( P ) | \ge \lambda \sum _ { P \in \mathcal { P } } | P | } \end{array}$

Definition 3.2. If$( { \mathcal { P } } , Y ) _ { a \times b \times c }$is a set of prisms and their associated shading and$\boldsymbol { x } \in \mathbb { R } ^ { 3 }$, we define

$$
\mathcal {P} _ {Y} (x) = \{P \in \mathcal {P}: x \in Y (P) \}.
$$

Similarly, if P is a set of prisms (or more generally, convex sets) and no shading is present, then we define${ \mathcal { P } } ( x ) = \{ P \in { \mathcal { P } } \colon x \in P \}$

Definition 3.3. We say a pair$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times c }$is a t-refinement of$( \mathcal { P } , Y ) _ { a \times b \times c } \mathrm { i f } \mathcal { P } ^ { \prime } \subset \mathcal { P } ; Y ^ { \prime } ( P ) \subset Y ( P )$ for each$P \in \mathcal { P } ^ { \prime }$, and$\begin{array} { r } { \sum _ { P ^ { \prime } \in \mathcal { P } ^ { \prime } } | Y ^ { \prime } ( P ^ { \prime } ) | \geq t \sum _ { P \in \mathcal { P } } | Y ( P ) | } \end{array}$|. In practice, we will often have$t \approx _ { \delta } 1$, in which case we will call it$\mathrm { ~ a ~ } { \approx } \delta$1 refinement.

Note that if$( { \mathcal { P } } , Y ) _ { a \times b \times c }$is λ dense and$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times c }$is a t-refinement, then$\# \mathcal { P } ^ { \prime } \geq \lambda t ( \# \mathcal { P } )$

Definition 3.4. If$W \subset \mathbb { R } ^ { 3 }$is a convex set whose outer John ellipsoid E has dimensions$a \times b \times c ,$we write dir$( W ) \in \mathrm { G r } ( 1 ; \mathbb { R } ^ { 3 } )$and$\Pi ( W ) \in \operatorname { G r } ( 2 ; \mathbb { R } ^ { 3 } )$to denote the 1 and 2-dimensional subspaces of $\mathbb { R } ^ { 3 }$spanned by the primary and secondary axes of E. We have that dir(W) is meaningfully defined up to accuracy$b / c _ { \mathrm { : } }$, and$\Pi ( W )$is meaningfully defined up to accuracy$a / b$. For example, if$T$is a$\delta$tube, then$\mathrm { d i r } ( T )$is meaningfully defined up to accuracy$\delta ,$while$\Pi ( T )$is only meaningfully defined up to accuracy$\mid ( \mathrm { i . e . } \Pi ( T )$is not a meaningful quantity if$T$is a δ tube).

We will employ the following synecdoche notation: if P (resp. T, W, etc.) is a collection of convex sets, each of the same volume, then we will use$| P |$(resp. |T|, |W|, etc) to denote the volume of one of these convex sets. In practice, we will abuse notation slightly and continue to employ this notation if the sets in$\mathcal { P }$have comparable (but not necessarily identical) volume.

Definition 3.5. Let$W \subset \mathbb { R } ^ { n }$be a convex set. We define$\phi _ { W } \colon \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$to be an afine-linear transformation that maps the outer John ellipsoid of$W$to the unit ball. For concreteness, if $v _ { 1 } , \ldots , v _ { n }$are the axes of the John Ellipsoid, with lengths$\ell _ { 1 } \leq \ldots \leq \ell _ { n } .$, then we select ϕ<sub>W</sub> so that the j-th axis of the John Ellipsoid is mapped to the$x _ { j }$axis in$\mathbb { R } ^ { n }$. If two more more axes have the same length, then we pick an ordering arbitrarily.

If$U \subset \mathbb { R } ^ { n }$, we define$U ^ { W } = \phi _ { W } ( U )$. In particular, if U is a convex subset of W then$U ^ { W }$is a convex subset of the unit ball, and$| \dot { U } ^ { \dot { W } } | \sim | U | / | W |$. This is compatible with our earlier definition of$T ^ { T _ { \rho } }$from (1.8).

Definition 3.6. Let U be a collection of convex subsets of$\mathbb { R } ^ { n }$and let W be a convex subset of$\mathbb { R } ^ { n }$ We define

$$
\mathcal {U} [ W ] = \{U \in \mathcal {U}: U \subset W \},
$$

and

$$
\mathcal {U} ^ {W} = \{U ^ {W}: U \in \mathcal {U} [ W ] \}.
$$

If Y is a shading on$u ,$we will use$Y ^ { W }$to denote the corresponding shading on$\mathcal { U } ^ { W }$, i.e. for each$U ^ { W } \in \mathcal { U } ^ { W }$, we define$Y ^ { W } ( U ^ { W } ) = \phi _ { W } ( Y ( U ) )$.

Remark 3.7. The expression$\mathcal { U } ^ { W }$should not be confused with$\mathcal { U } _ { W } ;$the latter notation will be as follows: If U and W are sets of convex subsets of$\mathbb { R } ^ { n }$, then$\mathcal { U } _ { W } , ~ W \in \mathcal { W }$will be used to denote a set of subsets of U that are indexed by the elements of W.

## 3.2 Table of notation

To aid the reader, we will use certain notation conventions throughout this paper. For example, some symbols (such as σ and$\omega )$will be reserved to always have the same meaning. For future reference, we record these notation conventions in the table below

| Symbol | Meaning |
| --- | --- |
| $\delta, \rho, \tau$ | These variables will denote scales. Typically $\delta \leq \rho \leq \tau$. |
| $a, b, c$ | These variables will denote scales; typically the dimensions of a prism. |
| $\theta$ | $\theta$ will denote an angle |
| $\varepsilon, \eta, \zeta, \alpha$ | These variables will represent (typically small) exponents, i.e. they will appear in the form $\delta^{\eta}, \rho^{\varepsilon}$, etc. |
| $\kappa, K$ | These variables will represent (positive) multiplicative constants, i.e. $\|\bigcup T\| \geq \kappa \delta^{\varepsilon}$ or $C_{KT-CW}(\mathbb{T}) \leq K \delta^{-\eta}$. Typically $\kappa > 0$ is small and $K \gg 1$ is large. |
| $\sigma, \omega$ | $\sigma$ and $\omega$ and their variants $\sigma', \tilde{\sigma}$, etc. will always be quantities related to the estimates $\mathcal{E}(\sigma, \omega)$ and $\mathcal{D}(\sigma, \omega)$. |
| $\sigma, \omega$ | In Sections 7 and 8, we will fix values of $\sigma$ and $\omega$ that are kept constant throughout that section. We use bold symbols to denote these fixed numbers, and all subsequent quantities that depend (only) on them. |
| $T, P, G, S, \Box$ | These variables will denote convex sets. Typically $T$ is a tube, $P$ and $G$ are prisms of dimensions $a \times b \times c$, $S$ is a slab, and $\Box$ is a “box” of dimensions $a \times c \times c$. We use symbols $\mathbb{T}, \mathcal{P}, \mathcal{G}, \mathcal{S}$ to denote sets of such objects. |
| $\mathbb{T}', \mathbb{T}_1, \tilde{\mathbb{T}}$ | $\mathbb{T}'$ or $\mathbb{T}_1$ will denote a subset of $\mathbb{T}$. Similarly $\mathbb{T}_2$ will denote a subset of $\mathbb{T}_1$, etc. $\tilde{\mathbb{T}}$ will denote a new set of tubes that is related to $\mathbb{T}$, but not necessarily a subset (for example, $\tilde{\mathbb{T}}$ might consist of the 2-fold dilates of the tubes in $\mathbb{T}$). |
| $(\mathbb{T}', Y')_\delta$ | $(\mathbb{T}', Y')_\delta$ will denote a refinement of $(\mathbb{T}, Y)_\delta$. Similarly for $(\mathbb{T}_1, Y_1)_\delta$. |

## 4 Wolf Axioms and Factoring Convex Sets

## 4.1 Definitions: Wolf axioms and covers

Definition 4.1. Let U, W be collections of convex sets in$\mathbb { R } ^ { n }$

(A) We say that W is a cover of U (or W covers U) if$\cup _ { W \in \mathcal { W } } \mathcal { U } [ W ] = \mathcal { U }$. We will denote this by $\mathcal { U } \prec \mathcal { W }$

(B) We say that W is a K-almost partitioning cover (resp. partitioning cover) if it is a cover, and furthermore each$U \in \mathcal { U }$is contained in at most K sets (resp. 1 set) of the form$\mathcal { U } [ W ]$

(D) We say that W is a K-balanced cover (resp. balanced cover) if it is a cover, and furthermore the numbers$\begin{array} { r } { | W | ^ { - 1 } \sum _ { U \in \mathcal { U } [ W ] } | U | } \end{array}$are comparable for all$W \in { \mathcal { W } }$, up to a multiplicative factor of K (resp. 2).

The following is a mild generalization of Definition 1.3.

Definition 1.3<sup>′</sup>. Let U and W be collections of convex subsets of$\mathbb { R } ^ { n }$.

(A) We define the Katz-Tao Wolf constant of U with respect to W to be the infimum of all$C > 0$ so that

$$
\sum_ {U \in \mathcal {U} [ W ]} | U | \leq C | W | \quad f o r a l l W \in \mathcal {W}.\tag{4.1}
$$

(B) We define the Frostman Wolf constant of U with respect to W to be the infimum of all$C > 0$ so that

$$
\sum_ {U \in \mathcal {U} [ W ]} | U | \leq C | W | \sum_ {U \in \mathcal {U}} | U | \quad f o r a l l W \in \mathcal {W}.\tag{4.2}
$$

Remark 4.2.

(A) To ease notation, we define$C _ { K T - C W } ( \mathcal { U } )$(resp.$C _ { F - C W } ( \mathcal { U } ) )$to be the Katz-Tao (resp. Frostman) Wolf constant of U associated to the set W of convex subsets of$\mathbb { R } ^ { n }$. We define$C _ { F - S W } ( \mathcal { U } )$to be the Frostman Wolf constant of U associated to the set$\mathcal { W }$of slabs in$\mathbb { R } ^ { n }$. Note that these definitions are compatible with those from Definition 1.3.

(B) A set T of δ-tubes obeys the Wolf axioms, in the sense of [27] (see Property (∗) on p655 and the preceding discussion) if the Katz-Tao Wolf constant of T is small with respect to the set W consisting of all rectangular prisms of dimensions 10δ$\times \rho \times \ldots \times \rho \times 2$, with$0 < \delta \leq \rho \leq 2$

(C) For some arguments, it will be useful to consider an analogue of the above definitions where the quantity$| W |$on the RHS of (4.1) is replaced by$| W \cap B ( 0 , 1 ) | / | B ( 0 , 1 ) |$|, and similarly for (4.2). This leads to a quantity that transforms naturally under afine maps such as ϕ<sub>W</sub> from Definition 3.5.

(D) Note that the above definitions continue to make sense if U is a multiset. This will be useful in Section 10.1.

(E) If the set$\mathcal { U } \ne \emptyset$consists of convex sets of the same size, then$C _ { F - C W } ( \mathcal { U } ) \leq C$implies that $\# \dot { \mathcal { U } } \geq C ^ { - 1 } | U | ^ { - 1 }$. To see this, take W to be a convex set in U. Then the LHS of (4.2) equals to |U| while the RHS of (4.2) equals to$C | U | ^ { 2 } ( \# u )$. Roughly speaking, if$C _ { K T - C W } ( \mathcal { U } )$is small, then U is “sparse”, while if$C _ { F - C W } ( \mathcal { U } )$is small, then U is “dense.”

## Remark 4.3.

(A) The Frostman Wolf constant is “inherited upwards” by covers. More precisely, if U and W are collections of convex subsets of$\mathbb { R } ^ { n }$, and if W is a K-balanced cover of$u ,$then

$$
C _ {F - C W} (\mathcal {W}) \lesssim K C _ {F - C W} (\mathcal {U}) \quad \text { and } \quad C _ {F - S W} (\mathcal {W}) \lesssim K C _ {F - S W} (\mathcal {U}).\tag{4.3}
$$

(B) The Katz-Tao Wolf constant is “inherited downwards” by covers. More precisely, if U is a collection of convex subsets of$\mathbb { R } ^ { n }$, and if W is a convex subset of$\mathbb { R } ^ { n }$, then

$$
C _ {K T - C W} (\mathcal {U} ^ {W}) = C _ {K T - C W} (\mathcal {U} [ W ]) \leq C _ {K T - C W} (\mathcal {U}).\tag{4.4}
$$

(C) The Frostman Slab Wolf Constant is “sub-multiplicative” with respect to covers. More pre-cisely, if$\mathcal { U } \prec \mathcal { V }$are collections of convex subsets of a convex set$W \subset \mathbb { R } ^ { n }$, then in some situations we have that$C _ { F - S W } ( \mathcal { U } ^ { W } )$is controlled by max$_ { V \in \mathcal { V } } C _ { F - S W } ( \mathcal { U } ^ { V } ) C _ { F - S W } ( \mathcal { V } ^ { W } )$. In certain special cases, the same is true for the Katz-Tao Convex Wolf Constant. See Section 4.4 for a precise statement.

## 4.2 Factoring Convex Sets

As we have observed in Remark 4.3, Frostman Wolf constants are inherited upwards, while Katz-Tao Wolf constants are inherited downwards. The following definition will help us exploit this observation when performing multi-scale analysis and induction on scale.

Definition 4.4. Let U and W be collections of convex subsets of$\mathbb { R } ^ { n }$, and let$K > 0$

(A) We say that W factors U from above with respect to the Katz-Tao (resp. Frostman) Convex Wolf axioms with error K if W covers U, and W satisfies the Katz-Tao (resp. Frostman) Convex Wolf axioms with error K.

(B) We say that W factors U from below with respect to the Katz-Tao (resp. Frostman) Convex Wolf axioms with error K if W covers U, and for each$W \in { \mathcal { W } }$the set$\mathcal { U } ^ { W }$satisfies the Katz-Tao (resp. Frostman) Convex Wolf axioms with error K.

(C) We say that W factors U from above (resp. below) with respect to the Katz-Tao (or Frostman) Slab Wolf axioms with error K if the natural analogue of (A) (resp. (B)) holds, where the Convex Wolf axioms are replaced by Slab Wolf axioms.

![](images/page_26_image_0.jpg)

Figure 5: Left: U is a set of tubes (red) that cluster into rectangular prisms. Right: Proposition 4.6 locates these prisms (black). The tubes in$\mathcal { U } \backslash \mathcal { U } ^ { \prime }$have been X-ed out.

Remark 4.5. Definition 4.4 highlights a few special cases of a more general definition: If U, W, and V are collections of convex subsets of$\mathbb { R } ^ { n }$, we can define what it means for W to factor U from above (or below) with respect to the Katz-Tao (or Frostman) Wolf axioms with respect to V. Item (A) and (B) in Definition 4.4 correspond to the special case where V is the collection of convex sets in$\mathbb { R } ^ { n }$, while Item (C) corresponds to the case where V is the collection of slabs in$\mathbb { R } ^ { n }$

Definition$1 . 3 ^ { \prime }$was carefully formulated to allow the following result, which says that for every collection U of convex subsets of$\mathbb { R } ^ { n }$, there exists some W that factors U from below with respect to the Frostman Convex Wolf axioms, and from above with respect to the Katz-Tao Convex Wolf axioms, both with small error. The precise statement is as follows.

Proposition 4.6. Let U be a finite set of congruent convex subsets of the unit ball in$\mathbb { R } ^ { n }$, each of which contains a ball of radius δ. Let$K = 1 0 0 ^ { n } e ^ { 1 0 0 { \sqrt { \log ( \delta ^ { - 1 } \# \mathcal { U } ) } } }$(the exact shape of K is not important; what matters is that if$\# \mathcal { U } \leq \delta ^ { - 1 0 0 }$, then$K \lessapprox _ { \delta } 1 )$

Then there exists a set W of congruent convex subsets of$\mathbb { R } ^ { n }$and a set$\mathcal { U } ^ { \prime } \subset \mathcal { U }$with the following properties:

i)$\# \mathcal { U } ^ { \prime } \geq K ^ { - 1 } ( \# \mathcal { U } )$

ii) W is a K-balanced, K-almost partitioning cover of U<sup>′</sup>, and

$$
\# \mathcal {U} ^ {\prime} [ W ] \geq K ^ {- 1} C _ {K T - C W} (\mathcal {U} ^ {\prime}) | W | | U | ^ {- 1} \quad f o r e a c h W \in \mathcal {W}.\tag{4.5}
$$

iii) W factors U<sup>′</sup> from above respecting the Katz-Tao Convex Wolf Axioms with error K.

iv) W factors U<sup>′</sup> from below respecting the Frostman Convex Wolf Axioms with error K.

Our proof of Proposition 4.6 will use the following “iterated graph pruning” lemma, which allows us to prune a bipartite graph and find an induced subgraph for which every vertex has many neighbours.

Lemma 4.7. Let$G = ( A \sqcup B , E )$be a bipartite graph. Then there is a sub-graph$G ^ { \prime } = ( A ^ { \prime } \sqcup B ^ { \prime } , E ^ { \prime } )$ so that #$E ^ { \prime } \ge \# E / 2$; each vertex in A<sup>′</sup> has degree at least${ \frac { \# E } { 4 \# A } } ;$and each vertex in$B ^ { \prime }$has degree at least$\frac { \# E } { 4 \# B }$

Lemma 4.7 is proved via iteratively removing those vertices that have few neighbours. See e.g. [7] for a proof.

Proof of Proposition$4 . 6 .$

Step 1. Let$\mathcal { U } _ { 0 } \subset \mathcal { U }$be a set minimizing the quantity

$$
\min_{\substack{\mathcal{U}^{\prime}\subset \mathcal{U}\\ \mathcal{U}^{\prime}\neq \emptyset}}\exp \left[ \left(\log \frac{\#\mathcal{U}}{\#\mathcal{U}^{\prime}}\right)^{2}\right]  C_{KT - CW}(\mathcal{U}^{\prime}).\tag{4.6}
$$

Since$C _ { K T - C W } ( \mathcal { U } _ { 0 } ) \geq 1$, we have

$$
\exp \left[ \left(\log \frac {\# \mathcal {U}}{\# \mathcal {U} _ {0}}\right) ^ {2} \right] \leq \exp \left[ \left(\log \frac {\# \mathcal {U}}{\# \mathcal {U} _ {0}}\right) ^ {2} \right] C _ {K T - C W} (\mathcal {U} _ {0}) \leq C _ {K T - C W} (\mathcal {U}) \leq \# \mathcal {U}.
$$

Re-arranging,

$$
\# \mathcal {U} _ {0} \geq e ^ {- \sqrt {\log (\# \mathcal {U})}} (\# \mathcal {U}).\tag{4.7}
$$

Observe that if$\mathcal { U } ^ { \prime } \subset \mathcal { U } _ { \mathrm { 0 } }$with$\# \mathcal { U } ^ { \prime } \geq \frac { 1 } { 2 } ( \# \mathcal { U } _ { 0 } )$, then

$$
\exp \left[ \left(\log \frac {2 (\# \mathcal {U})}{\# \mathcal {U} _ {0}}\right) ^ {2} \right] C _ {K T - C W} (\mathcal {U} ^ {\prime}) \geq \exp \left[ \left(\log \frac {\# \mathcal {U}}{\# \mathcal {U} ^ {\prime}}\right) ^ {2} \right] C _ {K T - C W} (\mathcal {U} ^ {\prime}) \geq \exp \left[ \left(\log \frac {\# \mathcal {U}}{\# \mathcal {U} _ {0}}\right) ^ {2} \right] C _ {K T - C W} (\mathcal {U} _ {0}).
$$

Re-arranging and using (4.7),

$$
C _ {K T - C W} (\mathcal {U} ^ {\prime}) \geq \kappa_ {0} C _ {K T - C W} (\mathcal {U} _ {0}), \quad \mathrm{where} \kappa_ {0} = e ^ {- 2 \log 2 \sqrt {\log (\# \mathcal {U})}}.\tag{4.8}
$$

Step 2. Select closed convex sets$W _ { 1 } , W _ { 2 } , \ldots \mathrm { i n } \mathbb { R } ^ { n }$and sets$\mathcal { U } _ { 1 } \supset \mathcal { U } _ { 2 } \supset . .$. according to the following procedure. Beginning with$j = 1$, we select$W _ { j }$to maximize<sup>1</sup> the quantity$\# \mathcal { U } _ { j - 1 } [ W _ { j } ] / | W _ { j } |$. By the definition of$C _ { K T - C W } ( \mathcal { U } _ { j - 1 } )$, we can select such a$W _ { j }$so that

$$
\# \mathcal {U} _ {j - 1} [ W _ {j} ] = C _ {K T - C W} (\mathcal {U} _ {j - 1}) \frac {| W _ {j} |}{| U |}.\tag{4.9}
$$

(Recall that$| U |$is the volume of a set from$\mathcal { U } ;$all such sets have identical volume). Define$u _ { j } =$ $\mathcal { U } _ { j - 1 } \backslash \mathcal { U } _ { j - 1 } [ W _ { j } ]$. Continue this process until$\begin{array} { r } { \# M _ { j } < \frac { 1 } { 2 } ( \# M _ { 0 } ) } \end{array}$

Let$\mathcal { W } _ { 0 } = \{ W _ { 1 } , \ldots , W _ { j - 1 } \}$. Then

$$
\# \Big (\bigcup_ {W \in \mathcal {W} _ {0}} \mathcal {U} _ {0} [ W ] \Big) = \# (\mathcal {U} _ {0} \backslash \mathcal {U} _ {j}) > \frac {1}{2} (\# \mathcal {U} _ {0}).\tag{4.10}
$$

Furthermore, for each$i = 1 , \ldots , j$, we have$\# { { \mathcal { U } } _ { i - 1 } } \geq \frac { 1 } { 2 } ( \# { { \mathcal { U } } _ { 0 } } )$, and hence by (4.9) and (4.8),

$$
\# \mathcal {U} _ {i - 1} [ W _ {i} ] = C _ {K T - C W} (\mathcal {U} _ {i - 1}) \frac {| W _ {i} |}{| U |} \geq \kappa_ {0} C _ {K T - C W} (\mathcal {U} _ {0}) \frac {| W _ {i} |}{| U |}.\tag{4.11}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">U</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Since U is a finite set of compact sets, such a maximizer exists; however the proof would work equally well if we merely approximate the maximum within a constant factor.</span></small>

Hence if$\mathcal { W } ^ { \prime } \subset \mathcal { W } _ { 0 }$, to compare${ \# } { \Bigl ( } \bigcup _ { W _ { i } \in \mathcal { W } ^ { \prime } } { \mathcal { U } } _ { 0 } [ W _ { i } ] { \Bigr ) }$and$\sum _ { W _ { i } \in \mathcal { W } ^ { \prime } } \# \mathcal { U } _ { 0 } [ W _ { i } ]$

$$
\begin{array}{l} \kappa_ {0} \frac {C _ {K T - C W} (\mathcal {U} _ {0})}{| U |} \sum_ {W _ {i} \in \mathcal {W} ^ {\prime}} | W _ {i} | \leq \sum_ {W _ {i} \in \mathcal {W} ^ {\prime}} \# \mathcal {U} _ {i - 1} [ W _ {i} ] = \# \Big (\bigsqcup_ {W _ {i} \in \mathcal {W} ^ {\prime}} \mathcal {U} _ {i - 1} [ W _ {i} ] \Big) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq \# \Big (\bigcup_ {W _ {i} \in \mathcal {W} ^ {\prime}} \mathcal {U} _ {0} [ W _ {i} ] \Big) \leq \sum_ {W _ {i} \in \mathcal {W} ^ {\prime}} \# \mathcal {U} _ {0} [ W _ {i} ] \leq \frac {C _ {K T - C W} (\mathcal {U} _ {0})}{| U |} \sum_ {W _ {i} \in \mathcal {W} ^ {\prime}} | W _ {i} |. \end{array}\tag{4.12}
$$

The equality in (4.12) uses the critical fact that if$i \neq i ^ { \prime }$, then$\mathcal { U } _ { i - 1 } [ W _ { i } ]$and$\mathcal { U } _ { i ^ { \prime } - 1 } [ W _ { i ^ { \prime } } ]$are disjoint.

Step 3. Each$W \in \mathcal { W } _ { 0 }$has a John ellipsoid whose axes have lengths$\ell _ { 1 } , \ldots , \ell _ { n }$. Since each set $\mathcal { U } _ { 0 } [ W ]$is non-empty and each$U \in \mathcal { U } _ { 0 }$contains a ball of radius$\delta ,$we have that$\ell _ { i } \geq \delta$for each i. Since the sets in U are contained in the unit ball, we may suppose that$\ell _ { i } \leq 2$for each i. Thus by dyadic pigeonholing and (4.10), there exist$a _ { 1 } , \ldots , a _ { n }$and a set$\mathcal { W } _ { 1 } \subset \mathcal { W } _ { 0 }$, so that the following two items hold:

(i) Each$W \in \mathcal { W } _ { 1 }$has a John ellipsoid whose axes have lengths$\ell _ { 1 } \leq \ell _ { 2 } \ldots \leq \ell _ { n }$with$\ell _ { i } \in [ a _ { i } / 2 , a _ { i } )$

(ii)

$$
\# \left(\bigcup_ {W \in \mathcal {W} _ {1}} \mathcal {U} _ {0} [ W ]\right) \geq (1 0 0 | \log \delta |) ^ {- n} (\# \mathcal {U} _ {0}).\tag{4.13}
$$

Replace each$W$by a congruent copy of$W _ { 0 } { - } \mathrm { a n }$ellipsoid whose axes have lengths$a _ { 1 } , \ldots , a _ { n }$, and denote the corresponding set$\mathcal { W } _ { 2 }$. Observe that (4.13) remains true with$\mathcal { W } _ { 2 }$in place of$\mathcal { W } _ { 1 }$, and (4.12) remains true for all sets$\mathcal { W } ^ { \prime } \subset \mathcal { W } _ { 2 }$, though the first inequality has been weakened by a factor of$2 ^ { n }$on the RHS. Define$\begin{array} { r } { \mathcal { U } _ { 2 } = \bigcup _ { W \in \mathcal { W } _ { 2 } } \mathcal { U } _ { 0 } [ W ] } \end{array}$(recall that a sequence sequence$\mathcal { U } _ { 1 } , \mathcal { U } _ { 2 } , \dotsc .$ was defined earlier, and hence$\boldsymbol { { \mathcal { U } } _ { 2 } }$was previously defined, but this is a harmless abuse of notation); we have that the cardinality of$\boldsymbol { { \mathcal { U } } } _ { 2 }$is bounded below by the RHS of (4.13).

Since$\mathcal { U } _ { 0 } [ W ] = \mathcal { U } _ { 2 } [ W ]$for all$W \in \mathcal { W } _ { 2 }$, by applying (4.12) (beginning with the final inequality, and then using the first few inequalities) with$\mathcal { W } ^ { \prime } = \mathcal { W } _ { 2 }$we conclude that

$$
\begin{array}{l} \# \{(U, W) \in \mathcal {U} _ {2} \times \mathcal {W} _ {2} \colon U \subset W \} = \sum_ {W \in \mathcal {W} _ {2}} \# \mathcal {U} _ {0} [ W ] \leq \frac {C _ {K T - C W} (\mathcal {U} _ {0})}{| U |} \sum_ {W \in \mathcal {W} _ {2}} | W | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq 2 ^ {n} \kappa_ {0} ^ {- 1} \# \Big (\bigcup_ {W \in \mathcal {W} _ {2}} \mathcal {U} _ {0} [ W ] \Big) = 2 ^ {n} \kappa_ {0} ^ {- 1} (\# \mathcal {U} _ {2}). \end{array}\tag{4.14}
$$

In the above estimate, (4.12) was used to obtain the first and second inequalities, while the final equality follows from the definition of$\mathcal { U } _ { 2 }$

Step 4. Construct the bipartite incidence graph$( { \mathcal { T } } , { \mathcal { U } } _ { 2 } \times { \mathcal { W } } _ { 2 } )$whose edges consist of those pairs $( U , W )$with$U \subset W$. This graph has the following properties:

(i) I has at most$2 ^ { n } \kappa _ { 0 } ^ { - 1 } ( \# M _ { 2 } )$edges.

(ii) Each$U \in \mathcal { U } _ { 2 }$has at least one neighbour.

(iii) Each$W \in \mathcal { W } _ { 2 }$has between$2 ^ { - n } \kappa _ { 0 } C _ { K T - C W } ( \mathcal { U } _ { 0 } ) | W _ { 0 } | | U | ^ { - 1 }$and$C _ { K T - C W } ( \mathcal { U } _ { 0 } ) | W _ { 0 } | | U | ^ { - 1 }$neighbours.

Note that Items (i) and (iii) imply that

$$
\# \mathcal {W} _ {2} \leq 2 ^ {2 n} \kappa_ {0} ^ {- 2} \frac {(\# \mathcal {U} _ {2}) | U |}{C _ {K T - C W} (\mathcal {U} _ {0}) | W _ {0} |}.\tag{4.15}
$$

We will construct an induced subgraph of$( { \mathcal { I } } , { \mathcal { U } } _ { 2 } \times { \mathcal { W } } _ { 2 } )$as follows. First, remove all$U \in { \mathcal { U } } _ { 2 }$ with more than$2 ^ { n + 1 } \kappa _ { 0 } ^ { - 1 }$neighbours, and denote the resulting induced subgraph by$( { \cal Z } _ { 3 } , { \cal { U } } _ { 3 } \times { \mathcal { W } } _ { 2 } )$ by Items (i) and (ii), we have$\# u _ { 3 } \geq \frac { 1 } { 2 } \# u _ { 2 }$, and$\# \mathbb { Z } _ { 3 } \geq \# \mathcal { U } _ { 3 }$. Next, apply Lemma 4.7 (iterated graph pruning) to$( { \cal Z } _ { 3 } , { \cal Z } _ { 3 } \times { \mathcal { W } } _ { 2 } )$. Denote the resulting induced subgraph by$( \boldsymbol { \mathcal { T } } ^ { \prime } , \boldsymbol { \mathcal { U } } ^ { \prime } \times \boldsymbol { \mathcal { W } } )$

Step 5. We will verify that$\mathcal { U } ^ { \prime }$and W satisfy Conclusions$( \mathrm { i } ) { - } ( \mathrm { i } \mathrm { v } )$of Proposition 4.6. For Conclusion (i), we have

$$
\# \mathcal {U} ^ {\prime} \geq \frac {\kappa_ {0}}{2 ^ {n + 1}} (\# \mathcal {I} ^ {\prime}) \geq \frac {\kappa_ {0}}{2 ^ {n + 3}} (\# \mathcal {I} _ {3}) \geq \frac {\kappa_ {0}}{2 ^ {n + 3}} (\# \mathcal {U} _ {3}) \geq \frac {\kappa_ {0}}{2 ^ {n + 4}} (\# \mathcal {U} _ {2}) \geq K ^ {- 1} (\# \mathcal {U}),
$$

since$\# \mathcal { U } _ { 2 }$is bounded below by the RHS of (4.13);$\# \mathcal { U } _ { 0 }$is bounded below by (4.7); and K was defined in the statement of Proposition 4.6.

For Conclusion (ii), Since each$U \in \mathcal { U } ^ { \prime }$has at most K neighbours in$( \boldsymbol { \mathcal { T } } ^ { \prime } , \boldsymbol { \mathcal { U } } ^ { \prime } \times \boldsymbol { \mathcal { W } } )$, we have that W is a K-almost partitioning cover of$\mathcal { U } ^ { \prime }$. It remains to verify (4.5). Since$\# \mathcal { U } ^ { \prime } [ W ] \ \leq$ $C _ { K T - C W } ( \mathcal { U } ^ { \prime } ) | W | | U | ^ { - 1 }$, it will then follow that W is a K-balanced cover of$\mathcal { U } ^ { \prime }$. By Lemma 4.7 followed by (4.15), for each$W \in \mathcal { W }$, we have

$$
\begin{array}{l} \# \mathcal {U} ^ {\prime} [ W ] \geq \frac {1}{4} \Big (\# I _ {3} \Big) \Big (\# \mathcal {W} _ {2} \Big) ^ {- 1} \geq \frac {1}{4} \Big (\frac {1}{2} \# \mathcal {U} _ {2} \Big) \Big (2 ^ {- 2 n} \kappa_ {0} ^ {2} \frac {C _ {K T - C W} (\mathcal {U} _ {0}) | W _ {0} |}{(\# \mathcal {U} _ {2}) | U |} \Big) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{4.16}
$$

Since$\mathcal { U } ^ { \prime } \subset \mathcal { U } _ { 0 }$, we have$C _ { K T - C W } ( \mathcal { U } ^ { \prime } ) \leq C _ { K T - C W } ( \mathcal { U } _ { 0 } )$

For Conclusion (iii), let$V \subset \mathbb { R } ^ { n }$be a convex set. Since each$U \in \mathcal { U } _ { 3 }$has at most$2 ^ { n + 1 } \kappa _ { 0 } ^ { - 1 }$ neighbours and$( \boldsymbol { \mathcal { T } } ^ { \prime } , \boldsymbol { \mathcal { U } } ^ { \prime } \times \boldsymbol { \mathcal { W } } )$is an induced subgraph of$( { \cal Z } _ { 3 } , { \cal Z } _ { 3 } \times { \mathcal { W } } _ { 2 } )$, each$U \in \mathcal { U } ^ { \prime }$is contained in at most$2 ^ { n + 1 } \kappa _ { 0 } ^ { - 1 }$sets$\mathcal { U } ^ { \prime } [ W ]$, we have

$$
\# \mathcal {U} ^ {\prime} [ V ] \geq 2 ^ {- n - 1} \kappa_ {0} \sum_ {W \in \mathcal {W} [ V ]} \# \mathcal {U} ^ {\prime} [ W ] \geq \left(2 ^ {- 3 n - 5} \kappa_ {0} ^ {3}\right) C _ {K T - C W} (\mathcal {U} _ {0}) | W _ {0} | | U | ^ {- 1} (\# \mathcal {W} [ V ]),\tag{4.17}
$$

where the final inequality used (4.16). On the other hand,

$$
\# \mathcal {U} ^ {\prime} [ V ] \leq C _ {K T - C W} (\mathcal {U} ^ {\prime}) | V | | W _ {0} | ^ {- 1}.\tag{4.18}
$$

Comparing (4.17) and (4.18), we see that$\# \mathcal { W } [ V ] \leq K | V | | W _ { 0 } | ^ { - 1 }$, as desired.

Finally, for Conclusion (iv), let$W \in { \mathcal { W } }$and let$V \subset W$be a convex set. Then

$$
\# (\mathcal {U} ^ {\prime} [ W ]) [ V ] \leq \# \mathcal {U} ^ {\prime} [ V ] \leq C _ {K T - C W} (\mathcal {U} ^ {\prime}) | V | | U | ^ {- 1}.\tag{4.19}
$$

Comparing (4.19) and (4.5) (which we verified using (4.16)), we conclude that

$$
\# (\mathcal {U} ^ {\prime} [ W ]) [ V ] \leq K | V | | W | ^ {- 1} (\# \mathcal {U} ^ {\prime} [ W ]).
$$

This is precisely the statement that$C _ { F - C W } \big ( ( \mathcal { U } ^ { \prime } ) ^ { W } \big ) \leq K$

## 4.3 Convex Sets and the Frostman Slab Wolf Axioms

The goal of this section is to prove that after a refinement, every collection of convex sets can be partitioned into non-interacting pieces, each of which (after an appropriate rescaling) satisfies the Frostman Slab Wolf axioms. The precise statement is as follows.

Proposition 4.8. For all$n \geq 2 , \varepsilon > 0$, there exists$\eta > 0$and$\kappa , K > 0$so that the following holds for all$\delta > 0$. Let U be a collection of closed convex subsets of the unit ball in$\mathbb { R } ^ { n }$, each of which contains a ball of radius δ. For each$U \in { \mathcal { U } } ,$, let$Y ( U ) \subset U$be a shading with$| Y ( U ) | \geq \delta ^ { \eta } | U |$

Then there exists a set$u ^ { \prime } \subset \mathcal { U } ;$sets$Y ^ { \prime } ( U ^ { \prime } ) \subset Y ( U ^ { \prime } ) , \ U ^ { \prime } \in { \mathcal { U } } ^ { \prime } ;$and a set W of closed convex subsets of$\mathbb { R } ^ { n }$with the following properties:

i) W factors$\mathcal { U } ^ { \prime }$from below with respect to the Frostman Slab Wolf axioms with error$\delta ^ { - \varepsilon }$

ii) The sets$\mathcal { U } ^ { \prime } [ W ] , W \in \mathcal { W }$do not interact, in the sense that the sets$\{ \cup _ { U ^ { \prime } \in \mathcal { U } ^ { \prime } [ W ] } Y ^ { \prime } ( U ^ { \prime } ) , W \in \mathcal { W } \}$ are disjoint.

iii) The subset U<sup>′</sup> and the refined shading$Y ^ { \prime }$preserve most of the mass of the original collection $( \mathcal { U } , Y )$, in the sense that

$$
\sum_ {U ^ {\prime} \in \mathcal {U} ^ {\prime}} | Y ^ {\prime} (U ^ {\prime}) | \geq \kappa \delta^ {\varepsilon} (\log \# \mathcal {U}) ^ {- K} \sum_ {U \in \mathcal {U}} | U |.\tag{4.20}
$$

Proposition 4.8 will rely on the following consequence of Brunn’s theorem:

Lemma 4.9. Let$U \subset \mathbb { R } ^ { n }$be a convex set, let$H \subset \mathbb { R } ^ { n }$be a hyperplane, and let$s > 0 , t \in ( 0 , 1 ]$ Suppose that$| U \cap N _ { s } ( H ) | = t | U |$. Then$U \subset N _ { K _ { n } s / t } ( H )$, where$K _ { n }$depends only on n.

Proof. Without loss of generality we may suppose that the hyperplane H is given by$\{ x _ { 1 } = 0 \}$ Let$f ( t ) = | U \cap \{ x _ { 1 } = t \} | ^ { \frac { 1 } { n - 1 } }$(here | · | denotes$( n - 1 )$)-dimensional Lebesgue measure), and let $I = \operatorname { s u p p } ( f )$. Our task is to show that$| I | \leq K _ { n } s / t$

By Brunn’s theorem, f is concave on I. The result now follows by comparing the estimates $t | U | = | U \cap N _ { s } ( H ) | \leq ( 2 s ) ( \operatorname* { s u p } f ) ^ { n - 1 }$and$| U | \geq K _ { n } | I | ( \operatorname* { s u p } f ) ^ { n - 1 }$(the latter is a consequence of the concavity of f).□

Combining Lemma 4.9 with a Cordoba-style$L ^ { 2 }$argument, we obtain the following.

Lemma 4.10. Let$\lambda \in \mathsf { \Gamma } ( 0 , 1 ]$, let U be a collection of closed convex subsets of the unit ball in R<sup>n</sup>, each of which contains a ball of radius δ. For each$U \in \mathcal { U }$, let$Y ( U ) \subset U$be a shading with $| Y ( U ) | \geq \lambda | U |$

Then there exists a set$u ^ { \prime } \subset \mathcal { U } ;$sets$Y ^ { \prime } ( U ) \subset Y ( U ) , \ U \in \mathcal { U } ^ { \prime } ;$and a set S of infinite slabs (i.e. the s-neighbourhood of a hyperplane in$\mathbb { R } ^ { n } )$with the following properties:

i) S is a partitioning cover of U<sup>′</sup>.

ii)$I f S \in { \cal S }$has thickness s, then the (rescaled) sets$\mathcal { U } ^ { \prime } [ S ]$have Frostman Slab Wolf constant $O ( s ^ { - 1 } )$. More concretely,$i f \tilde { S } \subset S$is$\textit { a s } \times 2 \times . . . \times 2$slab that contains the convex sets from $\mathcal { U } ^ { \prime } [ S ]$, then$C _ { F - S W } ( \mathcal { U } ^ { \prime \tilde { S } } ) \lesssim s ^ { - 1 }$

iii) The sets$\begin{array} { r } { \bigcup _ { U \in \mathcal { U } ^ { \prime } [ S ] } Y ^ { \prime } ( U ) , S \in \mathcal { S } } \end{array}$are pairwise disjoint.

iv)$\begin{array} { r } { | Y ^ { \prime } ( U ) | \geq \frac { \lambda } { 2 } | U | } \end{array}$for each$U \in \mathcal { U } ^ { \prime }$, and

$$
\sum_ {U \in \mathcal {U} ^ {\prime}} | U | \gtrsim \log (\lambda^ {- 1} \delta^ {- 1} \# \mathcal {U}) ^ {- 1} \lambda \sum_ {U \in \mathcal {U}} | U |.\tag{4.21}
$$

Proof.

Step 1. Define$\begin{array} { r } { \mathcal { U } _ { 0 } = \mathcal { U } . } \end{array}$, and define$Y _ { 0 } ( U ) = Y ( U )$for each$U \in { \mathcal { U } } _ { 0 }$. For$i = 1 , . . . ,$let$S _ { i } = N _ { s _ { i } } ( H _ { i } )$ be a slab maximizing the quantity

$$
s _ {i} ^ {- 1} \sum_ {U \in \mathcal {U} _ {i - 1} [ S _ {i} ]} | U |.\tag{4.22}
$$

Let$\mathcal { U } ^ { ( i ) } = \mathcal { U } _ { i - 1 } [ S _ { i } ]$; by the maximality of$S _ { i }$, we have that$\mathscr { U } ^ { ( i ) }$satisfies Conclusion (ii) from Lemma 4.10.

For each$U \in \mathcal { U } _ { i - 1 }$, define$Y _ { i } ( U ) = Y _ { i - 1 } ( U ) \backslash S _ { i }$, and define

$$
\mathcal {U} _ {i} = \left\{U \in \mathcal {U} _ {i - 1} \colon | Y _ {i} (U) | \geq \frac {\lambda}{2} | U | \right\}.
$$

In particular,$\mathcal { U } _ { i } \cap \mathcal { U } ^ { ( i ) } = \emptyset$

Step 2. We claim that

$$
\sum_ {U \in \mathcal {U} _ {i - 1}} | U \cap S _ {i} | \lesssim \log (\lambda^ {- 1} \delta^ {- 1} \# \mathcal {U}) \sum_ {U \in \mathcal {U} ^ {(i)}} | U |.\tag{4.23}
$$

We verify (4.23) as follows. Since$\begin{array} { r } { \sum _ { U \in \mathcal { U } ^ { ( i ) } } | U | \geq \frac { \lambda } { 2 } \delta ^ { n } } \end{array}$, the contribution from those$U \in \mathcal { U } _ { i - 1 }$with $\begin{array} { r } { | U \cap S _ { i } | \leq \frac { 1 } { 4 } \lambda \delta ^ { n } ( \# \mathcal { U } ) ^ { - 1 } } \end{array}$is negligible. For each dyadic$t \in [ \textstyle { \frac { 1 } { 4 } } \lambda \delta ^ { n } ( \# \mathcal { U } ) ^ { - 1 } , 1 ]$we have

$$
\begin{array}{c}\sum_{\substack{U\in \mathcal{U}_{i - 1}\\ |U\cap S|\sim t|U|}}|U\cap S_{i}|\lesssim t\sum_{\substack{U\in \mathcal{U}_{i - 1}\\ |U\cap S|\sim t|U|}}|U|\leq t\sum_{U\in \mathcal{U}_{i - 1}[N_{Kn s_{i} / t}(H_{i})]}|U|\\ \leq K_{n}\sum_{U\in \mathcal{U}_{i - 1}[S_{i}]}|U| = K_{n}\sum_{U\in \mathcal{U}^{(i)}}|U|. \end{array}\tag{4.24}
$$

The second inequality follows from the containment

$$
\left\{U \in \mathcal {U} _ {i - 1} \colon | U \cap S | \sim t | U | \right\} \subset \left\{U \in \mathcal {U} _ {i - 1} [ N _ {K _ {n} s / t} (H _ {i}) ] \right\}
$$

for an appropriately chosen constant$K _ { n }$depending on n; this is Lemma 4.9. The third inequality used the maximality of$S _ { i } ,$, in the sense of (4.22). (4.23) now follows from summing (4.24) over dyadic values of t.

Step 3. We halt the procedure described above when$\mathcal { U } _ { N } = \emptyset$. Define$\begin{array} { r } { \mathcal { U } ^ { \prime } = \bigsqcup _ { i = 1 } ^ { N } \mathcal { U } ^ { ( i ) } } \end{array}$, and for each $U \in \mathcal { U } ^ { \prime }$, define$Y ^ { \prime } ( U ) = Y _ { i - 1 } ( U )$, where i is the unique index so that$U \in \mathcal { U } ^ { ( i ) }$Conclusions (i) and (iii) follow immediately from the above construction, as does the fact that$\begin{array} { r } { | Y ^ { \prime } ( U ^ { \prime } ) | \geq \frac { \lambda } { 2 } | U ^ { \prime } | } \end{array}$for each$U ^ { \prime } \in \mathcal { U } ^ { \prime }$. Conclusion (ii) was already verified in Step 1.

It remains to verify (4.21). We claim that each$U \in \mathcal { U } = \mathcal { U } _ { 0 }$contributes at least${ \frac { \lambda } { 2 } } | U |$to the sum

$$
\sum_ {i = 1} ^ {N} \sum_ {U \in \mathcal {U} _ {i - 1}} | U \cap S _ {i} |,
$$

in the sense that$\begin{array} { r } { \sum _ { i : U \in \mathcal { U } _ { i - 1 } } | U \cap S _ { i } | \geq \frac { \lambda } { 2 } | U | } \end{array}$. Indeed, suppose that$j > 0$is the smallest index with $U \not \in { \mathcal { U } } _ { j }$, and hence$\begin{array} { r } { | Y ( U ) \backslash \bigcup _ { i = 1 } ^ { j } S _ { i } | < \frac { \lambda } { 2 } | U | } \end{array}$. But since$| Y ( U ) | \geq \lambda | U |$, this means that

$$
\sum_ {i = 1} ^ {j} | U \cap S _ {i} | \geq \frac {\lambda}{2} | U |,
$$

as claimed.

We conclude that

$$
\sum_ {i = 1} ^ {N} \sum_ {U \in \mathcal {U} _ {i - 1}} | U \cap S _ {i} | \geq \frac {\lambda}{2} \sum_ {U \in \mathcal {U}} | U |.\tag{4.25}
$$

Comparing (4.23) and (4.25), we obtain (4.21).

Proposition 4.8 follows from repeatedly applying Lemma 4.10. We now turn to the details.

Proof of Proposition$4 . 8 .$Let$\lambda = { \textstyle \frac { 1 } { 4 } } \delta ^ { \eta }$. After discarding those$U \in \mathcal { U }$with$| Y ( U ) | < \lambda | U |$, we may suppose that U satisfies the hypotheses of Lemma 4.10.

Let$\mathcal { U } _ { 0 } = \mathcal { U }$and for each$U \in { \mathcal { U } } _ { 0 }$, let$Y _ { 0 } ( U ) = Y ( U )$. Let$\mathcal { P } _ { 0 } = \{ B ( 0 , 1 ) \}$, and let${ \mathcal { W } } _ { 0 } = \emptyset$. The set$\mathcal { P } _ { 0 }$corresponds to convex sets that still need to be “processed” by Lemma 4.10, while$\mathcal { W } _ { 0 }$will hold the convex sets that satisfy the hypotheses of Proposition 4.8.

We will iteratively construct sets$\mathcal { U } _ { i } \subset \mathcal { U } _ { i - 1 }$and$Y _ { i } ( U ) \subset Y _ { i - 1 } ( U )$; a set$\mathcal { W } _ { i } \supset \mathcal { W } _ { i - 1 }$of convex subsets of$B ( 0 , 1 )$; and a set$\mathcal { P } _ { i }$of convex subsets of$B ( 0 , 1 )$such that the following properties hold:

1. For each$W \in \mathcal { W } _ { i } , C _ { F - S W } ( \mathcal { U } _ { i } ^ { W } ) \lesssim \delta ^ { - \varepsilon } \ ( \mathrm { r e c a l l } \ \mathcal { U } _ { i } ^ { W } = \phi _ { W } ( \mathcal { U } _ { i } [ W ] ) )$

2. For each$P \in \mathcal { P } _ { i } , | P | \leq \delta ^ { i \varepsilon } | B ( 0 , 1 ) |$

3.$\mathcal { W } _ { i } \sqcup \mathcal { P } _ { i }$is a partitioning cover of$\mathcal { U } _ { i }$.

4. The sets$\textstyle \bigcup _ { U \in { \mathcal { U } } _ { i } [ V ] } Y _ { i } ( U )$are pairwise disjoint, as V ranges over the convex sets in$\mathcal { P } _ { i } \sqcup \mathcal { W } _ { i }$

5.$| Y _ { i } ( U ) | \geq 2 ^ { - i } \lambda | U |$for each$U \in \mathcal { U } _ { i }$

6.

$$
\sum_ {V \in \mathcal {P} _ {i} \cup \mathcal {W} _ {i}} \sum_ {U \in \mathcal {U} _ {i} [ V ]} | Y _ {i} (U) | \gtrsim \log (\delta^ {- 1} \# \mathcal {U}) ^ {i} \lambda^ {i} \sum_ {U \in \mathcal {U}} | U |.
$$

These six items are trivially satisfied when$i = 0$. For the i-th step, begin by setting$\mathcal { W } _ { i } = \mathcal { W } _ { i - 1 }$ $\mathcal { P } _ { i } = \emptyset$, and$\begin{array} { r } { \mathcal { U } _ { i } = \bigcup _ { W \in \mathcal { W } _ { i - 1 } } \mathcal { U } _ { i - 1 } [ W ] , Y _ { i } ( U ) = Y _ { i - 1 } ( U ) } \end{array}$for each$U \in \mathcal { U } _ { i }$

For each$P \in \mathcal P _ { i - 1 }$, apply Lemma 4.10 (with$2 ^ { - ( i - 1 ) } \lambda$in place of λ) to each collection$\mathcal { U } _ { i - 1 } ^ { P } =$ $\phi _ { P } ( \mathcal { U } _ { i - 1 } [ P ] )$of ellipsoids, and their associated shadings$\phi _ { P } ( Y _ { i - 1 } ( U ) )$. We obtain a collection of slabs S, a set$\mathcal { U } _ { i - 1 } ^ { \prime } [ P ] \subset \mathcal { U } _ { i - 1 } [ P ]$, and a shading, which we denote by$Y _ { i } ( U )$, on the ellipsoids in $\mathcal { U } _ { i - 1 } ^ { \prime } [ P ]$. Add the ellipsoids in$\mathcal { U } _ { i - 1 } ^ { \prime } [ P ]$and their associated shading$Y _ { i } ( U )$to$\mathcal { U } _ { i }$. Next, we consider each slab$S \in S$in turn.

• If a slab$S \in S$has thickness$\geq \delta ^ { \varepsilon }$, then this corresponds to a convex set$W = P \cap \phi _ { P } ^ { - 1 } ( S )$ for which$C _ { F - S W } \big ( ( \mathcal { U } _ { i - 1 } ^ { \prime } [ P ] ) ^ { W } \big ) \lesssim \delta ^ { - \varepsilon }$. Add this set to$\mathcal { W } _ { i }$

• If a slab$S \in { \mathcal { S } }$has thickness$\leq \delta ^ { \varepsilon }$, then this corresponds to a convex set$P ^ { \prime } = P \cap \phi _ { P } ^ { - 1 } ( S )$for which

$$
| P ^ {\prime} | \leq \delta^ {\varepsilon} | P | \leq \delta^ {\varepsilon} \big (\delta^ {(i - 1) \varepsilon} | B (0, 1) | \big) = \delta^ {i \varepsilon} | B (0, 1) |.
$$

Add this set to$\mathcal { P } _ { i }$

After this procedure has been performed for each$P \in \mathcal P _ { i - 1 }$, Properties 1 and 2 are immediate, while Properties 3-6 follow from their counterparts in Lemma 4.10.

We halt the process when the output$\mathcal { P } _ { N } = \varnothing$. Since each$U \in \mathcal { U }$has volume at least$\delta ^ { n }$, the above procedure must halt after at most$n / \varepsilon$steps. We let$\mathcal { W } = \mathcal { W } _ { N } , \mathcal { U } ^ { \prime } = \mathcal { U } _ { N }$, and$Y ^ { \prime } ( U ) = Y _ { N } ( U )$ To obtain (4.20), η must be selected suficiently small so that$\delta ^ { N \eta } \leq \delta ^ { \varepsilon }$, i.e.$\eta \sim \varepsilon ^ { 2 } / n$and$K \sim n / \varepsilon$ will sufice.□

## 4.4 The Frostman Slab Wolf Axioms and Covers

In this section we will state and prove a precise version of Remark$4 . 3 ( \mathrm { C } )$. We first consider the Frostman Slab Wolf Axioms.

Lemma 4.11. Let$W \subset \mathbb { R } ^ { n }$be a convex set and let U and V be collections of convex subsets of$W$, with$\mathcal { U } \prec \mathcal { V }$and$\# { \mathcal { U } } [ V ] \leq K ( \# { \mathcal { U } } ) / ( \# \mathcal { V } )$for each$V \in \mathcal V$. Suppose that each set in U has the same volume, and similarly for V. Finally, suppose that each set in$\mathcal { U } ^ { W }$has diameter$\ge 1 / 1 0 0$

Then

$$
C _ {F - S W} (\mathcal {U} ^ {W}) \lesssim \log (2 + | U ^ {W} | ^ {- 1}) K \Bigl (\sup _ {V \in \mathcal {V}} C _ {F - S W} (\mathcal {U} ^ {V}) \Bigr) \Bigl (C _ {F - S W} (\mathcal {V} ^ {W}) \Bigr).\tag{4.26}
$$

Proof. First, to simplify notation we may suppose wlog that$W = B ( 0 , 1 )$; indeed, both the hypotheses and conclusion of Lemma 4.11 remain unchanged if we replace W by$W ^ { W }$(the latter is comparable to$B ( 0 , 1 ) )$; replace U by$\mathcal { U } ^ { W }$; and replace V by$\nu ^ { W }$. In particular, each set in$\boldsymbol { \mathcal { U } }$now has diameter$\ge 1 / 1 0 0$

Fix a truncated, thickened hyperplane$S = N _ { s } ( H ) \cap B ( 0 , 1 )$, with$\mathcal { U } [ S ] \neq \emptyset$(so in particular $s \geq | U | / K _ { n }$, where$K _ { n }$is a constant depending only on the dimension$n )$. We may suppose that $s \leq 2$, since otherwise we can replace$N _ { s } ( H )$by a hyperplane of the form$N _ { 2 } ( H ^ { \prime } )$, which has the same intersection with$B ( 0 , 1 )$

Since$\mathcal { U } \prec \mathcal { V }$, we have

$$
\mathcal{U}[S] = \bigcup_{V\in \mathcal{V}}\mathcal{U}[V\cap S] = \bigcup_{t\text{dyadic}}\bigcup_{\substack{V\in \mathcal{V}\\ |V\cap S|\sim t|V|}}\mathcal{U}[V\cap S],\tag{4.27}
$$

where the first union ranges over dyadic values of t between$| U | | B ( 0 , 1 ) | ^ { - 1 }$and 1 (this range is suficient, since if$| V \cap S | < | U | | B ( 0 , 1 ) | ^ { - 1 } | V | < | U |$, then$\mathcal { U } [ V \cap S ] = \emptyset )$. Observe that there are $\lesssim \log ( 2 + | U | ^ { - 1 } )$dyadic values of t in this range.

Since$\boldsymbol { \mathcal { U } } [ S ] \neq \boldsymbol { \emptyset }$and each element of U has diameter$\ge 1 / 1 0 0$, we have diam$( S \cap B ( 0 , 1 ) ) \geq 1 / 1 0 0$ and hence

$$
\left| N _ {s / t} (H) \cap B (0, 1) \right| \sim s / t \sim t ^ {- 1} | S | \quad \text { for   all } t \in [ s, 1 ].\tag{4.28}
$$

Next, let$V \in \mathcal V$with$| V \cap S | \sim t | V |$. This means that$| ( V \cap S ) ^ { V } | \sim t .$. We have

$$
\begin{array}{l} \# \mathcal {U} [ V \cap S ] = \# \{U \in \mathcal {U} \colon U \subset V \cap S \} \\ \qquad = \# \{U \in \mathcal {U} [ V ] \colon U \subset V \cap S \} \\ \qquad = \# \{U ^ {V} \in \mathcal {U} ^ {V} \colon U ^ {V} \subset (V \cap S) ^ {V} \} \\ \qquad \leq C _ {_ {F - S W}} (\mathcal {U} ^ {V}) | (V \cap S) ^ {V} | (\# \mathcal {U} [ V ]) \\ \qquad \lesssim t \Big (\sup _ {V \in \mathcal {V}} C _ {_ {F - S W}} (\mathcal {U} ^ {V}) \Big) \Big (K \frac {\# \mathcal {U}}{\# \mathcal {V}} \Big). \end{array}\tag{4.29}
$$

On the other hand, by Lemma 4.9 we have

$$
\begin{array}{r l} & {\# \{V \in \mathcal {V} \colon | V \cap S | \sim t | V | \} \leq \# \{V \in \mathcal {V} \colon V \subset N _ {K _ {n} s / t} (H) \}} \\ & {\qquad \lesssim C _ {F - S W} (\mathcal {V}) | B (0, 1) \cap N _ {K _ {n} s / t} (H) | (\# \mathcal {V})} \\ & {\qquad \lesssim t ^ {- 1} C _ {F - S W} (\mathcal {V}) | S | (\# \mathcal {V}),} \end{array}\tag{4.30}
$$

where the final inequality used (4.28).

Using (4.29) and (4.30) to control the cardinality of the union (4.27), we conclude that

$$
\begin{array}{l} \# \mathcal {U} [ S ] \lesssim \sum_ {t \text {dyadic}} \Big (t ^ {- 1} C _ {F - S W} (\mathcal {V}) | S | (\# \mathcal {V}) \Big) \Big (t \big (\sup _ {V \in \mathcal {V}} C _ {F - S W} (\mathcal {U} ^ {V}) \big) \big (K \frac {\# \mathcal {U}}{\# \mathcal {V}} \big) \Big) \\ \lesssim K _ {1} | S | (\# \mathcal {U}), \quad K _ {1} = \log (2 + | U | ^ {- 1}) K \Big (\sup _ {V \in \mathcal {V}} C _ {F - S W} (\mathcal {U} ^ {V}) \Big) \Big (C _ {F - S W} (\mathcal {V}) \Big). \end{array}
$$

Next we consider Remark$4 . 3 ( \mathrm { C } )$for the Katz-Tao Convex Wolf Axioms. We will restrict attention to the special case where the convex sets in question are tubes.

Lemma 4.12. Let$0 < \delta \leq \rho \leq 1$. Let T be a multiset of δ-tubes and let$\mathbb { T } _ { \rho }$be a cover of T. Then

$$
C _ {K T - C W} (\mathbb {T}) \lesssim \Bigl (\sup _ {T _ {\rho} \in \mathbb {T} _ {\rho}} C _ {K T - C W} (\mathbb {T} ^ {T _ {\rho}}) \Bigr) \Bigl (C _ {K T - C W} (\mathbb {T} _ {\rho}) \Bigr).\tag{4.31}
$$

Proof. Let$W \subset \mathbb { R } ^ { 3 }$be a convex set with$\mathbb { T } [ W ] \neq \emptyset$. Replacing W by$W \cap B ( 0 , 1 )$and then enlarging W by a constant factor, we may assume that W is a prism of dimensions$a \times b \times 2$. Since$\mathbb { T } _ { \rho }$covers T, we have

$$
\mathbb {T} [ W ] = \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} (\mathbb {T} [ T _ {\rho} ]) [ W ] = \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} \mathbb {T} [ T _ {\rho} \cap W ].\tag{4.32}
$$

Observe that if$\mathbb { T } [ T _ { \rho } \cap W ] \neq \emptyset$, then$T _ { \rho } \cap W$must contain a unit line segment, and thus$T _ { \rho } \subset N _ { 3 \rho } ( W )$

Let$\tilde { \boldsymbol { a } } = \operatorname* { m i n } ( \boldsymbol { a } , \rho )$and$\tilde { b } = \operatorname* { m i n } ( b , \rho )$. Observe that

$$
\left| N _ {3 \rho} (W) \right| \sim \left(\frac {\rho}{\tilde {a}}\right) \left(\frac {\rho}{\tilde {b}}\right) | W |,
$$

and thus

$$
\# \mathbb {T} _ {\rho} [ N _ {3 \rho} (W) ] \leq C _ {K T - C W} (\mathbb {T} _ {\rho}) \frac {| N _ {3 \rho} W |}{| T _ {\rho} |} \lesssim C _ {K T - C W} (\mathbb {T} _ {\rho}) \frac {| W |}{\tilde {a} \tilde {b}}.\tag{4.33}
$$

On the other hand, if$\mathbb { T } [ T _ { \rho } \cap W ]$is non-empty, then$T _ { \rho } \cap W$is a convex set of dimensions bounded by$2 \tilde { a } \times 2 \tilde { b } \times 1$, and thus

$$
\# \mathbb {T} [ T _ {\rho} \cap W ] \lesssim C _ {K T - C W} (\mathbb {T} [ T _ {\rho} ]) \frac {| T _ {\rho} \cap W |}{| T |} \lesssim C _ {K T - C W} (\mathbb {T} ^ {T _ {\rho}}) \frac {\tilde {a} \tilde {b}}{| T |}.\tag{4.34}
$$

(4.31) now follows by combining (4.32), (4.33), and (4.34).

## 5 Factoring tubes into flat prisms

In this section, we will explore what happens when Proposition 4.6 is applied to a set$\mathbb { T }$of$\delta _ { - }$ tubes. Recall that Proposition 4.6 outputs a refinement$\mathbb { T } ^ { \prime } \subset \mathbb { T }$and a set W of convex sets. If $C _ { F - C W } ( \mathbb { T } ) = 1$, then$\mathcal { W } = \{ B ( 0 , 1 ) \}$}. On the other hand, if$C _ { K T - C W } ( \mathbb { T } ) = 1$, then$\mathcal { W } = \mathbb { T }$. If both $C _ { K T - C W } ( \mathbb { T } )$and$C _ { F - C W } ( \mathbb { T } )$are large, then W will consist of a collection of convex sets, each of which are comparable to a rectangular prism of dimensions$a \times b \times 1$, for some$\delta \leq a \leq b \leq 1$. The goal of this section is to explore the following theme: if the prisms in W are flat, in the sense that$a \ll b ,$ then the union$\cup T$will have larger volume than predicted by the estimate (1.3) from Assertion $\mathcal { E } ( \sigma , \omega )$. The precise statement is as follows.

Proposition 5.1. Let$\omega > 0 , \ 0 < \sigma \le 2 / 3$, and suppose$\mathcal { E } ( \sigma , \omega )$is true. Then for all$\varepsilon > 0$, there exists$\kappa , \eta > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense. Let$\delta \leq a \leq b \leq 1$ and let W be$a ~ \delta ^ { - \eta }$balanced cover of T consisting of congruent copies of an$a \times b \times 2$prism.

(A) Suppose that W factors T from below with respect to the Frostman Convex Wolf axioms and from above with respect to the Katz-Tao Convex Wolf axioms, both with with error$\delta ^ { - \eta }$. Suppose as well that W is a$\delta ^ { - \eta }$-balanced,$\delta ^ { - \eta }$-almost partitioning cover of T, and that$\# \mathbb { T } [ W ] \geq$ $\delta ^ { \eta } C _ { K T - C W } ( \mathbb { T } ) \frac { | W | } { | T | }$for each$W \in { \mathcal { W } }$(this condition is satisfied, for example, if W is the output when Proposition$\it 4 . 6$is applied to T). Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega + \varepsilon} \Big (\frac {b}{a} \Big) ^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 3 / 2} \ell (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma},\tag{5.1}
$$

where$m = C _ { K T - C W } ( \mathbb { T } )$and$\ell = C _ { F \cdot S W } ( \mathbb { T } )$

(B) Suppose that W factors T from above and below with respect to the Frostman Convex$W o l f f$ Axioms, both with$e r r o r \le \delta ^ { - \eta }$. Suppose as well that W satisfies the Katz-Tao Convex Wolf axioms at scale b in the following sense: for all$W \in { \mathcal { W } }$we have$C _ { K T - C W } ( \mathcal { W } [ N _ { b } ( W ) ] ) \leq \delta ^ { - \eta }$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega + \varepsilon} \Big (\frac {b}{a} \Big) ^ {\omega} \big ((\# \mathbb {T}) ^ {1 / 2} | T | \big) ^ {\sigma}.\tag{5.2}
$$

Note that (5.2) agrees with (5.1) when$C _ { K T - C W } ( \mathbb { T } ) = ( \# \mathbb { T } ) | T |$, in which case both$C _ { F - C W } ( \mathbb { T } )$and $C _ { F - S W } ( \mathbb { T } )$have size$\sim 1$

In Section 9 we will need the following mild generalization of Proposition$5 . 1 ( \mathrm { A } )$

Proposition 5.2. Let$\omega > 0 , \ 0 < \sigma \le 2 / 3$, and suppose$\mathcal { E } ( \sigma , \omega )$is true. Then for all$\varepsilon > 0$, there exists κ$; , \eta > 0$so that the following holds for all$0 < \delta \leq \rho \leq a \leq b \leq 1$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense and let$\mathbb { T } _ { \rho }$be$a ~ \delta ^ { - \eta }$balanced cover of T. Let W be$a ~ \delta ^ { - \eta }$balanced cover of$\mathbb { T } _ { \rho }$consisting of congruent copies of an$a \times b \times 2$prism.

Suppose that$\mathbb { T } _ { \rho }$factors T from below with respect to the Frostman Slab Wolf Axioms with error $\ell ^ { \prime }$. Suppose that W factors$\mathbb { T } _ { \rho }$from above with respect to the Katz-Tao Convex Wolf axioms and from below with respect to the Frostman Convex Wolf axioms, both with error$\delta ^ { - \eta }$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega + \varepsilon} \Big (\frac {b}{a} \Big) ^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 3 / 2} \ell \ell^ {\prime} (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma},\tag{5.3}
$$

where$m = C _ { K T - C W } ( \mathbb { T } )$and$\ell = C _ { F \cdot S W } ( \mathbb { T } )$

Proposition$5 . 1 ( \mathrm { A } )$is the special case of Proposition 5.2 where$\rho = \delta$and$\mathbb { T } _ { \rho } = \mathbb { T }$

The main goal of Section 5 is to prove Propositions 5.1 and 5.2. A second goal is to introduce two cousins of the estimate$\mathcal { E } ( \sigma , \omega )$, and to show that these three estimates are equivalent. The first estimate is (formally) weaker: it is the special case of the estimate$\mathcal { E } ( \sigma , \omega )$when ℓ has size about 1.

$$
\tilde {\mathcal {E}} (\sigma , \omega)
$$

For all$\varepsilon > 0$, there exists$\kappa , \eta > 0$such that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$ dense, and suppose$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega + \varepsilon} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 3 / 2} (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma},\tag{5.4}
$$

where$m = C _ { K T - C W } ( \mathbb { T } )$

The second estimate is (formally) stronger: it is a generalization of the estimate$\mathcal { E } ( \sigma , \omega )$where δ-tubes are replaced by congruent convex sets of diameter 1.

Definition 5.4. We say that Assertion$\mathcal { F } ( \sigma , \omega )$is true if the following holds:

For all$\varepsilon > 0$, there exists$\kappa , \eta > 0$such that the following holds for all$0 < a \le b \le 1$. Let $( \mathcal { P } , Y ) _ { a \times b \times 1 }$be$a ^ { \eta }$dense. Then

$$
\Big | \bigcup_ {P \in \mathcal {P}} Y (P) \Big | \geq \kappa a ^ {\varepsilon} b ^ {\omega} m ^ {- 1} (\# \mathcal {P}) | P | (m ^ {- 3 / 2} \ell (\# \mathcal {P}) | P | ^ {1 / 2}) ^ {- \sigma} D ^ {- \sigma},\tag{5.5}
$$

where

$$
m = C _ {K T - C W} (\mathcal {P}), \quad \ell = C _ {F - S W} (\mathcal {P}), \quad \text {and} \quad D = \max _ {P \in \mathcal {P}} \sup _ {\rho \in [ a, b ]} \frac {| P |}{| N _ {\rho} (P) |} \bigl (\# \mathcal {P} [ N _ {\rho} (P) ] \bigr) ^ {1 / 2}.\tag{5.6}
$$

Remark 5.5. When$\sigma \in ( 0 , 2 / 3 ]$, the term

$$
m ^ {- 1} (\# \mathcal {P}) | P | (m ^ {- 3 / 2} \ell (\# \mathcal {P}) | P | ^ {1 / 2}) ^ {- \sigma} D ^ {- \sigma}
$$

is always at most 1. To see this, since$\# \mathcal { P } \leq m | P | ^ { - 1 }$and$\sigma \in ( 0 , 2 / 3 ]$, it remains to show that $( ( \# \mathcal { P } ) | P | ) ^ { 1 / 2 } l ^ { - 1 } | P | ^ { 1 / 2 } \leq D$. This is true because$\# \mathcal { P } \leq \# \mathcal { P } [ N _ { b } ( P ) ] \cdot b ^ { - \bar { 4 } } \leq D ^ { 2 } b ^ { - 2 } a ^ { - 2 }$, and$\ell \geq 1$ Remark 5.6. If P is non-empty, then by selecting$\rho = a$we see that the quantity$D = D ( \mathcal { P } )$from (5.6) is always$\gtrsim 1$. In general, D can be as large as$( b / a ) ^ { 1 / 2 }$: when$\rho = b ,$, it is possible for about $( b / a ) ^ { 3 }$essentially distinct$a \times b \times 1$prisms to fit inside the b tube$N _ { b } ( P )$. If this happens, then the RHS of (5.6) becomes$\textstyle { \frac { a b } { b ^ { 2 } } } ( b / a ) ^ { 3 / 2 } = ( b / a ) ^ { 1 / 2 }$. However, there are several important situations where we can guarantee that D has size roughly 1. We describe three of these below.

Situation 1. If$a = b .$then since the prisms in$\mathcal { P }$are essentially distinct, we have$\# \mathcal { P } ( N _ { a } ( P ) ) \sim 1$ and hence$D \sim 1$. In particular, this means that${ \mathcal { F } } ( \sigma , \omega ) \implies { \mathcal { E } } ( \sigma , \omega )$

Situation 2. Suppose that for each$P \in { \mathcal { P } }$, we have$C _ { K T - C W } ( \mathcal { P } [ N _ { b } ( P ) ] ) \le K$, for some$K \geq 1$. This means that the Katz-Tao Convex Wolf constant of P might be large, but if we restrict attention to those prisms${ \mathcal { P } } ^ { \prime }$contained inside a tube of diameter b, then the Katz-Tao Convex Wolf constant of${ \mathcal { P } } ^ { \prime }$is small (this is the setup for Item (B) of Proposition 5.1). Then for each$\rho \in [ a , b ]$and$P \in { \mathcal { P } }$ we have$\begin{array} { r } { \# \mathcal { P } [ \dot { N } _ { \rho } ( P ) ] \lesssim K \frac { \rho \cdot b \cdot 1 } { a \cdot b \cdot 1 } = K \frac { \rho } { a } } \end{array}$, and hence$D \lesssim K ^ { 1 / 2 }$

Situation 3. Let T be a set of essentially distinct δ-tubes contained in a$s \times t \times 2$prism$W$, with $0 < s \le t \le 2$. Let$\mathcal { P } = \phi _ { W } ( \mathbb { T } )$. Then the sets in$\mathcal { P }$are comparable to rectangular prisms of dimensions$a \times b \times 2$with$a = \delta / t$and$b = \delta / s$. Let us estimate the quantity$D = D ( \mathcal { P } )$for this arrangement. For each$\rho \in [ a , b ]$and each$P \in \mathcal { P }$, #${ \it \cdot } \mathcal { P } [ N _ { \rho } ( P ) ]$counts the number of δ-tubes from T contained inside a rectangular box of dimensions roughly$\delta \times ( \delta \rho / a ) \times 2$. Since the tubes in$\mathbb { T }$ are essentially distinct, at most$\begin{array} { r } { O \big ( \big ( \frac { ( \delta \rho / a ) } { \delta } \big ) ^ { 2 } \big ) = O \big ( \rho ^ { 2 } / a ^ { 2 } \big ) } \end{array}$tubes from$\mathbb { T }$can be contained in such a box, i.e.$\begin{array} { r } { D \lesssim \operatorname* { s u p } _ { \rho \in [ a , b ] } \left( \frac { a b } { \rho b } \right) \left( \frac { \rho } { a } \right) = 1 } \end{array}$

## 5.1 A few frequently used Cordoba-type$L ^ { 2 }$arguments

In this section, we will explore several variants of the following argument: To show that a union $\cup _ { P \in { \mathcal { P } } } P$is large, it sufices to show that the quantity$\begin{array} { r } { \| \sum _ { P \in \mathcal { P } } \chi _ { P } \| _ { 2 } ^ { 2 } = \sum _ { P , P ^ { \prime } \in \mathbb { T } } | P \cap P ^ { \prime } | } \end{array}$is small, and then use Cauchy-Schwartz to conclude that

$$
\Big | \bigcup_ {P \in \mathcal {P}} P \Big | \geq \Big (\sum_ {P \in \mathcal {P}} | P | \Big) ^ {2} \Big / \Big \| \sum_ {P \in \mathcal {P}} \chi_ {P} \Big \| _ {2}.
$$

This argument was used by Cordoba [6] to prove the Kakeya maximal function conjecture in$\mathbb { R } ^ { 2 }$ so we will call this style of argument a “Cordoba-type$L ^ { 2 }$argument.”

## 5.1.1 A volume estimate for slabs

In this section we will use a Cordoba-type$L ^ { 2 }$argument to estimate the volume of a union of slabs. The precise statement is as follows.

Lemma 5.7. Let$\delta , \lambda > 0$. Let S be a collection of$\delta \times 1 \times \ldots \times 1$slabs (n.b. these slabs need not be essentially distinct), and let Y be a λ-dense shading on$\boldsymbol { s }$. Let$m = C _ { K T - C W } ( S )$. Then

$$
\Big | \bigcup_ {S \in \mathcal {S}} Y (S) \Big | \gtrsim | \log \delta | ^ {- 1} m ^ {- 1} \lambda^ {2} (\# \mathcal {S}) | S |.\tag{5.7}
$$

Proof. Fix$S \in S$. By Lemma 4.9 (applied to the outer John ellipsoid of each element of$s )$, we have that for each$t \in [ \delta , 1 ]$, we have

$$
\# \{S ^ {\prime} \in \mathcal {S} \colon | S \cap S ^ {\prime} | \sim t | S | \} \leq \# \{S ^ {\prime} \in \mathcal {S} \colon S ^ {\prime} \subset N _ {C \delta / t} (S) \} \lesssim m \frac {\delta}{t} | S | ^ {- 1} \sim \frac {m}{t},
$$

where$C = C ( n )$depends only on n. Thus

$$
\begin{array}{c}\Big\| \sum_{S\in \mathcal{S}}\chi_{Y(S)}\Big\|_{2}^{2}\leq \Big\| \sum_{S\in \mathcal{S}}\chi_{S}\Big\|_{2}^{2}\\ \lesssim \sum_{S\in \mathcal{S}}\sum_{\substack{\delta \leq t\leq 1\\ t\text{dyadic}}}\sum_{\substack{S^{\prime}\in \mathcal{S}\\ |S\cap S^{\prime}|\sim t|S|}}t|S|\\ \lesssim \sum_{S\in \mathcal{S}}\sum_{\substack{\delta \leq t\leq 1\\ t\text{dyadic}}}(\frac{m}{t})t|S|\lesssim |\log \delta |m(\# \mathcal{S})|S|. \end{array}\tag{5.8}
$$

Let$E = \textstyle \bigcup _ { S \in S } Y ( S )$. Using Cauchy-Schwartz, we have

$$
\left(\lambda | S | (\# \mathcal {S})\right) ^ {2} \leq \left(\int \chi_ {E} \sum_ {S \in \mathcal {S}} \chi_ {Y (S)}\right) ^ {2} \leq | E | \Big \| \sum_ {S \in \mathcal {S}} \chi_ {Y (S)} \Big \| _ {2} ^ {2}.\tag{5.9}
$$

The result now follows by comparing (5.8) and (5.9).

We will highlight a few instances where Lemma 5.7 will be helpful.

$( S , Y )$is$\delta ^ { \eta }$dense, and$C _ { F - C W } ( { \cal S } ) \lessapprox \delta ^ { - \eta }$. Then the RHS of (5.7) is$\gtrapprox \delta ^ { 3 \eta }$

• R is a set of$\delta \times 1$rectangles inside a$\rho \times 2$rectangle W: we will apply Lemma 5.7 to$\mathcal { R } ^ { W }$

• T is a set of δ-tubes inside a$1 0 0 \delta \times b \times 1$prism W: we will apply Lemma 5.7 to$\mathbb { T } ^ { W }$

## 5.1.2 Tangential vs transverse prism intersection

The next result says that if a collection of$a \times b \times 1$prisms intersect transversely, in the sense that their tangent planes make large angle at a typical point of intersection, then the union of these prisms fills out a large fraction of a thickened neighbourhood of these prisms. The precise statement is Lemma 5.10 and Corollary 5.13 below. Before stating that result, we need a few definitions.

Definition 5.8. Let$W \subset \mathbb { R } ^ { n }$, let$Y ( W ) \subset W$be a shading, and let$\delta > 0$. We say that the shading $Y ( W )$is regular at scales$\geq \delta$if for each$x \in Y ( W )$and each$r \in [ \delta , 1 ]$, we have

$$
| Y (W) \cap B (x, r) | \geq (1 0 0 \log (1 / \delta)) ^ {- 1} | Y (W) | \left(\frac {| B (x , r) \cap W |}{| W |}\right).\tag{5.10}
$$

If the quantity δ is apparent from context, then we will omit it and say that$Y ( W )$is regular.

The next lemma says after a harmless refinement, every shading has a regular subshading. This is Lemma 2.7 from [19]; see also [26, Lemma 2.3].

Lemma 5.9. Let$W \subset \mathbb { R } ^ { n }$and let$Y ( W )$be a shading. Then there is a regular shading$Y ^ { \prime } ( W ) \subset$ $Y ( W )$with$\vert Y ^ { \prime } ( W ) \vert \ge \frac { 1 } { 2 } \vert Y ( W ) \vert$

The next result says that if a prism$P _ { 0 }$is incident to many prisms that intersect$P _ { 0 }$non-tangentially, then the union of these prisms fills out a thickened neighbourhood of$P _ { 0 }$

Lemma 5.10. Let$0 < a \le b \le c$and let$\lambda > 0$. Let$P _ { 0 }$be${ \textit { a a } } \times { \textit { b } } \times { \textit { c } }$prism with shading$Y _ { 0 } ( P _ { 0 } )$ Let$( { \mathcal { P } } , Y ) _ { a \times b \times c }$be a set of prisms and their associated shading. Suppose that$| Y _ { 0 } ( P _ { 0 } ) | \ge \lambda | P _ { 0 } |$ $| Y ( P ) | \geq \lambda | P |$for each$P \in { \mathcal { P } }$; and each shading$Y ( P )$is regular, in the sense of Definition 5.8.

Let$\theta \in [ \frac { a } { b } , 1 ]$, and suppose that

$$
\theta \leq \theta_ {\min} := \frac {a}{b} + \inf _ {x \in Y _ {0} (P _ {0})} \sup _ {P \in \mathcal {P} _ {Y} (x)} \angle (\Pi (P _ {0}), \Pi (P)).
$$

Then

$$
\left| N _ {b \theta} (P _ {0}) \cap \bigcup_ {P \in \mathcal {P}} Y (P) \right| \gtrsim_ {a} \lambda^ {4} | N _ {b \theta} (P _ {0}) |.\tag{5.11}
$$

Remark 5.11. The exponent$\lambda ^ { 4 }$in (5.14) is not important — the exponent$\lambda ^ { 1 0 0 }$would work equally well for our applications of Lemma 5.10.

Proof. The argument is similar in spirit to Wolf’s hairbrush argument from [27]. After dyadic pigeonholing, we can select a number$\theta _ { 1 } \in [ \theta , 1 ]$and a set$Y _ { 0 } ^ { \prime } ( P _ { 0 } ) \subset Y _ { 0 } ( P _ { 0 } )$with$| Y _ { 0 } ^ { \prime } ( P _ { 0 } ) | \gtrapprox a \ | Y _ { 0 } ( P _ { 0 } )$ so that

$$
\sup _ {P \in \mathcal {P} _ {Y} (y)} \angle (\Pi (P _ {0}), \Pi (P)) \sim \theta_ {1} \quad \text { for   each } y \in Y _ {0} ^ {\prime} (P _ {0}).
$$

![](images/page_39_image_0.jpg)

Figure 6: The geometry of Lemma 5.10. For each$x \in Y _ { 0 } ( P _ { 0 } )$, there is a prism (red) from$\mathcal { P }$that intersects$P _ { 0 }$at x at angle at least$\theta _ { \mathrm { m i n } }$. For clarify, only two such prisms have been drawn. The union of these (red) prisms fills out a large fraction of every b-ball centered at a point of$P _ { 0 }$.

Applying Lemma 5.9 (and further refining$Y _ { 0 } ^ { \prime } ( P _ { 0 } )$by a factor of 2), we may suppose that$Y _ { 0 } ^ { \prime } ( P _ { 0 } )$is regular.

Let$\begin{array} { r } { b ^ { \prime } = b \frac { \theta } { \theta _ { 1 } } } \end{array}$; note that$a \leq b ^ { \prime } \leq b$. Divide$P _ { 0 }$into sub-prisms of dimensions$a \times b ^ { \prime } \times b ^ { \prime } ;$we have that$\gtrapprox \lambda \frac { \lvert P \rvert } { a ( b ^ { \prime } ) ^ { 2 } }$of these sub-prisms intersect$Y ( P )$. Thus to obtain (5.14), it sufices to show that for each$x \in Y ^ { \prime } ( P _ { 0 } )$, we have

$$
\left| N _ {b \theta} \big (P _ {0} \cap B (x, b ^ {\prime}) \big) \cap \bigcup_ {P \in \mathcal {P}} Y (P) \right| \gtrsim_ {a} \lambda^ {3} (b \theta) (b ^ {\prime}) ^ {2}.\tag{5.12}
$$

Fix a choice of$x \in Y ^ { \prime } ( P _ { 0 } )$. Our goal is to show that (5.12) holds for this choice of$x .$Let $E = Y ^ { \prime } ( P _ { 0 } ) \cap B ( x , b ^ { \prime } )$. Since the shading$Y ^ { \prime } ( P _ { 0 } )$is regular, we have$| E | \gtrapprox _ { a } \lambda a ( b ^ { \prime } ) ^ { 2 }$. For each$y \in E$2 let$P _ { y } \in \mathcal { P } _ { Y } ( y )$be a prism with$\angle ( \Pi ( P _ { 0 } ) , \Pi ( P ) ) \sim \theta _ { 1 }$

$B ( x , b ^ { \prime } ) \cap \cup _ { y \in E } P _ { y }$is contained in a prism of dimensions comparable to${ b \theta \times b ^ { \prime } \times b ^ { \prime } }$that is concentric with the$\dot { a } \times b ^ { \prime } \times b ^ { \prime }$prism$B ( x , b ^ { \prime } ) \cap P ;$denote this${ b \theta \times b ^ { \prime } \times b ^ { \prime } }$prism by$Q$. Then $\phi _ { Q } ( B ( x , b ^ { \prime } ) \cap P )$is comparable to a prism of dimensions$\textstyle { \frac { a } { b \theta } } \times 1 \times 1$. For notational convenience, we will select coordinates so that this prism is given by$\begin{array} { r } { \tilde { P } = [ 0 , \frac { a } { b \theta } ] \times [ 0 , 1 ] \times [ 0 , 1 ] } \end{array}$

For each$y \in E$, we have that$\phi _ { Q } ( B ( x , b ^ { \prime } ) \cap P _ { y } )$is comparable to a$\textstyle { \frac { a } { b \theta } } \times 1 \times 1$prism, and each such prism intersects the$\left( z _ { 2 } , z _ { 3 } \right)$-plane with angle ∼ 1, i.e. the projection of the normal vector$v _ { y }$ of this prism to the$\left( z _ { 2 } , z _ { 3 } \right)$plane has magnitude$\gtrsim 1$. Since the shading of each$P _ { y } \in \mathcal { P }$is regular, we have that$\phi _ { Q } \left( Y ( P _ { y } ) \cap B ( x , b ^ { \prime } ) \right)$is a subset of the prism$\phi _ { Q } \left( P _ { y } \cap B ( x , b ^ { \prime } ) \right)$that has density$\gtrapprox a \implies$

After pigeonholing, we can select a set$E ^ { \prime } \subset E$with$| E ^ { \prime } | \gtrsim | E |$, so that for each$y \in E ^ { \prime }$2 $\phi _ { Q } \big ( P _ { y } \cap B ( x , b ^ { \prime } ) \big )$is comparable to a$\textstyle { \frac { a } { b \theta } } \times 1 \times 1$prism whose normal vector$v _ { y }$makes angle$\leq 1 /$100 with some fixed unit vector v, and the projection of v to the$\left( z _ { 2 } , z _ { 3 } \right)$plane has magnitude$\gtrsim 1$. Let $v ^ { \prime }$be the projection of v to the$\left( z _ { 2 } , z _ { 3 } \right)$plane.

By Fubini, we can find a line segment$L \subset [ 0 , \frac { a } { b \theta } ] \times [ 0 , 1 ] \times [ 0 , 1 ]$pointing in direction$v ^ { \prime } ,$with $| L \cap \phi _ { Q } ( E ^ { \prime } ) | \geq | \phi _ { Q } ( E ^ { \prime } ) |$; here the left$| \cdot |$denotes one-dimensional Lebesgue measure, while the right | · | denotes three-dimensional Lebesgue measure. Let$\begin{array} { r } { y _ { 1 } , . . . , y _ { N } , N \gtrsim \frac { b \theta } { a } | L \cap \phi _ { Q } ( E ^ { \prime } ) | \gtrapprox _ { a } \lambda \frac { b \theta } { a } } \end{array}$ be a$\frac { a } { b \theta }$-separated subset of$L \cap \phi _ { Q } ( E ^ { \prime } )$, and let

$$
\mathcal {S} = \left\{\phi_ {Q} \big (P _ {y _ {i}} \cap B (x, b ^ {\prime}) \big): i = 1, \dots , N \right\}.
$$

$s$is a set of convex subsets of$\mathbb { R } ^ { 3 }$, each of which is comparable to a$\textstyle { \frac { a } { b \theta } } \times 1 \times 1$slab. Each$S \in { \mathcal { S } }$ has a${ \gtrapprox } a$λ-dense shading (the shading is the set$\phi _ { Q } \big ( Y ( P _ { y _ { i } } ) \cap B ( x , b ^ { \prime } ) \big ) )$, so in particular the pair $( S , Y ) _ { \frac { a } { b \theta } \times 1 \times 1 }$is${ \gtrapprox } a$λ dense.

We claim that$C _ { K T - C W } ( S ) \lesssim 1$. To verify this, let$W \subset \mathbb { R } ^ { 3 }$be a convex set, and suppose #$\left\{ S \in S \colon S \subset W \right\} = M$. We need to show that

$$
M \lesssim | W | | S | ^ {- 1}.\tag{5.13}
$$

If M = 0 there is nothing to prove. If$M = 1$, then clearly$| W | \geq | S |$. Suppose instead that$M \geq 2$ Then$\begin{array} { r } { | W \cap L | \ge ( M - 1 ) \frac { a } { b \theta } \ge \frac { M } { 2 b \theta } \gtrsim M | S | } \end{array}$, since$W \cap L$contains at least M points on L that are <sup>a</sup> -separated. On the other hand, sincea$S [ W ]$is non-empty, we know that$W$contains a$\textstyle { \frac { a } { b \theta } } \times 1 \times 1$ prism$S \in { \cal S } [ W ]$whose normal direction makes angle ≤ <sup>1</sup> with the direction of v (whose projection to the$\left( z _ { 2 } , z _ { 3 } \right)$-plane is$v ^ { \prime } ,$i.e. the direction of$L )$. Since W is convex,$W$contains the convex hull of$S \cup ( W \cap L )$, which has three-dimensional volume$\gtrsim | W \cap L | \gtrsim M | S |$. Thus$| W | \gtrsim M | S |$, which gives (5.13).

Applying Lemma 5.7 (a Cordoba-type$L ^ { 2 }$argument for slabs), we conclude that

$$
\Big | \bigcup_ {S \in \mathcal {S}} Y (S) \Big | \gtrsim_ {a} \lambda^ {2} (\# \mathcal {S}) | S | \gtrsim_ {a} \lambda^ {2} \left(\lambda \frac {b \theta}{a}\right) \left(\frac {a}{b \theta}\right) = \lambda^ {3}.
$$

To conclude the proof, we verify that

$$
\begin{array}{l} \Big | N _ {b \theta} \big (P _ {0} \cap B (x, b ^ {\prime}) \big) \cap \bigcup_ {P \in \mathcal {P}} Y (P) \Big | \geq \Big | N _ {b \theta} \big (P _ {0} \cap B (x, b ^ {\prime}) \big) \cap \bigcup_ {y \in E ^ {\prime}} Y (P _ {y}) \Big | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq (b \theta) (b ^ {\prime}) ^ {2} \Big | \phi_ {Q} \Big (B (x, b ^ {\prime}) \cap \bigcup_ {y \in E ^ {\prime}} Y (P _ {y}) \Big) \Big | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq (b \theta) (b ^ {\prime}) ^ {2} \Big | \phi_ {Q} \Big (B (x, b ^ {\prime}) \cap \bigcup_ {i = 1} ^ {N} Y (P _ {y _ {i}}) \Big) \Big | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq (b \theta) (b ^ {\prime}) ^ {2} \Big |   \bigcup_ {S \in S} Y (S)   \Big |   \gtrsim_ {a}   \lambda^ {3} (b \theta) (b ^ {\prime}) ^ {2}. \end{array}
$$

This establishes (5.12), as desired.

In practice, we will often use Lemma 5.10 in situations where each prism in$P _ { 0 } \in \mathcal { P }$satisfies the hypotheses of the lemma. The following definitions help make that precise.

Definition 5.12. Let$( { \mathcal { P } } , Y ) _ { a \times b \times c }$be a collection of prisms and their associated shading, and let $x \in \textstyle \bigcup _ { P \in { \mathcal { P } } } Y ( P )$. We define

$$
\theta (x) = \frac {a}{b} + \sup _ {P, P ^ {\prime} \in \mathcal {P} _ {Y} (x)} \angle (\Pi (P), \Pi (P ^ {\prime})),
$$

where${ \mathcal { P } } _ { Y } ( x ) = \{ P \in { \mathcal { P } } \colon x \in Y ( P ) \}$}. We define

$$
\theta_ {\mathrm{min}} = \inf \theta (x),
$$

where the infimum is taken over all$x \in \textstyle \bigcup _ { P \in { \mathcal { P } } } Y ( P )$. Note that$\theta _ { \mathrm { m i n } }$depends on the pair $( { \mathcal { P } } , Y ) _ { a \times b \times c }$. The choice of P and Y will be apparent from context.

Be considering each prism$P _ { 0 } \in \mathcal { P }$in turn, Lemma 5.10 now has the following corollary

Corollary 5.13. Let$0 < a \leq b \leq c , \lambda > 0$. Let$( { \mathcal { P } } , Y ) _ { a \times b \times c }$be a set of prisms and their associated shading. Suppose that each shading$Y ( P )$is regular, in the sense of Definition 5.8, and satisfies $| Y ( P ) | \geq \lambda | P |$. Then for each$P _ { 0 } \in \mathcal { P }$, we have

$$
\left| N _ {b \theta_ {\min}} (P _ {0}) \cap \bigcup_ {P \in \mathcal {P}} Y (P) \right| \gtrsim_ {a} \lambda^ {4} | N _ {b \theta_ {\min}} (P) |.\tag{5.14}
$$

## 5.2 Assertions${ \mathcal { F } } , { \mathcal { E } } ,$, and$\tilde { \mathcal { E } }$are equivalent

As noted in Remark 5.6, Situation 1, we have${ \mathcal F } ( \sigma , \omega ) \implies { \mathcal E } ( \sigma , \omega ) \implies \tilde { \mathcal { E } } ( \sigma , \omega )$. In this section we will prove that the reverse implications hold. More precisely, we have the following.

Proposition 5.14. Let 0 < σ ≤ 2/3, ω > 0. Then$\mathcal { F } ( \sigma , \omega ) \longleftrightarrow \mathcal { E } ( \sigma , \omega ) \longleftrightarrow \tilde { \mathcal { E } } ( \sigma , \omega )$

The goal of Section 5.2 is to prove Proposition 5.14. We begin with several lemmas that describe the structure of arrangements of rectangular prisms. Recall the quantity$\theta _ { \mathrm { m i n } }$from Definition 5.12. When$\theta _ { \operatorname* { m i n } } \sim 1$, then a typical pair of intersecting prisms intersect transversely, and by Corollary 5.13 this means that each prism can be replaced by a thickened neighbourhood that is comparable to an a-tube. In the next lemma, we will analyze what happens when$\theta _ { \mathrm { m i n } }$is small. I.e. we consider a collection of$a \times b \times 1$prisms P that intersect tangentially, in the sense that their tangent planes make small angle at a typical point of intersection.

Informally, the argument is as follows. We will begin by describing three Moves, which we will then apply repeatedly. Note that these are not the Moves described in Section 2.2 — those Moves will be described in Sections 7 and 8.

Since the tangent plane of a prism is constant along the entire prism, this means that the collection of prisms can be partitioned into smaller sub-collections$\mathcal { P } _ { 1 } , \ldots , \mathcal { P } _ { N }$, where for each index i, the normal vector of the tangent plane of each prism in$\mathcal { P } _ { i }$makes small angle with a fixed unit vector$v _ { i }$. If$\mathcal { P } _ { i }$and$\mathcal { P } _ { j }$are two such sub-collections, then the corresponding sets$\cup _ { P \in { \mathcal { P } } _ { i } } P$ and$\cup _ { P \in \mathcal { P } _ { i } } P$are mostly disjoint. We can cover the prisms in each set$\mathcal { P } _ { i }$by a set of slabs whose tangent planes have normal vector$v _ { i }$. We then rescale and continue this process inside each slab. This is Move$\# 1$

Next, we can apply Proposition 4.8 (factoring with respect to the Frostman Slab Wolf Axioms) to further break our collection of prisms into sub-collections, each of which satisfy the Frostman Slab Wolf Axioms with small error. This is Move$\# 2$

Finally we apply Lemma 5.9 (every shading has a regular sub-shading). This is Move$\# 3 .$

We iteratively apply Moves 1, 2, and 3 until our set of prisms$\mathcal { P }$has been covered by a set W of convex subsets of$\mathbb { R } ^ { 3 }$, so that each set$\mathcal { P } ^ { W }$satisfies the hypotheses of Corollary 5.13 with$\theta _ { \mathrm { m i n } }$about 1, and$\mathcal { P } ^ { W }$satisfies the Frostman Slab Wolf Axioms with error about 1. The precise statement is as follows.

Lemma 5.15. For all$\varepsilon > 0$, there exists$\eta , c > 0$so that the following holds for all$0 < a \le b \le 1$ Let$( \mathcal { P } , Y ) _ { a \times b \times 1 }$be$a ^ { \eta }$dense. Then there exists a refinement$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times 1 }$with$\sum _ { P ^ { \prime } \in \mathcal { P } ^ { \prime } } | Y ^ { \prime } ( P ^ { \prime } ) | \gtrapprox$a $a ^ { \varepsilon } \sum _ { P \in { \mathcal { P } } } | P |$and cover W of P<sup>′</sup> by congruent convex sets, such that the following holds.

(A) The shading$Y ^ { \prime }$is regular, in the sense of Definition 5.8.

(B) W is$a \approx a$1 balanced cover of${ \mathcal { P } } ^ { \prime }$, and factors${ \mathcal { P } } ^ { \prime }$from below with respect to the Frostman Slab Wolf axioms, with error$a ^ { - \varepsilon }$

(C) All of the convex sets in$\cup _ { W \in \mathcal { W } } \mathcal { P } ^ { \prime W }$have the same dimensions up to a multiplicative factor of 2, i.e. each one is comparable (after a suitable rigid transformation) to a common convex set$\tilde { P }$(see Remark 5.16 below).

(D) For each$W \in \mathcal W _ { : }$, the sets$\mathcal { P } ^ { \prime W }$and their associated shading satisfy$\theta _ { \mathrm { m i n } } \geq a ^ { \varepsilon }$, in the sense of Definition 5.12.

(E) The sets$\begin{array} { r } { \bigcup _ { P ^ { \prime } \in \mathcal P ^ { \prime } [ W ] } Y ^ { \prime } ( P ) } \end{array}$$W \in \mathcal { W }$are pairwise disjoint.

Remark 5.16. Note that even though the prisms in$\mathcal { P } \left( \mathrm { r e s p . } \ \mathcal { W } \right)$all have the same dimensions, it could happen that the prisms in$\mathcal { P } ^ { W }$have difering dimensions — see Figure 7 for an example of this phenomena. Conclusion (C) (which is achieved by pigeonholing) ensures that this does not happen.

![](images/page_42_image_2.jpg)

Figure 7: An example where the convex sets$P _ { 1 }$and$P _ { 2 }$are congruent, and$U _ { 1 }$and$U _ { 2 }$are congruent, but$\phi _ { U _ { 1 } } ( P _ { 1 } )$and$\phi _ { U _ { 2 } } ( P _ { 2 } )$are not congruent.

Proof. The main ideas of the proof were already outlined above; in brief, we apply Moves 1, 2, and 3 described above, in that order. We iteratively repeat this process until Conclusions$( \mathrm { A } ) , ( \mathrm { B } ) , ( \mathrm { D } )$ and (E) of Lemma 5.15 are satisfied. Each iteration increases the volume of each surviving convex set by at least$a ^ { - \varepsilon }$. On the other hand, each convex set initially had volume$a b \geq a ^ { 2 }$, and at each step all convex sets are contained inside the unit ball, and thus have volume at most$O ( 1 )$. Hence the iterative process detailed above halts after at most$2 / \varepsilon$steps. If$\eta > 0$is chosen suficiently small (depending on ε), then the resulting refinement will satisfy$\begin{array} { r } { \sum _ { P ^ { \prime } \in \mathcal { P ^ { \prime } } } | Y ^ { \prime } ( P ^ { \prime } ) | \gtrapprox _ { a } a ^ { \varepsilon } \sum _ { P \in \mathcal { P } } | P | } \end{array}$ Finally, we dyadically pigeonhole the set${ \mathcal { P } } ^ { \prime }$to select a refinement that satisfies Conclusion (C).

We are now ready to prove Proposition 5.14. The idea is as follows. Given a set$( \mathcal { P } , Y ) _ { a \times b \times 1 }$of prisms, we apply Lemma 5.15 to cover a refinement of$\mathcal { P }$by a collection of convex sets W, and then apply Corollary 5.13 to each collection$\mathcal { P } ^ { W }$— this gives us a collection of$\tilde { b }$tubes associated to$\mathcal { P } ^ { W }$ for some$\tilde { b } \geq b$. The collection of$\tilde { b }$tubes satisfies the Frostman Slab Wolf axioms with error$\lessapprox 1$ and satisfies the Katz-Tao Convex Wolf axioms with some error ˜m that we will analyze later. We now apply the estimate$\tilde { \mathcal { E } } ( \sigma , \omega )$to this collection of$\tilde { b }$tubes, and then undo the transformation$\phi _ { W }$ Summing the contributions from each$W \in { \mathcal { W } }$, we obtain an estimate for$\left| \bigcup Y ( P ) \right|$that becomes better as$\tilde { m }$becomes larger. Thus we are faced with the task of estimating the size of$\tilde { m } -$this quantity is closely related to the quantity D from (5.6). We now turn to the details.

Proof of Proposition${ 5 . 1 4 }$. It sufices to prove that$\tilde { \mathcal { E } } ( \sigma , \omega ) \implies \mathcal { F } ( \sigma , \omega )$. Fix$0 < \sigma \leq 2 / 3 , \ \omega > 0$2 and suppose$\tilde { \mathcal { E } } ( \sigma , \omega )$is true. Fix$\varepsilon > 0$. Then there exists$\eta _ { 0 } > 0$so that the volume estimate (5.4) holds for all pairs$( \mathbb { T } , Y ) _ { \delta }$that are$\delta ^ { \eta _ { 0 } }$dense and satisfy$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta _ { 0 } }$

Let$\kappa , \eta > 0$be quantities to be determined below. Let$0 < a \le b \le 1$and let$( \mathcal { P } , Y ) _ { a \times b \times 1 }$be $a ^ { \eta }$dense. Our goal is to prove that

$$
\Big | \bigcup_ {P \in \mathcal {P}} Y (P) \Big | \geq \kappa a ^ {\varepsilon} b ^ {\omega} m ^ {- 1} (\# \mathcal {P}) | P | (m ^ {- 3 / 2} \ell (\# \mathcal {P}) | P | ^ {1 / 2}) ^ {- \sigma} D ^ {- \sigma},\tag{5.15}
$$

with$m , \ell ,$and$D$as defined in (5.6).

Step 1. Let$\eta _ { 1 }$be a small quantity to be determined later (we will select$\eta _ { 1 }$very small compared to$\eta _ { 0 }$, and η very small compared to$\eta _ { 1 } )$. We will choose$\eta > 0$suficiently small so that we can apply Lemma 5.15 with$\eta _ { 1 } / 4$in place of$\varepsilon$to$( \mathcal { P } , Y ) _ { a \times b \times 1 }$. Denote the output of that lemma by $( \mathcal { P } _ { 1 } , Y _ { 1 } ) _ { a \times b \times 1 }$and W. By Conclusion (B) of Lemma 5.15 we have$C _ { F - S W } ( \bar { \mathcal { P } } _ { 1 } ^ { W } ) \leq a ^ { - \eta _ { 1 } / 4 }$for each $W \in \mathcal { W } _ { 1 }$. By Conclusion (E) of Lemma 5.15, we have

$$
\Big | \bigcup_ {P \in \mathcal {P}} Y (P) \Big | \geq \sum_ {W \in \mathcal {W}} \Big | \bigcup_ {P \in \mathcal {P} _ {1} [ W ]} Y _ {1} (P) \Big |.\tag{5.16}
$$

By Conclusion (C) of Lemma 5.15, there are numbers$\tilde { a } \le \tilde { b } \le 1$with$\tilde { b } \geq b$so that for each $W \in \mathcal { W }$and each$\dot { P } ^ { \dot { W } } \in \mathcal { P } _ { 1 } ^ { W } , \ P ^ { W }$is comparable to a$\tilde { a } \times \tilde { b } \times 1$prism. Conclusions (A) and (D) of Lemma 5.15 say that for each$W \in \mathcal { W }$, the pair$( \mathcal { P } _ { 1 } ^ { W } , Y _ { 1 } ^ { W } ) _ { \tilde { a } \times \tilde { b } \times 1 }$satisfies the hypotheses of Corollary 5.13, and hence we can apply Corollary 5.13 to conclude that for each$P ^ { W } \in \mathcal { P } _ { 1 } ^ { W }$we have

$$
\left| N _ {\tilde {b}} (P ^ {W}) \cap \bigcup_ {P ^ {\prime W} \in \mathcal {P} _ {1} ^ {W}} Y _ {1} ^ {W} (P ^ {\prime W}) \right| \gtrsim a ^ {\eta_ {1}} | N _ {\tilde {b}} (P ^ {W}) |.\tag{5.17}
$$

In words, (5.17) says the following: for each$P ^ { W } \in \mathcal { P } _ { 1 } ^ { W }$, the set$N _ { \tilde { b } } ( P ^ { W } )$is comparable to a <sup>˜</sup>b-tube. This <sup>˜</sup>b-tube has almost full intersection with the union of shadings$\begin{array} { r } { \bigcup _ { P ^ { \prime } W \in \mathcal { P } _ { 1 } ^ { W } } Y _ { 1 } ^ { W } ( P ^ { \prime W } ) } \end{array}$. See Figure 6 for an illustration of this situation.

Step 2. As noted above, each set$N _ { \tilde { b } } ( P ^ { W } )$is comparable to a$\tilde { b }$tube. Let$\mathbb { T } _ { W }$be a maximal, essentially distinct subset of$\{ N _ { \tilde { b } } ( P ^ { W } ) \colon { P ^ { W } } \in \mathcal { P } _ { 1 } ^ { W } \}$. For each$T \in \mathbb { T } _ { W }$, define the shading

$$
Y (T) = T \cap \bigcup_ {P ^ {W} \in \mathcal {P} _ {1} ^ {W}} Y _ {1} ^ {W} (P ^ {W}).
$$

Then (5.17) says that$( \mathbb { T } _ { W } , Y ) _ { \widetilde { b } } \mathrm { i s } \gtrsim a ^ { \eta _ { 1 } }$dense. After pigeonholing and refining$\mathcal { W }$and$\mathbb { T } _ { W }$(which induces a refinement on$\mathcal { P } _ { 1 } ^ { W } )$, we can ensure that$\# \mathcal { P } _ { 1 } ^ { W } [ T ]$is roughly the same (up to a factor of 2) for each$T \in \mathbb { T } _ { W } , W \in \mathcal { W }$. Abusing notation, we continue to refer to these refined sets as$\mathcal { W } ,$<sup>T</sup><sub>W</sub> and$\mathcal { P } _ { 1 } ^ { W }$

At this point,$\mathbb { T } _ { W }$is a balanced cover of$\mathcal { P } _ { 1 } ^ { W }$, and we still have$C _ { F - S W } ( \mathcal { P } _ { 1 } ^ { W } ) \lessapprox a ^ { - 2 \eta _ { 1 } }$. Since$\mathbb { T } _ { W }$ is a balanced cover of$\mathcal { P } _ { 1 } ^ { W }$, by Remark 4$\mathrm { . . 3 ( A ) ~ ( i . e }$. Frostman Wolf constants are inherited upwards), we have that$\begin{array} { r } { \tilde { \ell } : = \operatorname* { m a x } _ { W \in \mathcal { W } } C _ { F - S W } ( \mathbb { T } _ { W } ) \lesssim _ { a } { \bar { a } } ^ { - 2 \eta _ { 1 } } } \end{array}$. Finally, define$\tilde { m } : = \operatorname* { m a x } _ { W \in \mathcal { W } } C _ { K T - C W } ( \mathbb { T } _ { W } )$

Step 3. At this point, we have covered our set of prisms$\mathcal { P } _ { 1 }$by a collection of convex sets W. For each rescaled set$\mathcal { P } _ { 1 } ^ { W }$, we have located a collection of tubes$\mathbb { T } _ { W }$, whose shadings are almost full. The relation between the volumes of these objects is as follows:

$$
\Big | \bigcup_ {P \in \mathcal {P} _ {1} [ W ]} Y _ {1} (P) \Big | \sim | W | \Big | \bigcup_ {P ^ {W} \in \mathcal {P} _ {1} ^ {W}} Y _ {1} ^ {W} (P ^ {W}) \Big | \geq | W | \Big | \bigcup_ {T \in \mathbb {T} _ {W}} Y (T) \Big |.\tag{5.18}
$$

Our next task is to estimate the volume of$\cup _ { \mathbb { T } _ { W } } Y ( T )$. First we consider the case where$\tilde { b } \le a ^ { \varepsilon / 5 }$ In this case,$( \mathbb { T } _ { W } , Y ) _ { \tilde { b } } \ \mathrm { i s } \gtrsim \tilde { b } ^ { 5 \eta _ { 1 } / \varepsilon }$dense, and$C _ { F - S W } ( \mathbb { T } _ { W } ) \lesssim _ { a } \tilde { b } ^ { - 1 0 \eta _ { 1 } / \varepsilon }$. If$\eta _ { 1 }$is selected suficiently small depending on$\eta _ { 0 }$and ε (for example,$\eta _ { 1 } = \varepsilon \eta _ { 0 } / 2 0$will sufice), then we can apply the estimate $\tilde { \mathcal { E } } ( \sigma , \omega )$with$\varepsilon / 2$in place of$\varepsilon$to conclude that

$$
\begin{array}{c} \Big | \bigcup_ {T \in \mathbb {T} _ {W}} Y (T) \Big | \gtrsim \tilde {b} ^ {\omega + \varepsilon / 2} \tilde {m} ^ {- 1} (\# \mathbb {T} _ {W}) | T | \Big (\tilde {m} ^ {- 3 / 2} \tilde {\ell} (\# \mathbb {T} _ {W}) | T | ^ {1 / 2} \Big) ^ {- \sigma} \\ \gtrsim_ {a} a ^ {\varepsilon / 2 + 2 \eta_ {1} \sigma} b ^ {\omega} \tilde {m} ^ {- 1} (\# \mathbb {T} _ {W}) | T | \Big (\tilde {m} ^ {- 3 / 2} (\# \mathbb {T} _ {W}) | T | ^ {1 / 2} \Big) ^ {- \sigma}. \end{array}
$$

(5.19)

On the other hand, if$\tilde { b } \geq a ^ { \varepsilon / 5 }$, then the estimate (5.19) follows from the fact that for every$T \in \mathbb { T } _ { W }$ we have

$$
\Big | \bigcup_ {T \in \mathbb {T} _ {W}} Y (T) \Big | \geq | Y (T) | \gtrsim a ^ {\eta_ {1}} \tilde {b} ^ {2} \geq a ^ {\varepsilon / 2},\tag{5.20}
$$

which is stronger than (5.19).

Step 4. We have estimated the volume of$\textstyle \bigcup _ { \mathbb { T } _ { W } } Y ( T )$for each$W \in { \mathcal { W } }$. Our next task is to combine these estimates in order to estimate the volume of$\textstyle \bigcup _ { P \in { \mathcal { P } } } Y ( P )$

We know that each prism$W \in \mathcal { W }$has the same dimensions up to a factor of$2 ;$call these dimensions$s \times t \times 1$. Then for each$W \in { \mathcal { W } }$and each$T \in \mathbb { T } _ { W }$, we have that$\phi _ { W } ^ { - 1 } ( T )$is comparable to a rectangular prism of dimensions$s \tilde { b } \times t \tilde { b } \times 1$

Let$\hat { \mathcal { P } } _ { W } = \{ \phi _ { W } ^ { - 1 } ( T ) : T \in \mathbb { T } _ { W } \}$, i.e.$\hat { \mathcal { P } } _ { W }$is a set of$s \tilde { b } \times t \tilde { b } \times 1$prisms contained in$W ; \left| T \right| \sim$ $| { \hat { P } } | / | W | ;$and$\# \hat { \mathcal { P } } _ { W } = \# \mathbb { T } _ { W }$. For each$W \in \mathcal { W }$and each$\hat { P } = \phi _ { W } ^ { - 1 } ( T ) \in \hat { \mathcal { P } } _ { W }$, define the natural shading$\hat { Y } ( \hat { P } ) = \phi _ { W } ^ { - 1 } ( Y ( T ) )$

(5.16) allows us to combine the (rescaled) volume estimates (5.18) and (5.19) from each$W \in { \mathcal { W } }$ Defining$\mathcal { \hat { P } } = \sqcup \hat { \mathcal { P } } _ { W }$, we have

$$
\begin{array}{r l} & {\Big | \bigcup_ {P \in \mathcal {P}} Y (P) \Big | \gtrsim_ {a} | W | \sum_ {W \in \mathcal {W}} \Big [ a ^ {\varepsilon / 2 + \eta_ {1} \sigma} b ^ {\omega} \tilde {m} ^ {- 1} (\# \hat {\mathcal {P}} _ {W}) \frac {| \hat {P} |}{| W |} \Big (\tilde {m} ^ {- 3 / 2} (\# \hat {\mathcal {P}} _ {W}) \Big (\frac {| \hat {P} |}{| W |} \Big) ^ {1 / 2} \Big) ^ {- \sigma} \Big ].} \\ & {\qquad \approx_ {a} a ^ {\varepsilon / 2 + \eta_ {1} \sigma} b ^ {\omega} \tilde {m} ^ {- 1} (\# \hat {\mathcal {P}}) | \hat {P} | \Big (\tilde {m} ^ {- 3 / 2} \frac {\# \hat {\mathcal {P}}}{\# \mathcal {W}} \Big (\frac {| \hat {P} |}{| W |} \Big) ^ {1 / 2} \Big) ^ {- \sigma}.} \end{array}\tag{5.21}
$$

Step 5. To understand the RHS of (5.21) we must estimate$\tilde { m }$. Recall that in Step 2, we have pigeonholed to ensure that$\# \mathcal { P } _ { 1 } ^ { W } [ T ]$is roughly the same for each$T \in \mathbb { T } _ { W } , \ W \in \mathcal { W }$. Thus each $\hat { P } \in \hat { \mathcal { P } }$satisfies$\begin{array} { r } { \# \mathcal { P } _ { 1 } [ \hat { P } ] \approx _ { a } \frac { \# \mathcal { P } _ { 1 } } { \# \hat { P } } } \end{array}$. Thus we have

$$
\tilde {m} \lesssim_ {a} m \frac {| \hat {P} |}{| P |} \frac {\# \hat {\mathcal {P}}}{\# \mathcal {P} _ {1}}.\tag{5.22}
$$

Thus we can estimate the RHS of (5.21) as follows.

$$
\begin{array}{r l} & {\Big | \bigcup_ {P \in \mathcal {P}} Y (P) \Big | \gtrsim_ {a} a ^ {\varepsilon / 2 + \eta_ {1} \sigma} b ^ {\omega} m ^ {- 1} (\# \mathcal {P} _ {1}) | P | \Big (m ^ {- 3 / 2} \Big (\frac {| P |}{| \hat {P} |} \frac {\# \mathcal {P} _ {1}}{\# \hat {\mathcal {P}}} \Big) ^ {3 / 2} \frac {\# \hat {\mathcal {P}}}{\# \mathcal {W}} \Big (\frac {| \hat {P} |}{| W |} \Big) ^ {1 / 2} \Big) ^ {- \sigma}} \\ & {\qquad \gtrsim_ {a} a ^ {\varepsilon / 2 + 3 \eta_ {1}} b ^ {\omega} m ^ {- 1} (\# \mathcal {P}) | P | \Big (m ^ {- 3 / 2} (\# \mathcal {P}) | P | ^ {1 / 2} \Big) ^ {- \sigma}} \\ & {\qquad \cdot \left[ (\# \mathcal {W}) | W | ^ {1 / 2} \right] ^ {\sigma} \Big [ \frac {| P |}{| \hat {P} |} \Big (\frac {\# \mathcal {P}}{\# \hat {\mathcal {P}}} \Big) ^ {1 / 2} \Big ] ^ {- \sigma}.} \end{array}\tag{5.23}
$$

In the above computation, we used the fact that$\# \mathcal { P } _ { 1 } \gtrapprox _ { a } \delta ^ { - \eta _ { 1 } } ( \# \mathcal { P } )$

Step 6. Compare the RHS of (5.23) with (5.15). It remains to analyze the final two terms on the RHS of (5.23). We begin with the penultimate term. Since the sets in$\mathcal { W }$are convex and have diameter ∼ 1, each$W \in { \mathcal { W } }$is contained in a slab of volume$O ( | W | ^ { 1 / 2 } )$. Thus

$$
\# \mathcal {P} _ {1} [ W ] \lesssim C _ {F - S W} (\mathcal {P}) | W | ^ {1 / 2} (\# \mathcal {P}).
$$

Since$\# \mathcal { P } _ { 1 } [ W ] \approx _ { a } \frac { \# \mathcal { P } _ { 1 } } { \# \mathcal { W } } \gtrapprox _ { a } a ^ { \eta _ { 1 } } \frac { \# \mathcal { P } } { \# \mathcal { W } }$, we conclude that$( \# \mathcal { W } ) | W | ^ { 1 / 2 } \gtrapprox _ { a } a ^ { \eta _ { 1 } } C _ { F - S W } ( \mathcal { P } ) ^ { - 1 } = a ^ { \eta _ { 1 } } \ell ^ { - 1 }$

Step 7. We now turn to the final term on the RHS of (5.23). Recall that P is a collection of prisms of dimensions$a \times b \times 1$, while$\hat { \mathcal { P } }$is a collection of prisms that all have the same, but unknown, dimensions$s \tilde { b } \times t \tilde { b } \times 1 -$call these dimensions$a ^ { \prime } \times b ^ { \prime } \times 1$, with$a \leq a ^ { \prime } \leq b ^ { \prime }$and$b ^ { \prime } \geq b$. Our desired estimate (5.15) will follow from (5.23) and the estimate

$$
\frac {| P |}{| \hat {P} |} \Bigl (\frac {\# \mathcal {P}}{\# \hat {\mathcal {P}}} \Bigr) ^ {1 / 2} \lesssim D = \max _ {P \in \mathcal {P}} \sup _ {\rho \in [ a, b ]} \frac {| P |}{| N _ {\rho} (P) |} \bigl (\# \mathcal {P} [ N _ {\rho} (P) ] \bigr) ^ {1 / 2}.\tag{5.24}
$$

Fix$\hat { P } \in \hat { \mathcal { P } }$. Let${ \mathcal { P } } ^ { \dagger }$be a maximal set of essentially distinct min$( a ^ { \prime } , b ) \times b \times 1$prisms contained in$\hat { P }$, so that each$P \in \mathcal { P } [ \hat { P } ]$is contained in at least one$P ^ { \dagger } \in { \mathcal { P } } ^ { \dagger }$. We claim that

$$
\# \mathcal {P} ^ {\dagger} \sim (| \hat {P} | / | P ^ {\dagger} |) ^ {2}.\tag{5.25}
$$

Indeed, when$a ^ { \prime } \leq b ,$the RHS of (5.25) is$( b ^ { \prime } / b ) ^ { 2 }$and the numerology comes from the fact that a $b ^ { \prime } \times 1$rectangle can be filled with about$( b ^ { \prime } / b ) ^ { 2 }$essentially distinct$b \times 1$rectangles. When$a ^ { \prime } \geq b$ the RHS of (5.25) is$( a ^ { \prime } b ^ { \prime } / b ^ { 2 } ) ^ { 2 }$, and the numerology comes from the fact that a$a ^ { \prime } \times b ^ { \prime } \times 1$prism can be filled with about$( b ^ { \prime } / a ^ { \prime } ) ^ { 2 }$essentially distinct$a ^ { \prime } \times a ^ { \prime } \times 1$tubes, and each of these tubes can be filled with about$( a ^ { \prime } / b ) ^ { 4 }$essentially distinct$b \times b \times 1$tubes.

By the definition of D, we have$\begin{array} { r } { D \ge \frac { | P | } { | P ^ { \dagger } | } \big ( \# \mathcal { P } [ P ^ { \dagger } ] \big ) ^ { 1 / 2 } } \end{array}$, i.e.$\begin{array} { r } { \# \mathcal { P } [ P ^ { \dagger } ] \leq \big ( D \frac { | P ^ { \dagger } | } { | P | } \big ) ^ { 2 } } \end{array}$. Thus by (5.25),

$$
\# \mathcal {P} [ \hat {P} ] \lesssim \Big (\frac {| \hat {P} |}{| P ^ {\dagger} |} \Big) ^ {2} \# \mathcal {P} [ P ^ {\dagger} ] \lesssim \Big (\frac {| \hat {P} |}{| P ^ {\dagger} |} \Big) ^ {2} \Big (D \frac {| P ^ {\dagger} |}{| P |} \Big) ^ {2},
$$

which is (5.24).

## 5.3 Proof of Proposition 5.1: Tubes that factor through flat boxes

With Proposition 5.14 in hand, we are now ready to prove Proposition 5.1. Fix$\omega > 0 , 0 < \sigma \le 2 / 3$ and suppose$\mathcal { E } ( \sigma , \omega )$is true (and thus by Proposition$5 . 1 4 , \mathcal { F } ( \sigma , \omega )$is true). Let$\kappa , \eta > 0$be small quantities to be specified below. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, let$\delta \leq a \leq b \leq 1$, and let W be a set of congruent copies of an$a \times b \times 2$prism$W _ { 0 }$, as described in the statement of Proposition 5.1.

Step 1. After dyadic pigeonholing, we can find a refinement$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$of$( \mathbb { T } , Y ) _ { \delta }$with$\sum _ { T \in \mathbb { T } _ { 1 } } \left. Y _ { 1 } ( T ) \right. \gtrapprox \delta$ $\textstyle \sum _ { T \in \mathbb { T } } | Y ( T ) |$, and a subset$\mathcal { W } _ { 1 } \subset \mathcal { W }$so that for each$W \in \mathcal { W } _ { 1 }$and each$x \in \bigcup _ { T \in \mathbb { T } _ { 1 } [ W ] } \bar { Y _ { 1 } } ( T )$, we have

$$
\left| B (x, a) \cap \bigcup_ {T \in \mathbb {T}} Y (T) \right| \sim \lambda | B (x, a) |, \quad \text { with } \quad \lambda \geq | W | ^ {- 1} \Big | \bigcup_ {T \in \mathbb {T} _ {1} [ W ]} Y _ {1} (T) \Big |,\tag{5.26}
$$

where the “density”$\lambda = \lambda ( W )$is the same (up to a factor of 2) for all$W \in \mathcal { W }$. In words, (5.26) says that if we blur the shading$\textstyle \bigcup _ { \mathbb { T } _ { 1 } \lceil W \rceil } Y _ { 1 } ( T )$at scale a (for example by convolving with the characteristic function of$B ( 0 , a ) )$, then each point in the shading has density$\sim \lambda$

After further pigeonholing, we can ensure that each set$( \mathbb { T } _ { 1 } [ W ] , Y _ { 1 } ) _ { \delta } , W \in \mathcal { W } _ { 1 } { \mathrm { i s } } \approx _ { \delta } \delta ^ { O ( \eta ) }$dense; $\mathcal { W } _ { 1 }$is a$\approx _ { \delta } \delta ^ { - O ( \eta ) }$balanced cover of$\mathbb { T } _ { 1 } ;$; and each set$\mathbb { T } _ { 1 } ^ { W }$obeys the Frostman Convex Wolf axioms with error${ \lesssim } \delta ^ { - O ( \eta ) }$. Abusing notation, we will continue to refer to the output of this pigeonholing by$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$and$\mathcal { W } _ { 1 }$

Step 2. Fix$W \in \mathcal { W } _ { 1 }$. Then$( \mathbb { T } _ { 1 } ^ { W } , Y _ { 1 } ^ { W } ) _ { \delta / b \times \delta / a \times 1 }$is a collection of convex sets, each comparable to ${ \textrm { a } } \delta / b \times \delta / a \times 1$prism, with a$\delta ^ { { \cal O } ( \eta ) }$-dense shading. We first consider the case where$b \geq \delta ^ { 1 - \varepsilon / 1 0 0 }$, so $\delta / \dot { b } \le \delta ^ { \varepsilon / 1 0 0 }$. In this case, the shading on$( \mathbb { T } _ { 1 } ^ { W } , Y _ { 1 } ^ { W } ) _ { \delta / b \times \delta / a \times 1 }$is$( \delta / b ) ^ { O ( \eta ) / \varepsilon }$dense. If η is selected suficiently small, then we can apply the estimate$\mathcal { F } ( \sigma , \omega )$with$\varepsilon / 2$in place of$\varepsilon$(recall that$\mathcal { F } ( \sigma , \omega )$ is true in light of Proposition 5.14) to conclude that

$$
\Big | \bigcup_ {T ^ {W} \in \mathbb {T} _ {1} ^ {W}} Y _ {1} ^ {W} (T ^ {W}) \Big | \geq \kappa_ {\varepsilon} \big (\frac {\delta}{b} \big) ^ {\varepsilon / 2} \big (\frac {\delta}{a} \big) ^ {\omega} m _ {W} ^ {- 1} (\# \mathbb {T} ^ {W}) | T ^ {W} | \Big (m _ {W} ^ {- 3 / 2} \ell_ {W} (\# \mathbb {T} ^ {W}) | T ^ {W} | ^ {1 / 2} \Big) ^ {- \sigma},\tag{5.27}
$$

where m<sub>W</sub>$\mathbf { \Psi } _ { \prime } = C _ { K T - C W } ( \mathbb { T } ^ { W } )$and$\ell _ { W } = C _ { F - S W } ( \mathbb { T } ^ { W } ) \le C _ { F - C W } ( \mathbb { T } ^ { W } ) \lesssim \delta \delta ^ { - O ( \eta ) }$. Recall as well that $| T ^ { W } | \sim | T | / | W |$. Note that the estimate$\mathcal { F } ( \sigma , \omega )$involves the additional term$^ { 6 6 } D ^ { 9 }$defined in (5.6), but as discussed in Remark 5.6, Situation 3, we have$D \lesssim 1$

Since$C _ { F - C W } ( \mathbb { T } ^ { W } ) \precsim _ { \delta } \delta ^ { - O ( \eta ) }$, we have that m$\lesssim _ { \delta } \delta ^ { - O ( \eta ) } | T ^ { W } | ( \# \mathbb { T } ^ { W } )$, and thus (5.27) allows us to estimate the density λ (recall that λ was defined in (5.26)):

$$
\lambda \geq \Big | \bigcup_ {T ^ {W} \in \mathbb {T} ^ {W}} Y ^ {W} (T ^ {W}) \Big | \gtrsim_ {\delta} \kappa_ {\varepsilon} \big (\frac {\delta}{b} \big) ^ {\varepsilon / 2} \delta^ {O (\eta)} \big (\frac {\delta}{a} \big) ^ {\omega} \Big ((\# \mathbb {T} ^ {W}) ^ {1 / 2} | T ^ {W} | \Big) ^ {\sigma}.\tag{5.28}
$$

Note that Inequality (5.28) is currently only valid when$b ~ \geq ~ \delta ^ { 1 - \varepsilon / 1 0 0 }$. Next we consider the case where$b < \delta ^ { 1 - \varepsilon / 1 0 0 }$, so each$T ^ { W } \in \mathbb { T } _ { 1 } ^ { W }$has dimensions comparable to$d _ { 1 } \times d _ { 2 } \times 1$for some $1 \geq d _ { 2 } \geq d _ { 1 } \geq \delta ^ { \varepsilon / 1 0 0 }$. This is true because

$$
\lambda \geq | Y ^ {W} (T ^ {W}) | \geq \delta^ {O (\eta)} | T ^ {W} | \geq \delta^ {\varepsilon / 5 0 + O (\eta)} \geq \delta^ {\varepsilon / 1 0}.
$$

Step 3. For each$W \in \mathcal { W } _ { 1 }$, define the shading

$$
\tilde {Y} _ {1} (W) = W \cap N _ {a} \Big (\bigcup_ {T \in \mathbb {T} _ {1} [ W ]} Y _ {1} (T) \Big).
$$

By (5.26), we have

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \lambda \Big | \bigcup_ {W \in \mathcal {W} _ {1}} \tilde {Y} _ {1} (W) \Big |.\tag{5.29}
$$

Our next task is to show that$( \mathcal { W } _ { 1 } , \tilde { Y } _ { 1 } ) _ { a \times b \times 1 }$is$\delta ^ { { \cal O } ( \eta ) }$dense. The argument is shown in Figure 8. Fix$W \in { \mathcal { W } }$. Since$( \mathbb { T } _ { 1 } ^ { W } , Y _ { 1 } ^ { W } ) { \mathrm { ~ i s } } \gtrapprox \delta ^ { O ( \eta ) }$dense, we can select a refinement so that each$T \in \mathbb { T } _ { 1 } [ W ]$ satisfies$| Y _ { 1 } ( T ) | \gtrapprox \delta ^ { O ( \eta ) } | T |$. After pigeonholing, we can select a set$\mathbb { T } _ { a }$of essentially distinct a-tubes that form a${ \approx } _ { \delta }$1 balanced cover of$\mathbb { T } _ { 1 } [ W ]$. Since$( \mathbb { T } _ { 1 } ^ { W } , Y _ { 1 } ^ { W } )$satisfies the Frostman Convex Wolf axioms with error$\lessapprox \delta \delta ^ { - O ( \eta ) }$, we have that$\mathbb { T } _ { a }$satisfies the Frostman Convex Wolf axioms with error$\lessapprox \delta \delta ^ { - O ( \eta ) }$. The shading$\begin{array} { r } { Y _ { a } ( T _ { a } ) = T _ { a } \cap N _ { a } \big ( \bigcup _ { T \in \mathbb { T } [ W ] } Y _ { 1 } ( T ) \big ) } \end{array}$is${ \approx } _ { \delta } ~ \delta ^ { { \cal O } ( \eta ) }$dense. Applying Lemma 5.7 to$( \mathbb { T } _ { a } ^ { W } , Y _ { a } ^ { W } ) _ { a / b \times 1 \times 1 }$and then undoing the scaling ϕ<sub>W</sub>, we conclude that

$$
\Big | W \cap N _ {a} \Big (\bigcup_ {T \in \mathbb {T} _ {1} [ W ]} Y _ {1} (T) \Big) \Big | \geq \Big | \bigcup_ {T _ {a} \in \mathbb {T} _ {a}} Y _ {a} (T _ {a}) \Big | \gtrsim_ {\delta} \delta^ {O (\eta)} | W |.
$$

Step 4. It remains to estimate the RHS of (5.29). We first consider the case where$a \leq \delta ^ { \varepsilon / 1 0 0 }$. In this case,$( \mathcal { W } _ { 1 } , \tilde { Y } _ { 1 } ) _ { a \times b \times 1 }$is$a ^ { O ( \eta / \varepsilon ) }$dense. If$\eta$is selected suficiently small depending on ε, then we can apply the estimate$\mathcal { F } ( \sigma , \omega )$to conclude that

$$
\Big | \bigcup_ {W \in \mathcal {W} _ {1}} \tilde {Y} _ {1} (W) \Big | \geq \kappa_ {\varepsilon} a ^ {\varepsilon / 2} b ^ {\omega} \tilde {m} ^ {- 1} (\# \mathcal {W} _ {1}) | W | \Big (\tilde {m} ^ {- 3 / 2} \tilde {\ell} (\# \mathcal {W} _ {1}) | W | ^ {1 / 2} \Big) ^ {- \sigma},
$$

(5.30)

![](images/page_47_image_0.jpg)

Figure 8: Each a-tube in$\mathbb { T } _ { a }$(blue tubes) contains at least one δ-tube from$\mathbb { T } _ { 1 } [ W ]$(red tube); this δ-tube has a dense shading (red dots), which in turn gives us a dense shading on the a-tube that contains it (blue balls; for clarify we have only drawn these for one of the tubes in$\mathbb { T } _ { a } )$. Finally, since W (black box) has thickness a, and the a-tubes inside W satisfy a (rescaled) Frostman Convex Wolf axioms, an$L ^ { 2 }$argument says that the union of a-tubes has almost full volume.

where$\tilde { m } = C _ { K T - C W } ( \mathcal { W } _ { 1 } )$and$\tilde { \ell } = C _ { F - S W } ( \mathcal { W } _ { 1 } )$. Note that the estimate$\mathcal { F } ( \sigma , \omega )$involves the additional term$^ { 6 6 } D ^ { \dag }$defined in (5.6). However, we claim that both both Parts (A) and (B) of Proposition 5.1, we have

$$
D \lesssim \delta^ {- \eta}.\tag{5.31}
$$

We verify this claim as follows. In Part (A) of Proposition 5.1, we have the hypothesis that $C _ { K T - C W } ( \mathcal { W } ) \leq \delta ^ { - \eta }$. As discussed in Remark 5.6, Situation 1, this ensures that$D \lesssim \delta ^ { - \eta }$. In Part (B) of Proposition 5.1, we have the hypothesis that

$$
C _ {K T - C W} (\mathcal {W} [ N _ {b} (W) ]) \leq \delta^ {- \eta} \quad \text { for   all } W \in \mathcal {W}.
$$

As discussed in Remark 5.6, Situation 2, this ensures that$D \lesssim \delta ^ { - \eta }$. This establishes (5.31).

In summary, we have established (5.30) when$a \leq \delta ^ { \varepsilon / 1 0 0 }$. If instead$a > \delta ^ { \varepsilon / 1 0 0 }$, then (5.30) follows from the estimate

$$
\Big | \bigcup_ {W \in \mathcal {W} _ {1}} \tilde {Y} _ {1} (W) \Big | \gtrsim \delta^ {\varepsilon / 2 0} \gtrsim \delta^ {\varepsilon / 2 0} \tilde {m} ^ {- 1} (\# \mathcal {W} _ {1}) | W |.\tag{5.32}
$$

Combining (5.28), (5.29), and (5.30) (when$a \leq \delta ^ { \varepsilon / 1 0 0 } )$or (5.32) (when$a \geq \delta ^ { \varepsilon / 1 0 0 } )$, we conclude that

$$
\begin{array}{r l} & {\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim_ {\delta} \delta^ {\omega + \varepsilon + O (\eta) - \varepsilon^ {2} / 2 0 0} \Big (\frac {b}{a} \Big) ^ {\omega} \tilde {m} ^ {- 1} (\# \mathcal {W} _ {1}) | W | \Big (\tilde {m} ^ {- 3 / 2} \tilde {\ell} (\# \mathcal {W} _ {1}) | W | ^ {1 / 2} \Big) ^ {- \sigma} \Big (\Big (\frac {\# \mathbb {T}}{\# \mathcal {W} _ {1}} \Big) ^ {1 / 2} \frac {| T |}{| W |} \Big) ^ {\sigma}} \\ & {\qquad = \delta^ {\omega + \varepsilon - \varepsilon^ {2} / 3 0 0} \Big (\frac {b}{a} \Big) ^ {\omega} \tilde {m} ^ {- 1} (\# \mathcal {W} _ {1}) | W | \Big (\tilde {m} ^ {- 3 / 2} \tilde {\ell} (\# \mathcal {W} _ {1}) ^ {3 / 2} | W | ^ {3 / 2} (\# \mathbb {T}) ^ {- 1 / 2} | T | ^ {- 1} \Big) ^ {- \sigma}.} \end{array}\tag{5.33}
$$

Step 5. It remains to analyze the RHS of (5.33). Our analysis will difer for Parts (A) and (B) of Proposition 5.1. We begin with Part (A). We have$\tilde { m } \lesssim \delta ^ { - \eta }$, and since$\mathcal { W } _ { 1 }$is${ \mathrm { a } } \approx _ { \delta } \ \delta ^ { - O ( \eta ) }$ balanced cover of$\mathbb { T } _ { 1 }$, by Remark 4.3(A) (i.e. Frostman Wolf constants are inherited upwards) we have$\delta ^ { \eta } \tilde { \ell } \lessapprox _ { F - S W } ( \mathbb { T } ) = \ell .$. Since W is a δ<sup>−η</sup>-balanced,$\delta ^ { - \eta }$-almost partitioning cover of$\mathbb { T } .$ $\# \mathbb { T } [ W ] \geq \delta ^ { \eta } C _ { K T - C W } ( \mathbb { T } ) \frac { | W | } { | T | }$for each$W \in { \mathcal { W } }$, and$\mathcal { W } _ { 1 }$is a refinement of W, we have$( \# \mathcal { W } _ { 1 } ) | W | \gtrapprox \delta$ $\delta ^ { \eta } m ^ { - 1 } ( \# \mathbb { T } ) | T |$. The RHS of (5.33) becomes

$$
\delta^ {\omega + \varepsilon} \left(\frac {b}{a}\right) ^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \left(m ^ {- 3 / 2} \ell (\# \mathbb {T}) | T | ^ {1 / 2}\right) ^ {- \sigma},
$$

as claimed.

Next we consider part (B). We have ˜m$\lessapprox \delta \delta ^ { - \eta } | W | ( \# \mathcal { W } ) \lesssim _ { \delta } \delta ^ { - \eta } | W | ( \# \mathcal { W } _ { 1 } )$, and$\widetilde { \ell } \lessapprox _ { \delta } \delta ^ { - \eta }$. Thus the RHS of (5.33) becomes

$$
\delta^ {\omega + \varepsilon} \left(\frac {b}{a}\right) ^ {\omega} \left((\# \mathbb {T}) ^ {1 / 2} | T |\right) ^ {\sigma}.
$$

This concludes the proof of Proposition 5.1.

## 5.4 Proof of Proposition 5.2: Factoring at two scales

The proof of Proposition 5.2 is almost identical to the proof of Proposition 5.1. Rather than present a more complicated unified proof of the two results, for clarity of exposition we have opted to instead briefly sketch the proof of Proposition 5.2 and highlight where the two proofs difer.

We begin by refining the shading$( \mathbb { T } , Y ) _ { \delta }$to find a subset$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$that has at least average density on balls of radius$a ;$this is the analogue of$\left( 5 . 2 6 \right)$. By Lemma 4.11, we have that for each $W \in \dot { \mathcal { W } } , C _ { F - S W } ( \mathbb { T } ^ { W } ) \overset { < } \approx \delta \overset \le \approx \delta C _ { F - S W } ( \mathbb { T } ^ { T _ { \rho } } ) \cdot C _ { F - S W } ( \mathbb { T } _ { \rho } ^ { W } ) \overset { < } \approx \delta \overset { < } { \delta } ^ { - \eta } \ell ^ { \prime }$. Thus the analogue of (5.27) is

$$
\Big | \bigcup_ {T ^ {W} \in \mathbb {T} _ {1} ^ {W}} Y _ {1} ^ {W} (T ^ {W}) \Big | \gtrsim \big (\frac {\delta}{b} \big) ^ {\varepsilon / 2} \big (\frac {\delta}{a} \big) ^ {\omega} m ^ {- 1} (\# \mathbb {T} ^ {W}) | T ^ {W} | \Big (m ^ {- 3 / 2} (\delta^ {- \eta} \ell^ {\prime}) (\# \mathbb {T} ^ {W}) | T ^ {W} | ^ {1 / 2} \Big) ^ {- \sigma},\tag{5.34}
$$

where$m = C _ { K T - C W } ( \mathbb { T } )$, and this gives us the following analogue of (5.28):

$$
\lambda \gtrsim_ {\delta} \big (\frac {\delta}{b} \big) ^ {\varepsilon / 2} \delta^ {O (\eta)} \big (\frac {\delta}{a} \big) ^ {\omega} m ^ {- 1} (\# \mathbb {T} [ W ]) | T | \Big (m ^ {- 3 / 2} \ell^ {\prime} (\# \mathbb {T} ^ {W}) | T ^ {W} | ^ {1 / 2} \Big) ^ {- \sigma}.\tag{5.35}
$$

The next step is to define a dense shading on$\mathcal { W } ;$it is here that we use the fact that W factors $\mathbb { T } _ { \rho }$from below with respect to the Frostman Convex Wolf axioms with error$\leq \delta ^ { - \eta } -$this allows us to use the same argument as in Step 3 from the proof of Proposition 5.1 to show that the shading $\tilde { Y } _ { 1 } ( W )$is$\delta ^ { { \cal O } ( \eta ) }$dense.

Finally, we have the following analogue of (5.30):

$$
\Big | \bigcup_ {W \in \mathcal {W} _ {1}} \tilde {Y} _ {1} (W) \Big | \gtrsim a ^ {\varepsilon / 2} b ^ {\omega} \tilde {m} ^ {- 1} (\# \mathcal {W} _ {1}) | W | \left(\tilde {m} ^ {- 3 / 2} \tilde {\ell} (\# \mathcal {W}) | W | ^ {1 / 2}\right) ^ {- \sigma},\tag{5.36}
$$

where$\tilde { m } = C _ { K T - C W } ( \mathcal { W } _ { 1 } ) \leq \delta ^ { - \eta }$(by hypothesis) and$\tilde { \ell } = C _ { F - S W } ( \mathcal { W } _ { 1 } ) \underset { \approx } { \lessapprox } \delta ^ { - \eta } \ell$(by Remark$4 . 3 ( \mathrm { A } ) \ )$

Combining (5.35) and (5.36) (using the same argument that was used to obtain (5.33)), we conclude that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \delta^ {\varepsilon + \omega} \big (\frac {b}{a} \big) ^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 3 / 2} \ell \ell^ {\prime} (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma}.
$$

## 5.5 Tubes organized into to slabs

We conclude this section by using the tools developed thus far to prove the following. Let$( \mathbb { T } , Y ) _ { \delta }$ be a set of tubes and their associated shading. Suppose that for each$T \in \mathbb { T }$, there is a$\delta \times b \times 1$ slab$S \supset T$that has large intersection with$\textstyle \bigcup _ { \mathbb { T } } Y ( T )$. Then provided$C _ { K T - C W } ( \mathbb { T } )$is small,${ \lvert { \mathrm { J } _ { \mathbb { T } } } { \boldsymbol { Y } } ( { \boldsymbol { T } } ) }$ has larger volume than one would expect from the estimate$\mathcal { E } ( \sigma , \omega )$; the estimate becomes better as$C _ { K T - C W } ( \mathbb { T } )$becomes smaller and b becomes larger. The precise statement is as follows.

Lemma 5.17. Let$\omega > 0 , \sigma \in [ 0 , 2 / 3 ]$and suppose$\mathcal { E } ( \sigma , \omega )$is true. For all$\varepsilon > 0$, there exist $\kappa , \eta > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be a set of tubes and their associated shading. Let$b \geq \delta$and suppose that for each$T \in \mathbb { T }$there exists a$\delta \times b \times 1$prism$S \supset T$with $\begin{array} { r } { \left| S \cap \bigcup _ { T \in \mathbb { T } } Y ( T ) \right| \geq \delta ^ { \eta } | S | } \end{array}$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\varepsilon} b ^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 1} \ell (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma} \Big (\frac {| S |}{| T |} \Big) ^ {\sigma / 2},\tag{5.37}
$$

where$m = C _ { K T - C W } ( \mathbb { T } )$and$\ell = C _ { F \cdot S W } ( \mathbb { T } )$

Remark 5.18. Note that the exponent of m in (5.37) is only$m ^ { \sigma - 1 }$, rather than the usual estimate $m ^ { ( 3 / 2 ) \sigma - 1 }$from$\mathcal { E } ( \sigma , \omega )$. While this is likely not optimal, in practice we will only apply Lemma 5.17 with m of size about 1, so the distinction will not be important.

Proof. After pigeonholing, we can select a${ \approx } _ { \delta }$1 refinement$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$of$( \mathbb { T } , Y ) _ { \delta }$and a set$s$of essentially distinct$\delta \times b \times 1$slabs with the following properties:

• For each$T \in \mathbb { T } _ { 1 }$with corresponding slab$S ( T )$, there is a slab$S \in { \mathcal { S } }$comparable to$S ( T )$ We denote this by$T \sim S$

• There is an integer N so that each slab in$s ,$there are between N and 2N tubes$T \in \mathbb { T } _ { 1 }$with $T \sim S$

Abusing notation, we will replace each slab in S with its 10-fold dilate. Then

(i)$\boldsymbol { s }$covers$\mathbb { T } _ { 1 }$

(ii)$\# \mathbb { T } [ S ] \geq N$for each$S \in { \mathcal { S } }$

(iii)$\# { \mathcal { S } } \sim N ^ { - 1 } ( \# \mathbb { T } _ { 1 } )$

(iv) The shading$\begin{array} { r } { Y ( S ) = S \cap \bigcup _ { T \in \mathbb { T } } Y ( T ) \ \mathrm { i s } \stackrel { > } { \sim } \delta ^ { \eta } } \end{array}$dense.

From Items (ii) and (iii) we conclude that

$$
C _ {F - S W} (\mathcal {S}) \lesssim C _ {F - S W} (\mathbb {T} _ {1}) \lesssim_ {\delta} \delta^ {- \eta} \ell ,
$$

and

$$
C _ {K T - C W} (\mathcal {S}) \lesssim C _ {K T - C W} (\mathbb {T} _ {1}) \frac {\# \mathcal {S}}{\# \mathbb {T} _ {1}} \frac {| S |}{| T |} \lesssim_ {\delta} \delta^ {- \eta} m \frac {\# \mathcal {S}}{\# \mathbb {T}} \frac {| S |}{| T |}.\tag{5.38}
$$

We would like to use Proposition 5.14 and apply the estimate$\mathcal { F } ( \sigma , \omega )$to obtain a lower bound for the volume of$\cup Y ( S )$. Before doing${ \mathrm { s o } } ,$we should estimate the quantity D from (5.6). By Remark 5.6, Situation 2, and (5.38), we have

$$
D \lesssim \Bigl (\sup _ {S \in \mathcal {S}} C _ {K T - C W} (\mathcal {S} [ N _ {b} (S) ]) \Bigr) ^ {1 / 2} \lesssim_ {\delta} \left(\delta^ {- \eta} m \frac {\# \mathcal {S}}{\# \mathbb {T}} \frac {| S |}{| T |}\right) ^ {1 / 2}.
$$

If$\eta , \kappa > 0$are chosen suficiently small depending on$\omega , \sigma _ { \mathrm { { : } } }$and ε, then we can apply the estimate $\mathcal { F } ( \sigma , \omega )$to conclude that

$$
\begin{array}{r l} & {\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \Big | \bigcup_ {S \in \mathcal {S}} Y (S) \Big |} \\ & {\qquad \geq \kappa \delta^ {\varepsilon / 2} b ^ {\omega} C _ {K T - C W} (\mathcal {S}) ^ {- 1} (\# \mathcal {S}) | S | \Big (C _ {K T - C W} (\mathcal {S}) ^ {- 3 / 2} C _ {F - S W} (\mathcal {S}) (\# \mathcal {S}) | S | ^ {1 / 2} \Big) ^ {- \sigma} D ^ {- \sigma}} \\ & {\qquad \gtrsim_ {\delta} \kappa \delta^ {\varepsilon / 2 + 2 \eta} b ^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 1} \ell (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma} \Big (m ^ {1 / 2} \frac {| S |}{| T |} \frac {(\# \mathcal {S}) ^ {1 / 2}}{(\# \mathbb {T}) ^ {1 / 2}} D ^ {- 1} \Big) ^ {\sigma}} \\ & {\qquad \gtrsim_ {\delta} \kappa \delta^ {\varepsilon / 2 + 2 \eta} b ^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 1} \ell (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma} \Big (\frac {| S |}{| T |} \Big) ^ {\sigma / 2}.} \end{array}
$$

Often, we will use the following weaker version of Lemma 5.17.

Corollary 5.19. Let$\omega > 0 , \sigma \in ( 0 , 2 / 3 ]$and suppose$\mathcal { E } ( \sigma , \omega )$is true. For all$\varepsilon > 0$, there exist $\eta , c > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be a set of tubes and their associated shading. Let$\rho \ge \delta$and suppose that for each$T \in \mathbb { T }$there exists a ρ tube$T _ { \rho } \supset T$with <sup></sup>T ∩ $\begin{array} { r } { \bigcup _ { T \in \mathbb { T } } Y ( T ) \big | \geq \delta ^ { \eta } | T _ { \rho } | } \end{array}$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\varepsilon} \rho^ {\omega} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 1} \ell (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma} \Big (\frac {\rho}{\delta} \Big) ^ {\sigma / 2},\tag{5.39}
$$

where$m = C _ { K T - C W } ( \mathbb { T } )$and$\ell = C _ { F \cdot S W } ( \mathbb { T } )$

## 6 Assertions D and$\mathcal { E }$are equivalent

Our goal in this section is to prove Proposition 1.6. To do so, we will need a result from [26], which (informally) says that if a set of δ-tubes satisfies the Frostman Convex Wolf Axioms at many diferent scales, then the union of these tubes must have large volume. To state the result precisely, we recall Definition 2.12 from [26].

Definition 6.1. Let$K \ge 1 , \delta > 0$. We say a set T of δ-tubes in$\mathbb { R } ^ { 3 }$satisfies the Frostman Convex Wolf Axioms at every scale with error K if the tubes in T are essentially distinct, and for every $\rho _ { 0 } \in [ \delta , 1 ]$, there exists$\rho \in [ \rho _ { 0 } , K \rho _ { 0 } )$and a set of ρ-tubes$\mathbb { T } _ { \rho }$that satisfies the following properties.

(i)$\mathbb { T } _ { \rho }$is a K-balanced partitioning cover of T.

(ii) For each$T _ { \rho } \in \mathbb { T } _ { \rho } , \mathbb { T } ^ { T _ { \rho } }$satisfies the Frostman Convex Wolf Axioms with error$K$

Next we recall Theorem 5.2 from [26].

Theorem 6.2. For all$\varepsilon > 0$, there exists η,$\kappa > 0$so that the following holds for all$\delta > 0$. Let$\mathbb { T }$ be a set of δ-tubes that satisfy the Frostman Convex Wolf Axioms at every scale with error$\delta ^ { - \eta }$ and let$Y ( T )$be$a ~ \delta ^ { \eta }$dense shading. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\varepsilon}.\tag{6.1}
$$

When$\varepsilon < \omega ,$the conclusion of Theorem 6.2 gives a volume estimate that is superior to the volume estimate (1.3) from Assertion$\mathcal { E } ( \sigma , \omega )$. However, the hypotheses of Assertion$\mathcal { E } ( \sigma , \omega )$are weaker. The next result says that for every collection T of tubes that satisfies the Frostman Convex Wolf axioms, at least one of the following must occur:

(A) T satisfies the hypothesis of Theorem 6.2. This is good, provided we select$\varepsilon < \omega$

(B) At a suitable scale, T satisfies the Katz-Tao Convex Wolf axioms with error roughly 1. This is good, if we know that$\mathcal { D } ( \sigma , \omega _ { 1 } )$is true for some$\omega _ { 1 } < \omega$

(C) At a suitable scale, T is factored by flat rectangular prisms, and thus satisfies the hypotheses of Proposition 5.1. This is good, since it gives a stronger volume estimate than$\mathcal { E } ( \sigma , \omega )$

The precise statement is as follows.

Proposition 6.3. Let$\zeta _ { 1 } \geq \zeta _ { 2 } \geq \zeta _ { 3 } > 0$. Then there exists$\eta > 0$such that the following holds for all$\delta > 0$. Let T be a set of δ-tubes satisfying the Frostman Convex Wolf Axioms with$e r r o r \le \delta ^ { - \eta }$ Then after replacing T by$a \approx _ { \delta }$1 refinement, at least one of the following is true.

(A) T satisfies the Frostman Convex Wolf Axioms at every scale with error$\delta ^ { - \zeta _ { 1 } }$, in the sense of Definition 6.1.

(B) There exists$\delta \le \tau < \rho \le 1$, with$\tau \leq \delta ^ { \zeta _ { 1 } / 5 } \rho ;$a balanced partitioning cover$\mathbb { T } _ { \tau } ~ o f \ \mathbb { T } ;$and a balanced partitioning cover$\mathbb { T } _ { \rho } \ o f \ \mathbb { T } _ { \tau }$such that the following is true:

(i)$C _ { F - C W } ( \mathbb { T } ^ { T _ { \tau } } ) \lesssim \delta ^ { - \zeta _ { 2 } }$for each$T _ { \tau } \in \mathbb { T } _ { \tau }$

(ii)$C _ { K T - C W } ( \mathbb { T } _ { \tau } ^ { T _ { \rho } } ) \lesssim \delta ^ { - \zeta _ { 2 } }$and$\# \mathbb { T } _ { \tau } ^ { T _ { \rho } } \geq \delta ^ { \zeta _ { 2 } } ( \rho / \tau ) ^ { 2 }$for each$T _ { \rho } \in \mathbb { T } _ { \rho }$

(iii)$C _ { F - C W } ( \mathbb { T } _ { \rho } ) \lesssim _ { \delta } \delta ^ { - \eta } .$

(C) There exists$\delta \leq a < b \leq 1$with$a ~ \le ~ \delta ^ { \zeta _ { 2 } / 1 0 0 } b$, and a set W of$a \times b \times 1$prisms that satisfies the hypotheses of Proposition$5 . 1 ( B ) \colon \mathcal { W }$factors T above and below with respect to the Frostman Convex Wolf Axioms, with error$O ( \delta ^ { - \zeta _ { 3 } } )$. And for each$W \in \mathcal { W }$, we have $C _ { K T - C W } ( \mathcal { W } [ N _ { b } ( W ) ] ) \lesssim \delta ^ { - \zeta _ { 3 } }$

We will defer the proof of Proposition 6.3 to Section 6.3.

Using Proposition 6.3, we will prove the following weaker form of Proposition 1.6; recall that$\tilde { \mathcal { E } }$ is defined in Definition 5.3.

Lemma 6.4. Let$0 < \sigma \le 2 / 3$. For all$\omega , t > 0$, there exists$\alpha > 0$so that the following holds for all$\omega ^ { \prime } \geq \omega + t$. Suppose$\mathcal { D } ( \sigma , \omega )$and$\mathcal { E } ( \sigma , \omega ^ { \prime } )$are true. Then$\tilde { \mathcal { E } } ( \sigma , \omega ^ { \prime } - \alpha )$is true.

Proof. Let$\alpha = \alpha ( \sigma , \omega , t ) > 0$be a small number to be specified below. Let$\eta , \kappa > 0$be small numbers that depend on$\omega , \omega ^ { \prime }$, and σ. Our goal is to prove that if$( \mathbb { T } , Y ) _ { \delta }$is$\delta ^ { \eta }$dense with $C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$, then

$$
\Big | \bigcup_ {T \in \mathbb {T}} \Big | \geq \kappa \delta^ {\omega^ {\prime} - \alpha} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 3 / 2} (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma},\tag{6.2}
$$

with$m = C _ { K T - C W } ( \mathbb { T } )$. Note that the estimate (6.2) is slightly stronger than the desired estimate $\tilde { \mathcal { E } } ( \sigma , \omega ^ { \prime } - \alpha )$, since there is no additional$\delta ^ { \varepsilon }$loss; this stronger estimate is possible since$\omega ^ { \prime } - \omega > 0$ which gives us a bit of “wiggle room.”

Step 1. Without loss of generality we may suppose that$| Y ( T ) | \geq \delta ^ { \eta } | T |$for each$T \in \mathbb { T }$. Let $\zeta _ { i } = \zeta _ { i } ( \sigma , \omega , t ) , i = 1 , \ldots , 5$be small quantities to be chosen below; we will have$\zeta _ { i + 1 }$very small compared to$\zeta _ { i } ,$and η very small compared to$\zeta _ { 5 }$

We first consider the case where there exists a subset$\mathbb { T } ^ { \prime } \subset \mathbb { T }$with$\# \mathbb { T } ^ { \prime } \geq \delta ^ { \eta } ( \# \mathbb { T } )$, and $C _ { F - C W } ( \mathbb { T } ^ { \prime } ) ~ \leq ~ \delta ^ { - \zeta _ { 4 } }$(this assumption will remain until Step 4, where we will consider the case where no such subset exists). Abusing notation slightly, we will continue to use$\mathbb { T }$to refer to this subset. In particular, we have that

$$
\# \mathbb {T} \gtrsim_ {\delta} \delta^ {\eta + \zeta_ {4}} m | T | ^ {- 1}, \quad \mathrm{and} \quad C _ {F - C W} (\mathbb {T}) \leq \delta^ {- \zeta_ {4}}.\tag{6.3}
$$

If$\zeta _ { 4 }$and η are chosen suficiently small compared to$\zeta _ { 1 } , \zeta _ { 2 } , \zeta _ { 3 }$, then we can apply Proposition 6.3 to$( \mathbb { T } , Y ) _ { \delta }$, with$\zeta _ { 1 } , \zeta _ { 2 } , \zeta _ { 3 }$as specified above. We will select$\zeta _ { 1 } = \zeta _ { 1 } ( \omega )$and$\eta$suficiently small so that if Conclusion (A) of Proposition 6.3 holds, then we can use Theorem 6.2 to conclude that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \delta^ {\omega},
$$

and hence (6.2) holds provided we choose$\alpha ( \omega , t ) \leq t$. Henceforth we shall assume that Conclusion (A) of Proposition 6.3 does not hold.

Step 2. Suppose that Conclusion (B) of Proposition 6.3 holds. We will define shadings$Y _ { \tau }$and $Y _ { \rho }$on the sets of tubes$\mathbb { T } _ { \tau }$and$\mathbb { T } _ { \rho }$as follows. For each$T _ { \tau } \in \mathbb { T } _ { \tau }$, we refine the shading on$\mathbb { T } [ T _ { \tau } ]$to have average density on balls of radius τ (see (5.26) and the surrounding discussion). We define the shading$Y _ { \tau } ( T _ { \tau } )$to be the union of those τ-balls that intersect$\begin{array} { r } { \bigcup _ { \mathbb { T } [ T _ { \tau } ] } Y ( T ) } \end{array}$. We perform the analogous procedure to define$Y _ { \rho }$(this induces a refinement on the shadings$Y _ { \tau }$and$Y )$

After these steps have been performed,$( \mathbb { T } _ { \rho } , Y _ { \rho } ) _ { \rho }$is$\delta ^ { { \cal O } ( \eta ) }$dense; each pair$( \mathbb { T } _ { \tau } ^ { T _ { \rho } } , Y _ { \tau } ^ { T _ { \rho } } ) _ { \tau / \rho }$is$\delta ^ { { \cal O } ( \eta ) }$ dense; and each pair$( \mathbb { T } ^ { T _ { \tau } } , Y ^ { T _ { \tau } } ) _ { \delta / \tau }$is$\delta ^ { { \cal O } ( \eta ) }$dense. Furthermore, we have

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \Bigg (\Big | \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} Y _ {\rho} (T _ {\rho}) \Big | \Bigg) \Bigg (\inf _ {T _ {\rho} \in \mathbb {T} _ {\rho}} \Big | \bigcup_ {T _ {\tau} ^ {T _ {\rho}} \in \mathbb {T} _ {\tau} ^ {T _ {\rho}}} Y _ {\tau} ^ {T _ {\rho}} (T _ {\tau} ^ {T _ {\rho}}) \Big | \Bigg) \Bigg (\inf _ {T _ {\tau} \in \mathbb {T} _ {\tau}} \Big | \bigcup_ {T ^ {T _ {\tau}} \in \mathbb {T} ^ {T _ {\tau}}} Y ^ {T _ {\tau}} (T ^ {T _ {\tau}}) \Big | \Bigg).\tag{6.4}
$$

Our next task is to estimate the three terms on the RHS of (6.4) as follows.

$$
\Big | \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} Y _ {\rho} (T _ {\rho}) \Big | \geq \delta^ {\varepsilon_ {1}} \rho^ {\omega^ {\prime}} \big ((\# \mathbb {T} _ {\rho}) ^ {1 / 2} | T _ {\rho} | \big) ^ {\sigma},\tag{6.5}
$$

$$
\inf _ {T _ {\rho} \in \mathbb {T} _ {\rho}} \Big | \bigcup_ {T _ {\tau} ^ {T _ {\rho}} \in \mathbb {T} ^ {T _ {\rho}}} Y _ {\tau} ^ {T _ {\rho}} (T _ {\tau} ^ {T _ {\rho}}) \Big | \geq \delta^ {\varepsilon_ {1}} \Big (\frac {\tau}{\rho} \Big) ^ {\omega} \Big (\Big (\frac {\# \mathbb {T} _ {\tau}}{\# \mathbb {T} _ {\rho}} \Big) ^ {1 / 2} \frac {| T _ {\tau} |}{| T _ {\rho} |} \Big) ^ {\sigma},\tag{6.6}
$$

$$
\inf _ {T _ {\tau} \in \mathbb {T} _ {\tau}} \Big | \bigcup_ {T ^ {T _ {\tau}} \in \mathbb {T} ^ {T _ {\tau}}} Y ^ {T _ {\tau}} (T ^ {T _ {\tau}}) \Big | \geq \delta^ {\varepsilon_ {1}} \Big (\frac {\delta}{\tau} \Big) ^ {\omega^ {\prime}} \Big (\Big (\frac {\# \mathbb {T}}{\# \mathbb {T} _ {\tau}} \Big) ^ {1 / 2} \frac {| T |}{| T _ {\tau} |} \Big) ^ {\sigma},\tag{6.7}
$$

where$\begin{array} { r } { \varepsilon _ { 1 } = \frac { \zeta _ { 1 } } { 2 4 } ( \omega - \omega ^ { \prime } ) } \end{array}$

First, observe that if we choose η suficiently small, then (6.5) (resp. (6.6) or (6.7)) immediately holds if$\rho > \delta ^ { \varepsilon _ { 1 } / 2 }$(resp.$\delta / \tau > \delta ^ { \varepsilon _ { 1 } } / 2 )$. This is because the volume of the union (6.5) is bounded by the volume of a single tube. In particular, we have the following

• Either (6.5) automatically holds, or$( \mathbb { T } _ { \rho } , Y _ { \rho } ) _ { \rho }$is$\rho ^ { O ( \eta / \varepsilon _ { 1 } ) }$dense and satisfies$C _ { F - C W } ( \mathbb { T } _ { \rho } ) \lesssim$ $\rho ^ { - 2 \zeta _ { 2 } / \varepsilon _ { 1 } }$

• Since$\varepsilon _ { 1 } \leq \zeta _ { 1 } / 2 4$and$\tau \leq \delta ^ { \zeta _ { 1 } / 5 } \rho .$, each pair$( \mathbb { T } _ { \tau } ^ { T _ { \rho } } , Y _ { \rho } ^ { T _ { \rho } } ) _ { \tau / \rho }$is$( \tau / \rho ) ^ { O ( \eta / \varepsilon _ { 1 } ) }$dense and satisfies $C _ { K T - C W } ( \mathbb { T } _ { \tau } ^ { T _ { \rho } } ) \lesssim ( \tau / \rho )$<sup>−2ζ2/ε1</sup> and$\# \mathbb { T } _ { \tau } ^ { T _ { \rho } } \geq ( \tau / \rho ) ^ { 2 \zeta _ { 2 } / \varepsilon _ { 1 } } ( \rho / \tau ) ^ { 2 }$

• Either (6.7) automatically holds, or each pair$( \mathbb { T } ^ { T _ { \tau } } , Y ^ { T _ { \tau } } ) _ { \delta / \tau } \mathrm { i s } ( \delta / \tau ) ^ { O ( \eta / \varepsilon _ { 1 } ) }$dense and satisfies $C _ { K T - C W } ( \mathbb { T } ^ { T _ { \tau } } ) \lesssim ( \delta / \tau ) ^ { - 2 \zeta _ { 2 } / \varepsilon _ { 1 } }$

If we select$\eta$and$\zeta _ { 2 }$suficiently small, depending on ω and t (recall that$t \le \omega - \omega ^ { \prime } )$(η and $\zeta _ { 2 }$also depend on$\varepsilon _ { 1 } .$, but$\varepsilon _ { 1 }$only depends on$\zeta _ { 1 } = \zeta _ { 1 } ( \omega )$, ω and$t )$, then in light of the three bullet points above, the estimates (6.5), (6.6), and (6.7) follow from$\mathcal { E } ( \sigma , \omega ^ { \prime } ) , \mathcal { D } ( \sigma , \omega )$, and$\mathcal { E } ( \sigma , \omega ^ { \prime } )$, respectively.

Combining (6.4), (6.5), (6.6), and (6.7), we conclude that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \delta^ {3 \varepsilon_ {1}} \Big (\frac {\rho}{\tau} \Big) ^ {\omega - \omega^ {\prime}} \delta^ {\omega^ {\prime}} \Big ((\# \mathbb {T}) ^ {1 / 2} | T | \Big) ^ {\sigma} \geq \delta^ {\frac {\zeta_ {1} (\omega - \omega^ {\prime})}{8}} \delta^ {\omega^ {\prime}} \Big ((\# \mathbb {T}) ^ {1 / 2} | T | \Big) ^ {\sigma}.\tag{6.8}
$$

Combining (6.3) and (6.8), we verify that (6.2) holds, provided$\begin{array} { r } { \alpha ( \omega , t ) \leq \frac { \zeta _ { 1 } t } { 1 6 } ; \zeta _ { 4 } < \frac { \zeta _ { 1 } t } { 1 7 } \qquad } \end{array}$; and$\eta > 0$is chosen suficiently small. Henceforth we shall assume that Conclusion (B) of Proposition 6.3 does not hold.

Step 3. Suppose that Conclusion (C) of Proposition 6.3 holds, i.e. there is a set W of$a \times b \times 1$ prisms, with$a \leq \delta ^ { \zeta _ { 2 } / 1 0 0 } b ,$so that W satisfies the hypotheses of Proposition 5.1(B): W factors T above and below with respect to the Frostman Convex Wolf Axioms with error$O ( \delta ^ { - \zeta _ { 3 } } )$. And for each$W \in { \mathcal { W } }$we have$C _ { K T - C W } ( \mathcal { W } [ N _ { b } ( W ) ] ) \lesssim \delta ^ { - \zeta _ { 3 } }$

Let$\varepsilon _ { 2 } = \zeta _ { 2 } \omega / 2 0 0$. If$\zeta _ { 3 }$is selected suficiently small depending on$\zeta _ { 2 }$and$\varepsilon _ { 2 }$(both of these numbers in turn ultimately only depend on ω and t) and if$\eta > 0$is selected suficiently small, then by Proposition 5.1(B) (with$\varepsilon _ { 2 }$in place of$\varepsilon )$we have

$$
\begin{array}{r l} \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | & \gtrsim \delta^ {\omega^ {\prime} + \varepsilon_ {2}} \Big (\frac {b}{a} \Big) ^ {\omega^ {\prime}} \big ((\# \mathbb {T}) ^ {1 / 2} | T | \big) ^ {\sigma} \\ & \geq \delta^ {\omega^ {\prime} + \varepsilon_ {2}} \delta^ {- \frac {\zeta_ {2} \omega}{1 0 0}} \big ((\# \mathbb {T}) ^ {1 / 2} | T | \big) ^ {\sigma} \\ & \geq \delta^ {\omega^ {\prime} - \frac {\zeta_ {2} \omega}{2 0 0}} \big ((\# \mathbb {T}) ^ {1 / 2} | T | \big) ^ {\sigma}. \end{array}\tag{6.9}
$$

Combining (6.3) and (6.9), we verify that (6.2) holds, provided$\begin{array} { r } { \alpha ( \omega , t ) \leq \frac { \zeta _ { 2 } \omega } { 4 0 0 } ; \zeta _ { 4 } < \frac { \zeta _ { 2 } \omega } { 5 0 0 } } \end{array}$; and$\eta > 0$ is chosen suficiently small.

Step 4. It remains to consider the case where every subset$\mathbb { T } ^ { \prime } \subset \mathbb { T }$with$\# \mathbb { T } ^ { \prime } \geq \delta ^ { \eta } ( \# \mathbb { T } )$satisfies $C _ { F - C W } ( \mathbb { T } ^ { \prime } ) > \delta ^ { - \zeta _ { 4 } }$. Apply Proposition 4.6 (factoring a collection of convex sets) to$\mathbb { T } _ { : }$, and denote the output by$\mathbb { T } ^ { \prime }$and W. Then Item ii) of Proposition 4.6 implies$\# \mathbb { T } [ W ] \approx _ { \delta } C _ { K T - C W } ( \mathbb { T } ^ { \prime } ) \frac { | W | } { | T | }$. Since $\# \mathbb { T } ^ { \prime } \geq \delta ^ { \eta } ( \# \mathbb { T } )$, we have$C _ { F - C W } ( \mathbb { T } ^ { \prime } ) > \delta ^ { - \zeta _ { 4 } }$. We also have$C _ { F - C W } ( \mathbb { T } ^ { \prime W } ) \lesssim _ { \delta } 1$for each$W \in { \mathcal { W } }$, from which it follows that$| W | \lessapprox _ { \delta } \delta ^ { \zeta _ { 4 } }$(recall that the sets$W \in { \mathcal { W } }$are congruent, and thus they all have identical volume).

If the prisms in W are flat, in the sense that they are comparable to$a \times b \times 1$prisms with $a \leq \delta ^ { \zeta _ { 5 } } b$, then we can apply Proposition$5 . 1 ( \mathrm { A } )$with$\varepsilon _ { 3 } = \zeta _ { 5 } \omega ^ { \prime } / 2$to conclude that

$$
\begin{array}{r l} & {\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \delta^ {\omega^ {\prime} + \varepsilon_ {3}} \Big (\frac {b}{a} \Big) ^ {\omega^ {\prime}} (m ^ {\prime}) ^ {- 1} (\# \mathbb {T} ^ {\prime}) | T | \big ((m ^ {\prime}) ^ {- 3 / 2} (\ell^ {\prime}) (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}} \\ & {\qquad \gtrsim \delta^ {\omega^ {\prime} - \frac {\zeta_ {5} \omega^ {\prime}}{2} + 2 \eta} m ^ {- 1} (\# \mathbb {T}) | T | \big (m ^ {- 3 / 2} (\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.} \end{array}\tag{6.10}
$$

In the second inequality, we used the fact that$\# \mathbb { T } ^ { \prime } \geq \delta ^ { \eta } \# \mathbb { T } ; \ell ^ { \prime } : = C _ { F - S W } ( \mathbb { T } ^ { \prime } ) \ \gtrapprox \delta ^ { - \eta } ; \ m ^ { \prime } : =$ $C _ { K T - C W } ( \mathbb { T } ^ { \prime } ) \le m ;$and$\sigma \le 2 / 3$. We conclude that (6.2) holds, provided$\begin{array} { r } { \alpha ( \omega , t ) \leq \frac { \zeta _ { 5 } \omega } { 4 } \leq \frac { \zeta _ { 5 } \omega ^ { \prime } } { 4 } } \end{array}$and $\eta > 0$is chosen suficiently small.

Finally, we consider the case where the prisms in W are not flat, in the sense that$a \ge \delta ^ { \zeta _ { 5 } } b$ In this case we can replace each prism$W \in \mathcal { W }$by its b-neighbourhood, and then refine the corresponding set of b-tubes$\mathbb { T } _ { b }$by a factor of$( b / a ) ^ { 3 } \leq \delta ^ { - 3 \zeta _ { 5 } }$(this is the number of essentially distinct $a \times b \times 1$prisms that can fit inside a b tube) so that the tubes in$\mathbb { T } _ { b }$are essentially distinct. Since $| W | \lessapprox _ { \delta } \delta ^ { \zeta _ { 4 } }$and$a \geq \delta ^ { \zeta _ { 5 } } b$, we have

$$
b \lesssim_ {\delta} \delta^ {\zeta_ {4} / 2 - \zeta_ {5}} \leq \delta^ {\zeta_ {4} / 3}.\tag{6.11}
$$

To recap, the set$\mathbb { T } _ { b }$has the following properties.

$$
\bullet C _ {K T - C W} (\mathbb {T} _ {b}) \lesssim \frac {b}{a} C _ {K T - C W} (\mathcal {W}) \lesssim_ {\delta} \delta^ {- \zeta_ {5}} \leq b ^ {- 3 \zeta_ {5} / \zeta_ {4}}.
$$

$$
\bullet C _ {F - S W} (\mathbb {T} _ {b}) \lesssim \delta^ {- 3 \zeta_ {5}} C _ {F - S W} (\mathcal {W}) \lesssim_ {\delta} \delta^ {- 3 \zeta_ {5}} C _ {F - S W} (\mathbb {T}) \lesssim_ {\delta} \delta^ {- 3 \zeta_ {5} - \eta}.
$$

• For each$T _ { b } \in \mathbb { T } _ { b }$, we have$C _ { F - C W } ( \mathbb { T } ^ { T _ { b } } ) \lesssim \frac { b } { a } C _ { F - C W } ( \mathbb { T } ^ { W } ) \lesssim \delta \delta ^ { - \zeta _ { 5 } }$, where$\mathcal { W } \ni W \subset T _ { b }$is the prism containing all of the tubes in$\mathbb { T } [ T _ { b } ]$

• For each$T _ { b } \in \mathbb { T } _ { b }$, we have$\# \mathbb { T } ^ { T _ { b } } \lesssim \delta C _ { K T - C W } ( \mathcal { W } ) \frac { b } { a } \# \mathbb { T } ^ { W } \lesssim _ { \delta } \frac { b } { a } m \frac { | W | } { | T | } \lesssim _ { \delta } \delta ^ { - 2 \zeta _ { 5 } } m \frac { | T _ { b } | } { | T | }$

(For the second item above, we make crucial use of the fact that$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$, which is why the conclusion of Lemma 6.4 only says that$\tilde { \mathcal { E } } ( \sigma , \omega ^ { \prime } - \alpha )$is true, rather than the superficially stronger statement$\mathcal { E } ( \sigma , \omega ^ { \prime } - \alpha ) )$.

Mirroring the argument in Step 2, refine the shadings$Y ( T )$on each set of tubes$\mathbb { T } [ T _ { b } ]$to have average density on balls of radius b. We define the shading$Y _ { b } ( T _ { b } )$to be the union of those b-balls that intersect$\cup _ { \mathbb { T } [ T _ { b } ] } Y ( T )$. Then$( \mathbb { T } _ { b } , Y _ { b } ) _ { b }$is$\delta ^ { \eta } \ge b ^ { 3 \eta / \zeta _ { 4 } }$dense. We thus have the following analogue of (6.4):

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \Bigg (\Big | \bigcup_ {T _ {b} \in \mathbb {T} _ {b}} Y _ {\rho} (T _ {b}) \Big | \Bigg) \Bigg (\inf _ {T _ {b} \in \mathbb {T} _ {b}} \Big | \bigcup_ {T ^ {T _ {b}} \in \mathbb {T} ^ {T _ {b}}} Y ^ {T _ {b}} (T ^ {T _ {b}}) \Big | \Bigg).\tag{6.12}
$$

Let$\begin{array} { r } { \varepsilon _ { 4 } = \frac { \zeta _ { 4 } ( \omega - \omega ^ { \prime } ) } { 1 2 } } \end{array}$. If$\zeta _ { 5 }$and η are selected suficiently small depending on$\zeta _ { 4 }$and$\varepsilon _ { 4 }$(which in turn depend on ω and t), then we can use the estimate (1.2) from Assertion$\mathcal { D } ( \sigma , \omega )$to conclude that

$$
\Big | \bigcup_ {T _ {b} \in \mathbb {T} _ {b}} Y _ {\rho} (T _ {b}) \Big | \gtrsim b ^ {\omega + \varepsilon_ {4}} (\# \mathbb {T} _ {b}) | T _ {b} | \big ((\# \mathbb {T} _ {b}) | T _ {b} | ^ {1 / 2} \big) ^ {- \sigma}.\tag{6.13}
$$

Finally, we would like to obtain the estimate

$$
\Big | \bigcup_ {T ^ {T _ {b}} \in \mathbb {T} ^ {T _ {b}}} Y ^ {T _ {b}} (T ^ {T _ {b}}) \Big | \gtrsim \delta^ {\varepsilon_ {4}} \big (\frac {\delta}{b} \big) ^ {\omega^ {\prime}} \Big ((\# \mathbb {T} ^ {T _ {b}}) ^ {1 / 2} \frac {| T |}{| T _ {b} |} \Big) ^ {\sigma}.\tag{6.14}
$$

When$\delta / b > \delta ^ { \varepsilon _ { 4 } / 2 }$, we have that (6.14) follows from the elementary fact that the shading on each $Y ( T ) { \mathrm { ~ i s } } \gtrapprox \delta ^ { \eta }$dense, and the union on the LHS of (6.14) is bounded by the volume of a single tube. On the other hand, when$\delta / b \le \delta ^ { \varepsilon _ { 4 } / 2 }$, we have that (6.14) follows from the estimate (1.3) from Assertion$\mathcal { E } ( \sigma , \omega ^ { \prime } )$, provided$\zeta _ { 5 }$is chosen suficiently small depending on$\zeta _ { 4 }$and$\varepsilon _ { 4 } .$since $C _ { F - C W } ( \mathbb { T } ^ { T _ { b } } ) \lessapprox \delta ^ { - \zeta _ { 5 } }$

Since$\# \mathbb { T } ^ { T _ { b } } \lessapprox m \delta ^ { - 2 \zeta _ { 5 } } \frac { | T | } { | T _ { b } | }$for each$T _ { b } \in \mathbb { T } _ { b }$(where$m = C _ { K T - C W } ( \mathbb { T } ) )$), (6.14) becomes

$$
\Big | \bigcup_ {T ^ {T _ {b}} \in \mathbb {T} ^ {T _ {b}}} Y ^ {T _ {b}} (T ^ {T _ {b}}) \Big | \gtrsim \delta^ {\varepsilon_ {4} + 2 \zeta_ {5}} \big (\frac {\delta}{b} \big) ^ {\omega^ {\prime}} m ^ {- 1} (\# \mathbb {T} ^ {T _ {b}}) \frac {| T |}{| T _ {b} |} \Big (m ^ {- 3 / 2} (\# \mathbb {T} ^ {T _ {b}}) \Big (\frac {| T |}{| T _ {b} |} \Big) ^ {1 / 2} \Big) ^ {- \sigma}.\tag{6.15}
$$

Combining (6.12), (6.13), (6.15), and (6.11), we conclude that if we select$\zeta _ { 5 } \le \zeta _ { 4 } ( \omega - \omega ^ { \prime } ) / 1 2$, then

$$
\begin{array}{l} \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \delta^ {\omega^ {\prime} + \varepsilon_ {4} + 2 \zeta_ {5}} b ^ {\omega - \omega^ {\prime} + \varepsilon_ {4}} m ^ {- 1} (\# \mathbb {T}) | T | \Big (m ^ {- 3 / 2} (\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{6.16}
$$

We conclude that (6.2) holds, provided$\begin{array} { r } { \alpha ( \omega , t ) \leq \frac { \zeta _ { 4 } t } { 1 2 } } \end{array}$, and$\eta > 0$is chosen suficiently small.□

We now use Lemma 6.4 to prove Proposition 1.6.

Proof of Proposition 1.6. Let$0 \leq \sigma \leq 2 / 3 , \ \omega \geq 0$, and suppose that Assertion$\mathcal { D } ( \sigma , \omega )$is true. Fix $t > 0$and let$\alpha = \alpha ( \sigma , \omega , t ) > 0$be the output of Lemma 6.4. Since a δ-tube has volume$\sim \delta ^ { 2 }$ we always have that$\mathcal { E } ( \sigma , 2 )$is true. Now suppose that$\mathcal { E } ( \sigma , \omega ^ { \prime } )$is true for some$\omega ^ { \prime } \in [ \omega + t , 2 ]$ Applying Lemma 6.4 followed by Proposition 5.14, we have

$$
\mathcal {E} (\sigma , \omega^ {\prime}) \implies \tilde {\mathcal {E}} (\sigma , \omega^ {\prime} - \alpha) \implies \mathcal {E} (\sigma , \omega^ {\prime} - \alpha).
$$

Iterating the above argument, we conclude that$\mathcal { E } ( \sigma , \omega ^ { \prime \prime } )$is true for some$\omega ^ { \prime \prime } \leq \omega + t$, so in particular $\mathcal { E } ( \sigma , \omega + t )$is true.

However,$t > 0$was arbitrary, and by the definition of E, it is clear that the set

$$
\{\omega^ {\prime} \in [ \omega , 2 ]: \mathcal {E} (\sigma , \omega^ {\prime}) \text {   is   true } \}
$$

is a closed interval. We conclude that$\mathcal { E } ( \sigma , \omega )$is true.

This concludes the proof of Proposition 1.6, except that we must still prove Proposition 6.3. We do this below.

## 6.1 Proof of Proposition 6.3: A factoring trichotomy

Step 1. We begin by regularizing the set T. Let$\eta > 0$be a small quantity to be determined below, with$N = 1 / \eta$an integer. Define$\delta _ { i } = \delta ^ { i / N } , ~ i = 1 , \dots , N$. By iterated pigeonholing and replacing T by$\mathrm { ~ a ~ } | \log \delta | ^ { - N }$-refinement, we may suppose that for each$i = 1 , \ldots , N$there exists a set $\mathbb { T } _ { \delta _ { i } }$of$\delta _ { i } \mathrm { - t u b e s }$that is a balanced partitioning cover of$\mathbb { T } _ { \delta _ { i + 1 } }$. We will call numbers of the form$\delta _ { i }$ “admissible scales.” In particular, for each admissible scale$\delta _ { i }$, we have

$$
\# \mathbb {T} [ T _ {\delta_ {i}} ] \approx_ {\delta} \frac {\# \mathbb {T}}{\# \mathbb {T} _ {\delta_ {i}}} \quad \mathrm{forevery} T _ {\delta_ {i}} \in \mathbb {T} _ {\delta_ {i}}.\tag{6.17}
$$

Next we apply Proposition 4.6 to each set$\mathbb { T } ^ { T _ { \delta _ { i } } } ;$the output of Proposition 4.6 is$\mathrm { a } \approx 1$refinement of$\mathbb { T } ^ { T _ { \delta _ { i } } }$(this induces$\mathrm { ~ a ~ } \approx 1$refinement of$\mathbb { T }$and all sets$\mathbb { T } _ { \delta _ { j } }$for$j > i ;$observe that (6.17) remains true after this refinement; to simplify notation, we still use$\mathbb { T } _ { \delta _ { i } }$and T to denote these refinement) and a set W of convex subsets of$\mathbb { R } ^ { 3 }$. If$| W | \ge \delta ^ { \zeta _ { 1 } / 2 }$, then$C _ { F - C W } ( \mathbb { T } ^ { T _ { \delta _ { i } } } ) \le \delta ^ { - \zeta _ { 1 } / 2 }$. In this case, we say$\mathbb { T } ^ { T _ { \delta _ { i } } }$is of Type 1.$\mathrm { I f ~ } | W | < \delta ^ { \zeta _ { 1 } / 2 }$, then we say we say$\mathbb { T } ^ { T _ { \delta _ { i } } }$is of Type 2.

We now proceed as follows. For each$i = N - 1 , \ldots , 1$, if at least half the sets$\mathbb { T } ^ { T _ { \delta _ { i } } } , \ T _ { \delta _ { i } } \in \mathbb { T } _ { \delta _ { i } }$ are of Type 1, then we refine$\mathbb { T } _ { \delta _ { i } }$to only consist of those$T _ { \delta _ { i } }$for which$\mathbb { T } ^ { T _ { \delta _ { i } } }$are of Type 1; observe that (6.17) remains true after this refinement. We say that T has passed stage i. On the other hand, if at least half the sets$\mathbb { T } ^ { T _ { \delta _ { i } } } , \ T _ { \delta _ { i } } \in \mathbb { T } _ { \delta _ { i } }$are of Type 2, then we say that$\mathbb { T }$has failed stage i.

Suppose that T passes every stage$i = N - 1 , \dots , 1$. Then by (6.17) we have that for each $i = 1 , \ldots , N$, the set$\mathbb { T } _ { \delta _ { i } }$(this consists of those δ<sub>i</sub>-tubes that survived the refinements described above) is a$\approx _ { \delta }$1-balanced partitioning cover of T. Furthermore, since T passed stage i, we have that for each$T _ { \delta _ { i } } \in \mathbb { T } _ { \delta _ { i } }$we have that$C _ { F - C W } ( \mathbb { T } ^ { T _ { \delta _ { i } } } ) \underset { \approx \delta } { \lessapprox } \delta ^ { - \zeta _ { 1 } / 2 }$. We conclude that T satisfies the Frostman Convex Wolf Axioms at every scale with error$O ( \delta ^ { - \zeta _ { 1 } } )$), and hence Conclusion (A) of Proposition 6.3 holds.

Step 2. Suppose that T fails some stage$i \geq 1$. After pigeonholing and replacing$\mathbb { T } _ { \delta _ { i } }$and T by a $\approx _ { \delta }$1 refinement, we may suppose that there exists$\delta \leq a \leq b \leq 1$so that for each$T _ { \delta _ { i } } \in \mathbb { T } _ { \delta _ { i } }$, the output of Proposition 4.6 applied to$\mathbb { T } ^ { T _ { \delta _ { i } } }$consists of a set$\mathcal { W } _ { T _ { \delta _ { i } } }$of$\begin{array} { r } { \frac { a } { \delta _ { i } } \times \frac { b } { \delta _ { i } } \times 1 } \end{array}$prisms that forms a ${ \approx } \delta$1 balanced cover of$\mathbb { T } ^ { T _ { \delta _ { i } } }$, and factors$\mathbb { T } ^ { T _ { \delta _ { i } } }$from above (resp. below) with respect to the Katz-Tao Convex Wolf Axioms (resp. Frostman Convex Wolf Axioms) with error$\lessapprox \delta { \mathrm { ~ 1 ~ } }$

Since the tubes in$\mathbb { T } _ { \delta _ { i } }$are essentially distinct, we can further refine$\mathbb { T } _ { \delta _ { i } }$by$\mathrm { a } \sim 1$factor so that every pair of distinct tubes$T _ { \delta _ { i } } , T _ { \delta _ { i } } ^ { \prime } \in \mathbb { T } _ { \delta _ { i } }$that intersect must satisfy$\angle \big ( \mathrm { d i r } ( T _ { \delta _ { i } } ) , \ \mathrm { d i r } ( T _ { \delta _ { i } } ^ { \prime } ) \big ) \geq 1 0 0 \delta _ { i }$ so in particular we have

$$
\mathrm{diam} (2 T _ {\delta_ {i}} \cap 2 T _ {\delta_ {i}} ^ {\prime}) \leq \frac {1}{2}.\tag{6.18}
$$

Define

$$
\mathcal {W} = \bigsqcup_ {T _ {\delta_ {i}} \in \mathbb {T} _ {\delta_ {i}}} \phi_ {T _ {\delta_ {i}}} ^ {- 1} \big (\mathcal {W} _ {T _ {\delta_ {i}}} \big).
$$

Then W is a collection of convex sets, each of which is comparable to a$a \times b \times 1$prism. Recall that since T failed stage$i ,$we have that the prisms in$\mathcal { W }$are substantially smaller than the tubes in$\mathbb { T } _ { \delta _ { i } }$; specifically, we have

$$
| W | \lesssim \delta^ {\zeta_ {1} / 2} | T _ {\delta_ {i}} |.\tag{6.19}
$$

We claim that the convex sets in W are essentially distinct. To verify this claim, we argue as follows. Every pair of convex sets W, W<sup>′</sup> from the same set$\mathcal { W } _ { T _ { \delta _ { i } } }$are essentially distinct. On the other hand, if$W \in \mathcal { W } _ { T _ { \delta _ { i } } }$and$W ^ { \prime } \in \mathcal { W } _ { T _ { \delta _ { i } } ^ { \prime } }$for distinct tubes$T _ { \delta _ { i } }$and$T _ { \delta _ { i } } ^ { \prime }$, then diam$( W \cap W ^ { \prime } ) \leq$ diam$\begin{array} { r } { ( T _ { \delta _ { i } } \cap T _ { \delta _ { i } } ^ { \prime } ) \leq \frac { 1 } { 2 } } \end{array}$by (6.18), from which it follows that W and$W ^ { \prime }$are essentially distinct.

Since W is$\mathrm { ~ a ~ } \approx _ { \delta }$1 balanced cover of$\mathbb { T } ,$, and$C _ { F - C W } ( \mathbb { T } ) \lesssim _ { \delta } \delta ^ { - \eta }$, by Remark 4.3(A) (Frostman Wolf Axioms are inherited upwards), we have$C _ { F - C W } ( { \mathcal W } ) \lesssim _ { \delta } \delta ^ { - \eta } ;$we will select$\eta > 0$suficiently small so that$C _ { F - C W } ( \mathcal { W } ) \lesssim \delta ^ { - \zeta _ { 3 } }$

Step 3. Suppose that the prisms in W are flat, in the sense that$a \leq \delta ^ { \zeta _ { 2 } / 1 0 0 } b$. Our task is to show that W and our refined set T satisfies the conditions of Conclusion (C) from Proposition 6.3.

Each$W \in { \mathcal { W } }$came from some set$\mathcal { W } _ { T _ { \delta _ { i } } }$. We claim that if$W ^ { \prime } \in \mathcal { W }$satisfies$W ^ { \prime } \subset N _ { b } ( W )$, then we must have that$W ^ { \prime }$came from the same set$\mathcal { W } _ { T _ { \delta _ { i } } }$, i.e.

$$
\mathcal {W} [ N _ {b} (W) ] = (\mathcal {W} [ T _ {\delta_ {i}} ]) [ N _ {b} (W) ] = \phi_ {T _ {\delta_ {i}}} ^ {- 1} (\mathcal {W} _ {T _ {\delta_ {i}}}) [ N _ {b} (W) ].\tag{6.20}
$$

To verify this claim, we argue by contradiction: suppose instead that$W ^ { \prime }$came from a distinct tube $T _ { \delta _ { i } } ^ { \prime }$, then we would have$W ^ { \prime } \subset N _ { b } ( W ) \cap T _ { \delta _ { i } } ^ { \prime } \subset 2 T _ { \delta _ { i } } \cap T _ { \delta _ { i } } ^ { \prime }$, and in particular the latter set would have diameter$\geq 1$. But this is forbidden by (6.18).

(6.20) implies that

$$
C _ {K T - C W} \big (\mathcal {W} [ N _ {b} (W) ] \big) = C _ {K T - C W} \big ((\mathcal {W} [ T _ {\delta_ {i}} ]) [ N _ {b} (W) ] \big) \leq C _ {K T - C W} (\mathcal {W} _ {T _ {\rho_ {i}}}) \lesssim_ {\delta} 1.
$$

Thus W and our refined set T satisfies the conditions of Conclusion (C) from Proposition 6.3.

Step 4. Now we consider the case where the prisms in W are not flat, in the sense that$a > \delta ^ { \zeta _ { 2 } / 1 0 0 } b$ Define τ to be the smallest admissible scale greater than or equal to b. Since at most${ \cal O } ( ( b / a ) ^ { 3 } )$ essentially distinct$a \times b \times 1$prisms can fit inside a b-tube, and at most${ \cal O } ( \delta ^ { - 4 / N } ) = { \cal O } ( \delta ^ { - 4 \eta } )$ essentially distinct b-tubes can fit inside${ \mathrm { a ~ } } \tau { \mathrm { - t u b e } }$, we have that${ \mathcal W } [ T _ { \tau } ] \lesssim \delta ^ { - 4 \eta } ( b / a ) ^ { 3 } \lesssim \delta ^ { - 4 \zeta _ { 2 } / 1 0 0 }$for every τ-tube$T _ { \tau }$(for the last inequality we select$\eta \leq \zeta _ { 2 } / 4 0 0 )$. After pigeonholing T, W, and$\mathbb { T } _ { \tau } .$ we may suppose that$\mathbb { T } _ { \tau }$is a balanced partitioning cover of W. We have

$$
1 \leq \# \mathcal {W} [ T _ {\tau} ] \lesssim \delta^ {- 4 \zeta_ {2} / 1 0 0} \quad \text { for   each } T _ {\tau} \in \mathbb {T} _ {\tau}.\tag{6.21}
$$

Since$C _ { F - C W } ( \mathbb { T } [ W ] ) \not \approx \delta ^ { \ 1 }$for each$W \in { \mathcal { W } }$, we conclude from (6.21) that$C _ { F - C W } ( \mathbb { T } [ T _ { \tau } ] ) \lesssim _ { \delta } \delta ^ { - 4 \zeta _ { 2 } / 1 0 0 }$ for each$T _ { \tau } \in \mathbb { T } _ { \tau } ;$this gives us Conclusion (B.i).

At this point, we have correctly identified the scale$\tau$from Conclusion (B) of Proposition 6.3. What about the scale$\rho ?$One candidate is$\delta _ { i } ;$by (6.19) we have$\tau \lesssim \delta ^ { \zeta _ { 1 } / 4 - 2 \dot { \zeta } _ { 2 } / 1 0 0 } \delta _ { i } \stackrel { - } { \leq } \delta ^ { \zeta _ { 1 } / 5 } \delta _ { i }$, as specified in Conclusion (B).

The scale$\delta _ { i }$satisfies some of the required properties of Conclusion (B). Recall that for each $T _ { \delta _ { i } } \in \mathbb { T } _ { \delta _ { i } }$, we have$C _ { K T - C W } ( \mathcal { W } [ T _ { \delta _ { i } } ] ) \lessapprox _ { \delta } 1$. Since$| T _ { \tau } | = ( b / a ) | W | \leq \delta ^ { - \zeta _ { 2 } / 1 0 0 } | W |$, by (6.21) we have

$$
C _ {K T - C W} \left(\mathbb {T} _ {\tau} \left[ T _ {\delta_ {i}} \right]\right) \leq \delta^ {- 5 \zeta_ {2} / 1 0 0} \quad \text { for   each } T _ {\delta_ {i}} \in \mathbb {T} _ {\delta_ {i}}.\tag{6.22}
$$

This is half of Conclusion (B.ii). If$\frac { \# \mathbb { T } _ { \tau } } { \# \mathbb { T } _ { \delta _ { i } } } \geq \delta ^ { 1 0 0 \eta } ( \delta _ { i } / \tau ) ^ { 2 }$(in fact a weaker estimate$\begin{array} { r } { \frac { \# \mathbb { T } _ { \tau } } { \# \mathbb { T } _ { \delta _ { i } } } \geq \delta ^ { \zeta _ { 2 } } ( \delta _ { i } / \tau ) ^ { 2 } } \end{array}$ sufices), then after a refinement,$\mathbb { T } _ { \delta _ { i } }$satisfies Conclusion (B.ii). Conclusion (B.iii) then follows from Remark 4.3(A) (Frostman Wolf Axioms are inherited upwards), and we are done.

Suppose instead that$\begin{array} { r } { \frac { \# \mathbb { T } _ { \tau } } { \# \mathbb { T } _ { \delta _ { i } } } < \delta ^ { 1 0 0 \eta } ( \delta _ { i } / \tau ) ^ { 2 } } \end{array}$. Let$\rho$be the minimum of all admissible scales in $[ \delta _ { i } , 1 ]$for which

$$
\frac {\# \mathbb {T} _ {\tau}}{\# \mathbb {T} _ {\rho}} \geq \delta^ {1 0 0 \eta} (\rho / \tau) ^ {2}.\tag{6.23}
$$

Such a choice of$\rho \in [ \rho _ { i } , 1 ]$must exist, since$C _ { F - C W } ( \mathbb { T } _ { \tau } ) \ \lessapprox \delta ^ { - \eta }$, and hence$\# \mathbb { T } _ { \tau } \gtrapprox \delta \tau \tau ^ { - 2 }$, from which it follows that$\rho = 1$satisfies (6.23) and hence$\rho = 1$is a valid candidate.

In particular, for this choice of$\rho$we have

$$
\delta^ {1 0 0 \eta} (\rho / \tau) ^ {2} \leq \frac {\# \mathbb {T} _ {\tau}}{\# \mathbb {T} _ {\rho}} \leq \delta^ {5 0 \eta} (\rho / \tau) ^ {2},\tag{6.24}
$$

since if the RHS of (6.24) failed, then (6.23) would hold for a smaller admissible scale, which would contradict the minimality of$\rho .$

Suppose for the moment that there exists a$\gtrapprox \delta$1-refinement of$\mathbb { T } _ { \tau }$(abusing notation, we will continue to call this set$\mathbb { T } _ { \tau } )$such that

$$
C _ {F - C W} \left(\mathbb {T} _ {\tau} ^ {T _ {\rho}}\right) \leq \delta^ {- \zeta_ {2} / 2} \quad \text { for   at   least   half   of   the   tubes } T _ {\rho} \in \mathbb {T} _ {\rho}.\tag{6.25}
$$

Then (6.24) plus (6.25) implies that Conclusion (B.ii) holds, and Conclusion (B.iii) follows from Remark 4.3(A) (Frostman Wolf axioms are inherited upwards). Thus if (6.25) is true, then Conclusion (B) of Proposition 6.3 holds, and we are done.

Step 5. We claim that either (6.25) holds (and we are done, as discussed in the previous step), or else Conclusion (C) of Proposition 6.3 holds.

We will verify this claim as follows. Suppose that (6.25) fails. Applying Proposition 4.6 to each set$\mathbb { T } ^ { T _ { \rho } }$and then undoing the scaling$\phi _ { T _ { \rho } }$, we obtain a refinement of$\mathbb { T } [ T _ { \rho } ]$(abusing notation, we will continue to call this set$\mathbb { T } [ T _ { \rho } ] )$, and a set$\mathcal { U } _ { T _ { \rho } }$of$s \times t \times 1$prisms contained in$T _ { \rho }$(so in particular $t \le \rho )$that factors$\mathbb { T } [ T _ { \rho } ]$from below with respect to the Frostman Convex Wolf axioms with error $\lessapprox \delta { \mathrm { ~ 1 ~ } }$and each$T \in \mathbb { T } [ T _ { \rho } ]$is contained in$\lessapprox \delta { \mathrm { ~ 1 ~ } }$sets$U \in \mathcal { U } _ { T _ { \rho } }$

Pigeonhole and refine$\mathbb { T } _ { \rho }$to consist of those tubes$T _ { \rho }$for which$C _ { F - C W } \big ( \mathbb { T } _ { \tau } ^ { T _ { \rho } } \big ) > \delta ^ { - \zeta _ { 2 } / 2 }$(such a refinement exists because (6.25) fails) and the corresponding sets$\mathcal { U } _ { T _ { \rho } }$are comparable to$s \times t \times 1$ prisms for a common pair of numbers$( s , t )$. In particular, this implies

$$
| U | \lesssim_ {\delta} \delta^ {\zeta_ {2} / 2} | T _ {\rho} |.\tag{6.26}
$$

(C.f. (6.19) when$s \geq \tau$. When$s \leq \tau$, this is true because$\tau \lesssim \delta ^ { \zeta _ { 1 } / 5 } \delta _ { i } \leq \delta ^ { \zeta _ { 1 } / 5 } \rho )$

Suppose for the moment that$s \geq \tau$. Then$C _ { F - C W } ( \mathbb { T } _ { \tau } ^ { U } ) \lessapprox \delta \ 1$by Remark$4 . 3 ( \mathrm { A } )$(Frostman Wolf axioms are inherited upwards). By (6.24) and our hypothesis that$C _ { F - C W } \big ( \mathbb { T } _ { \tau } ^ { T _ { \rho } } \big ) > \delta ^ { - \zeta _ { 2 } / 2 }$, we have

$$
C _ {K T - C W} \left(\mathbb {T} _ {\tau} \left[ T _ {\rho} \right]\right) \geq \delta^ {- \zeta_ {2} / 2 + 1 0 0 \eta}.\tag{6.27}
$$

We conclude that by Item ii) of Proposition 4.6,

$$
\# (\mathbb {T} [ T _ {\rho} ]) [ U ] \gtrsim_ {\delta} C _ {K T - C W} (\mathbb {T} [ T _ {\rho} ]) \left(\frac {| U |}{| T |}\right) \quad \text { for   each } U \in \mathcal {U} _ {T _ {\rho}}.
$$

Since$s \geq \tau$and τ is an admissible scale, we have

$$
C _ {K T - C W} (\mathbb {T} [ T _ {\rho} ]) \gtrsim_ {\delta} \frac {\# \mathbb {T}}{\# \mathbb {T} _ {\tau}} \frac {| T |}{| T _ {\tau} |} C _ {K T - C W} (\mathbb {T} _ {\tau} [ T _ {\rho} ]),
$$

and so

$$
\# (\mathbb {T} _ {\tau} [ T _ {\rho} ]) [ U ] \gtrsim_ {\delta} C _ {K T - C W} \bigl (\mathbb {T} _ {\tau} [ T _ {\rho} ] \bigr) \Bigl (\frac {| U |}{| T _ {\tau} |} \Bigr) \geq \delta^ {- \zeta_ {2} / 2 + 1 0 0 \eta} \Bigl (\frac {| U |}{| T _ {\tau} |} \Bigr) \quad \text { for   each } U \in \mathcal {U} _ {T _ {\rho}}.\tag{6.28}
$$

We will show that

$$
s <   \delta^ {\zeta_ {2} / 1 0 0} t.\tag{6.29}
$$

To verify (6.29), suppose to the contrary that$s \geq \delta ^ { \zeta _ { 2 } / 1 0 0 } t ;$we will obtain a contradiction. If $s \geq \delta ^ { \zeta _ { 2 } / 1 0 0 } t$then$t \leq \delta ^ { \zeta _ { 2 } / 4 } \rho$. By (6.28) and the fact that each tube in$\mathbb { T } _ { \tau } [ T _ { \rho } ]$is contained in$\lessapprox$1 sets$U \in \mathcal { U } _ { T _ { \rho } }$, we have

$$
\# \mathcal {U} _ {T _ {\rho}} \lessapprox_ {\delta} \frac {\# \mathbb {T} _ {\tau} [ T _ {\rho} ]}{\inf _ {U \in \mathcal {U} _ {T _ {\rho}}} \# (\mathbb {T} _ {\tau} [ T _ {\rho} ]) [ U ]} \lessapprox_ {\delta} \delta^ {\zeta_ {2} / 2 - 1 0 0 \eta} (\# \mathbb {T} _ {\tau} [ T _ {\rho} ]) \frac {| T _ {\tau} |}{| U |} \leq \delta^ {\frac {4 8}{1 0 0} \zeta_ {2}} (\# \mathbb {T} _ {\tau} [ T _ {\rho} ]) \big (\frac {\tau}{t} \big) ^ {2},
$$

and thus if$t ^ { \prime }$is the smallest admissible scale greater than or equal to t, then

$$
\# \mathbb {T} _ {t ^ {\prime}} \leq \# \left(\bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho}} \mathcal {U} _ {T _ {\rho}}\right) \lesssim_ {\delta} \delta^ {\frac {4 8}{1 0 0} \zeta_ {2}} (\# \mathbb {T} _ {\tau}) \left(\frac {\tau}{t}\right) ^ {2} \leq \delta^ {\frac {4 7}{1 0 0} \zeta_ {2}} (\# \mathbb {T} _ {\tau}) \left(\frac {\tau}{t ^ {\prime}}\right) ^ {2}.\tag{6.30}
$$

From (6.30) we see that$t ^ { \prime } \geq \delta _ { i } - \mathrm { i f }$not, then there would exist a t<sup>′</sup>-tube$T _ { t ^ { \prime } }$with$\# \mathbb { T } _ { \tau } [ T _ { t ^ { \prime } } ] \gtrapprox \delta$ $\delta ^ { - \frac { 4 7 } { 1 0 0 } \zeta _ { 2 } } \frac { | T _ { t ^ { \prime } } | } { | T _ { \tau } | }$, and this t<sup>′</sup>-tube would be contained in some$\delta _ { i } .$-tube; but this violates (6.22).

Comparing (6.30) and (6.23), we see that$t ^ { \prime } \in [ t , \delta ^ { \zeta _ { 2 } / 5 } \rho ] \subset [ \delta _ { i } , \delta ^ { \zeta _ { 2 } / 5 } \rho ]$is an admissible scale that satisfies (6.24). But this contradicts the assumption that$\rho$was the minimal such scale. We conclude that (6.29) must hold.

When (6.29) holds, we are in precisely the same situation as the beginning of Step 3: The set of flat (recall (6.29)) prisms$\begin{array} { r } { \mathcal { U } = \bigcup _ { T _ { \rho } \in \mathbb { T } _ { \rho } } \mathcal { U } _ { T _ { \rho } } } \end{array}$plays the role of W, and the set of essentially distinct ρ-tubes$\mathbb { T } _ { \rho }$plays the role of$\mathbb { T } _ { \delta _ { i } }$. An identical argument with the same numerology (up to harmless $\delta ^ { \eta }$factors) shows that Conclusion (C) of Proposition 6.3 holds.

Now suppose (6.29) does not hold, so$\delta ^ { \zeta _ { 2 } / 1 0 0 } t \le s < \tau$. If$s \geq \tau \delta ^ { \zeta _ { 2 } / 2 0 }$, then together with $s \geq \delta ^ { \zeta _ { 2 } / 1 0 0 } t$

$$
C _ {K T - C W} \left(\mathbb {T} _ {\tau} \left[ T _ {\rho} \right]\right) \leq \delta^ {- \zeta_ {2} / 4} C _ {K T - C W} \left(\mathcal {U} _ {T _ {\rho}}\right) \lesssim_ {\delta} \delta^ {- \zeta_ {2} / 4},
$$

which is a contradiction to (6.27). So we may assume$s \leq \tau \delta ^ { \zeta _ { 2 } / 2 0 }$and$s \geq \delta ^ { \zeta _ { 2 } / 1 0 0 } t$, and we are in the same situation as the beginning of Step 4 with$( s , t )$in place of$( a , b ) , \mathcal { U }$in place of W, and$\mathbb { T } _ { \rho }$in place of$\mathbb { T } _ { \delta _ { i } }$. However, we have the additional condition that$s / \rho \le \delta ^ { \zeta _ { 2 } / 2 0 } \tau / \delta _ { i } ;$; this means that the prisms in U are substantially flatter than the prisms in W. We return to the beginning of Step 4 and repeat the argument; we iterate this process until either Conclusion (B) or Conclusion (C) holds; this must occur after at most$2 0 / \zeta _ { 2 }$iterations. Note that each iteration of this process induces a $\approx _ { \delta }$1 refinement of T, etc. but since this process repeats at most$2 0 / \zeta _ { 2 }$times, this refinement is harmless.

## 7 A two-scale grains decomposition for tubes in$\mathbb { R } ^ { 3 }$

In [16], Katz, Laba and Tao proved that every union of δ tubes in$\mathbb { R } ^ { 3 }$coming from the discretization of a (hypothetical) Kakeya set with upper Minkowski dimension$5 / 2$can be written as a union of “grains,” (i.e. rectangular prisms) of dimensions roughly$\delta \times \delta ^ { 1 / 2 } \times \delta ^ { 1 / 2 }$. Guth [9] generalized this result and proved that every union of δ tubes in$\mathbb { R } ^ { 3 }$satisfying a certain broadness hypothesis can be written as a union of grains of dimensions roughly$\delta \times t \times t .$, where the diameter t is related to the number of tubes in the arrangement and the volume of their union.

The purpose of this section is to prove a structural statement for unions of δ tubes in$\mathbb { R } ^ { 3 }$, in the spirit of the Katz- Laba-Tao and Guth results described above. This is Proposition 7.5 below. As discussed in the introduction, Proposition 7.5 is a key step in the proof of Proposition 1.7— Proposition 7.5 helps us find the correct scales and arrangements of convex sets to which we can apply Assertion$\mathcal { E } ( \sigma , \omega )$

In brief, Proposition 7.5 explores what happens when we cover an arrangement of δ-tubes by ρ-tubes, apply (a variant of) Guth’s grains theorem inside each re-scaled$\rho \mathrm { - t u b e }$, and then analyze how the resulting grains coming from the δ tubes inside diferent ρ-tubes interact. The specific hypotheses and conclusions of Proposition 7.5 are somewhat technical; they were adapted to match the needs of the arguments in Section 9. In order to state Proposition 7.5 we will require a few definitions.

Definition 7.1. Let$\lambda > 0 , 0 < \delta \leq \rho \leq 1$and$\delta \leq a \leq b \leq c$with$\rho = b / c$. Let$( \mathbb { T } , Y ) _ { \delta }$be a set of$\delta$tubes and their associated shading, and let$\mathbb { T } _ { \rho }$be a balanced partitioning cover of T. We say $( { \mathcal { P } } , Y ) _ { a \times b \times c }$is a robustly λ-dense two-scale grains decomposition of$( \mathbb { T } , Y ) _ { \delta }$with regard to$( w r t ) \mathbb { T } _ { \rho }$ if the following is true:

![](images/page_60_image_0.jpg)

Figure 9: A tube exiting a grain through the long ends (left) vs failing to do so (middle and right).

(i) For each$P \in \mathcal { P }$, there is a unique$\mathbb { T } _ { \rho } \in \mathbb { T } _ { \rho }$satisfying$P \subset T _ { \rho }$and$\angle ( \mathrm { d i r } ( P ) , \mathrm { d i r } ( T _ { \rho } ) ) \leq 2 \rho$ This induces a partition$\begin{array} { r } { \mathcal { P } = \bigcup _ { \mathbb { T } _ { \rho } } \mathcal { P } _ { T _ { \rho } } } \end{array}$

(ii) For each$T _ { \rho } \in \mathbb { T } _ { \rho } ,$the sets$\{ Y ( P ) \colon P \in P \in \mathcal { P } _ { T _ { \rho } } \}$are disjoint, and we have

$$
\bigcup_ {T \in \mathbb {T} [ T _ {\rho} ]} Y (T) = \bigsqcup_ {P \in \mathcal {P} _ {T _ {\rho}}} Y (P).\tag{7.1}
$$

(iii) The pair$( { \mathcal { P } } , Y ) _ { a \times b \times c }$is λ-dense, and furthermore there exists a number$\mu$so that for each $T _ { \rho } \in \mathbb { T } _ { \rho }$and each$x \in ( 7 . 1 )$, we have$\# \mathbb { T } [ T _ { \rho } ] _ { Y } ( x ) \sim \mu$

(iv) For each$T _ { \rho } \in \mathbb { T } _ { \rho }$and each pair$T \in \mathbb { T } [ T _ { \rho } ]$and$P \in \mathcal { P } _ { T _ { \rho } }$with$Y ( T ) \cap Y ( P ) \neq \emptyset$, we have that T exits P through the “long end” (See Figure 9), and$Y ( T ) \cap P \subset Y ( P )$

Remark 7.2. Conclusion (iv) implies that$a \geq 2 \delta$. Usually we will be interested in the case where $a \sim \delta$, though it will sometimes be useful to consider larger values of a.

Definition 7.3. Let P be a$a \times b \times c$prism. Define$\boxed { \ d } ( P )$to be the$\textstyle { \frac { a c } { b } } \times c \times c$prism containing P with the same center and normal direction as$P$(the latter condition means that$\Pi ( P ) = \Pi ( \bigtriangledown ( P ) )$. Observe that both Π(P) and$\Pi ( \bigsqcup ( P ) )$are defined up to accuracy$a / b$

Let P be a set of$a \times b \times c$prisms, and let W be a convex set. Define

$$
\mathcal {P} \langle W \rangle = \{P \in \mathcal {P}: \square (P) \subset W \}.
$$

Note that since$P \subset \boxed { \square ( P ) }$, we have${ \mathcal { P } } \langle W \rangle \subset { \mathcal { P } } [ W ]$

Observe that if$P , P ^ { \prime }$are intersecting$a \times b \times c$prisms and$\begin{array} { r } { \angle ( \Pi ( P ) , \Pi ( P ^ { \prime } ) ) \le K \frac { a } { b } } \end{array}$for some $K \geq 1$, then the K-fold thickenings (i.e. the prisms of dimensions$\textstyle { \frac { a c } { b } } \times c \times c$with the same center, direction, and tangent plane) of$\boxed { \ d } ( P )$and$\boxed { \ d } ( P ^ { \prime } )$are comparable up to factors of K. In particular, if$( { \mathcal { P } } , Y ) _ { a \times b \times c }$is a pair of prisms and their associated shadings, with$\begin{array} { r } { \angle ( \Pi ( P ) , \Pi ( P ^ { \prime } ) ) \le K \frac { a } { b } } \end{array}$for all pairs$P , P ^ { \prime } \in \mathcal { P }$for which$Y ( P ) \cap Y ( P ^ { \prime } ) \neq \emptyset$, then we can find a set W of prisms of dimensions comparable to$\begin{array} { r } { K \frac { a c } { b } \times c \times c } \end{array}$so that each$P \in { \mathcal { P } }$is contained in at least 1, and at most$O ( 1 )$sets of the form${ \mathcal { P } } \langle W \rangle$⟩,$W \in { \mathcal { W } }$. Furthermore, the sets$\{ \cup _ { P \in { \mathcal { P } } \langle W \rangle } Y ( P ) , W \in \mathcal { W } \}$are$O ( 1 )$overlapping.

In our arguments below, we will exploit the above observation when$K \ \leq \ \delta ^ { - \varepsilon }$for a small $\varepsilon > 0$. Since we will analyze each set${ \mathcal { P } } \langle W \rangle$individually, we will be interested in the quantity $C _ { K T - C W } ( { \mathcal { P } } \langle W \rangle )$, rather than the (potentially much larger) quantity$C _ { K T - C W } ( \mathcal { P } )$. Each set W contains at most$1 0 0 K ^ { 1 0 0 }$essentially distinct prisms of the form$\boxed { \ d } ( P )$, and thus if K is not too large then$C _ { K T - C W } ( \mathcal { P } \langle W \rangle )$is controlled by s$\mathrm { u p } _ { P } C _ { K T - C W } ( { \mathcal { P } } \langle 2 \varTheta ( P ) \rangle )$), where$2 \boldsymbol { \boxed { P } } ( \boldsymbol { P } )$denotes the 2-fold dilate of$\boxed { \ d } ( P )$. This motivates the following definition.

Definition 7.4. Let$\mathcal { P }$be a set of$a \times b \times c$prisms. Define

$$
C _ {K T - C W} ^ {\mathrm{loc}} (\mathcal {P}) = \max _ {P \in \mathcal {P}} C _ {K T - C W} \bigl (\mathcal {P} \langle 2 \Box (P) \rangle \bigr).
$$

With these definitions, we can now state the main result of Section$7 .$

Proposition 7.5. Let$\omega > 0 , \sigma \in ( 0 , 2 / 3 ]$, and$\zeta \in ( 0 , \omega / 1 0 0 0 )$. Suppose that$\mathcal { E } ( \sigma , \omega )$is true. Then there exists$\alpha , \eta , \kappa > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, with $C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Then at least one of the following must hold.

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega - \alpha} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.\tag{A}
$$

(B) There exist the following:

– Numbers ρ and$\delta \leq a \leq b \leq c \leq 1$, with$\rho = b / c$

$A ~ \delta ^ { \zeta }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ~ o f \left( \mathbb { T } , Y \right) _ { \delta }$

$A$set$\mathbb { T } _ { \rho }$of ρ tubes.

– A pair$( { \mathcal { G } } , Y ) _ { a \times b \times c } .$

These objects have the following properties:

(i)$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is$\delta ^ { \zeta }$dense,$C _ { K T - C W } ( \mathbb { T } ^ { \prime } ) \le \delta ^ { - \zeta }$, and$C _ { F - S W } ( \mathbb { T } ^ { \prime } ) \leq \delta ^ { - \zeta }$

(ii)$\mathbb { T } _ { \rho }$is a balanced partitioning cover$o f \mathbb { T } ^ { \prime }$that factors$\mathbb { T } ^ { \prime }$above and below with respect to the Frostman Slab Wolf Axioms with error${ \delta } ^ { - \zeta }$

(iii)$( \mathcal { G } , Y ) _ { a \times b \times c }$is a robustly$\delta ^ { \zeta }$-dense two-scale grains decomposition of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$wrt$\mathbb { T } _ { \rho } .$

(iv)

$$
c \geq \delta^ {\zeta} \frac {\rho}{\delta} \frac {\# \mathbb {T} _ {\rho}}{\# \mathbb {T} _ {\delta}}.\tag{7.2}
$$

(v)$\delta ^ { 1 - \omega / 1 0 0 } \leq \rho \leq \delta ^ { \omega / 1 0 0 }$

(vi)$C _ { K T - C W } ^ { \mathrm { l o c } } ( \mathcal { G } ) \leq \delta ^ { - \zeta } .$

An overview for the proof of Proposition 7.5 is outlined in Section 2.2.

Fixing ω and σ. In our proof of Proposition 7.5, the values of$\omega > 0 , \sigma \in ( 0 , 2 / 3 ]$and$\zeta > 0$ will never change. Thus to simplify our exposition below, we will fix values of$\omega , \sigma ,$and ζ, which will remain unchanged throughout Sections 7 and 8. In particular, some of our definitions (such as Definition 7.6, which defines broadness) will depend on these quantities. By fixing them in advance, we can suppress this dependence.

As previewed in Section 2.2, we will make crucial use Guth’s methods to find a grains decomposition inside each re-scaled set$\mathbb { T } ^ { T _ { \rho } }$. In order to apply Guth’s techniques, the tubes need to satisfy a “broadness” condition. We describe this below.

## 7.1 Broadness

For the definition that follows, we will fix$\beta = \omega \zeta / 1 0 0$

Definition 7.6. Let$\delta > 0$and$K \geq 1$. We say a multi-set$\textstyle \mathcal { V } \subset S ^ { n - 1 }$of unit vectors in$\mathbb { R } ^ { n }$is broad with error K at scales$\geq \delta$if for all unit vectors$v _ { 0 } \in \mathbb { R } ^ { n }$and all$r \in [ \delta , 1 ]$we have

$$
\# \{v \in \mathcal {V} \colon \angle (v, v _ {0}) \leq r \} \leq K r ^ {\beta} (\# \mathcal {V}).
$$

More generally, let V be contained in a disk$D \subset S ^ { n - 1 }$of radius$\rho .$. We say V is broad with error K at scales$\geq \delta$inside D if for all unit vectors$v _ { 0 } \in \mathbb { R } ^ { n }$and all$r \in [ \delta , \rho ]$we have

$$
\# \{v \in \mathcal {V} \colon \angle (v, v _ {0}) \leq r \} \leq K (r / \rho) ^ {\beta} (\# \mathcal {V}).
$$

Definition 7.7. Let$( \mathbb { T } , Y ) _ { \delta }$be a collection of tubes and their associated shading, and let$\mathbb { T } _ { \rho }$be a cover of T.

(A) We say that$( \mathbb { T } , Y ) _ { \delta }$is broad with error K if for each$x \in \bigcup _ { T \in \mathbb { T } } Y ( T )$, the set of unit vectors $\{ \mathrm { d i r } ( T ) \colon x \in Y ( T ) \}$is broad with error K at scales$\geq \delta$

(B) We say that$( \mathbb { T } , Y ) _ { \delta }$is broad with error K relative to the cover$\mathbb { T } _ { \rho }$if for each$T _ { \rho } \in \mathbb { T } _ { \rho } ,$the set $( \mathbb { T } ^ { T _ { \rho } } , Y ^ { T _ { \rho } } ) _ { \delta / \rho }$is broad with error$K$

The next result is a variant of the “two ends” reduction. In general, a set V of unit vectors need not be broad (with small error). However, the next result says that every set of unit vectors is broad when localized inside$\rho$disks, for some value of$\rho .$The precise statement is as follows.

Lemma 7.8. Let$\delta > 0$and let V be a set of vectors in R<sup>n</sup> pointing in δ-separated directions. Then there exists a scale$\rho \in [ \delta , 1 ]$; a set B of disjoint balls$B \subset S ^ { n - 1 }$of radius$\rho ;$and sets$\mathcal { V } _ { B } \subset \mathcal { V } \cap B$ so that the following holds.

(i) Each set$\gamma _ { B }$has cardinality$\gtrsim \rho ^ { \beta } ( \# \mathcal { V } )$

(ii)$\gamma _ { B }$is broad with error 100 at scales$\geq \delta$inside$B$.

(iii)$\cup _ { B } \mathcal { V } _ { B } \gtrsim ( \log 1 / \delta ) ^ { - 1 } ( \# \mathcal { V } )$

Proof. We will greedily construct a sequence of sets$\mathcal { V } = \mathcal { V } _ { 0 } \supset \mathcal { V } _ { 1 } \supset . .$. as follows. For each index $i \geq 1$, let$v _ { i }$be a unit vector and$r _ { i } \in [ \delta , 1 ]$a radius that maximizes the quantity

$$
r _ {i} ^ {- \beta} (\# \mathcal {V} _ {i - 1} \cap B (v _ {i}, r _ {i})).\tag{7.3}
$$

Let$\mathcal { W } _ { i } = \mathcal { V } _ { i - 1 } \cap B ( v _ { i } , r _ { i } )$and let$\mathcal { V } _ { i } ~ = ~ \mathcal { V } _ { i - 1 } \backslash B ( v _ { i } , ~ 1 0 0 r _ { i } )$. Note that$\# ( \mathcal { V } _ { i - 1 } \cap B ( v _ { i } , 3 r _ { i } ) ) \ \leq$ $1 0 0 ^ { \beta } ( \# \mathcal { W } _ { i } )$. Continue this process until$\# \mathcal { V } _ { i } \leq \frac { 1 } { 2 } \# \mathcal { V }$

We claim that for each index i, each unit vector v, and each$r \geq \delta$, we have

$$
\# (\mathcal {W} _ {i} \cap B (v, r)) \leq 1 0 0 (r / r _ {i}) ^ {\beta} (\# \mathcal {W} _ {i}).\tag{7.4}
$$

This will give Conclusion (ii). To verify (7.4), suppose to the contrary that (7.4) failed for some pair$( v , r )$, then this would contradict the maximality of$( v _ { i } , r _ { i } )$in (7.3).

Note as well that since$r _ { i } = 1$is a valid choice of r, we have$\# \mathcal { W } _ { i } \geq r _ { i } ^ { \beta } ( \# \mathcal { V } _ { i - 1 } ) \geq \frac { 1 } { 2 } r _ { i } ^ { \beta } ( \# \mathcal { V } )$ Finally, note that if$r _ { i } \ \leq \ r _ { j } \ \leq \ 2 r _ { i } .$, then the balls$2 B ( v _ { i } , r _ { i } )$and$2 B ( v _ { j } , r _ { j } )$must be disjoint. Indeed, we may suppose that both$\mathcal { W } _ { i }$and$\mathcal { W } _ { j }$are non-empty. If$\textit { i } < \textit { j }$then we must have $B ( v _ { j } , r _ { j } ) \cap B ( v _ { i } , 1 0 0 r _ { i } ) ^ { c } \neq \emptyset$, while if$j < i$then we must have$B ( v _ { i } , r _ { i } ) \cap B ( v _ { i } , 1 0 0 r _ { j } ) ^ { c } \neq \emptyset$. In either case, since$r _ { i } \le r _ { j } \le 2 r _ { i }$, this means that$2 B ( v _ { i } , r _ { i } ) \cap 2 B ( v _ { j } , r _ { j } ) = \emptyset$

To conclude the proof, use dyadic pigeonholing to select a scale$\rho \in [ \delta , 1 ]$so that$\# \bigcup _ { i : \rho / 2 \leq r _ { i } \leq \rho } \mathcal { W } _ { i } \gtrsim$ $( \log 1 / \delta ) ^ { - 1 } ( \# \mathcal { V } )$. This gives us the collection B of disjoint balls (it is harmless for us to replace each ball$B ( v _ { i } , r _ { i } )$with$B ( v _ { i } , \rho )$; as noted above, the balls remain disjoint).□

Remark 7.9. Lemma 7.8 is similar to the standard$\mathrm { ^ { 6 6 } t w o \mathrm { - e n d s } ^ { \prime } }$broadness reduction. However, the standard two-ends broadness reduction typically replaces V by$\nu \cap B$for a single ρ ball B. The resulting set has cardinality$\gtrsim \rho ^ { \beta } ( \# \mathcal { V } )$. For our applications, this would have introduced an unacceptably large reduction in the cardinality of V.

Corollary 7.10. Let$( \mathbb { T } , Y ) _ { \delta }$be a set of δ tubes and their corresponding shading. Then there exists $a \gtrapprox \delta 1$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$of$( \mathbb { T } , Y ) _ { \delta } ;$a scale$\rho \in [ \delta , 1 ]$; and a balanced partitioning cover$\mathbb { T } _ { \rho }$of $( \mathbb { T } ^ { \prime } , Y ^ { \prime } )$, so that the following holds:

(i) Each point$\boldsymbol { x } \in \mathbb { R } ^ { 3 }$is contained$\stackrel { < } { \approx } \delta \rho ^ { - \beta }$sets of the form$\begin{array} { r } { \bigcup _ { \mathbb { T } ^ { \prime } [ T _ { \rho } ] } Y ^ { \prime } ( T ) , T _ { \rho } \in \mathbb { T } _ { \rho } . } \end{array}$

(ii) T<sup>′</sup> is broad with error${ \approx } \delta$1 relative to the cover$\mathbb { T } _ { \rho } .$

Proof. Using dyadic pigeonholing, we can select a number$\mu \geq 1$and a$( \log 1 / \delta ) ^ { - 1 }$refinement $( \mathbb { T } , Y _ { 1 } ) _ { \delta }$of$( \mathbb { T } , Y )$with the property that$\# \{ T \in \mathbb { T } \colon x \in Y _ { 1 } ( T ) \} \sim \mu$for each$x \in \bigcup _ { T \in \mathbb { T } } Y _ { 1 } ( T )$ Apply Lemma 7.8 to each point$x \in \bigcup Y _ { 1 } ( T )$. We obtain a scale$\rho _ { x } \in [ \delta , 1 ]$, and a set of disjoint $\rho _ { x }$balls$B _ { x }$(each ball in$B _ { x }$is a subset of$S ^ { 2 } )$. After further dyadic pigeonholing we can select the following:

• A common scale$\rho ;$

• Multiplicities$\nu \geq 1$and$N \lesssim \rho ^ { - \beta }$;

• A set B of ρ balls (each ball in B is a subset of$S ^ { 2 } )$, whose 100ρ neighbourhoods are disjoint;

$\mathrm { A } \gtrsim ( \log 1 / \delta ) ^ { - 1 }$refinement$( \mathbb { T } , Y _ { 2 } ) _ { \delta }$of$( \mathbb { T } , Y _ { 1 } ) _ { \delta }$

We can select the above numbers and sets so that the following property holds: for each$x \in$ $\cup _ { \mathbb { T } } Y _ { 2 } ( T )$, the set of unit vectors$\{ \operatorname { d i r } ( T ) \colon x \in Y _ { 2 } ( T ) \} \subset S ^ { 2 }$can be covered by a union of N balls from B, and for each such ball, we have that the set$B \cap \left\{ \mathrm { d i r } ( T ) : x \in Y _ { 2 } ( T ) \right\}$} has cardinality ν and is broad with error$O ( 1 )$inside B.

After refining T by a factor of${ \approx } _ { \delta } 1$, we obtain a new pair$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$that is$\mathrm { a } \approx _ { \delta } 1$refinement of$( \mathbb { T } , Y _ { 2 } ) _ { \delta }$, and a set$\mathbb { T } _ { \rho }$of$\rho$tubes with the property that$\mathbb { T } _ { \rho }$is a balanced partitioning cover of $\mathbb { T } _ { 2 }$, and furthermore the family of convex sets$\{ 3 T _ { \rho } \colon T _ { \rho } \in  { \mathbb { T } } _ { \rho } \}$is a partitioning cover of$\mathbb { T } _ { 2 }$. This means that for each$T _ { \rho } \in \mathbb { T } _ { \rho } , \mathbb { T } _ { 2 } [ T _ { \rho } ] = \mathbb { T } _ { 2 } [ 3 T _ { \rho } ]$

For each$T \in \mathbb { T } _ { 2 }$with$T \subset T _ { \rho } \in \mathbb { T } _ { \rho } .$, define

$$
Y _ {3} (T) = \{x \in Y _ {2} (T): \# \{T ^ {\prime} \in \mathbb {T} _ {2} [ T _ {\rho} ]: x \in Y _ {2} (T ^ {\prime}) \} \geq \kappa_ {0} \nu \}.
$$

Since$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$is a$\approx _ { \delta }$1 refinement of$( \mathbb { T } , Y _ { 2 } ) _ { \delta }$, if$\kappa _ { 0 } > 0$is chosen suficiently small (depending on the implicit constant mentioned previously), then$( \mathbb { T } _ { 2 } , Y _ { 3 } ) _ { \delta }$is$\mathrm { a } \approx _ { \delta } 1$refinement of$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$

Furthermore, for each point$\begin{array} { r } { x \in \bigcup _ { T \in \mathbb { T } [ 3 T _ { \rho } ] } Y _ { 3 } ( T ) = \bigcup _ { T \in \mathbb { T } [ T _ { \rho } ] } Y _ { 3 } ( T ) } \end{array}$, we have that the set of unit vectors$\{ \mathrm { d i r } ( T ) \colon T \in \mathbb { T } _ { 2 } [ 3 T _ { \rho } ] = \mathbb { T } _ { 2 } [ T _ { \rho } ] , \stackrel { \cdot \cdot } { x } \in Y _ { 3 } ( T ) \}$is broad inside$B ( \mathrm { d i r } ( T _ { \rho } ) , 2 \rho )$with error$O ( 1 )$ in the sense of Definition 7.6. We conclude that the pair$( \mathbb { T } _ { 2 } , Y _ { 3 } ) _ { \delta }$and$\{ 3 T _ { \rho } , T _ { \rho } \in \mathbb { T } _ { \rho } \}$satisfy the conclusions of Corollary 7.10 (with$3 \rho$in place of$\rho )$.□

The next result says that every pair$( \mathbb { T } , Y ) _ { \delta }$of$\delta$tubes and their associated shading is either broad at some scale$\delta \ll \rho \ll 1$, or else the tubes in$( \mathbb { T } , Y ) _ { \delta }$are almost disjoint.

Lemma 7.11. Let$\delta > 0$and let$( \mathbb { T } , Y ) _ { \delta }$be a pair of δ tubes and their associated shading. Then at least one of the following must occur:

(A)

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim_ {\delta} \delta^ {\omega / 2} \sum_ {T \in \mathbb {T}} | Y (T) |.\tag{7.5}
$$

(B) There is a scale$\rho \in [ \delta ^ { 1 - \omega / 1 0 0 } , \delta ^ { \omega / 1 0 0 } ]$, a${ \approx } _ { \delta }$1 refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } o f \left( \mathbb { T } , Y \right)$, and a balanced partitioning cover$\mathbb { T } _ { \rho } \ o f \mathbb { T } \quad$, so that$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with error$O ( 1 )$relative to the cover$\mathbb { T } _ { \rho } .$

Proof. Let$r = \delta ^ { \omega / 1 0 0 }$. After replacing$( \mathbb { T } , Y ) _ { \delta }$by$\mathrm { ~ a ~ } \sim 1$refinement, we can find a partitioning cover$\mathbb { T } _ { r }$of T. Apply Corollary 7.10 to each set$( \mathbb { T } ^ { T _ { r } } , Y ^ { T _ { r } } ) _ { \delta / r }$. After dyadic pigeonholing$\mathbb { T } _ { r }$and T, we can suppose that the resulting scale, which we will call${ \tilde { \rho } } ,$is the same for each$T _ { r } \in \mathbb { T } _ { r }$ Define$\rho = \tilde { \rho } r$, and let$( \mathbb { T } ^ { \prime } , Y ^ { \prime } )$be the${ \approx } _ { \delta }$1 refinement of$( \mathbb { T } , Y ) _ { \delta }$consisting of the tubes and their associated shadings coming from the conclusion of Corollary 7.10 for each$T _ { r } \in \mathbb { T } _ { r }$.

Recall that the tubes$\mathbb { T } _ { r }$form a partitioning cover of$\mathbb { T } ^ { \prime }$, and for each$T _ { r } \in \mathbb { T } _ { r }$, the (re-scaled)$\rho$ tubes coming from Corollary 7.10 form a partitioning cover of$\mathbb { T } ^ { \prime } [ T _ { r } ]$. We conclude that if we define $\mathbb { T } _ { \rho }$to be the union of these$\rho$tubes, then$\mathbb { T } _ { \rho }$is a partitioning cover of$\mathbb { T } ^ { \prime }$, and furthermore$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$ is broad with error$O ( 1 )$relative to the cover$\mathbb { T } _ { \rho } .$

At this point, we have constructed the pair$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$and$\mathbb { T } _ { \rho } ,$which satisfies all of the requirements for Conclusion (B) of Lemma 7.11 with one exception — we know that$\rho \in [ \delta , \delta ^ { \omega / 1 0 0 } ]$, but we do not know that$\rho \in [ \delta ^ { 1 - \omega / 1 0 0 } , \delta ^ { \omega / 1 0 0 } ]$. Our next task is to show that if$\rho < \delta ^ { 1 - \omega / 1 0 0 }$, then Conclusion (A) holds.

Since the tubes in$\mathbb { T } _ { r }$are essentially distinct,$O ( r ^ { - 2 } )$tubes can pass through a common point. By Conclusion (i) from Corollary 7.10, we have that for each tube$T _ { r }$and each$x \in T _ { r }$we have

$$
\# \{T _ {\rho} \in \mathbb {T} _ {\rho} [ T _ {r} ] \colon x \in \bigcup_ {T \in \mathbb {T} ^ {\prime} [ T _ {\rho} ]} Y ^ {\prime} (T) \} \lesssim_ {\delta} \rho^ {- \beta} \leq \delta^ {- \omega / 1 0 0}.
$$

Recall$\beta = \omega \zeta / 1 0 0$was fixed at the beginning of Section 7.1.

Finally, for each$T _ { \rho } \in \mathbb { T } _ { \rho } ,$at most$( \rho / \delta ) ^ { 2 }$tubes from$\mathbb { T } ^ { \prime } [ T _ { \rho } ]$can pass through a common point and at most$r ^ { - 2 }$distinct$T _ { r } \in \mathbb { T } _ { r }$can pass through a common point. We conclude that

$$
\# \mathbb {T} _ {Y ^ {\prime}} ^ {\prime} (x) \lesssim \delta^ {- \omega / 1 0 0} \left(\frac {\rho}{\delta r}\right) ^ {2} \quad \text { for   each } x \in \mathbb {R} ^ {3}.
$$

In summary, if$\rho < \delta ^ { 1 - \omega / 1 0 0 }$, then Conclusion (A) holds. Otherwise, Conclusion (B) holds.

We conclude this section with two results on the union of broad sets of vectors. The first is a straightforward result saying that a union of broad sets is broad. We omit the proof.

Lemma 7.12. Let$\delta > 0$, let$B \subset S ^ { n - 1 }$be a disk, and let$\mathcal { V } _ { i } , i = 1 , \ldots , N$be sets of unit vectors in B. Suppose that each set$\nu _ { i }$is broad with error K at scales$\ge \delta$inside B. Then the multi-set $\textstyle \bigcup _ { i = 1 } ^ { N } \mathcal { V } _ { i }$is broad with error K at scales$\geq \delta$inside B.

The second result described how broadness combines across scales.

Lemma 7.13. Let$0 < \delta < \rho \leq 1$. Let U be a set of unit vectors in$\mathbb { R } ^ { n }$. For each$u \in \mathcal { U } ,$let $\mathcal { V } _ { u } \subset B ( u , \rho ) \subset S ^ { n - 1 }$be contained in the disk of radius$\rho$centered at u. Suppose that$\mathcal { U }$is broad with error$K _ { 1 }$at scales$\geq \rho ,$and that each set$\nu _ { u }$is broad with error$K _ { 2 }$at scales$\geq \delta$inside$B ( u , \rho )$ Suppose furthermore that each set$\nu _ { u }$has comparable cardinality (up to a factor of 2). Then the multi-set$\textstyle { \bigsqcup _ { u \in { \mathcal { U } } } \mathcal { V } _ { u } }$is broad with error$O ( K _ { 1 } K _ { 2 } )$at$s c a l e s \geq \delta$

Proof. Let$\begin{array} { r } { \mathcal { V } = \bigcup _ { u \in \mathcal { U } } \mathcal { V } _ { u } } \end{array}$. By hypothesis, there is a number$M _ { 1 }$so that$M _ { 1 } \leq \# \mathcal { V } _ { u } \leq 2 M _ { 1 }$for each set$\nu _ { u }$. Let$X = \operatorname* { s u p } _ { u _ { 0 } } \# \{ u \in \mathcal { U } \colon \angle ( u , u _ { 0 } ) \leq \rho \}$, where the supremum is taken over all unit vectors $u _ { 0 } \in S ^ { n - 1 }$. Since$\mathcal { U }$is broad with error$K _ { 1 }$at scales$\geq \rho .$, if we choose a unit vector$u _ { 0 }$achieving the above supremum, then

$$
X \leq \# \{u \in \mathcal {U} \colon \angle (u, u _ {0}) \leq \rho \} \leq K _ {1} \rho^ {\beta} (\# \mathcal {U}),
$$

and thus$\# \mathcal { U } \geq K _ { 1 } ^ { - 1 } \rho ^ { - \beta } X$

First we consider the case where$r \in [ \delta , \rho ]$. For each unit vector$v _ { 0 }$, there are at most$O ( X )$ vectors$u \in \mathcal { U }$for which$\{ v \in \mathcal { V } _ { u } \colon \angle ( v , v _ { 0 } ) \leq r \}$is non-empty. For each such$u ,$we have

$$
\# \{v \in \mathcal {V} _ {u} \colon \angle (v, v _ {0}) \leq r \} \lesssim K _ {2} (r / \rho) ^ {\beta} (2 M _ {1}) \lesssim K _ {1} K _ {2} r ^ {\beta} (\# \mathcal {U}) X ^ {- 1} M _ {1}.
$$

Thus the total contribution from all such u is$\lesssim K _ { 1 } K _ { 2 } r ^ { \beta } ( \# \mathcal { V } )$, as desired.

Next we consider the case where$r \in [ \rho , 1 ]$. Then

$$
\# \{v \in \mathcal {V} \colon \angle (v, v _ {0}) \leq r \} \lesssim 2 M _ {1} (\# \{u \in \mathcal {U} \colon \angle (u, v _ {0}) \leq 2 r \}) \leq M _ {1} K _ {1} r ^ {\beta} (\# \mathcal {U}) = K _ {1} r ^ {\beta} (\# \mathcal {V}).
$$

## 7.2 Broadness and the Frostman Slab Wolf axioms

Given a pair$( \mathbb { T } , Y ) _ { \delta }$, Lemma 7.11 allows us to find a set$\mathbb { T } _ { \rho }$for which the pairs$( \mathbb { T } ^ { T _ { \rho } } , Y ^ { T _ { \rho } } ) _ { \delta / \rho }$are broad. The next result says that under suitable hypotheses,$\mathbb { T } _ { \rho }$will factor T with respect to the Frostman Slab Wolf axioms. The precise statement is as follows.

Lemma 7.14. Suppose that$\mathcal { E } ( \pmb { \sigma } , \omega )$is true, and let$\varepsilon > 0$. Then there exists$\alpha , \eta , \kappa > 0$so that the following holds for all$0 < \delta \le \rho \le 1$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, with$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and $C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Let$\mathbb { T } _ { \rho }$be a balanced cover of T, and suppose$( \mathbb { T } , Y ) _ { \delta }$is broad with error$\delta ^ { - \eta }$ relative to the cover$\mathbb { T } _ { \rho }$. Then at least one of the following must hold.

(A)

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega - \alpha} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.\tag{7.6}
$$

(B) There exists a$\delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$and a set$\mathbb { T } _ { \rho } ^ { \prime } \subset \mathbb { T } _ { \rho } ,$so that$\mathbb { T } _ { \rho } ^ { \prime }$factors$\mathbb { T } ^ { \prime }$above and below with respect to the Frostman Slab Wolf Axioms with error$\delta ^ { - \varepsilon }$

In brief, the proof is as follows. We apply Proposition 4.8 inside each set$\mathbb { T } ^ { T _ { \rho } }$to cover the tubes $\mathbb { T } [ T _ { \rho } ]$by prisms W, with the property that each set$\mathbb { T } ^ { W }$satisfies the Frostman Slab Wolf axioms with small error, and the tubes in$\mathbb { T } [ T _ { \rho } ]$from distinct prisms do not interact (i.e. their shadings are almost disjoint). Each prism$W$is contained inside its corresponding$\rho$tube$T _ { \rho }$. If W is almost as large as$T _ { \rho } ,$then$C _ { F - S W } ( \mathbb { T } ^ { T _ { \rho } } )$must be almost as small as$C _ { F - S W } ( \mathbb { T } ^ { W } )$, which in turn has size about 1. If this happens, then Conclusion (B) holds.

Suppose instead that the prisms are much smaller than$T _ { \rho } ;$we will refer to the dimensions of these prisms as$s \times t \times 1$, with$\delta \leq s \leq t$. Since each prism is contained inside a$\rho$tube, we also have$t \le \rho$. Thus if the prisms are much smaller than the$\rho$tubs, then in particular we must have $s \ll \rho$

Next, we will make use of the assumption that the tubes are broad relative to the cover$\mathbb { T } _ { \rho }$in order to show that$t \sim \rho .$. Since$s \ll \rho .$, this means that the prisms are flat. Specifically, broadness ensures that a typical pair of tubes passing through a common point$x \in \mathsf { U } _ { T \in \mathbb { T } [ T _ { o } ] } Y ( T )$) make angle roughly$\rho .$Such a pair of tubes is contained in a common prism$W$, from which it follows that W must have$\^ { 6 \ell } \mathrm { w i d t h } ^ { \prime \prime } \rho ,$i.e. each prism W has dimensions roughly$s \times \rho \times 1$

To summarize, at this point in the argument each$\delta$tube is contained inside a flat prism$W$ of dimensions roughly$s \times \rho \times 1$with$s \ll \rho$. Furthermore, at a typical point$x \in Y ( T )$, there is at least one other tube from$\mathbb { T }$contained inside the same flat prism$W ,$and this second tube intersects$T$at angle roughly$\rho .$. Thus the hairbrush of$T$(i.e. the union of set of tubes intersecting $T )$, when restricted to the$_ { s } ^ { \varrho } \delta$neighbourhood of$T$, fills out a rectangular slab of dimensions roughly $\delta \times { } _ { s } ^ { \rho } \delta \times { } 1$. But this is precisely the setting where Lemma 5.17 asserts that${ \lvert { J _ { \mathbb { T } } } { Y ( T ) } }$is larger than we would expect from the estimate$\mathcal { E } ( \sigma , \omega )$, and thus Conclusion (A) holds. We now turn to the details.

Proof of Lemma$\ 7 . 1 4 .$

Step 1. We may suppose that$\rho \leq \delta ^ { \varepsilon / 1 0 }$, or else Conclusion (B) follows by selecting a single$\rho \mathrm { - }$tube that contains at least$\rho ^ { 4 } ( \# \mathbb { T } )$tubes from T. We may also suppose that$\rho \ge \delta ^ { \varepsilon / 1 0 }$, or else Conclusion (B) holds trivially by taking$\mathbb { T } ^ { \prime } = \mathbb { T }$and$\mathbb { T } _ { \rho } ^ { \prime } = \mathbb { T } _ { \rho }$

By pigeonholing and replacing$\mathbb { T } _ { \rho }$by a subset$\mathbb { T } _ { \rho , 1 }$, we can find a${ \approx } _ { \delta }$1 refinement$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$of $( \mathbb { T } , Y ) _ { \delta }$so that$\mathbb { T } _ { \rho , 1 }$is a balanced cover of$\mathbb { T } _ { 1 }$, and furthermore each set$( \mathbb { T } _ { 1 } ^ { T _ { \rho } } , Y ^ { \rho } ) _ { \delta / \rho } { \mathrm { ~ i s ~ } } \gtrapprox \delta \mid \delta ^ { \eta } \gtrapprox \rho$ $\rho ^ { 1 0 \eta / \varepsilon }$dense.

Let$\varepsilon _ { 1 } = \varepsilon \beta / 1 6 0 0$. Apply Proposition 4.8 with$\varepsilon _ { 1 }$in place of$\varepsilon$to each set$\mathbb { T } _ { 1 } ^ { T _ { \rho } }$; this gives us a collection of convex sets$\mathcal { W } _ { T _ { \rho } }$that factors a$( \delta / \rho ) ^ { \varepsilon _ { 1 } }$<sup>1</sup>-fraction of$\mathbb { T } _ { 1 } ^ { T _ { \rho } }$(abusing notation, we continue to use$\mathbb { T } _ { 1 } ^ { T _ { \rho } }$to denote this$( \delta / \rho ) ^ { \varepsilon _ { 1 } } \mathrm { - f r a c t i o n ) }$from below with respect to the Frostman Slab Wolf axioms with error$( \delta / \rho ) ^ { - \varepsilon _ { 1 } } \leq \delta ^ { - \varepsilon _ { 1 } }$. We may do this, provided$\eta > 0$is selected suficiently small depending on ε and$\varepsilon _ { 1 }$

After further pigeonholing (which induces a further$\approx _ { \delta }$1 refinement$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$of$( \mathbb { T } _ { 1 } , Y _ { 1 } )$and replaces$\mathbb { T } _ { \rho , 1 }$by a subset$\mathbb { T } _ { \rho , 2 } )$, we may suppose that the convex sets in$\phi _ { T _ { \rho } } ^ { - 1 } ( \mathcal { W } _ { T _ { \rho } } )$all have common dimensions (up to a factor of 2) for each$T _ { \rho } \in \mathbb { T } _ { \rho , 2 } ;$call these dimensions$s \times t \times 1$. We may also suppose that the value of$C _ { F - S W } ( \mathbb { T } _ { 2 } ^ { T _ { \rho } } )$is the same (up to a factor of 2) for all$T _ { \rho } \in \mathbb { T } _ { \rho , 2 }$, and that the mass$\begin{array} { r } { \sum _ { T \in \mathbb { T } [ T _ { \rho } ] } | Y _ { 2 } ( T ) | } \end{array}$is the same (up to a factor of 2) for each$T _ { \rho } \in \mathbb { T } _ { \rho , 2 }$

Let$\begin{array} { r } { \mathcal { W } = \bigcup _ { T _ { \rho } \in \mathbb { T } _ { \rho } } \phi _ { T _ { \rho } } ^ { - 1 } ( \mathcal { W } _ { T _ { \rho } } ) } \end{array}$. To summarize, the situation is as follows:

(i) We have$\begin{array} { r } { \sum _ { T \in \mathbb { T } _ { 2 } \left[ T _ { \rho } \right] } \left| Y _ { 2 } ( T ) \right| \gtrapprox \delta \delta ^ { \varepsilon _ { 1 } } \sum _ { T \in \mathbb { T } \left[ T _ { \rho } \right] } \left| Y ( T ) \right| } \end{array}$for each$T _ { \rho } \in \mathbb { T } _ { \rho , 2 }$

(ii) We have a collection W of convex sets of dimensions$s \times t \times 1$, with$\mathbb { T } _ { 2 } \prec \mathcal { W } \prec \mathbb { T } _ { \rho } .$

(iii) For each$T _ { \rho } \in \mathbb { T } _ { \rho , 2 }$, the sets$\begin{array} { r } { \bigcup _ { \mathbb { T } _ { 2 } [ W ] } Y _ { 2 } ( T ) , W \in \mathcal { W } [ T _ { \rho } ] } \end{array}$are disjoint.

(iv) For each$W \in { \mathcal { W } }$, we have$C _ { F - S W } ( \mathbb { T } _ { 2 } ^ { W } ) \le \delta ^ { - \varepsilon _ { 1 } }$

By Items (ii) and (iv), for each$T _ { \rho } \in \mathbb { T } _ { \rho }$we have

$$
C _ {F - S W} (\mathbb {T} _ {2} ^ {T _ {\rho}}) \leq \Bigl (\sup _ {W \in \mathcal {W} [ T _ {\rho} ]} C _ {F - S W} (\mathbb {T} _ {2} ^ {W}) \Bigr) \Bigl (\frac {| T _ {\rho} |}{| W |} \Bigr) ^ {1 0 0} \leq \delta^ {- \varepsilon / 2} \Bigl (\frac {| T _ {\rho} |}{| W |} \Bigr) ^ {1 0 0}.\tag{7.7}
$$

The last term in the above inequality is an (intentionally) crude estimate for the number of essentially distinct$s \times t \times 1$prisms that can fit inside a ρ-tube.

$\mathrm { I f } \ \left( \frac { | T _ { \rho } | } { | W | } \right) ^ { 1 0 0 } \leq \delta ^ { - \varepsilon / 2 }$, then Conclusion (B) holds with$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } = ( \mathbb { T } _ { 2 } , Y _ { 2 } )$and$\mathbb { T } _ { \rho } = \mathbb { T } _ { \rho , 2 }$and we are done.

## Step 2. We shall suppose henceforth that

$$
| W | \leq \delta^ {\varepsilon / 2 0 0} | T _ {\rho} |.\tag{7.8}
$$

Our goal is to prove the (7.6) holds for an appropriate choice of α.

Each prism in W has dimensions$s \times t \times 1$, with$t \le \rho$. We claim the reverse inequality is almost true. Specifically, we have

$$
t \gtrsim_ {\delta} \delta^ {\frac {2 \varepsilon_ {1}}{\beta}} \rho .\tag{7.9}
$$

Recall from Definition 7.7 that for each$T _ { \rho } \in \mathbb { T } _ { \rho , 2 }$and each$x \in \mathsf { U } _ { T \in \mathbb { T } [ T _ { \rho } ] } Y ( T )$, we have

$$
\# \{T \in \mathbb {T} [ T _ {\rho} ] \colon x \in Y (T),   \angle (v, \mathrm{dir} (T)) \leq r \} \leq \delta^ {- \eta} (\frac {r}{\rho}) ^ {\boldsymbol {\beta}} \# \{T \in \mathbb {T} [ T _ {\rho} ] \colon x \in Y (T) \}, \quad v \in S ^ {2},   r \geq \delta .\tag{7.10}
$$

By Item (i) above, there exists at least one point$\boldsymbol { x } \in \mathbb { R } ^ { 3 }$for which

$$
\# \{T \in \mathbb {T} _ {2} [ T _ {\rho} ] \colon x \in Y _ {2} (T) \} \gtrsim_ {\delta} \delta^ {\varepsilon_ {1}} \# \{T \in \mathbb {T} [ T _ {\rho} ] \colon x \in Y (T) \} > 0,\tag{7.11}
$$

and hence for this choice of x we have

$$
\# \{T \in \mathbb {T} _ {2} [ T _ {\rho} ] \colon x \in Y _ {2} (T),   \angle (v, \mathrm{dir} (T)) \leq r \} \leq \delta^ {- \eta - \varepsilon_ {1}} (\frac {r}{\rho}) ^ {\boldsymbol {\beta}} \# \{T \in \mathbb {T} _ {2} [ T _ {\rho} ] \colon x \in Y _ {2} (T) \}, \quad v \in S ^ {2},   r \geq \delta .\tag{7.12}
$$

On the other hand, by Item (iii) above, the tubes$\{ T \in \mathbb { T } _ { 2 } [ T _ { \rho } ] \colon x \in Y _ { 2 } ( T ) \}$are all contained in a common prism$W \in \mathcal { W }$, and thus must all make angl$\mathrm { ~ e ~ } \leq 2 t$with the direction v of this prism. Selecting$r = 2 t$in (7.12) and comparing with (iii), we obtain (7.9) (provided we select$\eta \leq \varepsilon _ { 1 } )$

Comparing (7.8) and (7.9), we see that the prisms in W must be flat, i.e.

$$
s \sim t ^ {- 1} | W | \lesssim t ^ {- 1} \delta^ {\varepsilon / 2 0 0} \rho^ {2} \lesssim_ {\delta} \delta^ {\frac {\varepsilon}{2 0 0} - \frac {4 \varepsilon_ {1}}{\beta}} t \leq \delta^ {\frac {\varepsilon}{4 0 0}} t.\tag{7.13}
$$

Step 3. Apply Lemma 5.9 to replace each shading$Y _ { 2 } ( T ) , \ T \in \mathbb { T } _ { 2 }$with a regular sub-shading $Y _ { 3 } ( T ) \subset Y _ { 2 } ( T )$. Define$\mathbb { T } _ { 3 } = \mathbb { T } _ { 2 }$. We say a point$x \in \bigcup _ { T \in \mathbb { T } } Y ( T )$has survived if

$$
\# \{T \in \mathbb {T} _ {3} \colon x \in Y _ {3} (T) \} \geq \kappa_ {0} \delta^ {2 \varepsilon_ {1}} \# \{T \in \mathbb {T} \colon x \in Y (T) \}.
$$

Let$Y _ { 4 } ( T ) \subset Y _ { 3 } ( T )$consist of surviving points and let$\mathbb { T } _ { 4 } = \mathbb { T } _ { 3 } ;$we will choose the constant$\kappa _ { 0 }$ suficiently small so that$( \mathbb { T } _ { 4 } , Y _ { 4 } ) _ { \delta }$is$\mathrm { ~ a ~ } \gtrapprox \delta ^ { \varepsilon _ { 1 } }$refinement of$( \mathbb { T } _ { 3 } , Y _ { 3 } )$

Observe that if the point x has survived, then there is a unique prism$W \in \mathcal { W }$with$x \in$ $\cup _ { T \in \mathbb { T } _ { 3 } [ W ] } Y ( T )$, and at least two tubes T,$T ^ { \prime } \in \mathbb { T } _ { 3 } [ W ]$with$x \in Y _ { 3 } ( T ) , x \in Y _ { 3 } ( T ^ { \prime } )$with${ \mathcal { L } } ( \mathrm { d i r } ( T ) , \mathrm { d i r } ( T ^ { \prime } ) ) \gtrapprox \delta$ 2ε $\delta ^ { \frac { \omega _ { - 1 } } { \beta } } \rho .$

For each$T \in \mathbb { T } _ { 4 }$, let$S ( T ) \supset T$be the$\textstyle { \delta \times { \frac { t } { s } } \delta \times 1 }$prism with coaxial line$T ,$and plane parallel to $\Pi ( W )$, where$W \in { \mathcal { W } }$is the unique prism covering$T .$. Recall that by (7.13), we have$\begin{array} { r } { \frac { t } { s } \delta \geq \delta ^ { 1 } } \end{array}$<sup>−</sup> <sup>ε</sup>400 . A Cordoba style$L ^ { 2 }$argument (see i.e. Lemma 5.7 and its proof for an example of a similar argument) shows that for each$T \in \mathbb { T } _ { 4 }$

$$
\left| S (T) \cap \bigcup_ {T \in \mathbb {T} _ {3}} Y _ {3} (T) \right| \gtrsim_ {\delta} \delta^ {4 \varepsilon_ {1}} \frac {| Y _ {4} (T) |}{| T |} | S |.
$$

Let$\begin{array} { r } { b = \frac { t } { s } \delta \geq \delta ^ { 1 - \varepsilon / 4 0 0 } } \end{array}$. Applying Lemma 5.17, we obtain Conclusion$\mathrm { ( A ) }$for$\alpha = \varepsilon \omega / 5 0 0$, provided we select$\eta > 0$suficiently small.□

## 7.3 The iteration base case: Guth’s grains decomposition

In our proof sketch from Section 2.2, we described a single-scale grains decomposition due to Guth. In this section we will state the result precisely.

Proposition 7.15. Let$\varepsilon > 0$. Then there exists$\eta , \kappa > 0$so that the following holds for all$\delta > 0$ Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense and be broad with error$\delta ^ { - \eta }$. Suppose that the tubes in$\mathbb { T }$are contained in a common 1 tube$T _ { 1 }$

Then there is a$\delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } )$that is$\delta ^ { \varepsilon }$dense and is broad with error$\le \kappa ^ { - 1 } \delta ^ { - \varepsilon }$, and a number$\mu \geq 1$so that$\mu \sim \# \mathbb { T } _ { Y ^ { \prime } } ^ { \prime } ( x )$for each$x \in \bigcup _ { \mathbb { T } ^ { \prime } } Y ^ { \prime } ( T )$. In addition, there is a number $c \ge \kappa \mu \delta ^ { \varepsilon } ( \delta \# \mathbb { T } ) ^ { - 1 }$; and a pair$( \mathcal { G } , Y ) _ { \delta \times c \times c } ,$so that$( \mathcal { G } , Y ) _ { \delta \times c \times c }$is a robustly δ<sup>ε</sup>-dense two-scale grains decomposition of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$wrt$\{ T _ { 1 } \}$(the latter is a set consisting of a single 1 tube).

Remark 7.16. Proposition 7.15 says that$( \mathcal { G } , Y ) _ { \delta \times c \times c }$is a two-scale grains decomposition of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$ wrt$\{ T _ { 1 } \}$. A two-scale grains decomposition is defined in Definition 7.1, and Item$( \mathrm { i v } )$from that definition specifies that if$Y ^ { \prime } ( T ) \cap Y ( G ) \neq \emptyset$, then T exits$G$through its long ends, in the sense of Figure 9. Since the grains$( \mathcal { G } , Y ) _ { \delta \times c \times c }$from Proposition 7.15 are square, the definition is somewhat ambiguous in this setting. However, Proposition 7.15 is only used to prove Corollary 7.17. Thus the 1 tube$T _ { 1 }$should be thought of as the anisotropic rescaling of a$\rho$tube$T _ { \rho }$. What is needed is the following: the images of the tubes in$\mathbb { T } ^ { \prime }$under the anisotropic scaling sending$T _ { 1 }$to$T _ { \rho }$must exit the images of the grains in$\mathcal { G }$through their long ends.

Proposition 7.15 is a variant of Guth’s grains decomposition from [9]. Since this precise statement does not appear in [9] (the hypotheses in [9] are stated slightly diferently), we will provide a proof in Appendix A.

If$( \mathbb { T } , Y ) _ { \delta }$is broad relative to a set of$\rho$tubes$\mathbb { T } _ { \rho }$, then we can apply Proposition 7.15 to each re-scaled set$( \mathbb { T } ^ { T _ { \rho } } , Y ^ { T _ { \rho } } ) _ { \delta }$

Corollary 7.17. Let$\varepsilon > 0$. Then there exists$\kappa , \eta > 0$so that the following holds for all$\delta > 0$ Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense and let$\mathbb { T } _ { \rho }$be a balanced partitioning cover of T. Suppose that$( \mathbb { T } , Y ) _ { \delta }$is broad with error$\delta ^ { - \eta }$relative to the cover$\mathbb { T } _ { \rho . }$, and that$| \bigcup _ { T \in \mathbb { T } } Y ( T ) | \leq \delta ^ { \varepsilon } ( \# \mathbb { T } ) | T |$

Then there is a$\delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ~ o f \left( \mathbb { T } , Y \right) _ { \delta }$that is$\delta ^ { \varepsilon }$dense; a subset$\mathbb { T } _ { \rho } ^ { \prime } \subset \mathbb { T } _ { \rho } ;$a number $c \gtrsim \frac { \rho } { \delta } \frac { \# \mathbb { T } _ { \rho } } { \# \mathbb { T } }$; and a pair$( \mathcal { P } , Y ) _ { \delta \times b \times c }$with$\rho = b / c$that is a robustly$\delta ^ { \varepsilon } .$-dense two-scale grains decomposition$o f \left( \mathbb { T } ^ { \prime } , Y ^ { \prime } \right) _ { \delta }$wrt$\mathbb { T } _ { \rho } ^ { \prime }$. Finally,$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with error$\le \kappa ^ { - 1 } \delta ^ { - \varepsilon }$relative to the cover $\mathbb { T } _ { \rho } ^ { \prime } .$

Note that the estimate on the size of c in Corollary 7.17 omits the term$\mu$(though this term is used to compensate for the$\delta ^ { \varepsilon }$loss in Proposition 7.15); this is because the weaker estimate $c \gtrsim \frac { \rho } { \delta } \frac { \# \mathbb { T } _ { \rho } } { \# \mathbb { T } }$will be suficient in the arguments that follow.

Corollary 7.17 has two important consequences. First, when combined with Lemma 7.11, it says that if$( \mathbb { T } , Y ) _ { \delta }$is an arrangement for which$\mathcal { E } ( \pmb { \sigma } , \omega )$is tight, then$( \mathbb { T } , Y ) _ { \delta }$admits a two-scale grains decomposition. In Section 2.2, we called this the “Guth grains decomposition” of T. The precise statement is as follows

Lemma 7.18. Suppose that$\mathcal { E } ( \pmb { \sigma } , \omega )$is true and let$\varepsilon > 0$. Then there exists$\alpha , \eta , \kappa > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, with$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$ Then at least one of the following must hold.

(A)

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\boldsymbol {\omega} - \alpha} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \boldsymbol {\sigma}}.\tag{7.14}
$$

(C) There exist the following:

– A scale$\rho \in [ \delta ^ { 1 - \omega / 1 0 0 } , \delta ^ { \omega / 1 0 0 } ]$

– A$\delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ~ o f \left( \mathbb { T } , Y \right) _ { \delta }$

$A$balanced partitioning cover$\mathbb { T } _ { \rho } \ o f \ \mathbb { T } ^ { \prime }$

– Numbers$\delta \leq b \leq c$with$b / c = \rho$and$c \gtrsim \frac { \rho } { \delta } \frac { \# \mathbb { T } _ { \rho } } { \# \mathbb { T } }$

– A pair$( \mathcal { P } , Y ) _ { \delta \times b \times c }$

So that the following holds:

(i)$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with error$\leq \delta ^ { - \varepsilon }$relative to the cover$\mathbb { T } _ { \rho } .$

(ii)$( \mathcal { P } , Y ) _ { \delta \times b \times c }$is a robustly δ<sup>ε</sup>-dense two-scale grains decomposition of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$wrt$\mathbb { T } _ { \rho } .$

Remark 7.19. Note that the Conclusions of Lemma 7.18 are labelled (A) and (C), rather than (A) and (B). We chose this convention in order to have parallelism with Conclusions (A), (B), and (C) of Moves #1, #2, and #3 below.

Lemma 7.18 will serve as the starting point for the iterative process described in Section 2.2. In the following subsections, we will describe the three Moves in this iterative process.

## 7.4 Moves #1, #2, #3: Parallel structure

In the following sections, we will describe three Moves, which we will iteratively apply to the two scale grains decomposition that we obtained from Lemma 7.18. Each of these Moves are expressed as a lemma, and these three lemmas have similar structure. In particular, the three lemmas have the same hypotheses, and have similar conclusions.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Common setup for Moves #1, #2, #3: Hypotheses
Suppose that  $\mathcal{E}(\sigma,\omega)$  is true and let  $\varepsilon\in(0,\zeta/2]$ . Then there exists  $\alpha,\eta,\kappa&gt;0$  so that the following holds for all  $0&lt;\delta\leq1$ ,  $\rho\geq\delta^{1-\omega/100}$ , and all  $\delta\leq a\leq b\leq c$  with b/c= $\rho$ .
Let  $(\mathbb{T},Y)_{\delta}$  be  $\delta^{\eta}$  dense, with  $C_{KT-CW}(\mathbb{T})\leq\delta^{-\eta}$  and  $C_{F-SW}(\mathbb{T})\leq\delta^{-\eta}$ . Let  $T_{\rho}$  be a balanced partitioning cover of T, and suppose that  $(\mathbb{T},Y)_{\delta}$  is broad with error  $\delta^{-\eta}$  relative to  $T_{\rho}$ . Let  $(\mathcal{P},Y)_{a\times b\times c}$  be a robustly  $\delta^{\eta}$ -dense two-scale grains decomposition of  $(\mathbb{T},Y)_{\delta}$  wrt  $T_{\rho}$ .
</div>

Each of Moves$\# 1 , \# 2 .$, and$\# 3$will have three possible conclusions, which we label (A), (B), and (C). Conclusion (A) is the same for all three moves.

Common setup for Moves$\# 1$, #2, #3: Conclusion$( \mathbf { A } )$.

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\boldsymbol {\omega} - \alpha} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \boldsymbol {\sigma}}.\tag{7.15}
$$

In Inequality (7.15),$\kappa , \alpha > 0$are the quantities from the Common setup for Moves #1, #2, #3: Hypotheses described above.

Conclusion (B) is not identical for the three Moves, but shares many common elements. We describe these below

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Common setup for Moves #1, #2, #3: Conclusion (B).
There are  $\delta^{\varepsilon}$  refinements  $(\mathbb{T}^{\prime}, Y^{\prime})_{\delta}$  and  $(\mathcal{P}^{\prime}, Y^{\prime})_{a\times b\times c}$  of  $(\mathbb{T}, Y)_{\delta}$  and  $(\mathcal{P}, Y)_{a\times b\times c}$ , respectively, and a set  $T_{\rho}^{\prime} \subset T_{\rho}$ , so that the following holds.
(i)  $(\mathbb{T}^{\prime}, Y^{\prime})_{\delta}$  is  $\delta^{\varepsilon}$  dense,  $C_{KT-CW}(\mathbb{T}^{\prime}) \leq \delta^{-\varepsilon}$ , and  $C_{F-SW}(\mathbb{T}^{\prime}) \leq \delta^{-\varepsilon}$ .
(ii)  $T_{\rho}^{\prime}$  is a balanced partitioning cover of  $T'$ , and  $(\mathbb{T}', Y')_{\delta}$  is broad with error  $\delta^{-\varepsilon}$  relative to  $T_{\rho}'$ .
(iii)  $(\mathcal{P}^{\prime}, Y^{\prime})_{a\times b\times c}$  is a robustly  $\delta^{\varepsilon}$ -dense two-scale grains decomposition of  $(\mathbb{T}', Y')_{\delta}$  wrt  $T_{\rho}'$ .
(iv) Moves #1, #2, #3 will have additional conclusions specific to that Move.
</div>

Conclusion (C) is not identical for the three Moves, but shares many common elements. We describe these below

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Common setup for Moves #1, #2, #3: Conclusion (C).
There exist the following:
- Numbers $\tilde{\rho}$ and $\tilde{a} \leq \tilde{b} \leq \tilde{c} \leq 1$, with $\tilde{\rho} = \tilde{b}/\tilde{c}$.
- A $\delta^{\varepsilon}$ refinement $(\mathbb{T}', Y')_{\delta}$ of $(\mathbb{T}, Y)_{\delta}$.
- A set $\mathbb{T}_{\tilde{\rho}}$ of $\tilde{\rho}$ tubes.
- A pair $(\tilde{\mathcal{P}}, \tilde{Y})_{\tilde{a} \times \tilde{b} \times \tilde{c}}$.
These objects have the following properties:
(i) $(\mathbb{T}', Y')_{\delta}$ is $\delta^{\varepsilon}$ dense, $C_{KT-CW}(\mathbb{T}') \leq \delta^{-\varepsilon}$, and $C_{F-SW}(\mathbb{T}') \leq \delta^{-\varepsilon}$.
(ii) $\mathbb{T}_{\tilde{\rho}}$ is a balanced partitioning cover of $\mathbb{T}'$, and $(\mathbb{T}', Y')_{\delta}$ is broad with error $\delta^{-\varepsilon}$ relative to $\mathbb{T}_{\tilde{\rho}}$.
(iii) $(\tilde{\mathcal{P}}, \tilde{Y})_{\tilde{a} \times \tilde{b} \times \tilde{c}}$ is a robustly $\delta^{\varepsilon}$-dense two-scale grains decomposition of $(\mathbb{T}', Y')_{\delta}$ wrt $\mathbb{T}_{\tilde{\rho}}$.
(iv) $\delta^{1-\omega/100} \leq \tilde{\rho} \leq 1$.
(v) Moves #1, #2, #3 will have additional conclusions specific to that Move.
</div>

Remark 7.20. Observe that Items (i), (ii), and (iii) of Conclusion (B) (resp. Items$\mathrm { ( i ) ~ - ~ ( i v ) }$of Conclusion (C)) say that the output$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ; \mathbb { T } _ { \rho } ^ { \prime } ;$and$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { \delta \times b \times c }$(resp.$\mathbb { T } _ { \widetilde { \rho } }$and$( \tilde { \mathcal { P } } , \tilde { Y } ) _ { \tilde { a } \times \tilde { b } \times \tilde { c } } )$of Moves #1, #2, and$\# 3$match the “input” hypotheses$( \mathrm { i . e . }$the Common setup for Moves$\# 1$ #2, #3: Hypotheses), except that exponent$\eta$has been weakened to ε. This will allow us to iteratively apply these Moves many times.

## 7.5 Using Moves #1, #2, #3 to prove Proposition 7.5

We will state and prove Moves #1, #2, and #3 in Section 8. However, by using the parallel structure described above we can already state the hypotheses and conclusions of these three moves. We do so in the table below.

| Move | Lemma | Conclusion (B), Item (iv) | Conclusion (C), Item (v) |
| --- | --- | --- | --- |
| #1 | 8.1 | $c \geq \delta^{\zeta}(\rho/\delta) (\#\mathbb{T}_{\rho}/\#\mathbb{T}_{\delta})$ | $\tilde{c} \geq \delta^{-\zeta}c, \tilde{a} = \delta, \text{ and } \tilde{\rho} = \rho$ |
| #2 | 8.2 | $\rho \leq \delta^{\omega/100}$ | $\tilde{c} \geq \delta^{-\omega/100}c$ |
| #3 | 8.3 | $C_{KT-CW}^{\text{loc}}(\mathcal{P}') \leq \delta^{-\zeta}$ | $\tilde{\rho} \geq \delta^{-\zeta/1000} \rho \text{ and } \tilde{c} \geq c$ |

We will now match the Conclusions of Proposition 7.5 to their counterparts from Moves$\# 1$ #2, #3.

• Conclusion (A) for Moves #1, #2, #3 matches Conclusion (A) of Proposition 7.5.

• Conclusion (B), Items (i) and (iii) for Moves #1, #2, #3 matches Conclusion (B), Items (i) and (iii), respectively, of Proposition 7.5.

• Conclusion (B), Item (ii) for Moves #1, #2, #3, plus Lemma 7.14 either yields Conclusion (A), or Conclusion (B), Item (ii) of Proposition 7.5.

• Conclusion (B), Item (iv) for Move$\# 1$matches Conclusion (B), Item (iv) of Proposition 7.5.

• Conclusion (B), Item (iv) for Move$\# 2$plus the hypothesis$\rho \geq \delta ^ { 1 - \omega / 1 0 0 }$, matches Conclusion (B), Item (v) of Proposition 7.5.

• Conclusion (B), Item (v) for Move$\# 3$matches Conclusion (B), Item (vi) of Proposition 7.5.

Proof of Proposition 7.5. We proceed as follows. Let$\eta _ { 0 } < \eta _ { 1 } < . . . < \eta _ { N }$be a sequence of numbers that we will determine below. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta _ { 0 } }$dense, with$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta _ { 0 } }$and$C _ { F - S W } ( \mathbb { T } ) \leq$ $\delta ^ { - \eta _ { 0 } }$. If$\eta _ { 0 }$is suficiently small depending on$\eta _ { 1 }$, then we can apply the iteration base case, Lemma 7.18, with$\eta _ { 1 }$in place of ε. If Conclusion (A) of Lemma 7.18 holds, then Conclusion (A) of Proposition 7.5 holds, and we are done.

Suppose instead that Conclusion (B) of Lemma 7.18 holds. The output of Conclusion (B) is pre-cisely the set of objects required for the Common setup for Moves #1, #2, #3: Hypotheses, with$\eta _ { 1 }$in place of$\eta .$

We now repeatedly apply Moves$\# 1$, #2, #3, with$\eta _ { j + 1 }$in place of ε at stage j. We may do so, provided$\eta _ { j }$is suficiently small compared to$\eta _ { j + 1 }$

• If Conclusion (A) occurs at any point, then Conclusion (A) of Proposition 7.5 holds, and we halt.

• If Conclusion (B) occurs for Move # i, for some$i = { 1 , 2 , 3 }$, then we switch to a diferent move.

• If Conclusion (B) occurs for all three moves in succession, then Items (i), (iii), and (iv) of Conclusion (B) of Proposition 7.5 hold. We halt and apply Lemma 7.14 to show either Conclusion (B), Item (ii) holds, or else Conclusion (A) holds. We conclude that at least one of Conclusion (A) or Conclusion (B) of Proposition 7.5 holds.

• If Conclusion (C) occurs for Move$\# \mathrm { i } .$, then at least one of the following must occur:

– c does not decrease, and$\rho$becomes larger by$\delta ^ { - \zeta / 1 0 0 0 }$; this can occur at most 1000/ζ times in a row.

– c becomes larger by min$\{ \delta ^ { - \zeta } , \delta ^ { - \omega / 1 0 0 } \}$. This can occur at most$1 / \zeta + 1 0 0 / \omega$times total.

In particular, the iterative process described above must halt after at most$\begin{array} { r } { N = \frac { 1 0 0 0 } { \zeta } \big ( \frac { 2 } { \zeta } + \frac { 1 0 0 } { \omega } \big ) } \end{array}$ steps. We will choose$\eta _ { N + 1 }$below, and then select each of$\eta _ { N } , \eta _ { N - 1 } , . . . , \eta _ { 0 }$in turn. Finally, we define η (the quantity from Proposition 7.5 ) by$\eta = \eta _ { 0 }$

The refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$, the set$\mathbb { T } _ { \rho } .$, and the pair$( \mathcal { G } , Y ) _ { a \times b \times c }$satisfy all of the conclusions of Proposition 7.5, Conclusion (B), except that for Item (ii), we have not yet shown that$\mathbb { T } _ { \rho }$factors $\mathbb { T } ^ { \prime }$from below with respect to the Frostman Slab Wolf Axioms with error${ \delta } ^ { - \zeta }$. However, since $( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with respect to$\mathbb { T } _ { \rho } ,$, we can apply Lemma 7.14 and conclude that either either this is indeed the case (after replacing$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } , \mathbb { T } _ { \rho } .$, and$( \mathcal { G } , Y ) _ { a \times b \times c }$by a suitable refinement), or else Conclusion (A) of Proposition 7.5 holds.

This completes the proof of Proposition 7.5, except that we have not proved Moves$\# 1 , \# 2 .$ $\# 3$. We shall do so in the next section.□

## 8 Moves #1, #2, and$\# 3$

8.1 Move #1: Replacing grains with longer grains to ensure$c \ge \delta ^ { \zeta } \frac { \rho } { \delta } ( \# \mathbb { T } _ { \rho } ) / ( \# \mathbb { T } )$ Our goal in this section is to state and prove Move$\# 1$, as described in Section 2.2 and Section 7.4. Lemma 8.1. We assume the Common setup for Moves #1, #2, #3: Hypotheses from Section 7.4. Then at least one of the following must hold.

(A) Conclusion (A) of the common setup for Moves$\# 1 , \# 2 , \# 3 .$

(B) Conclusion (B) of the common setup for Moves$\# 1 , \# 2 , \# 3 .$In addition,

$$
c \geq \delta^ {\zeta} \frac {\rho}{\delta} \frac {\# \mathbb {T} _ {\rho}}{\# \mathbb {T} _ {\delta}}.\tag{8.1}
$$

(C) Conclusion (C) of the common setup for Moves$\# 1 , \# 2 , \# 3$. In addition,

(v) a˜ = δ, ρ˜ = ρ, and$\tilde { c } \geq \delta ^ { - \zeta } c$

Proof. If Conclusion (B) fails, then we discard the cover$( { \mathcal { P } } , Y ) _ { a \times b \times c }$and replace it with the cover coming from Corollary 7.17 applied to$( \mathbb { T } , Y ) _ { \delta }$and$\mathbb { T } _ { \rho } .$Conclusion (C) of Lemma 8.1 was chosen to match the output of Corollary 7.17. Note that the prisms coming from Corollary 7.17 have length $\begin{array} { r } { \tilde { c } \ge \frac { \rho } { \delta } \frac { \# \mathbb { T } _ { \rho } } { \# \mathbb { T } } } \end{array}$. If Conclusion (B) fails, then this quantity$\mathrm { i s } \geq \delta ^ { - \zeta } c ,$as claimed.□

## 8.2 Move #2: Replacing square grains with longer grains

In this section we will use geometric arguments in the spirit of Cordoba’s proof of the Kakeya maximal function conjecture in$\mathbb { R } ^ { 2 }$to show the following: if$( \mathbb { T } , Y ) _ { \delta }$has a two-scale grains decomposition consisting of square grains, i.e. grains of dimensions$a \times b \times c$with$\rho = b / c > \delta ^ { \omega / 1 0 0 }$, then either$\cup Y ( T )$is large, or else we can construct a new two-scale grains decomposition of$( \mathbb { T } , Y )$ with significantly longer grains. The precise statement is as follows.

Lemma 8.2. We assume the Common setup for Moves #1, #2, #3: Hypotheses from Section 7.4. Then at least one of the following must hold.

(A) Conclusion (A) of the common setup for Moves$\# 1 , \# 2 , \# 3 .$

(B) Conclusion (B) of the common setup for Moves$\# 1 , \# 2 , \# 3 .$In addition,

(iv)$\rho \leq \delta ^ { \omega / 1 0 0 }$

(C) Conclusion (C) of the common setup for Moves$\# 1 , \# 2 , \# 3 .$In addition,

(v)$\tilde { c } \geq \delta ^ { - \omega / 1 0 0 } c .$

Step 1. Let$0 < \varepsilon _ { 1 } < \varepsilon _ { 2 }$be small quantities to be chosen below. We will choose$\varepsilon _ { 1 }$very small compared to$\varepsilon _ { 2 } ;$we will choose$\varepsilon _ { 2 }$very small compared to$\varepsilon ;$we will choose α, η very small compared to$\varepsilon _ { 1 }$

First, we claim that either

$$
a \leq \delta^ {1 - \varepsilon_ {1}},\tag{8.2}
$$

or else Conclusion$\mathrm { ( A ) }$immediately holds, provided we choose α and η suficiently small depending on$\varepsilon _ { 1 }$

We verify this claim as follows. Suppose that (8.2) fails. Then after replacing$( \mathbb { T } , Y ) _ { \delta }$by an $\approx _ { \delta }$1 refinement, we have that for each$x \in \bigcup _ { T \in \mathbb { T } } Y ( T )$

$$
\left| B (x, \delta^ {1 - \varepsilon_ {1}}) \cap \bigcup_ {T \in \mathbb {T}} Y (T) \right| \gtrsim \delta^ {\eta} | B (x, \delta^ {1 - \varepsilon_ {1}}) |.
$$

But from this it follows (see Corollary 5.19) that Conclusion (A) holds, provided we select$\alpha \leq \omega \varepsilon _ { 1 } / 2$ and$\eta > 0$suficiently small. Henceforth we shall suppose that (8.2) holds.

Step 2. We will regularize the set T. By dyadic pigeonholing and replacing$( \mathbb { T } , Y ) _ { \delta }$by$\mathrm { ~ a ~ } \gtrsim$ $( \log 1 / \delta ) ^ { - 1 / \varepsilon _ { 1 } }$refinement$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$, we can suppose that

(i) For each scale of the form$\tau _ { i } = \delta ^ { \varepsilon _ { 1 } i } , i = 1 , \dots , \varepsilon _ { 1 } ^ { - 1 }$, there exists a balanced partitioning cover$\mathbb { T } _ { \tau _ { i } }$of$\mathbb { T } .$, and a number$\mu _ { i }$so that$\# ( \mathbb { T } _ { 1 } [ T _ { \tau _ { i } } ] ) _ { Y _ { 1 } } ( x ) \sim \mu _ { i }$for each$T _ { \tau _ { i } } \in \mathbb { T } _ { \tau _ { i } }$and each $x \in \bigcup _ { T \in \mathbb { T } _ { 1 } [ T _ { \tau _ { i } } ] } Y _ { 1 } ( T )$

(ii) There exists a number$\mu _ { \mathrm { f i n e } }$so that for each$T _ { \rho } \in \mathbb { T } _ { \rho }$and each$x \in \bigcup _ { T \in \mathbb { T } _ { 1 } [ T _ { \rho } ] } Y _ { 1 } ( T )$, we have $\# ( \mathbb { T } _ { 1 } [ T _ { \rho } ] _ { Y _ { 1 } } ) ( x ) \sim \mu _ { \mathrm { f i n e } }$

(iii) For each$T _ { \rho } \in \mathbb { T } _ { \rho }$and each$x \in \bigcup _ { T \in \mathbb { T } _ { 1 } [ T _ { \rho } ] } Y _ { 1 } ( T )$, we have

$$
\left(\# \mathbb {T} _ {1} \left[ T _ {\rho} \right]\right) _ {Y _ {1}} (x) \gtrsim (\log 1 / \delta) ^ {- 1 / \varepsilon_ {1}} \left(\# \mathbb {T} \left[ T _ {\rho} \right] _ {Y} (x)\right).
$$

Item (iii) implies that$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$is broad with error${ \lessapprox } \delta ^ { - \eta }$relative to$\mathbb { T } _ { \rho } .$

Since the tubes in$\mathbb { T } _ { \rho }$are essentially distinct, at most$O ( \rho ^ { - 2 } )$tubes from$\mathbb { T } _ { \rho }$can pass through a common point. We conclude that either Conclusion (B) holds, or

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \mu_ {\mathrm{fine}} ^ {- 1} \rho^ {2} \sum_ {T \in \mathbb {T}} | Y _ {1} (T) | \geq \delta^ {\frac {\omega}{5 0} + \eta} \mu_ {\mathrm{fine}} ^ {- 1} (\# \mathbb {T}) | T |.
$$

If$\mu _ { \mathrm { f i n e } }$is small, then Conclusion (A) holds. More precisely, if Conclusion (A) fails then

$$
\mu_ {\text { fine }} \geq \delta^ {- \boldsymbol {\omega} + \frac {\boldsymbol {\omega}}{5 0} + 2 \eta + \alpha} \left((\# \mathbb {T}) | T | ^ {1 / 2}\right) ^ {\boldsymbol {\sigma}} \geq \delta^ {- \frac {2 4}{2 5} \boldsymbol {\omega}},\tag{8.3}
$$

where for the final inequality we used the fact that$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$to conclude that$( \# \mathbb { T } ) | T | ^ { 1 / 2 } \geq$ $\delta ^ { \eta }$. Henceforth we shall suppose that (8.3) is true.

Step 3. Let$\tilde { c } = { \delta } ^ { - \omega / 1 0 0 } c ;$a bit later in the argument we will abuse notation and replace ˜c by a number of the form$K \delta ^ { - \omega / 1 0 0 } c$for$1 \leq K \lesssim 1$. We will describe a procedure that finds a prism$\tilde { P }$of dimensions$a \times \tilde { \rho } \tilde { c } \times \tilde { c } ,$for some$\tilde { \rho } = \tilde { \rho } ( \tilde { P } ) \in [ \delta ^ { 1 - \omega / 1 0 0 } , \delta ^ { \omega / 1 0 0 } ]$, that satisfies some of the properties from Conclusion (C). This procedure is illustrated in Figure 10. In Step 4, we will iterate this procedure multiple times.

Recall that$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$is${ \gtrap{ \approx } } \delta { \begin{array} { r } { \delta ^ { \eta } } \\ { \approx } \end{array} }$dense. This means that for a typical tube and a typical point $x \in Y _ { 1 } ( T )$, we expect$| B ( x , \tilde { c } ) \cap Y _ { 1 } ( T ) |$to have size$\gtrsim _ { \delta } \delta ^ { \eta } \tilde { c } \delta ^ { 2 }$. This should also hold for any (reasonably dense) sub-shading$Y ^ { \prime } ( T ) \subset Y _ { 1 } ( T )$. The next definition makes this heuristic precise: Given a shading$Y ^ { \prime } ( T ) \subset T$, we define$Y _ { \mathrm { r e g } } ^ { \prime } ( T ) \subset Y ^ { \prime } ( T )$to consist of those points$x \in Y ( T )$for which

![](images/page_75_image_0.jpg)

![](images/page_75_image_1.jpg)

Figure 10: Finding a prism$\tilde { P }$

$$
| B (x, \tilde {c}) \cap Y ^ {\prime} (T) | \geq \frac {1}{1 0 0} \delta^ {2 \eta} \tilde {c} \delta^ {2},\tag{8.4}
$$

i.e.$Y _ { \mathrm { r e g } } ^ { \prime }$consists of those points where$Y ^ { \prime } ( T )$has at density at least$\delta ^ { 2 \eta } / 1 0 0$at scale${ \tilde { c } } .$Observe that if$( \mathbb { T } _ { 1 } , Y ^ { \prime } ) _ { \delta }$$\delta ^ { 2 \eta }$dense, then$( \mathbb { T } , Y _ { \mathrm { r e g } } ^ { \prime } )$is$\mathrm { a } \sim 1$refinement of$( \mathbb { T } _ { 1 } , Y ^ { \prime } )$

With the above definition, we proceed as follows. Let$( \mathbb { T } _ { 1 } , Y ^ { \prime } ) _ { \delta }$be any refinement of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$ that satisfies$\begin{array} { r } { \sum \left| Y ^ { \prime } ( T ) \right| \ge \frac { 1 } { 2 } \sum \left| Y _ { 1 } ( T ) \right| } \end{array}$(so in particular,$( \mathbb { T } _ { 1 } , Y ^ { \prime } ) _ { \delta }$is${ \gtrap{ \approx } } \delta ^ { \ n }$dense).

We claim that we can select a$\rho$tube$T _ { \rho } ;$; a$\delta$tube$T _ { \mathrm { s t e m } } \in \mathbb { T } _ { 1 } [ T _ { \rho } ]$; a prism$P \in \mathcal { P } _ { T _ { \rho } }$(recall Definition 7.1, Item (i)) and a number$\kappa \sim 1$so that the set

$$
E = \{x \in Y ^ {\prime} (T _ {\mathrm{stem}}) \cap Y (P) \colon \# \mathbb {T} _ {1} [ T _ {\rho} ] _ {Y _ {\mathrm{reg}} ^ {\prime}} (x) \geq \kappa \mu_ {\mathrm{fine}} \}\tag{8.5}
$$

satisfies

$$
| E | \gtrsim \delta^ {2 \eta} c \delta^ {2}.\tag{8.6}
$$

To verify this claim, let us temporarily define the refinement$( \mathbb { T } _ { 1 } , Y ^ { \prime \prime } ) _ { \delta }$given by

$$
Y ^ {\prime \prime} (T) = Y ^ {\prime} (T) \cap \{x \colon \# \mathbb {T} _ {1} [ T _ {\rho} ] _ {Y _ {\mathrm{reg}} ^ {\prime}} (x) \geq \kappa \mu_ {\mathrm{fine}} \},
$$

where$T _ { \rho }$is the unique$\rho$tube from$\mathbb { T } _ { \rho }$containing$T _ { \mathrm { s t e m } }$. If$\kappa \sim 1$is chosen suficiently small, then $( \mathbb { T } _ { 1 } , Y ^ { \prime \prime } ) _ { \delta }$is a$1 / 2$refinement of$( \mathbb { T } _ { 1 } , Y ^ { \prime } ) _ { \delta }$. By pigeonholing we can select a tube$T _ { \mathrm { s t e m } }$and a point$x \in$ $T _ { \mathrm { s t e m } }$so that the two adjacent tube segments$T _ { \mathrm { s e g } } ^ { ( 1 ) } , T _ { \mathrm { s e g } } ^ { ( 2 ) }$of length$c / 1 0$whose intersection contains x (see Figure 11, Left) satisfy$| Y ^ { \prime \prime } ( T _ { \mathrm { s t e m } } ) \cap T _ { \mathrm { s e g } } ^ { ( i ) } | \gtrsim \delta ^ { 2 \eta } c \delta ^ { 2 } , i = 1 , 2$. Next, select a prism$P \in \mathcal { P } _ { T _ { \rho } }$with $x \in Y ( P )$(by Definition 7.1, Item (ii), such$P$is unique); by Definition 7.1, Item (iv), at least one of the segments$T _ { \mathrm { s e g } } ^ { ( i ) }$must be almost contained in$P ,$in the sense that$T _ { \mathrm { s e g } } ^ { ( i ) } \backslash N _ { \delta } ( x ) \subset P$(see Figure

![](images/page_76_image_0.jpg)

Figure 11: Left: The two tube segments on either side of the point x. Both tube segments have rich shadings.

Right: Since$x \in P$and$T _ { \mathrm { s t e m } }$exits P through its “long ends,” at least one of the tube segments must be almost contained in$P ,$, in the sense that$T _ { \mathrm { s e g } } ^ { ( i ) } \backslash N _ { \delta } ( x ) \subset P$

11, Right), and thus the set E from (8.5) contains at least one of the sets$\left( Y ^ { \prime \prime } ( T _ { \mathrm { s t e m } } ) \cap T _ { \mathrm { s e g } } ^ { ( i ) } \right) \backslash N _ { \delta } ( x )$ This yields the volume bound (8.6).

Since$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$is broad with error${ \lessapprox } \delta ^ { - \eta }$relative to$\mathbb { T } _ { \rho } ,$we have that for each$x \in E$, there are $\gtrapprox \delta \ \mu _ { \mathrm { { f i n e } } }$tubes$T \in \mathbb { T } _ { 1 } [ T _ { \rho } ] _ { Y _ { \mathrm { r e g } } ^ { \prime } } ( x )$with$\angle ( T , T _ { \mathrm { s t e m } } ) \gtrapprox \delta \delta ^ { \eta / \beta } \rho .$. Since each such tube intersects$T _ { \mathrm { s t e m } }$ in a set of dimensions at most$\begin{array} { r } { \delta \times \delta \times \frac { \delta } { \delta \eta / \beta \rho } } \end{array}$, we conclude that there is a set$\mathcal { H } = \mathcal { H } ( T _ { \mathrm { s t e m } } ) \subset \mathbb { T } _ { 1 } [ T _ { \rho } ]$ with the following properties:

$\# \mathcal { H } \gtrsim _ { \delta } ( \mu _ { \mathrm { f i n e } } \delta ^ { - 1 } c ) ( \delta ^ { \eta / \beta } \rho ) \delta ^ { 2 \eta } ,$

• Each$T \in { \mathcal { H } }$intersects$P ,$and exits P through the “long ends.”

• Each$T \in { \mathcal { H } }$satisfies$| B \cap Y ^ { \prime } ( T ) | \gtrsim \delta ^ { 2 \eta } | B \cap T | \sim \delta ^ { 2 \eta } \tilde { c } \delta ^ { 2 }$, where B is the ball of radius ˜c with the same center as$P$

The second item follows from Definition 7.1 Item (iv), plus the fact that$T \in { \mathcal { H } }$implies that$T$ and P are both associated to the same ρ tube, and$Y ( T ) \cap Y ( P ) \neq \emptyset$. The third item follows from the fact that the set E from (8.5) was defined with respect to the shading$Y _ { \mathrm { r e g } } ^ { \prime }$(recall (8.4) for the definition of$Y _ { \mathrm { r e g } } ^ { \prime } )$.

As a consequence, using$a \in [ \delta , \delta ^ { 1 - \varepsilon _ { 1 } } ] , \tilde { c } = c \delta ^ { - \omega / 1 0 0 }$, and (8.3), we have

$$
\sum_ {T \in \mathcal {H}} | B \cap Y ^ {\prime} (T) | \gtrsim \Big (\mu_ {\mathrm{fine}} \delta^ {- 1 + 2 \eta + \eta / \beta} c \rho \Big) \Big (\delta^ {2 \eta} \tilde {c} \delta^ {2} \Big) \gtrsim \mu_ {\mathrm{fine}} \delta^ {\eta / \beta + 4 \eta + \omega / 1 0 0 + \varepsilon_ {1}} (a \cdot \rho \tilde {c} \cdot \tilde {c}) \gtrsim \delta^ {- \frac {1}{2} \omega} (a \cdot \rho \tilde {c} \cdot \tilde {c}),
$$

where B is the ball of radius ˜c with the same center as P. To ensure that the final inequality holds, we select$\eta \leq \beta \omega / 1 0 0$and$\varepsilon _ { 1 } \leq \omega / 1 0 0$

We claim that by pigeonholing, we can select a prism$P ^ { \dagger } \supset P$(the larger prism on the right side of Figure 10) of dimensions 2a$\times 2 \rho \tilde { c } \times \tilde { c }$so that

$$
\sum_{\substack{T\in \mathcal{H}\\ T\text{long end} P^{\dagger}}} |P^{\dagger}\cap Y^{\prime}(T)|\gtrsim \delta^{2\eta}\sum_{\substack{T\in \mathcal{H}\\ T\text{long end} P^{\dagger}}} |P^{\dagger}\cap T|\gtrsim \delta^{-\frac{1}{4}\omega}|P^{\dagger}|,\tag{8.7}
$$

where$^ { 6 6 } T$long end$P ^ { \dagger } \ "$means that$T$exits$P ^ { \dagger }$through its long ends.

To verify this claim, note that for each tube$T \in { \mathcal { H } }$, there exists at least one$a \times \rho \tilde { c } \times \tilde { c }$prism $P ^ { \dagger }$so that$T$exits$P ^ { \dagger }$through its long end. On the other hand, there are only$\lesssim ( \tilde { c } / c ) ^ { 2 } = \delta ^ { - \frac { 1 } { 5 0 } \omega }$ essentially distinct prisms of dimensions$a \times \rho \tilde { c } \times \tilde { c }$that contain$P .$. The result now follows from pigeonholing. (Note that if$T$exits a prism$P _ { 1 } ^ { \dagger }$through its long ends, and if$P _ { 2 } ^ { \dagger }$is comparable to $P _ { 1 } ^ { \dagger }$, then$T ^ { \prime }$exits the 2-fold thickening of$P _ { 2 } ^ { \dagger }$through its long ends, where the 2-fold thickening is the prism obtained by increasing the two smaller dimensions of$P _ { 2 } ^ { \dagger }$by a factor of 2. This is why the dimension of our prisms have increased to$2 a \times 2 \rho \tilde { c } \times \tilde { c }$at this step).

Apply Corollary 7.10 (finding a broad scale) to the set H with the shading$P ^ { \dag } \cap Y ^ { \prime } ( T ) , T \in \mathcal { H }$ We obtain a scale$\tilde { \rho } \in [ \delta , 1 ]$; a set$\mathcal { H ^ { \prime } } \subset \mathcal { H }$(each$T \in { \mathcal { H } } ^ { \prime }$exists$P ^ { \dagger }$through its long ends); a subshading of the shadings$\{ P ^ { \dag } \cap Y ^ { \prime } ( T ) , T \in \mathcal { H } ^ { \prime } \}$, which we will denote by$Y _ { P \dagger } ( T )$; and a balanced partitioning cover$\mathbb { T } _ { \widetilde { \rho } } ^ { \mathcal { H } }$of$\mathcal { H ^ { \prime } }$

Note that$Y _ { P ^ { \dagger } } ( T ) \subset P ^ { \dagger } \cap Y ^ { \prime } ( T )$, and the latter set is contained in a tube segment of dimensions comparable to$\delta \times \delta \times { \tilde { c } } .$. In particular,$Y _ { P ^ { \dagger } } ( T )$is not a$\delta ^ { { \cal O } ( \eta ) }$dense shading of$T .$However, Corollary 7.10 guarantees that the shadings are “relatively” dense inside$T \cap P ^ { \dagger }$, thus

$$
\sum_ {T \in \mathcal {H} ^ {\prime}} | Y _ {P ^ {\dagger}} (T) | \gtrsim_ {\delta} \delta^ {2 \eta} \tilde {c} \delta^ {2} (\# \mathcal {H} ^ {\prime}).\tag{8.8}
$$

Note that (8.7) remains true if the shading$P ^ { \dagger } \cap Y ^ { \prime } ( T )$on the LHS of (8.7) is replaced by$Y _ { P ^ { \dagger } } ( T )$2 provided the RHS is weakened by an additional${ \approx } _ { \delta } 1$factor, i.e. we have

$$
\sum_ {T \in \mathcal {H} ^ {\prime}} | Y _ {P ^ {\dagger}} (T) | \gtrsim_ {\delta} \delta^ {- \frac {1}{4} \omega} | P ^ {\dagger} |.\tag{8.9}
$$

We claim that

$$
\tilde {\rho} \geq \delta^ {1 - \omega / 1 0 0}.\tag{8.10}
$$

We verify this claim as follows. Each point$x \in P ^ { \dagger }$is contained in at most$( \tilde { \rho } / \delta ) ^ { 2 } ( \tilde { \rho } ) ^ { - 2 \beta }$of the shadings$\{ Y _ { P ^ { \dagger } } ( T ) , \ T \in \mathcal { H } \}$. Thus if (8.10) failed, then by (8.9) we would have

$$
| P ^ {\dagger} | \geq \Big | \bigcup_ {T \in \mathcal {H}} P ^ {\dagger} \cap Y _ {P ^ {\dagger}} (T) \Big | \gtrsim_ {\delta} \Big ((\frac {\tilde {\rho}}{\delta}) ^ {2} (\tilde {\rho}) ^ {- 2 \beta} \Big) ^ {- 1} \Big (\delta^ {- \frac {1}{4} \omega} | P ^ {\dagger} | \Big) \gtrsim \delta^ {- \frac {1}{8} \omega} | P ^ {\dagger} |,
$$

which is impossible. For the final inequality, we used the assumption that$\beta \le \omega / 1 0 0$

By (8.8) and pigeonholing, we can select$T _ { 1 } \in \mathcal { H } ^ { \prime }$with$| Y _ { P ^ { \dagger } } ( T _ { 1 } ) | \gtrapprox \delta ~ \delta ^ { 2 \eta } \tilde { c } \delta ^ { 2 }$. Let$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } ^ { \mathcal { H } }$be the (unique)$\tilde { \rho }$tube with$T _ { 1 } \in \mathcal { H } ^ { \prime } [ T _ { \tilde { \rho } } ]$. For each$x \in Y _ { P ^ { \dagger } } ( T _ { 1 } )$, the directions of the tubes in$\mathcal { H } ^ { \prime } [ \dot { T } _ { \tilde { \rho } } ] _ { Y _ { P ^ { \dagger } } } ( x )$ are broad with error$\lessapprox \delta ^ { \mathrm { ~ 1 ~ } }$inside the$\tilde { \rho }$cap centered at dir$( T _ { \tilde { \rho } } )$. In particular, the intersection of each of these tubes with$P ^ { \dagger }$is contained in$P ^ { \dagger } \cap N _ { \tilde { \rho } \tilde { c } } ( T _ { 1 } )$; the latter set is contained in a$\phantom { } _ { \perp } 2 a \times \tilde { \rho } \tilde { c } \times \tilde { c }$ prism; call this prism${ \tilde { P } } _ { - }$—this is the green prism in Figure 10. Note that since each$T \in \mathcal { H } ^ { \prime }$exits $P ^ { \dagger }$through its long ends, each of the tubes$T \in \mathcal { H } ^ { \prime } [ T _ { \tilde { \rho } } ] _ { Y _ { P ^ { \dagger } } } ( x )$described above exit$\tilde { P }$through its long ends.

Applying a standard Cordoba-type$L ^ { 2 }$argument<sup>2</sup>, we conclude that if we define

$$
\mathbb {T} _ {\tilde {P}} = \{T \in \mathcal {H} ^ {\prime} [ T _ {\tilde {\rho}} ] \colon T \cap \tilde {P} \neq \emptyset , T \text {exits} \tilde {P} \text {through its long ends} \},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">T<sup>′</sup> ∈ H<sup>′</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∼ ρ˜</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">T1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">T1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">δ/</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">≲ 1.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2a × ρ˜c˜× c˜</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>In brief, we select a set of tubes that make angle with T<sub>1</sub> and intersect T<sub>1</sub> at δ/ρ˜ separated points; this latter collection of tubes, restricted to the prism described above, satisfies the Katz-Tao Convex Wolf Axioms with error Each of these tubes has a shading Y<sup>′</sup>(T) ∩ P<sup>˜</sup> that satisfies , and henceY'(T)∩P|Y<sup>′</sup>(T) ∩ P<sup>˜</sup>| ≳ δ<sup>2η</sup>cδ˜ <sup>2</sup> the union of these shadings is almost disjoint.</span></small>

and define the shading$Y _ { \tilde { P } } ( T ) = Y _ { P ^ { \dagger } } ( T ) \cap \tilde { P }$(note if$T \in \mathbb { T } _ { \tilde { P } } .$, T exists$\tilde { P }$through its long ends, so $Y _ { \tilde { P } } ( T ) = Y _ { P ^ { \dagger } } ( T )$, we rename it to be$Y _ { \tilde { P } } ( T )$just for notational convenience), then the set

$$
Y (\tilde {P}) = \bigcup_ {T \in \mathbb {T} _ {\tilde {P}}} Y _ {\tilde {P}} (T)
$$

satisfies$| Y ( \tilde { P } ) | \gtrsim \delta ^ { 4 \eta + 4 \varepsilon _ { 1 } } | \tilde { P } |$(here the$\delta ^ { 4 \varepsilon _ { 1 } }$loss comes from the fact that the prism$\tilde { P }$is not a $\delta \times \tilde { \rho } \tilde { c } \times \tilde { c }$prism, but rather a$2 a \times \tilde { \rho } \tilde { c } \times \tilde { c }$prism with$a \in [ \delta , \delta ^ { 1 - \varepsilon _ { 1 } } ] )$. Furthermore, for each $x \in Y ( \tilde { P } )$, the set of unit vectors$\{ \mathrm { d i r } ( T ) \colon T \in ( \mathbb { T } _ { \tilde { P } } ) _ { Y _ { \tilde { P } } } ( x ) \}$is broad with error$\lessapprox$1 inside the $\tilde { \rho } { - }$cap$B ( \mathrm { d i r } ( \tilde { P } ) , \tilde { \rho } )$

Step 4. We summarize the conclusion from Step 3. Given a refinement$( \mathbb { T } _ { 1 } , Y ^ { \prime } ) _ { \delta }$of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$that satisfies$\begin{array} { r } { \sum \left| Y ^ { \prime } ( T ) \right| \ge \frac { 1 } { 2 } \sum \left| Y _ { 1 } ( T ) \right| } \end{array}$, we have located the following objects:

• A scale${ \tilde { \rho } } .$

• A$2 a \times \tilde { \rho } \tilde { c } \times \tilde { c }$prism$\tilde { P }$and a shading$Y ( { \tilde { P } } )$on this prism.

• A set of tubes$\mathbb { T } _ { \tilde { P } }$and a shading$Y _ { \tilde { P } } ( { \cal T } ) \subset Y ^ { \prime } ( { \cal T } ) \cap \tilde { P }$on these tubes.

These objects have the following properties:

• Each$T \in \mathbb { T } _ { \tilde { P } }$exits$\tilde { P }$through its long ends, in the sense of Figure 9, Left.

$Y ( \tilde { P } ) = \bigcup _ { T \in \mathbb { T } _ { \tilde { D } } } Y _ { \tilde { P } } ( T )$, and$| Y ( \tilde { P } ) | \gtrapprox \delta ~ \delta ^ { 4 \eta + 4 \varepsilon _ { 1 } } | \tilde { P } |$

• For each$x \in Y ( P )$, the tubes in$( \mathbb { T } _ { \tilde { P } } ) _ { Y _ { \tilde { P } } } ( x )$point in directions that are broad with error$\lessapprox$1 inside the$\tilde { \rho }$cap$B ( \mathrm { d i r } ( \tilde { P } ) , \tilde { \rho } )$

We will now iteratively apply the argument from Step 3. We begin by setting$( \mathbb { T } , Y ^ { \prime } ) = ( \mathbb { T } , Y _ { 1 } )$ and$\tilde { \mathcal { P } } _ { 0 } = \emptyset$. As long as$\begin{array} { r } { \sum | Y ^ { \prime } ( T ) | \ge \frac { 1 } { 2 } \sum | Y _ { 1 } ( T ) } \end{array}$|, we proceed as follows:

• Apply the argument from Step 3.

• Place the prism$\tilde { P }$located in Step 3 into the multiset$\begin{array} { r } { \tilde { \mathcal { P } } _ { 0 } \ ( \mathrm { i . e . } } \end{array}$. if the prism is already present, then we add another copy).

• For each$T \in \mathbb { T } _ { \tilde { P } } ,$replace the shading$Y ^ { \prime } ( T )$with$Y ^ { \prime } ( T ) \backslash Y _ { \tilde { P } } ( T )$

We repeat the above steps until$\begin{array} { r } { \sum \left| Y ^ { \prime } ( T ) \right| < \frac { 1 } { 2 } \sum \left| Y _ { 1 } ( T ) \right| } \end{array}$, at which point we halt.

Let us examine the output from the above procedure. First, we have

$$
\sum_ {\tilde {P} \in \tilde {\mathcal {P}} _ {0}} \sum_ {T \in \mathbb {T} _ {\tilde {P}}} | Y _ {\tilde {P}} (T) | \geq \frac {1}{2} \sum_ {T \in \mathbb {T}} | Y _ {1} (T) | \gtrsim_ {\delta} \sum_ {T \in \mathbb {T}} | Y (T) |.\tag{8.11}
$$

After dyadic pigeonholing, we can select a multiset$\tilde { \mathcal { P } } _ { 1 } \subset \tilde { \mathcal { P } } _ { 0 }$so that each$\tilde { P } \in \tilde { \mathcal { P } } _ { 1 }$has a common value of$\tilde { \rho }$(up to a factor of 2). Abusing notation slightly, we will denote this value by${ \tilde { \rho } } .$We will choose$\mathcal { \hat { P } } _ { 1 }$so that the bound (8.11) (the first and final terms) remains true with$\tilde { \mathcal { P } } _ { 1 }$in place of$\mathcal { \tilde { P } } _ { 0 }$

For each$T \in \mathbb { T } _ { 1 }$, define$Y _ { 2 } ( T ) = \bigcup _ { \tilde { P } } Y _ { \tilde { P } } ( T )$, where the union is taken over those$\tilde { P } \in \tilde { \mathcal { P } } _ { 1 }$with $T \in \mathbb { T } _ { \tilde { P } }$. For notational consistency, define$\mathbb { T } _ { 2 } = \mathbb { T } _ { 1 }$. Then$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$is an${ \approx } _ { \delta } ~ 1$refinement of $( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$

Step 5. We will summarize the conclusion from Step 4. We have located the following objects:

$\mathrm { A } \approx _ { \delta } 1$refinement$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$, which in turn is an${ \approx } _ { \delta }$1 refinement of$( \mathbb { T } , Y ) _ { \delta }$

• A scale$\tilde { \rho } \geq \delta ^ { 1 - \omega / 1 0 0 }$

• A multiset$\tilde { \mathcal { P } } _ { 1 }$of$2 a \times \tilde { \rho } \tilde { c } \times \tilde { c }$prisms, and a shading$Y _ { 1 } ( \tilde { P } )$on these prisms (In Step 4 this shading was called$Y ( \tilde { P } ) )$. Note that the prisms in$\tilde { \mathcal { P } } _ { 1 }$might not be essentially distinct.

• For each prism$\tilde { P } \in \tilde { \mathcal { P } } _ { 1 }$, a set of tubes$\mathbb { T } _ { \tilde { P } } \subset \mathbb { T } _ { 2 }$

These objects have the following properties:

(a) For each$\tilde { P } \in \tilde { \mathcal { P } } _ { 1 }$, each$T \in \mathbb { T } _ { \tilde { P } }$exits$\tilde { P }$through the long ends.

(b) For each$\tilde { P } \in \tilde { \mathcal { P } } _ { 1 }$, we have$\begin{array} { r } { Y _ { 1 } ( \tilde { P } ) = \tilde { P } \cap \bigcup _ { T \in \mathbb { T } _ { \tilde { P } } } Y _ { 2 } ( T ) , \mathrm { a n d } | Y _ { 1 } ( \tilde { P } ) | \gtrapprox \delta \delta \delta ^ { 4 \eta + 4 \varepsilon _ { 1 } } | \tilde { P } | . } \end{array}$

(c) For each$\tilde { P } \in \tilde { \mathcal { P } } _ { 1 }$and for each$x \in Y _ { 1 } ( \tilde { P } )$, the tubes in$( \mathbb { T } _ { \widetilde { P } } ) _ { Y _ { 2 } } ( x )$point in directions that are broad with error$\lessapprox$1 inside the$\tilde { \rho }$cap$B ( \mathrm { d i r } ( \tilde { P } ) , \tilde { \rho } )$

Let us compare the above items to Conclusion (C) of Lemma 8.2. We have that Items (i) and (iv) of Conclusion (C) are currently satisfied. We will work towards satisfying the other Items.

First, the prisms in$\tilde { \mathcal { P } } _ { 1 }$might not be essentially distinct. This is not a minor failure fixable by$\mathrm { ~ a ~ } \sim 1$refinement, but instead a dramatic failure — it is possible that a very large number of prisms from$\tilde { \mathcal { P } } _ { 1 }$are all pairwise comparable, or even identical. We can fix this problem by merging comparable 2a${ \bf \nabla } \times \tilde { \rho } \tilde { c } \times \tilde { c }$prisms in$\tilde { \mathcal { P } } _ { 1 }$into a single$4 a \times \tilde { \rho } ( 2 \tilde { c } ) \times ( 2 \tilde { c } )$prism. We will refer to this new, post-merger set of prisms as$\tilde { \mathcal { P } } _ { 2 }$. Our shading$Y _ { 2 } ( \tilde { P } )$on our newly constructed prisms is given by the union of the shadings of the corresponding prisms from$\tilde { \mathcal { P } } _ { 1 }$, and the set$\mathbb { T } _ { \tilde { P } } \subset \mathbb { T } _ { 2 }$is the union of the sets$\{ \mathbb { T } _ { \tilde { P } _ { 1 } } \}$from the corresponding prisms from$\tilde { \mathcal { P } } _ { 1 }$

Item (a) from the start of Step 5 might no longer hold for our newly constructed prisms$\tilde { \mathcal { P } } _ { 2 } ^ { } .$ but this is a minor failure — we can restore it by replacing each 4a$\times 2 \tilde { \rho } ( 2 \tilde { c } ) \times ( 2 \tilde { c } )$prism by the prism of dimensions$1 0 0 a \times 1 0 0 \tilde { \rho } \tilde { c } \times 2 \tilde { c }$with the same center and axes (see Figure 12). Annoyingly, this might destroy the property that the prisms are essentially distinct, but this time, this is only a minor failure — essential distinctness can be restored by$\mathrm { ~ a ~ } \sim 1$refinement of the prisms (this refinement induces$\mathrm { a } \sim 1$refinement of the shading$Y _ { 2 }$on$\mathbb { T } _ { 2 } )$. Denote the new set of prisms created through this process by$\tilde { \mathcal { P } } _ { 3 }$. Abusing notation slightly, we will redefine the quantities${ \tilde { c } } ,$and$\tilde { \rho }$and let$\tilde { a } = 1 0 0 a$(increasing each by$\mathrm { ~ a ~ } \sim 1$multiplicative factor) so that the prisms in$\tilde { \mathcal { P } } _ { 3 }$still have dimensions$\tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c }$

Note that Item (b) above continues to hold for our newly constructed prisms and their associated shading. Crucially, Item (c) also continues to hold; this follows from Lemma 7.12 (a union of sets of broad vectors is broad). More specifically, the sets of broad vectors through each point are disjoint because in Step 4, for each$T \in \mathbb { T } _ { \tilde { P } }$, we have replaced the shading$Y ^ { \prime } ( T )$with$Y ^ { \prime } ( T ) \setminus Y _ { \tilde { P } } ( T )$, so through each point$x ,$there is at most one$\tilde { P }$such that$x \in Y _ { \tilde { P } } ( T )$. Since the sets are disjoint, their union is a set instead of multi-set, so Lemma 7.12 implies that the union (as a set) of sets of broad vectors is broad.

Step 6. In Step 5 we constructed a set$\tilde { \mathcal { P } } _ { 3 }$of essentially distinct$\tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c }$prisms, and a shading $Y _ { 3 }$on these prisms. We shall refer to this pair as$( \tilde { \mathcal { P } } _ { 3 } , Y _ { 3 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$. For each$\tilde { P } \in \tilde { \mathcal { P } } _ { 3 }$, we have a set $\mathbb { T } _ { \tilde { P } } \subset \mathbb { T } _ { 2 } ;$each of these tubes exits$\tilde { P }$through its long ends.

![](images/page_80_image_0.jpg)

Figure 12: The prisms$\tilde { P }$and${ \tilde { P } } ^ { \prime }$are comparable, and thus both are replaced by a common 4a × $\tilde { \rho } ( 2 \tilde { c } ) \times ( 2 \tilde { c } )$prism (which happens to be$2 \tilde { P }$, i.e. the 2-fold dilate of$\tilde { P } )$. This creates a problem (circled in red): A tube (green) that exits the prism${ \tilde { P } } ^ { \prime }$through its long ends might fail to exit$2 \tilde { P }$ through its long ends. However, this problem can be fixed by replacing the 4a$\times \tilde { \rho } ( 2 \tilde { c } ) \times ( 2 \tilde { c } )$prism by a slightly wider and thicker (but not taller) prism.

Our current task is to further refine the pair$( \tilde { \mathcal { P } } _ { 3 } , Y _ { 3 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$and$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$to more closely match Conclusion (C) of Lemma 8.2. Item (ii) of Conclusion (C) refers to a partitioning cover$\mathbb { T } _ { \widetilde { \rho } }$of $\mathbb { T } ^ { \prime }$. We will construct this as follows. To begin, let$\{ T _ { \tilde { \rho } } \}$be a set of$\tilde { \rho }$tubes with the following properties:

• Every δ tube is contained in at least one tube from$\{ T _ { \tilde { \rho } } \}$

• For every${ \tilde { a } } \times { \tilde { \rho } } { \tilde { c } } \times { \tilde { c } }$prism$\tilde { P } _ { \ l }$, there is at least one$\tilde { \rho }$tube$T _ { \tilde { \rho } } ~ \in ~ \{ T _ { \tilde { \rho } } \}$with$\tilde { P } \subset T _ { \tilde { \rho } }$and $\angle ( \mathrm { d i r } ( \tilde { P } ) , \mathrm { d i r } ( T _ { \tilde { \rho } } ) ) \leq 2 \tilde { \rho }$

• The tubes in$\{ T _ { \tilde { \rho } } \}$are weakly essentially distinct, in the following sense: for each fixed$T _ { \tilde { \rho } } \in$ $\{ T _ { \tilde { \rho } } \}$, there are$O ( 1 )$other tubes from$\{ T _ { \tilde { \rho } } \}$that are comparable to$T _ { \tilde { \rho } }$

Next, by pigeonholing the set$\{ T _ { \tilde { \rho } } \}$by a$O ( 1 )$factor, we can select a set$\mathbb { T } _ { \tilde { \rho } } \subset \{ T _ { \tilde { \rho } } \}$that is strongly essentially distinct, in the following sense: for each pair of distinct tubes$T _ { \tilde { \rho } } , T _ { \tilde { \rho } } ^ { \prime }$from$\mathbb { T } _ { \widetilde { \rho } } .$ we have that$N _ { 1 0 0 \tilde { \rho } } ( T _ { \tilde { \rho } } ) \cap N _ { 1 0 0 \tilde { \rho } } ( T _ { \tilde { \rho } } ^ { \prime } )$has diameter at most$1 / 2$, and in particular no$\delta$tube can be contained in both$N _ { 1 0 0 \tilde { \rho } } ( T _ { \tilde { \rho } } )$and$N _ { 1 0 0 \tilde { \rho } } ( T _ { \tilde { \rho } } ^ { \prime } )$. We will select the set$\mathbb { T } _ { \widetilde { \rho } }$so that the following properties hold:

(i) If we define$\mathbb { T } _ { 4 }$to be the set of tubes$T \in \mathbb { T } _ { 2 }$contained in some$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } ,$, i.e.$\mathbb { T } _ { 4 } ~ =$ $\textstyle \bigcup _ { T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } } \mathbb { T } _ { 2 } [ T _ { \tilde { \rho } } ]$, and define$Y _ { 4 }$to be the restriction of$Y _ { 2 }$to$\mathbb { T } _ { 4 }$, then$( \mathbb { T } _ { 4 } , Y _ { 4 } ) _ { \delta }$is$\mathrm { ~ a ~ } \sim 1$refinement of$( \mathbb { T } _ { 2 } , Y _ { 2 } ) _ { \delta }$

(ii) Similarly to the previous item, if we define$\tilde { \mathcal { P } } _ { 4 }$to be the set of prisms$\tilde { P } \in \tilde { \mathcal { P } } _ { 3 }$with the property that there exists$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } }$with$\tilde { P } \subset T _ { \tilde { \rho } }$and$\angle ( \mathrm { d i r } ( \tilde { P } ) , \mathrm { d i r } ( T _ { \tilde { \rho } } ) ) \leq 2 \tilde { \rho }$, and define

$$
Y _ {4} (\tilde {P}) = Y _ {3} (\tilde {P}) \cap \bigcup_ {T \in \mathbb {T} _ {\tilde {P}} \cap \mathbb {T} _ {4}} Y _ {4} (T),\tag{8.12}
$$

then$( \tilde { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$is$\mathrm { a } \gtrsim 1$refinement of$( \tilde { \mathcal { P } } _ { 3 } , Y _ { 3 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$

(a) A consequence of Item (i) is that$\mathbb { T } _ { \widetilde { \rho } }$is a partitioning cover of$\mathbb { T } _ { 4 }$, and in fact more is true: the sets$\{ N _ { 1 0 0 \widetilde { \rho } } ( T _ { \widetilde { \rho } } ) \colon T _ { \widetilde { \rho } } \in \mathbb { T } _ { \widetilde { \rho } } \}$form a partitioning cover of of T<sub>4</sub>.

(b) A consequence of Item (ii) is that for each$\tilde { P } \in \tilde { \mathcal { P } } _ { 4 }$, there is a unique$T _ { \widetilde { \rho } } \in \mathbb { T } _ { \widetilde { \rho } }$that satisfies the two properties$\tilde { P } \subset T _ { \tilde { \rho } }$and$\angle ( \mathrm { d i r } ( \tilde { P } ) , \mathrm { d i r } ( T _ { \tilde { \rho } } ) ) \leq 2 \tilde { \rho }$. This induces a partition

$$
\tilde {\mathcal {P}} _ {4} = \bigsqcup_ {\mathbb {T} _ {\tilde {\rho}}} (\tilde {\mathcal {P}} _ {4}) _ {T _ {\tilde {\rho}}}.\tag{8.13}
$$

(C.f. Definition 7.1, Item (i).)

(c) A consequence of Items (i) and (ii) is that if$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } , \tilde { P } \in ( \tilde { \mathcal { P } } _ { 4 } ) _ { T _ { \tilde { \rho } } }$, and$T \in \mathbb { T } _ { \tilde { P } } \cap \mathbb { T } _ { 4 }$, then$T \in$ $\mathbb { T } _ { 4 } [ T _ { \tilde { \rho } } ]$]. This is because T exits P<sup>˜</sup> through its long ends, and hence$\angle ( \mathrm { d i r } ( T ) , \mathrm { d i r } ( \tilde { P } ) ) \leq 1 0 \tilde { \rho }$

Our next task is to estimate the quantity$\textstyle \sum _ { \tilde { P } \in \tilde { \mathcal { P } } _ { 4 } } | \tilde { P } |$. Let$\tau _ { i }$be the scale from Step 2 satisfying $\delta ^ { \varepsilon _ { 1 } } \rho \leq \tau _ { i } < \rho$. Since$( \tilde { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } } \mathrm { ~ i s ~ } \gtrsim _ { \delta } \delta ^ { 4 \eta + 4 \varepsilon _ { 1 } }$dense, we have

$$
\begin{array}{l} \sum_ {\tilde {P} \in \tilde {\mathcal {P}} _ {4}} | \tilde {P} | \lesssim_ {\delta} \delta^ {- 4 \eta - 4 \varepsilon_ {1}} \sum_ {\tilde {P} \in \tilde {\mathcal {P}} _ {4}} | Y _ {4} (\tilde {P}) | \\ = \delta^ {- 4 \eta - 4 \varepsilon_ {1}} \sum_ {T _ {\tilde {\rho}} \in \mathbb {T} _ {\tilde {\rho}}} \Big | \bigsqcup_ {\tilde {P} \in (\tilde {\mathcal {P}} _ {4}) _ {T _ {\tilde {\rho}}}} Y _ {4} (\tilde {P}) \Big | \\ \leq \delta^ {- 4 \eta - 4 \varepsilon_ {1}} \sum_ {T _ {\tilde {\rho}} \in \mathbb {T} _ {\tilde {\rho}}} \Big | \bigcup_ {T \in \mathbb {T} _ {4} [ T _ {\tilde {\rho}} ]} Y _ {4} (T) \Big | \\ \lesssim \delta^ {- 4 \eta - 4 \varepsilon_ {1}} \sum_ {T _ {\tilde {\rho}} \in \mathbb {T} _ {\tilde {\rho}}} \Big (\mu_ {i} ^ {- 1} \sum_ {T \in \mathbb {T} _ {1} [ T _ {\tilde {\rho}} ]} | Y _ {1} (T) | \Big) \\ = \delta^ {- 4 \eta - 4 \varepsilon_ {1}} \mu_ {i} ^ {- 1} \sum_ {T \in \mathbb {T} _ {1}} | Y _ {1} (T) | \\ \lesssim \delta^ {- 4 \eta - 4 \varepsilon_ {1}} \mu_ {i} ^ {- 1} \sum_ {T \in \mathbb {T} _ {2}} | Y _ {2} (T) |. \end{array}\tag{8.14}
$$

For the third line we used (8.12). For the fourth line, we used the fact that each$\tilde { \rho }$tube contains some τ<sub>i</sub>-tube and Item (i) in Step 2. For the last line, we used (8.11) and the definition of$Y _ { 2 } ( T ) =$ $\begin{array} { r } { \bigcup _ { \tilde { P } } Y _ { \tilde { P } } ( T ) } \end{array}$

## Step 7.

We would like to show that after a suitable refinement,$( \tilde { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$is a robustly$\delta ^ { \varepsilon } .$-dense two-scale grains decomposition of$( \mathbb { T } _ { 4 } , Y _ { 4 } ) _ { \delta }$wrt$\mathbb { T } _ { \widetilde { \rho } } .$, in the sense of Definition 7.1. Currently, the biggest obstacle is Item (ii) from Definition 7.1. In particular, it need not be the case that the sets $\{ Y _ { 4 } ( \tilde { P } ) \colon \tilde { P } \in ( \tilde { \mathcal { P } } _ { 4 } ) _ { T _ { \tilde { \rho } } } \}$are pairwise disjoint.

We will fix this problem as follows. We claim that either Conclusion (A) of Lemma 8.2 is true (and thus we are done), or there exists a refinement$( \mathbb { T } _ { 5 } , Y _ { 5 } ) _ { \delta }$of$( \mathbb { T } _ { 4 } , Y _ { 4 } )$, and a refinement $( \tilde { \mathcal { P } } _ { 5 } , Y _ { 5 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } } ~ \mathrm { o f } ~ ( \tilde { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$with the following properties:

• For each$T _ { \rho } \in \mathbb { T } _ { \rho } .$the sets$\{ Y _ { 5 } ( \tilde { P } ) \colon \tilde { P } \in ( \tilde { \mathcal { P } } _ { 5 } ) _ { T _ { \tilde { \rho } } } \}$are pairwise disjoint (here$( \tilde { \mathcal { P } } _ { 5 } ) _ { T _ { \tilde { \rho } } } = \tilde { \mathcal { P } } _ { 5 } \cap$ $( \tilde { \mathcal { P } } _ { 4 } ) _ { T _ { \tilde { \rho } } }$; recall (8.13)).

$( \tilde { \mathcal { P } } _ { 5 } , Y _ { 5 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$is a$\stackrel { > } { \approx } \delta ^ { \varepsilon _ { 2 } }$refinement of$( \tilde { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$

• The pair$( \mathbb { T } _ { 5 } , Y _ { 5 } ) _ { \delta }$is a$\stackrel { > } { \approx } \delta ^ { \varepsilon _ { 2 } }$refinement of$( \mathbb { T } _ { 4 } , Y _ { 4 } ) _ { \delta }$, where$\mathbb { T } _ { 5 } = \mathbb { T } _ { 4 }$, and the shading$Y _ { 5 }$is given by

$$
Y_{5}(T) = Y_{4}(T)\cap \bigcup_{\substack{\tilde{P}\in (\tilde{\mathcal{P}}_{5})_{T_{\tilde{\rho}}}\\ T\in \mathbb{T}_{\tilde{P}}\cap \mathbb{T}_{4}}}Y_{5}(\tilde{P}),\tag{8.15}
$$

where$T _ { \tilde { \rho } }$is the unique$\tilde { \rho }$tube containing$T .$

• For each$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } .$, we have

$$
\bigcup_ {T \in \mathbb {T} _ {\mathfrak {S}} [ T _ {\tilde {\rho}} ]} Y _ {\mathfrak {S}} (T) = \bigsqcup_ {\tilde {P} \in (\tilde {\mathcal {P}} _ {\mathfrak {S}}) _ {T _ {\tilde {\rho}}}} Y _ {\mathfrak {S}} (\tilde {P}).\tag{8.16}
$$

We will prove this claim in Step 8 below. Let us accept this claim for the moment.

The pair$( \tilde { \mathcal { P } } _ { 5 } , Y _ { 5 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$and$( \mathbb { T } _ { 5 } , Y _ { 5 } ) _ { \delta }$now satisfy Items (i), (ii), and (iv) from Definition 7.1. Items (i) and (ii) are immediate. We can verify Item (iv) as follows: If$T$and$\tilde { P }$are associated to a common$\rho$tube, and if$Y _ { 5 } ( T ) \cap Y _ { 5 } ( \tilde { P } ) \neq \emptyset$, then we must have$T \in \mathbb { T } _ { 4 } \cap \mathbb { T } _ { \tilde { P } } ,$and hence we have that$T$exits$\tilde { P }$through its long end, and also$Y _ { 5 } ( T ) \cap \tilde { P } \subset Y _ { 5 } ( \tilde { P } )$(this follows from the definition of the shading$Y _ { 5 }$from (8.15)), as desired.

It remains to obtain Item (iii) from Definition 7.1. By dyadic pigeonholing, there is a number $\mu ;$a set$\mathbb { T } _ { \widetilde { \rho } } ^ { \prime } \colon$and an${ \approx } _ { \delta }$1 refinement$( \mathbb { T } _ { 6 } , Y _ { 6 } ) _ { \delta }$of$( \mathbb { T } _ { 5 } , Y _ { 5 } ) _ { \delta }$so that the following holds:

$\mathbb { T } _ { \widetilde { \rho } } ^ { \prime }$is a balanced partitioning cover of$\mathbb { T } _ { 6 }$.

• For each$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } ^ { \prime }$and each$x \in \bigcup _ { T \in \mathbb { T } _ { 6 } [ T _ { \tilde { \rho } } ] } Y _ { 6 } ( T )$, we have$\# \big ( ( \mathbb { T } _ { 6 } [ T _ { \widetilde { \rho } } ] ) _ { Y _ { 6 } } ( x ) \big ) \sim \mu$

Let$\begin{array} { r } { \tilde { \mathcal { P } } _ { 6 } = \bigcup _ { T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { o } } ^ { \prime } } ( \tilde { \mathcal { P } } _ { 5 } ) _ { T _ { \tilde { \rho } } } } \end{array}$and let$Y _ { 6 } ( { \tilde { P } } ) \subset Y _ { 5 } ( { \tilde { P } } )$be the shading so that (8.16) continues to hold with$( \mathbb { T } _ { 6 } , Y _ { 6 } ) _ { \delta }$in place of$( \mathbb { T } _ { 5 } , Y _ { 5 } ) _ { \delta }$, and$( \tilde { \mathcal { P } } _ { 6 } , Y _ { 6 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$in place of$( \tilde { \mathcal { P } } _ { 5 } , Y _ { 5 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$

The triple$( \mathbb { T } _ { 6 } , Y _ { 6 } ) _ { \delta } , ( \tilde { \mathcal { P } } _ { 6 } , Y _ { 6 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } } .$and$\mathbb { T } _ { \widetilde { \rho } }$continue to satisfy Items (i), (ii), and (iv) from Definition 7.1. To verify Item (iii), we need to estimate the density of the shading on$( \tilde { \mathcal { P } } _ { 6 } , Y _ { 6 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$ From (8.14), we have

$$
\sum_ {\tilde {P} \in \tilde {\mathcal {P}} _ {6}} | \tilde {P} | \lesssim_ {\delta} \delta^ {- 4 \eta - 4 \varepsilon_ {1}} \mu_ {i} ^ {- 1} \sum_ {T \in \mathbb {T} _ {2}} | Y _ {2} (T) |.\tag{8.17}
$$

Note that$\mu \lesssim \mu _ { i } \delta ^ { - 2 \varepsilon _ { 1 } }$(recall that$\mu _ { i }$is the multiplicity associated to scale$\tau _ { i } ,$which was chosen

in Step 6). Thus we can compute

$$
\begin{array}{l} \sum_ {\tilde {P} \in \tilde {\mathcal {P}} _ {6}} | Y _ {6} (\tilde {P}) | = \sum_ {T _ {\tilde {\rho}} \in \mathbb {T} _ {\tilde {\rho}} ^ {\prime}} \Big | \bigsqcup_ {\tilde {P} \in (\tilde {\mathcal {P}} _ {6}) _ {T _ {\tilde {\rho}}}} Y _ {6} (\tilde {P}) \Big | \\ \qquad = \sum_ {T _ {\tilde {\rho}} \in \mathbb {T} _ {\tilde {\rho}} ^ {\prime}} \Big | \bigcup_ {T \in \mathbb {T} _ {6} [ T _ {\tilde {\rho}} ]} Y _ {6} (T) \Big | \\ \gtrsim \sum_ {T _ {\tilde {\rho}} \in \mathbb {T} _ {\tilde {\rho}} ^ {\prime}} \Big (\mu^ {- 1} \sum_ {T \in \mathbb {T} _ {6} [ T _ {\tilde {\rho}} ]} | Y _ {6} (T) | \Big) \\ \gtrsim \mu_ {i} ^ {- 1} \delta^ {2 \varepsilon_ {1}} \sum_ {T \in \mathbb {T} _ {6}} | Y _ {6} (T) | \\ \gtrsim_ {\delta} \mu_ {i} ^ {- 1} \delta^ {\varepsilon_ {2} + 2 \varepsilon_ {1}} \sum_ {T \in \mathbb {T} _ {6}} | Y _ {2} (T) |. \end{array}\tag{8.18}
$$

Comparing (8.17) and (8.18), we conclude that$( \tilde { \mathcal { P } } _ { 6 } , Y _ { 6 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } } \mathrm { i s } \gtrsim \delta ^ { 4 \eta + 6 \varepsilon _ { 1 } + \varepsilon _ { 2 } } \geq \delta ^ { 2 \varepsilon _ { 2 } }$dense. We now select$\varepsilon _ { 2 }$suficiently small (depending on ε) so that this quantity is$\geq \delta ^ { \varepsilon }$. We conclude that Conclusion (C) of Lemma 8.2 holds.

This concludes the proof of Lemma 8.2, except that we must still prove the Claim stated at the beginning of Step 7. We will do this below.

Step 8. Our final task is to prove the Claim from Step 7. For notational convenience, we will abuse notation and rename the set$( \tilde { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$as$( \tilde { \mathcal { P } } , Y ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$. Informally, the idea is as follows: If the shadings$\{ Y ( \tilde { P } ) \colon \tilde { P } \in \tilde { \mathcal { P } } _ { T _ { \tilde { \rho } } } \}$have small overlap, then we can refine these these shadings to be disjoint. On the other hand, if the shadings have large overlap, then since the prisms in$\tilde { \mathcal { P } } _ { T _ { \tilde { \rho } } }$are essentially distinct and all satisfy$\angle ( \mathrm { d i r } ( \tilde { P } ) , \mathrm { d i r } ( T _ { \tilde { \rho } } ) ) \lesssim \tilde { \rho } ,$we have that the prisms in$\tilde { \mathcal { P } } _ { Y } ( x )$(i.e. the prisms passing through a typical point) must have difering tangent planes (i.e. there must exist prisms$\tilde { P } , \tilde { P } ^ { \prime } \in \tilde { \mathcal { P } } _ { Y } ( x )$for which$\angle ( \Pi ( \tilde { P } ) , \Pi ( \tilde { P } ^ { \prime } ) )$is large). We then apply Lemma 5.10 to show that the thickened neighbourhood of a typical prism in$\tilde { \mathcal P }$has large intersection with$\textstyle \bigcup _ { \tilde { P } \in \tilde { \mathcal { P } } } Y ( \tilde { P } )$, and this in turn means that the thickened neighbourhood of a typical tube in$\mathbb { T } _ { 4 }$has large intersection with$\cup _ { \mathbb { T } } Y ( T )$. By Corollary 5.19, this yields Conclusion (A) of Lemma 8.2. We now turn to the details.

Using Lemma 5.9 (every shading has a regular sub-shading), we may select$\mathrm { ~ a ~ } \gtrsim 1$refinement $( \tilde { \mathcal { P } } ^ { \prime } , Y ^ { \prime } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$with the property that each shading$Y ^ { \prime } ( \tilde { P } ) , \tilde { P } \in \tilde { \mathcal { P } } ^ { \prime }$is regular (recall Definition 5.8) and satisfies$| Y ^ { \prime } ( \tilde { P } ) | \gtrapprox \delta ~ \delta ^ { 4 \eta + 4 \varepsilon _ { 1 } } | \tilde { P } |$

After dyadic pigeonholing, we may suppose there exists a number ν and a$\gtrapprox \delta$refinement $( \tilde { \mathcal { P } } ^ { \prime \prime } , Y ^ { \prime \prime } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$of$( \tilde { \mathcal { P } } ^ { \prime } , Y ^ { \prime } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$so that for each$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } }$and each point$x \in \bigcup _ { \tilde { P } \in ( \tilde { \mathcal { P } } ^ { \prime \prime } ) _ { T _ { \tilde { \rho } } } } Y ^ { \prime \prime } ( \tilde { P } )$, we have$\# ( ( \tilde { \mathcal { P } } _ { T _ { \tilde { \rho } } } ^ { \prime \prime } ) _ { Y ^ { \prime \prime } } ( x ) ) \sim \nu$

First, we will consider the case where

$$
\nu \geq \delta^ {- \varepsilon_ {2}}.\tag{8.19}
$$

We will show that Conclusion (A) of Lemma 8.2 is true for a suitably chosen value of α. Observe that the prisms in$( ( \tilde { \mathcal { P } } ^ { \prime } ) _ { T _ { \tilde { \rho } } } ) _ { Y ^ { \prime } } ( x )$are essentially distinct, and they all satisfy$\angle ( \mathrm { d i r } ( T _ { \tilde { \rho } } ) , \mathrm { d i r } ( \tilde { P } ) ) \leq 2 \tilde { \rho } .$ Furthermore, they all (by definition) pass through the common point x. Thus for each point $x \in \bigcup _ { \tilde { P } \in ( \tilde { \mathcal { P } } ^ { \prime \prime } ) _ { T _ { \tilde { \rho } } } } Y ^ { \prime \prime } ( \tilde { P } )$, there must exist a pair of prisms$\tilde { P } , \tilde { P } ^ { \prime }$from this set with

$$
\angle \bigl (\Pi (\tilde {P} ^ {T _ {\tilde {\rho}}}), \Pi \bigl ((\tilde {P} ^ {\prime}) ^ {T _ {\tilde {\rho}}} \bigr) \bigr) \gtrsim \nu^ {1 / 2} (\tilde {a} / (\tilde {\rho} \tilde {c})).
$$

(For comparison,$\Pi ( { \tilde { P } } ^ { T _ { \tilde { \rho } } } )$and$\Pi \big ( ( \tilde { P } ^ { \prime } ) ^ { T _ { \tilde { \rho } } } \big )$are defined up to uncertainty$\tilde { a } / ( \tilde { \rho } \tilde { c } ) ~ )$

From the above discussion, we see that for each$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } .$, each$\tilde { P } _ { 0 } \in \tilde { \mathcal { P } } _ { T _ { \tilde { \rho } } } ^ { \prime \prime }$and each$x \in Y ^ { \prime \prime } ( \tilde { P } _ { 0 } )$，we have

$$
\sup _ {\tilde {P} \in ((\tilde {\mathcal {P}} _ {T _ {\tilde {\rho}}} ^ {\prime}) _ {Y ^ {\prime}} (x))} \angle \bigl (\Pi (\tilde {P} _ {0} ^ {T _ {\tilde {\rho}}}), \Pi (\tilde {P} ^ {T _ {\tilde {\rho}}}) \bigr) \gtrsim \nu^ {1 / 2} \tilde {a} / (\tilde {\rho} \tilde {c}),
$$

and thus

$$
\inf _ {x \in Y ^ {\prime \prime} (\tilde {P} _ {0})} \sup _ {\tilde {P} \in ((\tilde {\mathcal {P}} _ {T _ {\tilde {\rho}}} ^ {\prime}) _ {Y ^ {\prime}} (x))} \angle \bigl (\Pi (\tilde {P} _ {0} ^ {T _ {\tilde {\rho}}}), \Pi (\tilde {P} ^ {T _ {\tilde {\rho}}}) \bigr) \gtrsim \nu^ {1 / 2} \tilde {a} / (\tilde {\rho} \tilde {c}).
$$

But this is precisely the condition we need to apply Lemma 5.10 with$\lambda \approx _ { \delta } \delta ^ { 4 \eta + 4 \varepsilon _ { 1 } }$. Let${ \tilde { \mathcal { P } } } ^ { \prime \prime \prime }$be the set of those prisms$\tilde { P } _ { 0 } \in \tilde { \mathcal { P } } ^ { \prime \prime }$satisfying$| Y ^ { \prime \prime } ( \tilde { P } _ { 0 } ) | \gtrapprox \delta ~ \delta ^ { 4 \eta + 4 \varepsilon _ { 1 } }$. Undoing the scaling, we conclude that for each$\tilde { P } _ { 0 } \in \mathcal { P } ^ { \prime \prime \prime }$we have

$$
\left| N _ {\nu^ {1 / 2} \tilde {a}} (\tilde {P} _ {0}) \cap \bigcup_ {\tilde {P} \in \tilde {\mathcal {P}}} Y (\tilde {P}) \right| \gtrsim_ {\delta} ^ {\geqslant} \delta^ {1 6 \eta + 1 6 \varepsilon_ {1}} | N _ {\nu^ {1 / 2} \tilde {a}} (\tilde {P} _ {0}) |.\tag{8.20}
$$

But this means that after refining$( \mathbb { T } _ { 4 } , Y _ { 4 } ) _ { \delta }$by an${ \approx } _ { \delta }$1 factor, there is a pair$( \mathbb { T } _ { 4 } ^ { \prime } , Y _ { 4 } ^ { \prime } ) _ { \delta }$so that for each$x \in \bigcup _ { T \in \mathbb { T } _ { 4 } ^ { \prime } } Y _ { 4 } ^ { \prime } ( T )$, we have

$$
\left| B (x, \nu^ {1 / 2} \tilde {a}) \cap \bigcup_ {T \in \mathbb {T}} Y (T) \right| \gtrsim_ {\delta} \delta^ {O (\eta + \varepsilon_ {1})} | B (x, \nu^ {1 / 2} \tilde {a}) |.\tag{8.21}
$$

By Corollary 5.19 (and using (8.19)), we conclude that Conclusion (A) holds, provided$\alpha \leq \omega \varepsilon _ { 2 } / 2$ and provided$\varepsilon _ { 1 }$and η are selected suficiently small (depending on$\omega , \varepsilon _ { 2 }$, and the implicit constant on the RHS of (8.21)).

Finally, we will consider the case where (8.19) fails, i.e.

$$
\nu \leq \delta^ {- \varepsilon_ {2}}.\tag{8.22}
$$

This means that for each$T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } .$, the sets$\{ Y ^ { \prime \prime } ( \tilde { P } ) \colon \tilde { P } \in ( \tilde { \mathcal { P } } ^ { \prime \prime } ) _ { T _ { \tilde { \rho } } } \}$are$\leq \delta ^ { - \varepsilon _ { 2 } }$overlapping. By pigeonholing, we can select a refinement$( \tilde { \mathcal { P } } _ { 5 } , Y _ { 5 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$of$( \tilde { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { \tilde { a } \times \tilde { \rho } \tilde { c } \times \tilde { c } }$satisfying the four Items listed in Step 7.□

## 8.3 Move #3: Replacing grains with wider grains with small$C _ { K T - C W } ^ { \mathrm { l o c } }$

Lemma 8.3. We assume the Common setup for Moves #1, #2, #3: Hypotheses from Section 7.4. Then at least one of the following must hold.

Suppose that$\mathcal { E } ( \pmb { \sigma } , \omega )$is true and let$\varepsilon > 0$. Then there exists$\alpha , \eta , c > 0$so that the following holds for all$0 < \delta \leq \rho \leq 1$, and all$\delta \leq a \leq b \leq c$with$b / c = \rho$

Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, with$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Let$\mathbb { T } _ { \rho }$be a balanced partitioning cover$o f \mathbb { T }$, and suppose that$( \mathbb { T } , Y ) _ { \delta }$is broad with error$\delta ^ { - \eta }$relative to$\mathbb { T } _ { \rho }$. Let$( { \mathcal { P } } , Y ) _ { a \times b \times c }$ be a robustly δ<sup>η</sup>-dense two-scale grains decomposition of$( \mathbb { T } , Y ) _ { \delta }$wrt$\mathbb { T } _ { \rho }$

Then at least one of the following must hold.

(A) Conclusion (A) of the common setup for Moves$\# 1 , \# 2 , \# 3 .$

(B) Conclusion (B) of the common setup for Moves$\# 1 , \# 2 , \# 3$. In addition,

(iv)$C _ { K T - C W } ^ { \mathrm { l o c } } ( \mathcal { P } ^ { \prime } ) \leq \delta ^ { - \zeta } .$

(C) Conclusion (C) of the common setup for Moves$\# 1 , \# 2 , \# 3 .$In addition,

$$
(v) \tilde {c} \geq c, \delta^ {- \zeta / 4 0 0} \rho \leq \tilde {\rho} \leq 1.
$$

Proof. Step 1. Let$0 < \varepsilon _ { 1 } < \cdots < \varepsilon _ { 4 }$be small quantities to be chosen below. We will choose$\varepsilon _ { i }$ very small compared to$\varepsilon _ { i + 1 }$for each$i = 1 , \ldots , 3 ;$we will choose$\varepsilon _ { 4 }$very small compared to$\varepsilon ;$we will choose$\alpha , \eta$very small compared to$\varepsilon _ { 1 }$.

First, we may suppose that

$$
a \leq \delta^ {1 - \varepsilon_ {1}},\tag{8.23}
$$

or else Conclusion (A) immediately holds, provided we choose α and$\eta$suficiently small depending on$\varepsilon _ { 1 }$. The argument is identical to the argument in Step 1 of the proof of Lemma 8.2.

Next we will regularize the set T. By dyadic pigeonholing and replacing$( \mathbb { T } , Y ) _ { \delta }$by a$\gtrsim$ $( \log 1 / \delta ) ^ { - 1 / \varepsilon _ { 1 } }$refinement$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$, we can suppose that

(a) For each scale of the form$\tau _ { i } = \delta ^ { \varepsilon _ { 1 } i } , i = 1 , \dots , \varepsilon _ { 1 } ^ { - 1 }$, there exists a “density”$\lambda _ { i }$so that

$$
\left| B (x, \tau_ {i}) \cap \bigcup_ {T \in \mathbb {T}} Y (T) \right| \sim \lambda_ {i} | B (x, \tau_ {i}) | \quad \text { for   every } x \in \bigcup_ {T \in \mathbb {T} _ {1}} Y _ {1} (T).\tag{8.24}
$$

(b) For each$i = 1 , \ldots , \varepsilon _ { 1 } ^ { - 1 }$, there is a pair$( \mathbb { T } _ { \tau _ { i } } , Y _ { \tau _ { i } } ) _ { \tau _ { i } }$that is${ \gtrap{ \approx } } \delta ^ { \ n }$dense. Furthermore,$\mathbb { T } _ { \tau _ { i } }$is a balanced partitioning cover of$\mathbb { T } _ { 1 } ;$and for each$T _ { \tau _ { i } }$we have

$$
Y _ {\tau_ {i}} (T _ {\tau_ {i}}) \subset T _ {\tau_ {i}} \cap \bigcup_ {T \in \mathbb {T} _ {1}} N _ {\tau_ {i}} (Y _ {1} (T)).
$$

From the above items, we have that$C _ { F - S W } ( \mathbb { T } _ { \tau _ { i } } ) \lesssim C _ { F - S W } ( \mathbb { T } _ { 1 } ) \lesssim ( \log { 1 / \delta } ) ^ { - 1 / \varepsilon _ { 1 } } \delta ^ { - \eta }$, and

$$
C _ {K T - C W} (\mathbb {T} _ {\tau_ {i}}) \lesssim C _ {K T - C W} (\mathbb {T} _ {1}) \frac {\# \mathbb {T} _ {\tau_ {i}}}{\# \mathbb {T} _ {1}} \frac {| T _ {\tau_ {i}} |}{| T |}.
$$

If$\eta > 0$is selected suficiently small depending on$\varepsilon _ { 1 }$, then we can apply the estimate$\mathcal { E } ( \pmb { \sigma } , \omega )$(with $\varepsilon _ { 1 }$in place of ε) to conclude that

$$
\begin{array}{r l} & {\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \delta^ {2 \varepsilon_ {1}} \lambda_ {i} \tau_ {i} ^ {\omega} C _ {K T - C W} (\mathbb {T} _ {\tau_ {i}}) ^ {- 1} (\# \mathbb {T} _ {\tau_ {i}}) | T _ {\tau_ {i}} | \Big (C _ {K T - C W} (\mathbb {T} _ {\tau_ {i}}) ^ {- 3 / 2} C _ {F - S W} (\mathbb {T} _ {\tau_ {i}}) (\# \mathbb {T} _ {\tau_ {i}}) | T _ {\tau_ {i}} | ^ {1 / 2} \Big) ^ {- \sigma}} \\ & {\qquad \gtrsim_ {\delta} \delta^ {2 \varepsilon_ {1} + O (\eta)} \Big [ \lambda_ {i} \Big (\frac {\tau_ {i}}{\delta} \Big) ^ {\omega} \Big (\frac {| T _ {\tau_ {i}} | (\# \mathbb {T} _ {\tau_ {i}}) ^ {1 / 2}}{| T | (\# \mathbb {T}) ^ {1 / 2}} \Big) ^ {\sigma} \Big ] \delta^ {\omega} (\# \mathbb {T}) | T | \Big ((\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma}} \\ & {\qquad \gtrsim \delta^ {3 \varepsilon_ {1}} \Big [ \lambda_ {i} \Big (\frac {\tau_ {i}}{\delta} \Big) ^ {\omega} \frac {| T _ {\tau_ {i}} | ^ {\sigma / 2}}{| T | ^ {\sigma / 2}} \Big ] \delta^ {\omega} (\# \mathbb {T}) | T | \Big ((\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma}.} \end{array}\tag{8.25}
$$

For the last inequality, we used the fact that$C _ { K T - C W } ( \mathbb { T } _ { 1 } ) \ \underset { \approx } { \lessapprox } \delta ^ { - \eta }$, and so$( \# \mathbb { T } ) / ( \# \mathbb { T } _ { \tau _ { i } } ) \ \lessapprox \delta$ $\delta ^ { - \eta } \vert T _ { \tau _ { i } } \vert / \vert T \vert$. In particular, if there is an index i for which$\lambda _ { i } \bigg ( \frac { \tau _ { i } } { \delta } \bigg ) ^ { \omega } \frac { | T _ { \tau _ { i } } | ^ { \sigma / 2 } } { | T | ^ { \sigma / 2 } }$is substantially larger than 1, then we will obtain Conclusion (A) of Lemma 8.3.

Step 2. Let$\mathcal { P } _ { 1 } = \mathcal { P }$. For each$P \in { \mathcal { P } } _ { 1 }$, define$Y _ { 1 } ( P ) = Y ( P ) \cap \bigcup _ { T \in \mathbb { T } _ { 1 } [ T _ { o } ] } Y _ { 1 } ( T )$, where$T _ { \rho } \in \mathbb { T } _ { \rho }$is the unique$\rho$tube with$P \in T _ { \rho }$and$\angle ( \mathrm { d i r } ( P ) , \mathrm { d i r } ( T _ { \rho } ) ) \leq 2 \rho \quad$. Since$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$is an$\approx _ { \delta }$1 refinement of$( \mathbb { T } , Y ) _ { \delta } .$, by Definition 7.1 Items (ii) and (iii) we have that$( { \mathcal { P } } _ { 1 } , Y _ { 1 } ) _ { a \times b \times c }$is$\mathrm { a } \approx _ { \delta } 1$refinement of $( { \mathcal { P } } , Y ) _ { a \times b \times c }$

Apply Lemma 5.9 (every shading has a regular sub-shading) to each shading$Y _ { 1 } ( P ) , P \in \mathcal { P } _ { 1 }$ This gives us a regular sub-shading$Y _ { 2 } ( P ) \subset Y _ { 1 } ( P )$. Let$\mathcal { P } _ { 2 } ~ \subset ~ \mathcal { P } _ { 1 }$be those prisms for which $| Y _ { 2 } ( P ) | \geq \delta ^ { 2 \eta } | P | ;$; we have that$( \mathcal { P } _ { 2 } , Y _ { 2 } ) _ { a \times b \times c }$is a$\gtrsim 1$refinement of$( { \mathcal { P } } _ { 1 } , Y _ { 1 } ) _ { a \times b \times c }$

Let$\mathcal { P } _ { 3 } = \mathcal { P } _ { 2 }$. By dyadic pigeonholing, we can select a number$\theta _ { 0 } \in \left[ \frac { a } { b } , 1 \right]$and a$( \log 1 / \delta ) ^ { - 1 }$ refinement$( { \mathcal { P } } _ { 3 } , Y _ { 3 } ) _ { a \times b \times c } { \mathrm { ~ o f ~ } } ( { \mathcal { P } } _ { 2 } , Y _ { 2 } ) _ { a \times b \times c }$so that for each$x \in \bigcup _ { P \in \mathcal { P } _ { 3 } } Y _ { 3 } ( P )$, we have$\theta ( x ) \sim \theta _ { 0 }$ where$\theta ( x )$is as defined in Definition 5.12.

We first consider the case where$\theta _ { 0 } \geq \delta ^ { - \varepsilon _ { 1 } } ( a / b )$. Our goal is to show that Conclusion (A) holds. Let$\mathcal { P } _ { 3 } ^ { \prime } \subset \mathcal { P } _ { 3 }$be the set of those prisms for which$\begin{array} { r } { | Y _ { 3 } ( P _ { 0 } ) | \ge \frac { 1 } { 1 0 0 } \delta ^ { 2 \eta } | P _ { 0 } | } \end{array}$. Then for each$x \in Y _ { 3 } ( P _ { 0 } )$ we have

$$
\frac {a}{b} + \sup _ {P \in \mathcal {P} _ {2}} \angle (\Pi (P _ {0}), \Pi (P)) \gtrsim \theta_ {0}.
$$

We have$\begin{array} { r } { | Y _ { 3 } ( P _ { 0 } ) | \ge \frac { 1 } { 1 0 0 } \delta ^ { 2 \eta } | P _ { 0 } | ; } \end{array}$each$P \in \mathcal { P } _ { 2 }$satisfies$\begin{array} { r } { | Y _ { 2 } ( P ) | \ge \frac { 1 } { 1 0 0 } \delta ^ { 2 \eta } | P _ { 0 } | ; } \end{array}$and$Y _ { 2 } ( P )$is regular. Thus we can apply Lemma 5.10 (with$Y _ { 3 } ( P _ { 0 } )$in place of$Y _ { 0 } ( P _ { 0 } )$and$( { \mathcal { P } } _ { 2 } , Y _ { 2 } ) _ { a \times b \times c }$in place of $( \mathcal { P } , Y ) _ { a \times b \times c }$to conclude that

$$
\left| N _ {b \theta_ {0}} (P _ {0}) \cap \bigcup_ {P \in \mathcal {P}} Y (P) \right| \gtrsim_ {\delta} \delta^ {8 \eta} | N _ {b \theta} (P _ {0}) |.\tag{8.26}
$$

Recall that (8.26) holds for each$P _ { 0 } \in \mathcal { P } _ { 3 } ^ { \prime }$, and$( \mathcal { P } _ { 3 } ^ { \prime } , Y _ { 3 } ) _ { a \times b \times c }$is a$\gtrapprox \delta ~ 1$refinement of$( { \mathcal { P } } , Y ) _ { a \times b \times c }$ After replacing$( \mathcal { P } _ { 3 } ^ { \prime } , Y _ { 3 } ) _ { a \times b \times c }$by a further$\sim 1$refinement$( \mathcal { P } _ { 3 } ^ { \prime } , Y _ { 3 } ^ { \prime } ) _ { a \times b \times c } ,$we can suppose that for each$x \in \bigcup _ { P \in { \mathcal { P } } _ { 3 } ^ { \prime } } Y _ { 3 } ^ { \prime }$, we have

$$
\left| N _ {b \theta_ {0}} (x) \cap \bigcup_ {P \in \mathcal {P}} Y (P) \right| \gtrsim_ {\delta} \delta^ {8 \eta} | N _ {b \theta_ {0}} (x) |.
$$

Finally, if$( \mathbb { T } _ { 1 } , Y _ { 1 } ^ { \prime } ) _ { \delta }$is the refinement of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$induced by$( \mathcal { P } _ { 3 } ^ { \prime } , Y _ { 3 } ^ { \prime } ) _ { a \times b \times c }$, then by Definition 7.1, Item (ii),$( \mathbb { T } _ { 1 } , Y _ { 1 } ^ { \prime } ) _ { \delta }$is$\mathrm { ~ a ~ } \approx \delta$1-refinement of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$, and for each$x \in \mathsf { U } _ { T \in \mathbb { T } _ { 1 } ^ { \prime } } Y _ { 1 } ^ { \prime } ( T )$we have

$$
\left| N _ {b \theta_ {0}} (x) \cap \bigcup_ {T \in \mathbb {T} _ {1} ^ {\prime}} Y (T) \right| \gtrsim_ {\delta} \delta^ {8 \eta} | N _ {b \theta_ {0}} (x) |.\tag{8.27}
$$

Since$b \theta _ { 0 } \geq \delta ^ { - \varepsilon _ { 1 } } a .$, by Corollary 5.19 we see that Conclusion (A) holds, provided we select$\eta > 0$ suficiently small depending on$\varepsilon _ { 1 }$, and select$\alpha \leq \varepsilon _ { 1 } \omega / 2$

Henceforth we shall suppose that$\theta _ { 0 } \leq \delta ^ { - \varepsilon _ { 1 } } ( a / b )$, i.e.

$$
\sup _ {x} \sup _ {P, P ^ {\prime} \in (\mathcal {P} _ {3}) _ {Y _ {3}} (x)} \angle \bigl (\Pi (P), \Pi (P ^ {\prime}) \bigr) \leq \delta^ {- \varepsilon_ {1}} (a / b).\tag{8.28}
$$

Step 3. Recall the discussion following Definition 7.3 (the quantity$^ { 6 6 }$in that discussion is $\delta ^ { - \varepsilon _ { 1 } }$in this context); after replacing$( \mathcal { P } _ { 3 } , Y _ { 3 } ) _ { a \times b \times c }$by$\mathrm { ~ a ~ } \sim 1$refinement, which we will denote by $( { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { a \times b \times c }$(which in turn induces$\mathrm { ~ a ~ } \sim 1$refinement$( \mathbb { T } _ { 4 } , Y _ { 4 } ) _ { \delta }$of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta } )$, we can find a set U of pairwise distinct prisms of dimensions$\delta ^ { - \varepsilon _ { 1 } } { \frac { a c } { b } } \times c \times c$so that the following holds.

(a) The sets$\{ { \mathcal { P } } _ { 4 } \langle U \rangle : U \in { \mathcal { U } } \}$are a partition of$\mathcal { P } _ { 4 }$

(b) The sets$\{ \bigcup _ { P \in { \mathcal { P } } _ { 4 } \langle U \rangle } Y _ { 4 } ( P ) \colon U \in { \mathcal { U } } \}$are disjoint.

Each$U \in \mathcal { U }$is a prism of dimensions$\delta ^ { - \varepsilon _ { 1 } } \frac { a c } { b } \times c \times c = \delta ^ { - \varepsilon _ { 1 } } \frac { a } { \rho } \times c \times c$. Thus for each$U \in \mathcal { U }$ there is a set$\{ Z \}$of$\lesssim \delta ^ { - 3 \varepsilon _ { 1 } }$prisms of dimensions comparable to${ \frac { a } { \rho } } \times c \times c$with the property that for each$P \in { \mathcal { P } } _ { 4 } \langle U \rangle$, there is a prism$Z$from this collection with$\boxed { \ d } ( P ) \subset Z$(recall that$\rho = b / c ,$ and thus$\boxed { \ d } ( P )$is a prism of dimensions comparable to$\textstyle { \frac { a } { \rho } } \times c \times c )$

Let$Z _ { U }$be a prism of dimensions comparable to$\begin{array} { l } { \displaystyle { \frac { a } { \rho } } \times c \times c } \end{array}$that maximizes

$$
\# \{P \in \mathcal {P} _ {4} \colon \square (P) \subset Z \},
$$

so in particular #${ \langle } { \mathcal { P } _ { 4 } \langle Z _ { U } \rangle } \gtrsim \delta ^ { 3 \varepsilon _ { 1 } } ( \# \mathcal { P } _ { 4 } \langle U \rangle )$. Let$\mathcal { Z } = \{ Z _ { U } : U \in \mathcal { U } \}$; let$\begin{array} { r } { \mathcal { P } _ { 5 } = \bigcup _ { U \in \mathcal { U } } \mathcal { P } _ { 4 } \langle Z _ { U } \rangle } \end{array}$; and let $Y _ { 5 }$be the restriction of$Y _ { 4 }$to${ \mathcal { P } } _ { 5 }$. Then$( { \mathcal { P } } _ { 5 } , Y _ { 5 } ) _ { a \times b \times c }$is a$\iota \gtrsim \delta ^ { 3 \varepsilon _ { 1 } }$refinement of$( { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { a \times b \times c : }$and we have the following analogue of Items (a) and (b).

(a<sup>′</sup>) The sets$\{ { \mathcal { P } } _ { 4 } \langle Z \rangle : Z \in { \mathcal { Z } } \}$become a partition of${ \mathcal { P } } _ { 5 }$.

(b<sup>′</sup>) The sets$\{ \cup _ { P \in { \mathcal { P } } _ { 5 } \langle Z \rangle } Y _ { 5 } ( P ) \colon Z \in { \mathcal { Z } } \}$are disjoint.

For each$Z \in { \mathcal { Z } }$, the sets in$( \mathcal { P } _ { 5 } \langle Z \rangle ) ^ { Z }$are convex sets of dimensions comparable to$\rho \times \rho \times 1$ i.e. the sets are comparable to$\rho$tubes. To record this useful fact, we will define$( { \tilde { \mathbb { T } } } _ { Z } , { \tilde { Y } } _ { 5 } ) _ { \rho } =$ $( ( \mathcal { P } _ { 5 } \langle Z \rangle ) ^ { Z } , Y _ { 5 } ^ { Z } ) _ { \rho \times \rho \times 1 }$

After replacing$( { \mathcal { P } } _ { 5 } , Y _ { 5 } ) _ { a \times b \times c }$and$\mathcal { Z }$with$\approx _ { \delta }$1 refinements, we may suppose that each set$\tilde { \mathbb { T } } _ { Z }$ has approximately the same size (up to a factor of 2) for each$Z \in { \mathcal { Z } }$, and similarly each set $| \tilde { Y } _ { 5 } ( \tilde { T } )$has approximately the same size for each$\tilde { T } \in \tilde { \mathbb { T } } _ { Z }$. Furthermore, we can suppose that each pair$( { \tilde { \mathbb { T } } } _ { Z } , { \tilde { Y } } _ { 5 } ) _ { \rho } { \mathrm { ~ i s ~ } } \gtrapprox \delta \ \delta \eta$dense (indeed, recall that$( { \mathcal { P } } , Y ) _ { a \times b \times c }$is$\delta ^ { \eta }$dense;$( { \mathcal { P } } _ { 4 } , Y _ { 4 } ) _ { a \times b \times c }$is a $\gtrapprox \delta$1-refinement of$( \mathcal { P } , Y ) _ { a \times b \times c } ;$and$( { \mathcal { P } } _ { 5 } \langle Z \rangle , Y _ { 5 } ) _ { a \times b \times c }$is$\mathrm { a } \approx _ { \delta } 1$refinement of$( \mathcal { P } _ { 4 } \langle Z \rangle , Y _ { 4 } ) _ { a \times b \times c } )$

Step 4. For notational convenience, we will fix a prism$Z \in { \mathcal { Z } }$. In what follows, we will find certain quantities (for example certain scales, multiplicities, etc.), and navigate between diferent cases depending on the specifics of the arrangement$\tilde { \mathbb { T } } _ { Z }$. However, by pigeonholing the set$\mathcal { Z } ,$we may suppose that all quantities described below are the same (up to a factor of 2) for each$Z \in { \mathcal { Z } }$ and thus the same cases occur for each$Z \in { \mathcal { Z } }$

Apply Proposition 4.6 (factoring convex sets) to$\tilde { \mathbb { T } } _ { Z }$. We obtain a number$m \geq 1$; a${ \approx } _ { \delta }$1 refinement$\tilde { \mathbb { T } } _ { Z } ^ { \prime }$of$\tilde { \mathbb { T } } _ { Z } .$, and a partitioning cover$\mathcal { W } _ { Z }$of$\tilde { \mathbb { T } } _ { Z } ^ { \prime }$consisting of congruent prisms; we shall denote the dimensions of these prisms by$s \times t \times 1$(since each prism contains at least one tube, we know that the longest dimension is$\sim 1 )$. We have that$\mathcal { W } _ { Z }$factors$\tilde { \mathbb { T } } _ { Z } ^ { \prime }$from below with respect to the Frostman Convex Wolf Axioms, and from above with respect to the Katz-Tao Convex Wolf Axioms, both with error$\lessapprox \delta { \mathrm { ~ 1 ~ } }$. Finally,

$$
C _ {K T - C W} (\tilde {\mathbb {T}} _ {Z} ^ {\prime}) \leq m, \quad \text { and } \quad \# \tilde {\mathbb {T}} _ {Z} ^ {\prime} [ W ] \approx_ {\delta} m \frac {| W |}{| \tilde {T} |} \quad \text { for   each } W \in \mathcal {W} _ {Z}.\tag{8.29}
$$

We first consider the case where

$$
m \leq \delta^ {- \zeta}.\tag{8.30}
$$

Our goal is to show that Conclusion (B) of Lemma 8.3 holds.

As described at the beginning of Step 4, we can suppose that (8.30) is true for at least half the prisms$Z \in { \mathcal { Z } }$. Let$\mathcal { P } _ { 6 } \subset \mathcal { P } _ { 5 }$be given by$\begin{array} { r } { \mathcal { P } _ { 6 } = \bigcup _ { Z } \phi _ { Z } ^ { - 1 } ( \tilde { \mathbb { T } } _ { Z } ^ { \prime } ) } \end{array}$, where the union is taken over those prisms in$\mathcal { Z }$for which$( 8 . 3 0 )$holds (note that$\mathcal { P } _ { 6 } \subset \mathcal { P } _ { 5 }$, since each tube in$\tilde { \mathbb { T } } _ { Z } ^ { \prime } \subset \tilde { \mathbb { T } } _ { Z }$is the image of a prism from${ \mathcal { P } } _ { 5 }$under the map$\phi _ { Z } )$. Let$Y _ { 6 }$be the restriction of$Y _ { 5 }$to${ \mathcal { P } } _ { 6 }$

We have that$( { \mathcal { P } } _ { 6 } , Y _ { 6 } ) _ { a \times b \times c }$is a$\gtrapprox \delta ~ 1$refinement of$( \mathcal { P } _ { 5 } , Y _ { 5 } )$. Undoing the scaling$\phi _ { Z }$, we have that for each$P \in \mathcal { P } _ { 6 }$2

$$
C _ {K T - C W} \big (\mathcal {P} _ {6} \langle 2 \Box (P) \rangle \big) \lesssim \sup _ {Z \in \mathcal {Z}} C _ {K T - C W} (\mathcal {P} _ {6} \langle Z \rangle) \leq m.
$$

We conclude that

$$
C _ {K T - C W} ^ {\mathrm{loc}} (\mathcal {P} _ {6}) \lesssim m.
$$

Applying a final dyadic pigeonholing, we can select$\mathrm { a } \approx _ { \delta }$1 refinement$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times c }$of$( { \mathcal { P } } _ { 6 } , Y _ { 6 } ) _ { a \times b \times c }$ (this in turn induces a$\stackrel { > } { \approx } \delta ^ { 3 \varepsilon _ { 1 } }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$of$( \mathbb { T } _ { 4 } , Y _ { 4 } ) _ { \delta } )$and a set$\mathbb { T } _ { \rho } ^ { \prime } \subset \mathbb { T } _ { \rho }$so that the following holds:$\mathbb { T } _ { \rho } ^ { \prime }$is a balanced partitioning cover of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$, and$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times c }$is a robustly ${ \approx } _ { \delta } \delta ^ { 3 \varepsilon _ { 1 } }$-dense two-scale grains decomposition of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$wrt$\mathbb { T } _ { \rho } ^ { \prime } .$

Since$C _ { K T - C W } ^ { \mathrm { l o c } } ( \mathcal { P } ^ { \prime } ) \ \stackrel { < } { \sim } \ m$, Conclusion (B), Item (iv) of Lemma 8.3 is satisfied.$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times c }$ satisfies Conclusion (B), Item (iii) by construction.$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$satisfies Conclusion (B), Item (i), provided$\varepsilon _ { 1 }$is chosen suficiently small depending on ε. Finally, since

$$
\# \big (\mathbb {T} ^ {\prime} [ T _ {\rho} ] _ {Y ^ {\prime}} (x) \big) \gtrsim_ {\delta} \delta^ {3 \varepsilon_ {1}} \# (\mathbb {T} [ T _ {\rho} ]) _ {Y} (x) \quad \text {for every} T _ {\rho} \in \mathbb {T} _ {\rho} ^ {\prime} \text {and every} x \in \bigcup_ {T \in \mathbb {T} ^ {\prime} [ T _ {\rho} ]} Y ^ {\prime} (T),
$$

and since (by hypothesis)$( \mathbb { T } , Y ) _ { \delta }$is broad with error$\delta ^ { - \eta }$relative to$\mathbb { T } _ { \rho } .$we conclude that$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$ is broad with error$\lesssim \delta ^ { - \eta - 3 \varepsilon _ { 1 } }$relative to$\mathbb { T } _ { \rho } ^ { \prime }$. We will select η and$\varepsilon _ { 1 }$suficiently small so that this quantity$\mathrm { i s } \le \delta ^ { - \varepsilon }$. This verifies Conclusion (B), Item$( \mathrm { i i } ) ^ { \mathrm { ~ 3 ~ } }$

In summary, if (8.30) holds, then Conclusion (B) of Lemma 8.3 is satisfied. Henceforth we will suppose that (8.30) fails, i.e.

$$
m > \delta^ {- \zeta}.\tag{8.31}
$$

Step 5. In Step 4, we fixed a choice of prism$Z \in { \mathcal { Z } }$. We will continue to fix this choice of$Z ,$, and in additional we will fix a choice of$W \in \mathcal { W } _ { Z }$. As in Step 4, we can assume (by dyadic pigeonholing) that all relevant scales, multiplicities, etc. are approximately the same (up to a factor of 2) for each $Z \in { \mathcal { Z } }$and each$W \in \mathcal { W } _ { Z } )$.

In the arguments that follow, we will analyze the pairs$( \tilde { \mathbb { T } } _ { Z } ^ { \prime } [ W ] , \tilde { Y } _ { 5 } ) _ { \rho }$constructed in Step 4. For notational convenience, we will refer to such a pair as$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho }$. Recall that this pair is${ \gtrap{ \approx } } \delta ^ { \ J }$dense; the cardinality of$\tilde { \mathbb { T } }$is given by (8.29); and m satisfies (8.31). In particular, we have

$$
C _ {F - C W} (\tilde {\mathbb {T}} ^ {W}) \lesssim_ {\delta} 1.\tag{8.32}
$$

Apply Corollary 7.10 (finding a broad scale) to the set$\tilde { \mathbb { T } } .$Denote the “output” scale of this Corollary by$\tau$(in Corollary 7.10, this output scale is called$\rho ,$but that variable is already in use). Abusing notation, we will continue to use$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho }$to refer to the output of Corollary 7.10. Thus there is a set$\mathbb { T } _ { \tau }$that forms a balanced partitioning cover of$\tilde { \mathbb { T } } _ { : }$, and$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho }$is broad with error$\lessapprox$1 relative to$\mathbb { T } _ { \tau }$. Furthermore,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">⪆</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">≤ δ<sup>−ε</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">δ > 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">κ > 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>To be precise, we can only ensure that the error is provided  is suficiently small, depending on the implicit constant in the above notation. However if this fails then Conclusion (A) holds, provided we select suficiently small.</span></small>

$$
\text { the   sets } \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}} [ T _ {\tau} ]} \tilde {Y} (\tilde {T}), \quad T _ {\tau} \in \mathbb {T} _ {\tau} \quad \text { are } \lesssim \tau^ {- \beta} \text { overlapping. }\tag{8.33}
$$

We claim that

$$
\tau \geq \rho^ {1 - \omega / 8},\tag{8.34}
$$

or else Conclusion$\mathrm { ( A ) }$of Lemma 8.3 holds, and we are done. To verify this claim, note that if (8.34) failed, then the sets$\{ \tilde { Y } ( \tilde { T } ) \colon \tilde { T } \in \tilde { \mathbb { T } } \}$are$\lesssim \rho ^ { - \omega / 4 } \tau ^ { - \beta } \leq \delta ^ { - \omega / 2 }$overlapping; but this fact, combined with Item$\mathrm { ( b ^ { \prime } ) }$from Step 3, gives Conclusion$\mathrm { ( A ) }$of Lemma 8.3.

Step 6. We would like to apply the estimate$\mathcal { E } ( \pmb { \sigma } , \omega )$to each set$( \tilde { \mathbb { T } } ^ { T _ { \tau } } , \tilde { Y } ^ { T _ { \tau } } ) _ { \rho / \tau }$. However, we do not currently have a good estimate for$C _ { F - S W } ( \tilde { \mathbb { T } } ^ { T _ { \tau } } )$. To fix this problem, apply Proposition 4.8 (factoring convex sets with respect to the Frostman Slab Wolf Axioms) to each set$( \tilde { \mathbb { T } } [ T _ { \tau } ] , \tilde { Y } ) _ { \rho } ,$ with$\varepsilon _ { 2 }$in place of$\varepsilon .$. We can do${ \mathrm { s o } } ,$provided$\varepsilon _ { 1 }$and η is selected suficiently small compared to$\varepsilon _ { 2 }$ This gives us a$\stackrel { > } { \approx } \delta ^ { \varepsilon _ { 2 } }$refinement$( \tilde { \mathbb { T } } ^ { \prime } [ T _ { \tau } ] , \tilde { Y } ^ { \prime } ) _ { \rho }$of$( \tilde { \mathbb { T } } [ T _ { \tau } ] , \tilde { Y } ) _ { \rho } ,$and a family of convex subsets of$T _ { \tau }$ which we denote by$\left. \nu _ { T _ { \tau } } \right.$, that factors$\tilde { \mathbb { T } } ^ { \prime } [ T _ { \tau } ]$from below with respect to the Frostman Slab Wolf Axioms with error$\delta ^ { - \varepsilon _ { 2 } }$. In addition,

$$
\text { the   sets } \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}} ^ {\prime} [ V ]} \tilde {Y} ^ {\prime} (\tilde {T}), \quad V \in \mathcal {V} _ {T _ {\tau}} \quad \text { are   disjoint. }\tag{8.35}
$$

After pigeonholing, we may suppose that the sets in$\nu _ { T _ { \tau } }$have the same dimensions, and furthermore these dimensions are common across all$T _ { \tau } \in \mathbb { T } _ { \tau }$. Denote these dimensions$\theta \times \tau ^ { \prime } \times 1$ Since$V \subset T _ { \tau }$, we must have$\tau ^ { \prime } \leq \tau$. We claim that this inequality is almost tight, in the sense that

$$
\delta^ {\varepsilon_ {2} / \beta} \tau \lesssim_ {\delta} \tau^ {\prime} \leq \tau .\tag{8.36}
$$

To verify this claim, note that$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho }$is broad with error$\lessapprox$1 relative to the cover$\mathbb { T } _ { \tau }$. Since $( \tilde { \mathbb { T } } ^ { \prime } [ T _ { \tau } ] , \tilde { Y } ^ { \prime } ) _ { \rho }$is$\mathrm { ~ a ~ } \gtrapprox _ { \delta } \delta ^ { \varepsilon _ { 2 } }$refinement of$( \tilde { \mathbb { T } } [ T _ { \tau } ] , \tilde { Y } ) _ { \rho } .$, by pigeonholing there is at least one point x for which the tubes in$\tilde { \mathbb { T } } _ { Y ^ { \prime } } ^ { \prime } ( x )$point in directions that are broad with error$\stackrel { < } { \approx } \delta \stackrel { \delta - \varepsilon _ { 2 } } { }$inside a cap of radius$\tau .$. This means that there are at least two tubes from this set that make an angle$\stackrel { > } { \approx } \delta ^ { \varepsilon _ { 2 } / \beta } \tau$ On the other hand, by (8.35) we have that the pair of tubes described above must be contained in a common$\theta \times \tau ^ { \prime } \times 1$prism. This establishes (8.36).

Let$\widetilde { \mathbb { T } } ^ { \prime }$be the union of the sets$\tilde { \mathbb { T } } ^ { \prime } [ T _ { \tau } ]$, as$T _ { \tau }$ranges over the elements of$\mathbb { T } _ { \tau }$. Let${ \tilde { Y } } ^ { \prime }$be the associated shading on$\widetilde { \mathbb { T } } ^ { \prime }$coming from the pairs$( \tilde { \mathbb { T } } ^ { \prime } [ T _ { \tau } ] , \tilde { Y } ^ { \prime } ) _ { \rho } .$. Abusing notation, we will rename this pair$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho }$. At this point in the argument, this pair is$\stackrel { { \bf \lambda } } { \approx } \delta ^ { \eta + \varepsilon _ { 2 } } \geq \delta ^ { 2 \varepsilon _ { 2 } }$dense.

Step 7. We first consider the case where the prisms$\nu _ { T _ { \tau } }$from Step 6 are almost tubes, in the sense that

$$
\theta \geq \delta^ {\zeta / 1 0} \tau^ {\prime}.\tag{8.37}
$$

If (8.37) is true, then each set$\tilde { \mathbb { T } } ^ { V }$consists of prisms of dimensions${ \frac { \rho } { \tau ^ { \prime } } } \times { \frac { \rho } { \theta } } \times 1$. The pair$( \tilde { \mathbb { T } } ^ { V } , \tilde { Y } ^ { V } ) _ { \rho / \tau ^ { \prime } \times \rho / \theta \times 1 }$ is$\gtrapprox \delta \ \delta ^ { 2 \varepsilon _ { 2 } }$dense. Let us suppose for the moment that

$$
\rho \leq \delta^ {\sqrt {\varepsilon} _ {2}}.\tag{8.38}
$$

If we select$\varepsilon _ { 2 }$suficiently small so that$\varepsilon _ { 2 } \ \leq \ { \frac { 1 } { 2 } } { \sqrt { \varepsilon } } _ { 2 } \beta \omega$, and hence$\begin{array} { r } { \frac { 8 \varepsilon _ { 2 } \beta } { \sqrt { \varepsilon } _ { 2 } \beta \omega - 8 \varepsilon _ { 2 } } \leq \frac { 1 6 \sqrt { \varepsilon } _ { 2 } } { \omega } } \end{array}$, then by (8.34) and (8.36), we have$\delta ^ { 2 \varepsilon _ { 2 } } \geq \left( { \frac { \rho } { \tau ^ { \prime } } } \right) ^ { \frac { 3 2 { \sqrt { \varepsilon _ { 2 } } } } { \omega } }$

Thus if$\varepsilon _ { 2 }$is chosen suficiently small compared to$\varepsilon _ { 3 }$and$\omega ,$and if (8.38) is true, then we can apply the estimate$\mathcal { F } ( \pmb { \sigma } , \omega )$(recall Definition 5.4 and Remark 5.6, Situation 3) to estimate the volume of each (rescaled) set$( \tilde { \mathbb { T } } ^ { V } , \tilde { Y } ^ { V } ) _ { \rho / \tau ^ { \prime } \times \rho / \theta \times 1 }$, with$\varepsilon _ { 3 }$in place of$\varepsilon$and$3 2 { \sqrt { \varepsilon _ { 2 } } } / \omega$in place of$\eta .$ This gives the estimate

$$
\Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}} [ V ]} \tilde {Y} ^ {V} (\tilde {T} ^ {V}) \Big | \gtrsim \delta^ {\varepsilon_ {3}} \Big (\frac {\rho}{\theta} \Big) ^ {\omega} \tilde {m} ^ {- 1} (\# \tilde {\mathbb {T}} [ V ]) | \tilde {T} ^ {V} | \Big (\tilde {m} ^ {- 3 / 2} \tilde {\ell} (\# \tilde {\mathbb {T}} [ V ]) | \tilde {T} ^ {V} | ^ {1 / 2} \Big) ^ {- \sigma},\tag{8.39}
$$

where we define

$$
\tilde {m} = C _ {K T - C W} (\tilde {\mathbb {T}} [ V ]) \leq C _ {K T - C W} (\tilde {\mathbb {T}}) \leq m \quad \text { and } \quad \tilde {\ell} = C _ {F - S W} (\tilde {\mathbb {T}} [ V ]) \lesssim \delta^ {- \varepsilon_ {2}}.\tag{8.40}
$$

(for the first inequality, we used (8.29)). On the other hand, if (8.38) is false, then (8.39) follows from the fact that the LHS of (8.39) is bounded below by the volume of a single shading$| \tilde { Y } ^ { V } ( T ^ { V } ) |$, and we can select a tube with volume

$$
| \tilde {Y} ^ {V} (T ^ {V}) | \gtrsim \delta^ {2 \varepsilon_ {2}} | T ^ {V} | = \delta^ {2 \varepsilon_ {2}} \frac {\rho^ {2}}{\tau^ {\prime} \theta} \geq \delta^ {2 \varepsilon_ {2}} \rho^ {2} \geq \delta^ {3 \varepsilon_ {2}} \geq \delta^ {\varepsilon_ {3}}.\tag{8.41}
$$

Since$\sigma \in ( 0 , 2 / 3 ]$, by Remark 5.5 and Remark 5.6, Situation$3 .$

$$
\tilde {m} ^ {- 1} (\# \tilde {\mathbb {T}} [ V ]) | \tilde {T} ^ {V} | \left(\tilde {m} ^ {- 3 / 2} \tilde {\ell} (\# \tilde {\mathbb {T}} [ V ]) | \tilde {T} ^ {V} | ^ {1 / 2}\right) ^ {- \sigma} \lesssim 1.\tag{8.42}
$$

Combining (8.41) and (8.42) establishes (8.39) in the case where (8.38) is false. We conclude that (8.39) holds, independently of whether (8.38) is true or false.

Undoing the scaling$\phi _ { V }$and substituting the values of ˜m and$\tilde { \ell }$from (8.40), we have

$$
\Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}} [ V ]} \tilde {Y} (\tilde {T}) \Big | \gtrsim \delta^ {2 \varepsilon_ {3}} \left(\frac {\rho}{\theta}\right) ^ {\omega} m ^ {- 1} (\# \tilde {\mathbb {T}} [ V ]) | \tilde {T} | \left(m ^ {- 3 / 2} (\# \tilde {\mathbb {T}} [ V ]) \frac {| \tilde {T} | ^ {1 / 2}}{| V | ^ {1 / 2}}\right) ^ {- \sigma}.\tag{8.43}
$$

By (8.33), (8.35) (recall that we have renamed${ \tilde { Y } } ^ { \prime }$as$\tilde { Y } )$, and (8.43), we have

$$
\begin{array}{r l} & {\Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}}} \tilde {Y} (\tilde {T}) \Big | \gtrsim \tau^ {\beta} \sum_ {T _ {\tau} \in \mathbb {T} _ {\tau}} \sum_ {V \in \mathcal {V} _ {T _ {\tau}}} \Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}} [ V ]} \tilde {Y} (\tilde {T}) \Big |} \\ & {\qquad \gtrsim \delta^ {2 \varepsilon_ {3} + \beta} \Big (\frac {\rho}{\theta} \Big) ^ {\omega} m ^ {- 1} (\# \tilde {\mathbb {T}}) | \tilde {T} | \Big (m ^ {- 3 / 2} (\# \tilde {\mathbb {T}} [ V ]) \frac {| \tilde {T} | ^ {1 / 2}}{| V | ^ {1 / 2}} \Big) ^ {- \sigma}.} \end{array}\tag{8.44}
$$

Next, by (8.32) and using the fact that$( \tilde { \mathbb { T } } ^ { \prime } [ T _ { \tau } ] , Y ^ { \prime } ) _ { \rho }$is$\mathrm { a } \ \gtrapprox \delta ^ { \varepsilon _ { 2 } }$refinement of$( \mathbb { T } [ T _ { \tau } ] , { \tilde { Y } } ) _ { \rho }$, we have that$C _ { F - C W } ( \tilde { \mathbb { T } } ^ { W } ) \lesssim _ { \delta } \delta ^ { - 2 \varepsilon _ { 2 } }$. By (8.29),$\# \tilde { \mathbb { T } } \gtrapprox \delta \delta ^ { 2 \varepsilon _ { 2 } } \left( m \frac { \lvert W \rvert } { \lvert \tilde { T } \rvert } \right)$. Since

$$
\# \tilde {\mathbb {T}} [ V ] \leq C _ {F - C W} (\tilde {\mathbb {T}} ^ {W}) \frac {| V |}{| W |} (\# \tilde {\mathbb {T}}) \lesssim_ {\delta} \delta^ {- 2 \varepsilon_ {2}} \frac {| V |}{| W |} \left(m \frac {| W |}{| \tilde {T} |}\right),
$$

using (8.31), (8.36), (8.37), and (8.44) we conclude that

$$
\begin{array}{c} \Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}}} \tilde {Y} (\tilde {T}) \Big | \gtrsim_ {\delta} \delta^ {2 \varepsilon_ {3} + \beta - \zeta \sigma / 2} \Big (\frac {\rho}{\theta} \Big) ^ {\omega} m ^ {- 1} (m \frac {| W |}{| \tilde {T} |}) | \tilde {T} | \Big (m ^ {- 1} \big (m \frac {| V |}{| \tilde {T} |} \big) \frac {| \tilde {T} | ^ {1 / 2}}{| V | ^ {1 / 2}} \Big) ^ {- \sigma} \\ \gtrsim_ {\delta} \delta^ {2 \varepsilon_ {3} + \beta - \zeta \sigma / 4} \Big (\frac {\rho}{\theta} \Big) ^ {\omega + \sigma} | W |. \end{array}\tag{8.45}
$$

Step 8. Let us analyze (8.45). First, the set on the LHS of (8.45) is contained in$W ,$, which is a prism of dimensions$s \times t \times 1$. Second, the quantities$\varepsilon _ { 3 }$and$\beta$are chosen after$\zeta$and$\sigma ,$so we can select the former quantities to ensure that$\bar { \delta } ^ { - 2 \varepsilon _ { 3 } + \beta - \zeta \sigma / 4 } \geq \delta ^ { - \zeta \sigma / 5 }$

Thus by pigeonholing, we can select a ball B of radius$\theta$(recall that$\rho \le \theta \le s )$with the property that

$$
\left| B \cap \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}}} \tilde {Y} (T) \right| \gtrsim \delta^ {- \zeta \sigma / 5} \left(\frac {\rho}{\theta}\right) ^ {\omega + \sigma} | B |.\tag{8.46}
$$

Recall that at the beginning of Step 4 we fixed a prism$Z \in { \mathcal { Z } }$. The set of$\rho$tubes$\tilde { \mathbb { T } }$are the images of prisms from$\mathcal { P } _ { 3 } \langle Z \rangle$under the linear map$\phi _ { Z }$. Let$B ^ { \dagger } = \phi _ { Z } ^ { - 1 } ( B )$, where B is the ball described above. Then$B ^ { \dagger }$is an ellipsoid of dimensions$\theta _ { \rho } ^ { \underline { { a } } } \times \theta c \times \theta c$. By (8.46), we have

$$
\left| B ^ {\dagger} \cap \bigcup_ {P \in \mathcal {P} _ {1}} Y _ {1} (P) \right| \gtrsim \delta^ {- \zeta \sigma / 5} \left(\frac {\rho}{\theta}\right) ^ {\omega + \sigma} | B ^ {\dagger} |.\tag{8.47}
$$

Let$1 \leq i \leq \varepsilon _ { 1 } ^ { - 1 }$be the index so that$\delta ^ { i \varepsilon _ { 1 } } \leq \theta _ { \rho } ^ { \underline { { a } } } < \delta ^ { ( i - 1 ) \varepsilon _ { 1 } }$. Such an index exists since$\theta \in [ \rho , 1 ]$and $\begin{array} { r } { \delta \le \frac { a } { \rho } = \frac { a c } { b } \le c \le 1 } \end{array}$. Recall that we defined$\tau _ { i } = \delta ^ { i \varepsilon _ { 1 } }$, so$\theta a / \rho \le \tau _ { i } \delta ^ { - \varepsilon _ { 1 } }$implies$\rho / \theta \geq \delta ^ { \varepsilon _ { 1 } } a / \tau _ { i } \geq$ ${ { \delta } ^ { 1 + \varepsilon _ { 1 } } } / { \tau _ { i } }$. Then there exists a ball$B _ { \tau _ { i } }$of radius$\tau _ { i } .$, so that

$$
\lambda_ {i} \geq \Big | B _ {\tau_ {i}} \cap \bigcup_ {T \in \mathbb {T} _ {1}} Y _ {1} (T) \Big | | B _ {\tau_ {i}} | ^ {- 1} \geq \delta^ {3 \varepsilon_ {1} - \boldsymbol {\zeta} \sigma / 5} \Big (\frac {\rho}{\theta} \Big) ^ {\boldsymbol {\omega} + \boldsymbol {\sigma}} \geq \delta^ {4 \varepsilon_ {1} - \boldsymbol {\zeta} \sigma / 5} \Big (\frac {\delta}{\tau_ {i}} \Big) ^ {\boldsymbol {\omega}} \frac {| T | ^ {\boldsymbol {\sigma} / 2}}{| T _ {\tau_ {i}} | ^ {\boldsymbol {\sigma} / 2}}.\tag{8.48}
$$

Combining (8.25) and (8.48), we conclude that Conclusion (A) of Lemma 8.3 holds, provided we select$\begin{array} { r } { \varepsilon _ { 1 } \leq \frac { 1 } { 1 0 0 } \zeta \sigma } \end{array}$and select α suficiently small.

This concludes our analysis of the case where (8.37) holds (the analysis of this case began at the start of Step$7 )$. Henceforth we shall suppose that (8.37) fails.

Step 9. We shall now return to the start of Step$^ { 7 , }$except, instead of assuming (8.37), we will instead suppose that

$$
\theta <   \delta^ {\zeta / 1 0} \tau^ {\prime}.\tag{8.49}
$$

Informally, (8.49) says that the prisms$V \in \mathcal { V } _ { T _ { \tau } }$are flat.

Recall that in Steps 4 and 5, we fixed a prism$Z \in { \mathcal { Z } }$and a prism$W \in \mathcal { W } _ { Z }$. In this step, we will fix$\mathrm { ~ a ~ } \tau$tube$T _ { \tau } \in \mathbb { T } _ { \tau }$and a$\theta \times \tau ^ { \prime } \times 1$prism$V \in \mathcal { V } _ { T _ { \tau } }$. Define$\mathbb { T } ^ { \dagger } = \tilde { \mathbb { T } } [ V ]$and let$Y ^ { \dagger }$be the restriction of$\tilde { Y }$to T<sup>†</sup>. Thus$( \mathbb { T } ^ { \dagger } , Y ^ { \dagger } ) _ { \rho }$is a set of$\rho$tubes contained in$V$, and

$$
C _ {F - S W} ((\mathbb {T} ^ {\dagger}) ^ {V}) \lesssim_ {\delta} \delta^ {- \varepsilon_ {2}}.\tag{8.50}
$$

After pigeonholing, we may suppose that$( \mathbb { T } ^ { \dag } , Y ^ { \dag } ) _ { \rho } \mathrm { ~ i s ~ } \gtrapprox \delta \mathrm { ~ } \delta ^ { 2 \varepsilon _ { 2 } }$dense. For each “stem”$T _ { 0 } ^ { \dagger } \in \mathbb { T } ^ { \dagger }$，define the “hairbrush”

$$
\mathcal {H} (T _ {0} ^ {\dagger}) = \{T ^ {\dagger} \in \mathbb {T} ^ {\dagger} \colon Y ^ {\dagger} (T _ {0} ^ {\dagger}) \cap Y ^ {\dagger} (T ^ {\dagger}) \neq \emptyset \}.
$$

We claim that for each tube$T _ { 0 } ^ { \dagger } \in \mathbb { T } ^ { \dagger }$, the set

$$
N _ {(\tau^ {\prime} / \theta) \rho} (T _ {0} ^ {\dagger}) \cap \bigcup_ {T ^ {\dagger} \in \mathcal {H} (T _ {0} ^ {\dagger})} Y ^ {\dagger} (T ^ {\dagger})\tag{8.51}
$$

is contained in a rectangular prism of dimensions comparable to$\rho \times ( \tau ^ { \prime } / \theta ) \rho \times 1$; we will call this rectangular prism$X = X ( T _ { 0 } ^ { \dagger } )$. This claim follows from straightforward geometric considerations — See Figure 13. Define$Y ( X )$to be the set (8.51), so$Y ( X ) \subset X$

![](images/page_92_image_0.jpg)

Figure 13: All tubes (red) in this figure intersect the stem tube$T _ { 0 } ^ { \dagger }$(black). Since each tube is contained in the$\theta \times \tau ^ { \prime } \times 1$prism$V ,$each tube makes angle$\lesssim \theta / \tau ^ { \prime }$with the plane$\Pi ( V )$. Since each red tube intersect$T _ { 0 } ^ { \dagger }$, the union of these tubes, intersected with the$( \tau ^ { \prime } / \theta ) \rho$neighbourhood of$T _ { 0 } ^ { \dagger }$ are contained in the prism$X = X ( T _ { 0 } ^ { \dagger } )$(green) of dimensions$\begin{array} { r } { \frac { \theta } { \tau ^ { \prime } } \cdot \bigl ( \frac { \tau ^ { \prime } } { \theta } \bigr ) \rho \times \bigl ( \frac { \tau ^ { \prime } } { \theta } \bigr ) \rho \times 1 = \rho \times \bigl ( \frac { \tau ^ { \prime } } { \theta } \bigr ) \rho \times \bigr ] } \end{array}$

Next, we claim that if$\varepsilon _ { 2 }$is chosen suficiently small compared to$\varepsilon _ { 3 }$, then for a$\gtrapprox \delta$1 fraction of the tubes$T _ { 0 } ^ { \dagger } \in \mathbb { T } ^ { \dagger }$we have

$$
| Y (X) | \gtrsim_ {\delta} \delta^ {\varepsilon_ {3}} | X |, \quad \text { where } X = X (T _ {0} ^ {\dagger}).\tag{8.52}
$$

The estimate (8.52) says that the shading$Y ( X )$is$\stackrel { > } { \approx } \delta ^ { \varepsilon _ { 3 } }$dense. This is a standard Cordoba-type $L ^ { 2 }$argument. In brief, let$Y ^ { \ddagger } ( T ^ { \dagger } ) \subset Y ^ { \dagger } ( T ^ { \dagger } ) , T ^ { \dagger } \in \mathbb { T } ^ { \dagger }$be a regular shading, in the sense of Definition 5.8, with$| Y ^ { \ddag } ( T ^ { \dagger } ) | \geq \frac { 1 } { 2 } | Y ^ { \dag } ( T ^ { \dagger } ) |$. By pigeonholing,$\mathrm { ~ a ~ } _ { \widetilde { \approx } \delta }$1 fraction of the tubes$T _ { 0 } ^ { \dagger } \in \mathbb { T } ^ { \dagger }$satisfy

$$
| \{x \in Y ^ {\dagger} (T _ {0} ^ {\dagger}) \colon \# \mathbb {T} _ {Y ^ {\ddagger}} ^ {\dagger} (x) \geq \frac {1}{4} \# \mathbb {T} _ {Y ^ {\dagger}} ^ {\dagger} (x) \} | \gtrsim_ {\delta} \delta^ {2 \varepsilon_ {1}} | T _ {0} ^ {\dagger} |.\tag{8.53}
$$

For each point x in the set on the LHS of (8.53), we can select a tube$T ^ { \dagger } \in \mathbb { T } ^ { \dagger }$with$x \in Y ^ { \sharp } ( T )$ and$\angle ( \mathrm { d i r } ( T _ { 0 } ^ { \dagger } ) , \mathrm { d i r } ( T ^ { \dagger } ) ) \gtrapprox \delta ~ \tau$(recall that in Step 5, we refined our pair$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho }$to be broad with error$\lessapprox \delta { \mathrm { ~ 1 ~ } }$relative to$\mathbb { T } _ { \tau } )$. We now choose a δ/τ-separated set of points from the LHS of (8.53), and consider the corresponding tubes$\{ T ^ { \dagger } \}$. Since each shading$Y ^ { \ddag } ( T ^ { \dagger } )$is regular, we have that the sum of the volumes of these shadings, restricted to$X$, has volume$\stackrel { \wedge } { \approx } \delta ^ { \delta ^ { 2 \varepsilon _ { 1 } } | } X |$

$$
\sum_ {\{T ^ {\dagger} \}} | Y ^ {\ddagger} (T ^ {\dagger}) \cap X | \gtrsim_ {\delta} \delta^ {2 \varepsilon_ {1}} | X |.
$$

Finally, we use a Cordoba-style$L ^ { 2 }$argument to show that the corresponding shadings$\{ Y ^ { \ddag } ( T ) \}$are almost disjoint inside$X ;$this gives (8.52).

Abusing notation, we will refine$\mathbb { T } ^ { \dagger }$so that each$T ^ { \dagger } \in \mathbb { T } ^ { \dagger }$satisfies (8.52). By dyadic pigeonholing and replacing$\mathbb { T } ^ { \dagger }$by$\mathrm { ~ a ~ } \approx \delta$1 refinement (abusing notation, we will continue to refer to this set as $\mathbb { T } ^ { \dagger } )$, we can select a number$M$and a set$\mathcal { X }$of essentially distinct$\begin{array} { r } { \rho \times \frac { \tau ^ { \prime } \rho } { \theta } \times 1 } \end{array}$prisms of cardinality $\# \mathcal { X } = M ^ { - 1 } ( \# \mathbb { T } ^ { \dagger } )$), so that

(a) For each$X \in { \mathcal { X } }$, there are ∼ M tubes$T ^ { \dagger } \in \mathbb { T } ^ { \dagger }$with$T ^ { \dag } \subset X$and$X ( T ^ { \dagger } )$comparable to$X$. Denote this latter set by$\mathbb { T } _ { X } ^ { \dagger }$

(b) Each set$\mathbb { T } ^ { \dagger } [ X ] , X \in \mathcal { X }$has the same cardinality (up to a factor of 2).

Note that$\mathbb { T } _ { X } ^ { \dag } \subset \mathbb { T } ^ { \dag } [ X ]$, but the two sets need not be equal; it could be the case that$\# \mathbb { T } ^ { \dagger } [ X ]$is much larger than #X . In particular,$\mathbb { T } ^ { \dagger } = \sqcup _ { X \in \mathcal { X } } \mathbb { T } _ { X } ^ { \dagger }$, but X might not be a partitioning cover of $\mathbb { T } ^ { \dagger }$. For example, there could exist a tube in$\mathbb { T } ^ { \dagger } [ { \bar { X } } ]$that is contained in a diferent prism$V ^ { \prime } { : }$; such a tube will be also be contained in the set$\mathbb { T } _ { X ^ { \prime } } ^ { \dagger }$, where$X ^ { \prime }$a prism with orientation compatible with $V ^ { \prime }$(recall Figure 13). In particular, it is possible that X and$X ^ { \prime }$intersect transversely.

Step 10. In Step 9 we fixed a choice of$\tau$tube$T _ { \tau } \in \mathbb { T } _ { \tau }$and a$\theta \times \tau ^ { \prime } \times 1$prism$V \in \mathcal { V } _ { T _ { \tau } }$We then constructed a pair$( \mathcal { X } , Y ) _ { \rho \times \frac { \tau ^ { \prime } } { \theta } \rho \times 1 } .$The set X depended on the choice of prism$V \in \mathcal { V } _ { T _ { \tau } }$; we will highlight this dependence by writing$\mathcal { X } _ { V }$. In this step we will analyze the interaction between diferent collections$\mathcal { X } _ { V }$

Define$\begin{array} { r } { \mathcal { V } = \bigcup _ { T _ { \tau } \in \mathbb { T } _ { \tau } } \mathcal { V } _ { T _ { \tau } } } \end{array}$. Note that V is a set of$\theta \times \tau ^ { \prime } \times 1$prisms contained in W (the set W was fixed at Step 5). The quantity M from Step 9 depends on the choice of V , but after pigeonholing and refining V we may suppose that this number is the same (up to a factor of 2) for every$V \in \mathcal V$

We will first consider the case where

$$
\# \mathbb {T} _ {X} ^ {\dagger} \sim M \leq \delta^ {- \boldsymbol {\zeta} / 1 0 0} \frac {| X |}{| T ^ {\dagger} |}.\tag{8.54}
$$

We will show that Conclusion (A) of Lemma 8.3 holds.

Recall from Figure 13 that the prisms$X \in \mathcal { X } _ { V }$and V have compatible orientations, in the sense that$X ^ { V }$is a prism of dimensions comparable to${ \frac { \rho } { \theta } } \times { \frac { \rho } { \theta } } \times 1$. Thus we will refer to the set $( \boldsymbol { \mathcal { X } _ { V } ^ { V } } , Y ^ { V } ) _ { \frac { \rho } { \theta } \times \frac { \rho } { \theta } \times 1 } ) \ \mathrm { a s } \ ( \mathbb { T } _ { \frac { \rho } { \theta } , V } , Y _ { V } ) _ { \frac { \rho } { \theta } }$

We claim that

$$
\text { the   sets } \left\{\bigcup_ {X \in \mathcal {X} _ {V}} Y (X), V \in \mathcal {V} \right\} \text { are } \leq \delta^ {- \beta} \text { overlapping. }\tag{8.55}
$$

This claim follows from combining (8.33) and (8.35) (and noting that$\tau ^ { - \beta } \leq \delta ^ { - \beta } )$).

Observe that for each$V \in \mathcal V$we have

$$
C _ {F - S W} (\mathbb {T} _ {\frac {\rho}{\theta}, V}) \lesssim_ {\delta} \delta^ {- 2 \varepsilon_ {2}}.\tag{8.56}
$$

This is because$C _ { F - S W } ( \tilde { \mathbb { T } } ^ { V } ) \underset { \approx } { \lessapprox } \delta ^ { - 2 \varepsilon _ { 2 } }$(recall that V factors$\tilde { \mathbb { T } }$from below with small error with respect to the Frostman Slab Wolf Axioms), and by Item (b) from Step 9, each$X \in { \mathcal { X } } _ { V }$contains the same number (up to a factor of 2) of tubes from$\tilde { \mathbb { T } } [ V ]$. This means that$C _ { F - S W } ( \mathcal { X } _ { V } ^ { V } ) \lessapprox \delta ^ { - 2 \varepsilon _ { 2 } }$ which is precisely (8.56).

Define

$$
m _ {\frac {\rho}{\theta}} = m M ^ {- 1} \frac {| X |}{| \tilde {T} |},\tag{8.57}
$$

where$m$is as defined in (8.29), and$\begin{array} { r } { | X | = \rho \times \frac { \tau ^ { \prime } } { \theta } \rho \times 1 = \frac { \tau ^ { \prime } } { \theta } \rho ^ { 2 } } \end{array}$is the volume of a prism from$\mathcal { X } _ { V }$ We have

$$
C _ {K T - C W} (\mathbb {T} _ {\frac {\rho}{\theta}, V}) \lesssim_ {\delta} m M ^ {- 1} \frac {| X |}{| \tilde {T} |} \leq m _ {\frac {\rho}{\theta}}.\tag{8.58}
$$

Finally, we compute

$$
\sum_ {V \in \mathcal {V}} (\# \mathbb {T} _ {\frac {\rho}{\theta}, V}) \gtrsim_ {\delta} M ^ {- 1} \# \tilde {\mathbb {T}} [ W ] \gtrsim m M ^ {- 1} \frac {| W |}{| \tilde {T} |},\tag{8.59}
$$

where W is the prism fixed at Step$5 ,$and the final inequality used (8.29).

Fix a choice of$V \in \mathcal { V }$. Applying the estimate$\mathcal { E } ( \pmb { \sigma } , \omega )$to$( \mathbb { T } _ { \frac { \rho } { \theta } , V } , Y _ { V } ) _ { \rho / \theta }$with$\varepsilon _ { 4 }$in place of$\varepsilon$ and using (8.56), we have

$$
\Big | \bigcup_ {T _ {\frac {\rho}{\theta}} \in \mathbb {T} _ {\frac {\rho}{\theta}, V}} Y _ {V} (T _ {\frac {\rho}{\theta}}) \Big | \gtrsim_ {\delta} \delta^ {\varepsilon_ {4} + 2 \varepsilon_ {2}} \Big (\frac {\rho}{\theta} \Big) ^ {\omega} m _ {\frac {\rho}{\theta}} ^ {- 1} (\# \mathbb {T} _ {\frac {\rho}{\theta}, V}) | T _ {\frac {\rho}{\theta}} | \Big (m _ {\frac {\rho}{\theta}} ^ {- 3 / 2} (\# \mathbb {T} _ {\frac {\rho}{\theta}, V}) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \Big) ^ {- \sigma}.\tag{8.60}
$$

In the above inequality, we used (8.58) plus the fact that$\sigma \le 2 / 3$(the latter inequality allows us to replace$C _ { K T - C W } ( \mathbb { T } _ { \frac { \rho } { \theta } , V } )$with the potentially larger quantity$m _ { \frac { \rho } { \theta } } )$. Undoing the scaling$\phi _ { V }$and using (8.55), we conclude that

$$
\begin{array}{r l} & {\Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}}} Y (\tilde {T}) \Big | \geq \Big | \bigcup_ {V \in \mathcal {V}} \bigcup_ {X \in \mathcal {X} _ {V}} Y (X) \Big |} \\ & {\quad \geq \delta^ {\beta} \sum_ {V \in \mathcal {V}} \Big | \bigcup_ {X \in \mathcal {X} _ {V}} Y (X) \Big |} \\ & {\quad \geq \delta^ {\beta} \frac {| X |}{| T _ {\frac {\rho}{\theta}} |} \sum_ {V \in \mathcal {V}} \Big | \bigcup_ {T _ {\frac {\rho}{\theta}} \in \mathbb {T} _ {\frac {\rho}{\theta}, V}} Y _ {V} (T _ {\frac {\rho}{\theta}}) \Big |} \\ & {\quad \gtrsim_ {\delta} \delta^ {\beta} \frac {| X |}{| T _ {\frac {\rho}{\theta}} |} \cdot \delta^ {\varepsilon_ {4} + 2 \varepsilon_ {2}} \Big (\frac {\rho}{\theta} \Big) ^ {\omega} m _ {\frac {\rho}{\theta}} ^ {- 1} \Big (\sum_ {V \in \mathcal {V}} \# \mathbb {T} _ {\frac {\rho}{\theta}, V} \Big) | T _ {\frac {\rho}{\theta}} | \Big (m _ {\frac {\rho}{\theta}} ^ {- 3 / 2} (\sup _ {V \in \mathcal {V}} \# \mathbb {T} _ {\frac {\rho}{\theta}, V}) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \Big) ^ {- \sigma}} \\ & {\quad \gtrsim_ {\delta} \delta^ {\beta + 2 \varepsilon_ {4}} \frac {| X |}{| T _ {\frac {\rho}{\theta}} |} \cdot \Big (\frac {\rho}{\theta} \Big) ^ {\omega} m _ {\frac {\rho}{\theta}} ^ {- 1} \Big (m M ^ {- 1} \frac {| W |}{| \tilde {T} |} \Big) | T _ {\frac {\rho}{\theta}} | \Big (m _ {\frac {\rho}{\theta}} ^ {- 3 / 2} (\sup _ {V \in \mathcal {V}} \# \mathbb {T} _ {\frac {\rho}{\theta}, V}) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \Big) ^ {- \sigma},} \end{array}\tag{8.61}
$$

where the final inequality used (8.59). Substituting (8.57) and simplifying, we obtain

LHS (8.61)

$$
\begin{array}{r l} & {\gtrsim_ {\delta} \delta^ {\beta + 2 \varepsilon_ {4}} \frac {| X |}{| T _ {\frac {\rho}{\theta}} |} \cdot \Big (\frac {\rho}{\theta} \Big) ^ {\omega} \Big (m M ^ {- 1} \frac {| X |}{| \tilde {T} |} \Big) ^ {- 1} \Big (m M ^ {- 1} \frac {| W |}{| \tilde {T} |} \Big) | T _ {\frac {\rho}{\theta}} |} \\ & {\qquad \cdot \left(\Big (m M ^ {- 1} \frac {| X |}{| \tilde {T} |} \Big) ^ {- 3 / 2} \big (\sup _ {V \in \mathcal {V}} \# \mathbb {T} _ {\frac {\rho}{\theta}, V} \big) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2}\right) ^ {- \sigma}} \\ & {\gtrsim_ {\delta} \delta^ {\beta + 2 \varepsilon_ {4}} \Big (\frac {\rho}{\theta} \Big) ^ {\omega} | W | \Big (m M ^ {- 1} \frac {| X |}{| \tilde {T} |} \Big) ^ {\sigma / 2} \Big (\Big (m M ^ {- 1} \frac {| X |}{| \tilde {T} |} \Big) ^ {- 1} \big (M ^ {- 1} (\sup _ {V \in \mathcal {V}} \# \tilde {\mathbb {T}} [ V ]) \big) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \Big) ^ {- \sigma}} \\ & {\gtrsim_ {\delta} \delta^ {- \sigma \zeta / 4} \Big (\frac {\rho}{\theta} \Big) ^ {\omega} | W | \Big (m ^ {- 1} \frac {| \tilde {T} |}{| X |} \big (\# \tilde {\mathbb {T}} [ V ] \big) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \Big) ^ {- \sigma},} \end{array}\tag{8.62}
$$

where the second inequality used the fact that$\# \mathbb { T } _ { \frac { \rho } { \theta } , V } \sim M ^ { - 1 } ( \# \tilde { \mathbb { T } } [ V ] )$for each$V \in \mathcal { V } = \mathcal { V }$, and the third inequality used (8.31), (8.54),$| T ^ { \dagger } | = | \tilde { T } |$, and the fact that$\beta$and$\varepsilon _ { 4 }$are small compared to$\pmb { \sigma } \mathring { \zeta }$

Observe that the set on the LHS of (8.62) is contained in$| W |$, while the RHS involves the term $| W |$. Thus (8.62) gives a lower bound for the density of$\textstyle \bigcup _ { \tilde { T } \in \tilde { \mathbb { T } } } \tilde { Y } ( \tilde { T } )$inside W. This bound contains the term$\delta ^ { - \sigma \zeta / 4 } -$this quantity is much larger than 1, and this will eventually allow us to conclude that Conclusion (A) of Lemma 8.3 holds.

Let us analyze the final term in brackets$( \cdots ) ^ { - \sigma }$. We have

$$
\begin{array}{l} m ^ {- 1} \frac {| \tilde {T} |}{| X |} \big (\# \tilde {\mathbb {T}} [ V ] \big) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \leq m ^ {- 1} \frac {| \tilde {T} |}{| X |} \Big (C _ {F - C W} (\tilde {\mathbb {T}} ^ {W}) \frac {| V |}{| W |} (\# \tilde {\mathbb {T}} [ W ]) \Big) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \\ \quad \lesssim_ {\delta} m ^ {- 1} \frac {| \tilde {T} |}{| X |} \Big (\frac {| V |}{| W |} (m \frac {| W |}{| \tilde {T} |}) \Big) | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \\ = \frac {| V |}{| X |} | T _ {\frac {\rho}{\theta}} | ^ {1 / 2} \\ = \frac {\theta}{\rho}, \end{array}\tag{8.63}
$$

where the second inequality used (8.32) and (8.29).

Combining (8.62) and (8.63), we conclude that

$$
\Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}}} Y (\tilde {T}) \Big | \gtrsim_ {\delta} \delta^ {- \sigma \zeta / 4} \Big (\frac {\rho}{\theta} \Big) ^ {\omega + \sigma} | W |.\tag{8.64}
$$

Step 11. We can now argue similarly to our reasoning in Step 8. The set on the LHS of (8.64) is contained in$W$, which is a prism of dimensions$s \times t \times 1$, with$\delta \leq \rho \leq \theta \leq s \leq 1$. Thus there exists a ball$B _ { \theta }$of radius θ so that

$$
\left| B _ {\theta} \cap \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}}} Y (\tilde {T}) \right| \gtrsim_ {\delta} \delta^ {- \sigma \zeta / 4} \left(\frac {\rho}{\theta}\right) ^ {\omega + \sigma} | B _ {\theta} |.
$$

Recall that at the beginning of Step 4 we fixed a prism$Z \in { \mathcal { Z } }$. The set of$\rho$tubes$\tilde { \mathbb { T } }$are the images of prisms from$\mathcal { P } _ { 3 } \langle Z \rangle$under the linear map$\phi _ { Z }$. Let$B ^ { \dagger } = \phi _ { Z } ^ { - 1 } ( B _ { \theta } )$;$B ^ { \dagger }$is an ellipsoid of dimensions $\theta _ { \rho } ^ { \underline { { a } } } \times \theta c \times \theta c$, which satisfies

$$
\left| B ^ {\dagger} \cap \bigcup_ {T _ {1} \in \mathbb {T} _ {1}} Y _ {1} (T) \right| \gtrsim_ {\delta} \delta^ {- \sigma \zeta / 4} \left(\frac {\rho}{\theta}\right) ^ {\omega + \sigma} | B ^ {\dagger} |.
$$

This is the analogue of (8.47). An identical argument (in particular, note that$a \in [ \delta , 1 ] )$shows that Conclusion$\mathrm { ( A ) }$of Lemma 8.3 holds, provided we select$\alpha < \sigma \zeta / 1 0$. This concludes our analysis of the case where (8.54) holds.

Step 12. We shall now return to the start of Step 10, except, instead of assuming (8.54), we will instead suppose that

$$
M > \delta^ {- \zeta / 1 0 0} \frac {| X |}{| \tilde {T} |}.\tag{8.65}
$$

We summarize the situation thus far:

• We have fixed a choice of$Z \in { \mathcal { Z } }$(these are prisms of dimensions$\frac { a } { \rho } \times c \times c )$and$W \in \mathcal { W } _ { Z }$

• We have a set$\tilde { \mathbb { T } }$of$\rho$tubes contained in$W$.

• We have a set V of$\theta \times \tau ^ { \prime } \times 1$prisms contained in$W$

• For each$V \in \mathcal V$, we have a set$\mathcal { X } _ { V }$of$\rho \times \frac { \tau ^ { \prime } } { \theta } \rho \times 1$prisms, and a partition${ \\begin{array} { r } { { \tilde { \mathbb { T } } } [ V ] = \bigcup _ { X \in \mathcal { X } _ { V } } ( { \tilde { \mathbb { T } } } [ V ] ) _ { X } } \end{array} }$

• Each set$( \tilde { \mathbb { T } } [ V ] ) _ { X }$has cardinality roughly M, where M satisfies (8.65).

• We have a shading$\tilde { Y }$on$\tilde { \mathbb { T } }$so that$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho } \ \mathrm { i s } \ \gtrapprox \delta \ \delta ^ { 2 \varepsilon _ { 2 } }$dense.

Let${ \mathcal { X } } = \cup _ { V \in { \mathcal { V } } } { \mathcal { X } } _ { V }$(this is a slight abuse of notation, since in Step 9 we defined$\mathcal { X }$to be a set of the form$\mathcal { X } _ { V }$, where the prism$V$was fixed in advance). To simplify notation, define${ \tilde { \mathbb { T } } } _ { X } = ( { \tilde { \mathbb { T } } } [ V ] ) _ { X }$ where V is the (unique) prism for which$X \in { \mathcal { X } } _ { V }$. Since$( \tilde { \mathbb { T } } , \tilde { Y } ) _ { \rho } \ \mathrm { i s } \ \gtrapprox \delta \ \delta ^ { 2 \varepsilon _ { 2 } }$dense, after a harmless refinement of$\mathcal { X }$we may suppose that each pair$( \tilde { \mathbb { T } } _ { X } , \tilde { Y } ) _ { \rho } \mathrm { i s } \gtrapprox \delta \delta ^ { \mathrm { 2 } \varepsilon _ { 2 } }$dense, where$\tilde { Y }$is the restriction of the shading on$\tilde { \mathbb { T } }$to the set$\tilde { \mathbb { T } } _ { X }$

Apply Corollary 7.10 (finding a broad scale) to each pair$( \tilde { \mathbb { T } } _ { X } , \tilde { Y } ) _ { \rho } ,$for each$X \in { \mathcal { X } }$. This yields a scale$\tilde { \rho }$and a$\gtrapprox \delta ~ 1$refinement$( \tilde { \mathbb { T } } _ { X } ^ { \prime } , \tilde { Y } ^ { \prime } ) _ { \rho }$that is broad with error$\lessapprox \delta { \mathrm { ~ 1 ~ } }$with regard to a balanced partitioning cover of$\tilde { \rho }$tubes.

After dyadic pigeonholing and refining the set$x ,$we can suppose that the scale$\tilde { \rho }$from Corollary 7.10 is the same for each prism$X$. We claim that

$$
\tilde {\rho} \gtrsim_ {\delta} \delta^ {- \zeta / 2 0 0} \rho .\tag{8.66}
$$

To verify this claim, observe that for each$X \in { \mathcal { X } }$, the sets$\{ \tilde { Y } ^ { \prime } ( \tilde { T } ) \colon \tilde { T } \in \tilde { \mathbb { T } } _ { X } ^ { \prime } \}$are$\lesssim \delta ~ ( \tau ^ { \prime } / \tilde { \rho } ) ^ { \beta } ( \tilde { \rho } / \rho )$ overlapping. This is because the tubes from$\tilde { \mathbb { T } } _ { X } ^ { \prime }$whose shadings pass through a common point x must point in directions confined to a$\rho \times \tau ^ { \prime }$region in the unit sphere$S ^ { 2 } \subset \mathbb { R } ^ { \bar { 3 } }$(we identify$S ^ { 2 }$with the set of directions of tubes in$\mathbb { R } ^ { 3 } )$. Since these tubes are essentially distinct and pass through a common point, they must point in$\rho$separated directions. Thus at most$\rho / \tilde { \rho }$tubes can point in directions confined to a$\rho \times { \tilde { \rho } }$region in$S ^ { 2 }$(this corresponds to those$\rho$tubes contained in a single $\tilde { \rho }$tube), and at most$( \tau ^ { \prime } / \tilde { \rho } ) ^ { \beta }$distinct$\tilde { \rho }$tubes can contribute to the count. This implies that

$$
\Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}} _ {X} ^ {\prime}} \tilde {Y} ^ {\prime} (\tilde {T}) \Big | \gtrsim_ {\delta} \Big (\frac {\tilde {\rho}}{\tau^ {\prime}} \Big) ^ {\beta} \Big (\frac {\rho}{\tilde {\rho}} \Big) \sum_ {\tilde {T} \in \tilde {\mathbb {T}} _ {X} ^ {\prime}} | \tilde {Y} ^ {\prime} (\tilde {T}) | \geq \delta^ {- \zeta / 2 0 0} \Big (\frac {\rho}{\tilde {\rho}} \Big) | X |,
$$

where the second inequality used (8.65) and$\beta < \zeta / 2 0 0$. Since the set on the LHS is contained in X, we obtain (8.66), as claimed.

Next, for each prism$X \in { \mathcal { X } }$there exists a set$\{ U \}$of essentially distinct$\rho \times \tilde { \rho } \times 1$prisms, each of which are contained in X, so that these sets form a partitioning cover of$\tilde { \mathbb { T } } _ { X } ^ { \prime }$, and for each such U, the pair$( \tilde { \mathbb { T } } _ { X } ^ { \prime } [ U ] , \tilde { Y } ^ { \prime } ) _ { \rho }$is broad with error$\lessapprox$1 relative to the cap of diameter$\tilde { \rho }$centered at the point dir(U). See Figure 14.

For each such prism U, define

$$
Y (U) = \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}} _ {X} ^ {\prime} [ U ]} \tilde {Y} ^ {\prime} (\tilde {T}).
$$

Then a Cordoba-style$L ^ { 2 }$argument shows that for each prism$U$for which$( \ \tilde { \mathbb { T } } _ { X } ^ { \prime } [ U ] , \tilde { Y } ^ { \prime } ) _ { \rho } \ \mathrm { i s } \ \gtrapprox \delta \ \delta ^ { 2 \varepsilon _ { 2 } }$ dense (here${ \tilde { Y } } ^ { \prime }$denotes the restriction of the shading on$\tilde { \mathbb { T } } _ { X } ^ { \prime }$to$\tilde { \mathbb { T } } _ { X } ^ { \prime } [ U ] )$, we have${ | Y ( U ) | \gtrapprox } \delta ^ { 8 \varepsilon _ { 2 } } { | U | }$ Let U denote the set of all prisms$U$for which this holds, as$X$ranges over the elements of$\mathcal { X }$ Note, however, that the prisms in U need not be essentially distinct.

Step 13. Our task in this step is to unwind the various transformations and rescalings from the previous step, and to understand what the prisms$U$(and their associated shadings$Y ( U ) )$1 correspond to in the original space in which the tubes$\mathbb { T }$and prisms$\mathcal { P }$reside.

![](images/page_97_chart_0.jpg)

Figure 14: We find a set of$\rho \times \tilde { \rho } \times 1$prisms (blue) inside X (black prism), which forms a partitioning cover of$\tilde { \mathbb { T } } _ { X } ^ { \prime }$(red lines). A typical pair of tubes from$\tilde { \mathbb { T } } _ { X } ^ { \prime }$inside a common (blue)$\rho \times \tilde { \rho } \times 1$prism intersect at angle roughly${ \tilde { \rho } } .$

In Step 12, we fixed a choice of$Z \in { \mathcal { Z } }$and$W \in \mathcal { W } _ { Z }$. Recall that$\tilde { \mathbb { T } }$comes from$( \mathcal { P } _ { 5 } \langle Z \rangle ) ^ { Z }$, and is a set of$\rho \times \rho \times 1 \mathrm { - t u b e s }$. We obtained a set$\mathcal { U } = \mathcal { U } _ { W , Z }$of$\rho \times \tilde { \rho } \times 1$prisms (this U is diferent from the set$\mathcal { U }$in Step 3, the latter U was defined to introduce$\mathcal { Z }$and only appeared within Step 3), and a shading$Y ( U )$on these prisms. These prisms are contained inside$W$. Undoing the linear transformation$\phi _ { Z }$, we have a set$\phi _ { Z } ^ { - 1 } ( \mathcal { U } _ { W , Z } )$of prisms. After pigeonholing, we may assume that these prisms are of dimensions${ \tilde { a } } \times { \tilde { b } } \times c ,$, for some$\tilde { a } \geq a$and$\tilde { b } \geq b$. Since the linear transformation $\phi _ { Z }$distorts volume by a factor of$( a / \rho ) c ^ { 2 }$, we have that$( \tilde { a } \tilde { b } ) = a c \tilde { \rho }$. The dimensions$\tilde { a } , \tilde { b }$depend on the choice of$W$and$Z$, but after pigeonholing, we may suppose that these values are the same (up to a factor of 2) for all$Z \in { \mathcal { Z } }$and all$W \in \mathcal { W } _ { Z }$. We claim (provided$\varepsilon _ { 2 }$is chosen suficiently small compared to$\varepsilon _ { 3 } )$that either

$$
\tilde {a} \leq \delta^ {- \varepsilon_ {3}} a,\tag{8.67}
$$

or else Conclusion (A) of Lemma 8.3 holds (provided$\alpha$is chosen suficiently small, depending on $\varepsilon _ { 3 } )$. The argument is identical to the argument in Step 1 of Lemma 8.2; we refer the reader there for details.

Henceforth we shall assume that (8.67) holds. Abusing notation, we will re-define$\tilde { \rho } = \tilde { b } / c ;$this re-definition might decrease the value of$\tilde { \rho }$by as much as$\delta ^ { \varepsilon _ { 3 } }$, and (8.66) might be weakened to $\tilde { \rho } \ge \delta ^ { - \zeta / 4 0 0 } \rho$. With this re-definition of${ \tilde { \rho } } ,$we clearly have$\tilde { b } = \tilde { \rho } c$

Let

$$
\mathcal {Q} = \bigcup_ {Z \in \mathcal {Z}} \bigcup_ {W \in \mathcal {W} _ {Z}} \phi_ {Z} ^ {- 1} (\mathcal {U} _ {Z, W}).
$$

For each$Q \in \mathcal { Q }$of the form$Q = \phi _ { Z } ^ { - 1 } ( U )$, define the shading$Y ( Q ) = \phi _ { Z } ^ { - 1 } ( Y ( U ) )$and define the set${ \mathcal { P } } _ { Q } \subset { \mathcal { P } } [ Q ]$as$\phi _ { Z } ^ { - 1 } ( \tilde { \mathbb { T } } _ { X } ^ { \prime } [ U ] )$, where X is the$\begin{array} { r } { \rho \times \frac { \tau ^ { \prime } } { \theta } \rho \times 1 \cdot } \end{array}$-prism associated to U (see Step 12). Summarizing our conclusions thus far, we have the following.

• Each$Q \in \mathcal { Q }$is a prism of dimensions${ \tilde { a } } \times { \tilde { b } } \times c .$, with$\tilde { b } = \tilde { \rho } c$

• For each$Q \in { \mathcal { Q } } .$, there is a set${ \mathcal { P } } _ { Q } \subset { \mathcal { P } } [ Q ]$. Define$\mathcal { P } ^ { \prime } = \cup _ { Q \in \mathcal { Q } } \mathcal { P } _ { Q }$. There is a shading $Y ^ { \prime } ( P ) \subset Y ( P )$, so that$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times c } { \mathrm { ~ i s ~ a ~ } } \gtrapprox \delta \delta ^ { 2 \varepsilon _ { 2 } }$refinement of$( { \mathcal { P } } , Y ) _ { a \times b \times c } .$

• Each$Q \in \mathcal { Q }$has a shading$Y ( Q )$given by

$$
Y (Q) = \bigcup_ {P \in \mathcal {P} _ {Q}} Y ^ {\prime} (P).
$$

We have$| Y ( Q ) | \gtrapprox \delta \delta ^ { \delta \varepsilon _ { 2 } } | Q |$for each$Q \in \mathcal { Q }$

• For each$Q \in \mathcal { Q }$and each$x \in Y ( Q )$, the prisms$P \in { \mathcal { P } } _ { Q }$with$x \in Y ^ { \prime } ( P )$point in directions that are broad with error$\lessapprox \delta { \mathrm { ~ 1 ~ } }$inside a cap of radius$\tilde { b } / c$centered at dir(Q) (these correspond to the tubes$\tilde { \mathbb { T } } _ { X } ^ { \prime } [ U ]$and their associated shading, which are broad with error$\lessapprox \delta { \mathrm { ~ 1 ~ } }$inside the $\rho \times \tilde { \rho } \times 1$prism U).

• The refinement of$( \mathbb { T } , Y ) _ { \delta }$induced by the refinement$( \mathcal { P } ^ { \prime } , Y ^ { \prime } ) _ { a \times b \times c }$of$( { \mathcal { P } } , Y ) _ { a \times b \times c }$is$\stackrel { > } { \approx } \delta ^ { 2 \varepsilon _ { 2 } }$ dense. If we denote this refinement by$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$, then (by the definition of being an induced refinement) we have

$$
\bigcup_ {T \in \mathbb {T} ^ {\prime}} Y ^ {\prime} (T) = \bigcup_ {Q \in \mathcal {Q}} Y (Q).
$$

The pair$( \mathcal { Q } , Y ) _ { \tilde { a } \times \tilde { b } \times c }$has some of the desired properties from Conclusion (C) of Lemma 8.3. Observe that for each$Q \in { \mathcal { Q } } , \operatorname { d i r } ( Q )$is defined up to uncertainty${ \tilde { \rho } } .$. Thus after a refinement of$\mathcal { Q }$ and$\mathbb { T } ^ { \prime }$, we can find a set of$\tilde { \rho }$tubes$\mathbb { T } _ { \widetilde { \rho } }$and a partition$\begin{array} { r } { Q = \bigcup _ { T _ { \tilde { \rho } } \in \mathbb { T } _ { \tilde { \rho } } } \mathcal { Q } _ { T _ { \tilde { \rho } } } } \end{array}$, so that each$Q \in \mathcal { Q } _ { T _ { \tilde { \rho } } }$is contained in$T _ { \tilde { \rho } }$and satisfies$\begin{array} { r } { \angle ( \mathrm { d i r } ( Q ) , \mathrm { d i r } ( T _ { \tilde { \rho } } ) ) \leq \tilde { \rho } . } \end{array}$

Fix a prism$Q \in \mathcal { Q } _ { T _ { \tilde { \rho } } }$and a point$x \in Y ( Q )$. The set of prisms$P \in { \mathcal { P } } _ { Q }$with$x \in Y ^ { \prime } ( P )$point in directions that satisfy$\angle ( \mathrm { d i r } ( P ) , \mathrm { d i r } ( Q ) ) \leq \tilde { \rho } ,$and this set of directions is$\rho \mathrm { - }$-separated and broad with error$\lessapprox \delta ^ { \mathrm { ~ 1 ~ } }$at scales$\geq \rho$inside a cap of diameter$\tilde { \rho }$centered at$\mathrm { d i r } ( Q )$. For each such$P$ (contained in a$\rho$tube$T _ { \rho } )$, the set of tubes$T \in \mathbb { T } [ T _ { \rho } ]$with$x \in Y ^ { \prime } ( T )$are broad with error$\lessapprox \delta ^ { - 2 \varepsilon _ { 2 } }$ at scales$\geq \delta ,$, inside a cap of diameter$\rho$centered at$\mathrm { d i r } ( P )$. Thus by Lemma 7.13 (broadness combines across scales) and Items (ii) and (iii) of Definition 7.1, we have that the set of tubes $T \in \mathbb { T } ^ { \prime }$associated to the point$x \in Y ( Q )$point in directions that are broad with error$\lessapprox \delta ^ { - 2 \varepsilon _ { 2 } }$at scales$\geq \delta$inside a cap of diameter$\tilde { \rho }$centered at$\mathrm { d i r } ( Q )$

Note that even though the conclusion of Lemma 7.13 is a statement about multi-sets, here it is also true in the sense of sets. Indeed, Item (ii) of Definition 7.1 says that for each point $x \in \bigcup _ { Q \in \mathcal { Q } _ { T _ { \tilde { o } } } } Y ( Q )$, we have that the sets$\{ \mathrm { d i r } ( T ) : T \in \mathbb { T } [ T _ { \rho } ]$and$x \in Y ^ { \prime } ( T ) \cap Y ^ { \prime } ( P ) \}$are disjoint, as$P$ranges over the elements of$\cup _ { Q \in \mathcal { Q } _ { T _ { \widetilde { a } } } } \mathcal { P } _ { Q }$that are contained in$T _ { \rho }$. In particular, we can construct a set$\mathbb { T } _ { \widetilde { \rho } }$of$\tilde { \rho }$tubes that covers$\dot { \mathbb { T } ^ { \prime } }$, so that$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with error$\lessapprox _ { \delta } \delta ^ { - 2 \varepsilon _ { 2 } }$relative to$\mathbb { T } _ { \widetilde { \rho } }$

## Step 14.

We would like to show that$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } , \mathcal { Q }$and its associated shading$Y .$, and$\tilde { \mathbb { T } }$satisfy Conclusion (C) from Lemma 8.3. First, the prisms in$\mathcal { Q }$might not be essentially distinct. This can be fixed, however, using the same argument as was employed in Step 5 from the proof of Lemma 8.2. In brief, we merge comparable prisms from$\mathcal { Q }$into a single prism. Denote the resulting set of prisms by${ \tilde { \mathcal { P } } } ;$these are essentially distinct prisms of dimensions comparable to${ \tilde { a } } \times { \tilde { b } } \times c .$. Let$\tilde { Y }$be the shading on the prisms of$\tilde { \mathcal P }$obtained by taking the union of the shadings$Y ( Q ) , Q \subset { \tilde { P } }$. We define

$$
\mathcal{P}_{\tilde{P}} = \bigcup_{\substack{Q\in \mathcal{Q}\\ Q\subset \tilde{P}}}\mathcal{P}_{Q}.
$$

Note that if$P \in \mathcal { P } _ { \tilde { P } }$, then$\angle ( \mathrm { d i r } ( P ) , \mathrm { d i r } ( \tilde { P } ) ) \lesssim \tilde { b } / c = \tilde { \rho }$. Thus after enlarging$\tilde { a }$and$\tilde { b }$by a constant factor if needed, we can ensure that if (i):$T \cap P \neq \emptyset .$, (ii): T exists P through its long ends, and (iii):$P \in \mathcal { P } _ { \tilde { P } }$, then$T \cap { \tilde { P } } \neq \emptyset$and$T$exists$\tilde { P }$through its long ends. At this point, the pair$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$ and$( \tilde { \mathcal { P } } , \tilde { Y } ) _ { \tilde { a } \times \tilde { b } \times c }$satisfy some of the requirements of Conclusion (C) from Lemma 8.3. The situation matches the setup at the end of Step 5 in the proof of Lemma 8.2.

We now proceed with the same argument that was used in Steps 6 – 8 from the proof of Lemma 8.2. We conclude that either Conclusion$\mathrm { ( A ) }$of Lemma 8.3 holds (this is the same as Conclusion (A) of Lemma 8.2), or else there is a set$\mathbb { T } _ { \widetilde { \rho } }$and a further refinement of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$and$( \tilde { P } , \tilde { Y } ) _ { \tilde { a } \times \tilde { b } \times c }$ that satisfies Items (i), (ii), and (iii) of Conclusion (C) from Lemma 8.3 (Items$( \mathrm { i } ) , ( \mathrm { i i } )$, and (iii) of Conclusion (C) from Lemma 8.2). Note that Item (iv) Conclusion (C) is also satisfied, since $\tilde { \rho } \ge \delta ^ { - \zeta / 4 0 0 } \rho$. We conclude that Conclusion (C) from Lemma 8.3 holds.□

## 9 A refined induction-on-scales argument

The goal in this section is to show that if$( \mathbb { T } , Y ) _ { \delta }$is a set of δ-tubes, then either$\textstyle \bigcup _ { \mathbb { T } } Y ( T )$has larger volume than one would expect from the estimate (1.3) from Assertion$\mathcal { E } ( \sigma , \omega )$, or else there exists a scale$\delta \ll \rho \ll 1$and a set of$\rho$tubes that factors T above and below with respect to the Katz-Tao Convex Wolf Axioms and Frostman Slab Wolf Axioms. The precise statement is as follows.

Proposition 9.1. Let$\omega , \zeta > 0$and$\sigma \in ( 0 , 2 / 3 ]$, and suppose that$\mathcal { E } ( \sigma , \omega )$is true. Then there exists$\alpha , \eta , \kappa > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, and suppose that$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Then at least one of the following must hold.

(A)

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega - \alpha} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.\tag{9.1}
$$

(B) There exists a refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ~ o f ( \mathbb { T } , Y ) _ { \delta }$that is$\delta ^ { \zeta }$dense, a number$\rho \in [ \delta ^ { 1 - \omega / 1 0 0 } , \delta ^ { \omega / 1 0 0 } ]$9 and a set$\mathbb { T } _ { \rho }$that factors$\mathbb { T } ^ { \prime }$above and below with respect to both the Katz-Tao Convex Wolf Axioms and the Frostman Slab Wolf Axioms, both with error$\leq \delta ^ { - \zeta }$

Proof. Step 1. Let$\varepsilon _ { 1 } , \varepsilon _ { 2 } , \varepsilon _ { 3 }$be small numbers to be chosen below. We will select$\varepsilon _ { 1 }$very small compared to$\varepsilon _ { 2 }$and$\varepsilon _ { 2 }$very small compared to$\varepsilon _ { 3 }$. These numbers depend on$\omega , \sigma ,$and$\zeta .$We will select η and α very small compared to$\varepsilon _ { 1 }$.

Apply Proposition 7.5 (two scale grains decomposition) to$( \mathbb { T } , Y )$with$\varepsilon _ { 1 }$in place of$\zeta ,$and let $\alpha _ { 1 } = \alpha _ { 1 } ( \omega , \sigma , \varepsilon _ { 1 } )$be the output of that proposition. If Conclusion$\mathrm { ( A ) }$of Proposition 7.5 holds, then (9.1) is true (provided we select$\alpha \leq \alpha _ { 1 } )$, and we are done.

Next, suppose Conclusion (B) of Proposition 7.5 holds. Let$\rho , c , ( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta } , \mathbb { T } _ { \rho } .$, and$( \mathcal G , Y ) _ { a \times \rho c \times c }$ be the output from Proposition 7.5, Conclusion (B).

Apply Proposition 4.6 (factoring convex sets) to$\mathbb { T } _ { \rho } .$. We obtain a$\approx _ { \rho }$1 refinement of$\mathbb { T } _ { \rho } ,$, which in turn induces$\mathrm { a } \approx _ { \rho } 1$refinement of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$(abusing notation, we will continue to refer to these objects as$\mathbb { T } _ { \rho }$and$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta } )$and a collection Z of congruent convex sets that factors$\mathbb { T } _ { \rho }$from above with respect to the Katz-Tao Convex Wolf Axioms and from below with respect to the Frostman Convex Wolf Axioms, both with error$\lessapprox \rho 1$. Furthermore,

$$
\# \mathbb {T} _ {\rho} [ Z ] \gtrsim_ {\approx \rho} C _ {K T - C W} (\mathbb {T} _ {\rho}) | Z | | T _ {\rho} | ^ {- 1} \quad \text { for   each } Z \in \mathcal {Z}.\tag{9.2}
$$

If$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) \le \delta ^ { - \zeta }$, then provided we select$\varepsilon _ { 1 } \leq \zeta / 2$, we have that$( \mathbb { T } _ { 1 } , Y _ { 1 } )$and$\mathbb { T } _ { \rho }$satisfy Conclusion (B) of Proposition 9.1, and we are done. Indeed; by Remark$4 . 3 ( \mathrm { A } )$we have$C _ { F - S W } ( \mathbb { T } _ { \rho } ) \lesssim$ $C _ { F - S W } ( \mathbb { T } _ { 1 } ) \lesssim _ { \delta } \delta ^ { - \eta _ { 1 } - \varepsilon _ { 1 } } \leq \delta ^ { - \zeta }$, while by Remark 4.3(B) we have$C _ { K T - C W } ( \mathbb { T } _ { 1 } ^ { T _ { \rho } } ) \lesssim C _ { K T - C W } ( \mathbb { T } ) \leq \delta ^ { - \eta }$ for each$T _ { \rho } \in \mathbb { T } _ { \rho } .$

Step 2. We now consider the case where$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) > \delta ^ { - \zeta }$, and hence

$$
\# \mathbb {T} _ {\rho} [ Z ] \gtrsim \delta^ {- \zeta} \frac {| Z |}{| T _ {\rho} |} \quad \text { for   each } Z \in \mathcal {Z}.\tag{9.3}
$$

Our goal is to show that Conclusion (A) of Proposition 9.1 holds, provided$\alpha > 0$is chosen appropriately.

First, we claim that either Conclusion (A) of Proposition 9.1 holds, or else the prisms in$\mathcal { Z }$are almost tubes. Indeed, let$t \times \theta \times 2$be the dimensions of the prisms in$\mathcal { Z } .$. If$\varepsilon _ { 1 }$is chosen suficiently small depending on$\varepsilon _ { 2 } , \omega ,$and$\sigma ,$then by applying Proposition 5.2 with$\varepsilon _ { 2 }$in place of$\varepsilon ,$we have

$$
\Big | \bigcup_ {T \in \mathbb {T} _ {1}} Y _ {1} (T) \Big | \gtrsim \delta^ {\omega + \varepsilon_ {2}} \Big (\frac {\theta}{t} \Big) ^ {\omega} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma},\tag{9.4}
$$

where the implicit constant depends on$\varepsilon _ { 2 }$. In particular, we may suppose that

$$
t \geq \delta^ {\varepsilon_ {3}} \theta ,\tag{9.5}
$$

or else Conclusion$( \mathrm { A } )$of Proposition 9.1 holds, provided$\varepsilon _ { 2 } \le \varepsilon _ { 3 } \omega / 2$and$\alpha \leq \varepsilon _ { 3 } \omega / 2$. Replace each $t \times \theta \times 2$prism$Z \in { \mathcal { Z } }$with its coaxial θ-tube. After dyadic pigeonholing and replacing$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$ and$\mathbb { T } _ { \rho }$with a${ \approx } _ { \delta } 1$refinement, we can find a balanced cover$\mathbb { T } _ { \theta }$of$\mathbb { T } _ { \rho }$that factors$\mathbb { T } _ { \theta }$from below with respect to the Frostman Convex Wolf Axioms and from above with respect to the Katz-Tao Wolf Axioms, both with error$\lessapprox \delta  ^ { - \varepsilon _ { 3 } }$

(9.3) implies that for each$T _ { \theta } \in \mathbb { T } _ { \theta }$we have$\# \mathbb { T } _ { \rho } [ T _ { \theta } ] \gtrapprox \delta \delta ^ { \varepsilon _ { 3 } - \zeta } ( \theta / \rho ) ^ { 2 }$, and hence

$$
\# \mathbb {T} _ {\rho} \gtrsim_ {\delta} \delta^ {\varepsilon_ {3} - \zeta} (\theta / \rho) ^ {2} (\# \mathbb {T} _ {\theta}).\tag{9.6}
$$

Step 3. For each$T _ { \theta } \in \mathbb { T } _ { \theta }$, define

$$
\mathcal {G} _ {T _ {\theta}} = \bigcup_ {T _ {\rho} \in \mathbb {T} _ {\rho} [ T _ {\theta} ]} \mathcal {G} _ {T _ {\rho}}.
$$

We claim that either Conclusion$\mathrm { ( A ) }$holds (for a suitably chosen value of$\alpha )$, or else there is$\mathrm { a } \approx _ { \delta }$1 refinement of$( \mathcal G , Y ) _ { a \times \rho c \times c }$so that the following holds:$a \in [ \delta , \delta ^ { 1 - \varepsilon _ { 1 } } ]$and for each$T _ { \theta } \in \mathbb { T } _ { \theta }$and each

$G \in { \mathcal { G } } _ { T _ { \theta } }$, the set of grains$G ^ { \prime } \in { \mathcal { G } } _ { T _ { \theta } }$with$Y ( G ) \cap Y ( G ^ { \prime } ) \neq \emptyset$is contained in a prism of dimensions comparable to$\frac { \theta \delta ^ { 1 - \varepsilon _ { 2 } } } { \rho } \times \theta c \times c$(compare this with the dimensions of$G ,$which are$a \times \rho c \times c )$. The argument is identical to the argument in Steps 1 and 2 from Lemma$8 . 3 ;$we refer the reader to those Steps for details.

We shall suppose henceforth that for each$T _ { \theta } \in \mathbb { T } _ { \theta }$and each$G \in { \mathcal { G } } _ { T _ { \theta } }$, the set of grains$G ^ { \prime } \in { \mathcal { G } } _ { T _ { \theta } }$ with$Y ( G ) \cap Y ( G ^ { \prime } ) \neq \emptyset$is contained in a prism of dimensions comparable to$\frac { \theta \delta ^ { 1 - \varepsilon _ { 2 } } } { \rho } \times \theta c \times c .$

Step 4. By dyadic pigeonholing we can find a number$\mu _ { \mathrm { f i n e } }$and a${ \approx } _ { \delta } ~ .$1 refinement of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$and $\mathbb { T } _ { \rho }$so that for each$T _ { \rho } \in \mathbb { T } _ { \rho }$and each$x \in \bigcup _ { T \in \mathbb { T } _ { 1 } [ T _ { \rho } ] } Y _ { 1 } ( T )$, we have

$$
\# \big ((\mathbb {T} _ {1} [ T _ {\rho} ]) _ {Y _ {1}} (x) \big) \sim \mu_ {\mathrm{fine}}.
$$

We can choose these refinements so it continues to be the case that$( \mathbb { T } _ { 1 } ^ { T _ { \rho } } , Y _ { 1 } ^ { T _ { \rho } } ) _ { \delta / \rho }$is$\stackrel { > } { \approx } \delta ^ { \varepsilon _ { 1 } }$dense and$C _ { F - S W } \big ( \mathbb { T } _ { 1 } ^ { T _ { \rho } } \big ) \lesssim \delta \delta ^ { - \varepsilon _ { 1 } }$for each$T _ { \rho } \in \mathbb { T } _ { \rho }$(recall that we still have$C _ { K T - C W } ( \mathbb { T } _ { 1 } ^ { T _ { \rho } } ) \leq \delta ^ { - \eta } )$

If$\varepsilon _ { 1 }$is chosen suficiently small depending on$\varepsilon _ { 2 } .$then we can apply the estimate$\mathcal { E } ( \sigma , \omega )$to conclude that for each$T _ { \rho } \in \mathbb { T } _ { \rho } ,$we have

$$
\Big | \bigcup_ {T \in \mathbb {T} _ {1} [ T _ {\rho} ]} Y _ {1} (T) \Big | \gtrsim \big (\frac {\delta}{\rho} \big) ^ {\omega + \varepsilon_ {2}} (\# \mathbb {T} _ {1} [ T _ {\rho} ]) | T | \Big ((\# \mathbb {T} _ {1} [ T _ {\rho} ]) \big (\frac {| T |}{| T _ {\rho} |} \big) ^ {1 / 2} \Big) ^ {- \sigma},
$$

where the implicit constant depends on$\varepsilon _ { 2 }$, and hence by (9.6),

$$
\mu_ {\mathrm{fine}} \lesssim \left(\frac {\delta}{\rho}\right) ^ {- \omega - \varepsilon_ {2}} \left(\frac {\# \mathbb {T} _ {1}}{\# \mathbb {T} _ {\rho}} \frac {\delta}{\rho}\right) ^ {\sigma} \lesssim_ {\delta} \delta^ {- 2 \varepsilon_ {3} + \sigma \zeta} \left(\frac {\delta}{\rho}\right) ^ {- \omega} \left(\frac {\# \mathbb {T} _ {1}}{\# \mathbb {T} _ {\theta}} \frac {\delta \rho}{\theta^ {2}}\right) ^ {\sigma}.\tag{9.7}
$$

Step 5. In previous applications of induction on scale, the estimate (9.7) would be paired with a multiplicity estimate on the tubes in$\mathbb { T } _ { \rho } .$. Our innovation, however, is to pair the estimate (9.7) with a multiplicity estimate on$\mathcal { G }$

After refining the pair$( \mathcal G , Y ) _ { a \times \rho c \times c }$by$\mathrm { ~ a ~ } { \approx } \delta$1 factor (this in turn refines$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$by a similar quantity), we can find a number µ<sub>medium</sub> so that for each$T _ { \theta } \in \mathbb { T } _ { \theta }$and each$x \in \bigcup _ { G \in { \mathcal { G } } _ { T _ { \theta } } } Y ( G )$, we have

$$
\# \{G \in \mathcal {G} _ {T _ {\theta}} \colon x \in Y (G) \} \sim \mu_ {\mathrm{medium}}.
$$

Our task is to estimate$\mu _ { \mathrm { { m e d i u m } } }$. Recalling the conclusion of Step 3, we can cover$T _ { \theta }$by rectangular prisms P of dimensions comparable to$\frac { \breve { \theta } \delta ^ { 1 - \varepsilon _ { 2 } } } { \rho } \times \theta c \times c .$so that every pair of grains$G , G ^ { \prime } \in \mathcal { G } _ { T _ { \theta } }$ with$Y ( G ) \cap Y ( G ^ { \prime } ) \neq \emptyset$are contained in a common prism. Let$\mathcal { P }$denote this set of prisms; then for each$P \in \mathcal { P } , \mathcal { G } _ { T _ { \theta } } ^ { P }$is a set of prisms, each of which has dimensions roughly$\textstyle { \frac { \rho } { \theta } } \times { \frac { \rho } { \theta } } \times 1$(more precisely, each prism in$\dot { \mathcal { G } } _ { T _ { \theta } } ^ { P }$has dimensions comparable to$s \times t \times 1$, where$s , t \in [ \delta ^ { \varepsilon _ { 2 } } \frac { \rho } { \theta } , \frac { \rho } { \theta } ]$; this additional$\delta ^ { \varepsilon _ { 2 } }$ factor will be harmless). After pigeonholing, we may assume that the lengths s and t are the same for every$T _ { \theta } \in \mathbb { T } _ { \theta }$and every$P \in { \mathcal { P } }$

We have$C _ { K T - C W } ( \mathcal { G } _ { T _ { \theta } } ^ { P } ) \lesssim \delta ^ { - \varepsilon _ { 2 } } C _ { K T - C W } ^ { \mathrm { l o c } } ( \mathcal { G } ) \leq \delta ^ { - \varepsilon _ { 1 } - \varepsilon _ { 2 } }$, while

$$
C _ {F - S W} (\mathcal {G} _ {T _ {\theta}} ^ {P}) \leq C _ {F - C W} (\mathcal {G} _ {T _ {\theta}} ^ {P}) \leq C _ {K T - C W} (\mathcal {G} _ {T _ {\theta}} ^ {P}) (\rho / \theta) ^ {- 2} (\# \mathcal {G} _ {T _ {\theta}} ^ {P}) ^ {- 1} \leq \delta^ {- \varepsilon_ {1} - 2 \varepsilon_ {2}} (\rho / \theta) ^ {- 2} (\# \mathcal {G} _ {T _ {\theta}} ^ {P}) ^ {- 1}.
$$

If$\varepsilon _ { 2 }$is selected suficiently small depending on$\varepsilon _ { 3 } , \omega .$, and$\sigma _ { \mathrm { { ; } } }$then we can apply Assertion$\mathcal { E } ( \sigma , \omega )$

to conclude that

$$
\begin{array}{c} \Big | \bigcup_ {G ^ {P} \in \mathcal {G} _ {T _ {\theta}} ^ {P}} Y ^ {P} (G ^ {P}) \Big | \geq \big (\frac {\rho}{\theta} \big) ^ {\omega + \varepsilon_ {3}} \delta^ {5 \varepsilon_ {2}} (\# \mathcal {G} _ {T _ {\theta}} ^ {P}) | G ^ {P} | \Big (\big [ (\rho \theta) ^ {- 2} (\# \mathcal {G} _ {T _ {\theta}} ^ {P}) ^ {- 1} \big ] \big [ \# \mathcal {G} _ {T _ {\theta}} ^ {P} \big ] \big [ | G ^ {P} | ^ {1 / 2} \big ] \Big) ^ {- \sigma} \\ \gtrsim_ {\delta} \big (\frac {\rho}{\theta} \big) ^ {\omega + \varepsilon_ {3}} \delta^ {5 \varepsilon_ {2}} (\# \mathcal {G} _ {T _ {\theta}} ^ {P}) | G ^ {P} | \big (\frac {\rho}{\theta} \big) ^ {\sigma}, \end{array}
$$

and thus

$$
\mu_ {\text { medium }} \lesssim_ {\delta} \delta^ {- 2 \varepsilon_ {3}} \left(\frac {\rho}{\theta}\right) ^ {- \omega - \sigma}.\tag{9.8}
$$

Step 6. At this point, we have estimated the quantities$\mu _ { \mathrm { f i n e } }$and$\mu _ { \mathrm { { m e d i u m } } }$. The former allows us to control the number of$\delta$tubes that contribute to (a specific point in) a grain, while the latter allows us to control the number of grains that contribute to (a specific point in) a θ tube.

It remains to place a dense shading on$\mathbb { T } _ { \theta }$and obtain a corresponding multiplicity estimate for the number of θ tubes that contribute to (a specific point in)$\mathbb { R } ^ { \bar { 3 } }$. After dyadic pigeonholing, we can refine$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$and$\mathbb { T } _ { \rho }$so that for each$T _ { \theta } \in \mathbb { T } _ { \theta }$and each$x \in \mathsf { U } _ { T \in \mathbb { T } _ { 1 } [ T _ { \theta } ] } Y _ { 1 } ( T )$, we have that $\begin{array} { r } { | B ( x , \theta ) \cap \bigcup _ { T \in \mathbb { T } _ { 1 } [ T _ { \theta } ] } Y ( T ) | } \end{array}$has roughly the same volume. Let$\begin{array} { r } { Y ( T _ { \theta } ) = T _ { \theta } \stackrel { \cdot } { \cap } \dot { N } _ { \theta } \big ( \bigcup _ { T \in \mathbb { T } _ { 1 } [ T _ { \theta } ] } Y _ { 1 } ( T ) \big ) } \end{array}$; then$( \mathbb { T } _ { \theta } , Y ) _ { \theta } { \mathrm { ~ i s ~ } } { \gtrapprox } \delta ^ { \varepsilon _ { 1 } }$dense. After further pigeonholing we can find a number$\mu _ { \mathrm { c o a r s e } }$so that

$$
\# (\mathbb {T} _ {\theta}) _ {Y} (x) \sim \mu_ {\mathrm{coarse}} \quad \text { for   each } x \in \bigcup_ {T _ {\theta} \in \mathbb {T} _ {\theta}} Y (T _ {\theta}).
$$

By Remark$4 . 3 ( \mathrm { A } )$, we have$C _ { F - S W } ( \mathbb { T } _ { \theta } ) \lesssim C _ { F - S W } ( \mathbb { T } ) \lesssim _ { \delta } \delta ^ { - \varepsilon _ { 1 } }$, and$C _ { K T - C W } ( \mathbb { T } _ { \theta } ) \lesssim \delta ^ { - \varepsilon _ { 3 } } C _ { K T - C W } ( \mathcal { Z } ) \lesssim \delta$ $\delta ^ { - \varepsilon _ { 3 } }$. Thus if$\varepsilon _ { 1 }$is chosen suficiently small compared to$\varepsilon _ { 2 } .$, then we can apply$\mathcal { E } ( \sigma , \omega )$to conclude that

$$
\Big | \bigcup_ {T _ {\theta} \in \mathbb {T} _ {\theta}} Y (T _ {\theta}) \Big | \gtrsim \theta^ {\omega + \varepsilon_ {2} + \varepsilon_ {3}} (\# \mathbb {T} _ {\theta}) | T _ {\theta} | \Big ((\# \mathbb {T} _ {\theta}) | T _ {\theta} | ^ {1 / 2} \Big) ^ {- \sigma},
$$

and hence

$$
\mu_ {\text { coarse }} \lesssim \theta^ {- \omega - \varepsilon_ {2} - \varepsilon_ {3}} \left(\left(\# \mathbb {T} _ {\theta}\right) \theta\right) ^ {\sigma}.\tag{9.9}
$$

Combining (9.7), (9.8), and (9.9), we conclude that for each$\boldsymbol { x } \in \mathbb { R } ^ { 3 }$we have

$$
\begin{array}{c} \# \{T \in \mathbb {T} _ {1} \colon x \in Y _ {1} (T) \} \leq \mu_ {\text {fine}}   \mu_ {\text {medium}}   \mu_ {\text {coarse}} \\ \lesssim \delta^ {- 4 \varepsilon_ {3} + \sigma \zeta} \delta^ {- \omega} \Big ((\# \mathbb {T}) \delta \Big) ^ {\sigma}. \end{array}\tag{9.10}
$$

We conclude that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim_ {\delta} \delta^ {\omega + 4 \varepsilon_ {3} - \sigma \zeta} (\# \mathbb {T} _ {1}) | T | \Big ((\# \mathbb {T}) | T | ^ {1 / 2} \Big) ^ {- \sigma}.
$$

Since$\# \mathbb { T } _ { 1 } \gtrapprox \delta \mathrm { ~ } \delta ^ { \varepsilon _ { 1 } } ( \# \mathbb { T } )$, we have that Conclusion (A) holds, provided we select$\varepsilon _ { 3 } < \sigma \zeta / 1 0$and $\alpha < \sigma \zeta / 1 0$□

## 10 Sticky Kakeya for tubes satisfying the Katz-Tao Convex Wolf Axioms at every Scale

In Section 6, we recalled a version of the Sticky Kakeya Theorem that was proved in [26]; this is Theorem 6.2. Theorem 6.2 applies to families of tubes that satisfy the Frostman Convex Wolf

Axioms at every scale, in the sense of Definition 6.1. In this section, we will prove an analogue of Theorem 6.2 for sets of tubes that satisfy the Katz-Tao Convex Wolf Axioms at every scale.

Definition 10.1. Let$K \ge 1 , \delta > 0$. We say a set$\mathbb { T }$of essentially distinct δ-tubes satisfies the Katz-Tao Wolf Axioms at every scale with error K if for every$\rho _ { 0 } \in [ \delta , 1 ]$, there exists$\rho \in [ \rho _ { 0 } , K \rho _ { 0 } )$and a set of ρ-tubes$\mathbb { T } _ { \rho }$that satisfies the following properties.

(i)$\mathbb { T } _ { \rho }$is a K-balanced partitioning cover of$\mathbb { T } .$.

(ii)$C _ { K T - C W } ( \mathbb { T } _ { \rho } ) \leq K$

Theorem 10.2. For all$\varepsilon > 0$, there exists$\eta , \kappa > 0$so that the following holds for all$\delta > 0$. Let $\mathbb { T }$be a set of δ-tubes that satisfy the Katz-Tao Convex Wolf Axioms at every scale with error$\delta ^ { - \eta }$ and let$Y ( T )$be a$\delta ^ { \eta }$dense shading. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\varepsilon} (\# \mathbb {T}) | T |.\tag{10.1}
$$

In the next section, we will combine Theorem 10.2 with Proposition 9.1 to prove Proposition 1.7. Theorem 10.2 is proved by combining Theorem 6.2 with the following Nikishin-Stein-Pisier Factorization type result.

Proposition 10.3. Let$\varepsilon > 0$. Then there exists$K _ { \varepsilon } , \eta > 0$so that the following holds for all$\delta > 0$ Let T be a non-empty set of δ tubes inside the unit ball in$\mathbb { R } ^ { 3 }$that satisfy the Katz-Tao Convex Wolf axioms at every scale with error$\delta ^ { - \eta }$. Then there exist rigid transformations$A _ { 1 } , \dotsc , A _ { N }$ $N \leq K _ { \varepsilon } ( \# \mathbb { T } ) ^ { - 1 } | T | ^ { - 1 }$so that each set$A _ { i } ( \mathbb { T } )$is contained inside$B ( 0 , 2 )$, and$\textstyle \bigcup _ { i = 1 } ^ { N } A _ { i } ( \mathbb { T } )$contains a subset of essentially distinct tubes that satisfies the Frostman Convex Wolf Axioms at every scale with error$K _ { \varepsilon } \delta ^ { - \varepsilon }$

Proof of Theorem 10.2 using Proposition 10.3. Fix$\varepsilon > 0$and let$\eta = \eta ( \varepsilon ) > 0$be a small quantity to be determined below. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, and suppose that T satisfies the Katz-Tao Wolf Axioms at every scale with error$\delta ^ { - \eta }$. After a harmless refinement we may suppose$| Y ( T ) | \geq \delta ^ { 2 \eta } | T |$ for each$T \in \mathbb { T }$

Apply Proposition 10.3 with a small value$\varepsilon _ { 1 }$in place of$\varepsilon .$We may do this, provided$\eta$is selected suficiently small depending on ε . Let$\begin{array} { r } { \tilde { \mathbb { T } } \subset \bigcup _ { i = 1 } ^ { N } A _ { i } ( \mathbb { T } ) } \end{array}$be the output from Proposition 10.3. Note that each$\tilde { T } \in \tilde { \mathbb { T } }$is of the form$\tilde { \cal T } = A _ { i } ( T )$for some index i and some$T \in \mathbb { T }$, and hence we can define the shading$\tilde { Y } ( \tilde { T } ) = A _ { i } ( Y ( T ) )$; we have$| \tilde { Y } ( \tilde { T } ) | = | Y ( T ) | \ge \delta ^ { 2 \eta } | T |$, and hence$( \tilde { T } , \tilde { Y } ) _ { \delta }$ is$\delta ^ { 2 \eta }$dense.

If$\varepsilon _ { 1 }$and$\eta$are chosen suficiently small depending on$\varepsilon ,$then we can apply Theorem 6.2 to conclude that

$$
N \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | = \sum_ {i = 1} ^ {N} \Big | \bigcup_ {T \in \mathbb {T}} A _ {i} (Y (T)) \Big | \geq \Big | \bigcup_ {i = 1} ^ {N} \bigcup_ {T \in \mathbb {T}} A _ {i} (Y (T)) \Big | \geq \Big | \bigcup_ {\tilde {T} \in \tilde {\mathbb {T}}} \tilde {Y} (\tilde {T}) \Big | \geq \kappa_ {\varepsilon} \delta^ {\varepsilon}.
$$

Re-arranging and noting that$N \leq K _ { \varepsilon } ( \# \mathbb { T } ) ^ { - 1 } | T | ^ { - 1 }$, we obtain (10.1), with$\kappa = \kappa _ { \varepsilon } K _ { \varepsilon } ^ { - 1 }$

It remains to prove Proposition 10.3. We will do so below.

## 10.1 Nikishin-Stein-Pisier Factorization and the Convex Wolf Axioms

We begin with a single-scale version of Proposition 10.3. We first need the following definition.

Definition 10.4. We say that a set T of δ tubes is regular with granularity$\tau \in [ \delta , 1 ]$if for every scale$\rho \in [ \delta , 1 ]$of the form$\rho = \delta \tau ^ { - \ell } , \ell \in \mathbb { N }$, we have that$\mathbb { T }$has a balanced partitioning cover by$\rho$ tubes.

Definition 10.5. For$\rho > 0$, we define${ \mathfrak { A } } _ { \rho }$to be the set of rigid transformations$A \colon \mathbb { R } ^ { 3 }  \mathbb { R } ^ { 3 }$that satisfy$| A x - x | \leq \rho$for all$x \in B ( 0 , 1 )$

Lemma 10.6. For all$\varepsilon > 0$, there exists$\eta > 0$and$K _ { \varepsilon } \geq 1$so that the following holds for all $0 < \delta \le \rho \le 1$. Let$K , M \ge 1$and let$\mathbb { T } _ { 1 } , \dots , \mathbb { T } _ { K }$be sets of δ tubes in$B ( 0 , 1 ) \subset \mathbb { R } ^ { 3 }$, each of cardinality at most M. Suppose that the tubes in each set$\mathbb { T } _ { j }$are regular with granularity$\delta ^ { \eta }$, and furthermore each set$\mathbb { T } _ { j }$is contained in a$\rho$tube.

Then there exists a set of rigid transformations${ \mathcal { A } } \subset { \mathfrak { A } } _ { \rho }$with$\begin{array} { r } { \# \mathcal { A } = \left\lceil \frac { \rho ^ { 2 } } { M \delta ^ { 2 } } \right\rceil } \end{array}$, so that

$$
C _ {K T - C W} \Big (\bigsqcup_ {A \in \mathcal {A}} A (\mathbb {T} _ {j}) \Big) \leq K _ {\varepsilon} \delta^ {- \varepsilon} (\log (2 + K)) C _ {K T - C W} (\mathbb {T} _ {j}), \quad j = 1, \ldots , K.\tag{10.2}
$$

Remark 10.7. Note that for distinct$A , A ^ { \prime } \in { \mathcal { A } }$, the sets$A ( \mathbb { T } _ { j } )$and$A ^ { \prime } ( \mathbb { T } _ { j } )$might contain common tubes, and thus the disjoint union on the LHS of (10.2) should be interpreted as a multiset. By Remark 4.2(D), the LHS of (10.2) is well-defined.

Step 1. Define$\tilde { \delta } = \delta / \rho$. First, we may suppose that$M < \tilde { \delta } ^ { - 2 }$, or else we can define$A = \{ I \}$(here $I \colon \mathbb { R } ^ { 3 }  \mathbb { R } ^ { 3 }$is the identity map) and we are done. Similarly, we may suppose$\rho \ge \delta ^ { 1 - \varepsilon / 2 }$, or else we can define A to be$\textstyle \left\lceil { \frac { \rho ^ { 2 } } { M \delta ^ { 2 } } } \right\rceil$infinitesimally perturbed copies of$I ,$and (10.2) follows from the fact that

$$
C _ {K T - C W} \Big (\bigsqcup_ {A \in \mathcal {A}} A (\mathbb {T} _ {j}) \Big) \leq (\# \mathcal {A}) C _ {K T - C W} (\mathbb {T} _ {j}).
$$

Fix an index$j \in [ 1 , \ldots , K ]$and let$\mathbb { T } = \mathbb { T } _ { j }$. By hypothesis, all of the tubes in T are contained in a common ρ tube, which we will denote by$T _ { \rho }$. Fix numbers$\delta \leq a \leq b \leq 2 \rho$, with both a and b of the form$\delta ^ { \ell \eta }$. Let$\nu \geq 1$be a power of 2. By hypothesis, T has a balanced partitioning cover$\mathbb { T } _ { a }$

Let$\mathcal { W } _ { \nu }$be a maximal set of essentially distinct$a \times b \times 2$prisms, each of which satisfy$\# \mathbb { T } [ W ] \in$ $[ \nu \frac { \# \mathbb { T } } { \# \mathbb { T } _ { a } } , 2 \nu \frac { \# \mathbb { T } } { \# \mathbb { T } _ { a } } )$. Note that each$W \in \mathcal { W } _ { \nu }$is contained in$N _ { 2 \rho } ( T _ { \rho } )$. Observe that if W is an a ×$b \times 2$ prism and$\ddot { T } \in \mathbb { T } [ T _ { a } ]$with$T \subset W$, then$T _ { a } \subset 2 W$. In particular, since$\mathbb { T } _ { a }$is a balanced partitioning cover of T, we have

$$
\# \mathbb {T} _ {a} [ 2 W ] \geq \nu / 2 \quad \text { for   each } W \in \mathcal {W} _ {\nu}.
$$

Each tube$T _ { a } \in \mathbb { T } _ { a }$is contained in$\ \lesssim \ \frac { b } { a }$essentially distinct$2 a \times 2 b \times 4$prisms. Thus by double-counting we have

$$
\# \mathcal {W} _ {\nu} \lesssim (\# \mathbb {T} _ {a}) \frac {b}{a} \nu^ {- 1}.\tag{10.3}
$$

The above estimate is useful when ν is not too large. When$\nu \frac { \# \mathbb { T } } { \# \mathbb { T } _ { a } } \geq C _ { K T - C W } ( \mathbb { T } ) ( a b ) | T | ^ { - 1 }$, then $\mathcal { W } _ { \nu } = \emptyset$

Step 2. We say two rigid motions A,$A ^ { \prime } \in \mathfrak { A } _ { \rho }$are$\delta \cdot$-separated if there exists a point$x \in B ( 0 , 1 )$with $| A ( x ) - A ^ { \prime } ( x ) | \geq \delta$. Let$\mathfrak { A } _ { \rho } ^ { \delta }$be a maximal δ-separated subset of${ \mathfrak { A } } _ { \rho } ;$we have$\# \mathfrak { A } _ { \rho } ^ { \delta } \sim \tilde { \delta } ^ { - 6 } = \delta ^ { 6 } / \rho ^ { 6 }$

Let

$$
N = 2 \Bigl \lceil \frac {\rho^ {2}}{M \delta^ {2}} \Bigr \rceil ,\tag{10.4}
$$

and let$A _ { 1 } , \dotsc , A _ { N }$be chosen uniformly and independently at random from$\mathfrak { A } _ { \rho } ^ { \delta } .$. We have

$$
\mathbb {P} \big (\# \{A _ {1}, \dots , A _ {N} \} \geq N / 2 \big) \geq 3 / 4,\tag{10.5}
$$

where$\# \{ A _ { 1 } , \ldots , A _ { N } \}$denotes the number of distinct rigid motions in the set$\{ A _ { 1 } , . . . , A _ { N } \}$

Fix a$a \times b \times 2$prism$W _ { 0 }$. We would like to estimate the probability that

$$
\# \Big (\bigcup_ {i = 1} ^ {N} A _ {i} (\mathbb {T}) \Big) [ W _ {0} ] \geq K _ {\varepsilon} \delta^ {- \varepsilon / 2} (\log (2 + K)) C _ {K T - C W} (\mathbb {T}) | W _ {0} | | T | ^ {- 1},\tag{10.6}
$$

i.e. we would like to estimate the probability that

$$
\sum_ {i = 1} ^ {N} \# \mathbb {T} [ (A _ {i} ^ {- 1} (W _ {0})) ] \geq K _ {\varepsilon} \delta^ {- \varepsilon / 2} (\log (2 + K)) C _ {K T - C W} (\mathbb {T}) | W _ {0} | | T | ^ {- 1}.\tag{10.7}
$$

Note that if (10.7) occurs, then by pigeonholing, there must be some dyadic ν so that

$$
\# \left\{\left(W, i\right) \in \left(\mathcal {W} _ {\nu} \times \{1, \dots , N \}\right): A _ {i} (W) \text {is contained in} 1 0 W _ {0} \right\} \geq Z _ {\nu},\tag{10.8}
$$

where

$$
Z _ {\nu} = \left(4 \log (1 / \delta)\right) ^ {- 1} K _ {\varepsilon} \delta^ {- \varepsilon / 2} (\log (2 + K)) C _ {K T - C W} (\mathbb {T}) | W _ {0} | | T | ^ {- 1} \Big (\sup _ {W \in \mathcal {W} _ {\nu}} \# \mathbb {T} [ W ] \Big) ^ {- 1}.\tag{10.9}
$$

We may suppose that

$$
\sup _ {W \in \mathcal {W} _ {\nu}} \# \mathbb {T} [ W ] \sim \nu \frac {\# \mathbb {T}}{\# \mathbb {T} _ {a}} \leq C _ {K T - C W} (\mathbb {T}) (a b) | T | ^ {- 1},\tag{10.10}
$$

since otherwise$\mathcal { W } _ { \nu } = \emptyset$, and thus it is impossible for either of Inequality (10.8) or (10.7) to be true. Since$| W _ { 0 } | = 2 a b .$, we can use (10.10) to bound$Z _ { \nu }$. We conclude that

$$
Z _ {\nu} \geq \left(2 \log (1 / \delta)\right) ^ {- 1} K _ {\varepsilon} \delta^ {- \varepsilon / 2} (\log (2 + K)).
$$

We will choose the constant$K _ { \varepsilon }$suficiently large so that$Z _ { \nu } \geq 2$, and in particular

$$
Z _ {\nu} - 1 \sim Z _ {\nu}.\tag{10.11}
$$

This will be relevant in Step 3 when we apply Chernof’s inequality.

Step 3. We will estimate the probability that (10.8) occurs for a fixed choice of ν and$W _ { 0 }$. For two$a \times b \times 2$prisms$W , W _ { 0 } ,$, both of which are contained inside$N _ { 2 \rho } ( T _ { \rho } )$we have that the number of$A \in \mathfrak { A } _ { \rho } ^ { \delta }$for which$A ( W )$is comparable to$W _ { 0 }$(or equivalently,$A ^ { - 1 } ( W _ { 0 } )$is comparable to W) is $\lesssim \delta ^ { - 6 } a ^ { 2 } b ^ { 2 } \rho \operatorname* { m i n } \{ a / b , \rho \}$. We will write this as$\tilde { \delta } ^ { - 6 } \tilde { a } ^ { 2 } \tilde { b } ^ { 2 } \operatorname* { m i n } \{ \tilde { a } / ( \tilde { b } \rho ) , 1 \} \leq \tilde { \delta } ^ { - 6 } \tilde { a } ^ { 2 } \tilde { b } ^ { 2 }$, where we define $\tilde { a } = a / \rho$and$\tilde { b } = b / \rho$

The reason for this numerology is as follows. Without loss of generality, assume$W _ { 0 } = [ 0 , a ] \times$ $[ 0 , b ] \times [ 0 , 2 ]$. Then a rigid motion A is determined by$A ( v _ { i } )$with$v _ { 0 } = ( 0 , 0 , 0 ) , v _ { 1 } = ( 0 , 1 , 0 ) , v _ { 2 } =$ (0, 0, 1). Since$A \in \mathfrak { A } _ { \rho } ^ { \delta }$, the number of δ-separated choice for$\begin{array} { r } { A ( v _ { 0 } ) \mathrm { ~ i s } \le \frac { | W \cap B ( 0 , \rho ) | } { \delta ^ { 3 } } \sim \frac { a b \rho } { \delta ^ { 3 } } } \end{array}$. Once

$A ( v _ { 0 } )$is fixed, the number of δ-separated choices for$\textstyle A ( v _ { 2 } ) { \mathrm { ~ i s ~ } } \leq { \frac { a b } { \delta ^ { 2 } } }$. Once$A ( v _ { 0 } ) , A ( v _ { 2 } )$are fixed, the number of δ-separated choices for$\begin{array} { r } { A ( v _ { 1 } ) \mathrm { ~ i s } \le \operatorname* { m i n } \{ \frac { a } { b } , \rho \} \delta ^ { - 1 } } \end{array}$

Thus if we define$X _ { i }$to be the event that there exists$W \in \mathcal W _ { \nu }$such that$A _ { i } ( W )$is comparable to$W _ { 0 }$, then

$$
\mathbb {P} (X _ {i}) \lesssim \tilde {\delta} ^ {- 6} \tilde {a} ^ {2} \tilde {b} ^ {2} \cdot \# \mathfrak {A} _ {\rho} ^ {\delta} \cdot \# \mathcal {W} _ {\nu} \lesssim \tilde {a} ^ {2} \tilde {b} ^ {2} (\# \mathcal {W} _ {\nu}).\tag{10.12}
$$

Since the prisms in$\mathcal { W } _ { \nu }$are essentially distinct, there can exist at most$O ( 1 ) \ W \in \mathcal { W } _ { \nu }$such that $A _ { i } ( W )$is comparable to$W _ { 0 }$. Thus by linearity of expectation, we have

$$
\begin{array}{l} \mathbb {E} \Big (\# \{(W, i) \in (\mathcal {W} _ {\nu} \times \{1, \ldots , N \}) \colon A _ {i} (W) \text {is comparable to} W _ {0} \} \Big) \\ = \mathbb {E} (X _ {1} + \ldots + X _ {N}) \\ \lesssim N \tilde {a} ^ {2} \tilde {b} ^ {2} (\# \mathcal {W} _ {\nu}) \\ \lesssim 2 \Big [ \frac {\rho^ {2}}{M \delta^ {2}} \Big ] \tilde {a} ^ {2} \tilde {b} ^ {2} (\# \mathcal {W} _ {\nu}) \end{array}
$$

On the third line we used (10.12); on the fourth line we used (10.4) and (10.3).

Define$X = X _ { 1 } + \dots + X _ { N }$. Recalling (10.9) and (10.11), we have

$$
\begin{array}{l} \gamma := \frac {Z _ {\nu}}{\mathbb {E} (X)} \gtrsim \log (1 / \delta) ^ {- 1} K _ {\varepsilon} \delta^ {- \varepsilon / 2} (\log (2 + K)) C _ {K T - C W} (\mathbb {T}) | W _ {0} | | T | ^ {- 1} \Big (2 \Big \lceil \frac {\rho^ {2}}{M \delta^ {2}} \Big \rceil \tilde {a} ^ {2} \tilde {b} ^ {2} \sup _ {W \in \mathcal {W} _ {\nu}} \# \mathbb {T} [ W ] \cdot (\# \mathcal {W} _ {\nu}) \Big) ^ {- 1} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}
$$

On the second line we used (10.3) and the inequality$\# \mathbb { T } [ W ] \sim \nu { \frac { \# \mathbb { T } } { \mathbb { T } _ { a } } } ;$; on the third line we used the fact that$| T | \sim \delta ^ { 2 }$and the fact that$\tilde { a } = a / \rho ;$and on the final line we used the fact that $C _ { K T - C W } ( \mathbb { T } ) \geq 1 , \tilde { b } ^ { 2 } \leq 4 , | W _ { 0 } | = 2 a b$, and$\# \mathbb { T } \leq M$

Hence we can apply the multiplicative Chernof’s inequality to conclude that

$$
\mathbb {P} (X \geq Z _ {\nu}) \leq \left(\frac {e ^ {\gamma - 1}}{\gamma^ {\gamma}}\right) ^ {\mathbb {E} (X)} \lesssim e ^ {- \gamma \mathbb {E} (X)} = e ^ {- Z _ {\nu}} \lesssim (2 + K) ^ {- (\log 1 / \delta) ^ {- 1} K _ {\varepsilon} \delta^ {- \varepsilon / 2}} \lesssim K ^ {- 1} \exp [ - K _ {\varepsilon} \delta^ {- \varepsilon / 3} ].
$$

For the second inequality, we used the fact that$K _ { \varepsilon }$is suficiently large,$\frac { e ^ { \gamma - 1 } } { \gamma ^ { \gamma } } \leq e ^ { - \gamma }$for all$\delta > 0$ and$K \geq 1$

Step 4. There are$\log ( 1 / \delta )$choices of$\nu ;$at most$a ^ { - 3 } b ^ { - 1 } \leq \delta ^ { - 4 }$essentially distinct prisms$W _ { 0 } ;$ and$\eta ^ { - 2 }$choices of numbers$( a , b )$Thus the probability that there exists some prism$W \subset$ $N _ { 2 \rho } ( T _ { \rho } )$of dimensions$a \times b \times 2$for some pair$a \leq b$of the form$\delta ^ { \eta \ell }$for which (10.6) holds is $\lesssim \delta ^ { - 6 } K ^ { - 1 } \exp [ - K _ { \varepsilon } \delta ^ { - \varepsilon / 3 } ]$. We will select$K _ { \varepsilon }$suficiently large so that this quantity is at most $( 2 K ) ^ { - 1 }$. If no such prism exists, then provided$\eta \le \varepsilon / 4$we have

$$
C _ {K T - C W} \left(\bigsqcup_ {i = 1} ^ {N} A _ {i} (\mathbb {T})\right) \leq K _ {\varepsilon} \delta^ {- \varepsilon} (\log (2 + K)) C _ {K T - C W} (\mathbb {T}).\tag{10.13}
$$

Indeed, for every prism$W \subset \mathbb { R } ^ { 3 }$of dimensions$a \times b \times 2$, we can select a prism$W ^ { \prime } \subset W$of dimensions $a ^ { \prime } \times b ^ { \prime } \times 2$with$a ^ { \prime } , b ^ { \prime }$of the form$\delta ^ { \ell \eta }$and$| W ^ { \prime } | \leq \delta ^ { - 2 \eta } | W | \leq \delta ^ { - \varepsilon / 2 } | W |$

In particular, we have that (10.13) holds with probability at least$1 - ( 2 K ) ^ { - 1 }$. Since there are K sets of tubes$\mathbb { T } _ { 1 } , \dots , \mathbb { T } _ { K }$, we conclude that with probability at least$1 / 2$, we have that (10.13) is true for every set$\mathbb { T } _ { 1 } , \dots , \mathbb { T } _ { K }$. Finally, by (10.5), we have that the probability that$\# . A \geq N / 2$ and (10.13) is true for every set$\mathbb { T } _ { 1 } , \dots , \mathbb { T } _ { K }$is at least$1 / 4$. We conclude that there exists a choice of$A _ { 1 } , \dotsc , A _ { N }$and a set$\mathcal { A } \subset \{ A _ { 1 } , . . . A _ { N } \}$of cardinality$\left\lceil \frac { \rho ^ { 2 } } { M \delta ^ { 2 } } \right\rceil$so that (10.2) holds.□

Lemma 10.6 has the following consequence.

Corollary 10.8. For all$\varepsilon > 0$, there exists$\eta > 0$and$K _ { \varepsilon } \geq 1$so that the following holds for all $0 < \delta \le \rho \le 1$. Let T be a set of δ-tubes, and let$\mathbb { T } _ { \rho }$be a balanced partitioning cover of T. Suppose that for each$T _ { \rho } \in \mathbb { T } _ { \rho } ,$we have that$\mathbb { T } ^ { T _ { \rho } }$is regular with granularity$( \delta / \rho ) ^ { \eta }$

Then there exists a set of rigid transformations A with #$\begin{array} { r } { A = 2 \lceil \frac { \# \mathbb { T } _ { \rho } } { \# \mathbb { T } } \frac { | T _ { \rho } | } { | T | } \rceil } \end{array}$and

$$
A (T _ {\rho}) \subset N _ {3 \rho} (T _ {\rho}) \quad f o r e a c h A \in \mathcal {A}, T _ {\rho} \in \mathbb {T} _ {\rho},\tag{10.14}
$$

so that

$$
C _ {K T - C W} \left(\left(\bigsqcup_ {A \in \mathcal {A}} A (\mathbb {T})\right) \left[ N _ {3 \rho} (T _ {\rho}) \right]\right) \leq K _ {\varepsilon} \delta^ {- \varepsilon} C _ {K T - C W} (\mathbb {T}) \quad f o r e a c h T _ {\rho} \in \mathbb {T} _ {\rho}.\tag{10.15}
$$

Remark 10.9. An immediate application of Lemma 10.6 yields the slightly weaker statement

$$
C _ {K T - C W} \left(\left(\bigsqcup_ {A \in \mathcal {A}} A (\mathbb {T} [ T _ {\rho} ])\right)\right) \leq K _ {\varepsilon} \delta^ {- \varepsilon} C _ {K T - C W} (\mathbb {T}) \quad \text { for   each } T _ {\rho} \in \mathbb {T} _ {\rho},
$$

but (10.15) follows from the hypothesis that the tubes in$\mathbb { T } _ { \rho }$are essentially distinct, and hence there are$\lesssim 1$tubes$T _ { \rho } ^ { \prime } \in \mathbb { T } _ { \rho }$for which$\begin{array} { r } { \big ( \lfloor \rfloor _ { A } A ( \mathbb { T } [ T _ { \rho } ^ { \prime } ] ) \big ) [ T _ { \rho } ] } \end{array}$is non-empty.

We are now ready to prove Proposition 10.3.

Proof of Proposition 10.3. Step 1. Fix$\varepsilon > 0$. Let$\varepsilon _ { 1 } > 0$be a small quantity to be chosen below. We will choose$\varepsilon _ { 1 }$small compared to$\varepsilon ,$and η small compared to$\varepsilon _ { 1 }$. Let T be a set of$\delta$tubes that satisfy the Katz-Tao Convex Wolf axioms at every scale with error$\delta ^ { - \eta }$

Provided we select$\eta \leq \varepsilon$, there exists a number$J \sim \varepsilon ^ { - 1 }$and scales$1 = \rho _ { 0 } > \rho _ { 1 } > . . . > \rho _ { J } = \delta$ with$\delta ^ { \varepsilon } \le \rho _ { j + 1 } / \rho _ { j } < 1 / 8$for each index$j ,$, so that the following holds: for each index$j = 0 , \ldots , J - 1$ there is a δ<sup>−η</sup>-balanced partitioning cover$\mathbb { T } _ { \rho _ { j } }$of T, with$C _ { K T - C W } ( \mathbb { T } _ { \rho _ { j } } ) \le \delta ^ { - \eta }$. Define$\mathbb { T } _ { \rho _ { J } } = \mathbb { T }$

Currently,$\mathbb { T } _ { \rho _ { j } }$covers$\mathbb { T } _ { : }$but unfortunately, it might not be the case that$\mathbb { T } _ { \rho _ { j } }$covers$\mathbb { T } _ { \rho _ { j + 1 } } .$ We can fix this as follows. We know that for each index$j > 0$, we have$\mathbb { T } [ T _ { \rho _ { j + 1 } } ] \neq \emptyset$for each $T _ { \rho _ { j + 1 } } \in \mathbb { T } _ { \rho _ { j + 1 } }$. Since$\mathbb { T } _ { \rho _ { j } }$covers$\mathbb { T } .$, we have that for each$T _ { \rho _ { j + 1 } } \in \mathbb { T } _ { \rho _ { j + 1 } }$, there exists$T _ { \rho _ { j } } \in \mathbb { T } _ { \rho _ { j } }$so that$\mathbb { T } [ T _ { \rho _ { j + 1 } } ] \cap \mathbb { T } [ T _ { \rho _ { j } } ] \ \ne \ \emptyset$, and hence$T _ { \rho _ { j + 1 } } \cap T _ { \rho _ { j } }$contains a unit line segment. But this implies that$T _ { \rho _ { j + 1 } } ~ \subset ~ { \cal N } _ { 2 \rho _ { j + 1 } } ( T _ { \rho _ { j } } )$Thus, if we replace each set$\mathbb { T } _ { \rho _ { j } }$with$\{ N _ { 2 \rho _ { j + 1 } } ( T _ { \rho _ { j } } ) \colon T _ { \rho _ { j } } ~ \in ~ \mathbb { T } _ { \rho _ { j } } \}$for $j = 0 , \ldots , J - 1$(leaving$\mathbb { T } _ { \rho _ { J } }$unchanged), then for each index$j$we have that$\mathbb { T } _ { \rho _ { j } }$covers$\mathbb { T } _ { \rho _ { j + 1 } }$ It is still the case that$\mathbb { T } _ { \rho _ { j } }$is$\mathrm { ~ a ~ } \lesssim \delta ^ { - \eta } .$-balanced cover of$\mathbb { T }$, and hence$\mathbb { T } _ { \rho _ { j } }$is$\mathrm { ~ a ~ } \lesssim \delta ^ { - 2 \eta }$-balanced cover of$\mathbb { T } _ { \rho _ { j + 1 } }$. Abusing notation, we will continue to refer to these sets as$\mathbb { T } _ { \rho _ { j } }$(even though this set is technically a collection of$( \rho _ { j } + 2 \rho _ { j + 1 } )$tubes; since$\rho _ { j + 1 } \leq \rho _ { j } / 4$, this distinction will not be important). Note that it might no longer be the case that the tubes in$\mathbb { T } _ { \rho _ { j } }$are essentially distinct, nor that$\mathbb { T } _ { \rho _ { j } }$is a partitioning cover of T.

Step 2.

After dyadic pigeonholing, we can replace each set$\mathbb { T } _ { \rho _ { j } }$by a subset (abusing notation, we will continue to refer to this subset as$\mathbb { T } _ { \rho _ { j } } )$so that$\# \mathbb { T } _ { \rho _ { J } } \gtrapprox$#T, and the following holds for each $j = 0 , \ldots , J ,$. (To simplify notation, we define$\tilde { T } _ { \rho _ { j } } = N _ { 3 \rho _ { j } } ( T _ { \rho _ { j } } )$and$\tilde { \mathbb { T } } _ { \rho _ { j } } = \{ \tilde { T } _ { \rho _ { j } } \colon T _ { \rho _ { j } } \in \mathbb { T } _ { \rho _ { j } } \} \ )$.

(i) The tubes in$\tilde { \mathbb { T } } _ { \rho _ { j } }$are essentially distinct.

(ii) For each$T _ { \rho _ { j } } \in \mathbb { T } _ { \rho _ { j } }$, we have$\tilde { \mathbb { T } } _ { \rho _ { j + 1 } } [ \tilde { T } _ { \rho _ { j } } ] = \tilde { \mathbb { T } } _ { \rho _ { j + 1 } } [ T _ { \rho _ { j } } ]$

(iii)$\mathbb { T } _ { \rho _ { j } }$is a balanced partitioning cover of$\tilde { \mathbb { T } } _ { \rho _ { j + 1 } }$

(iv) for each$T _ { \rho _ { j } } \in \mathbb { T } _ { \rho _ { j } }$, we have that$( \tilde { \mathbb { T } } _ { \rho _ { j + 1 } } ) ^ { T _ { \rho _ { j } } }$is regular with granularity$( 3 \rho _ { j } / \rho _ { j + 1 } ) ^ { \eta _ { 1 } }$

For each index$j = 1 , \dots , J$, apply Corollary 10.8 with$\varepsilon _ { 1 }$in place of$\varepsilon , \tilde { \mathbb { T } } _ { \rho _ { j } }$in place of$\mathbb { T } , \mathbb { T } _ { \rho _ { j - 1 } }$ in place of$\mathbb { T } _ { \rho } , 3 \rho _ { j }$in place of δ, and$3 \rho _ { j } / \rho _ { j - 1 }$in place of$\rho .$. Let$A _ { j }$be the output of Corollary 10.8.

By (10.14) plus Item (ii) above, for each$T _ { \rho _ { j - 1 } } \in \mathbb { T } _ { \rho _ { j - 1 } }$, we have

$$
\bigsqcup_ {A \in \mathcal {A} _ {j}} A (\tilde {\mathbb {T}} _ {\rho_ {j}} [ \tilde {T} _ {\rho_ {j - 1}} ]) = \bigsqcup_ {A \in \mathcal {A} _ {j}} A (\tilde {\mathbb {T}} _ {\rho_ {j}} [ T _ {\rho_ {j - 1}} ]) \subset \tilde {T} _ {\rho_ {j - 1}},\tag{10.16}
$$

and hence by Item (iii),

$$
\tilde {\mathbb {T}} _ {\rho_ {j - 1}} \text {   covers   } \bigsqcup_ {A \in \mathcal {A} _ {j}} A (\tilde {\mathbb {T}} _ {\rho_ {j}}).\tag{10.17}
$$

Here the disjoint union is in the sense of multi-sets.

We have

$$
\# \Big (\Big (\bigsqcup_ {A \in \mathcal {A} _ {j}} A (\tilde {\mathbb {T}} _ {\rho_ {j}}) \Big) [ \tilde {T} _ {\rho_ {j - 1}} ] \Big) \geq (\# \mathcal {A} _ {j}) \Big (\frac {\# \tilde {\mathbb {T}} _ {\rho_ {j}}}{2 \# \mathbb {T} _ {\rho_ {j - 1}}} \Big) \gtrsim \frac {| T _ {\rho_ {j - 1}} |}{| T _ {\rho_ {j}} |} \quad \text {for each} T _ {\rho_ {j - 1}} \in \mathbb {T} _ {\rho_ {j - 1}}.\tag{10.18}
$$

By (10.15), there exists$C _ { \varepsilon _ { 1 } } \geq 1$so that

$$
C _ {K T - C W} \left(\left(\bigsqcup_ {A \in \mathcal {A} _ {j}} A (\tilde {\mathbb {T}} _ {\rho_ {j}})\right) [ \tilde {T} _ {\rho_ {j - 1}} ]\right) \leq C _ {\varepsilon_ {1}} \delta^ {- \varepsilon_ {1} - 2 \eta} \quad \text { for   each } \tilde {T} _ {\rho_ {j - 1}} \in \tilde {\mathbb {T}} _ {\rho_ {j - 1}}.\tag{10.19}
$$

Step 3. Define$\mathcal { A } ^ { ( 0 ) } = \{ I \}$and for$j = 1 , \dots , J ,$, define

$$
\mathcal {A} ^ {(j)} = \left\{A _ {1} \circ A _ {2} \circ \dots \circ A _ {j}: A _ {i} \in \mathcal {A} _ {i} \text {   for   each   } i = 1, \dots j \right\}.
$$

Define$\mathcal { A } = \mathcal { A } ^ { ( J ) }$; this set of transformations will be the output of Proposition 10.3.

For each index$j = 0 , \ldots , J ,$, define

$$
\hat {\mathbb {T}} _ {\rho_ {j}} = \bigsqcup_ {A \in \mathcal {A} ^ {(j)}} A (\tilde {\mathbb {T}} _ {\rho_ {j}}).
$$

By (10.17),$\hat { \mathbb T } _ { \rho _ { j - 1 } }$covers$\hat { \mathbb T } _ { \rho _ { j } }$for each$j = 1 , \dots , J ,$

By (10.18), for each$1 \le j \le J$and each$T _ { \rho _ { j - 1 } } \in \mathbb { T } _ { \rho _ { j - 1 } }$we have

$$
\# \hat {\mathbb {T}} _ {\rho_ {j}} [ \tilde {T} _ {\rho_ {j - 1}} ] \gtrsim \frac {| T _ {\rho_ {j - 1}} |}{| T _ {\rho_ {j}} |}.
$$

Thus after dyadic pigeonholing, we can replace each set$\hat { \mathbb T } _ { \rho _ { j } }$by a refinement$\hat { \mathbb { T } } _ { \rho _ { j } } ^ { \prime }$(in the sense of multi-sets), so that$\hat { \mathbb { T } } _ { \rho _ { j - 1 } } ^ { \prime }$is a balanced partitioning cover of$\hat { \mathbb { T } } _ { \rho _ { j } } ^ { \prime }$for each$j = 1 , \dots , J ,$, and for each$j = 1 , \dots , J$and each$T _ { \rho _ { j - 1 } } \in \mathbb { T } _ { \rho _ { j - 1 } }$we have

$$
\# \hat {\mathbb {T}} _ {\rho_ {j}} ^ {\prime} [ \tilde {T} _ {\rho_ {j - 1}} ] \gtrsim \delta^ {\eta} \frac {| T _ {\rho_ {j - 1}} |}{| T _ {\rho_ {j}} |},
$$

and hence

$$
\# \hat {\mathbb {T}} _ {\rho_ {J}} ^ {\prime} [ \tilde {T} _ {\rho_ {j}} ] \gtrsim \delta^ {\eta / \varepsilon} \frac {| T _ {\rho_ {j}} |}{| T |} \quad \text { for   each } \tilde {T} _ {\rho_ {j}} \in \hat {\mathbb {T}} _ {\rho_ {j}} ^ {\prime}.\tag{10.20}
$$

Step 4. Using Lemma 4.12 and (10.19), we have

$$
C _ {K T - C W} (\hat {\mathbb {T}} _ {\rho_ {J}} ^ {\prime}) \leq C _ {K T - C W} (\hat {\mathbb {T}} _ {\rho_ {J}}) \lesssim \prod_ {j = 1} ^ {J} \left(C _ {\varepsilon_ {1}} \delta^ {- \varepsilon_ {1} - 2 \eta}\right) \lesssim \delta^ {- 2 \varepsilon_ {1} J}.
$$

In particular, for each$T \in \hat { \mathbb { T } } _ { \rho _ { J } } ^ { \prime }$, there are$\lesssim \delta ^ { - 2 \varepsilon _ { 1 } J }$tubes$T ^ { \prime } \in \hat { \mathbb { T } } _ { \rho _ { J } } ^ { \prime }$comparable to$T .$. Recall that$J \sim \varepsilon ^ { - 1 }$. We will choose$\varepsilon _ { 1 }$suficiently small so that$2 \varepsilon _ { 1 } J < \varepsilon / 4$. Thus we can select a set $\begin{array} { r } { \mathbb { T } ^ { \dagger } \subset \hat { \mathbb { T } } _ { \rho _ { J } } ^ { \prime } \subset \bigcup _ { A \in \mathcal { A } } A ( \tilde { \mathbb { T } } _ { \rho _ { J } } ) } \end{array}$with$\# \mathbb { T } ^ { \dagger } \gtrsim \delta ^ { \varepsilon / 4 } ( \# \hat { \mathbb { T } } _ { \rho _ { J } } ^ { \prime } ) \geq \delta ^ { \varepsilon } | T | ^ { - 1 }$that consists of of essentially distinct tubes. The set$\mathbb { T } ^ { \dagger }$will be the output of Proposition 10.3.

It remains to verify that$\mathbb { T } ^ { \dagger }$satisfies the Frostman Convex Wolf Axioms at every scale, with error$\delta ^ { - \varepsilon }$. To do${ \mathrm { s o } } ,$it sufices to note that for each index$j = 0 , \ldots , J - 1$, we have that$\hat { \mathbb { T } } _ { \rho _ { j } } ^ { \prime }$is a $\delta ^ { - \varepsilon / 4 } 2 ^ { J }$<sup>−j</sup>-balanced partitioning cover of$\mathbb { T } ^ { \dagger }$, and thus if we choose$\eta < \varepsilon ^ { 2 } / 2$, then for each$\tilde { T } _ { \rho _ { j } } \in \hat { \mathbb { T } } _ { \rho _ { j } } ^ { \prime }$ we can use (10.20) to conclude that

$$
C _ {F - C W} \big ((\mathbb {T} ^ {\dagger}) ^ {\tilde {T} _ {\rho_ {j}}} \big) \leq \frac {C _ {K T - C W} (\mathbb {T} ^ {\dagger})}{\# \mathbb {T} ^ {\dagger} [ \tilde {T} _ {\rho_ {j}} ]} \frac {| \tilde {T} _ {\rho_ {j}} |}{| T |} \lesssim \delta^ {- \eta / \varepsilon} C _ {K T - C W} (\mathbb {T} ^ {\dagger}) \leq \delta^ {- \eta / \varepsilon - \varepsilon / 4} C _ {K T - C W} (\hat {\mathbb {T}} _ {\rho_ {J}} ^ {\prime}) \leq \delta^ {- \varepsilon}.
$$

## 11 Multi-scale analysis and the proof of Proposition 1.7

Our goal in this section is to prove Proposition 1.7 by combining Proposition 9.1 and Theorem 10.2.

Lemma 11.1. Let$\sigma \in ( 0 , 2 / 3 ] ; \omega , \varepsilon > 0$and$N \geq 1$. Suppose that$\mathcal { E } ( \sigma , \omega )$is true. Then there exists $\eta , \alpha , \kappa > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense with$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$ and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Then at least one of the following must hold.

(A)

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega - \alpha} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.
$$

(B) There is$a ~ \delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } o f ( \mathbb { T } , Y ) _ { \delta } ;$a number$J \le 2 ^ { N }$; scales$\delta = \rho _ { J } < \rho _ { J - 1 } < . . . <$ $\rho _ { 0 } = 1$; and sets$\mathbb { T } _ { \rho _ { j } } , \ j = 0 , \dots , J$, so that the following holds

(i)$\rho _ { i + 1 } / \rho _ { i } \geq \delta ^ { ( 1 - \omega / 1 0 0 ) ^ { N } }$for each$i = 0 , \ldots , J - 1$

(ii)$\mathbb { T } ^ { \prime } = \mathbb { T } _ { \rho _ { J } }$, and$\mathbb { T } _ { \rho _ { 0 } }$consists of a single 1 tube.

(iii) For each$i = 1 , \ldots , J - 1$and each$T _ { \rho _ { i - 1 } } \in \mathbb { T } _ { \rho _ { i - 1 } }$, we have that$\mathbb { T } _ { \rho _ { i } } ^ { T _ { \rho _ { i - 1 } } }$factors$\mathbb { T } _ { \rho _ { i + 1 } } ^ { T _ { \rho _ { i - 1 } } }$ from above and below with regard to the Katz-Tao Convex Wolf Axioms and Frostman Slab Wolf Axioms, both with error$\delta ^ { - \varepsilon }$

Proof.

Step 1. We will prove the result by induction on N. When$N = 0$there is almost nothing to prove; since the tubes in$\mathbb { T }$are contained in the unit ball, we can select$\mathrm  \ a \sim 1$refinement$\mathbb { T } ^ { \prime } \subset \mathbb { T }$ that is contained in a single 1 tube. We have$J = 1$, and Conclusion (B) always holds (note that Item (iii) of Conclusion B is vacuously true when$J = 1$

Suppose now that the result has been proved for$N - 1$. Let$\theta \in ( 0 , 2 / 3 ]$and let$\varepsilon , \omega \ > 0$ Let$\varepsilon _ { 1 } , \varepsilon _ { 2 } , \eta , \alpha , c > 0$be small quantities to be determined below. We will choose$\varepsilon _ { 1 }$depending on $\varepsilon , N , \theta , \omega ; \varepsilon _ { 2 }$small compared to$\varepsilon _ { 1 } ;$and$\eta , \alpha , c$small compared to$\varepsilon _ { 2 }$

Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense and satisfy$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. If$\eta$is chosen suficiently small depending on$\omega , \sigma$, and$\varepsilon _ { 2 } .$then we can apply the induction hypothesis with$\varepsilon _ { 2 }$in place of$\varepsilon ;$let$\alpha _ { 1 } = \alpha _ { 1 } ( \omega , \sigma , \varepsilon _ { 2 } , N - 1 )$be the corresponding value of α.

If Conclusion (A) holds when we apply the induction hypothesis, then Conclusion$( \mathrm { A } )$holds and we are done, provided we select$\alpha \leq \alpha _ { 1 }$. Suppose instead that Conclusion (B) holds, i.e. there is a$\delta ^ { \varepsilon _ { 2 } }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ;$scales$\delta = \rho _ { J } < \rho _ { J - 1 } < . . . < \rho _ { 0 } = 1$with$\dot { J } \le 2 ^ { N - 1 }$and $\rho _ { i + 1 } / \rho _ { i } \geq \delta ^ { ( 1 - \omega / 1 0 0 ) ^ { N - 1 } }$; and sets$\mathbb { T } _ { \rho _ { j } }$satisfying Conclusion (B) with$\varepsilon _ { 2 }$in place of$\varepsilon .$

Replacing$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$and each set$\mathbb { T } _ { \rho _ { i } }$with a$( \log 1 / \delta ) ^ { - J } \ge ( \log 1 / \delta ) ^ { - 2 ^ { N } }$refinement, we can construct shadings$Y _ { \rho _ { i } }$on$\mathbb { T } _ { \rho _ { i } }$so that the following holds.

(a)$| Y _ { \rho _ { 0 } } ( T _ { \rho _ { 0 } } ) | \gtrsim ( \log { 1 / \delta } ) ^ { - 2 ^ { N } } \delta ^ { \eta }$, where$T _ { \rho _ { 0 } }$is the unique tube in$\mathbb { T } _ { \rho _ { 0 } }$

(b) For each$T _ { \rho _ { i } } \in \mathbb { T } _ { \rho _ { i } }$, we have that$( \mathbb { T } _ { \rho _ { i + 1 } } ^ { T _ { \rho _ { i } } } , Y _ { \rho _ { i + 1 } } ^ { T _ { \rho _ { i } } } ) _ { \rho _ { i + 1 } / \rho _ { i } } { \mathrm { ~ i s } } \gtrsim ( \log 1 / \delta ) ^ { - 2 ^ { N } } \delta ^ { \eta }$dense, and$( Y _ { \rho _ { J } } , \mathbb { T } _ { \rho _ { J } } ) _ { \delta }$ is$\mathrm { ~ a ~ } \gtrsim ( \log 1 / \delta ) ^ { - 2 ^ { N } }$-refinement of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$

(c) Item (iii) of Conclusion (B) remains true, with the error$\delta ^ { - \varepsilon _ { 2 } }$weakened to$\lesssim ( \log 1 / \delta ) ^ { 2 ^ { N } } \delta ^ { - \varepsilon _ { 2 } }$

(d) For each$i = 1 , \ldots , J - 1$and each$T _ { \rho _ { i - 1 } } \in \mathbb { T } _ { \rho _ { i - 1 } }$, we have that$\mathbb { T } _ { \rho _ { i } } ^ { T _ { \rho _ { i - 1 } } }$is a balanced partitioning cover of$\mathbb { T } _ { \rho _ { i + 1 } } ^ { T _ { \rho _ { i - 1 } } }$

(e) For each$i = 0 , \ldots , J - 1$, the quantity

$$
\Big | \bigcup_ {T \in \mathbb {T} _ {\rho_ {i + 1}} [ T _ {\rho_ {i}} ]} Y _ {\rho_ {i + 1}} (T _ {\rho_ {i + 1}}) \Big |
$$

is approximately the same (up to a multiplicative factor of 2) for each$T _ { \rho _ { i } } \in \mathbb { T } _ { \rho _ { i } }$

(f) We have

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \prod_ {i = 1} ^ {J - 1} \Big (\sup _ {T _ {\rho_ {i} \in \mathbb {T} _ {\rho_ {i}}}} \frac {1}{| T _ {\rho_ {i}} |} \Big | \bigcup_ {T _ {\rho_ {i + 1}} \in \mathbb {T} _ {\rho_ {i + 1}} [ T _ {\rho_ {i}} ]} Y _ {\rho_ {i + 1}} (T _ {\rho_ {i + 1}}) \Big | \Big).\tag{11.1}
$$

Item (f) is obtained by selecting each shading$Y _ { \rho _ { i + 1 } }$so that the union$\begin{array} { r } { \bigcup _ { T _ { \rho _ { i + 1 } } \in \mathbb { T } _ { \rho _ { i + 1 } } \left[ T _ { \rho _ { i } } \right] } Y _ { \rho _ { i + 1 } } ( T _ { \rho _ { i + 1 } } ) \subset } \end{array}$ $Y _ { \rho _ { i } } ( T _ { \rho _ { i } } )$has approximately the same density (up to a multiplicative factor of 2) on balls of radius $\rho _ { i }$contained in$Y _ { \rho _ { i } } ( T _ { \rho _ { i } } )$. By the previous item, the RHS of (11.1) is reduced by at most a factor of$2 ^ { J }$if the supremum in (11.1) is replaced by an infimum. Items$\mathrm { ( a ) \mathrm { ~ - ~ } \mathrm { ( e ) } }$are obtained by dyadic pigeonholing; we omit the details.

If$\varepsilon _ { 2 }$is chosen suficiently small depending on$\varepsilon _ { 1 }$, then for each index i and each$T _ { \rho _ { i } } \in \mathbb { T } _ { \rho _ { i } }$we have

$$
\frac {1}{| T _ {\rho_ {i}} |} \Big | \bigcup_ {T _ {\rho_ {i + 1}} \in \mathbb {T} _ {\rho_ {i + 1} [ T _ {\rho_ {i}} ]}} Y _ {\rho_ {i + 1}} (T _ {\rho_ {i + 1}}) \Big | \gtrsim \delta^ {\varepsilon_ {1}} \big (\frac {\rho_ {i + 1}}{\rho_ {i}} \big) ^ {\omega} \big (\frac {\# \mathbb {T} _ {\rho_ {i + 1}}}{\# \mathbb {T} _ {\rho_ {i}}} \big) | T _ {\rho_ {i + 1}} | \Big ((\frac {\# \mathbb {T} _ {\rho_ {i + 1}}}{\# \mathbb {T} _ {\rho_ {i}}}) \big (\frac {| T _ {\rho_ {i + 1}}}{| T _ {\rho_ {i}} |} \big) ^ {1 / 2} \Big) ^ {- \sigma}\tag{11.2}
$$

Indeed, (11.2) follows from the estimate$\mathcal { E } ( \sigma , \omega ) ;$; this estimate can be applied, for example, when $\frac { \rho _ { i + 1 } } { \rho _ { z } } < \delta ^ { \varepsilon _ { 1 } }$and$\varepsilon _ { 2 }$is selected suficiently small depending on$\omega , \sigma _ { \mathrm { { : } } }$, and$\varepsilon _ { 1 }$. If$\frac { \rho _ { i + 1 } } { \rho _ { i } } \geq \delta ^ { \varepsilon _ { 1 } }$, then (11.2) follows from the elementary fact that the volume of the LHS of (11.2) is bounded below by the volume of$Y _ { \rho _ { i + 1 } } ( T _ { \rho _ { i + 1 } } )$for every$T _ { \rho _ { i + 1 } } \in \mathbb { T } _ { \rho _ { i + 1 } } [ T _ { \rho _ { i } } ]$

## Step 2.

We say an index i is of Type C if$\rho _ { i + 1 } / \rho _ { i } \geq 2 ^ { - N } \delta ^ { ( 1 - \omega / 1 0 0 ) ^ { N } }$; in this case no further splitting is required. If instead$\rho _ { i + 1 } / \rho _ { i } < 2 ^ { - N } \delta ^ { ( 1 - \omega / 1 0 0 ) ^ { N } }$, then apply Proposition 9.1 (refined induction on scales) with$\omega$and σ as above, and$\zeta = \varepsilon$to each arrangement$( \mathbb { T } _ { \rho _ { i + 1 } } ^ { T _ { \rho _ { i } } } , Y _ { \rho _ { i + 1 } } ^ { T _ { \rho _ { i } } } ) _ { \rho _ { i + 1 } / \rho _ { i } } \colon$we can do this provided$\varepsilon _ { 2 }$is chosen suficiently small depending on$\omega , \sigma , N ,$, and ε. If Conclusion (A) holds for at least one$T _ { \rho _ { i } } \in \mathbb { T } _ { \rho _ { i } }$, then we say the index i is of Type A. Otherwise we say that the index i is of Type B.

Suppose there exists at least one index of Type$\operatorname { A } ;$call this index$i _ { 0 }$. Let$\alpha _ { 2 } = \alpha _ { 2 } ( \omega , \sigma , \varepsilon )$be the output of Proposition 9.1. Then applying (11.2) to each index$i \neq i _ { 0 } ;$using Conclusion$\mathrm { ( A ) }$ of Proposition 9.1 to estimate the contribution from index$i _ { 0 } ;$and using (11.1) to combine these estimates, we have

$$
\begin{array}{l}\Big|\bigcup_{T\in \mathbb{T}}Y(T)\Big|\\ \gtrsim \prod_{\substack{i = 1,\ldots ,J - 1\\ i\neq i_{0}}}\Big(\delta^{\varepsilon_{1}}\big(\frac{\rho_{i + 1}}{\rho_{i}}\big)^{\omega}\big(\frac{\#\mathbb{T}_{\rho_{i + 1}}}{\#\mathbb{T}_{\rho_{i}}} \big)|T_{\rho_{i + 1}}\Big(\big(\frac{\#\mathbb{T}_{\rho_{i + 1}}}{\#\mathbb{T}_{\rho_{i}}} \big)\big(\frac{|T_{\rho_{i + 1}}}{|T_{\rho_{i}}|} \big)^{1 / 2}\Big)^{-\sigma}\Big).\\ \qquad \cdot \left(\delta^{\varepsilon_{1}}\big(\frac{\rho_{i_{0} + 1}}{\rho_{i_{0}}} \big)^{\omega - \alpha_{2}}\big(\frac{\#\mathbb{T}_{\rho_{i_{0} + 1}}}{\#\mathbb{T}_{\rho_{i_{0}}}} \big)|T_{\rho_{i_{0} + 1}}\Big(\big(\frac{\#\mathbb{T}_{\rho_{i_{0} + 1}}}{\#\mathbb{T}_{\rho_{i_{0}}}} \big)\big(\frac{|T_{\rho_{i_{0} + 1}}}{|T_{\rho_{i_{0}}}|} \big)^{1 / 2}\Big)^{-\sigma}\right)\\ \geq \delta^{\varepsilon_{1}J}\big(\frac{\rho_{i_{0} + 1}}{\rho_{i_{0}}} \big)^{-\alpha_{2}}(\# \mathbb{T})|T| \big((\# \mathbb{T})|T|^{1 / 2}\big)^{-\sigma}\\ \gtrsim \delta^{\varepsilon_{1}2^{N} - \alpha_{2}(1 - \omega /100)^{N}}(\# \mathbb{T})|T|\big((\# \mathbb{T})|T|^{1 / 2}\big)^{-\sigma} \\ \end{array}\tag{11.3}
$$

Thus Conclusion (A) of Lemma 11.1 holds, provided we select$\alpha \leq \textstyle { \frac { 1 } { 2 } } \alpha _ { 2 } ( 1 - \omega / 1 0 0 ) ^ { N }$and$\varepsilon _ { 1 } ~ <$ $2 ^ { - N - 1 } \alpha _ { 2 } ( 1 - \omega / 1 0 0 ) ^ { N }$

Step 3. Suppose instead that every index is of Type B or Type C. We will show that Conclusion (B) of Lemma 11.1 holds. For each index i of Type B, starting with the lowest, we will perform the following procedure. After dyadic pigeonholing, there is a number$s \in \left[ \left( \frac { \rho _ { i + 1 } } { \rho _ { i } } \right) ^ { 1 - \frac { \omega } { 1 0 0 } } , \left( \frac { \rho _ { i + 1 } } { \rho _ { i } } \right) ^ { \frac { \omega } { 1 0 0 } } \right]$ and a set$\mathbb { T } _ { \rho _ { i } } ^ { \prime } \subset \mathbb { T } _ { \rho _ { i } }$with$\# \mathbb { T } _ { \rho _ { i } } ^ { \prime } \gtrapprox \delta \# \mathbb { T } _ { \rho _ { i } }$such that the output$^ { 6 6 } \rho ^ { 5 }$from Proposition 9.1 is between s and 2s for each$T _ { \rho _ { i } } \in \mathbb { T } _ { \rho _ { i } } ^ { \prime }$. Define$\rho _ { i + 1 / 2 } = s \rho _ { i }$. Then

$$
\frac {\rho_ {i + 1 / 2}}{\rho_ {i}} \geq s \geq \big (\frac {\rho_ {i + 1}}{\rho_ {i}} \big) ^ {1 - \frac {\omega}{1 0 0}} \geq (2 ^ {- N + 1} \delta^ {(1 - \omega / 1 0 0) ^ {N - 1}}) ^ {1 - \frac {\omega}{1 0 0}} \geq 2 ^ {- N} \delta^ {(1 - \omega / 1 0 0) ^ {N}}.\tag{11.4}
$$

Similarly, we have

$$
\frac {\rho_ {i + 1}}{\rho_ {i + 1 / 2}} = \frac {\rho_ {i + 1}}{\rho_ {i}} \frac {\rho_ {i}}{\rho_ {i + 1 / 2}} \geq \frac {\rho_ {i + 1}}{\rho_ {i}} \frac {1}{2 s} \geq \frac {1}{2} \big (\frac {\rho_ {i + 1}}{\rho_ {i}} \big) ^ {1 - \frac {\omega}{1 0 0}} \geq 2 ^ {- N} \delta^ {(1 - \omega / 1 0 0) ^ {N}}.\tag{11.5}
$$

This verifies Item (i) from Conclusion (B) of Lemma 11.1.

Let$\mathbb { T } _ { \rho _ { i + 1 / 2 } }$be the union of the corresponding sets from Proposition 9.1, and let

$$
\mathbb {T} _ {\rho_ {i + 1}} ^ {\prime} = \bigcup_ {T _ {\rho_ {i + 1 / 2}} \in \mathbb {T} _ {\rho_ {i + 1 / 2}}} \mathbb {T} _ {\rho_ {i + 1}} [ T _ {\rho_ {i + 1 / 2}} ].
$$

Then for each$T _ { \rho _ { i } } \in \mathbb { T } _ { \rho _ { i } } ^ { \prime } ,$we have that$\mathbb { T } _ { \rho _ { i + 1 / 2 } } ^ { T _ { \rho _ { i } } }$factors$( \mathbb { T } _ { \rho _ { i + 1 } } ^ { \prime } ) ^ { T _ { \rho _ { i } } }$above and below with respect to the Katz-Tao Convex Wolf Axioms and Frostman Slab Wolf Axioms, both with error$\delta ^ { - \varepsilon }$. This verifies Item (iii) from Conclusion (B) of Lemma 11.1.

To conclude the proof, we re-index our sets$\mathbb { T } _ { \rho _ { i } } ^ { \prime }$and$\mathbb { T } _ { \rho _ { i + 1 / 2 } }$using consecutive integers$1 , 2 , 3 . . . ,$ and let$\mathbb { T } ^ { \prime } = \mathbb { T } _ { \rho _ { J ^ { \prime } } }$, where J<sup>′</sup> is the final index after re-indexing. Note that$J ^ { \prime } \le 2 J - 1 \le 2 ^ { N }$. After re-indexing, we still have$\rho _ { 0 } = 1$and$\rho _ { J ^ { \prime } } = \delta$. This concludes the induction step.□

Lemma 11.2. Let$\sigma \in ( 0 , 2 / 3 ]$and$\omega , \varepsilon > 0$. Suppose that$\mathcal { E } ( \sigma , \omega )$is true. Then there exists $\eta , \alpha , \kappa > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense with$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$ and$C _ { F - S W } ( \mathbb { T } ) \leq \delta ^ { - \eta }$. Then at least one of the following must hold.

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {\omega - \alpha} (\# \mathbb {T}) | T | \big ((\# \mathbb {T}) | T | ^ {1 / 2} \big) ^ {- \sigma}.\tag{A}
$$

(B) There is a$\delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ~ o f \left( \mathbb { T } , Y \right) _ { \delta }$that satisfies the Katz-Tao Convex Wolf Axioms at every scale with error$\delta ^ { - \varepsilon }$(recall Definition 10.1).

Proof. Let$\varepsilon _ { 1 } > 0$be a small quantity to be chosen below. Select N suficiently large so that $( 1 - \omega / 1 0 0 ) ^ { N } < \varepsilon .$. Apply Lemma 11.1 to$( \mathbb { T } , Y ) _ { \delta }$with this choice of$N$, with$\varepsilon _ { 1 }$in place of$\varepsilon ,$, and with$\omega , \sigma$as above. If Conclusion (A) of Lemma 11.1 holds, then Conclusion (A) of Lemma 11.2 holds and we are done.

Suppose instead that Conclusion (B) of Lemma 11.1 holds. After a harmless refinement we can suppose that each set$\mathbb { T } _ { \rho _ { i } }$is a balanced partitioning cover of$\mathbb { T } _ { \rho _ { i + 1 } }$, and hence$\mathbb { T } _ { \rho _ { i } }$is a$2 ^ { J } \leq \delta ^ { - \varepsilon }$ balanced partitioning cover of$\mathbb { T } ^ { \prime }$

We claim that if$\varepsilon _ { 1 }$is chosen suficiently small (depending on N and$\varepsilon )$, then the output$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$ of Lemma 11.1 satisfies the Katz-Tao Convex Wolf Axioms at every scale with error$\delta ^ { - \varepsilon }$. We verify this as follows. Since$( 1 - \omega / 1 0 0 ) ^ { N } < \varepsilon ,$for each$\rho \in [ \delta , 1 ]$the interval$[ \rho , \delta ^ { - \varepsilon } \rho ]$contains at least one$\rho _ { i }$. We have already noted that$\mathbb { T } _ { \rho _ { i } }$satisfies Item (i) from Definition 10.1. It remains to verify Item (ii). Applying Lemma 4.12, we have that for each index$i ,$

$$
C _ {K T - C W} (\mathbb {T} _ {i}) \lesssim \prod_ {j = i + 1} ^ {J} \delta^ {- 2 \varepsilon_ {1}} \lesssim \delta^ {- 2 ^ {N + 1} \varepsilon_ {1}}.
$$

We will select$\varepsilon _ { 1 }$suficiently small so that$C _ { K T - C W } ( \mathbb { T } _ { i } ) \le \delta ^ { - \varepsilon }$for all suficiently small$\delta > 0$. If$\delta > 0$ is not suficiently small, then Conclusion (A) always holds, provided we select$\kappa > 0$suficiently small.□

Proof of Proposition 1.7. Fix$\omega , \sigma > 0$and suppose that$\mathcal { E } ( \sigma , \omega )$is true. Let$\eta _ { 1 }$be the output of Theorem 10.2 with$\omega / 2$in place of ε. Let$\alpha _ { 2 } , \eta _ { 2 } , c _ { 2 }$be the output of Lemma 11.2 with$\eta _ { 1 }$in place of ε. Then for every pair$( \mathbb { T } , Y ) _ { \delta }$that is$\delta ^ { \eta _ { 2 } }$dense and satisfies$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta _ { 2 } } , C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta _ { 2 } }$ we have

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \delta^ {\omega - \min (\alpha_ {2}, \omega / 2)} (\# \mathbb {T}) | T | \Big ((\# \mathbb {T}) | T | \Big) ^ {- \sigma}.\tag{11.6}
$$

In particular, we have that$\mathcal { D } ( \sigma , \omega - g ( \sigma , \omega ) )$is true, where$g ( \sigma , \omega ) = \operatorname* { m i n } ( \alpha _ { 2 } , \omega / 2 )$

## 12 Tube Doubling

In this section we will prove Theorem 1.12. We will prove the following slightly stronger statement.

Theorem 1.12<sup>′</sup>. For all$\varepsilon > 0$, there exists$\eta > 0$so that the following is true for all$\delta > 0$ suficiently small. Let T be a set of δ tubes in$\mathbb { R } ^ { 3 }$. For each$T \in \mathbb { T }$, let$Y ( T ) \subset T$with$| Y ( T ) | \geq$ $\delta ^ { \eta } \vert T \vert$. Let$R \geq 1$and for each$T \in \mathbb { T }$, let$T _ { R }$denote the R-fold dilate of T. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} T _ {R} \Big | \leq \delta^ {- \varepsilon} R ^ {3} \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big |.\tag{12.1}
$$

Theorem 1.12 is the special case where$Y ( T ) = T$and$R = 2$

Proof. Step 1. First, we may suppose that the tubes in$\mathbb { T }$are contained in$B ( 0 , 1 )$(indeed, we can cover$\mathbb { R } ^ { 3 }$by a set of boundedly overlapping unit balls, so that each$T \in \mathbb { T }$is contained in at least one ball). Second, we may suppose that the tubes in T are essentially distinct, and in particular $\# \mathbb { T } \lesssim \delta ^ { - 4 }$(indeed, we can replace T by a maximal, essentially distinct sub-collection, and this afects the RHS of Inequality (12.1) by a constant factor).

Fix$\varepsilon > 0$. For each$i = 1 , 2 , \dots ,$we will define sets$\mathbb { T } _ { i } , \mathbb { T } _ { i } ^ { \prime } .$and$\mathcal { W } _ { i }$as follows. We begin by defining$\mathbb { T } _ { 0 } = \mathbb { T }$. Define$\mathbb { T } _ { i } ^ { \prime }$and$\mathcal { W } _ { i }$to be the output of Proposition 4.6 applied to$\mathbb { T } _ { i - 1 }$. Define $\mathbb { T } _ { i } = \mathbb { T } _ { i - 1 } \backslash \mathbb { T } _ { i } ^ { \prime }$. We continue this process until$\mathbb { T } _ { N }$is empty, at which point we halt. Observe that $\begin{array} { r } { \mathbb { T } = \bigcup _ { i = 1 } ^ { N } \mathbb { T } _ { i } ^ { \prime } } \end{array}$. For each index i we have

$$
\# \mathbb {T} _ {i} ^ {\prime} \geq 1 0 0 ^ {- 3} e ^ {- 1 0 0 \sqrt {\log (\delta^ {- 5})}} (\# \mathbb {T} _ {i - 1}),
$$

As a consequence, if$j - i \geq 2 \cdot 1 0 0 ^ { 3 } e ^ { 1 0 0 \sqrt { \log ( \delta ^ { - 5 } ) } }$, then$\# \mathbb { T } _ { j } \ \leq \ \frac { 1 } { 2 } ( \# \mathbb { T } _ { i } )$. Since$\# \mathbb { T } _ { 0 } \lesssim \delta ^ { - 4 }$, we conclude that the process described above must halt after$\lesssim ( \log 1 / \delta ) ( 2 \cdot 1 0 0 ^ { 3 } e ^ { 1 0 0 { \sqrt { \log ( \delta ^ { - 5 } ) } } } ) \gtrapprox \delta \mid$ steps, i.e.$N \lessapprox _ { \delta } 1$

Step 2. Fix an index$j .$. To simplify notation, we write$\mathbb { T } ^ { \prime } = \mathbb { T } _ { j } ^ { \prime }$and$\mathcal { W } ^ { \prime } = \mathcal { W } _ { j }$

We have that$\mathcal { W } ^ { \prime }$factors$\mathbb { T } ^ { \prime }$from above with respect to the Katz-Tao convex Wolf Axioms and from below with respect to the Frostman Convex Wolf Axioms, both with error$K \leq 1 0 0 ^ { 3 } e ^ { 1 0 0 { \sqrt { \log ( \delta ^ { - 5 } ) } } }$ Recall that the prisms in$\mathcal { W } ^ { \prime }$all have the same dimensions — denote these dimensions by$a \times b \times 1$

Let$\varepsilon _ { 1 } > 0$be a small quantity to be chosen below. Our next task is to estimate the volume of the tubes inside each prism from$\mathcal { W } ^ { \prime }$, i.e. we wish to obtain a bound of the form

$$
\Big | \bigcup_ {T \in \mathbb {T} ^ {\prime} [ W ]} Y (T) \Big | \geq \kappa_ {0} \delta^ {\varepsilon_ {1}} | W |,\tag{12.2}
$$

for some$\kappa _ { 0 } = \kappa _ { 0 } ( \varepsilon _ { 1 } ) > 0$. To do this, we will estimate the volume of the set$\mathsf { U } _ { \mathbb { T } ^ { \prime } [ W ] } Y ^ { W } ( T ) ^ { W }$; the latter is a union of prisms of dimensions$\delta / b \times \delta / a \times 1$. By Theorem 1.9 we have that Assertion $\mathcal { E } ( \varepsilon _ { 1 } / 1 0 , \varepsilon _ { 1 } / 1 0 )$is true, and thus by Proposition 5.14, we have that Assertion$\mathcal { F } ( \varepsilon _ { 1 } / 1 0 , \varepsilon _ { 1 } / 1 0 )$(recall Definition 5.4) is true. The latter assertion is helpful, since it allows us to bound the volume of unions of prisms with three distinct dimensions (i.e. prisms that are not tubes).

For each$W \in \mathcal { W } ^ { \prime }$, we will apply the estimate$\mathcal { F } ( \varepsilon _ { 1 } / 1 0 , \varepsilon _ { 1 } / 1 0 )$to the pair$( ( \mathbb { T } ^ { \prime } ) ^ { W } , Y ^ { W } ) _ { \delta / b \times \delta / a \times 1 } .$ Recall that the estimate$\mathcal { F } ( \varepsilon _ { 1 } / 1 0 , \varepsilon _ { 1 } / 1 0 )$contains an additional term$^ { 6 6 } D .$However, as discussed in Remark 5.6, Situation 3, we have$D \sim 1$in this setting. If$\eta > 0$is selected suficiently smal depending on$\varepsilon _ { 1 }$, we conclude that for each$W \in \mathcal { W } ^ { \prime }$, we have

$$
\begin{array}{l} \Big | \bigcup_ {T \in \mathbb {T} ^ {\prime} [ W ]} Y ^ {W} (T) ^ {W} \Big | \geq \kappa_ {0} \delta^ {\varepsilon_ {1} / 1 0} m ^ {- 1} (\# \mathbb {T} ^ {\prime} [ W ]) | T ^ {W} | \Big (m ^ {- 3 / 2} \ell (\# \mathbb {T} ^ {\prime} [ W ]) | T ^ {W} | ^ {1 / 2} \Big) ^ {- \varepsilon_ {1} / 1 0} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{12.3}
$$

where$\begin{array} { r } { m = C _ { K T - C W } \big ( \big ( \mathbb { T } ^ { \prime } \big ) ^ { W } \big ) \gtrapprox \delta ( \# \mathbb { T } ^ { \prime } [ W ] ) \frac { | T | } { | W | } = ( \# \mathbb { T } ^ { \prime } [ W ] ) | T ^ { W } | } \end{array}$, and$\ell = C _ { F - S W } ( ( \mathbb { T } ^ { \prime } ) ^ { W } )$. For the second inequality, the term$\left( m ^ { - 3 / 2 } \ell ( \# \mathbb { T } ^ { \prime } [ W ] ) | T ^ { W } | ^ { 1 / 2 } \right)$can be trivially bounded by$\delta ^ { - 4 }$. (12.2) now follows from (12.3) by rescaling and adjusting the constant$\kappa _ { 0 }$if necessary.

For each$W \in \mathcal { W } ^ { \prime }$, define$Y ( W ) = \bigcup _ { T \in \mathbb { T } ^ { \prime } [ W ] } T \mathrm { \mathrm { : } }$we have$Y ( W ) \subset W$and$| Y ( W ) | \ge \kappa _ { 0 } \delta ^ { \varepsilon _ { 1 } }$for each$W \in \mathcal { W } ^ { \prime } ;$; we will suppose that$\delta > 0$is chosen suficiently small so that this quantity is$\geq \delta ^ { 2 \varepsilon _ { 1 } }$

If$\varepsilon _ { 1 } ~ > ~ 0$is chosen suficiently small depending on$\varepsilon ,$then we can apply$\mathcal { F } ( \varepsilon / 1 0 , \varepsilon / 1 0 )$to $( \mathcal { W } ^ { \prime } , Y ) _ { a \times b \times 1 }$(again, the term D has size at most$C _ { K T - C W } ( \mathcal { W } ^ { \prime } ) \lesssim _ { \delta } 1$, as discussed in Remark 5.6, Situation 2) to conclude that

$$
\Big | \bigcup_ {W \in \mathcal {W} ^ {\prime}} Y (W) \Big | \geq \kappa_ {1} \delta^ {\varepsilon / 2} (\# \mathcal {W} ^ {\prime}) | W |.\tag{12.4}
$$

Combining (12.2) and (12.4) and returning to our original notation, we have

$$
\Big | \bigcup_ {T \in \mathbb {T} _ {j} ^ {\prime}} Y (T) \Big | \geq \kappa_ {1} \delta^ {\varepsilon / 2} \sum_ {W \in \mathcal {W} _ {j}} | W |.\tag{12.5}
$$

Step 3. We will now combine the estimates (12.5) for diferent values of$j$. Let$\textstyle \mathcal { W } = \bigcup _ { j = 1 } ^ { N } \mathcal { W } _ { j }$ Then W covers T, and

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq N ^ {- 1} \max _ {1 \leq j \leq N} \Big | \bigcup_ {T \in \mathbb {T} _ {j} ^ {\prime}} T \Big | \gtrsim_ {\delta} \kappa_ {1} \delta^ {\varepsilon / 2} \sum_ {W \in \mathcal {W}} | W |.\tag{12.6}
$$

Finally, since W covers$T ,$we have that the set of R-fold dilates$\{ R W \colon W \in \mathcal { W } \}$covers$\{ T _ { R } \colon T \in$ $\mathbb { T } \}$, and thus

$$
\left| \bigcup_ {T \in \mathbb {T}} T _ {R} \right| \leq \left| \bigcup_ {W \in \mathcal {W}} R W \right| \leq \sum_ {W \in \mathcal {W}} | R W | = R ^ {3} \sum_ {W \in \mathcal {W}} | W |.\tag{12.7}
$$

Inequality (12.1) now follows by comparing (12.6) and (12.7).

□

## A A grains decomposition for tubes in$\mathbb { R } ^ { 3 }$

Our goal in this section is to prove Proposition 7.15. For the reader’s convenience, we reproduce it here. In what follows, recall that broadness is defined in Definition 7.7. This definition assumes a small parameter$\beta > 0$, which was defined in Section 7.1. In Section$7 . 1$, an explicit value of$\beta$ was chosen, which depends on ω and$\zeta .$. In the results below, however, we will allow$\beta$to be any positive number (though in$\mathbb { R } ^ { n }$, we will always have$\beta \in ( 0 , n - 1 ] )$, and subsequent quantities (such as$\eta$and$K _ { 1 } )$may depend on$\beta .$In particular, the results proved in this section are applicable in Section 7.

Proposition 7.15. Let$\varepsilon > 0$. Then there exists$\eta , \kappa > 0$so that the following holds for all$\delta > 0$ Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense and be broad with error$\delta ^ { - \eta }$. Suppose that the tubes in$\mathbb { T }$are contained in a common 1 tube$T _ { 1 }$

Then there is a$\delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } )$that is$\delta ^ { \varepsilon }$dense and is broad with error$\le \kappa ^ { - 1 } \delta ^ { - \varepsilon }$, and a number$\mu \geq 1$so that$\mu \sum \# \mathbb { T } _ { Y ^ { \prime } } ^ { \prime } ( x )$for each$x \in \bigcup _ { \mathbb { T } ^ { \prime } } Y ^ { \prime } ( T )$. In addition, there is a number $c \ge \kappa \mu \delta ^ { \varepsilon } ( \delta \# \mathbb { T } ) ^ { - 1 }$and a pair$( \mathcal { G } , Y ) _ { \delta \times c \times c } ,$so that$( \mathcal { G } , Y ) _ { \delta \times c \times c }$is a robustly$\delta ^ { \varepsilon }$-dense two-scale grains decomposition of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$wrt$\{ T _ { 1 } \}$(the latter is a set consisting of a single 1 tube).

To prove Proposition 7.15, we shall repeatedly apply the Guth-Katz polynomial partitioning theorem [13] to decompose a (large portion of)$\textstyle \bigcup _ { \mathbb { T } } Y ( T )$into a union of thin neighbourhoods of semi-algebraic sets. This idea was first used by Guth [11, 12] in the context of the Fourier restriction problem, and later by Guth and the second author [14] in the context of the Kakeya problem.

Before stating this result precisely, we will need several definitions. First, recall that a semi-algebraic set is a set$S \subset \mathbb { R } ^ { n }$that is defined by a Boolean combination of polynomial equalities and inequalities.

Definition A.1. Let$\rho > 0$. A semi-algebraic grain of thickness$\rho$is a set of the form

$$
G = N _ {\rho} (S),
$$

where$S \subset \mathbb { R } ^ { 3 }$is a semi-algebraic set with dim$( S ) \le 2$. If there exists a non-zero polynomial $Q \colon \mathbb { R } ^ { 3 }  \mathbb { R }$with$S \subset Z ( Q )$, then we say that G is defined by a polynomial of degree at most $\deg ( Q )$

Next, we recall the following result of Wongkew [30], which allows us to bound the volume of a semi-algebraic grain.

Theorem A.2. Let$Z = Z ( Q ) \subset \mathbb { R } ^ { n }$be an algebraic variety of dimension d. Let$B \subset \mathbb { R } ^ { n }$be a ball of radius r. Then there exists a constant K depending only on n so that for all$0 < \rho \le r _ { \cdot }$

$$
| N _ {\rho} (Z \cap B) | \leq K (\deg Q) ^ {n} \rho^ {n - d} r ^ {d}.
$$

Corollary A.3. Let$G \subset \mathbb { R } ^ { 3 }$be a semi-algebraic grain of thickness$\rho$that is defined by a polynomial of degree at most D. Then

$$
| G | \lesssim D ^ {3} \rho \mathrm{diam} (G) ^ {2}.
$$

Next, we will need the following grains decomposition result, which is similar to Proposition 3.2 from [14].

Proposition A.4. Let$\varepsilon > 0$. Then there exists$K _ { \varepsilon } \ > \ 0$so that the following holds. Let$E \subset$ $B ( 0 , 1 ) \subset \mathbb { R } ^ { 3 }$be open. Then there exists

• A set$\mathcal { G }$of semi-algebraic grains of thickness 100δ, each of which has diameter$\leq K _ { \varepsilon } ( \# \mathcal { G } ) ^ { - 1 / 3 }$ and is defined by a polynomial of degree at most$K _ { \varepsilon }$

• For each$G \in { \mathcal { G } }$, a set$E _ { G } \subset E \cap G$. The sets$\{ E _ { G } \colon G \in { \mathcal { G } } \}$are disjoint.

Furthermore, we have

$$
\sum_ {G \in \mathcal {G}} | E _ {G} | \geq K _ {\varepsilon} ^ {- 1} \delta^ {\varepsilon} | E |,
$$

and for each$G \in { \mathcal { G } }$we have

$$
K _ {\varepsilon} ^ {- 1} \delta^ {\varepsilon} \frac {| E |}{\# \mathcal {G}} \leq | E _ {G} | \leq K _ {\varepsilon} \delta^ {- \varepsilon} \frac {| E |}{\# \mathcal {G}}.
$$

Finally,$f o r$every$\delta$tube$T ,$we have

$$
\# \{G \in \mathcal {G} \colon T \cap E _ {G} \neq \emptyset \} \leq K _ {\varepsilon} \delta^ {- \varepsilon} (\# \mathcal {G}) ^ {1 / 3}.\tag{A.1}
$$

The above result is essentially Proposition 3.2 from$\lceil 1 4 \rceil$, except that the result in$[ 1 4 ]$does not require that the grains in$\mathcal { G }$have diameter at most$\dot { K _ { \varepsilon } ( \# \mathcal { G } ) } ^ { - 1 / 3 }$. Adding this latter property is straightforward — we simply add additional partitioning planes in the$e _ { 1 } , e _ { 2 }$, and$e _ { 3 }$directions at each partitioning step.

Using Proposition A.4, we have the following structure theorem about arrangements of tubes.

Lemma A.5. Let$\varepsilon , \beta > 0$. Then there exists$K , \eta > 0$so that the following holds. Let$( \mathbb { T } , Y ) _ { \delta }$ be$\delta ^ { \eta }$dense and broad with error$\delta ^ { - \eta }$(and exponent$\beta )$. Suppose there is a number$\mu$so that $\# \mathbb { T } _ { Y } ( x ) \in [ \mu , 2 \mu )$for all$x \in \bigcup _ { T \in \mathbb { T } } Y ( T )$. Then there exists the following:

$A ~ \delta ^ { \varepsilon }$refinement$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta } ~ o f \left( \mathbb { T } , Y \right) _ { \delta }$

• A partition$E = E _ { 1 } \sqcup . . . E _ { N } o f \bigcup _ { \mathbb { T } } Y ^ { \prime } ( T )$

These objects have the following properties:

(a) (i)

$$
1 \leq N \leq K \delta^ {- \varepsilon} \left(\delta \mu^ {- 1} \# \mathbb {T}\right) ^ {3}.\tag{A.2}
$$

(ii)$r \geq K ^ { - 1 } \delta ^ { \varepsilon } N ^ { - 1 / 3 }$

(b) Each set$E _ { i }$has diameter at most$2 r _ { \colon }$, and volume

$$
K ^ {- 1} N ^ {- 1} \delta^ {\varepsilon} \left| \bigcup_ {T \in \mathbb {T}} Y (T) \right| \leq | E _ {i} | \leq K \delta \left(\operatorname{diam} \left(E _ {i}\right)\right) ^ {2}.\tag{A.3}
$$

(c)$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with error$K \delta ^ { - \varepsilon }$(and exponent$\beta )$, and$\# \mathbb { T } _ { Y ^ { \prime } } ^ { \prime } ( x ) \geq K ^ { - 1 } \delta ^ { \varepsilon } \mu$for each$x \in$ $\cup _ { T \in \mathbb { T } ^ { \prime } } Y ^ { \prime } ( T )$

(d) For each$T \in \mathbb { T } ^ { \prime }$, there exists a set$\{ T ^ { ( j ) } \}$of pairwise 100r-separated tube segments$T ^ { ( j ) } \subset T$2 each of length r. This set has the following properties:

(i) Each segment$T ^ { ( j ) }$intersects$Y ^ { \prime } ( T )$, and$Y ^ { \prime } ( T ) \subset \bigcup T ^ { ( j ) }$

(ii)$I f T ^ { ( j ) }$is a tube-segment, then$T ^ { ( j ) } \cap Y ^ { \prime } ( T )$intersects exactly one set$E _ { i }$

Proof.

Step 1. Let$\varepsilon _ { 1 }$be a small quantity to be chosen below. Let$\begin{array} { r } { \mathbb { T } _ { 1 } = \{ T \in \mathbb { T } \colon | Y ( T ) | \geq \frac { 1 } { 2 } \delta ^ { \eta } | T | \} } \end{array}$ and let$Y _ { 1 }$be the restriction of$Y$to$\mathbb { T } _ { 1 }$. Then$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$is a$( 1 / 2 )$-refinement of$( \mathbb { T } , Y ) _ { \delta } .$Apply Proposition A.4 to$\begin{array} { r } { E = \bigcup _ { T \in \mathbb { T } _ { 1 } } Y _ { 1 } ( T ) } \end{array}$with$\varepsilon _ { 1 }$in place of$\varepsilon ,$and let$\mathcal { G }$and$\{ E _ { G } \colon G \in { \mathcal { G } } \}$be the output of that Proposition.

For each$T \in \mathbb { T } _ { 1 }$, there are at most$K _ { \varepsilon _ { 1 } } \delta ^ { - \varepsilon _ { 1 } } ( \# \mathcal { G } ) ^ { 1 / 3 }$grains$G \in { \mathcal { G } }$for which$T \cap E _ { G } \neq \emptyset$. Define the set of “significant” grains

$$
\mathcal {G} _ {T, \mathrm{sig}} = \left\{G \in \mathcal {G} \colon | T \cap E _ {G} | \geq (\frac {1}{2} | Y _ {1} (T) |) \bigl (K _ {\varepsilon_ {1}} \delta^ {- \varepsilon_ {1}} (\# \mathcal {G}) ^ {1 / 3} \bigr) ^ {- 1} \right\}.
$$

Then

$$
\left| Y _ {1} (T) \cap \bigsqcup_ {G \in \mathcal {G} _ {T, \mathrm{sig}}} E _ {G} \right| \geq \frac {1}{2} | Y _ {1} (T) |.
$$

Each set$Y _ { 1 } ( T ) \cap E _ { G }$is contained in a sub-tube of length diam$( T \cap E _ { G } )$, and we have

$$
\delta^ {\eta + \varepsilon_ {1}} K _ {\varepsilon_ {1}} ^ {- 1} (\# \mathcal {G}) ^ {- 1 / 3} \lesssim \operatorname{diam} (T \cap E _ {G}) \leq K _ {\varepsilon_ {1}} (\# \mathcal {G}) ^ {- 1 / 3}.
$$

The first inequality follows from the volume bound$| T \cap E _ { G } | \gtrsim \delta ^ { \eta + \varepsilon _ { 1 } } | T | K _ { \varepsilon _ { 1 } } ^ { - 1 } ( \# \mathcal { G } ) ^ { - 1 / 3 }$, while the second follows from the diameter bound on$G$coming from Proposition$\mathrm { A . 4 }$

Define

$$
r = \kappa \delta^ {\eta + \varepsilon_ {1}} K _ {\varepsilon_ {1}} ^ {- 1} (\# \mathcal {G}) ^ {- 1 / 3},\tag{A.4}
$$

where$\kappa \sim 1$is chosen so that each set$T \cap E _ { G }$has diameter at least$^ { r } \cdot$Then for each grain $G \in { \mathcal { G } } _ { T , \mathrm { s i g } }$, we can choose a sub-tube$T _ { G } \subset T$of length$r ,$so that

$$
| T _ {G} \cap E _ {G} | \gtrsim \delta^ {\eta + \varepsilon_ {1}} K _ {\varepsilon_ {1}} ^ {- 2} | T \cap E _ {G} | \gtrsim \delta^ {2 \eta + 2 \varepsilon_ {1}} K _ {\varepsilon_ {1}} ^ {- 3} | T | (\# \mathcal {G}) ^ {- 1 / 3} \gtrsim \delta^ {\eta + \varepsilon_ {1}} K _ {\varepsilon_ {1}} ^ {- 2} r | T |.\tag{A.5}
$$

Furthermore, we can choose these sub-tubes so that every pair of sub-tubes in the set$\{ T _ { G } \colon G \in$ $\mathcal { G } _ { T , \mathrm { s i g } } \}$either coincide or are interior-disjoint.

Since the sets$\{ E _ { G } \}$are disjoint, the volume bound (A.5) says that for each tube$T ,$at most $\delta ^ { - \eta - \varepsilon _ { 1 } } K _ { \varepsilon _ { 1 } } ^ { 2 }$tubes from the set$\{ T _ { G } \colon G \in { \mathcal { G } } _ { T , \operatorname { s i g } } \}$can pairwise coincide (the sets$T _ { G }$are sub-tubes of$T ,$as described previously). Thus for each$T \in \mathbb { T } _ { 1 }$, we can select a set$Y _ { 2 } ( T ) \subset Y _ { 1 } ( T )$with the following properties:

$$
| Y _ {2} (T) | \gtrsim \delta^ {2 \eta + 2 \varepsilon_ {1}} K _ {\varepsilon_ {1}} ^ {- 4} | Y _ {1} (T) |.
$$

(This follows from the first inequality in (A.5), plus the fact that at most$\delta ^ { \eta + \varepsilon _ { 1 } } K _ { \varepsilon _ { 1 } } ^ { - 2 }$can coincide).

• There is a set$\{ T ^ { ( j ) } \}$of sub-tubes of$T ,$each of length r. These tubes are 100r separated. Each of these sub-tubes$T ^ { ( j ) }$intersects$Y _ { 2 } ( T )$, and for each sub-tube$T ^ { ( j ) }$there is exactly one $G \in { \mathcal { G } }$for which$Y _ { 2 } ( T ) \cap T ^ { ( j ) } \cap E _ { G } \neq \emptyset$

Step 2. In Step 1 we processed the tubes. In this step, we will process the grains in${ \mathcal { G } } .$. Fix a grain G. Cover G by boundedly overlapping balls$\{ B _ { i } \}$of radius$2 r$(recall that r was defined in

Step 1). We will select a 100r-separated subset of$\{ B _ { i } \}$(after re-indexing, we will denote this set by$\{ B _ { i } \} _ { i = 1 } ^ { M }$for some$M = M ( G ) \geq 1 )$so that

$$
\sum_ {i = 1} ^ {M} \sum_ {T \in \mathbb {T} _ {1}} | Y _ {2} (T) \cap E _ {G} \cap B _ {i} | \gtrsim \sum_ {T \in \mathbb {T} _ {1}} | Y _ {2} (T) \cap E _ {G} |.\tag{A.6}
$$

Since the balls are 100r-separated, each sub-tube$T ^ { ( j ) }$of length r intersects at most one ball. Thus for each$T \in \mathbb { T } _ { 1 }$and each sub-tube$T ^ { ( j ) }$, there is at most one ball$B _ { i }$from the above collection for which$Y _ { 2 } ( T ) \cap T ^ { ( j ) } \cap E _ { G } \cap B _ { i } \neq \emptyset$

We perform the above operation for each$G \in { \mathcal { G } }$. Let$\mathcal { G } ^ { \prime }$be the union of sets$\{ B _ { i } \cap G \colon i =$ $1 , \ldots , M ( G ) \}$, as$G$ranges over the grains in$\mathcal { G }$. For each$G ^ { \prime } \in { \mathcal { G } } ^ { \prime }$, define$E _ { G ^ { \prime } } = G ^ { \prime } \cap E _ { G }$, where $G \in { \mathcal { G } }$is the (unique) grain that gave rise to$G ^ { \prime }$. We have that the sets$\{ E _ { G ^ { \prime } } \colon G ^ { \prime } \in \mathcal G \}$are disjoint.

Define$\begin{array} { r } { Y _ { 3 } ( T ) = Y _ { 2 } ( T ) \cap \bigcup _ { G ^ { \prime } \in \mathcal { G } ^ { \prime } } E _ { G ^ { \prime } } } \end{array}$. By (A.6) we have that$( \mathbb { T } _ { 1 } , Y _ { 3 } ) _ { \delta }$is$\mathrm { ~ a ~ } \gtrsim 1$refinement of $( \mathbb { T } _ { 1 } , Y _ { 2 } ) _ { \delta }$, which in turn is$\mathrm { a } \gtrsim \delta ^ { 2 \eta + 2 \varepsilon _ { 1 } } K _ { \varepsilon _ { 1 } } ^ { - 4 }$refinement of$( \mathbb { T } , Y ) _ { \delta }$. Furthermore, for each$T \in \mathbb { T } _ { 1 }$it is still the case that there is a set of 100r-separated sub-tubes$\{ T ^ { ( j ) } \}$, each of which has length r and intersects$Y _ { 3 } ( T )$(indeed, any sub-tubes$T ^ { ( j ) }$from the previous collection that fail to intersect$Y _ { 3 } ( T )$ can be discarded), so that for each sub-tube$T ^ { ( j ) }$, there is exactly one$G ^ { \prime } \in \mathcal { G } ^ { \prime }$with$T ^ { ( j ) } \cap E _ { G ^ { \prime } } \neq \emptyset$

Step 3. Let$\mu ^ { \prime } \leq \mu$and let$( \mathbb { T } _ { 1 } , Y _ { 4 } ) _ { \delta }$be a$\gtrapprox \delta ~ 1$refinement (we use$\gtrapprox \delta$to absorb the$K _ { \varepsilon _ { 1 } } ^ { - 4 }$factor) of$( \mathbb { T } _ { 1 } , Y _ { 3 } ) _ { \delta }$with the property that$\# ( \mathbb { T } _ { 1 } ) _ { Y _ { 4 } } ( x ) \sim \mu ^ { \prime }$for each$x \in \bigcup _ { T \in \mathbb { T } _ { 1 } } Y _ { 4 } ( T )$. Since$( \mathbb { T } _ { 1 } , Y _ { 4 } ) _ { \delta }$is a $\approx _ { \delta } \delta ^ { 2 \eta + 2 \varepsilon _ { 1 } }$refinement of$( \mathbb { T } , Y ) _ { \delta }$, we have

$$
\mu^ {\prime} \gtrsim_ {\delta} \delta^ {2 \eta + 2 \varepsilon_ {1}} \mu ,\tag{A.7}
$$

and hence$( \mathbb { T } _ { 1 } , Y _ { 4 } ) _ { \delta }$is broad with error$\lesssim \delta ~ \delta ^ { - 3 \eta - 2 \varepsilon _ { 1 } }$and exponent$\beta .$. We will select$\eta$and$\varepsilon _ { 1 }$ suficiently small, and K suficiently large so that$( \mathbb { T } _ { 1 } , Y _ { 4 } ) _ { \delta }$is broad with error$\le \ K \delta ^ { - \varepsilon }$, and $\mu ^ { \prime } \geq K ^ { - 1 } \delta ^ { \varepsilon } \mu$(c.f. Conclusion (c) from Proposition A.5).

For each$G ^ { \prime } \in \mathcal { G } ^ { \prime }$, define$E _ { G ^ { \prime } } ^ { \prime } = E _ { G ^ { \prime } } \cap \bigcup _ { T \in \mathbb { T } _ { 1 } } Y _ { 4 } ( T )$. After dyadic pigeonholing, we can select a set${ \mathcal { G } } ^ { \prime \prime } \subset { \mathcal { G } } ^ { \prime }$so that$| E _ { G ^ { \prime } } ^ { \prime } |$is the same (up to a factor of 2) for each$G ^ { \prime } \in \mathcal { G } ^ { \prime \prime }$. For each$T \in \mathbb { T } _ { 1 }$1 define$Y _ { 5 } ( T ) = Y _ { 4 } ( T ) \cap \bigcup _ { G ^ { \prime \prime } \in \mathcal { G } ^ { \prime \prime } } E _ { G ^ { \prime \prime } } ^ { \prime }$

Define$N = \# \mathcal { G } ^ { \prime \prime }$. Abusing notation, we will enumerate the elements of$\{ E _ { G ^ { \prime \prime } } ^ { \prime } \colon G ^ { \prime \prime } \in \mathcal { G } ^ { \prime \prime } \}$as $E _ { 1 } , \ldots , E _ { N }$. Since$\# \mathbb { T } _ { Y } ( x ) \sim \mu$and$\begin{array} { r } { K _ { \varepsilon _ { 1 } } ^ { - 1 } \delta ^ { \varepsilon _ { 1 } } \frac { | E | } { \# \mathcal { G } } \leq | E _ { G } | \leq K _ { \varepsilon _ { 1 } } \delta ^ { - \varepsilon _ { 1 } } \frac { | E | } { \# \mathcal { G } } } \end{array}$for each$G \in { \mathcal { G } }$(the latter is true since$\mathcal { G }$was the output of Proposition A.4), we have

$$
\# \mathcal {G} \geq N = \# \mathcal {G} ^ {\prime \prime} \gtrsim_ {\delta} \delta^ {2 \varepsilon_ {1}} \# \mathcal {G}.\tag{A.8}
$$

Define$\mathbb { T } ^ { \prime } = \mathbb { T } _ { 1 }$and$Y ^ { \prime } ( T ) = Y _ { 5 } ( T )$. This choice of$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$satisfies Conclusion (c) from Proposition A.5.

We have

$$
\bigcup_ {T \in \mathbb {T} ^ {\prime}} Y ^ {\prime} (T) = \bigsqcup_ {i = 1} ^ {N} E _ {i},
$$

and if the constant$K = K ( \varepsilon _ { 1 } )$(recall that$\varepsilon _ { 1 }$depends on$\varepsilon )$is chosen suficiently large, then for for each index$i = 1 , \ldots , N$we have

$$
N ^ {- 1} \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \lesssim_ {\delta} N ^ {- 1} \Big | \bigcup_ {T \in \mathbb {T} ^ {\prime}} Y ^ {\prime} (T) \Big | \lesssim | E _ {i} | \leq K \delta (\mathrm{diam} (E _ {i})) ^ {2},
$$

where the final inequality is Corollary A.3. Thus we have established Conclusion (b) from Proposition A.5. Recall that for each$T \in \mathbb { T } ^ { \prime }$, we have a set$\{ T ^ { ( j ) } \}$of tube-segments, each of which has length r. These segments are 100r-separated. Discarding segments if necessary, we may suppose that each tube segment$T ^ { ( j ) }$intersects$Y ^ { \prime } ( T )$. It is still the case that for each surviving tube segments, there is exactly one index i so that$Y ^ { \prime } ( T ) \cap T ^ { ( j ) } \cap E _ { i } \neq \emptyset$. This establishes Conclusions (d.i) and (d.ii).

Step 4. It remains to establish Conclusion (a) from Proposition A.5. We begin with Conclusion (a.i), i.e. we must show that N satisfies Inequality (A.2). In Step 3 we established Conclusion (d.ii). Combining this with (A.4) and (A.8), we conclude that for each$T \in \mathbb { T }$, there are$\lesssim _ { \delta } \delta ^ { - 2 \varepsilon _ { 1 } } N ^ { 1 / 3 }$ indices i for which$Y ^ { \prime } ( T ) \cap E _ { i } \neq \emptyset$. Thus by pigeonholing, there is an index i so that

$$
\{\# T \in \mathbb {T} \colon Y ^ {\prime} (T) \cap E _ {i} \neq \emptyset \} \lesssim_ {\delta} \delta^ {- 2 \varepsilon_ {1}} N ^ {- 2 / 3} (\# \mathbb {T}).
$$

Fix this index i, and denote the above set by$\mathbb { T } _ { i }$. We have

$$
\nu \big (\{(x, T, T ^ {\prime}) \in E _ {i} \times \mathbb {T} _ {i} ^ {2} \colon x \in Y ^ {\prime} (T) \cap Y ^ {\prime} (T ^ {\prime}), \angle (\mathrm{dir} (T), \mathrm{dir} (T)) \gtrsim_ {\delta} \delta^ {(3 \eta + 2 \varepsilon_ {1}) / \beta} \big \} \lesssim_ {\delta} \delta^ {3 - (3 \eta + 2 \varepsilon_ {1}) / \beta} (\# \mathbb {T} _ {i}) ^ {2},\tag{A.9}
$$

where ν denotes the product of Lebesgue measure on$E _ { i }$with counting measure on$\mathbb { T } _ { i } ^ { 2 }$. The above inequality is justified by the observation that for each pair$T , T ^ { \prime } \in \mathbb { T } _ { i }$with${ \cal { L } } ( \mathrm { d i r } ( T ) , \mathrm { d i r } ( T ^ { \prime } ) ) \geq$ $\delta ^ { ( 3 \eta + 2 \varepsilon _ { 1 } ) / \beta }$, we have$| T \cap T ^ { \prime } | \lesssim \delta ^ { 3 - ( 3 \eta + 2 \varepsilon _ { 1 } ) / \beta }$

On the other hand, we have$| E _ { i } | \gtrapprox \delta \delta \delta ^ { \varepsilon _ { 1 } } N ^ { - 1 } \big ( \mu ^ { - 1 } \delta ^ { 2 } ( \# \mathbb { T } ) \big )$, and since$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with error $\lesssim _ { \delta } \delta ^ { - ( 3 \eta + 2 \varepsilon _ { 1 } ) }$, we have that for each$x \in E _ { i }$there are$\gtrsim ( \mu ^ { \prime } ) ^ { 2 }$pairs$T , T ^ { \prime } \in \mathbb { T } _ { i }$so that$( x , T , T ^ { \prime } )$is in the above set. We conclude that by (A.7),

$$
\begin{array}{r l} & {\mu \delta^ {2 + 6 \eta + 4 \varepsilon_ {1}} N ^ {- 1} (\# \mathbb {T}) \lesssim_ {\delta} (\mu^ {\prime}) ^ {2} \cdot \Big (\delta^ {4 \eta + 2 \varepsilon_ {1}} N ^ {- 1} \mu^ {\prime - 1} \delta^ {2} (\# \mathbb {T}) \Big) \lesssim \mathrm{LHS(A.9)}} \\ & {\qquad \lesssim \mathrm{RHS(A.9)} = \delta^ {- (3 \eta + 2 \varepsilon_ {1}) / \beta + 3} (\# \mathbb {T} _ {i}) ^ {2} \lesssim K _ {\varepsilon_ {1}} ^ {2} \delta^ {- (3 \eta + 2 \varepsilon_ {1}) / \beta - 4 \varepsilon_ {1} + 3} N ^ {- 4 / 3} (\# \mathbb {T}) ^ {2}.} \end{array}
$$

Re-arranging, we have

$$
N ^ {1 / 3} \lesssim_ {\delta} K _ {\varepsilon_ {1}} ^ {2} \mu^ {- 1} \delta^ {- (3 \eta + 2 \varepsilon_ {1}) / \beta - 6 \eta - 8 \varepsilon_ {1} + 1} (\# \mathbb {T}).
$$

The claimed bound on N now follows by selecting$3 \eta + 2 \varepsilon _ { 1 } < \varepsilon \beta / 2 0$, and choosing K appropriately.

Finally, Conclusion (a.ii) follows from the definition of r and (A.8).

Lemma A.5 says nothing about the shape of the sets$\{ E _ { i } \}$. The next result will help us show that a substantial portion of each set$E _ { i }$must be contained in the δ neighbourhood of a plane. The idea is that since the volume of$E _ { i }$is small, each point$x \in E _ { i }$is broad, and$E _ { i } \cap T$is dense for each tube$T \in \mathbb { T } _ { i }$, we can find many “triangles” formed by three tubes from$\mathbb { T } _ { i }$that pairwise intersect at distinct points. Since every triple of lines that pairwise intersect at distinct points must be coplanar, this in turn forces a significant subset of$E _ { i }$to be planar.

Lemma A.6. Let$\varepsilon , \beta > 0$. Then there exists$\kappa , \eta > 0$so that the following holds. Let$( \mathbb { T } , Y ) _ { \delta }$be $\delta ^ { \eta }$dense and broad with error$\leq \delta ^ { - \eta }$(and exponent$\beta )$. Suppose that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \leq \delta^ {1 - \eta}.
$$

Then there is a plane Π so that if we define$\mathbb { T } ^ { \prime } = \{ T \in \mathbb { T } \colon T \subset N _ { 2 \delta } ( \Pi ) \}$, then there is a shading $\{ Y ^ { \prime } ( T ) \colon T \in  { \mathbb { T } } ^ { \prime } \}$and a number µ so that

(a)$\# \mathbb { T } _ { Y ^ { \prime } } ^ { \prime } ( x ) \sim \mu$for each$x \in \bigcup _ { T \in \mathbb { T } ^ { \prime } } Y ^ { \prime } ( T )$

(b)

$$
\sum_ {T \in \mathbb {T} ^ {\prime}} | Y ^ {\prime} (T) | \geq \kappa \delta^ {\varepsilon} \sum_ {T \in \mathbb {T}} | Y (T) |.\tag{A.10}
$$

(c)

$$
\Big | \bigcup_ {T \in \mathbb {T} ^ {\prime}} Y ^ {\prime} (T) \Big | \geq \kappa \delta^ {1 + \varepsilon},\tag{A.11}
$$

Proof. First, after dyadic pigeonholing and replacing$( \mathbb { T } , Y ) _ { \delta }$by a refinement, we may suppose that there is a number$\mu$so that$\# \mathbb { T } _ { Y } ( x ) \sim \mu$for all$x \in \bigcup _ { T \in \mathbb { T } } Y ( T )$; we still have that$( \mathbb { T } , Y ) _ { \delta }$is${ \gtrap{ \approx } } \delta ^ { \ n }$ dense, and$( \mathbb { T } , Y ) _ { \delta }$is broad with error${ \lessapprox } \delta ^ { - \eta }$. Observe that

$$
\delta^ {2 + \eta} (\# \mathbb {T}) \lessapprox_ {\delta} \sum_ {T \in \mathbb {T}} | Y (T) | \lesssim \mu \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \leq \delta^ {1 - \eta} \mu ,
$$

and thus

$$
\# \mathbb {T} \lesssim_ {\delta} \delta^ {- 1 - 2 \eta} \mu .\tag{A.12}
$$

Define

$$
\begin{array}{r l} & {\mathbb {T} ^ {\prime} = \{T \in \mathbb {T} \colon | Y (T) | \geq \delta^ {2 \eta} | T | \},} \\ & {E = \{x \in \mathbb {R} ^ {3} \colon \# \mathbb {T} _ {Y} ^ {\prime} (x) \geq \delta^ {2 \eta} \mu \},} \\ & {\mathbb {T} ^ {\prime \prime} = \{T \in \mathbb {T} \colon | Y (T) \cap E | \geq \delta^ {4 \eta} | T | \}.} \end{array}
$$

By double-counting we have$\# \mathbb { T } ^ { \prime \prime } \geq \delta ^ { 5 \eta } ( \# \mathbb { T } )$

Note that for each$T _ { 0 } \in \mathbb { T } ^ { \prime \prime }$and each$x \in Y ( T _ { 0 } ) \cap E$, there are$\ge ~ \frac { 1 } { 2 } \delta ^ { 2 \eta } \mu$tubes$T \in \mathbb { T } ^ { \prime }$with $Y ( T ) \cap Y ( T _ { 0 } ) \neq \emptyset$and$\angle ( \mathrm { d i r } ( T ) , \mathrm { d i r } ( T _ { 0 } ) ) \geq \delta ^ { 3 \eta / \beta } ;$this is because there are$\ge \delta ^ { 2 \eta } \mu$tubes$T \in \mathbb { T } ^ { \prime }$with $Y ( T ) \cap Y ( T _ { 0 } ) \neq \emptyset$, and by broadness at most$\ge \frac { 1 } { 2 } \delta ^ { 3 \eta } \mu$of the tubes passing through a point$\boldsymbol { x } \in \mathbb { R } ^ { 3 }$ can satisfy$Z ( \mathrm { d i r } ( T ) , v ) \le \delta ^ { 3 \eta / \beta }$for any fixed vector$v .$. In particular, for each tube$T _ { 0 }$of this type, there are at least$\left( \delta ^ { 3 \eta } \dot { \mu } \right) \left( \delta ^ { 3 \eta / \beta } \delta ^ { - 1 } \right)$distinct tubes$T \in \mathbb { T } ^ { \prime }$with$T \cap T _ { 0 } \neq \emptyset$and$\begin{array} { r } { { \cal { L } } ( \mathrm { d i r } ( T ) , \mathrm { d i r } ( T _ { 0 } ) ) \geq } \end{array}$ $\delta ^ { 3 \eta / \beta }$. Since each such$T \in \mathbb { T } ^ { \prime }$satisfies$Y ( T ) \geq \delta ^ { 2 \eta } | T |$and$\begin{array} { r } { | T \cap N _ { \delta ^ { 1 0 \eta / \beta } } ( T _ { 0 } ) | \le \frac { 1 } { 2 } \delta ^ { 2 \eta } | T | } \end{array}$, we conclude that for each tube$T _ { 0 }$of the type described above, we have

$$
\sum_{\substack{T\in \mathbb{T}^{\prime}\\ Y(T)\cap Y(T_{0})\neq \emptyset \\ \angle (\mathrm{dir}(T),\mathrm{dir}(T_{0}))\geq \delta^{3\eta /\beta}}} |Y(T)\backslash N_{\delta^{10\eta /\beta}}(T_{0})| \gtrsim \big(\delta^{3\eta +3\eta /\beta}\mu \delta^{-1}\big) \big(\delta^{2\eta}|T|\big) \gtrsim \delta^{10\eta /\beta}\delta \mu .
$$

On the other hand,

$$
\Big|\bigcup_{\substack{T\in \mathbb{T}^{\prime}\\ Y(T)\cap Y(T_{0})\neq \emptyset \\ \angle (\mathrm{dir}(T),\mathrm{dir}(T_{0}))\geq \delta^{3\eta /\beta}}}Y(T)\backslash N_{\delta^{10\eta /\beta}}(T_{0})\Big|\leq \Big|\bigcup_{T\in \mathbb{T}}Y(T)\Big|\leq \delta^{1 - \eta},
$$

Thus if we define$F _ { T _ { 0 } }$to be the set of points$x \in \mathbb { R } ^ { 3 } \backslash N _ { \delta ^ { 1 0 \eta / \beta } } ( T _ { 0 } )$satisfying

$$
\sum_{\substack{T\in \mathbb{T}^{\prime}\\ Y(T)\cap Y(T_{0})\neq \emptyset \\ \angle (\operatorname{dir}(T),\operatorname{dir}(T_{0}))\geq \delta^{3\eta /\beta}}}\chi_{Y(T)}(x)\geq \delta^{11\eta /\beta}\mu ,
$$

then$| F _ { T _ { 0 } } | \ge \delta ^ { 1 1 \eta / \beta + 1 }$because$\# \mathbb { T } _ { Y } ( x ) \lesssim \mu$. Since$( \mathbb { T } , Y ) _ { \delta }$is broad with error$\delta ^ { - \eta }$, for each point $x \in F _ { 0 }$, there are$\gtrsim ( \delta ^ { 1 1 \eta / \beta } \mu ) ^ { 2 }$pairs$T , T ^ { \prime } \in \mathbb { T } ^ { \prime }$satisfying

$$
\begin{array}{l} Y (T) \cap Y (T _ {0}) \neq \emptyset , Y (T ^ {\prime}) \cap Y (T _ {0}) \neq \emptyset , Y (T) \cap Y (T ^ {\prime}) \neq \emptyset , \\ \angle (\mathrm{dir} (T _ {0}), \mathrm{dir} (T)) \geq \delta^ {3 \eta / \beta}, \angle (\mathrm{dir} (T _ {0}), \mathrm{dir} (T ^ {\prime})) \geq \delta^ {3 \eta / \beta}, \angle (\mathrm{dir} (T), \mathrm{dir} (T ^ {\prime})) \geq \delta^ {1 2 \eta / \beta^ {2}}, \\ (T \cap T ^ {\prime}) \backslash N _ {\delta^ {1 0 \eta / \beta}} (T _ {0}) \neq \emptyset . \end{array}\tag{A.13}
$$

For each such pair, we have$| Y ( T ) \cap Y ( T ^ { \prime } ) | \leq | T \cap T ^ { \prime } | \lesssim \delta ^ { 3 - 1 2 \eta / \beta ^ { 2 } }$. We conclude that for$T _ { 0 }$fixed, there ar$\gtrsim ( \delta ^ { 1 1 \eta / \beta } \mu ) ^ { 2 } ( | F _ { T _ { 0 } } | / \delta ^ { 3 - 1 2 \bar { \eta } / \beta ^ { 2 } } ) \gtrsim \delta ^ { 2 3 \bar { \eta } / \beta ^ { 2 } } \mu ^ { 2 } \delta ^ { - 2 }$distinct pairs$( T , T ^ { \prime } )$satisfying$\left( \mathrm { A . 1 3 } \right)$. Thus by (A.12) there are$\gtrsim \delta ^ { 2 3 \bar { \eta } / \beta ^ { 2 } } \mu ^ { 2 } \delta ^ { - 2 } ( \# \mathbb { T } ^ { \bar { \prime } \bar { \prime } } ) \gtrsim \delta ^ { 2 4 \eta / \beta ^ { 2 } } ( \# \mathbb { T } ^ { \prime } ) ^ { 2 } ( \# \bar { \mathbb { T } } )$triples$( T _ { 0 } , T _ { 1 } , T _ { 2 } ) \in \mathbb { T } ^ { \prime \prime } \times \mathbb { T } ^ { \prime } \times \mathbb { T } ^ { \prime }$ that satisfy (A.13).

By pigeonholing, we can select a pair$( T , T ^ { \prime } )$which is a member of$\gtrsim \delta ~ \delta ^ { 2 4 \eta / \beta ^ { 2 } } ( \# \mathbb { T } )$such triples. Fix this pair$T , T ^ { \prime }$, and let$\mathbb { T } _ { 0 }$denote the set of tubes$T _ { 0 }$so that$( T _ { 0 } , \bar { T } ^ { \prime } , T ^ { \prime \prime } )$satisfies (A.13). We have the following:

$T$and$T ^ { \prime }$intersect, and make angle$\gtrsim \delta ^ { 1 2 \eta / \beta ^ { 2 } }$

• For each$T _ { 0 } \in \mathbb { T } _ { 0 }$, we have that$Y ( T _ { 0 } )$intersects both T and$T ^ { \prime }$, and makes angle$\ge \delta ^ { 3 \eta / \beta }$ with T and$T ^ { \prime }$

$$
\bullet (T \cap T ^ {\prime}) \backslash N _ {\delta^ {1 0 \eta / \beta}} (T _ {0}) \neq \emptyset .
$$

The above items imply that each$T _ { 0 } \in \mathbb { T } _ { 0 }$is contained in the$\delta ^ { 1 - 1 0 0 \eta / \beta ^ { 2 } }$neighbourhood of a plane — this is the plane spanned by the tubes$T$and T (the latter plane is technically not well defined, but is instead defined up to uncertainty$\frac { \delta } { \angle ( \mathrm { d i r } ( T ) , \mathrm { d i r } ( T ^ { \prime } ) ) } \leq \delta ^ { 1 - 1 1 } \bar { \eta } ^ { / \beta ^ { 2 } } )$. In particular, there is a set of $\lesssim \delta ^ { 2 0 0 \eta / \beta ^ { 2 } }$planes {Π<sub>i</sub>} so that each$T _ { 0 } \in \mathbb { T } _ { 0 }$is contained in the 2δ neighbourhood of some plane from this collection. By pigeonholing, we can select a plane Π so that

$$
\sum_{\substack{T\in \mathbb{T}_{0}\\ T\subset N_{2\delta}(\Pi)}}|Y(T)|\gtrsim_{\delta}\left(\delta^{200\eta /\beta^{2}}\right)\left(\delta^{2 + 2\eta}\right)\left(\delta^{24\eta /\beta^{2}}(\# \mathbb{T})\right)\gtrsim_{\delta}\delta^{300\eta /\beta^{2}}\sum_{T\in \mathbb{T}}|Y(T)|.
$$

Define$\mathbb { T } ^ { \prime } = \{ T \in \mathbb { T } \colon T \subset N _ { 2 \delta } ( \Pi ) \}$. By pigeonholing, we can select a number$\mu ^ { \prime }$so that if we define the shading$Y ^ { \prime } ( T ) = \{ x \in Y ( T ) \colon \# \mathbb { T } _ { Y } ^ { \prime } ( x ) \sim \mu ^ { \prime } \}$, then$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is an$\approx _ { \delta }$1 refinement of $( \mathbb { T } ^ { \prime } , Y ) _ { \delta }$. This gives Conclusions$\mathrm { ( a ) }$with$\mu ^ { \prime }$in place of$\mu$and (b). Finally, Conclusion (c) follows by a standard Cordoba-type$L ^ { 2 }$argument (making use of the fact that$( \mathbb { T } ^ { \prime } , Y ^ { \prime } ) _ { \delta }$is broad with error $\delta ^ { - 4 0 0 \eta / \beta ^ { 2 } }$and exponent$\beta )$□

Next, we record the following re-scaled variant of Lemma A.6

Corollary A.7. Let$\varepsilon , \beta > 0$. Then there exists$\kappa , \eta > 0$so that the following holds. Let$0 < \delta <$ $r \leq 1$and let$B \subset \mathbb { R } ^ { 3 }$be a ball of radius r. Let$( \mathbb { T } , Y ) _ { \delta }$be broad with error$\delta ^ { - \eta }$(and exponent$\beta )$ Suppose that$Y ( T ) \subset B$for each$T \in \mathbb { T }$, and$\begin{array} { r } { \sum _ { T \in \mathbb { T } } | Y ( T ) | \ge \delta ^ { \eta } \delta ^ { 2 } r ( \# \mathbb { T } ) } \end{array}$. Suppose furthermore that the tubes in T are contained in a 1 tube$T _ { 1 }$, and that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \leq r ^ {2} \delta^ {1 - \eta}.
$$

Then there is a set$\mathbb { T } ^ { \prime } \subset \mathbb { T } _ { : }$a number µ; a shading$Y ^ { \prime } ( T ) \subset Y ( T ) , T \in \mathbb { T } ^ { \prime }$; a prism P of dimensions comparable to$\delta \times r \times r$so that each$T \in \mathbb { T } ^ { \prime }$satisfies$T \cap P \neq \emptyset$, and T exists P through its long sides, in the sense of Remark 7.16. Furthermore, we have

(a)$\# \mathbb { T } _ { Y ^ { \prime } } ^ { \prime } ( x ) \sim \mu$for each$x \in \bigcup _ { T \in \mathbb { T } ^ { \prime } } Y ^ { \prime } ( T )$

(b)

$$
\sum_ {T \in \mathbb {T} ^ {\prime}} | Y ^ {\prime} (T) | \geq \kappa \delta^ {\varepsilon} \sum_ {T \in \mathbb {T}} | Y (T) |.\tag{A.14}
$$

(c)

$$
\Big | \bigcup_ {T \in \mathbb {T} ^ {\prime}} Y ^ {\prime} (T) \Big | \geq \kappa \delta^ {1 + \varepsilon} r ^ {2}.\tag{A.15}
$$

We are now ready to prove Proposition 7.15. In brief, we use Lemma$\mathrm { A . 5 }$to cover a substantial portion of$( \mathbb { T } , Y ) _ { \delta }$by a union of disjoint sets$\left\{ E _ { i } \right\}$, and then we use Corollary$\mathrm { A . 7 }$to trap a substantial portion of each set$E _ { i }$in a prism$P _ { i }$of dimensions comparable to$\delta \times r \times r$, for an appropriately chosen diameter r.

## Proof of Proposition 7.15.

Step 1. Let$\delta _ { 0 } , \varepsilon _ { 1 } , \varepsilon _ { 2 }$be small numbers to be chosen below. We will select$\delta _ { 0 }$very small compared to$\varepsilon _ { 1 } , \varepsilon _ { 1 }$very small compared to$\varepsilon _ { 2 } ,$and$\eta ,$κ very small compared to$\varepsilon _ { 1 }$. These numbers depend on$\varepsilon$and$\beta$. We may suppose that$\delta \leq \delta _ { 0 }$, or else the result is immediate provided we choose κ suficiently small so that$\kappa \delta ^ { \varepsilon } ( \delta \mathbb { T } ) ^ { - 1 } \leq \delta$. In this case the set$\mathcal { G }$consists of$\delta \times \delta \times \delta$balls, and there is nothing to prove. Henceforth we shall assume that$\delta \leq \delta _ { 0 }$

After dyadic pigeonholing and replacing$( \mathbb { T } , Y ) _ { \delta }$by$\mathrm { a } \sim ( \log 1 / \delta )$<sup>−1</sup> refinement, we may suppose there exists a number$\mu \geq 1$so that$\# \mathbb { T } _ { Y } ( x ) \in [ \mu , 2 \mu )$for every$x \in \bigcup _ { T \in \mathbb { T } } Y ( T )$; we still have that $( \mathbb { T } , Y ) _ { \delta }$is broad with error$\delta ^ { - \eta }$

Apply Lemma A.5 to$( \mathbb { T } , Y ) _ { \delta }$with$\varepsilon _ { 1 }$in place of ε and$\beta$as above; we can do this, provided we select$\eta > 0$suficiently small depending on$\varepsilon _ { 1 }$and$\beta .$Let$K _ { 1 } , N , ( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$, and$E _ { 1 } , \ldots , E _ { N }$be the output of that lemma. In particular,$( \mathbb { T } _ { 1 } , Y _ { 1 } )$is broad with error$K _ { 1 } \delta ^ { - \varepsilon _ { 1 } }$. Note that by Item (a), we have

$$
r \geq K _ {1} ^ {- 2} \delta^ {2 \varepsilon_ {1}} (\delta \# \mathbb {T}) ^ {- 1} \mu .\tag{A.16}
$$

Let$I _ { 1 }$denote the set of indices in$\{ 1 , \ldots , N \}$for which

$$
\# \{T \in \mathbb {T} _ {1} \colon Y _ {1} (T) \cap E _ {i} \neq \emptyset \} \leq 2 N ^ {- 1} r ^ {- 1} (\# \mathbb {T}),
$$

and let$I _ { 2 }$denote the remaining indices. For each$T \in \mathbb { T } _ { 1 }$, there are at most$( 1 0 0 r ) ^ { - 1 }$sets$E _ { i }$for which$Y _ { 1 } ( T ) \cap E _ { i } \neq \emptyset$. Thus

$$
\# I _ {2} \leq \left(2 N ^ {- 1} r ^ {- 1} (\# \mathbb {T})\right) ^ {- 1} \sum_ {T \in \mathbb {T}} \# (i: Y _ {1} (T) \cap E _ {i} \neq \emptyset) \leq N / 2.
$$

We conclude that #$I _ { 1 } \geq N / 2$. For each$i \in I _ { 1 }$, define

$$
\mathbb {T} ^ {(i)} = \{T \in \mathbb {T}: Y _ {1} (T) \cap E _ {i} \neq \emptyset \}.
$$

We have

$$
\begin{array}{l} \sum_ {T \in \mathbb {T} ^ {(i)}} | Y _ {1} (T) \cap E _ {i} | \geq K _ {1} ^ {- 1} \delta^ {\varepsilon_ {1}} \mu | E _ {i} | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq \mu K _ {1} ^ {- 2} \delta^ {2 \varepsilon_ {1}} N ^ {- 1} \Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq K _ {1} ^ {- 1} N ^ {- 1} \delta^ {2 \varepsilon_ {1} + \eta} (| T | \# \mathbb {T}) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq K _ {1} ^ {- 2} \delta^ {2 \varepsilon_ {1} + \eta} N ^ {- 1} (N r / 2) (| T | \# \mathbb {T} ^ {(i)}) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq K _ {1} ^ {- 3} \delta^ {3 \varepsilon_ {1} + \eta} (\delta^ {2} r) (\# \mathbb {T} ^ {(i)}). \end{array}
$$

In the above, the first inequality used Conclusion (c) of Lemma$\mathrm { A . 5 ; }$the second inequality used $\left( \mathrm { { A . 3 } } \right)$; the third inequality used the fact that$( \mathbb { T } , Y ) _ { \delta }$is$\delta ^ { \eta }$dense, and$\# \mathbb { T } _ { Y } ( x ) \sim \mu$for each $x \in \bigcup Y ( T )$; and the fourth inequality used the fact that$i \in I _ { 1 }$

Step 2. By (A.3) we have$| E _ { i } | \ \le \ K \delta \big ( \mathrm { d i a m } ( E _ { i } ) \big ) ^ { 2 }$, and by Conclusion (b) of Lemma$\mathrm { A . 5 } ,$ dia$\begin{array} { l } { \operatorname { 1 } ( E _ { i } ) ~ \leq ~ 2 r } \end{array}$. Let$B _ { i }$be a ball of radius r that contains$E _ { i }$. For each$T \in \mathbb { T } ^ { ( i ) }$define $Y ^ { ( i ) } ( T ) = Y _ { 1 } ( T ) \cap E _ { i } \subset B _ { i }$. If$\delta _ { 0 }$and$\varepsilon _ { 1 }$are chosen suficiently small depending on$\varepsilon _ { 2 }$and$\beta ,$ then by Step 1,$( \mathbb { T } ^ { ( i ) } , Y ^ { ( i ) } ) _ { \delta }$satisfies the hypotheses of Corollary A.7. Applying this Corollary, we obtain a set$G _ { i }$comparable to a$\delta \times r \times r$prism; a number$\mu _ { i } ;$a set$\mathbb { T } ^ { ( i ) \prime } \subset \mathbb { T } ^ { ( i ) }$; and a sub-shading $Y ^ { ( i ) \prime } ( T ) \subset Y ^ { ( i ) } ( T ) , { \overline { { T } } } \in \mathbb { T } ^ { ( i ) \prime }$, so that the following holds:

• Each$T \in \mathbb { T } ^ { ( i ) \prime }$intersects$G _ { i }$and exits$G _ { i }$through its long ends, in the sense of Remark 7.16.

$$
\sum_ {T \in \mathbb {T} ^ {(i) \prime}} | Y ^ {(i) \prime} (T) | \geq \kappa_ {2} \delta^ {\varepsilon_ {2}} \sum_ {T \in \mathbb {T} ^ {(i)}} | Y ^ {(i)} (T) |.
$$

$$
\Big | \bigcup_ {T \in \mathbb {T} ^ {(i) \prime}} Y ^ {(i) \prime} (T) \Big | \geq \kappa_ {2} \delta^ {1 + \varepsilon_ {2}} r ^ {2} \gtrsim \kappa_ {2} \delta^ {\varepsilon_ {2}} | G _ {i} |.
$$

• For each$x \in \bigcup _ { T \in \mathbb { T } ^ { ( i ) } } Y ^ { ( i ) \prime } ( T )$we have$\# \mathbb { T } _ { Y ^ { ( i ) \prime } } ^ { ( i ) \prime } ( x ) \sim \mu _ { i }$

After dyadic pigeonholing, we can select a number$\mu ^ { \prime }$and a set of indices$I _ { 1 } ^ { \prime } \subset I _ { 1 }$so that$\mu _ { i } \sim \mu ^ { \prime }$ for each$i \in I _ { 1 } ^ { \prime }$. We will choose$\mu ^ { \prime }$in such a way that if we define$\mathcal { G } = \{ G _ { i } \colon i \in I _ { 1 } ^ { \prime } \}$, define the shading

$$
Y (G _ {i}) = \bigcup_ {T \in \mathbb {T} ^ {(i) \prime}} Y ^ {(i) \prime} (T),
$$

and define the shading

$$
Y _ {2} (T) = Y _ {1} (T) \cap \bigcup_ {G} Y (G),
$$

where the union is taken over those$G \in { \mathcal { G } }$for which$T \in \mathbb { T } ^ { ( i ) \prime }$, then$( \mathbb { T } _ { 1 } , Y _ { 2 } ) _ { \delta }$is$\mathrm { a } \gtrapprox \delta ^ { \varepsilon _ { 2 } }$refinement of$( \mathbb { T } _ { 1 } , Y _ { 1 } ) _ { \delta }$, and thus$\mathrm { a } \gtrapprox \delta \delta ^ { \varepsilon _ { 1 } + \varepsilon _ { 2 } }$refinement of$( \mathbb { T } , Y ) _ { \delta }$

Note that for each$G _ { i } \in \mathcal G$, we have$Y ( G _ { i } ) \subset G _ { i } \cap E _ { i } .$, and thus the sets$\{ Y ( G ) \colon G \in { \mathcal { G } } \}$are disjoint. Furthermore,$| Y _ { 1 } ( G ) | \geq \kappa _ { 2 } \delta ^ { \varepsilon _ { 2 } } | G _ { i } |$, and thus$( \mathcal { G } , Y ) _ { \delta \times r \times r }$is$\kappa _ { 2 } \delta ^ { \varepsilon _ { 2 } }$dense.

We have the following:

(i)$\textstyle \bigcup _ { \mathbb { T } } Y _ { 2 } ( T ) = \bigcup _ { G \in { \mathcal { G } } } Y ( G )$

(ii) If$Y _ { 2 } ( T ) \cap Y ( G ) \neq \emptyset$, then T exits G through its long ends, in the sense of in the sense of Remark 7.16.

(iii) If$Y _ { 2 } ( T ) \cap Y ( G ) \neq \emptyset$, then$Y _ { 2 } ( T ) \cap G \subset Y ( G )$

Item (iii) follows from the fact that if$Y _ { 2 } ( T ) \cap Y ( G _ { i } ) \neq \emptyset$for some$G _ { i } \in \mathcal G$(recall that$G _ { i }$is a prism associated to a set$E _ { i } )$, then there is a length-r sub-tube$T ^ { ( j ) } \subset T$so that$Y _ { 2 } ( T ) \cap T ^ { ( j ) } \subset E _ { i } \subset Y ( G _ { i } )$ Since the sub-tubes$\{ T ^ { ( j ) } \}$associated to$T$are 100r separated, and diam$. ( G ) \leq 1 0 r$, we conclude that$T ^ { ( j ) }$is the only sub-tube from the above collection that intersects G.

We conclude that$( \mathcal { G } , Y ) _ { \delta \times r \times r }$is a robustly$\kappa _ { 2 } \delta ^ { \varepsilon _ { 2 } }$-dense two-scale grains decomposition of $( \mathbb { T } _ { 1 } , Y _ { 2 } ) _ { \delta }$wrt the single 1-tube$\{ T _ { 1 } \}$. Finally, the desired bound on r is given by (A.16).□

## B Wolf ’s hairbrush argument and the proof of Proposition 1.8

The goal of this section is to prove Proposition 1.8. We will restate it here in an expanded form.

Proposition 1.8, expanded. For all$\varepsilon > 0$, there exists$\kappa , \eta > 0$so that the following holds for all$\delta > 0$. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, with$C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Then

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \geq \kappa \delta^ {3 / 2 + \varepsilon} (\# \mathbb {T}) ^ {1 / 2}.\tag{B.1}
$$

Proof. The proof uses a standard “bilinear” or “robust transversality” argument to reduce to the case where a typical pair of intersecting tubes make large angle (i.e. the unit vectors dir(T) and dir(T<sup>′</sup>) are far from parallel), followed by Wolf’s hairbrush argument. Since these arguments are covered in detail elsewhere (see e.g. [21, §2.4]), we will just provide a brief sketch.

Fix$\varepsilon > 0$and let$\eta > 0$be a small quantity to be chosen below. Let$( \mathbb { T } , Y ) _ { \delta }$be$\delta ^ { \eta }$dense, with $C _ { K T - C W } ( \mathbb { T } ) \le \delta ^ { - \eta }$and$C _ { F - S W } ( \mathbb { T } ) \le \delta ^ { - \eta }$. Applying standard reductions, we may replace$( \mathbb { T } , Y ) _ { \delta }$ by$\mathrm { ~ a ~ } \ge \delta ^ { \eta }$dense refinement so that the following holds: There exists a number$\theta \in [ \delta , 1 ]$so that for each$x \in \bigcup _ { T \in \mathbb { T } } Y ( T )$, there is a vector$v = v ( x )$so that$\angle ( v , \mathrm { d i r } ( T ) ) \leq \theta$for each$T \in \mathbb { T }$with $x \in Y ( T )$, and for each unit vector$w \in \mathbb { R } ^ { 3 }$and each$r \in [ \delta , \theta ]$, we have

$$
\# \{T \in \mathbb {T} _ {Y} (x), \angle (w, \operatorname{dir} (T)) \leq r \} \leq (r / \theta) ^ {\eta} \# \mathbb {T} _ {Y} (x).
$$

Furthermore, there exists a balanced partitioning cover$\mathbb { T } _ { \theta }$of T, so that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | = \sum_ {T _ {\theta} \in \mathbb {T} _ {\theta}} \Big | \bigcup_ {T \in \mathbb {T} [ T _ {\theta} ]} Y (T) \Big |.\tag{B.2}
$$

After a further refinement, we may suppose that each set$\mathbb { T } ^ { T _ { \theta } }$is$\delta ^ { 3 \eta } .$-dense. Note that$\mathbb { T } ^ { T _ { \theta } }$is a set of$\delta / \theta$tubes that satisfies the broadness condition

$$
\# \{T ^ {T _ {\theta}} \in \mathbb {T} _ {Y ^ {T _ {\theta}}} ^ {T _ {\theta}} (x), \angle (w, \mathrm{dir} (T ^ {T _ {\theta}})) \leq r \} \leq r ^ {\eta} \big (\# \mathbb {T} _ {Y ^ {T _ {\theta}}} ^ {T _ {\theta}} (x) \big),
$$

for all unit vectors w and all$r \in [ \delta / \theta , 1 ]$. Thus a standard application of Wolf’s hairbrush argument [27] for 2-broad tubes shows that

$$
\Big | \bigcup_ {T ^ {\theta} \in \mathbb {T} ^ {T _ {\theta}}} Y ^ {T _ {\theta}} (T ^ {T _ {\theta}}) \Big | \gtrsim \delta^ {(5 / 3) (3 \eta)} (\delta / \theta) ^ {1 / 2} \Big ((\delta / \theta) (\# \mathbb {T} ^ {T _ {\theta}}) \Big) ^ {1 / 2}.
$$

By (B.2), we conclude that

$$
\Big | \bigcup_ {T \in \mathbb {T}} Y (T) \Big | \gtrsim \delta^ {5 \eta} \delta^ {3 / 2} \theta^ {1 / 2} \sum_ {T _ {\theta} \in \mathbb {T} _ {\theta}} (\# \mathbb {T} ^ {T _ {\theta}}) ^ {1 / 2} \gtrsim \delta^ {5 \eta} \delta^ {3 / 2} \theta^ {1 / 2} (\# \mathbb {T} _ {\theta}) ^ {1 / 2} (\# \mathbb {T} ^ {1 / 2}).
$$

(B.1) now follows from the observation that$\# \mathbb { T } [ T _ { \theta } ] \leq \theta C _ { F - S W } ( \mathbb { T } ) ( \# \mathbb { T } ) \underset { \approx \delta } { \lesssim } \delta ^ { - 2 \eta } \theta ( \# \mathbb { T } )$, and thus $\# \mathbb { T } _ { \theta } \gtrapprox \delta \delta ^ { 2 \eta } \theta ^ { - 1 }$□

## References

[1] J. Bennett, A. Carbery, T. Tao. On the multilinear restriction and Kakeya conjectures. Acta Math. 196(2): 261–302, 2006.

[2] A. Besicovitch. Sur deux questions d’integrabilite des fonctions. J. Soc. Phys. Math. 2:105–123, 1919.

[3] J. Bourgain. Besicovitch type maximal operators and applications to Fourier analysis. Geom. Funct. Anal. 1:147–187, 1991.

[4] J. Bourgain. On the Erd˝os-Volkmann and Katz-Tao ring conjectures. Geom. Funct. Anal. 13(2): 334–365, 2003.

[5] R. Davies. Some remarks on the Kakeya problem. Proc. Cambridge Philos. Soc. 69(3): 417–421. 1971.

[6] A. Cordoba. The Kakeya maximal function and the spherical summation multipliers. Am. J. Math. 99:1–22, 1977.

[7] Z. Dvir, S. Gopi. On the number of rich lines in truly high dimensional sets. Proc. 31st International Symposium on Computational Geometry (SoCG 2015). 584–598, 2015.

[8] C. Feferman. The multiplier problem for the ball. Ann. of Math 94(2): 330–336, 1971.

[9] L. Guth. Degree reduction and graininess for Kakeya-type sets in$\mathbb { R } ^ { 3 }$. Rev. Mat. Iberoam. 32(2): 447–494, 2014

[10] L. Guth. Polynomial Methods in Combinatorics, volume 64 of University Lecture Series. American Mathematical Society, 2016.

[11] L. Guth. A restriction estimate using polynomial partitioning. J. Amer. Math. Soc. 29:371–413, 2016.

[12] L. Guth. A restriction estimate using polynomial partitioning II. Acta Math. 221:81–142, 2018.

[13] L. Guth and N.H. Katz. On the Erd˝os distinct distances problem in the plane. Ann. of Math. 181:155–190, 2015.

[14] L. Guth and J. Zahl. Polynomial Wolf axioms and Kakeya-type estimates in$\mathbb { R } ^ { 4 }$. Proc. London Math. Soc. 117:192–220, 2018.

[15] J. Hickman, K.M. Rogers, R. Zhang. Improved bounds for the Kakeya maximal conjecture in higher dimensions. Am. J. Math. 144(6): 1511–1560, 2022.

[16] N.H. Katz, I. Laba, T. Tao. An improved bound on the Minkowski dimension of Besicovitch sets in$\mathbb { R } ^ { 3 }$. Ann. of Math. 152: 383–446, 2000.

[17] N.H. Katz, T. Tao. Recent progress on the Kakeya conjecture. Publ. Mat. 46:161–179, 2002.

[18] N.H. Katz and T. Tao, New bounds for Kakeya problems. J. Anal. Math. 87:231—263, 2002.

[19] N.H. Katz, S. Wu, J. Zahl. Kakeya sets from lines in SL<sub>2</sub>. Ars Inven. Anal.. Paper No. 6, 23 pp, 2023.

[20] N.H. Katz, J. Zahl. An improved bound on the Hausdorf dimension of Besicovitch sets in$\mathbb { R } ^ { 3 }$ J. Amer. Math. Soc. 32(1):195–259, 2019.

[21] N.H. Katz, J. Zahl. A Kakeya maximal function estimate in four dimensions using planebrushes. Rev. Mat. Iberoam. 37(1):317–359, 2021.

[22] T. Keleti. Are lines much bigger than line segments? Proc. Am. Math. Soc. 144(4):1535–1541, 2016.

[23] T. Keleti and A. M´ath´e. Equivalences between diferent forms of the Kakeya conjecture and duality of Hausdorf and packing dimensions for additive complements. arXiv:2203.15731, 2022.

[24] T. Tao. Stickiness, graininess, planiness, and a sum-product approach to the Kakeya problem. https://terrytao.wordpress.com/2014/05/07/stickiness-graininess-planiness-and-a-sum-product-approach-to-the-kakeya-problem

[25] H. Wang, J. Zahl. Sticky Kakeya sets and the sticky Kakeya conjecture. arXiv:2210.09581, 2022.

[26] H. Wang, J. Zahl. The Assouad dimension of Kakeya sets in$\mathbb { R } ^ { 3 }$. arXiv:2401.12337, 2024.

[27] T. Wolf. An improved bound for Kakeya type maximal functions. Rev. Mat. Iberoam. 11:651–674, 1995.

[28] T. Wolf. Recent work connected with the Kakeya problem, Prospects in mathematics (Princeton, NJ, 1996), 129–162, Amer. Math. Soc., Providence, RI, 1999.

[29] T. Wolf: A mixed norm estimate for the x-ray transform. Rev. Mat. Iberoam. 14:561–601, 1998.

[30] R. Wongkew. Volumes of tubular neighbourhoods of real algebraic varieties. Pacific J. Math. 159:177–184, 1993.

[31] J. Zahl. New Kakeya estimates using Gromov’s algebraic lemma. Adv. Math. 380, 2021.