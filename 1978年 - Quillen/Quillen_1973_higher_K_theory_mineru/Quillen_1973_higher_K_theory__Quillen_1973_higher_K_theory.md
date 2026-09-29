## Daniel Quillen\*

The purpose of this paper is to develop a higher K-theory for additive categories with exact sequences which extends the existing theory of the Grothendieck group in a natural way. To describe the approach taken here, let $\underline{\underline{M}}$ be an additive category embedded as a full subcategory of an abelian category $\underline{\underline{A}}$, and assume $\underline{\underline{M}}$ is closed under extensions in $\underline{\underline{A}}$. Then one can form a new category $Q(\underline{\underline{M}})$ having the same objects as $\underline{\underline{M}}$, but in which a morphism from $M'$ to $M$ is taken to be an isomorphism of $M'$ with a subquotient $M_1/M_0$ of $M$, where $M_0 \subset M_1$ are subobjects of $M$ such that $M_0$ and $M/M_1$ are objects of $\underline{\underline{M}}$. Assuming the isomorphism classes of objects of $\underline{\underline{M}}$ form a set, the category $Q(\underline{\underline{M}})$ has a classifying space $BQ(\underline{\underline{M}})$ determined up to homotopy equivalence. One can show that the fundamental group of this classifying space is canonically isomorphic to the Grothendieck group of $\underline{\underline{M}}$, which motivates defining a sequence of K-groups by the formula

$$
\mathrm{K} _ {\mathbf {i}} (\underline {{\mathrm{M}}}) = \pi_ {\mathbf {i + 1}} (\mathrm{BQ} (\underline {{\mathrm{M}}}), 0).
$$

It is the goal of the present paper to show that this definition leads to an interesting theory.

The first part of the paper is concerned with the general theory of these K-groups. Section 1 contains various tools for working with the classifying space of a small category. It concludes with an important result which identifies the homotopy-theoretic fibre of the map of classifying spaces induced by a functor. In K-theory this is used to obtain long exact sequences of K-groups from the exact homotopy sequence of a map.

Section 2 is devoted to the definition of the K-groups and their elementary properties. One notes that the category $Q(\underline{\underline{M}})$ depends only on $\underline{\underline{M}}$ and the family of those short sequences $O \to M' \to M \to M'' \to O$ in $\underline{\underline{M}}$ which are exact in the ambient abelian category. In order to have an intrinsic object of study, it is convenient to introduce the notion of an exact category, which is an additive category equipped with a family of short sequences satisfying some standard conditions (essentially those axiomatized in [Heller]). For an exact category $\underline{\underline{M}}$ with a set of isomorphism classes one has a sequence of K-groups $K_{i}(\underline{\underline{M}})$ varying functorially with respect to exact functors. Section 2 also contains the proof that $K_{o}(\underline{\underline{M}})$ is isomorphic to the Grothendieck group of $\underline{\underline{M}}$. It should be mentioned, however, that there are examples due to Gersten and Murthy showing that in general $K_{1}(\underline{\underline{M}})$ is not the same as the universal determinant group of Bass.

The next three sections contain four basic results which might be called the exactness, resolution, devissage, and localization theorems. Each of these generalizes a well-known result for the Grothendieck group ([Bass, Ch. VIII]), and, as will be apparent from the rest of the paper, they enable one to do a lot of K-theory.

The second part of the paper is concerned with applications of the general theory to rings and schemes. Given a ring (resp. a noetherian ring) A, one defines the groups

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*Supported in part by the National Science Foundation.</span></small>

$K_{i}(A)$  (resp.  $K_{i}^{\prime}(A)$ ) to be the K-groups of the category of finitely generated projective A-modules (resp. the abelian category of finitely generated A-modules). There is a canonical map  $K_{i}(A) \rightarrow K_{i}^{\prime}(A)$  which is an isomorphism for A regular by the resolution theorem. Because the devissage and localization theorems apply only to abelian categories, the interesting results concern the groups  $K_{i}^{\prime}(A)$ . In section 6 we prove the formulas

$$
\mathrm{K} _ {\mathbf {i}} ^ {\prime} (\mathrm{A}) = \mathrm{K} _ {\mathbf {i}} ^ {\prime} (\mathrm{A} [ \mathrm{t} ]) \quad , \quad \mathrm{K} _ {\mathbf {i}} ^ {\prime} (\mathrm{A} [ \mathrm{t}, \mathrm{t} ^ {- 1} ]) = \mathrm{K} _ {\mathbf {i}} ^ {\prime} (\mathrm{A}) \oplus \mathrm{K} _ {\mathbf {i - 1}} ^ {\prime} (\mathrm{A})
$$

for A noetherian, which entail the corresponding results for K-groups when A is regular. The first formula is proved more generally for a class of rings with increasing filtration, including some interesting non-commutative rings such as universal enveloping algebras. To illustrate the generality, the K-groups of certain skew fields are computed.

For a scheme (resp. noetherian) scheme $X$, the groups $K_{i}(X)$ (resp. $K_{i}'(X)$) are defined using the category of vector bundles (resp. coherent sheaves) on $X$, and there is a canonical map $K_{i}(X) \to K_{i}'(X)$ which is an isomorphism for $X$ regular. Section 7 is devoted to the $K'$-theory. Especially interesting is a spectral sequence

$$
E _ {1} ^ {p q} = \underset {\operatorname{cod} (x) = p} {\coprod} K _ {- p - q} (k (x)) \Longrightarrow K _ {- n} ^ {\prime} (x)
$$

obtained by filtering the category of coherent sheaves according to the codimension of the support. In the case where X is regular and of finite type over a field, we carry out a program proposed by Gersten at this conference ([Gersten 3]), which leads to a proof of Bloch's formula

$$
\mathrm{A} ^ {\mathrm{p}} (\mathrm{X}) = \mathrm{H} ^ {\mathrm{p}} (\mathrm{X}, \mathrm{K} _ {\mathrm{p}} (\underline {{\mathrm{O}}} _ {\mathrm{X}}))
$$

proved by Bloch in particular cases ([Bloch]), where $A^p(X)$ is the group of codimension $p$ cycles modulo linear equivalence. One noteworthy feature of this formula is that the right side is clearly contravariant in $X$, which suggests rather strongly that higher $K$-theory might eventually provide a theory of the Chow ring for non-quasi-projective regular varieties.

Section 8 contains the computation of the K-groups of the projective bundle associated to a vector bundle over a scheme. This result generalizes the computation of the Grothendieck groups given in [SGA 6], and it may be viewed as a first step toward a higher K-theory for schemes, as opposed to the K'-theory of the preceding section. The proof, different from the one in [SGA 6], is based on the existence of canonical resolutions for regular sheaves on projective space, which may be of some independent interest. The method also permits one to determine the K-groups of a Severi-Brauer scheme in terms of the K-groups of the associated Azumaya algebra and its powers.

This paper contains proofs of all of the results announced in [Quillen 1], except for Theorem 1 of that paper, which asserts that the groups $K_{i}(A)$ here agree with those obtained by making BGL(A) into an H-space (see [Gersten 5]). From a logical point of view, this theorem should have preceded the second part of the present paper, since it is used there a few times. However, I recently discovered that the ideas involved its proof could be applied to prove the expected generalization of the localization theorem and

fundamental theorem for non-regular rings [Bass, p.494,663]. These results will appear in the next installment of this theory.

The proofs of Theorems A and B given in section 1 owe a great deal to conversations with Graeme Segal, to whom I am very grateful. One can derive these results in at least two other ways, using cohomology and the Whitehead theorem as in [Friedlander], and also by means of the theory of minimal fibrations of simplicial sets. The present approach, based on the Dold-Thom theory of quasi-fibrations, is quite a bit shorter than the others, although it is not as clear as I would have liked, since the main points are in the references. Someday these ideas will undoubtedly be incorporated into a general homotopy theory for topoi.

This paper was prepared with the editor's encouragement during the first two months of 1973. I mention this because the results in §7 on Gersten's conjecture and Bloch's formula, which were discovered at this time, directly affect the papers [Gersten 3, 4] and [Bloch] in this proceedings, which were prepared earlier.

## CONTENTS

First part: General theory

§1. The classifying space of a small category
Coverings of BC and the fundamental group
The homology of the classifying space
Properties of the classifying space functor
Theorem A: Conditions for a functor to be a homotopy equivalence
Theorem B: The exact homotopy sequence

§2. The K-groups of an exact category
Exact categories
The category Q(M) and its universal property
The fundamental group of Q(M) and the Grothendieck group
Definition of K₁(M)
Elementary properties of the K-groups

§3. Characteristic exact sequences and filtrations

§4. Reduction by Resolution
The resolution theorem
Transfer maps

§5. Devissage and localization in abelian categories

Second part: Applications

§6. Filtered rings and the homotopy property for regular rings
Graded rings
Filtered rings
Fundamental theorem for regular rings
K-groups of some skew fields

§7. K'-theory for schemes
The groups K₁(X) and K₁'(X)
Functorial behavior
Closed subschemes
Affine and projective space bundles
Filtration by support
Gersten's conjecture for regular local rings
Relation with the Chow ring (Bloch's formula)

§8. Projective fibre bundles
The canonical resolution of a regular sheaf on PE
The projective bundle theorem
The projective line over a (not necessarily commutative) ring
Severi-Brauer schemes and Azumaya algebras

In the succeeding sections of this paper K-groups will be defined as the homotopy groups of the classifying space of a certain small category. In this rather long section we collect together the various facts about the classifying space functor we will need. All of these are fairly well-known, except for the important Theorem B which identifies the homotopy-fibre of the map of classifying spaces induced by a functor under suitable conditions. It will later be used to derive long exact sequences in K-theory from the homotopy exact sequence of a map.

Let $\underline{\underline{C}}$ be a small category. Its nerve, denoted NC, is the (semi-)simplicial set whose p-simplices are the diagrams in $\underline{\underline{C}}$ of the form

$$
\mathrm{x} _ {\mathrm{o}} \longrightarrow \mathrm{x} _ {1} \longrightarrow \dots \longrightarrow \mathrm{x} _ {\mathrm{p}}.
$$

The i-th face (resp. degeneracy) of this simplex is obtained by deleting the object $X_{i}$ (resp. replacing $X_{i}$ by id: $X_{i} \longrightarrow X_{i}$) in the evident way. The classifying space of $\underline{C}$, denoted $BC$, is the geometric realization of $NC$. It is a CW complex whose p-cells are in one-one correspondence with the p-simplices of the nerve which are nondegenerate, i.e. such that none of the arrows is an identity map. (See [Segal 1], [Milnor 1].)

For example, let J be a (partially) ordered set regarded as a category in the usual way. Then BJ is the simplicial complex (with the weak topology) whose vertices are the elements of J and whose simplices are the totally ordered non-empty finite subsets of J. Conversely, if K is a simplicial complex and if J is the ordered set of simplices of K, then the simplicial complex BJ is the barycentric subdivision of K. Thus every simplicial complex (with the weak topology) is homeomorphic to the classifying space of some, and in fact many, ordered sets. Furthermore, since it is known that any CW complex is homotopy equivalent to a simplicial complex, it follows that any interesting homotopy type is realized as the classifying space of an ordered set. (I am grateful to Graeme Segal for bringing these remarks to my attention.)

As another example, let a group G be regarded as a category with one object in the usual way. Then BG is a classifying space for the discrete group G in the traditional sense. It is an Eilenberg–MacLane space of type  $K(G,1)$ , so few homotopy types occur in this way.

Let $X$ be an object of $\underline{\underline{C}}$. Using $X$ to denote also the corresponding O-cell of $BC$, we have a family of homotopy groups $\pi_{i}(BC, X)$, $i \geq 0$, which will be called the homotopy groups of $\underline{\underline{C}}$ with basepoint $X$ and denoted simply $\pi_{i}(C, X)$. Of course, $\pi_{o}(C, X)$ is not a group, but a pointed set, which can be described as the set $\pi_{o}^{C}$ of components of the category $\underline{\underline{C}}$ pointed by the component containing $X$. In effect, connected components of $BC$ are in one-one correspondence with components of $\underline{\underline{C}}$.

We will see below that $\pi_1(\underline{\underline{C}}, X)$ and also the homology groups of BC can be defined "algebraically" without the use of spaces or some closely related machine such as semi-simplicial homotopy theory, or simplicial complexes and subdivision. The existence of similar descriptions of the higher homotopy groups seems to be unlikely, because so far

nobody has produced an "algebraic" definition of the homotopy groups of a simplicial complex.

Coverings of BC and the fundamental group.

Let $E$ be a covering space of $\underline{BC}$. For any object $X$ of $\underline{C}$, let $E(X)$ denote the fibre of $E$ over $X$ considered as a O-cell of $\underline{BC}$. If $u: X \to X'$ is a map in $\underline{C}$, it determines a path from $X$ to $X'$ in $\underline{BC}$, and hence gives rise to a bijection $E(u): E(X) \xrightarrow{\sim} E(X')$. It is easy to see that $E(fg) = E(f)E(g)$, hence in this way we obtain a functor $X \mapsto E(X)$ from $\underline{C}$ to Sets which is morphism-inverting, that is, it carries arrows into isomorphisms.

Conversely, given $F: \underline{C} \to \text{Sets}$, let $F \backslash \underline{C}$ denote the category of pairs $(X, x)$ with $X$ in $\underline{C}$ and $x \in F(X)$, in which a morphism $(X, x) \to (X', x')$ is a map $u: X \to X'$ such that $F(u)x = x'$. The forgetful functor $F \backslash \underline{C} \to \underline{C}$ induces a map of classifying spaces $B(F \backslash \underline{C}) \to BC$ having the fibre $F(X)$ over $X$ for each object $X$. Using [Gabriel-Zisman, App.I, 3.2] it is not difficult to see that when $F$ is morphism-inverting, the map $B(F \backslash \underline{C}) \to BC$ is locally trivial, and hence $B(F \backslash \underline{C})$ is a covering space of $BC$. It is clear that the two procedures just described are inverse to each other, whence we have an equivalence of categories

$$
(\text { Coverings   of } \underline {{\mathrm{BC}}}) \quad \simeq \quad (\text { Morph. - inv. } \mathrm{F}: \underline {{\mathrm{C}}} \rightarrow \text { Sets })
$$

where the latter denotes the full subcategory of $\operatorname{Funct}(\underline{\underline{\mathbb{C}}},\text{Sets})$, the category of functors from $\underline{\underline{\mathbb{C}}}$ to Sets, consisting of the morphism-inverting functors.

Let $\underline{\underline{G}} = \underline{\underline{C}}[(\mathrm{Ar}\underline{\underline{C}})^{-1}]$ denote the groupoid obtained from $\underline{\underline{C}}$ by formally adjoining the inverses of all the arrows [Gabriel-Zisman, I, 1.1]. The canonical functor from $\underline{\underline{C}}$ to $\underline{\underline{G}}$ induces an equivalence of categories

$$
\text { Funct } (\underline {{G}}, \text { Sets }) = (\text { Morph. - inv.   F }: \underline {{C}} \rightarrow \text { Sets })
$$

(loc.cit., I, 1.2). Let X be an object of $\underline{\underline{C}}$ and let $G_{X}$ be the group of its automorphisms as an object of $\underline{\underline{G}}$. When $\underline{\underline{C}}$ is connected, the inclusion functor $G_{X} \to \underline{\underline{G}}$ is an equivalence of categories, hence one has an equivalence

$$
\text { Funct } (\underline {{G}}, \text { Sets }) \quad \xrightarrow {\sim} \text { Funct } (G _ {X}, \text { Sets }) = (G _ {X} - \text { sets }).
$$

Therefore by combining the above equivalences, we obtain an equivalence of categories of the category of coverings of $\underline{\mathbf{BC}}$ with the category of $G_{X}$-sets given by the functor $E \mapsto E(X)$. By the theory of covering spaces this implies that there is a canonical isomorphism: $\pi_1(\underline{\mathbf{C}}, X) \simeq G_X$. The same conclusion holds when $\underline{\mathbf{C}}$ is not connected, as both groups depend only on the component of $\underline{\mathbf{C}}$ containing $X$. Thus we have established the following.

Proposition 1. The category of covering spaces of BC is canonically equivalent to the category of morphism-inverting functors $F: \underline{C} \to \text{Sets}$, or what amounts to the same thing, the category $\text{Funct}(G, \text{Sets})$, where $G = C[(ArC)^{-1}]$ is the groupoid obtained by formally inverting the arrows of $\underline{C}$. The fundamental group $\pi_1(\underline{C}, X)$ is canonically isomorphic to the group of automorphisms of $X$ as an object of the groupoid $\underline{G}$.

It follows in particular that a local coefficient system $L$ of abelian groups on $\mathbb{C}$ may be identified with the morphism-inverting functor $X \mapsto L(X)$ from $\mathbb{C}$ to abelian groups.

The homology of BC

It is well-known that the homology and cohomology of the classifying space of a discrete group coincide with the homology and cohomology of the group in the sense of homological algebra. We now describe the generalization of this fact for an arbitrary small category.

Let $A$ be a functor from $\underline{C}$ to $Ab$, the category of abelian groups, and let $H_{p}(\underline{C}, A)$ denote the homology of the simplicial abelian group

$$
C _ {p} (\underline {{C}}, A) = \underset {X _ {o} \rightarrow \dots \rightarrow X _ {p}} {\perp \perp} A (X _ {o})
$$

of chains on NC with coefficients in A. (By the homology we mean the homology of the associated normalized chain complex.) Then there are canonical isomorphisms

$$
\mathrm{H} _ {\mathrm{p}} (\underline {{\mathrm{C}}}, \mathrm{A}) = \lim _ {\mathrm{p}} \frac {\underline {{\mathrm{C}}}}{\mathrm{p}} (\mathrm{A})
$$

$$
\underbrace {\lim} _ {*} \stackrel {{C}} {+}
$$

where $\varinjlim_{*}$ denotes the left derived functors of the right exact functor $\varinjlim$ from $\operatorname{Funct}(\underline{\underline{\mathbb{C}}},\mathrm{Ab})$ to $\mathrm{Ab}$. This is proved by showing that $A \mapsto H_{*}(\underline{\underline{\mathbb{C}}},A)$ is an exact $\partial$-functor which coincides with $\varinjlim$ in degree zero and is effaceable in positive degrees. (See [Gabriel-Zisman, App.II, 3.3].)

Let $H_{*}(BC, L)$ denote the singular homology of $BC$ with coefficients in a local coefficient system L. Then there are canonical isomorphisms

$$
\mathrm{H} _ {\mathrm{p}} (\underset {=} {\mathrm{BC}}, \mathrm{L}) = \mathrm{H} _ {\mathrm{p}} (\underset {=} {\mathrm{C}}, \mathrm{L})
$$

where we identify L with a morphism-inverting functor as above. This may be proved by filtering the CW complex BC by means of its skeleta and considering the associated spectral sequence. One has  $E_{pq}^{1}=0$  for  $q\neq0$  and  $E_{*0}^{1}=$  the normalized chain complex associated to  $C_{*}(C,L)$ . (Compare [Segal 1, 5.1].) The spectral sequence degenerates yielding the desired isomorphism.

Thus we have

$$
\mathrm{H} _ {\mathrm{p}} (\underset {=} {\mathrm{BC}}, \mathrm{L}) = \lim _ {\rightarrow} \underset {\mathrm{P}} {\stackrel {\underline {{\mathrm{C}}}} {=}} (\mathrm{L})\tag{1}
$$

and similarly we have a canonical isomorphism for cohomology

$$
\mathrm{H} ^ {\mathrm{P}} (\underset {\underline {{=}}} {\mathrm{BC}}, \mathrm{L}) = \underset {\underline {{=}}} {\lim} _ {\underline {{C}}} ^ {\mathrm{P}} (\mathrm{L})\tag{2}
$$

where $\varprojlim_{\underline{\underline{C}}}$ denotes the right derived functors of the left exact functor $\varprojlim$ from $\operatorname{Funct}(\underline{\underline{C}},\mathrm{Ab})$ to Ab.

Properties of the classifying space functor.

From now on we use the letters $\underline{\underline{C}}$, $\underline{\underline{C}'}$, etc. to denote small categories. If $f: \underline{\underline{C}} \to \underline{\underline{C}'}$ is a functor, it induces a cellular map $Bf: BC \to BC'$. In this way we obtain a faithful functor from the category of small categories to the category of CW complexes and cellular maps. This functor is of course not fully faithful. As a particularly interesting example, we note that there is an obvious canonical cellular homeomorphism

$$
\underset {=} {\mathrm{BC}} = \underset {=} {\mathrm{BC} ^ {0}}\tag{3}
$$

where $\underline{\underline{C}}^{\circ}$ is the dual category, which is not realized by a functor from $\underline{\underline{C}}$ to $\underline{\underline{C}}^{\circ}$ except in very special cases, e.g. groups.

By the compatibility of geometric realization with products [Milnor 1], one knows that the canonical map

$$
\mathrm{B} (\underset {\equiv} {\mathrm{C}} \times \underset {\equiv} {\mathrm{C} ^ {\prime}}) \longrightarrow \underset {\equiv} {\mathrm{BC}} \times \underset {\equiv} {\mathrm{BC} ^ {\prime}}
$$

is a homeomorphism if either BC or BC' is a finite complex, and also if the product is given the compactly generated topology. As pointed out in [Segal 1], this implies the following.

Proposition 2. A natural transformation $\theta: f \to g$ of functors from C to C' induces a homotopy BC x I $\longrightarrow$ BC' between Bf and Bg.

In effect, the triple $(f,g,\theta)$ can be viewed as a functor $\underline{\underline{C}}\times\mathbf{1}\longrightarrow\underline{\underline{C}}'$, where $\mathbf{1}$ is the ordered set $\{0<1\}$, and $\mathbf{B}\mathbf{1}$ is the unit interval.

We will say that a functor is a homotopy equivalence if it induces a homotopy equivalence of classifying spaces, and that a category is contractible if its classifying space is.

Corollary 1. If a functor $f$ has either a left or a right adjoint, then $f$ is a homotopy equivalence.

For if $f'$ is say left adjoint to $f$, then there are natural transformations $f'f \to id$, $id \to ff'$, whence $Bf'$ is a homotopy inverse for $Bf$.

Corollary 2. A category having either an initial or a final object is contractible.

For then the functor from the category to the punctual category has an adjoint.

Let $I$ be a small category which is filtering (= non-empty + directed [Bass, p.41]) and let $i \mapsto C_{=i}$ be a functor from $I$ to small categories. Let $C =$ be the inductive limit of the $C_{=i}$; because filtered inductive limits commute with finite projective limits, we have $\text{ObC} = \varinjlim \text{ObC}_{=i}, \text{ArC} = \varinjlim \text{ArC}_{=i}$, and more generally $NC = \varinjlim NC_{=i}$. Let $X_i \in \text{ObC}_{=i}$ be a family of objects such that for every arrow $i \to i'$ in $I$, the induced functor $C_{=i} \to C_{=i}$, carries $X_i$ to $X_i'$, whence we have an inductive system $\pi_n(C_{=i}, X_i)$ indexed by $I$.

Proposition 3. If X is the common image of the  $X_{i}$  in C, then

$$
\lim _ {\rightarrow} \pi_ {n} (C, X _ {i}) = \pi_ {n} (C, X).
$$

Proof. Because I is filtering and $\underline{\mathbf{NC}} = \varinjlim \underline{\mathbf{NC}}_{\underline{i}}$, it follows that any simplicial subset of $\underline{\mathbf{NC}}$ with a finite number of nondegenerate simplices lifts to $\underline{\mathbf{NC}}_{\underline{i}}$ for some i, and moreover the lifting is unique up to enlarging the index i in the evident sense. As every compact subset of a CW complex is contained in a finite subcomplex, we see that every compact subset of $\underline{\mathbf{BC}}$ lifts to $\underline{\mathbf{BC}}_{\underline{i}}$ for some i, uniquely up to enlarging i. The proposition follows easily from this.

Corollary 1. Suppose in addition that for every arrow $i \to i'$ in I the induced functor $C_{=i} \to C_{=i'}$, is a homotopy equivalence. Then the functor $C_{=i} \to C =$ is a homotopy equivalence for each $i$.

Proof. Replacing I by the cofinal category i\I of objects under i, we can suppose i is the initial object of I. It then follows from the proposition that the map of CW complexes BC=1→BC induces isomorphisms on homotopy. Hence it is a homotopy equivalence by a well-known theorem of Whitehead.

$$
\mathbf {I} / \mathbf {i}
$$

$$
i \mapsto I / i
$$

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Sufficient conditions for a functor to be a homotopy equivalence.

Let $f: \underline{\underline{C}} \to \underline{\underline{C}}'$ be a functor and denote objects of $\underline{\underline{C}}$ by X, X', etc. and objects of $\underline{\underline{C}}'$ by Y, Y', etc. If Y is a fixed object of $\underline{\underline{C}}'$, let Y\f denote the category consisting of pairs (X,v) with v: Y → fX, in which a morphism from (X,v) to (X',v') is a map w: X → X' such that f(w)v = v'. In particular, when f is the identity functor of $\underline{\underline{C}}'$, we obtain the category Y\C' of objects under Y. Similarly one defines the category f/Y consisting of pairs (X,u) with u: fX → Y.

Theorem A. If the category Y\f is contractible for every object Y of $\underline{\underline{C}}'$, then the functor f is a homotopy equivalence.

In view of (3), this result admits a dual formulation to the effect that f is a homotopy equivalence when all of the categories f/Y are contractible.

Example. Let g: K → K' be a simplicial map of simplicial complexes, and let f: J → J' be the induced map of ordered sets of simplices in K and K', so that g is homeomorphic to Bf. If $\overline{\sigma}$ denotes the element of J' corresponding to a simplex $\sigma$ of K', then f/$\overline{\sigma}$ is the ordered set of simplices in g$^{-1}$($\sigma$). In this situation the theorem says that a simplicial map is a homotopy equivalence when the inverse image of each (closed) simplex is contractible.

Before proving the theorem we derive a corollary. First we recall the definition of fibred and cofibred categories [SGA 1, Exp. VI] in a suitable form. Let f$^{-1}$(Y) denote the fibre of f over Y, that is, the subcategory of $\underline{\underline{C}}$ whose arrows are those mapped to the identity of Y by f. It is easily seen that f makes $\underline{\underline{C}}$ a prefibred category over $\underline{\underline{C}}'$ in the sense of loc.cit. if and only if for every object Y of $\underline{\underline{C}}'$ the functor

f$^{-1}$(Y) → Y\f, X ↦ (X, id_Y)

has a right adjoint. Denoting the adjoint by (X,v) ↦ v*X, we obtain for any map v: Y → Y' a functor

v* : f$^{-1}$(Y') → f$^{-1}$(Y)

determined up to canonical isomorphism, called base-change by v. The prefibred category $\underline{\underline{C}}$ over $\underline{\underline{C}}'$ is a fibred category if for every pair u,v of composable arrows in $\underline{\underline{C}}'$, the canonical morphism of functors u*v* → (vu)* is an isomorphism. We will call such functors f prefibred and fibred respectively.

Dually, f makes $\underline{\underline{C}}$ into a precofibred category over $\underline{\underline{C}}'$ when the functors f$^{-1}$(Y) → f/Y have left adjoints (X,v) ↦ v*X. In this case the functor v* : f$^{-1}$(Y) → f$^{-1}$(Y') induced by v: Y → Y' is called cobase-change by v, and $\underline{\underline{C}}$ is a cofibred category when (vu)* ≈ v*u* for all composable u,v. Such functors f will be called precofibred and cofibred respectively.

Corollary. Suppose that f is either prefibred or precofibred, and that f$^{-1}$(Y) is contractible for every Y. Then f is a homotopy equivalence.

This follows from Eqn 2, Gen 1
</div>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">This follows from Prop. 2, Cor. 1.</span></small>

Example. Let $S(\underline{\underline{C}})$ be the category whose objects are the arrows of $\underline{\underline{C}}$, and in which a morphism from $u: X \to Y$ to $u': X' \to Y'$ is a pair $v: X' \to X$, $w: Y \to Y'$ such that $u' = wuv$. (Thus $S(\underline{\underline{C}})$ is the cofibred category over $\underline{\underline{C}}\circ x\underline{\underline{C}}$ with discrete fibres defined by the functor $(X,Y) \mapsto \text{Hom}(X,Y)$.) One has functors

$$
\underline {{\underline {{\mathbb {C}}}}} ^ {\circ} \xleftarrow {\mathbf {s}} \mathrm{S} (\underline {{\underline {{\mathbb {C}}}}}) \xrightarrow {\mathbf {t}} \underline {{\underline {{\mathbb {C}}}}}
$$

given by source and target, and it is easy to see that these functors are cofibred. The categories $s^{-1}(X) = X \setminus \underline{C}$ and $t^{-1}(Y) = (\underline{C}/Y)^0$ have initial objects, hence are contractible. Therefore $s$ and $t$ are homotopy equivalences by the corollary. This construction provides the simplest way of realizing by means of functors the homotopy equivalence (3).

We now turn to the proof of Theorem A. We will need a standard fact about the realization of bisimplicial spaces which we now derive.

Let $\underline{\text{Ord}}$ be the category of ordered sets $\mathbf{p} = \{0 < 1 < .. < p\}$, $p \in \mathbb{N}$, so that by definition simplicial objects are functors with domain $\underline{\text{Ord}}^0$. The realization functor

$$
(p \mapsto x _ {p}) \mapsto | p \mapsto x _ {p} |
$$

from simplicial spaces to spaces ([Segal 1]) may be defined as the functor left adjoint to the functor which associates to a space $Y$ the simplicial space $p \mapsto \underline{\mathrm{Hom}}(\Delta^p, Y)$, where $\underline{\mathrm{Hom}}$ denotes function space and $\Delta^p$ is the simplex having $p$ as its set of vertices. In particular the realization functor commutes with inductive limits.

Let $T: \mathfrak{p}, \mathfrak{q} \mapsto T_{pq}$ be a bisimplicial space, i.e. a functor from $Ord^0 x Ord^0$ to spaces. Realizing with respect to $\mathfrak{q}$ keeping $\mathfrak{p}$ fixed, we obtain a simplicial space $\mathfrak{p} \mapsto |\mathfrak{q} \mapsto T_{pq}|$ which may then be realized with respect to $\mathfrak{p}$. Also, we may realize first in the $p$-direction and then in the $q$-direction, or we may realize the diagonal simplicial space $\mathfrak{p} \mapsto T_{pp}$. It is well-known (e.g. [Tornehave]) that these three procedures yield the same result:

Lemma. There are homeomorphisms

$$
\left| \mathbf {p} \mapsto \mathrm{T} _ {\mathrm{pp}} \right| = \left| \mathbf {p} \mapsto \left| \mathbf {q} \mapsto \mathrm{T} _ {\mathrm{pq}} \right| \right| = \left| \mathbf {q} \mapsto \left| \mathbf {p} \mapsto \mathrm{T} _ {\mathrm{pq}} \right| \right|
$$

which are functorial in the simplicial space T.

Proof. Suppose first that T is of the form

$$
h ^ {r s} x S: (p, q) \mapsto \operatorname{Hom} (p, r) x \operatorname{Hom} (q, s) x S
$$

where S is a given space. Then

$$
\left| \mathbf {p} \mapsto \operatorname{Hom} (\mathbf {p}, \mathbf {r}) \times \operatorname{Hom} (\mathbf {p}, \mathbf {s}) \times S \right| = \Delta^ {r} x \Delta^ {s} x S.
$$

(This is the basic homeomorphism used to prove that geometric realization commutes with products [Milnor 1].) On the other hand, we have

$$
\begin{array}{r l} \left| \mathbb {P} \mapsto | \mathbb {q} \mapsto \operatorname{Hom} (\mathbb {p}, \mathbf {r}) \times \operatorname{Hom} (\mathbf {q}, \mathbf {s}) \times \mathrm{S} | \right| \\ = \left| \mathbb {p} \mapsto \operatorname{Hom} (\mathbb {p}, \mathbf {r}) \times \bigtriangleup^ {\mathbf {s}} \times \mathrm{S} \right| & = \bigtriangleup^ {\mathbf {r}} \times \bigtriangleup^ {\mathbf {s}} \times \mathrm{S} \end{array}
$$

and similarly for the double realization taken in the other order. Thus the required functorial homeomorphisms exist on the full subcategory of bisimplicial spaces of this form.

But any T has a canonical presentation

$$
\underbrace {\left|\right|} _ {(\mathbf {r}, \mathbf {s}) \rightarrow (\mathbf {r} ^ {\prime}, \mathbf {s} ^ {\prime})} h ^ {r ^ {\prime} s ^ {\prime}} x T _ {r s} \Longrightarrow \underbrace {\left|\right|} _ {(\mathbf {r}, \mathbf {s})} h ^ {r s} x T _ {r s} \longrightarrow T
$$

which is exact in the sense that the right arrow is the cokernel of the pair of arrows. Since the three functors from bisimplicial spaces to spaces under consideration commute with inductive limits, the lemma follows.

Proof of Theorem A. Let $S(f)$ be the category whose objects are triples $(X,Y,v)$ with $X$ an object of $\underline{C}$ and $v: Y \to fX$ a map in $\underline{C}'$, and in which a morphism from $(X,Y,v)$ to $(X',Y',v')$ is a pair of arrows $u: X \to X'$, $w: Y' \to Y$ such that $v' = f(u)vw$. (Thus $S(f)$ is the cofibred category over $\underline{C} \times \underline{C}'^0$ defined by the functor $(X,Y) \mapsto \text{Hom}(Y,fX)$.) We have functors

