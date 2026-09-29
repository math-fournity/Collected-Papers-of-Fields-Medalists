# VISCOSITY SOLUTIONS OF HAMILTON-JACOBI EQUATIONS $^{1}$

BY

MICHAEL G. CRANDALL AND PIERRE-LOUIS LIONS

ABSTRACT. Problems involving Hamilton-Jacobi equations—which we take to be either of the stationary form  $H(x, u, Du) = 0$  or of the evolution form  $u_t + H(x, t, u, Du) = 0$ , where Du is the spatial gradient of u—arise in many contexts. Classical analysis of associated problems under boundary and/or initial conditions by the method of characteristics is limited to local considerations owing to the crossing of characteristics. Global analysis of these problems has been hindered by the lack of an appropriate notion of solution for which one has the desired existence and uniqueness properties. In this work a notion of solution is proposed which allows, for example, solutions to be nowhere differentiable but for which strong uniqueness theorems, stability theorems and general existence theorems, as discussed herein, are all valid.

Introduction. This paper introduces a new notion of solution for first order equations of Hamilton-Jacobi type (which we call HJ equations below). Attention will be focused on the following two classes of problems:

$$
H (x, u, D u) = 0 \quad \text { in } \Omega , \qquad u = z \quad \text { on } \partial \Omega ,\tag{0.1}
$$

which will be called the Dirichlet problem for HJ equations; and

$$
\begin{array}{c} u _ {t} + H (x, t, u, D u) = 0 \quad \text { in } \Omega \times ] 0, T ], \\ u = z \quad \text { on } \partial \Omega \times ] 0, T ], \qquad u (x, 0) = u _ {0} (x) \quad \text { in } \Omega , \end{array}\tag{0.2}
$$

which will be called the Cauchy problem HJ equations. Here and below  $\Omega$  is any open domain in  $R^{N}$ , z and  $u_{0}$  are given functions (boundary conditions) and  $H(x, u, p)$  (respectively,  $H(x, t, u, p)$ ) is a given function on  $\Omega \times R \times R^{N}$  (respectively,  $\Omega \times [0, T] \times R \times R^{N}$ ) which is called the Hamiltonian. The notation Du indicates the gradient of u with respect to the x variables:  $Du = (u_{x_{1}}, \ldots, u_{x_{N}})$ . We often take  $\Omega = R^{N}$  in which case the boundary condition z is replaced by requirements on the behaviour of u at  $\infty$ .

Problems (0.1), (0.2) are global nonlinear first-order problems and it is well known that they do not have classical solutions—that is solutions  $u \in C^{1}(\Omega)$  or  $u \in C^{1}(\Omega \times ]0, T]$ —in general, even if the Hamiltonian and boundary conditions are smooth. Thus these problems have been approached by looking for generalized solutions—usually solutions  $u \in W_{\mathrm{loc}}^{1,\infty}(\Omega)$  or  $u \in W_{\mathrm{loc}}^{1,\infty}(\Omega \times ]0, T]$ —which satisfy

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Received by the editors December 1, 1981.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1980 Mathematics Subject Classification. Primary 35F20, 35F25, 35L60.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Key words and phrases. Hamilton-Jacobi equations, uniqueness criteria.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$ Sponsored by the United States Army under Contract No. DAAG29-80-C00041 and supported in part by the National Science Foundation Grant MCS-8002946.</span></small>

the equations almost everywhere. In this context existence results have been obtained by several authors—e.g., A. Douglis [10], S. N. Kružkov [18, 19, 20], W. H. Fleming [13, 14, 15], A. Friedman [16], S. H. Benton [4], with the most general results being given by P. L. Lions [22].

The question of uniqueness of the solutions seems to be more difficult. The problems (0.1) and (0.2) may have many distinct generalized solutions. For example, if  $\Omega = R$ ,  $\lambda > 0$ , and  $H(x, u, Du) = |u_x| + \lambda u - 1$ , one checks easily that  $u \equiv 1/\lambda$  is a classical solution of (0.1) while

