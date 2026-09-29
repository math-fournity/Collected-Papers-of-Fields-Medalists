# Reducibility or nonuniform hyperbolicity for quasiperiodic Schr¨odinger cocycles

By Artur Avila\* and Raphael Krikorian<sup>¨</sup>

## Abstract

We show that for almost every frequency$\alpha \in \mathbb { R } \backslash \mathbb { Q }$, for every$C ^ { \omega }$potential $v : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$, and for almost every energy E the corresponding quasiperiodic Schr¨odinger cocycle is either reducible or nonuniformly hyperbolic. This result gives very good control on the absolutely continuous part of the spectrum of the corresponding quasiperiodic Schr¨odinger operator, and allows us to complete the proof of the Aubry-Andr´e conjecture on the measure of the spectrum of the Almost Mathieu Operator.

## 1. Introduction

A one-dimensional quasiperiodic$C ^ { r } { - } c o c y c l e$in$\operatorname { S L } ( 2 , \mathbb { R } )$(briefly, a$C ^ { r } { \mathrm { - } } \mathrm { c o } { \mathrm { - } }$ cycle) is a pair$( \alpha , A ) \in \mathbb { R } \times C ^ { r } ( \mathbb { R } / \mathbb { Z } , \operatorname { S L } ( 2 , \mathbb { R } ) )$, viewed as a linear skew-product:

$$
\begin{array}{c} (\alpha , A): \mathbb {R} / \mathbb {Z} \times \mathbb {R} ^ {2} \to \mathbb {R} / \mathbb {Z} \times \mathbb {R} ^ {2} \\ (x, w) \mapsto (x + \alpha , A (x) \cdot w). \end{array}\tag{1.1}
$$

For$n \in \mathbb { Z }$, we let$A _ { n } \in C ^ { r } ( \mathbb { R } / \mathbb { Z } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$be defined by the rule$( \alpha , A ) ^ { n } =$ $( n \alpha , A _ { n } )$(we will keep the dependence of$A _ { n }$on α implicit). Thus$A _ { 0 } ( x ) = \mathrm { i d }$

$$
A _ {n} (x) = \prod_ {j = n - 1} ^ {0} A (x + j \alpha) = A (x + (n - 1) \alpha) \dots A (x), \quad \text { for } n \geq 1,\tag{1.2}
$$

and$A _ { - n } ( x ) = A _ { n } ( x - n \alpha ) ^ { - 1 }$. The Lyapunov exponent of$( \alpha , A )$is defined as

$$
L (\alpha , A) = \lim _ {n \to \infty} \frac {1}{n} \int_ {\mathbb {R} / \mathbb {Z}} \ln \| A _ {n} (x) \| d x \geq 0.\tag{1.3}
$$

Also,$( \alpha , A )$is uniformly hyperbolic if there exists a continuous splitting $E _ { s } ( x ) \oplus E _ { u } ( x ) = \mathbb { R } ^ { 2 }$, and$C > 0 , 0 < \lambda < 1$such that for every$n \geq 1$we have

$$
\left\| A _ {n} (x) \cdot w \right\| \leq C \lambda^ {n} \| w \|, \quad w \in E _ {s} (x),\tag{1.4}
$$

$$
\left\| A _ {- n} (x) \cdot w \right\| \leq C \lambda^ {n} \| w \|, \quad w \in E _ {u} (x).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*A. A. is a Clay Research Fellow.</span></small>

Such splitting is automatically unique and thus invariant; that is,$A ( x ) E _ { s } ( x ) =$ $E _ { s } ( x + \alpha )$and$A ( x ) E _ { u } ( x ) = E _ { u } ( x + \alpha )$. The set of uniformly hyperbolic cocycles is open in the$C ^ { 0 } .$-topology (one allows perturbations both in α and in$A )$

Uniformly hyperbolic cocycles have a positive Lyapunov exponent. If $( \alpha , A )$has positive Lyapunov exponent but is not uniformly hyperbolic then it will be called nonuniformly hyperbolic.

We say that a C<sup>r</sup>-cocycle$( \alpha , A )$is$C ^ { r } { - } r e d u c i b l e$if there exists

$$
B \in C ^ {r} (\mathbb {R} / 2 \mathbb {Z}, \mathrm{SL} (2, \mathbb {R})) \text {and} A _ {*} \in \mathrm{SL} (2, \mathbb {R})
$$

such that

$$
B (x + \alpha) A (x) B (x) ^ {- 1} = A _ {*}, \quad x \in \mathbb {R}.\tag{1.5}
$$

Also,$( \alpha , A )$is$C ^ { r }$-reducible modulo Z if one can take$B \in C ^ { r } ( \mathbb { R } / \mathbb { Z } , { \mathrm { S L } } ( 2 , \mathbb { R } ) ) .$1 Now,$\alpha \in \mathbb { R } \setminus \mathbb { Q }$satisfies a Diophantine condition$\mathrm { D C } ( \kappa , \tau ) , \kappa > 0 , \tau > 0$ if

$$
| q \alpha - p | > \kappa | q | ^ {- \tau}, (p, q) \in \mathbb {Z} ^ {2}, q \neq 0.\tag{1.6}
$$

Let$\mathrm { D C } = \cup _ { \kappa > 0 , \tau > 0 } \mathrm { D C } ( \kappa , \tau )$. It is well known that$\cup _ { \kappa > 0 } \mathrm { D C } ( \kappa , \tau )$has full Lebesgue measure if$\tau > 1$

Now,$\alpha \in \mathbb { R } \setminus \mathbb { Q }$satisfies a recurrent Diophantine condition$\mathrm { R D C } ( \kappa , \tau )$if there are infinitely many$n > 0$such that$G ^ { n } ( \{ \alpha \} ) \in \mathrm { D C } ( \kappa , \tau )$, where {α} is the fractional part of α and$G : ( 0 , 1 ) \to [ 0 , 1 )$is the Gauss map$G ( x ) = \{ x ^ { - 1 } \}$ We let$\mathrm { R D C } = \cup _ { \kappa > 0 , \tau > 0 } \mathrm { R D C } ( \kappa , \tau )$. Notice that$\mathrm { R D C } ( \kappa , \tau )$has full Lebesgue measure as long as$\mathrm { D C } ( \kappa , \tau )$has positive Lebesgue measure (since the Gauss map is ergodic with respect to the probability measure$\frac { d x } { ( 1 + x ) \ln 2 } )$. It is possible to show that R \ RDC has Hausdorf dimension$1 / 2$

Given$v \in C ^ { r } ( \mathbb { R } / \mathbb { Z } , \mathbb { R } )$, let us consider the Schr¨odinger cocycle

$$
S _ {v, E} (x) = \left( \begin{array}{c c} E - v (x) & - 1 \\ 1 & 0 \end{array} \right) \in C ^ {r} (\mathbb {R} / \mathbb {Z}, \mathrm{SL} (2, \mathbb {R}))\tag{1.7}
$$

(v is called the potential and E is called the energy).

There is fairly good comprehension of the dynamics of Schr¨odinger cocycles in the case of either small or large potentials:

Proposition 1.1 (Sorets-Spencer [SS]). Let$v \in C ^ { \omega } ( \mathbb { R } / \mathbb { Z } , \mathbb { R } )$be a non-constant potential, and let$\alpha \in \mathbb { R }$. There exists$\lambda _ { 0 } = \lambda _ { 0 } ( v ) > 0$such that$i f$ $| \lambda | > \lambda _ { 0 }$then for every$E \in \mathbb { R }$there is$L ( \alpha , S _ { \lambda v , E } ) > 0$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2Z”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Obviously, reducibility modulo Z is a stronger notion than plain reducibility, but in some situations one can show that both definitions are equivalent (see Remark 1.5). The advantage of defining reducibility “modulo is to include some special situations (notably certain uniformly hyperbolic cocycles).</span></small>

Proposition 1.2 (Eliasson$[ \mathrm { E } 1 ] ^ { 2 } )$. Let$v \in C ^ { \omega } ( \mathbb { R } / \mathbb { Z } , \mathbb { R } )$, and let$\alpha \in \mathrm { D C }$ There exists$\lambda _ { 0 } = \lambda _ { 0 } ( v , \alpha )$such that$i f \left| \lambda \right| < \lambda _ { 0 }$then for almost every$E \in \mathbb { R }$ the cocycle$( \alpha , S _ { \lambda v , E } )$is$C ^ { \omega } { } _ { - r e d u c i b l e }$

Remark 1.1. Sorets-Spencer’s result is nonperturbative: the “largeness” condition$\lambda _ { 0 }$does not depend on$\alpha .$. On the other hand, the proof of Eliasson’s result is perturbative: the “smallness” condition$\lambda _ { 0 }$depends in principle on α (in the full measure set$\mathrm { D C } \subset \mathbb { R } )$. We will come back to this issue (cf. Theorem 1.4).

Remark 1.2. In general, one cannot replace “almost$\mathrm { e v e r y } ^ { \mathfrak { Y } }$by “every” in Eliasson’s result above. Indeed, in [E1] it is also shown that the set of energies for which$( \alpha , S _ { \lambda v , E } )$is not (even$C ^ { 0 } )$reducible is nonempty for a generic (in an appropriate topology) choice of$( \lambda , v )$satisfying$| \lambda | < \lambda _ { 0 } ( v )$ Those “exceptional” energies do have zero Lyapunov exponent.

Remark 1.3. Let$\alpha \in \mathrm { D C }$and$A \in C ^ { r } ( \mathbb { R } / \mathbb { Z } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$),$r = \infty , \omega$. In this case,$( \alpha , A )$is uniformly hyperbolic if and only if it is$C ^ { r } .$-reducible and has a positive Lyapunov exponent, see [E2, §2]. Thus, there are lots of “simple cocycles” for which one has positive Lyapunov exponent, resp. reducibility, and indeed both at the same time: this is the case in particular for$| E |$large in the Schr¨odinger case. Those examples are also stable (here we fix$\alpha \in \mathrm { D C }$ and stability is with respect to perturbations of A).

However, cocycles with a positive Lyapunov exponent, resp. reducible, but which are not uniformly hyperbolic do happen for a positive measure set of energies for many choices of the potential, and in particular in the situations described by the results of Sorets-Spencer (this follows from [B, Th. 12.14]), resp. Eliasson.

Our main result for Schr¨odinger cocycles aims to close the gap and describe the situation (for almost every energy) without largeness/smallness assumption on the potential:

Theorem A. Let$\alpha ~ \in ~ \mathrm { R D C }$and let$v : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$be$a ~ C ^ { \omega }$potential. Then, for Lebesgue almost every$E _ { i }$, the cocycle$( \alpha , S _ { v , E } )$is either nonuniformly hyperbolic$o r \ : C ^ { \omega }$-reducible.

For$\theta \in \mathbb { R }$, let

$$
R _ {\theta} = \left( \begin{array}{c c} \cos 2 \pi \theta & - \sin 2 \pi \theta \\ \sin 2 \pi \theta & \cos 2 \pi \theta \end{array} \right).\tag{1.8}
$$

Given a C<sup>r</sup>-cocycle$( \alpha , A )$, we associate a canonical one-parameter family of $C ^ { r } .$-cocycles$\theta \mapsto \left( \alpha , R _ { \theta } A \right)$. Our proof of Theorem$\mathrm { A }$goes through for the more general context of cocycles homotopic to the identity, with the role of the energy parameter replaced by the θ parameter.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>This result was originally stated for the continuous time case, but the proof also works for the discrete time case.</span></small>

Theorem$\mathrm { A } ^ { \prime } .$. Let$\alpha \in \mathrm { R D C } ,$and let$A : \mathbb { R } / \mathbb { Z } \to { \mathrm { S L } } ( 2 , \mathbb { R } )$be$C ^ { \omega }$and homotopic to the identity<sup>3</sup>. Then for Lebesgue almost every$\theta \in \mathbb { R } / \mathbb { Z }$, the cocycle$( \alpha , R _ { \theta } A )$is either nonuniformly hyperbolic or$C ^ { \omega }$-reducible.

Remark 1.4. Theorems A and$\mathrm { A } ^ { \prime }$also hold in the smooth setting. The only modification in the proof is in the use of a KAM theoretical result of Eliasson (see Theorem 2.7), which must be replaced by a smooth version. They also generalize to the case of continuous time (diferential equations): in this case the adaptation is straightforward. See [AK2] for a discussion of those generalizations.

Remark 1.5. One can distinguish two distinct behaviors among the reducible cocycles$( \alpha , A )$given by Theorems$\mathrm { A }$and$\mathrm { A } ^ { \prime }$. The first is uniformly hyperbolic behavior; see Remark 1.3. The second is totally elliptic behavior, corresponding (projectively) to an irrational rotation of$\mathbb { T } ^ { 2 } \equiv \mathbb { R } / \mathbb { Z } \times \mathbb { P } ^ { 1 }$. More precisely, we call a cocycle totally elliptic if it is$C ^ { r } .$-reducible and the constant matrix$A _ { * }$in (1.5) can be chosen to be a rotation$R _ { \rho }$, where$( 1 , \alpha , \rho )$ are linearly independent over$\mathbb { Q } .$. In this case it is easy to see that the cocycle $( \alpha , A )$is automatically$C ^ { r }$-reducible modulo$\mathbb { Z }$(possibly replacing$\rho$by$\rho + \frac { \alpha } { 2 } )$). (To see that almost every reducible cocycle is either uniformly hyperbolic or totally elliptic, it is enough to use Theorems 2.3 and 2.4 which are due to Johnson-Moser and Deift-Simon.)

Theorems A and$\mathrm { A } ^ { \prime }$give a nice global picture for the theory of quasiperiodic cocycles, extending known results for cocycles taking values on certain compact groups (see [K1] for the case of SU(2)). They fit with the Palis conjecture for general dynamical systems [Pa], and have a strong analogy with the work of Lyubich in the quadratic family [Ly], generalized in [ALM].

More importantly, reducible and nonuniformly hyperbolic systems can be eficiently described through a wide variety of methods, especially in the analytic case. With respect to reducible systems, the dynamics of the cocycle itself is of course very simple, and the use of KAM theoretical methods ([DiS], [E1]) allowed also a good comprehension of their perturbations. With respect to nonuniformly hyperbolic systems, there has been recently lots of success in the application of subtle properties of subharmonic functions ([BG], [GS], [BJ1]) to obtain large deviation estimates with important consequences (such as regularity properties of the Lyapunov exponent).

1.1. Application to Schrodinger operators.¨ We now discuss the application of the previous results to the quasiperiodic Schr¨odinger operator

$$
H _ {v, \alpha , x} u (n) = u (n + 1) + u (n - 1) + v (x + \alpha n) u (n), \quad u \in l ^ {2} (\mathbb {Z}),\tag{1.9}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>For the case of cocycles nonhomotopic to the identity, see [AK1].</span></small>

where$\alpha \in \mathbb { R } \setminus \mathbb { Q } , x \in \mathbb { R }$and$v : \mathbb { R } / \mathbb { Z } \to \mathbb { R } { \mathrm { ~ i s ~ } } C ^ { \omega }$. The properties of$H _ { v , \alpha , x }$are closely connected to the properties of the family of cocycles$( \alpha , S _ { v , E } ) , E \in \mathbb { R }$ Notice for instance that if$( u _ { n } ) _ { n \in \mathbb { Z } }$is a solution of$H _ { v , \alpha , x } u = E u$then

$$
\left( \begin{array}{c c} E - v (x + n \alpha) & - 1 \\ 1 & 0 \end{array} \right) \cdot \binom{u (n)}{u (n - 1)} = \binom{u (n + 1)}{u (n)}.\tag{1.10}
$$

Let Σ be the spectrum of$H _ { v , \alpha , x }$. It is well known (see [JM]) that

(1.11)$\Sigma = \{ E \in \mathbb { R } , ( \alpha , S _ { v , E } )$is not uniformly hyperbolic},