$$
\underline {{\underline {{C}}}} ^ {\circ} \xleftarrow {p _ {2}} \quad S (f) \quad \xrightarrow {p _ {1}} \underline {{\underline {{C}}}}
$$

given by  $p_{1}(X,Y,v) = X, \quad p_{2}(X,Y,v) = Y.$

Let $T(f)$ be the bisimplicial set such that an element of $T(f)_{pq}$ is a pair of diagrams

$$
\left(\mathrm{Y} _ {\mathrm{p}} \rightarrow \dots \rightarrow \mathrm{Y} _ {\mathrm{o}} \rightarrow \mathrm{fX} _ {\mathrm{o}}, \mathrm{X} _ {\mathrm{o}} \rightarrow \dots \rightarrow \mathrm{X} _ {\mathrm{q}}\right)
$$

in $\underline{\underline{C}}'$ and $\underline{\underline{C}}$ respectively, and such that the i-th face in the p-(resp. q-)direction deletes the object $Y_{i}$ (resp $X_{i}$) in the obvious way. Forgetting the first component gives a map of bisimplicial sets

$$
\mathrm{T} (f) _ {\mathrm{pq}} \longrightarrow \mathrm{NC} _ {= q}\tag{*}
$$

where the latter is constant in the p-direction. Since the diagonal simplicial set of T(f) is the nerve of the category S(f), it is clear that the realization of (\*) is the map  $\mathrm{Bp}_{1}:\mathrm{BS}(f)\longrightarrow\mathrm{BC}$ . (By the realization of a bisimplicial set we mean the space described in the above lemma, where the bisimplicial set is regarded as a bisimplicial space in the obvious way.) On the other hand, realizing (\*) with respect to p gives a map of simplicial spaces

$$
\underset {X _ {o} \rightarrow \dots \rightarrow X _ {q}} {\text { 丨   丨 }} B (\underset {=} {C ^ {\prime}} / f X _ {o}) ^ {o} \quad \longrightarrow \underset {X _ {o} \rightarrow \dots \rightarrow X _ {q}} {\text { 丨   丨 }} p t = N C _ {= q}
$$

which is a homotopy equivalence for each q because the category  $C'/fX_{0}$  has a final object. Applying a basic result of May and Tornehave ([Tornehave, A.3]), or the lemma below (Th. B), we see the realization of (\*) is a homotopy equivalence. Thus the functor  $p_{i}$  is a homotopy equivalence.

Similarly there is a map of bisimplicial sets $T(f)_{pq} \to N(C^{\prime 0})_p$ whose realization is the map $Bp_2: BS(f) \longrightarrow BC^{\prime 0}$. Realizing with respect to $q$, we obtain a map of simplicial spaces

$$
\bigcup_ {Y _ {o} \leftarrow \dots \leftarrow Y _ {p}} B (Y _ {o} \backslash f) \longrightarrow \bigcup_ {Y _ {o} \leftarrow \dots \leftarrow Y _ {p}} p t = N (\underline {{C}} ^ {\prime \circ}) _ {p}\tag{**}
$$

which is a homotopy equivalence for each $p$, because the categories $Y \setminus f$ are contractible by hypothesis. Thus we conclude that the functor $p_2$ is a homotopy equivalence.

But we have a commutative diagram of categories

![](images/page_11_image_1.jpg)

where $f'(X,Y,v) = (fX,Y,v)$. The horizontal arrows are homotopy equivalences by what has been proved, (note that $Y \backslash id_{\underline{C}} = Y \backslash \underline{C}'$ is contractible as it has an initial object).

Thus f is a homotopy equivalence, whence the theorem.

The exact homotopy sequence.

Let $g: E \to B$ be a map of topological spaces and let $b$ be a point of $B$. The homotopy-fibre of $f$ over $b$ is the space

$$
F (g, b) = E x _ {B} B ^ {I} x _ {B} \{b \}
$$

consisting of pairs $(\mathbf{e},\mathfrak{p})$ with $\mathbf{e}$ a point of $\mathbf{E}$ and $\mathfrak{p}$ a path joining $g(\mathbf{e})$ and $\mathbf{b}$. For any $\mathbf{e}$ in $g^{-1}(\mathfrak{b})$ one has the exact homotopy sequence of $\mathbf{g}$ with basepoint $\mathbf{e}$

$$
\longrightarrow \pi_ {i + 1} (B, b) \longrightarrow \pi_ {i} (F (g, b), \vec {e}) \longrightarrow \pi_ {i} (E, e) \xrightarrow {g *} \pi_ {i} (B, b) \longrightarrow .
$$

where  $\overline{e}=(e,\overline{b})$ ,  $\overline{b}$  denoting the constant path at b.

Let $f: \underline{\underline{C}} \to \underline{\underline{C}}'$ be a functor and $Y$ an object of $\underline{\underline{C}}'$. If $j: Y \setminus f \to \underline{\underline{C}}$ is the functor sending $(X, v: Y \to fX)$ to $X$, then $(X, v) \mapsto v: Y \to fX$ is a natural transformation from the constant functor with value $Y$ to $f_j$. Hence by Prop. 2 the composite $B(Y \setminus f) \to BC \to BC'$ contracts canonically to the constant map with image $Y$, and so we obtain a canonical map

$$
\mathrm{B} (\mathrm{Y} \backslash \mathrm{f}) \longrightarrow \mathrm{F} (\mathrm{Bf}, \mathrm{Y}).
$$

We want to know when this map is a homotopy equivalence, for then we have an exact sequence relating the homotopy groups of the categories $Y \setminus f, \underline{C}$ and $\underline{C}'$. Since the homotopy-fibres of a map over points connected by a path are homotopy equivalent, it is clearly necessary in order for the above map to be a homotopy equivalence for all $Y$, that the functor $Y' \setminus f \longrightarrow Y \setminus f$, $(X, v) \mapsto (X, vu)$ induced by $u: Y \longrightarrow Y'$ be a homotopy equivalence for every map $u$ in $\underline{C}'$. We are going to show the converse is true.

Because homotopy-fibres are not classifying spaces of categories, and hence are somewhat removed from what we ultimately will work with, it is convenient to formulate things in terms of homotopy-cartesian squares. Recall that a commutative square of spaces

![](images/page_11_image_14.jpg)

is called homotopy-cartesian if the map

$$
E ^ {\prime} \longrightarrow B ^ {\prime} x _ {B} B ^ {I} x _ {B} E, e ^ {\prime} \mapsto (g ^ {\prime} (e ^ {\prime}), \overline {{h g ^ {\prime} (b ^ {\prime})}}, h ^ {\prime} (e ^ {\prime}))
$$

from E' to the homotopy-fibre-product of h and g is a homotopy equivalence.

When $B'$ is contractible, the map $F(g', b') \to E'$ is a homotopy equivalence for any $b'$ in $B'$, hence one has a map $E' \to F(g, h(b'))$ unique up to homotopy. In this case the square is easily seen to be homotopy-cartesian if and only if $E' \to F(g, h(b'))$ is a homotopy equivalence.

A commutative square of categories will be called homotopy-cartesian if the corresponding square of classifying spaces is. With this terminology we have the following generalization of Theorem A.

Theorem B. Let $f: \underline{C} \longrightarrow \underline{C}'$ be a functor such that for every arrow $Y \to Y'$ in $\underline{C}'$, the induced functor $Y' \setminus f \longrightarrow Y \setminus f$ is a homotopy equivalence. Then for any object $Y$ of $\underline{C}'$ the cartesian square of categories

$$
\begin{array}{c c c} \mathrm{Y} \backslash f & \xrightarrow {\mathrm{j}} & \underline {{\mathrm{C}}} \\ \mathrm {f^ {\prime}} \Big \downarrow & & \Big \downarrow \mathrm{f} \\ \mathrm{Y} \backslash \underline {{\mathrm{C}}} ^ {\prime} & \xrightarrow {\mathrm{j} ^ {\prime}} & \underline {{\mathrm{C}}} ^ {\prime} \end{array}
$$

is homotopy-cartesian. Consequently for any X in  $f^{-1}(Y)$  we have an exact sequence
 $\rightarrow\pi_{i+1}(C',Y)\longrightarrow\pi_{i}(Y\backslash f,\bar{X})\xrightarrow{j_{*}}\pi_{i}(C,X)\xrightarrow{f_{*}}\pi_{i}(C',Y)\longrightarrow\ldots$

where $\overline{X} = (X, \mathrm{id}_{Y})$.

As with Theorem A, this result admits a dual formulation with the categories f/Y.

Corollary. Suppose $f: \underline{C} \to \underline{C}'$ is prefibred (resp. precofibred) and that for every arrow $u: Y \to Y'$ the base-change functor $u^*: f^{-1}(Y') \to f^{-1}(Y)$, (resp. the cobase-change functor $u_*: f^{-1}(Y) \to f^{-1}(Y' )$) is a homotopy equivalence. Then for any $Y$ in $\underline{C}'$, the category $f^{-1}(Y)$ is homotopy equivalent to the homotopy-fibre of $f$ over $Y$. (Precisely, the square

![](images/page_12_image_8.jpg)

where i is the inclusion functor, is homotopy-cartesian.) Consequently for any X in  $f^{-1}(Y)$  we have an exact homotopy sequence

$$
\rightarrow \pi_ {i + 1} (\underline {{C}}, Y) \longrightarrow \pi_ {i} (f ^ {- 1} (Y), X) \xrightarrow {i _ {*}} \pi_ {i} (\underline {{C}}, X) \xrightarrow {f _ {*}} \pi_ {i} (\underline {{C}}, Y) \longrightarrow .
$$

This is clear, since $f^{-1}(Y) \to Y \setminus f$ is a homotopy equivalence for prefibred $f$.

For the proof of the theorem we will need a lemma based on the theory of quasi-fibrations [Dold-Lashof], which is a special case of a general result about the realization of a map of simplicial spaces [Segal 2]. A quasi-fibration is a map $g: E \to B$ of spaces such that the canonical map $g^{-1}(b) \to F(g, b)$ induces isomorphisms on homotopy for all $b$ in $B$. When $E, B$ are in the class $\underline{W}$ of spaces having the homotopy type of a CW complex, one knows from [Milnor 2] that $F(g, b)$ is in $\underline{W}$. Thus if $g^{-1}(b)$ is also in $\underline{W}$, and $g$ is a quasi-fibration, we have that $g^{-1}(b) \to F(g, b)$ is a homotopy equivalence, i.e. the square

![](images/page_13_image_0.jpg)

is homotopy-cartesian.

Lemma. Let $i \mapsto X_i$ be a functor from a small category I to topological spaces, and let $g: X_I \to BI$ be the space over BI obtained by realizing the simplicial space

![](images/page_13_image_3.jpg)

If $X_{i} \to X_{i}$, is a homotopy equivalence for every arrow $i \to i'$ in $I$, then $g$ is a quasi-fibration.

Proof. It suffices by Lemma 1.5 of [Dold-Lashof] to show that the restriction of $g$ to the $p$-skeleton $F_p$ of BI is a quasi-fibration for all $p$. We have a map of cocartesian squares

![](images/page_13_image_6.jpg)

where the disjoint unions are taken over the nondegenerated p-simplices  $i_{o} \rightarrow \ldots \rightarrow i_{p}$  of NI. Let U be the open set of  $F_{p}$  obtained by removing the barycenters of the p-cells, and let  $V = F_{p} - F_{p-1}$ . It suffices by Lemma 1.4 of loc. cit. to show the restrictions of g to U, V and  $U \cap V$  are quasi-fibrations. This is clear for V and  $U \cap V$ , since over each p-cell g is a product map.

We will apply Lemma 1.3 of loc. cit. to $g|U$, assuming as we may by induction that $g|_{F_{p-1}}$ is a quasi-fibration, and using the evident fibre-preserving deformation $D$ of $g|U$ into $g|_{F_{p-1}}$ provided by the radial deformation of $\Delta^p$ minus barycenter onto $\partial \Delta^p$. We have only to check that if $D$ carries $x \in U$ into $x' \in F_{p-1}$, then the map $g^{-1}(x) \to g^{-1}(x')$ induced by $D$ induces isomorphisms of homotopy groups. Supposing $x \notin F_{p-1}$ as we may, let $x$ come from an interior point $z$ of the copy of $\Delta^p$ corresponding to the simplex $s = (i_0 \to \ldots \to i_p)$, and let the radial deformation push $z$ into the open face of $\Delta^p$ with vertices $j_0 < \ldots < j_q$. Then it is easy to see that $g^{-1}(x) = X_{i_0}$ and $g^{-1}(x') = X_k$, $k = i_{j_0}$, and that the map in question is the one $X_{i_0} \to X_k$ induced by the face $i_0 \to k$ of $s$. As these induced maps are homotopy equivalences by hypothesis, the proof of the lemma is complete.

Proof of Theorem B. We return to the proof of Theorem A. The functor $p_1: S(f) \to \underline{C}$ is a homotopy equivalence as before, but not necessarily the functor $p_2$. The map $Bp_2: BS(f) \to B(\underline{C}'0)$ is the realization of the map (\*\*). Thus applying the preceding lemma to the functor $Y \mapsto B(Y \setminus f)$ from $\underline{C}'0$ to spaces, we see that $Bp_2$ is a quasi-fibration, and hence the cartesian square

![](images/page_14_image_0.jpg)

is homotopy-cartesian. Consider now the diagram

![](images/page_14_image_2.jpg)

in which the squares are cartesian, and in which the sign $\sim$ denotes a homotopy equivalence. Since the square (1) + (3) is homotopy-cartesian, it follows that (1) is homotopy-cartesian, hence (1) + (2) is also, whence the theorem.

## §2. The K-groups of an exact category

Exact categories. Let $\underline{\underline{M}}$ be an additive category which is embedded as a full subcategory of an abelian category $\underline{\underline{A}}$, and suppose that $\underline{\underline{M}}$ is closed under extensions in $\underline{\underline{A}}$ in the sense that if an object $A$ of $\underline{\underline{A}}$ has a subobject $A'$ such that $A'$ and $A/A'$ are isomorphic to objects of $\underline{\underline{M}}$, then $A$ is isomorphic to an object of $\underline{\underline{M}}$. Let $\underline{\underline{E}}$ be the class of sequences

$$
0 \longrightarrow M ^ {\prime} \xrightarrow {i} M \xrightarrow {j} M ^ {\prime \prime} \longrightarrow 0\tag{1}
$$

in $\underline{\underline{M}}$ which are exact in the abelian category $\underline{\underline{A}}$. We call a map in $\underline{\underline{M}}$ an admissible monomorphism (resp. admissible epimorphism) if it occurs as the map i (resp. j) of some member (1) of $\underline{\underline{E}}$. Admissible monomorphisms and epimorphisms will sometimes be denoted $M' \longrightarrow M$ and $M \longrightarrow M''$, respectively.

The class $\underline{\mathbf{E}}$ clearly enjoys the following properties:

a) Any sequence in $\underline{\underline{M}}$ isomorphic to a sequence in $\underline{\underline{E}}$ is in $\underline{\underline{E}}$. For any $M', M''$ in $\underline{\underline{M}}$, the sequence

$$
0 \longrightarrow M ^ {\prime} \xrightarrow {(\mathrm{id} , 0)} M ^ {\prime} \oplus M ^ {\prime \prime} \xrightarrow {\operatorname{pr} _ {2}} M ^ {\prime \prime} \longrightarrow 0\tag{2}
$$

is in $\underline{\underline{E}}$. For any sequence (1) in $\underline{\underline{E}}$, i is a kernel for j and j is a cokernel for i in the additive category $\underline{\underline{M}}$.

b) The class of admissible epimorphisms is closed under composition and under base-change by arbitrary maps in M. Dually, the class of admissible monomorphisms is closed under composition and under cobase-change by arbitrary maps in M.

c) Let $M \to M''$ be a map possessing a kernel in $\underline{M}$. If there exists a map $N \to M$ in $\underline{M}$ such that $N \to M \to M''$ is an admissible epimorphism, then $M \to M''$ is an admissible epimorphism. Dually for admissible monomorphisms.

For example, suppose given a sequence (1) in $\underline{\underline{E}}$ and a map $f: N \to M^n$ in $\underline{\underline{M}}$. Form the diagram in $\underline{\underline{A}}$

![](images/page_15_image_0.jpg)

where P is a fibre product of f and j in A. Because M is closed under extensions in A, we can suppose P is an object of M. Hence the basechange of j by f exists in M and it is an admissible epimorphism.

Definition. An exact category is an additive category $\underline{\underline{M}}$ equipped with a family $\underline{\underline{E}}$ of sequences of the form (1), called the (short) exact sequences of $\underline{\underline{M}}$, such that the properties a), b), c) hold. An exact functor $F: \underline{\underline{M}} \to \underline{\underline{M}'}$ between exact categories is an additive functor carrying exact sequences in $\underline{\underline{M}}$ into exact sequences in $\underline{\underline{M}'}$.

Examples. Any abelian category is an exact category in an evident way. Any additive category can be made into an exact category in at least one way by taking $\underline{\mathbf{E}}$ to be the family of split exact sequences (2). A category which is 'abelian' in the sense of [Heller] is an exact category which is Karoubian (i.e. every projector has an image), and conversely.

Now suppose given an exact category $\underline{\underline{M}}$. Let $\underline{\underline{A}}$ be the additive category of additive contravariant functors from $\underline{\underline{M}}$ to abelian groups which are left exact, i.e. carry (1) to an exact sequence

$$
0 \longrightarrow F (M ^ {\prime \prime}) \longrightarrow F (M) \longrightarrow F (M ^ {\prime}).
$$

(Precisely, choose a universe containing $\underline{\underline{M}}$, and let $\underline{\underline{A}}$ be the category of left exact functors whose values are abelian groups in the universe.) Following well-known ideas (e.g. [Gabriel]), one can prove $\underline{\underline{A}}$ is an abelian category, that the Yoneda functor h embeds $\underline{\underline{M}}$ as a full subcategory of $\underline{\underline{A}}$ closed under extensions, and finally that a sequence (1) is in $\underline{\underline{E}}$ if and only if h carries it into an exact sequence in $\underline{\underline{A}}$. The details will be omitted, as they are not really important for the sequel.

The category QM.

If $\underline{\underline{M}}$ is an exact category, we form a new category $\underline{\underline{QM}}$ having the same objects as $\underline{\underline{M}}$ but with morphisms defined in the following way. Let $\underline{\underline{M}}$ and $\underline{\underline{M}'}$ be objects in $\underline{\underline{M}}$ and consider all diagrams

$$
M \xleftarrow {j} N \xrightarrow {i} M ^ {\prime}\tag{3}
$$

where $j$ is an admissible epimorphism and $i$ is an admissible monomorphism. We consider isomorphisms of these diagrams which induce the identity on $M$ and $M'$, such isomorphisms being unique when they exist. A morphism from $M$ to $M'$ in the category $Q\underline{M}$ is by definition an isomorphism class of these diagrams. Given a morphism from $M'$ to $M''$ represented by the diagram

$$
M ^ {\prime} \xleftarrow {j ^ {\prime}} N ^ {\prime} \xrightarrow {i ^ {\prime}} M ^ {\prime \prime}
$$

the composition of this morphism with the morphism from M to M' represented by (3) is the morphism represented by the pair  $j \cdot pr_{1}$ ,  $i' \cdot pr_{2}$  in the diagram

![](images/page_16_image_0.jpg)

It is clear that composition is well-defined and associative. Thus when the isomorphism classes of diagrams (3) form a set (e.g. if every object of $\underline{\underline{M}}$ has a set of subobjects) then $\underline{\underline{QM}}$ is a well-defined category. We assume this to be the case from now on.

It is useful to describe the preceding construction using admissible sub- and quotient objects. By an admissible subobject of M we will mean an isomorphism class of admissible monomorphisms $\mathbf{M}' \longrightarrow \mathbf{M}$, isomorphism being understood as isomorphism of objects over M. Admissible subobjects are in one-one correspondence with admissible quotient objects defined in the analogous way. The admissible subobjects of M form an ordered set with the ordering: $\mathbf{M}_1 \leqslant \mathbf{M}_2$ if the unique map $\mathbf{M}_1 \to \mathbf{M}_2$ over M is an admissible monomorphism. When $\mathbf{M}_1 \leqslant \mathbf{M}_2$, we call $(\mathbf{M}_1, \mathbf{M}_2)$ an admissible layer of M, and we call the cokernel $\mathbf{M}_2 / \mathbf{M}_1$ an admissible subquotient of M.

With this terminology, it is clear that a morphism from M to M' in QM may be identified with a pair  $((M_{1},M_{2}),\Theta)$  consisting of an admissible layer in M' and an isomorphism  $\Theta:M\approx M_{2}/M_{1}$ . Composition is the obvious way of combining an isomorphism of M with an admissible subquotient of M' and an isomorphism of M' with an admissible subquotient of M" to get an isomorphism of M with an admissible subquotient of M".

For example, the morphisms from O to M in QM are in one-one correspondence with the admissible subobjects of M. Isomorphisms from M to M' in QM are the same as isomorphisms from M to M' in M.

If $i: M' \longrightarrow M$ is an admissible monomorphism, then it gives rise to a morphism from $M'$ to $M$ in $QM$ which will be denoted

$$
\mathbf {i} _ {!}: \mathrm{M} ^ {\prime} \longrightarrow \mathrm{M}.
$$

Such morphisms will be called injective. Similarly, an admissible epimorphism $j: M \to M''$ gives rise to a morphism

$$
j ^ {!}: M ^ {\prime \prime} \rightarrow M
$$

and these morphisms will be called surjective. By definition, any morphism $u$ in QM can be factored $u = i_j j^!$, and this factorization is unique up to unique isomorphism. If we form the bicartesian square

(4)

![](images/page_16_image_11.jpg)

then $u = j' i'$, and this injective-followed-by-surjective factorization is also unique up to unique isomorphism. A map which is both injective and surjective is an isomorphism,

and it is of the form $\Theta_{!} = (\Theta^{-1})^{!}$ for a unique isomorphism $\Theta$ in $\underline{M}$.

Injective and surjective maps in $\underline{\underline{QM}}$ should not be confused with monomorphisms and epimorphisms in the categorical sense. Indeed, every morphism in $\underline{\underline{QM}}$ is a monomorphism. In fact, the category $\underline{\underline{QM}} / M$ is easily seen to be equivalent to the ordered set of admissible layers in $M$ with the ordering: $(M_0, M_1) \leqslant (M_0', M_1')$ if $M_0' \leqslant M_0 \leqslant M_1 \leqslant M_1'$.

We can use the operations $i \mapsto i_{!}$ and $j \mapsto j^{!}$ to characterize the category $QM$ by a universal property. First we note that these operations have the following properties:

a) If i and i' are composable admissible monomorphisms, then  $(i'i)! = i'!i!$ . Dually, if j and j' are composable admissible epimorphisms then  $(jj')! = j'!j!$ . Also  $(id_{M})! = (id_{M})! = id_{M}$ .

b) If (4) is a bicartesian square in which the horizontal (resp. vertical) maps are admissible monomorphisms (resp. epimorphisms), then $i, j' = j' i'$.