$$
u (x) = \left\{ \begin{array}{l l} 1 / \lambda - A e ^ {\lambda x} & \text { for } x \leqslant x _ {0}, \\ 1 / \lambda - A e ^ {\lambda (2 x _ {0} - x)} & \text { for } x \geqslant x _ {0}, \end{array} \right.
$$

is a bounded, Lipschitz continuous and piecewise analytic function which satisfies the equation except at  $x = x_{0}$  for all choices of the parameters A > 0 and  $x_{0} \in R$ . Similarly, setting  $\Omega = R$ ,  $u_{0} \equiv 0$ ,  $H(x, t, u, Du) = (u_{x})^{2}$  in (0.2), we have the classical solution  $u \equiv 0$  and the piecewise linear function

$$
u = \left\{ \begin{array}{l l} 0 & \text { for } | x | \geqslant t \geqslant 0, \\ - t + | x | & \text { for } t \geqslant | x |, \end{array} \right.
$$

which satisfies the equation classically except on the lines  $t = \pm x$ , x = 0. In addition, if u, v are generalized solutions of (0.1) or (0.2) then so are  $\min(u, v)$  and  $\max(u, v)$ . In fact, if the problems are nonlinear, one expects infinitely many  $W_{loc}^{1,\infty}$  solutions (e.g., Conway and Hopf [6]).

The uniqueness problem is resolved in this paper by introducing a new notion of solution. We call these solutions viscosity solutions. $^{2}$  This notion of solution is given in §I where we also develop basic results needed in the sequel. Later we establish, for each of the Cauchy and Dirichlet problems, uniqueness results for viscosity solutions. The question of existence in the class of viscosity solutions is also treated. This, however, usually reduces to checking that the standard existence mechanism provides viscosity solutions and passages to limits.

The nature of the results is illustrated quite well by the following special case. Take (0.1) with $\Omega = \mathbf{R}^N$ and $H(x, u, p)$ replaced by $H(p) + u - n(x)$ where $H \in C(\mathbf{R}^N)$, $n \in \mathrm{BUC}(\mathbf{R}^N)$, i.e. (0.1) reads $H(Du) + u = n(x)$. In this case we take a viscosity solution of (0.1) to be a function $u \in C_b(\mathbf{R}^N)$ which satisfies (0.3)

$\forall \varphi \in C_0^\infty (\mathbf{R}^N),\varphi \geqslant 0,\forall k\in \mathbf{R}$ if $\max \varphi (u - k) > 0$ (respectively, $\min \varphi (u - k) <   0)$ , then there exists $x_0\in \{x:\varphi (u - k) = \max \varphi (u - k)\}$ (respectively, $\{x:\varphi (u - k) = \min \varphi (u - k)\}$ ) such that $H\big(-((u - k)D\varphi /\varphi)(x_0)\big) + u(x_0)\leqslant n(x_0)$ (respectively, $\geqslant n(x_0)$ ).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$ This name refers to the “vanishing viscosity” method used in the existence results, and was chosen for want of a better idea.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$C_b(\Omega))$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$ BUC( $\Omega$ ) (respectively,  $C_{b}(\Omega)$ ) denotes the space of bounded and uniformly continuous (respectively, bounded and continuous) functions on  $\Omega$ .</span></small>

Under these assumptions, the results to follow imply:

(i) If $u$ is a classical solution of (0.1), then $u$ satisfies (0.3) (§I).

(ii) If $u$ is a viscosity solution of (0.1), and $u$ is differentiable at some $x_0$, then $H(Du(x_0)) + u(x_0) = n(x_0)$; in particular, if $u$ is locally Lipschitz then (0.1) holds a.e. (§I).

(iii) If $u, v$ are two viscosity solutions of (0.1), then $u \equiv v$ (§II).

(iv) Let $\{H_m(p) + u - n_m\}$ be a sequence of Hamiltonians of the above form and $u_m$ be a viscosity solution of the corresponding problem. If $H_m \to H$, $u_m \to u$, and $n_m \to n$ locally uniformly, then $u$ satisfies (0.3) (§I).

(v) The problem (0.1) has a viscosity solution $u$ and $|u(x + y) - u(x)| \leqslant \sup \{|n(z + y) - n(z)| : z \in \mathbf{R}^N\}$. In particular, $u \in \mathrm{BUC}(\mathbf{R}^N)$ and if $n \in C^{0,\alpha}(\mathbf{R}^N)$ then $u \in C^{0,\alpha}(\mathbf{R}^N)$, $0 < \alpha \leqslant 1$ (§IV).

It is of interest here that the viscosity solution of (0.1) with  $H(p) + u - n(x)$  as above exists and is unique in such generality. Indeed, the solution may be nowhere differentiable as is seen by taking  $H \equiv 0$  and n to be nowhere differentiable. Thus we have a notion of solution of HJ equations which admits nowhere differentiable functions and permits a good existence and uniqueness theory. It is akin to the standard distribution theory, but “integration by parts” is replaced by “differentiation by parts” and is done “inside” the nonlinearity. It is extremely convenient (as is the distribution theory) for passages to limits. Closely related ideas may be found in L. C. Evans [11], and there is also a parallel with the so-called “entropy condition” for scalar hyperbolic equations of the form  $u_{t} + \Sigma f_{i}(u)_{x_{i}} = 0$ . See E. Hopf [17], Vol’pert [26] and, especially, S. N. Kružkov [20].

Finally we recall that in the case of a convex Hamiltonian other uniqueness criteria are known (A. Douglis [10], S. N. Kružkov [18], P. L. Lions [22]). Some of the current results were announced in [8].

A few words about the presentation are in order. There are many interesting theorems in this subject. We have chosen what seem to us to be the most basic to discuss in some detail and then we make some remarks on variants. To keep the ideas clear we give a “layered” presentation—some proofs are given in simple cases and then more technical and general results are presented which subsume the simple ones. However, there is little redundancy, for we use the arguments given in the simple cases without repetition. Toward the end of the paper we give proofs in simple cases and refer the reader to previous arguments which show how to generalize. A first reading of this paper for the basic ideas could consist of §§I.1 and I.2 through Corollary I.6, §II.1, §IV and §§V.1, V.2.

§I.5 deserves a special remark. The results of this section, which were established rather late, provide two criteria which are each equivalent to the notion of a viscosity solution. One utilizes local extremals of  $u - \varphi$  rather than global extremals of  $\varphi(u - k)$  while the second eliminates reference to “test” functions  $\varphi$  altogether (see Proposition I.19). L. C. Evans has observed that the criterion utilizing extremals of  $u - \varphi$  is more convenient in various situations, and the virtues of proceeding directly from these alternative notions is exhibited in [27].

We remark that the current results can be used in the study of numerical approximation of HJ equations. The authors have obtained convergence theorems

(with error estimates) showing the convergence of a class of difference approximations to the viscosity solutions [9]. The definitions of the current paper obviously extend to second order equations, which will be considered elsewhere.

## I. Viscosity solutions.

I.1. Notation and definitions. Let $\mathcal{O}$ be an open set in $\mathbf{R}^M$ and $F(y, s, p)$ be a continuous function from $\mathcal{O} \times \mathbf{R} \times \mathbf{R}^M$ into $\mathbf{R}$. We consider the equation

$$
F (y, u, D u) = 0 \quad \text { in } \mathcal {O},\tag{1.1}
$$

where $Du = (u_{y_1}, \ldots, u_{y_M})$. We have in mind that (1.1) includes both (0.1) and (0.2) of the introduction. In the first case $\Omega = \mathcal{O}$ and $F = H$ while in the second $\mathcal{O} = \Omega \times ]0, T[, y = (x, t)$ and $F(x, t, u, p) = P_{N+1} + H(x, t, p_1, \ldots, p_N)$.

If X is a set of functions on O, then  $X^{+}$ denotes the nonnegative functions in X and  $X_{c}$  denotes those functions in X which vanish off a compact subset of O.  $\mathcal{D}(\mathcal{O})$  denotes the  $C^{\infty}$  functions on O vanishing off a compact subset of O, i.e.  $\mathcal{D}(\mathcal{O}) = C_{c}^{\infty}(\mathcal{O})$ . Convergence in  $C(\mathcal{O})$  means uniform convergence on compact subsets of O, etc.

To partially motivate the definitions to follow, consider a classical (i.e., $C^1$) solution $u$ of (1.1). Let $\varphi \in C^1(\Omega)$ and $\varphi(y)u(y) = \max \varphi u > 0$. Then $D(\varphi u)(y) = \varphi(y)Du(y) + u(y)D\varphi(y) = 0$ or

$$
D u (y) = - \frac {u (y)}{\varphi (y)} D \varphi (y).
$$

It follows that

$$
F \left(y, u (y), - \frac {u (y)}{\varphi (y)} D \varphi (y)\right) = 0.
$$

We could do a similar computation at a positive maximum point $y$ of $\varphi(u - \psi)$ where $\psi \in C^1(\Omega)$ as well to conclude

$$
F \left(y, u (y), - \frac {u (y) - \psi (y)}{\varphi (y)} D \varphi (y) + D \psi (y)\right) = 0.
$$

In the definitions which follow we specialize to $\psi \equiv k\in \mathbf{R}$.

We need some more notation. For $\psi \in C(\mathcal{O})$, set $E_{+}(\psi) = \{y \in \mathcal{O}: \psi(y) = \max \psi > 0\}$ (the positive extreme set of $\psi$), and $E_{-}(\psi) = \{y \in \mathcal{O}: \psi(y) = \min \psi < 0\}$ (the negative extreme set of $\psi$), with the understanding that $E_{+}(\psi) = \varnothing$ if $\psi$ does not assume a positive maximum value in $\mathcal{O}$, etc. When necessary, the dependence on $\mathcal{O}$ will be recalled by writing $E_{+}(\psi; \mathcal{O}), E_{-}(\psi; \mathcal{O})$.

We now define viscosity solutions of (1.1) as well as the corresponding notions of subsolutions and supersolutions.

DEFINITION I.1. A viscosity subsolution (respectively, supersolution) of (1.1) is a function $u \in C(\mathcal{O})$ such that for every $\varphi \in \mathfrak{D}(\mathcal{O})^+$ and $k \in \mathbb{R}$

$$
\left\{ \begin{array}{l} E _ {+} (\varphi (u - k)) \neq \emptyset \Rightarrow \exists y \in E _ {+} (\varphi (u - k)) \text {   such   that } \\ F \left(y, u (y), - \frac {u (y) - k}{\varphi (y)} D \varphi (y)\right) \leqslant 0, \end{array} \right.\tag{1.2}
$$

(respectively,

$$
\left\{ \begin{array}{l} E _ {-} (\varphi (u - k)) \neq \emptyset \Rightarrow \exists y \in E _ {-} (\varphi (u - k)) \text {   such   that } \\ F \bigg (y, u (y), - \frac {u (y) - k}{\varphi (y)} D \varphi (y) \bigg) \geqslant 0 \bigg). \end{array} \right.\tag{1.3}
$$

A viscosity solution is a $u \in C(\mathcal{O})$ for which both (1.2) and (1.3) hold, i.e. $u$ is both a viscosity subsolution and a viscosity supersolution.

It will be convenient at times to speak of viscosity solutions of  $F \leqslant 0$  rather than viscosity subsolutions of F = 0, etc. The reader should notice at this stage that the equations F = 0 and -F = 0 are not equivalent in the viscosity sense. For example,  $u(x) = |x|$  is a viscosity solution of  $(u_x)^2 - 1 = 0$  on R, but it is not a viscosity solution of  $-(u_x)^2 + 1 = 0$  on R. (The reader can verify this as an exercise or turn to §I.4.) However, we do have:

REMARK 1.4. u is a viscosity solution of  $F(y, u, Du) \leqslant 0$  if and only if v = -u is a viscosity solution of  $-F(y, -v, -Dv) \geqslant 0$ .

According to our “motivation”, admittedly meager at this point, classical solutions are clearly viscosity solutions. Complete consistency of the classical and viscosity notions of solution requires that a viscosity solution u which happens to be  $C^{1}$  will also be a classical solution. This is indeed the case; it is a consequence of subtler facts presented in the next paragraph.

I.2. Basic properties of viscosity solutions. In this paragraph we develop a variety of basic results concerning viscosity solutions. A matter of concern will be showing that the weak assumptions in Definition I.1—e.g., the small classes of functions  $\varphi \in \mathfrak{D}(\Omega)^{+}$ ,  $\psi \equiv k \in R$  occurring in the definition as well as the “∃” in place of “∀” in (1.2), (1.3)—can be strengthened without altering the notion defined. Before stating results to this effect, we will prove one which illustrates the convenience of the weakness of the definition.

In order to set the stage for this result, we first give an example showing it to be totally false for Lipschitz continuous solutions. Consider the problem

$$
\left\{ \begin{array}{l l} (u _ {x}) ^ {2} - 1 = 0 & \text { on } ] - 1, 1 [, \\ u (- 1) = u (1) = 0. \end{array} \right.
$$

This problem has a largest Lipschitz solution $u_{\max}(x) = 1 - |x|$ and a smallest Lipschitz solution $u_{\min} = -u_{\max}$. It has many others; e.g., $u_n(-1) = 0$, and $u_n' = (-1)^j$ on $]-1 + j/2n, -1 + (j+1)/2n[$ for $j = 0, \ldots, 4n-1$, defines a solution for which $0 \leqslant u_n \leqslant 1/2n$ for each $n$. Clearly $u_n \to 0$ uniformly as $n \to \infty$, but $u \equiv 0$ is not a solution of $(u_x)^2 = 1$ anywhere. More generally, given any $g \in C([-1, 1])$ with Lipschitz constant 1 and $g(-1) = g(1) = 0$, it can be uniformly approximated by Lipschitz continuous solutions of the above problem.

In contrast, for viscosity solutions we have

THEOREM I.2 (STABLILITY OF VISCOSITY SOLUTIONS). Let $\{F_l\}$ be a sequence of continuous functions on $\mathcal{O} \times \mathbf{R} \times \mathbf{R}^M$ converging in $C(\mathcal{O} \times \mathbf{R} \times \mathbf{R}^M)$ to $F \in C(\mathcal{O} \times \mathbf{R} \times \mathbf{R}^M)$ and let $u_l \in C(\mathcal{O})$ be a viscosity solution of $F_l(y, u_l, Du_l) \leqslant 0$ (respectively, $F_l \geqslant 0$). Let $u_l \to u$ in $C(\mathcal{O})$. Then $u$ is a viscosity solution of $F \leqslant 0$ (respectively, $F \geqslant 0$).

PROOF OF THEOREM I.2. Assume $u_{l}$ is a viscosity solution of $F_{l} \leqslant 0$. Let $\varphi \in \mathcal{D}(\mathcal{O})^{+}$ and $y \in E_{+}(\varphi(u - k))$. Then for large $l$, $\varphi(y)(u_{l}(y) - k) > 0$ so $E_{+}(\varphi(u_{l} - k)) \neq 0$ and, by assumption, there exists $y_{l} \in E_{+}(\varphi(u_{l} - k))$ for which

$$
F _ {l} \left(y _ {l}, u _ {l} (y _ {l}), - \frac {u _ {l} (y _ {l}) - k}{\varphi (y _ {l})} D \varphi (y _ {l})\right) \leqslant 0.\tag{1.5}
$$

Now $y_{l} \in \operatorname{supp} \varphi,^{4}$ and thus there is a subsequence $y_{l'}$ convergent to some $\bar{y} \in \mathcal{O}$. Moreover $\varphi(u - k) \leqslant \lim \max(\varphi(u_{l} - k)) = \lim \varphi(y_{l})(u_{l}(y_{l}) - k) \leqslant \varphi(\bar{y})(u(\bar{y}) - k)$ so $\bar{y} \in E_{+}(\varphi(u - \overline{k}))$. Letting $l \to \infty$ through the subsequence $l'$ in (1.5) and using the assumed convergence $F_{l} \to F$ we have

$$
F \left(\bar {y}, u (\bar {y}), - \frac {u (\bar {y}) - k}{\varphi (\bar {y})} D \varphi (\bar {y})\right) \leqslant 0.
$$

Thus $u$ is a viscosity subsolution. The proof for the case $F_{l} \geqslant 0$ is the same or one may use Remark 1.4. The proof is complete.

The next result summarizes the implications of the sequence of arguments which follow it and outlines the extent to which the definition of viscosity solution could be strengthened without changing the class of such solutions. If  $\varphi \in C(\mathcal{O})$  we set  $d(\varphi) = \{y \in \mathcal{O}: \varphi \text{ is differentiable at } y\}$ .

THEOREM I.3. Let $u$ be a viscosity subsolution of $F = 0$, $\varphi \in C(\mathcal{O})^{+}$ and $\psi \in C(\mathcal{O})$. Then

$$
F \left(y, u, - \frac {u - \psi}{\varphi} D \varphi + D \psi\right) \leqslant 0 \quad \text { on   } E _ {+} (\varphi (u - \psi)) \cap d (\varphi) \cap d (\psi). \tag {1.6}
$$

If $u$ is a viscosity supersolution, then

$$
F \left(y, u, - \frac {u - \psi}{\varphi} D \varphi + D \psi\right) \geqslant 0 \quad \text { on   } E _ {-} (\varphi (u - \psi)) \cap d (\varphi) \cap d (\psi), \tag {1.7}
$$

while if $u$ is a viscosity solution both (1.6) and (1.7) hold.

We prepare two lemmas. A key ingredient is the following formulation of a result of L. C. Evans [11].

LEMMA I.4. Let $\varphi \in C(\mathcal{O})$ be differentiable at $y_0 \in \mathcal{O}$. Then there exist functions $\psi_{+}$ and $\psi_{-}$ such that $\psi_{\pm} \in C_c^1(\mathcal{O})$, $\psi_{\pm}(y_0) = \varphi(y_0)$, $D\psi_{\pm}(y_0) = D\varphi(y_0)$ and $\psi_{+} > \varphi$, $\psi_{-} < \varphi$ on $B(y_0, r) \setminus \{y_0\}$, for some $r > 0$.

PROOF OF LEMMA I.4. Replacing $\varphi$ by $\hat{\varphi}(y) = \varphi(y_0 + y) - \varphi(y_0) - D\varphi(y_0) \cdot y$, we can assume $y_0 = 0$, $\varphi(0) = 0$, and $D\varphi(0) = 0$. It suffices to exhibit $\psi_+$. By assumption, $\varphi(y) = |y| \rho(y)$ where $\rho \in C(\mathcal{O})$ and $\rho(y) \to 0$ as $|y| \to 0$. Set $\bar{\rho}(r) = \sup\{\rho(y): y \in \mathcal{O} \cap B(0, r)\}$ and

$$
\psi_ {+} (y) = \int_ {| y |} ^ {2 | y |} \bar {\rho} (s) d s + | y | ^ {2}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{6}a \cdot b$ denotes the Euclidean inner-product of $a, b \in \mathbf{R}^{M}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{5}B(y_{0},r)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{6}a \cdot b$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$y_{0}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$a, b \in \mathbf{R}^{M}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{4}$ Supp  $\varphi$  denotes the support of  $\varphi$ .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{5}B(y_{0}, r)$ denotes the open ball of radius r and center $y_{0}$.</span></small>

Let $\overline{B(0,h)}\subset\mathcal{O}$. Then $\psi_{+}\in C^{1}(B(0,h))$, $\psi_{+}(0)=0$, $\psi_{+}(y)\geqslant|y|\bar{\rho}(|y|)+|y|^{2}>|y|\rho(y)=\varphi(y)$ for $y\in B(0,h)\backslash\{0\}$ by the monotonicity of $\bar{\rho}$, and $D\psi_{+}(0)=0$. This $\psi_{+}$ may be modified outside $B(0,h/2)$ if necessary to achieve $\psi_{+}\in C_{c}^{1}(\mathcal{O})$.

## We next prove

LEMMA I.5. The assertions of Theorem I.3 are valid if also $\psi \equiv k\in \mathbf{R}$ is a constant.

PROOF OF LEMMA I.5. It suffices to show (1.6) holds for viscosity subsolutions (recall Remark 1.4). Let $\varphi\in C(\mathcal{O})^{+}$ be differentiable at $y_{0}\in\mathcal{O}$ and $y_{0}\in E_{+}(\varphi(u-k))$. It follows at once from Lemma I.4 that there is a $\psi_{-}\in C_{c}^{1}(\mathcal{O})^{+}$ such that $\psi_{-}(y_{0})=\varphi(y_{0})$, $D\psi_{-}(y_{0})=D\varphi(y_{0})$ and $\psi_{-}<\varphi$ on supp $\psi_{-}\setminus\{y_{0}\}$. Then

$$
\left\{y _ {0} \right\} = E _ {+} \left(\psi_ {-} (u - k)\right).\tag{1.8}
$$

Next choose a sequence $\{\varphi_l\}_{l=1}^{\infty} \subset \mathfrak{D}(\mathcal{O})^+$ with supports contained in a fixed compact subset of $\mathcal{O}$ so that $\varphi_l \to \psi_-$ and $D\varphi_l \to D\psi_-$ uniformly. For large $l$, $\varphi_l(y_0)(u(y_0) - k) > 0$ so $E_+(\varphi_l(u - k)) \neq 0$ and, by assumption, there exist $y_l \in E_+(\varphi_l(u - k))$ such that

$$
F \left(y _ {l}, u (y _ {l}), - \frac {u (y _ {l}) - k}{\varphi (y _ {l})} D \varphi_ {l} (y _ {l})\right) \leqslant 0.\tag{1.9}
$$

Passing to a subsequence if necessary we may assume $y_{l}$ converges to a limit $y$. Clearly $y \in E_{+}(\psi_{-}(u - k))$ and then $y = y_0$ by (1.8). Sending $l$ to $\infty$ in (1.9) and using $\varphi_{l} \to \psi_{-}$ in $C^1, \psi_{-}(y_0) = \varphi(y_0), D\psi_{-}(y_0) = D\varphi(y_0)$ we conclude

$$
F \left(y _ {0}, u (y _ {0}), - \frac {u (y _ {0}) - k}{\varphi (y _ {0})} D \varphi (y _ {0})\right) \leqslant 0,
$$

hence the result.

PROOF OF THEOREM I.3. It suffices to consider the subsolution case. Let $\varphi \in C(\mathcal{O})^{+}$, $\psi \in C(\mathcal{O})$, $y_0 \in E_{+}(\varphi(u - \psi)) \cap d(\varphi) \cap d(\psi)$. Set

$$
\tilde {\varphi} (y) = \varphi (y) \frac {u (y) - \psi (y)}{u (y) - \psi \left(y _ {0}\right)} \chi (y)
$$

where $\chi \in \mathfrak{D}(\mathcal{O})^{+}$ satisfies $0 \leqslant \chi \leqslant 1$, $\chi(y_0) = 1$, and $\chi$ vanishes off a neighborhood of $y_0$ on which $u(y) > \psi(y_0)$. Then

$$
\tilde {\varphi} (y) \left(u (y) - \psi \left(y _ {0}\right)\right) = \chi (y) \varphi (y) \left(u (y) - \psi (y)\right)
$$

which is clearly at most $\varphi(y_0)(u(y_0) - \psi(y_0))$, i.e. $y_0 \in E_+$ ($\tilde{\varphi}(u - \psi(y_0))$). Since $\varphi$ and $\psi$ are differentiable at $y_0$ and

$$
\begin{array}{r l} \frac {u (y) - \psi (y)}{u (y) - \psi (y _ {0})} & = 1 + \frac {\psi (y _ {0}) - \psi (y)}{u (y _ {0}) - \psi (y _ {0}) + u (y) - u (y _ {0})} \\ & = 1 + \frac {\psi (y _ {0}) - \psi (y)}{u (y _ {0}) - \psi (y _ {0})} + o (| y - y _ {0} |), \end{array}
$$

we have

$$
D \tilde {\varphi} (y _ {0}) = D \varphi (y _ {0}) - \frac {1}{u (y _ {0}) - \psi (y _ {0})} D \psi (y _ {0}).
$$

The result now follows from Lemma I.5 applied with  $k = \psi(y_{0})$  and  $\tilde{\varphi}$  in place of  $\varphi$ . Using the above results it is now simple to prove

COROLLARY I.6 (CONSISTENCY). Let u be a viscosity subsolution (respectively; supersolution, solution) of  $F(y, u, Du) = 0$ . Then  $F(y, u, Du) \leqslant 0$  (respectively;  $F(y, u, Du) \geqslant 0$ ,  $F(y, u, Du) = 0$ ) on  $d(u)$ .

PROOF OF COROLLARY I.6. It suffices to treat the supersolution case. Let $y_0 \in d(u)$. Choose $\psi_+ \in C_c^1(\mathcal{O})$ such that $\psi_+(y_0) = u(y_0)$, $D\psi_+(y_0) = Du(y_0)$ and $\psi_+ > u$ in a deleted ball $B(y_0, h) \setminus \{y_0\}$. Choose $\varphi \in \mathfrak{D}(\mathcal{O})^+$ with $\operatorname{supp} \varphi \subset B(y_0, h)$, $0 \leqslant \varphi \leqslant 1$, $\varphi(y_0) = 1$ (so $D\varphi(y_0) = 0$). Then $\{y_0\} = E_-(\varphi(u - \psi_+ + 1))$. By Theorem I.3 and the assumption that $u$ is a viscosity supersolution, we have

$$
\begin{array}{c} F \Bigg (y _ {0}, u (y _ {0}), - \frac {u (y _ {0}) - \psi_ {+} (y _ {0}) + 1}{\varphi (y _ {0})} D \varphi (y _ {0}) + D \psi_ {+} (y _ {0}) \Bigg) \\ = F (y _ {0}, u (y _ {0}), D u (y _ {0})) \geqslant 0, \end{array}
$$

and the proof is complete.

The next two results are concerned with changes of variables.

COROLLARY I.7. Let $u$ be a viscosity subsolution (respectively; supersolution, solution) of (1.1). Then:

(i) If $g \in C^1(\mathcal{O})$, $g > 0$ in $\mathcal{O}$, $\psi \in C^1(\mathcal{O})$ and $v = g(u - \psi)$, then $v$ is a viscosity solution (respectively; supersolution, solution) of $G(y, v, Dv) = 0$ where

$$
G (y, r, p) = F \left(y, \frac {r}{g (y)} + \psi (y), \frac {- r D g (y)}{g (y) ^ {2}} + \frac {p}{g (y)} + D \psi (y)\right).
$$

(ii) If $\Phi: \mathcal{O} \to \hat{\mathcal{O}}$ is a $C^1$ diffeomorphism of the domain $\mathcal{O}$ onto the domain $\hat{\mathcal{O}}$, then $v(\Phi(y)) = u(y)$ defines a viscosity subsolution (respectively; supersolution, solution) of $G(\hat{y}, v, Dv) = 0$ where

$$
G (\hat {y}, r, p) = F \left(\Phi^ {- 1} (\hat {y}), r, p D \Phi \left(\Phi^ {- 1} (\hat {y})\right)\right)
$$

and $pD\Phi(y)$ denotes the action of $D\Phi(y)$ on the cotangent vector $p$.

We omit the proof of Corollary I.7 as it is an easy exercise given Theorem I.3. To conclude this section we obtain a partial result concerning nonlinear changes of the unknown.

COROLLARY I.8. Let $u$ be a viscosity subsolution (respectively; supersolution, solution) of (1.1) and let $\Phi \in C^1(\mathbf{R})$, $\Phi' > 0$ everywhere and $\Phi(\mathbf{R}) = \mathbf{R}$. Then $v = \Phi(u)$ is a viscosity subsolution (respectively; supersolution, solution) of

$$
F (y, \Phi^ {- 1} (v), (\Phi^ {- 1}) ^ {\prime} (v) D v) = 0.\tag{1.10}
$$

PROOF OF COROLLARY I.8. We treat the subsolution case. Let $u$ be a viscosity subsolution of $F = 0$. We claim that, if $x_0 \in E_+(\varphi(v - k))$ (with $\varphi \in \mathfrak{D}(\Omega)^+$, $k \in \mathbf{R}$) then there exists $\tilde{\varphi} \in C_c^1(\Omega)^+$, $\tilde{k} \in \mathbf{R}$ such that

$$
x _ {0} \in E _ {+} (\tilde {\varphi} (u - \tilde {k})), \quad - \frac {u (x _ {0}) - \tilde {k}}{\tilde {\varphi} (x _ {0})} D \tilde {\varphi} (x _ {0}) = - \Psi^ {\prime} (v (x _ {0})) \frac {v (x _ {0}) - k}{\varphi (x _ {0})} D \varphi (x _ {0}),
$$

where $\Psi(t) = \Phi^{-1}(t)$. This obviously implies the corollary.

Now, to prove our claim, we argue as follows: we have for  $|x - x_{0}|$  small,

$$
\begin{array}{r l} v (x) & \leqslant \frac {\varphi (x _ {0})}{\varphi (x)} (v (x _ {0}) - k) + k \\ & \leqslant v (x _ {0}) - \frac {v (x _ {0}) - k}{\varphi (x _ {0})} D \varphi (x _ {0}) \cdot (x - x _ {0}) + | x - x _ {0} | \varepsilon (| x - x _ {0} |) \end{array}\tag{1.11}
$$

where $\varepsilon \in C(\mathbf{R}_{+},\mathbf{R}^{M})$ and $\varepsilon (t)\to 0$ as $t\rightarrow 0+$. Thus, for $|x - x_0|$ small, we obtain, since $\Psi$ is nondecreasing,

$$
\begin{array}{l} u (x) \leqslant \Psi \left(v (x _ {0}) - \left(\frac {v (x _ {0}) - k}{\varphi (x _ {0})}\right) D \varphi (x _ {0}) \cdot (x - x _ {0}) + | x - x _ {0} | \varepsilon (| x - x _ {0} |)\right) \\ \leqslant \tilde {u} (x) = u (x _ {0}) - \Psi^ {\prime} (v (x _ {0})) \left(\frac {v (x _ {0}) - k}{\varphi (x _ {0})}\right) D \varphi (x _ {0}) \cdot | x - x _ {0} | \\ + | x - x _ {0} | \tilde {\varepsilon} (| x - x _ {0} |) \end{array}
$$

for $|x - x_0|$ small enough and $\tilde{\varepsilon} \in C(\mathbf{R}_+ , \mathbf{R}^M)$, $\tilde{\varepsilon}(t) \to 0$ as $t \to 0 +$. But the right-hand member $\tilde{u}$ of the above inequality is a continuous function differentiable at $x_0$ and therefore by Lemma I.4 we may find $\tilde{k}$ and $\tilde{\varphi} \in C_c^1(\Omega)^+$ such that: $u(x_0) - \tilde{k} > 0$; $x_0 \in E_+ (\tilde{\varphi}(\tilde{u} - \tilde{k}))$;

$$
- D \tilde {\varphi} (x _ {0}) \frac {u (x _ {0}) - \tilde {k}}{\tilde {\varphi} (x _ {0})} = - \Psi^ {\prime} (v (x _ {0})) \frac {v (x _ {0}) - k}{\varphi (x _ {0})} D \varphi (x _ {0}); \quad \operatorname{supp} \tilde {\varphi} \subset B (x _ {0}, h),
$$

where h is small enough in order to have  $u(x) \leqslant \tilde{u}(x)$  on  $B(x_{0}, h)$ . We are done since we have for all x,

$$
\tilde {\varphi} (x) \left(u (x) - \tilde {k}\right) \leqslant \tilde {\varphi} (x) \left(\tilde {u} (x) - \tilde {k}\right) \tilde {\varphi} \left(x _ {0}\right) \left(\tilde {u} \left(x _ {0}\right) - \tilde {k}\right) = \tilde {\varphi} \left(x _ {0}\right) \left(u \left(x _ {0}\right) \tilde {k}\right)\tag{1.12}
$$

and thus $x_0 \in E_+$ ($\tilde{\varphi}(u - \tilde{k})$).

REMARK 1.13. We pause here to consider the case in which $\mathcal{O}$ is not an open subset of $\mathbf{R}^N$. Indeed, in later sections we will want to use some of the above results when $\mathcal{O}$ has the form $\mathcal{O} = \Omega \times ([0,T])$. We claim that all we have done is correct in general if one interprets the definitions appropriately. This means: $\mathcal{D}(\mathcal{O}), C^1(\mathcal{O})$, etc., should denote restrictions of functions in $\mathcal{D}(\mathbf{R}^N)$, $C^1(\mathbf{R}^N)$, etc. to $\mathcal{O}$ (where, in the case of $\mathcal{D}(\mathcal{O})$, $\{x \in \mathcal{O}: u(x) \neq 0\}$ lies in a compact subset of $\mathcal{O}$, etc.). The other point is the notion of “differentiable”. We will say $\varphi \in C(\mathcal{O})$ is differentiable at $y_0 \in \mathcal{O}$ and $D\varphi(y_0) = z$ if there is an extension of $\varphi$ to $\tilde{\varphi} \in C(\mathbf{R}^N)$ such that $D\tilde{\varphi}(y_0) = z$ and moreover, for any extension of $\varphi$ to $\tilde{\varphi} \in C(\mathbf{R}^N)$ differentiable at $y_0$, $D\tilde{\varphi}(y_0) = z$. (In the case where $\mathcal{O}$ has some boundary which is sufficiently smooth, e.g. $\mathcal{O} = \Omega \times ]0,T]$, all notions coincide.) The reader can think through these claims.

I.3. Piecewise smooth viscosity solutions. In this section we consider piecewise  $C^{1}$  functions and determine conditions on the discontinuities of their derivatives equivalent to being viscosity solutions of F = 0. Consider the situation in which  $O = O_{+} \cup O_{-} \cup \Gamma$  is divided into two open parts  $O_{+}$  and  $O_{-}$  by a surface  $\Gamma$ . The unit normal to

$\Gamma$ at $y_0 \in \Gamma$ is denoted by $\vec{n}(y_0)$ which points into $\mathcal{O}_+$. A function $u \in C(\mathcal{O})$ is given as $u_+$ in $\mathcal{O}_+ \cup \Gamma$ and $u_-$ in $\mathcal{O}_- \cup \Gamma$. We assume $\Gamma$ is of class $C^1$ and so may be represented by a relation of the typical form $y_1 = f(y_2, \ldots, y_m)$ near $y_0 \in \Gamma$, where $f \in C^1$. We assume $u \in C(\mathcal{O})$ and $u_± \in C^1(\mathcal{O}_± \cup \Gamma)$. When is $u$ a viscosity solution of $F = 0$ in $\mathcal{O}$? We will use the following observations.

PROPOSITION I.9. (i) If $u$ is a viscosity solution of $F = 0$ in $\mathfrak{O}$ and $\mathfrak{O}'$ is an open subset of $\mathfrak{O}$ then $u|_{\mathfrak{O}'}^7$ is a viscosity solution of $F = 0$ in $\mathfrak{O}'$.

(ii) If $u \in C(\mathfrak{O})$, $\mathfrak{O}$ is the union of relatively open subsets $\mathfrak{O}_1$ and $\mathfrak{O}_2$, $\mathfrak{O} = \mathfrak{O}_1 \cup \mathfrak{O}_2$ and $u|_{\mathfrak{O}_i}$ is a viscosity solution of $F = 0$ in $\mathfrak{O}_i$, $i = 1, 2$, then $u$ is a viscosity solution of $F = 0$ in $\mathfrak{O}$.

That is, the property of being a viscosity solution is purely local. Part (i) of the proposition is completely trivial and we leave part (ii) as a very simple exercise.

To continue, assume $u \in C(\mathcal{O})$ is a viscosity solution. Then $u_{\pm}$ is a viscosity solution in $\mathcal{O}_{\pm}$. But $u_{\pm}$ lie in $C^1(\mathcal{O}_{\pm})$, so $u_{\pm}$ are classical solutions by Corollary I.6. Let $\varphi \in \mathfrak{D}(\mathcal{O})^+$, $y_0 \in E_{\pm}(\varphi(u - k))$. If $y_0 \in \mathcal{O}_+ \cup \mathcal{O}_-$ we then have

$$
F \left(y _ {0}, u (y _ {0}), - (u (y _ {0}) - k) \frac {D \varphi (y _ {0})}{\varphi (y _ {0})}\right) = 0
$$

by the opening remarks of this section. It remains to consider  $y_{0} \in \Gamma$ . Let

$$
T _ {y _ {0}} = \left\{\tau \in \mathbf {R} ^ {M}: \vec {n} (y _ {0}) \cdot \tau = 0 \right\}
$$

be the tangent space to $\Gamma$ to $y_0$ and $p_T$, $p_N = I - p_T$ be the orthogonal projections on $T_{y_0}$, $\operatorname{span}\{\bar{n}(y_0)\}$, i.e. $p_N y = (\bar{n}(y_0) \cdot y) \bar{n}(y_0)$. Since $u_+$, $u_-$ agree on $\Gamma$, $p_T Du_+(y_0) = p_T Du_-(y_0)$. When $y_0 \in E_+(\varphi(u-k)) \cap \Gamma$ we clearly have $T_{y_0} \ni \tau \to \Phi(\tau) = \varphi(y_0 + \tau)(u(y_0 + \tau) - k)$ satisfies $D_T \Phi(0) = 0$,

$$
\begin{array}{l} \lim _ {\alpha \downarrow 0} \frac {\varphi (y _ {0} + \alpha \vec {n}) (u _ {+} (y _ {0} + \alpha \vec {n}) - k) - \varphi (y _ {0}) (u (y _ {0}) - k)}{\alpha} \leqslant 0, \\ \lim _ {\alpha \uparrow 0} \frac {\varphi (y _ {0} + \alpha \vec {n}) (u _ {-} (y _ {0} + \alpha \vec {n}) - k) - \varphi (y _ {0}) (u (y _ {0}) - k)}{\alpha} \geqslant 0. \end{array}
$$

These relations amount to

$$
\begin{array}{l} - \frac {u (y _ {0}) - k}{\varphi (y _ {0})} p _ {T} D \varphi (y _ {0}) = p _ {T} D u _ {+} (y _ {0}) = p _ {T} D u _ {-} (y _ {0}), \\ - \frac {u (y _ {0}) - k}{\varphi (y _ {0})} D \varphi (y _ {0}) \cdot \vec {n} (y _ {0}) \geqslant D u _ {+} (y _ {0}) \cdot \vec {n} (y _ {0}), \\ - \frac {u (y _ {0}) - k}{\varphi (y _ {0})} D \varphi (y _ {0}) \cdot \vec {n} (y _ {0}) \leqslant D u _ {-} (y _ {0}) \cdot \vec {n} (y _ {0}). \end{array}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{7}u|_{\theta'}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">O'.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{7}u|_{\mathfrak{O}'}$ means the restriction of $u$ to $\mathfrak{O}'$.</span></small>

Hence

$$
\left\{ \begin{array}{l} - \frac {u (y _ {0}) - k}{\varphi (y _ {0})} D \varphi (y _ {0}) = p _ {T} D u _ {-} (y _ {0}) + \xi \vec {n} (y _ {0}) \\ \text {for some} \xi \in \left[ D u _ {+} (y _ {0}) \cdot \vec {n} (y _ {0}), D u _ {-} (y _ {0}) \cdot \vec {n} (y _ {0}) \right]. \end{array} \right.
$$

We conclude that the condition

$$
\left\{ \begin{array}{l} \forall y _ {0} \in \Gamma , \forall \xi \in \left[ D u _ {+} (y _ {0}) \cdot \vec {n} (y _ {0}), D u _ {-} (y _ {0}) \cdot \vec {n} (y _ {0}) \right], \\ F (y _ {0}, u (y _ {0}), p _ {T} D u _ {\pm} (y _ {0}) + \xi \vec {n} (y _ {0})) \leqslant 0 \end{array} \right.\tag{1.14}
$$

implies $u$ is a viscosity subsolution of $F = 0$. Similarly

$$
\left\{ \begin{array}{l} \forall y _ {0} \in \Gamma , \forall \xi \in \left[ D u _ {-} (y _ {0}) \cdot \vec {n} (y _ {0}), D u _ {+} (y _ {0}) \cdot \vec {n} (y _ {0}) \right], \\ F (y _ {0}, u (y _ {0}), p _ {T} D u _ {\pm} (y _ {0}) + \xi \vec {n} (y _ {0})) \geqslant 0 \end{array} \right.\tag{1.15}
$$

implies u is a viscosity supersolution of F = 0. Note that if, e.g.,  $Du_{-}(y_{0}) \cdot \vec{n}(y_{0}) > Du_{+}(y_{0}) \cdot \vec{n}(y_{0})$  then (1.15) is an empty condition, etc. In fact, (1.14), (1.15) are necessary as well as sufficient. We prove

THEOREM I.10. Let $\mathcal{O},\mathcal{O}_{+},\mathcal{O}_{-},\Gamma ,u,u_{\pm}$ be as above. Then $u$ is a viscosity solution of $F = 0$ in $\mathcal{O}$ if and only if $u_{\pm}$ are classical solutions in $\mathcal{O}_{\pm}$ and (1.14) and (1.15) hold.

PROOF. The sufficiency has been shown. We consider the necessity. First let $\xi = Du_{+}(y_0)\cdot \vec{n} (y_0) = Du_{-}(y_0)\cdot \vec{n} (y_0)$. In this case $u$ is differentiable at $y_{0}$ and $Du(y_0) = p_T Du_{\pm}(y_0) + \xi \vec{n} (y_0)$. By Theorem I.2 we have

$$
F \left(y _ {0}, u \left(y _ {0}\right), D u \left(y _ {0}\right)\right) = F \left(y _ {0}, u \left(y _ {0}\right), p _ {T} D u _ {\pm} \left(y _ {0}\right) + \xi \bar {n} \left(y _ {0}\right)\right) = 0
$$

so (1.14) and (1.15) hold. Next assume that $Du_{-}(y_0) \cdot \vec{n}(y_0) > \xi > Du_{+}(y_0) \cdot \vec{n}(y_0)$. We claim that then there is a $\psi \in C^1(\mathcal{O})$ such that $\psi(y_0) = u(y_0), \psi > u$ in a deleted neighborhood of $y_0$ and $D\psi(y_0) = p_T Du_{\pm}(y_0) + \xi \vec{n}(y_0)$. If this is so, choose $\varphi \in \mathfrak{D}(\mathcal{O}), 0 \leqslant \varphi \leqslant 1, \varphi(y_0) = 1$ and $\varphi(y) < 1$ for $y \neq y_0$ so that $1 > \varphi(\psi - u) \geqslant 0$. Then $\{y_0\} = E_{+}(\varphi(u - \psi + 1))$ and by Theorem I.3

$$
F \left(y _ {0}, u \left(y _ {0}\right), D \psi \left(y _ {0}\right)\right) = F \left(y _ {0}, u \left(y _ {0}\right), p _ {T} D u _ {\pm} \left(y _ {0}\right) + \xi \vec {n} \left(y _ {0}\right)\right) \leqslant 0,
$$

so we have (1.14). The case in which (1.14) is an empty requirement is similar. It remains to exhibit  $\psi$ . By Proposition I.9 and Corollary I.7 we may localize and change variables. Hence assume  $y_{0}=0$  and  $\Gamma$  is  $y_{1}=0$ . We have

$$
u (y _ {1}, \dots , y _ {m}) = \left\{ \begin{array}{l l} u _ {+} (y _ {1}, \dots , y _ {m}) & \text { if } y _ {1} \geqslant 0, \\ u _ {-} (y _ {1}, \dots , y _ {m}) & \text { if } y _ {1} \leqslant 0, \end{array} \right.
$$

and

$$
\frac {\partial u _ {-}}{\partial y _ {i}} \left(0, y _ {2}, \dots , y _ {m}\right) = \frac {\partial u _ {+}}{\partial y _ {i}} \left(0, y _ {2}, \dots , y _ {m}\right), \quad i = 2, \dots , m,
$$

$$
\frac {\partial u _ {+}}{\partial y _ {1}} (0, 0, \dots , 0) <   \xi <   \frac {\partial u _ {-}}{\partial y _ {1}} (0, 0, \dots , 0).
$$

Let $\psi_0(y_2,\ldots ,y_m)\geqslant u_{\pm}(0,y_2,\ldots ,y_m)$ with strict inequality if $(y_{2},\ldots ,y_{m})\neq (0,\ldots ,0)$ in some neighborhood of $(0,\ldots ,0),\psi_0(0,\ldots ,0) = u_{\pm}(0,0,\ldots ,0),\partial \psi_0(0,\ldots ,0) / \partial y_i =$$\partial u_{\pm}(0,\dots ,0) / \partial y_i$ for $i = 2,\dots ,m.\psi_0$ exists by Lemma I.4. Then set $\psi (y_1,\dots ,y_m) =$$\psi_0(y_2,\dots ,y_m) + \xi y_1$ . Clearly $\psi$ has the desired properties and the proof is complete.

To illustrate this result, consider the example solution $u = 0$ for $|x| \geqslant t \geqslant 0$, $u = -t + |x|$ if $|x| \leqslant t$ of $u_t + (u_x)^2 = 0$ in the introduction. Let $\Gamma$ be $x = 0$, $\vec{n}(0, t) = (1, 0)$. Then $F((x, t), u, (p_1, p_2)) = p_2 + (p_1)^2$, $u_+ = -t + x$ and $u_- = -t - x$ in the appropriate domains. We have

$$
\left\{ \begin{array}{l} p _ {T} D u _ {\pm} (0, t) = (0, 1), \\ D u _ {+} (0, t) \cdot \vec {n} (0, t) = 1 > - 1 = D u _ {-} (0, t) \cdot \vec {n} (0, t), \end{array} \right.
$$

but $F(p_T u_{\pm}(0, t) + \xi \vec{n}(0, t)) = -1 + \xi^2 < 0$ for $-1 < \xi < 1$ so (1.15) fails.

We remark that the conditions (1.14) and (1.15) were anticipated by Oleinik [24] in a special case. Moreover, an alternative way to obtain these results is given in §I.5.

I.4. Differential inequalities in the viscosity sense. In this section we treat some elementary inequalities in the viscosity sense. The first result concerns the one dimensional case.

PROPOSITION I.11. Let $T > 0$ and $g, h \in C([0, T])$. Assume $g$ is a viscosity solution of

$$
g ^ {\prime} \leqslant h\tag{1.16}
$$

in ]0, T[. Then

$$
g (t) \leqslant g (s) + \int_ {s} ^ {t} h (\tau) d \tau \quad f o r 0 \leqslant s \leqslant t \leqslant T.\tag{1.17}
$$

PROOF. It is enough to show (1.17) for $s = 0$ and for this it suffices to prove that for $\varepsilon > 0$

$$
g (t) \leqslant g (0) + \int_ {0} ^ {t} h (s) d s + \varepsilon + \varepsilon t, \quad 0 \leqslant t \leqslant T.\tag{1.18}
$$

Assume (1.18) is false and let $\bar{t} \in ]0$, $T[$ be the least $t$ for which equality holds in (1.18). Set $\psi(t) = g(0) + \int_0^t h(s) ds + \varepsilon$ and note $\psi(0) > g(0)$, $\psi(\bar{t}) < g(\bar{t})$. Choose $\delta > 0$ such that $\psi(t) > g(t)$ on $[0, \delta]$ and $\eta \in C^1([0, T])^+$ such that $\eta' < 0$ on $[\delta, T]$ and $\eta(T) = 0$. Then there is a $t_0 \in E_+(\eta(g - \psi))$ and $t_0 \in ]\delta$, $T[$. By Theorem I.3

$$
- \frac {\eta^ {\prime} (t _ {0})}{\eta (t _ {0})} (g (t _ {0}) - \psi (t _ {0})) + \psi^ {\prime} (t _ {0}) \leqslant h (t _ {0}).
$$

Since $\eta'(t_0) < 0$ we have $\psi'(t_0) = h(t_0) < h(t_0)$ which is a contradiction.

REMARK 1.19. It follows from Proposition I.11 that (1.16) holds in the viscosity sense if and only if it holds in the sense of distributions.

COROLLARY I.12. Let $T > 0$, $\gamma \in \mathbb{R}$ and $g, h \in C([0, T])$. Let $g$ be a viscosity solution of

(1.20)

$$
g ^ {\prime} + \gamma g \leqslant h \quad o n ] 0, T [.\tag{Then}
$$

$$
e ^ {\gamma t} g (t) \leqslant e ^ {\gamma s} g (s) + \int_ {s} ^ {t} e ^ {\gamma \tau} h (\tau) d \tau \quad f o r 0 \leqslant s \leqslant t \leqslant T.\tag{1.21}
$$

PROOF. By Remark 1.19, (1.20) holds in the sense of distributions and then it is known that (1.21) holds. (Of course, one could prove (1.21) directly by adapting the proof of the proposition or by using Corollary I.7 to find $(e^{\gamma t}g)' \leqslant e^{\gamma t}h$ in the viscosity sense.)

In the next result we show that u is a viscosity subsolution of

$$
\frac {\partial}{\partial y _ {1}} u (y _ {1}, y _ {2}, \dots , y _ {m}) = g (y _ {1}, \dots , y _ {m})\tag{1.22}
$$

exactly when the corresponding statement holds for the functions of one variable $r \to u(r, y_2, \ldots, y_m)$ obtained by fixing $(y_2, \ldots, y_m)$.

PROPOSITION I.13. Let $u, g \in C(\mathcal{O})$. For $z = (y_2, \ldots, y_m) \in \mathbf{R}^{M-1}$, let $\mathcal{O}_z = \{r: (r, z) \in \mathcal{O}\}$. Let $u_z(r) = u(r, z)$, $g_z(r) = g(r, z)$ on $\mathcal{O}_z$. Then the following are equivalent:

(1.23)

$$
\left\{ \begin{array}{l} \text { For   each } z \in \mathbf {R} ^ {M - 1}, u _ {z} \text { is   a   viscosity   solution   of } \\ u _ {z} ^ {\prime} \leqslant g _ {z} \text { in } \vartheta_ {z}. \end{array} \right.\tag{1.24}
$$

$$
\left\{ \begin{array}{l} u \text {   is   a   viscosity   subsolution   of } \\ \frac {\partial}{\partial y _ {1}} u (y _ {1}, \dots , y _ {m}) = g (y _ {1}, \dots , y _ {m}) \text {   in   } \mathcal {O}. \end{array} \right.
$$

PROOF. We show (1.24) implies (1.23). Let $z_0 \in \mathbb{R}^{m-1}$ be such that $\mathcal{O}_{z_0} \neq \emptyset$. Let $\eta \in \mathfrak{D}(\mathcal{O}_{z_0})^+$, $k \in \mathbb{R}$ and $r_0 \in E_+ (\eta(u_{z_0} - k): \mathcal{O}_{z_0})$. Using Lemma I.4 in the usual way we may assume $\{r_0\} = E_+ (\eta(u_{z_0} - k): \mathcal{O}_{z_0})$. Pick $\varphi \in \mathfrak{D}(B(z_0, 1))^+$ such that $\varphi(z_0) = 1$. Set $\varphi_\varepsilon(z) = \varphi(z/\varepsilon)$. For $\varepsilon > 0$ and small, $\eta(y_1)\varphi_\varepsilon(y_2, \ldots, y_m) \in \mathfrak{D}(\mathcal{O})^+$ and there exists $(r_\varepsilon, z_\varepsilon) \in E_+( \eta\varphi(u - k): \mathcal{O})$. By assumption,

$$
- \frac {\eta^ {\prime} (r _ {\varepsilon})}{\eta (r _ {\varepsilon})} (u (r _ {\varepsilon}, z _ {\varepsilon}) - k) \leqslant g (r _ {\varepsilon}, z _ {\varepsilon}).\tag{1.25}
$$

Clearly $z_{\varepsilon} \to z_0$ and $r_{\varepsilon} \to r_0$ as $\varepsilon \downarrow 0$. Thus the result follows by letting $\varepsilon \downarrow 0$ in (1.25).

It remains to show that  $(1.23)$  implies  $(1.24)$ . However, this amounts to checking the definitions and is left to the reader.

The next result is concerned with more general directional derivatives.

THEOREM I.14. Let $\pmb{\nu}\colon\mathcal{O}\to\mathbb{R}^{M}$ be continuously differentiable. Denote by $Y(\tau,y_{0})$ the solution of

$$
\left\{ \begin{array}{l} \frac {d Y}{d \tau} = \nu (Y), \\ Y (0, y _ {0}) = y _ {0}, \end{array} \right.\tag{1.26}
$$

which is defined on a maximal interval of existence $I_{y_0}$. (By assumption $Y(I_{y_0}, y_0) \subset \mathcal{O}$.) Let $u, g \in C(\mathcal{O})$ and $u$ be a viscosity solution of

$$
(D u) \cdot v \leqslant g \quad i n \mathcal {O}.\tag{1.27}
$$

Then for $y_0 \in \mathcal{O}$, $s, t \in I_{y_0}$ and $s \leqslant t$ one has

$$
u \big (Y (t, y _ {0}) \big) - u \big (Y (s, y _ {0}) \big) \leqslant \int_ {s} ^ {t} g \big (Y (\tau , y _ {0}) \big) d \tau .\tag{1.28}
$$

PROOF. If  $\nu(y_{0})=0$ , then  $Y(\tau,y_{0})\equiv y_{0}$  and there is nothing to show. If  $\nu(y_{0})\neq0$ , we may rotate coordinates so that  $\nu(y_{0})=(\nu_{1}(y_{0}),0,\ldots,0)$ . Without loss of generality we also assume  $y_{0}=0$ . Consider the change of variables  $\Phi$  defined near  $y_{0}=0$  by

$$
\Phi \left(y _ {1}, \dots , y _ {m}\right) = \left(\hat {y} _ {1}, \dots , \hat {y} _ {m}\right) \Leftrightarrow \left(y _ {1}, \dots , y _ {m}\right) = Y \left(\hat {y} _ {1}, \left(0, \hat {y} _ {2}, \dots , \hat {y} _ {m}\right)\right).
$$

Then, with the notation of Corollary I.7 and $H(y, r, p) = p \cdot \nu(y) - g(y)$, we have

$$
\begin{array}{c} G (\hat {y}, r, p) = p D \Phi \big (\Phi^ {- 1} (\hat {y}) \big) \cdot \nu \big (\Phi^ {- 1} (\hat {y}) \big) - g \big (\Phi^ {- 1} (\hat {y}) \big) \\ = p _ {1} - g \big (\Phi^ {- 1} (\hat {y}) \big). \end{array}
$$

(Of course, this is merely the statement that $\partial/\partial\hat{y}_{1}=\nu\cdot(\partial/\partial y_{1},\ldots,\partial/\partial y_{m})$.) Thus, by Corollary I.7, $u(\Phi^{-1}(\hat{y}))$ is a viscosity solution of

$$
\frac {\partial}{\partial \hat {y} _ {1}} u \leqslant g (\Phi^ {- 1} (\hat {y})).
$$

Propositions I.13 and I.11 then yield

$$
u \left(\Phi^ {- 1} (t, 0, \dots , 0)\right) - u \left(\Phi^ {- 1} (s, 0, \dots , 0)\right) \leqslant \int_ {s} ^ {t} g \left(\Phi^ {- 1} (\tau , 0, \dots , 0)\right) d \tau .
$$

for $s \leqslant t$ and $|s|, |t|$ small. But this means

$$
u (I (t, 0)) - u (Y (s, 0)) \leqslant \int_ {s} ^ {t} g (Y (\tau , 0)) d \tau .
$$

While this inequality is only established for $|s|, |t|$ small, it is then trivially extendable to $t, s \in I_0, s \leqslant t$.

COROLLARY I.15. Let $\mathcal{O}$ be convex, $u \in C(\mathcal{O})$ and $L \in \mathbb{R}$. If for every $\varphi \in \mathfrak{D}(\mathcal{O})^+$ and $k \in \mathbb{R}$

$$
\frac {(u - k)}{\varphi} \mid D \varphi \mid \leqslant L \quad o n E _ {+} (\varphi (u - k))\tag{1.29}
$$

$$
\text { then } \mid u (\bar {y}) - u (\hat {y}) \mid \leqslant L \mid \bar {y} - \hat {y} \mid \text { for } \bar {y}, \hat {y} \in \mathcal {O}.
$$

PROOF. Fix $y, \hat{y} \in \mathcal{O}$ with $y \neq \hat{y}$. Put $\nu \equiv (|\bar{y} - \hat{y}|)^{-1}(\bar{y} - \hat{y})$. From (1.29) it follows that $u$ is a viscosity solution of $Du \cdot \nu \leqslant L$ in $\mathcal{O}$. By Theorem I.14

$$
u \left(y _ {0} + t \nu\right) - u \left(y _ {0} + s \nu\right) \leqslant \int_ {s} ^ {t} L d \tau = L (t - s)
$$

whenever $s \leqslant t$ and $y_0, y_0 + tv, y_0 + sv \in \mathcal{O}$. Set $y_0 = \hat{y}, t = |\bar{y} - \hat{y}|$, $s = 0$ to obtain $u(\bar{y}) - u(\hat{y}) \leqslant L|\bar{y} - \hat{y}|$. Since we may interchange $\bar{y}$ and $\hat{y}$, the proof is complete.

I.5. Characterization of points in some  $E_{+}(\varphi(u-\psi))$ . According to Theorem I.3, if u is a viscosity solution of  $F \leqslant 0$ , then

$$
F \left(y, u, - \frac {(u - \psi)}{\varphi} D \varphi + D \psi\right) \leqslant 0 \quad \text { on } E _ {+} (\varphi (u - \psi)) \cap d (\varphi) \cap d (\psi).
$$

One is naturally led to ask: What are the points $y$ belonging to some $E_{+}(\varphi(u - \psi)) \cap d(\varphi) \cap d(\psi)$ and what are the possible values of $-((u - \psi)(D\varphi) / \varphi) + D\psi$ at

such points? We prove

THEOREM I.16. Let $u \in C(\mathcal{O})$ and $y_0 \in \mathcal{O}$, $a \in \mathbb{R}^M$. Then the problem

$$
\left\{ \begin{array}{l} y _ {0} \in E _ {+} (\varphi (u - \psi)) \cap d (\varphi) \cap d (\psi), \\ - \frac {u (y _ {0}) - \psi (y _ {0})}{\varphi (y _ {0})} D \varphi (y _ {0}) + D \psi (y _ {0}) = a \end{array} \right.\tag{1.30}
$$

has a solution $\varphi \in C(\mathfrak{O})^{+}$, $\psi \in C(\mathfrak{O})$ if and only if there exists $\tilde{\psi} \in C^{1}(\mathfrak{O})$ such that $y_{0}$ is a local maximum point for $u - \tilde{\psi}$ and $D\tilde{\psi}(y_0) = a$. If $E_{+}$ is replaced by $E_{-}$ in (1.30) and “maximum” is replaced by “minimum” the statement is true.

PROOF. We first observe the sufficiency. Let $\tilde{\psi} \in C^{1}(\mathcal{O})$ and $y_{0}$ be a local maximum for $u - \tilde{\psi}$. Assume, changing $\tilde{\psi}$ by a constant if necessary, that $u(y_{0}) = \tilde{\psi}(y_{0})$. Choose $\varphi \in C^{1}(\mathcal{O})^{+}$ with a strict maximum value of 1 at $y_{0}$ and $\operatorname{supp} \varphi \subset \{\tilde{\psi} \geqslant u\}$. Then $y_{0} \in E_{+}(\varphi(u - \tilde{\psi} + 1))$ and

$$
- \frac {u (y _ {0}) - \tilde {\psi} (y _ {0}) + 1}{\varphi (y _ {0})} D \varphi (y _ {0}) + D \tilde {\psi} (y _ {0}) = D \tilde {\psi} (y _ {0})
$$

since $D\varphi(y_0) = 0$. The necessity is equally simple. Since $y_0 \in E_+(\varphi(u - \psi)) \cap d(\varphi) \cap d(\psi)$ implies

$$
u (y) \leqslant \frac {1}{\varphi (y)} \left(\varphi (y _ {0}) \big (u (y _ {0}) - \psi (y _ {0}) \big)\right) + \psi (y)
$$

near $y_0$ and the right-hand side is differentiable at $y_0$ with the derivative

$$
- \frac {u (y _ {0}) - \psi (y _ {0})}{\varphi (y _ {0})} D \varphi (y _ {0}) + D \psi (y _ {0}),
$$

we may majorize it near $y_0$ by a $\tilde{\psi} \in C^1(\mathcal{O})$ which agrees to first order at $y_0$ (Lemma I.4). This completes the proof.

REMARK 1.31. By Lemma I.4 we may equally well characterize the pairs $(y_0, a)$ for which (1.30) has a solution by the condition

$$
\lim _ {y \rightarrow y _ {0}} \frac {\max \left\{u (y) - \left(u \left(y _ {0}\right) + a \cdot \left(y - y _ {0}\right)\right) , 0 \right\}}{| y - y _ {0} |} = 0.
$$

COROLLARY I.17. Let $u \in C(\mathcal{O})$. Then

$$
A _ {+} = \left\{y _ {0} \in \mathcal {O}: \exists \tilde {\psi} \in C ^ {1} (\mathcal {O}), \tilde {\psi} (y _ {0}) = u (y _ {0}) a n d \tilde {\psi} \geqslant u n e a r y _ {0} \right\}
$$

is dense in $\mathcal{O}$. Similarly, the set $A_{-}$ defined as above with $\tilde{\psi} \geqslant u$ replaced by $u \geqslant \tilde{\psi}$ is dense in $\mathcal{O}$.

PROOF. If $y_0 \in \mathcal{O}$ and $\varepsilon > 0$, choose $\varphi \in C_c^1(\mathcal{O})^+$ so that $\varphi(y_0) > 0$ and $\operatorname{supp} \varphi \subset B(y_0, \varepsilon)$. Then $E_+(u - (u(y_0) - 1)))$ is nonempty and it follows from Theorem I.16 that it is contained in $B(y_0, \varepsilon) \cap A_+$, hence the result.

REMARK 1.32. One cannot expect $A_{+}$ to be much more than dense (e.g., of full measure, second category, etc.) since $A_{+} \cap A_{-} = d(u)$ may well be empty.

We may also use these results to reformulate the notion of a viscosity solution as follows.

Let $u \in C(\mathcal{O})$ and $y_0 \in \mathcal{O}$. Set

$$
D ^ {+} u \left(y _ {0}\right) = \left\{a \in \mathbf {R} ^ {N}: \lim _ {y \rightarrow y _ {0}} \frac {\left(u (y) - u \left(y _ {0}\right) - a \cdot \left(y - y _ {0}\right)\right) ^ {+}}{\left| y - y _ {0} \right|} = 0 \right\}
$$

and

$$
D ^ {-} u \left(y _ {0}\right) = \left\{a \in \mathbf {R} ^ {N}: \lim _ {y \rightarrow y _ {0}} \frac {\left(u (y) - u \left(y _ {0}\right) - a \cdot \left(y - y _ {0}\right)\right) ^ {-}}{\left| y - y _ {0} \right|} = 0 \right\},
$$

where  $r^{+} = \max(r,0)$ ,  $r^{-} = -\min(r,0)$ . In general,  $D^{\pm}u(y_{0})$  may be empty, but by Corollary I.17 each is nonempty for a dense set of  $y_{0} \in \varnothing$ . The next result is an immediate consequence of the above considerations.

PROPOSITION I.18. Let $u \in C(\mathcal{O})$. Then:

(i) $u$ is a viscosity solution of $F \leqslant 0$ if and only if

$$
F (y, u (y), a) \leqslant 0 \quad \text {   for   every   } y \in \mathcal {O} \text {   and   } a \in D ^ {+} u (y).\tag{1.33}
$$

(ii) $u$ is a viscosity solution $F \geqslant 0$ if and only if

$$
F (y, u (y), a) \geqslant 0 \quad \text {   for   every   } y \in \mathcal {O} \text {   and   } a \in D ^ {-} u (y).\tag{1.34}
$$

(iii) $u$ is a viscosity solution of $F = 0$ if and only if (1.33) and (1.34) hold.

One can use Proposition I.18 to give another proof of Theorem I.10.

II. Uniqueness for the Dirichlet problem in $\mathbf{R}^N$. In §II.1 we treat the simple case

$$
u + H (D u) = n (x) \quad \text { in } \mathbf {R} ^ {N}.\tag{2.1}
$$

After this the general case

$$
H (x, u, D u) = 0 \quad \text { in } \mathbf {R} ^ {N},\tag{2.2}
$$

which involves technical assumptions, is discussed.

II.1. The equation $u + H(Du) = n(x)$. We consider two problems

$$
\left\{ \begin{array}{l l} (\mathrm{i}) & u + H (D u) = n (x), \\ (\mathrm{ii}) & v + H (D v) = m (x), \end{array} \right.\tag{2.3}
$$

where

$$
H \in C (\mathbf {R} ^ {N}), \quad n \in \operatorname{BUC} (\mathbf {R} ^ {N}), \quad m \in \operatorname{BUC} (\mathbf {R} ^ {N}).\tag{2.4}
$$

The main result concerning (2.3) is

THEOREM II.1. Let (2.4) hold. Let $u, v \in C_b(\mathbf{R}^N)$ be a viscosity subsolution and a viscosity supersolution of (2.3)(i) and (ii) respectively. Then

$$
\left\| (u - v) ^ {+} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant \left\| (n - m) ^ {+} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})}. ^ {8}\tag{2.5}
$$

REMARK 2.6. It follows from (2.5) that $n \leqslant m$ implies $u \leqslant v$. It is also an immediate consequence of the theorem that if $u, v$ are viscosity solutions of their

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{8}r^{+}(r^{-})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{8}r^{+}(r^{-})$ denotes the maximum of r (respectively, -r) and 0.</span></small>

respective problems, then  $\|(\boldsymbol{u}-\boldsymbol{v})\|_{L^{\infty}(\mathbb{R}^{N})}\leqslant\|(n-m)\|_{L^{\infty}(\mathbb{R}^{N})}$ . In particular, bounded viscosity solutions of (2.1) are unique.

PROOF OF THEOREM II.1. The basic arguments are best illustrated by first running through the proof under the stronger assumption

$$
u (x) \rightarrow 0 \quad \text { and } \quad v (x) \rightarrow 0 \quad \text { as } | x | \rightarrow \infty .\tag{2.7}
$$

The condition (2.7) is natural if $H(0) = 0$ and $n, m \to 0$ at $\infty$. After the proof is sketched for the case (2.7), we give the general argument.

Case 1. $u, v \to 0$ as $|x| \to \infty$. If $u(x) \leqslant v(x)$ everywhere there is nothing to show. Hence assume $u(\bar{x}) - v(\bar{x}) > 0$ for some $\bar{x}$. Let $\varphi \in \mathfrak{D}(\mathbb{R}^N)^+$, $0 \leqslant \varphi \leqslant 1$, and $\varphi(0) = 1$. Define

$$
M = \max _ {\mathbf {R} ^ {N} \times \mathbf {R} ^ {N}} (\varphi (x - y) (u (x) - v (y))).\tag{2.8}
$$

The maximum in (2.8) is assumed and $M > 0$ since $\varphi(\bar{x} - \bar{x})(u(\bar{x}) - v(\bar{x})) = u(\bar{x}) - v(\bar{x}) > 0$ while $\varphi(x - y)(u(x) - v(y)) \to 0$ as $|x| + |y| \to \infty$ by (2.7) and $\varphi \in \mathfrak{D}(\mathbf{R}^N)$. Notice also that for $x \in \mathbf{R}^N$

$$
u (x) - v (x) = \varphi (x - x) (u (x) - v (x)) \leqslant M
$$

so

$$
\left\| (u - v) ^ {+} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant M.\tag{2.9}
$$

Let $M = \varphi(x_0 - y_0)(u(x_0) - v(y_0))$, $k_1 = v(y_0)$, $k_2 = u(x_0)$. We then have

$$
x _ {0} \in E _ {+} (\varphi (\cdot - y _ {0}) (u (\cdot) - k _ {1})) \quad \text { and } \quad y _ {0} \in E _ {-} (\varphi (x _ {0} - \cdot) (v (\cdot) - k _ {2})).
$$

It now follows from Theorem I.3 and the assumptions that

$$
u \left(x _ {0}\right) + H \left(- \frac {u \left(x _ {0}\right) - v \left(y _ {0}\right)}{\varphi \left(x _ {0} - y _ {0}\right)} (D \varphi) \left(x _ {0} - y _ {0}\right)\right) \leqslant n \left(x _ {0}\right),
$$

$$
v (y _ {0}) + H \left(- \frac {u (x _ {0}) - v (y _ {0})}{\varphi (x _ {0} - y _ {0})} (D \varphi) (x _ {0} - y _ {0})\right) \geqslant m (y _ {0})
$$

where we used  $D_{x}(\varphi(x-y)) = -D_{y}(\varphi(x-y))$ . Subtracting the above inequalities yields

$$
u \left(x _ {0}\right) - v \left(y _ {0}\right) \leqslant n \left(x _ {0}\right) - m \left(y _ {0}\right) = n \left(y _ {0}\right) - m \left(y _ {0}\right) + n \left(x _ {0}\right) - n \left(y _ {0}\right).\tag{2.10}
$$

Choosing $\varphi$ to be supported in $B(0, \alpha)$ (so $|x_0 - y_0| \leqslant \alpha$), (2.10) and $0 \leqslant \varphi \leqslant 1$ imply

$$
M \leqslant \| (n - m) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} + \rho_ {n} (\alpha)
$$

where the modulus of continuity $\rho_{n}$ of $n$ is given by

$$
\rho_ {n} (\alpha) = \sup \left\{\mid n (x) - n (y) \mid : \mid x - y \mid \leqslant \alpha \right\}.\tag{2.11}
$$

Since $n \in \mathrm{BUC}(\mathbb{R}^N)$, we have $\rho_n(\alpha) \to 0$ as $\alpha \to 0$ and the result follows.

Case 2. The general case. Let $\varphi \in \mathfrak{D}(\mathbf{R}^N)^+$ be as above: $0 \leqslant \varphi \leqslant 1$, $\varphi(0) = 1$ and $\operatorname{supp} \varphi \subset B(0, \dot{\alpha})$. We are first going to prove, via a truncation argument, that

$$
M = \sup _ {x, y \in \mathbf {R} ^ {N}} \varphi (x - y) (u (x) - v (y)) \leqslant \| (n - m) ^ {+} \| _ {L ^ {\infty} (\mathbb {R} ^ {N})} + \rho_ {n} (\alpha)\tag{2.12}
$$

where  $\rho_{n}$  is given by (2.11). The result then follows as before. (The difference between this case and the previous one is that we cannot write “max” in place of “sup” in (2.12).) We may assume M > 0.

REMARK (ADDED IN PROOF). We belatedly observe that the proof below can be improved by using the maximum of  $\varphi(x-y)\exp(-\varepsilon(|x|^{2}+|y|^{2}))(u(x)-v(y))$  in place of  $M_{\varepsilon}$  below or by noting that  $\varepsilon|x_{\varepsilon}|^{2}\to0$  (which improves (2.13)).

Let $\varepsilon > 0$,

$$
M _ {\varepsilon} = \max _ {x, y \in \mathbf {R} ^ {N}} \varphi (x - y) \left(e ^ {- \varepsilon | x | ^ {2}} u (x) - e ^ {- \varepsilon | y | ^ {2}} v (y)\right),
$$

and

$$
M _ {\varepsilon} = \varphi (x _ {\varepsilon} - y _ {\varepsilon}) \left(e ^ {- \varepsilon | x _ {\varepsilon} | ^ {2}} u (x _ {\varepsilon}) - e ^ {- \varepsilon | y _ {\varepsilon} | ^ {2}} v (y _ {\varepsilon})\right).
$$

Let us first prove that $M_{\varepsilon} \to M$ as $\varepsilon \downarrow 0$. Since $u$ and $v$ are continuous it is clear that

$$
\varliminf_ {\varepsilon \downarrow 0} M _ {\varepsilon} \geqslant M > 0.
$$

Hence, for $\varepsilon$ small, $M_{\varepsilon} \geqslant M / 2$. Moreover, $|x_{\varepsilon} - y_{\varepsilon}| \leqslant \alpha$, and one then easily deduces that

$$
\sqrt {\varepsilon} \mid x _ {\varepsilon} \mid , \sqrt {\varepsilon} \mid y _ {\varepsilon} \mid \leqslant C\tag{2.13}
$$

for some $C$ independent of $\varepsilon$. Now

$$
\begin{array}{l} M _ {\varepsilon} = \varphi (x _ {\varepsilon} - y _ {\varepsilon}) \left(e ^ {- \varepsilon | x _ {\varepsilon} | ^ {2}} u (x _ {\varepsilon}) - e ^ {- \varepsilon | y _ {\varepsilon} | ^ {2}} v (y _ {\varepsilon})\right) \\ \leqslant \varphi (x _ {\varepsilon} - y _ {\varepsilon}) \left(u (x _ {\varepsilon}) - e ^ {\varepsilon (| x _ {\varepsilon} | ^ {2} - | y _ {\varepsilon} | ^ {2})} v (y _ {\varepsilon})\right) \\ \leqslant \varphi (x _ {\varepsilon} - y _ {\varepsilon}) \left(u (x _ {\varepsilon}) - v (y _ {\varepsilon}) + \left(1 - e ^ {\varepsilon (| x _ {\varepsilon} | ^ {2} - | y _ {\varepsilon} | ^ {2})}\right) v (y _ {\varepsilon})\right) \\ \leqslant M + | 1 - e ^ {\varepsilon (| x _ {\varepsilon} | ^ {2} - | y _ {\varepsilon} | ^ {2})} | | v (y _ {\varepsilon}) |. \end{array}\tag{2.14}
$$

However, $|\varepsilon (|x_{\varepsilon}|^2 - |y_{\varepsilon}|^2)| = \varepsilon |(x_{\varepsilon} - y_{\varepsilon}, x_{\varepsilon} + y_{\varepsilon})| \leqslant \sqrt{\varepsilon} 2\alpha C$ by (2.13). Therefore, by the above, $\varliminf_{\varepsilon \downarrow 0} M_{\varepsilon} \leqslant M$ and we have $M_{\varepsilon} \to M$ as $\varepsilon \downarrow 0$.

We next prove (2.12). By

$$
\left\{ \begin{array}{l} x _ {\varepsilon} \in E _ {+} \big (\varphi (\cdot - y _ {\varepsilon}) e ^ {- \varepsilon | \cdot | ^ {2}} \big (u (\cdot) - \psi_ {1} (\cdot)) \big), \psi_ {1} (x) = e ^ {\varepsilon (| x | ^ {2} - | y _ {\varepsilon} | ^ {2})} v \big (y _ {\varepsilon} \big), \\ y _ {\varepsilon} \in E _ {-} \big (\varphi (x _ {\varepsilon} - \cdot) e ^ {- \varepsilon | \cdot | ^ {2}} \big (v (\cdot) - \psi_ {2} (\cdot)) \big), \psi_ {2} (y) = e ^ {\varepsilon (| y | ^ {2} - | x _ {\varepsilon} | ^ {2})} u (x _ {\varepsilon}), \end{array} \right.
$$

and Theorem I.3 we have

$$
\left\{ \begin{array}{l} u \left(x _ {\varepsilon}\right) + H \left(- \left(u \left(x _ {\varepsilon}\right) - k _ {1}\right) \frac {(D \varphi) \left(x _ {\varepsilon} - y _ {\varepsilon}\right)}{\varphi \left(x _ {\varepsilon} - y _ {\varepsilon}\right)} + 2 \varepsilon u \left(x _ {\varepsilon}\right) x _ {\varepsilon}\right) \leqslant n \left(x _ {\varepsilon}\right), \\ k _ {1} = e ^ {\varepsilon \left(\left| x _ {\varepsilon} \right| ^ {2} - \left| y _ {\varepsilon} \right| ^ {2}\right)} v \left(y _ {\varepsilon}\right) \end{array} \right.\tag{2.15}
$$

and

$$
\left\{ \begin{array}{l} v (y _ {\varepsilon}) + H \left(- \left(k _ {2} - v (y _ {\varepsilon})\right) \frac {(D \varphi) (x _ {\varepsilon} - y _ {\varepsilon})}{\varphi (x _ {\varepsilon} - y _ {\varepsilon})} + 2 \varepsilon v (y _ {\varepsilon}) y _ {\varepsilon}\right) \geqslant m (y _ {\varepsilon}), \\ k _ {2} = e ^ {\varepsilon (| y _ {\varepsilon} | ^ {2} - | x _ {\varepsilon} | ^ {2})} u (x _ {\varepsilon}). \end{array} \right.\tag{2.15)'}
$$

Set

$$
\left\{ \begin{array}{l} \lambda_ {\varepsilon} = - (u (x _ {\varepsilon}) - v (y _ {\varepsilon})) \frac {D \varphi (x _ {\varepsilon} - y _ {\varepsilon})}{\varphi (x _ {\varepsilon} - y _ {\varepsilon})}, \\ \delta_ {\varepsilon} = - (1 - \exp (\varepsilon (| x _ {\varepsilon} | ^ {2} - | y _ {\varepsilon} | ^ {2}))) v (y _ {\varepsilon}) \frac {(D \varphi) (x _ {\varepsilon} - y _ {\varepsilon})}{\varphi (x _ {\varepsilon} - y _ {\varepsilon})} + 2 \varepsilon u (x _ {\varepsilon}) x _ {\varepsilon}, \\ \tilde {\delta} _ {\varepsilon} = (1 - \exp (\varepsilon (| y _ {\varepsilon} | ^ {2} - | x _ {\varepsilon} | ^ {2}))) u (x _ {\varepsilon}) \frac {(D \varphi) (x _ {\varepsilon} - y _ {\varepsilon})}{\varphi (x _ {\varepsilon} - y _ {\varepsilon})} + 2 \varepsilon v (y _ {\varepsilon}) y _ {\varepsilon}. \end{array} \right.\tag{2.16}
$$

Subtracting the inequalities of (2.15) and (2.15)' yields (recall (2.14))

$$
\begin{array}{l}M _ {\varepsilon} + H \left(\lambda_ {\varepsilon} + \delta_ {\varepsilon}\right) - H \left(\lambda_ {\varepsilon} + \tilde {\delta} _ {\varepsilon}\right) \leqslant n \left(x _ {\varepsilon}\right) - m \left(y _ {\varepsilon}\right) + g (\varepsilon)\\\quad \leqslant \| (n - m) ^ {+} \| _ {L ^ {\infty} \left(\mathbb {R} ^ {N}\right)} + \rho_ {n} (\alpha) + g (\varepsilon), \quad \text { where } g (\varepsilon) \rightarrow 0 \text { as } \varepsilon \downarrow 0.\end{array}
$$

The proof is completed by showing that $\lambda_{\varepsilon}$ remains bounded as $\varepsilon \downarrow 0$ while $\delta_{\varepsilon}$ and $\tilde{\delta}_{\varepsilon} \to 0$, for then letting $\varepsilon \downarrow 0$ above yields (2.12). Since $M_{\varepsilon} \geqslant M / 2 > 0$ for $\varepsilon$ small, $\varphi(x_{\varepsilon} - y_{\varepsilon})$ is bounded away from zero, proving $\lambda_{\varepsilon}$ remains bounded. Similarly, $\delta_{\varepsilon}, \tilde{\delta}_{\varepsilon}$ tend to zero for $\varepsilon x_{\varepsilon}, \varepsilon y_{\varepsilon}$ and $\varepsilon(|x_{\varepsilon}|^{2} - |y_{\varepsilon}|^{2})$ tends to zero by (2.13) and the remarks thereafter. This completes the proof.

REMARK 2.17. The proof (especially Case 1) is vaguely reminiscent of the proof of uniqueness of entropy solutions of conservation laws in S. N. Kružkov [21].

REMARK 2.18. The proofs given used only that n is uniformly continuous and m is continuous. Similarly, we could have used uniform continuity of m and continuity of n. Boundedness of n and m is irrelevant, although the result is not very interesting if n - m is not bounded above. We do not know if the result holds without uniform continuity of at least one of n and m. It is also possible, for example, to replace the boundedness assumptions on u and v by  $|u|$ ,  $|v| \leq C(1 + |x|^p)$ , 0 < p < 1, if either H is bounded and uniformly continuous or u and v are Lipschitz continuous. We conjecture that one can take p = 1 if u and v are Lipschitz continuous.

II.2 The equation $H(x, u, Du) = n(x)$. It will be assumed throughout that $H(x, r, p)$ satisfies

$$
\left\{ \begin{array}{l} \text { For   each } R > 0, H \text { is   uniformly   continuous } \\ \text { on } \mathbf {R} ^ {N} \times [ - R, R ] \times B (0, R), \end{array} \right.\tag{2.19}
$$

and

$$
\left\{ \begin{array}{l} \text { For   each } R > 0 \text { there   is   a   continuous   nondecreasing   function } \\ \gamma_ {R} \colon [ 0, 2 R ] \to \mathbf {R} \text { such   that } \gamma_ {R} (0) = 0 \text { and } \\ \big (H (x, r, p) - H (x, s, p) \big) \geqslant \gamma_ {R} (r - s) \\ \text { for } x \in \mathbf {R} ^ {N}, p \in \mathbf {R} ^ {N}, - R \leqslant s \leqslant r \leqslant R. \end{array} \right.\tag{2.20}
$$

We will need to restrict the nature of the joint continuity of $H$. The condition (2.21)

$$
\lim _ {\varepsilon \downarrow 0} \sup \left\{\left| H (x, r, p) - H (y, r, p) \right|: | x - y | (1 + | p |) \leqslant \varepsilon , | r | \leqslant R \right\} = 0
$$

$$
\text { for   all } R > 0,
$$

and the stronger requirement

$$
\lim _ {\varepsilon \downarrow 0} \sup \left\{\left| H (x, r, p) - H (y, r, p) \right|: | x - y | | p | \leqslant R _ {1}, | x - y | \leqslant \varepsilon , | r | \leqslant R _ {2} \right\} = 0\tag{2.21*}
$$

$$
\text { for   all } R _ {1}, R _ {2} > 0,
$$

will be used.

We may now state our main result.

THEOREM II.2. Let u be a bounded viscosity subsolution of  $H(x, u, Du) = 0$  and v be a bounded viscosity supersolution of  $H(x, v, Dv) = m(x)$  where  $m \in C_b(\mathbb{R}^N)$ . Let (2.19) and (2.20) hold,  $R_0 = \max(\|u\|_{L^\infty(\mathbb{R}^N)}, \|v\|_{L^\infty(\mathbb{R}^N)})$  and  $\gamma = \gamma_{R_0}$  as in (2.19). Then:

(i) If $(2.21^{*})$ holds we have

$$
\left\| \gamma \left(\left(u - v\right) ^ {+}\right) \right\| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)} \leqslant \left\| m ^ {+} \right\| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)}.\tag{2.22}
$$

(ii) If (2.21) holds and $u, v \in \mathbf{BUC}(\mathbb{R}^N)$, then (2.22) holds.

(iii) If $u, v \in W^{1,\infty}(\mathbf{R}^N)$, then (2.22) holds.

REMARK 2.23. Remarks analogous to (2.6) and (2.18) apply to Theorem II.2.

REMARK 2.24. It is not possible to relax the assumptions (2.21) and (2.21\*) in an essential way. This can be seen in the linear case $H(x, r, p) = r + b(x) \cdot p$, where (2.21) is equivalent to the Lipschitz continuity of $b$. See §V.4 concerning this remark.

PROOF OF THEOREM II.2. With the notation and assumptions of step 2 in the proof of Theorem I.2 we have, in the same way,

$$
H \left(x _ {\varepsilon}, u \left(x _ {\varepsilon}\right), \lambda_ {\varepsilon} + \delta_ {\varepsilon}\right) - H \left(y _ {\varepsilon}, v \left(y _ {\varepsilon}\right), \lambda_ {\varepsilon} + \tilde {\delta} _ {\varepsilon}\right) \leqslant \| m ^ {+} \| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)},\tag{2.25}
$$

where $\lambda_{\varepsilon},\delta_{\varepsilon},\tilde{\delta}_{\varepsilon}$ are given by (2.16). Rewrite (2.25) as

$$
\begin{array}{l} \big (H \big (x _ {\varepsilon}, u (x _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon} \big) - H \big (x _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon} \big) \big) \\ \quad + \big (H \big (x _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon} \big) - H \big (y _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon} \big) \big) \\ \quad + \big (H \big (y _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon} \big) - H \big (y _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \tilde {\delta} _ {\varepsilon} \big) \big) \leqslant \| m ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}. \end{array}
$$

By (2.20), (2.14) and $\gamma = \gamma_{R_0}$, this implies

$$
\gamma \big (M _ {\varepsilon} + g (\varepsilon) \big) \leqslant \| m ^ {+} \| _ {L ^ {\infty} (\mathbb {R} ^ {N})} + A _ {\varepsilon} + B _ {\varepsilon}\tag{2.26}
$$

where $\lim_{\varepsilon \downarrow 0}g(\varepsilon) = 0$ and

$$
\left\{ \begin{array}{l} A _ {\varepsilon} = | H (x _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon}) - H (y _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon}) |, \\ B _ {\varepsilon} = | H (y _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \delta_ {\varepsilon}) - H (y _ {\varepsilon}, v (y _ {\varepsilon}), \lambda_ {\varepsilon} + \tilde {\delta} _ {\varepsilon}) |. \end{array} \right.\tag{2.27}
$$

As we showed before, $\delta_{\varepsilon}, \tilde{\delta}_{\varepsilon} \to 0$ while $\lambda_{\varepsilon}$ remains bounded. Thus, by (2.19), $B_{\varepsilon} \to 0$ as $\varepsilon \downarrow 0$. We need to estimate $A_{\varepsilon}$. To this end we reintroduce the support of $\varphi$ explicitly by replacing $\varphi$ by $\varphi_{\alpha}(x) = \varphi(x / \alpha)$ where $\varphi \in \mathfrak{D}(B(0,1))^+$, $0 \leqslant \varphi \leqslant 1$, $\varphi(0) = 1$, $D\varphi(0) = 0$. Since $\varphi((x_{\varepsilon} - y_{\varepsilon}) / \alpha)$ remains bounded away from zero as $\varepsilon \downarrow 0$ we see from (2.16) and (2.13) that

$$
\limsup _ {\varepsilon \downarrow 0} \left(\left| \lambda_ {\varepsilon} + \delta_ {\varepsilon} \right|\right) <   \frac {K}{\alpha}
$$

for some $K$. Since $|x_{\varepsilon} - y_{\varepsilon}| \leqslant \alpha$,

$$
\begin{array}{r l} \underset {\varepsilon \downarrow 0} {\lim \sup} A _ {\varepsilon} & \leqslant \sup \left\{\mid H (x, r, p) - H (y, r, p) \mid : \mid x - y \mid \leqslant \alpha , \right. \\ & \quad \left. \mid r \mid \leqslant R _ {0}, \mid x - y \mid \mid p \mid \leqslant K \mid \right\} \\ & = \Lambda (\alpha). \end{array}
$$

Then (2.25) implies $\gamma(M) \leqslant \|m^{+}\|_{L^{\infty}(\mathbf{R}^{N})} + \Lambda(\alpha)$. If (2.21\*) holds, $\Lambda(\alpha) \to 0$ as $\alpha \downarrow 0$ and this proves (i).

To establish case (ii) we will prove that $\varphi$ can be chosen so that $\lim_{\varepsilon \downarrow 0}|x_{\varepsilon} - y_{\varepsilon}| < \alpha \kappa (\alpha)$ for some $\kappa (\cdot)$ satisfying $\kappa (0 + ) = 0$. Then for $\varepsilon$ small, $|x_{\varepsilon} - y_{\varepsilon}||\lambda_{\varepsilon} + \delta_{\varepsilon}|\leqslant K\kappa (\alpha)$ and the result follows as above. Assume $v\in \mathrm{BUC}(\mathbb{R}^N)$ and let $\rho_v$ be the modulus of continuity of $v$. Recalling the proof of Theorem I.1 we have

$$
\begin{array}{l} \sup (u (x) - v (x)) \leqslant \sup \varphi \left(\frac {x - y}{\alpha}\right) (u (x) - v (y)) \leqslant \lim _ {\varepsilon \downarrow 0} M _ {\varepsilon} \\ \leqslant \underset {\varepsilon \downarrow 0} {\lim} \varphi \left(\frac {x _ {\varepsilon} - y _ {\varepsilon}}{\alpha}\right) \left((u (x _ {\varepsilon}) - v (y _ {\varepsilon})) + \| v \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} | \exp (2 \alpha C \sqrt {\varepsilon}) - 1 |\right) \\ \leqslant \underset {\varepsilon \downarrow 0} {\lim} \varphi \left(\frac {x _ {\varepsilon} - y _ {\varepsilon}}{\alpha}\right) \left((u (x _ {\varepsilon}) - v (x _ {\varepsilon})) + \rho_ {v} (\alpha) + \| v \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} | \exp (2 \alpha C \sqrt {\varepsilon}) - 1 |\right). \end{array}
$$

Without loss of generality we assume  $M_{0}=\sup(u(x)-v(x))>0$ . The above inequality then implies, with new constants  $c_{1}, c_{2}$  independent of small  $\alpha$  and  $\varepsilon$ ,

$$
\varphi \left(\frac {x _ {\varepsilon} - y _ {\varepsilon}}{\alpha}\right) \geqslant \frac {M _ {0}}{M _ {0} + \rho_ {v} (\alpha) + c _ {1} \alpha \sqrt {\varepsilon}} \geqslant 1 - c _ {2} \left(\rho_ {v} (\alpha) + c _ {1} \alpha \sqrt {\varepsilon}\right)
$$

provided that $\varepsilon$ is small enough (depending on $\alpha$). If we choose $\varphi$ to be decreasing, radial and $\varphi(x) = 1 - |x|^2$ in $0 \leqslant 2 |x|^2 \leqslant 1$, the above inequality implies

$$
\alpha^ {2} c _ {2} \left(\rho_ {v} (\alpha) + c _ {1} \alpha \sqrt {\varepsilon}\right) \geqslant \left| x _ {\varepsilon} - y _ {\varepsilon} \right| ^ {2}
$$

when $c_{2}(\rho_{v}(\alpha) + c_{1}\alpha \sqrt{\varepsilon})\leqslant \frac{1}{2}$ and we are done.

For the final case (iii) we use the special case of the following lemma in which w is Lipschitz continuous:

LEMMA II.3. Let $w$ be continuous on $\mathbb{R}^N$, $\Phi \in C^1(\mathbb{R}^N)$ and $x_0 \in E^+(w\Phi)$. Set

$$
\rho_ {w} (\lambda) = \max \left\{\left| w (x _ {0}) - w (x) \right|: \left| x _ {0} - x \right| \leqslant \lambda \right\},
$$

and

$$
\rho_ {D \Phi} (\lambda) = \max \left\{\left| D \Phi \left(x _ {0}\right) - D \Phi (x) \right|: \left| x _ {0} - x \right| \leqslant \lambda \right\}.
$$

Then for $\lambda > 0$ with $w(x_0) > \rho_w(\lambda)$

$$
w \left(x _ {0}\right) \frac {\left| D \Phi \left(x _ {0}\right) \right|}{\Phi \left(x _ {0}\right)} \leqslant \frac {\rho_ {w} (\lambda)}{\lambda} \frac {w \left(x _ {0}\right)}{w \left(x _ {0}\right) - \rho_ {w} (\lambda)} + \frac {w \left(x _ {0}\right)}{\Phi (x)} \rho_ {D \Phi} (\lambda).
$$

In particular, if $Dw \in L^{\infty}(B(x_0, R))$ for some $R > 0$, then

$$
w \left(x _ {0}\right) \frac {\left| D \Phi \left(x _ {0}\right) \right|}{\Phi \left(x _ {0}\right)} \leqslant \| D w \| _ {L ^ {\infty} \left(B \left(x _ {0}, R\right)\right)}.
$$

We first complete the proof of the theorem and then prove the lemma. Recall (2.26), (2.27) and that

$$
\lambda_ {\varepsilon} + \delta_ {\varepsilon} = - (u (x _ {\varepsilon}) - \psi_ {1} (x _ {\varepsilon})) \frac {D \Phi (x _ {\varepsilon})}{\Phi (x _ {\varepsilon})} + D \psi_ {1} (x _ {\varepsilon})
$$

where $\Phi(x) = e^{-\varepsilon|x|^2}\varphi((x - y_\varepsilon)/\alpha)$, $\psi_1 = e^{\varepsilon(|x|^2 - |y_\varepsilon|^2)}$, $\sqrt{\varepsilon} (|x_\varepsilon| + |y_\varepsilon|) \leqslant c$ and $x_\varepsilon \in E_+(u - \psi_1)\Phi)$. It follows from Lemma II.3 that the first term on the right above is bounded by

$$
\left\| D u \right\| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)} + \left\| 2 x e ^ {\varepsilon \left(| x | ^ {2} - | y _ {\varepsilon} | ^ {2}\right)} \right\| _ {L ^ {\infty} \left(B \left(x, 1 _ {\varepsilon}\right)\right)}
$$

