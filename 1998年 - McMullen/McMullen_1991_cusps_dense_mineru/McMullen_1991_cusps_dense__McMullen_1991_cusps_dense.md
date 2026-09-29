# Cusps are dense

By CURT McMULLEN\*

## Abstract

We show cusps are dense in Bers' boundary for Teichmüller space. The proof rests on an estimate for the algebraic effect of a unit quasiconformal deformation supported in the thin part of a hyperbolic Riemann surface.

## 1. Introduction

The integrability of measurable complex structures is a powerful tool in the theory of dynamical systems in one complex variable—that is, Kleinian groups, iterated rational maps and their relatives.

A basic construction is the following. Given a conformal dynamical system on a Riemann surface X, consider any invariant complex structure (specified by a measurable ellipse field of bounded eccentricity). By the “measurable Riemann mapping theorem” [AB], there is a quasiconformal map  $f: X \to Y$  so that this measurable complex structure is the pull-back of a standard Riemann surface structure on Y. Conjugation by f yields a new conformal dynamical system on Y.

The deformation theory of Kleinian groups is founded on this construction ([Be4], [Mas2], [Su1]), and a parallel theory can be developed for rational maps [Su3].

Despite its power, this deformation theory is difficult to control; the geometry of the new dynamical system is typically hard to predict. In this regard, a fundamental problem is to estimate the algebraic effect of a quasiconformal deformation—how much does it change the coefficients of a rational map, or the generators of a Kleinian group?

In this paper we obtain an estimate for the algebraic change in a quasi-fuchsian group due to a unit quasiconformal deformation concentrated in the thin part of the quotient Riemann surface. The density of cusps in the boundary of Teichmüller space, conjectured by Bers in 1970 [Be3], follows from this estimate.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*Research partially supported by an NSF Postdoctoral Fellowship.</span></small>

To state our results, we recall some ideas from [Be3]. Let X be a hyperbolic Riemann surface of finite volume, presented as the quotient  $H/\Gamma_{X}$  of the upper half-plane by a Fuchsian group.

$\Gamma_{X}$ also acts on the whole Riemann sphere and in particular the quotient of the lower half-plane is $\overline{X}$, the complex conjugate of X.

Let $h: X \to Y$ be a quasiconformal isomorphism; then $(h, Y)$ determines a point in the Teichmüller space $\text{Teich}(X)$. The complex dilatation $\bar{\partial}h/\partial h$ lifts to a $\Gamma_X$-invariant differential $\mu$ on $H$, which we extend by zero to the whole of $\hat{C}$. Then there is a quasiconformal map $f: \hat{C} \to \hat{C}$ with dilatation $\mu$, which conjugates $\Gamma_X$ to a quasifuchsian group $\Gamma_Y$. Its limit set is a typically fractal Jordan curve which divides the sphere into two regions, one of which still yields as quotient $\overline{X}$, and the other of which uniformizes $Y$.

This construction provides an embedding

$$
\iota \colon \operatorname{Teich} (X) \hookrightarrow \operatorname{Hom} (\Gamma_ {X}, \mathrm{PSL} _ {2} \mathbf {C}) / \text { conjugation }
$$

whose image is a bounded set of discrete faithful representations. The closure of the image gives a compactification of Teichmüller space by Kleinian groups which are algebraic limits of quasifuchsian groups.

Definitions. A boundary point $\rho: \Gamma_X \to \Gamma \subset \mathrm{PSL}_2\mathbf{C}$ is a cusp if there is a hyperbolic $\gamma \in \Gamma_X$ such that $\rho(\gamma)$ is parabolic. In this case $\gamma$ represents a simple closed curve on $X$, and we say this curve has been pinched.

$\Gamma$ is totally degenerate if its domain of discontinuity consists of a single component. That is, the component uniformizing Y has disappeared completely. Bers showed that every boundary point is either a cusp or totally degenerate.

A boundary point is a maximal cusp if a maximal system of disjoint nonperipheral simple closed curves on X have been pinched to cusps. A maximal cusp is geometrically finite; Y has been reduced to a collection of triply punctured spheres.

In this paper we prove:

THEOREM 1.1 (Cusps are dense). Maximal cusps are dense on the boundary of Teichmüller space.

A maximal cusp is uniquely determined by purely topological data, namely the system of simple closed curves which is pinched. This theorem represents a first step towards a combinatorial description of the boundary, since a general point can be described by the cusps which approximate it, just as a real number can be encoded by a Cauchy sequence of rationals.

The proof depends on an estimate for the change in the representation  $\rho$  due to a unit quasiconformal deformation of Y supported in the thin part.

The technique by which quasiconformal and algebraic deformations are related can be applied to general hyperbolic 3-manifolds; this will be developed in a sequel. There is also some promise of application to other conformal dynamical systems, such as iterated rational maps.

To describe the estimate we return to Bers' construction. The map $f$ conjugating $\Gamma_X$ to $\Gamma_Y$ is conformal in the lower half-plane, and by invariance its Schwarzian derivative $Sf$ descends to a quadratic differential $\phi_Y$ on $\overline{X}$. This provides a related embedding

$$
\beta \colon \operatorname{Teich} (X) \hookrightarrow P (\overline {{X}})
$$

where  $P(\overline{X})$  is the finite dimensional space of holomorphic quadratic differentials on  $\overline{X}$  equipped with the norm

$$
\| \phi \| = \sup _ {\overline {{{X}}}} \rho^ {- 2} | \phi | <   \infty ;
$$

here $\rho(z)|dz|$ denotes the Poincaré metric on $\overline{X}$.

By a result of Nehari [N], in this norm Teichmüller space lies within a ball of radius 3/2, so again its closure is compact.

The space $P(\overline{X})$ parameterizes projective structures on $\overline{X}$. The original embedding $\iota$ can be factored as $\eta \circ \beta$, where $\eta$,

$$
\eta \colon P (\overline {{X}}) \to \operatorname{Hom} \left(\Gamma_ {X}, \mathrm{PSL} _ {2} \mathbf {C}\right) / \text { conjugation },
$$

is the holonomy map. The map  $\eta$  is analytic on all of  $P(\overline{X})$  and injective on the closure of  $\beta(\text{Teich}(X))$ ; thus the compactifications by projective structures and by groups are homeomorphic.

We will use the norm on P as a metric on the compactified Teichmüller space, even when we are thinking of the compactification as a space of groups. Since P is a vector space, it is naturally its own tangent space and the lengths of vectors on P will also be measured using the norm.

For  $Y \in \text{Teich}(X)$  let  $M(Y)$  denote the space of bounded measurable Beltrami differentials  $\mu(z) \, d\bar{z}/dz$  on Y with the norm

$$
\| \mu \| = \sup _ {Y} | \mu |.
$$

Each  $\mu$  determines an infinitesimal quasiconformal deformation of Y, and thereby a tangent vector to  $\operatorname{Teich}(X)$  at Y.

Density of cusps follows from:

THEOREM 1.2 (Short geodesics pinch quickly). Let $\mu$ be a unit-norm Beltrami differential supported in the part of $Y$ of injectivity radius less than

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$ A palatable discussion of the Schwarzian derivative appears in [T2].</span></small>

$L < 1/2$. Then the image of $\mu$ under the derivative of Bers' embedding has length at most $C(L \log 1/L)^{2}$ where the constant $C$ depends only on $X$.

## Remarks.

1. C must depend on the base Riemann surface X. In fact, for Y = X we have a Fuchsian group, and when X has a short geodesic it is easy to produce a unit quasiconformal deformation supported in the thin part which moves distance  $\asymp 1$  in Bers' embedding, independent of the length of the short geodesic. The proof shows we may take  $C = O(1 + 1/\text{short}(X)^{2})$  where  $\text{short}(X)$  is the length of the shortest closed geodesic on X.

