# Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0

By Manjul Bhargava and Arul Shankar

## Abstract

We prove an asymptotic formula for the number of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-equivalence classes of integral ternary cubic forms having bounded invariants. We use this result to show that the average size of the 3-Selmer group of all elliptic curves, when ordered by height, is equal to 4. This implies that the average rank of all elliptic curves, when ordered by height, is less than 1.17.

Combining our counting techniques with a recent result of Dokchitser and Dokchitser, we prove that a positive proportion of all elliptic curves have rank 0. Assuming the finiteness of the Tate–Shafarevich group, we also show that a positive proportion of elliptic curves have rank 1. Finally, combining our counting results with the recent work of Skinner and Urban, we show that a positive proportion of elliptic curves have analytic rank 0; i.e., a positive proportion of elliptic curves have nonvanishing L-function at $s = 1$. It follows that a positive proportion of all elliptic curves satisfy BSD.

## 1. Introduction

Any elliptic curve E over$\mathbb { Q }$is isomorphic to a unique curve of the form $E _ { A , B } : y ^ { 2 } = x ^ { 3 } + A x + B$, where$A , B \in \mathbb { Z }$and for all primes p:$p ^ { 6 } \nmid B$ whenever$p ^ { 4 } \mid A$. The (naive) height$H ( E _ { A , B } )$of the elliptic curve$E = E _ { A , B }$ is then defined by

$$
H (E _ {A, B}) := \max \{4 | A ^ {3} |, 2 7 B ^ {2} \}.
$$

In a previous paper [8], we showed that the average rank of all elliptic curves, when ordered by height, is finite. This was accomplished by proving that the average size of the 2-Selmer group of elliptic curves, when ordered by height, is exactly 3; it then followed from the latter result that (the limsup of) the average rank of all elliptic curves is bounded above by 1.5.

In this article, we prove an analogous result for the average size of the 3-Selmer group.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">c 2015 Department of Mathematics, Princeton University.</span></small>

Theorem 1. When all elliptic curves$E / \mathbb { Q }$are ordered by height, the average size of the 3-Selmer group$S _ { 3 } ( E )$is 4.

The above result is also seen to imply the boundedness of the average rank of all elliptic curves. Indeed, for an elliptic curve E over Q, since the 3-rank $r _ { 3 } ( S _ { 3 } ( E ) )$of the 3-Selmer group$S _ { 3 } ( E )$of E bounds the rank of$E ,$and since $6 r _ { 3 } ( E ) - 3 \le 3 ^ { r _ { 3 } ( E ) } = | S _ { 3 } ( E ) |$, by taking averages we immediately obtain the following improved bound on the average rank of elliptic curves.

Corollary 2. When all elliptic curves over$\mathbb { Q }$are ordered by height, their average 3-Selmer rank is at most$1 { \scriptstyle { \frac { 1 } { 6 } } } ;$; thus their average rank is also at most$1 { \frac { 1 } { 6 } } < 1 . 1 7$

Theorem 1 also yields the same bound of$1 \textstyle { \frac { 1 } { 6 } }$on the average 3-rank of the Tate–Shafarevich group of all elliptic curves, when ordered by height.

We will in fact prove a stronger version of Theorem 1, namely,

Theorem 3. When elliptic curves$E : y ^ { 2 } = x ^ { 3 } + A x + B$, in any family defined by finitely many congruence conditions on the coeficients A and$B _ { ; }$ are ordered by height, the average size of the 3-Selmer group$S _ { 3 } ( E )$is 4.

Thus the average size of the 3-Selmer group remains 4 even when one averages over any subset of elliptic curves defined by finitely many local conditions. We will actually prove Theorem 3 for an even larger class of families, including some that are defined by certain natural infinite sets of local conditions (such as the family of all semistable elliptic curves).

Theorem 3, and its above-mentioned extensions, allows us to deduce a number of additional results on ranks that could not be deduced solely through understanding the average size of the 2-Selmer group, as in [8]. First, by combining our counting techniques with the remarkable recent results of Dokchitser and Dokchitser [17] on the parity of p-ranks of Selmer groups, we prove

Theorem 4. When all elliptic curves$E / \mathbb { Q }$are ordered by height, a positive proportion of them have rank 0.

In the case of rank 1, if we assume the finiteness of the Tate–Shafarevich group, then we also have

Theorem 5. Assume$\operatorname { I I I } ( E )$is finite for all E. When all elliptic curves $E / \mathbb { Q }$are ordered by height, a positive proportion of them have rank 1.

Next, combining our counting arguments with the important recent work of Skinner–Urban [28] on the Iwasawa Main Conjectures for$\mathrm { G L _ { 2 } }$, we obtain:

Theorem 6. When all elliptic curves$E / \mathbb { Q }$are ordered by height, a positive proportion of them have analytic rank 0; that is, a positive proportion of elliptic curves have nonvanishing L-function at$s = 1$

Applying Kolyvagin’s Theorem, or noting that the elliptic curves of analytic rank 0 that arise in Theorem 6 form a subset of those that are constructed in Theorem 4, we conclude

## Corollary 7. A positive proportion of elliptic curves satisfy BSD.

Our previous results on the average size of the 2-Selmer group were obtained through counting integral binary quartic forms, up to$\operatorname { G L _ { 2 } } ( \mathbb { Z } )$-equivalence, having bounded invariants. The connection with elliptic curves is that the process of 2-descent has a classical interpretation in terms of rational binary quartic forms; indeed, this connection was behind the beautiful computations of Birch and Swinnerton-Dyer in [9]. The process of 2-descent through the use of binary quartic forms, as in Cremona’s remarkable mwrank program, remains the fastest method, in general, for computing ranks of elliptic curves.

In order to prove an analogous result for the average size of 3-Selmer groups, we apply our counting techniques in [8], appropriately modified, to the space$V _ { \mathbb { Z } }$of integral ternary cubic forms. The group$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$acts naturally on $V _ { \mathbb { Z } } ,$and the ring of polynomial invariants over C for this action turns out to have two independent generators, having degrees 4 and 6, which we denote by I and J respectively.

These invariants may be constructed as follows. For a ternary cubic form$f ,$ let$\mathcal { H } ( f )$denote the Hessian of$f , { \mathrm { i . e . } }$., the determinant of the$3 \times 3$matrix of second order partial derivatives of$f \colon$

$$
\mathcal {H} (f (x, y, z)) := \left| \begin{array}{c c c} f _ {x x} & f _ {x y} & f _ {x z} \\ f _ {x y} & f _ {y y} & f _ {y z} \\ f _ {x z} & f _ {y z} & f _ {z z} \end{array} \right|.\tag{1}
$$

Then$\mathcal { H } ( f )$is itself a ternary cubic form and, moreover, it is an$\mathrm { S L _ { 3 ^ { - } } }$-covariant of$f ;$i.e., for$\gamma \in \mathrm { S L _ { 3 } }$, we have$\mathcal { H } ( \gamma \cdot f ) = \gamma \cdot \mathcal { H } ( f )$. An easy computation gives

$$
\mathcal {H} (\mathcal {H} (f)) = 1 2 2 8 8 I (f) ^ {2} \cdot f + 5 1 2 J (f) \cdot \mathcal {H} (f)\tag{2}
$$

for certain rational polynomials$I ( f )$and$J ( f )$in the coeficients of$f ,$having degrees 4 and 6 respectively; note that (2) uniquely determines$J ( f )$and also uniquely determines$I ( f )$up to sign. The sign of$I ( f )$is fixed by the requirement that the discriminant$\Delta ( f )$of a ternary cubic form$f$be expressible in terms of$I ( f )$and$J ( f )$by the same formula as for binary quartic forms, namely,

$$
\Delta (f) := \Delta (I, J) := (4 I (f) ^ {3} - J (f) ^ {2}) / 2 7.\tag{3}
$$

These polynomials$I ( f )$and$J ( f )$are evidently$\mathrm { { S L } _ { 3 } }$-invariants, and in fact they generate the full ring of polynomial invariants over$\mathbb { C } .$.

Traditionally, the generators of the ring of invariants of the action of$\mathrm { { S L } _ { 3 } }$ on the space of ternary cubic forms have been denoted by$S$and$T$(called the Aronhold invariants [2]), which are certain integer multiples of I and$J ,$ respectively; explicitly, we have$S = 1 6 \cdot I$and$T = 3 2 \cdot J$. However, any ternary cubic form$f$having complex coeficients and nonzero discriminant is $\operatorname { S L _ { 3 } } ( \mathbb { C } )$-equivalent to a ternary cubic form E in Weierstrass form. In previous work (see$[ 8 , \ \ S 3 ] )$we had defined invariants$I ( E )$and$J ( E )$of such$E ,$and the invariants$I ( f )$and$J ( f )$of ternary cubic forms$f$have been chosen to agree with those same invariants of$E$

Now, for ternary cubic forms over the integers, the general work of Borel and Harish-Chandra [10] implies that the number of equivalence classes of integral ternary cubic forms, having any given fixed values for these basic invariants I and J (so long as I and$J$are not both equal to$\operatorname { z e r o } )$, is finite. The question thus arises: how many$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-classes of integral ternary cubic forms are there, on average, having invariants$I , J ,$as the pair$( I , J )$varies?

To answer this question, we require a couple of definitions. Let us define the height of a ternary cubic form$f ( x , y , z )$by

$$
H (f) := H (I, J) := \max \{| I ^ {3} |, J ^ {2} / 4 \}.\tag{4}
$$

(As usual, the constant factor$1 / 4$on$J ^ { 2 }$is present for convenience and is not of any real importance.) Thus$H ( f )$is$\mathrm { ~ a ~ } ^ { 6 6 }$degree$1 2 ^ { \mathfrak { s } }$function in the coeficients of$f ,$in the sense that$H ( \lambda f ) = \lambda ^ { 1 2 } H ( f )$for any constant$\lambda .$We may then order all$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-classes of ternary cubic forms$f$by their height$H ( f )$, and we may similarly order all pairs$( I , J )$of invariants by their height$H ( I , J )$

As with binary quartic forms, we wish to restrict ourselves to counting ternary cubic forms that are irreducible in an appropriate sense. Being simply $i r r e d u c i b l e \mathrm { - } \mathrm { i . e . }$, not having a smaller degree factor—is more a geometric condition rather than an arithmetic one. We wish to have a condition that implies that the ternary cubic form is suficiently “generic” over$\mathbb { Q } .$. The most convenient notion (also for the applications) turns out to be what we call strong irreducibility.

Let us say that an integral ternary cubic form$f$is strongly irreducible if $f$is irreducible and the common zero set of$f$and its Hessian$\mathcal { H } ( f )$in$\mathbb { P } ^ { 2 } \ ( \mathrm { i . e . }$ the set of flexes of$f$in$\mathbb { P } ^ { 2 } )$contains no rational points. We prove

Theorem 8. Let$h ( I , J )$denote the number$o f \operatorname { S L _ { 3 } } ( \mathbb { Z } )$-equivalence classes of strongly irreducible ternary cubic forms having invariants equal to I and J. Then

$$
\text{(a)} \sum_{\substack{\Delta (I,J) > 0\\ H(I,J) <   X}}h(I,J) = \frac{32}{45}\zeta (2)\zeta (3)X^{5 / 6} + o(X^{5 / 6});
$$

$$
\text{(b)} \sum_{\substack{\Delta (I,J) <   0\\ H(I,J) <   X}}h(I,J) = \frac{128}{45}\zeta (2)\zeta (3)X^{5 / 6} + o(X^{5 / 6}).
$$

In order to obtain the average size of$h ( I , J )$, as (I, J) varies, we first need to know which pairs (I, J) can actually occur as the invariants of an integral ternary cubic form. For example, in the case of binary quadratic and binary cubic forms, the answer is well known: there is only one invariant—the discriminant—and a number occurs as the discriminant of a binary quadratic (resp. cubic) form if and only if it is congruent to 0 or 1 (mod 4).

In the binary quartic case, we proved in [8] that a similar scenario occurs; namely, an$( I , J ) \in \mathbb { Z } \times \mathbb { Z }$is$e l i g i b l e \mathrm { - } \mathrm { i . e . }$, it occurs as the invariants of some integer binary quartic form—if and only if it satisfies any one of a certain specified finite set of congruence conditions modulo 27 (see [8, Th. 1.7]).

It turns out that the invariants (I, J) that can occur (i.e., are eligible) for an integral ternary cubic must also satisfy these same conditions modulo 27. However, there is also now a strictly larger set of possibilities at the prime 2. Indeed, the pairs$( I , J )$that occur for ternary cubic forms need not even be integral, but rather lie in${ \begin{array} { r } { { \frac { 1 } { 1 6 } } \mathbb { Z } \times { \frac { 1 } { 3 2 } } \mathbb { Z } ; } \end{array} }$and the pairs$( I , J )$in this set that actually occur are then defined by certain congruence conditions modulo 64 on 16I and 32J, in addition to the same congruence conditions modulo 27 on I and J that occur for binary quartic forms.

In particular, the set of integral pairs$( I , J ) \in \mathbb { Z } \times \mathbb { Z }$that occur as invariants for integral ternary cubic forms is the same as the set of all pairs$( I , J )$that occur for integral binary quartic forms! We prove

Theorem 9. A pair (I, J) occurs as the pair of invariants of an integral ternary cubic form if and only if$\begin{array} { r } { ( I , J ) \in \frac { 1 } { 1 6 } \mathbb { Z } \times \frac { 1 } { 3 2 } \mathbb { Z } } \end{array}$, the pair (16I, 32J) satisfies one of the following congruence conditions modulo 64:

(a) 16I ≡ 0 (mod 16) and 32J ≡ 0 (mod 32),

(b) 16I ≡ 0 (mod 16) and 32J ≡ 8 (mod 32),

(c) 16I ≡ 1 (mod 64) and 32J ≡ 31 (mod 32),

(d) 16I ≡ 9 (mod 64) and 32J ≡ 27 (mod 32),

(e) 16I ≡ 17 (mod 64) and 32J ≡ 7 (mod 32),

(f) 16I ≡ 25 (mod 64) and 32J ≡ 3 (mod 32),

(g) 16I ≡ 33 (mod 64) and 32J ≡ 15 (mod 32),

(h) 16I ≡ 41 (mod 64) and 32J ≡ 11 (mod 32),

(i) 16I ≡ 49 (mod 64) and 32J ≡ 23 (mod 32),

(j) 16I ≡ 57 (mod 64) and 32J ≡ 19 (mod 32),

and (I, J) satisfies one of the following congruence conditions modulo 27:

(a) I ≡ 0 (mod 3) and J ≡ 0 (mod 27),

(b) I ≡ 1 (mod 9) and J ≡ ±2 (mod 27),

(c) I ≡ 4 (mod 9) and J ≡ ±16 (mod 27),

(d) I ≡ 7 (mod 9) and J ≡ ±7 (mod 27).

We note that these additional possible invariants$( I , J ) \in { \frac { 1 } { 1 6 } } \mathbb { Z } \times { \frac { 1 } { 3 2 } } \mathbb { Z }$that arise for ternary cubic forms also arise in the case of binary quartics, provided one uses “generalized binary quartics”; see [13] or [20] for details on the construction and uses of these generalized quartics.

From Theorem 9, we then conclude that the number of eligible pairs $( I , J ) \in { \frac { 1 } { 1 6 } } \mathbb { Z } \times { \frac { 1 } { 3 2 } } \mathbb { Z }$, with$H ( I , J ) < X$, is asymptotically a certain constant times$X ^ { 5 / 6 }$. By Theorem$^ { 8 , }$the number of classes of strongly irreducible ternary cubic forms, per eligible$( I , J ) \in \frac { 1 } { 1 6 } \mathbb { Z } \times \frac { 1 } { 3 2 } \mathbb { Z } .$, is thus a constant on average. We have

Theorem 10. Let$h ( I , J )$denote the number of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-equivalence classes of strongly irreducible integral ternary cubic forms having invariants equal to I and J. Then

$$
\lim_{X\to \infty}\frac{\sum\limits_{\substack{\Delta(I,J) > 0\\ H(I,J) <   X}}h(I,J)}{\sum\limits_{(I,J)\text{eligible}}1} = \lim_{X\to \infty}\frac{\sum\limits_{\substack{\Delta(I,J) <   0\\ H(I,J) <   X}}h(I,J)}{\sum\limits_{(I,J)\text{eligible}}1} = 3\zeta (2)\zeta (3).
$$

