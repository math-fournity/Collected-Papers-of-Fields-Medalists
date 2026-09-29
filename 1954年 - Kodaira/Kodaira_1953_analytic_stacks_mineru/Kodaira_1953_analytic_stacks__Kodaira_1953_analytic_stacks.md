\* This note is an abstract of results to appear in the Acta Mathematica 1954, or in the Report$^{5}$ of the Michigan Conference of June 1953. These papers, together with three earlier papers of this series and papers by Kaplan$^{6}$ are listed below:

$^{1}$  “Topological Methods on Riemann Surfaces. Pseudoharmonic Function,” Contributions to the Theory of Riemann Surfaces, Ann. Math. Studies, No. 30, 111–139 (1953).

$^{2}$  “The Existence of Pseudoconjugates on Riemann Surfaces,” Fund. Math., 39, 269–287 (1952).

$^{3}$  “Curve Families F\* Locally the Level Curves of a Pseudoharmonic Function,” Acta Mathematica (1954).

$^{4}$  “Contour Equivalent Pseudoharmonic Functions and Pseudoconjugates,” Am. J. Math., 75, 23–51 (1952).

$^{5}$  “Conjugate Nets on an Open Riemann Surface,” Report of the Michigan Conference of June 1953; (to be published).

$^{6}$  Kaplan, “Regular Curve Families Filling the Plane,” Duke Math. J., I, 7, 154–185 (1940); II, 8, 11–45 (1941). “The Structure of a Curve-Family on a Surface in the Neighborhood of an Isolated Singularity,” Am. J. Math., 64, 1–35 (1942).

# ON A DIFFERENTIAL-GEOMETRIC METHOD IN THE THEORY OF ANALYTIC STACKS\*

## By K. KODAIRA

DEPARTMENT OF MATHEMATICS, PRINCETON UNIVERSITY

Communicated by S. Lefschetz, September 9, 1953

1. Introduction.—Let $V$ be a compact Kähler variety of complex dimension $n$ and let $F$ be a complex line bundle$^{1}$ over $V$ whose structure group is the multiplicative group of complex numbers. Moreover let $\Omega^{p}(F)$ be the stack (faisceau) over $V$ of germs of holomorphic $p$-forms with coefficients in $F$ and let $H^{q}(V; \Omega^{p}(F))$ be the $q$th cohomology group of $V$ with coefficients in $\Omega^{p}(F)$. It is important for applications to determine the circumstances under which the cohomology group $H^{q}(V; \Omega^{p}(F))$ vanishes. In the present note we shall prove by a differential-geometric method due to Bochner$^{2}$ some sufficient conditions for the vanishing of $H^{q}(V; \Omega^{p}(F))$ in terms of the characteristic class of the bundle $F$.

2. Harmonic Forms with Coefficients in Complex Line Bundles. $^{3}$ —We denote by  $ds^{2} = 2 \sum g_{\alpha\beta} (dz^{\alpha} d\bar{z}^{\beta})$  the Kähler metric on V. Take a sufficiently fine finite covering  $U = \{U_{j}\}$  of V. Then the bundle F is determined by the system  $\{f_{jk}\}$  of non-vanishing holomorphic functions  $f_{jk}$  defined, respectively, in  $U_{j} \cap U_{k}$  and satisfying  $f_{jk} f_{kl} f_{lj} = 1$  in  $U_{j} \cap U_{k} \cap U_{l}$ . Clearly there exists a system  $\{a_{j}\}$  of real positive functions  $a_{j}$  of class  $C^{\infty}$  defined, respectively, in  $U_{j}$  satisfying

$$
\frac {a _ {j}}{a _ {k}} = \left| f _ {j k} \right| ^ {2}, \quad \text { in } U _ {j} \cap U _ {k}.\tag{1}
$$

A form $\varphi$ with coefficients in $F$ is, by definition, a system $\{\varphi_j\}$ of exterior differential forms $\varphi_j$ defined, respectively, in $U_j$ such that

