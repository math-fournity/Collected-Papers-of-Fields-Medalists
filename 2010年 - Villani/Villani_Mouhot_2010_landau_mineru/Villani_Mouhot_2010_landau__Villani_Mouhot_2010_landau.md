# ALGEBRAIC FOURIER RECONSTRUCTION OF PIECEWISE SMOOTH FUNCTIONS

DMITRY BATENKOV AND YOSEF YOMDIN

ABSTRACT. Accurate reconstruction of piecewise-smooth functions from a finite number of Fourier coefficients is an important problem in various applications. This problem exhibits an inherent inaccuracy, in particular the Gibbs phenomenon, and it is being intensively investigated during the last decades. Several nonlinear reconstruction methods have been proposed in the literature, and it is by now well-established that the “classical” convergence order can be completely restored up to the discontinuities. Still, the maximal accuracy of determining the positions of these discontinuities remains an open question.

In this paper we prove that the locations of the jumps (and subsequently the pointwise values of the function) can be reconstructed with at least “half the classical accuracy”. In particular, we develop a constructive approximation procedure which, given the first k Fourier coefficients of a piecewise- $C^{2d+1}$ function, recovers the locations of the jumps with accuracy $\sim k^{-(d+2)}$, and the values of the function between the jumps with accuracy $\sim k^{-(d+1)}$ (similar estimates are obtained for the associated jump magnitudes). A key ingredient of the algorithm is to start with the case of a single discontinuity, where a modified version of one of the existing algebraic methods (due to K.Eckhoff) may be applied. It turns out that the additional orders of smoothness produce highly correlated error terms in the Fourier coefficients, which eventually cancel out in the corresponding algebraic equations. To handle more than one jump, we apply a localization procedure via a convolution in the Fourier domain, which eventually preserves the accuracy estimates obtained for the single jump. We provide some numerical results which support the theoretical predictions.

## 1. INTRODUCTION

Consider the problem of reconstructing a function $f:[-\pi ,\pi ]\to \mathbb{R}$ from a finite number of its Fourier coefficients

$$
c _ {k} (f) \stackrel {\mathrm{def}} {=} \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} f (t) \mathrm{e} ^ {- \imath k t} \mathrm{d} t, \quad k = 0, 1, \dots M
$$

It is well-known that for periodic smooth functions, the truncated Fourier series

$$
\mathfrak {F} _ {M} (f) \stackrel {\text {def}} {=} \sum_ {| k | = 0} ^ {M} c _ {k} (f) e ^ {\imath k x}
$$

converges to $f$ very fast, subsequently making Fourier analysis very attractive in a vast number of applications. We have by the classical Lebesgue lemma (see e.g. [30]) that

$$
\max _ {- \pi \leq x \leq \pi} | f (x) - \mathfrak {F} _ {M} (f) (x) | \leq (3 + \ln M) \cdot E _ {M} (f)
$$

where $E_{M}(f)$ is the error of the best uniform approximation to $f$ by trigonometric polynomials of degree at most $M$. This number, in turn, depends on the smoothness of the function. In particular:

(1) If $f$ is $d$-times continuously differentiable (including at the endpoints) and $\left|f^{(d)}(x)\right| \leq R$, then (see [39, Vol.I, Chapter 3, Theorem 13.6])

$$
E _ {M} (f) \leq C _ {d} \cdot R \cdot M ^ {- d}\tag{1.1}
$$

(2) If $f$ is analytic, then by classical results of S.Bernstein (see e.g. [30, Chapter IX]) there exist constants $C$ and $q < 1$ such that

$$
E _ {M} (f) \leq C \cdot q ^ {M}\tag{1.2}
$$

Yet many realistic phenomena exhibit discontinuities, in which case the unknown function f is only piecewise-smooth. As a result, the trigonometric polynomial  $\mathfrak{F}_{M}(f)$  no longer provides a good approximation to f due to the slow convergence of the Fourier series (one of the manifestations of this fact is commonly known as the “Gibbs phenomenon”). It has very serious implications, for example when using spectral methods to calculate solutions of PDEs with shocks. Therefore an important question arises: “Can such piecewise-smooth functions be reconstructed from their Fourier measurements, with accuracy which is comparable to the ‘classical’ one (such as (1.1) or (1.2))”?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Date: March 6, 2022.<br>2000 Mathematics Subject Classification. Primary: 65T40; Secondary: 65D15.<br>Key words and phrases. Fourier inversion, nonlinear approximation, piecewise-smooth functions.</span></small>

This problem has received much attention, especially in the last few decades ([23, 11, 9, 5, 20, 8, 29, 14, 15, 26, 3, 22, 13, 10, 4, 37] would be only a partial list). It has long been known that the key problem for Fourier series acceleration is the detection of the shock locations. By now it is well-established that classical convergence rates can be restored uniformly up to the discontinuities (see e.g. [22]), but the corresponding question for the jump locations themselves is still open. Notice that any linear approximation procedure with free (a-priori unknown) jump locations will not be able to achieve accuracy higher than $\frac{1}{\sqrt{M}}$ - see [17].

Several partial results and conjectures in this direction are known, in particular the following. The concentration method of Gelb&Tadmor [19, 20] recovers the jumps with first order accuracy, and it can be extended to higher orders. Kvernadze [26] proves that his method can recover jumps of a $C^3$ function with second order accuracy. In [17, 7] we have conjectured that the locations of the jumps of a piecewise $C^d$ function can be recovered with accuracy $k^{-d}$ from its first $k$ Fourier coefficients (a similar conjecture is made in [36]). Both Eckhoff [14] and Banerjee&Geer [3] made the same conjectures with respect to their particular reconstruction methods. We would also like to mention a related but different problem: reconstruction of piecewise-smooth functions from point measurements. There, adaptive approximations can achieve asymptotic accuracy $k^{-d}$ for piecewise $C^d$ functions [2, 31, 27].

With this motivation, our main goal in this paper is to arrive at a better understanding of the “optimal”, or the “best possible” accuracy of reconstruction, especially with respect to the locations and the magnitudes of the jumps. As a means to achieve this goal, we develop a reconstruction method which allows for explicit accuracy analysis. Our method is a “hybrid” between a Fourier filtering technique which is first applied to localize the jumps, and the algebraic approach of Eckhoff/Kvernadze which is used in order to resolve each discontinuity one at a time to a high order of accuracy. It is precisely this “localization” which makes the subsequent analysis tractable.

Our accuracy analysis is “asymptotic” in nature, although we provide the explicit constants at every step. These constants in general depend upon various a-priori estimates (such as the minimal distance between the jumps, or the upper bound on the jump magnitudes), which are presumably available. See discussion in Section 2 below, in particular (2.4).

Let us now give a brief summary of the main results.

(1) If a function with a single jump has at least $2d + 1$ continuous derivatives everywhere except the jump, then the jump location can be recovered from the first $M$ Fourier coefficients with error at most $\sim M^{-d - 2}$ (Theorem 4.13). In addition, a jump in the $l$-th derivative can be recovered with error at most $\sim M^{l - d - 1}$ (Theorem 4.21). A key observation in the analysis is that the additional orders of smoothness produce highly correlated error terms in the Fourier coefficients, which eventually cancel out in the corresponding algebraic equations.

(2) The localization step does not “destroy” the above accuracy estimates (Theorem 5.2). Thus, the pointwise values of f are recovered with the accuracy  $\sim M^{-d-1}$  (Theorem 6.1) up to the jumps.

(3) Numerical simulations are consistent with the theoretical accuracy predictions (Section 7).

By means of this constructive approximation procedure with provable asymptotic convergence properties, we therefore demonstrate that the algebraic reconstruction methods for piecewise-smooth data can be at least “half accurate” compared to the classical approximation theory for smooth data.

We provide an overview of the reconstruction procedure in Section 2. For expository reasons, the details of the localization step and the analysis of its accuracy are postponed until Section 5. The resolution method of a single jump is presented in Section 3, while Section 4 is devoted to proving its asymptotic convergence order. Finally, the accuracy of the whole reconstruction is analyzed in Section 6. Some common notations used throughout the paper are summarized below.

We would like to thank Ch.Fefferman, E.Tadmor and N.Zobin for useful discussions.

1.1. Notation.

\- $\mathbb{N}$ denotes the natural numbers, $\mathbb{R}$ - the real numbers, $\mathbb{C}$ - the complex numbers.

\- $C^d$ denotes the class of smooth functions which are continuously differentiable $d$ times everywhere. $C^\infty$ is the class of smooth functions having continuous derivatives of all orders.

\- $B_r(z)$ is the ball of radius $r$ centered at $z$, and $\partial B_r(z)$ is the boundary of such a ball.

![](images/page_2_chart_0.jpg)

FIGURE 2.1. A piecewise-smooth function

## 2. THE ALGEBRAIC RECONSTRUCTION METHOD

Let us assume that $f$ has $K \geq 0$ jump discontinuities $\{\xi_j\}_{j=1}^K$. Furthermore, we assume that $f \in C^d$ in every segment $(\xi_{j-1}, \xi_j)$, and we denote the associated jump magnitudes at $\xi_j$ by

$$
A _ {l, j} \stackrel {\mathrm{def}} {=} f ^ {(l)} (\xi_ {j} ^ {+}) - f ^ {(l)} (\xi_ {j} ^ {-})
$$

We write the piecewise smooth $f$ as the sum $f = \Psi + \Phi$, where $\Psi(x)$ is smooth and periodic and $\Phi(x)$ is a piecewise polynomial of degree $d$, uniquely determined by $\{\xi_j\}, \{A_{i,j}\}$ such that it "absorbs" all the discontinuities of $f$ and its first $d$ derivatives. This idea is very old and goes back at least to A.N.Krylov ([25, 4]). Eckhoff derives the following explicit representation for $\Phi(x)$:

$$
\begin{array}{c} \Phi (x) = \sum_ {j = 1} ^ {K} \sum_ {l = 0} ^ {d} A _ {l, j} V _ {l} (x; \xi_ {j}) \\ V _ {n} (x; \xi_ {j}) = - \frac {(2 \pi) ^ {n}}{(n + 1) !} B _ {n + 1} \left(\frac {x - \xi_ {j}}{2 \pi}\right) \quad \xi_ {j} \leq x \leq \xi_ {j} + 2 \pi \end{array}\tag{2.1}
$$

where $V_{n}(x; \xi_{j})$ is understood to be periodically extended to $[-\pi, \pi]$ and $B_{n}(x)$ is the $n$-th Bernoulli polynomial. For completeness, let us dervie the formula for the Fourier coefficients of $\Phi(x)$ (it can also be found in [14]).

Lemma 2.1. Let $\Phi(x)$ be a piecewise polynomial of degree $d$, with jump discontinuities $\{\xi_j\}_{j=1}^K$ and the associated jump magnitudes $\{A_{l,j}\}_{l=0,\ldots,d}^{j=1,\ldots,K}$. For definiteness, let us assume that $c_0(\Phi) = \int_{-\pi}^\pi \Phi(x) \, \mathrm{d}x = 0$. Then

$$
c _ {k} (\Phi) = \frac {1}{2 \pi} \sum_ {j = 1} ^ {K} \mathrm{e} ^ {- \imath k \xi_ {j}} \sum_ {l = 0} ^ {d} (\imath k) ^ {- l - 1} A _ {l, j}\tag{2.2}
$$

Proof. One integration by parts yields for  $k \neq 0$ :

$$
\begin{array}{l} c _ {k} (\Phi) = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {- \imath k x} \left(\sum_ {j = 0} ^ {K} \Phi_ {j} (x)\right) \mathrm{d} x \\ = \sum_ {j = 0} ^ {K} \left(\frac {\left(\Phi_ {j} \left(\xi_ {j + 1} ^ {-}\right) \mathrm{e} ^ {- \imath k \xi_ {j + 1}} - \Phi_ {j} \left(\xi_ {j} ^ {+}\right) \mathrm{e} ^ {- \imath k \xi_ {j}}\right)}{- 2 \pi \imath k} + \frac {1}{2 \pi \imath k} \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {- \imath k x} \Phi_ {j} ^ {\prime} (x) \mathrm{d} x\right) \\ = \frac {1}{2 \pi \imath k} \sum_ {j = 0} ^ {K} A _ {0, j} \mathrm{e} ^ {- \imath k \xi_ {j}} + \frac {1}{\imath k} c _ {k} \left(\sum_ {j = 0} ^ {K} \Phi_ {j} ^ {\prime}\right) \end{array}
$$

and so after $d + 1$-fold repetition we obtain (recall that $\Phi_j^{(d + 1)} \equiv 0$):

$$
c _ {k} (\Phi) = \frac {1}{2 \pi} \sum_ {l = 0} ^ {d} \sum_ {j = 0} ^ {K} (\imath k) ^ {- l - 1} A _ {l, j} \mathrm{e} ^ {- \imath k \xi_ {j}}
$$

A key observation is that if  $\Psi$  is sufficiently smooth, then the contribution of  $c_{k}(\Psi)$  to  $c_{k}(f)$  is negligible for large k. Therefore, for some large enough M one can build from the equations (2.2) an approximate system

$$
c _ {k} (f) \approx \frac {1}{2 \pi} \sum_ {j = 1} ^ {K} \omega_ {j} ^ {k} \sum_ {l = 0} ^ {d} \frac {A _ {l , j}}{(\imath k) ^ {l + 1}} \quad k = M, \dots , M + d + 1
$$

Here and in the rest of the paper we use the notation $\omega_{j} \stackrel{\mathrm{def}}{=} \mathrm{e}^{-\imath \xi_{j}}$.

In fact, this system (up to a change of variables and the number of equations) lies at the heart of the algebraic reconstruction methods of Eckhoff [14], Banerjee&Geer [3] and Kvernadze [26]. Banerjee&Geer solve it for all the parameters at once by least squares minimization. Eckhoff and Kvernadze eliminate all the $\{A_{i,j}\}$ first, resulting in a system of polynomial equations for the $\{\xi_j\}$, whose coefficients have nonlinear dependence on the initial data.

In contrast, we propose to solve this system separately for each  $\xi = \xi_{j}$ , because this case reduces to a single polynomial equation with respect to  $\xi$ . We achieve this “separation” by filtering the original Fourier coefficients such that only the part related to a particular  $\xi_{j}$  remains. This step requires some a-priori knowledge of the approximate locations of the jumps. Fortunately, such an information can easily be obtained by a variety of methods - see Section 5.

Let us finish this section by presenting the main steps of the reconstruction. We denote the approximately reconstructed parameters with a tilde sign. If not stated otherwise, it is understood that these approximations depend on the index M. It is important to note that we distinguish between the actual smoothness of the function f and the reconstruction order.

Algorithm 2.2. Let f be a piecewise-smooth function with jumps at  $\{\xi_{j}\}_{j=1}^{K}$ , continuously differentiable  $d_{1}$  times between the jumps. Fix a reconstruction order to be some nonnegative integer  $d \leq d_{1}$ . Let there be given the first  $M + d + 2$  Fourier coefficients of f.

(1) Solve the system (3.1) by localization (Algorithm 5.1) and resolution (Algorithm 3.2). This will provide us with approximate values for the parameters $\{\widetilde{\xi}_j\}$ and $\{\widetilde{A}_{l,j}\}$.

(2) Calculate the sequence

$$
c _ {k} (\widetilde {\Phi}) = \frac {1}{2 \pi} \sum_ {j = 1} ^ {K} \widetilde {\omega} _ {j} ^ {k} \sum_ {l = 0} ^ {d} \frac {\widetilde {A} _ {l , j}}{(\imath k) ^ {l + 1}} \quad | k | \leq M
$$

and subsequently recover the approximate Fourier coefficients of the smooth part:

$$
c _ {k} (\widetilde {\Psi}) \stackrel {d e f} {=} c _ {k} (f) - c _ {k} (\widetilde {\Phi}) \qquad | k | \leq M
$$

Take the final approximation to be

$$
\widetilde {f} = \widetilde {\Psi} + \widetilde {\Phi} = \sum_ {| k | \leq M} c _ {k} (\widetilde {\Psi}) e ^ {i k x} + \sum_ {j = 1} ^ {K} \sum_ {l = 0} ^ {d} \widetilde {A} _ {l, j} V _ {l} (x; \widetilde {\xi} _ {j})\tag{2.3}
$$

The rest of this paper is devoted to providing all the details of the above algorithm and analyzing its accuracy. In particular, we will seek estimates of the form

$$
\begin{array}{r l} \left| \widetilde {\xi} _ {j} - \xi_ {j} \right| & \leq C ^ {*} (d, d _ {1}, K) \cdot F _ {1} (\mathbb {A}, R, \mathbb {G}) \cdot M ^ {\alpha (d, d _ {1})} \\ \left| \widetilde {A} _ {l, j} - A _ {l, j} \right| & \leq C ^ {* *} (d, d _ {1}, K) \cdot F _ {2} (\mathbb {A}, R, \mathbb {G}) \cdot M ^ {\beta (l, d, d _ {1})} \\ \left| \widetilde {f} (x) - f (x) \right| & \leq C ^ {* * *} (d, d _ {1}, K) \cdot F _ {3} (\mathbb {A}, R, \mathbb {G}) \cdot M ^ {\gamma (d, d _ {1})} \end{array}\tag{2.4}
$$

where

\- $C^{*}, C^{**}, C^{***}$ are some absolute constants depending only on the "size" of the problem;

\- $\mathbb{G} = \mathbb{G}\left(\xi_1, \ldots, \xi_K\right)$ represents the geometry of the jump points (such as minimal distance between two adjacent jumps);

\- $\mathbb{A} = \mathbb{A}\left(|A_{0,1}|, \ldots, |A_{d_1,K}|\right)$ represents some a-priori bounds on the jump magnitudes, such as lower and upper bounds;

\- $R$ is an absolute bound for the Fourier coefficients of the smooth component $\Psi$:

$$
\left| c _ {k} (\Psi) \right| \leq R \cdot k ^ {- d - 2}\tag{2.5}
$$

\- $F_{1}, F_{2}, F_{3}$ and $\alpha, \beta, \gamma$ are some "simple" functions.

In the course of our investigation we shall be defining more specific bounds, but it will always be assumed that those can be expressed in terms of the above quantities.

Since we are interested in “asymptotic” estimates, we will in general allow the inequalities (2.4) to hold for all M starting from some index  $K^{*}$  which may be large and depend on the parameters of the problem. However, if a particular bound holds for all  $k > K^{*}$  then it will in general hold for  $k = 1, 2, \ldots, K^{*}$  as well, with some larger multiplicative constants  $\widetilde{C^{*}} \ldots$ , but which are harder to compute explicitly.

## 3. RESOLVING A SINGLE JUMP

Let $\omega \stackrel{\mathrm{def}}{=} \mathrm{e}^{-\imath \xi}$. The goal is to recover $\Phi$ from the approximate system of equations

$$
c _ {k} (f) \approx \frac {\omega^ {k}}{2 \pi} \sum_ {l = 0} ^ {d} \frac {A _ {l}}{(\imath k) ^ {l + 1}} (= c _ {k} (\Phi)) \quad k = M, \dots , M + d + 1\tag{3.1}
$$

To find $\omega$, we eliminate $\{A_0, \ldots, A_d\}$ from the equations. The result is a single polynomial equation having the exact value $\omega$ as one of its solutions. In Eckhoff's paper, this elimination is described in great detail, while here we present only the end result.

