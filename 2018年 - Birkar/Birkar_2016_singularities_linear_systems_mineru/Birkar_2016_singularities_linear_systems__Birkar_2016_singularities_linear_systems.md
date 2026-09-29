# Singularities of linear systems and boundedness of Fano varieties

Caucher Birkar

Abstract. We study log canonical thresholds (also called global log canonical threshold or α-invariant) of R-linear systems. We prove existence of positive lower bounds in diferent settings, in particular, proving a conjecture of Ambro. We then show that the Borisov-Alexeev-Borisov conjecture holds, that is, given a natural number d and a positive real number ǫ, the set of Fano varieties of dimension d with ǫ-log canonical singularities forms a bounded family. This implies that birational automorphism groups of rationally connected varieties are Jordan which in particular answers a question of Serre. Next we show that if the log canonical threshold of the anti-canonical system of a Fano variety is at most one, then it is computed by some divisor, answering a question of Tian in this case.

## Contents

1. Introduction 2  
2. Preliminaries 9  
2.1. Divisors 9  
2.2. Pairs and singularities 10  
2.4. Fano pairs 10  
2.5. Minimal models, Mori fibre spaces, and MMP 10  
2.6. Plt pairs 11  
2.8. Bounded families of pairs 12  
2.9. Effective birationality and birational boundedness 12  
2.12. Complements 12  
2.14. From bounds on lc thresholds to boundedness of varieties 13  
2.16. Sequences of blowups 13  
2.18. Analytic pairs and analytic neighbourhoods of algebraic singularities 14  
2.19. Étale morphisms 15  
2.22. Toric varieties and toric MMP 15  
2.23. Bounded small modifications 15  
2.25. Semi-ample divisors 16  
3. Lc thresholds of anti-log canonical systems of Fano pairs 17  
4. Complements in a neighbourhood of a non-klt centre 22  
5. Singularities of divisors with bounded degree 27  
5.1. Finite morphisms to the projective space 27  
5.3. Bound on the length of blowup sequences 28  
5.6. Bound on multiplicity at an lc place 31  
5.10. Construction of $\Lambda$ 37  
6. Proof of main results 42

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Date: December 2, 2020.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2010 MSC: 14J45, 14E30, 14C20.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Keywords: Fano varieties, bounded families, linear systems, log canonical thresholds, minimal mode program.</span></small>

References

## 1. Introduction

We work over an algebraically closed field of characteristic zero unless stated otherwise.

Boundedness of singular Fano varieties. A normal projective variety X is Fano if $- K _ { X }$is ample and if X has log canonical singularities. Fano varieties are among the most extensively studied varieties because of their rich geometry. They are of great importance from the point of view of birational geometry, diferential geometry, arithmetic geometry, derived categories, mirror symmetry, etc.

Given a smooth projective variety W with$K _ { W }$not pseudo-efective, the minimal model program produces a birational model Y of W together with a Mori fibre space structure $Y  Z [ 7 ]$. A general fibre of$Y  Z$is a Fano variety X with terminal singularities. Thus it is no surprise that Fano varieties constitute a fundamental class in birational geometry. It is important to understand them individually but also collectively in families for various reasons such as construction of moduli spaces.

In dimension one, there is only one Fano variety up to isomorphism which is$\mathbb { P } ^ { 1 }$. In dimension two, there are many, in fact, infinitely many families. To get a better picture one needs to impose a bound on the singularities. For example, it is a classical result tha the smooth Fano surfaces form a bounded family. More generally, the Fano surfaces with ǫ-log canonical (ǫ-lc) singularities form a bounded family [1], for any fixed$\epsilon > 0$(see 2.2 for definition of singularities). The smaller is ǫ the larger is the family.

In any given dimension, there is a bounded family of smooth Fano varieties [26] (also see [32][10]). This is proved using geometry of rational curves. Unfortunately, this method does not work when one allows singularities. On the other hand, toric Fano varieties of given dimension with ǫ-lc singularities also form a bounded family [9], for fixed$\epsilon > 0$. In this case, the method of proof is based on combinatorics.

The results mentioned above led Alexeev [1] and the Borisov brothers [9] to conjecture that, in any given dimension, Fano varieties with ǫ-lc singularities form a bounded family, for fixed$\epsilon > 0$. A generalised form of this statement, which is known in the literature as the Borisov-Alexeev-Borisov or the BAB conjecture, is our first result.

Theorem 1.1. Let d be a natural number and ǫ be a positive real number. Then the projective varieties X such that

$( X , B )$is ǫ-lc of dimension d for some boundary B, and

$- ( K _ { X } + B )$is nef and big,

form a bounded family.

The theorem would not hold if one takes$\epsilon = 0$(see below): it already fails in dimension two, and in dimension three it fails even if we replace bounded by birationally bounded [30].

In addition to the results mentioned earlier, there are numerous other partial cases of the theorem in the literature (also see Nikulin [35][34][33] for related results in dimension two). Indeed boundedness was known for:

• Fano 3-folds with terminal singularities and Picard number one [22],

• Fano 3-folds with canonical singularities [27],

• spherical Fano varieties [2],

• Fano 3-folds with klt singularities and fixed Cartier index of$K _ { X } \ [ 8 ]$2

• Fano varieties of given dimension with klt singularities and fixed Cartier index of $K _ { X } \ [ 1 3 ]$;

• Fano varieties$X$of given dimension equipped with a boundary$\Delta$such that$K _ { X } +$ $\Delta \equiv 0 , ( X , \Delta )$is ǫ-lc for fixed$\epsilon > 0$, and such that the coeficients of$\Delta$belong to a DCC set [13], or more generally when the coeficients of$\Delta$are bounded from below away from zero [5].

We give two examples of unbounded families of klt Fano varieties of dimension two.

Example 1.2. For each natural number$n \geq 2 ,$, let$X _ { n }$be the projective cone over the rational curve of deg n in$\mathbb { P } ^ { n }$. Let$f \colon W _ { n } \to X _ { n }$be given by the blowup of the vertex, and let E be the exceptional curve. Using adjunction it is easy to show that

$$
K _ {W _ {n}} + \frac {n - 2}{n} E = f ^ {*} K _ {X _ {n}}.
$$

Thus$X _ { n }$is$\mathrm { ~ a ~ } \frac { 2 } { n } { - } \mathrm { l c }$Fano variety. As$n  \infty$, the singularities of$X _ { n }$get worse. Now $\{ X _ { n } \mid n \in \mathbb { N } , n \stackrel { \cdot \cdot } { \geq } 2 \}$is not a bounded family otherwise the Cartier index of$K _ { X _ { n } }$would have been bounded which in turn would imply that the coeficient of E in the above formula belongs to a fixed finite set which is clearly not the case.

## Example 1.3. Consider the pair

$$
(\mathbb {P} ^ {2}, \Delta = S + T + R)
$$

where S, T, R are the coordinate lines. Let$V _ { 1 } \to { \mathbb P } ^ { 2 }$be the blowup of$x _ { 0 } : = S \cap T$. Let $V _ { 2 }  V _ { 1 }$be the blowup of$x _ { 1 } : = S ^ { \sim } \cap E _ { 1 }$where$E _ { 1 }$is the exceptional divisor of$V _ { 1 } \to \mathbb { P } ^ { 2 }$ and$S ^ { \sim }$is the birational transform of S. Similarly define$V _ { n }  V _ { n - 1 }$where in each step we blowup the intersection point of$S ^ { \sim }$with the newest exceptional curve. The$V _ { n }$are all toric varieties, in particular,$- K _ { V _ { n } }$is big. Run an MMP on$- K _ { V _ { n } }$and let$X _ { n } ^ { \prime }$be the resulting model. Then$X _ { n } ^ { \prime }$is a klt toric weak Fano variety. Let$X _ { n } ^ { \prime }  X _ { n }$be the contraction defined by$- K _ { X _ { n } ^ { \prime } }$. Then$X _ { n }$is a klt toric Fano variety. Now$\{ X _ { n } \mid n \in \mathbb { N } \}$is not a bounded family because$\left\{ V _ { n } \mid n \in \mathbb { N } \right\}$is not a bounded family: indeed if the$X _ { n }$form a bounded family, then each$K _ { X _ { n } }$has a klt m-complement for some m independent of$n ;$but then each$K _ { V _ { n } }$ would also have a klt m-complement which implies the$V _ { n }$form a bounded family by [15]; this is a contradiction because the Picard number of$V _ { n }$is clearly not bounded.

It is easy to see that Theorem 1.1 is equivalent to the following statement.

Corollary 1.4. Let d be a natural number and ǫ be a positive real number. Then the projective varieties X such that

$( X , \Delta )$is ǫ-lc of dimension d for some boundary$\Delta _ { \cdot }$

$K _ { X } + \Delta \sim _ { \mathbb { R } } ~$0 and$\Delta$is big,

## form a bounded family.

The corollary was previously known when the coeficients of$\Delta$are in a fixed DCC set [15] or when the coeficients are bounded from below away from zero [5].

The pairs$( X , \Delta )$in the corollary are log Calabi-Yau pairs with big boundary. Viewed in this context one is immediately led to the question: what other classes of log Calabi-Yau pairs form bounded families? In fact one can ask a host of hard fundamental questions regarding boundedness, singularities, complements and linear systems, in the more general context of log Calabi-Yau fibrations.

For example, a conjecture of M<sup>c</sup>Kernan and Prokhorov [31] predicts that the set of projective rationally connected varieties X such that$( X , \Delta )$is log Calabi-Yau of given dimension with ǫ-lc singularities for fixed$\epsilon > 0$forms a bounded family. Without the rational connectedness assumption the conjecture does not hold as, for example, all smooth K3 surfaces do not form a bounded family. The conjecture is a more general form of 1.4 since the X in the corollary are of Fano type hence automatically rationally connected. Here by X being of Fano type we mean there is a boundary B such that (X, B) is klt and $- ( K _ { X } + B )$is nef and big.

For a systematic treatment of generalised log Calabi-Yau fibrations, see [4].

Jordan property of Cremona groups. Prokhorov and Shramov [39] studied the birational automorphism group of algebraic varieties using techniques of birational geometry. They investigated the question whether such groups are Jordan. They in particular showed that the BAB conjecture, that is Theorem 1.1, implies the Jordan property for rationally connected varieties.

A group C is Jordan of index h if for any finite subgroup G of C there is a normal abelian subgroup H of G of index at most h. When we say C is Jordan we mean that it is Jordan of index h for some h.

Corollary 1.5. Let d be a natural number. Then there is a natural number h depending only on d satisfying the following. Let k be a field of characteristic zero (not necessarily algebraically closed) and X be a rationally connected variety of dimension d over k. Then the birational automorphism group Bir(X) is Jordan of index h.

The corollary follows immediately from Theorem 1.1 and [39, Theorem 1.8]. If we take $X = \mathbb { P } _ { k } ^ { d }$in the corollary, then we deduce that the Cremona group$\mathrm { C r } _ { d } ( k ) : = \mathrm { B i r } ( \mathbb { P } _ { k } ^ { d } )$is Jordan, answering a question of Serre [41, 6.1] which was the main motivation for the work [39].

Note that Bir(X) is not Jordan for arbitrary algebraic varieties X. Indeed when X is the product of$\mathbb { P } _ { k } ^ { 1 }$and an abelian variety, then Bir(X) is not Jordan [45]. However, if X is a non-uniruled variety, then Bir(X) is always Jordan [40].

Lc thresholds of R-linear systems. Let (X, B) be an lc pair. The lc threshold of an R-Cartier R-divisor$L \geq 0$with respect to$( X , B )$is defined as

$$
\operatorname{lct} (X, B, L) := \sup \{t \in \mathbb {R} \mid (X, B + t L) \text {is lc} \}.
$$

Now let A be an R-Cartier R-divisor. The R-linear system of A is

$$
| A | _ {\mathbb {R}} = \{L \geq 0 \mid L \sim_ {\mathbb {R}} A \}.
$$

We then define the lc threshold of$| A | _ { \mathbb { R } }$with respect to$( X , B )$(also called global lc threshold or α-invariant) as

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) := \inf \left\{\operatorname{lct} (X, B, L) \mid L \in | A | _ {\mathbb {R}} \right\}
$$

which coincides with

$$
\sup \{t \in \mathbb {R} \mid (X, B + t L) \text {   is   lc   for   every   } L \in | A | _ {\mathbb {R}} \}.
$$

One can similarly define the lc threshold of$| A |$and$| A | _ { \mathbb { Q } }$but we will not need them.

Due to connections with the notion of stability and existence of K¨ahler-Einstein metrics, lc thresholds of R-linear systems have attracted a lot of attention particularly when A is ample. An important special case is when X is Fano and$A = - K _ { X }$

Lc thresholds of anti-log canonical systems of Fano pairs. We were led to lc thresholds of Fano varieties for a quite diferent reason. The paper [5] reduces Theorem 1.1 to existence of a positive lower bound for lc thresholds of anti-canonical systems of certain Fano varieties which is guaranteed by our next result.

Theorem 1.6. Let d be a natural number and ǫ be a positive real number. Then there is a positive real number t depending only on d, ǫ satisfying the following. Assume

$( X , B )$is a projective ǫ-lc pair of dimension d, and

$A : = - ( K _ { X } + B )$is nef and big.

Then

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) \geq t.
$$

Although one may try to derive the theorem from 1.1 but we actually do the opposite, that is, we will use the theorem to prove 1.1 (see 2.15 below). The theorem was conjectured by Ambro [3] who proved it in the toric case. Jiang [19][18] proved it in dimension two. It is worth mentioning that they both try to relate lc thresholds to boundedness of Fano’s but our approach is entirely diferent.

The lc threshold of an R-linear system$| A | _ { \mathbb { R } }$is defined as an infimum of usual lc thresholds. Tian [42, Question 1] asked whether the infimum is a minimum when$A = - K _ { X }$and X is Fano. The question was reformulated and generalised to log Fano’s in [11, Conjecture 1.12]. The next result gives a positive answer when the lc threshold is at most 1.

Theorem 1.7. Let$( X , B )$be a projective klt pair such that$A : = - ( K _ { X } + B )$is nef and big. Assume that

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) \leq 1.
$$

Then there is$0 \le D \sim _ { \mathbb { R } }$A such that

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) = \operatorname{lct} (X, B, D).
$$

Moreover,$i f B$is a Q-boundary, then we can choose$D \sim _ { \mathbb { Q } } A$, hence in particular, the lc threshold is a rational number in this case.

The theorem is not used in the rest of the paper and its proof in the case

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) <   1
$$

relies on [13] but does not rely on the other results of this paper nor on the results of [5]. Ivan Cheltsov informed us that Shokurov has an unpublished proof of the theorem in dimension two.

Lc thresholds of R-linear systems with bounded degree. Next we treat lc thresholds associated with divisors on varieties, in a general setting. To obtain any useful boundedness result, one needs to impose certain boundedness conditions on the invariants of the divisor and the variety.

Theorem 1.8. Let$d , r$be natural numbers and ǫ be a positive real number. Then there is a positive real number t depending only on d, r, ǫ satisfying the following. Assume

$( X , B )$is a projective ǫ-lc pair of dimension$d ,$

• A is a very ample divisor on X with$A ^ { d } \leq r _ { i }$

$A - B$is pseudo-efective, and

$M \geq 0$is an R-Cartier R-divisor with A − M pseudo-efective.

Then

$$
\operatorname{lct} (X, B, | M | _ {\mathbb {R}}) \geq \operatorname{lct} (X, B, | A | _ {\mathbb {R}}) \geq t.
$$

This is one of the main ingredients of the proof of Theorem 1.6 but it is also interesting on its own. We explain briefly some of the assumptions of the theorem. The condition$A ^ { d } \leq r$ means that X belongs to a bounded family of varieties, actually, if we choose A general in its linear system, then$( X , A )$belongs to a bounded family of pairs. We can use the divisor A to measure how “large” other divisors are on X. Indeed, the pseudo-efectivity of$A - B$ and$A - M$, roughly speaking, say that the “degree” of B and M are bounded from above, that is,

$$
\deg_ {A} B := A ^ {d - 1} B \leq A ^ {d} \leq r \text { and } \deg_ {A} M := A ^ {d - 1} M \leq A ^ {d} \leq r.
$$

Without such boundedness assumptions, one would not find a positive lower bound for the lc threshold. For example, if$X = \mathbb { P } ^ { d }$, then one can easily find M with arbitrarily small lc threshold if the degree of M is allowed to be large enough. The bound on the degree of B is much more subtle.

Complements near a non-klt centre. We prove boundedness of certain “complements” near a non-klt centre on a projective pair. For the definition of complements in the global setting, see 2.12.

Theorem 1.9. Let d, p be natural numbers. Then there exists a natural number n depending only on d, p satisfying the following. Assume

$( X , B )$is a projective lc pair of dimension d,

• pB is integral,

• M is a semi-ample Cartier divisor on X defining a contraction f :$X  Z$2

• X is of Fano type over Z,

$M - ( K _ { X } + B )$is nef and big, and

• S is a non-klt centre of$( X , B )$with$M | _ { S } \equiv 0$

Then there is a Q-divisor$\Lambda \geq B$such that

$( X , \Lambda )$is lc over a neighbourhood of$z : = f ( S )$, and

$n ( K _ { X } + \Lambda ) \sim ( n + 2 ) M$

This is a key ingredient of the proof of Theorem 1.8. Note that$K _ { X } + \Lambda$is actually a relative n-complement of$K _ { X } + B$over a neighbourhood of z in the sense of [5, 2.18]. The important point here is that the complement is not an arbitrary one since Λ is somehow controlled globally by M as it satisfies the formula$n ( K _ { X } + \Lambda ) \sim ( n + 2 ) M$

We devote the rest of the introduction to rough sketches of the proofs of 1.1, 1.6, and 1.8.

Sketch of the proof of Theorem 1.1. We will assume Theorem 1.6 in dimension d. For simplicity we assume$B = 0 .$. The idea is to apply [5, Proposition 7.13], that is, 2.15 below. For this it is enough to show that there exist natural numbers m, v and a positive real number t, all depending only on$d , \epsilon ,$such that

$K _ { X }$has an m-complement,

$\vert - m K _ { X } \vert$defines a birational map,

$\operatorname { v o l } ( - K _ { X } ) \leq v .$and

• for any$0 \leq L \sim _ { \mathbb { R } } - K _ { X }$, the pair$( X , t L )$is klt.

The number m is given by [5, Theorems 1.2 and 1.7]. The number v is given by [5, Theorem 1.6] assuming 1.1 in lower dimension. The number t is given by Theorem 1.6. In turn we will see that 1.6 is reduced to the general theorem on boundedness of lc thresholds, that is, 1.8.

For reader’s convenience we also include some rough explanations for as to why the existence of$m , v , t$is enough to deduce boundedness of X.$\mathrm { A p p l y i n g }$[15], it is enough to show that$K _ { X }$has a klt n-complement for some bounded number$n \in \mathbb { N } .$By assumption, there is an lc m-complement$K _ { X } + B ^ { + }$. If X is exceptional, the latter complement is automatically klt, so we are done in this case. Here by X being exceptional we mean that $( X , L )$is klt for every$0 \leq L \sim _ { \mathbb { R } } - K _ { X }$

To treat the non-exceptional case the idea is to modify the complement$K _ { X } + B ^ { + }$into a klt one. We do this using birational boundedness. By induction we can assume that 1.1 holds in lower dimension, so X is birationally bounded by [5, Theorem 1.6]. In fact it turns out that$( X , B ^ { + } )$is log birationally bounded, that${ \mathrm { i s } } ,$there exists a log smooth projective pair$( V , \Sigma )$belonging to a bounded family of pairs and there exists a birational map$V  X$such that Σ contains the exceptional divisors of$V  X$and the support of the birational transform of$B ^ { + }$

Next we pull back$K _ { X } + B ^ { + }$to a high resolution of X and push it down to V and denote it by$K _ { V } + B _ { V } ^ { + }$. Then$( V , B _ { V } ^ { + } )$is sub-lc and$m ( K _ { V } + B _ { V } ^ { + } ) \sim 0$. Now Supp$B _ { V } ^ { + }$is contained in$\Sigma$. So we can use the boundedness of$( V , \Sigma )$to perturb the coeficients of$B _ { V } ^ { + }$. More precisely, perhaps after replacing$m ,$, there is$\Delta _ { V } \sim _ { \mathbb { Q } } B _ { V } ^ { + }$such that$( V , \Delta _ { V } )$is sub-klt and m$\iota ( K _ { V } + \Delta _ { V } ) \sim 0$. Pulling back$K _ { V } + \Delta _ { V }$to$X$and denoting it by$K _ { X } + \Delta$we get a sub-klt pair$( X , \Delta )$with$m ( K _ { X } + \Delta ) \sim 0$

Now a serious issue is that$\Delta$may not be efective, so$K _ { X } + \Delta$is not necessarily an m-complement. In fact it is by no means clear that the coeficients of$\Delta$are even bounded from below. However, it is not hard to see that existence of t remedies the situation: indeed, if$0 \leq L \sim _ { \mathbb { R } } - K _ { X }$, then the coeficients of$L$are bounded from above. This implies that the coeficients of$\Delta$are bounded from below, by construction of$\Delta$. The rest of the argument which modifies$\Delta$to get a klt n-complement for some bounded n is an easy application of the results of [5] on complements.

Sketch of the proof of Theorem 1.6. We will assume Theorem 1.8 in dimension d and assume Theorem 1.1 in lower dimension. Let$( X , B )$and$A = - ( K _ { X } + B )$be as in Theorem 1.6 in dimension d. Replacing X with can assume it is Q-factorial. Pick$\epsilon ^ { \prime } \in ( 0 , \epsilon )$and pick $L \in | A | _ { \mathbb { R } }$. Let$s$be the largest number such that$( X , B + s L )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$. It is enough to show s is bounded from below away from zero.

There is a prime divisor$T$over X with

$$
a (T, X, B + s L) = \epsilon^ {\prime}.
$$

If$T$is not exceptional over X, then we let$\phi \colon Y  X$be the identity morphism but if$T$ is exceptional over$X$, then we let$\phi \colon Y  X$be the extremal birational contraction which extracts T. Let${ \cal L } _ { Y } = \phi ^ { * } { \cal L }$. One shows$\mu _ { T } s L _ { Y } \geq \epsilon - \epsilon ^ { \prime }$, hence that it is enough to show that$\mu _ { T } L _ { Y }$is bounded from above.

Running an MMP on −T, restricting to the general fibres of the resulting Mori fibre space, and applying induction on dimension reduces the problem to the situation in which $X$is an ǫ-lc Q-factorial Fano variety with Picard number one on which we want to show that$\mu _ { T } L$is bounded from above for any$L \in \mathsf { \Omega } | \mathrm { ~ - ~ } K _ { X } | _ { \mathbb { R } }$and any prime divisor$T$on$X$

Using the Picard number one property, we can replace L and assume Supp$L = T$, hence we can assume$L = u T$with$u = \mu _ { T } L$

Applying [5, Theorems 1.2, 1.6, 1.7] and Theorem 1.1 in lower dimension we find a bounded number$n \in \mathbb N$such that$K _ { X }$has an n-complement$K _ { X } + \Omega , \lvert - n K _ { X } \rvert$defines a birational map and that$\operatorname { v o l } ( - K _ { X } )$is bounded from above. In particular, we deduce that $( X , \Omega )$is log birationally bounded. So there is a projective log smooth pair$( V , \Sigma )$belonging to a bounded family and a birational map$X \  \ V$so that Σ is reduced whose support contains the exceptional divisors of$V  X$and the birational transform of Supp Ω.

Pull back$K _ { X } + B , L$to a high resolution of X and then push down to V and denote the resulting divisors by$K _ { V } + B _ { V } , M$. The main idea of the rest of the proof is to find a boundary$\Delta$by taking an appropriate average between$B _ { V }$and Σ so that

$( V , \Delta )$is$\epsilon ^ { \prime \prime } { - } \mathrm { l c }$for some fixed$\epsilon ^ { \prime \prime } > 0$2

$\begin{array} { r } { ( V , \Delta + \frac { 1 } { u } M ) } \end{array}$is not klt, and

$^ { 6 6 } \mathrm { d e g r e e s } ^ { 5 5 }$of ∆ and M are bounded with respect to some very ample divisor.

Applying Theorem 1.8 gives a positive lower bound for$\textstyle { \frac { 1 } { u } }$, hence an upper bound for u.

Sketch of the proof of Theorem 1.8. It is easy to see that

$$
\operatorname{lct} (X, B, | M | _ {\mathbb {R}}) \geq \operatorname{lct} (X, B, | A | _ {\mathbb {R}}),
$$