$$
\varphi_ {j} = f _ {j k} \cdot \varphi_ {k}, \quad \text { in } U _ {j} \cap U _ {k}.
$$

For a form $\varphi = \{\varphi_j\}$ with coefficients in $F$, $\bar{\partial}\varphi = \{(\bar{\partial}\varphi)_j\}$ and $\mathfrak{d}\varphi = \{(\mathfrak{d}\varphi)_j\}$ are defined, respectively, by

$$
(\bar {\partial} \varphi) _ {j} = \bar {\partial} \varphi_ {j}, \quad (\mathfrak {d} \varphi) _ {j} = - * a _ {j} \partial \left(\frac {1}{a _ {j}} * \varphi_ {j}\right),
$$

provided that $\varphi$ is differentiable, where $*\varphi_j$ denotes the dual form of $\varphi_j$ with respect to the preassigned Kähler metric $ds^2$ on $V$. The form $\varphi$ is called harmonic if $\bar{\partial}\varphi = 0$ and $\mathfrak{d}\varphi = 0$.

Let $\Omega^{p}(F)$ be the stack (faisceau) over $V$ of germs of holomorphic $p$-forms with coefficients in $F$. Then, as was shown by the author,$^{4}$ the cohomology group $H^{q}(V; \Omega^{p}(F))$ of $V$ with coefficients in $\Omega^{p}(F)$ is isomorphic to the space $H^{p,q}(F)$ consisting of all harmonic forms of type $(p, q)$ with coefficients in $F$:

$$
H ^ {q} (V; \Omega^ {p} (F)) \cong H ^ {p, q} (F).\tag{2}
$$

As one readily infers, the mapping

$$
\varphi = \{\varphi_ {j} \} \rightarrow \varphi^ {\dagger} = \{\varphi_ {j} ^ {\dagger} \}, \quad \varphi_ {j} ^ {\dagger} = \frac {1}{a _ {j}} * \bar {\varphi} j
$$

maps $H^{p,q}(F)$ isomorphically onto $H^{n - p,n - q}(-F)$, where $-F$ denotes the complex line bundle defined by the system $\{f_{jk}^{-1}\}$. Combining this with (2), we obtain therefore the isomorphism$^{5}$

$$
H ^ {q} (V; \Omega^ {p} (F)) \cong H ^ {n - q} (V; \Omega^ {n - p} (- F)).\tag{3}
$$

3. An Inequality.—The equations $\bar{\partial}\varphi = 0$, $\mathfrak{d}\varphi = 0$ for $\varphi = \{\varphi_j\}$,

$$
\varphi_ {j} = (1 / p! q!) \sum \varphi_ {j \tau_ {1} \dots \tau_ {p} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*}} d z ^ {\tau_ {1}} \dots d z ^ {\tau_ {p}} d \bar {z} ^ {\alpha_ {1}} \dots d \bar {z} ^ {\alpha_ {q}},
$$

can be written explicitly in the forms

$$
\sum_ {m = 0} ^ {q} (- 1) ^ {m} \nabla_ {\alpha_ {m} ^ {*} \varphi_ {j _ {\tau_ {1}} \dots \tau_ {p}} \alpha_ {0} ^ {*} \dots \alpha_ {m - 1} ^ {*}} \alpha_ {m + 1} ^ {*} \dots \alpha_ {q} ^ {*} = 0,\tag{4) \( _{1} \}
$$

$$
\sum g ^ {\lambda \mu^ {*}} (\nabla_ {\lambda} + \rho_ {j \lambda}) \varphi_ {j \tau_ {1} \dots \tau_ {p} \mu^ {*} \alpha_ {2} ^ {*} \dots \alpha_ {q} ^ {*}} = 0,\tag{4) \( _{2} \}
$$

where  $\nabla_{\lambda}, \nabla_{\alpha^{*}}$  denote the covariant differentiations with respect to the local coordinates  $z^{\lambda}, \bar{z}^{\alpha}$  and where

$$
\rho_ {j \lambda} = - \partial_ {\lambda} \log a _ {j}, \quad \partial_ {\lambda} = \frac {\partial}{\partial z ^ {\lambda}}.
$$