Let

$$
m _ {k} \stackrel {\text { def }} {=} 2 \pi (\imath k) ^ {d + 1} c _ {k} (\Phi) = \omega^ {k} \sum_ {l = 0} ^ {d} (\imath k) ^ {d - l} A _ {l}
$$

$$
p _ {k} ^ {d} (z) \stackrel {\mathrm{def}} {=} \sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} m _ {k + j} z ^ {d + 1 - j}\tag{3.2}
$$

Lemma 3.1. The point $\omega$ satisfies:

$$
p _ {k} ^ {d} (\omega) = 0 \qquad \forall k \in \mathbb {N}
$$

Proof. The proof is an immediate consequence of Lemma A.4 (see Appendix A).

Since the exact coefficients $m_{k}$ (and as a result the polynomials $p_k^d(z)$) are unknown, we approximate these with the known quantities

$$
\begin{array}{c} r _ {k} \stackrel {{\text {def}}} {{=}} 2 \pi (\imath k) ^ {d + 1} c _ {k} (f) \\ q _ {k} ^ {d} (z) \stackrel {{\text {def}}} {{=}} \sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} r _ {k + j} z ^ {d + 1 - j} \end{array}\tag{3.3}
$$

Now we are ready to formulate the procedure of recovering the parameters of a single jump.

Algorithm 3.2. Let us be given the first $M + d + 2$ Fourier coefficients of the function $f$ which has a single jump $\xi \in [-\pi, \pi]$.

(1) Solve the polynomial equation

$$
q _ {M} ^ {d} (z) = 0
$$

and take $\widetilde{\omega}$ to be the root which is closest to the unit circle. In Section 4 below, we shall provide the justification for this choice.

(2) The jump magnitudes $A_0, \ldots, A_d$ are reconstructed as follows. By (3.2), the exact values of $A_j$ satisfy

$$
m _ {k} \omega^ {- k} = \sum_ {l = 0} ^ {d} (\imath k) ^ {d - l} A _ {l} \quad \forall k \in \mathbb {N}\tag{3.4}
$$

We use the approximations $r_k \approx m_k$, $\widetilde{\omega} \approx \omega$ and solve the system of linear equations

$$
r _ {k} \widetilde {\omega} ^ {- k} = \sum_ {l = 0} ^ {d} (\imath k) ^ {d - l} \widetilde {A} _ {l} \quad k = M, \dots , M + d\tag{3.5}
$$

with respect to the unknowns $\left\{\widetilde{A}_l\right\}$ by any one of the standard methods.

## 4. ACCURACY ANALYSIS: A SINGLE JUMP

Our goal in this section is to analyze Algorithm 3.2 and calculate its accuracy. We shall express all our estimates in terms of the index k, keeping in mind that it should be replaced with M to be consistent with the definitions of the previous sections.

4.1. Accuracy analysis: jump location. We start with the determination of the jump point  $\widetilde{\omega}$ . Our strategy will be to investigate the polynomial  $q_{k}^{d}(z)$ , and determine the bounds on locations of its roots. We can informally summarize the main results as follows:

(1) Starting from some $k$, the roots of $q_{k}^{d}(z)$ are "separated" from each other by at least $\sim k^{-1}$.

(2) If the function $f$ is continuously differentiable at least $d_1 \geq 2d + 1$ times everywhere except at $\xi$, then one of those roots deviates from the "true" value $\omega$ by at most $\sim k^{-d - 2}$.

We regard  $q_{k}^{d}(z)$  as a perturbation of  $p_{k}^{d}(z)$ . With this point of view, we shall first describe the roots of  $p_{k}^{d}(z)$ , and then calculate the “deviations” due to the difference

$$
e _ {k} ^ {d} (z) = q _ {k} ^ {d} (z) - p _ {k} ^ {d} (z)
$$

In the subsequent analysis we denote the roots of $p_k^d (z)$ by $z_i^{(k,d)}$ for $i = 0,1,\dots ,d$, with the convention that $z_0^{(k,d)} = \omega$. Also, we denote the roots of $q_k^d (z)$ by $\kappa_i^{(k,d)}$.

It will be convenient to study $p_k^d(z)$ in a different coordinate system. For this purpose, consider the following transformation of the punctured $z$-plane:

$$
u = \mathcal {T} (z) = \frac {\omega}{z} - 1 \qquad z \neq 0
$$

Then the inverse map is given by

$$
z = \mathcal {T} ^ {- 1} (u) = \frac {\omega}{u + 1} \quad u \neq - 1\tag{4.1}
$$

Now we translate the problem into the u-plane.

Definition 4.1. For all $k, d \in \mathbb{N}$ let

$$
s _ {k} ^ {d} (u) \stackrel {\mathrm{def}} {=} \frac {p _ {k} ^ {d} (z)}{\omega^ {k} z ^ {d + 1}} = \frac {(u + 1) ^ {d + 1}}{\omega^ {k + d + 1}} p _ {k} ^ {d} \left(\frac {\omega}{u + 1}\right)\tag{4.2}
$$

Claim 4.2. $s_k^d (u)$ is a polynomial function. Furthermore, if $u_0 \neq -1$ is a root of $s_k^d (u)$, then $z_0 = \mathcal{T}^{-1}(u_0)$ is a root of $p_k^d (u)$.

Therefore it makes sense to study the roots of $s_k^d (u)$. We denote these roots by $\sigma_i^{(k,d)}, i = 0,\dots ,d$. The observation below is an immediate consequence of Lemma 3.1.

Claim 4.3. $s_k^d (0) = 0$

Therefore we will always take $\sigma_0^{(k,d)} = 0$.

In what follows, we shall break $s_k^d(u)$ into a sum of terms and subsequently apply a perturbation analysis to determine its roots. We begin with some simplifications:

$$
\begin{array}{l} s _ {k} ^ {d} (u) = \frac {(u + 1) ^ {d + 1}}{\omega^ {k + d + 1}} \sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} \underbrace {\left\{\omega^ {k + j} \sum_ {l = 0} ^ {d} (\imath (k + j)) ^ {d - l} A _ {l} \right\}} _ {= m _ {k + j}} \frac {\omega^ {d + 1 - j}}{(u + 1) ^ {d + 1 - j}} \\ = \sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} (u + 1) ^ {j} \sum_ {l = 0} ^ {d} (\imath (k + j)) ^ {d - l} A _ {l} = \sum_ {l = 0} ^ {d} \imath^ {d - l} A _ {l} \sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} (u + 1) ^ {j} (k + j) ^ {d - l}. \end{array}
$$

Now substitute the binomial expansions

$$
(k + j) ^ {d - l} = \sum_ {m = 0} ^ {d - l} k ^ {m} j ^ {d - l - m} {\binom {d - l} {m}}
$$

$$
(u + 1) ^ {j} = \sum_ {s = 0} ^ {j} u ^ {s} \binom {j} {s}
$$

and get

$$
s _ {k} ^ {d} (u) = \sum_ {l = 0} ^ {d} \imath^ {d - l} A _ {l} \sum_ {m = 0} ^ {d - l} k ^ {m} \sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} \sum_ {s = 0} ^ {j} u ^ {s} \binom {j} {s} j ^ {d - l - m} \binom {d - l} {m}
$$

Now we make a change in indexing according to the following scheme:

$$
\sum_ {j = 0} ^ {d + 1} \sum_ {s} ^ {j} = \sum_ {s = 0} ^ {d + 1} \sum_ {j = s} ^ {d + 1} \quad \sum_ {l = 0} ^ {d} \sum_ {m = 0} ^ {d - 1} = \sum_ {m = 0} ^ {d} \sum_ {l = 0} ^ {d - m}
$$

and continue:

$$
s _ {k} ^ {d} (u) = \sum_ {s = 0} ^ {d + 1} u ^ {s} \sum_ {m = 0} ^ {d} k ^ {m} \sum_ {l = 0} ^ {d - m} \binom {d - l} {m} \imath^ {d - l} A _ {l} \sum_ {j = s} ^ {d + 1} (- 1) ^ {j} \binom {j} {s} \binom {d + 1} {j} j ^ {d - l - m}
$$

Definition 4.4. For all integers $t, s$ with $0 \leq t \leq d$ and $0 \leq s \leq d + 1$ let

$$
\mathcal {F} (d, t, s) \stackrel {{\text { def }}} {{=}} \sum_ {j = s} ^ {d + 1} (- 1) ^ {j} \binom {j} {s} \binom {d + 1} {j} j ^ {d - t}
$$

With this definition, we can write

$$
s _ {k} ^ {d} (u) = \sum_ {s = 0} ^ {d + 1} u ^ {s} \sum_ {m = 0} ^ {d} k ^ {m} \sum_ {l = 0} ^ {d - m} \binom {d - l} {m} \imath^ {d - l} A _ {l} \cdot \mathcal {F} (d, m + l, s)
$$

We will need a technical result.

Lemma (A.5). For all $0 \leq s \leq d + 1$

(1) If $m + l \geq s$ then $\mathcal{F}(d, m + l, s) = 0$

$$
(2) \mathcal {F} (d, s - 1, s) = (- 1) ^ {d + 1} (d + 1 - s)! \binom {d + 1} {s} \tag {2}
$$

## Proof. See Appendix A.

The polynomial  $s_{k}^{d}(u)$  must therefore be of the form

$$
s _ {k} ^ {d} (u) = \sum_ {s = 1} ^ {d + 1} \left(a _ {0, s} + a _ {1, s} k + \dots + a _ {s - 1, s} k ^ {s - 1}\right) u ^ {s}
$$

where in particular

$$
a _ {s - 1, s} = \binom {d} {s - 1} \imath^ {d} A _ {0} (- 1) ^ {d + 1} (d + 1 - s)! \binom {d + 1} {s}\tag{4.3}
$$

We break up the polynomial $s_k^d(u)$ into a "dominant" and a "perturbation" part: $s_k^d(u) = s_k^d(u) + h_k^d(u)$ where

$$
\begin{array}{l} \widetilde {s _ {k} ^ {d}} (u) \stackrel {{\text {def}}} {{=}} \sum_ {s = 1} ^ {d + 1} a _ {s - 1, s} k ^ {s - 1} u ^ {s} \\ h _ {k} ^ {d} (u) \stackrel {{\text {def}}} {{=}} \sum_ {s = 2} ^ {d + 1} \left(a _ {0, s} + a _ {1, s} k + \dots + a _ {s - 2, s} k ^ {s - 2}\right) u ^ {s} \end{array}\tag{4.4}
$$

Next we shall see that the dominant component  $s_{k}^{d}(u)$  determines the locations of the roots of  $s_{k}^{d}(u)$  up to the first order accuracy, while the other component  $h_{k}^{d}(u)$  is responsible for second-order perturbations of these roots.

We denote the roots of $\widetilde{s}_k^d (u)$ by $\widetilde{\sigma}_i^{(k,d)}, i = 0,\dots ,d$ with $\widetilde{\sigma}_0^{(k,d)} = 0$.

It turns out that $\widetilde{s}_k^d (u)$ can be completely characterized.

Definition 4.5. For every $\alpha > -1$ and $n = 0,1,2,\ldots$ let $\mathcal{L}_n^{(\alpha)}(x)$ denote the generalized Laguerre polynomial ([1, Chapter 22], [34, Chapter 5.2]):

$$
\mathcal {L} _ {n} ^ {(\alpha)} (x) = \sum_ {m = 0} ^ {n} {\binom {n + \alpha} {n - m}} \frac {(- x) ^ {m}}{m !}
$$

Lemma 4.6. With the above notations:

(1) The polynomial $\widetilde{s}_k^d (u)$ satisfies

$$
\widetilde {s _ {k} ^ {d}} (u) = \frac {1}{k} \widetilde {s _ {1} ^ {d}} (k u)\tag{4.5}
$$

(2) Furthermore,

$$
\widetilde {s} _ {1} ^ {d} (u) = - (- \imath) ^ {d} A _ {0} (d + 1)! \mathcal {L} _ {d + 1} ^ {(- 1)} (- u)
$$

Proof. The first part follows from (4.4):

$$
k \cdot \widetilde {s} _ {k} ^ {d} (u) = k \cdot \sum_ {s = 1} ^ {d + 1} a _ {s - 1, s} k ^ {s - 1} u ^ {s} = \sum_ {s = 1} ^ {d + 1} a _ {s - 1, s} (k u) ^ {s} = \widetilde {s} _ {1} ^ {d} (k u)
$$

To prove the second part, we substitute the expression (4.3) into (4.4):

$$
\begin{array}{l} \widetilde {s _ {1} ^ {d}} (u) = \sum_ {s = 1} ^ {d + 1} a _ {s - 1, s} u ^ {s} = \sum_ {s = 1} ^ {d + 1} \binom {d} {s - 1} \imath^ {d} A _ {0} (- 1) ^ {d + 1} (d + 1 - s)! \binom {d + 1} {s} u ^ {s} \\ = - (- \imath) ^ {d} A _ {0} (d + 1)! \sum_ {s = 1} ^ {d + 1} \binom {d} {d + 1 - s} \frac {u ^ {s}}{s !} = - (- \imath) ^ {d} A _ {0} (d + 1)! \mathcal {L} _ {d + 1} ^ {(- 1)} (- u) \end{array}
$$

Corollary 4.7. For all $k \in \mathbb{N}$, $\widetilde{s_k^d}(u^*) = 0$ if and only if $\mathcal{L}_{d+1}^{(-1)}(-ku^*) = 0$.

Lemma 4.8. The numbers $\left\{\widetilde{\sigma}_i^{(k,d)}\right\}$ satisfy the following properties:

(1) each $\widetilde{\sigma}_i^{(k,d)}$ is a simple root of $\widetilde{s}_k^d (u)$;

(2) $\widetilde{\sigma}_i^{(k,d)} < 0$ for $i = 1,2,\ldots ,d;$

(3) there exist constants $C_1, C_2$ such that for every $k \in \mathbb{N}$ and $0 \leq i < j \leq d$

$$
C _ {1} k ^ {- 1} \leq \left| \widetilde {\sigma} _ {i} ^ {(k, d)} - \widetilde {\sigma} _ {j} ^ {(k, d)} \right| \leq C _ {2} k ^ {- 1}\tag{4.6}
$$

Proof. Following Corollary 4.7, we only need to characterize the roots of $\mathcal{L}_{d+1}^{(-1)}(-u)$. By [34, Chapter 5.2], for every integer $m \geq 1$

$$
\mathcal {L} _ {n} ^ {(- m)} (x) = (- x) ^ {m} \frac {(n - m) !}{n !} \mathcal {L} _ {n - k} ^ {(m)} (x)
$$

and therefore

$$
\mathcal {L} _ {d + 1} ^ {(- 1)} (- u) = u \frac {d !}{(d + 1) !} \mathcal {L} _ {d} ^ {(1)} (- u)
$$

The polynomials $\left\{\mathcal{L}_n^{(1)}(x)\right\}_{n=0}^{\infty}$ form an orthogonal system on the interval $(0,\infty)$ (see again [1, Chapter 22], [34, Chapter 5.2]). Parts (1) and (2) follow immediately. Part (3) follows by taking $C_1$ and $C_2$ to be the minimal and the maximal distance between the roots of $\mathcal{L}_d^{(1)}(u)$, correspondingly.

Now we show that $h_k^d (u)$ perturbes the zeros of $\widetilde{s}_k^d (u)$ by at most $\sim k^{-2}$. Since the coefficients $h_k^d (u)$ depend linearly on $A_0\ldots ,A_d$, we can expect that the bound will depend on the quantity $\sum_{l = 0}^{d}|A_l|$. For convenience, let us therefore define

$$
A ^ {*} \stackrel {{\text { def }}} {{=}} \max \left(1, \sum_ {l = 0} ^ {d} | A _ {l} |\right)
$$

Lemma 4.9. There exist constants $C_3, K_1$ such that for all $k > K_1 A^*$ and for all $i = 0, \ldots, d$

$$
\left| \widetilde {\sigma} _ {i} ^ {(k, d)} - \sigma_ {i} ^ {(k, d)} \right| \leq C _ {3} A ^ {*} k ^ {- 2}\tag{4.7}
$$

Proof. Our method of proof is based on Rouche's theorem (Theorem B.1). We shall define a sequence $\rho(k) = C_3 A^* k^{-2}$ (where $C_3$ is to be determined) and consider disks of radius $\rho(k)$ around each one of the roots $\widetilde{\sigma}_i^{(k,d)}$. Our goal is to find $C_3$ so that $\left|\widetilde{s}_k^d(u_\theta)\right| > \left|h_k^d(u_\theta)\right|$ for all points $u_\theta = \widetilde{\sigma}_i^{(k,d)} + \rho(k)\mathrm{e}^{\imath \theta}$ on the boundaries of these disks.

\- In order to bound $\left| s_k^d(u_\theta) \right|$ from below, we shall use Lemma B.2. We need to bound from below the first derivative at $\widetilde{\sigma}_i^{(k,d)}$, as well as to bound from above the second derivative in the disk $B_{k-1}(\widetilde{\sigma}_i^{(k,d)})$.

(1) We always have

$$
\left. \frac {\mathrm{d}}{\mathrm{d} u} \widetilde {s _ {k} ^ {d}} (u) \right| _ {u = \widetilde {\sigma} _ {i} ^ {(k, d)}} = \left. \frac {\mathrm{d}}{\mathrm{d} u} \left(\frac {1}{k} \widetilde {s _ {1} ^ {d}} (k u)\right) \right| _ {u = \widetilde {\sigma} _ {i} ^ {(k, d)}} = \left. \frac {\mathrm{d} \widetilde {s _ {1} ^ {d}} (w)}{\mathrm{d} w} \right| _ {w = k \widetilde {\sigma} _ {i} ^ {(k, d)}}
$$

Now $k\widetilde{\sigma}_i^{(k,d)}$ is always a root of $\widetilde{s}_1^d (u)$, therefore the value of $\frac{\mathrm{d}}{\mathrm{d}u}\widetilde{s}_k^d (u)\bigg|_{u = \widetilde{\sigma}_i^{(k,d)}}$ is independent of $k$ and thus we can write

$$
\left| \frac {\mathrm{d}}{\mathrm{d} u} \widetilde {s _ {k} ^ {d}} (u) \right| _ {u = \widetilde {\sigma} _ {i} ^ {(k, d)}} \geq C _ {4} \stackrel {{\text {def}}} {{=}} \min _ {i} \left| \frac {\mathrm{d}}{\mathrm{d} u} \widetilde {s _ {1} ^ {d}} (u) \right| _ {u = \widetilde {\sigma} _ {i} ^ {(1, d)}}
$$

Since all the roots are simple, this is guaranteed to be a strictly positive bound.

(2) Now consider a point $u^{*} \in B_{k - 1}\left(\widetilde{\sigma}_{i}^{(k,d)}\right)$. Then $\left|ku^{*} - k\widetilde{\sigma}_{i}^{(k,d)}\right| \leq 1$ and therefore $ku^{*} \in B_{1}\left(\widetilde{\sigma}_{i}^{(1,d)}\right)$. Using (4.5) and differentiating twice, we get

$$
\left. \frac {\mathrm{d} ^ {2}}{\mathrm{d} u ^ {2}} \widetilde {s} _ {k} ^ {d} (u) \right| _ {u = u ^ {*}} = k \left. \frac {\mathrm{d} ^ {2}}{\mathrm{d} w ^ {2}} \widetilde {s} _ {1} ^ {d} (w) \right| _ {w = k u ^ {*}}
$$

