# STRICHARTZ ESTIMATES FOR THE SCHRODINGER EQUATION ON <sup>¨</sup> NON-RECTANGULAR TWO-DIMENSIONAL TORI

YU DENG, PIERRE GERMAIN, LARRY GUTH, AND SIMON L. RYDIN MYERSON

Abstract. We propose a conjecture for long time Strichartz estimates on generic (non-rectangular) flat tori. We proceed to partially prove it in dimension 2. Our arguments involve on the one hand Weyl bounds; and on the other hands bounds on the number of solutions of Diophantine problems.

## 1. Introduction

1.1. A general question. It is a classical result that, if v is a solution of the linear Schr¨odinger equation on$\mathbb { R } ^ { d }$with data$v _ { 0 }$

$$
i \partial_ {t} v - \Delta_ {M} v = 0, \qquad v (0, x) = v _ {0} (x),
$$

and if furthermore$P _ { N }$is a projector on frequencies$\lesssim N$, then

$$
\| P _ {N} v \| _ {L ^ {p} (\mathbb {R} \times \mathbb {R} ^ {d})} \lesssim N ^ {s} \| v _ {0} \| _ {L ^ {2} (\mathbb {R} ^ {d})} \quad \text { with } s = \max \left(0, \frac {d}{2} - \frac {d + 2}{p}\right)\tag{1.1}
$$

(Strichartz estimates for the linear Schr¨odinger equation are usually stated with diferent space and time Lebesgue indices, see [29]; the above inequality follows from these through the Sobolev embedding theorem).

Can this inequality be extended to compact manifolds? Let M be a compact Riemannian manifold without boundary, let$v _ { 0 } \in L ^ { 2 } ( M )$and let v be the solution to the linear Schr¨odinger equation

$$
i \partial_ {t} v - \Delta_ {M} v = 0, \qquad v (0, x) = v _ {0} (x)\tag{1.2}
$$

where$\Delta _ { M }$is the Laplace-Beltrami operator on M. Finally, let$P _ { N }$be a projector on eigenmodes of the Laplacian$< N ^ { 2 }$, for instance$\begin{array} { r } { P _ { N } = \chi \left( \frac { - \Delta _ { M } } { N ^ { 2 } } \right) } \end{array}$, where$\chi$is a smooth cutof function.

In order to extend the inequality (1.1), a natural question is to determine the best constant $C ( T , p , N , M )$in

$$
\left\| P _ {N} v \right\| _ {L ^ {p} ([ 0, T ] \times M)} \leq C (T, p, N, M) \| v _ {0} \| _ {L ^ {2} (M)}.\tag{1.3}
$$

In cases where such a problem could be solved, experience shows that the dependence of$C$on$T , p ,$N is in general of the type$N ^ { s _ { 1 } ( p ) } T ^ { s _ { 2 } ( p ) }$, or a sum of such summands, up to possible subpolynomial factors$O _ { \epsilon } ( N ^ { \epsilon } T ^ { \epsilon } )$

Writing$\| v _ { 0 } \| _ { H ^ { s } }$for the Sobolev norm (defined through fractional powers of$\Delta _ { M } )$, it is essentially equivalent to examine inequalities of the type$\| P _ { N } v \| _ { L ^ { p } ( [ 0 , T ] \times M ) } \leq C \| v _ { 0 } \| _ { H ^ { s } ( M ) }$

1.2. Background for$T = 1$. Burq, G´erard and Tzvetkov in [12], showed that, for general ddimensional compact Riemannian manifolds,

$$
\| P _ {N} v \| _ {L ^ {p} ([ 0, 1 ] \times M)} \lesssim N ^ {s (p)} \| v _ {0} \| _ {L ^ {2} (M)} \quad \text { with } s (p) = \max \left(\frac {d}{4} - \frac {d}{2 p}, \frac {d}{2} - \frac {d + 1}{p}\right).
$$

Notice that these authors actually proved more general inequalities (Theorem 1 in [12]), allowing for a diferent Lebesgue index in time and space. As a consequence of the above estimate, the deduce existence results for certain nonlinear Schr¨odinger equations in two and three dimensions.

Is the above estimate optimal for some$M ?$This seems unclear. In the case of the sphere (or more generally of Zoll manifolds), which might lead to the largest constants$C ( T , p , N , M )$(in particular since it has very concentrated eigenmodes of the Laplacian), the above authors show (Theorem 4 in [12]) that the above estimate can be improved, if$p = 4$, to

$$
s (4) = \max \left(\frac {1}{8}, \frac {d}{4} - \frac {1}{2}\right);
$$

this is furthermore optimal if$d \geq 3$

The best-studied situation is when M is a flat torus$\mathbb { R } ^ { d } / \Lambda$for some rank d lattice Λ. In the foundational paper of Bourgain [3], Strichartz estimates lead to well-posedness results for the nonlinear Schr¨odinger equation on the square torus$\mathbb { T } ^ { d } = \mathbb { R } ^ { d } / \mathbb { Z } ^ { d }$. This led to much subsequent work on the nonlinear problem, see for example [24] and [25] for the energy-critical case. Coming back to (linear) Strichartz estimates, Bourgain stated a conjecture [3, (3.2)-(3.4), cf. (1.7)] for these Strichartz estimates which was pursued in a number of works [5, 6, 18], culminating in Theorem 2.2 of Bourgain and Demeter [8] which delivers an essentially sharp range

$$
\| P _ {N} v \| _ {L ^ {p} ([ 0, 1 ] \times M)} \lesssim N ^ {s (p)} \| v _ {0} \| _ {L ^ {2} (M)} \quad \text { with } s (p) > \max \left(0, \frac {d}{2} - \frac {d + 2}{p}\right).\tag{1.4}
$$

for general tori.

When M is a flat torus and T is large, we study refinements of (1.4) and their relation to the geometry of M. Note that this case is significant in connection with weak turbulence for nonlinear Schr¨odinger equations [15, 14]. We conjecture that the optimal bound is sensitive to the geometry of the torus$M ,$depending on whether M is rectangular$( M = \mathbb { R } / \theta _ { i } \mathbb { Z } )$and also on whether the spectrum of$\Delta _ { M }$the torus is rational, in the sense that all ratios of eigenvalues are rational numbers. We prove a lower bound supporting this conjecture, and in the two-dimensional case we give partial results toward it.

For the rest of this paper we restrict to the case when M is a flat torus.

## 1.3. Strichartz estimates on tori for$T \geq 1$. Define a torus

$$
M = M _ {e _ {1} \dots e _ {d}} = \mathbb {R} ^ {d} / (\mathbb {Z} e _ {1} + \dots + \mathbb {Z} e _ {d}),
$$

where$e _ { 1 } , \ldots , e _ { d }$are linearly independent vectors of$\mathbb { R } ^ { d }$. As above, we ask for the best constant $C ( p , T , N , M )$in

$$
\left\| e ^ {i t \Delta_ {M}} f \right\| _ {L ^ {p} ([ 0, T ] \times M)} \leq C (p, T, N, M) \| f \| _ {L ^ {2} (M)},\tag{1.5}
$$

where$T \geq 1$and the Fourier transform$\hat { f }$is supported on the ball$B ( 0 , N )$

The three first authors [16] investigated the case$T \geq 1$in the “rectangular” case where$( e _ { 1 } , \ldots , e _ { d } )$ form an orthogonal basis; we focus in the present article on the case where$( e _ { 1 } , \ldots , e _ { d } )$are in general position.

We change variables as follows. If x M then write

$$
x = y _ {1} e _ {1} + \dots + y _ {d} e _ {d}
$$

(so that now$y \in \mathbb { T } ^ { d } = \mathbb { R } ^ { d } / \mathbb { Z } ^ { d } )$and expand in Fourier series

$$
f (x) = \sum \widehat {f} _ {k} e ^ {2 \pi i k \cdot y}.
$$

Then$\nabla _ { x } = A \nabla _ { y }$for a matrix A, and

$$
\Delta_ {M} f (x) = - 4 \pi^ {2} \sum_ {k \in \mathbb {Z} ^ {d}} | A k | ^ {2} \widehat {f} _ {k} e ^ {2 \pi i k \cdot y}.
$$

In other words, it sufices to consider the inequality

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbf {T} ^ {d})} \leq C (p, T, N, M) \| f \| _ {L ^ {2} (\mathbf {T} ^ {d})},
$$

where

$$
\widetilde {\Delta} = \frac {1}{2 \pi} \sum \alpha_ {i j} \partial_ {i} \partial_ {j}, \quad \text {   for   a   symmetric,   positive   definite,   matrix   } (\alpha_ {i j}) = 2 \pi A ^ {T} A.
$$

Without loss of generality we set$\alpha _ { 1 1 } = 1$

By dividing the range for t into pieces of length 1, the result of Bourgain and Demeter referred to around (1.4) implies that for$p \geq 2$and$\epsilon > 0$we have

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbf {T} ^ {d})} \lesssim_ {p, (\alpha_ {i j}), \epsilon} T ^ {1 / p} N ^ {\epsilon} (1 + N ^ {\frac {d}{2} - \frac {d + 2}{p}}) \| f \| _ {L ^ {2} (\mathbf {T} ^ {d})}.\tag{1.6}
$$

In this formulation, we ask whether the factor$T ^ { 1 / p }$can be improved for large$T .$

If the$\alpha _ { i j }$are rational (equivalently: if the eigenvalues of$\Delta _ { M }$all lie in$\mathbb { Q } )$then the operator$e ^ { i t \tilde { \Delta } }$ is periodic, and consequently$T ^ { 1 / p }$is the correct growth rate as$T \to \infty$. If the$\alpha _ { i j }$were unusually well approximated by rational numbers, for example if they were Liouville numbers, then one would expect a similar behavior.

If the$\alpha _ { i j }$are not well approximable by rational numbers then one expects$C$to grow more slowly than$T ^ { 1 / p }$. In [16] the first three authors conjecture that if$\left( \alpha _ { i j } \right)$is diagonal then

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbf {T} ^ {d})} \lesssim_ {p, (\alpha_ {i j}), \epsilon} N ^ {\epsilon} (T ^ {1 / p} + N ^ {\frac {d}{2} - \frac {d + 2}{p}} + T ^ {1 / p} N ^ {\frac {d}{2} - \frac {3 d}{p}}) \| f \| _ {L ^ {2} (\mathbf {T} ^ {d})},
$$

provided$\left( \alpha _ { i j } \right)$is generic; that is provided$\left( \alpha _ { i j } \right)$is lies outside an exceptional set of diagonal matrices E which has d-dimensional Lebesgue measure zero. The following conjecture proposes a stronger result for general, not necessarily diagonal matrices$\left( \alpha _ { i j } \right)$

Let E be the set of all symmetric$\left( \alpha _ { i j } \right)$such that$- 2 \leq \alpha _ { i j } \leq 2$, and with smallest absolute eigenvalue$| \lambda _ { 1 } | > 1$. In the remainder of this paper we say that a statement holds for generic$\left( \alpha _ { i j } \right)$ if it is true for all$( \alpha _ { i j } ) \in E \setminus F$, where F has Lebesgue measure zero. Implicit constants might of course not be uniform in$\left( \alpha _ { i j } \right)$

Conjecture 1.1. For$p \geq 2 ,$, generic$\left( \alpha _ { i j } \right)$, and any$\epsilon > 0$

$$
\left\| e ^ {i t \widetilde {\Delta}} f \right\| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {d})} \lesssim N ^ {\epsilon} \left[ N ^ {\frac {d}{2} - \frac {d + 2}{p}} + T ^ {\frac {1}{p}} \sum_ {n = 0} ^ {d} N ^ {\frac {n}{2} - \frac {n ^ {2} + 2 n}{p}} \right] \| f \| _ {L ^ {2} (\mathbb {T} ^ {d})},
$$

provided Supp${ \widehat { f } } \subset B ( 0 , N )$

This can also be written

$$
\begin{array}{l} \| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {d})} \lesssim \\ N ^ {\epsilon} \| f \| _ {L ^ {2} (\mathbb {T} ^ {d})} \left\{ \begin{array}{l l} T ^ {\frac {1}{p}} & \text { if } 2 \leq p \leq \frac {2 (d + 2)}{d} \\ N ^ {\frac {d}{2} - \frac {d + 2}{p}} + T ^ {\frac {1}{p}} & \text { if } \frac {2 (d + 2)}{d} <   p \leq 6 \\ N ^ {\frac {d}{2} - \frac {d + 2}{p}} + T ^ {\frac {1}{p}} N ^ {\frac {n}{2} - \frac {n ^ {2} + 2 n}{p}} & \text { if } 4 n + 2 <   p \leq 4 n + 6, \text { with } n \in \{1, \ldots , d - 1 \} \\ N ^ {\frac {d}{2} - \frac {d + 2}{p}} + T ^ {\frac {1}{p}} N ^ {\frac {d}{2} - \frac {d ^ {2} + 2 d}{p}} & \text { if } p > 4 d + 2 \end{array} \right. \end{array}
$$

The heuristic behind this conjecture, and some supporting lower bounds, are explained in section 2 below. In particular, it is seen there that the saving over the rectangular case is due to the longer refocusing time, which more closely reflects the expected behavior on a “typical” nonpositively curved manifold.

We now focus on the case of dimension$d = 2 .$, in which case the above conjecture becomes:

For$p \leq 4$, bound$\sim T ^ { \frac { 1 } { p } }$

For$4 < p \le 6$, bound$\sim T ^ { \frac { 1 } { p } } + N ^ { 1 - \frac { 4 } { p } }$(with a cutof at$T \sim N ^ { p - 4 } )$

For$6 < p \le 1 0$, bound$\sim T ^ { \frac { 1 } { p } } N ^ { \frac { 1 } { 2 } - \frac { 3 } { p } } + N ^ { 1 - \frac { 4 } { p } }$(with a cutof at$T \sim N ^ { \frac { p } { 2 } - 1 } )$

• <sup>For</sup>$p > 1 0$, bound$\sim N ^ { 1 - \frac { 8 } { p } } T ^ { \frac { 1 } { p } } + N ^ { 1 - \frac { 4 } { p } }$(with a cutof at$T \sim N ^ { 4 } )$

From (1.6) one immediately obtains the conjecture for$p < 4$. Our results for the remaining cases are as follows.

Theorem 1.1.$I f d = 2$, for generic$\left( \alpha _ { i j } \right)$and for$p > 4$

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} \lesssim_ {\alpha , \epsilon} N ^ {\epsilon} \| f \| _ {L ^ {2} (\mathbb {T} ^ {d})} \left[ N ^ {1 - \frac {4}{p}} + T ^ {\frac {1}{p}} N ^ {\frac {2}{3} (1 - \frac {4}{p})} \right],
$$

provided Supp${ \widehat { f } } \subset B ( 0 , N )$

The theorem, which is proved in sections 3 and 4, thus misses the conjecture when$4 < p < 6$ and$T > N ^ { p - 4 }$by a factor of$N ^ { \frac { 2 } { 3 } ( 1 - \frac { 4 } { p } ) }$. Proving Strichartz estimates can be reduced to counting solutions of Diophantine inequalities when the Lebesgue index is an even integer. Using this idea, the cases$p = 8 , 1 0$can be addressed, and they are the focus of the next theorem; but the case$p = 6$ seems to remain out of reach.

Theorem 1.2. The conjecture holds for$d = 2 , p \ge 8$. In other words, there holds, for generic $\left( \alpha _ { i j } \right)$and all$\epsilon > 0$

$$
\begin{array}{l l} i f 8 \leq p \leq 1 0, & \| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} \lesssim_ {\alpha , \epsilon} N ^ {\epsilon} \| f \| _ {L ^ {2} (\mathbb {T} ^ {d})} \left[ N ^ {1 - \frac {4}{p}} + T ^ {\frac {1}{p}} N ^ {\frac {1}{2} - \frac {3}{p}} \right] \\ i f p > 1 0, & \| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} \lesssim_ {\alpha , \epsilon} N ^ {\epsilon} \| f \| _ {L ^ {2} (\mathbb {T} ^ {d})} \left[ N ^ {1 - \frac {4}{p}}   +   N ^ {1 - \frac {8}{p}} T ^ {\frac {1}{p}} \right], \end{array}
$$

provided Supp${ \widehat { f } } \subset B ( 0 , N )$

Remark 1.3. Most of the arguments developed in the present article apply to the case when the”elliptic” Laplacian$\partial _ { x } ^ { 2 } + \partial _ { y } ^ { 2 }$is replaced by a ”hyperbolic” Laplacian$\partial _ { x } ^ { 2 } - \partial _ { y } ^ { 2 }$; or in other words, when the symmetric matrix$\left( \alpha _ { i j } \right)$is allowed to be indefinite, but remains non-degenerate. However, the $\ell ^ { 2 }$decoupling inequality follows a diferent numerology, see [10].$\mathrm { A s \ a }$consequence, the results for $p \geq 8$are identical for elliptic and hyperbolic Laplacian, but for$p \leq 8 \mathrm { ~ a ~ }$diferent set of exponents is found.

1.3.1. The Weyl bound argument. This is used to prove Theorem 1.1. Let$d = 2$. With$f ( x ) =$ $\textstyle \sum _ { k \in \mathbb { Z } ^ { 2 } } { \widehat { f } } _ { k } e ^ { 2 \pi i k \cdot x }$, we have

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {p} = \int_ {0} ^ {T} \int_ {\mathbb {T} ^ {2}} \bigg | \sum_ {n \in \mathbb {Z} ^ {2}} \hat {f} _ {n} e ^ {2 \pi i [ x \cdot n + t \sum_ {i, j} \alpha_ {i j} n _ {i} n _ {j} ]} \bigg | ^ {p} d x d t.\tag{1.7}
$$

We construct an exponential sum like that inside the absolute value, with the$\hat { f } _ { n }$replaced by some more tractable coeficients. Let$\chi : \mathbb { R } ^ { 2 } \to [ 0 , \infty )$be a compactly supported smooth cutof function. Let$K _ { N }$denote the exponential sum

$$
K _ {N} (t, x) = \sum_ {n \in \mathbb {Z} ^ {2}} \chi \left(\frac {n _ {1}}{N}\right) \chi \left(\frac {n _ {2}}{N}\right) e ^ {2 \pi i [ x \cdot n + t \sum_ {i, j} \alpha_ {i j} n _ {i} n _ {j} ]},
$$

which can be regarded as a regularized fundamental solution of$( i \partial _ { t } - \tilde { \Delta } ) u = 0$

eSimilar sums are investigated by Bentkus and G¨otze [1, 2], G¨otze [21], M¨uller [23] and G¨otze and Margulis [20] in the case when$\left( \alpha _ { i j } \right)$is irrational, that is not a multiple of a matrix with rational entries. We investigate this sum for generic$\left( \alpha _ { i j } \right)$. In Lemma 3.1 and Proposition 3.2 we will prove the following bounds:

$$
\begin{array}{r l r l} & {\sup _ {x \in \mathbb {T} ^ {2}} | K _ {N} (t, x) | \lesssim \min \left(N ^ {2}, \frac {1}{t}\right)} & & {(T \lesssim \frac {1}{N}),} \\ & {\sup _ {x \in \mathbb {T} ^ {2}} | K _ {N} (t, x) | \preceq N ^ {4 / 3} (1 + t ^ {1 / 6})} & & {(T > \frac {1}{N}),} \\ & {\int_ {1} ^ {T} \sup _ {x \in \mathbb {T} ^ {2}} | K _ {N} (t, x) | ^ {4} d t \preceq N ^ {4} T} & & {(T > 1).} \end{array}
$$

We prove these estimates using the geometry of numbers approach pioneered by Davenport [13]. The first one is classical and optimal. An analysis similar to step (2) in section 2 suggests that $N ( 1 + t ^ { 1 / 4 } )$might be the correct bound in the second formula. The third bound can be related to a system of diagonal equations to see that on average over$\alpha _ { i j }$it is optimal, see also section 1.4 below.

The classical$T T ^ { * }$argument of Stein-Tomas can be localized to obtain level-set estimates for $| e ^ { i t \tilde { \Delta } } f ( x , t ) |$. Consider$f$a function on the torus, normalized in$L ^ { 2 }$, and localized in Fourier on $B ( 0 , N )$, and let

$$
E _ {\lambda} = \{(x, t) \in \mathbb {T} ^ {2} \times [ - T, T ] \mathrm{s.t.} | e ^ {i t \bar {\Delta}} f (x, t) | > \lambda \}.
$$

Then, if$\chi ( t / T ) K _ { N } ( t , x )$is split into

$$
\chi (t / T) K _ {N} (t, x) = J _ {1} (t, x) + J _ {2} (t, x),
$$

one can bound

$$
| E _ {\lambda} | \lesssim \frac {1}{\lambda^ {2} - \| J _ {2} \| _ {L ^ {\infty}}} \| \widehat {J} _ {1} \| _ {L ^ {\infty}}
$$

provided$\lambda ^ { 2 } > \| J _ { 2 } \| _ { L ^ { \infty } } )$. The question becomes then: how can one optimally split$\chi ( t / T ) K _ { N } ( t , x )$ into$J _ { 1 } + J _ { 2 }$, by making the norm of$J _ { 2 }$in$L ^ { \infty }$, and that of$J _ { 1 }$in$\widehat { L ^ { \infty } }$small? Let

$$
S = \left\{t \in [ 0, T ]: \sup _ {x \in \mathbf {T} ^ {2}} | \chi (t / T) K _ {N} (t, x) | \geq \lambda^ {2} \right\}
$$