2. This estimate is close to sharp; for example, in the usual process of pinching a short geodesic (see [Be3, Th. 11]),  $\|d\beta(\mu)\| > cL^{2}$  as  $L \to 0$ . (A unit deformation changes the trace of the group element being made parabolic by  $cL^{2}$ , and the trace is a Lipschitz function on Bers' compactification.)

COROLLARY 1.3. Let Y be a point of a fixed Teichmüller space. Then if Y has some disjoint simple geodesics of length less than L < 1/2, Y is within  $O((L \log 1/L)^{2})$  of a cusp where these curves become parabolic.

Proof. By a roughly unit deformation on the level of Teichmüller space, we can pinch a curve from length L to length L/2, using a  $\mu$  supported in the part of injectivity radius less than 2L (see Figure 1). The movement in the  $P(\overline{X})$  norm may be bounded using the preceding result. After the  $k^{th}$  step the Beltrami differential can be concentrated in the region of injectivity radius less than  $2^{-k}L$ ; sum the resulting geometric series. ☐

![](images/page_3_image_6.jpg)

FIGURE 1. Pinching supported in the thin part.

To derive the density of cusps we begin with some topological facts about Bers' compactification.

PROPOSITION 1.4. Teich(X) is embedded in $P(\overline{X})$ as a regular open set.

(This means Teichmüller space is the interior of its closure.)

Proof. Over the interior of its closure we have a holomorphically varying family of discrete groups. By the extended  $\lambda$ -lemma, these are all quasiconformally conjugate (see [Be5], [Su2]). Since the interior is connected, they are all quasifuchsian groups. Therefore this space coincides with Teichmüller space. ☐

(See [Sh., Cor. 1] for another proof.)

We now recall a theorem of [Bel]:

COROLLARY 1.5. The boundary of Teichmüller space contains a dense $G_{\delta}$ consisting of totally degenerate groups.

Proof. The cusps are contained in a countable union of proper analytic subsets, defined by  $\mathrm{Tr}(\gamma)^{2}=4$  for each  $\gamma\in\pi_{1}(X)$  represented by a simple geodesic which can potentially be pinched. By the preceding proposition, each of these is nowhere dense in the boundary. Therefore cusp-free totally degenerate groups form a dense  $G_{\delta}$ . □

Proof of 1.1 (Cusps are dense). Let B be a point in the boundary of the Teichmüller space  $\operatorname{Teich}(X)$ . By preceding results, it is enough to show B is a limit of cusps when B represents a totally degenerate group.

Let $Y_{n} \to B$ be a sequence of points in Teichmüller space tending to $B$. For each $n$ we may choose a maximal set of disjoint simple closed curves $S_{n}$ such that the total length of $S_{n}$ on $Y_{n}$ is less than some universal constant depending only on the topology of $X$.

Now, by a uniformly bounded quasiconformal deformation of each  $Y_{n}$  we may obtain a new sequence  $Z_{n}$  such that the length of  $S_{n}$  is less than  $\varepsilon$  for all n. Since B is quasiconformally rigid (relative to the fixed conformal structure on one end, by Sullivan's extension of Mostow rigidity [Su1]),  $Z_{n} \rightarrow B$  as well. By a diagonalization argument, we obtain  $Z_{n} \rightarrow B$  with the length of  $S_{n}$  tending to zero. By Corollary 1.3, we may pinch the  $S_{n}$  simultaneously to cusps  $C_{n}$, moving a distance which goes to zero as the length of  $S_{n}$  goes to zero. Therefore  $B = \lim C_{n}$  is a limit of maximal cusps.

Recall that each point in the closure of Teichmüller space determines a hyperbolic 3-manifold  $\mathbf{H}^{3}/\rho(\Gamma_{X})$ .

COROLLARY 1.6. The boundary of Teichmüller space contains a dense $G_{\delta}$ of hyperbolic 3-manifolds with arbitrarily short geodesics.

Proof. The set of boundary points with a geodesic of length less than 1/n is open and dense by density of cusps; apply the Baire category theorem. □

COROLLARY 1.7. Under the action of the mapping-class group, the orbit of any point in Teichmüller space accumulates densely on Bers' boundary.

Proof. Let Y be a point in Teichmüller space, S a maximal system of disjoint simple closed curves on Y, and let  $\tau$  be an element of the mapping class group obtained as the composition of Dehn twists around every element of S. Then  $\tau^{n}(Y)$  tends to the unique cusp point for which every curve S has become parabolic ([Ab2, Th. 3]; see also [Mar], [H]). Since maximal cusp points are dense, the corollary follows. □

Idea of the proof of Theorem 1.2. Given a quasifuchsian group $\Gamma_{Y}$, normalize so that a point in the component uniformizing $\overline{X}$ is at infinity, and the Poincaré metric at infinity matches the spherical metric. Then the limit set has universally bounded diameter; so the total area it encloses is bounded, and the distortion of projective structure at infinity is proportional (by a fixed constant) to $\int \mu dz^2$, where $\mu$ is a group-invariant Beltrami differential, and $dz^2$ is the standard quadratic differential in the plane.

The thin part of Y has cyclic fundamental group; to each component of its lift to the plane there corresponds a Möbius transformation  $\gamma$  with small translation length in hyperbolic space. By invariance under  $\gamma$, the Beltrami differential  $\mu$  is forced to swirl quite a bit. For example,  $\mu$  might be a constant multiple of the line field shown in Figure 2 (next page), which is invariant under a loxodromic transformation with small translation. This swirling causes inefficiency (cancellation) in the integral (that is,  $|f\mu dz^{2}| \ll f|\mu|dz|^{2}$ ).

To each short  $\gamma$ , associate a region in the plane on which there is some definite inefficiency due to swirling. The Margulis lemma forces these regions to be scattered about independent of one another. One finds that the local inefficiencies fit together without conflict to give the desired global estimate.

Remark. In general, it is not sufficient just to estimate the area of the support of  $\mu$ . The role of cancellation is essential in the case where the length of the geodesic  $\gamma$  to be pinched is much shorter in the hyperbolic 3-manifold  $H^{3}/\Gamma_{Y}$  than on the hyperbolic surface Y. (This occurs, for example, when  $Y = \tau^{n}(Y_{0})$  and  $\tau^{n}$  is a high power of a Dehn twist about  $\gamma$ ; see [KT, §3]).

![](images/page_6_image_0.jpg)

FIGURE 2. An invariant line field for a short geodesic.

## Outline of the paper

Section 2 introduces the integral kernel for the derivative of Bers' embedding; this kernel provides a link between quasiconformal and algebraic deformations. As an illustration, a bound of $O(\exp(-1/L))$ is derived for the effect of a deformation supported in the cuspidal thin part of $Y$.

Section 3 addresses the heart of the matter: estimating the effect of a deformation supported in the geodesic thin part. We begin by examining the geometry of an invariant region for a single hyperbolic transformation  $\gamma$ . Then a calculation gives an asymptotic formula for the inefficiency forced by invariance.

Section 4 applies the Margulis lemma to analyze the way in which invariant regions associated to different short geodesics fit together. In Section 5 we return to the setting of quasifuchsian groups and complete the proof of Theorem 1.2.

Acknowledgements. After this paper was submitted, Mitsuhiro Shishikura found a more concise proof of Proposition 3.4, which we present below. I would also like to thank Harumi Tanigawa and the referee for useful comments.

Bibliographical remarks. Bers' boundary is discussed in [Be3], [Mas1], [Ab1], and [Ab2]. Quasifuchsian groups are discussed from a 3-dimensional point of view in [T1, §§8, 9], [T3] and [Bo].

Ehrenpreis conjectured that the “limit set” of the mapping-class group is the full boundary of Teichmüller space, in a weaker sense than that of Corollary 1.7 [E]; this was proved by Abikoff [Ab2].

A more detailed picture of 3-manifolds with arbitrarily short geodesics (as in Corollary 1.6) can be found in [BO] and [T3].

The author was introduced to the closely related Maskit boundary of the Teichmüller space of once-punctured tori by Mumford and Wright in 1981, as part of a joint computer investigation stemming from work of Jørgenson. This investigation is presented in [W].

Notation.  $O(x)$  denotes a quantity whose absolute value is bounded by Cx for some unspecified universal constant C > 0 (often computable in principle);  $f \asymp x$  means cx < f < Cx, again for unspecified c, C > 0.

## 2. Quasiconformal distortion of projective structure

Let $\mu = \mu(z) d\bar{z}/dz$ be a bounded measurable Beltrami differential on $\hat{\mathbf{C}}$, vanishing on an open set $U$. By [AB] there is a one-parameter family of quasiconformal maps $f_t: \hat{\mathbf{C}} \to \hat{\mathbf{C}}$ with dilatation $t\mu$, such that $f_t(z)$ is holomorphic in $t$. Here $t$ ranges in the unit disk in $\mathbf{C}$.

Since $\mu = 0$ on $U$, $f_{t}$ gives a family of conformal mappings of $U$ into $\hat{\mathbf{C}}$. Taking the Schwarzian derivative with respect to $z$,

$$
S (f _ {t}) = \left(\frac {f _ {t} ^ {\prime \prime}}{f _ {t} ^ {\prime}}\right) ^ {\prime} - \frac {1}{2} \left(\frac {f _ {t} ^ {\prime \prime}}{f _ {t} ^ {\prime}}\right) ^ {2},
$$

we obtain a holomorphic family of quadratic differentials  $S(f_{t})(z) dz^{2}$  on U.

Remark. A solution to the Beltrami equation

$$
\frac {d (f _ {t}) / d \bar {z}}{d (f _ {t}) / d z} = t \mu
$$

is well-defined only up to post-composition with a Möbius transformation  $M_{t}$ . However, replacing  $f_{t}$  with  $M_{t} \circ f_{t}$  leaves its Schwarzian derivative unchanged; so the family of quadratic differentials  $S(f_{t})$  is naturally determined by  $\mu$  without any choice of normalization.

The rate of change of Schwarzian derivative at t = 0 gives the infinitesimal distortion of projective structure on U caused by the change in conformal structure on its complement.

PROPOSITION 2.1. The quadratic differential

$$
\phi = \frac {d S (f _ {t})}{d t} \Bigg | _ {t = 0}
$$

is given by convolution of $\mu$ with a kernel

$$
K (z, w) = - \frac {6}{\pi} \frac {d z ^ {2} d w ^ {2}}{(z - w) ^ {4}}
$$

on $\hat{\mathbf{C}}\times \hat{\mathbf{C}}$ ; that is

$$
\phi (w) d w ^ {2} = \left(- \frac {6}{\pi} \int_ {\hat {\mathrm{C}}} \frac {\mu (z) | d z | ^ {2}}{(z - w) ^ {4}}\right) d w ^ {2}.
$$

(Note that the product of a quadratic differential and a Beltrami differential in $z$ naturally has the type of an area form $|dz|^2$.)

Proof. See [Be2] or [Ga, §5.7].

To better understand this formula, assume  $\infty \in U$ . Introducing the coordinate u = 1/w, we find the projective distortion at infinity is given by

$$
\phi (\infty) = \left(- \frac {6}{\pi} \int_ {\hat {\mathbf {C}}} \mu (z) | d z | ^ {2}\right) d u ^ {2};\tag{2.1}
$$

i.e., the value of  $\phi$  is essentially the average of  $\mu$  with respect to Euclidean area. The factor  $-6/\pi$  can be checked using the example

$$
f _ {t} (z) = \left\{ \begin{array}{l l} z + t / z & \text {if} | z | > 1 \\ z + t \bar {z} & \text {otherwise} \end{array} \right.,
$$

for which  $\mu = d\bar{z}/dz$  is supported on the unit disk and  $dS(f_{t})/dt = -6 dz^{2}/z^{4}$ ; the  $\pi$  comes from the area of the disk. (In fact, the general form of the kernel follows from this example by continuity and linearity.)

2.1. The derivative of Bers' embedding. For $Y \in \operatorname{Teich}(X)$ let $\mu \in M(Y)$ represent a tangent vector to Teichmüller space at $Y$. We will give a geometric picture for the quantity $\| d\beta(\mu)\|$ which measures the infinitesimal change in projective structure on $\overline{X}$ due to $\mu$.

The limit set  $\Lambda$  of  $\Gamma_{Y}$  divides the sphere into two disks,  $\Omega(\overline{X})$  and  $\Omega(Y)$ , whose quotients are  $\overline{X}$  and Y. The Beltrami differential  $\mu$  lifts to an invariant form on  $\Omega(Y)$  which we continue to denote by  $\mu$ .

THEOREM 2.2. The derivative of Bers' embedding satisfies

$$
\left\| d \beta (\mu) \right\| \asymp \sup _ {p} \frac {1}{\operatorname{diam} _ {p} (\Lambda) ^ {2}} \left| \int_ {\Omega (Y)} \mu \left(z _ {p}\right) \left| d z _ {p} \right| ^ {2} \right|
$$

where $p$ ranges over $\Omega (\overline{X})$, $z_{p}$ denotes an affine coordinate on $\hat{\mathbf{C}}$ such that $z_{p}(\infty) = p$, and $\mathrm{diam}_p(\Lambda)$ is the diameter of the limit set measured in the $|dz_p|$-metric.

Proof. Let $f \colon \hat{\mathbf{C}} \to \hat{\mathbf{C}}$ conjugate $\Gamma_X$ to $\Gamma_Y$ as in Bers' construction. Then

$$
\beta (Y) = S f | \overline {{\mathbf {H}}}
$$

in the sense that Sf is a  $\Gamma_{X}$ -invariant quadratic differential, holomorphic on the lower half plane and thereby representing an element of  $P(\overline{X})$ .

Solve the Beltrami equation

$$
\frac {d (g _ {t}) / d \bar {z}}{d (g _ {t}) / d z} = t \mu .
$$

Then we obtain a path $Y_{t}$ in Teichmüller space with

$$
d \beta (\mu) = \frac {d \beta (Y _ {t})}{d t} \Bigg | _ {t = 0} = \frac {d}{d t} S (g _ {t} \circ f) = \frac {d}{d t} (S f + f ^ {*} S g _ {t}) = f ^ {*} \left(\frac {d S g _ {t}}{d t}\right) = f ^ {*} \phi ,
$$

where $\phi(p)$ can be expressed by equation 2.1, giving

$$
\left| \phi (\infty) \right| \asymp \left| \int_ {\hat {\mathbf {C}}} \mu (z) | d z _ {p} | ^ {2} \right| | d u | ^ {2},\tag{2.2}
$$

$u = 1 / z_{p}$. Since the limit set is connected, the Poincaré metric at infinity satisfies $\rho(p)|du| \asymp \text{diam}(\Lambda)|du|$. (This follows from the Schwarz lemma and the Koebe 1/4 theorem; cf. [BP].) The result now follows from the definition $\|\phi\| = \sup_{p} \rho^{-2}|\phi|$, when we use the fact that $f$ is an isometry for the Poincaré metric.

COROLLARY 2.3. $\| d\beta \| = O(1)$.

Proof. For unit-norm $\mu$,

$$
\left| \int \mu | d z _ {p} | ^ {2} \right| \leq \operatorname{area} _ {p} (\Omega (Y)) \leq O \left(\operatorname{diam} _ {p} (\Lambda) ^ {2}\right).
$$

Remark. In fact,  $\|d\beta\|\leq3/2$ . (The image of  $\beta$  is contained in the ball of radius 3/2 by Nehari's theorem; apply the Schwarz lemma.)

Here is a dual description of the size of  $\|d\beta(\mu)\|$ .

Definitions. For any Riemann surface X, let  $Q(X)$  denote the space of holomorphic quadratic differentials  $\phi(z) dz^{2}$  on X such that

$$
\| \phi \| = \int_ {X} | \phi | <   \infty .
$$

With this norm,  $Q(X)$  is a Banach space.

There is a natural pairing between Beltrami differentials in  $M(X)$  and quadratic differentials in  $Q(X)$ , given by

$$
\langle \phi , \mu \rangle = \mathrm{Re} \int_ {X} \phi \mu .
$$

$Q(X)$ may be identified with the cotangent space to Teichmüller space at X, and $Q^{*}(X) = M(X)/Q(X)^{\perp}$ with the tangent space (see, e.g., [G]).

Given a covering $\pi: Y \to X$ and $\phi \in Q(Y)$, the push-forward $\pi_*(\phi)$ is defined by summing $(\pi^{-1})^*\phi$ over the various branches of $\pi^{-1}$. The map $\phi \mapsto \pi_*(\phi)$ defines an operator traditionally denoted

$$
\Theta_ {Y / X} \colon Q (Y) \to Q (X),
$$

first introduced by Poincaré in his construction of automorphic forms [P].

Push-forward of quadratic differentials is like push-forward of measures, except some cancellation may result due to incoherence in the phase of  $\phi$  over different sheets. Thus  $\|\Theta_{Y/X}\| \leq 1$ .

For simplicity of notation, let

$$
\Theta = \Theta_ {\Omega (Y) / Y}.
$$

In terms of  $\Theta$ , a useful reformulation of Theorem 2.2 is the following:

THEOREM 2.4. Let $\mu$ be of unit norm in $M(Y)$ and supported in $Y' \subset Y$. Then

$$
\left\| d \beta (\mu) \right\| \leq O \left(\sup _ {p} \frac {1}{\operatorname{diam} _ {p} (\Lambda) ^ {2}} \int_ {Y ^ {\prime}} \left| \Theta \left(d z _ {p} ^ {2}\right) \right|\right).
$$

Proof. This is immediate from the duality

$$
\langle \phi , \pi^ {*} \mu \rangle = \langle \pi_ {*} \phi , \mu \rangle .
$$

2.2. Cuspidal deformations are negligible. This section presents a bound for the effect of a quasiconformal deformation concentrated in a neighborhood of the cusps of Y.

Definition. The L-thin part of Y is the set of points through which there is a nontrivial loop of length less than L; we will denote it by  $Y(L)$ .

There is an  $L_{0} > 0$  such that for  $L < L_{0}$ , the thin part consists of annuli centered on short geodesics and horoball neighborhoods of cusps. The union of the cuspidal components is the cuspidal thin part  $Y(L, \text{cusps})$ .

Remark. The triply-punctured sphere and the punctured square torus are the extreme examples for  $L_{0}$ ; the sharp value is  $L_{0} = \log(3 + 2\sqrt{2})$  [Y].

PROPOSITION 2.5. Let Y be a hyperbolic Riemann surface, $\phi \in Q(Y)$. Then the mass of $|\phi|$ in the cuspidal thin part is exponentially small:

$$
\int_ {Y (L, \text { cusps })} | \phi | \leq O (\exp (- 1 / L)) \int_ {Y} | \phi |.
$$

Proof. Assume  $L < L_{0}$ . Let E be a cuspidal component of the  $L_{0}$ -thin part of Y, and let  $D \subset E$  be the subset lying in the L-thin part.

Introduce a local coordinate w on Y so that E corresponds to the punctured unit disk  $\{w: 0 < |w| < 1\}$ . Then D is contained in the punctured disk of w-radius  $R = O(\exp(-1/L))$ , by a standard Poincaré metric calculation.

$\phi$ is integrable so at worst it has a pole at the puncture w = 0. Write $\phi(w) dw^{2} = (\psi(w)/w) dw^{2}$ where $\psi$ is holomorphic; then $|\psi(w)|$ is subharmonic, so its average over the circle $|w| = r$ is an increasing function of r. Therefore

$$
\begin{array}{r l} \int_ {D} | \phi | & = \int_ {0} ^ {R} \int_ {0} ^ {2 \pi} \frac {| \psi (r \exp (i \theta)) |}{r} r d \theta d r \leq R \int_ {0} ^ {1} \int_ {0} ^ {2 \pi} | \psi (r \exp (i \theta)) | d \theta d r \\ & = R \int_ {E} | \phi |. \end{array}
$$

This inequality holds on each component E, and the proposition follows.

COROLLARY 2.6. Let $\mu \in M(Y)$, $\| \mu \| = 1$ be supported in the cuspidal components of the $L$-thin part of $Y$. Then the image of $\mu$ under the derivative of Bers' embedding has length $O(\exp(-1/L))$.

Proof. Since $\| \Theta \| \leq 1$,

$$
\int_ {Y} \left| \Theta \left(d z _ {p} ^ {2}\right) \right| \leq \int_ {\Omega (Y)} | d z _ {p} ^ {2} | = \operatorname{area} _ {p} (\Omega (Y)) \leq O \left(\operatorname{diam} _ {p} (\Lambda) ^ {2}\right)
$$

because $\Lambda$ is the boundary of $\Omega(Y)$. The integral of $|\Theta(dz_p^2)|$ over just $Y(L, \text{cusps})$ is $O(\exp(-1/L))$ times smaller; apply Theorem 2.4.

Remark. This sort of argument cannot be applied to the geodesic thin part. In fact, when Y has a short geodesic, there is a quadratic differential  $\phi$  with most of its mass in the thin part.

The idea for treating the geodesic thin part appears, in a non-quantitative form, in the proof of Theorem 6.1 of [Mc].

## 3. Short geodesics

Definitions. Let

$$
\mathcal {L} = \ell + i \theta , \quad \ell > 0
$$

be a complex translation length, and let  $\gamma$  be a Möbius transformation with translation length L. This means  $\gamma$  stabilizes a geodesic in hyperbolic 3-space, translates points on the geodesic by distance l, and twists a normal plane by angle  $\theta$ . Notice that  $\gamma$  determines  $\theta$  only up to a multiple of  $2\pi$ .

Let $\Omega \subset \hat{\mathbf{C}}$ be the complement of the fixed points of $\gamma$; then $\Omega / \gamma = T$ is a complex torus. We give $T$ its usual flat metric (well-defined up to scale).

Using L, we can include  $\gamma$  in a 1-parameter group of translations of length  $tL$ ,  $t \in R$ ; letting t range in [0, 1], we obtain a path connecting p to  $\gamma(p)$  for any  $p \in \Omega$ , which descends to a well-defined homotopy class  $[\gamma] \in \pi_{1}(T)$ . Conversely, the choice of a representative in the  $\gamma$ -coset of  $\pi_{1}(T)$  determines L uniquely.

An annulus has modulus M if it is conformally isomorphic to a right cylinder of radius 1 and height M (equivalently the region  $1 < |z| < \log M$ ).

Let $M$ denote the modulus of the cylinder $T - g$ where $g$ is a geodesic representative for $[\gamma]$; one may check that

$$
M = 4 \pi^ {2} \operatorname{Re} (1 / \mathscr {L}).
$$

(Note that $T - g$ is isomorphic to the region in $\mathbf{C}$ between the two lines $\mathbf{R}\mathcal{L}$ and $2\pi i + \mathbf{R}\mathcal{L}$, modulo the translation $z \mapsto z + \mathcal{L}$. Multiplying this region by $2\pi / \mathcal{L}$, we find $T - g$ is also isomorphic to the quotient of

$$
\{z \colon 0 <   \operatorname{Im} (z) <   \operatorname{Im} \left(4 \pi^ {2} i / \mathscr {L}\right) = M \}
$$

by $z \mapsto z + 2\pi$, which is clearly a cylinder of modulus $M$.)

Given  $p \in \Omega$  and m < M, let  $A \subset T$  be the annulus in the homotopy class  $[\gamma]$  obtained by removing a right cylinder of modulus m centered at the image of p on T. This means p projects to a point in T - A at maximal distance from A, i.e., midway between the two boundary components.

Define the thickened spiral  $B \subset \Omega$  to be the pre-image of A. The region B is bounded by a pair of exponential spirals connecting the fixed points of  $\gamma$ .

Note that the construction of $B$ depends only on:

1. The isometry $\gamma$;

2. The complex translation length $\mathcal{L}$;

3. The modulus $m$; and

4. The point $p$.

When necessary this dependence will be made explicit by the notation  $B(\gamma, \mathcal{L}, m, p)$ .

Let $z_{p}$ be any affine coordinate such that $z_{p}(p) = \infty$. By restriction, the quadratic differential $dz_{p}^{2}$ is an element of $Q(B)$.

Associated to the covering  $B \rightarrow A$  is the push-forward operator

$$
\Theta_ {B / A} \colon Q (B) \to Q (A).
$$

THEOREM 3.1 (Inefficiency from swirling). For $m > 4\pi$,

$$
\frac {\left\| \Theta_ {B / A} \left(d z _ {p} ^ {2}\right) \right\|}{\left\| d z _ {p} ^ {2} \right\|} = O \left(\frac {m ^ {2}}{M ^ {2}} + \frac {m ^ {2}}{\exp (m / 2)}\right);
$$

the norms are in $Q(B)$ and $Q(A)$ respectively.

Remarks.

1. Geometrically, the theorem bounds the extent to which a  $\gamma$ -invariant line field on B can be synchronized with the horizontal lines in the plane. More precisely, associate to each point  $z \in B$  an unoriented tangent line through z at angle  $\theta(z)$  (defined mod  $\pi$ ), in such a way that the derivative of  $\gamma$  carries the line at z to the line at  $\gamma(z)$ . Then the theorem gives a bound for the average of  $\cos(2\theta(z))$  over B. In fact, when we set  $\mu = \exp(2i\theta(z)) d\bar{z}/dz$ , this average is exactly

$$
\frac {\langle \mu , d z ^ {2} \rangle}{\| d z ^ {2} \|} \leq \frac {\| \Theta_ {B / A} (d z ^ {2}) \|}{\| d z ^ {2} \|}.
$$

2. An affine change of coordinates  $(z \mapsto az + b)$  leaves the ratio above unchanged; one may choose any coordinate system in which  $z_{p}(p) = \infty$ .

3. We are mostly interested in the case where $m$ is large but $m \ll M$. If $m$ is $4\log(M)$, then the bound becomes $O(M^{-2}(\log M)^2)$, which leads to Theorem 1.2.

4. The result fails without a lower bound on m. When m is small, a fundamental domain for the action of  $\gamma$  on B occupies most of the area of B, and pushing forward causes little cancellation.

The remainder of the section is devoted to the proof.

3.1. Spirals. We begin with some estimates for the shape of B when viewed from p, i.e., in the metric  $|dz_{p}|$ . In this section  $B = B(\gamma, \mathscr{L}, m, p)$ .

Choose the coordinate $z = z_{p}$ so that the attracting and repelling fixed points of $\gamma$ are 0 and 1 respectively; then $\Omega = \hat{\mathbf{C}} - \{0,1\}$ and

$$
\gamma (z) = N \left(\exp (\mathscr {L}) N ^ {- 1} (z)\right) \quad \text { where } \quad N (z) = 1 / (1 - z).
$$

(The Möbius transformation N carries  $C^{*}$  to  $\Omega$ , sending 1 to  $\infty$ .)

Identify the universal cover of  $\Omega$  with C via the covering map

$$
s \mapsto N (\exp (\mathscr {L} s)) = z;
$$

then in these coordinates,

$$
\begin{array}{l l} T = \mathbf {C} / \Lambda & \text { where } \\ \Lambda = \mathbf {Z} \oplus \mathbf {Z} \tau & \text { and } \\ \tau = 2 \pi i / \mathscr {L}, \end{array}
$$

and our choice of $\mathcal{L}$ determines a natural lift of $\gamma$ to the transformation $\gamma(s) = s + 1$.

We introduce the notation

$$
p _ {\Omega} \colon \mathbf {C} \to \mathbf {C} / \mathbf {Z} \tau = \Omega \quad \mathrm{and}
$$

$$
p _ {T} \colon \mathbf {C} \rightarrow \mathbf {C} / \Lambda = T
$$

for covering maps from the s-plane.

For $y \in [0, \operatorname{Im} \tau / 2]$ let

$$
C (y) = \{s: y <   \operatorname{Im} (s) <   \operatorname{Im} (\tau) - y \}
$$

denote a strip in the universal cover of  $\Omega$ ; then

$$
B = p _ {\Omega} (C (y)) \quad \mathrm{and}
$$

$$
A = p _ {T} (C (y)) \quad \text { where } y = m / 4 \pi .
$$

Here $A$ and $T - A$ are cylinders on $T$ in the homotopy class $[\gamma]$;

$$
m = \operatorname{mod} (T - A) = 4 \pi y \quad \mathrm{and}
$$

$$
M = \operatorname{mod} (T - g) = 2 \pi \operatorname{Im} \tau .
$$

The region B is bounded by a pair of exponential spirals running from 0 to 1 (see Figure 3).

![](images/page_14_image_9.jpg)

FIGURE 3. Spirals.

PROPOSITION 3.2.

1. The diameter of $B$ is $\asymp 1 / |m\mathcal{L}|$.

2. If $m < M / 2$, then $\mathrm{area}_p(B) \asymp (\mathrm{diam}_p B)^2$.

Remark. Note that

$$
| m \mathscr {L} | \leq | M \mathscr {L} | \asymp \frac {| \operatorname{Im} (1 / \mathscr {L}) |}{1 / | \mathscr {L} |} \leq 1;
$$

so the estimate above is compatible with the fact that the diameter of B is always at least one.

Proof. Recall the Koebe 1/4 theorem (see, e.g., [Ah]): the image of a univalent map $f \colon D(x, r) \to \mathbf{C}$ contains a disk $D(f(x), R)$ where $R = f'(x)r/4$. (Here $D(x, r)$ denotes the disk of radius $r$ centered at $x$.)

1. Since  $p_{\Omega}$  maps  $D(0, y)$  univalently to a neighborhood of infinity, disjoint from B, we can bound the diameter of B from above using the Koebe theorem. To this end, let

$$
q (s) = 1 / p _ {\Omega} (s) = 1 - \exp (\mathscr {L} s).
$$

Then $|q'(0)| = |\mathcal{L}|$, so that $q(D(0,y)) \supset D(0,r)$ where $r \asymp |\mathcal{L}|y \asymp |\mathcal{L}|m$; therefore $B \subset D(0,1/r)$, giving an upper bound on the diameter.

On the other hand, $q(iy) = O(|\mathcal{L}y|)$ (since $|\mathcal{L}y| = O(1)$), and both 0 and $1/q(iy)$ belong to $B$, so that the diameter of $B$ is in fact comparable to $1/|m\mathcal{L}|$.

2. Similarly, if $m < M / 2$, then $D(2iy, y) \subset C(y)$ and $p_{\Omega}$ maps this disk univalently into $B$; so the Koebe theorem provides a lower bound on the area of $B$. The assumption $m < M / 2$ implies $|2\mathcal{L}iy| < \pi$, and therefore

$$
\left| p _ {\Omega} ^ {\prime} (2 i y) \right| = \frac {| \mathscr {L} \exp (2 \mathscr {L} i y) |}{\left| 1 - \exp (2 \mathscr {L} i y) \right| ^ {2}} \asymp \frac {1}{| \mathscr {L} | y ^ {2}}.
$$

Thus the image of $D(2iy, y)$ under $p_{\Omega}$ has area at least $1 / |y\mathcal{L}|^2 \asymp \mathrm{diam}_p(B)^2$.

The bound in the other direction,  $\text{area}_{p}(B) = O(\text{diam}_{p}(B)^{2})$ , holds for any region B.

Remark. Our main interest lies in the region  $1 < m \ll M$ . Then B is well-approximated by a pair of round disks of diameter  $\asymp 1/|mL|$ , tangent at the origin. The spiraling of  $\partial B$  is only evident at a scale much smaller than the diameter of B.

PROPOSITION 3.3. Let $E$ be a $\gamma$-invariant subset of $\hat{\mathbf{C}}$, disjoint from $B = B(\gamma, \mathcal{L}, m, p)$, where $m > 1$. Then:

1. $\operatorname{diam}_p(B) \leq O(\operatorname{diam}_p(E))$.

2. There is a constant $\dot{C} > 0$ such that if

$$
\max _ {e \in E} \operatorname{dist} _ {p} (e, B) <   C \operatorname{diam} _ {p} (B),
$$

then $E$ is contained in the larger twisted spiral $B' = B(\gamma, \mathcal{L}, m/2, p)$.

Proof. Since $E$ is $\gamma$-invariant, its preimage $F = p_{\Omega}^{-1}(E)$ is invariant under the full lattice $\Lambda = \mathbf{Z} \oplus \mathbf{Z}\tau$. Moreover, $E$ is disjoint from $B$; so there is an $s \in F$ with $|\operatorname{Re}s| < 1$ and $|\operatorname{Im}s| < y$. Our assumption $m > 1$ gives $y > 1/4\pi$ and so we can assert $|s| = O(y)$.

1. As in the preceding proof, $q(s) = O(|\mathcal{L}y|)$, and so $E$ contains one point $p_{\Omega}(s)$ with $|p_{\Omega}(s)| > c / |\mathcal{L}y|$ for some constant $c > 0$.

In addition, $\overline{E}$ contains the fixed points 0 and 1 of $\gamma$; thus $\mathrm{diam}_p(B) \asymp 1 / |\mathcal{L}y| = O(\mathrm{diam}_p(E))$.

2. If $E$ is not contained in $B'$, then we can assume in addition that $|\operatorname{Im}s| < y/2$. To complete the proof, we need only show that for $e = p_{\Omega}(s)$, $\text{dist}_p(e, B) > C \text{diam}_p(B)$ for some universal $C > 0$. But $p_{\Omega}$ maps $D(s, y/2)$ univalently into the complement of $B$, and the desired estimate follows by the Koebe theorem once again.

3.2. Descent to the torus. We now turn to the problem of estimating  $\|\Theta_{B/A}(dz^{2})\|$ . Let

$$
\phi = d z ^ {2}, \quad \Phi = \sum_ {n} (\gamma^ {n}) ^ {*} \phi .
$$

Then

$$
\left\| \Theta_ {B / A} (\phi) \right\| = \int_ {B _ {0}} | \Phi |,
$$

where  $B_{0}$  denotes a fundamental domain for the action of  $\gamma$  on B.

Similarly, if we let

$$
\psi (s) d s ^ {2} = p _ {\Omega} ^ {*} (\phi),
$$

and

$$
\Psi (s) d s ^ {2} = p _ {T} ^ {*} \left(\Theta_ {B / A} (\phi)\right) = \sum_ {n} \psi (s - n) d s ^ {2},
$$

then

(3.1)

$$
\left\| \Theta_ {B / A} (\phi) \right\| = \int_ {C _ {0}} | \Psi | | d s | ^ {2}
$$

where

$$
C _ {0} (y) = \{s \in C (y): \operatorname{Re} (s) \in [ 0, 1 ] \}
$$

is the intersection of $C(y)$ with a fundamental domain for the lattice $\Lambda$.

Note that  $\psi(s)$  is periodic with period  $\tau$ , while  $\Psi(s)$  is periodic with respect to the full lattice  $\Lambda$  generated by 1 and  $\tau$ . In addition both  $\psi$  and  $\Psi$  are even functions of s.

The main point of this section is to establish the following estimate.

PROPOSITION 2.3. For $y > 1$,

$$
\left\| \Theta_ {B / A} (\phi) \right\| = \int_ {C _ {0} (y)} | \Psi (s) | | d s | ^ {2} = O \left(| \mathscr {L} | \operatorname{Im} \tau + \frac {\exp (- 2 \pi y)}{| \mathscr {L} | ^ {2}}\right).
$$

The proof we present uses an explicit formula, due to Shishikura, which expresses  $\Psi$  as a power series in  $\exp(2\pi is)$ . (Such a series exists because  $\Psi(s)=\Psi(s+1)$ .) The constant term in the series turns out to dominate the behaviour of  $\Psi$  in the region  $C_{0}(y)$ ; the remaining terms are exponentially small, giving the estimate above.

PROPOSITION 3.5. For $s$ with $0 < \operatorname{Im}(s) < \operatorname{Im}(\tau)$,

$$
\Psi (s) = \sum_ {- \infty} ^ {\infty} a _ {n} \exp (2 \pi i n s),
$$

where $a_0 = \mathcal{L} / 6$, and

$$
a _ {n} = \frac {2 \pi^ {2} (n + 4 \pi^ {2} n ^ {3} / \mathscr {L} ^ {2})}{3 (1 - \exp (2 \pi i n \tau))} \quad f o r n \neq 0.
$$

Proof. Recalling that

$$
z = p _ {\Omega} (s) = N \left(\exp (\mathscr {L} s)\right) = 1 / \left(1 - \exp (\mathscr {L} s)\right),
$$

we compute

$$
\psi (s) d s ^ {2} = \left(\frac {d p _ {\Omega}}{d s}\right) ^ {2} d s ^ {2} = \frac {\mathscr {L} ^ {2} \exp (2 \mathscr {L} s)}{(\exp (\mathscr {L} s) - 1) ^ {4}} d s ^ {2} = \frac {\mathscr {L} ^ {2}}{1 6 \sinh (\mathscr {L} s / 2) ^ {4}} d s ^ {2}.
$$

Thus  $\psi(s)$  is analytic away from integral multiples of  $\tau$  (while at such points  $\psi$  has a fourth order pole). Similarly,  $\Psi(s)$  has poles on the lattice  $\Lambda$  and is holomorphic elsewhere; in particular,  $\Psi(s)$  is holomorphic throughout the strip

$$
\{s: 0 <   \operatorname{Im} s <   \operatorname{Im} \tau \}.
$$

Since $\Psi(s + 1) = \Psi(s)$, within this strip $\Psi(s)$ can be expressed as a power series $\sum a_n w^n$ where $w = \exp(2\pi is)$. Moreover, the coefficients $a_n$ can be computed as follows: fixing any $y, 0 < y < \operatorname{Im} \tau$, we have

$$
\begin{array}{r l} a _ {n} & = \int_ {0} ^ {1} \Psi (x + i y) \exp (- 2 \pi i n (x + i y)) d x \\ & = \int_ {- \infty} ^ {\infty} \psi (x + i y) \exp (- 2 \pi i n (x + i y)) d x. \end{array}\tag{3.2}
$$

(This is equivalent to the integral formula for the coefficients of a Laurent series in $w$.)

We claim $a_0 = \mathcal{L} / 6$; this is checked using the indefinite integral

$$
\int \frac {d t}{\sinh^ {4} t} = \frac {\cosh t}{\sinh t} - \frac {1}{3} \left(\frac {\cosh t}{\sinh t}\right) ^ {3}
$$

along with the fact that $\operatorname{Re}(\mathcal{L}) > 0$ (which is our convention for a complex translation length).

For  $n \neq 0$ ,  $a_{n}$  is computed using the residue theorem. Consider a parallelogram  $\gamma_{t}$ , t > 0, with vertices  $iy + t$ ,  $iy - t$ ,  $iy - t - \tau$ ,  $iy + t - \tau$  and counter-clockwise orientation. We claim

$$
(\exp (2 \pi i n \tau) - 1) a _ {n} = \lim _ {t \rightarrow \infty} \int_ {\gamma_ {t}} \psi (s) \exp (- 2 \pi i n s) d s.
$$

To see this, first note that the path integral along the vertical sides of the parallelogram tends to zero by properties of sinh. The part from  $iy + t$  to iy - t tends to  $-a_{n}$  by equation 3.2. Finally the part from  $iy - t - \tau$  to  $iy + t - \tau$  tends to  $\exp(2\pi in\tau)a_{n}$ , since  $\psi(s + \tau) = \psi(s)$ .

On the other hand,

$$
\int_ {\gamma_ {t}} \psi (s) \exp (- 2 \pi i n s) = 2 \pi i \operatorname{Res} (\psi (s) \exp (- 2 \pi i n s), 0)
$$

by the residue theorem. The residue at zero turns out to be

$$
\frac {\pi i}{3} \left(n + \frac {4 \pi^ {2} n ^ {3}}{\mathscr {L} ^ {2}}\right),
$$

and proof is completed by algebra.

COROLLARY 3.6. For $s \in C(y)$, $y > 1$,

$$
\Psi (s) = \frac {\mathscr {L}}{6} + O \left(\frac {\exp (- 2 \pi y)}{| \mathscr {L} | ^ {2}}\right).
$$

Proof. Let $w = \exp(2\pi is)$. By Proposition 3.5, we have $\Psi(s) = \sum a_n w^n$ in the strip $C(y)$, where $a_0 = \mathcal{L}/6$. Thus it suffices to check that

$$
S = \sum_ {n > 0} a _ {n} w ^ {n} + a _ {- n} w ^ {- n} = O \left(\frac {\exp (- 2 \pi y)}{| \mathscr {L} | ^ {2}}\right).
$$

Note that $a_{-n} = \exp(2\pi in\tau)a_n$ (this reflects the symmetry $\Psi(s) = \Psi(\tau - s)$). For $s \in C(y)$, we obtain the bound

$$
\begin{array}{r} a _ {n} w ^ {n} + a _ {- n} w ^ {- n} = a _ {n} \big (\exp (2 \pi i n s) + \exp (2 \pi i n (\tau - s)) \big) \\ = O \big (| a _ {n} | \exp (- 2 \pi n y) \big), \end{array}
$$

since $y$ is a lower bound for both $\operatorname{Im}(s)$ and $\operatorname{Im}(\tau - s)$.

Now assume $\operatorname{Im}(\tau) > 1$ since otherwise $C(y)$ is empty. Then for $n > 0$,

$$
a _ {n} = O \left(\left| n \right| ^ {3} / \left| \mathscr {L} \right| ^ {2}\right).
$$

(For n > 0,

$$
\left| 1 - \exp (2 \pi i n \tau) \right| > 1 - \exp (- 2 \pi)
$$

so that $a_{n} = O(|n| + |n|^{3} / |\mathcal{L}|^{2})$ by Proposition 3.5. But $\operatorname{Im}(\tau) > 1$ implies $1 / |\mathcal{L}| \geq 1 / 2\pi$ and we can ignore the $O(|n|)$ term.)

Since $y > 1$, $r = \exp(-2\pi y) < \exp(-2\pi) < 1$ and so $\sum_{n>0} n^3 r^n = O(r)$. Therefore

$$
S = O \left(\sum_ {n > 0} | a _ {n} | \exp (- 2 \pi n y)\right) = O \left(\frac {1}{| \mathscr {L} | ^ {2}} \sum | n | ^ {3} r ^ {n}\right) = O \left(\frac {\exp (- 2 \pi y)}{| \mathscr {L} | ^ {2}}\right),
$$

as claimed.

Proof of Proposition 3.4. The region $C_0(y)$ is a rectangle of width 1 in the real direction and height at most $\operatorname{Im} \tau$. By the preceding corollary, for $s \in C_0(y)$,

$$
\left| \Psi (s) \right| = O \left(\left| \mathscr {L} \right| + \exp (- 2 \pi y ^ {\prime}) / \left| \mathscr {L} \right| ^ {2}\right)
$$

where $y' = \min(\operatorname{Im} s, \operatorname{Im} \tau - s)$. Integrate this bound over $C_0(y)$.

Proof of Theorem 3.1 (Inefficiency from swirling). The moduli m and M are given by  $m = 4\pi y$  and  $M = 2\pi \operatorname{Im}(\tau)$ . By hypothesis,  $m > 4\pi$ ; this implies y > 1.

By Proposition 3.2, as an element of $Q(B)$,

$$
\| \phi \| \asymp 1 / m ^ {2} | \mathcal {L} | ^ {2}
$$

since integration of $|\phi| = |dz|^2$ over $B$ just gives its area. Then by Proposition 3.4,

$$
\frac {\| \Theta_ {B / A} (\phi) \|}{\| \phi \|}
$$

is of the order

$$
\left(| \mathscr {L} | \operatorname{Im} \tau + \frac {\exp (- 2 \pi y)}{| \mathscr {L} | ^ {2}}\right) m ^ {2} | \mathscr {L} | ^ {2} = O \left(\frac {m ^ {2}}{M ^ {2}} + \frac {m ^ {2}}{\exp (m / 2)}\right),
$$

since $\operatorname{Im} \tau = O(M)$ and $|\mathcal{L}| = O(1/M)$.

Remark. Let

$$
A _ {n} = \left\{ \begin{array}{l l} \sum_ {k} \frac {1}{(n + k \tau) ^ {2}}, & n \neq 0, \\ \sum_ {k} ^ {\prime} \frac {1}{(k \tau) ^ {2}}, & n = 0, \end{array} \right.
$$

where the prime indicates that the k = 0 term is omitted from the second sum.

In terms of the Weierstrass p-function

$$
\mathfrak {p} (s) = \frac {1}{s ^ {2}} + \sum_ {\Lambda} ^ {\prime} \frac {1}{(s - \lambda) ^ {2}} - \frac {1}{\lambda^ {2}},
$$

we may write

$$
\Psi (s) = \frac {1}{\mathscr {L} ^ {2}} \left(\mathfrak {p} (s) ^ {2} - 5 \sum_ {\Lambda} ^ {\prime} \frac {1}{\lambda^ {4}}\right) - \frac {1}{6} \left(\mathfrak {p} (s) + \sum A _ {n}\right).
$$

Our original proof of Proposition 3.4 takes this expression as its point of departure.

## 4. Organizing the sphere at infinity

This section analyzes the intersections between various  $B(\gamma)$  for  $\gamma \in \Gamma_{\gamma}$ . The idea is to organize the support of a  $\Gamma_{\gamma}$ -invariant deformation  $\mu$  into various disjoint regions, each stabilized by a particular group element, on which a definite inefficiency is apparent by the results of the preceding section. The argument rests on the disjointness of Margulis tubes about short geodesics.

A simpler covering argument would lead to the bound  $O(L^{\alpha})$  in Theorem 1.2, which is sufficient for all the qualitative corollaries we derive in the introduction. On the other hand, by finding disjoint regions we are able to exploit the full power of Theorem 3.1 (Inefficiency from swirling), leading to a bound which is close to sharp.

## 4.1. Tubes and shadows.

Definitions. There is a universal constant  $\varepsilon_{0}$  (the Margulis constant for hyperbolic space) such that any two nontrivial loops through the same point in a hyperbolic 3-manifold generate an abelian subgroup of  $\pi_{1}$  (see, e.g., [T1, §5.10]).

Let  $\gamma$  be a hyperbolic isometry. The Margulis tube for  $\gamma$  is the set of points in hyperbolic space such that the hyperbolic distance  $d(x, \gamma^{n}x) < \varepsilon_{0}$  for some n > 0; this defines a cylinder enclosing the geodesic g stabilized by  $\gamma$ .

If  $\gamma$  and  $\delta$  lie in a discrete group and stabilize distinct geodesics, their Margulis tubes are disjoint.

In general, a tube of radius r for  $\gamma$  will mean the set of points in  $H^{3}$  at distance at most r from the geodesic g.

Given any two sets E, F in  $H^{3} \cup \hat{C}$ , define the shadow of E from F as the set of endpoints of all geodesic rays which initiate in F and pass through E. For example, the shadow of E from  $\infty \in \hat{C}$  is its orthogonal projection onto C in the

upper half-space model  $(\mathbf{H}^{3}=\{(z,t):z\in\mathbf{C},t>0\}$ , with the metric  $(|dz|^{2}+dt^{2})/t^{2})$ .

PROPOSITION 4.1. Let $B = B(\gamma, \mathcal{L}, m; p)$. Then there is an $r$-tube $\tau$ for $\gamma$, where $r = r(\mathcal{L}, m)$ is independent of $p$, such that

1. The shadow of $S$ of $\tau$ from $p$ contains a $\mathrm{diam}_p(B')$ neighborhood of the larger twisted spiral $B' = B(\gamma, \mathcal{L}, m/2, p)$.

2. S itself has diameter $O(\mathrm{diam}_p(B))$.

3. Any point at distance  $(\log m) - O(1)$  from  $\tau$  is contained in the Margulis tube for  $\gamma$ .

Proof. Let

$$
r = \dot {C} + \log (1 / | m _ {\mathcal {L}} |);
$$

we claim (1-3) hold if we fix $C$ sufficiently large. (Remark: $|m\mathcal{L}| = O(1)$ so that $r > 0$ for $C$ large.)

1. In the coordinate $z$ of subsection 3.1, $g$ is the geodesic joining 0 and 1, which contains the point $P = (1/2, 1/2)$ in the upper half-space model. For $r$ large, the $r$-tube about $g$ contains an $r$-ball about $P$ which projects to a Euclidean disk in $\mathbf{C}$, centered at $z = 1/2$ and of radius $\asymp \exp(r) = \exp(C)/|m\mathcal{L}| \asymp \exp(C)\mathrm{diam}(B')$ by Proposition 3.2. This projection is contained in the shadow of $\tau$, so that (1) follows for any $C$ sufficiently large. Fix $C$ large enough that (1) holds.

2. On the other hand, any point at distance $r$ from $g$ is at 'distance $O(\exp(r))$ from (0, 0) in the Euclidean metric $|dz|^2 + dt^2$; so the entire shadow of $\tau$ has diameter $O(\mathrm{diam}_p(B))$.

3. Let $x$ be at distance $R$ from $g$. Then the hyperbolic distance from $x$ to $\gamma(x)$ is at most

$$
\theta \sinh (R) + \ell \exp (R) \leq 2 | \mathscr {L} | \exp (R)
$$

(where $\mathcal{L} = \ell + i\theta$). If $x$ is at distance less than $\log(m) - D$ from $\tau$, then

$$
R \leq r + \log (m) - D = C - D + \log (1 / | \mathscr {L} |),
$$

so that  $d(\gamma x, x) \leq 2 \exp(C - D)$ , which is less than the Margulis constant  $\varepsilon_{0}$  for D sufficiently large. Therefore any point at distance  $\log(m) - O(1)$  from  $\tau$  is still contained in the Margulis tube for  $\gamma$ .

Remark. When r is large, an r-tube for  $\gamma$  is well-approximated (in the upper half-space picture) by a horoball resting on one of the fixed points of  $\gamma$ .

## 4.2. Scattered sets.

Definitions. Let S be a collection of nonempty open sets in a metric space. S is  $\alpha$ -scattered if for distinct  $S, S' \in S$ ,

$$
d (S, S ^ {\prime}) \leq \operatorname{diam} (S) \Rightarrow \frac {\operatorname{diam} (S)}{\operatorname{diam} (S ^ {\prime})} \text { is } <   \alpha \text { or } > 1 / \alpha ,
$$

where $0 < \alpha < 1$. Here $d(S, S')$ denotes the minimum distance between points in $S$ and $S'$. Intuitively, nearby sets have disproportionate size.

When S is scattered,  $\cup S$  tends to be disconnected; any connected component of the union is dominated by a single member.

THEOREM 4.2 (Scattered domination). Let S be α-scattered, with ∪ S a connected bounded set. Then for α < 1/3, ∪ S is contained in a  $3\alpha \times \text{diam}(S_{0})$  neighborhood of some single  $S_{0} \in S$ .

Proof. Choose $S_0$ so that $\mathrm{diam}(S_0) > \sup_{\mathcal{S}} \mathrm{diam}(S)/2$.

Since $\bigcup \mathcal{S}$ is connected, for any $S \in \mathcal{S}$ there is a finite chain $S_0, S_1, \ldots, S_n = S$ of distinct sets with $S_i \cap S_{i+1}$ nonempty.

Let $d_k = \text{diam}(S_k)$. Then $(d_0, d_1, \ldots, d_n)$ satisfy the following:

Size conditions:

1. $2d_{0} \geq d_{k} > 0$ for all $k$;

2. Whenever $\sum_{i < k < j} d_k \leq d_i$ or $d_j$, the ratio $d_i / d_j$ is less than $\alpha$ or greater than $1 / \alpha$.

LEMMA 4.3. For $\alpha < 1/3$, the size conditions imply

$$
\sum_ {1} ^ {n} d _ {k} \leq d _ {0} \left(\sum_ {1} ^ {n} 2 ^ {k - 1} \alpha^ {k}\right) <   3 \alpha d _ {0}.
$$

This lemma will complete the proof, since the sum above bounds the distance from  $S_{0}$  to any point in  $S_{n}$ .

Proof of the lemma. The proof is by induction on n, n = 0 being trivial. Assume the lemma holds up to n. Let  $(d_{0}, \ldots, d_{n+1})$  satisfy the size conditions. Applying the lemma for n we have

$$
\sum_ {1} ^ {n} d _ {k} <   d _ {0} \quad (\text { since } \alpha <   1 / 3);
$$

by condition (2) $d_k < \alpha d_0$ for $k = 1, \ldots, n + 1$ (it cannot be $>d_0 / \alpha$ by condition (1)).

Let $d_{i}$ achieve the maximum of $(d_{1},\ldots ,d_{n + 1})$. The sequences $(d_i,d_{k + 1},\dots ,d_{n + 1})$ and $(d_i,d_{i - 1},\dots ,d_1)$ satisfy the size conditions; applying

the lemma to each one gives the bound

$$
\sum_ {1} ^ {n + 1} d _ {k} \leq d _ {i} + 2 d _ {i} \left(\sum_ {1} ^ {n} 2 ^ {k - 1} \alpha^ {k}\right) \leq d _ {0} \left(\sum_ {1} ^ {n + 1} 2 ^ {k - 1} \alpha^ {k}\right)
$$

since $d_{i} < \alpha d_{0}$.

$$
\text {   Finally   } d _ {0} \Sigma_ {1} ^ {\infty} 2 ^ {k - 1} \alpha^ {k} = d _ {0} \alpha / (1 - 2 \alpha) <   3 \alpha d _ {0} \text {   for   } \alpha <   1 / 3.
$$

Examples. Scattered sets arise naturally as shadows in hyperbolic geometry. Let B be a collection of unit balls in hyperbolic space. Assume the hyperbolic distance between distinct balls in B is at least D. Let S denote the collection of shadows from  $\infty \in \hat{C}$  of balls in B. Then for D large, S is an  $\alpha$ -scattered collection of subsets of C, where  $\alpha = O(\exp(-D))$  (see Figure 4).

![](images/page_23_image_5.jpg)

FIGURE 4. Shadows of disjoint hyperbolic balls.

We will show that the shadows of distant tubes (cylinders about geodesics) are also scattered. Let  $x \in H^{3}$ . The visual metric from x is the metric on  $\hat{C}$  given by  $d(y, z) = \rho(\gamma y, \gamma z)$ , where  $\rho$  is the usual spherical metric on  $\hat{C}$  and  $\gamma$  is any hyperbolic isometry moving x to the center of the sphere.

For any tube  $\tau$  about a geodesic g, we refer to the endpoints of g on the sphere at infinity as the ends of the tube.

PROPOSITION 4.4. Let $\tau_{i}$ be a collection of tubes in hyperbolic space. Assume that the hyperbolic distance $d(\tau_{i},\tau_{j}) > D$ for all $i\neq j$. Then there is a function $\alpha (D)\to 0$ as $D\to \infty$ such that:

1. The shadows  $S_{i}$  of  $\tau_{i}$  from infinity are  $\alpha(D)$ -scattered in the Euclidean metric on C (assuming infinity is not the end of any tube).

2. The shadows $S_{i}^{\prime}$ of $\tau_{i}$ from $\tau_{0} (i \neq 0)$ are $\alpha(D)$-scattered in the visual metric from $x$, where $x$ is a point of $\tau_{0}$.

Proof. 1. In the upper half-space model, the height of any tube is comparable to the diameter of its shadow; i.e., $\tau_{i}$ contains a point $x_{i} = (z_{i}, t_{i})$

with $t_i \asymp \text{diam}(S_i)$. Consider two distinct tubes $\tau_i, \tau_j$; we may assume $1 = \text{diam}(S_i) \geq \text{diam}(S_j)$. If $d(S_i, S_j) < 1$, then $|z_i - z_j| < 3$. But the hyperbolic distance $d(x_i, x_j) > D$, so that $t_j / t_i$ must be small (about $\exp(-D)$); therefore $\text{diam}(S_j) \asymp t_j < \alpha(D)\text{diam}(S_i)$ where $\alpha(D) \to 0$ as $D \to \infty$.

2. This follows from (1) by a limiting argument. Normalize so that $x$ is at the center of the hyperbolic ball. As $D \to \infty$, the spherical (= visual) $\mathrm{diam}(S_i') < \delta(D) \to 0$. Let $S_i', S_j'$ be shadows of distinct tubes separated by a spherical distance no greater than the diameter of the larger shadow. Then both shadows are contained in a ball $U$ of radius $3\delta(D)$.

Let $p$ denote the shadow of $x$ from some point in $U$; then $p$ is approximately antipodal to $U$. Since the spherical metric is nearly flat on the scale of $U$, there is an affine coordinate $z_p$ with $z_p(p) = \infty$, such that the $|z_p|$ metric nearly matches the spherical metric on $U$. Moreover the shadows $S_i''$ of $\tau_i$ from $p$ are nearly the same as the shadows $S_i'$ from $\tau_0$. The result then follows from part (1) when $p$ is the point at infinity.

4.3. Finding an invariant partition. Let $\Gamma$ be a discrete torsion-free Kleinian group.

Start with a collection $\mathcal{G}$ of distinct oriented closed geodesics in $\mathbf{H}^3/\Gamma$, and a compatible complex translation length $\mathcal{L}(g)$ for each $g \in \mathcal{G}$.

For each geodesic  $g_{i}$  in  $H^{3}$  that lies over an element of G, let  $\gamma_{i}$  denote the generator of its stabilizer corresponding to the choice of orientation. Let  $L_{i}$  denote the corresponding complex translation length.

Different $\gamma_{i}$ stabilize different geodesics. If $\gamma$ is a conjugate of $\gamma_{i}$ in $\Gamma$, then $\gamma = \gamma_{j}$ for some $j$.

Let

$$
M = \inf 4 \pi^ {2} \operatorname{Re} (1 / \mathscr {L} _ {i})
$$

be a uniform lower bound for the modulus of a cylinder embedded in the  $L_{i}$ -homotopy class on the quotient torus for  $\gamma_{i}$ .

Given  $p \in \hat{C}$  distinct from the fixed points of all  $\gamma_{i}$ , and m > 0 with m < M, form the collection of thickened spirals

$$
B _ {i} = B \big (\gamma_ {i}, \mathcal {L} _ {i}, m, p \big)
$$

as in the preceding section.

THEOREM 4.5 (Invariant partition). Assume $\bigcup B_{i}$ is bounded. For $m$ sufficiently large, there is a subsequence of group elements $\gamma_{j}$ and disjoint $\gamma_{j}$-invariant

regions $E_{j}$ such that

$$
\begin{array}{c} B \big (\gamma_ {j}, \mathscr {L} _ {j}, m, p \big) \subset E _ {j} \subset B \big (\gamma_ {j}, \mathscr {L} _ {j}, m / 2, p \big) \text { and } \\ \bigcup B _ {i} \subset \bigcup E _ {j}. \end{array}
$$

Proof. We begin with some notation. Let  $\tau_{i}$  denote the tube associated to  $B_{i}$  by Proposition 4.1; recall that  $\tau_{i}$  does not depend on p. Let  $T_{i}$  be the shadow of  $\tau_{i}$  from p, and for  $i \neq j$, let  $S_{ij}$  be the shadow of  $\tau_{j}$  from  $\tau_{i}$. Let  $x_{i}$  denote the point of  $\tau_{i}$  closest to p (i.e. of maximum height in the upper half-space model with p at infinity). Finally let  $B_{i}'$  denote the larger thickened spiral  $B(\gamma_{i}, \mathcal{L}_{i}, m/2, p)$.

Note that the visual metric from  $x_{i}$  and the metric  $|z_{p}|$  are quasi-similar on  $T_{i}$ ; that is, ratios of distances are approximately the same in both metrics. Moreover the visual diameter of  $B_{i}$  is > c > 0.

Here is the idea of the proof. One might try to construct regions  $E_{i}$  as follows: (a) pick a large  $B_{i}$, (b) adjoin to it all the  $B_{j}$  which meet it (each of which has much smaller diameter), (c) add in those  $B_{k}$  which meet the result, and continue, creating a cluster  $E_{i}$  hopefully not much larger than the original  $B_{i}$.

The problem with this construction is that the  $B_{j}$  are not  $\gamma_{i}$ -invariant, since p is not  $\gamma_{i}$ -invariant. To remedy this, we replace  $B_{j}$  with the shadow  $S_{ij}$ . Then  $\gamma_{i}(S_{ij}) = S_{ik}$ , where  $\gamma_{k} = \gamma_{i}\gamma_{j}\gamma_{i}^{-1}$ .

Let $E_{i}$ be the union of $B_{i}$ and those components of $\bigcup_{j\neq i}S_{ij}$ which meet $B_{i}$. By the preceding remark, $E_{i}$ is $\gamma_{i}$-invariant.

For $m$ sufficiently large, $E_{i} \subset B_{i}^{\prime}$.

Indeed, by Proposition 4.1 and disjointness of Margulis tubes, the hyperbolic distance between distinct $\tau_{i}$ is $\log(m)-O(1)$. By Proposition 4.4, the shadows $S_{ij}$ for fixed $i$ and varying $j$ are $\alpha(m)$-scattered in the visual metric from $x_{i}$, where $\alpha(m)\to0$ as $m\to\infty$. It follows by Theorem 4.2 (Scattered domination) that the visual diameter of any component of $\bigcup S_{ij}$ is approximately that of some single shadow $S_{ik}$. But for $m$ large any single shadow has small visual size; so $E_{i}$ is contained in an $r$-neighborhood of $B_{i}$ where $r$ is small compared to the visual diameter of $B_{i}$. Near $B_{i}$, ratios of lengths are approximately the same in the visual metric and the $|z_{p}|$ metric, and since $E_{i}$ is $\gamma_{i}$-invariant, by Proposition 3.3 we have $E_{i}\subset B_{i}^{\prime}$.

If $E_{i}$ meets $E_{k}$, then $E_{i}$ contains $E_{k}$ or vice-versa.

For suppose $E_{i}$ meets $E_{k}$; then $B_{i}'$ meets $B_{k}'$. Assume $\text{diam}_p(B_i') \geq \text{diam}_p(B_k')$; then by Proposition 4.1, $B_{k}' \subset T_{i}$; so $E_{k}$ lies in the shadow of $\tau_{i}$ from $p$. Any ray from $p$ to $E_{k}$ passes through both $\tau_{i}$ and $\tau_{k}$ (since $E_{k} \subset B_{k}' \subset T_{k}$), whence $E_{k} \subset S_{ik}$. Now by the definition of $E_{i}$, any $S_{ij}$ which meets $E_{i}$ is contained in $E_{i}$, and therefore $E_{k} \subset S_{ik} \subset E_{i}$.

Now let  $\langle E_{j}\rangle$  be the subsequence of maximal elements of the collection  $\langle E_{i}\rangle$  (with respect to inclusion). By assumption  $\cup B_{i}$  is bounded and so every  $E_{i}$  is contained in a maximal element. (For m small, no pair of nested  $E_{i}$ 's have comparable diameter and so there is no infinite ascending chain.)

Since  $E_{i} \supset B_{i}$ , these  $E_{j}$  give a disjoint cover of  $\cup B_{i}$ , and we have seen they satisfy the remaining conditions of the theorem. ☐

## 5. Quasifuchsian groups

We return to the setting of Bers' embedding. Let $\gamma \in \Gamma_Y$ be a hyperbolic element with fixed points $F$. Then $\gamma$ determines closed geodesics $\gamma_{\overline{X}}$ and $\gamma_Y$ on $\overline{X}$ and $Y$; let $L_{\overline{X}}$ and $L_Y$ denote their lengths in the respective Poincaré metrics.

Remove the fixed points F of  $\gamma$  and form the torus  $T = (\hat{\mathbf{C}} - F)/\gamma$ . The limit set  $\Lambda$  of  $\Gamma_{Y}$  descends to a pair of simple closed curves on T, separating it into a pair of annuli  $A_{\overline{X}}$  and  $A_{Y}$  which are the covering spaces of  $\overline{X}$  and Y corresponding to the cyclic group  $\langle\gamma\rangle$  (Figure 5).

![](images/page_26_image_5.jpg)

FIGURE 5. Quotient torus for a short geodesic.

The homotopy class of these annuli determines the complex translation length  $\mathcal{L}(\gamma)$ . To compute L concretely, choose coordinates so that  $\gamma(z)=\lambda z$ ,  $|\lambda|>1$ , and  $1\in\Lambda$ . Then  $\mathcal{L}=\log\lambda$  is the value obtained by analytic continuation of the logarithm from 1 to  $\lambda$  along  $\Lambda$ , starting with  $\log(1)=0$ .

The following two propositions are well-known.

PROPOSITION 5.1. The moduli of $A_{\overline{X}}$ and $A_{Y}$ are given by

$$
\operatorname{mod} \left(A _ {\bar {X}}\right) = \frac {2}{L _ {\bar {X}}}, \quad \operatorname{mod} \left(A _ {Y}\right) = \frac {2}{L _ {Y}};
$$

and it follows that

$$
2 \operatorname{Re} 1 / \mathscr {L} \geq \frac {1}{L _ {\bar {X}}} + \frac {1}{L _ {Y}}.
$$

Proof. This uses an extremal length argument; see [Mc, §6.3], [Be3, Th. 3].

PROPOSITION 5.2. 1. An annulus $A \subset C$ separating 0 from $\infty$ contains a Euclidean annulus

$$
B = \{z: r <   | z | <   R \}
$$

with $\operatorname{mod}(B) = \operatorname{mod}(A) - O(1)$.

2. An essential annulus A in a torus T contains a right cylinder B with  $\text{mod}(B) = \text{mod}(A) - O(1)$ .

Proof.

1. Taking r as small as possible and R as large as possible, we have that A separates the pair  $\{0, z_{1}\}$  from  $\{z_{2}, \infty\}$  where  $|z_{1}| = r$ ,  $|z_{2}| = R$ . By a theorem of Teichmüller and estimates of the Grötzsch modulus (see [LV, II.1.3, II.2.3]), the modulus of A is at most  $\log(R/r) + O(1)$ , while the modulus of B is simply  $\log(R/r)$ .

2. Apply the first part to the lift of A to the  $\pi_{1}(A)$ -covering space of T (which can be identified with C\*).

Proof of 1.2 (Short geodesics pinch quickly). Let $\mu$ be a unit norm Beltrami differential supported in the part of $Y$ of injectivity radius less than $L < 1/2$. By Theorem 2.6, we may assume $\mu$ is supported in the geodesic thin part $Y(L, \text{geod})$, since the contribution from the cuspidal thin part is of order $\exp(-1/L) = O(L^2)$.

The lift of $\mu$ to $\Omega(Y)$ is a $\Gamma_{Y}$-invariant form which we continue to denote by $\mu$.

Let $p$ be any point in $\Omega(\overline{X})$, $z_p$ an affine coordinate such that $p$ is at infinity.

Let G denote those geodesics in  $H^{3}/\Gamma_{Y}$  which correspond to geodesics of length less than L on Y. Orient the elements of G (in any way). Each geodesic g has a natural complex translation length  $\mathcal{L}(g)$ . By Proposition 5.1,

$$
M = 2 \pi^ {2} / L \leq 4 \pi^ {2} \operatorname{Re} \left(1 / \mathscr {L} (g)\right)
$$

is a lower bound for the modulus of a cylinder on the quotient torus in the homotopy class determined by $\mathcal{L}(g)$.

Let

$$
m = 8 \log (1 / L).
$$

Then $m < M$ for $L$ large enough; in fact, this already holds under our assumption that $L < 1/2$.

Form the collection $B_{i} = B(\gamma_{i}, \mathcal{L}_{i}, m, p)$ corresponding to $\mathcal{G}, \mathcal{L}(g)$ as in subsection 4.3. For each $i, B_{i}$ lies over an annulus $A_{i}$ on the quotient torus $T_{i}$.

Since $\| d\beta \| = O(1)$, the bound

$$
\left\| d \beta (\mu) \right\| = O \left(\left(L \log 1 / L\right) ^ {2}\right)
$$

need only be verified for all L sufficiently small. Note that as L tends to zero, m and M tend to infinity but  $m \ll M$ .

LEMMA 5.3. For all $L$ sufficiently small:

1. The support of $\mu$ is contained in $\bigcup B_{i}$.

$$
2. \frac {\operatorname{area} _ {p} (\bigcup B _ {i})}{\operatorname{diam} _ {p} (\Lambda) ^ {2}} = O (1 + 1 / \operatorname{short} (X) ^ {2}),
$$

where short(X) denotes the length of the shortest geodesic on X.

Proof. 1. If z lies in the support of  $\mu$ , then there is a hyperbolic  $\gamma_{i}$  translating z distance less than L in the Poincaré metric on  $\Omega(Y)$ . To see if z lies in  $B_{i}$ , it suffices to check that  $A_{i}$  contains  $A_{Y}(L)$ , the L-thin part of the annulus  $A_{Y} = \Omega(Y)/\langle\gamma_{i}\rangle$ . But for small L, there are a pair of right cylinders of modulus  $\asymp 1/L$  separating the L-thin part from the image of p on  $T_{i}$ , by Proposition 5.2. Since  $m \ll 1/L$ ,  $A_{Y}(L)$  does not meet an annulus of modulus m centered at the image of p and so it is contained in  $A_{i}$ .

2. The modulus of the annulus $A_{\overline{X}}$ is at most $2 / \text{short}(X)$, so that it does not contain an annulus of modulus $m' = 1 + 2 / \text{short}(X)$. Consequently $B' = B(\gamma_i, \mathcal{L}_i, m', p)$ does not contain the entire limit set. Since $\Lambda - B'$ is $\gamma_i$-invariant,

$$
\operatorname{diam} _ {p} \left(B ^ {\prime}\right) = O \left(\operatorname{diam} _ {p} (\Lambda)\right),
$$

by Proposition 3.3, and $\mathrm{diam}_p(B_i) \asymp (m' / m)\mathrm{diam}_p(B')$, by Proposition 3.2. For $L$ sufficiently small, $m$ is at least 1 and so we arrive at the estimate

$$
\operatorname{diam} _ {p} (B _ {i}) = O \big ((1 + 1 / \operatorname{short} (X)) \operatorname{diam} _ {p} (\Lambda) \big).
$$

But every $B_{i}$ meets the limit set and thus the same bound holds for $\mathrm{diam}_p(\bigcup B_i)$. Now bound the area by the square of the diameter.

For L sufficiently small, we may apply Theorem 4.5 (Invariant partition) to obtain a covering of  $\cup B_{i}$  by disjoint sets  $E_{j}$ . For each j, there exist a  $\gamma, L$  among the original  $\langle\gamma_{i},\mathscr{L}_{i}\rangle$  with  $\gamma(E_{j})=E_{j}$  and

$$
B (\gamma , \mathscr {L}, m, p) \subset E _ {j} \subset B (\gamma , \mathscr {L}, m / 2, p) =: B.
$$

The $Q(B)$-norm

$$
\left\| d z _ {p} ^ {2} \right\| = \operatorname{area} _ {p} (B) \asymp \operatorname{area} _ {p} \left(E _ {j}\right)
$$

since changing $m / 2$ to $m$ alters the area of $B(\gamma, \mathcal{L}, m, p)$ by a bounded factor.

The restriction  $\nu$  of  $\mu$  to  $E_{j}$  is a unit-norm  $\gamma$ -invariant form. Applying Theorem 3.1 (Inefficiency from swirling) with  $m = 4\log(1/L)$  and  $M > 2\pi^{2}/L$ , we find

$$
\left| \int_ {E _ {j}} \mu (z _ {p}) | d z _ {p} | ^ {2} \right| = \left| \int_ {B} \nu (z _ {p}) | d z _ {p} | ^ {2} \right| \leq \left\| \Theta_ {B / A} (d z _ {p} ^ {2}) \right\| \leq O ((L \log 1 / L) ^ {2} \text {area} _ {p} (E _ {j})).
$$

As the $E_{j}$ are disjoint and cover the support of $\mu$, the above implies a bound for $|\int \mu (z_p)|dz_p|^2|$ in terms of the area$_p(\bigcup E_j)\asymp$ area$_p(\bigcup B_i)$. We find

$$
\begin{array}{r l} \frac {1}{\operatorname{diam} _ {p} (\Lambda) ^ {2}} \left| \int \mu (z _ {p}) | d z _ {p} | ^ {2} \right| & = O \left((L \log 1 / L) ^ {2} \frac {\operatorname{area} _ {p} (\bigcup B _ {i})}{\operatorname{diam} _ {p} (\Lambda) ^ {2}}\right) \\ & = O \Big ((L \log 1 / L) ^ {2} \big (1 + 1 / \operatorname{short} (X) ^ {2} \big) \Big) \end{array}
$$

by part (2) of Lemma 5.3.

This inequality is independent of p, so it provides a bound for  $\left\|d\beta(\mu)\right\|$  by Theorem 2.2. □

PRINCETON UNIVERSITY, PRINCETON, NEW JERSEY

## REFERENCES

[Ab1] W. ABIKOFF, On boundaries of Teichmüller spaces and on Kleinian groups: III, Acta. Math. 134 (1975), 211–237.

[Ab2] \_\_\_\_, Degenerating families of Riemann surfaces, Ann. of Math. 105 (1977), 29–44.

[Ah] L. AHLFORS, Conformal Invariants: Topics in Geometric Function Theory, McGraw-Hill Book Co., 1973.

[AB] L. AHLFORS and L. BERS, Riemann's mapping theorem for variable metrics, Ann. of Math. 72 (1960), 385–404.

[BP] A. BEARDON and C. POMMERENKE, The Poincaré metric of plane domains, J. Lond. Math. Soc. 18 (1978), 475–483.

[Be1] L. BERS, Simultaneous uniformization, Bull. AMS 66 (1960), 94–97.

[Be2] \_\_\_\_, A non-standard integral equation with applications to quasiconformal mappings, Acta Math. 116 (1966), 113–134.

[Be3] \_\_\_\_, On boundaries of Teichmüller spaces and on kleinian groups: I, Ann. of Math. 91 (1970), 570–600.

[Be4] \_\_\_\_, Spaces of Kleinian groups, in Several Complex Variables I, Maryland 1970, pages 9–34. Springer Lecture Notes in Math. 155, 1970.

[Be5] \_\_\_\_, Holomorphic families of isomorphisms of Möbius groups, J. of Math. of Kyoto Univ. 26 (1986), 73–76.

[Bo] F. BONAHON, Bouts des variétés hyperboliques de dimension 3, Ann. of Math. 124 (1986), 71–158.

[BO] F. BONAHON and J. P. OTAL, Variétés hyperboliques à géodésiques arbitrairement courtes. Bull. London Math. Soc. 20 (1988), 255–261.

[E] L. EHRENPREIS, Holes in moduli spaces, in Proc. Conf. Quasi-Conformal Mappings, Moduli and Discontinuous Groups, pages 30–38, Tulane Univ., 1965.

[G] F. GARDINER, Teichmüller Theory and Quadratic Differentials, Wiley Interscience, 1987.

[H] D. A. HEJHAL, Regular $b$-groups and repeated Dehn twists, in Complex Analysis, Joensuu 1987, pages 169-192, Springer-Verlag Lecture Notes in Math. 1351, 1988.

[KT] S. KERCKHOFF and W. THURSTON, Non-continuity of the action of the modular group at Bers' boundary of Teichmüller space, Inv. Math. 100 (1990), 25–48.

[LV] O. LEHTO and K. J. VIRTANEN, Quasiconformal Mappings in the Plane, Springer-Verlag, 1973.

[Mar] A. MARDEN, Geometric relations between homeomorphic Riemann surfaces, Bull. AMS 3 (1980), 1001–1017.

[Mas1] B. Maskit, On boundaries of Teichmüller spaces and on kleinian groups: II. Ann. of Math. 91 (1970), 607–639.

[Mas2] \_\_\_\_, Self mappings of Kleinian groups, Amer. J. Math. 93 (1971), 840–856.

[Mc] C. McMULLEN, Iteration on Teichmüller space, Invent. Math. 99 (1990), 425-454.

[N] Z. NEHARI, Schwarzian derivatives and schlicht functions, Bull. AMS 55 (1949), 545–551.

[P] H. POINCARE, Mémoire sur les fonctions Fuchsiennes, Acta Math. 1 (1882/3), 193–294.

[Sh] H. SHICA, On analytic and geometric properties of Teichmüller spaces, J. Math. Kyoto Univ. 24 (1984), 441–452.

[Su1] D. SULLIVAN, On the ergodic theory at infinity of an arbitrary discrete group of hyperbolic motions, in Riemann Surfaces and Related Topics: Proc. 1978 Stony Brook Conf., Ann. of Math. Studies 97, Princeton, 1981.

[Su2] \_\_\_\_, Quasiconformal homeomorphisms and dynamics II: Structural stability implies hyperbolicity for Kleinian groups, Acta Math. 155 (1985), 243–260.

[Su3] \_\_\_\_, Quasiconformal homeomorphisms and dynamics III: Topological conjugacy classes of analytic endomorphisms, preprint.

[T1] W. P. THURSTON, Geometry and topology of three-manifolds, Princeton lecture notes, 1979.

[T2] \_\_\_\_, Zippers and univalent functions, in A. Baernstein et al., editors, The Bierberbach Conjecture, pages 185–197. AMS, 1986.

[T3] \_\_\_\_, Hyperbolic structures on 3-manifolds II: Surface groups and 3-manifolds which fiber over the circle, accepted by Ann. of Math., 1987.

[W] D. WRIGHT, The shape of the boundary of Maskit's embedding of the Teichmüller space of once-punctured tori, preprint.

[Y] A. YAMADA, On Marden's universal constant of Fuchsian groups, Kodai Math. J. 4 (1981), 266–277.

(Received May 16, 1989)