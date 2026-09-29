# Prym Varieties I

DAVID MUMFORD

HARVARD UNIVERSITY

## INTRODUCTION

This paper gives the first steps in a purely algebraic version (in all characteristics except two) of the Riemann–Prym–Wirtinger–Schottky–Jung theory of double coverings of one curve (or compact Riemann surface) over another. It also tries to incorporate some of the interesting generalizations of this theory in the thesis of Fay [4]. The basic idea is this:

$$
\pi \colon \quad \hat {C} \longrightarrow C
$$

is a double covering, where C and  $\tilde{C}$  are nonsingular complete curves with Jacobians J and  $\tilde{J}$ . The involution  $\iota\colon\tilde{C}\longrightarrow\tilde{C}$  interchanging sheets extends to  $\iota\colon\tilde{J}\longrightarrow\tilde{J}$ , and up to some points of order two,  $\tilde{J}$  splits into an even part J and an odd part P, the Prym variety. The Prym P has a natural polarization on it, but only in two cases—where  $\pi$  has zero or two branch points—do we get a unique principal polarization on P, hence a theta divisor  $\Xi\subset P$ . This is discussed in the first part of this paper (Sections 1–3).

The surprise comes, however, on a closer analysis of the relations between the theta divisors $\Theta \subset J$ and $\widetilde{\Theta} \subset \tilde{J}$: It turns out that they are related in a much tighter way than would be expected from looking only at the configuration of Abelian varieties and homomorphisms present. In the case of zero or two branch points this leads finally to identities relating $(J, \Theta)$ and $(P, \Xi)$ discovered by Schottky and Jung [15] (cf. also Riemann [13] and Farkas and Rauch [3]). The point is that the existence of any $(P, \Xi)$ standing in this relation to $(J, \Theta)$ means that if $g \geqslant 4$, $J$ is not the most general Abelian variety of dimension $g!$. Unfortunately, an efficient method of translating this into an equivalent polynomial identity on the theta nulls of $J$ is only known at present for $g = 4$. These matters are discussed in the second part of this paper (Sections 4 and 5).

In the other direction, the curves C and  $\tilde{C}$  and their geometry can be used to compute things about P. The importance of this is that it is usually quite hard to make detailed computations on the geometry of the theta divisor in a general principally polarized n-dimensional Abelian variety [which has  $\frac{1}{2}n(n+1)$  moduli]; those which are Jacobians of curves of genus n (with 3n-3 moduli) are much better understood. However, by taking the Pryms for unramified double coverings  $\tilde{C}\longrightarrow C$ , genus

$C = n + 1$, we get a bigger family of principally polarized $n$-dimensional Abelian varieties which can be closely studied (depending on $3n$ moduli). For instance, for $n = 2, 3$ a generic principally polarized Abelian variety is a Jacobian; and according to Wirtinger, for $n = 4, 5$ a generic principally polarized Abelian variety appears to be a Prym but not of course a Jacobian. Moreover Pryms occur sometimes as the Intermediate Jacobians of unirational but not rational 3-folds (cf. Clemens and Griffiths [2], and Murre [12]). In the final part of the paper (Sections 6 and 7) with these applications in mind we compute the dimension of singular locus of the theta divisor in a Prym using results of Martens [8].

In a sequel to this paper we would like to discuss (a) how close the Schottky–Jung identities come to characterizing Jacobians among all Abelian varieties, and (b) ways of utilizing the Schottky–Jung identities in the two-branch-point case.

## NOTATIONS

k the algebraically closed ground field: always of char. ≠2

$\mathbb{R}(X)$ field of rational functions on a variety $X$

$\operatorname{Pic}(X)$ group of divisor classes, line bundles, or invertible sheaves on a variety $X$$\operatorname{Pic}^0 (X)$ connected component of $0\in \operatorname {Pic}(X)$

$\hat{X}$ another notation for $\operatorname{Pic}^{0}(X)$ if X is an Abelian variety (called the “dual” Abelian variety)

$\lambda_{D}\colon X\xrightarrow{\quad}\hat{X}$ the homomorphism $x\longmapsto$ [divisor class of $T_x^{-1}D - D]$, where $D$ is a divisor on an Abelian variety $X$

A polarization of an Abelian variety X is a homomorphism  $\lambda: X \longrightarrow \hat{X}$  such that  $\lambda - \lambda_{D}$  for some ample D: in this case D is determined modulo  $\operatorname{Pic}^{0}(X)$ ;  $\lambda$  is a principle polarization if  $\lambda$  is also an isomorphism, in which case  $\lambda = \lambda_{D}$  for a positive ample D, unique up to a translation. (See my book [10] for a general reference for the facts on Abelian varieties.)

## 1. DOUBLE COVERINGS OF CURVES

The main object of our study is a morphism

$$
\pi \colon \quad \tilde {C} \longrightarrow C.
$$

where C and  $\tilde{C}$  are nonsingular complete curves and  $\pi$  is of degree two, i.e.,  $\pi$  is surjective and via  $\pi^{*}$ ,  $\mathbb{R}(\tilde{C})$  is a quadratic extension of  $\mathbb{R}(C)$ . In fact, in this case C has an open covering by affines  $U_{\alpha} = Spec R_{\alpha}$  such that  $\pi^{-1}(U_{\alpha}) = Spec S_{\alpha}$ , where  $S_{\alpha}$  is an  $R_{\alpha}$ -algebra of the form

$$
S _ {\alpha} \cong R _ {\alpha} [ t _ {\alpha} ] / (t _ {\alpha} ^ {2} - \beta_ {\alpha}), \quad \beta_ {\alpha} \in R _ {\alpha}.
$$

Or, sheaf-theoretically, we may put this in the equivalent form $\tilde{C} = \mathbf{Spec}(\mathcal{S})$, where $\mathcal{S}$ is a sheaf of $\mathcal{O}_C$ algebras of the form

$$
\mathcal {S} \cong \mathcal {O} _ {c} \oplus L
$$

with L an invertible sheaf of  $O_{C}$  modules. Multiplication is given by

$$
(a + l) \cdot (b + m) = (a \cdot b + \phi (l \otimes m), a \cdot m + b \cdot l),
$$

$a, b$ sections of $\mathcal{O}_C$, $l, m$ sections of $L$, for some

$$
\phi \colon L ^ {2} \xrightarrow {\approx} \mathcal {O} _ {C} \left(- \sum_ {i = 1} ^ {m} P _ {i}\right) \subset \mathcal {O} _ {C}.
$$

Then the zeros of  $\beta_{\alpha}$ , or equivalently the points  $P_{i}$  where  $\phi(L^{2}) \neq \mathcal{O}_{c}$ , are the branch points of  $\pi$ . Since  $\tilde{C}$  is nonsingular, they are all simple zeros (equivalently,  $\sum P_{i}$  has no multiple points); and because

$$
\# \text {   branch   points   } = - \deg L ^ {2} = 2 (- \deg L),
$$

there are an even number $m = 2n$ of them.

Let $J$ and $\tilde{J}$ be the Jacobians of $C$ and $\tilde{C}$: By definition, we take this to mean

$$
J = \operatorname{Pic} ^ {0} (C), \quad \tilde {J} = \operatorname{Pic} ^ {0} (\tilde {C}).
$$

Now fix base points $x_0 \in C$, and $\tilde{x}_0 \in \tilde{C}$ such that $\pi(\tilde{x}_0) = x_0$. Then we get the Albanese mappings:

$$
t: \quad C \longrightarrow J \quad \text { via } \quad x \longmapsto \text { divisor   class } (x - x _ {0})
$$

and

$$
\tilde {i}: \quad \tilde {C} \longrightarrow \tilde {J} \quad \text { via } \quad x \longmapsto \text { divisor   class } (\tilde {x} - \tilde {x} _ {0}).
$$

Moreover, define

$$
\mathrm{Nm}: \quad \tilde {J} \longrightarrow J
$$

by either (a) the restriction of the map Nm,

$$
\begin{array}{l} \tilde {J} \subset H ^ {1} (\widetilde {C}, \mathcal {O} _ {\widetilde {c}} ^ {*}) \cong H ^ {1} (C, (\pi_ {*} \mathcal {O} _ {\widetilde {c}}) ^ {*}) \\ \Biggl \downarrow \mathrm{Nm} \\ J \subset \longrightarrow H ^ {1} (C, \mathcal {O} _ {c} ^ {*}) \end{array}
$$

or (b) the induced map on divisor classes given on divisors by $\mathfrak{A} \longmapsto \pi(\mathfrak{A})$ ($\mathfrak{A}$ a divisor on $\tilde{C}$). Then we get a commutative diagram:

$$
\begin{array}{c} \tilde {C} \xrightarrow {\tilde {t}} \tilde {J} \\ \pi \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ C \xrightarrow {t} J. \end{array}
$$

Now this diagram defines a second by applying the functor $\mathbf{Pic}^0$:

$$
\begin{array}{c} \tilde {J} = \operatorname{Pic} ^ {0} (\tilde {C}) \xleftarrow {\tilde {t} ^ {*}} \operatorname{Pic} ^ {0} (\tilde {J}) _ {\text { def }} = \hat {J} \\ \Bigg | _ {\pi^ {*}} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ J = \operatorname{Pic} ^ {0} (C) \xleftarrow {t ^ {*}} \operatorname{Pic} ^ {0} (J) _ {\text { def }} = \hat {J} \end{array}
$$

where  $\hat{J}$  and  $\hat{J}$  are the “duals” of  $\tilde{J}$  and J, respectively. By the standard theory of Jacobians,  $t^{*}$  and  $\tilde{t}^{*}$  are isomorphisms and, in fact, if  $\Theta\subset J$,  $\tilde{\Theta}\subset\tilde{J}$  are the theta divisors, then

$$
(t ^ {*}) ^ {- 1} = - \lambda_ {\Theta}, \quad (\tilde {t} ^ {*}) ^ {- 1} = - \lambda_ {\tilde {\Theta}}
$$

(where for any divisor $D$ on an Abelian variety $X$, $\lambda_{D}\colon X\longrightarrow\hat{X}$ is the homomorphism given by $x\longrightarrow[\text{divisor class }T_{x}^{-1}(D)-D]$). Thus the principally polarized Abelian varieties $(J,\Theta)$ and $(\tilde{J},\tilde{\Theta})$ are related by two maps:

$$
\pi^ {*}: \quad J \longrightarrow \tilde {J}, \qquad \mathrm{Nm:} \quad \tilde {J} \longrightarrow J
$$

and the main result is that these have two properties:

(i) $\pi^{*}$ and Nm are dual to each other:

$$
\widehat {\mathrm{Nm}} = \lambda_ {\widetilde {\Theta}} \cdot \pi^ {*} \cdot \lambda_ {\Theta} ^ {- 1}, \quad \hat {\pi} ^ {*} = \lambda_ {\Theta} \cdot \mathrm{Nm} \cdot \lambda_ {\widetilde {\Theta}} ^ {- 1}.
$$

(ii) $\mathrm{Nm} \cdot \pi^{*}: J \longrightarrow J$ is multiplication by two.

Proof of(ii). If $\mathfrak{A}$ is a divisor class of degree zero on $C$, and $\alpha$ is the corresponding point of $J$, then $\pi^{-1}(\mathfrak{A})$ represents $\pi^{*}\alpha \in \tilde{J}$ and $\pi(\pi^{-1}\mathfrak{A})$ represents $\mathrm{Nm}(\pi^{*}\alpha)$. But $\pi(\pi^{-1}\mathfrak{A}) = 2\mathfrak{A}$. Q.E.D.

Rather than studying in detail the implications of (i) and (ii) in this special case, it seems easier at this point to study such a situation in general, and afterward to specialize the study to the case of Jacobians.

## 2. A CONFIGURATION OF ABELIAN VARIETIES

Suppose  $(X, \theta_{X})$  and  $(Y, \theta_{Y})$  are two principally polarized Abelian varieties: Thus  $\theta_{X}$  and  $\theta_{Y}$  are positive divisors on X and Y, given only up to translations, however, such that  $\lambda_{\theta_{X}}$  and  $\lambda_{\theta_{Y}}$  are isomorphisms. (It is well known then that  $\theta_{X}$  and  $\theta_{Y}$  are ample and are the only positive divisors D such that  $\lambda_{D} = \lambda_{\theta_{X}}$  or  $\lambda_{\theta_{Y}}$ .)

DATA I. Suppose $\phi: X \longrightarrow Y$ is a homomorphism and assume that

$$
\phi^ {*} (\theta_ {Y}) \quad \text {   algebraically   equivalent   to   } \quad 2 \theta_ {X}\tag{2.1}
$$

i.e., $\phi^{*}\theta_{Y} - 2\theta_{X}\in \mathrm{Pic}^{0}(X)$. This is equivalent to saying

$$
\lambda_ {\phi^ {*} (\theta_ {Y})} = 2 \lambda_ {\theta_ {X}},\tag{2.2}
$$