which is bounded independent of $\varepsilon, \alpha$. The term $D\psi_{1}(x_{\varepsilon}) \to 0$ as $\varepsilon \downarrow 0$ uniformly in $\alpha$. Thus (2.19) implies $\lim_{\alpha \downarrow 0} A_{\varepsilon} = 0$ uniformly in $\varepsilon$, and the proof is complete.

PROOF OF LEMMA II.3. Let $\lambda > 0$, $\rho_w(\lambda) < w(x_0)$ and set $\hat{x} = |D\Phi(x_0)|^{-1}D\Phi(x_0)$. Set

$$
\begin{array}{c} \lambda \partial^ {2} \Phi (\lambda) = \Phi (x _ {0} + \lambda \hat {x}) - (\Phi (x _ {0}) + \lambda D \Phi (x _ {0}) \hat {x}) \\ = \Phi (x _ {0} + \lambda \hat {x}) - (\Phi (x _ {0}) + \lambda | D \Phi (x _ {0}) |). \end{array}
$$

Then

$$
w \left(x _ {0} + \lambda \hat {x}\right) \Phi \left(x _ {0} + \lambda \hat {x}\right) \leqslant w \left(x _ {0}\right) \Phi \left(x _ {0}\right)
$$

implies

$$
w \left(x _ {0} + \lambda \hat {x}\right) \left(\Phi \left(x _ {0}\right) + \lambda \mid D \Phi \left(x _ {0}\right) \mid + \lambda \partial^ {2} \Phi (\lambda)\right) \leqslant w \left(x _ {0}\right) \Phi \left(x _ {0}\right)
$$

