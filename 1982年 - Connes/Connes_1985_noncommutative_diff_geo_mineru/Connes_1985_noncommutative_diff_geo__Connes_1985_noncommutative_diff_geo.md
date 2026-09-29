ALAIN CONNES

Non-commutative differential geometry

Publications mathématiques de l'I.H.É.S., tome 62 (1985), p. 41-144

&lt;http://www.numdam.org/item?id=PMIHES_1985__62__41_0&gt;

© Publications mathématiques de l'I.H.É.S., 1985, tous droits réservés.

L'accès aux archives de la revue « Publications mathématiques de l'I.H.É.S. » (http://www.ihes.fr/IHES/Publications/Publications.html) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

# NON-COMMUTATIVE DIFFERENTIAL GEOMETRY by ALAIN CONNES

## Introduction

This is the introduction to a series of papers in which we shall extend the calculus of differential forms and the de Rham homology of currents beyond their customary framework of manifolds, in order to deal with spaces of a more elaborate nature, such as,

a) the space of leaves of a foliation,

b) the dual space of a finitely generated non-abelian discrete group (or Lie group),

c) the orbit space of the action of a discrete group (or Lie group) on a manifold.

What such spaces have in common is to be, in general, badly behaved as point sets, so that the usual tools of measure theory, topology and differential geometry lose their pertinence. These spaces are much better understood by means of a canonically associated algebra which is the group convolution algebra in case b). When the space V is an ordinary manifold, the associated algebra is commutative. It is an algebra of complex-valued functions on V, endowed with the pointwise operations of sum and product.

A smooth manifold V can be considered from different points of view such as

α) Measure theory (i.e. V appears as a measure space with a fixed measure class),

β) Topology (i.e. V appears as a locally compact space),

γ) Differential geometry (i.e. V appears as a smooth manifold).

Each of these structures on V is fully specified by the corresponding algebra of functions, namely:

$\alpha)$ The commutative von Neumann algebra $\mathbf{L}^{\infty}(\mathbf{V})$ of classes of essentially bounded measurable functions on $\mathbf{V}$,

β) The C\*-algebra  $C_{0}(V)$  of continuous functions on V which vanish at infinity,

$\gamma)$ The algebra $\mathbf{C}_c^\infty (\mathbf{V})$ of smooth functions with compact support.

It has long been known to operator algebraists that measure theory and topology extend far beyond their usual framework to

A) The theory of weights and von Neumann algebras,

B) C\*-algebras, K-theory and index theory.

Let us briefly discuss these two fields,

## A) The theory of weights and von Neumann algebras

To an ordinary measure space  $(\mathbf{X}, \mu)$  correspond the von Neumann algebra  $\mathbf{L}^{\infty}(\mathbf{X}, \mu)$  and the weight  $\varphi$ :

$$
\varphi (f) = \int_ {\mathbf {X}} f d \mu \quad \forall f \in \mathbf {L} ^ {\infty} (\mathbf {X}, \mu) ^ {+}.
$$

Any pair  $(M, \varphi)$  of a commutative von Neumann algebra M and weight  $\varphi$  is obtained in this way from a measure space  $(X, \mu)$ . Thus the place of ordinary measure theory in the theory of weights on von Neumann algebras is similar to that of commutative algebras among arbitrary ones. This is why A) is often called non-commutative measure theory.

Non-commutative measure theory has many features which are trivial in the commutative case. For instance to each weight $\varphi$ on a von Neumann algebra M corresponds canonically a one-parameter group $\sigma_{i}^{\varphi}\in\mathrm{Aut}\;\mathbf{M}$ of automorphisms of M, its modular automorphism group. When M is commutative, one has $\sigma_{i}^{\varphi}(x)=x,\;\forall\;t\in\mathbf{R},\;\forall\;x\in\mathbf{M},$ and for any weight $\varphi$ on M. We refer to [17] for a survey of non-commutative measure theory.

## B) C\*-algebras, K-theory and index theory

Gel'fand's theorem implies that the category of commutative $\mathbf{C}^*$-algebras and $*$-homomorphisms is dual to the category of locally compact spaces and proper continuous maps.

Non-commutative C\*-algebras have first been used as a tool to construct von Neumann algebras and weights, exactly as in ordinary measure theory, where the Riesz representation theorem [60], Theorem 2.14, enables to construct a measure from a positive linear form on continuous functions. In this use of C\*-algebras the main tool is positivity. The fine topological features of the “space” under consideration do not show up. These fine features came into play thanks to Atiyah’s topological K-theory [2]. First the proof of the periodicity theorem of R. Bott shows that its natural set up is non-commutative Banach algebras (cf. [71]). Two functors  $K_{0}$ ,  $K_{1}$  (with values in the category of abelian groups) are defined and any short exact sequence of Banach algebras gives rise to an hexagonal exact sequence of K-groups. For  $A = C_{0}(X)$ , the commutative C\*-algebra associated to a locally compact space X,  $K_{j}(A)$  is (in a natural manner) isomorphic to  $K^{j}(X)$ , the K-theory with compact supports of X.

Since (cf. [65]) for a commutative Banach algebra B,  $\mathbf{K}_{j}(\mathbf{B})$  depends only on the Gel'fand spectrum of B, it is really the  $C^{*}$ -algebra case which is most relevant.

Secondly, Brown, Douglas and Fillmore have classified (cf. [11]) short exact sequences of $\mathbf{C}^*$-algebras of the form

$$
0 \rightarrow \mathcal {K} \rightarrow A \rightarrow C (X) \rightarrow 0
$$

where $\mathcal{K}$ is the C\*-algebra of compact operators in Hilbert space, and X is a compact space. They have shown how to construct a group from such extensions. When X is a finite dimensional compact metric space, this group is naturally isomorphic to $\mathrm{K}_{1}(\mathrm{X})$, the Steenrod K-homology of X, cf. [24] [38].

Since the original classification problem of extensions did arise as an internal question in operator and C\*-algebra theory, the work of Brown, Douglas and Fillmore made it clear that K-theory is an indispensable tool even for studying C\*-algebras per se. This fact was further emphasized by the role of K-theory in the classification of C\*-algebras which are inductive limits of finite dimensional ones (cf. [10] [26] [27]) and in the work of Cuntz and Krieger on C\*-algebras associated to topological Markov chains ([22]).

Finally the work of the Russian school, of Miščenko and Kasparov in particular, ([50] [42] [43] [44]), on the Novikov conjecture, has shown that the K-theory of noncommutative C\*-algebras plays a crucial role in the solution of classical problems in the theory of non-simply-connected manifolds. For such a space X, a basic homotopy invariant is the Γ-equivariant signature σ of its universal covering  $\widetilde{X}$ , where  $\Gamma = \pi_{1}(X)$  is the fundamental group of X. This invariant σ lies in the K-group,  $\mathrm{K}_{0}(\mathrm{C}^{*}(\Gamma))$ , of the group  $\mathrm{C}^{*}$  algebra  $\mathrm{C}^{*}(\Gamma)$ .

The K-theory of C\*-algebras, the extension theory of Brown, Douglas and Fillmore and the Ell theory of Atiyah ([3]) are all special cases of Kasparov's bivariant functor KK(A, B). Given two Z/2 graded C\*-algebras A and B, KK(A, B) is an abelian group whose elements are homotopy classes of Kasparov A-B bimodules (cf. [42] [43]). For the convenience of the reader we have gathered in appendix 2 of part I the definitions of [42] which are relevant for our discussion.

After this quick overview of measure theory and topology in the non-commutative framework, let us be more specific about the algebras associated to the “spaces” occurring in  $a)$ ,  $b)$ ,  $c)$  above.

a) Let V be a smooth manifold, F a smooth foliation of V. The measure theory of the leaf space “V/F” is described by the von Neumann algebra  $W^{*}(V, F)$  of the foliation (cf. [14] [15] [16]). The topology of the leaf space is described by the  $C^{*}$ -algebra  $C^{*}(V, F)$  of the foliation (cf. [14] [15] [66]).

b) Let  $\Gamma$  be a discrete group. The measure theory of the (reduced) dual space  $\hat{\Gamma}$  is described by the von Neumann algebra  $\lambda(\Gamma)$  of operators in the Hilbert space  $\ell^{2}(\Gamma)$  which are invariant under right translations. This von Neumann algebra is the weak closure of the group ring  $\mathbf{C}\Gamma$  acting in  $\ell^{2}(\Gamma)$  by left translations. The topology of the

(reduced) dual space $\hat{\Gamma}$ is described by the $\mathbf{C}^*$-algebra $\mathbf{C}_r^*(\Gamma)$, the norm closure of $\mathbf{C}\Gamma$ in the algebra of bounded operators in $\ell^2 (\Gamma)$.

$b^{\prime})$ For a Lie group $\mathbf{G}$ the discussion is the same, with $\mathbf{C}_{c}^{\infty}(\mathbf{G})$ instead of $\mathbf{C}\Gamma$.

c) Let $\Gamma$ be a discrete group acting on a manifold $W$. The measure theory of the “orbit space” $W/\Gamma$ is described by the von Neumann algebra crossed product $\mathbf{L}^{\infty}(W) \rtimes \Gamma$ (cf. [51]). Its topology is described by the C\*-algebra crossed product $\mathbf{C}_0(V) \rtimes \Gamma$ (cf. [51]).

The situation is summarized in the following table:

| Space | V | V/F | $\hat{\Gamma}$ | $\hat{G}$ | W/$\Gamma$ |
| --- | --- | --- | --- | --- | --- |
| Measure theory | $L^{\infty}(V)$ | W*(V, F) | $\lambda(\Gamma)$ | $\lambda(G)$ | $L^{\infty}(W) \times\Gamma$ |
| Topology | $C_{0}(V)$ | $C^{*}(V, F)$ | $C_{r}^{*}(\Gamma)$ | $C_{r}^{*}(G)$ | $C_{0}(W) \times\Gamma$ |

It is a general principle (cf. [5] [18] [7]) that for families of elliptic operators  $(\mathbf{D}_{y})_{y\in\mathbf{Y}}$  parametrized by a “space” Y such as those occurring above, the index of the family is an element of  $\mathrm{K}_{0}(\mathrm{A})$, the K-group of the  $C^{*}$-algebra associated to Y. For instance the  $\Gamma$-equivariant signature of the universal covering X of a compact oriented manifold is the  $\Gamma$-equivariant index of the elliptic signature operator on X. We are in case b) and  $\sigma\in\mathrm{K}_{0}(\mathrm{C}_{r}^{*}(\Gamma))$. The obvious problem then is to compute  $\mathrm{K}_{*}(\mathrm{A})$  for the  $C^{*}$-algebras of the above spaces, and then the index of families of elliptic operators.

After the breakthrough of Pimsner and Voiculescu ([54]) in the computation of K-groups of crossed products, and under the influence of the Kasparov bivariant theory, the general program of computation of the K-groups of the above spaces (i.e. of the associated C\*-algebras) has undergone rapid progress in the last years ([16] [66] [52] [53] [68] [69]).

So far, each new result confirms the validity of the general conjecture formulated in [7]. In order to state it briefly, we shall deal only with case $c)$ above (1). By a familiar construction of algebraic topology a space such as $W / \Gamma$, the orbit space of a discrete group action, can be modeled as a simplicial complex, up to homotopy. One lets $\Gamma$ act freely and properly on a contractible space $E\Gamma$ and forms the homotopy quotient $W \times_{\Gamma} E\Gamma$ which is a meaningful space even when the quotient topological space $W / \Gamma$ is pathological. In case $b)$ ($\Gamma$ acting on $W = \{pt\}$) this yields the classifying space $B\Gamma$. In case $a)$, see [16] for the analogous construction. In [7] (using [16] and [18]) a map $\mu$ is defined from the twisted K-homology $K_{*,\tau}(W \times_{\Gamma} E\Gamma)$ to the K group of the $C^*$-algebra $C_0(W) \rtimes \Gamma$:

$$
\mu : \mathrm{K} _ {*, \tau} (\mathrm{W} \times_ {\Gamma} \mathrm{E} \Gamma) \rightarrow \mathrm{K} _ {*} (\mathrm{C} _ {0} (\mathrm{W}) \rtimes \Gamma).
$$

The conjecture is that this map  $\mu$  is always an isomorphism.

At this point it would be tempting to advocate that the space  $W \times_{\Gamma} E\Gamma$  gives a sufficiently good description of the topology of  $W/\Gamma$  and that we can dispense with

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) And we assume that $\Gamma$ is discrete and torsion free, cf. [7] for the general case.</span></small>

C\*-algebras. However, it is already clear in the simplest examples that the C\*-algebra  $A = \mathbf{C}_{0}(W) \rtimes \Gamma$  is a finer description of the “topological space” of orbits. For instance, with  $W = S^{1}$  and  $\Gamma = Z$, the actions given by two irrational rotations  $R_{\theta_{1}}$,  $R_{\theta_{2}}$  yield isomorphic C\*-algebras if and only if  $\theta_{1} = \pm \theta_{2}$  ([54] [55]), and Morita equivalent C\*-algebras if and only if  $\theta_{1}$  and  $\theta_{2}$  belong to the same orbit of the action of  $\text{PSL}(2, \mathbf{Z})$  on  $\mathbf{P}_{1}(\mathbf{R})$  [58]. On the contrary, the homotopy quotient is independent of  $\theta$  (and is homotopic to the 2-torus).

Moreover, as we already mentioned, an important role of a “space” such as  $Y = W/\Gamma$  is to parametrize a family of elliptic operators,  $(\mathbf{D}_{y})_{y \in \mathbb{Y}}$ . Such a family has both a topological index  $\operatorname{Ind}_{t}(\mathbf{D})$ , which belongs to the twisted K-homology group  $\mathbf{K}_{*,\tau}(\mathbf{W} \times_{\Gamma} \mathbf{E}\Gamma)$ , and an analytic index  $\operatorname{Ind}_{a}(\mathbf{D}) = \mu(\operatorname{Ind}_{t}(\mathbf{D}))$ , which belongs to  $\mathbf{K}_{*}(\mathbf{C}_{0}(\mathbf{W}) \rtimes \Gamma)$  (cf. [7] [20]). But it is a priori only through  $\operatorname{Ind}_{a}(\mathbf{D})$  that the analytic properties of the family  $(\mathbf{D}_{y})_{y \in \mathbb{Y}}$  are reflected. For instance, if each  $D_{y}$  is the Dirac operator on a Spin Riemannian manifold  $M_{y}$  of strictly positive scalar curvature, one has  $\operatorname{Ind}_{a}(\mathbf{D}) = o$  (cf. [59] [20]), but the equality  $\operatorname{Ind}_{t}(\mathbf{D}) = o$  follows only if one knows that the map  $\mu$  is injective (cf. [7] [59] [20]). The problem of injectivity of  $\mu$  is an important reason for developing the analogue of de Rham homology for the above “spaces”. Any closed de Rham current C on a manifold V yields a map  $\varphi_{c}$  from  $\mathbf{K}^{*}(\mathbf{V})$  to C

$$
\varphi_ {\mathrm{C}} (e) = \langle \mathbf {C}, \operatorname{ch} e \rangle \quad \forall e \in \mathbf {K} ^ {*} (\mathbf {V})
$$

where $\operatorname{ch}:\mathbf{K}^{*}(\mathbf{V})\to \mathbf{H}^{*}(\mathbf{V},\mathbf{R})$ is the usual Chern character.

Now, any “closed de Rham current” C on the orbit space W/Γ should yield a map  $\varphi_{C}$  from  $\mathbf{K}_{*}(\mathbf{C}_{0}(\mathbf{W})\rtimes\Gamma)$  to C. The rational injectivity of  $\mu$  would then follow from the existence, for each  $\omega\in\mathbf{H}^{*}(\mathbf{W}\times_{\Gamma}\mathbf{E}\Gamma)$ , of a “closed current”  $\mathbf{C}(\omega)$  making the following diagram commutative,

$$
\begin{array}{l} \mathrm{K} _ {*, \tau} (\mathrm{W} \times_ {\Gamma} \mathrm{E} \Gamma) \xrightarrow {\mu} \mathrm{K} _ {*} ((\mathrm{C} _ {0} (\mathrm{W}) \rtimes \Gamma) \\ \left| \begin{array}{c c} \mathbf {e h} _ {*} & \\ \downarrow & \end{array} \right. \\ \mathrm{H} _ {*} (\mathrm{W} \times_ {\Gamma} \mathrm{E} \Gamma , \mathbf {R}) \xrightarrow {\omega} \mathbf {C} \end{array}
$$

Here we assume that W is  $\Gamma$ -equivariantly oriented so that the dual Chern character  $ch_{*}:K_{*,\tau}\to H_{*}$  is well defined (see [20]). Also, we view  $\omega\in\mathrm{H}^{*}(\mathrm{W}\times_{\Gamma}\mathrm{E}\Gamma,\mathbf{C})$  as a linear map from  $\mathrm{H}_{*}(\mathrm{W}\times_{\Gamma}\mathrm{E}\Gamma,\mathbf{R})$  to C.

This leads us to the subject of this series of papers which is

1. The construction of de Rham homology for the above spaces;

2. Its applications to K-theory and index theory.

The construction of the theory of currents, closed currents, and of the maps  $\varphi_{c}$  for the above “spaces” requires two quite different steps.

261

The first is purely algebraic:

One starts with an algebra A over C, which plays the role of  $\mathbf{C}^{\infty}(\mathbf{V})$ , and one develops the analogue of de Rham homology, the pairing with the algebraic K-groups  $\mathrm{K}_{0}(\mathcal{A})$ ,  $\mathrm{K}_{1}(\mathcal{A})$ , and algebraic tools to perform the computations. This step yields a contravariant functor  $H_{\lambda}^{*}$  from non commutative algebras to graded modules over the polynomial ring  $\mathbf{C}(\sigma)$  with a generator  $\sigma$  of degree 2. In the definition of this functor the finite cyclic groups play a crucial role, and this is why  $H_{\lambda}^{*}$  is called cyclic cohomology. Note that it is a contravariant functor for algebras and hence a covariant one for “spaces”. It is the subject of part II under the title,

## De Rham homology and non-commutative algebra

The second step involves analysis:

The non-commutative algebra $\mathcal{A}$ is now a dense subalgebra of a $\mathbf{C}^*$-algebra A and the problem is, given a closed current $\mathbf{C}$ on $\mathcal{A}$ as above satisfying a suitable continuity condition relative to $\mathbf{A}$, to extend $\varphi_{\mathbb{C}}: \mathrm{K}_{0}(\mathcal{A}) \to \mathbf{C}$ to a map from $\mathrm{K}_{0}(\mathbf{A})$ to $\mathbf{C}$. In the simplest situation, which will be the only one treated in parts I and II, the algebra $\mathcal{A} \subset \mathbf{A}$ is stable under holomorphic functional calculus (cf. Appendix 3 of part I) and the above problem is trivial to handle since the inclusion $\mathcal{A} \subset \mathbf{A}$ induces an isomorphism $\mathrm{K}_{0}(\mathcal{A}) \approx \mathrm{K}_{0}(\mathbf{A})$. However, even to treat the fundamental class of $W/\Gamma$, where $\Gamma$ is a discrete group acting by orientation preserving diffeomorphisms on $W$, a more elaborate method is required and will be discussed in part V (cf. [20]). In the context of actions of discrete groups we shall construct $\mathrm{C}(\omega)$ and $\varphi_{\mathbb{C}(\omega)}$ for any cohomology class $\omega \in H^{*}(W \times_{\Gamma} E\Gamma, \mathbf{C})$ in the subring R generated by the following classes:

a) Chern classes of $\Gamma$-equivariant (non unitary) bundles on W,

b) $\Gamma$-invariant differential forms on W,

c) Gel'fand Fuchs classes.

As applications of our construction we get (in the above context):

$\alpha)$ If $x \in \mathbf{K}_{*,\tau}(\mathsf{W} \times_{\Gamma} \mathsf{E}\Gamma)$ and $\langle \operatorname{ch}_* x, \omega \rangle \neq 0$ for some $\omega$ in the above ring R then $\mu(x) \neq 0$.

In fact we shall further improve this result by varying W; it will then apply also to the case  $W = \{pt\}$ , i.e. to the usual Novikov conjecture. All this will be discussed in part V, but see [20] for a preview.

β) For any $\omega \in \mathbb{R}$ and any family $(\mathbf{D}_y)_{y \in \mathbf{Y}}$ of elliptic operators parametrized by $\mathbf{Y} = \mathbf{W} / \Gamma$, one has the index theorem:

$$
\varphi_ {\mathrm{C}} (\operatorname{Ind} _ {a} (\mathbf {D})) = \langle \operatorname{ch} _ {*} \operatorname{Ind} _ {t} (\mathbf {D}), \omega \rangle .
$$

When Y is an ordinary manifold, this is the cohomological form of the Atiyah-Singer index theorem for families ([5]).

It is important to note that, in all cases, the right hand side is computable by a standard recipe of algebraic topology from the symbol of D. The left hand side carries the analytic information such as vanishing, homotopy invariance...

All these results will be extended to the case of foliations (i.e. when Y is the leaf space of a foliation) in part VI.

As a third application of our analogue of de Rham homology for the above “spaces” we shall obtain index formulae for transversally elliptic operators, that is, elliptic operators on those “spaces” Y. In part IV we shall work out the pseudo-differential calculus for crossed products of a C\*-algebra by a Lie group (cf. [19]), thus yielding many non-trivial examples of elliptic operators on spaces of the above type. Let A be the C\* algebra associated to Y, any such elliptic operator on Y yields a finitely summable Fredholm module over the dense subalgebra A of smooth elements of A. In part I we show how to construct canonically from such a Fredholm module a closed current on the dense subalgebra A. The title of part I, the Chern character in K-homology is motivated by the specialization of the above construction to the case when Y is an ordinary manifold. Then the K homology K\*(V) is entirely described by elliptic operators on V ([9] [18]) and the association of a closed current provides us with a map,

$$
\mathbf {K} _ {*} (\mathbf {V}) \rightarrow \mathbf {H} _ {*} (\mathbf {V}, \mathbf {C})
$$

which is exactly the dual Chern character  $ch_{*}$ .

The explicit computation of this map  $ch_{*}$  will be treated in part III as an introduction to the asymptotic methods of computations of cyclic cocycles which will be used again in part IV. As a corollary we shall, in part IV, give completely explicit formulae for indices of finite difference, differential operators on the real line.

If D is an elliptic operator on a “space” Y and C is the closed current  $C = ch_{*}D$  (constructed in part I), the map  $\varphi_{C}: K_{*}(A) \to C$  makes sense and one has

$$
\varphi_ {\mathrm{C}} (\mathbf {E}) = \langle \mathbf {E}, [ \mathbf {D} ] \rangle = \text { Index }   \mathbf {D} _ {\mathbf {E}} \quad \forall   \mathbf {E} \in \mathbf {K} _ {*} (\mathbf {A})
$$

where the right hand side means the index of D with coefficients in E, or equivalently the value of the pairing between K-homology and K-cohomology. The integrality of this value, Index  $D_{E} \in Z$ , is a basic result which will be already used in a very efficient way in part I, to control  $\mathrm{K}_{*}(\mathrm{A})$ .

The aim of part I is to show that the construction of the Chern character  $ch_{*}$  in K homology dictates the basic definitions and operations—such as the suspension map S—in cyclic cohomology. It is motivated by the previous work of Helton and Howe [30], Carey and Pincus [12] and Douglas and Voiculescu [25].

There is another, equally important, natural route to cyclic cohomology. It was taken by Loday and Quillen ([46]) and by Tsigan ([67]). Since the latter's work is independent from ours, cyclic cohomology was discovered from two quite different points of view.

There is also a strong relation with the work of I. Segal [61] [62] on quantized differential forms, which will be discussed in part IV and with the work of M. Karoubi on secondary characteristic classes [39], which is discussed in part II, Theorem 33.

Our results and in particular the spectral sequence of part II were announced in the conference on operator algebras held in Oberwolfach in September 1981 ([21]).

This general introduction, required by the referee, is essentially identical to the survey lecture given in Bonn for the 25th anniversary of the Arbeitstagung.

This set of papers will contain,

I. The Chern character in K-homology.

II. De Rham homology and non commutative algebra.

III. Smooth manifolds, Alexander-Spanier cohomology and index theory.

IV. Pseudodifferential calculus for  $C^{*}$  dynamical systems, index theorem for crossed products and the pseudo torus.

V. Discrete groups and actions on smooth manifolds.

VI. Foliations and transversally elliptic operators.

VII. Lie groups.

Parts I and II follow immediately the present introduction.

## I. — THE CHERN CHARACTER IN K-HOMOLOGY

The basic theme of this first part is to “quantize” the usual calculus of differential forms. Letting A be an algebra over C we introduce the following operator theoretic definitions for a) the differential df of any  $f \in A$ , b) the graded algebra  $\Omega = \oplus \Omega^{q}$  of differential forms, c) the integration  $\omega \to \int \omega \in C$  of forms  $\omega \in \Omega^{n}$ ,

$$
d f = i [ \mathrm{F}, f ] = i (\mathrm{F} f - f \mathrm{F}) \quad \forall f \in \mathscr {A},
$$

$$
\Omega^ {q} = \{\Sigma f ^ {0} d f ^ {1} \dots d f ^ {q}, f ^ {j} \in \mathscr {A} \},
$$

$$
\int \omega = \operatorname{Trace} (\varepsilon \omega) \quad \forall \omega \in \Omega^ {n}.
$$

The data required for these definitions to have a meaning is an n-summable Fredholm module (H, F) over A.

Definition 1. — Let A be a (not necessarily commutative) Z/2 graded algebra over C. An n-summable Fredholm module over A is a pair (H, F), where,

1) $\mathbf{H} = \mathbf{H}^{+} \oplus \mathbf{H}^{-}$ is a $\mathbf{Z}/2$ graded Hilbert space with grading operator $\varepsilon$, $\varepsilon \xi = (-1)^{\deg \xi} \xi$ for all $\xi \in \mathbf{H}^{\pm}$,

2) H is a Z/2 graded left A-module, i.e. one has a graded homomorphism  $\pi$  of A in the algebra  $\mathcal{L}(\mathrm{H})$  of bounded operators in H,

3) $\mathbf{F} \in \mathcal{L}(\mathbf{H})$, $\mathbf{F}^2 = \mathbf{i}$, $\mathbf{F}\varepsilon = -\varepsilon \mathbf{F}$ and for any $a \in \mathcal{A}$ one has

$$
\mathbf {F} a - (- \mathrm{I}) ^ {\deg a} a \mathbf {F} \in \mathcal {L} ^ {n} (\mathbf {H})
$$

where $\mathcal{L}^n (\mathbf{H})$ is the Schatten ideal (cf. Appendix 1).

When $\mathcal{A}$ is the algebra $C^\infty(V)$ of smooth functions on a manifold $V$ the basic examples of Fredholm module over $\mathcal{A}$ come from elliptic operators on $V$ (cf. [3]). These modules are $p$-summable for any $p > \dim V$. We shall explain in section 6, theorem 5 how the usual calculus of differential forms, suitably modified by the use of the Pontrjagin classes, appears as the classical limit of the above quantized calculus based on the Dirac operator on $V$.

The above idea is directly in the line of the earlier works of Helton and Howe [30], Carey and Pincus [12], and Douglas and Voiculescu [25]. The notion of $n$-summable Fredholm module is a refinement of the notion of Fredholm module. The latter is due to Atiyah [3] in the even case and to Brown, Douglas and Fillmore [11] and Kas-

parov [42] in the odd case. The point of our construction is that n-summable Fredholm modules exist in many situations where the basic algebra A is no longer commutative, cf. sections 8 and 9. Moreover, even when A is commutative it improves on the previous works by determining all the lower dimensional homology classes of an extension and not only the top dimensional “fundamental trace form”. This point is explained in section 7.

Let then $\mathcal{A}$ be a not necessarily commutative algebra over $\mathbf{C}$ and (H, F) an $n$-summable Fredholm module over $\mathcal{A}$. We assume for simplicity that $\mathcal{A}$ is trivially $\mathbf{Z}/2$ graded. For any $a \in \mathcal{A}$, one has $da = i[\mathrm{F}, a] \in \mathcal{L}^n(\mathrm{H})$. For each $q \in \mathbf{N}$, let $\Omega^q$ be the linear span in $\mathcal{L}^{n/q}(\mathrm{H})$ of the operators

$$
\left(a ^ {0} + \lambda . \mathrm{I}\right) d a ^ {1} d a ^ {2} \dots d a ^ {q}, \quad a ^ {j} \in \mathscr {A}, \lambda \in \mathbf {C}.
$$

Since $\mathcal{L}^{n / q_1}\times \mathcal{L}^{n / q_2}\subset \mathcal{L}^{n / (q_1 + q_2)}$ (cf. Appendix 1) one checks that the composition of operators, $\Omega^{q_1}\times \Omega^{q_2}\to \Omega^{q_1 + q_2}$ endows $\Omega = \bigoplus_{j = 0}^{n}\Omega^{j}$ with a structure of a graded algebra. The differential $d$, $d\omega = i[\mathrm{F},\omega ]$ is such that

$$
d ^ {2} = 0, \quad d (\omega_ {1} \omega_ {2}) = (d \omega_ {1}) \omega_ {2} + (- \mathrm{I}) ^ {\deg \omega_ {1}} \omega_ {1} d \omega_ {2} \quad \forall \omega_ {1}, \omega_ {2} \in \Omega .
$$

Thus $(\Omega, d)$ is a graded differential algebra, with $d^2 = 0$. Moreover the linear functional $\int: \Omega^n \to \mathbf{C}$, defined by

$$
\int \omega = \operatorname{Trace} (\varepsilon \omega) \quad \forall \omega \in \Omega^ {n}
$$

has the same properties as the integration of the trace of ordinary matrix valued differential forms on an oriented manifold, namely,

$$
\int d \omega = 0 \quad \forall \omega \in \Omega^ {n - 1}, \quad \int \omega_ {2} \omega_ {1} = (- 1) ^ {\deg \omega_ {1} \deg \omega_ {2}} \int \omega_ {1} \omega_ {2}
$$

for any $\omega_{j} \in \Omega^{q_{j}}$, $j = 1, 2, q_{1} + q_{2} = n$.

Thus our construction associates to any n-summable Fredholm module (H, F) over A an n-dimensional cycle over A in the following sense.

Definition 2. — a) A cycle of dimension n is a triple $\left(\Omega, d, \int\right)$ where $\Omega = \bigoplus_{j=0}^{n} \Omega^j$ is a graded algebra over $\mathbf{C}$, $d$ is a graded derivation of degree 1 such that $d^2 = 0$, and $\int: \Omega^n \to \mathbf{C}$ is a closed graded trace on $\Omega$.

b) Let $\mathcal{A}$ be an algebra over $\mathbf{C}$. Then a cycle over $\mathcal{A}$ is given by a cycle $(\Omega, d, \int)$ and a homomorphism $\rho: \mathcal{A} \to \Omega^0$.

As we shall see in part II (cf. theorem 32) a cycle of dimension n over A is essentially determined by its character, the  $(n + 1)$ -linear function  $\tau$ ,

$$
\tau (a ^ {0}, \dots , a ^ {n}) = \int \rho (a ^ {0}) d (\rho (a ^ {1})) d (\rho (a ^ {2})) \dots d (\rho (a ^ {n})) \quad \forall a ^ {j} \in \mathcal {A}.
$$

266

Moreover (cf. part II, proposition 1), an $n + 1$ linear function $\tau$ on $\mathcal{A}$ is the character of a cycle of dimension $n$ over $\mathcal{A}$ if and only if it satisfies the following two simple conditions,

$$
\begin{array}{l} \alpha) \tau (a ^ {1}, a ^ {2}, \dots , a ^ {n}, a ^ {0}) = (- \mathrm{I}) ^ {n} \tau (a ^ {0}, \dots , a ^ {n}) \forall a ^ {j} \in \mathscr {A}, \\ \beta) \sum_ {0} ^ {n} (- \mathrm{I}) ^ {j} \tau (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}) + (- \mathrm{I}) ^ {n + 1} \tau (a ^ {n + 1} a ^ {0}, a ^ {1}, \dots , a ^ {n}) = 0. \end{array}
$$

There is a trivial manner to construct functionals $\tau$ satisfying conditions $\alpha)$ and $\beta)$. Indeed let $C_{\lambda}^{p}(\mathcal{A})$ be the space of $(p + 1)$-linear functionals on $\mathcal{A}$ such that,

$$
\varphi (a ^ {1}, \dots , a ^ {p}, a ^ {0}) = (- \mathrm{I}) ^ {p} \varphi (a ^ {0}, \dots , a ^ {p}) \quad \forall a ^ {j} \in \mathscr {A}.
$$

Then the equality,

$$
\begin{array}{r l} b \varphi (a ^ {0}, \dots , a ^ {p + 1}) & = \sum_ {0} ^ {p} (- \mathrm{I}) ^ {j} \varphi (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {p + 1}) \\ & \quad + (- \mathrm{I}) ^ {p + 1} \varphi (a ^ {p + 1} a ^ {0}, \dots , a ^ {p}) \end{array}
$$

defines a linear map $b$ from $\mathbf{C}_{\lambda}^{p}(\mathcal{A})$ to $\mathbf{C}_{\lambda}^{p + 1}(\mathcal{A})$ (cf. part II, corollary 4). Obviously conditions $\alpha)$ and $\beta)$ mean that $\tau \in \mathbf{C}_{\lambda}^{n}$ and $b\tau = 0$. As $b^2 = 0$, any $b\varphi, \varphi \in \mathbf{C}_{\lambda}^{n - 1}(\mathcal{A})$, satisfies $\alpha)$ and $\beta)$. The relevant group is then the cyclic cohomology group

$$
\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) = \{\tau \in \mathrm{C} _ {\lambda} ^ {n} (\mathcal {A}), b \tau = 0 \} / \{b \varphi , \varphi \in \mathrm{C} _ {\lambda} ^ {n - 1} (\mathcal {A}) \}.
$$

The above construction yields a map

## $\mathrm{ch}^*: \{n \text{ summable Fredholm modules over } \mathcal{A}\} \to \mathrm{H}_{\lambda}^{n}(\mathcal{A})$.

Since $\mathcal{A}$ is trivially $\mathbf{Z}/2$ graded, the character $\tau\in\mathrm{C}_{\lambda}^{n}(\mathcal{A})$ of any $n$ summable Fredholm module over $\mathcal{A}$ turns out to be equal to 0 for $n$ odd. Let us now restrict to even $n$'s. The inclusion $\mathcal{L}^{p}(\mathrm{H})\subset\mathcal{L}^{q}(\mathrm{H})$ for $p\leqq q$ (cf. Appendix 1) shows that an $n$ summable Fredholm module $(\mathrm{H},\mathrm{F})$ is also $n+2k$ summable for any $k=1,2,\ldots$. We shall prove (cf. section 4) that the $(n+2k)$-dimensional character $\tau_{n+2k}$ of $(\mathrm{H},\mathrm{F})$ is determined uniquely as an element of $\mathrm{H}_{\lambda}^{n+2k}(\mathcal{A})$ by the $n$-dimensional character $\tau_{n}$ of $(\mathrm{H},\mathrm{F})$. More precisely, there exists a linear map $\mathrm{S}:\mathrm{H}_{\lambda}^{n}(\mathcal{A})\to\mathrm{H}_{\lambda}^{n+2}(\mathcal{A})$ such that

$$
\tau_ {n + 2 k} = \mathrm{S} ^ {k} \tau_ {n} \text {   in   } \mathrm{H} _ {\lambda} ^ {n + 2 k} (\mathscr {A}).
$$

The operation  $\mathrm{S}:\mathrm{H}_{\lambda}^{n}(\mathcal{A})\to\mathrm{H}_{\lambda}^{n+2}(\mathcal{A})$  is easy to describe at the level of cycles. Let  $\Sigma$  be the 2-dimensional cycle over the algebra B=C with character  $\sigma,\sigma(1,1,1)=2i\pi$ . Then given a cycle over A with character  $\tau$ ,  $S\tau$  is the character of the tensor product of the original cycle by  $\Sigma$ . The reason for the normalization constant  $2i\pi$  appears clearly from the computation of an example (cf. section 2). It corresponds to the following normalization for  $\int\omega,\quad\omega\in\Omega^{n},\quad n=2m$ ,

$$
\int \omega = m! (2 i \pi) ^ {m} \operatorname{Trace} (\varepsilon \omega).
$$

Let now $\mathbf{H}_{\lambda}^{*}(\mathcal{A}) = \bigoplus_{n=0}^{\infty} \mathbf{H}_{\lambda}^{n}(\mathcal{A})$. The operation S turns $\mathbf{H}_{\lambda}^{*}(\mathcal{A})$ into a module over the polynomial ring $\mathbf{C}(\sigma)$, S being the multiplication by $\sigma$. Let,

$$
\mathrm{H} ^ {*} (\mathcal {A}) = \underset {\longrightarrow} {\operatorname{Lim}} \left(\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}), \mathrm{S}\right) = \mathrm{H} _ {\lambda} ^ {*} (\mathcal {A}) \otimes_ {\mathfrak {C} (\sigma)} \mathbf {C}
$$

where $\mathbf{C}(\sigma)$ acts on $\mathbf{C}$ by $\mathrm{P}(\sigma) z = \mathrm{P}(\mathrm{I}) z$ for $z \in \mathbf{C}$. The above results yield a map $\operatorname{ch}^*: \{\text{finitely summable Fredholm modules over } \mathcal{A}\} \to \mathrm{H}^*(\mathcal{A})$.

We shall show (section 5) that two finitely summable Fredholm modules over A which are homotopic (among such modules) yield the same element of  $H^{*}(\mathcal{A})$ .

When $\mathcal{A} = \mathbf{C}^{\infty}(\mathbf{V})$, where $\mathbf{V}$ is a smooth compact manifold, one has $\mathrm{H}_{\mathrm{cont}}^{*}(\mathcal{A}) = \mathrm{H}_{*}(\mathrm{V}, \mathbf{C})$ where $\mathrm{H}_{\mathrm{cont}}^{*}$ means that the $(n + 1)$-linear functionals $\varphi \in \mathrm{C}_{\lambda}^{n}(\mathcal{A})$ are assumed to be continuous, and $\mathrm{H}_{*}(\mathrm{V}, \mathbf{C})$ is the ordinary homology of $\mathbf{V}$ with complex coefficients. We can now explain what our construction has to do with the Chern character in K-homology. The latter is (cf. [9]) a natural map,

$$
\mathrm{ch} _ {*} \colon \mathrm{K} _ {*} (\mathrm{V}) \rightarrow \mathrm{H} _ {*} (\mathrm{V}, \mathbf {C})
$$

where the left side is the K-homology of V ([9]). By [24] the left side is isomorphic to the Kasparov group KK(C(V), C) of homotopy classes of \*Fredholm modules over the C\*-algebra C(V) (1). The link between our construction and the ordinary dual Chern character ch\* is contained in the commutativity of the following diagram:

$$
\begin{array}{c} \left\{ \begin{array}{l} \text {homotopy classes of finitely summable} \\ * \text {Fredholm modules over C} ^ {\infty} (\mathrm{V}) \end{array} \right\} \xrightarrow {\mathrm{ch} ^ {*}} \mathrm{H} _ {\text {cont}} ^ {*} (\mathrm{C} ^ {\infty} (\mathrm{V})) \\ \Bigg \downarrow \\ \mathrm{KK} (\mathrm{C} (\mathrm{V}), \mathbf {C}) \xrightarrow {\mathrm{ch} _ {*}} \mathrm{H} _ {*} (\mathrm{V}, \mathbf {C}) \end{array}
$$

For an arbitrary algebra $\mathcal{A}$ over $\mathbf{C}$, let $\mathrm{K}_0(\mathcal{A})$ be the algebraic K-theory of $\mathcal{A}$ (cf. [40]). One has (cf. part II, proposition 14) a natural pairing $<,>$ between $\mathrm{K}_0(\mathcal{A})$ and the even part of $\mathrm{H}^*(\mathcal{A})$. Moreover the following simple index formula holds for any finitely summable Fredholm module (H, F) over $\mathcal{A}$:

$$
\langle [ e ], \operatorname{ch} ^ {*} (\mathrm{H}, \mathrm{F}) \rangle = \text { Index } \mathrm{F} _ {e} ^ {+} \quad \forall e \in \operatorname{Proj} \mathrm{M} _ {k} (\mathscr {A}).
$$

Here $e$ is an arbitrary idempotent in the algebra of $k \times k$ matrices over $\mathcal{A}$, [e] is the corresponding element of $\mathrm{K}_0(\mathcal{A})$, and $\mathbf{F}_e^+$ is the Fredholm operator from $e(\mathbf{H}^+ \otimes \mathbf{C}^k)$ to $e(\mathbf{H}^- \otimes \mathbf{C}^k)$ given by $e(\mathbf{F} \otimes \mathbf{1}) e$. This formula is a direct generalisation of [20], [34]. It follows that any element $\tau$ of $\mathrm{H}^*(\mathcal{A})$ which is the Chern character of a finitely summable Fredholm module has the following integrality property,

$$
\langle \mathrm{K} _ {0} (\mathscr {A}), \tau \rangle \subset \mathbf {Z}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$a\in \mathcal{A},\xi ,\eta \in \mathrm{H}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">if $\langle a\xi, \eta \rangle = \langle \xi, a^* \eta \rangle$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) A Fredholm module over a \*algebra $\mathcal{A}$ is a \*Fredholm module if and only if $\langle a\xi, \eta \rangle = \langle \xi, a^* \eta \rangle$ for $a \in \mathcal{A}$, $\xi, \eta \in H$.</span></small>

1. The character of a 1-summable Fredholm module .... 53
2. Higher characters for a p-summable Fredholm module .... 56
3. Computation of the index map from any of the characters $\tau_{n}$ .... 60
4. The operation S and the relation between higher characters .... 61
5. Homotopy invariance of ch\*(H, F).... 63
6. Fredholm modules and unbounded operators .... 66
7. The odd dimensional case .... 69
8. Transversally elliptic operators for foliations .... 77
9. Fredholm modules over the convolution algebra of a Lie group .... 80

APPENDICES

1. Schatten classes.... 86
2. Fredholm modules.... 88
3. Stability under holomorphic functional calculus.... 92

To illustrate the power of this result we shall use it to reprove a remarkable result of M. Pimsner and D. Voiculescu: the reduced $\mathbf{C}^*$-algebra of the free group on 2 generators does not contain any non trivial idempotent. Letting $\tau$ be the canonical trace on $\mathbf{C}_r^*(\Gamma)$, and $e \in \operatorname{Proj}(\mathbf{C}_r^*(\Gamma))$, one knows that $\tau(e) \in [0, 1]$. Using a suitable Fredholm module (cf. [56], [23], [37]) with character $\tau$ we shall get $\tau(e) \in \mathbf{Z}$ and hence $\tau(e) \in \{0, 1\}$, i.e. $e = 0$ or $e = 1$.

Part I is organized as follows:

## CONTENTS

## 1. The character of a 1-summable Fredholm module

Let A be an algebra over C, with the trivial Z/2 grading. Let  $(H, F)$  be a 1-summable Fredholm module over A.

Lemma 1. — a) The equality $\tau(a) = \frac{1}{2} \operatorname{Trace}(\varepsilon F[F, a])$, $\forall a \in \mathcal{A}$, defines a trace on $\mathcal{A}$.

b) The index map, $\mathbf{K}_0(\mathcal{A})\to \mathbf{Z}$, is given by the trace $\tau$:

$$
\text { Index   } \mathbf {F} _ {e} ^ {+} = (\tau \otimes \text { Trace }) (e) \quad \forall e \in \text { Proj   } \mathbf {M} _ {q} (\mathscr {A}).
$$

Proof. — a) Since $\mathcal{A}$ is trivially $\mathbf{Z}/2$ graded, one has $\varepsilon a = a\varepsilon$ for all $a \in \mathcal{A}$. As $\varepsilon F = -F\varepsilon$ one has $\varepsilon F[F, a] = \varepsilon F^2 a - \varepsilon FaF = \varepsilon F^2 a + Fa\varepsilon F = \varepsilon a + Fa\varepsilon F$ since $F^2 = 1$. Thus,

$$
\varepsilon \mathrm{F} [ \mathrm{F}, a ] = [ \mathrm{F}, a ] \varepsilon \mathrm{F}.
$$

Then

$$
\begin{array}{r l} \tau (a b) & = \frac {1}{2} \operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, a b ]) = \frac {1}{2} \operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, a ] b + \varepsilon \mathrm{Fa} [ \mathrm{F}, b ]) \\ & = \frac {1}{2} \operatorname{Trace} ([ \mathrm{F}, a ] \varepsilon \mathrm{F} b + [ \mathrm{F}, b ] \varepsilon \mathrm{Fa}), \end{array}
$$

which is symmetric in $a$ and $b$. Thus $\tau(ab) = \tau(ba)$ for $a, b \in \mathcal{A}$.

b) Replacing $\mathcal{A}$ by $\mathrm{M}_{q}(\mathcal{A})$, and (H, F) by $(\mathrm{H} \otimes \mathbf{C}^{q}, \mathrm{F} \otimes \mathrm{i})$ we may assume that $q = \mathrm{i}$. Let $\mathrm{F} = \begin{bmatrix} 0 & Q \\ P & 0 \end{bmatrix}$ so that $\mathrm{PQ} = \mathrm{i}_{\mathrm{H}^{-}}$, $\mathrm{QP} = \mathrm{i}_{\mathrm{H}^{+}}$. With $\mathrm{H}_{1} = e\mathrm{H}^{+}$, $\mathrm{H}_{2} = e\mathrm{H}^{-}$ we let $\mathrm{P}'$ (resp. $\mathbf{Q}'$) be the operator from $\mathrm{H}_{1}$ to $\mathrm{H}_{2}$ (resp. $\mathrm{H}_{2}$ to $\mathrm{H}_{1}$) which is the restriction of $e\mathrm{P}$ (resp. $e\mathrm{Q}$) to $\mathrm{H}_{1}$ (resp. $\mathrm{H}_{2}$). Since $[\mathrm{F}, e] \in \mathcal{L}^{1}(\mathrm{H})$ one has $\mathrm{P}'\, \mathrm{Q}' - \mathrm{i}_{\mathrm{H}_{2}} \in \mathcal{L}^{1}(\mathrm{H}_{2})$, $\mathrm{Q}'\, \mathrm{P}' - \mathrm{i}_{\mathrm{H}_{1}} \in \mathcal{L}^{1}(\mathrm{H}_{1})$. Thus (proposition 6 of Appendix i) one has

$$
\begin{array}{r l} \text {Index P^{\prime}} & = \operatorname{Trace} (\mathrm{I} _ {\mathrm{H} _ {1}} - \mathrm{Q} ^ {\prime} \mathrm{P} ^ {\prime}) - \operatorname{Trace} (\mathrm{I} _ {\mathrm{H} _ {2}} - \mathrm{P} ^ {\prime} \mathrm{Q} ^ {\prime}) \\ & = \operatorname{Trace} _ {\mathrm{H} ^ {+}} (e - e \mathrm{QePe}) - \operatorname{Trace} _ {\mathrm{H} ^ {-}} (e - e \mathrm{PeQe}) \\ & = \operatorname{Trace} (\varepsilon (e - e \mathrm{FeFe})). \end{array}
$$

But

$$
\begin{array}{r l} \operatorname{Trace} (\varepsilon (e - e \mathrm{FeFe})) & = \operatorname{Trace} (\varepsilon (e - \mathrm{FeFe}) e) = \operatorname{Trace} (\varepsilon \mathrm{F} (\mathrm{Fe} - e \mathrm{F}) e) \\ & = \frac {1}{2} \operatorname{Trace} (\varepsilon \mathrm{Fe} [ \mathrm{F}, e ] + \varepsilon \mathrm{F} [ \mathrm{F}, e ] e) = \frac {1}{2} \operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, e ]) = \tau (e). \end{array}
$$

Definition 2. — Let (H, F) be a 1-summable Fredholm module over A. Then its character is the trace τ on A given by lemma 1a).

Corollary 3. — Let $\tau$ be the character of a 1-summable Fredholm module over $\mathcal{A}$. Then $\langle K_0(\mathcal{A}), \tau \rangle \subset \mathbf{Z}$.

Now let A be a C\*-algebra with unit and  $\tau$  a trace on A such that

1) $\tau$ is positive, i.e. $\tau(x^{*}x) \geq 0$ for $x \in \mathbf{A}$,

2) $\tau$ is faithful, i.e. $x \neq 0 \Rightarrow \tau(x^* x) > 0$ (cf. [55]).

Corollary 4. — Let A be a C\*-algebra with unit and $\tau$ a faithful positive trace on A such that $\tau(1) = 1$. Let (H, F) be a Fredholm module over A (cf. Appendix 2) such that a) $\mathcal{A} = \{a \in A, [F, a] \in \mathcal{L}^1(H)\}$ is dense in A,

b) $\tau / \mathcal{A}$ is the character of (H, F).

Then A contains no non trivial idempotent.

Proof. — By proposition 3, Appendix 3, the subalgebra $\mathcal{A}$ of A is stable under holomorphic functional calculus. Hence (Appendix 3) the injection $\mathcal{A} \to A$ yields an isomorphism, $\mathrm{K}_0(\mathcal{A}) \to \mathrm{K}_0(\mathrm{A})$. Thus the image of $\mathrm{K}_0(\mathrm{A})$ by $\tau$ is equal to the image of $\mathrm{K}_0(\mathcal{A})$ by the restriction of $\tau$ to $\mathcal{A}$ so that, by corollary 3, it is contained in $\mathbf{Z}$. If $e$ is a selfadjoint idempotent one has $\tau(e) \in [0,1] \cap \mathbf{Z} = \{0,1\}$ and hence, since $\tau$ is faithful, one has $e = 0$ or $e = 1$. It follows that A contains no non trivial idempotent $f$, $f^2 = f$.

Before we give an application of this corollary, let us point out that its proof is exactly in the spirit of differential topology. The result is purely topological; it is a statement on a C\*-algebra, which, for A commutative, means that the spectrum of A is connected. But to prove it one uses an auxiliary “smooth structure” given here by the subalgebra  $\mathcal{A}=\{a\in\mathrm{A},[\mathrm{F},a]\in\mathcal{L}^{1}(\mathrm{H})\}$ .

As an application we shall give a new proof of the beautiful result of M. Pimsner and D. Voiculescu that the reduced C\*-algebra of the free group on two generators does not contain any non trivial idempotent [56]. This solved a long standing conjecture of R. V. Kadison. We shall use a specific Fredholm module (H, F) over the reduced C\*-algebra of the free group which already appears in [56] and in the work of J. Cuntz [23], and whose geometric meaning in terms of trees was clarified by P. Julg and A. Valette in [37].

Definition 5. — Let $\Gamma$ be a discrete group. Then the reduced $\mathbf{C}^*$-algebra $\mathbf{A} = \mathbf{C}_r^*(\Gamma)$ of $\Gamma$ is the norm closure of the group ring $\mathbf{C}\Gamma$ in the algebra $\mathcal{L}(\ell^2 (\Gamma))$ of operators in the left regular representation of $\Gamma$ (cf. [51]).

Now let $\Gamma$ be an arbitrary free group, and $\mathbf{T}$ a tree on which $\Gamma$ acts freely and transitively. By definition $\mathbf{T}$ is a 1-dimensional simplicial complex which is connected and simply connected. For $j = 0$, $\mathbf{1}$ let $\mathbf{T}^j$ be the set of $j$-simplices in $\mathbf{T}$. Let $p \in \mathbf{T}^0$ and $\varphi: \mathbf{T}^0 \setminus \{p\} \to \mathbf{T}^1$ be the bijection which associates to any $q \in \mathbf{T}^0$, $q \neq p$, the only 1-simplex containing $q$ and belonging to the interval $[p, q]$. One readily checks that the bijection $\varphi$ is almost equivariant in the following sense: for all $g \in \Gamma$ one has $\varphi(gq) = g\varphi(q)$ except for finitely many $q$'s (cf. [23], [37]). Next, let $\mathbf{H}^+ = \ell^2(\mathbf{T}^0)$, $\mathbf{H}^- = \ell^2(\mathbf{T}^1) \oplus \mathbf{C}$. The action of $\Gamma$ on $\mathbf{T}^0$ and $\mathbf{T}^1$ yields a $\mathbf{C}_r^*(\Gamma)$-module structure on $\ell^2(\mathbf{T}^j)$, $j = 0, 1$, and hence on $\mathbf{H}^\pm$ if we put

$$
a (\xi , \lambda) = (a \xi , 0) \quad \forall \xi \in \ell^ {2} (\mathrm{T} ^ {1}), \lambda \in \mathbf {C}, a \in \mathrm{C} _ {r} ^ {*} (\Gamma).
$$

Let P be the unitary operator  $P:H^{+}\rightarrow H^{-}$  given by

$$
\mathrm{P} \varepsilon_ {p} = (\mathrm{o}, \mathrm{i}), \quad \mathrm{P} \varepsilon_ {q} = \varepsilon_ {\varphi (q)} \quad \forall q \neq p
$$

(where for any set X,  $(\varepsilon_{x})_{x\in X}$  is the natural basis of  $\ell^{2}(X)$ ). The almost equivariance of  $\varphi$  shows that

Lemma 6. — The pair (H, F), where $\mathbf{H} = \mathbf{H}^{+} \oplus \mathbf{H}^{-}$, $\mathbf{F} = \begin{bmatrix} 0 & \mathbf{P}^{-1} \\ \mathbf{P} & 0 \end{bmatrix}$ is a Fredholm module over A and $\mathcal{A} = \{a, [F, a] \in \mathcal{L}^1(H)\}$ is a dense subalgebra of A.

Proof. — For any  $g \in \Gamma$  the operator gP — Pg is of finite rank, hence the group ring  $C\Gamma$  is contained in  $\mathcal{A} = \{a \in \mathrm{C}_{r}^{*}(\Gamma), [\mathrm{F}, a] \in \mathcal{L}^{1}(\mathrm{H})\}$ . As  $C\Gamma$  is dense in  $\mathrm{C}_{r}^{*}(\Gamma)$  the conclusion follows. □

Let us compute the character of (H, F).

Let $a \in \mathcal{A}$, then $a - \mathbf{P}^{-1} a \mathbf{P} \in \mathcal{L}^1(\mathbf{H}^+)$ and

$$
\frac {1}{2} \operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, a ]) = \operatorname{Trace} (a - \mathrm{P} ^ {- 1} a \mathrm{P}).
$$

Let $\tau$ be the unique positive trace on A such that $\tau(\Sigma a_g g) = a_1$, where $i \in \Gamma$ is the unit, for any element $a = \Sigma a_g g$ of $\mathbf{C}\Gamma$. Then for any $a \in \mathrm{A} = \mathrm{C}_r^*(\Gamma)$, $a - \tau(a)i$ belongs to the norm closure of the linear span of the elements $g \in \Gamma$, $g \neq i$.

271

Since the action of $\Gamma$ on $\mathbf{T}^j$ is free, it follows that the diagonal entries in the matrix of $a - \tau(a)$ in $\ell^2 (\mathbf{T}^j)$ are all equal to 0. This shows that for any $a\in \mathcal{A}$ one has,

$$
\operatorname{Trace} (a - \mathrm{P} ^ {- 1} a \mathrm{P}) = \tau (a) \operatorname{Trace} (\mathrm{I} - \mathrm{P} ^ {- 1} \mathrm{I} \mathrm{P}) = \tau (a).
$$

Thus the character of (H, F) is the restriction of $\tau$ to $\mathcal{A}$ and since $\tau$ is faithful and positive (cf. [51]), corollary 4 shows that

Corollary 7. — (Cf. [56]). Let $\Gamma$ be the free group on 2 generators. Then the reduced $\mathbf{C}^*$-algebra $\mathbf{C}_r^*(\Gamma)$ contains no non trivial idempotent.

## 2. Higher characters for a p-summable Fredholm module

Let $\mathcal{A}$ be a trivially $\mathbf{Z}/2$ graded algebra over $\mathbf{C}$. Let $(\mathrm{H},\mathrm{F})$ be a $p$-summable Fredholm module over $\mathcal{A}$. As explained in the introduction we shall associate to $(\mathrm{H},\mathrm{F})$ an $n$-dimensional cycle over $\mathcal{A}$, where $n$ is an arbitrary even integer such that $n \geq p$. In fact we shall improve this construction so that we only have to assume that $n \geq p - 1$, i.e. that $(\mathrm{H},\mathrm{F})$ is $(n + 1)$-summable.

Let $\mathcal{A}$ be obtained from $\mathcal{A}$ by adjoining a unit which acts by the identity operator in H. For any $T \in \mathcal{L}(H)$ let $dT = i[F, T]$ where the commutator is a graded commutator. For each $j \in \mathbf{N}$ we let $\Omega^j$ be the linear span in $\mathcal{L}(H)$ of the operators of the form

$$
a ^ {0} d a ^ {1} \dots d a ^ {j}, \quad a ^ {k} \in \widetilde {\mathcal {A}}.
$$

Lemma 1. — a) $d^{2} \mathrm{T} = 0$$\forall \mathrm{T} \in \mathcal{L}(\mathrm{H})$.

b) $d(\mathrm{T}_1\mathrm{T}_2) = (d\mathrm{T}_1)\mathrm{T}_2 + (-\mathrm{I})^{\partial \mathrm{T}_1}\mathrm{T}_1d\mathrm{T}_2\forall \mathrm{T}_1,\mathrm{T}_2\in \mathcal{L}(\mathrm{H}).$

c) $d\Omega^{j}\subset \Omega^{j + 1}.$

d) $\Omega^j \times \Omega^k \subset \Omega^{j+k}$; in particular each $\Omega^j$ is a two-sided $\widetilde{\mathcal{A}}$-module.

e) $\Omega^k\subset \mathcal{L}^{(n + 1) / k}(\mathbf{H})$

Proof. — a) If T is homogeneous, then

$$
\mathbf {F} (\mathbf {F T} - (- \mathrm{i}) ^ {\partial \mathrm{T}} \mathbf {T F}) - (- \mathrm{i}) ^ {\partial \mathrm{T} + 1} (\mathbf {F T} - (- \mathrm{i}) ^ {\partial \mathrm{T}} \mathbf {T F}) \mathbf {F}
$$

$$
= \mathrm{F} ^ {2} \mathrm{T} - \mathrm{TF} ^ {2} = 0.
$$

b) The map $\mathbf{T} \to [\mathbf{F}, \mathbf{T}]$ is a graded derivation of $\mathcal{L}(\mathbf{H})$.

c) Follows from a), b).

$d)$ It is enough to show that for $a^0, \ldots, a^j$, $a \in \widetilde{\mathcal{A}}$ one has

$$
\left(a ^ {0} d a ^ {1} \dots d a ^ {j}\right) a \in \Omega^ {j}.
$$

This follows from the equality  $(da^{j})a=d(a^{j}a)-a^{j}da$ , by induction.

e) Since (H, F) is $n + \mathrm{i}$ summable one has $da \in \mathcal{L}^{n+1}(\mathrm{H})$ for all $a \in \mathcal{A}$ and e) follows from the inclusion $\mathcal{L}^p \times \mathcal{L}^q \subset \mathcal{L}^r$ for $\frac{\mathrm{I}}{r} = \frac{\mathrm{I}}{p} + \frac{\mathrm{I}}{q}$ (cf. Appendix 1). □

Lemma 1 shows that the direct sum $\Omega = \bigoplus_{j=0}^{n} \Omega^j$ of the vector spaces $\Omega^j$ is naturally endowed with a structure of graded differential algebra, with $d^2 = 0$.

Lemma 2. — For any $\mathrm{T} \in \mathcal{L}(\mathrm{H})$ such that $[\mathrm{F}, \mathrm{T}] \in \mathcal{L}^1(\mathrm{H})$ let

$$
\operatorname{Tr} _ {s} (\mathrm{T}) = \frac {\mathrm{I}}{2} \operatorname{Trace} (\varepsilon \mathrm{F} ([ \mathrm{F}, \mathrm{T} ])).
$$

a) If $\mathbf{T}$ is homogeneous with odd degree, then $\operatorname{Tr}_s(\mathbf{T}) = 0$.

b) If $\mathbf{T} \in \mathcal{L}^1(\mathbf{H})$ then $\operatorname{Tr}_s(\mathbf{T}) = \operatorname{Trace}(\varepsilon \mathbf{T})$.

c) One has $[\mathbf{F},\Omega^n ]\subset \mathcal{L}^1 (\mathrm{H})$ and the restriction of $\mathrm{Tr}_s$ to $\Omega^n$ defines a closed graded trace on the differential algebra $\Omega$.

Proof. — a) Since F[F, T] is homogeneous with odd degree one has

$$
\varepsilon \mathrm{F} [ \mathrm{F}, \mathrm{T} ] = - \mathrm{F} [ \mathrm{F}, \mathrm{T} ] \varepsilon
$$

and

$$
\operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, \mathrm{T} ]) = \operatorname{Trace} (\mathrm{F} [ \mathrm{F}, \mathrm{T} ] \varepsilon) = - \operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, \mathrm{T} ])
$$

thus

$$
\operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, \mathrm{T} ]) = 0.
$$

b) $\frac{\mathrm{I}}{2}\operatorname{Trace}(\varepsilon\mathbf{F}[\mathbf{F},\mathbf{T}]) = \frac{\mathrm{I}}{2}\operatorname{Trace}\varepsilon(\mathbf{T} - \mathbf{FTF})$ for all $\mathbf{T}$ with $\partial \mathbf{T} = 0 (\mathrm{mod} 2)$.

If $\mathbf{T} \in \mathcal{L}^1(\mathbf{H})$ then $\operatorname{Trace}(\varepsilon \mathbf{FTF}) = -\operatorname{Trace}(\mathbf{F}\varepsilon \mathbf{TF}) = -\operatorname{Trace}(\varepsilon \mathbf{T})$, so that

$$
\frac {1}{2} \operatorname{Trace} (\varepsilon F [ F, T ]) = \operatorname{Trace} (\varepsilon T).
$$

c) One has $[\mathbf{F},\Omega^n ]\subset \Omega^{n + 1}\subset \mathcal{L}^1 (\mathrm{H})$ by lemma i. Since $d^2 = 0$ one has $\operatorname {Tr}_s(d\omega) = 0\forall \omega \in \Omega^{n - 1}$. It remains to show that for $\omega_{1}\in \Omega^{n_{1}}$$\omega_{2}\in \Omega^{n_{2}}$$n_1 + n_2 = n$ one has $\operatorname {Tr}_s(\omega_1\omega_2) = (-1)^{n_1n_2}\operatorname {Tr}_s(\omega_2\omega_1),$

or equivalently, that

$$
\operatorname{Trace} \left(\varepsilon \mathrm{F} d \left(\omega_ {1} \omega_ {2}\right)\right) = (- 1) ^ {n _ {1}} \operatorname{Trace} \left(\varepsilon \mathrm{F} d \left(\omega_ {2} \omega_ {1}\right)\right).
$$

Since  $\varepsilon F$  commutes with  $d\omega_{1}$  and  $d\omega_{2}$ , one has

$$
\begin{array}{r l} \operatorname{Trace} (\varepsilon \mathrm{F} d (\omega_ {1} \omega_ {2})) & = \operatorname{Trace} (\varepsilon \mathrm{F} (d \omega_ {1}) \omega_ {2}) + (- \mathrm{i}) ^ {n _ {1}} \operatorname{Trace} (\varepsilon \mathrm{F} \omega_ {1} d \omega_ {2}) \\ & = \operatorname{Trace} (\varepsilon \mathrm{F} \omega_ {2} d \omega_ {1}) + (- \mathrm{i}) ^ {n _ {1}} \operatorname{Trace} ((\varepsilon \mathrm{F} d \omega_ {2}) \omega_ {1}) \\ & = (- \mathrm{i}) ^ {n _ {1}} \operatorname{Trace} (\varepsilon \mathrm{F} d (\omega_ {2} \omega_ {1})). \quad \square \end{array}
$$

We can now associate an $n$-dimensional cycle over $\mathcal{A}$ to any $n + 1$ summable Fredholm module (H, F).

Definition 3. — Let $n = 2m$ be an even integer, and (H, F) an $(n + 1)$-summable Fredholm module over $\mathcal{A}$. Then the associated cycle over $\mathcal{A}$ is given by the graded differential algebra $(\Omega, d)$, the integral

$$
\int \omega = (2 i \pi) ^ {m} m! \operatorname{Tr} _ {s} (\omega) \quad \forall \omega \in \Omega^ {n}
$$

and the homomorphism $\pi : \mathcal{A} \to \Omega^0 \subset \mathcal{L}(\mathbf{H})$ of definition 1.

273

The normalization constant $(2i\pi)^m m!$ is introduced to conform with the usual integration of differential forms on a smooth manifold. To be more precise let us treat the following simple example. We let $\Gamma \subset \mathbf{C}$ be a lattice, and $V = \mathbf{C} / \Gamma$. Then $V$ is a smooth manifold and the $\bar{\partial}$ operator yields a natural Fredholm module over $\mathbf{C}^{\infty}(V)$. We consider $\bar{\partial}$ as a bounded operator from the Sobolev space $H^{+} = \{\xi \in L^{2}(V), \bar{\partial}\xi \in L^{2}(V)\}$ to $H^{-} = L^{2}(V)$. The algebra $\mathbf{C}^{\infty}(V)$ acts in $H^{\pm}$ by multiplication operators, and the operator $F$ is given by $\left[ \begin{array}{ccc}0 & (\bar{\partial} + \varepsilon)^{-1} \\ \bar{\partial} + \varepsilon & 0 \end{array} \right]$, where $\varepsilon \in \mathbf{C}$, $i\varepsilon \notin \Gamma^{\perp}$ the orthogonal of the lattice $\Gamma$ (to ensure that $\bar{\partial} + \varepsilon$ is invertible). We let $(\varepsilon_g^-)_{g \in \Gamma^{\perp}}$ be the natural orthonormal basis of $L^{2}(V) = H^{-}$, $\varepsilon_g^- (z) = |\mathbf{C} / \Gamma^{\perp}|^{-1/2} \exp i\langle g, z\rangle$ for $z \in \mathbf{C} / \Gamma$, and $(\varepsilon_g^+)$ be the corresponding basis of $H^{+}$, $\varepsilon_g^+ = (\bar{\partial} + \varepsilon)^{-1} \varepsilon_g^-$. Thus $\varepsilon_g^+(z) = (ig + \varepsilon)^{-1} \varepsilon_g^- (z)$ for $z \in \mathbf{C} / \Gamma$, and we may as well assume that the $\varepsilon_g^+$ form an orthonormal basis of $H^{+}$. For each $g \in \Gamma^{\perp}$, let $U_g \in C^\infty(V)$ be given by $U_g(z) = \exp i\langle g, z\rangle$, then $U_{g_1 + g_2} = U_{g_1} U_{g_2}$ for $g_1, g_2 \in \Gamma^{\perp}$ and the algebra $\mathbf{C}^\infty(V)$ is naturally isomorphic to the convolution algebra $\mathcal{S}(\Gamma^{\perp})$ of sequences of rapid decay on $\Gamma^{\perp}$, $\mathbf{C}^\infty(V) = \{\Sigma a_g U_g, a \in \mathcal{S}(\Gamma^{\perp})\}$. One has $U_g \varepsilon_k^- = \varepsilon_{g+k}^-$ and

$$
\mathrm{U} _ {g} \varepsilon_ {k} ^ {+} = \mathrm{U} _ {g} (i k + \varepsilon) ^ {- 1} \varepsilon_ {k} ^ {-} = (i k + \varepsilon) ^ {- 1} \varepsilon_ {g + k} ^ {-} = \frac {i (g + k) + \varepsilon}{i k + \varepsilon} \varepsilon_ {g + k} ^ {+},
$$

for any $g, k \in \Gamma^{\perp}$. We are now ready to prove

Lemma 4. — With the above notations, (H, F) is a 3-summable $\mathbf{C}^{\infty}(\mathbf{V})$-module and

$$
\operatorname{Tr} _ {s} \left(f ^ {0} i [ F, f ^ {1} ] i [ F, f ^ {2} ]\right) = \frac {I}{2 i \pi} \int f ^ {0} d f ^ {1} \wedge d f ^ {2} \quad \forall f ^ {0}, f ^ {1}, f ^ {2} \in C ^ {\infty} (V),
$$

where V is oriented by its complex structure.

Proof. — For $g \in \Gamma^{\perp}$ one has

$$
\begin{array}{r l} \left(\mathrm{FU} _ {g} - \mathrm{U} _ {g} \mathrm{F}\right) \varepsilon_ {k} ^ {+} & = \mathrm{F} \left(\frac {i (g + k) + \varepsilon}{i k + \varepsilon}\right) \varepsilon_ {g + k} ^ {+} - \varepsilon_ {g + k} ^ {-} \\ & = \left(\frac {i (g + k) + \varepsilon}{i k + \varepsilon} - 1\right) \varepsilon_ {g + k} ^ {-} = \frac {i g}{i k + \varepsilon} \varepsilon_ {g + k} ^ {-} \end{array}
$$

and similarly $(\mathrm{FU}_g - \mathrm{U}_g\mathrm{F})\varepsilon_k^- = \frac{-ig}{ik + \varepsilon}\varepsilon_{g + k}^+$. Since $\mathcal{S}(\Gamma^{\perp})\subset \ell^{1}(\Gamma^{\perp})$, it follows that (H, F) is $p$-summable for any $p > 2$.

To prove the equality of the lemma we may assume that $f^j = \mathbf{U}_{g_j}$ with $g_0, g_1, g_2 \in \Gamma^\perp$. From the above computation we get

$$
\begin{array}{r l} & {\left[ \mathrm{F}, \mathrm{U} _ {g _ {0}} \right] \left[ \mathrm{F}, \mathrm{U} _ {g _ {1}} \right] \left[ \mathrm{F}, \mathrm{U} _ {g _ {2}} \right] \varepsilon_ {k} ^ {+}} \\ & {\qquad = \left(\frac {g _ {0}}{g _ {1} + g _ {2} + k - i \varepsilon}\right) \left(\frac {- g _ {1}}{g _ {2} + k - i \varepsilon}\right) \left(\frac {g _ {2}}{k - i \varepsilon}\right) \varepsilon_ {g _ {0} + g _ {1} + g _ {2} + k} ^ {-}} \end{array}
$$

274

and

$$
\begin{array}{r l} & {\left[ \mathrm{F}, \mathrm{U} _ {g _ {0}} \right] \left[ \mathrm{F}, \mathrm{U} _ {g _ {1}} \right] \left[ \mathrm{F}, \mathrm{U} _ {g _ {2}} \right] \varepsilon_ {k} ^ {-}} \\ & {\qquad = \left(\frac {- g _ {0}}{g _ {1} + g _ {2} + k - i \varepsilon}\right) \left(\frac {g _ {1}}{g _ {2} + k - i \varepsilon}\right) \left(\frac {- g _ {2}}{k - i \varepsilon}\right) \varepsilon_ {g _ {0} + g _ {1} + g _ {2} + k} ^ {+}.} \end{array}
$$

Thus $\operatorname{Tr}_s(\mathbf{U}_{g_0} i[\mathbf{F}, \mathbf{U}_{g_1}] i[\mathbf{F}, \mathbf{U}_{g_2}]) = -\frac{\mathrm{I}}{2} \operatorname{Trace}(\varepsilon \mathbf{F}[\mathbf{F}, \mathbf{U}_{g_0}][\mathbf{F}, \mathbf{U}_{g_1}][\mathbf{F}, \mathbf{U}_{g_2}])$ is equal to o if $g_0 + g_1 + g_2 \neq o$ and otherwise to:

$$
\sum_ {k \in \Gamma^ {\perp}} \left(\frac {g _ {0}}{g _ {1} + g _ {2} + k - i \varepsilon}\right) \left(\frac {g _ {1}}{g _ {2} + k - i \varepsilon}\right) \left(\frac {g _ {2}}{k - i \varepsilon}\right).
$$

This sum can be computed as an Eisenstein series ([70]). More precisely let u, v be generators of  $\Gamma^{\perp}$  with  $\operatorname{Im}(v/u) > 0$  and  $\operatorname{E}_{1}(z)$  the function

$$
\mathrm{E} _ {1} (z) = \lim _ {\mathrm{N} \rightarrow \infty} \sum_ {\nu = - \mathrm{N}} ^ {\mathrm{N}} (\operatorname * {L i m} _ {\mathrm{M} \rightarrow \infty} \sum_ {\mu = - \mathrm{M}} ^ {\mathrm{M}} (z + k) ^ {- 1}) \quad \text { where } k = \mu u + \nu v.
$$

Then the above expression coincides with

$$
\begin{array}{r l} g _ {1} (\mathrm{E} _ {1} (- i \varepsilon) - \mathrm{E} _ {1} (g _ {2} - i \varepsilon)) - g _ {2} (\mathrm{E} _ {1} (g _ {2} - i \varepsilon) - \mathrm{E} _ {1} (g _ {1} + g _ {2} - i \varepsilon)) \\ & = 2 i \pi (n _ {2} m _ {1} - n _ {1} m _ {2}), \end{array}
$$

where $g_{i} = n_{i}u + m_{i}v$ (cf. [70], p. 17).

Let $(\alpha, \beta)$ be the basis of $\mathbf{C}$ over $\mathbf{R}$ dual to $(u, v)$. Then $\Gamma = 2\pi(\mathbf{Z}\alpha + \mathbf{Z}\beta)$, $\mathrm{U}_g(x\alpha + y\beta) = e^{inx} e^{imy}$ for all $x, y \in \mathbf{R}$, $g = nu + mv \in \Gamma^\perp$. For $g_0 + g_1 + g_2 \neq 0$ one has $\int_{\mathrm{V}} \mathrm{U}_{g_0} d\mathrm{U}_{g_1} d\mathrm{U}_{g_2} = 0$ and otherwise

$$
\begin{array}{r l} \int_ {\mathrm{V}} \mathrm{U} _ {g _ {0}} d \mathrm{U} _ {g _ {1}} d \mathrm{U} _ {g _ {2}} & = \int_ {0} ^ {2 \pi} \int_ {0} ^ {2 \pi} ((i n _ {1}) (i m _ {2}) - (i n _ {2}) (i m _ {1})) d x d y \\ & = (2 i \pi) ^ {2} \times (n _ {1} m _ {2} - n _ {2} m _ {1}). \end{array}\tag{□}
$$

A similar computation yields the factor $(2i\pi)^m m!$ for $n = 2m$.

Proposition 5. — Let $n = 2m$, (H, F) be an $(n + 1)$-summable Fredholm module over $\mathcal{A}$, and $\tau$ be the character of the cycle associated to (H, F),

$$
\tau (a ^ {0}, \dots , a ^ {n}) = (2 i \pi) ^ {m} m! \operatorname{Tr} _ {s} (a ^ {0} d a ^ {1} \dots d a ^ {n}).
$$

Then a) $\tau(a^1, \ldots, a^n, a^0) = \tau(a^0, \ldots, a^n)$ for $a^j \in \mathcal{A}$;

$$
\sum_ {0} ^ {n} (- \mathrm{I}) ^ {j} \tau (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}) + (- \mathrm{I}) ^ {n + 1} \tau (a ^ {n + 1} a ^ {0}, \dots , a ^ {n}) = 0.
$$

Proof. — Follows from proposition I of part II. □

With the notation of part II, corollary 4, one has $\tau \in \mathbf{C}_{\lambda}^{n}(\mathcal{A})$ by a) and $b\tau = 0$ by b), i.e. $\tau \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$.

Remark 6. — All the results of this section extend to the general case, when A is not trivially Z/2 graded. The following important points should be stressed,

$\alpha)$ Since $a^j \in \mathcal{A}$ can have non zero degree mod 2, it is not true in general that $\int \omega = 0$ for $\omega \in \Omega^n$, $n$ odd.

$\beta)$ Since the symbol $d$ has degree $\mathbf{1}$, the $n$-dimensional character $\tau_{n}$ of an $(n + 1)$-summable Fredholm module (H, F) over $\mathcal{A}$ is now given by the equality,

$$
\tau_ {n} \left(a ^ {0}, \dots , a ^ {n}\right) = c _ {n} (- 1) ^ {\partial a ^ {1} + \partial a ^ {3} + \dots + \partial a ^ {2 k + 1} + \dots} \operatorname{Tr} _ {s} \left(a ^ {0} d a ^ {1} \dots d a ^ {n}\right).
$$

Here $c_n$ is a normalization constant such that $c_{n+2} = 2i\pi \frac{n+2}{2} c_n$, we take $c_{2m} = (2i\pi)^m m!$, $c_{2m-1} = (2i\pi)^m \left(m - \frac{1}{2}\right) \ldots \left(\frac{3}{2}\right) \left(\frac{1}{2}\right)$.

γ) In general, the conditions a), b) of proposition 5 become

$a^{\prime})$

$$
\tau (a ^ {1}, \dots , a ^ {n}, a ^ {0}) = (- \mathrm{I}) ^ {n} (- \mathrm{I}) ^ {\partial a ^ {0} (\sum_ {1} ^ {n} \partial a ^ {j})} \tau (a ^ {0}, a ^ {1}, \dots , a ^ {n}) \quad \forall a ^ {j} \in \mathscr {A},\tag{\( b' \}
$$

$$
\begin{array}{l} \sum_ {j = 0} ^ {n} (- \mathrm{I}) ^ {j} \tau (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}) \\ \qquad + (- \mathrm{I}) ^ {n + 1} (- \mathrm{I}) ^ {\partial a ^ {n + 1} \sum_ {0} ^ {n} \partial a ^ {j}} \tau (a ^ {n + 1} a ^ {0}, a ^ {1}, \dots , a ^ {n}) = 0. \end{array}
$$

The general rule (cf. [49]) is that, when two objects of $\mathbf{Z}/2$ degrees $\alpha$ and $\beta$ are permuted, the sign $(-1)^{\alpha\beta}$ is introduced.

## 3. Computation of the index map from any of the characters  $\tau_{n}$

Let $\mathcal{A}$ be an algebra over $\mathbf{C}$, with trivial $\mathbf{Z}/2$ grading. Let $n = 2m$ be an even integer, (H, F) an $(n + 1)$-summable Fredholm module over $\mathcal{A}$, and $\tau_n$ the $n$-dimensional character of (H, F).

Let $(\tau_{n})$ be the class of $\tau_{n}$ in $\mathrm{H}_{\lambda}^{n}(\mathcal{A}) = \mathrm{Z}_{\lambda}^{n}(\mathcal{A}) / b\mathrm{C}_{\lambda}^{n - 1}(\mathcal{A})$. By part II, proposition 14, the following defines a bilinear pairing $< , >$ between $\mathrm{K}_0(\mathcal{A})$ and $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$:

$$
\langle e, \varphi \rangle = (2 i \pi) ^ {- m} (m!) ^ {- 1} (\varphi \neq \operatorname{Tr}) (e, \dots , e)
$$

for any idempotent $e \in \mathbf{M}_k(\mathcal{A})$ and any $\varphi \in \mathbf{Z}_\lambda^n(\mathcal{A})$. Here $\varphi \neq \operatorname{Tr} \in \mathbf{Z}_\lambda^n(\mathbf{M}_k(\mathcal{A}))$ is defined by

$$
(\varphi \neq \operatorname{Tr}) (a ^ {0} \otimes m ^ {0}, \dots , a ^ {n} \otimes m ^ {n}) = \varphi (a ^ {0}, \dots , a ^ {n}) \operatorname{Trace} (m ^ {0} \dots m ^ {n})
$$

for any $a^j \in \mathcal{A}$, $m^j \in \mathrm{M}_k(\mathbf{C})$.

When the algebra $\mathcal{A}$ is not unital, one first extends $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$ to $\widetilde{\varphi} \in Z_{\lambda}^{n}(\widetilde{\mathcal{A}})$, where $\widetilde{\mathcal{A}}$ is obtained from $\mathcal{A}$ by adjoining a unit,

$$
\widetilde {\varphi} \left(a ^ {0} + \lambda^ {0} \mathrm{I}, \dots , a ^ {n} + \lambda^ {n} \mathrm{I}\right) = \varphi \left(a ^ {0}, \dots , a ^ {n}\right) \quad \forall a ^ {j} \in \mathscr {A}, \lambda^ {j} \in \mathbf {C}.
$$

Then one applies the above formula, for $e \in \mathbf{M}_k(\widetilde{\mathcal{A}})$.

Theorem 1. — (Compare with [25] and [34]). Let $n = 2m$ and (H, F) an $(n + 1)$-summable Fredholm module over $\mathcal{A}$. Then the index map $K_0(\mathcal{A}) \to \mathbf{Z}$ is given by the pairing of $K_0(\mathcal{A})$ with the class in $H_\lambda^n(\mathcal{A})$ of the $n$-dimensional character $\tau_n$ of (H, F):

$$
\text { Index   } \mathbf {F} _ {e} ^ {+} = \langle [ e ], (\tau_ {n}) \rangle \quad \text { for   } e \in \operatorname{Proj} \mathrm{M} _ {q} (\mathcal {A}).
$$

276

Proof. — As in the proof of lemma 1.1 b) we may assume that $k = \mathbf{I}$, that $\mathcal{A}$ is unital and that its unit acts in H as the identity. Let $\mathbf{F} = \begin{bmatrix} 0 & Q \\ P & 0 \end{bmatrix}$, so that $PQ = \mathrm{I}_{H^{-}}$, $QP = \mathrm{I}_{H^{+}}$. Let $H_1 = eH^+$, $H_2 = eH^-$, and $P'$ (resp. $Q'$) be the operator from $H_1$ to $H_2$ (resp. $H_2$ to $H_1$) which is the restriction of $eP$ (resp. $eQ$) to $H_1$ (resp. $H_2$). Thus $\mathrm{I}_{\mathrm{H}_1} - \mathrm{Q}'\mathrm{P}'$ (resp. $\mathrm{I}_{\mathrm{H}_2} - \mathrm{P}'\mathrm{Q}'$) is the restriction to $H_1$ (resp. $H_2$) of $e - eFeFe$. As $e - eFeFe = -e[F, e]^2e$, and $[F, e] \in \mathscr{L}^{n+1}(H)$, we get (Appendix 1, proposition 6) Index $P' = \text{Trace } \varepsilon(e - eFeFe)^{m+1}$.

One has $\langle e, \tau_m \rangle = \frac{(-1)^m}{2} \operatorname{Trace}(\varepsilon F[F, e]^{2m+1})$. As $[F, e] = e[F, e] + [F, e] e$, one has

$$
\operatorname{Trace} (\varepsilon \mathrm{F} ([ \mathrm{F}, e ]) ^ {2 m + 1}) = \operatorname{Trace} (\varepsilon \mathrm{Fe} [ \mathrm{F}, e ] [ \mathrm{F}, e ] ^ {2 m}) + \operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, e ] e [ \mathrm{F}, e ] ^ {2 m}).
$$

Now $\varepsilon \mathbf{F} = -\mathbf{F}\varepsilon, \mathbf{F}[\mathbf{F}, e]^{2m + 1} = -[\mathbf{F}, e]^{2m + 1}\mathbf{F}$, so that

$$
\begin{array}{r l} \operatorname{Trace} (\varepsilon \mathrm{F} e [ \mathrm{F}, e ] ^ {2 m + 1}) & = - \operatorname{Trace} (\mathrm{F} \varepsilon e [ \mathrm{F}, e ] ^ {2 m + 1}) \\ & = - \operatorname{Trace} (\varepsilon e [ \mathrm{F}, e ] ^ {2 m + 1} \mathrm{F}) = \operatorname{Trace} (\varepsilon e \mathrm{F} [ \mathrm{F}, e ] ^ {2 m + 1}). \end{array}
$$

As $e[\mathbf{F}, e]^2 = [\mathbf{F}, e]^2 e$ we get

$$
\begin{array}{r l} \operatorname{Trace} (\varepsilon \mathrm{F} [ \mathrm{F}, e ] ^ {2 m + 1}) & = 2 \operatorname{Trace} (\varepsilon e \mathrm{F} [ \mathrm{F}, e ] e [ \mathrm{F}, e ] ^ {2 m}) \\ & = 2 (- \mathrm{i}) ^ {m} \operatorname{Trace} \varepsilon (e - e \mathrm{FeFe}) ^ {m + 1}. \end{array}
$$

## 4. The operation S and the relation between higher characters

In part II, theorem 9, we show that the operation of tensor product of cycles yields a homomorphism $(\varphi, \psi) \mapsto \varphi \# \psi$ of $Z_{\lambda}^{n}(\mathcal{A}) \times Z_{\lambda}^{m}(\mathcal{B})$ to $Z_{\lambda}^{n+m}(\mathcal{A} \otimes \mathcal{B})$, for any algebras $\mathcal{A}$, $\mathcal{B}$ over $\mathbf{C}$. Taking $\mathcal{B} = \mathbf{C}$ and $\sigma \in Z_{\lambda}^{2}(\mathbf{C})$, $\sigma(\lambda_0, \lambda_1, \lambda_2) = 2i\pi\lambda_0 \lambda_1 \lambda_2$ yields the map S, $S\varphi = \varphi \# \sigma$ from $Z_{\lambda}^{n}(\mathcal{A})$ to $Z_{\lambda}^{n+2}(\mathcal{A} \otimes \mathbf{C}) = Z_{\lambda}^{n+2}(\mathcal{A})$. By part II, corollary 10, one has $SB_{\lambda}^{n}(\mathcal{A}) \subset B_{\lambda}^{n+2}(\mathcal{A})$. Now let $n = 2m$ be even, (H, F) be an $(n + 1)$-summable Fredholm module over $\mathcal{A}$. As $\mathcal{L}^{n+1}(H) \subset \mathcal{L}^{n+3}(H)$, the Fredholm module (H, F) is $(n + 3)$-summable, and hence has characters $\tau_n$, $\tau_{n+2}$ of dimensions $n$ and $n + 2$.

Theorem 1. — One has $\tau_{n+2} = S\tau_n$ in $H_{\lambda}^{n+2}(\mathcal{A})$.

Proof. — By construction, $\tau_{n}$ is the character of the cycle $(\Omega, d, \int)$ associated to (H, F) by definition 3. Thus (part II, corollary 10) $S\tau_{n}$ is given by

$$
\begin{array}{l} \mathrm{S} \tau_ {n} (a ^ {0}, \dots , a ^ {n + 2}) = 2 i \pi \sum_ {0} ^ {n + 1} \int (a ^ {0} d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} a ^ {j + 1} (d a ^ {j + 2} \dots d a ^ {n + 2}) \\ = (2 i \pi) ^ {m + 1} m! \sum_ {0} ^ {n + 1} \operatorname{Tr} _ {s} ((a ^ {0} d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} a ^ {j + 1} (d a ^ {j + 2} \dots d a ^ {n + 2})). \end{array}
$$

By definition, $\tau_{n + 2}$ is given by

$$
\tau_ {n + 2} (a ^ {0}, \dots , a ^ {n + 2}) = (2 i \pi) ^ {m + 1} (m + 1)! \operatorname{Tr} _ {s} (a ^ {0} d a ^ {1} \dots d a ^ {n + 2}).
$$

We just have to find $\varphi_0\in \mathbf{C}_{\lambda}^{n + 1}(\mathcal{A})$ such that $b\varphi_0 = \mathrm{S}\tau_n - \tau_{n + 2}$. We shall construct $\varphi \in \mathbf{C}_{\lambda}^{n + 1}(\mathcal{A})$ such that

$$
\begin{array}{r l} b \varphi (a ^ {0}, \dots , a ^ {n + 2}) & = \frac {2}{i} \sum_ {0} ^ {n + 1} \mathrm{Tr} _ {s} ((a ^ {0} d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} a ^ {j + 1} (d a ^ {j + 2} \dots d a ^ {n + 2})) \\ & \qquad - \left(\frac {n + 2}{i}\right) \mathrm{Tr} _ {s} (a ^ {0} d a ^ {1} \dots d a ^ {n + 2}). \end{array}
$$

We take $\varphi = \sum_{0}^{n + 1}(-\mathrm{I})^{j}\varphi^{j}$, where

$$
\varphi^ {j} (a ^ {0}, \dots , a ^ {n + 1}) = \operatorname{Trace} (\varepsilon \mathrm{F} a ^ {j} d a ^ {j + 1} \dots d a ^ {j - 1}).
$$

One has $a^{j}da^{j + 1}\ldots da^{j - 1}\in \Omega^{n + 1}\subset \mathcal{L}^{1}(\mathbf{H})$ so that the trace makes sense; moreover by construction one has $\varphi \in \mathrm{C}_{\lambda}^{n + 1}(\mathcal{A})$.

To end the proof we shall show that

$$
\begin{array}{r l} b \varphi^ {j} (a ^ {0}, \dots , a ^ {n + 2}) & = \frac {(- \mathrm{I}) ^ {j - 1}}{i} \operatorname{Tr} _ {s} (a ^ {0} d a ^ {1} \dots d a ^ {n + 2}) \\ & + \frac {2}{i} (- \mathrm{I}) ^ {j} \operatorname{Tr} _ {s} ((a ^ {0} d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} a ^ {j + 1} (d a ^ {j + 2} \dots d a ^ {n + 2})). \end{array}
$$

Using the equality $d(ab) = (da)b + adb$, with $a, b \in \mathcal{A}$, we get

$$
\begin{array}{r l} b \varphi^ {j} (a ^ {0}, \dots , a ^ {n + 2}) & = \operatorname{Trace} (\varepsilon \mathrm{F} (a ^ {j + 1} d a ^ {j + 2} \dots d a ^ {n + 2}) a ^ {0} (d a ^ {1} \dots d a ^ {j})) \\ & + (- \mathrm{I}) ^ {j - 1} \operatorname{Trace} (\varepsilon \mathrm{Fa} ^ {j + 1} (d a ^ {j + 2} \dots d a ^ {0} \dots d a ^ {j - 1}) a ^ {j}) \\ & + \operatorname{Trace} (\varepsilon \mathrm{Fa} ^ {j} (d a ^ {j + 1} \dots d a ^ {n + 2}) a ^ {0} (d a ^ {1} \dots d a ^ {j - 1})). \end{array}
$$

Let $\beta = (da^{j + 2}\dots da^{n + 2})a^0 (da^1\dots da^{j - 1})\in \Omega^n$ . Using the equality

$$
\operatorname{Trace} (\varepsilon \alpha d \beta) = \operatorname{Tr} _ {s} (\alpha d \beta) = \operatorname{Tr} _ {s} (i [ F, \alpha ] \beta) \quad \forall \alpha \in \mathscr {L} (H), \quad \varepsilon \alpha = - \alpha \varepsilon ,
$$

we get

$$
\begin{array}{r l} (- \mathrm{I}) ^ {j - 1} \operatorname{Trace} (\varepsilon \mathrm{F} a ^ {j + 1} (d a ^ {j + 2} \dots d a ^ {0} \dots d a ^ {j - 1}) a ^ {j}) & = \operatorname{Tr} _ {\varepsilon} (i [ \mathrm{F}, a ^ {j} \mathrm{F} a ^ {j + 1} ] \beta). \end{array}
$$

Thus,

$$
\begin{array}{l} b \varphi^ {j} (a ^ {0}, \dots , a ^ {n + 2}) = \operatorname{Trace} (d a ^ {j} \varepsilon \mathrm{Fa} ^ {j + 1} \beta) + \operatorname{Tr} _ {s} (i [ \mathrm{F}, a ^ {j} \mathrm{Fa} ^ {j + 1} ] \beta) \\ \quad + \operatorname{Trace} (\varepsilon \mathrm{Fa} ^ {j} d a ^ {j + 1} \beta) = \operatorname{Tr} _ {s} ((\mathrm{Fd} (a ^ {j} a ^ {j + 1}) + i [ \mathrm{F}, a ^ {j} \mathrm{Fa} ^ {j + 1} ]) \beta). \end{array}
$$

One has  $\mathrm{Fd}(a^{j}a^{j+1}) + i[\mathrm{F}, a^{j}\mathrm{Fa}^{j+1}] = -i(da^{j}da^{j+1} - 2a^{j}a^{j+1})$  and the above equality follows easily. □

This theorem leads one to introduce the group $\mathbf{H}^{\mathrm{ev}}(\mathcal{A})$ which is the inductive limit of the groups $\mathbf{H}_{\lambda}^{2n}(\mathcal{A})$ with the maps,

$$
\mathrm{H} _ {\lambda} ^ {2 m} (\mathcal {A}) \stackrel {{\mathrm{S}}} {{\to}} \mathrm{H} _ {\lambda} ^ {2 m + 2} (\mathcal {A}).
$$

With the notation of part II, corollary 10, one has,

$$
\mathrm{H} ^ {\theta \nu} (\mathcal {A}) = \mathrm{H} _ {\lambda} ^ {\theta \nu} (\mathcal {A}) \otimes_ {\mathbf {C} [ \sigma ]} \mathbf {C}
$$

where $\mathbf{C}(\sigma)$ acts on $\mathbf{C}$ by $\mathrm{P}(\sigma) \to \mathrm{P}(\mathrm{I})$ (cf. part II, definition 16).

Definition 2. — Let (H, F) be a finitely summable Fredholm module over $\mathcal{A}$. We let $\operatorname{ch}^*(\mathrm{H}, \mathrm{F})$ be the element of $\mathbf{H}^*(\mathcal{A})$ given by any of the characters $\tau_{2m}$, $m$ large enough.

By part II, corollary 17, one has a canonical pairing $\langle ,\rangle$ between $\mathrm{H}^{\mathrm{ev}}(\mathcal{A})$ and $\mathrm{K}_0(\mathcal{A})$ and theorem 3.1 implies the following corollary.

Corollary 3. — Let (H, F) be a finitely summable Fredholm module over A. Then the index map  $\mathbf{K}_{0}(\mathcal{A}) \to \mathbf{Z}$  is given by

$$
\text { Index   } \mathbf {F} _ {e} ^ {+} = \langle \mathrm{ch} _ {*} (e), \mathrm{ch} ^ {*} (\mathrm{H}, \mathbf {F}) \rangle \quad \forall e \in \operatorname{Proj} \mathbf {M} _ {k} (\widetilde {\mathcal {A}}).
$$

For such a formula to be interesting one needs to solve two problems:

1) compute $\mathbf{H}^{*}(\mathcal{A})$;

2) compute $\operatorname{ch}^*(\mathbf{H},\mathbf{F})$

In part II we shall develop general tools to handle problem 1.

## 5. Homotopy invariance of  $\mathbf{ch}^{*}(\mathbf{H},\mathbf{F})$

Let $\mathcal{A}$ be an algebra over $\mathbf{C}$. In this section we shall show that the character $\mathrm{ch}^*(\mathrm{H},\mathrm{F})\in \mathrm{H}^{\mathrm{ev}}(\mathcal{A})$ of a finitely summable Fredholm module only depends upon the homotopy class of (H, F). Let $\mathbf{H}_0$ be a Hilbert space and $\mathbf{H}$ the $\mathbf{Z}/2$ graded Hilbert space with $\mathbf{H}^{+} = \mathbf{H}_{0}$, $\mathbf{H}^{-} = \mathbf{H}_{0}$. Let $\mathbf{F}\in\mathcal{L}(\mathbf{H})$, $\mathbf{F}=\begin{bmatrix}0&1\\ I&0\end{bmatrix}$.

Lemma 1. — Let $p = 2m$ be an even integer. For each $t \in [0, \mathbf{i}]$ let $\pi_t$ be a graded homomorphism of $\mathcal{A}$ in $\mathcal{L}(\mathbf{H})$ such that $\mathbf{i}$) $t \to [\mathbf{F}, \pi_i(a)]$ is a continuous map from $[0, \mathbf{i}]$ to $\mathcal{L}^p(\mathbf{H})$ for any $a \in \mathcal{A}, 2)$$t \to \pi_i(a) \xi$ is a $\mathbf{C}^1$ map from $[0, \mathbf{i}]$ to $\mathbf{H}$ for any $a \in \mathcal{A}, \xi \in \mathbf{H}$. Let $(\mathbf{H}_t, \mathbf{F})$ be the corresponding $p$-summable Fredholm modules over $\mathcal{A}$. Then the class in $\mathrm{H}_{\lambda}^{p+2}(\mathcal{A})$ of the $(p+2)$-dimensional character of $(\mathbf{H}_t, \mathbf{F})$ is independent of $t \in [0, \mathbf{i}]$.

Proof. — Replacing $\mathcal{A}$ by $\mathcal{A}$ we can assume that $\mathcal{A}$ is unital and that $\pi_t(\mathrm{i}) = \mathrm{i}$, $\forall t \in [0, \mathrm{i}]$. By the Banach Steinhaus theorem, the derivative $\delta_t(a)$ of the map $t \to \pi_t(a)$ is a strongly continuous map from $[0, \mathrm{i}]$ to $\mathcal{L}(\mathrm{H})$. Moreover,

$$
\delta_ {t} (a b) = \pi_ {t} (a) \delta_ {t} (b) + \delta_ {t} (a) \pi_ {t} (b) \quad \text { for } a, b \in \mathscr {A}, t \in [ 0, 1 ].
$$

For $t \in [0, 1]$ let $\varphi_t$ be the $(p + 2)$-linear functional on $\mathscr{A}$ given by

$$
\varphi_ {t} (a ^ {0}, \dots , a ^ {p + 1}) = \sum_ {k = 1} ^ {p + 1} (- \mathrm{i}) ^ {k - 1} \operatorname{Trace} (\varepsilon \pi_ {t} (a ^ {0}) [ \mathrm{F}, \pi_ {t} (a ^ {1}) ] \dots
$$

$$
[ \mathrm{F}, \pi_ {t} (a ^ {k - 1}) ] \delta_ {t} (a ^ {k}) [ \mathrm{F}, \pi_ {t} (a ^ {k + 1}) ] \dots [ \mathrm{F}, \pi_ {t} (a ^ {p + 1}) ]).
$$

Using the equality $\delta_t(ab) = \pi_i(a)\delta_i(b) + \delta_i(a)\pi_i(b),\forall a,b\in \mathcal{A}$, one checks that $\varphi_{t}$ is a Hochschild cocycle, i.e. $b\varphi_{t} = 0$, where

$$
\begin{array}{r l} b \varphi_ {t} (a ^ {0}, \dots , a ^ {p + 2}) & = \sum_ {q = 0} ^ {p + 1} (- \mathrm{I}) ^ {q} \varphi_ {t} (a ^ {0}, \dots , a ^ {q} a ^ {q + 1}, \dots , a ^ {p + 2}) \\ & \quad + (- \mathrm{I}) ^ {p + 2} \varphi_ {t} (a ^ {p + 2} a ^ {0}, a ^ {1}, \dots , a ^ {p + 1}), \quad \forall a ^ {j} \in \mathcal {A}. \end{array}
$$

Let $\varphi$ be the $(p + 2)$-linear functional on $\mathcal{A}$ given by

$$
\varphi (a ^ {0}, \dots , a ^ {p + 1}) = \int_ {0} ^ {1} \varphi_ {t} (a ^ {0}, \dots , a ^ {p + 1}) d t.
$$

(Since $||\pi_t(a)||$ and $||\delta_t(a)||$ are bounded, the integral makes sense.)

One has $b\varphi = 0$ and $\varphi(a^0, \ldots, a^{p+1}) = 0$ if $a^j = 1$ for some $j \neq 0$. One has

$$
\begin{array}{c} \varphi (\mathrm{I}, a ^ {0}, a ^ {1}, \dots , a ^ {p}) = \int_ {0} ^ {1} d t \sum_ {k = 0} ^ {p} (- \mathrm{I}) ^ {k} \operatorname{Trace} (\varepsilon [ \mathrm{F}, \pi_ {t} (a ^ {0}) ] \dots \\ \left[ \mathrm{F}, \pi_ {t} (a ^ {k - 1}) \right] \delta_ {t} (a ^ {k}) \left[ \mathrm{F}, \pi_ {t} (a ^ {k + 1}) \right] \dots \left[ \mathrm{F}, \pi_ {t} (a ^ {p}) \right]). \end{array}
$$

Let

$$
\tau_ {t} (a ^ {0}, \dots , a ^ {p}) = \operatorname{Trace} (\varepsilon \pi_ {t} (a ^ {0}) [ \mathrm{F}, \pi_ {t} (a ^ {1}) ] \dots [ \mathrm{F}, \pi_ {t} (a ^ {p}) ]).
$$

One has

$$
\begin{array}{l} \frac {\mathrm{I}}{s} \left(\tau_ {t + s} (a ^ {0}, \dots , a ^ {p}) - \tau_ {t} (a ^ {0}, \dots , a ^ {p})\right) \\ = \operatorname{Trace} \left(\varepsilon \frac {\mathrm{I}}{s} \left(\pi_ {t + s} (a ^ {0}) - \pi_ {t} (a ^ {0})\right) [ \mathrm{F}, \pi_ {t + s} (a ^ {1}) ] \dots [ \mathrm{F}, \pi_ {t + s} (a ^ {p}) ]\right) \\ + \operatorname{Trace} \left(\varepsilon \pi_ {t} (a ^ {0}) \left[ \mathrm{F}, \frac {\mathrm{I}}{s} \left(\pi_ {t + s} (a ^ {1}) - \pi_ {t} (a ^ {1})\right) \right] \dots [ \mathrm{F}, \pi_ {t + s} (a ^ {p}) ]\right) + \dots \\ + \operatorname{Trace} \left(\varepsilon \pi_ {t} (a ^ {0}) [ \mathrm{F}, \pi_ {t} (a ^ {1}) ] \dots \left[ \mathrm{F}, \frac {\mathrm{I}}{s} \left(\pi_ {t + s} (a ^ {p}) - \pi_ {t} (a ^ {p})\right) \right]\right). \end{array}
$$

When $s \to 0$ one has, using 1) and 2),

$$
\begin{array}{l}\operatorname{Trace} \left(\varepsilon \pi_ {t} (a ^ {0}) [ \mathrm{F}, \pi_ {t} (a ^ {1}) ] \dots [ \mathrm{F}, \pi_ {t} (a ^ {k - 1}) ] \left[ \mathrm{F}, \frac {\mathrm{I}}{s} (\pi_ {t + s} (a ^ {k}) - \pi_ {t} (a ^ {k})) \right] \dots [ \mathrm{F}, \pi_ {t + s} (a ^ {p}) ]\right)\\= (- \mathrm{I}) ^ {k} \operatorname{Trace} \left(\varepsilon [ \mathrm{F}, \pi_ {t} (a ^ {0}) ] \dots [ \mathrm{F}, \pi_ {t} (a ^ {k - 1}) ] \frac {\mathrm{I}}{s} (\pi_ {t + s} (a ^ {k}) - \pi_ {t} (a ^ {k})) [ \mathrm{F}, \pi_ {t} (a ^ {k + 1}) ] \dots [ \mathrm{F}, \pi_ {t + s} (a ^ {p}) ]\right)\\\rightarrow (- \mathrm{I}) ^ {k} \operatorname{Trace} (\varepsilon [ \mathrm{F}, \pi_ {t} (a ^ {0}) ] \dots [ \mathrm{F}, \pi_ {t} (a ^ {k - 1}) ] \delta_ {t} (a ^ {k}) [ \mathrm{F}, \pi_ {t + s} (a ^ {k + 1}) ] \dots [ \mathrm{F}, \pi_ {t + s} (a ^ {p}) ]).\end{array}
$$

Thus $\varphi(1, a^0, \ldots, a^p) = \int_0^1 \tau_t' dt = \tau_1(a^0, \ldots, a^p) - \tau_0(a^0, \ldots, a^p)$ and the result follows from Part II, lemma 34, since $b\varphi = 0$ and $\mathbf{B}_0\varphi = \tau_1 - \tau_0$.

Theorem 2. — Let A be an algebra over C, H a Z/2 graded Hilbert space. Let  $(\mathrm{H}_{t}, \mathrm{F}_{t})$  be a family of Fredholm modules over A with the same underlying Z/2 graded Hilbert space H. Let  $\rho_{t}^{\pm}$  be the corresponding homomorphisms of A in  $\mathcal{L}(\mathrm{H}^{\pm})$  and  $F_{t} = \begin{bmatrix} o & Q_{t} \\ P_{t} & o \end{bmatrix}$ . Assume that for some  $p < \infty$  and any  $a \in A$ ,

1) $t \mapsto \rho_t^+(a) - Q_t \rho_t^-(a) P_t$ is a continuous map from [0, 1] to $\mathcal{L}^p(\mathbf{H})$,

2) $t \mapsto \rho_t^+(a)$ and $t \mapsto \mathbf{Q}_t \rho_t^-(a) \mathbf{P}_t$ are piecewise strongly $\mathbf{C}^1$.

Then $\operatorname{ch}^{*}(\mathbf{H}_{t},\mathbf{F}_{t})\in \mathrm{H}^{\mathrm{ev}}(\mathcal{A})$ is independent of $t\in [\mathrm{o},\mathrm{i}]$.

Proof. — Let  $T_{t}=\begin{bmatrix}I & O \\ O & Q_{t}\end{bmatrix}$ , then  $T_{t}F_{t}T_{t}^{-1}=\begin{bmatrix}O & I \\ I & O\end{bmatrix}$  and

$$
\mathrm{T} _ {t} \rho_ {t} (a) \mathrm{T} _ {t} ^ {- 1} = \left[ \begin{array}{c c} \rho_ {t} ^ {+} (a) & \mathbf {0} \\ \mathbf {0} & \mathbf {Q} _ {t} \rho_ {t} ^ {-} (a) \mathbf {P} _ {t} \end{array} \right].
$$

Then the result follows from lemma 1 and the invariance of the trace under similarity. $\square$

Corollary 3. — Let  $(\mathbf{H}, \mathbf{F}_{t})$  be a family of p-summable Fredholm modules over A with the same underlying A-module H and such that  $t \mapsto F_{t}$  is norm continuous. Then  $\operatorname{ch}^{*}(\mathbf{H}, \mathbf{F}_{t})$  is independent of  $t \in [0, 1]$ .

Proof. — Since the set of invertible operators in  $\mathcal{L}(\mathrm{H}^{+},\mathrm{H}^{-})$  is open, one can replace the homotopy  $F_{t}$  by one such that  $t\mapsto P_{t}$  is piecewise linear and hence piecewise norm differentiable. □

Let now A be a C\*-algebra and  $\mathscr{A} \subset A$  a dense \*subalgebra which is stable under holomorphic functional calculus (cf. Appendix 3). By theorem 2, the value of  $\text{ch}^{*}(H, F)$  only depends upon the homotopy class of  $(H, F)$ . We thus get the following commutative diagram,

$$
\begin{array}{c} \left\{ \begin{array}{l} \text {Homotopy classes of finitely summable} \\ ^ {*} \text {Fredholm modules over} \mathcal {A} \end{array} \right\} \xrightarrow {\mathrm{ch} ^ {*}} \mathrm{H} ^ {\mathrm{ev}} (\mathcal {A}) \\ \Bigg \downarrow \\ \mathrm{KK} (\mathrm{A}, \mathbf {C}) \longrightarrow \mathrm{Hom} (\mathrm{K} _ {0} (\mathrm{A}), \mathbf {Z}) \subset \mathrm{Hom} (\mathrm{K} _ {0} (\mathrm{A}), \mathbf {C}) \end{array}
$$

where

a) the left vertical arrow is given by proposition 4 of Appendix 3,

b) the right vertical arrow is given by the pairing of $\mathbf{K}_0(\mathcal{A})$ with $\mathrm{H}^{\mathrm{ev}}(\mathcal{A})$ of part II, corollary 17 together with the isomorphism $\mathbf{K}_0(\mathcal{A}) \approx \mathbf{K}_0(\mathbf{A})$ (Appendix 3, proposition 2),

c) the lower horizontal arrow is given by the pairing between $\mathbf{KK}(\mathbf{A},\mathbf{C})$ and $\mathbf{KK}(\mathbf{C},\mathbf{A}) = \mathbf{K}_0(\mathbf{A})$.

## 6. Fredholm modules and unbounded operators

Let A be an algebra over C. In this section we shall show how to construct p-summable Fredholm modules over A from unbounded operators D between A-modules. We shall then apply the construction to the Dirac operator on a manifold. We let H be a Z/2 graded Hilbert space which is an A-module and D a densely defined closed operator in H such that

1) $\varepsilon D = -D\varepsilon,$

2) $\mathbf{D}$ is invertible with $\mathbf{D}^{-1} \in \mathcal{L}(\mathbf{H})$,

3) for any $a \in \mathcal{A}$ the closure of $a - \mathrm{D}^{-1} a \mathrm{~D}$ belongs to $\mathcal{L}^p(\mathrm{H})$ (where $p \in [\mathrm{I}, \infty[$ is fixed).

Proposition 1. — a) Write $\mathbf{D} = \begin{bmatrix} \mathbf{o} & \mathbf{D}_2 \\ \mathbf{D}_1 & \mathbf{o} \end{bmatrix}$. Let $\mathrm{H}_{1}$ be the $\mathbf{Z}/2$ graded $\mathcal{A}$-module given by $\mathrm{H}_{1}^{+} = \mathrm{H}^{+}$, $\mathrm{H}_{1}^{-} = \text{The Hilbert space } \mathrm{H}^{+}$ with $a\xi = \mathrm{D}_{1}^{-1} a \mathrm{D}_{1} \xi$, for $\xi \in \operatorname{Dom} \mathrm{D}_{1}$$a \in \mathcal{A}$. Let $\mathrm{F}_{1} = \begin{bmatrix} \mathbf{o} & \mathbf{i} \\ \mathbf{i} & \mathbf{o} \end{bmatrix}$. Then $(\mathrm{H}_{1}, \mathrm{F}_{1})$ is a $p$-summable Fredholm module over $\mathcal{A}$.

b) The following equality defines an element $\tau \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$, $n = 2m$, $n \geq p - 1$

$$
\tau \left(a ^ {0}, \dots , a ^ {n}\right) = (2 \pi i) ^ {m} m! \operatorname{Trace} \left(\mathrm{D} ^ {- 1} [ \mathrm{D}, a ^ {0} ] \dots \mathrm{D} ^ {- 1} [ \mathrm{D}, a ^ {n} ]\right), \quad \forall a ^ {j} \in \mathscr {A}.
$$

c) Let  $(\mathbf{H}_{2}, \mathbf{F}_{2})$  be constructed as in a) from  $H^{-}$ and  $D_{2}$ . Then  $\tau = \tau_{1} - \tau_{2}$  where  $\tau_{j}$  is the character of  $(\mathbf{H}_{j}, \mathbf{F}_{j})$ .

Proof. — a) For  $a \in A$ , let  $\pi(a)$  be the operator in  $H^{+}$ defined as the closure of  $D_{1}^{-1} a D_{1}$ . Since  $a - D^{-1} a D \in L^{p}$ , we see that  $\pi(a) - a$  is bounded and belongs to  $\mathcal{L}^{p}(H^{+})$ . Since  $D_{1}D_{1}^{-1} = 1$  one has  $\pi(ab) = \pi(a)\pi(b)$  for  $a, b \in A$ . Thus the module  $H_{1}^{-}$ is well defined and one has  $[F_{1}, a] \in \mathcal{L}^{p}(H_{1}), \forall a \in A$ .

b) Follows from c).

c) One has  $D^{-1}[D, a] = \begin{bmatrix} a - D_{1}^{-1} & a D_{1} & 0 \\ 0 & & a - D_{2}^{-1} & a D_{2} \end{bmatrix}$  so that, for any  $a^{j} \in A$ ,

$$
\begin{array}{r l} \tau (a ^ {0}, \dots , a ^ {n}) & = \mathrm{Trace} _ {\mathrm{H} ^ {+}} ((a _ {0} - \mathrm{D} _ {1} ^ {- 1} a _ {0} \mathrm{D} _ {1}) \dots (a _ {n} - \mathrm{D} _ {1} ^ {- 1} a _ {n} \mathrm{D} _ {1})) \\ & \quad - \mathrm{Trace} _ {\mathrm{H} ^ {-}} ((a _ {0} - \mathrm{D} _ {2} ^ {- 1} a _ {0} \mathrm{D} _ {2}) \dots (a _ {n} - \mathrm{D} _ {2} ^ {- 1} a _ {n} \mathrm{D} _ {2})). \end{array}
$$

Now the character $\tau_{1}$ of $(\mathbf{H}_{1},\mathbf{F}_{1})$ is given by

$$
\begin{array}{r l} \tau_ {1} (a ^ {0}, \dots , a ^ {n}) & = (2 \pi i) ^ {m} m! \frac {\mathrm{I}}{2} \operatorname{Trace} \left(\left[ \begin{array}{c c} \mathrm{I} & 0 \\ 0 & - \mathrm{I} \end{array} \right] \mathrm{F} _ {1} [ \mathrm{F} _ {1}, a ^ {0} ] \mathrm{F} _ {1} [ \mathrm{F} _ {1}, a ^ {1} ] \dots \mathrm{F} _ {1} [ \mathrm{F} _ {1}, a ^ {n} ]\right) \\ & = (2 \pi i) ^ {m} m! \operatorname{Trace} _ {\mathrm{H} ^ {+}} ((a ^ {0} - \mathrm{D} _ {1} ^ {- 1} a ^ {0} \mathrm{D} _ {1}) \dots (a ^ {n} - \mathrm{D} _ {1} ^ {- 1} a ^ {n} \mathrm{D} _ {1})). \end{array}
$$

Similarly one has

$$
\tau_ {2} (a ^ {0}, \dots , a ^ {n}) = (2 \pi i) ^ {m} m! \operatorname{Trace} _ {\mathrm{H} ^ {-}} ((a _ {0} - \mathrm{D} _ {2} ^ {- 1} a _ {0} \mathrm{D} _ {2}) \dots (a _ {n} - \mathrm{D} _ {2} ^ {- 1} a _ {n} \mathrm{D} _ {2}))
$$

282

Let us now assume that $\mathcal{A}$ is a \*algebra and H a \*module (i.e. $\langle a^{*}\xi, \eta \rangle = \langle \xi, a\eta \rangle$, $\forall \xi, \eta \in \mathrm{H}$, $a \in \mathcal{A}$). For any $\varphi \in \mathrm{C}_{\lambda}^{n}(\mathcal{A})$, let $\varphi^{*}$ be defined by

$$
\varphi^ {*} (a ^ {0} \dots , a ^ {n}) = \overline {{\varphi (a _ {n} ^ {*} , \dots , a _ {0} ^ {*})}} \quad \forall a _ {j} \in \mathscr {A}.
$$

One checks that $\varphi^{*}\in\mathbf{C}_{\lambda}^{n}$ and that $(b\varphi)^{*}=(-1)^{n}b\varphi^{*}$.

Corollary 2. — If D is selfadjoint, then

$$
\tau = ((2 \pi i) ^ {- m} (m!) ^ {- 1} \tau_ {1}) + ((2 \pi i) ^ {- m} (m!) ^ {- 1} \tau_ {1}) ^ {*}.
$$

Proof. — One has  $D_{2}=D_{1}^{*}$ , thus

$$
\begin{array}{r l} \mathrm{Trace} _ {\mathrm{H} ^ {-}} ((a _ {0} - \mathrm{D} _ {2} ^ {- 1} a _ {0} \mathrm{D} _ {2}) & \dots (a _ {n} - \mathrm{D} _ {2} ^ {- 1} a _ {n} \mathrm{D} _ {2})) \\ & = \mathrm{Trace} _ {\mathrm{H} ^ {-}} ((a _ {0} - \mathrm{D} _ {1} ^ {* - 1} a _ {0} \mathrm{D} _ {1} ^ {*}) \dots (a _ {n} - \mathrm{D} _ {1} ^ {* - 1} a _ {n} \mathrm{D} _ {1} ^ {*})) \\ & = (\mathrm{Trace} _ {\mathrm{H} ^ {-}} ((a _ {n} ^ {*} - \mathrm{D} _ {1} a _ {n} ^ {*} \mathrm{D} _ {1} ^ {- 1}) \dots (a _ {0} ^ {*} - \mathrm{D} _ {1} a _ {0} ^ {*} \mathrm{D} _ {1} ^ {- 1}))) ^ {-} \\ & = (\mathrm{Trace} _ {\mathrm{H} ^ {+}} ((\mathrm{D} _ {1} ^ {- 1} a _ {n} ^ {*} \mathrm{D} _ {1} - a _ {n} ^ {*}) \dots (a _ {0} ^ {*} - \mathrm{D} _ {1} ^ {- 1} a _ {0} ^ {*} \mathrm{D} _ {1}))) ^ {-} \\ & = - ((2 \pi i) ^ {- m} (m!) ^ {- 1} \tau_ {1}) ^ {*} (a _ {0}, \dots , a _ {n}). \quad \square \end{array}
$$

We shall define the character of a pair (H, D) satisfying 1) 2) 3) as

$$
\tau (a ^ {0}, \dots , a ^ {n}) = (2 \pi i) ^ {m} m! \frac {\mathrm{I}}{2} \operatorname{Trace} (\varepsilon \mathrm{D} ^ {- 1} [ \mathrm{D}, a ^ {0} ] \dots \mathrm{D} ^ {- 1} [ \mathrm{D}, a ^ {n} ]).
$$

When $\mathbf{D} = \mathbf{F}$ with $\mathbf{F}^2 = \mathbf{i}$ we get the same formula as in section 2. Since $\tau = \frac{\mathbf{i}}{2} (\tau_1 - \tau_2)$ where $\tau_j$ is the character of a Fredholm module determined by (H, D), the results of section 4 still hold for the character $\tau$, i.e. $\tau_{n+2k} = \mathrm{S}^k\tau_n$ in $\mathrm{H}_{\lambda}^{n+2k}(\mathcal{A})$ for any $k = \mathbf{i}, 2 \ldots$. We let $\operatorname{ch}^*(\mathbf{H}, \mathbf{D})$ be the element of $\mathrm{H}^{\mathrm{ev}}(\mathcal{A})$ determined by any of the $\tau_n$.

Corollary 3. — Let $\mathcal{A}$ be a \* algebra, H a $\mathbf{Z}/2$ graded Hilbert space which is a \* module over $\mathcal{A}$, and D a (possibly unbounded) selfadjoint operator in H such that, $\alpha$$\varepsilon\mathbf{D} = -\mathbf{D}\varepsilon$, $\beta$ the domain of D is invariant by any $a \in \mathcal{A}$ and [D, a] is bounded, $\gamma$$\mathbf{D}^{-1} \in \mathcal{L}^p$. Then D satisfies conditions 1) 2) 3) above and for any selfadjoint idempotent $e \in \mathbf{M}_k(\mathcal{A})$, the operator $\mathbf{D}_e = e(\mathbf{D} \otimes \mathbf{1})$$e$ is selfadjoint in $e(\mathbf{H} \otimes \mathbf{C}^k)$. Its kernel is finite dimensional and invariant under $\varepsilon$, with

$$
\text { Signature } \varepsilon / \operatorname{Ker} D _ {e} = \langle [ e ], \operatorname{ch} ^ {*} (H, D) \rangle .
$$

Proof. — Since  $D^{-1} \in L^{p}$ , one has  $D^{-1}[D, a] \in L^{p}$  for all  $a \in A$ , so that D satisfies 1) 2) 3). For the rest of the proof we may assume that k = 1. By  $\beta$ ,  $D_{e}$  is densely defined in eH. It is selfadjoint by [57], since  $D - (e De + (1 - e) D(1 - e))$  is a bounded operator. Let f be the closure of  $D^{-1} e D$ , then f is a bounded operator with  $f - e \in L^{p}$  and  $f^{2} = f$ . Let us show that the kernel of fe in eH is the same as the kernel of  $D_{e}$ . Clearly  $\xi \in Ker D_{e}$  implies  $\xi \in Ker fe$ . Conversely, let  $\xi \in Ker fe$ . Let us show that  $e\xi \in Dom e De$ . Let  $\xi_{n} \in Dom D$ ,  $\xi_{n} \mapsto e\xi$ . Let  $\eta_{n} = f\xi_{n} = D^{-1} e D\xi_{n}$ . One has  $fe\xi = o$ , hence  $\eta_{n} \to o$ . Thus  $\xi_{n} - \eta_{n} \in Dom D$ ,  $\xi_{n} - \eta_{n} \mapsto e\xi$  and  $e D(\xi_{n} - \eta_{n}) = e D\xi_{n} - e D\xi_{n} = o$ . This shows that  $e\xi \in Dom e D$  and that  $e De\xi = o$ .

Now, as $f - e \in \mathcal{L}^p$, $fe$ defines a Fredholm operator from $eH$ to $fH$, and its kernel is finite dimensional. The operator $\varepsilon$ commutes with $fe$ and one has,

$$
\text { Signature } (\varepsilon / \operatorname{Ker} \mathbf {D} _ {e}) = \dim \operatorname{Ker} (f e) _ {e \mathrm{H} ^ {+}} - \dim \operatorname{Ker} (f e) _ {e \mathrm{H} ^ {-}}.
$$

Let us show that the codimension of the range of $fe$ in $f\mathrm{H}^{+}$ is equal to $\dim \operatorname{Ker}(fe)_{e\mathrm{H}^{-}}$. In fact both are equal to the codimension of the range of $e\mathrm{De}\mathrm{D}^{-1}\mathrm{H}^{-}$ in $e\mathrm{H}^{-}$. Thus,

$$
\text { Signature } (\varepsilon / \operatorname{Ker} D _ {e}) = \text { Index } f e: e H ^ {+} \to f H ^ {+}.
$$

With the notation of proposition 1 the right side of the above equality is the index of $(\mathbf{F}_1^+)_e$ so that, by theorem 3.1, it is equal to

$$
\left(\frac {\mathrm{I}}{2 i \pi}\right) ^ {m} \frac {\mathrm{I}}{m !} \tau_ {1} (e, \dots , e).
$$

The conclusion follows from corollary 5 combined with the equality $e = e^{*}$.

In corollary 3 the condition “D is invertible” is still unnatural, we shall now show how to replace it by

$$
(\mathrm{I} + \mathrm{D} ^ {2}) ^ {- 1} \in \mathscr {L} ^ {p / 2}.\tag{\( \gamma' \}
$$

Let H be a Z/2 graded Hilbert space which is a module over the algebra A. Let D be a (possibly unbounded) selfadjoint operator in H verifying  $\alpha$  and  $\beta$  of Corollary 3. To make D invertible we shall form its cup product (cf. [6]) with the following simple Fredholm module  $(\mathbf{H}_{\mathbf{c}}, \mathbf{F}_{\mathbf{c}})$  over the algebra C. We let  $H_{c}$  be the Z/2 graded Hilbert space  $H_{c}^{\pm} = C$, we let C act on the left in  $H_{c}$  by  $\lambda \to \begin{bmatrix} \lambda & 0 \\ 0 & 0 \end{bmatrix} \in \mathcal{L}(\mathbf{H}_{\mathbf{c}})$, and we let  $F_{c} = \begin{bmatrix} 0 & I \\ I & 0 \end{bmatrix}$.

Proposition 4. — a) Let $\widetilde{\mathbf{H}} = \mathbf{H} \widehat{\otimes} \mathbf{H}_{\mathbf{C}}$ be the graded tensor product of $\mathbf{H}$ by $\mathbf{H}_{\mathbf{C}}$ viewed as an $\mathcal{A} \otimes \mathbf{C} = \mathcal{A}$ left module. For any $m \neq 0$, $m \in \mathbf{R}$, the operator $\mathbf{D}_m = \mathbf{D} \widehat{\otimes} \mathbf{i} + m \mathbf{i} \widehat{\otimes} \mathbf{F}_{\mathbf{C}}$ is an invertible selfadjoint operator in $\widetilde{\mathbf{H}}$ which satisfies $\alpha)$$\beta)$ if $\mathbf{D}$ satisfies $\alpha)$$\beta)$$\gamma'$.

b) Corollary 3 still holds under this weaker hypothesis.

c) $\operatorname{ch}^{*}(\mathbf{H}, \mathbf{D}_{m}) = [\tau_{m}] \in \mathrm{H}^{\mathrm{ev}}(\mathcal{A})$ is independent of $m$ (where $\tau_{m}$ is the character of $(\mathbf{H}, \mathbf{D}_{m})$).

Proof. — a) One has  $\mathbf{D}_{m}^{2} = (\mathbf{D}^{2} + m^{2}) \hat{\otimes} \mathbf{I}$ , so that  $D_{m}$  is invertible. Moreover  $|\mathbf{D}_{m}^{-1}| = (\mathbf{D}^{2} + m^{2})^{-1/2} \hat{\otimes} \mathbf{I} \in \mathcal{L}^{p}$ . Since conditions  $\alpha) \beta$  are obviously satisfied by  $D_{m}$  we get a).

b) Let $e_{\mathbf{G}} = \begin{bmatrix} \mathrm{I} & 0 \\ 0 & 0 \end{bmatrix} \in \mathcal{L}(\mathrm{H}_{\mathbf{G}})$. For any $e = e^2 = e^* \in \mathcal{A}$ one has

$$
(e \hat {\otimes} e _ {\mathbf {c}}) \mathbf {D} _ {m} (e \hat {\otimes} e _ {\mathbf {c}}) = e \mathbf {D} e \hat {\otimes} e _ {\mathbf {c}},
$$

thus

$$
\begin{array}{r l} \text { Signature } (\varepsilon / \operatorname{Ker} e \mathbf {D} e) & = \text { Signature } (\varepsilon \otimes \varepsilon_ {\mathbf {c}} / \operatorname{Ker} (e \hat {\otimes} e _ {\mathbf {c}}) \mathbf {D} _ {m} (e \hat {\otimes} e _ {\mathbf {c}})) = \langle [ e ], \mathrm{ch} ^ {*} (\mathbf {H}, \mathbf {D} _ {m}) \rangle \end{array}
$$

by corollary 3.

c) Follows from Corollary 2 and Lemma 5.1. □

284

The above construction of the operator  $D_{m}$  from the operator D associates to the Dirac operator in  $R^{3}$  the Dirac Hamiltonian with mass m.

Let now V be a compact even dimensional Spin manifold. Let g be a Riemannian metric on V, S the bundle of complex spinors and D the Dirac operator in  $\mathrm{L}^{2}(\mathrm{V},\mathrm{S})=\mathrm{H}$ . By construction H is a Z/2 graded Hilbert space, with  $\mathrm{H}^{\pm}=\mathrm{L}^{2}(\mathrm{V},\mathrm{S}^{\pm})$  and is a module over  $\mathcal{A}=\mathbf{C}^{\infty}(\mathrm{V})$ . One has:

$\alpha)\varepsilon \mathbf{D} = -\mathbf{D}\varepsilon ;$

$\beta)$ the domain of $\mathbf{D}$ is invariant under any $f \in \mathcal{A}$ and $[\mathbf{D}, f]$ is bounded; $\gamma')$ ($1 + \mathbf{D}^2)^{-1} \in \mathcal{L}^{p/2}$ for any $p > \dim V$.

Thus proposition 4 applies and combined with proposition 1 b) it yields for each $m \in \mathbf{R}$, $m \neq 0$ an element $\tau_m$ of $Z_\lambda^{\dim V}(C^\infty(V))$, the character of $(\tilde{H}, D_m)$.

Theorem 5. — a) With the above notation, $\tau_{m}(f^{0},\ldots,f^{n})$ is convergent, when $m\to\infty$, for any $f^{0},\ldots,f^{n}\in\mathbf{C}^{\infty}(\mathrm{V})$.

b) The limit $\tau(f^0, \ldots, f^n)$ is given by

$$
\begin{array}{r l} \tau (f ^ {0}, \ldots , f ^ {n}) & = \int f ^ {0} d f ^ {1} \wedge \ldots \wedge d f ^ {n} + (\mathrm{S} ^ {2} \widetilde {\omega} _ {1}) (f ^ {0}, \ldots , f ^ {n}) \\ & \quad + (\mathrm{S} ^ {4} \widetilde {\omega} _ {2}) (f ^ {0}, \ldots , f ^ {n}) + \ldots + \mathrm{S} ^ {n / 2} \widetilde {\omega} _ {\mathrm{E} (n / 4)} (f ^ {0}, \ldots , f ^ {n}) \end{array}
$$

where S is the canonical operation  $Z_{\lambda}^{k} \to Z_{\lambda}^{k+2}$  (cf. Part II),  $\omega_{j}$  is the differential form  $\hat{\mathbf{A}}_{j}(p_{1}, \ldots, p_{j})$  describing the component of degree 4j of the  $\hat{A}$  genus of V in terms of the curvature matrix of the metric g, and is considered as an element of  $\mathbf{Z}_{\lambda}^{n-4j}(\mathcal{A})$  by the formula

$$
\widetilde {\omega} _ {j} \left(f ^ {0}, f ^ {1}, \dots , f ^ {n - 4 j}\right) = \int_ {\mathrm{V}} f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {n - 4 j} \wedge \omega_ {j}.
$$

Here the manifold V is oriented by its Spin structure.

This theorem will be proven in part III using the technique introduced by E. Getzler in [28].

## 7. The odd dimensional case

For nuclear C\*-algebras A, there are two equivalent descriptions of the K-homology K$^{1}$(A). The first, due to Brown, Douglas and Fillmore ([11]) classifies extensions of A by the algebra $\mathcal{H}$ of compact operators, i.e. exact sequences, of C\*-algebras and homomorphisms

$$
0 \rightarrow \mathcal {K} \rightarrow \mathcal {E} \rightarrow A \rightarrow 0.
$$

The second, due to Kasparov classifies Fredholm modules over the Z/2 graded C\*-algebra A ⊗ C₁ where C₁ is the following Z/2 graded Clifford algebra over C,

$$
\mathbf {C} _ {1} ^ {+} = \{\lambda \mathrm{I}, \lambda \in \mathbf {C} \}, \quad \mathrm{Itheunitof} \mathbf {C} _ {1}
$$

$$
\mathbf {C} _ {1} ^ {-} = \{\lambda \alpha , \lambda \in \mathbf {C} \}, \quad \alpha^ {2} = 1.
$$

In the work of Helton and Howe on operators with trace class commutators and in the further work [23] [12] [20], differential geometric invariants on V are assigned to an exact sequence of the form,

$$
0 \rightarrow \mathscr {L} ^ {p} (H) \rightarrow \mathscr {E} \rightarrow C ^ {\infty} (V) \rightarrow 0.
$$

In this section we shall clarify the link of these invariants with our Chern character. We show that, given a trivially Z/2 graded algebra A over C,

1) a $p$-summable Fredholm module (H, F) over $\mathcal{A} \otimes \mathrm{C}_1$ yields an exact sequence,

$$
0 \rightarrow \mathscr {L} ^ {p / 2} \rightarrow \mathscr {E} \rightarrow \mathscr {A} \rightarrow 0;
$$

2) the cohomology class $[\tau] \in \mathrm{H}_{\lambda}^{2m-1}(\mathcal{A})$, $m \in \mathbf{N}$, $m \geq p/2$ of the character of the above Fredholm module only depends upon the associated exact sequence, and can be defined directly (without (H, F));

3) when $\mathcal{A} = \mathrm{C}^{\infty}(\mathrm{V})$, the fundamental trace form $\varphi$ of Helton and Howe ([31]) is obtained from the character $\tau$ by complete antisymmetrisation: $\varphi = \Sigma \varepsilon (\sigma)\tau^{\sigma}$. Hence, using the results of part II (lemma 45 a) and theorem 46) we see that $\varphi$ is the image of $\tau$ under the canonical map

$$
\mathrm{I}: \mathrm{H} _ {\lambda} ^ {2 m - 1} (\mathbf {C} ^ {\infty} (\mathrm{V})) \rightarrow \mathrm{H} ^ {2 m - 1} (\mathbf {C} ^ {\infty} (\mathrm{V}), \mathbf {C} ^ {\infty} (\mathrm{V}) ^ {*}).
$$

Since the kernel of I is the direct sum of the de Rham homology groups

$$
\mathrm{H} _ {2 m - 3} (\mathrm{V}, \mathbf {C}) \oplus \mathrm{H} _ {2 m - 5} (\mathrm{V}, \mathbf {C}) \oplus \dots \oplus \mathrm{H} _ {1} (\mathrm{V}, \mathbf {C}),
$$

we see that some information is lost in the process when the latter group is not trivial. This fits with the results of [31] and [25] where the fundamental trace form is used either in low dimensions or for spheres. Our formalism thus gives an explicit formula for the lower homology classes of Helton and Howe ([31]). Let us begin with 1). We let $\mathbf{H}_1$ be the $\mathbf{Z}/2$ graded Hilbert space $\mathbf{H}_1^+ = \mathbf{C}$, $\mathbf{H}_1^- = \mathbf{C}$. We let $\mathbf{C}_1$ act in $\mathbf{H}_1$ by,

$$
\lambda + \mu \alpha \mapsto \left[ \begin{array}{c c} \lambda & \mu \\ \mu & \lambda \end{array} \right] \in \mathcal {L} (\mathrm{H} _ {1}).
$$

Lemma 1. — Let A be a trivially Z/2 graded algebra, (K, P) a pair, where K is a Hilbert space in which A acts (by bounded operators), while  $\mathbf{P} \in \mathcal{L}(\mathbf{K})$  satisfies the conditions

$$
a) [ \mathbf {P}, b ] \in \mathscr {L} ^ {p} (\mathbf {K}), \forall b \in \mathscr {A}, b) \quad \mathbf {P} ^ {2} = 1.
$$

Then let $\mathbf{H} = \mathbf{K} \otimes \mathbf{H}_1$ be the obvious $\mathcal{A} \otimes \mathbf{C}_1$ module, and put $\mathbf{F} = i\begin{bmatrix} 0 & \mathbf{P} \\ -\mathbf{P} & 0 \end{bmatrix}$. Then (H, F) is a $p$-summable Fredholm module over the $\mathbf{Z}/2$ graded algebra $\mathcal{A} \otimes \mathbf{C}_1$.

Proof. — By construction H is a Z/2 graded  $A \otimes C_{1}$  module. The operator F satisfies  $\varepsilon F = -F\varepsilon$ ,  $F^{2} = 1$ . Finally for any  $x = a \otimes 1 + b \otimes \alpha \in A \otimes C_{1}$  the graded commutator [F, x] is given by

$$
i [ \mathrm{F}, x ] = \left[ \begin{array}{c c} - [ \mathrm{P}, b ] & - [ \mathrm{P}, a ] \\ [ \mathrm{P}, a ] & [ \mathrm{P}, b ] \end{array} \right] \in \mathscr {L} ^ {p} (\mathrm{H}). \quad \square
$$

286

Lemma 2. — Let $\tau_{n}$ be the $n$-dimensional character of (H, F) for $n \geq p - 1$. Then, a) if $n$ is even one has $\tau_{n} = 0$;

b) if $n$ is odd, one has $\tau_n = \tau_n' \otimes \gamma$, where $\gamma$ is the graded trace on $\mathbf{C}_1$, $\gamma(\lambda + \mu\alpha) = \mu \forall \lambda + \mu\alpha \in \mathbf{C}_1$, and where

$$
\tau_ {n} ^ {\prime} \left(a ^ {0}, \dots , a ^ {n}\right) = (- 1) ^ {\frac {n - 1}{2}} c _ {n} \operatorname{Trace} \left(\mathrm{P} [ \mathrm{P}, a ^ {0} ] [ \mathrm{P}, a ^ {1} ] \dots [ \mathrm{P}, a ^ {n} ]\right), \quad \forall a ^ {i} \in \mathscr {A};
$$

c) one has $\tau_n' \in \mathbf{Z}_\lambda^n(\mathcal{A})$.

Proof. — One has by definition (cf. remark 1.6)

$$
\tau_ {n} (x ^ {0}, \dots , x ^ {n}) = (- \mathrm{I}) ^ {q} c _ {n} \operatorname{Tr} _ {s} (x ^ {0} d x ^ {1} \dots d x ^ {n}), \quad d x ^ {j} = i [ \mathrm{F}, x ^ {j} ],
$$

for $x^0, \ldots, x^n \in \mathcal{A} \otimes \mathbf{C}_1$, $x^i$ homogeneous, $q = \Sigma \deg(x^{2k+1})$. Replacing $\mathcal{A}$ by $\tilde{\mathcal{A}}$ we may assume that $\mathcal{A}$ is unital and that its unit acts as the identity in $K$. We shorten the notation and replace $i \otimes \alpha$ by $\alpha$ in $\mathcal{A} \otimes \mathbf{C}_1$. It acts in $H$ by the matrix $\alpha = \begin{bmatrix} 0 & I \\ I & 0 \end{bmatrix}$. One has $x\alpha = \alpha x$ for $x \in \mathcal{A} \otimes \mathbf{C}_1$ and $(\varepsilon F) \alpha = \alpha(\varepsilon F)$; this shows that when $n$ is even, any $\omega \in \Omega^n$ satisfies

$$
\alpha \omega = \omega \alpha .
$$

As $\varepsilon \alpha = -\alpha \varepsilon$, this shows that for $n$ even, $n \geq p - 1$, one has

$$
\operatorname{Tr} _ {s} (\omega) = 0 \quad \forall \omega \in \Omega^ {n}.
$$

Let $n$ be odd. By remark 1.6, $\tau_n(x^0, \ldots, x^n) = 0$ for $x^i \in \mathcal{A} \otimes \mathbf{C}_1$, $x^i$ homogeneous, $\Sigma \partial x^i = 0 \pmod{2}$.

Since $\mathbf{F}\alpha = -\alpha \mathbf{F}$, one has $d\alpha = 0$, and hence, for $a^j \in \mathcal{A}$, $\varepsilon_j \in \{0, 1\}$, $\Sigma \varepsilon_j = 1 \pmod{2}$,

$$
\tau_ {n} (a ^ {0} \alpha^ {\varepsilon_ {0}}, \dots , a ^ {n} \alpha^ {\varepsilon_ {n}}) = \tau_ {n} (\alpha a ^ {0}, a ^ {1}, \dots , a ^ {n}).
$$

Now for $a \in \mathcal{A}$, one has $da = i[\mathrm{F}, a] = [\mathrm{P}, a] \otimes \begin{bmatrix} 0 & \mathrm{I} \\ -\mathrm{I} & 0 \end{bmatrix}$, thus, with

$$
\omega = \alpha a ^ {0} d a ^ {1} \dots d a ^ {n},
$$

$$
\begin{array}{r l} \frac {\mathrm{I}}{2} \mathrm{F} (\mathrm{F} \varepsilon \omega - \omega \mathrm{F} \varepsilon) & = \frac {\mathrm{I}}{2} i \mathrm{F} \alpha \varepsilon d a ^ {0} \dots d a ^ {n} \\ & = \frac {\mathrm{I}}{2} (- \mathrm{I}) ^ {\frac {n - 1}{2}} (\mathrm{P} [ \mathrm{P}, a ^ {0} ] \dots [ \mathrm{P}, a ^ {n} ]) \otimes \left[ \begin{array}{l l} \mathrm{I} & 0 \\ 0 & \mathrm{I} \end{array} \right]. \end{array}
$$

This shows that

$$
\tau_ {n} (a ^ {0} \alpha^ {\varepsilon_ {0}}, \dots , a ^ {n} \alpha^ {\varepsilon_ {n}}) = \tau_ {n} ^ {\prime} (a ^ {0}, \dots , a ^ {n}) \gamma (\alpha^ {\varepsilon_ {0}} \alpha^ {\varepsilon_ {1}} \dots \alpha^ {\varepsilon_ {n}}).
$$

$$
\tau_ {n} ^ {\prime} \in \mathbf {Z} _ {\lambda} ^ {n} (\mathcal {A}). \quad \square
$$

Finally, the character $\tau_{n}$ satisfies conditions $a')$$b')$ of remark 1.6 $\gamma$). It follows that

To any pair (K, P) verifying the conditions a) b) of lemma 1, we have thus associated, for any odd $n \geq p - 1$, the $(n + 1)$-linear functional $\tau_n' \in Z_\lambda^n(\mathcal{A})$. We shall now show that the class of $\tau_n'$ in $\mathrm{H}_\lambda^n(\mathcal{A})$ only depends on the extension of $\mathcal{A}$ by $\mathcal{L}^{p/2}$ associated to (K, P) as follows,

Proposition 3. — Let A, K, P be as above and put  $E_{0} = \frac{1 + P}{2} \in \mathcal{L}(K)$ , E = Range of  $E_{0}$ ,  $\rho(b) = E_{0} bE_{0} \in \mathcal{L}(E)$  for any  $b \in A$ .

a) One has $\rho(ab) - \rho(a)\rho(b) \in \mathcal{L}^{p/2}(\mathrm{E})$ for all $a, b \in \mathcal{A}$.

b) Let $\mathcal{E} = \rho (\mathcal{A}) + \mathcal{L}^{p / 2}(\mathrm{E})\subset \mathcal{L}(\mathrm{E}),$ and $\mathcal{A}'$ be the quotient of $\mathcal{A}$ by the ideal

$\mathcal{A}'' = \{a \in \mathcal{A}, \rho(a) \in \mathcal{L}^{p/2}(\mathrm{E})\}$; then one has a natural exact sequence,

$$
0 \rightarrow \mathscr {L} ^ {p / 2} (\mathrm{E}) \rightarrow \mathscr {E} \rightarrow \mathscr {A} ^ {\prime} \rightarrow 0.
$$

Proof. — a) Since  $P^{2} = I$ , one has  $E_{0}^{2} = E_{0}$ . Hence

$$
\mathrm{E} _ {0} a b \mathrm{E} _ {0} - \mathrm{E} _ {0} a \mathrm{E} _ {0} b \mathrm{E} _ {0} = - \mathrm{E} _ {0} [ \mathrm{E} _ {0}, a ] [ \mathrm{E} _ {0}, b ] \in \mathscr {L} ^ {p / 2} (\mathrm{K}).
$$

b) By a), $\mathcal{E}$ is a subalgebra of $\mathcal{L}(\mathrm{E})$. One has $\mathcal{L}^{p/2}(\mathrm{E}) \subset \mathcal{E}$ and $\rho$ yields an isomorphism $\rho'$ of $\mathcal{A}'$ with $\mathcal{E}/\mathcal{L}^{p/2}$. $\square$

Let $J = \mathcal{L}^{p/2} \subset \mathcal{E}$. Then for any integer $m \geq p/2$ we have $J^m \subset \mathcal{L}^1$, so that the trace defines a linear functional $\tau$ on $J^m$ such that

$$
\tau (a b) = \tau (b a) \quad \text { for } a \in \mathbf {J} ^ {k}, b \in \mathbf {J} ^ {q}, k + q \geq m.
$$

Moreover $\rho: \mathcal{A} \to \mathcal{E}$ is multiplicative modulo J. We shall show in this generality how to get an element $\varphi_{2m-1}$ of $Z_{\lambda}^{2m-1}(\mathcal{A})$ and relate it to $\tau_n'$ in the above situation.

Proposition 4. — Let $\Sigma$ be an algebra, $J \subset \Sigma$ a two-sided ideal, $m \in \mathbf{N}$, and $\tau$ a linear functional on $J^m$ such that

$$
\tau (a b) = \tau (b a) \quad f o r a \in J ^ {k}, b \in J ^ {q}, k + q = m.
$$

Let $\rho : \mathcal{A} \to \Sigma$ be a linear map which is multiplicative modulo J.

a) Let $\varphi$ be the 2m-linear functional on $\mathcal{A}$ given by

$$
\varphi (a ^ {0}, \dots , a ^ {2 m - 1}) = \tau (\varepsilon_ {0} \varepsilon_ {2} \dots \varepsilon_ {2 m - 2}) - \tau (\varepsilon_ {1} \varepsilon_ {3} \dots \varepsilon_ {2 m - 1}),
$$

where

$$
\varepsilon_ {j} = \rho (a ^ {j} a ^ {j + 1}) - \rho (a ^ {j}) \rho (a ^ {j + 1}), j = 0, I, \dots , 2 m - I.
$$

Then $\varphi \in Z_{\lambda}^{2m - 1}(\mathcal{A})$

b) Let $\rho': \mathcal{A} \to \Sigma$ satisfy the same conditions as $\rho$, with $\rho(a) - \rho'(a) \in J$ for $a \in \mathcal{A}$; then, with obvious notation, one has $\varphi' - \varphi \in B_{\lambda}^{2m-1}(\mathcal{A})$.

c) Let (K, P) satisfy conditions a) b) of lemma 1 and $\tau_n'$ be given by lemma 2, for $n = 2m - 1$, $m \geq p$. Let $\Sigma = \mathcal{E}$, $J = \mathcal{L}^{p/2}(E)$, and $\rho$ be as in proposition 3. Then the corresponding $\varphi \in Z_{\lambda}^{2m-1}(\mathcal{A})$ satisfies

$$
\varphi = - \left(2 ^ {- (n + 2)} c _ {n} ^ {- 1}\right) \tau_ {n} ^ {\prime}.
$$

Proof. — a) One has, by construction,

$$
\varphi (a ^ {1}, \dots , a ^ {2 m - 1}, a ^ {0}) = - \varphi (a ^ {0}, \dots , a ^ {2 m - 1}), \quad \forall a ^ {j} \in \mathscr {A}.
$$

With the notations of a), let $\varphi^{+} = \tau(\varepsilon_{0}\varepsilon_{2}\ldots\varepsilon_{2m-2})$. One has

$$
\begin{array}{r l} \rho (a ^ {j} a ^ {j + 1} a ^ {j + 2}) - \rho (a ^ {j} a ^ {j + 1}) \rho (a ^ {j + 2}) - (\rho (a ^ {j} a ^ {j + 1} a ^ {j + 2}) - \rho (a ^ {j}) \rho (a ^ {j + 1} a ^ {j + 2})) \\ = \rho (a ^ {j}) \rho (a ^ {j + 1} a ^ {j + 2}) - \rho (a ^ {j} a ^ {j + 1}) \rho (a ^ {j + 2}) = \rho (a ^ {j}) \varepsilon_ {j + 1} - \varepsilon_ {j} \rho (a ^ {j + 2}). \end{array}
$$

Using this equality, we get

Similarly, with $\varphi^{-} = \varphi^{+} - \varphi$, we have

$$
\begin{array}{r l} b \varphi^ {-} (a ^ {0}, \dots , a ^ {n + 1}) - \varphi^ {-} (a ^ {0} a ^ {1}, a ^ {2}, \dots , a ^ {n + 1}) \\ & = - \tau (\rho (a ^ {1}) \varepsilon_ {2} \varepsilon_ {4} \dots \varepsilon_ {n + 1} - \varepsilon_ {1} \varepsilon_ {3} \dots \varepsilon_ {n} \rho (a ^ {0})). \end{array}
$$

Thus

$$
\begin{array}{r l} b \varphi (a ^ {0}, \dots , a ^ {n + 1}) & = \varphi^ {+} (a ^ {n + 1} a ^ {0}, \dots , a ^ {n}) - \tau (\varepsilon_ {0} \dots \varepsilon_ {n - 1} \rho (a ^ {n + 1})) \\ & - \varphi^ {-} (a ^ {0} a ^ {1}, \dots , a ^ {n + 1}) + \tau (\rho (a ^ {1}) \varepsilon_ {2} \dots \varepsilon_ {n + 1}) = \tau (\mathrm{A} \varepsilon_ {2} \dots \varepsilon_ {n - 1}) \end{array}
$$

where

$$
\begin{array}{r l} \mathrm{A} & = \rho (a ^ {n + 1} a ^ {0} a ^ {1}) - \rho (a ^ {n + 1} a ^ {0}) \rho (a ^ {1}) - \rho (a ^ {n + 1}) \varepsilon_ {0} - (\rho (a ^ {n + 1} a ^ {0} a ^ {1}) \\ & \qquad - \rho (a ^ {n + 1}) \rho (a ^ {0} a ^ {1})) + \varepsilon_ {n + 1} \rho (a ^ {1}) = 0. \end{array}
$$

Therefore $\varphi \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$

b) Let $\mathbf{L} = \rho' - \rho$; then $\mathbf{L}$ is a linear map from $\mathcal{A}$ to $\mathbf{J}$. With $\rho_t = \rho + t\mathbf{L}$ it is enough to show that the cocycle $\varphi_t$ associated to $\rho_t$, satisfies $\frac{d}{dt}\varphi_t = b\psi_t$ for a continuous family $\psi_t \in \mathbf{C}_\lambda^{n-1}(\mathcal{A})$. Clearly it is enough to do it for $t = 0$. Letting $\varphi' = \left(\frac{d}{dt}\varphi_t\right)_{t=0}$, we have

$$
\varphi^ {\prime} (a ^ {0}, \dots , a ^ {n}) = \tau (\mathrm{A} - \mathrm{B}),
$$

where

$$
A = \varepsilon_ {0} ^ {\prime} \varepsilon_ {2} \dots \varepsilon_ {n - 1} + \varepsilon_ {0} \varepsilon_ {2} ^ {\prime} \varepsilon_ {4} \dots \varepsilon_ {n - 1} + \dots + \varepsilon_ {0} \varepsilon_ {2} \dots \varepsilon_ {n - 1} ^ {\prime},
$$

$$
\mathrm{B} = \varepsilon_ {1} ^ {\prime} \varepsilon_ {3} \dots \varepsilon_ {n} + \varepsilon_ {1} \varepsilon_ {3} ^ {\prime} \dots \varepsilon_ {n} + \dots + \varepsilon_ {1} \varepsilon_ {3} \dots \varepsilon_ {n} ^ {\prime}
$$

and

$$
\varepsilon_ {j} ^ {\prime} = \mathrm{L} (a ^ {j} a ^ {j + 1}) - \rho (a ^ {j}) \mathrm{L} (a ^ {j + 1}) - \mathrm{L} (a ^ {j}) \rho (a ^ {j + 1}).
$$

Let $\psi_0(a^0, \ldots, a^{n-1}) = \tau(\mathbf{L}(a^0) \varepsilon_1 \varepsilon_3 \ldots \varepsilon_{n-2})$ and let

$$
\psi_ {j} (a ^ {0}, \dots , a ^ {n - 1}) = \psi_ {0} (a ^ {j}, a ^ {j + 1}, \dots , a ^ {j - 1}).
$$

Using the same equality as in a) we obtain

$$
\begin{array}{r l} & b \psi_ {2 k} (a ^ {0}, \ldots , a ^ {n}) = \tau ((\rho (a ^ {0}) \varepsilon_ {1} \varepsilon_ {3} \ldots \mathrm{L} (a ^ {2 k + 1}) \ldots \varepsilon_ {n - 1}) \\ & \quad - (\varepsilon_ {0} \ldots \varepsilon_ {2 k - 2} \rho (a ^ {2 k}) \mathrm{L} (a ^ {2 k + 1}) \ldots \varepsilon_ {n - 1}) \\ & \qquad \qquad + (\varepsilon_ {0} \ldots \varepsilon_ {2 k - 2} \mathrm{L} (a ^ {2 k} a ^ {2 k + 1}) \ldots \varepsilon_ {n - 1}) \\ & \quad - (\varepsilon_ {0} \ldots \varepsilon_ {2 k - 2} \mathrm{L} (a ^ {2 k}) \rho (a ^ {2 k + 1}) \ldots \varepsilon_ {n - 1}) \\ & \qquad \qquad + (\varepsilon_ {0} \ldots \varepsilon_ {2 k - 2} \mathrm{L} (a ^ {2 k}) \varepsilon_ {2 k + 1} \ldots \varepsilon_ {n - 2} \rho (a ^ {n})) \\ & \quad - (\rho (a ^ {n} a ^ {0} a ^ {1}) - \rho (a ^ {n} a ^ {0}) \rho (a ^ {1})) \varepsilon_ {2} \ldots \varepsilon_ {2 k - 2} \mathrm{L} (a ^ {2 k}) \varepsilon_ {2 k + 1} \ldots \varepsilon_ {n - 2})). \end{array}
$$

289

The last two terms cancel the first two in

$$
\begin{array}{r l} b \psi_ {2 k - 1} (a ^ {0}, \dots , a ^ {n}) & = \tau ((\rho (a ^ {n} a ^ {0} a ^ {1}) \\ & \quad - \rho (a ^ {n}) \rho (a ^ {0} a ^ {1})) \varepsilon_ {2} \dots \varepsilon_ {2 k - 2} \mathbf {L} (a ^ {2 k}) \dots \varepsilon_ {n - 2}) \\ & \quad - (\rho (a ^ {1}) \varepsilon_ {2} \dots \mathbf {L} (a ^ {2 k}) \dots \varepsilon_ {n}) - (\varepsilon_ {1} \dots \varepsilon_ {2 k - 3} \varepsilon_ {2 k - 1} ^ {\prime} \dots \varepsilon_ {n}) \\ & \quad - (\varepsilon_ {1} \dots \mathbf {L} (a ^ {2 k - 1}) \dots \varepsilon_ {n - 1} \rho (a ^ {0})). \end{array}
$$

Thus we get, for $k = 1, 2, \ldots, m - 1$,

$$
\begin{array}{l} b (\psi_ {2 k - 1} + \psi_ {2 k}) (a ^ {0}, \dots , a ^ {n}) = \tau ((\rho (a ^ {0}) \varepsilon_ {1} \dots \varepsilon_ {2 k - 1} L (a ^ {2 k + 1}) \dots \varepsilon_ {n - 1}) \\ \quad - (\rho (a ^ {0}) \varepsilon_ {1} \dots \varepsilon_ {2 k - 3} L (a ^ {2 k - 1}) \dots \varepsilon_ {n - 1}) + (\varepsilon_ {0} \dots \varepsilon_ {2 k - 2} \varepsilon_ {2 k} ^ {\prime} \dots \varepsilon_ {n - 1}) \\ \quad - (\varepsilon_ {1} \dots \varepsilon_ {2 k - 3} \varepsilon_ {2 k - 1} ^ {\prime} \dots \varepsilon_ {n})). \end{array}
$$

As

$$
\begin{array}{r l} b \psi_ {0} (a ^ {0}, \dots , a ^ {n}) & = \tau ((\rho (a ^ {0}) \mathrm{L} (a ^ {1}) \varepsilon_ {2} \dots \varepsilon_ {n - 1}) - (\rho (a ^ {0}) \varepsilon_ {1} \dots \mathrm{L} (a ^ {n})) \\ & \quad + (\varepsilon_ {0} ^ {\prime} \varepsilon_ {2} \dots \varepsilon_ {n - 1}) - (\varepsilon_ {1} \dots \varepsilon_ {n - 2} \varepsilon_ {n} ^ {\prime}), \end{array}
$$

one obtains

$$
\sum_ {j = 0} ^ {n - 1} b \psi_ {j} = \varphi^ {\prime}.
$$

c) Let $\rho(a) = \mathrm{E}_0 a\mathrm{E}_0 \in \mathcal{L}(\mathrm{E})$, where $\mathrm{E}_0 = \frac{\mathrm{i} + \mathrm{P}}{2}$. One has

$$
\rho \left(a ^ {0} a ^ {1}\right) - \rho \left(a ^ {0}\right) \rho \left(a ^ {1}\right) = - \mathrm{E} _ {0} \left[ \mathrm{E} _ {0}, a ^ {0} \right] \left[ \mathrm{E} _ {0}, a ^ {1} \right] = - \frac {\mathrm{I}}{4} \mathrm{E} _ {0} [ \mathrm{P}, a ^ {0} ] [ \mathrm{P}, a ^ {1} ].
$$

Therefore, since  $E_{0}$  commutes with  $[P, a^{0}]$$[P, a^{1}]$ ,

$$
\prod_ {k = 0} ^ {m - 1} \left(\rho (a ^ {2 k} a ^ {2 k + 1}) - \rho (a ^ {2 k}) \rho (a ^ {2 k + 1})\right) = (- 4) ^ {- m} \mathrm{E} _ {0} \prod_ {j = 0} ^ {n} [ \mathrm{P}, a ^ {j} ].
$$

Thus we obtain

$$
\begin{array}{r l} \varphi (a ^ {0}, \dots , a ^ {2 m - 1}) & = \operatorname{Trace} (\varepsilon_ {0} \varepsilon_ {2} \dots \varepsilon_ {2 m - 2}) - \operatorname{Trace} (\varepsilon_ {1} \varepsilon_ {3} \dots \varepsilon_ {2 m - 1}) \\ & = (- 4) ^ {- m} \operatorname{Trace} (\mathrm{E} _ {0} (\prod_ {j = 0} ^ {n} [ \mathrm{P}, a ^ {j} ] - \prod_ {j = 0} ^ {n} [ \mathrm{P}, a ^ {j + 1} ])). \end{array}
$$

Similarly, if we let  $E_{0}^{\prime} = \mathtt{I} - E_{0}$ ,  $E^{\prime} = \text{Range of } E_{0}^{\prime}$ ,  $\rho^{\prime}(a) = E_{0}^{\prime} a E_{0}^{\prime} \in \mathcal{L}(E^{\prime})$  for  $a \in A$ , we have, with obvious notation,

$$
\varphi^ {\prime} (a ^ {0}, \dots , a ^ {2 m - 1}) = (- 4) ^ {- m} \operatorname{Trace} (\mathrm{E} _ {0} ^ {\prime} (\prod_ {j = 0} ^ {n} [ \mathrm{P}, a ^ {j} ] - \prod_ {j = 0} ^ {n} [ \mathrm{P}, a ^ {j + 1} ])).
$$

One has $\mathbf{P} = 2\mathbf{E}_0 - \mathbf{i} = \mathbf{E}_0 - \mathbf{E}_0'$, thus

$$
\varphi - \varphi^ {\prime} = (- 4) ^ {- m} (- \mathrm{I}) ^ {m - 1} (c _ {m}) ^ {- 1} \tau_ {n} ^ {\prime}.
$$

Since $\mathbf{E}_0 + \mathbf{E}_0' = \mathbf{i}$, one has

$$
\left(\varphi + \varphi^ {\prime}\right) \left(a ^ {0}, \dots , a ^ {n}\right) = (- 4) ^ {- m} \operatorname{Trace} \left(\prod_ {j = 0} ^ {n} [ P, a ^ {j} ] - \prod_ {j = 0} ^ {n} [ P, a ^ {j + 1} ]\right) = 0.
$$

Thus $\varphi = -2^{-2m - 1}c_n^{-1}\tau_n'$.

290

The construction of the character of an extension of A by  $L^{p/2}$  can be summarized as follows:

Theorem 5. — a) Let E be a Hilbert space, $\rho$ a linear map of $\mathcal{A}$ in $\mathcal{L}(\mathbf{E})$ which is multiplicative modulo $\mathcal{L}^{p/2}$; then the following functional $\tau_n$, $n = 2m - 1$, $m \geq p/2$ belongs to $\mathbf{Z}_{\lambda}^{n}(\mathcal{A})$:

$$
\tau_ {n} \left(a ^ {0}, \dots , a ^ {n}\right) = - 2 ^ {n + 2} c _ {n} \operatorname{Trace} \left(\left(\varepsilon_ {0} \varepsilon_ {2} \dots \varepsilon_ {n - 1}\right) - \left(\varepsilon_ {1} \varepsilon_ {3} \dots \varepsilon_ {n}\right)\right),
$$

where $\varepsilon_{j} = \rho (a^{j}a^{j + 1}) - \rho (a^{j})\rho (a^{j + 1}).$

b) The class of $\tau_{n}$ in $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$ depends only on the quotient homomorphism $\mathcal{A} \to \mathcal{L}(\mathrm{E}) / \mathcal{L}^{p/2}(\mathrm{E})$.

c) The class of $\tau_{n}$ in $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$ is unaffected by a homotopy $\rho_{t}$ such that

1) $||\rho_t(ab) - \rho_t(a)\rho_t(b)||_{p/2}$ is bounded on [0, 1] for any $a, b \in \mathcal{A}$;

2) for $a \in \mathcal{A}$, $\xi \in \mathbf{E}$, the map $t \to \rho_t(a)$$\xi$ is $\mathbf{C}^1$.

d) The index map $\mathbf{K}_1(\mathcal{A})\to \mathbf{Z}$ is given by

Index $\widetilde{\rho}(u) = \langle [u],\tau_n\rangle$$\forall u\in \mathbf{GL}(\widetilde{\mathcal{A}})$

e) One has $\mathrm{S}[\tau_n] = [\tau_{n+2}]$ in $\mathrm{H}_{\lambda}^{n+2}(\mathcal{A})$.

Proof. — a) and b) follow from proposition 4.

c) Follows from the proof of proposition 4 b).

d) Follows from the equality

$$
\text { Index } \widetilde {\rho} (u) = \text { Trace } (\mathrm{I} - \widetilde {\rho} (u ^ {- 1}) \widetilde {\rho} (u)) ^ {m} - \text { Trace } (\mathrm{I} - \widetilde {\rho} (u) \widetilde {\rho} (u ^ {- 1})) ^ {m}
$$

(cf. Appendix 1) and the definition of the pairing between $\mathbf{K}_1(\mathcal{A})$ and $\mathbf{H}_{\lambda}^{n}(\mathcal{A})$ (Part II, proposition 15).

e) Follows from the following algebraic lemma, whose proof is left as an exercise to the reader.

Lemma 6. — With the notation of proposition 4 one has

$$
\left(\frac {\mathrm{I}}{2 i \pi} \mathrm{S}\right) (\varphi_ {2 m - 1}) = 4 \left(m + \frac {\mathrm{I}}{2}\right) \varphi_ {2 m + 1}
$$

We shall thus define the Chern character of the given extension as the element of $\mathbf{H}^{\mathrm{odd}}(\mathcal{A}) = \varinjlim (\mathrm{H}_{\lambda}^{2m - 1}(\mathcal{A}),\mathrm{S})$ given by any of the characters $\tau_{n}, n$ odd.

Let us now clarify the relation between $\tau_{n}$ and the fundamental trace form of Helton and Howe ([31]). We assume now that $\mathcal{A}$ is commutative. The fundamental trace form is defined, under the hypothesis of theorem 5, by the equality,

$$
\mathrm{T} (a ^ {0}, \dots , a ^ {n}) = \operatorname{Trace} (\Sigma \varepsilon (\sigma) \rho (a ^ {\sigma (0)}) \dots \rho (a ^ {\sigma (n)}))
$$

where  $\sigma$  runs through the group  $S_{n+1}$  of all permutations of  $\{0, 1, \ldots, n\}$  and  $\varepsilon(\sigma)$  denotes its signature.

Proposition 7. — Let A be a commutative algebra,  $\rho$  and E be as in theorem 5,  $\rho: \mathcal{A} \to \mathcal{L}(\mathrm{E}) / \mathcal{L}^{p/2}(\mathrm{E})$ .

a) For $p = \mathbf{I}$ the fundamental trace form $\mathrm{T}(a^0, a^1)$ is equal to $\frac{\mathrm{I}}{8\pi i} \tau_1(a^0, a^1)$.

b) For $p > 1$, one has

$$
\mathrm{T} (a ^ {0}, \dots , a ^ {n}) = \frac {(- \mathrm{I}) ^ {m} (n + \mathrm{I})}{2 ^ {n + 3} c _ {n}} \Sigma_ {\varepsilon} (\sigma) \tau_ {n} (a ^ {0}, a ^ {\sigma (1)}, \dots , a ^ {\sigma (n)}).
$$

Proof. — a) One has, by definition,

$$
\begin{array}{r l} \tau_ {1} (a ^ {0}, a ^ {1}) = & (\text {Trace} (\rho (a ^ {0} a ^ {1}) - \rho (a ^ {0}) \rho (a ^ {1})) \\ & - \text {Trace} (\rho (a ^ {1} a ^ {0}) - \rho (a ^ {1}) \rho (a ^ {0}))). \end{array}
$$

As $a^1 a^0 = a^0 a^1$ one gets the result.

b) For any $n + 1$ linear functional $\psi$ on $\mathcal{A}$, let $\theta \psi$ be given by

$$
\theta \psi (a ^ {0}, \dots , a ^ {n}) = \sum_ {\pi \in \mathfrak {S} _ {n + 1}} \varepsilon (\pi) \psi (a ^ {\pi (0)}, \dots , a ^ {\pi (n)}).
$$

Since $\tau_{n}$ satisfies $\tau_{n}(a^{1},\ldots ,a^{n},a^{0}) = -\tau_{n}(a^{0},\ldots ,a^{n})$ , one has

$$
\begin{array}{r l} \sum_ {\sigma \in \mathfrak {S} _ {n}} \varepsilon (\sigma) \tau_ {n} (a ^ {0}, a ^ {\sigma (1)}, \dots , a ^ {\sigma (n)}) \\ & = \frac {\mathrm{I}}{n + \mathrm{I}} \sum_ {\pi \in \mathfrak {S} _ {n + 1}} \varepsilon (\pi) \tau_ {n} (a ^ {\pi (0)}, \dots , a ^ {\pi (n)}) = \frac {\mathrm{I}}{n + \mathrm{I}} \theta \tau_ {n}. \end{array}
$$

Let us write $\tau_{n} = \tau_{n}^{+} - \tau_{n}^{-}$, where, with the notation of theorem 5 a),

$$
\tau_ {n} ^ {+} (a ^ {0}, \dots , a ^ {n}) = - 2 ^ {n + 2} c _ {n} \operatorname{Trace} (\varepsilon_ {0} \varepsilon_ {2} \dots \varepsilon_ {n - 1}).
$$

One has $\tau_{n}^{-}(a^{0},\ldots ,a^{n}) = \tau_{n}^{+}(a^{1},\ldots ,a^{0})$ , and hence

$$
\theta \tau_ {n} = \theta \tau_ {n} ^ {+} - \theta \tau_ {n} ^ {-} = 2 \theta \tau_ {n} ^ {+}.
$$

As in the proof of a) one has

$$
\begin{array}{r l} \rho (a ^ {2 k} a ^ {2 k + 1}) - \rho (a ^ {2 k}) \rho (a ^ {2 k + 1}) - (\rho (a ^ {2 k + 1} a ^ {2 k}) - \rho (a ^ {2 k + 1}) \rho (a ^ {2 k})) \\ & = [ \rho (a ^ {2 k + 1}), \rho (a ^ {2 k}) ]. \end{array}
$$

Let $\alpha_{2k}$ be the transposition between $2k$ and $2k + 1$; then

$$
\begin{array}{l} \left(\prod_ {k = 0} ^ {m - 1} \left(\mathrm{I} - \alpha_ {2 k}\right)\right) \tau_ {n} ^ {+} = (- \mathrm{I}) ^ {m} \left(- 2 ^ {n + 2} c _ {n}\right) \\ \times \operatorname{Trace} ([ \rho (a ^ {0}), \rho (a ^ {1}) ] \dots [ \rho (a ^ {n - 1}), \rho (a ^ {n}) ]). \end{array}
$$

Since $\theta (\mathrm{I} - \alpha_{2k}) = 2\theta$ , we get

$$
\theta \tau_ {n} ^ {+} = 2 ^ {- m} \theta \psi ,
$$

where

$$
\begin{array}{r l} \psi (a ^ {0}, \dots , a ^ {n}) & = (- 1) ^ {m} (- 2 ^ {n + 2} c _ {n}) \\ & \times \operatorname{Trace} ([ \rho (a ^ {0}), \rho (a ^ {1}) ] \dots [ \rho (a ^ {n - 1}), \rho (a ^ {n}) ]). \end{array}
$$

The result now follows easily. □

292

## 8. Transversally elliptic operators for foliations

Let (V, F) be a compact manifold with a smooth foliation F, given as an integrable subbundle F of TV. We shall show that any differential or pseudodifferential operator D on V, which is transversally elliptic with respect to F yields a finitely summable Fredholm module over the convolution algebra  $\mathcal{A} = \mathrm{C}_{e}^{\infty}(\mathrm{Graph}(\mathrm{V}, \mathrm{F}))$  ([15], [16]). We deal here with the obvious notion of transversally elliptic operator; a more general notion will be handled in Part VI.

Let $E^{\pm}$ be complex vector bundles on V which are equivariant for the action of Graph(V, F) on V. This means that for any $\gamma \in \text{Graph}(V, F)$, $s(\gamma) = x$, $r(\gamma) = y$, one is given a linear map $\xi \to \gamma\xi$ of $E_x^{\pm}$ to $E_y^{\pm}$ with the obvious smoothness and compatibility conditions.

Definition 1. — Let D be a pseudodifferential operator of order n from  $E^{+}$ to  $E^{-}$ . Then D is transversally elliptic with respect to F if and only if its principal symbol is a) invariant under holonomy, and b) invertible for  $\xi \perp F$ ,  $\xi \neq 0$ .

More explicitly, a) means that for any $\gamma \in \operatorname{Graph}(\mathbf{V}, \mathbf{F})$, $\gamma: x \mapsto y$, one has $\sigma((d\gamma)^t\xi) = \gamma\sigma(\xi)\,\gamma^{-1}$, $\forall\,\xi \in \mathbf{F}_y^\perp$, where $d\gamma$ is the differential of the holonomy, a linear map from $\mathbf{T}_x/\mathbf{F}_x$ to $\mathbf{T}_y/\mathbf{F}_y$. Let $\mathbf{E} = \mathbf{E}^+ \oplus \mathbf{E}^-$, and let us show that each of the usual Sobolev spaces $\mathbf{W}^s(\mathbf{V}, \mathbf{E})$ of sections of $\mathbf{E}$ is a module over $\mathcal{A} = \mathbf{C}_c^\infty(\operatorname{Graph}(\mathbf{V}, \mathbf{F}))$. Let $\mathbf{G} = \operatorname{Graph}(\mathbf{V}, \mathbf{F})$.

Lemma 2. — For any $s \in \mathbf{R}$, the equality

$$
(k * f) (x) = \int_ {\mathbb {G} ^ {x}} k (\gamma) f (y), \quad k \in \mathrm{C} _ {c} ^ {\infty} (\mathrm{G}), f \in \mathrm{W} ^ {s} (\mathrm{V}, \mathrm{E}), y = s (\gamma),
$$

defines a representation of  $\mathbf{C}_{c}^{\infty}(\mathbf{G})$  in  $\mathrm{W}^{s}(\mathrm{V},\mathrm{E})$ .

Before we prove it, we have to explain the notation. Elements of  $\mathbf{C}_{e}^{\infty}(\mathbf{G})$  are not quite functions but sections of the line bundle  $s^{*}(\Omega)$, where  $s: G \to V$  is the source map and  $\Omega$  the line bundle (trivial on V) of 1-densities in the leaf direction. This gives a meaning to the integral  $\int_{\mathbb{G}^{x}} k(\gamma) f(y)$  for scalar functions f. For sections of E one has to replace  $f(y) \in \mathrm{E}_{y}$  by  $\gamma f(y) \in \mathrm{E}_{x}$  and then the integral is performed in  $E_{x}$.

When dealing with Sobolev spaces which are not spaces of functions (i.e. $s < 0$) the statement means that $k *$ extends by continuity to $W^s$.

Proof. — The definition of the Sobolev spaces  $W^{s}(V, E)$  is invariant under diffeomorphism. More precisely given open sets  $V_{1}, V_{2} \subset V$  and functions  $\varphi_{i} \in \mathbf{C}_{c}^{\infty}(V)$  with (support  $\varphi_{i}) \subset V_{i}$ , any partial diffeomorphism  $\Psi : V_{1} \to V_{2}$  covered by a bundle map defines by the formula  $T\xi = \varphi_{1} \Psi^{*}(\varphi_{2} \xi)$  a bounded operator in each of the  $W^{s}$ . Hence (as in [15]) to show that  $k *$  is bounded in  $W^{s}$  one may assume that  $k \in \mathbf{C}_{c}^{\infty}(\mathbf{G}_{\mathrm{W}}) \subset \mathbf{C}_{c}^{\infty}(\mathbf{G})$  where W is a small open set in V (i.e. the foliation F restricted

to W is trivial) and  $G_{w}$  is the graph of the restriction of F to W. Then one can write  $k*$  as an integral of operators of translation along the plaques of W and the statement follows (say by taking the local Sobolev norms to be translation invariant). □

Note that unless  $F_{x} = T_{x}$  for all x, the operators  $k *$  are not smoothing; they are only smoothing in the leaf direction.

Lemma 3. — Let D be a transversally elliptic pseudo-differential operator from  $E^{+}$  to  $E^{-}$  (both bundles are holonomy equivariant and the transverse symbol of D is holonomy invariant). Let Q be any (1) pseudo-differential operator on V from  $E^{-}$  to  $E^{+}$  with order — q (with q = order D) and transverse symbol  $\sigma_{D}^{-1}$ .

$$
L e t \quad \mathrm{H} ^ {+} = \mathrm{W} ^ {s} (\mathrm{V}, \mathrm{E} ^ {+}), \quad \mathrm{H} ^ {-} = \mathrm{W} ^ {s - q} (\mathrm{V}, \mathrm{E} ^ {-}) \quad a n d \quad \mathrm{F} = \left[ \begin{array}{c c} 0 & Q \\ D & 0 \end{array} \right]
$$

$s \in \mathbf{R}$ ) the pair (H, F) is a pre-Fredholm module over $\mathcal{A} = \mathrm{C}_{\mathrm{c}}^{\infty}(\mathrm{G})$. It is $p$-summable for any $p > \operatorname{Codim} \mathrm{F} = \dim \mathrm{V} - \dim \mathrm{F}$.

Proof. — Let us first show that  $k(F^{2}-1)$  and  $(F^{2}-1)k$  belong to  $\mathcal{L}^{p}(W^{s})$  for any s, and  $p>n_{2}=Codim F$ . (We take  $n=dim V$ ,  $n_{1}=dim F$ ,  $n_{2}=Codim F$ ). Both DQ-1 and QD-1 are pseudo-differential operators of order o on V with vanishing transversal symbol, and we shall show that if S is such an operator, then kS and Sk are in  $\mathcal{L}^{p}(W^{s})$  for any  $k\in\mathbf{C}_{c}^{\infty}(\mathbf{G})$ . It is enough, as in the proof of lemma 2, to prove it for  $k\in\mathbf{C}_{c}^{\infty}(\mathbf{G}_{\mathbf{W}})$ , where W is a small open set in V. This shows that the problem is local, and hence we may as well take for (V, F) the torus  $T^{n}=T^{n_{1}}\times T^{n_{2}}(T=R/Z)$  with the foliation whose leaves are the  $T^{n_{1}}\times\{x\}$ ,  $x\in T^{n_{2}}$ . Let  $\sigma$  be the total symbol of S; then S is of the form

$$
(S f) (x) = (2 \pi) ^ {- n} \int e ^ {i \langle s, \xi \rangle} \sigma (x, \xi) f (x - s) \chi (s) d s d \xi ,
$$

where $s$ varies in $\mathbf{R}^n$ (which acts by translations on $\mathbf{T}^n$), $\xi$ in $\mathbf{R}_n = (\mathbf{R}^n)^*$, and $\chi \in \mathbf{C}_c^\infty(\mathbf{R}^n)$ is identically i near o.

One has $\mathbf{G} = \mathbf{T}^{n_1}\times \mathbf{T}^{n_1}\times \mathbf{T}^{n_2}$ and $k\in \mathbf{C}_c^\infty (\mathbf{G})$ acts on functions by

$$
(k f) (x) = \int k \left(x _ {1}, y _ {1}, x _ {2}\right) f \left(y _ {1}, x _ {2}\right) d y _ {1} \quad \text { where } x = \left(x _ {1}, x _ {2}\right) \in \mathrm{T} ^ {n}.
$$

To show that $\mathbf{Sk} \in \mathcal{L}^p(\mathbf{W}^s)$, it is enough to show that, given $s$, the $\mathcal{L}^p$-norm of $(\mathrm{I} + \Delta)^{s/2} \mathbf{Sk}_\alpha(\mathrm{I} + \Delta)^{-s/2}$, $k_\alpha(x) = \exp i2\pi \langle \alpha, x \rangle$, does not grow faster than a polynomial in $\alpha = (\alpha_1, \beta_1, \beta_2) \in \mathbf{Z}^{n_1 + n_1 + n_2}$. Also since any $k_\alpha$ as an operator is the product of a multiplication operator by a $k_{\alpha'}$, $\alpha'$ of the form $(-\beta, \beta, 0)$, it is enough to estimate $||(\mathrm{I} + \Delta)^{s/2} \mathbf{Sk}_{\alpha'}(\mathrm{I} + \Delta)^{-s/2}||_p$, and as $k_{\alpha'}$ commutes with $\Delta$ one is reduced to the case $s = 0$. Finally it is enough to estimate $\sum_{\alpha} ||\mathbf{S}_\alpha k_{\alpha'}||_p$, where $S_\alpha$ has total symbol $\sigma_\alpha$ independent of $x$:

$$
\sigma_ {\alpha} (\xi) = \int e ^ {i 2 \pi \langle \alpha , x \rangle} \sigma (x, \xi) d x, \quad \alpha \in \mathbf {Z} ^ {n}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$p:\mathbf{T}^{*}\rightarrow \mathbf{F}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\sigma (\xi) = (\mathrm{I} - \chi)\sigma_{\mathbf{D}}^{-1}(p(\xi))$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\chi \in \mathbf{C}_{c}^{\infty}(\mathbf{F})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) For instance take $\mathbf{Q}$ with symbol $\sigma(\xi) = (\mathrm{i} - \chi)\sigma_{\mathrm{D}}^{-1}(p(\xi))$, where $\chi \in \mathrm{C}_{e}^{\infty}(\mathbf{F})$ is equal to $\mathrm{i}$ on $\mathbf{V} \subset \mathbf{F}^{\perp}$ and $p: \mathbf{T}^{\bullet} \to \mathbf{F}$ is a linear projection.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{V}\subset \mathbf{F}^{\perp}$</span></small>

Now both  $S_{\alpha}$  and  $k_{\alpha'}$  are diagonal in the basis  $e_{\alpha''}, (e_{\alpha''}(x) = \exp i2\pi\langle\alpha'', x\rangle, \alpha'' \in \mathbf{Z}^n)$ . The operator  $S_{\alpha}$  multiplies  $e_{\alpha''}$  by  $(\sigma_{\alpha} * \widehat{\chi})(2\pi\alpha'')$ , where  $\widehat{\chi}$  is the Fourier transform of  $\chi$ ), and  $k_{\alpha'} (\alpha' = (-\beta, \beta, 0))$  multiplies  $e_{\alpha''}$  by o if  $\alpha_{1}'' \neq \beta$  and by r if  $\alpha_{1}'' = \beta$ . Thus

$$
\left(\left| \left| S _ {\alpha} k _ {\alpha^ {\prime}} \right| \right| _ {p}\right) ^ {p} = \sum_ {\alpha_ {2} ^ {\prime \prime}} \left| \left(\sigma_ {\alpha} * \widehat {\chi}\right) \left(2 \pi \left(\beta , \alpha_ {2} ^ {\prime \prime}\right)\right) \right| ^ {p}.
$$

This is finite for $p > n_2$, since by hypothesis one has for $\sigma$ (and hence $\sigma_{\alpha} * \hat{\chi}$) an inequality $|\sigma(x, \xi_1, \xi_2)| \leq C(I + ||\xi_1||)(I + ||\xi_1|| + ||\xi_2||)^{-1}$.

Since the same inequality holds for the partial derivatives with respect to $x$, one gets that the $C_{\alpha}$'s (for the $\sigma$'s) are of rapid decay in $\alpha$, thus the conclusion follows.

Let us check that $[\mathbf{F}, k] \in \mathcal{L}^p$, $p > n_2$, for any $k \in \mathbf{C}_c^\infty(\mathbf{G})$. If $\mathbf{P}: W^s \to W^{s-k}$ is a pseudo-differential operator of order $k$ and its principal symbol vanishes on $\mathbf{F}^\perp$, we have $k\mathbf{P}$ and $\mathbf{P}k$ in $\mathcal{L}^p(W^s, W^{s-k})$ for any $p > n_2$. This shows that to prove that if the principal symbol of $\mathbf{P}$ is holonomy invariant one has $[\mathbf{P}, k] \in \mathcal{L}^p$, one can assume that $k \in \mathbf{C}_c^\infty(G_W)$, $W$ a small open set. One is then back to the above case where $V = T^{n_1} \times T^{n_2}$. Applying again the above result one can now assume that $\mathbf{P}$ is exactly invariant under the action of the compact group $T^{n_1}$.

Now the action of $k \in \mathbf{C}_e^\infty(\mathbf{G})$ in $W^s$ is of the form

$$
k f = \int_ {\mathrm{T} ^ {n _ {1}}} k _ {t} \mathrm{U} _ {t} (f) d t,
$$

where  $U_{t}$  is the translation by  $t \in T^{n_{1}}$  and  $k_{t}$  is the multiplication by a smooth function of  $x \in V$  (and  $t \in T^{n_{1}}$ ). Thus  $[P, k] = \int [P, k_{t}] U_{t} dt = \int P_{t} U_{t} dt$  where  $P_{t}$  is pseudodifferential with order -1. Using Fourier expansion one checks that any  $k \in \mathbf{C}_{c}^{\infty}(\mathbf{G})$  is of the form  $k = k_{1} * k_{2}$ , thus  $[P, k] = [P, k_{1}] k_{2} + k_{1}[P, k_{2}]$  and both terms are in  $L^{p}$  by the above result. □

Remark 4. — In the special case when the foliation (V, F) comes from a locally free action of a Lie group H (not necessarily compact), the graph of (V, F) is equal to V × H. The convolution algebra  $\mathbf{C}_{c}^{\infty}(\mathbf{H})$  becomes a subalgebra of  $\mathbf{C}_{c}^{\infty}(\mathbf{G})$  (by composing  $f \in \mathbf{C}_{c}^{\infty}(\mathbf{H})$  with the proper projection V × H → H). Thus given a transversally elliptic operator D for (V, F) one can restrict its n-dimensional character ( $n \geq \dim V - \dim F$ ) to  $\mathbf{C}_{c}^{\infty}(\mathbf{H})$ . If both D and a parametrix Q are exactly H-invariant, then one can compute this restriction  $\tau_{n}^{H}$  from the distribution character  $\chi$  of D. The easy computation gives  $\tau_{n}^{H} - S^{m}\chi = (n = 2m)$ .

$$
\tau_ {n} ^ {\mathrm{H}} = \mathrm{S} ^ {m} \chi , (n = 2 m).
$$

The central distribution $\chi$ is defined as in [2] by the equality

$$
\chi (f) = \operatorname{Trace} (\text { action   of } f \text { in   } \operatorname{Ker} D) - \operatorname{Trace} (\text { action   of } f \text { in   } \operatorname{Ker} D ^ {t})
$$

(cf. [2], Remark, p. 17).

In the simplest examples with H non compact, the distribution character  $\chi$  of D is not invariant under homotopy. However, by the above results, its class in  $\mathrm{H}^{*}(\mathrm{C}_{e}^{\infty}(\mathrm{H}))$  is stable.

## 9. Fredholm modules over the convolution algebra of a Lie group

Given a Lie group G, we let  $\mathcal{A} = \mathrm{C}_{c}^{\infty}(\mathrm{G})$  be the convolution algebra of smooth functions with compact support.

The Miščenko extension ([50]) gives a natural construction of Fredholm modules over $\mathcal{A} = \mathbf{C}_{e}^{\infty}(\mathbf{G})$ parametrized by a representation $\pi$ of the maximal compact subgroup $\mathbf{K}$ of $\mathbf{G}$.

In this section we shall show in the two examples  $G = R^{2}$  and  $G = \text{SL}(2, \mathbf{R})$  that the corresponding modules are p-summable and go a good way in the computation of their Chern characters. For  $\text{SL}(2, \mathbf{R})$  we shall find a precise link with the surface of triangles in hyperbolic geometry which is a standard 2-cocycle in the group cohomology with coefficients in C. This link appears very natural if one has the example of  $G = R^{2}$  in mind. The method that we use goes over to semi-simple real Lie groups of real rank one. For such groups, in the corresponding symmetric spaces G/K the angle under which one sees a given compact set  $B \subset G/K$  from a distance d tends to o as  $e^{-cd}$  when  $d \to \infty$ . Thus the p-summability follows as in lemma 1 below using Russo's theorem ([63], p. 57). For groups of higher rank the problem of constructing natural p-summable Fredholm modules is open.

The case $\mathbf{G} = \mathbf{R}^2$

Let $G = R^2$. We define a Fredholm module over the convolution algebra $\mathcal{A} = C_e^\infty(G)$ as follows: $H^+ = L^2(R^2)$, $H^- = L^2(R^2)$ (with the action of $\mathcal{A}$ by left translation), and $F = \begin{bmatrix} o & D^{-1} \\ D & o \end{bmatrix}$ where the operator $D: H^+ \to H^-$ is the multiplication by the complex valued function

$$
\varphi (z) = z / | z | \quad \forall z \in \mathbf {R} ^ {2} = \mathbf {C}, z \neq 0.
$$

The function $\varphi$ is not defined at $z = 0$ but this is unimportant since only its class in $\mathbf{L}^{\infty}(\mathbb{R}^{2})$ matters to define D.

Lemma 1. — The pair $(\mathbf{H}^{\pm}, \mathbf{F})$ is a Fredholm module over $\mathcal{A} = \mathbf{C}_c^\infty(\mathbf{R}^2)$. It is $p$-summable for any $p > 2$.

Proof. — One has  $F^{2} = \imath$  by construction. For  $f \in \mathbf{C}_{c}^{\infty}(\mathbf{R}^{2})$  and  $\xi \in H^{+}$ , one has

$$
\begin{array}{r l} ([ \mathrm{D}, f ] \xi) (s) & = \varphi (s) \int f (t) \xi (s - t) d t - \int f (t) \varphi (s - t) \xi (s - t) d t \\ & = \int f (s - s ^ {\prime}) (\varphi (s) - \varphi (s ^ {\prime})) \xi (s ^ {\prime}) d s ^ {\prime}. \end{array}
$$

Thus it is the integral operator with kernel $k(s, s') = f(s - s') (\varphi(s) - \varphi(s'))$. Since $f$ has compact support one has $k(s, s') = 0$ if $d(s, s') > \mathbf{C}$ for some $\mathbf{C} < \infty$, where $d$ is the Euclidean distance. Also for $|s|$ large and $d(s, s') \leq \mathbf{C}$, the term $\varphi(s) - \varphi(s')$

297

is of the order of $\mathbf{1} / |s|$. This shows that for any $p > 2$, with $q = \frac{p}{p - \mathbf{1}}$, one has $\int \left( \int |k(s, s')|^q ds \right)^{p/q} ds' < \infty$ (and similarly for the kernel $k^* = \bar{k}(s', s)$). So Russo's theorem ([63], p. 57) gives the conclusion.

We shall now compute the character  $\tau_{2}$  of (H, F). By a straightforward computation, as in section 1, one gets

$$
\tau_ {2} \left(f ^ {0}, f ^ {1}, f ^ {2}\right) = 2 i \pi \int_ {s ^ {0} + s ^ {1} + s ^ {2} = 0} f ^ {0} \left(s ^ {0}\right) f ^ {1} \left(s ^ {1}\right) f ^ {2} \left(s ^ {2}\right) c \left(s ^ {0}, s ^ {1}, s ^ {2}\right) d s ^ {1} d s ^ {2}
$$

where the function $c(s^0, s^1, s^2)$, $s^i \in \mathbf{R}^2$ is given by

$$
c (s ^ {0}, s ^ {1}, s ^ {2}) = \int \beta (s ^ {0}, s) \beta (s ^ {1}, s - s ^ {0}) \beta (s ^ {2}, s - s ^ {0} - s ^ {1}) d s
$$

with $\beta(s^0, s) = \mathrm{I} - \varphi(s)^{-1} \varphi(s - s^0)$. To get this, one just has to write the trace of an integral operator as the integral $\int k(s, s) ds$.

We shall compute $c(s^0, s^1, s^2)$; we try to prove the next lemma in such a way that the proof goes over to the case of hyperbolic geometry.

Lemma 2. — One has $c(s^0, s^1, s^2) = 2i\pi(s^1 \wedge s^2)$.

Proof. — Let us first simplify the integrand $\beta(s^{0}, s) \beta(s^{1}, s - s^{0}) \beta(s^{2}, s - s^{0} - s^{1})$. For that we consider the Euclidean triangle with vertices $o, s^{0}, s^{0} + s^{1}$ (remember that $s^{0} + s^{1} + s^{2} = o$). Then $\varphi(s)^{-1} \varphi(s - s^{0}) = e^{i\alpha}$ where $\alpha = \nless (o, s, s^{0})$ is the angle (between $-\pi$ and $\pi$) obtained by looking at the edge $(o, s^{0})$ from $s$. Thus $\beta(s^{0}, s) = i - e^{i\alpha}$. Similarly $\beta(s^{1}, s - s^{0}) = i - e^{i\beta}$ where $\beta = \nless (o, s - s^{0}, s^{1}) = \nless (s^{0}, s, s^{0} + s^{1})$ and $\beta(s^{2}, s - s^{0} - s^{1}) = i - e^{i\gamma}$ where $\gamma = \nless (o, s - s^{0} - s^{1}, -s^{0} - s^{1}) = \nless (s^{0} + s^{1}, s; o)$. Since $\alpha + \beta + \gamma = o$ we get

$$
\begin{array}{r l} \left(\mathrm{I} - e ^ {i \alpha}\right) \left(\mathrm{I} - e ^ {i \beta}\right) \left(\mathrm{I} - e ^ {i \gamma}\right) & = - e ^ {i \alpha} - e ^ {i \beta} - e ^ {i \gamma} + e ^ {- i \alpha} + e ^ {- i \beta} + e ^ {- i \gamma} \\ & = - 2 i (\sin \alpha + \sin \beta + \sin \gamma). \end{array}
$$

Define

Then

$$
\begin{array}{l} \mathrm{S(A,B,C)} = \int (\sin \nless \mathrm{AsB} + \sin \nless \mathrm{BsC} + \sin \nless \mathrm{CsA}) d s. \\ c (s ^ {0}, s ^ {1}, s ^ {2}) = - 2 i \mathrm{S(A,B,C)}, \end{array}
$$

where A = 0,  $B = s^{0}$ ,  $C = s^{0} + s^{1}$  form the triangle A, B, C. The integrand is  $o(|s|^{-3})$  for large s so that the integral is well defined.

To prove that  $S(A, B, C)$  is proportional to the Euclidean area of the triangle  $(A, B, C)$ , the main point is to show that S is additive for triangles  $T_{1}$ ,  $T_{2}$  such that  $T_{1} \cup T_{2}$  is again a triangle. Let us prove this. Let  $\sigma$  be the symmetry around the straight line which contains three vertices, say  $B_{1}$ ,  $C_{1} = B_{2}$  and  $C_{2}$  and let  $A_{1} = A_{2}$  be the only vertex outside this line. Writing the integral defining S as a limit of integrals

over $\sigma$-invariant subsets eliminates the terms of the form $\sin \nless B_1 sC_1$, $\sin \nless B_2 sC_2$ and $\sin \nless B_1 sC_2$. Moreover one has $\sin \nless C_1 sA_1 = -\sin \nless A_2 sB_2$. The equality $S(T_1 \cup T_2) = S(T_1) + S(T_2)$ is now clear.

![](images/page_42_image_1.jpg)

The next point is that  $S(A, B, C) \geq o$  if the triangle ABC is positively oriented (i.e. if the orientation ABC fits with the natural orientation of  $R^{2} = C$ ). To see that, consider the disk  $D_{R}$  with center A and radius R. Then  $D_{R}$  is invariant under the symmetries around both sides AC and AB so that the integral expressing S reduces to  $\int \sin \nLeftrightarrow BsC$ . Let  $\sigma$  be the symmetry around BC, then the complement of the line BC in  $D_{R}$  has (for R large) two components  $D'$  and  $D''$  such that  $\sigma(D') \subset D''$ . As on  $D'' \setminus \sigma(D')$  one has  $\sin \nLeftrightarrow BsC \geq o$ , one gets the answer.

![](images/page_42_image_3.jpg)

Now we can define the functional S on all subsets C of  $R^{2}$  which are finite unions of closed triangles. The collection C of such subsets is a compact class in the sense of probability theory and thus we see that S defines a translation invariant Radon measure on  $R^{2}$ . Thus S is proportional to the area, and the constant of proportionality is easy to check.

Corollary 3. — The 2-dimensional character $\tau_{2}$ of (H, F) is

$$
\tau_ {2} (f ^ {0}, f ^ {1}, f ^ {2}) = \int \hat {f} ^ {0} d \hat {f} ^ {1} \wedge d \hat {f} ^ {2}
$$

where $f^0, f^1, f^2 \in \mathbf{C}_c^\infty(\mathbf{R}^2)$ have Fourier transforms $\hat{f}^i$.

The case $\mathbf{G} = \mathbf{SL}(2,\mathbf{R})$

Let $\mathbf{G} = \mathrm{SL}(2, \mathbf{R})$. In fact we shall use the realization of $\mathbf{G}$ as $\mathrm{SU}(1, 1)$ i.e. 2 by 2 complex matrices $g = \begin{bmatrix} \alpha & \overline{\beta} \\ \beta & \overline{\alpha} \end{bmatrix}$, $|\alpha|^2 - |\beta|^2 = 1$. As maximal compact subgroup $\mathbf{K}$, we choose $\mathbf{K} = \begin{cases} \begin{bmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{bmatrix}, & \theta \in \mathbb{R}/2\pi\mathbb{Z} \end{cases}$, and we identify $\mathbf{G}/\mathbf{K}$ with the unit disk $U$ in the complex plane $\mathbf{C}$, on which $G$ acts by $gz = \frac{\alpha z + \overline{\beta}}{\beta z + \overline{\alpha}}$ for $z \in U$, $g \in G$. To the character $\chi_n$ of $K$ given by $\chi_n\left(\begin{bmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{bmatrix}\right) = e^{in\theta}$ corresponds an induced line bundle $E_n$ on $U$ whose sections correspond canonically to functions $\xi$ on $G$ such that $\xi(gk) = \chi_n(k)^{-1} \xi(g)$ for $k \in K$, $g \in G$. The tangent bundle of $U$ considered as a complex curve corresponds to $\chi_2$ where $\chi_2(k) = e^{i2\theta}$ which is the isotropy representation of $K$. At each point $p \in U$, $p \neq 0$, there is a unit tangent vector $\varphi(p) \in T_p(U)$, i.e. the one-dimensional complex tangent space $T = E_2$, such that $o$ belongs to the half-line starting at $p$ in the direction of $\varphi(p)$. (We use the unique G-invariant metric of curvature — 1: $2(1 - |z|^2)^{-1}|dz|$ as a Riemannian metric on $U$.)

![](images/page_43_image_6.jpg)

Being a section of $\mathbf{E}_2$ (on $\mathbf{U} / \{\mathbf{o}\}$), $\varphi$ can be considered as a function on $\mathbf{G}$; given $g \in \mathbf{G}$, $g = \begin{bmatrix} \alpha & \overline{\beta} \\ \beta & \overline{\alpha} \end{bmatrix}$, $g \notin \mathbf{K}$ one gets

$$
\varphi (g) = \frac {\overline {{{{\beta}}}} \overline {{{{\alpha}}}}}{| \beta \alpha |}
$$

It has a simple interpretation in terms of the $\mathbf{K}\mathbf{A}^{+}\mathbf{K}$ decomposition. One has $\varphi (kak^{\prime}) = \chi_{-2}(k^{\prime})$, where $\mathbf{A} = \left\{\left[ \begin{array}{ll}\operatorname {ch}t & \operatorname {sh}t\\ \operatorname {sh}t & \operatorname {ch}t \end{array} \right],t\in \mathbf{R}\right\}$, and $k,k^{\prime}\in \mathbf{K},a\in \mathbf{A}^{+}$.

For each $n \in \mathbf{Z}$ we let $\mathbf{D}_n$ be the operator of multiplication by $\varphi$ from $\mathbf{L}^2(\mathbf{U}, \mathbf{E}_n)$ to $\mathbf{L}^2(\mathbf{U}, \mathbf{E}_{n+2})$ (1).

Lemma 4. — a) For each $n \in \mathbf{Z}$, the pair $(\mathrm{H}_n, \mathrm{F}_n)$ is a Fredholm module over $\mathcal{A} = \mathrm{C}_c^\infty(\mathrm{G})$, where $\mathrm{H}_n^+ = \mathrm{L}^2(\mathrm{U}, \mathrm{E}_n)$, $\mathrm{H}_n^- = \mathrm{L}^2(\mathrm{U}, \mathrm{E}_{n+2})$,

$$
\mathbf {F} _ {n} = \left[ \begin{array}{c c} \mathrm{o} & \mathrm{D} _ {n} ^ {*} \\ \mathrm{D} _ {n} & \mathrm{o} \end{array} \right].
$$

b) The direct sum $(\oplus \mathbf{H}_n, \oplus \mathbf{F}_n)$ is also a Fredholm module and is $p$-summable for any $p > 1$, as well as all $(\mathbf{H}_n, \mathbf{F}_n)$.

Proof. — The algebra $\mathcal{A}$ acts by left convolution in $\mathbf{H}_n$. One has by construction $\mathbf{F}_n^2 = \mathbf{i}$, $\mathbf{F}^2 = \mathbf{i}$ (where $\mathbf{F} = \oplus \mathbf{F}_n$). It is clearly enough to prove b). Now $\mathbf{H}^+ = \oplus \mathbf{H}_n^+ = \mathbf{L}^2 (\mathbf{G})$ where $\mathcal{A}$ acts by the left regular representation; also $\mathbf{H}^- = \mathbf{L}^2 (\mathbf{G})$, and the operator $\mathbf{D} = \oplus \mathbf{D}_n$ is given simply by the multiplication by the function $\varphi(g)$. As in the case of $\mathbf{R}^2$ we get

where

$$
\begin{array}{r l} & ([ \mathrm{D}, f ] \xi) (g) = \varphi (g) \int f (g g ^ {\prime - 1}) \xi (g ^ {\prime}) d g ^ {\prime} - \int f (g g ^ {\prime - 1}) \varphi (g ^ {\prime}) \xi (g ^ {\prime}) d g ^ {\prime} \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad = \int k (g, g ^ {\prime}) \xi (g ^ {\prime}) d g ^ {\prime} \\ & k (g, g ^ {\prime}) = (\varphi (g) - \varphi (g ^ {\prime})) f (g g ^ {\prime - 1}). \end{array}
$$

We want to show that  $(\mathbf{H}, \mathbf{F})$  is 2-summable, i.e. that

$$
\int \left| k (g, g ^ {\prime}) \right| ^ {2} d g d g ^ {\prime} <   \infty .
$$

Since $f$ has compact support, it is enough to show (with $d$ a left invariant metric on $G$) that

$$
\begin{array}{l} \int | \varphi (g ^ {- 1}) - \varphi (g ^ {\prime - 1}) | ^ {2} d g <   \infty \\ d (g, g ^ {\prime}) \leq \mathbf {C} <   \infty \end{array}
$$

where

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{G} = \mathbf{SL}(2,\mathbf{R})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{U} = \mathbf{G} / \mathbf{K}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) In this special case  $\mathbf{G} = \mathbf{SL}(2, \mathbf{R})$  we rely on the natural conformal structure of U = G/K, but the true nature of the construction is to take the Clifford multiplication by  $\varphi$  (cf. [50]) for which one just needs an invariant spin $^{e}$  structure on G/K.</span></small>

(more precisely $\int \mathbf{M}(g)^2 dg < \infty$ where $\mathbf{M}(g) = \sup \{|\varphi(g^{-1}) - \varphi(g'^{-1})|, d(g, g') \leq \mathbf{C}\}$). But by construction, if we let $p = g\mathbf{K}$, $p' = g'\mathbf{K} \in \mathbf{U}$, then $|\varphi(g^{-1}) - \varphi(g'^{-1})|$ is of the order of the angle $\nless p\mathbf{Op}'$. The basic formula in hyperbolic geometry

## ch $c = \operatorname{ch} a \operatorname{ch} b - \operatorname{sh} a \operatorname{sh} b \cos \angle C$

implies that $|\varphi(g)^{-1} - \varphi(g'^{-1})|$ is of the order of $\exp(-d(o, p))$. Since the area of the disk of center o and radius $d = d(o, p)$ is of the order of $\exp d$, one easily gets $\int M(g)^2 dg < \infty$.

As in the case of  $R^{2}$  we shall now compute the 2-dimensional character  $\tau_{2}$  of (H, F). (The computation of  $\tau_{2}^{n}$  (for  $(\mathrm{H}_{n}, \mathrm{F}_{n})$ ) and its relation with characters of discrete series is postponed until part VII.) Note that obviously  $\tau_{2} = \Sigma\tau_{2}^{n}$ . By a straightforward computation we get

$$
\tau_ {2} (f ^ {0}, f ^ {1}, f ^ {2}) = 2 i \pi \int_ {g ^ {0} g ^ {1} g ^ {2} = 1} f ^ {0} (g ^ {0}) f ^ {1} (g ^ {1}) f ^ {2} (g ^ {2}) c (g ^ {0}, g ^ {1}, g ^ {2}) d g ^ {1} d g ^ {2}
$$

where the function $c(g^{0}, g^{1}, g^{2})$, $g^{i} \in \mathbf{G}$, $g^{0}g^{1}g^{2} = \mathrm{i}$, is given by

$$
c \left(g ^ {0}, g ^ {1}, g ^ {2}\right) = \int \beta \left(g ^ {0}, g\right) \beta \left(g ^ {1}, \left(g ^ {0}\right) ^ {- 1} g\right) \beta \left(g ^ {2}, \left(g ^ {0} g ^ {1}\right) ^ {- 1} g\right) d g
$$

with $\beta(g^0, g) = \mathrm{I} - \varphi(g)^{-1} \varphi((g^0)^{-1} g)$.

We now relate  $c(g^{0}, g^{1}, g^{2})$  to the 2-cocycle  $A(g^{1}, g^{2})$  which is given by the (oriented) area of the hyperbolic triangle (in the Poincaré disk U) with vertices o,  $(g^{1})^{-1}(o)$ ,  $g^{2}(o)$ . Note the relations

$$
\mathrm{A} (k g ^ {1}, g ^ {2}) = \mathrm{A} (g ^ {1} k, k g ^ {2}) = \mathrm{A} (g ^ {1}, g ^ {2} k) = \mathrm{A} (g ^ {1}, g ^ {2}) \quad \forall k \in \mathbf {K}
$$

and

$$
\mathrm{A} (g ^ {0}, g ^ {1}) = \mathrm{A} (g ^ {1}, g ^ {2}) = \mathrm{A} (g ^ {2}, g ^ {0}) \quad \text { for } g ^ {0} g ^ {1} g ^ {2} = \mathrm{I}.
$$

$$
\text { Lemma   5. } - \text { One   has } c (g ^ {0}, g ^ {1}, g ^ {2}) = 4 i \pi A (g ^ {1}, g ^ {2}) \quad (\text { where } g ^ {0} g ^ {1} g ^ {2} = 1).
$$

Proof. — Let A = 0, B = $g^0(o)$, C = $g^0g^1(o)$, and let us consider the hyperbolic triangle T = (A, B, C) in the Poincaré disk U. For $g \in \mathrm{SL}(2, \mathbf{R})$ let $p = g(o) \in U$. The value of $\varphi(g)^{-1}\varphi((g^0)^{-1}g)$ only depends on the three points A, $p$, B. Since $\varphi((g^0)^{-1}g)$, considered as a function of $g$, is the section of the tangent bundle T(U) which to $p \in U$ assigns the unit tangent vector at $p$ looking at $g^0(o) = B$, we get $\varphi(g)^{-1}\varphi((g^0)^{-1}g) = \exp i \nless ApB$. Thus $\beta(g^0,g) = 1 - \exp i \nless ApB$. Also

$$
\beta (g ^ {1}, (g ^ {0}) ^ {- 1} g) = \mathrm{i} - \exp i \beta ,
$$

where

$$
\beta = \nless (0, (g ^ {0}) ^ {- 1} g (0), g ^ {1} (0)) = \nless (g ^ {0} (0), g (0), g ^ {0} g ^ {1} (0)) = \nless B p C,
$$

and similarly one has

$$
\beta (g ^ {2}, (g ^ {0} g ^ {1}) ^ {- 1} g) = \mathrm{I} - \exp i \gamma , \quad \gamma = \nless C p A.
$$

As in the Euclidean case one has $\alpha + \beta + \gamma = 0$ so that the same computation as in lemma 9.2 gives $c(g^0, g^1, g^2) = -2i\mathrm{S}(\mathbf{A}, \mathbf{B}, \mathbf{C})$, where

$$
\mathrm{S} (\mathrm{A}, \mathrm{B}, \mathrm{C}) = \int_ {\mathrm{U}} (\sin \nless \mathrm{ApB} + \sin \nless \mathrm{BpC} + \sin \nless \mathrm{CpA}) d p.
$$

Now the proof of lemma 9.2 is written in such a way that it goes over without changes to the hyperbolic case. For instance it is still true that the disk  $D_{R}$  with center A is invariant under the symmetries around AC and AB while the complement of the line BC in  $D_{R}$  has two components  $D'$,  $D''$  with  $\sigma_{\mathrm{BC}}(\mathbf{D}') \subset \mathbf{D}'$. Thus as in lemma 9.2 one gets a G-invariant Radon measure on U so that S is proportional to the hyperbolic area.

## Appendix 1: Schatten classes

In this appendix we have gathered for the convenience of the reader the properties of the Schatten classes $\mathcal{L}^p$ needed in the text. Let H be a separable Hilbert space, $\mathcal{L}(\mathrm{H})$ the algebra of bounded operators in H and $\mathcal{L}^{\infty}(\mathrm{H})$ the ideal of compact operators. For $\mathrm{T}\in \mathcal{L}^{\infty}(\mathrm{H})$ we let $\mu_n(\mathrm{T})$ be the $n$-th singular value of T, i.e. the $n$-th eigenvalue of $|\mathrm{T}| = (\mathrm{T}^{*}\mathrm{T})^{1 / 2}$ (cf. [63]). By definition, the Schatten class $\mathcal{L}^p (\mathrm{H})$ is, for $p\in [\mathrm{i},\infty [$,

$$
\mathcal {L} ^ {p} (\mathrm{H}) = \{\mathrm{T} \in \mathcal {L} (\mathrm{H}), \Sigma \mu_ {n} (\mathrm{T}) ^ {p} <   \infty \}.
$$

Proposition 1. — a) $\mathcal{L}^{p}(\mathrm{H})$ is a two sided ideal in $\mathcal{L}(\mathrm{H})$.

b) $\mathcal{L}^p (\mathbf{H})$ is a Banach space for the norm

$$
\left| \left| \mathrm{T} \right| \right| _ {p} = (\Sigma \mu_ {n} (\mathrm{T}) ^ {p}) ^ {1 / p}.
$$

c) $\mathcal{L}^p (\mathbf{H})\subset \mathcal{L}^q (\mathbf{H})$ for $p\leq q$

d) Let $p, q, r \in [\mathrm{I}, \infty]$ with $\frac{\mathrm{I}}{r} = \frac{\mathrm{I}}{p} + \frac{\mathrm{I}}{q}$. For any $\mathrm{S} \in \mathcal{L}^p(\mathrm{H})$, $\mathrm{T} \in \mathcal{L}^q(\mathrm{H})$, one has $\mathrm{ST} \in \mathcal{L}^r(\mathrm{H})$ and $||\mathrm{ST}\|_r \leq ||\mathrm{S}\|_p ||\mathrm{T}\|_q$.

Proof. — See [63].

One could equivalently define $\mathcal{L}^{p}(\mathrm{H})$ starting from the trace on $\mathcal{L}(\mathrm{H})$, which we consider as a weight, i.e. a map: $\mathcal{L}(\mathrm{H})^{+}\to [0,\infty]$ defined by

$$
\operatorname{Trace} (\mathrm{T}) = \Sigma \left\langle \mathrm{T} \xi_ {n}, \xi_ {n} \right\rangle
$$

for any orthonormal basis $(\xi_{n})$ of H and any $\mathbf{T} \in \mathcal{L}(\mathbf{H})^{+}$. (See [51] theorem 2.14.)

Proposition 2. — a) $\mathcal{L}^{p}(\mathrm{H}) = \{\mathrm{T}\in \mathcal{L}(\mathrm{H}),\operatorname {Trace}|T|^{p} <   \infty \}$

b) For $\mathbf{T} \in \mathcal{L}^p(\mathbf{H})$ one has $||\mathbf{T}||_p = (\text{Trace} |\mathbf{T}|^p)^{1/p}$.

c) $\operatorname{Trace}(\mathbf{A}^*\mathbf{A}) = \operatorname{Trace}(\mathbf{AA}^*)$ for all $\mathbf{A} \in \mathcal{L}(\mathbf{H})$.

d) The trace extends by linearity to a linear functional on $\mathcal{L}^1 (\mathbf{H})$ and

$$
\operatorname{Trace} (\mathrm{T}) = \Sigma \left\langle \mathrm{T} \xi_ {n}, \xi_ {n} \right\rangle \quad f o r \mathrm{T} \in \mathscr {L} ^ {1} (\mathrm{H})
$$

and any orthonormal basis $(\xi_{n})$ of H.

e) $|\operatorname{Trace}(\mathbf{T})| \leq ||\mathbf{T}||_1$ for $\mathbf{T} \in \mathcal{L}^1(\mathbf{H})$.

302

Proof. — See [51] and [63].

The next theorem, due to Lidskii, expresses Trace T from the eigenvalues of T. Since $\mathcal{L}^1\subset \mathcal{L}^\infty$ the eigenvalues of $T\in \mathcal{L}^1$ form a sequence $(\lambda_n)$, with $\lambda_{n}\to 0$ when $n\to \infty$ (see [63]).

Theorem 3. — Let $\mathrm{T} \in \mathcal{L}^1(\mathrm{H})$, then $\Sigma |\lambda_n(\mathrm{T})| < \infty$ and Trace $\mathrm{T} = \Sigma \lambda_n(\mathrm{T})$.

Corollary 4. — Let A, B ∈ L(H) be such that AB and BA belong to L¹(H). Then Trace(AB) = Trace(BA) (cf. [63], p. 50).

We shall now prove two results needed in part I. They are an easy modification of lemma 3.2, p. 158 in [30].

Proposition 5. — Let $p \in [\mathrm{I}, \infty[, \mathrm{S}, \mathrm{T} \in \mathcal{L}(\mathrm{H})$ and assume that $[\mathrm{S}, \mathrm{T}] \in \mathcal{L}^p(\mathrm{H})$. Then:

α) if f is an analytic function in a neighborhood of the spectrum of S, one has  $[f(S), T] \in \mathcal{L}^{p}(H)$ ;

$\beta)$ if $\mathbf{S}$ is selfadjoint and if $f$ is a $\mathbf{C}^{\infty}$ function on the spectrum of $\mathbf{S}$, one has $[f(\mathbf{S}), \mathbf{T}] \in \mathcal{L}^{p}(\mathbf{H})$.

Proof. —  $\alpha$ ) Let  $\gamma$  be a simple closed curve containing the spectrum of S, with f analytic on  $\gamma$ . Then,

$$
f (\mathrm{S}) = (1 / 2 i \pi) \int_ {\gamma} f (\lambda) (\lambda - \mathrm{S}) ^ {- 1} d \lambda
$$

and hence, $[f(\mathbf{S}),\mathbf{T}] = (\mathrm{I} / 2i\pi)\int_{\gamma}f(\lambda)[(\lambda -\mathbf{S})^{-1},\mathbf{T}]d\lambda .$

Now $[(\lambda - S)^{-1}, T] = (\lambda - S)^{-1}[S, T](\lambda - S)^{-1}$, which implies that the map $\lambda \mapsto f(\lambda)[(\lambda - S)^{-1}, T]$ is a continuous function from $\gamma$ to $\mathcal{L}^p(H)$. Thus the integral converges in $\mathcal{L}^p(H)$ and $[f(S), T] \in \mathcal{L}^p(H)$.

$\beta)$ Let us show that $||[e^{itS}, T] ||_p$ is $\mathrm{O}(|t|)$ when $t \to \infty$. For any $\mathbf{U} \in \mathcal{L}(\mathbf{H})$, with $[\mathbf{U}, \mathbf{T}] \in \mathcal{L}^p$ one has,

$$
\left| \left| [ \mathrm{U} ^ {n}, \mathrm{T} ] \right| \right| _ {p} \leq n \left| \left| [ \mathrm{U}, \mathrm{T} ] \right| \right| _ {p} \left| \left| \mathrm{U} \right| \right| ^ {n - 1} \quad \forall n \in \mathbf {N}.
$$

This shows that $||[e^{it\mathbb{S}}, \mathbf{T}]||_p$ is bounded on any bounded interval. Since, with $\mathbf{U} = e^{it\mathbb{S}}$, one gets,

$$
\left| \left| \left[ e ^ {i n t \mathrm{S}}, \mathrm{T} \right] \right| \right| _ {p} \leq n \left| \left| \left[ e ^ {i t \mathrm{S}}, \mathrm{T} \right] \right| \right| _ {p} \quad \forall n \in \mathbf {N},
$$

it follows that $||[e^{it\mathbb{S}}, \mathbf{T}]||_p \leq \mathbf{C}(\mathfrak{I} + |t|)$ for all $t$. Then take $f$ to be compactly supported, so that $f = \hat{g}$ with $(\mathfrak{I} + |t|) g \in \mathbf{L}^1(\mathbf{R})$. This yields,

$$
\left| \left| [ f (\mathrm{S}), \mathrm{T} ] \right| \right| _ {p} \leq \int | g (t) | \left| \left| \left[ e ^ {i t \mathrm{S}}, \mathrm{T} \right] \right| \right| _ {p} d t \leq \mathrm{C} \int | g (t) | (\mathrm{I} + | t |) d t <   \infty \quad \square
$$

Proposition 6. (Cf. [34].) — Let $p \in [\mathrm{I}, \infty]$ and $\mathbf{P}, \mathbf{Q} \in \mathcal{L}(\mathbf{H})$ be such that $\mathrm{I} - \mathrm{PQ} \in \mathcal{L}^p(\mathrm{H})$, $\mathrm{I} - \mathrm{QP} \in \mathcal{L}^p(\mathrm{H})$. Then $\mathbf{P}$ is a Fredholm operator and for any integer $n \geq p$, one has,

$$
\text { Index   } \mathbf {P} = \text { Trace } (\mathrm{I} - \mathbf {Q P}) ^ {n} - \text { Trace } (\mathrm{I} - \mathbf {P Q}) ^ {n}.
$$

Proof. — Since 1 — QP and 1 — PQ are compact operators, P is a Fredholm operator. Moreover 1 is an isolated point in

$$
\mathrm{K} = \{\mathrm{i} \} \cup \text { Spectrum } (\mathrm{i} - \mathrm{PQ}) \cup \text { Spectrum } (\mathrm{i} - \mathrm{QP}).
$$

Let $\gamma$ be the boundary of a small closed disk $D$ with center $i$ such that $D \cap K = \{i\}$. Set

$$
e = \frac {1}{2 i \pi} \int_ {\gamma} \frac {d \lambda}{\lambda - (1 - Q P)}, f = \frac {1}{2 i \pi} \int_ {\gamma} \frac {d \lambda}{\lambda - (1 - P Q)}.
$$

Then $e = e^2$, $f = f^2$; $\mathbf{E}_1 = \text{Range of } e$, $\mathbf{F}_1 = \text{Range of } f$ are finite dimensional, and admit respectively $\mathbf{E}_2 = \text{Ker } e$, $\mathbf{F}_2 = \text{Ker } f$ as supplements in H. For any $\mu \in \mathbf{C}$ one has,

$$
\mathrm{Q} (\mu - \mathrm{PQ}) = (\mu - \mathrm{QP}) \mathrm{Q}.
$$

Thus, for any $\lambda \notin \mathbf{K}$, one has

$$
(\lambda - (\mathrm{I} - \mathrm{QP})) ^ {- 1} \mathrm{Q} = \mathrm{Q} (\lambda - (\mathrm{I} - \mathrm{PQ})) ^ {- 1}.
$$

This shows that $\mathbf{Q}f = e\mathbf{Q}$ and similarly that $\mathbf{Pe} = f\mathbf{P}$. Thus,

$$
\mathrm{P} \left(\mathrm{E} _ {1}\right) \subset \mathrm{F} _ {1}, \quad \mathrm{P} \left(\mathrm{E} _ {2}\right) \subset \mathrm{F} _ {2}, \quad \mathrm{Q} \left(\mathrm{F} _ {1}\right) \subset \mathrm{E} _ {1}, \quad \mathrm{Q} \left(\mathrm{F} _ {2}\right) \subset \mathrm{E} _ {2}.
$$

Let  $P_{j}$  (resp.  $Q_{j}$ ) be the restriction of P (resp. Q) to  $E_{j}$  (resp.  $F_{j}$ ), j = 1, 2. By construction the restrictions of QP to  $E_{2}$  and of PQ to  $F_{2}$  are invertible operators, and hence,

a) Index $\mathbf{P} = \dim \mathbf{E}_1 - \dim \mathbf{F}_1$,

$$
b) \operatorname{Trace} (\mathrm{I} _ {\mathrm{E} _ {2}} - \mathrm{Q} _ {2} \mathrm{P} _ {2}) ^ {n} = \operatorname{Trace} (\mathrm{I} _ {\mathrm{F} _ {2}} - \mathrm{P} _ {2} \mathrm{Q} _ {2}) ^ {n} \forall n \geq p.
$$

The spectrum of $\mathrm{I}_{\mathrm{E}_1} - \mathrm{Q}_1\mathrm{P}_1$ and of $\mathrm{I}_{\mathrm{F}_1} - \mathrm{P}_1\mathrm{Q}_1$ contains only $\{\mathrm{I}\}$, thus,

c) $\operatorname{Trace}(\mathrm{I}_{\mathrm{E}_1} - \mathrm{Q}_1\mathrm{P}_1)^n - \operatorname{Trace}(\mathrm{I}_{\mathrm{F}_1} - \mathrm{P}_1\mathrm{Q}_1)^n = \dim \mathrm{E}_1 - \dim \mathrm{F}_1.$

Combining $a), b), c)$, one gets the conclusion. $\square$

## Appendix 2: Fredholm modules

The notion of Fredholm module is due to Atiyah [3] in the even case, and to Brown, Douglas, Fillmore [11] and Kasparov [42] in the odd case. Their definitions are slightly different from the definition below and our aim is to clarify this point.

Let $\mathbf{X}$ be a compact space and $\mathbf{A} = \mathbf{C}(\mathbf{X})$. An element of Atiyah's $\operatorname{Ell}(\mathbf{X})$ is given by two representations,

$$
\sigma^ {+}: \mathrm{A} \rightarrow \mathcal {L} (\mathrm{H} ^ {+}), \quad \sigma^ {-}: \mathrm{A} \rightarrow \mathcal {L} (\mathrm{H} ^ {-})
$$

304

of A in Hilbert spaces  $H^{+}$ ,  $H^{-}$  and a Fredholm operator  $P:H^{+}\rightarrow H^{-}$  with parametrix Q, which intertwines  $\sigma^{+}$  and  $\sigma^{-}$  modulo compact operators,

$$
\mathrm{P} \sigma^ {+} (a) \mathrm{Q} - \sigma^ {-} (a) \in \mathscr {K} \quad \forall a \in \mathrm{A}.
$$

The typical example is obtained when X = V is a smooth compact manifold,  $\mathrm{H}^{\pm} = \mathrm{L}^{2}(\xi^{\pm})$  are Hilbert spaces of square integrable sections of bundles  $\xi^{\pm}$  over V,  $\sigma^{\pm}$  are the obvious actions of C(V) by multiplication, and P is an elliptic operator of order o from  $\xi^{+}$ to  $\xi^{-}$ . With Q a parametrix of P, let  $\mathrm{F} \in \mathcal{L}(\mathrm{H}^{+} \oplus \mathrm{H}^{-})$  be given by

$$
\mathbf {F} = \left[ \begin{array}{c c} \mathbf {0} & \mathbf {Q} \\ \mathbf {P} & \mathbf {0} \end{array} \right].
$$

One has,

$\alpha)$ H is a $\mathbf{Z}/2$ graded \* module over $\mathrm{A} = \mathrm{C}(\mathrm{X})$,

$\beta)$$[\mathbf{F},a]\in \mathcal{K}\quad \forall a\in \mathbf{A},$

$\gamma)\mathbf{F}^{2}-\mathrm{I}\in\mathcal{K}.$

Note that in general $\mathbf{F}^2 \neq \mathfrak{i}$ since $\mathbf{P}$ is not invertible.

Definition 1. — Let A be a Z/2 graded algebra over C. Then a pre-Fredholm module over A (resp. Fredholm module over A) is a pair (H, F) where

1) H is a $\mathbf{Z}/2$ graded Hilbert space and a graded left $\mathcal{A}$-module,

2) $\mathbf{F} \in \mathcal{L}(\mathbf{H})$, $\mathbf{F}\varepsilon = -\varepsilon \mathbf{F}$, $[\mathbf{F}, a] \in \mathcal{K} \quad \forall a \in \mathcal{A}$,

3) $a(\mathbf{F}^2 - \mathbf{i}) \in \mathcal{K} \forall a \in \mathcal{A} (resp. \mathbf{F}^2 = \mathbf{i}).$

We shall now show how to associate canonically to each pre-Fredholm module a Fredholm module.

Let $H_{c}$ be the Z/2 graded Hilbert space $H_{c}^{\pm} = C$ and let $\tilde{H} = H \hat{\otimes} H_{c}$ be the graded tensor product of H by $H_{c}$. One has $\tilde{H}^{+} = H^{+} \oplus H^{-}$, $\tilde{H}^{-} = H^{-} \oplus H^{+}$. We turn $\tilde{H}$ into a graded left A-module by

$$
a (\xi \hat {\otimes} \eta) = a \xi \hat {\otimes} e \eta \quad \forall a \in \mathscr {A}, \xi \in H, \eta \in H _ {\mathbf {c}},
$$

where $e\in \mathcal{L}(\mathrm{H}_{\mathbf{C}}),\quad e = \left[ \begin{array}{ll}\mathrm{I} & 0\\ \mathrm{o} & 0 \end{array} \right].$ Next, with $\mathbf{F} = \left[ \begin{array}{ll}\mathrm{o} & \mathrm{Q}\\ \mathrm{P} & 0 \end{array} \right]\in \mathcal{L}(\mathrm{H})$ we define

$\widetilde{\mathbf{F}}\in \mathcal{L}(\widetilde{\mathbf{H}}),\widetilde{\mathbf{F}} = \begin{bmatrix} \mathrm{o} & \widetilde{\mathbf{Q}}\\ \widetilde{\mathbf{P}} & \mathrm{o} \end{bmatrix}$ by

$$
\widetilde {\mathbf {P}} = \left[ \begin{array}{c c} \mathrm{P} & \mathrm{I} - \mathrm{PQ} \\ \mathrm{I} - \mathrm{QP} & (\mathrm{QP} - 2) \mathrm{Q} \end{array} \right], \quad \widetilde {\mathbf {Q}} = \left[ \begin{array}{c c} (2 - \mathrm{QP}) \mathrm{Q} & \mathrm{I} - \mathrm{QP} \\ \mathrm{I} - \mathrm{PQ} & - \mathrm{P} \end{array} \right].
$$

One checks that $\widetilde{\mathbf{P}}\widetilde{\mathbf{Q}} = \mathbf{i}$, $\widetilde{\mathbf{Q}}\widetilde{\mathbf{P}} = \mathbf{i}$, so that $\widetilde{\mathbf{F}}^2 = \mathbf{i}$.

Proposition 2. — Let (H, F) be a pre-Fredholm module over A.

a) $(\widetilde{\mathbf{H}},\widetilde{\mathbf{F}})$ is a Fredholm module over $\mathcal{A}$.

b) Let  $H_{0}$  be the Hilbert space H with opposite Z/2 grading and o-module structure over A, then  $(\mathrm{H}_{0},\mathrm{o})$  is a pre-Fredholm module over A.

305

c) One has $\widetilde{\mathbf{H}} = \mathbf{H} \oplus \mathbf{H}_0$ as a $\mathbf{Z}/2$ graded $\mathcal{A}$-module, and

$$
a (\widetilde {\mathbf {F}} - \mathbf {F} \oplus \mathbf {o}) \in \mathscr {K} \quad \forall a \in \mathscr {A}.
$$

Proof. — a) Since $\widetilde{\mathbf{F}}^{2} = \mathfrak{i}$, conditions 1) and 3) are verified. Let us check that $[\widetilde{\mathbf{F}}, a] \in \mathcal{K}$, $\forall a \in \mathcal{A}$. One has by hypothesis $[\mathbf{F}, a] \in \mathcal{K}$, $a(\mathbf{F}^{2} - \mathfrak{i}) \in \mathcal{K}$ and hence $(\mathbf{F}^{2} - \mathfrak{i}) a \in \mathcal{K}$. Let us first assume that $a$ is even. One has

$$
\widetilde {\mathbf {P}} a - a \widetilde {\mathbf {P}} = \left[ \begin{array}{c c} \mathrm{Pa} - a \mathrm{P} & a (\mathrm{I} - \mathrm{PQ}) \\ (\mathrm{I} - \mathrm{QP}) a & 0 \end{array} \right] \in \mathcal {K}.
$$

Since $\widetilde{\mathbf{Q}} = \widetilde{\mathbf{P}}^{-1}$ one gets $\widetilde{\mathbf{Q}} a - a\widetilde{\mathbf{Q}} \in \mathcal{K}$, hence $[\widetilde{\mathbf{F}}, a] \in \mathcal{K}$. Let now $a$ be odd and $\begin{bmatrix} 0 & a_{12} \\ a_{21} & 0 \end{bmatrix} \in \mathcal{L}(\mathbf{H})$ be the corresponding operator in H. By hypothesis one has

$$
a _ {1 2} \mathrm{P} + \mathrm{Q} a _ {2 1} \in \mathscr {K}, \quad a _ {2 1} \mathrm{Q} + \mathrm{P} a _ {1 2} \in \mathscr {K}, \quad (\mathrm{QP} - \mathrm{I}) a _ {1 2} \in \mathscr {K},
$$

$$
a _ {2 1} (\mathrm{QP} - \mathrm{I}) \in \mathscr {K}, \quad (\mathrm{PQ} - \mathrm{I}) a _ {2 1} \in \mathscr {K}, \quad a _ {1 2} (\mathrm{PQ} - \mathrm{I}) \in \mathscr {K}.
$$

The action of $a$ in $\widetilde{\mathbf{H}} = \widetilde{\mathbf{H}}^{+}\oplus \widetilde{\mathbf{H}}^{-}$ is given by the matrix

$$
\mathrm{T} = \left[ \begin{array}{c c} \mathrm{o} & \mathrm{T} ^ {\prime \prime} \\ \mathrm{T} ^ {\prime} & \mathrm{o} \end{array} \right] \quad \text { where } \mathrm{T} ^ {\prime} = \left[ \begin{array}{c c} a _ {2 1} & \mathrm{o} \\ \mathrm{o} & \mathrm{o} \end{array} \right], \quad \mathrm{T} ^ {\prime \prime} = \left[ \begin{array}{c c} a _ {1 2} & \mathrm{o} \\ \mathrm{o} & \mathrm{o} \end{array} \right].
$$

One has to check that  $T^{\prime\prime}\tilde{P} + \tilde{Q}T^{\prime} \in K$  and  $T^{\prime}\tilde{Q} + \tilde{P}T^{\prime\prime} \in K$ . This follows easily. from our hypothesis.

b) Obvious.

b) Obvious. c) Let $\mathbf{F}' = \mathbf{F} \oplus \mathbf{o}$. Then $\mathbf{F}' = \begin{bmatrix} \mathbf{o} & \mathbf{Q}' \\ \mathbf{P}' & \mathbf{o} \end{bmatrix}$ with $\mathbf{P}' = \begin{bmatrix} \mathbf{P} & \mathbf{o} \\ \mathbf{o} & \mathbf{o} \end{bmatrix}$, $\mathbf{Q}' = \begin{bmatrix} \mathbf{Q} & \mathbf{o} \\ \mathbf{o} & \mathbf{o} \end{bmatrix}$ With a even one has,

$$
a (\widetilde {\mathbf {P}} - \mathbf {P} ^ {\prime}) = \left[ \begin{array}{c c} 0 & a (\mathrm{I} - \mathrm{PQ}) \\ 0 & 0 \end{array} \right] \in \mathcal {K}
$$

$$
a (\widetilde {\mathbf {Q}} - \mathbf {Q} ^ {\prime}) = \left[ \begin{array}{c c} a (2 - \mathbf {Q P}) \mathbf {Q} - a \mathbf {Q} & a (\mathrm{I} - \mathbf {Q P}) \\ 0 & 0 \end{array} \right] \in \mathcal {K}.
$$

The odd case is treated similarly. $\square$

Let $p \in [1, \infty[$. We shall say that a pre-Fredholm module (H, F) over $\mathcal{A}$ is $p$-summable when,

$\alpha)$$[\mathbf{F},a]\in \mathcal{L}^p (\mathbf{H})$ for $a\in \mathcal{A}$,

$\beta) a(\mathbf{F}^2 - \mathbf{i}) \in \mathcal{L}^p(\mathbf{H})$ for $a \in \mathcal{A}$.

Proposition 3. — Let (H, F) be a p-summable pre-Fredholm module over A. Then ( $\widetilde{H}$ ,  $\widetilde{F}$ ) is a p-summable Fredholm module.

Proof. — In the proof of proposition 2 one can replace $\mathcal{K}$ by any two-sided ideal. □ We shall now discuss the index map associated to a Fredholm module.

306

Lemma 4. — Let A be a Z/2 graded algebra, (H, F) a Fredholm module over A.

a) Let $\widetilde{\mathcal{A}} = \mathcal{A} \oplus \mathbf{C}$ be obtained from $\mathcal{A}$ by adjoining a unit. Let $\widetilde{\mathcal{A}}$ act in H by $(a + \lambda\mathrm{i})\xi = a\xi + \lambda\xi$ for $a \in \mathcal{A}, \lambda \in \mathbf{C}$. Then (H, F) is a Fredholm module over $\widetilde{\mathcal{A}}$. b) Let $\mathrm{H}_n = \mathrm{H} \otimes \mathbf{C}^n$, $\mathrm{F}_n = \mathrm{F} \otimes \mathrm{id}_n$ and $\mathrm{M}_n(\mathcal{A}) = \mathcal{A} \otimes \mathrm{M}_n(\mathbf{C})$ act in $\mathrm{H}_n$ in the obvious way. Then $(\mathrm{H}_n, \mathrm{F}_n)$ is a Fredholm module over $\mathrm{M}_n(\mathcal{A})$.

The proof is obvious.

Let us now assume that A is trivially graded.

Proposition 5. — Let (H, F) be a Fredholm module over $\mathcal{A}$. There exists a unique additive map $\varphi: \mathrm{K}_{0}(\mathcal{A}) \to \mathbf{Z}$ such that for any idempotent $e \in \mathbf{M}_{n}(\widetilde{\mathcal{A}})$, $\varphi([e])$ is the index of the Fredholm operator from $e\mathrm{H}_{n}^{+}$ to $e\mathrm{H}_{n}^{-}$ given by

$$
\mathrm{T} \xi = e \mathrm{F} _ {n} \xi \quad \forall \xi \in e \mathrm{H} _ {n} ^ {+}.
$$

Proof. — One checks that T is a Fredholm operator with parametrix  $T'$  where  $T'\eta = eF_n\eta$  for  $\eta \in eH_n^-$ , and that the index of T is an additive function of the class of e in  $\mathrm{K}_{0}(\mathcal{A})$ .

Finally we shall relate the above notion of Fredholm module with the Kasparov A - B bimodules, we recall (cf. [42]).

Definition 6. — Let A and B be C\*-algebras. A Kasparov A—B bimodule is given by 1) a Z/2 graded C\*-module $\mathcal{E}=\mathcal{E}^{+}\oplus\mathcal{E}^{-}$ over B, 2) $a*$ homomorphism $\pi$ of A in $\mathcal{L}_{\mathrm{B}}(\mathcal{E})$, 3) an element F of $\mathcal{L}_{\mathrm{B}}(\mathcal{E})$ such that $\mathrm{F}=\begin{bmatrix}\mathrm{o}&\mathrm{Q}\\ \mathrm{P}&\mathrm{o}\end{bmatrix}$ and

$\alpha)$$[\mathbf{F},a]\in \mathcal{K}_{\mathrm{B}}(\mathcal{E})$$\forall a\in \mathbf{A},$

$\beta) a(F - F^{*}) \in \mathcal{K}_{B}(\mathcal{E}) \quad \forall a \in A,$

$\gamma) a(\mathbf{F}^2 - \mathrm{i}) \in \mathcal{K}_{\mathrm{B}}(\mathcal{E}) \quad \forall a \in \mathbf{A}$.

(Cf. [42] for the notions of endomorphism $(\mathcal{L}_{\mathrm{B}}(\mathcal{E}))$ of $\mathcal{E}$ and of compact endomorphism $(\mathcal{K}_{\mathrm{B}}(\mathcal{E}).)$

Let us take $\mathbf{B} = \mathbf{C}$. Then a Kasparov $\mathbf{A} - \mathbf{C}$ bimodule is in particular a pre-Fredholm module over $\mathbf{A}$. Conversely,

Proposition 7. — Let A be a C\*-algebra and (H, F) a \* Fredholm module over A. Let $\mathbf{F}' = \mathbf{F}|\mathbf{F}|^{-1}$. Then (H, F') is a Kasparov A - C bimodule. Moreover, for each t, $\mathbf{F}_t = \mathbf{F}|\mathbf{F}|^{-t}$ defines a \* Fredholm module (H, $\mathbf{F}_t$).

Proof. — One has  $[F^{*}F, a] \in K$ ,  $\forall a \in A$ , thus  $[|F|^{s}, a] \in K$  for  $s \in R$ ,  $a \in A$ . Let  $F = J\Delta$  be the polar decomposition of F, with  $\Delta = |F|$ . One has  $F^{-1} = \Delta^{-1}J^{-1}$  which gives the right polar decomposition of  $F = F^{-1}$ , thus  $J = J^{-1}$  and  $J = J^{*} = F'$ , so that  $(H, F')$  is a Kasparov A - C bimodule. Finally  $J\Delta J^{-1} = \Delta^{-1}$  and hence  $J\Delta^{s}J^{-1} = \Delta^{-s}$  for any  $s \in R$ , so that  $J\Delta^{s}$  is an involution for any s. It follows that  $(H, F_{s})$  is a \*Fredholm module. □

## Appendix 3: Stability under holomorphic functional calculus

Let A be a Banach algebra over C and A a subalgebra of A,  $\tilde{A}$  and  $\tilde{A}$  be obtained by adjoining a unit.

Definition 1. — $\mathcal{A}$ is stable under holomorphic functional calculus if and only if for any $n \in \mathbf{N}$ and $a \in \mathrm{M}_n(\widetilde{\mathcal{A}}) \subset \mathrm{M}_n(\widetilde{\mathbf{A}})$ one has,

$$
f (a) \in \mathrm{M} _ {n} (\widetilde {\mathcal {A}})
$$

for any function $f$ holomorphic in a neighborhood of the spectrum of $a$ in $\mathbf{M}_n(\widetilde{\mathbf{A}})$.

In particular one has  $\mathrm{GL}_{n}(\widetilde{\mathcal{A}})=\mathrm{GL}_{n}(\widetilde{\mathrm{A}})\cap\mathrm{M}_{n}(\widetilde{\mathcal{A}})$ , hence if we endow  $\mathrm{GL}_{n}(\widetilde{\mathcal{A}})$  with the induced topology we get a topological group which is locally contractible as a topological space. We recall the density theorem (cf. [4], [40]).

Proposition 2. — Let A be a dense subalgebra of A, stable under holomorphic functional calculus.

a) The inclusion $i: \mathcal{A} \to \mathbf{A}$ is an isomorphism of $\mathbf{K}_0$-groups

$$
i _ {*}: \mathrm{K} _ {0} (\mathcal {A}) \rightarrow \mathrm{K} _ {0} (\mathrm{A}).
$$

b) Let $\mathrm{GL}_{\infty}(\widetilde{\mathcal{A}})$ be the inductive limit of the topological groups $\mathrm{GL}_n(\widetilde{\mathcal{A}})$. Then $i_*$ yields an isomorphism,

$$
\pi_ {k} (\mathbf {G L} _ {\infty} (\widetilde {\mathcal {A}})) \rightarrow \pi_ {k} (\mathbf {G L} _ {\infty} (\widetilde {\mathbf {A}})) = \mathbf {K} _ {k + 1} (\mathbf {A}).
$$

Let now (H, F) be a Fredholm module over the Banach algebra A and assume that the corresponding homomorphism of A in $\mathcal{L}(\mathrm{H})$ is continuous.

Proposition 3. — Let $p \in [\mathrm{I}, \infty[$ and $\mathcal{A} = \{a \in \mathrm{A}, [\mathrm{F}, a] \in \mathcal{L}^p(\mathrm{H})\}$. Then $\mathcal{A}$ is a subalgebra of A stable under holomorphic functional calculus.

Proof. — One has  $[F, ab] = [F, a] b + a[F, b]$  for  $a, b \in A$ . Thus as  $\mathcal{L}^{p}(H)$  is a two-sided ideal in  $\mathcal{L}(H)$ , A is a subalgebra of A. Let  $n \in N$ ,  $(H_{n}, F_{n})$  be the Fredholm module over  $M_{n}(A)$  given by lemma 4 b) of Appendix 2 and  $\pi_{n}$  the corresponding homomorphism:  $M_{n}(A) \to \mathcal{L}(H_{n})$ . One has,

$$
\mathrm{M} _ {n} (\mathcal {A}) = \left\{a \in \mathrm{M} _ {n} (\widetilde {\mathrm{A}}), [ \mathrm{F} _ {n}, \pi_ {n} (a) ] \in \mathscr {L} ^ {p} (\mathrm{H} _ {n}) \right\}.
$$

Moreover $\operatorname{Sp}(\pi_n(a)) \subset \operatorname{Sp}(a)$, and since $\pi_n$ is continuous, $\pi_n(f(a)) = f(\pi_n(a))$ for any $f$ holomorphic on $\operatorname{Sp}(a)$. The conclusion follows from proposition 5 of Appendix I.

Let now A be a C\*-algebra and A a dense \* subalgebra of A stable under holomorphic functional calculus.

Proposition 4. — Let (H, F) be a \* Fredholm module over A. Then the corresponding \* homomorphism π of A in L(H) is continuous and extends to a \* homomorphism π of A in L(H) yielding a \* Fredholm module over A.

Proof. — We can assume that A and A are unital and  $\pi(1) = 1$ . Let  $a \in A$ , then the Spectrum of  $a^{*}a$  in A is the same as its Spectrum in A. Thus the norm of a in A is  $||a|| = \rho^{1/2}$  where  $\rho$  is the radius of the Spectrum of  $a^{*}a$  in A. One has

$$
\text { Spectrum } (\pi (a ^ {*} a)) \subset \text { Spectrum } (a ^ {*} a),
$$

thus

$$
\left| \left| \pi (a) \right| \right| ^ {2} = \text { Spectral   radius   of } \pi (a ^ {*} a) \leq \rho = \left| \left| a \right| \right| ^ {2}.
$$

This shows that $\pi$ is continuous. Let $\widetilde{\pi}$ be the corresponding $*$ homomorphism of A in $\mathcal{L}(\mathrm{H})$. For $a \in \mathrm{A}$, $[\mathrm{F}, \widetilde{\pi}(a)]$ is a norm limit of $[\mathrm{F}, \pi(a_n)]$, $a_n \in \mathcal{A}$, which are compact operators by hypothesis, thus $[\mathrm{F}, \widetilde{\pi}(a)] \in \mathcal{K}$ for all $a \in \mathrm{A}$.

In part I the construction of the Chern character of an element of K-homology led to the definition of a purely algebraic cohomology theory  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$ . By construction, given any (possibly non commutative) algebra A over C,  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$  is the cohomology of the complex  $(\mathbf{C}_{\lambda}^{n}, b)$  where  $C_{\lambda}^{n}$  is the space of  $(n + 1)$ -linear functionals  $\varphi$  on A such that

$$
\varphi (a ^ {1}, \dots , a ^ {n}, a ^ {0}) = (- \mathrm{I}) ^ {n} \varphi (a ^ {0}, \dots , a ^ {n}) \quad \forall a ^ {i} \in \mathscr {A}
$$

and where b is the Hochschild coboundary map given by

$$
\begin{array}{r l} (b \varphi) (a ^ {0}, \dots , a ^ {n + 1}) & = \sum_ {j = 0} ^ {n} (- \mathrm{I}) ^ {j} \varphi (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}) \\ & \quad + (- \mathrm{I}) ^ {n + 1} \varphi (a ^ {n + 1} a ^ {0}, \dots , a ^ {n}). \end{array}
$$

Moreover  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$  turned out to be naturally a module over  $\mathrm{H}_{\lambda}^{*}(\mathbf{C})$  which is a polynomial ring with one generator  $\sigma$  of degree 2.

In this second part we shall develop this cohomology theory from scratch, using part I only as a motivation.

We shall arrive, in section 4, at an exact couple of the form

![](images/page_54_image_7.jpg)

relating  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$  to the Hochschild cohomology of A with coefficients in the bimodule of linear functionals on A. This will give a powerful tool to compute  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$  since Hochschild cohomology, defined as a derived functor, is computable via an arbitrary resolution of the bimodule A (cf. [13] [47]).

For instance, if one takes for A the algebra  $\mathbf{C}^{\infty}(\mathbf{V})$  of smooth functions on a compact manifold V and imposes the obvious continuity to multilinear functionals on A, one arrives quickly at the equality (for arbitrary n)

$$
\mathrm{H} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) = \text { space   of   all   de   Rham   currents   of   dimension } n.
$$

(This will be dealt with in section 5. The purely algebraic results of sections 1 to 4 easily adapt to the topological situation.) The operator $\mathbf{I} \circ \mathbf{B}: \mathrm{H}^n(\mathcal{A}, \mathcal{A}^*) \to \mathrm{H}^{n-1}(\mathcal{A}, \mathcal{A}^*)$ coincides with the usual de Rham boundary for currents, and the computation of $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$ will follow easily (cf. section 5). In particular we shall get

$$
\mathrm{H} ^ {*} (\mathcal {A}) = \text { Ordinary   de   Rham   homology   of   V },
$$

where $\mathbf{H}^{*}(\mathcal{A})$ is defined as in part I by

$$
\mathrm{H} ^ {*} (\mathcal {A}) = \mathrm{H} _ {\lambda} ^ {*} (\mathcal {A}) \otimes_ {\mathrm{H} _ {\lambda} ^ {*} (\mathbf {c})} \mathbf {C}.
$$

As another application we shall compute  $\mathbf{H}^{*}(\mathcal{A})$  for the following highly non commutative algebra. Fix  $\theta \in R/Z$ ,  $\theta \notin Q/Z$ . Then  $A_{\theta}$  is defined by

$$
\mathscr {A} _ {\theta} = \left\{\Sigma a _ {n, m} U ^ {n} V ^ {m}; \left(a _ {n, m}\right) _ {n, m \in \mathbf {Z}} \text { sequence   of   rapid   decay } \right\},
$$

where  $\mathrm{VU} = (\exp i2\pi\theta) \mathrm{UV}$  gives the product rule. The algebra  $A_{\theta}$  corresponds to the “irrational rotation C\*-algebra” studied by Rieffel [58] and Pimsner and Voiculescu [55]. It arises in the study of the Kronecker foliation of the 2-torus [16].

In section 1 we introduce the following notion of cycle over an algebra $\mathcal{A}$ which is crucial both for the construction of the cup product

$$
\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) \times \mathrm{H} _ {\lambda} ^ {m} (\mathcal {B}) \rightarrow \mathrm{H} _ {\lambda} ^ {n + m} (\mathcal {A} \otimes \mathcal {B})
$$

and for the construction of B :  $\mathbf{H}^{n+1}(\mathcal{A},\mathcal{A}^{*})\to\mathbf{H}_{\lambda}^{n}(\mathcal{A})$ .

By definition a cycle of dimension $n$ is a triple $(\Omega, d, \int)$ where $\Omega = \bigoplus_{j=0}^{\infty} \Omega^j$ is a graded algebra, $d$ is a graded derivation of degree 1 such that $d^2 = 0$, and $\int: \Omega^n \to \mathbf{C}$ is a closed graded trace. A cycle over an algebra $\mathcal{A}$ is given by a homomorphism $\rho: \mathcal{A} \to \Omega^0$ where $(\Omega, d, \int)$ is a cycle.

In part I we saw that any p-summable Fredholm module over A yields such a cycle. Here are some other examples.

## 1) Foliations

Let $(\mathbf{V},\mathbf{F})$ be a transversally oriented foliated manifold. Using the canonical integral of operator valued transverse differential forms [14] of degree $q = \operatorname{Codim} \mathbf{F}$, we shall construct in Part VI a cycle of dimension $q$ over the algebra $\mathcal{A} = \mathbf{C}_{c}^{\infty}(\operatorname{Graph}(\mathbf{V},\mathbf{F}))$.

## 2) $\mathbf{C}^*$ dynamical systems

Given a  $C^{*}$  dynamical system  $(A, G, \alpha)$  (cf. [19]) where G is a Lie group, the construction of [19] associates a cycle on the algebra  $A^{\infty}$  of smooth elements of A to any pair of an invariant trace  $\tau$  on A and a closed element  $v \in \wedge$  (Lie G).

## 3) Discrete groups

In part V we shall associate a cycle on the group algebra  $\mathbf{C}(\Gamma)$  to any group cocycle  $\omega\in\mathbf{Z}^{n}(\Gamma,\mathbf{C})$  and obtain in this way a natural map of the group cohomology  $\mathrm{H}^{n}(\Gamma,\mathbf{C})$  to  $\mathrm{H}_{\lambda}^{n}(\mathbf{C}(\Gamma))$ .

Given a cycle of dimension $n$, $\mathcal{A} \xrightarrow{\mathfrak{p}} \Omega$ over $\mathcal{A}$, its character is the $(n + 1)$-linear functional

$$
\tau (a ^ {0}, \dots , a ^ {n}) = \int \rho (a ^ {0}) d \rho (a ^ {1}) \dots d \rho (a ^ {n}).
$$

We show that $\tau \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A}) = \mathbf{C}_{\lambda}^{n}(\mathcal{A}) \cap \operatorname{Ker} b$, that any element of $\mathbf{Z}_{\lambda}^{n}(\mathcal{A})$ appears in this way and that the elements of $\mathbf{B}_{\lambda}^{n}(\mathcal{A}) = b\mathbf{C}_{\lambda}^{n-1}(\mathcal{A})$ are those coming from cycles with $\Omega^0$ flabby. (See [40] for the definition of a flabby algebra).

Then the straightforward notion of tensor product of two cycles gives a cup product

$$
\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) \otimes \mathrm{H} _ {\lambda} ^ {m} (\mathcal {B}) \rightarrow \mathrm{H} _ {\lambda} ^ {n + m} (\mathcal {A} \otimes \mathcal {B}).
$$

We then check that  $H_{\lambda}^{*}(\mathbf{C})$  is a polynomial ring with a canonical generator  $\sigma$  of degree 2 and we define at the level of cochains the map

$$
\mathrm{S}: \mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) \rightarrow \mathrm{H} _ {\lambda} ^ {n + 2} (\mathcal {A})
$$

given by cup product by  $\sigma$ .

In section 2 we show that the standard construction of the Chern character by connexion and curvature gives a pairing of $\mathrm{H}_{\lambda}^{\mathrm{ev}}(\mathcal{A})$ with the algebraic K theory group $\mathbf{K}_0(\mathcal{A})$ and of $\mathrm{H}_{\lambda}^{\mathrm{odd}}(\mathcal{A})$ with $\mathbf{K}_1$. The invariance of this pairing naturally yields the group $\mathrm{H}^{*}(\mathcal{A}) = \mathrm{H}_{\lambda}^{*}(\mathcal{A}) \otimes_{\mathrm{H}_{\lambda}^{*}(\mathbb{C})}\mathbf{C}$, inductive limit of the groups $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$ with map S.

We then discuss the invariance of  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$  under Morita equivalence. In section 3 we show that two cycles over A are cobordant (cf. 3 for the definition of cobordism) if and only if their characters  $\tau_{1}, \tau_{2}$  differ by an element of the image of B, where B is a canonical map of the Hochschild cohomology  $\mathrm{H}^{n+1}(\mathcal{A}, \mathcal{A}^{*})$  to  $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$  defined as follows:

$$
\mathbf {B} \tau = \sum_ {\gamma \in \Gamma} \varepsilon (\gamma) \left(\mathbf {B _ {0}} \tau\right) ^ {\gamma}
$$

where $\Gamma$ is the group of cyclic permutations of $\{0, \ldots, n\}$,

$$
\varphi^ {\gamma} (a ^ {0}, \dots , a ^ {n}) = \varphi (a ^ {\gamma (0)}, \dots , a ^ {\gamma (n)}),
$$

$\varepsilon$ is the signature and $(\mathbf{B}_0\tau)(a^0,\ldots ,a^n) = \tau (\mathrm{I},a^0,\ldots ,a^n) + (-\mathrm{I})^n\tau (a^0,\ldots ,a^n,\mathrm{I})$ for all $a^i\in \mathcal{A}$. Thus defined at the level of cochains, $\mathbf{B}:\mathbf{C}^n (\mathcal{A},\mathcal{A}^*)\to \mathbf{C}^{n - 1}(\mathcal{A},\mathcal{A}^*)$ commutes (in the graded sense) with the Hochschild coboundary $b$, which yields the basic double complex of section 4.

The above result yields a new interpretation of  $\mathrm{H}^{*}(\mathcal{A})$  as

$$
\mathrm{H} ^ {*} (\mathcal {A}) = (\text { Cobordism   group   of   cycles   over } \mathcal {A}) \otimes_ {\text { Cobordism   of } \mathbb {C}} \mathbf {C}
$$

which is completed in section 4 thanks to the exact triangle

$$
\begin{array}{c} \mathrm{H} ^ {*} (\mathcal {A}, \mathcal {A} ^ {*}) \\ \Big \downarrow^ {\mathrm{B}} \\ \mathrm{H} _ {\lambda} ^ {*} (\mathcal {A}) \xrightarrow {\mathrm{s}} \mathrm{H} _ {\lambda} ^ {*} (\mathcal {A}) \end{array}
$$

where I is induced by the inclusion map from the subcomplex  $C_{\lambda}^{n}$  to  $C^{n}$ . This exact triangle gives in particular the characterization of the image of S which was missing in part I (cf. theorem 16):  $\tau \in Im S$  if and only if  $\tau$  is a Hochschild coboundary. It also proves that  $H_{\lambda}^{n}(\mathcal{A})$  is periodic with period 2 above the Hochschild dimension of A.

By comparing the above exact triangle with the derived exact sequence of $\mathbf{o} \to \mathbf{C}_{\lambda}^{n} \to \mathbf{C}^{n} \to \mathbf{C}^{n} / \mathbf{C}_{\lambda}^{n} \to \mathbf{o}$ we prove that there is a natural isomorphism

$$
\mathrm{H} ^ {n} (\mathbf {C} / \mathbf {C} _ {\lambda}) \cong \mathrm{H} _ {\lambda} ^ {n - 1} (\mathscr {A}).
$$

We then show that the cohomology of the double complex

$$
\mathbf {C} ^ {n, m} = \mathbf {C} ^ {n - m} (\mathcal {A}, \mathcal {A} ^ {*}), \quad d _ {1} = b, \quad d _ {2} = \mathbf {B}
$$

is equal to  $\mathrm{H}^{\mathrm{ev}}(\mathcal{A})$  for n even, and  $\mathrm{H}^{\mathrm{odd}}(\mathcal{A})$  for n odd. The spectral sequence associated to the first filtration ( $\sum_{n\geq p}C^{n,m}$ ) does not converge in general, and in fact has initial term  $E_{2}$  always o. This and the equality  $S=bB^{-1}$  are the technical facts allowing to identify the cohomology of this double complex with  $\mathrm{H}^{*}(\mathcal{A})$ .

The spectral sequence associated to the second filtration  $(\sum_{m\geq q}\mathbf{C}^{n,m})$  is always convergent. It coincides with the spectral sequence associated to the above exact couple and

1) its initial term $\mathbf{E}_1$ is the complex $(\mathbf{H}^n (\mathcal{A},\mathcal{A}^*),\mathbf{I}\circ \mathbf{B})$ of Hochschild cohomology groups with the differential given by the map $\mathbf{I}\circ \mathbf{B}$;

2) its limit is the graded group associated to the filtration  $\mathbf{F}^{n}(\mathbf{H}^{*}(\mathcal{A}))$  by dimensions of cycles.

Finally we note that in a purely algebraic context the homology theory (which is dual to the cohomology theory we describe here) is more natural. All the results of our paper are easily transposed to the homological side. However, from the point of view of analysis, the cohomology appeared more naturally and, for technical reasons (non Hausdorff quotient spaces), it is not in general the dual of the homology theory. This motivates our choice.

## Part II is organized as follows:

## CONTENTS

1. Definition of $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$ and cup product 97  
2. Pairing of $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$ with $\mathrm{K}_4(\mathcal{A})$, $i = 0,1$ 107  
3. Cobordism of cycles and the operator B 114  
4. The exact couple relating $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$ to Hochschild cohomology 119  
5. Locally convex algebras 125  
6. Examples 127

## 1. Definition of  $H_{\lambda}^{n}(\mathcal{A})$  and cup product

By a cycle of dimension $n$, we shall mean a triple $(\Omega, d, \int)$ where $\Omega = \bigoplus_{j=0}^{\infty} \Omega_j$ is a graded algebra, $d$ is a graded derivation of degree 1 with $d^2 = 0$ and $\int: \Omega^n \to \mathbf{C}$ is a closed graded trace.

Thus one has:

$$
\begin{array}{l} \text { I) } \Omega^ {i} \times \Omega^ {j} \subset \Omega^ {i + j} \forall i, j \in \{0, 1, \dots , n \}, i + j \leq n; \\ 2) d \Omega^ {i} \subset \Omega^ {i + 1}, d (\omega \omega^ {\prime}) = (d \omega) \omega^ {\prime} + (- 1) ^ {\deg \omega} \omega d \omega^ {\prime}, d ^ {2} = 0; \\ 3) \int d \omega = 0, \forall \omega \in \Omega^ {n - 1}; \int \omega^ {\prime} \omega = (- 1) ^ {\deg \omega \deg \omega^ {\prime}} \int \omega \omega^ {\prime}. \end{array}
$$

Given two cycles $\Omega$, $\Omega'$ of dimension $n$, their sum $\Omega \oplus \Omega'$ is defined by $(\Omega'')^i = \Omega^i \oplus \Omega'^i$, $(\omega_1, \omega_1') (\omega_2, \omega_2') = (\omega_1 \omega_2, \omega_1' \omega_2')$, $d(\omega, \omega') = (d\omega, d\omega')$ and $\int (\omega, \omega') = \int \omega + \int \omega'$.

Given cycles $\Omega, \Omega'$ of dimensions $n$ and $n'$, their tensor product $\Omega'' = \Omega \otimes \Omega'$ is the cycle of dimension $n + n'$ which as a differential graded algebra is the tensor product of $(\Omega, d)$ by $(\Omega', d')$, and where

$$
\int (\omega \otimes \omega^ {\prime}) = \int \omega \quad \int \omega^ {\prime} \quad \forall \omega \in \Omega^ {n}, \quad \omega^ {\prime} \in \Omega^ {n ^ {\prime}}.
$$

For example, let V be a smooth compact manifold, and let C be a closed current of dimension $q$ ($\leq \dim V$) on V. Let $\Omega^i$, $i \in \{0, \ldots, q\}$ be the space $\mathbf{C}^\infty(V, \wedge^i T^*V)$ of smooth differential forms of degree $i$. With the usual product structure and differentiation $\Omega = \bigoplus_{i=0}^{q} \Omega^i$ is a differential algebra, on which the equality $\int \omega = \langle C, \omega \rangle$, for $\omega \in \Omega^q$, defines a closed graded trace.

In this example $\Omega$ was graded commutative but this is not required in general. Now let $\mathcal{A}$ be an algebra, and $\Omega(\mathcal{A})$ be the universal graded differential algebra associated to $\mathcal{A}$ ([1] [39]).

Proposition 1. — Let $\tau$ be an $(n + 1)$-linear functional on $\mathcal{A}$. Then the following conditions are equivalent:

1) There exists an $n$-dimensional cycle $(\Omega, d, \int)$ and a homomorphism $\rho: \mathcal{A} \to \Omega^0$ such that

$$
\tau (a ^ {0}, \dots , a ^ {n}) = \int \rho (a ^ {0}) d (\rho (a ^ {1})) \dots d (\rho (a ^ {n})) \quad \forall a ^ {0}, \dots , a ^ {n} \in \mathscr {A}.
$$

2) There exists a closed graded trace $\mathbf{T}$ of dimension $n$ on $\Omega(\mathcal{A})$ such that

$$
\tau \left(a ^ {0}, \dots , a ^ {n}\right) = \mathrm{T} \left(a ^ {0} d a ^ {1} \dots d a ^ {n}\right) \quad \forall a ^ {0}, \dots , a ^ {n} \in \mathscr {A}.
$$

3) One has $\tau(a^1, \ldots, a^n, a^0) = (-\mathrm{I})^n \tau(a^0, \ldots, a^n)$ for $a^0, \ldots, a^n \in \mathcal{A}$ and

$$
\begin{array}{l} \sum_ {i = 0} ^ {n} (- \mathrm{I}) ^ {i} \tau (a ^ {0}, \dots , a ^ {i} a ^ {i + 1}, \dots , a ^ {n + 1}) \\ \qquad + (- \mathrm{I}) ^ {n + 1} \tau (a ^ {n + 1} a ^ {0}, \dots , a ^ {n}) = 0 \quad \text { for } a ^ {0}, \dots , a ^ {n + 1} \in \mathscr {A}. \end{array}
$$

Proof. — Let us first recall the construction of the universal algebra $\Omega(\mathcal{A})$ ([1] [39]). Even if $\mathcal{A}$ is already unital, let $\widetilde{\mathcal{A}}$ be the algebra obtained from $\mathcal{A}$ by adjoining a unit: $\widetilde{\mathcal{A}} = \{a + \lambda\mathrm{I}; a \in \mathcal{A}, \lambda \in \mathbf{C}\}$. For each $n \in \mathbf{N}$, $n \geq 1$, let $\Omega^n(\mathcal{A})$ be the linear space

$$
\Omega^ {n} (\mathcal {A}) = \widetilde {\mathcal {A}} \otimes \bigotimes_ {1} ^ {n} \mathcal {A}.
$$

314

The differential $d:\Omega^n\to \Omega^{n + 1}$ is given by

$$
d \left(\left(a ^ {0} + \lambda^ {0} \mathrm{I}\right) \otimes a ^ {1} \otimes \dots \otimes a ^ {n}\right) = \mathrm{I} \otimes a ^ {0} \otimes \dots \otimes a ^ {n} \in \Omega^ {n + 1}.
$$

By construction one has $d^2 = 0$. Let us now define the product $\Omega^i \times \Omega^j \to \Omega^{i+j}$. One first defines a right $\mathcal{A}$-module structure on $\Omega^n$ by the equality

$$
\left(\widetilde {a} ^ {0} \otimes a ^ {1} \otimes \dots \otimes a ^ {n}\right) a = \sum_ {j = 0} ^ {n} (- 1) ^ {n - j} \widetilde {a} ^ {0} \otimes \dots \otimes a ^ {j} a ^ {j + 1} \otimes \dots \otimes a.
$$

Let us check that $(\omega a)b = \omega (ab)\forall \omega \in \Omega^n,a,b\in \mathcal{A}$ . One has

$$
\left(\widetilde {a} ^ {0} \otimes \dots \otimes a ^ {j - 1} \otimes a ^ {j} a ^ {j + 1} \otimes \dots \otimes a ^ {n} \otimes a ^ {n + 1}\right) a ^ {n + 2} = \sum_ {k = 0} ^ {n + 1} \varepsilon_ {j, k} \alpha_ {j, k}
$$

where

$$
\varepsilon_ {j, k} = 0 \quad \text { if } j = k, \quad \varepsilon_ {j, k} = (- 1) ^ {n + k - 1} \quad \text { if } j <   k
$$

$$
\text { and } \quad \varepsilon_ {j, k} = (- \mathrm{I}) ^ {n - k} \quad \text { if } k <   j
$$

while

$$
\alpha_ {j, k} = \alpha_ {k, j} = a ^ {0} \otimes \dots \otimes a ^ {j} a ^ {j + 1} \otimes \dots \otimes a ^ {k} a ^ {k + 1} \otimes \dots \otimes a ^ {n + 2}.
$$

Thus if one expands $((\widetilde{a}^0\otimes \ldots \otimes a^n)a^{n + 1})a^{n + 2}$, one gets twice the term $\alpha_{j,k}$ for $j,k\in \{\mathbf{o},\mathbf{i},\dots ,n\}$ and with opposite signs:

$$
(- \mathrm{I}) ^ {n - j} (- \mathrm{I}) ^ {n + 1 - k} \quad \text { and } \quad (- \mathrm{I}) ^ {n - k} (- \mathrm{I}) ^ {n - j}.
$$

Thus

$$
\begin{array}{r l} \left(\left(\widetilde {a} ^ {0} \otimes \dots \otimes a ^ {n}\right) a ^ {n + 1}\right) a ^ {n + 2} & = \sum_ {j = 0} ^ {n} (- 1) ^ {n - j} \varepsilon_ {j, n + 1} \alpha_ {j, n + 1} \\ & = \left(\widetilde {a} ^ {0} \otimes \dots \otimes a ^ {n}\right) (a ^ {n + 1} a ^ {n + 2}). \end{array}
$$

This right action of $\mathcal{A}$ on $\Omega^n$ extends to a unital action of $\tilde{\mathcal{A}}$. One then defines the product: $\Omega^i \times \Omega^j \to \Omega^{i+j}$ by

$$
\omega \left(\widetilde {b} ^ {0} \otimes b ^ {1} \otimes \dots \otimes b ^ {j}\right) = \omega \widetilde {b} _ {0} \otimes b ^ {1} \otimes \dots \otimes b ^ {j} \quad \forall \omega \in \Omega^ {i}.
$$

It is then immediate that the product is associative.

With $\omega = \widetilde{a}^0\otimes a^1\otimes \ldots \otimes a^n\in \Omega^n$ , one has, for $a\in \mathcal{A}$

$$
d (\omega a) = \sum_ {j = 0} ^ {n} (- \mathrm{I}) ^ {n - j} \mathrm{I} \otimes a ^ {0} \otimes \dots \otimes a ^ {j} a ^ {j + 1} \otimes \dots \otimes a,
$$

$$
\begin{array}{r l} (d \omega) a & = \sum_ {j = 0} ^ {n + 1} (- \mathrm{I}) ^ {n + 1 - j} \mathrm{I} \otimes a ^ {0} \otimes \dots \otimes a ^ {j - 1} a ^ {j} \otimes \dots \otimes a \\ & = (- \mathrm{I}) ^ {n - 1} \omega d a + d (\omega a). \end{array}
$$

Thus $(\Omega, d)$ is a differential graded algebra, and the equality

$$
\widetilde {a} ^ {0} d a ^ {1} \dots d a ^ {n} = \widetilde {a} ^ {0} \otimes a ^ {1} \otimes \dots \otimes a ^ {n}
$$

shows that it is generated by $\mathcal{A}$. One checks that any homomorphism $\mathcal{A} \xrightarrow{\rho} \Omega'^0$ of $\mathcal{A}$ in a differential graded algebra $(\Omega', d')$, $d'^2 = 0$, extends to a homomorphism $\bar{\rho}$ of $(\Omega(\mathcal{A}), d)$ to $(\Omega', d')$ with

$$
\begin{array}{r l} \overline {{{\rho}}} (\widetilde {a} ^ {0} d a ^ {1} \dots d a ^ {n}) & = \rho (a ^ {0}) d ^ {\prime} (\rho (a ^ {1})) d ^ {\prime} (\rho (a ^ {2})) \dots d ^ {\prime} (\rho (a ^ {n})) \\ & \quad + \lambda^ {0} d ^ {\prime} (\rho (a ^ {1})) \dots d ^ {\prime} (\rho (a ^ {n})) \end{array}
$$

for $a^i \in \mathcal{A}$, $\widetilde{a}^0 \in \widetilde{\mathcal{A}}$, $\widetilde{a}^0 = (a^0, \lambda^0)$.

315

Thus 1) and 2) are obviously equivalent. Let us show that 3) $\Rightarrow$ 2). Given any $(n + 1)$-linear functional $\varphi$ on $\mathcal{A}$, define $\hat{\varphi}$ as a linear functional on $\Omega^n (\mathcal{A})$ by

$$
\hat {\varphi} ((a ^ {0} + \lambda^ {0} \mathrm{I}) \otimes a ^ {1} \otimes \dots \otimes a ^ {n}) = \varphi (a ^ {0}, a ^ {1}, \dots , a ^ {n}).
$$

By construction one has $\hat{\varphi}(d\omega) = 0$ for all $\omega \in \Omega^{n-1}(\mathcal{A})$. Now, with $\tau$ satisfying 3) let us show that $\hat{\tau}$ is a graded trace. We have to show that

$$
\begin{array}{r l} \widehat {\tau} ((a ^ {0} d a ^ {1} \dots d a ^ {k}) (a ^ {k + 1} d a ^ {k + 2} \dots d a ^ {n + 1})) \\ = (- 1) ^ {k (n - k)} \widehat {\tau} ((a ^ {k + 1} d a ^ {k + 2} \dots d a ^ {n + 1}) (a ^ {0} d a ^ {1} \dots d a ^ {k})). \end{array}
$$

Using the definition of the product in $\Omega(\mathcal{A})$ the first term gives

$$
\sum_ {0} ^ {k} (- 1) ^ {k - j} \tau (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}),
$$

and the second one gives

$$
\sum_ {j = 0} ^ {n - k} (- \mathrm{I}) ^ {k (n - k) + n - k - j} \tau \left(a ^ {k + 1}, \dots , a ^ {k + 1 + j} a ^ {k + 1 + j + 1}, \dots , a ^ {k}\right).
$$

The cyclic permutation $\lambda$, $\lambda(\ell) = k + \mathrm{i} + \ell$, has a signature equal to $(-1)^{n(k+1)}$ so that, as $\tau^{\lambda} = \varepsilon(\lambda)\tau$ by hypothesis, the second term gives

$$
- \sum_ {k + 1} ^ {n + 1} (- \mathrm{I}) ^ {k - j} \tau (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}).
$$

Hence the equality follows from the second hypothesis on  $\tau$ .

Let us show that 1) $\Rightarrow 3)$. We can assume that $\mathcal{A} = \Omega^0$. One has

$$
\begin{array}{r l} \tau (a ^ {0}, a ^ {1}, \dots , a ^ {n}) & = \int (a ^ {0} d a ^ {1}) (d a ^ {2} \dots d a ^ {n}) = (- 1) ^ {n - 1} \int (d a ^ {2} \dots d a ^ {n}) (a ^ {0} d a ^ {1}) \\ & = (- 1) ^ {n} \int (d a ^ {2} \dots d a ^ {n} d a ^ {0}) a ^ {1} = (- 1) ^ {n} \tau (a ^ {1}, \dots , a ^ {n}, a ^ {0}). \end{array}
$$

To prove the second property we shall only use the equality

$$
\int a \omega = \int \omega a \quad \text { for } \omega \in \Omega^ {n}, a \in \mathscr {A}.
$$

From the equality $d(ab) = (da)b + a db$ it follows that

$$
\begin{array}{r l} (d a ^ {1} \dots d a ^ {n}) a ^ {n + 1} & = \sum_ {j = 1} ^ {n} (- \mathrm{I}) ^ {n - j} d a ^ {1} \dots d (a ^ {j} a ^ {j + 1}) \dots d a ^ {n + 1} \\ & \quad + (- \mathrm{I}) ^ {n} a ^ {1} d a ^ {2} \dots d a ^ {n + 1}, \end{array}
$$

thus the second property follows from

$$
\int a ^ {n + 1} (a ^ {0} d a ^ {1} \dots d a ^ {n}) = \int (a ^ {0} d a ^ {1} \dots d a ^ {n}) a ^ {n + 1} \quad \square
$$

(Note that the cohomology of the complex $(\Omega(\mathcal{A}), d)$ is $0$ in all dimensions, including $0$ since $\Omega^0(\mathcal{A}) = \mathcal{A}$.)

Let us now recall the definition of the Hochschild cohomology groups  $\mathrm{H}^{n}(\mathcal{A},\mathcal{M})$  of A with coefficients in a bimodule M ([13]). Let  $A^{e}=A\otimes A^{0}$  be the tensor

product of $\mathcal{A}$ by the opposite algebra. Then any bimodule $\mathcal{M}$ over $\mathcal{A}$ becomes a left $\mathcal{A}^e$ module and by definition: $\mathrm{H}^n (\mathcal{A},\mathcal{M}) = \mathrm{Ext}_{\mathcal{A}^e}^n (\mathcal{A},\mathcal{M})$, where $\mathcal{A}$ is viewed as a bimodule over $\mathcal{A}$ via $a(b)c = abc$, $\forall a,b,c\in \mathcal{A}$. As in [13], one can reformulate the definition of $\mathrm{H}^n (\mathcal{A},\mathcal{M})$ using the standard resolution of the bimodule $\mathcal{A}$. One forms the complex $(\mathbf{C}^n (\mathcal{A},\mathcal{M}),b)$, where

a) $\mathbf{C}^n (\mathcal{A},\mathcal{M})$ is the space of $n$ -linear maps from $\mathcal{A}$ to $\mathcal{M}$;

b) for $\mathbf{T} \in \mathbf{C}^n(\mathcal{A}, \mathcal{M})$, $b\mathbf{T}$ is given by

$$
\begin{array}{l} (b \mathrm{T}) (a ^ {1}, \dots , a ^ {n + 1}) = a ^ {1} \mathrm{T} (a ^ {2}, \dots , a ^ {n + 1}) \\ + \sum_ {i = 1} ^ {n} (- \mathrm{I}) ^ {i} \mathrm{T} (a ^ {1}, \dots , a ^ {i} a ^ {i + 1}, \dots , a ^ {n + 1}) + (- \mathrm{I}) ^ {n + 1} \mathrm{T} (a ^ {1}, \dots , a ^ {n}) a ^ {n + 1}. \end{array}
$$

Definition 2. — The Hochschild cohomology of $\mathcal{A}$ with coefficients in $\mathcal{M}$ is the cohomology $\mathrm{H}^n (\mathcal{A},\mathcal{M})$ of the complex $(\mathbf{C}^n (\mathcal{A},\mathcal{M}),b)$.

(Note the close relation of the $\Omega^n (\mathcal{A})$ with the standard resolution and the use of the bimodules $\mathcal{A}\Omega^n (\mathcal{A})$ in the process of reduction of dimensions: see for instance [36], p. 8).

The space $\mathcal{A}^*$ of all linear functionals on $\mathcal{A}$ is a bimodule over $\mathcal{A}$ by the equality $(a\varphi b)(c) = \varphi(bca)$, for $a, b, c \in \mathcal{A}$. We consider any $\mathbf{T} \in \mathbf{C}^n(\mathcal{A}, \mathcal{A}^*)$ as an $(n + 1)$-linear functional $\tau$ on $\mathcal{A}$ by the equality

$$
\tau (a ^ {0}, a ^ {1}, \dots , a ^ {n}) = \mathrm{T} (a ^ {1}, \dots , a ^ {n}) (a ^ {0}) \quad \forall a ^ {i} \in \mathscr {A}.
$$

To the boundary bT corresponds the  $(n + 2)$ -linear functional  $b\tau$ :

$$
\begin{array}{l} (b \tau) (a ^ {0}, \dots , a ^ {n + 1}) = \tau (a ^ {0} a ^ {1}, a ^ {2}, \dots , a ^ {n + 1}) \\ + \sum_ {i = 1} ^ {n} (- I) ^ {i} \tau (a ^ {0}, \dots , a ^ {i} a ^ {i + 1}, \dots , a ^ {n + 1}) + (- I) ^ {n + 1} \tau (a ^ {n + 1} a ^ {0}, \dots , a ^ {n}). \end{array}
$$

Thus, with this notation, the condition 3) of proposition 1 becomes

$a)\tau^{\gamma} = \varepsilon (\gamma)\tau$ for any cyclic permutation $\gamma$ of $\{0,1,\dots ,n\}$;

$$
b) b \tau = 0.
$$

Now, though the Hochschild coboundary $b$ does not commute with cyclic permutations, it maps cochains satisfying $a)$ to cochains satisfying $a)$. More precisely, let $A$ be the linear map of $C^n(\mathcal{A}, \mathcal{A}^*)$ to $C^n(\mathcal{A}, \mathcal{A}^*)$ defined by

$$
(A \varphi) = \sum_ {\gamma \in \Gamma} \varepsilon (\gamma) \varphi^ {\gamma},
$$

where $\Gamma$ is the group of cyclic permutations of $\{0, 1, \ldots, n\}$. Obviously the range of A is the subspace $\mathbf{C}_{\lambda}^{n}(\mathcal{A})$ of $\mathbf{C}^{n}(\mathcal{A}, \mathcal{A}^{*})$ of cochains which satisfy $a)$. One has

Lemma 3. — $b \circ A = A \circ b'$ where $b': C^n(\mathcal{A}, \mathcal{A}^*) \to C^{n+1}(\mathcal{A}, \mathcal{A}^*)$ is defined by the equality

$$
(b ^ {\prime} \varphi) (x ^ {0}, \dots , x ^ {n + 1}) = \sum_ {j = 0} ^ {n} (- \mathrm{I}) ^ {j} \varphi (x ^ {0}, \dots , x ^ {j} x ^ {j + 1}, \dots , x ^ {n + 1}).\tag{317}
$$

Proof. — One has

$$
((\mathrm{Ab} ^ {\prime}) \varphi) (x ^ {0}, \dots , x ^ {n + 1}) = \sum (- \mathrm{I}) ^ {i + (n + 1) k} \varphi (x ^ {k}, \dots , x ^ {k + i} x ^ {k + i + 1}, \dots , x ^ {k - 1})
$$

where $\mathbf{o} \leq i \leq n, \mathbf{o} \leq k \leq n + 1$. Also

$$
\begin{array}{r l} ((b \mathrm{A}) \varphi) (x ^ {0}, \dots , x ^ {n + 1}) & = \sum_ {j = 0} ^ {n} (- \mathrm{I}) ^ {j} (\mathrm{A} \varphi) (x ^ {0}, \dots , x ^ {j} x ^ {j + 1}, \dots , x ^ {n + 1}) \\ & \quad + (- \mathrm{I}) ^ {n + 1} (\mathrm{A} \varphi) (x ^ {n + 1} x ^ {0}, \dots , x ^ {n}). \end{array}
$$

For $j \in \{0, \ldots, n\}$ one has

$$
\begin{array}{l} (A \varphi) (x ^ {0}, \dots , x ^ {j} x ^ {j + 1}, \dots , x ^ {n + 1}) = \sum_ {k = 0} ^ {j} (- I) ^ {n k} \varphi (x ^ {k}, \dots , x ^ {j} x ^ {j + 1}, \dots , x ^ {k - 1}) \\ \quad + \sum_ {k = j + 2} ^ {n + 1} (- I) ^ {n (k - 1)} \varphi (x ^ {k}, \dots , x ^ {n + 1}, x ^ {0}, \dots , x ^ {j} x ^ {j + 1}, \dots , x ^ {k - 1}). \end{array}
$$

Also,

$$
\begin{array}{r l} (\mathrm{A} \varphi) (x ^ {n + 1} x ^ {0}, \dots , x ^ {n}) & = \varphi (x ^ {n + 1} x ^ {0}, \dots , x ^ {n}) \\ & \quad + \sum_ {1} ^ {n} (- 1) ^ {j} \varphi (x ^ {j}, \dots , x ^ {n}, x ^ {n + 1} x ^ {0}, \dots , x ^ {j - 1}). \end{array}
$$

In all these terms, the $x^{j}$'s remain in cyclic order, with only two consecutive $x^{j}$'s replaced by their product. There are $(n + 1)(n + 2)$ such terms, which all appear in both $bA\varphi$ and $Ab' \varphi$. Thus we just have to check the signs in front of $T_{k,j}$ ($k \neq j + 1$) where $T_{k,j} = \varphi(x^k, \ldots, x^j x^{j+1}, \ldots, x^{k-1})$. For $Ab'$ we get $(-1)^{i+(n+1)k}$ where $i = j - k \pmod{n+2}$ and $0 \leq i \leq n$. For $bA$ we get $(-1)^{j+nk}$ if $j \geq k$ and $(-1)^{j+n(k-1)}$ if $j < k$. When $j \geq k$ one has $i = j - k$ thus the two signs agree. When $j < k$ one has $i = n + 2 - k + j$. Then as

$$
n + 2 - k + j + (n + \mathrm{i}) k = j + n (k - \mathrm{i}) \text { modulo } 2
$$

the two signs still agree. □

Corollary 4. — $(\mathbf{C}_{\lambda}^{n}(\mathcal{A}), b)$ is a subcomplex of the Hochschild complex.

We let  $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$  be the n-th cohomology group of the complex  $(\mathrm{C}_{\lambda}^{n}, b)$  and call it the cyclic cohomology of the algebra A. For n=0,  $\mathrm{H}_{\lambda}^{0}(\mathcal{A})=\mathrm{Z}_{\lambda}^{0}(\mathcal{A})$  is exactly the linear space of traces on A.

For $\mathcal{A} = \mathbf{C}$ one has $\mathrm{H}_{\lambda}^{n} = 0$ for $n$ odd but $\mathrm{H}_{\lambda}^{n} = \mathbf{C}$ for any even $n$. This example shows that the subcomplex $\mathbf{C}_{\lambda}^{n}$ is not a retraction of the complex $\mathbf{C}^n$, which for $\mathcal{A} = \mathbf{C}$ has a trivial cohomology for all $n > 0$.

To each homomorphism $\rho: \mathcal{A} \to \mathcal{B}$ corresponds a morphism of complexes: $\rho^{*}: \mathrm{C}_{\lambda}^{n}(\mathcal{B}) \to \mathrm{C}_{\lambda}^{n}(\mathcal{A})$ defined by

$$
\left(\rho^ {*} \varphi\right) \left(a ^ {0}, \dots , a ^ {n}\right) = \varphi \left(\rho \left(a ^ {0}\right), \dots , \rho \left(a ^ {n}\right)\right)
$$

and hence an induced map $\rho^{*}:\mathrm{H}_{\lambda}^{n}(\mathcal{B})\to \mathrm{H}_{\lambda}^{n}(\mathcal{A})$

318

319

Proposition 5. — 1) Any inner automorphism of $\mathcal{A}$ defines the identity morphism in $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$.

2) Assume that there exists a homomorphism $\rho: \mathcal{A} \to \mathcal{A}$ and an invertible element X of $\mathrm{M}_{2}(\mathcal{A})$ (here we suppose $\mathcal{A}$ unital) such that $\mathrm{X}\begin{bmatrix} a & 0 \\ 0 & \rho(a) \end{bmatrix} \mathrm{X}^{-1} = \begin{bmatrix} 0 & 0 \\ 0 & \rho(a) \end{bmatrix}$ for $a \in \mathcal{A}$. Then $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$ is o for all $n$.

Proof. — 1) Let $a \in \mathcal{A}$ and let $\delta$ be the corresponding inner derivation of $\mathcal{A}$ given by $\delta(x) = ax - xa$. Given $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$ let us check that $\psi$,

$$
\psi (a ^ {0}, \dots , a ^ {n}) = \sum_ {i = 0} ^ {n} \varphi (a ^ {0}, \dots , \delta (a ^ {i}), \dots , a ^ {n}),
$$

is a coboundary, i.e. that $\psi \in \mathrm{B}_{\lambda}^{n}(\mathcal{A})$. Let $\psi_0(a^0, \ldots, a^{n-1}) = \varphi(a^0, \ldots, a^{n-1}, a)$ with $a$ as above. Let us compute $b\mathrm{A}\psi_0 = \mathrm{Ab}'\psi_0$. One has:

$$
\begin{array}{r l} (b ^ {\prime} \psi_ {0}) (a ^ {0}, \dots , a ^ {n}) & = \sum_ {i = 0} ^ {n - 1} (- \mathrm{I}) ^ {i} \varphi (a ^ {0}, \dots , a ^ {i} a ^ {i + 1}, \dots , a ^ {n}, a) \\ & = (b \varphi) (a ^ {0}, \dots , a ^ {n}, a) - (- \mathrm{I}) ^ {n} \varphi (a ^ {0}, \dots , a ^ {n - 1}, a ^ {n} a) \\ & \quad - (- \mathrm{I}) ^ {n + 1} \varphi (a a ^ {0}, \dots , a ^ {n - 1}, a ^ {n}). \end{array}
$$

Since $b\varphi = 0$ by hypothesis, only the last two terms remain and one gets $Ab' \psi_0 = (-1)^n \psi$. Thus $\psi = (-1)^n Ab' \psi_0 = b((-1)^n A \psi_0) \in B_\lambda^n(\mathcal{A})$.

Now let $u$ be an invertible element of $\mathcal{A}$, let $\varphi \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$ and define $\theta(x) = uxu^{-1}$ for $x \in \mathcal{A}$. To prove that $\varphi$ and $\varphi \circ \theta$ are in the same cohomology class, one can replace $\mathcal{A}$ by $\mathrm{M}_{2}(\mathcal{A})$, $u$ by $v = \begin{bmatrix} u & 0 \\ 0 & u^{-1} \end{bmatrix}$ and $\varphi$ by $\varphi_{2}$ where, for $a^{i} \in \mathcal{A}$ and $b^{i} \in \mathrm{M}_{2}(\mathbf{C})$,

$$
\varphi_ {2} \left(a ^ {0} \otimes b ^ {0}, a ^ {1} \otimes b ^ {1}, \dots , a ^ {n} \otimes b ^ {n}\right) = \varphi \left(a ^ {0}, \dots , a ^ {n}\right) \operatorname{Trace} \left(b ^ {0} \dots b ^ {n}\right).
$$

Now $v = v_{1}v_{2}$ with $v_{1} = \begin{bmatrix} u & 0 \\ 0 & I \end{bmatrix} \begin{bmatrix} 0 & -I \\ I & 0 \end{bmatrix} \begin{bmatrix} u^{-1} & 0 \\ 0 & I \end{bmatrix}, v_{2} = \begin{bmatrix} 0 & I \\ -I & 0 \end{bmatrix}.$ One has $v_{i} = \exp a_{i}, a_{i} = \frac{\pi}{2} v_{i},$ thus the result follows from the above discussion.

2) Let $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$ and $\varphi_{2}$ be the cocycle on $M_{2}(\mathcal{A})$ defined in the proof of 1). For $a \in \mathcal{A}$, let $\alpha(a) = \begin{bmatrix} a & 0 \\ 0 & \rho(a) \end{bmatrix}$ and $\beta(a) = \begin{bmatrix} 0 & 0 \\ 0 & \rho(a) \end{bmatrix}$. By hypothesis $\alpha$ and $\beta$ are homomorphisms of $\mathcal{A}$ in $M_{2}(\mathcal{A})$ and, by 1), $\varphi_{2} \circ \alpha$ and $\varphi_{2} \circ \beta$ are in the same cohomology class. From the definition of $\varphi_{2}$ one has

$$
\begin{array}{l} \varphi_ {2} (\alpha (a ^ {0}), \dots , \alpha (a ^ {n})) = \varphi (a ^ {0}, \dots , a ^ {n}) + \varphi (\rho (a ^ {0}), \dots , \rho (a ^ {n})), \\ \varphi_ {2} (\beta (a ^ {0}), \dots , \beta (a ^ {n})) = \varphi (\rho (a ^ {0}), \dots , \rho (a ^ {n})). \quad \square \end{array}
$$

Following Karoubi-Villamayor [41], let $\mathbf{C}$ be the algebra of infinite matrices $(a_{ij})_{i,j\in \mathbb{N}}$ with $a_{ij}\in \mathbf{C}$, such that

$\alpha)$ the set of complex numbers $\{a_{ij}\}$ is finite,

$\beta)$ the number of non zero $a_{ij}$'s per line or column is bounded.

Then C satisfies condition 2) of proposition 5, taking  $\rho$  of the form

$$
\rho (a) = \operatorname{Diag} (a, 0, a, 0, \dots).
$$

The same condition is satisfied by  $A \otimes C$  for any A, thus:

Corollary 6. — For any $\mathcal{A}$ one has $\mathrm{H}_{\lambda}^{n}(\mathbf{C}\mathcal{A}) = 0$ where $\mathbf{C}\mathcal{A} = \mathbf{C} \otimes \mathcal{A}$.

We are now ready to characterize the coboundaries  $B_{\lambda}^{n} \subset Z_{\lambda}^{n}$  from the corresponding cycles, as in proposition 1. For convenience we shall also restate the characterization of  $Z_{\lambda}^{n}$ .

Definition 7. — We shall say that a cycle is vanishing when the algebra $\Omega^0$ satisfies the condition 2) of proposition 5 ([41]).

Given an $n$-dimensional cycle $(\Omega, d, \int)$ and a homomorphism $\rho: \mathcal{A} \to \Omega^0$, we shall define its character by

$$
\tau (a ^ {0}, \dots , a ^ {n}) = \int \rho (a ^ {0}) d (\rho (a ^ {1})) \dots d (\rho (a ^ {n})).
$$

Proposition 8. — Let $\tau$ be an $(n + 1)$-linear functional on $\mathcal{A}$; then

$\alpha)\tau \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$ if and only if $\tau$ is a character;

$\beta) \tau \in \mathbf{B}_{\lambda}^{n}(\mathcal{A})$ if and only if $\tau$ is the character of a vanishing cycle.

Proof. — $\alpha$ ) is just a restatement of proposition 1.

$\beta)$ For $(\Omega, d, \int)$ a vanishing cycle, one has $\mathrm{H}_{\lambda}^{n}(\Omega^{0}) = 0$, thus the character is a coboundary. Conversely if $\tau \in \mathrm{B}_{\lambda}^{n}(\mathcal{A})$, $\tau = b\psi$ for some $\psi \in \mathrm{C}_{\lambda}^{n-1}(\mathcal{A})$, one can extend $\psi$ to $\mathrm{C}\mathcal{A} = \mathrm{C} \otimes \mathcal{A}$ in an $n$-linear functional $\widetilde{\psi}$ such that

$$
\widetilde {\psi} (\mathrm{I} \otimes a ^ {0}, \dots , \mathrm{I} \otimes a ^ {n - 1}) = \psi (a ^ {0}, \dots , a ^ {n - 1}) \quad \text { for   all } a ^ {i} \in \mathscr {A},
$$

and such that $\widetilde{\psi}^{\lambda} = \varepsilon (\lambda)\widetilde{\psi}$ for any cyclic permutation $\lambda$ of $\{0,\dots ,n - 1\}$. (Take for instance $\widetilde{\psi}(b^0,\dots ,b^{n - 1}) = \psi (\alpha (b^0),\dots ,\alpha (b^{n - 1}))$ where $\alpha (b) = b_{11}\in \mathcal{A}$ for any $b = (b_{ij})\in \mathbf{C}\mathcal{A}$.) Let $\rho :\mathcal{A}\to \mathbf{C}\mathcal{A}$ be the obvious homomorphism $\rho (a) = 1\otimes a$. Then $\tau^{\prime} = b\widetilde{\psi}$ is an $n$-cocycle on $\mathbf{C}\mathcal{A}$ and $\tau = \rho^{*}\tau^{\prime}$ so that the implication $3)\Rightarrow 2)$ of proposition $\mathfrak{i}$ gives the desired result.

Let us now pass to the definition of the cup product

$$
\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) \otimes \mathrm{H} _ {\lambda} ^ {m} (\mathcal {B}) \rightarrow \mathrm{H} _ {\lambda} ^ {n + m} (\mathcal {A} \otimes \mathcal {B}).
$$

In general one does not have $\Omega(\mathcal{A} \otimes \mathcal{B}) = \Omega(\mathcal{A}) \otimes \Omega(\mathcal{B})$ (where the right hand sid is the graded tensor product of differential graded algebras) but, from the universale property of $\Omega(\mathcal{A} \otimes \mathcal{B})$, we get a natural homomorphism $\pi: \Omega(\mathcal{A} \otimes \mathcal{B}) \to \Omega(\mathcal{A}) \otimes \Omega(\mathcal{B})$.

Thus, for arbitrary cochains $\varphi \in \mathbf{C}^n (\mathcal{A},\mathcal{A}^*)$ and $\psi \in \mathbf{C}^m (\mathcal{B},\mathcal{B}^*)$, one can define the cup product $\varphi \# \psi$ by the equality

$$
(\varphi \# \psi) ^ {\wedge} = (\widehat {\varphi} \otimes \widehat {\psi}) \circ \pi .
$$

320

To become familiar with this notion, let us compute $\varphi \# \psi$ where $\varphi \in \mathbf{C}^n (\mathcal{A},\mathcal{A}^*)$ is an arbitrary cochain, and where $\psi \in \mathbf{C}^1 (\mathbf{C},\mathbf{C})$ (so that $\mathcal{B} = \mathbf{C}$) is given by $\psi (\mathrm{I},\mathrm{I}) = \mathrm{I}$. Here $\mathcal{A}\otimes \mathcal{B} = \mathcal{A}$ so that $\varphi \# \psi \in \mathbf{C}^{n + 1}(\mathcal{A},\mathcal{A}^*)$. One has

$$
(\varphi \# \psi) (a ^ {0}, \dots , a ^ {n + 1}) = (\widehat {\varphi} \otimes \widehat {\psi}) (\pi (a ^ {0} \otimes \mathrm{I}) d (a ^ {1} \otimes \mathrm{I}) \dots d (a ^ {n + 1} \otimes \mathrm{I})).
$$

One has $\pi d(a^1 \otimes \mathrm{I}) = da^1 \otimes \mathrm{I} + a^1 \otimes d\mathrm{I}$. As $\mathrm{I}^2 = \mathrm{I}$ one gets $\mathrm{I}(d\mathrm{I})\mathrm{I} = 0$ thus the only component of bidegree $(n, \mathrm{I})$ of $(\pi(a^0 \otimes \mathrm{I})d(a^1 \otimes \mathrm{I})\ldots d(a^{n+1} \otimes \mathrm{I}))$ is $(a^0 da^1\ldots da^n)a^{n+1} \otimes \mathrm{I}d\mathrm{I}$. Hence we get

$$
\varphi \# \psi = \sum_ {0} ^ {n} (- \mathrm{I}) ^ {j + n} \varphi (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}) = (- \mathrm{I}) ^ {n} b ^ {\prime} \varphi
$$

with the notation of lemma 3.

Theorem 9. — 1) The cup product $\varphi, \psi \mapsto \varphi \# \psi$ defines a homomorphism

$$
\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) \otimes \mathrm{H} _ {\lambda} ^ {m} (\mathcal {B}) \rightarrow \mathrm{H} _ {\lambda} ^ {n + m} (\mathcal {A} \otimes \mathcal {B}).
$$

2) The character of the tensor product of two cycles is the cup product of their characters.

Proof. — First, let $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$, $\psi \in Z_{\lambda}^{m}(\mathcal{B})$; then $\hat{\varphi}$ (and similarly $\hat{\psi}$) is a closed graded trace on $\Omega(\mathcal{A})$, thus $\hat{\varphi} \otimes \hat{\psi}$ is a closed graded trace on $\Omega(\mathcal{A}) \otimes \Omega(\mathcal{B})$ and $\varphi \# \psi \in Z_{\lambda}^{n+m}(\mathcal{A} \otimes \mathcal{B})$ by proposition 1.

Next, given cycles $\Omega$, $\Omega'$ and homomorphisms $\rho: \mathcal{A} \to \Omega$, $\rho': \mathcal{B} \to \Omega'$, one has a commutative triangle

![](images/page_65_image_10.jpg)

Thus 2) follows.

It remains to show that if $\varphi \in B_{\lambda}^{n}(\mathcal{A})$ then $\varphi \# \psi$ is a coboundary:

$$
\varphi \# \psi \in \mathbf {B} _ {\lambda} ^ {n + m} (\mathcal {A} \otimes \mathcal {B}).
$$

This follows from 2), proposition 8 and the trivial fact that the tensor product of any cycle with a vanishing cycle is vanishing. □

Corollary 10. — 1) H$_{\lambda}^{*}$(C) is a polynomial ring with one generator σ of degree 2.

2) Each $\mathbf{H}_{\lambda}^{*}(\mathcal{A})$ is a module over the ring $\mathbf{H}_{\lambda}^{*}(\mathbf{C})$.

Proof. — 1) It is obvious that $\mathrm{H}_{\lambda}^{n}(\mathbf{C}) = 0$ for $n$ odd and $\mathrm{H}_{\lambda}^{n}(\mathbf{C}) = \mathbf{C}$ for $n$ even. Let $e$ be the unit of $\mathbf{C}$; then any $\varphi \in \mathbb{Z}_{\lambda}^{n}(\mathbf{C})$ is characterized by $\varphi(e, \ldots, e)$. Let us

compute $\varphi \# \psi$ where $\varphi \in Z_{\lambda}^{2m}(\mathbf{C})$, $\psi \in Z_{\lambda}^{2m'}(\mathbf{C})$. Since $e$ is an idempotent one has in $\Omega(\mathbf{C})$ the equalities

$$
d e = e d e + (d e) e, \quad e (d e) e = 0, \quad e (d e) ^ {2} = (d e) ^ {2} e.
$$

Similar identities hold for $e \otimes e$ and $\pi(e \otimes e) \in \Omega(\mathbf{C}) \otimes \Omega(\mathbf{C})$ and one has

$$
\pi ((e \otimes e) d (e \otimes e) d (e \otimes e)) = e d e d e \otimes e + e \otimes e d e d e.
$$

Thus one gets $(\varphi \# \psi)(e, \ldots, e) = \frac{(m + m')!}{m! m'!} \varphi(e, \ldots, e) \psi(e, \ldots, e)$. We shall choose as generator of $\mathbf{H}_{\lambda}^{*}(\mathbf{C})$ the 2-cocycle $\sigma$

$$
\sigma (\mathrm{I}, \mathrm{I}, \mathrm{I}) = 2 i \pi .
$$

2) Let $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$. Let us check that $\sigma \# \varphi = \varphi \# \sigma$ and at the same time write an explicit formula for the corresponding map $S: H_{\lambda}^{n}(\mathcal{A}) \to H_{\lambda}^{n+2}(\mathcal{A})$.

With the notations of 1) one has

$$
\begin{array}{r l} \frac {\mathrm{I}}{2 i \pi} (\varphi \# \sigma) (a ^ {0}, \dots , a ^ {n + 2}) & = \left(\widehat {\varphi} \otimes \frac {\mathrm{I}}{2 i \pi} \widehat {\sigma}\right) (a ^ {0} \otimes e d (a ^ {1} \otimes e) \dots d (a ^ {n + 2} \otimes e)) \\ & = \widehat {\varphi} (a ^ {0} a ^ {1} a ^ {2} d a ^ {3} \dots d a ^ {n + 2}) + \widehat {\varphi} (a ^ {0} d a ^ {1} (a ^ {2} a ^ {3}) d a ^ {4} \dots d a ^ {n + 2}) + \dots \\ & \quad + \widehat {\varphi} (a ^ {0} d a ^ {1} \dots d a ^ {i - 1} (a ^ {i} a ^ {i + 1}) d a ^ {i + 2} \dots d a ^ {n + 2}) + \dots \\ & \quad + \widehat {\varphi} (a ^ {0} d a ^ {1} \dots d a ^ {n} (a ^ {n + 1} a ^ {n + 2})). \end{array}
$$

The computation of  $\sigma\#\varphi$  gives the same result.

For $\varphi \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$, let $S\varphi = \sigma \# \varphi = \varphi \# \sigma \in Z_{\lambda}^{n + 2}(\mathcal{A})$. By theorem 9 we know that $\mathrm{SB}_{\lambda}^{n}(\mathcal{A}) \subset \mathrm{B}_{\lambda}^{n + 2}(\mathcal{A})$ but we do not have a definition of S as a morphism of cochain complexes. We shall now explicitly construct such a morphism.

Recall that $\varphi \# \psi$ is already defined at the cochain level by $(\varphi \# \psi)^{\wedge} = (\widehat{\varphi} \otimes \widehat{\psi}) \circ \pi$.

Lemma 11. — For any cochain $\varphi \in \mathbf{C}_{\lambda}^{n}(\mathcal{A})$ let $\mathrm{S}\varphi \in \mathrm{C}_{\lambda}^{n + 2}(\mathcal{A})$ be defined by $\mathrm{S}\varphi = \frac{\mathrm{I}}{n + 3}\mathrm{A}(\sigma \# \varphi)$; then

a) $\frac{1}{n + 3} A(\sigma \# \varphi) = \sigma \# \varphi$ for $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$, so S extends the previously defined map.

b) $bS\varphi = \frac{n + 1}{n + 3} Sb\varphi$ for $\varphi \in C_{\lambda}^{n}(\mathcal{A})$.

Proof. — a) If $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$ then $(\sigma \# \varphi)^{\lambda} = \varepsilon (\lambda)$$\sigma \# \varphi$ for any cyclic permutation $\lambda$ of $\{0, 1, \ldots, n + 2\}$.

b) We shall leave to the reader the tedious check in the special case $\psi = \sigma$ of the equality $(bA\varphi) \# \psi = bA(\varphi \# \psi)$ for $\varphi \in C^m(\mathcal{A}, \mathcal{A}^*)$. It is based on the following explicit formula for $A(\varphi \# \sigma)$. For any subset with two elements $s = \{i, j\}$, $i < j$, of $\{0, 1, \ldots, n + 2\} = \mathbf{Z}/(n + 3)$ one defines

$$
\alpha (s) = \varphi (a ^ {0}, \dots , a ^ {i - 1}, a ^ {i} a ^ {i + 1}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 2}).
$$

In the special case $j = n + 2$ one takes

$$
\begin{array}{l l} \alpha (s) = \varphi (a ^ {n + 2} a ^ {0}, \dots , a ^ {i} a ^ {i + 1}, \dots , a ^ {n + 1}) & \text { if } i <   n + \mathrm{i}, \\ \alpha (s) = \varphi (a ^ {n + 1} a ^ {n + 2} a ^ {0}, \dots , a ^ {n}) & \text { if } i = n + \mathrm{i}. \end{array}
$$

Then one gets $\mathbf{A}(\sigma \# \varphi) = \sum_{i=1}^{1 + \operatorname{E}(n/2)} (-\operatorname{i})^{i+1}(n + 3 - 2i) \psi_i$ where, for $n$ even, one has

$$
\psi_ {i} = \alpha (\{0, i \}) + \alpha (\{\mathrm{I}, i + \mathrm{I} \}) + \dots + \alpha (\{n + 2, i - \mathrm{I} \}),
$$

and for $n$ odd

$$
\begin{array}{r l} \psi_ {i} = & \alpha (\{0, i \}) + \dots + \alpha (\{n + 2 - i, n + 2 \}) \\ & - \alpha (\{n + 2 - i + 1, 0 \}) \dots - \alpha (n + 2, i - 1 \}. \end{array}
$$

We shall end this section with the following proposition. One can show in general that, if $\varphi \in \mathbf{Z}^n (\mathcal{A},\mathcal{A}^*)$ and $\psi \in \mathbf{Z}^m (\mathcal{B},\mathcal{B}^*)$ are Hochschild cocycles, then $\varphi \# \psi$ is still a Hochschild cocycle $\varphi \# \psi \in \mathbf{Z}^{n + m}(\mathcal{A}\otimes \mathcal{B},\mathcal{A}^{*}\otimes \mathcal{B}^{*})$ and that the corresponding product of cohomology classes is related to the product v of [13], p. 216, by $[\varphi \# \psi ] = \frac{(n + m)!}{n!m!} [\varphi ]\vee [\psi ]$. Since $\sigma \in \mathbf{Z}^2 (\mathbf{C},\mathbf{C})$ is a Hochschild boundary one has:

Proposition 12. — For any cocycle $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$, $S\varphi$ is a Hochschild coboundary: $S\varphi = b\psi$ where

$$
\psi (a ^ {0}, \dots , a ^ {n + 1}) = 2 i \pi \sum_ {j = 1} ^ {n} (- 1) ^ {j} \widehat {\varphi} (a ^ {0} (d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n})).
$$

Proof. — One checks that the coboundary of the j-th term in the sum defining  $\psi$  gives

$$
\widehat {\varphi} (a ^ {0} (d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} a ^ {j + 1} (d a ^ {j + 2} \dots d a ^ {n + 2})). \quad \square
$$

## 2. Pairing of $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$ with $\mathbf{K}_i(\mathcal{A}), i = 0, \mathrm{I}$

Let $\mathcal{A}$ be a unital (non commutative) algebra and $\mathbf{K}_0(\mathcal{A})$, $\mathbf{K}_1(\mathcal{A})$ its algebraic K-theory groups (cf. [16]). By definition $\mathbf{K}_0(\mathcal{A})$ is the group associated to the semi-group of stable isomorphism classes of finite projective modules over $\mathcal{A}$. Also $\mathbf{K}_1(\mathcal{A})$ is the quotient of the group $\mathrm{GL}_{\infty}(\mathcal{A})$ by its commutator subgroup, where $\mathrm{GL}_{\infty}(\mathcal{A})$ is the inductive limit of the groups $\mathrm{GL}_n(\mathcal{A})$ of invertible elements of $\mathbf{M}_n(\mathcal{A})$, under the maps $x \to \begin{bmatrix} x & 0 \\ 0 & 1 \end{bmatrix}$.

In this section we shall define by straightforward formulae a pairing between  $\mathrm{H}_{\lambda}^{\mathrm{ev}}(\mathcal{A})$  and  $\mathrm{K}_{0}(\mathcal{A})$  and between  $\mathrm{H}_{\lambda}^{\mathrm{odd}}(\mathcal{A})$  and  $\mathrm{K}_{1}(\mathcal{A})$ .

The pairing satisfies $\langle \mathbf{S}\varphi, e \rangle = \langle \varphi, e \rangle$, for $\varphi \in \mathrm{H}_{\lambda}^{*}(\mathcal{A})$, $e \in \mathbf{K}(\mathcal{A})$ and hence is in fact defined on $\mathrm{H}^{*}(\mathcal{A}) = \mathrm{H}_{\lambda}^{*}(\mathcal{A}) \otimes_{\mathrm{H}_{\lambda}^{*}(\mathbb{C})} \mathbf{C}$. As a computational device we shall

also formulate the pairing in terms of connexions and curvature as one does for the usual Chern character for smooth manifolds.

This will show the Morita invariance of  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$  and will give in the case A abelian, an action of the ring  $\mathrm{K}_{0}(\mathcal{A})$  on  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$ .

Lemma 13. — Let $\varphi \in Z_{\lambda}^{n}(\mathcal{A})$ and $p, q \in \operatorname{Proj} M_{k}(\mathcal{A})$ be two idempotents of the form $p = uv$, $q = vu$ for some $u, v \in M_{k}(\mathcal{A})$. Then the following cocycles on $\mathcal{B} = \{x \in M_{k}(\mathcal{A}), xp = px = x\}$ differ by a coboundary

$$
\psi_ {1} (a ^ {0}, \dots , a ^ {n}) = (\varphi \# \operatorname{Tr}) (a ^ {0}, \dots , a ^ {n}),
$$

$$
\psi_ {2} (a ^ {0}, \dots , a ^ {n}) = (\varphi \# \operatorname{Tr}) (v a ^ {0} u, \dots , v a ^ {n} u).
$$

Proof. — First, replacing $\mathcal{A}$ by $\mathrm{M}_k(\mathcal{A})$ one may assume that $k = 1$. Then one can replace $p, q, u, v$ by $\begin{bmatrix} p & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 0 & q \end{bmatrix}, \begin{bmatrix} 0 & u \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ v & 0 \end{bmatrix}$ and hence assume the existence of an invertible element $U$ such that $UpU^{-1} = q$, $u = pU^{-1} = U^{-1}q$, $v = qU = Up$ (take $U = \begin{bmatrix} I - p & u \\ v & I - q \end{bmatrix}$). Then the result follows from proposition 5.1. $\square$

Recall that an equivalent description of  $\mathrm{K}_{0}(\mathcal{A})$  is as the abelian group associated to the semi-group of stable equivalence classes of idempotents  $e \in \operatorname{Proj} \mathrm{M}_{k}(\mathcal{A})$ .

Proposition 14. — a) The following equality defines a bilinear pairing between $\mathbf{K}_{0}(\mathcal{A})$ and $\mathrm{H}_{\lambda}^{\mathrm{ev}}(\mathcal{A})$: $\langle [e], [\varphi] \rangle = (2i\pi)^{-m}(m!)^{-1} (\varphi \# \operatorname{Tr})(e, \ldots, e)$ for $e \in \operatorname{Proj} \mathbf{M}_{k}(\mathcal{A})$ an $\varphi \in \mathbf{Z}_{\lambda}^{2m}(\mathcal{A})$.

b) One has $\langle [e], [S\varphi] \rangle = \langle [e], [\varphi] \rangle$.

Proof. — First if $\varphi \in \mathbf{B}_{\lambda}^{2m}(\mathcal{A})$, $\varphi \# \operatorname{Tr}$ is also a coboundary, $\varphi \# \operatorname{Tr} = b\psi$ and hence $(\varphi \# \operatorname{Tr})(e, \ldots, e) = b\psi(e, \ldots, e) = \sum_{i=0}^{2m} (-1)^i \psi(e, \ldots, e) = \psi(e, \ldots, e) = 0$, since $\psi^\lambda = -\psi$. This together with lemma 13 shows that $(\varphi \# \operatorname{Tr})(e, \ldots, e)$ only depends on the equivalence class of $e$. Since replacing $e$ by $\begin{bmatrix} e & 0 \\ 0 & 0 \end{bmatrix}$ does not change the result, one gets the additivity and hence $a$).

b) One has $\frac{1}{2i\pi}\mathrm{S}\varphi(e,\ldots,e)=\sum_{j=1}^{2m}\hat{\varphi}(e(de)^{j-1}e(de)^{n-j+1})$ and, since $e^2=e$, one has $e(de)e=0$, $e(de)^{2}=(de)^{2}e$, so that

$$
\frac {\mathrm{I}}{2 i \pi} \mathrm{S} \varphi (e, \dots , e) = (m + \mathrm{I}) \varphi (e, \dots , e). \quad \square
$$

We shall now describe the odd case.

Proposition 15. — a) The following equality defines a bilinear pairing between $\mathbf{K}_{1}(\mathcal{A})$ and $\mathrm{H}_{\lambda}^{\mathrm{odd}}(\mathcal{A})$:

$$
\begin{array}{r l} \langle [ u ], [ \varphi ] \rangle & = (2 i \pi) ^ {- m} 2 ^ {- (2 m + 1)} \frac {\mathrm{I}}{(m - \mathrm{I} / 2) \dots \mathrm{I} / 2} \\ & (\varphi \# \operatorname{Tr}) (u ^ {- 1} - \mathrm{I}, u - \mathrm{I}, u ^ {- 1} - \mathrm{I}, \dots , u - \mathrm{I}) \end{array}
$$

where $\varphi \in \mathbf{Z}_{\lambda}^{2m - 1}(\mathcal{A})$ and $u\in \mathrm{GL}_k(\mathcal{A})$

b) One has $\langle [u], [S\varphi] \rangle = \langle [u], [\varphi] \rangle$.

Proof. — a) Let $\widetilde{\mathcal{A}}$ be the algebra obtained from $\mathcal{A}$ by adjoining a unit. Since $\mathcal{A}$ is already unital, $\widetilde{\mathcal{A}}$ is isomorphic to the product of $\mathcal{A}$ by $\mathbf{C}$, by means of the homomorphism $\rho: (a, \lambda) \to (a + \lambda\mathrm{I}, \lambda)$ of $\widetilde{\mathcal{A}}$ to $\mathcal{A} \times \mathbf{C}$. Let $\widetilde{\varphi} \in Z_{\lambda}^{n}(\widetilde{\mathcal{A}})$ be defined by the equality

$$
\widetilde {\varphi} ((a ^ {0}, \lambda^ {0}), \dots , (a ^ {n}, \lambda^ {n})) = \varphi (a ^ {0}, \dots , a ^ {n}), \quad \forall (a ^ {i}, \lambda^ {i}) \in \widetilde {\mathcal {A}}.
$$

Let us check that $b\widetilde{\varphi} = 0$. For $(a^0, \lambda^0), \ldots, (a^{n+1}, \lambda^{n+1}) \in \widetilde{\mathcal{A}}$ one has

$$
\begin{array}{r l} \widetilde {\varphi} ((a ^ {0}, \lambda^ {0}), \dots , (a ^ {i}, \lambda^ {i}) (a ^ {i + 1}, \lambda^ {i + 1}), \dots , (a ^ {n + 1}, \lambda^ {n + 1})) \\ & = \varphi (a ^ {0}, \dots , a ^ {i} a ^ {i + 1}, \dots , a ^ {n + 1}) + \lambda^ {i} \varphi (a ^ {0}, \dots , a ^ {i - 1}, a ^ {i + 1}, \dots , a ^ {n + 1}) \\ & \qquad + \lambda^ {i + 1} \varphi (a ^ {0}, \dots , a ^ {i}, a ^ {i + 2}, \dots , a ^ {n + 1}). \end{array}
$$

Thus

$$
\begin{array}{r l} b \widetilde {\varphi} ((a ^ {0}, \lambda^ {0}), \dots , (a ^ {n + 1}, \lambda^ {n + 1})) \\ & = \lambda^ {0} \varphi (a ^ {1}, \dots , a ^ {n + 1}) + (- \mathrm{i}) ^ {n - 1} \lambda^ {0} \varphi (a ^ {n + 1}, a ^ {1}, \dots a ^ {n}) = 0. \end{array}
$$

Now for $u\in \mathbf{GL}_1(\mathcal{A})$ one has

$$
\varphi \left(u ^ {- 1} - \mathrm{I}, u - \mathrm{I}, \dots , u ^ {- 1} - \mathrm{I}, u - \mathrm{I}\right) = (\widetilde {\varphi} \circ \rho^ {- 1}) (\bar {u} ^ {- 1}, \bar {u}, \dots , \bar {u} ^ {- 1}, \bar {u})
$$

where $\bar{u} = (u, \mathbf{i}) \in \mathcal{A} \times \mathbf{C}$. Thus to show that this function $\chi(u)$ satisfies

$$
\chi (u v) = \chi (u) + \chi (v) \quad \text { for } u, v \in \mathrm{GL} _ {1} (\mathscr {A}),
$$

one can assume that $\varphi(\mathfrak{I}, a^0, \ldots, a^{n-1}) = 0$ for $a^i \in \mathcal{A}$, and replace $\chi$ by

$$
\chi (u) = \varphi (u ^ {- 1}, u, \dots , u ^ {- 1}, u).
$$

Now one has with $\mathbf{U} = \begin{bmatrix} uv & 0 \\ 0 & \mathrm{I} \end{bmatrix}$, $\mathbf{V} = \begin{bmatrix} u & 0 \\ 0 & v \end{bmatrix}$

$$
\chi (u v) = (\varphi \# \operatorname{Tr}) (\mathrm{U} ^ {- 1}, \mathrm{U}, \dots , \mathrm{U} ^ {- 1}, \mathrm{U}),
$$

$$
\chi (u) + \chi (v) = (\varphi \# \operatorname{Tr}) (\mathrm{V} ^ {- 1}, \mathrm{V}, \dots , \mathrm{V} ^ {- 1}, \mathrm{V}).
$$

Since U is connected to V by the smooth path

$$
\mathbf {U} _ {t} = \left[ \begin{array}{c c} u & \mathrm{o} \\ \mathrm{o} & \mathrm{i} \end{array} \right] \left[ \begin{array}{c c} \sin t & - \cos t \\ \cos t & \sin t \end{array} \right] \left[ \begin{array}{c c} \mathrm{i} & \mathrm{o} \\ \mathrm{o} & v \end{array} \right] \left[ \begin{array}{c c} \sin t & \cos t \\ - \cos t & \sin t \end{array} \right]
$$

it is enough to check that

$$
\frac {d}{d t} (\varphi \# \operatorname{Tr}) \left(\mathrm{U} _ {t} ^ {- 1}, \mathrm{U} _ {t}, \dots , \mathrm{U} _ {t}\right) = 0.
$$

Using $(\mathbf{U}_t^{-1})' = -\mathbf{U}_t^{-1}\mathbf{U}_t'\mathbf{U}_t^{-1}$ the desired equality follows easily. We have shown that the right hand side of 15 a) defines a homomorphism of $\mathbf{GL}_k(\mathcal{A})$ to $\mathbf{C}$. The compatibility with the inclusion $\mathbf{GL}_k \subset \mathbf{GL}_{k'}$ is obvious.

To show that the result is o if $\varphi$ is a coboundary, one may assume that $k = 1$, and, using the above argument, that $\varphi = b\psi$ where $\psi \in \mathbf{C}_{\lambda}^{n-1}$, $\psi(1, a^0, \ldots, a^{n-2}) = 0$ for $a^i \in \mathcal{A}$. (One has $b\widetilde{\psi} = (b\psi)^{\sim}$ for $\psi \in \mathbf{C}_{\lambda}^{n-1}$.) Then one gets $b\psi(u^{-1}, \ldots, u^{-1}, u) = 0$. b) The proof is left to the reader. $\square$

$$
\text { Definition   16. } - \text { Let } \mathrm{H} ^ {*} (\mathcal {A}) = \mathrm{H} _ {\lambda} ^ {*} (\mathcal {A}) \otimes_ {\mathrm{H} _ {\lambda} ^ {*} (\mathbf {C})} \mathbf {C}.
$$

Here  $H_{\lambda}^{*}(\mathbf{C})$ , which by corollary 10 1) is identified with a polynomial ring  $C[\sigma]$ , acts on C by  $\mathbf{P}(\sigma)\mapsto\mathbf{P}(\mathbf{i})$ . This homomorphism of  $H_{\lambda}^{*}(\mathbf{C})$  to C is the pairing given by proposition 14 with the generator of  $\mathbf{K}_{0}(\mathbf{C})=\mathbf{Z}$ .

By construction $\mathbf{H}^*(\mathcal{A})$ is the inductive limit of the groups $\mathbf{H}_{\lambda}^{n}(\mathcal{A})$ under the map $\mathbf{S}:\mathbf{H}_{\lambda}^{n}(\mathcal{A})\to \mathbf{H}_{\lambda}^{n + 2}(\mathcal{A})$, or equivalently the quotient of $\mathbf{H}_i^* (\mathcal{A})$ by the equivalence relation $\varphi \sim \mathrm{S}\varphi$. As such, it inherits a natural $\mathbf{Z} / 2$ grading and a filtration:

$$
\mathrm{F} ^ {n} \mathrm{H} ^ {*} (\mathcal {A}) = \operatorname{Im} \mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}).
$$

We shall come back to this filtration in section 4.

Corollary 17. — One has a canonical pairing between $\mathbf{H}^{\mathrm{ev}}(\mathcal{A})$ and $\mathbf{K}_0(\mathcal{A})$, and between $\mathbf{H}^{\mathrm{odd}}(\mathcal{A})$ and $\mathbf{K}_1(\mathcal{A})$.

The following notion will be important both in explicit computations of the above pairing (this is already clear in the case  $\mathcal{A} = \mathrm{C}^{\infty}(\mathrm{V})$ , V a smooth manifold) and in the discussion of Morita equivalences.

Definition 18. — Let $\mathcal{A} \xrightarrow{\circ} \Omega$ be a cycle over $\mathcal{A}$, and $\mathcal{E}$ a finite projective module over $\mathcal{A}$. Then a connexion $\nabla$ on $\mathcal{E}$ is a linear map $\nabla: \mathcal{E} \to \mathcal{E} \otimes_{\mathcal{A}} \Omega^1$ such that

$$
\nabla (\xi . x) = (\nabla \xi) x + \xi \otimes d \rho (x), \quad \forall \xi \in \mathcal {E}, x \in \mathcal {A}.
$$

Here $\mathcal{E}$ is a right module over $\mathcal{A}$ and $\Omega^1$ is considered as a bimodule over $\mathcal{A}$ using the homomorphism $\rho: \mathcal{A} \to \Omega^0$ and the ring structure of $\Omega^*$. Let us list a number of obvious properties:

Proposition 19. — a) Let $e \in \operatorname{End}_{\mathcal{A}}(\mathcal{E})$ be an idempotent and $\nabla$ a connexion on $\mathcal{E}$; then $\xi \to (e \otimes \mathrm{I}) \nabla \xi$ is a connexion on $e\mathcal{E}$.

b) Any finite projective module $\mathcal{E}$ admits a connexion.

c) The space of connexions is an affine space over the vector space $\operatorname{Hom}_{\mathcal{A}}(\mathcal{E}, \mathcal{E} \otimes_{\mathcal{A}} \Omega^1)$.

d) Any connexion $\nabla$ extends uniquely to a linear map of $\widetilde{\mathcal{E}} = \mathcal{E} \otimes_{\mathcal{A}} \Omega$ into itself such that

$$
\nabla (\xi \otimes \omega) = (\nabla \xi) \omega + \xi \otimes d \omega , \quad \forall \xi \in \mathscr {E}, \omega \in \Omega .
$$

Proof. — a) One multiplies the equality 18 by $e \otimes \mathbf{i}$ (on the left).

b) By a) one can assume that $\mathcal{E} = \mathbf{C}^k\otimes \mathcal{A}$ for some $k$. Then, with $(\xi_i)_{i = 1,\dots ,k}$ the canonical basis of $\mathcal{E}$, put

$$
\nabla (\Sigma \xi_ {i} a _ {i}) = \Sigma \xi_ {i} \otimes d \rho (a _ {i}) \in \mathcal {E} \otimes_ {\mathscr {A}} \Omega^ {1}.
$$

Note that, if $k = \mathfrak{I}$ (for instance), then $\mathcal{A} \otimes_{\mathcal{A}} \Omega^1 = \rho(\mathfrak{I}) \Omega^1$ and $\nabla a = \rho(\mathfrak{I}) d\rho(a)$ for any $a \in \mathcal{A}$ since $\mathcal{A}$ is unital. This differs in general from $d$, even when $\rho(\mathfrak{I})$ is the unit of $\Omega^0$.

c) Immediate.

d) By construction $\mathcal{E}$ is the finite projective module over $\Omega$ induced by the homomorphism $\rho$. The uniqueness statement is obvious since $\nabla\xi$ is already defined for $\xi\in\mathcal{E}$. The existence follows from the equality

$$
\text { for   any } \xi \in \mathcal {E}, a \in \mathcal {A} \text { and } \omega \in \Omega .
$$

We shall now construct a cycle over $\operatorname{End}_{\mathcal{A}}(\mathcal{E})$. We start with the graded algebra $\operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$ (where $T$ is of degree $k$ if $T\widetilde{\mathcal{E}}^j\subset \widetilde{\mathcal{E}}^{j + k}$ for all $j$). For any $T\in \operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$ of degree $k$ we let $\delta (T) = \nabla T - (-1)^{k}\mathrm{T}\nabla$. By the equality $d$ one gets

$$
\nabla (\xi \omega) = (\nabla \xi) \omega + (- 1) ^ {\deg} \xi d \omega \quad \text { for } \xi \in \widetilde {\mathcal {E}}, \omega \in \Omega ,
$$

and hence that $\delta(T) \in \operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$, and is of degree $k + 1$. By construction $\delta$ is a graded derivation of $\operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$. Next, since $\widetilde{\mathcal{E}}$ is a finite projective module, the graded trace $\int: \Omega^n \to \mathbf{C}$ defines a trace, which we shall still denote by $\int$, on the graded algebra $\operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$.

$$
\text { Lemma   20. } - \text { One   has } \int \delta (\mathrm{T}) = 0 \text { for   any } \mathrm{T} \in \operatorname{End} _ {\Omega} (\widetilde {\mathcal {E}}) \text { of   degree } n - 1.
$$

Proof. — First, if we replace the connexion $\nabla$ by $\nabla' = \nabla + \Gamma$, where $\Gamma \in \operatorname{Hom}_{\mathcal{A}}(\mathcal{E}, \mathcal{E} \otimes_{\mathcal{A}} \Omega^1)$, the corresponding extension to $\widetilde{\mathcal{E}}$ is $\nabla' = \nabla + \widetilde{\Gamma}$, where $\widetilde{\Gamma} \in \operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$ and is of degree 1. Thus it is enough to prove the lemma for some connexion on $\mathcal{E}$. Hence we can assume that $\mathcal{E} = e\mathcal{A}^k$ for some $e \in \operatorname{Proj} M_k(\mathcal{A})$ and that $\nabla$ is given by 19 a) from a connexion $\nabla_0$ on $\mathcal{A}^k$. Then using the equality $\delta(T) = e \delta_0(T)e$ for $T \in \operatorname{End} \widetilde{\mathcal{E}} \subset \operatorname{End} \widetilde{\mathcal{E}}_0$ ($\mathcal{E}_0 = \mathcal{A}^k$), as well as

$$
\delta_ {0} (\mathbf {T}) = \delta_ {0} (e \mathbf {T} e) = \delta_ {0} (e) \mathbf {T} + \delta (\mathbf {T}) + (- \mathrm{i}) ^ {\partial \mathbf {T}} \mathbf {T} \delta_ {0} (e),
$$

one is reduced to the case $\mathcal{E} = \mathcal{A}^k$, with $\nabla$ given by 19 b). Let us end the computation say with $k = 1$. Let $e = \rho(1)$. One has $\widetilde{\mathcal{E}} = e\Omega$, $\operatorname{End}_{\Omega}(\widetilde{\mathcal{E}}) = e\Omega e$, $\delta(a) = e(da)e$. Thus $\int \delta(a) = \int (d(eae) - (de)a - (-1)^{\partial a}ade) = 0$. $\square$

Now we do not yet have a cycle over  $\operatorname{End}_{\mathcal{A}}(\mathcal{E})$  by taking the obvious homomorphism of  $\operatorname{End}_{\mathcal{A}}(\mathcal{E})$  in  $\operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$ , the differential  $\delta$  and the integral  $\int$ . In fact the crucial property  $\delta^{2}=0$  is not satisfied:

Proposition 21. — a) The map $\theta = \nabla^{2}$ of $\widetilde{\mathcal{E}}$ to $\widetilde{\mathcal{E}}$ is an endomorphism: $\theta \in \operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$ and $\delta^{2}(\mathrm{T}) = \theta \mathrm{T} - \mathrm{T}\theta$ for all $\mathrm{T} \in \operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$.

b) One has $\langle [\mathcal{E}], [\tau] \rangle = \frac{1}{m!} \int (\theta / 2\pi i)^m$, when $n$ is even, $n = 2m$, where $[\mathcal{E}] \in \mathrm{K}_0(\mathcal{A})$ is the class of $\mathcal{E}$, and $\tau$ is the character of $\Omega$.

Proof. — a) One uses the rules $\nabla(\eta\omega) = (\nabla\eta)\omega + (-1)^{\deg\eta}\eta d\omega$ and $d^{2} = 0$ to check that $\nabla^{2}(\eta\omega) = \nabla^{2}(\eta)\omega$.

b) Let us show that $\int \theta^{m}$ is independent of the choice of the connexion $\nabla$. The result is then easily checked by taking on $\mathcal{E} = e\mathcal{A}^{k}$ the connexion of proposition 19. Thus let $\nabla' = \nabla + \Gamma$ where $\Gamma$ is an endomorphism of degree 1 of $\widetilde{\mathcal{E}}$. It is enough to check that the derivative of $\int \theta_{t}^{m}$ is 0 where $\theta_{t}$ corresponds to $\nabla_{t} = \nabla + t\Gamma$. Also it is enough to do it for $t = 0$. We get:

$$
d / d t \int \theta_ {t} ^ {m} = \sum_ {k = 0} ^ {m - 1} \int \theta_ {t} ^ {k} \left(\frac {d}{d t} \theta_ {t}\right) \theta_ {t} ^ {m - k - 1}.
$$

As $\left(\frac{d}{dt}\theta_t\right)_{t = 0} = \Gamma \nabla +\nabla \Gamma = \delta (\Gamma)$ one has

$$
\left((d / d t) \int \theta_ {t} ^ {m}\right) _ {t = 0} = m \int \delta (\theta^ {m - 1} \Gamma) = 0. \quad \square
$$

Thus, while $\delta^2 \neq 0$, there exists $\theta \in \Omega' = \operatorname{End}_{\Omega}(\widetilde{\mathcal{E}})$ such that

$$
\delta^ {2} (\mathrm{T}) = \theta \mathrm{T} - \mathrm{T} \theta , \quad \forall \mathrm{T} \in \Omega^ {\prime}.
$$

We shall now construct a cycle from the quadruple $(\Omega', \delta, \theta, \int)$.

Lemma 22. — Let $\left(\Omega', \delta, \theta, \int\right)$ be a quadruple such that $\Omega'$ is a graded algebra, $\delta$ a graded derivation of degree 1 of $\Omega'$ and $\theta \in \Omega'^{2}$ satisfies

$$
\delta (\theta) = 0 \quad a n d \quad \delta^ {2} (\omega) = \theta \omega - \omega \theta \quad f o r \omega \in \Omega^ {\prime}.
$$

Then one constructs canonically a cycle by adjoining to $\Omega'$ an element X of degree 1 with $d\mathbf{X} = 0$, such that $\mathbf{X}^2 = \theta$, $\omega_1\mathbf{X}\omega_2 = 0$, $\forall \omega_i \in \Omega'$.

Proof. — Let $\Omega''$ be the graded algebra obtained by adjoining X. Any element of $\Omega''$ has the form $\omega = \omega_{11} + \omega_{12}X + X\omega_{21} + X\omega_{22}X,\ \omega_{ij} \in \Omega'$. Thus, as a vector space, $\Omega''$ coincides with $M_2(\Omega')$, the product is such that

$$
\left[ \begin{array}{c c} \omega_ {1 1} ^ {\prime \prime} & \omega_ {1 2} ^ {\prime \prime} \\ \omega_ {2 1} ^ {\prime \prime} & \omega_ {2 2} ^ {\prime \prime} \end{array} \right] = \left[ \begin{array}{c c} \omega_ {1 1} & \omega_ {1 2} \\ \omega_ {2 1} & \omega_ {2 2} \end{array} \right] \left[ \begin{array}{c c} \mathrm{I} & \mathrm{O} \\ \mathrm{O} & \theta \end{array} \right] \left[ \begin{array}{c c} \omega_ {1 1} ^ {\prime} & \omega_ {1 2} ^ {\prime} \\ \omega_ {2 1} ^ {\prime} & \omega_ {2 2} ^ {\prime} \end{array} \right]
$$

328

and the grading is obtained by considering X as an element of degree 1; thus $[\omega_{ij}]$ is of degree $k$ when $\omega_{11}$ is of degree $k$, $\omega_{12}$ and $\omega_{21}$ of degree $k - 1$ and $\omega_{22}$ of degree $k - 2$. One checks easily that $\Omega''$ is a graded algebra containing $\Omega'$. The differential $d$ is given by the conditions $d\omega = \delta(\omega) + X\omega - (-1)^{\deg \omega} \omega X$ for $\omega \in \Omega' \subset \Omega''$, and $dX = 0$. One gets

$$
\begin{array}{r l} d \left[ \begin{array}{l l} \omega_ {1 1} & \omega_ {1 2} \\ \omega_ {2 1} & \omega_ {2 2} \end{array} \right] = & \left[ \begin{array}{c c} \delta (\omega_ {1 1}) & \delta (\omega_ {1 2}) \\ - \delta (\omega_ {2 1}) & - \delta (\omega_ {2 2}) \end{array} \right] + \left[ \begin{array}{c c} 0 & - \theta \\ I & 0 \end{array} \right] \left[ \begin{array}{l l} \omega_ {1 1} & \omega_ {1 2} \\ \omega_ {2 1} & \omega_ {2 2} \end{array} \right] \\ & - (- I) ^ {\deg \omega} \left[ \begin{array}{l l} \omega_ {1 1} & \omega_ {1 2} \\ \omega_ {2 1} & \omega_ {2 2} \end{array} \right] \left[ \begin{array}{l l} 0 & I \\ - \theta & 0 \end{array} \right]. \end{array}
$$

One checks that the two terms on the right define graded derivations of $\Omega''$ and that $d^2 = 0$.

Finally one checks that the equality

$$
\int \left(\omega_ {1 1} + \omega_ {1 2} X + X \omega_ {2 1} + X \omega_ {2 2} X\right) = \int \omega_ {1 1} - (- I) ^ {\deg \omega} \int \omega_ {2 2} \theta .
$$

defines a closed graded trace. $\square$

Putting together proposition 21 a) and lemma 22 we get:

Corollary 23. — Let $\mathcal{A} \xrightarrow{\circ} \Omega$ be a cycle over $\mathcal{A}$, $\mathcal{E}$ a finite projective module over $\mathcal{A}$ and $\mathcal{A}' = \operatorname{End}_{\mathcal{A}}(\mathcal{E})$. To each connexion $\nabla$ on $\mathcal{E}$ corresponds canonically a cycle $\mathcal{A}' \xrightarrow{\circ'} \Omega'$ over $\mathcal{A}'$.

One can show that the character $\tau' \in Z_{\lambda}^{n}(\mathcal{A}')$ of this new cycle has a class $[\tau'] \in H_{\lambda}^{n}(\mathcal{A}')$ independent of the choice of the connexion $\nabla$, which coincides with the class given by lemma 13. One can then easily check a reciprocity formula which takes care of the Morita equivalence.

Corollary 24. — Let $\mathcal{A}$, $\mathcal{B}$ be unital algebras and $\mathcal{E}$ an $\mathcal{A}$, $\mathcal{B}$ bimodule, finite projective on both sides, with $\mathcal{A} = \operatorname{End}_{\mathrm{B}}(\mathcal{E})$, $\mathcal{B} = \operatorname{End}_{\mathcal{A}}(\mathcal{E})$. Then $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$ is canonically isomorphic to $\mathrm{H}_{\lambda}^{*}(\mathcal{B})$.

Finally when $\mathcal{A}$ is abelian, and one is given a finite projective module $\mathcal{E}$ over $\mathcal{A}$, then one has an obvious homomorphism of $\mathcal{A}$ to $\mathcal{A}' = \operatorname{End}_{\mathcal{A}}(\mathcal{E})$. Thus in this case, by restriction to $\mathcal{A}$ of the cycle of corollary 23 one gets:

Corollary 25. — When $\mathcal{A}$ is abelian, $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$ is in a natural manner a module over the ring $\mathrm{K}_{0}(\mathcal{A})$.

To give some meaning to this statement we shall compute an example. We let V be a compact oriented smooth manifold. Let  $\mathcal{A} = \mathrm{C}^{\infty}(\mathrm{V})$  and  $\Omega$  be the cycle over A given by the ordinary de Rham complex and integration of forms of degree n. Let E be a complex vector bundle over V and  $\mathcal{E} = \mathrm{C}^{\infty}(\mathrm{V}, \mathrm{E})$  the corresponding finite

projective module over  $\mathcal{A} = \mathbf{C}^{\infty}(\mathbf{V})$ . Then the notion of connexion given by definition 18 coincides with the usual notion.

Thus corollary 25 yields a new cocycle $\tau \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$, $\mathcal{A} = \mathbf{C}^{\infty}(\mathbf{V})$, canonically associated to $\nabla$. We shall leave as an exercise the following proposition.

Proposition 26. — Let $\omega_{k}$ be the differential form of degree $2k$ on V which gives the component of degree $2k$ of the Chern character of the bundle E with connexion $\nabla: \omega_{k} = 1/k!$ Trace $\left(\frac{\theta}{2\pi i}\right)^{k}$, where $\theta$ is the curvature form ([17]). Then one has the equality

$$
\tau = \Sigma \mathrm{S} ^ {k} \widetilde {\omega} _ {k},
$$

where $\widetilde{\omega}_k\in \mathbf{Z}_{\lambda}^{n - 2k}(\mathcal{A})$ is given by

$$
\widetilde {\omega} _ {k} \left(f ^ {0}, \dots , f ^ {n - 2 k}\right) = \int f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {n - 2 k} \wedge \omega_ {k}, \quad \forall f ^ {i} \in \mathscr {A} = \mathrm{C} ^ {\infty} (\mathrm{V}),
$$

and where $\tau$ is the restriction to $\mathcal{A} = \mathrm{C}^{\infty}(\mathrm{V})$ of the character of the cycle associated to the bundle E, the connexion $\nabla$, and the de Rham cycle of $\mathcal{A}$ by corollary 23.

## 3. Cobordism of cycles and the operator B

By a chain of dimension $n + \mathfrak{i}$ we shall mean a triple $(\Omega, \partial \Omega, \int)$ where $\Omega$ and $\partial \Omega$ are differential graded algebras of dimensions $n + \mathfrak{i}$ and $n$ with a given surjective morphism $r: \Omega \to \partial \Omega$ of degree 0, and where $\int: \Omega^{n+1} \to \mathbf{C}$ is a graded trace such that

$$
\int d \omega = 0, \quad \forall \omega \in \Omega^ {n} \quad \text { such   that } r (\omega) = 0.
$$

By the boundary of such a chain we mean the cycle  $\left(\partial\Omega,\int^{\prime}\right)$  where for  $\omega^{\prime}\in(\partial\Omega)^{n}$  one takes  $\int^{\prime}\omega^{\prime}=\int d\omega$  for any  $\omega\in\Omega^{n}$  with  $r(\omega)=\omega^{\prime}$ . One easily checks, using the surjectivity of r, that  $\int^{\prime}$  is a graded trace on  $\partial\Omega$  which is closed by construction.

Definition 27. — Let $\mathcal{A}$ be an algebra, and let $\mathcal{A} \xrightarrow{\rho} \Omega$, $\mathcal{A} \xrightarrow{\rho'} \Omega'$ be two cycles over $\mathcal{A}$ (cf. proposition 1). We shall say that these cycles are cobordant (over $\mathcal{A}$) if there exists a chain $\Omega''$ with boundary $\Omega \oplus \widetilde{\Omega}'$ (where $\widetilde{\Omega}'$ is obtained from $\Omega'$ by changing the sign of $\int$) and a homomorphism $\rho'': \mathcal{A} \to \Omega''$ such that $r \circ \rho'' = (\rho, \rho')$.

Using a fibered product of algebras one checks that the relation of cobordism is transitive. It is obviously symmetric. Let us check that any cycle over $\mathcal{A}$ is cobordant to itself. Let $\Omega^0 = \mathbf{C}^\infty([0,1])$, $\Omega^1$ be the space of $\mathbf{C}^\infty$ 1-forms on $[0,1]$, and $d$ be the usual differential. Set $\partial \Omega = \mathbf{C} \oplus \mathbf{C}$ and take $\int$ to be the usual integral. Then taking for $r$ the restriction of functions to the boundary, one gets a chain of dimension 1 with boundary $(\mathbf{C} \oplus \mathbf{C}, \varphi)$, $\varphi(a, b) = a - b$. Tensoring a given cycle over $\mathcal{A}$ by the above chain gives the desired cobordism.

Thus cobordism is an equivalence relation. The main result of this section is a precise description of its meaning for the characters of the cycles. We shall assume throughout that the algebra A is unital.

Lemma 28. — Let $\tau_{1}, \tau_{2}$ be the characters of two cobordant cycles over $\mathcal{A}$. Then there exists a Hochschild cocycle $\varphi \in Z^{n+1}(\mathcal{A}, \mathcal{A}^{*})$ such that $\tau_{1} - \tau_{2} = B_{0} \varphi$, where

$$
\left(\mathrm{B} _ {0} \varphi\right) \left(a ^ {0}, \dots , a ^ {n}\right) = \varphi (\mathrm{I}, a ^ {0}, \dots , a ^ {n}) - (- \mathrm{I}) ^ {n + 1} \varphi \left(a ^ {0}, \dots , a ^ {n}, \mathrm{I}\right).
$$

Proof. — With the notation of definition 27, let

$$
\varphi (a ^ {0}, \dots , a ^ {n + 1}) = \int \rho^ {\prime \prime} (a ^ {0}) d \rho^ {\prime \prime} (a ^ {1}) \dots d \rho^ {\prime \prime} (a ^ {n + 1}), \quad \forall a ^ {i} \in \mathscr {A}.
$$

Let

$$
\omega = \rho^ {\prime \prime} (a ^ {0}) d \rho^ {\prime \prime} (a ^ {1}) \dots d \rho^ {\prime \prime} (a ^ {n}) \in \Omega^ {\prime \prime n}.
$$

Then by hypothesis one has

$$
\left(\tau_ {1} - \tau_ {2}\right) \left(a ^ {0}, a ^ {1}, \dots , a ^ {n}\right) = \int d \omega .
$$

Since $\rho''(a^0) = \rho''(1)\rho''(a^0)$ one has

$$
d \omega = (d \rho^ {\prime \prime} (\mathrm{I})) \rho^ {\prime \prime} (a ^ {0}) d \rho^ {\prime \prime} (a ^ {1}) \dots d \rho^ {\prime \prime} (a ^ {n}) + \rho^ {\prime \prime} (\mathrm{I}) d \rho^ {\prime \prime} (a ^ {0}) \dots d \rho^ {\prime \prime} (a ^ {n}).
$$

Using the tracial property of $\int$ one gets

$$
\int d \omega = (- \mathrm{I}) ^ {n} \varphi (a ^ {0}, a ^ {1}, \dots , a ^ {n}, \mathrm{I}) + \varphi (\mathrm{I}, a ^ {0}, \dots , a ^ {n}).
$$

Using again the tracial property of $\int$ one checks that $\varphi$ is a Hoschchild cocycle.

Lemma 29. — Let $\tau_{1}, \tau_{2} \in Z_{\lambda}^{n}(\mathcal{A})$ and assume that $\tau_{1} - \tau_{2} = B_{0}\varphi$ for some $\varphi \in Z^{n+1}(\mathcal{A}, \mathcal{A}^{*})$. Then any two cycles over $\mathcal{A}$ with characters $\tau_{1}, \tau_{2}$ are cobordant.

Proof. — Let $\mathcal{A} \xrightarrow{\rho} \Omega$ be a cycle over $\mathcal{A}$ with character $\tau$. Let us first show that it is cobordant with $(\Omega(\mathcal{A}), \hat{\tau})$. In the above cobordism of $\Omega$ with itself, with restriction maps $r_0, r_1$, we can consider the subalgebra defined by $r_1(\omega) \in \Omega'$, where $\Omega'$ is the graded differential subalgebra of $\Omega$ generated by $\rho(\mathcal{A})$. This defines a cobordism of $\Omega$ with $\Omega'$. Now the homomorphism $\widetilde{\rho}: \Omega(\mathcal{A}) \to \Omega'$ is surjective, and satisfies $\widetilde{\rho}^* \int = \hat{\tau}$. Thus one can modify the restriction map in the canonical cobordism of $(\Omega(\mathcal{A}), \hat{\tau})$ with itself to get a cobordism of $(\Omega(\mathcal{A}), \hat{\tau})$ with $\Omega'$.

Let us show that $(\Omega(\mathcal{A}), \widehat{\tau}_{1})$ and $(\Omega(\mathcal{A}), \widehat{\tau}_{2})$ are cobordant. Let $\mu$ be the linear functional on $\Omega^{n+1}(\mathcal{A})$ defined by

$$
\text { I) } \mu (a ^ {0} d a ^ {1} \dots d a ^ {n + 1}) = \varphi (a ^ {0}, \dots , a ^ {n + 1}),
$$

$$
2) \mu (d a ^ {1} \dots d a ^ {n + 1}) = (\mathrm{B} _ {0} \varphi) (a ^ {1}, \dots , a ^ {n + 1}).
$$

Let us check that $\mu$ is a graded trace on $\Omega(\mathcal{A})$. We already know by the Hochschild cocycle property of $\varphi$ that

$$
\mu (a (b \omega)) = \mu ((b \omega) a), \quad \forall a, b \in \mathscr {A}, \omega \in \Omega^ {n + 1}.
$$

Let us check that $\mu(a\omega) = \mu(\omega a)$ for $\omega = da^{1} \ldots da^{n+1}$. The right side gives

$$
\begin{array}{r l} \mu (\sum_ {j = 1} ^ {n + 1} (- \mathrm{I}) ^ {n + 1 - j} d a ^ {1} \dots d (a ^ {j} a ^ {j + 1}) \dots d a ^ {n + 1} d a) & \\ & + (- \mathrm{I}) ^ {n + 1} \mu (a ^ {1} d a ^ {2} \dots d a) \\ & = \sum_ {= 1} ^ {n + 1} (- \mathrm{I}) ^ {n + 1 - j} (\mathrm{B} _ {0} \varphi) (a ^ {1}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}, a) \\ & + (- \mathrm{I}) ^ {n + 1} \varphi (a ^ {1}, a ^ {2}, \dots , a ^ {n + 1}, a) \\ & = (- \mathrm{I}) ^ {n} ((b ^ {\prime} \mathrm{B} _ {0} \varphi) - \varphi) (a ^ {1}, a ^ {2}, \dots , a ^ {n + 1}, a). \end{array}
$$

Now one checks that for an arbitrary cochain $\varphi \in \mathbf{C}^{n + 1}(\mathcal{A},\mathcal{A}^*)$ one has

$$
\mathrm{B} _ {0} b \varphi + b ^ {\prime} \mathrm{B} _ {0} \varphi = \varphi - (- 1) ^ {n + 1} \varphi^ {\lambda},
$$

where $\lambda$ is the cyclic permutation $\lambda(i) = i - 1$. Here $\varphi$ is a cocycle, $b\varphi = 0$ and $b'\mathrm{B}_0\varphi -\varphi = (-1)^n\varphi^\lambda$ so that $\mu (\omega a) = \varphi (a,a^1,\dots ,a^{n + 1}) = \mu (a\omega)$.

It remains to check that for any $a \in \mathcal{A}$ and $\omega \in \Omega^n$ one has

$$
\mu ((d a) \omega) = (- 1) ^ {n} \mu (\omega d a).
$$

For $\omega \in d\Omega^{n-1}$ this follows from the fact that $\mathbf{B}_0 \varphi \in \mathbf{C}_\lambda^n$ (recall that $\mathbf{B}_0 \varphi = \tau_1 - \tau_2$). For $\omega = a^0 da^1 \ldots da^n$ it is a consequence of the cocycle property of $\mathbf{B}_0 \varphi$. Indeed one has $b\mathbf{B}_0 \varphi = 0$, hence $b' \mathbf{B}_0 \varphi(a^0, a^1, \ldots, a^n, a) = (-1)^n \mathbf{B}_0 \varphi(aa^0, a^1, \ldots, a^n)$ and since $b' \mathbf{B}_0 \varphi = \varphi - (-1)^{n+1} \varphi^\lambda$ we get

$$
\begin{array}{r l} \varphi (a ^ {0}, \dots , a ^ {n}, a) - (- \mathrm{I}) ^ {n + 1} \varphi (a, a ^ {0}, \dots , a ^ {n}) & = (- \mathrm{I}) ^ {n + 1} (\mathrm{B} _ {0} \varphi) (a a ^ {0}, a ^ {1}, \dots , a ^ {n}), \end{array}
$$

i.e. that $\mu((da)a^0 da^1\ldots da^n) = (-1)^n\mu(a^0 da^1\ldots da^n da)$.

To end the proof of lemma 29 one modifies the natural cobordism between $(\Omega(\mathcal{A}), \hat{\tau}_{1})$ and itself, given by the tensor product of $\Omega(\mathcal{A})$ by the algebra of differential forms on $[0, 1]$, by adding to the integral the term $\mu \circ r_{1}$, where $r_{1}$ is the restriction map to $\{1\} \subset [0, 1]$.

Putting together lemmas 28 and 29 we see that two cocycles $\tau_{1}, \tau_{2} \in Z_{\lambda}^{n}(\mathcal{A})$ correspond to cobordant cycles if and only if $\tau_{1} - \tau_{2}$ belongs to the subspace $Z_{\lambda}^{n}(\mathcal{A}) \cap B_{0}(Z^{n+1}(\mathcal{A}, \mathcal{A}^{*}))$.

We shall now work out a better description of this subspace. Since  $\mathbf{A}\tau = (n + 1)\tau$  for any  $\tau \in \mathbf{C}_{\lambda}^{n}(\mathcal{A})$ , where A is the operator of cyclic antisymmetrisation, the above subspace is clearly contained in the subspace

$$
\mathbf {Z} ^ {n} (\mathcal {A}) \cap \mathrm{B} (\mathbf {Z} ^ {n + 1} (\mathcal {A}, \mathcal {A} ^ {*})),
$$

where $\mathbf{B} = \mathrm{AB}_0\colon \mathbf{C}^{n + 1}\to \mathbf{C}^n.$

Lemma 30. — a) One has bB = - Bb.

b) One has $\mathbf{Z}_{\lambda}^{n}(\mathcal{A})\cap \mathrm{B}_{0}(\mathbf{Z}^{n + 1}(\mathcal{A},\mathcal{A}^{*})) = \mathrm{BZ}^{n + 1}(\mathcal{A},\mathcal{A}^{*}).$

Proof. — a) For any cochain $\varphi \in \mathbf{C}^{n+1}(\mathcal{A}, \mathcal{A}^*)$, one has

$$
\mathrm{B} _ {0} b \varphi + b ^ {\prime} \mathrm{B} _ {0} \varphi = \varphi - (- \mathrm{i}) ^ {n + 1} \varphi^ {\lambda},
$$

332

where  $\lambda$  is the cyclic permutation  $\lambda(i)=i-1$ . Applying A to both sides gives  $AB_{0}b\varphi+Ab'B_{0}\varphi=0$ . Thus the answer follows from lemma 3 of section 1.

b) By a) one has $\mathbf{BZ}^{n + 1}(\mathcal{A},\mathcal{A}^*)\subset \mathbf{Z}_\lambda^n (\mathcal{A})$ . Let us show that

$$
\mathrm{BZ} ^ {n + 1} (\mathscr {A}, \mathscr {A} ^ {*}) \subset \mathrm{B} _ {0} \mathrm{Z} ^ {n + 1} (\mathscr {A}, \mathscr {A} ^ {*}).
$$

Let $\beta \in \mathbf{BZ}^{n + 1}(\mathcal{A},\mathcal{A}^*)$ , so that $\beta = \mathbf{B}\varphi ,\varphi \in \mathbf{Z}^{n + 1}(\mathcal{A},\mathcal{A}^*)$

We shall construct in a canonical way a cochain $\psi \in \mathbf{C}^n (\mathcal{A},\mathcal{A}^*)$ such that $\frac{\mathrm{I}}{n + \mathrm{I}}\beta = \mathrm{B}_0(\varphi -b\psi)$. Let $\theta = \mathrm{B}_0\varphi -\frac{\mathrm{I}}{n + \mathrm{I}}\beta$. By hypothesis A$\theta = 0$. Thus there exists a canonical $\psi$ such that $\psi -\varepsilon (\lambda)\psi^{\lambda} = \theta$, where $\lambda$ is the generator of the group of cyclic permutations of $\{0,\mathrm{I},\dots,n\}$, $\lambda (i) = i - \mathrm{I}$. We just have to check the equality

$$
\mathrm{B} _ {0} b \psi = \theta .
$$

Using the equality  $B_{0} b\psi + b' B_{0} \psi = \psi - \varepsilon(\lambda) \psi^{\lambda}$ , we just have to show that  $b' B_{0} \psi = 0$ . One has

$$
\begin{array}{l} \mathrm{B} _ {0} \psi (a ^ {0}, \dots , a ^ {n - 1}) = \psi (\mathrm{I}, a ^ {0}, \dots , a ^ {n - 1}) - (- \mathrm{I}) ^ {n} \psi (a ^ {0}, \dots , a ^ {n - 1}, \mathrm{I}) \\ = (- \mathrm{I}) ^ {n - 1} (\psi - \varepsilon (\lambda) \psi^ {\lambda}) (a ^ {0}, \dots , a ^ {n - 1}, \mathrm{I}) = (- \mathrm{I}) ^ {n - 1} \theta (a ^ {0}, \dots , a ^ {n - 1}, \mathrm{I}) \\ = (- \mathrm{I}) ^ {n - 1} (\varphi (\mathrm{I}, a ^ {0}, \dots , a ^ {n - 1}, \mathrm{I}) - (- \mathrm{I}) ^ {n + 1} \varphi (a ^ {0}, \dots , a ^ {n - 1}, \mathrm{I}, \mathrm{I})) \\ + \frac {\mathrm{I}}{n + \mathrm{I}} (- \mathrm{I}) ^ {n} \beta (a ^ {0}, \dots , a ^ {n - 1}, \mathrm{I}). \end{array}
$$

The contribution of the first two terms to $b' \mathbf{B}_0 \psi(a^0, \ldots, a^n)$ is

$$
\begin{array}{r l} (- \mathrm{I}) ^ {n - 1} \sum_ {j = 0} ^ {n - 1} (- \mathrm{I}) ^ {j} & (\varphi (\mathrm{I}, a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n}, \mathrm{I}) \\ & + (- \mathrm{I}) ^ {n} \varphi (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n}, \mathrm{I}, \mathrm{I})) \\ & = (- \mathrm{I}) ^ {n} (b \varphi (\mathrm{I}, a ^ {0}, \dots , a ^ {n}, \mathrm{I}) - \varphi (a ^ {0}, \dots , a ^ {n}, \mathrm{I})) \\ & - (b \varphi (a ^ {0}, \dots , a ^ {n}, \mathrm{I}, \mathrm{I}) - (- \mathrm{I}) ^ {n} \varphi (a ^ {0}, \dots , a ^ {n}, \mathrm{I})) = 0 \end{array}
$$

since $b\varphi = 0$.

The contribution of the second term is proportional to

$$
\sum_ {j = 0} ^ {n - 1} (- \mathrm{I}) ^ {j} \beta (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n}, \mathrm{I}) = b \beta (a ^ {0}, \dots , a ^ {n}, \mathrm{I}) = 0. \quad \square
$$

Corollary 31. — 1) The image of $\mathbf{B}:\mathbf{C}^{n + 1}\to \mathbf{C}^n$ is exactly $\mathbf{C}_{\lambda}^{n}$.

$$
2) \mathrm{B} _ {\lambda} ^ {n} (\mathcal {A}) \subset \mathrm{B} _ {0} \mathrm{Z} ^ {n + 1} (\mathcal {A}, \mathcal {A} ^ {*}).
$$

Proof. — 1) ⇒ 2) since, assuming 1), any $b\varphi$, $\varphi \in \mathbf{C}_{\lambda}^{n+1}$ is of the form $b\mathrm{B}\psi = -\mathrm{B}b\psi$ and hence belongs to $\mathrm{BZ}^{n+1}(\mathcal{A}, \mathcal{A}^*)$ so that the conclusion follows from $b)$. To prove 1) let $\varphi \in \mathbf{C}_{\lambda}^{n}$. Choose a linear functional $\varphi_{0}$ on $\mathcal{A}$ with $\varphi_{0}(1) = 1$, and then let

$$
\begin{array}{r l} \psi (a ^ {0}, \dots , a ^ {n + 1}) & = \varphi_ {0} (a ^ {0}) \varphi (a ^ {1}, \dots , a ^ {n + 1}) \\ & \quad + (- \mathrm{I}) ^ {n} \varphi ((a ^ {0} - \varphi_ {0} (a ^ {0}) \mathrm{I}), a ^ {1}, \dots , a ^ {n}) \varphi_ {0} (a ^ {n + 1}). \end{array}\tag{333}
$$

One has $\psi (\mathrm{I},a^0,\dots ,a^n) = \varphi (a^0,\dots ,a^n)$ and

$$
\begin{array}{r l} \psi (a ^ {0}, \dots , a ^ {n}, \mathrm{I}) & = \varphi_ {0} (a ^ {0}) \varphi (a ^ {1}, \dots , a ^ {n}, \mathrm{I}) + (- \mathrm{I}) ^ {n} \varphi (a ^ {0}, \dots , a ^ {n}) \\ & + (- \mathrm{I}) ^ {n + 1} \varphi_ {0} (a ^ {0}) \varphi (\mathrm{I}, a ^ {1}, \dots , a ^ {n}) = (- \mathrm{I}) ^ {n} \varphi (a ^ {0}, \dots , a ^ {n}). \end{array}
$$

Thus $\mathbf{B}_0\psi = 2\varphi$ and $\varphi \in \operatorname {Im}\mathbf{B}.$

We are now ready to state the main result of this section. By lemma 4 a) one has a well-defined map B from the Hochschild cohomology group $\mathbf{H}^{n + 1}(\mathcal{A},\mathcal{A}^*)$ to $\mathbf{H}_{\lambda}^{n}(\mathcal{A})$.

Theorem 32. — Two cycles over $\mathcal{A}$ are cobordant if and only if their characters $\tau_{1}, \tau_{2} \in \mathrm{H}_{\lambda}^{n}(\mathcal{A})$ differ by an element of the image of B, where

$$
\mathbf {B}: \mathrm{H} ^ {n + 1} (\mathcal {A}, \mathcal {A} ^ {*}) \rightarrow \mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}).
$$

It is clear that the direct sum of two cycles over $\mathcal{A}$ is still a cycle over $\mathcal{A}$ and that cobordism classes of cycles over $\mathcal{A}$ form a group $\mathbf{M}^{*}(\mathcal{A})$. The tensor product of cycles gives a natural map: $\mathbf{M}^{*}(\mathcal{A}) \times \mathbf{M}^{*}(\mathcal{B}) \to \mathbf{M}^{*}(\mathcal{A} \otimes \mathcal{B})$. Since $\mathbf{M}^{*}(\mathbf{C})$ is equal to $\mathrm{H}_{\lambda}^{*}(\mathbf{C}) = \mathbf{C}[\sigma]$ as a ring, each of the groups $\mathbf{M}^{*}(\mathcal{A})$ is a $\mathbf{C}[\sigma]$ module and in particular a vector space. By theorem 32 this vector space is $\mathrm{H}_{\lambda}^{*}(\mathcal{A}) / \mathrm{Im}\, \mathrm{B}$.

The same group  $\mathbf{M}^{*}(\mathcal{A})$  has a closely related interpretation in terms of graded traces on the differential algebra  $\Omega(\mathcal{A})$  of proposition 1. Recall that, by proposition 1, the map  $\tau\mapsto\widehat{\tau}$  is an isomorphism of  $\mathbf{Z}_{\lambda}^{n}(\mathcal{A})$  with the space of closed graded traces of degree n on  $\Omega(\mathcal{A})$ .

Theorem 33. — The map $\tau \mapsto \hat{\tau}$ gives an isomorphism of $\mathrm{H}_{\lambda}^{n}(\mathcal{A}) / \mathrm{Im}\, \mathrm{B}$ with the quotient of the space of closed graded traces of degree $n$ on $\Omega(\mathcal{A})$ by those of the form $d^{t}\mu$, $\mu$ a graded trace on $\Omega(\mathcal{A})$ (of degree $n + 1$).

Proof. — We have to show that, given $\tau \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$, one has $\hat{\tau} = d^{t}\mu$ for some graded trace $\mu$ if and only if $\tau \in \operatorname{Im} B \supset B_{\lambda}^{n}$. Assume first that $\hat{\tau} = d^{t}\mu$. Then as in lemma 28, one gets $\tau = B_{0}\varphi$ where $\varphi \in Z^{n+1}(\mathcal{A},\mathcal{A}^{*})$ is the Hochschild cocycle

$$
\varphi (a ^ {0}, a ^ {1}, \dots , a ^ {n + 1}) = \mu (a ^ {0} d a ^ {1} \dots d a ^ {n + 1}), \quad \forall a ^ {i} \in \mathscr {A}.
$$

Thus $\tau = \frac{\mathrm{I}}{n + \mathrm{I}}\mathrm{AB}_0\varphi \in \operatorname {Im}\mathbf{B}.$

Conversely, if $\tau \in \operatorname{Im} B$, then by lemma 30 b) one has $\tau = B_0 \varphi$ for some $\varphi \in Z^{n+1}(\mathcal{A}, \mathcal{A}^*)$. Defining the linear functional $\mu$ on $\Omega^{n+1}(\mathcal{A})$ as in lemma 29 we get a graded trace such that

$$
\mu (d a ^ {0} d a ^ {1} \dots d a ^ {n}) = \tau (a ^ {0}, \dots , a ^ {n}), \quad \forall a ^ {i} \in \mathcal {A}
$$

i.e.

$$
\mu (d \omega) = \hat {\tau} (\omega), \quad \forall \omega \in \Omega^ {n} (\mathscr {A}). \quad \square
$$

Thus  $\mathbf{M}^{*}(\mathcal{A})$  is the homology of the complex of graded traces on  $\Omega(\mathcal{A})$  with the differential  $d^{t}$ . This theory is dual to the theory obtained as the cohomology of the quotient of the complex  $(\Omega(\mathcal{A}), d)$  by the subcomplex of commutators. The latter appears

433

independently in the work of M. Karoubi [39] as a natural range for the higher Chern character defined on all the Quillen algebraic K-theory groups  $\mathrm{K}_{\mathbf{i}}(\mathcal{A})$ . Thus theorem 33 (and the analogous dual statement) allows:

1) to apply Karoubi's results [39] to extend the pairing of section 2 to all $\mathbf{K}_{\mathbf{i}}(\mathcal{A})$;

2) to apply the results of section 4 (below) to compute the cohomology of the complex $(\Omega(\mathcal{A}) / [ , ], d)$.

## 4. The exact couple relating  $H_{\lambda}^{*}(\mathcal{A})$  to Hochschild cohomology

By construction the complex  $(\mathbf{C}_{\lambda}^{n}(\mathcal{A}), b)$  is a subcomplex of the Hochschild complex  $(\mathbf{C}^{n}(\mathcal{A}, \mathcal{A}^{*}), b)$ , i.e. the identity map I is a morphism of complexes and gives an exact sequence:

$$
0 \rightarrow C _ {\lambda} ^ {n} \stackrel {I} {\rightarrow} C ^ {n} \rightarrow C ^ {n} / C _ {\lambda} ^ {n} \rightarrow 0.
$$

To this exact sequence corresponds a long exact sequence of cohomology groups.

We shall prove in this section that the cohomology of the complex $\mathbf{C} / \mathbf{C}_{\lambda}$ is $\mathbf{H}^n (\mathbf{C} / \mathbf{C}_{\lambda}) = \mathbf{H}^{n - 1}(\mathbf{C}_{\lambda})$.

Thus the long exact sequence of the above triple will take the form

$$
\begin{array}{r l} \mathrm{o} & \to \mathrm{H} _ {\lambda} ^ {0} (\mathcal {A}) \xrightarrow {\mathrm{I}} \mathrm{H} ^ {0} (\mathcal {A}, \mathcal {A} ^ {*}) \to \mathrm{H} _ {\lambda} ^ {- 1} (\mathcal {A}) \to \mathrm{H} _ {\lambda} ^ {1} (\mathcal {A}) \xrightarrow {\mathrm{I}} \mathrm{H} ^ {1} (\mathcal {A}, \mathcal {A} ^ {*}) \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {…} \\ & \mathrm{H} ^ {n} (\mathcal {A}) \xrightarrow {\mathrm{I}} \mathrm{H} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) \to \mathrm{H} _ {\lambda} ^ {n - 1} (\mathcal {A}) \to \mathrm{H} _ {\lambda} ^ {n + 1} (\mathcal {A}) \xrightarrow {\mathrm{I}} \mathrm{H} ^ {n + 1} (\mathcal {A}, \mathcal {A} ^ {*}) \to \dots . \end{array}
$$

On the other hand we have already constructed morphisms of cochain complexes S and B which have precisely the right degrees:

$$
\begin{array}{l} \mathrm{S}: \mathrm{H} _ {\lambda} ^ {n - 1} (\mathcal {A}) \to \mathrm{H} _ {\lambda} ^ {n + 1} (\mathcal {A}), \\ \mathrm{B}: \mathrm{H} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) \to \mathrm{H} _ {\lambda} ^ {n - 1} (\mathcal {A}). \end{array}
$$

We shall prove that these are exactly the maps involved in the above long exact sequence, which now takes the form

$$
\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) \xrightarrow {\mathrm{I}} \mathrm{H} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) \xrightarrow {\mathrm{B}} \mathrm{H} _ {\lambda} ^ {n - 1} (\mathcal {A}) \xrightarrow {\mathrm{S}} \mathrm{H} _ {\lambda} ^ {n + 1} (\mathcal {A}) \xrightarrow {\mathrm{I}} \dots
$$

Finally to the pair $b$, $\mathbf{B}$ corresponds a double complex as follows:

$C^{n,m} = C^{n-m}(A, A^*)$  (i.e.  $C^{n,m}$  is o above the main diagonal) where the first differential  $d_{1}: C^{n,m} \to C^{n+1,m}$  is given by the Hochschild coboundary b and the second differential  $d_{2}: C^{n,m} \to C^{n,m+1}$  is given by the operator B.

By lemma 30 of section 3 one has the graded commutation of  $d_{1}$ ,  $d_{2}$ . Also one checks that  $B^{2}=0$  so that  $d_{2}^{2}=0$ . By construction the cohomology of this double complex depends only upon the parity of n and we shall prove that the sum of the even and odd groups is canonically isomorphic with

$$
\mathrm{H} _ {\lambda} ^ {*} (\mathcal {A}) \underset {\mathrm{H} _ {\lambda} ^ {*} (\mathbf {c})} {\otimes} \mathbf {C} = \mathrm{H} ^ {*} (\mathcal {A})
$$

(where $\mathbf{H}_{\lambda}^{*}(\mathbf{C})$ acts on $\mathbf{C}$ by evaluation at $\sigma == \mathrm{I}$).

335

The second filtration of this double complex  $(\mathbf{F}^{q}=\sum_{m\geq q}\mathbf{C}^{n,m})$  yields the same filtration of  $\mathrm{H}^{*}(\mathcal{A})$  as the filtration by dimensions of cycles. The associated spectral sequence is convergent and coincides with the spectral sequence coming from the above exact couple. All these results are based on the next two lemmas.

Lemma 34. — Let $\psi \in \mathbf{C}^n(\mathcal{A}, \mathcal{A}^*)$ be such that $b\psi \in \mathbf{C}_\lambda^{n+1}(\mathcal{A})$. Then $\mathbf{B}\psi \in \mathbf{Z}_\lambda^{n-1}(\mathcal{A})$ and $\mathrm{SB}\psi = 2i\pi n(n + 1)b\psi$ in $\mathrm{H}_{\lambda}^{n+1}(\mathcal{A})$.

Proof. — One has  $B\psi \in C_{\lambda}^{n-1}$  by construction, and  $bB\psi = -Bb\psi = 0$  since  $b\psi \in C_{\lambda}^{n+1}$ . Thus  $B\psi \in Z_{\lambda}^{n-1}$ . In the same way  $b\psi \in Z_{\lambda}^{n+1}$ .

Let $\varphi = B\psi$, by proposition 12 of section 1 one has $S\varphi = b\psi'$ where $\psi'(a^0, \ldots, a^n) = \sum_{j=1}^{n} (-1)^{j-1} \widehat{\varphi}(a^0(da^1 \ldots da^{j-1}) a^j(da^{j+1} \ldots da^n)).$

It remains to show that

$$
\psi^ {\prime} - \varepsilon (\lambda) \psi^ {\prime \lambda} = n (n + 1) (\psi^ {\prime \prime} - \varepsilon (\lambda) \psi^ {\prime \prime \lambda})
$$

where $\lambda(i) = i - \mathrm{I}$ for $i \in \{0, \mathrm{I}, \ldots, n + \mathrm{I}\}$ and $\psi'' - \psi \in \mathbf{B}^n$. Let us first check that $(\psi' - \varepsilon(\lambda) \psi'^{\lambda})(a^0, \ldots, a^n) = (-\mathrm{I})^{n-1}(n + \mathrm{I}) \varphi(a^n a^0, a^1, \ldots, a^{n-1})$.

One has

$$
\psi^ {\prime \lambda} (a ^ {0}, \dots , a ^ {n}) = \sum_ {j = 0} ^ {n - 1} (- \mathrm{I}) ^ {j} \widehat {\varphi} ((d a ^ {0} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n - 1}) a ^ {n}).
$$

Let

$$
\omega_ {j} = a ^ {0} (d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n - 1}) a ^ {n}.
$$

Then

$$
\begin{array}{r l} d \omega_ {j} = (d a ^ {0} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n - 1}) a ^ {n} \\ & + (- \mathrm{I}) ^ {j - 1} a ^ {0} (d a ^ {1} \dots d a ^ {i} \dots d a ^ {n - 1}) a ^ {n} \\ & + (- \mathrm{I}) ^ {n} a ^ {0} (d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n}). \end{array}
$$

Thus for $j \in \{\mathrm{I}, \dots, n - \mathrm{I}\}$ one has

$$
\begin{array}{r l} (- \mathrm{I}) ^ {j - 1} \widehat {\varphi} (a ^ {0} (d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n})) & \\ - \varepsilon (\lambda) (- \mathrm{I}) ^ {j} \widehat {\varphi} ((d a ^ {0} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n - 1}) a ^ {n}) & \\ = (- \mathrm{I}) ^ {n - 1} \varphi (a ^ {n} a ^ {0}, a ^ {1}, \dots , a ^ {n - 1}). \end{array}
$$

Taking into account the cases j = 0 and j = n gives the desired result.

Let us now determine $\psi''$, $\psi'' - \psi \in \mathbf{B}^n(\mathcal{A}, \mathcal{A}^*)$ such that

$$
(\psi^ {\prime \prime} - \varepsilon (\lambda) \psi^ {\prime \prime \lambda}) (a ^ {0}, \dots , a ^ {n}) = \frac {(- \mathrm{I}) ^ {n - 1}}{n} \varphi (a ^ {n} a ^ {0}, \dots , a ^ {n - 1}).
$$

Let $\theta = B_0\psi$ and write $\theta = \theta_{1} + \theta_{2}$ with $A\theta_{1} = o$, $\theta_{2} \in C_{\lambda}^{n-1}(\mathcal{A})$ so that $\theta_{2} = \frac{1}{n}\varphi$. Since $A\theta_{1} = o$ there exists $\psi_{1} \in C^{n-1}$ such that $\theta_{1} = D\psi_{1}$ where $D\psi_{1} = \psi_{1} - \varepsilon(\lambda)\psi_{1}^{\lambda}$.

Parallel to lemma 3 of section 1 one checks that $\mathbf{D} \circ b = b' \circ \mathbf{D}$ and hence $\mathrm{D}(b\psi_1) = b'\theta_1$. Let $\psi'' = \psi - b\psi_1$. As $\mathbf{D} = \mathbf{B}_0b + b'\mathbf{B}_0$ we get $\mathrm{D}\psi = b'\mathbf{B}_0\psi = b'\theta_1 + b'\theta_2$ hence $\mathrm{D}\psi'' = b'\theta_2 = \frac{\mathrm{I}}{n}b'\varphi$. Finally since $b\varphi = 0$ one has

$$
b ^ {\prime} \varphi = (- 1) ^ {n - 1} \varphi (a ^ {n} a ^ {0}, a ^ {1}, \dots , a ^ {n - 1}). \quad \square
$$

As an immediate application of this lemma we get:

Corollary 35. — The image of S: H$_{\lambda}^{n-1}$(A) → H$_{\lambda}^{n+1}$(A) is the kernel of the map I: H$_{\lambda}^{n+1}$(A) → H$^{n+1}$(A, A$^{*}$).

This is a really useful criterion for deciding when a given cocycle is a cup product by $\sigma \in \mathrm{H}_{\lambda}^{2}(\mathbf{C})$, a question which arose naturally in part I. In particular it shows that if V is a compact manifold of dimension $m$ and if we take $\mathcal{A} = \mathbf{C}^{\infty}(\mathbf{V})$, any cocycle $\tau$ in $\mathrm{H}_{\lambda}^{n}(\mathcal{A})$ (satisfying the obvious continuity requirements (cf. Section 5)) is in the image of S for $n > m = \dim V$.

Let us now prove the second important lemma:

Lemma 36. — The obvious map from (Im B ∩ Ker b)/b(Im B) to (Ker B ∩ Ker b)/b(Ker B) is bijective.

Proof. — Let us show the injectivity. Let $\varphi \in \operatorname{Im} B \cap \operatorname{Ker} b$, say $\varphi \in Z_{\lambda}^{n+1}(\mathcal{A})$, and assume $\varphi \in b(\operatorname{Ker} B)$. Then the above lemma shows that $\varphi$ and $So = o$ are in the same class in $H_{\lambda}^{n+1}(\mathcal{A})$ and hence $\varphi \in b(\operatorname{Im} B)$.

Let us show the surjectivity. Let $\varphi \in \mathbf{Z}^{n+1}(\mathcal{A},\mathcal{A}^*)$, $\mathbf{B}\varphi = 0$ and $\psi \in \mathbf{C}^n (\mathcal{A},\mathcal{A}^*)$; $\psi -\varepsilon (\lambda)\psi^{\lambda} = \mathbf{B}_0\varphi$. As in the proof of lemma 30 of section 3 one gets $\mathbf{B}_0b\psi = \mathbf{B}_0\varphi$. This shows that $\varphi^{\prime} = \varphi -b\psi \in \mathbf{Z}_{\lambda}^{n}(\mathcal{A})$ since $\mathbf{D}\varphi^{\prime} = \mathbf{B}_0b\varphi ' + b' \mathbf{B}_0\varphi ' = 0$. Let us show that $\mathbf{B}\psi \in b\mathbf{C}_{\lambda}^{n-2}$. Since $\psi -\varepsilon (\lambda)\psi^{\lambda} = \mathbf{B}_0b\psi$ one has $b^{\prime}\mathbf{B}_{0}\psi = 0$. One checks easily that $b^{\prime 2} = 0$ and that the $b^{\prime}$ cohomology on $\mathbf{C}^n (\mathcal{A},\mathcal{A}^*)$ is trivial (if $b^{\prime}\varphi_{1} = 0$ one has $b^{\prime}\varphi_{1}(a^{0},\ldots ,a^{n},1) = 0$ i.e. $\varphi_{1} = b^{\prime}\varphi_{2}$ where

$$
\varphi_ {2} (a ^ {0}, \dots , a ^ {n - 1}) = (- \mathrm{I}) ^ {n - 1} \varphi_ {1} (a ^ {0}, \dots , a ^ {n - 1}, \mathrm{I})).
$$

Thus $\mathbf{B}_0\psi = b'\theta$ for some $\theta \in \mathbf{C}^{n - 2}$ and $\mathbf{B}\psi = \mathbf{A}b'\theta = b\mathbf{A}\theta \in b\mathbf{C}_{\lambda}^{n - 2}$.

Thus since $\mathbf{C}_{\lambda}^{n-2} = \operatorname{Im} \mathbf{B}$ one has $\mathbf{B} \psi = b \mathbf{B} \theta_{1}$ for some $\theta_{1} \in \mathbf{C}^{n-1}$ i.e. $\psi + b \theta_{1} \in \operatorname{Ker} \mathbf{B}$ and $b \psi \in b (\operatorname{Ker} \mathbf{B})$. As $\varphi - b \psi \in \mathbf{Z}_{\lambda}^{n}$ this ends the proof of the surjectivity. $\square$

Putting together the above lemmas 34, 36 we arrive at an expression of $\mathbf{S}:\mathrm{H}_{\lambda}^{n - 1}(\mathcal{A})\to \mathrm{H}_{\lambda}^{n + 1}(\mathcal{A})$ involving $b$ and B:

$$
\mathrm{S} = 2 i \pi n (n + \mathrm{i}) b \mathrm{B} ^ {- 1}.\tag{337}
$$

More explicitly, given $\varphi \in Z_{\lambda}^{n - 1}(\mathcal{A})$ one has $\varphi \in \operatorname{Im} B$, thus $\varphi = B\psi$ for some $\psi$, and this determines uniquely $b\psi \in (\operatorname{Ker} b \cap \operatorname{Ker} B) / b(\operatorname{Ker} B) = H_{\lambda}^{n + 1}(\mathcal{A})$. To check that $b\psi$ is equal to $\frac{I}{2i\pi}\frac{I}{n(n + I)} S\varphi$ one chooses $\psi$ as in proposition 12:

$$
\psi (a ^ {0}, \dots , a ^ {n}) = \frac {\mathrm{I}}{n (n + \mathrm{I})} \sum_ {j = 1} ^ {n} \widehat {\varphi} (a ^ {0} (d a ^ {1} \dots d a ^ {j - 1}) a ^ {j} (d a ^ {j + 1} \dots d a ^ {n})).
$$

As an immediate corollary we get:

Theorem 37. — The following triangle is exact:

![](images/page_82_image_4.jpg)

Proof. — We have already seen that $\operatorname{Im} S = \operatorname{Ker} I$. By the above description of $S$ one has $\operatorname{Ker} S = \operatorname{Im} B$. Next $B \circ I = 0$ since $B$ is equal to $0$ on $C_{\lambda}$. Finally if $\varphi \in Z^{n}(\mathcal{A}, \mathcal{A}^{*})$ and $B\varphi \in B_{\lambda}^{n-1}$, $B\varphi = bB\theta$ for some $\theta \in C^{n-1}$ so that

$$
\varphi + b \theta \in \operatorname{Ker} \mathrm{B} \cap \operatorname{Ker} b \subset \operatorname{Im} \mathrm{I} + b (\operatorname{Ker} \mathrm{B})
$$

by lemma 36. Thus $\operatorname{Ker} B = \operatorname{Im} I$.

We shall now identify the long exact sequence given by theorem 37 with the one derived from the exact sequence of complexes

$$
\mathrm{o} \rightarrow \mathrm{C} _ {\lambda} \rightarrow \mathrm{C} \rightarrow \mathrm{C} / \mathrm{C} _ {\lambda} \rightarrow \mathrm{o}.
$$

Corollary 38. — The morphism of complexes $\mathbf{B}:\mathbf{C} / \mathbf{C}_{\lambda}\to \mathbf{C}$ induces an isomorphism of $\mathrm{H}^n (\mathbf{C} / \mathbf{C}_\lambda)$ with $\mathrm{H}_{\lambda}^{n - 1}(\mathcal{A})$ and identifies the above triangle with the long exact sequence derived from the exact sequence of complexes $\mathrm{o}\rightarrow \mathrm{C}_{\lambda}\rightarrow \mathrm{C}\rightarrow \mathrm{C} / \mathrm{C}_{\lambda}\rightarrow \mathrm{o}$.

Proof. — This follows from the five lemma applied to

$$
\begin{array}{c c c c c c c} \mathrm{H} ^ {n} (\mathbf {C} _ {\lambda}) & \longrightarrow & \mathrm{H} ^ {n} (\mathbf {C}) & \longrightarrow & \mathrm{H} ^ {n} (\mathbf {C} / \mathbf {C} _ {\lambda}) & \longrightarrow & \mathrm{H} ^ {n + 1} (\mathbf {C} _ {\lambda}) & \longrightarrow & \mathrm{H} ^ {n + 1} (\mathbf {C}) \\ \Downarrow & & \Downarrow & & \Big \downarrow_ {\mathrm{B}} & & \Downarrow & & \Downarrow \\ \mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) & \stackrel {{\mathrm{I}}} {{\longrightarrow}} & \mathrm{H} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) & \stackrel {{\mathrm{B}}} {{\longrightarrow}} & \mathrm{H} _ {\lambda} ^ {n - 1} (\mathcal {A}) & \stackrel {{\mathrm{S}}} {{\longrightarrow}} & \mathrm{H} _ {\lambda} ^ {n + 1} (\mathcal {A}) & \longrightarrow & \mathrm{H} ^ {n + 1} (\mathcal {A}, \mathcal {A} ^ {*}) \end{array}
$$

Together with theorem 32 of section 3 we get:

Corollary 39. — a) Two cycles with characters $\tau_{1}, \tau_{2}$ are cobordant if and only if $S\tau_{1} = S\tau_{2}$ in $H_{\lambda}^{*}(\mathcal{A})$.

b) One has a canonical isomorphism

$$
\mathbf {M} ^ {*} (\mathcal {A}) \underset {\mathbf {M} ^ {*} (\mathbf {C})} {\otimes} \mathbf {C} = \mathrm{H} ^ {*} (\mathcal {A}) \quad (c f. d e f i n i t i o n r 6).
$$

c) Under that isomorphism the canonical filtration $\mathbf{F}^n\mathbf{H}^*(\mathcal{A})$ corresponds to the filtration of the left side by the dimension of the cycles.

Proof of b). — Both sides are identical with the inductive limit of the system  $(\mathrm{H}_{\lambda}^{n}(\mathcal{A}), \mathrm{S})$ . □

Let us now carefully define the double complex C as follows:

a) $\mathbf{C}^{n,m} = \mathbf{C}^{n - m}(\mathcal{A},\mathcal{A}^*)$ ， $\forall n,m\in \mathbf{Z};$

b) for $\varphi \in \mathbf{C}^{n,m}$, $d_{1}\varphi = (n - m + 1)b\varphi \in \mathbf{C}^{n + 1,m}$;

c) for $\varphi \in \mathbf{C}^{n,m}$, $d_{2}\varphi = \frac{\mathrm{I}}{n - m}\mathbf{B}\varphi \in \mathbf{C}^{n,m + 1}$ (if $n = m$, the latter is o).

Note that $d_{1}d_{2} = -d_{2}d_{1}$ follows from $\mathbf{B}b = -b\mathbf{B}$.

Theorem 40. — a) The initial term $\mathbf{E}_2$ of the spectral sequence associated to the first filtration $\mathbf{F}_p\mathbf{C} = \sum_{n\geq p}\mathbf{C}^{n,m}$ is equal to o.

b) Let $\mathbf{F}^q\mathbf{C} = \sum_{m\geq q}\mathbf{C}^{n,m}$ be the second filtration, then $\mathrm{H}^p (\mathrm{F}^q\mathrm{C}) = \mathrm{H}_\lambda^n (\mathcal{A})$ for $n = p - 2q.$

c) The cohomology of the double complex $\mathbf{C}$ is given by

$$
\mathbf {H} ^ {n} (\mathbf {C}) = \mathbf {H} ^ {\mathrm{ev}} (\mathcal {A}) \quad i f n i s e v e n
$$

and

$$
\mathrm{H} ^ {n} (\mathbf {C}) = \mathrm{H} ^ {\text { odd }} (\mathscr {A}) \quad i f n i s o d d.
$$

d) The spectral sequence associated to the second filtration is convergent: it converges to the associated graded  $\Sigma\mathrm{F}^{q}\mathrm{H}^{*}(\mathcal{A})/\mathrm{F}^{q+1}\mathrm{H}^{*}(\mathcal{A})$  and it coincides with the spectral sequence associated with the exact couple. In particular its initial term  $E_{2}$  is

$$
\operatorname{Ker} (\mathbf {I} \circ \mathbf {B}) / \operatorname{Im} (\mathbf {I} \circ \mathbf {B}).
$$

Proof. — a) Let us consider the exact sequence of complexes of cochains  $o \rightarrow Im B \rightarrow Ker B \rightarrow Ker B/Im B \rightarrow o$  where the coboundary is b. By lemma 36 the first map:  $Im B \rightarrow Ker B$  becomes an isomorphism in cohomology, thus the b cohomology of the complex  $Ker B/Im B$  is o.

b) Let $\varphi \in (\mathbf{F}^q\mathbf{C})^p = \sum_{m\geq q,n + m = p}\mathbf{C}^{n,m},$ satisfy $d\varphi = 0,$ where $d = d_{1} + d_{2}$. By a) it is cohomologous in $\mathbf{F}^q\mathbf{C}$ to an element $\psi$ of $\mathbf{C}^{p - q,q}$. Then $d\psi = 0$ means $\psi \in \operatorname {Ker}b\cap \operatorname {Ker}\mathbf{B}$, and $\psi \in \operatorname {Im}d$ means $\psi \in b(\operatorname {Ker}\mathbf{B})$. Thus using the isomorphism

$$
(\operatorname{Ker} b \cap \operatorname{Ker} \mathrm{B}) / b (\operatorname{Ker} \mathrm{B}) = \mathrm{H} _ {\lambda} ^ {p - 2 q} (\mathscr {A}) \quad (\text { lemma   36 })
$$

one gets the result.

c) By the above computation of S as  $d_{1}d_{2}^{-1}$  we see that the map from  $\mathrm{H}^{p}(\mathrm{F}^{q}\mathrm{C})$  to  $\mathrm{H}^{p}(\mathrm{F}^{q-1}\mathrm{C})$  is the map S from  $\mathrm{H}_{\lambda}^{p-2q}(\mathcal{A})$  to  $\mathrm{H}_{\lambda}^{p-2q+2}(\mathcal{A})$ ; thus the answer is immediate.

d) The convergence of the spectral sequence is obvious, since  $C^{n,m}=0$  for m>n. Since the filtration of  $H^{n}(C)$  given by  $H^{n}(F^{q}C)$  coincides with the natural

filtration of  $\mathrm{H}^{*}(\mathcal{A})$  (cf. the proof of c)), the limit of the spectral sequence is the associated graded

$$
\begin{array}{l l} \sum_ {q} \mathrm{F} ^ {q} \mathrm{H} ^ {\mathrm{ev}} (\mathcal {A}) / \mathrm{F} ^ {q + 1} \mathrm{H} ^ {\mathrm{ev}} (\mathcal {A}) & \text { for } n \text { even }, \\ \sum_ {q} \mathrm{F} ^ {q} \mathrm{H} ^ {\mathrm{odd}} (\mathcal {A}) / \mathrm{F} ^ {q + 1} \mathrm{H} ^ {\mathrm{odd}} (\mathcal {A}) & \text { for } n \text { odd }. \end{array}
$$

It is clear that the initial term  $E_{2}$  is Ker I o B/Im I o B. One then checks that it coincides with the spectral sequence of the exact couple. □

We shall end this section with several remarks.

Remarks. — a) Relative theory. Since the cohomology theory  $\mathrm{H}_{\lambda}^{*}(\mathcal{A})$  is defined from the cohomology of a complex  $(\mathbf{C}_{\lambda}^{n}, b)$ , it is easy to develop a relative theory  $\mathrm{H}_{\lambda}^{*}(\mathcal{A}, \mathcal{B})$ , for pairs  $A \xrightarrow{\pi} B$  of algebras, where  $\pi$  is a surjective homomorphism. To the exact sequence of complexes

$$
0 \to \mathrm{C} _ {\lambda} ^ {n} (\mathcal {B}) \stackrel {\pi^ {*}} {\to} \mathrm{C} ^ {n} (\mathcal {A}) \to \mathrm{C} ^ {n} (\mathcal {A}, \mathcal {B}) = \mathrm{C} ^ {n} (\mathcal {A}) / \mathrm{C} ^ {n} (\mathcal {B}) \to 0
$$

corresponds a long exact sequence of cohomology groups.

Using the five lemma, the results of this section on the absolute groups extend easily to the relative groups, provided that one also extends the Hochschild theory  $\mathrm{H}^{*}(\mathcal{A},\mathcal{A}^{*})$  to the relative case.

b) Action of $\mathbf{H}^* (\mathcal{A},\mathcal{A})$ . Using the product v of [13]

$$
\mathrm{H} ^ {n} (\mathcal {A}, \mathcal {M} _ {1}) \otimes \mathrm{H} ^ {m} (\mathcal {A}, \mathcal {M} _ {2}) \rightarrow \mathrm{H} ^ {n + m} (\mathcal {A}, \mathcal {M} _ {1} \otimes_ {\mathcal {A}} \mathcal {M} _ {2})
$$

one sees that  $\mathrm{H}^{*}(\mathcal{A},\mathcal{A})$  becomes a graded commutative algebra (using  $A\otimes_{A}A=A$ , as A bimodules) which acts on  $\mathrm{H}^{*}(\mathcal{A},\mathcal{A}^{*})$  (since  $A\otimes_{A}A^{*}=A^{*}$ ). In particular any derivation  $\delta$  of A defines an element [ $\delta$ ] of  $\mathrm{H}^{1}(\mathcal{A},\mathcal{A})$ . The explicit formula of [13] for the product v would give, at the cochain level

$$
(\varphi \vee \delta) (a ^ {0}, a ^ {1}, \dots , a ^ {n + 1}) = \varphi (\delta (a ^ {n + 1}) a ^ {0}, a ^ {1}, \dots , a ^ {n}), \quad \forall \varphi \in Z ^ {n} (\mathscr {A}, \mathscr {A} ^ {*}).
$$

One checks that at the level of cohomology classes it coincides with

$$
\begin{array}{r l} (\varphi \# \delta) (a ^ {0}, a ^ {1}, \dots , a ^ {n + 1}) & = \frac {\mathrm{I}}{n + \mathrm{I}} \sum_ {j = 1} ^ {n + 1} (- \mathrm{I}) ^ {j} \widehat {\varphi} (a ^ {0} (d a ^ {1} \dots d a ^ {j - 1}) \delta (a ^ {j}) (d a ^ {j + 1} \dots d a ^ {n + 1})), \\ & \quad \forall \varphi \in \mathbb {Z} ^ {n} (\mathscr {A}, \mathscr {A} ^ {*}). \end{array}
$$

With the latter formula one checks the equality

$$
\delta^ {*} \varphi = (\mathbf {I} \circ \mathbf {B}) (\delta \vee \varphi) + \delta \vee ((\mathbf {I} \circ \mathbf {B}) \varphi) \text { in } \mathbf {H} ^ {n + 1} (\mathscr {A}, \mathscr {A} ^ {*})
$$

(where $\delta^{*}\varphi(a^{0},\ldots,a^{n})=\sum_{i=1}^{n}\varphi(a^{0},\ldots,\delta(a^{i}),\ldots,a^{n})$ for all $a^{i}\in\mathcal{A}$). This is the natural extension of the basic formula of differential geometry $\partial_{X}=di_{X}+i_{X}d$, expressing the Lie derivative with respect to a vector field X on a manifold.

c) Homotopy invariance of $\mathbf{H}^{*}(\mathcal{A})$. Let $\mathcal{A}$ be an algebra (with unit), $\mathcal{B}$ a locally convex topological algebra and $\varphi \in \mathbf{Z}_{\lambda}^{n}(\mathcal{B})$ a continuous cocycle (cf. section 5). Let $\rho_{t}, t \in [0,1]$, be a family of homomorphisms $\rho_{t}: \mathcal{A} \to \mathcal{B}$ such that

## for all $a \in \mathcal{A}$, the map $t \in [0, 1] \to \rho_t(a) \in \mathcal{B}$ is of class $\mathbf{C}^1$.

Then the images by S of the cocycles $\rho_0^*\varphi$ and $\rho_1^*\varphi$ coincide. To prove this one extends the Hochschild cocycle $\varphi \# \psi$ on $\mathcal{B} \otimes \mathbf{C}^1([o, i])$ giving the cobordism of $\varphi$ with itself (i.e. $\psi(f^0, f^1) = \int_0^1 f^0 df^1$, $\forall f^i \in \mathbf{C}^1([o, i])$) to a Hochschild cocycle on the algebra $\mathbf{C}^1([o, i], \mathcal{B})$ of $\mathbf{C}^1$-maps from $[o, i]$ to $\mathcal{B}$. Then the map $\rho: \mathcal{A} \to \mathbf{C}^1([o, i], \mathcal{B})$, $(\rho(a))_t = \rho_t(a)$, defines a chain over $\mathcal{A}$ and is a cobordism of $\rho_0^*\varphi$ with $\rho_1^*\varphi$. This shows that if one restricts to continuous cocycles, one has

$$
\rho_ {0} ^ {*} = \rho_ {1} ^ {*}: \mathrm{H} ^ {*} (\mathcal {B}) \rightarrow \mathrm{H} ^ {*} (\mathcal {A}).
$$

## 5. Locally convex algebras

Before we begin with the examples we shall briefly indicate how sections 1 to 4 adapt to a topological situation. Thus we shall assume now that the algebra $\mathcal{A}$ is endowed with a locally convex topology, for which the product $\mathcal{A} \times \mathcal{A} \to \mathcal{A}$ is continuous. In other words, for any continuous seminorm $p$ on $\mathcal{A}$ there exists a continuous seminorm $p'$ such that $p(ab) \leq p'(a)\ p'(b)$, $\forall a, b \in \mathcal{A}$. Then we replace the algebraic dual $\mathcal{A}^*$ of $\mathcal{A}$ by the topological dual, and the space $\mathbf{C}^n(\mathcal{A}, \mathcal{A}^*)$ of $(n + 1)$-linear functionals on $\mathcal{A}$ by the space of continuous $(n + 1)$-linear functionals: $\varphi \in \mathbf{C}^n$ if and only if for some continuous seminorm $p$ on $\mathcal{A}$ one has

$$
\left| \varphi (a ^ {0}, \dots , a ^ {n}) \right| \leq p (a ^ {0}) \dots p (a ^ {n}), \quad \forall a ^ {i} \in \mathscr {A}.
$$

Since the product is continuous one has  $b\varphi \in C^{n+1}$ ,  $\forall \varphi \in C^{n}$ . Since the formulae for the cup product of cochains only involve the product in A they still make sense for continuous multilinear functions and all the results of sections 1 to 4 apply with no change.

There is however an important point which we wish to discuss: the use of resolutions in the computation of the Hochschild cohomology. Note first that we may as well assume that A is complete, since  $C^{n}$  is unaffected if one replaces A by its completion, which is still a locally convex topological algebra.

Let $\mathcal{B}$ be a complete locally convex topological algebra. By a topological module over $\mathcal{B}$ we mean a locally convex vector space $\mathcal{M}$, which is a $\mathcal{B}$-module, and is such that the map $(b, \xi) \to b\xi$ is continuous (from $\mathcal{B} \times \mathcal{M}$ to $\mathcal{M}$). We say that $\mathcal{M}$ is topologically projective if it is a direct summand of a topological module of the form $\mathcal{M}' = \mathcal{B} \widehat{\otimes}_{\pi} \mathrm{E}$, where $\mathrm{E}$ is a complete locally convex vector space and $\widehat{\otimes}_{\pi}$ means the projective tensor product ([29]).

In particular M is complete, as a closed subspace of the complete locally convex vector space  $M'$ .

It is clear then that if  $M_{1}$  and  $M_{2}$  are topological B-modules which are complete (as locally convex vector spaces) and  $p: M_{1} \rightarrow M_{2}$  is a continuous B-linear map with a continuous C-linear cross-section s, one can complete the triangle of continuous B-linear maps

![](images/page_86_image_1.jpg)

for any continuous $\mathcal{B}$-linear map $f: \mathcal{M} \to \mathcal{M}_2$.

Definition 42. — Let M be a topological B-module. By a (topological) projective resolution of M we mean an exact sequence of projective B-modules and B-linear continuous maps

$$
\mathcal {M} \stackrel {\varepsilon} {\leftarrow} \mathcal {M} _ {0} \stackrel {b _ {1}} {\leftarrow} \mathcal {M} _ {1} \stackrel {b _ {2}} {\leftarrow} \mathcal {M} _ {2} \leftarrow \dots
$$

which admits a $\mathbf{C}$-linear continuous homotopy $s_i: \mathcal{M}_i \to \mathcal{M}_{i+1}$

$$
b _ {i + 1} s _ {i} + s _ {i - 1} b _ {i} = \mathrm{id}, \quad \forall i.
$$

As in [36] the module $\mathcal{A}$ over $\mathcal{B} = \mathcal{A} \hat{\otimes}_{\pi} \mathcal{A}^{0}$ (tensor product of the algebra $\mathcal{A}$ by the opposite algebra $\mathcal{A}^{0}$) given by

$$
(a \otimes b ^ {0}) c = a c b, \quad a, b, c \in \mathscr {A}
$$

admits the following canonical projective resolution:

1) $\mathcal{M}_n = \mathcal{B} \hat{\otimes}_{\pi} \mathrm{E}_n$ (as a $\mathcal{B}$-module), with $\mathrm{E}_n = \mathcal{A} \hat{\otimes}_{\pi} \ldots \hat{\otimes}_{\pi} \mathcal{A}$ ($n$ factors);

2) $\varepsilon : \mathcal{M}_0 \to \mathcal{A}$ is given by $\varepsilon(a \otimes b^0) = ab$, $a, b \in \mathcal{A}$;

$$
\begin{array}{l} 3) b _ {n} (\mathrm{I} \otimes a _ {1} \otimes \dots \otimes a _ {n}) = (a _ {1} \otimes \mathrm{I}) \otimes (a _ {2} \otimes \dots \otimes a _ {n}) \\ \qquad + \sum_ {j = 1} ^ {n - 1} (- \mathrm{I}) \dot {\mathrm{I}} \otimes a _ {1} \otimes \dots \otimes a _ {j} a _ {j + 1} \otimes \dots \otimes a _ {n}) \\ \qquad + (- \mathrm{I}) ^ {n} (\mathrm{I} \otimes a _ {n} ^ {0}) \otimes (a _ {1} \otimes \dots \otimes a _ {n - 1}). \end{array}
$$

The usual section is obviously continuous:

$$
s _ {n} ((a \otimes b ^ {0}) \otimes (a _ {1} \otimes \dots \otimes a _ {n})) = (\mathrm{I} \otimes b ^ {0}) \otimes (a \otimes a _ {1} \otimes \dots \otimes a _ {n})).
$$

Comparing this resolution with an arbitrary topological projective resolution of the module A over B yields:

Lemma 43. — For any topological projective resolution $(\mathcal{M}^n, b_n)$ of the module $\mathcal{A}$ over $\mathcal{B} = \mathcal{A} \widehat{\otimes}_{\pi} \mathcal{A}^0$, the Hochschild cohomology $\mathrm{H}^n(\mathcal{A}, \mathcal{A}^*)$ coincides with the cohomology of the

$$
\operatorname{Hom} _ {\mathcal {B}} \left(\mathcal {M} ^ {0}, \mathcal {A} ^ {*}\right) \xrightarrow {b _ {1} ^ {*}} \operatorname{Hom} _ {\mathcal {B}} \left(\mathcal {M} ^ {1}, \mathcal {A} ^ {*}\right)\rightarrow \dots
$$

(where $\operatorname{Hom}_{\mathcal{B}}$ means continuous $\mathcal{B}$ linear maps).

Of course, this lemma extends to any complete topological bimodule over $\mathcal{A}$. Let us now pass to the examples.

## 6. Examples

I) $\mathcal{A} = \mathbf{C}^{\infty}(\mathbf{V})$, V a compact smooth manifold.

We endow $\mathbf{C}^{\infty}(\mathbf{V})$ with its usual Frechet space topology, defined by the seminorms $\sup_{|\alpha| \leq n} |\partial^{\alpha} f| = p_n(f)$ using local charts in $\mathbf{V}$.

As a locally convex space,  $\mathbf{C}^{\infty}(\mathbf{V})$  is then nuclear ([29]) and one has

$$
\mathbf {C} ^ {\infty} (\mathbf {V}) \hat {\otimes} _ {\pi} \mathbf {C} ^ {\infty} (\mathbf {V}) = \mathbf {C} ^ {\infty} (\mathbf {V} \times \mathbf {V}).
$$

Thus $\mathcal{B} = \mathcal{A}\hat{\otimes}_{\pi}\mathcal{A}^{0}$ is canonically isomorphic to $\mathbf{C}^{\infty}(\mathbf{V}\times \mathbf{V})$ and the module $\mathcal{A}$ over $\mathcal{B}$ corresponds to the diagonal $\Delta$:

$$
\forall f \in \mathbf {C} ^ {\infty} (\mathbf {V} \times \mathbf {V}), \varepsilon (f) = \Delta^ {*} f.
$$

Let us assume for a while that the Euler characteristic of V vanishes. The general case will be treated by crossing V with  $S^{1}$ . Let  $E_{k}$  be the complex vector bundle on  $V \times V$  which is the pull back by the second projection  $pr_{2}: V \times V \to V$  of the exterior power  $\wedge^{k} T_{\mathfrak{G}}^{*}(V)$  of the complexified cotangent bundle of V. By construction, the dual  $E_{1}^{*}$  of  $E_{1}$  is the pull back by  $pr_{2}$  of the complexified tangent bundle. We let  $X(a, b)$  be a section of  $E_{1}^{*}$  such that:

a) for $(a, b)$ close enough to the diagonal, $\mathbf{X}(a, b)$ coincides with the real tangent vector $\exp_b^{-1}(a)$ (where $\exp_b: \mathrm{T}_b(\mathrm{V}) \to \mathrm{V}$ is the exponential map associated to a fixed affine connexion);

b) $\mathrm{X}(a,b)\neq 0$ when $a\neq b$

By hypothesis, the Euler characteristic of V vanishes so that there exists on V a real nowhere vanishing vector field Y, with the help of which one easily extends the germ of X around the diagonal to a section of  $E_{1}^{*}$  satisfying b). (Use Y as a purely imaginary component.)

Lemma 44. — The following is a continuous projective resolution of the module $\mathbf{G}^{\infty}(\mathbf{V})$ over $\mathbf{C}^{\infty}(\mathbf{V}\times\mathbf{V})$ (with the diagonal action):

$$
\mathrm{C} ^ {\infty} (\mathrm{V}) \stackrel {{\Delta^ {*}}} {{\leftarrow}} \mathrm{C} ^ {\infty} (\mathrm{V} \times \mathrm{V}) \stackrel {{i _ {\mathbf {x}}}} {{\leftarrow}} \mathrm{C} ^ {\infty} (\mathrm{V} ^ {2}, \mathrm{E} _ {1}) \stackrel {{i _ {\mathbf {x}}}} {{\leftarrow}} \dots \leftarrow \mathrm{C} ^ {\infty} (\mathrm{V} ^ {2}, \mathrm{E} _ {n}) \leftarrow 0
$$

$(n = \dim V)$ where $i_{X}$ is the contraction with X.

Proof. — Each of the modules  $\mathcal{M}_{k} = \mathrm{C}^{\infty}(\mathrm{V} \times \mathrm{V}, \mathrm{E}_{k})$  is finite projective and hence also topologically projective. Obviously  $i_{X}^{2} = 0$ . To show that one has a topological resolution it remains to construct a continuous linear section. Let  $\chi, \chi' \in \mathrm{C}^{\infty}(\mathrm{V} \times \mathrm{V})$  be such that :

$$
\mathrm{X} (a, b) = \exp_ {b} ^ {- 1} (a), \quad \forall (a, b) \in \text { Support } \chi^ {\prime};
$$

$\chi' = \mathrm{I}$ on the support of $\chi$ and $\chi = \mathrm{I}$ is a neighborhood of $\Delta$.

Let $\omega'$ be a section of $\mathbf{E}_1$ such that $\langle \mathbf{X},\omega' \rangle = \mathfrak{i}$ on the support of $\mathfrak{i} - \chi$. Put $\varphi_t(a,b) = \exp_a(t\mathbf{X}(b,a))$ for $(a,b)$ close enough to $\Delta$ and let

$$
s (\omega) = \chi^ {\prime} \int_ {0} ^ {1} \varphi_ {i} ^ {*} (d _ {b} (\chi \omega)) \frac {d t}{t} + (I - \chi) \omega^ {\prime} \wedge \omega .
$$

By construction $s$ is $\mathbf{C}^{\infty}(\mathbf{V})$-linear in the variable $a$. Fixing $a$ and taking normal coordinates around $a = o$ one gets $\varphi_t(b) = tb$, $\mathbf{X}(o, b) = -b$, so that one can easily check the equality

$$
\int_ {0} ^ {1} \left(\varphi_ {t} ^ {*} d i _ {\mathrm{X}} \omega_ {1}\right) \frac {d t}{t} + i _ {\mathrm{X}} \int_ {0} ^ {1} \left(\varphi_ {t} ^ {*} d \omega_ {1}\right) \frac {d t}{t} = \int_ {0} ^ {1} \varphi_ {t} ^ {*} \left(\partial_ {\mathrm{X}} \omega_ {1}\right) \frac {d t}{t} = \omega_ {1}
$$

for any differential form $\omega_{1}$ vanishing off the support of $\chi$ and satisfying $\omega_{1}(a, a) = 0$. Applying this with $\omega_{1} = \chi \omega$ shows that $si_{\mathrm{X}} + i_{\mathrm{X}}s = id$.

We are now ready to prove:

Lemma 45. — Let V be a compact smooth manifold, and consider $\mathcal{A} = \mathbf{C}^{\infty}(\mathbf{V})$ as a locally convex topological algebra, then:

a) The continuous Hochschild cohomology group $\mathbf{H}^k (\mathcal{A},\mathcal{A}^*)$ is canonically isomorphic with the space of de Rham currents of dimension $k$ on V. To the $(k + 1)$-linear functional $\varphi$ is associated the current C such that

$$
\langle \mathbf {C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k} \rangle = \sum_ {\sigma \in \mathfrak {G} _ {k}} \varepsilon (\sigma) \varphi (f ^ {0}, f ^ {\sigma (1)}, f ^ {\sigma (2)}, \dots , f ^ {\sigma (k)}).
$$

b) Under the isomorphism a) the operator $\mathbf{I} \circ \mathbf{B}: \mathrm{H}^k(\mathcal{A}, \mathcal{A}^*) \to \mathrm{H}^{k-1}(\mathcal{A}, \mathcal{A}^*)$ is the de Rham boundary for currents and the image of $\mathbf{B}$ in $\mathrm{H}_{\lambda}^{k-1}(\mathcal{A})$ is contained in the space of totally antisymmetric cocycle classes.

Proof. — a) One just has to compare the standard projective resolution of $\mathcal{A}$ with the resolution of lemma 44, applying lemma 43. Note that (cf. [33]) given any commutative algebra $\mathcal{A}$ and bimodule $\mathcal{M}$, the map $\mathrm{T} \mapsto \sum_{\sigma \in \mathfrak{G}_k} \varepsilon(\sigma) \mathrm{T}^\sigma$, where $\mathrm{T} \in \mathrm{C}^k(\mathcal{A}, \mathcal{M})$ and $\mathrm{T}^\sigma(a^1, \ldots, a^k) = \mathrm{T}(a^{\sigma(1)}, \ldots, a^{\sigma(k)})$, transforms Hochschild cocycles in Hochschild cocycles and its kernel contains the Hochschild coboundaries.

Next, if $\varphi \in \mathbf{Z}^k (\mathcal{A},\mathcal{A}^*)$ and $\varphi^{\sigma} = \varepsilon (\sigma)\varphi$ for $\sigma \in \mathfrak{G}_k$, with $\mathcal{A} = \mathbf{C}^{\infty}(\mathrm{V})$, then (under the obvious continuity hypothesis) there exists a current $\mathbf{C}$ on $\mathbf{V}$ such that

$$
\langle \mathbf {C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k} \rangle = \varphi (f ^ {0}, f ^ {1}, \dots , f ^ {k}), \quad \forall f ^ {i} \in \mathscr {A}.
$$

Indeed $\varphi$ now satisfies the condition

$$
\begin{array}{r l} \varphi (f ^ {0}, f ^ {1} f ^ {2}, f ^ {3}, \dots , f ^ {k + 1}) & = \varphi (f ^ {0} f ^ {1}, f ^ {2}, f ^ {3}, \dots , f ^ {k + 1}) \\ & \quad + \varphi (f ^ {0} f ^ {2}, f ^ {1}, f ^ {3}, \dots , f ^ {k + 1}) \end{array}
$$

for $f^i \in \mathbf{C}^\infty(\mathbf{V})$, which shows that, as a distribution on $\mathbf{V}^{k+1}$, its support is contained in the diagonal $\Delta_{k+1} = \{(x, x, \ldots, x) \in \mathbf{V}^{k+1}, x \in \mathbf{V}\}$. Thus the problem of existence

of C is local and easily handled say with  $V = T^{n}$  or also using local coordinates. Let  $D_{k}$  be the space of currents of dimension k on V. Define  $\beta: \mathcal{D}_{k} \to \mathrm{H}^{k}(\mathcal{A}, \mathcal{A}^{*})$  by

$$
\beta (\mathbf {C}) \left(f ^ {0}, f ^ {1}, \dots , f ^ {k}\right) = \langle \mathbf {C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k} \rangle , \quad \forall f ^ {i} \in \mathbf {C} ^ {\infty} (\mathrm{V});
$$

then the map $\beta$ has a left inverse $\alpha$ given by $\alpha(\varphi) = C$, where

$$
\langle \mathbf {C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k} \rangle = \mathrm{I} / k! \sum_ {\sigma \in \mathfrak {G} _ {k}} \varepsilon (\sigma) \varphi (f ^ {0}, f ^ {\sigma (1)}, \dots , f ^ {\sigma (k)}).
$$

To check that $\beta \circ \alpha = \mathrm{id}$ we may replace V by $V \times S^1$, since the homomorphism $\rho: \mathcal{B} = C^\infty(V \times S^1) \to \mathcal{A} = C^\infty(V)$ given by evaluation at a point $p \in S^1$ induces a split injection $H^k(\mathcal{A}, \mathcal{A}^*) \xrightarrow{\rho^*} H^k(\mathcal{B}, \mathcal{B}^*)$.

Thus we may as well assume that the Euler characteristic of V is o. Let X be a section of  $E_{1}^{*}$  as above. Let then  $(\mathcal{M}_{k}^{\prime}, b_{k}^{\prime})$  be the projective resolution of  $\mathbf{C}^{\infty}(\mathbf{V})$  given by lemma 44:

$$
\mathcal {M} _ {k} ^ {\prime} = \mathrm{C} ^ {\infty} (\mathrm{V} ^ {2}, \mathrm{E} _ {k}), \quad b _ {k} ^ {\prime} = i _ {\mathrm{X}}.
$$

By lemma 43 the Hochschild cohomology $\mathrm{H}^k (\mathbf{C}^\infty (\mathbf{V}),(\mathbf{C}^\infty (\mathbf{V}))^*)$ coincides with the cohomology of the complex $\mathrm{Hom}_{\mathbf{C}^{\infty}(\mathbf{V}^{*})}(\mathcal{M}_k',\mathbf{C}^\infty (\mathbf{V})^*)$. One has a natural isomorphism

$$
\mathbf {C} ^ {\infty} \left(\mathrm{V} ^ {2}, \mathrm{E} _ {k}\right) \otimes_ {\mathrm{C} ^ {\infty} \left(\mathrm{V} ^ {*}\right)} \mathbf {C} ^ {\infty} (\mathrm{V}) \approx \mathbf {C} ^ {\infty} \left(\mathrm{V}, \Delta^ {*} \mathrm{E} _ {k}\right)
$$

and since $\Delta^{*}\mathrm{E}_{k}$ is by construction the exterior power $\wedge^{k}\mathrm{T}_{\mathbf{c}}^{*}(\mathrm{V})$, one has a natural isomorphism of $\operatorname{Hom}_{\mathbb{C}^{\infty}(\mathbb{V}^{*})}(\mathcal{M}_{k}^{\prime},\mathbf{C}^{\infty}(\mathbf{V})^{*})$ with the space $\mathcal{D}_k$ of $k$-dimensional currents on V. More explicitly, to $\mathbf{T}\in \operatorname{Hom}_{\mathbb{C}^{\infty}(\mathbb{V}^{*})}(\mathcal{M}_{k}^{\prime},\mathbf{C}^{\infty}(\mathbf{V})^{*})$ corresponds the current $\mathbf{C}$ given by the equality

$$
\langle \mathrm{C}, \omega \rangle = \mathrm{T} (\omega^ {\prime}) (\mathrm{I}), \quad \forall \omega^ {\prime} \in \mathcal {M} _ {k} ^ {\prime}, \quad \Delta^ {*} \omega^ {\prime} = \omega .
$$

Since the restriction of X to the diagonal $\Delta$ is zero we see that the coboundary operator $i_{\mathrm{X}}^*$ is zero and hence that $\mathbf{H}^k (\mathcal{A},\mathcal{A}^*) = \mathcal{D}_k$. To write down explicitly the isomorphism we just need a chain map F of the resolution $\mathcal{M}'$ to the standard resolution $(\mathcal{M}_k = (\mathcal{A}\hat{\otimes}_{\pi}\mathcal{A}^0)\hat{\otimes}_{\pi}\mathcal{A}\hat{\otimes}_{\pi}\dots \hat{\otimes}_{\pi}\mathcal{A})$ above the identity map $\mathcal{M}_0\to \mathcal{M}_0$. Here $\mathcal{M}_k = \mathbf{C}^\infty (\mathrm{V}\times \mathrm{V}\times \mathrm{V}^k)$ and we take

$$
(\mathrm{F} \omega) (a, b, x ^ {1}, \dots , x ^ {k}) = \langle \mathrm{X} (x ^ {1}, b) \wedge \dots \wedge \mathrm{X} (x ^ {k}, b), \omega (a, b) \rangle ,
$$

$$
\forall a, b, x ^ {i} \in \mathbf {V}
$$

and $\omega \in \mathcal{M}_k^\prime = \mathrm{C}^\infty (\mathrm{V}^2,\mathrm{E}_k)$

One has

$$
\begin{array}{l} (b _ {k} \mathrm{F} \omega) (a, b, x ^ {1}, \dots , x ^ {k - 1}) = (\mathrm{F} \omega) (a, b, a, x ^ {1}, \dots , x ^ {k - 1}) \\ \qquad - \sum_ {j = 1} ^ {k - 1} (- \mathrm{i}) ^ {j} \mathrm{F} \omega (a, b, x ^ {1}, \dots , x ^ {j}, x ^ {j}, \dots , x ^ {k - 1}) \\ \qquad + (- \mathrm{i}) ^ {k} \mathrm{F} \omega (a, b, x ^ {1}, \dots , x ^ {k - 1}, b) \\ \qquad = \langle \mathrm{X} (a, b) \wedge \mathrm{X} (x ^ {1}, b) \wedge \dots \wedge \mathrm{X} (x ^ {k - 1}, b), \omega (a, b) \rangle . \end{array}
$$

This shows that $b_{k} \mathrm{F}\omega = \mathrm{Fi}_{\mathrm{X}} \omega, \forall \omega,$ so that $b_{k} \mathrm{F} = \mathrm{F}b_{k}'$ and $\mathbf{F}$ is a chain map.

Let $\varphi\in\mathbf{Z}^{k}(\mathcal{A},\mathcal{A}^{*})$ be a Hochschild cocycle, the corresponding element of $\mathrm{Hom}_{\mathbb{C}^{\infty}(\mathbb{V}^{*})}(\mathcal{M}_{k},\mathcal{A}^{*})$ is given by the equality

$$
\widetilde {\varphi} ((f \otimes g) \otimes f ^ {1} \otimes \dots \otimes f ^ {k}) (f ^ {0}) = \varphi (g f ^ {0} f, f ^ {1}, \dots , f ^ {k}), f, g, f ^ {i} \in \mathscr {A}.
$$

Let us compute the k-dimensional current corresponding to  $\widetilde{\varphi} \circ F$ . One has

$$
\langle \mathbf {C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k} \rangle = \widetilde {\varphi} \circ \mathrm{F} (\omega^ {\prime}) (\mathrm{I}),
$$

where

$$
\omega^ {\prime} = f ^ {0} \omega_ {1} \wedge \dots \wedge \omega_ {k}, \quad \omega_ {j} (a, b) = d f ^ {j} (b) \in \mathrm{T} _ {b} ^ {*} (\mathrm{V}).
$$

One has

$$
\begin{array}{r l} \mathrm{F} \omega^ {\prime} (a, b, x ^ {1}, \dots , x ^ {k}) & = \langle \mathrm{X} (x ^ {1}, b) \wedge \dots \wedge \mathrm{X} (x ^ {k}, b), \omega^ {\prime} (a, b) \rangle \\ & = f ^ {0} (b) \sum_ {\sigma \in \mathfrak {G} _ {k}} \varepsilon (\sigma) \prod_ {1} ^ {k} \langle \mathrm{X} (x ^ {i}, b), d f ^ {\sigma (i)} (b) \rangle . \end{array}
$$

This shows that to compute $\widetilde{\varphi} \circ F$ one may replace $\varphi$ by the total antisymmetrization $\varphi' = \frac{1}{k!} \sum_{\mathfrak{G}_k} \varepsilon(\sigma) \varphi^\sigma$ on the last $k$ variables. As the differential of the function $x \to \langle X(x, b), df(b) \rangle$ at the point $x = b$ is equal to $df(b)$, we conclude that the $k$-dimensional current corresponding to $\widetilde{\varphi} \circ F$ is $C = k! \alpha(\varphi)$ and hence that $\alpha$ is an isomorphism.

b) Let $\mathbf{C} \in \mathcal{D}_k$ be a $k$-dimensional current, and $\varphi$ the corresponding Hochschild cocycle: $\varphi(f^0, f^1, \ldots, f^k) = \langle \mathbf{C}, f^0 df^1 \wedge \ldots \wedge df^k \rangle$. Then

$$
\begin{array}{r l} \mathrm{B} _ {0} \varphi (f ^ {0}, \dots , f ^ {k - 1}) & = \varphi (\mathrm{I}, f ^ {0}, \dots , f ^ {k - 1}) \\ & = \langle \mathrm{C}, d f ^ {0} \wedge \dots \wedge d f ^ {k - 1} \rangle = \langle b \mathrm{C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k - 1} \rangle . \end{array}
$$

As an immediate corollary, we get:

Theorem 46. — Let $\mathcal{A} = \mathrm{C}^{\infty}(\mathrm{V})$ as a locally convex topological algebra. Then:

1) For each $k$, $\mathrm{H}_{\lambda}^{k}(\mathcal{A})$ is canonically isomorphic to the direct sum

$$
\operatorname{Ker} b \left(\subset \mathscr {D} _ {k}\right) \oplus \mathrm{H} _ {k - 2} (\mathrm{V}, \mathbf {C}) \oplus \mathrm{H} _ {k - 4} (\mathrm{V}, \mathbf {C}) \oplus \dots
$$

(where $\mathbf{H}_q(\mathbf{V},\mathbf{C})$ is the usual de Rham homology of V).

2) $\mathbf{H}^{*}(\mathcal{A})$ is canonically isomorphic to the de Rham homology $\mathrm{H}_{*}(\mathrm{V},\mathbf{C})$ (with filtration by dimensions).

Proof. — 1) Let us explicitly describe the isomorphism. Let $\varphi \in \mathrm{H}_{\lambda}^{k}(\mathcal{A})$. Then the current $\mathbf{C} = \alpha (\mathbf{I}(\varphi))$ given by

$$
\langle \mathbf {C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k} \rangle = \frac {\mathrm{I}}{k !} \sum_ {\sigma \in \mathfrak {G} _ {k}} \varphi (f ^ {0}, f ^ {\sigma (1)}, \dots , f ^ {\sigma (k)})
$$

is closed (since $\mathbf{B}(\mathbf{I}(\varphi)) = \mathbf{o}$), so that the cochain

$$
\overline {{{\varphi}}} (f ^ {0}, f ^ {1}, \dots , f ^ {k}) = \langle \mathbf {C}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k} \rangle
$$

346

belongs to  $\mathbf{Z}_{\lambda}^{k}(\mathcal{A})$ . The class of  $\varphi - \overline{\varphi}$  in  $\mathrm{H}_{\lambda}^{k}(\mathcal{A})$  is well determined, and is by construction in the kernel of I. Thus by theorem 37 there exists  $\psi \in \mathrm{H}_{\lambda}^{k-2}(\mathcal{A})$  with  $S\psi = \varphi - \overline{\varphi}$ , and  $\psi$  is unique modulo the image of B. Thus the homology class of the closed current  $\alpha(\mathrm{I}(\psi))$  is well determined. Moreover by lemma 45 b) the class of  $\psi - \overline{\psi}$  in  $\mathrm{H}_{\lambda}^{k-2}(\mathcal{A})$  is well determined. Repeating this process one gets the desired sequence of homology classes  $\omega_{j} \in \mathrm{H}_{k-2j}(\mathrm{V}, \mathbf{C})$ . By construction,  $\varphi$  is in the same class (in  $\mathrm{H}_{\lambda}^{k}(\mathcal{A})$ ) as  $\widetilde{C} + \sum_{j=1}^{\infty} S_{j} \widetilde{\omega}_{j}$  (where for any closed current  $\omega_{j}$  in the class one takes

$$
\widetilde {\omega} _ {j} (f ^ {0}, f ^ {1}, \dots , f ^ {k - 2 j}) = \langle \omega_ {j}, f ^ {0} d f ^ {1} \wedge \dots \wedge d f ^ {k - 2 j} \rangle).
$$

This shows that the map that we just constructed is an injection of $\mathbf{H}_{\lambda}^{k}(\mathcal{A})$ to $\operatorname{Ker} b(\subset \mathcal{E}_{k}) \oplus \mathbf{H}_{k-2}(\mathbf{V}, \mathbf{C}) \oplus \ldots \oplus \mathbf{H}_{k-2i}(\mathbf{V}, \mathbf{C}) \oplus \ldots$

The surjectivity is obvious.

2) In 1) we see by the construction of the isomorphism, that $\mathbf{S} : \mathbf{H}_{\lambda}^{k}(\mathcal{A}) \to \mathbf{H}_{\lambda}^{k + 2}(\mathcal{A})$ is the map which associates to each $\mathbf{C} \in \operatorname{Ker} b$ its homology class. The conclusion follows.

Remarks 47. — a) In this example the spectral sequence of theorem 39 d) is degenerate and the  $E_{2}$  term is already the de Rham homology of V (with differential equal to o).

b) Let $\varphi \in \mathrm{H}_{\lambda}^{k}(\mathbf{C}^{\infty}(\mathbf{V}))$. Then theorem 46 shows that $\varphi$ is in the same class as $\widetilde{\mathbf{C}} + \sum_{j=1}^{\infty} \mathbf{S}^{j} \widetilde{\omega}_{j}$ where the current $\mathbf{C}$ is well defined and the homology classes $\omega_{j}$ are also well defined. One can prove that, once an affine connection $\nabla$ on $\mathbf{V}$ has been chosen, one can associate canonically a sequence $\omega_{j}$ of closed currents to any $\varphi \in \mathbf{Z}_{\lambda}^{k}(\mathbf{C}^{\infty}(\mathbf{V}))$ whose support (in $\mathbf{V}^{k+1}$) is close enough to the diagonal $\Delta = \{(x, \ldots, x), x \in \mathbf{V}\}$. Moreover if $\varphi$ is local, i.e. if its support is contained in $\Delta$, then the germ of $\omega_{j}$ around any $x \in \mathbf{V}$ only depends upon the germ of $\varphi$ around $x$ and the connexion $\nabla$. This is proven by explicitly comparing the resolution of lemma 44 and the standard one. It remains valid without the hypothesis $\chi(\mathbf{V}) = 0$.

c) Let $W \subset V$ be a submanifold of $V$, $i^{*}: \mathbf{C}^{\infty}(V) \to \mathbf{C}^{\infty}(W)$ the restriction map, and $o \to \operatorname{Ker} i^{*} \to \mathbf{C}^{\infty}(V) \to \mathbf{C}^{\infty}(W) \to o$ the corresponding exact sequence of algebras. For the ordinary homology groups one has a long exact sequence

$$
\rightarrow \mathrm{H} _ {q} (\mathrm{W}) \rightarrow \mathrm{H} _ {q} (\mathrm{V}) \rightarrow \mathrm{H} _ {q} (\mathrm{V}, \mathrm{W}) \rightarrow \mathrm{H} _ {q - 1} (\mathrm{W}) \rightarrow \dots
$$

where the connecting map is of degree - 1.

Since $\mathbf{H}_{\lambda}^{n}$ is defined as a cohomology theory, i.e. from a cochain complex, the long exact sequence

$$
\begin{array}{r l}&\rightarrow \mathrm{H} _ {\lambda} ^ {q} (\mathbf {C} ^ {\infty} (\mathrm{W})) \rightarrow \mathrm{H} _ {\lambda} ^ {q} (\mathbf {C} ^ {\infty} (\mathrm{V})) \rightarrow \mathrm{H} _ {\lambda} ^ {q} (\mathbf {C} ^ {\infty} (\mathrm{V}), \mathbf {C} ^ {\infty} (\mathrm{W}))\\&\quad \xrightarrow {\partial} \mathrm{H} _ {\lambda} ^ {q + 1} (\mathbf {C} ^ {\infty} (\mathrm{W})) \rightarrow \dots\end{array}
$$

has a connecting map of degree + 1. So one may wonder how this is compatible with theorem 46. The point is that the connecting map for the long exact sequence of Hochschild cohomology groups is o (any current on W whose image in V is zero, does vanish), thus $\operatorname{Im}(\partial) \subset \mathrm{SH}_{\lambda}^{q-1}(\mathbf{C}^{\infty}(\mathbf{W}))$.

d) Only very trivial cyclic cocycles on  $\mathbf{C}^{\infty}(\mathbf{V})$  do extend continuously to the  $C^{*}$ -algebra  $\mathbf{C}(\mathbf{V})$  of continuous functions on a compact manifold. In fact for any compact space X the continuous Hochschild cohomology of  $\mathcal{A} = \mathbf{C}(\mathbf{X})$  with coefficients in the bimodule  $A^{*}$  is trivial in dimension  $n \geq 1$  (cf. [35]). Thus by theorem 37 the cyclic cohomology of A is given by  $\mathrm{H}_{\lambda}^{2n}(\mathcal{A}) = \mathrm{H}_{\lambda}^{0}(\mathcal{A})$  and  $\mathrm{H}_{\lambda}^{2n+1}(\mathcal{A}) = 0$ . This remark extends to arbitrary nuclear  $C^{*}$  algebras [51].

Example 2. — $\mathcal{A} = \mathcal{A}_{\theta}$, $\theta \in \mathbf{R}/\mathbf{Z}$. (Cf. [16] [19] [55] [58].) Let $\lambda = \exp 2\pi i\theta$. Denote by $\mathcal{S}(\mathbf{Z}^2)$ the space of sequences $(a_{n,m})_{n,m \in \mathbb{Z}^{\bullet}}$ of rapid decay (i.e. $(|n| + |m|)^q |a_{n,m}|$ is bounded for any $q \in \mathbf{N}$).

Let $\mathcal{A}_{\theta}$ be the algebra whose generic element is a formal sum $\sum a_{n,m} U_1^n U_2^m$, where $(a_{n,m}) \in \mathcal{S}(\mathbf{Z}^2)$ and the product is specified by the equality $U_2 U_1 = \lambda U_1 U_2$.

For $\theta \in \mathbf{Q}$ this algebra is Morita equivalent, in the sense of corollary 24, to the commutative algebra of smooth functions on the 2-torus. Thus in the case $\theta \in \mathbf{Q}$, the computation of $\mathrm{H}^{*}(\mathcal{A}_{\theta})$ follows from theorem 46.

We shall now do the computation for arbitrary  $\theta$ . The first step is to compute the Hochschild cohomology  $\mathrm{H}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*})$ , where of course  $A_{\theta}$  is considered as a locally convex topological algebra (using the seminorms  $p_{q}(a)=\operatorname{Sup}(\mathrm{i}+|n|+|m|)^{q}|a_{n,m}|$ ).

Let us describe a topological projective resolution of $\mathcal{A}_{\theta}$ viewed as a module over $\mathcal{B} = \mathcal{A}_{\theta} \hat{\otimes}_{\pi} \mathcal{A}_{\theta}^{0}$. Put $\mathcal{M}_{i} = \mathcal{B} \otimes \Omega_{i}$ where $\Omega = \Omega_{0} \oplus \Omega_{1} \oplus \Omega_{2}$ is the exterior algebra over the 2-dimensional vector space $\Omega_{1} = \mathbf{C}^{2}$ with canonical basis $e_{1}, e_{2}$.

For $j = 1, 2$ let $b_j: \mathcal{M}_j \to \mathcal{M}_{j+1}$ be the $\mathcal{B}$-linear map such that

$$
b _ {1} (\mathrm{I} \otimes e _ {j}) = \mathrm{I} \otimes \mathring {\mathrm{U}} _ {j} - \mathrm{U} _ {j} \otimes \mathrm{I}, \quad j = \mathrm{I}, 2.
$$

$$
b _ {2} \left(\mathrm{I} \otimes \left(e _ {1} \wedge e _ {2}\right)\right) = \left(\mathrm{U} _ {2} \otimes \mathrm{I} - \lambda \otimes \bar {\mathrm{U}} _ {2}\right) \otimes e _ {1} - \left(\lambda \mathrm{U} _ {1} \otimes \mathrm{I} - \mathrm{I} \otimes \mathrm{U} _ {1} ^ {0}\right) \otimes e _ {2}.
$$

As usual, let $\varepsilon : \mathcal{B} \to \mathcal{A}_{\theta}$ be given by $\varepsilon(a \otimes b) = ab$ for $a, b \in \mathcal{A}_{\theta}$.

Lemma 48. — a) $(\mathcal{M}_i, b_i)$ is a projective resolution of the module $\mathcal{A}_{\theta}$.

$$
b) \mathrm{H} ^ {i} (\mathscr {A} _ {\theta}, \mathscr {A} _ {\theta} ^ {*}) = 0 f o r i > 2.
$$

Proof. — For  $\nu = (n_{1}, n_{2}) \in \mathbf{Z}^{2}$ , let  $U^{\nu} = U_{1}^{n_{1}} U_{2}^{n_{2}} \in A_{0}$ ,  $X^{\nu} = U^{\nu} \otimes I \in B$  and  $Y^{\nu} = I \otimes \mathring{U}^{\nu} \in B$ . Then  $X^{\nu}$  and  $Y^{\nu'}$  commute for any  $\nu, \nu'$  and any element of B is of the form

$$
x = \Sigma a _ {\nu , \nu^ {\prime}} X ^ {\nu} Y ^ {\nu^ {\prime}},
$$

where the sequence $(a_{\nu, \nu'})$ is an arbitrary element of $\mathcal{S}(\mathbf{Z}^4)$.

One has $\mathbf{X}^{\nu}\mathbf{X}^{\nu^{\prime}} = \lambda^{n_{2}n_{1}^{\prime}}\mathbf{X}^{\nu +\nu^{\prime}},\quad \mathbf{Y}^{\nu}\mathbf{Y}^{\nu^{\prime}} = \lambda^{n_{2}^{\prime}n_{1}}\mathbf{Y}^{\nu +\nu^{\prime}}.$

Let us check that $\operatorname{Ker} \varepsilon = \operatorname{Im} b_1$. The inclusion $\operatorname{Im} b_1 \subset \operatorname{Ker} \varepsilon$ is clear. For $x = \sum a_{v, v'} X^v Y^{v'}$, $\varepsilon(x) = 0$ implies $\sum a_{v, v'} X^v X^{v'} = 0$ i.e. $x = \sum a_{v, v'} X^v (Y^{v'} - X^{v'})$. Using the equality

$$
\begin{array}{r l} \left(\mathrm{I} \otimes \mathring {\mathrm{U}} _ {2} ^ {n _ {2}}\right) \left(\mathrm{I} \otimes \mathring {\mathrm{U}} _ {1} ^ {n _ {1}}\right) - \left(\mathrm{U} _ {1} ^ {n _ {1}} \otimes \mathrm{I}\right) \left(\mathrm{U} _ {2} ^ {n _ {2}} \otimes \mathrm{I}\right) & = \left(\mathrm{I} \otimes \mathring {\mathrm{U}} _ {2} ^ {n _ {2}}\right) \left(\sum_ {0} ^ {n _ {1} - 1} \mathrm{U} _ {1} ^ {j} \otimes \mathring {\mathrm{U}} _ {1} ^ {n _ {1} - 1 - j}\right) \left(\mathrm{I} \otimes \mathrm{U} _ {1} - \mathrm{U} _ {1} \otimes \mathrm{I}\right) \\ & + \left(\mathrm{U} _ {1} ^ {n _ {1}} \otimes \mathrm{I}\right) \left(\sum_ {0} ^ {n _ {2} - 1} \mathrm{U} _ {2} ^ {j} \otimes \mathrm{U} _ {2} ^ {n _ {2} - 1 - j}\right) \left(\mathrm{I} \otimes \mathrm{U} _ {2} - \mathrm{U} _ {2} \otimes \mathrm{I}\right), \end{array}
$$

we see that the left ideal $\operatorname{Ker} \varepsilon$ is generated by $\mathbf{i} \otimes \mathbf{U}_1 - \mathbf{U}_1 \otimes \mathbf{i}$ and $\mathbf{i} \otimes \mathbf{U}_2 - \mathbf{U}_2 \otimes \mathbf{i}$ and hence is equal to $\operatorname{Im} b_1$.

Next, one checks that $b_{1}b_{2} = 0$. Given $x = x_{1}\otimes e_{1} - x_{2}\otimes e_{2}\in \operatorname{Ker}b_{1}$, one has $x_{1}(\mathrm{I}\otimes \mathring{\mathrm{U}}_{1} - \mathrm{U}_{1}\otimes \mathrm{I}) = x_{2}(\mathrm{I}\otimes \mathring{\mathrm{U}}_{2} - \mathrm{U}_{2}\otimes \mathrm{I})$. To prove that $x\in \operatorname{Im}b_{2}$ it is enough to find $y\in \mathcal{B}$ such that $x_{1} = y(\mathrm{U}_{2}\otimes \mathrm{I} - \lambda \otimes \mathring{\mathrm{U}}_{2})$.

With $Z = \lambda U_2^{-1} \otimes \mathring{U}_2$ one first proves that $x_1(\sum_{-\infty}^{\infty} Z^k) = 0$, using the relation

$$
\begin{array}{r l} x _ {1} (\sum_ {- \infty} ^ {\infty} Z ^ {k}) (I \otimes \mathring {U} _ {1} - U _ {1} \otimes I) & = x _ {1} (I \otimes \mathring {U} _ {1} - U _ {1} \otimes I) \sum_ {- \infty} ^ {\infty} (U _ {2} ^ {- 1} \otimes \mathring {U} _ {2}) ^ {k} \\ & = x _ {2} (I \otimes \mathring {U} _ {2} - U _ {2} \otimes I) \sum_ {- \infty} ^ {\infty} (U _ {2} ^ {- 1} \otimes \mathring {U} _ {2}) ^ {k} = 0. \end{array}
$$

Then writing $x_{1} = \Sigma a_{k}Z^{k}$, where $(a_{k})$ is a sequence of rapid decay of elements of the closed subalgebra of $\mathcal{B}$ generated by $U_{1}\otimes I, I\otimes \mathring{U}_{1}, U_{2}\otimes I$, one gets

$$
x _ {1} = \sum a _ {k} (Z ^ {k} - 1) = \sum a _ {k} (\sum_ {0} ^ {k - 1} Z ^ {j}) (Z - 1) = y _ {1} (Z - 1).
$$

Finally the injectivity of $b_{2}$ is immediate.

Using this resolution one easily computes  $\mathrm{H}^{i}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*})$ . We say (cf. [32]) that  $\theta$  satisfies a diophantine condition if the sequence  $|I-\lambda^{n}|^{-1}$  is  $\mathrm{O}(n^{k})$  for some k.

Proposition 49. — a) Let $\theta \notin \mathbf{Q}$. One has $\mathrm{H}^0 (\mathcal{A}_\theta ,\mathcal{A}_\theta^*) = \mathbf{C}$.

b) If $\theta \notin \mathbf{Q}$ satisfies a diophantine condition, then $\mathrm{H}^j (\mathcal{A}_\theta ,\mathcal{A}_\theta^*)$ is of dimension 2 for $j = 1$, and of dimension 1 for $j = 2$.

c) If $\theta \notin \mathbf{Q}$ does not satisfy a diophantine condition, then $\mathbf{H}^1$, $\mathbf{H}^2$ are infinite dimensional non Hausdorff spaces.

(Recall that by theorem 46, $\mathbf{H}^j (\mathcal{A}_\theta ,\mathcal{A}_\theta^*)$ is infinite dimensional for $j\leq 2$ when $\theta \in \mathbf{Q}$.)

Proof. — We have to compute the cohomology of the complex  $(\operatorname{Hom}_{\mathcal{B}}(\mathcal{M}_{i}, \mathcal{A}_{\theta}^{*}), b_{i}^{t})$ . The map  $\mathrm{T} \in \operatorname{Hom}_{\mathcal{B}}(\mathcal{B}, \mathcal{A}_{\theta}^{*}) \to \mathrm{T}(\mathrm{I}) \in \mathcal{A}_{\theta}^{*}$  allows to identify  $\operatorname{Hom}_{\mathcal{B}}(\mathcal{M}_{i}, \mathcal{A}_{\theta}^{*})$  with

$\mathcal{A}_{\theta}^{*}\otimes \Omega_{i}^{*}$ . Moreover, using the canonical trace $\tau$ on $\mathcal{A}_{\theta}$ ， $\tau (\Sigma a_{\nu}\mathrm{U}^{\nu}) = a_{(0,0)}$ one can identify $\mathcal{A}_{\theta}^{*}$ with the space of formal sums

$$
\varphi = \Sigma a _ {\nu} U ^ {\nu},
$$

where $(a_{v})_{v\in \mathbf{Z}^{n}}$ is a tempered sequence of complex numbers $(|a_{n,m}|\leq \mathbf{C}(|n| + |m|)^{\beta}$ for some $\mathbf{C}$ and $\beta)$. The linear functional is given by $\langle \varphi ,x\rangle = \tau (\varphi x)$ for $x\in \mathcal{A}_{\theta}$.

With these notations, the above complex becomes

$$
\mathcal {A} _ {\theta} ^ {*} \xrightarrow {\alpha_ {1}} \mathcal {A} _ {\theta} ^ {*} \oplus \mathcal {A} _ {\theta} ^ {*} \xrightarrow {\alpha_ {2}} \mathcal {A} _ {\theta} ^ {*} \to 0
$$

where

$$
\alpha_ {1} (\varphi) = ((\mathbf {U _ {1}} \varphi - \varphi \mathbf {U _ {1}}), (\mathbf {U _ {2}} \varphi - \varphi \mathbf {U _ {2}}))
$$

and

$$
\alpha_ {2} \left(\varphi_ {1}, \varphi_ {2}\right) = U _ {2} \varphi_ {1} - \lambda \varphi_ {1} U _ {2} - \left(\lambda U _ {1} \varphi_ {2} - \varphi_ {2} U _ {1}\right).
$$

Since $\lambda \notin \mathbf{Q}$ one easily gets $\operatorname{Ker} \alpha_{1} = \mathbf{C}$, which gives a).

For $(\varphi_{1},\varphi_{2})\in \operatorname {Ker}\alpha_{2}$, one has $\mathbf{U}_2\varphi_1 - \lambda \varphi_1\mathbf{U}_2 = \lambda \mathbf{U}_1\varphi_2 - \varphi_2\mathbf{U}_1$ and the coefficients $a_{\nu}$ of $\varphi = \sum a_{\nu}\mathbf{U}^{\nu}$ are uniquely determined by the conditions

$$
a _ {(0, 0)} = 0, \quad \mathrm{U} _ {1} \varphi - \varphi \mathrm{U} _ {1} = \varphi_ {1}, \quad \mathrm{U} _ {2} \varphi - \varphi \mathrm{U} _ {2} = \varphi_ {2}.
$$

Indeed one has $(\mathrm{I} - \lambda^{n_2})a_{n_1 - 1,n_2} = a_{n_1,n_2}^1$ and $(\lambda^{n_1} - \mathrm{I})a_{n_1,n_2 - 1} = a_{n_1,n_2}^2$. For these conditions to be compatible one needs

$$
a _ {n, 0} ^ {1} = \mathrm{o} \forall n; \quad a _ {0, n} ^ {2} = \mathrm{o} \forall n; \quad a _ {n _ {1} + 1, n _ {2}} ^ {1} (\mathrm{I} - \lambda^ {n _ {2}}) ^ {- 1} = a _ {n _ {1}, n _ {2} + 1} ^ {2} (\lambda^ {n _ {1}} - \mathrm{I}) ^ {- 1}
$$

$$
\text { for } n _ {1} \neq 0, n _ {2} \neq 0.
$$

From the hypothesis $\alpha_{2}(\varphi_{1},\varphi_{2}) = 0$ one gets

$$
\left(\lambda^ {n _ {1}} - \mathrm{I}\right) a _ {n _ {1} + 1, n _ {2}} ^ {1} = \left(\mathrm{I} - \lambda^ {n _ {3}}\right) a _ {n _ {1}, n _ {2} + 1} ^ {2} \quad \forall n _ {1}, n _ {2}.
$$

Thus the compatibility conditions are: $a_{1,0}^{1} = 0$, $a_{0,1}^{2} = 0$.

If $\theta$ satisfies a diophantine condition, the sequence $(a_{\nu})$ is automatically tempered, which shows that $\mathbf{H}^1 (\mathcal{A}_\theta ,\mathcal{A}_\theta^*) = \mathbf{C}^2$.

If $\theta$ does not satisfy a diophantine condition, then by choosing say the pair $(\varphi_{1}, 0)$ where $\varphi_{1} = \sum_{n \neq 0} U_{1} U_{2}^{n}$, one checks that the compatibility conditions are fulfilled but that $(a_{v})$ is not tempered. This proves b), c) for $H^{1}$; the proofs for $H^{2}$ are similar. $\square$

At this point, it might seem hopeless to compute  $\mathrm{H}^{*}(\mathcal{A}_{\theta})$  (cf. definition 16) when  $\theta$  is an irrational number not satisfying a diophantine condition, since the Hochschild cohomology is already quite complicated. We shall see however that even in that case, where  $\mathrm{H}^{*}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*})$  is infinite dimensional non Hausdorff, the homology of the complex  $(\mathrm{H}^{n}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*}),\mathrm{I}\circ\mathrm{B})$  is still finite dimensional. The first thing is to translate I o B in the resolution used above. Before we begin the computations we can already state a corollary of proposition 49 and theorem 37:

Corollary 50. — $(\theta \notin \mathbf{Q})$. One has $\mathrm{H}_{\lambda}^{0}(\mathcal{A}_{\theta}) = \mathbf{C}$ and the map

$$
\mathrm{I}: \mathrm{H} _ {\lambda} ^ {1} (\mathscr {A} _ {\theta}) \rightarrow \mathrm{H} ^ {1} (\mathscr {A} _ {\theta}, \mathscr {A} _ {\theta} ^ {*})
$$

is an isomorphism.

(Thus in particular any 1-dimensional current is closed.)

Proof. — By proposition 49, a) one has  $\mathrm{H}_{\lambda}^{0}(\mathcal{A}_{\theta})=\mathrm{H}^{0}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*})=\mathbf{C}$ . By theorem 37 the following sequence is exact:

$$
\mathrm{o} \rightarrow \mathrm{H} _ {\lambda} ^ {1} (\mathscr {A} _ {\theta}) \xrightarrow {\mathrm{I}} \mathrm{H} ^ {1} (\mathscr {A} _ {\theta}, \mathscr {A} _ {\theta} ^ {*}) \xrightarrow {\mathrm{B}} \mathrm{H} _ {\lambda} ^ {0} (\mathscr {A} _ {\theta}) \xrightarrow {\mathrm{S}} \mathrm{H} _ {\lambda} ^ {2} (\mathscr {A} _ {\theta}).
$$

Since the image by S of the generator $\tau$ of $\mathrm{H}_{\lambda}^{0}(\mathcal{A}_{\theta})$ is non zero (it pairs non trivially with $1 \in \operatorname{Proj} \mathcal{A}_{\theta}$) one gets $B = 0$.

Lemma 51. — Let $\varphi \in \mathcal{A}_{\theta}^{*} / \mathrm{Im}\alpha_{2} = \mathrm{H}^{2}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*})$ ; then

$$
(\mathbf {I} \circ \mathbf {B}) (\varphi) \in \mathrm{H} ^ {1} (\mathcal {A} _ {\theta}, \mathcal {A} _ {\theta} ^ {*}) = \operatorname{Ker} \alpha_ {2} / \operatorname{Im} \alpha_ {1}
$$

is the class of $(\varphi_{1},\varphi_{2})$ where

and

$$
\begin{array}{l} \left(\varphi_ {1}\right) _ {n, m} = - \lambda^ {- 1} \left(\mathrm{I} - \lambda^ {(n - 1) m}\right) \left(\mathrm{I} - \lambda^ {n - 1}\right) ^ {- 1} \varphi_ {n, m + 1} \\ \left(\varphi_ {2}\right) _ {n, m} = \lambda^ {- 1} \left(\mathrm{I} - \lambda^ {n (m - 1)}\right) \left(\mathrm{I} - \lambda^ {m - 1}\right) ^ {- 1} \varphi_ {n + 1, m}. \end{array}
$$

Proof. — To do the computation we first have to compare the projective resolution of lemma 48 with the standard resolution  $(\mathcal{M}_{k}^{\prime} = \mathcal{B} \widehat{\otimes}_{\pi} \mathcal{A}_{\theta}^{\otimes k} \ldots)$ , i.e. to find morphisms  $h : M \to M'$  and  $k : M' \to M$  of complexes of B-modules which are the identity in degree o. Recall that

$$
\begin{array}{r l} b _ {n} ^ {\prime} (\mathrm{I} \otimes a _ {1} \otimes \dots \otimes a _ {n}) & = (a _ {1} \otimes \mathrm{I}) \otimes (a _ {2} \otimes \dots \otimes a _ {n}) \\ & + \sum_ {j = 1} ^ {n - 1} (- \mathrm{I}) ^ {j} \mathrm{I} \otimes a _ {1} \otimes \dots a _ {j} a _ {j + 1} \otimes \dots \otimes \dots \otimes a ^ {n} \\ & + (- \mathrm{I}) ^ {n} (\mathrm{I} \otimes a _ {n} ^ {0}) \otimes (a _ {1} \otimes \dots \otimes a _ {n - 1}). \end{array}
$$

The module map $h_1$ is determined by $h_1(\mathbf{i} \otimes e_j)$ which must satisfy

$$
b ^ {\prime} h _ {1} (\mathrm{I} \otimes e _ {j}) = b _ {1} (\mathrm{I} \otimes e _ {j}) = \mathrm{I} \otimes \mathrm{U} _ {j} ^ {0} - \mathrm{U} _ {j} \otimes \mathrm{I};
$$

thus we can take $h_{1}(\mathbf{i} \otimes e_{j}) = \mathbf{i} \otimes \mathbf{U}_{j}$.

One determines in a similar way (but we do not need it for the lemma) $h_2(\mathbf{I} \otimes (e_1 \wedge e_2)) = \mathbf{I} \otimes \mathbf{U}_2 \otimes \mathbf{U}_1 - \lambda \mathbf{I} \otimes \mathbf{U}_1 \otimes \mathbf{U}_2$.

The module map $k_{1}:\mathcal{B}\widehat{\otimes}_{\pi}\mathcal{A}_{\theta}\to \mathrm{B}\otimes \Omega_{1}$ is determined by $k_{1}(\mathrm{I}\otimes \mathrm{U}^{\nu})$ ($\nu = (n_1,n_2)$) which must satisfy $b_{1}(k_{1}(\mathrm{I}\otimes \mathrm{U}^{\nu})) = b_{1}'(\mathrm{I}\otimes \mathrm{U}^{\nu}) = \mathrm{U}^{\nu}\otimes \mathrm{I} - \mathrm{I}\otimes (\mathrm{U}^{\nu})^{0}$.

As in the proof of lemma 48 we take $k_1(\mathbf{I} \otimes \mathbf{U}^\nu) = \mathbf{A}_\nu \otimes e_1 + \mathbf{B}_\nu \otimes e_2$ where $\mathbf{A}_\nu = \mathring{\mathbf{U}}_2^{n_1}(\mathbf{U}_1^{n_1} - \mathring{\mathbf{U}}_1^{n_1})(\mathbf{U}_1 - \mathring{\mathbf{U}}_1)^{-1}, \mathbf{B}_\nu = \mathbf{U}_1^{n_1}(\mathbf{U}_2^{n_1} - \mathring{\mathbf{U}}_2^{n_1})(\mathbf{U}_2 - \mathring{\mathbf{U}}_2)^{-1}$ where to simplify notation we omit the tensor product signs (i.e. $\mathbf{U}_j, \mathring{\mathbf{U}}_j$ mean $\mathbf{U}_j \otimes \mathbf{I}, \mathbf{I} \otimes \mathring{\mathbf{U}}_j$).

Now the module map $k_2: \mathcal{M}_2' \to \mathcal{M}_2$ is uniquely determined by the equality $b_2 k_2 = k_1 b_2'$ since $\mathcal{M}_3 = 0$.

A tedious but straightforward computation gives:

$$
k _ {2} (\mathrm{I} \otimes \mathrm{U} ^ {\nu} \otimes \mathrm{U} ^ {\mu}) = \mathrm{U} _ {1} ^ {n _ {1}} \frac {\lambda^ {n _ {3} m _ {1}} \mathrm{U} _ {1} ^ {m _ {1}} - \lambda^ {- m _ {1} m _ {2}} \stackrel {\circ} {\mathrm{U}} _ {2} ^ {m _ {1}}}{\lambda^ {n _ {3}} \mathrm{U} _ {1} - \lambda^ {- m _ {3}} \stackrel {\circ} {\mathrm{U}} _ {1}} \frac {\mathrm{U} _ {2} ^ {n _ {3}} - \lambda^ {n _ {3}} \stackrel {\circ} {\mathrm{U}} _ {2} ^ {n _ {3}}}{\mathrm{U} _ {2} - \lambda \stackrel {\circ} {\mathrm{U}} _ {2}} \stackrel {\circ} {\mathrm{U}} _ {2} ^ {m _ {3}} \otimes (e _ {1} \wedge e _ {2}).\tag{351}
$$

In fact we shall only need the special cases

a) $\nu = (\mathrm{I},\mathrm{o}),\quad \mu$ arbitrary,

b) v arbitrary, $\mu = (0, 0)$,

c) v arbitrary, $\mu = (\mathrm{I},\mathrm{o})$

one may as well check directly that $k_{2} = 0$ in cases a), b) (compute $k_{1}b_{2}^{\prime}$) and that

$$
k _ {2} (\mathrm{I} \otimes \mathrm{U} ^ {\nu} \otimes \mathrm{U} _ {1}) = \mathrm{U} _ {1} ^ {n _ {1}} \left(\mathrm{U} _ {2} ^ {n _ {2}} - \lambda^ {n _ {2}} \stackrel {\circ} {\mathrm{U}} _ {2} ^ {n _ {2}}\right) \left(\mathrm{U} _ {2} - \lambda \stackrel {\circ} {\mathrm{U}} _ {2}\right) ^ {- 1} \otimes \left(e _ {1} \wedge e _ {2}\right).
$$

We thus have determined the morphisms h and k. They yield the morphisms

$$
k _ {2} ^ {*}: \operatorname{Hom} _ {\mathcal {B}} (\mathcal {M} _ {2}, \mathcal {A} _ {\theta} ^ {*}) \rightarrow \operatorname{Hom} _ {\mathcal {B}} (\mathcal {M} _ {2} ^ {\prime}, \mathcal {A} _ {\theta} ^ {*}),
$$

$$
h _ {1} ^ {*}: \operatorname{Hom} _ {\mathcal {B}} (\mathcal {M} _ {1} ^ {\prime}, \mathcal {A} _ {\theta}) \to \operatorname{Hom} _ {\mathcal {B}} (\mathcal {M} _ {1}, \mathcal {A} _ {\theta} ^ {*}),
$$

and we want to compute the composition

$$
\alpha = h _ {1} ^ {*} (\mathrm{I} \circ \mathrm{B}) k _ {2} ^ {*}: \mathcal {A} _ {\theta} ^ {*} \rightarrow \mathcal {A} _ {\theta} ^ {*} \oplus \mathcal {A} _ {\theta} ^ {*}.
$$

Let $\varphi \in \mathcal{A}_{\theta}^{*}$ and let $\widetilde{\varphi}$ be the corresponding element of $\operatorname{Hom}_{\mathcal{B}}(\mathcal{M}_2, \mathcal{A}_{\theta}^{*})$:

$$
\widetilde {\varphi} (a \otimes b ^ {0} \otimes e _ {1} \wedge e _ {2}) (x) = \varphi (b x a) \quad \forall a, b, x \in \mathscr {A} _ {\theta}.
$$

Let $\psi = k_2^*\widetilde{\varphi} = \widetilde{\varphi}\circ k_2$ . One has

$$
\psi (x ^ {0}, x ^ {1}, x ^ {2}) = \widetilde {\varphi} (k _ {2} (\mathrm{I} \otimes x ^ {1} \otimes x ^ {2})) (x ^ {0}) \quad \forall x ^ {0}, x ^ {1}, x ^ {2} \in \mathscr {A} _ {\theta}.
$$

Let $\psi_{1} = (\mathbf{I}\circ \mathbf{B})\psi .$ One has by definition, for $x^0,x^1\in \mathcal{A}_\theta$

$$
\psi_ {1} (x ^ {0}, x ^ {1}) = \psi (\mathrm{I}, x ^ {0}, x ^ {1}) - \psi (x ^ {0}, x ^ {1}, \mathrm{I}) - \psi (\mathrm{I}, x ^ {1}, x ^ {0}) + \psi (x ^ {1}, x ^ {0}, \mathrm{I}).
$$

Using b) one gets that $\psi(x^0, x^1, 1) = 0$ for $x^0, x^1 \in \mathcal{A}_\theta$; thus

$$
\psi_ {1} (x ^ {0}, x ^ {1}) = \psi (\mathrm{I}, x ^ {0}, x ^ {1}) - \psi (\mathrm{I}, x ^ {1}, x ^ {0}) \quad \forall x ^ {0}, x ^ {1} \in \mathscr {A} _ {\theta}.
$$

Let then $\alpha (\varphi) = (\varphi_1,\varphi_2)$. One has $\alpha (\varphi) = h_1^*\psi_1$; thus

$$
\varphi_ {j} (x) = \psi_ {1} (x, U _ {j}) = \psi (I, x, U _ {j}) - \psi (I, U _ {j}, x) \quad \forall x \in \mathscr {A} _ {\theta}, j = I, 2.
$$

Let us compute $\varphi_j(U^\nu)$, $\nu = (n_1, n_2)$, $j = 1, 2$. Using a), we have

$$
\varphi_ {1} (\mathbf {U} ^ {\nu}) = \psi (\mathrm{I}, \mathbf {U} ^ {\nu}, \mathbf {U} _ {1}).
$$

Using c) we have

$$
\begin{array}{l l} \varphi_ {1} (\mathbf {U} ^ {\nu}) = \psi (\mathrm{I}, \mathbf {U} ^ {\nu}, \mathbf {U} _ {1}) = \widetilde {\varphi} (k _ {2} (\mathrm{I} \otimes \mathbf {U} ^ {\nu} \otimes \mathbf {U} _ {1})) (\mathrm{I}) \\ = \left\{ \begin{array}{l l} (\mathrm{I} - \lambda^ {(n _ {1} + 1) n _ {2}}) (\mathrm{I} - \lambda^ {(n _ {1} + 1)}) ^ {- 1} \varphi (\mathbf {U} _ {1} ^ {n _ {1}} \mathbf {U} _ {2} ^ {n _ {2} - 1}) & \text { if } n _ {2} \neq 0, \\ 0 & \text { if } n _ {2} = 0. \end{array} \right. \end{array}
$$

The knowledge of $\varphi_{1}(\mathbf{U}^{\nu})$, $\forall \nu \in \mathbf{Z}^{2}$, determines the coefficients $a_{\nu}^{1}$ of $\varphi_{1} = \Sigma a_{\nu}^{1} \mathbf{U}^{\nu}$ by the equality

$$
a _ {\nu} ^ {1} = \lambda^ {n _ {1} n _ {2}} \varphi_ {1} (\mathrm{U} ^ {- \nu}).
$$

Hence we get

$$
a _ {n, m} ^ {1} = \lambda^ {n m} (\mathrm{I} - \lambda^ {(n - 1) m}) (\mathrm{I} - \lambda^ {- (n - 1)}) ^ {- 1} \lambda^ {n (- m - 1)} a _ {n, m + 1},
$$

where $\varphi = \Sigma a_{\nu} U^{\nu}$.

The computation of $\varphi_{2} = \Sigma a_{\nu}^{2}\mathrm{U}^{\nu}$ is done in a similar way.

352

We are now ready to determine the kernel and the image of $\mathbf{I} \circ \mathbf{B}$. Let $\varphi \in \mathcal{A}^*/\mathrm{Im} \, \alpha_2 \in \mathrm{H}^2(\mathcal{A}_\theta, \mathcal{A}_\theta^*)$ be such that $(\mathbf{I} \circ \mathbf{B}) \, \varphi \in \mathrm{Im} \, \alpha_1$. Let thus $\psi = \Sigma b_{\nu} U^{\nu} \in \mathcal{A}_\theta^*$ with $\alpha_1(\psi) = (\mathbf{I} \circ \mathbf{B}) \, \varphi$. Then

$$
\begin{array}{l} \text { I) } (I - \lambda^ {n _ {2}}) b _ {n _ {1} - 1, n _ {2}} = - \lambda^ {- 1} (I - \lambda^ {(n _ {1} - 1) n _ {2}}) (I - \lambda^ {n _ {1} - 1}) ^ {- 1} a _ {n _ {1}, n _ {2} + 1}, \\ 2) (I - \lambda^ {n _ {1}}) b _ {n _ {1}, n _ {2} - 1} = - \lambda^ {- 1} (I - \lambda^ {n _ {1} (n _ {2} - 1)}) (I - \lambda^ {n _ {2} - 1}) ^ {- 1} a _ {n _ {1} + 1, n _ {2}}. \end{array}
$$

So the image $(\mathbf{I} \circ \mathbf{B}) \varphi \in \mathrm{H}^1(\mathcal{A}_\theta, \mathcal{A}_\theta^*)$ is o if and only if the following sequence is tempered: $c_{n,m} = (\mathrm{I} - \lambda^{nm})(\mathrm{I} - \lambda^n)^{-1}(\mathrm{I} - \lambda^m)^{-1}a_{n+1,m+1}$.

$$
\varphi \in
$$

$$
\alpha_ {2}
$$

$$
\left(c _ {n, m} ^ {j}\right), j = 1, 2,
$$

$$
\left(\lambda^ {n} - \mathrm{I}\right) c _ {n + 1, m} ^ {1} + \left(\lambda^ {m} - \mathrm{I}\right) c _ {n, m + 1} ^ {2} = a _ {n + 1, m + 1},
$$

$$
a _ {1, 1} = 0
$$

$$
\left(\left| \lambda^ {n} - \mathrm{I} \right| + \left| \lambda^ {m} - \mathrm{I} \right|\right) ^ {- 1} a _ {n + 1, m + 1}.
$$

Thus the next lemma shows that in all cases the kernel of I $\circ$ B is one-dimensional.

Lemma 52. — For any $\theta \notin \mathbf{Q}$, and $(n, m) \in \mathbf{Z}^2$, $(n, m) \neq (0, 0)$, one has

$$
\left(\left| \lambda^ {n} - \mathrm{I} \right| + \left| \lambda^ {m} - \mathrm{I} \right|\right) ^ {- 1} \leq \frac {| m |}{2} + \left| \mathrm{I} - \lambda^ {n m} \right| \left| \mathrm{I} - \lambda^ {n} \right| ^ {- 1} \left| \mathrm{I} - \lambda^ {m} \right| ^ {- 1}
$$

with $\lambda = e^{2\pi i\theta}$.

Proof. — For $n = 0$, $|(\mathrm{I} - \lambda^{nm})(\mathrm{I} - \lambda^n)^{-1}|$ is equal to $|m| \geq \mathrm{I}$ so that the inequality is obvious. Thus we may assume that $n \neq 0$, $m \neq 0$. If $|\mathrm{I} - \lambda^{nm}| \geq |\mathrm{I} - \lambda^n|$ the inequality is again obvious, thus one can assume $|\mathrm{I} - \lambda^{nm}| < |\mathrm{I} - \lambda^n|$. With $\lambda^n = e^{i\alpha}$, $\alpha \in [-\pi, \pi[$, one has $|\mathrm{I} - e^{im\alpha}| < |\mathrm{I} - e^{i\alpha}|$ with $m \neq 0$, thus $|m\alpha| \geq \pi$, $|e^{i\alpha} - \mathrm{I}| \geq 2 / m$.

Let us now look for the image of $\mathbf{I} \circ \mathbf{B}$ in $\mathrm{H}^1(\mathcal{A}_\theta, \mathcal{A}_\theta^*) = \operatorname{Ker} \alpha_2 / \operatorname{Im} \alpha_1$. Any pair $(\varphi_1, \varphi_2) \in \operatorname{Im}(\mathbf{I} \circ \mathbf{B}) + \operatorname{Im} \alpha_1$ satisfies $a_{1,0}^1 = 0$, $a_{0,1}^2 = 0$ (using lemma 51). Conversely, if $a_{1,0}^1 = a_{0,1}^2 = 0$, let us find $\varphi \in \mathcal{A}_\theta^*$ ($\varphi = \Sigma a_\nu U^\nu$) and $\psi \in \mathcal{A}_\theta^*$ ($\psi = \Sigma b_\nu U^\nu$) so that, with the notation of lemma 51, one has

$$
(\varphi_ {1}, \varphi_ {2}) = \alpha_ {1} (\psi) + (I \circ B) \varphi .
$$

This means:

$$
\begin{array}{l} \text {I)} a _ {n, m} ^ {1} = (\text {I} - \lambda^ {m}) b _ {n - 1, m} - \lambda^ {- 1} (\text {I} - \lambda^ {(n - 1) m}) (\text {I} - \lambda^ {n - 1}) ^ {- 1} a _ {n, m + 1}, \\ 2) a _ {n, m} ^ {2} = (\lambda^ {n} - \text {I}) b _ {n, m - 1} + \lambda^ {- 1} (\text {I} - \lambda^ {n (m - 1)}) (\text {I} - \lambda^ {m - 1}) ^ {- 1} a _ {n + 1, m}. \end{array}
$$

Since $\alpha_{2}(\varphi_{1},\varphi_{2}) = 0$ by hypothesis, one has $(\lambda^n -\mathrm{I})a_{n + 1,m}^1 = (\mathrm{I} - \lambda^m)a_{n,m + 1}^2.$ Thus one can find sequences $b,a$ satisfying the above equalities with

$$
\left| b _ {n, m} \right| = \left| a _ {n + 1, m + 1} \right| = (\mathrm{I} + | \mathrm{I} - \lambda^ {n m} | | \mathrm{I} - \lambda^ {n} | ^ {- 1} | \mathrm{I} - \lambda^ {m} | ^ {- 1}) ^ {- 1} \left| \frac {a _ {n + 1 , m} ^ {1}}{\mathrm{I} - \lambda^ {m}} \right|
$$

where for $m = 0$ and $n \neq 0$ the right term is replaced by $\left|\frac{a_{n,m+1}^2}{1 - \lambda^n}\right|$.

By lemma 52,

$$
\begin{array}{r l} \left| b _ {n, m} \right| & \leq (\mathrm{I} + | m |) \left(\left| \lambda^ {n} - \mathrm{I} \right| + \left| \lambda^ {m} - \mathrm{I} \right|\right) \left| a _ {n - 1, m} ^ {1} \right| \left| (\mathrm{I} - \lambda^ {m}) ^ {- 1} \right| \\ & = (\mathrm{I} + | m |) \left(\left| a _ {n + 1, m} ^ {1} \right| + \left| a _ {n, m + 1} ^ {2} \right|\right). \end{array}
$$

Thus $a, b$ are tempered and we have shown that $(\varphi_{1}, \varphi_{2})$ belongs to the image of $\mathbf{I} \circ \mathbf{B}$ in $\mathbf{H}^{1}(\mathcal{A}_{\theta}, \mathcal{A}_{\theta}^{*})$.

Theorem 53. — a) For all values of $\theta$, $\mathrm{H}^{\mathrm{ev}}(\mathcal{A}_{\theta}) \cong \mathbf{C}^{2}$ and $\mathrm{H}^{\mathrm{odd}}(\mathcal{A}_{\theta}) \cong \mathbf{C}^{2}$.

b) The map $(\varphi_{1},\varphi_{2})\in \mathrm{Ker}\alpha_{2}\mapsto (\varphi_{1}(\mathbf{U}_{1}^{-1}),\varphi_{2}(\mathbf{U}_{2}^{-1}))\in \mathbf{C}^{2}$ gives an isomorphism of $\mathrm{H}^{\mathrm{odd}}(\mathcal{A}_{\theta}) = \mathrm{H}^{1}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*}) / \mathrm{Im}(\mathrm{I}\circ \mathrm{B})$ with $\mathbf{C}^2$

c) One has $\mathrm{H}^{\mathrm{ev}}(\mathcal{A}_{\theta}) = \mathrm{H}^{2}(\mathcal{A}_{\theta})$; it is a vector space of dimension 2 with basis $\mathbf{S}\tau$ ($\tau$ the canonical trace) and the functional $\varphi$ given by

$$
\varphi (x ^ {0}, x ^ {1}, x ^ {2}) = x ^ {0} (\delta_ {1} (x ^ {1}) \delta_ {2} (x ^ {2}) - \delta_ {2} (x ^ {1}) \delta_ {1} (x ^ {2})) \quad \forall x ^ {i} \in \mathscr {A} _ {\theta}.
$$

In the last formula, $\delta_{1}$, $\delta_{2}$ are the basic derivations of $\mathcal{A}_{\theta}$: $\delta_{1}(\mathrm{U}^{\nu}) = 2\pi in_{1}\mathrm{U}^{\nu}$, $\delta_{2}(\mathrm{U}^{\nu}) = 2\pi in_{2}\mathrm{U}^{\nu}$.

Proof. — Since  $\mathrm{H}^{n}(\mathcal{A}_{\theta},\mathcal{A}_{\theta}^{*})=0$  for  $n\geq3$ , one has by theorem 37 an equality  $\mathrm{H}^{\mathrm{odd}}(\mathcal{A}_{\theta})=\mathrm{H}_{\lambda}^{3}(\mathcal{A}_{\theta})=\mathrm{H}_{\lambda}^{1}(\mathcal{A}_{\theta})/\mathrm{Im}\;\mathrm{B}$ . By corollary 50 one gets

$$
\mathrm{H} _ {\lambda} ^ {1} (\mathscr {A} _ {\theta}) / \operatorname{Im} \mathrm{B} = \mathrm{H} ^ {1} (\mathscr {A} _ {\theta}, \mathscr {A} _ {\theta} ^ {*}) / \operatorname{Im} (\mathrm{I} \circ \mathrm{B}).
$$

Thus b) follows from the above computations.

In the same way, one has $\mathrm{H}^{\mathrm{ev}}(\mathcal{A}_{\theta}) = \mathrm{H}_{\lambda}^{2}(\mathcal{A}_{\theta})$, and the exact sequence $0 \to \mathrm{H}_{\lambda}^{0}(\mathcal{A}_{\theta}) \xrightarrow{\mathrm{S}} \mathrm{H}_{\lambda}^{2}(\mathcal{A}_{\theta}) \xrightarrow{\mathrm{I}} \mathrm{H}^{2}(\mathcal{A}_{\theta}, \mathcal{A}_{\theta}^{*}) \xrightarrow{\mathrm{B}} \mathrm{H}_{\lambda}^{1}(\mathcal{A}_{\theta})$. With $\theta \notin \mathbf{Q}$ one has $\mathrm{H}_{\lambda}^{0}(\mathcal{A}_{\theta}) = \mathbf{C}$ with generator $\tau$, and using corollary 50 and the computation of $\operatorname{Ker}(\mathrm{I} \circ \mathrm{B})$, we see that the image of $\mathbf{I}$ in the above sequence is the one-dimensional subspace of $\mathrm{H}^{2}(\mathcal{A}_{\theta}, \mathcal{A}_{\theta}^{*}) = \mathcal{A}_{\theta}^{*}/\mathrm{Im} \alpha_{2}$ generated by $\mathrm{U}_{1} \mathrm{U}_{2}$ (i.e. the functional $x \mapsto \tau(x \mathrm{U}_{1} \mathrm{U}_{2}), \forall x \in \mathcal{A}_{\theta}$). Let us compute the image $\mathrm{I}(\varphi)$ of the $\varphi \in \mathrm{H}_{\lambda}^{2}(\mathcal{A}_{\theta})$ given by 53 c). Let $\widetilde{\varphi} \in \operatorname{Hom}_{\mathcal{B}}(\mathcal{M}_{2}', \mathcal{A}_{\theta}^{*})$ be given by

$$
\widetilde {\varphi} ((a \otimes b ^ {0}) \otimes x ^ {1} \otimes x ^ {2}) (x ^ {0}) = \varphi (b x ^ {0} a, x ^ {1}, x ^ {2}) \quad \forall a, b, x ^ {i} \in \mathscr {A} _ {\theta},
$$

with the notations of lemma 51. Under the identification of $\mathbf{H}^2 (\mathcal{A}_\theta ,\mathcal{A}_\theta^*)$ with $\mathcal{A}_{\theta}^{*} / \mathrm{Im}\alpha_{2},$$\mathbf{I}(\varphi)$ corresponds to the class of $\widetilde{\varphi}\circ h_2$. One has

$$
\begin{array}{r l} \widetilde {\varphi} (h _ {2} (\mathrm{I} \otimes e _ {1} \wedge e _ {2})) (x ^ {0}) & = \varphi (x ^ {0}, \mathrm{U} _ {2}, \mathrm{U} _ {1}) - \lambda \varphi (x ^ {0}, \mathrm{U} _ {1}, \mathrm{U} _ {2}) \\ & = - 2 \lambda (2 \pi i) ^ {2} \tau (x ^ {0} \mathrm{U} _ {1} \mathrm{U} _ {2}). \end{array}
$$

This shows that $\mathrm{H}_{\lambda}^{2}(\mathcal{A}_{\theta})$ is generated by $\mathrm{S}\tau$ and $\varphi$.

We can now determine in this example the Chern character, viewed (as in section 2) as a pairing between $\mathrm{K}_0(\mathcal{A}_\theta)$ and $\mathrm{H}^{\mathrm{ev}}(\mathcal{A}_{\theta})$. With the notations of theorem 53, we take $\mathrm{S}\tau$ and $\varphi$ as a basis for $\mathrm{H}^{\mathrm{ev}}(\mathcal{A}_{\theta})$. From the results of Pimsner and Voiculescu [55]

and of [19] lemme 1 and théorème 7 the following finite projective modules over $\mathcal{A}_{\theta}$ form a basis of the group $\mathbf{K}_0(\mathcal{A}_\theta) = \mathbf{Z}^2$:

1) $\mathcal{A}_{\theta}$ as a right $\mathcal{A}_{\theta}$-module.

2) $\mathcal{S}(\mathbf{R})$, (the ordinary Schwartz space of the real line), with module structure given by:

$$
(\xi . \mathrm{U} _ {1}) (s) = \xi (s + \theta), \quad (\xi . \mathrm{U} _ {2}) (s) = e ^ {i 2 \pi s} \xi (s), \quad \forall s \in \mathbf {R}, \xi \in \mathcal {S} (\mathbf {R}).
$$

We shall denote the respective classes in  $\mathbf{K}_{0}(\mathcal{A}_{\theta})$  by [1] and [S].

Lemma 54. — The pairing of $\mathbf{K}_{0}(\mathcal{A}_{\theta})$ with $\mathrm{H}^{\mathrm{ev}}(\mathcal{A}_{\theta})$ is given by:

$$
a) \langle [ \mathrm{I} ], \mathrm{S} \tau \rangle = \mathrm{I}, \langle [ \mathscr {S} ], \mathrm{S} \tau \rangle = \theta \in ] 0, \mathrm{I} ]
$$

$$
b) \langle [ \mathrm{I} ], \varphi \rangle = 0, \langle [ \mathcal {S} ], \varphi \rangle = \mathrm{I}.
$$

Proof. — a) One has $\tau(1) = 1$. We leave the second equality as an exercise.

b) Since $\delta_j(1) = 0$ the first equality is clear. The second follows from [19] théorème 7, noticing that the notion of connexion used there is the same as that of definition 18 above relative to the cycle over $\mathcal{A}_{\theta}$ which defines $\varphi$ namely:

$$
\mathscr {A} _ {\theta} \rightarrow \mathscr {A} _ {\theta} \otimes \wedge^ {1} \rightarrow \mathscr {A} _ {\theta} \otimes \wedge^ {2} \stackrel {\tau} {\rightarrow} \mathbf {C}
$$

where $\wedge^1, \wedge^2$ are the exterior powers of the vector space $\mathbf{C}^2$, dual of the Lie algebra of $\mathbf{R}^2$ (which acts on $\mathcal{A}_0$ by $\delta_1, \delta_2$). (Cf. [19] definition 2.)

Corollary 55. — For $\theta \notin \mathbf{Q}$ the filtration of $\mathrm{H}^{\mathrm{ev}}(\mathcal{A}_{\theta})$ by dimensions is not compatible with the lattice dual to $\mathrm{K}_0(\mathcal{A}_\theta)$.

We shall see in chapter 4 that any element of this dual lattice is the Chern character of a $2 + \varepsilon$ summable Fredholm module on $\mathcal{A}_{\theta}$.

Problem 56. — Extend the result of this section to the “crossed product” of  $\mathbf{C}^{\infty}(\mathbf{S}^{1})$  by an arbitrary diffeomorphism of  $S^{1}$  with rotation number equal to  $\theta$  [32].

## Terminology (references to part II)

Chain, section 3
Character of a cycle, introduction and proposition 1
Cobordism of cycles, section 3
Cup product of cochains, section 1
Cycle, introduction and section 1
Cyclic cohomology, section 1, corollary 4
Exact couple, section 4
Filtration by dimension, section 2, definition 16, section 4, corollary 39
Flabby (algebra), introduction, section 1, corollary 6 and [13]
Hochschild cohomology, section 1, definition 2
Hochschild coboundary, introduction
Homotopy invariance, section 4, remark c.
Irrational rotation algebra, section 6
Pairing with K-theory, section 2
Relative theory, section 4, remark a.
Stabilized cyclic cohomology, section 2, definition 16
Suspension map, section 1, lemma 11
Tensor product of cycles, section 1
Topological projective module, section 5
Universal differential algebra, section 1, proposition 1 and [1] [14]
Vanishing cycle, section 1, definition 7

List of formulae in Part II

$$
b \mathbf {A} = \mathbf {A} b ^ {\prime}
$$

$$
b ^ {2} = 0, b ^ {\prime 2} = 0
$$

$$
\mathbf {D} b = b ^ {\prime} \mathbf {D}
$$

$$
\mathbf {B} _ {0} b + b ^ {\prime} \mathbf {B} _ {0} = \mathbf {D}
$$

$$
b \mathbf {B} = - \mathbf {B} b
$$

$$
\mathbf {B} ^ {2} = \mathbf {0}
$$

$$
\frac {1}{n + 3} \mathrm{A} (\sigma \# \varphi) = \sigma \# \varphi \quad \forall \varphi \in Z _ {\lambda} ^ {n} (\mathscr {A})
$$

$$
b \mathrm{S} = \frac {n + 1}{n + 3} \mathrm{S} b
$$

$$
[ \varphi \# \psi ] = \frac {(n + m) !}{n ! m !} [ \varphi ] \vee [ \psi ]
$$

$$
e (d e) ^ {2} = (d e) ^ {2} e
$$

## Notation used in part II

## A, B algebras over C

$\mathbf{C}^n (\mathcal{A},\mathcal{A}^*)$ space of $n + 1$ linear forms on $\mathcal{A}$

$\varphi^{\gamma}(a^{0},\ldots ,a^{n}) = \varphi (a^{\gamma (0)},\ldots ,a^{\gamma (n)})\quad \forall \varphi \in \mathrm{C}^{n}(\mathcal{A},\mathcal{A}^{*}),\gamma$ permutation of $\{0,1,\dots ,n\}$ and $a^j\in \mathcal{A}$

$$
b \varphi , \quad \varphi \in \mathrm{C} ^ {n} (\mathscr {A}, \mathscr {A} ^ {*})
$$

$$
b \varphi (a ^ {0}, \dots , a ^ {n + 1}) = \sum_ {j = 0} ^ {n} (- 1) ^ {j} \varphi (a ^ {0}, \dots , a ^ {j} a ^ {j + 1}, \dots , a ^ {n + 1}) + (- 1) ^ {n + 1} \varphi (a ^ {n + 1} a ^ {0}, \dots , a ^ {n})
$$

$$
\mathrm{Z} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) = \operatorname{Ker} b, \mathrm{B} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) = \operatorname{Im} b, \mathrm{H} ^ {n} (\mathcal {A}, \mathcal {A} ^ {*}) = \mathrm{Z} ^ {n} / \mathrm{B} ^ {n}
$$

$C_{\lambda}^{n}(\mathcal{A}) = \{\varphi \in C^{n}(\mathcal{A},\mathcal{A}^{\bullet})\}$ ， $\varphi^{\lambda} = \varepsilon (\lambda)\varphi$$\forall \lambda$ cyclic permutation

$$
\mathrm{Z} _ {\lambda} ^ {n} (\mathcal {A}) = \mathrm{C} _ {\lambda} ^ {n} (\mathcal {A}) \cap \operatorname{Ker} b
$$

$$
\mathrm{B} _ {\lambda} ^ {n} (\mathcal {A}) = b \mathrm{C} _ {\lambda} ^ {n - 1} (\mathcal {A})
$$

$$
\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}) = \mathrm{Z} _ {\lambda} ^ {n} (\mathcal {A}) / \mathrm{B} _ {\lambda} ^ {n} (\mathcal {A})
$$

$\tilde{A}$  algebra obtained from A by adjoining a unit

$\Omega (\mathcal{A})$ universal graded differential algebra

$$
\widehat {\tau} (a ^ {0}   d a ^ {1}   \dots   d a ^ {n}) = \tau (a ^ {0}, a ^ {1}, \dots , a ^ {n}) \quad (\text { proposition   } 1)
$$

$$
\mathcal {A} ^ {e} = \mathcal {A} \otimes \mathcal {A} ^ {0}, \quad \mathcal {A} ^ {0} = \text { opposite   algebra   of } \mathcal {A}
$$

$$
\mathrm{A} \varphi = \sum_ {\gamma \in \Gamma} \varepsilon (\gamma) \varphi^ {\gamma}, \quad \Gamma = \text { group   of   cyclic   permutations }
$$

$$
b ^ {\prime} \varphi = \sum_ {j = 0} ^ {n} (- 1) ^ {j} \varphi (x ^ {0}, \dots , x ^ {j} x ^ {j + 1}, \dots , x ^ {n + 1}) \quad \forall \varphi \in C ^ {n} (\mathscr {A}, \mathscr {A} ^ {*})
$$

$$
\pi : \Omega (\mathcal {A} \otimes \mathrm{B}) \rightarrow \Omega (\mathcal {A}) \otimes \Omega (\mathrm{B}) \quad \forall x ^ {j} \in \mathcal {A}
$$

$$
\varphi \# \psi = (\widehat {\varphi} \otimes \widehat {\psi}) \circ \pi
$$

$$
\sigma \in Z _ {\lambda} ^ {2} (\mathbf {C}), \sigma (\mathrm{I}, \mathrm{I}, \mathrm{I}) = 2 i \pi
$$

$$
\mathrm{S} \varphi = \varphi \# \sigma \forall \varphi \in Z _ {\lambda} ^ {*} (\mathscr {A})
$$

$$
\mathrm{H} ^ {*} (\mathcal {A}) = \varinjlim (\mathrm{H} _ {\lambda} ^ {n} (\mathcal {A}), \mathrm{S})
$$

$$
\mathbf {F} ^ {n} \mathbf {H} ^ {*} (\mathcal {A}) = \operatorname{Im} \mathbf {H} _ {\lambda} ^ {n} (\mathcal {A})
$$

$$
\mathrm{B} _ {0} \varphi (a ^ {0}, \dots , a ^ {n - 1}) = \varphi (\mathrm{i}, a ^ {0}, \dots , a ^ {n - 1}) - (- \mathrm{i}) ^ {n} \varphi (a ^ {0}, \dots , a ^ {n - 1}, \mathrm{i}), \forall \varphi \in \mathrm{C} ^ {n} (\mathscr {A}, \mathscr {A} ^ {*})
$$

$$
\mathbf {M} ^ {*} (\mathcal {A}) \text {   Cobordism   group   of   cycles   over   } \mathcal {A}
$$

$$
\text { I:   morphism   of   complexes } \quad (\mathbf {C} _ {\lambda} ^ {n}, b) \to (\mathbf {C} ^ {n}, b)
$$

$D\varphi = \varphi - \varepsilon(\lambda) \varphi^{\lambda} \quad \forall \varphi \in C^{n}(\mathscr{A}, \mathscr{A}^{*}), \lambda \text{ canonical generator of cyclic group } \Gamma$

$$
d _ {1} \varphi = (n - m + 1) b \varphi \forall \varphi \in \mathrm{C} ^ {n, m} = \mathrm{C} ^ {n - m} (\mathscr {A}, \mathscr {A} ^ {*})
$$

$$
d _ {2} \varphi = \frac {\mathrm{I}}{n - m} \mathrm{B} \varphi \in \mathrm{C} ^ {n, m + 1} \forall \varphi \in \mathrm{C} ^ {n, m}
$$

$$
\delta^ {*} \varphi (a ^ {0}, \dots , a ^ {n}) = \sum_ {i = 1} ^ {n} \varphi (a ^ {0}, \dots , \delta (a ^ {i}), \dots , a ^ {n}) \forall a ^ {i} \in \mathscr {A}, \varphi \in \mathrm{C} ^ {n} (\mathscr {A}, \mathscr {A} ^ {*}) \text { and } \delta \text { derivation   of } \mathscr {A}.
$$

[1] W. ARVESON, The harmonic analysis of automorphism groups, Operator algebras and applications, Proc. Symposia Pure Math. 38 (1982), part I, 199-269.

[2] M. F. ATIYAH, Transversally elliptic operators and compact groups, Lecture Notes in Math. 401, Berlin-New York, Springer (1974).

[3] M. F. ATIYAH, Global theory of elliptic operators, Proc. Internat. Conf. on functional analysis and related topics, Tokyo, Univ. of Tokyo Press (1970), 21-29.

[4] M. F. ATIYAH, K-theory, Benjamin (1967).

[5] M. F. ATIYAH and I. SINGER, The index of elliptic operators IV, Ann. of Math. 93 (1971), 119-138.

[6] S. BAAJ et P. JULG, Théorie bivariante de Kasparov et opérateurs non bornés dans les C\* modules Hilbertiens, C. r. Acad. Sci. Paris, Série I, 296 (1983), 875-878.

[7] P. BAUM and A. CONNES, Geometric K-theory for Lie groups and Foliations, Preprint I.H.E.S., 1982.

[8] P. BAUM and A. CONNES, Leafwise homotopy equivalence and rational Pontrjagin classes, Preprint I.H.E.S., 1983.

[9] P. BAUM and R. DOUGLAS, K-homology and index theory, Operator algebras and applications, Proc. Symposia Pure Math. 38 (1982), part I, 117-173.

[10] O. BRATTELI, Inductive limits of finite dimensional C\*-algebras, Trans. Am. Math. Soc. 171 (1972), 195-234.

[11] L. G. BROWN, R. DOUGLAS and P. A. FILLMORE, Extensions of C\*-algebras and K-homology, Ann. of Math. (2) 105 (1977), 265-324.

[12] R. CAREY and J. D. PINCUS, Almost commuting algebras, K-theory and operator algebras, Lecture Notes in Math. 575, Berlin-New York, Springer (1977).

[13] H. CARTAN and S. EILENBERG, Homological algebra, Princeton University Press (1956).

[14] A. CONNES, The von Neumann algebra of a foliation, Lecture Notes in Physics 80 (1978), 145-151, Berlin-New York, Springer.

[15] A. CONNES, Sur la théorie non commutative de l'intégration, Algèbres d'opérateurs, Lecture Notes in Math. 725, Berlin-New York, Springer (1979).

[16] A. CONNES, A Survey of foliations and operator algebras, Operator algebras and applications, Proc. Symposia Pure Math. 38 (1982), Part I, 521-628.

[17] A. CONNES, Classification des facteurs, Operator algebras and applications, Proc. Symposia Pure Math. 38 (1982), Part II, 43-109.

[18] A. CONNES and G. SKANDALIS, The longitudinal index theorem for foliations, Publ. R.I.M.S., Kyoto, 20 (1984), 1139-1183.

[19] A. CONNES, C\* algèbres et géométrie différentielle, C.r. Acad. Sci. Paris, Série I, 290 (1980), 599-604.

[20] A CONNES, Cyclic cohomology and the transverse fundamental class of a foliation, Preprint I.H E.S. M/84/7 (1984).

[21] A. CONNES, Spectral sequence and homology of currents for operator algebras. Math. Forschungsinstitut Oberwolfach Tagungsbericht 42/81, Funktionalanalysis und C\*-Algebren, 27-9/3-10-1981.

[22] J. Cuntz and W. Krieger, A class of $\mathbf{C}^*$-algebras and topological Markov chains, Invent. Math. 56 (1980), 251-268.

[23] J. Cuntz, K-theoretic amenability for discrete groups, J. Reine Angew. Math. 344 (1983), 180-195.

[24] R. DOUGLAS, C\*-algebra extensions and K-homology, Annals of Math. Studies 95, Princeton University Press, 1980.

[25] R. DOUGLAS and D. VOICULESCU, On the smoothness of sphere extensions, J. Operator Theory 6 (1) (1981), 103.

[26] E. G. EFFROS, D. E. HANDELMAN and C. L. SHEN, Dimension groups and their affine representations, Amer. J. Math. 102 (1980), 385-407.

[27] G. ELLIOTT, On the classification of inductive limits of sequences of semi-simple finite dimensional algebras, J. Alg. 38 (1976), 29-44.

[28] E. GETZLER, Pseudodifferential operators on supermanifolds and the Atiyah Singer index theorem, Commun. Math. Physics 92 (1983), 163-178.

[29] A. GROTHENDIECK, Produits tensoriels topologiques, Memoirs Am. Math. Soc. 16 (1955).

[30] J. HELTON and R. HOWE, Integral operators, commutators, traces, index and homology, Proc. of Conf. on operator theory, Lecture Notes in Math. 345, Berlin-New York, Springer (1973).

[31] J. HELTON and R. HOWE, Traces of commutators of integral operators, Acta Math. 135 (1975), 271-305.

[32] M. HERMAN, Sur la conjugaison différentiable des difféomorphismes du cercle à des rotations, Publ. Math. I.H.E.S. 49 (1979).

[33] G. HOCHSCHILD, B. KOSTANT and A. ROSENBERG, Differential forms on regular affine algebras, Trans. Am. Math. Soc. 102 (1962), 383-408.

[34] L. HÖRMANDER, The Weyl calculus of pseudodifferential operators, Comm. Pure Appl. Math. 32 (1979), 359-443.

[35] B. JOHNSON, Cohomology in Banach algebras, Memoirs Am. Math. Soc. 127 (1972).

[36] B. JOHNSON, Introduction to cohomology in Banach algebras, in Algebras in Analysis, Ed. Williamson, New York, Academic Press (1975), 84-99.

[37] P. JULG and A. VALETTE, K-moyennabilité pour les groupes opérant sur les arbres, C. r. Acad. Sci. Paris, Série I, 296 (1983), 977-980.

[38] D. S. KAHN, J. KAMINKER and C. SCHOCHET, Generalized homology theories on compact metric spaces, Michigan Math. J. 24 (1977), 203-224.

[39] M. KAROUBI, Connexions, courbures et classes caractéristiques en K-théorie algébrique, Canadian Math. Soc. Proc., Vol. 2, part I (1982), 19-27.

[40] M. KAROUBI, K-theory. An introduction, Grundlehren der Math., Bd. 226 (1978), Springer Verlag.

[41] M. KAROUBI et O. VILLAMAYOR, K-théorie algébrique et K-théorie topologique I., Math. Scand. 28 (1971), 265-307.

[42] G. KASPAROV, K-functor and extensions of C\*-algebras, Izv. Akad. Nauk SSSR, Ser. Mat. 44 (1980), 571-636.

[43] G. KASPAROV, K-theory, group C\*-algebras and higher signatures, Conspectus, Chernogolovka (1983).

[44] G. KASPAROV, Lorentz groups: K-theory of unitary representations and crossed products, preprint, Chernogolovka, 1983.

[45] B. KOSTANT, Graded manifolds, graded Lie theory and prequantization, Lecture Notes in Math. 570, Berlin-New York, Springer (1975).

[46] J. L. LODAY and D. QUILLEN, Cyclic homology and the Lie algebra of matrices, C. r. Acad. Sci. Paris, Série I, 296 (1983), 295-297.

[47] S. MAC LANE, Homology, Berlin-New York, Springer (1975).

[48] J. MILNOR, Introduction to algebraic K-theory, Annals of Math. Studies, 72, Princeton Univ. Press.

[49] J. MILNOR and D. STASHEFF, Characteristic classes, Annals of Math. Studies 76, Princeton Univ. Press.

[50] A. S. Miščenko, Infinite dimensional representations of discrete groups and higher signatures, Math. USSR Izv. 8 (1974), 85-112.

[51] G. PEDERSEN, C\*-algebras and their automorphism groups, New York, Academic Press (1979).

[52] M. PENINGTON, K-theory and C\*-algebras of Lie groups and Foliations, D. Phil. thesis, Oxford, Michaelmas, Term., 1983.

[53] M. PENINGTON and R. PLYMEN, The Dirac operator and the principal series for complex semi-simple Lie groups, J. Funct. Analysis 53 (1983), 269-286.

[54] M. PIMSNER and D. VOICULESCU, Exact sequences for K-groups and Ext groups of certain cross-product C\*-algebras, J. of operator theory 4 (1980), 93-118.

[55] M. PIMSNER and D. VOICULESCU, Imbedding the irrational rotation $\mathbf{C}^*$ algebra into an AF algebra, $J$. of operator theory 4 (1980), 201-211.

[56] M. PIMSNER and D. VOICULESCU, K groups of reduced crossed products by free groups, J. operator theory 8 (1) (1982), 131-156.

[57] M. REED and B. SIMON, Fourier Analysis, Self adjointness, New York, Academic Press (1975).

[58] M. RIEFFEL, C\*-algebras associated with irrational rotations, Pac. J. of Math. 95 (2) (1981), 415-429.

[59] J. ROSENBERG, C\*-algebras, positive scalar curvature and the Novikov conjecture, Publ. Math. I.H.E.S. 58 (1984), 409-424.

[60] W. RUDIN, Real and complex analysis, New York, McGraw Hill (1966).