Let

$$
C _ {5} \stackrel {\text {def}} {=} \max _ {i} \max _ {w ^ {*} \in B _ {1} \left(\widetilde {\sigma} _ {i} ^ {(1, d)}\right)} \left| \frac {\mathrm{d} ^ {2}}{\mathrm{d} w ^ {2}} \widetilde {s} _ {1} ^ {d} (w) \right| _ {w = w ^ {*}}
$$

(3) The constants $C_4$ and $C_5$ therefore satisfy the assumptions of Lemma B.2. We define $C_6 \stackrel{\mathrm{def}}{=} \min \left(1, \frac{C_4}{C_5}\right)$. The conclusion is that there exists a constant $C_7$ such that for every function $\eta(k): \mathbb{N} \to \mathbb{R}$ satisfying $0 < \eta(k) < \frac{C_6}{k}$ we have

$$
\left| \widetilde {s} _ {k} ^ {d} \left(\widetilde {\sigma} _ {i} ^ {(k, d)} + \eta (k) e ^ {\imath \theta}\right) \right| > C _ {7} \eta (k)
$$

\- Now we shall bound $\left|h_k^d(u_\theta)\right|$ from above. Recall that

$$
h _ {k} ^ {d} (u) = \sum_ {s = 2} ^ {d + 1} \left(a _ {0, s} + a _ {1, s} k + \dots + a _ {s - 2, s} k ^ {s - 2}\right) u ^ {s}
$$

where $a_{i,j}$ are some linear functions of $A_0, \ldots, A_d$. Let $\zeta(k): \mathbb{N} \to \mathbb{R}$ be any function satisfying $0 < \zeta(k) < \frac{1}{k}$, and consider $u_\theta = \widetilde{\sigma}_i^{(k,d)} + \zeta(k)\mathrm{e}^{\imath\theta}$. By Lemma 4.8, $\left|\widetilde{\sigma}_i^{(k,d)}\right| < C_2k^{-1}$ and therefore $|u_\theta| < 2 \cdot \max(1, C_2)k^{-1}$. But then

$$
\left| h _ {k} ^ {d} (u _ {\theta}) \right| \leq | a _ {0, 2} | | u _ {\theta} | ^ {2} + \left(| a _ {0, 3} | + | a _ {1, 3} | k\right) | u _ {\theta} | ^ {3} + \dots + \left(| a _ {0, d + 1} | + \dots + | a _ {d - 1, d + 1} | k ^ {d - 1}\right) | u _ {\theta} | ^ {d + 1} \leq C _ {8} A ^ {*} k ^ {- 2}
$$

for some constant $C_8$.

We set

$$
C _ {3} \stackrel {\mathrm{def}} {=} \frac {2 C _ {8}}{C _ {7}}
$$

and let $\rho(k) = C_3 A^* k^{-2}$. We need the inequality $\rho(k) < \frac{C_6}{k}$ to be satisfied, and this is obviously possible if

$$
k > \underbrace {\frac {2 C _ {8}}{C _ {7} C _ {6}}} _ {\stackrel {\mathrm{def}} {=} K _ {1}} A ^ {*}
$$

In this case we have shown that

$$
\left| \widetilde {s} _ {k} ^ {d} \left(\widetilde {\sigma} _ {i} ^ {(k, d)} + \rho (k) e ^ {i \theta}\right) \right| > C _ {7} \rho (k) = 2 C _ {8} A ^ {*} k ^ {- 2}
$$

and also

$$
\left| h _ {k} ^ {d} \left(\widetilde {\sigma} _ {i} ^ {(k, d)} + \rho (k) \mathsf {e} ^ {\imath \theta}\right) \right| \leq C _ {8} A ^ {*} k ^ {- 2}
$$

Therefore

$$
\left| \widetilde {s} _ {k} ^ {d} \left(\widetilde {\sigma} _ {i} ^ {(k, d)} + \rho (k) \mathsf {e} ^ {\imath \theta}\right) \right| > \left| h _ {k} ^ {d} \left(\widetilde {\sigma} _ {i} ^ {(k, d)} + \rho (k) \mathsf {e} ^ {\imath \theta}\right) \right|
$$

which completes the proof.

Remark 4.10. We have in fact shown that for each $k > K_{1}$ the polynomial $s_k^d (u)$ has precisely $d + 1$ distinct roots.

Now we can go back to the original polynomial  $p_{k}^{d}(z)$  and accurately describe the location of its roots  $\left\{ z_{i}^{(k,d)} \right\}$ . Recall from Claim 4.2 that  $z_{i}^{(k,d)} = \mathcal{T}^{-1} \left( \sigma_{i}^{(k,d)} \right)$ . Being careful to avoid the singularity  $\sigma_{i}^{(k,d)} = -1$  (by choosing large enough k), we now show that the geometry of the roots  $\sigma_{i}^{(k,d)}$  is preserved under  $T^{-1}$ . In particular, the numbers  $z_{i}^{(k,d)}$  remain separated from each other (following (4.6)), each of them being close (following Lemma 4.9) to one of the numbers

$$
y _ {i} ^ {(k, d)} \stackrel {\text { def }} {=} \mathcal {T} ^ {- 1} \left(\widetilde {\sigma} _ {i} ^ {(k, d)}\right) = \frac {\omega}{\widetilde {\sigma} _ {i} ^ {(k , d)} + 1}\tag{4.8}
$$

The only thing which is different are the constants.

Lemma 4.11. Let $y_{i}^{(k,d)}$ be defined by (4.8). Then

(1) there exist constants $C_9, C_{10}, K_2$ such that for all $k > K_2$ and $0 \leq i < j \leq d$

$$
C _ {9} k ^ {- 1} \leq \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right| \leq C _ {1 0} k ^ {- 1}
$$

(2) there exist constants $C_{11}, K_3$ such that for all $k > K_3A^*$

$$
\left| z _ {i} ^ {(k, d)} - y _ {i} ^ {(k, d)} \right| <   C _ {1 1} A ^ {*} \cdot k ^ {- 2}
$$

(3) there exist constants $C_{12}, C_{13}, K_4$ such that for all $k > K_4A^*$ and $0 \leq i < j \leq d$

$$
C _ {1 2} k ^ {- 1} \leq \left| z _ {i} ^ {(k, d)} - z _ {j} ^ {(k, d)} \right| \leq C _ {1 3} k ^ {- 1}
$$

Proof. If $k > 2C_2$ then $\left|\widetilde{\sigma}_i^{(k,d)}\right| < \frac{1}{2}$ (see (4.6)). It follows that $\frac{1}{2} < \left|\widetilde{\sigma}_i^{(k,d)} + 1\right| \leq 1$ and so by (4.8)

$$
C _ {1} k ^ {- 1} <   \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right| <   4 C _ {2} k ^ {- 1}
$$

This proves (1) with $C_9 = C_1$, $C_{10} = 4C_2$ and $K_2 = 2C_2$.

If in addition $k > \frac{2C_3}{C_1}$ then $\left|\widetilde{\sigma}_i^{(k,d)} - \sigma_i^{(k,d)}\right| < \frac{\left|\widetilde{\sigma}_i^{(k,d)}\right|}{2} < \frac{1}{4}$ and therefore $\left|\sigma_i^{(k,d)} + 1\right| > \frac{1}{4}$. It follows from (4.7) that

$$
\left|z_{i}^{(k,d)} - y_{i}^{(k,d)}\right| = \frac{\left|\widetilde{\sigma}_{i}^{(k,d)} - \sigma_{i}^{(k,d)}\right|}{\left|\widetilde{\sigma}_{i}^{(k,d)} + 1\right|\left|\sigma_{i}^{(k,d)} + 1\right|} <  4C_{3}k^{-2}\qquad k > \underbrace{\max \left(2C_{2},\frac{2C_{3}}{C_{1}},K_{1}\right)}_{\substack{\stackrel {\text{def}}{=} K_{3}}}A^{*}
$$

and this proves (2) with $C_{11} = 4C_3$ and $K_3$ as above.

Let $k > \underbrace{\max\left(K_2, K_3, \frac{4C_{11}}{C_9}\right)} A^*$. Using (1) and (2), we have one one hand

$$
\begin{array}{r l} \left| z _ {i} ^ {(k, d)} - z _ {j} ^ {(k, d)} \right| <   & \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right| + \left| z _ {i} ^ {(k, d)} - y _ {i} ^ {(k, d)} \right| + \left| y _ {j} ^ {(k, d)} - z _ {j} ^ {(k, d)} \right| \\ <   & \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right| + \frac {C _ {1 1}}{k ^ {2}} + \frac {C _ {1 1}}{k ^ {2}} \\ <   & \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right| + 2 \cdot \frac {C _ {9}}{4 k} <   \frac {3}{2} \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right| <   \underbrace {\frac {3}{2} C _ {1 0}} _ {\stackrel {\text {def}} {=} C _ {1 3}} k ^ {- 1} \end{array}
$$

and on the other hand

$$
\left|z_{i}^{(k,d)} - z_{j}^{(k,d)}\right| > \left|y_{i}^{(k,d)} - y_{j}^{(k,d)}\right| - \left|y_{j}^{(k,d)} - z_{j}^{(k,d)}\right| - \left|y_{j}^{(k,d)} - z_{j}^{(k,d)}\right| > \frac{1}{2}\left|y_{i}^{(k,d)} - y_{j}^{(k,d)}\right| > \\ \underbrace{\frac{1}{2}C_{9}}_{\substack{\text{def}\\ \equiv C_{12}}}k^{-1}
$$

That proves (3).

Remaining in the $z$-plane, we now turn to investigate $q_{k}^{d}(z)$ and its roots $\left\{\kappa_{i}^{(k,d)}\right\}$. Recall that we consider $q_{k}^{d}(z)$ to be a "perturbation" of $p_{k}^{d}(z)$ by another polynomial $e_k^d (z)$, i.e.

$$
q _ {k} ^ {d} (z) = p _ {k} ^ {d} (z) + e _ {k} ^ {d} (z)
$$

The coefficients of  $e_{k}^{d}(z)$  depend on the Fourier coefficients of the “smooth part” of our piecewise-smooth function f. It turns out that in the general setting, the coefficients of  $e_{k}^{d}(z)$  are large compared to those of  $p_{k}^{d}(z)$  and therefore the perturbations of the roots are large too. If, however, there is enough structure in those coefficients due to additional orders of smoothness, then the perturbation of the roots is small. This is the essence of the key Lemma 4.12 below.

Recall that $f$ has in fact $d_1 \geq d$ continuous derivatives everywhere in $[-\pi, \pi] \setminus \{\xi\}$, and denote the additional jump magnitudes at $\xi$ by $A_{d+1}, \ldots, A_{d_1}$. For every $l \leq d_1$, let $\Phi_l$ denote the piecewise polynomial of degree $l$ with jump point $\xi$ and jump magnitudes $A_0, \ldots, A_l$. Then we write

$$
f = \Phi_ {d} + (\Phi_ {d _ {1}} - \Phi_ {d}) + \Psi^ {*}\tag{4.9}
$$

where $\Psi^{*}$ is $d_{1}$-times smooth everywhere in $[- \pi, \pi]$. Thus there exists a constant $R^{*}$ such that

$$
\left| c _ {k} \left(\Psi^ {*}\right) \right| \leq R ^ {*} k ^ {- d _ {1} - 2}\tag{4.10}
$$

Let us also denote

$$
A ^ {* *} \stackrel {{\text { def }}} {{=}} \max \left(1, \sum_ {l = d + 1} ^ {d _ {1}} | A _ {l} |\right)
$$

$$
H \stackrel {\text { def }} {=} (A ^ {*} + A ^ {* *} + R ^ {*})
$$

Lemma 4.12. Let $d_1 \geq 2d + 1$. Then there exist constants $C_{14}, C_{15}, K_5$ such that for all $k > K_5H$

$$
\left| \kappa_ {i} ^ {(k, d)} - z _ {i} ^ {(k, d)} \right| \leq \left\{ \begin{array}{l l} C _ {1 4} \cdot H \cdot k ^ {- 2} & i = 1, 2, \dots , d \\ C _ {1 5} \cdot H \cdot k ^ {- d - 2} & i = 0 \end{array} \right.
$$

Proof. The idea of the proof is the same as in Lemma 4.9. Namely, we shall seek the constants $C_{14}, C_{15}$ and $K_5$ such that if $\rho_1(k) = C_{14} \cdot H \cdot k^{-2}$ and $\rho_2(k) = C_{15} \cdot H \cdot k^{-d-2}$ then for $i = 0, 1, \ldots, d$ and $k > K_5H$ there exist neighborhoods $D_i^{(k)}$ of $z_i^{(k,d)}$ such that $|p_k^d(z)| > |e_k^d(z)|$ on the boundary of $D_i^{(k)}$ and

\- $\operatorname{diam} D_i^{(k)} = \rho_1(k)$ for $i = 1,2,\ldots,d$;

\- $\operatorname{diam} D_0^{(k)} = \rho_2(k)$.

(1) In order to show that $\left|p_k^d (z)\right|$ is large in some neighborhood of $z_{i}^{(k,d)}$, let us first show that $\left|s_k^d (u)\right|$ is large in some neighborhood of $\sigma_i^{(k,d)}$. Recall that $s_k^d (u) = \widetilde{s}_k^d (u) + h_k^d (u)$. We have shown in the proof of Lemma 4.9 that if $\eta (k)$ is any function satisfying $0 < \eta (k) < \frac{C_6}{k}$, then $\left|\widetilde{s}_k^d (u)\right| > C_7\eta (k)$ everywhere on $\partial B_{\eta (k)}\left(\widetilde{\sigma}_i^{(k,d)}\right)$. Furthermore, in this case $\left|h_k^d (u)\right| < C_8A^* k^{-2}$. We now require that

$$
C _ {8} A ^ {*} k ^ {- 2} <   \frac {1}{2} C _ {7} \eta (k)
$$

which is true if $k > \frac{2C_8A^*}{C_7C_6} = K_1A^*$. In that case we have

$$
\left| s _ {k} ^ {d} (u) \right| > \frac {1}{2} C _ {7} \eta (k) \quad \forall u \in B _ {\eta (k)} \left(\widetilde {\sigma} _ {i} ^ {(k, d)}\right)
$$

This is almost what we want - we would like to have such a bound on the boundary of a neighborhood of $\sigma_i^{(k,d)}$ instead of $\widetilde{\sigma}_i^{(k,d)}$. If $i = 0$ then these values coincide, and so we're done. Otherwise, recall that for $k > K_1A^*$ we also have

$\left|\widetilde{\sigma}_i^{(k,d)} - \sigma_i^{(k,d)}\right| \leq C_3A^* k^{-2}$. So in order to make sure that $\sigma_i^{(k,d)}$ belongs to $B_{\eta (k)}\left(\widetilde{\sigma}_i^{(k,d)}\right)$, we just require that $\eta (k) \geq C_3A^* k^{-2}$.

We have thus shown the following:

(a) For every function $0 < \eta(k) < \frac{C_6}{k}$ and for every $k > K_1A^*$, the following bound holds for every $u$ on the boundary of a neighborhood of $\sigma_0^{(k,d)} = 0$ of diameter $2\eta(k)$:

$$
\left| s _ {k} ^ {d} (u) \right| > \frac {1}{2} C _ {7} \eta (k)\tag{4.11}
$$

(b) For every $k > K_{1}A^{*}$ and $\eta(k)$ as above, which additionally satisfies $\eta(k) \geq C_{3}A^{*}k^{-2}$, the above bound holds for every $u$ on the boundary of a neighborhood of $\sigma_{i}^{(k,d)}$ of the same diameter $2\eta(k)$, for every $i = 0,1,\ldots,d$.

(2) We can now show that similar bounds hold for $p_k^d (z)$. Again, only the constants will be different. The map $\mathcal{T}^{-1}$ (4.1), being a Möbius transformation, maps $B_{\eta (k)}\left(\widetilde{\sigma}_i^{(k,d)}\right)$ to a circular neighborhood of $z_{i}^{(k,d)}$ (which is not necessarily centered at $z_{i}^{(k,d)}$). Let $u^{*}\in B_{\eta (k)}\left(\widetilde{\sigma}_{i}^{(k,d)}\right)$. Now $\left|u^{*} - \widetilde{\sigma}_{i}^{(k,d)}\right|\leq C_6k^{-1}$ and also $-\frac{C_2}{k} < \widetilde{\sigma}_i^{(k,d)} < 0$. Therefore if $k > 2(C_2 + C_6)$ then $\Re (u^{*}) > -\frac{1}{2}$ and so $|u^{*} + 1| > \frac{1}{2}$. On the other hand, in this case $|u^{*} + 1| < 2$.

Now let $u_{1}$ and $u_{2}$ be two points in the $u$-plane, such that $|u_{1} - u_{2}| = r$ and $\frac{1}{2} < |u_{1}|, |u_{2}| < 2$. They are mapped to the $z$-plane such that

$$
\frac {r}{4} <   \left| \frac {\omega}{u _ {1} + 1} - \frac {\omega}{u _ {2} + 1} \right| <   4 r
$$

Recalling (4.11) and (4.2), we conclude:

(a) For every function $0 < \eta(k) < \frac{C_6}{k}$ and every $k > \underbrace{\max\left(K_1, 2\left(C_2 + C_6\right)\right)}_{\stackrel{\mathrm{def}}{=} K_6} A^*$, there exists a circular neighborhood of

$\omega$ having diameter between $\frac{\eta(k)}{2}$ and $8\eta(k)$, such that the magnitude of $p_k^d(z)$ on the boundary of this neighborhood satisfies

$$
\left| p _ {k} ^ {d} (z) \right| = \left| z ^ {d + 1} \right| \left| s _ {k} ^ {d} (u) \right| > 2 ^ {- d - 2} C _ {7} \eta (k) = C _ {1 6} \eta (k)
$$

(b) For every $k > K_6 A^*$ and $\eta(k)$ as above, which additionally satisfies $\eta(k) \geq C_3 A^* k^{-2}$, the above bound holds for every $z$ on the boundary of a neighborhood of $z_i^{(k,d)}$ of the same diameter as above, for every $i = 0, 1, \ldots, d$.

(3) Once we have the lower bound for $\left|p_k^d (z)\right|$ on circles of diameter at most $8\eta (k) < \frac{8C_6}{k}$ containing $z_{i}^{(k,d)}$, let us now establish an upper bound for $\left|e_k^d (z)\right|$ on these circles. Let $z_*$ belong to such a circle. On one hand, its distance from $z_{i}^{(k,d)}$ is at most $\frac{8C_6}{k}$. On the other hand, by Lemma 4.11 $\left|z_{i}^{(k,d)} - \omega\right| < \frac{C_{13}}{k}$ for all $k > K_4A^*$. Therefore $|z_* - \omega| < \frac{8C_6 + C_{13}}{k}$. Denote $C_{17} \stackrel{\mathrm{def}}{=} 8C_6 + C_{13}$ and let $z_\theta = \omega + \zeta(k)\mathrm{e}^{\imath\theta}$ where $\zeta(k)$ is some function satisfying $0 < \zeta(k) < \frac{C_{17}}{k}$. Our goal now is to find a uniform upper bound for $\left|e_k^d (z_\theta)\right|$.

(a) By (4.9) we have

$$
\begin{array}{l} r _ {k} - m _ {k} = 2 \pi (\imath k) ^ {d + 1} \left\{c _ {k} (f) - c _ {k} (\Phi_ {d}) \right\} = 2 \pi (\imath k) ^ {d + 1} \left\{c _ {k} (\Phi_ {d _ {1}}) - c _ {k} (\Phi_ {d}) + c _ {k} (\Psi^ {*}) \right\} \\ = 2 \pi (\imath k) ^ {d + 1} \left\{\frac {\omega^ {k}}{2 \pi} \cdot \sum_ {l = d + 1} ^ {d _ {1}} \frac {A _ {l}}{(\imath k) ^ {l + 1}} + c _ {k} (\Psi^ {*}) \right\} = \omega^ {k} \cdot \sum_ {l = 1} ^ {d _ {1} - d} \frac {A _ {d + l}}{(\imath k) ^ {l}} + \underbrace {2 \pi (\imath k) ^ {d + 1} c _ {k} (\Psi^ {*})} _ {\stackrel {{\text {def}}} {{=}} \delta_ {k}} \end{array}\tag{4.12}
$$

Therefore

$$
\begin{array}{l} e _ {k} ^ {d} (z _ {\theta}) = \sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} \left\{\omega^ {k + j} \cdot \sum_ {l = 1} ^ {d _ {1} - d} \frac {A _ {d + l}}{(\imath (k + j)) ^ {l}} + \delta_ {k + j} \right\} z _ {\theta} ^ {d + 1 - j} \\ = \underbrace {\sum_ {l = 1} ^ {d _ {1} - d} (- \imath) ^ {l} A _ {d + l} \sum_ {j = 0} ^ {d + 1} \frac {(- 1) ^ {j}}{(k + j) ^ {l}} \binom {d + 1} {j} \omega^ {k + j} z _ {\theta} ^ {d + 1 - j}} _ {\stackrel {{\mathrm{def}}} {{=}} \Lambda_ {k} (z _ {\theta})} + \underbrace {\sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} \delta_ {k + j} z _ {\theta} ^ {d + 1 - j}} _ {\stackrel {{\mathrm{def}}} {{=}} \Delta_ {k} (z _ {\theta})}. \end{array}
$$