Let $R_{\tau \alpha^{*}\beta}^{\sigma} = \bar{\partial}_{\alpha}(\sum g^{\sigma \nu^{*}}\partial_{\beta}g_{\tau \nu^{*}})$ be the curvature tensor and let $R_{\alpha^{*}\beta} = \sum R_{\tau \alpha^{*}\beta}^{\tau}$ be the Ricci tensor. Moreover we set

$$
X _ {\lambda \alpha^ {*}} = - \bar {\partial} _ {\alpha} \rho_ {j \lambda} = \partial_ {\lambda} \bar {\partial} _ {\alpha} \log a _ {j}.\tag{5}
$$

Then, by a simple computation, we infer from (4) that, for any harmonic form $\varphi = \{\varphi_j\} \epsilon H^{p,q}(F)$, the following relation holds:

$$
\sum g ^ {\lambda \mu^ {*}} (\nabla_ {\lambda} + \rho_ {j \lambda}) \nabla_ {\mu^ {*}} \varphi_ {j _ {\tau_ {1}} \dots \tau_ {p} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*}} = \sum_ {m} \sum_ {h} \sum R _ {\tau_ {h} \alpha_ {m} ^ {*}} ^ {\sigma} ^ {\mu^ {*}} \times
$$

$$
\varphi_ {j \tau_ {1} \dots (\sigma) _ {h}} \dots \tau_ {p} \alpha_ {1} ^ {*} \dots (\mu^ {*}) _ {m} \dots \alpha_ {q} ^ {*} + \sum_ {m} \sum [ X _ {\alpha_ {m} ^ {*}} ^ {\mu^ {*}} - R _ {\alpha_ {m} ^ {*}} ^ {\mu^ {*}} ] \times
$$

$$
\varphi_ {j \tau_ {1}} \dots \tau_ {p} \alpha_ {1} ^ {*} \dots (\mu^ {*}) _ {m} \dots \alpha_ {q} ^ {*},\tag{6}
$$

where $X^{\mu^{*}}_{\alpha^{*}} = \sum g^{\lambda \mu^{*}}X_{\lambda \alpha^{*}}, R^{\mu^{*}}_{\alpha^{*}} = \sum g^{\lambda \mu^{*}}\bar{R}_{\lambda^{*}\alpha}$ and where $(\sigma)_h$ or $(\mu^{*})_m$ indicates that $\tau_h$ or $\alpha_m^*$ is to be replaced by $\sigma$ or $\mu^*$ respectively. We note here that $\partial \overline{\partial} \log a_j = \partial \overline{\partial} \log a_k$ in $U_j \cap U_k$, so

$$
\sum X _ {\lambda \alpha^ {*}} d z ^ {\lambda} d \bar {z} ^ {\alpha} = \partial \bar {\partial} \log a _ {j}\tag{7}
$$

is a well defined 2-form on the whole of $V$. Now we set

$$
\xi_ {\mu^ {*}} = \frac {1}{a _ {j}} \sum \nabla_ {\mu^ {*}} \varphi_ {j \tau_ {1} \dots \tau_ {p}} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*} \cdot \bar {\varphi} _ {j} ^ {\tau_ {1} \dots \tau_ {p}} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*}
$$

where

$$
\bar {\varphi} _ {j} ^ {\tau_ {1} \dots \tau_ {p} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*}} = \sum g ^ {\tau_ {1} \sigma_ {1} ^ {*}} \dots g ^ {\tau_ {p} \sigma_ {p} ^ {*}} g ^ {\beta_ {1} \alpha_ {1} ^ {*}} \dots g ^ {\beta_ {q} \alpha_ {q} ^ {*} \overline {{\varphi_ {j \sigma_ {1} \cdots \sigma_ {p} \beta_ {1} ^ {*} \cdots \beta_ {q} ^ {*}}}}}.
$$

Then $\xi = \sum \xi_{\tau^{*}}d\bar{z}^{\tau}$ is a well defined 1-form on $V$ and