so that$\Sigma = \Sigma ( v , \alpha )$does not depend on x.

Let$\Sigma _ { s c } = \Sigma _ { s c } ( \alpha , v , x )$(respectively,$\Sigma _ { a c } , \ \Sigma _ { p p } )$be (the support of) the singular continuous (respectively, absolutely continuous, pure point) part of the spectrum of$H _ { v , \alpha , x } .$

It has been shown by Last-Simon ([LS], Theorem 1.5) that$\Sigma _ { a c }$does not depend on x for$\alpha \in \mathbb { R } \setminus \mathbb { Q }$(there are no hypotheses on the smoothness of v beyond continuity). It is known that$\Sigma _ { s c }$and$\Sigma _ { p p }$do depend on x in general.

We will also introduce some decompositions of Σ that only depend on the cocycle, and hence are independent of x.

We split$\Sigma = \Sigma _ { 0 } \cup \Sigma _ { + }$in the parts corresponding to zero Lyapunov exponent and positive Lyapunov exponent for the cocycle$( \alpha , S _ { v , E } )$. By [BJ1],$\Sigma _ { 0 }$ is closed.

Let$\Sigma _ { r }$be the set of$E \in \Sigma$such that$( \alpha , S _ { v , E } )$is C<sup>ω</sup>-reducible. It is easy to see that$\Sigma _ { r } \subset \Sigma _ { 0 }$

Notice that by the Ishii-Pastur Theorem (see [I] and [P]), we have$\Sigma _ { a c } \subset \Sigma _ { 0 }$

By Theorem A,$\Sigma _ { 0 } \setminus \Sigma _ { r }$has zero Lebesgue measure if$\alpha ~ \in ~ \mathrm { R D C }$and $v \in C ^ { \omega }$. One way to interpret$| \Sigma _ { 0 }  \setminus \Sigma _ { r } | = 0$(using the Ishii-Pastur Theorem) is that generalized eigenfunctions in the essential support of the absolutely continuous spectrum are (very regular) Bloch waves. This already gives (in the particular cases under consideration) strong versions of some conjectures in the literature (see for instance the discussion after Theorem 7.1 in [DeS]). (Analogous statements hold in the continuous time case.)

Another immediate application of Theorem A is a nonperturbative version of Eliasson’s result stated in Proposition 1.2. It is based on the following nonperturbative result:

Proposition 1.3 (Bourgain-Jitomirskaya). Let$\alpha \in \mathrm { D C } , v \in C ^ { \omega }$. There exists$\lambda _ { 0 } = \lambda _ { 0 } ( v ) > 0$(only depending on the bounds of v, but not on α) such that$i f \mid \lambda \mid < \lambda _ { 0 }$, then the spectrum of$H _ { \lambda v , \alpha , x }$is purely absolutely continuous for almost every x.

Theorem 1.4. Let$\alpha \in \mathrm { R D C } , v \in C ^ { \omega }$. There exists$\lambda _ { 0 } > 0$(which may be taken the same as in the previous proposition) such that$i f \left| \lambda \right| < \lambda _ { 0 }$, then $( \alpha , S _ { \lambda v , E } )$is reducible for almost every E.

Proof. By the previous proposition,$\Sigma _ { a c } = \Sigma$, so that$\Sigma _ { + } = \emptyset$

There are several other interesting results which can be concluded easily from Theorem A and current results and techniques:

(1) Zero Lebesgue measure of$\Sigma _ { s c }$for almost every frequency,

(2) Persistence of absolutely continuous spectrum under perturbations of the potential,

(3) Continuity of the Lebesgue measure of Σ under perturbations of the potential.

Although the key ideas behind those results are quite transparent (given the appropriate background), a proper treatment would take us too far from the proof of Theorem A, which is the main goal of this paper. We will thus concentrate on a particular case which provides one of the most striking applications of Theorem A. For the applications mentioned above (and others), see [AK2].

1.1.1. Almost Mathieu. Certainly the most studied family of potentials in the literature is$v ( \theta ) = \lambda \cos 2 \pi \theta , \lambda > 0$. In this case,$H _ { v , \alpha , x }$is called the Almost Mathieu Operator.

The Aubry-Andr´e conjecture on the measure of the spectrum of the Almost Mathieu Operator states that the measure of the spectrum of$H _ { \lambda \cos 2 \pi \theta , \alpha , x }$ is$| 4 - 2 \lambda |$for every$\alpha \in \mathbb { R } \setminus \mathbb { Q } , x \in \mathbb { R } { \mathrm { ~ ( s e e ~ [ A A ] ) } } .$.<sup>4</sup> There is a long story of developments around this problem, which led to several partial results ([HS], [AMS], [L], [JK]). In particular, it has already been proved for every$\lambda \neq 2$ (see [JK]), and for every α not of constant$\mathrm { t y p e ^ { 5 } }$[L]. However, for α, say, the golden mean, and$\lambda = 2$, where one should prove zero Lebesgue measure of the spectrum, previous to this work, it was still unknown even whether the spectrum has empty interior.

Using Theorem A, we can deal with the last cases (which are also Problem 5 of [Si2]).

Theorem 1.5.The spectrum of$H _ { \lambda \cos 2 \pi \theta , \alpha , x }$has Lebesgue measure |4−2λ| for every$\alpha \in \mathbb { R } \setminus \mathbb { Q }$

Proof. As stated above, it is enough to consider$\lambda = 2$and α of constant type, in particular$\alpha ~ \in ~ \mathrm { R D C }$. Let Σ be the spectrum of$H _ { 2 \cos 2 \pi \theta , \alpha , x } .$. By Corollary 2 of [BJ1],$\Sigma _ { + } ~ = ~ \emptyset$. By Theorem$\mathrm { A } .$, for almost every$E \in \Sigma _ { 0 }$ $( \alpha , S _ { 2 \cos 2 \pi \theta , E } )$is$C ^ { \omega } .$-reducible. Thus, it is enough to show that$\left( \alpha , S _ { 2 \cos 2 \pi \theta , E } \right)$ is not$C ^ { \omega } .$-reducible for every$E \in \Sigma$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">λ = 2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">α ∈ R</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">if and only if .α <sub>κ>0</sub>RDC(κ, 1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>The “critical case”  can be traced even further back to Hofstadter [H].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>A number α  R is said to be of constant type if the coeficients of its continued fraction expansion are bounded. It follows that α is of constant type if and only if α∈ ∪κ>0<sup>DC(κ,</sup> <sup>1)</sup></span></small>

Assume this is not the case, that is,$\left( \alpha , S _ { 2 \cos 2 \pi \theta , E } \right)$is reducible for some $E \in \Sigma$. To reach a contradiction, we will approximate the potential 2 cos 2πθ by λ cos 2πθ with$\lambda > 2$close to 2. Then, by Theorem A of [E1], if$( \lambda , E ^ { \prime } )$ is suficiently close to$( 2 , E )$, either$\left( \alpha , S _ { \lambda \cos 2 \pi \theta , E ^ { \prime } } \right)$is uniformly hyperbolic or $L ( \alpha , S _ { \lambda \cos 2 \pi \theta , E ^ { \prime } } ) = 0$. In particular (since the spectrum depends continuously on the potential), there exists$E ^ { \prime } \in \mathbb { R }$such that$L ( \alpha , S _ { \lambda \cos 2 \pi \theta , E ^ { \prime } } ) = 0$. But it is well known, see [H], that the Lyapunov exponent of$S _ { \lambda \cos 2 \pi \theta , E ^ { \prime } }$is bounded from below by max$\{ \ln { \frac { \lambda } { 2 } } , 0 \} > 0$and the result follows.□

Remark 1.6. Barry Simon has pointed out to us an alternative argument based on duality that shows that if$\alpha \in \mathbb { R } \setminus \mathbb { Q }$and if$E \in \Sigma = \Sigma ( 2 \cos 2 \pi \theta , \alpha )$ then the cocycle$\left( \alpha , S _ { 2 \cos 2 \pi \theta , E } \right)$is not$C ^ { \omega } .$-reducible. Indeed, if$( \alpha , S _ { v , E } )$is $C ^ { \omega } .$-reducible and$E \in \Sigma$, then (by duality) there exists$x \in \mathbb { R }$such that E is an eigenvalue for$H _ { 2 \cos 2 \pi \theta , \alpha , x } ,$and the corresponding eigenvector decays exponentially, hence$L ( \alpha , S _ { v , E } ) > 0$which gives a contradiction. (This argument actually can be used to show that$( \alpha , S _ { v , E } )$is not$C ^ { 1 } { \mathrm { - r e d u c i b l e . } } )$

By [GJLS], we get:

Corollary 1.6. The spectrum of$H _ { 2 \cos 2 \pi \theta , \alpha , x }$is purely singular continuous for every$\alpha \in \mathbb { R } \setminus \mathbb { Q }$, and for almost every$x \in \mathbb { R } / \mathbb { Z }$

Theorem A also gives a fairly precise dynamical picture for$\lambda < 2$(completing the spectral picture obtained by Jitomirskaya in [J]):

Theorem 1.7.Let$\lambda { < } 2 , \alpha { \in } \mathrm { R D C }$. For almost every$E \in \mathbb { R } , ( \alpha , S _ { \lambda \cos 2 \pi \theta , E } )$ is reducible.

Proof. By Corollary 2 of [BJ1], the Lyapunov exponent is zero on the spectrum. The result is now a consequence of Theorem A.□

1.2. Outline of the proof of Theorem A. The proof has some distinct steps, and is based on a renormalization scheme. This point of view, which has already been used in the study of reducibility properties of quasiperiodic cocycles with values in SU(2) and SL(2, R), has proved to be very useful in the nonperturbative case (see [K1], [K2]). However, the scheme we present in this paper is somehow simpler and fits better (at least in the$\mathrm { S L } ( 2 , \mathbb { R } )$case) with the general renormalization philosophy (see [S] for a very nice description of this point of view on renormalization):

(1) The starting point is the theory of Kotani<sup>6</sup>. For almost every energy E, if the Lyapunov exponent of$( \alpha , S _ { v , E } )$is zero, then the cocycle is

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>This step holds in much greater generality, namely for cocycles over ergodic transformations.</span></small>

$L ^ { 2 } .$-conjugate to a cocycle in SO(2, R). Moreover, the fibered rotation number of the cocycle is Diophantine with respect to α. (The set$\Delta$of those energies will be precisely the set of energies for which we will be able to conclude reducibility.)

(2) We now consider a smooth cocycle$( \alpha , A )$which is$L ^ { 2 } .$-conjugate to rotations. An explicit estimate allows us to control the derivatives of iterates of the cocycle restricted to certain small intervals.

(3) After introducing the notion of renormalization of cocycles, we interpret item (2) as$^ { 6 6 } a$priori bounds” (or precompactness) for a sequence of renormalizations$( \alpha _ { n _ { k } } , A ^ { ( n _ { k } ) } )$.

(4) The recurrent Diophantine condition for α allows us to take$\alpha _ { n _ { k } }$uniformly Diophantine, so that the limits of renormalization are cocycles $( { \hat { \alpha } } , { \hat { A } } )$where ˆα satisfies a Diophantine condition. Those limits are essentially (that is, modulo a constant conjugacy) cocycles in$\mathrm { S O } ( 2 , \mathbb { R } )$, and are trivial to analyze: they are always reducible.

(5) Since$\operatorname* { l i m } ( \alpha _ { n _ { k } } , A ^ { ( n _ { k } ) } )$is reducible, Eliasson’s theorem [E1] allows us to conclude that some renormalization$( \alpha _ { n _ { k } } , A ^ { ( n _ { k } ) } )$must be reducible, provided the fibered rotation number of$( \alpha _ { n _ { k } } , A ^ { ( n _ { k } ) } )$is Diophantine with respect to$\alpha _ { n _ { k } }$

(6) This last condition is actually equivalent to the fibered rotation number of$( \alpha , A )$being Diophantine with respect to α. It is easy to see that reducibility is invariant under renormalization and so$( \alpha , A )$is itself reducible.

We conclude that for almost every$E \in \mathbb { R }$such that$L ( \alpha , S _ { v , E } ) = 0$, the cocycle$( \alpha , S _ { v , E } )$is reducible, which is equivalent to Theorem A by Remark 1.3.

The above strategy uses$\alpha \in \mathrm { R D C }$in order to take good limits of renormalization. It would be interesting to try to obtain results under the weaker condition$\alpha \in \mathrm { D C }$by working directly with deep renormalizations (without considering limits).

Remark 1.7. Renormalization methods have been previously applied to the study of quasiperiodic Schr¨odinger operators, see for instance [BF], [FK] and [HS]. While the notions used by Helfer-Sj¨ostrand are quite diferent from ours, the “monodromization techniques” of Buslaev-Fedotov-Klopp correspond to essentially the same notion of renormalization used here. An important conceptual diference is in the use of renormalization: we are interested in the dynamics of the renormalization operator itself, in a spirit close to works in one-dimensional dynamics (see for instance [Ly], [Y], [S]).

## 2. Parameter exclusion

2.1.$L ^ { 2 } \ – e s t i m a t e s .$. We say that$( \alpha , A )$is$L ^ { 2 } .$-conjugated to a cocycle of rotations if there exists a measurable${ B : \mathbb { R } / \mathbb { Z } } \to \mathrm { S L } ( 2 , \mathbb { R } )$such that$\| B \| \in L ^ { 2 }$ and

$$
B (x + \alpha) A (x) B (x) ^ {- 1} \in \mathrm{SO} (2, \mathbb {R}).\tag{2.1}
$$

Theorem 2.1. Let$v : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$be continuous. Then for almost every $E ,$either$L ( \alpha , S _ { v , E } ) > 0 \ o r \ S _ { v , E }$is$L ^ { 2 } .$-conjugated to a cocycle of rotations.

Proof. Looking at the projectivized action of$( \alpha , S _ { v , E } )$on the upper halfplane H, one sees that the existence of an$L ^ { 2 }$conjugacy to rotations is equivalent to the existence of a measurable invariant section<sup>7</sup>$m ( \cdot , E ) : \mathbb { R } / \mathbb { Z } \to$H satisfying$\textstyle \int _ { \mathbb { R } / \mathbb { Z } } { \frac { 1 } { \Im m ( x , E ) } } d x \ < \ \infty$This holds for almost every$E$such that $L ( \alpha , S _ { v , E } ) = 0$by Kotani Theory, as described in$[ \mathrm { S i l } ] ^ { 8 }$(the measurable invariant section m we want is given by$\frac { - 1 } { m _ { - } }$in the notation of [Si1]).□

It turns out that this result generalizes to the setting of Theorem$\mathrm { A ^ { \prime } } { : }$

Theorem 2.2. Let$A : \mathbb { R } / \mathbb { Z } \to { \mathrm { S L } } ( 2 , \mathbb { R } )$be continuous. Then for almost every$\theta \in \mathbb { R }$, either$L ( \alpha , R _ { \theta } A ) > 0 \ o r \ ( \alpha , R _ { \theta } A )$is$L ^ { 2 }$-conjugated to a cocycle of rotations.

The proof of this generalization is essentially the same as in the Schr¨odinger case. We point the reader to [AK1] for a discussion of this and further generalizations.

Remark 2.1. Both theorems above are valid in a much more general setting, namely for cocycles over transformations preserving a probability measure. The requirement on the cocycle is the least to speak of Lyapunov exponents (and Oseledets theory), namely integrability of the logarithm of the norm.