hence (since $\lambda_{\phi^{*}D} = \hat{\phi} \cdot \lambda_{D} \cdot \phi$), it is equivalent to having the following diagram commute:

![](images/page_3_image_17.jpg)

(2.3)

Thus if we define $\psi: Y \longrightarrow X$ to be the dual $\lambda_{\theta_X}^{-1} \cdot \hat{\phi} \cdot \lambda_{\theta_Y}$ of $\phi$, we get $\psi \cdot \phi =$ mult. by two: exactly the situation of Section 1.

I claim that all triples $((X, \theta_X), (Y, \theta_Y), \phi)$ satisfying (2.1)—call these Data I—and only such triples arise in the following way.

## DATA II.

(i) $(X, \theta_X)$ is a principally polarized Abelian variety.

(ii) $P$ and $\rho: P \longrightarrow \hat{P}$ is some Abelian variety and a polarization of $P$.

(iii)  $H_{0} \subset H_{1} \subset X_{2}$  are subgroups of points of order two, and  $\psi: H_{1}/H_{0} \longrightarrow$  ker  $\rho$  is an isomorphism.

These data should satisfy:

(iv) With respect to the skew-symmetric multiplicative pairings induced by the Riemann forms of  $\theta_{X}$  and  $\rho$

$$
e _ {2, X}: \quad X _ {2} \times X _ {2} \longrightarrow \{\pm 1 \}, \quad e _ {\rho}: \quad \ker \rho \times \ker \rho \longrightarrow \{\pm 1 \},
$$

we have the following:

(a) $e_{2,X}(\alpha ,\beta) = 1$ , all $\alpha ,\beta \in H_0$

(b) $H_{1} = H_{0}^{\perp}$, where $H_0^\perp = \{\alpha \in X_2 | e_{2,X}(\alpha, \beta) = 1, \text{all } \beta \in H_0\}$.

(c)  $e_{\rho}(\psi\alpha,\psi\beta)=e_{2,X}(\alpha,\beta),\text{ all }\alpha,\beta\in H_{1}.$

In this case we set $Y = X \times P / H$, where

$$
H = \{(\alpha , \psi \alpha) | \alpha \in H _ {1} \}
$$

and let  $\phi$  be the composition of canonical maps:

$$
X \longrightarrow X \times P \longrightarrow Y.
$$

Moreover, if $\sigma: X \times P \longrightarrow Y$ is the canonical map, then the polarization $\lambda_{\theta_Y}$ is determined by the requirement that the diagram

$$
\begin{array}{c} X \times P \xrightarrow {2 \lambda_ {\theta_ {X}} \times \rho} \hat {X} \times \hat {P} \\ \sigma \Biggl \downarrow \\ Y \xrightarrow {\lambda_ {\theta_ {Y}}} \hat {Y} \end{array}
$$

commutes.

In other words, we find that whenever one has such a  $\phi$ , then up to a small group H of points of order two, Y and its polarization split into a product of two natural blocks, one being X and the other we call P—which in the case of curves will be the “Prym variety.” Moreover, to tie the two types of data together, I claim that:

(v)  $H_{0} = \ker \phi.$

(vi) There is an involution $\iota$ on $Y$ such that

$$
P = \operatorname{Im} (1 _ {Y} - \iota) = \ker (1 _ {Y} + \iota) ^ {0}, \quad \phi (X) = \operatorname{Im} (1 _ {Y} + \iota) = \ker (1 _ {Y} - \iota) ^ {0}.
$$

In fact, if $\psi = \lambda_{\theta_X}^{-1}\cdot \hat{\phi}\cdot \lambda_{\theta_Y}\colon Y\longrightarrow X$ , then

$\ker (1_Y - \iota) = X \times P_2 / H \cong \phi(X) \times (\mathbb{Z} / 2\mathbb{Z})^{2b - 2c}, \quad \ker \psi = X_2 \times P / H \cong P \times (\mathbb{Z} / 2\mathbb{Z})^{a - c}$ [for a,b,c see (viii)].

(vii) If $\sigma: X \times P \longrightarrow Y$ is the canonical map and $\tau: Y \longrightarrow X \times P$ is the map $\tau(x) = (\psi x, x - \iota x)$, then

$$
\sigma \cdot \tau = 2 _ {Y}, \quad \tau \cdot \sigma = 2 _ {X \times P}.
$$

(viii) If $\dim X = a$, $\dim Y = a + b$, $\# \ker \phi = 2^{a - c}$, then $\dim P = b$, $\# H_0 = 2^{a - c}$, $\# H_1 = 2^{a + c}$, $\# \ker \rho = 2^{2c}$, and $0 \leqslant c \leqslant \min(a, b)$.

Much of the verification of the equivalence here is straightforward, so we will run through only the first part.

Start with Data I. Define

$$
P = \lambda_ {\theta_ {Y}} ^ {- 1} (\ker \hat {\phi}) ^ {0},
$$

and v the number of components of  $\lambda_{\theta_{Y}}^{-1}(\ker\hat{\phi})$ . Via  $\phi$  and the inclusion of P in Y, we get  $\sigma: X \times P \longrightarrow Y$ . Let  $H = \ker \sigma$ . Note that

$$
(x, y) \in H \Longrightarrow \phi (x) + y = 0 \Longrightarrow \hat {\phi} \left(\lambda_ {\theta_ {Y}} (\phi (x))\right) = 0 \Longrightarrow 2 x = 0 \Longrightarrow 2 y = 0;
$$

hence $H \subset X_2 \times P_2$. Since $H \cap (0) \times P_2 = (0) \times (0)$, there is a subgroup $H_1 \subset X_2$ and a homomorphism $\psi: H_1 \longrightarrow P_2$ such that

$$
H = \{(\alpha , \psi \alpha) | \alpha \in H _ {1} \}.
$$

Also, if $H_0 = \ker \phi$, then $H_0 \subset H_1$, and $\psi$ factors as $H_1 / H_0 \hookrightarrow P_2$. Moreover, for all $y \in Y$, let

$$
x = \lambda_ {\theta_ {X}} ^ {- 1} (\hat {\phi} (\lambda_ {\theta_ {Y}} (y))).
$$

Then

$$
2 y = \phi (x) + (2 y - \phi (x))
$$

and

$$
\hat {\phi} (\lambda_ {\theta_ {Y}} (2 y - \phi (x))) = 2 \lambda_ {\theta_ {X}} (x) - \hat {\phi} (\lambda_ {\theta_ {Y}} (\phi (x))) = 0;
$$

hence $v \cdot (2y - \phi(x)) \in P$. Therefore

$$
2 v \cdot y \in \phi (x) + P \subset \operatorname{Im} \sigma
$$

and since Y is a divisible group, this implies that  $\sigma$  is surjective. Next, the polarization  $\lambda_{\theta_{Y}}$  of Y “pulls back” to a polarization of  $X \times P$  given by the composition:

$$
X \times P \xrightarrow {\sigma} Y \xrightarrow {\lambda_ {\theta_ {Y}}} \hat {Y} \xrightarrow {\hat {\sigma}} \hat {X} \times \hat {P},
$$

which may be considered as being given by a  $2 \times 2$  matrix

$$
\left( \begin{array}{c c} \alpha & \beta \\ \gamma & \delta \end{array} \right), \quad \begin{array}{l l} \alpha \colon & X \longrightarrow \hat {X}, \\ \gamma \colon & X \longrightarrow \hat {P}, \end{array} \quad \begin{array}{l l} \beta \colon & P \longrightarrow \hat {X}, \\ \delta \colon & P \longrightarrow \hat {P}. \end{array}
$$

Also, because any polarization is symmetric,  $\gamma = \hat{\beta}$ . But by the very definition of P, the coefficient  $\beta$  is zero. So  $\gamma = 0$ , too, and the polarization splits. Note that by assumption (2.1) on Data I,  $\alpha = 2\lambda_{\theta_{X}}$ . Define  $\rho$  to be  $\delta$ . Next, the fact that the polarization  $(2\gamma_{\theta_{X}}, \rho)$  of  $X \times P$  is a pullback of a principal polarization with respect to the isogeny  $\sigma$  is equivalent to the condition that ker  $\sigma$ , as a subgroup of ker  $(2\lambda_{\theta_{X}}, \rho)$ ,

is maximal isotropic for the skew-symmetric form of this polarization (cf. Mumford [10, Section 23]). Hence

$$
H \subset X _ {2} \times \ker \rho
$$

and if $(\alpha, \psi \alpha)$, $(\beta, \psi \beta) \in H$, then

$$
e _ {2, X} (\alpha , \beta) \cdot e _ {\rho} (\psi \alpha , \psi \beta) = 1.
$$

This means that  $\psi(H_{1}/H_{0})\subset\ker\rho$  and  $\psi$  is “symplectic” in the sense of (iv)c. Moreover, counting orders, the maximality of H implies