Now suppose given a category $\underline{\underline{\underline{C}}}$ and for each object M of $\underline{\underline{M}}$ an object hM of $\underline{\underline{C}}$, and for each i : M' $\rightarrow$ M (resp. j : M $\rightarrow$ M") a map i! ; hM' $\rightarrow$ hM (resp. j! : hM" $\rightarrow$ hM) such that the properties a), b) hold. Then it is clear that this data induces a unique functor $\underline{\underline{Q}}\underline{\underline{M}} \rightarrow \underline{\underline{C}}$, M $\mapsto$ hM compatible with the operations i $\mapsto$ i! and j $\mapsto$ j! in the two categories.

In particular, an exact functor $F: \underline{\underline{M}} \to \underline{\underline{M}'}$ between exact categories induces a functor $\underline{\underline{QM}} \to \underline{\underline{QM}'}$, $M \mapsto FM$, $i_! \mapsto (Fi)!$, $j! \mapsto (Fj)!$. We note also that if $\underline{\underline{M}^0}$ is the dual exact category, then we have an isomorphism of categories

$$
\mathrm{Q} (\underline {{\mathrm{M}}} ^ {\mathrm{O}}) = \mathrm{QM}\tag{5}
$$

such that the injective arrows in the former correspond to surjective arrows in the latter and conversely.

The fundamental group of QM. Suppose now that M is a small exact category, so that the classifying space B(QM) is defined. Let O be a given zero object of M.

Theorem 1. The fundamental group $\pi_{1}(B(QM),0)$ is canonically isomorphic to the Grothendieck group $K_{M}$.

Proof. The Grothendieck group is by definition the abelian group with one generator $[M]$ for each object $M$ of $\underline{M}$ and one relation $[M] = [M'][M'']$ for each exact sequence (1) in $\underline{M}$. We note that it could also be defined as the not-necessarily-abelian group with the same generators and relations, because the relations $[M'][M''] = [M' \oplus M''] = [M''][M']$ force the group to be abelian.

According to Prop. 1, the category of covering spaces of $B(QM)$ is equivalent to the category $\underline{F}$ of morphism-inverting functors $F: QM \to \text{Sets}$. It suffices therefore to show the group $K_{0}M$ acts naturally on $F(0)$ for $F$ in $\underline{F}$, and that the resulting functor from $\underline{F}$ to $K_{0}M - \text{sets}$ is an equivalence of categories.

Let $i_M : 0 \to M$ and $j_M : M \to O$ denote the obvious maps, and let $\underline{\underline{F}}'$ be the full subcategory of $\underline{\underline{F}}$ consisting of $F$ such that $F(M) = F(0)$ and $F(i_{M!}) = id_{F(0)}$ for all $M$. Clearly any $F$ is isomorphic to an object of $\underline{F}'$, so it suffices to show

$F'$ is equivalent to $K_{0}M - sets$.

Given a  $K_{0}=M$  - set S, let  $F_{S}: QM \rightarrow Sets$  be the functor defined by

$$
\mathbf {F} _ {\mathrm{S}} (\mathrm{M}) = \mathrm{S}, \mathbf {F} _ {\mathrm{S}} (\mathrm{i} _ {!}) = \mathrm{id} _ {\mathrm{S}}, \quad \mathbf {F} _ {\mathrm{S}} (\mathrm{j} ^ {!}) = \text { multiplication   by } \quad [ \text { Ker   j } ] \text { on   S },
$$

using the universal property of $\underline{\mathbf{QM}}$. Clearly $\mathbf{S} \mapsto \mathbf{F}_{\mathbf{S}}$ is a functor from $\underline{\mathbf{K}}\underline{\mathbf{M}} - \text{sets to} \underline{\mathbf{F}}'$. On the other hand if $\mathbf{F} \in \underline{\mathbf{F}}'$, then given $\mathbf{i}: \mathbf{M}' \to \mathbf{M}$ we have $\mathbf{i} \cdot \mathbf{i}_{\mathbf{M}'} = \mathbf{i}_{\mathbf{M}}$, hence $\mathbf{F}(\mathbf{i}_!') = \mathrm{id}_{\mathbf{F}(0)}$. Given the exact sequence

$$
0 \longrightarrow M ^ {\prime} \xrightarrow {i} M \xrightarrow {j} M ^ {n} \longrightarrow 0
$$

we have  $j^{!}i_{M^{m}!}=i_{!}j_{M}^{!}$ , hence  $F(j^{!})=F(j_{M}^{!})\in\operatorname{Aut}(F(0))$ . Also

$$
F (j _ {M} ^ {!}) = F (j ^ {!} j _ {M ^ {\prime \prime}} ^ {!}) = F (j _ {M ^ {\prime}} ^ {!}) F (j _ {M ^ {\prime \prime}} ^ {!})
$$

so by the universal property of $K_{0^{\underline{M}}}$, there is a unique group homomorphism from $K_{0^{\underline{M}}}$ to $\text{Aut}(F(0))$ such that $[M] \mapsto F(j_{M}^{!})$. Thus we have a natural action of $K_{0^{\underline{M}}}$ on $F(0)$ for any $F$ in $\underline{F}'$. In fact, it is clear that the resulting functor $F \mapsto F(0)$ from $\underline{F}'$ to $K_{0^{\underline{M}}}$-sets is an isomorphism of categories with inverse $S \mapsto F_S$, so the proof of the theorem is complete.

Higher K-groups. The above theorem offers some motivation for the following definition of K-groups for a small exact category M.

Definition.  $K_{i=M} = \pi_{i+1}(B(QM),0)$ .

Note first of all that the K-groups are independent of the choice of the zero object O. Indeed, given another zero object 0', there is a unique map  $0 \rightarrow 0'$  in  $Q_{M}$ , hence there is a canonical path from 0 to 0' in the classifying space.

Secondly we note that the preceding definition extends to exact categories having a set of isomorphism classes of objects. We define $K_{1}M$ to be $K_{1}M'$, where $M'$ is a small subcategory equivalent to $M$, the choice of $M'$ being irrelevant by Prop. 2. From now on we will only consider exact categories whose isomorphism classes form a set, except when mentioned otherwise. In addition, when we apply the results of §1, it will be tacitly assumed that we have replaced any large exact category by an equivalent small one.

Elementary properties of K-groups. An exact functor $f: \underline{\underline{M}} \to \underline{\underline{M}'}$ induces a functor $\underline{\underline{QM}} \to \underline{\underline{QM}'}$, and hence a homomorphism of K-groups which will be denoted

$$
f _ {\star}: K _ {i} M \longrightarrow K _ {i} M ^ {\prime}.\tag{6}
$$

In this way  $K_{i}$  becomes a functor from exact categories and exact functors to abelian groups. Moreover, isomorphic functors induce the same map on K-groups by Prop. 2. From (5) we have

$$
\mathrm{K} _ {\mathbf {i}} (\underset {=} {\mathrm{M} ^ {0}}) = \mathrm{K} _ {\mathbf {i} =} \mathrm{M}.\tag{7}
$$

The product $\underline{\underline{M}}\times\underline{\underline{M}'}$ of two exact categories is an exact category in which a sequence is exact when its projections in $\underline{\underline{M}}$ and $\underline{\underline{M}'}$ are. Clearly $Q(\underline{\underline{M}}\times\underline{\underline{M}'}) = Q\underline{\underline{M}}\times\underline{\underline{Q}\underline{M}'}$. Since the classifying space functor is compatible with products (S1, (4)), we have

$$
\mathrm{K} _ {\underline {{1}}} (\underline {{M}} \times \underline {{M ^ {\prime}}}) \simeq \mathrm{K} _ {\underline {{1}} \underline {{M}}} \oplus \mathrm{K} _ {\underline {{1}} \underline {{M ^ {\prime}}}}, \quad x \mapsto \operatorname{pr} _ {1 *} (x) + \operatorname{pr} _ {2 *} (x).\tag{8}
$$

The functor $\oplus: \underline{\underline{\mathbf{M}}}\times\underline{\underline{\mathbf{M}}}\to\underline{\underline{\mathbf{M}}}$, $(\mathbf{M},\mathbf{M}')\mapsto\mathbf{M}\oplus\mathbf{M}'$ is exact, so it induces a homomorphism

$$
K _ {i} \underset {=} {M} \oplus K _ {i} \underset {=} {M} = K _ {i} (\underset {=} {M} x \underset {=} {M}) \xrightarrow {\oplus_ {*}} K _ {i} \underset {=} {M}.
$$

This map coincides with the sum in the abelian group  $K_{i}M$  because the functors  $M \mapsto 0 \oplus M$ ,  $M \mapsto M \oplus 0$  are isomorphic to the identity.

Let $j \mapsto \underline{M}_{j}$ be a functor from a small filtering category to exact categories and functors, and let $\varinjlim M_{j}$ be the inductive limit of the $\underline{M}_{j}$ in the sense of Prop. 3. Then $\varinjlim M_{j}$ is an exact category in a natural way, and $Q(\varinjlim M_{j}) = \varinjlim QM_{j}$, hence from Prop. 3 we obtain an isomorphism

$$
\mathrm{K} _ {\mathbf {i}} (\underset {\rightarrow} {\lim} \underset {\equiv j} {\mathrm{M}}) = \underset {\rightarrow} {\lim} \mathrm{K} _ {\mathbf {i}} \underset {\equiv j} {\mathrm{M}}.\tag{9}
$$

Example. Let $A$ be a ring with 1 and let $\underline{P}(A)$ denote the additive category of finitely generated projective (left) $A$-modules. We regard $\underline{P}(A)$ as an exact category in which the exact sequences are those sequences which are exact in the category of all $A$-modules, and we define the $K$-groups of the ring $A$ by

$$
\mathrm{K} _ {\mathbf {i}} \mathrm{A} = \mathrm{K} _ {\mathbf {i}} (\underline {{\mathrm{P}}} (\mathrm{A})).
$$

A ring homomorphism $A \to A'$ induces an exact functor $A' \otimes_A ? : \underline{P}(A) \to \underline{P}(A')$ which is defined up to canonical isomorphism, hence it induces a well-defined homomorphism

$$
\left(\mathrm{A} ^ {\prime} \otimes_ {\mathrm{A}}?\right) _ {*} \colon \mathrm{K} _ {\mathbf {i}} \mathrm{A} \longrightarrow \mathrm{K} _ {\mathbf {i}} \mathrm{A} ^ {\prime}.\tag{10}
$$

making  $K_{i}A$  a covariant functor of A. From (8) we have

$$
\mathrm{K} _ {\mathbf {i}} (\mathrm{A} \times \mathrm{A} ^ {\prime}) = \mathrm{K} _ {\mathbf {i}} \mathrm{A} \oplus \mathrm{K} _ {\mathbf {i}} \mathrm{A} ^ {\prime}.\tag{11}
$$

If $j \mapsto A_j$ is a filtered inductive system of rings, we have from (9) an isomorphism

$$
\mathrm{K} _ {\mathbf {i}} (\underset {\rightarrow} {\lim} \mathrm{A} _ {\mathbf {j}}) = \underset {\rightarrow} {\lim} \mathrm{K} _ {\mathbf {i}} \mathrm{A} _ {\mathbf {j}}.\tag{12}
$$

(To apply (9), one replaces $\underline{\underline{P}}(A_j)$ by the equivalent category $\underline{\underline{P}}(A_j)$' whose objects are the idempotent matrices over $A_j$, so that $\underline{\underline{P}}(\varinjlim A_j)' = \varinjlim \underline{\underline{P}}(A_j)'$.) Finally we note that $P \mapsto \operatorname{Hom}_A(P, A)$ is an equivalence of $\underline{\underline{P}}(A)$ with the dual category to $\underline{\underline{P}}(A^{\text{op}})$, where $A^{\text{op}}$ is the opposed ring to $A$, hence from (7) we get a canonical isomorphism

$$
\mathrm{K} _ {\mathbf {i}} (\mathrm{A}) = \mathrm{K} _ {\mathbf {i}} (\mathrm{A} ^ {\mathrm{op}}).\tag{13}
$$

Remarks. It can be proved that the groups $K_{1}A$ defined here agree with those defined by making BGL(A) into an H-space and taking homotopy groups (see for example [Gersten 5]). In particular, they coincide for $i = 1, 2$ with the groups defined by by Bass and Milnor, and with the K-groups computed for a finite field in [Quillen 2]. On the other hand, for a general exact category $\underline{M}$, the group $K_{1}(\underline{M})$ is not the same as the universal determinant group defined in [Bass, p.389]. There is a canonical homomorphism from the universal determinant group to $K_{1}(\underline{M})$, but Gersten and Murthy have produced examples showing that it is neither surjective nor injective in general.

Let $\underline{\underline{M}}$ be an exact category and regard the family $\underline{\underline{E}}$ of short exact sequences in $\underline{\underline{M}}$ as an additive category in the obvious way. We denote objects of $\underline{\underline{E}}$ by E, E', etc. and let sE, tE, qE denote the sub-, total, and quotient objects of E, whence we have an exact sequence

$$
0 \longrightarrow s E \longrightarrow t E \longrightarrow q E \longrightarrow 0
$$

in $\underline{\underline{M}}$ associated to each object $E$ of $\underline{\underline{E}}$. A sequence in $\underline{\underline{E}}$ will be called exact if it gives rise to three exact sequences in $\underline{\underline{M}}$ on applying $s, t,$ and $q$. With this notion of exactness, it is clear that $\underline{\underline{E}}$ is an exact category, and that $s, t,$ and $q$ are exact functors from $\underline{\underline{E}}$ to $\underline{\underline{M}}$.

Theorem 2. The functor (s,q): QE → QM x QM is a homotopy equivalence.

Proof. It suffices by Theorem A to show the category $(s,q)/(M,N)$ is contractible for any given pair $M,N$ of objects of $\underline{M}$. Put $\underline{C} = (s,q)/(M,N)$; it is the fibred category over $\underline{QE}$ consisting of triples $(E,u,v)$, where $u: sE \to M$, $v: qE \to N$ are maps in $\underline{QM}$. Let $\underline{C}'$ be the full subcategory of $\underline{C}$ consisting of the triples $(E,u,v)$ such that $u$ is surjective, and let $\underline{C}''$ be the full subcategory of triples such that $u$ is surjective and $v$ is injective.

Lemma. The inclusion functors  $C' \rightarrow C$  and  $C'' \rightarrow C'$  have left adjoints.

Consider first the inclusion of $\underline{\underline{C}}'$ in $\underline{\underline{C}}$. Let $X = (E, u, v) \in \underline{\underline{C}}$; it suffices to show that there is a universal arrow $X \to \overline{X}$ in $\underline{\underline{C}}$ with $\overline{X}$ in $\underline{\underline{C}}'$.

Let $u = j'i_{!}$ where $i: sE \mapsto M'$, $j: M \twoheadrightarrow M'$, and define the exact sequence $i_E$ by 'pushout':

$$
\begin{array}{l} \text {E}: \quad \text {O} \longrightarrow \text {sE} \longrightarrow \text {tE} \longrightarrow \text {qE} \longrightarrow \text {O} \\ \text {i} _ {*} \text {E}: \quad \text {O} \longrightarrow \text {M} ^ {\prime} \longrightarrow \text {T} \longrightarrow \text {qE} \longrightarrow \text {O}. \end{array}
$$

Let $\overline{X} = (i_{*}E, j', v)$; it belongs to $\underline{\underline{C}}'$ and there is a canonical arrow $X \to \overline{X}$ given by the evident injective map $E \to i_{*}E$.

Now suppose given $X \to X'$ with $X' = (E', j', v')$ in $\underline{C}'$. Represent the map $E \to E'$ by the pair $E \to E_0$, $E' \to E_0$. Since

$$
\mathrm{sE} \longrightarrow \mathrm{sE} _ {\mathrm{o}} \ll - \mathrm{sE} ^ {\prime} \ll^ {\mathrm{j} ^ {\prime}} \mathrm{M}
$$

represents u, we can suppose  $E_{0}$  chosen so that  $sE \rightarrow sE_{0}$  is the map i, and  $M \longrightarrow sE_{0}$  is j. By the universal property of pushouts, the map  $E \rightarrow E_{0}$  factors uniquely  $E \rightarrow i_{*}E \rightarrow E_{0}$ , so it is clear that we have a map  $\overline{X} \rightarrow X'$  in  $C'$  such that  $X \rightarrow \overline{X} \rightarrow X'$  is the given map  $X \rightarrow X'$ .

It remains to show the uniqueness of the map $\overline{X} \to X'$. Consider factorizations $X \to X'' \to X'$ of $X \to X'$ such that $X''$ is in $\underline{\underline{C}}'$. Note that $\underline{\underline{C}}/X' = \underline{\underline{QE}}/E'$ is equivalent to the ordered set of admissible layers in $E'$. Let $(E_0, E_1)$ be the layer corresponding to $X \to X'$ and $(E_0'', E_1'')$ the layer corresponding to $X'' \to X'$ so that

$(E_{0}, E_{1}) \leqslant (E_{0}^{\prime\prime}, E_{1}^{\prime\prime})$ and $sE_{1}^{\prime\prime} = sE^{\prime}$. There is a least such layer $(E_{0}^{\prime\prime}, E_{1}^{\prime\prime})$ given by $tE_{0}^{\prime\prime} = tE_{0}$, $tE_{1}^{\prime\prime} = sE^{\prime} + tE_{1}$, which is characterized by the fact that the map $E_{1}/E_{0} \to E_{1}^{\prime\prime}/E_{0}^{\prime\prime}$ is injective and induces an isomorphism on quotient objects. Thus among the factorizations $X \to X^{\prime\prime} \to X^{\prime}$ there is a least one, unique up to canonical isomorphism, and characterized by the condition that $E \to E^{\prime\prime}$ should be injective and induce an isomorphism $qE \cong qE^{\prime\prime}$. Since the factorization $X \to \overline{X} \to X^{\prime}$ has this property, it is clear that the map $\overline{X} \to X^{\prime}$ is uniquely determined. Thus $C^{\prime} \to C$ has the left adjoint $X \mapsto \overline{X}$.

Next consider the inclusion of $\underline{\underline{C}}''$ in $\underline{\underline{C}}'$, and let $(E, u, v) \in \underline{\underline{C}}'$. Represent $v: qE \to N$ by the pair $j: N' \longrightarrow qE$, $i: N' \longrightarrow N$, and define $j^*E$ by pull-back:

![](images/page_21_image_2.jpg)

One verifies by an argument essentially dual to the preceding one that $(E, u, v) \mapsto (j^* E, u, i_!)$ is left adjoint to the inclusion of $\underline{C}''$ in $\underline{C}'$. This finishes the lemma. By Prop. 2, Cor. 1, the categories $\underline{C}$ and $\underline{C}''$ are homotopy equivalent. Let $(E, j_!, i_!)) \in \underline{C}''$, and let $j_M: M \to O$ and $i_N: O \to N$ be the obvious maps. A map from $(O, j_M', i_{N!})$ to $(E, j_!, i_!)$ may be identified with an admissible subobject $E'$ of $E$ such that $sE' = sE$ and $qE' = 0$. Clearly $E'$ is unique, so $(O, j_M', i_{N!})$ is an initial object of $\underline{C}''$. Thus $\underline{C}''$, and hence $\underline{C}$ is contractible, which finishes the proof of the theorem.

Corollary 1. Let M' and M be exact categories and let

$$
0 \longrightarrow F ^ {\prime} \longrightarrow F \longrightarrow F ^ {\prime \prime} \longrightarrow 0
$$

be an exact sequence of exact functors from M' to M. Then

$$
F _ {*} = F _ {*} ^ {\prime} + F _ {*} ^ {\prime \prime}: K _ {i =} M ^ {\prime} \rightarrow K _ {i =} M.
$$

Proof. It clearly suffices to treat the case of the exact sequence

$$
0 \longrightarrow s \longrightarrow t \longrightarrow q \longrightarrow 0
$$

of functors from $\underline{\underline{E}}$ to $\underline{\underline{M}}$. Let $f: \underline{\underline{M}} \times \underline{\underline{M}} \to \underline{\underline{E}}$ be the exact functor sending $(M', M'')$ to the split exact sequence

$$
0 \longrightarrow M ^ {\prime} \longrightarrow M ^ {\prime} \oplus M ^ {\prime \prime} \longrightarrow M ^ {\prime \prime} \longrightarrow 0.
$$

The functors tf and  $\oplus(s,q)f$  are isomorphic, hence

$$
t _ {*} f _ {*} = \oplus_ {*} (s _ {*}, q _ {*}) f _ {*} = (s _ {*} + q _ {*}) f _ {*}: (K _ {i} M) ^ {2} \rightarrow K _ {i} M.
$$

But $f_*$ is a section of $(s_*, q_*) : K_{i=1}^E \to (K_{i}M)^2$ which is an isomorphism by the theorem. Thus $t_* = s_* + q_*$, proving the corollary.

Note that the category of functors from a category $\underline{\underline{C}}$ to an exact category $\underline{\underline{M}}$ is an exact category in which a sequence of functors is exact if it is pointwise exact. We thus have the notion of an admissible filtration $0 = F_0 \subset F_1 \subset \ldots \subset F_n = F$ of a functor $F$. This means that $F_{p-1}(X) \hookrightarrow F_p(X)$ is an admissible monomorphism in $\underline{\underline{M}}$ for every $X$

in $\underline{\underline{C}}$, and it implies that there exist quotient functors $F_{p}/F_{q}$ for $q \leq p$, determined up to canonical isomorphism. It is easily seen that if $\underline{\underline{C}}$ is an exact category, and if the functors $F_{p}/F_{p-1}$ are exact for $1 \leqslant p \leqslant n$, then all the quotients $F_{p}/F_{q}$ are exact.

Corollary 2. (Additivity for 'characteristic' filtrations) Let $F: M' \to M$ be an exact functor between exact categories equipped with an admissible filtration $0 = F_0 < \ldots < F_n = F$ such that the quotient functors $F_p / F_{p-1}$ are exact for $1 \leqslant p \leqslant n$. Then

$$
F _ {*} = \sum_ {p = 1} ^ {n} \left(F _ {p} / F _ {p - 1}\right) _ {*}: K _ {i =} M ^ {\prime} \longrightarrow K _ {i =} M.
$$

Corollary 3. (Additivity for 'characteristic' exact sequences) If

$$
0 \longrightarrow F _ {o} \longrightarrow \dots \longrightarrow F _ {n} \longrightarrow 0
$$

is an exact sequence of exact functors from M' to M, then

$$
\sum_ {p = 0} ^ {n} (- 1) ^ {p} \left(F _ {p}\right) _ {*} = 0: K _ {i =} M ^ {\prime} \rightarrow K _ {i =} M.
$$

These result from Cor. 1 by induction.

Applications. We give two simple examples to illustrate the preceding results.

Let $X$ be a ringed space, and put $K_{1}X = K_{1}P(X)$, where $P(X)$ is the category of vector bundles on $X$, (i.e. sheaves of $\underline{O}_{X}$-modules which are locally direct factors of $\underline{O}_{X}^{n}$) equipped with the usual notion of exact sequence. Given $E$ in $P(X)$, we have an exact functor $E\otimes?: \underline{P}(X) \to \underline{P}(X)$ which induces a homomorphism of $K$-groups $(E\otimes?)_{*}: K_{1}X \to K_{1}X$. If $0 \longrightarrow E' \longrightarrow E \longrightarrow E'' \longrightarrow 0$ is an exact sequence of vector bundles, then Cor. 1 implies $(E\otimes?)_{*} = (E'\otimes?)_{*} + (E''\otimes?)_{*}$. Thus we obtain products

$$
\mathrm{K} _ {\mathrm{o}} \mathrm{X} \otimes_ {\mathbf {Z}} \mathrm{K} _ {\mathbf {i}} \mathrm{X} \longrightarrow \mathrm{K} _ {\mathbf {i}} \mathrm{X}, [ \mathrm{E} ] \otimes \mathrm{x} \mapsto (\mathrm{E} \otimes ?) _ {*} \mathrm{x}\tag{1}
$$

which clearly make  $K_{i}X$  into a module over  $K_{o}X$ . (Products  $K_{i}X \otimes K_{j}X \rightarrow K_{i+j}X$  can also be defined, but this requires more machinery.)

Graded rings. Let $A = A_0 \oplus A_1 \oplus \ldots$ be a graded ring and denote by $\underline{\underline{Pgr}}(A)$ the category of graded finitely generated projective A-modules $P = \oplus P_n, n \in \mathbb{Z}$. The group $K_1(Pgr(A))$ is a $Z[t, t^{-1}]$-module, where multiplication by $t$ is the automorphism induced by the translation functor $P \mapsto P(-1), P(-1)_n = P_{n-1}$.

Proposition. There is a $\mathbb{Z}[t,t^{-1}]$ -module isomorphism

$$
\mathbb {Z} \left[ t, t ^ {- 1} \right] \otimes_ {\mathbb {Z}} K _ {i A _ {0}} \stackrel {{\sim}} {{\longrightarrow}} K _ {i} (\underline {{{P}}} g r (A)), 1 \otimes x \mapsto (A \otimes_ {A _ {0}}?) _ {*} x.
$$

Proof. Given $P$ in $\underline{\underline{Pgr}}(A)$, let $F_k P$ be the $A$-submodule of $P$ generated by $P_n$ for $n \leq k$, and let $\underline{\underline{P}}_{=q}$ be the full subcategory of $\underline{\underline{Pgr}}(A)$ consisting of those $P$ for which $F_{-q-1} P = 0$ and $F_q P = P$. We have an exact functor

$$
\mathrm{T}: \underline {{\underline {{\mathrm{Pgr}}}}} (\mathrm{A}) \longrightarrow \underline {{\underline {{\mathrm{Pgr}}}}} (\mathrm{A} _ {\mathrm{o}}), \quad \mathrm{T} (\mathrm{P}) = \mathrm{A} _ {\mathrm{o}} \otimes_ {\mathrm{A}} \mathrm{P}
$$

where  $A_{0}$  is considered as a graded ring concentrated in degree zero. It is known ([Bass], p.637) that P is non-canonically isomorphic to

$$
\mathrm{A} \otimes_ {\mathrm{A} _ {\mathrm{o}}} \mathrm{T} (\mathrm{P}) = \prod_ {\mathrm{n}} \mathrm{A} (- \mathrm{n}) \otimes_ {\mathrm{A} _ {\mathrm{o}}} \mathrm{T} (\mathrm{P}) _ {\mathrm{n}}.
$$

It follows that $P \mapsto F_k P$ is an exact functor from $\underline{\mathrm{Pgr}}(A)$ to itself, and that there is a canonical isomorphism of exact functors

$$
F _ {n} P / F _ {n - 1} P \simeq A (- n) \otimes_ {A _ {0}} T (P) _ {n}.
$$

Applying Cor. 2 to the identity functor of $\mathbb{P}_{\underline{q}}$ and the filtration $0 = \mathbb{F}_{-q - 1} < \ldots < \mathbb{F}_q = \mathrm{id}$, one sees that the homomorphism

$$
\bigcup_ {- q \leqslant n \leqslant q} t ^ {n} \otimes K _ {i} A _ {o} \rightarrow K _ {i} P _ {= q}, t ^ {n} \otimes x \mapsto (A (- n) \otimes_ {A _ {o}}?) _ {*} x
$$

is an isomorphism with inverse given by the map with components $(\mathbb{T}_{n})_{*}$, $-q \leq n \leq q$. Since $\underline{\underline{Pgr}}(A)$ is the union of the $\underline{\underline{P}}_{=q}$, the proposition results from §2, (9).

## §4. Reduction by resolution

In this section $\underline{\underline{M}}$ denotes an exact category with a set of isomorphism classes, and $\underline{\underline{P}}$ a full subcategory closed under extensions in $\underline{\underline{M}}$ in the sense that $\underline{\underline{P}}$ contains a zero object and for any exact sequence in $\underline{\underline{M}}$

$$
\mathrm{O} \longrightarrow \mathrm{M} ^ {\prime} \longrightarrow \mathrm{M} \longrightarrow \mathrm{M} ^ {\prime \prime} \longrightarrow \mathrm{O}\tag{1}
$$

if M' and M" are isomorphic to objects of P, so is M. Such a P is an exact category where a sequence is exact if and only if it is exact in M. The category QP is a subcategory of QM which is not usually a full subcategory, as M-admissible monomorphisms and epimorphisms need not be P-admissible.

In the following, letters P, P', etc. will denote objects of $\underline{\underline{P}}$, and the symbols $\rightarrow$, $\rightarrow$, $\leqslant$ will always refer to $\underline{\underline{M}}$-admissible monomorphisms, epimorphisms and subobjects, respectively. The corresponding $\underline{\underline{P}}$-admissible notions will be specified explicitly. For example, P $\rightarrow$ P' denotes an $\underline{\underline{M}}$-admissible monomorphism between two objects of $\underline{\underline{P}}$; it is $\underline{\underline{P}}$-admissible iff the cokernel is isomorphic to an object of $\underline{\underline{P}}$.

We are interested in showing that the inclusion of $\underline{\underline{P}}$ in $\underline{\underline{M}}$ induces isomorphisms $K_{\underline{i}}\underline{P} \simeq K_{\underline{i}}\underline{M}$ when every object M of $\underline{\underline{M}}$ has a finite $\underline{\underline{P}}$-resolution:

$$
0 \longrightarrow P _ {n} \longrightarrow \dots \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0.\tag{2}
$$

The standard proof for $\mathbf{K}_0$ consists in defining an inverse map $\mathbf{K}_{\mathbf{O}} = \mathbf{K}_{\mathbf{O}} = \mathbf{K}_{\mathbf{P}}$ by showing $\sum_{i} (-1)^n [\mathbf{P}_n] \in \mathbf{K}_{\mathbf{O}} = \mathbf{K}_{\mathbf{P}}$ depends only on $[\mathbf{M}]$. By Cor. 3 of the preceding section, this method works when there exist resolutions (2) depending on $\mathbf{M}$ in an exact functorial fashion. However, this situation occurs rarely, so we must proceed differently.

The following theorem handles the case where resolutions of length one exist. As an example, think of $\underline{\underline{M}}$ as modules of projective dimension $\leqslant n$, and $\underline{\underline{P}}$ as the subcategory of modules of projective dimension $<n$. The general case follows by induction (see Cor. 1).

Theorem 3. Let P be a full subcategory of an exact category M which is closed under extensions and is such that

ii) For any M" in M, there exists an exact sequence (1) with M in P. Then the inclusion functor  $Q^{P} \rightarrow Q^{M}$  is a homotopy equivalence, so  $K_{i}P \simeq K_{i}M$ .

Proof. We factor  $Q_{P} \rightarrow Q_{M}$  into two inclusion functors

$$
\underline {{\mathrm{QP}}} \xrightarrow {\mathcal {G}} \underline {{\mathrm{C}}} \xrightarrow {\mathbf {f}} \underline {{\mathrm{QM}}}
$$

where $\underline{\mathbb{C}}$ is the full subcategory of $\underline{\mathbb{Q}\underline{\mathbb{M}}}$ with the same objects as $\underline{\mathbb{Q}\underline{\mathbb{P}}}$. We will prove $g$ and $f$ are homotopy equivalences.

To show $g$ is a homotopy equivalence, it suffices by Theorem A to prove $g / P$ is contractible for any object $P$ in $\underline{C}$. The category $g / P$ is easily seen to be equivalent to the ordered set $J$ of $\underline{M}$-admissible layers $(M_0, M_1)$ in $P$ such that $M_1 / M_0 \in \underline{P}$, with the ordering $(M_0, M_1) \prec (M_0', M_1')$ iff $M_0' \leqslant M_0 \leqslant M_1 \leqslant M_1'$ and $M_0 / M_0'$, $M_1' / M_1 \in \underline{P}$. By hypothesis i), one knows that $M_1$ and $M_0$ are in $\underline{P}$ for every $(M_0, M_1)$ in $J$. Hence in $J$ we have arrows

$$
\left(\mathrm{M} _ {\mathrm{o}}, \mathrm{M} _ {1}\right) \prec \left(\mathrm{O}, \mathrm{M} _ {1}\right) \succ (\mathrm{O}, \mathrm{O})
$$

which can be viewed as natural transformations of functors from J to J joining the functor $(\mathbf{M}_0,\mathbf{M}_1)\mapsto (0,\mathbf{M}_1)$ to the identity and to the constant functor with value $(0,0)$. Using Prop. 2, we see that J, hence $g / P$, is contractible, so $g$ is a homotopy equivalence.

To prove $f$ is a homotopy equivalence, we show $M \setminus f$ is contractible for any $M$ in $\underline{\underline{Q}}M$. Put $\underline{\underline{F}} = M \setminus f$; it is the cofibred category over $\underline{\underline{C}}$ consisting of pairs $(P, u)$ with $u: M \to P$ a map in $\underline{\underline{Q}}M$. Let $\underline{\underline{F}}'$ be the full subcategory consisting of $(P, u)$ with $u$ surjective. Given $X = (P, u)$ in $\underline{\underline{F}}$, write $u = i_j j!$ with $j: \overline{P} \to M$, $i: \overline{P} \to P$. By hypothesis $i)$, $\overline{P}$ is in $\underline{\underline{P}}$ as the notation suggests. Thus $\overline{X} = (\overline{P}, j!)$ is an object of $\underline{\underline{F}}'$, and $i$ defines a map $\overline{X} \to X$. One verifies easily that $\overline{X} \to X$ is a universal arrow from an object of $\underline{\underline{F}}'$ to $X$, hence $X \mapsto \overline{X}$ is right adjoint to the inclusion of $\underline{\underline{F}}'$ in $\underline{\underline{F}}$. By Prop. 2, Cor. 1, we have only to prove that $\underline{\underline{F}}'$ is contractible.

The dual category $\underline{\underline{F}^{\prime\circ}}$ is the category whose objects are maps $P \longrightarrow M$, and in which a morphism from $P \longrightarrow M$ to $P^{\prime} \longrightarrow M$ is a map $P \longrightarrow P^{\prime}$ such that the obvious triangle commutes. By hypothesis ii), there is at least one such object $P_{0} \longrightarrow M$. Given another $P \longrightarrow M$, the fibre product $Px_{M}P_{0}$ is an object of $\underline{\underline{P}}$, as it is an extension of $P_{0}$ by $\operatorname{Ker}(P \rightarrow M)$ which is in $\underline{\underline{P}}$ by hypothesis i). Hence in $\underline{\underline{F}^{\prime\circ}}$ we have arrows

$$
(P \rightarrow M) \leftarrow (P x _ {M} P _ {o} \rightarrow M) \rightarrow (P _ {o} \rightarrow M)
$$

which may be viewed as natural transformations from the functor $(P \to M) \mapsto (P \times_{M} P_{0} \to M)$ to the constant functor with value $P_{0} \to M$ and to the identity functor. Using Prop. 2, we conclude that $\underline{F'}$ is contractible, finishing the proof of the theorem.

Corollary 1. Assume P is closed under extensions in M and further that
a) For every exact sequence (1), if M, M" are in P, then so is M'.
b) Given j: M → P, there exists j': P' → P and f: P' → M such that
jf = j'. (This holds, for example, if for every M there exists P' → M.)
Let P = n be the full subcategory of M consisting of M having P-resolutions of length ≤n, i.e. such that there exists an exact sequence (2), and put P = ∪P = n. Then

$$
\mathrm{K} _ {\mathbf {i}} \mathrm{P} \stackrel {{\sim}} {{=}} \mathrm{K} _ {\mathbf {i}} \mathrm{P} _ {\mathbf {i} = 1} \stackrel {{\sim}} {{=}} \dots \stackrel {{\sim}} {{=}} \mathrm{K} _ {\mathbf {i}} \mathrm{P} _ {\mathbf {i} = \infty}.
$$

That $\underline{\underline{P}}_{=n}$ is closed under extensions in $\underline{\underline{M}}$, and hence the groups $K_{i=n}P$ are defined results from the following standard facts (compare [Bass, p.39]).

Lemma. For any exact sequence (1) and integer $n \geqslant 0$, we have

1)  $M \in P_{=n}$ ,  $M'' \in P_{=n+1} \implies M' \in P_{=n}$

2) $M', M'' \in P_{=n+1} \implies M \in P_{=n+1}$

3) M, M'' ∈ P = n+1  ⇒ M' ∈ P = n+1 .

Assuming this, we apply Theorem 3 to the pair $\underline{\underline{P}}_{\underline{n}} \subset \underline{\underline{P}}_{\underline{n+1}}$. Hypothesis ii) is satisfied, for given $M \in \underline{\underline{P}}_{\underline{n+1}}$, there exists an $\underline{\underline{M}}$-admissible epimorphism $P \to M$ with $P \in \underline{\underline{P}}$; and by 1) it is $\underline{\underline{P}}_{\underline{n+1}}$-admissible. The other hypotheses are clear, so $K_{i=n} \xrightarrow{\sim} K_{i=n+1}$ for each n. The case of $\underline{\underline{P}}_{\underline{n}}$ follows by passage to the limit (§2, (9)).

To prove the lemma, it suffices by a simple induction to treat the case n = 0.

1): Since $M'' \in \underline{P}_{\underline{1}}$, there exists a short exact sequence $P' \to P \to M''$, so we can form the diagram on the left with short exact rows and columns

![](images/page_25_image_8.jpg)

and with $\mathbf{F} = M \times_{M''}\mathbb{P}$. Since $P'$, $M$ are in $\underline{\underline{P}}$ and $\underline{\underline{P}}$ is closed under extensions, we have $F \in \underline{\underline{P}}$. Since $F, P \in \underline{\underline{P}}$ we have from a) that $M' \in \underline{\underline{P}}$, proving 1).

2): Since $M'' \in \underline{\underline{P}}_1$, there exists $P \to M''$, so applying b) to $\text{pr}_1: P \times_{M''} M \to P$, we can enlarge $P$ and find $P'' \to M$ factoring into $P'' \to M \to M''$. Thus we can form the above diagram on the right with short exact rows and columns, and with $P'$, $R' \in \underline{\underline{P}}_1$ as $M' \in \underline{\underline{P}}_1$. Applying 1) we see that $R'' \in \underline{\underline{P}}_1$, so $R \in \underline{\underline{P}}_1$ and $M \in \underline{\underline{P}}_1$, proving 2).

3): Since $M \in \underline{P}_1$, we can form the diagram with short exact rows and columns