2.2. Fibered rotation number. Besides the Lyapunov exponent, there is one important invariant associated to continuous cocycles which are homotopic to the identity. This invariant, called the fibered rotation number will be denoted by$\rho ( \alpha , A ) \in \mathbb { R } / \mathbb { Z }$, and was introduced in [H], [JM] (we recall its definition in Appendix$\mathrm { A } )$. The fibered rotation number is a continuous function of$( \alpha , A )$ where$( \alpha , A )$varies in the space of continuous cocycles which are homotopic to the identity. Another important elementary fact is that both$E \mapsto - \rho { \left( \alpha , S _ { v , E } \right) }$ and$\theta \mapsto \rho ( \alpha , R _ { \theta } A )$have nondecreasing lifts$\mathbb { R } \to \mathbb { R }$, and in particular, those functions have nonnegative derivatives almost everywhere. The following result was proved in [JM], in the continuous time case, and in [DeS], in the discrete time case used here (and where an optimal estimate is given).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7That</sup> <sup>is</sup> <sup>S</sup>v,E<sup>(x)</sup> · <sup>m(x,</sup> <sup>E) =</sup> <sup>m(x</sup> <sup>+</sup> <sup>α,</sup> <sup>E).</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>This reference was pointed out to us by Hakan Eliasson.</span></small>

Theorem 2.3. Let$v \in C ^ { 0 } ( \mathbb { R } / \mathbb { Z } , \mathbb { R } )$. Then for almost every E such that $L ( \alpha , S _ { v , E } ) = 0$2

$$
\frac {d}{d E} \rho (\alpha , S _ {v, E}) <   0.\tag{2.2}
$$

This result (and proof) also generalize to the setting of Theorem$\mathrm { A } ^ { \prime }$(see [AK1] for further generalizations):

Theorem 2.4. Let$A \in C ^ { 0 } ( \mathbb { R } / \mathbb { Z } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$be continuous and homotopic to the identity. Then for almost every E such that$L ( \alpha , R _ { \theta } A ) = 0$

$$
\frac {d}{d \theta} \rho (\alpha , R _ {\theta} A) > 0.\tag{2.3}
$$

Remark 2.2. In the Schr¨odinger case, it is possible to show that the fibered rotation number is a surjective function (of E) onto$[ 0 , 1 / 2 ]$. In [AS] it is also shown that$N ( E ) = 1 - 2 \rho ( \alpha , S _ { v , E } )$can be interpreted as the integrated density of states.

The arithmetic properties of the fibered rotation number are also important for the analysis of cocycles$( \alpha , A )$. Fix$\alpha \in \mathbb { R }$. Let us say that$\beta \in \mathbb { R } / \mathbb { Z }$is Diophantine with respect to α if there exists$\kappa > 0 , \tau > 0$such that

$$
\| 2 \beta - k \alpha \| _ {\mathbb {R} / \mathbb {Z}} \geq \kappa (1 + | k |) ^ {- \tau}, \quad k \in \mathbb {Z},\tag{2.4}
$$

where$\| \cdot \| _ { \mathbb { R } / \mathbb { Z } }$denotes the distance to the nearest integer.$\mathrm { I f } \ \tau > 1$then the Lebesgue measure of the set of$\beta \in \mathbb { R } / \mathbb { Z }$which satisfy (2.4) is at least$1 - 2 \frac { \tau + 1 } { \tau - 1 } \kappa$ In particular, Lebesgue almost every$\beta$is Diophantine with respect to α. By Theorems 2.3 and 2.4 we conclude:

Corollary 2.5. Let$\alpha \in \mathrm { D C } , v \in C ^ { 0 } (  { \mathbb { R } } /  { \mathbb { Z } } ,  { \mathbb { R } } )$. Then for almost every $E \in \mathbb { R }$such that$L ( \alpha , S _ { v , E } ) = 0 , \rho ( \alpha , S _ { v , E } )$is Diophantine with respect to α.

Corollary 2.6. Let$\alpha \in \mathrm { D C } , A \in C ^ { 0 } (  { \mathbb { R } } /  { \mathbb { Z } } , \mathrm { S L } ( 2 ,  { \mathbb { R } } ) )$. Then for almost every$\theta \in \mathbb { R }$such that$L ( \alpha , R _ { \theta } A ) = 0 , \rho ( \alpha , R _ { \theta } A )$is Diophantine with respect to α.

The fibered rotation number and its arithmetic properties play a role in the following result of Eliasson [E1]:

Theorem 2.7. Let$( \alpha , A ) \in \mathbb { R } \times C ^ { \omega } ( \mathbb { R } / \mathbb { Z } , \operatorname { S L } ( 2 , \mathbb { R } ) )$). Assume that:

(1)$\alpha \in \mathrm { D C } ( \kappa , \tau )$for some$\kappa > 0 , \tau > 0$

(2)$\rho ( \alpha , A )$is Diophantine with respect to$\alpha ,$

(3) A admits a holomorphic extension to some strip$\mathbb { R } / \mathbb { Z } \times ( - \epsilon , \epsilon )$2

(4) A is suficiently close to a constant$\hat { A } \in \mathrm { S L } ( 2 , \mathbb { R } )$

$$
\sup _ {z \in \mathbb {R} / \mathbb {Z} \times (- \epsilon , \epsilon)} \| A (z) - \hat {A} \| <   \delta = \delta (\kappa , \tau , \epsilon , \hat {A}).\tag{2.5}
$$

Then$( \alpha , A )$is reducible.

This theorem was originally proved in the case of diferential equations, but the adaptation to our setting is immediate. For further generalizations, see$\mathrm { [ A K 2 ] }$

## 3. Estimates for derivatives

In this section, we will assume that$( \alpha , A )$is$L ^ { 2 } .$-conjugated to a cocycle of rotations. There exist measurable${ B : \mathbb { R } / \mathbb { Z } \to \mathrm { S L } ( 2 , \mathbb { R } ) }$and$R : \mathbb { R } / \mathbb { Z } \to$ $\mathrm { S O } ( 2 , \mathbb { R } )$such that

$$
(3. 1) \quad \forall x \in \mathbb {R} / \mathbb {Z}, \quad A (x) = B (x + \alpha) R (x) B (x) ^ {- 1} \quad \mathrm{and} \quad \int_ {\mathbb {R} / \mathbb {Z}} \phi (x) d x <   \infty
$$

where we set$\phi ( \boldsymbol { x } ) = \| \boldsymbol { B } ( \boldsymbol { x } ) \| ^ { 2 } = \| \boldsymbol { B } ( \boldsymbol { x } ) ^ { - 1 } \| ^ { 2 }$(here and in what follows,$\mathbb { R } ^ { 2 }$is supplied with the Euclidean norm and the space of real$2 \times 2$matrices$\operatorname { M } ( 2 , \mathbb { R } )$ is supplied with the operator norm).

We introduce the maximal function$S ( \cdot )$of φ:

$$
S (x) = \sup _ {n \geq 1} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \phi (x + k \alpha).\tag{3.2}
$$

Since the dynamics of$x \mapsto x + \alpha$is ergodic on$\mathbb { R } / \mathbb { Z }$endowed with Lebesgue measure, the Maximal Ergodic Theorem gives us the weak-type inequality

$$
\forall M > 0, \quad \operatorname{Leb} (\{x \in \mathbb {R} / \mathbb {Z}, S (x) > M \}) \leq \frac {1}{M} \int_ {\mathbb {R} / \mathbb {Z}} \phi (x) d x,\tag{3.3}
$$

and for$\mathrm { a . e \ } x _ { 0 } \in \mathbb { R } / \mathbb { Z }$the quantity$S ( x _ { 0 } )$is finite.

If$X \in \operatorname { G L } ( 2 , \mathbb { R } )$, we let$\operatorname { A d } ( X )$be the linear operator in$\operatorname { M } ( 2 , \mathbb { R } )$which is given by$\operatorname { A d } ( X ) \cdot Y = X \cdot Y \cdot X ^ { - 1 }$. Notice that the operator norm of$\operatorname { A d } ( X )$ satisfies the bound$\| \operatorname { A d } ( X ) \| \leq \| X \| \cdot \| X ^ { - 1 } \|$

Lemma 3.1. Assume that A is Lipschitz (with constant$\operatorname { L i p } ( A ) )$. Then for every$x _ { 0 } , x \in \mathbb { R } / \mathbb { Z }$such that$S ( x _ { 0 } ) < \infty .$

$$
\left\| A _ {n} \left(x _ {0}\right) ^ {- 1} \left(A _ {n} (x) - A _ {n} \left(x _ {0}\right)\right) \right\| \leq e ^ {n \left| x - x _ {0} \right| \| A \| _ {C ^ {0}} \operatorname{Lip} (A) \phi \left(x _ {0}\right) S \left(x _ {0}\right)} - 1,\tag{3.4}
$$

and in particular

$$
\| A _ {n} (x) \| \leq e ^ {n | x - x _ {0} | \| A \| _ {C ^ {0}} \operatorname{Lip} (A) S (x _ {0}) \phi (x _ {0})} \left(\phi (x _ {0}) \phi (x _ {0} + n \alpha)\right) ^ {1 / 2}.\tag{3.5}
$$

Proof. We compute$I _ { n } ( x _ { 0 } , x ) : = A _ { n } ( x _ { 0 } ) ^ { - 1 } ( A _ { n } ( x ) - A _ { n } ( x _ { 0 } ) )$

$$
\begin{array}{l} I _ {n} (x _ {0}, x) \\ = A _ {n} (x _ {0}) ^ {- 1} \left(\prod_ {k = n - 1} ^ {0} \left(A (x _ {0} + k \alpha) + (A (x + k \alpha) - A (x _ {0} + k \alpha))\right) - A _ {n} (x _ {0})\right) \\ = \sum_ {r = 1} ^ {n} \sum_ {0 \leq i _ {r} <   \dots <   i _ {1} \leq n - 1} \prod_ {j = 1} ^ {r} (\operatorname{Ad} (A _ {i _ {j}} (x _ {0}) ^ {- 1}) \cdot H _ {i _ {j}} (x _ {0}, x)) \end{array}\tag{3.6}
$$

where we have set

$$
H _ {i} (x _ {0}, x) = A (x _ {0} + i \alpha) ^ {- 1} \cdot (A (x + i \alpha) - A (x _ {0} + i \alpha)),\tag{3.7}
$$

so that

$$
\| H _ {i} (x _ {0}, x) \| \leq \| A \| _ {C ^ {0}} \mathrm{Lip} (A) | x - x _ {0} |.\tag{3.8}
$$

The assumptions we made give

$$
\| A _ {i} (x _ {0}) \| = \| A _ {i} (x _ {0}) ^ {- 1} \| \leq \| B (x _ {0} + i \alpha) ^ {- 1} \| \cdot \| B (x _ {0}) \|;\tag{3.9}
$$

that is,

$$
\left\| \operatorname{Ad} (A _ {i} (x _ {0}) ^ {- 1}) \right\| \leq (\left\| B (x _ {0} + i \alpha) ^ {- 1} \right\| \cdot \left\| B (x _ {0}) \right\|) ^ {2} = \phi (x _ {0}) \phi (x _ {0} + i \alpha).\tag{3.10}
$$

Thus

(3.11)

$$
\begin{array}{l} \| I _ {n} (x _ {0}, x) \| \leq \sum_ {r = 1} ^ {n} \sum_ {0 \leq i _ {r} <   \ldots <   i _ {1} \leq n - 1} \prod_ {j = 1} ^ {r} \bigg (\| A \| _ {C ^ {0}} \mathrm{Lip} (A) | x - x _ {0} | \phi (x _ {0}) \phi (x _ {0} + i _ {j} \alpha) \bigg) \\ = - 1 + \prod_ {k = 0} ^ {n - 1} \bigg (1 + \| A \| _ {C ^ {0}} \mathrm{Lip} (A) | x - x _ {0} | \phi (x _ {0}) \phi (x _ {0} + k \alpha) \bigg) \\ \leq - 1 + \exp \bigg (\sum_ {k = 0} ^ {n - 1} \| A \| _ {C ^ {0}} \mathrm{Lip} (A) | x - x _ {0} | \phi (x _ {0}) \phi (x _ {0} + k \alpha) \bigg). \end{array}
$$

Hence for every$x \in \mathbb { R } / \mathbb { Z }$

$$
\left\| A _ {n} \left(x _ {0}\right) ^ {- 1} \left(A _ {n} (x) - A _ {n} \left(x _ {0}\right)\right) \right\| \leq e ^ {n \left| x - x _ {0} \right| \| A \| _ {C ^ {0}} \operatorname{Lip} (A) \phi \left(x _ {0}\right) S \left(x _ {0}\right)} - 1,\tag{3.12}
$$

which implies

$$
\begin{array}{l} \| A _ {n} (x) \| \leq e ^ {n | x - x _ {0} | \| A \| _ {C ^ {0}} \mathrm{Lip} (A) \phi (x _ {0}) S (x _ {0})} \| A _ {n} (x _ {0}) \| \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{3.13}
$$

We now give estimates for the derivatives.

Lemma 3.2. Assume that$A : \mathbb { R } / \mathbb { Z } \to { \mathrm { S L } } ( 2 , \mathbb { R } )$is of class$C ^ { k } \ ( 1 \leq k$ $\leq \infty )$. Then for every$0 \leq r \leq k _ { \cdot }$and any$x _ { 0 } , x \in \mathbb { R } / \mathbb { Z }$such that$S ( x _ { 0 } ) < \infty$，

$$
\| (\partial^ {r} A _ {n}) (x) \| \leq C ^ {r} n ^ {r} \phi (x _ {0} + n \alpha) ^ {1 / 2} \bigg (c _ {1} (x _ {0}) e ^ {n c _ {2} (x _ {0}) | x - x _ {0} |} \bigg) ^ {r + \frac {1}{2}} \| \partial^ {r} A \| _ {C ^ {0}}\tag{3.14}
$$

where C is an absolute constant and

$$
\begin{array}{l} c _ {1} (x _ {0}) = \phi (x _ {0}) S (x _ {0}) \| A \| _ {C ^ {0}} ^ {2}, \\ c _ {2} (x _ {0}) = 2 S (x _ {0}) \phi (x _ {0}) \| A \| _ {C ^ {0}} \| \partial A \| _ {C ^ {0}}. \end{array}\tag{3.15}
$$

Proof. We compute

$$
\partial^ {r} A _ {n} (x) = \partial^ {r} \left(\prod_ {k = n - 1} ^ {0} A (\cdot + k \alpha)\right) (x)\tag{3.16}
$$

which by Leibniz formula is a sum of$n ^ { r }$terms of the form

$$
\begin{array}{l} I _ {(i ^ {*})} (x) = \left(\prod_ {l = n - 1} ^ {i _ {1} + 1} A (x + l \alpha)\right) \cdot \partial^ {m _ {1}} A (x + i _ {1} \alpha) \cdot \left(\prod_ {l = i _ {1} - 1} ^ {i _ {2} + 1} A (x + l \alpha)\right) \\ \qquad \qquad \qquad \cdot \partial^ {m _ {2}} A (x + i _ {2} \alpha) \cdot \left(\prod_ {l = i _ {2} - 1} ^ {i _ {3} + 1} A (x + l \alpha)\right) \dots \\ \qquad \qquad \qquad \cdot \partial^ {m _ {s}} A (x + i _ {s} \alpha) \cdot \left(\prod_ {l = i _ {s} - 1} ^ {0} A (x + l \alpha)\right) \end{array}\tag{3.17}
$$

where$i ^ { * }$runs through${ \mathcal { T } } = \{ 0 , \dots , n - 1 \} ^ { \{ 1 , \dots , r \} }$and where$s \leq r$and$\{ i _ { 1 } , \dots , i _ { s } \}$ $= i ^ { * } ( \{ 1 , . . . , r \} )$satisfy$n - 1 \geq i _ { 1 } > i _ { 2 } > \cdot \cdot \cdot i _ { s } \geq 0$and$m _ { l } = \# ( i ^ { * } ) ^ { - 1 } ( i _ { l } )$. (Notice that$m _ { 1 } + . . . + m _ { s } = r . )$Each term$I _ { ( i ^ { * } ) }$can be written