$$
(\# H _ {1}) ^ {2} = (\# H) ^ {2} = \# (X _ {2} \times \ker \rho);
$$

hence

$$
\# H _ {1} ^ {\perp} = \frac {\# X _ {2}}{\# H _ {1}} = \frac {\# H _ {1}}{\# \ker \rho} \leqslant \frac {\# H _ {1}}{\# \operatorname{Im} \psi} \leqslant \# H _ {0}.
$$

Since $\ker \rho \subseteq H_1^\perp$, this implies that $\psi$ maps $H_1$ onto $\ker \rho$ and that $H_0 = H_1^\perp$, hence $H_1 = H_0^\perp$. Thus we have Data II.

We leave it to the reader to check now that one can go backward from Data II to Data I and that for corresponding data, (v)-(viii) hold.

## 3. DEFINITION OF THE PRYM VARIETY

Returning to a covering $\pi: \tilde{C} \longrightarrow C$ and their Jacobians related by $\pi^*: J \longrightarrow \tilde{J}$, we see that $\tilde{J} \cong J \times P / H$. In this case there is an involution $\iota: \tilde{C} \longrightarrow \tilde{C}$ interchanging the two sheets above any point, which induces an involution $\iota: \tilde{J} \longrightarrow \tilde{J}$. Since for any divisor $\mathfrak{A}$ on $\tilde{C}$,

$$
\pi^ {- 1} (\pi \mathfrak {A}) = \mathfrak {A} + \iota (\mathfrak {A}),
$$

it follows that

$$
\pi^ {*} (\mathrm{Nm} x) = x + \iota (x), \quad \text { all } \quad x \in \tilde {J}.
$$

And since Nm is surjective, this also shows that

$$
\iota (\pi^ {*} y) = \pi^ {*} y, \quad \text {   all   } \quad y \in J.
$$

Therefore  $\iota = +1$  on  $\pi^{*}J$  and  $\iota = -1$  on ker Nm. Thus  $\iota$  is precisely the involution introduced in (vi) of Section 2, and we find that

$$
P _ {\text { def }} = (\ker \mathrm{Nm}) ^ {0} = \ker (1 _ {j} + t) ^ {0} = \operatorname{Im} (1 _ {j} - t).
$$

i.e., $P$ is the "odd" part of $\tilde{J}$, which we call the Prym variety of $\tilde{C}$ over $C$.

Let $g =$ genus of $C$ and let $2n = \#$ of branch points. Then by Hurwitz's formula

$$
\text { genus } \tilde {g} \text { of } \tilde {C} = 2 g + n - 1.
$$

Therefore

$$
\dim J = g, \quad \dim \tilde {J} = 2 g + n - 1, \quad \dim P = g + n - 1.
$$

To apply fully the theory of Section 2, we need only compute $\ker (\pi^{*})\cong \{\mathrm{div.}$ classes $\mathfrak{A}$ on $C|\pi^{-1}\mathfrak{A}\equiv 0\}$. But

$$
\pi^ {- 1} \mathfrak {A} \equiv 0 \Longrightarrow 2 \mathfrak {A} = \pi \pi^ {- 1} \mathfrak {A} \equiv 0,
$$

i.e., $\ker (\pi^{*})\subset J_{2}$. If $\mathfrak{A}$ is any such divisor class, then $\mathfrak{A}$ defines an unramified double covering $\pi_{\mathfrak{A}}\colon C_{\mathfrak{A}}\longrightarrow C$ by "Kummer theory," i.e., $C_{\mathfrak{A}}$ is the normalization of $C$ in $\mathbb{R}(C)(\sqrt{f})$, where $2\mathfrak{A} = (f)$, or

$C_{\mathfrak{A}} = \mathbf{Spec}(\mathcal{O}_C\oplus \mathcal{O}_C(\mathfrak{A}))$ , mult. given by $\mathcal{O}_C(\mathfrak{A})\times \mathcal{O}_C(\mathfrak{A})\longrightarrow \mathcal{O}_C(2\mathfrak{A})\cong \mathcal{O}_C.$

Then

$\pi^{-1}\mathfrak{A} \equiv 0 \iff$ the double covering $C_{\mathfrak{A}} \times {}_c \tilde{C}$ of $\tilde{C}$

splits into two copies of $\tilde{C}$

$\Longleftrightarrow$ there is a morphism

![](images/page_7_image_8.jpg)

and hence

$\pi^{-1}\mathfrak{A} \equiv 0, \quad \mathfrak{A} \neq 0 \iff$ there is an isomorphism $f$:

![](images/page_7_image_11.jpg)

This proves

Lemma. If $\pi$ is ramified, $\ker \pi^{*} = (0)$. If $\pi$ is unramified, hence $\tilde{C} = C_{\mathfrak{A}}$ for some $\mathfrak{A}$, then $\ker \pi^{*} = \{0, \mathfrak{A}\}$.

Combining this with the results of Section 2, we deduce the following.

Corollary 1. If $\pi$ is ramified, we get a symplectic injection $\psi: J_2 \hookrightarrow P_2$ such that

(a) $\operatorname{Im} \psi = \ker \rho$, where $\rho: P \longrightarrow \hat{P}$ is the polarization of $P$, and

(b) $\tilde{J} \cong J \times P / \{(\alpha, \psi \alpha) | \alpha \in J_2\}$.

If $\pi$ is unramified, we get subgroups

$$
\begin{array}{c c} (0) & \subset H _ {0} \subset H _ {1} \subset J _ {2} \\ & \| \quad \| \\ & \{0, \mathfrak {A} \} \quad \{\mathfrak {B} | e _ {2} (\mathfrak {A}, \mathfrak {B}) = + 1 \} \\ & \text { order } 2 \quad \text { order } 2 ^ {2 g - 1} \end{array}
$$

and a symplectic isomorphism $\psi: H_1 / H_0 \xrightarrow{\approx} P_2 = \ker \rho$ such that

$$
\tilde {J} \cong J \times P / \{(\alpha , \psi \alpha) | \alpha \in H _ {1} \}.
$$

Corollary 2. If $\pi$ is unramified or has only two branch points, then $\ker \rho = P_2$, hence $\rho = 2\lambda_{\Xi}$, where

$$
\hat {\lambda} _ {\Xi}: \quad P \stackrel {\approx} {\longrightarrow} \hat {P}
$$

is a principal polarization. Moreover, in these cases

$$
\phi (J) = \{x \in \tilde {J} | \iota x = x \}.
$$

## 11

## 4. RELATIONS BETWEEN THETA DIVISORS

The question arises: In the class of all positive divisors algebraically equivalent to  $2\theta_{X}$ , which ones arise as  $\phi^{-1}(\theta_{Y,y})$ , where  $\theta_{Y,y}=T_{y}(\theta_{Y})$  is a translate of  $\theta_{Y}$  by y and  $\phi^{-1}$  means its pullback as actual divisor, when defined? This class of divisors is the (disjoint) union of the linear systems  $|\theta_{X}+\theta_{X,x}|$ ,  $x\in X$ . In particular, one can ask whether it ever happens that

$$
\phi^ {- 1} \theta_ {Y, y} = \theta_ {X, x _ {1}} + \theta_ {X, x _ {2}}
$$

for some  $y \in Y$ ,  $x_{1}, x_{2} \in X$ . The situation seems to be that this does not occur in general, that it does occur for Jacobians, and that this special occurrence is the ultimate source of the “Schottky relations” satisfied by the theta nulls of Jacobians.

Let us see first what we can say about the situation in general. Since

$$
\phi^ {- 1} (\theta_ {Y, \phi (x)}) = \phi^ {- 1} (\theta_ {Y}) _ {x}
$$

for all $x \in X$, we may as well restrict our attention to the divisors $\phi^{-1}(\theta_{Y,y})$ for $y \in P$. All these divisors are linearly equivalent, since

[the div. class

$$
\phi^ {- 1} (\theta_ {Y, y}) - \phi^ {- 1} (\theta_ {Y}) \quad \text { in } \quad X ] = \hat {\phi} (\lambda_ {\theta_ {Y}} (y))
$$

and this is 0 if $y \in P$. Moreover, if we replace $\theta_X$ and $\theta_Y$ by suitable translates, we can then assume that $\theta_X$ and $\theta_Y$ are symmetric divisors (invariant under $-1_X$ and $-1_Y$) and that†

$$
\phi^ {- 1} (\theta_ {Y, y}) \in | 2 \theta_ {X} |, \quad \text { all } \quad y \in P.
$$

Therefore we get a morphism (we change the sign of $y$ to simplify the proposition that follows):

$$
\begin{array}{c} \delta \colon P - \{y | \phi (X) \subset \theta_ {Y, - y} \} \longrightarrow | 2 \theta_ {X} | \\ y \longmapsto \phi^ {- 1} (\theta_ {Y, - y}). \end{array}
$$

† In fact, first take any symmetric $\theta_{X}$ and $\theta_{Y}$. Then $\phi^{-1}(\theta_{Y}) = 2\theta_{X} + D$, where $2D \equiv 0$, hence $e_{*}^{\theta Y}(\phi(x)) = e_{2}(D, x)$ for all $x \in X_{2}$. This is a homomorphism from $\phi(X_{2})$ to $\{\pm 1\}$: Extend it to a homomorphism $f: Y_{2} \to \{\pm 1\}$ and represent $f$ by $f(x) = e_{2}(y, x)$, for some $y \in Y_{2}$. Then $\theta_{Y,y}$ is still symmetric and $e_{2}^{\theta Y,y}(\phi(x)) = 1$, all $x \in X_{2}$, hence $\phi^{-1}(\theta_{Y,y})$ is totally symmetric, i.e., $\in |2\theta_{X}|$.

Moreover, because the polarization  $\theta_{Y}$  on Y, pulled back to  $X \times P$ , splits into a product, it follows that we can write

$$
\sigma^ {*} (\mathcal {O} _ {Y} (\theta_ {Y})) = p _ {1} ^ {*} (\mathcal {O} _ {X} (2 \theta_ {X})) \otimes p _ {2} ^ {*} (L _ {\rho}),
$$

where  $L_{\rho}$  is a symmetric invertible sheaf on P representing the polarization  $\rho$ . I claim the following:

Proposition. $\delta$ is essentially the morphism of $P$ to projective space defined by the section of $L_{\rho}$. More precisely

$$
\{y \mid \phi (X) \subset \theta_ {Y, - y} \} = \{y \mid s (y) = 0 \quad \text { for   all } \quad s \in \Gamma (L _ {\rho}) \}
$$

—call this set $B_{\rho}$ (for base points)—and there is an isomorphism

$$
i \colon \mathbb {P} (\Gamma (L _ {\rho})) \hookrightarrow | 2 \theta_ {X} |
$$

of $\mathbb{P}(\Gamma(L_{\rho}))$ with a linear subspace of $|2\theta_X|$ such that the diagram

![](images/page_9_image_8.jpg)

commutes, where $\phi_{\rho}$ is the canonical morphism defined by sections of $L_{\rho}$.

Proof. We abbreviate  $\mathcal{O}_{X}(\theta_{X})$  to  $L_{X}$  and  $\mathcal{O}_{Y}(\theta_{Y})$  to  $L_{Y}$ . Now, according to the general theory of Mumford [9, Section 1] (see also Mumford [10, Section 23]), the isomorphism

$$
\sigma^ {*} L _ {Y} \cong p _ {1} ^ {*} L _ {X} ^ {2} \otimes p _ {2} ^ {*} L _ {\rho}
$$

defines a lifting of the group H:

$$
1 \longrightarrow \mathbb {G} _ {m} \longrightarrow \mathcal {G} (p _ {1} ^ {*} L _ {X} ^ {2} \otimes p _ {2} ^ {*} L _ {\rho}) \longrightarrow X _ {2} \times \ker \rho \longrightarrow 0
$$

and the pullback $\sigma^{*}(s_{0})$ of the unique section $s_0\in \Gamma (L_Y)$ (unique up to scalars) is the unique element of $\Gamma (L_X^2)\otimes \Gamma (L_\rho)$ fixed by $H^{*}$. But for any such $H^{*}$, it is easy to describe the element fixed by $H^{*}$: in fact

$$
\mathcal {G} (p _ {1} ^ {*} L _ {X} ^ {2} \otimes p _ {2} ^ {*} L _ {\rho}) \cong \mathcal {G} (L _ {X} ^ {2}) \times \mathcal {G} (L _ {\rho}) / \{(\lambda , \lambda^ {- 1}) | \lambda \in \mathbb {G} _ {m} \}
$$

and any such $H^{*}$ contains a subgroup $H_{0}^{*}$:

$$
\begin{array}{c} 1 \longrightarrow \mathbb {G} _ {m} \longrightarrow \mathcal {G} (L _ {X} ^ {2}) \longrightarrow X _ {2} \longrightarrow 0 \\ \underset {H _ {0} ^ {*}} {\cup} \xrightarrow {\approx} H _ {0} \end{array}
$$

Then if $Z(H_0^*)$ is the centralizer of $H_0^*$, we get a Heisenberg group:

$$
1 \longrightarrow \mathbb {G} _ {m} \longrightarrow Z (H _ {0} ^ {*}) / H _ {0} ^ {*} \longrightarrow H _ {1} / H _ {0} \longrightarrow 0
$$

and  $H^{*}$  itself is defined by an isomorphism  $\psi^{*}$ :

![](images/page_10_image_1.jpg)

by this connecting link

$$
H ^ {*} = \{(x, \psi^ {*} x) | x \in Z (H _ {0} ^ {*}) / H _ {0} ^ {*} \}.
$$

Now the subspace $\Gamma(L_X^2)^{H_0^*}$ of $H_0^*$ invariants is the unique irreducible representation of $Z(H_0^*) / H_0^*$ on which $\mathbb{G}_m$ acts identically, and the dual $\mathrm{Hom}(\Gamma(L_\rho), k)$ is the unique irreducible representation of $\mathcal{G}(L_\rho)$ on which $\mathbb{G}_m$ acts by $\lambda \longmapsto \lambda^{-1} \cdot (\text{identity})$. Therefore $\psi^*$ defines an isomorphism of these representations:

$$
\chi \colon \Gamma (L _ {X} ^ {2}) ^ {H _ {0} *} \xrightarrow {\approx} \operatorname{Hom} (\Gamma (L _ {\rho}), k).
$$

If $\beta_{1},\ldots ,\beta_{d}$ is a basis of $\Gamma (L_{\rho})$ and $\alpha_{1},\ldots ,\alpha_{d}$ is the basis of $\Gamma (L_X^2)^{H_0^*}$ such that $\chi (\alpha_i)(\beta_j) = \delta_{ij}$, then it is immediate that $\sum \alpha_{i}\otimes \beta_{i}\in \Gamma (L_{X}^{2})\otimes \Gamma (L_{\rho})$ is $H^{*}$ invariant. Thus

$$
\sigma^ {*} (s _ {0}) = \sum_ {i = 1} ^ {d} p _ {1} ^ {*} \alpha_ {i} \otimes p _ {2} ^ {*} \beta_ {i};
$$

hence for all $y \in P$

$$
\phi^ {- 1} \left(\theta_ {Y, - y}\right) = \text { zero   set   of } \quad \operatorname{res} _ {X \times \{y \}} \left(\sigma^ {*} s _ {0}\right) = \text { zero   set   of } \quad \sum_ {i = 1} ^ {d} \beta_ {i} (y) \cdot \alpha_ {i}.\tag{4.1}
$$

Thus, first of all

$$
\begin{array}{r l} \phi^ {- 1} (\theta_ {Y, - y}) = X & \Longleftrightarrow \sum \beta_ {i} (y) \cdot \alpha_ {i} \equiv 0 \Longleftrightarrow \beta_ {i} (y) = 0, \text {   all   } i \\ & \Longleftrightarrow y \text {   is   a   base   point   of   } \Gamma (L _ {\rho}), \end{array}
$$

and second if $l \in \operatorname{Hom}(\Gamma(L_{\rho}), k)$ is “homogeneous coordinates” for a point of $\mathbb{P}(\Gamma(L_{\rho}))$, then set $i(l) = \text{the divisor } (\sum l(\beta_i) \cdot \alpha_i = 0)$. Then (4.1) implies that $\delta = i \cdot \phi_{\rho}$. Q.E.D.

Now starting from the other direction,  $|2\theta_{X}|$  contains the reducible divisors  $\theta_{X,x} + \theta_{X,-x}, x \in X$ . Therefore we get a morphism:

$$
\begin{array}{l l} \phi_ {X ^ {\prime}}: & X \longrightarrow | 2 \theta_ {X} | \\ & x \longmapsto \theta_ {X, x} + \theta_ {X, - x}. \end{array}
$$

I claim the following

Proposition (Wirtinger). There is a nondegenerate inner product $B: \Gamma(L_X^2) \otimes \Gamma(L_X^2) \longrightarrow k$ (which is symmetric or skew-symmetric depending on whether $\mathrm{mult}_0 \theta_X$ is even or odd) such that if $B$ induces the isomorphism $B'$,

$$
\mathbb {P} (\Gamma (L _ {X} ^ {2})) \xrightarrow {\approx} \mathbb {P} (\Gamma (L _ {X} ^ {2}) ^ {*}) = | 2 \theta_ {X} |,
$$

then the diagram

![](images/page_11_image_1.jpg)

commutes, where  $\phi_{X}$  is the canonical morphism defined by sections of  $L_{X}^{2}$ .

Proof. In this case we use the morphism

$$
\begin{array}{c} \xi \colon X \times X \longrightarrow X \times X \\ (x, y) \longmapsto (x + y, x - y), \end{array}
$$

and the isomorphism

$$
\xi^ {*} (p _ {1} ^ {*} L _ {X} \otimes p _ {2} ^ {*} L _ {X}) \cong p _ {1} ^ {*} L _ {X} ^ {2} \otimes p _ {2} ^ {*} L _ {X} ^ {2}
$$

(cf. Mumford 9, Section 2). Let $\{s_{\alpha}\}$ be a basis of $\Gamma(L_X^2)$: Then we can write

$$
\xi^ {*} (p _ {1} ^ {*} \theta_ {X} \otimes p _ {2} ^ {*} \theta_ {X}) = \sum_ {\alpha , \beta} c _ {\alpha \beta} p _ {1} ^ {*} s _ {\alpha} \times p _ {2} ^ {*} s _ {\beta}
$$

for some matrix $c_{\alpha \beta} \in k$; or, more transparently,

$$
\theta_ {X} (u + v) \theta_ {X} (u - v) = \sum c _ {\alpha \beta} s _ {\alpha} (u) \cdot s _ {\beta} (v), \quad \forall u, v \in X.\tag{4.2}
$$

As a section of $L_X$, $\theta_X$ is even or odd depending on $\text{mult}_0 \theta_X$ and hence interchanging $u$ and $v$ in this formula, we find $c_{\alpha\beta}$ is symmetric or skew-symmetric in these two cases. Moreover, the element $\xi^*(p_1^*\theta_X \otimes p_2^*\theta_X)$ is invariant under the action of $\Delta(X_2) = \{(x,x)|x \in X_2\}$ on $p_1^*L_X^2 \otimes p_2^*L_X^2$ [via a suitable lifting of $\Delta(X_2)$ into $\mathcal{G}(p_1^*L_X^2 \otimes p_2^*L_X^2)$]. And since $X_2$ acts irreducibly on $\Gamma(L_X^2)$, this element cannot lie in any proper subspace $W_1 \otimes W_2$ of $\Gamma(L_X^2) \otimes \Gamma(L_X^2)$. This implies that $\det c_{\alpha\beta} \neq 0$, hence $c_{\alpha\beta}$ defines a form $B$. Finally, for each fixed $v$ the formula (4.2) implies

$$
u \in \operatorname{support} (\theta_ {X, v} + \theta_ {X, - v}) \Longleftrightarrow u \in \operatorname{zeros} \left(\sum c _ {\alpha \beta} s _ {\beta} (v) s _ {\alpha}\right)
$$

which gives us immediately

$$
\phi_ {X} ^ {\prime} (v) = B ^ {\prime} (\phi_ {X} (v)). \quad \mathrm{Q.E.D.}
$$

Corollary 1. In the abstract situation $(X, \theta_X), (Y, \theta_Y), \phi$, we get a diagram:

$$
\begin{array}{r l} P - B _ {\rho} & \xrightarrow {\phi_ {\rho}} \mathbb {P} (\Gamma (L _ {\rho})) \\ X & \xrightarrow {\phi_ {X}} \mathbb {P} (\Gamma (L _ {X} ^ {2})) \end{array} \begin{array}{c} i \\ | 2 \theta_ {X} |. \\ \nearrow^ {B ^ {\prime}} \approx \end{array}
$$

Then for all $y \in P - B_{\rho}$, $x \in X$

$$
\phi^ {- 1} \left(\theta_ {Y, y}\right) = \theta_ {X, x} + \theta_ {X, - x} \Longleftrightarrow i \left(\phi_ {\rho} (y)\right) = B ^ {\prime} \left(\phi_ {X} (x)\right).
$$

The most important case here is when  $\ker \rho = P_{2}$ , so that there is a theta divisor  $\theta_{P}$  on P with  $\rho = 2\lambda_{\theta_{P}}$  and  $L_{\rho} = L_{P}^{2}$ , where  $L_{P} = \mathcal{O}_{P}(\theta_{P})$ . Then Corollary 1 becomes the following.

Corollary 2. In the abstract situation $(X, \theta_X), (Y, \theta_Y), \phi$, when $\rho = 2\lambda_{\theta_P}$, we get a diagram

![](images/page_12_image_2.jpg)

and for all $y \in P$, $x \in X$

$$
\phi^ {- 1} (\theta_ {Y, y}) = \theta_ {X, x} + \theta_ {X, - x} \Longleftrightarrow i (\phi_ {P} (y)) = B ^ {\prime} (\phi_ {X} (x)).
$$

## 5. THE SPLITTING OF  $\phi^{-1}(\theta_{Y,y})$  FOR JACOBIANS

Now return to the double covering $\pi\colon\tilde{C}\longrightarrow C$. Recall the geometric meaning of the theta divisors $\Theta\subset J$, $\tilde{\Theta}\subset\tilde{J}$:

(1) Let $J_{k}$ be the variety of invertible sheaves on $C$ of degree $k$, and $\tilde{J}_{k}$ be the variety of invertible sheaves on $\tilde{C}$ of degree $k$ [so that if we choose a base point on $J_{k}$ or $\tilde{J}_{k}$, $J_{k} \cong J$ and $\tilde{J}_{k} \cong \tilde{J}$, but without such a choice $J_{k}(\tilde{J}_{k})$ is merely a principal homogeneous space over $J(\tilde{J})$]. Note that $\pi^{*}$ induces: $\pi^{*}: J_{k} \longrightarrow \tilde{J}_{2k}$ because $\deg \pi^{*}L = 2 \cdot \deg L$. Moreover, note that there is a canonical group structure on the big schemes:

$$
\coprod_ {k \in \mathbb {Z}} J _ {k} \quad \text { and } \quad \coprod_ {k \in \mathbb {Z}} \tilde {J} _ {k}.
$$

(2) Then we can find $\Theta$ canonically in $J_{g - 1}$ by

$$
\Theta = \{L \in J _ {g - 1} | \Gamma (L) \neq (0) \} \subset J _ {g - 1}
$$

and similarly

$$
\tilde {\Theta} = \{L \in \tilde {J} _ {\tilde {g} - 1} | \Gamma (L) \neq (0) \} \subset \tilde {J} _ {\tilde {g} - 1} = \tilde {J} _ {2 g + n - 2}.
$$

(3) The various translates of the theta divisors in $J$ and $\tilde{J}$ are given by $\Theta_{-y}$, and $\tilde{\Theta}_{-\tilde{y}}$ for $y \in J_{g-1}$ and $\tilde{y} \in \tilde{J}_{\tilde{g}-1}$. To ask whether $\phi^{-1}(\theta_{Y,y})$ splits in this case is therefore the same as asking for points $y \in \tilde{J}_n$ if

$$
(\pi^ {*}) ^ {- 1} (\widetilde {\Theta} _ {- y}) = \Theta_ {x _ {1}} + \Theta_ {x _ {2}}
$$

for some $x_{1}, x_{2} \in J$.

The double covering $\pi$ gives us a unique divisor class $\mathfrak{A}$ such that:

$$
2 \mathfrak {A} \equiv \sum_ {i = 1} ^ {2 n} P _ {1}, \quad P _ {i} = \text { branch   points },
$$

$$
\pi^ {- 1} \mathfrak {A} \equiv \sum_ {i = 1} ^ {2 n} Q _ {i}, \quad Q _ {i} = \pi^ {- 1} (P _ {i}).
$$

In fact, if $\mathbb{R}(\tilde{C}) = \mathbb{R}(C)(\sqrt{f})$, then $(f) = \sum_{i=1}^{2n} P_i - 2\mathfrak{A}$ on $C$ and $(\sqrt{f}) = \sum_{i=1}^{2n} Q_i - \pi^{-1}(\mathfrak{A})$ on $\tilde{C}$ for some divisor $\mathfrak{A}$. Sheaf-theoretically, if $\tilde{C} = \text{Spec}(\mathcal{O}_C \oplus L)$ as in Section 1, $L = \mathcal{O}_C(-\mathfrak{A})$. We then have the following.

Proposition. Let $x_{1}, \ldots, x_{d}$ be any $d$ closed points on $\tilde{C}$ such that $\pi x_{i} \neq \pi x_{j}$, all $i \neq j$. Then for all invertible sheaves $L$ of degree $g - 1$ on $C$

$$
\Gamma \left(\tilde {C}, \pi^ {*} L \left(\sum_ {i = 1} ^ {d} x _ {i}\right)\right) \neq (0) \Longleftrightarrow \Gamma (C, L) \neq (0) \quad \text { or } \quad \Gamma \left(C, L \left(\sum_ {i = 1} ^ {d} \pi x _ {i} - \mathfrak {A}\right)\right) \neq (0).
$$

Proof. Note that $\pi_{*}(\mathcal{O}_{\bar{c}}) = \mathcal{O}_c\oplus \mathcal{O}_c(-\mathfrak{A})$, where $\mathcal{O}_c$ is the subsheaf of functions even under the involution $\iota$, and $\mathcal{O}_c(-\mathfrak{A})$ is the subsheaf of odd functions. Therefore

$$
\pi_ {*} (\pi^ {*} L \bigl (\sum x _ {i} + \sum \imath x _ {i} \bigr)) \cong L \bigl (\sum \pi x _ {i} \bigr) \otimes \pi_ {*} \mathcal {O} _ {\tilde {C}} \cong L \bigl (\sum \pi x _ {i} \bigr) \oplus L \bigl (\sum \pi x _ {i} - \mathfrak {A} \bigr).
$$

This sheaf has subsheaves as follows:

$$
\begin{array}{c c c c} \pi_ {*} (\pi^ {*} L (\sum_ {\cup} x _ {i} + \sum \iota x _ {i})) \cong L (\sum \pi x _ {i}) \oplus L (\sum \pi x _ {i} - \mathfrak {A}) \\ \pi_ {*} (\pi^ {*} L (\sum x _ {i})) & \cup & \cup \\ \underset {\cup} {\pi_ {*}} (\pi^ {*} L) & \cong & L & \oplus & L (- \mathfrak {A}) \end{array}
$$

but the middle sheaf does not break up into even and odd pieces, because  $x_{i} \neq tx_{j}$  for any i, j. In fact at every point  $\pi x_{i}$  the middle sheaf is generated by  $L \oplus L(-\mathfrak{A})$ , plus a section  $(s_{1}, s_{2})$  with nonzero images  $\bar{s}_{1} \in L(\pi x_{i})/L$  and  $\bar{s}_{2} \in L(\pi x_{i} - \mathfrak{A})/L(-\mathfrak{A})$ . It follows that the middle sheaf fits into an exact sequence:

$$
0 \longrightarrow L \longrightarrow \pi_ {*} (\pi^ {*} L (\sum x _ {i})) \longrightarrow L (\sum \pi x _ {i} - \mathfrak {A}) \longrightarrow 0.
$$

This gives:

$$
\begin{array}{r l} 0 & \longrightarrow \Gamma (C, L) \longrightarrow \Gamma (\tilde {C}, \pi^ {*} L (\sum x _ {i})) \\ & \longrightarrow \Gamma (C, L (\sum \pi x _ {i} - \mathfrak {A})) \stackrel {\delta} {\longrightarrow} H ^ {1} (C, L) \longrightarrow \dots \end{array}
$$

which gives the implication “——” of the lemma immediately. As for “←—,” the only problem would be if

$$
\begin{array}{l} \Gamma (C, L) = (0) \\ \delta : \quad \Gamma \big (C, L (\sum_ {\text {   +   }} \pi x _ {i} - \mathfrak {A}) \big) \longrightarrow H ^ {1} (C, L) \quad \text { injective } \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad (0). \end{array}
$$

But $\deg L = g - 1$, so $\chi(L) = 0$ and this is impossible. Q.E.D.

Corollary 1. Let $x_{1}, \ldots, x_{n}$ be any $n$ closed points on $\tilde{C}$ such that $\pi x_{i} \neq \pi x_{j}$, all $i \neq j$. If

$$
y = \sum_ {i = 1} ^ {n} x _ {i} \in \tilde {J} _ {n} \quad \text { and } \quad x = \sum_ {i = 1} ^ {n} \pi x _ {i} - \mathfrak {A} \in J _ {0},
$$

$\dagger$  To simplify notation, we are identifying divisor classes of degree k with point of  $J_{k}$ , e.g., writing x for  $t(x)$ , etc.

then

$$
(\pi^ {*}) ^ {- 1} (\widetilde {\Theta} _ {- y}) = \Theta + \Theta_ {- x}.
$$

Proof. Set-theoretically, this is just a translation of the proposition. Since the divisor  $\pi^{-1}(\widetilde{\Theta}_{-y})$  is algebraically equivalent to  $2\Theta$ , there can be no multiplicities and the equality holds between divisors, too.

Note what happens if $\pi x_{i} = \pi x_{j}$ but $x_{i}\neq x_{j}$. Then

$$
L \left(\pi x _ {i}\right) \subset \pi_ {*} \left(\pi^ {*} L \left(\sum_ {i = 1} ^ {n} x _ {i}\right)\right)
$$

and since $\deg L(\pi x_i) = g$, $\Gamma(L(\pi x_i))$ is always nontrivial. Therefore in this case

$$
\pi^ {*} (J _ {g - 1}) \subset \tilde {\Theta} _ {- y}.
$$

To rephrase this corollary in a form parallel to the general description of Section 4, we must choose suitable symmetric representatives of $\Theta$ and $\tilde{\Theta}$ in $J$ and $\tilde{J}$ themselves (instead of in $J_{g-1}$ and $\tilde{J}_{2g+n-2}$). In fact, choose:

(a) Theta characteristics  $\zeta$  and  $\tilde{\zeta}$  on C and  $\tilde{C}$ , i.e., divisor classes such that  $2\zeta = K$  (the canonical class on C) and  $2\tilde{\zeta} = \tilde{K}$  (the canonical class on  $\tilde{C}$ ), and moreover such that

$$
N m \tilde {\zeta} = K + \mathfrak {A}.
$$

[To see that this is possible, let $\mathfrak{B}$ be a divisor class on $C$ such that $2\mathfrak{B} \equiv \mathfrak{A} - \sum_{i=1}^{n} P_i$ (half of the $P_i$ only). Then set $\tilde{\zeta} = \pi^{-1} (\zeta + \mathfrak{B}) + \sum_{i=1}^{n} Q_i$.]

(b) $\zeta$ and $\tilde{\zeta}$ define theta divisors $\Theta_0 = \Theta_{-\zeta}$ and $\widetilde{\Theta}_0 = \widetilde{\Theta}_{-\tilde{\zeta}}$ in $J$ and $\tilde{J}$ which are well known to be symmetric. Moreover, I claim that because of our careful choice of $\tilde{\zeta}$, $(\pi^*)^{-1}\widetilde{\Theta}_0\in |2\Theta_0|$. This follows, in fact, from the next Corollary soon to be stated.

(c) Now write $\tilde{\zeta} = \pi^{-1}\zeta +\delta$ and note that $2\delta = \sum_{i = 1}^{2n}Q_{i},\mathrm{Nm}\delta = \mathfrak{A},$ and $\deg \delta = n.$

We make the following important definition.

Definition. If  $x_{1}, \ldots, x_{n}$  are points of  $\tilde{C}$ , we wish to find elements

$$
z = \frac {1}{2} \sum_ {i = 1} ^ {n} (x _ {i} - i x _ {i}) \in P, \quad w = \frac {1}{2} \left(\sum_ {i = 1} ^ {n} \pi x _ {i} - \mathfrak {A}\right) \in J.
$$

We say that $z \in P$ and $w \in J$ are compatible solutions of the equations

$$
2 z = \sum_ {i = 1} ^ {n} (x _ {i} - \iota x), \quad 2 w = \sum_ {i = 1} ^ {n} \pi x _ {i} - \mathfrak {A}
$$

if $z + \pi^{*}w = \sum_{i=1}^{n} x_{i} - \delta$.

(Note that such a pair $z, w$ always exists: In fact $J \times P \longrightarrow \tilde{J}$ is surjective, so $\sum_{i=1}^{n} x_i - \delta$ can be written $z + \pi^*w$, where $z \in P$ and $w \in J$. Taking Nm and 1-1, it follows that 2z and 2w have the required values.)

We can now state the following result.

Corollary 2. If $x_{1}, \ldots, x_{n}$ are any points of $\tilde{C}$ such that $\pi x_{i} \neq \pi x_{j}$, all $i \neq j$, and

$$
z = \frac {1}{2} \sum_ {1} ^ {n} (x _ {i} - \iota x _ {i}), \quad w = \frac {1}{2} \left(\sum_ {1} ^ {n} \pi x _ {i} - \mathfrak {A}\right)
$$

are compatible halves in $P$ and $J$, then

$$
(\pi^ {*}) ^ {- 1} (\widetilde {\Theta}) _ {0, - z}) = \Theta_ {0, w} + \Theta_ {0, - w}.
$$