so we only need to find a positive lower bound for lct$( X , B , | A | _ { \mathbb { R } } )$. Pick$0 \leq N \sim _ { \mathbb { R } } A$. Let s be the largest number such that$( X , B + s N )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$where$\epsilon ^ { \prime } = \frac { \epsilon } { 2 }$. It is enough to show s is bounded from below away from zero. There is a prime divisor$\overline { T }$on birational models of X with log discrepancy

$$
a (T, X, \Delta := B + s N) = \epsilon^ {\prime}.
$$

It is enough to show the multiplicity of$T$in$\phi ^ { * } N$is bounded from above on some resolution $\phi \colon V \to X$on which$T$is a divisor. We can assume the image of$T$on X is a closed point x otherwise we can cut by hyperplane sections and apply induction on dimension. Since

$$
a (T, X, \Delta) = \epsilon^ {\prime} <   1,
$$

there is a birational contraction$Y  X$extracting T but no other divisors. Moreover, we can assume that −$- ( K _ { Y } + T )$is ample over$X$, and using ACC for lc thresholds [13] we can assume$( Y , T )$is lc.

The next step is to do a “toroidalisation”. A key ingredient here is provided by the theory of complements, that is, Theorem 1.9. Using ampleness of$- ( K _ { Y } + T )$over$X .$, we can find $\Lambda _ { Y }$such that$( Y , \Lambda _ { Y } )$is lc near$T$and$n ( K _ { Y } + \Lambda _ { Y } ) \sim 0 / X$for a bounded$n \in \mathbb N$. Crucial point: if Λ is the pushdown of$\Lambda _ { Y }$, then after some delicate work we can assume$A - \Lambda$is ample. In particular, the log discrepancy$a ( T , X , \Lambda ) = 0$and$( X , { \mathrm { S u p p } } \Lambda )$is log bounded. Using resolution of singularities we can assume$( X , \Lambda )$is log smooth and Λ is reduced. The advantage of having Λ is that now$T$can be obtained by a sequence of blowups, toroidal with respect to$( X , \Lambda )$. The first step of this sequence is just the blowup of x. One argues that it is enough to bound the number of these blowups.

We can discard any component of$\Lambda$not passing through$x ,$say$\Lambda = S _ { 1 } + \cdot \cdot \cdot + S _ { d }$. A careful analysis of$Y  X$allows us to modify the situation so that$\operatorname { S u p p } \Delta$does not contain any stratum of$( X , \Lambda )$apart from x. This is one of the dificult steps of the proof.

The next step is to do a “torification”. Since$( X , \Lambda )$is log smooth and log bounded, we can find a surjective finite morphism$X  \mathbb { P } ^ { d }$such that it maps x to the origin

$$
z = (1: 0: \dots : 0),
$$

and it maps$S _ { i }$onto$H _ { i }$where$H _ { 1 } , \ldots , H _ { d }$are the coordinate hyperplanes passing through z. Since Supp ∆ does not contain any stratum of$( X , \Lambda )$apart from$x ,$it is not hard to reduce the problem to a similar problem on$\mathbb { P } ^ { d }$. From now on we assume$X = \mathbb { P } ^ { d }$and that $S _ { i }$are the coordinate hyperplanes. The point of this reduction is that now$( X , \Lambda )$is not only toroidal but actually toric, and$- ( K _ { X } + \Lambda )$is ample. In particular, we can modify$\Delta$ so that$K _ { X } + \Delta$is numerically trivial.

Let$W  X$be the sequence of blowups which obtains$T ,$. Since the blowups are toric, W is a toric variety. If$Y  X$is the birational morphism contracting$T$only, as before, then $Y$is also a toric variety. Moreover, if$K _ { Y } + \Delta _ { Y }$is the pullback of$K _ { X } + \Delta$, then$( Y , \Delta _ { Y } )$ is$\epsilon ^ { \prime } -$lc and$K _ { Y } + \Delta _ { Y }$is numerically trivial. Running MMP on$- K _ { Y }$we get another toric variety$Y ^ { \prime }$which is Fano and$\epsilon ^ { \prime } { - } \mathrm { l c } .$. By the toric version of 1.1 [9],$Y ^ { \prime }$belongs to a bounded family. From this we can produce a klt m-complement$K _ { Y ^ { \prime } } + \Omega _ { Y ^ { \prime } }$for some bounded$m \in \mathbb { N }$ which induces a klt m-complement$K _ { Y } + \Omega _ { Y }$which in turn gives a klt m-complement $K _ { X } + \Omega$. In particular,$( X , \Omega )$belongs to a bounded family as$m ( K _ { X } + \Omega ) \sim 0$. This implies that$( X , \Omega + u \Lambda )$is klt for some$u > 0$bounded from below away from zero. Finally an easy calculation shows that the multiplicity of$T$in the pullback of$\Lambda$on W is bounded from above which in turn implies the number of blowups in$W  X$is bounded as required.

Acknowledgements. I would like to thank Florin Ambro, Ivan Cheltsov, Christopher Hacon, Jingjun Han, Yujiro Kawamata, Mihai Pˇaun, Vyacheslav Shokurov, and Yanning Xu as well as the referees for their valuable comments. Thanks to Jungkai A. Chen and the National Taiwan University ofice of the National Center for Theoretical Sciences for hosting a workshop on this paper and [5] and thanks to the participants for their comments. It is likely that I am forgetting other people who have given me helpful comments on the paper in the last few years: I would like to thank those as well.

## 2. Preliminaries

All the varieties in this paper are defined over an algebraically closed field k of characteristic zero unless stated otherwise.

2.1. Divisors. Let X be a normal variety and$D = \sum d _ { i } D _ { i }$be an R-divisor where$D _ { i }$are the distinct irreducible components of D. We sometimes denote the coeficient$d _ { i }$by$\mu _ { D _ { i } } D$ Let Y also be a normal variety and$\phi \colon X \to Y$be a birational map whose inverse does not contract any divisor. We often denote$\phi _ { * } D$by$D _ { Y }$

Now let X be a normal projective variety of dimension d and$A , D$be R-Cartier Rdivisors. We define the degree of D with respect to A to be the intersection number $\deg _ { A } D : = A ^ { d - 1 } D$when$d > 1$and$\deg _ { A } D : = \deg D { \mathrm { ~ i f ~ } } d = 1$where deg D denotes the usual degree of divisors on curves. If$A - D$is pseudo-efective, then one easily sees that $\deg _ { A } D \leq \deg _ { A } A$

We can similarly define$\deg _ { A } D$even if D is not R-Cartier, for example, when A is an ample Q-divisor because in this case we can express$A ^ { d - 1 }$as a 1-cycle in the smooth locus of$X$.

The volume of an R-divisor D on a normal projective variety X of dimension d is defined as

$$
\operatorname{vol} (D) = \limsup _ {m \to \infty} \frac {h ^ {0} (\lfloor m D \rfloor)}{m ^ {d} / d !}.
$$

2.2. Pairs and singularities. A sub-pair$( X , B )$consists of a normal quasi-projective variety X and an R-divisor B with coeficients in$( - \infty , 1 ]$such that$K _ { X } + B$is R-Cartier. If$B \geq 0$, we call B a boundary and call$( X , B )$a pair.

Let φ:$W  X$be a log resolution of a sub-pair$( X , B )$. Let$K _ { W } + B _ { W }$be the pullback of $K _ { X } + B$. The log discrepancy of a prime divisor D on W with respect to$( X , B )$is defined as

$$
a (D, X, B) := 1 - \mu_ {D} B _ {W}.
$$