(b) On one hand, we have the bound (4.10). On the other hand, $|z_{\theta}| < 2$ and therefore

$$
| \Delta_ {k} (z _ {\theta}) | \leq C _ {1 8} 2 ^ {d + 1} \cdot 2 \pi \cdot k ^ {d + 1} | c _ {k} (\Psi) | \leq \frac {C _ {1 9} R ^ {*}}{k ^ {d _ {1} - d + 1}}
$$

for some $C_{19}$.

(c) Now we need to estimate $\Lambda_{k}(z_{\theta})$. First

$$
\begin{array}{r l} z _ {\theta} ^ {d + 1 - j} & = \left(\omega + \zeta (k) e ^ {i \theta}\right) ^ {d + 1 - j} \\ & = \omega^ {d + 1 - j} + (d + 1 - j) \omega^ {d - j} \zeta (k) e ^ {i \theta} + \alpha_ {j} (k) \end{array}
$$

where $|\alpha_j(k)| \leq C_{20}\zeta^2(k)$ for some constant $C_{20}$. Furthermore, using the estimate of Lemma A.3 we have

$$
\begin{array}{r c l} \Lambda_ {k} (z _ {\theta}) & = & \omega^ {k + d + 1} \sum_ {l = 1} ^ {d _ {1} - d} \frac {A _ {d + l}}{\imath^ {l}} \underbrace {\sum_ {j = 0} ^ {d + 1} (- 1) ^ {j} \binom {d + 1} {j} \frac {1}{(k + j) ^ {l}}} _ {| \cdot | \leq C _ {2 1} \cdot k ^ {- d - l - 1}} \\ & & + \zeta (k)   \mathrm{e} ^ {\imath \theta} (d + 1) \omega^ {k + d} \sum_ {l = 1} ^ {d _ {1} - d} \frac {A _ {d + l}}{\imath^ {l}} \underbrace {\sum_ {j = 0} ^ {d} (- 1) ^ {j} \binom {d} {j} \frac {1}{(k + j) ^ {l}}} _ {| \cdot | \leq C _ {2 2} \cdot k ^ {- d - l}} \\ & & \underbrace {\sum_ {l = 1} ^ {d _ {1} - d} (- \imath) ^ {l} A _ {d + l} \sum_ {j = 0} ^ {d + 1} \frac {(- 1) ^ {j}}{(k + j) ^ {l}} \binom {d + 1} {j} \omega^ {k + j} \alpha_ {j} (k)} _ {| \cdot | \leq C _ {2 3} \cdot k ^ {- 1} \zeta^ {2} (k)} \end{array}
$$

for all $k > K_{7}$ where $K_{7}$ is an explicit constant (see Lemma A.3). Therefore

$$
\left| \Lambda_ {k} (z _ {\theta}) \right| <   A ^ {* *} \times \left\{C _ {2 4} \cdot k ^ {- d - 2} + C _ {2 5} \zeta (k) k ^ {- d - 1} + C _ {2 6} \cdot k ^ {- 1} \zeta^ {2} (k) \right\}
$$

Combining all the above estimates we therefore have for $k > \max(K_4, K_7) A^*$

$$
\left| e _ {k} ^ {d} (z _ {\theta}) \right| <   A ^ {* *} \times \left(\frac {C _ {2 4}}{k ^ {d + 2}} + \frac {C _ {2 5}}{k ^ {d + 1}} \zeta (k) + \frac {C _ {2 6}}{k} \zeta^ {2} (k)\right) + \frac {C _ {1 9} R ^ {*}}{k ^ {d _ {1} - d + 1}}\tag{4.13}
$$

(4) We can finally compare $\left|p_k^d (z)\right|$ and $\left|e_k^d (z)\right|$. Let $k > \underbrace{\max(K_4, K_7, K_6)}_{A^*} A^*$ and consider two cases.

$$
k > \underbrace {\max \left(K _ {4} , K _ {7} , K _ {6}\right)} _ {\stackrel {{\text { def }}} {{=}} K _ {8}} A ^ {*}
$$

(a) Suppose $z_{i}^{(k,d)} \neq \omega$. Set $\rho(k) = \frac{C_{14}H}{8k^2}$ where $C_{14}$ is to be determined, and suppose also that

$$
C _ {3} A ^ {*} k ^ {- 2} \leq \rho (k) <   \frac {C _ {6}}{k}\tag{4.14}
$$

We have shown above that there exists a neighborhood $D_{i}^{(k)}$ containing $z_{i}^{(k,d)}$ of diameter at most $8\rho(k) = C_{14}\cdot H\cdot k^{-2}$ such that for every $z^{*}\in \partial D_{i}^{(k,d)}$ we have $\left|p_k^d (z^*)\right| > C_{16}\rho (k) = \frac{C_{16}C_{14}H}{8k^2}$. On the other hand, for every such $z^{*}$ we have by (4.13)

$$
\begin{array}{r l} & {\left| e _ {k} ^ {d} (z ^ {*}) \right| <   A ^ {* *} \times \left(\frac {C _ {2 4}}{k ^ {d + 2}} + \frac {C _ {2 5}}{k ^ {d + 1}} \rho (k) + \frac {C _ {2 6}}{k} \rho^ {2} (k)\right) + \frac {C _ {1 9} R ^ {*}}{k ^ {d _ {1} - d + 1}}} \\ & {\qquad <   \frac {A ^ {* *} \times \left(C _ {2 4} + C _ {2 5} C _ {6} + C _ {2 6} C _ {6} ^ {2}\right) + C _ {1 9} R ^ {*}}{k ^ {2}} <   (A ^ {* *} + R ^ {*}) \frac {C _ {2 7}}{k ^ {2}}} \end{array}
$$

Therefore we must choose $C_{14}$ and $k$ for which the condition $\frac{C_{16}C_{14}H}{8k^2} >\frac{C_{27}(A^{**} + R^*)}{k^2}$ is satisfied, together with (4.14). For example:

$$
\begin{array}{c} C _ {1 4} \stackrel {{\mathrm{def}}} {{=}} \max \left(\frac {8 C _ {2 7}}{C _ {1 6}}, 8 C _ {3}\right) \\ k > \underbrace {\max \left(K _ {8} , \frac {C _ {1 4}}{8 C _ {6}}\right)} _ {\stackrel {{\mathrm{def}}} {{=}} K _ {5}} \times H \end{array}
$$

In this case, $q_{k}^{d}(z)$ has a simple zero $\kappa_{i}^{(k,d)}$ in $D_{i}^{(k)}$ so that $\left|\kappa_{i}^{(k,d)} - z_{i}^{(k,d)}\right| < C_{14}\left(A^{*} + A^{**} + R^{*}\right)k^{-2}$.

(b) Now consider the case $z_0^{(k,d)} = \omega$. Set $\rho(k) = \frac{C_{15}H}{8k^{d + 2}}$ where $C_{15}$ is to be determined. We again require that $\rho(k) < \frac{C_6}{k}$. We have shown that whenever $k > K_6A^*$, there exists a neighborhood $D_0^{(k)}$ containing $\omega$ such that for every $z^* \in \partial D_0^{(k)}$ we have $|p_k^d (z^*)| > C_{16}\rho(k) = \frac{C_{15}C_{16}H}{8k^{d + 2}}$. On the other hand, by (4.13) for every such $z^*$

we have

$$
\begin{array}{c} \left| e _ {k} ^ {d} (z ^ {*}) \right| <   A ^ {* *} \times \left(\frac {C _ {2 4}}{k ^ {d + 2}} + \frac {C _ {2 5}}{k ^ {d + 1}} \rho (k) + \frac {C _ {2 6}}{k} \rho^ {2} (k)\right) + \frac {C _ {1 9} R ^ {*}}{k ^ {d _ {1} - d + 1}} \\ <   \frac {A ^ {* *} \times \left(C _ {2 4} + C _ {2 5} C _ {6} + C _ {2 6} C _ {6} ^ {2}\right) + C _ {1 9} R ^ {*}}{k ^ {d + 2}} <   \frac {C _ {2 7} (A ^ {* *} + R ^ {*})}{k ^ {d + 2}} \end{array}
$$

So we require $\frac{C_{15}C_{16}H}{8k^d + 2} >\frac{C_{27}(A^{**} + R^*)}{k^d + 2}$ together with $\frac{C_{15}H}{8k^d + 2} < \frac{C_6}{k}$. This is possible for example when

$$
C _ {1 5} = \frac {8 C _ {2 7}}{C _ {1 6}}
$$

$$
k > K _ {5} H \geq \left(\frac {C _ {1 5} H}{8 C _ {6}}\right) ^ {\frac {1}{d + 1}}
$$

Thus we have completed the proof of Lemma 4.12.

We can finally combine everything and prove the main result of this section.

Theorem 4.13. Let $f$ have $d_1 \geq 2d + 1$ continuous derivatives everywhere in $[-\pi, \pi] \setminus \{\xi\}$. Let $q_k^d(z)$ be as defined in (3.3), and let $\left\{\kappa_i^{(k,d)}\right\}_{i=0}^d$ denote its roots, such that $\left|\kappa_0^{(k,d)}\right| \leq \ldots \left|\kappa_d^{(k,d)}\right|$. Let $\{\phi_i\}_{i=1}^d$ denote the roots of the Laguerre polynomial $\mathcal{L}_d^{(1)}$, such that $|\phi_1| < \ldots |\phi_d|$. Let $y_0^{(k,d)} = \omega$ and $y_i^{(k,d)} = \mathcal{T}^{-1}\left(-\frac{\phi_i}{k}\right)$ for $i = 1, \ldots, d$ (see (4.8)). Then there exist constants $C_9, C_{15}, C_{28}$ and $K_9$ such that for every $k > K_9H$ the following statements are true:

(1) The numbers $\left\{y_i^{(k,d)}\right\}$ lie on the ray $O\omega$, so that $\left|y_i^{(k,d)}\right| \geq 1$, and:

$$
C _ {9} k ^ {- 1} \leq \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right| \quad 0 \leq i <   j \leq d
$$

(2) Each of the numbers $\left\{\kappa_i^{(k,d)}\right\}_{i = 1}^d$ is close to some $y_{i}^{(k,d)}$:

$$
\left| \kappa_ {i} ^ {(k, d)} - y _ {i} ^ {(k, d)} \right| \leq C _ {2 8} \cdot H \cdot k ^ {- 2}
$$

(3) The smallest $\kappa_0^{(k,d)}$ is very close to $\omega$:

$$
\left| \kappa_ {0} ^ {(k, d)} - \omega \right| \leq C _ {1 5} \cdot H \cdot k ^ {- d - 2}
$$

(4) Algorithm 3.2 provides an approximation for $\omega$ which is accurate up to order $k^{-(d+2)}$.

Proof. We have already proved (1) (for $k > K_2$) and (3) (for $k > K_3A^*$) - see Lemma 4.12. (2) follows from Lemma 4.12 and Lemma 4.11 by choosing $C_{28} = C_{14} + C_{11}$ and $k > K_5H$. In order to prove (4), we need to show that no root $\kappa_i^{(k,d)}$ is closer to the unit circle than $\kappa_0^{(k,d)}$. From geometric considerations (see Figure 4.1 on page 15), it is sufficient to require that

$$
\left| \kappa_ {i} ^ {(k, d)} - y _ {i} ^ {(k, d)} \right| \leq C _ {2 8} \cdot H \cdot k ^ {- 2} <   \frac {1}{2} C _ {9} k ^ {- 1} <   \frac {1}{2} \min _ {j \neq i} \left| y _ {i} ^ {(k, d)} - y _ {j} ^ {(k, d)} \right|
$$

which is true whenever

$$
k > \frac {2 C _ {2 8} H}{C _ {9}}
$$

Therefore we choose

$$
K _ {9} = \max \left(K _ {2}, K _ {3}, K _ {5}, \frac {2 C _ {2 8}}{C _ {9}}\right)
$$

4.2. Accuracy analysis: jump magnitudes. Suppose that  $d_{1} \geq 2d + 1$  and let  $k > K_{9}H$  so that our algorithm gives an approximation  $\widetilde{\omega}_{(k)}$  with error at most  $C_{15}H \cdot k^{-d-2}$ , in accordance with Theorem 4.13. Our goal is to analyze the accuracy of calculating the approximate jump magnitudes  $A_{l}^{(k)}$ , given by the solution of the linear system (3.5). For convenience, we denote

$$
\begin{array}{r l} {B _ {l}} & {\stackrel {\mathrm{def}} {=} \imath^ {l} A _ {d - l}} \\ {\widetilde {B} _ {l} ^ {(k)}} & {\stackrel {\mathrm{def}} {=} \imath^ {l} \widetilde {A} _ {d - l} ^ {(k)}} \end{array}
$$

![](images/page_14_image_0.jpg)

FIGURE 4.1. The geometry of $\left\{\kappa_i^{(k,d)}\right\},\left\{y_i^{(k,d)}\right\},\left\{z_i^{(k,d)}\right\}$. The superscripts $(k,d)$ are omitted. The picture on the right shrinks towards the unit circle as $k\to \infty$.

We consider only the case of exactly $d + 1$ equations. Thus we can write this system in the following form:

$$
\left[ \begin{array}{c} r _ {k} \widetilde {\omega} _ {(k)} ^ {- k} \\ \vdots \\ r _ {k + d} \widetilde {\omega} _ {(k)} ^ {- k - d} \end{array} \right] = V _ {k} \times \left[ \begin{array}{c} \widetilde {B} _ {0} ^ {(k)} \\ \vdots \\ \widetilde {B} _ {d} ^ {(k)} \end{array} \right]\tag{4.15}
$$

where $V_{k}$ is the $(d + 1)\times (d + 1)$ system matrix

$$
V _ {k} \stackrel {\mathrm{def}} {=} \left[ \begin{array}{c c c c} 1 & k & \ldots & k ^ {d} \\ 1 & (k + 1) & \ldots & (k + 1) ^ {d} \\ \vdots & \vdots & \vdots & \vdots \\ 1 & (k + d) & \ldots & (k + d) ^ {d} \end{array} \right]
$$

By (3.4), the "true" coefficients $B_{j}$ satisfy

$$
\left[ \begin{array}{c} m _ {k} \omega^ {- k} \\ \vdots \\ m _ {k + d} \omega^ {- k - d} \end{array} \right] = V _ {k} \times \left[ \begin{array}{c} B _ {0} \\ \vdots \\ B _ {d} \end{array} \right]\tag{4.16}
$$

Our goal is to estimate the error $\varepsilon_{j}^{(k)} \stackrel{\mathrm{def}}{=} B_{j} - \widetilde{B}_{j}^{(k)}$ for $j = 0,1,\ldots,d$. Let

$$
\eta_ {j} ^ {(k)} \stackrel {\mathrm{def}} {=} r _ {k + j} \widetilde {\omega} _ {(k)} ^ {- k - j} - m _ {k + j} \omega^ {- k - j}
$$

Then subtracting (4.16) from (4.15) gives

$$
\left[ \begin{array}{c} \varepsilon_ {0} ^ {(k)} \\ \varepsilon_ {1} ^ {(k)} \\ \vdots \\ \varepsilon_ {d} ^ {(k)} \end{array} \right] = V _ {k} ^ {- 1} \times \left[ \begin{array}{c} \eta_ {0} ^ {(k)} \\ \eta_ {1} ^ {(k)} \\ \vdots \\ \eta_ {d} ^ {(k)} \end{array} \right]\tag{4.17}
$$

This is the key relation of this section. In order to estimate the magnitude of  $\varepsilon_{j}^{(k)}$ , we shall first write out explicit expansions for the quantities  $\eta_{j}^{(k)}$ , and then investigate how these expansions are transformed when multiplied by the matrix  $V_{k}^{-1}$ . Our analysis will show that the special combination of the structures of both this matrix and the expansion coefficients results in remarkable cancellations.

Let us start by investigating the structure of the matrix  $V_{k}$ .

Definition 4.14. Let $S_{k,d}$ denote the $(d + 1) \times (d + 1)$ square matrix with entries:

$$
\left(S _ {k, r}\right) _ {m, n} = \left(- k\right) ^ {n - m} {\binom {n - 1} {n - m}}
$$

Example 4.15. For $d = 4$, we have

$$
S _ {k, 4} = \left( \begin{array}{c c c c c} 1 & - k & k ^ {2} & - k ^ {3} & k ^ {4} \\ 0 & 1 & - 2 k & 3 k ^ {2} & - 4 k ^ {3} \\ 0 & 0 & 1 & - 3 k & 6 k ^ {2} \\ 0 & 0 & 0 & 1 & - 4 k \\ 0 & 0 & 0 & 0 & 1 \end{array} \right)
$$

Definition 4.16. For every $k \in \mathbb{N}$ let the symbol $\mathbf{v}_{\mathbf{k}}$ denote the following $1 \times (d + 1)$ row vector

$$
\mathbf {v _ {k}} \stackrel {\mathrm{def}} {=} \left[ \begin{array}{l l l l} 1 & k & \ldots & k ^ {d} \end{array} \right]
$$

With this definition, we have

$$
V _ {k} = \left[ \begin{array}{c} \mathbf {v} _ {\mathbf {k}} \\ \mathbf {v} _ {\mathbf {k + 1}} \\ \vdots \\ \mathbf {v} _ {\mathbf {k + d}} \end{array} \right]\tag{4.18}
$$