$$
\begin{array}{l} I _ {(i ^ {*})} (x) = A _ {n} (x) \cdot \mathrm{Ad} \left(A _ {i _ {1}} (x) ^ {- 1}\right) \cdot \bigg (A (x + i _ {1} \alpha) ^ {- 1} \partial^ {m _ {1}} A (x + i _ {1} \alpha) \bigg) \\ \qquad \cdot \mathrm{Ad} \left(A _ {i _ {2}} (x) ^ {- 1}\right) \cdot \bigg (A (x + i _ {2} \alpha) ^ {- 1} \partial^ {m _ {2}} A (x + i _ {2} \alpha) \bigg) \dots \\ \qquad \cdot \mathrm{Ad} \left(A _ {i _ {s}} (x) ^ {- 1}\right) \cdot \bigg (A (x + i _ {s} \alpha) ^ {- 1} \partial^ {m _ {s}} A (x + i _ {s} \alpha) \bigg). \end{array}\tag{3.18}
$$

From the previous lemma,

(3.19)

$$
\left\| A _ {i _ {p}} (x) \right\| \leq \bigl (K \phi (x _ {0}) \phi (x _ {0} + i _ {p} \alpha) \bigr) ^ {1 / 2},\tag{3.20}
$$

$$
\left\| \operatorname{Ad} \left(A _ {i _ {p}} (x)\right) \right\| \leq \left\| A _ {i _ {p}} (x) \right\| ^ {2} \leq K \phi (x _ {0}) \phi (x _ {0} + i _ {p} \alpha)
$$

where

$$
K = e ^ {2 n | x - x _ {0} | \phi (x _ {0}) S (x _ {0}) \| A \| _ {C ^ {0}} \| \partial A \| _ {C ^ {0}}}.\tag{3.21}
$$

Hence we get the following bound

$$
\| I _ {(i ^ {*})} (x) \| \leq \bigg (K \phi (x _ {0}) \phi (x _ {0} + n \alpha) \bigg) ^ {1 / 2} \prod_ {p = 1} ^ {s} \bigg (K \phi (x _ {0}) \phi (x _ {0} + i _ {p} \alpha) \| A \| _ {C ^ {0}} \| \partial^ {m _ {p}} A \| _ {C ^ {0}} \bigg).\tag{3.22}
$$

From this and the convexity (Hadamard-Kolmogorov) inequalities [Ko]

$$
\| \partial^ {m} A \| _ {C ^ {0}} \leq C \| A \| _ {0} ^ {1 - (m / r)} \| \partial^ {r} A \| _ {C ^ {0}} ^ {\frac {m}{r}}, \quad 0 \leq m \leq r,\tag{3.23}
$$

we deduce (using$\begin{array} { r } { \sum _ { p = 1 } ^ { s } m _ { p } = r ) } \end{array}$

$$
\begin{array}{l} \| I _ {(i ^ {*})} (x) \| \leq \bigg (K \phi (x _ {0}) \phi (x _ {0} + n \alpha) \bigg) ^ {1 / 2} \\ \qquad \times K ^ {s} \phi (x _ {0}) ^ {s} \| A \| _ {C ^ {0}} ^ {s} \prod_ {p = 1} ^ {s} \bigg (C \| A \| _ {C ^ {0}} ^ {1 - \frac {m _ {p}}{r}} \| \partial^ {r} A \| _ {C ^ {0}} ^ {\frac {m _ {p}}{r}} \phi (x _ {0} + i _ {p} \alpha) \bigg) \\ \qquad \leq C ^ {s} K ^ {s + \frac {1}{2}} \phi (x _ {0}) ^ {s + \frac {1}{2}} \phi (x _ {0} + n \alpha) ^ {1 / 2} \| A \| _ {C ^ {0}} ^ {2 s - 1} \| \partial^ {r} A \| _ {C ^ {0}} \prod_ {p = 1} ^ {s} \phi (x _ {0} + i _ {p} \alpha) \\ \qquad \leq C ^ {r} \big (K \| A \| _ {C ^ {0}} ^ {2} \phi (x _ {0}) \big) ^ {r + \frac {1}{2}} \phi (x _ {0} + n \alpha) ^ {1 / 2} \| \partial^ {r} A \| _ {C ^ {0}} \prod_ {p = 1} ^ {s} \phi (x _ {0} + i _ {p} \alpha), \end{array}\tag{3.24}
$$

so that

$$
\begin{array}{l} \| \partial^ {r} A _ {n} (x) \| \leq \sum_ {i ^ {*} \in \mathcal {I}} \| I _ {(i ^ {*})} (x) \| \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad C ^ {r} \big (K \| A \| _ {C ^ {0}} ^ {2} \phi (x _ {0}) \big) ^ {r + \frac {1}{2}} \phi (x _ {0} + n \alpha) ^ {1 / 2} \| \partial^ {r} A \| _ {C ^ {0}} \\ \qquad \qquad \qquad \times \sum_ {i ^ {*} \in \mathcal {I}} \phi (x _ {0} + i _ {1} \alpha) \dots \phi (x _ {0} + i _ {s} \alpha). \end{array}\tag{3.25}
$$

But the last sum in this estimate satisfies the inequality

$$
\begin{array}{l l} & \sum_ {i ^ {*} \in \mathcal {I}} \phi (x _ {0} + i _ {1} \alpha) \dots \phi (x _ {0} + i _ {s} \alpha) \\ & \qquad \qquad \qquad \leq \bigg (\phi (x _ {0}) + \ldots + \phi (x _ {0} + (n - 1) \alpha) \bigg) ^ {r} \leq n ^ {r} S (x _ {0}) ^ {r} \end{array}\tag{3.26}
$$

(recall that$\phi \geq 1 )$which implies the result.

We can now conclude easily:

Lemma 3.3. Assume that$A : \mathbb { R } / \mathbb { Z } \to { \mathrm { S L } } ( 2 , \mathbb { R } )$is${ \cal C } ^ { k } \ ( 1 \leq k \leq \infty )$. For almost every$x _ { * } \in \mathbb { R } / \mathbb { Z }$, there exists$K > 0 ,$, such that for every$d > 0$and for every$\begin{array} { r } { n > n _ { 0 } ( d ) , \ i f \| \alpha n \| _ { \mathbb { R } / \mathbb { Z } } \le \frac { d } { n } } \end{array}$, then

$$
\| \partial^ {r} A _ {n} (x) \| \leq K ^ {r + 1} n ^ {r} \| A \| _ {C ^ {r}}, \quad | x - x _ {*} | \leq \frac {d}{n}.\tag{3.27}
$$

Proof. Let$X \subset \mathbb { R } / \mathbb { Z }$be the set of all x such that$S ( x ) < \infty$where the x are measurable continuity points of$S$and$\phi .$. This means that for every$\epsilon > 0$ x is a density point of

$$
Y (x, \epsilon) = S ^ {- 1} (S (x) - \epsilon , S (x) + \epsilon) \cap \phi^ {- 1} (\phi (x) - \epsilon , \phi (x) + \epsilon).\tag{3.28}
$$

It is a classical fact that X has full Lebesgue Measure.

Fix$x _ { * } \in X , d > 0$and$\epsilon > 0$. If$n$is suficiently big then

$$
\left| Y (x _ {*}, \epsilon) \cap \left[ x _ {*} - \frac {2 d}{n}, x _ {*} + \frac {2 d}{n} \right] \right| \geq \frac {(4 - \epsilon) d}{n}.\tag{3.29}
$$

If$\begin{array} { r } { \| \alpha n \| _ { \mathbb { R } / \mathbb { Z } } < \frac { d } { n } } \end{array}$, this implies

$$
\left| \left(Y (x _ {*}, \epsilon) - \alpha n\right) \cap Y (x _ {*}, \epsilon) \cap \left[ x _ {*} - \frac {d}{n}, x _ {*} + \frac {d}{n} \right] \right| \geq \frac {(2 - 2 \epsilon) d}{n}.\tag{3.30}
$$

In particular, each point$\begin{array} { r } { x \in \left[ x _ { * } - \frac { d } { n } , x _ { * } + \frac { d } { n } \right] } \end{array}$is at distance at most$\textstyle { \frac { 2 \epsilon d } { n } }$from a point$x _ { 0 }$such that$x _ { 0 } \in Y ( x _ { * } , \epsilon )$and x<sub>0</sub>+αn$\in Y ( x _ { * } , \epsilon )$. In particular, for every $\delta > 0 , \mathrm { i f } \epsilon > 0$is suficiently small then$c _ { 1 } ( x _ { 0 } ) \leq c _ { 1 } ( x _ { * } ) + \delta , c _ { 2 } ( x _ { 0 } ) \leq c _ { 2 } ( x _ { * } ) + \delta$ where$c _ { 1 }$and$c _ { 2 }$are as in the previous lemma. The previous lemma implies that

$$
\begin{array}{l} \| (\partial^ {r} A _ {n}) (x) \| \leq C ^ {r} n ^ {r} \phi (x _ {0} + n \alpha) ^ {1 / 2} \left(c _ {1} (x _ {0}) e ^ {c _ {2} (x _ {0}) n | x - x _ {0} |}\right) ^ {r + \frac {1}{2}} \| \partial^ {r} A \| _ {C ^ {0}} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{3.31}
$$

It immediately follows that for every$\epsilon > 0$, for every n suficiently big such that$\begin{array} { r } { \| \alpha n \| _ { \mathbb { R } / \mathbb { Z } } < \frac { d } { n } } \end{array}$, we have

$$
\| \partial^ {r} A _ {n} (x) \| \leq n ^ {r} \left(C c _ {1} \left(x _ {*}\right) + \epsilon\right) ^ {r + 1} \| A \| _ {C ^ {r}}, \quad | x - x _ {*} | \leq \frac {d}{n}.\tag{3.32}
$$

Lemma 3.4. Assume that$A : \mathbb { R } / \mathbb { Z } \to { \mathrm { S L } } ( 2 , \mathbb { R } )$is Lipschitz. For almost every$x _ { * } \in \mathbb { R } / \mathbb { Z }$, for every$d > 0 , f o r$every$\epsilon > 0 , i f n > n _ { 0 } ( d , \epsilon )$and$\| \alpha n \| _ { \mathbb { R } / \mathbb { Z } }$ $\leq { \frac { d } { n } }$, then the matrix$B ( x _ { * } ) A _ { n } ( x ) B ( x _ { * } ) ^ { - 1 }$is close to$\mathrm { S O } ( 2 , \mathbb { R } )$provided that $\begin{array} { r } { | x - x _ { * } | \le \frac { d } { n } } \end{array}$

Proof. Let$x _ { * }$be a measurable continuity point of S and B. By the same argument of the previous lemma, for n big enough,$\begin{array} { r } { \mathrm { i f ~ } \| \alpha n \| _ { \mathbb { R } / \mathbb { Z } } < \frac { d } { n } } \end{array}$, then every $x$such that$\begin{array} { r } { | x - x _ { * } | < \frac { d } { n } } \end{array}$is at distance at most$\frac { \epsilon } { n }$from some x such that $| S ( x _ { 0 } ) - S ( x _ { * } ) | < \epsilon , \| B ( \overset { \cdot } { x } _ { 0 } ) - B ( x _ { * } ) \| < \epsilon$and$\| B ( x _ { 0 } + n \alpha ) - B ( x _ { * } ) \| < \epsilon$. By (3.4), we have

$$
\left\| A _ {n} \left(x _ {0}\right) ^ {- 1} \left(A _ {n} (x) - A _ {n} \left(x _ {0}\right)\right) \right\| \leq e ^ {n \left| x - x _ {0} \right| \| A \| _ {C ^ {0}} \operatorname{Lip} (A) \phi \left(x _ {0}\right) S \left(x _ {0}\right)} - 1 \leq K \epsilon\tag{3.33}
$$

and so it is enough to show that$B ( x _ { * } ) A _ { n } ( x _ { 0 } ) B ( x _ { * } ) ^ { - 1 }$is close to$\mathrm { S O } ( 2 , \mathbb { R } )$. But this is clear since$B ( x _ { 0 } + \alpha n ) A _ { n } ( x _ { 0 } ) B ( x _ { 0 } ) ^ { - 1 } \in \mathrm { S O } ( 2 , \mathbb { R } )$and$B ( x _ { 0 } ) , B ( x _ { 0 } + n \alpha )$ are close to$B ( x _ { * } )$□

## 4. Renormalization

Let$\Omega ^ { r } \ = \ \mathbb { R } \times C ^ { r } ( \mathbb { R } , \mathrm { S L } ( 2 , \mathbb { R } ) )$. We will view$\Omega ^ { r }$as a subgroup of $\mathrm { D i f f } ^ { r } ( \mathbb { R } \times \mathbb { R } ^ { 2 } )$

$$
(\alpha , A) \cdot (x, w) = (x + \alpha , A (x) \cdot w).\tag{4.1}
$$

$\mathrm { ~ A ~ } C ^ { r }$fibered$\mathbb { Z } ^ { 2 } .$-action is a homomorphism$\Phi : \mathbb { Z } ^ { 2 } \to \Omega ^ { r }$(that is,$\Phi ( n , m ) \circ$ $\Phi ( n ^ { \prime } , m ^ { \prime } ) = \Phi ( n + n ^ { \prime } , m + m ^ { \prime } ) )$. We let$\Lambda ^ { r }$denote the space of$C ^ { r }$fibered $\mathbb { Z } ^ { 2 } { \mathrm { - a c t i o n s } }$. We endow$\Lambda ^ { r }$with the pointwise topology. This topology is induced from the embedding$\Lambda ^ { r } \to \Omega ^ { r } \times \Omega ^ { r } , \Phi \mapsto ( \Phi ( 1 , 0 ) , \Phi ( 0 , 1 ) )$9

Let

$$
\Pi_ {1}: \mathbb {R} \times C ^ {r} (\mathbb {R}, \mathrm{SL} (2, \mathbb {R})) \to \mathbb {R}, \quad \Pi_ {2}: \mathbb {R} \times C ^ {r} (\mathbb {R}, \mathrm{SL} (2, \mathbb {R})) \to C ^ {r} (\mathbb {R}, \mathrm{SL} (2, \mathbb {R}))
$$