and let$J _ { 1 } = { \bf 1 } _ { S } ( t ) \chi ( t / T ) K _ { N } ( t , x )$and$J _ { 2 } = [ 1 - \mathbf { 1 } _ { S } ( t ) ] \chi ( t / T ) K _ { N } ( t , x )$. The bound$\lambda ^ { 2 } > \| J _ { 2 } \| _ { L ^ { \infty } }$is then trivial. But we compute

$$
\widehat {J} _ {1} (k, \tau) = \chi \left(\frac {k _ {1}}{N}\right) \chi \left(\frac {k _ {2}}{N}\right) \int \phi \left(\frac {t}{T}\right) \mathbf {1} _ {S} (t) e ^ {2 \pi i t (\sum_ {i, j} \alpha_ {i j} k _ {i} k _ {j} - \tau)} d t
$$

and so

$$
\| \widehat {J} _ {1} \| _ {L ^ {\infty}} \lesssim | S |.
$$

The measure$| S |$bcan be controlled using the bounds for$\mathrm { s u p } _ { x \in \mathbf { T } ^ { 2 } } | K _ { N } ( t , x ) |$discussed above.

The approach which was has been sketched is implemented in sections 3 and 4:

Section 2 is dedicated to establishing bounds for the Weyl sum$K _ { N }$

These bounds are then used in Section 3 to deduce Theorem 1.1 by the modified$T T ^ { * }$ argument.

1.3.2. The counting argument. This is used to prove Theorem 1.2. If$p$is an even integer, one deduces from (1.7) that

$$
\| e^{it\widetilde{\Delta}}f\|_{L^{p}([0,T]\times \mathbb{T}^{2})}^{p} = \sum_{\substack{k_{1}\ldots k_{p}\in \mathbb{Z}^{2}\\ k_{1} - k_{2} + \dots -k_{p} = 0}}\widehat{f}_{k_{1}}\overline{\widehat{f}_{k_{2}}} \ldots \overline{\widehat{f}_{k_{p}}}\frac{1 - e^{2\pi iT\Omega(k_{1},\ldots,k_{p})}}{2\pi i\Omega(k_{1},\ldots,k_{p})},
$$

where, denoting$Q$the quadratic form associated to$( \alpha _ { i j } )$

$$
\Omega (k _ {1}, \ldots , k _ {p}) = Q (k _ {1}) - Q (k _ {2}) + \dots - Q (k _ {p}).
$$

After some manipulations, matters reduce to counting weighted solutions of Diophantine inequalities. In Section 5, the decoupling theory of Bourgain and Demeter [9] leads to the proof of the conjecture for$p \geq 1 6$in a rather straightforward way. Alternatively, one can sum trivially over the odd numbered vectors$k _ { 1 } , k _ { 3 } , . . .$. and proceed by seeking a bound for the number of solutions to

$$
\left| Q \left(k _ {2}\right) + Q \left(k _ {4}\right) + \dots + Q \left(k _ {p}\right) - \beta \right| <   \delta , \quad k _ {2} + k _ {4} + \dots + k _ {p} = a, \quad k _ {i} \in \mathbb {Z} ^ {2} \cap B (0, N),\tag{1.8}
$$

which is uniform in$a , \beta .$. To recover the conjecture it is necessary, in particular, to have an optimal bound in the case$\begin{array} { r } { \delta = \frac { 1 } { N } } \end{array}$

There is previous work on bounds for the count of integer solutions to a generic quadratic inequality, where one wants uniformity in certain parameters [7, 19, 26]. In those cases one in interested principally in lower bounds. In short, the strategy is to seek an asymptotic for the number of solutions which is valid unless the coeficients lie in a set with small measure. If the sum of this measure over all values of the parameters is finite, then by the Borel-Cantelli lemma the asymptotic holds for generic values of the coeficients.

It seems that this strategy does not work in our case, as we want uniformity in a rather large range of parameters and the space of coeficients has a relatively low dimension compared to the number of variables.

In Section 6 we use an alternative approach to count solutions to (1.8), proving the conjecture in the case$p = 8$. We rely on the formula of Pall [27] on the number of solutions$( k _ { 1 } , k _ { 2 } , k _ { 3 } , \ell _ { 1 } , \ell _ { 2 } , \ell _ { 3 } )$ to the system

$$
k _ {1} ^ {2} + k _ {2} ^ {2} + k _ {3} ^ {2} = A, \qquad \ell_ {1} ^ {2} + \ell_ {2} ^ {2} + \ell_ {3} ^ {2} = B, \qquad k _ {1} \ell_ {1} + k _ {2} \ell_ {2} + k _ {3} \ell_ {3} = C.
$$

The ensuing analysis is delicate but repeatedly falls back on a simple estimate: for any$k \geq 2$ the number of solutions$x \in \mathbb { Z } ^ { d } \cap B ( 0 , N )$to some inequality$| f ( x ) - \nu | < \delta$is at most$N _ { k } ^ { 1 / k }$2 where$N _ { k }$is the number of k-tuples$x _ { 1 } , \ldots , x _ { k } \in \mathbb { Z } ^ { d } \cap B ( 0 , N )$such that$f ( x _ { 1 } ) - f ( x _ { i } ) = O ( \delta )$for each$i = 2 , \ldots , k$. In particular$N _ { k }$is independent of the parameter$\nu ,$allowing for uniform upper bounds.

Finally, Section 7 contains the proof of the conjecture for$p = 1 0$, also making use of Pall’s formula, but this case turns out to be much simpler than$p = 8$

1.4. Higher dimensions d. One naturally asks whether the proof of Theorems 1.1 and 1.2 can be extended to$d > 2$

We first consider Theorem 1.1. To follow the strategy of section 1.3.1 for$d > 2$we would define

$$
K _ {N} ^ {(d)} (t, x) = \sum_ {n \in \mathbb {Z} ^ {d}} \chi \left(\frac {n _ {1}}{N}\right) \dots \chi \left(\frac {n _ {d}}{N}\right) e ^ {2 \pi i [ x \cdot n + t \sum_ {i, j} \alpha_ {i j} n _ {i} n _ {j} ]},
$$

and we would then look for bounds on the quantities

$$
S (T) = \sup _ {x \in \mathbf {T} ^ {d}, t \in [ T, 2 T ]} \left| K _ {N} ^ {(d)} (t, x) \right|, \qquad I _ {s} (T) = \int_ {1} ^ {T} \sup _ {x \in \mathbf {T} ^ {d}} \left| K _ {N} ^ {(d)} (t, x) \right| ^ {2 s} d t \qquad (s \in \mathbb {N}).\tag{1.9}
$$

As a first bound on$I _ { s } ( T )$, it follows from the work of Guo and Zhang [22] that for generic$\left( \alpha _ { i j } \right)$we have

$$
I _ {s} (T) \lesssim N ^ {\epsilon} T (N ^ {d s + d} + N ^ {2 d s - d (d + 1)}).\tag{1.10}
$$

See Appendix A for a brief account of the argument by which (1.10) follows from the cited work. There we also sketch a strategy for replacing the$d s + d$with ds.

One might be able to imitate the proof of our Proposition 3.2 to bound$I _ { s } ( T )$and$S ( T )$from (1.9). To see how, let$E ^ { d }$be the set of all$d \times d$symmetric$\left( \alpha _ { i j } \right)$such that$- 2 \leq \alpha _ { i j } \leq 2$, and with smallest absolute eigenvalue$| \lambda _ { 1 } | > 1$. To majorize$S ( T )$we would need to bound

$$
\begin{array}{c} \mu_ {1} (T, \vec {\gamma}) = \text {measure} \left\{(\alpha_ {i j}) \in E: \alpha_ {i 1} n _ {1} ^ {(j)} + \dots + \alpha_ {i d} n _ {d} ^ {(j)} = t ^ {- 1} m _ {i} ^ {(j)} + O \Big (\frac {\gamma_ {j}}{T N} \Big) \right. \\ \text {for all} i, j = 1, \ldots , d \text {and some} t \sim T, n _ {i} ^ {(j)} \lesssim \gamma_ {j} N, m _ {i} ^ {(j)} \lesssim T \gamma_ {j} N \big \} \end{array}
$$

for appropriate$\begin{array} { r } { \frac { 1 } { N } \leq \gamma _ { i } \leq 1 } \end{array}$. For$I _ { s } ( T )$the analogous quantity is

$$
\begin{array}{c} \mu_ {2} (t) = \text {measure} \big \{(\alpha_ {i j}) \in E: \alpha_ {i 1} n _ {1} ^ {(j)} + \dots + \alpha_ {i d} n _ {d} ^ {(j)} = t ^ {- 1} m _ {i} ^ {(j)} + O \Big (\frac {1}{t N} \Big) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {for all i,j = 1,\ldots,d and some n_{i} ^{(j)} \lesssim N, m_{i} ^{(j)} \lesssim tN} \big \}. \end{array}
$$

We suggest that it may be possible to estimate$\mu _ { 1 }$and$\mu _ { 2 }$using the geometry of numbers.

Finally we consider extending the proof of Theorem 1.2, as outlined in section 1.3.2, to the case $d > 2$. The problem here is easier to describe. Given a symmetric integer matrix$( A _ { i j } )$, one requires a bound for the number of solution$y ^ { ( 1 ) } , \dots , y ^ { ( d + 1 ) } ) \in (  { \mathbb { Z } } ^ { d } ) ^ { d + 1 }$with$| y ^ { ( k ) } | \lesssim N$to the system

$$
\sum_ {k = 1} ^ {d + 1} y _ {i} ^ {(k)} y _ {j} ^ {(k)} = A _ {i j} \quad (1 \leq i \leq j \leq d)
$$

and one requires this bound to have explicit dependence on the$A _ { i j }$. One possibility is to use the Siegel mass formula as in [11].

## 1.5. Notations.

For x a real number, x denotes the smallest distance to an integer:$\left\| x \right\| = \operatorname* { m i n } _ { k \in \mathbb { Z } } \left| x - k \right|$

We denote$A \lesssim B$if there exists a universal constant such that$| A | \leq C B ;$; and$A \sim B$if $A \lesssim B$and$B \lesssim A$

We denote$A \preceq B { \mathrm { ~ i f } } ,$for any$\epsilon > 0$, there exists$C _ { \epsilon }$such that$\vert A \vert \le C _ { \epsilon } N ^ { \epsilon } B .$

We follow the analytic (rather than the number analytic) convention in using the somewhat informal notation$A \ll B$if there is a very small constant c such that$A \leq c B$

Given a set$E _ { i }$, its characteristic function${ \mathbf { 1 } } _ { E } ( x )$equals 1 if$x \in E$, and 0 otherwise.

For$f ( x )$a function on the torus T, its Fourier coeficients are

$$
\mathrm{for} k \in \mathbb {Z} ^ {2}, \qquad \widehat {f _ {k}} = \int_ {\mathbb {T} ^ {2}} f (x) e ^ {- 2 \pi i k \cdot x} d x.
$$

For$f ( t , x )$a function on$\mathbb { R } \times \mathbb { T }$, its space-time Fourier transform is given by

$$
\mathrm{for} (\tau , k) \in \mathbb {R} \times \mathbb {Z} ^ {2}, \qquad \widehat {f} (\tau , k) = \int_ {\mathbb {R}} \int_ {\mathbb {T} ^ {2}} f (t, x) e ^ {- 2 \pi i k \cdot x - 2 \pi i t \tau} d x d t.
$$

• <sup>Finally,</sup>$\langle t \rangle = { \sqrt { 1 + t ^ { 2 } } } .$

Acknowledgements. While working on this project, Y. D. was supported by the$\mathrm { N S F }$grant DMS-1900251.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. G. was supported by a Simons Investigator Award.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">S. M. was supported by the Engineering and Physical Sciences Research Council [EP/M507970/1],[EP/M507970/1] by the European Research Council under ERC grant agreement no. 670239, by the Fields Institute for Research in Mathematical Sciences, and by NSF-DMS 1363013.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">P. G. was supported by the NSF grant DMS-1501019, by the Simons collaborative grant on weak turbulence, and by the Center for Stability, Instability and Turbulence (NYUAD).</span></small>

## 2. The conjecture

In order to formulate a conjecture, we examine a few particular functions$f ,$, and determine heuristically the ratio$\| e ^ { i t \tilde { \Delta } } f \| _ { L ^ { p } ( [ 0 , T ] \times  { \mathbb { T } } ^ { d } ) } / \| f \| _ { L ^ { 2 } (  { \mathbb { T } } ^ { d } ) }$which they yield.

(1) If$f = 1$, we find$\| e ^ { i t \widetilde { \Delta } } f \| _ { L ^ { p } ( [ 0 , T ] \times  { \mathbb { T } } ^ { d } ) } \sim T ^ { \frac { 1 } { p } }$

(2) Choose$f ( x ) = N ^ { \frac { d } { 2 } } \chi \left( N x \right)$for a smooth compactly supported function$\chi .$. Then$f$is normalized in$L ^ { 2 }$, with$\| f \| _ { L ^ { 2 } (  { \mathbb { T } } ^ { d } ) } \sim 1$, and the transform$\hat { f }$has rapid decay outside the ball $B ( 0 , N )$. Furthermore, for$\begin{array} { r } { \frac { 1 } { N ^ { 2 } } \ll t \ll \frac { 1 } { N } , e ^ { i t \widetilde { \Delta } } f } \end{array}$nearly coincides with the solution of the Schr¨odinger equation on$\mathbb { R } ^ { d }$with initial data$f _ { i }$which is mostly supported on$B ( 0 , t N )$and has size$\sim \frac { 1 } { ( t N ) ^ { d / 2 } } ;$this is because the solution to this PDE propagates at a group velocity$\lesssim N$, hence for times$\ll \frac { 1 } { N }$, the diference between the torus and the whole space is negligible. Therefore

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, 1 ] \times \mathbb {T} ^ {d})} ^ {p} \gtrsim \int_ {\frac {1}{N ^ {2}}} ^ {\frac {1}{N}} \int_ {B (0, t N)} \frac {d x d t}{(t N) ^ {d p / 2}} \gtrsim N ^ {\frac {d p}{2} - (d + 2)} \qquad \mathrm{if} p > \frac {2 (d + 2)}{d}.
$$

(3) We want to find the “refocusing time” with the same$f .$. In other words, how big should t be taken in order that$e ^ { i t \tilde { \Delta } } f$be similar to$f$itself? Or what is an “almost period” of the flow?

On a rectangular torus all possible$e ^ { i t \Delta } f$are periodic with a common period, forcing the refocusing time to be$O ( 1 )$; clearly this is not the typical behaviour of a nonpositively curved manifold.

The solution$e ^ { i t \tilde { \Delta } } f$can be expressed as

$$
e ^ {i t \widetilde {\Delta}} f (y) = N ^ {- d / 2} \sum_ {k \in \mathbb {Z} ^ {d}} \widehat {\chi} \left(\frac {k}{N}\right) e ^ {2 \pi i [ y \cdot k + t \sum \alpha_ {i j} k _ {i} k _ {j} ]}
$$

Heuristically, for$e ^ { i t \tilde { \Delta } } f$to be similar to$f ,$we need that

$$
\forall k \in \mathbb {Z} ^ {d} \quad \text { with } | k | \lesssim N, \qquad \| t \sum_ {i j} \alpha_ {i j} k _ {i} k _ {j} \| \ll 1,
$$

where$\lVert x \rVert$is the smallest distance of$x$to an integer (this is simply because this makes the time dependent summand in the complex exponential close to a integer multiple of$2 \pi )$ This will be achieved if$\begin{array} { r } { \| t \alpha _ { i j } \| \ll \frac { 1 } { N ^ { 2 } } } \end{array}$for all$i , j$. Since$\alpha _ { 1 1 } = 1$, we will look for$t \in \mathbb { N } ;$and since$\alpha _ { i j } = \alpha _ { j i } ,$this leaves$\scriptstyle { \frac { d ^ { 2 } + d - 2 } { 2 } }$independent coeficients.

By Dirichlet’s and Khinchin’s approximation theorems, for generic$\left( \alpha _ { i j } \right)$, and for any $\epsilon > 0$, there exists an integer$q$such that$N ^ { d ^ { 2 } + d - 2 - \epsilon } \lesssim q \lesssim N ^ { d ^ { 2 } + d - 2 }$and

$$
\forall i, j, \qquad \| q \alpha_ {i j} \| <   \frac {1}{N ^ {2}}.
$$

Choosing$t = q$, we find an almost period$\sim N ^ { d ^ { 2 } + d - 2 }$up to subpolynomial factors.

It is natural to expect that, at each refocusing time, a contribution similar to that found in (2) will occur. This suggests that, for any$\epsilon > 0$

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {d})} \gtrsim N ^ {\frac {d}{2} - \frac {d + 2}{p}} \left[ \frac {T}{N ^ {d ^ {2} + d - 2 - \epsilon}} \right] ^ {\frac {1}{p}} > N ^ {\frac {d}{2} - \frac {d ^ {2} + 2 d}{p} - \epsilon} T ^ {\frac {1}{p}}.
$$

(4) Compared to the rectangular case, we also have new competitors, namely n-dimensional data, where$n \in \{ 1 , \ldots , d - 1 \}$. Here we choose$f ( x ) = N ^ { n / 2 } \chi ( N x _ { 1 } , \ldots , N x _ { n } )$to depend only on (say) the first n variables, replicating the behavior on an n-dimensional torus. By the above, this give examples for which

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {d})} \gtrsim N ^ {\frac {n}{2} - \frac {n ^ {2} + 2 n}{p} - \epsilon} T ^ {\frac {1}{p}} \| f \| _ {L ^ {2} (\mathbb {T} ^ {d})}.
$$

These may dominate the contribution from (3), because the refocusing time grows rapidly with the dimension.

Overall, this gives the conjecture (1.1).

Remark 2.1. When p is an even integer, parts (1), (3) and (4) of the heuristic above can be made rigorous as follows (the remaining part is more straightforward).

Let$p \in 2 \mathbb { N }$and consider the lower bound on the number of solutions of the quadratic Parsell-Vinogradov system in Parsell, Prendiville and Wooley [28]. There, we learn that the number of solutions$( k ^ { ( 1 ) } , \dots , k ^ { ( p ) } ) \in (  { \mathbb { Z } } ^ { d } ) ^ { p }$of

$$
\forall \ell , m, n, \qquad \sum_ {j = 1} ^ {p} (- 1) ^ {j} k _ {\ell} ^ {(j)} = 0 \quad \text { and } \quad \sum_ {j = 1} ^ {p} (- 1) ^ {j} k _ {m} ^ {(j)} k _ {n} ^ {(j)} = 0,
$$

which furthermore satisfy$| k ^ { ( j ) } | < N$, is

$$
\gtrsim N ^ {\frac {p d}{2}} + \sum_ {j = 1} ^ {d} N ^ {(p - 1) j + d - j (j + 2)} \geq N ^ {\frac {p d}{2}} + N ^ {p d - d (d + 2)}
$$

(this is Theorem 1.2 in that paper; the notations there are related to ours by$2 s = p , k = 2$, while d remains the same). Defining f by its Fourier coeficients$\widehat { f } _ { k } = \mathbf { 1 } _ { | k | < N }$, the above bound implies that

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {d})} \gtrsim (N ^ {\frac {d}{2}} + N ^ {d - \frac {d (d + 2)}{p}}) T ^ {\frac {1}{p}} > \max (1, N ^ {\frac {d}{2} - \frac {d (d + 2)}{p}}) T ^ {\frac {1}{p}} \| f \| _ {L ^ {2} (\mathbb {T} ^ {d})}
$$

for generic$\alpha _ { i j }$and large T. Considering lower dimensional examples, we find that

$$
\text { as } T \to \infty , \qquad \sup _ {f} \frac {\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0 , T ] \times \mathbb {T} ^ {d})}}{\| f \| _ {L ^ {2} (\mathbb {T} ^ {d})}} \gtrsim T ^ {1 / p} \sum_ {n = 0} ^ {d} N ^ {\frac {n}{2} - \frac {n ^ {2} + 2 n}{p}}.
$$

This is consistent with the conjecture which was heuristically derived above.

## 3. Weyl sum estimates

3.1. Statement of the results. For χ a smooth, nonnegative function on$\mathbb { R } .$, equal to 1 on$B ( 0 , \scriptstyle { \frac { 1 } { 2 } } )$ and 0 on$B ( 0 , 1 ) ^ { \complement }$, we define the regularized fundamental solution

$$
K _ {N} (t, x) = \sum_ {n \in \mathbb {Z} ^ {2}} \chi \left(\frac {n _ {1}}{N}\right) \chi \left(\frac {n _ {2}}{N}\right) e ^ {2 \pi i [ x \cdot n + t \sum_ {i, j} \alpha_ {i j} n _ {i} n _ {j} ]}.
$$

We state without proof the following classical bound for short time, which does not use the genericity of the matrix$\left( \alpha _ { i j } \right)$

Lemma 3.1.$\begin{array} { r } { I f \left| t \right| \lesssim \frac { 1 } { N } } \end{array}$, then

$$
\forall x \in \mathbb {T} ^ {2}, \quad | K _ {N} (t, x) | \lesssim \min \left(N ^ {2}, \frac {1}{t}\right).
$$

Proof. This bound can be proved first on$\mathbb { R } ^ { 2 }$by stationary phase, and then transferred to the torus by Poisson summation.

For larger time, we obtain the following bounds.

Proposition 3.2. Consider a generic positive symmetric matrix$( \alpha _ { i j } ) _ { 1 \leq i , j \leq 2 }$, with eigenvalues $\lambda _ { 1 } < \lambda _ { 2 }$, which satisfies