Lemma 4.17. Let $k \geq 0$, then

$$
V _ {k} ^ {- 1} = S _ {k, d} \times V _ {0} ^ {- 1}\tag{4.19}
$$

Proof. Let $1 \leq m \leq d + 1$ and $0 \leq t \leq d$. The $m$-th entry of the vector $\mathbf{v}_{\mathbf{k} + \mathbf{t}} \times S_{k,d}$ equals to

$$
\left(\mathbf {v} _ {\mathbf {k} + \mathbf {t}} \times S _ {k, d}\right) _ {m} = \sum_ {l = 0} ^ {m - 1} (k + t) ^ {l} (- k) ^ {m - 1 - l} \binom {m - 1} {m - 1 - l} = t ^ {m - 1}
$$

and therefore

$$
\mathbf {v _ {k + t}} \times S _ {k, d} = \mathbf {v _ {t}}
$$

(4.19) then follows from (4.18).

Now we would like to expand $\eta_j^{(k)}$. We can obviously assume the equality

$$
\widetilde {\omega} _ {(k)} = \omega + \frac {\alpha (k)}{k ^ {d + 2}} \quad \text { such   that } \quad | \alpha (k) | \leq C _ {1 5} H
$$

Now we estimate $\widetilde{\omega}_{(k)}$ by Proposition B.3 as follows:

$$
\left(\omega + \frac {\alpha (k)}{k ^ {d + 2}}\right) ^ {- (k + j)} = \omega^ {- k - j} \left(1 + \frac {\alpha (k) \omega^ {- 1}}{k ^ {d + 2}}\right) ^ {- k - j} = \omega^ {- k - j} \left(1 - (k + j) \frac {\alpha (k) \omega^ {- 1}}{k ^ {d + 2}} + R _ {1} (k, j)\right)
$$

where $k$ is large enough so that $\frac{\alpha(k)\omega^{-1}}{k^{d + 2}} < \frac{3}{k + j + 2}$ is satisfied, and

$$
\left| R _ {1} (k, j) \right| <   \frac {(k + j) (k + j + 1) \alpha^ {2} (k) \omega^ {- 2}}{2 k ^ {2 (d + 2)} \left(1 - \frac {\alpha (k) \omega^ {- 1} (k + j + 2)}{3 k ^ {d + 2}}\right)} <   C _ {2 9} \cdot H ^ {2} k ^ {- 2 d - 3}
$$

Obviously, $|r_k| \leq C_{30} \cdot H \cdot k^d$. Now by (4.12), we have

$$
\begin{array}{l} \eta_ {j} ^ {(k)} = \left(m _ {k + j} + \omega^ {k + j} \cdot \sum_ {l = 1} ^ {d _ {1} - d} \frac {A _ {d + l}}{(\imath (k + j)) ^ {l}} + \delta_ {k + j}\right) \widetilde {\omega} _ {(k)} ^ {- k - j} - m _ {k + j} \omega^ {- k - j} \\ = \left(m _ {k + j} + \omega^ {k + j} \cdot \sum_ {l = 1} ^ {d _ {1} - d} \frac {A _ {d + l}}{(\imath (k + j)) ^ {l}} + \delta_ {k + j}\right) \omega^ {- k - j} \left(1 - \frac {(k + j) \alpha (k) \omega^ {- 1}}{k ^ {d + 2}}\right) - m _ {k + j} \omega^ {- k - j} + r _ {k + j} \omega^ {- k - j} R _ {1} (k) \\ = \frac {\beta (k)}{k ^ {d + 2}} \sum_ {l = 0} ^ {d} B _ {l} (k + j) ^ {l + 1} + \sum_ {l = 1} ^ {d _ {1} - d} \frac {A _ {d + l}}{(\imath (k + j)) ^ {l}} + R _ {2} (k, j) \end{array}
$$

where $|R_2(k,j)| \leq C_{31} \cdot H^2 k^{-d-2}$ and $|\beta(k)| \leq C_{32} \cdot H$.

Therefore we can write

$$
\begin{array}{r l} & {\left[ \begin{array}{c} \eta_ {0} ^ {(k)} \\ \vdots \\ \eta_ {j} ^ {(k)} \\ \vdots \\ \eta_ {d} ^ {(k)} \end{array} \right] = \beta (k) B _ {0} \left[ \begin{array}{c} \frac {k}{k ^ {d + 2}} \\ \vdots \\ \frac {k + j}{k ^ {d + 2}} \\ \vdots \\ \frac {k + d}{k ^ {d + 2}} \end{array} \right] + \dots + \beta (k) B _ {l} \left[ \begin{array}{c} \frac {k ^ {l}}{k ^ {d + 2}} \\ \vdots \\ \frac {(k + j) ^ {l}}{k ^ {d + 2}} \\ \vdots \\ \frac {(k + d) ^ {l}}{k ^ {d + 2}} \end{array} \right] + \dots + \beta (k) B _ {d} \left[ \begin{array}{c} \frac {k ^ {d + 1}}{k ^ {d + 2}} \\ \vdots \\ \frac {(k + j) ^ {d + 1}}{k ^ {d + 2}} \\ \vdots \\ \frac {(k + d) ^ {d + 1}}{k ^ {d + 2}} \end{array} \right]} \\ & {\quad + \frac {A _ {d + 1}}{\imath} \left[ \begin{array}{c} \frac {1}{k} \\ \vdots \\ \frac {1}{k + j} \\ \vdots \\ \frac {1}{k + d} \end{array} \right] + \dots + \frac {A _ {d + l}}{\imath^ {l}} \left[ \begin{array}{c} \frac {1}{k ^ {l}} \\ \vdots \\ \frac {1}{(k + j) ^ {l}} \\ \vdots \\ \frac {1}{(k + d) ^ {l}} \end{array} \right] + \dots + \frac {A _ {d _ {1}}}{\imath^ {d}} \left[ \begin{array}{c} \frac {1}{k ^ {d + 1}} \\ \vdots \\ \frac {1}{(k + j) ^ {d + 1}} \\ \vdots \\ \frac {1}{(k + d) ^ {d + 1}} \end{array} \right] + \left[ \begin{array}{c} R _ {2} (k, 0) \\ \vdots \\ R _ {2} (k, j) \\ \vdots \\ R _ {2} (k, d) \end{array} \right]} \end{array}\tag{4.20}
$$

In light of (4.17), we would now like to examine the action of the matrix $V_0^{-1}$ on the vectors in the right hand side of (4.20).

Lemma 4.18. Let $j = 0,1,\ldots ,d$.

(1) If $l = 1,2,\ldots,d$ then

$$
\left[ \begin{array}{c} k ^ {l} \\ \vdots \\ (k + j) ^ {l} \\ \vdots \\ (k + d) ^ {l} \end{array} \right] = V _ {0} \times \left[ \begin{array}{c} k ^ {l} \binom {l} {0} \\ \vdots \\ k ^ {l - j} \binom {l} {j} \\ \vdots \\ 1 \cdot \binom {l} {i} \\ 0 \\ \vdots \\ 0 \end{array} \right]\tag{4.21}
$$

(2) Otherwise, there exists a function $R_3: \{0, 1, \ldots, d\} \to \mathbb{R}$ such that

$$
\left[ \begin{array}{c} k ^ {d + 1} \\ \vdots \\ (k + j) ^ {d + 1} \\ \vdots \\ (k + d) ^ {d + 1} \end{array} \right] = V _ {0} \times \left[ \begin{array}{c} k ^ {d + 1} \binom {d + 1} {0} \\ \vdots \\ k ^ {d + 1 - j} \binom {d + 1} {j} \\ \vdots \\ k \binom {d + 1} {1} \end{array} \right] + \left[ \begin{array}{c} R _ {3} (0) \\ \vdots \\ R _ {3} (j) \\ \vdots \\ R _ {3} (d) \end{array} \right]\tag{4.22}
$$

Proof. Straightforward application of the binomial theorem.

Lemma 4.19. For  $j = 1, 2, \ldots$  and  $i = 1, \ldots, d + 1$  denote

$$
\tau_ {j} ^ {i} \stackrel {\text {def}} {=} (- 1) ^ {i - 1} \binom {j + i - 2} {j - 1}
$$

Then there exists a bounded function $R_4:\{0,1,\ldots ,d\} \times \mathbb{N}\to \mathbb{R}$ such that

$$
\left[ \begin{array}{c} \frac {1}{k ^ {j}} \\ \frac {1}{(k + 1) ^ {j}} \\ \vdots \\ \frac {1}{(k + d) ^ {j}} \end{array} \right] = V _ {0} \times \left[ \begin{array}{c} \frac {\tau_ {j} ^ {1}}{k ^ {j}} \\ \frac {\tau_ {j} ^ {2}}{k ^ {j + 1}} \\ \vdots \\ \frac {\tau_ {j} ^ {d + 1}}{k ^ {j + d}} \end{array} \right] + \frac {1}{k ^ {d + j + 1}} \left[ \begin{array}{c} R _ {4} (0, j) \\ \vdots \\ R _ {4} (l, j) \\ \vdots \\ R _ {4} (d, j) \end{array} \right]\tag{4.23}
$$

Proof. First recall the well-known $^{1}$ power series expansion

$$
\frac {1}{(1 + x) ^ {j}} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \binom {j - 1 + n} {j - 1} x ^ {n}
$$

Now let  $l = 0, 1, \ldots, d$ .

(1) On one hand, the  $(l+1)$ -st entry in the product on the right-hand side of (4.23) equals to

$$
g _ {j, l} \stackrel {\mathrm{def}} {=} \sum_ {i = 0} ^ {d} (- 1) ^ {i} \frac {\binom {j - 1 + i} {i}}{k ^ {i + j}} l ^ {i}
$$

(2) On the other hand, by Proposition B.3 we have for some bounded function  $R_{4}:\{0,1,\ldots,d\}\times N\to R$

$$
\begin{array}{c} \frac {1}{(k + l) ^ {j}} = \frac {1}{k ^ {j}} \cdot \frac {1}{\left(1 + \frac {l}{k}\right) ^ {j}} = \frac {1}{k ^ {j}} \left\{\sum_ {i = 0} ^ {d} (- 1) ^ {i} \binom {j - 1 + i} {j - 1} \left(\frac {l}{k}\right) ^ {i} + \frac {R _ {4} (l , j)}{k ^ {d + 1}} \right\} \\ = \underbrace {\sum_ {i = 0} ^ {d} (- 1) ^ {i} \frac {\binom {j - 1 + i} {i}}{k ^ {i + j}} l ^ {i}} _ {= g _ {j, l}} + \frac {R _ {4} (l , j)}{k ^ {j + d + 1}} \end{array}
$$

Thus (4.23) is proved.

It is now easily seen that the multiplication by  $V_{0}^{-1}$  “orders up” the vectors in (4.20) by decreasing powers of k. Further multiplication by  $S_{k,d}$  from the left preserves this structure, as is evident from the following calculation.

Lemma 4.20. Let  $c_{i,j}$  be arbitrary constants. Then there exist constants  $\gamma_{i,j}$  such that

$$
\boldsymbol {S} _ {k, d} \times \left[ \begin{array}{c} \frac {c _ {1 , j}}{k ^ {j}} \\ \frac {c _ {2 , j}}{k ^ {j + 1}} \\ \vdots \\ \frac {c _ {d + 1 , j}}{k ^ {j + d}} \end{array} \right] = \left[ \begin{array}{c} \frac {\gamma_ {1 , j}}{k ^ {j}} \\ \frac {\gamma_ {2 , j}}{k ^ {j + 1}} \\ \vdots \\ \frac {\gamma_ {d + 1 , j}}{k ^ {j + d}} \end{array} \right]\tag{4.24}
$$

Proof. Let  $i = 1, \ldots, d + 1$  and consider the i-th entry of the product, say  $y_{i}$ :

$$
y _ {i} = \sum_ {l = 1} ^ {d + 1} (S _ {k, d}) _ {i, l} \times \frac {c _ {l , j}}{k ^ {j + l - 1}} = \sum_ {l = 0} ^ {d} (- k) ^ {l + 1 - i} \binom {l} {l + 1 - i} \times \frac {c _ {l + 1 , j}}{k ^ {l + j}} = \frac {1}{k ^ {j + i - 1}} \gamma_ {i, j}
$$

where $\gamma_{i,j} = \sum_{l = i - 1}^{d}(-1)^{l + 1 - i}\binom{l}{l - (i - 1)}c_{l + 1,j}$. This proves the claim.

We can now prove the main result of this section.

Theorem 4.21. Assume that $d_1 \geq 2d + 1$ and $k > K_9H$, so that by Theorem 4.13 we have $\left|\widetilde{\omega}_{(k)} - \omega\right| \leq C_{15} \cdot H \cdot k^{-d-2}$. Then there exist constants $C_{33}, K_{10}$ such that for every $k > K_{10}H$ and $l = 0, 1, \ldots, d$ the error in determining $A_l$ is

$$
\left| \widetilde {A} _ {l} ^ {(k)} - A _ {l} \right| \leq C _ {3 3} \cdot H ^ {2} \cdot k ^ {l - d - 1}
$$

Proof. Combine (4.17), (4.20), (4.21), (4.22), (4.23) and (4.24).

## 5. LOCALIZING THE DISCONTINUITIES

As we have seen, both the location and the magnitudes of the jump can be reconstructed with high accuracy. The remaining ingredient in our method is to divide the initial function into regions containing a single jump, and subsequently apply the reconstruction algorithm in each region.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">j,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\sum_{k = 0}^{n}\binom{r + k}{r} = \binom{r + n + 1}{r + 1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$ It can be proven by induction on j, using the identity  $\sum_{k=0}^{n}\binom{r+k}{r}=\binom{r+n+1}{r+1}$ .</span></small>

Our approach is to multiply the initial function f by a “bump”  $g_{j}$  which vanishes outside some neighborhood of the j-th jump. This step requires a-priori estimates of the jump positions, which can fortunately be obtained by a variety of methods, for example:

(1) The concentration method of Gelb&Tadmor [20];

(2) The method of partial sums due to Banerjee&Geer [3];

(3) Eckhoff's method with order zero (the Prony method).

All the above methods provide accurate estimates of $\{\xi_j\}$ up to first order. For definiteness, we present the description of the last method and a rigorous proof of its convergence in Appendix D.

Now, the multiplication is implemented as Fourier domain convolution. Because of the Fourier uncertainty principle, the Fourier series of our bump will have infinite support and therefore every practically computable convolution will always be an approximation to the exact one. Nevertheless, an error of order at most  $k^{-d_{1}-2}$  in the Fourier coefficients will be “absorbed” in the constant  $R^{*}$  (4.10) and therefore we will still have accurate estimates for the reconstruction of each separate jump. This will require us to use bump functions which are  $C^{\infty}$ . An explicit construction of such a function is provided in Appendix C. We assume that the following quantities are known a-priori:

\- the lower and upper bounds for the jump magnitudes of order zero: $J_{1} \leq |A_{0,j}| \leq J_{2}$;

\- the minimal distance between any two jumps $|\xi_i - \xi_j| \geq J_3 > 0$;

\- a constant T for which

$$
\left| 2 \pi (\imath k) c _ {k} (f) - \sum_ {j = 1} ^ {K} A _ {0, j} \omega_ {j} ^ {k} \right| \leq T \cdot k ^ {- 1}\tag{5.1}
$$

Our localization algorithm can be summarized as follows.

Algorithm 5.1. Let $f$ be a piecewise-smooth function of order $d_1 \geq 2d + 1$ with $K$ jumps $\{\xi_j\}_{j=1}^K$ and jump magnitudes $\{A_{l,j}\}_{l=0,\dots,d}^{j=1,\dots,K}$. Let there be given the Fourier coefficients $\{c_k(f)\}_{|k|=0}^{2M+d+1}$, where $M$ is large enough (see below).

(1) Using the a-priori bounds $J_{1}, J_{2}, J_{3}, T$, obtain approximate locations of the jumps $\{\widehat{\xi}_j\}$ via Algorithm D.3. In particular, the error $|\widehat{\xi}_j - \xi_j|$ should not exceed $\frac{J_3}{3}$, and this will be possible if $M$ is not smaller than required by Theorem D.9.

(2) For each $\widehat{\xi_j}$:

(a) Construct the bump $g_{j}$ centered at $\widehat{\xi}_{j}$ with parameters $t = 2 \cdot \frac{J_3}{3}$ and $E = J_3$, according to Appendix C. Calculate its Fourier coefficients in the range $k = -3M \ldots 3M$ according to (C.2).

(b) Now let $h_j = f \cdot g_j$. For each $k = 0, 1, \ldots, M + d + 1$ calculate

$$
\widetilde {c _ {k}} ^ {(M)} (h _ {j}) = \sum_ {i = - 2 M} ^ {2 M} c _ {i} (f) c _ {k - i} (g _ {j})\tag{5.2}
$$

(c) Use the above approximate Fourier coefficients $\widetilde{c}_k^{(M)}(h_j)$ as the input to Algorithm 3.2 for reconstructing all the parameters of a single jump.

Theorem 5.2. Algorithm 5.1 will produce estimates of all these parameters with the accuracy as stated in Theorems 4.13 and 4.21,  $R^{*}$  being replaced with some other constant  $\widehat{R}^{*} = \widehat{R}^{*}(R^{*}, T, J_{2}, J_{3})$ .

Proof. It is clear that the exact function $h_j = f \cdot g_j$ has exactly one jump at $\xi$ and jump magnitudes $A_{0,j}, \ldots, A_{d,j}$. In order to prove that Theorems 4.13 and 4.21 can be applied, it is sufficient to show that the error $\left|\widetilde{c_k}^{(M)}(h_j) - c_k(h_j)\right|$ is of the order $k^{-(d_1 + 2)}$. By the Fourier convolution theorem the exact Fourier coefficients of $h_j$ are equal to:

$$
c _ {k} (h _ {j}) = \sum_ {i = - \infty} ^ {\infty} c _ {i} (f) c _ {k - i} (g _ {j})
$$

while our algorithm approximates these by the truncated convolution (5.2). Let us estimate the convolution tail

$$
\Delta c _ {k} ^ {(M)} (h _ {j}) = \sum_ {i = - \infty} ^ {- 2 M} c _ {i} (f) c _ {k - i} (g _ {j}) + \sum_ {i = 2 M} ^ {\infty} c _ {i} (f) c _ {k - i} (g _ {j})
$$

On one hand, the Fourier coefficients of $f$ can be bounded using (5.1):

$$
\left| c _ {k} (f) \right| \leq C _ {3 4} \left(J _ {2} + T\right) k ^ {- 1}
$$

On the other hand, taking  $\alpha = d_{1} + 1$  we have by Theorem C.1

$$
\left| c _ {k} \left(g _ {j}\right) \right| \leq \frac {C _ {3 5}}{J _ {3} ^ {d _ {1} + 1}} \cdot \frac {1}{k ^ {d _ {1} + 2}}
$$

Finally

$$
\left| \Delta c _ {k} ^ {(M)} (h _ {j}) \right| \leq \frac {C _ {3 6} (J _ {2} + T)}{J _ {3} ^ {d _ {1} + 1}} \sum_ {i = 2 M} ^ {\infty} \frac {1}{i ^ {d _ {1} + 3}} \leq \frac {C _ {3 6} (J _ {2} + T)}{J _ {3} ^ {d _ {1} + 1}} \zeta (d _ {1} + 3, 2 M) \leq \frac {C _ {3 7} \cdot (J _ {2} + T)}{J _ {3} ^ {d _ {1} + 1}} M ^ {- d _ {1} - 2}
$$