or

$$
w \left(x _ {0}\right) \frac {\left| D \Phi \left(x _ {0}\right) \right|}{\Phi \left(x _ {0}\right)} \leqslant \frac {w \left(x _ {0}\right)}{w \left(x _ {0} + \lambda \hat {x}\right)} \frac {\left(w \left(x _ {0}\right) - w \left(x _ {0} + \lambda \hat {x}\right)\right)}{\lambda} - \frac {w \left(x _ {0}\right)}{\Phi \left(x _ {0}\right)} \partial^ {2} \Phi (\lambda),
$$

where the manipulations are justified by $w(x_0 + \lambda \hat{x}) \geqslant w(x_0) - \rho_w(\lambda) > 0$. The result now follows from $|w(x_0) - w(x_0 + \lambda \hat{x})| \leqslant \rho_w(\lambda)$, $w(x_0 + \lambda \hat{x}) \geqslant w(x_0) - \rho_w(\lambda)$, $|\partial^2\Phi(\lambda)| \leqslant \rho_{D\Phi}(\lambda)$. The final assertion follows from the relations $\rho_w(\lambda) / \lambda \leqslant \| Dw\|_{L^\infty(B(x_0,R))}$ for $\lambda \leqslant R$, $\rho_{D\Phi}(0+) = 0$, and letting $\lambda \downarrow 0$ in the inequality.