$$
\forall i, j, \quad | \alpha_ {i j} | \leq 2, \quad a n d \quad \lambda_ {1} > 1.\tag{3.1}
$$

Then

(i) For any$\begin{array} { r } { t > \frac { 1 } { N } } \end{array}$(and recalling that$\langle t \rangle = \sqrt { 1 + t ^ { 2 } } )$

$$
\sup _ {x \in \mathbb {T} ^ {2}} | K _ {N} (t, x) | \preceq N ^ {4 / 3} \langle t \rangle^ {1 / 6}.
$$

(ii) For any$T \geq 1$

$$
\int_ {1} ^ {T} \sup _ {x \in \mathbb {T} ^ {2}} | K _ {N} (t, x) | ^ {4} d t \preceq N ^ {4} T.
$$

3.2. Proof of (i) in Proposition 3.2. The first step is to apply Weyl diferencing to obtain the following lemma, whose proof we postpone for the moment.

Lemma 3.3. Denoting$\begin{array} { r } { L _ { j } ( n ) = \sum \alpha _ { i j } n _ { i } } \end{array}$, for any$\boldsymbol { x } \in \mathbb { T } ^ { 2 }$and$t \in \mathbb { R }$，

$$
| K _ {N} (t, x) | ^ {2} \lesssim \sum_ {r _ {1} = - 2 N} ^ {2 N} \sum_ {r _ {2} = - 2 N} ^ {2 N} \prod_ {j = 1} ^ {2} \min \left(N, \frac {1}{\| 2 t L _ {j} (r) \|}\right).
$$

By the above,

$$
| K _ {N} (t, x) | ^ {2} \lesssim \sum_ {m _ {1}, m _ {2}} \# E _ {m _ {1}, m _ {2}} ^ {N} \frac {N ^ {2}}{\langle m _ {1} \rangle \langle m _ {2} \rangle}
$$

where

$$
E _ {m _ {1}, m _ {2}} ^ {N} = \{n \in [ - 2 N, 2 N ] ^ {2} \mathrm{s.t.} \frac {m _ {j} - 1}{N} \leq \| t L _ {j} (n) \| \leq \frac {m _ {j}}{N} \mathrm{for} j = 1, 2 \}
$$

But since any$n , n ^ { \prime }$in$E _ { m _ { 1 } , m _ { 2 } } ^ { N }$are such that$\vert n - n ^ { \prime } \vert < 4 N$, and$\begin{array} { r } { \| t L _ { j } ( n - n ^ { \prime } ) \| < \frac { 2 } { N } } \end{array}$, we find that