![](images/page_25_image_12.jpg)

As $M^{*} \in \underline{P}_{=1}$, 1) implies $K \in \underline{P}$, so $M' \in \underline{P}_{=1}$, proving 3). The lemma and Cor. 1 are done.

As an example of the corollary, take $\underline{\underline{P}} = \underline{\underline{P}}(A)$ and $\underline{\underline{M}} = \text{Mod}(A)$, the category of (left) A-modules. (Better, so that $\underline{\underline{M}}$ has a set of isomorphism classes, take $\underline{\underline{M}}$ to be the abelian category of all A-modules of cardinality $<\alpha$, where $\alpha$ is some infinite cardinal $>\text{card}(A)$.) Let $\underline{\underline{P}}_{=n}(A)$ be the category of A-modules having $\underline{\underline{P}}$-resolutions of length $\leqslant n$, and $\underline{\underline{P}}_{=00}(A) = \bigcup_{=n} P(A)$. Then $\underline{\underline{P}}_{=n}(A) = \underline{\underline{P}}_{=n}$ as in the corollary, so we obtain

Corollary 2. For $0 \leqslant n \leqslant \infty$, we have $K_{i}A \simeq K_{i}(P(A))$. In particular if $A$ is regular, then $K_{i}A \simeq K_{i}(\text{Modf}(A))$, where $\text{Modf}(A)$ is the category of finitely generated $A$-modules.

We recall that a regular ring is a noetherian ring such that every (left) module has finite projective dimension. For such a ring A we have  $P_{\mathrm{F0}}(A) = \mathrm{Modf}(A)$ .

Similarly, Cor. 1 implies that for a regular noetherian separated scheme the K-groups of the category of coherent sheaves and the category of vector bundles are the same, since every coherent sheaf has a finite resolution by vector bundles [SGA 6, II, 2.2].

Transfer maps. Let $f: A \to B$ be a ring homomorphism such that as an $A$-module $B$ is in $\underline{P}_{\underline{\infty}}(A)$. Then restriction of scalars defines an exact functor from $\underline{P}_{\underline{\infty}}(B)$ to $\underline{P}_{\underline{\infty}}(A)$, hence by Cor. 2 it induces a homomorphism of $K$-groups which we will denote

$$
f _ {*} \colon K _ {i} B \longrightarrow K _ {i} A\tag{3}
$$

and call the transfer map with respect to f. Clearly given another homomorphism $g: B \to C$ with $C \in P_{\infty}(B)$, we have

$$
(g f) _ {*} = f _ {*} g _ {*}: K _ {1} C \longrightarrow K _ {1} A.\tag{4}
$$

We suppose now for simplicity that A and B are commutative, so that we have functors

$$
\underline {{\mathrm{P}}} (\mathrm{A}) \times \underline {{\mathrm{P}}} _ {\mathrm{n}} (\mathrm{A}) \longrightarrow \underline {{\mathrm{P}}} _ {\mathrm{n}} (\mathrm{A}), \quad (\mathrm{P}, \mathrm{M}) \mapsto \mathrm{P} \otimes_ {\mathrm{A}} \mathrm{M}.
$$

for $0 \leqslant n \leqslant \infty$, which induce a product $K_{0}A \otimes K_{1}A \to K_{1}A$, $[P] \otimes z \mapsto (P \otimes_{A}?)_z$, and similarly for B. Then if $f^{*} = (B \otimes_{A} ?)_*: K_{1}A \to K_{1}B$, we have the projection formula

$$
\mathbf {f} _ {*} \left(\mathbf {f} ^ {*} \mathbf {x} \cdot \mathbf {y}\right) = \mathbf {x} \cdot \mathbf {f} _ {*} \mathbf {y}\tag{5}
$$

for $\mathbf{x} \in \mathbf{K}_0\mathbf{A}$ and $\mathbf{y} \in \mathbf{K}_1\mathbf{B}$. This results immediately from the fact that for $X$ in $\underline{\underline{\mathbf{P}}}(A)$ there is an isomorphism of exact functors

$$
\mathrm{Y} \mapsto (\mathrm{B} \otimes_ {\mathrm{A}} \mathrm{X}) \otimes_ {\mathrm{B}} \mathrm{Y} = \mathrm{X} \otimes_ {\mathrm{A}} \mathrm{Y}
$$

from $\underline{\mathbb{P}}_{= \infty}(\mathbb{B})$ to $\underline{\mathbb{P}}_{= \infty}(\mathbb{A})$.

Corollary 3. Let $T = \{T_i, i \geq 1\}$ be an exact connected sequence of functors from an exact category $M$ to an abelian category $A$ (i.e. for every exact sequence (1), we have a long exact sequence

$$
\longrightarrow \mathrm{T} _ {2} \mathrm{M} ^ {\prime \prime} \longrightarrow \mathrm{T} _ {1} \mathrm{M} ^ {\prime} \longrightarrow \mathrm{T} _ {1} \mathrm{M} \longrightarrow \mathrm{T} _ {1} \mathrm{M} ^ {\prime \prime}).
$$

Let $\underline{\underline{P}}$ be the full subcategory of T-acyclic objects (T$_n$M = 0 for all n ≥1), and assume for each M in $\underline{\underline{M}}$ that there exists P → M with P in $\underline{\underline{P}}$, and that T$_n$M = 0 for n sufficiently large. Then K$_1\underline{\underline{P}} \xrightarrow{\sim}$K$_1\underline{\underline{M}}$.

This results either from Cor. 1, or better by applying Theorem 3 directly to the inclusion $\mathbb{P}_{=n} \subset \mathbb{P}_{=n+1}$, where $\mathbb{P}_{=n}$ consists of $M$ such that $T_jM = 0$ for $j > n$.

Here is an application of this result. Put $K_{1}^{\prime}A = K_{1}(\text{Modf}(A))$ for $A$ noetherian, and let $f: A \to B$ be a homomorphism of noetherian rings. If $B$ is flat as a right $A$-module, then we obtain a homomorphism of $K$-groups

$$
(B \otimes_ {A}?): K _ {i} ^ {\prime} A \longrightarrow K _ {i} ^ {\prime} B\tag{6}
$$

because $B \otimes_{A} ?$ is exact. But more generally if $B$ is of finite Tor-dimension as a right A-module, then applying Cor. 3 to $\underline{M} = \text{Modf}(A)$ and $T_{n} M = \text{Tor}_{n}^{A}(B, M)$,

we find that $K_{\mathbf{i}} \underline{P} \simeq K_{\mathbf{i}}' \mathbf{A}$, where $\underline{P}$ is the full subcategory of $\text{Modf(A)}$ consisting of $M$ such that $T_{n}M = 0$ for $n > 0$. Since $B \otimes_{A}?$ is exact on $\underline{P}$, we obtain a homomorphism (6) in this more general situation.

## §5. Devissage and localization in abelian categories

In this section $\underline{\underline{A}}$ will denote an abelian category having a set of isomorphism classes of objects, and $\underline{\underline{B}}$ will be a non-empty full subcategory closed under taking subobjects, quotient objects, and finite products in $\underline{\underline{A}}$. Clearly $\underline{\underline{B}}$ is an abelian category and the inclusion functor $\underline{\underline{B}} \to \underline{\underline{A}}$ is exact. We regard $\underline{\underline{A}}$ and $\underline{\underline{B}}$ as exact categories in the obvious way, so that all monomorphisms and epimorphisms are admissible. Then $\underline{\underline{QB}}$ is the full subcategory of $\underline{\underline{QA}}$ consisting of those objects which are also objects of $\underline{\underline{B}}$.

Theorem 4. (Devissage) Suppose that every object M of A has a finite filtration $0 = M_0 \subset M_1 \subset \ldots \subset M_n = N$ such that $M_j / M_{j-1}$ is in B for each j. Then the inclusion functor $\mathbb{Q}\mathbb{B} \to \mathbb{Q}\mathbb{A}$ is a homotopy equivalence, so $K_i\mathbb{B} \xrightarrow{\sim} K_i\mathbb{A}$.

Proof. Denoting the inclusion functor by $f$, it suffices by Theorem A to prove that $f / M$ is contractible for any object $M$ of $\underline{A}$. The category $f / M$ is the fibred category over $\underline{QB}$ consisting of pairs $(N, u)$, where $N \in \underline{QB}$ and $u : N \to M$ is a map in $\underline{QA}$. By associating to $u$ what might be called its image, that is, the layer $(M_0, M_1)$ of $M$ such that $u$ is given by an isomorphism $N \simeq M_1 / M_0$, it is clear that we obtain an equivalence of $f / M$ with the ordered set $J(M)$ consisting of layers $(M_0, M_1)$ in $M$ such that $M_1 / M_0 \in \underline{B}$, with the ordering $(M_0, M_1) \leq (M_0', M_1')$ iff $M_0' \subset M_0 \subset M_1 \subset M_1'$.

By virtue of the hypothesis that M has a finite filtration with quotients in $\underline{\underline{B}}$, it will suffice to show the inclusion $i: J(M') \to J(M)$ is a homotopy equivalence whenever $M' \subset M$ is such that $M/M' \in \underline{B}$. We define functors

$$
\begin{array}{l l} \mathbf {r}: J (M) \longrightarrow J (M ^ {\prime}) & , \quad (M _ {o}, M _ {1}) \mapsto (M _ {o} \cap M ^ {\prime}, M _ {1} \cap M ^ {\prime}) \\ \mathbf {s}: J (M) \longrightarrow J (M) & , \quad (M _ {o}, M _ {1}) \mapsto (M _ {o} \cap M ^ {\prime}, M _ {1}). \end{array}
$$

These are well-defined because

$$
\mathrm{M} _ {1} \cap \mathrm{M} ^ {\prime} / \mathrm{M} _ {0} \cap \mathrm{M} ^ {\prime} \subset \mathrm{M} _ {1} / \mathrm{M} _ {0} \cap \mathrm{M} ^ {\prime} \subset \mathrm{M} _ {1} / \mathrm{M} _ {0} \times \mathrm{M} / \mathrm{M} ^ {\prime}
$$

and because $\underline{\underline{B}}$ is closed under subobjects and products by assumption. Note that $\mathbf{ri} = \mathrm{id}_{\mathbf{J}(\mathbf{M}^{\prime})}$ and that there are natural transformations $\mathbf{ir} \to \mathbf{s} \leftarrow \mathrm{id}_{\mathbf{J}(\mathbf{M})}$ represented by

$$
\left(\mathrm{M} _ {\circ} \cap \mathrm{M} ^ {\prime}, \mathrm{M} _ {1} \cap \mathrm{M} ^ {\prime}\right) \leqslant \left(\mathrm{M} _ {\circ} \cap \mathrm{M} ^ {\prime}, \mathrm{M} _ {1}\right) \geqslant \left(\mathrm{M} _ {\circ}, \mathrm{M} _ {1}\right).
$$

Hence by Prop. 2, r is a homotopy inverse for i, so the proof is complete.

Corollary 1. Let A be an abelian category (with a set of isomorphism classes) such that every object has finite length. Then

$$
K _ {i} \underset {=} {A} \simeq \prod_ {j \in J} K _ {i} D _ {j}
$$

where $\{X_{j}, j \in J\}$ is a set of representatives for the isomorphism classes of simple objects of $\underline{\underline{\mathbf{A}}}$, and $D_{j}$ is the sfield $\operatorname{End}(X_{j})^{\mathrm{op}}$.

Proof. From the theorem we have $K_{i}B = K_{i}A$, where $B$ is the subcategory of semi-simple objects, so we reduce to the case where every object of $A$ is semi-simple. Using the fact that $K$-groups commute with products and filtered inductive limits (§2, (8), (9)) we reduce to the case where $A$ has a single simple object $X$ up to isomorphism. But then $M \mapsto \operatorname{Hom}(X, M)$ is an equivalence of $A$ with $P(D)$, $D = \operatorname{End}(X)^{\mathrm{OP}}$, so the corollary follows.

Corollary 2. If I is a nilpotent two-sided ideal in a noetherian ring A, then  $K_{i}^{\prime}(A/I) \xrightarrow{\sim} K_{i}^{\prime}A$ , (notation as in §4,(6)).

This results by applying the theorem to the inclusion  $\text{Modf}(A/I) \subset \text{Modf}(A)$ .

Theorem 5. (Localization) Let B be a Serre subcategory of A, let A/B be the associated quotient abelian category (see for example [Gabriel], [Swan]), and let e: B → A, s: A → A/B denote the canonical functors. Then there is a long exact sequence
    s\* K₁(A/B) → K\_B e\* K\_A s\* K₀(A/B) → O .

(It will be clear from the proof that this exact sequence is functorial for exact functors $(\underline{\underline{A}},\underline{\underline{B}})\longrightarrow (\underline{\underline{A}}^{\prime},\underline{\underline{B}}^{\prime})$. Unfortunately the proof does not shed much light on the nature of the boundary map $\partial :K_{i+1}(\underline{\underline{A}}/\underline{\underline{B}})\longrightarrow K_{i}(\underline{\underline{B}})$, and further work remains to be done in this direction.)

Before taking up the proof of the theorem, we give an example.

Corollary. If A is a Dedekind domain with quotient field F, there is a long exact sequence

$$
\longrightarrow \mathrm{K} _ {\mathrm{i} + 1} \mathrm{F} \longrightarrow \bigsqcup_ {\mathrm{m}} \mathrm{K} _ {\mathrm{i}} (\mathrm{A} / \mathrm{m}) \longrightarrow \mathrm{K} _ {\mathrm{i}} \mathrm{A} \longrightarrow \mathrm{K} _ {\mathrm{i}} \mathrm{F} \longrightarrow ..
$$

where m runs over the maximal ideals of A.

This follows by applying the theorem to $\underline{\underline{A}} = \text{Modf}(A)$, with $\underline{\underline{B}}$ the subcategory of torsion modules, whence $\underline{\underline{A}}/\underline{\underline{B}}$ is equivalent to $\text{Modf}(F) = \underline{\underline{P}}(F)$, (compare [Swan, p. 115]). We have $K_{i}A = K_{i}A$ by Cor. 2 of Theorem 3, and $K_{i}B = \coprod_{i} K_{i}(A/m)$ by Theorem 4, Cor. 1. Note that the map $K_{i}A \to K_{i}F$ in the exact sequence is the one induced by the homomorphism $A \to F$ as in §2, (10), and the map $K_{i}(A/m) \to K_{i}A$ is the transfer map associated to the homomorphism $A \to A/m$ in the sense of the preceding section.

Proof of Theorem 5. Fix a zero object $O$ in $\underline{\underline{A}}$, and let $O$ also denote its image in $\underline{\underline{A}}/\underline{\underline{B}}$. One knows that $\underline{\underline{B}}$ is the full subcategory of $\underline{\underline{A}}$ consisting of $M$ such that $sM \cong 0$. Hence the composite of $Qe: \underline{\underline{QB}} \to \underline{\underline{QA}}$ with $Qs: \underline{\underline{QA}} \to Q(\underline{\underline{A}}/\underline{\underline{B}})$ is isomorphic to the constant functor with value $O$, so $Qe$ factors

$$
\begin{array}{l} \underline {{\underline {{Q B}}}} \xrightarrow {} O \backslash Q s \xrightarrow {} Q \underline {{\underline {{A}}}} \\ M \mapsto (M, O \simeq s M), (N, u) \mapsto N. \end{array}
$$

In view of Theorem B, §1, it suffices to establish the following assertions.

a) For every u : V' → V in Q(A/B), u\*: V \ Qs → V'\Qs is a homotopy equivalence.

b) The functor  $QB \longrightarrow O \setminus Qs$  is a homotopy equivalence.

Factoring u into injective and surjective maps, one sees that it suffices to prove a) when u is either injective or surjective. On the other hand, replacing a category by its dual does not change the Q-category (S2,(7)). As surjective maps in $Q(\underline{A}/\underline{B})$ become injective in $Q((\underline{A}/\underline{B})^0) = Q(\underline{A}^0/\underline{B}^0)$, it is enough to prove a) when u is injective, say $u = i_!$, $i: V' \to V$. Finally we have $i_! i_{V',!} = i_{V!}$, so it suffices to prove a) for the injective map $i_{V!}$ for any V in $\underline{A}/\underline{B}$.

Let $\underline{\underline{F}}_{V}$ be the full subcategory of $V \setminus Qs$ consisting of pairs $(M, u)$ such that $u: V \xrightarrow{\sim} sM$ is an isomorphism. Clearly $\underline{\underline{F}}_{0}$ is isomorphic to $\underline{\underline{QB}}$, so assertion b) results from the following.

Lemma 1. The inclusion functor $\underline{F}_{\underline{V}} \to V \setminus Qs$ is a homotopy equivalence.

Denoting this functor by $f$, it suffices by Theorem A to show the category $f/(M, u)$ is contractible for any object $(M, u)$ of $V \setminus \mathfrak{g}s$. Let the map $u: V \to sM$ in $Q(\underline{A}/\underline{B})$ be represented by an isomorphism $V \simeq V_1/V_0$, where $(V_0, V_1)$ is a layer in $sM$. It is easily seen that the category $f/(M, u)$ is equivalent to the ordered set of layers $(M_0, M_1)$ in $M$ such that $(sM_0, sM_1) = (V_0, V_1)$, with the ordering $(M_0, M_1) \leqslant (M'_0, M'_1)$ iff $M'_0 \subset M_0 \subset M_1 \subset M'_1$. This ordered set is directed because

$$
\left(M _ {0}, M _ {1}\right) \leqslant \left(M _ {0} \cap M _ {0} ^ {\prime}, M _ {1} + M _ {1} ^ {\prime}\right) \geqslant \left(M _ {0} ^ {\prime}, M _ {1} ^ {\prime}\right).
$$

It is non-empty because any subobject $V_1$ of sM is of the form $sM_1$ for some $M_1 \subset M$. In effect, $V_1 = sN$ for some N in $A$, and the map $V_1 \to sM$ can be represented as $s(g)s(i)^{-1}$ where $i: N' \to N$ has its cokernel in $B$ and $g: N' \to M$ is a map in $A$; then one can take $M_1$ to be the image of $g$. Thus $f/(M, u)$ is a filtering category, so it is contractible by Prop. 3, Cor. 2, proving the lemma.

The next four lemmas will be devoted to proving that the category $\underline{\mathbf{F}}_{\underline{\mathbf{V}}}$ is homotopy equivalent to $\underline{\mathbf{QB}}$. To this end we introduce the following auxiliary categories. Let $N$ be a given object of $\underline{\mathbf{A}}$, and let $\underline{\mathbf{E}}_{\underline{\mathbf{N}}}$ be the category having as objects pairs $(M,h)$, where $h:M\to N$ is a mod-$\underline{\mathbf{B}}$ isomorphism, i.e. a map in $\underline{\mathbf{A}}$ whose kernel and cokernel are in $\underline{\mathbf{B}}$, or equivalently one which becomes an isomorphism in $\underline{\mathbf{A}}/\underline{\mathbf{B}}$. A morphism from $(M,h)$ to $(M',h')$ in $\underline{\mathbf{E}}_{\underline{\mathbf{N}}}$ is by definition a map $u:M\to M'$ in $\underline{\mathbf{QA}}$ such that

$$
\begin{array}{c c c} M _ {1} & \xrightarrow {i} & M ^ {\prime} \\ j & \downarrow & \downarrow \\ M & \xrightarrow {h} & N \end{array} h ^ {\prime}\tag{*}
$$

commutes if $u = i_j j^!$. To each $(M, h)$ in $E_N$ we associate $\text{Ker}(h)$, which is an object of $B$ determined up to canonical isomorphism. To the map $(M, h) \to (M', h')$ represented by (\*) we associate the map in $QB$ represented by the maps

$$
\operatorname{Ker} (h) \xleftarrow {} \operatorname{Ker} (h j) \longrightarrow \operatorname{Ker} (h ^ {\prime})
$$

induced by j and i respectively. It is easily checked that in this way we obtain a functor

$$
k _ {N}: \underline {{E}} _ {N} \longrightarrow Q B, (M, h) \mapsto \operatorname{Ker} (h)
$$

determined up to canonical isomorphism. We prove  $k_{N}$  is a homotopy equivalence in two

steps.

Lemma 2. Let $\mathbb{E}_{\mathbb{N}}^{\prime}$ be the full subcategory of $\mathbb{E}_{\mathbb{N}}$ consisting of pairs (M,h) such that $h:M\to N$ is an epimorphism. Then the restriction $\mathbf{k}_{\mathbb{N}}^{\prime}:\mathbb{E}_{\mathbb{N}}^{\prime}\to \mathbb{Q}\mathbb{B}$ of $\mathbf{k}_{\mathbb{N}}$ is a homotopy equivalence.

It suffices to prove $k_N'/T$ is contractible for any $T$ in $\underline{QB}$. Put $\underline{C} = k_N'/T$; it is the fibred category over $\underline{E}_N'$ consisting of pairs $((M,h),u)$, with $(M,h)$ in $\underline{E}_N'$, and where $u: \text{Ker}(h) \to T$ is a map in $\underline{QB}$. Let $\underline{C}'$ be the full subcategory consisting of $((M,h),u)$ with $u$ surjective. Given $X = ((M,h),u)$ in $\underline{C}$, write $u = j'i!$ with $i: \text{Ker}(h) \to T_0$, $j: T \to T_0$ and define $(i_M, \overline{h})$ by 'pushout':

![](images/page_30_image_3.jpg)

Let $\overline{X} = ((i_{*}M, \overline{h}), j^{!})$; it belongs to $\underline{\underline{C}}'$ and there is an evident map $X \to \overline{X}$. One verifies as in the proof of Theorem 3 that $X \to \overline{X}$ is a universal arrow from $X$ to an object of $\underline{\underline{C}}'$. Hence the inclusion $\underline{\underline{C}}' \to \underline{\underline{C}}$ has the left adjoint $X \mapsto \overline{X}$, so we have reduced to proving that $\underline{\underline{C}}'$ is contractible. But $\underline{\underline{C}}'$ has the initial object $((N, id_N), j_T^!)$, so this is clear, whence the lemma.

Lemma 3. The functor $k_{N}: E_{N} \to QB$ is a homotopy equivalence.

Thanks to the preceding lemma, it suffices to show the inclusion $\underline{\underline{E}}_{\underline{\underline{N}}}^{\prime}\to\underline{\underline{E}}_{\underline{\underline{N}}}$ is a homotopy equivalence. Let $\underline{\underline{I}}$ be the ordered set of subobjects I of N such that N/I is in $\underline{\underline{B}}$, and consider the functor $f:\underline{\underline{E}}_{\underline{\underline{N}}}\to\underline{\underline{I}}$ sending $(M,h)$ to $\operatorname{Im}(h)$. One verifies easily that f is fibred, the fibre over I being $\underline{\underline{E}}_{\underline{\underline{I}}}^{\prime}$, and the base change functor from $\underline{\underline{E}}_{\underline{\underline{I}}}^{\prime}$ to $\underline{\underline{E}}_{\underline{\underline{J}}}^{\prime}$ being $Jx_{I}?:(M\longrightarrow I)\mapsto(Jx_{I}W\rightarrow J)$. Since $Jx_{I}?$ commutes with $k_{I}$ and $k_{J}$, it follows from Lemma 2 that $Jx_{I}?$ is a homotopy equivalence for every arrow $J\subset I$ in $\underline{\underline{I}}$. From Theorem B, Cor., we conclude $\underline{\underline{E}}_{\underline{\underline{I}}}^{\prime}$ is homotopy equivalent to the homotopy-fibre of f over I. Since $\underline{\underline{I}}$ is contractible (it has N for final object), one knows from homotopy theory that the inclusion $\underline{\underline{E}}_{\underline{\underline{I}}}^{\prime}\to\underline{\underline{E}}_{\underline{\underline{N}}}$ is a homotopy equivalence for each I, proving the lemma.

We now want to show $\underline{\underline{F}}_{\mathbf{V}}$ is homotopy equivalent to $\underline{\underline{E}}_{\mathbf{N}}$ when $\mathrm{sN} \cong \mathrm{V}$. First we note a simple consequence of the preceding.

Lemma 4. Let $g: N \to N'$ be a map in $\underline{A}$ which is a mod-$\underline{B}$ isomorphism. Then the functor $g_*: \underline{E}_N \to \underline{E}_N', (M, h) \mapsto (M, gh)$ is a homotopy equivalence.

One verifies easily that by associating to $(M,h)\in E_{\mathbb{N}}$ the obvious injective map $\operatorname{Ker}(h)\to \operatorname{Ker}(gh)$, one obtains a natural transformation from $k_N$ to $k_N,g_*$. (Observe: In 'lower' K-theory one calculates with matrices - in 'higher' K-theory with functors.) Thus $k_N$ and $k_N,g_*$ are homotopic, and since $k_N$ and $k_N$, are homotopy equivalences, so is $g_*$, whence the lemma.

Now given V in $\underline{\underline{A}}/\underline{\underline{B}}$, let $\underline{\underline{I}}_{V}$ be the category having as objects pairs $(N,\phi)$, where N is in $\underline{\underline{A}}$ and $\phi$: sN $\rightarrow$ V is an isomorphism in $\underline{\underline{A}}/\underline{\underline{B}}$, in which a morphism

$(N, \phi) \to (N', \phi')$ is a map $g: N \to N'$ such that $\phi'\mathbf{s}(g) = \phi$. It is clear from the construction of $\underline{\underline{A/B}}$ that $\underline{\underline{I}}_V$ is a filtering category. For example, given two maps $g_1, g_2: (N, \phi) \to (N', \phi')$ we have $s(g_1 - g_2) = 0$, so $\operatorname{Im}(g_1 - g_2) \in \underline{\underline{B}}$, hence we obtain a map $(N', \phi') \to (N'', \phi'')$ equalizing $g_1, g_2$ with $N'' = N'/\operatorname{Im}(g_1 - g_2)$.

We have a functor from $\underline{\underline{I}}_V$ to categories sending $(N,\phi)$ to $\underline{\underline{E}}_N$ and $g:(N,\phi)\to (N',\phi')$ to $g_{*}:\underline{\underline{E}}_{N}\to\underline{\underline{E}}_{N}$. Further, for each $(N,\phi)$ we have a functor

$$
P _ {(N, \phi)}: \underset {=} {E} _ {N} \longrightarrow \underset {=} {F}, (M, h) \mapsto (M, s (h) ^ {- 1} \phi^ {- 1}: V \simeq s N \simeq s M)
$$

Since  $p(N', \phi') g_{*} = p(N, \phi)$  for any map  $g : (N, \phi) \to (N', \phi')$  in I=V, we obtain a functor

$$
\lim _ {\underset {=} {I} _ {V}} \left\{(N, \phi) \mapsto \underset {=} {E} _ {N} \right\} \stackrel {{\sim}} {{\longrightarrow}} \underset {=} {F} _ {V}\tag{\( \star\star \)}
$$

which we claim is an isomorphism of categories. In effect

$$
(M, \Theta : V \simeq s M) = p _ {(M, \Theta^ {- 1})} (M, i d _ {M})
$$

for any $(M, \theta)$ in $\underline{F}_V$, showing that $(^{**})$ is surjective on objects. Also given $p_{(N, \phi)}(M, h) = p_{(N, \phi)}(M', h')$, then $M = M'$ and $s(h) = s(h')$. Letting $N' = N / I_m(h - h')$ we obtain a map $g: (N, \phi) \to (N', \phi')$ such that $g_*(M, h) = g_*(M', h')$, showing that $(^{**})$ is injective on objects. The verification that $(^{**})$ is bijective on arrows is similar.

Applying Prop. 3, Cor. 1, we obtain from Lemma 4 and (\*\*) the following.

Lemma 5. For any $\phi : sN \xrightarrow{\sim} V$, the functor $p(N, \phi)$ is a homotopy equivalence.

The end is now near. To finish the proof of the theorem, we have only to show $(i_{V!})^{*}: V \setminus Qs \to O \setminus Qs$ is a homotopy equivalence. Choose $(N, \emptyset)$ as in Lemma 5 and form the diagram

$$
\begin{array}{c c c} \underset {= N} {\mathrm{E}} & \xrightarrow {\mathrm{P} (N , \phi)} & \underset {= V} {\mathrm{F}} \subset V \setminus \mathrm{Qs} \\ k _ {N} \Big \downarrow & & \Big \downarrow (\mathrm{i} _ {V!}) ^ {*} \\ \underset {=} {\mathrm{QB}} & \xrightarrow {\sim} & \underset {= 0} {\mathrm{F}} \subset O \setminus \mathrm{Qs} \end{array}
$$

The diagram is not commutative, for the lower-left and upper-right paths are respectively the functors