be the coordinate projections. Let also$\gamma _ { n , m } ^ { \Phi } = \Pi _ { 1 } \circ \Phi ( n , m ) \in \mathbb { R }$and$A _ { n , m } ^ { \Phi } =$ $\Pi _ { 2 } \circ \Phi ( n , m ) \in C ^ { r } ( \mathbb { R } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$.

The action Φ will be called nondegenerate if$\Pi _ { 1 } \circ \Phi : \mathbb { Z } ^ { 2 } \to$R is injective. Let$\Gamma ^ { r }$be the set of nondegenerate actions.

We let$\Lambda _ { 0 } ^ { r }$be the set of$\Phi \in \Lambda ^ { r }$such that$\gamma _ { 1 , 0 } ^ { \Phi } = 1$. For$\Phi \in \Lambda _ { 0 } ^ { r }$, we let $\alpha ^ { \Phi } = \gamma _ { 0 , 1 } ^ { \Phi }$. We let$\Gamma _ { 0 } ^ { r } = \Gamma ^ { r } \cap \Lambda _ { 0 } ^ { r } = \{ \Phi \in \Lambda _ { 0 } ^ { r } , \alpha ^ { \Phi } \in ( 0 , 1 ) \setminus \mathbb { Q } \}$

4.1. Some operations. Let$\lambda \neq 0$. Define$M _ { \lambda } \colon \Lambda ^ { r } \to \Lambda ^ { r }$by

$$
M _ {\lambda} (\Phi) (n, m) = (\lambda^ {- 1} \gamma_ {n, m} ^ {\Phi}, x \mapsto A _ {n, m} ^ {\Phi} (\lambda x)).\tag{4.2}
$$

Let$x _ { * } \in \mathbb { R }$. Define$T _ { x _ { * } } : \Lambda ^ { r } \to \Lambda ^ { r }$by

$$
T _ {x _ {*}} (\Phi) (n, m) = \left(\gamma_ {n, m} ^ {\Phi}, x \mapsto A _ {n, m} ^ {\Phi} \left(x + x _ {*}\right)\right).\tag{4.3}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">C<sup>r</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">C<sup>r</sup>-</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">C<sup>r</sup>(R, SL(2, R)))</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>Here and in what follows, spaces of functions (such as  are always endowed with the weak topology of uniform convergence on compacts. In the caseC<sup>ω</sup> (which is the most important for us), this means that a sequence converges to A if andA<sup>(n)</sup>A only if for every compact K there exists a complex neighborhood V  K such that (theV⊃K holomorphic extensions of) (are defined and) converge to uniformly on V. We recallA<sup>(n)</sup>AV that the weak topology is metrizable for but not even separable for r = ω.<sup>r</sup> <sup>=</sup> <sup>ω,</sup>r = ω</span></small>

Let$U \in \operatorname { G L } ( 2 , \mathbb { Z } )$. Define$N _ { U } : \Lambda ^ { r } \to \Lambda ^ { r }$by

$$
N _ {U} (\Phi) (n, m) = \Phi (n ^ {\prime}, m ^ {\prime}), \quad \binom{n ^ {\prime}}{m ^ {\prime}} = U ^ {- 1} \cdot \binom{n}{m}.\tag{4.4}
$$

The operations$M , T ,$, and N will be called rescaling, translation, and base change.

Notice that$M _ { \lambda } M _ { \lambda ^ { \prime } } = M _ { \lambda \lambda ^ { \prime } } , T _ { x _ { * } } T _ { x _ { * } ^ { \prime } } = T _ { x _ { * } + x _ { * } ^ { \prime } }$, and$N _ { U } N _ { U ^ { \prime } } = N _ { U U ^ { \prime } }$(that is, M, T, and N are left actions of$\mathbb { R } ^ { * }$, R and${ \mathrm { G L } } ( 2 , \mathbb { Z } )$on$\Lambda ^ { r } )$. Moreover, base changes commute with translations and rescalings.

Notice that$C ^ { r } ( \mathbb { R } , \mathrm { S L } ( 2 , \mathbb { R } ) )$acts on$\Omega ^ { r }$by

$$
\mathrm{Ad} _ {B} (\alpha , A (\cdot)) = (\alpha , B (\cdot + \alpha) A (\cdot) B (\cdot) ^ {- 1}).
$$

This action extends to an action (still denoted$\operatorname { A d } _ { B } )$on$\Lambda ^ { r }$. We will say that $\Phi$and$\operatorname { A d } _ { B } ( \Phi )$are$C ^ { r } { \mathrm { - c o n j u g a t e } }$via B.

4.2. Continued fraction expansion. Let$0 < \alpha < 1$be irrational. We will discuss some elementary facts and fix notation regarding the continued fraction expansion

$$
\alpha = \frac {1}{a _ {1} + \frac {1}{a _ {2} + \cdots}}\tag{4.5}
$$

and we refer the reader to [HW] for details. Define$\alpha _ { n } = G ^ { n } ( \alpha )$where G is the Gauss map$G ( x ) = \{ x ^ { - 1 } \} \ ( \{ \cdot \}$denotes the fractionary part). The coeficients $a _ { n }$in (4.5) are given by$a _ { n } = [ \alpha _ { n - 1 } ^ { - 1 } ]$, where [·] denotes the integer part. We also set$a _ { 0 } = 0$for convenience. Then

$$
\alpha_ {n} = \frac {1}{a _ {n + 1} + \frac {1}{a _ {n + 2} + \cdots}}.\tag{4.6}
$$

Let$\textstyle \beta _ { n } = \prod _ { j = 0 } ^ { n } \alpha _ { j }$. Define

(4.7)

$$
Q _ {0} = \left( \begin{array}{c c} q _ {0} & p _ {0} \\ q _ {- 1} & p _ {- 1} \end{array} \right) = \left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right),\tag{4.8}
$$

$$
Q _ {n} = \left( \begin{array}{c c} q _ {n} & p _ {n} \\ q _ {n - 1} & p _ {n - 1} \end{array} \right) = \left( \begin{array}{c c} a _ {n} & 1 \\ 1 & 0 \end{array} \right) \left( \begin{array}{c c} q _ {n - 1} & p _ {n - 1} \\ q _ {n - 2} & p _ {n - 2} \end{array} \right);
$$

that is,

$$
Q _ {n} = U (\alpha_ {n - 1}) \dots U (\alpha_ {0}),\tag{4.9}
$$

where

$$
U (x) = \left( \begin{array}{c c} [ x ^ {- 1} ] & 1 \\ 1 & 0 \end{array} \right).\tag{4.10}
$$

Then we have

(4.11)

$$
\beta_ {n} = (- 1) ^ {n} (q _ {n} \alpha - p _ {n}) = \frac {1}{q _ {n + 1} + \alpha_ {n + 1} q _ {n}},\tag{4.12}
$$

$$
\frac {1}{q _ {n + 1} + q _ {n}} <   \beta_ {n} <   \frac {1}{q _ {n + 1}}.
$$

4.3. Renormalization. We define the renormalization operator around$0 ,$ $R \equiv R _ { 0 } : \Gamma _ { 0 } ^ { r } \to \Gamma _ { 0 } ^ { r }$, by$R ( \Phi ) = M _ { \alpha } ( N _ { U ( \alpha ) } ( \Phi ) )$where$\alpha = \alpha ^ { \Phi }$and$U ( \cdot )$is given by (4.10).

The renormalization operator around$x _ { * } \in \mathbb { R } , R _ { x _ { * } } : \Gamma _ { 0 } ^ { r } \to \Gamma _ { 0 } ^ { r }$is defined by $R _ { x _ { * } } = T _ { x _ { * } } ^ { - 1 } \circ R \circ T _ { x _ { * } }$

Notice that if$\Phi \in \Gamma _ { 0 } ^ { r }$and$\alpha ^ { \Phi } = \alpha$then$\alpha ^ { R ( \Phi ) } = G ( \alpha )$and so

$$
R ^ {n} (\Phi) = M _ {\alpha_ {n - 1}} \circ N _ {U (\alpha_ {n - 1})} \circ \dots \circ M _ {\alpha_ {0}} \circ N _ {U (\alpha_ {0})} (\Phi) = M _ {\beta_ {n - 1}} (N _ {Q _ {n}} (\Phi)).\tag{4.13}
$$

4.4. Normalized actions, relation to cocycles. An action$\Phi \in \Lambda _ { 0 } ^ { r }$will be called normalized if$\Phi ( 1 , 0 ) = ( 1 , \operatorname { i d } )$. If Φ is normalized then$\Phi ( 0 , 1 ) = \left( \alpha , A \right)$ can be viewed as a C<sup>r</sup>-cocycle, since A is automatically defined modulo$\mathbb { Z } . ^ { 1 0 }$ Inversely, given a$C ^ { r }$-cocycle$( \alpha , A ) , \alpha \in [ 0 , 1 ]$, we associate a normalized action $\Phi _ { \alpha , A }$by setting

$$
\Phi_ {\alpha , A} (1, 0) = (1, \mathrm{id}), \quad \Phi_ {\alpha , A} (0, 1) = (\alpha , A).\tag{4.14}
$$

Lemma 4.1. Any$\Phi \in \Lambda _ { 0 } ^ { r }$is$C ^ { r }$-conjugate to a normalized action. Moreover,$i f \Phi _ { n } ( 1 , 0 ) \in \Lambda _ { 0 } ^ { r }$converges to (1, id) in$\Lambda _ { 0 } ^ { r }$then one can choose a sequence of conjugacies converging to id in the$C ^ { r }$topology<sup>11</sup>.

Proof. We first assume that$r \neq \omega$. Let$\Phi ( 1 , 0 ) \ = \ ( 1 , A )$. Let$B \in$ $C ^ { r } ( [ 0 , 3 / 2 ] , \mathrm { S L } ( 2 , \mathbb { R } ) )$be such that$B ( x ) = \mathrm { i d } , x \in [ 0 , 1 / 2 ] , B ( x ) = A ( x - 1 )$ $x \in [ 1 , 3 / 2 ]$. Let us extend B to R forcing$\operatorname { A d } _ { B } ( 1 , \operatorname { i d } ) = ( 1 , A )$(B is still smooth after the modification). If A is$C ^ { r }$close to id, we can select$B :$ $[ 0 , 3 / 2 ]  \mathrm { S L } ( 2 , \mathbb { R } )$to be$C ^ { r }$close to id, and in this case$B : \mathbb { R } \to \mathrm { S L } ( 2 , \mathbb { R } )$is also$C ^ { r }$close to id.

Let us now assume that$r = \omega$. Let us first deal with the case where (the holomorphic extension of) A is close to the identity in a definite neighborhood of R. Extend A to a real-symmetric$C ^ { \infty }$function$A : \mathbb { C } \to { \mathrm { S L } } ( 2 , \mathbb { C } )$which is

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">A(x + 1).A(x + 1).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1, id) o (α, A) = (α, A) o (1, id)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">A(x) =</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>10Since</sup> <sup>the</sup> <sup>commutativity</sup> <sup>relation</sup> <sup>(1,</sup> <sup>id)</sup> ◦ <sup>(α,</sup> <sup>A) = (α,</sup> <sup>A)</sup> ◦ <sup>(1,</sup> <sup>id)</sup> <sup>is</sup> <sup>equivalent</sup> <sup>to</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Cω</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>11</sup>The reason we refer to sequences instead of speaking of closeness is because the C<sup>ω</sup> topology is not separable.</span></small>

$C ^ { \infty }$close to the identity and which is holomorphic on a definite neighborhood V of R. We will assume that V satisfies (after shrinking)

(4.15)

$$
z \in V \implies z + 1 \in V, \quad \Re z \leq 0,\tag{4.16}
$$

$$
z \in V \implies z - 1 \in V, \quad \Re z \geq 1,\tag{4.17}
$$

$$
[ 0, 1 ] \times [ - \epsilon , \epsilon ] \subset V.
$$

Let$B \in C ^ { \infty } ( \mathbb { C } , { \mathrm { S L } } ( 2 , \mathbb { C } ) )$be$C ^ { \infty }$close to the identity, real-symmetric, and satisfying$A ( z ) = B ( z + 1 ) B ( z ) ^ { - 1 } , \ z \in \mathbb { C } \ ( B$is obtained as in the previous case). Notice that$\overline { { { \partial } } } B ( z + 1 ) = \overline { { { \partial } } } A ( z ) B ( z ) + A ( z ) \overline { { { \partial } } } B ( z )$, so for$z \in V$we have $B ( z + 1 ) ^ { - 1 } \overline { { { \partial } } } B ( z + 1 ) = B ( z + 1 ) ^ { - 1 } A ( z ) \overline { { { \partial } } } B ( z ) = B ( z ) ^ { - 1 } \overline { { { \partial } } } B ( z )$. Moreover,

$$
\| B (z) ^ {- 1} \overline {{\partial}} B (z) \| <   \delta , \quad z \in [ 0, 1 ] \times [ - \epsilon , \epsilon ]\tag{4.18}
$$

for some small δ.

Given$C : \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] \to \mathrm { S L } ( 2 , \mathbb { C } )$, we let$D = B C ^ { - 1 }$and we obviously have$A ( z ) = D ( z + 1 ) D ( z ) ^ { - 1 }$. We want to choose C so that

$$
\overline {{\partial}} (C (z) ^ {- 1}) C (z) = - B (z) ^ {- 1} \overline {{\partial}} B (z), \quad z \in [ 0, 1 ] \times [ - \epsilon , \epsilon ],\tag{4.19}
$$

for this will assure us that

$$
B (z) ^ {- 1} \overline {{\partial}} D (z) C (z) = B (z) ^ {- 1} \overline {{\partial}} B (z) + \overline {{\partial}} (C (z) ^ {- 1}) C (z)\tag{4.20}
$$

vanishes for$z \in [ 0 , 1 ] \times [ - \epsilon , \epsilon ]$and also in$V \cap ( \mathbb { R } \times [ - \epsilon , \epsilon ] )$(this guarantees that D is holomorphic in a definite neighborhood of R), and we also want to impose that C (and hence$D )$is$C ^ { 0 }$close to the identity. Here the smoothness requirement on$C$is for it to be of class$W ^ { 1 , 1 }$; that is, it should be continuous and have distributional derivatives in$L ^ { 1 }$

Equation (4.19) is equivalent to

$$
C (z) ^ {- 1} \overline {{\partial}} C (z) = B (z) ^ {- 1} \overline {{\partial}} B (z).\tag{4.21}
$$

To conclude, we use the following proposition:

Proposition 4.2. There exists$\kappa > 0$with the following property. Let $\eta \in L ^ { \infty } ( \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] , \mathrm { s l } ( 2 , \mathbb { R } ) )$and assume that$\| \eta \| _ { L ^ { \infty } } < \kappa$. Then there exists $C : \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] \to \mathrm { S L } ( 2 , \mathbb { R } )$of class$W ^ { 1 , 1 }$such that$C ( z ) ^ { - 1 } \overline { { { \partial } } } C ( z ) = \eta$and $\| C - \mathrm { i d } \| _ { C ^ { 0 } } \leq \kappa ^ { - 1 } \| \eta \| _ { L ^ { \infty } }$close to the identity for$z \in \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ]$. Moreover, C is real-symmetric provided η is real-symmetric.

Proof. Let$W ^ { 1 , 1 } ( \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] , \mathrm { s l } ( 2 , \mathbb { R } ) )$be the space of continuous maps $a : \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] \to { \mathrm { s l } } ( 2 , \mathbb { R } )$with integrable distributional derivatives, endowed with the natural norm. We can obtain a bounded linear map$P : L ^ { \infty } ( \mathbb { R } / \mathbb { Z } \times$ $[ - 1 , 1 ] , \mathrm { s l } ( 2 , \mathbb { C } ) ) \to W ^ { 1 , 1 } ( \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] , \mathrm { s l } ( 2 , \mathbb { C } ) )$which is real-symmetric and solves${ \overline { { \partial } } } \circ P = \operatorname { i d }$. Indeed P can be given explicitly in terms of the Cauchy transform

$$
(P \alpha) (z) = \frac {- 1}{\pi} \int_ {\mathbb {R} \times [ - 1, 1 ]} \frac {\alpha (\zeta)}{z - \zeta} d \zeta \wedge d \overline {{\zeta}} = \lim _ {t \to \infty} \frac {- 1}{\pi} \int_ {[ - t, t ] \times [ - 1, 1 ]} \frac {\alpha (\zeta)}{z - \zeta} d \zeta \wedge d \overline {{\zeta}}.\tag{4.22}
$$

Define an analytic map$T : L ^ { \infty } ( \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] ) \to L ^ { \infty } ( \mathbb { R } / \mathbb { Z } \times [ - 1 , 1 ] )$by $T ( \cdot ) = e ^ { - P ( \cdot ) } \overline { { { \partial } } } e ^ { P ( \cdot ) }$. Then$T ( 0 ) ~ = ~ 0 , ~ D T ( 0 ) ~ = ~ \mathrm { i d }$. It follows that T is a difeomorphism in a neighborhood of$\eta = 0$, so we may solve$e ^ { - P \alpha } \overline { { { \partial } } } e ^ { P \alpha } = \eta$ with$\| \alpha \| _ { \infty } \leq K \| \eta \| _ { L ^ { \infty } }$provided$\eta$is close to 0. It follows that$C = e ^ { P \alpha }$satisfies the conclusion of the proposition.□

We may now obtain C with the required properties by taking$\eta = B ^ { - 1 } \overline { { { \partial } } } B$ in$[ 0 , 1 ] \times [ - \epsilon , \epsilon ]$and$\eta = 0$otherwise and applying the previous proposition. This concludes the second part of the lemma in the case$r = \omega$