$$
\left. \left| K _ {N} (t, x) \right| ^ {2} \preceq N ^ {2} \left[ \# \{n \in [ - 4 N, 4 N ] ^ {2} \text {s.t.} \| t L _ {j} (n) \| <   \frac {2}{N} \} + 1 \right]. \right.\tag{3.2}
$$

We now apply Lemma 3 from [13] to get

$$
| K _ {N} (t, x) | ^ {2} \preceq \frac {N ^ {2}}{M _ {1} ^ {t} M _ {2} ^ {t}},
$$

where$( M _ { i } ^ { t } )$are the Minkowski minima for the norm on$\mathbb { R } ^ { 4 }$given by

$$
\text { if } (n, m) \in \mathbb {Z} ^ {4}, \quad F (n, m) = \max \left(\left| \frac {n _ {i}}{N} \right|, N | t L _ {i} (n) - m _ {i} |\right).
$$

Recall that$M _ { k } ^ { t }$is the smallest real number r such that the set$\{ ( n , m ) \in \mathbb { Z } ^ { 4 }$such that$F ( n , m ) \leq r \}$ contains k independent vectors.

Below, t is such that$t \sim T \in 2 ^ { \mathbb { Z } }$. We introduce dyadic scales$\beta$and$\gamma$. By definition,$M _ { 1 } ^ { t } \le \beta$ and$\begin{array} { r } { M _ { 2 } ^ { t } \le \frac { \gamma } { \beta } } \end{array}$if there exists$n , m , n ^ { \prime } , m ^ { \prime } \in \mathbb { Z } ^ { 2 }$such that

(3.3a)

$$
(n, m) \neq (0, 0) \text {   and   } (n ^ {\prime}, m ^ {\prime}) \text {   not   colinear   to   } (n, m)\tag{3.3b}
$$

$$
| n _ {1} |, | n _ {2} | \leq \beta N\tag{3.3c}
$$

$$
| n _ {1} ^ {\prime} |, | n _ {2} ^ {\prime} | \leq \frac {\gamma}{\beta} N\tag{3.3d}
$$

$$
| m | \lesssim T \beta N\tag{3.3e}
$$

$$
| m ^ {\prime} | \lesssim T \frac {\gamma}{\beta} N
$$

and furthermore

(3.4a)

$$
| t (\alpha_ {1 1} n _ {1} + \alpha_ {1 2} n _ {2}) - m _ {1} | \leq \frac {\beta}{N}\tag{3.4b}
$$

$$
| t (\alpha_ {1 2} n _ {1} + \alpha_ {2 2} n _ {2}) - m _ {2} | \leq \frac {\beta}{N}\tag{3.4c}
$$

$$
\left| t (\alpha_ {1 1} n _ {1} ^ {\prime} + \alpha_ {1 2} n _ {2} ^ {\prime}) - m _ {1} ^ {\prime} \right| \leq \frac {\gamma}{\beta N}\tag{3.4d}
$$

$$
\left| t (\alpha_ {1 2} n _ {1} ^ {\prime} + \alpha_ {2 2} n _ {2} ^ {\prime}) - m _ {2} ^ {\prime} \right| \leq \frac {\gamma}{\beta N}.
$$

We are interested in the regime where$\begin{array} { r } { \frac { 1 } { N } < \beta < \sqrt { \gamma } \ll 1 } \end{array}$(the first inequality is needed for n to be nonzero; the second one expresses the fact that$M _ { 1 } \leq M _ { 2 } ;$and the third one is related to the kernel bound we want to prove). Furthermore, there are no solutions of the above unless

$$
\beta \gtrsim \frac {1}{N T}.\tag{3.5}
$$

Indeed, if$T \beta N \ll 1$, we find$m = 0$by (3.3d), and then, by (3.4a) and (3.4b),$\begin{array} { r } { | n | \lesssim \frac { \beta } { N T } \lesssim T \beta N \ll } \end{array}$ 1. Thus$( n , m ) = 0$, which is excluded.

$E _ { \beta , \gamma , N , T } ^ { n , n ^ { \prime } } = \{ ( \alpha _ { i j } ) _ { 1 \leq i , j \leq 2 }$such that (3.1), and (3.4a) to (3.4d) hold for some m,$m ^ { \prime } \in \mathbb { Z } ^ { 2 }$and$t \sim T \}$ (notice that any$m , m ^ { \prime }$appearing in the above definition automatically satisfy (3.3d) and (3.3e) as soon as$n , n ^ { \prime }$satisfy (3.3b) and (3.3c)).

The next lemma provides an upper bound for the size of$E _ { \beta , \gamma , N , T } ^ { n , n ^ { \prime } } ;$we postpone its proof for the moment.

Lemma 3.4.(i)${ \cal I } f n \times n ^ { \prime } = 0$

$$
E _ {\beta , \gamma , N, T} ^ {n, n ^ {\prime}} = \emptyset .
$$

(ii)$I f n \times n ^ { \prime } \ne 0$, assuming that$n _ { 2 } ^ { \prime } \neq 0$2

$$
| E _ {\beta , \gamma , N, T} ^ {n, n ^ {\prime}} | \preceq \frac {\gamma^ {2} N}{| n \times n ^ {\prime} |} \left(1 + \frac {T \gamma N \operatorname* {g c d} (n _ {2} , n _ {2} ^ {\prime})}{\beta | n _ {2} ^ {\prime} |}\right) \min \left(\frac {\beta}{| n |}, \frac {\gamma}{\beta | n ^ {\prime} |}\right).
$$

Our aim is to estimate$\begin{array} { r } { \sum _ { n , n ^ { \prime } } | E _ { \beta , \gamma , N , T } ^ { n , n ^ { \prime } } | } \end{array}$. The cases where one of$n _ { 1 } , n _ { 2 } , n _ { 1 } ^ { \prime } , n _ { 2 } ^ { \prime }$is zero is easier to deal with, so we will omit them and assume below that$n _ { 1 } n _ { 2 } n _ { 1 } ^ { \prime } n _ { 2 } ^ { \prime } \neq 0$

We split this sum into two pieces: by Lemma 3.4,

$$
\begin{array}{l}\sum_{n,n^{\prime}}|E^{n,n^{\prime}}_{\beta ,\gamma ,N,T}|\\ \preceq \sum_{n\times n^{\prime}\neq 0}\frac{\gamma^{2}N}{|n\times n^{\prime}|}\left(1 + \frac{T\gamma N\gcd(n_{2},n_{2}^{\prime})}{\beta|n_{2}^{\prime}|}\right)\min \left(\frac{\beta}{|n|},\frac{\gamma}{\beta|n^{\prime}|}\right)\\ = \sum_{\substack{n\times n^{\prime}\neq 0\\ \beta |n_{2}^{\prime}| <   T\gamma N\gcd (n_{2},n_{2}^{\prime})}} + \sum_{\substack{n\times n^{\prime}\neq 0\\ \beta |n_{2}^{\prime}|\geq T\gamma N\gcd (n_{2},n_{2}^{\prime})}}\dots \\ = \Sigma_{1} + \Sigma_{2} \end{array}
$$

(the summations above are always understood under the conditions (3.3b) and (3.3c))

Bound for$\underline { { \Sigma _ { 1 } } }$It can be controlled by

$$
\gamma^ {3} T N ^ {2} \sum_ {n, n ^ {\prime}} \frac {\operatorname * {g c d} (n _ {2} , n _ {2} ^ {\prime})}{| n _ {2} ^ {\prime} | | n \times n ^ {\prime} | | n _ {1} |}.
$$

Now we have

$$
\sum_{n,n^{\prime}}\frac{\gcd(n_{2},n_{2}^{\prime})}{|n_{2}^{\prime}||n\times n^{\prime}||n_{1}|} = \sum_{\lambda}\frac{1}{\lambda}\sum_{\substack{n_{2} = \lambda \nu_{2}\\ n_{2}^{\prime} = \lambda \nu_{2}^{\prime}\\ \gcd (\nu_{2},\nu_{2}^{\prime}) = 1}}\frac{1}{|n_{1}||\nu_{2}^{\prime}||n_{1}\nu_{2}^{\prime} - n_{1}^{\prime}\nu_{2}|}\preceq 1,
$$

due to divisor bounds, which gives

$$
\Sigma_ {1} \preceq \gamma^ {3} T N ^ {2}.
$$

Bound for$\Sigma _ { 2 }$It is less than

$$
\sum_ {n, n ^ {\prime}} \frac {\gamma^ {3} N}{\beta | n \times n ^ {\prime} | | n _ {2} ^ {\prime} |}.
$$

We have

$$
\sum_ {n, n ^ {\prime}} \frac {1}{| n \times n ^ {\prime} | | n _ {2} ^ {\prime} |} = \sum_ {n _ {1}, n _ {2} ^ {\prime}} \frac {1}{| n _ {2} ^ {\prime} |} \sum_ {n _ {1} ^ {\prime}, n _ {2}} \frac {1}{| n _ {1} n _ {2} ^ {\prime} - n _ {2} n _ {1} ^ {\prime} |} \preceq \sum_ {n _ {1}, n _ {2} ^ {\prime}} \frac {1}{| n _ {2} ^ {\prime} |} \preceq \beta N.
$$

In other words,

$$
\Sigma_ {2} \preceq \gamma^ {3} N ^ {2}.
$$

We can now conclude the proof of Proposition (3.2): we just showed that

$$
\sum_ {n, n ^ {\prime}} | E _ {\beta , \gamma , N, T} ^ {n, n ^ {\prime}} | \preceq \gamma^ {3} N ^ {2} (1 + T).
$$

Since$\begin{array} { r } { \frac { 1 } { N } < \beta < 1 } \end{array}$, this implies that

$$
\sum_ {\beta} \sum_ {n, n ^ {\prime}} | E _ {\beta , \gamma , N, T} ^ {n, n ^ {\prime}} | \preceq \gamma^ {3} N ^ {2} (1 + T).
$$

We now distinguish between diferent regimes:

If$T > 1$, set$\gamma = T ^ { - 1 / 3 - \delta } N ^ { - 2 / 3 - \delta }$, for an arbitrarily small$\delta .$

If$T < 1$, set$\gamma = T ^ { - \delta } N ^ { - 2 / 3 - \delta }$, for an arbitrarily small$\delta .$

With these choices for$\gamma$(which ensure that$\gamma \ll 1 )$, we obtain

$$
\sum_ {n, n ^ {\prime}} \sum_ {\beta , N, T} | E _ {\beta , \gamma , N, T} ^ {n, n ^ {\prime}} | <   \infty .
$$

Therefore, by Borel-Cantelli, we learn that almost surely in$( \alpha _ { i j } )$，

$$
M _ {1} ^ {t} M _ {2} ^ {t} \succeq \gamma (t, N).
$$

This gives

$$
\forall t > \frac {1}{N} \text {   and   } x \in \mathbb {T} ^ {d}, \qquad | K _ {N} (t, x) | \preceq N ^ {4 / 3} \langle T \rangle^ {1 / 6}.
$$

3.3. Proof of (ii) in Proposition 3.2. Just like in the proof of (i), the first step is to appeal to Lemma 3.3 to obtain that

$$
| K _ {N} (t, x) | ^ {2} \lesssim \sum_ {n _ {1} = - 2 N} ^ {2 N} \sum_ {n _ {2} = - 2 N} ^ {2 N} \prod_ {j = 1} ^ {2} \min \left(N, \frac {1}{\| t L _ {j} (n) \|}\right).
$$

Denoting$P ( t )$for the above right-hand side

$$
P (t) = \sum_ {n _ {1}, n _ {2}} \prod_ {j = 1} ^ {2} \min \left(N, \frac {1}{\| t L _ {j} (n) \|}\right),
$$

observe that

$$
\begin{array}{l}\iint |P(t)|^{2}  d\alpha_{11}  d\alpha_{22}\lesssim \sum_{\substack{n_{1},n_{1}^{\prime}\\ n_{2},n_{2}^{\prime}}}\int \frac{1}{\|t(\alpha_{11}n_{1} + \alpha_{12}n_{2})\| + \frac{1}{N}}\frac{1}{\|t(\alpha_{11}n_{1}^{\prime} + \alpha_{12}n_{2}^{\prime})\| + \frac{1}{N}}  d\alpha_{11}\\ \\ \int \frac{1}{\|t(\alpha_{12}n_{1} + \alpha_{22}n_{2})\| + \frac{1}{N}}\frac{1}{\|t(\alpha_{12}n_{1}^{\prime} + \alpha_{22}n_{2}^{\prime})\| + \frac{1}{N}}  d\alpha_{22}\\ \\ = \sum_{\substack{n_{1},n_{1}^{\prime}\\ n_{2},n_{2}^{\prime}}}S_{1}(t)S_{2}(t). \end{array}\tag{3.6}
$$

The case when either of$n _ { 1 } , n _ { 1 } ^ { \prime } , n _ { 2 } , n _ { 2 } ^ { \prime }$is zero can be dealt with in a similar fashion to the general case; therefore, we assume in the following that none of$n _ { 1 } , n _ { 1 } ^ { \prime } , n _ { 2 } , n _ { 2 } ^ { \prime }$vanishes. Since$S _ { 1 }$and$S _ { 2 }$are symmetrical, we focuse on the former and write

$$
\left\{ \begin{array}{l l} n _ {1} = k p _ {1} \\ n _ {1} ^ {\prime} = k p _ {1} ^ {\prime} \end{array} \right. \quad \text {with} \quad \operatorname * {g c d} (p _ {1}, p _ {1} ^ {\prime}) = 1,
$$

we claim that (uniformly in$n _ { 2 } , n _ { 2 } ^ { \prime } , \alpha _ { 1 2 }$and for$t \geq 1 )$

$$
S _ {1} (t) \preceq \frac {N}{| p _ {1} | + | p _ {1} ^ {\prime} |}.\tag{3.7}
$$

Coming back to (3.6), this implies that

$$
\iint | P (t) | ^ {2} d \alpha_ {1 1} d \alpha_ {2 2} \preceq \bigg (\sum_ {p _ {1}, p _ {1} ^ {\prime}} \frac {N}{| p _ {1} | + | p _ {1} ^ {\prime} |} \sum_ {k: | k p _ {1} | \leq N, | k p _ {1} ^ {\prime} | \leq N} 1 \bigg) ^ {2} \lesssim N ^ {4} \bigg (\sum_ {p _ {1}, p _ {1} ^ {\prime}} \frac {1}{(| p _ {1} | + | p _ {1} ^ {\prime} |) ^ {2}} \bigg) ^ {2} \preceq N ^ {4},
$$

which in turn implies that

$$
\iint \int_ {1} ^ {T} \sup _ {x} | K _ {N} (t, x) | ^ {4} d t d \alpha_ {1 1} d \alpha_ {2 2} \preceq N ^ {4} T,
$$

from which the desired result follows by a Borel-Cantelli type argument.

There remains to prove (3.7). From now on,$n , n ^ { \prime } , t , \alpha _ { 1 2 }$are fixed. First decompose the arguments into integer and fractional part

$$
\left\{ \begin{array}{l l} t \alpha_ {1 1} n _ {1} + t \alpha_ {1 2} n _ {2} = \nu + \delta \\ t \alpha_ {1 1} n _ {1} ^ {\prime} + t \alpha_ {1 2} n _ {2} ^ {\prime} = \nu^ {\prime} + \delta^ {\prime} \end{array} \right. \quad \text {where} \quad \nu , \nu^ {\prime} \in \mathbb {Z} \quad \text {and} \quad - \frac {1}{2} \leq \delta , \delta^ {\prime} <   \frac {1}{2}.
$$

Furthermore, define$\epsilon , \epsilon ^ { \prime } \in 2 ^ { \mathbb { Z } } \cap \left[ { \frac { 1 } { N } } , { \frac { 1 } { 2 } } \right] { \mathrm { ~ b y ~ } } | \delta | \sim \epsilon { \mathrm { ~ i f ~ } } | \delta | > { \frac { 1 } { N } }$; and$\begin{array} { r } { \epsilon \sim \frac { 1 } { N } \mathrm { ~ i f ~ } | \delta | < \frac { 1 } { N } } \end{array}$so that

$$
S _ {1} (t) \lesssim \sum_ {n _ {1}, n _ {1} ^ {\prime}} \int \frac {1}{\epsilon \epsilon^ {\prime}} d \alpha_ {1 1}.
$$

We now argue as follows:

For$\epsilon , \epsilon ^ { \prime }$fixed,$\nu$and$\nu ^ { \prime }$satisfy

$$
| \nu p _ {1} ^ {\prime} - \nu^ {\prime} p _ {1} - C | <   \epsilon | p _ {1} ^ {\prime} | + \epsilon^ {\prime} | p _ {1} |,
$$

where$C$is a constant dedending on$n , n ^ { \prime } , \alpha _ { 1 2 }$and t. The number of$( \nu , \nu ^ { \prime } )$satisfying this constraint is

$$
\preceq t k (\epsilon | p _ {1} ^ {\prime} | + \epsilon^ {\prime} | p _ {1} | + 1).
$$

Indeed, for each fixed value of$\nu p _ { 1 } ^ { \prime } - \nu ^ { \prime } p _ { 1 } , \nu$is determined modulo$p _ { 1 }$, and it ranges in an interval of size$\sim t | n _ { 1 } |$, leaving$\begin{array} { r } { \lesssim \frac { t | n _ { 1 } | } { | p _ { 1 } | } = t k } \end{array}$possibilities. Finally, the number of possible values for$\nu p _ { 1 } ^ { \prime } - \nu ^ { \prime } p _ { 1 }$is$\lesssim \epsilon | p _ { 1 } ^ { \prime } | + \epsilon ^ { \prime } | \stackrel { \sim } { p } _ { 1 } | + 1$

Furthermore, given$\nu , \nu ^ { \prime } , \epsilon , \epsilon ^ { \prime }$, the measure of possible$\alpha _ { 1 1 }$is

$$
\lesssim \min \left(\frac {\epsilon}{t | n _ {1} |}, \frac {\epsilon^ {\prime}}{t | n _ {1} ^ {\prime} |}\right).
$$

This leads to the bound

$$
| S _ {1} (t) | \preceq \sum_ {\epsilon , \epsilon^ {\prime}} \frac {1}{\epsilon \epsilon^ {\prime}} t k (\epsilon | p _ {1} ^ {\prime} | + \epsilon^ {\prime} | p _ {1} | + 1) \min \left(\frac {\epsilon}{t | n _ {1} |}, \frac {\epsilon^ {\prime}}{t | n _ {1} ^ {\prime} |}\right) \lesssim \sum_ {\epsilon , \epsilon^ {\prime}} 1 + \frac {1}{\epsilon^ {\prime} | p _ {1} |} \preceq \frac {N}{| p _ {1} |},
$$

the bound involving$p _ { 1 } ^ { \prime }$following by symmetry.

## 3.4. Proof of Lemma 3.3. Squaring$K _ { N }$, and using that$\left( \alpha _ { i j } \right)$is symmetrical, gives

$$
| K _ {N} (t, x) | ^ {2} = \sum_ {n \in \mathbb {Z} ^ {2}} \sum_ {n ^ {\prime} \in \mathbb {Z} ^ {2}} \chi \left(\frac {n _ {1}}{N}\right) \chi \left(\frac {n _ {2}}{N}\right) \chi \left(\frac {n _ {1} ^ {\prime}}{N}\right) \chi \left(\frac {n _ {2} ^ {\prime}}{N}\right) e ^ {2 \pi i \left[ \sum x _ {i} (n _ {i} - n _ {i} ^ {\prime}) + t \sum_ {i, j} \alpha_ {i j} (n _ {i} - n _ {i} ^ {\prime}) (n _ {j} + n _ {j} ^ {\prime}) \right]}.
$$

Changing variables to$r = n - n ^ { \prime } , s = n + n ^ { \prime }$, this becomes

$$
| K _ {N} (t, x) | ^ {2} = \sum_ {r \in \mathbb {Z} ^ {2}} e ^ {2 \pi i \sum r _ {i} x _ {i}} \sum_ {s \in \mathbb {Z} ^ {2}} ^ {*} \chi \left(\frac {r _ {1} + s _ {1}}{2 N}\right) \chi \left(\frac {r _ {2} + s _ {2}}{2 N}\right) \chi \left(\frac {s _ {1} - r _ {1}}{2 N}\right) \chi \left(\frac {s _ {2} - r _ {2}}{2 N}\right) e ^ {2 \pi i t \sum_ {i, j} \alpha_ {i j} r _ {i} s _ {j}},
$$

where$\textstyle \sum _ { s } ^ { * }$means that the sum is restricted to these s such that, for all$i , s _ { i }$and$r _ { i }$have the same parity. The second sum above factors into a sum over$s _ { 1 }$times a sum over$s _ { 2 } ;$we focus on the sum over$s _ { 1 }$, which reads

$$
\sum_ {s _ {1}} ^ {*} \chi \left(\frac {r _ {1} + s _ {1}}{2 N}\right) \chi \left(\frac {s _ {1} - r _ {1}}{2 N}\right) e ^ {2 \pi i t s _ {1} \sum_ {j} \alpha_ {1 j} r _ {j}}.
$$

By Abel summation, the modulus of this sum is

$$
\dots \lesssim \min \left(N, \frac {1}{\| 2 t \sum \alpha_ {1 j} r _ {j} \|}\right).
$$

Overall, we find

$$
| K _ {N} (t, x) | ^ {2} \lesssim \sum_ {r _ {1} = - 2 N} ^ {2 N} \sum_ {r _ {2} = - 2 N} ^ {2 N} \prod_ {j = 1} ^ {2} \min \left(N, \frac {1}{\| 2 t L _ {j} (r) \|}\right),
$$

where$\begin{array} { r } { L _ { j } ( r ) = \sum \alpha _ { i j } r _ { i } } \end{array}$

3.5. Proof of Lemma 3.4. (i) The case$n \times n ^ { \prime } = 0 .$. We argue by contradiction and start by assuming that$E _ { \beta , \gamma , N , T } ^ { n , n ^ { \prime } }$is not empty. Since n and$n ^ { \prime }$are aligned, they can be written

$$
n = k p, \qquad n ^ {\prime} = k p ^ {\prime},
$$

where$k \in \mathbb { Z } ^ { 2 }$has relatively prime coordinates, and$p , p ^ { \prime } \in \mathbb { Z }$. The inequalities (3.4a) to (3.4d) become

$$
\left| t (\alpha_ {1 1} k _ {1} + \alpha_ {1 2} k _ {2}) - \frac {m _ {1}}{p} \right| \leq \frac {\beta}{N | p |}
$$

$$
\left| t (\alpha_ {1 2} k _ {1} + \alpha_ {2 2} k _ {2}) - \frac {m _ {2}}{p} \right| \leq \frac {\beta}{N | p |}
$$

$$
\left| t (\alpha_ {1 1} k _ {1} + \alpha_ {1 2} k _ {2}) - \frac {m _ {1} ^ {\prime}}{p ^ {\prime}} \right| \leq \frac {\gamma}{\beta N | p ^ {\prime} |}
$$

$$
\left| t (\alpha_ {1 2} k _ {1} + \alpha_ {2 2} k _ {2}) - \frac {m _ {2} ^ {\prime}}{p ^ {\prime}} \right| \leq \frac {\gamma}{\beta N | p ^ {\prime} |}.
$$

This implies that, on the one hand,

$$
\left| \binom{m _ {1} / p}{m _ {2} / p} - \binom{m _ {1} ^ {\prime} / p ^ {\prime}}{m _ {2} ^ {\prime} / p ^ {\prime}} \right| \lesssim \frac {\beta}{N | p |} + \frac {\gamma}{\beta N | p ^ {\prime} |}.
$$

But, on the other hand, by definition of the Minkowski minima,$( m , n )$and$( m ^ { \prime } , n ^ { \prime } )$cannot be colinear, therefore

$$
\left| \binom{m _ {1} / p}{m _ {2} / p} - \binom{m _ {1} ^ {\prime} / p ^ {\prime}}{m _ {2} ^ {\prime} / p ^ {\prime}} \right| \geq \frac {1}{| p p ^ {\prime} |}.
$$

The two above inequalities imply that

$$
1 \lesssim \frac {\beta | p ^ {\prime} |}{N} + \frac {\gamma | p |}{\beta N}.
$$

But this leads to a contradiction since

$$
\frac {\beta | p ^ {\prime} |}{N} + \frac {\gamma | p |}{\beta N} \leq \frac {\beta | n ^ {\prime} |}{N} + \frac {\gamma | n |}{\beta N} \lesssim \gamma \ll 1.
$$

(ii) The case$n \times n ^ { \prime } \ne 0 .$. In order to estimate the size of$E _ { \beta , \gamma , N , T } ^ { n , n ^ { \prime } } ,$we proceed in three steps.

First freezing t, we note that the system (3.4a) to (3.4d) is overdetermined in$\left( \alpha _ { i j } \right)$, which results in a compatibility condition on$m , m ^ { \prime }$. To derive this compatibility condition, observe that solving for$\alpha _ { 1 2 }$by (3.4a) and (3.4c) or (3.4b) and (3.4d) gives, respectively,

$$
\alpha_ {1 2} = \frac {1}{t (n \times n ^ {\prime})} (- n _ {1} ^ {\prime} m _ {1} + n _ {1} m _ {1} ^ {\prime}) + O \left(\frac {\gamma}{T | n \times n ^ {\prime} |}\right)
$$

$$
\alpha_ {1 2} = \frac {1}{t (n \times n ^ {\prime})} (n _ {2} ^ {\prime} m _ {2} - n _ {2} m _ {2} ^ {\prime}) + O \left(\frac {\gamma}{T | n \times n ^ {\prime} |}\right).
$$

Since$\gamma \ll 1$, these two equalities can only hold if

$$
- n _ {1} ^ {\prime} m _ {1} + n _ {1} m _ {1} ^ {\prime} = n _ {2} ^ {\prime} m _ {2} - n _ {2} m _ {2} ^ {\prime}.\tag{3.8}
$$

To estimate the number of m,$m ^ { \prime }$staisfying the above, note that, on the one hand, by (3.3d), (3.3e), and (3.5), the number of possible choices for$m _ { 1 }$and$m _ { 1 } ^ { \prime }$is$\lesssim \gamma ( T N ) ^ { 2 }$. On the other hand, the number of solutions$( m _ { 2 } , m _ { 2 } ^ { \prime } )$of (3.8) for$n , n ^ { \prime } , m _ { 1 } , m _ { 1 } ^ { \prime }$fixed is

$$
\lesssim 1 + \frac {T \gamma N \operatorname * {g c d} (n _ {2} , n _ {2} ^ {\prime})}{\beta | n _ {2} ^ {\prime} |}.
$$

Overall, the number of solutions of (3.8) in$( m , m ^ { \prime } )$for$( n , n ^ { \prime } )$fixed is thus

$$
\lesssim \gamma (T N) ^ {2} \left(1 + \frac {T \gamma N \operatorname* {g c d} (n _ {2} , n _ {2} ^ {\prime})}{\beta | n _ {2} ^ {\prime} |}\right).
$$

With t still frozen, and now m and$m ^ { \prime }$fixed, we use (3.4a) and (3.4c) to solve for$\alpha _ { 1 1 }$and $\alpha _ { 1 2 }$. This gives a set of measure$\sim \frac { \gamma } { N ^ { 2 } T ^ { 2 } } \frac { 1 } { | n \times n ^ { \prime } | }$. Next use (3.4b) to solve for$\alpha _ { 2 2 }$. This gives a set of measure$\sim \frac { \beta } { N T } \frac { 1 } { | n _ { 2 } | }$. Symmetrically, one could use (3.4d) to solve for α<sub>22</sub>, giving a set of measure$\sim \frac { \gamma } { \beta N T } \frac { \mathrm { i } } { | n _ { 2 } ^ { \prime } | }$. By symmetry between the first and second coordinates, we get a bound$\begin{array} { r } { \lesssim \frac { \gamma } { N ^ { 3 } T ^ { 3 } } \frac { 1 } { | n \times n ^ { \prime } | } } \end{array}$min$\begin{array} { r } { \left( \frac { \beta } { | n | } , \frac { \gamma } { \beta | n ^ { \prime } | } \right) } \end{array}$

Now observe that if t changes by an amount$\begin{array} { r } { d t \ll \frac { 1 } { N ^ { 2 } } } \end{array}$, the inequalities (3.4a) to (3.4d) need only be modified by a constant factor on the right-hand side. Since we want to cover the range$t \sim T$, it sufices to consider a number$O ( N ^ { 2 } T )$of discrete times.

Overall, we find

$$
| E _ {\beta , \gamma , N, T} ^ {n, n ^ {\prime}} | \preceq \frac {\gamma^ {2} N}{| n \times n ^ {\prime} |} \left(1 + \frac {T \gamma N \operatorname* {g c d} (n _ {2} , n _ {2} ^ {\prime})}{\beta | n _ {2} ^ {\prime} |}\right) \min \left(\frac {\beta}{| n |}, \frac {\gamma}{\beta | n ^ {\prime} |}\right).
$$

## 4. From Weyl sum estimates to Strichartz estimates

This section is dedicated to the proof of Theorem 1.1.

Step 1: decompositions of the kernel Let$\phi$be a smooth, real, non-negative function supported on $B ( 0 , 2 )$such that$\phi > 1$on$B ( 0 , 1 )$and$\widehat { \phi } \geq 0$. For a number$A \in ( 0 , \textstyle { \frac { 1 } { N } } )$to be fixed later, decompose $\begin{array} { r } { \phi \left( \frac { t } { T } \right) K _ { N } ( t , x ) } \end{array}$into

$$
\begin{array}{l} \phi \left(\frac {t}{T}\right) K _ {N} (t, x) = \underbrace {\phi \left(\frac {t}{T}\right) \chi \left(\frac {t}{A}\right) K _ {N} (t , x)} _ {J _ {1} (t, x)} + \underbrace {\phi \left(\frac {t}{T}\right) \chi (N t / 2) \left[ 1 - \chi \left(\frac {t}{A}\right) \right] K _ {N} (t , x)} _ {J _ {2} (t, x)} \\ \qquad + \underbrace {\phi \left(\frac {t}{T}\right) [ 1 - \chi (N t / 2) ] K _ {N} (t , x)} _ {J _ {3} (t, x)}. \end{array}
$$

By Lemma 3.1 and Proposition 3.2, and using the time support of$J _ { 1 }$, we find

$$
\begin{array}{l} \| \widehat {J} _ {1} \| _ {L ^ {\infty}} \lesssim A \\ \| J _ {2} \| _ {L ^ {\infty}} \lesssim \frac {1}{A} \\ \| J _ {3} \| _ {L ^ {\infty}} \preceq N ^ {4 / 3} T ^ {1 / 6}, \end{array}
$$

where the third bound holds for generic$\alpha _ { i j }$. Introducing the set

$$
S _ {\mu} = \{t \text { s.t. } t \geq 1 \text { and } \sup _ {x} K _ {N} (t, x) > \mu \},
$$

we learn from Proposition 3.2 and Chebyshev’s inequality that

$$
| S _ {\mu} | \preceq \frac {N ^ {4} T}{\mu^ {4}}.
$$

The above decomposition can be refined by letting

$$
J _ {3} = J _ {3} \mathbf {1} _ {S _ {\mu}} + J _ {3} (1 - \mathbf {1} _ {S _ {\mu}}) = J _ {3} ^ {\prime} + J _ {3} ^ {\prime \prime}.
$$

The bounds are now

$$
\| \widehat {J} _ {3} ^ {\prime} \| _ {L ^ {\infty}} \preceq \frac {N ^ {4} T}{\mu^ {4}}
$$

$$
\| J _ {3} ^ {\prime \prime} \| _ {L ^ {\infty}} \leq \mu ,
$$

provided$\mu > N ^ { 4 / 3 }$(in order to be able to estimate$\| J _ { 3 } ^ { \prime \prime } \| _ { L ^ { \infty } ( [ 0 , 1 ] \times  { \mathbb { T } } ^ { 2 } ) } )$

Step 2: level set estimates. We essentially follow the argument in Bourgain [3]. Start with$f \in$ $L ^ { 2 } (  { \mathbb { T } } ^ { 2 } )$supported in Fourier on$B ( 0 , N / 2 )$and of norm 1:$\| f \| _ { L ^ { 2 } (  { \mathbb { T } } ^ { 2 } ) } = 1$. Setting$F = e ^ { i t \widetilde { \Delta } } f$, we want to estimate the size of

$$
E _ {\lambda} = \{(x, t) \in \mathbb {T} ^ {2} \times [ 0, T ] \text {s.t.} | F (x, t) | > \lambda \}.
$$

Set$\begin{array} { r } { \widetilde { F } = \frac { F } { | F | } \mathbf { 1 } _ { E _ { \lambda } } } \end{array}$and$\begin{array} { r } { Q ( k ) = \sum _ { i j } \alpha _ { i j } k _ { i } k _ { j } } \end{array}$. We can bound, using successively Plancherel’s theorem, ethe Cauchy Schwarz inequality, and again Plancherel’s theorem,

$$
\begin{array}{r l} & {\lambda^ {2} | E _ {\lambda} | ^ {2} \lesssim \left[ \int_ {\mathbb {T} ^ {2} \times \mathbb {R}} \widetilde {F} (x, t) \overline {{F (x , t) \phi \left(\frac {t}{T}\right)}} \mathrm{d} x \mathrm{d} t \right] ^ {2}} \\ & {\quad = \left[ \sum_ {k} \int \widehat {\widetilde {F}} (\tau , k) \overline {{T \widehat {f} _ {k} \widehat {\phi} (T (\tau + Q (k)))}} \chi \left(\frac {k _ {1}}{N}\right) ^ {1 / 2} \chi \left(\frac {k _ {2}}{N}\right) ^ {1 / 2} \mathrm{d} \tau \right] ^ {2}} \\ & {\quad \leq \left[ \sum_ {k} \int_ {\mathbb {R}} \left| \widehat {\widetilde {F}} (\tau , k) \right| ^ {2} T \widehat {\phi} (T (\tau + Q (k))) \chi \left(\frac {k _ {1}}{N}\right) \chi \left(\frac {k _ {2}}{N}\right) \mathrm{d} \tau \right] \left[ \sum_ {k} | \widehat {f} _ {k} | ^ {2} \int T \widehat {\phi} (T (\tau + Q (k))) \mathrm{d} \tau \right]} \\ & {\quad \lesssim \sum_ {k} \int \left| \widehat {\widetilde {F}} (\tau , k) \right| ^ {2} T \widehat {\phi} (T (\tau + Q (k))) \chi \left(\frac {k _ {1}}{N}\right) \chi \left(\frac {k _ {2}}{N}\right) \mathrm{d} \tau} \\ & {\quad = \int \left[ (K _ {N} \phi (\frac {\cdot}{T})) * \widetilde {F} \right] (t, x) \overline {{\widetilde {F} (t , x)}} \mathrm{d} x \mathrm{d} t.} \end{array}
$$

Now using the first decomposition of Step 1,

$$
\begin{array}{l} \lambda^ {2} | E _ {\lambda} | ^ {2} \lesssim \Big \langle (J _ {1} + J _ {2} + J _ {3}) * \widetilde {F},   \widetilde {F} \Big \rangle \\ \qquad \lesssim \| \widehat {J} _ {1} \| _ {L ^ {\infty}} \| \widetilde {F} \| _ {L ^ {2}} ^ {2} + (\| J _ {2} \| _ {L ^ {\infty}} + \| J _ {3} \| _ {L ^ {\infty}})   \| \widetilde {F} \| _ {L ^ {1}} ^ {2} \\ \qquad \preceq A | E _ {\lambda} | + \left(\frac {1}{A} + N ^ {4 / 3} T ^ {1 / 6}\right) | E _ {\lambda} | ^ {2}. \end{array}
$$

Summarizing, we get if$\textstyle A < { \frac { 1 } { N } }$

$$
\lambda^ {2} | E _ {\lambda} | ^ {2} \preceq A | E _ {\lambda} | + \left(\frac {1}{A} + N ^ {4 / 3} T ^ {1 / 6}\right) | E _ {\lambda} | ^ {2}\tag{4.1}
$$

If we now resort to the refined decomposition of Step 1, we are led to

$$
\lambda^ {2} | E _ {\lambda} | ^ {2} \preceq \left(A + \frac {N ^ {4} T}{\mu^ {4}}\right) | E _ {\lambda} | + \left(\frac {1}{A} + \mu\right) | E _ {\lambda} | ^ {2}.\tag{4.2}
$$

Step 3: from level set estimates to$L ^ { p }$bounds. Recall first that$\| F \| _ { L ^ { \infty } (  { \mathbb { R } } \times  { \mathbb { T } } ^ { d } ) } \lesssim N$by the Sobolev embedding theorem. Choose next$\delta > 0$. When estimating$\left| E _ { \lambda } \right|$, three cases have to be distin guished:

If$\lambda > N ^ { 2 / 3 + \delta } T ^ { 1 / 1 2 }$, then we choose$\begin{array} { r } { A = \frac { N ^ { \delta } } { \lambda ^ { 2 } } } \end{array}$(notice that$\textstyle A < { \frac { 1 } { N } } )$. The bound (4.1) becomes then

$$
| E _ {\lambda} | \preceq N ^ {\delta} \lambda^ {- 4}.
$$

If$N ^ { 2 / 3 } < \lambda < N ^ { 2 / 3 + \delta } T ^ { 1 / 1 2 }$, then we choose$\begin{array} { r } { A = \frac { N ^ { \delta } } { \lambda ^ { 2 } } , \mu = \lambda ^ { 2 } N ^ { - \delta / 4 } } \end{array}$, and appeal to (4.2) to obtain

$$
\left| E _ {\lambda} \right| \lesssim N ^ {\delta} \left[ \lambda^ {- 4} + N ^ {4} T \lambda^ {- 1 0} \right] \lesssim N ^ {4 + \delta} T \lambda^ {- 1 0}.
$$

Finally, if$\lambda < N ^ { 2 / 3 }$, we rely on the Chebyshev inequality and the estimate$\| F \| _ { L ^ { 4 } ( [ 0 , T ] \times  { \mathbb { T } } ^ { d } ) } \lesssim$ $T ^ { 1 / 4 }$(which follows from the$L ^ { 4 }$bound of Bourgain-Demeter [9]) to obtain

$$
| E _ {\lambda} | \lesssim T \lambda^ {- 4}.
$$

All in all, this gives for$4 < p < 1 0$

$$
\begin{array}{l} \| F \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {d})} ^ {p} = p \int_ {0} ^ {N} \lambda^ {p - 1} | E _ {\lambda} |   d \lambda \\ \preceq \int_ {0} ^ {N ^ {2 / 3}} T \lambda^ {p - 5}   d \lambda + \int_ {N ^ {2 / 3}} ^ {N ^ {2 / 3 + \delta} T ^ {1 / 1 2}} N ^ {\delta} N ^ {4} T \lambda^ {p - 1 1}   d \lambda + \int_ {N ^ {2 / 3 + \delta} T ^ {1 / 1 2}} ^ {N} N ^ {\delta} \lambda^ {p - 5}   d \lambda \\ \preceq T (N ^ {2 / 3}) ^ {p - 4} + N ^ {p - 4 + \delta}, \end{array}
$$

so Theorem 1.1 is true.

## 5. The counting argument through$\ell ^ { 2 }$decoupling:$p = 1 4$

We will prove Theorem 1.2 for$p \geq 1 4$. Note that the more general case$p \geq 1 0$is proved in the next section, but the easier case here has a much simpler proof. We want to estimate

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {p}
$$

for

$$
f (y) = \sum \widehat {f} _ {k} e ^ {2 \pi i k \cdot y}.
$$

By interpolation with$p = \infty$, we may assume$p = 1 4$. By splitting into dyadic scales, and absorbing the sum over scales in the subpolynomial factor, it sufices to consider the case where

$$
f (y) = \sum \widehat {f} _ {k} {\bf 1} _ {S} (k) e ^ {2 \pi i k \cdot y},
$$

where$S \subset B ( 0 , N ) \cap \mathbb { Z } ^ { 2 }$and$\widehat { f } _ { k } \sim 1$

bOur aim is to prove the following

Theorem 5.1. With f as above, and generically in$\left( \alpha _ { i j } \right)$

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {p} \preceq (N ^ {4} + T) N ^ {p - 8} | S | ^ {\frac {p}{2}} \quad i f p = 1 4.
$$

Proof. Here and in the following, it will be convenient to denote

$$
\left( \begin{array}{c c} \alpha_ {1 1} & \alpha_ {1 2} \\ \alpha_ {1 2} & \alpha_ {2 2} \end{array} \right) = \left( \begin{array}{c c} 1 & \beta \\ \beta & \alpha \end{array} \right).
$$

We define$\Omega _ { a , b , A , B , C } ^ { p , N }$to be the set of$( k _ { i } , \ell _ { i } ) \in (  { \mathbb { Z } } ^ { 2 } ) ^ { p }$such that$| k | < N , | \ell | < N$and

$$
\sum_ {i = 1} ^ {p} (- 1) ^ {i} k _ {i} = a, \sum_ {i = 1} ^ {p} (- 1) ^ {i} \ell_ {i} = b, \sum_ {i = 1} ^ {p} (- 1) ^ {i} k _ {i} ^ {2} = A, \sum_ {i = 1} ^ {p} (- 1) ^ {i} \ell_ {i} ^ {2} = B, \sum_ {i = 1} ^ {p} (- 1) ^ {i} k _ {i} \ell_ {i} = C.\tag{5.1}
$$

The result of Bourgain and Demeter [9] implies that

$$
| S ^ {p} \cap \Omega_ {a, b, A, B, C} ^ {p, N} | \preceq N ^ {2 p - 1 0} | S | \quad \text { for } p \geq 8.
$$

This implies that

$$
| S ^ {p} \cap \Omega_ {a, b, A, B, C} ^ {p, N} | \preceq N ^ {p - 8} | S | ^ {\frac {p}{2}} \quad \text { for } p = 1 4.\tag{5.2}
$$

Indeed, observe that one can first choose$k _ { i } , \ell _ { i }$for$i = 1 , \ldots , { \frac { p } { 2 } } - 1$. There are$| S | ^ { { \frac { p } { 2 } } - 1 }$possibilities. For the remaining$\begin{array} { r } { k _ { i } , \ell _ { i } \mathrm { ~ } ( \mathrm { i e ~ } i \geq \frac { p } { 2 } } \end{array}$, we use the estimate of Bourgain-Demeter, leading to a number of solutions$O ( N ^ { p - 8 } | S | )$. Thus the total number of solutions is$O ( N ^ { p - 8 } | S | ^ { \frac { p } { 2 } } )$

We can write

$$
\begin{array}{l} \| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {p} = \sum_ {A, B, C} \sum_ {(k _ {i}, \ell_ {i}) \in \Omega_ {0, 0, A, B, C} ^ {p, N}} \widehat {f} _ {k _ {1}, \ell_ {1}} \ldots \overline {{\widehat {f} _ {k _ {p} , \ell_ {p}}}} \mathbf {1} _ {S} (k _ {1}, \ell_ {1}) \ldots \mathbf {1} _ {S} (k _ {p}, \ell_ {p}) \frac {1 - e ^ {2 \pi i T (A + B \alpha + C \beta)}}{2 \pi i (A + B \alpha + C \beta)} \\ \lesssim \sum_ {2 ^ {j} > \frac {1}{T}} \sum_ {| A + B \alpha + C \beta | \lesssim 2 ^ {j}} 2 ^ {- j} \sum_ {\Omega_ {0, 0, A, B, C} ^ {p, N}} \mathbf {1} _ {S} (k _ {1} \ell_ {1}) \ldots \mathbf {1} _ {S} (k _ {p} \ell_ {p}) \\ = \sum_ {2 ^ {j} > \frac {1}{T}} \sum_ {| A + B \alpha + C \beta | \lesssim 2 ^ {j}} 2 ^ {- j} | S ^ {p} \cap \Omega_ {0, 0, A, B, C} ^ {p, N} |. \end{array}
$$

On the one hand, we can use (5.2) to bound$| S ^ { p } \cap \Omega _ { 0 , 0 , A , B , C } ^ { p , N } |$. On the other hand, by genericity of α and$\beta _ { i }$,

$$
\sum_ {| A + B \alpha + C \beta | <   2 ^ {j}} 1 \lesssim N ^ {4} 2 ^ {j} + 1.
$$

The above can be shown for example by summing in$( A , B , C )$and integrating in$( \alpha , \beta )$the characteristic function of$| A + B \alpha + C \beta | < 2 ^ { j }$, then applying Borel-Cantelli lemma. Overall, we find

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {p} \preceq \sum_ {\frac {1}{T} <   2 ^ {j} \lesssim N ^ {2}} (N ^ {4} + 2 ^ {- j}) N ^ {p - 8} | S | ^ {p / 2} \preceq (N ^ {4} + T) N ^ {p - 8} | S | ^ {\frac {p}{2}}.
$$

## 6. The counting argument through Pall’s bound:$p = 8$

With the same ansatz for$f$as in the previous section, we are going to prove the following theorem, which implies Theorem 1.2 for$p = 8$

Theorem 6.1. Generically in$\left( \alpha _ { i j } \right)$，

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {8} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {8} \lesssim | S ^ {4} | (N ^ {4} + N T).
$$

Before starting, we first record an elementary estimate, which will be useful in the proofs below: for$a , \cdots , f \in \mathbb { R }$and$\varepsilon > 0$, we have

$$
\mathrm{meas} \left\{(x, y) \in [ 1, 2 ] ^ {2}: | a x + b y + c | <   \varepsilon \right\} \lesssim \frac {\varepsilon}{\max (| a | , | b | , | c |)},\tag{6.1}
$$

$$
\text { meas } \left\{(x, y) \in [ 1, 2 ] ^ {2}: | a x + b y + c | <   \varepsilon ,   | d x + e y + f | <   \varepsilon \right\} \lesssim \frac {\varepsilon^ {2}}{\max (| a e - b d | , | a f - c d | , | b f - c e |)}.
$$

We only prove the second inequality, since the first one is similar and easier. Let the given set be A, define the set

$$
B = \left\{(x, y, z) \in [ 1, 4 ] ^ {3}: | a x + b y + c z | <   2 \varepsilon , | d x + e y + f z | <   2 \varepsilon \right\},
$$

then by fixing one of the variables we easily deduce that

$$
\mathrm{meas} _ {\mathbb {R} ^ {3}} (B) \lesssim \frac {\varepsilon^ {2}}{\max (| a e - b d | , | a f - c d | , | b f - c e |)}.
$$

Moreover we have

$$
\mathrm{meas} _ {\mathbb {R} ^ {3}} (B) \geq \int_ {1} ^ {2} \mathrm{meas} _ {\mathbb {R} ^ {2}} (A _ {z})   \mathrm{d} z, \quad A _ {z} := \left\{(x, y) \in [ 1, 4 ] ^ {2}: | a \frac {x}{z} + b \frac {y}{z} + c | <   \frac {2 \varepsilon}{z}, | d \frac {x}{z} + e \frac {y}{z} + f | <   \frac {2 \varepsilon}{z} \right\},
$$

and that$z A \subset A _ { z } { \mathrm { ~ f o r ~ } } z \in [ 1 , 2 ]$, so a bound for meas<sub>R</sub>3 (B) implies the same bound for meas<sub>R</sub>2 (A).

6.1. Pall’s formula. Our technical tool will be a formula from a paper of Pall [27]. Let$A ^ { \prime } , B ^ { \prime } , C ^ { \prime } \in$ Z. We apply Pall’s formula (43) to the quadratic form$\phi ( x , y ) = A ^ { \prime } x ^ { 2 } + B ^ { \prime } y ^ { 2 } \stackrel { . } { + } 2 C ^ { \prime } x y$. This gives

Lemma 6.2. If$A ^ { \prime } B ^ { \prime } - C ^ { \prime 2 } > 0$, so that$\phi$is positive definite, then

$$
\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime} = C^{\prime}}}1 = 24\cdot 2^{\nu}\prod_{p|2k\Delta}\chi (p)
$$