$$
\begin{array}{l l}(M, h)&\longmapsto \quad (K e r (h), 0 \simeq s (K e r (h))\\(M, h)&\longmapsto \quad (M, (i _ {s M}) _ {!}: 0 \rightarrow s M).\end{array}
$$

However it is easily checked that by associating to (M,h) the obvious injective map $\operatorname{Ker}(h) \to M$, one obtains a natural transformation between these two functors. Thus the diagram is homotopy commutative, and since all the arrows in the diagram are homotopy equivalences except possibly $(i_{V!})^*$ by Lemmas 1, 3, and 5, it follows that $(i_{V!})^*$ is one also. The proof of the localization theorem is now complete.

## §6. Filtered rings and the homotopy property for regular rings

This section contains some important applications of the preceding results to the groups $K_{i}^{\prime}A = K_{i}(\text{Modf}(A))$ for A noetherian. If A is regular, we have $K_{i}A = K_{i}^{\prime}A$ by the resolution theorem (Th. 3, Cor. 2), so we also obtain results about $K_{i}A$ for A regular. In particular, we prove the homotopy theorem: $K_{i}A = K_{i}(A[t])$ for A regular. According to [Gersten 1], this signifies that the groups $K_{i}A$ are the same as the K-groups of Karoubi and Villamayor for A regular (assuming Theorem 1 of the announcement [Quillen 1] which asserts that the groups $K_{i}A$ are the same as the Quillen K-groups of [Gersten 1]).

Graded rings. Let $B = \coprod B_n$, $n \geq 0$ be a graded ring and put $k = B_0$. From now on we consider only graded B-modules $N = \coprod N_n$ with $n \geq 0$, unless specified otherwise. Put

$$
\mathrm{T} _ {\mathbf {i}} (N) = \operatorname{Tor} _ {\mathbf {i}} ^ {B} (\mathbf {k}, N)
$$

where k is regarded as a right B-module by means of the augmentation  $B \rightarrow k$ . Then  $T_{i}(N)$  is a graded k-module in a natural way, e.g.  $T_{o}(N)_{n} = N_{n}/(A_{1}N_{n-1} + \ldots + A_{n}N_{o})$ . Denote by  $F_{p}N$  the submodule of N generated by  $N_{n}$  for  $n \leq p$ , so that we have  $O = F_{-1}N \subset F_{o}N \subset \ldots$ ,  $\bigcup F_{p}N = N$ . It is clear that

$$
\mathrm{T} _ {\mathbf {o}} (\mathrm{F} _ {\mathbf {p}} \mathrm{N}) _ {\mathbf {n}} = \left\{ \begin{array}{c c} 0 & \quad \mathrm{n} > \mathrm{p} \\ \mathrm{T} _ {\mathbf {o}} (\mathrm{N}) _ {\mathbf {n}} & \quad \mathrm{n} \leqslant \mathrm{p} \end{array} \right.\tag{1}
$$

and that there are canonical epimorphisms

$$
B (- p) \otimes_ {k} T _ {o} (N) _ {p} \longrightarrow F _ {p} N / F _ {p - 1} N\tag{2}
$$

where  $B(-p)_{n} = B_{n-p}$ .

Lemma 1. If $T_1(N) = 0$ and $\text{Tor}_i^k(B, T_0(N)) = 0$ for all $i > 0$, then (2) is an isomorphism for all $p$.

Proof. For any k-module X we have

$$
\operatorname{Tor} _ {i} ^ {k} (B, X) = 0 \quad \text { for } \quad i > 0 \quad \Longrightarrow \quad T _ {i} (B \otimes_ {k} X) = 0 \quad \text { for } \quad i > 0.\tag{3}
$$

In effect, if P. is a k-projective resolution of X, then B⊗P. is a B-projective resolution of B⊗X, and T$_{i}$(B⊗X) = H$_{i}$(k⊗B⊗P.) = H$_{i}$(P.) = 0 for i > 0. In particular by the hypothesis on T$_{o}$(N), we have

$$
\mathrm{T} _ {\mathbf {i}} \left(\mathrm{B} \oplus_ {\mathbf {k}} \mathrm{T} _ {\mathbf {o}} (\mathrm{N})\right) = 0 \text {   for   } \mathbf {i} > 0.\tag{4}
$$

Let $R^p$ be the kernel of (2). Since (2) clearly induces an isomorphism on $T_0$, we obtain from the Tor long exact sequence an exact sequence

$$
\mathrm{T} _ {1} (B (- p) \otimes_ {k} \mathrm{T} _ {o} (N) _ {p}) _ {n} \longrightarrow \mathrm{T} _ {1} (F _ {p} N / F _ {p - 1} N) _ {n} \xrightarrow {\partial} \mathrm{T} _ {o} (R ^ {p}) _ {n} \longrightarrow 0.
$$

The first group is zero by (4), so $\partial$ is an isomorphism.

Fix an integer $s$. We will show that (2) is an isomorphism in degrees $\leqslant s$ and also that $T_1(F_p N)_n = 0$ for $n \leqslant s$ by decreasing induction on $p$. For large $p$, this is true, because $T_1(F_p N)_n = T_1(N)_n$ for $p \geqslant n$, and because $T_1(N) = 0$ by hypothesis. Assuming $T_1(F_p N)_n = 0$ for $n \leqslant s$, we find from (1) and the exact sequence

$$
\mathrm{T} _ {1} \left(\mathrm{F} _ {\mathrm{p}} \mathrm{N}\right) _ {\mathrm{n}} \longrightarrow \mathrm{T} _ {1} \left(\mathrm{F} _ {\mathrm{p}} \mathrm{N} / \mathrm{F} _ {\mathrm{p} - 1} \mathrm{N}\right) _ {\mathrm{n}} \longrightarrow \mathrm{T} _ {\mathrm{o}} \left(\mathrm{F} _ {\mathrm{p} - 1} \mathrm{N}\right) _ {\mathrm{n}} \longrightarrow \mathrm{T} _ {\mathrm{o}} \left(\mathrm{F} _ {\mathrm{p}} \mathrm{N}\right) _ {\mathrm{n}}
$$

that $T_1(F_p N / F_{p-1} N)_n = T_o(R^p)_n = 0$ for $n \leq s$. It follows that $R^p$ is zero in degrees $\leq s$, showing that (2) is an isomorphism in degrees $\leq s$ as claimed. In addition we find $O = T_2(B(-p) \otimes_k T_o(N)_p)_n \simeq T_2(F_p N / F_{p-1} N)_n$ for $n \leq s$, whence from the exact sequence

$$
\mathrm{T} _ {2} \left(\mathrm{F} _ {\mathrm{p}} \mathrm{N} / \mathrm{F} _ {\mathrm{p} - 1} \mathrm{N}\right) _ {\mathrm{n}} \longrightarrow \mathrm{T} _ {1} \left(\mathrm{F} _ {\mathrm{p} - 1} \mathrm{N}\right) _ {\mathrm{n}} \longrightarrow \mathrm{T} _ {1} \left(\mathrm{F} _ {\mathrm{p}} \mathrm{N}\right) _ {\mathrm{n}}
$$

we have  $T_{1}(F_{p-1}N)_{n}=0$  for  $n\leqslant s$ , completing the induction. Since s is arbitrary, the lemma is proved.

Suppose now that B is (left) noetherian, and let $\text{Modfgr}(B)$ be the abelian category of finitely generated graded B-modules. Its K-groups are naturally modules over $Z[t]$, where the action of t is induced by the translation functor $N \mapsto N(-1)$. The ring k is also noetherian, so if B has finite Tor dimension as a right k-module, we have a homomorphism (§4,(6))

$$
(B \otimes_ {k}?): K _ {i} ^ {\prime} k \longrightarrow K _ {i} (\text { Modfgr } (B))\tag{5}
$$

induced by the exact functor $B \otimes_{k}?$ on the subcategory $F = \text{of } \text{Modf}(k)$ consisting of $k$-modules $F$ such that $\text{Tor}_{i}^{k}(B, F) = 0$ for $i > 0$.

Theorem 6. Suppose B is a graded noetherian ring such that B has finite Tor dimension as a right k-module, and such that k has finite Tor dimension as a right B-module. Then (5) extends to a Z[t]-module isomorphism

$$
\mathbb {Z} [ t ] \otimes_ {\mathbb {Z}} K _ {i} ^ {\prime} k \quad \xrightarrow {\sim} K _ {i} (\text { Modfgr } (B)) .
$$

(The hypothesis that k be of finite Tor dimension over B is very restrictive. For example, if k is a field and B is commutative, then B has to be a polynomial ring over k. In all situations where this theorem is used, it happens that B is flat over k. Does this follow from the assumption that B and k are of finite Tor dimension over each other?)

Proof. Let $\underline{\underline{N}}'$ be the full subcategory of Modfgr(B) consisting of N such that $T_{i}(N) = 0$ for $i > 0$, and let $\underline{\underline{N}}''$ be the full subcategory of $\underline{\underline{N}}'$ consisting of N such that $T_{o}(N) \in \underline{\underline{F}}$. By the finite Tor dimension hypotheses and the resolution theorem (§4) one has isomorphisms $K_{i=} F = K_{i}'k$, $K_{i=} N'' = K_{i=} N' = K_{i} (\text{Modfgr}(B))$. Let $\underline{\underline{N}}''$ be the full subcategory of $\underline{\underline{N}}''$ consisting of N such that $F_{n} N = N$. We have homomorphisms

$$
\left(\mathrm{K} _ {\underline {{\mathbf {i}}} \underline {{\mathbf {F}}}}\right) ^ {\mathrm{n}} = \mathrm{K} _ {\underline {{\mathbf {i}}}} \left(\underline {{\mathbf {F}}} ^ {\mathrm{n}}\right) \xrightarrow {\mathrm{b}} \mathrm{K} _ {\underline {{\mathbf {i}}}} \left(\underline {{\mathrm{N} ^ {\prime \prime}}} _ {\mathrm{n}}\right) \xrightarrow {\mathrm{c}} \left(\mathrm{K} _ {\underline {{\mathbf {i}}} \underline {{\mathbf {F}}}}\right) ^ {\mathrm{n}}
$$

induced by the exact functors $(F_j, 0 \leqslant j \leqslant n) \mapsto \coprod B(-j) \otimes_k F_j$ (this is in $\underline{\underline{N}}''$ by (3)) and $N \mapsto (T_o(N)_j)$ respectively. Clearly $cb = id$. On the other hand, by Lemma 1 any $N$ in $\underline{\underline{N}}''_n$ has an exact characteristic filtration $O \subset F_o N \subset .. \subset F_n N = N$ with $F_p N / F_{p-1} N = B(-p) \otimes_k T_o(N)_p$, so applying Th. 2, Cor. 2, one finds that $bc = id$. Thus $b$ is an isomorphism, so by passing to the limit over $n$ we have $\mathbb{Z}[t] \otimes K_i F \xrightarrow{\sim} K_i N''$, which proves the theorem.

The following will be used in the proof of Theorem 7.

Lemma 2. Suppose B is noetherian, k is regular, and that k has finite Tor dimension as a right B-module. Then any N in Modfgr(B) has a finite resolution by finitely generated projective graded B-modules.

Proof. Starting with $N_0 = N$, we recursively construct exact sequences in Modfgr(B)

$$
0 \longrightarrow N _ {r} \longrightarrow P _ {r - 1} \longrightarrow N _ {r - 1} \longrightarrow 0
$$

where $P_{r-1}$ is projective. We have to show $N_r$ is projective for $r$ large. Since $T_i(N_r) = T_{i+1}(N_{r-1})$ for $i > 0$, it follows that $T_i(N_r) = 0$ for $i > 0$ and $r \geq d$, where $d$ is the Tor dimension of $k$ over $B$. Then for $r > d$ we have exact sequences

$$
0 \longrightarrow T _ {o} (N _ {r}) \longrightarrow T _ {o} (P _ {r - 1}) \longrightarrow T _ {o} (N _ {r - 1}) \longrightarrow 0.
$$

As $k$ is regular, $T_{0}(N_{d})$ has finite projective dimension $s$, so $T_{0}(N_{r})$ is projective for $r \geqslant d + s$. It follows from Lemma 1 that $N_{d + s}$ is projective, whence the lemma.

Filtered rings. Let A be a ring equipped with an increasing filtration by subgroups $0 = F_{-1}A \subset F_{0}A \subset F_{1}A \subset \ldots$ such that $1 \in F_{0}A$, $F_{p}A \cdot F_{q}A \subset F_{p + q}A$, and $\bigcup F_{p}A = A$. Let $B = gr(A) = \coprod F_{p}A / F_{p - 1}A$ be the associated graded ring and put $k = F_{0}A = B_{0}$. By a filtered A-module M we will mean an A-module equipped with an increasing filtration $0 = F_{-1}M \subset F_{0}M \subset \ldots$ such that $F_{p}A \cdot F_{q}M \subset F_{p + q}M$ and $\bigcup F_{p}M = M$. Then $gr(M) = \coprod F_{p}M / F_{p - 1}M$ is a graded B-module in a natural way.

Lemma 3. i) If $\text{gr}(M)$ is a finitely generated B-module, then M is a finitely generated A-module. In particular, if every graded left ideal in B is finitely generated, then A is noetherian.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
ii) If  $\mathrm{gr}(M)$  is a projective B-module, then M is a projective A-module.
iii) If  $\mathrm{gr}(M)$  has a resolution by finitely generated projective graded B-modules of length  $\leqslant n$ , then M has a  $\underline{\underline{\mathrm{P(A)}}}$ -resolution of length  $\leqslant n$ .
</div>

Proof. We use the following construction. Suppose given k-modules  $L_{j}$  and maps of k-modules  $L_{j} \rightarrow F_{j}M$  for each  $j \geq 0$  such that the composition

$$
\mathrm{L} _ {\mathrm{j}} \longrightarrow \mathrm{F} _ {\mathrm{j}} \mathrm{M} \longrightarrow g r _ {\mathrm{j}} (\mathrm{M}) \longrightarrow \mathrm{T} _ {\mathrm{o}} (g r (\mathrm{M})) _ {\mathrm{j}}
$$

is onto. Let $P$ be the filtered A-module with $F_{n}P = \coprod_{j} F_{n-j}A \otimes_{k} L_{j}$ and let $\phi : P \to M$ be such that $\phi$ restricted to $A \otimes_{k} L_{j}$ is the A-linear extension of the given map from $L_{j}$ to $F_{j}M$. Then $T_{o}(gr(P))_{j} = L_{j}$, and $\phi$ is a map of filtered A-modules such that $T_{o}(gr(\phi))$ is onto. It follows that $gr(\phi)$ is onto, hence $F_{n}(\phi)$ is onto for all $n$, and so $\phi$ is onto. Thus if $K = Ker(\phi)$, $F_{n}K = K \cap F_{n}M$, we have an exact sequence of A-modules

$$
0 \longrightarrow K \longrightarrow P \longrightarrow M \longrightarrow O
$$

such that

$$
0 \longrightarrow F _ {n} K \longrightarrow F _ {n} P \longrightarrow F _ {n} M \longrightarrow 0\tag{6}
$$

$$
0 \longrightarrow g r _ {n} K \longrightarrow g r _ {n} P \longrightarrow g r _ {n} M \longrightarrow 0
$$

are exact for all n.

i): If  $\mathrm{gr}(M)$  is a finitely generated B-module, then  $\mathrm{T}_{0}(\mathrm{gr}(M))$  is a finitely

generated k-module, hence we can take  $L_{j}$  to be a free finitely generated k-module which is zero for large j. Then P is a free finitely generated A-module, so M is finitely generated, proving the first part of i). The second part follows by taking M to be a left ideal of A and endowing it with the induced filtration  $F_{n}M = M \cap F_{n}A$ .

ii): If  $\mathrm{gr}(M)$  is projective over B, then  $\mathrm{T}_{\mathrm{o}}(\mathrm{gr}(M))$  is projective over k, and we can take  $\mathrm{L}_{\mathrm{j}} = \mathrm{T}_{\mathrm{o}}(\mathrm{gr}(M))_{\mathrm{j}}$ . Then  $\mathrm{T}_{\mathrm{o}}(\mathrm{gr}(\phi))$  is an isomorphism, so from the exact sequence

$$
\mathrm{T} _ {1} (\operatorname{gr} (\mathrm{M})) \longrightarrow \mathrm{T} _ {\circ} (\operatorname{gr} (\mathrm{K})) \longrightarrow \mathrm{T} _ {\circ} (\operatorname{gr} (\mathrm{P})) \longrightarrow \mathrm{T} _ {\circ} (\operatorname{gr} (\mathrm{M}))
$$

we conclude that $\mathbf{T}_{\mathbf{O}}(\mathbf{gr}(\mathbf{K})) = 0$. Then $\mathbf{gr}(\mathbf{K}) = 0$, so $K = 0, M = P$, and $M$ is projective over $A$, proving ii).

iii): We use induction on $n$, the case $n = 0$ being clear from i) and ii). Assuming $\text{gr}(M)$ has a resolution of length $\leqslant n$ by finitely generated graded projective B-modules, choose P as in the proof of i), so that $\text{gr}(P)$ is a free finitely generated B-module. From the exact sequence (6), and the lemma after Th. 3, Cor. 1, (or Schanuel's lemma), we know that $\text{gr}(K)$ has a resolution of length $\leqslant n-1$ by finitely generated graded projective B-modules. Applying the induction hypothesis, it follows that K has a $\underline{\underline{P}}(A)$-resolution of length $\leqslant n-1$, so M has a $\underline{\underline{P}}(A)$-resolution of length $\leqslant n$, as was to be shown.

Lemma 4. If B is noetherian, k is regular, and if k has finite Tor dimension as a right B-module, then A is regular.

This is an immediate consequence of Lemma 2 and Lemma 3 iii).

We can now prove the main result of this section.

Theorem 7. Let $A$ be a ring equipped with an increasing filtration
$O = F_{-1}A \subset F_{0}A \subset F_{1}A \subset \ldots$ such that $1 \in F_{0}A$, $F_{p}A \cdot F_{q}A \subset F_{p+q}A$, and $\bigcup_{p} F_{p}A = A$. Suppose $B = gr(A)$ is noetherian and that $B$ is of finite Tor dimension as a right module over $B_{0} = F_{0}A$, (hence $F_{0}A$ and $A$ are noetherian and $A$ is of finite Tor dimension as a right $F_{0}A$-module). Suppose also that $F_{0}A$ is of finite Tor dimension as a right $B$-module. Then the inclusion $F_{0}A \subset A$ induces isomorphisms $K_{i}'(F_{0}A) \simeq K_{i}'A$. If further $F_{0}A$ is regular, then so is $A$, and we have isomorphisms $K_{i}(F_{0}A) \simeq K_{i}A$.

Proof. Put $k = F_{0}A$. Since $B$ is noetherian, we know $A$ is also by Lemma 3 i). Also if $B$ has Tor dimension $d$ over $k$, then $F_{n}A / F_{n-1}A$ has Tor dimension $\leqslant d$ for each $n$, so the same is true for $F_{n}A$, and hence also for $A$. Thus the map $K_{i}^{\prime}k \to K_{i}^{\prime}A$ is defined, and we have only to prove that it is an isomorphism. Indeed, the last assertion of the theorem results from Lemma 4 and the fact that $K_{i}A = K_{i}^{\prime}A$ for regular $A$ by the resolution theorem (Th. 3, Cor. 2).

Let $z$ be an indeterminate and let $A'$ be the subring $\coprod (F_A)z^n$ of $A[z]$. We show the graded ring $A'$ satisfies the hypotheses of Theorem 6. The fact that $A'$ has finite Tor dimension over $k$ is clear from the preceding paragraph. Since $z$ is a central non-zero-divisor in $A'$, we have that $B = A'/zA'$ is of Tor dimension one over $A'$. As $k$ has finite Tor dimension over $B$, it follows that $k$ has finite Tor dimension

over A'. Finally to show A' is noetherian, we filter A' by letting  $F_{p}A'$  consist of those polynomials whose coefficients are in  $F_{p}A$ . The ring

$$
\operatorname{gr} \left(\mathrm{A} ^ {\prime}\right) = \frac {1}{p \leqslant n} \left(\operatorname{gr} _ {p} \mathrm{A}\right) z ^ {n}
$$

is isomorphic to $\operatorname{gr}(A)[z]$, which is noetherian, hence $A'$ is noetherian by Lemma 3 i). Let $\underline{\underline{\mathbf{F}}}$ be the full subcategory of $\operatorname{Modf}(k)$ consisting of $\mathbf{F}$ such that $\operatorname{Tor}_{i}^{k}(B,F)=0$ for $i>0$, whence $K_{i}\underline{\underline{\mathbf{F}}} = K_{i}'k$ by the resolution theorem (Th.3, Cor. 3). Applying Theorem 6 to B and $A'$, we obtain $\mathbb{Z}[t]$-module isomorphisms

$$
\begin{array}{l l l l} \mathbb {Z} [ t ] \otimes K _ {i} F & \simeq & K _ {i} (\text { Modfgr } (B)) \quad , \quad 1 \otimes x \mapsto (B \otimes_ {k}?) _ {*} x \\ \mathbb {Z} [ t ] \otimes K _ {i} F & \simeq & K _ {i} (\text { Modfgr } (A ^ {\prime})) \quad , \quad 1 \otimes x \mapsto (A ^ {\prime} \otimes_ {k}?) _ {*} x. \end{array}\tag{7}
$$

Let $\underline{\underline{\mathbf{B}}}$ be the Serre subcategory of $\underline{\underline{\mathbf{A}}} = \text{Modfgr}(\mathbf{A}')$ consisting of modules on which $z$ is nilpotent. The functor

$$
j: \operatorname{Modfgr} (A ^ {\prime}) \longrightarrow \operatorname{Modf} (A), M \mapsto M / (z - 1) M
$$

is exact and induces an equivalence of the quotient category $\underline{\underline{A}}/\underline{\underline{B}}$ with Modf(A). (Compare [Swan, p.114, 130]; note that if $S = \{z^n\}$, then $S^{-1}A'$ is the Laurent polynomial ring $A[z,z^{-1}]$, and a graded module over $A[z,z^{-1}]$ is the same as a module over $A = A'/(z-1)A'$.) Since $A'/zA' = B$, we have an embedding

$$
\mathrm{i}: \operatorname{Modfgr} (\mathrm{B}) \longrightarrow \operatorname{Modfgr} \left(\mathrm{A} ^ {\prime}\right)
$$

identifying the former with the full subcategory of the latter consisting of modules killed by z. The devissage theorem implies that  $K_{i}(\text{Modfgr}(B)) = K_{i}B$ . Thus the exact sequence of the localization theorem for the pair  $(\underline{A}, \underline{B})$  takes the form

$$
\longrightarrow \mathrm{K} _ {\mathbf {i}} (\text { Modfgr } (B)) \xrightarrow {\mathbf {i} _ {*}} \mathrm{K} _ {\mathbf {i}} (\text { Modfgr } (A ^ {\prime})) \xrightarrow {\mathbf {j} _ {*}} \mathrm{K} _ {\mathbf {i}} ^ {\prime} A \longrightarrow .\tag{8}
$$

We next compute $\mathbf{i}_{*}$ with respect to the isomorphisms (7). Associating to $\mathbf{F}$ in $\underline{\mathbf{F}}$ the exact sequence

$$
0 \longrightarrow A ^ {\prime} (- 1) \otimes_ {k} F \stackrel {z} {\longrightarrow} A ^ {\prime} \otimes_ {k} F \longrightarrow B \otimes_ {k} F \longrightarrow O
$$

we obtain an exact sequence of exact functors from $\underline{\mathbb{F}}$ to Modfgr(A'). Applying Th. 2, Cor. 1, we conclude that the square of $\mathbb{Z}[t]$-module homomorphisms

$$
\begin{array}{c c c c} \mathbb {Z} [ t ] & \otimes K _ {i} F & \xrightarrow {\sim} & K _ {i} (\text { Modfgr } (B)) \\ 1 - t & \downarrow & & \downarrow i _ {*} \\ \mathbb {Z} [ t ] & \otimes K _ {i} F & \xrightarrow {\sim} & K _ {i} (\text { Modfgr } (A ^ {\prime})) \end{array}
$$

is commutative. Since 1-t is injective with cokernel $K_{i}F$, we conclude from the exact sequence (8) that the composition

$$
\mathrm{K} _ {\mathbf {i}} \stackrel {{\mathrm{F}}} {{=}} \longrightarrow \mathrm{K} _ {\mathbf {i}} (\text { Modfgr } (A ^ {\prime})) \stackrel {{\mathrm{j} _ {*}}} {{\longrightarrow}} \mathrm{K} _ {\mathbf {i}} ^ {\prime} A
$$

induced by $F \mapsto A' \otimes_k F \mapsto A \otimes_k F$ is an isomorphism. Since $K_{i} = K_i'k$, this proves the theorem.

The preceding theorem enables one to compute the K-groups of some interesting non-commutative rings.

Examples. Let $\mathcal{G}$ be a finite dimensional Lie algebra over a field $k$, and let $U(\mathcal{G})$ be its universal enveloping algebra. The Poincare-Birkhoff-Witt theorem asserts that $U(\mathcal{G})$ is a filtered algebra such that $\text{gr}(U(\mathcal{G}))$ is a polynomial ring over $k$. Thus Theorem 7 implies that $K_{i}k = K_{i}U(\mathcal{G})$. Similarly if $H_{n}$ is the Heisenberg-Weyl algebra over $k$ with generators $p_{i}, q_{i}, 1 \leqslant i \leqslant n$, subject to the relations $[p_{i}, p_{j}] = [q_{i}, q_{j}] = 0$, $[p_{i}, q_{j}] = \delta_{ij}$, then we have $K_{i}k = K_{i}H_{n}$.

Theorem 8. If A is noetherian, then there are canonical isomorphisms

i)  $K_{i}^{\prime}(A[t]) \simeq K_{i}^{\prime}A$

ii)  $K_{i}^{\prime}(A[t,t^{-1}]) \cong K_{i}^{\prime}A \oplus K_{i-1}^{\prime}A$

Proof. i) follows immediately from the preceding theorem.

ii): Applying the localization theorem to the Serre subcategory $\underline{\underline{\mathbf{B}}}$ of Modf(A[t]) consisting of modules on which t is nilpotent, we get a long exact sequence

$$
\longrightarrow \begin{array}{c c c} K _ {i} B & \longrightarrow & K _ {i} ^ {\prime} (A [ t ]) \\ s \uparrow & & s \uparrow \\ K _ {i} ^ {\prime} A & & K _ {i} ^ {\prime} A \end{array} \longrightarrow K _ {i} ^ {\prime} (A [ t, t ^ {- 1} ]) \longrightarrow
$$

where the first vertical isomorphism results from applying the devissage theorem to the embedding $\operatorname{Modf}(A) = \operatorname{Modf}(A[t]/tA[t]) \subset \underline{B}$. The homomorphism $A[t, t^{-1}] \longrightarrow A$ sending $t$ to 1 makes $A$ a right module of Tor dimension one over $A[t, t^{-1}]$, so it induces a map $K_{i}'(A[t, t^{-1}]) \longrightarrow K_{i}'A$ left inverse to the oblique arrow. Thus the exact sequence breaks up into split short exact sequences proving ii).

Corollary. (Fundamental theorem for regular rings) If A is regular, then there are canonical isomorphisms  $K_{i}(A[t]) = K_{i}A$  and  $K_{i}(A[t,t^{-1}]) = K_{i}A \oplus K_{i-1}A$ .

This is clear from Th. 3, Cor. 2, since A[t] and A[t,t $^{-1}$ ] are regular if A is.

Exercise. Let $\phi$ be an automorphism of a noetherian ring $A$, and let $A_{\phi}[t]$, $A_{\phi}[t,t^{-1}]$ be the associated twisted polynomial and Laurent polynomial rings in which $t \cdot a = \phi(a) \cdot t$, ([Farrell-Hsiang]). Show that $K_{i}^{\prime}A = K_{i}^{\prime}(A_{\phi}[t])$ and that there is a long exact sequence

$$
\longrightarrow \mathrm{K} _ {i} ^ {\prime} \mathrm{A} \xrightarrow {1 - \phi_ {*}} \mathrm{K} _ {i} ^ {\prime} \mathrm{A} \longrightarrow \mathrm{K} _ {i} ^ {\prime} (\mathrm{A} _ {\phi} [ t, t ^ {- 1} ]) \longrightarrow \mathrm{K} _ {i - 1} ^ {\prime} \mathrm{A} \longrightarrow .\tag{9}
$$

We finish this section by showing how the preceding results can be used to compute the K-groups of certain skew-fields. Keith Dennis points out that this has some interest already in the case of  $K_{2}$ , since a non-commutative generalization of Matsumoto's theorem is not known. (Here and in the computation to follow, we will be assuming Theorem 1 of the announcement [Quillen 1], which implies that the  $K_{2}A$  here is the same as Milnor's, and that the groups  $K_{i}F_{q}$  are the same as the ones computed in [Quillen 2].)

Example 1. Let $k$ be the algebraic closure of the finite field $\mathbb{F}_p$, and let $A$ be the twisted polynomial ring $k_{\phi}[F]$ with $Fx = x^q F$ for $x$ in $k$, where $q = p^d$.

Then A is a non-commutative domain in which every left ideal is principal. Let D be the quotient skew-field of A, whence  $\text{Modf}(D) = \text{Modf}(A)/\underline{\underline{B}}$ , where  $\underline{\underline{B}}$  is the Serre subcategory consisting of A-modules which are torsion, or equivalently, which are finite dimensional over k. The localization theorem gives an exact sequence

$$
\longrightarrow K _ {i} B \xrightarrow {i _ {*}} K _ {i} A \longrightarrow K _ {i} D \longrightarrow K _ {i - 1} B \longrightarrow\tag{10}
$$

(A and D are regular), and we have  $K_{i}A = K_{i}k$  by Theorem 7.

An object of $\underline{\underline{B}}$ is a finite dimensional vector space $V$ over $k$ equipped with an additive map $F: V \to V$ such that $F(xv) = x^q F(v)$ for $x$ in $k$ and $v$ in $V$. It is well-known that $V$ splits canonically: $V = V_o \oplus V_1$, where $F$ is nilpotent on $V_o$ and bijective on $V_1$, and moreover that

$$
k \otimes_ {F _ {q}} v ^ {F} \stackrel {{\sim}} {{\longrightarrow}} v _ {1}
$$

where  $V^{F} = \{v \in V \mid Fv = v\}$  is a finite dimensional vector space over the subfield  $F_{q}$  of k with q elements. Thus we have an equivalence of categories

$$
\underline {{B}} \cong \bigcup_ {n} \text { Modf } (A / A F ^ {n}) x \text { Modf } (F _ {q}).
$$

Applying the devissage theorem to the first factor, we obtain $K_{i}B = K_{i}k \oplus K_{i}F_{g}$.

Let $\phi : k \to k$ be the Frobenius automorphism: $\phi(x) = x^q$, and let $\phi(V)^q$ denote the base extension of the $k$-vector space $V$ with respect to $\phi$, i.e. $\phi(V) = k \otimes_k V$, where $k$ is regarded as a right $k$-module via $\phi$. If $V$ is regarded as an $A$-module killed by $F$, we have an exact sequence of $A$-modules

$$
\begin{array}{r c l} \mathrm{O} & \longrightarrow & \mathrm{A}   \otimes_ {\mathrm{k}} \phi (\mathrm{V}) \quad \longrightarrow \quad \mathrm{A}   \otimes_ {\mathrm{k}} \mathrm{V} \quad \longrightarrow \quad \mathrm{V} \quad \longrightarrow \quad \mathrm{O} \\ & & \mathrm{a}   \otimes (\mathrm{x}   \otimes   \mathrm{v}) \quad \mapsto \quad \mathrm{axF}   \otimes   \mathrm{v} \end{array}
$$

On the other hand, if W is a finite dimensional vector space over  $F_{q}$ , we have an exact sequence of A-modules

$$
\begin{array}{c c c c c} \text {O} & \longrightarrow & \mathrm{A} \otimes_ {\mathbb {F}} W & \longrightarrow & \mathrm{A} \otimes_ {\mathbb {F}} W \\ & & \mathrm{a} \otimes w & \mapsto & \mathrm{a} (\mathrm{F} - 1) \otimes w \end{array} \longrightarrow \begin{array}{c c c c c} \mathrm{k} \otimes_ {\mathbb {F}} W & \longrightarrow & \mathrm{O} \\ & & \mathrm{q} \end{array}
$$

where $F$ acts on the cokernel by $F(x \otimes w) = x^q \otimes w$. Applying Th. 2, Cor. 1, to these "characteristic" sequences, one easily deduces that the composite

$$
K _ {i} k \oplus K _ {i} F _ {q} = K _ {i} B \xrightarrow {i _ {*}} K _ {i} A = K _ {i} k
$$

is zero on the factor  $K_{i}F_{q}$  and the map  $1 - \phi_{*}$  on  $K_{i}k$ . From [Quillen 2] one has exact sequences

$$
0 \longrightarrow K _ {i} F _ {q} \longrightarrow K _ {i} k \xrightarrow {1 - \phi_ {*}} K _ {i} k \longrightarrow 0
$$

for i>0. Combining this with (10) we obtain the formulas

$$
\mathrm{K} _ {\circ} \mathrm{D} = \mathbb {Z}, \quad \mathrm{K} _ {1} \mathrm{D} = \mathbb {Z} \oplus \mathbb {Z}\tag{11}
$$

$$
\mathrm{K} _ {2 \mathbf {i}} D = \left(\mathrm{K} _ {2 \mathbf {i} - 1} \mathbb {F} _ {\mathbf {q}}\right) ^ {2} = (\mathbb {Z} / (\mathrm{q} ^ {\mathbf {i}} - 1) \mathbb {Z}) ^ {2} \quad \mathbf {i} > 0
$$

$$
\mathrm{K} _ {2 \mathbf {i} + 1} D = \left(\mathrm{K} _ {2 \mathbf {i}} \mathbb {F} _ {\mathbf {q}}\right) ^ {2} = 0 \quad \mathbf {i} > 0.
$$

Example 2. Let H be the Heisenberg-Weyl algebra with generators p,q such that pq - qp = 1 over an algebraically closed field k, and let D be the quotient skew-field of H. In this case, one can prove that the localization exact sequence associated to Modf(H) and the Serre subcategory of torsion modules breaks up into short exact sequences

$$
0 \longrightarrow K _ {i} k \longrightarrow K _ {i} D \longrightarrow \perp K _ {i - 1} k \longrightarrow 0
$$

where the direct sum is taken over the set of isomorphism classes of simple H-modules. The proof is similar to the preceding, the essential points being a) torsion finitely generated H-modules are of finite length, because H has no modules finite dimensional over k, and b) k is the ring of endomorphisms of any simple H-module ([Quillen 3]).