This argument also works if we only assume that A is close to the identity in the$C ^ { \infty }$topology (indeed the$C ^ { 1 }$topology is enough, as this is all that we need to get (4.18)), and gives the first part of the lemma also in this case (but we obviously do not get that the holomorphic extension of the normalizing matrix is close to the identity). In order to treat the global case, we first consider $B \in C ^ { \infty } ( \mathbb { R } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$with$A ( x ) = B ( x + 1 ) B ( x ) ^ { - 1 }$, and then approximate B (in the$C ^ { \infty }$topology) by$B ^ { \prime } \in C ^ { \omega } ( \mathbb { R } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$. Then$B ^ { \prime } ( x + 1 ) ^ { - 1 } A ( x ) B ^ { \prime } ( x )$is $C ^ { \infty }$close to the identity and we can apply the previous case.□

4.5. Degree and fibered rotation number. The degree and the fibered rotation number of an action will be considered in detail in Appendix A. Here we present only a summarized (and more intuitive) discussion.

The degree deg Φ of a nondegenerate action Φ can be defined as follows. The degree of a normalized action$\Phi _ { \alpha , A }$is the (topological) degree of the map ${ \cal A } : \mathbb { R } / \mathbb { Z }  \mathrm { S L } ( 2 , \mathbb { R } ) ^ { 1 2 }$. It is easy to see that the degree of a normalized action is invariant under conjugacies. This allows us to define the degree of a nondegenerate action Φ as the degree of any normalized action$\Phi _ { \alpha , A }$obtained from Φ by rescaling and conjugacy. It is readily seen that the degree is invariant under rescalings, conjugacies, and translations. In the Appendix A we will see that base changes preserve the degree up to sign: deg$N _ { U } ( \Phi ) = \operatorname* { d e t } U \log \Phi$ In particular, the renormalization of an action of degree 0 still has degree 0.

The fibered rotation number rot(Φ) of an action Φ is only defined in the case deg$\Phi = 0$. For a nondegenerate action, it can be defined as follows. If Φ has degree 0, and is conjugated to a normalized action$\Phi _ { \alpha , A }$, then$( \alpha , A )$ is homotopic to the identity, and it is natural to define rot(Φ) as the fibered rotation number of the cocycle$( \alpha , A )$. In general, a nondegenerated action Φ may be rescaled to an action$M _ { \lambda } ( \Phi )$which is conjugated to a normalized action: we then define$\mathrm { r o t } ( \Phi ) = \lambda \mathrm { r o t } ( M _ { \lambda } ( \Phi ) )$. It turns out (see Appendix A) that$\operatorname { r o t } ( \Phi )$is only well defined up to addition of an element of the module of frequency of$\Phi _ { i }$that is, the Z-module$\Gamma _ { \Phi } = \{ \gamma _ { n , m } ^ { \Phi } , ( n , m ) \in \mathbb { Z } ^ { 2 } \}$, and so rot(Φ) should be regarded as an element of$\mathbb { R } / \Gamma _ { \Phi } . ^ { 1 3 }$It is readily seen that rot(Φ) is invariant under translations. We will see in Appendix A that base changes preserve the fibered rotation number up to sign: rot$\left( N _ { U } ( \Phi ) \right) = \operatorname* { d e t } U \cot ( \Phi )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">SL(2, R)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>θ</sup> → <sup>R</sup>θ<sup>,</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>12</sup>Recall that the fundamental group of is generated by  and hence is canonically isomorphic to Z.</span></small>

We shall say that an element in$\mathbb { R } / \Gamma _ { \Phi }$is Diophantine if for some representative$\beta ,$some basis$\{ e _ { 1 } , e _ { 2 } \} \subset \mathbb { Z } ^ { 2 }$and some$\kappa > 0 , \tau > 0$, one has

$$
\left| 2 \beta - k \gamma_ {e _ {1}} - l \gamma_ {e _ {2}} \right| \geq \kappa (1 + | k | + | l |) ^ {- \tau}, \quad (k, l) \in \mathbb {Z} ^ {2}.\tag{4.23}
$$

This definition is clearly independent of the choice of the representative and of the chosen basis (κ then has to be changed). Finally, we say that the action $\Phi$is (fiberwise) Diophantine if$\operatorname { r o t } ( \Phi )$is Diophantine. This notion is stable under conjugation, translation, rescaling, and base change, so it is also stable under renormalization. This definition is such that a nondegenerate normalized action$\Phi _ { \alpha , A }$is Diophantine if and only if$\rho ( \alpha , A )$is Diophantine with respect to α.

4.6. Reducibility. An action$\Phi$is called constant if for every$( n , m ) \in \mathbb { Z } ^ { 2 }$ $x \mapsto A _ { n , m } ^ { \Phi } ( x )$is constant. We will say that an action$\Phi \in \Lambda _ { 0 } ^ { r }$is$C ^ { r }$-reducible if it is$C ^ { r } { \mathrm { - c o n j u g a t e } }$to a constant action. It immediately follows that reducibility is invariant under conjugation, translation, rescaling and base change. Thus reducibility is also invariant under renormalization: an action$\Phi \in \Gamma _ { 0 } ^ { r }$is $C ^ { r }$-reducible if and only if its renormalization$R ( \Phi )$is$C ^ { r }$-reducible. Moreover, reducibility of a nondegenerate normalized action$\Phi _ { \alpha , A }$can be interpreted in familiar terms:

Lemma 4.3. Let$( \alpha , A ) \in \ P \left( \mathbb { R } \setminus \mathbb { Q } \right) \times C ^ { r } ( \mathbb { R } / \mathbb { Z } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$. Then$\Phi _ { \alpha , A }$is C<sup>r</sup>-reducible if and only if (α, A) is$C ^ { r }$-reducible.

Proof. Assume that$\Phi _ { \alpha , A }$is reducible. Then there exists$B \in C ^ { r } ( \mathbb { R } , \mathrm { S L } ( 2 , \mathbb { R } ) )$ such that$B ( x + 1 ) B ( x ) ^ { - 1 } = U , B ( x + \alpha ) A ( x ) B ( x ) ^ { - 1 } = V$, where$U , V \in$ $\mathrm { S L } ( 2 , \mathbb { R } )$commute. Write$U = \varepsilon e ^ { u }$, where$u \in \mathrm { { s l } } ( 2 , \mathbb { R } )$commutes with V , and $\varepsilon \in \{ 1 , - 1 \}$. Let$B ^ { \prime } ( x ) = e ^ { - x u } B ( x )$Then$B ^ { \prime } ( x + 1 ) B ^ { \prime } ( x ) ^ { - 1 } = \varepsilon \mathrm { i d }$, and so $B ^ { \prime } ( x + 2 ) = B ^ { \prime } ( x )$. Moreover,$B ^ { \prime } ( x + \alpha ) A ( x ) B ^ { \prime } ( x ) ^ { - 1 } = e ^ { - \alpha u } V$is a constant. Thus$( \alpha , A )$is reducible.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>13</sup>This is related to the fact that the fibered rotation number is not a conjugacy invariant for cocycles.</span></small>

Assume that$( \alpha , A )$is reducible. Thus there exists$B \in C ^ { r } ( \mathbb { R } / 2 \mathbb { Z } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$ such that$B ( x + \alpha ) A ( x ) B ( x ) ^ { - 1 } = C$for some$C \in \mathrm { S L } ( 2 , \mathbb { R } )$. Let$D ( x ) =$ $B ( x + 1 ) B ( x ) ^ { - 1 }$, so that$D ( x + 2 ) = D ( x )$. Then$C D ( x ) C ^ { - 1 } = D ( x + \alpha )$

Assume that C is not conjugate to a rotation of angle$\theta = k \alpha / 2$for any $k \in \mathbb { Z } \setminus \{ 0 \}$. Write in the Fourier series

$$
D (x) = \sum_ {k \in \mathbb {Z}} \hat {D} (k) e ^ {\pi i k x}, \quad \hat {D} (k) \in \mathrm{M} (2, \mathbb {C}).\tag{4.24}
$$

Then

$$
\hat {D} (k) e ^ {\pi i k \alpha} = C \hat {D} (k) C ^ {- 1}.\tag{4.25}
$$

If$\hat { D } ( k ) \neq 0$for some$k \neq 0$then$e ^ { \pi i k \alpha }$is an eigenvalue of$\operatorname { A d } ( C ) : \operatorname { M } ( 2 , \mathbb { C } ) \to$ $\operatorname { M } ( 2 , \mathbb { C } )$. This implies that C is conjugate to$R _ { \theta }$where$\theta = \pm \frac { k \alpha } { 2 }$, contradicting our assumption. Thus$D ( x ) = { \hat { D } } ( 0 )$is a constant, and it follows that $\mathrm { A d } _ { B } \big ( \Phi _ { \alpha , A } \big )$is a constant action.

Assume that C is conjugate to a rotation of angle$\theta = k \alpha / 2$for some $k \in \mathbb { Z } \backslash \{ 0 \} \colon C = U R _ { \theta } U ^ { - 1 } , U \in { \mathrm { S L } } ( 2 , \mathbb { R } )$. Let$B ^ { \prime } ( x ) = U R _ { - ( \theta / \alpha ) x } U ^ { - 1 } B ( x )$ Then$B ^ { \prime } ( x + 2 ) = B ^ { \prime } ( x )$and

$$
B ^ {\prime} (x + \alpha) A (x) B ^ {\prime} (x) ^ {- 1} = U R _ {- (\theta / \alpha) (x + \alpha)} U ^ {- 1} C U R _ {(\theta / \alpha) x} U ^ {- 1} = \mathrm{id}.
$$

Thus, up to changing$B$to$B ^ { \prime }$we may assume that$C = \mathrm { i d }$, and we can apply the previous case.□

We will need the following version of a well-known reducibility result:

Lemma 4.4. Let$\Phi \in \Gamma _ { 0 } ^ { r } , r = \omega , \infty$be C<sup>r</sup>-conjugate to an$\mathrm { S O } ( 2 , \mathbb { R } )$action of degree 0.$I f \alpha ^ { \Phi } \in \mathrm { D C }$then$\Phi$is$C ^ { r }$-conjugate to a normalized constant action. In particular, Φ is$C ^ { r }$-reducible.

Proof. We may assume that Φ is normalized, since we can always conjugate $\Phi ( 1 , 0 )$to (1, id) via$C ^ { r } ( \mathbb { R } , \mathrm { S O } ( 2 , \mathbb { R } ) )$: this can be done in the same way as in Lemma 4.1 (it is indeed easier to proceed for the$\mathrm { S O } ( 2 , \mathbb { R } )$case).

Let$( \alpha , A ) = \Phi ( 0 , 1 )$, and let$\phi : \mathbb { R }  \mathbb { R }$satisfy$A ( x ) = R _ { \phi ( x ) }$. Since Φ is normalized, A is defined modulo$\mathbb { Z } ,$and since Φ is of degree 0, this implies that$\phi$is defined modulo Z as well.

Consider the Fourier series

$$
\phi (\theta) = \sum_ {k \in \mathbb {Z}} \hat {\phi} (k) e ^ {2 k \pi i \theta},\tag{4.26}
$$

and let

$$
\psi (\theta) = \sum_ {k \in \mathbb {Z} \backslash \{0 \}} \hat {\psi} (k) e ^ {2 k \pi i \theta},\tag{4.27}
$$

where

$$
\hat {\psi} (k) = \frac {\hat {\phi} (k)}{1 - e ^ {2 k \pi i \alpha}}, \quad k \neq 0\tag{4.28}
$$

so that

$$
\phi (x) - \hat {\phi} (0) = \psi (x) - \psi (x + \alpha).\tag{4.29}
$$

The fact that$\alpha \in \mathrm { D C }$implies that$| 1 - e ^ { 2 k \pi i \alpha } | > \kappa k ^ { - \tau }$for some$\kappa > 0 , \tau > 0$ In particular$\psi \in C ^ { r } ( \mathbb { R } / \mathbb { Z } , \mathbb { R } )$

Let$B ( x ) = R _ { \psi ( x ) }$. Then$B \in C ^ { r } ( \mathbb { R } / \mathbb { Z } , \mathrm { S O } ( 2 , \mathbb { R } ) )$, and we have$B ( x + 1 )$ $B ( x ) ^ { - 1 } = \mathrm { i d } , B ( x + \alpha ) A ( x ) B ( x ) ^ { - 1 } = R _ { \hat { \phi } ( 0 ) }$. This implies that$\operatorname { A d } _ { B } \Phi$is a normalized constant action.□

The following is a restatement of Theorem 2.7 in the language of actions.

Lemma 4.5. Let$\Psi \in \Gamma _ { 0 } ^ { \omega }$be$C ^ { \omega }$-conjugate to a normalized constant action, and let$\kappa > 0 , \tau > 0$be fixed. Let$\Psi _ { n }$be a sequence of Diophantine actions converging to Ψ in$\Gamma _ { 0 } ^ { \omega }$and satisfying$\alpha _ { n } \equiv \alpha ^ { \Psi _ { n } } \in \mathrm { D C } ( \kappa , \tau )$. Then$\Psi _ { n }$is $C ^ { \omega }$-reducible for n large enough.

Proof. After performing a conjugation, we may assume that$\Psi ( 1 , 0 ) =$ $( 1 , \operatorname { i d } )$and$\Psi ( 0 , 1 ) = ( \hat { \alpha } , \hat { A } )$where$\hat { A } \in \mathrm { S L } ( 2 , \mathbb { R } )$is a constant. By Lemma 4.1, there exists a sequence$B ^ { ( n ) } \in C ^ { \omega } ( \mathbb { R } , \mathrm { S L } ( 2 , \mathbb { R } ) )$converging to id which conjugates$\Psi _ { n }$to a normalized cocycle$\Psi _ { n } ^ { \prime } = \operatorname { A d } _ { B ^ { ( n ) } } \Psi _ { n }$. It follows that$( \alpha _ { n } , A ^ { ( n ) } ) \equiv$ $\Psi _ { n } ^ { \prime } ( 0 , 1 )$converges to$( { \hat { \alpha } } , { \hat { A } } )$in the$C ^ { \omega } { \mathrm { - t o p o l o g y . } }$Thus, Theorem 2.7 applies and$( \alpha _ { n } , A ^ { ( n ) } )$is$C ^ { \omega } .$-reducible for n large enough. This implies that$\Psi _ { n } ^ { \prime }$and $\Psi _ { n }$are$C ^ { \omega }$-reducible as well.□

## 5. A priori bounds and limits of renormalization

The language of renormalization allows us to restate Lemma 3.3 as a precompactness result:

Theorem 5.1 (A priori bounds). Let$\Phi \in \Gamma _ { 0 } ^ { r } , \ r \geq 1$, be a normalized action, and assume that the cocycle$( \alpha , A ) \ = \ \Phi ( 0 , 1 )$is$L ^ { 2 }$-conjugated to a cocycle of rotations. Then for almost every$x _ { * } \in \mathbb { R }$, there exists$K > 0$such that for every$d > 0$and for every$n > n _ { 0 } ( d )$

(5.1)

$$
\left\| \partial^ {k} A _ {1, 0} ^ {R _ {x _ {*}} ^ {n} \Phi} (x) \right\| \leq K ^ {k + 1} \| A \| _ {C ^ {k}}, \quad 0 \leq k \leq r, \quad | x - x _ {*} | <   d.\tag{5.2}
$$

$$
\left\| \partial^ {k} A _ {0, 1} ^ {R _ {x _ {*}} ^ {n} \Phi} (x) \right\| \leq K ^ {k + 1} \| A \| _ {C ^ {k}}, \quad 0 \leq k \leq r, \quad | x - x _ {*} | <   d.
$$

In particular,$i f r = \omega , \infty$then$\{ R _ { x _ { * } } ^ { n } ( \Phi ) \} _ { n }$is precompact in$\Lambda _ { 0 } ^ { r }$

Proof. Apply Lemma 3.3 to both$( \alpha , A )$and to$( \alpha , A ) ^ { - 1 }$, obtaining a full measure set of “good point${ \boldsymbol { { \mathbf { \ } } } } ^ { \mathfrak { S } } \ x _ { * }$. Notice that

(5.3)

$$
A _ {1, 0} ^ {R _ {x *} ^ {n} \Phi} (x) = A _ {(- 1) ^ {n - 1} q _ {n - 1}} (x _ {*} + \beta_ {n - 1} (x - x _ {*})),\tag{5.4}
$$

$$
A _ {0, 1} ^ {R _ {x *} ^ {n} \Phi} (x) = A _ {(- 1) ^ {n} q _ {n}} (x _ {*} + \beta_ {n - 1} (x - x _ {*})).
$$

Fix d (we may assume$d > 1 )$. Since$\beta _ { n - 1 } < \frac { 1 } { q _ { n } } < \frac { 1 } { q _ { n - 1 } }$, the estimates of Lemma 3.3 imply that for$0 \leq k \leq r$and for$| x - \overline { { x _ { * } } } | < \bar { d } .$

(5.5)

$$
\begin{array}{r l} & {\left\| \partial^ {k} A _ {1, 0} ^ {R _ {x _ {*}} ^ {n} \Phi} (x) \right\| \leq \beta_ {n - 1} ^ {k} \| (\partial^ {k} A _ {(- 1) ^ {n - 1} q _ {n - 1}}) (x _ {*} + \beta_ {n - 1} (x - x _ {*})) \|} \\ & {\qquad \leq (\beta_ {n - 1} q _ {n - 1}) ^ {k} K ^ {k + 1} \| A \| _ {C ^ {k}} \leq K ^ {k + 1} \| A \| _ {C ^ {k}},} \end{array}\tag{5.6}
$$

$$
\begin{array}{r l} & {\left\| \partial^ {k} A _ {0, 1} ^ {R _ {x _ {*}} ^ {n} \Phi} (x) \right\| \leq \beta_ {n - 1} ^ {k} \| (\partial^ {k} A _ {(- 1) ^ {n} q _ {n}}) (x _ {*} + \beta_ {n - 1} (x - x _ {*})) \|} \\ & {\qquad \leq (\beta_ {n - 1} q _ {n}) ^ {k} K ^ {k + 1} \| A \| _ {C ^ {k}} \leq K ^ {k + 1} \| A \| _ {C ^ {k}}} \end{array}
$$

(notice that$\| A \| _ { C ^ { k } } = \| A ^ { - 1 } \| _ { C ^ { k } } )$. The precompactness statement is then obvious.□

This result allows us to consider limits of renormalization. Those are easy to analyze due to the following simple corollary of Lemma 3.4:

Theorem 5.2 (Limits). Let$\Phi \in \Gamma _ { 0 } ^ { \mathrm { L i p } }$be a normalized action, and assume that the cocycle$( \alpha , A ) = \Phi ( 0 , 1 )$$L ^ { 2 }$-conjugated to a cocycle of rotations. Then for almost every$x _ { * } \in \mathbb { R }$, any limit of$R _ { x _ { * } } ^ { n } ( \Phi )$is conjugate to an action of rotations, via a constant$B \in \mathrm { S L } ( 2 , \mathbb { R } )$

We can now prove the following rigidity result.

Theorem 5.3 (Rigidity). Let$\alpha \in \mathrm { R D C }$, and let$A : \mathbb { R } / \mathbb { Z } \to { \mathrm { S L } } ( 2 , \mathbb { R } )$be $C ^ { \omega }$and homotopic to the identity. If$( \alpha , A )$is L<sup>2</sup>-conjugated to a cocycle of rotations, and the fibered rotation number of$( \alpha , A )$is Diophantine with respect to α, then$( \alpha , A )$is$C ^ { \omega }  – r e d u c i b l e$

Proof. Let$\alpha \in \mathrm { R D C } ( \kappa , \tau )$and let$n _ { k } \to \infty$be such that$\alpha _ { n _ { k } } \in \mathrm { D C } ( \kappa , \tau )$

Consider the renormalizations$\Psi _ { k } = R _ { x _ { * } } ^ { n _ { k } } ( \Phi _ { \alpha , A } )$, where x is as in Theorems 5.1 and 5.2. Notice that for every$k , ~ \alpha ^ { \Psi _ { k } } \in \mathrm { D C } ( \kappa , \tau )$and$\Psi _ { k }$is a Diophantine action.

Passing to a subsequence, we may assume that$\Psi _ { k } ~  ~ \Psi$in the$C ^ { \omega }$ topology. Since$\mathrm { D C } ( \kappa , \tau )$is compact,$\alpha ^ { \Psi } = \operatorname* { l i m } \alpha _ { n _ { k } } \in \mathrm { D C } ( \kappa , \tau )$. By Theorem 5.2, Ψ is$C ^ { \omega } .$-conjugate to an$\mathrm { S O } ( 2 , \mathbb { R } )$action, and so by Lemma 4.4, Ψ is $C ^ { \omega _ { - } } \mathrm { c o n j u g a t e }$to a normalized constant action. Thus Lemma 4.5 applies and we conclude that$\Psi _ { k }$is$C ^ { \omega }$-reducible for k large enough. It follows that$\Phi _ { \alpha , A }$ is reducible, so that$( \alpha , A )$is reducible as well.□

Proof of Theorems A and$\mathrm { A } ^ { \prime }$. We can now prove Theorem A easily. Let $\alpha \in \mathrm { R D C } , v \in C ^ { \omega } ( \mathbb { R } / \mathbb { Z } , \mathbb { R } )$, and let$\Delta$be the set of$E \in \mathbb { R }$such that$( \alpha , S _ { v , E } )$ is$L ^ { 2 } .$-conjugated to a cocycle of rotations and the fibered rotation number of $( \alpha , S _ { v , E } )$is Diophantine with respect to α. By Theorem 2.1 and Corollary 2.5, $\Delta \cup \{ E \in \mathbb { R } , L ( \alpha , S _ { v , E } ) > 0 \}$has full Lebesgue measure in R, and Theorem 5.3 implies that$( \alpha , S _ { v , E } )$is$C ^ { \omega } .$-reducible for all$E \in \Delta$. This shows that$( \alpha , S _ { v , E } )$is $C ^ { \omega } .$-reducible for almost every$E \in \mathbb { R }$such that$L ( \alpha , S _ { v , E } ) = 0$. By Remark 1.3, if$E \in \mathbb { R }$is such that$L ( \alpha , S _ { v , E } ) > 0$then$( \alpha , S _ { v , E } )$is either nonuniformly hyperbolic or$C ^ { \omega } .$-reducible, and the result follows.

This argument also works for Theorem$\mathrm { A } ^ { \prime }$, if we use Theorem 2.2 and Corollary 2.6 instead of Theorem 2.1 and Corollary 2.5.□

Acknowledgements. We would like to thank Hakan Eliasson, Svetlana Jitomirskaya, Barry Simon, and Jean-Christophe Yoccoz for several discussions and suggestions. We also thank the referee, whose comments were useful in improving the presentation of this article.

## Appendix A. Degree and and fibered rotation number

In this section we will recall the intrinsic definition of degree and fibered rotation number for actions given in [K2], and check that they coincide with the definitions given in §4.5. The advantage of the intrinsic definitions is that they allow us to compute easily the efect of base changes.

For$\alpha \in \mathbb { R }$and$A : \mathbb { R } \to \mathrm { S L } ( 2 , \mathbb { R } )$continuous, we introduce the following objects. If w is a point of the usual euclidean circle$\mathbb { S } ^ { 1 } \subset \mathbb { R } ^ { 2 } \equiv \mathbb { C }$we set

$$
f ^ {A} (x, w) = \frac {A \cdot w}{\| A \cdot w \|},\tag{A.1}
$$

and define, for$\alpha \in \mathbb { R }$2

$$
\begin{array}{c} F ^ {\alpha , A}: \mathbb {R} \times \mathbb {S} ^ {1} \to \mathbb {R} \times \mathbb {S} ^ {1} \\ (x, w) \mapsto (x + \alpha , f ^ {A} (x, w)). \end{array}\tag{A.2}
$$

If$\pi : \mathbb { R } \to \mathbb { S } ^ { 1 }$is the projection$\pi ( y ) = \exp ( 2 \pi i y )$we can find a continuous lift $d ^ { A } : \mathbb { R } \times \mathbb { R } \to \mathbb { R }$of$f ^ { A } ( x , w ) w ^ { - 1 }$, that is

$$
\pi (y + d ^ {A} (x, y)) = f ^ {A} (x, \pi (y)).\tag{A.3}
$$

Observe that such a lift is not uniquely defined, every other lift being of the form$d ^ { A } ( x , y ) + k _ { \cdot }$, where k is a constant integer. Also, for any$x , y \in \mathbb { R } \times \mathbb { R }$we have$d ^ { A } ( x , y + 1 ) = d ^ { A } ( x , y )$and thus$d ^ { A } ( x , w )$can be defined for any$x \in \mathbb { R }$ $w \in \mathbb { S } ^ { 1 }$

A.1. Cocycles. Let us first consider the case of a cocycle$( \alpha , A ) \in \mathbb { R } / \mathbb { Z } \times$ $C ^ { 0 } ( \mathbb { R } / \mathbb { Z } , { \mathrm { S L } } ( 2 , \mathbb { R } ) )$). Viewing A as defined on$\mathbb { R } .$we can define$d ^ { A } ~ \mathrm { ( u p ) }$to an integer), and we get$d ^ { A } ( x + 1 , w ) = d ^ { A } ( x , w ) + n$, where n is the topological degree of$\mathbb { R } / \mathbb { Z } \to \operatorname { S L } ( 2 , \mathbb { R } )$. Indeed, up to homotopy, we may assume that $A ( x ) = R _ { n x }$, and we have$d ^ { A } ( x , w ) = n x$

If$( \alpha , A )$is homotopic to the identity,$d ^ { A }$descends to a map$\mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 } \to \mathbb { R }$ and$F ^ { \alpha , A }$descends to a map$\mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 } \to \mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 }$. The usual definition (see [H], [JM]) of the fibered rotation number of$( \alpha , A )$is