where $\zeta(s, q)$ is the Hurwitz zeta function. Therefore Algorithm 3.2 will produce estimates of $\{\widetilde{\xi}_j\}$ and $\{\widetilde{A}_{l,j}\}$ with accuracy as guaranteed by Theorems 4.13 and 4.21 where

$$
\widehat {R ^ {*}} = R ^ {*} + \frac {(J _ {2} + T)}{J _ {3} ^ {d _ {1} + 1}}
$$

## 6. FINAL ACCURACY

In this section we are going to calculate the overall accuracy of approximation. Let us therefore suppose that $d_1 \geq 2d + 1$, and so using the Fourier coefficients $c_{-2M}(f), \ldots, c_{2M}(f)$ we have reconstructed the singular part $\Phi(x)$ with accuracy specified by Theorem 5.2. Recall from (2.3) that our final approximation is defined by

$$
\widetilde {f} = \sum_ {| k | \leq M} \left(c _ {k} (f) - c _ {k} (\widetilde {\Phi})\right) e ^ {i k x} + \widetilde {\Phi}
$$

where $\widetilde{\Phi} = \sum_{j=1}^{K} \sum_{l=0}^{d} \widetilde{A}_{l,j} V_l(x; \widetilde{\xi}_j)$. Intuitively, the approximation error function $\widetilde{f} - f$ will look as depicted in Figure 6.1 on page 21 - very small almost everywhere except in some shrinking neighborhoods of the jump points. Let $y \in [-\pi, \pi] \setminus \{\xi_j\}_{j=1}^K$. If we take $M$ large enough so that the error estimate of Theorem 4.13 will be less than the distance to the nearest jump $|y - \xi_j|$, then $y$ will lie in the "flat" region of Figure 6.1 on page 21 and the error $\left|\widetilde{f}(y) - f(y)\right|$ will be small. This is precisely the content of our final theorem.

Let us denote the "jump-free" region by

$$
\mathbf {D} _ {\mathbf {r}} \stackrel {{\text { def }}} {{=}} \left[ - \pi , \pi \right] \setminus \left(\bigcup_ {j = 1} ^ {K} B _ {r} \left(\xi_ {j}\right)\right)
$$

Theorem 6.1. Let $f: [-\pi, \pi] \to \mathbb{R}$ have $K$ jump discontinuities $\{\xi_j\}_{j=1}^K$, and let it be $d_1$-times continuously differentiable between the jumps. Let $r > 0$. Then for every integer $d$ satisfying $2d + 1 \leq d_1$, there exist explicit functions $F = F(\mathbb{A}, \widehat{R^*})$, $G = G(\mathbb{A}, \widehat{R^*}, r)$ depending on all the $a$-priori bounds such that for all $M > G$. Algorithm 2.2 reconstructs the locations and the magnitudes of the jumps with accuracy provided by Theorem 5.2, and with the pointwise accuracy

$$
\left| \widetilde {f} (y) - f (y) \right| \leq F \cdot M ^ {- d - 1} \quad y \in \mathbf {D _ {r}}
$$

Proof. Define

$$
f _ {M} \stackrel {\text { def }} {=} \sum_ {| k | \leq M} \left(c _ {k} (f) - c _ {k} (\Phi)\right) e ^ {\imath k x} + \Phi
$$

We write the overall approximation error as

$$
\left| \widetilde {f} (y) - f (y) \right| \leq \left| \widetilde {f} (y) - f _ {M} (y) \right| + \left| f _ {M} (y) - f (y) \right|\tag{6.1}
$$

Let us examine the two terms on the right-hand side separately.

According to our previous notation, $\Psi = f - \Phi$ is a $d$-times continuously differentiable everywhere function. The term $|f_M - f|$ is easily seen to be the usual Fourier truncation error of $\Psi$, since

$$
\left| f _ {M} (y) - f (y) \right| = \left| \sum_ {| k | \leq M} \left(c _ {k} (f) - c _ {k} (\Phi)\right) e ^ {\imath k y} + \Phi (y) - f (y) \right| = \left| \sum_ {| k | \leq M} c _ {k} (\Psi) e ^ {\imath k y} - \Psi (y) \right| = \left| \sum_ {| k | > M} c _ {k} (\Psi) e ^ {\imath k y} \right|
$$

![](images/page_20_image_0.jpg)

FIGURE 6.1. The approximation error

Now recall that the Fourier coefficients of  $\Psi \in C^{d}$  are bounded by (2.5), therefore

$$
\left| f _ {M} (y) - f (y) \right| \leq C _ {3 8} \cdot R \cdot M ^ {- d - 1}\tag{6.2}
$$

Let $\Theta \stackrel{\mathrm{def}}{=} \widetilde{\Phi} - \Phi$ denote the "singular error function" (see Figure 6.1 on page 21). Then the second term can be written as:

$$
\left| \widetilde {f} (y) - f _ {M} (y) \right| = \left| \sum_ {| k | \leq M} \left(c _ {k} (\Phi) - c _ {k} (\widetilde {\Phi})\right) e ^ {i k y} + \left(\widetilde {\Phi} (y) - \Phi (y)\right) \right| = \left| \sum_ {| k | \leq M} c _ {k} (\Theta) e ^ {i k y} - \Theta (y) \right|
$$

Write

$$
\begin{array}{r l} \widetilde {\xi} _ {j} = \xi_ {j} + \alpha (M) & | \alpha (M) | \leq F _ {\alpha} (A ^ {*}, A ^ {* *}, \widehat {R ^ {*}}) \cdot M ^ {- d - 2} \\ \widetilde {A} _ {l, j} = A _ {l, j} + \beta_ {l} (M) & | \beta_ {l} (M) | \leq F _ {\beta} (A ^ {*}, A ^ {* *}, \widehat {R ^ {*}}) \cdot M ^ {l - d - 1} \end{array}
$$

where  $F_{\alpha}$  and  $F_{\beta}$  are provided by Theorem 5.2. For every  $\epsilon < r$ , we define

$$
U _ {l, \epsilon} (y) \stackrel {\text {def}} {=} V _ {l} (y; \xi_ {j} + \epsilon) - V _ {l} (y; \xi_ {j})
$$

Using the formula (2.1) we therefore have

$$
\begin{array}{l} \Theta (y) = \sum_ {j = 1} ^ {K} \sum_ {l = 0} ^ {d} \left\{\widetilde {A} _ {l, j} V _ {l} (y; \widetilde {\xi} _ {j}) - A _ {l, j} V _ {l} (y; \xi_ {j}) \right\} = \sum_ {j = 1} ^ {K} \sum_ {l = 0} ^ {d} \left\{(A _ {l, j} + \beta_ {l} (M)) (V _ {l} (y; \xi_ {j}) + U _ {l, \alpha (M)} (y)) - A _ {l, j} V _ {l} (y; \xi_ {j}) \right\} \\ = \underbrace {\sum_ {j = 1} ^ {K} \sum_ {l = 0} ^ {d} \beta_ {l} (M) V _ {l} (y ; \xi_ {j})} _ {\stackrel {{\text {def}}} {{=}} Z (y)} + \underbrace {\sum_ {j = 1} ^ {K} \sum_ {l = 0} ^ {d} \widetilde {A} _ {l , j} U _ {l , \alpha (M)} (y)} _ {\stackrel {{\text {def}}} {{=}} W (y)} \end{array}
$$

and so

$$
\left| \widetilde {f} (y) - f _ {M} (y) \right| \leq \left| \sum_ {| k | > M} c _ {k} (Z) e ^ {\imath k y} \right| + \left| \sum_ {| k | <   M} c _ {k} (W) e ^ {\imath k y} - W (y) \right|\tag{6.3}
$$

The functions $V_{l}$ belong to $C^{l}$, and therefore by the well-known estimate (see also (1.1)), there exist constants $S_{l}$ such that

$$
\left| \sum_ {| k | > M} c _ {k} (V _ {l}) e ^ {\imath k y} \right| \leq S _ {l} \cdot M ^ {- l}
$$

and therefore

$$
\left| \sum_ {| k | > M} c _ {k} (Z) e ^ {\imath k y} \right| \leq C _ {3 9} \cdot F _ {\beta} \cdot M ^ {- d - 1}\tag{6.4}
$$

Let us now investigate $W(y)$. Let $L$ denote an upper bound for the magnitudes of the jumps:

$$
\left| A _ {l, j} \right| <   L \quad j = 1, \dots , K; \quad l = 0, 1, \dots , d _ {1}
$$

Clearly the functions $U_{l,\epsilon}(y)$ satisfy:

(1) Since $y \in \mathbf{D}_{\mathbf{r}}$, then $|U_{l,\epsilon}(y)| \leq C_{40}\epsilon$ for some absolute constant $C_{40}$. This bound can be obtained by just Taylor-expanding the functions $V_{l}(y; \xi_{j} + \epsilon)$ at $\epsilon = 0$. In particular for $\epsilon = \alpha(M)$ we have

$$
\left| W (y) \right| \leq \sum_ {j = 1} ^ {K} \sum_ {l = 0} ^ {d} \left| \widetilde {A} _ {l, j} \right| \left| U _ {l, \alpha (M)} (y) \right| \leq C _ {4 1} \cdot L \cdot F _ {\alpha} \cdot M ^ {- d - 2}\tag{6.5}
$$

(2) In the “no man’s land” of length  $\alpha(M)$  between  $\xi_{j}$  and  $\widetilde{\xi}_{j}$ ,  $U_{l,\epsilon}$  is bounded by  $C_{42} \cdot L$ . Furthermore, as we have just seen, in the flat regions  $U_{l,\alpha(M)}$  is bounded by  $C_{40}F_{\alpha}M^{-d-2}$ . Therefore the Fourier coefficients of W are certainly bounded by

$$
\left| c _ {k} (W) \right| \leq C _ {4 3} \cdot L \cdot F _ {\alpha} \cdot M ^ {- d - 2}
$$

and so

$$
\left| \sum_ {| k | <   M} c _ {k} (W) e ^ {i k y} \right| \leq C _ {4 4} \cdot L \cdot F _ {\alpha} \cdot M ^ {- d - 1}\tag{6.6}
$$

Combining (6.1), (6.2), (6.3), (6.4), (6.5) and (6.6) completes the proof.

## 7. NUMERICAL RESULTS

In this section we present results of various numerical simulations whose primary goal is to validate the asymptotic accuracy predictions for large M. We have used a straightforward implementation and made no attempt to optimize it further. In particular, the Fourier coefficients are assumed to be known with arbitrary precision (this is important for the localization, see below).

7.1. Recovery of a single jump. Given $d, d_1$ and $M$, a piecewise function with one discontinuity is generated according to the formula

$$
f (x) = \sum_ {l = 0} ^ {d _ {1}} A _ {l} V _ {l} (x; \xi) + \sum_ {k = - M} ^ {M} f _ {k} e ^ {\imath k x}
$$

where the numbers $\xi \in [-\pi, \pi], \{A_l \in \mathbb{R}\}_{l=0}^{d_1}$ and $\{f_k \in \mathbb{C}\}_{k=-M}^M$ are chosen at random, such that $f_k \sim k^{-d_1 - 2}$ and $f_{-k} = \bar{f}_k$. The Fourier coefficients are calculated with the exact formula

$$
c _ {k} (f) = \frac {\mathrm{e} ^ {- \imath k \xi}}{2 \pi} \sum_ {l = 0} ^ {d _ {1}} \frac {A _ {l}}{(\imath k) ^ {l + 1}} + f _ {k}
$$

These coefficients are then passed to the reconstruction routine for a single jump, of order d. This routine implements Algorithm 3.2 in a standard MATLAB environment with double-precision calculations.

The following experiments were carried out:

(1) Keeping $d$ and $d_{1}$ fixed, compare the accuracy of recovering the jump location and all the jump magnitudes for different values of $M$. The results can be seen in Figure 7.1 on page 23. We also plot the distribution of roots of the corresponding polynomials $q_{M}^{d}(z)$ - compare with Figure 4.1 on page 15.

(2) Keeping $d_{1}$ fixed, compare the accuracy for different reconstruction orders $d = 1, \ldots, d_{1}$. The results are presented in Figure 7.2 on page 23.

(3) Keeping the reconstruction order $d$ fixed, compare the accuracy for different smoothness values $d_{1}$. The results are presented in Figure 7.3 on page 23.

The optimality of $d = \frac{d_1}{2} - 1$, as well as the asymptotic order of convergence, are clearly seen to fit the theoretical predictions. The instability and eventual breakup of the measured accuracy for large values of $M$ is due to the finite-precision calculations.

![](images/page_22_chart_0.jpg)

(A) Accuracy of reconstruction with $d = 3$ and $d_{1} = 11$, as a function of $M$.

![](images/page_22_chart_2.jpg)

(B) The roots of $q_{M}^{d}(z)$

FIGURE 7.1. Reconstruction of a single jump

![](images/page_22_chart_5.jpg)

(A) $d_{1} = 8$

![](images/page_22_chart_7.jpg)

(B) $d_{1} = 12$

FIGURE 7.2. Dependence of the accuracy on the order with fixed smoothness, with increasing M.

![](images/page_22_chart_10.jpg)

(A) d = 3

![](images/page_22_chart_12.jpg)

(B) $d = 4$

FIGURE 7.3. Dependence of the accuracy on the smoothness with fixed order, with increasing M.

![](images/page_23_chart_0.jpg)

FIGURE 7.4. Localization: accuracy of recovering the jump. The predicted accuracy  $M^{-d-2}$  is drawn for comparison.

7.2. Localization. We have restricted ourselves to the following simplified setting: the function has two jumps at $\xi_1 = 0$ and $\xi_2 = 3$, and we localize the jump at the origin by a bump having width $\frac{8}{3}$ around the initial approximation $\widehat{\xi_1} = \frac{1}{40}$. The explicit formulas for the Fourier coefficients of the bump are derived in Appendix C. We have used Mathematica in order to carry out the computations with arbitrary precision.

The results can be seen in Figure 7.4 on page 24. Localization convergence can clearly be seen here, although it starts from very large coefficients.

## 8. Discussion

In this paper we have demonstrated that nonlinear Fourier reconstruction of piecewise-smooth functions can achieve accuracy with asymptotic order of at least half the order of smoothness. As indicated by our theoretical results as well as the numerical simulations, a reconstruction method whose order is more than half the order of smoothness becomes less accurate. So it appears that the algebraic approach has certain limitations, and the interesting question is whether these limitations are inherent or superficial. We hope that our results may provide a clue towards obtaining sharp upper bounds.

In addition, it seems that Eckhoff's conjecture is false as stated in [14], namely that the jumps of a piecewise-smooth $C^d$ function can be reconstructed with accuracy $k^{-d - 2}$. Using a method of highest possible order doesn't take into account the stiffness of the problem. In fact, it can be shown that the Lipschitz constant of the solution map $\{c_k(f)\}_{k=M}^{M+d+1} \to \{\xi_j, A_{l,j}\}$ of order $d$ is proportional to $M^d$. We plan to present these results elsewhere.

Hopefully, our analysis can be related to the algebraic reconstruction schemes of Kvernadze and Banerjee&Geer as well.

We would like to point out the connection of the algebraic system (2.2) as well as the well-known Prony system of equations (D.1) (which plays a central role in many branches of mathematics - see [33] and [28]) to other recent nonlinear reconstruction methods in Signal Processing, in particular: finite rate of innovation techniques [35, 12], reconstruction of shapes from moments [24, 21] and piecewise $D$-finite moment inversion [6, 7]. We therefore hope that our results can be extended to these subjects as well.

## REFERENCES

[1] M. Abramowitz and I.A. Stegun. Handbook of mathematical functions: with formulas, graphs, and mathematical tables. 1965.

[2] F. Arandiga, A. Cohen, R. Donat, and N. Dyn. Interpolation and approximation of piecewise smooth functions. SIAM Journal on Numerical Analysis, 43:41, 2005.

[3] N.S. Banerjee and J.F. Geer. Exponentially accurate approximations to periodic Lipschitz functions based on Fourier series partial sums. Journal of Scientific Computing, 13(4):419–460, 1998.

[4] A. Barkhudaryan, R. Barkhudaryan, and A. Poghosyan. Asymptotic behavior of Eckhoff's method for Fourier series convergence acceleration. Analysis in Theory and Applications, 23(3):228–242, 2007.

[5] P. Barone and R. March. Reconstruction of a Piecewise Constant Function from Noisy Fourier Coefficients by Padé Method. SIAM Journal on Applied Mathematics, 60(4):1137-1156, 2000.

[6] D. Batenkov. Moment inversion problem for piecewise D-finite functions. Inverse Problems, 25(10):105001, October 2009.

[7] D. Batenkov, N. Sarig, and Y. Yomdin. An “algebraic” reconstruction of piecewise-smooth functions from integral measurements. Proc. of Sampling Theory and Applications (SAMPTA), 2009. Arxiv preprint arXiv:0901.4659.

[8] R. Bauer. Band filters for determining shock locations. PhD thesis, Department of Applied Mathematics, Brown University, Providence, RI, 1995.

[9] B. Beckermann, A.C. Matos, and F. Wielonsky. Reduction of the Gibbs phenomenon for smooth functions with jumps by the  $\varepsilon$ -algorithm. Journal of Computational and Applied Mathematics, 219(2):329–349, 2008.

[10] John P. Boyd. Acceleration of algebraically-converging fourier series when the coefficients have series in powers of 1/n. Journal of Computational Physics, 228(5):1404 - 1411, 2009.

[11] C. Brezinski. Extrapolation algorithms for filtering series of functions, and treating the Gibbs phenomenon. Numerical Algorithms, 36(4):309-329, 2004.

[12] P.L. Dragotti, M. Vetterli, and T. Blu. Sampling Moments and Reconstructing Signals of Finite Rate of Innovation: Shannon meets Strang-Fix. IEEE Transactions on Signal Processing, 55(5):1741, 2007.

[13] T.A. Driscoll and B. Fornberg. A Padé-based algorithm for overcoming the Gibbs phenomenon. Numerical Algorithms, 26(1):77–92, 2001.

[14] K.S. Eckhoff. Accurate reconstructions of functions of finite regularity from truncated Fourier series expansions. Mathematics of Computation, 64(210):671-690, 1995.

[15] K.S. Eckhoff. On a high order numerical method for functions with singularities. Mathematics of Computation, 67(223):1063-1088, 1998.

[16] S. Elaydi. An Introduction to Difference Equations. Springer, 2005.

[17] B. Ettinger, N. Sarig, and Y. Yomdin. Linear versus Non-Linear Acquisition of Step-Functions. Journal of Geometric Analysis, 18(2):369–399, 2008.

[18] W. Gautschi. Norm estimates for inverses of Vandermonde matrices. Numerische Mathematik, 23(4):337-347, 1974.

[19] A. Gelb and D. Cates. Segmentation of Images from Fourier Spectral Data. Commun. Comput. Phys., 5:326–349, 2009.

[20] A. Gelb and E. Tadmor. Detection of edges in spectral data. Applied and computational harmonic analysis, 7(1):101, 1999.