We say$( X , B ) { \mathrm { ~ i s ~ } } s u b { - } l c { \mathrm { ~ ( r e s p . ~ } } s u b { - } k l t { ) }  ( { \mathrm { r e s p . ~ } } s u b { - } k l { - } l c { \mathrm { ) ~ i f ~ } } a ( D , X , B ) { \mathrm { ~ i s \geq 0 ~ ( r e s p . ~ } } > 0 { \mathrm { ) ( r e s p . ~ } } s u b { - } l c { \mathrm { ) ~ i f ~ } } a ( D , X , B ) { \mathrm { ~ i s \geq 0 ~ ( r e s p . ~ } } s { - } 0 { \mathrm { ) ( r e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { - } l c { \mathrm { ) ( l e s p . ~ } } s u b { ) }$. $\geq \epsilon )$for every D. This means that every coeficient of$B _ { W } ~ { \mathrm { i s } } \leq 1 ~ ( { \mathrm { r e s p . } } ~ < 1 ) ( { \mathrm { r e s p . } } ~ \leq 1 - \epsilon )$ If$( X , B )$is a pair, we remove the sub and just say it is lc (resp. klt)(resp. ǫ-lc). Note that since$a ( D , X , B ) = 1$for most prime divisors, we necessarily have$\epsilon \leq 1$

Let (X, B) be a pair. An non-klt place of$( X , B )$is a prime divisor D over X, that${ \mathrm { i s } } ,$on birational models of X such that$a ( D , X , B ) \leq 0$. A non-klt centre is the image on X of a non-klt place. When (X, B) is lc, a non-klt place and a non-klt centre are also sometimes referred to as an lc place and an lc centre, respectively.

A log smooth pair is a pair (X, B) where X is smooth and Supp B has simple normal crossing singularities. Assume (X, B) is log smooth and assume$\begin{array} { r } { B = \sum _ { 1 } ^ { r } B _ { i } } \end{array}$is reduced where$B _ { i }$are the irreducible components. A stratum of$( X , B )$is an irreducible component of$\cap _ { i \in I } B _ { i }$for some$I \subseteq \{ 1 , \ldots , r \}$. Since B is reduced, a stratum is nothing but an lc centre of (X, B) or X itself.

Lemma 2.3.$H f \left( X , B \right)$and$( X , B ^ { \prime } )$are sub-pairs and$\Delta = t B + ( 1 - t ) B ^ { \prime }$for some real number$t \in [ 0 , 1 ]$, then

$$
a (D, X, \Delta) = t a (D, X, B) + (1 - t) a (D, X, B ^ {\prime})
$$

for any prime divisor D over X. In particular,$i f \left( X , B \right)$is sub-ǫ-lc and$( X , B ^ { \prime } )$is$s u b \mathrm { - } \epsilon ^ { \prime } \mathrm { - } l c ,$ then$( X , \Delta )$is$s u b \ – ( t \epsilon + ( 1 - t ) \epsilon ^ { \prime } ) – l c$

We leave the proof to the reader.

2.4. Fano pairs. A pair (X, B) is called Fano (resp. weak Fano) if it is lc and −$( K _ { X } + B )$ is ample (resp. nef and big). When$B = 0$we just say X is Fano (resp. weak Fano). A variety X is of Fano type if (X, B) is klt weak Fano for some B. By [7], a Fano type variety is a Mori dream space, so we can run an MMP on any R-Cartier R-divisor on X and it terminates.

2.5. Minimal models, Mori fibre spaces, and MMP. Let$X  Z$be a projective morphism of normal varieties and D be an R-Cartier R-divisor on X. Let Y be a normal variety projective over Z and$\phi \colon X \ {  } \ Y / Z$be a birational map whose inverse does not contract any divisor. Assume$D _ { Y } : = \phi _ { * } D$is also R-Cartier and that there is a common resolution $g \colon W \to X$and$h \colon W \to Y$such that$E : = g ^ { * } D - h ^ { * } D _ { Y }$is efective and exceptional/Y, and Supp$g _ { * } E$contains all the exceptional divisors of φ.

Under the above assumptions we call Y a minimal model of D over Z if D is nef/Z. On the other hand, we call Y a Mori fibre space of D over Z if there is an extremal contraction $Y  T / Z$with$- D _ { Y }$ample/T and dim$Y > \dim T$

If one can run a minimal model program (MMP) on D over Z which terminates with a model$Y$, then Y is either a minimal model or a Mori fibre space of D over Z. If X is a Mori dream space, eg if X is of Fano type over Z, then such an MMP always exists by [7].

2.6. Plt pairs. In this subsection we construct plt models associated with certain lc pairs. This is similar to the construction of plt blowups [36] (also see [38, Definition 3.5] and [44, Lemma 1]).

Lemma 2.7. Assume$( X , B )$is an lc pair. Assume that$( X , B )$is not klt but$( X , C )$is klt for some boundary C. Then there exist a prime divisor T over X and a projective birational morphism$\phi \colon Y  X$such that

• either$\phi$is small or it contracts$T$but no other divisors,

$( Y , T ) \ i s \ p l t ,$

$- ( K _ { Y } + T )$is ample over$X$, and

$a ( T , X , B ) = 0 .$

Proof. Assume that there is a boundary Γ and a prime divisor T over X such that

$$
a (T, X, B) = a (T, X, \Gamma) = 0
$$

and such that$( X , \Gamma )$has no lc place other than$T .$. Replacing C with$( 1 - t ) B + t C$for a suficiently small real number$t > 0 .$, we can assume that$a ( T , X , C ) \leq 1$, by Lemma 2.3. If$T$is not exceptional over X, let$Y  X$be a small Q-factorialisation. But if T is exceptional over$X ,$, let$Y  X$be the birational contraction from Q-factorial Y which extracts$T$but no other divisor. Let$K _ { Y } + C _ { Y }$be the pullback of$K _ { X } + C$. Then$( Y , C _ { Y } )$ is klt.

Run an MMP on$- ( K _ { Y } + T )$over X and let$Y ^ { \prime }$be the resulting model; we can run such an MMP as$Y$is of Fano type over X. Next let$Y ^ { \prime }  Y ^ { \prime \prime } / X$be the contraction defined by $- ( K _ { Y ^ { \prime } } + T ^ { \prime } )$. It turns out that$T$is not contracted over$Y ^ { \prime \prime }$: indeed, otherwise$( Y ^ { \prime \prime } , 0 )$would be lc but not klt because$K _ { Y ^ { \prime } } + T ^ { \prime } \sim _ { \mathbb { O } } 0 / Y ^ { \prime \prime }$, and this contradicts the fact that$( Y ^ { \prime \prime } , C _ { Y ^ { \prime \prime } } )$is klt. Now replace$Y , T$with$Y ^ { \prime \prime } , T ^ { \prime \prime }$where$T ^ { \prime \prime }$is the pushdown of$T$to$Y ^ { \prime \prime }$. By construction, $- ( K _ { Y } + T )$is ample over X. Moreover, if$K _ { Y } + \Gamma _ { Y }$is the pullback of$K _ { X } + \Gamma$, then$( Y , \Gamma _ { Y } )$ is plt because$a ( D , Y , \Gamma _ { Y } ) > 0$for every prime divisor D over X other than T. So$( Y , T )$is plt and$Y  X$is the desired morphism.

We will find$\Gamma , T$as in the first paragraph. Let$\psi \colon W \to X$be a log resolution of $( X , B + C )$and write

$$
K _ {W} + B _ {W} = \psi^ {*} (K _ {X} + B) \text { and } K _ {W} + C _ {W} = \psi^ {*} (K _ {X} + C).
$$

Write

$$
B _ {W} - C _ {W} \sim_ {\mathbb {R}} H _ {W} + G _ {W} / X
$$

where$H _ { W } \geq 0$is ample over X and$G _ { W } \geq 0$. Let$H , G$be the pushdowns of$H _ { W } , G _ { W }$ to$X$. Note that$H _ { W } + G _ { W } \sim _ { \mathbb { R } } 0 / X$, so$H + G$is R-Cartier. Replacing$\psi$with a higher resolution and replacing$H _ { W } , G _ { W }$appropriately we can assume that$\psi$is a log resolution of

$$
(X, B + C + H + G).
$$

Moreover, replacing C with$( 1 - t ) B + t C$for a suficiently small real number$t > 0$we can assume that the coeficients of$B _ { W } - C _ { W }$are suficiently close to 0.

Let E be the sum of the components of$B _ { W }$with coeficient 1. Since$( X , B )$is not klt, $E \neq 0$. First assume that E and$G _ { W }$have no common component. Then we can pick a small real number$a > 0$and find

$$
\Gamma_ {W} \sim_ {\mathbb {R}} B _ {W} + a H _ {W} + a G _ {W}
$$

so that$( W , \Gamma _ { W } )$is sub-lc,$( W , \mathrm { S u p p } \Gamma _ { W } )$is log smooth,$\mu _ { T } \Gamma _ { W } = 1$for some component $T$of$E$, all the other coeficients of$\Gamma _ { W }$are$< ~ 1$, and$\Gamma : = \psi _ { * } \Gamma _ { W }$is efective. Since $K _ { Y } + \Gamma _ { Y } \sim _ { \mathbb { R } } 0 / X$, the pair$( X , \Gamma )$is lc with the unique lc place$T .$. So we are done in this case.

Now assume$G _ { W }$and E have common components. Recall that the coeficient$\mu _ { T } C _ { W }$of each component$T$of$E$is suficiently close to 1. Let$a > 0$be the largest real number such that$( W , C _ { W } + a G _ { W } )$is sub-lc. Then we can assume that each component of$C _ { W } + a G _ { W }$ with coeficient 1 is a component of$E .$Thus we can find

$$
\Gamma_ {W} \sim_ {\mathbb {R}} C _ {W} + a H _ {W} + a G _ {W}
$$

so that$( W , \Gamma _ { W } )$is sub-lc,$( W , \mathrm { S u p p } \Gamma _ { W } )$is log smooth,$\mu _ { T } \Gamma _ { W } = 1$for some component $T$of$E$, all the other coeficients of$\Gamma _ { W }$are$< ~ 1$, and$\Gamma : = \psi _ { * } \Gamma _ { W }$is efective. Since $K _ { Y } + \Gamma _ { Y } \sim _ { \mathbb { R } } 0 / X$, the pair$( X , \Gamma )$is lc with the unique lc place$T$. So we are again done.

2.8. Bounded families of pairs. We say a set$\mathcal { Q }$of normal projective varieties is birationally bounded (resp. bounded) if there exist finitely many projective morphisms$V ^ { i }  T ^ { i }$ of varieties such that for each$X \in \mathcal { Q }$there exist an i, a closed point$t \in T ^ { i }$, and a birational isomorphism (resp. isomorphism) φ :$V _ { t } ^ { i } \ - + \ X$where$V _ { t } ^ { i }$is the fibre of$V ^ { i }  T ^ { i }$over$t .$

Next we will define boundedness for couples. A couple$( X , S )$consists of a normal projective variety X and a divisor S on X whose coeficients are all equal to 1, i.e. S is a reduced divisor. We use the term couple instead of pair because$K _ { X } + S$is not assumed to be Q-Cartier and$( X , S )$is not assumed to have good singularities.

We say that a set P of couples is birationally bounded if there exist finitely many projective morphisms$V ^ { i }  T ^ { i }$of varieties and reduced divisors$C ^ { i }$on$V ^ { i }$such that for each $( X , S ) \in { \mathcal { P } }$there exist an$i ,$a closed point$t \in T ^ { i }$, and a birational isomorphism$\phi \colon V _ { t } ^ { i } \ \mathrm { ~ -- \gamma } X$ such that$( V _ { t } ^ { i } , C _ { t } ^ { i } )$is a couple and$E \leq C _ { t } ^ { i }$where$V _ { t } ^ { i }$and$C _ { t } ^ { i }$are the fibres over t of the morphisms$V ^ { i }  T ^ { i }$and$C ^ { i }  T ^ { i }$, respectively, and$E$is the sum of the birational transform of S and the reduced exceptional divisor of$\phi .$. We say$\mathcal { P }$is bounded if we can choose$\phi$to be an isomorphism.

A set R of projective pairs$( X , B )$is said to be log birationally bounded (resp. log bounded) if the set of the corresponding couples (X, Supp B) is birationally bounded (resp. bounded). Note that this does not put any condition on the coeficients of$B _ { ; }$eg we are not requiring the coeficients of B to be in a finite set.

2.9. Efective birationality and birational boundedness. In the next few subsections, we recall some of the main results of [5] which are needed in this paper.

Theorem 2.10 ([5, Theorem 1.2]). Let d be a natural number and ǫ be a positive real number. Then there is a natural number m depending only on d and ǫ such that if X is any ǫ-lc weak Fano variety of dimension$d ,$then$\vert - m K _ { X } \vert$defines a birational map.

Theorem 2.11 ([5, Theorem 1.6]). Let d be a natural number and ǫ be a positive real number. Assume Theorem 1.1 holds in dimension d−1. Then there is a number v depending only on d and ǫ such that if X is an ǫ-lc weak Fano variety of dimension d, then the volume $\mathrm { v o l } ( - K _ { X } ) \le v$. In particular, such X are birationally bounded.

In fact the proof of the theorem shows that (X, 0) is log bounded.

2.12. Complements. Let$( X , B )$be a projective pair. Let$T = \lfloor B \rfloor$and$\Delta = B - T$. An n-complement of$K _ { X } + B$is of the form$K _ { X } + B ^ { + }$where

$( X , B ^ { + } )$is lc,

$n ( K _ { X } + B ^ { + } ) \sim 0$, and

$n B ^ { + } \geq n T + \lfloor ( n + 1 ) \Delta \rfloor$

Theorem 2.13 ([5, Theorem 1.7]). Let d be a natural number and$\Re \subset [ 0 , 1 ]$be a finite set of rational numbers. Then there exists a natural number n depending only on d and R satisfying the following. Assume$( X , B )$is a projective pair such that

$( X , B )$is lc of dimension d,

$B \in \Phi ( \Re )$, that is, the coeficients of B are in$\Phi ( { \mathfrak { R } } )$，

• X is of Fano type, and

$- ( K _ { X } + B )$is nef.

Then there is an n-complement$K _ { X } + B ^ { + }$of$K _ { X } + B$such that$B ^ { + } \geq B$. Moreover, the complement is also an mn-complement for any$m \in \mathbb { N }$

In the theorem

$$
\Phi (\mathfrak {R}) := \left\{1 - \frac {r}{m} \mid r \in \mathfrak {R}, m \in \mathbb {N} \right\}.
$$

2.14. From bounds on lc thresholds to boundedness of varieties. The following result connects lc thresholds and boundedness of Fano varieties, and it is one of the main ingredients of the proof of Theorem 1.1.

Theorem 2.15 ([5, Proposition 7.13]). Let d, m, v be natural numbers and let$t _ { l }$be a sequence of positive real numbers. Let P be the set of projective varieties X such that

• X is a klt weak Fano variety of dimension$d ,$

$K _ { X }$has an m-complement,

$\vert - m K _ { X } \vert$defines a birational map,

$\mathrm { v o l } ( - K _ { X } ) \le v ,$and

• for any$l \in \mathbb N$and any$L \in | - l K _ { X } |$, the pair$( X , t _ { l } L )$is klt.

Then P is a bounded family.

Assuming Theorem 1.1 in lower dimension, Theorems 2.10, 2.11, and 2.13 show that all the assumptions of 2.15 are satisfied for X as in 1.1 in dimension d (when$B = 0 )$except the last assumption. We will use Theorem 1.6 to show that this last assumption is also satisfied.

The theorem also has applications to boundedness of K-semistable Fano varieties [17, Theorem 1.1].

2.16. Sequences of blowups. We discuss some elementary aspects of blowups.

(1) Let X be a smooth variety of dimension$\geq 2$and let

$$
\dots \rightarrow X _ {i + 1} \rightarrow X _ {i} \rightarrow \dots \rightarrow X _ {0} = X
$$

be a (finite or infinite) sequence of smooth blowups, that is, each$X _ { i + 1 }  X _ { i }$is the blowup along a smooth subvariety$C _ { i }$of codimension$\geq 2$. If the sequence is finite, say$X _ { p }  X _ { p - 1 }$ is the last blowup, the length of the sequence is$p .$We denote the exceptional divisor of $X _ { i + 1 }  X _ { i }$by$E _ { i + 1 }$

(2) Let Λ be a reduced divisor such that$( X , \Lambda )$is log smooth. We say a sequence as in (1) is toroidal with respect to$( X , \Lambda )$, if for each i, the centre$C _ { i }$is a stratum of$( X _ { i } , \Lambda _ { i } )$ where$K _ { X _ { i } } + \Lambda _ { i }$is the pullback of$K _ { X } + \Lambda$(cf. [24]). This is equivalent to saying that the exceptional divisor of each blowup in the sequence is an lc place of$( X , \Lambda )$

Lemma 2.17. Under the above notation, assume we have a finite sequence of smooth blowups of length$p ,$toroidal with respect to$( X , \Lambda )$, and let

$$
\phi \colon X _ {p} \to X _ {0} = X
$$

be the induced morphism. Suppose$C _ { i } \subset E _ { i }$for each$0 < i < p$. Then$\mu _ { E _ { p } } \phi ^ { * } \Lambda \geq p + 1$

Proof. If$0 \leq i < p ,$then$C _ { i }$is contained in at least two components of$\Lambda _ { i }$because$C _ { i }$is an lc centre of$( X _ { i } , \Lambda _ { i } )$of codimension$\geq 2$. When$i > 0 ,$, one of these components is$E _ { i }$ by assumption. Let$\phi _ { i }$denote$X _ { i }  X _ { 0 }$. Then by the equality$\Lambda _ { i } = \mathrm { S u p p } \phi _ { i } ^ { * } \Lambda$and by induction on i we have

$$
\mu_ {E _ {i + 1}} \phi_ {i + 1} ^ {*} \Lambda \geq \mu_ {E _ {i}} \phi_ {i} ^ {*} \Lambda + 1 \geq i + 2.
$$

(3) Consider a sequence of blowups as in (1) (so this is not necessarily toroidal). Let $T$be a prime divisor over$X$, that is, on birational models of$X$. Assume that for each $i , C _ { i }$is the centre of$T$on$X _ { i }$. We then call the sequence a sequence of centre blowups associated to$T .$By [28, Lemma 2.45], such a sequence cannot be infinite, that is, after finitely many centre blowups,$T$is obtained, i.e. there is$p$such that$T$is the exceptional divisor of$X _ { p }  X _ { p - 1 }$(here we think of$T$birationally; if$T$is fixed on some model, then we should say the exceptional divisor is the birational transform of T). In this case, we say $T$is obtained by the sequence of centre blowups$X _ { p }  X _ { p - 1 }  \cdots  X _ { 0 } = X$

2.18. Analytic pairs and analytic neighbourhoods of algebraic singularities. For convenience we will recall certain analytic notions shortly. We will use these mainly to compare analytic neighbourhoods of algebraic singularities and this involves only elementary aspects of the analytic theory. Strictly speaking we can replace these by purely algebraic constructions, eg formal varieties and formal neighbourhoods, but we prefer the analytic language as it is more straightforward. When we have an algebraic object A defined over C, eg a variety, a morphism, etc, we denote the associated analytic object by$A ^ { \mathrm { a n } }$

(1) An analytic pair$( U , G )$consists of a normal complex analytic variety U and an Rdivisor$G$with finitely many components and with coeficients in [0, 1] such that$K _ { U } + G$ is R-Cartier. Log discrepancies and notions of lc, klt, ǫ-lc singularities can be defined for such pairs just as in 2.2 using log resolutions. In this paper, we will only need analytic pairs (U, G) which are derived from algebraic pairs with U being smooth.

Two analytic pairs$( U , G )$and$( U ^ { \prime } , G ^ { \prime } )$are analytically isomorphic if there is an analytic isomorphism, that is, a biholomorphic map$\nu \colon U \to U ^ { \prime }$such that$\nu _ { * } G = G ^ { \prime }$

(2) Let (X, B) be an algebraic pair over C (that is, a pair as in 2.2), let$x \in X$be a closed point, and let$U$be an analytic neighbourhood of x in the associated analytic variety$X ^ { \mathrm { a n } }$. Take a log resolution$\phi \colon W \to X$and let V be the inverse image of$U$under $\phi ^ { \mathrm { a n } } \colon W ^ { \mathrm { a n } } \to X ^ { \mathrm { a n } }$. Then$\phi ^ { \mathrm { a n } } | _ { V }$is an analytic log resolution of$( U , B ^ { \mathrm { a n } } | _ { U } )$. In particular, if $( U , B ^ { \mathrm { a n } } | _ { U } )$is ǫ-lc in the analytic sense, then$( X , B )$is ǫ-lc in some algebraic neighbourhood of x. Conversely, it is clear that if$( X , B )$is ǫ-lc in some algebraic neighbourhood of$x ,$, then we can choose U so that$( U , B ^ { \mathrm { a n } } | _ { U } )$is ǫ-lc in the analytic sense.

(3) Now let$( X , B )$and$( X ^ { \prime } , B ^ { \prime } )$be algebraic pairs over$\mathbb { C } ,$let$x \in X$and$x ^ { \prime } \in X ^ { \prime }$ be closed points, and let U and$U ^ { \prime }$be analytic neighbourhoods of x and$x ^ { \prime } ,$, respectively. Assume that$( U , B ^ { \mathrm { a n } } | _ { U } )$and$( U ^ { \prime } , B ^ { \prime \mathrm { a n } } | _ { U ^ { \prime } } )$are analytically isomorphic. Then$( X , B )$is$\epsilon \mathrm { - }$ lc in some algebraic neighbourhood of x if and only if$( X ^ { \prime } , B ^ { \prime } )$is ǫ-lc in some algebraic neighbourhood of$x ^ { \prime }$. Note that it may well happen that$( X , B )$and$( X ^ { \prime } , B ^ { \prime } )$are not algebraically isomorphic in any algebraic neighbourhoods of$x$and$x ^ { \prime }$. For example, the two pairs$\left( \mathbb { P } ^ { 2 } , B \right)$and$\left( \mathbb { P } ^ { 2 } , B ^ { \prime } \right)$have isomorphic analytic neighbourhoods where B is an irreducible curve with a node at x but$B ^ { \prime }$is the union of two lines intersecting at$x ^ { \prime }$.

2.19. Etale morphisms. <sup>´</sup> We look at singularities of images of a pair under a finite morphism which is ´etale at some point.

Lemma 2.20. Let$\left( { \cal X } , { \cal B } = \sum b _ { j } B _ { j } \right)$be a pair over$\mathbb { C } , \pi \colon X  Z$be a finite morphism, $x \in X$a closed point, and$z = \pi ( x )$. Assume

• X and Z are smooth near x and z, respectively,

• π is ´etale at x,

• Supp B does not contain any point of$\pi ^ { - 1 } \{ z \}$except possibly x, and

$\begin{array} { r } { C : = \pi ( B ) : = \sum b _ { j } \pi ( B _ { j } ) } \end{array}$

Then$( X , B )$is ǫ-lc near x if and only if$( Z , C )$is ǫ-lc near z. More precisely, there exist analytic neighbourhoods U and V of x and z, respectively, such that$\pi ^ { \mathrm { a n } } | _ { U }$induces an analytic isomorphism between$( U , B ^ { \mathrm { a n } } | _ { U } )$and$( V , C ^ { \mathrm { a n } } | _ { V } )$

We leave the proof of this lemma and the next lemma to the reader.

Note that in the previous lemma, C may not even be a boundary away from$z ,$that is, it may have components not passing through z but with coeficients larger than 1.

The next lemma is useful for showing that a morphism is ´etale at a point.

Lemma 2.21. Let$\pi \colon X \to Z$be a finite morphism between varieties of dimension$d , x \in X$ a closed point, and$z = \pi ( x )$. Assume X and Z are smooth at x and z, respectively. Assume $t _ { 1 } , \ldots , t _ { d }$are local parameters at z and that$\pi ^ { * } t _ { 1 } , \ldots , \pi ^ { * } t _ { d }$are local parameters at x. Then π is ´etale at x.

2.22. Toric varieties and toric MMP. We will reduce Theorem 1.8 to the case when $X = \mathbb { P } ^ { d }$. To deal with this case we need some elementary toric geometry. All we need can be found in [12]. Let X be a (normal) Q-factorial projective toric variety. Then X is a Mori dream space, meaning we can run an MMP on any Q-divisor D which terminates with a minimal model or a Mori fibre space of D. Moreover, the MMP is toric, that is, all the contractions and varieties in the process are toric. If we have a projective toric morphism $X  Z$to a toric variety, then we can run an MMP on D over Z which terminates with a minimal model or a Mori fibre space of D over Z. See [12, §15.5] for proofs.

Now let Λ be the sum of some of the torus-invariant divisors on a projective toric variety X, and assume$( X , \Lambda )$is log smooth. Let$Y  X$be a sequence of blowups toroidal with respect to$( X , \Lambda )$. Then Y is also a toric variety as each blowup in the process is a blowup along an orbit closure.

2.23. Bounded small modifications. The following lemma is useful for reducing problems to the case when the canonical divisor is Q-Cartier.

Lemma 2.24. Let d, r be natural numbers and ǫ be a positive real number. Then there is a natural number l depending only on d, r, ǫ satisfying the following. Assume that

$( X , B )$is a projective ǫ-lc pair of dimension d, and

• A is a very ample divisor on X with$A ^ { d } \leq r$

Then there is a projective small birational morphism$\phi \colon Y  X$and a very ample divisor A on Y such that

• Y is normal,

$K _ { Y }$is Q-Cartier,

$A _ { Y } ^ { d } \leq l ,$, and

$A _ { Y } - \phi ^ { * } A$is ample.

Proof. Since A is very ample and$A ^ { d } \leq r$, X belongs to a bounded set of projective varieties. Then there exist finitely many projective morphisms$V ^ { i }  T ^ { i }$of quasi-projective varieties such that each X in the lemma is isomorphic to the fibre of$V ^ { i }  T ^ { i }$over some closed point$t \in T ^ { i }$for some i. We can also assume that there is a divisor$A _ { V } ^ { i }$on$V ^ { i }$which is very ample over$T ^ { i }$and such that$A \sim A _ { V } ^ { i } | _ { X }$. For the rest of the proof we fix i and write $V = V ^ { i } , T = T ^ { i } , A _ { V } = A _ { V } ^ { i }$. We will shrink$V , T$when convenient.

Let$W  V$be a log resolution. Let Σ be the reduced exceptional divisor of$W  V$ Let$\Gamma _ { W } = ( 1 - \textstyle { \frac { \epsilon } { 2 } } ) \Sigma$. Run an MMP on$K _ { W } + \Gamma _ { W }$over V and let$( U , \Gamma _ { U } )$be the resulting log minimal model of$( W , \Gamma _ { W } )$over V. Shrinking$W , U , V , T$we can assume that the following holds: if$t \in T$is a closed point and if$Y , X$are the fibres of$U  T$and$V  T$over$t ,$ respectively, then

• Y is normal,

$K _ { Y } \sim _ { \mathbb { Q } } K _ { U } | _ { Y } .$

$\Gamma _ { U }$does not contain$Y .$,

• support of$\Gamma _ { Y } : = \Gamma _ { U } | _ { Y }$coincides with the reduced exceptional divisor of$Y  X$，

• and each non-zero coeficient of$\Gamma _ { Y }$is equal to$1 - \textstyle { \frac { \epsilon } { 2 } }$

Now let$( X , B )$be as in the lemma. We can assume X is isomorphic to the fibre of $V  T$over some closed point t. Let Y be the fibre of$U \to T$over t and let$\phi \colon Y  X$be the induced birational morphism. We show that$\phi$is a small morphism. Let$K _ { Y } + B _ { Y } =$ $\phi ^ { * } ( K _ { X } + B )$. Then

$$
B _ {Y} - \Gamma_ {Y} = (K _ {Y} + B _ {Y}) - (K _ {Y} + \Gamma_ {Y}) \equiv - (K _ {Y} + \Gamma_ {Y}) / X
$$

is anti-nef over X. Moreover,$\phi _ { * } ( B _ { Y } - \Gamma _ { Y } ) = B \ge 0$. Thus by the negativity lemma, $B _ { Y } - \Gamma _ { Y } \geq 0$. However,$( X , B )$is ǫ-lc, so each coeficient of$B _ { Y } { \mathrm { ~ i s ~ } } \leq 1 - \epsilon$but by the previous paragraph each non-zero coeficient of$\Gamma _ { Y }$is$\geq 1 - \frac { \epsilon } { 2 }$. This is possible only if $\Gamma _ { Y } = 0$. Therefore,$\phi$is a small morphism as Supp Γ<sub>Y</sub> contains every divisor contracted by $\phi .$Moreover, since U is Q-factorial,$K _ { Y } \sim _ { \mathbb { Q } } K _ { U } | _ { Y }$is Q-Cartier.

Pick a divisor A<sub>U</sub> on U which is very ample over T. Let$A _ { Y } = A _ { U } | _ { Y }$. Then$A _ { Y }$is very ample on$Y$and$A _ { Y } ^ { d } \leq l$for some fixed natural number l. We can assume that$A _ { U } - \psi ^ { * } A _ { V }$ is ample over$T$where ψ is the morphism$U  V$. This ensures that$A _ { Y } - \phi ^ { * } A$is ample.

## 2.25. Semi-ample divisors.

Lemma 2.26. Assume$Y  X$is a contraction of normal projective varieties, C is a nef R-divisor on Y and A is the pullback of an ample R-divisor on X. If C is semi-ample over X, then$C + a A$is semi-ample (globally) for any real number$a > 0$

Proof. Since C is semi-ample over X, it defines a contraction$\phi \colon Y \to Z / X$to a normal projective variety. Replacing$Y$with$Z$and replacing$C , A$with$\phi _ { * } C , \phi _ { * } A$, respectively, we can assume$C$is ample over X. Pick$a > 0$. Now$C + b A$is ample for some$b \gg a$because A is the pullback of an ample divisor on X. Since C is globally nef,

$$
C + t b A = (1 - t) C + t (C + b A)
$$

is ample for any$t \in ( 0 , 1 ]$. In particular, taking$\begin{array} { r } { t = \frac { a } { b } } \end{array}$we see that$C +$aA is ample.

## 3. Lc thresholds of anti-log canonical systems of Fano pairs

In this section we study lc thresholds of the R-linear systems$| - ( K _ { X } + B ) | _ { \mathbb { R } }$for (weak) log Fano pairs (X, B). As pointed out in the introduction, understanding such thresholds is key to the proof of Theorem 1.1. We will show that Theorem 1.8 implies Theorem 1.6 assuming Theorem 1.1 in lower dimension. We also prove that Theorem 1.8 implies Theorem 1.7. First we consider a special case of Theorem 1.6.

Proposition 3.1. Let d be a natural number and ǫ be a positive real number. Assume that Theorem 1.8 holds in dimension$\leq d$and that Theorem 1.1 holds in dimension$\leq d - 1$. Then there is a positive real number v depending only on$d , \epsilon$satisfying the following. Assume that

• X is a Q-factorial ǫ-lc Fano variety of dimension$d ,$

• X has Picard number one, and

$0 \leq L \sim _ { \mathbb { R } } - K _ { X }$

Then each coeficient of L is less than or equal to$v .$

Proof. Step 1. In this step we do some preparations. Pick a component$T$of L. Since X has Picard number one,$L \sim _ { \mathbb { R } } u T$for some$u \geq \mu _ { T } L$. Thus we may replace$L _ { ; }$hence assume $L = u T$. We need to show u is bounded from above. By Theorem 2.13, there is a natural number n depending only on d such that$K _ { X }$has an n-complement$K _ { X } + \Omega$. Moreover, by Theorems 2.10 and 2.11 in dimension d, and 1.1 in lower dimension, replacing n depending only on$d , \epsilon ,$we can assume$\vert - n K _ { X } \vert$defines a birational map and that$\operatorname { v o l } ( - K _ { X } )$is bounded from above.

Step 2. In this step we show that$( X , \Omega )$is log birationally bounded. Indeed applying [5, Proposition$4 . 4 ]$(by taking$B = 0$and$M = n \Omega )$we deduce that there exist a number $\dot { c } \in \mathbb { R } ^ { > 0 }$and a bounded set of couples P depending only on$d , \epsilon$satisfying the following: there is a projective log smooth couple$( V , \Lambda ) \in \mathcal { P }$and a birational map$V  X$such that

• Supp Λ contains the exceptional divisor of$V  X$and the birational transform of $\operatorname { S u p p } \Omega ;$

• for a common resolution$\phi \colon W \to X$and$\psi \colon W \to V$, each coeficient of$\psi _ { * } \phi ^ { * } \Omega$is at most c.

Enlarging Λ we can also assume that$H \leq \Lambda$for some very ample divisor$H \geq 0$

Step 3. Let B be a boundary such that$( X , B )$is ǫ-lc and$K _ { X } + B \sim _ { \mathbb { R } } 0$. Let

$$
K _ {V} + B _ {V} = \psi_ {*} \phi^ {*} (K _ {X} + B) \text {   and   } K _ {V} + \Omega_ {V} = \psi_ {*} \phi^ {*} (K _ {X} + \Omega).
$$

Then$( V , B _ { V } )$is sub-ǫ-lc and

$$
a (T, V, B _ {V}) = a (T, X, B) \leq 1.
$$

Similarly,$( V , \Omega _ { V } )$is sub-lc and

$$
a (T, V, \Omega_ {V}) = a (T, X, \Omega) \leq 1.
$$

By Step 2, the union of$\operatorname { S u p p } \Omega _ { V }$and the exceptional divisors of$V \ -  \ X$is contained in $\operatorname { S u p p } \Lambda$, hence$\Omega _ { V } \leq \Lambda$which implies

$$
a (T, V, \Lambda) \leq a (T, V, \Omega_ {V}) \leq 1.
$$

Step$\it 4 .$In this step we show that the coeficients of$B _ { V }$are bounded from below. Assume D is a component of$B _ { V }$with negative coeficient. Let$K _ { V } + \Gamma _ { V } = \psi _ { * } \phi ^ { * } K _ { X }$. Then$\Gamma _ { V } +$ $\psi _ { * } \phi ^ { * } B = B _ { V }$, hence$\mu _ { D } \Gamma _ { V } \leq \mu _ { D } B _ { V } ,$so it is enough to bound$\mu _ { D } \Gamma _ { V }$from below. Now $K _ { V } + \Gamma _ { V } \equiv - \psi _ { * } \phi ^ { * } \Omega$, hence$\mathrm { d e g } _ { H } ( K _ { V } + \Gamma _ { V } )$is bounded from below, by Step 2. Thus $\deg _ { H } \Gamma _ { V }$is bounded from below because$\deg _ { H } K _ { V }$belongs to a fixed finite set as$( V , \Lambda ) \in \mathcal { P }$ and$H \leq \Lambda$

Write$\Gamma _ { V } = I - J$where$I , J$are efective divisors with no common components. Since $I \leq \Lambda , \deg _ { H } I \leq \deg _ { H } \Lambda$which shows$\deg _ { H } I$is bounded from above, hence$\deg _ { H } J$is bounded from above too. Therefore, the coeficients of J are bounded from above which in turn shows the coeficient of D in$\Gamma _ { V }$is bounded from below as required. Note that this also implies the coeficients of$\Omega _ { V }$are bounded from below.

Step 5. In this step we introduce a boundary$\Delta$. By the previous step, there exists $\alpha \in ( 0 , 1 )$depending only on$d ,$ǫ such that

$$
\Delta := \alpha B _ {V} + (1 - \alpha) \Lambda \geq 0.
$$

Then, by Lemma$2 . 3 , ( V , \Delta )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$where$\epsilon ^ { \prime } = \alpha \epsilon$because$( V , B _ { V } )$is sub-ǫ-lc and$( V , \Lambda )$is lc. Moreover, by Step$s ,$

$$
\begin{array}{c} a (T, V, \Delta) = \alpha a (T, V, B _ {V}) + (1 - \alpha) a (T, V, \Lambda) \\ \leq \alpha + (1 - \alpha) = 1. \end{array}
$$

On the other hand, there is a bounded number$l \in \mathbb N$such that$l H { - } N$is ample. Moreover, by construction,$- B _ { V } \sim _ { \mathbb { R } } K _ { V }$, hence we can assume$l H - B _ { V } \sim _ { \mathbb { R } } l H + K _ { V }$is ample as well. This in turn implies

$$
l H - \Delta = \alpha (l H - B _ {V}) + (1 - \alpha) (l H - \Lambda)
$$

is ample too. In addition, there is a bounded natural number r such that$( l H ) ^ { d } \leq r .$

Step 6. In this step we finish the proof by applying Theorem 1.8. Let$M = \psi _ { * } \phi ^ { * } u T$ Since$\Omega \equiv - K _ { X } \equiv u T$, the degree deg${ \mathrm { ~  ~ \mu ~ } } _ { H } M = \deg _ { H } ( \psi _ { * } \phi ^ { * } \Omega )$is bounded from above, by Step 2, which implies the coeficients of M are bounded from above. In particular, we may assume$T$is exceptional over$V ,$otherwise u would be bounded. Thus M is exceptional over X, hence its support is inside Λ. So perhaps after replacing l we can assume$l H - M$ is ample.

On the other hand, since T is ample,$\phi ^ { * } u T \leq \psi ^ { * } M$, by the negativity lemma, hence the coeficient of the birational transform of$T$in$\psi ^ { * } M$is at least u. Therefore,$\begin{array} { r } { ( V , \Delta + \frac { 1 } { u } M ) } \end{array}$is not klt as

$$
a (T, V, \Delta + \frac {1}{u} M) \leq a (T, V, \Delta) - 1 \leq 0.
$$

Now by Theorem 1.8, there is a positive number t depending only on$d , \epsilon ^ { \prime } , r$such that $( V , \Delta + t M )$is klt. Therefore,$\textstyle t < { \frac { 1 } { u } }$, hence$\begin{array} { r } { u < v : = \frac { 1 } { t } } \end{array}$

Lemma 3.2. Assume that Theorem 1.8 holds in dimension$\leq d$and that Theorem 1.1 holds in dimension$\leq d - 1$. Then Theorem 1.6 holds in dimension$d .$

Proof. Pick$\epsilon ^ { \prime } \in ( 0 , \epsilon )$. Let$( X , B )$and$A = - ( K _ { X } + B )$be as in Theorem 1.6 in dimension d and pick$L \in | A | _ { \mathbb { R } }$. Let s be the largest number such that$( X , B + s L )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$. It is enough to show s is bounded from below away from zero. In particular, we may assume$s < 1$

Replacing X with a Q-factorialisation, we can assume X is Q-factorial. There is a prime divisor$T$over$X$, that is, on birational models of X, with log discrepancy

$$
a (T, X, B + s L) = \epsilon^ {\prime}.
$$

If$T$is not exceptional over X, then we let$\phi \colon Y  X$be the identity morphism. But if T is exceptional over X, then we let$\phi \colon Y  X$be the extremal birational contraction which extracts T. Let$K _ { Y } + B _ { Y } = \phi ^ { * } ( K _ { X } + B )$and let${ \cal L } _ { Y } = \phi ^ { * } { \cal L }$. By assumption,

$$
\mu_ {T} B _ {Y} \leq 1 - \epsilon \text {   but   } \mu_ {T} (B _ {Y} + s L _ {Y}) = 1 - \epsilon^ {\prime},
$$

hence µ<sub>T</sub>s$L _ { Y } \geq \epsilon - \epsilon ^ { \prime } .$

Since$s < 1$

$$
- (K _ {X} + B + s L) = A - s L \sim_ {\mathbb {R}} (1 - s) A
$$

is nef and big, hence$- ( K _ { Y } + B _ { Y } + s L _ { Y } )$is also nef and big. Thus$( Y , B _ { Y } + s L _ { Y } )$is klt weak log Fano, so$Y$is of Fano type. Run an MMP on −T and let$Y ^ { \prime }  Z ^ { \prime }$be the resulting Mori fibre space. Then

$$
- \left(K _ {Y ^ {\prime}} + B _ {Y ^ {\prime}} + s L _ {Y ^ {\prime}}\right) \sim_ {\mathbb {R}} (1 - s) L _ {Y ^ {\prime}} \geq 0.
$$

Moreover,$( Y ^ { \prime } , B _ { Y ^ { \prime } } + s L _ { Y ^ { \prime } } )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$because$( Y , B _ { Y } + s L _ { Y } )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$and −$. ( K _ { Y } + B _ { Y } + s L _ { Y } )$ is semi-ample. If dim$Z ^ { \prime } > 0$, then restricting to a general fibre of$Y ^ { \prime }  Z ^ { \prime }$and applying Theorem 1.6 in lower dimension by induction (or applying Theorem 1.1) shows that the coeficients of the horizontal$/ Z ^ { \prime }$components of$( 1 - s ) L _ { Y ^ { \prime } }$are bounded from above. In particular,$\mu _ { T ^ { \prime } } ( 1 - s ) L _ { Y ^ { \prime } }$is bounded from above. Thus from the inequality

$$
\mu_ {T ^ {\prime}} (1 - s) L _ {Y ^ {\prime}} \geq \frac {(1 - s) (\epsilon - \epsilon^ {\prime})}{s},
$$

we deduce that$s$is bounded from below away from zero. Therefore, we can assume$Z ^ { \prime }$is a point and that$Y ^ { \prime }$is a Fano variety with Picard number one. Now

$$
- K _ {Y ^ {\prime}} \sim_ {\mathbb {R}} L _ {Y ^ {\prime}} + B _ {Y ^ {\prime}} = (1 - s) L _ {Y ^ {\prime}} + s L _ {Y ^ {\prime}} + B _ {Y ^ {\prime}} \geq (1 - s) L _ {Y ^ {\prime}},
$$

so by Proposition 3.1,$\mu _ { T ^ { \prime } } ( 1 - s ) L _ { Y ^ { \prime } }$is bounded from above which again gives a lower bound for s as before.

Next we treat Theorem 1.7. As mentioned in the introduction, the theorem and its proof are independent of the rest of this paper when lct$( X , B , | A | _ { \mathbb { R } } ) < 1$

Lemma 3.3. Assume Theorem 1.8 holds in dimension d. Then Theorem 1.7 holds in dimension d when lct$( X , B , | A | _ { \mathbb { R } } ) = 1$

Proof. By definition of the lc threshold, there exists a sequence of R-divisors

$$
0 \leq L _ {i} \sim_ {\mathbb {R}} A = - (K _ {X} + B)
$$

such that the numbers$t _ { i } : = \operatorname { l c t } ( X , B , L _ { i } )$form a decreasing sequence with lim$t _ { i } = 1$

Assume$( X , B )$is not exceptional, that is, assume there is$0 \leq L \sim _ { \mathbb { R } }$A such that$( X , B +$ $L )$is not klt. Thus lct$( X , B , L ) \leq 1$. Since lct$( X , B , \vert A \vert _ { \mathbb { R } } ) = 1$, we deduce lct$( X , B , L ) = 1$ and that$( X , B + L )$is lc but not klt. If B is a Q-boundary, then using approximation, we can replace L so that$0 \leq L \sim _ { \mathbb { Q } } A .$, so we are done in this case by taking$D = L$

Now assume$( X , B )$is exceptional, that is, for any$0 \leq L \sim _ { \mathbb { R } } A$the pair$( X , B + L )$is klt. We will derive a contradiction. By [5, Lemma$7 . 2 ]$, there is$\epsilon > 0$such that$( X , B { + } L _ { i } )$is ǫ-lc for every i. Then by Theorem 1.8 in dimension$d ,$there is$s > 0$such that$\left( X , B + L _ { i } + s L _ { i } \right)$ is klt, for every i. But then$1 + s < t _ { i }$for every i which contradicts lim$t _ { i } = 1$

Proposition 3.4. Theorem 1.7 holds when lct$( X , B , | A | _ { \mathbb { R } } ) < 1$

Proof. Step 1. From here to the end of Step 4 we find$D \in | A | _ { \mathbb { R } }$such that

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) = \operatorname{lct} (X, B, D).
$$