$$
\rho (\alpha , A) = \int_ {\mathbb {R} / \mathbb {Z} \times \mathbb {S} ^ {1}} d ^ {A} (x, w) d \mu (x, w),\tag{A.4}
$$

(defined modulo an integer) where$\mu$is any probability measure which is invariant under$F ^ { A } : \mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 } \xrightarrow { } \mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 }$and which projects to Lebesgue measure on$\mathbb { S } ^ { 1 }$. One easily checks that if$x \in \mathbb { R }$and$w , w ^ { \prime } \in \mathbb { S } ^ { 1 }$then$\textstyle | \sum _ { k = 0 } ^ { n - 1 } d ^ { A }$◦ $\begin{array} { r } { ( F ^ { \alpha , A } ) ^ { k } ( x , w ^ { \prime } ) - \sum _ { k = 0 } ^ { n - 1 } d ^ { A } \circ ( F ^ { \alpha , A } ) ^ { k } ( x , w ) | < 1 } \end{array}$. This implies that

$$
\begin{array}{l} \left| n \int_ {\mathbb {R} / \mathbb {Z} \times \mathbb {S} ^ {1}} d ^ {A} (x, w) d \mu (x, w) - \int_ {\mathbb {R} / \mathbb {Z} \times \mathbb {S} ^ {1}} \sum_ {k = 0} ^ {n - 1} d ^ {A} \circ (F ^ {\alpha , A}) ^ {k} (x, w) d \mathrm{Leb} (x, w) \right| \\ = \left| \int_ {\mathbb {R} / \mathbb {Z} \times \mathbb {S} ^ {1}} \sum_ {k = 0} ^ {n - 1} d ^ {A} \circ (F ^ {\alpha , A}) ^ {k} (x, w) d \mu (x, w) \right. \\ \left. - \int_ {\mathbb {R} / \mathbb {Z} \times \mathbb {S} ^ {1}} \sum_ {k = 0} ^ {n - 1} d ^ {A} \circ (F ^ {\alpha , A}) ^ {k} (x, w) d \mathrm{Leb} (x, w) \right| <   1, \end{array}\tag{A.5}
$$

for every$n > 0$, so that$\begin{array} { r } { \rho ( \alpha , A ) { = } \operatorname* { l i m } \frac { 1 } { n } \int _ { \mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 } } \sum _ { k = 0 } ^ { n - 1 } d ^ { A } \circ ( F ^ { \alpha , A } ) ^ { k } ( x , w ) d \mathrm { L e b } ( x , w ) } \end{array}$ does not depend on$\mu .$.

A.2. Actions. Let$( e _ { 1 } , e _ { 2 } )$be a basis of the Z-module$\mathbb { Z } ^ { 2 }$. Then it is easy to see that the quantity

$$
\deg_ {e _ {1}, e _ {2}} \Phi = (d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {2})} + d ^ {A _ {e _ {2}} ^ {\Phi}}) - (d ^ {A _ {e _ {2}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1})} + d ^ {A _ {e _ {1}} ^ {\Phi}})\tag{A.6}
$$

is independent of the choices made for the lifts and is a constant integer. Obviously from$( \mathrm { A } . 6 ) , \deg _ { e _ { 2 } , e _ { 1 } } \Phi = - \deg _ { e _ { 1 } , e _ { 2 } } \Phi$. Notice that$d ^ { A _ { e _ { 1 } + e _ { 2 } } ^ { \Phi } } = d ^ { A _ { e _ { 1 } } ^ { \mp } } ,$◦ $F ^ { \Phi ( e _ { 2 } ) } + d ^ { A _ { e _ { 2 } } ^ { \Phi } }$(up to a constant integer), so that

$$
\begin{array}{l} \text {(A.7)} \deg_ {e _ {1}, e _ {1} + e _ {2}} \Phi = (d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1} + e _ {2})} + d ^ {A _ {e _ {1} + e _ {2}} ^ {\Phi}}) - (d ^ {A _ {e _ {1} + e _ {2}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1})} + d ^ {A _ {e _ {1}} ^ {\Phi}}) \\ = (d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1} + e _ {2})} + d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {2})} + d ^ {A _ {e _ {2}} ^ {\Phi}}) \\ \quad - (d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {2})} \circ F ^ {\Phi (e _ {1})} + d ^ {A _ {e _ {2}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1})} + d ^ {A _ {e _ {1}} ^ {\Phi}}) \\ = (d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1} + e _ {2})} + d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e_{2})} + d ^ {A _ {e _ {2}} ^ {\Phi}}) \\ \quad - (d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1} + e _ {2})} + d ^ {A _ {e _ {2}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1})} + d ^ {A _ {e _ {1}} ^ {\Phi}}) \\ = (d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {2})} + d ^ {A _ {e _ {2}} ^ {\Phi}}) - (d ^ {A _ {e _ {2}} ^ {\Phi}} \circ F ^ {\Phi (e _ {1})} + d ^ {A _ {e _ {1}} ^ {\Phi}}) = \deg_ {e _ {1}, e _ {2}} (\Phi). \end{array}
$$

A similar computation gives$\deg _ { e _ { 1 , - e _ { 2 } } } \Phi = - \deg _ { e _ { 1 , e _ { 2 } } } \Phi$. These elementary base change rules imply that$\deg _ { U \cdot e _ { 1 } , U \cdot e _ { 2 } } \Phi =$det$U \mathrm { d e g } _ { e _ { 1 } , e _ { 2 } }$Φ for any$U \in \operatorname { G L } ( 2 , \mathbb { Z } )$ We define deg Φ as$\deg _ { ( 0 , 1 ) , ( 1 , 0 ) } \Phi$. To see that this coincides with the previous definition (given in §4.5), it is enough to check it in the case of a normalized action$\Phi = \Phi _ { \alpha , A }$. Recalling that$d ^ { A } ( x + 1 , w ) = d ^ { A } ( x , w ) + n$where n is the topological degree of A : R$/ \mathbb { Z } \longrightarrow \mathrm { S L } ( 2 , \mathbb { R } )$, we get from$d ^ { A _ { ( 1 , 0 ) } ^ { \Phi } } = 0$and $d ^ { A _ { ( 0 , 1 ) } ^ { \Phi } } ( x , w ) = d ^ { A } ( x , w )$that$\deg ( \Phi ) = d ^ { A } ( x + 1 , w ) - d ^ { A } ( x , w ) = n$, according to the previous definition.