## §7. K'-theory for schemes

1. If $X$ is a scheme, we put $K_{q}X = K_{q=}P(X)$, where $P(X)$ is the category of vector bundles over $X$ (= locally free sheaves of $O_{=X}$-modules of finite rank) equipped with the usual notion of exact sequence. If $X$ is a noetherian scheme, we put $K_{q}'X = K_{q=}M(X)$, where $M(X)$ is the abelian category of coherent sheaves on $X$. The following theory concerns primarily the groups $K_{q}'X$, so for the rest of this section we will assume all schemes to be noetherian and separated, unless stated otherwise.

As the inclusion functor from $\underline{\underline{P}}(X)$ to $\underline{\underline{M}}(X)$ is exact, it induces a homomorphism (1.1) $K_{q}^{X} \to K_{q}^{\prime X}$.

When $X$ is regular this is an isomorphism. In effect, one knows that any coherent sheaf $F$ is a quotient of a vector bundle [SGA 6 II 2.2.3 - 2.2.7.1], hence it has a resolution by vector bundles, in fact a finite resolution as $X$ is regular and quasi-compact (see [SGA 2 VIII 2.4]). Thus 1.1 is an isomorphism by the resolution theorem (Th. 3, Cor. 1).

If $E$ is a vector bundle on $X$, then $F \mapsto E \otimes F$ is an exact functor from $\underline{M}(X)$ to itself, hence as in §3, (1), we obtain pairings

$$
\mathrm{K} _ {\mathrm{o}} ^ {\mathrm{X}} \otimes \mathrm{K} _ {\mathrm{q}} ^ {\prime \mathrm{X}} \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime \mathrm{X}}\tag{1.2}
$$

making $K_{q}^{\prime}X$ a module over the ring $K_{0}X$. (In a later paper I plan to extend this idea to define a graded anti-commutative ring structure on $K_{*}X$ such that $K_{*}^{\prime}X$ is a graded module over $K_{*}X$.)

2. Functorial behavior. If $f: X \to Y$ is a morphism of schemes (resp. a flat morphism), then the inverse image functor $f^*: \underline{P}(Y) \to \underline{P}(X)$ (resp. $f^*: \underline{M}(Y) \to \underline{M}(X)$) is exact, hence it induces a homomorphism of K-groups which will be denoted

$$
f ^ {*}: K _ {q} Y \rightarrow K _ {q} X \quad (\text { resp. } f ^ {*}: K _ {q} ^ {\prime} Y \rightarrow K _ {q} ^ {\prime} X).\tag{2.1}
$$

It is clear that in this way  $K_{q}$  becomes a contravariant functor from schemes to abelian groups, and that  $K'_{q}$  is a contravariant functor on the subcategory of schemes and flat morphisms.

Proposition 2.2. Let $i \mapsto X_i$ be a filtered projective system of schemes such that the transition morphisms $X_i \to X_j$ are affine, and let $X = \varprojlim X_i$. Then
(2.3)
$K_X = \varinjlim K_X_i$.

If in addition the transition morphisms are flat, then

$$
\mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{X} = \lim _ {\rightarrow} \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{X} _ {i}.\tag{2.4}
$$

Proof. We wish to apply §2 (9), using the fact that $\underline{\underline{P}}(X)$ is essentially the inductive limit of the $\underline{\underline{P}}(X_i)$ by [EGA IV 8.5]. In order to obtain an honest inductive system of categories, we replace $\underline{\underline{P}}(X_i)$ by an equivalent category using Giraud's method as follows. Let $I$ be the index category of the system $X_i$, and let $I'$ be the category obtained by adjoining an initial object $\phi$ to $I$. We extend the system $X_i$ to $I'$ by putting $X_\phi = X$, and let $\underline{\underline{P}}$ be the fibred category over $I'$ having the fibre $\underline{\underline{P}}(X_i)$ over $i$. Let $\underline{\underline{P}_i}$ be the category of cartesian sections of $\underline{\underline{P}}$ over $I'/i$. (An object of $\underline{\underline{P}_i}$ is a family of pairs $(E_j, \Theta_j)$ with $E_j \in \underline{\underline{P}}(X_j)$ and $\Theta_j$ an isomorphism $(j \to i)*E_i \simeq E_j$ for each object $j \to i$ of $I'/i$.) Clearly $\underline{\underline{P}_i}$ is equivalent to $\underline{\underline{P}}(X_i)$ and $i \mapsto \underline{\underline{P}_i}$ is a functor from $I^0$ to categories. Using [EGA IV 8.5] it is not hard to see that we have an equivalence of categories

$$
\xrightarrow [ I ]{\lim} (i \mapsto \underline {{P}} _ {i}) \longrightarrow \underline {{P}} (X)
$$

such that a sequence is exact in $\underline{\underline{P}}(X)$ if and only if it comes from an exact sequence in some $\underline{\underline{P}}_{i}$. Thus from §2 (9) we have $K_{q=1}P(X) = \lim_{\rightarrow} K_{q=1}P_i$, proving 2.3. The proof of 2.4 is similar.

2.5. Suppose that $f: X \to Y$ is a morphism of finite Tor dimension (i.e. $\underline{O}_X$ is of finite Tor dimension as a module over $f^{-1}(\underline{O}_Y)$), and let $\underline{P}(Y, f)$ be the full subcategory of $\underline{M}(Y)$ consisting of sheaves $F$ such that

$$
\operatorname{Tor} _ {i} \stackrel {{0}} {{=}} Y (\underset {\sim X} {0}, F) = 0 \quad \text { for } \quad i > 0.
$$

Assuming that every $F$ in $\underline{\underline{M}}(Y)$ is a quotient of a member of $\underline{\underline{P}}(Y, f)$, the resolution theorem (Th. 3, Cor. 3) implies that the inclusion $\underline{\underline{P}}(Y, f) \to \underline{\underline{M}}(Y)$ induces isomorphisms on K-groups. Combining this isomorphism with the homomorphism induced by the exact functor $f^* : \underline{\underline{P}}(Y, f) \to \underline{\underline{M}}(X)$, we obtain a homomorphism which will be denoted

$$
f ^ {*}: K _ {q} ^ {\prime Y} \longrightarrow K _ {q} ^ {\prime X}.\tag{2.6}
$$

The assumption holds if either $f$ is flat (whence $\underline{\underline{P}}(Y, f) = \underline{\underline{M}}(Y)$), or if every coherent sheaf on $Y$ is the quotient of a vector bundle (e.g. if $Y$ has an ample line bundle). In both of these cases the formula $(fg)^* = g^*f^*$ is easily verified.

2.7. Let $f: X \to Y$ be a proper morphism, so that the higher direct image functors $R^{i}f_{*}$ carry coherent sheaves on $X$ to coherent sheaves on $Y$. Let $F(X, f)$ denote the full subcategory of $M(X)$ consisting of $F$ such that $R^{i}f_{*}(F) = 0$ for $i > 0$. Since $R^{i}f_{*} = 0$ for $i$ large [EGA III 1.4.12], we can apply Th. 3, Cor. 3 to the inclusion $F(X, f)^{0} \to M(X)^{0}$ to get an isomorphism $K F(X, f) \stackrel{\sim}{\to} K'X$, provided we assume that every

coherent sheaf on X can be embedded in a member of $\underline{\underline{F}}(X,f)$. Composing this isomorphism with the homomorphism of K-groups induced by the exact functor $f_{*}:\underline{\underline{F}}(X,f)\to\underline{\underline{M}}(Y)$, we obtain a homomorphism which will be denoted

$$
f _ {*}: K _ {q} ^ {\prime} X \longrightarrow K _ {q} ^ {\prime} Y.\tag{2.8}
$$

The assumption is satisfied in the following cases:

i) When $f$ is finite, in particular, when $f$ is a closed immersion. In this case $R^i f_* = 0$ for $i > 0$ [EGA III 1.3.2], so $F(X, f) = M(X)$.

ii) When $X$ has an ample line bundle [EGA II 4.5.3]. In effect if $L$ is ample on $X$, then it is ample when restricted to any open subset, and in particular, it is ample relative to $f$. Replacing $L$ by a high tensor power, we can suppose $L$ is very ample relative to $f$, and further that $L$ is generated by its global sections. Then for any $n$ we have an epimorphism $(\underline{Q}_X)^{rn} \to L^{\otimes n}$, hence dualizing and tensoring with $L^{\otimes n}$, we obtain an exact sequence of vector bundles

$$
0 \longrightarrow \underline {{0}} _ {X} \longrightarrow (L ^ {\otimes n}) ^ {r n} \longrightarrow E \longrightarrow 0.
$$

Hence for any coherent sheaf F on X we have an exact sequence

$$
0 \longrightarrow F \longrightarrow F (n) ^ {r n} \longrightarrow F \otimes E \longrightarrow 0\tag{2.9}
$$

where $F(n) = F \otimes L^{\otimes n}$. But by Serre's theorem [EGA III 2.2.1], there is an $n_0$ such that $R^1 f_*(F(n)) = 0$ for $i > 0$, $n \geqslant n_0$, so $F(n) \in \underline{F}(X, f)$ for $n \geqslant n_0$. Thus $F$ can be embedded in a member of $\underline{F}(X, f)$ as asserted.

The verification of the formula $(fg)_* = f_*g_*$ in cases i) and ii) is straightforward and will be omitted.

Proposition 2.10. (Projection formula) Suppose $f: X \to Y$ proper and of finite Tor dimension, and assume $X$ and $Y$ have ample line bundles so that 2.6 and 2.8 are defined. Then for $x \in K_0^X$ and $y \in K_q'Y$ we have $f_*(x \cdot f*y) = f_*(x) \cdot y$ in $K_q'Y$, where $f_*(x)$ is the image of $x$ by the homomorphism $f_*: K_0^X \to K_0^Y$ of [SGA 6 2.12.3].

Proof. We recall that if $\mathbf{x} = [\mathbf{E}]$ is the class of a vector bundle $\mathbf{E}$, then $f_{*}(\mathbf{x})$ is the class of the perfect complex $Rf_{*}(E)$. Arguing as in case ii) above, one sees that $K_{0}X$ is generated by the elements $[\mathbf{E}]$ such that $R^{i}f_{*}(E) = 0$ for $i > 0$. Then $Rf_{*}(E) \cong f_{*}E$, and $f_{*}(\mathbf{x}) = \sum (-1)^{i}[P_{i}] \in K_{0}X$, where $\{P_{i}\}$ is a finite resolution of $f_{*}E$ by vector bundles on $Y$. Let $\underline{\underline{L}}$ denote the full subcategory of $\underline{\underline{M}}(Y)$ consisting of $F$ such that

$$
\operatorname{Tor} _ {\mathbf {i}} \stackrel {{\mathrm{O}}} {{=}} \mathrm{Y} (\mathbf {f} _ {*} \mathrm{E}, \mathbf {F}) = 0 = \operatorname{Tor} _ {\mathbf {i}} \stackrel {{\mathrm{O}}} {{=}} \mathrm{Y} (\underset {\equiv X} {\mathrm{O}}, \mathbf {F})
$$

By the resolution theorem we have $K_{q}L = K'Y$. Moreover, applying Th. 2, Cor. 3 to

$$
0 \longrightarrow P _ {n} \otimes F \longrightarrow .. \longrightarrow P _ {o} \otimes F \longrightarrow f _ {*} E \otimes F \longrightarrow 0
$$

for $F \in \underline{\underline{L}}$, one sees that $y \mapsto f_{*}(x) \cdot y$ is the endomorphism of $K'Y_q$ induced by the exact functor $F \mapsto f_{*}E \otimes F$ from $\underline{\underline{L}}$ to $\underline{\underline{M}}(Y)$.

From the projection formula in the derived category: $\mathrm{Rf}_{*}(\mathrm{E}\stackrel{\mathrm{L}}{\otimes}_{\mathrm{Y}}\mathrm{F}) = \mathrm{Rf}_{*}(\mathrm{E})\stackrel{\mathrm{L}}{\otimes}_{\mathrm{Y}}\mathrm{F}$ (see [SGA 6 III 2.7]), we find for $\mathbf{F}$ in $\underline{\underline{\mathbf{L}}}$ that

$$
R ^ {q} f _ {*} (E \otimes f ^ {*} E) = \left\{ \begin{array}{l l} 0 & q \neq 0 \\ f _ {*} E \otimes F & q = 0. \end{array} \right.
$$

Thus $E \otimes f^*F$ is in $\underline{\underline{F}}(X, f)$, so by the definition of 2.6 and 2.8, we have that $y \mapsto f_*(x \cdot f*y)$ is the endomorphism of $K'Y_q$ induced by the exact functor $F \mapsto f_*(E \otimes f^*F)$ from $\underline{L}$ to $\underline{M}(Y)$. Since we have an isomorphism $f_*(E \otimes f^*F) \simeq f_*E \otimes F$, the projection formula follows.

Proposition 2.11. Let

![](images/page_42_image_3.jpg)

be a cartesian square of schemes having ample line bundles. Assume $f$ is proper, $g$ is of finite Tor dimension, and that $Y'$ and $X$ are Tor independent over $Y$, (i.e.

$$
\operatorname{Tor} _ {i} \stackrel {{\underline {{0}}}} {{=}} Y, y (\underset {\underline {{0}} Y ^ {\prime}, y ^ {\prime}} {{=}}, \underset {\underline {{0}} X, x} {{=}}) = 0 \quad \text { for } i > 0
$$

for any  $x \in X$ ,  $y' \in Y'$ ,  $y \in Y$  such that  $f(x) = y = g(y')$ . Then

$$
g ^ {*} f _ {*} = f _ {*} ^ {\prime} g ^ {\prime *} \quad : K _ {q} ^ {\prime} X \longrightarrow K _ {q} ^ {\prime} Y ^ {\prime}.
$$

Sketch of proof. Set $\underline{\underline{L}} = \underline{\underline{P}}(X, g') \cap \underline{\underline{F}}(X, f)$. From the formula $Lg^{*}Rf_{*} = Rf'_{*}Lg'^{*}$ in the derived category [SGA 6 IV 3.1.0], one deduces that for $F \in \underline{\underline{L}}$ we have that $f_{*}F \in \underline{\underline{P}}(Y, g)$, $g'^{*}F \in \underline{\underline{F}}(X', f')$, and that there is an isomorphism $g^{*}f_{*}(F) = f'_{*}g'^{*}(F)$. Thus everything comes to showing that $K_{q} \underline{\underline{L}} \xrightarrow{\sim} K'_{q}X$. Since $K_{q} \underline{\underline{P}}(X, g') \xrightarrow{\sim} K'_{q}X$, we have only to check that the inclusion $\underline{\underline{L}} \longrightarrow \underline{\underline{P}}(X, g')$ induces isomorphisms on $K$-groups. But this follows from the resolution theorem, because the exact sequence 2.9 shows that the functors $R^{i}f_{*}$ on the category $\underline{\underline{P}}(X, g')$ are effaceable for $i > 0$.

3. Closed subschemes. Let $Z$ be a closed subscheme of $X$, let $i: Z \to X$ be the canonical immersion, and let $I$ be the coherent sheaf of ideals in $\underline{Q}_X$ defining $Z$. The functor $i_*: \underline{M}(Z) \to \underline{M}(X)$ allows us to identify coherent sheaves on $Z$ with coherent sheaves on $X$ killed by $I$.

Proposition 3.1. If I is nilpotent, then $i_* : K'Z \to K'X$ is an isomorphism. In particular, $K'(X_{\text{red}}) \xrightarrow{\sim} K'X$.

This is an immediate consequence of Theorem 4.

Proposition 3.2. Let U be the complement of Z in X, and j: U → X the canonical open immersion. Then there is a long exact sequence

$$
\longrightarrow \mathrm{K} _ {\mathrm{q} + 1} ^ {\prime} \mathrm{U} \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{Z} \xrightarrow {\mathrm{i} _ {*}} \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{X} \xrightarrow {\mathrm{j} ^ {*}} \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{U} \longrightarrow\tag{3.3}
$$

Proof. One knows [Gabriel, Ch. V] that $j^{*} : \underline{\underline{M}}(X) \to \underline{\underline{M}}(U)$ induces an equivalence of $\underline{\underline{M}}(U)$ with the quotient category $\underline{\underline{M}}(X)/\underline{\underline{B}}$, where $\underline{\underline{B}}$ is the Serre subcategory consisting of coherent sheaves with support in $Z$. Theorem 4 implies that $i_{*} : \underline{\underline{M}}(Z) \to \underline{\underline{B}}$

induces isomorphisms on K-groups, so the desired exact sequence results from Theorem 5.

Remark 3.4. The exact sequence 3.3 has some evident naturality properties which follow from the fact that it is the homotopy exact sequence of the "fibration"

$$
\mathrm{BQ} (\underline {{\mathrm{M}}} (Z)) \longrightarrow \mathrm{BQ} (\underline {{\mathrm{M}}} (X)) \longrightarrow \mathrm{BQ} (\underline {{\mathrm{M}}} (U)).
$$

For example, if $Z'$ is a closed subscheme of $X$ containing $Z$, then there is a map from the exact sequence of $(X,Z)$ to the one for $(X,Z')$. Also a flat map $f: X' \to X$ induces a map from the exact sequence for $(X,Z)$ to the one for $(X',f^{-1}Z)$.

Remark 3.5. From 3.3 one deduces in a well-known fashion a Mayer-Vietoris sequence

$$
\longrightarrow \mathrm{K} _ {\mathrm{q} + 1} ^ {\prime} (\mathrm{U} \cap \mathrm{V}) \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} (\mathrm{U} \cup \mathrm{V}) \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} \cup \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{V} \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} (\mathrm{U} \cap \mathrm{V}) \longrightarrow
$$

for any two open sets U and V of X. Starting essentially from this point, Brown and Gersten (see their paper in this proceedings) construct a spectral sequence

$$
\mathrm{E} _ {2} ^ {\mathrm{pq}} = \mathrm{H} ^ {\mathrm{p}} (X, \underset {- q} {K ^ {\prime}}) \Longrightarrow K _ {- n} ^ {\prime} X
$$

which reflects the fact that K'-theory is a sheaf of generalized cohomology theories in a certain sense. In connection with this, we mention that Gersten has proposed defining higher K-groups for regular schemes by piecing together the Karoubi-Villamayor theories belonging to the open affine subschemes (see [Gersten 2]). Using the above Mayer-Vietoris sequence and the fact that Karoubi-Villamayor K-theory coincides with ours for regular rings, Gersten has shown that his method leads to the groups $\mathbf{K}_{\alpha}\mathbf{X} = \mathbf{K}_{\alpha}'\mathbf{X}$ studied here.

## 4. Affine and projective space bundles.

Proposition 4.1. (Homotopy property) Let $f: P \to X$ be a flat map whose fibres are affine spaces (for example, a vector bundle or a torsor under a vector bundle). Then $f^*: K'X \to K'P$ is an isomorphism.

Proof. If $Z$ is a closed subset of $X$ with complement $U$, then because $f$ is flat we have a map of exact sequences

$$
\begin{array}{c c c c c} \longrightarrow & K ^ {\prime} Z & \longrightarrow & K ^ {\prime} X & \longrightarrow & K ^ {\prime} U \\ & q & & q & & q \\ & \downarrow & & \downarrow & & \downarrow \\ \longrightarrow & K ^ {\prime} P _ {Z} & \longrightarrow & K ^ {\prime} P & \longrightarrow & K ^ {\prime} P _ {U} \\ & q & & q & & q \end{array}
$$

By the five lemma, the proposition is true for one of $X, Z$, and $U$ if it is true for the other two. Using noetherian induction we can assume the proposition holds for all closed subsets $Z \neq X$. We can suppose $X$ is irreducible, for if $X = Z_1 \cup Z_2$ with $Z_1, Z_2 \neq X$, then the proposition holds for $Z_1$ and $X - Z_1 = Z_2 - (Z_1 \cap Z_2)$, hence also for $X$. We can also suppose $X$ reduced by 3.1.

Now take the inductive limit in the above diagram as $Z$ runs over all closed subsets $\neq X$. Then by 2.4, $\varinjlim K'U = K'q(k(x))$ and $\varinjlim K'p_{q}U = K'q(k(x)x_XP)$, where $k(x)$ is the residue field at $x$, and where $x$ is the generic point of $X$. Thus we have reduced to the case where $X = \text{Spec}(k)$, $k$ a field, and we want to prove $K'k \cong K'q(k[t_1, \ldots, t_n])$. But this follows from §6 Th. 8, so the proof is complete.

4.2. Jouanolou's device. Jouanolou has shown that at least for a quasi-projective scheme $X$ over a field, there is a torsor $P$ over $X$ with group a vector bundle such that $P$ is an affine scheme. He defines higher $K$-groups for smooth $X$ by taking the Karoubi-Villamayor $K$-groups of the coordinate ring of $P$ and showing that these do not depend on the choice of $P$. From 4.1 it is clear that his method yields the groups $KX = K'X$ considered here.

Proposition 4.3. Let E be a vector bundle of rank r over X, let PE = Proj(SE) be the associated projective bundle, where SE is the symmetric algebra of E, and let f : PE → X be the structural map. Then we have a K$_{0}$(PE)-module isomorphism

$$
\mathrm{K} _ {\mathrm{o}} (\mathrm{PE}) \otimes_ {\mathrm{K} _ {\mathrm{o}} \mathrm{X}} \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{X} \quad \stackrel {{\sim}} {{\longrightarrow}} \quad \mathrm{K} _ {\mathrm{q}} ^ {\prime} (\mathrm{PE})\tag{4.4}
$$

given by $y \otimes x \mapsto y \cdot f^*x$. Equivalently, if $z \in K_0(\text{PE})$ is the class of the canonical line bundle $O(-1)$, then we have an isomorphism

$$
\left(K _ {q} ^ {\prime} X\right) ^ {r} \stackrel {{\sim}} {{\rightarrow}} K _ {q} ^ {\prime} (P E), \quad \left(x _ {i}\right) _ {0 \leqslant i <   r} \mapsto \sum_ {i = 0} ^ {r - 1} z ^ {i} \cdot f * x _ {i}.\tag{4.5}
$$

Sketch of proof. The equivalence of 4.4 and 4.5 results from the fact that $K_{0}(PE)$ is a free $K_{0}X$-module with basis $1, \ldots, z^{r-1}$, [SGA 6 VI 1.1]. Using the exact sequence 3.3 as in the proof of 4.1, one reduces to the case where $X = \text{Spec}(k)$, $k$ a field. By the standard correspondence between coherent sheaves on PE and finitely generated graded SE-modules, one knows that $\underline{\underline{M}}(PE)$ is equivalent to the quotient of Modfgr(SE) by the subcategory of $M$ such that $M_{n} = 0$ for $n$ large. This subcategory has the same $K$-groups as the category $\text{Modfgr}(k)$ by Theorem 4, where we view $k$-modules as SE-modules killed by the augmentation ideal. Thus from the localization theorem we have an exact sequence

$$
\longrightarrow K _ {q} (\operatorname{Modfgr} (k)) \xrightarrow {i _ {*}} K _ {q} (\operatorname{Modfgr} (S E)) \xrightarrow {j _ {*}} K _ {q} ^ {\prime} (P E) \longrightarrow\tag{4.6}
$$

where i is the inclusion and j associates to a module M the associated sheaf M on PE. From Theorem 6 we have the vertical isomorphisms in the square

$$
\begin{array}{c} \mathrm{K} _ {\mathrm{q}} (\text {Modfgr} (\mathrm{k})) \xrightarrow {\mathrm{i} _ {*}} \mathrm{K} _ {\mathrm{q}} (\text {Modfgr} (\mathrm{SE})) \\ \uparrow \mathrm{s} \\ \mathbb {Z} [ t ] \otimes \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{k} \xrightarrow {\mathrm{h}} \mathbb {Z} [ t ] \otimes \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{k} \end{array}
$$

Using the Koszul resolution

$$
0 \longrightarrow \mathrm{SE} (- r) \otimes \bigwedge^ {r} E \otimes M \longrightarrow \dots . \longrightarrow \mathrm{SE} \otimes M \longrightarrow M \longrightarrow O
$$

and Th. 2, Cor. 3, one shows that the map h rendering the above square commutative is multiplication by $\lambda_{-t}(E) = \sum (-t)^{i}[\Lambda^{i}E]$. Thus $i_*$ is injective, so from 4.6 we get an isomorphism

$$
\underset {0 \leqslant i <   r} {\text {   Ⅱ   }} t ^ {i} \otimes K _ {q} ^ {\prime} k \quad \xrightarrow {\sim} \quad K _ {q} ^ {\prime} (P E)
$$

induced by the functors $M \mapsto \underline{Q}(-1)^{\mathfrak{M}^1} \otimes_k M$, $O \leqslant i < r$ from $\text{Modf}(k)$ to $\underline{M}(PE)$. This gives the desired isomorphism 4.5.

The following generalizes 3.1.

Proposition 4.7. Let $f: X' \to X$ be a finite morphism which is radical and surjective (i.e. for each $x$ in $X$ the fibre $f^{-1}(x)$ has exactly one point $x'$ and the residue field extension $k(x') / k(x)$ is purely inseparable). Let $S$ be the multiplicative system in $Z$ generated by the degrees $[k(x'): k(x)]$ for all $x$ in $X$. Then $f_*: K'_q(X') \to K'_qX$ induces an isomorphism $S^{-1}K'_q(X') \cong S^{-1}K'_qX$.

Proof. If Z is a closed subscheme of X with complement U, and if  $Z'$  and  $U'$  are the respective inverse images of Z and U in  $X'$, then we have a map of exact sequences

$$
\begin{array}{c} \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} (\mathrm{Z} ^ {\prime}) \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} (\mathrm{X} ^ {\prime}) \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} (\mathrm{U} ^ {\prime}) \longrightarrow \\ \Biggl \downarrow (\mathrm{f} _ {\mathrm{Z}}) _ {*} \quad \Biggl \downarrow \mathrm{f} _ {*} \quad \Biggl \downarrow (\mathrm{f} _ {\mathrm{U}}) _ {*} \\ \longrightarrow \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{Z} \xrightarrow {} \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{X} \xrightarrow {} \mathrm{K} _ {\mathrm{q}} ^ {\prime} \mathrm{U} \end{array}
$$

Localizing with respect to S and using the five lemma, we see that if the proposition holds for two of $f_Z$, $f$, $f_U$ it holds for the third. Thus arguing as in the proof of 4.1 we can reduce to the case where $X = \text{Spec}(k)$, $k$ a field. By 3.1 we can suppose $X' = \text{Spec}(k')$, where $k'$ is a purely inseparable finite extension of $k$. Thus we have reduced to the following.

Proposition 4.8. Let $f: k \to k'$ be a purely inseparable finite extension of degree $p^d$. Then $f_* f* = \underline{\text{multiplication by }} p^d$ on $K_q k$ and $f * f_* = \underline{\text{multiplication by }} p^d$ on $K_q(k')$.

Proof. The fact that $f_{*}f^{*} =$ multiplication by $[k':k]$ is an immediate consequence of the projection formula §4 (5) and does not use the purely inseparable hypothesis. The homomorphism $f^{*}f_{*}$ is induced by the exact functor

$$
V \mapsto k ^ {\prime} \otimes_ {k} V = (k ^ {\prime} \otimes_ {k} k ^ {\prime}) \otimes_ {k}, V
$$

from  $\underline{\underline{P}}(k')$  to itself. Since  $k'/k$  is purely inseparable, the augmentation ideal I of  $k' \otimes_{k} k'$  is nilpotent. Filtering by powers of I, one obtains a filtration of the above functor with

$$
\operatorname{gr} \left(\left(k ^ {\prime} \otimes_ {k} k ^ {\prime}\right) \otimes_ {k}, V\right) = \prod_ {n} \left(I ^ {n} / I ^ {n + 1}\right) \otimes_ {k}, V.
$$

But because the two $k'$-module structures on $I^n / I^{n+1}$ coincide, this graded functor is isomorphic to the functor $V \mapsto V^r$, where $r = \dim_{k'} (\text{gr}(k' \otimes_k k')) = p^d$. Applying Th. 2, Cor. 2 to this filtration, we find $f^* f_* = \text{multiplication by } p^d$, completing the proof.

5. Filtration by support, Gersten's conjecture, and the Chow ring. Let $\underline{\underline{M}}_{\underline{\underline{p}}}(\underline{\underline{X}})$ denote the Serre subcategory of $\underline{\underline{M}}(\underline{\underline{X}})$ consisting of those coherent sheaves whose support is of codimension $\geqslant p$. (The codimension of a closed subset $Z$ of $X$ is the infimum of the dimensions of the local rings $\underline{\underline{O}}_{\underline{\underline{X}},\underline{\underline{z}}}$ where $z$ runs over the generic points of $Z$.) From §2 (9) and 3.1, it is clear that we have

$$
\mathrm{K} _ {\mathrm{q}} (\underset {= \mathrm{p}} {\mathrm{M}} (X)) = \lim _ {\longrightarrow} \mathrm{K} ^ {\prime} Z\tag{5.1}
$$

where Z runs over the closed subsets of codimension  $\geq p$ . We also have

$$
f ^ {*} \left(\underset {= p} {M} (X)\right) \subset \underset {= p} {M} \left(X ^ {\prime}\right) \quad \text { if } f: X ^ {\prime} \rightarrow X \quad \text { is   flat. }\tag{5.2}
$$

In effect, one has to show that if $Z$ has codimension $\geqslant p$ in $X$, then $f^{-1}Z$ has codimension $\geqslant p$ in $X'$. But if $z'$ is a generic point of $f^{-1}Z$, and $z = f(z')$, then the homomorphism $\underline{O}_{X,z} \to \underline{O}_{X',z'}$ is a flat local homomorphism such that $\text{rad}(\underline{O}_{X,z}) \cdot \underline{O}_{X',z'}$ is primary for $\text{rad}(\underline{O}_{X',z'})$; hence $\dim(\underline{O}_{X,z}) = \dim(\underline{O}_{X',z'})$ by [EGA IV 6.1.3], proving the assertion.

If $X = \varprojlim X_{i}$ where $i \mapsto X_{i}$ is a filtered projective system with affine flat transition morphisms, then we have isomorphisms

$$
\mathrm{K} _ {\mathrm{q}} (\underset {= \mathrm{p}} {\mathrm{M}} (\mathrm{X})) = \underset {\longrightarrow} {\lim} \mathrm{K} _ {\mathrm{q}} (\underset {= \mathrm{p}} {\mathrm{M}} (\mathrm{X} _ {i})) .\tag{5.3}
$$

In view of 5.1 this reduces to showing that any $Z$ of codimension $p$ in $X$ is of the form $f_{i}^{-1}(Z_i)$ for some $i$, where $Z_{i}$ is of codimension $p$ in $X_i$, and where $f_{i}: X \to X_i$ denotes the canonical map. But for $i$ large enough, one has $Z = f_{i}^{-1}(Z_i)$ with $Z_{i} =$ the closure of $f_{i}(Z)$. Hence any generic point $z'$ of $Z_{i}$ is the image of a generic point $z$ of $Z$, so the local rings at $z'$ and $z$ have the same dimension by the result about dimension used above. Thus $Z_{i}$ also has codimension $p$, proving 5.3.

Theorem 5.4. Let $X_p$ be the set of points of codimension $p$ in $X$. There is a spectral sequence

$$
E _ {1} ^ {p q} (X) = \frac {\left| \right|}{x \in X _ {p}} K _ {- p - q} k (x) \Longrightarrow K _ {- n} ^ {\prime} X\tag{5.5}
$$

which is convergent when $X$ has finite (Krull) dimension. This spectral sequence is contravariant for flat morphisms. Furthermore, if $X = \varprojlim X_i$, where $i \mapsto X_i$ is a filtered projective system with affine flat transition morphisms, then the spectral sequence for $X$ is the inductive limit of the spectral sequences for the $X_i$.

In this spectral sequence we interpret  $K_{n}$  as zero for n<0. Thus the spectral sequence is concentrated in the range  $p\geqslant0$ ,  $p+q\leqslant0$ .

Proof. We consider the filtration

$$
\underline {{\underline {{M}}}} (X) = \underline {{\underline {{M}}}} _ {0} (X) \supset \underline {{\underline {{M}}}} _ {1} (X) \supset \dots .
$$

of  $\underline{\mathsf{M}}(\mathsf{X})$  by Serre subcategories. There is an equivalence

$$
\underline {{\underline {{M}}}} _ {p} (X) / \underline {{\underline {{M}}}} _ {p + 1} (X) \simeq \coprod_ {\mathbf {x} \in X _ {p}} \bigcup_ {n} \operatorname{Modf} (\underline {{O}} _ {X, \mathbf {x}} / \operatorname{rad} (\underline {{O}} _ {X, \mathbf {x}}) ^ {n})
$$

so from Th. 4, Cor. 1, one has an isomorphism

$$
\mathrm{K} _ {\mathbf {i}} (\underset {= p} {\mathrm{M}} (X) / \underset {= p + 1} {\mathrm{M}} (X)) \simeq \coprod_ {x \in X _ {p}} \mathrm{K} _ {\mathbf {i}} k (x)
$$

where  $k(x)$  is the residue field at x. From Th. 5 we get exact sequences

$$
\rightarrow \mathrm{K} _ {\mathbf {i}} (\underset {= p + 1} {\mathrm{M}} (X)) \longrightarrow \mathrm{K} _ {\mathbf {i}} (\underset {= p} {\mathrm{M}} (X)) \longrightarrow \underset {x \in X _ {p}} {\text { 丨 }} \mathrm{K} _ {\mathbf {i}} k (x) \longrightarrow \mathrm{K} _ {\mathbf {i} - 1} (\underset {= p + 1} {\mathrm{M}} (X)) \longrightarrow
$$

which give rise to the desired spectral sequence in a standard way. The functorality assertions of the theorem follow immediately from 5.2 and 5.3.

We will now take up a line of investigation initiated by Gersten in his talk at this conference [Gersten 3].

Proposition 5.6. The following conditions are equivalent:

i) For every $p \geq 0$, the inclusion $\underline{\underline{M}}_{=p+1}(X) \to \underline{\underline{M}}_p(X)$ induces zero on K-groups. ii) For all $q$, $E_2^{pq}(X) = 0$ if $p \neq 0$ and the edge homomorphism $K_q' X \to E_2^{Oq}(X)$ is an isomorphism.