In Step 5 we treat the case when B is a Q-boundary. In this step we make some preparations.

Replacing X with a Q-factorialisation, we can assume X is Q-factorial. By definition of the lc threshold, there exists a sequence of R-divisors

$$
0 \leq L _ {i} \sim_ {\mathbb {R}} A = - (K _ {X} + B)
$$

such that the numbers$t _ { i } : = \mathrm { l c t } ( X , B , L _ { i } ) \in ( 0 , 1 )$form a decreasing sequence with

$$
t := \operatorname{lct} (X, B, | A | _ {\mathbb {R}}) = \lim t _ {i}.
$$

If$t = t _ { i }$for some$i ,$then put$D = L _ { i }$. So for now assume$t \neq t _ { i }$for every i.

Step 2. In this step we choose elements$H _ { i } \in | A | _ { \mathbb { R } }$and define birational contractions $X _ { i } ^ { \prime }  X$with respect to some lc places of$( X , B + t _ { i } L _ { i } )$. Pick$H _ { i } \in | A | _ { \mathbb { R } }$so that$( X , B + H _ { i } )$ is klt and$\left( { { X , B + t _ { i } } { L _ { i } } + H _ { i } } \right)$is lc, for any$i ,$and such that the coeficients of the$H _ { i }$belong to a fixed DCC set. Existence of the DCC set follows from the fact that A is semi-ample: indeed,$A \sim _ { \mathbb { R } } \sum \alpha _ { j } G _ { j }$where$G _ { j }$are base point free Cartier divisors and$\alpha _ { j } > 0 ;$so to find the$H _ { i }$we only need to move the$G _ { j }$appropriately. Note that

$$
K _ {X} + B + t _ {i} L _ {i} + (1 - t _ {i}) H _ {i} \sim_ {\mathbb {R}} 0.
$$

Let$T _ { i } ^ { \prime }$be an lc place of$( X , B + t _ { i } L _ { i } )$. If$T _ { i } ^ { \prime }$is not exceptional over X, we let$\phi _ { i } \colon X _ { i } ^ { \prime } \to X$ to be the identity morphism, but if$T _ { i } ^ { \prime }$is exceptional over X, we let$\phi _ { i } \colon X _ { i } ^ { \prime } \ \to \ \bar { X }$be the extremal birational contraction which extracts$T _ { i } ^ { \prime } .$. Let$B _ { i } ^ { \prime } , L _ { i } ^ { \prime } , H _ { i } ^ { \prime }$be the birational transforms of$B , L _ { i } , H _ { i }$Then${ \cal H } _ { i } ^ { \prime } \ = \ \phi _ { i } ^ { * } { \cal H } _ { i }$because$H _ { i }$cannot contain any lc centre of $( X , B + t _ { i } L _ { i } )$. Moreover,

$$
K _ {X _ {i} ^ {\prime}} + T _ {i} ^ {\prime} + B _ {i} ^ {\prime} + t _ {i} L _ {i} ^ {\prime} + (1 - t _ {i}) H _ {i} ^ {\prime} = \phi_ {i} ^ {*} (K _ {X} + B + t _ {i} L _ {i} + (1 - t _ {i}) H _ {i}) \sim_ {\mathbb {R}} 0.
$$

Step 3. In this step we run an MMP on

$$
- (K _ {X _ {i} ^ {\prime}} + T _ {i} ^ {\prime} + B _ {i} ^ {\prime} + (1 - t) H _ {i} ^ {\prime})
$$

and study the outcome. Note that here we have used t rather than$t _ { i } .$. By [5, 2.13(7)],$X _ { i } ^ { \prime }$ is of Fano$\mathrm { t y p e } .$, so we can indeed run such an MMP. Let$X _ { i } ^ { \prime \prime }$be the resulting model of the MMP. Then

$$
\left(X _ {i} ^ {\prime \prime}, T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + t _ {i} L _ {i} ^ {\prime \prime} + \left(1 - t _ {i}\right) H _ {i} ^ {\prime \prime}\right)
$$

is lc, and the coeficients of$T _ { i } ^ { \prime \prime } + B _ { i } ^ { \prime \prime }$and$H _ { i } ^ { \prime \prime }$belong to a fixed DCC set independent of i. Since the numbers$1 - t _ { i }$form an increasing sequence approaching$1 - t .$, by the ACC for lc thresholds [13], we can assume

$$
(X _ {i} ^ {\prime \prime}, T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + (1 - t) H _ {i} ^ {\prime \prime})
$$

is lc, for every i.

Now assume the MMP ends with a Mori fibre space$X _ { i } ^ { \prime \prime }  Z _ { i } ^ { \prime \prime }$, for infinitely many i. Then for such i,

$$
K _ {X _ {i} ^ {\prime \prime}} + T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + (1 - t) H _ {i} ^ {\prime \prime}
$$

is ample over$Z _ { i } ^ { \prime \prime }$. On the other hand,

$$
K _ {X _ {i} ^ {\prime \prime}} + T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + t _ {i} L _ {i} ^ {\prime \prime} + (1 - t _ {i}) H _ {i} ^ {\prime \prime} \sim_ {\mathbb {R}} 0
$$

which implies

$$
K _ {X _ {i} ^ {\prime \prime}} + T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + (1 - t _ {i}) H _ {i} ^ {\prime \prime}
$$

is anti-nef over$Z _ { i } ^ { \prime \prime }$. This contradicts [13, Theorem 1.5] by restricting to the general fibres of$X _ { i } ^ { \prime \prime }  Z _ { i } ^ { \prime \prime }$. Thus replacing the sequence with a subsequence, we can assume the MMP ends with a minimal model$X _ { i } ^ { \prime \prime }$, for every i.

Step$\it 4 .$In this step we find the desired$D \in | A | _ { \mathbb { R } }$such that lct$( X , B , D ) = t$. Fix i. Since

$$
- (K _ {X _ {i} ^ {\prime \prime}} + T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + (1 - t) H _ {i} ^ {\prime \prime})
$$

is nef, hence semi-ample, it is R-linearly equivalent to some R-divisor$P _ { i } ^ { \prime \prime } ~ \ge ~ 0$. Since $X _ { i } ^ { \prime } \ \mathrm { ~ -- \to ~ } X _ { i } ^ { \prime \prime }$is an MMP on

$$
- (K _ {X _ {i} ^ {\prime}} + T _ {i} ^ {\prime} + B _ {i} ^ {\prime} + (1 - t) H _ {i} ^ {\prime}),
$$

we get an R-divisor$P _ { i } ^ { \prime } \ge 0$such that

$$
- (K _ {X _ {i} ^ {\prime}} + T _ {i} ^ {\prime} + B _ {i} ^ {\prime} + (1 - t) H _ {i} ^ {\prime}) \sim_ {\mathbb {R}} P _ {i} ^ {\prime}
$$

which in turn gives an R-divisor$P _ { i } \ge 0$such that

$$
- (K _ {X} + B + (1 - t) H _ {i}) \sim_ {\mathbb {R}} P _ {i}.
$$

By construction,

$$
(X, B + (1 - t) H _ {i} + P _ {i})
$$

is not klt near the generic point of the centre of$T _ { i } ^ { \prime }$on$X$. Moreover,$P _ { i } ~ \sim _ { \mathbb { R } ^ { } } ~ t A$, and $( X , B + P _ { i } )$is not klt as Supp$H _ { i }$does not contain the centre of$T _ { i }$. Put$\begin{array} { r } { D = \frac { 1 } { t } P _ { i } } \end{array}$. Then D ∼<sub>R</sub> A and lct$( X , B , D ) \leq t ,$so the inequality is actually an equality by definition of t.

Step 5. In this step we treat the case when B is a Q-boundary. Fix i. Since$A _ { i }$is a Q-divisor, we can assume$H _ { i }$is a Q-divisor. If t is a rational number, then in Step 4 we can take$P _ { i } ^ { \prime \prime }$to be a Q-divisor, hence$P _ { i }$is also a Q-divisor which in turn means we can choose D to be a Q-divisor. Assume now that t is not a rational number. We will derive a contradiction. Assume

$$
- (K _ {X _ {i} ^ {\prime \prime}} + T _ {i} ^ {\prime \prime} + B _ {i} ^ {\prime \prime} + (1 - t) H _ {i} ^ {\prime \prime})
$$

is not big. Then, since it is semi-ample, it is numerically trivial on some covering family of curves, hence taking intersection with such curves C and using the fact that$H _ { i } ^ { \prime \prime } \cdot C \neq 0$(as $H _ { i } ^ { \prime \prime }$is big) ensures that t is a rational number, a contradiction. On the other hand, if the above divisor is big, then

$$
- (K _ {X _ {i} ^ {\prime}} + T _ {i} ^ {\prime} + B _ {i} ^ {\prime} + (1 - t) H _ {i} ^ {\prime})
$$

is big and this in turn implies

$$
- (K _ {X _ {i} ^ {\prime}} + T _ {i} ^ {\prime} + B _ {i} ^ {\prime} + (1 - e) H _ {i} ^ {\prime})
$$

is also big for some rational number$e \in ( 0 , t )$. Thus as in Step 4 we can find$0 \leq Q _ { i } \sim _ { \mathbb { Q } }$eA such that$( X , B + Q _ { i } )$is not klt. Letting$\begin{array} { r } { D = \frac { 1 } { e } Q _ { i } } \end{array}$gives$0 \leq D \sim _ { \mathbb { Q } }$A with

$$
\operatorname{lct} (X, B, D) \leq e <   t,
$$

contradicting the definition of t.

## 4. Complements in a neighbourhood of a non-klt centre

In this section, we prove our main result on the existence of complements (Theorem 1.9). It does not follow directly from [5] but the proofs in [5] work with appropriate modifications. First we treat a special case of the theorem.

Proposition 4.1. Theorem 1.9 holds under the additional assumption that there is a boundary Γ such that

• (X, Γ) is plt with$S = | \Gamma |$, and

$\alpha M - ( K _ { X } + \Gamma )$is ample for some real number$\alpha > 0$

Proof. Step 1. In this step we reduce to the case when$\alpha \in ( 0 , 2 )$and when$B - \Gamma$has small (positive or negative) coeficients. Since$M - \left( K _ { X } + B \right)$is nef and big and$\alpha M - ( K _ { X } + \Gamma )$ is ample,

$$
\begin{array}{c} (1 - t + t \alpha) M - (K _ {X} + (1 - t) B + t \Gamma) = (1 - t + t \alpha) M - (1 - t) (K _ {X} + B) - t (K _ {X} + \Gamma) \\ = (1 - t) (M - (K _ {X} + B)) + t (\alpha M - (K _ {X} + \Gamma)) \end{array}
$$

is ample for any$t \in ( 0 , 1 )$. Thus replacing Γ with$( 1 - t ) B + t \Gamma$for some suficiently small real number$t > 0$, we can replace α by some rational number in (0, 2). Note that since $( X , B )$is lc and since S is a non-klt centre of this pair, we have$S \le \lfloor B \rfloor$and the above change of Γ preserves the plt property of$( X , \Gamma )$and the condition$S = \left\lfloor \Gamma \right\rfloor$

It is also clear that if we choose t small enough then we can ensure that$B - \Gamma$has suficiently small positive or negative coeficients (we will use this in steps below).

Step 2. In this step we consider bounded complements on S. Since$( X , \Gamma )$is plt, S is normal. Define

$$
K _ {S} + B _ {S} = (K _ {X} + B) | _ {S}
$$

by adjunction. Then$( S , B _ { S } )$is lc and the coeficients of$B _ { S }$belong to$\Phi ( \mathfrak { S } )$for some finite set${ \mathfrak { S } } \subset [ 0 , 1 ]$of rational numbers depending only on p [37, Proposition 3.8][5, Lemma 3.3] where

$$
\Phi (\mathfrak {S}) = \{1 - \frac {s}{l} \mid s \in \mathfrak {S}, l \in \mathbb {N} \}.
$$

By assumption,$M | _ { S } \equiv 0$, hence$M | _ { S } \sim _ { \mathbb { Q } } 0$as M is semi-ample. In particular,

$$
- (K _ {X} + \Gamma) | _ {S} \sim_ {\mathbb {R}} (\alpha M - (K _ {X} + \Gamma)) | _ {S}
$$

is ample. Moreover, since (X, Γ) is plt, defining

$$
K _ {S} + \Gamma_ {S} = (K _ {X} + \Gamma) | _ {S}
$$

by adjunction,$( S , \Gamma _ { S } )$is klt. Thus we deduce that S is of Fano type. On the other hand,

$$
- (K _ {S} + B _ {S}) \sim_ {\mathbb {Q}} (M - (K _ {X} + B)) | _ {S}
$$

is nef. Therefore, applying Theorem 2.13, there is a natural number n depending only on $d , \mathfrak { S }$such that$K _ { S } + B _ { S }$has an n-complement$K _ { S } + B _ { S } ^ { + }$which satisfies$B _ { S } ^ { + } \geq B _ { S }$. We can assume that nB is an integral divisor after replacing n with np.

Note that since S is of Fano type and$M | _ { S } \sim _ { \mathbb { Q } } 0$, in fact we have$M | _ { S } \sim 0$as$\mathrm { P i c } ( S )$is torsion-free (cf. [16, Proposition 2.1.2]; the point is that$h ^ { i } ( { \mathcal { O } } _ { S } ) = 0$for$i > 0$which is a consequence of Kawamata-Viehweg vanishing theorem).

Step 3. In this step we take a resolution of X and define appropriate divisors on it. Let $\phi \colon X ^ { \prime } \to X$be a log resolution of$( X , B + \Gamma ) , \ S ^ { \prime } \subset X ^ { \prime }$be the birational transform of$S _ { i }$ and$\psi \colon S ^ { \prime } \to S$be the induced morphism. Put

$$
N := M - (K _ {X} + B)
$$

and let$K _ { X ^ { \prime } } + B ^ { \prime } , M ^ { \prime } , N ^ { \prime }$be the pullbacks of$K _ { X } + B , M , N$, respectively. Let$E ^ { \prime }$be the sum of the components of$B ^ { \prime }$which have coeficient 1, and let$\Delta ^ { \prime } = B ^ { \prime } - E ^ { \prime }$. Define

$$
L ^ {\prime} := (n + 2) M ^ {\prime} - n K _ {X ^ {\prime}} - n E ^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor
$$

which is an integral divisor. Note that

$$
\begin{array}{c} L ^ {\prime} = (n + 2) M ^ {\prime} - n K _ {X ^ {\prime}} - n B ^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor \\ = 2 M ^ {\prime} + n (M ^ {\prime} - K _ {X ^ {\prime}} - B ^ {\prime}) + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor \\ = 2 M ^ {\prime} + n N ^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor . \end{array}
$$

Now write

$$
K _ {X ^ {\prime}} + \Gamma^ {\prime} = \phi^ {*} (K _ {X} + \Gamma).
$$

Then we can assume that$B ^ { \prime } - \Gamma ^ { \prime } = \phi ^ { * } ( B - \Gamma )$has suficiently small (positive or negative) coeficients by Step 1. The coeficient of$S ^ { \prime }$in both$B ^ { \prime }$and$\Gamma ^ { \prime }$is 1 but its coeficient in$\Delta ^ { \prime }$is 0.

Step$\it 4 .$In this step we introduce a boundary$\Theta ^ { \prime }$and study related divisors. Let$P ^ { \prime }$be the unique integral divisor so that

$$
\Theta^ {\prime} := \Gamma^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor + P ^ {\prime}
$$

is a boundary,$( X ^ { \prime } , \Theta ^ { \prime } )$is plt, and$\lfloor \Theta ^ { \prime } \rfloor = S ^ { \prime }$(in particular, we are assuming$\Theta ^ { \prime } \geq 0 )$. More precisely, we let$\mu _ { S ^ { \prime } } P ^ { \prime } = 0$and for each prime divisor$D ^ { \prime } \neq S ^ { \prime }$, we let

$$
\mu_ {D ^ {\prime}} P ^ {\prime} := - \mu_ {D ^ {\prime}} \left\lfloor \Gamma^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor \right\rfloor
$$

which satisfies

$$
\begin{array}{c} \mu_ {D ^ {\prime}} P ^ {\prime} = - \mu_ {D ^ {\prime}} \left\lfloor \Gamma^ {\prime} - \Delta^ {\prime} + (n + 1) \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor \right\rfloor \\ = - \mu_ {D ^ {\prime}} \left| \Gamma^ {\prime} - \Delta^ {\prime} + \langle (n + 1) \Delta^ {\prime} \rangle \right| \end{array}
$$

where$\langle { ( n + 1 ) \Delta ^ { \prime } } \rangle$is the fractional part of$( n + 1 ) \Delta ^ { \prime } .$

We claim that$P ^ { \prime } \ge 0$. Pick a component$D ^ { \prime }$of$P ^ { \prime }$. By the above,$D ^ { \prime } \neq S ^ { \prime }$. If$D ^ { \prime }$is a component of$E ^ { \prime }$, then$D ^ { \prime }$is not a component of$\Delta ^ { \prime }$and$\mu _ { D ^ { \prime } } \Gamma ^ { \prime } \in ( 0 , 1 )$as$B ^ { \prime } - \Gamma ^ { \prime }$has small coeficients and$\mu _ { D ^ { \prime } } B ^ { \prime } = 1$, hence$\mu _ { D ^ { \prime } } P ^ { \prime } = 0 ;$; on the other hand, if$D ^ { \prime }$is not a component of$E ^ { \prime }$, then the absolute value of

$$
\mu_ {D ^ {\prime}} (\Gamma^ {\prime} - \Delta^ {\prime}) = \mu_ {D ^ {\prime}} (\Gamma^ {\prime} - B ^ {\prime})
$$

is suficiently small and

$$
\mu_ {S ^ {\prime}} \langle (n + 1) \Delta^ {\prime} \rangle \in [ 0, 1),
$$

hence$\mu _ { D ^ { \prime } } P ^ { \prime } = 0$or$\mu _ { D ^ { \prime } } P ^ { \prime } = 1$, so in any case$\mu _ { D ^ { \prime } } P ^ { \prime } \geq 0$

We show$P ^ { \prime }$is exceptiona$1 / X$. Assume$D ^ { \prime }$is a component of$P ^ { \prime }$which is not exceptional/X and let$D$be its pushdown. Since$S ^ { \prime }$is not a component of$P ^ { \prime }$$D ^ { \prime } \neq S ^ { \prime }$. Let$E , \Delta$be the pushdowns of$E ^ { \prime } , \Delta ^ { \prime }$. Since nB and$n E$are integral,$\mu _ { D } n \Delta$is integral, hence

$$
\mu_ {D} \left\lfloor (n + 1) \Delta \right\rfloor = \mu_ {D} n \Delta .
$$

Then

$$
\begin{array}{r} \mu_ {D ^ {\prime}} P ^ {\prime} = - \mu_ {D ^ {\prime}} \left\lfloor \Gamma^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor \right\rfloor \\ = - \mu_ {D} \left\lfloor \Gamma + n \Delta - \left\lfloor (n + 1) \Delta \right\rfloor \right\rfloor = - \mu_ {D} \left\lfloor \Gamma \right\rfloor = 0 \end{array}
$$

because$\mu _ { D } \Gamma \in [ 0 , 1 )$, a contradiction.

Step 5. In this step we show that sections of$( L ^ { \prime } + P ^ { \prime } ) | _ { S ^ { \prime } }$can be lifted to$X ^ { \prime }$. Let

$$
A := \alpha M - (K _ {X} + \Gamma).
$$

Letting$A ^ { \prime } = \phi ^ { * } A$we have

$$
K _ {X ^ {\prime}} + \Gamma^ {\prime} + A ^ {\prime} - \alpha M ^ {\prime} = 0.
$$

Then

$$
\begin{array}{c} {L ^ {\prime} + P ^ {\prime} = 2 M ^ {\prime} + n N ^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor + P ^ {\prime}} \\ {= K _ {X ^ {\prime}} + \Gamma^ {\prime} + A ^ {\prime} - \alpha M ^ {\prime} + 2 M ^ {\prime} + n N ^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor + P ^ {\prime}} \\ {= K _ {X ^ {\prime}} + \Theta^ {\prime} + A ^ {\prime} + n N ^ {\prime} + (2 - \alpha) M ^ {\prime}.} \end{array}
$$

By Step 1,$2 - \alpha \geq 0$, so

$$
A ^ {\prime} + n N ^ {\prime} + (2 - \alpha) M ^ {\prime}
$$

is nef and big. Moreover,$( X ^ { \prime } , \Theta ^ { \prime } )$is plt with$\lfloor \Theta ^ { \prime } \rfloor = S ^ { \prime }$, so we have

$$
h ^ {1} (L ^ {\prime} + P ^ {\prime} - S ^ {\prime}) = 0
$$

by the Kawamata-Viehweg vanishing theorem as$( X ^ { \prime } , \Theta ^ { \prime } - S ^ { \prime } )$is klt. Thus the restriction map

$$
H ^ {0} (L ^ {\prime} + P ^ {\prime}) \rightarrow H ^ {0} ((L ^ {\prime} + P ^ {\prime}) | _ {S ^ {\prime}})
$$

is surjective.

Step 6. In this step we introduce an efective divisor$G _ { S ^ { \prime } } \sim ( L ^ { \prime } + P ^ { \prime } ) | _ { S ^ { \prime } }$. Recall the n-complement$K _ { S } + B _ { S } ^ { + }$from Step 2. Let$R _ { S } : = B _ { S } ^ { + } - B _ { S }$which satisfies

$$
- n (K _ {S} + B _ {S}) = - n (K _ {S} + B _ {S} ^ {+} + B _ {S} - B _ {S} ^ {+}) \sim - n (B _ {S} - B _ {S} ^ {+}) = n R _ {S} \geq 0.
$$

Let$R _ { S ^ { \prime } }$be the pullback of$R _ { S }$. Since$M ^ { \prime }$is Cartier and since$S ^ { \prime }$is a component of$B ^ { \prime }$with coeficient 1, the divisor