Assume now that the action Φ has degree zero. Let us denote by$\mathcal { M } ^ { \Phi }$the set of measures on$\mathbb { R } \times \mathbb { S } ^ { 1 }$which project on the first factor to Lebesgue measure on R and which are invariant by$F ^ { \Phi ( n , m ) }$for any$( n , m ) \in \mathbb { Z } ^ { 2 }$. It is not dificult to see that$\mathcal { M } ^ { \Phi }$is nonempty. Take as before$( e _ { 1 } , e _ { 2 } )$to be a basis of$\mathbb { Z } ^ { 2 }$, and for$\mu \in \mathcal { M } ^ { \Phi }$, define the quantity:

$$
\mathrm{rot} _ {e _ {1}, e _ {2}, \mu} \Phi = I (0, \gamma_ {e _ {2}} ^ {\Phi}; d ^ {A _ {e _ {1}} ^ {\Phi}}, \mu) - I (0, \gamma_ {e _ {1}} ^ {\Phi}; d ^ {A _ {e _ {2}} ^ {\Phi}}, \mu),\tag{A.8}
$$

where we have defined for any function$h : \mathbb { R } \times \mathbb { S } ^ { 1 } \to \mathbb { R }$and$( a , b ) \in \mathbb { R } ^ { 2 }$the quantity

$$
I (a, b; h, \mu) = \operatorname{sgn} (b - a) \int_ {[ a, b ] \times \mathbb {S} ^ {1}} h (x, v) d \mu (x, v).\tag{A.9}
$$

If we make other choices for the lifts of$F ^ { \Phi }$, the numbers we obtain just difer by the addition of an element of the module of frequency of Φ.

We notice that$\mathrm { r o t } _ { e _ { 2 } , e _ { 1 } , \mu } \Phi = - \mathrm { r o t } _ { e _ { 1 } , e _ { 2 } , \mu } \Phi$and

$$
\begin{array}{l} \mathrm{rot} _ {e _ {1}, e _ {1} + e _ {2}, \mu} \Phi = I (0, \gamma_ {e _ {1}} ^ {\Phi} + \gamma_ {e _ {2}} ^ {\Phi}; d ^ {A _ {e _ {1}} ^ {\Phi}}, \mu) - I (0, \gamma_ {e _ {1}} ^ {\Phi}; d ^ {A _ {e _ {1} + e _ {2}}} ^ {\Phi}, \mu) \\ = I (0, \gamma_ {e _ {2}} ^ {\Phi}; d ^ {A _ {e _ {1}} ^ {\Phi}}, \mu) + I (\gamma_ {e _ {2}} ^ {\Phi}, \gamma_ {e _ {1}} ^ {\Phi} + \gamma_ {e _ {2}} ^ {\Phi}; d ^ {A _ {e _ {1}} ^ {\Phi}}, \mu) - I (0, \gamma_ {e _ {1}} ^ {\Phi}; d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {2})} + d ^ {A _ {e _ {2}} ^ {\Phi}}, \mu) \\ = \mathrm{rot} _ {e _ {1}, e _ {2}, \mu} \Phi + I (\gamma_ {e _ {2}} ^ {\Phi}, \gamma_ {e _ {1}} ^ {\Phi} + \gamma_ {e _ {2}} ^ {\Phi}; d ^ {A _ {e _ {1}} ^ {\Phi}}, \mu) - I (0, \gamma_ {e _ {1}} ^ {\Phi}; d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi {(e _ {2})}}, \mu) = \mathrm{rot} _ {e _ {1}, e _ {2}, \mu} \Phi , \end{array}\tag{A.10}
$$

since

$$
\begin{array}{c} \int_ {[ 0, \gamma_ {e _ {1}} ^ {\Phi} ] \times \mathbb {S} ^ {1}} d ^ {A _ {e _ {1}} ^ {\Phi}} \circ F ^ {\Phi (e _ {2})} d \mu = \int_ {F ^ {\Phi (e _ {2})} ([ 0, \gamma_ {e _ {1}} ^ {\Phi} ] \times \mathbb {S} ^ {1})} d ^ {A _ {e _ {1}} ^ {\Phi}} d (F ^ {\Phi (e _ {2})}) _ {*} \mu \\ = \int_ {[ \gamma_ {e _ {2}} ^ {\Phi}, \gamma_ {e _ {1}} ^ {\Phi} + \gamma_ {e _ {2}} ^ {\Phi} ] \times \mathbb {S} ^ {1}} d ^ {A _ {e _ {1}} ^ {\Phi}} d \mu . \end{array}\tag{A.11}
$$

A similar computation gives$\mathrm { r o t } _ { e _ { 1 , - e _ { 2 } , \mu } } \Phi = - \mathrm { r o t } _ { e _ { 1 , e _ { 2 } , \mu } } \Phi$. Those elementary base change rules imply that$\mathrm { r o t } _ { U \cdot e _ { 1 } , U \cdot e _ { 2 } , \mu } \Phi = \operatorname* { d e t } U \mathrm { r o t } _ { e _ { 1 } , e _ { 2 } , \mu } \Phi$for any$U \in$ GL(2, Z).

Given$B : \mathbb { R } \to \mathrm { S L } ( 2 , \mathbb { R } )$continuous, we notice that$F _ { * } ^ { 0 , B } \mathcal { M } ^ { \Phi } = \mathcal { M } ^ { \mathrm { A d } _ { B } \Phi }$ and it follows immediately from the definition that

$$
\mathrm{rot} _ {e _ {1}, e _ {2}, \mu} \Phi = \mathrm{rot} _ {e _ {1}, e _ {2}, F _ {*} ^ {0, B} \mu} \mathrm{Ad} _ {B} \Phi .
$$

The transformation rule for$M _ { \lambda }$can be also readily checked: rot$M _ { \lambda } ( \Phi ) =$ $\lambda ^ { - 1 } \cot \Phi$

Let us check that$\mathrm { r o t } _ { e _ { 1 } , e _ { 2 } , \mu }$Φ does not depend on$\mu \in \mathcal { M }$. This is obvious if$\Gamma _ { \Phi } = \{ 0 \}$(in this case rot = 0). Otherwise, via conjugacies, scalings, and base change, we reduce to the case of checking that$\mathrm { r o t } _ { ( 0 , 1 ) , ( 1 , 0 ) , \mu } \Phi$does not depend on$\mu$when Φ is a normalized action$\Phi _ { \alpha , A }$. In this case, measures in $\mathcal { M } ^ { \Phi }$are invariant under$( x , w ) \mapsto ( x + 1 , w )$, and so they descend to$\mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 }$ Since$A : \mathbb { R } / \mathbb { Z } \to { \mathrm { S L } } ( 2 , \mathbb { R } )$is homotopic to the identity, we have$d ^ { A } ( x + 1 , w ) =$ $d ^ { A } ( x , w )$, so that$d ^ { A }$also descends to$\mathbb { R } / \mathbb { Z } \times \mathbb { S } ^ { 1 }$. We have

$$
\operatorname{rot} _ {(0, 1), (1, 0), \mu} \Phi = I (0, 1; d ^ {A}, \mu) = \int_ {\mathbb {R} / \mathbb {Z} \times \mathbb {S} ^ {1}} d ^ {A} (x, w) d \mu (x, w).\tag{A.12}
$$

This is precisely the usual definition of the fibered rotation number$\rho ( \alpha , A )$ (see §A.1), which does not depend on$\mu .$This also shows that setting rot Φ = $\mathrm { r o t } _ { ( 0 , 1 ) , ( 1 , 0 ) , \mu } \Phi$one recovers the previous definition (given in §4.5) of the fibered rotation number of a nondegenerate action.

College de France<sub>,</sub> Paris<sub>,</sub> France\`

Current address: CNRS UMR 7599, Universite Pierre et Marie Curie,<sup>´</sup>

E-mail address: artur@ccr.jussieu.fr

Universite Pierre et Marie Curie<sub>,</sub> Paris<sub>,</sub> France ´

E-mail address: krikoria@ccr.jussieu.fr

## References

[AA] S. Aubry and G. Andre, Analyticity breaking and Anderson localization in incommensurate lattices, in Group Theoretical Methods in Physics, Proc. Eighth Internat. Colloq. (Kiryat Anavim, 1979), Ann. Israel Phys. Soc. 3, 133–164, Hilger, Bristol, 1980.

[AK1] A. Avila and R. Krikorian, Quasiperiodic SL(2, R) cocycles, in preparation.

[AK2], Some remarks on local and semi-local results for Schr¨odinger cocycles, in preparation.

[ALM] A. Avila, M. Lyubich, and W. de Melo, Regular or stochastic dynamics in real analytic families of unimodal maps, Invent. Math. 154 (2003), 451–550.

[AMS] J. Avron, P. H. M. van Mouche, and B. Simon, On the measure of the spectrum for the almost Mathieu operator, Comm. Math. Phys. 132 (1990), 103–118.

[AS] J. Avron and B. Simon, Almost periodic Schr¨odinger operators. II. The integrated density of states, Duke Math. J. 50 (1983), 369–391.

[B]J. Bourgain, Green’s Function Estimates for Lattice Schr¨odinger Operators and Applications, Ann. of Math. Studies 158, Princeton Univ. Press, Princeton, NJ, 2005.

[BG] J. Bourgain and M. Goldstein, On nonperturbative localization with quasi-periodic potential, Ann. of Math. 152 (2000), 835–879.

[BJ1] J. Bourgain and S. Jitomirskaya, Continuity of the Lyapunov exponent for quasiperiodic operators with analytic potential, J. Statist. Phys. 108 (2002), 1203–1218.

[BJ2], Absolutely continuous spectrum for 1D quasiperiodic operators, Invent. Math. 148 (2002), 453–463.

[BF] V. Buslaev and A. Fedotov, On the diference equations with periodic coeficients, Adv. Theor. Math. Phys. 5 (2001), 1105–1168.

[DeS] P. Deift and B. Simon, Almost periodic Schr¨odinger operators. III. The absolutely continuous spectrum in one dimension, Comm. Math. Phys. 90 (1983), 389–411.

[DiS] E. I. Dinaburg and Ja. G. Sinai, The one-dimensional Schr¨odinger equation with quasiperiodic potential, Funk. Anal. i Priloˇzen. 9 (1975), 8–21.

[E1]L. H. Eliasson, Floquet solutions for the 1-dimensional quasi-periodic Schr¨odinger equation, Comm. Math. Phys. 146 (1992), 447–482.

[E2]Reducibility and point spectrum for linear quasi-periodic skew-products, Proc. Internat. Congress of Mathematicians, Vol. II (Berlin, 1998), Doc. Math. 1998, Extra Vol. II, 779–787.

[FK] A. Fedotov and F. Klopp, Anderson transitions for a family of almost periodic Schr¨odinger equations in the adiabatic case, Comm. Math. Phys. 227 (2002), 1–92.

[GS] M. Goldstein and W. Schlag, H¨older continuity of the integrated density of states for quasi-periodic Schr¨odinger equations and averages of shifts of subharmonic functions, Ann. of Math. 154 (2001), 155–203.

[GJLS] A. Y. Gordon, S. Jitomirskaya, Y. Last, and B. Simon, Duality and singular continuous spectrum in the almost Mathieu equation, Acta Math. 178 (1997), 169–183.

[HW] G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, Fifth edition, The Clarendon Press, Oxford Univ. Press, New York, 1979.

[HS] B. Helffer and J. Sjostrand ¨ , Semiclassical analysis for Harper’s equation. III. Cantor structure of the spectrum, Mem. Soc. Math. France´ 39 (1989), 1–124.

[H]M. Herman, Une m´ethode pour minorer les exposants de Lyapounov et quelques exemples montrant le caract\`ere local d’un th´eor\`eme d’Arnold et de Moser sur le tore de dimension 2, Comment. Math. Helv. 58 (1983), 453–502.

[Ho] D. R. Hofstadter, Energy levels and wave functions of Bloch electrons in a rational or irrational magnetic field, Phys. Rev. B 14 (1976), 2239–2249.

[I]K. Ishii, Localization of eigenstates and transport phenomena in one-dimensional disordered systems, Suppl. Prog. Theor. Phy. 53 (1973), 77–138.

[J]S. Jitomirskaya, Metal-insulator transition for the almost Mathieu operator, Ann. of Math. 150 (1999), 1159–1175.

[JK] S. Ya. Jitomirskaya and I. V. Krasovsky, Continuity of the measure of the spectrum for discrete quasiperiodic operators, Math. Res. Lett. 9 (2002), 413–421.

[JM] R. Johnson and J. Moser, The rotation number for almost periodic potentials, Comm. Math. Phys. 84 (1982), 403–438.

[Ko] A. N. Kolmogorov, On inequalities between the upper bounds of the successive derivatives of an arbitrary function on an infinite interval, Amer. Math. Soc. Transl. (1949), 19 pp.

<sup>[K1]</sup> <sup>R.</sup> <sup>Krikorian,</sup> <sup>Global</sup> <sup>density</sup> <sup>of</sup> <sup>reducible</sup> <sup>quasi-periodic</sup> <sup>cocycles</sup> <sup>on</sup> <sup>T</sup>×<sup>SU(2),</sup> <sup>Ann.</sup> of Math. 154 (2001), 269-326.

[K2], Reducibility, diferentiable rigidity and Lyapunov exponents for quasi-periodic cocycles on$\mathbb { T } \times \mathrm { S L } ( 2 , \mathbb { R } )$, preprint (www.arXiv.org, math.DS/0402333).

[L]Y. Last, Zero measure spectrum for the almost Mathieu operator, Comm. Math. Phys. 164 (1994), 421–432.

[LS] Y. Last and B. Simon, Eigenfunctions, transfer matrices, and absolutely continuous spectrum of one-dimensional Schr¨odinger operators, Invent. Math. 135 (1999), 329–367.

[Ly]M. Lyubich, Almost every real quadratic map is either regular or stochastic, Ann. of Math. 156 (2002), 1–78.

[Pa] J. Palis, A global view of dynamics and a conjecture on the denseness of finitude of attractors, Geom´ etrie Complexe et Syst´ emes Dynamiques\` (Orsay, 1995), Asterisque´ 261 (2000), 335–347.

[P]L. A. Pastur, Spectral properties of disordered systems in the one-body approximation, Comm. Math. Phys. 75 (1980), 179–196.

[Si1] B. Simon, Kotani theory for one-dimensional stochastic Jacobi matrices, Comm. Math. Phys. 89 (1983), 227–234.

[Si2], Schr¨odinger operators in the twenty-first century, in Mathematical Physics 2000, 283–288, Imperial College Press, London, 2000.

[SS] E. Sorets and T. Spencer, Positive Lyapunov exponents for Schr¨odinger operators with quasi-periodic potentials, Comm. Math. Phys. 142 (1991), 543–566.

[S]D. Sullivan, Reminiscences of Michel Herman’s first great theorem, in “Michael R. Herman” Gazette des Mathematiciens ´ 88, 90–93, Soc. Math. France, Paris, 2001.

[Y]J.-C. Yoccoz, Th´eor\`eme de Siegel, nombres de Bruno et polynˆomes quadratiques, in Petits Diviseurs en Dimension 1, Asterisque ´ 231, 3–88, Soc. Math. France, Paris, 1995.

(Received February 20, 2004)