$$
\text {   iii)   For   every   } n \text {   the   sequence   } \tag {5.7} 0 \longrightarrow K _ {n} ^ {\prime} X \stackrel {{e}} {{\longrightarrow}} \prod_ {x \in X _ {o}} K _ {n} k (x) \stackrel {{d _ {1}}} {{\longrightarrow}} \prod_ {x \in X _ {1}} K _ {n - 1} k (x) \stackrel {{d _ {1}}} {{\longrightarrow}} \dots
$$

is exact. Here $d_1$ is the differential on $E_1(X)$ and $e$ is the map obtained by pulling-back with respect to the canonical morphisms $\operatorname{Spec} k(x) \to X$.

This follows immediately from the spectral sequence 5.5 and its construction.

Proposition 5.8. (Gersten) Let $\underline{\underline{K^{\prime}}}_{\underline{n}}$ denote the sheaf on $X$ associated to the presheaf $U \mapsto K^{\prime}U$. Assume that $\text{Spec}(O_{\underline{x},x})$ satisfies the equivalent conditions of for all $x$ in $X$. Then there is a canonical isomorphism

$$
\mathrm{E} _ {2} ^ {\mathrm{pq}} (\mathrm{x}) = \mathrm{H} ^ {\mathrm{p}} \left(\mathrm{x}, \underline {{\mathrm{K} ^ {\prime}}} _ {- \mathrm{q}}\right)
$$

with  $E_{2}^{pq}(X)$  as in 5.5.

Proof. We view the sequences 5.7 for the different open subsets of X as a sequence of presheaves, and we sheafify to get a sequence of sheaves

$$
0 \rightarrow \underset {= n} {K ^ {\prime}} \rightarrow \underset {x \in X _ {o}} {\coprod} (i _ {x}) _ {*} (K _ {n} k (x)) \rightarrow \underset {x \in X _ {1}} {\coprod} (i _ {x}) _ {*} (K _ {n - 1} k (x)) \rightarrow ..\tag{5.9}
$$

where $i_x: \text{Spec } k(x) \to X$ denotes the canonical map. The stalk of 5.9 over $x$ is the sequence 5.7 for $\text{Spec}(Q_{\underline{\underline{\mathbf{x}}},x})$, because $\text{Spec}(Q_{\underline{\underline{\mathbf{x}}},x}) = \lim U$, where $U$ runs over the affine open neighborhoods of $x$, and because the spectral sequence 5.5 commutes with such projective limits. By hypothesis, 5.9 is exact, hence it is a flask resolution of $K'_n$, so

$$
\begin{array}{r c l} \mathrm{H} ^ {\mathrm{p}} (X, K _ {= n} ^ {\prime}) & = & \mathrm{H} ^ {\mathrm{p}} \left\{\mathbf {s} \longmapsto \Gamma (X, \bigsqcup_ {\mathbf {x} \in X _ {\mathbf {s}}} (\mathbf {i} _ {\mathbf {x}}) _ {*} K _ {n - s} k (\mathbf {x})) \right\} \\ & = & \mathrm{H} ^ {\mathrm{p}} \left\{\mathbf {s} \longmapsto E _ {1} ^ {s, - n} (X) \right\} = E _ {2} ^ {p, - n} (X) \end{array}
$$

as asserted.

The following conjecture has been verified by Gersten in certain cases [Gersten 3].

Conjecture 5.10. (Gersten) The conditions of 5.6 are satisfied for the spectrum of a regular local ring.

Actually, it seems reasonable to conjecture that the conditions of 5.6 hold more generally for semi-local regular rings, for in the cases where the conjecture has been

proved, the arguments also apply to the corresponding semi-local situation. On the other hand there are examples suggesting that it is unreasonable to expect the conditions of 5.6 to hold for any general class of local rings besides the regular local rings.

We will now prove Gersten's conjecture in some important equi-characteristic cases.

Theorem 5.11. Let $R$ be a finite type algebra over a field $k$, let $S$ be a finite set of primes in $R$ such that $R_p$ is regular for each $p$ in $S$, and let $A$ be the regular semi-local ring obtained by localizing $R$ with respect to $S$. Then Spec A satisfies the conditions of 5.6.

Proof. We first reduce to the case where R is smooth over k. There exists a subfield $k'$ of k finitely generated over the prime field, a finite type $k'$-algebra $R'$, and a finite subset $S'$ of $\operatorname{Spec} R'$ such that $R = k \otimes_k, R'$ and such that the primes in S are the base extensions of the primes in $S'$. If $A'$ is the localization of $R'$ with respect to $S'$, then $A = k \otimes_k, A'$ and $A'$ is regular. Letting $k_i$ run over the subfields of k containing $k'$ and finitely generated over the prime field, we have $A = \varinjlim_{\mathbf{k}} k_i \otimes_k, A'$ and $K_*(M(A)) = \varinjlim_{\mathbf{k}} K_*(M(k_i \otimes_k, A'))$ by 5.3, where here and in the following we write $M(A)$ instead of $M(\operatorname{Spec} A)$. Thus it suffices to prove the theorem when k is finitely generated over the prime field. In this case A is a localization of a finite type algebra over the prime field, so by changing R, we can suppose k is the prime field. As prime fields are perfect, it follows that R is smooth over k at the points of S, hence also in an open neighborhood of S. Replacing R by $R_f$ for some f not vanishing at the points in S, we can suppose R is smooth over k as asserted.

We wish to prove that for any $p \geq 0$ the inclusion $\underline{\underline{M}}_{p+1}(A) \to \underline{\underline{M}}_p(A)$ induces zero on K-groups. By 5.3 we have

$$
K _ {*} \left(\underset {p + 1} {\mathrm{M}} (A)\right) = \underset {\rightarrow} {\lim} K _ {*} \left(\underset {p + 1} {\mathrm{M}} \left(R _ {f}\right)\right)
$$

where f runs over elements not vanishing at the points of S, hence replacing R by  $R_{f}$ , we reduce to showing that the functor  $M_{=p+1}(R) \to M_{=p}(A)$  induces zero on K-groups. As

$$
\mathrm{K} _ {*} (\underset {= p + 1} {\mathrm{M}} (R)) = \underbrace {\lim} _ {\rightarrow} \mathrm{K} _ {*} (\underset {= p} {\mathrm{M}} (R / t R))
$$

where t runs over the regular elements of R, it suffices to show that given a regular element t, there exists an f, not vanishing at the points of S, such that the functor  $M \mapsto M_{f}$  from  $\underset{=p}{M}(R/tR)$  to  $\underset{=p}{M}(R)$  induces zero on K-groups.

We will need the following variant of the normalization lemma.

Lemma 5.12. Let $R$ be a smooth finite type algebra of dimension $r$ over a field $k$, let $t$ be a regular element of $R$, and let $S$ be a finite subset of $\operatorname{Spec} R$. Then there exist elements $x_1, \ldots, x_{r-1}$ of $R$ algebraically independent over $k$ such that if $B = k[x_1, \ldots, x_{r-1}] \subset R$, then i) $R / tR$ is finite over $B$, and ii) $R$ is smooth over $B$ at the points of $S$.

Granting this for the moment, put $B' = R / tR$ and $R' = R \otimes_B B'$ so that we have arrows

![](images/page_49_image_0.jpg)

where the horizontal arrows are finite. Let $S'$ be the finite set of points of $\text{Spec } R'$ lying over the points in $S$. As $u$ is smooth of relative dimension one at the points of $S, u'$ is smooth of relative dimension one at the points of $S'$. One knows then [SGA 1 II 4.15] that the ideal $I = \text{Ker} (R' \to B')$ is principal at the points of $S'$, hence principal in a neighborhood of $S'$. Since $R'/R$ is finite, this neighborhood contains the inverse image of a neighborhood of $S$ in $\text{Spec } R$. Thus we can find $f$ in $R$ not vanishing at the points of $S$ such that $I_f$ is isomorphic to $R'_f$ as an $R'_f$-module. We can also suppose $f$ chosen so that $R'_f$ is smooth, hence flat, over $B'$.

Then for any B'-module M we have an exact sequence of  $R_{f}$ -modules

$$
0 \longrightarrow I _ {f} \otimes_ {B, M} \longrightarrow R _ {f} ^ {\prime} \otimes_ {B, M} \longrightarrow M _ {f} \longrightarrow 0.\tag{*}
$$

Since $R'_{f}$ is flat over $B'$, if $M$ is in $\underline{M}_{=p}(B')$, then $R'_{f} \otimes_{B'} M$ is in $\underline{M}_{=p}(R'_{f})$, so viewed as an $R_{f}$-module, we have $R'_{f} \otimes_{B'} M$ is in $\underline{M}_{=p}(R_{f})$. Thus (\*) is an exact sequence of exact functors from $\underline{M}_{=p}(B')$ to $\underline{M}_{=p}(R_{f})$. Applying Th. 2, Cor. 1, and using the isomorphism $I_{f} \simeq R'_{f}$, we conclude that the functor from $\underline{M}_{=p}(B')$ to $\underline{M}_{=p}(R_{f})$ induces the zero map on K-groups, as was to be shown.

Proof of the lemma. Choosing for each prime in S a maximal ideal containing it, we can suppose S is a finite set of maximal ideals of R. Let $\Omega^1$ be the module of Kahler differentials of R over k. It is a projective R-module of rank r, and for R to be smooth over $B = k[x_1 \ldots, x_{r-1}]$ at the points of S means that the differentials $dx_i \in \Omega^1$ are independent at the points of S. Let J be the intersection of the ideals in S. As $R/J^n = \prod R/m^n$, $m \in S$, is finite dimensional over k, we can find a finite dimensional k-subspace V of R such that for each m in S, there exists $v_1, \ldots, v_r$ in V whose differentials form a basis for $\Omega^1$ at m vanishing at the other points of S. We can suppose also that V generates R as an algebra over k.

Define an increasing filtration of R/tR by letting  $F_{n}(R/tR)$  be the subspace spanned by the monomials of degree  $\leqslant n$  in the elements of V. Then the associated graded ring  $\text{gr}(R/tR)$  is of dimension r-1. To see this, note that  $\text{Proj}(\coprod F_{n}(R/tR))$  is the closure in projective space of the subscheme Spec (R/tR) of the affine space Spec S(V). Since R/tR has dimension r-1, the part of this Proj at infinity, namely  $\text{Proj}(\text{gr}(R/tR))$ , is of dimension r-2, so  $\text{gr}(R/tR)$  has dimension r-1 as asserted. Let  $z_{1},\ldots,z_{r-1}$  be a system of parameters for  $\text{gr}(R/tR)$  such that each  $z_{i}$  is homogeneous of degree  $\geqslant 2$ . Then  $\text{gr}(R/tR)$  is finite over  $k[z_{1},\ldots,z_{r-1}]$ , so if the  $z_{i}$  are lifted to elements  $x_{i}'$  of R, then R/tR is finite over  $k[x_{i}',\ldots,x_{r-1}']$ .

By the choice of V, we can choose  $v_{1},\ldots,v_{r-1}$  in V such that  $x_{i}=x_{i}^{\prime}+v_{i}$ ,  $1\leq i<r$ , have independent differentials at the points of S, whence condition ii) of the lemma is satisfied. On the other hand, the  $x_{i}$  have the leading terms  $z_{i}$  in  $\mathrm{gr}(R/tR)$ , so R/tR is finite over  $k[x_{1},\ldots,x_{r-1}]$ . The proof of the lemma and Theorem 5.11 is now complete.

Theorem 5.13. The conditions of 5.6 hold for Spec A when A is the ring of formal power series $k[[X_1, \ldots, X_n]]$ over a field $k$, and when A is the ring of convergent power series in $X_1, \ldots, X_n$ with coefficients in a field complete with respect to a non-trivial valuation.

The proof is analogous to the preceding. Indeed, given $O \neq t \in A = k[[X_1, \ldots, X_n]]$, then after a change of coordinates, $A / tA$ becomes finite over $B = k[[X_1, \ldots, X_{r-1}]]$ by the Weierstrass preparation theorem. Further, if we put $A' = A \otimes_B A / tA$, then $\text{Ker}(A' \to A / tA)$ is principal, so arguing as before, we can conclude that $M_p(A / tA) \to M_p(A)$ induces zero on $K$-groups. The argument also works for convergent power series, since the preparation theorem is still available.

We now want to give an application of 5.11 to the Chow ring. We will assume known the fact that the $K_{1}A$ defined here is canonically isomorphic to the Bass $K_{1}$, and in particular that $K_{1}A$ is canonically isomorphic to the group of units $A^{*}$, when $A$ is a local ring or a Euclidean domain.

Proposition 5.14. Let X be a regular scheme of finite type over a field. Then the

$$
d _ {1}: \prod_ {\mathbf {x} \in X _ {p - 1}} K _ {1} k (\mathbf {x}) \longrightarrow \prod_ {\mathbf {x} \in X _ {p}} K _ {0} k (\mathbf {x}) = \prod_ {\mathbf {x} \in X _ {p}} Z
$$

in the spectral sequence 5.5 is the subgroup of codimension p cycles which are linearly equivalent to zero. Consequently  $E_{2}^{p,-p}(X)$  is canonically isomorphic to the group  $A^{p}(X)$  of cycles of codimension p modulo linear equivalence.

Proof. Let $P^1$ be the projective line over the ground field, and let $t$ denote the canonical rational function on $P^1$. Let $C^p(X)$ denote the group of codimension $p$ cycles. The subgroup of cycles linearly equivalent to zero is generated by cycles of the form $W_0 - W_\infty$, where $W$ is an irreducible subvariety of $X \times P^1$ of codimension $p$ such that the intersections $W_0 = W \cap (X \times 0)$ and $W_\infty = W \cap (X \times \infty)$ are proper. We need a known formula for $W_0 - W_\infty$ which we now recall.

Let Y be the image of W under the projection  $X \times P^{1} \rightarrow X$ , so that  $\dim(Y) = \dim(W)$  or  $\dim(W) - 1$ . In the latter case we have  $W = Y \times P^{1}$  and  $W_{0} - W_{\infty} = 0$ , so we may assume  $\dim(W) = \dim(Y)$ , whence Y has codimension p - 1 in X. Let y be the generic point of Y and w the generic point of W, so that  $k(w)$  is a finite extension of  $k(y)$ . Let  $t'$  be the non-zero element of  $k(w)$  obtained by pulling t back to W, and let x be a point of codimension one in Y, whence  $O_{=Y,x}$  is a local domain of dimension one with quotient field  $k(y)$ . Then the formula we want is

$$
\text {(multiplicity of} \quad x \quad \text {in} \quad W _ {o} - W _ {\infty}) = \operatorname{ord} _ {y x} (\operatorname{Norm} _ {k (w) / k (y)} t ^ {\prime})\tag{5.15}
$$

where $\operatorname{ord}_{\mathbf{vx}}: k(y)^{\bullet} \to \mathbb{Z}$ is the unique homomorphism such that

$$
\operatorname{ord} _ {\mathbf {y x}} (\mathbf {f}) = \text { length } (O _ {= Y, \mathbf {x}} / f O _ {= Y, \mathbf {x}})
$$

for $f \in \mathbb{O}_{\geq Y, X}$, $f \neq 0$. For a proof of 5.15 see [Chevalley, p. 2-12].

From 5.15 it is clear that the subgroup of cycles linearly equivalent to zero is

the image of the homomorphism

$$
\phi : \underset {y \in X _ {p - 1}} {\coprod} k (y) ^ {*} \longrightarrow \underset {x \in X _ {p}} {\coprod} Z x = C ^ {p} (X)
$$

where if $f \in k(y)^*$, then $\phi(f) = \sum \text{ord}_{yx}(f) \cdot x$ and we put $\text{ord}_{yx} = 0$ if $x \notin \{\overline{y}\}$. Since $K_1 k(y) = k(y)^*$, we see $\phi$ is a map from $E_1^{p-1}, -p(X)$ to $E_1^{p}, -p(X)$, so all that remains to prove the proposition is to show that $\phi = d_1$.

Let $d_{1}$ have the components

$$
\left(d _ {1}\right) _ {\mathbf {y x}}: k (\mathbf {y}) ^ {*} = K _ {1} k (\mathbf {y}) \longrightarrow K _ {0} k (\mathbf {x}) = Z
$$

for y in  $X_{p-1}$  and x in  $X_{p}$ . We want to show that  $(d_{1})_{yx} = \text{ord}_{yx}$ . Fix y in  $X_{p-1}$  and let Y be its closure. The closed immersion  $Y \to X$  carries  $M_{j}(Y)$  to  $M_{j+p-1}(X)$  for all j, hence it induces a map from the spectral sequence 5.5 for Y to the one for X augmenting the filtration by p-1. Thus we get a commutative diagram

$$
\begin{array}{r c l r c l} & \mathrm{E} _ {1} ^ {\mathrm{p} - 1, - \mathrm{p}} (\mathrm{X}) & \xrightarrow {\mathrm{d} _ {1}} & \mathrm{E} _ {1} ^ {\mathrm{p}, - \mathrm{p}} (\mathrm{X}) & = & \mathrm{C} ^ {\mathrm{p}} (\mathrm{X}) \\ & \uparrow & & \uparrow & & \\ \mathrm{K} _ {1} \mathrm{k} (\mathrm{y}) & = & \mathrm{E} _ {1} ^ {\mathrm{O}, - 1} (\mathrm{Y}) & \xrightarrow {\mathrm{d} _ {1}} & \mathrm{E} _ {1} ^ {1, - 1} (\mathrm{Y}) & = & \mathrm{C} ^ {1} (\mathrm{Y}) \end{array}
$$

which shows that $(\mathbf{d}_1)_{\mathbf{yx}} = 0$ unless $\mathbf{x}$ is in Y. On the other hand, if $\mathbf{x}$ is of codimension one in Y, then the flat map $\operatorname{Spec}(\underline{\underline{\mathbf{O}}}_{\underline{\underline{\mathbf{Y}}},\mathbf{x}}) \to \mathbf{Y}$ induces a map of spectral sequences, so we get a commutative diagram

$$
\begin{array}{r c l r c l} \mathrm{K} _ {1} \mathrm{k(y)} & = & \mathrm{E} _ {1} ^ {\mathrm{O}, - 1} (\mathrm{Y}) \xrightarrow {\mathrm{d} _ {1}} & \mathrm{E} _ {1} ^ {1, - 1} (\mathrm{Y}) & = & \mathrm{C} ^ {1} (\mathrm{Y}) \\ | | & & \Big \downarrow & \Big \downarrow & & \Big \downarrow_ {\text {   multiplicity   }} \\ \mathrm{K} _ {1} \mathrm{k(y)} & = & \mathrm{E} _ {1} ^ {\mathrm{O}, - 1} (\underline {{\mathrm{O}}} _ {\mathrm{Y,x}}) \xrightarrow {\mathrm{d} _ {1}} & \mathrm{E} _ {1} ^ {1, - 1} (\underline {{\mathrm{O}}} _ {\mathrm{Y,x}}) & = & \mathrm{Z} \end{array}
$$

which shows that $(d_1)_{yx}$ is the map $d_1$ in the spectral sequence for $\underline{O}_{Y,x}$. Therefore the equality $(d_1)_{yx} = \text{ord}_{yx}$ is a consequence of the following.

Lemma 5.16. Let $A$ be an equi-characteristic local noetherian domain of dimension one with quotient field $F$ and residue field $k$, and let

$$
\rightarrow \mathrm{K} _ {1} ^ {\prime} \mathrm{A} \rightarrow \mathrm{K} _ {1} \mathrm{F} \xrightarrow {\partial} \mathrm{K} _ {0} \mathrm{k} \rightarrow \mathrm{K} _ {0} ^ {\prime} \mathrm{A} \rightarrow \mathrm{K} _ {0} \mathrm{F} \rightarrow 0
$$

be the exact sequence 3.3 associated to the closed set Spec k of Spec A. Then $\partial: K_1 F \longrightarrow K_0 k$ is isomorphic to ord: $F^* \to \mathbb{Z}$, where ord is the homomorphism such that $\text{ord}(x) = \text{length}(A / xA)$ for $x$ in $A, x \neq 0$.

Proof. We have isomorphisms $K_1F = F^*$ and $K_1A = A^*$ since $A$ and $F$ are local rings. We wish to show $\partial(x) = \text{ord}(x)$ for $x$ in $A, x \neq 0$. If $x$ is in $A^*$, this is clear, as $\partial(x) = 0$ since $x$ is in the image of the map $K_1A \to K_1'A \to K_1F$. Thus we can suppose $x$ is not a unit. By hypothesis $A$ is an algebra over the prime subfield $k_0$ of $k$. If $x$ were algebraic over $k_0$, it would be a unit in $A$. Thus $x$ is not algebraic, so we have a flat homomorphism $k_0[t] \to A$ sending the indeterminate $t$ to $x$. By naturality of the exact sequence 3.3 for flat maps, we get a commutative diagram

![](images/page_52_image_0.jpg)

such that  $u(t) = x$ . The homomorphism v is induced by sending a  $k_{0}$ -vector space V to the A-module

$$
A \otimes_ {k _ {o} [ t ]} V = A / x A \otimes_ {k _ {o}} V
$$

and using devissage to identify the K-groups of the category of A-modules of finite length with those of $\underline{\underline{P}}(k)$. Thus with respect to the isomorphisms $K_{0}k_{0}=K_{0}k=Z$, v is multiplication by $\text{length}(A/xA)=\text{ord}(x)$. Therefore it suffices to show that in the top row of the above diagram, one has $\partial(t)=\pm1$. But this is easily verified by explicitly computing the top row, using the fact that $K_{0}R=Z$ and $K_{1}R=R^{*}$ for a Euclidean domain. q.e.d.

Remark 5.17. In another paper, along with the proof of Theorem 1 of [Quillen 1], I plan to justify the following description of the boundary map $\partial: K_{n} F \to K_{n-1} k$ for a local noetherian domain $A$ of dimension one with quotient field $F$ and residue field $k$. By the universal property of the $K$-theory of a ring, such a map is defined by giving for every finite dimensional vector space $V$ over $F$ a homotopy class of maps

$$
\mathrm{B} (\mathrm{Aut} (\mathrm{V})) \longrightarrow \mathrm{BQ} (\underline {{\mathrm{P}}} (\mathrm{k}))\tag{5.18}
$$

compatible with direct sums. To do this consider the set of A-lattices in V, i.e. finitely generated A-submodules L such that  $F \otimes_{A} L = V$ . Let  $X(V)$  be the ordered set of layers  $(L_{0}, L_{1})$  such that  $L_{1}/L_{0}$  is killed by the maximal ideal of A, and put  $G = \text{Aut}(V)$ . Then G acts on  $X(V)$ , so we can form a cofibred category  $X(V)_{G}$  over G with fibre  $X(V)$ . One can show that  $X(V)$  is contractible (it is essentially a 'building'), hence the functor  $X(V)_{G} \to G$  is a homotopy equivalence. On the other hand there is a functor  $X(V)_{G} \to Q(P(k))$  sending  $(L_{0}, L_{1})$  to  $L_{1}/L_{0}$ , hence we obtain the desired map 5.18.

It can be deduced from this description that the Lemma 5.16 is valid without the equi-characteristic hypothesis.

Combining 5.8, 5.11, and 5.14 we obtain the following.

Theorem 5.19. For a regular scheme X of finite type over a field, there is a canonical isomorphism

$$
\mathrm{H} ^ {\mathrm{p}} (\mathrm{X}, \underset {=} {\mathrm{K}} _ {\mathrm{p}}) = \mathrm{A} ^ {\mathrm{p}} (\mathrm{X}).
$$

For $p = 0$ and 1 this amounts to the trivial formulas $H^0(X, \mathbb{Z}) = C^0(X)$ and $H^1(X, Q_X^*) = \text{Pic}(X)$. For $p = 2$ this formula has been established by Spencer Bloch in certain cases (see his paper in this proceedings).

One noteworthy feature about the formula 5.19 is that the left side is manifestly contravariant in X, which suggests that higher K-theory will eventually provide the tool for a theory of the Chow ring for non-projective nonsingular varieties.

## §8. Projective fibre bundles

The main result of this section is the computation of the K-groups of the projective bundle associated to a vector bundle over a scheme. It generalizes the theorem about Grothendieck groups in [SGA 6 VI] and may be considered as a first step toward a higher K-theory for schemes (as opposed to the K'-theory developed in the preceding section). The method of proof differs from that of [SGA 6] in that it uses the existence of canonical resolutions for sheaves on projective space which are regular in the sense of [Mumford, Lecture 14]. We also discuss two variants of this result proved by the same method. The first concerns the 'projective line' over a (not necessarily commutative) ring; it is one of the ingredients for a higher K generalization of the 'Fundamental Theorem' of Bass to be presented in a later paper. The second is a formula relating the K-groups of a Severi-Brauer scheme with those of the associated Azumaya algebra and its powers, which was inspired by a calculation of Roberts.

1. The canonical resolution of a regular sheaf on PE. Let S be a scheme (not necessarily noetherian or separated), let E be a vector bundle of rank r over S, and let X = PE = Proj(SE) be the associated projective bundle, where SE is the symmetric algebra of E over  $\underline{O}_{S}$ . Let  $\underline{O}_{X}(1)$  be the canonical line bundle on X and f : X → S the structural map. We will use the term "X-module" to mean a quasi-coherent sheaf of  $\underline{O}_{X}$ -modules, unless specified otherwise.

The following lemma summarizes some standard facts about the higher direct image functors  $R^{q}f_{*}$  we will need.

Lemma 1.1. a) For any X-module F, R$^{q}$f$_{*}$(F) is an S-module which is zero for q≥r.

b) For any X-module F and vector bundle E' on S, one has

$$
R ^ {q} f _ {*} (F) \otimes_ {S} E ^ {\prime} = R ^ {q} f _ {*} (F \otimes_ {S} E ^ {\prime}).
$$

c) For any S-module N, one has

$$
R ^ {q} f _ {*} (O _ {X} (n) \otimes_ {S} N) = \left\{ \begin{array}{c c} 0 & q \neq 0, r - 1 \\ S _ {n} E \otimes_ {S} N & q = 0 \\ (S _ {r - n} E) ^ {\vee} \otimes_ {S} \bigwedge^ {r} E \otimes_ {S} N & q = r - 1 \end{array} \right.
$$

where "▼" denotes the dual vector bundle.

d) If F is an X-module of finite type (e.g. a vector bundle), and if S is affine, then F is a quotient of  $(\underline{O}_{X}(-1)^{\otimes n})^{k}$  for some n, k.

Parts a), c) result from the standard Cech calculations of the cohomology of projective space [EGA III 2]. Part b) is obvious since locally E' is a direct sum of finitely many copies of $\underline{\underline{O}}_{\mathbf{S}}$. For d), see [EGA II 2.7.10].

Following Mumford, we call an X-module F regular if  $R^{q}f_{*}(F(-q)) = 0$  for q > 0, where as usual,  $F(n) = \underline{O}_{X}(1)^{\otimes n} \otimes_{X} F$ . For example, we have  $O_{X}(n) \otimes_{S} N$  is regular for  $n \geq 0$  by c).

Lemma 1.2. Let $0 \to F' \to F \to F'' \to 0$ be an exact sequence of X-modules.

a) If $F'(n)$ and $F''(n)$ are regular, so is $F(n)$.

b) If  $F(n)$  and  $F'(n+1)$  are regular, so is  $F''(n)$ .

c) If $F(n+1)$ and $F''(n)$ are regular, and if $f_*(F(n)) \to f_*(F''(n))$ is onto, then $F'(n+1)$ is regular.

Proof. This follows immediately from the long exact sequence

$$
R ^ {q} f _ {*} (F ^ {\prime} (n - q)) \longrightarrow R ^ {q} f _ {*} (F (n - q)) \longrightarrow R ^ {q} f _ {*} (F ^ {\prime \prime} (n - q)) \longrightarrow R ^ {q + 1} f _ {*} (F ^ {\prime} (n - q)) \longrightarrow R ^ {q + 1} f _ {*} (F (n - q)).
$$

The following two lemmas appear in [Mumford, Lecture 14] and in [SGA 6 XIII 1.3], but the proof given here is slightly different.

Lemma 1.3. If $F$ is regular, then $F(n)$ is regular for all $n \geqslant 0$.

Proof. From the canonical epimorphism $\underline{\underline{O}}_{X} \otimes_{S} E \to \underline{\underline{O}}_{X}(1)$ one has an epimorphism

$$
\underset {X} {\mathrm{O}} (- 1) \otimes_ {S} E \rightarrow \underset {X} {\mathrm{O}}\tag{1.4}
$$

so we get an exact sequence of vector bundles on $X$

$$
0 \rightarrow \underline {{\underline {{O}}}} _ {X} (- r) \otimes_ {S} \bigwedge^ {r} E \rightarrow \dots \rightarrow \underline {{\underline {{O}}}} _ {X} (- 1) \otimes_ {S} E \rightarrow \underline {{\underline {{O}}}} _ {X} \rightarrow 0\tag{1.5}
$$