where$k _ { i } ^ { \prime \prime } , \ell _ { i } ^ { \prime \prime } \in \mathbb { Z } , k = \operatorname* { g c d } ( A ^ { \prime } , B ^ { \prime } , C ^ { \prime } ) , \Delta = ( A ^ { \prime } B ^ { \prime } - C ^ { \prime } ) / k ^ { 2 }$, we let ν be the number of distinct odd prime factors of k∆ and$\chi$is defined in the comments after (43) and at the start of page 358 in [27].

For the reader’s convenience we repeat the definition of$\chi$in full here. Given a prime$p ,$let$p ^ { u _ { 1 } }$ be the largest power of$p$dividing k, let$p ^ { u _ { 2 } - u _ { 1 } }$be the largest power of$p$dividing$\Delta$and write $\begin{array} { r } { \delta _ { 1 } = \lfloor \frac { u _ { 1 } + \bar { 1 } } { 2 } \rfloor } \end{array}$. If$p = 2$then$\chi ( p ) = 0$or 1 according to the cases set out in Pall’s formula (44). If $p \neq 2$we let$\phi _ { 1 } = \phi / k$and adopt the convention that, if$p \mid \Delta$, then$\begin{array} { r } { \big ( \frac { \phi _ { 1 } } { p } \big ) = \big ( \frac { \phi _ { 1 } ( x , y ) } { p } \big ) } \end{array}$for any$x , y \in \mathbb { Z }$ such that$\phi _ { 1 } ( x , y )$is prime to$p .$We further define quantities$\kappa _ { 1 }$and$\kappa _ { 2 }$by

$$
\begin{array}{c c c} \kappa_ {1} & \kappa_ {2} \\ 1 & \frac {1}{2} + \frac {1}{4} \left(1 + \left(\frac {- k p ^ {- u _ {1}}}{p}\right) \left(\frac {\phi_ {1}}{p}\right)\right) (u _ {2} - u _ {1}) & \text {if u_{1} and u_{2} even}, \\ \frac {1}{2} \left(1 + \left(\frac {- k p ^ {- u _ {1}}}{p}\right) \left(\frac {\phi_ {1}}{p}\right)\right) & \frac {1}{4} \left(1 + \left(\frac {- k p ^ {- u _ {1}}}{p}\right) \left(\frac {\phi_ {1}}{p}\right)\right) (u _ {2} + 1 - u _ {1}) & \text {if u_{1} even and u_{2} odd}, \\ \frac {1}{2} \left(1 + \left(\frac {- k \Delta p ^ {- u _ {2}}}{p}\right) \left(\frac {\phi_ {1}}{p}\right)\right) & 0 & \text {if u_{1} odd and u_{2} even}, \\ \frac {1}{2} \left(1 + \left(\frac {- \Delta p ^ {u _ {1} - u _ {2}}}{p}\right)\right) & 0 & \text {if u_{1} and u_{2} odd}. \end{array}
$$

Then we can set

$$
\chi (p) = \kappa_ {1} (p ^ {\delta_ {1}} - 1) / (p - 1) + \kappa_ {2} p ^ {\delta_ {1}}.\tag{6.2}
$$

Corollary 6.3. If$A ^ { \prime } B ^ { \prime } - C ^ { \prime 2 } > 0$and$A ^ { \prime } , B ^ { \prime } , C ^ { \prime } \lesssim N ^ { 2 }$then

$$
\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime} = C^{\prime}}}1\preceq h,
$$

where$h$is the largest natural number such that$h ^ { 2 } \mid \operatorname* { g c d } ( A ^ { \prime } , B ^ { \prime } , C ^ { \prime } )$

Proof. It is immediate from (6.2) and the preceding table that for odd$p$we have

$$
\chi (p) \leq \left\{ \begin{array}{l l} 2 (u _ {2} + 1 - u _ {1}) p ^ {\delta_ {1}} & u _ {1} \text {   even }, \\ 2 p ^ {\delta_ {1} - 1} & u _ {1} \text {   odd }. \end{array} \right.
$$

Hence, where as in Lemma 6.2 we let ν be the number of distinct odd prime factors of$k \Delta$

$$
\begin{array}{l} \prod_ {p | k \Delta} \chi (p) \leq 2 ^ {\nu} \left(\prod_ {p | k \Delta} (u _ {2} + 1 - u _ {1})\right) \left(\prod_ {p | k \Delta} p ^ {\lfloor \frac {u _ {1}}{2} \rfloor}\right) \\ = 2 ^ {\nu} d (\Delta) h \end{array}
$$

on recalling the definitions of$k$and$u _ { 1 }$in Lemma 6.2 and the subsequent comments. The result follows by the divisor bound.

6.2. Preliminaries. We start with a discussion valid for any even p. Recall that

$$
\Omega_ {a, b, A, B, C} ^ {p, N} = \{(k _ {i}, \ell_ {i}) _ {i = 1, \dots , p} \in (\mathbb {Z} ^ {2}) ^ {p} \text {   such   that   } | k _ {i} | <   N, | \ell_ {i} | <   N, \sum_ {i = 1} ^ {p} (- 1) ^ {i} k _ {i} = a, \text {   etc. } \}.
$$

Define a version without the alternating signs,

$$
\Omega_ {a, b, A, B, C} ^ {q, N, +} = \{(k _ {i}, \ell_ {i}) _ {i = 1, \dots , q} \in (\mathbb {Z} ^ {2}) ^ {q} \text {   such   that   } | k _ {i} | <   N, | \ell_ {i} | <   N, \sum_ {i = 1} ^ {q} k _ {i} = a, \text {   etc. } \}.
$$

Recall that

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {p} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {p} \lesssim \sum_ {2 ^ {j} > \frac {1}{T}} \sum_ {| A + B \alpha + C \beta | \lesssim 2 ^ {j}} 2 ^ {- j} | S ^ {p} \cap \Omega_ {0, 0, A, B, C} ^ {p, N} |
$$

and observe (for$p / 2$even)

$$
\begin{array}{l}\| e^{it\widetilde{\Delta}}f\|_{L^{p}([0,T]\times \mathbb{T}^{2})}^{p}\\ \lesssim \sum_{2^{j} > \frac{1}{T}}\sum_{\substack{a,b\lesssim N\\ A_{i},B_{i},C_{i}\lesssim N^{2}\\ |(A_{1} - A_{2}) + (B_{1} - B_{2})\alpha +(C_{1} - C_{2})\beta |\lesssim 2^{j}}}2^{-j}|S^{p / 2}\cap \Omega_{a,b,A_{1},B_{1},C_{1}}^{p / 2,N, + }\big|\cdot |S^{p / 2}\cap \Omega_{a,b,A_{2},B_{2},C_{2}}^{p / 2,N, + }\big|\\ \lesssim \sum_{\frac{1}{T} <  2^{j}\lesssim N^{2}}2^{-j}|S^{p / 2}|\sup_{\substack{a,b\lesssim N\\ \tau \lesssim N^{2}}}\sum_{\substack{A_{1},B_{1},C_{1}\lesssim N^{2}\\ |A_{1} + B_{1}\alpha +C_{1}\beta -\tau | <   2^{j}}}|\Omega_{a,b,A_{1},B_{1},C_{1}}^{p / 2,N, + }\big|. \end{array}\tag{6.3}
$$

Restricting the discussion to$p = 8$from now on, we may write$k _ { i } ^ { \prime } = 4 k _ { i } - a$and$\ell _ { i } ^ { \prime } = 4 \ell _ { i } - b$to obtain

$$
\begin{array}{c} \sum_ {i = 1} ^ {4} k _ {i} = a, \sum_ {i = 1} ^ {4} \ell_ {i} = b, \sum_ {i = 1} ^ {4} k _ {i} ^ {2} = A _ {1}, \sum_ {i = 1} ^ {4} \ell_ {i} ^ {2} = B _ {1}, \sum_ {i = 1} ^ {4} k _ {i} \ell_ {i} = C _ {1} \\ \Longleftrightarrow \\ \sum_ {i = 1} ^ {4} k _ {i} ^ {\prime} = 0, \sum_ {i = 1} ^ {4} \ell_ {i} ^ {\prime} = 0, \sum_ {i = 1} ^ {4} (k _ {i} ^ {\prime}) ^ {2} = 1 6 A _ {1} - 4 a ^ {2}, \\ \sum_ {i = 1} ^ {4} (\ell_ {i} ^ {\prime}) ^ {2} = 1 6 B _ {1} - 4 b ^ {2}, \sum_ {i = 1} ^ {4} k _ {i} ^ {\prime} \ell_ {i} ^ {\prime} = 1 6 C _ {1} - 4 a b. \end{array}\tag{6.4}
$$

So, writing

$$
\begin{array}{r} k _ {1} ^ {\prime \prime} = k _ {2} ^ {\prime} + k _ {3} ^ {\prime}, k _ {2} ^ {\prime \prime} = k _ {1} ^ {\prime} + k _ {3} ^ {\prime}, k _ {3} ^ {\prime \prime} = k _ {1} ^ {\prime} + k _ {2} ^ {\prime}, \\ \ell_ {1} ^ {\prime \prime} = \ell_ {2} ^ {\prime} + \ell_ {3} ^ {\prime}, \ell_ {2} ^ {\prime \prime} = \ell_ {1} ^ {\prime} + \ell_ {3} ^ {\prime}, \ell_ {3} ^ {\prime \prime} = \ell_ {1} ^ {\prime} + \ell_ {2} ^ {\prime}, \\ A ^ {\prime} = 1 6 A _ {1} - 4 a ^ {2}, B ^ {\prime} = 1 6 B _ {1} - 4 b ^ {2}, C ^ {\prime} = 1 6 C _ {1} - 4 a b, \end{array}\tag{6.5}
$$

we get an injection

$$
\Omega_ {a, b, A _ {1}, B _ {1}, C _ {1}} ^ {4, N, +} \hookrightarrow \{(k _ {i} ^ {\prime \prime}, \ell_ {i} ^ {\prime \prime}) _ {i = 1, 2, 3}: \sum_ {i = 1} ^ {3} (k _ {i} ^ {\prime \prime}) ^ {2} = A ^ {\prime}, \sum_ {i = 1} ^ {3} (\ell_ {i} ^ {\prime \prime}) ^ {2} = B ^ {\prime}, \sum_ {i = 1} ^ {3} k _ {i} ^ {\prime \prime} \ell_ {i} ^ {\prime \prime} = C ^ {\prime}. \}\tag{6.6}
$$

In particular, we may conclude from (6.3) that

$$
\begin{array}{l}\| e^{it\widetilde{\Delta}}f\|_{L^{8}([0,T]\times \mathbb{T}^{2})}^{8}\lesssim \sum_{\frac{1}{T} <  2^{j}\lesssim N^{2}}2^{-j}|S^{4}|\sup_{\tau^{\prime}\lesssim N^{2}}\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}}}\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime} = C^{\prime}}}1\\ \\ \succeq \sum_{\frac{1}{T} <  2^{j}\lesssim N^{2}}2^{-j}|S^{4}|\sup_{\tau^{\prime}\lesssim N^{2}}\left((1 + 2^{j})N + \sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}\\ A^{\prime}B^{\prime}\neq 0}}\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime}  = C^{\prime}}}1\right) \end{array}\tag{6.7}
$$

by separating out the terms where$k ^ { \prime \prime } = 0 \mathrm { o r } \ell ^ { \prime \prime } = 0$

6.3. The case$A ^ { \prime } B ^ { \prime } = ( C ^ { \prime } ) ^ { 2 }$. The innermost sum in (6.7) is largest for values of$A ^ { \prime } , B ^ { \prime } , C ^ { \prime }$for which $A ^ { \prime } B ^ { \prime } = ( C ^ { \prime } ) ^ { 2 }$. We will need to deal with these degenerate terms separately.$\begin{array} { r l r } { \mathrm { { I f } } \sum _ { i = 1 } ^ { 3 } ( k _ { i } ^ { \prime \prime } ) ^ { 2 } \sum _ { i = 1 } ^ { 3 } ( \ell _ { i } ^ { \prime \prime } ) ^ { 2 } = } & { { } } & { } \end{array}$ $\begin{array} { r } { ( \sum _ { i = 1 } ^ { 3 } k _ { i } ^ { \prime \prime } \ell _ { i } ^ { \prime \prime } ) ^ { 2 } \neq 0 } \end{array}$then we must have

$$
k _ {i} ^ {\prime \prime} = p z _ {i}, \ell_ {i} ^ {\prime \prime} = q z _ {i}
$$

for some unique$z _ { i } , p , q$with$p , q > 0$and$\operatorname* { g c d } ( p , q ) = 1$. Thus

$$
\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}\\ A^{\prime}B^{\prime}\neq 0\\ A^{\prime}B^{\prime} = (C^{\prime})^{2}}}\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime} = C^{\prime}}}1\leq \sum_{\substack{p,q,m\in \mathbb{N}\\ \gcd (p,q) = 1\\ p,q\lesssim N / \sqrt{m}\\ |(p^{2} + q^{2}\alpha +pq\beta)m - \tau^{\prime}| <   2^{j}}}\sum_{\substack{z_{i}\\ z_{1}^{2} + z_{2}^{2} + z_{3}^{2} = m}}1\\ \preceq \sum_{\substack{p,q,m\in \mathbb{N}\\ \gcd (p,q) = 1\\ mp^{2},mq^{2}\lesssim N^{2}\\ |(p^{2} + q^{2}\alpha +pq\beta)m - \tau^{\prime}| <   2^{j}}}\sqrt{m}.\tag{6.8}
$$

To finish this case, it is enough to involve the genericity of$\alpha , \beta$as follows:

Lemma 6.4. For almost all$\alpha , \beta$and all$m , m ^ { \prime } , p , p ^ { \prime } , q , q ^ { \prime }$satisying$( m p ^ { 2 } , m q ^ { 2 } ) \neq ( m ^ { \prime } ( p ^ { \prime } ) ^ { 2 } , m ^ { \prime } ( q ^ { \prime } ) ^ { 2 } )$ and$m p ^ { 2 } , m q ^ { 2 } , m ^ { \prime } ( p ^ { \prime } ) ^ { 2 } , m ^ { \prime } ( q ^ { \prime } ) ^ { 2 } \leq N ^ { 2 }$we have