$$
N ^ {\prime} | _ {S ^ {\prime}} = (M ^ {\prime} - (K _ {X ^ {\prime}} + B ^ {\prime})) | _ {S ^ {\prime}}
$$

is well-defined up to linear equivalence. Now since$M ^ { \prime } | _ { S ^ { \prime } } \sim 0$by Step 2, we have

$$
\begin{array}{c} n N ^ {\prime} | _ {S ^ {\prime}} = n (M ^ {\prime} - (K _ {X ^ {\prime}} + B ^ {\prime})) | _ {S ^ {\prime}} \sim - n (K _ {X ^ {\prime}} + B ^ {\prime}) | _ {S ^ {\prime}} \\ = - n \psi^ {*} (K _ {S} + B _ {S}) \sim n \psi^ {*} R _ {S} = n R _ {S ^ {\prime}} \geq 0. \end{array}
$$

Then

$$
\begin{array}{c} (L ^ {\prime} + P ^ {\prime}) | _ {S ^ {\prime}} = (2 M ^ {\prime} + n N ^ {\prime} + n \Delta^ {\prime} - \left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor + P ^ {\prime}) | _ {S ^ {\prime}} \\ \sim G _ {S ^ {\prime}} := n R _ {S ^ {\prime}} + n \Delta_ {S ^ {\prime}} - \left\lfloor (n + 1) \Delta_ {S ^ {\prime}} \right\rfloor + P _ {S ^ {\prime}} \end{array}
$$

where$\Delta _ { S ^ { \prime } } = \Delta ^ { \prime } | _ { S ^ { \prime } }$and$P _ { S ^ { \prime } } = P ^ { \prime } | _ { S ^ { \prime } }$. Note that

$$
\left\lfloor (n + 1) \Delta^ {\prime} \right\rfloor | _ {S ^ {\prime}} = \left\lfloor (n + 1) \Delta^ {\prime} | _ {S ^ {\prime}} \right\rfloor
$$

since$\Delta ^ { \prime }$and$S ^ { \prime }$intersect transversally.

We show$G _ { S ^ { \prime } } \geq 0$. Assume$C ^ { \prime }$is a component of$G _ { S ^ { \prime } }$with negative coeficient. Then since$R _ { S ^ { \prime } }$and$P _ { S ^ { \prime } }$are efective, there is a component$D ^ { \prime }$of$\Delta ^ { \prime }$such that$C ^ { \prime }$is a component of$D ^ { \prime } \vert _ { S ^ { \prime } }$. But

$$
\mu_ {C ^ {\prime}} (n \Delta_ {S ^ {\prime}} - \lfloor (n + 1) \Delta_ {S ^ {\prime}} \rfloor) = \mu_ {C ^ {\prime}} (- \Delta_ {S ^ {\prime}} + \langle (n + 1) \Delta_ {S ^ {\prime}} \rangle) \geq - \mu_ {C ^ {\prime}} \Delta_ {S ^ {\prime}} = - \mu_ {D ^ {\prime}} \Delta^ {\prime} > - 1
$$

which gives$\mu _ { C ^ { \prime } } G _ { S ^ { \prime } } > - 1$and this in turn implies$\mu _ { C ^ { \prime } } G _ { S ^ { \prime } } \geq 0$because$G _ { S ^ { \prime } }$is integral, a contradiction. Therefore$G _ { S ^ { \prime } } \geq 0$, and by Step 5,$L ^ { \prime } + P ^ { \prime } \sim G ^ { \prime }$for some efective divisor$G ^ { \prime }$ whose support does not contain$S ^ { \prime }$and$G ^ { \prime } | _ { S ^ { \prime } } = G _ { S ^ { \prime } }$

Step 7. In this step we introduce Λ and show that it satisfies the properties listed in the theorem. Let$L , P , G$be the pushdowns to X of$L ^ { \prime } , P ^ { \prime } , G ^ { \prime }$. By the definition of$L ^ { \prime } ,$, by the previous step, and by the exceptionality of$P ^ { \prime } { } _ { ; }$, we have

$$
(n + 2) M - n K _ {X} - n E - \left\lfloor (n + 1) \Delta \right\rfloor = L = L + P \sim G \geq 0.
$$

Since$n B$is integral,$\lfloor ( n + 1 ) \Delta \rfloor = n \Delta$, so

$$
\begin{array}{c} (n + 2) M - n (K _ {X} + B) \\ = (n + 2) M - n K _ {X} - n E - n \Delta = L \sim n R := G \geq 0. \end{array}
$$

Let$\Lambda : = B ^ { + } : = B + R$. For consistency of notation, for the rest of the proof we will use $B ^ { + }$instead of Λ. By construction,

$$
n (K _ {X} + B ^ {+}) \sim (n + 2) M.
$$

It remains to show that$( X , B ^ { + } )$is lc over$z = f ( S )$. First we show that$( X , B ^ { + } )$is lc near S: this follows from inversion of adjunction [20], if we show

$$
K _ {S} + B _ {S} ^ {+} = (K _ {X} + B ^ {+}) | _ {S}
$$

which is equivalent to showing$R | _ { S } = R _ { S }$. Since

$$
n R ^ {\prime} := G ^ {\prime} - P ^ {\prime} + \left| (n + 1) \Delta^ {\prime} \right| - n \Delta^ {\prime} \sim L ^ {\prime} + \left| (n + 1) \Delta^ {\prime} \right| - n \Delta^ {\prime} = 2 M ^ {\prime} + n N ^ {\prime} \sim_ {\mathbb {Q}} 0 / X
$$

and since$\lfloor ( n + 1 ) \Delta \rfloor - n \Delta = 0$, we get$\phi _ { * } n R ^ { \prime } = G = n R$and that$R ^ { \prime }$is the pullback of$R .$ Now by Step 6,

$$
\begin{array}{c} n R _ {S ^ {\prime}} = G _ {S ^ {\prime}} - P _ {S ^ {\prime}} + \left\lfloor (n + 1) \Delta_ {S ^ {\prime}} \right\rfloor - n \Delta_ {S ^ {\prime}} \\ = (G ^ {\prime} - P ^ {\prime} + \left| (n + 1) \Delta^ {\prime} \right| - n \Delta^ {\prime}) | _ {S ^ {\prime}} = n R ^ {\prime} | _ {S ^ {\prime}} \end{array}
$$

which means$R _ { S ^ { \prime } } = R ^ { \prime } | _ { S ^ { \prime } }$, hence$R _ { S }$and$R | _ { S }$both pull back to$R _ { S ^ { \prime } }$which implies$R _ { S } = R { \mid } _ { S }$ as required.

Assume now that$( X , B ^ { + } )$is not lc over$z = f ( S )$. By the previous paragraph,$( X , B ^ { + } )$ is lc near$S$and S is a non-klt centre of this pair. On the other hand,$( X , \Gamma )$is plt with $\lfloor \Gamma \rfloor = S$, so if$u > 0$is suficiently small, then

$$
(X, (1 - u) B ^ {+} + u \Gamma)
$$

is plt near$S$and S is a non-klt centre of this pair and no other non-klt centre intersects$S _ { ☉ }$. Then since$( X , B ^ { + } )$is not lc over z, the non-klt locus of

$$
(X, (1 - u) B ^ {+} + u \Gamma)
$$

has at least two connected components (one of which is S) near the fibre$f ^ { - 1 } \{ z \}$. This contradicts the connectedness principle [25, Theorem 17.4] as

$$
- (K _ {X} + (1 - u) B ^ {+} + u \Gamma) = - (1 - u) (K _ {X} + B ^ {+}) - u (K _ {X} + \Gamma)
$$

$$
\sim_ {\mathbb {R}} - u (K _ {X} + \Gamma) \sim_ {\mathbb {R}} u \alpha M - u (K _ {X} + \Gamma) / Z
$$

is ample over$Z .$Therefore,$( X , B ^ { + } )$is lc over z.

Proof. (of Theorem 1.9) Step 1. In this step we take a Q-factorialisation of X and consider the contraction defined by$a M - ( K _ { X } + B )$for some$a > 1$. Replacing$( X , B )$with a Qfactorial dlt model, we can assume X is Q-factorial and that S is a component of$\lfloor B \rfloor$. All the assumptions of the theorem are preserved. The Fano type property is preserved by a relative version of$[ 5 , 2 . 1 3 ( 7 ) ] ~ \mathrm { a s } - ( K _ { X } + B )$is nef over$Z .$

By assumption, M is the pullback of an ample divisor on$Z .$Moreover,$M - \left( K _ { X } + B \right)$ is nef and big, hence in particular it is semi-ample over$Z$since X is of Fano type over $Z .$Thus by Lemma 2.26, if$a > 1$is a real number, then$a M - ( K _ { X } + B )$is semi-ample globally, so it defines a birational contraction$X  U$which is simply the contraction over $Z$defined by$M - \left( K _ { X } + B \right)$: indeed, for any curve C on$X$

$$
(a M - (K _ {X} + B)) \cdot C = 0 \text {   iff   } (M - (K _ {X} + B)) \cdot C = 0 \text {   and   } M \cdot C = 0.
$$

In particular,$X  U$is birational as$a M - ( K _ { X } + B )$is big, the induced map$U \ - \to \ Z$is a morphism and$K _ { X } + B \sim _ { \mathbb { Q } } 0 / U$

Step 2. In this step we make some further modifications of$( X , B )$using the MMP. Since $X$is of Fano type over$Z ,$it is also of Fano type over U. Run an MMP over U on$- ( K _ { X } + S )$ and let$X ^ { \prime }$be the resulting model. The MMP does not contract S as

$$
B - S \sim_ {\mathbb {Q}} - (K _ {X} + S) / U
$$

and S is not a component of$B - S$. Assume that there exist$n \in \mathbb { N }$and$\Lambda ^ { \prime } \geq B ^ { \prime }$such that $( X ^ { \prime } , \Lambda ^ { \prime } )$is lc over$z$and

$$
n (K _ {X ^ {\prime}} + \Lambda^ {\prime}) \sim (n + 2) M ^ {\prime}
$$

where$B ^ { \prime } , M ^ { \prime }$are the pushdowns of$B , M$. Then since$K _ { X } + B \sim _ { \mathbb { Q } } 0 / U$, taking the crepant pullback of$K _ { X ^ { \prime } } + \Lambda ^ { \prime }$to X we get$\Lambda \geq B$such that$( X , \Lambda )$is lc over z and

$$
n (K _ {X} + \Lambda) \sim (n + 2) M.
$$

Note that$M ^ { \prime }$is Cartier as the Cartier property of M is preserved by the MMP, by the cone theorem. Thus replacing X with$X ^ { \prime }$, we can assume$- ( K _ { X } + S )$is semi-ample over U defining a contraction$X \to V / U$. Moreover, every non-klt centre of$( X , S )$is contained in S because$( X , 0 )$is klt as X is Q-factorial and of Fano type over$Z .$

We claim that S is not contracted over$V { : }$otherwise since$K _ { X } + S \sim _ { \mathbb { Q } } 0 / V$, the pair $( V , 0 )$would be lc but not klt and this is a contradiction because there is a boundary Θ such that$( V , \Theta )$is klt as$V$is of Fano type over$Z .$

Note that the pushdown of M to V is Cartier, again by the cone theorem. Replacing X with V , we can then assume that$- ( K _ { X } + S )$is ample over$U$. The Q-factorial property of X maybe lost but we do not need it any more.

Step 3. In this step we introduce a boundary$\Delta$and study some of its properties. Let

$$
\Delta = (1 - b) B + b S
$$

for a suficiently small real number$b > 0$(depending on a). Then$( X , \Delta )$is lc and$S$is a non-klt centre of this pair. Moreover, every non-klt place of$( X , \Delta )$is a non-klt place of both$( X , B )$and$( X , S )$, in particular, every non-klt centre of$( X , \Delta )$is also a non-klt centre of (X, S), hence such centres are contained in S and they are mapped to z.

On the other hand, since$a M - ( K _ { X } + B )$is the pullback of an ample divisor on$U$and $a M - ( K _ { X } + S )$is ample over$U _ { : }$, we see that

$$
\begin{array}{c} a M - (K _ {X} + \Delta) = a M - (K _ {X} + (1 - b) B + b S) \\ = a M - (1 - b) (K _ {X} + B) - b (K _ {X} + S) \\ = (1 - b) (a M - (K _ {X} + B)) + b (a M - (K _ {X} + S)) \end{array}
$$

is globally ample.

Step$\it 4 .$In this step we produce a plt pair and apply Proposition 4.1 to finish the proof. By Lemma 2.7 applied to$( X , \Delta )$, there exist a prime divisor$T$over X and a projective birational morphism$Y  X$such that

• either$Y  X$is small or it contracts$T$but no other divisors,

$( Y , T )$is plt,

$- ( K _ { Y } + T )$is ample over X, and

$a ( T , X , \Delta ) = 0 .$

In particular,$T$is mapped to z, by Step 3, as it is an lc place of$( X , S )$. Moreover, since $\Delta \le B$2

$$
a (T, X, B) = 0.
$$

Let$K _ { Y } + \Delta _ { Y }$be the pullback of$K _ { X } + \Delta$. Define

$$
\Gamma_ {Y} = (1 - v) \Delta_ {Y} + v T
$$

for some suficiently small$v > 0$. Let$M _ { Y }$be the pullback of M. Let$\alpha = ( 1 - v ) a$. Since $a M - ( K _ { X } + \Delta )$is ample and since$- ( K _ { Y } + T )$is ample over$X$

$$
\begin{array}{c} \alpha M _ {Y} - (K _ {Y} + \Gamma_ {Y}) = (1 - v) a M _ {Y} - (K _ {Y} + (1 - v) \Delta_ {Y} + v T) \\ = (1 - v) a M _ {Y} - (1 - v) (K _ {Y} + \Delta_ {Y}) - v (K _ {Y} + T) \\ = (1 - v) (a M _ {Y} - (K _ {Y} + \Delta_ {Y})) - v (K _ {Y} + T) \end{array}
$$

is ample. Moreover,$( Y , \Gamma _ { Y } )$is plt and$T = \lfloor \Gamma _ { Y } \rfloor$maps to z.

Let$K _ { Y } + B _ { Y }$be the pullback of$K _ { X } + B$. By definition of$\Delta , T$is an lc place of $( X , B )$, hence it appears in$B _ { Y }$with coeficient 1. Now we can replace$( X , B ) , M , S$with $( Y , B _ { Y } ) , M _ { Y } , T$and apply Proposition 4.1.

## 5. Singularities of divisors with bounded degree

In this section, we make necessary preparations for the proof of Theorem 1.8. This involves a reduction to the case of projective space and eventually to the toric version of Theorem 1.1 which is well-known [9].

5.1. Finite morphisms to the projective space. We prove a version of Noether normalisation theorem. Part of it is similar to [23, Theorem$2 ]$proved for fields of positive characteristic.

Proposition 5.2. Let$\left( X , \Lambda = \textstyle \sum _ { 1 } ^ { d } S _ { i } \right)$be a projective log smooth pair of dimension d where Λ is reduced. Let$\begin{array} { r } { B = \sum b _ { j } B _ { j } \geq 0 } \end{array}$be an R-divisor. Assume

$x \in \cap ^ { d } S _ { i }$

$\operatorname { S u p p } B$contains no stratum of$( X , \Lambda )$except possibly x, and

• A is a very ample divisor such that$A - S _ { i }$is very ample for each$i .$

Then there is a finite morphism

$$
\pi \colon X \to \mathbb {P} ^ {d} = \operatorname{Proj} k [ t _ {0}, \dots , t _ {d} ]
$$

such that

$\pi ( x ) = z : = ( 1 : 0 : \cdot \cdot : 0 )$

$\pi ( S _ { i } ) = H _ { i }$where$H _ { i }$is the hyperplane defined by$t _ { i }$,

• π is ´etale over a neighbourhood$o f z$,

$\operatorname { S u p p } B$contains no point of$\pi ^ { - 1 } \{ z \}$except possibly x, and

$\deg \pi = A ^ { d }$and de$\begin{array} { r } { \mathrm { { \small ~ \beta ~ } } _ { H _ { i } } C \leq \deg _ { A } B } \end{array}$where$\begin{array} { r } { C = \sum b _ { j } \pi ( B _ { j } ) } \end{array}$

Proof. Since$A - S _ { i }$is very ample for each i, taking general divisors$D _ { i } \in | A - S _ { i } |$we can make sure$( X , \textstyle \sum _ { 1 } ^ { d } R _ { i } )$is log smooth where$R _ { i } : = D _ { i } + S _ { i } \sim A$. Moreover, we can assume that Supp B contains no stratum of$( X , \Sigma _ { 1 } ^ { d } R _ { i } )$other than x: since$D _ { 1 }$is general, it is not a component of$B .$, and if$I \neq x$is a stratum of$( X , \Lambda )$, then$D _ { 1 } | _ { I }$has no common component with$| B | _ { I } ;$this ensures Supp B does not contain any stratum of$( X , \Lambda + D _ { 1 } )$other than$x ;$ repeating this process proves the claim.

Now each$R _ { i }$is the zero divisor of some global section$\alpha _ { i }$of${ \mathcal { O } } _ { X } ( A )$. Choose another global section$\alpha _ { 0 }$so that if$R _ { 0 }$is the zero divisor of$\alpha _ { 0 }$, then$( X , \textstyle \sum _ { 0 } ^ { d } R _ { i } )$is still log smooth, and that$\cap _ { 0 } ^ { d } R _ { i }$is empty. The sections$\alpha _ { 0 } , \ldots , \alpha _ { d }$have no common vanishing point, so they define a morphism$\pi \colon X \to \mathbb { P } ^ { d }$so that${ \mathcal { O } } _ { X } ( A ) \simeq \pi ^ { * } { \mathcal { O } } _ { \mathbb { P } ^ { d } } ( 1 )$and the global section$t _ { i }$of $\mathcal { O } _ { \mathbb { P } ^ { d } } ( 1 )$pulls back to$\alpha _ { i }$, for each$0 \leq i \leq d .$. In particular, since A is ample, π does not contract any curve, hence π is a surjective finite morphism.

Since$t _ { i }$pulls back to$\alpha _ { i }$, the zero divisor of$t _ { i }$pulls back to the zero divisor of$\alpha _ { i } .$that is,$\pi ^ { * } H _ { i } = R _ { i }$. Thus$\pi ( R _ { i } ) = H _ { i }$which in turn gives$\pi ( S _ { i } ) = H _ { i }$. Moreover, since

$$
z := (1: 0: \dots : 0) = \bigcap_ {1} ^ {d} H _ {i},
$$

we get

$$
\pi^ {- 1} \{z \} = \bigcap_ {1} ^ {d} \pi^ {- 1} H _ {i} = \bigcap_ {1} ^ {d} R _ {i}
$$

which shows$\pi ( x ) = z$as$x \in \bigcap _ { 1 } ^ { d } S _ { i } \subseteq \bigcap _ { 1 } ^ { d } R _ { i }$

The rest of the proof is elementary which uses 2.21 among other things and we leave it to the reader.

5.3. Bound on the length of blowup sequences. We state a baby version of Theorem 1.8, due to Viehweg (see [43, Corollary 5.11]), before moving on to the main result of this subsection.

Lemma 5.4. Let d, r be natural numbers. Then there is a positive real number t depending only on d, r satisfying the following. Assume

$X$is a smooth projective variety of dimension$d ,$

$A$is a very ample divisor on X with$A ^ { d } \leq r _ { i }$

$L \geq 0$is an R-divisor on X with$\deg _ { A } L \leq r$

Then$( X , t L )$is klt.

Proof. The assumptions imply that the multiplicity$\mu _ { x } L$is bounded from above, for each closed point$x \in X$. Thus taking t small enough we have$\mu _ { x } t L < 1$. Now applying [29, Proposition 9.5.13] we deduce that$( X , t L )$is klt. It is also easy to prove the lemma using induction on dimension and inversion of adjunction.

It is not hard to extend the lemma and prove Theorem 1.8 when$( X , \operatorname { S u p p } B )$belongs to some bounded family of pairs [5, Proposition 4.2]. The general case of the theorem however requires a lot more work and the main reason is that we have no control over the support of B. Much of the dificulties already appear in the case$X = \mathbb { P } ^ { d }$

In the next key result, we bound the number of blowups in the centre blowup sequence associated to certain lc places.

Proposition 5.5. Let d, r be natural numbers and ǫ be a positive real number. Then there is a natural number p depending only on d, r, ǫ satisfying the following. Assume

$( X , B )$is a projective ǫ-lc pair of dimension$d ,$

• A is a very ample divisor on X with$A ^ { d } \leq r _ { i }$

$( X , \Lambda )$is log smooth where$\Lambda \geq 0$is reduced,

$\deg _ { A } B \leq r$and deg$_ A \Delta \leq r _ { ; }$

• x is a zero-dimensional stratum of$( X , \Lambda )$2

• Supp B does not contain any stratum$o f \left( X , \Lambda \right)$except possibly x,

• T is an lc place of (X, Λ) with centre x, and

$a ( T , X , B ) \leq 1 .$

Then T can be obtained by a sequence of centre blowups, toroidal with respect to$( X , \Lambda )$, of length at most p.

Proof. We will prove the proposition over C. Over other fields we can either apply the Lefschetz principle or simply use formal neighbourhoods instead of analytic neighbourhoods in the arguments below.

Step 1. From here until the end of Step 3, we will relate the problem to a similar problem on the projective space$\mathbb { P } ^ { d }$. In this step we consider a finite morphism to$\mathbb { P } ^ { d }$ Removing the components of Λ not passing through$x ,$we can assume$\Lambda = \textstyle \sum _ { 1 } ^ { d } S _ { i }$where $S _ { i }$are the irreducible components. Since$\deg _ { A } \Lambda \leq r , ( X , \Lambda )$belongs to a bounded family of pairs depending only on$d , r .$. Thus replacing A with a bounded multiple and replacing r accordingly, we can assume$A - S _ { i }$is very ample for each i. Writing$B = \sum b _ { j } B _ { j }$where $B _ { j }$are the distinct irreducible components, by Proposition 5.2, there is a finite morphism

$$
\pi \colon X \to \mathbb {P} ^ {d} = \mathrm{Proj} \mathbb {C} [ t _ {0}, \ldots , t _ {d} ]
$$

mapping x to the origin$z = ( 1 : 0 : \cdots : 0 )$and mapping$S _ { i }$onto the hyperplane$H _ { i }$ defined by$t _ { i }$. Moreover, π is ´etale over z, Supp B contains no point of$\pi ^ { - 1 } \{ z \}$other than $x ,$deg$\pi = A ^ { d }$, and$\deg _ { H _ { i } } C \leq \deg _ { A } B \leq r$where$\begin{array} { r } { C = \sum b _ { j } \pi ( B _ { j } ) } \end{array}$. In addition, by the proof of$5 . 2 , \pi ^ { * } H _ { i }$coincides with$S _ { i }$near x.

Step 2. In this step we consider the centre blowup sequence of T and the induced sequence associated to$\mathbb { P } ^ { d }$. By Lemma 2.20, there exist analytic neighbourhoods U and V of x and z, respectively, such that$\pi ^ { \mathrm { a n } } | _ { U }$induces an analytic isomorphism between the analytic pairs $( U , B ^ { \mathrm { a n } } | _ { U } )$and$( V , C ^ { \mathrm { a n } } | _ { V } )$. In particular,$( \mathbb { P } ^ { d } , C )$is ǫ-lc near z. Let$\begin{array} { r } { \Theta : = \sum _ { 1 } ^ { d } H _ { i } } \end{array}$. Since $\pi ^ { * } H _ { i }$coincides with$S _ { i }$near x, we also have an analytic isomorphism between$( U , \Lambda ^ { \mathrm { a n } } | _ { U } )$and $( V , \Theta ^ { \mathrm { a n } } | _ { V } )$. Moreover, each stratum of$( \mathbb { P } ^ { d } , \Theta )$passes through z and each one is the image of a stratum of$( X , \Lambda )$passing through x. Thus Supp C does not contain any stratum of $( \mathbb { P } ^ { d } , \Theta )$, except possibly z: indeed, if Supp C contains a stratum I, then there is a stratum J of$( X , \Lambda )$passing through x which maps onto I; by the above analytic isomorphisms, $J ^ { \mathrm { a n } } | _ { U } \subseteq \mathrm { S u p p } B ^ { \mathrm { a n } } | _ { U }$which implies$J \subseteq \operatorname { S u p p } B$, hence$J = x$and$I = z$