The fact that this class number$h ( I , J )$is a finite constant on average is indeed what allows us to show that the size of the 3-Selmer group of elliptic curves too is a finite constant on average.

We actually prove a strengthening of Theorem 10; namely, we obtain the asymptotic count of ternary cubic forms having bounded invariants that satisfy any specified finite set of congruence conditions (see Section 2.4, Theorem 17). This strengthening turns out to be crucial for the application to 3-Selmer groups (as in Theorem 1), which we now discuss.

Recall that, for any positive integer$n ,$an element of the n-Selmer group $S _ { n } ( E )$of an elliptic curve$E / \mathbb { Q }$may be thought of as$\mathrm { a }$“locally soluble n-covering.” An n-covering of$E / \mathbb { Q }$is a genus one curve$C$together with maps$\phi : C \to E$and$\theta : C \to E$, where$\phi$is an isomorphism defined over $\mathbb { C }$and$\theta$is a degree$n ^ { 2 }$map defined over$\mathbb { Q }$such that the following diagram commutes:

$$
\begin{array}{c} E \xrightarrow {[ n ]} E. \\ \phi \Big \uparrow \quad \Big \backslash \theta \\ C \end{array}
$$

Thus an n-covering$C = ( C , \phi , \theta )$may be viewed as a “twist over$\mathbb { Q }$of the multiplication-by-n map on$E . ^ { \mathfrak { s } }$Two n-coverings C and$C ^ { \prime }$are said to be isomorphic if there exists an isomorphism$\Phi : C \to C ^ { \prime }$defined over$\mathbb { Q } ,$and an n-torsion point$P \in E$, such that the following diagram commutes:

![](images/page_6_image_1.jpg)

A soluble n-covering C is one that possesses a rational point, while a locally soluble n-covering C is one that possesses an R-point and a$\mathbb { Q } _ { p } { \mathrm { - p o i n t } }$for all primes$p .$. Then we have the isomorphisms

$$
\{\text { soluble   } n \text {-coverings} \} / \sim \cong E (\mathbb {Q}) / n E (\mathbb {Q}),
$$

$$
\{\text { locally   soluble } n \text {-coverings} \} / \sim \cong S _ {n} (E).
$$

Now, counting elements of$S _ { 3 } ( E )$leads to counting ternary cubic forms for the following reason. There is a result of Cassels (see [12, Th. 1.3]) that states that any locally soluble n-covering C possesess a degree n divisor defined over $\mathbb { Q } .$If$n = 3$, we thus obtain an embedding of$C$into$\mathbb { P } ^ { 2 }$, thereby yielding a ternary cubic form, well defined up to$\mathrm { G L _ { 3 } ( \mathbb { Q } ) }$)-equivalence! Conversely, given any ternary cubic form$f$having rational coeficients and nonzero discriminant, there exists a 3-covering defined over$\mathbb { Q }$from the plane cubic C defined by the equation$f = 0$to the elliptic curve$\operatorname { J a c } ( C )$, where$\operatorname { J a c } ( C )$is the Jacobian of $C$and is given by the equation

$$
Y ^ {2} = X ^ {3} - \frac {I (f)}{3} X - \frac {J (f)}{2 7};\tag{5}
$$

an explicit formula for this 3-covering map may be given in terms of the $\mathrm { { S L } _ { 3 } . }$-covariants of f (see [1, §3.2]). Note that (5) gives another nice interpretation for the invariants$I ( f )$and$J ( f )$of a ternary cubic form$f .$

To carry out the proof of Theorems 1 and 3, we do the following:

• For each rational elliptic curve$E _ { A , B }$and element$\sigma \in S _ { 3 } ( E _ { A , B } )$, choose a weighted finite set$S _ { \sigma }$of integral ternary cubic forms, such that

– the sum of the weights of the elements in$S _ { \sigma }$is equal to one;

– each element$f \in S _ { \sigma }$gives the 3-covering$\sigma ;$

– the invariants$( I ( f ) , J ( f ) )$of each element$f \in S _ { \sigma }$agree with the invariants$( A , B )$of the elliptic curve;

– the weighted set$S = \bigcup _ { A , B } \bigcup _ { \sigma } S _ { \sigma }$is defined by congruence conditions.

The work of Cremona, Fisher, and Stoll [13] on “minimization” for ternary cubic forms plays a key role in this construction.

• Count these weighted integral ternary cubic forms via a weighted congruence version of Theorem 8. The relevant weighted set$S$of ternary cubic forms is defined by infinitely many congruence conditions, so a suitable sieve has to be performed.

In the last step, we first use a simple sieve to obtain the optimal upper bounds. The optimal lower bounds, on the other hand, are significantly more dificult to obtain, and we use the techniques and results of [6] in order to prove them.

We may compare Theorem 1 with a result of de Jong [16], who showed that for a finite field of characteristic not equal to$s ,$, the average size of the 3-Selmer group of all elliptic curves over$\mathbb { F } _ { q } ( t )$is at most$4 + \varepsilon ( q )$for an explicit function $\varepsilon ( q )$that tends to 0 as$q \to \infty$. The technique in [16] was also essentially that of counting ternary cubic forms over$\mathbb { F } _ { q } ( t ) !$Our main result, Theorem 1, may thus be viewed as a precise version of de Jong’s Theorem over the number field$\mathbb { Q } .$For more on the history of average ranks of elliptic curves in families, and related results, see [4] and [8, §1].

This paper is organized as follows. In Section 2, following the methods of [8], we determine the asymptotic number of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-equivalence classes of strongly irreducible integral ternary cubic forms having bounded height; in particular, we prove Theorems 8, 9, and 10. The primary method is that of reduction theory, allowing us to reduce the problem to counting integral points in certain finite volume regions in$\mathbb { R } ^ { 1 0 }$. However, the dificulty in such a count, as usual, lies in the fact that these regions are not compact, but rather have cusps going of to infinity. By studying the geometry of these regions via the averaging method of [5], we are able to isolate the subregions of the fundamental domains that contain predominantly (and all of the) strongly irreducible points. The appropriate volume computations for these subregions are then carried out to obtain the desired result.

In Section 3, we then describe the precise correspondence between ternary cubic forms and elements of the 3-Selmer groups of elliptic curves. We show, in particular, that nonidentity elements of the 3-Selmer group correspond to strongly irreducible ternary cubic forms. We then apply this correspondence, together with the counting results of Section 2 and a simple sieve (which involves the determination of certain local mass formulae for 3-coverings of elliptic curves over$\mathbb { Q } _ { p } )$, to prove that the average size of the 3-Selmer groups of elliptic curves, when ordered by height, is at most 4. We then use the methods of [6] to obtain the same lower bound on the average size of the 3-Selmer groups of elliptic curves, thus proving Theorems 1 and 3.

Finally, in Section 4, we combine the results of Sections 2 and 3, as well as the aforementioned results of Dokchitser–Dokchitser [17] and Skinner– Urban [28], to obtain Theorems 4, 5, and 6.

## 2. The number of integral ternary cubic forms having bounded invariants

Let$V _ { \mathbb { R } }$denote the space of all ternary cubic forms having coeficients in$\mathbb { R }$. The group$\mathrm { G L _ { 3 } ( \mathbb { R } ) }$acts on$V _ { \mathbb { R } }$on the left via linear substitution of variable; namely,$\mathrm { i f } \ \gamma \in \mathrm { G L } _ { 3 } ( \mathbb { R } )$and$f \in V _ { \mathbb { R } }$, then

$$
(\gamma \cdot f) (x, y, z) = f ((x, y, z) \cdot \gamma).
$$

For a ternary cubic form$f \in V _ { \mathbb { R } }$, let$\mathcal { H } ( f )$denote the Hessian covariant of $f ,$defined by (1), and let$I ( f )$and$J ( f )$denote the two fundamental polynomial invariants of$f$as in$( 2 )$. As noted earlier, these polynomials$I ( f )$and$J ( f )$ are invariant under the action of$\mathrm { S L _ { 3 } ( \mathbb { R } ) } \subset \mathrm { G L _ { 3 } ( \mathbb { R } ) }$and, moreover, they are relative invariants of degrees 4 and$6 ,$respectively, for the action of$\mathrm { G L _ { 3 } ( \mathbb { R } ) }$1 on V<sub>R</sub>; i.e,$I ( \gamma \cdot f ) = \operatorname * { d e t } ( \gamma ) ^ { 4 } I ( f )$and$J ( \gamma \cdot f ) = \operatorname * { d e t } ( \gamma ) ^ { 6 } J ( f )$for$\gamma \in \operatorname { G L } _ { 3 } ( \mathbb { R } )$ and$f \in V _ { \mathbb { R } }$

The discriminant$\Delta ( f )$of a ternary cubic form$f$is a relative invariant of degree 12 and is given by the formula$\Delta ( f ) = \Delta ( I , J ) = ( 4 I ( f ) ^ { 3 } - J ( f ) ^ { 2 } ) / 2 7$ We define the height$H ( f )$of$f$by

$$
H (f) := H (I, J) := \max \{| I (f) | ^ {3}, J (f) ^ {2} / 4 \}.
$$

Note that the height is also a degree 12 relative invariant for the action of $\mathrm { G L _ { 3 } ( \mathbb { R } ) }$on$V _ { \mathbb { R } }$

The action of$\mathrm { S L _ { 3 } ( \mathbb { Z } ) } \subset \mathrm { G L _ { 3 } ( \mathbb { R } ) }$on$V _ { \mathbb { R } }$evidently preserves the lattice$V _ { \mathbb { Z } }$ consisting of integral ternary cubic forms. In fact, it also preserves the two sets$V _ { \mathbb { Z } } ^ { + }$and$V _ { \mathbb { Z } } ^ { - }$consisting of those integral ternary cubics that have positive and negative discriminant, respectively.

As before, we say that an integral ternary cubic form is strongly irreducible if the corresponding cubic curve in$\mathbb { P } ^ { 2 }$has no rational flex. For an$\operatorname { S L _ { 3 } } ( \mathbb { Z } ) .$ invariant set$S \subset V _ { \mathbb { Z } }$, let$N ( S ; X )$denote the number of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-equivalence classes of strongly irreducible elements in$S$having height less than$X$. Our purpose in this section is to prove the following rephrasing of Theorem 8.

Theorem 11. We have

$$
\mathrm{(a)} N (V _ {\mathbb {Z}} ^ {+}; X) = \frac {3 2}{4 5} \zeta (2) \zeta (3) X ^ {5 / 6} + o (X ^ {5 / 6});
$$

$$
\text {(b)} N (V _ {\mathbb {Z}} ^ {-}; X) = \frac {1 2 8}{4 5} \zeta (2) \zeta (3) X ^ {5 / 6} + o (X ^ {5 / 6}).
$$

2.1. Reduction theory. Let$V _ { \mathbb { R } } ^ { + } \left( \mathrm { r e s p . } V _ { \mathbb { R } } ^ { - } \right)$denote the set of elements in$V _ { \mathbb { R } }$ having positive (resp. negative) discriminant. We first construct fundamental sets in$V _ { \mathbb { R } } ^ { \pm }$for the action of$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$on$V _ { \mathbb { R } } ^ { \pm }$, where$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$is the subgroup of all elements in$\mathrm { G L _ { 3 } ( \mathbb { R } ) }$having positive determinant.

To this end, let$f$be a ternary cubic form in$V _ { \mathbb { R } }$having nonzero discriminant, and let$C$denote the cubic curve in$\mathbb { P } ^ { 2 }$defined by the equation $f ( x , y , z ) = 0$. The set of flexes of$C$is given by the set of common zeroes of$f$ and$\mathcal { H } ( f )$in$\mathbb { P } ^ { 2 }$, and hence the number of such flexes is 9 by Bezout’s Theorem. As both$f$and$\mathcal { H } ( f )$have real coeficients, the flex points of$C$are either real or come in complex conjugate pairs. Therefore, since the total number of flex points is odd,$C$possesses at least one real flex point.

This implies, in particular, that any ternary cubic form over$\mathbb { R }$is$\operatorname { S L _ { 3 } } ( \mathbb { R } )$ equivalent to one in Weierstrass form, i.e., one in the form

$$
f (x, y, z) = x ^ {3} + A x z ^ {2} + B z ^ {3} - y ^ {2} z\tag{6}
$$

for some$A , B \in \mathbb { R }$. It can be checked that the ternary cubic form$f$in (6) has invariants$I ( f )$and$J ( f )$equal to$- 3 A$and$- 2 7 B$, respectively. Thus, since I and$J$are relative invariants of degrees 4 and 6, respectively, two ternary cubic forms$f$and$g$over$\mathbb { R } .$, having nonzero discriminant, are$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$)-equivalent if and only if there exists a positive constant$\lambda \in \mathbb { R }$such that$I ( f ) = \lambda ^ { 4 } I ( g )$and $J ( f ) = \lambda ^ { 6 } J ( g )$. It follows that a fundamental set$L ^ { + } \ ( \mathrm { r e s p . } \ L ^ { - } )$for the action of$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$on$V _ { \mathbb { R } } ^ { + } ~ ( \mathrm { r e s p . } ~ V _ { \mathbb { R } } ^ { - } )$may be constructed by choosing one ternary cubic form, having invariants I and$J ,$for each pair$( I , J ) \in \mathbb { R } \times \mathbb { R }$such that $H ( I , J ) = 1$and$4 I ^ { 3 } - J ^ { 2 } > 0$(resp.$4 I ^ { 3 } - J ^ { 2 } < 0 )$. We may thus choose

$$
L ^ {+} = \Bigl \{x ^ {3} - \frac {1}{3} x z ^ {2} - \frac {J}{2 7} z ^ {3} - y ^ {2} z: - 2 <   J <   2 \Bigr \},
$$

$$
L ^ {-} = \left\{x ^ {3} - \frac {I}{3} x z ^ {2} \pm \frac {2}{2 7} z ^ {3} - y ^ {2} z: - 1 \leq I <   1 \right\}
$$

$$
\cup \left\{x ^ {3} + \frac {1}{3} x z ^ {2} - \frac {J}{2 7} z ^ {3} - y ^ {2} z: - 2 <   J <   2 \right\}.
$$

The key fact that we need about these fundamental sets$L ^ { \pm }$is that the coeficients of all the ternary cubic forms in the$L ^ { \pm }$are bounded. Note also that if$G _ { 0 } \subset \mathrm { G L } _ { 3 } ^ { + } ( \mathbb { R } )$is any fixed compact subset then, for any$h \in G _ { 0 }$, the set$h \cdot L ^ { \pm }$is also a fundamental set for the action of$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$on$V _ { \mathbb { Z } } ^ { \pm }$, and the coeficients of the forms in$h \cdot L ^ { \pm }$are bounded independent of$h \in G _ { 0 }$

We also require the following fact, whose proof we postpone to Section 3.1.

Lemma 12. Let$f \in V _ { \mathbb { R } }$be any ternary cubic form having nonzero discriminant. Then the order of the stabilizer in$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$(and hence in$\operatorname { S L } _ { 3 } ( \mathbb { R } ) )$) of$f$is$3$.

Let$\mathcal { F }$denote a fundamental domain in$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$for the left action of $\mathrm { G L _ { 3 } ^ { + } ( Z ) = S L _ { 3 } ( Z ) }$on$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$contained in a standard Siegel set [10, §2]. We may take$\mathcal { F } = \{ n a k \lambda : n \in N ^ { \prime } ( a ) , a \in A ^ { \prime } , k \in K , \lambda \in \Lambda \}$, where

$$
\begin{array}{r c l} K & = & \text {subgroup SO_{3} (\mathbb {R}) \subset GL_{3} ^{+} (\mathbb {R}) of orthogonal tran} \\ A ^ {\prime} & \subset & \{a (s _ {1}, s _ {2}): s _ {1}, s _ {2} > c \}, \\ & & \text {where a(s_{1} ,s_{2}) = \left( \begin{array}{ccccc}s_{1}^{-2}s_{2}^{-1} & & & \\ & s_{1}s_{2}^{-1} & & \\ & & s_{1}s_{2}^{2}\end{array} \right),} \\ N ^ {\prime} (a) = & \{n (u _ {1}, u _ {2}, u _ {3}): (u _ {1}, u _ {2}, u _ {3}) \in \nu (a) \}, \\ & & \text {where n(u_{1},u_{2},u_{3}) = \left( \begin{array}{cc} 1 & \\ u_{1} & 1\\ u_{2} & u_{3}   1\end{array} \right),} \\ \Lambda & = & \{\lambda : \lambda > 0 \}, \\ & & \text {where \lambda = \left( \begin{array}{cc}\lambda & \\ & \lambda \\ & \lambda\end{array} \right);} \end{array}
$$