III. Uniqueness for the Dirichlet problem in $\Omega$. In this section we turn to the uniqueness question for

$$
\left\{ \begin{array}{l l} H (x, u, D u) = 0 & \text { in } \Omega , \\ u (x) = z (x) & \text { on } \partial \Omega , \end{array} \right.\tag{3.1}
$$

in the case where $\Omega$ is an open subset of $\mathbf{R}^N$ and $\partial\Omega \neq \emptyset$. In this section the restrictions (2.19)-(2.21\*) on $H$ are to be understood by replacing $\mathbf{R}^N$ by $\Omega$. The main result is

THEOREM III.1. Let $u, v \in C_b(\overline{\Omega})$ and (2.19) and (2.20) hold. Let $u, v$ be viscosity solutions of $H(x, u, Du) = 0$ and $H(x, v, Dv) = m$ in $\Omega$ where $m \in C_b(\overline{\Omega})$. Let $R_0 = \max(\|u\|_{L^\infty(\Omega)}, \|v\|_{L^\infty(\Omega)})$ and $\gamma = \gamma_{R_0}$ from (2.20). Then:

(i) If (2.21\*) holds and $u|_{\partial \Omega}$ or $v|_{\partial \Omega}$ is uniformly continuous and

$$
\lim_{\substack{x\in \Omega \\ x\to x_{0}}}\big(|u(x) - u(x_{0})| + |v(x) - v(x_{0})|\big) = 0
$$

uniformly for $x_0 \in \partial \Omega$, then

(3.2) $\| \gamma ((u - v)^{+})\|_{L^{\infty}(\Omega)}\leqslant \max \bigl (\| m^{-}\|_{L^{\infty}(\Omega)},\| \gamma ((u - v)^{+})\|_{L^{\infty}(\partial \Omega)}\bigr).$

(ii) If (2.19), (2.20) and (2.21) hold and $u, v \in \mathrm{BUC}(\overline{\Omega})$, then (3.2) holds.

(iii) If (2.19) and (2.20) hold and $u, v \in W^{1,\infty}(\Omega)$, then (3.2) holds.

REMARK 3.3. Remarks analogous to (2.6) and (2.18) are valid here.

PROOF OF THEOREM III.1. We give the proof only in the case when  $\Omega$  is bounded. The general case follows from a combination of the arguments given below and in the proof of Theorem II.2.

Without loss of generality we may assume  $\|(u-v)^{+}\|_{L^{\infty}(\Omega)}>\|(u-v)^{+}\|_{L^{\infty}(\partial\Omega)}$ . Then (3.2) reduces to

$$
\left\| \gamma \left(\left(u - v\right) ^ {+}\right) \right\| _ {L ^ {\infty} (\Omega)} <   \left\| m ^ {+} \right\| _ {L ^ {\infty} (\Omega)}.
$$

Let $\varphi_{\alpha}(x) = \varphi (x / \alpha)$ as in the end of the proof of Theorem II.2 and

$$
M _ {\alpha} = \sup _ {x, y \in \overline {{{\Omega}}}} \varphi_ {\alpha} (x - y) (u (x) - v (y)).
$$

Now $u, v \in C_b(\overline{\Omega}) = \mathrm{BUC}(\overline{\Omega})$ since $\overline{\Omega}$ is compact. With $M_0 = \| (u - v)^+ \|_{L^\infty (\Omega)}$ we therefore clearly have

$$
M _ {0} \leqslant M _ {\alpha} \leqslant \varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha}) (M _ {0} + \rho_ {v} (\alpha))\tag{3.4}
$$

where $\rho_v$ is the modulus of continuity of $v$ and

$$
x _ {\alpha}, y _ {\alpha} \in \overline {{{\Omega}}}, \quad \varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha}) (u (x _ {\alpha}) - v (y _ {\alpha})) = M _ {\alpha}.
$$

From (3.4) and the choice of $\varphi_{\alpha}$ we deduce $|x_{\alpha} - y_{\alpha}| \leqslant \alpha \delta(\alpha)$ where $\delta(0+) = 0$ as in the proof of Theorem II.2(ii). Finally, as $\alpha \downarrow 0$ all limit points of $x_{\alpha}, y_{\alpha}$ lie in $E_{+}((u - v)) \subset \Omega$. Therefore, there is a compact $K \subset \Omega$ such that $x_{\alpha}, y_{\alpha} \in K$ for $\alpha$ small. It follows that $\varphi_{\alpha}(\cdot - y_{\alpha}), \varphi_{\alpha}(x_{\alpha} - \cdot) \in \mathfrak{D}(\Omega)^{+}$ for small $\alpha$. From the assumptions we conclude

$$
H \left(x _ {\alpha}, u (x _ {\alpha}), - (u (x _ {\alpha}) - v (y _ {\alpha})) \frac {(D \varphi_ {\alpha}) (x _ {\alpha} - y _ {\alpha})}{\varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha})}\right) \leqslant 0,
$$

$$
H \left(y _ {\alpha}, v (y _ {\alpha}), - (u (x _ {\alpha}) - v (y _ {\alpha})) \frac {(D \varphi_ {\alpha}) (x _ {\alpha} - y _ {\alpha})}{\varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha})}\right) \geqslant m (y _ {\alpha})
$$

which implies (recall the proof of Theorem II.2)

$$
\gamma \big(M_{\alpha}\big)\leqslant \| m^{-}\|_{L^{\infty}(\Omega)} + \sup_{\substack{|x - y|\leqslant \alpha \delta (\alpha)\\ |r|\leqslant R_{0}\\ |p|\leqslant c / \alpha}}|H(x,r,p) - H(y,r,p)|
$$

for some $c$. Moreover, if $Du, Dv \in L^{\infty}(\Omega)$ we may replace $|p| \leqslant c / \alpha$ by $|p| \leqslant c$. The argument concludes in the usual way.

REMARK 3.5. The condition (2.20) can be weakened to $H(x, r, p) - H(x, s, p) \geqslant \gamma_{R,\delta}(r - s)$ for $-R \leqslant s \leqslant r \leqslant R$, $p \in \mathbf{R}^N$ and $x \in \Omega_\delta = \{x: \text{distance}(x, \partial\Omega) > \delta\}$ with the conclusion being $u \leqslant v$ if $m \geqslant 0$ and $u \leqslant v$ on $\partial\Omega$.

All the above results require that $H(x, r, p)$ be strictly increasing in $r$. Moreover uniqueness fails without some monotonicity in this sense. An extreme example is $H \equiv 0$. We treat one case without strict monotonicity in $r$ via an adaptation of a device of S. N. Kružkov [18].

For simplicity consider the example

$$
H (D u) = n (x) \quad \text { in } \Omega ,\tag{3.6}
$$

where we assume

$$
\left\{ \begin{array}{l l} H (0) = 0, & H \text {   is   convex,   continuous   and   } H \geqslant 0, \\ n \in C (\overline {{\Omega}}), & n > 0 \text {   in   } \overline {{\Omega}}, \Omega \text {   is   bounded }. \end{array} \right.\tag{3.7}
$$

PROPOSITION III.2. Let (3.7) hold and $u, v \in C(\overline{\Omega})$ be viscosity sub- and supersolutions, respectively, of (3.6). Then

$$
\left\| (u - v) ^ {+} \right\| _ {L ^ {\infty} (\partial \Omega)} \leqslant \left\| (u - v) ^ {+} \right\| _ {L ^ {\infty} (\partial \Omega)}.
$$

PROOF. Let $\Psi \in C^{\infty}(\mathbf{R})$ satisfy $\Psi' > 0$, $\Psi'' > 0$ everywhere and $\Psi(\mathbf{R}) = \mathbf{R}$. Let $\Phi = \Psi^{-1}$. By Corollary I.8, $\tilde{u} = \Phi(u)$, $\tilde{v} = \Phi(v)$ are viscosity sub- and supersolutions, respectively, of

$$
\frac {1}{\Psi^ {\prime} (w)} H \left(\Psi^ {\prime} (w) D w\right) = \frac {1}{\Psi^ {\prime} (w)} n (x) \quad \text { in } \Omega .\tag{3.8}
$$

The Hamiltonian

$$
\tilde {H} (x, r, p) = \frac {1}{\Psi^ {\prime} (r)} H (\Psi^ {\prime} (r) p) - \frac {1}{\Psi^ {\prime} (r)} n (x)
$$

is locally Lipschitz in $r$ and a computation yields

$$
\frac {\partial}{\partial r} \tilde {H} = \frac {\Psi^ {\prime \prime} (r)}{(\Psi^ {\prime} (r)) ^ {2}} [ (D H) (\Psi^ {\prime} (r) p) \Psi^ {\prime} (r) p - H (\Psi^ {\prime} (r) p) ] + \frac {\Psi^ {\prime \prime} (r)}{(\Psi^ {\prime} (r)) ^ {2}} n (x).
$$

Since $H$ is convex, $DH(q) \cdot q - H(q) \geqslant -H(0) = 0$ and we deduce

$$
\frac {\partial \tilde {H}}{\partial r} \geqslant \frac {\Psi^ {\prime \prime} (r)}{(\Psi^ {\prime} (r)) ^ {2}} n (x).
$$

Therefore $\tilde{H}$ satisfies the conditions of Theorem III.1(i) and we obtain

$$
\left\| \left(\Phi (u) - \Phi (v)\right) ^ {+} \right\| _ {L ^ {\infty} (\Omega)} \leqslant \left\| \left(\Phi (u) - \Phi (v)\right) ^ {+} \right\| _ {L ^ {\infty} (\partial \Omega)}.
$$

Since $\Psi$ can be replaced by $\Psi_{\theta}(r) = \theta \Psi(r) + (1 - \mathcal{O})r$ for any $\theta \in ]0, 1]$, we deduce

$$
\left\| \left(\Phi_ {\theta} (u) - \Phi_ {\theta} (v)\right) ^ {+} \right\| _ {L ^ {\infty} (\Omega)} \leqslant \left\| \left(\Phi_ {\theta} (u) - \Phi_ {\theta} (v)\right) ^ {+} \right\| _ {L ^ {\infty} (\partial \Omega)}
$$

where $\Phi_{\theta} = (\Psi_{\theta})^{-1}$. To conclude, we observe that $\Phi_{\theta}(r) \to r$ locally uniformly as $\theta \to 0^{+}$.

REMARK 3.9. It is worth noting that uniqueness of (viscosity) solutions of (3.6) may fail if we assume only:

$$
\left\{ \begin{array}{l l} H (0) = 0, & H \text {   is   convex,   continuous   and   } H \geqslant 0, \\ n \in C (\overline {{\Omega}}), & n \geqslant 0 \text {   in   } \overline {{\Omega}}, \Omega \text {   is   bounded. } \end{array} \right.\tag{3.10}
$$

Actually it is enough for $n$ to vanish at one point to have nonuniqueness, as is shown in the following example: Let $\Omega = [-1, +1]$, $H(p) = |p|^2$, $n(x) = x^4$. Clearly $\bar{u}(x) = \frac{1}{3} - \frac{1}{3} |x|^3$ is a $C^1$ solution of

$$
\mid \bar {u} ^ {\prime} \mid^ {2} = \mid x \mid^ {4} \quad \text { in } \Omega , \qquad \bar {u} = 0 \quad \text { on } \partial \Omega .
$$

On the other hand, if we let $u(x) = \frac{1}{3} - \frac{1}{3} |x|^3$ for $|x| \geqslant t_0$ and $u(x) = \frac{1}{3} |x|^3$ for $|x| \leqslant t_0$, where $t_0 = 2^{-1/3}$, $u$ is a solution of the same equation which is also $C^1$ except at $\pm t_0$ where the discontinuity of $u'$ is such that $u$ is still a viscosity solution. Therefore in this example we have two different viscosity solutions.

As remarked in the introduction, all the above uniqueness results are new. No uniqueness criteria (even for generalized solutions in  $W^{1,\infty}(\Omega)$ ) are known except in the case of a convex Hamiltonian. In the convex case, A. Douglas [10] and S. N. Kružkov [18] have introduced the class of semiconcave functions, that is functions u such that  $\partial^{2}u/\partial\chi^{2}\leqslant C_{\delta}$  in  $\mathcal{D}'(\Omega_{\delta})$  for all  $\delta>0$  and for all  $\chi:|\chi|=1$  with  $\dot{\Omega}_{\delta}$  defined in (3.5) and  $\chi$  denoting an arbitrary direction. Uniqueness in this class is proved by the above authors. P. L. Lions [22] (see also [23]) extends these results to the class of functions satisfying

$$
\Delta u \leqslant C _ {\delta} \quad \text { in } \mathcal {D} ^ {\prime} (\Omega_ {\delta}) \text { for   all } \delta > 0.
$$

All these results require convex Hamiltonians and some degree of regularity of the solutions.

To conclude this section, we observe that in the convex case any Lipschitz subsolution is a viscosity subsolution and any Lipschitz, semiconcave supersolution is a viscosity supersolution. (This implies, by the way, that the uniqueness results of Douglas and Kružkov are completely contained in ours.)

PROPOSITION III.3. Let $H(x, r, p)$ be a continuous Hamiltonian, convex in $p$.

(i) Let $u \in W_{\mathrm{loc}}^{1,\infty}(\Omega)$ satisfy: $H(x, u, Du) \leqslant 0$ in $\Omega$. Then $u$ is a viscosity subsolution of $H(x, v, Dv) = 0$.

(ii) Let $u$ be a locally bounded semiconcave function satisfying

$$
H (x, u, D u) \geqslant 0 \quad i n \Omega .
$$

Then $u$ is a viscosity supersolution of $H(x, v, Dv) = 0$.

PROOF OF PROPOSITION III.3. (i) We first remark that if u is a locally Lipschitz subsolution of

$$
H (x, u, D u) \leqslant 0 \quad \text { in } \Omega ,
$$

then an easy argument shows that we have

$$
H (x, u ^ {\varepsilon}, D u ^ {\varepsilon}) \leqslant f _ {\varepsilon} (x) \quad \text { in } \Omega_ {\varepsilon}
$$

where $f_{\varepsilon} \to 0$ uniformly on compact sets of $\Omega$ and $u_{\varepsilon} = u * p_{\varepsilon}$ with $p_{\varepsilon} = p(\cdot / \varepsilon) / \varepsilon^{N}$, $p \in \mathfrak{D}_{+}(\mathbf{R}^{N})$, $\operatorname{supp} p \subset B_{1}, \| p \|_{L^{1}} = 1$. (Observe that $H(Du_{\varepsilon}) \leqslant H(Du) * p_{\varepsilon}$ if $H$ is convex.)

Now since $u^{\varepsilon}$ is $C^\infty$, $u^{\varepsilon}$ is obviously a viscosity subsolution of the equation: $H(x, v, Dv) = f_{\varepsilon}(x)$ in $\Omega_{\varepsilon_0}$ (for any $0 < \varepsilon \leqslant \varepsilon_0$). Thus we conclude by a simple application of Theorem I.2.

(ii) Let $u$ be a locally bounded semiconcave function satisfying: $H(x, u, Du) \geqslant 0$ on $\Omega$. Without loss of generality (restricting, if necessary, our attention to each $\Omega_{\delta}$, and making a translation) we may assume: $u \in W^{1,\infty}(\Omega)$, $u$ is concave on $\Omega$ or more precisely: $\partial^2 u / \partial \chi^2 \leqslant 0$ in $\mathfrak{D}'(\Omega) \forall \chi: |\chi| = 1$. (This implies that $u$ is concave on every convex subset of $\overline{\Omega}$.)

Now let $\varphi, k$ be such that $E_{-}(\varphi(u - k)) \neq \emptyset$, $\varphi \in \mathfrak{D}_{+}(\Omega)$, $k \in \mathbf{R}$, and let $x_0 \in E_{-}(\varphi(u - k))$. Obviously, there exists $\rho > 0$ small enough such that on $B(x_0, \rho)$, we have

$$
\begin{array}{r l} u (x _ {0}) & \geqslant k + \frac {\varphi (x _ {0})}{\varphi (x)} (u (x _ {0}) - k) \\ & = u (x _ {0}) - \frac {D \varphi (x _ {0})}{\varphi (x _ {0})} (u (x _ {0}) - k) \cdot (x - x _ {0}) + | x - x _ {0} | \varepsilon (x) \end{array}
$$

where $\varepsilon(x) \to 0$ as $|x - x_0| \to 0$. Since $u$ is concave on $B(x_0, \rho)$, this inequality implies that $u$ is differentiable at $x_0$ and $Du(x_0) = -D\varphi(x_0)(u(x_0) - k)/\varphi(x_0)$. To conclude we just have to prove that $H(x_0, u(x_0), Du(x_0)) \geqslant 0$. But by assumption $\exists x_n \in \Omega$, $x_n \to_{n \to +\infty} x_0$, $u$ is differentiable at $x_n$ and

$$
H \left(x _ {n}, u \left(x _ {n}\right), D u \left(x _ {n}\right)\right) \geqslant 0.
$$

And since u is concave, we have  $Du(x_{n}) \to Du(x_{0})$  (all limit points of  $Du(x_{n})$  are superdifferentials of u at  $x_{0}$  and therefore reduce to  $Du(x_{0})$ ).

IV. Existence of viscosity solutions of the Dirichlet problem. In this section we establish that the most common method of obtaining generalized solutions of HJ equations actually provides viscosity solutions. This is done in §IV.1 and roughly means that we could take all known existence theorems and generalize (using Theorem IV.1 in the process) and restate them as results concerning viscosity solutions. Of course we will not do this—we refer the reader instead to [22] for a complete treatment of general results of this sort and references to the earlier literature. However, it seems worthwhile to illustrate the situation by giving very general new results for a simple model problem, which we do in §IV.2.

IV.1. The method of vanishing viscosity and viscosity solutions of HJ equations. The vanishing viscosity method for obtaining solutions of

$$
H (x, u, D u) = 0 \quad \text { in } \Omega , \qquad u = z \quad \text { on } \partial \Omega\tag{4.1}
$$

consists of approximating the problem by ones of the form

$$
\begin{array}{l l} \text {(a)} & - \varepsilon \Delta u _ {\varepsilon} + H _ {\varepsilon} (x, u _ {\varepsilon}, D u _ {\varepsilon}) = 0 \quad \text { in } \Omega , \\ \text {(b)} & u _ {\varepsilon} = z _ {\varepsilon} \quad \text { on } \partial \Omega \end{array}\tag{4.1) \( _{\varepsilon} \}
$$

where $\varepsilon > 0$, $H_{\varepsilon}$, $z_{\varepsilon}$ are adequately smooth and converge locally uniformly to $H$, $z$ respectively. One attempts to prove $(4.1)_{\varepsilon}$ is solvable for $\varepsilon > 0$, and to obtain precompactness of the family $\{u_{\varepsilon}: 0 < \varepsilon \leqslant 1\}$ in $C(\Omega)$ (or $C(\overline{\Omega})$). Typically this is done by obtaining (perhaps local) estimates on $u_{\varepsilon}$ and $Du_{\varepsilon}$ in $L^{\infty}$. See [18] and §IV.2 below in this regard. We prove

PROPOSITION IV.1. Let $u_{\varepsilon} \in C^{2}(\Omega)$ be a solution of (4.1)$_{\varepsilon}$(a) where $H_{\varepsilon} \to H$ as $\varepsilon \downarrow 0$ in $C(\Omega \times \mathbf{R} \times \mathbf{R}^{n})$. Assume $\varepsilon_{n} \downarrow 0$ and $u_{\varepsilon_{n}} \to u$ in $C(\Omega)$ and $n \to \infty$. Then $u$ is a viscosity solution of $H(x, u, Du) = 0$. If also $u_{\varepsilon} = z_{\varepsilon}$ on $\partial \Omega$, $z_{\varepsilon} \to z$ in $C(\partial \Omega)$ and $u_{\varepsilon_{n}} \to u$ in $C(\overline{\Omega})$ then $u|_{\partial \Omega} = z$.

PROOF. Let $u_{\varepsilon_n} \to u$ in $C(\Omega)$ as in the assumptions. Fix $\varphi \in \mathfrak{D}(\Omega)^+$, $k \in \mathbf{R}^N$ and assume $E_+(\varphi(u-k)) \neq \emptyset$. Then for large $n$ there exists $x_n \in E_+(\varphi(u_{\varepsilon_n}-k))$ and, passing to a subsequence if necessary, we may assume $x_n \to x \in E_+(\varphi(u-k))$. By a simple computation we have, on supp $\varphi$,

$$
\begin{array}{l} 0 = \frac {1}{\varphi} \left(\varphi \left(- \varepsilon \Delta u _ {\varepsilon} + H (x, u _ {\varepsilon}, D u _ {\varepsilon})\right)\right) \\ = - \varepsilon \frac {1}{\varphi} \Delta \left(\varphi \left(u _ {\varepsilon} - k\right)\right) + \varepsilon \left(u _ {\varepsilon} - k\right) \frac {\Delta \varphi}{\varphi} + 2 \varepsilon \frac {D \varphi \cdot D \left(\varphi \left(u _ {\varepsilon} - k\right)\right)}{\phi^ {2}} \\ - 2 \varepsilon \frac {(u _ {\varepsilon} - k)}{\varphi^ {2}} | D \varphi | ^ {2} + H \left(x, u _ {\varepsilon}, \frac {1}{\varphi} D (\varphi (u _ {\varepsilon} - k)) - \frac {u _ {\varepsilon} - k}{\varphi} D \varphi\right). \end{array}
$$

Evaluating this identity at $\varepsilon = \varepsilon_{n}$, $x = x_{n}$ and using $(\Delta (\varphi (u_{\varepsilon} - k))) (x_{n}) \leqslant 0$, $(D\varphi (u_{\varepsilon} - k))(x_{n}) = 0$ (because $x_{n} \in E_{+}(\varphi (u_{\varepsilon_{n}} - k)))$ we conclude

$$
\begin{array}{l} \varepsilon_ {n} \big (u _ {\varepsilon_ {n}} (x _ {n}) - k \big) \frac {\Delta \varphi (x _ {n})}{\varphi (x _ {n})} - 2 \varepsilon_ {n} \big (u _ {\varepsilon_ {n}} (x _ {n}) - k \big) \frac {| D \varphi (x _ {n}) | ^ {2}}{\varphi (x _ {n}) ^ {2}} \\ + H \Bigg (x _ {n}, u _ {\varepsilon_ {n}} (x _ {n}), - \big (u _ {\varepsilon_ {n}} (x _ {n}) - k \big) \frac {D \varphi (x _ {n})}{\varphi (x _ {n})} \Bigg) \leqslant 0. \end{array}
$$

Since $x_{n}\to x\in E_{+}(\varphi (u - k))$ we find, letting $n\to \infty$

$$
H (x, u (x), - (u (x) - k) D \varphi (x) / \varphi (x)) \leqslant 0.
$$

Thus u is a viscosity subsolution. Similarly, it is a viscosity supersolution and the result follows.

REMARK 4.2. We could replace $u_{\varepsilon} \in C^{2}(\Omega)$ above by $u_{\varepsilon} \in W_{\mathrm{loc}}^{2,p}(\Omega), p > N$, via Bony's maximum principle [5].

REMARK 4.3. If we obtain a viscosity solution of (4.1) in this way and one of our uniqueness results applies, it follows that  $u_{\varepsilon}$  converges to this unique solution as  $\varepsilon\downarrow0$ . This is known in some particular cases via arguments using considerations of control theory or differential games (W. H. Fleming [14, 15], A. Friedman [16]).

REMARK 4.4. This result also shows that the optimal cost function  $\bar{u}$  of the control problem associated with (4.1) (or the value function in the case of differential games — see S. H. Benton [4], W. H. Fleming [13, 14, 15]) is indeed a (or the) viscosity solution. Indeed, in these contexts it is easy to show  $u_{\varepsilon}$  converges to  $\bar{u}$, and the theorem applies.

IV.2. A model equation. We will assume

$$
\left\{ \begin{array}{l l} (\mathrm{i}) & H \in C (\mathbf {R} ^ {N}), \\ (\mathrm{ii}) & \beta \colon \mathbf {R} \to \mathbf {R} \text {   is   an   increasing   homeomorphism   of   } \mathbf {R} \text {   onto   } \mathbf {R}, \\ (\mathrm{iii}) & n \in \mathrm{BUC} (\mathbf {R} ^ {N}) \end{array} \right.\tag{4.5}
$$

and consider the model problem

$$
\beta (u) + H (D u) = n \quad \text { in } \mathbf {R} ^ {N}.\tag{4.6}
$$

It simplifies the discussion to follow to assume

$$
H (0) = 0, \quad \beta (0) = 0,\tag{4.7}
$$

which amounts to changing n by a constant. We will consider solutions of approximate problems of the form

$$
- \varepsilon \Delta u _ {\varepsilon} + \beta_ {\varepsilon} (u _ {\varepsilon}) + \varepsilon u _ {\varepsilon} + H _ {\varepsilon} (D u _ {\varepsilon}) = n _ {\varepsilon}\tag{4.8}
$$

under assumptions given later. Before doing so we obtain the key estimates we need. This also motivates Proposition IV.3 concerning (4.6).

LEMMA IV.2. Let $F \in C(\mathbb{R}^N)$, $F(0) = 0$, and $\gamma$ be an increasing homeomorphism of $\mathbb{R}$, $\gamma(0) = 0$. Assume $v, \hat{v} \in C^2(\mathbb{R}^N) \cap L^\infty(\mathbb{R}^N)$, $F(Dv)$, $F(D\hat{v}) \in L^\infty(\mathbb{R}^N)$ and

$$
\begin{array}{l l} \text {(a)} & - \varepsilon \Delta v + \gamma (v) + F (D v) = m \in C _ {b} (\mathbf {R} ^ {N}), \\ \text {(b)} & - \varepsilon \Delta \hat {v} + \gamma (\hat {v}) + F (D \hat {v}) = \hat {m} \in C _ {b} (\mathbf {R} ^ {N}). \end{array}\tag{4.9}
$$

Then for $\nu \in \{+, -\}$

$$
\left\| \gamma (v) ^ {\nu} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant \left\| m ^ {\nu} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})}, \quad \left\| \gamma (\hat {v}) ^ {\nu} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant \left\| \hat {m} ^ {\nu} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})}\tag{4.10}
$$