Proof. Note that

$$
\widetilde {\Theta} _ {0, - z} = (\widetilde {\Theta} _ {- \tilde {\zeta}}) _ {- \sum x _ {i} + \delta + \pi^ {*} w} = \widetilde {\Theta} _ {\pi^ {*} (w - \zeta) - \sum x _ {i}};
$$

hence

$$
\begin{array}{r l} (\pi^ {*}) ^ {- 1} (\widetilde {\Theta} _ {0, - z}) & = (\pi^ {*}) ^ {- 1} \widetilde {\Theta} _ {\pi^ {*} (w - \zeta) - \sum x _ {i}} = ((\pi^ {*}) ^ {- 1} \widetilde {\Theta} _ {- \sum x _ {i}}) _ {w - \zeta} = (\Theta + \Theta_ {\mathfrak {A} - \sum \pi x _ {i}}) _ {w - \zeta} \\ & = \Theta_ {0, w} + \Theta_ {0, w + \mathfrak {A} - \sum \pi x _ {i}} = \Theta_ {0, w} + \Theta_ {0, - w}. \quad \text { Q.E.D. } \end{array}
$$

In case there are zero or two branch points, we can (a) work out more precisely what pairs  $(z, w)$  are compatible and  $(b)$  combine the result with Corollary 2 in Section 4 to obtain the following.