$$
\left| m \left(p ^ {2} + q ^ {2} \alpha + p q \beta\right) - m ^ {\prime} \left(\left(p ^ {\prime}\right) ^ {2} + \left(q ^ {\prime}\right) ^ {2} \alpha + p ^ {\prime} q ^ {\prime} \beta\right) \right| \succeq_ {\alpha , \beta} N ^ {- 2}.
$$

Proof. Fix$\tau > 0$. Denoting$E _ { m , p , q , m ^ { \prime } , p ^ { \prime } , q ^ { \prime } } = \{ ( \alpha , \beta )$such that$| m ( p ^ { 2 } + \alpha q ^ { 2 } + p q \beta ) - m ^ { \prime } ( ( p ^ { \prime } ) ^ { 2 } +$ $\alpha ( q ^ { \prime } ) ^ { 2 } + \beta p ^ { \prime } q ^ { \prime } ) | < N ^ { - 2 - \tau } \}$, we get, by applying (6.1), that

$$
\left| E _ {m, p, q, m ^ {\prime}, p ^ {\prime}, q ^ {\prime}} \right| \leq N ^ {- 2 - \tau} \min \left(\frac {1}{m q ^ {2} - m ^ {\prime} (q ^ {\prime}) ^ {2}}, \frac {1}{m p ^ {2} - m ^ {\prime} (p ^ {\prime}) ^ {2}}\right).
$$

Now we will calculate

$$
\sum_{m,p,q,m^{\prime},p^{\prime},q^{\prime}}|E_{m,p,q,m^{\prime},p^{\prime},q^{\prime}}|\sim N^{-2 - \tau}\sum_{1\leq d\lesssim N^{2}}\frac{1}{d}\sum_{\substack{(m,p,q,m^{\prime},p^{\prime},q^{\prime}):\\ |mq^{2} - m^{\prime}(q^{\prime})^{2}| = d\\ |mp^{2} - m^{\prime}(p^{\prime})^{2}|\leq d}}1.
$$

For fixed$C ,$when$( m , m ^ { \prime } , q , q ^ { \prime } )$is also fixed, we have$1 \le p \lesssim N / \sqrt { m }$, and for each$p ,$we have

$$
\frac {\sqrt {\max (m p ^ {2} - d , 0)}}{\sqrt {m ^ {\prime}}} \leq p ^ {\prime} \leq \frac {\sqrt {m p ^ {2} + d}}{\sqrt {m ^ {\prime}}},
$$

so the number of choices for$p ^ { \prime }$is at most

$$
1 + \frac {\sqrt {m p ^ {2} + d} - \sqrt {\max (m p ^ {2} - d , 0)}}{\sqrt {m ^ {\prime}}} \sim 1 + \frac {d}{\sqrt {m ^ {\prime} (m p ^ {2} + d)}}.
$$

Therefore, for fixed$( m , m ^ { \prime } , q , q ^ { \prime } )$we have

$$
\sum_ {(p, p ^ {\prime}): | m p ^ {2} - m ^ {\prime} (p ^ {\prime}) ^ {2} | \leq d} 1 \lesssim \sum_ {p \lesssim N / \sqrt {m}} \left(1 + \frac {d}{\sqrt {m ^ {\prime} (m p ^ {2} + d)}}\right) \preceq \frac {N}{\sqrt {m}} + \frac {d}{\sqrt {m m ^ {\prime}}}.
$$

Now by definition of$d ,$we have

$$
\sum_{1\leq d\lesssim N^{2}}\frac{1}{d}\sum_{\substack{(m,m^{\prime},q,q^{\prime}):\\ |mq^{2} - m^{\prime}(q^{\prime})^{2}| = d}}\frac{d}{\sqrt{mm^{\prime}}}\lesssim \sum_{\substack{1\leq m,m^{\prime}\lesssim N^{2}\\ 1\leq q\lesssim N / \sqrt{m},1\leq q^{\prime}\lesssim N / \sqrt{m^{\prime}}}}\frac{1}{\sqrt{mm^{\prime}}}\lesssim \sum_{1\leq m,m^{\prime}\lesssim N^{2}}\frac{1}{\sqrt{mm^{\prime}}}\frac{N^{2}}{\sqrt{mm^{\prime}}} \preceq N^{2}.
$$

Moreover, when m is fixed there are at most$N / \sqrt { m }$choices for$q ,$and when$( m , q )$is fixed, there are most$O ( N ^ { \varepsilon } )$choices for$( m ^ { \prime } , q ^ { \prime } )$such that$| \dot { m } \dot { q } ^ { 2 } - m ^ { \prime } ( q ^ { \prime } ) ^ { 2 } | = \bar { d }$due to divisor estimates, so

$$
\sum_{1\leq d\lesssim N^{2}}\frac{1}{d}\sum_{\substack{(m,m^{\prime},q,q^{\prime}):\\ |mq^{2} - m^{\prime}(q^{\prime})^{2}| = d}}\frac{N}{\sqrt{m}} \preceq \sum_{1\leq d\lesssim N^{2}}\frac{1}{d}\sum_{1\leq m\lesssim N^{2}}\frac{N}{\sqrt{m}} \frac{N}{\sqrt{m}} \preceq N^{2}.
$$

This implies that

$$
\sum_ {m, p, q, m ^ {\prime}, p ^ {\prime}, q ^ {\prime}} | E _ {m, p, q, m ^ {\prime}, p ^ {\prime}, q ^ {\prime}} | <   \infty ,
$$

so the lemma of Borel-Cantelli then gives the result. Namely, almost all$( \alpha , \beta )$belongs to only finitely many$E _ { m , p , q , m ^ { \prime } , p ^ { \prime } , q ^ { \prime } ; \ l }$, so the desired inequality holds with some constant depending on$( \alpha , \beta )$ by treating the finitely many sets individually.

By (6.8) and the Lemma we get

$$
\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}\\ A^{\prime}B^{\prime}\neq 0\\ A^{\prime}B^{\prime} = (C^{\prime})^{2}}}\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime} = C^{\prime}}}1\preceq (2^{j}N^{2} + 1)N\tag{6.9}
$$

which is enough for us.

6.4. The case$A ^ { \prime } B ^ { \prime } \ne ( C ^ { \prime } ) ^ { 2 }$, main argument. Recall the bound from Corollary 6.3 above. Setting$h = h ( A ^ { \prime } , B ^ { \prime } , \dot { C ^ { \prime } } ) , \dot { U } = h ^ { - 2 } A ^ { \prime } , V = \bar { h } ^ { - 2 } B ^ { \prime }$, and$W = h ^ { - 2 } C ^ { \prime }$we deduce from it that

$$
\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}\\ A^{\prime}B^{\prime}\neq (C^{\prime})^{2}}}\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime} = C^{\prime}}}1\preceq \sum_{h\lesssim N}\sum_{\substack{U,V,W\lesssim N^{2} / h^{2}\\ |U + V\alpha +W\beta -\tau^{\prime} / h^{2}| <   2^{j} / h^{2}\\ UV - W^{2} > 0}}h.\tag{6.10}
$$

Observe that since$| U + V \alpha + W \beta | \succeq _ { \alpha , \beta } h ^ { 4 } / N ^ { 4 }$for all$U , V , W \lesssim N ^ { 2 } / h ^ { 2 }$not all zero (by integrating in α and$\beta$exploiting genericity, in the same way as in the proof of Theorem 5.1), the sum over those$h \leq N ^ { 1 / 2 }$satisfies

$$
\sum_{h\leq N^{1 / 2}}\sum_{\substack{U,V,W\lesssim N^{2} / h^{2}\\ |U + V\alpha +W\beta -\tau^{\prime} / h^{2}| <   2^{j} / h^{2}\\ UV - W^{2} > 0}}h\preceq \sum_{h\lesssim N^{1 / 2}}(2^{j}N^{4} / h^{6} + 1)h\lesssim 2^{j}N^{4} + N.
$$

This is satisfactory, and it remains to treat$N ^ { 1 / 2 } \leq h \lesssim N$. Our proof does not use the full strength of the condition$U V - W ^ { 2 } > 0$but only the weaker$( U , V , W ) \neq ( 0 , 0 , 0 )$; this should heuristically make no diference in the size of the sum and we do not know any way to take advantage of the full condition$U V - W ^ { 2 } > 0$. The result which is required is then the following.

Lemma 6.5. Let

$$
\Phi (\alpha ,\beta ,\tau^{\prime}) = \sum_{h\sim K}\sum_{\substack{U,V,W\lesssim N^{2} / h^{2}\\ |U + V\alpha +W\beta -\tau^{\prime} / h^{2}| <   2^{j} / h^{2}\\ (U,V,W)\neq (0,0,0)}}1
$$

For almost all$\alpha , \beta$and any$\tau ^ { \prime } \in \mathbb { R } , j \in \mathbb { Z } , K \in [ N ^ { 1 / 2 } , N ]$we have

$$
\Phi (\alpha , \beta , \tau^ {\prime}) \preceq_ {\alpha , \beta} 2 ^ {j} N ^ {4} / K + N / K.
$$

Combining this lemma with the previous two bounds will show that for generic$\alpha , \beta$we have

$$
\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}\\ A^{\prime}B^{\prime}\neq (C^{\prime})^{2}}}\sum_{\substack{\sum_{i = 1}^{3}(k_{i}^{\prime \prime})^{2} = A^{\prime},\\ \sum_{i = 1}^{3}(\ell_{i}^{\prime \prime})^{2} = B^{\prime},\\ \sum_{i = 1}^{3}k_{i}^{\prime \prime}\ell_{i}^{\prime \prime} = C^{\prime}}}1\preceq_{\alpha ,\beta}2^{j}N^{4} + N.\tag{6.11}
$$

To motivate the proof of the lemma, we sketch some attacks on the problem based on the proof of (6.9). Imitating Lemma 6.4, one might try to show that for generic$( \alpha , \beta )$, all$h , h ^ { \prime } \sim K$ $U , \dot { U ^ { \prime } } , \dot { V } , V ^ { \prime } , W , W ^ { \prime } \stackrel { - } { \sim } N ^ { 2 } / h ^ { 2 }$, and some appropriate$\rho$we have

$$
\left| h ^ {2} (U + V \alpha + W \beta) - h ^ {\prime 2} (U ^ {\prime} + V ^ {\prime} \alpha + W ^ {\prime} \beta) \right| \gtrsim_ {\alpha , \beta} \rho\tag{6.12}
$$

whenever the left-hand side is nonzero. It would follow that the number of values of$h ^ { 2 } ( U + V \alpha + W \beta )$ such that$\left| h ^ { 2 } ( U + V \alpha + W \beta ) - \tau ^ { \prime } \right| < 2 ^ { j }$is at most$\preceq _ { \alpha , \beta } 2 ^ { j } / \rho$. Taking an optimistic view, we might get a bound$\preceq _ { \alpha , \beta } 2 ^ { j } K / \rho$for the sum in Lemma 6.5.

What value of$\rho$might be possible? The left-hand side of (6.12) is of the form$G + H \alpha + J \beta$for integers$G , H , J \lesssim N ^ { 2 }$. It is elementary that if$K \sim N ^ { 1 / 2 }$, any triple of integers$G , H , J \lesssim _ { \epsilon } N ^ { 2 - \epsilon }$ will occur for some$h , h ^ { \prime } , U , U ^ { \prime }$, etc. So if$K \sim N ^ { 1 / 2 }$then there are$h , h ^ { \prime } , U , U ^ { \prime }$, etc. with

$$
\left| h ^ {2} (U + V \alpha + W \beta) - h ^ {\prime 2} (U ^ {\prime} + V ^ {\prime} \alpha + W ^ {\prime} \beta) \right| \lesssim_ {\epsilon} N ^ {- 4 + \epsilon}.
$$

Thus$\rho \lesssim _ { \epsilon } N ^ { - 4 + \epsilon }$in this case. The optimistic bound$2 ^ { j } K / \rho$for the sum in Lemma 6.5 is then of size at least$\gtrsim _ { \epsilon } 2 ^ { j } K N ^ { 4 - \epsilon }$. But this is bigger than the bound in (6.11) by a factor of$K N ^ { - \epsilon }$

We can try to refine the argument: rather than prove$\left| h ^ { 2 } ( U + V \alpha + W \beta ) - h ^ { \prime 2 } ( U ^ { \prime } + V ^ { \prime } \alpha + W ^ { \prime } \beta ) \right| <$ $\rho$has no solutions, we can seek a bound for the number of solutions. More precisely, let

$$
\Sigma (\alpha ,\beta ,\tau^{\prime}) = \sum_{h,h^{\prime}\sim K}\sum_{\substack{|U + V\alpha +W\beta -\tau^{\prime} / h^{2}| <   2^{j} / h^{2}\\ |U^{\prime} + V^{\prime}\alpha +W^{\prime}\beta -\tau^{\prime} / h^{\prime 2}| <   2^{j} / h^{\prime 2}\\ h^{2}(U,V,W)\neq h^{\prime 2}(U^{\prime},V^{\prime},W^{\prime})}}1
$$

and write

$$
\bigg(\sum_{h\sim K}\sum_{\substack{U,V,W\lesssim N^{2} / h^{2}\\ |U + V\alpha +W\beta -\tau^{\prime} / h^{2}| <   2^{j} / h^{2}}}h\bigg)^{2}\lesssim K^{2}\Sigma (\alpha ,\beta ,\tau^{\prime}) + \sum_{h,h^{\prime}\sim K}\sum_{\substack{|U + V\alpha +W\beta -\tau^{\prime} / h^{2}| <   2^{j} / h^{2}\\ |U^{\prime} + V^{\prime}\alpha +W^{\prime}\beta -\tau^{\prime} / h^{\prime 2}| <   2^{j} / h^{\prime 2}\\ h^{2}(U,V,W) = h^{\prime 2}(U^{\prime},V^{\prime},W^{\prime})}}hh^{\prime}.\tag{6.13}
$$

The second term captures the diagonal contribution from$h ^ { 2 } ( U , V , W ) = h ^ { \prime 2 } ( U ^ { \prime } , V ^ { \prime } , W ^ { \prime } )$, which would otherwise cause problems later; we might hope that this term is negligible. We would then need to bound$\Sigma ( \alpha , \beta , \tau ^ { \prime } )$for almost all$\alpha , \beta ,$uniformly in$\tau ^ { \prime }$. We can eliminate$\tau ^ { \prime }$using the same idea as Lemma 6.4: we observe that$\Sigma ( \alpha , \beta , \tau ^ { \prime } ) \leq \Sigma ^ { \prime } ( \alpha , \beta )$, where we set

$$
\Sigma^{\prime}(\alpha ,\beta) = \sum_{h,h^{\prime}\sim K}\sum_{\substack{\left|h^{2}(U + V\alpha +W\beta) - h^{\prime 2}(U^{\prime} + V^{\prime}\alpha +W^{\prime}\beta)\right| <   2^{j}\\ h^{2}(U,V,W)\neq h^{\prime 2}(U^{\prime},V^{\prime},W^{\prime})}}1.
$$

Using the Borel-Cantelli lemma we find that for generic$\alpha , \beta$we have

$$
\begin{array}{c} \Sigma^ {\prime} (\alpha , \beta) \preceq_ {\alpha , \beta} \int \Sigma^ {\prime} (\alpha^ {\prime}, \beta^ {\prime})   d \alpha^ {\prime} d \beta^ {\prime} = \sum_ {h, h ^ {\prime} \sim K} \sum_ {h ^ {2} (U, V, W) \neq h ^ {\prime 2} (U ^ {\prime}, V ^ {\prime}, W ^ {\prime})} \\ \text {measure} \big \{(\alpha^ {\prime}, \beta^ {\prime}): \big | h ^ {2} (U + V \alpha^ {\prime} + W \beta^ {\prime}) - h ^ {\prime 2} (U ^ {\prime} + V ^ {\prime} \alpha^ {\prime} + W ^ {\prime} \beta^ {\prime}) \big | <   2 ^ {j} \big \}. \end{array}
$$

The condition$h ^ { 2 } ( U , V , W ) \neq h ^ { \prime 2 } ( U ^ { \prime } , V ^ { \prime } , W ^ { \prime } )$removes the terms for which the measure above is largest, which could otherwise have dominated the sum. But even for typical$h , h ^ { \prime } , U , U ^ { \prime } , . . .$. this measure will have size$\gtrsim 2 ^ { j } / N ^ { 2 }$. Consquently the best upper bound for$\Sigma ^ { \prime } ( \alpha , \beta )$which we could hope to prove is

$$
\Sigma^ {\prime} (\alpha , \beta) \preceq_ {\alpha , \beta} 2 ^ {j} N ^ {1 2} / K ^ {1 0}.
$$

Via (6.13) this would lead to a bound of at best$2 ^ { j / 2 } N ^ { 6 } / K ^ { 4 }$for the sum in Lemma 6.5, which is not suficient. For example when$K = N ^ { 1 / 2 }$and$2 ^ { j } = N ^ { - 3 }$that bound is at least$N ^ { 5 / 2 }$, while (6.11) requires a bound of$\lesssim _ { \alpha , \epsilon } N ^ { 1 + \epsilon }$

The proof we give of Lemma 6.5 is nonetheless very close to the sketch above. Instead of the square in (6.13) we will take the cube of the sum we hope to bound. We will split of a kind of “diagonal contribution”, and the remaining term will be estimated by eliminating$\tau ^ { \prime }$and applying the Borel-Cantelli lemma.

Proof of Lemma 6.5. We may assume$2 ^ { j } \geq N ^ { - 3 }$, since otherwise the term$N / K$on the right hand side dominates so the case can be treated as if$2 ^ { j } \sim N ^ { - 3 }$. We take the cube:

$$
\Phi (\alpha ,\beta ,\tau^{\prime})^{3} = \sum_{h_{0},h_{1},h_{2}\sim K}\sum_{\substack{U_{i},V_{i},W_{i}\lesssim N^{2} / K^{2} (i = 0,1,2)\\ |U_{i} + V_{i}\alpha +W_{i}\beta -\tau^{\prime} / h_{i}^{2}| <   2^{j} / h_{i}^{2} (i = 0,1,2)\\ (U_{i},V_{i},W_{i})\neq (0,0,0) (i = 0,1,2)}}1.
$$

We split the terms according to whether the$h _ { i } ^ { 2 } ( U _ { i } , V _ { i } , W _ { i } )$lie on a line through the origin, or else on a line which is not through the origin, or neither. Write for the vector product of two column vectors. Observe that the$h _ { i } ^ { 2 } ( U _ { i } , V _ { i } , \bar { W _ { i } } )$are collinear if the quantity

$$
\Delta = \left(h _ {2} ^ {2} (U _ {2}, V _ {2}, W _ {2}) - h _ {0} ^ {2} (U _ {0}, V _ {0}, W _ {0})\right) ^ {T} \times \left(h _ {1} ^ {2} (U _ {1}, V _ {1}, W _ {1}) - h _ {0} ^ {2} (U _ {0}, V _ {0}, W _ {0})\right) ^ {T}\tag{6.14}
$$

vanishes. So the promised splitting of the sum is

$$
\begin{array}{l}\Phi (\alpha ,\beta ,\tau^{\prime})^{3}\lesssim \sum_{h_{0},h_{1},h_{2}\sim K}\sum_{\substack{U_{i},V_{i},W_{i}\lesssim N^{2} / K^{2} (i = 0,1,2)\\ \left|h_{i}^{2}(U_{i} + V_{i}\alpha +W_{i}\beta) - \tau^{\prime}\right| <   2^{j} (i = 0,1,2)\\ h_{i}^{2}(U_{i},V_{i},W_{i}) = \lambda_{i}(U_{0},V_{0},W_{0}) (\lambda_{i}\in \mathbb{Q})\\ (U_{0},V_{0},W_{0})\neq (0,0,0)}}1\\ \\ +\sum_{h_{0},h_{1},h_{2}\sim K}\sum_{\substack{U_{i},V_{i},W_{i}\lesssim N^{2} / K^{2} (i = 0,1,2)\\ \left|h_{i}^{2}(U_{i} + V_{i}\alpha +W_{i}\beta) - \tau^{\prime}\right| <   2^{j}(i = 0,1,2)\\ (U_{0},V_{0},W_{0})^{T}\times (U_{1},V_{1},W_{1})^{T}\neq 0\\ \Delta = 0}}1\\ \\ +\sum_{h_{0},h_{1},h_{2}\sim K}\sum_{\substack{U_{i},V_{i},W_{i}\lesssim N^{2} / K^{2} (i = 0,1,2)\\ \left|h_{i}^{2}(U_{i} + V_{i}\alpha +W_{i}\beta) - \tau^{\prime}\right| <    2^{j} (i = 0,1,2)\\ \Delta \neq 0}}1. \end{array}\tag{6.15}
$$

The first term on the right-hand side includes the diagonal contribution, when the$h _ { i } ^ { 2 } ( U _ { i } , V _ { i } , W _ { i } )$ are all equal. Letting$( \hat { U } _ { 0 } , \hat { V } _ { 0 } , \hat { W } _ { 0 } ) = ( U _ { 0 } , V _ { 0 } , W _ { 0 } ) / \operatorname* { g c d } ( U _ { 0 } , V _ { 0 } , W _ { 0 } )$, this first term is bounded by