and

$$
\begin{array}{l} \text {4.11)} \| (v - \hat {v}) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \\ \leqslant \sup \left\{| \gamma^ {- 1} (s + \| (m - \hat {m}) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}) - \gamma^ {- 1} (s) |: | s | \leqslant \| \hat {m} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \right\}. \end{array}
$$

SKETCH OF PROOF. If $x \in E_{+}(v)$ then $\Delta v(x) \leqslant 0$ and $F(Dv(x)) = F(0) = 0$. Hence, from (4.9), $\gamma(v(x)) \leqslant m(x)$, and we would have (4.10) with $\nu = +$. If $E_{+}(v) = \emptyset$ but $v > 0$ somewhere, one chooses $x_{\lambda} \in E_{+}(e^{-\lambda |x|^{2}}v)$, makes the associated computation and uses $\lambda |x_{\lambda}|^{2} \leqslant C$ to let $\lambda \downarrow 0$ and reach the same conclusion.

For this we need to observe that $Dv \in L^{\infty}(\mathbb{R}^{N})$ because $v \in L^{\infty}(\mathbb{R}^{N})$ and $-\varepsilon \Delta v = m - F(Dv) - \gamma(v) \in L^{\infty}(\mathbb{R}^{N})$ by assumption. To understand (4.11), let $x \in E_{+}(v - \hat{v})$. Forming the difference of (4.9)(a) and (b) and using $\Delta(v - \hat{v})(x) \leqslant 0$, $F(Dv) = F(D\hat{v})$ at $x$, one finds $\gamma(v(x)) - \gamma(\hat{v}(x)) \leqslant m(x) - \hat{m}(x)$. Writing $v(x) = \hat{v}(x) + \| (v - \hat{v})^{+} \|_{L^{\infty}(\mathbb{R}^{N})}$ we have

$$
\gamma (\mu + r) - \gamma (\mu) \leqslant \| (m - \hat {m}) ^ {+} \| _ {L ^ {\infty} \left(\mathbb {R} ^ {N}\right)}, \quad \mu = \hat {v} (x), \quad r = \| (v - \hat {v}) ^ {+} \| _ {L ^ {\infty} \left(\mathbb {R} ^ {N}\right)}.
$$

But then

$$
r \leqslant \gamma^ {- 1} (\gamma (\mu) + \| (m - \hat {m}) \| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)}) - \gamma^ {- 1} (\gamma (\mu))
$$

and we have (4.11). If $E_{+}(v - \hat{v}) = \emptyset$ but $v - \hat{v} > 0$ somewhere, approximate by $x_{\lambda} \in E_{+}(e^{-\lambda |\cdot|^{2}}(v - \hat{v}))$ and let $\lambda \downarrow 0$. This completes the discussion of Lemma IV.2. The main result concerning (4.6) is

PROPOSITION IV.3. Let (4.5) and (4.7) hold. Then (4.6) has a unique viscosity solution $u \in C_b(\mathbb{R}^N)$. Moreover,

$$
\| \beta (u) ^ {\nu} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant \| n ^ {\nu} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}, \quad \nu \in \{+, - \}.\tag{4.12}
$$

(4.13) If $m \in \mathrm{BUC}(\mathbb{R}^N)$ and $v$ is the viscosity solution of $\beta(v) + H(Dv) = m$, then

$$
\begin{array}{l} \| (u - v) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \\ \leqslant \sup \left\{\mid \beta^ {- 1} (s + \| (n - m) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}) - \beta^ {- 1} (s) \mid : | s | \leqslant \| m \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \right\}. \end{array}
$$

(4.14) If $\rho_{u}, \rho_{n}$ are the moduli of continuity of $u, n$, respectively, then

$$
\rho_ {u} (r) \leqslant \sup \left\{\beta^ {- 1} \left(s + \rho_ {n} (r)\right) - \beta^ {- 1} (s): | s | \leqslant \| m \| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)} \right\}.
$$

SKETCH OF PROOF OF PROPOSITION IV.3. The uniqueness of viscosity solutions of (4.6) follows from Theorem II.2. The Hamiltonian $\overline{H}(x, r, p) = \beta(r) + H(p) - n(x)$ clearly satisfies (2.19). For (2.20) we note that

$$
\overline {{{H}}} (x, r, p) - \overline {{{H}}} (x, s, p) = \beta (r) - \beta (s) \geqslant \gamma_ {R} (r - s), \quad - R \leqslant s \leqslant r \leqslant R,
$$

with $\gamma_R(\tau) = \inf \{\beta (s + \tau) - \beta (s)\colon |s|\leqslant R\}$ for $\tau \geqslant 0$. Finally, (2.21\*) reduces to the uniform continuity of $n$.

For the existence, let $\beta_{\varepsilon}, H_{\varepsilon}, n_{\varepsilon} \in C^{\infty}$ be approximations of $\beta, H, n$ such that

$$
\left\{\begin{array}{l}\beta_ {\varepsilon}, \beta_ {\varepsilon} ^ {\prime} \in L ^ {\infty} (R), \beta_ {\varepsilon} ^ {\prime} \geqslant 0, \beta_ {\varepsilon} (0) = 0, \beta_ {\varepsilon} \rightarrow \beta \text {   in   } C (\mathbf {R}) \text {   as   } \varepsilon \downarrow 0,\\n _ {\varepsilon} \in \mathrm{BUC} (\mathbf {R} ^ {N}) \text {   and   } n _ {\varepsilon} \rightarrow n \text {   uniformly   as   } \varepsilon \downarrow 0,\\H _ {\varepsilon} \in L ^ {\infty} (\mathbf {R} ^ {N}), H _ {\varepsilon} (0) = 0, \text {   and   } H _ {\varepsilon} \rightarrow H \text {   in   } C (\mathbf {R} ^ {N}) \text {   as   } \varepsilon \downarrow 0.\end{array}\right.\tag{4.15}
$$

It is then nearly trivial that

$$
- \varepsilon \Delta u _ {\varepsilon} + \beta_ {\varepsilon} (u _ {\varepsilon}) + \varepsilon u _ {\varepsilon} + H _ {\varepsilon} (D u _ {\varepsilon}) = n _ {\varepsilon}\tag{4.16}
$$

has a solution $u_{\epsilon} \in C^{2}(\mathbf{R}^{N}) \cap L^{\infty}(\mathbf{R}^{N})$. One can simply solve the associated truncated problem in $B(0, R)$ for $u_{\epsilon R}$ subject to $u_{\epsilon R} = 0$ on $|x| = R$. Then

$$
\left| \beta_ {\varepsilon} \left(u _ {\varepsilon R}\right) + \varepsilon u _ {\varepsilon R} \right| \leqslant \left\| n _ {\varepsilon} \right\| _ {L ^ {\infty} (B (0, R))}
$$

follows as in Lemma IV.2. Using $H_{\varepsilon} \in L^{\infty}$ and interior estimates we conclude $-\varepsilon \Delta u_{\varepsilon R}$ is bounded in $L^{\infty}(B(0, R))$ as $R \to \infty$ and by compactness there is a sequence $R_{n} \to \infty$ and $u_{\varepsilon} \in C_b^1(\mathbf{R}^N)$, $\Delta u_{\varepsilon} \in L^{\infty}(\mathbf{R}^{N})$, such that $u_{R_n} \to u_{\varepsilon}$ boundedly in $C_{\mathrm{loc}}^1(\mathbf{R}^N)$ while $\Delta u_{\varepsilon R_n} \to \Delta u_{\varepsilon}$ weakly in $L_{\mathrm{loc}}^2(\mathbf{R}^N)$. Then (4.15) implies $u_{\varepsilon} \in C^{\infty}(\mathbf{R}^{N})$. Using Lemma IV.2 we conclude

$$
\left\| \left(\beta_ {\varepsilon} (u _ {\varepsilon}) + \varepsilon u _ {\varepsilon}\right) ^ {\nu} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant \left\| n _ {\varepsilon} ^ {\nu} \right\| _ {L ^ {\infty} (\mathbf {R} ^ {N})}.\tag{4.17}
$$

Since $\beta_{\varepsilon} \to \beta$ locally uniformly and $\beta(\mathbf{R}) = R$, (4.5) implies $u_{\varepsilon}$ is bounded in $L^{\infty}(\mathbf{R}^{N})$. Moreover, $u_{\varepsilon}(\cdot + y)$ solves (4.16) with $n_{\varepsilon}$ replaced by $n_{\varepsilon}(\cdot + y)$. By Lemma IV.2 we therefore have

$$
\begin{array}{r l} & {\left| u _ {\varepsilon} (x + y) - u _ {\varepsilon} (x) \right|} \\ & {\quad \leqslant \sup \Big \{\big | (\beta_ {\varepsilon} + \varepsilon I) ^ {- 1} \big (s + \rho_ {n _ {\varepsilon}} (| y |) \big) - (\beta_ {\varepsilon} + \varepsilon I) ^ {- 1} (s) \big |: | s | \leqslant \| n _ {\varepsilon} \| _ {L ^ {\infty} (\mathbb {R} ^ {N})} \Big \}} \end{array}\tag{4.18}
$$

where $\rho_{n_{\varepsilon}}$ is the modulus of continuity of $n_{\varepsilon}$. It is easy to choose $n_{\varepsilon}$ so that $\rho_{n_{\varepsilon}} \leqslant \rho_{n}$, and we assume we have done so. Moreover, since $\beta_{\varepsilon} + \varepsilon I \to \beta$ locally uniformly, $(\beta_{\varepsilon} + \varepsilon I)^{-1} \to \beta^{-1}$ locally uniformly. It thus follows from (4.18) that $\{u_{\varepsilon}\}$ is equicontinuous. Then there is a sequence $\varepsilon_{n} \downarrow 0$ and $u \in \mathrm{BUC}(\mathbf{R}^{N})$ such that $u_{\varepsilon_{n}} \to u$ locally uniformly. In view of Proposition IV.1, the existence assertion is proved.

We have in fact shown (4.14) in the process of constructing u. It follows equally well from (4.13) by noting that if u is the solution u of  $\beta(u) + H(Du) = n$ , then  $v(\cdot) = u(\cdot + y)$  is the solution of  $\beta(v) + H(Dv) = m$ ,  $m(\cdot) = n(\cdot + y)$ . One similarly verifies (4.13) by the construction, however let us observe that it essentially follows from Theorem II.2. Indeed, if  $u + H(Du) - n = 0$  and  $v + H(Dv) - n = m - n$ , Theorem II.2 implies

$$
\left\{ \begin{array}{l} \gamma_ {R} \big ((u - v) ^ {+} \big) \leqslant \| (n - m) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}, \\ R = \max \big (\| u \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}, \| v \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \big), \\ \gamma_ {R} (\tau) = \inf \{\beta (s + \tau) - \beta (s): | s | \leqslant R \} \end{array} \right.
$$

which is equivalent to

$$
\begin{array}{c} (u - v) ^ {+} \leqslant \sup \Bigl \{\beta^ {- 1} \bigl (s + \| (n - m) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \bigr) - \beta^ {- 1} (s): \\ | s | \leqslant \max \bigl (\| m \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \| n \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \bigr) \Bigr \}. \end{array}
$$

The estimate (4.12) follows from the construction. This ends the sketch of the proof.

V. Uniqueness for the Cauchy problem. We consider the Cauchy problem for HJ equations. More precisely, we consider the problem

$$
\left\{ \begin{array}{l l} (a) & u _ {t} + H (x, t, u, D u) = 0 \quad \text {in} \Omega \times ] 0, T ], \\ (b) & u (x, t) = z (x, t) \quad \text {on} \partial \Omega \times ] 0, T ], \\ (c) & u (t, x) = u _ {0} (x) \quad \text {on} \Omega . \end{array} \right.\tag{5.1}
$$

V.1. Viscosity solutions of the Cauchy problem. The notations