here$\nu ( a )$is a measurable subset of$[ - 1 / 2 , 1 / 2 ] ^ { 3 }$dependent only on$a \in A ^ { \prime }$and $c > 0$is an absolute constant.

For$h \in \mathrm { { G L } _ { 3 } ^ { + } ( \mathbb { R } ) }$, we regard$F h \cdot L ^ { \pm }$as a multiset, where the multiplicity of a point$f \in V _ { \mathbb { R } } ^ { \pm }$is equal to #$\{ g \in \mathcal { F } : f \in g h \cdot L ^ { \pm } \}$. As in [8, §2.1], it follows that for any$h \in \mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$and$f \in V _ { \mathbb { R } } ^ { \pm }$, the$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-orbit of$f$is represented $m ( f )$times in$F h \cdot L ^ { \pm }$, where

$$
m (f) := \# \operatorname{Stab} _ {\mathrm{SL} _ {3} (\mathbb {R})} (f) / \# \operatorname{Stab} _ {\mathrm{SL} _ {3} (\mathbb {Z})} (f);\tag{7}
$$

i.e., the sum of the multiplicity in$F h \cdot L ^ { \pm }$of$f ^ { \prime } ,$over all forms$f ^ { \prime }$that are $\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-equivalent to$f ,$is equal to$m ( f )$