The centre of T on X, that is x, is an lc centre and a stratum of$( X , \Lambda )$. Let$X _ { 1 }  X _ { 0 } = X$ be the blowup of X along this centre. Let$K _ { X _ { 1 } } + \Lambda _ { 1 }$be the pullback of$K _ { X } + \Lambda$. Then $( X _ { 1 } , \Lambda _ { 1 } )$is log smooth with$\Lambda _ { 1 }$reduced and containing the exceptional divisor of the blowup. Moreover, the centre of T on$X _ { 1 }$is an lc centre of$( X _ { 1 } , \Lambda _ { 1 } )$, hence a stratum of$( X _ { 1 } , \Lambda _ { 1 } )$ We blowup$X _ { 1 }$along the centre of$T$and so on. Thus we get a sequence

$$
Y = X _ {l} \rightarrow \dots \rightarrow X _ {0} = X
$$

of centre blowups obtaining$T$as the exceptional divisor of the last blowup (2.16 (3)). The sequence is toroidal with respect to$( X , \Lambda )$

Since the above sequence starts with blowing up x, and since$( U , \Lambda ^ { \mathrm { a n } } | _ { U } )$and$( V , \Theta ^ { \mathrm { a n } } | _ { V } )$ are analytically isomorphic, the sequence corresponds to a sequence of blowups

$$
W = Z _ {l} \rightarrow \dots \rightarrow Z _ {0} = \mathbb {P} ^ {d}
$$

which is the sequence of centre blowups of$R ,$, the exceptional divisor of$Z _ { l } \to Z _ { l - 1 }$. The latter sequence starts with blowing up z and it is toroidal with respect to$( \mathbb { P } ^ { d } , \Theta )$, hence $a ( R , \mathbb { P } ^ { d } , \Theta ) = 0$. On the other hand, since$( U , B ^ { \mathrm { a n } } | _ { U } )$and$( V , C ^ { \mathrm { a n } } | _ { V } )$are analytically isomorphic, we get

$$
a (R, \mathbb {P} ^ {d}, C) = a (T, X, B) \leq 1.
$$

Note that we cannot simply replace X, B, Λ with$\mathbb { P } ^ { d } , C , \Theta$because we do not know whether$( \mathbb { P } ^ { d } , C )$is ǫ-lc away from$z .$

Step 3. In this step we show that there is a positive real number$t \in ( 0 , \frac { 1 } { 2 } )$depending only on d, r such that$( \mathbb { P } ^ { d } , \Theta + t C )$is lc away from z. Pick a closed point$\boldsymbol { y } \in \mathbb { P } ^ { d }$other than z. If $y$is not contained in Θ, we can apply Lemma 5.4 to find$t > 0$bounded from below away from zero so that$( \mathbb { P } ^ { d } , t C )$is klt, hence$( \mathbb { P } ^ { d } , \Theta + t C )$is klt near$y .$. Now assume y is contained in$\Theta ,$hence it is contained in some stratum G of$( \mathbb { P } ^ { d } , \Theta )$of minimal dimension. Note that G is positive-dimensional and de$\ ^ { \mathrm { { z g } } } _ { H ^ { \prime } } C | _ { G } = \deg _ { H } C \leq r$where$H ^ { \prime }$on G is the restriction of a general hyperplane H. Moreover, G is not inside Supp C, by Step 2. Applying Lemma 5.4 again, we find$t > 0$bounded from below away from zero such that$\left( G , t C | _ { G } \right)$is klt. Thus by inversion of adjunction,$( \mathbb { P } ^ { d } , \Theta + t C )$is lc near$y$because in a neighbourhood of$y$ we have

$$
K _ {G} + t C | _ {G} = (K _ {\mathbb {P} ^ {d}} + \Theta + t C) | _ {G}.
$$

This proves the existence of t.

Step$\it 4 .$Letting$\begin{array} { r } { \epsilon ^ { \prime } = \frac { t } { 2 } \epsilon . } \end{array}$, in this step we construct a boundary$\Delta$such that$( \mathbb { P } ^ { d } , \Delta )$is$\epsilon ^ { \prime } { - } \mathrm { l c } .$ $K _ { \mathbb { P } ^ { d } } \mathrm { + } \Delta \sim _ { \mathbb { R } } 0$, and$a ( R , \mathbb { P } ^ { d } , \Delta ) \leq 1$. We start with an auxiliary boundary$D = ( 1 - \textstyle \frac { t } { 2 } ) \Theta + \frac { t } { 2 } C$ We will show that$( \mathbb { P } ^ { d } , D )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$. Let E be a prime divisor over$\mathbb { P } ^ { d }$and let I be its centre on$\mathbb { P } ^ { d }$. If I passes through$z ,$then by Lemma 2.3,

$$
a (E, \mathbb {P} ^ {d}, D) = (1 - \frac {t}{2}) a (E, \mathbb {P} ^ {d}, \Theta) + \frac {t}{2} a (E, \mathbb {P} ^ {d}, C) \geq \frac {t}{2} \epsilon = \epsilon^ {\prime}
$$

because$( \mathbb { P } ^ { d } , C )$is ǫ-lc near z. So assume$z \not \in I$. In particular, I is not a stratum of$( \mathbb { P } ^ { d } , \Theta )$ because each stratum contains z. Thus I is not an lc centre of$( \mathbb { P } ^ { d } , \Theta )$. Then

$$
a (E, \mathbb {P} ^ {d}, D) \geq a (E, \mathbb {P} ^ {d}, \Theta + \frac {t}{2} C) = \frac {1}{2} a (E, \mathbb {P} ^ {d}, \Theta + t C) + \frac {1}{2} a (E, \mathbb {P} ^ {d}, \Theta) \geq \frac {1}{2} \geq \epsilon^ {\prime}
$$

because$( \mathbb { P } ^ { d } , \Theta + t C )$is lc near I, by Step 3, and because$a ( E , \mathbb { P } ^ { d } , \Theta ) \geq 1$as$E$is not an lc place of$( \mathbb { P } ^ { d } , \Theta )$. Therefore, we have proved$( \mathbb { P } ^ { d } , D )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$

By Step 2,

$$
a (R, \mathbb {P} ^ {d}, D) = (1 - \frac {t}{2}) a (R, \mathbb {P} ^ {d}, \Theta) + \frac {t}{2} a (R, \mathbb {P} ^ {d}, C) = \frac {t}{2} a (R, \mathbb {P} ^ {d}, C) \leq 1.
$$

Moreover, taking t small enough in Step 3 we can assume

$$
- (K _ {\mathbb {P} ^ {d}} + D) = - (1 - \frac {t}{2}) (K _ {\mathbb {P} ^ {d}} + \Theta) - \frac {t}{2} (K _ {\mathbb {P} ^ {d}} + C)
$$

is ample because de$\mathrm { g } _ { H _ { i } } - ( K _ { \mathbb { P } ^ { d } } + \Theta ) = 1$and because

$$
\deg_ {H _ {i}} - (K _ {\mathbb {P} ^ {d}} + C) = d + 1 - \deg_ {H _ {i}} C \geq d + 1 - r.
$$

Therefore, there is a boundary$\Delta \ge D$so that$( \mathbb { P } ^ { d } , \Delta )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$2$K _ { \mathbb { P } ^ { d } } + \Delta \sim _ { \mathbb { R } ^ { \mathrm { ~ 0 ~ } } }$, and $a ( R , \mathbb { P } ^ { d } , \Delta ) \leq 1$

Step 5. In this step we show that there is a bounded number$n \in \mathbb { N }$such that$K _ { \mathbb { P } ^ { d } }$has a klt n-complement$K _ { \mathbb { P } ^ { d } } + \Omega$with$a ( R , \mathbb { P } ^ { d } , \Omega ) \leq 1$. Since$W \to \mathbb { P } ^ { d }$is a sequence of blowups toroidal with respect to$( \mathbb { P } ^ { d } , \Theta )$, it is a sequence of toric blowups and$W$is a toric variety. Let ψ :$W ^ { \prime } \to \mathbb { P } ^ { d }$be the weighted blowup given by$R ,$that is, ψ is an extremal birational contraction contracting a single prime divisor which is the birational transform of R. Let $K _ { W ^ { \prime } } { + } \Delta _ { W ^ { \prime } }$be the pullback of$K _ { \mathbb { P } ^ { d } } + \Delta$. Then$\Delta _ { W ^ { \prime } }$is efective as$a ( R , \mathbb { P } ^ { d } , \Delta ) \leq 1$. Moreover, $- K _ { W ^ { \prime } }$is big by construction.

Now run an MMP on$- K _ { W } ,$and let$W ^ { \prime \prime }$be the resulting model. Then$W ^ { \prime \prime }$is a toric variety, and$- K _ { W ^ { \prime \prime } }$is nef and big. Thus$- K _ { W ^ { \prime \prime } }$defines a contraction$W ^ { \prime \prime } \to W ^ { \prime \prime \prime }$to a toric Fano variety. Moreover, since$( W ^ { \prime } , \Delta _ { W ^ { \prime } } )$is ǫ<sup>′</sup>-lc,$( W ^ { \prime \prime \prime } , \Delta _ { W ^ { \prime \prime \prime } } )$is ǫ<sup>′</sup>-lc too. Thus$W ^ { \prime \prime \prime }$is an $\epsilon ^ { \prime } { - } \mathrm { l c }$toric Fano variety. Now by [9],$W ^ { \prime \prime \prime }$belongs to a bounded family of varieties depending only on$d , \epsilon ^ { \prime }$. Therefore, there is a natural number$n > 1$depending only on$d , \epsilon ^ { \prime }$such that$\vert - n K _ { W ^ { \prime \prime \prime } } \vert$is base point free, in particular,$K _ { W ^ { \prime \prime \prime } }$has an n-complement$K _ { W ^ { \prime \prime \prime } } + \Omega _ { W ^ { \prime \prime \prime } }$ which is klt. This gives an n-complement$K _ { W ^ { \prime \prime } } + \Omega _ { W ^ { \prime \prime } }$of$K _ { W ^ { \prime \prime } }$which in turn gives an n-complement$K _ { W ^ { \prime } } + \Omega _ { W ^ { \prime } }$of$K _ { W ^ { \prime } }$because$W ^ { \prime }  W ^ { \prime \prime }$is an MMP on$- K _ { W ^ { \prime } }$. Then we get an n-complement$K _ { \mathbb { P } ^ { d } } + \Omega$of$K _ { \mathbb { P } ^ { d } }$which is klt. By construction,

$$
a (R, \mathbb {P} ^ {d}, \Omega) = a (R, W ^ {\prime}, \Omega_ {W ^ {\prime}}) \leq 1.
$$

Step 6. In this step we finish the proof by applying Lemma 2.17. Since nΩ is integral and deg$\dot { \bf \Phi } _ { H _ { i } } \Omega = d + 1$, the pair$( \mathbb { P } ^ { d } , \operatorname { S u p p } ( \Omega + \Theta ) )$belongs to a bounded family of pairs depending only on$d , n$. Therefore, there is a positive real number u depending only on$d , n$such that $( \mathbb { P } ^ { d } , \Omega + u \Theta )$is lc. Since$\Omega _ { W ^ { \prime } } \geq 0$, we deduce that the coeficient of the birational transform of R in$\psi ^ { * } \Theta$is at most$\textstyle { \frac { 1 } { u } }$which in turn implies$\begin{array} { r } { \mu _ { R } \phi ^ { * } \Theta \le \frac { 1 } { u } } \end{array}$where$\phi$denotes$W \to \mathbb { P } ^ { d }$. On the other hand, since$W \overset { \vartriangle } {  } \mathbb { P } ^ { d }$is a sequence of centre blowups of R which is toroidal with respect to$( \mathbb { P } ^ { d } , \Theta )$, we have$l + 1 \le \mu _ { R } \phi ^ { * } \Theta$, by Lemma 2.17. Therefore,$\begin{array} { r } { l \le p : = \lfloor \frac { 1 } { u } - 1 \rfloor } \end{array}$

5.6. Bound on multiplicity at an lc place. The next result bounds the multiplicity of divisors at lc places of a pair under suitable assumptions. An example of such boundedness is the boundedness of$\mu _ { R } \phi ^ { * } \Theta$that we obtained in Step 6 of the previous proof.

Proposition 5.7. Let$d , r , n$be natural numbers and ǫ be a positive real number. Assume Theorem 1.8 holds in dimension$\leq d - 1$. Then there is a positive number q depending only on$d , r , n , \epsilon$satisfying the following. Assume

$( X , B )$is a projective ǫ-lc pair of dimension$d ,$

• A is a very ample divisor on X with$A ^ { d } \leq r ,$

$\Lambda \geq 0$is a Q-divisor on X with nΛ integral,

$L \geq 0$is an R-divisor on X,

• the divisors

$$
A - B, A - \Lambda , a n d A - L
$$

are all ample (in particular, we are assuming$B , \Lambda , L$are all$\mathbb { R } \mathrm { - } C a r t i e r )$，

$( X , \Lambda )$is lc near a point x (not necessarily closed),

•$T$is an lc place of$( X , \Lambda )$with centre the closure of x, and

$a ( T , X , B ) \leq 1$

Then for any resolution$\nu \colon U \to X$so that T is a divisor on$U _ { i }$, we have$\mu _ { T } \nu ^ { * } L \leq q$

We first treat a special case of the proposition.

Lemma 5.8. Assume that Proposition 5.7 holds in dimension$d - 1$. Then the proposition holds in dimension d when x is not a closed point.

Proof. Let C be the closure of x. Take a general$H \in | A |$and let

$$
B _ {H} = B | _ {H}, A _ {H} = A | _ {H}, \Lambda_ {H} = \Lambda | _ {H}, \text { and } L _ {H} = L | _ {H}.
$$

Then by adjunction

$$
K _ {H} + B _ {H} = (K _ {X} + B + H) | _ {H} \text { and } K _ {H} + \Lambda_ {H} = (K _ {X} + \Lambda + H) | _ {H}.
$$

Now take a log resolution φ:$W  X$on which T is a divisor and let$G = \phi ^ { * } H$. Pick a component S of$G \cap T$and let R be its image on X. Then R is contained in$H \cap C$. In fact, considering the map$T  C$and taking into account the generality of H, we can assume that R is a component of$H \cap C$

Now we have:

$( H , B _ { H } )$is a projective ǫ-lc pair of dimension$d - 1$

$A _ { H }$is a very ample divisor on H with$A _ { H } ^ { d - 1 } \leq r ,$

$\Lambda _ { H } \geq 0$is a Q-divisor on H with n$\iota \Lambda _ { H }$integral,

$L _ { H } \ge 0$is an R-divisor on H,

• the divisors

$$
A _ {H} - B _ {H}, A _ {H} - \Lambda_ {H}, \mathrm{and} A _ {H} - L _ {H}
$$

are ample,

$( H , \Lambda _ { H } )$is lc near the generic point of R (by the generality of H),

• S is an lc place of$( H , \Lambda _ { H } )$with centre R, and

$a ( S , H , B _ { H } ) \leq 1 .$

The last two points can be seen by considering the pullbacks$K _ { W } + \Lambda _ { W }$and$K _ { W } + B _ { W }$ of$K _ { X } + \Lambda$and$K _ { X } + B$, respectively, and noting that

$$
(K _ {W} + \Lambda_ {W} + G) | _ {G} \mathrm{and} (K _ {W} + B _ {W} + G) | _ {G}
$$

are the pullbacks of

$$
K _ {H} + \Lambda_ {H} \mathrm{and} K _ {H} + B _ {H}
$$

respectively, and that$\mu _ { T } \Lambda _ { W } = 1$while$\mu _ { T } B _ { W } \geq 0 .$

Denote the induced contraction$G  H$by σ. Since we are assuming that Proposition 5.7 holds in dimension$d - 1$, the coeficient of S in$\sigma ^ { * } ( L _ { H } ) = ( \phi ^ { * } L ) | _ { G }$is bounded from above which implies the coeficient of$T$in$\phi ^ { * } L$is bounded from above too. Finally note that$\mu _ { T } \phi ^ { * } L = \mu _ { T } \nu ^ { * } L$for any resolution$\nu \colon U \to X$on which T is a divisor.

Lemma 5.9. Assume that Proposition 5.7 holds in dimension$d - 1$. Then the proposition holds in dimension d when$( X , \Lambda )$is log smooth and Λ is reduced.

Proof. We will assume$d > 1$as the case$d = 1$holds trivially. We will use Lemma 5.8 so that we can assume x is a closed point. The idea is then to apply Proposition 5.5. For this we need to modify the setting so that Supp B does not contain any stratum of$( X , \Lambda )$other than x, and this occupies much of the proof.

Step 1. In this step we reduce the proposition to the case in which x is a closed point and that$( X , \Lambda )$has no other zero-dimensional stratum. Applying Lemma 5.8, we can indeed assume that x is a closed point. Assume$( X , \Lambda )$has another zero-dimensional stratum $y \neq x .$Let$X ^ { \prime }  X$be the blowup of X at y and$E ^ { \prime }$be the exceptional divisor. Let $K _ { X ^ { \prime } } + B ^ { \prime } , K _ { X ^ { \prime } } + \Lambda ^ { \prime } , L ^ { \prime }$, be the pullbacks of$K _ { X } + B , K _ { X } + \Lambda , L$, respectively. Then

$$
\mu_ {E ^ {\prime}} B ^ {\prime} \geq - d + 1 \text { and } \mu_ {E ^ {\prime}} \Lambda^ {\prime} = 1.
$$

We can pick a very ample divisor$A ^ { \prime }$on$X ^ { \prime }$with bounded$A ^ { \prime d }$such that

$$
A ^ {\prime} - B ^ {\prime}, A ^ {\prime} - \Lambda^ {\prime}, A ^ {\prime} - L ^ {\prime}
$$

are all ample.

Now there is$\beta \in ( 0 , 1 )$depending only on d such that

$$
B ^ {\prime \prime} := \beta B ^ {\prime} + (1 - \beta) \Lambda^ {\prime} \geq 0.
$$

Let$\Lambda ^ { \prime \prime }$be the birational transform of Λ and let$\epsilon ^ { \prime } = \epsilon \beta$. Replacing$A ^ { \prime }$with a bounded multiple we can assume

$$
A ^ {\prime} - B ^ {\prime \prime}, A ^ {\prime} - \Lambda^ {\prime \prime}, A ^ {\prime} - L ^ {\prime}
$$

are all ample, by definition of$B ^ { \prime \prime } , \Lambda ^ { \prime \prime }$

Note that each stratum of$( X ^ { \prime } , \Lambda ^ { \prime \prime } )$is the birational transform of a stratum of$( X , \Lambda )$ Now replacing$X , B , A , \Lambda , L , \epsilon$with$\dot { X ^ { \prime } } , B ^ { \prime \prime } , A ^ { \prime } , \Lambda ^ { \prime \prime } , L ^ { \prime } , \epsilon ^ { \prime } .$, and replacing r appropriately, we can remove one of the zero-dimensional strata of$( X , \Lambda )$other than x. Repeating this process a bounded number of times, we get to the situation in which$( X , \Lambda )$has no zerodimensional stratum other than x.

Step 2. In this step we find a positive real number t depending only on$d , r , \epsilon$such that $( X , B + t B )$is <sup>ǫ</sup> -lc outside finitely many closed points. Let H be a general element of$| A |$ and let$A _ { H } = \tilde { A | _ { H } } , B _ { H } = B | _ { H }$, and$L _ { H } = L | _ { H }$. Then

$( H , B _ { H } )$is a projective ǫ-lc pair of dimension$d - 1$

$A _ { H }$is a very ample divisor on H with$A _ { H } ^ { d - 1 } \leq r ,$and

$A _ { H } - B _ { H }$is ample.

Thus since we are assuming Theorem 1.8 in dimension$\leq d - 1$, we find a positive real number t depending only on$d , r , \epsilon$such that$( H , B _ { H } + 2 t B _ { H } )$is klt. This implies that $( X , H + B + 2 t B )$is plt in a neighbourhood of H, by inversion of adjunction [28, Theorem 5.50] (note that [28, Theorem 5.50] assumes B to be a Q-divisor but the conclusion holds for R-divisors as well). Therefore,$( X , B + 2 t B )$is klt near H, hence$( X , B + 2 t B )$is klt outside finitely many closed points because H being general very ample it intersects every positive dimensional subvariety of X. In particular,$( X , B + t B )$is <sup>ǫ</sup><sub>2</sub> -lc outside these finitely many closed points, by Lemma 2.3, because

$$
K _ {X} + B + t B = \frac {1}{2} (K _ {X} + B) + \frac {1}{2} (K _ {X} + B + 2 t B)
$$

and because$( X , B )$is$\epsilon { - } \mathrm { l c }$

Step 3. In this step we take a resolution and introduce a boundary$\Gamma _ { V }$. Let$\psi \colon V \to X$ be a log resolution of$( X , B )$on which T is a divisor. Define a boundary

$$
\Gamma_ {V} = (1 + t) B ^ {\sim} + (1 - \frac {\epsilon}{4}) \sum E _ {i} + (1 - a) T
$$

where$E _ { i }$are the exceptional divisors of ψ other than T,$a = a ( T , X , B )$, and ∼ denotes birational transform. Let$a _ { i } = a ( E _ { i } , X , B )$. Since$( X , B )$is ǫ-lc and since$\mu _ { T } \Gamma _ { V } = 1 - a .$2 we have

$$
\begin{array}{c} K _ {V} + \Gamma_ {V} = K _ {V} + B ^ {\sim} + \sum (1 - a _ {i}) E _ {i} + (1 - a) T + t B ^ {\sim} + \sum (a _ {i} - \frac {\epsilon}{4}) E _ {i} \\ = \psi^ {*} (K _ {X} + B) + t B ^ {\sim} + F \end{array}
$$

where

$$
F := \sum (a _ {i} - \frac {\epsilon}{4}) E _ {i}
$$

is efective and exceptional over X and its support does not contain T. On the other hand, if

$$
a ^ {\prime} = a (T, X, B + t B) \text { and } a _ {i} ^ {\prime} = a (E _ {i}, X, B + t B),
$$

then we can write

$$
\begin{array}{r l} & K _ {V} + \Gamma_ {V} = K _ {V} + (1 + t) B ^ {\sim} + \sum (1 - a _ {i} ^ {\prime}) E _ {i} + (1 - a ^ {\prime}) T + \sum (a _ {i} ^ {\prime} - \frac {\epsilon}{4}) E _ {i} + (a ^ {\prime} - a) T \\ & \qquad = \psi^ {*} (K _ {X} + (1 + t) B) + G \end{array}
$$

where

$$
G := \sum (a _ {i} ^ {\prime} - \frac {\epsilon}{4}) E _ {i} + (a ^ {\prime} - a) T
$$

is exceptional over X. Moreover, if the image of$E _ { i }$on X is positive-dimensional for some $i ,$then$E _ { i }$is a component of$G$with positive coeficient because$( X , B + t B )$is <sup>ǫ</sup><sub>2</sub> -lc outside finitely many closed points.

Step 4. In this step we run an MMP on$K _ { V } + \Gamma _ { V }$over X and study its outcome. By construction,$( V , \Gamma _ { V } )$is klt. Run an MMP on$K _ { V } + \Gamma _ { V }$over X, let$Y$be the resulting model, and$\pi \colon Y  X$the corresponding morphism. Since$K _ { V } + \Gamma _ { V } \equiv G / X$and G is exceptional/X, the MMP contracts every component of G with positive coeficient, by the negativity lemma. Thus$\pi$is an isomorphism over the complement of finitely many closed points: indeed, by the last sentence of the previous step every$E _ { i }$with positive-dimensional centre on X is a component of G with positive coeficient so these are all contracted; also note that X is smooth by assumption so it is Q-factorial, hence the claim. Moreover, since

$$
K _ {V} + \Gamma_ {V} \equiv t B ^ {\sim} + F / X
$$

and since$T$is not a component of$t B ^ { \sim } + F$, we see that$T$is not contracted by the MMP.

Step 5. In this step we introduce a divisor$D _ { Y }$. Let$A _ { Y }$be the pullback of A to$Y .$ By boundedness of the length of extremal rays [21] and by the base point free theorem, $K _ { Y } + \Gamma _ { Y } + 3 d A _ { Y }$is nef and big and semi-ample, globally. Pick a general

$$
0 \leq D _ {Y} \sim_ {\mathbb {R}} \frac {1}{t} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y})
$$

with coeficients$\leq 1 - \epsilon$. By Step 3,

$$
K _ {Y} + \Gamma_ {Y} = \pi^ {*} (K _ {X} + B) + t B _ {Y} ^ {\sim} + F _ {Y},
$$