$$
Q _ {T} = \Omega \times ] 0, T ], \quad Q _ {T} ^ {0} = \Omega \times ] 0, T [\tag{5.2}
$$

will be used below. The notions of viscosity solutions of (5.1)(a) in $Q_{T}$ or $Q_{T}^{0}$ is contained in §II (in particular, recall Remark 1.13). Let us restate them explicitly for the particular equation (5.1)(a).

DEFINITION 5.3. Let $H \in C(\Omega \times [0, T] \times \mathbf{R} \times \mathbf{R}^N)$. Then a viscosity subsolution (respectively, supersolution, solution) of $u_t + H(x, t, u, Du) = 0$ on $Q_T^0$ is a function $u \in C(Q_T^0)$ such that: $\forall \varphi \in \mathfrak{D}(Q_T^0)^+, k \in R$,

$$
\left\{ \begin{array}{l} E _ {+} (\varphi (u - k), Q _ {T} ^ {0}) \neq \varnothing \Rightarrow \exists (x _ {0}, t _ {0}) \in E _ {+} (\varphi (u - k), Q _ {T} ^ {0}) \\ \text {such that} - \frac {u (x _ {0} , t _ {0}) - k}{\varphi (x _ {0} , t _ {0})} \varphi_ {t} (x _ {0}, t _ {0}) \\ + H \left(x _ {0}, t _ {0}, u (x _ {0}, t _ {0}), - \frac {u (x _ {0} , t _ {0}) - k}{\varphi (x _ {0} , t _ {0})} D \varphi (x _ {0}, t _ {0})\right) \leqslant 0 \end{array} \right.\tag{5.4}
$$

(respectively,

$$
\left\{ \begin{array}{l} E _ {-} \big (\varphi (u - k), Q _ {T} ^ {0} \big) \neq \varnothing \Rightarrow \exists (x _ {0}, t _ {0}) \in E _ {-} \big (\varphi (u - k), Q _ {T} ^ {0} \big) \\ \text { such   that } - \frac {u (x _ {0} , t _ {0}) - k}{\varphi (x _ {0} , t _ {0})} \varphi_ {t} (x _ {0}, t _ {0}) \\ + H \Bigg (x _ {0}, t _ {0}, u (x _ {0}, t _ {0}), - \frac {u (x _ {0} , t _ {0}) - k}{\varphi (x _ {0} , t _ {0})} D \varphi (x _ {0}, t _ {0}) \Bigg) \geqslant 0; \end{array} \right.\tag{5.5}
$$

respectively (5.4) and (5.5)).

One defines viscosity subsolutions, etc., in $Q_{T}$ by replacing $Q_{T}^{0}$ by $Q_{T}$ everywhere above. A viscosity subsolution (etc.) of (5.1) is a $u \in C(\overline{Q}_{T})$ which is a viscosity solution of (5.1)(a) in $Q_{T}$ such that $u \leqslant z$ on $\partial \Omega \times [0, T]$, $u(x, 0) \leqslant u_{0}(x)$ in $\Omega$ (etc.).

Owing to the special form of the equation (5.1)(a) with respect to the domain $Q_{T}$ we have

PROPOSITION V.1. Let $u \in C(Q_T)$ be a viscosity subsolution (respectively, supersolution, solution) of (5.1)(a) in $Q_T^0$. Then $u$ is a viscosity subsolution (respectively, supersolution, solution) of (5.1)(a) in $Q_T$.

PROOF. It suffices to treat the subsolution case. Let $\varphi \in \mathfrak{D}(Q_T)^+$, $k \in R$, $u$ be a viscosity subsolution in $Q_T^0$ and $(x_0, t_0) \in E_+(\varphi(u-k), Q_T)$. If $0 < t_0 < T$ we choose $\chi \in \mathfrak{D}((0, T))$ such that $0 \leqslant \chi \leqslant 1$ and $\chi(t_0) = 1$. Then $\chi\varphi \in \mathfrak{D}(Q_T^0)^+$ and $(x_0, t_0) \in E_+(\chi\varphi(u-k), Q_T^0)$. By Theorem I.3 and $\chi'(t_0) = 0$, the inequality of (5.4) holds. If $t_0 = T$ we choose $\chi_\varepsilon \in C^\infty([0, T])$ so that $0 \leqslant \chi_\varepsilon \leqslant 1$, $\chi_\varepsilon \equiv 1$ on $[0, T - 2\varepsilon]$, $\chi_\varepsilon \equiv 0$ on $[T - \varepsilon, T]$ and $\chi'_\varepsilon \leqslant 0$. Again $\chi_\varepsilon\varphi \in \mathfrak{D}(Q_T^0)^+$. Moreover, $\varphi(u-k) > 0$ at $(x_0, T)$ implies $\chi_\varepsilon\varphi(u-k)$ has a positive value for $\varepsilon$ small. Let $(x_\varepsilon, t_\varepsilon) \in E_+(\chi_\varepsilon\varphi(u-k), Q_T^0)$. Passing to a subsequence if necessary, we assume

$(x_{\varepsilon}, t_{\varepsilon}) \to (\bar{x}, \bar{t}) \in E_{+}(\varphi(u - k), Q_T)$. Then, by Theorem I.3,

$$
\begin{array}{r l} - \frac {(u (x _ {\varepsilon} , t _ {\varepsilon}) - k)}{\varphi (x _ {\varepsilon} , t _ {\varepsilon})} \varphi_ {t} (x _ {\varepsilon}, t _ {\varepsilon}) - \frac {(u (x _ {\varepsilon} , t _ {\varepsilon}) - k)}{\chi (t _ {\varepsilon})} \chi_ {\varepsilon} ^ {\prime} (t _ {\varepsilon}) \\ & + H \left(x _ {\varepsilon}, t _ {\varepsilon}, u (x _ {\varepsilon}, t _ {\varepsilon}), - \frac {(u (x _ {\varepsilon} , t _ {\varepsilon}) - k)}{\varphi (x _ {\varepsilon} , t _ {\varepsilon})} D \varphi (x _ {\varepsilon}, t _ {\varepsilon})\right) \leqslant 0. \end{array}
$$

Now $-(u(x_{\varepsilon},t_{\varepsilon}) - k)\chi_{\varepsilon}^{\prime}(t_{\varepsilon})\geqslant 0$ so we deduce the inequality of (5.4) with $(\bar{x},\bar{t})$ in place of $(x_0,t_0)$ in the limit. This completes the proof.

REMARK 5.6. In the general context of §I, if $\mathcal{O} \subset \mathcal{O}_1 \cap \mathcal{O} \cup \partial \mathcal{O}$ we roughly have that if $u \in C(\mathcal{O}_1)$ is a viscosity subsolution of $F = 0$ in $\mathcal{O}$ and $F(y, r, p + \lambda \nu(y))$ is nondecreasing in $\lambda$ for $y \in \mathcal{O}_1 \setminus \mathcal{O}$ and $\nu(y)$ the exterior normal to $\mathcal{O}$ at $y$, then $u$ is a viscosity subsolution in $\mathcal{O}_1$. However, we will not make the assumptions precise.

We will freely use the assertions of §I concerning viscosity subsolutions, etc., in  $Q_{T}^{0}$  and  $Q_{T}$ . In this connection we again recall Remark 1.13 as well as the fact that if  $u \in C^{1}(Q_{T}^{0})$  and u and Du extend continuously to all of  $Q_{T}$ , then  $u \in C^{1}(Q_{T})$ , etc.

V.2. Uniqueness of solutions of the Cauchy problem. We first formulate the various assumptions we will use in what follows:

(5.7)

$$
\left\{ \begin{array}{l} H \in C (\overline {{\Omega}} \times [ 0, T ] \times \mathbf {R} \times \mathbf {R} ^ {N}) \text {   is   uniformly   continuous   in } \\ \overline {{\Omega}} \times [ 0, T ] \times [ - R, R ] \times B (0, R) \text {   for   each   } R > 0. \end{array} \right.\tag{5.8}
$$

$$
\left\{ \begin{array}{l} \text { For } R > 0 \text { there   is   a } \gamma_ {R} \in R \text { such   that } \\ H (x, t, r, p) - H (x, t, s, p) \geqslant \gamma_ {R} (r - s) \text { for } x \in \Omega , - R \leqslant s \leqslant r \leqslant R, \\ 0 \leqslant t \leqslant T \text { and } p \in \mathbf {R} ^ {n}. \end{array} \right.\tag{5.9}
$$

$$
\lim _ {\alpha \downarrow 0} \sup \left\{\left| H (x, t, s, p) - H (y, t, s, p) \right|: | x - y | (1 + | p |) \leqslant \alpha , \right.
$$

$$
0 \leqslant t \leqslant T, | s | \leqslant R \} = 0
$$

for any R > 0.

$$
\lim _ {\alpha \downarrow 0} \sup \{| H (x, t, s, p) - H (y, t, s, p) |: | x - y | \leqslant \alpha , \tag {5.9*}
$$

$$
\left| x - y \right| \left| p \right| \leqslant R, 0 \leqslant t \leqslant T, \left| s \right| \leqslant R \} = 0
$$

for any $R > 0$.

These conditions are obvious analogues of (2.19)-(2.21\*). See §V.4 concerning their necessity.

The main uniqueness result is

THEOREM V.2. Let (5.7) and (5.8) hold. Let $u \in C_b(\overline{Q}_T)$ be a viscosity subsolution of $u_t + H(x, t, u, Du) = 0$ in $Q_T$ and $v \in C_b(\overline{Q}_\overline{T})$ be a viscosity supersolution of $v_t + H(x, t, v, Dv) = g(x, t)$ in $Q_T$ where $g \in C_b(\overline{Q}_\overline{T})$. Let

$$
R _ {0} = \max \Big (\| u \| _ {L ^ {\infty} (Q _ {T})}, \| v \| _ {L ^ {\infty} (Q _ {T})} \Big)
$$

and $\gamma = \gamma_{R_0}$ as in (5.8). Set $\partial_0Q_T = \partial \Omega \times [0,T]\cup (\overline{\Omega}\times \{0\})$ . Then:

(i) If $(5.9^{*})$ holds and $u|_{\partial_0Q_T}$, $v|_{\partial_0Q_T} \in \mathrm{BUC}(\partial_0Q_T)$ and

$$
\lim_{\substack{(x,t)\in Q_{T}^{0}\\ (x,t)\to (x_{0},t_{0})}}|u(x,t) - u(x_{0},t_{0})| + |v(x,t) - v(x_{0},t_{0})| = 0
$$

uniformly for $(x_0, t_0) \in \partial_0 Q_T$, then

$$
\left\| e ^ {\gamma t} (u - v) ^ {+} \right\| _ {L ^ {\infty} \left(Q _ {T}\right)} \leqslant \left\| e ^ {\gamma t} (u - v) ^ {+} \right\| _ {L ^ {\infty} \left(\partial_ {0} Q _ {T}\right)} + \int_ {0} ^ {T} e ^ {\gamma s} \| g (\cdot , s) ^ {-} \| _ {L ^ {\infty} (\Omega)} d s.\tag{5.10}
$$

(ii) If (5.9) holds and $u, v \in \mathrm{BUC}(\overline{Q}_T)$, then (5.10) holds.

(iii) If $Du, Dv \in L^{\infty}(Q_T)$, then (5.10) holds.

REMARK 5.11. Remarks parallel to (2.6) and (2.18) are valid here.

Much of the proof of Theorem V.2 consists of straightforward adaptation of the arguments given in earlier sections and we will not repeat these. Instead we treat a simple model case to exhibit the only new features. To this end, assume  $\gamma \in R$ ,

$$
H (x, t, u, p) = \gamma u + \overline {{{H}}} (p)\tag{5.12}
$$

and

(5.13) $\Omega = \mathbf{R}^N$ and $u(x,t),v(x,t)\to 0$ as $|x|\rightarrow \infty$ uniformly for $0\leqslant t\leqslant T$

We will write $H$ in place of $\overline{H}$ above. Now choose $\varphi_{\alpha}(x) = \varphi(x / \alpha), \psi_{\alpha}(t) = \psi(t / \alpha)$ where $\varphi \in \mathfrak{D}(\mathbf{R}^N)^+$, $\varphi(0) = 1, \psi(0) = 1, 0 \leqslant \varphi, \psi \leqslant 1$, $\operatorname{supp} \varphi \subset B(0,1)$, $\operatorname{supp} \psi \subset [-1,1]$. (In the case of $(x,t)$ dependence of $H$ we would require $\varphi(x) = 1 - |x|^2$, $\psi(t) = 1 - t^2$ near $x = 0, t = 0$.) Set

$$
m _ {0} (t) = \max _ {x \in \mathbf {R} ^ {N}} \bigl (u (x, t) - v (x, t) \bigr).\tag{5.14}
$$

Finally, let $\eta \in \mathfrak{D}(]0, T[)^+$ and assume

$$
E _ {+} \left(\eta (m _ {0} - k): ] 0, T [\right) \neq \varnothing .\tag{5.15}
$$

Now define

$$
M_{\alpha} = \sup_{\substack{x,y\in \mathbf{R}^{N}\\ 0\leqslant t,s\leqslant T}}\eta \left(\frac{t + s}{2}\right)\psi_{\alpha}(t - s)\varphi_{\alpha}(x - y)(u(x,t) - v(y,s) - k).\tag{5.16}
$$

Clearly $M_{\alpha} \geqslant \eta(m_0 - k)$ on $[0, T]$ and

$$
M _ {\alpha} \rightarrow \max _ {[ 0, T ]} \eta (m _ {0} - k) \quad \text { as } \alpha \downarrow 0.\tag{5.17}
$$

Let $x_{\alpha}, y_{\alpha} \in \mathbf{R}^N, t_{\alpha}, s_{\alpha} \in [0, T]$ be such that

$$
M _ {\alpha} = \eta \left(\frac {t _ {\alpha} + s _ {\alpha}}{2}\right) \psi_ {\alpha} (t _ {\alpha} - s _ {\alpha}) \varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha}) (u (x _ {\alpha}, t _ {\alpha}) - v (y _ {\alpha}, s _ {\alpha}) - k).\tag{5.18}
$$

Because $|x_{\alpha} - y_{\alpha}| \leqslant \alpha$ and $u, v \to 0$ at $\infty$ uniformly (5.13), we may assume (using subsequences if necessary) that $x_{\alpha}, y_{\alpha} \to x_0, x_0$ and $t_{\alpha}, s_{\alpha} \to t_0, t_0$ as $\alpha \downarrow 0$. Moreover, by (5.17),

$$
t _ {0} \in E _ {+} (\eta (m _ {0} - k))\tag{5.19}
$$

and so $t_0 > 0$. Then

$$
\eta \left(\left(\cdot + s _ {\alpha}\right) / 2\right) \psi_ {\alpha} \left(\cdot - s _ {\alpha}\right) \varphi_ {\alpha} \left(\cdot - y _ {\alpha}\right) \quad \text { and } \quad \eta \left(\left(t _ {\alpha} + \cdot\right) / 2\right) \psi_ {\alpha} \left(t _ {\alpha} - \cdot\right) \varphi_ {\alpha} \left(x _ {\alpha} - \cdot\right)
$$

are in $\mathfrak{D}(Q_T)^+$ for $\alpha$ small and using the assumed properties of $u, v$ we find

$$
\begin{array}{r l} & - \left[ \frac {\eta^ {\prime} ((t _ {\alpha} + s _ {\alpha}) / 2)}{2 \eta ((t _ {\alpha} + s _ {\alpha}) / 2)} + \frac {\psi_ {\alpha} ^ {\prime} (t _ {\alpha} - s _ {\alpha})}{\psi_ {\alpha} (t _ {\alpha} - s _ {\alpha})} \right] (u (x _ {\alpha}, t _ {\alpha}) - v (y _ {\alpha}, s _ {\alpha}) - k) \\ & \qquad + \gamma u (x _ {\alpha}, t _ {\alpha}) + H \left(- \frac {(u (x _ {\alpha} , t _ {\alpha}) - v (y _ {\alpha} , s _ {\alpha}) - k)}{\varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha})} (D \varphi_ {\alpha}) (x _ {\alpha} - y _ {\alpha})\right) \leqslant 0, \end{array}
$$

and

$$
\begin{array}{r l} & - \left[ \frac {\eta^ {\prime} ((t _ {\alpha} + s _ {\alpha}) / 2)}{2 \eta ((t _ {\alpha} + s _ {\alpha}) / 2)} - \frac {\psi_ {\alpha} ^ {\prime} (t _ {\alpha} - s _ {\alpha})}{\psi_ {\alpha} (t _ {\alpha} - s _ {\alpha})} \right] (v (y _ {\alpha}, s _ {\alpha}) - u (x _ {\alpha}, t _ {\alpha}) + k) + \gamma v (y _ {\alpha}, s _ {\alpha}) \\ & \quad + H \left(- \frac {(u (x _ {\alpha} , t _ {\alpha}) - v (y _ {\alpha} , s _ {\alpha}) - k)}{\varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha})} (D \varphi_ {\alpha}) (x _ {\alpha} - y _ {\alpha})\right) \geqslant g (y _ {\alpha}, s _ {\alpha}). \end{array}
$$

Combining these inequalities we find

$$
\begin{array}{r l} - \frac {\eta^ {\prime} ((t _ {\alpha} + s _ {\alpha}) / 2)}{\eta ((t _ {\alpha} + s _ {\alpha}) / 2)} & (u (x _ {\alpha}, t _ {\alpha}) - v (y _ {\alpha}, s _ {\alpha}) - k) + \gamma (u (x _ {\alpha}, t _ {\alpha}) - v (y _ {\alpha}, s _ {\alpha})) \\ & \leqslant - g (y _ {\alpha}, s _ {\alpha}) \leqslant \| g (\cdot , s _ {\alpha}) ^ {-} \| _ {L ^ {\infty} (\mathbb {R} ^ {N})}. \end{array}
$$

Now let $\alpha \downarrow 0$ to find

$$
\begin{array}{l} - \frac {\eta^ {\prime} (t _ {0})}{\eta (t _ {0})} (u (x _ {0}, t _ {0}) - v (x _ {0}, t _ {0}) - k) + \gamma (u (x _ {0}, t _ {0}) - v (x _ {0}, t _ {0})) \\ \leqslant \| g (\cdot , t _ {0}) ^ {-} \| _ {L ^ {\infty} (\mathbb {R} ^ {N})}. \end{array}\tag{5.20}
$$

We also claim that  $m_{0}(t_{0}) = u(x_{0}, t_{0}) - v(x_{0}, t_{0})$ , which is in fact clear. Let us review the outcome of the above that we need. If  $m_{0}$  is given by (5.14),  $\eta \in \mathcal{D}(]0, t[)$ , and (5.15) holds, we have produced  $t_{0} \in E_{+} (\eta(m_{0}(t) - k))$  such that (5.20) holds, which is

$$
- \frac {\eta^ {\prime} (t _ {0})}{\eta (t _ {0})} (m _ {0} (t _ {0}) - k) + \gamma m _ {0} (t _ {0}) \leqslant \| g (\cdot , t _ {0}) ^ {-} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}.
$$

By Corollary I.12 we conclude,

$$
e ^ {\gamma t} m _ {0} (t) \leqslant m _ {0} (0) + \int_ {0} ^ {t} e ^ {\gamma s} \left\| g (\cdot , s) ^ {-} \right\| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)} d s,
$$

which completes the proof.

REMARK (ADDED IN PROOF). If u and v are merely continuous and bounded, then  $m_{0}(t)$  is not necessarily continuous and one works with its upper-semicontinuous envelope. (Corollary I.12—and other results herein—are valid for usc functions.) The alternative proof introduced in [27] is probably more convenient then.

V.3. The cone of dependence. We are out to show that if $u, v$ are two viscosity solutions of

$$
u _ {t} + H (x, t, u, D u) = 0 \quad \text { in } \mathbf {R} ^ {N} \times ] 0, T ]\tag{5.21}
$$

with $u(x,0) = v(x,0)$ on some ball $|x| \leqslant R$, then—under natural assumptions—$u = v$ on the cone $|x| \leqslant R - Lt$ where $L$ is a Lipschitz constant for $H(x,t,r,p)$ in $p$. We assume

(5.22) $\left\{ \begin{array}{ll} H \in C(\mathbf{R}^N \times [0, T] \times R \times \mathbf{R}^N) \text{ and } H(x, t, r, p) \text{ is nondecreasing in } r \\ \text{ for } (x, t, p) \in \mathbf{R}^N \times [0, T] \times \mathbf{R}^N. \end{array} \right.$

The main result is

THEOREM V.3. Let $u, v \in C(\mathbf{R}^N \times [0, T])$ be viscosity solutions of (5.21) on $Q_T = \mathbf{R}^N \times [0, T]$. Let (5.22) hold and

(5.23)

$$
u (x, 0) \leqslant v (x, 0) \quad o n | x | \leqslant R,\tag{5.24}
$$

$$
C = \max \left(\| D u \| _ {L ^ {\infty} \left(Q _ {T}\right)}, \| D v \| _ {L ^ {\infty} \left(Q _ {T}\right)}\right), \quad m = \max \left(\| u \| _ {L ^ {\infty} \left(Q _ {T}\right)}, \| v \| _ {L ^ {\infty} \left(Q _ {T}\right)}\right)
$$

and

$$
\left\{ \begin{array}{l} | H (x, t, r, p) - H (x, t, r, q) | \leqslant L | p - q | \\ f o r | p |, | q | \leqslant C, | r | \leqslant m, | x | \leqslant R - L t, a n d 0 \leqslant t \leqslant T. \end{array} \right.\tag{5.25}
$$

Then

$$
u \leqslant v \quad o n | x | \leqslant R - L t, \quad 0 \leqslant t \leqslant T.\tag{5.26}
$$

Moreover, this is correct if $C = \infty$ in (5.25), $u, v \in C(\overline{Q}_T)$, and $H(x, t, r, p)$ is continuous in $(x, t)$ uniformly for $|r| \leqslant m$, $p \in \mathbf{R}^N$.

This result is a consequence of the following proposition.

PROPOSITION V.4. Let (5.22) hold and $u, v \in C(\overline{Q}_T)$ be viscosity solutions of (5.21) on $Q_T$. Let $\Lambda \in C^1(\overline{Q}_T), \Lambda \geqslant 0, \Lambda = 0$ for $|x|$ large and

$$
- \Lambda_ {t} > L | D \Lambda | \quad i n (\operatorname{supp} \Lambda) ^ {0} (t h e i n t e r i o r o f \operatorname{supp} \Lambda).\tag{5.27}
$$

Assume (5.24) and that (5.25) holds for $(x,t)\in (\operatorname {supp}\Lambda)^{0}$. If $u(x,0)\leqslant v(x,0)$ on $\{(x,0)\colon \Lambda (x,0) > 0\}$, then $u\leqslant v$ on $\operatorname {supp}\Lambda$. Moreover, the result is valid if $C = \infty$ in (5.25), $u,v\in C(\overline{Q}_T)$ and $H(x,t,r,p)$ is continuous in $(x,t)$ uniformly for $|r|\leqslant m$, $p\in \mathbf{R}^N$.

We prove the theorem from the proposition and then prove the proposition.

PROOF OF THEOREM V.3. Consider

$$
\Lambda (x, t) = g \left(R _ {0} - L t - \lambda | x | ^ {1 + \alpha}\right)
$$

where $g \in C^{\infty}(\mathbb{R})$, $g(r) = 0$ if $r \leqslant 0$, $g'(r) > 0$ if $r > 0$. One has

$$
\operatorname{supp} \Lambda = \left\{(x, t): 0 \leqslant t \leqslant R / L, | x | \leqslant \left(\lambda^ {- 1} \left(R _ {0} - L t\right)\right) ^ {1 / (1 + \alpha)} \right\}
$$

so $\{x: \Lambda(x, 0) > 0\} = \{|x| < (\lambda^{-1}R_0)^{1/(1+\alpha)}\}$. We choose $\lambda, \alpha$ so that

$$
\left(\lambda^ {- 1} R _ {0}\right) ^ {1 / (1 + \alpha)} \leqslant R \quad \text { or } \quad 1 \leqslant \lambda R ^ {1 + \alpha} / R _ {0},\tag{5.28}
$$

whence (5.23) implies $u(x,0) \leqslant v(x,0)$ on supp $\Lambda(\cdot,0)$. Now

$$
g ^ {\prime} \left(R _ {0} - L t - \lambda | x | ^ {1 + \alpha}\right) > 0 \quad \text { on } (\operatorname{supp} \Lambda) ^ {0}
$$

and

$$
\begin{array}{c} L \mid D \Lambda \mid = L \lambda (1 + \alpha) \mid x \mid^ {\alpha} g ^ {\prime} \big (R _ {0} - L t - \lambda \mid x \mid^ {1 + \alpha} \big), \\ - \Lambda_ {t} = L g ^ {\prime} \big (R _ {0} - L t - \lambda \mid x \mid^ {1 + \alpha} \big). \end{array}
$$

If

$$
\lambda (1 + \alpha) R _ {0} ^ {\alpha} <   1\tag{5.29}
$$

we have $-\Lambda_t > L | D\Lambda|$ on (supp $\Lambda$)$^0$. The proposition implies $u \leqslant v$ on supp $\Lambda$. We will be done once we show that we can choose $\lambda = \lambda(\alpha)$, $R_0 = R_0(\alpha)$ so that (5.28) and (5.29) hold and $\lambda(\alpha) \to 1$, $R_0(\alpha) \to R$ as $\alpha \downarrow 0$. Put $(1 + 2\alpha)R_0^{1+\alpha} = R^{1+\alpha}$. Then (5.28) and (5.29) become

$$
\frac {1}{(1 + 2 \alpha) ^ {1 / (1 + \alpha)} R ^ {\alpha}} \leqslant \lambda <   \frac {(1 + 2 \alpha) ^ {\alpha / (1 + \alpha)}}{(1 + \alpha) R ^ {\alpha}}
$$

so we may use $\lambda (\alpha) = 1 / ((1 + 2\alpha)^{1 / (1 + \alpha)}R^{\alpha})$. The proof is complete.

PROOF OF PROPOSITION V.4. Let $\varphi_{\alpha}, \psi_{\alpha}$ be as in the proof of Theorem V.2 and $u, v, \Lambda$ as in the proposition. We assume

$$
M = \max_{\substack{\text{supp} \Lambda \\ 0\leqslant t\leqslant T}}\Lambda^{2}(u - v) > 0
$$

and will reach a contradiction.

Set

$$
\begin{array}{l} M _ {\alpha} = \max _ {Q _ {T} \times Q _ {T}} \varphi_ {\alpha} (x - y) \psi_ {\alpha} (t - s) \Lambda (x, t) \Lambda (y, s) (u (x, t) - v (y, s)) \\ = \varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha}) \psi_ {\alpha} (t _ {\alpha} - s _ {\alpha}) \Lambda (x _ {\alpha}, t _ {\alpha}) \Lambda (y _ {\alpha}, s _ {\alpha}) (u (x _ {\alpha}, t _ {\alpha}) - v (y _ {\alpha}, s _ {\alpha})). \end{array}
$$

Clearly $M_{\alpha} \to M > 0$ and so $t_{\alpha}, s_{\alpha} \geqslant \delta > 0$ and $(x_{\alpha}, t_{\alpha}), (y_{\alpha}, s_{\alpha}) \in \operatorname{supp} \Lambda^0$ for $\alpha$ small. Thus

$$
\left\{ \begin{array}{l} - \frac {\psi_ {\alpha} ^ {\prime}}{\psi_ {\alpha}} (u - v) - \frac {\partial \Lambda}{\partial t} \frac {(u - v)}{\Lambda} + H \left(x _ {\alpha}, t _ {\alpha}, u, (u - v) \left(\frac {D _ {x} \varphi_ {\alpha}}{\varphi_ {\alpha}} + \frac {D _ {x} \Lambda}{\Lambda}\right)\right) \leqslant 0, \\ + \frac {\psi_ {\alpha} ^ {\prime}}{\psi_ {\alpha}} (v - u) - \frac {\partial \Lambda}{\partial s} \frac {(u - v)}{\Lambda} + H \left(y _ {\alpha}, s _ {\alpha}, v, - (u - v) \left(\frac {D _ {x} \varphi_ {\alpha}}{\varphi_ {\alpha}} - \frac {D _ {y} \Lambda}{\Lambda}\right)\right) \geqslant 0 \end{array} \right.
$$

where the reader can keep track of the correct arguments in each term. Subtracting these yields

$$
\begin{array}{r l} & - \frac {\partial \Lambda}{\partial t} (x _ {\alpha}, t _ {\alpha}) \frac {u - v}{\Lambda (x _ {\alpha} , t _ {\alpha})} - \frac {\partial \Lambda}{\partial t} (y _ {\alpha}, s _ {\alpha}) \frac {u - v}{\Lambda (x _ {\alpha} , t _ {\alpha})} \\ & \qquad + H \left(x _ {\alpha}, t _ {\alpha}, u, (u - v) \left(\frac {D _ {x} \varphi_ {\alpha}}{\varphi_ {\alpha}} + \frac {D _ {x} \Lambda}{\Lambda}\right)\right) \\ & \qquad - H \left(y _ {\alpha}, s _ {\alpha}, v, - (u - v) \left(\frac {D _ {x} \varphi_ {\alpha}}{\varphi_ {\alpha}} - \frac {D _ {y} \Lambda}{\Lambda}\right)\right) \leqslant 0. \end{array}
$$

Since $u(x_{\alpha}, t_{\alpha}) \geqslant v(y_{\alpha}, s_{\alpha})$, (5.22) allows us to replace $v$ by $u$ in the third argument of $H$ above. Now, since $(x_{\alpha}, t_{\alpha}), (y_{\alpha}, s_{\alpha}) \to (x_0, t_0) \in (\operatorname{supp} \Lambda)^0$ and

$$
\begin{array}{l} \left| (u (x _ {\alpha}, t _ {\alpha}) - v (y _ {\alpha}, s _ {\alpha})) \left(\frac {(D \varphi_ {\alpha}) (x _ {\alpha} - y _ {\alpha})}{\varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha})} + \frac {D \Lambda (x _ {\alpha} , t _ {\alpha})}{\Lambda (x _ {\alpha} , t _ {\alpha})}\right) \right| \leqslant C, \\ \left| (u (x _ {\alpha}, t _ {\alpha}) - v (y _ {\alpha}, s _ {\alpha})) \left(\frac {(D \varphi_ {\alpha}) (x _ {\alpha} - y _ {\alpha})}{\varphi_ {\alpha} (x _ {\alpha} - y _ {\alpha})} - \frac {D \Lambda (y _ {\alpha} , s _ {\alpha})}{\Lambda (y _ {\alpha} , s _ {\alpha})}\right) \right| \leqslant C \end{array}
$$

by (5.24) and Lemma II.3 we may let $\alpha \downarrow 0$ above and use (5.25) to conclude

$$
- 2 \frac {\partial \Lambda}{\partial t} \left(x _ {0}, t _ {0}\right) (u - v) \left(x _ {0}, t _ {0}\right) - 2 L \mid D \Lambda \left(x _ {0}, t _ {0}\right) \mid (u - v) \left(x _ {0}, t _ {0}\right) \leqslant 0
$$

which contradicts $-\Lambda_t > L |D\Lambda|$ on (supp $\Lambda$)$^0$. This passage to the limit is valid if $C < \infty$. If $C = \infty$ it is valid under the assumption that $H(x, t, r, p)$ is uniformly continuous in $(x, t)$ for $|r| \leqslant m, p \in \mathbb{R}^N$.

REMARK 5.30. There are many possible variants of these results, including continuous dependence of solutions of $u_t + H(x, t, u, Du) = g$ in the cone of dependence on $u(x, 0)$ in $|x| \leqslant R$ and $g$ in $|x| \leqslant R - LT$. But it is obvious how to obtain these.