For any given$A \in \mathrm { S L _ { 3 } ( Z ) }$, the set of elements in$V _ { \mathbb { R } }$fixed by A has measure 0. Since$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$is countable, we see that the set$\{ f \in V _ { \mathbb { R } } : \# \mathrm { S t a b } _ { \mathrm { S L } _ { 3 } ( \mathbb { Z } ) } ( f ) > 1 \}$ has measure 0 as well. Thus, by Lemma 12, the multiset$F h \cdot L ^ { \pm }$is essentially the union of three fundamental domains for the action of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$on$V _ { \mathbb { R } } ^ { \pm }$

For$h \in \mathrm { G L _ { 3 } ^ { + } } ( \mathbb { R } )$, let$\mathcal { R } _ { X } ( h \cdot L ^ { + } )$and$\mathcal { R } _ { X } ( h \cdot L ^ { - } )$denote the multisets defined by

$$
\mathcal {R} _ {X} (h \cdot L ^ {\pm}) := \{f \in \mathcal {F} h \cdot L ^ {\pm}: H (f) <   X \}.
$$

We will show (cf. Lemma 19) that the number of elements in$\mathcal { R } _ { X } ( h \cdot L ^ { \pm } )$having nontrivial stabilizer in$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$(in fact, in$\mathrm { S L _ { 3 } ( \mathbb { Q } ) }$is negligible. It follows, by (7) and Lemma 12, that the quantity$3 N ( V _ { \mathbb { Z } } ^ { \pm } ; X )$is equal to the number of strongly irreducible integral ternary cubic forms contained in$\mathcal { R } _ { X } ( h \cdot L ^ { \pm } )$, up to an error of$o ( X ^ { 5 / 6 } )$

Counting strongly irreducible integer points in a single such$\mathcal { R } _ { X } ( h \cdot L ^ { \pm } )$is dificult because the domain$\mathcal { R } _ { X } ( h \cdot L ^ { \pm } )$is unbounded (although we will show that it has finite volume). As in [8], we simplify the counting by averaging over lots of such domains, i.e., by averaging over a continuous range of elements h lying in a certain fixed compact subset of$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$

2.2. Averaging and cutting of the cusp. Let$G _ { 0 } \subset \mathrm { G L } _ { 3 } ^ { + } ( \mathbb { R } )$be a compact semialgebraic K-invariant subset that is the closure of some nonempty open set in$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$, such that every element in$G _ { 0 }$has determinant greater than 1. For any$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$)-invariant set$S \subset V _ { \mathbb { Z } } ^ { \pm }$, let$S ^ { \mathrm { i r r } }$denote the set of strongly irreducible elements of S. We pick dh to be a Haar measure on$\mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$, and we normalize dh as follows: if$h \in \mathrm { G L _ { 3 } ^ { + } ( \mathbb { R } ) }$is equal to$h = n ( u ) a ( s _ { 1 } , s _ { 2 } ) k \lambda$in its Iwasawa decomposition, then

$$
d h = s _ {1} ^ {- 6} s _ {2} ^ {- 6} d u d ^ {\times} s d k d ^ {\times} \lambda ,
$$

where dk is Haar measure on$K$normalized so that K has measure 1. Then we have

$$
N (S; X) = \frac {\int_ {h \in G _ {0}} \# \{\mathcal {R} _ {X} (h \cdot L) \cap S ^ {\mathrm{irr}} \} d h}{C _ {G _ {0}}} + o (X ^ {5 / 6}),\tag{8}
$$

where$L = L ^ { \pm }$and$\begin{array} { r } { C _ { G _ { 0 } } = 3 \int _ { h \in G _ { 0 } } d h } \end{array}$

For na$( s _ { 1 } , s _ { 2 } ) \lambda \in \mathcal { F }$, let us write

$$
B (n, s _ {1}, s _ {2}, \lambda , X) := \{f \in n a (s _ {1}, s _ {2}) \lambda G _ {0} \cdot L: H (f) <   X \}.
$$

We then have the following equality, which follows from an argument identical to the proof of [8, Th. 2.5]:

$$
\begin{array}{l} N (S; X) \\ = \frac {1}{C _ {G _ {0}}} \int_ {g \in N ^ {\prime} (a) A ^ {\prime} \Lambda} \# \{S ^ {\mathrm{irr}} \cap B (n, s _ {1}, s _ {2}, \lambda , X) \} s _ {1} ^ {- 6} s _ {2} ^ {- 6} d n d ^ {\times} t d ^ {\times} \lambda + o (X ^ {5 / 6}). \end{array} \tag {9}
$$

To simplify the right-hand side of (9), we require the following lemma, which states that the set$B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$contains no strongly irreducible integral points if s<sub>1</sub> or s<sub>2</sub> is large enough (i.e., when we are in the “cuspidal regions” of the fundamental domains).

Lemma 13. Let$C > 1$be a constant that bounds the absolute values of the $x ^ { 3 } - , x ^ { 2 } y - , x y ^ { 2 } -$, and x<sup>2</sup>z-coeficients of all the forms in$G _ { 0 } \cdot L ^ { \pm }$. Then the set $B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$contains no strongly irreducible integral ternary cubic forms $i f s _ { 1 } > C ^ { 1 / 3 } \lambda / c$or if$s _ { 2 } > C ^ { 1 / 3 } \lambda / c ^ { 2 }$

Proof. It is easy to see that if$s _ { 1 } > C ^ { 1 / 3 } \lambda / c .$, then the absolute values of the $x ^ { 3 } - , x ^ { 2 } y - ,$and x<sup>2</sup>z-coeficients of any ternary cubic form in$B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$ are all less than 1. Therefore, in this case any integral ternary cubic form in$B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$must have its$x ^ { 3 } - , \ x ^ { 2 } y -$, and$x ^ { 2 } z$-coeficients equal to$0 ,$ and such a form has a rational flex at$[ 1 : 0 : 0 ] \in \mathbb { P } ^ { 2 }$and so is not strongly irreducible.

Similarly, if$s _ { 2 } ~ > ~ C ^ { 1 / 3 } \lambda / c ^ { 2 }$, then any integral ternary cubic form in $B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$has its$x ^ { 3 } - , \ x ^ { 2 } y -$, and$x y ^ { 2 } .$-coeficients equal to 0, and such a form too always has a flex at$[ 1 : 0 : 0 ] \in \mathbb { P } ^ { 2 }$and so is not strongly irreducible.

Now let$V _ { \mathbb { Z } } ^ { \mathrm { r e d } }$denote the set of all integral ternary cubic forms that are not strongly irreducible. Then we have the following lemma, which states that the number of reducible points—i.e., points in$V _ { \mathbb { Z } } ^ { \mathrm { r e d } } -$that are in the “main body” of the fundamental domains is negligible.

Lemma 14. Let${ \mathcal { F } } ^ { \prime }$denote the set of elements na$( s _ { 1 } , s _ { 2 } ) \lambda k \in \mathcal { F }$that satisfy$s _ { 1 } < C ^ { 1 / 3 } \lambda / c$and$s _ { 2 } < C ^ { 1 / 3 } \lambda / c ^ { 2 }$. Then

$$
\int_ {n a (s _ {1}, s _ {2}) \lambda k \in \mathcal {F} ^ {\prime}} \# \{V _ {\mathbb {Z}} ^ {\text {red}} \cap B (n, s _ {1}, s _ {2}, \lambda , X) \} s _ {1} ^ {- 6} s _ {2} ^ {- 6} d n   d ^ {\times} t   d ^ {\times} \lambda d k = o (X ^ {5 / 6}).
$$

We defer the proof of Lemma 14 to Section 2.5.

To estimate the number of integral points in$B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$, we use the following proposition due to Davenport [15].

Proposition 15. Let R be a bounded, semi-algebraic multiset in$\mathbb { R } ^ { n }$having maximum multiplicity m and that is defined by at most k polynomial inequalities each having degree at most \`. Then the number of integer lattice points (counted with multiplicity) contained in R is

$$
\operatorname{Vol} (\mathcal {R}) + O \left(\max \left\{\operatorname{Vol} (\bar {\mathcal {R}}), 1 \right\}\right),
$$

where$\operatorname { V o l } ( \bar { \mathcal { R } } )$denotes the greatest d-dimensional volume of any projection of R onto a coordinate subspace obtained by equating$n - d$coordinates to zero, where d takes all values from 1 to$n - 1$. The implied constant in the second summand depends only on n, m, k, and \`.

Since every element of$G _ { 0 }$was assumed to have determinant greater than 1, the set$B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$is empty unless$c _ { 1 } \leq \lambda \leq X ^ { 1 / 3 6 }$, where$c _ { 1 }$is a constant such that$1 / c _ { 1 } ^ { 3 }$bounds the determinants of all the elements in$G _ { 0 }$from above. By equation (9), Lemmas 13 and 14, and Proposition 15, we see that$N ( V _ { \mathbb { Z } } ^ { \pm } ; X )$ equals

$$
\frac{1}{C_{G_{0}}}\int_{\substack{na(s_{1},s_{2})\lambda k\in \mathcal{F}^{\prime}\\ c_{1}\leq \lambda \leq X^{1 / 36}}}\bigl (\operatorname{Vol}(B(n,s_{1},s_{2},\lambda ,X)) + O(\operatorname{Vol}(\overline{B(n,s_{1},s_{2},\lambda,X)}))\bigr)\tag{10}
$$

$$
\times s _ {1} ^ {- 6} s _ {2} ^ {- 6} d n d ^ {\times} s d ^ {\times} \lambda d k + o (X ^ {5 / 6})
$$

because Vol$( \overline { { B ( n , s _ { 1 } , s _ { 2 } , \lambda , X ) } } ) \gg 1$when$\lambda \geq c _ { 1 }$

It is easily checked that when$n a ( s _ { 1 } , s _ { 2 } ) \lambda k \in \mathcal { F } ^ { \prime }$and$\lambda \geq c _ { 1 }$, the projection of$B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$onto any coordinate in$V _ { \mathbb { R } } .$, apart from the$x ^ { 3 } -$and$x ^ { 2 } y -$ coeficients, is bounded below independent of$n , s _ { 1 } , s _ { 2 }$, and λ. (For example, the projection of$B ( n , s _ { 1 } , s _ { 2 } , \lambda , X )$onto the$x ^ { 2 } .$z-coeficient is bounded below by an absolute constant times$\lambda ^ { 3 } s _ { 1 } ^ { - 3 }$, which is bounded from below since$\lambda \geq c _ { 1 }$ and$s _ { 1 } \ll \lambda . )$Thus, the integral of the error term in the integrand of (10) is computed to be

$$
O \Bigl (\int_ {\lambda = 0} ^ {X ^ {1 / 3 6}} \int_ {s _ {1}, s _ {2} = c} ^ {\lambda} (\lambda^ {2 7} s _ {1} ^ {6} s _ {2} ^ {3} + \lambda^ {2 4} s _ {1} ^ {9} s _ {2} ^ {6}) s _ {1} ^ {- 6} s _ {2} ^ {- 6} d ^ {\times} s d ^ {\times} \lambda \Bigr) = O (X ^ {3 / 4}).
$$

Meanwhile, the integral of the main term in the integrand of (10) is equal to

$$
\begin{array}{l}\frac{1}{C_{G_{0}}}\int_{\substack{na(s_{1},s_{2})\lambda k\in \mathcal{F}^{\prime}\\ c_{1}\leq \lambda \leq X^{1 / 36}}}\big(\operatorname{Vol}(B(n,s_{1},s_{2},\lambda ,X))s_{1}^{-6}s_{2}^{-6}dn  d^{\times}s  d^{\times}\lambda   dk\\ \\ = \frac{1}{C_{G_{0}}}\int_{h\in G_{0}}\operatorname{Vol}(\mathcal{R}_{X}(h\cdot L^{\pm}))dh\\ \\ -O\Big(\int_{na(s_{1},s_{2})\lambda k\in \mathcal{F} / \mathcal{F}^{\prime}}\lambda^{30}s_{1}^{-6}s_{2}^{-6}dn  d^{\times}s  d^{\times}\lambda \\ \\ +\int_{na(s_{1},s_{2})\lambda k\in \mathcal{F}}\lambda^{30}s_{1}^{-6}s_{2}^{-6}dn  d^{\times}s  d^{\times}\lambda \Big)\\ \end{array}
$$

since$\mathrm { V o l } ( B ( n , s _ { 1 } , s _ { 2 } , \lambda , X ) ) = { \cal O } ( \lambda ^ { 3 0 } )$. The error term in the above equation is computed to be$O ( X ^ { 2 / 3 } )$. Hence it follows from equation (10), and the fact that$\mathrm { V o l } ( \mathcal { R } _ { X } ( h \cdot L ^ { \pm } ) )$) is independent of$h ,$that

$$
N (V _ {\mathbb {Z}} ^ {\pm}; X) = \frac {1}{3} \mathrm{Vol} (\mathcal {R} _ {X} (L ^ {\pm})) + o (X ^ {5 / 6}).\tag{11}
$$

Therefore, to prove Theorem 11, it remains only to compute the volume $\mathrm { V o l } ( \mathcal { R } _ { X } ( L ^ { \pm } ) )$

2.3. Computing the volume. In this section, we compute the volumes of $\mathcal { R } _ { X } ( L ^ { \pm } )$. To this end, let$R ^ { \pm } : = \Lambda \cdot L ^ { \pm }$. Then the sets$R ^ { \pm }$consist of one element in$V _ { \mathbb { R } } ^ { \pm }$having invariants$( I , J )$for each$( I , J ) \in \mathbb { R } \times$R such that $\pm \Delta ( I , J ) \in \mathbb { R } _ { > 0 }$. Let$R ^ { \pm } ( X )$denote the set of points in$R ^ { \pm }$having height bounded by$X$. For a ring$T$, define the twisted action of the group$\mathrm { G L _ { 3 } } ( T )$ on the space$V _ { T }$of ternary cubic forms having coeficients in$T$by

$$
\gamma \cdot f (x, y, z) := \det (\gamma) ^ {- 1} f ((x, y, z) \cdot \gamma);\tag{12}
$$

this induces an action of$\mathrm { P G L _ { 3 } } ( T )$on$V _ { T }$. Let$\mathcal { F } _ { \mathrm { P G L _ { 3 } } }$denote the image in $\mathrm { P G L _ { 3 } ( \mathbb { R } ) }$of$\mathcal { F }$. Then$\mathcal { F } _ { \mathrm { P G L _ { 3 } } }$is a fundamental domain for the action of$\mathrm { P G L _ { 3 } ( Z ) }$ on$\mathrm { P G L _ { 3 } ( \mathbb { R } ) }$. We have$\mathscr { R } _ { X } ( L ^ { \pm } ) = \mathscr { F } _ { \mathrm { P G L } _ { 3 } } \cdot R ^ { \pm } ( X )$

Let$\omega$be a diferential that generates the rank 1 module of top-degree diferentials of$\mathrm { P G L _ { 3 } }$over$\mathbb { Z } .$. Then$\omega$is well defined up to sign. To compute the volume of the multiset${ \mathcal { F } } _ { \mathrm { P G L 3 } } \cdot R ^ { \pm } ( X )$, we have the following proposition.

Proposition 16. For any measurable function$\phi$on$V _ { \mathbb { R } }$, we have

$$
\frac {4}{9} \int_ {R ^ {\pm}} \int_ {\mathrm{PGL} _ {3} (\mathbb {R})} \phi (g \cdot p _ {I, J})   \omega (g)   d I d J = \int_ {\mathrm{PGL} _ {3} (\mathbb {R}) \cdot R ^ {\pm}} \phi (v) d v = 3 \int_ {V _ {\mathbb {R}} ^ {\pm}} \phi (v) d v, \tag {13}
$$

where$p _ { I , J } \in R ^ { \pm }$is the point having invariants equal to I and J and we regard $\mathrm { P G L _ { 3 } } ( \mathbb { R } ) \cdot R ^ { \pm }$as a multiset.

The above proposition may be verified by a direct Jacobian computation. We will also give a more noncomputational proof in Section 3.2.

Since the volume of$\mathcal { F } _ { \mathrm { { P G L } _ { 3 } } }$is equal to$3 \zeta ( 2 ) \zeta ( 3 )$(see [24]), we have

$$
\begin{array}{r l} & {\int_ {\mathcal {R} _ {X} (L ^ {\pm})} d v = \int_ {\mathcal {F} _ {\mathrm{PGL} _ {3}} \cdot R ^ {\pm} (X)} d v} \\ & {\qquad = \frac {4}{9} \int_ {R ^ {\pm} (X)} \int_ {\mathcal {F} _ {\mathrm{PGL} _ {3}}} \omega (g) d I d J = \frac {4 \zeta (2) \zeta (3)}{3} \int_ {R ^ {\pm} (X)} d I d J.} \end{array}\tag{14}
$$

The quantity$\int _ { R ^ { + } ( X ) }$dI dJ is equal to

$$
\int_ {I = 0} ^ {X ^ {1 / 3}} \int_ {J = - 2 I ^ {3 / 2}} ^ {2 I ^ {3 / 2}} d J d I = \int_ {I = 0} ^ {X ^ {1 / 3}} 4 I ^ {3 / 2} d I = \frac {8}{5} X ^ {5 / 6},\tag{15}
$$

while$\int _ { R ^ { - } ( X ) }$dI dJ is equal to

$$
\int_ {I = - X ^ {1 / 3}} ^ {X ^ {1 / 3}} \int_ {J = - 2 X ^ {1 / 2}} ^ {2 X ^ {1 / 2}} d J d I - \int_ {R _ {V} ^ {+} (X)} d I d J = 8 X ^ {5 / 6} - \frac {8}{5} X ^ {5 / 6} = \frac {3 2}{5} X ^ {5 / 6}.\tag{16}
$$

We conclude that

$$
\mathrm{Vol} (\mathcal {R} _ {X} (L ^ {+})) = \frac {3 2 \zeta (2) \zeta (3)}{1 5} X ^ {5 / 6},\tag{17}
$$

$$
\mathrm{Vol} (\mathcal {R} _ {X} (L ^ {-})) = \frac {1 2 8 \zeta (2) \zeta (3)}{1 5} X ^ {5 / 6},
$$

which along with (11) yields Theorem 11.

2.4. Congruence conditions. In this subsection, we prove a version of Theorem 11 where we count integral ternary cubic forms satisfying any finite set of congruence conditions.

For any set$S$in$V _ { \mathbb { Z } }$that is definable by congruence conditions, we denote by$\mu _ { p } ( S )$the p-adic density of the p-adic closure of S in$V _ { \mathbb { Z } _ { p } } .$where we normalize the additive measure$\mu _ { p }$on$V _ { \mathbb { Z } _ { p } }$so that$\mu _ { p } ( V _ { \mathbb { Z } _ { p } } ) = 1$. We then have the following theorem, whose proof is identical to that of [8, Th. 2.11].

Theorem 17. Suppose$S$is a subset of$V _ { \mathbb { Z } } ^ { \pm }$defined by finitely many congruence conditions. Then we have

$$
N (S \cap V _ {\mathbb {Z}} ^ {\pm}; X) = N (V _ {\mathbb {Z}} ^ {\pm}; X) \prod_ {p} \mu_ {p} (S) + o (X ^ {5 / 6}),\tag{18}
$$

where$\mu _ { p } ( S )$denotes the p-adic density of$S$in$V _ { \mathbb { Z } }$and where the implied constant in$o ( X ^ { 5 / 6 } )$depends only on$S .$

We will also have occasion to use the following weighted version of Theorem$1 7 ;$the proof is identical to that of [8, Th. 2.12].

Theorem 18. Let$p _ { 1 } , \ldots , p _ { k }$be distinct prime numbers. For$j = 1 , \dots , k$ let$\phi _ { p _ { j } } : V _ { \mathbb { Z } } \to \mathbb { R }$be an$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-invariant function on$V _ { \mathbb { Z } }$such that$\phi _ { p _ { j } } ( f )$ depends only on the congruence class of f modulo some power$p _ { j } ^ { a _ { j } }$of$p _ { j }$. Let $N _ { \phi } ( V _ { \mathbb { Z } } ^ { \pm } ; X )$denote the number of strongly irreducible$\mathrm { { S L _ { 3 } ( Z ) } }$-orbits in$V _ { \mathbb { Z } } ^ { \pm }$having height bounded by$X$, where each orbit$\operatorname { S L } _ { 3 } ( \mathbb { Z } ) \cdot f$is counted with weight $\textstyle \phi ( f ) : = \prod _ { j = 1 } ^ { k } \phi _ { p _ { j } } ( f )$. Then we have

$$
N _ {\phi} (V _ {\mathbb {Z}} ^ {\pm}; X) = N (V _ {\mathbb {Z}} ^ {\pm}; X) \prod_ {j = 1} ^ {k} \int_ {f \in V _ {\mathbb {Z} _ {p _ {j}}}} \tilde {\phi} _ {p _ {j}} (f) d f + o (X ^ {5 / 6}),\tag{19}
$$

where$\tilde { \phi } _ { p _ { j } }$is the natural extension of$\phi _ { p _ { j } }$to$V _ { \mathbb { Z } _ { p _ { j } } }$by continuity, df denotes the additive measure on$V _ { \mathbb { Z } _ { p _ { j } } }$normalized so that$\begin{array} { r } { \int _ { f \in V _ { \mathbb { Z } _ { p _ { i } } } } d f = 1 } \end{array}$, and where the implied constant in the error term depends only on the local weight functions$\phi _ { p _ { j } }$

2.5. The number of reducible points and points with large stabilizers in the main bodies of the fundamental domains is negligible. In this section, we prove Lemma 14, i.e., that the number of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-orbits of reducible elements in$V _ { \mathbb { Z } }$of bounded height is negligible. Via a similar argument, we also show that the number of$\mathrm { { S L _ { 3 } ( Z ) } }$-orbits of strongly irreducible elements in$V _ { \mathbb { Z } }$having nontrivial stabilizer in$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$and bounded height is negligible. We use the technique in the proof of [5, Lemma 14].

Proof of Lemma 14. Suppose$f$is an integral ternary cubic form. If$f$has a rational flex in$\mathbb { P } ^ { 2 }$, then for any prime$p ,$the reduction$\bar { f }$of$f$modulo$p$has a point of inflection in$\mathbb { P } ^ { 2 } ( \mathbb { F } _ { p } )$. Now let$p$be a prime that is congruent to 1 (mod 3), and let$a , b , c$be elements in$\mathbb { F } _ { p } ^ { \times }$that are in diferent cube classes$( \mathrm { i . e . }$ none of$a / b , b / c , c / a$are cubes in$\mathbb { F } _ { p } ^ { \times } )$. Then one easily checks that the ternary cubic form$f _ { a , b , c } ( x , y , z ) = a x ^ { 3 } + b y ^ { 3 } + c z ^ { 3 } \in V _ { \mathbb { F } _ { p } }$has no point of inflection in$\mathbb { F } _ { p } .$ Hence none of the forms in the set$S _ { p } = \{ \gamma \cdot f _ { a , b , c } : \gamma \in \operatorname { G L } _ { 3 } ( \mathbb { F } _ { p } ) \}$contain points of inflection in$\mathbb { F } _ { p }$. It is clear that$\# S _ { p } \gg p ^ { 9 }$, where the implied constant is independent of$p .$. Thus, if$s _ { p }$denotes the p-adic density of the set of elements in $V _ { \mathbb { Z } }$whose reduction modulo$p$is contained in$S _ { p } { } _ { ; }$, then$s _ { p } \gg p ^ { 9 } / p ^ { 1 0 } = 1 / p .$, where the implied constant is independent of$p .$Therefore, for any$Y > 0$, we have

$$
\begin{array}{l}\int_{na(s_{1},s_{2})\lambda k\in \mathcal{F}^{\prime}}\# \{V_{\mathbb{Z}}^{\mathrm{red}}\cap B(n,s_{1},s_{2},\lambda ,X)\} s_{1}^{-6}s_{2}^{-6}dn  d^{\times}t  d^{\times}\lambda dk\\ \ll X^{5 / 6}\prod_{\substack{p\equiv 1 (\mathrm{mod} 3)\\ p\leq Y}}(1 - s_{p}). \end{array}\tag{20}
$$

Since$s _ { p } \gg 1 / p$, it follows that$\begin{array} { r } { \prod _ { p \equiv 1 ( \mathrm { m o d } ~ 3 ) } ( 1 - s _ { p } ) } \end{array}$diverges, and hence the left-hand side of (20) is$o ( X ^ { 5 / 6 } )$as required.

We may use the same method to bound the number of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-orbits on strongly irreducible integral ternary cubic forms having bounded height and nontrivial stabilizer in$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$, i.e., integral ternary cubic forms of bounded height whose associated cubic curves have no rational flex in$\mathbb { P } ^ { 2 }$, but whose Jacobians possess a nontrivial 3-torsion point defined over$\mathbb { Q }$(see Proposition 28).

Lemma 19. Let$V _ { \mathbb { Z } } ^ { \mathrm { b i g s t a b } }$denote the set of elements in$V _ { \mathbb { Z } }$whose stabilizer in$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$is nontrivial. Then$N ( V _ { \mathbb { Z } } ^ { \mathrm { b i g s t a b } } ; X ) = o ( X ^ { 5 / 6 } )$

Proof. By equation (9) and Lemma 13, it sufices to prove the estimate (21)

$$
\int_ {n a (s _ {1}, s _ {2}) \lambda k \in \mathcal {F} ^ {\prime}} \# \{V _ {\mathbb {Z}} ^ {\text {bigstab}} \cap B (n, s _ {1}, s _ {2}, \lambda , X) \} s _ {1} ^ {- 6} s _ {2} ^ {- 6} d n   d ^ {\times} t   d ^ {\times} \lambda d k = o (X ^ {5 / 6}).
$$

The Jacobian of the cubic curve defined by the vanishing of a ternary cubic form$f \in V _ { \mathbb { Z } }$may be embedded in$\mathbb { P } ^ { 2 }$as a Weierstrass elliptic curve$\operatorname { J a c } ( f )$via the equation

$$
y ^ {2} z = x ^ {3} - \frac {I (f)}{3} x z ^ {2} - \frac {J (f)}{2 7} z ^ {3},
$$

and under this embedding, the 3-torsion points of$\operatorname { J a c } ( f )$are precisely its flex points. Thus an integral ternary cubic form$f$is contained in$V _ { \mathbb { Z } } ^ { \mathrm { b i g s t a b } }$if and only if the curve$\operatorname { J a c } ( f )$contains at least two rational flex points in$\mathbb { P } ^ { 2 }$. The proof of the estimate in (21) now proceeds very similarly to that of Lemma 14. The only diference is that we now consider, for each$p \equiv 7$(mod 12), the form $f _ { b } ( x , y , z ) = x ^ { 3 } + b z ^ { 3 } - y ^ { 2 } z \in V _ { \mathbb { F } _ { p } }$, where b is a nonresidue in$\mathbb { F } _ { p }$. We see that $\operatorname { J a c } ( f _ { b } )$is then precisely the curve defined by the equation$f _ { b } = 0$, and it has exactly one inflection point in$\mathbb { P } ^ { 2 } ( \mathbb { F } _ { p } )$, namely the point$[ 0 : 1 : 0 ]$

2.6. The average number of strongly irreducible integral ternary cubic forms with given invariants (Proofs of Theorems 9 and 10). We first prove Theorem 9 by describing the set of eligible pairs$\begin{array} { r } { ( I , J ) \in \frac { 1 } { 1 6 } \mathbb { Z } \times \frac { 1 } { 3 2 } \mathbb { Z } . } \end{array}$i.e., those pairs that occur as invariants of integral ternary cubic forms. We begin by showing that a pair$( I , J )$is eligible if and only if it occurs as the invariants of a Weierstrass elliptic curve over$\mathbb { Z } .$

Proposition 20. A pair$( I , J )$is eligible if and only$i f$it occurs as the invariants$o f$some Weierstrass cubic over$\mathbb { Z } .$where a Weierstrass cubic over $\mathbb { Z }$is an element in$V _ { \mathbb { Z } }$of the form

$$
y ^ {2} z + a _ {1} x y z + a _ {3} y z ^ {2} - x ^ {3} - a _ {2} x ^ {2} z - a _ {4} x z ^ {2} - a _ {6} z ^ {3}.
$$

Proof. This proposition is easily deduced from the results in [3]. To any integral ternary cubic form$f \in V _ { \mathbb { Z } }$, one may associate a Weierstrass ternary cubic form$f ^ { * }$over$\mathbb { Z }$that defines the Jacobian curve (see [3, eq. 1.5]). The invariants$c _ { 4 } ( f )$and$c _ { 6 } ( f )$of$f$are then defined to be equal to the classical invariants$c _ { 4 } ( f ^ { * } )$and$c _ { 6 } ( f ^ { * } )$of the corresponding Weierstrass cubic. (See [27] for a definition of$c _ { 4 } ( f ^ { * } )$and$c _ { 6 } ( f ^ { * } ) . )$Using [3, eq. 1.7], we easily check that our invariants$I ( f )$and$J ( f )$are equal to the invariants$c _ { 4 } ( f ) / 1 6$and$c _ { 6 } ( f ) / 3 2$, respectively, for any ternary cubic form$f .$. We conclude that$I ( f ) = I ( f ^ { * } )$and $J ( f ) = J ( f ^ { * } )$, as desired.

Next, we have a result of Kraus (see [22, Prop. 2]), which describes those pairs$( c _ { 4 } , c _ { 6 } )$that can occur for a Weierstrass cubic over$\mathbb { Z }$

Proposition 21. Let$c _ { 4 }$and$c _ { 6 }$be integers. In order for there to exist a Weierstrass cubic over$\mathbb { Z }$having nonzero discriminant and invariants$c _ { 4 }$and $c _ { 6 }$, it is necessary and suficient that

(a)$( c _ { 4 } ^ { 3 } - c _ { 6 } ^ { 2 } ) / 1 7 2 8$is a nonzero integer ;

(b)$c _ { 6 } \not \equiv \pm 9$(mod 27);

(c) either$c _ { 6 } \equiv - 1$(mod 4), or$c _ { 4 } \equiv 0$(mod 16) and$c _ { 6 } \equiv 0 , 8$(mod 32).

It can be checked that the set of pairs$( I , J )$that satisfy the congruence conditions of Theorem 9 is the same as the set of pairs$( c _ { 4 } / 1 6 , c _ { 6 } / 3 2 )$for which the congruence conditions of Proposition 21 are satisfied for$( c _ { 4 } , c _ { 6 } )$. Thus Theorem 9 follows from Propositions 20 and 21 and the fact that$I ( f ) = c _ { 4 } ( f ) / 1 6$ and$J ( f ) = c _ { 6 } ( f ) / 3 2$for Weierstrass cubics$f$having integral coeficients.

The next lemma follows immediately from Theorem 9.

Lemma 22. The set of all eligible$( I , J )$is a union of 144 distinct translates$o f 3 6  { \mathbb { Z } } \times 2 7  { \mathbb { Z } }$in${ \frac { 1 } { 1 6 } } \mathbb { Z } \times { \frac { 1 } { 3 2 } } \mathbb { Z }$

Proposition 23. Let$N _ { I , J } ^ { + } ( X )$and$N _ { I , J } ^ { - } ( X )$denote the number of eligible pairs$( I , J ) \in { \frac { 1 } { 1 6 } } \mathbb { Z } \times { \frac { 1 } { 3 2 } } \mathbb { Z }$satisfying$H ( I , J ) < X$that have positive discriminant and negative discriminant, respectively. Then

$$
\mathrm{(a)} N _ {I, J} ^ {+} (X) = \frac {3 2}{1 3 5} X ^ {5 / 6} + O (X ^ {1 / 2});
$$

$$
\text {(a)} N _ {I, J} ^ {-} (X) = \frac {1 2 8}{1 3 5} X ^ {5 / 6} + O (X ^ {1 / 2}).
$$

Proof. Let$R _ { I , J } ^ { + } ( X )$(resp.$R _ { I , J } ^ { - } ( X ) )$denote the set of points$( i , j ) \in \mathbb { R } \times \mathbb { R }$ satisfying$H ( i , j ) < X$and$4 i ^ { 3 } - { j ^ { 2 } } > 0$(resp.$4 i ^ { 3 } - j ^ { 2 } < 0 )$). The sizes of the projections of$R _ { I , J } ^ { \pm } ( X )$onto smaller-dimensional coordinate hyperplanes are all bounded by$O ( X ^ { 1 / 2 } )$. Using Proposition 15 and Lemma 22 then gives

$$
N _ {I, J} ^ {\pm} (X) = \frac {1 4 4}{3 6 \cdot 2 7} \operatorname{Vol} \left(R _ {I, J} ^ {\pm} (X)\right) + O \left(X ^ {1 / 2}\right).
$$

The volumes of the sets$R _ { I , J } ^ { + } ( X )$and$R _ { I , J } ^ { - } ( X )$have been computed in (15) and (16) to be equal to$8 / 5$and$3 2 / 5$, respectively. The proposition follows. 

Theorem 8 combined with Proposition 23 now yields Theorem 10.

2.7. Uniformity estimates and a squarefree sieve. For our applications, we require a general version of Theorem 18, namely, one that counts weighted ternary cubic forms where the weight functions are defined by appropriate infinite sets of congruence conditions. A function$\phi : V _ { \mathbb { Z } } \to [ 0 , 1 ] \in \mathbb { R }$is said to be defined by congruence conditions if, for all primes$p ,$there exist functions $\phi _ { p } : V _ { \mathbb { Z } _ { p } } \to [ 0 , 1 ]$satisfying the following conditions:

(1) For all$f \in V _ { \mathbb { Z } } .$, the product$\Pi _ { p } \phi _ { p } ( f )$converges to$\phi ( f )$

(2) For each prime$p ,$the function$\phi _ { p }$is locally constant outside some closed set$S _ { p } \subset V _ { \mathbb { Z } _ { p } }$of measure zero.

We say that such a function φ is acceptable if for suficiently large primes$p ,$we have$\phi _ { p } ( f ) = 1$whenever$p ^ { 2 } \nmid \Delta ( f )$

Our purpose in this section is to prove the following generalization of Theorem 18.

Theorem 24. Let$\phi : V _ { \mathbb { Z } } \to [ 0 , 1 ]$be an acceptable function that is defined by congruence conditions via the local functions$\phi _ { p } : V _ { \mathbb { Z } _ { p } } \to [ 0 , 1 ]$. Then, with notation as in Theorem 18, we have

$$
N _ {\phi} (V _ {\mathbb {Z}} ^ {\pm}; X) = N (V _ {\mathbb {Z}} ^ {\pm}; X) \prod_ {p} \int_ {f \in V _ {\mathbb {Z} _ {p}}} \phi_ {p} (f) d f + o (X ^ {5 / 6}).\tag{22}
$$

To prove Theorem 24, we follow the method of [6]. We establish the following tail estimate.

Proposition 25. Let$\mathcal { W } _ { p } ( V )$denote the set of ternary cubic forms f such that$p ^ { 2 } \mid \Delta ( f )$. Then, for any fixed$\epsilon > 0$, we have

$$
N (\cup_ {p > M} \mathcal {W} _ {p}; X) = O _ {\epsilon} (X ^ {5 / 6} / (M \log M) + X ^ {3 / 4}) + O (\epsilon X ^ {5 / 6}).\tag{23}
$$

Proof. If$p ^ { 2 } \le X ^ { 1 / 1 2 }$, then the counting method of Sections 2.2–2.4, with the relevant congruence conditions modulo$p ^ { 2 }$imposed, immediately yields the individual estimate$N ( W _ { p } ; X ) = O ( X ^ { 5 / 6 } / p ^ { 2 } )$(noting that$\mathcal { R } _ { X } ( L ^ { \pm } ) =$ $X ^ { 1 / 1 2 } \mathcal { R } _ { 1 } ( L ^ { \pm } ) )$. Hence, to prove Proposition 25, it sufices to assume that $M > X ^ { 1 / 2 4 }$

Let$\mathcal { W } _ { p } ^ { ( 1 ) }$denote the set of ternary cubic forms such that$p ^ { 2 } \mid \Delta ( f )$for “mod$p$reasons,” i.e.,$p ^ { 2 } \mid \Delta ( g )$for every$g \equiv f { \pmod { p } }$. For any$\epsilon > 0$，let$\mathcal { F } _ { \mathrm { P G L 3 } } ^ { ( \epsilon ) } \subset \mathcal { F } _ { \mathrm { P G L 3 } }$denote the subset of elements$n a ( s _ { 1 } , s _ { 2 } ) k \in \mathcal { F } _ { \mathrm { P G L 3 } }$such that$s _ { 1 }$and$s _ { 2 }$are bounded above by an appropriate constant to ensure that $\mathrm { V o l } ( \mathcal { F } _ { \mathrm { P G L } _ { 3 } } ^ { ( \epsilon ) } ) = ( 1 - \epsilon ) \mathrm { V o l } ( \mathcal { F } _ { \mathrm { P G L } _ { 3 } } )$. Then$\mathcal { F } _ { \mathrm { P G L 3 } } ^ { ( \epsilon ) } \cdot R ^ { \pm } ( X )$is a bounded domain in$V _ { \mathbb { R } }$that expands homogeneously with X. By [6, Th. 3.3], we have

$$
\# \{\mathcal {F} _ {\mathrm{PGL} _ {3}} ^ {(\epsilon)} \cdot R ^ {\pm} (X) \bigcap (\cup_ {p > M} \mathcal {W} _ {p} ^ {(1)}) \} = O (X ^ {5 / 6} / (M \log M) + X ^ {9 / 1 2}).\tag{24}
$$

Furthermore, the results of Sections 2.1 and 2.2 imply that

$$
\# \{(\mathcal {F} _ {\mathrm{PGL} _ {3}} \backslash \mathcal {F} _ {\mathrm{PGL} _ {3}} ^ {(\epsilon)}) \cdot R ^ {\pm} (X) \bigcap V _ {\mathbb {Z}} ^ {\mathrm{irr}} \} = O (\epsilon X ^ {5 / 6}).\tag{25}
$$

Combining the two estimates (24) and (25) yields (23) with$\mathcal { W } _ { p }$replaced with $\mathcal { W } _ { p } ^ { ( 1 ) }$

Next, suppose f belongs to$\mathcal { W } _ { p } ^ { ( 2 ) } : = \mathcal { W } _ { p } \backslash \mathcal { W } _ { p } ^ { ( 1 ) }$. Let$\bar { f }$denote the reduction of$f$modulo$p .$Then the curve$C \subset \mathbb { P } _ { \mathbb { F } _ { \tau } } ^ { 2 }$defined by$\bar { f } ( x , y , z ) = 0$contains a single nodal singularity. This singularity must be$\mathbb { F } _ { p } .$-rational, and we can move it to$[ 0 : 0 : 1 ]$using an element of$\mathrm { S L _ { 3 } } ( \mathbb { F } _ { p } )$. In that case, the$z ^ { 3 } \mathrm { - } , x z ^ { 2 } \mathrm { - }$, and$y z ^ { 2 } .$ coeficients of$\bar { f } ( x , y , z )$are zero. Evaluating the discriminant of an element$f$ that reduces mod$p$to such an${ \bar { f } } .$, we see that$\Delta ( f ) \equiv c G ( f )$(mod$p ^ { 2 } )$, where c is the coeficient of$z ^ { 3 }$and$G ( f )$is an irreducible polynomial in the coeficients of$f . \mathrm { ~ A s ~ } f \in \mathcal { W } _ { p } ^ { ( 2 ) }$, we see that$G ( f ) \not \equiv 0$(mod$p )$. Therefore, since$p ^ { 2 } \mid \Delta ( f )$ we obtain that$p ^ { 2 } \mid c ,$the coeficient of$z ^ { 3 }$. Now the element$g$defined by

$$
\left( \begin{array}{c c c} 1 & & \\ & 1 & \\ & & p ^ {- 1} \end{array} \right) \cdot p f\tag{26}
$$

has the same discriminant as$f$and is in$\mathcal { W } _ { p } ^ { ( 1 ) }$, because its$x ^ { 3 } - , \ x ^ { 2 } y - , \ x y ^ { 2 } -$ and$y ^ { 3 } .$-coeficients are zero modulo$p .$We therefore obtain a discriminant preserving map$\phi$from$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-orbits on$\mathcal { W } _ { p } ^ { ( 2 ) }$to$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-orbits on$\mathcal { W } _ { p } ^ { ( 1 ) }$. The following lemma states that this map is at most 3 to 1.

Lemma 26. Given an$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-orbit on$\mathcal { W } _ { p } ^ { ( 1 ) } ,$there are at most three$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$ orbits on$\mathcal { W } _ { p } ^ { ( 2 ) }$that map to it under$\phi .$.

Proof. If the reduction of$f \in \mathcal { W } _ { p } ^ { ( 2 ) }$modulo$p$has a nodal singularity at $[ 0 : 0 : 1 ] \in \mathbb { P } ^ { 2 } ( \mathbb { F } _ { p } )$, then the form in$\bar { W } _ { p } ^ { ( 1 ) }$given by (26), when reduced modulo $p ,$has z as a factor. Moreover, for$g \in W _ { p } ^ { ( 1 ) }$, the form

$$
\left( \begin{array}{c c} 1 & \\ & 1 \\ & p \end{array} \right) \cdot p ^ {- 1} g\tag{27}
$$

can be integral only if the$x ^ { 3 } - , \ x ^ { 2 } y - , \ x y ^ { 2 } -$, and$y ^ { 3 } .$-coeficients of$g$are zero modulo$p .$. Therefore, the preimages under$\phi$of the$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-orbit of$g \in \mathcal { W } _ { p } ^ { ( 1 ) }$ are associated to linear factors of the reduction of g modulo$p$. The reduction of g modulo p has at most three linear factors, unless$g \equiv 0$(mod$p )$. However, if $g \equiv 0$(mod p), then it is easy to see that (27) belongs to$\mathcal { W } _ { p } ^ { ( 1 ) }$. Thus, the map $\phi : \mathrm { S L } _ { 3 } ( \mathbb { Z } ) \backslash \mathcal { W } _ { p } ^ { ( 2 ) }  \mathrm { S L } _ { 3 } ( \mathbb { Z } ) \backslash \mathcal { W } _ { p } ^ { ( 1 ) }$is at most 3-to-1, and the lemma follows. 

Therefore, since discriminants less than X can have at most 24 distinct prime factors$p > X ^ { 1 / 2 4 }$, we obtain

$$
\begin{array}{r l} & N (\cup_ {p > M} \mathcal {W} _ {p} ^ {(2)}; X) \leq 3 \cdot 2 4 N (\cup_ {p > M} \mathcal {W} _ {p} ^ {(1)}; X) \\ & \qquad = O _ {\epsilon} (X ^ {5 / 6} / (M \log M) + X ^ {3 / 4}) + O (\epsilon X ^ {5 / 6}). \end{array}\tag{28}
$$

This concludes the proof of the proposition.

Theorem 24 now follows from Proposition 25 just as [8, Th. 2.21] followed from [8, Th. 2.13].

## 3. The average number of elements in the 3-Selmer groups of elliptic curves

Recall that any isomorphism class of elliptic curve E over$\mathbb { Q }$has a unique representative of the form

$$
E (A, B): y ^ {2} = x ^ {3} + A x + B,\tag{29}
$$

where A,$B \in \mathbb { Z }$and for all primes$p ,$we have$p ^ { 4 } \nmid A { \mathrm { ~ i f ~ } } p ^ { 6 } \mid B$. For any elliptic curve$E ( A , B )$over$\mathbb { Q }$written in the form (29), we define the quantities$I ( E )$ and$J ( E )$by

(30)

$$
\begin{array}{l} I (E) = - 3 A, \\ J (E) = - 2 7 B. \end{array}\tag{31}
$$

We denote the elliptic curve over Q having invariants I and J by$E ^ { I , J }$, and we define its height$H ^ { \prime } ( E ^ { I , J } )$by

$$
H ^ {\prime} (E ^ {I, J}) := \max \{| I ^ {3} |, J ^ {2} / 4 \}.
$$

We use the height$H ^ { \prime }$instead of H on elliptic curves to agree with the height on integral ternary cubic forms defined in (4). Note that since H and$H ^ { \prime }$agree up to a constant factor, they induce the same ordering on the set of elliptic curves over$\mathbb { Q }$

In this section, we prove Theorem 3 by computing the average size of the 3-Selmer group of elliptic curves over$\mathbb { Q } .$, whose coeficients satisfy finitely many congruence conditions, when these curves are ordered by their heights. We also prove a theorem where we bound the average size of the 3-Selmer group of elliptic curves in more general families. To define these families, we need the following notation. For each prime$p ,$let$\Sigma _ { p }$be a closed subset of $\mathbb { Z } _ { p } ^ { 2 } \backslash \{ \Delta \neq 0 \}$. We associate the family$F _ { \Sigma }$of elliptic curves to$( \Sigma _ { p } ) _ { p }$, where $\dot { E ^ { I , J } } \in F _ { \Sigma }$if$( I , J ) \in \Sigma _ { p }$for all$p .$Such a family is said to be defined by congruence conditions. We can also impose “congruence conditions at infinity” by insisting that$E ^ { I , J } \in F _ { \Sigma }$if and only if$( I , J ) \in \Sigma _ { \infty }$, where$\Sigma _ { \infty }$is equal to $\{ ( I , J ) \in \mathbb { R } ^ { 2 } : \Delta ( I , J ) > 0 \} , \{ ( I , J ) \in \mathbb { R } ^ { 2 } : \Delta ( I , J ) < 0 \}$, or$\{ ( I , J ) \in \mathbb { R } ^ { 2 }$: $\Delta ( I , J ) \neq 0 \}$

If F is a family of elliptic curves defined by congruence conditions, then let Inv(F) denote the set$\{ ( I ( E ) , J ( E ) ) : E \in F \}$. For a prime$p ,$let$\operatorname { I n v } _ { p } ( F )$ denote the$p \textmd { - }$adic closure of Inv$( F )$in$\mathbb { Z } _ { p } ^ { 2 }$. We define$\mathrm { I n v } _ { \infty } ( F )$to be$\{ ( I , J ) \in$ $\mathbb { R } ^ { 2 } : \Delta ( I , J ) > 0 \} , \{ ( I , J ) \in \mathbb { R } ^ { 2 } : \Delta ( I , J ) < 0 \} , \mathrm { o r } \ \{ ( I , J ) \in \mathbb { R } ^ { 2 } : \Delta ( I , J ) \neq 0 \}$ in accordance with whether F contains curves only of positive discriminant, negative discriminant, or both. A family F of elliptic curves is then said to be large if, for all but finitely many primes$p ,$the set$\operatorname { I n v } _ { p } ( F )$contains all pairs $( I , J ) \in \mathbb { Z } _ { p } \times \mathbb { Z } _ { p }$such that$p ^ { 2 } \dag \Delta ( I , J )$

In this section, we prove the following theorem.

Theorem 27. When elliptic curves E in any large family are ordered by height, the average size of the 3-Selmer group$S _ { 3 } ( E )$is 4.

3.1. Ternary cubic forms and elements in the 3-Selmer groups of elliptic curves. Recall that, for a field K, we may define a twisted action of the group $\operatorname { G L _ { 3 } } ( K )$on the space$V _ { K }$of ternary cubic forms having coeficients in K via

$$
\gamma \cdot f (x, y, z) := \det (\gamma) ^ {- 1} f ((x, y, z) \cdot \gamma),\tag{32}
$$

which induces an action of$\mathrm { P G L _ { 3 } } ( K )$on$V _ { K }$. We say that a ternary cubic form $f \in V _ { K }$is K-soluble if the equation$f ( x , y , z ) = 0$has a nontrivial solution over K. We then have the following result, which follows from [19, Th. 2.5 and Rem. 2.7] (see also [7, §4.2]).

Proposition 28. Let K be a field having characteristic not equal to 2 $o r \ 3 .$, and let$\begin{array} { r } { E : y ^ { 2 } = x ^ { 3 } - \frac { I } { 3 } x - \frac { J } { 2 7 } } \end{array}$be an elliptic curve over K. Then there exists a natural injection

$$
\mathcal {T} _ {E}: E (K) / 3 E (K) \to \{\text { PGL } _ {3} (K) \text {-orbits   of   ternary   cubic   forms   over   } K \},
$$

whose image consists exactly of the K-soluble ternary cubic forms having invariants equal to I and$J .$Under this correspondence, the identity element of$E ( K ) / 3 E ( K )$maps to the$\mathrm { P G L _ { 3 } } ( K )$-orbit of ternary cubic forms having a K-rational point of inflection.

Furthermore, the stabilizer in$\mathrm { P G L _ { 3 } } ( K )$of any ternary cubic form having invariants equal to I and J is isomorphic to$E ( K ) [ 3 ]$

A rational ternary cubic form$f \in V _ { \mathbb { Q } }$is said to be locally soluble if f is R-soluble and$\mathbb { Q } _ { p ^ { - \mathrm { { s o l u b l e } } } }$for all primes$p$. We then have the following proposition (see [19, Remark 2.8]).

Proposition 29. Let$E / \mathbb { Q }$be an elliptic curve. Then the elements in the 3-Selmer group of$E$are in bijective correspondence with$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$-orbits on the set of locally soluble ternary cubic forms in$V _ { \mathbb { Q } }$having invariants equal to $I ( E )$and$J ( E )$

Furthermore, the set of all ternary cubic forms in$V _ { \mathbb { Q } }$having invariants equal to$I ( E )$and$J ( E )$that are not strongly irreducible lie in a single$\mathrm { P G L _ { 3 } } ( \mathbb { Q } )$ orbit, and this orbit corresponds to the identity element in the 3-Selmer group of$E$.

By a result of Cremona, Fisher, and Stoll [13, Th. 1.1], any rational ternary cubic form$f \in V _ { \mathbb { Q } }$having integral invariants I and J is$\operatorname { S L } _ { 3 } ( \mathbb { Q } )$-equivalent to an integral ternary cubic form$g \in V _ { \mathbb { Z } }$having invariants I and J. In particular, it follows that such an$f$is$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$)-equivalent to either$g \mathrm { o r } - g$. Since$g$and $- g$have the same invariants, we obtain the following proposition.

Proposition 30. Let$E / \mathbb { Q }$be an elliptic curve. Then the elements in the 3-Selmer group of E are in bijective correspondence with$\mathrm { P G L _ { 3 } } ( \mathbb { Q } )$-equivalence classes<sup>1</sup> of locally soluble integral ternary cubic forms in$V _ { \mathbb { Z } }$having invariants equal to$I ( E )$and$J ( E )$

Furthermore, the set of all ternary cubic forms in$V _ { \mathbb { Z } }$having invariants equal to$I ( E )$and$J ( E )$that are not strongly irreducible lie in a single$\mathrm { P G L _ { 3 } } ( \mathbb { Q } )$ equivalence class, and this equivalence class corresponds to the identity element in the 3-Selmer group of$E$.

We may use Proposition 28 to prove Lemma 12, i.e., that the order of the stabilizer of a real ternary cubic form of nonzero discriminant is always equal to 3.

Proof of Lemma 12. Let$f \in V _ { \mathbb { R } }$be a ternary cubic form having nonzero discriminant. By Proposition 28, if f has invariants I and$J ,$then the size of the stabilizer of$f$in$\mathrm { P G L _ { 3 } } ( \mathbb { R } )$is equal to the number of real 3-torsion points on the elliptic curve$E ^ { I , J } / \mathbb { R }$having invariants I and$J .$Now the 3-torsion points of a plane Weierstrass elliptic curve are its flex points, and it is known that any plane cubic curve over R having nonzero discriminant has exactly three flex points defined over R (see, e.g., [21, Chap. 13]). Furthermore, if$\gamma \in \operatorname { G L } _ { 3 } ^ { + } ( \mathbb { R } )$ stabilizes$f ,$then$I ( \gamma \cdot f ) = ( \operatorname * { d e t } \gamma ) ^ { 4 } I ( f )$and$J ( \gamma \cdot f ) = ( \operatorname * { d e t } \gamma ) ^ { 6 } J ( f )$, and so det$\gamma = 1$. This completes the proof of Lemma 12.

3.2. A change-of-measure formula. We begin with the following proposition, which is an extension of the change-of-measure formula in Proposition 16 so that it holds also over$\mathbb { Z } _ { p } ,$, with$4 / 9$replaced by$| \mathcal { I } |$for some rational constant$\mathcal { I }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">g ∈Vz</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">PGL<sub>3</sub>(Q)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">g</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">PGL<sub>3</sub>(Q)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">V<sub>Z</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>We refer to the set of all g ∈ V<sub>Z</sub> such that g is -equivalent to a fixed integral ternary cubic form as the -equivalence class of f in .</span></small>

Proposition 31. Let K be R or$\mathbb { Z } _ { p }$for some prime$p , l e t \mid \cdot \mid$denote the usual absolute value on K, and let$s : K ^ { 2 } \to V _ { K }$be a continuous section. Then there exists a rational nonzero constant J, independent of K and$s ,$such that for any measurable function$\phi$on$V _ { K }$, we have

$$
\begin{array}{c} \int_ {\mathrm{PGL} _ {3} (K) \cdot s (K ^ {2})} \phi (f) d f = | \mathcal {J} | \int_ {(I, J) \in K ^ {2}} \int_ {g \in \mathrm{PGL} _ {3} (K)} \phi (g \cdot s (I, J)) \omega (g) d I d J \\ a n d \\ \int_ {V _ {K}} \phi (f) d f = | \mathcal {J} | \int_ \underset {\Delta (I, J) \neq 0 \}} ^ {(I, J) \in K ^ {2}} \Big (\sum_ {f \in \frac {V _ {K} (I , J)}{\mathrm{PGL} _ {3} (K)}} \frac {1}{\# \mathrm{Stab} (f)} \int_ {g \in \mathrm{PGL} _ {3} (K)} \phi (g \cdot f) \omega (g) \Big) d I d J, \end{array}
$$

where$\operatorname { S t a b } ( f )$denotes the stabilizer of f in$\mathrm { P G L _ { 3 } } ( K )$and$\frac { V _ { K } ( I , J ) } { \mathrm { P G L } _ { 3 } ( K ) }$denotes a set of representatives for the action of$\mathrm { P G L _ { 3 } } ( K )$on the set of elements in$V _ { K }$ having invariants I and J.

Proposition 31 follows immediately from the proofs of [8, Props. 3.11 and 3.12] (see [8, Rem. 3.14]).

In the rest of the section, we compute the value of$\mathcal { I }$. To do so, we use the following proposition, which follows from Proposition 31; the proof is identical to that of [8, Prop. 3.13].

Proposition 32. Let p be a fixed prime number. Let$S ~ \subset ~ V _ { \mathbb { Z } _ { p } }$be a set defined by congruence conditions modulo$p ,$and let$\bar { S } \subset V _ { \mathbb { F } _ { p } }$denote the reduction of S modulo$p .$Assume that$S = \pi ^ { - 1 } ( \pi ( S ) )$, where π is given by taking invariants. Then

$$
|\mathcal{J}|_{p} = \frac{\#PGL_{3}(\mathbb{F}_{p})\cdot\Big(\sum_{f\in PGL_{3}(\mathbb{F}_{p})\setminus\bar{S}}\frac{1}{\#Aut_{\mathbb{F}_{p}}(f)}\Big)}{p^{\dim V}\cdot\operatorname{Vol}(PGL_{3}(\mathbb{Z}_{p}))\cdot\Big(\int_{(I,J)\in\pi(S)}\sum_{\substack{V_{\mathbb{Z}_{p}}(I,J)\\ f\in \frac{PGL_{3}(\mathbb{Z}_{p})}{}}} \frac{1}{\#Aut_{\mathbb{Z}_{p}}(f)}dIdJ\Big)}.\tag{33}
$$

Note that the numerator in the right-hand side of (33) is equal to$\# \bar { S }$by the orbit-stabilizer formula.

The next two lemmas allow us to evaluate the numerator and the denominator of (33) for the set$S \subset V _ { \mathbb { Z } _ { p } }$consisting of elements whose discriminants are prime to p.

Lemma 33. Let p be a fixed prime. Then the number of elements in$V _ { \mathbb { F } _ { p } }$ that have nonzero discriminant is equal to$( p ^ { 2 } - p ) \cdot \# \mathrm { P G L } _ { 3 } ( \mathbb { F } _ { p } )$

Proof. Ternary cubic forms over$\mathbb { F } _ { p }$having nonzero discriminant correspond to isomorphism classes of triples$( C , L , B )$, where$C$is a genus 1 curve over$\mathbb { F } _ { p } , ~ L$is a degree 3 line bundle on$C ,$and B is a basis for the space of sections of$L ;$here, two such pairs$( C , L , B )$and$( C ^ { \prime } , L ^ { \prime } , B ^ { \prime } )$are called isomorphic if there exists an isomorphism$\phi : C \to C ^ { \prime }$such that${ \cal L } = \phi ^ { * } ( L ^ { \prime } )$and $B = \phi ^ { * } ( B ^ { \prime } )$. The number of such isomorphism classes of pairs$( C , L )$over$\mathbb { F } _ { p }$ is exactly$p ,$since there is exactly one pair for each j-invariant. Once the pair $( C , L )$is fixed, there are$\# \mathrm { G L } _ { 3 } ( \mathbb { F } _ { p } )$diferent possible bases for the space of sections. Since$\# \mathrm { G L } _ { 3 } ( \mathbb { F } _ { p } ) = ( p - 1 ) \# \mathrm { P G L } _ { 3 } ( \mathbb { F } _ { p } )$, we obtain the lemma.

Lemma 34. Let p be a fixed prime and let$( I , J ) \in \mathsf { \Omega } _ { 1 6 } ^ { 1 } \mathbb { Z } _ { p } \times \mathsf { \Omega } _ { 3 2 } ^ { 1 } \mathbb { Z } _ { p }$be an element in the image of$\pi$such that$p ^ { 2 } \dag \Delta ( I , J )$. Then

$$
\sum_ {f \in \frac {V _ {\mathbb {Z} _ {p}} (I , J)}{\mathrm{PGL} _ {3} (\mathbb {Z} _ {p})}} \frac {1}{\# \mathrm{Aut} _ {\mathbb {Z} _ {p}} (f)} = \left\{ \begin{array}{l l} 1 & \text {for p\neq 3;} \\ 3 & \text {for p = 3.} \end{array} \right.
$$

Proof. Since$p ^ { 2 } \nmid \Delta ( I , J )$, we have$\operatorname { A u t } _ { \mathbb { Z } _ { p } } ( f ) = \operatorname { A u t } _ { \mathbb { Q } _ { p } } ( f ) = E ^ { I , J } [ 3 ] ( \mathbb { Q } _ { p } )$ for$f \in V _ { \mathbb { Z } _ { p } } ( I , J )$. Furthermore, we have

$$
\# \frac {V _ {\mathbb {Z} _ {p}} (I , J)}{\mathrm{PGL} _ {3} (\mathbb {Z} _ {p})} = \# (E (\mathbb {Q} _ {p}) / 3 E (\mathbb {Q} _ {p})).
$$

The lemma therefore follows from Lemma 40 in Section 3.4.

We may now compute the value of$| { \mathcal { I } } | _ { p }$using Proposition 32. For each prime p, we pick S to be the set of elements$f \in V _ { \mathbb { Z } _ { p } }$such that$p \ \nmid \Delta ( f )$ Since$\mathrm { V o l } ( \mathrm { P G L _ { 3 } } ( \mathbb { Z } _ { p } ) ) = \# \mathrm { P G L } _ { 3 } ( \mathbb { F } _ { p } ) / p ^ { 8 }$, equation (33), in conjunction with Lemmas 33 and 34, implies that

$$
| \mathcal {J} | _ {p} = | 3 | _ {p} \frac {p - 1}{p \mathrm{Vol} (\pi (S))}.
$$

We may now use Theorem 9 to compute the volume of$\pi ( S )$, yielding

$$
\operatorname{Vol} (\pi (S)) = \left\{ \begin{array}{l l} \frac {p - 1}{p} & \text { if } p \geq 5; \\ \frac {2}{8 1} & \text { if } p = 3; \\ 2 & \text { if } p = 2. \end{array} \right.
$$

We conclude that$\mathcal { I } = 4 / 9$, as desired.

3.3. Computations of p-adic densities in terms of local masses. Proposition 30 asserts that the nonidentity elements in the 3-Selmer group of$E ^ { I , J }$ are in bijection with$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$-orbits on the set of strongly irreducible locally soluble integral ternary cubic forms having invariants I and J. In Section 2, we computed the asymptotic number of$\operatorname { S L _ { 3 } } ( \mathbb { Z } )$-equivalence classes of strongly irreducible integral ternary cubic forms having bounded height. In order to use this to compute the number of$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$-equivalence classes of strongly irreducible locally soluble integral ternary cubic forms having bounded height, we must count each locally soluble orbit$\mathrm { P G L _ { 3 } } ( \mathbb { Z } ) \cdot f$weighted by$1 / n ( f )$• where$n ( f )$is the number of$\mathrm { P G L _ { 3 } ( Z ) }$-orbits in the$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$-equivalence class of$f$in$V _ { \mathbb { Z } }$. Since we have shown that all but a negligible number of integral ternary cubic forms have trivial stabilizer in$\mathrm { P G L _ { 3 } } ( \mathbb { Q } )$, we may instead count each locally soluble orbit$\mathrm { P G L _ { 3 } ( Z ) }$· f weighted by$1 / m ( f )$, where

$$
m (f) := \sum_ {f ^ {\prime} \in B (f)} \frac {\# \operatorname{Aut} _ {\mathbb {Q}} \left(f ^ {\prime}\right)}{\# \operatorname{Aut} _ {\mathbb {Z}} \left(f ^ {\prime}\right)} = \sum_ {f ^ {\prime} \in B (f)} \frac {\# \operatorname{Aut} _ {\mathbb {Q}} (f)}{\# \operatorname{Aut} _ {\mathbb {Z}} \left(f ^ {\prime}\right)};
$$

here$B ( f )$is a set of representatives for the action of$\mathrm { P G L _ { 3 } ( Z ) }$on the$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$ equivalence class of$f$in$V _ { \mathbb { Z } } .$, while$\operatorname { A u t } _ { \mathbb { Q } } ( f )$and$\operatorname { A u t z } ( f )$are the stabilizers of f in$\mathrm { P G L _ { 3 } } ( \mathbb { Q } )$and$\mathrm { P G L _ { 3 } ( Z ) }$, respectively.

For a prime p and an ternary cubic form$f \in V _ { \mathbb { Z } _ { p } }$, define$m _ { p } ( f )$by

$$
m _ {p} (f) := \sum_ {f ^ {\prime} \in B _ {p} (f)} \frac {\# \operatorname{Aut} _ {\mathbb {Q} _ {p}} \left(f ^ {\prime}\right)}{\# \operatorname{Aut} _ {\mathbb {Z} _ {p}} \left(f ^ {\prime}\right)} = \sum_ {f ^ {\prime} \in B (f)} \frac {\# \operatorname{Aut} _ {\mathbb {Q} _ {p}} (f)}{\# \operatorname{Aut} _ {\mathbb {Z} _ {p}} \left(f ^ {\prime}\right)},
$$

where$B _ { p } ( f )$denotes a set of representatives for the action of$\mathrm { P G L _ { 3 } } ( \mathbb { Z } _ { p } )$on the$\mathrm { P G L _ { 3 } } ( \mathbb { Q } _ { p } )$-equivalence class of$f$in$V _ { \mathbb { Z } _ { p } }$, while$\operatorname { A u t } _ { \mathbb { Q } _ { p } } ( f )$(resp.$\operatorname { A u t } _ { \mathbb { Z } _ { p } } ( f ) )$ denotes the stabilizers of$f$in$\mathrm { P G L _ { 3 } } ( \mathbb { Q } _ { p } )$(resp.$\operatorname { P G L _ { 3 } } ( \mathbb { Z } _ { p } ) )$). Then we have the following proposition, which explains the advantage of using the weights$m ( f )$ rather than$n ( f )$, and whose proof is identical to that of [8, Prop. 3.6].

Proposition 35. Suppose$f \in V _ { \mathbb { Z } }$has nonzero discriminant. Then

$$
m (f) = \prod_ {p} m _ {p} (f).
$$

Suppose now that F is a large family of elliptic curves. Recall that we denoted the set$\{ ( I ( E ) , J ( E ) : E \in F \}$by Inv(F) and the p-adic closure of Inv$( F )$in$\mathbb { Z } _ { p } ^ { 2 }$by$\operatorname { I n v } _ { p } ( F )$. Let$S ( F )$denote the set of all locally soluble integral ternary cubic forms having invariants I and J such that$( I , J ) \in \operatorname { I n v } ( F )$, and let $S _ { p } ( F )$denote the p-adic closure of$S ( F )$in$V _ { \mathbb { Z } _ { p } }$. We now determine the p-adic density of$S _ { p } ( F )$, where each element$f \in S _ { p } ( F )$is weighted by$1 / m _ { p } ( f )$, in terms of a local$( p { - } a d i c )$mass$M _ { p } ( V , F )$involving all isomorphism classes of soluble 3-coverings of elliptic curves over$\mathbb { Q } _ { p }$

Proposition 36. We have

$$
\int_ {S _ {p} (F)} \frac {1}{m _ {p} (f)} d f = | 4 / 9 | _ {p} \mathrm{Vol} (\mathrm{PGL} _ {3} (\mathbb {Z} _ {p})) M _ {p} (V, F),
$$

where

$$
M _ {p} (V, F) = \int_ {(I, J) \in \mathrm{Inv} _ {p} (F)} \frac {\# (E ^ {I , J} (\mathbb {Q} _ {p}) / 3 E ^ {I , J} (\mathbb {Q} _ {p}))}{\# E ^ {I , J} (\mathbb {Q} _ {p}) [ 3 ]} d I d J.\tag{34}
$$

The proof of Proposition 36 is identical to that of [8, Prop. 3.9].

3.4. The average size of the 3-Selmer groups of elliptic curves in a large family (Proof of Theorem 27). In analogy with$M _ { p } ( V , F )$, we define the local mass$M _ { p } ( F )$by

$$
M _ {p} (F) = \int_ {(I, J) \in \operatorname{Inv} _ {p} (F)} d I d J.\tag{35}
$$

We also define the following analogues at infinity of$M _ { p } ( F )$and$M _ { p } ( V , F )$ respectively:

$$
\begin{array}{c}M_{\infty}(F;X):= \int_{\substack{(I,J)\in \operatorname{Inv}_{\infty}(F)\\ H(I,J) <   X}}dIdJ,\\ M_{\infty}(V,F;X):= \int_{\substack{(I,J)\in \operatorname{Inv}_{\infty}(F)\\ H(I,J) <   X}}\frac{\#(E^{I,J}(\mathbb{R}) / 3E^{I,J}(\mathbb{R}))}{\#E^{I,J}(\mathbb{R})[3]} dIdJ. \end{array}\tag{36}
$$

We then have the following result counting the number of elliptic curves in a large family, which is [8, Th. 3.17].

Theorem 37. Let F be a large family of elliptic curves, and let$N ( F ; X )$ denote the number of elliptic curves in F that have height bounded by X. Then

$$
N (F; X) = M _ {\infty} (F; X) \prod_ {p} M _ {p} (F) + o (X ^ {5 / 6}).\tag{37}
$$

We say that an element$f \in V _ { \mathbb { Z } }$is bad at$p$if either$f$is not$\mathbb { Q } _ { p }$-soluble or $m _ { p } ( f ) \neq 1$. To deduce Theorem 27 using Theorem 24, we need the following result.

Proposition 38. Let f be an integral ternary cubic form such that either f is insoluble at p or$m _ { p } ( f ) \neq 1$. Then$p ^ { 2 } \mid \Delta ( f )$

Proof. Suppose that$f$is an integral ternary cubic form such that the curve defined by$f ( x , y , z ) = 0$has no$\mathbb { Q } _ { p } { \mathrm { - p o i n t s } }$. We claim that$f$is geometrically reducible over$\mathbb { F } _ { p } \ ( \mathrm { i . e . , } \ f$(mod$p )$factors into a product of lower degree forms defined over$\overline { { \mathbb { F } } } _ { p } )$. This is because if$f$were geometrically irreducible over$\mathbb { F } _ { p } ,$ then the Lang–Weil estimates [23] would imply that the curve$f ( x , y , z ) = 0$ has a smooth point in$\mathbb { P } ^ { 2 } ( \mathbb { F } _ { p } )$. By Hensel’s lemma, this smooth point lifts to a point in$\mathbb { P } ^ { 2 } ( \mathbb { Q } _ { p } )$. Therefore, f is geometrically reducible over$\mathbb { F } _ { p }$, implying that$p ^ { 2 } \mid \Delta ( f )$

If$f \in V _ { \mathbb { Z } }$satisfies$m _ { p } ( f ) \neq 1$, then there exists an element$\gamma \in \operatorname { P G L } _ { 3 } ( \mathbb { Q } _ { p } )$ such that$\gamma \cdot f \in V _ { \mathbb { Z } _ { p } }$. By an appropriate change-of-basis in$\mathrm { P G L _ { 3 } } ( \mathbb { Z } _ { p } )$, we may assume that$\gamma$is of the form$\gamma = \binom { p ^ { - a } } { 1 } _ { p ^ { b } } \biggr )$, where a and b are nonnegative Åand at least one of a and b is nonzero. If$b > a$, then clearly$z$is a factor of the reduction of$f$modulo$p .$Now assume that$a \geq b ,$so that$a > 0$. In this case, consider the form$f _ { 1 } \stackrel { \textstyle - } { = } \left( { { \begin{array} { c c } { { p ^ { - 1 } } } & { { } } \\ { { 1 } } & { { 1 } } \end{array} } } \right) \cdot p f$, which is an element of$V _ { \mathbb { Z } _ { p } }$having the same invariants as$f .$. The reduction of$f _ { 1 }$modulo$p ,$being a multiple of$x _ { i }$ is a reducible ternary cubic form. We conclude that$p ^ { 2 } \mid \Delta ( f _ { 1 } ) = \Delta ( f )$

Theorem 27 will be deduced from the following result.

Theorem 39. Let F be a large family of elliptic curves. Then

$$
\begin{array}{l}\sum_{\substack{E\in F\\ H^{\prime}(E) <   X}}(\# S_{3}(E) - 1)\\ \lim_{X\to \infty}\frac{\sum_{\substack{E\in F\\ H^{\prime}(E) <   X}}1}{\sum_{\substack{E\in F\\ H^{\prime}(E) <   X}}}\\ = \operatorname{Vol}(\operatorname{PGL}_{3}(\mathbb{Z})\backslash \operatorname{PGL}_{3}(\mathbb{R}))\frac{M_{\infty}(V,F;X)}{M_{\infty}(F;X)}\prod_{p}\Bigl [\operatorname{Vol}(\operatorname{PGL}_{3}(\mathbb{Z}_{p}))\frac{M_{p}(V,F)}{M_{p}(U_{1},F)}\Bigr ]. \end{array}\tag{38}
$$

Proof. The numerator of the right-hand side of (38) is equal to the number of$\mathrm { P G L _ { 3 } ( Z ) }$-orbits on$S ( F )$having height bounded by$X$, where each orbit $\mathrm { P G L _ { 3 } } ( \mathbb { Z } ) \cdot f$is counted with weight$1 / m ( f )$. Therefore, by Theorem 24 and Propositions 35 and 38, we obtain

$$
\begin{array}{l}\sum_{\substack{E\in F\\ H^{\prime}(E) <   X}}(\# S_{3}(E) - 1) = N(V_{\mathbb{Z}}\cap S_{\infty}(F);X)\prod_{p}\int_{S_{p}(F)}\frac{1}{m_{p}(f)} df + o(X^{5 / 6})\\ \\ \qquad = \frac{4}{9}\mathrm{Vol}(\mathrm{PGL}_{3}(\mathbb{Z})\backslash \mathrm{PGL}_{3}(\mathbb{R}))M_{\infty}(V,F;X)\\ \\ \qquad \times \prod_{p}\bigl [\Big|\frac{4}{9}\Bigr |_{p}\mathrm{Vol}(\mathrm{PGL}_{3}(\mathbb{Z}_{p}))M_{p}(V,F)\bigr ] + o(X^{5 / 6})\\ \\ \qquad = \mathrm{Vol}(\mathrm{PGL}_{3}(\mathbb{Z})\backslash \mathrm{PGL}_{3}(\mathbb{R}))M_{\infty}(V,F;X)\\ \\ \qquad \times \prod_{p}\bigl [\mathrm{Vol}(\mathrm{PGL}_{3}(\mathbb{Z}_{p}))M_{p}(V,F)\bigr ] + o(X^{5 / 6}), \end{array}\tag{39}
$$

where the second equality follows from Proposition 36. Taking the ratio of (39) and (37), we obtain the theorem.

To evaluate the right-hand side of (38) we need the following fact, whose proof is identical to that of [11, Lemma 3.1].

Lemma 40. Let E be an elliptic curve over$\mathbb { Q } _ { p }$. We have

$$
\# (E (\mathbb {Q} _ {p}) / 3 E (\mathbb {Q} _ {p})) = \left\{ \begin{array}{l l} \# E [ 3 ] (\mathbb {Q} _ {p}) & \text { if } p \neq 3; \\ 3 \cdot \# E [ 3 ] (\mathbb {Q} _ {p}) & \text { if } p = 3. \end{array} \right.
$$

Proof. A well-known result of Lutz (see, e.g., [27, Chap. 7, Prop. 6.3] for a proof) asserts that there exists a subgroup$M \subset E ( \mathbb { Q } _ { p } )$of finite index that is isomorphic to$\mathbb { Z } _ { p } .$. Let G denote the finite group$E ( \mathbb { Q } _ { p } ) / M$. Then by applying the snake lemma to the following diagram,

![](images/page_28_image_1.jpg)

we obtain the exact sequence

$$
0 \to M [ 3 ] \to E (\mathbb {Q} _ {p}) [ 3 ] \to G [ 3 ] \to M / 3 M \to E (\mathbb {Q} _ {p}) / 3 E (\mathbb {Q} _ {p}) \to G / 3 G \to 0.
$$

Since G is a finite group and M is isomorphic to$\mathbb { Z } _ { p }$, Lemma 40 follows. 

By Lemma 40 and the definitions of$M _ { p } ( V , F )$and$M _ { p } ( U _ { 1 } , F )$, we have (40)

$$
\frac {M _ {p} (V , F)}{M _ {p} (F)} = \frac {\int_ {(I , J) \in \mathrm{Inv} _ {p} (F)} \frac {\# (E ^ {I , J} (\mathbb {Q} _ {p}) / 3 E ^ {I , J} (\mathbb {Q} _ {p}))}{\# E ^ {I , J} (\mathbb {Q} _ {p}) [ 3 ]} d I d J}{\int_ {(I , J) \in \mathrm{Inv} _ {p} (F)} d I d J} = \left\{ \begin{array}{l l} 1 & \text {if p\neq 3 ;} \\ 3 & \text {if p = 3 .} \end{array} \right.
$$

Furthermore, we know that$M _ { \infty } ( V , F ; X ) / M _ { \infty } ( F ; X ) = 1 / 3$. Therefore, Theorem 39 yields

$$
\lim_{X\to \infty}\frac{\sum\limits_{\substack{E\in F\\ H^{\prime}(E) <   X}}(\# S_{3}(E) - 1)}{\sum\limits_{\substack{E\in F\\ H^{\prime}(E) <   X}}1} = \operatorname{Vol}(\operatorname{PGL}_{3}(\mathbb{Z})\backslash \operatorname{PGL}_{3}(\mathbb{R}))\prod_{p}\operatorname{Vol}(\operatorname{PGL}_{3}(\mathbb{Z}_{p})),
$$

which is then equal to$3 \zeta ( 2 ) \zeta ( 3 ) \prod _ { p } \bigl ( ( 1 - p ^ { - 2 } ) ( 1 - p ^ { - 3 } ) \bigr ) = 3$, the Tamagawa number of$\mathrm { P G L _ { 3 } ( \mathbb { Q } ) }$. We have proven Theorem 27.

## 4. A positive proportion of elliptic curves have rank 0

We have shown in the previous section that the average rank of all elliptic curves, when ordered by height, is less than$1 \textstyle { \frac { 1 } { 6 } }$. This immediately implies that a large proportion (indeed, at least 62.5%) of all elliptic curves must have rank 0 or 1.

In order to deduce analogous positive proportion statements for the individual ranks 0 and 1, we may attempt to make use of information regarding the distribution of the parity of the ranks—or of the 3-Selmer ranks—of these curves. Indeed, if we knew that even and odd 3-Selmer ranks occur equally often in a large family of elliptic curves, then this would imply by Theorem 27 that a positive proportion of curves in that family have rank 0, and (assuming finiteness of the Tate–Shafarevich group) a positive proportion have rank 1.

In Section 4.1, we use a recent result of Dokchitser–Dokchitser [17] (see also Nekov´aˇr [25]) to construct a large, positive proportion family F of elliptic curves in which the parities of the 3-Selmer ranks of the curves in F are equally distributed between even and odd, thus unconditionally yielding a positive proportion of elliptic curves having rank 0.

We may also combine our counting techniques with the recent work of Skinner–Urban [28] in order to deduce that a positive proportion of all elliptic curves, when ordered by height, have analytic rank 0; i.e., a positive proportion of all elliptic curves have nonvanishing L-function$L ( E , s )$at$s = 1$. Since these analytic rank 0 curves form a subset of the rank 0 curves of Section 4.1, it follows that a positive proportion of all elliptic curves satisfy the Birch and Swinnerton-Dyer conjecture. This is discussed in Section 4.2.

4.1. Elliptic curves having algebraic rank 0. Recall that the conjecture of Birch and Swinnerton-Dyer implies, in particular, that the evenness or oddness of the rank of an elliptic curve E is determined by whether its root number— that is, the sign of the functional equation of the L-function$L ( E , s )$of E—is +1 or −1, respectively. It is widely believed that the root numbers +1 and −1 occur equally often among all elliptic curves when ordered by height. Indeed, we expect the same to be true in any large family as well.

In this subsection, we prove

Theorem 41. Suppose F is a large family of elliptic curves such that exactly 50% of the curves in F, when ordered by height, have root number +1. Then at least 25% of the curves in F, when ordered by height, have rank 0. Furthermore, if we assume that all the elliptic curves in F have finite Tate– Shafarevich groups, then at least$5 / 1 2 > 4 1 . 6 \%$of the curves in F have rank 1.

We will construct an explicit positive proportion family F satisfying the hypotheses of Theorem 41; this will then imply Theorem 4. (Of course, it is expected that the family F of all curves satisfies the root number hypothesis of the theorem; however, this remains unproved.)

Our proof of Theorem 41 is based on Theorem 27 in conjunction with a recent remarkable result of Dokchitser and Dokchitser [17], which asserts (as predicted by the Birch and Swinnerton-Dyer conjecture) that the parity of the p-Selmer rank of an elliptic curve E (for any prime p) is determined by the root number of E.

Theorem 42 (Dokchitser–Dokchitser). Let E be an elliptic curve over$\mathbb { Q }$ and let p be any prime. Let$s _ { p } ( E )$and$t _ { p } ( E )$denote the rank of the p-Selmer group of E and the rank of$E ( \mathbb { Q } ) [ p ]$, respectively. Then the quantity$r _ { p } ( E ) : =$ $s _ { p } ( E ) - t _ { p } ( E )$is even if and only if the root number of E$i s + 1$

We now prove Theorem 41.

Proof of Theorem 41. First note that Lemma 19 implies that the number of elliptic curves over$\mathbb { Q }$that have a nontrivial rational 3-torsion point is negligible. Thus for a density of 100% of elliptic curves E, we have$r _ { p } ( E ) = s _ { p } ( E )$

Now, by Theorem 27, the average size of the 3-Selmer group of curves in F is at most 4. On the other hand, by Theorem 42 we know that that exactly 50% of the curves in F have odd 3-Selmer rank and thus have at least three elements in the 3-Selmer group. Hence the average size of the 3-Selmer groups among the 50% of elliptic curves in F having even 3-Selmer rank is at most 5. Now if the 3-Selmer group of an elliptic curve has even rank, then it must have size 1, 9, or more than 9. For the average of such sizes to be 5, at least half must be equal to 1. Thus among these 50% of curves in F having even 3-Selmer rank, at least half have trivial 3-Selmer group and therefore have rank 0.

Next, suppose that every odd rank curve in F has a finite Tate–Shafarevich group. A well-known result of Cassels states that if$E / \mathbb { Q }$is an elliptic curve such that$\operatorname { I I I } ( E )$is finite, then$| \mathrm { I I I } ( E ) |$is a square. Now if the 3-Selmer group of an elliptic curve has odd rank, then it must have size 3, 27, or more than 27. For the average of such sizes to be at most$^ { 7 , }$at least$5 / 6$of them must equal 3. Thus among these 50% of curves in F with odd 3-Selmer rank, at least$5 / 6$of them have 3-Selmer group of size 3. Since X is always a square, we conclude that X[3] for all these elliptic curves is trivial and so they each have rank 1. 

We now construct an explicit positive proportion large family F of elliptic curves for which exactly 50% of the curves have root number equal to 1. By Theorem 41, this will then imply Theorems 4 and 5.

First, recall that the root number$\omega ( E )$of an elliptic curve$E$over$\mathbb { Q }$may be expressed in terms of a product over all primes of local root numbers$\omega _ { p } ( E )$ of$E _ { \mathrm { { i } } }$, namely,$\begin{array} { r } { \omega ( E ) = - \prod _ { p } \omega _ { p } ( E ) } \end{array}$. The local root number$\omega _ { p } ( E )$is easy to compute when$E$has good or multiplicative reduction at$p .$In fact, it is known $( \mathrm { s e e } , \mathrm { e . g . } , [ 2 6 ] )$that$\omega _ { p } ( E ) = 1$whenever E has good or nonsplit multiplicative reduction at$p ,$, and$\omega _ { p } ( E ) = - 1$when E has split multiplicative reduction at$p .$

Suppose an elliptic curve$E / \mathbb { Q }$has multiplicative reduction at a prime $p \geq 3$. Then it is easily checked that E has split reduction precisely when $\begin{array} { r } { \left( { \frac { - 2 J } { p } } \right) = 1 } \end{array}$. It is also clear that if$E _ { - 1 }$denotes the twist of E over$\mathbb { Q } [ i ]$, then $\overset { \cdot } { J } ( \overset { \cdot } { E } _ { - 1 } ) = - \overset { \cdot } { J } ( E )$. Hence, given an odd prime p for which E has multiplicative reduction at p, we have$\omega _ { p } ( E ) = \omega _ { p } ( E _ { - 1 } )$if and only if$p \equiv 1$(mod 4).

Let F denote the set of all elliptic curves E over$\mathbb { Q }$satisfying the following conditions:

• The curve E and its twist$E _ { - 1 }$both have additive reduction at 2, and furthermore the j-invariant of both curves E and$E _ { - 1 }$are 2-adic units.

•$E$has square-free discriminant away from 2.

$\Delta ^ { \prime } ( E ) \equiv 1 { \pmod { 4 } }$, where${ \Delta } ^ { \prime } ( E ) : = | \Delta ( E ) / 2 ^ { v _ { 2 } ( \Delta ( E ) ) } |$is the positive odd part of the discriminant of$E$.

The set F is a large family. Moreover, if$E \in F$, then the twist$E _ { - 1 }$of E by −1 is also clearly in$F ,$since the odd part of the discriminant of an elliptic curve is preserved under such a twist. Since$\Delta ^ { \prime } ( E )$is squarefree, the third condition implies that the number of distinct primes congruent to 3 (mod 4) that divide the discriminant of E is even. Now for a prime factor$p$of the discriminant, we have already observed that$\omega _ { p } ( E ) = - \omega _ { p } ( E _ { - 1 } )$if and only if$p \equiv 3$(mod 4). Furthermore, the first condition implies that$\omega _ { 2 } ( E ) ~ = ~ - \omega _ { 2 } ( E _ { - 1 } )$(see [29, Lemma 12]); therefore,$\omega ( E ) = - \omega ( E _ { - 1 } )$for all$E \in F$. Since the height of an elliptic curve also remains the same under twisting by −1, it follows that a density of exactly 50% of elliptic curves in$F _ { ; }$, when ordered by height, have root number +1, as desired.

We have proven Theorems 4 and 5.

4.2. Elliptic curves having analytic rank 0. We may similarly prove that a positive proportion of all elliptic curves have analytic rank 0, by combining our counting arguments with the recent beautiful work of Skinner–Urban [28]. Their work implies, in particular, that if$E / \mathbb { Q }$is an elliptic curve satisfying certain mild conditions and having trivial 3-Selmer group (and therefore rank 0), then the L-function of E does not vanish at the point 1! The following theorem is a consequence of [28, Th. 2].

Theorem 43 (Skinner–Urban). Let$E / \mathbb { Q }$be an elliptic curve such that (a) the 3-Selmer group of E is trivial;

(b) E has good ordinary reduction at 3;

(c) the action of G<sub>Q</sub> on$E [ 3 ]$is irreducible;

(d) there exists a prime$p \neq 3$such that$p \| \mathrm { C o n d } ( E )$and${ \bar { \rho } } ( E , 3 )$is ramified at$p ,$

where$\bar { \rho } ( E , 3 ) : \mathrm { G a l } ( \bar { \mathbb { Q } } / \mathbb { Q } ) \to \mathrm { G L } _ { 2 } ( \mathbb { F } _ { 3 } )$denotes the usual Galois representation obtained from the action of$\operatorname { G a l } ( { \bar { \mathbb { Q } } } / \mathbb { Q } )$on the 3-torsion points of$E$. Then $L ( E , 1 ) \neq 0$

We may use Theorem 41 in conjunction with Skinner and Urban’s Theorem to prove

Theorem 44. Suppose F is a large family of elliptic curves having good ordinary reduction at 3 such that$5 \| \operatorname { D i s c } ( E )$for every curve$E \in F$. Further assume that exactly 50% of the curves in F, when ordered by height, have root number +1. Then at least 25% of elliptic curves in F have analytic rank 0.

Proof. It is easy to see$( \mathrm { e . g . }$, by Hilbert irreducibility) that a density of 100% of elliptic curves$E _ { \mathrm { { i } } }$, when ordered by height, have the property that the action of$G _ { \mathbb { Q } }$on$E [ 3 ]$is irreducible. (In fact, it has been shown by Duke [18, Th. 1] that 100% of all elliptic curves$E _ { i }$, when ordered by height, have the property that the action of$G _ { \mathbb { Q } }$on$E [ p ]$is irreducible for all primes$p . )$As F is a large family, it contains a positive proportion of all elliptic curves, and so 100% of the curves in F satisfy condition (c) of Theorem 43. As$5 \| \operatorname { D i s c } ( E )$ for$E \in F$, we see that E has multiplicative reduction at 5, which implies that$5 \| \operatorname { C o n d } ( E )$. Furthermore, since$3 \mathbin { \left\{ \ v _ { 5 } ( \mathrm { C o n d } ( E ) ) \right. }$, [14, Prop. 2.12] implies that condition (d) of Theorem 43 is satisfied by E. The proof of Theorem 41 now implies that at least 25% of the curves in F satisfy all four conditions of Theorem 43, and so Theorem 44 follows.

As in Section 4.1, we may construct an explicit union F of positive proportion large families of elliptic curves satisfying the hypotheses of Theorem 44. Indeed, let F denote the family of all elliptic curves E satisfying the following conditions:

• The curve E and its twist$E _ { - 1 }$both have additive reduction at$^ { 2 , }$and furthermore the j-invariant of both curves E and$E _ { - 1 }$are 2-adic units.

• E has square-free discriminant away from 2, and$5 \| \operatorname { D i s c } ( E )$

• E has good ordinary reduction at 3.

$\Delta ^ { \prime } ( E ) \equiv 1$(mod 4), where${ \Delta } ^ { \prime } ( E ) : = | \Delta ( E ) / 2 ^ { v _ { 2 } ( \Delta ( E ) ) } |$is the positive odd part of the discriminant of E.

Then, just as in Section 4.1, we see that 50% of the curves in F have root number +1. Thus, by Theorem 44, a positive proportion of these and thus all elliptic curves, when ordered by height, have both algebraic and analytic rank 0; we have proven Theorem 6 and Corollary 7.

Acknowledgments. We are very grateful to John Cremona, Johan de Jong, Tom Fisher, Wei Ho, Bjorn Poonen, Shrenik Shah, Christopher Skinner, Michael Stoll, Damiano Testa, Eric Urban, and Jerry Wang for helpful conversations. The first author was partially supported by NSF Grant DMS-1001828.

## References

[1] S. Y. An, S. Y. Kim, D. C. Marshall, S. H. Marshall, W. G. McCallum, and A. R. Perlis, Jacobians of genus one curves, J. Number Theory 90 (2001), 304–315. MR 1858080. Zbl 1066.14035. http://dx.doi.org/10.1006/jnth.2000.2632.

[2] S. Aronhold, Theorie der homogenen Funktionen dritten Grades von drei Ver¨anderlichen, J. reine Angew. Math. 55 (1858), 97–191. Zbl 055.1455cj.

[3] M. Artin, F. Rodriguez-Villegas, and J. Tate, On the Jacobians of plane cubics, Adv. Math. 198 (2005), 366–382. MR 2183258. Zbl 1092.14054. http://dx.doi.org/10.1016/j.aim.2005.06.004.

[4] B. Bektemirov, B. Mazur, W. Stein, and M. Watkins, Average ranks of elliptic curves: tension between data and conjecture, Bull. Amer. Math. Soc.

44 (2007), 233–254. MR 2291676. Zbl 1190.11032. http://dx.doi.org/10.1090/S0273-0979-07-01138-X.

[5] M. Bhargava, The density of discriminants of quintic rings and fields, Ann. of Math. 172 (2010), 1559–1591. MR 2745272. Zbl 1220.11139. http://dx.doi.org/10.4007/annals.2010.172.1559.

[6] M. Bhargava, The Ekedahl sieve and the density of squarefree values of invariant polynomials. arXiv 1402.0031.

[7] M. Bhargava and W. Ho, Coregular spaces and genus one curves. arXiv 1306. 4424v1.

[8] M. Bhargava and A. Shankar, Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves, Ann. of Math. 181 (2015), 191–242. http://dx.doi.org/10.4007/annals.2015.181.1.3.

[9] B. J. Birch and H. P. F. Swinnerton-Dyer, Notes on elliptic curves. I, J. Reine Angew. Math. 212 (1963), 7–25. MR 0146143. Zbl 0118.27601. http://dx.doi.org/10.1515/crll.1963.212.7.

[10] A. Borel and Harish-Chandra, Arithmetic subgroups of algebraic groups, Ann. of Math. 75 (1962), 485–535. MR 0147566. Zbl 0107.14804. http://dx.doi.org/10.2307/1970210.

[11] A. Brumer and K. Kramer, The rank of elliptic curves, Duke Math. J. 44 (1977), 715–743. MR 0457453. Zbl 0376.14011. http://dx.doi.org/10.1215/S0012-7094-77-04431-3.

[12] J. W. S. Cassels, Arithmetic on curves of genus 1. IV. Proof of the Hauptvermutung, J. Reine Angew. Math. 211 (1962), 95–112. MR 0163915. Zbl 0106.03706. http://dx.doi.org/10.1515/crll.1962.211.95.

[13] J. E. Cremona, T. A. Fisher, and M. Stoll, Minimisation and reduction of 2-, 3- and 4-coverings of elliptic curves, Algebra Number Theory 4 (2010), 763–820. MR 2728489. Zbl 1222.11073. http://dx.doi.org/10.2140/ant.2010.4.763.

[14] H. Darmon, F. Diamond, and R. Taylor, Fermat’s last theorem, in Elliptic Curves, Modular Forms & Fermat’s Last Theorem (Hong Kong, 1993), Int. Press, Cambridge, MA, 1997, pp. 2–140. MR 1605752. Zbl 0997.11504.

[15] H. Davenport, On a principle of Lipschitz, J. London Math. Soc. 26 (1951), 179–183, [Corrigendum: “On a principle of Lipschitz”, J. London Math. Soc. 39 (1964), 580. MR 0166155. Zbl 0125.02703. http://dx.doi.org/10.1112/jlms/s1-39.1.580-t]. MR 0043821. Zbl 0042.27504. http://dx.doi.org/10.1112/jlms/s1-26.3.179.

[16] A. J. de Jong, Counting elliptic surfaces over finite fields, Mosc. Math. J. 2 (2002), 281–311, Dedicated to Yuri I. Manin on the occasion of his 65th birthday. MR 1944508. Zbl 1031.11033.

[17] T. Dokchitser and V. Dokchitser, On the Birch-Swinnerton-Dyer quotients modulo squares, Ann. of Math. 172 (2010), 567–596. MR 2680426. Zbl 1223. 11079. http://dx.doi.org/10.4007/annals.2010.172.567.

[18] W. Duke, Elliptic curves with no exceptional primes, C. R. Acad. Sci. Paris S´er. I Math. 325 (1997), 813–818. MR 1485897. Zbl 1002.11049. http://dx.doi.org/10.1016/S0764-4442(97)80118-8.

[19] T. Fisher, Testing equivalence of ternary cubics, in Algorithmic Number Theory, Lecture Notes in Comput. Sci. 4076, Springer-Verlag, New York, 2006, pp. 333–345. MR 2282934. Zbl 1143.11325. http://dx.doi.org/10.1007/11792086 24.

[20] T. Fisher, The invariants of a genus one curve, Proc. Lond. Math. Soc. 97 (2008), 753–782. MR 2448246. Zbl 1221.11135. http://dx.doi.org/10.1112/plms/pdn021.

[21] C. G. Gibson, Elementary Geometry of Algebraic Curves : An Undergraduate Introduction, Cambridge Univ. Press, Cambridge, 1998. MR 1663524. Zbl 0997. 14500. http://dx.doi.org/10.1017/CBO9781139173285.

[22] A. Kraus, Quelques remarques \`a propos des invariants c<sub>4</sub>, c<sub>6</sub> et ∆ d’une courbe elliptique, Acta Arith. 54 (1989), 75–80. MR 1024419. Zbl 0628.14024.

[23] S. Lang and A. Weil, Number of points of varieties in finite fields, Amer. J. Math. 76 (1954), 819–827. MR 0065218. Zbl 0058.27202. http://dx.doi.org/10.2307/2372655.

[24] R. P. Langlands, The volume of the fundamental domain for some arithmetical subgroups of Chevalley groups, in Algebraic Groups and Discontinuous Subgroups (Proc. Sympos. Pure Math., Boulder, Colo., 1965), Amer. Math. Soc., Providence, RI, 1966, pp. 143–148. MR 0213362. Zbl 0218.20041.

[25] J. Nekova<sup>´</sup>r<sup>ˇ</sup>, Selmer Complexes, Ast´erisque 310, 2006. MR 2333680. Zbl 1211. 11120.

[26] D. E. Rohrlich, Variation of the root number in families of elliptic curves, Compositio Math. 87 (1993), 119–151. MR 1219633. Zbl 0791.11026. Available at http://www.numdam.org/item?id=CM 1993 87 2 119 0.

[27] J. H. Silverman, The Arithmetic of Elliptic Curves, Grad. Texts in Math. 106, Springer-Verlag, New York, 1986. MR 0817210. Zbl 0585.14026. http://dx.doi.org/10.1007/978-1-4757-1920-8.

[28] C. Skinner and E. Urban, The Iwasawa Main Conjectures for GL<sub>2</sub>, Invent. Math. 195 (2014), 1–277. MR 3148103. Zbl 06261655. http://dx.doi.org/10.1007/s00222-013-0448-1.

[29] S. Wong, On the density of elliptic curves, Compositio Math. 127 (2001), 23–54. MR 1832985. Zbl 1003.11023. http://dx.doi.org/10.1023/A:1017514507447.

Princeton University<sub>,</sub> Princeton<sub>,</sub> NJ E-mail : bhargava@math.princeton.edu

Harvard University<sub>,</sub> Cambridge<sub>,</sub> MA E-mail : arul@math.harvard.edu