$$
\begin{array}{l}\sum_{h_{0}\sim K}\sum_{\substack{U_{0},V_{0},W_{0}\lesssim N^{2} / K^{2}\\ \left|h_{0}^{2}(U_{0} + V_{0}\alpha +W_{0}\beta) - \tau^{\prime}\right| <   2^{j}\\ (U_{0},V_{0},W_{0})\neq (0,0,0)}}\left(\sum_{\substack{|y(\hat{U}_{0} + \hat{V}_{0}\alpha +\hat{W}_{0}\beta) - \tau^{\prime}| <   2^{j}\\ (y\in \mathbb{Z})}}1\right)^{2}\\ \leq \sum_{h_{0}\sim K}\sum_{\substack{U_{0},V_{0},W_{0}\lesssim N^{2} / K^{2}\\ \left|h_{0}^{2}(U_{0} + V_{0}\alpha +W_{0}\beta) - \tau^{\prime}\right| <   2^{j}\\ (U_{0},V_{0},W_{0})\neq (0.0,0)}}\left(\frac{2^{j + 1}}{|\hat{U}_{0} + \hat{V}_{0}\alpha + \hat{W}_{0}\beta |}\right)^{2} + 1. \end{array}
$$

For generic$\alpha , \beta$we have$| \hat { U } _ { 0 } + \hat { V } _ { 0 } \alpha + \hat { W } _ { 0 } \beta | \stackrel { } { \underset { } { et { } { ^ { - } } } } \alpha , \beta \stackrel { } { K ^ { 4 } } / N ^ { 4 }$and so the sum on the last line is

$$
\preceq_ {\alpha , \beta} \left(\frac {2 ^ {2 j} N ^ {8}}{K ^ {8}} + 1\right) \Phi (\alpha , \beta , \tau^ {\prime}).\tag{6.16}
$$

This will sufice for the first term. A variation of the same argument produces the following lemma, which is enough to treat the second term in (6.15).

Lemma 6.6. For generic$\alpha , \beta , 2 ^ { j } \geq N ^ { - 3 }$and$\tau ^ { \prime } \in \mathbb { R } , K \in [ N ^ { 1 / 2 } , N ]$and$m , c \in \mathbb { Z } ^ { 3 }$with$| m | , | c | \lesssim$ $N ^ { 2 } , \operatorname* { g c d } ( m _ { 1 } , m _ { 2 } , m _ { 3 } ) = 1$and$m ^ { T } \times c ^ { T } \neq 0$, we have

$$
\sum_{h_{2}\sim K}\sum_{\substack{U_{2},V_{2},W_{2}\lesssim N^{2} / K^{2}\\ \left|h_{2}^{2}(U_{2} + V_{2}\alpha +W_{2}\beta) - \tau^{\prime}\right| <   2^{j}\\ h_{2}^{2}(U_{2},V_{2},W_{2}) = mx + c (x\in \mathbb{Z})}}1\preceq_{\alpha ,\beta}\frac{2^{j}N^{4}}{K^{2}} +1.
$$

We also need a lemma to treat the third term in (6.15); this will be proved in the next section using a Borel-Cantelli argument.

Lemma 6.7. Define

$$
\Sigma_{0}(\alpha ,\beta) = \sum_{h_{0},h_{1},h_{2}\sim K}\sum_{\substack{U_{i},V_{i},W_{i}\lesssim N^{2} / K^{2} (i = 0,1,2)\\ \left|h_{i}^{2}(U_{i} + V_{i}\alpha +W_{i}\beta) - h_{0}^{2}(U_{0} + V_{0}\alpha +W_{0}\beta)\right| <   2^{j} (i = 1,2)\\ \Delta \neq 0}}1.
$$

For generic$\alpha , \beta , 2 ^ { j } \geq N ^ { - 3 }$and$K \in [ N ^ { 1 / 2 } , N ]$we have

$$
\Sigma_ {0} (\alpha , \beta) \preceq_ {\alpha , \beta} 1 + \frac {2 ^ {3 j} N ^ {1 2}}{K ^ {3}}.
$$

Inserting (6.16) and the two lemmas into (6.15) gives

$$
\Phi (\alpha , \beta , \tau^ {\prime}) ^ {3} \preceq \left(\frac {2 ^ {2 j} N ^ {8}}{K ^ {8}} + 1\right) \Phi (\alpha , \beta , \tau^ {\prime}) + \left(\frac {2 ^ {j} N ^ {4}}{K ^ {2}} + 1\right) \Phi (\alpha , \beta , \tau^ {\prime}) ^ {2} + 1 + \frac {2 ^ {3 j} N ^ {1 2}}{K ^ {3}},
$$

from which we obtain

$$
\Phi (\alpha , \beta , \tau^ {\prime}) \preceq_ {\alpha , \beta} \frac {2 ^ {j} N ^ {4}}{K ^ {4}} + \frac {2 ^ {j} N ^ {4}}{K ^ {2}} + 1 + \frac {2 ^ {j} N ^ {4}}{K}.
$$

This proves the lemma.

## 6.5. The case$A ^ { \prime } B ^ { \prime } \ne ( C ^ { \prime } ) ^ { 2 }$, auxiliary lemmas.

Proof of Lemma 6.6. Suppose mx$+ c \equiv 0$(mod$h _ { 2 } ^ { 2 } )$. From this we draw two conclusions. First,

$$
\operatorname * {g c d} (x, h _ {2} ^ {2}) \mid \operatorname * {g c d} (c _ {1}, c _ {2}, c _ {3}).
$$

Second,$\begin{array} { r } { m x \times \left( \frac { c } { \operatorname* { g c d } ( x , h _ { 2 } ^ { 2 } ) } \right) \equiv 0 } \end{array}$mod$h _ { 2 } ^ { 2 }$and so

$$
\frac {m \times c}{\operatorname* {g c d} (x , h _ {2} ^ {2})} \equiv 0 \mod \frac {h _ {2} ^ {2}}{\operatorname* {g c d} (x , h _ {2} ^ {2})}.
$$

From these and the fact that$| m | , | c | \lesssim N ^ { 2 }$and$m ^ { T } \times c ^ { T } \neq 0$, we find that$\operatorname* { g c d } ( x , h _ { 2 } ^ { 2 } )$and$h _ { 2 } ^ { 2 }$are determined up$\mathrm { t o } \preceq 1$possibilities by m and c. Thus the sum in the lemma is

$$
\preceq \max_{h_{2}\sim K}\sum_{\substack{U_{2},V_{2},W_{2}\lesssim N^{2} / K^{2} (i = 0,1,2)\\ \left|h_{2}^{2}(U_{2} + V_{2}\alpha +W_{2}\beta) - \tau^{\prime}\right| <   2^{j}\\ h_{2}^{2}(U_{2},V_{2},W_{2}) = mx + c (x\in \mathbb{Z})}}1.
$$

Let$x _ { 0 } \in \mathbb { Z }$be fixed such that$m x _ { 0 } + c \equiv 0$(mod$h _ { 2 } ^ { 2 } )$(such$x _ { 0 }$exists, otherwise the sum will be zero). Let$x ^ { \prime } = x - x _ { 0 }$and$c ^ { \prime } = c + m x _ { 0 }$, then we have$m x ^ { \prime } \equiv 0$(mod$h _ { 2 } ^ { 2 } )$. As$\operatorname* { g c d } ( m _ { 1 } , m _ { 2 } , m _ { 3 } ) = 1$ we conclude that$x ^ { \prime } \equiv 0$(mod$h _ { 2 } ^ { 2 } )$. Then the expression above is bounded by

$$
\max_{h_{2}\sim K}\sum_{\substack{x^{\prime}\equiv 0\pmod {h_{2}^{2}}\\ \left|x^{\prime}(m_{1} + m_{2}\alpha +m_{3}\beta) + (c_{1}^{\prime} + c_{2}^{\prime}\alpha +c_{3}^{\prime}\beta) - \tau^{\prime}\right| <   2^{j}}}1\lesssim \max_{h_{2}\sim K}\left(\frac{2^{j}}{|h_{2}^{2}(m_{1} + m_{2}\alpha + m_{3}\beta)|} +1\right).
$$

Now for generic$\alpha , \beta$this is

$$
\preceq_ {\alpha , \beta} \frac {2 ^ {j} | m | ^ {2 + \epsilon}}{K ^ {2}} + 1
$$

from which the claim follows.

Proof of Lemma 6.7. By letting K and$N$range over powers of 2, the Borel-Cantelli lemma implies that for almost all$\alpha , \beta$we have

$$
\begin{array}{l}\Sigma_{0}(\alpha ,\beta)\preceq_{\alpha ,\beta}1 + \int \Sigma_{0}(\alpha^{\prime},\beta^{\prime})  d\alpha^{\prime}d\beta^{\prime}\\ = 1 + \sum_{h_{0},h_{1},h_{2}\sim K} \sum_{\substack{U_{i},V_{i},W_{i}\lesssim N^{2} / K^{2}\\ \Delta \neq 0}}(i = 0,1,2)\\ \text{measure}\big\{(\alpha^{\prime},\beta^{\prime}):  \big|h_{i}^{2}(U_{i} + V_{i}\alpha^{\prime} + W_{i}\beta^{\prime}) - h_{0}^{2}(U_{0} + V_{0}\alpha^{\prime} + W_{0}\beta^{\prime})\big| <   2^{j}\quad (i = 1,2)\big\} . \end{array}
$$

In light of (6.1) and (6.14), this implies

$$
\Sigma_{0}(\alpha ,\beta)\preceq_{\alpha ,\beta}1 + \sum_{h_{0},h_{1},h_{2}\sim K}\sum_{\substack{U_{i},V_{i},W_{i}\lesssim N^{2} / K^{2}\\ \Delta \neq 0}}2^{2j}|\Delta |^{-1}.\tag{6.17}
$$

How often can$\Delta$be small? Let

$$
H = \operatorname * {g c d} (h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0}, h _ {1} ^ {2} V _ {1} - h _ {0} ^ {2} V _ {0}), \quad G = \operatorname * {g c d} (h _ {1} ^ {2}, h _ {0} ^ {2} U _ {0}, h _ {0} ^ {2} V _ {0}), \quad T = | h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0} |.\tag{6.18}
$$

After permuting$U , V ,$and W if necessary, and also swapping$( U _ { 1 } , V _ { 1 } , W _ { 1 } ) , ( U _ { 2 } , V _ { 2 } , W _ { 2 } )$if necessary, we will have

$$
\frac {\operatorname * {g c d} (h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0} , h _ {1} ^ {2} W _ {1} - h _ {0} ^ {2} W _ {0})}{\operatorname * {g c d} (h _ {1} ^ {2} , h _ {0} ^ {2} U _ {0} , h _ {0} ^ {2} W _ {0})} \geq \frac {\operatorname * {g c d} (h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0} , h _ {1} ^ {2} V _ {1} - h _ {0} ^ {2} V _ {0})}{\operatorname * {g c d} (h _ {1} ^ {2} , h _ {0} ^ {2} U _ {0} , h _ {0} ^ {2} V _ {0})} = \frac {H}{G},\tag{6.19}
$$

$$
| h _ {2} ^ {2} U _ {2} - h _ {0} ^ {2} U _ {0} | \leq T, \quad | h _ {i} ^ {2} V _ {i} - h _ {0} ^ {2} V _ {0} | \leq T, \quad | h _ {i} ^ {2} W _ {i} - h _ {0} ^ {2} W _ {0} | \leq T (i = 1, 2).
$$

In particular, if$\Delta \neq 0$then it follows from this that$T > 0$and$H > 0$. Observe that

$$
\Delta \quad = h _ {2} ^ {2} \binom{(h _ {1} ^ {2} W _ {1} - h _ {0} ^ {2} W _ {0}) V _ {2} + (h _ {0} ^ {2} V _ {0} - h _ {1} ^ {2} V _ {1}) W _ {2}}{(h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0}) W _ {2} + (h _ {0} ^ {2} W _ {0} - h _ {1} ^ {2} W _ {1}) U _ {2}} + Q (h _ {0}, h _ {1}, U _ {0}, U _ {1}, V _ {0}, V _ {1}, W _ {0}, W _ {1})
$$

for some triple of forms Q. Suppose for a moment we are given$h _ { i } \sim K \ ( i = 0 , 1 , 2 )$and$U _ { i } , V _ { i } , W _ { i }$ $( i = 0 , 1 )$satisfying (6.18) and (6.19). One can deduce from the formula above that

$$
\sum_{\substack{U_{2},V_{2},W_{2}\lesssim N^{2} / K^{2}\\ \left|h_{2}^{2}(U_{2},V_{2},W_{2}) - h_{0}^{2}(U_{0},V_{0},W_{0})\right|\leq T\\ |\Delta |\leq M}}1\lesssim 1 + \frac{N^{2}H}{K^{2}T} +\frac{M}{K^{2}} +\frac{N^{2}HM}{K^{4}T} +\frac{M^{2}N^{2}}{T^{2}K^{6}}.
$$

In fact, if$M / T K ^ { 2 } \gtrsim 1$, then there are at most$N ^ { 2 } / K ^ { 2 }$choices for$U _ { 2 } ;$when$U _ { 2 }$is fixed, from $| \Delta | \le M$we get that there is at most$M / T K ^ { 2 }$choices for each of$V _ { 2 }$and$W _ { 2 }$. This gives a total of

$$
\frac {N ^ {2}}{K ^ {2}} \left(\frac {M}{T K ^ {2}}\right) ^ {2} = \frac {M ^ {2} N ^ {2}}{T ^ {2} K ^ {6}}
$$

choices.

Now if$M / T K ^ { 2 } \ll 1$, then for fixed$U _ { 2 }$there is at most 1 choice for each of$V _ { 2 }$and$W _ { 2 }$. Moreover, as$| \Delta | \le M$, there are at most$M / K ^ { 2 } + 1$choices for the quantity

$$
(h _ {1} ^ {2} V _ {1} - h _ {0} ^ {2} V _ {0}) U _ {2} + (h _ {0} ^ {2} U _ {0} - h _ {1} ^ {2} U _ {1}) V _ {2},
$$

so there are at most$M / K ^ { 2 } + 1$choices for the residue

$$
U _ {2} \pmod {\xi}, \quad \xi := \frac {h _ {0} ^ {2} U _ {0} - h _ {1} ^ {2} U _ {1}}{\operatorname* {g c d} (h _ {1} ^ {2} V _ {1} - h _ {0} ^ {2} V _ {0} , h _ {0} ^ {2} U _ {0} - h _ {1} ^ {2} U _ {1})}.
$$

Now$U _ { \mathrm { 2 } } \lesssim N ^ { 2 } / K ^ { 2 }$and$| \xi | \sim T / H$, so the number of choices for$U _ { 2 }$is at most

$$
\left(\frac {M}{K ^ {2}} + 1\right) \left(\frac {N ^ {2} H}{K ^ {2} T} + 1\right) \lesssim 1 + \frac {N ^ {2} H}{K ^ {2} T} + \frac {M}{K ^ {2}} + \frac {N ^ {2} H M}{K ^ {4} T}.
$$

Clearly the same bound holds if we permute$U , V$and W in (6.18), and also if we put  in place of the equalities in (6.18). Inserting this into (6.17) we find

$$
\begin{array}{c}\Sigma_{0}(\alpha ,\beta)\preceq_{\alpha ,\beta}1 + \sum_{T,M,G,H\in 2^{\mathbb{Z}}}\sum_{\substack{h_{0},h_{2}\sim K\\ 1\leq T\leq N^{2}\\ 1\leq M\leq T^{2}\\ 1\leq G\leq K^{2}\\ G\leq H\leq T}}\sum_{\substack{h_{1}\sim K\\ U_{0}\lesssim N^{2} / K^{2}}}\sum_{\substack{U_{1}\lesssim N^{2} / K^{2}\\ \gcd (h_{1}^{2},h_{0}^{2}U_{0})\gtrsim G\\ |h_{1}^{2}U_{1} - h_{0}^{2}U_{0}|\sim T}}\sum_{V_{0},W_{0}\lesssim N^{2} / K^{2}}\\ \\ \sum_{\substack{V_{1},W_{1}\lesssim N^{2} / K^{2}\\ |h_{1}^{2}V_{1} - h_{0}^{2}V_{0}|\lesssim T\\ |h_{1}^{2}W_{1} - h_{0}^{2}W_{0}|\lesssim T\\ \gcd (h_{1}^{2}U_{1} - h_{0}^{2}U_{0},h_{1}^{2}V_{1} - h_{0}^{2}V_{0})\sim H\\ \gcd (h_{1}^{2},h_{0}^{2}U_{0},h_{0}^{2}V_{0})\sim G\\ \frac{\gcd(h_{1}^{2}U_{1} - h_{0}^{2}U_{0},h_{1}^{2}W_{1} - h_{0}^{2}W_{0})}{\gcd(h_{1}^{2},h_{0}^{2}U_{0},h_{0}^{2}W_{0})}\gtrsim H / G}}\\ \\ \preceq 1 + \sum_{T,M,G,H\in 2^{\mathbb{Z}}}N^{2}\frac{K}{G^{1 / 2}}\left(\frac{T}{K^{2}} +1\right)\frac{N^{4}}{K ^{4}}\\ \\ \left(\frac{GT}{HK^{2}} +1\right)^{2}\left(1 + \frac{HN^{2}}{TK^{2}} +\frac{M}{K^{2}} +\frac{N^{2}HM}{K^{4}T} +\frac{M^{2}N^{2}}{T^{2}K^{6}}\right)2^{2j}M^{-1}. \end{array}
$$

Here we will explain the bound in the summation in$( V _ { 1 } , W _ { 1 } )$; the bounds in all other summations are straightforward. First consider$V _ { 1 } ;$as$( h _ { 0 } , h _ { 1 } , U _ { 0 } , U _ { 1 } , V _ { 0 } , W _ { 0 } )$is fixed, the four gcd’s in the summation have$\preceq 1$choices, so we may assume they are fixed. Let

$$
\xi = \operatorname * {g c d} (h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0}, h _ {1} ^ {2} V _ {1} - h _ {0} ^ {2} V _ {0}) \sim H, \qquad \operatorname * {g c d} (\xi , h _ {1} ^ {2}) = \operatorname * {g c d} (h _ {1} ^ {2}, h _ {0} ^ {2} U _ {0}, h _ {0} ^ {2} V _ {0}) \sim G,
$$

then we have$h _ { 1 } ^ { 2 } V _ { 1 } - h _ { 0 } ^ { 2 } V _ { 0 } \equiv 0$(mod ξ). This implies that the residue of$V _ { 1 }$modulo$\xi / \operatorname* { g c d } ( \xi , h _ { 1 } ^ { 2 } ) \sim$ $H / G$is fixed; as also$| \bar { h _ { 1 } ^ { 2 } V _ { 1 } } - h _ { 0 } ^ { 2 } V _ { 0 } | \lesssim T$, the number of choices for$V _ { 1 }$will be at most$G T / H K ^ { 2 } + 1$ For$W _ { 1 }$the bound is similar, except that instead of$\xi / \operatorname* { g c d } ( \xi , h _ { 1 } ^ { 2 } )$we have

$$
\frac {\eta}{\operatorname* {g c d} (\eta , h _ {1} ^ {2})} = \frac {\operatorname* {g c d} (h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0} , h _ {1} ^ {2} W _ {1} - h _ {0} ^ {2} W _ {0})}{\operatorname* {g c d} (h _ {1} ^ {2} , h _ {0} ^ {2} U _ {0} , h _ {0} ^ {2} W _ {0})}, \qquad \eta := \operatorname * {g c d} (h _ {1} ^ {2} U _ {1} - h _ {0} ^ {2} U _ {0}, h _ {1} ^ {2} W _ {1} - h _ {0} ^ {2} W _ {0}),
$$

which is not less than$H / G$by our assumptions.

Maximising the summand on the right-hand side over G and M, we find it is bounded by

$$
N ^ {2} K \left(\frac {T}{K ^ {2}} + 1\right) \frac {N ^ {4}}{K ^ {4}} \left(\frac {T ^ {2}}{H ^ {1 / 2} K (H + K ^ {2}) ^ {3 / 2}} + 1\right) \left(1 + \frac {H N ^ {2}}{T K ^ {2}} + \frac {N ^ {6}}{T ^ {2} K ^ {6}}\right) 2 ^ {2 j}
$$

and maximising this over H, it in turn is bounded by

$$
N ^ {2} K \left(\frac {T}{K ^ {2}} + 1\right) \frac {N ^ {4}}{K ^ {4}} \left(\frac {N ^ {2} T ^ {3 / 2}}{(T ^ {3 / 2} + K ^ {3}) K ^ {3}} + \frac {T N ^ {2}}{K ^ {5}} + \frac {T ^ {2}}{K ^ {4}} + \frac {N ^ {6}}{K ^ {1 0}} + \frac {N ^ {2}}{K ^ {2}} + \frac {N ^ {6}}{T ^ {2} K ^ {6}}\right) 2 ^ {2 j}
$$

which, considering the cases when$T \in \{ 1 , K ^ { 2 } , N ^ { 2 } \}$, is bounded by

$$
\left(\frac {N ^ {1 2}}{K ^ {9}} + \frac {N ^ {1 4}}{K ^ {1 5}}\right) 2 ^ {2 j} \lesssim \frac {N ^ {1 2}}{K ^ {9}} 2 ^ {2 j} \lesssim \frac {N ^ {1 2}}{K ^ {3}} 2 ^ {3 j}
$$

using the fact that$2 ^ { j } \geq N ^ { - 3 }$and$N ^ { 1 / 2 } \leq K \leq N$

6.6. Completing the case$p = 8$. Combining (6.7) with (6.9) and (6.11) shows that