REMARK 5.31. Results in the spirit of Theorem V.3 are given in A. Friedman [16], S. N. Kružkov [20] and P. L. Lions [22]. However, these all deal with generalized $(W^{1,\infty})$ solutions obtained via the vanishing viscosity method rather than intrinsically characterized solutions.

REMARK 5.32. The assumption $C < \infty$ in (5.24) is a stringent requirement—but certainly a necessary one in general. Typical existence theorems provide $W^{1,\infty}$ solutions in any case (e.g. [13, 16, 22]).

V.4. Examples of nonuniqueness. Let $b \in C(\mathbf{R})$. If the solutions of

$$
\left\{ \begin{array}{l} \frac {d x}{d t} = b (x), \\ x (0) = x _ {0} \end{array} \right.\tag{5.33}
$$

are “too” nonunique, then bounded viscosity solutions of

$$
\left\{ \begin{array}{l} u _ {t} + b (x) u _ {x} = 0, t > 0, x \in \mathbf {R}, \\ u (x, 0) = u _ {0} (x), \end{array} \right.\tag{5.34}
$$

will also not be unique.

Let us make this precise. Assume for every  $x_{0} \in R$  we may choose a solution  $x = X(t, x_{0})$  of (5.33) defined for  $t \in R$  in such a way that:  $X(t, x_{0})$  is continuous in  $(t, x_{0}), x_{0} \to X(t, x_{0})$  is a homeomorphism of R for each  $t \in R$  and  $X(t, X(\tau, x_{0})) = X(t + \tau, x_{0})$  for  $t, \tau, x_{0} \in R$  (i.e., X is a “flow” or one parameter group). We claim that then

$$
u (x, t) \equiv u _ {0} (X (- t, x))\tag{5.35}
$$

is a viscosity solution of (5.34). The initial condition is clearly satisfied. Let $\varphi \in \mathfrak{D}(\mathbf{R} \times (0, \infty))^+$, $k \in \mathbf{R}$ and $(\bar{x}, t) \in E_+(\varphi(u - k))$. Then, by (5.35),

$$
\begin{array}{r l} \varphi (\bar {x}, \bar {t}) (u (\bar {x}, \bar {t}) - k) & = \varphi (\bar {x}, \bar {t}) (u _ {0} (X (- \bar {t}, \bar {x})) - k) \\ & \geqslant \varphi (x, t) (u _ {0} (X (- t, x)) - k) \end{array}
$$

for all $t$ and $x$. Put $x = X(t - \bar{t}, \bar{x})$ in this inequality to find

$$
\varphi (\bar {x}, \bar {t}) (u (\bar {x}, \bar {t}) - k) \geqslant \varphi (X (t - \bar {t}, \bar {x}), t) (u (\bar {x}, \bar {t}) - k)
$$

for all $t$. This implies that $t \to \varphi(X(t - \bar{t}, \bar{x}), t)$ is maximized at $t = \bar{t}$ and so

$$
\frac {d}{d t} \varphi (X (t - \bar {t}, \bar {x}), t) \Big | _ {t = \bar {t}} = \varphi_ {t} (\bar {x}, \bar {t}) + b (\bar {x}) \varphi_ {x} (\bar {x}, \bar {t}) = 0.
$$

Multiplying this relation by  $(u(\bar{x},\bar{t})-k)/\varphi(\bar{x},\bar{t})$  we find u is a viscosity subsolution of  $u_{t}+bu_{x}=0$ . Similarly, it is a supersolution and so a solution.

Nonuniqueness arises when $X$ may be chosen in more than one way. In [3] examples of this may be found. The simplest have the following structure: There are classes $\mathfrak{F}$ of continuously differentiable homeomorphisms of $R$ such that for $f, g \in \mathfrak{F}$ one has $f'(f^{-1}(x)) \equiv g'(g^{-1}(x))$. If $f \neq g$ and $b(x) = f'(f^{-1}(x))$, then

$$
X _ {1} (t, x _ {0}) = f \left(t + f ^ {- 1} \left(x _ {0}\right)\right), \quad X _ {2} (t, x _ {0}) = g \left(t + g ^ {- 1} \left(x _ {0}\right)\right)
$$

are distinct flows with the desired properties. More complex examples in higher dimensions are also given in [3].

While this example is for the pure Cauchy problem, it may be regarded as a Dirichlet problem in a half-space. To get the Hamiltonian to be increasing in the unknown, set  $v = e^{-\gamma t} u$  in (5.34) so that it becomes

$$
\left\{ \begin{array}{l} v _ {t} + \gamma v + b (x) v _ {x} = 0, \\ v (x, 0) = u _ {0} (x). \end{array} \right.
$$

VI. Existence of viscosity solutions for the Cauchy problem. As in §IV, we will restrict ourselves to a few remarks. Two of the basic ways to produce solutions of the Cauchy problem are the vanishing viscosity method and numerical approximation. If the method of vanishing viscosity converges, the result will be a viscosity solution (Theorem VI.1). This fact may be used in a straightforward way to obtain many new existence and uniqueness theorems. This is indicated by the very general results stated for the simple model problem of §IV.2. The relationship to the nonlinear semigroup theory is touched on in §VI.3. Convergence of numerical schemes to viscosity solutions is discussed in [8].

VI.1. Vanishing viscosity and viscosity solutions. Avoiding useless repetition, we rely on the reader to adapt the proof of Proposition IV.1 and establish

PROPOSITION VI.1. Let $u_{\varepsilon}$ be a solution of

$$
\left\{ \begin{array}{l} u _ {\varepsilon t} - \varepsilon \Delta u _ {\varepsilon} + H _ {\varepsilon} (x, t, u _ {\varepsilon}, D u _ {\varepsilon}) = 0 \quad i n Q _ {T}, \\ u _ {\varepsilon} = z _ {\varepsilon} \quad o n \partial \Omega \times [ 0, T ], \qquad u _ {\varepsilon} (x, 0) = u _ {0 \varepsilon} (x) \quad i n \overline {{\Omega}}, \end{array} \right.\tag{6.1}
$$

with $u_{\varepsilon t}, u_{\varepsilon x_i x_j} \in C(Q_T)$ and $u \in C_b(\overline{Q}_T)$. Assume $H_{\varepsilon} \to H$ in $C(Q_T \times \mathbf{R} \times \mathbf{R}^N)$,

$z_{\varepsilon} \to z$ in $C(\partial \Omega \times [0, T])$ and $u_{0\varepsilon} \to u_0$ in $C(\overline{\Omega})$. If $\varepsilon_n \downarrow 0$ and $u_{\varepsilon_n} \to u$ in $C(Q_T)$, then $u$ is a viscosity solution of

$$
u _ {t} + H (x, t, u, D u) = 0 \quad i n Q _ {T}.\tag{6.2}
$$

If the convergence $u_{\epsilon_n} \to u$ is in $C(\overline{Q}_T)$, then $u$ also satisfies

$$
u = z \quad o n \partial \Omega \times [ 0, T ], \quad u (x, 0) = u _ {0} (x) \quad i n \overline {{{\Omega}}}.\tag{6.3}
$$

VI.2. A model problem. Let

$$
H \in C (\mathbf {R} ^ {N}), \quad u _ {0} \in \operatorname{BUC} (\mathbf {R} ^ {N})\tag{6.4}
$$

and consider the problem

$$
\left\{ \begin{array}{l l} (\mathrm{i}) & u _ {t} + H (D u) = 0 \quad \text { in } \mathbf {R} ^ {N} \times ] 0, \infty [ = Q, \\ (\mathrm{ii}) & u (x, 0) = u _ {0} (x) \quad \text { in } \mathbf {R} ^ {N}. \end{array} \right.\tag{6.5}
$$

Our main existence result for (6.5) is

THEOREM VI.2. Let (6.4) hold. Then there is a unique $u \in C(\overline{Q}) \cap C_b(\overline{Q}_T)$ for all $T > 0$ which is a viscosity solution of $u_t + H(Du) = 0$ and $Q$ and satisfies

$$
\lim _ {t \downarrow 0} \| u (\cdot , t) - u _ {0} (\cdot) \| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)} = 0.\tag{6.6}
$$

Moreover,

$$
| u (x, t) - u (y, t) | \leqslant \sup _ {\xi \in \mathbf {R} ^ {N}} | u _ {0} (\xi) - u _ {0} (\xi + y - x) | \text {   for   } x, y \in \mathbf {R} ^ {N}, t \geqslant 0.\tag{6.7}
$$

Finally, if $S(t) \colon \mathbf{BUC}(\mathbf{R}^N) \to \mathbf{BUC}(\mathbf{R}^N)$ is defined for $t \geqslant 0$ by $S(t)u_0 = u(\cdot, t)$, then $S$ is a strongly continuous nonexpansive semigroup on $\mathbf{BUC}(\mathbf{R}^N)$ such that

$$
\left\| \left(S (t) u _ {0} - S (t) v _ {0}\right) ^ {+} \right\| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)} \leqslant \left\| \left(u _ {0} - v _ {0}\right) ^ {+} \right\| _ {L ^ {\infty} \left(\mathbf {R} ^ {N}\right)}\tag{6.8}
$$

$$
f o r u _ {0} v _ {0} \in \operatorname{BUC} (\mathbf {R} ^ {N}).
$$

The existence of u satisfying (6.6) and (6.7) is easily established by the vanishing viscosity method, and we will not carry this out. (The proof of Proposition IV.3 indicates the main points.) The uniqueness and the estimate (6.8) follow from Theorem V.2. The uniqueness implies the semigroup property  $S(t)S(\tau) = S(t + \tau)$  for  $t, \tau \geqslant 0$  as usual. We remark that (6.7) also follows from (6.8) and the translation invariance of this model problem as reflected in

$$
v _ {0} (x + y) = u _ {0} (x) \Rightarrow (S (t) v _ {0}) (x + y) = (S (t) u _ {0}) (x).
$$

Actually, Theorem VI.2 follows directly from Proposition IV.3 and nonlinear semigroup theory, as recalled next.

VI.3. An m-accretive operator. Several authors, in particular Aizawa [1] and Tamburro [25], recognized that nonlinear semigroup theory provides solutions to the Cauchy problem for HJ equations. We just sketch this here in our new context for our model problem.

Let $H \in C(\mathbf{R}^N)$. Define an operator $A$ in BUC $(\mathbf{R}^N)$ by $u \in \mathrm{BUC}(\mathbf{R}^N)$ is in $D(A)$ if there is a $g \in \mathrm{BUC}(\mathbf{R}^N)$ for which $H(Du) = g$ in the viscosity sense and then set $Au = g$. It follows from Proposition IV.3 that for each $m \in \mathrm{BUC}(\mathbf{R}^N)$ and $\lambda > 0$ the

problem  $u + \lambda Au = m$  has a unique viscosity solution  $u \in D(A)$ . Denote this solution by  $u = J_{\lambda}m$ ,  $J_{\lambda} = (I + \lambda A)^{-1}$ . It also follows from Proposition IV.3 that

$$
\left\{ \begin{array}{l l} (\mathrm{i}) & \| (J _ {\lambda} m - J _ {\lambda} n) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant \| (m - n) ^ {+} \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}, \\ (\mathrm{ii}) & \| (J _ {\lambda} m - J _ {\lambda} n) \| _ {L ^ {\infty} (\mathbf {R} ^ {N})} \leqslant \| (m - n) \| _ {L ^ {\infty} (\mathbf {R} ^ {N})}, \end{array} \right.\tag{6.9}
$$

for $m, n \in \mathrm{BUC}(\mathbf{R}^N)$. The condition (6.9)(ii) is the definition of “$A$ is accretive” in $\mathrm{BUC}(\mathbf{R}^N)$. The fact that also $R(I + \lambda A) = \mathrm{BUC}(\mathbf{R}^N)$ is by definition “$A$ is $m$-accretive” in $\mathrm{BUC}(\mathbf{R}^N)$. Clearly $D(A)$ is dense in $\mathrm{BUC}(\mathbf{R}^N)$. By the Crandall-Liggett Theorem (see, e.g., [2, 7, 11]), the functions $u_{\varepsilon} \colon [0, \infty] \to \mathrm{BUC}(\mathbf{R}^N)$ defined for $\varepsilon > 0$ by

$$
\left\{ \begin{array}{l l} (\mathrm{i}) & u _ {\varepsilon} (0) = u _ {0}, \\ (\mathrm{ii}) & \frac {u _ {\varepsilon} (t + \varepsilon) - u _ {\varepsilon} (t)}{\varepsilon} + A u _ {\varepsilon} (t + \varepsilon) = 0 \quad \text { for } t > 0 \end{array} \right.\tag{6.10}
$$

converge in  $\mathbf{BUC}(\mathbb{R}^{N})$  uniformly on compact t-sets as  $\varepsilon\downarrow0$  to a limit

$$
\lim _ {\varepsilon \downarrow 0} u _ {\varepsilon} (t) = \lim _ {\varepsilon \downarrow 0} (I + \varepsilon A) ^ {- [ t / \varepsilon ]} u _ {0} = S (t) u _ {0}
$$

where $S(t)$ is a strongly continuous nonexpansive semigroup on $\mathbf{BUC}(\mathbf{R}^N)$. We claim $S(t)u_0$ is the viscosity solution of (6.5). Indeed, let $u = S(t)u_0$, $k \in \mathbb{R}$, $\varphi \in \mathfrak{D}(Q)^+$ and $E_{+}(\varphi(u - k)) = \{(x_0, t_0)\}$. Set $u_{\varepsilon}(x, t) = u_{\varepsilon}(t)(x)$. Since $u_{\varepsilon} \to u$ locally uniformly, there will be an $(x_{\varepsilon}, t_{\varepsilon})$ in $E_{+}(\varphi(u_{\varepsilon} - k))$ for all sufficiently small $\varepsilon > 0$ for which $t_0$ is not a discontinuity (a multiple of $\varepsilon$) of $u_{\varepsilon}$. In the discussion below we let $\varepsilon \downarrow 0$ in the complement of $\{t_0 / j: j = 1, 2, \ldots\}$. Clearly $(x_{\varepsilon}, t_{\varepsilon}) \to (x_0, t_0)$. We have

$$
\varphi \left(x _ {\varepsilon}, t _ {\varepsilon}\right) \left(u _ {\varepsilon} \left(x _ {\varepsilon}, t _ {\varepsilon}\right) - k\right) \geqslant \varphi (x, t) \left(u _ {\varepsilon} (x, t) - k\right).\tag{6.11}
$$

Since $x_{\varepsilon} \in E_{+}(\varphi(\cdot, t_{\varepsilon})(u_{\varepsilon}(\cdot, t_{\varepsilon}) - k), \mathbf{R}^N)$, the definition of $A$ and (6.10)(ii) yield

$$
\frac {u _ {\varepsilon} \left(x _ {\varepsilon} , t _ {\varepsilon}\right) - u _ {\varepsilon} \left(x _ {\varepsilon} , t _ {\varepsilon} - \varepsilon\right)}{\varepsilon} + H \left(\frac {- \left(u _ {\varepsilon} \left(x _ {\varepsilon} , t _ {\varepsilon}\right) - k\right)}{\varphi \left(x _ {\varepsilon} , t _ {\varepsilon}\right)} D \varphi \left(x _ {\varepsilon}, t _ {\varepsilon}\right)\right) \leqslant 0.\tag{6.12}
$$

Now, by (6.11)

$$
\left\{ \begin{array}{l} \varphi (x _ {\varepsilon}, t _ {\varepsilon}) \big (u _ {\varepsilon} (x _ {\varepsilon}, t _ {\varepsilon}) - u _ {\varepsilon} (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) \big) \\ = \varphi (x _ {\varepsilon}, t _ {\varepsilon}) \big (u _ {\varepsilon} (x _ {\varepsilon}, t _ {\varepsilon}) - k \big) - \varphi (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) \big (u _ {\varepsilon} (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) - k \big) \\ - \big (\varphi (x _ {\varepsilon}, t _ {\varepsilon}) - \varphi (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) \big) \big (u _ {\varepsilon} (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) - k \big) \\ \geqslant - \big (\varphi (x _ {\varepsilon}, t _ {\varepsilon}) - \varphi (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) \big) \big (u _ {\varepsilon} (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) - k \big). \end{array} \right.\tag{6.13}
$$

Using (6.13) in (6.12) yields

$$
\begin{array}{r l} - \frac {1}{\varphi (x _ {\varepsilon} , t _ {\varepsilon})} & \frac {(\varphi (x _ {\varepsilon} , t _ {\varepsilon}) - \varphi (x _ {\varepsilon} , t _ {\varepsilon} - \varepsilon))}{\varepsilon} (u _ {\varepsilon} (x _ {\varepsilon}, t _ {\varepsilon} - \varepsilon) - k) \\ & + H \left(- \frac {(u _ {\varepsilon} (x _ {\varepsilon} , t _ {\varepsilon}) - k)}{\varphi (x _ {\varepsilon} , t _ {\varepsilon})} D \varphi (x _ {\varepsilon}, t _ {\varepsilon})\right) \leqslant 0. \end{array}
$$

Letting $\varepsilon \downarrow 0$ we find

$$
- \frac {(u (x _ {0} , t _ {0}) - k)}{\varphi (x _ {0} , t _ {0})} \varphi_ {t} (x _ {0}, t _ {0}) + H \left(- \frac {(u (x _ {0} , t _ {0}) - k)}{\varphi (x _ {0} , t _ {0})} D \varphi (x _ {0}, t _ {0})\right) \leqslant 0
$$

and $u$ is a viscosity subsolution. Similarly, it is a supersolution and the claim is proved.

REMARK. The notation used above assumed, for simplicity, that  $H(Du) = g_{1}$  and  $H(Du) = g_{2}$  implies  $g_{1} = g_{2}$ . This has been established by L. C. Evans if H is uniformly continuous and follows from results herein if  $|H(p)| \to \infty$  as  $|p| \to \infty$ . The general case remains unsettled at the moment, so the A above might be “multivalued” for some choices of H.

We make some further remarks below which help to clarify the relationship between the notions of viscosity solutions and accretivity. (Only the reader who is familiar with accretivity in spaces of continuous functions and its characterization via duality will see the remarks in this light.) Assume  $H \in C(\Omega \times \mathbf{R} \times \mathbf{R}^{N})$ ,  $g \in C(\Omega)$  and  $u \in C_{b}(\Omega)$ . By Theorem I.3 and Proposition I.18, u is a viscosity solution of

$$
H (x, u, D u) \leqslant g (x) \quad \text { in } \Omega\tag{6.14}
$$

if and only if for $\psi \in C^{1}(\Omega)$

$$
H (x, u (x), D \psi (x)) \leqslant g (x)\tag{6.15}
$$

at each local maximum of $u - \psi$. Since we assumed that $u$ is bounded, simple arguments show that this condition be rewritten as

$$
H (x, u (x), D \psi (x)) \leqslant g (x) \quad \text { on } E _ {+} (u - \psi) \text { for } \psi \in C _ {b} ^ {1} (\Omega).\tag{6.16}
$$

Similarly, $u$ is a supersolution if and only if

$$
H (x, u (x), D (x)) \geqslant g (x) \quad \text { on } E _ {-} (u - \psi) \text { for } \psi \in C _ {b} ^ {1} (\Omega)\tag{6.17}
$$

and, combining (6.16) and (6.17), $u$ is a viscosity solution of $H(x, u, Du) = g$ if and only if

$$
\begin{array}{l} \big (H (x, u (x), D \psi (x)) - g (x) \big) \big (u (x) - \psi (x) \big) \geqslant 0 \\ \text { on } E _ {+} (u - \psi) \cup E _ {-} (u - \psi) \text { for } \psi \in C _ {b} ^ {1} (\Omega). \end{array}\tag{6.18}
$$

In the case in which H is independent of  $(x, u)$  and  $\Omega = R^{N}$ , this implies that A constructed above is the unique maximal T-accretive extension of its restriction to smooth functions.

## REFERENCES

1. S. Aizawa, A semigroup treatment of the Hamilton-Jacobi equation in several space variables, Hiroshima Math. J. 6 (1976), 15–30.

2. V. Barbu, Nonlinear semigroups and differential equations in Banach spaces, Noordhoff, Leyden, 1976.

3. Anatole Beck, Uniqueness of flow solutions of differential equations, Recent Advances in Topological Dynamics, Lecture Notes in Math., vol. 318, Springer-Verlag, Berlin and New York, 1973, pp. 30–50.

4. S. H. Benton, The Hamilton-Jacobi equation: A global approach, Academic Press, New York, 1977.

5. J. M. Bony, Principe du maximum dans les espaces de Sobolev, C. R. Acad. Sci. Paris Sér. A-B 265 (1967), 333-336.

6. E. D. Conway and E. Hopf, Hamilton's theory and generalized solutions of the Hamilton-Jacobi equation, J. Math. Mech. 13 (1964), 939–986.

7. M. G. Crandall, An introduction to evolution governed by accretive operators, Dynamical Systems—An International Symposium (L. Cesari, J. Hale, J. LaSalle, eds.), Academic Press, New York, 1976, pp. 131–165.

8. M. G. Crandall and P. L. Lions, Condition d'unicité pour les solutions généralisées des équations de Hamilton-Jacobi du 1 $^{er}$ ordre, C. R. Acad. Sci. Paris Sér. A–B 292 (1981), 183–186.

9. \_\_\_\_, Two approximations of solutions of Hamilton-Jacobi equations (to appear).

10. A. Douglas, The continuous dependence of generalized solutions of nonlinear partial differential equations upon initial data, Comm. Pure Appl. Math. 14 (1961), 267-284.

11. L. C. Evans, On solving certain nonlinear partial differential equations by accretive operator methods, Israel J. Math. 86 (1980), 225–247.

12. \_\_\_\_, Application of nonlinear semigroup theory to certain partial differential equations, Nonlinear Evolution Equations (M. G. Crandall, ed.), Academic Press, New York, 1978.

13. W. H. Fleming, The Cauchy problem for a nonlinear first order partial differential equation, J. Differential Equations 5 (1969), 515–530.

14. \_\_\_\_, Nonlinear partial differential equations—probabilistic and game theoretic methods, Problems in Nonlinear Analysis, CIME, Ed. Cremonese, Roma, 1971.

15. \_\_\_\_, The Cauchy problem for degenerate parabolic equations, J. Math. Mech. 13 (1964), 987–1008.

16. A. Friedman, The Cauchy problem for first order partial differential equations, Indiana Univ. Math. J. 23 (1973), 27–40.

17. E. Hopf, On the right weak solution of the Cauchy problem for a quasilinear equation of first order, J. Math. Mech. 19 (1969/70), 483–487.

18. S. N. Kružkov, Generalized solution of the Hamilton-Jacobi equations of Eikonal type. I, Math. USSR-Sb. 27 (1975), 406–446.

19. \_\_\_\_, Generalized solutions of nonlinear first order equations and certain quasilinear parabolic equations, Vestnik Moscow. Univ. Ser. I Mat. Meh. 6 (1964), 67–74. (Russian)

20. \_\_\_\_, Generalized solutions of first order nonlinear equations in several independent variables. I, Mat. Sb. 70 (112) (1966), 394–415; II, Mat. Sb. (N. S.) 72 (114) (1967), 93–116. (Russian)

21. \_\_\_\_, First order quasilinear equations with several space variables, Math. USSR-Sb. 10 (1970), 217–243.

22. P. L. Lions, Generalized solutions of Hamilton-Jacobi equations, Pitman Research Notes Series, Pitman, London, 1982.

23. \_\_\_\_, Control of diffusion processes in  $R^{N}$ , Comm. Pure Appl. Math. 34 (1981), 121–147.

24. O. A. Oleinik, Discontinuous solutions of nonlinear differential equations, Amer. Math. Soc. Transl. 26 (1963), 95–172.

25. M. B. Tamburro, The evolution operator approach to the Hamilton-Jacobi equations, Israel J. Math. 26 (1977), 232–264.

26. A. I. Vol'pert, The spaces BV and quasilinear equations, Math. USSR-Sb. 2 (1967), 225-267.

27. M. G. Crandall, P. L. Lions and L. C. Evans, Some properties of viscosity solutions of Hamilton-Jacobi equations, Trans. Amer. Math. Soc. (to appear).

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF WISCONSIN, MADISON, WISCONSIN 53706

CEREMADE, UNIVERSITÉ PARIS-IX, DAUPHINE, PARIS, FRANCE