by taking the exterior algebra of $\underline{\underline{O}}_X(-1) @_S E$ with differential the interior product by 1.4. Tensoring with $F$ we obtain an exact sequence

$$
0 \longrightarrow F (- r) \otimes_ {S} \Lambda^ {r} E \longrightarrow \dots \longrightarrow F (- 1) \otimes_ {S} E \longrightarrow F \longrightarrow 0.\tag{1.6}
$$

Assuming F to be regular, then  $(F(-p)\mathbb{W}_{S}\Lambda^{p}E)(p)$  is seen to be regular using 1.1 b). Thus if 1.6 is split into short exact sequences

$$
0 \rightarrow z _ {p} \rightarrow F (- p) \otimes_ {S} \Lambda^ {p} E \rightarrow z _ {p - 1} \rightarrow 0
$$

we can use 1.2 b) to show by decreasing induction on p that $Z_{p}(p+1)$ is regular. Thus $Z_{0}(1) = F(1)$ is regular, so the lemma follows by induction on n.

Lemma 1.7. If F is regular, then the canonical map  $O_{X} \otimes_{S} f_{*}(F) \to F$  is surjective.

Proof. From the preceding proof one has an exact sequence

$$
0 \longrightarrow Z _ {1} \longrightarrow F (- 1) \otimes_ {S} E \longrightarrow F \longrightarrow 0
$$

where $Z_1(2)$ is regular. Thus $R^1 f_*(Z_1(n)) = 0$ for $n \geqslant 1$, so we find that the canonical map $f_*(F(n-1)) \otimes_S E \longrightarrow f_*(F(n))$ is surjective for $n \geqslant 1$. Hence the canonical map of SE-modules

$$
\mathrm{SE} \otimes_ {S} f _ {*} (F) \longrightarrow \coprod_ {n \geqslant 0} f _ {*} (F (n))
$$

is surjective. The lemma follows by taking associated sheaves.

Suppose now that F is an X-module which admits a resolution

$$
0 \longrightarrow \underset {= X} {O} (- r + 1) \otimes_ {S} T _ {r - 1} \longrightarrow \dots \longrightarrow \underset {= X} {O} \otimes_ {S} T _ {o} \longrightarrow F \longrightarrow O
$$

where the  $T_{i}$  are modules on S. Breaking this sequence up into short exact sequences

and applying 1.2 b), one sees as in the proof of 1.3 that F has to be regular. Moreover, the above exact sequence can be viewed as a resolution of the zero module by acyclic objects for the $\delta$-functor $R^{q}f_{*}(\ref{eq:0})$, where n is any fixed integer $\geqslant 0$. Thus on applying $f_{*}$ we get an exact sequence

$$
0 \rightarrow S _ {n - r + 1} E \otimes_ {S} T _ {r - 1} \longrightarrow \dots \rightarrow S _ {n} E \otimes_ {S} T _ {o} \longrightarrow f _ {*} (F (n)) \longrightarrow 0
$$

for each  $n \geq 0$ . In particular, we have exact sequences

$$
(1. 8) \quad 0 \rightarrow T _ {n} \rightarrow E \otimes_ {S} T _ {n - 1} \longrightarrow \dots \rightarrow f _ {*} (F (n)) \longrightarrow 0
$$

for $n = 0, \ldots, r-1$ which can be used to show recursively that the modules $T_n$ are determined by $F$ up to canonical isomorphism.

Conversely, given an X-module F, we inductively define a sequence of X-modules  $Z_{n} = Z_{n}(F)$  and a sequence of S-modules  $T_{n} = T_{n}(F)$  as follows. Starting with  $Z_{-1} = F$ , let  $T_{n} = f_{*}(Z_{n-1}(n))$ , and let  $Z_{n}$  be the kernel of the canonical map  $O_{X}(-n) \otimes S_{n} \to Z_{n-1}$ . It is clear that  $Z_{n}$  and  $T_{n}$  are additive functors of F.

Supposing now that $F$ is regular, we show by induction that $Z_{n}(n + 1)$ is regular, this being clear for $n = -1$. We have an exact sequence

$$
0 \longrightarrow Z _ {n} (n) \longrightarrow \underline {{O}} _ {X} \otimes_ {S} T _ {n} \stackrel {{c}} {{\longrightarrow}} Z _ {n - 1} (n) \longrightarrow 0\tag{1.9}
$$

where the canonical map $c$ is surjective by 1.7 and the induction hypothesis. By 1.3, 1.2c) we find that $Z_{n}(n + 1)$ is regular, so the induction works. In addition we have

$$
\mathbf {f} _ {*} (Z _ {n} (n)) = 0 \quad \text { for } n \geqslant 0\tag{1.10}
$$

because c induces an isomorphism after applying  $f_{*}$ .

From 1.9 and the fact that $f_*$ is exact on the category of regular X-modules, one concludes by induction that $F \mapsto T_n(F)$ is an exact functor from regular X-modules to S-modules.

We next show that $Z_{r-1} = 0$. From 1.9 we get exact sequences

$$
R ^ {q - 1} f _ {*} (Z _ {n + q - 1} (n)) \xrightarrow {\delta} R ^ {q} f _ {*} (Z _ {n + q} (n)) \longrightarrow R ^ {q} f _ {*} (\underline {{O}} _ {X} (- q) @ S ^ {T} n + q)
$$

which allow one to prove by induction on $q$, starting from 1.10, that $R^{q}f_{*}(Z_{n + q}(n)) = 0$ for $q, n \geqslant 0$. This shows that $Z_{r-1}(r-1)$ is regular, since $R^{q}f_{*}$ is zero for $q \geqslant r$. By 1.10 and 1.7 we have $Z_{r-1}(r-1) = 0$, so $Z_{r-1} = 0$ as was to be shown.

Combining the exact sequences 1.9 we obtain a canonical resolution of the regular sheaf $F$ of length $r - 1$. Thus we have proved the following.

Proposition 1.11. Any regular X-module F has a resolution of the form

$$
0 \longrightarrow \underset {= X} {\mathrm{O}} (- r + 1) \otimes_ {S} T _ {r - 1} (F) \longrightarrow \dots \longrightarrow \underset {= X} {\mathrm{O}} \otimes_ {S} T _ {o} (F) \longrightarrow F \longrightarrow 0
$$

where the  $T_{i}(F)$  are S-modules determined up to unique isomorphism by F. Moreover  $F \mapsto T_{i}(F)$  is an exact functor from the category of regular X-modules to the category of S-modules.

The next three lemmas are concerned with the situation when $F$ is a vector bundle on $X$.

$$
\begin{array}{l l} \text {Lemma 1.12. Assume S is quasi - compact. Then for any vector bundle F on X,} \\ \text {there exists an integer n} _ {\circ} \text {such that for all S -modules N and n≥n}, \text {one has} \\ \text {a)} & R ^ {q} f _ {*} (F (n) @ _ {S} N) = 0 \text {for q > 0} \\ \text {b)} & f _ {*} (F (n)) @ _ {S} N \xrightarrow {} f _ {*} (F (n) @ _ {S} N) \\ \text {c)} & f _ {*} (F (n)) \text {is a vector bundle on S.} \end{array}
$$

Proof. Because $S$ is the union of finitely many open affines, it suffices to prove the lemma when $S$ is affine. In this case $F$ is the quotient of $L = \underline{Q}_{X}(-n)^k$ for some $n$ and $k$ by 1.1 d). Thus for any vector bundle $F$ on $S$, there is an exact sequence of vector bundles

$$
0 \longrightarrow F ^ {\prime} \longrightarrow L \longrightarrow F \longrightarrow 0
$$

such that the lemma is true for L by 1.1. Since

$$
0 \longrightarrow F ^ {\prime} (n) \otimes_ {S} N \longrightarrow L (n) \otimes_ {S} N \longrightarrow F (n) \otimes_ {S} N \longrightarrow 0
$$

is exact, we have an exact sequence

$$
R ^ {q} f _ {*} (L (n) \otimes_ {S} N) \longrightarrow R ^ {q} f _ {*} (F (n) \otimes_ {S} N) \longrightarrow R ^ {q + 1} f _ {*} (F ^ {\prime} (n) \otimes_ {S} N)
$$

so part a) can be proved by decreasing induction on q, as in the proof of Serre's theorem [EGA III 2.2.1]. Using a) we have a diagram with exact rows

$$
\begin{array}{c c c c c c c c} & f _ {*} (F ^ {\prime} (n)) \otimes_ {S} N & \longrightarrow & f _ {*} (L (n)) \otimes_ {S} N & \longrightarrow & f _ {*} (F (n)) \otimes_ {S} N & \longrightarrow & 0 \\ & u ^ {\prime} \Big \downarrow & & \Big \downarrow & & u \Big \downarrow \\ 0 & \longrightarrow & f _ {*} (F ^ {\prime} (n) \otimes_ {S} N) & \longrightarrow & f _ {*} (L (n) \otimes_ {S} N) & \longrightarrow & f _ {*} (F (n) \otimes_ {S} N) & \longrightarrow & 0 \end{array}
$$

for $n \geqslant$ some $n_0$ and all $N$. Hence $u$ is surjective; applying this to the vector bundle $F'$, we see that $u'$ is surjective, hence $u$ is bijective for $n \geqslant$ some $n_0$ and all $N$, whence $b$). By a), $f_*(F(n))_{\mathbb{S}^N}$ is exact as a functor of $N$ for sufficiently large $n$, whence using b) we see $f_*(F(n))$ is a flat $O_S$-module. On the other hand, $f_*(F(n))$ is a quotient of $f_*(L(n))$ for $n \geqslant$ some $n_0$, so $f_*(F(n))$ is of finite type. Applying this to $F'$ we see that $f_*(F(n))$ is of finite presentation for all sufficiently large $n$. But a flat module of finite presentation is a vector bundle, whence c).

Lemma 1.13. If F is a vector bundle on X such that  $\mathrm{R}^{\mathrm{q}}\mathrm{f}_{*}(\mathrm{F}(\mathrm{n})) = 0$  for  $q \geqslant 0$ ,  $n \geqslant 0$ , then  $f_{*}(\mathrm{F}(\mathrm{n}))$  is a vector bundle on S for all  $n \geqslant 0$ .

Proof. The assertion being local on S, one can suppose S affine, whence  $f_{*}(F(n))$  is a vector bundle on S for large n by 1.12 c). Consider the exact sequence

$$
0 \longrightarrow F (n) \longrightarrow F (n + 1) \otimes_ {S} E ^ {\vee} \longrightarrow \dots \longrightarrow F (n + r) \otimes_ {S} \wedge^ {r} E ^ {\vee} \longrightarrow 0
$$

obtained by tensoring $F(n)$ with the dual of the sequence 1.5. For $n \geqslant 0$, this is a resolution of the zero module by acyclic modules for the $\delta$-functor $R^q f_*$, hence one knows that on applying $f_*$ one gets an exact sequence

$$
0 \longrightarrow f _ {*} (F (n)) \longrightarrow \dots \longrightarrow f _ {*} (F (n + r)) \otimes_ {S} \Lambda^ {r} E \longrightarrow 0.
$$

Therefore one can show $f_{*}(\mathbb{F}(n))$ is a vector bundle for all $n \geqslant 0$ by decreasing induction on $n$.

Lemma 1.14. If F is a regular vector bundle on X, then  $T_{i}(F)$  is a vector bundle on S for each i.

This follows by induction on i, using the exact sequences 1.8 and the lemma 1.13.

2. The projective bundle theorem. Recall that the K-groups of a scheme are naturally modules over  $K_{0}$  by §3 (1). The following result generalizes [SGA 6 VI 1.1].

Theorem 2.1. Let E be a vector bundle of rank r over a scheme S and X = Proj(SE) the associated projective scheme. If S is quasi-compact, then one has isomorphisms

$$
(K _ {q} S) ^ {r} \xrightarrow {\sim} K _ {q} X, (a _ {i}) _ {0 \leqslant i <   r} \mapsto \sum_ {i = 0} ^ {r - 1} z ^ {i}. f ^ {*} a _ {i}
$$

where $z \in K_{0}X$ is the class of the canonical line bundle $O_{X}(-1)$ and $f: X \to S$ is the structural map.

Proof. Let $\underline{\underline{P}}_n$ denote the full subcategory of $\underline{\underline{P}}(X)$ consisting of vector bundles $F$ such that $R^q f_*(F(k)) = 0$ for $q \neq 0$ and $k \geqslant n$. Let $\underline{\underline{R}}_n$ denote the full subcategory of $\underline{\underline{P}}(X)$ consisting of $F$ such that $F(n)$ is regular. Each of these subcategories is closed under extensions, so its $K$-groups are defined.

Lemma 2.2. For all n, one has isomorphisms: $K_{q}(R) \simeq K_{q}(P) \simeq K_{q}(P(X))$ induced by the inclusions $R = n < P_n < P(X)$.

To prove the lemma, we consider the exact sequence

$$
0 \longrightarrow F \longrightarrow F (1) \otimes_ {S} E \longrightarrow \dots \longrightarrow F (r) \otimes_ {S} \wedge^ {r} E \longrightarrow 0.\tag{2.3}
$$

For each $p > 0$, $F \mapsto F(p)_{S} \wedge^{p} E$ is an exact functor from $P = n$ to $P = n - 1$, hence it induces a homomorphism $u_p: K_q(P) \to K_q(P = n - 1)$. From Th. 2, Cor. 3 it is clear that $\sum_{p > 0} (-1)^{p-1} u_p$ is an inverse to the map induced by the inclusion of $P = n - 1$ in $P = n$. Thus we have $K_q(P = n - 1) \xrightarrow{\sim} K_q(P = n)$ for all $n$. By 1.12 a), $P(X)$ is the union of the $P = n$, so by §2 (9) we have $K_q(P) = n \cong K_q(P(X))$ for all $n$. The proof that $K_q(R) \cong K_q(P(X))$ is similar, whence the lemma.

Put $U_n(N) = \underline{O_k}(-n) \otimes_S N$ for $N$ in $\underline{P}(S)$. For $0 \leq n < r$, $U_n$ is an exact functor from $\underline{P}(S)$ to $\underline{P}_0$ by 1.1 c), hence it induces a homomorphism $u_n: K_q(P(S)) \to K_q(P_0)$. In view of 2.2, it suffices for the proof of the theorem to show that the homomorphism

$$
u: K _ {q} (P (S)) ^ {r} \rightarrow K _ {q} (P) \quad , \quad (a _ {n}) _ {0 \leqslant n <   r} \mapsto \sum_ {n = 0} ^ {r - 1} u _ {n} (a _ {n})
$$

is an isomorphism.

From 1.13 we know that $V_{n}(F) = f_{*}(F(n))$ is an exact functor from $\underline{P}_{=0}$ to $\underline{P}(S)$ for $n \geqslant 0$, hence we have a homomorphism

$$
v: K _ {q} (P) \longrightarrow K _ {q} (P (S)) \quad , \quad x \mapsto (v _ {n} (x)) _ {0 \leqslant n <   r},
$$

where  $v_{n}$  is induced by  $V_{n}$ . Since

$$
V _ {n} U _ {m} (N) = f _ {*} \left(O _ {X} (n - m) \otimes_ {S} N\right) = S _ {n - m} (E) \otimes_ {S} N
$$

by 1.1 c), it follows that the composition vu is described by a triangular matrix with ones on the diagonal, Therefore vu is an isomorphism, so u is injective.

On the other hand,  $T_{n}$  is an exact functor from  $\underline{R}_{0}$  to  $\underline{P(S)}$  by 1.11 and 1.14, hence we have a homomorphism

$$
t: K _ {q} (R) \rightarrow K _ {q} (P (S)) ^ {r}, x \mapsto ((- 1) ^ {n} t _ {n} (x)) _ {0 \leqslant n <   r}
$$

where  $t_{n}$  is induced by  $T_{n}$ . Applying Th. 2, Cor. 3 to the exact sequence 1.11, we see that the composition ut is the map  $K_{q}(R)=0\rightarrow K_{q}(P)=0$  induced by the inclusion of  $R=0$  in  $P=0$ . By 2.2, ut is an isomorphism, so u is surjective, concluding the proof.

3. The projective line over a ring. Let A be a (not necessarily commutative) ring let t be an indeterminate, and let

$$
A [ t ] \xrightarrow {i _ {1}} A [ t, t ^ {- 1} ] \xleftarrow {i _ {2}} A [ t ^ {- 1} ]
$$

denote the canonical homomorphisms. When A is commutative, a quasi-coherent sheaf on  $P_{A}^{1} = \text{Proj}(A[X_{0}, X_{1}])$  may be identified with a triple  $F = (M^{+}, M^{-}, \Theta)$ , where  $M^{+} \in \text{Mod}(A[t])$ ,  $M^{-} \in \text{Mod}(A[t^{-1}])$  and  $\Theta : i_{1}^{*}(M^{+}) \xrightarrow{\sim} i_{2}^{*}(M^{-})$  is an isomorphism of  $A[t, t^{-1}]$ -modules. Following [Bass XII §9], we define  $\text{Mod}(P_{A}^{1})$  for A non-commutative to be the abelian category of such triples, and we define the category of vector bundles on  $P_{A}^{1}$ , denoted  $\underline{P}(P_{A}^{1})$ , to be the full subcategory consisting of triples with  $M^{+} \in \underline{P}(A[t])$ ,  $M^{-} \in \underline{P}(A[t^{-1}])$ .

Theorem 3.1. Let $h_n: P(A) \to P(P_A^1)$ be the exact functor sending $P$ to the triple consisting of $P[t] = A[t] \otimes_A P, P[t^{-1}]$, and multiplication by $t^{-n}$ on $P[t, t^{-1}]$. Then one has isomorphisms

$$
\left(\mathrm{K} _ {\mathrm{q}} \mathrm{A}\right) ^ {2} \quad \xrightarrow {\sim} \quad \mathrm{K} _ {\mathrm{q}} \left(\underset {=} {\mathrm{P}} \left(\mathrm{P} _ {\mathrm{A}} ^ {1}\right)\right) \quad , \quad (\mathrm{x}, \mathrm{y}) \mapsto \left(\mathrm{h} _ {\mathrm{o}}\right) _ {*} (\mathrm{x}) + \left(\mathrm{h} _ {1}\right) _ {*} (\mathrm{y})
$$

and the relations

$$
\left(h _ {n}\right) _ {*} - 2 \left(h _ {n - 1}\right) _ {*} + \left(h _ {n - 2}\right) _ {*} = 0\tag{3.2}
$$

for all n.

When $A$ is commutative, this follows from 2.1, once one notices that $h_n(P)$ is the module $\underline{O}_X(n)\otimes_S P$. For the non-commutative case, one modifies the proof of 2.1 in a straightforward way. For example, if $F = (M^+, M^-, \Theta)$, we put $F(n) = (M^+, M^-, t^{-n} \Theta)$, and let $X_0, X_1: F(n-1) \to F(n)$ be the homomorphisms given by $X_0 = 1$ on $M^+$ and $t^{-1}$ on $M^-$, $X_1 = t$ on $M^+$ and 1 on $M^-$). Then we have an exact sequence

$$
0 \longrightarrow F (n - 2) \xrightarrow {(X _ {1} , - X _ {o})} F (n - 1) ^ {2} \xrightarrow {X _ {o} p r _ {1} + X _ {1} p r _ {2}} F (n) \longrightarrow 0
$$

corresponding to 1.6, which leads to the relations 3.2. Also using the fact that $R^{q}f_{*}$ can be computed by means to the standard open affine covering of $P^{1}$, we can define $R^{q}f_{*}(F)$ in the non-commutative case to be the homology of the complex concentrated in degrees 0, 1 given by the map $d: M^{+} \times M^{-} \longrightarrow i_{2}^{*}(M^{-})$, $d(x,y) = \theta(1 \otimes x) - 1 \otimes y$. One therefore has available all of the tools used in the proof of 2.1 in the non-commutative case; the rest is straightforward checking which will be omitted.

4. Severi-Brauer schemes and Azumaya algebras. Let $S$ be a scheme and let $X$ be a Severi-Brauer scheme over $S$ of relative dimension $r-1$. By definition $X$ is an $S$-scheme locally isomorphic to the projective space $P_S^{r-1}$ for the etale topology on $S$. (see [Grothendieck]), and it is essentially the same thing as an Azumaya algebra of rank $r^2$ over $S$. We propose now to generalize 2.1 to this situation.

When there exists a line bundle $L$ on $X$ which restricts to $O(-1)$ on each geometric fibre, one has $X = PE$, where $E$ is the vector bundle $f_{*}L^{\vee}$ on $S$, $f: X \to S$ being the structural map of $X$. In general such a line bundle $L$ exists only locally for the etale topology on $X$. However, we shall now show that there is a canonical vector bundle of rank $r$ on $X$ which restricts to $O(-1)^{r}$ on each geometric fibre.

Let the group scheme  $GL_{r,S}$  act on  $O_{S}^{r}$  in the standard way, and put  $Y = P_{S}^{r-1} = \text{Proj}(S(\underline{O}_{S}^{r}))$ . The induced action on Y factors through the projective group  $PGL_{r,S} = GL_{r,S}/G_{m,S}$ . Since  $G_{m,S}$  acts trivially on the vector bundle  $\underline{O}_{Y}(-1)\otimes\underline{O}_{S}\otimes\underline{O}_{S}^{r}$ , the group  $PGL_{r,S}$  operates on this vector bundle compatibly with its action on Y. As X is locally isomorphic to Y for the etale topology on S and  $PGL_{r,S}$  is the group of automorphisms of Y over S, one knows that X is the bundle over S with fibre Y associated to a torsor T under  $PGL_{r,S}$  locally trivial for the etale topology. Thus by faithfully flat descent, the bundle  $\underline{O}_{Y}(-1)\otimes\underline{O}_{S}\otimes\underline{O}_{S}^{r}$  on Y gives rise to a vector bundle J on X of rank r.

It is clear that the construction of $J$ is compatible with base change, and that $J = \underline{O}_X(-1) \otimes_S E$ if $X = PE$. In the general case there is a cartesian square

![](images/page_59_image_4.jpg)

where $g$ is faithfully flat (e.g. an etale surjective map over which $T$ becomes trivial) such that $X' = PE$ for some vector bundle $E$ of rank $r$ on $S'$, and further

$$
g ^ {\prime *} (J) = \underset {= X, (- 1)} {O} _ {S}, E.
$$

Let A be the sheaf of (non-commutative)  $\underline{O}_{S}$ -algebras given by

$$
A = f _ {*} (\underline {{\text { End }}} _ {X} (J)) ^ {\text { op }}
$$

where 'op' denotes the opposed ring structure. As $g$ is flat, we have $g^{*}f_{*} = f_{*}'g'^{*}$. Hence we have

$$
g ^ {*} (A) ^ {O P} = f _ {*} ^ {\prime} (\underline {{\text { End }}} _ {X}, (\underline {{O}} _ {X}, (- 1) \otimes_ {S}, E)) = f _ {*} ^ {\prime} (\underline {{O}} _ {X}, \otimes_ {S}, \underline {{\text { End }}} _ {S}, (E)) = \underline {{\text { End }}} _ {S}, (E),
$$

hence A is an Azumaya algebra of rank $r^2$ over S. Moreover one has

$$
f ^ {*} A = \underline {\underline {{\text { End }}}} _ {X} (J) ^ {\mathrm{op}}
$$

as one verifies by pulling back to X'.

Let $J_{n}$ (resp. $A_{n}$) be the n-fold tensor product of J on X (resp. A on S), so that $A_{n}$ is an Azumaya algebra of rank $(r^{n})^{2}$ such that

$$
A _ {n} = f _ {*} \left(\underset {\text {   }} {\text {End}} _ {X} (J _ {n})\right) ^ {\text {op}}, \quad f ^ {*} (A _ {n}) = \underset {\text {   }} {\text {End}} _ {X} (J _ {n}) ^ {\text {op}}.
$$

Let $\underline{P(A_n)}$ denote the category of vector bundles on S which are left modules for $A_n$. Since $J_n$ is a right $f^*(A_n)$-module, which locally on X is a direct summand of $f^*(A_n)$, we have an exact functor

$$
J _ {n} \otimes_ {A _ {n}}?    :    \underline {{P}} (A _ {n})    \longrightarrow    \underline {{P}} (X)    ,    M    \longmapsto    J _ {n} \otimes_ {f ^ {*} (A _ {n})} f ^ {*} (M)    .
$$

and hence an induced map of K-groups.

Theorem 4.1. If S is quasi-compact, one has isomorphisms

$$
\prod_ {n = 0} ^ {r - 1} K _ {i} (A _ {n}) \stackrel {{\sim}} {{\longrightarrow}} K _ {i} (X) \quad , \quad (x _ {n}) \mapsto \sum_ {n = 0} ^ {r - 1} (J _ {n} \otimes_ {A _ {n}}?) _ {*} (x _ {n}).
$$

This is actually a generalization of 2.1 because if two Azumaya algebras A, B represent the same element of the Brauer group of S, then the categories $\underline{\underline{P}}(A)$, $\underline{\underline{P}}(B)$ are equivalent, and hence have isomorphic K-groups. Thus $K_{i}(\underline{\underline{P}}(A_{n})) = K_{i}(S)$ for all n if X is the projective bundle associated to some vector bundle.

The proof of 4.1 is a modification of the proof of 2.1. One defines an X-module F to be regular if its inverse image on $X' = PE$ is regular. For a regular F one constructs a sequence

$$
0 \longrightarrow J _ {r - 1} \otimes_ {A _ {r - 1}} T _ {r - 1} (F) \longrightarrow \dots \longrightarrow O _ {X} \otimes_ {S} T _ {o} (F) \longrightarrow F \longrightarrow 0\tag{4.2}
$$

recursively by

$$
\mathrm{T} _ {\mathrm{n}} (\mathrm{F}) = \mathrm{f} _ {*} \left(\underset {\text {   }} {\text {   }} \left(\underset {\text {   }} {\text {   }} \mathrm{nom} _ {\mathrm{X}} \left(\mathrm{J} _ {\mathrm{n}}, \mathrm{Z} _ {\mathrm{n-1}} (\mathrm{F})\right)\right)\right); \mathrm{Z} _ {\mathrm{n}} (\mathrm{F}) = \operatorname{Ker} \left\{\mathrm{J} _ {\mathrm{n}} \otimes_ {\mathrm{A} _ {\mathrm{n}}} \mathrm{T} _ {\mathrm{n}} (\mathrm{F}) \longrightarrow \mathrm{Z} _ {\mathrm{n-1}} (\mathrm{F}) \right\}
$$

starting with  $Z_{-1}(F) = F$ . It is easy to see this sequence when lifted to  $X'$  coincides the canonical resolution 1.11 for the inverse image of F on  $X'$ . Since  $X'$  is faithfully flat over X, 4.2 is a resolution of F.

We note also that there is a canonical epimorphism $J \to \underline{O_X}$ obtained by descending 1.4, and hence a canonical vector bundle exact sequence

$$
0 \longrightarrow \Lambda^ {r} J \longrightarrow \dots \longrightarrow J \longrightarrow \underset {X} {\circ} \longrightarrow 0
$$

on X corresponding to 1.5. Therefore it should be clear that all of the tools used in the proof of 2.1 are available in the situation under consideration; the rest of the proof of 4.1 will be left to the reader.

Example: Let $X$ be a complete non-singular curve of genus zero over the field $k = H^0(X, \underline{O}_X)$, and suppose $X$ has no rational point. Then $X$ is a Severi-Brauer scheme over $k$ of relative dimension one, and $J$ is the unique indecomposable vector bundle of rank 2 over $X$ with degree -2. The above theorem says

$$
\mathrm{K} _ {\mathbf {i}} (\mathrm{X}) = \mathrm{K} _ {\mathbf {i}} (\mathrm{k}) \oplus \mathrm{K} _ {\mathbf {i}} (\mathrm{A})
$$

where A is the skew-field of endomorphisms of J. This formula in low dimensions has been proved by Leslie Roberts ([Roberts]).

## References

H. Bass: Algebraic K-theory, Benjamin 1968.

S. Bloch:  $K_{2}$  and algebraic cycles, these proceedings.

K. Brown and S. Gersten: Algebraic K-theory as generalized sheaf cohomology, these proceedings.

C. Chevalley: Les classes d'equivalence rationelle I, Exp. 2, Séminaire Chevalley 1958, Anneaux de Chow et applications, Secrétariat mathématique, Paris.

A. Dold and R. Lashof: Principal quasifibrations and fibre homotopy equivalence of bundles, Ill. J. Math. 3 (1959) 285-305.

F. T. Farrell and W. C. Hsiang: A formula for  $K_{1}R_{\alpha}[T]$ , Applications of categorical algebra, Proceedings of symposia in pure mathematics XVIII (1970), Amer. Math. Soc.

E. Friedlander: Fibrations in etale homotopy theory, Publ. Math. I.H.E.S. 42 (1972).

P. Gabriel: Des categories abeliennes, Bull. Math. Soc. France 90 (1962) 323-448.

P. Gabriel and M. Zisman: Calculus of fractions and homotopy theory, Ergebnisse der Mathematik und ihrer Grenzgebiete, Band 35, Springer 1967.

S. Gersten 1: The relation between the K-theory of Karoubi and Villamayor and the K-theory of Quillen (preprint).

---- 2: K-theory of regular schemes, Bull. Amer. Math. Soc. (Jan. 1973).

---- 3: On some exact sequences in the higher K-theory of rings, these proceedings.

---- 4: Problems about higher K-functors, these proceedings.

---- 5: Higher K-theory of rings, these proceedings.

A. Grothendieck: Le groupe de Brauer I, Dix exposés sur la cohomologie des schémas, North-Holland Publ. Co. 1968.

A. Heller: Homological algebra in abelian categories, Ann. of Math. 68 (1958) 484-525.

J. Milnor 1: The realization of a semi-simplicial complex, Ann. of Math. 65 (1957) 357-362.

---- 2: On spaces having the homotopy type of a CW-complex, Trans. Amer. Math. Soc. 90 (1959) 272-280.

D. Mumford: Lectures on curves on an algebraic surface, Annals of Math. Studies 59 (1966).

D. Quillen 1: Higher K-theory for categories with exact sequences, to appear in the proceedings of the June 1972 Oxford symposium "New developments in topology".

---- 2: On the cohomology and K-theory of the general linear groups over a finite field, Ann. of Math. 96 (1972) 552-586.

---- 3: On the endomorphism ring of a simple module over an enveloping algebra, Proc.

Amer. Math. Soc. 21 (1969) 171-172.

L. Roberts: Real quadrics and  $K_{1}$  of a curve of genus zero, Mathematical Preprint No. 1971–60, Queen's University at Kingston.

G. Segal 1: Classifying spaces and spectral sequences, Publ. Math. I.H.E.S. 34 (1968) 105-112.

2: Categories and cohomology theories, preprint, Oxford 1972.

R. G. Swan: Algebraic K-theory, Lecture notes in Math. 76 (1968).

J. Tornehave: On BSG and the symmetric groups (to appear).

EGA: Élements de Géométrie Algébrique, by A. Grothendieck and J. Dieudonné

EGA II: Publ. Math. I.H.E.S. 8 (1961)

EGA III (first part): —— 11 (1961)

EGA IV (third part): ---- 28 (1966).

SGA: Séminaire de Géométrie Algébrique du Bois Marie, by A. Grothendieck and others

SGA 1: Lecture Notes in Math. 224 (1971)

SGA 6: 225 (1971)

SGA 2: Cohomologie locale des faisceaux cohérents et Théorèmes de Lefschetz locaux et globaux, North-Holland Publ. Co. 1968.

Massachusetts Institute of Technology