where$B _ { Y } ^ { \sim } , F _ { Y }$denote the pushdowns of$B ^ { \sim } , F$, respectively. Thus we get

$$
\frac {1}{t} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y}) = \frac {1}{t} \pi^ {*} (K _ {X} + B + 3 d A) + B _ {Y} ^ {\sim} + \frac {1}{t} F _ {Y}.
$$

Then we can write

$$
D _ {Y} = \pi^ {*} H + B _ {Y} ^ {\sim} + \frac {1}{t} F _ {Y}
$$

for some

$$
H \sim_ {\mathbb {R}} \frac {1}{t} (K _ {X} + B + 3 d A).
$$

Letting D be the pushdown of$D _ { Y }$to$X$, we get$D = H + B ,$

Step 6. In this step replacing B with D we reduce the proposition to the situation in which Supp B does not contain any stratum of$( X , \Lambda )$other than x. First we show that $( X , D )$is ǫ-lc. Write

$$
K _ {Y} + B _ {Y} ^ {\sim} + R _ {Y} = \pi^ {*} (K _ {X} + B)
$$

where$R _ { Y }$is exceptional over X. We then have

$$
\begin{array}{c} K _ {Y} + R _ {Y} + D _ {Y} - \frac {1}{t} F _ {Y} = K _ {Y} + R _ {Y} + B _ {Y} ^ {\sim} + \pi^ {*} H \\ = \pi^ {*} (K _ {X} + B + H) = \pi^ {*} (K _ {X} + D). \end{array}
$$

Since (X, B) is ǫ-lc,$( Y , B ^ { \sim } + R _ { Y } )$is sub-ǫ-lc, hence

$$
(Y, R _ {Y} + D _ {Y} - \frac {1}{t} F _ {Y})
$$

is sub-ǫ-lc because$D _ { Y }$is general semi-ample with coeficients$\leq 1 - \epsilon$and$F _ { Y } \geq 0$. Therefore, $( X , D )$is ǫ-lc. Moreover, since$T$is not a component of$B _ { Y } ^ { \sim } + F _ { Y } + D _ { Y }$

$$
\begin{array}{c} a (T, X, D) = 1 - \mu_ {T} (R _ {Y} + D _ {Y} - \frac {1}{t} F _ {Y}) = 1 - \mu_ {T} R _ {Y} \\ = 1 - \mu_ {T} (B ^ {\sim} + R _ {Y}) = a (T, X, B) \leq 1. \end{array}
$$

On the other hand, since

$$
D \sim_ {\mathbb {R}} \frac {1}{t} (K _ {X} + B + 3 d A) + B,
$$

there is a natural number m depending only on$d , r , t ,$so depending only on$d , r , \epsilon .$such that

$$
3 m A - D \sim_ {\mathbb {R}} \left(m A - \frac {1}{t} K _ {X}\right) + \left(m A - \frac {3 d}{t} A\right) + \left(m A - \frac {1 + t}{t} B\right)
$$

is ample because we can ensure that each bracket is an ample divisor.

Since π is an isomorphism over the complement of finitely many closed points and since $D _ { Y }$is semi-ample, we can assume that Supp D does not contain any positive-dimensional stratum of$( X , \Lambda )$. Replacing B with$D$, and then replacing A with 3mA and replacing r accordingly, we can assume that Supp B does not contain any positive-dimensional stratum of$( X , \Lambda )$. Since x is the only zero-dimensional stratum of$( X , \Lambda )$, by Step 1, Supp B does not contain any stratum other than x.

Step 7. In this step we apply Proposition 5.5 and finish the proof. All the assumptions of Proposition 5.5 are satisfied in our setting, so there is a natural number p depending only on$d , r , \epsilon$such that$T$can be obtained by a sequence of centre blowups

$$
\nu \colon U = X _ {l} \to \dots \to X _ {0} = X,
$$

toroidal with respect to$( X , \Lambda )$, and of length$l \leq p$

Since$( X , \Lambda )$belongs to a bounded family of pairs, one can show inductively that all the $X _ { i }$are bounded. Moreover, we can assume that there is a very ample divisor J on U such that$J ^ { d }$is bounded from above depending only on$d , r , \epsilon$and that$J - \nu ^ { * } A$is ample. In particular, since$\nu ^ { * } A - \nu ^ { * } L$is nef,$J - \nu ^ { * } L$is ample. Therefore, there is a natural number q depending only on$d , r , \epsilon$such that

$$
\mu_ {T} \nu^ {*} L \leq \deg_ {J} \nu^ {*} L \leq J ^ {d} \leq q.
$$

Thus$\mu _ { T } \nu ^ { * } L \leq q$if we replace ν with any other resolution on which$T$is a divisor.

Proof. (of Proposition 5.7) Applying induction on dimension we can assume that the proposition holds in dimension$\leq d - 1$. Let$X , B , A , L , \Lambda ,$x be as in the proposition in dimension d. Replacing A we can assume it is efective and that$A - \left( K _ { X } + B \right)$is ample (we use the latter below). Since$A - \Lambda$is ample, deg$_ { A } \Lambda < A ^ { d } \leq r$. Thus since$n \Lambda$is integral, the couple $( X , { \mathrm { S u p p } } ( \Lambda + A ) )$belongs to a bounded family of couples$\mathcal { P }$depending only on$d , r , n$. Then there exists a log bounded family Q of log smooth pairs depending only on$d , r ,$n such that there exist a log resolution$\phi \colon W \to X$of$( X , \Lambda )$and a very ample divisor$A _ { W } \geq 0$so that

• if$\Theta _ { W }$is the sum of the exceptional divisors of$\phi$and the support of the birational transform of$\Lambda ,$then$( W , \Theta _ { W } + A _ { W } )$belongs to$\mathcal { Q } .$

$A _ { W } - \Theta _ { W }$and$A _ { W } - \phi ^ { * } A$are ample.

In particular, this means that$A _ { W } ^ { d }$is bounded from above.

Let$K _ { W } + \Lambda _ { W }$be the pullback of$K _ { X } + \Lambda$. Since$( X , \Lambda )$is lc near x,$\Lambda _ { W } \leq \Theta _ { W }$over some neighbourhood of$x ,$hence

$$
0 = a (T, X, \Lambda) = a (T, W, \Lambda_ {W}) \geq a (T, W, \Theta_ {W}) \geq 0
$$

which shows that$T$is an lc place of$( W , \Theta _ { W } )$. Moreover, if C is the centre of$T$on$W$and if w is its generic point, then$\Lambda _ { W } = \Theta _ { W }$near w.

Let$K _ { W } + B _ { W }$be the pullback of$K _ { X } + B$. We claim that the coeficients of$B _ { W }$are bounded from below. Writing$K _ { W } + J _ { W } = \phi ^ { * } K _ { X }$, we see that$J _ { W } \le B _ { W }$, so it is enough to show that the coeficients of$J _ { W }$are bounded from below. Note that since both$K _ { X } + B$and B are R-Cartier by assumption,$K _ { X }$is$\mathbb { Q } \mathrm { { - } C a r t i e r }$, so$\phi ^ { * } K _ { X }$makes sense. Since$( X , { \mathrm { S u p p } } \Lambda )$ belongs to bounded family of couples, we can indeed choose$\phi$so that the coeficients of$J _ { W }$ belong to a fixed finite set, hence in particular they are bounded from below.

Now there is a fixed$\alpha \in ( 0 , 1 )$such that

$$
\Delta_ {W} := \alpha B _ {W} + (1 - \alpha) \Theta_ {W} \geq 0
$$

because the coeficients of$B _ { W }$are bounded from below and each exceptional$/ X$prime divisor has coeficient 1 in$\Theta _ { W }$

Let$\delta = \alpha \epsilon$. Since$( W , B _ { W } )$is sub-ǫ-lc and$( W , \Theta _ { W } )$is lc, the pair$( W , \Delta _ { W } )$is$\delta { \mathrm { - l c } } .$by Lemma 2.3. Moreover, since

$$
a (T, W, \Theta_ {W}) = 0,
$$

we have

$$
\begin{array}{c} a (T, W, \Delta_ {W}) = \alpha a (T, W, B _ {W}) + (1 - \alpha) a (T, W, \Theta_ {W}) \\ = \alpha a (T, W, B _ {W}) = \alpha a (T, X, B) \leq 1. \end{array}
$$

On the other hand, by the above and by assumption,$A _ { W } - \Theta _ { W }$is ample, and$\phi ^ { * } A -$ $( K _ { W } + B _ { W } )$and$\phi ^ { * } A - L _ { W }$are nef where$L _ { W }$is the pullback of L. Since$A _ { W } - \phi ^ { * } A$is ample, we deduce that$A _ { W } - ( K _ { W } + B _ { W } )$and$A _ { W } - L _ { W }$are ample. Moreover, replacing $A _ { W }$with a bounded multiple we can assume that${ \textstyle { \frac { 1 } { 2 } } } A _ { W } + K _ { W }$and${ \textstyle { \frac { 1 } { 2 } } } A _ { W } - ( K _ { W } + B _ { W } )$are ample. In particular,$A _ { W } - B _ { W }$is ample, hence

$$
A _ {W} - \Delta_ {W} = \alpha (A _ {W} - B _ {W}) + (1 - \alpha) (A _ {W} - \Theta_ {W})
$$

is ample too.

Now after replacing ǫ with δ and replacing r appropriately, we can replace$X , B , A , L ,$ $\Lambda , x$with$W , \Delta _ { W } , A _ { W } , L _ { W } , \Theta _ { W } , w$, respectively. In particular, we can assume that$( X , \Lambda )$ is log smooth with Λ reduced. We are then done by Lemma 5.9.

5.10. Construction of Λ. We want to apply Proposition 5.7 to prove Theorem 1.8. The proposition assumes existence of an extra divisor Λ which helps to eventually reduce the problem to the case of toric varieties via 5.5. Next, we will use complements (as in Theorem 1.9) to get the required divisor Λ.

Proposition 5.11. Let$d , r$be natural numbers and ǫ be a positive real number. Assume Theorem 1.8 holds in dimension$\leq d - 1$. Then there exist natural numbers n, m and a positive real number$\epsilon ^ { \prime } < \epsilon$depending only on$d , r , \epsilon$satisfying the following. Assume

$( X , B )$is a projective ǫ-lc pair of dimension$d ,$

$A$is a very ample divisor on X with$A ^ { d } \leq r ,$

$L \geq 0$is an R-divisor on X,

$A - B$and$A - L$are ample (so we are assuming that B and L are$\mathbb { R } \mathrm { - } C a r t i e r )$

$( X , B + t L )$is ǫ<sup>′</sup>-lc for some$t \in ( 0 , r )$

• we have

$$
a (T, X, B + t L) = \epsilon^ {\prime}
$$

for some prime divisor T over X, and

• the centre of T on X is a closed point x.

Then there is a Q-Cartier Q-divisor$\Lambda \geq 0$such that

$n \Lambda$is integral,

$m A - \Lambda$is ample,

$( X , \Lambda )$is lc near x, and

• T is an lc place of$( X , \Lambda )$

Proof. We can assume that$d > 1$as the proposition holds trivially in dimension one. On the other hand, by the ACC for lc thresholds [13], there exists a real number$\epsilon ^ { \prime } \in ( 0 , \epsilon )$ depending only on$d ,$so that if$( Y , ( 1 - \epsilon ^ { \prime } ) S )$is a klt pair of dimension d where$S$is reduced and Q-Cartier, then$( Y , S )$is lc. Let$X , B , A , L , T , t$t be as in the proposition with$\epsilon ^ { \prime }$as in the previous sentence.

Step 1. In this step we find a positive real number v depending only on$d , r , \epsilon$such that

$$
(X, B + t L + v (B + t L))
$$

is$\frac { \epsilon ^ { \prime } } { 2 } \mathrm { - l c }$outside finitely many closed points. Since$t < r .$2

$$
(r + 1) A - B - t L = A - B + t (A - L) + (r - t) A
$$

is ample, so replacing A with$( r + 1 ) A$and replacing r accordingly we can assume that $A - B - t L$is ample.

Let H be a general element of |A| and let$A _ { H } = A | _ { H } , B _ { H } = B | _ { H }$, and$L _ { H } = L | _ { H }$. Then

$( H , B _ { H } + t L _ { H } )$is a projective ǫ<sup>′</sup>-lc pair of dimension$d - 1$

$A _ { H }$is a very ample divisor on H with$A _ { H } ^ { d - 1 } \leq r$, and

$A _ { H } - B _ { H } - t L _ { H }$is ample.

Thus since we are assuming Theorem 1.8 in dimension$\leq d - 1$, we find a positive real number v depending only on$d , r , \epsilon ^ { \prime }$such that

$$
(H, B _ {H} + t L _ {H} + 2 v (B _ {H} + t L _ {H}))
$$

is klt. As$\epsilon ^ { \prime }$was picked depending only on$d ,$we can choose v depending only on$d , r , \epsilon .$ Now

$$
(X, H + B + t L + 2 v (B + t L))
$$

is plt in a neighbourhood of$H _ { ; }$by inversion of adjunction [28, Theorem 5.50]. Therefore,

$$
(X, B + t L + 2 v (B + t L))
$$

is klt near$H$, hence it is klt outside finitely many closed points. In particular,

$$
(X, B + t L + v (B + t L))
$$

is$\frac { \epsilon ^ { \prime } } { 2 } \mathrm { - l c }$outside finitely many closed points, by Lemma 2.3, because

$$
K _ {X} + B + t L + v (B + t L) = \frac {1}{2} (K _ {X} + B + t L) + \frac {1}{2} (K _ {X} + B + t L + 2 v (B + t L))
$$

and because$( X , B + t L )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$

Step 2. In this step we take a log resolution$W  X$and define a boundary Γ<sub>W</sub> and study some of its properties. Let ψ :$W  X$be a log resolution of$( X , B + t L )$so that$T$ is a divisor on$W$. Define a boundary

$$
\Gamma_ {W} = (1 + v) (B ^ {\sim} + t L ^ {\sim}) + (1 - \frac {\epsilon^ {\prime}}{4}) \sum E _ {i} + (1 - \epsilon^ {\prime}) T
$$

where$E _ { i }$are the exceptional divisors of ψ other than$T _ { i }$and ∼ denotes birational transform. Let

$$
c _ {i} = a (E _ {i}, X, B + t L).
$$

Since

$$
\epsilon^ {\prime} = a (T, X, B + t L),
$$

we can write

$$
\begin{array}{r} K _ {W} + \Gamma_ {W} = K _ {W} + B ^ {\sim} + t L ^ {\sim} + \sum (1 - c _ {i}) E _ {i} + (1 - \epsilon^ {\prime}) T + v (B ^ {\sim} + t L ^ {\sim}) + \sum (c _ {i} - \frac {\epsilon^ {\prime}}{4}) E _ {i} \\ = \psi^ {*} (K _ {X} + B + t L) + v (B ^ {\sim} + t L ^ {\sim}) + F \end{array}
$$

where

$$
F := \sum (c _ {i} - \frac {\epsilon^ {\prime}}{4}) E _ {i}
$$

is exceptional over X and its support does not contain T. Moreover, since$( X , B + t L )$is $\epsilon ^ { \prime } { - } \mathrm { l c } ,$we have$c _ { i } \geq \epsilon ^ { \prime }$for every$i ,$so$F$is efective.

On the other hand, letting

$$
c _ {i} ^ {\prime} = a (E _ {i}, X, (1 + v) (B + t L))
$$

and

$$
a ^ {\prime} = a (T, X, (1 + v) (B + t L))
$$

we can write

$$
\begin{array}{c} K _ {W} + \Gamma_ {W} = K _ {W} + (1 + v) (B ^ {\sim} + t L ^ {\sim}) + \sum (1 - c _ {i} ^ {\prime}) E _ {i} + (1 - a ^ {\prime}) T + \sum (c _ {i} ^ {\prime} - \frac {\epsilon^ {\prime}}{4}) E _ {i} + (a ^ {\prime} - \epsilon^ {\prime}) T \\ = \psi^ {*} (K _ {X} + (1 + v) (B + t L)) + G \end{array}
$$

where

$$
G := \sum (c _ {i} ^ {\prime} - \frac {\epsilon^ {\prime}}{4}) E _ {i} + (a ^ {\prime} - \epsilon^ {\prime}) T
$$

is exceptional over X. Moreover, since

$$
(X, (1 + v) (B + t L))
$$

is$\frac { \epsilon ^ { \prime } } { 2 } \mathrm { - l c }$outside finitely many closed points, if the image of$E _ { i }$on X is positive-dimensional for some$i ,$then$\begin{array} { r } { c _ { i } ^ { \prime } \geq \frac { \epsilon ^ { \prime } } { 2 } } \end{array}$so$E _ { i }$is a component of G with positive coeficient.

Step 3. In this step we run an MMP on$K _ { W } + \Gamma _ { W }$over X and argue that it does not contract$T$. By construction,$( W , \Gamma _ { W } )$is klt; here we are using the fact that the coeficients of$( 1 + v ) ( B ^ { \sim } + t L ^ { \sim } )$are less than 1 because

$$
(X, (1 + v) (B + t L))
$$

is$\frac { \epsilon ^ { \prime } } { 2 } -$lc outside finitely many closed points.

Run an MMP on$K _ { W } + \Gamma _ { W }$over$X$and let$Y ^ { \prime }$be the resulting model. Since$K _ { W } + \Gamma _ { W } \equiv$ $G / X$and since$G$is exceptional over X by Step 2, applying the negativity lemma shows that the MMP contracts every component of$G$with positive coeficient. In particular, every$E _ { i }$with positive-dimensional image on$X$is contracted, by Step 2. Thus the induced morphism$Y ^ { \prime }  X$is a small morphism over the complement of finitely many closed points. On the other hand, by Step 2,

$$
K _ {W} + \Gamma_ {W} \equiv v (B ^ {\sim} + t L ^ {\sim}) + F / X
$$

and$T$is not a component of

$$
v (B ^ {\sim} + t L ^ {\sim}) + F \geq 0,
$$

so the MMP does not contract T.

Let$A _ { Y ^ { \prime } }$be the pullback of A. By boundedness of the length of extremal rays [21] and by the base point free theorem,$K _ { Y ^ { \prime } } + \Gamma _ { Y ^ { \prime } } + 2 d A _ { Y ^ { \prime } }$is semi-ample, globally. Note that over the complement of a finite set of closed points on$X , K _ { Y ^ { \prime } } + \Gamma _ { Y ^ { \prime } } + 2 d A _ { Y ^ { \prime } }$is the pullback of

$$
K _ {X} + (1 + v) (B + t L) + 2 d A.
$$

Step$\it 4 .$In this step we consider a model$Y$on which$- T _ { Y }$is ample over X. Since $( X , B + t L )$is$\epsilon ^ { \prime } { - } \mathrm { l c }$and

$$
a (T, X, B + t L) = \epsilon^ {\prime} <   1,
$$

there is a birational contraction$Y ^ { \prime \prime }  X$extracting$T$but no other divisor where$Y ^ { \prime \prime }$is normal and Q-factorial. We denote the centre of$T$on$Y ^ { \prime \prime }$by$T _ { Y ^ { \prime \prime } }$. Then$Y ^ { \prime \prime }$is of Fano type over$X ,$so there is an ample model Y of$- T _ { Y ^ { \prime \prime } }$over$X { \mathrm { : } }$: that${ \mathrm { i s } } ,$we run an MMP on$- T _ { Y ^ { \prime \prime } }$ to get a semi-ample over$X$divisor and then take the associated contraction to get$Y$. The induced birational morphism$\phi \colon Y  X$contracts$T _ { Y }$but no other divisors and any curve contracted by$\phi$is inside$T _ { Y } { \mathrm { ~ a s ~ } } - T _ { Y }$is ample over$X .$. In particular, since$T _ { Y }$is mapped to $x ,$φ is an isomorphism over the complement of x in$X$. By construction, the induced map $Y \mathrm { ~ -- }  Y ^ { \prime }$does not contract any divisor.

Step 5. In this step we show that$K _ { Y } + \Gamma _ { Y } + 3 d A _ { Y }$is ample where$K _ { Y } + \Gamma _ { Y } , A _ { Y }$are the pushdowns of$K _ { Y ^ { \prime } } + \Gamma _ { Y ^ { \prime } } , A _ { Y ^ { \prime } }$. First note that, by Step 2,

$$
K _ {Y} + \Gamma_ {Y} \sim_ {\mathbb {R}} G _ {Y} = (a ^ {\prime} - \epsilon^ {\prime}) T _ {Y} / X
$$

which in particular means that$K _ { Y } + \Gamma _ { Y }$is R-Cartier. It is obvious that$A _ { Y }$is Q-Cartier. Thus$K _ { Y } + \Gamma _ { Y } + 3 d A _ { Y }$is R-Cartier.

Since

$$
a (T, X, B) \geq \epsilon > \epsilon^ {\prime} = a (T, X, B + t L)
$$

we get

$$
\mu_ {T _ {Y}} \phi^ {*} t L \geq \epsilon - \epsilon^ {\prime} > 0.
$$

Thus

$$
a ^ {\prime} = a (T, X, (1 + v) (B + t L)) <   \epsilon^ {\prime} = a (T, X, B + t L).
$$

Therefore, from

$$
K _ {Y} + \Gamma_ {Y} + 2 d A _ {Y} \sim_ {\mathbb {R}} (a ^ {\prime} - \epsilon^ {\prime}) T _ {Y} / X
$$

we deduce that$K _ { Y } + \Gamma _ { Y } + 2 d A _ { Y }$is ample over X because$- T _ { Y }$is ample over$X .$

Now let C be a curve on Y that is not contracted over X. Let c be a general closed point of C. By Steps 2 and 3,

$$
K _ {Y ^ {\prime}} + \Gamma_ {Y ^ {\prime}} + 2 d A _ {Y ^ {\prime}} \sim_ {\mathbb {R}} G _ {Y ^ {\prime}} / X
$$

and$G _ { Y ^ { \prime } } = 0$over the complement of finitely many closed points. Thus since$K _ { Y ^ { \prime } } + \Gamma _ { Y ^ { \prime } } +$ $2 d A _ { Y ^ { \prime } }$is semi-ample by Step 3 and since it is${ \sim _ { \mathbb { R } } } 0$over a neighbourhood of$\phi ( c )$, we can find

$$
0 \leq P _ {Y ^ {\prime}} \sim_ {\mathbb {R}} K _ {Y ^ {\prime}} + \Gamma_ {Y ^ {\prime}} + 2 d A _ {Y ^ {\prime}}
$$

such that$P _ { Y ^ { \prime } }$does not intersect the fibre of$Y ^ { \prime }  X$over$\phi ( c )$. So the pushdown of$P _ { Y ^ { \prime } }$to $X$does not contain$\phi ( c )$. On the other hand, by Step$4 , \phi \colon Y \to X$is an isomorphism over $\phi ( c )$, so$P _ { Y }$does not contain c where$P _ { Y }$is the pushdown of$P _ { Y } ,$to$Y$. Then

$$
\left(K _ {Y} + \Gamma_ {Y} + 2 d A _ {Y}\right) \cdot C = P _ {Y} \cdot C \geq 0.
$$

Therefore,$K _ { Y } + \Gamma _ { Y } + 2 d A _ { Y }$is nef globally while being ample over$X$. Since$A _ { Y }$is the pullback of the ample divisor$A ,$it follows that$K _ { Y } + \Gamma _ { Y } + 3 d A _ { Y }$is ample.

Step$\it 6 .$In this step we show that there is a natural number l depending only on$d , r , \epsilon$ such that

$$
l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y})
$$

is ample. Since

$$
a (T, X, B + t L) = \epsilon^ {\prime},
$$

we have

$$
K _ {Y} + B _ {\widetilde {Y}} ^ {\sim} + t L _ {\widetilde {Y}} ^ {\sim} + (1 - \epsilon^ {\prime}) T _ {Y} = \phi^ {*} (K _ {X} + B + t L),
$$

where$B _ { Y } ^ { \sim } , L _ { Y } ^ { \sim }$are the pushdowns of$B ^ { \sim } , L ^ { \sim }$. Hence for any l we have

$$
l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y}) = l A _ {Y} - \phi^ {*} (K _ {X} + B + t L) + B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim}
$$

$$
= (l - \frac {3 d}{v}) A _ {Y} - (1 + \frac {1}{v}) \phi^ {*} (K _ {X} + B + t L) + \frac {1}{v} \phi^ {*} (K _ {X} + B + t L) + B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim} + \frac {3 d}{v} A _ {Y}.
$$