[21] G.H. Golub, P. Milanfar, and J. Varah. A Stable Numerical Method for Inverting Shape from Moments. SIAM Journal on Scientific Computing, 21(4):1222–1243, 2000.

[22] D. Gottlieb and C.W. Shu. On the Gibbs phenomenon and its resolution. SIAM Review, pages 644–668, 1997.

[23] C. Guilpin, J. Gacougnolle, and Y. Simon. The  $\varepsilon$ -algorithm allows to detect Dirac delta functions. Applied Numerical Mathematics, 48(1):27–40, 2004.

[24] B. Gustafsson, C. He, P. Milanfar, and M. Putinar. Reconstructing planar domains from their moments. Inverse Problems, 16(4):1053–1070, 2000.

[25] L.V. Kantorovich and V.I. Krylov. Approximate Methods of Higher Analysis. Fizmatgiz, Moscow, 1962.

[26] G. Kvernadze. Approximating the jump discontinuities of a function by its Fourier-Jacobi coefficients. Mathematics of Computation, 73(246):731-752, 2004.

[27] Yaron Lipman and David Levin. Approximating piecewise-smooth functions. IMA J Numer Anal, page drn087, 2009.

[28] Y.I. Lyubich. The Sylvester-Ramanujan System of Equations and The Complex Power Moment Problem. The Ramanujan Journal, 8(1):23–45, 2004.

[29] HN Mhaskar and J. Prestin. Polynomial frames for the detection of singularities. In Wavelet Analysis and Multiresolution Methods: Proceedings of the Conference Held at University of Illinois at Urbana-Champaign, Illinois, page 273. CRC, 2000.

[30] I.P. Natanson. Constructive Function Theory (in Russian). Gostekhizdat, 1949.

[31] L. Plaskota and G.W. Wasilkowski. The power of adaptive algorithms for functions with singularities. Journal of Fixed Point Theory and Applications, 6(2):227-248, 2009.

[32] R. Prony. Essai experimental et analytique. J. Ec. Polytech. (Paris), 2:24–76, 1795.

[33] N. Sarig and Y. Yomdin. Signal Acquisition from Measurements via Non-Linear Models. Mathematical Reports of the Academy of Science of the Royal Society of Canada, 29(4):97–114, 2008.

[34] G. Szegő. Orthogonal Polynomials. American Mathematical Society, 1975.

[35] M. Vetterli, P. Marziliano, and T. Blu. Sampling signals with finite rate of innovation. IEEE Transactions on Signal Processing, 50(6):1417-1428, 2002.

[36] J. Vindas. Local Behavior of Distributions and Applications. PhD thesis, 2009.

[37] M. Wei, A.G. Martínez, and A.R. De Pierro. Detection of edges from spectral data: New results. Applied and Computational Harmonic Analysis, 22(3):386–393, 2007.

[38] J.H. Wilkinson. Rounding errors in algebraic processes. Dover Pubns, 1994.

[39] A. Zygmund. Trigonometric Series. Vols. I, II. Cambridge University Press, New York, 1959.

## APPENDIX A. DISCRETE DIFFERENCE CALCULUS AND RELATED RESULTS

In this appendix we provide proofs of several combinatorial auxiliary results.

Let E denote the discrete “shift” operator in k, i.e. for every function  $g(k): \mathbb{R} \to \mathbb{R}$  we have

$$
\operatorname{E} g (k) \stackrel {\text { def }} {=} g (k + 1)
$$

Furthermore, let $\Delta$ denote the discrete difference operator, i.e. $\Delta = E - I$ where $I$ is the identity operator. Then by the binomial theorem we have

$$
\Delta^ {d} g (k) = (\mathbb {E} - \mathrm{I}) ^ {d} g (k) = (- 1) ^ {d} \sum_ {j = 0} ^ {d} (- 1) ^ {j} {\binom {d} {j}} g (k + j)\tag{A.1}
$$

Lemma A.1. Let  $p(k) = a_{0}k^{n} + a_{1}k^{n-1} + \cdots + a_{n}$  be a polynomial of degree n. Then

$$
\begin{array}{c} \Delta^ {n} p (k) = a _ {0} n! \\ \Delta^ {n + 1} p (k) = 0 \end{array}
$$

Proof. See e.g. [16].

Now assume that $g(k): \mathbb{R}^+ \to \mathbb{R}$ is a given function. Let us perform a change of variable $y = \frac{1}{k}$, and define $G(y) \stackrel{\mathrm{def}}{=} g\left(\frac{1}{y}\right) = g(k)$. With this notation, we have

$$
\Delta g (k) = g (k + 1) - g (k) = g \left(\frac {1}{y} + 1\right) - g \left(\frac {1}{y}\right) = G \left(\frac {y}{1 + y}\right) - G (y)
$$

We subsequently define the "dual" operator $\mathcal{D}$ as:

$$
\mathcal {D} \left\{G (y) \right\} \stackrel {\mathrm{def}} {=} G \left(\frac {y}{1 + y}\right) - G (y)
$$

The operator D has an interesting property of “killing” the lowest-order Taylor coefficient at 0.

Proposition A.2. Let $H(y)$ be analytic at $y = 0$, such that $H(y) = h_m y^m + h_{m+1} y^{m+1} + \ldots$. Then for $n \in \mathbb{N}$, the function $\mathcal{D}^n\{H(y)\}$ is analytic at 0 with Taylor expansion

$$
\mathcal {D} ^ {n} \left\{H (y) \right\} = h _ {m + n} ^ {*} y ^ {m + n} + h _ {m + n + 1} ^ {*} y ^ {m + n + 1} + \dots
$$

Proof. The proof is by induction on $n$. The basis $n = 0$ is given. Assuming that $U(y) = \mathcal{D}^{n-1}\{H(y)\}$ is analytic at 0 and $U(y) = u_{m+n-1}^* y^{m+n-1} + u_{m+n-1}^* y^{m+n-1} + \ldots$, consider the function $\mathcal{D}\{U(y)\} = \mathcal{D}^n\{H(y)\}$. Let $z = \frac{y}{1+y}$, and so for $|y| < 1$ we have

$$
z (y) = y \left(1 - y + y ^ {2} + \dots\right) = y - y ^ {2} + \dots
$$

Making the analytic change of coordinates $y \to z(y)$ we conclude that the Taylor expansion of $U(z(y))$ at the origin is

$$
U (z (y)) = u _ {m + n - 1} ^ {*} z ^ {m + n - 1} + \dots = u _ {m + n - 1} ^ {*} y ^ {m + n - 1} + \dots
$$

That is, the leading coefficient is the same as in the Taylor expansion of $U(y)$. Therefore

$$
\begin{array}{r l} \mathcal {D} \left\{U (y) \right\} & = U (z) - U (y) \\ & = u _ {m + n} ^ {* *} y ^ {m + n} + u _ {m + n + 1} ^ {* *} y ^ {m + n + 1} + \dots \end{array}
$$

This expansion holds in some neighborhood of the origin.

Lemma A.3. Let $l, d \in \mathbb{N}$. Then there exist positive constants $C_{45}, K_{11}$ such that for all $k > K_{11}$

$$
\left| \sum_ {j = 0} ^ {d} (- 1) ^ {j} {\binom {d} {j}} \frac {1}{(k + j) ^ {l}} \right| <   \frac {C _ {4 5}}{k ^ {d + l}}
$$

Proof. Let $g(k) = \frac{1}{k^l}$. It is easy to check (see (A.1)) that

$$
A _ {l, d} (k) \stackrel {\text { def }} {=} \sum_ {j = 0} ^ {d} (- 1) ^ {j} \binom {d} {j} \frac {1}{(k + j) ^ {l}} = \Delta^ {d} g (k)
$$

The proof of the claim is in two steps. First, we shall develop the expression $A_{l,d}(k)$ into power series in $\frac{1}{k}$ converging for sufficiently large $k$. Then, based on this representation we shall establish the required bound.

Let $y = \frac{1}{k}$. According to our notation, let $G(y) = g\left(\frac{1}{y}\right) = g(k)$ and so $A_{l,d}(k) = \mathcal{D}^d\{G(y)\} \stackrel{\text{def}}{=} F(y)$. Furthermore, for all $j = 0, 1, \ldots$ we have

$$
k + j = \frac {1}{y} + j = \frac {1 + j y}{y}
$$

and so

$$
F (y) = \sum_ {j = 0} ^ {d} (- 1) ^ {j} \binom {d} {j} G \left(\frac {y}{1 + j y}\right)
$$

Substituting $G(y) = y^l$, we conclude that $F(y)$ is a real analytic function of $y$ in the disk $|y| < \frac{1}{d}$, and so it can be written as a converging power series

$$
F (y) = \sum_ {i = 0} ^ {\infty} f _ {i} y ^ {i}
$$

Applying Proposition A.2 to  $G(y)$  we conclude that  $f_{0} = \cdots = f_{l+d-1} = 0$ . Therefore the expansion

$$
A _ {l, d} (k) = \sum_ {i = l + d} ^ {\infty} \frac {f _ {i}}{k ^ {i}}\tag{A.2}
$$

holds for k > d.

Let us now estimate the magnitude of the coefficients $f_{i}$. Since (A.2) is valid for $k = d + 1$, then there exists a constant $C_{46}$ such that $\left|f_{i}(d + 1)^{-i}\right| < C_{46}$ for all $i\in \mathbb{N}$ and therefore

$$
\left| f _ {i} \right| <   C _ {4 6} (d + 1) ^ {i}
$$

But then for arbitrary $k \geq d + 2$ we have

$$
\begin{array}{l} \left| A _ {l, d} (k) \right| = \left| \sum_ {i = 0} ^ {\infty} \frac {f _ {l + d + i}}{k ^ {l + d + i}} \right| <   \frac {C _ {4 6} (d + 1) ^ {l + d}}{k ^ {l + d}} \sum_ {i = 0} ^ {\infty} \frac {(d + 1) ^ {i}}{k ^ {i}} \\ \leq \frac {C _ {4 6} (d + 1) ^ {l + d}}{k ^ {l + d}} \cdot \frac {1}{1 - \frac {d + 1}{d + 2}} \leq \frac {C _ {4 5}}{k ^ {l + d}} \end{array}
$$

Lemma A.4. Let $\omega \in \mathbb{C}$, $a_0, \ldots, a_n \in \mathbb{C}$ and $n, k \in \mathbb{N}$. Denote $b_k \stackrel{def}{=} \omega^k \cdot (a_0 + a_1 k + \ldots a_n k^n)$. Then

$$
\sum_ {j = 0} ^ {n + 1} (- 1) ^ {j} \binom {n + 1} {j} b _ {k + j} \omega^ {n + 1 - j} \equiv 0
$$

Proof. Denote

$$
p (k) \stackrel {\mathrm{def}} {=} a _ {0} + a _ {1} k + \dots a _ {n} k ^ {n}
$$

Then we rewrite the given expression as

$$
\begin{array}{c} \sum_ {j = 0} ^ {n + 1} (- 1) ^ {j} \binom {n + 1} {j} b _ {k + j} \omega^ {n + 1 - j} = \sum_ {j = 0} ^ {n + 1} (- 1) ^ {j} \binom {n + 1} {j} p (k + j) \omega^ {n + k + 1} \\ = (- 1) ^ {d + 1} \omega^ {n + k + 1} \Delta^ {n + 1} p (k) \\ _ {(L e m m a A. 1)} = 0 \end{array}
$$

The claim is therefore proved.

Lemma A.5. Let

$$
\mathcal {F} (d, t, s) \stackrel {{d e f}} {{=}} \sum_ {j = s} ^ {d + 1} (- 1) ^ {j} \binom {j} {s} \binom {d + 1} {j} j ^ {d - t}
$$

The following statements are true for all $s = 0,1,\ldots ,d + 1$:

(1) If $t \geq s$ then $\mathcal{F}(d, t, s) = 0$

$$
(2) \mathcal {F} (d, s - 1, s) = (- 1) ^ {d + 1} (d + 1 - s)! \binom {d + 1} {s} \tag {2}
$$

Proof. Let $\alpha \stackrel{\mathrm{def}}{=} d - s$ and $\beta \stackrel{\mathrm{def}}{=} d - t$. Now

$$
\begin{array}{l} \mathcal {F} (d, t, s) = \sum_ {j = 0} ^ {d + 1 - s} (- 1) ^ {j + s} \binom {j + s} {s} \binom {d + 1} {j + s} (j + s) ^ {d - t} \\ \qquad = \sum_ {j = 0} ^ {\alpha + 1} (- 1) ^ {j + s} \frac {(j + s) !}{s ! j !} \cdot \frac {(d + 1) !}{(j + s) ! (d + 1 - j - s) !} (j + s) ^ {\beta} \\ \qquad = (- 1) ^ {d - \alpha} \sum_ {j = 0} ^ {\alpha + 1} (- 1) ^ {j} \frac {(d + 1) !}{(d - \alpha) ! j ! (\alpha + 1 - j) !} (j + s) ^ {\beta} \cdot \frac {(\alpha + 1) !}{(\alpha + 1) !} \\ \qquad = (- 1) ^ {d - \alpha} \binom {d + 1} {\alpha + 1} \sum_ {j = 0} ^ {\alpha + 1} (- 1) ^ {j} \binom {\alpha + 1} {j} (j + s) ^ {\beta} \end{array}
$$

Now let $g(s) \stackrel{\mathrm{def}}{=} s^{\beta}$ be a polynomial of degree $\beta$. By (A.1), the above expression can be rewritten as

$$
\mathcal {F} (d, t, s) = (- 1) ^ {d + 1} \binom {d + 1} {\alpha + 1} \Delta^ {\alpha + 1} g (s)\tag{A.3}
$$

(1) Assume $t \geq s$. Then $\alpha + 1 \geq \beta + 1$, and so by Lemma A.1 we have $\Delta^{\alpha + 1} g(s) = 0$. This completes the proof of the first part.

(2) Let $t = s - 1$. By Lemma A.1 we have $\Delta^{\alpha + 1}g(s) = (\alpha + 1)!$ and so by (A.3)

$$
\mathcal {F} (d, t, s) = (- 1) ^ {d + 1} \binom {d + 1} {\alpha + 1} (\alpha + 1)! = (- 1) ^ {d + 1} (d - s + 1)! \binom {d + 1} {s}
$$

This completes the proof of the second part.

## APPENDIX B. MISCELLANEOUS AUXILIARY RESULTS

