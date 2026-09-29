JEAN BOURGAIN

Pointwise ergodic theorems for arithmetic sets

Publications mathématiques de l'I.H.É.S., tome 69 (1989), p. 5-41

&lt;http://www.numdam.org/item?id=PMIHES_1989__69__5_0&gt;

© Publications mathématiques de l'I.H.É.S., 1989, tous droits réservés.

L'accès aux archives de la revue « Publications mathématiques de l'I.H.É.S. » (http://www.ihes.fr/IHES/Publications/Publications.html) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

# POINTWISE ERGODIC THEOREMS FOR ARITHMETIC SETS by JEAN BOURGAIN

With an appendix on return-time sequences

jointly with HARRY FURSTENBERG, YITZHAK KATZNELSON and DONALD S. ORNSTEIN

## 1. Introduction

This paper is a development of the earlier work  $[B_{1}]$ ,  $[B_{2}]$ ,  $[B_{3}]$  of the author on extending Birkhoff's ergodic theorem to certain subsets of the integers. It was proved in  $[B_{1}]$  that given a dynamical system (DS, for short)  $(\Omega, \mathcal{B}, \mu, T)$  and a polynomial  $p(x)$  with integer coefficients, then the ergodic means

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{\mathrm{N}} \sum_ {1 \leqslant n \leqslant \mathrm{N}} \mathrm{T} ^ {p (n)} f\tag{1.1}
$$

converge almost surely for  $N \to \infty$ , assuming f a function of class  $\mathbf{L}^{2}(\Omega, \mu)$ . Here and in the sequel, one denotes by  $\mu$  a probability measure and by T a measure-preserving automorphism. The natural problem of developing the  $L^{p}$ -theory for p < 2 was studied in  $[B_{2}]$  and a partial result was obtained. We continue this line of investigation here.

The approach used in  $[B_{1}]$ ,  $[B_{2}]$  relies on a method which may be summarized as follows:

a) Reduction of the general problem to statements about the shift S on Z, which are of a “finite” and “quantitative” nature (in the sense of inequalities involving finitely many iterates of the transformation).

b) Proof of certain maximal function inequalities, relative to the shift, by Fourier Analysis methods.

c) Use of the “major arc” description of the relevant exponential sums, similar to that in the Hardy-Littlewood circle method.

As I observed in  $[B_{1}]$ , this approach should be considered more general than the solution to some isolated questions.

The purpose of this paper is two-fold. First, as far as the  $L^{2}$ -theory is concerned, we will develop appropriate harmonic analysis methods (maximal function estimates for certain sequences of multipliers), which will make the argument less dependent on special properties of the exponential sums (essentially exploited in  $[B_{1}]$ ,  $[B_{2}]$ ). Using this additional ingredient, further examples will be obtained, for instance sets of the form

$$
\Lambda = \{[ p (n) ]; n = 1, 2, \dots \}
$$

where $p(x)$ is any polynomial with real coefficients and $[x]$ stands for the integer part. Secondly, a method will be described to cover the full $L^p$-range, $p > 1$. In particular, it is shown that the averages $A_N f$ given by (1.1) converge almost surely for $f$ a function of class $L^p(\Omega, \mu), p > 1$. The problem for $L^1$-functions remains open at the present time. The shift reduction mentioned above allows one to give a new and simple proof of Birkhoff's ergodic theorem (cf. $[B_3]$). Our proof of the pointwise and maximal ergodic theorem is related to [K-W], but it is different and provides more quantitative information. In particular, in order to illustrate ideas, it will be shown how to avoid the invariance of the limit. When dealing with subsets of $Z$, this invariance is indeed not available in general and the pointwise ergodic theorem is not a formal consequence of the maximal ergodic theorem (except if the linear span of the eigenfunctions of $T$ is dense). The shift reduction applies equally well for positive isometries. Already for the sequence of squares $\Lambda = \{n^2\}$, the $L^p$-result for all $p > 1$ is new, and in particular the following corollary (for $p = 2$, see $[B_1]$):

Let $f$ be and $\mathbf{L}^{p}$-function on the circle $\pi = \mathbf{R}/\mathbf{Z}$ and $\alpha \in \mathbf{R} \backslash \mathbf{Q}$ an irrational number. Then the averages

$$
\frac {1}{N} \sum_ {n = 1} ^ {N} f (x + n ^ {2} \alpha)\tag{1.2}
$$

converge to the mean $\int_0^1 f(x)dx$, for almost all $x$.

It is tempting, especially for p = 2, to approach such a problem by straight forward Fourier Analysis, considering the Fourier expansion of the function f (cf. [S]). However, to make this method succeed, stronger information on the Fourier coefficients of f seems needed than just their square summability. The proof of the previous statement uses indeed harmonic analysis methods, but only after reduction to a dynamical system problem. Observe that in this case only the maximal inequality needs to be proven (p > 1)

$$
\int_ {0} ^ {1} \left(\sup _ {\mathbf {N}} \left[ \frac {1}{N} \sum_ {n \leqslant N} f (x + n ^ {2} \alpha) \right] ^ {p}\right) d x \leqslant c \int_ {0} ^ {1} f (x) ^ {p} d x\tag{1.3}
$$

for $f \geqslant 0$.

Next, we describe the organisation of the paper and state the main results.

In the next section, an approach to Birkhoff's theorem is presented along the lines explained above and some less known features of this result are pointed out.

In section 3, we considerer the variation spaces $v_{p}$, where $||x||_{v_p}$ is defined as

$$
\sup _ {s; j _ {1} <   \dots <   j _ {s}} (\Sigma | x _ {j _ {s - 1}} - x _ {j _ {s}} | ^ {p}) ^ {1 / p}, \quad x = (x _ {j}) _ {j = 1, 2, \dots}.\tag{1.4}
$$

These spaces are well-adapted for a quantitative formulation of convergence properties. In this context, we recall a result due to Lépingle on bounded martingales, which is of importance later on in the paper.

Section 4 is devoted to the proof of a maximal inequality for certain sequences of Fourier multipliers. These Fourier multipliers appear naturally in the “major arc” description of exponential sums. The results of section 4 are purely  $L^{2}$ .

In section 5, we recall some basic and well-known facts on the behaviour of exponential sums of the form

$$
\varphi_ {N} (\overline {{\alpha}}) = \sum_ {n = 0} ^ {N} e ^ {2 \pi i p (n, \overline {{\alpha}})}\tag{1.5}
$$

where

$$
p (x, \bar {\alpha}) = \alpha_ {d} x ^ {d} + \alpha_ {d - 1} x ^ {d - 1} + \dots + \alpha_ {1} x \quad \text { and } \quad \bar {\alpha} = (\alpha_ {1}, \dots , \alpha_ {d}) \in [ 0, 1 ] ^ {d}.\tag{1.6}
$$

The information on these sums needed for our purpose is essentially the same as for solving the Waring problem by the Hardy-Littlewood circle method.

Section 6 is a new presentation of the  $L^{2}$ -result on polynomial ergodic averages obtained in  $[B_{1}]$ , based on the new ingredient obtained in section 4. In this proof, we no longer need the a priori estimate of A. Weil for exponential sums with prime modulus.

Section 7 of this paper contains the corresponding (new) L$^{r}$-result for all r > 1. Thus the following theorem is proved:

Theorem 1. — Let  $(\Omega, \mathcal{B}, \mu, T)$  by a dynamical system and  $p(x)$  a polynomial with integer coefficients. Then there is the maximal inequality

$$
\left| \left| \sup _ {\mathbf {N}} \right| A _ {\mathbf {N}} f \right| \| _ {r} \leqslant C \| f \| _ {r}\tag{1.7}
$$

where $\mathbf{A}_{\mathbf{N}}f$ is given by (1.1), i.e.,

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{\mathrm{N}} \sum_ {1 \leqslant n \leqslant \mathbf {N}} \mathrm{T} ^ {p (n)} f
$$

and $f \in \mathbf{L}^r(\Omega, \mu), r > 1$. The constant $\mathbf{C}$ in (1.7) depends only on $r > 1$ and on the polynomial $p(x)$. Moreover, the averages $A_{N}f$ converge almost surely for $N \to \infty$. If $T$ is weakly mixing, the limit if given by $\int f d\mu$.

The previous result remains valid for positive isometries on  $\mathbf{L}^{\prime}(\Omega,\mu)$ . Let us point out that the proof of Theorem 1, in the case of a general polynomial  $p(x)$  with integer coefficients, is essentially identical to the special case  $p(x)=x^{2}$ . Essential use is made of duality and interpolation methods.

In section 8, the results of section 4 and section 5 are used to prove the following

Theorem 2. — Let  $(\Omega, \mathcal{B}, \mu, T)$  be a dynamical system and  $p(x)$  an arbitrary polynomial. Then the averages

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{\mathbf {N}} \sum_ {1 \leqslant n \leqslant \mathbf {N}} \mathrm{T} ^ {[ p (n) ]} f\tag{1.8}
$$

for $f$ any bounded measurable function on $\Omega$, converge almost surely. Here $[x]$ stands for the integer part of $x \in \mathbf{R}$.

It is possible to obtain  $L^{r}$ -results, r > 1, relative to the averages (1.8), at the price of additional technicalities, based on the method of proof for Theorem 1. This further development is not worked out in the paper.

Section 9 contains various comments and remarks on almost sure convergence in general, related to  $[B_{5}]$ .

## CONTENTS

1. Introduction ..... 1
2. Birkhoff's theorem revisited ..... 4
3. Variation spaces and variational inequalities ..... 8
4. Maximal inequalities for certain sequences of Fourier multipliers ..... 13
5. Behaviour of exponential sums ..... 19
6. Ergodic theorems in L² ..... 21
7. Ergodic theorem in L^p, p > 1 ..... 25
8. Integer parts of polynomial sequences ..... 34
9. Further comments and remarks on almost sure convergence ..... 36

The paper has an Appendix on return time sequences, in joint work with H. Furstenberg, Y. Katznelson and D. Ornstein, simplifying an earlier exposition  $[B_{4}]$  (cf. also  $[B_{6}]$ ).

## 2. Birkhoff's Theorem Revisited

Let $(\Omega, \mathcal{B}, \mu, T)$ be a dynamical system. In this section, we consider the usual ergodic averages $A_{N}f = \frac{1}{N}\sum_{1 \leqslant n \leqslant N} T^{n}f$ appearing in Birkhoff's ergodic theorem. We discuss their convergence properties, partly keeping in mind possible extensions to certain subsets of Z.

## A) Mean Convergence

The sequence of complex polynomials  $p_{\mathbf{N}}(z) = \frac{1}{\mathbf{N}} \sum_{n=1}^{\mathbf{N}} z^{n}$  pointwise converges on the unit circle (to 0 except for z = 1). Consequently, by general spectral theory of unitary operators,  $A_{N} f$  converges in  $\mathrm{L}^{2}(\mu)$  whenever  $f \in \mathrm{L}^{2}(\mu)$ . The main point here is the existence of a spectral measure. The Herglotz-Bochner theorem indeed ensures the existence of a positive Radon measure v on the circle T, such that

$$
\langle \mathrm{T} ^ {n} f, f \rangle = \widehat {\nu} (n) \equiv \int_ {0} ^ {1} e ^ {- 2 \pi i n \theta} \nu (d \theta)\tag{2.1}
$$

implying that the map  $\mathrm{L}^{2}(\Pi,\nu)\to\mathrm{L}^{2}(\Omega,\mu)$  mapping the nth character  $e^{2\pi in\theta}$  on  $T^{n}f$  is an isometry. Thus the convergence of  $A_{N}f$  in  $\mathrm{L}^{2}(\Omega,\mu)$  is equivalent to the convergence of  $p_{\mathbf{N}}(z)$  in  $\mathrm{L}^{2}(\Pi,\nu)$ .

This is clearly an  $L^{2}$ -theory. In general, given a subset  $\Lambda$  of the positive integers, the pointwise convergence on the unit circle of the sequence of polynomials

$$
p_{\mathbf{N}}(z) = \frac{1}{|\Lambda\cap[1,\mathbb{N}]|}\sum_{\substack{1\leqslant n\leqslant \mathbf{N}\\ n\in \Lambda}}z^{n}\tag{2.2}
$$

is equivalent with a mean ergodic theorem for the set $\Lambda$. In the case of “arithmetic sets” this test is particularly useful since the convergence of $p_{\mathbf{N}}(x)$ given by (4) is closely related to phenomena of uniform distribution. For instance, if $\Lambda$ is the set of squares $\{n^2 \mid n = 1, 2, \ldots\}$, we have

$$
p _ {\mathbf {N}} (e ^ {2 \pi i \alpha}) \rightarrow 0 \quad \text { if } \alpha \text { is   irrational }
$$

and

$$
p _ {N} (e ^ {2 \pi i \alpha}) \rightarrow S (q, a) \equiv \frac {1}{q} \sum_ {r = 0} ^ {q - 1} e ^ {2 \pi i \alpha r ^ {2}} \quad \text { for } \alpha = \frac {a}{q} \quad (\text { the   Gauss - sums }).
$$

It is not surprising that the (stronger) almost-sure convergence properties result from a finer analysis of these exponential sums and the class of $\mathbf{L}^2$-functions appears as the natural function space in these problems. A sequence $\Lambda \subset \mathbf{Z}_+$ is “ergodic” provided $p_{\mathbf{N}}(z) \to 0$ for $z \in \mathbf{T} - \{1\}$. The property implies mean convergence of $\mathrm{A}_{\mathbf{N}}f$ to $\int_{\Omega} f d\mu$, assuming T ergodic (this is the case for $\Lambda = \mathbf{Z}_+$ but not if $\Lambda = \{n^2 | n = 1, 2, \ldots\}$ for instance).

B. Weiss [W] observed that sequences  $\Lambda$  obtained by taking suitable unions of disjoint intervals are ergodic but may fail to satisfy the pointwise ergodic theorem, even with respect to bounded measurable functions.

## B) Maximal Ergodic Theorems

Let again

$$
\mathrm{A} _ {n} f = \frac {1}{\mathrm{N}} \sum_ {n = 1} ^ {\mathrm{N}} \mathrm{T} ^ {n} f
$$

and define the “ maximal function ”

$$
f ^ {*} = \sup _ {\mathbf {N} = 1, 2, \dots} | \mathrm{A} _ {\mathbf {N}} f |.
$$

There are the $\mathbf{L}^p$-inequalities ($1 < p \leqslant \infty$)

$$
\left| \left| f ^ {*} \right. \right| \left| _ {\mathrm{L} ^ {p} (\Omega , \mu)} \leqslant \mathrm{C} (p) \right. \left| \left| f \right| \right| _ {\mathrm{L} ^ {p} (\Omega , \mu)}\tag{2.3}
$$

and the weak-type inequality

$$
\left| \left| f ^ {*} \right. \right| \left| _ {\mathbf {L} ^ {1, \infty} (\Omega , \mu)} \leqslant \mathbf {C} \right. \left| \left| f \right| \right| _ {\mathbf {L} ^ {1} (\Omega , \mu)}\tag{2.4}
$$

where $||g||_{\mathbf{L}^{1,\infty}} = \sup_{\lambda > 0}\lambda \mu [|g| > \lambda]$ and $\mathbf{C}, \mathbf{C}(p)$ are absolute constants.

Let us give a simple proof (2.3), (2.4) by deriving them from the shift model (Z, S). In the case of the shift, the weak-type property (2.4) easily follows from geometric covering properties of integer-intervals, in the some way as for the Hardy-Littlewood maximal function on the real line. Once (2.4) is obtained, the  $L^{p}$ -inequalities follow from the Marcinkiewicz interpolation theorem. Consider now the case of the general dynamical system ( $\Omega$ ,  $\mu$ , T). Of course it suffices to prove inequalities (2.3), (2.4) (with fixed constants) for a “restricted” maximal function

$$
\bar {f} = \sup _ {1 \leqslant N \leqslant \overline {{N}}} A _ {N} f (f \leqslant 0)\tag{2.5}
$$

where  $\bar{N}$  is an arbitrarily chosen positive integer. Take an integer  $J \gg \bar{N}$  and for fixed  $x \in \Omega$ , consider the orbit

$$
x, \mathrm{T} x, \mathrm{T} ^ {2} x, \dots , \mathrm{T} ^ {\mathrm{J}} x.
$$

For the function f, define the function  $\varphi$  on Z as follows