$$
- \delta \xi = \sum g ^ {\lambda \mu^ {*}} \nabla_ {\lambda} \xi_ {\mu^ {*}}
$$

$$
= \# + \frac {1}{a _ {j}} \sum g ^ {\lambda \mu^ {*}} (\nabla_ {\lambda} + \rho_ {j \lambda}) \nabla_ {\mu^ {*} \varphi_ {j _ {\tau_ {1}} \dots \tau_ {p}}} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*} \cdot \bar {\varphi} _ {j} ^ {\tau_ {1} \dots \tau_ {p}} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*}\tag{8}
$$

where

$$
\# = \frac {1}{a _ {j}} \sum g ^ {\lambda \mu^ {*}} \nabla_ {\mu^ {*} \varphi_ {j \tau_ {1}} \dots \tau_ {p} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*}} \cdot \overline {{\nabla_ {\lambda^ {*} \varphi_ {j}}}} ^ {\tau_ {1} \dots \tau_ {p}} \alpha_ {1} ^ {*} \dots \alpha_ {q} ^ {*} \geq 0.
$$

Denoting by $g$ the determinant $g = |g_{\alpha \beta^*}|$, we have $\int_V \delta \xi \cdot g dV = 0$, where $dV = (i)^n dz^1 d\bar{z}^1 \ldots dz^n d\bar{z}^n$. Combining (6) with (8), we obtain therefore the inequality

$$
\begin{array}{l} 0 \geq \int_ {V} \left\{q \sum (\delta_ {\tau} ^ {\sigma} [ X _ {\alpha^ {*}} ^ {\beta^ {*}} - R _ {\alpha^ {*}} ^ {\beta^ {*}} ] + p R _ {\tau \alpha^ {*}} ^ {\sigma \beta^ {*}}) \cdot \right. \\ \left. \frac {1}{a _ {j}} \varphi_ {j \sigma \tau_ {2} \dots \tau_ {p} \beta^ {*} \alpha_ {2} ^ {*} \dots \alpha_ {q} ^ {*}} \bar {\varphi} _ {j} ^ {\tau \tau_ {2} \dots \tau_ {p} \alpha^ {*} \alpha_ {2} ^ {*} \dots \alpha_ {q} ^ {*}} \right\} g d V. \end{array}\tag{9}
$$

By a $(p, q)$-form we shall mean a $(p + q)$-form of type $(p, q)$. A real (1,1)-form $\psi$ on $V$ can be written in the form $\psi = i \sum \psi_{\alpha\beta^*}(z, \bar{z}) dz^\alpha d\bar{z}^\beta$, where $\psi_{\alpha\beta^*} = \psi_{\alpha\beta^*}(z, \bar{z})$ satisfy $\bar{\psi}_{\alpha\beta^*} = \psi_{\beta\alpha^*}$. We say that such a form $\psi$

is positive and write $\psi > 0$ if the Hermitian form $\sum \psi_{\alpha \beta *} (z, \bar{z}) \bar{u}^{\alpha} u^{\beta}$ in $n$ variables $u^{1}, u^{2}, \ldots, u^{n}$ is positive definite at each point $z$ on $V$.

Now, let $c(F)$ be the characteristic class of the principal bundle associated with $F$.

LEMMA. Let $\{a_{j}\}$ be a system of functions satisfying (1). Then the real $d$-closed (1,1)-form $\gamma = (i/2\pi)\partial\overline{\partial}\log a_{j}$ belongs to the characteristic class $c(F)$ of the bundle $F$. Conversely, given a $d$-closed real (1,1)-form $\gamma$ of class $C^{\infty}$ belonging to the characteristic class $c(F)$, there exists a system $\{a_{j}\}$ of positive functions $a_{j}$ of class $C^{\infty}$ satisfying (1) such that $(i/2\pi)\partial\overline{\partial}\log a_{j} = \gamma$.