Theorem B.1 (Rouche's theorem). Let the polynomial $q(z) \in \mathbb{C}[z]$ be a sum $q(z) = p(z) + e(z)$. Let $z_0$ be a simple zero of $p(z)$. If there exists $\rho \in \mathbb{R}^+$ such that

$$
\left| p (z) \right| > \left| e (z) \right| \quad \forall z \in \partial B _ {\rho} \left(z _ {0}\right)
$$

then $q(z)$ has a simple zero inside $B_{\rho}(z_0)$.

Lemma B.2. Let there be given a sequence of polynomials  $P_{k}(z):\mathbb{C}\to\mathbb{C}$  and a point  $z_{0}\in\mathbb{C}$  such that

(1) $P_{k}(z_{0}) = 0$ for all $k\in \mathbb{N}$;

(2) $\left|P_{k}^{\prime}(z_{0})\right| \geq C_{47}$ for all $k \in \mathbb{N}$ and some constant $C_{47}$ independent of $k$;

(3) For every fixed $k$ the following inequality holds for all $z \in B_{k-1}(z_0)$

$$
\left| P _ {k} ^ {\prime \prime} (z) \right| \leq C _ {4 8} k
$$

where $C_{48}$ is a constant independent of $k$.

Let $\rho(k): \mathbb{N} \to \mathbb{R}$ satisfy

$$
0 <   \rho (k) <   \min \left(\frac {1}{k}, \frac {C _ {4 7}}{C _ {4 8} k}\right)
$$

Then there exists a constant $C_{49}$ independent of $\rho(k)$ such that for all $k$, the following holds for every $z \in \partial B_{\rho(k)}(z_0)$:

$$
\left| P _ {k} (z) \right| \geq C _ {4 9} \rho (k)
$$

Proof. Let us write the truncated Taylor expansion of  $P_{k}$  around  $z_{0}$  with remainder in Lagrange form:

$$
P _ {k} \left(z _ {0} + \rho (k) e ^ {\imath \theta}\right) = P _ {k} (z _ {0}) + \underbrace {P _ {k} ^ {\prime} (z _ {0}) \rho (k) e ^ {\imath \theta}} _ {= E _ {1}} + \underbrace {\frac {P _ {k} ^ {\prime \prime} (\xi)}{2} \rho^ {2} (k) e ^ {2 \imath \theta}} _ {= E _ {2}}
$$

for some $\xi \in B_{\rho}(z_0)$. Now since $\rho(k) \leq \frac{1}{k}$ we have

$$
\begin{array}{l} {| E _ {1} | \ge C _ {4 7} \rho (k)} \\ {| E _ {2} | \le \frac {C _ {4 8} k \rho^ {2} (k)}{2}} \end{array}
$$

On the other hand,

$$
\begin{array}{r} \rho (k) \leq \frac {C _ {4 7}}{C _ {4 8} k} \\ \frac {C _ {4 8} k \rho^ {2} (k)}{2} \leq \frac {C _ {4 7} \rho (k)}{2} \end{array}
$$

Therefore $\frac{|E_1|}{2} \geq |E_2|$ and so by taking $C_{49} \stackrel{\mathrm{def}}{=} \frac{C_{47}}{2}$ we have $|P_k(z)| \geq C_{49} \rho(k)$.

Proposition B.3. Let $n \in \mathbb{N}$ be given. Then for $|x| < \frac{3}{n + 2}$ the following estimate holds:

$$
(1 + x) ^ {- n} = 1 - n x + \frac {n (n + 1)}{2} x ^ {2} R _ {5} (x) \quad \text {where} \quad | R _ {5} (x) | <   \frac {1}{1 - \frac {x (n + 2)}{3}}
$$

In general, for approximation of order $d$, we have for $|x| < \frac{d + 2}{n + d + 1}$

$$
(1 + x) ^ {- n} = 1 - n x + \frac {n (n + 1)}{2} x ^ {2} + \dots + (- 1) ^ {d} \frac {n \times \cdots \times (n + d - 1)}{d !} x ^ {d} + (- 1) ^ {d + 1} \frac {n \times \cdots \times (n + d)}{(d + 1) !} x ^ {d + 1} R _ {6} (x)
$$

where

$$
\left| R _ {6} (x) \right| <   \frac {1}{1 - \frac {(n + d + 1)}{d + 2} x}
$$

Proof. Standard majorization of the Taylor series tail by a geometric series.

## APPENDIX C. EXPLICIT CONSTRUCTION OF A BUMP

In this appendix we present an explicit construction of the bump function which we used in our numerical simulations. We also derive an explicit bound for the size of its Fourier coefficients, to be used in the proof of localization accuracy.

Let there be given two parameters $t$ and $E$ with $2E > t$, together with the point $\xi \in \mathbb{R}$. Our goal is to build a function $g = g_{E,t}(x; \xi)$ which satisfies the following conditions:

(G1) $g \equiv 0$ for $x \notin [\xi - E, \xi + E]$;

(G2) $g \equiv 1$ for $x \in \left[\xi - \frac{t}{2}, \xi + \frac{t}{2}\right]$;

(G3)  $g \in C^{\infty}(\mathbb{R})$ ;

(G4) the Fourier coefficients of g decay as rapidly as possible.

The idea is to take a standard  $C^{\infty}$  mollifier, scale it and convolve with a box function.

We define two new parameters: the scaling factor $s$ and the width of the box $r$. Note that our construction implies $r \geq 2s$, because otherwise the result of the convolution will not have a flat segment in the middle.

Let us therefore take the standard  $C^{\infty}$  mollifier

$$
\Psi (x) = \left\{ \begin{array}{l l} \mathbf {e} ^ {- 1 / (1 - x ^ {2})} & \text {for |x| <   1} \\ 0 & \text {otherwise} \end{array} \right.
$$

and scale it between -s and s for some s > 0:

$$
m _ {s} (x) = \frac {1}{s \Delta} \Psi \left(\frac {x}{s}\right)
$$

where

$$
\Delta = \frac {1}{s} \int_ {- s} ^ {s} \Psi \left(\frac {x}{s}\right) \mathrm{d} x = \int_ {- 1} ^ {1} \Psi (y) \mathrm{d} y \sim 0. 4 4 3 9 9 4
$$

Now we take a box function centered at  $\xi$ , having width r:

$$
b _ {r} (x; \xi) = \left\{ \begin{array}{l l} 1 & \text {for - \frac {r}{2} \leq x- \xi\leq \frac {r}{2}} \\ 0 & \text {otherwise} \end{array} \right.
$$

Finally we convolve the two and get a smooth bump:

$$
g = g _ {r, s} (x; \xi) = b _ {r} (x; \xi) * m _ {s} (x) = \frac {1}{s \Delta} \int_ {\xi - \frac {r}{2}} ^ {\xi + \frac {r}{2}} \Psi \left(\frac {x - t}{s}\right) d t
$$

The new parameters s, r should be compatible with the original E, t. In particular, we want to have a strip of width t in the center, and the extent of the whole bump should not exceed E. Therefore we have the following compatibility conditions:

$$
\begin{array}{r} s + \frac {t}{2} <   \frac {r}{2} \\ 2 s + \frac {r}{2} <   E \end{array}\tag{C.1}
$$

The function $g$ so constructed clearly satisfies conditions $(G1) - (G3)$ above. Let us now maximize the decay of its Fourier coefficients. By definition:

$$
c _ {k} (g) = \frac {1}{2 \pi s \Delta} \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {- \imath k x} \left\{\int_ {\xi - \frac {r}{2}} ^ {\xi + \frac {r}{2}} \Psi \left(\frac {x - t}{s}\right) \mathrm{d} t \right\} \mathrm{d} x
$$

Notice first that $\Psi(z)$ is zero outside the region $-1 \leq z \leq 1$, therefore we can make the change of variables $z \to t - x, t \to t$ and rewrite the integral as

$$
c _ {k} (g) = \frac {1}{2 \pi s \Delta} \int_ {- s} ^ {s} e ^ {\imath k z} \Psi \left(\frac {z}{s}\right) \left\{\int_ {\xi - \frac {r}{2}} ^ {\xi + \frac {r}{2}} e ^ {- \imath k t} d t \right\} d z
$$

![](images/page_29_chart_0.jpg)

FIGURE C.1. The construction of the bump

So now the two integrals are completely separated. Explicit calculation gives

$$
\int_ {\xi - \frac {r}{2}} ^ {\xi + \frac {r}{2}} \mathrm{e} ^ {- \imath k t} \mathrm{d} t = - \frac {\imath \mathrm{e} ^ {- \frac {1}{2} \imath k (r + 2 \xi)} \left(- 1 + \mathrm{e} ^ {\imath k r}\right)}{k}
$$

Now we scale back: $z = sy$ and obtain the explicit formula

$$
\begin{array}{r} c _ {k} (g) = - \frac {\imath \mathrm{e} ^ {- \frac {1}{2} \imath k (r + 2 \xi)} (- 1 + \mathrm{e} ^ {\imath k r})}{k} \cdot \frac {1}{2 \pi \Delta} \int_ {- 1} ^ {1} \mathrm{e} ^ {\imath k s y} \Psi (y) \mathrm{d} y \\ = - \frac {\imath \mathrm{e} ^ {- \frac {1}{2} \imath k (r + 2 \xi)} (- 1 + \mathrm{e} ^ {\imath k r})}{2 \pi \Delta k} c _ {- k s} (\Psi) \end{array}\tag{C.2}
$$

Finally we would like to determine the optimal values for $s$ and $r$ so that $|c_k(g)|$ decrease as rapidly as possible with $k \to \infty$. First note that since $\Psi \in C^\infty$, then for every $\alpha > 1$ there exists a constant $C_{50}(\alpha)$ such that

$$
\left| c _ {k} (\Psi) \right| \leq C _ {5 0} \cdot | k | ^ {- \alpha}
$$

The formula (C.2) suggests that we should take $s$ to be as large as possible. Applying the conditions (C.1) we get that the following values maximize $s$:

$$
\begin{array}{l} {s ^ {*} = \frac {1}{3} \left(E - \frac {t}{2}\right)} \\ {r ^ {*} = \frac {2}{3} (E + t)} \end{array}
$$

We have thus proved the following result:

Theorem C.1. Given $E, t$ with $2E > t$ and a point $\xi$, let $g_{E,t}(x; \xi)$ be the bump constructed above. Then it satisfies the conditions (G1) - (G4) such that for every $\alpha > 1$ there exists a constant $C_{51} = C_{51}(\alpha)$ such that for all $k \in \mathbb{N}$

$$
\left| c _ {k} \left(g _ {E, t}\right) \right| \leq C _ {5 1} \cdot (2 E - t) ^ {- \alpha} k ^ {- 1 - \alpha}
$$

## APPENDIX D. INITIAL ESTIMATES VIA PRONY'S METHOD

In this appendix we present a rigorous proof that the Eckhoff's method of order zero produces sufficiently accurate estimates of the jump locations $\{\xi_j\}$, to be used in Algorithm 5.1. Denote $\omega_{j} = \mathrm{e}^{-\imath \xi_{j}}$. For $d = 0$, the system (2.2) becomes

$$
\underbrace {\sum_ {j = 1} ^ {K} A _ {0 , j} \omega_ {j} ^ {k}} _ {= m _ {k}} \approx 2 \pi (\imath k) c _ {k} (f)\tag{D.1}
$$

(D.1) is a well-known system of equations which is sometimes called the Prony system ([33]) or Sylvester-Ramanujan system ([28]). The original method of solution (due to Baron de Prony, [32]) is to exploit the following fact.

Lemma D.1. The sequence  $\{m_{k}\}$  satisfies the recurrence relation with constant coefficients

$$
\sum_ {i = 0} ^ {K} m _ {k + i} q _ {i} = 0
$$

where $\{q_i\}$ are the coefficients of the polynomial

$$
Q (z) \stackrel {d e f} {=} \prod_ {j = 1} ^ {K} (z - \omega_ {j}) = \sum_ {i = 0} ^ {K} q _ {i} z ^ {i}
$$

Proof. We have $Q(\omega_j) = 0$ for all $j = 1, \ldots, K$. Therefore

$$
\sum_ {i = 0} ^ {K} q _ {i} m _ {k + i} = \sum_ {i = 0} ^ {K} q _ {i} \sum_ {j = 1} ^ {K} A _ {0, j} \omega_ {j} ^ {k + i} = \sum_ {j = 1} ^ {K} A _ {0, j} \omega_ {j} ^ {k} \sum_ {i = 0} ^ {K} q _ {i} \omega_ {j} ^ {i} = \sum_ {j = 1} ^ {K} A _ {0, j} \omega_ {j} ^ {k} Q (\omega_ {j}) = 0
$$

Corollary D.2. Let $q_{K} = 1$ for normalization. Then for all $k \in \mathbb{N}$ the coefficient vector $\{q_i\}_{i=0}^{K-1}$ is the solution of the linear system

$$
\underbrace {\left[ \begin{array}{c c c c} m _ {k} & m _ {k + 1} & \cdots & m _ {k + K - 1} \\ m _ {k + 1} & m _ {k + 2} & \cdots & m _ {k + K} \\ \vdots & \vdots & \vdots & \vdots \\ m _ {k + K - 1} & m _ {k + K} & \cdots & m _ {k + 2 K - 2} \end{array} \right]} _ {\stackrel {{d e f}} {{=}} H _ {k}} \times \left[ \begin{array}{c} q _ {0} \\ q _ {1} \\ \vdots \\ q _ {K - 1} \end{array} \right] = - \left[ \begin{array}{c} m _ {k + K} \\ m _ {k + K + 1} \\ \vdots \\ m _ {k + 2 K - 1} \end{array} \right]\tag{D.2}
$$

After this preparation, we can now describe the algorithm for obtaining initial estimates using Prony's method. Recall that our a-priori bounds are given by $J_{1}, J_{2}, J_{3}$ and $T$ - see Section 5.

Algorithm D.3. Let us be given the first $M + 2K - 1$ Fourier coefficients $c_k(f)$ of a function $f$ with $K$ unknown discontinuities $\{\xi_j\}_{j=1}^K$, which is continuously differentiable between these discontinuities. Denote the magnitudes of the jumps by $\{A_j\}_{j=1}^K$.

(1) Calculate the sequence

$$
r _ {k} = 2 \pi (\imath k) c _ {k} (f)
$$

(2) Solve the system

$$
\underbrace {\left[ \begin{array}{c c c c} r _ {M} & r _ {M + 1} & \cdots & r _ {M + K - 1} \\ r _ {M + 1} & r _ {M + 2} & \cdots & r _ {M + K} \\ \vdots & \vdots & \vdots & \vdots \\ r _ {M + K - 1} & r _ {M + K} & \cdots & r _ {M + 2 K - 2} \end{array} \right]} _ {\stackrel {{d e f}} {{=}} \widetilde {H _ {k}}} \times \left[ \begin{array}{c} \widetilde {q} _ {0} \\ \widetilde {q} _ {1} \\ \vdots \\ \widetilde {q} _ {K - 1} \end{array} \right] = - \left[ \begin{array}{c} r _ {M + K} \\ r _ {M + K + 1} \\ \vdots \\ r _ {M + 2 K - 1} \end{array} \right]\tag{D.3}
$$

(3) Take the estimated $\{\widetilde{\omega}_j\}$ to be the roots of the polynomial

$$
\widetilde {Q} (z) = z ^ {K} + \sum_ {i = 0} ^ {K - 1} \widetilde {q} _ {i} z ^ {i}
$$

and then set

$$
\widetilde {\xi} _ {j} = - \arg \widetilde {\omega} _ {j}
$$

Now we would like to analyze the accuracy of Algorithm D.3. First, we need to estimate the error in solving the system (D.3). We use standard result from numerical linear algebra.

Lemma D.4. Consider the linear system Ax = b and let  $x_{0}$  be the exact solution. Let this system be perturbed:

$$
(A + \Delta A) x = b + \Delta b
$$

and let  $x_{0} + \Delta x$  denote the exact solution of this perturbed system. Denote

$$
\delta x = \frac {| | \Delta x | |}{| | x _ {0} | |} \qquad \delta A = \frac {| | \Delta A | |}{| | A | |} \qquad \delta b = \frac {| | \Delta b | |}{| | b | |} \qquad \kappa = | | A | | | A ^ {- 1} | | (c o n d i t i o n n u m b e r)
$$

for some vector norm  $\|\cdot\|$  and the induced matrix norm. Then

$$
\delta x \leq \frac {\kappa}{1 - \kappa \cdot \delta A} (\delta A + \delta b)\tag{D.4}
$$

Proof. See e.g. [38].

Consider (D.3). The error in the right-hand side is given by (5.1). Therefore we now need to estimate the condition number of the matrix $H_{k}$. Although all the entries are bounded, it may still happen$^{2}$ that $\kappa(H_{k})$ is unbounded. Fortunately, this is not the case. To see this, we are going to factorize $H_{k}$ into a component which depends on $k$, and a component which doesn't.

Lemma D.5. Let  $V = V(\xi_{1}, \ldots, \xi_{K})$  denote the Vandermonde matrix on the nodes  $\{\omega_{j}\}$ , i.e.

$$
V = \left[ \begin{array}{c c c c} 1 & 1 & \ldots & 1 \\ \omega_ {1} & \omega_ {2} & \ldots & \omega_ {K} \\ \vdots & \vdots & \ddots & \vdots \\ \omega_ {1} ^ {K - 1} & \omega_ {2} ^ {K - 1} & \ldots & \omega_ {K} ^ {K - 1} \end{array} \right]
$$

Then for all $k\in \mathbb{N}$

$$
H _ {k} = V \times \operatorname{diag} \left\{A _ {0, j} \omega_ {j} ^ {k} \right\} \times V ^ {T}
$$

Proof. Direct computation from the definitions (D.1) and (D.2).

Corollary D.6. For all $k \in \mathbb{N}$

$$
\kappa (H _ {k}) \leq \frac {J _ {2}}{J _ {1}} \kappa (V)
$$

Remark D.7. $\kappa(V)$ is well-studied in e.g. [18]. It essentially depends on the minimal distance between the nodes. In particular:

$$
\| V ^ {- 1} \| \sim \max _ {1 \leq i \leq K} \prod_ {j = 1, j \neq i} ^ {n} \frac {1}{| \omega_ {j} - \omega_ {i} |}
$$

Lemma D.8. There exist constants $C_{52}, K_{12}$ such that for all $i = 0, 1, \ldots, d$ and for all $k > K_{12} \frac{TJ_2}{J_1^2} \kappa(V)$

$$
\left| q _ {i} - \widetilde {q} _ {i} \right| \leq C _ {5 2} \frac {T J _ {2}}{J _ {1} ^ {2}} \kappa (V) k ^ {- 1}
$$

Proof. In the context of Lemma D.4, our original system is $H_{k}\mathbf{q} = \mathbf{m}$ (D.2) and the perturbed system is $\widetilde{H}_k\widetilde{\mathbf{q}} = \widetilde{\mathbf{m}}$ (D.3). Note that $|m_k| \geq J_1 \cdot C_{53}$ for some $C_{53}$. From previous considerations we therefore have

$$
\begin{array}{c} \delta H _ {k} = \frac {\| \widetilde {H} _ {k} - H _ {k} \|}{\| H _ {k} \|} \leq C _ {5 4} \frac {T}{J _ {1}} \cdot \frac {1}{k} \\ \delta \mathbf {m} \leq C _ {5 5} \cdot \frac {T}{J _ {1}} \cdot \frac {1}{k} \\ \kappa (H _ {k}) \leq \frac {J _ {2}}{J _ {1}} \kappa (V) \end{array}
$$

We would like to estimate $\delta \mathbf{q}$ according to (D.4). If

$$
k > \underbrace {2 C _ {5 4}} _ {\stackrel {{\text { def }}} {{=}} K _ {1 2}} \frac {T}{J _ {1}} \cdot \frac {J _ {2}}{J _ {1}} \kappa (V)
$$

then $\kappa (H_k)\delta H_k\leq \frac{1}{2}$ and so

$$
\delta \mathbf{q}\leq \underbrace{2\left(C_{54} + C_{55}\right)}_{\substack{\text{def}\\ \equiv C_{52}}}\frac{J_{2}}{J_{1}}\kappa \left(V\right)\frac{T}{J_{1}}\cdot \frac{1}{k}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">[H\_{k} = \left[ \begin{array}{cccc}1 &  & 1 + \frac{1}{k}\\ 1 & 1 - \frac{1}{k} \end{array} \right]]</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^2$Consider for instance $H_{k} = \left[ \begin{array}{ll}1 & 1 + \frac{1}{k}\\ 1 & 1 - \frac{1}{k} \end{array} \right]$</span></small>

We can finally estimate the accuracy of Algorithm D.3. To shorten notation, let

$$
F = F (\mathbb {A}, \mathbb {G}, T) \stackrel {\mathrm{def}} {=} \frac {T J _ {2}}{J _ {1} ^ {2}} \kappa (V)
$$

Theorem D.9. For every $0 < \alpha < 1$ there exist constants $C_{56}(\alpha), K_{13}(\alpha, F)$ such that for every $k > K_{13}$ Algorithm D.3 reconstructs the locations of the jumps with accuracy

$$
\left| \xi_ {j} - \widetilde {\xi} _ {j} \right| \leq C _ {5 6} \cdot F \cdot k ^ {\alpha - 1}
$$

Proof. We have shown that the perturbation $Q - \widetilde{Q}$ has coefficients of magnitude $k^{-1}$. We will use the same reasoning as in Section 4 in order to estimate the quantity $|\omega_j - \widetilde{\omega}_j|$ - which is the perturbation of the roots of $Q(z)$. Let $|z| < 2$. Since the coefficients of $Q(z)$ do not depend on $k$, we can obviously find constants $C_{57}$ and $C_{58}$ such that

(1) $|Q'(\omega_j)| \geq C_{57}$

(2) $|Q''(z)| < C_{58}$

By a reasoning similar to Lemma B.2 we conclude that there exist constants $C_{59} < 1, C_{60}$ such that for every function $0 < \rho(k) < C_{59}$ we have

$$
\left| Q (z) \right| > C _ {6 0} \rho (k) \quad \forall z \in \partial B _ {\rho (k)} (\omega_ {j})\tag{D.5}
$$

Now let

$$
\rho (k) = F \cdot k ^ {\alpha - 1}
$$

If $k > \left(\frac{F}{C_{59}}\right)^{\frac{1}{1 - \alpha}}$, then $\rho(k) < C_{59}$ and so (D.5) holds. On the other hand, by Lemma D.8 we have that

$$
\left| (Q - \widetilde {Q}) (z) \right| \leq C _ {6 1} \cdot F \cdot k ^ {- 1}
$$

Now finally we require that $k > \left(\frac{C_{61}}{C_{60}}\right)^{\frac{1}{\alpha}}$, in which case

$$
\left| (Q - \widetilde {Q}) (z) \right| \leq C _ {6 1} \cdot F \cdot k ^ {- 1} <   C _ {6 0} F k ^ {\alpha - 1} <   | Q (z) |
$$

and therefore $\widetilde{Q}(z)$ has a simple zero inside $B_{\rho(k)}(\omega_j)$.

Thus we have shown that $\left|\widetilde{\omega}_j - \omega_j\right| \leq F \cdot k^{\alpha - 1}$. Write $\widetilde{\omega}_j = \omega_j + \beta(k)k^{\alpha - 1}$ where $|\beta(k)| < F$. Then by Taylor expansion of the logarithm we will have (recall $|\omega_j| = 1$) for large enough $k > K_{13}(\alpha)$

$$
\left| \widetilde {\xi} _ {j} - \xi_ {j} \right| = \left| \arg \omega_ {j} - \arg \widetilde {\omega} _ {j} \right| = \left| \arg \left(\frac {\omega_ {j}}{\widetilde {\omega} _ {j}}\right) \right| \leq C _ {5 6} (\alpha) \cdot F \cdot k ^ {\alpha - 1}
$$

DEPARTMENT OF MATHEMATICS, WEIZMANN INSTITUTE OF SCIENCE, REHOVOT 76100, ISRAEL

E-mail address: dima.batenkov@weizmann.ac.il

URL: http://www.wisdom.weizmann.ac.il/\~dmitryb

E-mail address: yosef.yomdin@weizmann.ac.il

URL: http://www.wisdom.weizmann.ac.il/\~yomdin