$$
\left\{ \begin{array}{l l} \varphi (j) = f (\mathrm{T} ^ {j} x) & \text { if } 0 \leqslant j \leqslant \mathrm{J} \\ = 0 & \text { otherwise. } \end{array} \right.\tag{2.6}
$$

Thus $\mathbf{A}_{\mathbf{N}}\varphi (j) = \mathbf{A}_{\mathbf{N}}f(\mathbf{T}^{j}x)$ provided that $0\leqslant j <   \mathbf{J} - \mathbf{N}$ and hence, with the definition (2.5),

$$
\bar {\varphi} (j) = \bar {f} (\mathrm{T} ^ {j} x) \quad \text { for } 0 \leqslant j <   \mathrm{J} - \bar {\mathrm{N}}.\tag{2.7}
$$

The inequality $||\bar{\varphi}||_{\ell^p (\mathbb{Z})}\leqslant ||\varphi^{*}||_{\ell^p (\mathbb{Z})}\leqslant \mathrm{C}(p)||\varphi ||_{\ell^p (\mathbb{Z})}$ then immediately implies, by (2.6), (2.7),

$$
\sum_ {0 \leqslant j <   J - \overline {{N}}} | | \bar {f} (T ^ {j} x) | ^ {p} \leqslant C (p) ^ {p} \sum_ {0 \leqslant j \leqslant J} | f (T ^ {j} x) | ^ {p}.\tag{2.8}
$$

Integrating (2.8) in  $x \in \Omega$  with respect to the measure  $\mu$  yields

$$
\sum_ {0 \leqslant j <   J - \overline {{N}}} | | T ^ {j} \bar {f} | | _ {\mathfrak {p}} ^ {\mathfrak {p}} \leqslant C (p) ^ {\mathfrak {p}} \sum_ {0 \leqslant j <   J} | | T ^ {j} f | | _ {\mathfrak {p}} ^ {\mathfrak {p}}
$$

and since T is measure-preserving, one gets

$$
\left| \left| \bar {f} \right| \right| _ {\mathfrak {p}} \leqslant \mathrm{C} (p) \frac {\mathrm{J}}{\mathrm{J} - \bar {\mathrm{N}}} \left| \left| f \right| \right| _ {\mathfrak {p}},
$$

hence

$$
\left| \left| f ^ {*} \right| \right| _ {p} \leqslant \mathbf {C} (p) \left| \left| f \right| \right| _ {p}.
$$

One can deal similarly with the weak-type inequality (2.4). Assume $f \in \mathbf{L}^1(\Omega, \mu)$, $\lambda > 0$, let $\Omega_{\lambda} = [\bar{f} > \lambda]$ and $\chi$ be its indicator function. Given $x \in \Omega$, let $\varphi$ be defined as above and let $|I|$ stand for the cardinality of a (finite) subset $I$ of $Z$. The shift inequality thus gives

$$
\left| \left| \overline {{\varphi}} \right| \right| _ {\ell^ {1} \infty_ {(\mathbf {Z})}} \leqslant \mathrm{C} \left| \left| \varphi \right| \right| _ {\ell^ {1} (\mathbf {Z})}
$$

and, by (2.7),

$$
\lambda \left| \left\{0 \leqslant j <   J - \overline {{N}} \mid \bar {f} (T ^ {j} x) > \lambda \right\} \right| \leqslant C \sum_ {0 \leqslant j \leqslant J} f (T ^ {j} x),
$$

hence

$$
\sum_ {0 \leqslant j <   J - \overline {{N}}} \chi (T ^ {j} x) \leqslant \frac {C}{\lambda} \sum_ {0 \leqslant j \leqslant J} f (T ^ {j} x).\tag{2.9}
$$

Integrating again, we have

$$
\lambda \mu (\Omega_ {\lambda}) \leqslant \mathrm{C} \frac {\mathrm{J}}{\mathrm{J} - \overline {{\mathrm{N}}}} | | f | | _ {1},
$$

from which (2.4) easily follows.

At present, the covering argument leading to weak-type inequalities does not seem to be available when dealing with particular subsets of Z, such as the squares or the primes. In these cases, we were unable so far to develop an  $L^{1}$ -theory. The  $L^{2}$  and  $L^{2}$ -inequalities (p > 1) are obtained by making essential use of Fourier-transform methods. This is an approach similar to that in differentiation problems in real analysis involving lower-dimensional manifolds.

## C) Almost sure Convergence

By the maximal inequality and a standard truncation argument, the almost sure convergence of  $A_{N}f$  for f in  $\mathbf{L}^{1}(\Omega,\mu)$  reduces to bounded functions. Denote by F the  $L^{2}$ -limit of  $(\mathrm{A}_{\mathbf{N}}f)$  and, for given  $\varepsilon>0$, let  $N_{\varepsilon}$  satisfy

$$
\left| \left| F - A _ {N _ {\varepsilon}} f \right| \right| _ {2} <   \varepsilon .
$$

By the invariance of the limit (since the ergodic means relates to the full set of positive integers) and the maximal inequality, we have

$$
\left| \sup _ {\mathbf {N}} \right| \mathrm{F} - \mathrm{A} _ {\mathbf {N}} (\mathrm{A} _ {\mathbf {N} _ {\varepsilon}} f) \left| \right| _ {2} <   \mathrm{C} \varepsilon .\tag{2.10}
$$

Since

$$
\left| \mathrm{A} _ {\mathbf {N}} \left(\mathrm{A} _ {\mathbf {N} _ {\varepsilon}} f\right) - \mathrm{A} _ {\mathbf {N}} f \right| \leqslant 2 \frac {\mathrm{N} _ {\varepsilon}}{\mathrm{N}} \| f \| _ {\infty},
$$

it follows from (2.10) that

$$
\left| \left| \overline {{\lim}} \right| F - A _ {N} f \right| \| _ {2} <   C \varepsilon , \quad \text { hence } \quad \overline {{\lim}} _ {N} | F - A _ {N} f | = 0 \text { almost   surely. }
$$

This discussion completes the proof of Birkhoff's theorem. It is clear that the preceding argument does not apply when dealing with the more general averages

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{| \Lambda \cap [ 1 , \mathrm{N} ] |} \sum_ {n \in \Lambda , n \leqslant \mathbf {N}} \mathrm{T} ^ {n} f\tag{2.11}
$$

corresponding to a subset $\Lambda$ of $\mathbf{Z}_{+}$.

If the eigenfunctions of T generate a dense subspace of  $L^{2}$ , the almost sure conver-

gence of  $A_{N}f$  for f of class  $L^{p}$ ,  $p \leqslant 2$ , is implied by the pointwise convergence of the sequence  $p_{\mathbf{N}}(z)$ ,  $|z| = 1$ , given by (2.2) and the maximal inequality

$$
\left| \left| f ^ {*} \right| \right| _ {p} \leqslant C \left| \left| f \right| \right| _ {p}; \quad f ^ {*} = \sup | A _ {N} f |.
$$

This is the case for instance for the model $(\Omega, \mathbf{T}) = (\mathbf{T}, \mathbf{R}_a)$, $\mathbf{R}_a x = x + a$.

In the remainder of this section, an alternative method is explained for the purpose of proving the theorems stated in the introduction.

Take $f$ in $\mathbf{L}^{\infty}(\Omega, \mu)$, $|f| \leqslant 1$. For $\varepsilon > 0$, consider the subset

$$
Z _ {\varepsilon} = \left\{\left[ (1 + \varepsilon) ^ {n} \right] \mid n = 1, 2, \dots \right\}\tag{2.12}
$$

of  $Z_{+}$ . Clearly, for each  $N \in Z_{+}$ , there is  $N' \in Z_{\varepsilon}$  such that

$$
\left| \mathrm{A} _ {\mathrm{N}} f - \mathrm{A} _ {\mathrm{N} ^ {\prime}} f \right| \leqslant 2 \varepsilon .
$$

Thus to prove the almost sure convergence of $(\mathbf{A}_{\mathbf{N}}f)$, it suffices to show that there is no $\varepsilon > 0$ and no sequence of positive integers $\mathbf{N}_j, \mathbf{N}_{j+1} > 2\mathbf{N}_j$, such that

$$
\left|\left|\mathcal{M}_{j}f\right| \right|_{2} > \varepsilon \quad \text{where}\mathcal{M}_{j}f = \sup_{\substack{\mathrm{N}_{j}\leqslant \mathrm{N}\leqslant \mathrm{N}_{j + 1}\\ \mathrm{N}\in \mathrm{Z}_{\varepsilon}}}\left|\mathrm{A}_{\mathrm{N}}f - \mathrm{A}_{\mathrm{N}_{j}}f\right|.\tag{2.13}
$$

In fact, a more quantitative statement is shown, namely

$$
\sum_ {1 \leqslant j \leqslant J} | | \mathcal {M} _ {j} f | | _ {2} \leqslant o (J) | | f | | _ {2}\tag{2.14}
$$

for J large (depending on $\varepsilon$ appearing in the definition of $\mathcal{M}_j$). Since (2.14) only involves finitely many iterates of T, the general case reduces again to the shifts (Z, S). For the sets $\{p(n) \mid n = 1, 2, \ldots\}$ (resp. $\{[p(n)]; n = 1, 2, \ldots\}$) considered in Theorem 1 (resp. Theorem 2), the inequality (2.14) follows easily from the proof of the L²-maximal inequality. In the context of theorem 1, this argument was carried out in [B₁]. The method will be repeated in section 6 of this paper, for the sake of completeness.

## 3. Variation Spaces and Variational Inequalities

We start by recalling the definition of the variation norm $v_{s} (1 \leqslant s \leqslant \infty)$ for scalar sequences $\bar{x} = (x_{n})_{n=1,2,\ldots}$.

$$
\left| \left| \bar {x} \right| \right| _ {v _ {s}} = \sup \left\{\left(\sum_ {j = 1} ^ {J} \left| x _ {n _ {j}} - x _ {n _ {j + 1}} \right| ^ {s}\right) ^ {1 / s} \mid J = 1, 2, \dots \text {   and   } n _ {1} <   n _ {2} <   \dots <   n _ {J} \right\}.\tag{3.1}
$$

The sequence space $v_s$ then consists of those sequences $\bar{x}$ for which $||\bar{x}||_{v_s} < \infty$. We will also use the notation $||\|_{v_s}$ for continuously indexed systems $\bar{x} = (x_t)_{t > 0}$, where now

$$
\left| \left| \bar {x} \right| \right| _ {v _ {s}} = \sup \left\{\left(\sum_ {j = 1} ^ {s} \left| x _ {t _ {j}} - x _ {t _ {j + 1}} \right| ^ {s}\right) ^ {1 / s} \mid J = 1, 2, \dots \text {   and   } t _ {1} <   t _ {2} <   \dots <   t _ {J} \right\}.\tag{3.2}
$$

These spaces  $v_{s}$  are frequently used in probability theory when studying questions about convergence. In this context, some known inequalities about martingales are needed for our purpose. More precisely, we will use the following result due to Lépingle [Lé] (cf. also [P-X]).

Lemma 3.3. — Let $\mathbf{E}_{n}$ ($n=1,2,\ldots$) be the sequence of expectation operators with respect to an increasing sequence of $\sigma$-algebras on a probability space and $f_{n}=\mathbf{E}_{n}f$ an associated scalar martingale. Then, for $s>2$, we have the inequality

$$
\left| \left| \left\{f _ {n} \right\} \right| \right| _ {\mathrm{L} _ {v _ {s}} ^ {2}} \leqslant c (s - 2) ^ {- 1} \left| \left| f \right| \right| _ {\mathrm{L} ^ {2}}\tag{3.4}
$$

where  $L_{v_{s}}^{2}$  refers to the  $v_{s}$ -valued  $L^{2}$ -space.

This result may be seen as the quantitative form of the martingale convergence theorem. The inequality (3.4) fails for s = 2 (this is a well-known feature of the Brownian martingale, related to the law of the iterated logarithm). In fact, the dependence in s stated in (3.4) will be of relevance later on and we include a fast proof here.

Proof of (3.4). — For  $\lambda > 0$ , denote by  $\mathrm{N}_{\lambda}(\omega)$  the number of  $\lambda$ -jumps in the sequence  $\{f_{n}(\omega)\}$ , where  $f_{n}$  is defined as above. One has the following inequality for  $1 < r < \infty$ :

$$
\left| \left| \lambda (N _ {\lambda}) ^ {1 / 2} \right| \right| _ {r} \leqslant c _ {r} \left| \left| f \right| \right| _ {r} \quad \text { for   all } \lambda > 0.\tag{3.5}
$$

This is a form of Doob's oscillation lemma for martingales (see [Nev]) and is obtained by methods of stopping times and square functions. We use interpolation to derive (3.4) from (3.5). First we prove $(\mathbf{L}^{\mathfrak{p},1}$ denoting the Lorentz space):

$$
\left| \left| \left\{f _ {n} \right\} \right| \right| _ {\mathrm{L} _ {v _ {s}} ^ {p}} \leqslant c (s - 2) ^ {- 1 / p} \left| \left| f \right| \right| _ {\mathrm{L} ^ {p, 1}} \quad \text { for } \frac {3}{2} \leqslant p \leqslant s <   \frac {5}{2}, \quad s > 2.\tag{3.6}
$$

Let thus $f = \chi_{\mathbf{A}}$ and $\mathbf{A} \subset \Omega$ be a measurable set of measure $\mu(\mathbf{A}) = \varepsilon$, hence $||f||_{p,1} = \varepsilon^{1/p}$. Estimate pointwise, for $N_{\lambda}$ defined as above from the function $f$, yields

$$
\left| \left| \left\{f _ {n} (\omega) \right| \right| _ {v _ {s}} \leqslant \left[ \sum_ {k = 0} ^ {\infty} 2 ^ {- k s} \mathrm{N} _ {2 - k} (\omega) \right] ^ {1 / s}. \right.\tag{3.7}
$$

Hence, since $p \leqslant s$,

$$
\left| \left| \left\{f _ {n} \right\} \right| \right| _ {\mathrm{L} _ {v _ {s}} ^ {p}} \leqslant 2 \left[ \sum_ {k = 0} ^ {\infty} 2 ^ {- k p} \int_ {\Omega} \left(\mathrm{N} _ {2 - k}\right) ^ {p / s} d \omega \right] ^ {1 / p} \leqslant c [ \sum 2 ^ {- k p (1 - (2 / s))} | | f | | _ {r} ^ {r} ] ^ {1 / p}\tag{3.8}
$$

applying (3.5) with $r = 2p / s$ (which implies $6/5 \leqslant r < 2$ in view of the hypotheses made on $p, s$) and $\lambda = 2^{-k}$. Since $||f||_r^r = \varepsilon$, (3.6) is immediate from (3.8). Writing $\mathbf{L}^2$ as interpolation space between $\mathbf{L}^{s,1}$ and $\mathbf{L}^{3/2}$, (3.6) is easily seen to imply (3.4).

We will now derive a real analysis version of (3.4) from Lemma 3.3. For a function $f$ on $\mathbf{R}$, set $f_{t}(x) = \frac{1}{t} f\left(\frac{x}{t}\right)$. Denote also by

$$
\mathcal {F} f (\lambda) \equiv \hat {f} (\lambda) = \int_ {- \infty} ^ {\infty} f (x) e ^ {- 2 \pi i \lambda x} d x\tag{3.9}
$$

the Fourier transform of $f$. Thus

$$
\hat {f} _ {t} (\lambda) = \hat {f} (t \lambda).\tag{3.10}
$$

Lemma 3.11. — Let $\chi = \chi_{[0,1]}$ be the indicator function of the interval [0, 1]. Then, for $f \in \mathbf{L}^2(\mathbb{R})$ and $s > 2$, one has

$$
\left| \left| \left\{f * \chi_ {t} \mid t > 0 \right\} \right| \right| _ {L _ {v _ {s}} ^ {2} (\mathbb {R})} \leqslant c (s - 2) ^ {- 1} \| f \| _ {2},\tag{3.12}
$$

where $v_{s}$ stands for $v_{s}(\mathbf{R}_{+})$ with the norm given by (3.2).

As usual, $f * g$ denotes the convolution of $f$ and $g$.

Denote by $(\mathbf{P}_t)_{t > 0}$ the Poisson semi-group on $\mathbb{R}$. Thus if $\mathbf{P}_t f = f * \mathbf{P}_t$, one has $\hat{\mathbf{P}}_t(\lambda) = e^{-i|\lambda|}$. Considering the Brownian martingale associated to the harmonic function $u(x,t) = (f*\mathbf{P}_t)(x)$ on the upper half-plane or, alternatively, invoking Rota's dilation theorem, inequality (3.4) relative to martingales implies

$$
\left| \left| \left\{\mathrm{P} _ {t} f \mid t > 0 \right\} \right| \right| _ {\mathrm{L} _ {v _ {s}} ^ {2}} \leqslant c (s - 2) ^ {- 1} \left| \left| f \right| \right| _ {2}.\tag{3.13}
$$

Proof of Lemma 3.11. — By (3.13), (3.12) will be a consequence of the following inequality

$$
\left| \left| \left\{f * \mathrm{K} _ {t} \mid t > 0 \right\} \right| \right| _ {\mathrm{L} _ {v _ {2}} ^ {2}} \leqslant c \| f \| _ {2},\tag{3.14}
$$

where K stands for the function  $\chi - P_{1}$ , hence satisfies the Fourier transform estimates

$$
\mid \lambda \mid . \left| (\hat {\mathbf {K}}) ^ {\prime} (\lambda) \right| <   c \quad \text { and } \quad \mid \hat {\mathbf {K}} (\lambda) \mid \leqslant c \min (| \lambda |, | \lambda | ^ {- 1}).\tag{3.15}
$$

We clearly have the pointwise estimate

$$
\begin{array}{r l} \left| \left| \left\{f * \mathrm{K} _ {t} \mid t > 0 \right\} \right| \right| _ {v _ {2}} & \leqslant (\sum_ {k \in \mathbb {Z}} | f * \mathrm{K} _ {2 ^ {k}} | ^ {2}) ^ {1 / 2} \\ & + (\sum_ {k \in \mathbb {Z}} | | \left\{f * \mathrm{K} _ {t} \mid 2 ^ {k} \leqslant t \leqslant 2 ^ {k + 1} \right\} | | _ {v _ {3}} ^ {2}) ^ {1 / 2}. \end{array}\tag{3.16}
$$

By Parseval's identity, the  $L^{2}$ -norm of the first term in (3.16) is bounded by

$$
\left[ \sum_ {k \in \mathbf {Z}} \int_ {- \infty} ^ {\infty} | \hat {f} (\lambda) | ^ {2} \mid \hat {\mathrm{K}} (2 ^ {k} \lambda) | ^ {2} d \lambda \right] ^ {1 / 2} \leqslant c. \left[ \int | \hat {f} (\lambda) | ^ {2} d \lambda \right] = c \| f \| _ {2},\tag{3.17}
$$

invoking also (3.5).

Next, we estimate the contribution of the second term

$$
\{\sum_ {k \in \mathbf {Z}} | | \{f * \mathrm{K} _ {t} \mid 2 ^ {k} \leqslant t \leqslant 2 ^ {k + 1} \} | | _ {\mathrm{L} _ {v _ {3}} ^ {2}} ^ {2} \} ^ {1 / 2}.\tag{3.18}
$$

Let $0 < \eta < 1$ be a function supported by $\left[\frac{1}{2}, 2\right] \cup \left[-2, -\frac{1}{2}\right]$, $|\eta'| < C$, such that

$$
\sum_ {\alpha \in \mathbf {Z}} \eta (2 ^ {\alpha} \lambda) = 1.
$$

Defining $\mathbf{K}_{\alpha}$ by $\hat{\mathbf{K}}_{\alpha}(\lambda) = \hat{\mathbf{K}}(\lambda)\eta(2^{\alpha}\lambda)$, one has that $\mathbf{K} = \sum_{\alpha}\mathbf{K}_{\alpha}$, and (3.18) may be estimated by the triangle inequality as

$$
\sum_ {\alpha \in \mathbf {Z}} \left\{\sum_ {k \in \mathbf {Z}} | | \{f * (\mathrm{K} _ {\alpha}) _ {t} \mid 2 ^ {k} \leqslant t \leqslant 2 ^ {k + 1} \} | | _ {\mathrm{L} _ {v _ {3}} ^ {2}} ^ {2} \right\} ^ {1 / 2}.\tag{3.19}
$$

From (3.15),

$$
| \lambda | | (\hat {\mathbf {K}} _ {\alpha}) ^ {\prime} (\lambda) | <   c \quad \text { and } \quad | \hat {\mathbf {K}} _ {\alpha} (\lambda) | <   c 2 ^ {- | \alpha |}.\tag{3.20}
$$

Fix $\alpha \in \mathbf{Z}$. For $k \in \mathbf{Z}$, consider a net $2^k = u_1 < u_2 < \ldots < u_N = 2^{k+1}$ of $N = N_\alpha$ equidistributed points. The number $N_\alpha$ will be specified later. Estimate

(3.21)

$$
\begin{array}{r l} & {\left| \left| \left\{f * (\mathrm{K} _ {\alpha}) _ {t} \mid 2 ^ {k} \leqslant t \leqslant 2 ^ {k + 1} \right\} \right| \right| _ {v _ {2}} \leqslant} \\ & {\quad \left[ \sum_ {\ell = 1} ^ {\mathrm{N}} | f * (\mathrm{K} _ {\alpha}) _ {u _ {\ell}} | ^ {2} \right] ^ {1 / 2} +} \\ & {\quad \left\{\sum_ {\ell = 1} ^ {\mathrm{N}} \left[ \int_ {u _ {\ell}} ^ {u _ {\ell + 1}} | \partial_ {t} [ f * (\mathrm{K} _ {\alpha}) _ {t} ] | d t \right] ^ {2} \right\} ^ {1 / 2}} \end{array}\tag{3.22}
$$

majorizing $v_{2}([u_{\ell}, u_{\ell+1}])$ by $v_{1}([u_{\ell}, u_{\ell+1}])$.

Again by Parseval's identity, the  $L^{2}$ -norm of (3.21) is bounded by

$$
\left[ \sum_ {\ell = 1} ^ {N} \int_ {- \infty} ^ {\infty} | \hat {f} (\lambda) | ^ {2} | \hat {K} _ {\alpha} (u _ {\ell} \lambda) | ^ {2} d \lambda \right] ^ {1 / 2} \leqslant C N _ {\alpha} ^ {1 / 2} 2 ^ {- | \alpha |} \left[ \int_ {| \lambda | \sim 2 ^ {- \alpha - k}} | \hat {f} (\lambda) | ^ {2} d \lambda \right] ^ {1 / 2}\tag{3.23}
$$

by the definition of $\mathbf{K}_{\alpha}$ and (3.20). Here $|\lambda| \sim \rho$ stands for $\frac{1}{4}\rho < |\lambda| < 4\rho$. Similarly, the $\mathbf{L}^2$-norm of (3.22) is bounded by

$$
\begin{array}{r l} & {\left[ \sum_ {\ell = 1} ^ {N} (u _ {\ell + 1} - u _ {\ell}) \int_ {u _ {\ell}} ^ {u _ {\ell + 1}} \left[ \int_ {- \infty} ^ {\infty} | \hat {f} (\lambda) | ^ {2} | \lambda | ^ {2} | (\hat {K} _ {\alpha}) ^ {\prime} (t \lambda) | ^ {2} d \lambda \right] d t \right] ^ {1 / 2} \leqslant} \\ & {\qquad \mathrm{C} \left[ \sum_ {\ell = 1} ^ {N} \left(\frac {2 ^ {k}}{N}\right) ^ {2} 4 ^ {- k} \left(\int_ {| \lambda | \sim 2 ^ {- k - \alpha}} | \hat {f} (\lambda) | ^ {2} d \lambda\right) \right] ^ {1 / 2}} \\ & {\qquad = \mathrm{CN} _ {\alpha} ^ {- 1 / 2} \left[ \int_ {| \lambda | \sim 2 ^ {- k - \alpha}} | \hat {f} (\lambda) | ^ {2} d \lambda \right] ^ {1 / 2}.} \end{array}\tag{3.24}
$$

Substitution of estimates (3.23), (3.24) in (3.19) finally gives the bound

$$
\left[ \sum_ {\alpha , k \in \mathbb {Z}} \left(\mathrm{N} _ {\alpha} 4 ^ {- | \alpha |} + \mathrm{N} _ {\alpha} ^ {- 1}\right) \left(\int_ {| \lambda | \sim 2 ^ {- k - \alpha}} | \hat {f} (\lambda) | ^ {2} d \lambda\right) \right] ^ {1 / 2} \leqslant \mathrm{C} \| \hat {f} \| _ {2} = \mathrm{C} \| f \| _ {2},
$$

chosing  $N_{\alpha}=2^{|\alpha|}$ .

Summation of (3.17), (3.18) yields (3.14), which proves Lemma 3.11.

Let us point out one application of Lemma 3.11 to the convergence of the averages

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{\overline {{\mathbf {N}}}} \sum_ {1 \leqslant n \leqslant \mathbf {N}} \mathbf {T} ^ {n} f
$$

in Birkhoff's theorem.

Corollary 3.25. — Let $(\Omega, \mathbf{K}, \mu, \mathbf{T})$ be a DS and $f \in \mathbf{L}^2(\mu)$. Then, for $s > 2$,

$$
\left| \left| \left\{\frac {1}{N} \sum_ {n \leqslant N} T ^ {n} f | N = 1, 2, \dots \right\} \right| \right| _ {L _ {v _ {s}} ^ {2}} \leqslant c (s) \| f \| _ {2}.\tag{3.26}
$$

The last result does not seem to appear in the literature. It refines the results discussed in the previous section (related to almost sure convergence). The proof of  $(3.26)$  reduces to the particular case of the shift model  $(\mathbf{Z}, \mathbf{S})$ , following the procedure described in section 2 of this paper. In the context of the shift,  $(3.26)$  is just a discrete version of  $(3.12)$ .

Writing

$$
\varphi = - \int_ {0} ^ {\infty} \chi_ {t} \cdot \varphi^ {\prime} (t) t d t, \quad \chi_ {t} = \frac {1}{t} \chi_ {[ 0, t ]},\tag{3.27}
$$

for a smooth function $\varphi$ on $[0, \infty]$, vanishing at $\infty$, the following lemma is a consequence of (3.12) and the convexity.

Lemma 3.28. — Let $\varphi$ be a differentiable function on $\mathbf{R}$, vanishing at $\infty$. Then, for $s > 2$,

$$
\left| \left| \left\{f * \varphi_ {t} \mid t > 0 \right\} \right| \right| _ {\mathrm{L} _ {v _ {s}} ^ {2}} \leqslant c. (s - 2) ^ {- 1} \left(\int_ {- \infty} ^ {\infty} | \varphi^ {\prime} (x) | | x | d x\right) \| f \| _ {2}.\tag{3.29}
$$

We conclude this section with a corollary of  $(3.28)$  which will be of importance in the proof of certain Fourier-multiplier maximal inequalities considered in the next section.

Let H be a Hilbert space. If A is a subset of H, denote by  $\mathbf{M}_{\lambda}(\mathbf{A})$  the  $\lambda$ -entropy number of A,  $\lambda > 0$ . By  $\lambda$ -entropy number, we mean the minimal number ( $\leqslant \infty$ ) of balls (with respect to the H-norm) of radius  $\lambda$ , needed to cover A. We set  $M_{\lambda} = 0$  if diam A <  $\lambda$ . The following result relates to H-valued functions on R.

Lemma 3.30. — Let $\varphi$ be as in (3.28), $s > 2$ and H a Hilbert space. Then, for $f \in \mathbf{L}_{\mathbf{H}}^{2}(\mathbf{R})$,

$$
\left| \sup _ {\lambda > 0} \left(\lambda \mathrm{M} _ {\lambda} ^ {1 / s}\right) \right| | _ {2} \leqslant c _ {\varphi} (s - 2) ^ {- 1} \| f \| _ {2},\tag{3.31}
$$

where one defines pointwise $\mathrm{M}_{\lambda}(x) = \mathrm{M}_{\lambda}(\{(f*\varphi_t)(x)\mid t > 0\})$ and $\mathbf{C}_{\varphi} = \int |\varphi '(x)||x|dx.$

Proof. — Observe first the pointwise inequality

$$
\lambda \mathrm{M} _ {\lambda} (x) ^ {1 / s} \leqslant \left\{\sum_ {j} \left| \left(f * \varphi_ {t _ {j}}\right) (x) - \left(f * \varphi_ {t _ {j - 1}}\right) (x) \right| \right| _ {\mathbf {H}} ^ {s} \} ^ {1 / s} \leqslant \left| \left| \left\{\left(f * \varphi_ {t}\right) (x) \right\} \right| \right| _ {v _ {s}},\tag{3.32}
$$

where $\bar{t} = (t_j)$ is defined by putting

$$
t _ {j} = \min \left\{t > t _ {j - 1} \mid \left| \left| (f * \varphi_ {t}) (x) - (f * \varphi_ {t _ {j - 1}}) (x) \right| \right| _ {\mathbf {H}} > \lambda \right\}.
$$

(Since we are concerned with a priori inequalities, we may take the sequence $\bar{t} = (t_j)$ of bounded length.)

Writing $f = \sum f_{\alpha} e_{\alpha}, f_{\alpha} = \langle f, e_{\alpha} \rangle$, where $\{e_{\alpha}\}$ is an orthonormal basis for H, it follows from (3.32), (3.29) and the convexity $(s > 2)$, that

$$
\left| \left| \sup _ {\lambda > 0} \left(\lambda M _ {\lambda} ^ {1 / s}\right) \right| \right| _ {2} \leqslant \left[ \sum_ {\alpha} \left| \left| \left\{f _ {\alpha} * \varphi_ {t} \right\} \right| \right| _ {L _ {v _ {s}} ^ {2}} ^ {2} \right] ^ {1 / 2} \leqslant c _ {\varphi} (s - 2) ^ {- 1} \left(\sum_ {\alpha} \left| \left| f _ {\alpha} \right| \right| _ {2} ^ {2}\right) ^ {1 / 2}.
$$

This proves (3.31).

Lemma 3.33. — Let $\varphi$ be as in (3.28) and H be a Hilbert space. Then, with the notation of (3.30) and for $f \in \mathbf{L}_{\mathbf{H}}^{2}(\mathbf{R})$ and K > 0, one has

$$
\left| \left| \int_ {0} ^ {\infty} \min (\mathrm{K}, \mathrm{M} _ {\lambda} (x)) ^ {1 / 2} d \lambda \right| \right| _ {2} \leqslant c _ {\varphi} ^ {\prime} (\log \mathrm{K}) ^ {2} | | f | | _ {2}.\tag{3.34}
$$

Proof. — With the notation of the proof of Lemma 3.30, set

$$
f _ {\alpha} ^ {*} = \sup _ {t > 0} | f _ {\alpha} * \varphi_ {t} |; \quad f _ {\alpha} = \langle f, e _ {\alpha} \rangle
$$

so that

$$
\left| \left| f _ {\alpha} ^ {*} \right| \right| _ {2} \leqslant c _ {\varphi} \left| \left| f _ {\alpha} \right| \right| _ {2}\tag{3.35}
$$

by the Hardy-Littlewood maximal inequality. Define

$$
\mathrm{F} = [ \Sigma (f _ {\alpha} ^ {*}) ^ {2} ] ^ {1 / 2}\tag{3.36}
$$

and, for $s > 2$, write

$$
\begin{array}{r l} \int_ {0} ^ {\infty} \min (\mathrm{K}, \mathrm{M} _ {\lambda} (x)) ^ {1 / 2} d \lambda & \leqslant \mathrm{F} (x) + \int_ {\mathbf {K} ^ {- 1 / s} \mathbf {F} (x)} ^ {\mathbf {F} (x)} \mathrm{K} ^ {\frac {1}{2} - \frac {1}{s}} \mathrm{M} _ {\lambda} (x) ^ {1 / s} d \lambda \\ & \leqslant \mathrm{F} (x) + \mathrm{K} ^ {\frac {1}{2} - \frac {1}{s}} (\log \mathrm{K}) \sup _ {\lambda > 0} \lambda . \mathrm{M} _ {\lambda} (x) ^ {1 / s}. \end{array}
$$

Now, (3.34) follows from (3.35), (3.36) and (3.31), letting $\frac{1}{2} - \frac{1}{s} = (\log K)^{-1}$.

## 4. Maximal Inequalities for Certain Sequences of Fourier Multipliers

Proving the  $L^{2}$ -maximal inequality in Theorems 1 and 2 in the context of the shift (Z, S) by harmonic analysis methods leads to Fourier multipliers given by exponential sums (the properties of which will be recalled in the next section). In this section a rather general estimate is obtained, especially motivated by the major arc description of these exponential sums.

The dual group of $\mathbf{Z}$ is the circle group $\Pi = \mathbf{R} / \mathbf{Z}$, which will be identified with [0, 1] (identifying 0 and 1).

The main result of this section is contained in

Lemma 4.1. — Assume $\lambda_{1} < \ldots < \lambda_{K} \in \Pi$ and, for $j \in \mathbf{Z}_{+}$, define the neighborhoods

$$
\mathrm{R} _ {j} = \{\lambda \in \Pi | \min _ {\mathbf {1} \leqslant k \leqslant \mathbf {K}} | \lambda - \lambda_ {k} | \leqslant 2 ^ {- j} \}.\tag{4.2}
$$

Then

$$
\left| \left| \sup _ {j} \left| \int_ {\mathbf {R} _ {j}} \hat {f} (\lambda) e ^ {2 \pi i \lambda x} d \lambda \right| \right| \right| _ {\ell^ {2} (\mathbf {Z})} \leqslant \mathrm{C} (\log \mathrm{K}) ^ {2} | | f | | _ {\ell^ {2} (\mathbf {Z})}\tag{4.3}
$$

for functions $f$ on $\mathbf{Z}$.

Remark. — It is an interesting question whether there needs to be a dependence on the number K of base points in (4.3). The logarithmic dependence will suffice for our purpose.

In order to simplify notation, we denote by $\mathcal{F}$ (resp. $\mathcal{F}^{-1}$) the Fourier transform (resp. inverse Fourier transform) for functions on either $\mathbf{R}$ or $\mathbf{Z}$.

For the sake of completeness, we include the following known argument to derive the corresponding inequality for Z from the R case. Indeed, it is often more appealing to prove the result on R because of the presence of the dilation structure.

Lemma 4.4. — Let $\Phi$ be a set of multipliers on $[0,1]$ satisfying

(4.5)

$$
\left| \sup _ {\varphi \in \Phi} \right| \mathcal {F} ^ {- 1} [ \varphi \mathcal {F} f ] | | _ {\mathrm{L} ^ {2} (\mathbf {R})} \leqslant \mathrm{B} | | f | | _ {\mathrm{L} ^ {2} (\mathbf {R})}.\tag{Then}
$$

$$
\left| \right| \sup _ {\varphi \in \Phi} | \mathcal {F} ^ {- 1} [ \varphi \mathcal {F} f ] | | | _ {\ell^ {2} (\mathbf {Z})} \leqslant \mathrm{CB} | | f | | _ {\ell^ {2} (\mathbf {Z})}\tag{4.6}
$$

where $\mathbf{C}$ is an absolute constant.

Proof. — Denote by  $B_{1}$  the best constant satisfying (4.6). Writing, for  $x \in Z$  and  $u \in [0, \rho] (\rho < 1$  to be specified later),

$$
\mathcal {F} ^ {- 1} [ \varphi \mathcal {F} f ] (x) = \mathcal {F} ^ {- 1} [ \varphi \mathcal {F} f ] (x + u) + \mathcal {F} ^ {- 1} [ (1 - e ^ {2 \pi i \lambda u}) \varphi \mathcal {F} f ] (x)
$$

and averaging in $u$ gives

(4.7)

$$
\begin{array}{r l} & {| | \sup _ {\varphi} | \mathcal {F} ^ {- 1} [ \varphi \mathcal {F} f ] | | | _ {\ell^ {2} (\mathbb {Z})} \leqslant} \\ & {\qquad \rho^ {- 1 / 2} | | \sup _ {\varphi} | \mathcal {F} ^ {- 1} [ \varphi \mathcal {F} f ] | | | _ {L ^ {2} (\mathbb {R})} +} \\ & {\qquad \sup _ {0 <   u <   \rho} | | \sup _ {\varphi} | \mathcal {F} ^ {- 1} [ (1 - e ^ {2 \pi i \lambda u}) \varphi \mathcal {F} f ] | | | _ {\ell^ {2} (\mathbb {Z})}.} \end{array}\tag{4.8}
$$

By (4.5), (4.7) is clearly bounded by

$$
\rho^ {- 1 / 2} \mathrm{B} | | \mathscr {F} f | | _ {\mathrm{L} ^ {2} [ 0, 1 ]} = \rho^ {- 1 / 2} \mathrm{B} | | f | | _ {\ell^ {2} (\mathbb {Z})}.\tag{4.9}
$$

By definition of $\mathbf{B}_1$, (4.8) is bounded by

$$
\begin{array}{r l} \mathrm{B} _ {1} | | f * \mathcal {F} ^ {- 1} [ 1 - e ^ {2 \pi i \lambda u} ] | | _ {\ell^ {2} (\mathbf {Z})} & = \mathrm{B} _ {1} | | \mathcal {F} f. [ 1 - e ^ {2 \pi i \lambda u} ] | | _ {\mathrm{L} ^ {2} [ 0, 1 ]} \\ & \leqslant \mathrm{C} \rho \mathrm{B} _ {1} | | \mathcal {F} f | | _ {\mathrm{L} ^ {2} [ 0, 1 ]} \\ & = \mathrm{C} \rho \mathrm{B} _ {1} | | f | | _ {\ell^ {2} (\mathbf {Z})}. \end{array}\tag{4.10}
$$

Hence, from (4.9), (4.10),  $B_{1} \leqslant \rho^{-1/2} B + C \rho B_{1}$ , thus  $B_{1} \leqslant C' B$  by choosing  $\rho$  small enough.

By Lemma 4.4, Lemma 4.1 may be restated as

Lemma 4.11. — Let $\lambda_{1}, \ldots, \lambda_{\mathbb{K}} \in \mathbb{R}$ and let $\mathbb{R}_{j}$ stand for the $2^{-j}$-neighborhood of the set $\Lambda = \{\lambda_{1}, \ldots, \lambda_{\mathbb{K}}\}$, for $j \in \mathbb{Z}$. Then

$$
\left| \sup _ {j} \mid \mathcal {F} ^ {- 1} \left[ \chi_ {\mathrm{R} _ {j}} \mathcal {F} f \right] \right| \left| \right| _ {2} \leqslant \mathrm{C} (\log \mathrm{K}) ^ {2} \left| \right| f \left| \right| _ {2}.\tag{4.12}
$$

The proof is mainly based on Lemma 3.33 of the previous section and will be presented in several steps.

Lemma 4.13.—Let $\lambda_{1},\ldots,\lambda_{K}\in\mathbf{R}$ satisfy $|\lambda_{k}-\lambda_{k'}|>\tau>0$ for $k\neq k'$. Let $0\leqslant\varphi\leqslant1$ be a smooth function such that supp $\widehat{\varphi}\subset[-1,1]$. Then

$$
\left| \left| \sup _ {t > \tau^ {- 1}} \right| \sum_ {k = 1} ^ {\mathbf {K}} e ^ {2 \pi i \lambda_ {k} x} (f _ {k} * \varphi_ {t}) \right| \left| \right| _ {2} \leqslant \mathbf {C} (\log \mathbf {K}) ^ {2} \left(\sum_ {k = 1} ^ {\mathbf {K}} \left| \right| f _ {k} \left| \right| _ {2} ^ {2}\right) ^ {1 / 2}.\tag{4.14}
$$

Proof. — Observe first that

$$
\left| \right| \sum_ {k \leqslant \mathbf {K}} a _ {k} e ^ {2 \pi i \lambda_ {k} u} \left| \right| _ {\mathrm{L} ^ {3} [ 0, \tau^ {- 1} ]} \leqslant \mathrm{C} \tau^ {- 1 / 2} (\sum_ {k = 1} ^ {k} | a _ {k} | ^ {2}) ^ {1 / 2}\tag{4.15}
$$

for all scalar sequences $\overline{a} = (a_k)_{1 \leqslant k \leqslant \mathbf{K}}$. This is an easy consequence of the separation hypothesis of the $\lambda_k$'s and we leave the verification to the reader.

Since supp $\hat{\varphi}_t\subset [-\tau ,\tau ]$ for $t > \tau^{-1}$ , there is no restriction in assuming that

$$
\operatorname{supp} \hat {f} _ {k} \subset [ - \tau , \tau ] \quad \text { for } 1 \leqslant k \leqslant K.\tag{4.16}
$$

For $u \in \mathbf{R}$, denote by $\sigma_u$ the translation operator; thus $\sigma_u f(x) = f(x + u)$. It follows from (4.16) and Parseval's identity that

$$
\left| \left| f _ {k} - \sigma_ {u} f _ {k} \right| \right| _ {2} <   \frac {1}{2} \left| \left| f _ {k} \right| \right| _ {2} \quad \text { for } | u | <   \frac {1}{1 0 0} \tau^ {- 1}.\tag{4.17}
$$

Denoting by B the best constant fulfilling (4.14) $(\mathbf{CK}^{1/2}$ will certainly do), one gets from (4.17) for $0 \leqslant u \leqslant \frac{1}{100} \tau^{-1}$ that

$$
\left| \right| \sup _ {t > \tau^ {- 1}} \left| \sum_ {k = 1} ^ {\mathbf {K}} e ^ {2 \pi i \lambda_ {k} x} (f _ {k} * \varphi_ {t}) \right| \left| \right| _ {2} \leqslant\tag{4.18}
$$

$$
\begin{array}{r l} & {\big | \big | \sup _ {t > \tau^ {- 1}} \big | \sum_ {k = 1} ^ {\mathbf {K}} e ^ {2 \pi i \lambda_ {k} x} \sigma_ {u} (f _ {k} * \varphi_ {t}) \big | \big | \big | _ {2}} \\ & {\qquad + \frac {1}{2} B (\sum \big | | f _ {k} \big | | _ {2} ^ {2}) ^ {1 / 2}.} \end{array}
$$

Integrating (4.18) in $u$ on $\left[0, \frac{\tau^{-1}}{100}\right]$ allows to replace (4.18) by

$$
\mathrm{C} \left| \left| \tau^ {1 / 2} \right| \right| \sup _ {t > 0} \left| \sum_ {k = 1} ^ {\mathrm{K}} e ^ {- 2 \pi i \lambda_ {k} u} e ^ {2 \pi i \lambda_ {k} x} (f _ {k} * \varphi_ {t}) (x) \right| \left| \left| _ {\mathrm{L} ^ {2} ([ 0, \tau^ {- 1} ], d u)} \right| \right| _ {\mathrm{L} ^ {2} (d x)}.\tag{4.19}
$$

Therefore, it will suffice to bound (4.19) by  $\mathbf{C}(\log\mathbf{K})^{2}$ .  $(\Sigma ||f_{k}||_{2}^{2})^{1/2}$  in order to prove Lemma 4.13.

Fixing $x \in \mathbf{R}$, consider the set

$$
\mathrm{A} = \mathrm{A} _ {x} = \left\{\left(\left(f _ {1} * \varphi_ {t}\right) (x), \dots , \left(f _ {\mathbf {K}} * \varphi_ {t}\right) (x)\right) \mid t > 0 \right\}\tag{4.20}
$$

as a subset of the K-dimensional Hilbert space $\ell_{\mathbf{K}}^{2}$. For $\lambda > 0$, denote again by $\mathbf{M}_{\lambda} = \mathbf{M}_{\lambda}(x)$ the entropy numbers of A. There exists a sequence $\mathbf{B}_{s} (s \in \mathbf{Z})$ of finite subsets of the difference set $\mathbf{A}' - \mathbf{A}$ such that

(4.21)

$$
\mid \overline {{{b}}} \mid \leqslant 2. 2 ^ {s} \quad \text { for } \overline {{{b}}} \in \mathbf {B} _ {s}\tag{4.22}
$$

$$
\# \mathbf {B} _ {s} \leqslant \mathbf {M} _ {(2 ^ {s})}
$$

and each element $\bar{a} \in \mathbf{A}$ has a representation

$$
\bar {a} = \sum_ {s \in \mathbf {Z}} \bar {b} _ {s} \quad \text { with } \bar {b} _ {s} \in \mathrm{B} _ {s}\tag{4.23}
$$

(# stands for “cardinality” and  $\left|\bar{a}\right|$  refers to  $(\sum_{k=1}^{\mathbb{K}}\left|a_{k}\right|^{2})^{1/2}$ ). In writing (4.23), we make the implicit assumption that  $A = A_{x}$  is bounded, which is clearly no restriction.

Estimate

$$
\sup _ {t > 0} \left| \sum_ {k = 1} ^ {\mathbf {K}} e ^ {- 2 \pi i \lambda_ {k} u} e ^ {2 \pi i \lambda_ {k} x} (f _ {k} * \varphi_ {t}) (x) \right| \leqslant \sum_ {s \in \mathbf {Z}} \max _ {\bar {b} \in \mathbf {B} _ {s}} \left| \sum_ {k = 1} ^ {\mathbf {K}} e ^ {- 2 \pi i \lambda_ {k} u} e ^ {2 \pi i \lambda_ {k} x} b _ {k} \right|
$$

and replace the $\mathbf{L}^2 ([0,\tau^{-1}],du)$-norm by

$$
\sum_ {s \in \mathbf {Z}} | | \max _ {\bar {b} \in \mathrm{B} _ {s}} | \sum_ {k = 1} ^ {\mathbf {K}} e ^ {- 2 \pi i \lambda_ {k} u} e ^ {2 \pi i \lambda_ {k} x} b _ {k} | | | _ {\mathrm{L} ^ {3} ([ 0, \tau^ {- 1} ])}.\tag{4.24}
$$

For given $s$, consider the following bounds

$$
\max _ {\bar {b} \in \mathrm{B} _ {s}} | \dots | \leqslant \min \left\{2 ^ {s + 1} \mathrm{K} ^ {1 / 2}, \left[ \sum_ {\bar {b} \in \mathrm{B} _ {s}} \right| \sum_ {k = 1} ^ {\mathbf {K}} e ^ {- 2 \pi i \lambda_ {k} u} e ^ {2 \pi i \lambda_ {k} x} b _ {k} | ^ {2} ] ^ {1 / 2} \right\}.
$$

They imply, invoking (4.15), that (4.24) is bounded by

$$
\sum_ {s \in \mathbf {Z}} \min \left\{\tau^ {- 1 / 2} 2 ^ {s + 1} \mathrm{K} ^ {1 / 2}, \mathrm{C} \tau^ {- 1 / 2} 2 ^ {s + 1} (\# \mathrm{B} _ {s}) ^ {1 / 2} \right\} \sim \mathrm{C} \tau^ {- 1 / 2} \int_ {0} ^ {\infty} \min (\mathrm{K}, \mathrm{M} _ {\lambda} (x)) ^ {1 / 2} d \lambda\tag{4.25}
$$

using (4.21), (4.22).

Taking the  $\mathbf{L}^{2}(dx)$ -norm of (4.25), the required bound on (4.19) is obtained from (3.34). This proves (4.14).

Lemma 4.26. — Assume that $\lambda_{1},\ldots,\lambda_{K}\in\mathbf{R}$ satisfy $|\lambda_{k}-\lambda_{k'}|>2^{-s}$ for $k\neq k'$. Then, with previous notation,

$$
\left| \sup _ {j \geqslant s} \mid \mathcal {F} ^ {- 1} \left[ \chi_ {\mathrm{R} _ {j}} \mathcal {F} f \right] \right| \mid | _ {2} \leqslant \mathrm{C} (\log \mathrm{K}) ^ {2} \mid | f | | _ {2}.\tag{4.27}
$$

Proof. — The inequality (4.27) is derived from (4.14) by a standard square function argument. Take $\varphi$ as in Lemma 4.13 satisfying $\hat{\varphi} = 1$ on $\left[-\frac{1}{2}, \frac{1}{2}\right]$. Estimate

(4.28)

$$
\begin{array}{r l} \sup _ {j \geqslant s} | \mathcal {F} ^ {- 1} [ \chi_ {\mathrm{R} _ {j}} \mathcal {F} f ] | & \leqslant \\ & \sup _ {j \geqslant s} | \sum_ {k = 1} ^ {\mathrm{K}} e ^ {2 \pi i \lambda_ {k} x} [ (f. e ^ {- 2 \pi i \lambda_ {k} x}) * \varphi_ {2 ^ {j}} ] | \\ & + \{\sum_ {j \geqslant s} | \mathcal {F} ^ {- 1} [ (\chi_ {\mathrm{R} _ {j}} - \sum_ {k = 1} ^ {\mathrm{K}} \hat {\varphi} _ {2 ^ {j}} (\lambda - \lambda_ {k})) \mathcal {F} f ] | ^ {2} \} ^ {1 / 2}. \end{array}\tag{4.29}
$$

By the hypothesis on $\varphi, g * \varphi_{2^j} = (g * \varphi_{2^{s-1}}) * \varphi_{2^j}$ for $j \geqslant s$. Hence, applying (4.13) with $f_k = (f.e^{-2\pi i\lambda_k x}) * \varphi_{2^{s-1}}$, (4.14) gives the following bound on (4.28)

$$
\mathrm{C} (\log \mathrm{K}) ^ {2} \left\{\int [ \sum_ {k = 1} ^ {\mathrm{K}} | \hat {f} (\lambda + \lambda_ {k}) | ^ {2} | \hat {\varphi} (2 ^ {s - 1} \lambda) | ^ {2} ] d \lambda \right\} ^ {1 / 2} \leqslant \mathrm{C} (\log \mathrm{K}) ^ {2} \| f \| _ {2}\tag{4.30}
$$

invoking the separation hypothesis of the $\lambda_{k}$'s and the fact that $\operatorname{supp} \hat{\varphi} \subset [-1, 1]$.

By Parseval's identity, (4.29) is bounded by

$$
\begin{array}{r l} & {\left\{\sum_ {j \geqslant s} \int | \hat {f} (\lambda) | ^ {2} \left[ \chi_ {\mathrm{R} _ {j}} (\lambda) - \sum_ {k = 1} ^ {\mathrm{K}} \hat {\varphi} (2 ^ {j} (\lambda - \lambda_ {k})) \right] ^ {2} d \lambda \right\} ^ {1 / 2} \leqslant} \\ & {\qquad \sup _ {\lambda \in \mathbf {R}} [ \sum_ {j \geqslant s} | \chi_ {\mathrm{R} _ {j}} (\lambda) - \sum_ {k = 1} ^ {\mathrm{K}} \hat {\varphi} (2 ^ {j} (\lambda - \lambda_ {k})) | ]. | | f | | _ {2}.} \end{array}\tag{4.31}
$$

Since $\chi_{\mathbf{R}_j}(\lambda) - \sum_{k=1}^{\mathbf{K}} \hat{\varphi}(2^j (\lambda - \lambda_k))$ is bounded, and vanishes if either $\mathrm{dist}(\lambda, \Lambda) < 2^{-j-1}$ or $\mathrm{dist}(\lambda, \Lambda) > 2^{-j}$, the first factor in (4.31) is clearly bounded.

Now, (4.27) is implied by (4.30), (4.31).

Remark. — In a later application, $\Lambda = \{\lambda_1, \ldots, \lambda_K\}$ will be typically a set of rational numbers $a/q$, $(a, q) = 1$, with $q \leqslant Q$ and the neighborhoods (major-arcs) considered $\ll Q^{-2}$. Thus the more restrictive Lemma 4.26 actually already suffices for our purpose. The statement of Lemma 4.11 is simpler, however, and the result may be of independent interest.

In the remainder of this section, we complete the proof of (4.12).

Lemma 4.32. — Let again

Then

$$
\mathbf {R} _ {j} = \{\lambda \in \mathbf {R} | \min _ {1 \leqslant k \leqslant \mathbb {K}} | \lambda - \lambda_ {k} | \leqslant 2 ^ {- j} \} f o r j \in \mathbf {Z}.\tag{4.33}
$$

$$
\left| \left| \sup _ {j \in \mathbb {S}} \right| \mathcal {F} ^ {- 1} \left[ \chi_ {\mathrm{R} _ {j}} \mathcal {F} f \right] \right| | | _ {2} \leqslant (\log | S |) | | f | | _ {2}
$$

for S a finite subset of Z.

Proof. — The argument is inspired by the Burkholder-Davis-Gundy-Stein (cf. [Ga]) dual version of Doob's maximal inequality. The only difference here is that the operators are not positive. We only use the fact that the  $R_{j}$ 's are decreasing. Assume thus, redefining  $R_{j}$ , that

$$
\mathrm{R} _ {j + 1} \subset \mathrm{R} _ {j}, \quad 1 \leqslant j \leqslant 2 ^ {s} \text {   where   } s \sim \log | \mathrm{S} |.
$$

Denote by B the best constant satisfying the inequality

$$
\left| \left| \sup _ {1 \leqslant j \leqslant 2 ^ {s}} \right| \mathcal {F} ^ {- 1} \left[ \chi_ {\mathrm{R} _ {j}} \mathcal {F} f \right] \right| | | _ {2} \leqslant \mathrm{B} | | f | | _ {2}
$$

or equivalently (by dualization)

$$
\left| \left| \sum_ {j \leqslant 2 ^ {s}} \mathcal {F} ^ {- 1} \left[ \chi_ {\mathrm{R} _ {j}} \mathcal {F} g _ {j} \right] \right| \right| _ {2} \leqslant \mathrm{B} \left| \left| \sum_ {j \leqslant 2 ^ {s}} \mid g _ {j} \mid \right| \right| _ {2}.\tag{4.34}
$$

Identify S and $\{1, 2, \ldots, 2^s\}$ and let $(S_c)_{|c| \leqslant s}$ be a diadic partitioning of S

![](images/page_17_image_16.jpg)

Set $\widetilde{g}_j = \mathcal{F}^{-1}[\chi_{\mathrm{R}_j}\mathcal{F}g_j]$; clearly

$$
\langle \widetilde {g} _ {j}, \widetilde {g} _ {k} \rangle = \langle g _ {j}, \widetilde {g} _ {k} \rangle \quad \text { for } j \leqslant k.\tag{4.35}
$$

Using this fact and Hölder's inequality, one gets, from the definition of B,

$$
\begin{array}{r l} | | \sum_ {j \in \mathbb {S}} \widetilde {g} _ {j} | | _ {2} ^ {2} & = \sum | | \widetilde {g} _ {j} | | _ {2} ^ {2} + 2 \sum_ {j <   k} \langle \widetilde {g} _ {j}, \widetilde {g} _ {k} \rangle \\ & \leqslant \sum | | g _ {j} | | _ {2} ^ {2} + 2 \sum_ {| c | <   s} | \langle \sum_ {j \in \mathbb {S} _ {c, 0}} g _ {j}, \sum_ {k \in \mathbb {S} _ {c, 1}} \widetilde {g} _ {k} \rangle | \\ & \leqslant \sum | | g _ {j} | | _ {2} ^ {2} + 2 B \sum_ {| c | <   s} | | \sum_ {j \in \mathbb {S} _ {c, 0}} | g _ {j} | | _ {2} | | \sum_ {J \in \mathbb {S} _ {c, 1}} | g _ {j} | | _ {2} \\ & \leqslant (1 + 2 B s) | | \sum | g _ {j} | | _ {2} ^ {2}. \end{array}
$$

Consequently, $\mathbf{B}^2 \leqslant 1 + 2\mathrm{Bs}$ implies $\mathbf{B} \leqslant cs$, proving (4.33).

Proof of (4.12). — Define

$$
\mathrm{S} = \{j \in \mathbf {Z} | \mathrm{K} ^ {- 1} 2 ^ {- j} <   | \lambda_ {k} - \lambda_ {k ^ {\prime}} | <   \mathrm{K} 2 ^ {- j} \quad \text { for   some } 1 \leqslant k \neq k ^ {\prime} \leqslant \mathrm{K} \}.
$$

Obviously

$$
| \mathrm{S} | \leqslant \mathrm{K} ^ {3}.\tag{4.36}
$$

Define further

$$
\mathbf {Z} _ {r} = \{j \in \mathbf {Z} \backslash \mathrm{S} \mid \mathrm{R} _ {j} \text {   has   } r \text {   components   } \}
$$

for $1 \leqslant r \leqslant K$. Hence

$$
\mathrm{Z} _ {1} \prec \mathrm{Z} _ {2} \prec \dots \prec \mathrm{Z} _ {\mathrm{K}}\tag{4.37}
$$

where  $Z_{1}$ ,  $Z_{K}$  are half-lines and  $Z_{r}$  is a finite segment for 1 < r < K. For r > 1, let  $j_{r} = \min Z_{r}$ . By construction, there is a set  $\Lambda_{r} \subset \{\lambda_{k}\}$  satisfying

(4.38)

$$
\mid \lambda - \lambda^ {\prime} \mid > 2 ^ {- j _ {r}} \quad \text { for } \lambda \neq \lambda^ {\prime} \text { in } \Lambda_ {r}\tag{4.39}
$$

$$
\bigcup_ {\lambda \in \Lambda_ {r}} [ \lambda - 2 ^ {- j}, \lambda + 2 ^ {- j} ] \subset R _ {j} \subset \bigcup_ {\lambda \in \Lambda_ {r}} [ \lambda - 2 ^ {- j + 1}, \lambda + 2 ^ {- j + 1} ] \quad \text { for } j \in Z _ {r}.
$$

To prove (4.12) we proceed again by duality and estimate the best B fulfilling

$$
\left| \left| \sum_ {j} \widetilde {g} _ {j} \right| \right| _ {2} \leqslant B \left| \left| \sum \mid g _ {j} \right| \right| | _ {2} \quad \text { for } \widetilde {g} _ {j} = \mathcal {F} ^ {- 1} [ \chi_ {\mathrm{R} _ {j}} \mathcal {F} g _ {j} ].
$$

Using (4.32) and (4.36) and setting $\mathbf{G}_r = \sum_{j\in \mathbb{Z}_r}g_j$ and $\widetilde{\mathbf{G}}_r = \sum_{j\in \mathbb{Z}_r}\widetilde{g}_j$ we have

$$
\left| \left| \sum_ {j} \widetilde {g} _ {j} \right| \right| _ {2} \leqslant \left| \left| \sum_ {j \in S} \widetilde {g} _ {j} \right| \right| _ {2} + \left| \left| \sum_ {r} \left(\sum_ {j \in Z _ {r}} \widetilde {g} _ {j}\right) \right| \right| _ {2} \leqslant (\log K) \left| \left| \Sigma | g _ {j} | \right| \right| _ {2} + \left| \left| \sum_ {r} \widetilde {G} _ {r} \right| \right| _ {2}.
$$

Since $Z_r \prec Z_{r'}$ for $r < r'$, we have, for $j \in Z_r, j' \in Z_{r'}$,

$$
\langle \widetilde {g} _ {j}, \widetilde {g} _ {j ^ {\prime}} \rangle = \langle g _ {j}, \widetilde {g} _ {j ^ {\prime}} \rangle .
$$

Hence

$$
\langle \widetilde {\mathrm{G}} _ {r}, \widetilde {\mathrm{G}} _ {r ^ {\prime}} \rangle = \langle \mathrm{G} _ {r}, \widetilde {\mathrm{G}} _ {r ^ {\prime}} \rangle
$$

and

$$
\left| \left| \Sigma \widetilde {G} _ {r} \right| \right| _ {2} ^ {2} = \Sigma \left| \left| \widetilde {G} _ {r} \right| \right| _ {2} ^ {2} + 2 \sum_ {r <   r ^ {\prime}} \langle G _ {r}, \widetilde {G} _ {r ^ {\prime}} \rangle .
$$

The same argument as in (4.32) than shows that

$$
\mathbf {B} ^ {2} \leqslant (\log \mathbf {K}) ^ {2} + \mathbf {B} _ {1} ^ {2} + \mathbf {B} (\log \mathbf {K})\tag{4.40}
$$

where $\mathbf{B}_1$ has to satisfy

$$
\left| \sup _ {j \in \mathbf {Z} _ {r}} \right| \mathcal {F} ^ {- 1} [ \chi_ {\mathrm{R} _ {j}} \mathcal {F} f ] | | _ {2} \leqslant \mathrm{B} _ {1} | | f | | _ {2}.\tag{4.41}
$$

In order to estimate  $B_{1}$ , apply (4.26) with  $\Lambda = \Lambda_{r}$ ,  $s = j_{r}$ , taking into account (4.38) and  $j \geqslant j_{r}$  for  $j \in Z_{r}$ . Invoking then (4.39) and a square function argument such as in (4.31), it follows that  $B_{1} < C(\log K)^{2}$ . Substitution in (4.40) yields that  $B < C(\log K)^{2}$ . This proves (4.12), hence Lemma's 4.11 and 4.1.

## 5. Behaviour of Exponential Sums

In analyzing the Fourier multipliers appearing in proving Theorems 1 and 2, information is needed on the exponential sums (1.5), i.e.,

$$
\varphi_ {N} (\overline {{\alpha}}) = \frac {1}{N} \sum_ {n = 1} ^ {N} e ^ {2 \pi i p (n, \overline {{\alpha}})}\tag{5.1}
$$

where

$$
p (x, \bar {\alpha}) = \alpha_ {1} x + \dots + \alpha_ {d} x ^ {d} \quad \text { and } \quad \bar {\alpha} = (\alpha_ {1}, \dots , \alpha_ {d}) \in [ 0, 1 ] ^ {d}.\tag{5.2}
$$

In this section, some well-known results and procedures are summarized. The estimates required are mainly provided by H. Weyl's basic lemma

Lemma 5.3. — Let $f(x) = \alpha_{1}x + \alpha_{2}x^{2} + \ldots + \alpha_{d}x^{d}$ and $|\alpha_{d} - (a / q)| < 1 / q^{2}$, where $(a, q) = 1$. Then for all $\varepsilon > 0$,

$$
\left| \sum_ {m = 1} ^ {n} e ^ {2 \pi i f (m)} \right| \leqslant \mathrm{C} _ {\varepsilon} n ^ {1 + \varepsilon} [ q ^ {- 1} + n ^ {- 1} + q n ^ {- d} ] ^ {\rho}, \quad w h e r e \rho = \frac {1}{2 ^ {d - 1}}\tag{5.4}
$$

(cf. [Vaug] or [Vin] for a proof).

Denote by Q the set of rational numbers. For

$$
\delta = \delta (d) > 0 \quad \text { and } \quad \theta_ {1}, \dots , \theta_ {d} \in [ 0, 1 ] \cap \mathbf {Q}
$$

with common denominator  $q < N^{\delta}$ , define the “major box” in the d-dimensional torus as

$$
\mathcal {M} \left(\theta_ {1}, \dots , \theta_ {d}\right) = \{\bar {\alpha} = \left(\alpha_ {1}, \dots , \alpha_ {d}\right) \in \Pi^ {d} | | \alpha_ {j} - \theta_ {j} | <   N ^ {- j + \delta} (1 \leqslant j \leqslant d) \}.\tag{5.5}
$$

The following fact may be found in [Vin] (ch. IV, Th. 3) and can be proved by iterated applications of Lemma 5.3 combined with Dirichlet's principle.

Lemma 5.6. — If  $\bar{\alpha}$  does not belong to some major box as defined above, then

$$
\mid \varphi_ {\mathbf {N}} (\overline {{\alpha}}) \mid <   \mathbf {C N} ^ {- \delta^ {\prime}}.\tag{5.7}
$$

Here $\varphi_{\mathbf{N}}(\overline{\alpha})$ is defined by (5.1) and $\mathbf{C}, \delta' > 0$ depend on $d$.

One may describe the shape of $\varphi_{\mathbf{N}}(\overline{\alpha})$ on $\mathcal{M}(\theta_1, \ldots, \theta_d)$. Let $\theta_j = a_j / q$, $\alpha_j = \theta_j + \beta_j$ and $|\beta_j| < \mathbb{N}^{-j + \delta}$. Writing $n = qs + r$, where $0 \leqslant s < \mathbb{N} / q$ and $r = 0, 1, \ldots, q - 1$, one has, for $j = 1, \ldots, d$,

$$
\alpha_ {j} n ^ {j} = \left(\theta_ {j} + \beta_ {j}\right) (q s + r) ^ {j} \in \mathbf {Z} + \theta_ {j} r ^ {j} + \beta_ {j} q ^ {j} s ^ {j} + o \left(\mathrm{N} ^ {- 1 + 2 \delta}\right)\tag{5.8}
$$

since $q < \mathbf{N}^{\delta}$. Hence, clearly

$$
\varphi_ {\mathbf {N}} (\overline {{\alpha}}) = \left\{\frac {1}{q} \sum_ {r = 0} ^ {q - 1} e ^ {2 \pi i (r \theta_ {1} + \dots + r ^ {d} \theta_ {d})} \right\} \left\{\frac {q}{\mathbf {N}} \sum_ {s = 0} ^ {\mathbf {N} / q} e ^ {2 \pi i (\beta_ {1} q s + \dots + \beta_ {d} q ^ {d} s ^ {d})} \right\} + o (\mathbf {N} ^ {- 1 / 2}).\tag{5.9}
$$

For $(a_{1},\ldots ,a_{d},q) = 1$ and $\theta_{j} = a_{j} / q$ , define

$$
\mathrm{S} (q, a _ {1}, \dots , a _ {d}) = \frac {1}{q} \sum_ {r = 0} ^ {q - 1} e ^ {2 \pi i (r \theta_ {1} + \dots + r ^ {d} \theta_ {d})}.\tag{5.10}
$$

Set

$$
\mathrm{V} _ {\mathbf {N}} (\overline {{\beta}}) = \frac {1}{\mathrm{N}} \int_ {0} ^ {\mathbf {N}} e ^ {2 \pi i (\beta_ {1} \mathbf {y} + \beta_ {2} \mathbf {y} ^ {2} + \dots + \beta_ {d} \mathbf {y} ^ {d})} d y.\tag{5.11}
$$

Then, (5.9) and the estimates  $\left|\beta_{j}\right|<N^{-j+\delta}$  easily yield the following lemma, replacing the second factor in (5.9) by its continuous substitute:

Lemma 5.12. — For $\overline{\alpha} \in \mathcal{M}(\overline{\theta})$, $\overline{\alpha} = \overline{\theta} + \overline{\beta}$, one has

$$
\varphi_ {\mathbf {N}} (\overline {{{\alpha}}}) = \mathrm{S} (q, a _ {1}, \dots , a _ {d}) \mathrm{V} _ {\mathbf {N}} (\overline {{{\beta}}}) + \mathrm{O} (\mathrm{N} ^ {- 1 / 2}),\tag{5.13}
$$

where $\theta_{j} = a_{j} / q$.

Recall also

Lemma 5.14. — If $(q, a_{1}, \ldots, a_{d}) = 1$, then

$$
\left| \mathrm{S} (q, a _ {1}, \dots , a _ {d}) \right| \leqslant c q ^ {- \delta^ {\prime}}\tag{5.15}
$$

where $\delta' = \delta(d) > 0$.

This is clearly a consequence of (5.3).

In this work, we will not need finer information on the  $\mathrm{S}(q,a_{1},\ldots,a_{d})$ , such as the multiplicativity properties and A. Weil's estimate for q a prime number.

Finally, we give some estimates on the function

$$
\mathrm{V} _ {\mathbf {N}} (\overline {{\beta}}) = \int_ {0} ^ {1} e ^ {2 \pi i (\beta_ {1} \mathbf {N} y + \beta_ {2} \mathbf {N} ^ {2} y ^ {2} + \dots + \beta_ {d} \mathbf {N} ^ {d} y ^ {d})} d y.\tag{5.16}
$$

Lemma 5.17.

(5.18)

$$
\mid 1 - \mathrm{V} _ {\mathbf {N}} (\overline {{\beta}}) \mid <   \mathbf {C} \sum_ {j = 1} ^ {d} \mid \beta_ {j} \mid \mathrm{N} ^ {j}\tag{5.19}
$$

$$
\mid \mathrm{V} _ {\mathbf {N}} (\overline {{\beta}}) \mid <   \mathbf {C} [ 1 + \sum_ {j = 1} ^ {d} \mid \beta_ {j} \mid \mathrm{N} ^ {j} ] ^ {- 1 / d}
$$

where $\mathbf{C} = c(d)$.

The first estimate (5.18) is obvious and the second (5.19) follows from van der Corput's estimate on oscillatory integrals.

## 6. Ergodic Theorems in $\mathbf{L}^2$

In this section, we prove Theorem 1 for functions of class  $L^{2}$ . This result appears in  $[B_{1}]$ . The argument presented here uses less structure. According to the discussion in section 1, the maximal inequality and convergence problem for the averages

(6.1)

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{\mathbf {N}} \sum_ {n = 1} ^ {\mathbf {N}} \mathrm{T} ^ {p (n)} f\tag{6.2}
$$

$$
p (x) = b _ {1} x + b _ {2} x ^ {2} + \dots + b _ {d} x ^ {d}, \quad b _ {j} \in \mathbf {Z} \text {   and   } b _ {d} > 0,
$$

where reduced to proving certain inequalities for the shift model  $(\mathbf{Z}, \mathbf{S})$ . In the case of the shift, one has

$$
\mathrm{A} _ {\mathbf {N}} \mathcal {F} = f * \mathrm{K} _ {\mathbf {N}}, \quad \text { where } \quad \mathrm{K} _ {\mathbf {N}} = \frac {1}{\mathrm{N}} \sum_ {n = 1} ^ {\mathrm{N}} \delta_ {\{\boldsymbol {p} (n) \}}\tag{6.3}
$$

and $\delta_x$ stands for the Dirac measure at $x \in \mathbf{Z}$. Hence, introducing the Fourier transform,

$$
\mathrm{A} _ {\mathbf {N}} f = \mathcal {F} ^ {- 1} [ \mathcal {F} [ \mathrm{K} _ {\mathbf {N}} ]. \mathcal {F} [ f ] ],\tag{6.4}
$$

where, for $\alpha \in \Pi \simeq [0,1]$,

$$
\mathcal {F} [ \mathrm{K} _ {\mathrm{N}} ] (\alpha) = \frac {1}{\mathrm{N}} \sum_ {n = 1} ^ {\mathrm{N}} e ^ {- 2 \pi i p (n). \alpha} = \varphi_ {\mathrm{N}} (- b _ {1} \alpha , \dots , - b _ {d} \alpha) \equiv \varphi_ {\mathrm{N}} (- \alpha . \bar {b}).\tag{6.5}
$$

For $s \geqslant 0$, define an exhaustion of the rationals in $\mathbf{T}$

$$
\mathcal {R} _ {s} = \{\theta \in Q \cap [ 0, 1 ] | \theta = a / q, (a, q) = 1 \text {   and   } 2 ^ {s} \leqslant q <   2 ^ {s + 1} \}\tag{6.6}
$$

which is considered as subset of $\Pi$. Thus $\mathcal{R}_0 = \{0 \equiv 1\}$.

Denote by $\zeta$ a smooth function on $\mathbf{R}$ with $\zeta = 1$ on $\left[-\frac{1}{10},\frac{1}{10}\right]$ and $\zeta = 0$ outside $\left[-\frac{1}{5},\frac{1}{5}\right]$. (The smoothness of $\zeta$ will be irrelevant for the $\mathbf{L}^2$-theory but has importance when considering $\mathbf{L}^r$-estimates for $r < 2$ in the next section.)

Define

$$
\psi_ {s, \mathbf {N}} (\alpha) = \sum_ {\theta \in \mathcal {R} _ {s}} \mathrm{S} (\theta) w _ {\mathbf {N}} (\alpha - \theta) \zeta (1 0 ^ {s} (\alpha - \theta))\tag{6.7}
$$

where, with the notation (5.10), (5.11) of section 5,

(6.8)

$$
\begin{array}{r l} \mathrm{S} (\theta) & = \mathrm{S} (q ^ {\prime}, a _ {1} ^ {\prime}, \dots , a _ {d} ^ {\prime}) \\ & \text { where } - \theta . b _ {j} \equiv a _ {j} ^ {\prime} / q ^ {\prime} (\bmod 1) \text { and } (a _ {1} ^ {\prime}, \dots , a _ {d} ^ {\prime}, q ^ {\prime}) = 1, \end{array}\tag{6.9}
$$

$$
w _ {\mathbf {N}} (\beta) = \mathrm{V} _ {\mathbf {N}} (- \beta b _ {1}, \dots , - \beta b _ {d}).
$$

Thus it follows from Lemma 5.12 that, if $\theta = a / q$, $q < \mathbf{N}^{\delta}$,

$$
\mathcal {F} \left[ \mathrm{K} _ {\mathrm{N}} \right] (\alpha) = \mathrm{S} (\theta) w _ {\mathrm{N}} (\alpha - \theta) + \mathrm{O} \left(\mathrm{N} ^ {- 1 / 2}\right) \quad \text { if } | \alpha - \theta | <   \mathrm{N} ^ {- d + \delta}.\tag{6.10}
$$

Also, since $q' > q / b_d$, if $\theta = a / q$, $(a, q) = 1$, one has by (5.15) with notation (6.8)

(6.11) $|\mathbf{S}(\theta)| < \mathbf{C}2^{-s\delta'}$ for $\theta \in \mathcal{R}_s$.

From (6.9) and (5.17)

(6.12)

$$
\mid 1 - w _ {\mathbf {N}} (\beta) \mid <   \mathbf {C} \mid \beta \mid . \mathbf {N} ^ {d},\tag{6.13}
$$

$$
\mid w _ {\mathbf {N}} (\beta) \mid <   \mathrm{C} [ 1 + \mid \beta \mid \mathrm{N} ^ {d} ] ^ {- 1 / d}.
$$

Observe also that the summands in (6.7) are disjointly supported, by definition of $\mathcal{R}_s$ and $\zeta$.

Lemma 6.14. — There exists $\delta_{1}>0$ such that the uniform estimate

$$
\left| \mathcal {F} [ \mathrm{K} _ {\mathrm{N}} ] (\alpha) - \sum_ {s \geqslant 0} \psi_ {s, \mathrm{N}} (\alpha) \right| <   \mathrm{CN} ^ {- \delta_ {1}}\tag{6.15}
$$

holds.

This lemma allows the replacement of  $F[K_{N}]$  in (6.4) by more explicit multipliers which will be taken care of by Lemma 4.1.

Proof of (6.14). — Redefine major arcs in $\Pi$ by letting

$$
\mathcal {M} (\theta) = \{\alpha \in \Pi | | \alpha - \theta | <   N ^ {- d + \delta} \}\tag{6.16}
$$

for $\theta$ a rational $a / q$, $1 \leqslant a \leqslant q$, $(a, q) = 1$ with $q < \mathbf{N}^{\delta}$.

Case 1. — $\alpha$ belongs to an arc $\mathcal{M}(\theta_0)$.

Assume $\theta_0 \in \mathcal{R}_{s_0}$, thus $2^{s_0} < N^\delta$. Let $s_1$ be a positive integer (depending on $N$), to be specified later. Estimate, using (6.10), (6.11),

$$
\begin{array}{r l} | \mathcal {F} [ \mathrm{K} _ {\mathrm{N}} ] (\alpha) - \sum \psi_ {s, \mathrm{N}} (\alpha) | & \leqslant | 1 - \zeta (1 0 ^ {s _ {0}} (\alpha - \theta_ {0})) | \\ & + \sum_ {s \leqslant s _ {1}} \sup | w _ {\mathrm{N}} (\alpha - \theta) | + \mathrm{C} 2 ^ {- s _ {1} \delta^ {\prime}} + \mathrm{CN} ^ {- 1 / 2}, \end{array}\tag{6.17}
$$

where the sup is extended over all $\theta \in \mathcal{R}_s$ different from $\theta_0$.

Since $10^{s_0} < \mathbf{N}^{4\delta}$ and $|\alpha - \theta_0| < \mathbf{N}^{-d + \delta} < \mathbf{N}^{-1}$, the first term in (6.17) vanishes. Letting $2^{s_1} \sim \mathbf{N}^{\delta}$ and writing

$$
\mid \alpha - \theta \mid \geqslant \mid \theta - \theta_ {0} \mid - \mid \alpha - \theta_ {0} \mid , \quad \mid \theta - \theta_ {0} \mid > \frac {1}{2} q ^ {- 1} 2 ^ {- s _ {1}} \geqslant \frac {1}{4} N ^ {- 2 \delta}
$$

for $\theta \in \mathcal{R}_s$,

$s \leqslant s_{1}, \theta \neq \theta_{0}$ and $|\alpha - \theta_{0}| < N^{-1}$, it follows that $|\alpha - \theta| > \frac{1}{2} |\theta - \theta_{0}|$. Thus the second term of (6.17) is bounded by $(\log N).N^{-1 + (2\delta / d)}$, invoking (6.13). Hence (6.15) holds.

Case 2. — $\alpha$ does not belong to a major arc.

Clearly, from the definition (5.5) and (5.7), we have $|\mathcal{F}[\mathrm{K}_{\mathbf{N}}](\alpha)| < \mathrm{CN}^{-\delta'}$, by (6.5). For $2^{s_1} < \frac{1}{2}\mathrm{N}^\delta$, $2^{s_1} \sim \mathrm{N}^\delta$, write

$$
\left| \sum \psi_ {s, \mathrm{N}} (\alpha) \right| \leqslant \sum_ {s \leqslant s _ {1}} \sup _ {\theta \in \mathcal {R} _ {s}} \left| w _ {\mathrm{N}} (\alpha - \theta) \right| + \mathrm{C} 2 ^ {- s _ {1} \delta^ {\prime}}.\tag{6.18}
$$

By definition of $\mathcal{M}(\theta)$, it follows from the hypothesis on $\alpha$ that $|\alpha - \theta| > \mathrm{N}^{-d + \delta}$ whenever $\theta \in \mathcal{R}_s$, $s \leqslant s_1$. Hence $|w_{\mathrm{N}}(\alpha - \theta)| < \mathrm{CN}^{-\delta / d}$ by (6.13) and (6.18) implies again (6.15). This proves Lemma (6.14).

It is clear that, when proving the maximal inequality

$$
\left| \sup _ {\mathbf {N}} | f * \mathrm{K} _ {\mathbf {N}} | \right| _ {\ell^ {2} (\mathbf {Z})} \leqslant \mathrm{C} \| f \| _ {\ell^ {2} (\mathbf {Z})},\tag{6.19}
$$

the function $f$ may be taken positive and hence the supremum taken over the set $Z_{1} = \{2^{k} \mid k = 1, 2, \ldots\}$. Setting

$$
\psi_ {\mathbf {N}} = \sum_ {\mathbf {s}} \psi_ {\mathbf {s}, \mathbf {N}},\tag{6.20}
$$

estimate by (6.15) and Parseval

$$
\begin{array}{r l} & {\left| \left| \sup _ {N \in Z _ {1}} | f * K _ {N} | \right| \right| _ {2} \leqslant \left| \left| \sup _ {n \in Z _ {1}} | \mathcal {F} ^ {- 1} [ \psi_ {N} \mathcal {F} f ] \right| \right| _ {2}} \\ & {\qquad + (\sum_ {n \in Z _ {1}} | | \mathcal {F} [ K _ {N} ] - \psi_ {N} \| _ {\infty} ^ {2}) ^ {1 / 2} \| f \| _ {2}} \\ & {\leqslant \sum_ {s = 0} ^ {\infty} \left| \left| \sup _ {Z _ {1}} | \mathcal {F} ^ {- 1} [ \psi_ {s, N} \mathcal {F} f ] \right| \right| _ {2} + C \| f \| _ {2}.} \end{array}\tag{6.21}
$$

To estimate the contribution of the first terms, define

$$
\widetilde {\psi} _ {s, \mathbf {N}} (\alpha) = \sum_ {\theta \in \mathcal {R} _ {s}} \mathrm{S} (\theta) \chi (\mathrm{N} ^ {d} (\alpha - \theta)) \zeta (1 0 ^ {s} (\alpha - \theta))\tag{6.22}
$$

with $\chi = \chi_{[-1,1]}$, considered as function on $\mathbf{R}$. It easily follows from (6.11), (6.12), (6.13) that there is a uniform estimate

$$
\sum_ {\mathbf {N} \in \mathbf {Z _ {1}}} | \psi_ {s, \mathbf {N}} - \widetilde {\psi} _ {s, \mathbf {N}} | \leqslant \mathrm{C2} ^ {- s \delta^ {\prime}}.\tag{6.23}
$$

Therefore, again by a square function argument

$$
\left| \left| \sup _ {z _ {1}} \right| \mathcal {F} ^ {- 1} \left[ \psi_ {s, N} \mathcal {F} f \right] \right| \| _ {2} \leqslant \left| \left| \sup _ {z _ {1}} \right| \mathcal {F} ^ {- 1} \left[ \tilde {\psi} _ {s, N} \mathcal {F} f \right] \right| \| _ {2} + C 2 ^ {- s \delta^ {\prime}} \| f \| _ {2}.\tag{6.24}
$$

For $\mathbf{N} \in \mathbf{Z}_1$, write $\mathbf{N}^d = 2^j$ and let $\mathbf{R}_j$ be the $2^{-j}$-neighborhood of $\mathbf{R}_s \subset \Pi$. Thus, setting

(6.25)

$$
\mathcal {F} [ g _ {s} ] = \mathcal {F} [ f ] \sum_ {\theta \in \mathcal {R} _ {s}} S (\theta) \zeta (1 0 ^ {s} (\alpha - \theta))\tag{6.26}
$$

$$
\widetilde {\Psi} _ {s, \mathrm{N}} \mathcal {F} f = \mathcal {F} [ g _ {s} ] \cdot \chi_ {\mathrm{R} _ {j}},
$$

it follows from inequality (4.3) in Lemma 4.1 that

$$
\begin{array}{r l} \left| \left| \sup _ {\mathbf {N} \in \mathbf {Z} _ {1}} \right| \mathcal {F} ^ {- 1} [ \widetilde {\psi} _ {s, \mathbf {N}}. \mathcal {F} f ] \right| & \| _ {2} \leqslant \left| \left| \sup _ {j \in \mathbf {Z} _ {+}} \right| \mathcal {F} ^ {- 1} [ \mathcal {F} [ g _ {s} ] \chi_ {\mathrm{R} _ {j}} ] \right| \| _ {2} \\ & \leqslant \mathrm{C} (\log | \mathcal {R} _ {s} |) ^ {2} \| g _ {s} \| _ {2}. \end{array}\tag{6.27}
$$

By definition, $|\mathcal{R}_s| < 4^s$, and it follows from (6.11) and Parseval that

$$
\left| \left| g _ {s} \right| \right| _ {2} \leqslant \mathrm{C} 2 ^ {- s \delta^ {\prime}} \left| \left| f \right| \right| _ {2}.
$$

Substitution in (6.24) yields the bound

$$
\left| \left| \sup _ {z _ {1}} \right| \mathcal {F} ^ {- 1} [ \psi_ {s, N} \mathcal {F} f ] \right| \left| \right| _ {2} \leqslant C. s ^ {2} 2 ^ {- s \delta^ {\prime}} \left| \right| f \left| \right| _ {2}\tag{6.28}
$$

and hence, substituting in (6.21),

$$
\left| \left| \sup _ {N \in Z _ {1}} | f * K _ {N} | \right| \right| _ {2} \leqslant C \left(\sum_ {s = 0} ^ {\infty} s ^ {2} 2 ^ {- s \delta^ {\prime}}\right) \| f \| _ {2} \leqslant C \| f \| _ {2}\tag{6.29}
$$

which proves the maximal inequality

$$
\left| \sup _ {\mathbf {N}} \mid \mathrm{A} _ {\mathbf {N}} f \right| \left| \right| _ {2} \leqslant \mathrm{C} \left| \right| f \left| \right| _ {2}.\tag{6.30}
$$

Next, we verify the almost sure convergence using the method described in section 2 of this paper. Thus we prove an inequality (2.14) in (Z, S)

$$
\sum_ {j = 1} ^ {J} \left| \left| \mathcal {M} _ {j} f \right| \right| _ {2} \leqslant o (J) \left| \left| f \right| \right| _ {2}\tag{6.31}
$$

setting

$$
\mathcal{M}_{j}f = \sup_{\substack{\mathrm{N}_{j} <   \mathrm{N} <   \mathrm{N}_{j + 1}\\ \mathrm{N}\in \mathrm{Z}_{\varepsilon}}}|f*(\mathrm{K}_{\mathrm{N}} - \mathrm{K}_{\mathrm{N}_{j}})|\tag{6.32}
$$

where  $Z_{\varepsilon}=\{[(1+\varepsilon)^{n}]; n=1,2,\ldots\}$  for  $\varepsilon>0$  fixed, and  $N_{j}$  is any rapidly increasing sequence  $(N_{j+1}>2N_{j})$ .

We again apply the Fourier transform method. With previous definitions, it again follows from (6.15) that $f * (\mathrm{K}_{\mathbf{N}} - \mathrm{K}_{\mathbf{N}_j})$ may be replaced by $\mathcal{F}^{-1}[(\psi_{\mathbf{N}} - \psi_{\mathbf{N}_j})\mathcal{F}f]$ when defining $\mathcal{M}_j f$. Fixing $s_0$, it follows from the previous inequality (6.28) that then

$$
\left|\left|\mathcal{M}_{j}f\right| \right|_{2}\leqslant \sum_{s\leqslant s_{0}}\left|\left|\sup_{\substack{\mathrm{N}_{j} <   \mathrm{N} <   \mathrm{N}_{j + 1}\\ \mathrm{N}\in \mathrm{Z}_{\varepsilon}}}\mid \mathcal{F}^{-1}[(\psi_{s,\mathrm{N}} - \psi_{s,\mathrm{N}_{j}})\mathcal{F}f]\right|\right| |_{2}\\ +\mathrm{C}\varepsilon^{-1}2^{-\delta^{\prime \prime}s_{0}}\left|\left|f\right| \right|_{2},\tag{6.33}
$$

where the second term in (6.33) will be $o(||f||_2)$ for appropriate $s_0$. Thus it suffices to verify (6.31), defining now

$$
\mathcal{M}_{j}f = \sup_{\substack{\mathrm{N}_{j} <   \mathrm{N} <   \mathrm{N}_{j + 1}\\ \mathrm{N}\in \mathrm{Z}_{\varepsilon}}}|  \mathcal{F}^{-1}[(w_{\mathrm{N}} - w_{\mathrm{N}_{j}})  \mathcal{F}f] |,\tag{6.34}
$$

where  $w_{N}$  is given by (6.9). The reader will indeed verify that summing up the first terms of (6.33) over  $j = 1, \ldots, J$  will only introduce an additional factor (depending on  $s_{0}$ ).

Let $\chi = \chi_{[0,1]}$ and

$$
\widetilde {\mathcal {M}} _ {j} f = \sup _ {\mathrm{N} _ {j} <   \mathrm{N} <   \mathrm{N} _ {j + 1}} | f * (\chi_ {(\mathrm{N} ^ {d})} - \chi_ {(\mathrm{N} _ {j} ^ {d})}) |,\tag{6.35}
$$

where $\chi_t = \frac{1}{t}\chi_{[0,t]}$. Since the following inequality clearly holds pointwise (with $v_{\mathrm{s}}$ as in section 3),

$$
\{\sum_ {j = 1} ^ {J} (\widetilde {\mathcal {M}} _ {j} f) ^ {2} \} ^ {1 / 2} \leqslant J ^ {1 / 4} | | \{f * \chi_ {N} | N = 1, 2, \dots \} | | _ {v _ {4}},\tag{6.36}
$$

is follows from (6.36) and (3.26) that

$$
\sum_ {j = 1} ^ {J} \left| \left| \widetilde {\mathcal {M}} _ {j} f \right| \right| _ {2} ^ {2} \leqslant \mathrm{CJ} ^ {1 / 2} \left| \left| f \right| \right| _ {2} ^ {2}
$$

hence

$$
\sum_ {j = 1} ^ {J} \left| \left| \mathcal {M} _ {j} f \right| \right| _ {2} ^ {2} \leqslant C \sum_ {N \in Z _ {\xi}} \left| \left| \mathcal {F} ^ {- 1} [ (w _ {N} - \mathcal {F} (\chi_ {N ^ {d}})) \mathcal {F} f \right| \right| _ {2} ^ {2} + C J ^ {1 / 2} \left| \left| f \right| \right| _ {2} ^ {2}.\tag{6.37}
$$

This first term in (6.37) is bounded by

$$
\sup _ {\alpha} \left[ \sum_ {N \in Z _ {\varepsilon}} | w _ {N} (\alpha) - \hat {\chi} (N ^ {d} \alpha) | ^ {2} \right] \| f \| _ {2} ^ {2} <   C _ {\varepsilon} \| f \| _ {2} ^ {2}\tag{6.38}
$$

using the fact that, by (6.12), (6.13),

$$
\left| w _ {N} (\alpha) - \widehat {\chi} (N ^ {d} \alpha) \right| \leqslant C \min \left(\left| \alpha \right| N ^ {d}, \left(\left| \alpha \right| N ^ {d}\right) ^ {- 1 / d}\right).\tag{6.39}
$$

Hence, for $\mathcal{M}_j f$ defined by (6.34), one has, by (6.37) and (6.38),

$$
\Sigma \left| \left| \mathcal {M} _ {j} f \right| \right| _ {2} \leqslant \mathrm{C} _ {\varepsilon} \mathrm{J} ^ {3 / 4} \left| \left| f \right| \right| _ {2}\tag{6.40}
$$

independently of the choice of the sequence  $N_{1} \ll N_{2} \ll \ldots \ll N_{J}$ . The proof of (6.31) is now completed, and so is the proof of Theorem 1 for  $L^{2}$ -functions.

Observe finally that if T is weakly mixing, then  $A_{N}f \to \int f d\mu$  in  $L^{2}$  (hence a.s.). Indeed T has no point spectrum as unitary operator and  $\frac{1}{N}\sum_{n \leq N} z^{p(n)} \xrightarrow{N \to \infty} 0$  for

$$
z \in \mathbf {C} _ {1} = \{z \in \mathbf {C} | | z | = 1 \},
$$

except on a countable set.

## 7. Ergodic Theorems in $\mathbf{L}^p$, $p > 1$

The purpose of this section is to extend the  $L^{2}$ -theory to  $L^{p}$ , p > 1. Of course, only the maximal inequality

$$
\left| \left| \sup _ {\mathbf {N}} \right| A _ {\mathbf {N}} f \right| \left| \right| _ {p} \leqslant c \left| \right| f \left| \right| _ {p}\tag{7.1}
$$

needs to be shown. Once (7.1) is obtained, the a.s. convergence for functions $f$ of class $\mathbf{L}^p(\mu)$ reduces to bounded functions and hence is taken care of by the $\mathbf{L}^2$ result, obtained in the previous section.

The partial result was obtained in $\left[\mathrm{B}_{2}\right]\left(p > \frac{1 + \sqrt{5}}{2}\right)$.

Considering again the shift model  $(\mathbf{Z}, \mathbf{S})$ , (7.1) becomes

$$
\left| \left| \sup \right| f * \mathrm{K} _ {\mathrm{N}} \right| \left| \right| _ {p} \leqslant \mathrm{C} \left| \left| f \right| \right| _ {p}; \quad \mathrm{K} _ {\mathrm{N}} = \frac {1}{\mathrm{N}} \sum_ {n = 1} ^ {\mathrm{N}} \delta_ {\{p (n) \}}.\tag{7.2}
$$

The proof of (7.2) by Fourier Analysis methods is more delicate than in the  $L^{2}$ -case because the Fourier multipliers involved in the argument need to have goods bounds on  $L^{p}$ .

We use the notation of the previous section. Thus in particular

$$
\mathrm{S} (\theta) = 1 / q \sum_ {r = 0} ^ {q - 1} e ^ {- 2 \pi i p (r) \theta} \quad \text { for } \theta = a / q \text { and } w _ {\mathrm{N}} (\beta) = \int_ {0} ^ {1} e ^ {- 2 \pi i p (\mathrm{Ny}) \beta} d y.\tag{7.3}
$$

Denote again by $\zeta$ a smooth function on $\mathbf{R}$, $0 \leqslant \zeta \leqslant 1$, supp $\zeta \subset [-1/2, 1/2]$ and $\zeta = 1$ on $[-1/4, 1/4]$.

The following lemma will be useful when comparing  $\mathbf{L}^{\nu}(\mathbf{R})$  and  $\ell^{\nu}(\mathbf{Z})$ -norms.

Lemma 7.4. — For $1 < q < \varepsilon D, \varepsilon = o(1)$, one has

$$
\left| \left| \int \mathrm{F} (\beta) e ^ {2 \pi i \beta q y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\mathbf {L} ^ {p} (\mathbf {R})} \sim \left| \left| \int \mathrm{F} (\beta) e ^ {2 \pi i \beta q y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\ell^ {p} (\mathbf {Z})}.\tag{7.5}
$$

Proof. — Observe that, by Bernstein's inequality and the hypothesis,

$$
\left| \left| \int \mathrm{F} (\beta) [ e ^ {2 \pi i q \beta u} - 1 ] e ^ {2 \pi i q \beta y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\mathbf {L} ^ {p}} \leqslant \mathrm{C} \varepsilon \left| \left| \int \mathrm{F} (\beta) e ^ {2 \pi i q \beta y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\mathbf {L} ^ {p}}\tag{7.6}
$$

for $0 \leqslant u \leqslant 1$.

We first prove the inequality $||||_{t^p(\mathbf{Z})} \leqslant \rho ||||_{L^p(\mathbf{R})}$ in (7.5), for some bounded $\rho$. Let $0 \leqslant u < 1$ and write

$$
\begin{array}{r l} \left| \left| \int \mathrm{F} (\beta) e ^ {2 \pi i \beta q y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\ell^ {p}} & \leqslant \left| \left| \int \mathrm{F} (\beta) e ^ {2 \pi i \beta q (y + u)} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\ell^ {p}} + \\ & + \left| \left| \int \mathrm{F} (\beta) [ 1 - e ^ {2 \pi i \beta q u} ] e ^ {2 \pi i \beta q y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\ell^ {p}}. \end{array}\tag{7.7}
$$

Integrating the pth power of the first term in (7.7) in u, the  $\mathbf{L}^{p}(\mathbf{R})$ -norm is obtained. Let  $\rho$  be an a priori constant satisfying the above inequality; the second term in (7.7) may be estimated for fixed u

$$
\begin{array}{r l} \rho \left| \left| \int \mathrm{F} (\beta) [ 1 - e ^ {2 \pi i \beta q u} ] e ^ {2 \pi i \beta q y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\mathbf {L} ^ {p}} \\ & \leqslant \mathrm{C} \varepsilon \rho \left| \left| \int \mathrm{F} (\beta) e ^ {2 \pi i q \beta y} \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\mathbf {L} ^ {p}}, \end{array}
$$

invoking (7.6). Thus it follows that $\rho \leqslant 1 + C\varepsilon \rho$, hence the boundedness of $\rho$.

To prove the converse inequality in (7.5), write

$$
\left| \right| \left| \right| _ {\mathbf {L} ^ {p} (\mathbb {R})} \leqslant \left| \right| \left| \right| _ {\ell^ {p} (\mathbb {Z})} + \left\{\int_ {0} ^ {1} \left| \right| \int \mathrm{F} (\beta) e ^ {2 \pi i \beta q v} [ 1 - e ^ {2 \pi i \beta q u} ] \zeta (\mathrm{D} \beta) d \beta \left| \right| _ {\ell^ {p} (d y)} ^ {p} d u \right\} ^ {1 / p}\tag{7.8}
$$

and apply the inequality $||||_{\ell^p} \leqslant \rho ||||_{L^p}$ and (7.6) to estimate

$$
\left| \left| \int \mathrm{F} (\beta) e ^ {2 \pi i \beta \alpha y} [ 1 - e ^ {2 \pi i \beta \alpha u} ] \zeta (\mathrm{D} \beta) d \beta \right| \right| _ {\ell^ {p} (d y)} \leqslant \mathrm{C} \varepsilon \rho | | \mathrm{F} (\beta) e ^ {2 \pi i q \beta y} \zeta (\mathrm{D} \beta) d \beta | | _ {\mathbf {L} ^ {p}}\tag{7.9}
$$

for $0 \leqslant u \leqslant 1$. Since $\mathbf{C}_{\varepsilon \rho} < 1/2$ for $\varepsilon$ small enough, substitution of (7.9) in (7.8) yields the converse inequality, proving (7.5).

Lemma 7.10. — For S(θ) defined by (7.3), the ℓ¹(Z)-norm of the Fourier transform of the function on Π

$$
\sum_ {0 \leqslant a \leqslant q} \mathrm{S} \left(\frac {a}{q}\right) \mathrm{F} \left(\alpha - \frac {a}{q}\right)\tag{7.11}
$$

is bounded by

$$
q \sum_ {j \in \mathbf {Z}} \sup _ {0 \leqslant x <   q} | \mathcal {F F} (j q + x) |.\tag{7.12}
$$

Proof. — By definition of S(θ), the Fourier transform of (7.11) at the point x ∈ Z equals

$$
\sum_ {0 \leqslant a <   q} \mathrm{S} \left(\frac {a}{q}\right) e ^ {2 \pi \mathrm{i} (a / q) x} \mathcal {F} \mathrm{F} (x) = (\# \{0 \leqslant r <   q | x - p (r) \in q \mathbf {Z} \}) \mathcal {F} \mathrm{F} (x).
$$

Thus the $\ell^1 (\mathbf{Z})$-norm is bounded by $\sum_{r = 0}^{q - 1}\sum_{j\in \mathbf{Z}}|\mathcal{FF}(jq + p(r))|$, hence by (7.12)

Lemma 7.13. — Let $1 < q < \mathbf{D}$. Then, with the notation (7.3),

$$
\left| \left| \sum_ {0 \leqslant a <   q} S \left(\frac {a}{q}\right) \int w _ {N} \left(\alpha - \frac {a}{q}\right) \zeta \left(D \left(\alpha - \frac {a}{q}\right)\right) e ^ {2 \pi i \alpha x} d \alpha \right| \right| _ {\ell^ {1} (Z)} <   G.\tag{7.14}
$$

Proof. — Apply (7.10) with  $\mathbf{F}(\beta) = w_{\mathbf{N}}(\beta) \zeta(\mathbf{D}\beta)$ . It follows from (7.3) that  $w_{\mathbf{N}}(\beta)$  is the Fourier transform of the image measure  $v_{N}$  under the mapping  $p(Ny) : [0, 1] \to \mathbb{R}$ . Hence  $FF = v_{N} * (\mathcal{F}^{-1}[\zeta])_{D}$  and (7.12) is bounded by

$$
\frac {q}{D} \sum_ {j \in \mathbf {Z}} \sup _ {0 \leqslant x <   q} \int_ {0} ^ {1} \left| \mathcal {F} ^ {- 1} [ \zeta ] \left(\frac {x + j q - p (N y)}{D}\right) \right| d y.\tag{7.15}
$$

Since $|\mathcal{F}^{-1}[\zeta](t)| < \mathbf{C}(1 + t^2)^{-1}$, one has

$$
\sum_ {j \in \mathbb {Z}} \sup _ {0 \leqslant x <   q} \left| \mathcal {F} ^ {- 1} [ \zeta ] \left(\frac {x + j q}{\mathrm{D}}\right) \right| <   \mathrm{C} \left(\frac {\mathrm{D}}{q} + 1\right).
$$

Substituting in (7.15), (7.14) follows.

One has the following real Analysis maximal inequality:

Lemma 7.16. — For $p > 1$ and $f \in \mathbf{L}^p(\mathbf{R})$

$$
\left| \right| \sup _ {\mathbf {N}} | \mathcal {F} ^ {- 1} [ w _ {\mathbf {N}} \mathcal {F} f ] | \left| \right| _ {\mathbf {L} ^ {p} (\mathbf {R})} \leqslant \mathrm{C} \left| \right| f \left| \right| _ {\mathbf {L} ^ {p} (\mathbf {R})}.\tag{7.17}
$$

Proof. — As observed earlier,  $w_{N}$  is the Fourier transform of the measure  $v_{N}$ , image of the measure dy/N under the mapping  $p: [0, N] \to R$ . Thus we have to estimate  $\left|\left|\sup_{N}\left|f * v_{N}\right|\right|\right|_{p}$ . For t sufficiently large, one has that  $\frac{d v_{N}}{ds}\bigg|_{s=t}=1/Np'(p^{-1}(t))$  which is of the order  $(1/N)t^{-1+(1/d)}$  in size. Thus the problem reduces to show that

$$
\left| \left| \sup _ {\mathbf {N}} \right| f * \left[ (1 / \mathrm{N}) t ^ {- 1 + (1 / d)} \chi_ {[ 0, \mathrm{N} d ]} (t) \right] \right| \left| \right| _ {\mathcal {P}} \leqslant \mathrm{C} \left| \right| f \left| \right| _ {\mathcal {P}}.\tag{7.18}
$$

Defining $k(t) = t^{-1 + (1 / d)}\chi_{[0,1]}$, (1/N) $t^{-1 + (1 / d)}\chi_{[0,\mathbf{N}^d ]}(t) = k_{(\mathbf{N}^d)}$, where $k_{s}(t) = \frac{1}{s} k\left(\frac{t}{s}\right)$, $s > 0$. The fact that

$$
\left| \right| \sup _ {s > 0} | f * k _ {s} | \| _ {\mathcal {P}} \leqslant \mathrm{C} \| f \| _ {\mathcal {P}}\tag{7.19}
$$

follows from the Hardy-Littlewood maximal function boundedness on R. This proves the lemma.

Next, we prove a discrete maximal inequality:

$$
\begin{array}{l} \text { Lemma   7.20. } - \text { Let } 1 <   q <   \varepsilon \mathrm{D}, \varepsilon = o (1). \text { Then,for } p > 1, \\ \left\| \sup _ {\mathbf {N}} \left| \sum_ {0 \leqslant a <   q} \int w _ {\mathbf {N}} (\beta) \mathcal {F} f \left(\frac {a}{q} + \beta\right) \zeta (\mathrm{D} \beta) e ^ {2 \pi i x \left(\frac {a}{q} + \beta\right)} d \beta \right| \right\| _ {\mathrm{L} ^ {p} (\mathbf {Z})} \\ \leqslant \mathrm{C} _ {p} \| f \| _ {\ell^ {p} (\mathbf {Z})}. \end{array}\tag{7.21}
$$

Proof. — The main ingredient will be (7.16) and the problem is to pass from R to Z. Writing  $x \in Z$  as  $x = yq + z$ ,  $z = 0, 1, \ldots, q - 1$ , the left member of (7.21) equals

$$
\left\{\sum_ {0 \leqslant z <   q} \left| \left| \sup _ {\mathbf {N}} \right| \int w _ {\mathbf {N}} (\beta) F _ {z} (\beta) \zeta (D \beta) e ^ {2 \pi i \beta q y} d \beta \right| \left| \right| _ {\ell^ {p} (d y)} ^ {p} \right\} ^ {1 / p}\tag{7.22}
$$

with

$$
\mathrm{F} _ {z} (\beta) = \sum_ {0 \leqslant a <   q} \mathcal {F} f \left(\frac {a}{q} + \beta\right) e ^ {2 \pi i z \left(\frac {a}{q} + \beta\right)}.\tag{7.23}
$$

As in the proof of (7.4), denote by $\rho$ the a priori best constant in the inequality

$$
\left| \left| \sup _ {N} \right| \int w _ {N} (\beta) F (\beta) \zeta (D \beta) e ^ {2 \pi i \beta a v} d \beta \right| \left| \right| _ {\ell^ {p}} \leqslant \rho \left| \left| \int F (\beta) \zeta (D \beta) e ^ {2 \pi i \beta a v} d \beta \right. \right| _ {\ell^ {p}}.\tag{7.24}
$$

For $0 \leqslant u < 1$, write

$$
\begin{array}{r l} \sup _ {\mathbf {N}} \left| \int w _ {\mathbf {N}} (\beta) \mathrm{F} (\beta) \zeta (\mathrm{D} \beta) e ^ {2 \pi i \beta a y} d \beta \right| & \leqslant \\ \sup _ {\mathbf {N}} \left| \int w _ {\mathbf {N}} (\beta) \mathrm{F} (\beta) \zeta (\mathrm{D} \beta) e ^ {2 \pi i \beta a (y + u)} d \beta \right| \\ & + \sup _ {\mathbf {N}} \left| \int w _ {\mathbf {N}} (\beta) \mathrm{F} (\beta) \zeta (\mathrm{D} \beta) [ e ^ {2 \pi i \beta a u} - 1 ] e ^ {2 \pi i \beta a y} d \beta \right|. \end{array}\tag{7.25}
$$

Integrating the $p$th power of the first term of (7.25) in $u \in [0,1]$ gives, by (7.16) and (7.4)

$$
\begin{array}{r l} q ^ {- 1 / p} \left| \left| \sup _ {N} \right| \mathcal {F} ^ {- 1} [ w _ {N} F \zeta (D.) ] \right| & \| _ {L ^ {p}} \leqslant \\ C q ^ {- 1 / p} \left| \left| \mathcal {F} ^ {- 1} [ F \zeta (D.) ] \right| \right| _ {L ^ {p}} = \\ C \left| \left| \int F (\beta) \zeta (D \beta) e ^ {2 \pi i \beta q y} d \beta \right| \right| _ {L ^ {p} (d y)} & \sim \left| \left| \int F (\beta) \zeta (D \beta) e ^ {2 \pi i q y} d \beta \right| \right| _ {\ell^ {p} (d y)}. \end{array}\tag{7.26}
$$

By definition of $\rho$, the $\ell^p$-norm of the second term in (7.25) is, for fixed $u \in [0, 1]$, bounded by

$$
\rho \left| \left| \int F (\beta) [ e ^ {2 \pi i \beta q u} - 1 ] \zeta (D \beta) e ^ {2 \pi i \beta q y} d \beta \right| \right| _ {\ell^ {p}}.\tag{7.27}
$$

Apply consecutively (7.5), (7.6, (7.5) to estimate (7.27) by

$$
\mathbf {C} \varepsilon \rho \left| \left| \int \mathbf {F} (\beta) \zeta (\mathrm{D} \beta) e ^ {2 \pi i \beta q y} d \beta \right| \right| _ {\ell^ {p}}.\tag{7.28}
$$

From (7.26), (7.27), (7.28), it follows that $\rho \leqslant \mathbf{C} + \mathbf{C}\varepsilon \rho$ implies $\rho < \mathbf{C}$, assuming $\varepsilon$ small enough. This yields (7.24).

Applying (7.24) with $\mathbf{F} = \mathbf{F}_z$ and substitution of (7.23) yields

$$
\begin{array}{r l} \left| \left| \sup _ {N} \right| \int w _ {N} (\beta) F _ {z} (\beta) \zeta (D \beta) e ^ {2 \pi i \beta q y} d \beta \right| & \bigg | \bigg | _ {\ell^ {p} (d y)} \leqslant \\ C \left| \left| \sum_ {0 \leqslant a <   q} e ^ {2 \pi i z (a / q)} \left[ \int \mathscr {F} f \left(\frac {a}{q} + \beta\right) \zeta (D \beta) e ^ {2 \pi i \beta (q y + z)} d \beta \right] \right| \right| _ {\ell^ {p} (d y)} = \\ C \left| \left| \sum_ {0 \leqslant a <   q} \mathscr {F} ^ {- 1} \left[ \mathscr {F} f \cdot \zeta \left(D \left(\cdot - \frac {a}{q}\right)\right) \right] (q y + z) \right| \right| _ {\ell^ {p} (d y)} \end{array}
$$

and summation over $z = 0, \ldots, q - 1$ gives the following estimate on (7.22)

$$
\left| \left| f * \mathscr {F} ^ {- 1} \left[ \sum_ {0 \leqslant a <   q} \zeta \left(\mathrm{D} \left(\cdot - \frac {a}{q}\right)\right) \right] \right| \right| _ {\ell^ {p}} <   \mathrm{C} | | f | | _ {\ell^ {p}}.
$$

This completes the proof of Lemma 7.20.

Lemma 7.29. — Under the hypothesis of Lemma (7.20), for $p > 1$,

$$
\left|\left| \sup _ {\mathbf {N}} \right| \sum_ {0 \leqslant a <   q} \mathrm{S} \left(\frac {a}{q}\right) \int w _ {\mathrm{N}} (\beta) \mathscr {F} f \left(\frac {a}{q} + \beta\right) \zeta (\mathrm{D} \beta) e ^ {2 \pi i x \left(\frac {a}{q} + \beta\right)} d \beta \right|\left. \right| _ {\ell^ {p}} \leqslant \mathrm{C} _ {\boldsymbol {p}} | | f | | _ {\ell^ {p}}.\tag{7.30}
$$

Proof. — Apply (7.21) to the function g given by

$$
\mathcal {F} g (\alpha) = \left[ \sum_ {0 \leqslant a <   q} \mathrm{S} \left(\frac {a}{q}\right) \zeta \left(\frac {\mathrm{D}}{4} \left(\alpha - \frac {a}{q}\right)\right) \right] \mathcal {F} f (\alpha).\tag{7.31}
$$

Observe that $\zeta\left(\frac{D}{4}\beta\right)\zeta(D\beta)=\zeta(D\beta)$ and that the first factor in (7.31) is the Fourier-transform of an $\ell^{1}(\mathbf{Z})$-function, by taking $w_{N}=1$ in (7.14). Inequality (7.30) now follows.

The following lemma in an important new ingredient in proving (7.1).

Lemma 7.32. — One has the following restricted maximal inequality:

$$
\left| \left| \sup _ {\mathbf {N} _ {0} <   \mathbf {N} <   \mathbf {N} _ {0} ^ {2}} | f * \mathrm{K} _ {\mathbf {N}} | \right| \right| _ {\mathfrak {p}} \leqslant \mathrm{C} _ {\mathfrak {p}} (\log \log \mathrm{N} _ {0}) \| f \| _ {\mathfrak {p}} \quad \text { for } p > 1.\tag{7.33}
$$

This is a problem about positive functions and hence N may be taken of the form  $N = 2^{k}$ ,  $k_{0} \leqslant k \leqslant 2k_{0}$ . Instead of considering the  $\ell^{p}(\mathbf{Z})$ -inequality, we will rather deal with functions f taken on a finite cyclic group  $G \equiv Z_{J} = Z/JZ$ , where J is taken large enough (depending on  $N_{0}$ ). The measure on G is the normalized counting measure and  $f * K_{N}$  is the convolution on G of f and  $\frac{1}{N} \sum_{1 \leqslant n \leqslant N} \delta_{\{\mathcal{P}(n)\}}$ . The inequality (7.33) is equivalent to

$$
\left| \right| \sup _ {k _ {0} \leqslant k \leqslant 2 k _ {0}} | f * \mathrm{K} _ {2 k} | \left| \right| _ {\mathrm{L} ^ {p} (\mathrm{G})} \leqslant \mathrm{C} _ {p} (\log k _ {0}) \left| | f | \right| _ {\mathrm{L} ^ {p} (\mathrm{G})}.\tag{7.34}
$$

The reason for this set-up is to invoke Stein's extrapolation theorem [St] according to which the inequalities (7.34) for $p > 1$ follow from the weaker inequalities

$$
\left| \right| \sup _ {k _ {0} \leqslant k \leqslant 2 k _ {0}} | f * \mathrm{K} _ {2 ^ {k}} | \left| \right| _ {\mathrm{L} ^ {1} (\mathrm{G})} \leqslant \mathrm{C} _ {p} (\log k _ {0}) | | f | | _ {\mathrm{L} ^ {p} (\mathrm{G})}.\tag{7.35}
$$

Since (7.35) weakens for increasing $p$, one may assume that $q = p' = p / (p - 1)$ is an integer. We replace (7.35) by its dual version

$$
\left| \right| \sum_ {k = k _ {0}} ^ {2 k _ {0}} \left(g _ {k} * \mathrm{K} _ {2 ^ {k}}\right) \left| \right| _ {q} <   \mathrm{C} _ {q} (\log k _ {0})\tag{7.36}
$$

whenever

$$
g _ {k} \geqslant 0, \quad \Sigma g _ {k} \leqslant 1.\tag{7.37}
$$

Let M (to be specified later) satisfy

$$
\mathbf {M} \sim \log k _ {\mathbf {0}}\tag{7.38}
$$

and put $\mathbf{L}_k = \mathbf{K}_{2^{\mathbf{uk}}}$ for simplicity. By splitting in sub-sums, (7.36) will clearly follow from

$$
\left| \right| \sum_ {k _ {0} <   k <   2 k _ {0}} \left(g _ {k} * \mathrm{L} _ {k}\right) \left| \right| _ {q} <   \mathrm{C} _ {q}\tag{7.39}
$$

whenever $\{g_k\}$ fulfils (7.37). Denote by $\rho$ the smallest constant $\mathbf{C}_q$ satisfying (7.39). In the sequel, let $\mathbf{C}$ stand for a constant depending on $q$.

Expanding the qth power of a sum and integrating, we have

(7.40)

$$
\begin{array}{r l} & {| | \sum_ {k _ {0} <   k <   2 k _ {0}} (g _ {k} * \mathrm{L} _ {k}) | | _ {q} ^ {q} \leqslant} \\ & {\quad \mathrm{C} \sum_ {k _ {0} <   k _ {1} <   \dots <   k _ {q} <   2 k _ {0}} \int_ {\mathrm{G}} (g _ {k _ {1}} * \mathrm{L} _ {k _ {1}}) \dots (g _ {k _ {q}} * \mathrm{L} _ {k _ {q}})} \end{array}\tag{7.41}
$$

$$
+ \mathrm{C} \int_ {\mathrm{G}} [ \sum_ {k _ {0} <   k <   2 k _ {0}} (g _ {k} * \mathrm{L} _ {k}) ] ^ {q - 1},
$$

where (7.41) is bounded by $\rho^{k - 1}$.

Choosing M appropriately, we will achieve the estimate

$$
\left| \left[ g _ {k _ {2}} * \mathrm{L} _ {k _ {2}}\right) \dots \left(g _ {k _ {q}} * \mathrm{L} _ {k _ {q}}\right) \right] * \left(\mathrm{L} _ {k _ {1}} - \mathrm{L} _ {k _ {0}}\right) \left| \right| _ {\mathrm{L} ^ {2} (\mathrm{G})} \leqslant k _ {0} ^ {- q}\tag{7.42}
$$

whenever $k_0 < k_1 < k_2 < \ldots < k_q < 2k_0$.

Once (7.42) is obtained, write

$$
\begin{array}{r l} & {\left| \int_ {\mathrm{G}} (g _ {k _ {1}} * \mathrm{L} _ {k _ {1}}) (g _ {k _ {2}} * \mathrm{L} _ {k _ {2}}) \dots (g _ {k _ {q}} * \mathrm{L} _ {k _ {q}}) \right.} \\ & {\qquad \left. - \int_ {\mathrm{G}} (g _ {k _ {1}} * \mathrm{L} _ {k _ {0}}) (g _ {k _ {2}} * \mathrm{L} _ {k _ {2}}) \dots (g _ {k _ {q}} * \mathrm{L} _ {k _ {q}}) \right| <   k _ {0} ^ {- q}} \end{array}
$$

and estimate (7.40) by

$$
\mathrm{C} + \sum_ {k _ {0} <   k _ {2} <   \dots <   k _ {q} <   2 k _ {0}} \int_ {\mathrm{G}} \left[ \left(\sum_ {k _ {0} <   k <   2 k _ {0}} g _ {k}\right) * \mathrm{L} _ {k _ {0}} \right] \left(g _ {k _ {2}} * \mathrm{L} _ {k _ {2}}\right) \dots \left(g _ {k _ {q}} * \mathrm{L} _ {k _ {q}}\right).\tag{7.43}
$$

Since the first factor in the integrand is 1-bounded, by (7.37), (7.43) turns out to be bounded by (7.41), thus by $\mathbf{C}\rho^{k-1}$. Consequently, one gets $\rho^k < \mathbf{C} + \mathbf{C}\rho^{k-1}$, hence $\rho < \mathbf{C}$, proving (7.39), thus (7.36) and (7.33). It remains to obtain (7.42).

Proof of (7.42). — This is an  $L^{2}$ -problem and we use the Fourier transform method. Denote  $g_{k_{r}}$  by  $g_{r}$  and let  $N_{r}=2^{Mk_{r}}$ .

We keep the notation F for the Fourier transform on Z and identify G with the integer interval  $[0, J]$  endowed with normalized counting measure.

For each r, let  $s_{r}$  be increasing integers to be specified later. With the notation of the previous section and D to be specified, define

$$
\Omega_ {r} = \sum_ {s \leqslant s _ {r}} \sum_ {\theta \in \mathcal {R} _ {s}} S (\theta) w _ {N _ {r}} (\alpha - \theta) \zeta (1 0 ^ {s} (\alpha - \theta)) \zeta (D ^ {- 1} N _ {r} ^ {d} (\alpha - \theta)).\tag{7.44}
$$

It follows from (6.15), (6.11), (6.13) that, for some $\delta > 0$,

$$
\left| \mathcal {F} \left[ L _ {k _ {r}} \right] (\alpha) - \Omega_ {r} (\alpha) \right| <   C \left(N _ {r} ^ {- \delta} + 2 ^ {- s _ {r} \delta} + D ^ {- 1 / d}\right).\tag{7.45}
$$

Since, from the definition (6.6) of $\mathcal{R}_s$, one clearly has

$$
\left| \left| \mathcal {F} ^ {- 1} \left(\Omega_ {r}\right) \right| \right| _ {\ell^ {1} (\mathbf {Z})} \leqslant \mathrm{C} 4 ^ {s _ {r}},\tag{7.46}
$$

there is a uniform estimate

$$
\mid \mathcal {F} ^ {- 1} [ \Omega_ {r}. \mathcal {F} (g _ {r}) ] \mid \leqslant \mathrm{C} 4 ^ {s _ {r}}.\tag{7.47}
$$

It also follows from (7.45) that

$$
\left| \left| \left(g _ {r} * L _ {k _ {r}}\right) - \mathcal {F} ^ {- 1} \left[ \Omega_ {r} \mathcal {F} \left(g _ {r}\right) \right] \right| \right| _ {L ^ {2} (G)} \leqslant C \left(N _ {r} ^ {- \delta} + 2 ^ {- s _ {r} \delta} + D ^ {- 1 / d}\right).\tag{7.48}
$$

Observe that the Fourier transform of the function $\mathcal{F}^{-1}[\Omega_2\mathcal{F}(g_2)]\ldots \mathcal{F}^{-1}[\Omega_q\mathcal{F}(g_q)]$ vanishes outside a $\mathrm{DN}_2^{-d}$ neighborhood $\Gamma$ of $\{(a / b)\in \Pi \cap \mathbf{Q}|b\leqslant 2^{qs_q}\}$.

Estimate the left member of (7.42) as

$$
\begin{array}{r l} & {| | (g _ {2} * \mathrm{L} _ {k _ {2}}) - \mathcal {F} ^ {- 1} [ \mathcal {F} (g _ {2}) \Omega_ {2} ] | | _ {\mathrm{L} ^ {2} (\mathrm{G})} +} \\ & {\quad | | \mathcal {F} ^ {- 1} [ \mathcal {F} (g _ {2}) \Omega_ {2} ] | | _ {\infty} | | (g _ {3} * \mathrm{L} _ {k _ {3}}) - \mathcal {F} ^ {- 1} [ \mathcal {F} (g _ {3}) \Omega_ {3} ] | | _ {\mathrm{L} ^ {2} (\mathrm{G})} + \dots +} \end{array}\tag{7.49}
$$

$$
\begin{array}{r l} \left| \left| \mathcal {F} ^ {- 1} [ \mathcal {F} (g _ {2}) \Omega_ {2} \right| \right| _ {\infty} \dots & \left| \left| \mathcal {F} ^ {- 1} [ \mathcal {F} (g _ {q - 1}) \Omega_ {q - 1} ] \right| \right| _ {\infty} \left| \right| (g _ {q} * L _ {k _ {q}}) \\ & - \mathcal {F} ^ {- 1} [ \mathcal {F} (g _ {q}) \Omega_ {q} ] \left| \right| _ {L ^ {2} (G)} \end{array}\tag{7.50}
$$

$$
+ \left\| \left\{\mathcal {F} ^ {- 1} \left[ \mathcal {F} \left(g _ {2}\right) \Omega_ {2} \right] \dots \mathcal {F} ^ {- 1} \left[ \mathcal {F} \left(g _ {q}\right) \Omega_ {q} \right] \right\} * \left(\mathrm{L} _ {k _ {1}} - \mathrm{L} _ {k _ {0}}\right) \right\| _ {\mathrm{L} ^ {2} (\mathrm{G})}.
$$

By (7.47) and (7.48), (7.49) is bounded by

$$
\mathbf {C} \sum_ {r = 2} ^ {q} 4 ^ {s _ {3} + \dots + s _ {r - 1}} (\mathrm{N} _ {r} ^ {- \delta} + 2 ^ {- s _ {r} \delta} + \mathrm{D} ^ {- 1 / d}).\tag{7.51}
$$

Making the appropriate choice of the numbers  $s_{r} \sim \log k_{0}$  then allows the estimation

$$
(7. 4 9) \leqslant \frac {1}{1 0} k _ {0} ^ {- q} + k _ {0} ^ {\mathrm{C}}. (\mathrm{N} _ {2} ^ {- \delta} + \mathrm{D} ^ {- 1 / d}).\tag{7.52}
$$

By the remark on the support of the Fourier transform made above, (7.50) is clearly bounded by

$$
\left| \left| \mathcal {F} ^ {- 1} \left[ \mathcal {F} \left(g _ {2}\right) \Omega_ {2} \right] \dots \mathcal {F} ^ {- 1} \left[ \mathcal {F} \left(g _ {q}\right) \Omega_ {q} \right] \right| \right| _ {\mathrm{L} ^ {2} (\mathrm{G})}. \sup _ {\alpha \in \Gamma} | \mathcal {F} \left(\mathrm{L} _ {k _ {1}} - \mathrm{L} _ {k _ {0}}\right) (\alpha) |.\tag{7.53}
$$

Again from (7.49), the first factor in (7.53) is bounded by  $C4^{s_{2}+\cdots+s_{q}}<k_{0}^{C}$ . By definition of  $\Gamma$ , (6.10) and (6.12), one easily verifies that the second factor in (7.53) is at most

$$
\mathrm{CD} \left(\frac {\mathrm{N} _ {1}}{\mathrm{N} _ {2}}\right) ^ {d} + \mathrm{CN} _ {0} ^ {- 1 / 2}\tag{7.54}
$$

provided that

$$
\mathrm{D} 2 ^ {q s _ {q}} <   \mathrm{N} _ {0} ^ {\delta^ {\prime}},\tag{7.55}
$$

which is obviously satisfied for  $D < 2^{\delta k_{0}}$ .

By definition of  $N_{r}$  and since  $k_{1}<k_{2}$ ,

$$
(7. 5 3) \leqslant k _ {0} ^ {\mathrm{C}} [ \mathbf {D} 2 ^ {- \mathbf {M} d} + 2 ^ {- \frac {1}{2} \mathbf {M} k _ {0}} ].\tag{7.56}
$$

Collecting estimates (7.52) and (7.56), the left number of (7.42) is bounded by

$$
\frac {1}{1 0} k _ {0} ^ {- a} + k _ {0} ^ {\mathrm{C}} \left[ \mathrm{D} ^ {- 1 / d} + \mathrm{D} 2 ^ {- \mathbf {M} d} + 2 ^ {- \delta k _ {0}} \right] <   k _ {0} ^ {- a}
$$

for a suitable choice of D,  $\log D \sim \log k_{0}$  and  $M \sim \log k_{0}$  (cf. (7.38)). This completes the proof of (7.42) and hence of Lemma 7.32.

The proof of (7.2) is mainly based on $\mathbf{L}^2$-estimates, (7.29), (7.32) and interpolation.

Proof of (7.2). — Denote by || ||, the  $\ell^{r}(\mathbf{Z})$ -norm in what follows. For  $s = 1, 2, \ldots$ , define

(7.57)

$$
Q _ {s} = 2 ^ {s}!\tag{7.58}
$$

$$
\mathcal {K} _ {s} = \{k \in \mathbf {Z} | 4 ^ {s} \leqslant k <   4 ^ {s + 1} \}
$$

and with previous notation, let

$$
\Omega_ {k, s ^ {\prime}} = \sum_ {0 \leqslant a <   Q _ {s ^ {\prime}}} S \left(\frac {a}{Q _ {s ^ {\prime}}}\right) w _ {2 k} \left(\alpha - \frac {a}{Q _ {s ^ {\prime}}}\right) \zeta \left(Q _ {s ^ {\prime}} ^ {2} \left(\alpha - \frac {a}{Q _ {s ^ {\prime}}}\right)\right)\tag{7.59}
$$

for $s' \leqslant s, k \in \mathcal{K}_s$.

It follows from (6.15), (6.11), (6.13) that for $s' \leqslant s$, $k \in \mathcal{K}_s$

$$
\left| \mathcal {F} [ \mathrm{K} _ {2 k} ] (\alpha) - \Omega_ {k, s ^ {\prime}} (\alpha) \right| <   2 ^ {- \delta^ {\prime} s ^ {\prime}}\tag{7.60}
$$

and by (7.13)

$$
\left| \left| \mathcal {F} ^ {- 1} \left[ \Omega_ {k, s ^ {\prime}} \right] \right| \right| _ {1} <   \mathrm{C}.\tag{7.61}
$$

Fix $1 < p_0 < p < 2$. It follows from (7.30) that

$$
\left| \left| \sup _ {k} \right| \mathcal {F} ^ {- 1} [ \Omega_ {k, s ^ {\prime}} \mathcal {F} f ] \right| \left| \right| _ {p _ {0}} \leqslant C \left| | f | \right| _ {p _ {0}}.\tag{7.62}
$$

For $k\in \mathcal{K}_s$ , write

$$
\begin{array}{r l} f * \mathrm{K} _ {2 k} & = \mathcal {F} ^ {- 1} [ \Omega_ {k, 1} \mathcal {F} f ] + \mathcal {F} ^ {- 1} [ (\Omega_ {k, 2} - \Omega_ {k, 1} ] \mathcal {F} f ] + \dots \\ & \quad + \mathcal {F} ^ {- 1} [ (\Omega_ {k, s} - \Omega_ {k, s - 1}) \mathcal {F} f ] + [ (f * \mathrm{K} _ {2 k}) - \mathcal {F} ^ {- 1} [ \Omega_ {k, s} \mathcal {F} f ] ], \end{array}
$$

so that

(7.63)

$$
\begin{array}{r l} \sup _ {k} | f * \mathrm{K} _ {2 k} | & \leqslant \sum_ {s ^ {\prime}} \sup _ {k \geqslant 4 s ^ {\prime}} | \mathcal {F} ^ {- 1} [ (\Omega_ {k, s ^ {\prime}} - \Omega_ {k, s ^ {\prime} - 1}) \mathcal {F} f ] | \\ & \quad + \sum_ {s} \sup _ {k \in \mathcal {X} _ {s}} | (f * \mathrm{K} _ {2 k}) - \mathcal {F} ^ {- 1} [ \Omega_ {k, s} \mathcal {F} f ] |. \end{array}\tag{By (7.62}
$$

$$
\left| \left| \sup _ {k \geqslant 4 ^ {s ^ {\prime}}} \right| \mathcal {F} ^ {- 1} \left[ \left(\Omega_ {k, s ^ {\prime}} - \Omega_ {k, s ^ {\prime} - 1}\right) \mathcal {F} f \right] \right| \left| \right| _ {p _ {0}} <   C \| f \| _ {p _ {0}}\tag{7.64}
$$

while by (7.33) and (7.62) also

$$
\left| \sup _ {k \in \mathcal {K} _ {s}} \right| (f * \mathrm{K} _ {2 ^ {k}}) - \mathcal {F} ^ {- 1} [ \Omega_ {k, s} \mathcal {F} f ] | | _ {\mathfrak {p} _ {0}} \leqslant \mathrm{C}. s | | f | | _ {\mathfrak {p} _ {0}}.\tag{7.65}
$$

Our purpose is to interpolate (7.64), (7.65) with better  $\ell^{2}$ -estimates. Using (6.15), estimate

$$
\begin{array}{l} \left| \left| \sup _ {k \geqslant 4 ^ {s ^ {\prime}}} \right| (f * K _ {2 k}) - \mathcal {F} ^ {- 1} [ \Omega_ {k, s ^ {\prime}} \mathcal {F} f ] \right| \left| \right| _ {2} \leqslant \\ C \sum_ {k \geqslant 4 ^ {s ^ {\prime}}} 2 ^ {- k \delta_ {1}} + \left| \left| \sup _ {k \geqslant 4 ^ {s ^ {\prime}}} \right| \sum_ {0 \leqslant r \leqslant s ^ {\prime}} \mathcal {F} ^ {- 1} [ \psi_ {r, 2 k}. \mathcal {F} f ] - \mathcal {F} ^ {- 1} [ \Omega_ {k, s ^ {\prime}}. \mathcal {F} f ] \right| \left| \right| _ {2} + \\ \sum_ {r > s ^ {\prime}} \left| \left| \sup _ {k} \right| \mathcal {F} ^ {- 1} [ \psi_ {r, 2 k}. \mathcal {F} f ] \right| \left| \right| _ {2}, \end{array}\tag{7.66}
$$

where $\psi_{r,\mathbf{N}}$ is given by (6.7).

By (6.28), the last term of (7.66) is bounded by $\mathbf{C}.2^{-s'\delta'}||f||_2$.

Write

(7.67)

$$
\begin{array}{l}\Omega_{k,s^{\prime}} - \sum_{r\leqslant s^{\prime}}\psi_{r,2^{k}} = \\ \sum_{r\leqslant s^{\prime}}\sum_{\theta \in \mathcal{R}_{r}}S(\theta) w_{2k}(\alpha - \theta)[\zeta (Q_{s^{\prime}}^{2}(\alpha - \theta)) - \zeta (10^{r}(\alpha - \theta))]\\ +\sum_{\substack{q|Q_{s^{\prime}}\\ q\geqslant 2^{s^{\prime} + 1}}}\sum_{\substack{1\leqslant a\leqslant q\\ (a,q) = 1}}S\left(\frac{a}{q}\right)w_{2k}\left(\alpha - \frac{a}{q}\right)\zeta \left(Q_{s^{\prime}}^{2}\left(\alpha - \frac{a}{q}\right)\right). \end{array}\tag{7.68}
$$

There is a uniform estimate on (7.67) for $k \geqslant 4^{s'}$ by

$$
\mathrm{C}. 4 ^ {s ^ {\prime}}. \sup _ {| \beta | > \mathbf {Q} _ {s ^ {\prime}} ^ {- 2}} | w _ {2 k} (\beta) | <   \mathrm{C} 2 ^ {- k / 2}\tag{7.69}
$$

in view of (6.13) and (7.57). Thus (7.67) contributes to the maximal function for at most  $C2^{-s'}$ .

As was done in section 6 to prove (6.28), (6.29), one estimates the maximal function contribution of (7.68) (in $\ell^2$) by C. $2^{-\delta' s'}$.

Collecting estimates yields the bound C. $2^{-\delta^{\prime}s^{\prime}}$ on (7.66). Hence also, by subtraction

$$
\left| \sup _ {k \geqslant 4 ^ {s ^ {\prime}}} \right. | \mathcal {F} ^ {- 1} [ (\Omega_ {k, s ^ {\prime}} - \Omega_ {k, s ^ {\prime} - 1}) \mathcal {F} f ] | | _ {2} \leqslant C. 2 ^ {- \delta^ {\prime} s ^ {\prime}} | | f | | _ {2}\tag{7.70}
$$

while

$$
\left| \sup _ {k \in \mathcal {K} _ {s}} \right| (f * \mathrm{K} _ {2 k}) - \mathscr {F} ^ {- 1} \left[ \Omega_ {k s}. \mathscr {F} f \right] | | _ {2} \leqslant \mathrm{C}. 2 ^ {- \delta^ {\prime s}} | | f | | _ {2}.\tag{7.71}
$$

Interpolating (7.64), (7.70) at $p_0 < p < 2$ yields the corresponding $\ell^p$-inequality with constant $C.2^{-\delta_p s'}$. Similarly when interpolating (7.65), (7.71), and $\ell^p$-estimate $C.2^{-\delta_p s}$ is found. Here $\delta_p > 0$ depends on $p > 1$. Substitution of these bounds in (7.63) yields

$$
\left| \left| \sup _ {k} | f * \mathrm{K} _ {2 k} | \right| \right| _ {p} \leqslant \mathrm{C} \sum_ {s ^ {\prime}} 2 ^ {- \delta_ {p} s ^ {\prime}} + \mathrm{C} \sum_ {s} 2 ^ {- \delta_ {p} s} <   \mathrm{C},
$$

completing the proof of (7.2).

## 8. Integer Parts of Polynomial Sequences

Consider a polynomial with real coefficients $(d\geqslant 1)$

$$
p (x) = b _ {0} + b _ {1} x + \dots + b _ {d} x ^ {d}, \quad b _ {d} > 0\tag{8.1}
$$

and for a given $\mathbf{DS}(\Omega, \mathcal{B}, \mu, \mathbf{T})$ the averages

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{\mathbf {N}} \sum_ {n = 1} ^ {\mathbf {N}} \mathrm{T} ^ {[ p (n) ]} f\tag{8.2}
$$

where $[y]$ stands for the integer part of $y$. Here we let $f$ be of class $\mathbf{L}^{\infty}(\Omega, \mu)$. In proving the a.s. convergence of (8.2), one may assume at least one of the coefficients $b_{1}, \ldots, b_{d}$ irrational. Otherwise, if $b_{j} = (a_{j}/q) (1 \leqslant j \leqslant q)$, write $n = mq + r (0 \leqslant r < q)$ and

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{q} \sum_ {0 \leqslant r <   q} \frac {1}{\mathrm{N} q ^ {- 1}} \sum_ {m \leqslant \mathrm{N} q ^ {- 1}} \mathrm{T} ^ {p _ {1} (m)} (\mathrm{T} ^ {[ p (r) ]} f)
$$

where $p_1(m) = p(mq + r) - p(r)$ has integer coefficients. The a.s. convergence of the $A_N f$ is thus implied by Theorem 1 of this paper.

Assuming that $b_{1}, \ldots, b_{d}$ are not all rational, the sequence

$$
\{p (n) - [ p (n) ] \mid n = 1, 2, \dots \}
$$

is uniformly distributed in [0, 1]. Fix $\varepsilon < 0$ and consider the function $\tau = \tau_{\varepsilon}$ on $\mathbf{R}$

![](images/page_34_image_14.jpg)

Set

$$
\widetilde {\mathrm{A}} _ {\mathrm{N}} f = \frac {1}{\mathrm{N}} \sum_ {n = 1} ^ {\mathrm{N}} \sum_ {m \in \mathbf {Z}} \tau (p (n) - m) \mathrm{T} ^ {m} f.\tag{8.3}
$$

Clearly, invoking the uniform distribution property, there is the pointwise inequality

$$
\left| \mathrm{A} _ {\mathrm{N}} f - \widetilde {\mathrm{A}} _ {\mathrm{N}} f \right| \leqslant \frac {| | f | | _ {\infty}}{\mathrm{N}} \sharp \{1 \leqslant n \leqslant \mathrm{N} | \operatorname{dist} (p (n), \mathbf {Z}) <   \varepsilon \} \leqslant 3 \varepsilon | | f | | _ {\infty}\tag{8.4}
$$

for N large enough.

Thus, it suffices to show the a.s. convergence of (8.3) for a fixed $\varepsilon > 0$, assuming $f \in \mathbf{L}^2(\mu)$ (the hypothesis $f \in \mathbf{L}^\infty$ is only of relevance when replacing $\mathbf{A}_{\mathbf{N}}f$ by $\widetilde{\mathbf{A}}_{\mathbf{N}}f$).

The proof of this uses the same method as in section 6. The relevant exponential sums are given by

$$
\begin{array}{r l} \mathcal {F} [ \mathrm{K} _ {\mathrm{N}} ] (\alpha) & = \frac {1}{\mathrm{N}} \sum_ {n \leqslant \mathrm{N}} \sum_ {m \in \mathbf {Z}} \tau (p (n) - m) e ^ {- 2 \pi i m \alpha} \\ & = \sum_ {k \in \mathbf {Z}} \hat {\tau} (k - \alpha) \left\{\frac {1}{\mathrm{N}} \sum_ {n \leqslant \mathrm{N}} e ^ {2 \pi i (k - \alpha) p (n)} \right\}, \end{array}\tag{8.5}
$$

where

$$
\mathrm{K} _ {\mathrm{N}} = \frac {1}{\mathrm{N}} \sum_ {n \leqslant \mathrm{N}} \sum_ {m \in \mathbf {Z}} \tau (p (n) - m) \delta_ {\{m \}}.\tag{8.6}
$$

Let $\varphi_{\mathbf{N}}(\overline{\alpha})$ be given by (5.1)

$$
\varphi_ {N} (\overline {{\alpha}}) = \frac {1}{N} \sum_ {n = 1} ^ {N} e ^ {2 \pi i (\alpha_ {1} n + \alpha_ {2} n ^ {2} + \dots + \alpha_ {d} n ^ {d})}.
$$

Then

$$
\mathcal {F} [ \mathrm{K} _ {\mathrm{N}} ] (\alpha) = \sum_ {k \in \mathbb {Z}} \widehat {\tau} (k - \alpha) e ^ {2 \pi i (k - \alpha) b _ {0}} \varphi_ {\mathrm{N}} (b _ {1} (k - \alpha), \dots , b _ {d} (k - \alpha)).\tag{8.7}
$$

Observe also the decay property

$$
\mid \widehat {\tau} (\lambda) \mid <   \frac {\mathbf {C}}{1 + \varepsilon^ {2} \lambda^ {2}}.\tag{8.8}
$$

For $k\in \mathbf{Z}$ , define

$$
\mathcal {R} _ {s, k} = \left\{\theta \in [ 0, 1 ] \mid b _ {j} (k - \theta) \equiv \frac {a _ {j}}{q} (\mathrm{mod} 1) \right.\tag{8.9}
$$

$$
\text { where } (q, a _ {1}, \dots , a _ {d}) = 1 \text { and } 2 ^ {s} \leqslant q \leqslant 2 ^ {s + 1} \Bigg \}
$$

and for $\theta \in \mathcal{R}_{s,k}$, let, with the notation (5.10),

$$
\mathrm{S} (\theta) = \mathrm{S} (q, a _ {1}, \dots , a _ {d}).\tag{8.10}
$$

Define also, with the notation (5.11),

$$
w _ {\mathrm{N}} (\beta) = v _ {\mathrm{N}} (- b _ {1} \beta , \dots , - b _ {d} \beta).\tag{8.11}
$$

Set further

(8.12)

$$
\psi_ {s, k, \mathrm{N}} (\alpha) = \sum_ {\theta \in \mathcal {R} _ {s, k}} \mathrm{S} (\theta) w _ {\mathrm{N}} (\alpha - \theta) \zeta (1 0 ^ {s} b _ {d} (\alpha - \theta))\tag{8.13}
$$

$$
\psi_ {s, \mathrm{N}} (\alpha) = \sum_ {k \in \mathbf {Z}} \widehat {\tau} (k - \alpha) e ^ {2 \pi i (k - \alpha) b _ {0}} \psi_ {s, k, \mathrm{N}} (\alpha).
$$

Notice that different elements of  $R_{s,k}$  are at least  $4^{-s-1}b_{d}^{-1}$ -separated and the summands in (8.12) are thus supported by disjoint arcs in  $\Pi$  (not necessarily centered around rational points).

Using (8.8), one then has the analogue of (6.14)

$$
\mid \mathcal {F} [ \mathrm{K} _ {\mathrm{N}} ] - \sum_ {s \geqslant 0} \psi_ {s, \mathrm{N}} \mid <   \mathrm{C}. \mathrm{N} ^ {- \delta_ {1}}.\tag{8.14}
$$

We leave the verification to the reader.

Proceeding as in the proof of (6.28) in section 6, one gets

$$
\left| \left| \sup _ {\mathbf {N} \in \mathbf {Z} _ {1}} \right| \mathcal {F} ^ {- 1} \left[ \psi_ {s, k, \mathbf {N}} \mathcal {F} f \right] \right| | | _ {2} \leqslant \mathrm{C} (\log | \mathcal {R} _ {s, k} |) ^ {2} 2 ^ {- \delta^ {\prime} s} | | f | | _ {2} \sim \mathrm{Cs} ^ {2} 2 ^ {- \delta^ {\prime} s} | | f | | _ {2}.\tag{8.15}
$$

Hence, by (8.8)

$$
\begin{array}{r l} \left| \right| \sup _ {N \in Z _ {1}} | \mathcal {F} ^ {- 1} [ (\sum_ {s \geqslant 0} \psi_ {s, N}) \mathcal {F} f ] | | _ {2} \\ & \leqslant C \sum_ {s \geqslant 0} \sum_ {k \in Z} \frac {1}{1 + \varepsilon^ {2} k ^ {2}} s ^ {2} 2 ^ {- \delta^ {\prime} s} \| f \| _ {2} \leqslant C \| f \| _ {2} \end{array}
$$

yielding the maximal inequality

$$
\left| \right| \sup | \widetilde {\mathrm{A}} _ {\mathrm{N}} f | \left| \right| _ {2} \leqslant \mathrm{C} _ {\varepsilon} \left| \right| f \left| \right| _ {2}.\tag{8.16}
$$

With this information, the proof of a maximal variational inequality (6.31) is essentially identical to the argument given in section 6 and will therefore not be elaborated here.

This completes the proof of Theorem 2 (for $\mathbf{L}^{\infty}$-functions).

Remark. — The main additional item in proving the  $L^{r}$ -version, r>1, of the previous result for sets  $\Lambda=\{[p(n)]\}$  is a more detailed analysis of the approximation of  $A_{N}f$  by  $\widetilde{A}_{N}f$ , based on rational approximation of the coefficients  $b_{1},\ldots,b_{d}$  of  $p(x)$ .

## 9. Further Comments and Remarks on Almost Sure Convergence

(1) In  $[B_{3}]$ , the author considered the sequence  $\Lambda$  of prime numbers and proved that the averages

$$
\mathrm{A} _ {\mathbf {N}} f = \frac {1}{| \Lambda_ {\mathbf {N}} |} \sum_ {n \in \Lambda_ {\mathbf {N}}} \mathrm{T} ^ {n} f; \quad \Lambda_ {\mathbf {N}} = \{\text { primes } \leqslant \mathrm{N} \}\tag{9.1}
$$

converge a.s. for f a function of class  $L^{2}$ . Setting

$$
\mathrm{K} _ {\mathrm{N}} = \frac {1}{\mathrm{N}} \sum_ {\substack {\boldsymbol {p} \leqslant \mathrm{N} \\ \boldsymbol {p} \text {prime}}} (\log p) \delta_ {\{\boldsymbol {p} \}},\tag{9.2}
$$

it is well known that

$$
\mathcal {F} \left[ \mathrm{K} _ {\mathrm{N}} \right] (\alpha) = \frac {\mu (q)}{\varphi (q)} \frac {1}{\mathrm{N}} \left(\sum_ {k = 1} ^ {\mathrm{N}} e ^ {2 \pi i k \left(\alpha - \frac {a}{q}\right)}\right) + \mathrm{O} \left(e ^ {- c \sqrt {\log \mathrm{N}}}\right)\tag{9.3}
$$

for $|\alpha - (a / q)| < (\log \mathrm{N})^c \mathrm{~N}^{-1}$, $1 \leqslant a \leqslant q$, $(a, q) = 1$ and $q < (\log \mathrm{N})^c$. Here $\mu$ denotes the Moebius function and $\varphi(q)$ the number of Dirichlet characters to the modulus $q$.

Prior to this work, it has been shown in [W1] that  $A_{N}f$  given by (9.1) converges a.s. for a function of class  $L^{r}$, whenever r > 1. The argument is based on special properties of the expression in the right member of (9.3) and does not seem adaptable to the set of the squares for instance. The reader will easily check that the method described in section 7 of this paper applies equally well to the primes.

(2) Both Theorems 1 and 2 of this paper generalize to positive (not necessarily invertible) isometries on $\mathbf{L}^r$, $r > 1$. It was indeed pointed out in section 2 that this situation reduces also to the shift. Thus in particular, one has the following generalization of the Riesz-Raikov result (cf. [Ra], [Ri]), where $p(x) = x$:

Let $p(n)$ be a polynomial mapping positive integers to positive integers and $f$ a function on the circle $\Pi$ of class $L^r$, $r > 1$. Then $(1/N)\sum_{1\leqslant n\leqslant N}f(2^{p(n)}x)$ converges a.s. to $\int_{\Pi}f$. Recall in this context Marstrand's counterexample to the Khinchine conjecture [Ma], according to which there are bounded measurable functions $f$ on $\Pi$ such that $(1/N)\sum_{1\leqslant n\leqslant N}f(nx)$ does not converge a.s.

(3) Let  $T_{n}$  ( $n = 1, 2, \ldots$ ) be a sequence of commuting positive isometries on  $\mathbf{L}^{2}(\mu)$  and define  $A_{N}f = (1/N)\sum_{n\leqslant N}T_{n}f$ . It follows from the results of  $[B_{5}]$  that the following property is a necessary condition for a.s. convergence of  $A_{N}f$ ,  $N \to \infty$ , even restricting to functions  $f \in L^{\infty}(\mu)$ :

For each $\delta > 0$, there is a bound $C(\delta) < \infty$ on the $\delta$-metrical entropy number (in the sense of section 3)

$$
\mathrm{M} _ {\delta} (\{\mathrm{A} _ {\mathrm{N}} f | \mathrm{N} = 1, 2, \dots \}) <   \mathrm{C} (\delta)\tag{9.4}
$$

of the subset  $\{A_{N}f\}$  of  $\mathbf{L}^{2}(\mu)$ . This bound (9.4) has to be uniform when f ranges in the unit ball of  $\mathbf{L}^{2}(\mu)$ .

As pointed out through several applications (including Marstrand's example mentioned above) in  $[B_{5}]$ , the previous criterion if often effective in disproving the a.s. convergence of such averages.