This in particular shows that

$$
l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y})
$$

is R-Cartier because$B _ { Y } ^ { \sim } , L _ { Y } ^ { \sim }$are R-Cartier which in turn follow from the fact that$\phi ^ { * } B , \phi ^ { * } L , T _ { Y }$ are all R-Cartier.

By assumption,$A - B$and$A - L$are ample. Moreover, since A is very ample and$A ^ { d } \leq r$2 $\beta A - K _ { X }$is ample for some bounded natural number$\beta$depending only on$d , r$. Thus we can choose l depending only on$d , r , \epsilon$so that

$$
(l - \frac {3 d}{v}) A _ {Y} - (1 + \frac {1}{v}) \phi^ {*} (K _ {X} + B + t L) = \phi^ {*} ((l - \frac {3 d}{v}) A - (1 + \frac {1}{v}) (K _ {X} + B + t L))
$$

is nef where we also used the assumption$t \leq r$and that$v , \beta$depend only on$d , r , \epsilon .$. On the other hand, by Step 2 and the fact that$F$is contracted over$Y$

$$
K _ {Y} + \Gamma_ {Y} = \phi^ {*} (K _ {X} + B + t L) + v (B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim}),
$$

hence by Step 5,

$$
\frac {1}{v} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y}) = \frac {1}{v} \phi^ {*} (K _ {X} + B + t L) + B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim} + \frac {3 d}{v} A _ {Y}
$$

is ample. Therefore,

$$
l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y})
$$

is ample by the previous paragraph.

Step 7. In this step we show that after replacing l with a bounded multiple we can ensure that$l A _ { Y } - ( K _ { Y } + T _ { Y } )$is ample. By Step 5, we have$\mu _ { T _ { Y } } \phi ^ { * } t L \geq \epsilon - \epsilon ^ { \prime } .$. Thus there is a positive real number$\begin{array} { r } { \alpha \le \frac { \epsilon ^ { \prime } } { \epsilon - \epsilon ^ { \prime } } } \end{array}$such that

$$
\alpha \mu_ {T _ {Y}} \phi^ {*} (B + t L) = \epsilon^ {\prime}.
$$

Then

$$
\alpha \phi^ {*} (B + t L) = \alpha (B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim}) + \epsilon^ {\prime} T _ {Y}.
$$

Thus we have

$$
\begin{array}{c} 3 l A _ {Y} - (K _ {Y} + T _ {Y}) = 3 l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y}) - \epsilon^ {\prime} T _ {Y} \\ = 3 l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y}) - \alpha \phi^ {*} (B + t L) + \alpha (B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim}) \\ = (l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y})) + (l A _ {Y} - \alpha \phi^ {*} (B + t L)) + (l A _ {Y} + \alpha (B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim})). \end{array}
$$

We argue that we can replace l with a bounded multiple so that$3 l A _ { Y } - \left( K _ { Y } + T _ { Y } \right)$is ample. By Step 6,

$$
l A _ {Y} - (K _ {Y} + (1 - \epsilon^ {\prime}) T _ {Y})
$$

is ample. Moreover, if

$$
l \geq \frac {(1 + r) \epsilon^ {\prime}}{\epsilon - \epsilon^ {\prime}},
$$

then$l \geq ( 1 + t ) \alpha .$, hence

$$
l A _ {Y} - \alpha \phi^ {*} (B + t L)
$$

is nef because

$$
l A - \alpha (B + t L) = (l - (1 + t) \alpha) A + \alpha (A - B + t A - t L)
$$

is ample. In addition, by Step 6, we can write

$$
\begin{array}{r l} & {l A _ {Y} + \alpha (B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim}) = l A _ {Y} + \alpha (\frac {1}{v} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y}) - \frac {1}{v} \phi^ {*} (K _ {X} + B + t L) - \frac {3 d}{v} A _ {Y})} \\ & {\qquad = (l - \frac {3 d \alpha}{v}) A _ {Y} - \frac {\alpha}{v} \phi^ {*} (K _ {X} + B + t L) + \frac {\alpha}{v} (K _ {Y} + \Gamma_ {Y} + 3 d A _ {Y})} \end{array}
$$

which shows that

$$
l A _ {Y} + \alpha (B _ {Y} ^ {\sim} + t L _ {Y} ^ {\sim})
$$

is ample if l is large enough depending only on$d , r , \epsilon$remembering from Step 5 that $K _ { Y } + \Gamma _ { Y } + 3 d A _ { Y }$is ample. Therefore, taking l large enough and then replacing it with$3 l$ we can assume$l A _ { Y } - ( K _ { Y } + T _ { Y } )$is ample.

Step 8. In this step we finish the proof by applying Theorem 1.9. The pair$( Y , ( 1 - \epsilon ^ { \prime } ) T _ { Y } )$ is klt because$( X , B + t L )$is klt and

$$
a (T, X, B + t L) = \epsilon^ {\prime}.
$$

Thus the pair$( Y , T _ { Y } )$is lc, by our choice of$\epsilon ^ { \prime } .$Moreover,$A _ { Y } | _ { T _ { Y } } \sim 0$since$T _ { Y }$is mapped to the closed point x. Now applying Theorem 1.9 (by taking$M = l A _ { Y } , S = T _ { Y }$, and$z = x )$), there is a natural number n depending only on d and there is a Q-divisor$\Lambda _ { Y } \geq T _ { Y }$such that$( Y , \Lambda _ { Y } )$is lc over x and

$$
n (K _ {Y} + \Lambda_ {Y}) \sim (n + 2) l A _ {Y}.
$$

Let Λ be the pushdown of$\Lambda _ { Y }$. Then$K _ { Y } + \Lambda _ { Y }$is the pullback of$K _ { X } + \Lambda$, so the pair$( X , \Lambda )$ is lc near x. Also$n \Lambda$is integral. Moreover, from

$$
K _ {X} + \Lambda \sim_ {\mathbb {Q}} \frac {(n + 2) l}{n} A
$$

we deduce that$4 l A - ( K _ { X } + \Lambda )$is ample which in turn implies that there is a natural number m depending only on$d , r , \epsilon$such that$m A - \Lambda$is ample. Finally,

$$
a (T, X, \Lambda) = a (T, Y, \Lambda_ {Y}) = a (T _ {Y}, Y, \Lambda_ {Y}) = 0,
$$

so$T$is an lc place of$( X , \Lambda )$

## 6. Proof of main results

We apply induction on dimension to prove Theorems 1.1, 1.6, and 1.8, so assume they all hold in dimension$\leq d - 1$. It is easy to verify them in dimension one. Recall that we proved Theorem 1.9 in Section 4.

Proof. (of Theorem 1.8) Step 1. In this step we make some simple reductions. Since$A - B$ and$A - M$are pseudo-efective, replacing A with 2A we can assume$A - B$and$A - M$are big. In particular,$A \sim _ { \mathbb { R } } M + N$for some$N \geq 0$. Thus

$$
\operatorname{lct} (X, B, | M | _ {\mathbb {R}}) \geq \operatorname{lct} (X, B, | M + N | _ {\mathbb {R}}) = \operatorname{lct} (X, B, | A | _ {\mathbb {R}}),
$$

so it is enough to give a positive lower bound for the right hand side.

Step 2. In this step we reduce the theorem to the case when$K _ { X }$is Q-Cartier. By Lemma 2.24, there exist a natural number l depending only on$d , r , \epsilon$such that there exist a small projective birational morphism$\phi \colon Y  X$and a very ample divisor$A _ { Y }$on$Y$such that

•$Y$is normal and$K _ { Y }$is Q-Cartier,

$A _ { Y } ^ { d } \leq l$and$A _ { Y } - \phi ^ { * } A$is ample.

Let$K _ { Y } + B _ { Y } = \phi ^ { * } ( K _ { X } + B )$. Then

$$
A _ {Y} - B _ {Y} = \left(A _ {Y} - \phi^ {*} A\right) + \left(\phi^ {*} A - B _ {Y}\right)
$$

is big as$\phi$is small. Moreover,

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) = \operatorname{lct} (Y, B _ {Y}, | \phi^ {*} A | _ {\mathbb {R}}) \geq \operatorname{lct} (Y, B _ {Y}, | A _ {Y} | _ {\mathbb {R}}).
$$

Thus replacing$( X , B ) , A , r$with$( Y , B _ { Y } ) , A _ { Y } , l$, we can assume that$K _ { X }$is Q-Cartier.

Step 3. From here to the end of Step 5 we assume that$A - B$is ample. In Step 6 we treat the general case. In this step we consider the lc threshold of the R-linear system defined by${ \dot { C } } : = { \textstyle { \frac { 1 } { 2 } } } A$and make some preparations for applying Proposition 5.11. We have

$$
\operatorname{lct} (X, B, | A | _ {\mathbb {R}}) = \frac {1}{2} \operatorname{lct} (X, B, | C | _ {\mathbb {R}})
$$

because if$N \in | A | _ { \mathbb { R } }$, then$L : = { \textstyle { \frac { 1 } { 2 } } } N \in | C | _ { \mathbb { R } }$and$( X , B + t N )$is lc if and only if$( X , B + 2 t L )$ is lc where$t \in \mathbb { R }$. Thus it is enough to find a positive lower bound for lct$( X , B , | C | _ { \mathbb { R } } )$

Let$n , m , \epsilon ^ { \prime }$be the numbers given by Proposition 5.11 for the data$d , r , \epsilon .$Note that since $K _ { X } + B$and$K _ { X }$are both R-Cartier, B is R-Cartier. Also note that$A - C$is ample by definition of C. Pick$L \in | C | _ { \mathbb { R } }$. Let t be the largest real number such that$( X , B + t L )$is $\epsilon ^ { \prime } { - } \mathrm { l c }$. It is enough to find a positive lower bound for t. In particular, we can assume$t < 1$

By definition of$t ,$there is a prime divisor$T$on birational models of X such that

$$
a (T, X, B + t L) = \epsilon^ {\prime}.
$$

Let x be the generic point of the centre of$T$on$X$.

Step$\it 4 .$In this step we reduce to the case when x is a closed point. Assume x is not a closed point. Then cutting by general elements of$| A |$and applying induction (see Step 1 of the proof of Proposition 5.7 for similar arguments), there is a positive real number v depending only on$d , r , \epsilon$such that$( X , B + v L )$is lc outside finitely many closed points, in particular, it is lc near x. Then

$$
(X, B + (1 - \frac {\epsilon^ {\prime}}{\epsilon}) v L)
$$

is$\epsilon ^ { \prime } { - } \mathrm { l c }$near x, by Lemma 2.3, because

$$
B + (1 - \frac {\epsilon^ {\prime}}{\epsilon}) v L = \frac {\epsilon^ {\prime}}{\epsilon} B + (1 - \frac {\epsilon^ {\prime}}{\epsilon}) (B + v L)
$$

and because$( X , B )$is ǫ-lc. In particular,$\begin{array} { r } { t \geq ( 1 - \frac { \epsilon ^ { \prime } } { \epsilon } ) v } \end{array}$. Thus we can assume x is a closed point.

Step 5. In this step we show that t is bounded from below away from zero by applying Propositions 5.7 and 5.11. First, by Proposition 5.11 there is a Q-Cartier Q-divisor$\Lambda \geq 0$ such that

$n \Lambda$is integral,

$m A - \Lambda$is ample,

$( X , \Lambda )$is lc near$x ,$and

• T is an lc place of$( X , \Lambda )$

Replacing$A , C , L , t$with 2mA, 2mC, 2m$L , { \frac { t } { 2 m } }$, respectively, and replacing r accordingly, we can assume$A - B - t L$and$A - \Lambda$are ample. Applying Proposition 5.7 to$( X , B + t L )$, there is a natural number$q$depending only on$d , r , n , \epsilon ^ { \prime }$such that if$\nu \colon U \to X$is a resolution so that$T$is a divisor on$U .$, then$\mu _ { T } \nu ^ { * } L \leq q$. Pick such a resolution.

Now since

$$
a (T, X, B) \geq \epsilon > \epsilon^ {\prime} = a (T, X, B + t L),
$$

we have$\mu _ { T } \nu ^ { * } t L \geq \epsilon - \epsilon ^ { \prime }$which implies$\begin{array} { r } { t \geq \frac { \epsilon - \epsilon ^ { \prime } } { q } } \end{array}$, hence t is bounded from below as required.

Step 6. In this step we finish the proof of the theorem. It remains to treat the case when $A - B$may not be ample. We will show that after replacing A with a bounded multiple, $A - B$becomes ample. As mentioned in Step 1, we can assume$A - B$is big. We can then find$0 \leq P \sim _ { \mathbb { R } } A - B$. By Steps 1-5 above, more precisely, by applying the theorem in the case when the boundary is zero, we find a positive real number s depending only on$d , r ,$ǫ such that$( X , s P )$is klt. Thus$K _ { X } + s P + 3 d A$is ample by boundedness of length of extremal rays. On the other hand, we can assume that$A - K _ { X }$is ample, hence$s P + ( 3 d + 1 ) .$A is ample which means that letting$\textstyle e = { \bigl \lceil } { \frac { 3 d + 1 } { s } } { \bigr \rceil }$, P + eA is ample.

By assumption,$P \sim _ { \mathbb { R } } A - B ,$so$( e + 1 ) A - B$is ample. Therefore, replacing A with $( e + 1 ) A$, we are reduced to the case when$A - B$is ample.

The idea of Step 6 in the previous proof is due to Yanning Xu.

Proof. (of Theorem 1.7) This follows by combining Theorem 1.8, Lemma 3.3, and Proposition 3.4.

Proof. (of Theorem 1.6) This follows from Theorem 1.8 in dimension$\leq d .$, Theorem 1.1 in dimension$\leq d - 1$, and Lemma 3.2.

Proof. (of Theorem 1.1) Let$X ^ { \prime }$be a small Q-factorialisation of X. Then$X ^ { \prime }$is of Fano type. Run an MMP on$- K \boldsymbol { X } \boldsymbol { \mathit { \Pi } }$and let$X ^ { \prime \prime }$be the resulting model. Then$X ^ { \prime \prime }$is an ǫ-lc weak Fano variety because we can find$\Delta \ge B$so that$( X , \Delta )$is ǫ-lc and$K _ { X } + \Delta \sim _ { \mathbb { R } } ($which gives$\Delta ^ { \prime \prime }$so that$( X ^ { \prime \prime } , \Delta ^ { \prime \prime } )$is ǫ-lc. It is enough to show such$X ^ { \prime \prime }$form a bounded family because then there is a bounded natural number n such that$K _ { X ^ { \prime \prime } }$has a klt n-complement $K _ { X ^ { \prime \prime } } + \Omega ^ { \prime \prime }$which gives a klt n-complement$K _ { X ^ { \prime } } + \Omega ^ { \prime } \ [ 5 , 6 . 1 ( 3 ) ]$and this in turn gives a klt n-complement$K _ { X } + \Omega$of$K _ { X }$, hence we can apply [15]. Replacing X with$X ^ { \prime \prime }$we can then assume$B = 0$

By Theorems 2.10 and 2.13, there is a natural number m depending only on$d , \epsilon$such that$\vert - m K _ { X } \vert$defines a birational map and such that$K _ { X }$has an m-complement. Moreover, by Theorem 1.1 in dimension$\leq d - 1$and by Theorem 2.11, there is a natural number v depending only on$d , \epsilon$such that vo$. ( - K _ { X } ) \leq v$

On the other hand, by Theorem 1.6, there is a positive real number t depending only on$d , e$ǫ such that if$0 \leq N \sim _ { \mathbb { R } } - K _ { X }$then$( X , t N )$is klt. Thus letting$\begin{array} { r } { t _ { l } = \frac { t } { l } } \end{array}$for$l \in \mathbb N$, we deduce that for any$0 \le L \sim - l K _ { X }$, the pair$( X , t _ { l } L )$is klt. Now boundedness of such X follows from Theorem 2.15.

Proof. (of Corollary 1.4) Since$\Delta$is big, we can write$\Delta \sim _ { \mathbb { R } } A + D$where A is ample and $D \geq 0$. Pick$\alpha \in ( 0 , 1 )$and let

$$
\Gamma = (1 - \alpha) \Delta + \alpha D.
$$

Then

$$
- (K _ {X} + \Gamma) = - (1 - \alpha) (K _ {X} + \Delta) - \alpha (K _ {X} + D)
$$

is ample because

$$
- (K _ {X} + D) \sim_ {\mathbb {R}} \Delta - D \sim_ {\mathbb {R}} A
$$

is ample. Since$( X , \Delta )$is$\epsilon { \mathrm { - l c } } ,$choosing α to be suficiently small we can ensure that$( X , \Gamma )$ is$\frac { \epsilon } { 2 } { - } \mathrm { l c }$. Now apply Theorem 1.1.

Proof. (of Corollary 1.5) This follows from Theorem 1.1 and [39, Theorem 1.8].

## References

[1] V. Alexeev; Boundedness and$K ^ { 2 }$for log surfaces. Internat. J. Math. 5 (1994), no. 6, 779–810.

[2] V. Alexeev, M. Brion, Boundedness of spherical Fano varieties. The Fano Conference, 69-80, Univ. Torino, Turin, 2004.

[3] F. Ambro; Variation of Log Canonical Thresholds in Linear Systems. Int. Math. Res. Notices 14 (2016), 4418-4448.

[4] C. Birkar; Log Calabi-Yau fibrations, arXiv:1811.10709.

[5] C. Birkar; Anti-pluricanonical systems on Fano varieties, Ann. of Math. (2) 190 (2019), no. 2, 345-463.

[6] C. Birkar; Existence of log canonical flips and a special LMMP, Pub. Math. IHES., 115 (2012), 325-368.

[7] C. Birkar, P. Cascini, C. Hacon and J. M<sup>c</sup>Kernan; Existence of minimal models for varieties of log general type, J. Amer. Math. Soc. 23 (2010), no. 2, 405-468.

[8] A. Borisov; Boundedness of Fano threefolds with log-terminal singularities of given index. J. Math. Sci. Univ. Tokyo 8 (2001), no. 2, 329–342.

[9] A. Borisov, L. Borisov; Singular toric Fano varieties. Acad. Sci. USSR Sb. Math. 75 (1993), no. 1, 277–283.

[10] F. Campana, Une version g´eom´etrique g´en´eralis´ee du th´eor\`eme du produit de Nadel [A generalized geometric version of the Nadel product theorem], Bull. Soc. Math. France 119 (1991), no. 4, 479–493 (French).

[11] I. Cheltsov, C. Shramov; Log canonical thresholds of smooth Fano threefolds. Russian Mathematical Surveys 63 (2008), 859-958. Appendix by J.-P. Demailly; On Tian’s invariant and log canonical thresholds.

[12] D. A. Cox, J. B. Little, H. K. Schenck; Toric varieties. Graduate Studies in Mathematics, volume 214, American Mathematical Society (2011).

[13] C. D. Hacon, J. M<sup>c</sup>Kernan and C. Xu; ACC for log canonical thresholds, Ann. of Math. (2) 180 (2014), no. 2, 523-571.

[14] C. D. Hacon, J. M<sup>c</sup>Kernan and C. Xu; On the birational automorphisms of varieties of general type, Ann. of Math. (2) 177 (2013), no. 3, 1077-1111.

[15] C. D. Hacon and C. Xu; Boundedness of log Calabi-Yau pairs of Fano type. Math. Res. Lett. 22 (2015), no. 6, 1699-1716.

[16] V. A. Iskovskikh and Yu. G. Prokhorov, Fano varieties. Algebraic geometry. V., Encyclopaedia Math. Sci., vol. 47, Springer, Berlin, 1999.

[17] C. Jiang, Boundedness of Q-Fano varieties with degrees and alpha-invariants bounded from below, to appear in Annales scientifiques de l’ENS, arXiv:1705.02740.

[18] C. Jiang, Boundedness of anti-canonical volumes of singular log Fano threefolds, to appear in Comm. Anal. Geom., arXiv:1411.6728v2.

[19] C. Jiang, On birational boundedness of Fano fibrations, Amer. J. Math. 140 (2018), no. 5, 1253-1276.

[20] M. Kawakita; Inversion of adjunction on log canonicity, Invent. Math. 167 (2007), 129-133.

[21] Y. Kawamata; On the length of an extremal rational curve, Invent. Math. 105 (1991), no. 3, 609-611.

[22] Y. Kawamata; Boundedness of Q-Fano threefolds. Proceedings of the International Conference on Algebra, Part 3 (Novosibirsk, 1989), 439–445, Contemp. Math., 131, Part 3, Amer. Math. Soc., Providence, RI, 1992.

[23] K. S. Kedlaya; More ´etale covers of afine spaces in positive characteristic. Journal of Algebraic Geometry 14 (2005), 187-192.

[24] J. Koll´ar; Partial resolution by toroidal blow-ups. Tunis. J. Math. 1 (2019), no. 1, 3-12.

[25] J. Koll´ar ´et al.; Flips and abundance for algebraic threefolds, Ast´erisque No. 211 (1992).

[26] J. Koll´ar; Y. Miyaoka; S. Mori; Rationally connectedness and boundedness of Fano manifolds. J. Di. Geom. 36 (1992), 765-769.

[27] J. Koll´ar; Y. Miyaoka; S. Mori; H. Takagi; Boundedness of canonical Q-Fano 3-folds. Proc. Japan Acad. Ser. A Math. Sci. 76 (2000), no. 5, 73–77.

[28] J. Koll´ar and S. Mori, Birational geometry of algebraic varieties, Cambridge Tracts in Math. 134, Cambridge Univ. Press, 1998.

[29] R. Lazarsfeld; Positivity in algebraic geometry II. Springer (2004).

[30] J. Lin; Birational unboundedness of Q-Fano threefolds. Int. Math. Res. Not. 6 (2003), 301-312.

[31] J. M<sup>c</sup>Kernan, Yu. Prokhorov; Threefold thresholds. Manuscripta Math. 114 (2004), no. 3, 281–304.

[32] A. M. Nadel, The boundedness of degree of Fano varieties with Picard number one, J. Amer. Math. Soc. 4 (1991), no. 4, 681–692.

[33] V. V. Nikulin, del Pezzo surfaces with log-terminal singularities. III. (Russian) Izv. Akad. Nauk SSSR Ser. Mat. 53 (1989), no. 6, 1316–1334, 1338; translation in Math. USSR-Izv. 35 (1990), no. 3, 657–675.

[34] V. V. Nikulin, del Pezzo surfaces with log-terminal singularities. II. (Russian) Izv. Akad. Nauk SSSR Ser. Mat. 52 (1988), no. 5, 1032–1050, 1119; translation in Math. USSR-Izv. 33 (1989), no. 2, 355–372.

[35] V. V. Nikulin, Del Pezzo surfaces with log-terminal singularities, Mat. Sb. 180 (1989), no. 2, 226–243, translation in Math. USSR-Sb. 66 (1990), no. 1, 231–248.

[36] Yu. Prokhorov; Blow-ups of canonical singularities. Algebra (Moscow, 1998), 301–317, de Gruyter, Berlin, 2000.

[37] Yu. Prokhorov, V.V. Shokurov; Towards the second main theorem on complements. J. Algebraic Geometry, 18 (2009) 151-199.

DPMMS, Centre for Mathematical Sciences

[38] Yu. Prokhorov; V.V. Shokurov; The first fundamental Theorem on complements: from global to local. (Russian) Izv. Ross. Akad. Nauk Ser. Mat. 65 (2001), no. 6, 99–128; translation in Izv. Math. 65 (2001), no. 6, 1169–1196.

[39] Yu. Prokhorov and C. Shramov; Jordan property for Cremona groups. Amer. J. Math.,138 (2016), 403-418.

[40] Yu. Prokhorov and C. Shramov; Jordan property for groups of birational selfmaps. Compositio Math., Volume 150, Issue 12 (2014), 2054-2072.

[41] J.-P. Serre; A Minkowski-style bound for the orders of the finite subgroups of the Cremona group of rank 2 over an arbitrary field. Mosc. Math. J., 9 (2009):193-208.

[42] G. Tian; On a set of polarized K¨ahler metrics on algebraic manifolds. J. Diferential Geom. 32 (1990), 99-130.

[43] E. Viehweg; Quasi-Projective Moduli of Polarized Manifolds. Springer-Verlag, Berlin, 1995

[45] Yu. G. Zarhin. Theta groups and products of abelian and rational varieties. Proc. Edinburgh Math. Soc., 57 (2014):299-304.

[44] C. Xu; Finiteness of algebraic fundamental groups. Compositio Math., 150 (3) (2014), 409-414.