Corollary 3 (Schottky–Jung). If $\tilde{C}$ is unramified over $C$, so that $2\mathfrak{A} = 0$ as divisor class, then choose a divisor class $\mathfrak{B}$ on $C$ such that $2\mathfrak{B} = \mathfrak{A}$. Choose any theta characteristic $\zeta$ on $C$ and take $\tilde{\zeta} = \pi^{-1}(\zeta + \mathfrak{B})$ as theta characteristic on $\tilde{C}$. [Note that $2\tilde{\zeta} = \pi^{-1}(2\zeta + 2\mathfrak{B}) = \pi^{-1}(K + \mathfrak{A}) = \tilde{K}$ and $\mathrm{Nm}\,\tilde{\zeta} = 2\zeta + 2\mathfrak{B} = K + \mathfrak{A}$ as required.] These define $\Theta_0 \subset J$, $\tilde{\Theta}_0 \subset \tilde{J}$ and we have the following.

(i) $(\pi^{*})^{-1}(\widetilde{\Theta}_{0}) = \Theta_{0,\mathfrak{B}} + \Theta_{0, - \mathfrak{B}}.$

(ii) If $\Xi \subset P$ is a symmetric theta divisor on the Prym $P$, we get a canonical diagram

$$
\begin{array}{r c l} P & \xrightarrow {\phi_ {P}} & \mathbb {P} (\Gamma (L _ {P} ^ {2})) \\ & & \bigcup_ {i} | 2 \Theta_ {0} | \\ J & \xrightarrow {\phi_ {J}} & \mathbb {P} (\Gamma (L _ {J} ^ {2})) \xrightarrow {\approx_ {B ^ {\prime}}} \end{array}
$$

where $\phi_{P}$ and $\phi_{J}$ are the Kummer maps defined by the linear systems $|2\Xi|$ and $|2\Theta_0|$, and $i$ and $B'$ are as in Section 4; and

$$
i (\phi_ {P} (0)) = B ^ {\prime} (\phi_ {J} (\mathfrak {B})).
$$

Corollary 4 (Fay) (see Note, p. 350). If $\tilde{C}$ has two branch points over $C$, then choosing suitable theta characteristics on $C$ and $\tilde{C}$, we get a symmetric theta divisor $\Xi$ on $P$ and a canonical diagram

$$
\begin{array}{c} P \xrightarrow {\phi_ {P}} \mathbb {P} (\Gamma (L _ {P} ^ {2})) \\ J \xrightarrow {\phi_ {J}} \mathbb {P} (\Gamma (L _ {J} ^ {2})) \end{array}
$$