Proof: Let $\pi$ be the canonical projection of $F$ onto $V$ and let $\zeta_j$ be the linear coordinate on the fibre $\pi^{-1}(z)$, $z \in U_j$, such that $\zeta_j = f_{jk}(z)\zeta_k$ for $z \in U_j \cap U_k$. The principal bundle $F^*$ associated with $F$ is obtained from $F$ by removing the origin $\zeta_j = 0$ of each fibre $\pi^{-1}(z)$. Now

$$
\Phi = \frac {1}{2 \pi i} (d \log \zeta_ {j} - \partial \log a _ {j})
$$

is a well defined 1-form of class $C^\infty$ on the principal bundle $F^*$ and

$$
- d \Phi = \frac {i}{2 \pi} \partial \bar {\partial} \log a _ {j},
$$

while the restriction of $\Phi$ to the fibre $\pi^{-1}(z)^{*} = \pi^{-1}(z) - (0)$ of $F^{*}$ equals the $d$-closed 1-form $(1/2\pi i)d \log \zeta_{j}$ which represents the basic cohomology class of $\pi^{-1}(z)^{*}$. This shows that $\gamma = (i/2\pi)\partial\bar{\partial} \log a_{j}$ belongs to the characteristic class $c(F)$ of $F^{*}$.

To prove that every $\gamma$ belonging to $c(F)$ can be written in the form $\gamma = (i/2\pi)\partial\overline{\partial}\log a_j$, we take a system $\{a_j'\}$ satisfying (1) and consider the difference $\gamma_0 = \gamma - (i/2\pi)\partial\overline{\partial}\log a_j'$. Obviously the harmonic part $H\gamma_0$ of $\gamma_0$ vanishes and consequently $\gamma_0 = \Delta G\gamma_0 = 2\partial\overline{\partial}G\gamma_0$, where $G$ denotes the Green's operator. Using the formula$^8$$\Lambda\partial - \partial\Lambda = -i\partial$, we get therefore $\gamma_0 = i2\partial\overline{\partial}\Lambda G\gamma_0$. Now $r = 2\Lambda G\gamma_0$ is a real scalar function of class $C^\infty$ defined on the whole of $V$ and, hence, setting $a_j = a_j' \cdot e^{i\pi r}$ we obtain a system $\{a_j\}$ of positive functions $a_j$ of class $C^\infty$ satisfying (1) and also $(i/2\pi)\partial\overline{\partial}\log a_j = \gamma$.

Now, letting $\gamma = (i/2\pi) \sum X_{\alpha\beta*} dz^{\alpha} d\bar{z}^{\beta}$ be an arbitrary real (1,1)-form, we introduce the Hermitian form

$$
\Theta^ {p, q} (\gamma , u; z) = \sum \left(\delta_ {\tau} ^ {\sigma} \left[ X _ {\alpha^ {*}} ^ {\beta^ {*}} - R _ {\alpha^ {*}} ^ {\beta^ {*}} \right] + p R _ {\tau \alpha^ {*}} ^ {\sigma \beta^ {*}}\right) \times
$$

$$
\mathcal {U} _ {\sigma \tau_ {2}} \dots \tau_ {p} \beta^ {*} \alpha_ {2} ^ {*} \dots \alpha_ {q} ^ {*} \bar {\mathcal {U}} ^ {\tau \tau_ {2}} \dots \tau_ {p} \alpha^ {*} \alpha_ {2} ^ {*} \dots \alpha_ {q} ^ {*}
$$

in a skew-symmetric tensor $u_{\tau_1\tau_2 \ldots \tau_p\alpha_1^* \ldots \alpha_q^*}$ at each point $z$ on $V$, provided that $q \geq 1$. Then the inequality (9) can be written in the following form:

$$
\int_ {V} \frac {g}{a _ {j}} \Theta^ {p, q} (\gamma , \varphi_ {j}; z) d V \leq 0, \quad \text { for } q \geq 1.\tag{10}
$$

With the help of the above lemma, we derive from (10) the following theorem:

THEOREM 1. If the characteristic class $c(F)$ of $F$ contains a real $d$-closed (1,1)-form $\gamma = (i/2\pi) \sum X_{\alpha\beta*} dz^{\alpha} d\bar{z}^{\beta}$ which is sufficiently large with respect to the order $>$ in the sense that the Hermitian form $\Theta^{p,q}(\gamma, u; z)$ is positive definite at each point $z$ on $V$, then the cohomology groups $H^{q}(V, \Omega^{p}(F))$ and $H^{n-q}(V, \Omega^{n-p}(-F))$ both vanish, provided that $1 \leqq q \leqq n$.

Proof: In view of (2) and (3), it is sufficient to show that $H^{p,q}(F) = 0$. By virtue of the above lemma, we may choose the system $\{a_j\}$ satisfying (1) such that $(i / 2\pi)\partial \bar{\partial}\log a_j = \gamma$. Then the inequality (10) holds for any $\varphi = \{\varphi_j\} \in H^{p,q}(F)$, while, by hypothesis, $\Theta^{p,q}(\gamma, \varphi_j; z) > 0$ unless $\varphi_j = 0$. This proves that $H^{p,q}(F) = 0$, q. e. d.

In the case where $p = n$, we have

$$
\Theta^ {n, q} (\gamma , u; z) = n! \sum X _ {\alpha^ {*}} ^ {\beta^ {*}} u _ {1 2 \dots n \beta^ {*} \alpha_ {2} ^ {*} \dots \alpha_ {q} ^ {*}} \bar {u} ^ {1 2 \dots n \alpha^ {*} \alpha_ {2} ^ {*} \dots \alpha_ {q} ^ {*}}.
$$

Hence $\Theta^{n,q}(\gamma, u; z)$ is positive definite if and only if $\gamma > 0$. As a corollary to the above theorem, we therefore obtain the following:

THEOREM 2. If $c(F)$ contains a real $d$-closed (1,1)-form $\gamma > 0$, then the cohomology groups $H^q(V, \Omega^n(F))$ and $H^{n - q}(V, \Omega^0(-F))$ both vanish for $1 \leq q \leq n$.

By the canonical bundle over V we shall mean the complex line bundle K defined by the system  $\{J_{jk}\}$  of Jacobians

$$
J _ {j k} = \frac {\partial (z _ {k} ^ {1} , \dots , z _ {k} ^ {n})}{\partial (z _ {j} ^ {1} , \dots , z _ {j} ^ {n})},
$$

where $(z_j^1, \ldots, z_j^n)$ is the local coordinates in $U_j$. We note that $-c(K)$ equals the first Chern class of the variety $V$. Since the isomorphism

$$
\Omega^ {0} (F) \cong \Omega^ {n} (F - K)
$$

holds in an obvious manner, we get from the above theorem the following: THEOREM 3. If $c(F) - c(K)$ contains a real $d$-closed (1,1)-form $\gamma > 0$, then the cohomology group $H^q(V, \Omega^0(F))$ vanishes for $1 \leq q \leq n$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$C^*$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* This work was supported by a research project at Princeton University sponsored by the Office of Ordnance Research, U. S. Army.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">K.,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  By a complex line bundle over V will be meant an analytic fibre bundle over V whose fibre is the complex number field C and whose structure group is the multiplicative group  $C^{*}$  of complex numbers acting on C. Cf. Kodaira, K., and Spencer, D. C., "Groups of Complex Line Bundles Over Compact Kähler Varieties," these PROCEEDINGS, 39, 868–872 (1953).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  Bochner, S., “Curvature and Betti Numbers” (I) and (II), Ann. Math., 49, 379–390 (1948); 50, 77–93 (1949).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{4}$  Kodaira, loc. cit.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$  See Kodaira, K., “On Cohomology Groups of Compact Analytic Varieties with Coefficients in Some Analytic Faisceaux,” these PROCEEDINGS, 39, 865–868 (1953).</span></small>

$^{5}$  This result reduces to a special case of Serre's duality theorem.

$^{6}$  See Garabedian, P. R., and Spencer, D. C., “A Complex Tensor Calculus for Kähler Manifolds,” Acta Math., 89, 279–331 (1953).

$^{7}$ In view of de Rham's theorem, any cohomology class may be regarded as a class of $d$-closed forms. By a $d$-closed form we shall mean a form which is closed under $d$.

$^{8}$  Garabedian and Spencer, loc. cit., p. 290.

# ON A THEOREM OF LEFSCHETZ AND THE LEMMA OF ENRIQUES-SEVERI-ZARISKI\*

By K. Kodaira and D. C. Spencer

DEPARTMENT OF MATHEMATICS, PRINCETON UNIVERSITY

Communicated by S. Lefschetz, October 8, 1953

1. Introduction.—The present note is mainly concerned with a generalization of a theorem of Lefschetz which establishes a relation between the cohomology groups of an algebraic variety and those of its general hyperplane sections. We generalize the theorem to the case of cohomology groups of Kähler varieties with coefficients in some analytic stacks. Our generalization includes the lemma of Enriques-Severi-Zariski as a special case.

2. Some Exact Sequences of Stacks.—Let $V$ be a compact Kähler variety of complex dimension $n$ and let $S$ be a non-singular analytic subvariety of $V$ of complex dimension $n-1$. Take a sufficiently fine finite covering $\{U_j\}$ of $V$. Then, in each $U_j$, the subvariety $S$ is defined by a holomorphic equation $s_j = 0$. We associate with $S$ the complex line bundle$^1$$\{S\}$ determined by the system $\{s_{jk}\}$ of non-vanishing holomorphic functions $s_{jk} = s_j/s_k$ defined, respectively, in $U_j \cap U_k$. We note that the characteristic class$^2$$c(\{S\})$ of $\{S\}$ is the dual of the homology class of the cycle $S$. For simplicity's sake, we set $c(S) = c(\{S\})$. Now, let $F$ be an arbitrary complex line bundle over $V$ and let $\Omega^p(F)$ be the stack over $V$ of the germs of holomorphic $p$-forms with coefficients in $F$. Take a point $\mathfrak{p} \in S \cap U_j$ and choose a system of local coordinates $(z_j^1, \ldots, z_j^n)$ in $U_j$ such that $s_j(z) = z_j^1$. Then each germ $\eta_j \in \Omega^p(F)_{\mathfrak{p}}$ can be written in the form

$$
\eta_ {j} = \sum_ {1 <   \alpha_ {1} <   \dots <   \alpha_ {p}} \eta_ {j \alpha_ {1} \dots \alpha_ {p}} d z _ {j} ^ {\alpha_ {1}} \dots d z _ {j} ^ {\alpha_ {p}} + \sum_ {1 <   \alpha_ {2} <   \dots <   \alpha_ {p}} \eta_ {j 1 \alpha_ {2} \dots \alpha_ {p}} d z _ {j} ^ {1} d z _ {j} ^ {\alpha_ {2}} \dots d z _ {j} ^ {\alpha_ {p}},
$$

where $\Omega^{p}(F)_{\mathfrak{p}}$ is the fiber of $\Omega^{p}(F)$ over the point $\mathfrak{p}$. With the help of this expression, we associate with $\eta_{j}$ two germs $\eta_{j}^{\prime}, \eta_{j}^{\prime \prime}$ of holomorphic forms on $S$ defined, respectively, by

$$
\eta_ {j} ^ {\prime} = \sum_ {1 <   \alpha_ {1} <   \dots <   \alpha_ {p}} (\eta_ {j \alpha_ {1} \dots \alpha_ {p}}) _ {S} d z _ {j} ^ {\alpha_ {1}} \dots d z _ {j} ^ {\alpha_ {p}},
$$

$$
\eta_ {j} ^ {\prime \prime} = \sum_ {1 <   \alpha_ {2} <   \dots <   \alpha_ {p}} (\eta_ {j 1 \alpha_ {2} \dots \alpha_ {p}}) _ {S} d z _ {j} ^ {\alpha_ {2}} \dots d z _ {j} ^ {\alpha_ {p}},
$$