$$
\| e ^ {i t \tilde {\Delta}} f \| _ {L ^ {8} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {8} \lesssim | S ^ {4} | \Big ((N T + N) + (N ^ {3} + N T) + (N ^ {4} + N T) \Big)
$$

which proves the case$p = 8$of Theorem 6.1.

## 7. The counting argument through Pall’s bound:$p = 1 0$

With the same ansatz for f as in Section 5, we will prove

Theorem 7.1. Generically in$( \alpha _ { i j } )$

$$
\| e ^ {i t \widetilde {\Delta}} f \| _ {L ^ {1 0} ([ 0, T ] \times \mathbb {T} ^ {2})} ^ {1 0} \lesssim | S ^ {5} | (N ^ {6} + T N ^ {2}).
$$

This implies Theorem 1.2 for$p = 1 0$

Following the same argument as in Section$6 ,$we have by (6.3) that

$$
\| e^{it\widetilde{\Delta}}f\|_{L^{p}([0,T])}^{10}\lesssim \sum_{2^{j} > \frac{1}{T}}2^{-j}|S^{5}|\sup_{a,b\lesssim N,\tau \lesssim N^{2}}\sum_{\substack{A_{1},B_{1},C_{1}\lesssim N^{2}\\ |A_{1} + B_{1}\alpha +C_{1}\beta -\tau | <   2^{j}}}|\Omega_{a,b,A_{1},B_{1},C_{1}}^{5,N, + }
$$

where$\Omega _ { a , b , A _ { 1 } , B _ { 1 } , C _ { 1 } } ^ { 5 , N , + }$is the set of solutions of size less than N to

$$
\sum_ {i = 1} ^ {5} k _ {i} = a, \sum_ {i = 1} ^ {5} \ell_ {i} = b, \sum_ {i = 1} ^ {5} k _ {i} ^ {2} = A _ {1}, \sum_ {i = 1} ^ {5} \ell_ {i} ^ {2} = B _ {1}, \sum_ {i = 1} ^ {5} k _ {i} \ell_ {i} = C _ {1}.
$$

After shifting the variables we can assume$a , b = 0$. Over$\mathbb { Q }$the form$x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } + x _ { 4 } ^ { 2 } + ( x _ { 1 } + x _ { 2 } +$ $x _ { 3 } + x _ { 4 } ) ^ { 2 }$is equivalent to$x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } + 5 x _ { 4 } ^ { 2 }$, namely

$$
\begin{array}{r l} & x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} + x _ {4} ^ {2} + (x _ {1} + x _ {2} + x _ {3} + x _ {4}) ^ {2} \\ & \qquad = (x _ {1} + x _ {2} + x _ {4} / 2) ^ {2} + (x _ {2} + x _ {3} + x _ {4} / 2) ^ {2} + (x _ {1} + x _ {3} + x _ {4} / 2) ^ {2} + 5 (x _ {4} / 2) ^ {2}. \end{array}
$$

So under some linear change of variables, each integral solution to the equations above gives us an integral solution to

$$
\sum_ {i = 1} ^ {3} k _ {i} ^ {2} + 5 k _ {4} ^ {2} = A ^ {\prime}, \sum_ {i = 1} ^ {3} \ell_ {i} ^ {2} + 5 \ell_ {4} ^ {2} = B ^ {\prime}, \sum_ {i = 1} ^ {3} k _ {i} \ell_ {i} + 5 k _ {4} \ell_ {4} = C ^ {\prime}
$$

for some fixed, integral$A ^ { \prime } , B ^ { \prime } , C ^ { \prime }$. That is,

$$
\begin{array}{l}\| e^{it\widetilde{\Delta}}f\|_{L^{10}([0,T])}^{10}\lesssim \sum_{2^{j} > \frac{1}{T}}2^{-j}|S^{5}|\sup_{\tau^{\prime}\lesssim N^{2}}\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}}}\sum_{\substack{\sum_{i = 1}^{3}\mu_{i}^{2} + 5\mu_{4}^{2} = A^{\prime},\\ \sum_{i = 1}^{3}\lambda_{i}^{2} + 5\lambda_{4}^{2} = B^{\prime},\\ \sum_{i = 1}^{3}\mu_{i}\lambda_{i} + 5\mu_{4}\lambda_{4} = C^{\prime}}}1\\ \\ \preceq \sum_{2^{j} > \frac{1}{T}}2^{-j}|S^{5}|\sup_{\tau^{\prime}\lesssim N^{2}}\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2 ^ {j}}}\sum_{x,y\lesssim N}\sum_{\substack{\sum_{i = 1}^{3}\mu_{i}^{2} = A^{\prime} - 5x^{2},\\ \sum_{i = 1}^{3}\lambda_{i}^{2} = B^{\prime} - 5y^{2},\\ \sum_{i = 1}^{3}\mu_{i}\lambda_{i} = C^{\prime} - 5xy}}1. \end{array}
$$

The idea is to use Pall’s result to bound the innermost sum. First we deal with degenerate cases. The first degenerate case is when$A ^ { \prime } = 5 x ^ { 2 }$or$B ^ { \prime } = 5 y ^ { 2 }$; without loss of generality we treat$B ^ { \prime } = 5 y ^ { 2 }$ which gives a contribution of

$$
\sum_ {(m, x, y): | m + 5 x ^ {2} + 5 y ^ {2} \alpha + 5 x y \beta - \tau^ {\prime} | <   2 ^ {j}} \sum_ {(\mu_ {i}): \sum_ {i = 1} ^ {3} \mu_ {i} ^ {2} = m} 1 \preceq (2 ^ {j} N ^ {4} + 1) N,
$$

by the Diophantine condition$| i + j \alpha + k \beta | \gtrsim N ^ { - 4 } \mathrm { ~ i f ~ } i , j , k \lesssim N ^ { 2 }$, with$( i , j , k ) \neq ( 0 , 0 , 0 )$. This is more than satisfactory.

Next we consider the contribution from$( \sum _ { i = 1 } ^ { 3 } \mu _ { i } ^ { 2 } ) ( \sum _ { i = 1 } ^ { 3 } \lambda _ { i } ^ { 2 } ) = ( \sum _ { i = 1 } ^ { 3 } \mu _ { i } \lambda _ { i } ) ^ { 2 } \ne 0 .$. In this case there are unique$z _ { i } , p , q$with$p , q \in \mathbb { N }$and$\operatorname* { g c d } ( p , q ) = 1$such that$\mu _ { i } = p z _ { i } , \lambda _ { i } = q z _ { i }$. These terms give a contribution of

$$
\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}}}\sum_{\substack{mp^{2} + 5x^{2} = A^{\prime},\\ mq^{2} + 5y^{2} = B^{\prime},\\ mpq + 5xy = C^{\prime}}}\sum_{\substack{i = 1^{3}z_{i}^{2} = m\\ }}1\\ \lesssim (2^{j}N^{4} + 1)N\sup_{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}}|\{(m,p,q,x,y):mp^{2} + 5x^{2} = A^{\prime},mq^{2} + 5y^{2} = B^{\prime},mpq + 5xy = C^{\prime}\} |.
$$

We claim the last supremum$\mathrm { i s } \preceq N$. Indeed we can choose x arbitrarily,$\mathrm { g e t } \preceq 1$choices for$m$and $p$by the divisor bound, and then as mp$\neq 0$by assumption, we get that$( q , y )$lies on the intersection of an ellipse and a line and we’re done. This gives us a contribution of$\lesssim ( 2 ^ { j } N ^ { 4 } + 1 ) N ^ { 2 }$, as desired.

Finally we treat the case$0 \neq ( \textstyle \sum _ { i = 1 } ^ { 3 } \mu _ { i } ^ { 2 } ) ( \textstyle \sum _ { i = 1 } ^ { 3 } \lambda _ { i } ^ { 2 } ) \neq ( \textstyle \sum _ { i = 1 } ^ { 3 } \mu _ { i } \lambda _ { i } ) ^ { 2 }$. By Pall, the contribution is

$$
\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\beta -\tau^{\prime}| <   2^{j}}}\sum_{h\lesssim N}\sum_{\substack{h^{2}U + 5x^{2} = A\\ h^{2}V + 5y^{2} = B\\ h^{2}W + 5xy = C}}h.
$$

We get

$$
| \{(U, V, W, x, y): h ^ {2} U + 5 x ^ {2} = A, h ^ {2} V + 5 y ^ {2} = B, h ^ {2} W + 5 x y = C \} | \preceq \frac {N ^ {2}}{h ^ {2}}
$$

by choosing the values of$W$and$x y .$and then using the divisor bound. Note that if$x y = 0$, say $x = 0$, then$( U , W )$is uniquely fixed, and we can get the same bound by choosing the values of$V$ and$y ^ { 2 }$. This gives us

$$
\sum_{\substack{A^{\prime},B^{\prime},C^{\prime}\lesssim N^{2}\\ |A^{\prime} + B^{\prime}\alpha +C^{\prime}\widehat{\beta} -\tau^{\prime}| <   2^{j}}}\sum_{h \lesssim N}\sum_{\substack{h^{2}U + 5x^{2} = A\\ h^{2}V + 5y^{2} = B\\ h^{2}W + 5xy = C}}h\preceq (2^{j}N^{4} + 1)N^{2}
$$

and we’re done.

## Appendix A. Higher dimensions: the result of Guo and Zhang

The case$k = 2$of the main result of Guo and Zhang [22] is

$$
\begin{array}{l}\int \dots \int \bigg|\sum_{\substack{0\leq \beta_{i}\leq 1\\ 0\leq \alpha_{ij}\leq 1}}\Big|\sum_{\substack{x\in \mathbb{Z}^{d}\\ |x|\leq M}}e\Big(\sum_{i,j = 1}^{d}\alpha_{ij}x_{i}x_{j} + \sum_{i = 1}^{d}\beta_{i}x_{i}\Big)\bigg|^{2s}d\alpha_{11}  d\alpha_{12}\dots d\alpha_{dd}  d\beta_{1}\dots d\beta_{d}\\ \\ \lesssim_{\epsilon}N^{\epsilon}\bigg(N^{ds} + \sum_{j = 1}^{d}N^{(2s - 1)j + d - j(j + 2)}\bigg), \end{array}
$$

and the right-hand side is seen to be$\lesssim N ^ { \epsilon } ( N ^ { d s } + N ^ { 2 d s - d ( d + 2 ) } )$. We sketch the argument by which (1.10) follows from this bound. More precisely, if we define

$$
Z (M) = \# \Bigl \{x ^ {(1)}, \ldots , x ^ {(2 s)} \in \mathbb {Z} ^ {d}: | x ^ {(i)} | \leq M, \sum_ {i = 1} ^ {2 s} (- 1) ^ {i} x _ {j} ^ {(i)} x _ {k} ^ {(i)} = 0 (1 \leq j, k \leq d) \Bigr \},
$$

then we have

$$
Z (M) \lesssim_ {\epsilon} M ^ {d s + d + \epsilon} + M ^ {2 d s - d (d + 1) + \epsilon}.\tag{A.1}
$$

Indeed this follows from the result of Guo-Zhang on summing over the possible values of$\textstyle \sum _ { i = 1 } ^ { 2 s } ( - 1 ) ^ { i } x ^ { ( i ) }$ We will deduce (1.10) from this last estimate.

For generic$\left( \alpha _ { i j } \right)$we have

$$
I _ {s} (T) \lesssim_ {\alpha} N ^ {\epsilon} T ^ {\epsilon} \int_ {1 \leq \alpha_ {i j} \leq 2} \dots \int I _ {s} (T) d \alpha_ {1 1} d \alpha_ {1 2} \dots d \alpha_ {d d},\tag{A.2}
$$

by estimating the measure of the set of exceptional α for which this fails, and taking the union over T, N of the form$2 ^ { k }$. For$T \geq 2$the right-hand side above is

$$
\asymp N ^ {\epsilon} T ^ {1 + \epsilon} \int_ {0 \leq \alpha_ {i j} \leq 1} \dots \int_ {x \in \mathbf {T} ^ {d}} \sup _ {x \in \mathbf {T} ^ {d}} \left| K _ {N} ^ {(d)} (1, x) \right| ^ {2 s} d \alpha_ {1 1} d \alpha_ {1 2} \dots d \alpha_ {d d},\tag{A.3}
$$

using the fact that the last integrand is 1-periodic in each$\alpha _ { i j }$. Now, by the same argument as (3.2), we have

$$
\left. \left| K _ {N} ^ {(d)} (1, x) \right| ^ {2} \preceq N ^ {d} \left[ \# \{n \in [ - 4 N, 4 N ] ^ {d} \text {s.t.} \| L _ {j} (n) \| <   \frac {2}{N} \} + 1 \right]. \right.
$$

The idea is that we can bound the right-hand side by some kind of exponenetial sum which looks very much like$| K _ { N } ^ { ( d ) } ( 0 , 0 ) | ^ { 2 }$. To motivate this strategy requires some inspection of the proof of (3.2), but the argument itself is short. We observe that the right-hand side in the last display is

$$
\lesssim N ^ {d} \sum_ {w, n \in \mathbb {Z} ^ {d}} e ^ {- \frac {2}{N ^ {2}} | n | ^ {2} - \frac {N ^ {2}}{8} | w - 4 (\alpha_ {i j}) n | ^ {2}}
$$

and, by Poisson summation in$w ,$this is

$$
= 2 ^ {d} \sum_ {n, m \in \mathbb {Z} ^ {d}} e ^ {- \frac {2}{N ^ {2}} | n | ^ {2} - \frac {2}{N ^ {2}} | m | ^ {2}} e \bigg (- 4 \sum_ {i j} \alpha_ {i j} n _ {i} m _ {j} \bigg).
$$

Changing variables to$x = n - m , y = n + m$we have shown that

$$
\sup_{x\in \mathbf{T}^{d}}\Big|K_{N}^{(d)}(1,x)\Big|^{2}\preceq \sum_{\substack{x,y\in \mathbb{Z}^{d}\\ x\equiv y  (2)}}e^{-\frac{|x|^{2} + |y|^{2}}{N^{2}}}e\bigg(\sum_{ij}\alpha_{ij}x_{i}x_{j} - \sum_{ij}\alpha_{ij}y_{i}y_{j}\bigg).
$$

Substituting this into (A.3) we obtain

$$
\begin{array}{l}I_{s}(T)\preceq_{\alpha}T\sum_{\substack{x^{(i)},y^{(i)}\in \mathbb{Z}^{d},x^{(i)}\equiv y^{(i)}  (2)\\ \sum_{i = 1}^{s}x_{j}^{(i)}x_{k}^{(i)} = \sum_{i = 1}^{s}y_{j}^{(i)}y_{k}^{(i)}  (1\leq j,k\leq d)}}e^{-\sum_{i}\frac{|x^{(i)}|^{2} + |y^{(i)}|^{2}}{N^{2}}}\\ \lesssim T\sum_{\substack{M\in 2^{\mathbb{Z}}\\ M > N}}e^{-M^{2} / N^{2}}Z(M). \end{array}
$$

This together with (A.1) proves (1.10).

We would have an optimal bound for$Z ( M )$if we could replace the$d s + d$in (A.1) and hence (1.10) with$d s .$This would be predicted by a square-root cancellation heuristic standard in the circle method, and it seems likely that it can be proved as follows. We can intepret$Z ( M )$as a count of d-tuples of integer points$y \in \mathbb { Z } ^ { 2 s }$with norm at most M and whose span V is contained in the hypersurface$\begin{array} { r } { \sum ( - 1 ) ^ { i } \bar { y } ^ { ( i ) } = 0 } \end{array}$. Given dim$V _ { : }$, we can count the possible spans$V ,$for example using the work of Franke-Manin-Tschinkel [17], and then we can count d-tuples of points in each space V.

## References

[1] V. Bentkus, F. G¨otze, On the lattice point problem for ellipsoids. Acta Arith. 80 (1997), no. 2, 101-125.

[2] V. Bentkus, F. G¨otze, Lattice point problems and distribution of values of quadratic forms. Ann. of Math. (2) 150 (1999), no. 3, 977-1027.

[3] J. Bourgain, Fourier transform restriction phenomena for certain lattice subsets and applications to nonlinea evolution equations. I. Schr¨odinger equations. Geom. Funct. Anal. 3 (1993), no. 2, 107-156.

[4] J. Bourgain, On the growth in time of higher Sobolev norms of smooth solutions of Hamiltonian PDE. Internat. Math. Res. Notices (1996), no. 6, 277-304.

[5] J. Bourgain, On Strichartz’s inequalities and the nonlinear Schr¨odinger equation on irrational tori, in Mathematical Aspects of Nonlinear Dispersive Equations, Ann. of Math. Stud. 163, Princeton Univ. Press, Princeton, NJ, 2007, 1-20.

[6] J. Bourgain, Moment inequalities for trigonometric polynomials with spectrum in curved hypersurfaces. Israel J. Math. 193 (2013), 441-458.

[7] J. Bourgain, A quantitative Oppenheim theorem for generic diagonal quadratic forms. Israel J. Math. 215 (2016), no. 1, 503-512.

[8] J. Bourgain, C. Demeter, The proof of the$\ell ^ { 2 }$decoupling conjecture. Ann. of Math. (2) 182 (2015), no. 1, 351-389.

[9] J. Bourgain, C. Demeter, Mean value estimates for Weyl sums in two dimensions. J. Lond. Math. Soc. (2) 94 (2016), no. 3, 814-838.

[10] J. Bourgain, C. Demeter, Decouplings for curves and hypersurfaces with nonzero Gaussian curvature. J. Anal. Math. 133 (2017), 279-311.

[11] J. Bourgain, C. Demeter, Three applications of the Siegel mass formula, in Geometric Aspects of Functional Analysis. Lecture Notes in Mathematics, vol 2256 (2020). Springer, Cham.

[12] N. Burq, P. G´erard, N. Tzvetkov, Strichartz inequalities and the nonlinear Schr¨odinger equation on compact manifolds. Amer. J. Math. 126 (2004), no. 3, 569-605.

[13] H. Davenport, Indefinite quadratic forms in many variables. II. Proc. London Math. Soc. (3) 8 (1958), 109-126.

[14] Y. Deng, On growth of Sobolev norms for energy critical NLS on irrational tori: Small energy case. Comm. Pure Appl. Math., 72: 801-834.

[15] Y. Deng, P. Germain, Growth of solutions to NLS on irrational tori. Internat. Math. Res. Notices (2019), no. 9, 2919-2950.

[16] Y. Deng, P. Germain, L. Guth, Strichartz estimates for the Schr¨odinger equation on irrational tori. J. Funct. Anal. 273 (2017), no. 9, 2846-2869.

[17] J. Franke, Y. I. Manin, and Y. Tschinkel, Rational points of bounded height on Fano varieties, Invent. Math. 95 (1989), no. 2, 421-435.

[18] Z. Guo, T. Oh, Y. Wang, Strichartz estimates for Schr¨odinger equations on irrational tori. Proc. Lond. Math. Soc. 109 (2014), 975-1013.

[19] A. Ghosh, D. Kelmer, A quantitative Oppenheim theorem for generic ternary quadratic forms. J. Mod. Dyn. 12 (2018), 1-8.

[20] F. G¨otze, G. Margulis, Distribution of values of quadratic forms at integral points. ArXiv e-prints (2010), arXiv:1004.5123.

[21] F. G¨otze, Lattice point problems and values of quadratic forms. Invent. Math. 157 (2004), no. 1, 195-226.

[22] S. Guo, R. Zhang, On integer solutions of Parsell–Vinogradov systems. Invent. math. 218, 1–81 (2019).

[23] W. M¨uller, Systems of quadratic Diophantine inequalities and the value distribution of quadratic forms. Monatsh. Math. 153 (2008), no. 3, 233-250.

[24] S. Herr, D. Tataru, N. Tzvetkov, Global well-posedness of the energy-critical nonlinear Schr¨odinger equation with small initial data in$H ^ { 1 } ( T ^ { 3 } )$. Duke Math. J. 159 (2011) 329-349.

[25] A. Ionescu, B. Pausader, The energy-critical defocusing NLS on T<sup>3</sup>. Duke Math. J. 161 (2012), no. 8, 1581-1612.

[26] D. Kelmer, S. Yu, Values of random polynomials in shrinking targets. Trans. Amer. Math. Soc. 373 (2020), 8677-8695.

[27] G. Pall, Representation by quadratic forms. Canadian J. Math. 1, (1949). 344-364.

[28] S. T. Parsell, S. M. Prendiville, T. D. Wooley, Near-optimal mean value estimates for multidimensional Weyl sums. Geom. Funct. Anal. 23.6 (2013) 1962-2024.

[29] T. Tao, Nonlinear dispersive equations: local and global analysis, No 106 (2006), American Mathematical Soc.

[30] P. A. Tomas, A restriction theorem for the Fourier transform. Bull. Amer. Math. Soc. 81 (1975), 477-478.

(Y. Deng) Courant Institute of Mathematical Sciences, New York University, 251 Mercer Street, New York, N.Y. 10012-1185, USA Email address: yudeng@cims.nyu.edu

(P. Germain) Courant Institute of Mathematical Sciences, New York University, 251 Mercer Street, New York, N.Y. 10012-1185, USA Email address: pgermain@cims.nyu.edu

(L. Guth) Massachusetts Institute of Technology, Department of Mathematics, 77 Massachusetts Avenue, Cambridge, MA 02139-4307, USA Email address: larry.guth.work@gmail.com

(S. L. Rydin Myerson) Mathematisches Institut, Georg-August-Universitat G¨ ottingen, Bunsenstraße¨ 3-5, D-37073 Gottingen, Deutschland¨ Email address: myerson@goettingen.de