where  $j = (B')^{-1} \cdot i$  is now an isomorphism. Then for every  $x \in \tilde{C}$  there are compatible halves:

$$
z = \frac {1}{2} (x - \iota x) \in P, \quad w - \frac {1}{2} (\pi x - \mathfrak {A}) \in J
$$

such that

$$
j (\phi_ {P} (z)) = \phi_ {J} (w).
$$

As mentioned in the Introduction, one would hope that these last two corollaries can be used to find strong polynomial identities for the “theta-null werte” of Jacobians. Unfortunately, whereas for the projective embedding of any principally polarized Abelian variety  $(X, \theta)$  defined by  $|4\theta|$  one knows simple identities satisfied by the image of  $0 \in X$  (namely Riemann’s identities; cf. Mumford [9, Section 3]) for the morphism defined by  $|2\theta|$  no analogous simple identities seem to be known. In classical terms, the problem is: Find identities for the set of  $2^{n}$  functions of Z

$$
f _ {a} (Z) = \theta [ _ {0} ^ {a} ] (0, Z), \quad a = [ a _ {1}, \dots , a _ {n} ], \quad a _ {i} = 0 \quad \text { or } \quad 1.
$$

$(Z \in \mathfrak{H}_{n}, \text{Siegel's upper half-space}). \text{If } n = 3, \text{ there appears to be a unique irreducible identity of order eight, which applied to } \phi_{P}(0) \text{ in Corollary 3 leads to the usual “Schottky relation” on the theta nulls of a curve C of genus 4.}$

To explain the strength of Corollary 4, for instance, it may be helpful to contrast it with the following result: If $(X, \theta_X)$ and $(Y, \theta_Y)$ are two principally polarized Abelian varieties and if $k \geqslant 4$, consider the diagram

$$
\begin{array}{c} X \xrightarrow {\phi_ {X}} \mathbb {P} (\Gamma (L _ {X} ^ {k})) \\ Y \xrightarrow {\phi_ {Y}} \mathbb {P} (\Gamma (L _ {Y} ^ {k})) \end{array}
$$

where $\phi_X$ and $\phi_Y$ are the canonical maps defined by $|k\theta_X|$ and $|k\theta_Y|$ and $j$ is an isomorphism under which the translations by $X_k$ [which extend uniquely to projective transformations on $\mathbb{P}(\Gamma(L_X^k))]$ correspond to translations by $Y_k$. (For any $X$ and $Y$ a finite number of such $j$'s always exist.) Then

$$
j (\phi_ {X} (X)) \cap \phi (Y) \neq \varnothing
$$

implies

$$
j (\phi_ {X} (X)) = \phi_ {Y} (Y);
$$

hence $X \cong Y$. In other words, distinct Abelian varieties, projectively embedded by somewhat more ample linear systems, never meet!

## III

## 6. GEOMETRIC DESCRIPTION OF SING E, UNRAMIFIED CASE

We now consider only an unramified  $\pi\colon\tilde{C}\longrightarrow C$ . Recall that in this case

(a) genus $C = \dim J = g$, genus $\tilde{C} = \dim \tilde{J} = 2g - 1$, $\dim P = g - 1$, and $\ker \rho = P_2 \cong \{0, \mathfrak{A}\}^\perp / \{0, \mathfrak{A}\}$, $\mathfrak{A} \in J_2$ defining $\pi$ (hence $P$ principally polarized).

(b) $\{x\in \tilde{J} |i x = x\} = \pi^{*}J,$ and $\{x\in \tilde{J} |Nm x = 0\} \cong P\times \mathbb{Z} / 2\mathbb{Z}$.

[Use the fact that in the notation of (i)-(viii) of Section 2, $a = g$, $b = g - 1$, and $c = g - 1$.] In fact, in a previous paper [11] we have shown by a different argument that if we look at the principal homogeneous space $\tilde{J}_{2g-2}$ instead of $\tilde{J} = \tilde{J}_0$, and at

$$
\mathrm{Nm}: \quad \tilde {J} _ {2 g - 2} \longrightarrow J _ {2 g - 2},
$$

then $\mathrm{Nm}^{-1}(K)(K\in J_{2g - 2}$ the canonical divisor class) breaks into two components $P^{+},P^{-}$ such that:

$\forall$ invertible sheaves $L_{\alpha}$ on $\tilde{C}$, corresponding to $\alpha \in \tilde{J}_{2g - 2}$,

if $\mathbf{Nm}L\cong \Omega_C^1$ , then

$$
\dim \Gamma (L _ {\alpha}) \quad \text { even } \Longleftrightarrow \alpha \in P ^ {+}, \quad \dim \Gamma (L _ {\alpha}) \quad \text { odd } \Longleftrightarrow \alpha \in P ^ {-};\tag{6.1}
$$

moreover, for some x,

$$
\dim \Gamma (L _ {\alpha}) = 0 \quad \text { and } \quad \dim \Gamma (L _ {\alpha}) = 1.
$$

Translating these back to $\tilde{J}_0$ by any $\alpha \in \mathrm{Nm}^{-1}(K)$, $P^+$ and $P^{-}$ correspond to $P$ and its nontrivial coset in $\ker \mathrm{Nm}$. Now the theta divisors of $C$ and $\tilde{C}$ live canonically in $J_{g-1}$ and $\tilde{J}_{2g-2}$ and Riemann's theorem (see Kempf [7], and Szpiro [16]) asserts

$\forall$ invertible sheaves $L_{\alpha}$ on $C$ (resp. $\tilde{C}$) corresponding to $\alpha \in J_{g-1}$ (resp. $\tilde{J}_{2-g2}$),

(6.2)

dim $\Gamma(L_{\alpha}) = \text{mult. of } \alpha \text{ on } \Theta (\text{resp. } \Theta)$.

Combining (6.1) and (6.2), we find the following result.

Proposition. (a)  $\tilde{\Theta} \supset P^{-}$ ; (b)  $\tilde{\Theta} \cdot P^{+} = 2\Xi$ , where  $\Xi \subset P^{+}$  is a canonical representative of the theta divisor on P.

Proof. In fact

$$
\alpha \in P ^ {-} \Longrightarrow \dim \Gamma (L _ {\alpha}) \quad \text { odd } \quad \Longrightarrow \dim \Gamma (L _ {\alpha}) \geqslant 1 \quad \Longrightarrow \alpha \in \widetilde {\Theta}
$$

and

$$
\begin{array}{r l} \alpha \in \widetilde {\Theta} \cap P ^ {+} & \Longrightarrow \dim \Gamma (L _ {\alpha}) \quad \text { even   and   positive } \Longrightarrow \dim \Gamma (L _ {\alpha}) \geqslant 2 \\ & \Longrightarrow \alpha \quad \text { singular   on } \quad \widetilde {\Theta}; \end{array}
$$

hence $\tilde{\Theta} \cdot P^{+}$ consists entirely in multiple components. But the principal polarization on $\tilde{J}$ restricts to twice that on $P$, so $\Theta \cdot P^{+}$ is in the algebraic equivalence class $2\Xi$. It is easy to check that such a divisor can never have a component of multiplicity $\geqslant 3$ (or else the morphism it defines would not collapse an involution $x \longrightarrow x_{0} - x$). Thus $\Theta \cdot P^{+} = 2D$, $D$ algebraically equivalent to $\Xi$, hence equal to it after a suitable translation. Q.E.D.

Corollary.

Sing $\Xi = \{x\in P^{+}|$ mult. at $x$ of $\tilde{\Theta}\geqslant 4\}$

$$
\cup \left\{x \in P ^ {+} \left| \begin{array}{c c c c} \text { mult.   at } & x & \text { of } & \tilde {\Theta} = 2, \\ & & & T _ {x, P ^ {+}} \subset (\text { tangent   cone   to } & \Theta & \text { at } & x) \end{array} \right. \right\}.
$$

In order to apply this corollary, we must know how to compute the tangent cone to  $\tilde{\Theta}$ . In general, suppose J is any Jacobian and  $\Theta \subset J_{g-1}$ . If  $L_{\alpha}$  on C corresponds to the point  $\alpha \in J_{g-1}$ , then not only is

$$
\dim \Gamma (L _ {\alpha}) = \text { mult.   at } \quad \alpha \quad \text { of } \quad \Theta ,
$$

but if $k = \dim \Gamma(L_{\alpha}), s_1, \ldots, s_k$ is the basis of $\Gamma(L_{\alpha}), t_1, \ldots, t_k$ is the basis of $\Gamma(\Omega \otimes L_{\alpha}^{-1})$, and $s_i \otimes t_j \in \Gamma(\Omega)$ defines the differential $\omega_{ij}$ at $\alpha \in J_{g-1}$, then identifying $\Gamma(\Omega)$ to

the cotangent space $m_{\alpha} / m_{\alpha}^2$ of $J_{g-1}$ at $\alpha$, Kempf [7] proves that $\det(\omega_{ij}) = 0$ is the tangent cone to $\Theta$ at $\alpha$.

Now if $L_{\alpha}$ is a sheaf on $\tilde{C}$ such that $\mathrm{Nm} L_{\alpha} \cong \Omega_C$, then

$$
L _ {\alpha} \otimes \iota^ {*} L _ {\alpha} = \pi^ {*} \mathrm{Nm} L _ {\alpha} \cong \pi^ {*} \Omega_ {C} \cong \Omega_ {\tilde {C}};
$$

hence choosing such an isomorphism  $\phi$ , we may use the pairing

$$
\begin{array}{r l} \langle , \rangle : & \Gamma (L _ {\alpha}) \otimes \Gamma (L _ {\alpha}) \longrightarrow \Gamma (\Omega_ {\bar {c}}) \\ & (s, t) \longmapsto \phi (s \otimes i ^ {*} t) = \langle s, t \rangle \end{array}
$$

instead of

$$
\Gamma (L _ {\alpha}) \otimes \Gamma (\Omega_ {\bar {C}} \otimes L _ {\alpha} ^ {- 1}) \xrightarrow {\otimes} \Gamma (\Omega_ {\bar {C}}).
$$

Now $i$ induces $i^{*}\colon \Gamma (\Omega_{\bar{c}})\longrightarrow \Gamma (\Omega_{\bar{c}})$, too: In fact, this is just the automorphism found by decomposing

$$
\begin{array}{c} \Gamma (\Omega_ {\bar {C}}) \cong \Gamma (\pi^ {*} \Omega_ {C}) \cong \Gamma (\pi_ {*} \pi^ {*} \Omega_ {C}) \\ \subset \Gamma (\Omega_ {C}) + \Gamma (\Omega_ {C} (\mathfrak {A})) \\ \| \\ \text {the ``Prym   differentials''} \end{array}
$$

and letting $\iota^{*} = +1$ on $\Gamma (\Omega_c)$, $\iota^{*} = -1$ on $\Gamma (\Omega_c(\mathfrak{A}))$. It is easy to check that

$$
\iota^ {*} (\langle s, t \rangle) = \langle t, s \rangle ;
$$

hence the above pairing splits into two pairings:

$$
\operatorname{Symm} ^ {2} \Gamma (L _ {\alpha}) \longrightarrow \Gamma (\Omega_ {C}), \quad \Lambda^ {2} \Gamma (L _ {\alpha}) \longrightarrow \Gamma (\Omega_ {C} (\mathfrak {A})).
$$

Moreover, in the identification $\Gamma(\Omega_C) + \Gamma(\Omega_C(\mathfrak{A})) \cong \Gamma(\Omega_{\tilde{C}}) \cong$ cotangent space $T_{\alpha, \tilde{J}_{2g-2}}^*$, clearly the even and odd subspaces under $\iota^*$ go over as follows: $\Gamma(\Omega_C) \cong$ cotangent space at $\alpha$ to the coset $\alpha + \pi^*(J_{2g-2})$, and $\Gamma(\Omega_C(\mathfrak{A})) \cong$ cotangent space at $\alpha$ to $P^\pm$.

Taking a basis $s_1, \ldots, s_k$ of $\Gamma(L_\alpha)$, let $\omega_{ij} = \langle s_i, s_j \rangle$. Then $\iota^* \omega_{ij} = \omega_{ji}$, hence decomposing $\omega_{ij}$.

$$
\omega_ {i j} = \omega_ {i j} ^ {+} + \omega_ {i j} ^ {-}, \qquad \omega_ {i j} ^ {+} \in \Gamma (\Omega_ {C}), \qquad \omega_ {i j} ^ {-} \in \Gamma (\Omega_ {C} (\mathfrak {A})),
$$

It follows that $\omega_{ij}^{+}$ is symmetric and $\omega_{ij}^{-}$ is skew-symmetric. Therefore if $\alpha \in P^{+}$, $\det (\omega_{ij}) = 0$ is the tangent cone to $\widetilde{\Theta}$ at $\alpha$, and $\det (\omega_{ij}^{-}) = 0$ is the tangent cone to $\widetilde{\Theta} \cdot P^{+}$ at $\alpha$. But $\det (\omega_{ij}^{-}) = Pf(\omega_{ij}^{-})^{2}$ ($Pf = Pfaffian$), so that $Pf(\omega_{ij}^{-}) = 0$ is the tangent cone to $\Xi$ at $\alpha$ (unless it vanishes identically).

We use this to establish the following result.

Proposition. If $\mathbf{Nm}L_{\alpha} = \Omega_C$ and $\dim \Gamma (L_{\alpha}) = 2$, then

$T_{\alpha, P^{+}} \subset \text{tangent cone to} \tilde{\Theta}$ at $\alpha \Longleftrightarrow L_{\alpha} \cong \pi^{*}(\mathfrak{A})(\sum x_{i})$ for some points $x_{i} \in \tilde{C}$.

and a sheaf $M$ on $C$ such that $\dim \Gamma(M) = 2$.

Proof. Let $s, t$ be a basis of $\Gamma(L_{\alpha})$. In the proceeding notation

$$
(\omega_ {i j} ^ {-}) = \left( \begin{array}{c c} 0 & \langle s, t \rangle - \langle t, s \rangle \\ \langle t, s \rangle - \langle s, t \rangle & 0 \end{array} \right).
$$

So the linear form $\langle s, t \rangle - \langle t, s \rangle$ is the tangent cone to $\Xi$ unless $\alpha \in \operatorname{Sing} \Xi$. Thus

$$
\begin{array}{r l} T _ {\alpha , P ^ {+}} \subset \text { tangent   cone   to } & \tilde {\Theta} \quad \text { at } \quad \alpha \Longleftrightarrow \langle s, t \rangle = \langle t, s \rangle \\ & \Longleftrightarrow s \otimes i ^ {*} t = t \otimes i ^ {*} s \Longleftrightarrow i ^ {*} (s / t) = s / t \\ & \Longleftrightarrow s / t \in \mathbb {R} (C). \end{array}
$$

In classical language,  $s/t \in \mathbb{R}(C)$  says “the pencil defined by  $L_{\alpha}$  is pulled back from a pencil on C.” In modern language, let  $\sum x_{i}$  be the base points of  $\Gamma(L_{\alpha})$ , let B be the poles of s/t on C, and let  $M = \mathcal{O}_{C}(\mathfrak{B})$ . Then  $L_{\alpha} \cong \pi^{*} M (\sum x_{i})$  and 1,  $s/t \in \Gamma(M)$ ; hence  $\dim \Gamma(M) \geqslant 2$ . Clearly  $\dim \Gamma(M) = 2$  since  $\dim \Gamma(L_{\alpha}) = 2$ . Q.E.D.

## 7. DIM SING Ξ

Notations are as in Section 6. Recall that if C is a curve, a theta characteristic of C is a sheaf such that  $L^{2} \cong \Omega_{C}$ ; L is even or odd if  $\dim \Gamma(L)$  is even or odd. We wish to prove the following theorem.

Theorem.

(a) $C$ hyperelliptic $\Longrightarrow (P, \Xi)$ is a hyperelliptic Jacobian (hence dim Sing $\Xi = g - 4$) or a product of two such (hence dim Sing $\Xi = g - 3$).

(b) $g = 3, C$ not hyperelliptic $\Longrightarrow (P, \Xi)$ is a two-dimensional Jacobian.

(c) $g = 4$, $C$ not hyperelliptic $\Longrightarrow (P, \Xi)$ is a three-dimensional Jacobian, and $\Xi$ is singular iff $P$ is a hyperelliptic Jacobian iff $\exists$ is an even theta characteristic $L$ with $\Gamma(L) \neq (0)$ and $L(\mathfrak{A})$ even.

(d) Assuming $C$ not hyperelliptic and $g \geqslant 5$, then $\dim \operatorname{Sing} \Xi \leqslant g - 5$ and

$$
\dim \operatorname{Sing} \Xi = g - 5 \Longrightarrow \left\{ \begin{array}{l l} C & \text { trigonal, } \\ \text { or } & C \text { double   cover   of   an   elliptic   curve, } \\ \text { or } & g = 5 \quad \text { and } \exists \text { even   theta   characteristic } L \text { with } \\ \Gamma (L) \neq (0) & \text { and } L (\mathfrak {A}) \text { even, } \\ \text { or } & g = 6 \text { and } \exists \text { odd   theta   characteristic } L \text { with } \\ \dim \Gamma (L) \geqslant 3, & \text { and } L (\mathfrak {A}) \text { even. } \end{array} \right.
$$

In fact, in part (d), “$\Longleftarrow$” apparently also holds, but we will omit the proof of this. We first want to point out the following corollary.

Corollary. If  $g \geqslant 5$  and C is neither trigonal, a double cover of an elliptic curve, nor of the preceding two special types of genus 5 or 6, then the polarized Abelian variety  $(P, \Xi)$  is not a Jacobian or a product of Jacobians.

This follows from the theorem and the fact that  $\dim\operatorname{Sing}\Theta\geqslant\dim J-4$  for polarized Jacobians  $(J,\Theta)$  [1]. It would be quite interesting to find out in the special cases exactly which  $(P,\Xi)$  is a Jacobian.

Proof of Theorem. As shown in the previous section, the singularities of $\Xi$ canonically embedded in $P^{+}$ arise from two sources.

Case 1: sheaves $L_{\alpha}$ such that $\mathrm{Nm}L_{\alpha} = \Omega_C$, $\dim \Gamma(L_{\alpha}) \geqslant 2$ and even, and $L_{\alpha} = \pi^{*}M(\sum x_{i})$, where $\dim \Gamma(M) \geqslant 2$.

Case 2: sheaves $L_{\alpha}$ such that $\mathrm{Nm}L_{\alpha} = \Omega_C$, $\dim \Gamma(L_{\alpha}) \geqslant 4$ and even. Note that in case 1

$$
\Omega_ {C} = \mathrm{Nm} L _ {\alpha} = \mathrm{Nm} (\pi^ {*} M (\sum x _ {i}) (= M ^ {2} (\sum \pi x _ {i}),
$$

so $M$ satisfies the two conditions: (a) $\dim \Gamma(M) \geqslant 2$ and (b) $\dim \Gamma(\Omega_C \otimes M^{-2}) \geqslant 1$. Also, if there are no $x_i$, i.e., $L_\alpha = \pi^* M$, then $\dim \Gamma(L_\alpha)$ even implies (c) If $\Omega_C \cong M^2$, $\dim \Gamma(M) + \dim \Gamma(M \otimes \mathfrak{A})$ even.

Conversely, if $M$ satisfies (a)-(c), choose an effective divisor $\sum \pi x_{i}$ in the linear system $\Gamma(\Omega_C \otimes M^{-2})$ and set $L_{\alpha} = \pi^{*}M\big(\sum x_{i}\big)$. This falls in case 1 unless there is at least one $x_{i}$ and $\dim \Gamma(L_{\alpha})$ odd. But as shown in a previous work [11, p. 187], we can then replace one $x_{i}$ by $\iota(x_{i})$ to make $\dim \Gamma(L_{\alpha})$ even. So all $M$ satisfying (a)-(c) define $L_{\alpha}$ in case 1.

It is not so easy to construct all the $L_{\alpha}$ in case 2 directly from sheaves on $C$. However, I claim the following.

Lemma. If dim Sing $\Xi \geqslant g - 5$, then almost all $\alpha \in$ Sing $\Xi$ correspond to sheaves $L_{\alpha}$ in case 1.

Proof. Suppose $Z \subset \operatorname{Sing} \Xi$ were a component of dimension $\geqslant (g - 5)$ such that

$$
\dim \Gamma (L _ {\alpha}) \geqslant 4, \quad \text { all } \quad \alpha \in Z.
$$

According to previous results [11, pp. 186–188],  $\dim \Gamma(L_{\alpha}) = 4$  for almost all  $\alpha \in Z$ . Let  $Z_{0} \subset Z$  be the open subset where  $\dim \Gamma(L_{\alpha}) = 4$ . We wish to apply the following quite general result.

Proposition. Let C be any curve,  $Z \subset J_{d}$  a subvariety,  $Z_{0} \subset Z$  an open set, and assume that for some k

$$
\dim \Gamma (L _ {\alpha}) = k, \quad \text { all } \quad \alpha \in Z _ {0}.
$$

Then identifying $T_{\alpha, J_{\alpha}}$ to $H^{1}(\mathcal{O}_{C})$, hence to the dual of $\Gamma(\Omega_{C})$, I claim

$$
\operatorname{Im} \left[ \Gamma \left(L _ {\alpha}\right) \otimes \Gamma \left(\Omega_ {C} \otimes L _ {\alpha} ^ {- 1}\right) \longrightarrow \Gamma \left(\Omega_ {C}\right) \right] ^ {\perp} \supset T _ {\alpha , Z}
$$

for all $\alpha \in Z_0$.

This is proved for $k = 2$ in Lemma 2.5 of Saint-Donat [14] but the proof extends verbatim to all $k$. Applying this to our case, let

$$
W _ {\alpha} = \operatorname{Im} [ \Lambda^ {2} \Gamma (L _ {\alpha}) \longrightarrow \Gamma (\Omega_ {C} \otimes \mathfrak {A}) ].
$$

Identifying $\Gamma(\Omega_C \otimes \mathfrak{A})$ with $T_{\alpha, P^+}^*$, we find $T_{\alpha, Z} \subset W_{\alpha}^\perp$. Since the codimension of $Z$ in $P^+$ is $\leqslant 4$, it follows that $\dim W_{\alpha} \leqslant 4$. But $\dim \Lambda^2\Gamma(L_{\alpha}) = 6$, so the kernel of $\Lambda^2\Gamma(L_{\alpha}) \longrightarrow \Gamma(\Omega_C \otimes \mathfrak{A})$ has dimension at least two. Now the set of decomposable 2-forms $s \wedge t$ in $\Lambda^2\Gamma(L_{\alpha})$ forms a cone in $\Lambda^2\Gamma(L_{\alpha})$ of codimension one, so at least one such $s \wedge t$ lies in the kernel. But for any $s, t$ we find

$$
\begin{array}{r l} s \wedge t = 0 & \Longleftrightarrow \langle s, t \rangle = \langle t, s \rangle \\ & \Longleftrightarrow s / t \in \mathbb {R} (C) \quad (\text { as   before }). \end{array}
$$

Therefore, exactly as in the last section, $L_{\alpha} \cong \pi^{*} M(\sum x_{i})$ where $\dim \Gamma(M) \geqslant 2$. Q.E.D.

We are now ready to prove the theorem—or rather reduce it to a strengthened form of a theorem of Martens which is given in the appendix. First of all, say C is hyperelliptic: Let  $p: C \longrightarrow P^{1}$  be the double covering and let  $\{z_{1}, \ldots, z_{2g+2}\}$  be the branch points. It is well known that all unramified double coverings  $\pi: \tilde{C} \longrightarrow C$  arise as follows.

(a) Separate the $z_{i}$ into two groups of even cardinality:

$$
\{1, 2, \dots , 2 g + 2 \} = I ^ {\prime} \cup I ^ {\prime \prime}, \quad I ^ {\prime} = 2 h + 2, \quad I ^ {\prime \prime} = 2 k + 2.
$$

$I^{\prime}\cap I^{\prime \prime} = \phi ;$ hence $h + k + 1 = g$

(b) Let $p': C' \longrightarrow \mathbb{P}^1$ and $p'': C'' \longrightarrow \mathbb{P}^1$ be the hyperelliptic curves with branch points $\{z_i\}_{I'}$ and $\{z_i\}_{I''}$, respectively.

(c) Let $\tilde{C}$ be the normalization of $C \times_{\mathbb{P}^1} C'$. The $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ acts on $\tilde{C}$ and we get a tower of curves:

![](images/page_21_image_6.jpg)

by dividing by its three subgroups of order two. Note that $\tilde{C} = \text{norm. of } C \times_{\mathbb{P}^1} C'' = C' \times_{\mathbb{P}^1} C''$. I claim that in this situation

$$
\begin{array}{c} \operatorname{Prym} (\tilde {C} / C) \cong J ^ {\prime} \times J ^ {\prime \prime} \\ \Xi \longleftrightarrow J ^ {\prime} \times \Theta^ {\prime \prime} + \Theta^ {\prime} \times J ^ {\prime \prime}, \end{array}
$$

where  $J'$  and  $J''$  are the Jacobians of  $C'$  and  $C''$ . (Note that if h or k is zero, one of the factors here disappears.)

Idea of Proof: Now we have $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ acting on $\tilde{J}$ and up to 2-isogenies, $\tilde{J}$ splits into four “eigensubvarieties”; the part invariant under the whole group will be empty, and the other three pieces will be $\pi^{*}J$, $J'$, and $J''$. One checks that $J' \times J''$ injects into $\tilde{J}$ by the natural map $(\pi')^{*} \times (\pi'')^{*}$, and that the image is $P$. Finally, one checks that the $\tilde{\Theta}$ polarization on $\tilde{J}$ splits into the sum of $2\Theta$, $2\Theta'$, and $2\Theta''$ on the three pieces; hence $\Xi$ splits into the sum of $\Theta'$ and $\Theta''$. The details are left to the reader.

Now suppose $C$ is not hyperelliptic and that $\dim \operatorname{Sing} \Xi = v \geqslant g - 5$. Almost all of these singular points must define sheaves $L_{\alpha}$ in case 1: It follows that for some $d$ there is a $v$-dimensional family of pairs $\{M, \sum_{i=1}^{e} y_i\}$ where (i) $M$ is an invertible sheaf on $C$; (ii) $\sum y_i$ is an effective divisor of degree $e$; (iii) $\deg M = d$ and $2d + e = 2g - 2$; (iv) $\dim \Gamma(M) \geqslant 2$; (v) $M^2\left(\sum_{i=1}^{e} y_i\right) \cong \Omega_C$; and (vi) if $e = 0$, then $\dim \Gamma(M) + \dim \Gamma(M \otimes \mathfrak{A})$ even.

Now for each $M$ the set of all divisors $\sum y_{i}$ of this type is a projective space whose dimension equals $\dim \Gamma (\Omega_c\otimes M^{-2}) - 1$. By Clifford's theorem, we can bound this by

$$
\dim \Gamma (\Omega_ {C} \otimes M ^ {- 2}) - 1 <   \frac {1}{2} \deg \Omega_ {C} \otimes M ^ {- 2} = g - 1 - d.
$$

If $d < g - 1$, by Marten's theorem (see appendix), the dimension of the set of $M_s$ of degree $d$ with $\dim \Gamma(M) \geqslant 2$ is bounded by $d - 3$, and if $C$ is not trigonal, a double cover of an elliptic curve, or a nonsingular quintic, then it is bounded by $d - 4$. Therefore

$$
v = (\text { dim.   of   possible } M s) + (\text { dim.   of   possible } \sum y _ {i}) <   g - 4
$$

and $v < g - 5$, except in the aforementioned special cases. Also, if $d = g - 1$, then $M^2 \cong \Omega_C$, i.e., $M$ is one of the finite set of theta characteristics: if $g \leqslant 5$, these can give us a $(\geqslant g - 5)$-dimensional singular locus on $\Xi$.

Finally, let us look at the low-genus cases: If g = 3, the only singularities on  $\Xi$  arise from theta characteristics M. But if C is not hyperelliptic, dim  $\Gamma(M) = 0$  or 1 for all M, so  $\Xi$  is nonsingular. Thus  $(P, \Xi)$  is a principally polarized two-dimensional Abelian variety with  $\Xi$  nonsingular: Hence it is a Jacobian. If g = 4 and C is not hyperelliptic, again singularities on  $\Xi$  can arise only from theta characteristics. In fact, in  $P^{3}$  the canonical model of C equals F.G, with F a quadric, C a cubic. And if F is nonsingular, again dim  $\Gamma(M) = 0$  or 1 for all theta characteristics M. But if F is a cone, there is one even M with dim  $\Gamma(M) = 2$ —namely the M defined by the divisors C.(line on F). If also dim  $\Gamma(M \otimes \mathfrak{A})$  equals zero rather than one, then Sing  $\Xi$  has a single point. Thus  $(P, \Xi)$  is a principally polarized three dimensional Abelian variety with zero or one singularity on  $\Xi$. Now either from the fact that the moduli space over Z of such varieties is irreducible six dimensional, hence Jacobians are dense in it, hence by Hoyt [6] every such variety is a Jacobian or product of Jacobians; or from Harris' thesis [5], it follows that  $(P, \Xi)$  is a Jacobian. Since a three dimensional Jacobian  $(J, \Theta)$  has a singular  $\Theta$  if and only if J comes from a hyperelliptic curve, this proves (c). As for (d), we have proved this already modulo noting that nonsingular quintics are precisely the nonhyperelliptic curves of genus six with sheaves N such that

$$
N ^ {2} \cong \Omega_ {C}, \quad \dim \Gamma (M) = 3.
$$

[i.e., $N = \mathcal{O}_C(1)$]. This $N$ defines sheaves $M$ by $M = N(-z)$, $z \in C$, hence potential singularities of $\Xi$ by

$$
L _ {\alpha} = \pi^ {*} (N (- z)) (x _ {1} + x _ {2}).
$$

Then $x_{1}$ and $x_{2}$ must satisfy

$$
\Omega_ {C} \cong N ^ {2} (- 2 z) (\pi x _ {1} + \pi x _ {2});
$$

hence $\pi x_{1} = \pi x_{2} = z$. Therefore

$$
L _ {\alpha} = \pi^ {*} N (x - i x) \quad \text { or } \quad L _ {\alpha} = \pi^ {*} N.
$$

But one of these will be in  $P^{+}$ , the other in  $P^{-}$ , hence  $\Xi$  will either have a whole curve of singularities parametrized by x, or exactly one singularity, and in fact

$$
\dim \operatorname{Sing} \Xi = 1 \Longleftrightarrow \pi^ {*} N (x - \iota x) \in P ^ {+} \Longleftrightarrow \pi^ {*} N \in P ^ {-}
$$

$$
\Longleftrightarrow \dim \Gamma (N) + \dim \Gamma (N \otimes \mathfrak {A}) \quad \text { odd } \quad \Longleftrightarrow \dim \Gamma (N \otimes \mathfrak {A}) \quad \text { even. } \quad \text { Q.E.D. }
$$

Precisely this final special case has turned out recently to be surprisingly interesting. The reason is that the Pryms $(P, \Xi)$ arising from quintics $C \subset \mathbb{P}^2$ and double coverings

$\tilde{C} = \text{Spec}(\mathcal{O}_C + \mathcal{O}_C(\mathfrak{A}))$ for which $\dim \Gamma(\mathcal{O}_C(1)(\mathfrak{A}))$ is odd include the intermediate Jacobians of cubic hypersurfaces in $P^4$: By the corollary, these are not Jacobians and their $\Xi$ has one singular point at which the tangent cone is in fact exactly the cubic hypersurface! Clemens and Griffiths [2] have given another proof that this intermediate Jacobian is not a Jacobian and have deduced from this that the cubic hypersurface is not rational. On the other hand, Clemens conjectures that when $\dim \Gamma(\mathcal{O}_C(1)(\mathfrak{A}))$ is even, then $(P, \Xi)$ is a Jacobian.

## APPENDIX: A THEOREM OF MARTENS

The purpose of this appendix is to somewhat strengthen Marten's theorem [8, Theorem 1] (see also Saint-Donat [14, Theorem 2.4]) as follows.

Theorem. If C is a nonsingular curve of genus g, and  $W_{d} \subset J_{d}, 1 \leqslant d \leqslant g - 1$ , is the locus of invertible sheaves of degree d with sections, then

$\exists d, 2 \leqslant d \leqslant g - 2,$ such that $\dim \operatorname{Sing} W_d \geqslant g - 3$

$\Longleftrightarrow C$ is (a) hyperelliptic, or (b) trigonal, or

(c) double cover of an elliptic curve, or

(d) nonsingular plane quintic.

Proof. Recall that by Kempf's results [7,16]

Sing $W_{d} = (\text{locus of inv. sheaves } L, \dim \Gamma(L) \geqslant 2)$;

hence, in Marten's notations, Sing $W_{d} = G_{d}^{1}$. Thus he shows that

$\exists d, 2 \leqslant d \leqslant g - 2, \dim \operatorname{Sing} W_d \geqslant d - 2 \Longleftrightarrow C$ hyperelliptic.

Excluding this case, we assume dim Sing $W_{d} = d - 3$ for some $d$. If $d = 3$,

$$
\begin{array}{r l} \text { Sing } W _ {3} \neq \phi & \Longleftrightarrow \exists L \quad \text { of   degree   three, } \quad \dim \Gamma (L) \geqslant 2 \\ & \Longleftrightarrow C \quad \text { trigonal. } \end{array}
$$

Excluding this case, we may assume  $d \geqslant 4$  (hence  $g \geqslant 6$ ) and C not trigonal. Consider a general L of degree d with  $\dim \Gamma(L) = 2$  and look at the pairing

$$
\underbrace {\Gamma (L)} _ {\dim 2} \otimes \underbrace {\Gamma (\Omega \otimes L ^ {- 1})} _ {\dim (g - d + 1)} \xrightarrow {\phi} \Gamma (\Omega).
$$

If $d$ is the smallest $d$ for which $\dim \operatorname{Sing} W_d = d - 3$, we can assume that $\Gamma(L)$ is basepoint free. Let $\alpha, \beta \in \Gamma(L)$ be a basis. Now according to Kempf's results, the pairing $\phi$ allows us to compute the Zariski tangent space to $\operatorname{Sing} W_d$ at any point $L \in \operatorname{Sing} W_d$ such that $\dim \Gamma(L) = 2$: namely, identify

$$
T _ {L, \text { Sing } W _ {d}} \subset T _ {L, J _ {d}} \cong T _ {0, J} \cong H ^ {1} (\mathcal {O} _ {C}) \cong \text { dual   of } \quad \Gamma (\Omega).
$$

Then he shows that

$$
\operatorname{Im} \phi = (T _ {L, \text { Sing } W _ {d}}) ^ {\perp}.
$$

Therefore

$$
\dim (\operatorname{Im} \phi) \leqslant g - d + 3.
$$

But since $\alpha$ and $\beta$ have no common zeros, we get an exact sequence:

$$
\begin{array}{c} 0 \longrightarrow \alpha \otimes \beta \otimes \Gamma (\Omega \otimes L ^ {- 2}) \longrightarrow \alpha \otimes \Gamma (\Omega \otimes L ^ {- 1}) + \beta \otimes \Gamma (\Omega \otimes L ^ {- 1}) \\ \longrightarrow \operatorname{Im} \phi \longrightarrow 0; \end{array}\tag{A.1}
$$

hence

$$
\dim \operatorname{Im} \phi = 2 (g - d + 1) - \dim \Gamma (\Omega \otimes L ^ {- 2}) = g + 3 - \dim \Gamma (L ^ {2}).
$$

Therefore $\dim \Gamma(L^2) \geqslant d$. In other words, the $L^2$s define a $(d-3)$-dimensional subset of $W_{2d}$ of points corresponding to $M$s with $\dim \Gamma(M) \geqslant d$: In Martens's notation,

$$
\dim G _ {2 d} ^ {d - 1} \geqslant d - 3.
$$

Applying his Theorem 1 again, the only cases where this might happen are: (i) $d = 4$, dim Sing $W_{4} = 1$, or (ii) $d = 5$, $g = 7$, dim Sing $W_{5} = 2$.

If (i) happens, fix one $L_0$ of degree four, $\dim \Gamma(L_0) = 2$, $\Gamma(L_0)$ base-point free, and let $L$ be any other. Note that $\dim \Gamma(L_0 \otimes L) = 4$ in all cases where $L \not\approx L_0$ [e.g., by computing $\Gamma(L_0 \otimes L)$ by an exact sequence like (A.1)]. Therefore by Riemann-Roch,

$$
\dim \Gamma (\Omega \otimes L _ {0} ^ {- 1}) = \dim \Gamma (L _ {0}) + 2 g - 6 - g + 1 = g - 3
$$

$$
\dim \Gamma (\Omega \otimes L _ {0} ^ {- 1} \otimes L ^ {- 1}) = \dim \Gamma (L _ {0} \otimes L) + 2 g - 1 0 - g + 1 = g - 5.
$$

Let $P_{1},\ldots ,P_{g - 6}$ be any $g - 6$ points on $C$ in general position. Then

$$
\Gamma \left(\Omega \otimes L _ {0} ^ {- 1} \otimes L ^ {- 1} \left(- \sum_ {i = 1} ^ {g - 6} P _ {i}\right)\right) \neq (0),
$$

hence if $s_L$ is a section here, and $M = \Omega \otimes L_0^{-1} \left( -\sum_{i=1}^{g-6} P_i \right)$, we find

$$
s _ {L} \otimes \Gamma (L) \subseteq \Gamma (M)
$$

for all $L$. Note that

$$
\dim \Gamma (M) = \dim \Gamma (\Omega \otimes L _ {0} ^ {- 1}) - (g - 6) = 3.
$$

Therefore $\Gamma(M)$ defines a rational map $\pi\colon C\longrightarrow\mathbb{P}^{2}$ such that every base-point-free pencil $\Gamma(L)$ of degree four defines a map $C\longrightarrow\mathbb{P}^{1}$ which is the composition of $\pi$ and a projection of $\pi(C)$ to $\mathbb{P}^{1}$. But if $d=\text{degree}(\pi(C))$, then projecting $\pi(C)$ from a point of $\mathbb{P}^{2}-\pi(C)$, or from a simple point of $\pi(C)$, gives a map of degree $d$, or $d-1$, from $\pi(C)$ to $\mathbb{P}^{1}$. Since $\pi(C)$ has only finitely many multiple points and there are supposed to be an infinite number of $Ls$, we conclude that either $\pi$ birational and $d\leqslant5$ or $\pi$ of degree two, $d\leqslant3$. Since $g\geqslant6$, $C$ is either a nonsingular plane quintic or a double covering of an elliptic curve. Both of these do have an infinite Sing $W_{4}$, i.e., take the line bundles $[\mathcal{O}_{C}\otimes\mathcal{O}_{\mathbb{P}^{2}}(1)](-P)$, any $P\in C$, in the first case, or $\pi^{*}L$, any $L$ of degree two on the elliptic curve, in the second case.

Finally, we want to exclude (ii). Assume we have a two-dimensional family of $Ls$ such that

$$
\deg L = 5, \quad \dim \Gamma (L) = 2, \quad \dim \Gamma (L ^ {2}) = 5.
$$

By Riemann–Roch,  $\Gamma(\Omega\otimes L^{-2})\neq(0)$ ; hence  $L^{2}\cong\Omega(-P-Q)$  for some P, Q. Since the set of all L of degree five such that  $L^{2}\cong\Omega(-P-Q)$  for some P and Q is irreducible and two dimensional, it follows that  $\dim\Gamma(L)\geqslant2$  for any such L. Especially if  $M^{2}\cong\Omega$ , then  $\dim\Gamma(M(-P))\geqslant2$  for every  $P\in C$ . Therefore  $\dim\Gamma(M)\geqslant3$ . But for any principally polarized Abelian variety X and symmetric theta divisor  $\Theta\subset X$ ,  $\Theta$  cannot contain all points of order two on X (see Mumford [9, p. 346]). For Jacobians this means by Riemann's theorem that there is always an M with  $M^{2}\cong\Omega$ ,  $\Gamma(M)=(0)$ . This is a contradiction and (ii) never occurs. Q.E.D.

Note added in proof. Corollary 4 is Proposition 5.7 of Fay [4], in which there is a misprint: The lower limit of the integral in Fay should be D. To get our version, use the remarks at the top of p. 100.

## REFERENCES

1. A. Andreotti and A. Mayer, On period relations for abelian integrals on algebraic curves, Ann. Scuola Norm. Sup. Pisa 21 (1967), 189–238.

2. H. Clemens and P. Griffiths, The intermediate Jacobian of the cubic 3-fold, Ann. of Math. 95 (1972), 281–356.

3. H. Farkas and H. Rauch, Period relations of Schottky type on Riemann surfaces, Ann. of Math. 92 (1970), 434–461.

4. J. Fay, "Theta functions on Riemann Surfaces." Springer-Verlag, Berlin and New York, 1973, Lecture Notes, Vol. 352.

5. D. Harris, A study of 3-dimensional principally polarized abelian varieties. Ph.D. Thesis, Harvard Univ., Cambridge, Massachusetts, 1972.

6. W. Hoyt, On products and algebraic families of Jacobian varieties, Ann. of Math. 77 (1963), 415-423.

7. G. Kempf, On the geometry of a theory of Riemann, Ann. of Math. 98 (1973), 178–185.

8. H. Martens, On the varieties of special divisors on a curve, J. Reine Angew. Math. 227 (1967), 111–120.

9. D. Mumford, On the equations defining abelian varieties, Invent. Math. 1 (1966).

10. D. Mumford, “Abelian Varieties.” Tata Inst. Studies in Math., Oxford Univ. Press, London and New York, 1970.

11. D. Mumford, Theta characteristics of an algebraic curve, Ann. Sci. Ecole Norm. Sup. 4 (1971), 181–192.

12. J. Murre, Algebraic equivalence mod rational equivalence on a cubic 3-fold. Compositio Math. 25 (1972), 161–206.

13. B. Riemann, "Collected Works," Nochtrag IV. Dover, New York, 1953.

14. B. Saint-Donat, On Petri's analysis of the linear system of quadrics through a canonical curve, Math. Ann. 206 (1973), pp. 157–175.

15. F. Schottky and H. Jung, Neue Sätze über symmetralfunctionen und die Abelschen funktionen, S.-B. Berlin Akad. Wiss. (1909).

16. L. Szpiro, “Travaux de Kempf, Kleiman, Laksov,” (Sem. Bourbaki, Exp. 417), Springer-Verlag, Berlin and New York, 1972 Lecture Notes, Vol. 317.