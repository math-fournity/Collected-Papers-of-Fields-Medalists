FABIEN MOREL
VLADIMIR VOEVODSKY
A$^{1}$-homotopy theory of schemes

Publications mathématiques de l'I.H.É.S., tome 90 (1999), p. 45-143 &lt;http://www.numdam.org/item?id=PMIHES_1999__90__45_0&gt;

© Publications mathématiques de l'I.H.É.S., 1999, tous droits réservés.

L'accès aux archives de la revue « Publications mathématiques de l'I.H.É.S. » (http://www.ihes.fr/IHES/Publications/Publications.html) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

# A$^{1}$-HOMOTOPY THEORY OF SCHEMES by F$_{ABIEN}$ MOREL, V$_{LADIMIR}$ VOEVODSKY

## CONTENTS

1. Preface 45  
2. Homotopy category of a site with interval 45  
2.1. Homotopy theory of simplicial sheaves 46  
2.2. A localization theorem for simplicial sheaves 70  
2.3. Homotopy category of a site with interval 85  
3. The $\mathbf{A}^1$-homotopy category of schemes over a base 94  
3.1. Simplicial sheaves in the Nisnevich topology on smooth sites 95  
3.2. The $\mathbf{A}^1$-homotopy categories 105  
3.3. Some realization functors 119  
4. Classifying spaces of algebraic groups 122  
4.1. Generalities 122  
4.2. Geometrical models for $\mathrm{B_{et}G}$ in $\mathcal{H}(\mathrm{S})$ 133  
4.3. Examples 137

## 1. Preface

In this paper we begin to develop a machinery which we call  $A^{1}$ -homotopy theory of schemes. All our constructions are based on the intuitive feeling that if the category of algebraic varieties is in any way similar to the category of topological spaces then there should exist a homotopy theory of algebraic varieties where affine line plays the role of the unit interval. For a discussion of the main ideas on which our approach is based we refer the reader to [32].

## 2. Homotopy category of a site with interval

In this section we prove a number of general results about simplicial sheaves on sites which will be later applied to our study of the homotopy category of schemes. In the first part (Section 1) we describe the main features of the homotopy theory of simplicial sheaves on a site. Many results of this part can be found in [20] and [17], [18]. Surprisingly, there are some nontrivial things to be proven in relation to basic functoriality of the homotopy categories of simplicial sheaves. This is done in Section 1.

In Section 2 we prove a general theorem which shows that there is a “good” way to invert any set of morphisms in the simplicial homotopy category of a site. Here “good” means that the resulting localized category is again the homotopy category for some model category structure on the category of simplicial sheaves. The results of this

sections remain valid in a more general context of model categories satisfying suitable conditions of being “locally small” but we do not consider this generalizations here.

In Section 3 we apply this localization theorem to define a model category structure on the category of simplicial sheaves on a site with interval (see [31, 2.2]). We show that this model category structure is always proper (in the sense of [2, Definition 1.2]) and give examples of how some known homotopy categories can be obtained using this construction.

All through this section we use freely the standard terminology associated with Quillen's theory of model categories. The notion of a model category which we use here first appeared in [9] and is a little stronger than the one originally proposed by Quillen. To avoid confusion we recall it here.

Definition 0.1. — A category C equipped with three classes of morphisms respectively called weak equivalences, cofibrations and fibrations is called a model category if the following axioms hold :

• MC1 C has all small limits and colimits;

\- MC2 If $f$ and $g$ are two composable morphisms and two of $f$, $g$ or $g \circ f$ are weak equivalences, then so is the third;

\- MC3 If the morphism $f$ is retract of $g$ and $g$ is a weak-equivalence, cofibration or fibration then so is $f$;

\- MC4 Any fibration has the right lifting property with respect to trivial cofibrations (cofibrations which are also weak equivalences) and any trivial fibration (a fibration which is also a weak equivalence) has the right lifting property with respect to cofibrations;

\- MC5 Any morphism $f$ can be functorially (in $f$) factorised as a composition $p \circ i$ where $p$ is a fibration and $i$ a trivial cofibration and as a composition $q \circ j$ where $q$ is a trivial fibration and $j$ a cofibration.

The only differences between these axioms and Quillen's axioms CM1, ..., CM5 of a closed model category are the existence of all small limits and colimits in axiom MC1 instead of just finite limits and colimits, and the existence of functorial factorisations in axiom MC5.

Recall that a site is a category with a Grothendieck topology, see [13, II.1.1.5]. All the sites we consider in this paper are essentially small (equivalent to a small category) and, to simplify the exposition, we always assume they have enough points (see [13]).

## 2.1. Homotopy theory of simplicial sheaves

## Simplicial sheaves

Let T be a site. Denote by  $Shv(T)$  the category of sheaves of sets on T. We shall usually use the same letter to denote an object of T and the associated sheaf

because in our applications the sites we shall consider will have the property that any representable presheaf is a sheaf, in which case the canonical functor  $T \to Shv(T)$  is a fully faithfull embedding. Let  $\Delta^{op}Shv(T)$  be the category of simplicial objects in  $Shv(T)$ ; this category is a topos (cf [13]) and in particular has all small limits and colimits and internal function objects (the latter means that for any simplicial sheaf X the functor  $Y \mapsto Y \times X$  has a right adjoint  $Z \mapsto Hom(\mathcal{X}, Z)$ ).

An object $\mathcal{K}$ of $\Delta^{op}Shv(T)$, i.e. a functor $\Delta^{op} \to Shv(T)$ is determined by a collection of sheaves of sets $\mathcal{K}_n$, $n \geqslant 0$, together with morphisms

$$
\begin{array}{l l l} d _ {i} ^ {n}: \mathcal {X} _ {n} \to \mathcal {X} _ {n - 1} & n \geqslant 1 & i = 0, \dots , n \\ s _ {i} ^ {n}: \mathcal {X} _ {n} \to \mathcal {X} _ {n + 1} & n \geqslant 0 & i = 0, \dots , n \end{array}
$$

called the faces and degeneracies which satisfy the usual simplicial relations ([22]).

To any set E one may assign the corresponding constant sheaf on T which we also denote by E. This correspondence extends to a functor from the category  $\Delta^{op}Sets$  of simplicial sets to  $\Delta^{op}Shv(T)$ . For any simplicial set K the corresponding constant simplicial sheaf is again denoted K.

The cosimplicial object

$$
\begin{array}{c c c} \Delta & \stackrel {{\Delta^ {\bullet}}} {{\to}} & \Delta^ {o p} S h v (\mathbf {T}) \\ \uplus & & \uplus \\ n & \mapsto & \Delta^ {n} \end{array}
$$

defines as usual a structure of simplicial category on  $\Delta^{op}Shv(\mathbf{T})$  (see [26]) with the simplicial function object  $S(-,-)$  given by

$$
\mathrm{S} (\mathcal {K}, \mathcal {Y}) = H o m _ {\Delta^ {o p} S h v (\mathrm{T})} (\mathcal {K} \times \Delta^ {\bullet}, \mathcal {Y}).
$$

Observe that for a simplicial sheaf X and an object U of T the simplicial set S(U, X) is just the simplicial set of sections of X over U.

For any simplicial sheaf $\mathcal{X}$ and any $n \geqslant 0$, let $\mathcal{X}_n^{deg} \subset \mathcal{X}_n$ be the union of the images of all degeneracy morphisms from $\mathcal{X}_{n-1}$ to $\mathcal{X}_n$, i.e.

$$
\mathcal {K} _ {n} ^ {d e g} = \cup_ {i = 0} ^ {n - 1} s _ {i} ^ {n - 1} (\mathcal {K} _ {n - 1}).
$$

For any simplicial sheaf $\mathcal{X}$ and any $n \geqslant 0$, one defines its $n$-th skeleton $sk_n(\mathcal{X}) \subset \mathcal{X}$ as the image of the obvious morphism $\mathcal{X}_n \times \Delta^n \to \mathcal{X}$. We extend this definition to the case $n = -1$ by setting $sk_{-1}(\mathcal{X}) := \emptyset$. For example, $(sk_n\mathcal{X})_{n+1}$ is equal to $\mathcal{X}_{n+1}^{deg}$.

The skeleton functor  $\mathcal{X}\mapsto sk_{n}(\mathcal{X})$  has a right adjoint  $\mathcal{X}\mapsto\cos k_{n}(\mathcal{X})$  which is called the n-th coskeleton functor.

A simplicial sheaf $\mathcal{X}$ is said to be of simplicial dimension $\leqslant n$ if $\mathcal{X}_n\times \Delta^n\to \mathcal{X}$ is an epimorphism, or equivalently if $sk_{n}(\mathcal{X}) = \mathcal{X}$. We will identify sheaves of sets with simplicial sheaves of simplicial dimension zero.

For any  $n \geqslant 0$ , let  $\partial\Delta^{n}$  be the boundary of the n-th standard simplicial simplex. The following straightforward lemma (which can be proven using points of T and the corresponding lemmas for simplicial sets) provides the basis for skeleton induction and will be used in Section 3 below.

Lemma 1.1. — For any monomorphism of simplicial sheaves $f: \mathcal{X} \to \mathcal{Y}$ denote by $sk_{n}(f)$ the union of $f(\mathcal{X})$ and $sk_{n}(\mathcal{Y})$ in $\mathcal{Y}$. Then for any $n \geqslant 0$ the square

$$
\begin{array}{r l r} ((\mathcal {X} _ {n} \amalg_ {\mathcal {X} _ {n} ^ {d e g}} \mathcal {Y} _ {n} ^ {d e g}) \times \Delta^ {n}) \amalg_ {(\mathcal {X} _ {n} \amalg_ {\mathcal {X} _ {n} ^ {d e g}} \mathcal {Y} _ {n} ^ {d e g}) \times \partial \Delta^ {n}} (\mathcal {Y} _ {n} \times \partial \Delta^ {n}) & \longrightarrow & s k _ {n - 1} (f) \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {Y} _ {n} \times \Delta^ {n} & \longrightarrow & s k _ {n} (f) \end{array}
$$

is cocartesian.

## The simplicial model category structure

Recall that a point of a site T is a functor  $x^{*}: Shv(T) \to Sets$  which commutes with finite limits and all colimits.

Definition 1.2. — Let $f: \mathcal{X} \to \mathcal{Y}$ be a morphism of simplicial sheaves.

1. $f$ is called a weak equivalence if for any point $x$ of the site $\mathbf{T}$ the morphism of simplicial sets $x^{*}(f): x^{*}(\mathcal{X}) \to x^{*}(\mathcal{Y})$ is a weak equivalence;

2. $f$ is called a cofibration if it is a monomorphism;

3. $f$ is called a fibration if it has the right lifting property with respect to any cofibration which is a weak equivalence (see [26, I.5] for the definition of the right- (or left-) lifting property).

Denote by  $W_{s}$  (resp. C,  $F_{s}$ ) the class of (simplicial) weak equivalences (resp. cofibration, (simplicial) fibrations).

Remark 1.3. — Let $\mathcal{X}$ be a simplicial sheaf. One defines its $n$-th homotopy sheaf $\Pi_{n}(\mathcal{X})$ as the sheaf of pointed sets over $\mathcal{X}_{0}$ associated to the presheaf $(x_{0}:U\to\mathcal{X}_{0})\mapsto\pi_{n}(\mathcal{X}(U),x_{0})$ (of course, it is a sheaf of groups (resp. abelian groups) over $\mathcal{X}_{0}$ for $n\geqslant1$ (resp. $n\geqslant2$)). A morphism of simplicial sheaves $f:\mathcal{X}\to\mathcal{Y}$ is a weak equivalence if and only if for any $n\geqslant0$ the square

$$
\begin{array}{c c c} \Pi_ {n} (\mathcal {X}) & \longrightarrow & \Pi_ {n} (\mathcal {Y}) \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {X} _ {0} & \longrightarrow & \mathcal {Y} _ {0} \end{array}
$$

is cartesian. Using this fact one can see that f is a weak equivalence if and only if  $x^{*}f$  is a weak equivalences for all x in a conservative set of points of T (see [13] for this notion).

Theorem 1.4. — For any small site T the triple  $(\mathbf{W}_{s}, \mathbf{C}, \mathbf{F}_{s})$  gives the category  $\Delta^{op}Shv(T)$  the structure of a model category.

Proof. — It was shown in [18, Corollary 2.7] that the triple  $(\mathbf{W}_{s}, \mathbf{C}, \mathbf{F}_{s})$  defines a closed model structure on  $\Delta^{op}Shv(T)$  in the sense of Quillen. The proof of existence of factorizations given in [18] shows that they are functorial and therefore the stronger axioms which we use are satisfied.

This model category structure is called the simplicial model category structure on  $\Delta^{op}Shv(\Gamma)$ . In the sequel, if not otherwise stated, we shall always consider the category  $\Delta^{op}Shv(\Gamma)$  endowed with that model category structure. We shall sometimes use the terminology simplicial weak equivalence (resp. fibration, cofibration) if we want to insist that we use this model category structure.

We denote the corresponding homotopy category by  $\mathcal{H}_{s}(\mathrm{T})$ .

Remark 1.5. — The simplicial model category structure on $\Delta^{op}Shv(T)$ is proper (cf [2, Definition 1.2]). This is proven in [19].

By the axiom MC5 of model categories, we know that it is possible to find a functor  $Ex : \Delta^{op}Shv(T) \to \Delta^{op}Shv(T)$  and a natural transformation  $Id \to Ex$  such that for any X the object  $Ex(\mathcal{X})$  is fibrant and the morphism  $\mathcal{X} \to Ex(\mathcal{X})$  is a trivial cofibration.

Definition 1.6. — A resolution functor on a site T is a pair  $(Ex, \theta)$  consisting of a functor  $Ex : \Delta^{op}Shv(T) \to \Delta^{op}Shv(T)$  and a natural transformation  $\theta : Id \to Ex$  such that for any X the object  $Ex(\mathcal{X})$  is fibrant and the morphism  $\mathcal{X} \to Ex(\mathcal{X})$  is a trivial cofibration.

Remark 1.7. — It is not hard to check that the functor which sends a simplicial set to the corresponding constant simplicial sheaf preserves weak equivalences. It gives us for any T an “augmentation” functor $\mathcal{H}_{s}(\Delta^{op}\text{Sets}) \to \mathcal{H}_{s}(\text{T})$. Any point $x$ of T gives a functor $x^{*}: \mathcal{H}_{s}(\text{T}) \to \mathcal{H}_{s}(\Delta^{op}\text{Sets})$ which splits this augmentation functor.

If we consider the category of simplicial sheaves on T as a symmetric monoidal category with respect to the categorical product then it is a closed symmetric monoidal category (cf [21]) because of the existence of internal function objects. In more precise terms, for any pair of objects  $(\mathcal{Y}, \mathcal{Z}) \in (\Delta^{op}Shv(T))^{2}$  the contravariant functor on  $\Delta^{op}Shv(T)$ :

$$
\mathcal {K} \mapsto H o m _ {\Delta^ {o p} S h v (\mathrm{T})} (\mathcal {X} \times \mathcal {Y}, \mathcal {Z})
$$

is representable by an object denoted by  $\underline{\text{Hom}}(\mathcal{Y}, \mathcal{Z})$ , and called the internal function object from Y to Z. The following lemma says that, in the terminology of [16, B.3], the model category structure we consider on  $\Delta^{op}\text{Shv}(\mathbf{T})$  is an enriched model category structure:

Lemma 1.8.

1. For any pair $(i:\mathcal{A}\to \mathcal{B},j:\mathcal{X}\to \mathcal{Y})$ of cofibrations, the obvious morphism

$$
\mathrm{P} (i, j): (\mathcal {A} \times \mathcal {Y}) \amalg_ {\mathcal {A} \times \mathcal {X}} (\mathcal {B} \times \mathcal {X}) \to \mathcal {B} \times \mathcal {Y}
$$

is a cofibration which is trivial if either $i$ or $j$ is.

2. For any pair of morphisms $(i: \mathcal{X} \to \mathcal{Y}, p: \mathcal{E} \to \mathcal{B})$ such that $i$ is a cofibration and $p$ a fibration the obvious morphism

$$
\underline {{{H o m}}} (\mathcal {Y}, \mathcal {E}) \rightarrow \underline {{{H o m}}} (\mathcal {X}, \mathcal {E}) \times_ {\underline {{{H o m}}} (\mathcal {X}, \mathcal {B})} \underline {{{H o m}}} (\mathcal {Y}, \mathcal {B})
$$

is a fibration which is trivial if either $i$ or $p$ is.

3. For any pair of morphisms $(i: \mathcal{X} \to \mathcal{Y}, p: \mathcal{E} \to \mathcal{B})$ such that $i$ is a cofibration and $p$ a fibration the obvious morphism of simplicial sets

$$
\mathrm{S} (\mathcal {Y}, \mathcal {E}) \rightarrow \mathrm{S} (\mathcal {X}, \mathcal {E}) \times_ {\mathrm{S} (\mathcal {X}, \mathcal {B})} \mathrm{S} (\mathcal {Y}, \mathcal {B})
$$

is a Kan fibration which is trivial if either $i$ or $p$ is.

Proof. — It is an easy exercise in adjointness to prove that 1) implies 2) and 3). One proves 1) by reducing to the corresponding lemma in the category of simplicial sets using points of T.

Remark 1.9. — Lemma 1.8 clearly implies that the model category structure on  $\Delta^{op}Shv(\Gamma)$  is a simplicial model category structure : indeed, the third point in this lemma is precisely axiom SM7 of [26, II.2].

Lemma 1.10. — Let $f: \mathcal{X} \to \mathcal{Y}$ be a morphism between fibrant simplicial sheaves. Then the following conditions are equivalent:

1. $f$ is a simplicial homotopy equivalence (i.e. there exists $g: \mathcal{Y} \to \mathcal{X}$ such that $f \circ g$ and $g \circ f$ are simplicially homotopic to identity);

2. $f$ is a weak equivalence;

3. for any object $\mathbf{U} \in \mathbf{T}$ the map of (Kan) simplicial sets:

$$
\mathrm{S} (\mathrm{U}, f): \mathrm{S} (\mathrm{U}, \mathscr {X}) \rightarrow \mathrm{S} (\mathrm{U}, \mathscr {Y})
$$

is a weak equivalence (in fact a homotopy equivalence).

Proof. — The implication  $(2) \Rightarrow (1)$  is standard: one factorizes first f as a trivial cofibration followed by a (trivial) fibration and applies [26, Cor. II.2.5].  $(1) \Rightarrow (3)$  follows easily from the canonical isomorphism  $\mathrm{S}(\mathrm{U}, \underline{\mathrm{Hom}}(\Delta^{1}, \mathcal{X})) \cong \underline{\mathrm{Hom}}(\Delta^{1}, \mathcal{X}(U))$ . To prove  $(3) \Rightarrow (2)$  we note from [13, IV.6.8.2] that any point x of T is associated to a pro-object  $\{U_{\alpha}\}$  of the category T. Then  $x^{*}(f)$  is a filtering colimit of weak equivalences and thus a weak equivalence.

## Local fibrations and resolution lemmas

Besides the classes of cofibrations, fibrations and weak equivalences there is another important class of morphisms  $F_{loc}$  in  $\Delta^{op}Shv(T)$  which is called the class of local fibrations.

Definition 1.11. — A morphism of simplicial sheaves $f: \mathcal{X} \to \mathcal{Y}$ is called a local fibration (resp. trivial local fibration) if for any point $x$ of T the corresponding morphism of simplicial sets $x^{*}(\mathcal{X}) \to x^{*}(\mathcal{Y})$ is a Kan fibration (resp. a Kan fibration and a weak equivalence).

A list of the most important properties of local fibrations can be found in [17]. We will only recall the following result. For simplicial sheaves $\mathcal{X}$, $\mathcal{Y}$ denote by $\pi(\mathcal{X},\mathcal{Y})$ the quotient of $Hom(\mathcal{X},\mathcal{Y}) = S_0(\mathcal{X},\mathcal{Y})$ with respect to the equivalence relation generated by simplicial homotopies, i.e. the set of connected components of the simplicial function object $S(\mathcal{X},\mathcal{Y})$, and call it the set of simplicial homotopy classes of morphisms from $\mathcal{X}$ to $\mathcal{Y}$. One easily checks that the simplicial homotopy relation is compatible with composition and thus one gets a category $\pi\Delta^{op}Shv(T)$ with objects the simplicial sheaves and morphisms the simplicial homotopy classes of morphisms. For any simplicial sheaf $\mathcal{X}$ denote by $\pi Triv/\mathcal{X}$ the category whose objects are the trivial local fibrations to $\mathcal{X}$ and whose morphisms are the obvious commutative triangles in $\pi\Delta^{op}Shv(T)$. From [6, §2] this category is filtering.

Lemma 1.12. — For any simplicial sheaf $\mathcal{X}$, the category $\pi\text{Triv}/\mathcal{X}$ is essentially small, i.e. equivalent to a small one.

Proof. — Let's say that a simplicial sheaf Y is (T, X)-bounded if for each  $n \geqslant 0$  and each  $U \in T$  the cardinal of the set  $\mathcal{Y}_{n}(U)$  is less than or equal to that of  $Sup_{V \in T, m \in N} \# \mathcal{X}_{m}(V)$ . The full subcategory of (T, X)-bounded simplicial sheaves is clearly essentially small. Thus to prove the lemma it suffices to prove that for any trivial local fibration  $f: Y \to X$  there is a (T, X)-bounded simplicial sheaf  $Y'$  and a morphism  $g: Y' \to Y$  such that  $f \circ g$  is a trivial local fibration. This fact is proven as follows. Let  $n \geqslant 1$  and  $Z \subset Y$  a sub-simplicial sheaf which is (T, X)-bounded and such that for each  $i \in \{0, ..., n-1\}$  the morphism of sheaves:

$$
\mathcal {Z} _ {i} \rightarrow \underline {{H o m}} (\partial \Delta^ {i}, \mathcal {Z}) _ {0} \times_ {\underline {{H o m}} (\partial \Delta^ {i}, \mathcal {X}) _ {0}} \mathcal {K} _ {i}
$$

is an epimorphism (observe that $\mathcal{Z} \to \mathcal{X}$ is a trivial local fibration exactly when one has this property for any $i \geqslant 0$). Now there is an $(T, \mathcal{X})$-bounded subsheaf $S_n \subset \mathcal{Y}_n$ whose image by the morphism

$$
\mathcal {Y} _ {n} \rightarrow \underline {{{H o m}}} (\partial \Delta^ {n}, \mathcal {Y}) _ {0} \times_ {\underline {{{H o m}}} (\partial \Delta^ {n}, \mathcal {X}) _ {0}} \mathcal {X} _ {0}
$$

is  $\underline{Hom}(\partial\Delta^{n},\mathcal{Z})_{0}\times_{\underline{Hom}(\partial\Delta^{n},\mathcal{X})_{0}}\mathcal{X}_{n}$ : this follows easily from the fact that the latter sheaf is  $(\mathrm{T},\mathcal{X})$ -bounded (observe it is a subsheaf of  $(\mathcal{Z}_{n-1})^{n}\times\mathcal{X}_{n}$ ). Call  $Z'$  the sub-simplicial sheaf of Y generated by Z and  $S_{n}$ . It is clear that  $Z'$  is  $(\mathrm{T},\mathcal{X})$ -bounded and has the same property as Z up to i=n. By induction we get the result.

Proposition 1.13. — For any simplicial sheaves $\mathcal{X}$, $\mathcal{Y}$, with $\mathcal{Y}$ locally fibrant, the canonical map:

$$
\operatorname{colim} _ {p: \mathcal {X} ^ {\prime} \rightarrow \mathcal {X} \in \pi T r i v / \mathcal {X}} \pi (\mathcal {X} ^ {\prime}, \mathcal {Y}) \rightarrow H o m _ {\mathcal {H} _ {s} (T)} (\mathcal {X}, \mathcal {Y})
$$

is a bijection.

For the proof see [6, §2] for sheaves on topological spaces and [18, p. 55] in the general case.

Remark 1.14. — One of the corollaries of Proposition 1.13 is the fact that for any pair  $(X,Y)$  of sheaves of simplicial dimension zero the map

$$
H o m _ {S h v (\mathrm{T})} (\mathrm{X}, \mathrm{Y}) \rightarrow H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathrm{X}, \mathrm{Y})
$$

is bijective. In other words, the obvious functor $Shv(\mathbf{T}) \to \mathcal{H}_s(\mathbf{T})$ is a full embedding.

An important class of local fibrations can be obtained as follows. Let $f: \mathbf{X} \to \mathbf{Y}$ be a morphism of sheaves of sets. Denote by $\check{\mathbf{C}}(f)$ the simplicial sheaf such that

$$
\check {\mathrm{C}} (f) _ {n} = \mathbf {X} _ {\mathrm{Y}} ^ {n + 1}
$$

and faces and degeneracy morphisms are given by partial projections and diagonals respectively. Then f factors through an obvious morphism  $\check{\mathrm{C}}(f) \to \mathrm{Y}$  which we denote  $p_{f}$ .

Lemma 1.15. — The morphism $p_f$ is a local fibration. It is a trivial local fibration if and only if $f$ is an epimorphism.

Proof. — Since T has enough points, it is sufficient to prove the lemma for T the category of sets in which case it is obvious.

The following two “resolution lemmas” will be used below to replace simplicial sheaves by weakly equivalent simplicial sheaves of a given type.

Lemma 1.16. — Let S be a set of objects in  $Shv(T)$  such that for any U in T there exists an epimorphism  $F \to U$  with F being a sum of elements in S. Then there exists a functor  $\Phi_{\mathcal{S}} : \Delta^{op}Shv(T) \to \Delta^{op}Shv(T)$  and a natural transformation  $\Phi_{\mathcal{S}} \to Id$  such that for any Y one has

1. for any $n \geqslant 0$ the sheaf of sets $\Phi_{\mathcal{S}}(\mathcal{Y})_n$ is a direct sum of sheaves in $\mathcal{S}$

2. the morphism $\Phi_{\mathcal{S}}(\mathcal{Y})\to \mathcal{Y}$ is a trivial local fibration.

Proof. — For a morphism $f \colon \mathcal{K} \to \mathcal{Y}$ define $\Phi_{\mathcal{S}}^{1}(f)$ by the cocartesian square

$$
\begin{array}{c c c} \coprod \mathrm{F} \times \partial \Delta^ {n} & \longrightarrow & \mathcal {X} \\ \Big \downarrow & & \Big \downarrow \\ \coprod \mathrm{F} \times \Delta^ {n} & \longrightarrow & \Phi_ {\mathcal {S}} ^ {1} (f) \end{array}
$$

where the coproduct is taken over the set of all commutative squares of the form

$$
\begin{array}{c c c} \mathrm{F} \times \partial \Delta^ {n} & \longrightarrow & \mathcal {X} \\ \Big \downarrow & & \Big \downarrow_ {f} \\ \mathrm{F} \times \Delta^ {n} & \longrightarrow & \mathcal {Y} \end{array}
$$

with $n \geqslant 0$ and $F$ in $\mathcal{S}$. Let $\Phi_{\mathcal{S}}^{1}(f)$ be the canonical morphism $\Phi_{\mathcal{S}}^{1}(f) \to \mathcal{Y}$. Set $\Phi_{\mathcal{E}}^{m+1}(f)$ to be $\Phi_{\mathcal{S}}^{1}(\Phi_{\mathcal{S}}^{m}(f))$ and let $\Phi_{\mathcal{E}}^{m+1}(f)$ be the corresponding morphism $\Phi_{\mathcal{S}}^{m+1}(f) \to \mathcal{Y}$. We get a sequence of simplicial sheaves $\Phi_{\mathcal{E}}^{i}(f)$ and monomorphisms $\Phi_{\mathcal{S}}^{i}(f) \to \Phi_{\mathcal{S}}^{i+1}(f)$ and we set $\Phi_{\mathcal{S}}(f)$ to be the colimit of this sequence. This construction gives a functorial decomposition of any morphism $f$ of the form $\mathcal{X} \to \Phi_{\mathcal{S}}(f) \to \mathcal{Y}$.

One verifies easily that the functor $\mathcal{Y} \mapsto \Phi_{\mathcal{S}}(\emptyset \to \mathcal{Y})$ satisfies the conditions of the lemma by using the fact ([13, IV.6.8] that any point $x$ of $T$ is associated to a pro-object $\{F_{\alpha}\}$ with each $F_{\alpha} \in \mathcal{S}$.

Remark 1.17. — Lemma 1.16 applied to the class of representable sheaves shows, using Lemma 1.1, that the smallest full subcategory of  $\mathcal{H}_{s}(\mathrm{T})$  which contains all representable sheaves and which is closed under isomorphisms, homotopy cofiber and direct sums is  $\mathcal{H}_{s}(\mathrm{T})$  itself.

Lemma 1.18. — Let $\mathcal{X}$ be a simplicial sheaf and $p_0: \mathcal{X}'_0 \to \mathcal{X}_0$ be an epimorphism of sheaves. Then there exists a trivial local fibration $p: \mathcal{X}' \to \mathcal{X}$ such that $p_0$ is the zero component of $p$.

Proof. — Consider  $p_{0}$  as a morphism of simplicial sheaves  $X_{0}^{\prime} \to X$ . Then construct its decomposition in the same way as in the proof of Lemma 1.16 using the inclusions  $U \times \partial\Delta^{n} \to U \times \Delta^{n}$  with U running through all objects of T and n being strictly greater than zero.

## Homotopy limits and colimits

Let $\mathcal{T}$ be a small category. For any functor $\mathcal{K}:\mathcal{T}\to\Delta^{op}Shv(\mathrm{T})$ we may define by the usual formulas (cf [3, XI.4.5, XII.3.7]) its homotopy limit and its homotopy colimit which gives us functors

$$
h o l i m _ {\mathcal {I}}: \Delta^ {o p} S h v (\mathrm{T}) ^ {\mathcal {I}} \rightarrow \Delta^ {o p} S h v (\mathrm{T})
$$

$$
h o c o l i m _ {\mathcal {T}}: \Delta^ {o p} S h v (\mathrm{T}) ^ {\mathcal {T}} \to \Delta^ {o p} S h v (\mathrm{T})
$$

where  $holim_{T}K$  is the sheaf of the form

$$
\mathbf {U} \mapsto h o l i m _ {\mathcal {I}} (\mathcal {K} (\mathbf {U}))
$$

and  $hocolim_{\mathcal{F}}K$  is the sheaf associated with the presheaf of the form

$$
\mathrm{U} \mapsto h o c o l i m _ {\mathcal {T}} (\mathscr {K} (\mathrm{U})).
$$

Lemma 1.19. — For any functor $\mathcal{X}:\mathcal{T}\to\Delta^{op}\mathrm{Shv}(\mathrm{T})$ and any simplicial sheaf $\mathcal{Y}$, there is a canonical isomorphism

$$
\underline {{H o m}} (h o c o l i m _ {\mathcal {I}} \mathcal {K}, \mathcal {Y}) \cong h o l i m _ {\mathcal {T} o p} \underline {{H o m}} (\mathcal {K}, \mathcal {Y}),
$$

and in particular there's a canonical isomorphism of simplicial sets

$$
\mathrm{S} (h o c o l i m _ {\mathcal {I}} \mathcal {K}, \mathcal {Y}) \cong h o l i m _ {\mathcal {T} o p} \mathrm{S} (\mathcal {K}, \mathcal {Y}).
$$

Similarly, there are canonical isomorphisms

$$
\underline {{H o m}} (\mathcal {Y}, h o l i m _ {\mathcal {I}} \mathcal {K}) \cong h o l i m _ {\mathcal {I}} \underline {{H o m}} (\mathcal {Y}, \mathcal {K}),
$$

and

$$
\mathrm{S} (\mathcal {Y}, \operatorname{holim} _ {\mathcal {T}} \mathcal {K}) \cong \operatorname{holim} _ {\mathcal {T}} \mathrm{S} (\mathcal {Y}, \mathcal {K}).
$$

Lemma 1.20. — For any functor $\mathcal{X}:\mathcal{T}\to\Delta^{op}\mathrm{Shv}(\mathrm{T})$ and any point $x$ of $\mathrm{T}$, the simplicial set $x^{*}(\mathrm{hocolim}_{\mathcal{T}}\mathcal{X})$ is canonically isomorphic to the simplicial set $\mathrm{hocolim}_{\mathcal{T}}x^{*}(\mathcal{X})$. If $\mathcal{T}$ is a finite category the same holds for $\mathrm{holim}_{\mathcal{T}}$.

Corollary 1.21. — Let $\mathcal{X}$, $\mathcal{Y}$ be functors $\mathcal{T} \to \Delta^{op} Shv(T)$ and $f$ a natural transformation $\mathcal{X} \to \mathcal{Y}$. Then:

1. if for any  $i \in T$  the morphism  $f(i)$  is a cofibration (resp. a weak equivalence) then the morphism  $\operatorname{hocolim}_{\mathcal{T}}(f)$  is cofibration (resp. a weak equivalence);

2. if $\mathcal{T}$ is a right filtering category (cf [3, XII.3.5]), then the obvious morphism:

$$
h o c o l i m _ {\mathcal {I}} \mathcal {K} \rightarrow c o l i m _ {\mathcal {I}} \mathcal {K}
$$

is a weak equivalence.

Proof. — The first point and the third one are easy corollaries of Lemma 1.20 and [3, XII, 3.5, 4.2, 5.2]. The second point is an easy exercise in adjointness using Lemmas 1.19, 1.10 and [3, XI, 5.5, 5.6].

Proposition 1.22. — Let $\mathcal{X}$, $\mathcal{Y}$ be functors $\mathcal{T} \to \Delta^{op}Shv(T)$ and $f$ a natural transformation $\mathcal{X} \to \mathcal{Y}$ such that all the simplicial sheaves $\mathcal{X}(i)$, $\mathcal{Y}(i)$ are pointwise fibrant and the morphisms $f(i)$ are fibrations. Then $holim(f)$ is a fibration. In particular if all the sheaves $\mathcal{X}(i)$ are fibrant then $holim_{\mathcal{T}}\mathcal{X}$ is fibrant.

Proof. — Follows from [22, XI, 5.5, 5.6], Lemma 1.8(3) and the obvious fact that $\mathcal{S}(-, \text{holim}_{\mathcal{T}} -) = \text{holim}_{\mathcal{T}} \mathcal{S}(-, -)$.

Unlike the theory of homotopy colimits the theory of homotopy limits for simplicial sheaves on sites is different from the corresponding theory for simplicial sets because the analog of Lemma 1.20 does not hold for infinite homotopy limits. As a result holim functor may not preserve weak equivalences even between systems of pointwise fibrant objects unless the objects are actually fibrant. An example of such a situation for an infinite product is given below. A more sophisticated example is given in 1.30.

Example 1.23. — Let T be a site with precanonical topology i.e. such that any representable presheaf is a sheaf. Assume that there exists a family of coverings  $p_{i}: U_{i} \to pt$  of the final object of T such that for any U in T the intersection of images of  $Hom(U, U_{i})$  in  $pt = Hom(U, pt)$  is empty (such a family can be found for example in the site associated with any profinite group which is not finite). Consider the simplicial sheaves  $\mathcal{X}_{i} = \check{\mathrm{C}}(U_{i} \to pt)$  (see definition prior to Lemma 1.15) and let Ex be a resolution functor on  $\Delta^{op}Shv(T)$ . We claim that the canonical morphism  $\prod X_{i} \to \prod ExX_{i}$  is not a weak equivalence. Indeed, by Lemma 1.15 each of  $X_{i}$ 's is weakly equivalent to the final object and therefore  $\prod ExX_{i}$  is weakly equivalent to the final object as well. On the other hand our condition on  $U_{i}$ 's implies that the product  $\prod X_{i}$  is empty.

## Eilenberg-MacLane sheaves and Postnikov towers

In this section we give a reformulation of the main results of  $[22, Ch. V]$  for the case of simplicial sheaves. In this context there are two noticeable differences between simplicial sheaves and simplicial sets. The first is that the weak homotopy type of a simplicial sheaf can not be recovered from the weak homotopy type of its Postnikoff tower unless some finitness assumptions are used (Example 1.30). The second is that a simplicial abelian group object is not necessarily weakly equivalent to the product of Eilenberg-MacLane objects corresponding to its homotopy groups (Theorem 1.34).

We adopt the following convention concerning complexes with values in an abelian category A: a chain complex  $C_{*}$  is one whose differential has degree -1 and a cochain complex  $C^{*}$  is whose differential has degree +1. If  $C_{*}$  is a chain complex, we shall denote  $C^{*}$  its associated cochain complex with  $C^{n} := C^{-n}$ .

For a sheaf of simplicial abelian groups $\mathcal{G}$ on $\mathrm{T}$ denote by $\underline{\pi}_i(\mathcal{G})$ the presheaf of the form $\mathrm{U} \mapsto \pi_i(\mathcal{G}(\mathrm{U}), 0)$. Similarly, for a chain complex of sheaves of abelian groups $\mathrm{C}_*$ denote by $\underline{\mathrm{H}}_i(\mathrm{C}_*)$ the presheaf $\mathrm{U} \mapsto \mathrm{H}_i(\mathrm{C}_*(\mathrm{U}))$.

Let $\mathrm{N}(\mathcal{G})$ be the chain complex of sheaves of abelian groups on T obtained from a simplicial abelian group G by applying the functor of the normalized complex (see [22, p. 93]) pointwise. Then we have $\underline{\pi}_{i}(\mathcal{G}) = \underline{\mathrm{H}}_{i}(\mathrm{N}(\mathcal{G}))$. The functor N has a right adjoint $\Gamma$ ([22, p. 95]) and we get the following result ([22, Th. 22.4]).

Proposition 1.24. — (N, $\Gamma$) is a pair of mutually inverse equivalences between the category of complexes of sheaves of abelian groups A with $A_i = 0$ for $i < 0$ and the category of sheaves of simplicial abelian groups.

Remark 1.25. — For a complex A which does not satisfy the condition  $A_{i}=0$  for i<0 the composition  $N\circ\Gamma$  maps A to the truncation of A of the form  $\mathbf{N}\circ\Gamma(\mathbf{A})_{i}=\mathbf{A}_{i}$  for i>0,  $\mathbf{N}\circ\Gamma(\mathbf{A})_{0}=ker(d_{0}:\mathbf{A}_{0}\to\mathbf{A}_{-1})$  and  $\mathbf{N}\circ\Gamma(\mathbf{A})_{i}=0$  for i<0.

One defines the Eilenberg-MacLane objects associated with a sheaf of abelian groups A as  $\mathrm{K}(\mathrm{A}, n) = \Gamma(\mathrm{A}[n])$  where  $A[n]$  is the chain complex of sheaves with the only nontrivial term being A in dimension n.

Denote the category of chain complexes of sheaves of abelian groups on T by  $Compl(AbShv(T))$ . Recall that a morphism of cochain complexes  $f: C_{*}^{\prime} \to C_{*}$  is called a quasi-isomorphism if the corresponding morphisms of homology sheaves  $a\underline{H}_{i}(C_{*}^{\prime}) \to a\underline{H}_{i}(C_{*})$  are isomorphisms for all  $i \in Z$ . The localization of the category  $Compl(AbShv(T))$  with respect to quasi-isomorphisms is called the derived category of chain complexes of sheaves on T and denoted by  $D(AbShv(T))$ .

For any chain complex of sheaves  $C_{*}$  let  $\pi Triv/C_{*}$  be the category whose objects are epimorphisms of complexes  $C_{*}^{\prime} \rightarrow C_{*}$  which are quasi-isomorphisms and whose morphisms are the obvious homotopy commutative triangles of complexes. The same method as the one used in the proof of Lemma 1.12 shows that  $\pi Triv/C$  is a (left) filtering category, essentially small. This implies that the derived category  $D(AbShv(T))$  obtained from  $Comp(AbShv(T))$  by inverting all the quasi-isomorphisms is indeed a category, in which the set of morphisms from  $C_{*}$  to  $D_{*}$  is given by the colimit:

$$
\operatorname{colim} _ {(p: \mathrm{C} _ {*} ^ {\prime} \rightarrow \mathrm{C} _ {*}) \in \pi T r i v / \mathrm{C} _ {*}} \pi (\mathrm{C} _ {*} ^ {\prime}, \mathrm{D} _ {*})
$$

where  $\pi(-,-)$  denotes the set of homotopy classes of morphisms of chain complexes. Recall that the hypercohomology  $\mathbf{H}^{*}(\mathbf{U},\mathbf{C}^{*})$  of an object U of T with coefficients in a cochain complex of sheaves  $C^{*}$  is the graded group of morphisms  $\operatorname{Hom}(\mathbf{Z},\mathbf{C}_{*})$

in the derived category of (chain) complexes of sheaves on T. The following almost tautological result provides an interpretation of hypercohomology groups in terms of simplicial sheaves (for a proof see [6, §3 Theorem 2]).

Proposition 1.26. — Let  $C^{*}$  be a cochain complex of sheaves of abelian groups on T. Then for any integer n and any object U of T one has a canonical isomorphism  $\mathbf{H}^{n}(\mathbf{U},\mathbf{C}^{*})=Hom_{\mathcal{H}_{s}}(\mathbf{U},\Gamma(\mathbf{C}_{*}[n]))$ . In particular if  $C^{*}=A$  is a sheaf of abelian groups we have  $\mathrm{H}^{n}(\mathrm{U},\mathrm{A})=Hom_{\mathcal{H}_{s}}(\mathrm{U},\mathrm{K}(\mathrm{A},n))$ .

For a simplicial sheaf $\mathcal{X}$ denote by $\mathrm{P}^{(n)}(\mathcal{X})$ the simplicial sheaf associated with the presheaf $\mathrm{U} \mapsto (\mathcal{X}(\mathrm{U}))^{(n)}$ where $\mathrm{K} \mapsto \mathrm{K}^{(n)} = Im(\mathrm{K} \to \cos k_n(\mathrm{K}))$ is the functor on simplicial sets defined in [22, p. 32]. The following result is a direct corollary of [22, 8.2, 8.4].

Proposition 1.27. — Let $\mathcal{K}$ be a locally fibrant simplicial sheaf. Then the sheaves $\mathrm{P}^{(n)}\mathcal{K}$ are locally fibrant and the morphisms

$$
\mathcal {K} \rightarrow \mathrm{P} ^ {(n)} \mathcal {K}
$$

$$
\mathrm{P} ^ {(n + 1)} \mathcal {X} \rightarrow \mathrm{P} ^ {(n)} \mathcal {X}
$$

are local fibrations.

If $f: \mathcal{X} \to \mathcal{Y}$ is a weak equivalence of locally fibrant simplicial sheaves then for any $n \geqslant 0$ the morphism $\mathrm{P}^{(n)}(f)$ is a weak equivalence.

Remark 1.28. — Let $\mathcal{X}$ be a pointwise fibrant simplicial sheaf i.e. a simplicial sheaf such that for any U in T the simplicial set $\mathcal{X}(\mathrm{U})$ is a Kan complex. Then the simplicial sheaf $\mathrm{P}^{(n)}\mathcal{X}$ is pointwise fibrant. For any U and T and a point $x \in \mathcal{X}(\mathrm{U})$ one has

$$
\begin{array}{l l} \pi_ {i} (\mathrm{P} ^ {(n)} \mathcal {K} (\mathrm{U}), x) = \pi_ {i} (\mathcal {K} (\mathrm{U}), x) & \text {for} i <   n \\ \pi_ {i} (\mathrm{P} ^ {(n)} \mathcal {K} (\mathrm{U}), x) = c o l i m _ {\mathcal {U} \to \mathrm{U}} I m (\pi_ {i} (\mathcal {K} (\mathrm{U}), x) \to \pi_ {i} (\mathcal {K} (\mathcal {U}), x)) & \text {for} i = n \\ \pi_ {i} (\mathrm{P} ^ {(n)} \mathcal {K} (\mathrm{U}), x) = 0 & \text {for} i > n \end{array}
$$

where the colimit in the middle row is taken over all coverings $\mathcal{U} = \{\mathrm{U}_j\to \mathrm{U}\}$ of U and $\pi_i(\mathcal{X}(\mathcal{U}),x) = \prod_j\pi_i(\mathcal{X}(\mathrm{U}_j),x)$.

Definition 1.29. — The tower of local fibrations  $(\mathbf{P}^{(n)}\mathcal{X}, \mathbf{P}^{(n+1)}\mathcal{X} \to \mathbf{P}^{(n)}\mathcal{X})$  associated to a locally fibrant simplicial sheaf K is called the Postnikov tower of K.

Functors  $\mathbf{P}^{(n)}$  do not take fibrant simplicial sheaves to fibrant simplicial sheaves. As a result of this fact the homotopy limit  $\operatorname{holim}_{n\geq0}Ex(\mathbf{P}^{(n)}\mathcal{X})$  of the tower of fibrant objects associated to the Postnikov tower of X is not in general weakly equivalent to X as shown in the following example.

Example 1.30. — Let T be the site of finite G-sets where  $G = \prod_{\infty} Z/2$  is the product of infinitely many copies of Z/2. Consider the constant simplicial sheaf X on T which corresponds to the product of Eilenberg-MacLane spaces of the form  $\prod_{i>0} K(Z/2, i)$  (it is also the product of the corresponding Eilenberg-MacLane sheaves in the category of sheaves). Then  $P^{(n)}X$  is weakly equivalent to  $\prod_{n \geqslant i > 0} K(Z/2, i)$  and one can easily see that for any resolution functor Ex the homotopy limit  $holim_{n \geqslant 0} Ex(P^{(n)}X)$  is weakly equivalent to  $\widetilde{X} = \prod_{i > 0} Ex(K(Z/2, i))$ . We claim that the sheaf associated to the presheaf  $U \mapsto \pi_0(\widetilde{X}(U))$  is nontrivial while the corresponding sheaf for X is clearly trivial. By Proposition 1.26 we have for any U in T

$$
\pi_ {0} (\widetilde {\mathcal {K}} (\mathbf {U})) = \prod_ {i > 0} \mathrm{H} ^ {i} (\mathbf {U}, \mathbf {Z} / 2)
$$

Let $\tau$ be the generator of $\mathrm{H}^1 (\mathbf{Z} / 2,\mathbf{Z} / 2)$ and $p_i:\mathbf{G}\to \mathbf{Z} / 2$ the projection to the i-th multiple. Consider the element $\alpha = \prod p_i^* (\tau^{\wedge i})$ in $\pi_0(\widetilde{\mathcal{X}} (pt))$. This element does not become zero on any covering of the point and therefore gives a nontrivial element in the sections of the sheaf associated to $\mathbf{U}\mapsto \pi_0(\widetilde{\mathcal{X}} (\mathbf{U}))$.

Definition 1.31. — A site T is called a site of finite type if for any simplicial sheaf $\mathcal{X}$ on T the canonical morphism $\mathcal{X} \to \operatorname{holim}_{n \geqslant 0} Ex(\mathrm{P}^{(n)}\mathcal{X})$ is a weak equivalence.

Our next goal is to show that any site satisfying a fairly weak finiteness condition on cohomological dimension is a site of finite type in the sense of Definition 1.31. In order to do it we will need a description of simplicial sheaves with only one nontrivial “homotopy group” which is also of independent interest.

Definition 1.32. — Let $\mathcal{K}$ be a simplicial sheaf. We say that $\mathcal{K}$ has only nontrivial homotopy in dimension $d \geqslant 0$ if the following condition holds:

1. for any U in T, any  $x \in \mathcal{X}(U)$  and any  $n \geqslant 0$ ,  $n \neq d$  the sheaf of sets on T/U associated with the presheaf V/U  $\mapsto \pi_{n}(\mathcal{X}(V), x)$  is isomorphic to the point.

We say that $\mathcal{K}$ has only one nontrivial abelian homotopy group in dimension $d \geqslant 1$ if it has only nontrivial homotopy in dimension $d$ and for any U in T and any $x \in \mathcal{K}(\mathrm{U})$ the sheaf of groups on T/U associated with the presheaf V/U $\mapsto \pi_d(\mathcal{K}(\mathrm{V}), x)$ is abelian (this condition is of course only meaningful for $d = 1$).

The forgetful functor from the category of sheaves of simplicial abelian groups on T to the category of simplicial sheaves (of sets) on T has a left adjoint which we call the functor of free abelian group and denote by  $\mathbf{Z}:\Delta^{op}Shv(\mathrm{T})\to\Delta^{op}AbShv(\mathrm{T})$ . For any simplicial sheaf X the sheaf of simplicial abelian groups  $\mathbf{Z}(\mathcal{X})$  is the sheaf associated with the presheaf  $\mathrm{U}\mapsto\mathbf{Z}(\mathcal{X}(\mathrm{U}))$  where  $\mathbf{Z}(\mathcal{X}(\mathrm{U}))$  is the free abelian group generated by the simplicial set  $\mathcal{X}(\mathrm{U})$  (in [22] the functor Z is denoted by  $C:K\mapsto C(K)$ ).

Proposition 1.33. — Let $\mathcal{X}$ be a simplicial sheaf which has only one nontrivial abelian homotopy group in dimension $d \geqslant 1$. Denote by $\mathcal{E}(\mathcal{X})$ the fiber product

![](images/page_15_image_1.jpg)

Then the obvious morphism $\mathcal{X} \to \mathcal{E}(\mathcal{X})$ is a weak equivalence.

Proof. — For any point x of T one has  $x^{*}(\mathrm{P}^{(d)}(\mathbf{Z}(\mathcal{X}))) = (\mathrm{C}(x^{*}\mathcal{X}))^{n}$  (where the right hand side is written in the notations of [22, Def. 8.1]) which shows that it is enough to prove the proposition in the case of simplicial sets. For any simplicial set K the homotopy groups of the simplicial abelian group  $\mathrm{C}(\mathbf{K})$  are the homology groups of K and by our assumption on X, Hurewicz Theorems ([22, Th. §13]) and the main property of functors  $K \mapsto K^{n}$  ([22, Th. 8.4]) we conclude that  $(\mathrm{C}(x^{*}\mathcal{X}))^{n} \cong x^{*}\mathcal{X} \times \mathbf{Z}$  which implies the statement of the proposition.

For $\mathcal{X}$ satisfying the conditions of Definition 1.32 (2) we define a sheaf $a\underline{\pi}_d(\mathcal{X})$ as the sheaf associated with the presheaf $\mathrm{U} \mapsto \mathrm{H}_d(\mathcal{X}(\mathrm{U}); \mathbf{Z})$. Using Hurewicz Theorems ([22, Th. §13]) one can verify immediately that for any $\mathrm{U}$ in $\mathrm{T}$ such that $\mathcal{X}(\mathrm{U})$ is not empty and any $x \in \mathcal{X}(\mathrm{U})_0$ there is a canonical isomorphism between $a\underline{\pi}_d(\mathcal{X})_{\mathrm{T/U}}$ and the sheaf on $\mathrm{T/U}$ associated with the presheaf $\mathrm{V} \mapsto \pi_d(\mathcal{X}(\mathrm{V}), x)$.

The simplicial sheaf $\mathrm{P}^{(d)}(\mathbf{Z}(\mathcal{X}))$ has a canonical structure of a sheaf of simplicial abelian groups, the morphism $\mathrm{P}^{(d)}(\mathbf{Z}(\mathcal{X}))\to \mathbf{Z}$ is a surjective homomorphism and its kernel is canonically weakly equivalent to $\Gamma (a\underline{\pi}_d(\mathcal{X})[d])$. Thus the complex of sheaves $\mathrm{N}(\mathrm{P}^{(d)}(\mathbf{Z}(\mathcal{X})))$ has two nontrivial homology groups namely $a\underline{\mathrm{H}}_0 = \mathbf{Z}$ and $a\underline{\mathrm{H}}_d = a\underline{\pi}_d(\mathcal{X})$. Therefore it defines a morphism in the derived category of complexes of sheaves on T of the form $\mathbf{Z}\rightarrow a\underline{\pi}_d(\mathcal{X})[d + 1]$ and the projection $\mathrm{P}^{(d)}(\mathbf{Z}(\mathcal{X}))\to \mathbf{Z}$ splits if and only if this morphism is zero. Combining these observations we get the following result.

Theorem 1.34. — Let $\mathcal{X}$ be a simplicial sheaf whose only nontrivial homotopy group $a\underline{\pi}_d(\mathcal{X})$ is abelian and lies in dimension $d \geqslant 1$. Any such $\mathcal{X}$ defines a cohomology class $\eta_{\mathcal{X}} \in \mathrm{H}^{d+1}(\mathrm{T}, a\underline{\pi}_d(\mathcal{X}))$ and the pair $(a\underline{\pi}_d(\mathcal{X}), \eta_{\mathcal{X}})$ determines $\mathcal{X}$ up to a weak equivalence. If in addition $\mathcal{X}$ is fibrant then

$$
\pi_ {0} (\mathcal {X} (\mathrm{U})) = \left\{ \begin{array}{l l} \emptyset & \text {if the restriction of} \eta_ {\mathcal {X}} \text {to U is not zero} \\ \mathrm{H} ^ {d} (\mathrm{U}, a \underline {{\pi}} _ {d} (\mathcal {X})) & \text {otherwise} \end{array} \right.
$$

Corollary 1.35. — Let $\mathcal{K}$ be a fibrant simplicial sheaf satisfying the conditions of Definition 1.32 for some $d \geqslant 1$ and let U be an object of T such that for any sheaf of abelian groups F on T and any $m \geqslant d$ one has $\mathrm{H}^m (\mathrm{U},\mathrm{F}) = 0$. Then $\pi_0(\mathcal{K}(\mathrm{U})) = pt$.

Sheaves with only one nontrivial homotopy group are related to Postnikov towers as follows.

Proposition 1.36. — Let X be a locally fibrant simplicial sheaf and  $p: Y \to Z$  be a local fibration weakly equivalent to the local fibration  $\mathbf{P}^{(d)}\mathcal{X} \to \mathbf{P}^{(d-1)}\mathcal{X}$ . Then for any U in T and any point z in  $\mathcal{Z}(\mathbf{U})_{0}$  the fiber  $F_{z}$  of p over z considered as a sheaf on T/U has only one nontrivial homotopy group in dimension d (which is abelian if  $d \geqslant 2$ ).

Proof. — Follows by the use of points from [22, Cor. 8.7].

Theorem 1.37. — Let T be a site and suppose that there exists a family  $(\mathbf{A}_{d})_{d\geqslant0}$  of classes of objects of T such that the following conditions hold:

1. Any object U in  $A_{d}$  has cohomological dimension  $\leqslant d$  i.e. for any sheaf F on T/U and any m > d one has  $\mathbf{H}^{m}(\mathbf{U}, \mathbf{F}) = 0$ .

2. For any object V of T there exists an integer  $d_{V}$  such that any covering of V in T has a refinement of the form  $\{U_{i} \rightarrow V\}$  with  $U_{i}$  being in  $A_{d_{V}}$ .

Then $\mathbf{T}$ is a site of finite type.

Proof. — Let $\mathcal{X}$ be a simplicial sheaf on T. Denote by $p^{(i)}: \mathrm{GP}^{(i)}(\mathcal{X}) \to \mathrm{GP}^{(i-1)}(\mathcal{X})$ a tower of fibrations weakly equivalent to the tower of local fibrations $\mathrm{P}^{(i)}\mathcal{X} \to \mathrm{P}^{(i-1)}\mathcal{X}$. This tower is then pointwise weakly equivalent to the tower $(Ex(\mathrm{P}^{(i)}\mathcal{X}))$ for any resolution functor $Ex$ on simplicial sheaves and since homotopy limits preserve pointwise weak equivalences of Kan simplicial sets and homotopy limit of a tower of fibration is weakly equivalent to the ordinary limit we conclude that to prove the theorem we have to show that the canonical morphism $\mathcal{X} \to \lim_{i \geq 0} \mathrm{GP}^{(i)}\mathcal{X}$ is a weak equivalence. We may further assume that $\mathcal{X}$ is a fibrant simplicial sheaf.

It is easy to see that our claim will follow if we show that the sheaves $a\underline{\pi}_0(\mathcal{X})$ and $a\underline{\pi}_0(\lim_{i\geqslant 0}\mathrm{GP}^i)\mathcal{X})$ are isomorphic for all $\mathcal{X}$ (to deduce the same fact for $\pi_i$ one then replaces $\mathcal{X}$ by the simplicial sheaf of pointed maps from any model of the i-sphere to $\mathcal{X}$).

By the second condition of the theorem any object in T has a covering consisting of objects in  $A_{d}$  for some d. Therefore it is sufficient to verify that for any  $d \geqslant 0$  and any  $U \in A_{d}$  the canonical map  $a\underline{\pi}_{0}(\mathcal{X})(U) \to a\underline{\pi}_{0}(\lim_{i \geqslant 0} GP^{(i)}\mathcal{X})(U)$  is an isomorphism. By definition of  $P^{(i)}$  for any  $i \geqslant 0$  we have

$$
a \underline {{\pi}} _ {0} (\mathbf {P} ^ {(i)} \mathcal {K}) = a \underline {{\pi}} _ {0} (\mathbf {G P} ^ {(i)} \mathcal {K}) = a \underline {{\pi}} _ {0} (\mathcal {K})
$$

which immediately implies that the map in question is a monomorphism. The fact that it is an epimorphism follows from the standard criterion for a map of presheaves to give an epimorphism of sheaves, Lemma 1.38 below and the exact form of condition (2) of the theorem.

Lemma 1.38. — Let U be an object in $\mathbf{A}_d$. Then

$$
\pi_ {0} (\lim _ {i \geqslant 0} \mathrm{GP} ^ {(i)} \mathcal {K} (\mathrm{U})) \rightarrow \pi_ {0} (\mathrm{GP} ^ {(d)} \mathcal {K} (\mathrm{U}))
$$

is an isomorphism.

Proof. — Let  $p^{(i)} : \mathbf{K}^{(i)} \to \mathbf{K}^{(i-1)}$ ,  $i \geqslant 1$  be a sequence of Kan fibrations of Kan simplicial sets and d be such that for any  $m \geqslant d$  and any  $x \in \mathbf{K}_{0}^{(m)}$  one has  $\pi_{0}((p^{(m+1)})^{-1}(x)) = pt$ . Then the map  $\pi_{0}(\lim_{i} \mathbf{K}^{(i)}) \to \pi_{0}(\mathbf{K}^{(d)})$  is bijective. Combining this fact with Corollary 1.35 and Proposition 1.36 we get the statement of the lemma.

Remark 1.39. — We do not know of any example of a site where each object has a finite cohomological dimension but condition (2) of Theorem 1.37 does not hold.

For sites of finite type Corollary 1.35 has the following important generalization which is the basis for all kinds of convergence theorems for spectral sequences build out of towers of local fibrations on such sites.

Proposition 1.40. — Let T be a site of finite type and U be an object of T of cohomological dimension less than or equal to  $d \geqslant 2$ . Let further X be a fibrant simplicial sheaf on T which has no nontrivial homotopy groups in dimension  $\leqslant d$  i.e. such that the sheaf  $\mathrm{P}^{(d)}\mathcal{X}$  is weakly equivalent to the point. Then  $\pi_{0}(\mathcal{X}(U)) = pt$ .

Proof. — Let  $\mathrm{GP}^{(i+1)}\mathcal{X}\to\mathrm{GP}^{(i)}\mathcal{X}$  be a tower of fibrations weakly equivalent to the tower of local fibrations  $\mathrm{P}^{(i+1)}\mathcal{X}\to\mathrm{P}^{(i)}\mathcal{X}$ . Since T is a site of finite type one has  $\mathcal{X}(\mathrm{U})\cong\lim_{i\geq0}\mathrm{GP}^{(i)}\mathcal{X}(\mathrm{U})$ . By Corollary 1.35 and Proposition 1.36 the fibers  $F_{i}$  of the maps  $\mathrm{GP}^{i+1}\mathcal{X}(\mathrm{U})\to\mathrm{GP}^{i}\mathcal{X}(\mathrm{U})$  satisfy the condition  $\pi_{0}(\mathrm{F}_{i})=pt$  for  $i\geq d$ . Therefore  $\pi_{0}(\lim_{i\geq0}\mathrm{GP}^{(i)}\mathcal{X}(\mathrm{U}))=\pi_{0}(\mathrm{GP}^{(d)}\mathcal{X}(\mathrm{U}))$  and the latter set is pt by our condition on X.

Corollary 1.41. — For any T and U as in Proposition 1.40 and any simplicial sheaf $\mathcal{K}$ one has:

1. the map $\pi_0(Ex(\mathcal{K})(\mathbf{U})) \to \pi_0(Ex(\mathbf{P}^i\mathcal{K})(\mathbf{U}))$ is an epimorphism for $i \geqslant d - 1$ and an isomorphism for $i \geqslant d$;

2. for any $x \in \mathcal{X}(\mathbf{U})$ the map $\pi_k(Ex(\mathcal{X})(\mathbf{U}), x) \to \pi_k(Ex(\mathbf{P}^i\mathcal{X})(\mathbf{U}), x)$ is an epimorphism for $i - k \geqslant d - 1$ and an isomorphism for $i - k \geqslant d$.

## Functoriality

We first recall briefly the standard definitions related to functoriality of sites. Let  $f^{-1}: T_{2} \to T_{1}$  be a functor between the underlying categories of sites  $T_{1}, T_{2}$ . Associated to any such functor we have a pair of adjoint functors between the corresponding categories of presheaves of sets

$$
f _ {p r e} ^ {*}: \operatorname{PreShv} \left(\mathrm{T} _ {2}\right)\rightarrow \operatorname{PreShv} \left(\mathrm{T} _ {1}\right)
$$

$$
f _ {*}: \operatorname{PreShv} \left(\mathrm{T} _ {1}\right)\rightarrow \operatorname{PreShv} \left(\mathrm{T} _ {2}\right)
$$

(where $f_*$ is just the functor given by the composition with $f^{-1}$).

Definition 1.42. — A continuous map of sites $f: \mathrm{T}_{1} \to \mathrm{T}_{2}$ is a functor $f^{-1}: \mathrm{T}_{2} \to \mathrm{T}_{1}$ such that for any sheaf $\mathbf{F}$ on $\mathrm{T}_{1}$ the presheaf $f_{*}(\mathbf{F})$ is a sheaf on $\mathrm{T}_{2}$.

If $f$ is a continuous map of sites, the functor $f_{*} \colon Shv(\mathrm{T}_{1}) \to Shv(\mathrm{T}_{2})$ has a left adjoint $f^{*} \colon Shv(\mathrm{T}_{2}) \to Shv(\mathrm{T}_{1})$ given by the composition of the inclusion $Shv(\mathrm{T}_{2}) \subset PreShv(\mathrm{T}_{2})$ with the functor $f_{pre}^{*}$ and the functor associated sheaf $a: PreShv(\mathrm{T}_{1}) \to Shv(\mathrm{T}_{1})$.

Definition 1.43. — A continuous map of sites $f: \mathrm{T}_{1} \to \mathrm{T}_{2}$ is called a morphism of sites if the functor $f^{*}: Shv(\mathrm{T}_{2}) \to Shv(\mathrm{T}_{1})$ commutes with finite limits.

Remark 1.44. — If the topology on  $T_{2}$  is defined by a pretopology ([13, II. Definition 1.3]) and the functor  $f^{-1}$  commutes with fiber products then  $f^{-1}$  defines a continuous map of sites if and only if it takes coverings (of the pretopology on  $T_{2}$ ) to coverings (cf [13, III. Proposition 1.6]). See [13, III. Exemple 1.9.3] for an example of a functor  $f^{-1}$  which takes coverings to coverings and which is not continuous.

Remark 1.45. — If the category  $T_{2}$  has fiber products and any representable presheaf on  $T_{1}$  is a sheaf then a continuous map f is a morphism of sites if and only if the functor  $f^{-1}$  commutes with fiber products. A more general statement can be found in (cf [13, IV.4.9.2]).

Example 1.46. — A typical example of a continuous map which is not a morphism of sites is given by the inclusion functor  $Sm/S \rightarrow Sch/S$  from the category of smooth S-schemes of finite type to the category of all schemes of finite type over some base scheme S considered with Zariski (or etale, flat, Nisnevich etc.) topology (cf 1.19 below).

Let $f: T_{1} \to T_{2}$ be a continuous map of sites. Then we have a pair of adjoint functors

$$
\begin{array}{l} f ^ {*}: \Delta^ {o p} S h v (\mathrm{T} _ {2}) \longrightarrow \Delta^ {o p} S h v (\mathrm{T} _ {1}) \\ f _ {*}: \Delta^ {o p} S h v (\mathrm{T} _ {1}) \longrightarrow \Delta^ {o p} S h v (\mathrm{T} _ {2}) \end{array}
$$

between the corresponding categories of simplicial sheaves. In general neither one of them preserves weak equivalences.

Choose a resolution functor $Ex$ for $T$ (see 1.6). The functor $f_* \circ Ex: \Delta^{op}Shv(T_1) \to \Delta^{op}Shv(T_2)$ does preserve weak equivalences because for any weak equivalence $f$ the morphism $Ex(f)$ is a simplicial homotopy equivalence ($cf$ 1.10) and the functor $f_*$ clearly preserves simplicial homotopies. Let us denote by

$$
\mathbf {R} f _ {*}: \mathcal {H} _ {s} (\mathrm{T} _ {1}) \rightarrow \mathcal {H} _ {s} (\mathrm{T} _ {2})
$$

the functor induced by the functor $f_* \circ Ex$. One can easily see that $\mathbf{R}f_*$ is the total right derived of $f_*$ in the sense of [26, I.4]; in particular it doesn't depend on the choice of the resolution functor $Ex$.

The following simple result describes the basic functoriality of the simplicial homotopy categories for morphisms of sites.

Proposition 1.47. — Let $f: \mathrm{T}_{1} \to \mathrm{T}_{2}$ be a morphism of sites. Then the functor $f^{*}$ preserves weak equivalences and the corresponding functor between homotopy categories is left adjoint to $\mathbf{R}f_{*}$. If $\mathrm{T}_{1} \xrightarrow{f} \mathrm{T}_{2} \xrightarrow{g} \mathrm{T}_{3}$ is a composable pair of morphisms of sites then the canonical morphism of functors

$$
\mathbf {R} (g \circ f) _ {*} \rightarrow \mathbf {R} g _ {*} \circ \mathbf {R} f _ {*}
$$

is an isomorphism.

For a site T denote by  $T'$  the site with the same underlying category considered with the trivial topology and let  $\pi: T \to T'$  be the canonical morphism of sites. Then  $\pi_{*}$  is the inclusion of sheaves to presheaves,  $\pi^{*}$  is the functor of associated sheaf and we have the following refinement of Proposition 1.47.

Lemma 1.48. — In the notations given above the functor

$$
\pi^ {*}: \mathcal {H} _ {s} (\mathrm{T} ^ {\prime}) \rightarrow \mathcal {H} _ {s} (\mathrm{T})
$$

is a localization, the functor $\mathbf{R}\pi_{*}:\mathcal{H}_{s}(\mathrm{T})\to \mathcal{H}_{s}(\mathrm{T}^{\prime})$ is a full embedding and there is a canonical isomorphism $\pi^{*}\mathbf{R}\pi_{*}\cong Id$.

If f is not a morphism of sites it is not clear in general whether or not  $Rf_{*}$  has a left adjoint. There are also examples of composable pairs of continuous maps f and g such that the natural morphism  $\mathbf{R}(g \circ f)_{*} \to \mathbf{R}g_{*} \circ \mathbf{R}f_{*}$  is not an isomorphism. We are going to define now a class of continuous maps called reasonable for which a left adjoint to  $Rf_{*}$  always exists and the composition morphisms are isomorphisms.

Recall that for simplicial sheaves $\mathcal{X},\mathcal{X}'$, the simplicial function object $\mathrm{S}(\mathcal{X},\mathcal{X}')$ is the simplicial set of the form

$$
\mathrm{S} (\mathcal {X}, \mathcal {X} ^ {\prime}) _ {n} = H o m _ {\Delta^ {o p} S h v (\Gamma)} (\mathcal {X} \times \Delta^ {n}, \mathcal {X} ^ {\prime}).
$$

Definition 1.49. — Let  $T_{1} \rightarrow T_{2}$  be a continuous map of sites. A simplicial sheaf Y on  $T_{2}$  is said to be f-admissible if for any fibrant simplicial sheaf X on  $T_{1}$  and any simplicial set K the map :

$$
\pi (\mathcal {Y} \times \mathrm{K}, f _ {*} (\mathcal {X})) \rightarrow H o m _ {\mathcal {H} _ {s} (\mathrm{T} _ {2})} (\mathcal {Y} \times \mathrm{K}, f _ {*} (\mathcal {X}))
$$

is bijective.

We say that  $T_{2}$  has enough f-admissibles if there is a functor  $ad_{f}: \Delta^{op}Shv(T_{2}) \to \Delta^{op}Shv(T_{2})$  and a natural transformation  $ad_{f} \to Id$  such that  $ad_{f}$  takes values in the full subcategory of objects admissible with respect to f and for any Y on  $T_{2}$  the morphism  $ad_{f}(\mathcal{Y}) \to \mathcal{Y}$  is a weak equivalence. We then say that the pair  $(ad_{f}, ad_{f} \to Id)$  is an f-admissible resolution.

Remark 1.50. — Observe that a simplicial sheaf Y on  $T_{2}$  is f-admissible if and only if for any fibrant simplicial sheaf X on  $T_{1}$  and for any weak equivalence  $f_{*}(\mathcal{X}) \to \mathcal{X}'$  with  $X'$  fibrant the induced map of simplicial sets  $\mathrm{S}(\mathcal{Y}, f_{*}(\mathcal{X})) \to \mathrm{S}(\mathcal{Y}, \mathcal{X}')$  is a weak equivalence.

The following two results follow immediately from the definitions (and the formal fact that for any simplicial sheaves X on  $T_{1}$ , Y on  $T_{2}$ , the map  $\pi(\mathcal{Y} \times \mathbf{K}, f_{*}(\mathcal{X})) \to \pi(f^{*}(\mathcal{Y}) \times \mathbf{K}, \mathcal{X})$  is bijective).

Proposition 1.51. — Let  $T_{1} \rightarrow T_{2}$  be a continuous map of sites such that  $T_{2}$  has enough admissibles with respect to f and  $(ad_{f}, ad_{f} \rightarrow Id)$  be an f-admissible resolution. Then the functor  $f^{*} \circ ad_{f}$  preserves weak equivalences and the induced functor  $\mathbf{L} f^{*}: \mathcal{H}_{s}(\mathbf{T}_{2}) \to \mathcal{H}_{s}(\mathbf{T}_{1})$  is left adjoint to  $Rf_{*}$  (in particular this induced functor is independent of the f-admissible resolution).

Proposition 1.52. — Let  $T_{1} \rightarrow T_{2}$  be a continuous map of sites such that  $T_{2}$  has enough f-admissibles. Then a simplicial sheaf K on  $T_{2}$  is f-admissible if and only if the canonical morphism  $f^{*}(ad_{f}(\mathcal{K})) \rightarrow f^{*}(\mathcal{K})$  is a weak equivalence.

Lemma 1.53. — Let  $T_{1} \rightarrow T_{2}$  be a continuous map of sites and  $A_{f}$  be the class of f-admissible simplicial sheaves on  $T_{2}$ . Then one has:

1. $\mathbf{A}_f$ is closed under sums;

2. for any diagram of the form $\mathcal{Y}_0 \xrightarrow{u_0} \mathcal{Y}_1 \xrightarrow{u_1} \ldots \xrightarrow{u_{n-1}} \mathcal{Y}_n \to \ldots$ such that $\mathcal{Y}_n \in \mathbf{A}_f$ and all the morphisms $u_n, f^*(u_n)$ are monomorphisms one has $\operatorname{colim}_n \mathcal{Y}_n \in \mathbf{A}_f$;

3. for any cocartesian square of the form

![](images/page_20_image_8.jpg)

such that $\mathcal{Y}_0, \mathcal{Y}_1, \mathcal{Y}_2 \in \mathbf{A}_f$ and both $u$ and $f^*(u)$ are monomorphisms one has $\mathcal{Y}_3 \in \mathbf{A}_f$.

Proof. — The first statement is obvious. The second follows from the fact that an inverse limit of a tower of weak equivalences of simplicial sets is a weak equivalence at least if all the morphisms in the towers are fibrations.

To prove the third one, one notes that for any fibrant $\mathcal{X}$ on $\mathrm{T}_1$ we have a morphism of Cartesian squares of simplicial sets consisting of $\mathrm{S}(\mathcal{Y}_i,f_*(\mathcal{X}))$ and $\mathrm{S}(\mathcal{Y}_i,Ex(f_*(\mathcal{X})))$ respectively such that three out of four morphisms are weak equivalences and all we have to show is that the fourth one is also a weak equivalence. This follows immediately from the fact that the maps

$$
\begin{array}{l} \mathrm{S} (\mathcal {Y} _ {1}, f _ {*} (\mathcal {X})) \to \mathrm{S} (\mathcal {Y} _ {0}, f _ {*} (\mathcal {X})) \\ \mathrm{S} (\mathcal {Y} _ {1}, E x (f _ {*} (\mathcal {X}))) \to \mathrm{S} (\mathcal {Y} _ {0}, E x (f _ {*} (\mathcal {X}))) \end{array}
$$

induced by $u$ are fibrations - the first one since $f^{*}(u)$ is a monomorphism and $\mathcal{X}$ is fibrant and the second since $u$ is a monomorphism and $Ex(f_{*}(\mathcal{X}))$ is fibrant.

Proposition 1.54. — Let Y be a simplicial sheaf on  $T_{2}$  such that all its terms  $Y_{n}$  are f-admissible. Then so is Y.

Proof. — Let X be a fibrant simplicial sheaf on  $T_{1}$ . We have to show that the morphism of simplicial sets  $\mathrm{S}(\mathcal{Y}, f_{*}(\mathcal{X})) \to \mathrm{S}(\mathcal{Y}, \mathcal{X}')$  is a weak equivalence for any weak equivalence  $X \to X'$  with  $X'$  fibrant. This morphism can be obtained by applying the total space functor to the morphism of the corresponding cosimplicial simplicial sets (cf [3, X.3]) which is a weak equivalence in the sense of [3] by the conditions of the proposition.

For any simplicial sheaf Y and any fibrant simplicial sheaf Z the cosimplicial simplicial set  $\mathrm{S}(\mathcal{Y},\mathcal{Z})$  is fibrant (in the sense of [3, X]). Since  $\mathrm{S}(\mathcal{Y},f_{*}(\mathcal{X}))=\mathrm{S}(f^{*}(\mathcal{Y}),\mathcal{X})$  we conclude that both cosimplicial simplicial sets we consider are fibrant and our result follows now from [3, X.5.2].

Definition 1.55. — A continuous map  $T_{1} \rightarrow T_{2}$  is called reasonable if any representable sheaf on  $T_{2}$  is f-admissible.

Example 1.56. — One may get an “unreasonable” map of sites as follows. Let  $f: T_{1} \to T_{2}$  be any continuous map which is not a morphism of sites. Consider  $Shv(T_{1})$  and  $Shv(T_{2})$  as sites with the canonical topologies. Then the functor of inverse image  $Shv(T_{2}) \to Shv(T_{1})$  is an unreasonable continuous map. Note that this example also confirms that the notion of a reasonable map actually depends on sites and not just on the corresponding topoi.

Let $f: T_1 \to T_2$ be a reasonable continuous map of sites. By Lemma 1.16 applied to the set $\mathcal{S}$ of representable sheaves there exists a functor $\Phi_{T_2}: \Delta^{op}Shv(T) \to \Delta^{op}Shv(T)$ and a natural transformation $\Phi_{T_2} \to Id$ such that for any $\mathcal{X}$ and any $n \geqslant 0$ the sheaf of sets $\Phi_{T_2}(\mathcal{X})_n$ is a direct sum of representable sheaves and the morphism $\Phi_{T_2}(\mathcal{X}) \to \mathcal{X}$ is a trivial local fibration. Proposition 1.54 then implies that $T_2$ has enough $f$-admissibles. We may sum up the situation as follows using Propositions 1.51, 1.52 and keeping previous notations.

Proposition 1.57. — Let $f: \mathrm{T}_{1} \to \mathrm{T}_{2}$ be a reasonable continuous map of sites:

1. the functor $f^{*} \circ \Phi_{\mathrm{T}_{2}} : \Delta^{op} Shv(\mathrm{T}_{2}) \to \Delta^{op} Shv(\mathrm{T}_{1})$ preserves weak equivalences and the induced functor $\mathbf{L}f^{*} : \mathcal{H}_{s}(\mathrm{T}_{2}) \to \mathcal{H}_{s}(\mathrm{T}_{1})$ is left adjoint to $\mathbf{R}f_{*}$;

2. if $\mathcal{Y}$ is a simplicial sheaf such that any term $\mathcal{Y}_n$ of $\mathcal{Y}$ is a direct sum of representable sheaves then the canonical morphism $f^*(\Phi_{\mathrm{T}_2}(\mathrm{F})) \to f^*(\mathrm{F})$ is a weak equivalence;

3. if $\mathrm{T}_1 \xrightarrow{f} \mathrm{T}_2 \xrightarrow{g} \mathrm{T}_3$ is a composable pair of reasonable continuous maps of sites then there are canonical isomorphisms

$$
\mathbf {L} (g \circ f) ^ {*} = \mathbf {L} f ^ {*} \circ \mathbf {L} g ^ {*}
$$

$$
\mathbf {R} (g \circ f) _ {*} = \mathbf {R} g _ {*} \circ \mathbf {R} f _ {*}
$$

of functors between the corresponding homotopy categories.

Remark 1.58. — An example of a reasonable continuous map $f: \mathrm{T}_{1} \to \mathrm{T}_{2}$ and a simplicial sheaf $\mathcal{Y}$ on $\mathrm{T}_{2}$ such the morphism $\mathbf{L}f^{*}(\mathcal{Y}) \to f^{*}(\mathcal{Y})$ is not a weak equivalence is given in 1.22.

## Godement resolutions

The main result of this section is Theorem 1.66 below which asserts that for any site of finite type there exists a resolution functor on the category of simplicial sheaves which commutes with finite limits and takes local fibrations to global fibrations. We do not know whether the finite type assumption is really necessary for this result or not.

For any set of points $\mathcal{L}$ of T define a functor $\mathcal{G}_{\mathcal{L}}^{\bullet}$ from sheaves on T to cosimplicial sheaves on T as follows. Let $\mathcal{E}$ be the product of $\mathcal{L}$ copies of the category of sets. A point of T is a morphism of sites $Sets \to T$ and a set of points $\mathcal{L}$ defines a morphism of sites $p: \mathcal{E} \to T$. The corresponding adjoint pair of functors $p^{*}$ and $p_{*}$ gives in a standard way a cosimplicial functor with terms of the form $(p_{*}p^{*})^{n+1}$ which we denote by $\mathcal{G}_{\mathcal{L}}^{\bullet}$. In most places below we omit $\mathcal{L}$ from our notations.

Proposition 1.59. — For any local fibration of locally fibrant simplicial sheaves $f: \mathcal{X} \to \mathcal{Y}$ the morphism

$$
h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} (f): h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} \mathcal {K} \rightarrow h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} \mathcal {Y}
$$

is a fibration.

Proof. — By definition of local fibration the functor  $p^{*}$  takes local fibrations to fibrations in  $\Delta^{op}Shv(\mathcal{E})$ . Since direct images preserve fibrations the composition  $p_{*}p^{*}$  takes local fibrations to fibrations and in particular locally fibrant sheaves to fibrant sheaves. The statement of the proposition follows now from Proposition 1.22.

Proposition 1.60. — The functor $\mathcal{X} \mapsto \operatorname{holim}_{\Delta} \mathcal{G}^{\bullet}(\mathcal{X})$ takes weak equivalences of locally fibrant simplicial sheaves to weak equivalences of simplicial sheaves.

Proof. — One can easily see that the functors  $(p_{*}p^{*})^{n+1}$  take weak equivalences to pointwise weak equivalences. The statement of the proposition follows now from the fact that holim preserves pointwise weak equivalences between pointwise fibrant sheaves by its definition and the corresponding result for simplicial sets (see [3, XI.5.6]).

Proposition 1.61. — Let $\mathcal{X}^{\bullet}$ be a cosimplicial simplicial sheaf such that all of its simplicial terms are locally fibrant and there exists $s \geqslant 0$ such that the canonical morphisms

$$
\mathcal {K} ^ {n} \rightarrow \mathrm{P} ^ {(s)} \mathcal {K} ^ {n}
$$

are weak equivalences for all  $n \geqslant 0$ . Then for any point x of T the canonical morphism

$$
x ^ {*} (h o l i m _ {\Delta} \mathcal {K} ^ {\bullet}) \rightarrow h o l i m _ {\Delta} x ^ {*} \mathcal {K} ^ {\bullet}
$$

is a weak equivalence.

Proof. — Let  $Ex^{R}$  be a resolution functor on the category of cosimplicial simplicial sets (with respect to the standard closed model structure described in [3]). Below we use the equality sign instead of specifying explicit weak equivalences. Unless otherwise specified functors on cosimplicial simplicial sets are extended to functors on cosimplicial simplicial presheaves pointwise. The functor of associated sheaf is denoted by a. We have

$$
x ^ {*} (h o l i m _ {\Delta} \mathcal {K} ^ {\bullet}) = x ^ {*} a (h o l i m _ {\Delta} \mathcal {K} ^ {\bullet}) = x ^ {*} a (h o l i m _ {\Delta} E x ^ {\mathrm{R}} (\mathcal {K} ^ {\bullet}))
$$

since the functor  $x^{*}a$  takes pointwise weak equivalences of simplicial presheaves to weak equivalences of simplicial sets. We have

$$
x ^ {*} a (h o l i m _ {\Delta} E x ^ {R} (\mathcal {X} ^ {\bullet})) = x ^ {*} a (T o t (E x ^ {R} (\mathcal {X} ^ {\bullet})))
$$

since the homotopy limit is weakly equivalent to $\mathcal{T}\dot{t}$ for fibrant cosimplicial simplicial sets. By Lemma 1.62 we have

$$
x ^ {*} a (T o t (E x ^ {R} (\mathscr {K} ^ {\bullet}))) = x ^ {*} a (T o t _ {s + 1} (E x ^ {R} (\mathscr {K} ^ {\bullet}))).
$$

Since  $Tot_{s+1}$  involves only finite limits and functors  $x^{*}$  and a commute with such limits we have

$$
x ^ {*} a (T o t _ {s + 1} (E x ^ {\mathrm{R}} (\mathscr {K} ^ {\bullet}))) = T o t _ {s + 1} (x ^ {*} a (E x ^ {\mathrm{R}} (\mathscr {K} ^ {\bullet}))).
$$

The functor  $x^{*}a$  commutes with finite limits and takes pointwise fibrations of simplicial presheaves to Kan fibrations of simplicial sets. In addition  $x^{*}a$  commutes with pointwise  $\mathbf{P}^{(s)}$ . Therefore cosimplicial simplicial set  $x^{*}a(Ex^{\mathrm{R}}(\mathcal{K}^{\bullet}))$  satisfies the condition of Lemma 1.62 and we have

$$
\operatorname{Tot} _ {s + 1} \left(x ^ {*} a \left(E x ^ {\mathrm{R}} \left(\mathscr {X} ^ {\bullet}\right)\right)\right) = \operatorname{Tot} \left(x ^ {*} a \left(E x ^ {\mathrm{R}} \left(\mathscr {X} ^ {\bullet}\right)\right)\right) = h o l i m _ {\Delta} \left(x ^ {*} a \left(E x ^ {\mathrm{R}} \left(\mathscr {X} ^ {\bullet}\right)\right)\right).
$$

Finally  $x^{*}a$  takes pointwise weak equivalences to weak equivalences and therefore

$$
h o l i m _ {\Delta} (x ^ {*} a (E x ^ {\mathrm{R}} (\mathcal {K} ^ {\bullet}))) = h o l i m _ {\Delta} x ^ {*} a \mathcal {K} ^ {\bullet} = h o l i m _ {\Delta} x ^ {*} \mathcal {K} ^ {\bullet}.
$$

Lemma 1.62. — Let $\mathbf{K}^{\bullet}$ be a fibrant cosimplicial simplicial set and $s \geqslant 0$ be an integer such that for any $n \geqslant 0$ the map of simplicial sets $\mathbf{K}^{n} \to \mathbf{P}^{(s)}\mathbf{K}^{n}$ is a weak equivalence. Then the canonical map

$$
\mathsf {T o t K} ^ {\bullet} \rightarrow \mathsf {T o t} _ {s + 1} \mathbf {K} ^ {\bullet}
$$

is a weak equivalence of simplicial sets.

Proof. — Let  $cosk_{s+1}K^{\bullet}$  be the cosimplicial simplicial set obtained from  $K^{\bullet}$  by applying the coskeleton functor to each simplicial term. Under our assumptions on  $K^{\bullet}$  the canonical morphism  $K^{\bullet} \rightarrow cosk_{s+1}K^{\bullet}$  is a weak equivalence of cosimplicial simplicial sets. In addition, the cosimplicial simplicial set  $cosk_{s+1}K^{\bullet}$  is fibrant i.e. all the maps  $cosk_{s+1}K^{n+1} \rightarrow M^{n}cosk_{s+1}K^{\bullet}$  are fibrations (see [3]). To prove this fact observe that the functor  $cosk_{s+1}$  commutes with finite limits which implies that  $M^{n}cosk_{s+1}K^{\bullet} = cosk_{s+1}M^{n}K^{\bullet}$ . Although the coskeleton functor does not in general take Kan fibrations to Kan fibrations the following simple result holds.

Lemma 1.63. — Let $f: \mathbf{E} \to \mathbf{B}$ be a Kan fibration of Kan simplicial sets and $s$ be an integer such that for any point $x$ in $\mathbf{B}$ one has $\pi_{s+1}(\mathbf{B}, x) = 0$. Then $\cos k_{s+1}(f)$ is again a Kan fibration.

Under our assumptions on  $K^{\bullet}$  we have  $\pi_{s+1}(\mathbf{M}^{n}\mathbf{K}^{\bullet}, x)=0$  for any point x in  $M^{n}K^{\bullet}$ . This can be shown by induction on n using the intermediate objects  $M_{k}^{n}K^{\bullet}$  as in [3, Lemma 5.3, p. 278]. Therefore the maps  $cosk_{s+1}K^{n+1} \rightarrow cosk_{s+1}M^{n}K^{\bullet}$  are fibrations and  $cosk_{s+1}X$  is fibrant.

For any cosimplicial simplicial set  $K^{\bullet}$  the canonical map  $\operatorname{Tot}(\cos k_{s+1}K^{\bullet}) \to \operatorname{Tot}_{s+1}(\cos k_{s+1}K^{\bullet})$  is an isomorphism of cosimplicial simplicial sets. Since both functors  $\operatorname{Tot}$  and  $\operatorname{Tot}_{s+1}$  preserve weak equivalences between fibrant objects we conclude that

$$
\operatorname{Tot} \left(\mathbf {K} ^ {\bullet}\right) \cong \operatorname{Tot} \left(\cos k _ {s + 1} \mathbf {K} ^ {\bullet}\right) = \operatorname{Tot} _ {s + 1} \left(\cos k _ {s + 1} \mathbf {K} ^ {\bullet}\right) \cong \operatorname{Tot} _ {s + 1} \left(\mathbf {K} ^ {\bullet}\right).
$$

Lemma 1.64. — For any simplicial sheaf $\mathcal{K}$ the composition

$$
p ^ {*} \mathcal {K} \rightarrow p ^ {*} (h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} \mathcal {K}) \rightarrow h o l i m _ {\Delta} p ^ {*} (\mathcal {G} ^ {\bullet} \mathcal {K})
$$

is a weak equivalence of simplicial sheaves on $\mathcal{E}$.

Proof. — This is a particular case of [23, Cor. 3.5]. In the notations of that paper one takes U = Id, F = p\* and T = p\_\*p\*.

Recall that a set $\mathcal{L}$ of points of T is called conservative if any morphism $f: \mathrm{F} \to \mathrm{G}$ of sheaves on T for which all the maps of sets $x^{*}(f): x^{*}\mathrm{F} \to x^{*}\mathrm{G}$ are isomorphisms is an isomorphism.

Proposition 1.65. — Let T be a site of finite type and $\mathcal{L}$ be a conservative set of points of T. Then for any locally fibrant simplicial sheaf $\mathcal{X}$ the canonical morphism $g_{\mathcal{X}}: \mathcal{X} \to \operatorname{holim}_{\Delta} \mathcal{G}^{\bullet}(\mathcal{X})$ is a weak equivalence.

Proof. — We will prove this fact in several steps.

1. For any $s$ the canonical morphism $\mathbf{P}^{(s)}\mathcal{X}\to holim_{\Delta}\mathcal{G}^{\bullet}\mathbf{P}^{(s)}\mathcal{X}$ is a weak equivalence.

Proof. — Since $\mathcal{L}$ is a conservative set of points it is sufficient to show that the morphism

$$
p ^ {*} (\mathbf {P} ^ {(s)} \mathcal {K}) \rightarrow p ^ {*} (h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} \mathbf {P} ^ {(s)} \mathcal {K})
$$

is a weak equivalence. This follows from Proposition 1.61 and Lemma 1.64.

2. The canonical morphism

$$
h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} \mathcal {K} \rightarrow h o l i m _ {s \geqslant 0} (h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} \mathrm{P} ^ {(s)} \mathcal {K})
$$

is a weak equivalence.

Proof. — By Proposition 1.59 all the simplicial sheaves  $holim_{\Delta}G^{\bullet}P^{(s)}X$  are fibrant and the morphisms between them are fibrations. Thus by [3, XI.4.1] the right hand side is pointwise weakly equivalent to  $\lim_{s\geqslant0}(holim_{\Delta}G^{\bullet}P^{(s)}X)$ . We further have

$$
\lim _ {s \geqslant 0} (h o l i m _ {\Delta} \mathcal {G} ^ {\bullet} \mathrm{P} ^ {(s)} \mathcal {K}) = h o l i m _ {\Delta} \lim _ {s \geqslant 0} (\mathcal {G} ^ {\bullet} \mathrm{P} ^ {(s)} \mathcal {K})
$$

since holim commutes with limits. On the other hand for any n we have

$$
\lim _ {s \geqslant 0} (p _ {*} p ^ {*}) ^ {n + 1} (\mathrm{P} ^ {(s)} \mathcal {K}) = (p _ {*} p ^ {*}) ^ {n + 1} (\lim _ {s \geqslant 0} \mathrm{P} ^ {(s)} \mathcal {K}) = (p _ {*} p ^ {*}) ^ {n + 1} (\mathcal {K})
$$

since the towers of sheaves of sets $(\mathbf{P}^{(s)}\mathcal{X})_i$ stabilize after finitely many steps for each $i$ which implies that

$$
\lim _ {s \geqslant 0} (\mathcal {G} ^ {\bullet} \mathrm{P} ^ {(s)} \mathcal {K}) \cong \mathcal {G} ^ {\bullet} \mathcal {K}.
$$

3. By step 1 $\text{holim}_{\Delta} \mathcal{G}^{\bullet} \mathrm{P}^{(s)} \mathcal{K}$ is weakly equivalent to $\mathrm{P}^{(s)} \mathcal{K}$ and since it is fibrant (by Proposition 1.59) it is pointwise weakly equivalent to $Ex(\mathrm{P}^{(s)} \mathcal{K})$ for any resolution functor $Ex$ on $\Delta^{op} Shv(T)$. Since $\text{holim}_{s \geqslant 0}$ preserves pointwise weak equivalences between pointwise fibrant objects step 2 implies that $\text{holim}_{\Delta} \mathcal{G}^{\bullet} \mathcal{K}$ is weakly equivalent to $\text{holim}_{s \geqslant 0} Ex(\mathrm{P}^{(s)} \mathcal{K})$ which is weakly equivalent to $\mathcal{K}$ by definition of site of finite type.

Theorem 1.66. — Let T be a site of finite type. Then there exists a functor

$$
E x ^ {\mathcal {G}}: \Delta^ {o p} S h v (\mathrm{T}) \rightarrow \Delta^ {o p} S h v (\mathrm{T})
$$

and a natural transformation $Id \to Ex^{\mathcal{G}}$ with the following properties:

1. $Ex^{\mathcal{G}}$ commutes with finite limits and in particular takes the final object to the final object;

2. Ex $^{G}$ takes any simplicial sheaf to a fibrant simplicial sheaf;

3.  $Ex^{G}$  takes local fibrations to fibrations;

4. for any $\mathcal{X}$ the canonical morphism $\mathcal{X} \to Ex^{\mathcal{G}}(\mathcal{X})$ is a weak equivalence.

Proof. — For a simplicial sheaf $\mathcal{X}$ denote by $Ex^{sets} \mathcal{X}$ the simplicial sheaf associated to the simplicial presheaf of the form $\mathrm{U} \mapsto Ex^{\infty}(\mathcal{X}(\mathrm{U}))$ where $Ex^{\infty}$ is a resolution functor on the category of simplicial sets satisfying the conditions of Lemma 1.67 below (note that when the topology on T can be defined by a pretopology whose covering families are all finite $\mathrm{U} \mapsto Ex^{\infty}(\mathcal{X}(\mathrm{U}))$ is already a simplicial sheaf since $Ex^{\infty}$ commutes with finite limits). Let $\mathcal{L}$ be a conservative set of points of T. We set

$$
E x ^ {\mathcal {G}} (\mathcal {X}) = h o l i m _ {\Delta} \mathcal {G} _ {\mathcal {L}} ^ {\bullet} (E x ^ {s e t s} \mathcal {X}).
$$

The properties (1)-(4) for this functor follow immediately from Propositions 1.59, 1.65 and the fact that all the functors involved in the construction of $Ex^{\mathcal{G}}$ commute with finite limits.

Lemma 1.67. — There exists a functor $Ex^{\infty} : \Delta^{op}Sets \to \Delta^{op}Sets$ and a natural transformation $Id \to Ex^{\infty}$ such that the following conditions hold:

1. $Ex^{\infty}$ commutes with finite limits and in particular takes the final object to the final object;

2. $Ex^{\infty}$ takes Kan fibrations to Kan fibrations;

3. for any simplicial set X the map  $X \rightarrow Ex^{\infty}X$  is a monomorphism and a weak equivalence and  $Ex^{\infty}X$  is a Kan simplicial set.

Proof. — A purely combinatorial construction of  $Ex^{\infty}$  as a filtered colimit of functors right adjoint to certain subdivision functors can be found in [11, pp. 212-215].

## 2.2. A localization theorem for simplicial sheaves

## Basic definitions and main results

Let $\mathrm{T}$ be a small site and let $\mathrm{A}$ be a set of morphisms in $\mathcal{H}_s(\mathrm{T})$. Let us recall the standard notions of A-local objects and A-weak equivalences (cf [10] and [4, §7]).

Definition 2.1. — An object $\mathcal{X}$ of $\mathcal{H}_{s}(\mathrm{T})$ is called A-local if for any $\mathcal{Y}$ in $\mathcal{H}_{s}(\mathrm{T})$ and any $f\colon \mathcal{Z}_1\to \mathcal{Z}_2$ in A the map

$$
H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\boldsymbol {\mathcal {Y}} \times \mathcal {Z} _ {2}, \mathcal {X}) \rightarrow H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\boldsymbol {\mathcal {Y}} \times \mathcal {Z} _ {1}, \mathcal {X})
$$

is a bijection.

We write $\mathcal{H}_{s,\mathrm{A}}(\mathrm{T})$ for the full subcategory of A-local objects in $\mathcal{H}_s(\mathrm{T})$.

Definition 2.2. — A morphism $f: \mathcal{X}_{1} \to \mathcal{X}_{2}$ in $\Delta^{op}Shv(T)$ is called an A-weak equivalence if for any A-local object $\mathcal{Y}$ the map

$$
H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathcal {X} _ {2}, \mathcal {Y}) \rightarrow H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathcal {X} _ {1}, \mathcal {Y})
$$

induced by $f$ is a bijection.

Denote the class of A-weak equivalences by  $W_{A}$  and define the class of A-fibrations  $F_{A}$  as the class of morphisms with the right lifting property with respect to  $C \cap W_{A}$ . Observe that for any Y and any  $f: Z_{1} \to Z_{2}$  in A the map

$$
\boldsymbol {\mathcal {Y}} \times \mathcal {Z} _ {1} \rightarrow \boldsymbol {\mathcal {Y}} \times \mathcal {Z} _ {2}
$$

is an A-weak equivalence by definition.

Remark 2.3. — An object $\mathcal{E}$ is A-local if and only if for any A-weak equivalence $f\colon \mathcal{X} \to \mathcal{Y}$ the induced map $Hom_{\mathcal{H}_s(\mathrm{T})}(\mathcal{Y}, \mathcal{E}) \to Hom_{\mathcal{H}_s(\mathrm{T})}(\mathcal{X}, \mathcal{E})$ is bijective.

Remark 2.4. — Let $f'$ be the coproduct of all member of A and $A' = \{f'\}$. Then the notions of A'-local objects, A'-weak equivalences and A'-fibrations coincides with the corresponding notions associated to A. So that it is always possible to assume A has exactly one element.

The main result of this section is the following theorem.

Theorem 2.5. — For any set A the classes  $(\mathbf{W}_{\mathrm{A}}, \mathbf{F}_{\mathrm{A}}, \mathbf{C})$  define a model category structure on  $\Delta^{op}Shv(\mathrm{T})$ . The inclusion functor  $\mathcal{H}_{s,\mathrm{A}}(\mathrm{T}) \to \mathcal{H}_{s}(\mathrm{T})$  has a left adjoint  $L_{A}$  which identifies  $\mathcal{H}_{s,\mathrm{A}}(\mathrm{T})$  with the localization of  $\mathcal{H}_{s}(\mathrm{T})$  with respect to A-weak equivalences.

If A consists of one element f, the functor  $L_{A}$  will also be denoted by  $L_{f}$ .

Remark 2.6. — This theorem appears in [5, Th. 4.6] for T the category of sets. See also [10, §C. 2].

We also investigate the question of whether or not the A-model structure  $(\mathbf{W}_{\mathrm{A}}, \mathbf{F}_{\mathrm{A}}, \mathbf{C})$  is proper in the sense of [2, Definition 1.2]. We do not know the answer in general but we are able to prove the following result which is sufficient to demonstrate properness in the case of sites with intervals. We shall give a proof of the following result in §2.

Theorem 2.7. — For any set of morphisms A in $\mathcal{H}_{s}(\mathbf{T})$ the closed model structure $(\mathbf{W}_{\mathrm{A}}, \mathbf{F}_{\mathrm{A}}, \mathbf{C})$ is right proper. It is left proper if there exists a set $\widetilde{\mathbf{A}}$ of monomorphisms in $\Delta^{op}\text{Shv}(\mathbf{T})$ such that:

1. the image of $\widetilde{\mathbf{A}}$ in $Mor(\mathcal{H}_s(\mathbf{T}))$ coincides with A "up to isomorphisms";

2. for any $\mathcal{X}$ in $\Delta^{op}Shv(\mathbf{T})$, any morphism $f: \mathcal{Y} \to \mathcal{Z}$ in $\widetilde{\mathbf{A}}$ and any morphism $p: \mathcal{E} \to \mathcal{X} \times \mathcal{Z}$ in $\mathbf{F}_{\mathrm{A}}$ the projection

$$
\mathcal {E} \times_ {(\mathcal {X} \times \mathcal {Z})} (\mathcal {X} \times \mathcal {Y}) \rightarrow \mathcal {E}
$$

is in $\mathbf{W}_{\mathrm{A}}$

## Elementary properties of classes  $W_{A}$  and  $F_{A}$

All through this section  $\widetilde{A}$  denotes a set of monomorphisms in  $\Delta^{op}Shv(\mathbf{T})$  such that the image of  $\widetilde{A}$  in  $Mor(\mathcal{H}_{s}(\mathbf{T}))$  coincides with A (up to isomorphisms).

Lemma 2.8. — Let X be a simplicially fibrant object. Then the following conditions are equivalent:

1. $\mathcal{K}$ is A-local;

2. for any $f: \mathcal{Y} \to \mathcal{Z}$ in A the morphism of simplicial sheaves

$$
\underline {{H o m}} (\mathcal {Z}, \mathcal {K}) \rightarrow \underline {{H o m}} (\mathcal {Y}, \mathcal {X})
$$

induced by $f$ is a simplicial weak equivalence;

3. for any $f\colon \mathcal{Y}\to \mathcal{Z}$ in $\widetilde{\mathrm{A}}$ the morphism of simplicial sheaves

$$
\underline {{{H o m}}} (\mathcal {Z}, \mathcal {K}) \rightarrow \underline {{{H o m}}} (\mathcal {Y}, \mathcal {K})
$$

induced by $f$ is a simplicial trivial fibration;

4. for any $f\colon\mathcal{Y}\to\mathcal{Z}$ in $\widetilde{\mathrm{A}}$ and any object U of T the map of simplicial sets

$$
\mathrm{S} (\mathrm{U} \times \mathcal {Z}, \mathcal {X}) \rightarrow \mathrm{S} (\mathrm{U} \times \mathcal {Y}, \mathcal {X})
$$

is a trivial Kan fibration.

Proof. — The equivalence of the first three conditions is clear from definitions. The fact that the last one is equivalent to the second one follows from Lemma 1.10.

Proposition 2.9. — A morphism $\mathcal{X} \to \mathcal{X}'$ is an A-weak equivalence (resp. an A-weak equivalence and a cofibration) if and only if for any simplicially fibrant, A-local $\mathcal{Y}$ the morphism :

$$
\underline {{{H o m}}} (\mathcal {X} ^ {\prime}, \mathcal {Y}) \rightarrow \underline {{{H o m}}} (\mathcal {X}, \mathcal {Y})
$$

is a simplicial weak equivalence (resp. a trivial fibration).

Proof. — This is an easy reformulation (using adjointness) of the fact that if Y is simplicially fibrant, A-local then so is  $\underline{\text{Hom}}(\mathcal{Z}, \mathcal{Y})$  for any simplicial sheaf Z.

Lemmas 2.10 and 2.11 below which describe some basic properties of A-weak equivalences follow immediately from the criterion given in Proposition 2.9, Theorem 1.4, Remark 1.5 and standard facts about fibrations in proper model categories.

Lemma 2.10. — Consider a cocartesian square

$$
\begin{array}{c c c} \mathcal {X} & \stackrel {{a}} {{\longrightarrow}} & \mathcal {Y} \\ b \Big \downarrow & & \Big \downarrow d \\ \mathcal {X} ^ {\prime} & \stackrel {{c}} {{\longrightarrow}} & \mathcal {Y} ^ {\prime} \end{array}
$$

where a is a monomorphism. Then if b is an A-weak equivalence so is d and if a is an A-weak equivalence so is c.

Lemma 2.11. — Consider cocartesian squares

$$
\begin{array}{c c c} \mathcal {X} _ {i} & \stackrel {{a _ {i}}} {{\longrightarrow}} & \mathcal {Y} _ {i} \\ b _ {i} \Big \downarrow & & \Big \downarrow d _ {i} \\ \mathcal {X} _ {i} ^ {\prime} & \stackrel {{c _ {i}}} {{\longrightarrow}} & \mathcal {Y} _ {i} ^ {\prime} \end{array}
$$

i=1,2 such that  $a_{1}, a_{2}$  are monomorphisms and let  $f_{X}, f_{Y}, f_{X'}$ ,  $f_{Y'}$  be a morphism from the first square to the second such that  $f_{X}, f_{Y}, f_{X'}$  are A-weak equivalences. Then  $f_{Y'}$  is an A-weak equivalence.

The following lemma is an easy consequence of Proposition 2.9 and Lemmas 1.19, 1.21.

Lemma 2.12. — Let $\mathcal{I}$ be a (small) category, $\mathcal{X}$, $\mathcal{Y}$ be functors from $\mathcal{I}$ to $\Delta^{op}Shv(\mathrm{T})$ and $f$ a natural transformation $\mathcal{X} \to \mathcal{Y}$ such that all the morphisms $f_i$ are in $\mathbf{W}_{\mathrm{A}}$. Then the morphism $hocolim_{\mathcal{I}}\mathcal{X} \to hocolim_{\mathcal{I}}\mathcal{Y}$ is in $\mathbf{W}_{\mathrm{A}}$.

Corollary 2.13. — Let $\mathcal{I}$ be a right filtering (small) category, $\mathcal{X}$, $\mathcal{Y}$ be functors $\mathcal{I} \to \Delta^{\phi} Shv(T)$ and $f$ a natural transformation $\mathcal{X} \to \mathcal{Y}$. Then one has:

1. if for each morphism $i \to j$ in $\mathcal{I}$ the morphism $\mathcal{X}_i \to \mathcal{X}_j$ is in $\mathbf{W}_{\mathrm{A}}$, then for each $i \in \mathcal{I}$ the obvious morphisms $\mathcal{X}_i \to \operatorname{colim}_{\mathcal{I}} \mathcal{X}$ are also in $\mathbf{W}_{\mathrm{A}}$;

2. if for each $i \in \mathcal{I}$ the morphisms $f_i$ are in $\mathbf{W}_{\mathrm{A}}$, then the morphism $\operatorname{colim}_{\mathcal{I}}: \operatorname{colim}_{\mathcal{I}}\mathcal{X} \to \operatorname{colim}_{\mathcal{I}}\mathcal{Y}$ is in $\mathbf{W}_{\mathrm{A}}$.

Proof. — It is clear that the first point is a particular case of the second one (with X a constant functor). By Corollary 1.21 the morphisms  $hocolim_{T}X \rightarrow colim_{T}X$  and  $hocolim_{T}Y \rightarrow colim_{T}Y$  are weak equivalences and therefore our result follows from Lemma 2.12.

Proposition 2.14. — Let $\mathcal{K} \to \mathcal{Y}$ be a morphism of simplicial sheaves such that for any $n \geqslant 0$ the corresponding morphism of sheaves of sets $f_n: \mathcal{K}_n \to \mathcal{Y}_n$ is an A-weak equivalence. Then $f$ is an A-weak equivalence.

Proof. — Consider X and Y as diagrams of simplicial sheaves of simplicial dimension zero indexed by  $\Delta^{op}$ . The obvious morphisms

$$
h o c o l i m _ {\Delta^ {o p}} \mathcal {K} \rightarrow \mathcal {K}
$$

$$
h o c o l i m _ {\Delta^ {o p}} \mathcal {Y} \rightarrow \mathcal {Y}
$$

are weak equivalences by [3, XII.3.4] and our result follows from Lemma 2.12.

Lemma 2.15. — 1. Let $\mathcal{X} \to \mathcal{Y}$ be an A-weak equivalence and $\mathcal{Z}$ a simplicial sheaf. Then the morphism $\mathcal{X} \times \mathcal{Z} \to \mathcal{Y} \times \mathcal{Z}$ is an A-weak equivalence.

2. For any pair $(i: \mathcal{A} \to \mathcal{B}, j: \mathcal{X} \to \mathcal{Y})$ of cofibrations with either $i$ or $j$ in $\mathbf{W}_{\mathrm{A}}$, the obvious morphism:

$$
\mathrm{P} (i, j): (\mathcal {A} \times \mathcal {Y}) \amalg_ {\mathcal {A} \times \mathcal {X}} (\mathcal {B} \times \mathcal {X}) \rightarrow \mathcal {B} \times \mathcal {Y}
$$

is in $\mathbf{C} \cap \mathbf{W}_{\mathrm{A}}$.

Proof. — The first point follows formally from Proposition 2.9 and the fact that for any fibrant A-local E then Hom(Z, E) is again fibrant and A-local (which in turn follows directly from Definition 2.1). The second point is an easy exercice using the first point and Lemma 2.10.

The following simple result will be used in computations in Section 4.

Lemma 2.16. — Let C be a set of objects of Shv(T) satisfying the condition of Lemma 1.16 and $f: \mathbf{F} \to \mathbf{G}$ be a morphism of sheaves of sets on T such that for any X in C and any morphism $\mathbf{X} \to \mathbf{G}$ the projection $\mathbf{F} \times_{\mathbf{G}} \mathbf{U} \to \mathbf{X}$ is an A-weak equivalence. Then $f$ is an A-weak equivalence.

Proof. — By Lemma 1.16 we get a trivial local fibration (thus a weak equivalence) $\Phi_{\mathbf{C}}(\mathbf{G}) \to \mathbf{G}$ such that each of the terms $\Phi_{\mathbf{C}}(\mathbf{G})_n$ is a direct sum of sheaves in $\mathbf{C}$. By the assumption the morphism $\mathrm{F} \times_{\mathrm{G}} \Phi_{\mathbf{C}}(\mathbf{G}) \to \Phi_{\mathbf{C}}(\mathbf{G})$ is an A-weak equivalence termwise and thus is an A-weak equivalence by Proposition 2.14 which implies the statement of the lemma since the morphism $\mathrm{F} \times_{\mathrm{G}} \Phi_{\mathbf{A}}(\mathbf{G}) \to \mathrm{F}$ is a weak equivalence.

## A-model category structure theorem

We still assume throughout this section that  $\widetilde{A}$  denotes a set of monomorphisms in  $\Delta^{op}Shv(T)$  such that the image of  $\widetilde{A}$  in  $Mor(\mathcal{H}_{s}(T))$  coincides with A (up to isomorphisms).

For any $f\colon\mathcal{Y}\to\mathcal{Z}$ in $\widetilde{\mathbf{A}}$, any object U and $n\geqslant0$ in T, write (U,f,n) for the object given by the cocartesian square

$$
\begin{array}{c c c} \mathrm{U} \times \mathcal {Y} \times \partial \Delta^ {n} & \stackrel {{I d \times f \times I d}} {{\longrightarrow}} & \mathrm{U} \times \mathcal {Z} \times \partial \Delta^ {n} \\ \Big \downarrow & & \Big \downarrow \\ \mathrm{U} \times \mathcal {Y} \times \Delta^ {n} & \longrightarrow & (\mathrm{U}, f, n) \end{array}
$$

and by  $i_{(\mathrm{U},f,n)}:(\mathrm{U},f,n)\to\mathrm{U}\times\mathcal{Z}\times\Delta^{n}$  be the obvious monomorphism. Denote the set of morphisms of the form  $i_{(\mathrm{U},f,n)}$  by  $B_{1}$ . Note that Lemma 2.10 implies that  $B_{1}\subset C\cap W_{A}$ .

Lemma 2.17. — Let $\mathcal{K}$ be a fibrant simplicial sheaf. Then the following conditions are equivalent

1. $\mathcal{K}$ is A-local

2. the projection $\mathcal{K} \to pt$ has the right lifting property with respect to morphisms in $\mathbf{B}_1$.

Proof. — Observe that the second condition holds if and only if for any  $U \in T$  and any  $(f: \mathcal{Y} \to \mathcal{Z}) \in \widetilde{\mathbf{A}}$  the morphism of simplicial sets  $S(U \times \mathcal{Z}, \mathcal{X}) \to S(U \times \mathcal{Y}, \mathcal{X})$  has the right lifting property with respect to embeddings  $\partial\Delta^{n} \to \Delta^{n}$ , i.e. if and only if this morphism is a trivial fibration of simplicial sets. Since X is fibrant and f is a monomorphism this morphism is always a fibration which implies the required equivalence by Lemma 2.8.4).

Corollary 2.18. — There exists a set (as opposed to a class) B of morphisms in  $C \cap W_{A}$  such that for any simplicial sheaf X, if the projection  $X \rightarrow pt$  has the right lifting property with respect to morphisms in B then X is A-local.

Proof. — As was shown by Jardine ([18, Lemma 2.4]) there exists a subset  $B_{0}$  in  $C \cap W_{s}$  such that X is simplicially fibrant if and only if the projection  $X \to pt$  has the right lifting property with respect to morphisms in  $B_{0}$ . In view of Lemma 2.17 it is sufficient to take B to be  $B_{0} \cup B_{1}$ .

Let B be a set of morphisms in  $C \cap W_{A}$ . For a morphism f denote by  $S_{f}$  its source and by  $T_{f}$  its target. Define a functor  $\Phi_{\mathrm{B}}^{0} : \Delta^{op}Shv(\mathrm{T}) \to \Delta^{op}Shv(\mathrm{T})$  such that for a simplicial sheaf X the object  $\Phi_{\mathrm{B}}^{0}(\mathcal{X})$  is given by the cocartesian square

$$
\begin{array}{c c c} \coprod_ {f \in B} \coprod_ {g \in H o m (S _ {f}, \mathcal {K})} S _ {f} & \longrightarrow & \mathcal {K} \\ \Big \downarrow & & \Big \downarrow \\ \coprod_ {f \in B} \coprod_ {g \in H o m (S _ {f}, \mathcal {K})} T _ {f} & \longrightarrow & \Phi_ {\mathrm{B}} ^ {0} (\mathcal {K}) \end{array}
$$

and denote $\iota_{\mathcal{X}}: \mathcal{X} \to \Phi_{\mathrm{B}}^{0}(\mathcal{X})$ the canonical morphism. Observe that $\iota_{\mathcal{X}}$ is an A-weak equivalence by 2.10.

For any ordinal number $\omega$ let's define as usual the iteration $(\Phi_{\mathrm{B}}^{0})^{\omega}$ of the previous functor; in fact one defines a functor from the ordered set of ordinal numbers $\gamma \leqslant \omega$ to the "category" of functors. One proceeds by transfinite induction, requiring that if $\gamma = \gamma' + 1$ then $(\Phi_{\mathrm{B}}^{0})^{\gamma} = \Phi_{\mathrm{B}}^{0}((\Phi_{\mathrm{B}}^{0})^{\gamma'})$ and if $\gamma$ is a limit ordinal then $(\Phi_{\mathrm{B}}^{0})^{\gamma} = colim_{\gamma' < \gamma}(\Phi_{\mathrm{B}}^{0})^{\gamma'}$. Observe that for ordinals $\gamma' < \gamma$ one has a natural transformation $(\Phi_{\mathrm{B}}^{0})^{\gamma'} \to (\Phi_{\mathrm{B}}^{0})^{\gamma}$ whose value on a simplicial sheaf is an A-weak equivalence (2.13).

Let $\alpha$ be a cardinal number and $\mathcal{T}$ an ordered set; we shall write $\mathcal{T} \geqslant \alpha$ if any subset of $\mathcal{T}$ of cardinal $\leqslant \alpha$ has an upper bound. Denote $Seq[\alpha]$ the well-ordered set consisting of ordinal numbers $\gamma$ whose cardinality is strictly less than $\alpha$. Then if $\beta$ is a cardinal number $< \alpha$ the ordered set $Seq[\alpha]$ satisfies $Seq[\alpha] \geqslant \beta$.

Recall [13, I. Definition 9.3] the notion of accessible object in $\Delta^{op}Shv(T)$ (this notion is stronger than the notion of $s$-definite object from [4, §4.2]). A simplicial sheaf $\mathcal{X}$ is called accessible if there is an cardinal number $\alpha_{\mathcal{X}}$ such that for any functor $\mathcal{Y}: \mathcal{T} \to \Delta^{op}Shv(T)$, with $\mathcal{T}$ an ordered set $\geqslant \alpha_{\mathcal{X}}$, the map:

$$
\operatorname{colim} _ {i \in \mathcal {T}} \operatorname{Hom} _ {\Delta^ {o p} S h v (\mathrm{T})} (\mathscr {X}, \mathscr {Y} _ {i}) \rightarrow \operatorname{Hom} _ {\Delta^ {o p} S h v (\mathrm{T})} (\mathscr {X}, \operatorname{colim} _ {\mathcal {T}} \mathscr {Y})
$$

is bijective. Any object in $\Delta^{op}Shv(T)$ is accessible by [13, I. Rem. 9.11.3]. Let $\omega$ be a cardinal number such that, for any $f\in B$, $\alpha_{S_f}<\omega$. Then $Seq[\omega]\geqslant\alpha_{S_f}$ for any $f\in B$. Set

$$
\Phi_ {\mathrm{B}, \omega} := (\Phi_ {\mathrm{B}} ^ {0}) ^ {S e q [ \omega ]}.
$$

The following result follows easily from 2.17 and from what we said above (it is essentially a restatement of [4, Corollary 7.2]).

Proposition 2.19. — Let B be a set of morphisms satisfying the conclusion of lemma 2.18. Then for $\omega$ as above, the functor $\Phi_{\mathrm{B},\omega}:\Delta^{op}\mathrm{Shv}(\mathrm{T})\to \Delta^{op}\mathrm{Shv}(\mathrm{T})$ takes values in the subcategory of A-local fibrant objects and for any $\mathcal{X}$ the canonical morphism $i:\mathcal{X}\to \Phi_{\mathrm{B},\omega}(\mathcal{X})$ is a cofibration and an A-weak equivalence.

The functor  $\Phi_{B}$  sends an A-weak equivalence to a weak equivalence and the induced functor

$$
\mathrm{L} _ {\mathrm{A}}: \mathcal {H} _ {s} (\mathrm{T}) \rightarrow \mathcal {H} _ {s, \mathrm{A}} (\mathrm{T})
$$

is left adjoint to the inclusion $\mathcal{H}_{s,\mathrm{A}}(\mathrm{T})\to \mathcal{H}_s(\mathrm{T})$

Observe now that the functor $\Phi_{\mathrm{B}}^{0}$ commutes with (filtering) colimits of functors $\mathcal{Y}:\mathcal{T}\to \Delta^{op}Shv(\Gamma)$, with $\mathcal{T}$ an ordered set such that $\mathcal{T}\geqslant \alpha_{\mathrm{S}_f}$ for any $f\in \mathbf{B}$. Thus $\Phi_{\mathrm{B},\omega}$ does also (as any ordinal composition of $\Phi_{\mathrm{B}}^{0}$). Check this by transfinite induction.

Using Proposition 2.19 and this observation, one deduces the following technical result using an argument similar to the one in the proof of [18, Lemma 2.4] (see also [4, 4.7]).

Corollary 2.20. — There exists a set (as opposed to a class) $\mathbf{B}'$ of morphisms in $\mathbf{C} \cap \mathbf{W}_{\mathrm{A}}$ such that a morphism $\mathcal{X} \to \mathcal{Y}$ is in $\mathbf{F}_{\mathrm{A}}$ if and only if it has the right lifting property with respect to morphisms in $\mathbf{B}'$.

Theorem 2.21. — The triple  $(\mathbf{W}_{\mathrm{A}}, \mathbf{C}, \mathbf{F}_{\mathrm{A}})$  is a model category structure on  $\Delta^{op}Shv(\mathrm{T})$ .

Proof. — The axioms MC1-MC3 are obvious from the definitions. The (trivial cofibration)/(fibration) part of MC4 is the definition of  $F_{A}$ . The (cofibration)/(trivial fibration) part of MC5 follows immediately from the corresponding fact in the simplicial case since an trivial fibration is a trivial A-fibration. The (trivial cofibration)/(fibration) part of the axiom MC5 follows by the transfinite analog of the small object argument from Corollary 2.20 in exactly the same way as in [18, Lemma 2.5]. The (cofibration)/(trivial fibration) part of MC4 follows from MC5 and Lemma 2.10 by Joyal trick (see [18, p. 64]).

Theorem 2.21 finishes the proof of Theorem 2.5.

Remark 2.22. — The A-model category structure ( $W_{A}$ , C,  $F_{A}$ ) is an enriched structure (cf [16, B.3]) for the monoidal structure given by the categorical product by Lemma 2.15(1).

## Properness theorem

In this section we shall prove Theorem 2.7. Again, let  $\widetilde{A}$  be a set of representatives for morphisms in A which satisfies the conditions of this theorem. We begin by establishing a number of technical results describing different properties of the classes  $W_{A}$  and  $F_{A}$  which are necessary for the proof of Theorem 2.7.

Proposition 2.23. — Let $p: \mathcal{E} \to \mathcal{B}$ be a fibration such that $\mathcal{B}$ is fibrant and suppose that for any commutative diagram of the form

$$
\begin{array}{c c c} \mathcal {E} & \stackrel {{I d}} {{\longrightarrow}} & \mathcal {E} \\ i \Big \downarrow & & \Big \downarrow^ {p} \\ \mathcal {Y} & \longrightarrow & \mathcal {B} \end{array}
$$

in $\mathcal{H}_s(\mathrm{T})$ such that $i$ is in $\mathbf{W}_{\mathrm{A}}$, there exists a morphism $\mathcal{Y} \to \mathcal{E}$ which makes the corresponding two triangles commutative. Then $p$ is an A-fibration.

Proof. — Consider a commutative square

$$
\begin{array}{c c c} \mathcal {X} & \longrightarrow & \mathcal {E} \\ i \Big \downarrow & & \Big \downarrow_ {p} \\ \mathcal {Y} & \longrightarrow & \mathcal {B} \end{array}
$$

in $\Delta^{op}Shv(T)$ such that $i$ is in $\mathbf{W}_{\mathrm{A}} \cap \mathbf{C}$. We have to construct a morphism $\mathcal{Y} \to \mathcal{E}$ which makes the two triangles commutative. By Lemma 2.10 we may replace $\mathcal{Y}$ by the coproduct $\mathcal{E} \amalg_{\mathcal{X}} \mathcal{Y}$ and assume that the upper horizontal arrow is identity. By our condition on $p$ there exists a morphism $\mathcal{Y} \to \mathcal{E}$ in $\mathcal{H}_s(T)$ which makes the two triangles commutative. Applying Lemma 2.24 below to the corresponding diagram in the opposite category $(\Delta^{op}Shv(T))^{op}$ we get a morphism with the required property in $\Delta^{op}Shv(T)$.

Lemma 2.24. — Consider a commutative square in a model category $\mathcal{C}$ of the form

$$
\begin{array}{c c c} \mathbf {X} & \stackrel {{a}} {{\longrightarrow}} & \mathbf {E} \\ i \Big \downarrow & & \Big \downarrow^ {p} \\ \mathbf {B} & \stackrel {{I d}} {{\longrightarrow}} & \mathbf {B} \end{array}
$$

such that p is a fibration, i is a cofibration, X is cofibrant and B is fibrant. Suppose that there exists a morphism  $f: B \to E$  in  $\mathcal{H}(C)$  which makes the corresponding two triangles commutative. Then f can be represented by a morphism with the same property in C.

Proof. — It follows from our conditions that B is cofibrant and E is fibrant and therefore f can be represented by a morphism in C. Let

$$
\mathbf {X} \coprod \mathbf {X} \stackrel {i _ {0}} {\longrightarrow} \coprod^ {i _ {1}} C y l (\mathbf {X}) \rightarrow \mathbf {X}
$$

be a decomposition of the morphism $Id \coprod Id$ into a cofibration and a trivial fibration (i.e. $Cyl(X)$ is a “good cylinder” object for X, see [26]). Then there is a morphism $G: Cyl(X) \to E$ such that the diagrams

$$
\begin{array}{c c c c c c} \mathbf {X} & \stackrel {{a}} {{\longrightarrow}} & \mathbf {E} \\ i _ {0} \Big \downarrow & \nearrow_ {\mathrm{G}} & & & \mathbf {X} & \stackrel {{i}} {{\longrightarrow}} & \mathbf {B} \\ C y l (\mathbf {X}) & & & & i _ {1} \Big \downarrow & & \Big \downarrow_ {g} \\ & & & & C y l (\mathbf {X}) & \stackrel {{G}} {{\longrightarrow}} & \mathbf {E} \end{array}
$$

commute (because a is, by hypothesis, homotopic to  $g \circ i$ ). Define  $X'$  and  $X''$  by the cocartesian squares

$$
\begin{array}{c c c c c c} \mathbf {X} & \stackrel {{i}} {{\longrightarrow}} & \mathbf {B} & \mathbf {X} & \stackrel {{i}} {{\longrightarrow}} & \mathbf {B} \\ _ {i _ {1}} \Big \downarrow & & \Big \downarrow & _ {j \circ i _ {0}} \Big \downarrow & & \Big \downarrow^ {q} \\ C y l (\mathbf {X}) & \stackrel {{j}} {{\longrightarrow}} & \mathbf {X ^ {\prime}} & \mathbf {X ^ {\prime}} & \longrightarrow & \mathbf {X ^ {\prime \prime}}. \end{array}
$$

We have a canonical morphism  $X^{\prime} \rightarrow X^{\prime\prime} \rightarrow B$  which is a weak equivalence since it splits the trivial cofibration  $B \rightarrow X^{\prime}$ . Decompose the last arrow into a cofibration  $X^{\prime\prime} \rightarrow X^{\prime\prime\prime}$  and a trivial fibration  $X^{\prime\prime\prime} \rightarrow B$ . We have a commutative diagram

$$
\begin{array}{c c c} \mathrm {X^ {\prime}} & \longrightarrow & \mathrm{E} \\ \Big \downarrow & & \\ \mathrm {X^ {\prime\prime}} & & \Big \downarrow \\ \Big \downarrow & & \\ \mathrm {X^{\prime\prime\prime}} & \longrightarrow & \mathrm{B} \end{array}
$$

where the composition of the two left vertical arrows is a trivial cofibration. Therefore there exists a morphism  $X''' \rightarrow E$  which makes the corresponding two triangles commutative. One can easily see now that the composition  $B \stackrel{q}{\rightarrow} X'' \rightarrow X''' \rightarrow E$  is a morphism in C with the required property.

Corollary 2.25. — Let $p: \mathcal{E} \to \mathcal{B}$ be a fibration such that the objects $\mathcal{E}, \mathcal{B}$ are A-local and fibrant. Then $p$ is a A-fibration.

Proposition 2.26. — Let $p: \mathcal{E} \to \mathcal{B}$ be an A-fibration. Then for any commutative diagram in $\mathcal{H}_{s}(\mathrm{T})$ of the form

$$
\begin{array}{c c c} \mathcal {X} & \longrightarrow & \mathcal {E} \\ i \Big \downarrow & & \Big \downarrow_ {p} \\ \mathcal {Y} & \longrightarrow & \mathcal {B} \end{array}
$$

such that $i$ is in $\mathbf{W}_{\mathrm{A}}$ there exists a morphism $\mathcal{Y} \to \mathcal{E}$ which makes the corresponding two triangles commutative.

Proof. — Let  $j_{B}: B \to B'$  be a trivial cofibration such that  $B'$  is fibrant. Taking a decomposition of  $j_{B} \circ p$  into a trivial cofibration and a fibration we get a

commutative square

$$
\begin{array}{c c c} \mathcal {E} & \stackrel {{j _ {E}}} {{\longrightarrow}} & \mathcal {E} ^ {\prime} \\ p \Big \downarrow & & \Big \downarrow p ^ {\prime} \\ \mathcal {B} & \stackrel {{j _ {B}}} {{\longrightarrow}} & \mathcal {B} ^ {\prime} \end{array}
$$

where the vertical arrows are fibrations and the horizontal ones are trivial cofibrations. Our diagram in  $\mathcal{H}_{s}(\mathrm{T})$  may be represented now by a diagram of the form

$$
\begin{array}{c c c} \mathcal {X} & \stackrel {{f}} {{\longrightarrow}} & \mathcal {E} ^ {\prime} \\ i \Big \downarrow & & \Big \downarrow p ^ {\prime} \\ \mathcal {Y} & \stackrel {{g}} {{\longrightarrow}} & \mathcal {B} ^ {\prime} \end{array}
$$

in $\Delta^{op}Shv(T)$ such that $i$ is in $\mathbf{C} \cap \mathbf{W}_{\mathrm{A}}$. We have to construct a morphism $\mathcal{Y} \to \mathcal{E}'$ in $\mathcal{H}_s(T)$ which makes the two triangles commutative. By Lemma 2.10 we may replace $\mathcal{Y}$ be the coproduct $\mathcal{Y} \amalg_{\mathcal{X}} \mathcal{E}'$ and thus assume that $f$ is the identity morphism. We may also decompose $g$ into a trivial cofibration and a fibration and further assume that $g$ is a fibration. Considering the base change along the morphism $j_{\mathrm{B}}$ we get the diagram

$$
\begin{array}{c c c} \mathcal {E} & \stackrel {{I d}} {{\longrightarrow}} & \mathcal {E} \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {E} ^ {\prime} \times_ {\mathcal {B}}, \mathcal {B} & \stackrel {{I d}} {{\longrightarrow}} & \mathcal {E} ^ {\prime} \times_ {\mathcal {B}}, \mathcal {B} \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {Y} \times_ {\mathcal {B}}, \mathcal {B} & \longrightarrow & \mathcal {B} \end{array}
$$

where the right vertical arrow is p. Since  $\Delta^{op}Shv(T)$  is a proper model category the big square of this diagram is isomorphic to the original one in  $\mathcal{H}_{s}(T)$  and in particular the left vertical arrow is in  $W_{A}$ . Decomposing it into a cofibration and a trivial fibration and using the fact that p is an A-fibration we get a morphism  $Y \to E$  in  $\mathcal{H}_{s}(T)$  with the required property.

Combining Propositions 2.23 and 2.26 we get the following corollary.

Corollary 2.27. — Let $p: \mathcal{E} \to \mathcal{B}$ be a fibration such that B is fibrant and suppose that p is isomorphic in $\mathcal{H}_s(\mathrm{T})$ to an A-fibration. Then p is an A-fibration.

Proposition 2.28. — Let E be a fibrant simplicial sheaf. Then the following conditions are equivalent:

1. $\mathcal{E}$ is A-fibrant;

2. $\mathcal{E}$ is A-local.

Proof. — The fact that the second condition implies the first is a particular case of Corollary 2.25. To show that the first one implies the second it is sufficient in view of Lemma 2.8 to verify that if we have a morphism $i: \mathcal{X} \to \mathcal{Y}$ in $\mathbf{C} \cap \mathbf{W}_{\mathrm{A}}$ then the morphism $\underline{\text{Hom}}(\mathcal{Y}, \mathcal{E}) \to \underline{\text{Hom}}(\mathcal{X}, \mathcal{E})$ is a trivial fibration. This follows from Lemma 2.15, by adjointness.

Let us now assume that  $\widetilde{A}$  satisfies the conditions of theorem 2.7.

Lemma 2.29. — Let $\mathcal{X}$ be a simplicial sheaf and $\mathcal{E} \to \Phi(\mathcal{X})$ be a morphism in $\mathbf{F}_{\mathrm{A}}$. Then the projection $\mathcal{X} \times_{\Phi(\mathcal{X})} \mathcal{E} \to \mathcal{E}$ is in $\mathbf{W}_{\mathrm{A}} \cap \mathbf{C}$.

Proof. — Consider the class G of morphisms  $X \to Y$  in  $W_{A} \cap C$  such that for any A-fibration  $E \to Y$  the projection  $X \times Y E \to E$  is in  $W_{A} \cap C$ . This class has the following properties:

1. if two out of three morphisms $f, g, f \circ g \in \mathbf{C} \cap \mathbf{W}_{\mathrm{A}}$ are in $\mathbf{G}$ then so is the third;

2. G is closed under filtering colimits (by Corollary 2.13);

3. G is closed under arbitrary direct sums;

4. G is closed under cobase change (by Lemma 2.10);

5. G contains  $C \cap W_{s}$  (since the simplicial model structure is proper and  $F_{A} \subset F_{s}$ );

6. G contains  $\widetilde{A}$  (by assumption).

The statement of the proposition follows easily from these properties, the construction of the functor  $\Phi$  and the definition of the class B given in the proof of Corollary 2.18.

Lemma 2.30. — Let $p: \mathcal{E} \to \mathcal{B}$ be an A-fibration. Then there exists an A-fibration $\mathcal{E}' \to \Phi(\mathcal{B})$ such that $p$ is an B-deformational retract of $\mathcal{E}' \times_{\mathcal{B}} \Phi(\mathcal{B})$.

Proof. — By Theorem 2.21 we can construct a commutative square of the form

$$
\begin{array}{c c c} \mathcal {E} & \longrightarrow & \mathcal {E} ^ {\prime} \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {B} & \longrightarrow & \Phi (\mathcal {B}) \end{array}
$$

such that the upper horizontal arrow is in  $C \cap W_{A}$  and the right vertical one is an A-fibration. Using Lemma 2.29 we conclude immediately that the canonical morphism  $s: E \to E' \times_{\Phi(\mathcal{B})} B$  is in  $C \cap W_{A}$ . Since both objects are fibrant over B we conclude that there is a morphism  $f: E' \times_{\Phi(\mathcal{B})} B \to E$  over B such that  $f \circ s = Id$ . Applying

the right lifting property of the A-fibration $f \colon \mathcal{E}' \times_{\Phi(\mathcal{B})} \mathcal{B} \to \mathcal{B}$ to the A-acyclic cofibration $\mathrm{P}(s, \partial \Delta^1 \subset \Delta^1)$ we get a homotopy (over $\mathcal{B}$) from $s \circ p$ to $Id_{\mathcal{E}' \times_{\Phi(\mathcal{B})'} \mathcal{B}}$ (cf Lemma 2.15).

To finish the proof of Theorem 2.7 we have to show that for any cartesian square

$$
\begin{array}{c c c} \mathcal {X} _ {1} & \longrightarrow & \mathcal {X} _ {2} \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {X} _ {3} & \longrightarrow & \mathcal {X} _ {4} \end{array}
$$

such that the right vertical arrow is in  $F_{A}$  and the lower horizontal one is in  $W_{A}$ , the upper horizontal one is also in  $W_{A}$ . Using Lemma 2.30 we see it is sufficient to prove the result in the case when there exists a cartesian square of the form

$$
\begin{array}{c c c} \mathcal {X} _ {2} & \longrightarrow & \mathcal {E} \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {X} _ {4} & \longrightarrow & \Phi (\mathcal {X} _ {4}). \end{array}
$$

The morphism  $X_{3} \to \Phi(X_{4})$  factors through the morphism  $\Phi(X_{3}) \to \Phi(X_{4})$  which is a simplicial weak equivalence since both objects are A-local. Our result follows now from the fact that the simplicial model structure is proper and Lemma 2.29.

## Localization of loop spaces

Let $Shv(T)_{\bullet}$ (resp. $\Delta^{op}Shv(T)_{\bullet}$) be the category of pointed sheaves (resp. simplicial pointed sheaves) of sets on T whose objects are pairs $(\mathbf{X}, x)$ consisting of a sheaf (resp. simplicial sheaf) of sets X together a morphism $x: pt \to X$. Note that pointed sheaves of sets and sheaves of pointed sets are two different names for the same type of objects.

Let us say that a morphism of pointed simplicial sheaves is a fibration, cofibration or weak equivalence (simplicial) if it belongs to the corresponding class as a morphism of sheaves without base points. This definition clearly provides us with a model category structures which we will call the simplicial model category structures on  $\Delta^{op}Shv_{\mathcal{Nis}}(Sm/S)$ . We denote the corresponding homotopy categories by  $\mathcal{H}_{\bullet}^{s}(T)$ .

Recall that the left adjoint to the forgetfull functor $\Delta^{op}Shv(T)_{\bullet}\to \Delta^{op}Shv(T)$ is the functor $\mathcal{X}\mapsto \mathcal{X}_{+}$ where $\mathcal{X}_{+}$ is the simplicial sheaf $\mathcal{X}\amalg pt$ pointed by the canonical embedding $pt\rightarrow \mathcal{X}\amalg pt$. Both functors preserve weak equivalences and thus induce a pair of adjoint functors between $\mathcal{H}_{\bullet}^{s}((Sm / S)_{Nis})$ and $\mathcal{H}_s((Sm / S)_{Nis})$.

For pointed simplicial sheaves  $(\mathcal{X}, x)$ ,  $(\mathcal{Y}, y)$  define their wedge  $(\mathcal{X}, x) \vee (\mathcal{Y}, y)$  and their smash product  $(\mathcal{X}, x) \wedge (\mathcal{Y}, y)$  in the usual way

$$
\begin{array}{l} (\mathcal {X}, x) \lor (\mathcal {Y}, y) = (\mathcal {X} \amalg_ {p t} \mathcal {Y}, x = y) \\ (\mathcal {X}, x) \wedge (\mathcal {Y}, y) = (\mathcal {X} \times \mathcal {Y} / (\mathcal {X}, x) \lor (\mathcal {Y}, y), x \times y). \end{array}
$$

Note that  $(\mathcal{X}, x) \vee (\mathcal{Y}, y)$  is the sheaf associated to the presheaf which takes an object U of T to the wedge of pointed simplicial sets  $(\mathcal{X}(U), x_{U})$  and  $(\mathcal{Y}(U), y_{U})$  and  $(\mathcal{X}, x) \wedge (\mathcal{Y}, y)$  is the sheaf associated to the presheaf which takes an object U of T to the smash product of pointed simplicial sets  $(\mathcal{X}(U), x_{U})$  and  $(\mathcal{Y}(U), y_{U})$ .

The functor $\Delta^{op}Shv(T)_{\bullet}\to \Delta^{op}Shv(T)_{\bullet},(\mathcal{X},x)\mapsto (\mathcal{X},x)\wedge (\mathcal{Y},y)$ has as right adjoint the functor $(\mathcal{Z},z)\mapsto \underline{Hom}_{\bullet}((\mathcal{Y},y),(\mathcal{Z},z))$ whose value is the fiber over the base point of $\mathcal{Z}$ of the evaluation morphism $y^{*}:\underline{Hom} (\mathcal{Y},\mathcal{Z})\to \underline{Hom}(pt,\mathcal{Z})\cong \mathcal{Z}$.

Let $S_{s}^{1}$ denote the constant pointed simplicial sheaf corresponding to the simplicial circle $\Delta^{1}/\partial\Delta^{1}$ (pointed by the image of $\partial\Delta^{1}$). We define the suspension functor on the category $\Delta^{op}Shv_{Nis}(Sm/S)$. of pointed simplicial sheaves setting:

$$
\Sigma_ {s} (\mathcal {K}, x) = \mathrm{S} _ {s} ^ {1} \wedge (\mathcal {K}, x).
$$

Let $\Omega_s^1(-) := \underline{Hom}_{\bullet}(\mathbf{S}_s^1, -)$ be the right adjoint to $\Sigma_s(-)$. We denote $\mathbf{R}\Omega_s^1(-)$ the total right derived functor of $\Omega_s^1(-)$ which is given by $\Omega_s^1 \circ Ex$ for a chosen resolution functor $Ex$ (1.6); it is right adjoint to the suspension functor in the pointed simplicial homotopy category.

Let $f: \mathbf{A} \to \mathbf{B}$ be a morphism of simplicial sheaves. Denote by $\Sigma_s(f_+)$ the suspension of the pointed morphism $f_+: \mathbf{A}_+ \to \mathbf{B}_+$. The proof of the following lemma is straightforward.

Lemma 2.31. — Let E be a pointed connected fibrant simplicial sheaf. The following conditions are equivalent:

1. $\mathcal{E}$ is $\Sigma_s(f_+) - local$;

2. the (pointed) simplicial sheaf $\Omega_s^1 (\mathcal{E})$ is $f$-local.

Moreover, if $f$ is pointed, these conditions are also equivalent to the following one:

$\mathcal{E}$ is $\Sigma_s(f)$-local.

As a corollary, we see that any f-local pointed connected simplicial sheaf E is also  $\Sigma_{s}f_{+}$ -local. Indeed,  $\mathbf{R}\Omega_{s}^{1}(\mathcal{E})$  is again f-local.

Lemma 2.32. — For any simplicial sheaf of groups G there is a morphism of simplicial sheaves of groups  $G' \rightarrow G$  which is a weak equivalence (as morphism of simplicial sheaves of sets) and a morphism of simplicial sheaves of groups  $G' \rightarrow H$  which is an f-weak equivalence (as morphism of simplicial sheaves of sets) and such that H is f-local (as a simplicial sheaf of sets).

This lemma is just [10, 3 Lemma A.3] in the case $\mathrm{T} = \text{Sets}$.

Remark 2.33. — The statement of the lemma could be made more functorial, as one can see by looking at the proof.

Proof. — Denote  $\underline{\mathbf{B}}(\mathbf{G})$  the bisimplicial sheaf of sets  $(n,m)\mapsto\mathbf{B}(\mathbf{G}_{m})_{n}$  (so that  $\underline{\mathbf{B}}(\mathbf{G})_{n,*}\cong\mathbf{G}^{n}$ ). Then applying the functor  $\Phi:=\Phi_{B}$  from Proposition 2.19 (applied with  $A=\{f\}$ ) we get a new bisimplicial sheaf  $\Phi(\underline{\mathbf{B}}(\mathbf{G}))$  with  $\Phi(\underline{\mathbf{B}}(\mathbf{G}))_{0,*}=\Phi(pt)$  weakly equivalent to pt, and such that for each  $n\geqslant2$, the morphisms:

$$
\Pi_ {i = 1, \dots , n} \Phi (p r _ {i}): \Phi (\underline {{\mathbf {B}}} (\mathbf {G}) _ {n}) \rightarrow (\Phi (\underline {{\mathbf {B}}} (\mathbf {G})) _ {1}) ^ {n}
$$

are simplicial weak equivalences because the localization functor obviously commutes with finite products in the homotopy category. From [27, Proposition 1.5], the fact that $\Phi(G)$ is a group object in the homotopy category (because the $f$-localization functor commutes to finite products in the homotopy category) and the fact that the functor $\mathbf{R}\Omega_s^1$ commutes with restriction to points of the site, we get that the morphism of simplicial sheaves

$$
\Phi (\mathbf {G}) \to \mathbf {R} \Omega_ {s} ^ {1} (D i a g (\Phi (\underline {{\mathbf {B}}} (\mathbf {G}))))
$$

(induced by the morphisms $\Sigma_s(\Phi(G)) \to \text{Diag}(\Phi(\underline{\mathbf{B}}(G)))$, where Diag means the diagonal simplicial sheaf of a bisimplicial sheaf) is a simplicial weak equivalence.

Denote $Gr(T)$ the category of sheaves of groups on T, $\Delta^{op}Shv(T)_0$ that of 0-reduced simplicial sheaves (meaning simplicial sheaves $\mathcal{X}$ with $\mathcal{X}_0 = pt$) and $\mathrm{G}(-):\Delta^{op}Shv(T)_0\to \Delta^{op}Gr(T)$ the (obvious analogue of the) Kan construction functor [22]. Then $Diag(\Phi (\underline{\mathrm{B}} (\mathrm{G})))$ is pointed connected, thus weakly equivalent to a 0-reduced simplicial sheaf $\mathcal{X}$, so that the canonical morphism $\mathrm{B(G)}\rightarrow Diag(\Phi (\underline{\mathrm{B}} (\mathrm{G})))$ is isomorphic in the pointed homotopy category of simplicial sheaves to a (pointed) morphism $\mathrm{B(G)}\rightarrow \mathcal{X}$ (thus $\mathrm{G}(\mathcal{X})$ is weakly homotopy equivalent to $\mathbf{R}\Omega_s^1 (Diag(\Phi (\underline{\mathrm{B}} (\mathrm{G}))))$). Moreover there is a morphism (of simplicial sheaves of groups) $\mathrm{G(B(G))}\to \overline{\mathrm{G}}$ which is a weak equivalence and the induced morphism (in the pointed homotopy category) $\mathrm{G}\rightarrow \mathbf{R}\Omega_s^1 (Diag(\Phi (\underline{\mathrm{B}} (\mathrm{G}))))$ is the previous one, as required.

Theorem 2.34. — For any pointed morphism $f$ and any pointed connected simplicial sheaf $\mathcal{K}$, the simplicial sheaf $\mathrm{L}_{\Sigma_s(f)}(\mathcal{K})$ is connected. From Lemma 2.31 $\mathbf{R}\Omega_s^1\mathrm{L}_{\Sigma_s(f)}(\mathcal{K})$ is thus $f$-local. Then the canonical induced morphism:

$$
\mathrm{L} _ {f} \left(\mathbf {R} \boldsymbol {\Omega} _ {s} ^ {1} (\mathcal {X})\right)\rightarrow \mathbf {R} \boldsymbol {\Omega} _ {s} ^ {1} \mathrm{L} _ {\Sigma_ {s} (f)} (\mathcal {X}).
$$

is a weak equivalence.

In the case $\mathrm{T} = \text{Sets}$ this theorem was proven by Bousfield and independently by Dror [10, 3. Theorem A.1].

Proof. — One may assume $\mathcal{K}$ 0-reduced and set $\mathrm{G} := \mathrm{G}(\mathcal{K})$. Let $\mathrm{G}' \to \mathrm{G}$ and $\mathrm{G}' \to \mathrm{H}$ be given by Lemma 2.32. From Lemma 2.31 BH is $\Sigma_s(f)$-local and moreover, using Lemma 2.35 below, one knows that the morphism $\mathrm{B}(\mathrm{G}') \to \mathrm{B}(\mathrm{H})$ is a $\Sigma_s(f)$-weak

equivalence which thus gives the  $\Sigma_{s}(f)$ -localization of  $\mathbf{B}(\mathbf{G}')$ , which is the same as that of X.

Lemma 2.35. — Let $f: \mathbf{M}_{1} \to \mathbf{M}_{2}$ be a homomorphism of simplicial monoids which is a $f$-weak equivalence as a morphism of simplicial sheaves of sets. Then the corresponding morphism $\mathrm{B}(\mathbf{M}_{1}) \to \mathrm{B}(\mathbf{M}_{2})$ is a $\Sigma_{s}(f)$-weak equivalence (of simplicial sheaves of sets).

Proof. — Indeed for any monoid M the successive quotients in the skeletal filtration of B(M) have obviously the following form:

$$
s k _ {n} \mathbf {B} (\mathbf {M}) / s k _ {n - 1} \mathbf {B} (\mathbf {M}) \cong \Delta^ {n} / \partial \Delta^ {n} \wedge \mathbf {M} ^ {\wedge n}.
$$

For a simplicial monoid M we thus get a functorial filtration on the bisimplicial sheaf  $(p, q) \mapsto \mathbf{B}_{p}(\mathbf{M}_{q})$  whose successive quotients are isomorphic for each  $n \geqslant 0$  to  $\Delta^{n}/\partial\Delta^{n} \wedge^{ext} M^{\wedge n}$  (exterior smash-product which take two pointed simplicial sheaves to the obvious bisimplicial sheaf). The realization of this filtration of bisimplicial sheaves gives us a natural filtration of  $\mathbf{B}(\mathbf{M})$  with quotients of the form:

$$
\Delta^ {n} / \partial \Delta^ {n} \wedge \mathbf {M} ^ {\wedge n}
$$

which easily implies the result.

We end with the following result:

Lemma 2.36. — Let $f: \mathbf{M}_{1} \to \mathbf{M}_{2}$ be a morphism of simplicial sheaves of monoids which is a $f$-weak equivalence as a morphism of simplicial sheaves of sets. Then the corresponding morphism $\mathbf{R}\Omega_{s}^{1}\mathbf{B}(\mathbf{M}_{1}) \to \mathbf{R}\Omega_{s}^{1}\mathbf{B}(\mathbf{M}_{2})$ is a $f$-weak equivalence.

Proof. — Using previous lemma, we see that the morphism:

$$
\mathbf {L} _ {\boldsymbol {\Sigma} (f)} (\mathbf {B} (\mathbf {M} _ {1})) \rightarrow \mathbf {L} _ {\boldsymbol {\Sigma} (f)} (\mathbf {B} (\mathbf {M} _ {2}))
$$

is a simplicial weak equivalence. The lemma follows now from Theorem 2.34.

## 2.3. Homotopy category of a site with interval

## Definitions, examples and the main theorem

Let us first recall the definition of a site with interval given in [31, 2.2]. Let T be site (with enough points, as usual). Write pt for the final object of  $Shv(T)$ . An interval in T is a sheaf of sets I together with morphisms:

$$
\mu : \mathrm{I} \times \mathrm{I} \rightarrow \mathrm{I}
$$

$$
i _ {0}, i _ {1}: p t \rightarrow \mathrm{I}
$$

satisfying the following two conditions:

\- let $p$ be the canonical morphism $I \to pt$ then

$$
\mu (i _ {0} \times I d) = \mu (I d \times i _ {0}) = i _ {0} p
$$

$$
\mu (i _ {1} \times I d) = \mu (I d \times i _ {1}) = I d
$$

\- the morphism $i_0 \coprod i_1 : pt \coprod pt \to I$ is a monomorphism.

Definition 3.1. — Let (T, I) be a site with interval. A simplicial sheaf $\mathcal{X}$ is called I-local if for any simplicial sheaf $\mathcal{Y}$ the map

$$
H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathcal {Y} \times \mathrm{I}, \mathcal {K}) \rightarrow H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathcal {Y}, \mathcal {K})
$$

induced by $i_0: pt \to I$ is a bijection.

A morphism $f: \mathcal{X} \to \mathcal{Y}$ is called an I-weak equivalence if for any I-local $\mathcal{Z}$ the corresponding map

$$
\operatorname{Hom} _ {\mathscr {H} _ {s} (\mathrm{T})} (\mathcal {Y}, \mathscr {Z}) \rightarrow \operatorname{Hom} _ {\mathscr {H} _ {s} (\mathrm{T})} (\mathscr {X}, \mathscr {Z})
$$

is a bijection.

The homotopy category $\mathcal{H}(\mathrm{T},\mathrm{I})$ of a site with interval $(\mathrm{T},\mathrm{I})$ is the localization of $\Delta^{op}\mathrm{Shv}(\mathrm{T})$ with respect to the class of I-weak equivalences.

Denote the class of I-weak equivalences by  $W_{I}$  and define a class  $F_{I}$  of I-fibrations as the class of morphisms with the right lifting property with respect to  $C \cap W_{I}$ . Clearly these definitions are a particular case of general definitions of Section 2 for  $A = \{i_{0}\}$ . We will show in the next section that the morphism  $i_{0}$  satisfies the conditions of Theorem 2.7, which implies the following result.

Theorem 3.2. — Let (T, I) be a site with interval. Then the category of simplicial sheaves on T together with the classes of morphisms  $(\mathbf{W}_{\mathrm{I}}, \mathbf{C}, \mathbf{F}_{\mathrm{I}})$  is a proper model category. The inclusion of the category of I-local objects  $\mathcal{H}_{s,\mathrm{I}}(\mathrm{T})$  to  $\mathcal{H}_{s}(\mathrm{T})$  has a left adjoint  $L_{I}$  which identifies  $\mathcal{H}_{s,\mathrm{I}}(\mathrm{T})$  with the homotopy category  $\mathcal{H}(\mathrm{T}, \mathrm{I})$ .

Remark 3.3. — It is an easy exercise to show that the I-model category structure on  $\Delta^{op}Shv(T)$  only depends on the object I and not on the morphism  $i_{0}$  and coincides with the A-model category structure of Theorem 2.5 with  $A=\{I\to pt\}$ .

Examples.

1. Let T be the standard simplicial category  $\Delta$  with the trivial topology. Then  $Shv(T)$  is the category of simplicial sets. If we take I to be the simplicial interval  $\Delta^{1}$  the corresponding homotopy category is canonically equivalent to the usual homotopy category of simplicial sets.

2. Let T be the category of locally contractible topological spaces with the usual open topology and I be the sheaf represented by the unit interval. Again the corresponding homotopy category is the usual homotopy category (cf Proposition 3.3).

3. Let G be a finite group and T be the category of good G-spaces (see Definition 3.1). We may consider two different topologies c and f on T. A covering in the first one is a morphism  $X \rightarrow Y$  which locally splits as a morphism of topological spaces without G-action. A covering in the second is a morphism  $X \rightarrow Y$  which has a G-equivariant splitting over a G-equivariant open covering of Y. Take I to be the sheaf represented by the unit interval with the trivial G-action. The category  $\mathcal{H}(T_{c}, I)$  is equivalent to the “coarse” homotopy category of G-spaces where a morphism  $f: X \rightarrow Y$  is defined to be a weak equivalence if and only if it is a weak equivalence of topological spaces. The category  $\mathcal{H}(T_{f}, I)$  is equivalent to the “fine” homotopy category of G-spaces where a morphism  $f: X \rightarrow Y$  is defined to be a weak equivalence if and only if the corresponding morphisms  $X^{H} \rightarrow Y^{H}$  are weak equivalences for all subgroups H of G (see Section 3).

4. Let T be the category Sm/S of smooth schemes over a base S considered with the Nisnevich topology (see Definition 1.2) and I be the sheaf represented by the affine line  $A^{1}$  over S. The corresponding homotopy category  $\mathcal{H}\left((Sm/S)_{\mathcal{N}s},\mathbf{A}^{1}\right)$  which is called the homotopy category of schemes over S is the main object we are interested in this paper.

5. More generally, any ringed site (T, O) defines a site with interval. In particular we may consider the homotopy category associated with any subcategory in the category of schemes (over a base) which contains affine line.

## The functor Sing\*

In this section we prove that the conditions of Theorem 2.7 hold for the morphism $i_0: pt \to I$ in any site with interval (T, I). In order to do it we construct an endofunctor $Sing_{*}^{I}$ on the category of simplicial sheaves on a site with interval together with a natural transformation $s: Id \to Sing_{*}^{I}$ such that one has

1. $Sing_{*}^{I}$ commutes with limits;

2. $Sing_{*}^{I}$ takes the morphism $i_0: pt \to I$ to a weak equivalence;

3. for any $\mathcal{X}$ the morphism $s_{\mathcal{X}}: \mathcal{X} \to \operatorname{Sing}_{*}^{\mathrm{I}}(\mathcal{X})$ is a monomorphism and an I-weak equivalence;

4. Sing $^{I}$ takes I-fibrations to I-fibrations.

Provided that a functor  $Sing_{*}^{I}$  satisfying these properties exists, the proof of the required condition goes as follows. Let X be an object of  $\Delta^{op}Shv(T)$  and  $p: E \to X \times I$

be a morphism in  $F_{I}$ . We have to show that the upper horizontal arrow in the cartesian square

$$
\begin{array}{c c c} \mathcal {E} \times_ {\mathcal {X}} (\mathcal {X} \times \mathrm{I}) & \longrightarrow & \mathcal {E} \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {X} & \stackrel {{I d \times i _ {0}}} {{\longrightarrow}} & \mathcal {X} \times \mathrm{I} \end{array}
$$

is an I-weak equivalence. Applying the functor  $Sing_{*}^{I}$  to this diagram we get a cartesian square (by (1)) which is I-weak equivalent to the original one (by (4)). By (2) the morphism  $Sing_{*}^{I}(p)$  is an I-fibration and in particular a fibration and by (3) and (1) the morphism  $Sing_{*}^{I}(Id \times i_{0})$  is a simplicial weak equivalence. Therefore the morphism  $Sing_{*}^{I}(\mathcal{E} \times_{\mathcal{X}} (\mathcal{K} \times \mathbf{I})) \to Sing_{*}^{I}(\mathcal{E})$  is a simplicial weak equivalence since the simplicial model structure is proper.

Define a cosimplicial object $\Delta_{\mathrm{I}}^{\bullet}:\Delta \to Shv(\mathrm{T})$ as follows. On objects we set $\Delta_{\mathrm{I}}^{n} = \mathrm{I}^{n}$. Let $f\colon (0,\dots,n)\to (0,\dots,m)$ be a morphism in the standard simplicial category $\Delta$. Define a morphism of sets $\phi(f):\{1,\dots,m\} \to \{0,\dots,n + 1\}$ setting

$$
\phi (f) (i) = \left\{ \begin{array}{l l} m i n \{l \in \{0,..., n \} | f (l) \geq i \} & \text { if   this   set   is   not   empty } \\ n + 1 & \text { otherwise. } \end{array} \right.
$$

Denote by  $pr_{k}: I^{n} \to I$  the k-th projection and by  $p: I^{n} \to pt$  the canonical morphism from  $I^{n}$  to the finial object of T. Then  $\Delta_{\mathrm{I}}^{\bullet}(f): \mathrm{I}^{n} \to \mathrm{I}^{m}$  is given by the following rule

$$
p r _ {k} \circ a (f) = \left\{ \begin{array}{l l} p r _ {\phi (f) (k)} & \text {if} \quad \phi (f) (k) \in \{1,..., n \} \\ i _ {0} \circ p & \text {if} \quad \phi (f) (k) = n + 1 \\ i _ {1} \circ p & \text {if} \quad \phi (f) (k) = 0. \end{array} \right.
$$

For a simplicial sheaf $\mathcal{X}$ let $Sing_{*}^{I}(\mathcal{X})$ be the diagonal simplicial sheaf of the bisimplicial sheaf with terms of the form $\underline{Hom}(\Delta_{\mathrm{I}}^{m},\mathcal{X}_{n})$. We shall often forget to mention the interval in the previous notation and denote $Sing_{*}^{I}(\mathcal{X})$ simply by $Sing_{*}(\mathcal{X})$. There is a canonical natural transformation $s:Id\to Sing_{*}$ such that for any $\mathcal{X}$ the morphism $s_{\mathcal{X}}:\mathcal{X}\to Sing_{*}(\mathcal{X})$ is a monomorphism. We are going to show now that the functor $Sing_{*}$ satisfies the conditions (1)-(4) listed above.

The first of them is obvious from the construction of  $Sing_{*}$ . The second one is proven in Corollary 3.5, the third one in Corollary 3.8 and the fourth one in Corollary 3.13.

Let $f, g: \mathcal{X} \to \mathcal{Y}$ be two morphisms of simplicial sheaves. An elementary I-homotopy from $f$ to $g$ is a morphism $H: \mathcal{X} \times I \to \mathcal{Y}$ such that $H \circ i_0 = f$ and $H \circ i_1 = g$. Two morphisms are called I-homotopic if they can be connected by a sequence of elementary I-homotopies. A morphism $f: \mathcal{X} \to \mathcal{Y}$ is called a strict I-homotopy equivalence if there is a morphism $g: \mathcal{Y} \to \mathcal{X}$ such that $f \circ g$ and $g \circ f$

are I-homotopic to  $Id_{Y}$  and  $Id_{X}$  respectively. Replacing I in these definitions by  $\Delta^{1}$  one gets the corresponding notions of elementary simplicial homotopy, simplicially homotopic morphisms and strict simplicial homotopy equivalences.

Proposition 3.4. — Let $f, g: \mathcal{X} \to \mathcal{Y}$ be two morphisms and H be an elementary I-homotopy from $f$ to $g$. Then there exists an elementary simplicial homotopy from $\operatorname{Sing}_{*}(f)$ to $\operatorname{Sing}_{*}(g)$.

Proof. — Since  $Sing_{*}$  commutes with products it is sufficient to show that the morphisms  $Sing_{*}(i_{0})$ ,  $Sing_{*}(i_{1}): pt = Sing_{*}(pt) \rightarrow Sing_{*}(I)$  are elementary simplicially homotopic. The required homotopy is given by the morphism  $pt \rightarrow Sing_{1}(I) = \underline{Hom}(I, I)$  which corresponds to the identity of I.

Corollary 3.5. — For any simplicial sheaf $\mathcal{X}$ the morphism

$$
S i n g _ {*} (\mathcal {X}) \stackrel {I d \times i _ {0}} {\rightarrow} S i n g _ {*} (\mathcal {X} \times \mathbf {I})
$$

is a simplicial homotopy equivalence.

Proof. — By Proposition 3.4 it is sufficient to show that the composition $\mathcal{X} \times \mathbf{A}^1 \xrightarrow{pr} \mathcal{X} \xrightarrow{Id \times i_0} \mathcal{X} \times \mathbf{I}$ is elementary I-homotopic to the identity. This homotopy is given by the morphism $Id \times \mu : \mathcal{X} \times \mathbf{I} \times \mathbf{I} \to \mathcal{X} \times \mathbf{I}$.

Lemma 3.6. — Any strict I-homotopy equivalence is an I-weak equivalence.

Proof. — Let  $f: X \to Y$  be a strict I-homotopy equivalence and g be a I-homotopy inverse to f. We have to show that the compositions  $f \circ g$  and  $g \circ f$  are equal to the corresponding identity morphisms in the I-homotopy category. By definition these compositions are I-homotopic to identity and it remains to show that two elementary I-homotopic morphisms coincide in the I-homotopy category which follows immediately from definitions.

Lemma 3.7. — For any $\mathcal{X}$ the canonical morphism $\mathcal{X} \to \underline{\text{Hom}}(\mathbf{I}, \mathcal{X})$ is a strict I-homotopy equivalence, and thus an I-weak equivalence.

Proof. — The morphism  $\underline{\text{Hom}}(\mathbf{I},\mathcal{X})\times\mathbf{I}\to\underline{\text{Hom}}(\mathbf{I},\mathcal{X})$  whose adjoint corresponds to  $\mu$  defines a strict I-homotopy from  $\underline{\text{Hom}}(p,\mathcal{X})\circ\underline{\text{Hom}}(i_{0},\mathcal{X})$  to  $\underline{\text{Id}_{\underline{\text{Hom}}(\mathbf{I},\mathcal{X})}}$ . Since  $\underline{\text{Hom}}(i_{0},\mathcal{X})\circ\underline{\text{Hom}}(p,\mathcal{X})=Id_{\mathcal{X}}$ , the lemma is proven.

Corollary 3.8. — For any $\mathcal{X}$ the canonical morphism $\mathcal{X} \to \operatorname{Sing}_{*}(\mathcal{X})$ is an I-weak equivalence.

Proof. — One observes easily that the i-th term of the simplicial sheaf  $\mathrm{C}_{*}(\mathcal{X})$  is isomorphic to  $Hom(\mathbf{I}^{i}, \mathcal{X}_{i})$  and the canonical morphism  $\mathcal{X} \to Sing_{*}(\mathcal{X})$  coincides

termwise with the canonical morphisms  $\mathcal{X}_{i} \to \underline{\text{Hom}}(\Gamma^{i}, \mathcal{X}_{i})$  from Lemma 3.7. Our result follows now from Proposition 2.14.

It remains to show that the functor  $Sing_{*}$  preserves I-fibrations. In order to do it we will show that it has a left adjoint which preserves cofibrations (i.e. monomorphisms) and I-weak equivalences.

For any cosimplicial object $\mathbf{D}^{\bullet}$ in $\Delta^{op}Shv(\mathbf{T})$ and any simplicial sheaf $\mathcal{K}$ denote by $|\mathcal{K}|_{\mathbf{D}}$. the coend (cf [21, p. 222]) of the functor

$$
\begin{array}{c c c}\Delta^ {o p} \times \Delta&\rightarrow&\Delta^ {o p} S h v (\mathbf {T})\\\uplus&&\uplus\end{array}
$$

$$
(n, m) \quad \mapsto \quad \mathscr {K} _ {n} \times \mathrm{D} ^ {m}.
$$

Any morphism of cosimplicial objects  $D^{\bullet} \rightarrow D^{\prime\bullet}$  induces in the obvious way a morphism of realization functors  $| - |_{D^{\bullet}} \rightarrow | - |_{D^{\prime}\bullet}$ .

One can observe easily that the functor $\mathcal{K} \mapsto |\mathcal{K}|_{\Delta^{\bullet} \times \Delta_{\mathrm{I}}^{\bullet}}$ is left adjoint to $Sing_{*}$. For a cosimplicial simplicial sheaf $\mathbf{D}^{\bullet}$ and $n \geqslant 0$ let us denote by $\partial \mathbf{D}^{n}$ the simplicial sheaf $|\partial \Delta^{n}|_{\mathrm{D}^{\bullet}}$. We shall say that a cosimplicial simplicial sheaf $\mathbf{D}^{\bullet}$ is unaugmentable if the morphism $\mathbf{D}^{0} \amalg \mathbf{D}^{0} \to \mathbf{D}^{1}$ induced by the cofaces morphisms is a monomorphism. For example, $\Delta^{\bullet}, \Delta_{\mathrm{I}}^{\bullet}$ and $\Delta^{\bullet} \times \Delta_{\mathrm{I}}^{\bullet}$ are unaugmentable cosimplicial simplicial sheaves.

Lemma 3.9. — For any unaugmentable cosimplicial object D• the obvious morphisms $\partial\mathrm{D}^{n}\to\mathrm{D}^{n}$ are monomorphisms.

Lemma 3.10. — For any unaugmentable cosimplicial simplicial sheaf D• the functor  $| - |_{D}$  preserves monomorphisms.

Proof. — Using Lemma 1.1 one can reduce the problem to the case of monomorphisms of the form  $\mathrm{P}(\mathcal{X}\to\mathcal{Y},\partial\Delta^{n}\subset\Delta^{n})$  for monomorphisms  $X\to Y$  of sheaves of simplicial dimension zero (see Lemma 1.8 for the notation  $\mathrm{P}(-,-)$ ). Then  $|Y\times\Delta^{n}|_{D^{\bullet}}$  is isomorphic to the simplicial sheaf  $Y\times D^{n}$  and the morphism  $|\mathrm{P}(\mathcal{X}\to\mathcal{Y},\partial\Delta^{n}\subset\Delta^{n})|_{D^{\bullet}}$  is isomorphic to the monomorphism  $\mathrm{P}(\mathcal{X}\to\mathcal{Y},\partial\mathrm{D}^{n}\subset\mathrm{D}^{n})$  which proves the lemma.

Remark 3.11. — Looking at the morphism $|\partial \Delta^1|_{\mathrm{D}^\bullet} \to |\Delta^1|_{\mathrm{D}^\bullet}$ one can see that the property that the functor $| - |_{\mathrm{D}^\bullet}$ preserves monomorphisms characterizes unaugmentable cosimplicial simplicial sheaves.

Lemma 3.12. — For any $\mathcal{X}$ the morphisms

$$
\begin{array}{l} | \mathcal {X} | _ {\Delta^ {\bullet} \times \Delta_ {\mathrm{I}} ^ {\bullet}} \to \mathcal {X} \\ | \mathcal {X} | _ {\Delta^ {\bullet} \times \Delta_ {\mathrm{I}} ^ {\bullet}} \to | \mathcal {X} | _ {\Delta_ {\mathrm{I}} ^ {\bullet}} \end{array}
$$

induced by the projections $\Delta^{\bullet} \times \Delta_{\mathrm{I}}^{\bullet} \to \Delta^{\bullet}$ and $\Delta^{\bullet} \times \Delta_{\mathrm{I}}^{\bullet} \to \Delta_{\mathrm{I}}^{\bullet}$ are I-weak equivalences.

Proof. — To prove that the first type of morphisms are I-weak equivalences we use Lemmas 1.1, Lemma 2.11 and Corollary 2.13 to reduce the problem to the case when X is of the form  $Y \times \Delta^{n}$  for some Y of simplicial dimension zero and  $n \geqslant 0$ . Then the morphism  $|Y \times \Delta^{n}| \to Y \times \Delta^{n}$  is isomorphic to the projection  $Y \times \Delta^{n} \times \Delta_{I}^{n} \to Y \times \Delta^{n}$  which is an I-weak equivalence by Lemma 2.15. The proof for the second type is similar.

Corollary 3.13. — The functor Sing\* preserves I-fibrations.

Proof. — By definition of I-fibrations it is sufficient to show that the left adjoint functor  $\left|-\right|_{\Delta\bullet\times\Delta_{I}^{\bullet}}$  preserves monomorphisms and I-weak equivalences. The first fact is proven in Lemma 3.10. The second follows immediately from Lemma 3.12.

Note that the realization functor $| - |_{\Delta_{\mathrm{I}}^{\bullet}} : \Delta^{op}Shv(\mathrm{T}) \to \Delta^{op}Shv(\mathrm{T})$ takes values in the full subcategory of simplicial sheaves of simplicial dimension zero, i.e. factors through a functor $| - |_{\Delta_{\mathrm{I}}^{\bullet}} : \Delta^{op}Shv(\mathrm{T}) \to Shv(\mathrm{T})$ which is left adjoint to the restriction of $\mathbf{C}_*$ to $Shv(\mathrm{T})$. Together with Lemma 3.12 this fact can be used to obtain an alternative description of the homotopy category $\mathcal{H}(\mathrm{T},\mathrm{I})$ as follows.

Let us say that a morphism in $Shv(T)$ is a I-weak equivalence if it is a I-weak equivalence in $\Delta^{op}Shv(T)$. Let $\mathbf{W}_{\mathrm{I}}^{\prime}$ be the class of I-weak equivalences in $Shv(T)$, $\mathbf{C}'$ the class of monomorphisms in $Shv(T)$ and $\mathbf{F}_{\mathrm{I}}^{\prime}$ the class of morphisms which have the right lifting property with respect to $\mathbf{W}_{\mathrm{I}}^{\prime} \cap \mathbf{C}'$. One can prove in the same way as we proved Theorem 2.5 that the triple $(\mathbf{W}_{\mathrm{I}}^{\prime}, \mathbf{C}', \mathbf{F}_{\mathrm{I}}^{\prime})$ gives $Shv(T)$ a structure of model category.

Proposition 3.14. — The adjoint functors

$$
S i n g _ {*}: S h v (\mathrm{T}) \longrightarrow \Delta^ {o p} S h v (\mathrm{T})
$$

$$
\mid - \mid_ {\Delta_ {I} ^ {\bullet}}: \Delta^ {o p} S h v (T) \rightarrow S h v (T)
$$

take I-weak equivalences to I-weak equivalences and the corresponding functors between homotopy categories are mutually inverse equivalences.

Proof. — Follows formally from Lemma 3.12.

## Functoriality

We consider the functoriality of homotopy categories of sites with intervals only in the case of reasonable continuous maps of sites (cf 1.55). We have the following obvious lemma.

Lemma 3.15. — Let  $(\mathrm{T}_{1}, \mathrm{I}_{1})$ ,  $(\mathrm{T}_{2}, \mathrm{I}_{2})$  be sites with intervals and  $f: T_{1} \rightarrow T_{2}$  be a reasonable continuous map. Then the following conditions are equivalent:

1.  $Rf_{*}$  takes  $I_{1}$ -local objects to  $I_{2}$ -local objects;

2. $\mathbf{L}f^{*}$ takes $\mathbf{I}_2$-weak equivalences to $\mathbf{I}_1$-weak equivalences;

3. for any $\mathcal{K}$ on $\mathrm{T}_2$ the morphism $\mathbf{L}f^{*}(\mathcal{K}\times \mathrm{I}_{2})\to \mathbf{L}f^{*}(\mathcal{K})$ is an $\mathrm{I}_1$-weak equivalence.

## Definition 3.16. — A reasonable continuous map of sites with intervals

$$
(\mathbf {T} _ {1}, \mathbf {I} _ {1}) \rightarrow (\mathbf {T} _ {2}, \mathbf {I} _ {2})
$$

is a reasonable continuous map of sites $f: \mathbf{T}_1 \to \mathbf{T}_2$ satisfying the equivalent conditions of Lemma 3.15.

For any reasonable continuous map of sites with intervals  $(\mathbf{T}_{1}, \mathbf{I}_{1}) \to (\mathbf{T}_{2}, \mathbf{I}_{2})$  the functor  $Lf^{*}$  induces by definition a functor on the localized categories

$$
\mathbf {L} _ {\mathrm{I}} f ^ {*}: \mathcal {H} (\mathrm{T} _ {2}, \mathrm{I} _ {2}) \rightarrow \mathcal {H} (\mathrm{T} _ {1}, \mathrm{I} _ {1})
$$

and the functor $\mathbf{R}f_{*}$ induces (first by restriction to the subcategories $\mathcal{H}_{s,\mathrm{I}_i}(\mathrm{T}_i)$ defined in Theorem 3.2, and then using the isomorphisms $\mathcal{H}_{s,\mathrm{I}_i}(\mathrm{T}_i) \cong \mathcal{H}(\mathrm{T}_i,\mathrm{I}_i)$ of the same Theorem 3.2) a functor:

$$
\mathbf {R} ^ {\mathrm{I}} f _ {*}: \mathscr {H} \left(\mathrm{T} _ {1}, \mathrm{I} _ {1}\right)\rightarrow \mathscr {H} \left(\mathrm{T} _ {2}, \mathrm{I} _ {2}\right).
$$

Using Theorem 3.2, Proposition 1.57 and Lemma 3.15 we get the following result.

Proposition 3.17. — Let $f: (\mathrm{T}_{1}, \mathrm{I}_{1}) \to (\mathrm{T}_{2}, \mathrm{I}_{2})$ be a reasonable continuous map of sites with intervals. Then the functor $\mathbf{L}_{\mathrm{I}} f^{*}: \mathcal{H}(\mathrm{T}_{2}, \mathrm{I}_{2}) \to \mathcal{H}(\mathrm{T}_{1}, \mathrm{I}_{1})$ is left adjoint to $\mathbf{R}^{\mathrm{I}} f_{*}: \mathcal{H}(\mathrm{T}_{1}, \mathrm{I}_{1}) \to \mathcal{H}(\mathrm{T}_{2}, \mathrm{I}_{2})$.

If $f, g$ is a composable pair of reasonable continuous maps of sites with interval then there are canonical isomorphisms of functors

$$
\mathbf {L} _ {\mathrm{I}} (g \circ f) ^ {*} \cong \mathbf {L} _ {\mathrm{I}} f ^ {*} \circ \mathbf {L} _ {\mathrm{I}} g ^ {*}
$$

$$
\mathbf {R} ^ {\mathrm{I}} (g \circ f) _ {*} \cong \mathbf {R} ^ {\mathrm{I}} g _ {*} \circ \mathbf {R} ^ {\mathrm{I}} f _ {*}
$$

## An "explicit" I-resolution functor

Definition 3.18. — A I-resolution functor on a site with interval (T, I) is a pair  $(Ex_{I}, \theta)$  consisting of a functor  $Ex_{I} : \Delta^{op}Shv(T) \to \Delta^{op}Shv(T)$  and a natural transformation  $\theta : Id \to Ex$  such that for any X the object  $Ex(\mathcal{X})$  is I-fibrant and the morphism  $\mathcal{X} \to Ex(\mathcal{X})$  is an I-trivial cofibration.

Let $(T, I)$ be a site with interval. From theorem 2.21 we know that such I-resolution functors do exist. The purpose of this section is to give a construction of such an I-resolution functor which emphasizes the role of the interval. As an application we get corollary 3.22 below.

Proposition 3.19. — Let $\mathcal{K}$ be a fibrant simplicial sheaf. Then the following conditions are equivalent:

1. $\mathcal{K}$ is I-local (or equivalently I-fibrant by 2.28);

2. for any object U in T the morphism of simplicial sets $\mathcal{K}(\mathrm{U}) \to \mathcal{K}(\mathrm{U} \times \mathrm{I})$ is a weak equivalence;

3. for any object U in T and any element  $x \in \mathcal{K}_{0}(\mathrm{U})$  the homomorphisms  $\pi_{i}(\mathcal{K}(\mathrm{U}), x) \to \pi_{i}(\mathcal{K}(\mathrm{U} \times \mathrm{I}), x)$  induced by the projection  $U \times I \to U$  are epimorphisms for all  $i \geqslant 0$ .

Proof. — The third condition is equivalent to the second one since the morphisms in question are always monomorphisms (use the zero section of the projection  $U \times I \rightarrow U$ ). The equivalence of the first two conditions follows clearly from Lemma 2.8(4) and Proposition 2.28.

Choose a resolution functor  $(Ex, \theta)$  (see 1.6) corresponding to the simplicial model category structure on  $\Delta^{op}Shv(\Gamma)$ . Thus for any simplicial sheaf X the morphism  $X \to Ex(X)$  is a (simplicial) weak equivalence and  $Ex(X)$  is (simplicially) fibrant.

The composition $\theta \circ s$ (remember 3 that $s$ is a natural transformation $Id \to Sing_{*}$) defines a natural transformation $Id \to Ex \circ Sing_{*}$. The functor $Ex \circ Sing_{*}$ can thus be iterated to any ordinal number power (see 2).

Lemma 3.20. — For any sufficiently large ordinal number $\omega$, the functor $Ex_{\mathrm{I}} := (Ex \circ \operatorname{Sing}_{*})^{\omega} \circ Ex$ together with the canonical natural transformation $Id \to Ex_{\mathrm{I}}$ form an I-resolution functor.

By Lemma 2.13 and Corollary 3.8, for any $\mathcal{K}$ and any ordinal number $\omega$ the canonical morphism $\mathcal{K} \to Ex_{\mathrm{I}}(\mathcal{K})$ is a monomorphism and an I-weak equivalence. It thus suffices to establish:

Lemma 3.21. — For any sufficiently large ordinal number $\omega$ then for any simplicial sheaf $\mathcal{X}$ the object $Ex_{\mathrm{I}}(\mathcal{X})$ is I-local.

Proof. — Choose  $\alpha$  to be a cardinal large enough to ensure:

– any filtering colimit of (simplicially) fibrant objects indexed by the ordered set  $Seq[\alpha]$  is again fibrant;

\- for any $\mathbf{U} \in \mathbf{T}$ and any functor $\mathcal{Y} : Seq[\alpha] \to \Delta^{op}Shv(\mathbf{T})$ the map $colim_{\gamma \in Seq[\alpha]}\mathcal{Y}_{\gamma}(\mathbf{U}) \to colim_{Seq[\alpha]}\mathcal{Y}(\mathbf{U})$ is bijective.

(This is possible using corollary 2.18 and the fact that any object of $Shv(T)$ is accessible.) Then choose $\omega$ to be the smallest ordinal number of cardinality $\alpha$. It is sufficient (using 3.19) to show that for any simplicial sheaf $\mathcal{K}$ the fibrant simplicial

sheaf  $Ex_{I}K$  satisfies the third of the equivalent conditions of Proposition 3.19. By construction (and the choice of  $\omega$ ), for any  $U \in T$  one has:

$$
E x _ {\mathrm{I}} (\mathcal {K}) (\mathrm{U}) = \operatorname{colim} _ {\gamma \in S e q [ \alpha ]} (E x \circ S i n g _ {*}) ^ {\gamma} (E x (\mathcal {K})) (\mathrm{U}).
$$

Let $\gamma \in Seq[\alpha]$ and $x$ be an element of $(Ex \circ Sing_{*})^{\gamma}(\mathcal{X})_{0}(\mathrm{U})$ for some $n$ and

$$
\boldsymbol {\beta} \in \pi_ {i} ((E x \circ S i n g _ {*}) ^ {\gamma} (\mathscr {K}) (\mathrm{U} \times \mathrm{I}), x).
$$

Let further $\beta_0 = p^* i_0^*(\beta)$ where $i_0$ means $Id_{\mathrm{U}} \times i_0: \mathrm{U} \to \mathrm{U} \times \mathrm{I}$ and $p: \mathrm{U} \times \mathrm{I} \to \mathrm{U}$ is the projection. It is sufficient to show that $\beta = \beta_0$ in the colimit of homotopy groups. We may assume that $(Ex \circ Sing_*)^\gamma(\mathcal{K})(\mathrm{U} \times \mathrm{I})$ is a Kan simplicial set; indeed if not, we replace $\gamma$ by $\gamma + 1 \in Seq[\alpha]$. Thus $\beta$ is represented by a morphism

$$
b: \mathrm{U} \times \mathrm{I} \times \partial \Delta_ {s} ^ {i + 1} \rightarrow (E x \circ S i n g _ {*}) ^ {\gamma} (\mathscr {K})
$$

in  $\Delta^{op}Shv(\mathrm{T})$  and  $\beta_{0}$  is represented by  $b_{0}=\beta\circ i_{0}\circ p$ . One can easily see that the composition  $i_{0}\circ p:U\times I\times\partial\Delta_{s}^{i+1}\to U\times I\times\partial\Delta_{s}^{i+1}$  is I-homotopic to the identify. Therefore b is I-homotopic to  $b_{0}$  and by Proposition 3.4 we conclude that  $\beta=\beta_{0}$  in  $\pi_{i}((Ex\circ Sing_{*})^{\gamma+1}(\mathcal{K})(U\times I),x)$ .

Corollary 3.22. — Let $\mathcal{X}$ be a simplicial sheaf and $\mathcal{X} \to \mathcal{X}'$ be an I-weak equivalence with $\mathcal{X}'$ I-local. Then the canonical morphism of sheaves $a\underline{\pi}_0(\mathcal{X}) \to a\underline{\pi}_0(\mathcal{X}')$ is an epimorphism. In particular, if $\mathcal{X}$ is connected ($a\underline{\pi}_0(\mathcal{X}) = pt$) then so is $\mathcal{X}'$.

## 3. The A $^{1}$ -homotopy category of schemes over a base

In this section we study the basic properties of  $A^{1}$ -homotopy category of smooth schemes over a base. Modulo the conventions of the previous section the definition of the  $A^{1}$ -homotopy category  $\mathcal{H}(S)$  of smooth schemes over a base scheme S takes one line –  $\mathcal{H}(S)$  is the homotopy category of the site with interval  $((Sm/S)_{\mathcal{Nis}}, \mathbf{A}^{1})$ , where Sm/S is the category of smooth schemes (of finite type) over S and Nis refers to the Nisnevich topology.

Nisnevich topology was introduced by Y. Nisnevich in [25]. We recall its definition and some of its basic properties in Section 1. This topology is strictly stronger (i.e. has more coverings) than the Zariski one and strictly weaker (i.e. has less coverings) than the étale one. Miraculously, it seems to have the good properties of both while avoiding the bad ones. Here are some examples.

\- the Nisnevich cohomological dimension of a scheme of Krull dimension $d$ is $d$ (similar to the Zariski topology);

\- algebraic K-theory has Nisnevich descent (similar to the Zariski topology);

\- spectrum of a field has no notrivial Nisnevich cohomology (similar to the Zariski topology);

\- the functor of direct image for finite morphisms is exact (similar to the étale topology);

\- Nisnevich cohomology can be computed using Cech cochains (similar to the étale topology);

\- any smooth pair $(\mathbf{Z}, \mathbf{X})$ is locally equivalent in the Nisnevich topology to a pair of the form $(\mathbf{A}^n, \mathbf{A}^m)$ (similar to the étale topology).

In the rest of Section 1 we discuss the properties of the homotopy category of simplicial sheaves on $(Sm / S)_{Nis}$. The fact that Nisnevich topology can be generated by a set of elementary coverings of very special type implies that in many cases fibrant simplicial sheaves can be replaced by simplicial sheaves satisfying a much weaker condition which we call the B.G. - property after K.S. Brown and S.M. Gersten who considered it in the context of Zariski topology in [7].

In Section 2 we first recall the most important definitions and results of Section 3 in the context of the site with interval  $((Sm/S)_{\mathcal{N}is}, \mathbf{A}^{1})$ . We then discuss briefly the functoriality of our constructions with respect to S.

In Section 2 we prove three theorems which play major role in further applications of our constructions.

In the final section we discuss some examples of topological realizations functors.

## 3.1. Simplicial sheaves in the Nisnevich topology on smooth sites

## Nisnevich topology

Let S be a Noetherian scheme of finite dimension. Denote by Sch/S (resp. Sm/S) the category of schemes (resp. smooth schemes) of finite type over S. Let  $O_{X,x}$  (resp.  $O_{X,x}^{h}$ ) be the local ring (resp. the henselisation of the local ring) of x in X (cf [15, 18.6]). One has the following proposition.

Proposition 1.1. — Let X be a scheme of finite type over S and  $\{U_{i}\} \rightarrow X$  a finite family of étale morphisms in Sch/S. The following conditions are equivalent:

1. For any point x of X there is an i and a point u of  $U_{i}$  over x such that the corresponding morphism of residue fields is an isomorphism which maps to x with the same residue field;

2. for any point $x$ of $\mathbf{X}$, the morphism of S-schemes

$$
\amalg_ {i} (\mathrm{U} _ {i} \times_ {\mathrm{X}} S p e c \mathcal {O} _ {\mathrm{X}, x} ^ {h}) \to S p e c \mathcal {O} _ {\mathrm{X}, x} ^ {h}
$$

admits a section.

The following definition of the Nisnevich topology on $Sm / S$ is equivalent to the original definition given in [25].

Definition 1.2. — The collection of families of étale morphisms $\{U_{i}\} \to X$ in $Sm/S$ satisfying the equivalent conditions of the proposition forms a pretopology on the category $Sm/S$ (in

the sense of [13, II. Definition 1.3]). The corresponding topology is called the Nisnevich topology. The corresponding site will be denoted $(\mathrm{Sm} / \mathrm{S})_{\mathcal{N}\mathrm{i}s}$.

The presheaf on $Sm / S$ represented by a scheme over $S$ is always a Nisnevich sheaf (see [13, VII.2] or [24, I.2.17]). In particular the canonical functor $Sm / S \to Shv(Sm / S)_{Nis}$ is a fully faithfull embedding and we'll often identify the category $Sm / S$ with its image by this functor. A family of morphisms in $Sm / S$ satisfying the conditions of 1.1 will be called a Nisnevich covering and we shall call a morphism in $Sm / S$ a Nisnevich cover if the corresponding morphism of representable sheaves is an epimorphism in the Nisnevich topology.

The Nisnevich topology is clearly stronger than the Zariski one and weaker than the étale. In practice, it means that it behaves as the Zariski one in some regards and as the étale one in others.

Definition 1.3. — An elementary distinguished square in $(\mathrm{Sm} / \mathrm{S})_{\mathrm{Nis}}$ is a cartesian square of the form

$$
\begin{array}{c c c} \mathrm{U} \times_ {\mathrm{X}} \mathrm{V} & \longrightarrow & \mathrm{V} \\ \Big \downarrow & & \Big \downarrow^ {p} \\ \mathrm{U} & \stackrel {{j}} {{\longrightarrow}} & \mathrm{X} \end{array}
$$

such that p is an étale morphism, j is an open embedding and  $p^{-1}(\mathbf{X}-\mathbf{U}) \to \mathbf{X}-\mathbf{U}$  is an isomorphism (we put the reduced induced structure on the corresponding closed sets).

Clearly, for any elementary distinguished square as in Definition 1.3 the morphisms j and p form a Nisnevich covering of X. The following lemma shows that the Nisnevich topology is generated by coverings of this form. A similar statement holds in Zariski topology (with elementary distinguished squares being replaced by coverings by two Zariski open subschemes) but not in the étale.

Proposition 1.4. — A presheaf of sets F on Sm/S is a sheaf in the Nisnevich topology if and only if for any elementary distinguished square as in 1.3 the square of sets

$$
\begin{array}{c c c} \mathrm{F(X)} & \longrightarrow & \mathrm{F(U)} \\ \Big \downarrow & & \Big \downarrow \\ \mathrm{F(V)} & \longrightarrow & \mathrm {F(U\times_ {X} V)} \end{array}
$$

is cartesian.

Proof. — To prove the “only if” part observe first that for any elementary distinguished square as in Definition 1.3 the pair of morphisms  $\{U \rightarrow X, V \rightarrow X\}$  is

a Nisnevich covering of X. Thus for any Nisnevich sheaf F the square

$$
\begin{array}{c c c} \mathrm{F} (\mathrm{X}) & \longrightarrow & \mathrm{F} (\mathrm{V} \amalg \mathrm{U}) \\ \Big \downarrow & & \Big \downarrow \\ \mathrm{F} (\mathrm{V} \amalg \mathrm{U}) & \longrightarrow & \mathrm{F} ((\mathrm{V} \amalg \mathrm{U}) \times_ {\mathrm{X}} (\mathrm{V} \amalg \mathrm{U})) \end{array}
$$

is cartesian. On the other hand we have

$$
(\mathrm{V} \coprod \mathrm{U}) \times_ {\mathrm{X}} (\mathrm{V} \coprod \mathrm{U}) = (\mathrm{V} \times_ {\mathrm{X}} \mathrm{V}) \coprod (\mathrm{U} \times_ {\mathrm{X}} \mathrm{V}) \coprod (\mathrm{V} \times_ {\mathrm{X}} \mathrm{U}) \coprod (\mathrm{U} \times_ {\mathrm{X}} \mathrm{U})
$$

and, in view of the definition of an elementary distinguished square, we see that the pair of morphisms  $\{V \xrightarrow{\Delta} V \times_{X} V, U \times_{X} V \times_{X} V \to V \times_{X} V\}$  is a Nisnevich covering of  $V \times_{X} V$ . By diagram search we conclude that the square of the lemma is cartesian for any Nisnevich sheaf.

Let now F be a presheaf such that for any elementary distinguished square the corresponding square of sets of sections of F is cartesian. To prove that F is a Nisnevich sheaf we have to show that for any Nisnevich covering  $W=\{W_{i}\to X\}$  the sequence of sets  $F(X)\to\Pi F(W_{i})\Rightarrow\Pi F(W_{i}\times_{X}W_{j})$  is exact. A sequence of closed subsets of X of the form

$$
\emptyset = \mathbf {Z} _ {n + 1} \subset \mathbf {Z} _ {n} \subset \mathbf {Z} _ {n - 1} \subset \dots \subset \mathbf {Z} _ {0} = \mathbf {X}
$$

is called a splitting sequence for a covering W if the morphisms  $(\coprod p_{i})^{-1}(\mathbf{Z}_{i}-\mathbf{Z}_{i+1})\to\mathbf{Z}_{i}-\mathbf{Z}_{i+1}$  split. We are going to prove the required exactness by induction on the minimal length of a splitting sequence for W.

Lemma 1.5. — Let W be a Nisnevich covering of a noetherian scheme S. Then there exists a splitting sequence for W.

Proof. — Set  $p = \coprod p_{i}$ . By the definition of Nisnevich topology there exists a dense open subset  $U_{1}$  of X such that p splits over  $U_{1}$ . Set  $Z_{1} = X - U_{1}$ . Since  $p^{-1}(Z_{1}) \to Z_{1}$  is again a Nisnevich covering there exists a dense open subset  $U_{2}$  of  $Z_{1}$  such that  $p^{-1}(Z_{1}) \to Z_{1}$  splits over  $U_{2}$ . Set  $Z_{2} = Z_{1} - U_{2}$ . The sequence  $Z_{1}, Z_{2}$  etc. is a strictly decreasing sequence of closed subsets of X which must stabilize since X is noetherian.

If $\mathcal{W}$ has a splitting sequence of length zero this means that $\coprod p_i$ splits as a morphism in which case the exactess is a formality. Let $(\mathrm{X} = \mathrm{Z}_0, \dots, \mathrm{Z}_n, \mathrm{Z}_{n+1} = \emptyset)$ be a splitting sequence of minimal length for $\mathcal{W}$. Let us choose a splitting $s$ for the morphism $p^{-1}(\mathrm{Z}_n) \to \mathrm{Z}_n$. Since $p$ is étale we have a decomposition $p^{-1}(\mathrm{Z}_n) = Im(s) \coprod Y$ where $Y$ is a closed subset of $\coprod W_i$. Let $U = X - Z_n$ and let $V = (\coprod W_i) - Y$. Clearly $U$ and $V$ form an elementary distinguished square over $X$ and family of morphisms

$\mathcal{W} \times_{\mathrm{X}} \mathrm{U} \to \mathrm{U}$ is a Nisnevich covering of $\mathrm{U}$ with a splitting sequence of length $n - 1$. Therefore, by induction and our assumption of $\mathrm{F}$ the sequences

$$
\begin{array}{l}\mathbf {F} (\mathbf {X}) \to \mathbf {F} (\mathbf {U}) \times \mathbf {F} (\mathbf {V}) \rightrightarrows \mathbf {F} (\mathbf {U} \times_ {\mathbf {X}} \mathbf {V})\\\mathbf {F} (\mathbf {U}) \to \prod \mathbf {F} (\mathbf {W} _ {i} \times_ {\mathbf {X}} \mathbf {U}) \rightrightarrows \prod \mathbf {F} (\mathbf {W} _ {i} \times_ {\mathbf {X}} \mathbf {W} _ {j} \times_ {\mathbf {X}} \mathbf {U})\end{array}
$$

are exact. Since both morphisms  $U \rightarrow X$  and  $V \rightarrow X$  factor through  $\coprod W_{i}$  this implies the required exactness by diagram chase.

Lemma 1.6. — Any elementary distinguished square (cf Definition 1.3) is a cocartesian square in the category $Shv(Sm/S)_{\mathbb{N}is}$. In particular, the canonical morphism of Nisnevich sheaves $V/(U \times_X V) \to X/U$ is an isomorphism.

Proof. — This is a formal consequence of the fact that the morphism  $UIV \rightarrow X$  is an epimorphism of sheaves, the fact that  $U \rightarrow X$  is a monomorphism and that the Nisnevich sheaf associated to the fibre product  $U \times_{X} V$  is indeed the fibre product in the category of sheaves.

Remark 1.7. — Let F be a sheaf of abelian groups on the small Nisnevich site  $X_{Nis}$  of X. If U is an object of  $X_{Nis}$  and  $Z_{Nis}[U]$  is the sheaf of abelian groups on  $X_{Nis}$  freely generated by the sheaf of sets represented by U then the adjointness implies that for any  $i \in Z$  one has a canonical isomorphism  $Ext^{i}(\mathbf{Z}_{Nis}[U], \mathbf{F}) = \mathbf{H}_{Nis}^{i}(U, \mathbf{F})$ . Lemma 1.6 implies that for any elementary distinguished square the sequence of sheaves of abelian groups

$$
0 \to {\bf Z} _ {\mathcal {N} \bar {s}} [ {\bf U} \times_ {\bf X} {\bf V} ] \to {\bf Z} _ {\mathcal {N} \bar {s}} [ {\bf U} ] \oplus {\bf Z} _ {\mathcal {N} \bar {s}} [ {\bf V} ] \to {\bf Z} _ {\mathcal {N} \bar {s}} [ {\bf X} ] \to 0
$$

is exact. Combining this fact with the previous remark on cohomology groups we conclude that for any F and any elementary distinguished square we have the following “generalized” Mayer-Vietoris long exact sequence:

$$
\begin{array}{l} \ldots \to \mathrm{H} _ {\mathcal {N} \bar {s}} ^ {i} (\mathrm{X}, \mathrm{F}) \to \mathrm{H} _ {\mathcal {N} \bar {s}} ^ {i} (\mathrm{U}, \mathrm{F}) \oplus \mathrm{H} _ {\mathcal {N} \bar {s}} ^ {i} (\mathrm{V}, \mathrm{F}) \to \mathrm{H} _ {\mathcal {N} \bar {s}} ^ {i} (\mathrm{U} \times_ {\mathrm{X}} \mathrm{V}, \mathrm{F}) \\ \to \mathrm{H} _ {\mathcal {N} \bar {s}} ^ {i + 1} (\mathrm{X}, \mathrm{F}) \to \ldots \end{array}
$$

Proposition 1.8. — Let S be a noetherian scheme of dimension  $\leqslant d$ , then for any sheaf of abelian groups F on  $Sm/S_{Nis}$  one has  $\mathrm{H}_{\mathcal{Nis}}^{i}(\mathrm{S},\mathrm{F})=0$  for i>d.

Proof. — (Sketch) See [30, Lemma E.6.(c)] By induction assume that the proposition is known for schemes of dimension less than d. The Leray spectral sequence applied to the obvious morphism of sites  $(Sm/S)_{\mathcal{Nis}} \rightarrow (Sm/S)_{Zar}$  together with the cohomological dimension theorem for Zariski topology implies that it is sufficient to prove the proposition for local S. Let s be the closed point of S. Since the Nisnevich sheaves associated with the cohomology presheaves  $H^{i}$  are zero for i > 0 we conclude

that for any element $a$ in $\mathrm{H}_{\mathcal{N}s}^{i}(\mathrm{S})$ there exists an étale morphism $\mathrm{V} \to \mathrm{S}$ such that $\mathrm{U} = \mathrm{S} - s$ and $\mathrm{V}$ form an elementary distinguished square and $a_{|\mathrm{V}} = 0$. It follows now from Remark 1.7 and the inductive assumption that for $i > dim(\mathrm{S})$ we have $a = 0$. Finally let us mention the following fact.

Proposition 1.9. — For any sheaf of abelian groups F on  $(Sm/S)_{Nis}$  and any  $n \geqslant 0$  the canonical morphism  $\check{\mathrm{H}}_{\mathcal{N}is}^{n}(\mathrm{S}, \mathrm{F}) \to \mathrm{H}_{\mathcal{N}is}^{n}(\mathrm{S}, \mathrm{F})$ , where the left hand side refers to the Čech cohomology groups, is an isomorphism.

Proof. — The proof is identical to the one given in [24, III.2.17] for the étale topology with the reference to [1, Th. 3.4(iii)] replaced by the reference to [1, Th. 3.4(i)].

Example 1.10. — Let us give an example which shows that Proposition 1.9 is false for Zariski topology. Let  $x_{0}, x_{1}$  be two closed points of  $A^{2}$  over a field k. Let S be the spectrum of the semilocal ring of  $x_{0}, x_{1}$ . Any Zariski open covering for S has a refinement which consists of exactly two open subsets and therefore  $\check{\mathrm{H}}_{\mathcal{Z}ar}^{i}(\mathrm{S}, \mathrm{F}) = 0$  for any F and any i > 1.

Let us show that there exists a sheaf F such that  $\mathrm{H}_{\mathcal{Z}ar}^{2}(\mathrm{S},\mathrm{F})\neq0$ . Choose two irreducible curves  $C_{1},C_{2}$  on S such that  $C_{1}\cap C_{2}=\{x_{0},x_{1}\}$  and let  $\mathrm{U}=\mathrm{S}-(\mathrm{C}_{1}\cup\mathrm{C}_{2}),\mathrm{V}=\mathrm{S}-\{x_{0},x_{1}\}$ . Denote the open embedding  $U\to S$  by j and the open embedding  $U\to V$  by  $j'$ . We claim that  $\mathrm{H}^{2}(\mathrm{S},j_{!}(\mathbf{Z}))\neq0$ . Looking at the Mayer-Vietoris exact sequence for the covering  $\mathrm{V}=(\mathrm{V}-\mathrm{V}\cap\mathrm{C}_{1})\cup(\mathrm{V}-\mathrm{V}\cap\mathrm{C}_{2})$  we get a canonical element in  $\mathrm{H}^{1}(\mathrm{V},j_{!}^{\prime}(\mathbf{Z}))$  (since the intersection of these two open subsets is U) and looking at the Mayer-Vietoris exact sequence for the covering  $\mathrm{S}=(\mathrm{S}-\{x_{0}\})\cup(\mathrm{S}-\{x_{1}\})$  we get a canonical element in  $\mathrm{H}^{2}(\mathrm{S},j_{!}(\mathbf{Z}))\neq0$  (since the intersection of these two open subsets is V). One verifies easily that since the curves  $C_{1},C_{2}$  are irreducible this element is not zero.

## Simplicial presheaves with the B.G.-property

For any presheaf F on  $(Sm/S)_{\mathcal{Nis}}$  and any left filtering diagram  $X_{\alpha}$  of smooth schemes over S with affine transition morphisms and the limit scheme X we denote by  $F(X)$  the set  $colim_{\alpha}F(X_{\alpha})$ . For example, for any smooth S-scheme X and any point x of X the set  $F(Spec\mathcal{O}_{X,x})$  (resp.  $F(Spec\mathcal{O}_{X,x}^{h})$ ) is the filtering colimit of the sets  $F(U)$  over the categories of Zariski and Nisnevich neighborhoods of x respectively. The family of functors  $F \mapsto F(Spec\mathcal{O}_{X,x}^{h})$  parameterized by all pairs  $(X,x)$  with  $X \in Sm/S$  and  $x \in X$  forms a conservative family of points of  $(Sm/S)_{\mathcal{Nis}}$  (use [13, IV.6.5]). This observation leads to the following “explicit” description of simplicial weak equivalences in  $\Delta^{op}Shv((Sm/S)_{\mathcal{Nis}})$ .

Lemma 1.11. — A morphism $\mathbf{F} \to \mathbf{G}$ of simplicial sheaves on $Sm/S$ is a simplicial weak equivalence if and only if for any smooth $X$ over $S$ and any point $x$ of $X$ the map $\mathrm{F}(\operatorname{Spec}(\mathcal{O}_{X,x}^{h})) \to \mathrm{G}(\operatorname{Spec}(\mathcal{O}_{X,x}^{h}))$ is a weak equivalence of simplicial sets.

Definition 1.12. — A B.G. class of objects in Sm/S is a class $\mathcal{A}$ of objects in Sm/S such that:

1. for any $\mathbf{X}$ in $\mathcal{A}$ and any open immersion $\mathrm{U} \to \mathrm{X}$ we have $\mathrm{U} \in \mathcal{A}$;

2. any smooth S-scheme X has a Nisnevich covering (see 1.2) which consists of objects in A.

The basic examples we have in mind is the class of quasi-affine smooth S-scheme and that of quasi-projective smooth S-schemes. If not otherwise stated, it will always be understood that we consider the B.G. class of quasi-affine smooth S-schemes. Let A be any B.G. class of objects in Sm/S.

Definition 1.13. — A simplicial presheaf $\mathcal{K}$ on $(\mathrm{Sm} / \mathrm{S})_{\mathrm{Nis}}$ is said to have the B.G.-property with respect to $\mathcal{A}$ if for any elementary distinguished square as in 1.3 such that X and V belong to $\mathcal{A}$ the square of simplicial sets

$$
\begin{array}{c c c} \mathcal {X} (\mathrm{X}) & \longrightarrow & \mathcal {X} (\mathrm{V}) \\ \Big \downarrow & & \Big \downarrow \\ \mathcal {X} (\mathrm{U}) & \longrightarrow & \mathcal {X} (\mathrm{U} \times_ {\mathrm{X}} \mathrm{V}) \end{array}
$$

is homotopy cartesian.

Remark 1.14. — Note that the property of having the B.G.-property is invariant with respect to weak equivalences of presheaves, i.e. if $\mathcal{X} \to \mathcal{X}'$ is a morphism of simplicial presheaves on $(Sm/S)$ such that for any $U \in \mathcal{A}$ the map of simplicial sets $\mathcal{X}(U) \to \mathcal{X}'(U)$ is a weak equivalence then $\mathcal{X}$ has the B.G.-property with respect to $\mathcal{A}$ if and only if $\mathcal{X}'$ has.

Remark 1.15. — For any simplicial sheaf $\mathcal{X}$ and an elementary distinguished square as in 1.3 the corresponding square of simplicial sets is cartesian (see Proposition 1.4). Thus if $\mathcal{X}$ is a simplicial sheaf such that for any open embedding $U \to V$ with $V \in \mathcal{A}$ the map of simplicial sets $\mathcal{X}(V) \to \mathcal{X}(U)$ is a fibration then $\mathcal{X}$ has the B.G.-property with respect to $\mathcal{A}$. For example a simplicially fibrant $\mathcal{X}$ has this property.

Proposition 1.16. — A simplicial sheaf $\mathcal{X}$ on the category $(Sm/S)_{Nis}$ has the B.G.-property with respect to $\mathcal{A}$ if and only if for any trivial cofibration $\mathcal{X} \to \mathcal{X}'$ such that $\mathcal{X}'$ is fibrant and any U in $\mathcal{A}$ the morphism of simplicial sets $\mathcal{X}(U) \to \mathcal{X}'(U)$ is a weak equivalence.

Proof. — The “if” part is trivial (see Remarks 1.14, 1.15). To prove the “only if” part we need an analog of [7, Theorem 1] for Nisnevich topology. Let X be a Noetherian scheme of finite dimension. Denote by  $X_{Nis}$  the small Nisnevich site of X (i.e. the category of étale schemes over X considered with the Nisnevich topology).

A B.G.-functor on  $X_{Nis}$  is a family of contravariant functors  $T_{q}, q \geqslant 0$  from  $X_{Nis}$  to the category of pointed sets, together with pointed maps  $\partial_{Q}: T_{q+1}(U \times_{X} V) \to T_{q}(X)$  given for all elementary distinguished squares in  $X_{Nis}$, such that the following two conditions hold:

1. the morphisms $\partial_{\mathbb{Q}}$ are natural with respect to morphisms of elementary distinguished squares;

2. for any $q \geqslant 0$ the sequence of pointed sets

$$
\mathbf {T} _ {q + 1} (\mathbf {U} \times_ {\mathbf {X}} \mathbf {V}) \rightarrow \mathbf {T} _ {q} (\mathbf {X}) \rightarrow \mathbf {T} _ {q} (\mathbf {U}) \times \mathbf {T} _ {q} (\mathbf {V})
$$

is exact.

Lemma 1.17. — Let  $(\mathrm{T}_{q}, \partial_{\mathrm{Q}})$  be a B.G.-functor on  $X_{Nis}$  such that the Nisnevich sheaves associated with  $T_{q}$  are trivial (i.e. isomorphic to the point sheaf pt) for all q. Then  $T_{q} = pt$  for all q.

Proof. — Restricting  $T_{q}$  to the small Zariski site of X we get a family of functors satisfying the conditions of [7, Theorem 1']. Thus it is sufficient to show that Zariski sheaves associated to  $T_{q}$ 's are trivial i.e. that for any point x on X we have  $\mathrm{T}_{q}(\mathrm{Spec}(\mathcal{O}_{\mathrm{X},x})) = *$ . Let  $t \in \mathrm{T}_{q}(\mathrm{Spec}(\mathcal{O}_{\mathrm{X},x}))$  be an element and let  $\mathrm{U} = \mathrm{Spec}(\mathcal{O}_{\mathrm{X},x}) - \{x\}$ . Then  $dim(\mathrm{U}) < dim(\mathrm{X})$  and by obvious induction by dimension we may assume that  $\mathrm{T}_{q}(\mathrm{U}) = *$  for all q. On the other hand since the Nisnevich sheaves associated to  $T_{q}$  are zero there exists an étale morphism  $p : V \to Spec(\mathcal{O}_{\mathrm{X},x})$  which splits over x and such that  $p^{*}(t) = *$ . Shrinking V we may assume that  $p^{-1}(x) \to x$  is an isomorphism and therefore U and V form an elementary distinguished square which implies the result we need.

The following lemma finishes the proof of Proposition 1.16.

Lemma 1.18. — Let $\mathcal{X} \to \mathcal{Y}$ be a morphism of simplicial presheaves such that the associated morphism of simplicial sheaves is a weak equivalence and suppose that both $\mathcal{X}$ and $\mathcal{Y}$ have the B.G.-property with respect to $\mathcal{A}$. Then for any U in $\mathcal{A}$ the morphism of simplicial sets $\mathcal{X}(U) \to \mathcal{Y}(U)$ is a weak equivalence.

Proof. — Consider the (simplicial) model category structure on the category of simplicial presheaves  $\Delta^{op}Preshv(T)$  given by applying Theorem 1.4 to the site  $T'$  with

the same underlying category as T but with trivial topology. The axiom MC5 implies that there exists a commutative square of simplicial presheaves

![](images/page_58_image_1.jpg)

such that for any smooth scheme U over S, the maps  $\mathcal{X}(U) \to \mathcal{X}'(U)$  and  $\mathcal{Y}(U) \to \mathcal{Y}'(U)$  are weak equivalences of simplicial sets and the map  $\mathcal{X}'(U) \to \mathcal{Y}'(U)$  is a Kan fibration of Kan simplicial sets. Replacing X, Y by  $X'$,  $Y'$  we may assume that the maps  $\mathcal{X}(U) \to \mathcal{Y}(U)$  are Kan fibrations between Kan simplicial sets.

It is sufficient to prove that for any U in A and  $x \in \mathcal{Y}(U)$  the fiber  $\mathrm{K}_{x}(\mathrm{U})$  of the map  $\mathcal{X}(\mathrm{U}) \to \mathcal{Y}(\mathrm{U})$  over x is contractible (i.e. weakly equivalent to point and in particular non empty). The simplicial presheaf  $V/U \mapsto K(V/U)$  on  $(Sm/U)_{Nis}$ , clearly has the B.G.-property with respect to A/U which means that we may further replace Y by pt in which case we have to show that the (Kan) simplicial set  $\mathcal{X}(S)$  is contractible.

Assume first that $\mathcal{X}(\mathrm{S}) \neq \emptyset$ and let $a \in \mathcal{X}(\mathrm{S})$ be an element. Consider the family of functors $\mathrm{T}_i$ on $\mathrm{S}_{\mathcal{N}\bar{\imath}s}$ of the form

$$
\mathrm{U} \mapsto \pi_ {i} (\mathcal {K} (\mathrm{U}), a _ {| \mathrm{U}}).
$$

It is a B.G.-functor and the associated Nisnevich sheaves are trivial since $\mathcal{X} \to pt$ is a weak equivalence. Contractibility of $\mathcal{X}(S)$ follows now from Lemma 1.17.

It remains to prove that $\mathcal{X}(\mathrm{S})$ is not empty. We already know that for any V/S such that $\mathcal{X}(\mathrm{V})$ is not empty it is contractible. Let $s$ be a point of S. Let us show first that there exists an open neighborhood V of $s$ such that $\mathcal{X}(\mathrm{V}) \neq \emptyset$. We may clearly assume that S is local and $s$ is the closed point of S. Using induction by dimension of S we may assume that $\mathcal{X}(\mathrm{S} - s) \neq \emptyset$. Since the map $\mathcal{X} \to pt$ is a weak equivalence there exists a Nisnevich neighborhood V of $s$ in S such that $\mathcal{X}(\mathrm{V}) \neq \emptyset$. Shrinking V we may assume that the pair $\{\mathrm{S} - s \subset \mathrm{S}, \mathrm{V} \to \mathrm{S}\}$ gives an elementary distinguished square and therefore $\mathcal{X}(\mathrm{S}) \neq \emptyset$ by the corresponding homotopy cartesian square.

To finish the proof of the lemma take U to be a maximal Zariski open subset of S such that  $\mathcal{X}(U) \neq \emptyset$  (it always exist since S is noetherian). Assume that there is a point  $s \in S$  outside U. Then there exists an open neighbourhood V of s in S such that  $\mathcal{X}(V) \neq \emptyset$ . Using the fact that X has the B.G.-property for the elementary distinguished square formed by U and V we conclude that  $\mathcal{X}(U \cup V) \neq \emptyset$ , which contradicts the maximality of U.

## Functoriality in S

For any morphism of schemes  $f: S_{1} \to S_{2}$  the functor of base change gives a continuous map of sites  $f: (Sm/S_{1})_{\mathcal{Nis}} \to (Sm/S_{2})_{\mathcal{Nis}}$ . The following example shows that

this map is not in general a morphism of sites, i.e. the corresponding functor of the inverse image does not have to commute with fiber products.

Example 1.19. — Let k be a field. Consider the morphism  $f: \text{Spec}(k) \to \mathbf{A}_{k}^{1}$  which corresponds to the point 0. Let us show that the corresponding functor of inverse image

$$
f ^ {*}: S h v _ {\mathcal {N i s}} (S m / \mathbf {A} ^ {1}) \rightarrow S h v _ {\mathcal {N i s}} (S m / k)
$$

does not commute with fiber products. Let  $X=A^{2}$  which is considered as a smooth scheme over  $A^{1}$  by means of the second coordinate. Let  $Y_{+}, Y_{-}$ be closed subschemes of X given by the equations  $x+y=0$  and x-y=0 respectively. Note that there are smooth over  $A^{1}$ . Then  $Y_{+}\times_{X}Y_{-}$ is the sheaf on  $Sm/A^{1}$  represented by the  $A^{1}$ -scheme of equation x=0, y=0 in  $A^{2}$  which is empty. On the other hand  $f^{*}(Y_{+})=f^{*}(Y_{-})=pt$  and therefore  $f^{*}(Y_{+})\times_{f^{*}(X)}f^{*}(Y_{-})=pt$  which proves our claim.

(Note that the same setup may be used to show that the continuous map of sites  $(Sch/k)_{\mathcal{Nis}} \rightarrow (Sm/k)_{\mathcal{Nis}}$  is not a morphism of sites.)

Proposition 1.20. — For any morphism of schemes $f: \mathrm{S}_{1} \to \mathrm{S}_{2}$ the corresponding continuous map of sites $(\mathrm{Sm}/\mathrm{S}_{1})_{\mathbb{N}\bar{s}} \to (\mathrm{Sm}/\mathrm{S}_{2})_{\mathbb{N}\bar{s}}$ is reasonable (see 1.55). In particular the corresponding functor

$$
\mathbf {R} f _ {*}: \mathscr {H} _ {s} ((S m / S _ {1}) _ {\mathcal {N i s}}) \rightarrow \mathscr {H} _ {s} ((S m / S _ {2}) _ {\mathcal {N i s}})
$$

has a left adjoint $\mathbf{L}f^{*}$ and for a composable pair of morphisms of schemes $f, g$ one has canonical isomorphisms of functors between homotopy categories of the form

$$
\mathbf {R} (g \circ f) _ {*} \cong \mathbf {R} g _ {*} \circ \mathbf {R} f _ {*}
$$

$$
\mathbf {L} (g \circ f) ^ {*} \cong \mathbf {L} f ^ {*} \circ \mathbf {L} g ^ {*}.
$$

Proof. — It is clear that for any f and any simplicial sheaf X on  $(Sm/S_{1})_{Nis}$  with the B.G.-property the sheaf  $f_{*}(\mathcal{X})$  on  $(Sm/S_{2})_{Nis}$  also has the B.G.-property which implies that f is reasonable by Proposition 1.16 in view of Definition 1.49.

Remark 1.21. — One can verify easily that the statement of Propositions 1.20 also holds in the Zariski and étale topologies. A general proof working for all three cases can be obtained using the fact that in all of them there is a notion of the small site over a smooth scheme X (Zariski, Nisnevich or étale) which has fiber products preserved by the base change functors for arbitrary morphisms of base schemes.

Example 1.22. — In the notations of Example 1.19 consider the quotient sheaf  $\mathbf{F} = \mathbf{X}/(\mathbf{Y}_{-} \cup \mathbf{Y}_{+})$ . We claim that the canonical morphism  $\mathbf{L} f^{*}(\mathbf{F}) \to f^{*}(\mathbf{F})$  is not a

weak equivalence. Since the morphism  $Y_{-}\coprod Y_{+}\to X$  is a monomorphism on  $Sm/A^{1}$  the canonical morphism  $cone(Y_{-}\coprod Y_{+}\to X)\to F$  is a weak equivalence. By Lemma 1.53 and Proposition 1.57(2) this implies that we have an isomorphism  $\mathbf{L}f^{*}(\mathbf{F})\cong cone(f^{*}(Y_{-}\coprod Y_{+})\to f^{*}(\mathbf{X}))$  (in the homotopy category). Since  $f^{*}(Y_{-}\coprod Y_{+})\to f^{*}(\mathbf{X})$  is clearly not a monomorphism the simplicial sheaf  $\mathbf{L}f^{*}(\mathbf{F})$  has a nontrivial  $\underline{\pi}_{1}$  and in particular is not weakly equivalent to  $f^{*}(\mathbf{F})$ .

Proposition 1.23. — Let $f: \mathrm{S}_{1} \to \mathrm{S}_{2}$ be a smooth morphism. Then there exists a functor $f_{\#}: Shv_{\mathcal{Nis}}(Sm/S_{1}) \to Shv_{\mathcal{Nis}}(Sm/S_{2})$ left adjoint to $f^{*}$ which has the following properties:

1. for a smooth scheme U over  $S_{1}$  the sheaf  $f_{\#}(U)$  is represented by the smooth scheme U over  $S_{2}$ ;

2. for any sheaves $\mathbf{F}$ on $Sm / S_1$ and $\mathbf{G}$ on $Sm / S_2$ the canonical morphism $f_{\#}(\mathbf{F} \times f^{*}(\mathbf{G})) \to f_{\#}(\mathbf{F}) \times \mathbf{G}$ is an isomorphism.

Proof. — Let $\phi^{-1}(f): Sm/S_1 \to Sm/S_2$ denote the functor

$$
(\pi : \mathrm{V} \rightarrow \mathrm{S} _ {1}) \mapsto (f \circ \pi : \mathrm{V} \rightarrow \mathrm{S} _ {2}).
$$

This defines a continuous map of sites $\phi(f): (Sm/S_2)_{Nis} \to (Sm/S_1)_{Nis}$ ($cf$ 1) because for any sheaf F on $(Sm/S_2)_{Nis}$ the presheaf U $\mapsto$ F($\phi^{-1}(f)(U)$) is a sheaf on $(Sm/S_1)_{Nis}$ (the functor $\phi^{-1}(f): Sm/S_1 \to Sm/S_2$ sends covering families to covering families). Correspondingly we have a pair of adjoint functors $(\phi(f))_*$ and $(\phi(f))^*$ acting between the corresponding categories of sheaves. One can easily see that $(\phi(f))_* = f^*$ and therefore $f_\# = (\phi(f))^*$ is left adjoint to the inverse image functor $f^*$. The properties of $f_\#$ stated in the proposition follow immediately from definitions.

Corollary 1.24. — Let $f: \mathrm{S}' \to \mathrm{S}$ be a scheme over $\mathrm{S}$ which is a filtering limit of a diagram of smooth schemes over $\mathrm{S}$ with affine transition morphisms (cf [15, 8.2]). Then $f: (\mathrm{Sm}/\mathrm{S}')_{\mathbb{N}is} \to (\mathrm{Sm}/\mathrm{S})_{\mathbb{N}is}$ is a morphism of sites, and in particular (cf 1.47) the functor $f^*$ preserves weak equivalences.

Same argument as in the proof of Proposition 1.20 implies that the continuous map of sites $\phi(f): (Sm/S_2)_{Nis} \to (Sm/S_1)_{Nis}$ associated to a smooth morphism of schemes $f: S_1 \to S_2$ is reasonable (cf 1.55). Therefore, the functor of inverse image $f^* = (\phi(f))_*$ between the corresponding homotopy categories of simplicial sheaves has a left adjoint which we denote by $\mathbf{L}f_\#$. Note that the continuous map $\phi(f)$ is not a morphism of sites unless $f$ is an isomorphism. The following example shows that the functor $f_\#$ does not have to preserve weak equivalence.

Example 1.25. — Keep the notations of examples 1.19, 1.22. Let $\phi$ denote the morphism $Y_{+} \coprod Y_{-} \to X$ over $A^{1}$ and $\psi : cone(\phi) \to F$ the obvious morphism (of simplicial sheaves); recall that $\psi$ is a simplicial weak equivalence. Consider now the

projection  $p : A^{1} \to Spec(k)$ . The functor  $p_{\#}$  commutes with colimits and therefore we have

$$
\begin{array}{l} p _ {\#} (\mathbf {F}) = \mathbf {A} ^ {2} / (\mathbf {A} ^ {1} \cup \mathbf {A} ^ {1}) \\ p _ {\#} (c o n e (\phi)) = c o n e (\mathbf {A} ^ {1} \amalg \mathbf {A} ^ {1} \to \mathbf {A} ^ {2}). \end{array}
$$

Thus the morphism  $p_{\#}(\psi)$  is not a simplicial weak equivalence since  $p_{\#}(\phi)$  is not a monomorphism of sheaves on  $Sm/Spec(k)$  and therefore  $p_{\#}(cone(\phi))$  has a nontrivial  $\underline{\pi}_{1}$  while  $p_{\#}(F)$  does not.

Proposition 1.26. — Let $p: \mathrm{S}_1 \to \mathrm{S}_2$ be an étale morphism. Then the functor $p_{\#}$ preserves simplicial weak equivalences.

Proof. — For any site T and an object X in T the base change functor  $T/X \to T$  is a morphism of sites and the corresponding inverse image functor  $Shv(T) \to Shv(T/X)$  has a left adjoint  $f_{\#}$  which preserves simplicial weak equivalences. It remains to observe that for an étale p we have  $Sm/S_{1} \cong (Sm/S_{2})/S_{1}$ .

The following proposition is a simplicial analog of the fact that the functor of direct image for Nisnevich sheaves of abelian groups associated to a finite morphism is exact.

Proposition 1.27. — Let $f: S_{1} \to S_{2}$ be a finite morphism. Then the functor $f_{*}$ preserves weak equivalences of simplicial sheaves. Thus, for any simplicial sheaf $\mathcal{X}$ on $(Sm/S_{1})_{\text{Nis}}$ the canonical morphism $f_{*}(\mathcal{X}) \to \mathbf{R}f_{*}(\mathcal{X})$ is a weak equivalence.

Proof. — Let  $a: X \to X'$  be a weak equivalence. Let's show that the morphism  $f_{*}(a)$  is again a weak equivalence. Let U be a smooth scheme over  $S_{2}$  and u be a point of U. Consider the point  $(U, u)^{*}: F \mapsto F(SpecO_{U,u}^{h})$  of  $(Sm/S_{2})_{Nis}$  associated to the pair  $(U, u)$ . By Lemma 1.11 all we have to check is that the morphism

$$
(\mathrm{U}, u) ^ {*} (f _ {*} (a)): (\mathrm{U}, u) ^ {*} (f _ {*} (\mathscr {K} _ {1})) \rightarrow (\mathrm{U}, u) ^ {*} (f _ {*} (\mathscr {K} _ {1}))
$$

is a weak equivalence of simplicial sets. Since a scheme finite over a henselian local scheme is a disjoint union of henselian local schemes one verifies immediately that for any simplicial sheaf $\mathcal{X}$ one has $(\mathrm{U}, u)^*(f_*(\mathcal{X})) = (\mathrm{U} \times_{\mathrm{S}_2} \mathrm{S}_1, u)^*(\mathcal{X})$ which implies that the morphism in question is a weak equivalence.

## 3.2. The  $A^{1}$ -homotopy categories

The  $A^{1}$ -model category structure on  $\Delta^{op}Shv_{Nis}(Sm/S)$

Let us recall the basic definitions of Section 3 in the context of the site with interval  $((Sm/S)_{\mathcal{Nis}}, \mathbf{A}^{1})$ .

Definition 2.1. — A simplicial sheaf $\mathcal{K}$ on $(Sm/S)_{Nis}$ is called $\mathbf{A}^1$-local if for any simplicial sheaf $\mathcal{Y}$ the map

$$
H o m _ {\mathscr {H} _ {s} ((S m / S) _ {\mathcal {N i s}})} (\mathscr {Y}, \mathscr {X}) \rightarrow H o m _ {\mathscr {H} _ {s} ((S m / S) _ {\mathcal {N i s}})} (\mathscr {Y} \times \mathbf {A} ^ {1}, \mathscr {X})
$$

induced by the projection $\mathcal{Y} \times \mathbf{A}^1 \to \mathcal{Y}$ is a bijection.

A morphism of simplicial sheaves $f: \mathcal{X} \to \mathcal{Y}$ is called an $\mathbf{A}^{1}$-weak equivalence if for any $\mathbf{A}^{1}$-local, simplicially fibrant sheaf $\mathcal{Z}$ the map of simplicial sets

$$
\mathrm{S} (\mathcal {Y}, \mathcal {Z}) \rightarrow \mathrm{S} (\mathcal {X}, \mathcal {Z})
$$

induced by $f$ is a weak equivalence.

A morphism of simplicial sheaves $f: \mathcal{X} \to \mathcal{Y}$ is called an $\mathbf{A}^{1}$-fibration if it has the right lifting property with respect to monomorphisms which are $\mathbf{A}^{1}$-weak equivalences.

As was shown in Section 3 the classes of $\mathbf{A}^1$-weak equivalences, monomorphisms and $\mathbf{A}^1$-fibrations form a proper simplicial model structure on the category of simplicial sheaves on $(Sm/S)_{Nis}$. The corresponding homotopy category, i.e. the localization of the category of simplicial sheaves on $(Sm/S)_{Nis}$ with respect to the class of $\mathbf{A}^1$-weak equivalences is called the homotopy category of smooth schemes over S. We denote this category by $\mathcal{H}(S)$.

Example 2.2. — For any vector bundle $\mathcal{E}$ over a smooth scheme X the morphism $\mathcal{E} \to X$ is an $\mathbf{A}^1$-weak equivalence since it is a strict $\mathbf{A}^1$-homotopy equivalence.

Example 2.3. — Let T be a Zariski torsor for a vector bundle E over the smooth scheme X over S. Then the morphism  $T \rightarrow X$  is an  $A^{1}$ -weak equivalence. It follows from Lemma 2.16 applied to the class C of sheaves represented by smooth schemes over S which are affine (over  $Spec(\mathbf{Z})$ ), Example 2.2 and the fact that any such torsor is trivial when the base is affine over  $Spec(\mathbf{Z})$ . More generally any smooth morphism  $Y \rightarrow X$  of schemes which is a locally trivial fibration in the Nisnevich topology with an  $A^{1}$ -contractible fiber is an  $A^{1}$ -weak equivalence.

Example 2.4. — Let X be any scheme over S which is  $A^{1}$ -rigid in the sense that for any smooth scheme U over S the map  $Hom_{\mathrm{S}}(\mathrm{U},\mathrm{X})\to Hom_{\mathrm{S}}(\mathrm{U}\times\mathbf{A}^{1},\mathbf{X})$  is a bijection. Then the (simplicial) sheaf represented by X is  $A^{1}$ -local and for any smooth S-scheme U the map  $Hom_{\mathrm{S}}(\mathrm{U},\mathrm{X})\to[\mathrm{U},\mathrm{X}]$  is a bijection (use 1.14). For example any smooth morphism  $X\to S$  whose fibers are either smooth curves of genus  $\geqslant1$  or the affine line minus a point, is  $A^{1}$ -rigid in this sense when S is integral.

Remark 2.5. — Assume S is local henselian (for example a field). Then it follows from corollary 3.22 that for any simplicial sheaf X, the map  $\mathcal{X}_{0}(S) \to [S, \mathcal{X}]$  is

surjective. Thus to have an S-point is a property on a simplicial sheaf $\mathcal{X}$ which is invariant under $\mathbf{A}^1$-weak equivalences.

Let $\Delta_{\mathbf{A}^1}^\bullet$ be the cosimplicial object in $Sm / S$ given by

$$
\Delta_ {\mathbf {A} ^ {1}} ^ {n} = \mathrm{S} \times_ {S p e c (\mathbf {Z})} S p e c \mathbf {Z} [ x _ {0},..., x _ {n} ] / (\sum x _ {i} = 1)
$$

with usual coface and codegeneracy morphisms. As was shown in [31] it is isomorphic to the cosimplicial object constructed from the interval $\mathbf{A}^1$ by the procedure described in Section 3. In particular the results of this section can be applied to the functor $Sing_{*}(-)$ constructed by means of $\Delta_{\mathbf{A}^1}^{\bullet}$.

Choose a resolution functor  $(Ex(-), \theta)$  (for the simplicial model category structure 1.6). Then set:

$$
E x _ {\mathbf {A} ^ {1}} = E x \circ (E x \circ S i n g _ {*}) ^ {\mathbf {N}} \circ E x.
$$

By Lemma 2.13 and Lemma 3.12 for any $\mathcal{X}$ the canonical morphism $\mathcal{X} \to Ex_{\mathbf{A}^1}(\mathcal{X})$ is a monomorphism and an $\mathbf{A}^1$-weak equivalence. The following lemma shows that this functor is indeed an $\mathbf{A}^1$-resolution functor.

Lemma 2.6. — For any simplicial sheaf $\mathcal{X}$ the object $Ex_{\mathbf{A}^1}(\mathcal{X})$ is $\mathbf{A}^1$-fibrant.

Observe the difference with Lemma 3.20:  $\omega$  is chosen to be N and one has to compose one more time with Ex to make sure the result is fibrant.

Proof. — It is sufficient to check the fourth condition of Proposition 3.19. Since the site  $(Sm/S)_{\mathcal{N}is}$  is Noetherian and since all the objects  $(Ex \circ Sing_{*})^{n}(Ex(\mathcal{X}))$  have the B.G.-property with respect to the class Sm/S, so does  $\mathcal{X}' := (Ex \circ Sing_{*})^{\mathrm{N}}(Ex(\mathcal{X}))$ . Thus from Proposition 1.16 it is sufficient to show that for any smooth S-scheme U and any  $x : U \to X'$  the maps  $\pi_{i}(\mathcal{X}'(U), x) \to \pi_{i}(\mathcal{X}'(U \times A^{1}), x)$  induced by the morphism  $Id \times \{0\} : U \to U \times A^{1}$  are epimorphisms for all  $i \geqslant 0$ . One then finishes exactly in the same way as in the proof of Lemma 3.21.

The following example shows that for a sheaf of sets F the simplicial sheaf  $Sing_{*}(F)$  does not have to be  $A^{1}$ -local.

Example 2.7. — Let $S = \text{Spec}(k)$ where $k$ is a field. Consider the covering of $\mathbf{A}_k^1$ by two open subsets $U_0 = \mathbf{A}^1 - \{0\}$, $U_1 = \mathbf{A}^1 - \{1\}$ and let $U_{01} = U_0 \cap U_1$. Choose a closed embedding $j: U_{01} \to \mathbf{A}_k^n$ for some $n$. Define $F$ as the coproduct $F = (U_0 \times \mathbf{A}^n) \cup_{U_{01}} (U_1 \times \mathbf{A}^n)$ where the morphism $U_{01} \to U_i \times \mathbf{A}^n$ is the product of $j$ with the open embedding $U_{01} \to U_i$. Let $X$ be a connected smooth scheme over $k$. Then

$$
\mathbf {F} (\mathbf {X}) = H o m (\mathbf {X}, \mathrm{U} _ {0} \times \mathbf {A} ^ {n}) \cup_ {H o m (\mathbf {X}, \mathrm{U} _ {0 1})} H o m (\mathbf {X}, \mathrm{U} _ {1} \times \mathbf {A} ^ {n})
$$

and since  $Hom(\mathbf{X} \times \mathbf{A}^{1}, \mathbf{U}_{i}) = Hom(\mathbf{X}, \mathbf{U}_{i})$  and the same holds for  $U_{01}$  we conclude that  $Sing_{*}(\mathbf{F})$  is weakly equivalent to the sheaf  $A^{1}$  and therefore is not  $A^{1}$ -local.

Let $f: S_1 \to S_2$ be a morphism of base schemes. For any smooth scheme U over $S_2$ we have $f^*(U \times A^1) = f^*(U) \times A^1$. Therefore the functor $Lf^*$ preserves $A^1$-weak equivalences and induces a functor on $A^1$-homotopy categories which we again denote $Lf^*$. We also know that the functor $Rf_*$ preserves $A^1$-local objects and we denote the induced functor on $A^1$-homotopy categories by $R^{A^1}f_*$. Proposition 3.17 gives us the following result.

Proposition 2.8. — For any morphism $f: S_{1} \to S_{2}$ the functor $\mathbf{R}^{\mathbf{A}^{1}} f_{*}$ is right adjoint to $\mathbf{L} f^{*}$. For any composable pair $f, g$ of morphisms of base schemes there is a canonical isomorphism of functors between $\mathbf{A}^{1}$-homotopy categories of the form

$$
\mathbf {R} ^ {\mathbf {A} ^ {1}} (g \circ f) _ {*} \cong \mathbf {R} ^ {\mathbf {A} ^ {1}} g _ {*} \circ \mathbf {R} ^ {\mathbf {A} ^ {1}} f _ {*}.
$$

Proposition 2.9. — Let $f: S_{1} \to S_{2}$ be a smooth morphism of schemes. Then the functor $\mathbf{L}f_{\#}$ preserves $\mathbf{A}^{1}$-weak equivalences and the corresponding functor between $\mathbf{A}^{1}$-homotopy categories is left adjoint to the functor $\mathbf{L}_{\mathbf{A}}f^{*} \cong f^{*}$. In addition in this case the functor $f^{*}$ preserves $\mathbf{A}^{1}$-local objects.

Proof. — The projection formula for  $f_{\#}$  (1.23(2)) implies that for any simplicial sheaf X on  $S_{1}$  one has  $f_{\#}(\mathcal{X} \times \mathbf{A}^{1}) = f_{\#}(\mathcal{X}) \times \mathbf{A}^{1}$ . Since  $\phi(f)$  is a reasonable continuous map of sites (cf 3.16) Proposition 3.17 (cf also 1.23 and 3.15) implies our result.

Example 2.10. — It is not true in general that the functor $\mathbf{L}f^{*}$ takes $\mathbf{A}^{1}$-local objects to $\mathbf{A}^{1}$-local objects. Consider for example the canonical morphism $p: \text{Spec}(k[\varepsilon]/(\varepsilon^{2}=0)) \to \text{Spec}(k)$. The sheaf $\mathbf{G}_{m}$ represented by $\mathbf{A}^{1}-\{0\}$ on $Sm/k$ is $\mathbf{A}^{1}$-local. On the other hand $\mathbf{L}p^{*}(\mathbf{G}_{m}) \cong p^{*}(\mathbf{G}_{m})$ is the sheaf represented by $\mathbf{A}^{1}-\{0\}$ on $Sm/\text{Spec}(k[\varepsilon]/(\varepsilon^{2}=0))$ which is not $\mathbf{A}^{1}$-local since $\mathcal{O}^{*}(\text{Spec}(k[\varepsilon]/(\varepsilon^{2}=0))) \neq \mathcal{O}^{*}(\text{Spec}(k[\varepsilon]/(\varepsilon^{2}=0)) \times \mathbf{A}^{1})$.

The following example shows that the functors  $R^{A^{1}}f_{*}$  and  $Rf_{*}$  can be different even for smooth morphisms f, i.e. the functor  $Rf_{*}$  does not preserve in general  $A^{1}$ -weak equivalences.

Example 2.11. — Let $p: S_1 \to S_2$ be a smooth morphism. Observe that for a simplicially fibrant sheaf $\mathcal{X}$ the sheaf $\mathbf{R}p_*p^*(\mathcal{X})$ is given by $\underline{\text{Hom}}(S_1, \mathcal{X})$. Thus to show that the functor $\mathbf{R}p_*$ does not preserve $\mathbf{A}^1$-weak equivalences it is sufficient to

construct an $\mathbf{A}^1$-weak equivalence of fibrant simplicial sheaves $\mathcal{X}_1 \to \mathcal{X}_2$ such that $Hom(S_1, \mathcal{X}_1) \to Hom(S_1, \mathcal{X}_2)$ is not an $\mathbf{A}^1$-weak equivalence. Set $S_2 = Spec(k)$, $S_1 = \mathbf{P}^1$, $\overline{\mathcal{X}_2} = \mathbf{P}_1$. Let $i: \overline{\mathbf{P}^1 - \{0, \infty\}} \to \mathbf{A}^2$ be a closed embedding and

$$
j _ {0}: \mathbf {P} ^ {1} - \{0, \infty \} \rightarrow \mathbf {P} ^ {1} - \{0 \}
$$

$$
j _ {\infty}: \mathbf {P} ^ {1} - \{0, \infty \} \rightarrow \mathbf {P} ^ {1} - \{\infty \}
$$

be the obvious open embeddings. Set

$$
\mathscr {K} _ {1} = \left(\left(\mathbf {P} ^ {1} - \{0 \}\right) \times \mathbf {A} ^ {2}\right) \cup_ {j _ {0} \times i, j _ {\infty} \times i} \left(\left(\mathbf {P} ^ {1} - \{\infty \}\right) \times \mathbf {A} ^ {2}\right).
$$

The obvious map $\mathcal{X}_1\to \mathbf{P}^1$ is an $\mathbf{A}^1$-weak equivalence but the map

$$
\underline {{H o m}} (\mathbf {P} ^ {1}, \mathcal {X} _ {1}) \rightarrow \underline {{H o m}} (\mathbf {P} ^ {1}, \mathcal {X} _ {2})
$$

is not since $\mathcal{K}_1$ is affine and thus $\underline{\text{Hom}}(\mathbf{P}^1, \mathcal{K}_1) = \mathcal{K}_1$.

Proposition 2.12. — Let $f: \mathrm{S}_{1} \to \mathrm{S}_{2}$ be a finite morphism. Then for any simplicial sheaf $\mathcal{K}$ on $\mathrm{S}_{1}$ the canonical morphism $\mathbf{R}f_{*}(\mathcal{K}) \to \mathbf{R}^{\mathbf{A}^{1}}f_{*}(\mathcal{K})$ is an $\mathbf{A}^{1}$-weak equivalence.

Proof. — It is sufficient to show that  $\mathbf{R}f_{*}(\mathcal{X}) \to \mathbf{R}f_{*}(Ex_{\mathbf{A}^{1}}(\mathcal{X}))$  is an  $A^{1}$ -weak equivalence. By 1.27 we may replace  $Rf_{*}$  by  $f_{*}$  and the right hand side is simplicially weakly equivalent to  $\text{colim}_{n}f_{*}((Ex \circ Sing_{*})^{n})$ . Using again 1.27 we see that it is sufficient to show that for any X the map  $f_{*}(\mathcal{X}) \to f_{*}(Sing_{*}(\mathcal{X}))$  is an  $A^{1}$ -weak equivalence. By 2.14 we reduce the problem to showing that  $f_{*}(\mathcal{X}) \to f_{*}(\overline{\text{Hom}}(\mathbf{A}^{n}, \mathcal{X}))$  is an  $A^{1}$ -weak equivalence which follows from the fact that this morphism is a strict  $A^{1}$ -homotopy equivalence 3.7.

Consider the category $\Delta^{op}Shv_{Nis}(Sm/S)$. of pointed simplicial sheaves in the Nisnevich topology on $Sm/S$. Recall from 2 that a morphism of pointed sheaves is said to be a fibration, cofibration or weak equivalence (simplicial or $\mathbf{A}^1$-) if it belongs to the corresponding class as a morphism of sheaves without base points. Clearly, this definition provides us with model category structures which we will call respectively the simplicial and $\mathbf{A}^1$-model structures on $\Delta^{op}Shv_{Nis}(Sm/S)$. (see 2 for the simplicial structure). We denote the corresponding homotopy categories by $\mathcal{H}_{\bullet}^{s}((Sm/S)_{Nis})$ and $\mathcal{H}_{\bullet}(S)$ respectively.

Recall that the left adjoint to the forgetful functor $\Delta^{op}Shv_{\mathcal{Nis}}(Sm/S)_{\bullet}\to\Delta^{op}Shv_{\mathcal{Nis}}(Sm/S)$ is the functor $\mathcal{K}\mapsto\mathcal{K}_{+}$ where $\mathcal{K}_{+}$ is the simplicial sheaf $\mathcal{K}\amalg S$ pointed by the canonical embedding $S\to\mathcal{K}\amalg S$. Both functors preserve weak equivalences (as well as weak $\mathbf{A}^{1}$-equivalences) and thus induce a pair of adjoint functors between $\mathcal{H}_{\bullet}^{s}((Sm/S)_{\mathcal{Nis}})$ and $\mathcal{H}_{s}((Sm/S)_{\mathcal{Nis}})$ (as well as between $\mathcal{H}_{\bullet}(S)$ and $\mathcal{H}(S)$).

For pointed simplicial sheaves  $(\mathcal{X}, x)$ ,  $(\mathcal{Y}, y)$ , recall from Section 2 that  $(\mathcal{X}, x) \vee (\mathcal{Y}, y)$  denotes their wedge and  $(\mathcal{X}, x) \wedge (\mathcal{Y}, y)$  their smash-product.

The following lemma is an obvious corollary of the basic properties of  $A^{1}$ -weak equivalences.

Lemma 2.13. — Let $f: (\mathcal{X}, x) \to (\mathcal{Y}, y)$ be a simplicial (resp. $\mathbf{A}^{1-}$) weak equivalence. Then for any $(\mathcal{Z}, z)$ the morphism $f \wedge Id_{(\mathcal{Z}, z)}$ is a simplicial (resp. $\mathbf{A}^{1-}$) weak equivalence.

Lemma 2.13 implies in particular that the smash product defines a structure of a symmetric monoidal category on $\mathcal{H}_{\bullet}(\mathrm{S})$.

For any pointed simplicial sheaf $(\mathcal{X}, x)$ and any $i \geqslant 0$ we get three types of presheaves of homotopy groups (or sets):

\- the naive homotopy groups (or sets) $\underline{\pi}_i^{naive}(\mathcal{X}, x)(U) = \pi_i(\mathcal{X}(U), x)$

\- the simplicial homotopy group $\underline{\pi}_i(\mathcal{X}, x)(\mathrm{U}) = \pi_i(Ex(\mathcal{X})(\mathrm{U}), x)$

\- the $\mathbf{A}^1$-homotopy group $\underline{\pi}_i^{\mathbf{A}^1}(\mathcal{X}, x)(\mathrm{U}) = \pi_i^s(Ex_{\mathbf{A}^1}(\mathcal{X})(\mathrm{U}), x)$

(all of which being independent up to isomorphism of presheaves of the choice of Ex (see section 1)). We shall denote  $a\underline{\pi}_{i}(\mathcal{X}, x)$  the sheaf associated to the presheaf  $\underline{\pi}_{i}(\mathcal{X}, x)$  and  $a\underline{\pi}_{i}^{\mathbf{A}^{1}}(\mathcal{X}, x)$  the sheaf associated to the presheaf  $\underline{\pi}_{i}^{\mathbf{A}^{1}}(\mathcal{X}, x)$ . Note that  $a\underline{\pi}_{i}(\mathcal{X}, x)$  is isomorphic to the sheaf associated to the presheaf  $\underline{\pi}_{i}^{\text{naive}}(\mathcal{X}, x)$  of “naive” homotopy groups. We say that X is  $A^{1}$ -connected if  $a\underline{\pi}_{0}^{\mathbf{A}^{1}}(\mathcal{X})$  is the constant sheaf pt. The following obvious result is a version of the Whitehead theorem in our setting.

Proposition 2.14. — Let $f: (\mathcal{X}, x) \to (\mathcal{Y}, y)$ be a morphism of $\mathbf{A}^{1}$-connected pointed simplicial sheaves. Then the following conditions are equivalent:

1. $f$ is an $\mathbf{A}^1$-weak equivalence;

2. for any $i \geqslant 0$ the morphism of the presheaves of $\mathbf{A}^1$-homotopy groups $\underline{\pi}_i^{\mathbf{A}^1}(\mathcal{X}, x) \to \underline{\pi}_i^{\mathbf{A}^1}(\mathcal{Y}, y)$ is an isomorphism;

3. for any $i > 0$ the morphism of the sheaves of $\mathbf{A}^1$-homotopy groups $\alpha \underline{\pi}_i^{\mathbf{A}^1}(\mathcal{K}, x) \to \alpha \underline{\pi}_i^{\mathbf{A}^1}(\mathcal{Y}, y)$ is an isomorphism.

## Spheres, suspensions and Thom spaces

Consider the following objects in  $\Delta^{op}Shv_{\mathcal{Nis}}(Sm/S)_{\bullet}$ :

$S_{s}^{1}$  the constant simplicial sheaf corresponding to the simplicial circle  $\Delta^{1}/\partial\Delta^{1}$  pointed in the obvious way;

$\mathbf{S}_t^1$ the sheaf represented by $\mathbf{A}^1 -\{0\}$ pointed by 1;

T the quotient sheaf $\mathbf{A}^1 / (\mathbf{A}^1 - \{0\})$ pointed by the image of $\mathbf{A}^1 - \{0\}$.

The first two of them play the role of two circles in the homotopy theory of schemes over S. We will use the following notations:

$$
\begin{array}{r l} & {\mathbf {S} _ {s} ^ {n} = (\mathbf {S} _ {s} ^ {1}) ^ {\wedge n}} \\ & {\mathbf {S} _ {t} ^ {n} = (\mathbf {S} _ {t} ^ {1}) ^ {\wedge n}} \\ & {\mathbf {T} ^ {n} = \mathbf {T} ^ {\wedge n}} \\ & {\mathbf {S} ^ {p, q} = \mathbf {S} _ {s} ^ {p - q} \wedge \mathbf {S} _ {t} ^ {q}.} \end{array}
$$

Observe that the last one makes sense only for $p \geqslant q \geqslant 0$.

Lemma 2.15. — There is a canonical isomorphism in $\mathcal{H}_{\bullet}(\mathrm{S})$ of the form

$$
\mathbf {S} _ {t} ^ {1} \wedge \mathbf {S} _ {s} ^ {1} \cong \mathbf {T}.
$$

Proof. — Consider an object X given by the cocartesian square

$$
\begin{array}{c c c} \mathrm{S} _ {t} ^ {1} & \longrightarrow & (\mathbf {A} ^ {1}, \{1 \}) \\ \Big \downarrow & & \Big \downarrow \\ \Delta_ {s} ^ {1} \wedge \mathrm{S} _ {t} ^ {1} & \longrightarrow & \mathcal {X}. \end{array}
$$

Projecting  $\Delta_{s}^{1}\wedge S_{t}^{1}$  to the point we get a pointed morphism  $X\to T$ . Projecting  $(\mathbf{A}^{1};\{1\})$  to the point we get a morphism  $X\to S_{s}^{1}\wedge S_{t}^{1}$ . By Lemma 2.11 we conclude that both morphisms are  $A^{1}$ -weak equivalences (in fact the first one is a simplicial weak equivalence).

We define three suspension functors on  $\Delta^{op}Shv_{Nis}(Sm/S)$ . setting:

$$
\begin{array}{r l} & {\boldsymbol {\Sigma} _ {s} (\mathcal {K}, x) = \mathrm{S} _ {s} ^ {1} \wedge (\mathcal {K}, x)} \\ & {\boldsymbol {\Sigma} _ {t} (\mathcal {K}, x) = \mathrm{S} _ {t} ^ {1} \wedge (\mathcal {K}, x)} \\ & {\boldsymbol {\Sigma} _ {\mathrm{T}} (\mathcal {K}, x) = \mathrm{T} \wedge (\mathcal {K}, x).} \end{array}
$$

We will also use the obvious notations $\Sigma_s^n$, $\Sigma_t^n$, $\Sigma_\mathrm{T}^n$ and $\Sigma^{p,q}$. By Lemma 2.13 these suspension functors define functors on $\mathcal{H}_{\bullet}(S)$ and by Lemma 2.15 on the level of $\mathbf{A}^1$-homotopy categories we have a canonical isomorphism of functor $\Sigma_{\mathrm{T}} \cong \Sigma_s \circ \Sigma_t$.

Definition 2.16. — Let X be a smooth scheme over S and E be a vector bundle over X. The Thom space of E is the pointed sheaf

$$
T h (\mathcal {E}) = T h (\mathcal {E} / \mathrm{X}) = \mathcal {E} / (\mathcal {E} - i (\mathrm{X}))
$$

where $i:\mathbf{X}\to \mathcal{E}$ is the zero section of $\mathcal{E}$.

For any vector bundle E over X denote by  $\mathbf{P}(\mathcal{E}) \to \mathbf{X}$  the corresponding projective bundle over X.

## Proposition 2.17.

1. Let $\mathcal{E}_1, \mathcal{E}_2$ be vector bundles on smooth S-schemes $\mathbf{X}_1$ and $\mathbf{X}_2$ respectively. Then there is a canonical isomorphism of pointed sheaves $Th(\mathcal{E}_1 \times \mathcal{E}_2 / \mathbf{X}_1 \times \mathbf{X}_2) = Th(\mathcal{E}_1 / \mathbf{X}_1) \wedge Th(\mathcal{E}_2 / \mathbf{X}_2)$.

2. Let  $O_{X}^{n}$  be the trivial vector bundle of dimension n on X. Then there is a canonical isomorphism of pointed sheaves  $Th(\mathcal{O}_{\mathrm{X}}^{n}) = \Sigma_{\mathrm{T}}^{n}\mathrm{X}_{+}$ .

3. Let E be a vector bundle over X and  $\mathbf{P}(\mathcal{E}) \to \mathbf{P}(\mathcal{E} \oplus \mathcal{O})$  be the (closed) embedding at infinity. Then the canonical morphism of pointed sheaves:  $\mathbf{P}(\mathcal{E} \oplus \mathcal{O}) / \mathbf{P}(\mathcal{E}) \to Th(\mathcal{E})$  is an  $A^{1}$ -weak equivalence.

Proof. — The only statement which may require a detailed proof is the last one. Consider the open covering of  $\mathbf{P}(\mathcal{E} \oplus \mathcal{O})$  of the form

$$
\mathbf {P} (\mathcal {E} \oplus \mathcal {O}) = \mathcal {E} \cup (\mathbf {P} (\mathcal {E} \oplus \mathcal {O}) - \mathbf {X})
$$

where the closed embedding of X into  $\mathbf{P}(\mathcal{E} \oplus \mathcal{O})$  is the composition of the embedding of E with the zero section.

It gives a cocartesian square of sheaves in the usual way such that in particular we get an isomorphism of pointed sheaves of the form

$$
T h (\mathcal {E}) = \mathbf {P} (\mathcal {E} \oplus \mathcal {O}) / (\mathbf {P} (\mathcal {E} \oplus \mathcal {O}) - \mathbf {X}).
$$

As the embedding “at infinity” factors through  $\mathbf{P}(\mathcal{E} \oplus \mathcal{O}) - \mathbf{X}$ , we thus get the required morphism:

$$
\mathbf {P} (\mathcal {E} \oplus \mathcal {O}) / \mathbf {P} (\mathcal {E}) \rightarrow T h (\mathcal {E}).
$$

In view of Lemma 2.11 it is sufficient to show that the embedding $\mathbf{P}(\mathcal{E}) \to \mathbf{P}(\mathcal{E} \oplus \mathcal{O}) - \mathbf{X}$ is an $\mathbf{A}^1$-weak equivalence. But from [14, §8] we know that this embedding is isomorphic to the zero section embedding of $\mathbf{P}(\mathcal{E})$ into the total space of the canonical vector bundle of rank one over $\mathbf{P}(\mathcal{E})$. The proposition then follows from 2.2.

Corollary 2.18. — The canonical morphism of pointed sheaves  $P^{n}/P^{n-1} \cong T^{n}$  is an  $A^{1}$ -weak equivalence. In particular one has  $(\mathbf{P}^{1}, *) \cong T$ .

Remark 2.19. — In the above corollary the projective line was pointed by  $\infty$ . Of course one may use one of the three canonical base points  $\infty$ , 0, 1 of the projective line because the corresponding pointed projective lines are isomorphic.

Example 2.20. — Another example of a sphere in our theory is, for each  $n \geqslant 1$ ,  $A^{n} - \{0, \ldots, 0\}$ . One can show easily that there is a canonical isomorphism (in  $\mathcal{H}_{\bullet}^{s}(S)$ ) of the form

$$
\mathbf {A} ^ {n} - \{0, \dots , 0 \} \cong (\mathrm{S} _ {s} ^ {1}) ^ {n - 1} \wedge (\mathrm{S} _ {t} ^ {1}) ^ {n} = \mathrm{S} ^ {2 n - 1, n}.
$$

## Gluing, homotopy purity and the blow-up square

All the results proven so far about  $\mathcal{H}(S)$  would also hold (with some obvious changes) if we were to consider Zariski topology instead of the Nisnevich one. The results of this section require the topology to be at least as strong as the Nisnevich one. The first of them (Theorem 2.21) also uses in an essential way the fact that we are working with the category of smooth schemes over S.

Recall that S is a Noetherian scheme of finite dimension. Let  $i: Z \to S$  be a closed embedding and  $j: U \to S$  be the complimentary open embedding. For any simplicial sheaf X we have a canonical commutative square in the simplicial homotopy category of the form

$$
\begin{array}{c c c} (\mathbf {L} j _ {\#}) j ^ {*} \mathcal {X} & \longrightarrow & \mathcal {X} \\ \Big \downarrow & & \Big \downarrow \\ \mathrm{U} & \longrightarrow & i _ {*} \mathrm{Li} ^ {*} (\mathcal {X}). \end{array}
$$

This square is the simplicial analog of the sequence

$$
0 \rightarrow j _ {!} j ^ {*} \mathrm{F} \rightarrow \mathrm{F} \rightarrow i _ {*} i ^ {*} \mathrm{F} \rightarrow 0
$$

the exactness of which for sheaves of abelian groups on small sites plays major role in the gluing theory for such sheaves. Analogous to this exactness property would be the property of our square to be (homotopy) cocartesian – however, one can easily see that this square is not homotopy cocartesian in  $\mathcal{H}_{s}((Sm/S)_{\tilde{Nis}})$ . The problem has nothing to do with the fact that we are working with simplicial sheaves and not with sheaves of abelian groups but comes instead from the fact that we are working with big sites and not with the small ones. If we were to consider simplicial sheaves on the small Nisnevich site  $S_{Nis}$  it would disappear, i.e. the corresponding square would be (homotopy) cocartesian. The following Gluing Theorem shows that this problem disappears once we pass to the  $A^{1}$ -homotopy category. Observe that this theorem is very sensitive to the choices which one makes to define  $\mathcal{H}(S)$ . It would become false if we were to take Zariski topology instead of the Nisnevich or if we were to consider the category of all schemes of finite type over S instead of the category of smooth ones.

Theorem 2.21. — For any simplicial sheaf $\mathcal{K}$ the square

![](images/page_70_image_1.jpg)

is homotopy cocartesian in $\mathcal{H}(\mathbf{S})$.

Proof. — It is clearly sufficient (using resolution lemmas) to show that for a smooth scheme X over S the canonical morphism of sheaves  $X \cup_{X \times_{S} U} U \to i_{*}(X \times_{S} Z)$  is an  $A^{1}$ -weak equivalence. By Lemma 2.16 it is sufficient to verify that for a smooth scheme Y over S and a section  $Y \to i_{*}(X \times_{S} Z)$  the projection  $(X \cup_{X \times_{S} U} U) \times_{i_{*}(X \times_{S} Z)} Y \to Y$  is an  $A^{1}$ -weak equivalence.

A section of $i_{*}(\mathbf{X} \times_{\mathrm{S}} \mathbf{Z})$ over $\mathbf{Y}$ is by definition a morphism $\phi: \mathbf{Y} \times_{\mathrm{S}} \mathbf{Z} \to \mathbf{X}$ over $\mathrm{S}$. Consider the sheaf $\Phi_{(\mathbf{X} \times_{\mathrm{S}} \mathbf{Y}, \phi)}$ on $(Sm / \mathbf{Y})_{\mathcal{Nis}}$ such that $\Phi_{(\mathbf{X} \times_{\mathrm{S}} \mathbf{Y}, \phi)}(\mathbf{W} / \mathbf{Y})$ is the subset of the set of morphism $\mathbf{W} \to (\mathbf{X} \times_{\mathrm{S}} \mathbf{Y})$ over $\mathbf{Y}$ whose restriction to $\mathbf{W} \times_{\mathrm{Y}} (\mathbf{Z} \times_{\mathrm{S}} \mathbf{Y})$ coincides with $\mathbf{W} \times_{\mathrm{S}} \mathbf{Z} \to \mathbf{Y} \times_{\mathrm{S}} \mathbf{Z} \xrightarrow{\phi} \mathbf{X}$. If $p_{\mathrm{Y}}: \mathbf{Y} \to \mathbf{X}$ is the canonical morphism then $(p_{\mathrm{Y}})_{\#}(\Phi_{(\mathbf{X} \times_{\mathrm{S}} \mathbf{Y}, \phi)})$ is isomorphic to the fiber product $\mathbf{X} \times_{i_{*}(\mathbf{X} \times_{\mathrm{S}} \mathbf{Z})}\mathbf{Y}$ and the morphism $(\mathbf{X} \cup_{\mathrm{X} \times_{\mathrm{S}}\mathrm{U}} \mathbf{U}) \times_{i_{*}(\mathbf{X} \times_{\mathrm{S}}\mathrm{Z})}\mathbf{Y} \to \mathbf{Y}$ is isomorphic to the $(p_{\mathrm{Y}})_{\#}$ of the canonical morphism

$$
\Phi_ {(\mathrm{X} \times_ {\mathrm{S}} \mathrm{Y}, \phi)} \cup_ {\mathrm{X} \times_ {\mathrm{S}} \mathrm{U} \times_ {\mathrm{S}} \mathrm{Y}} (\mathrm{U} \times_ {\mathrm{S}} \mathrm{Y}) \rightarrow \mathrm{Y}
$$

in  $(Sm/Y)_{Nis}$ . By Proposition 1.26 the functor  $Lj_{\#}$  coincides with  $j_{\#}$  and in particular  $j_{\#}$  preserves  $A^{1}$ -weak equivalences. Thus it remains to show that the morphism  $\Phi_{(\mathrm{X}\times_{\mathrm{S}}\mathrm{Y},\phi)}\cup_{\mathrm{X}\times_{\mathrm{S}}\mathrm{U}\times_{\mathrm{S}}\mathrm{Y}}(\mathrm{U}\times_{\mathrm{S}}\mathrm{Y})\to\mathrm{Y}$  is an  $A^{1}$ -weak equivalence over Y.

For simplicity of notations we may assume now that Y=S. Denote the sheaf  $\Phi_{(X,\phi)}\cup_{X_{U}}U$  by  $\Psi_{(X,\phi)}$ . We want to show that the canonical morphism  $\Psi_{(X,\phi)}\to S$  is an  $A^{1}$ -weak equivalence for any smooth X over S. The following lemma follows immediately from the fact that we are using Nisnevich topology and therefore it is sufficient to compare the sets of sections of our sheaves over henselian local schemes.

Lemma 2.22. — Let $p: \mathbf{X} \to \mathbf{X}'$ be an étale morphism such that the map $p^{-1}(p(\phi(\mathbf{Z}))) \to \phi(\mathbf{Z})$ is a bijection. Then the morphism of sheaves $\Psi_{(\mathbf{X},\phi)} \to \Psi_{(\mathbf{X}',\phi \circ p)}$ on $(Sm/S)_{Nis}$ is an isomorphism.

We can clearly assume now that S is henselian. Then,  $\phi$  can be extended to a point  $x: S \to X$  of X and since  $(X, x: S \to X)$  is a smooth pair there exists an étale morphism  $p: X \to A_{S}^{n}$  such that  $p^{-1}(\{0\}_{Z}) = \phi(Z)$ . By Lemma 2.22 we conclude that  $\Psi_{(X,\phi)}$  is isomorphic to  $\Psi_{(A^{n},0)} = \Psi_{(A^{1},0)}^{n}$ . It remains to observe that  $\Psi_{(A^{1},0)}^{n} \cong \Phi_{(A^{1},0)}$  in  $\mathcal{H}(S)$  and the latter sheaf is strictly  $A^{1}$ -homotopy equivalent to the point.

Theorem 2.23. — Let $i: \mathbf{Z} \to \mathbf{X}$ be a closed embedding of smooth schemes over S. Denote by $\mathbf{N}_{\mathbf{X},\mathbf{Z}} \to \mathbf{Z}$ the normal vector bundle to $i$. Then there is a canonical isomorphism in $\mathcal{H}_{\bullet}(\mathbf{S})$ of the form

$$
\mathbf {X} / (\mathbf {X} - i (\mathbf {Z})) \cong T h (\mathbf {N} _ {\mathrm{X}, \mathrm{Z}}).
$$

Proof. — Denote by  $p_{\mathrm{X},\mathrm{Z}}:\mathbf{B}(\mathrm{X},\mathrm{Z})\to\mathbf{X}\times\mathbf{A}^{1}$  the blow-up of  $i(\mathbf{Z})\times\{0\}$  in  $X\times A^{1}$ . We have a canonical closed embedding  $f_{\mathrm{X},\mathrm{Z}}:\mathbf{Z}\times\mathbf{A}^{1}\to\mathbf{B}(\mathrm{X},\mathrm{Z})$  which splits  $p_{\mathrm{X},\mathrm{Z}}$  over  $i(\mathbf{Z})\times\mathbf{A}^{1}$  and a canonical closed embedding  $g_{\mathrm{X},\mathrm{Z}}:\mathbf{X}\to\mathbf{B}(\mathbf{X},\mathbf{Z})$  which splits  $p_{\mathrm{X},\mathrm{Z}}$  over  $X\times\{1\}$ . There is a canonical isomorphism  $p^{-1}(i(\mathbf{Z})\times\{0\})\cong\mathbf{P}(\mathbf{N}\oplus\mathcal{O})$  which induces an isomorphism  $(p^{-1}(i(\mathbf{Z})\times\{0\})-f(\mathbf{Z}\times\{0\}))\cong\mathbf{P}(\mathbf{N}\oplus\mathcal{O})-\mathbf{P}(\mathcal{O})$  and thus an isomorphism of pointed sheaves

$$
T h (\mathbf {N}) \cong p ^ {- 1} (i (\mathbf {Z}) \times \{0 \}) / (p ^ {- 1} (i (\mathbf {Z}) \times \{0 \}) - f (\mathbf {Z} \times \{0 \}))
$$

(we omitted the index  $(X, Z)$  for simplicity of the notations). Since we have

$$
\begin{array}{l} g (\mathbf {X}) \cap f (\mathbf {Z} \times \mathbf {A} ^ {1}) = g (i (\mathbf {Z})) \\ p ^ {- 1} (i (\mathbf {Z}) \times \{0 \}) \cap f (\mathbf {Z} \times \mathbf {A} ^ {1}) = f (\mathbf {Z} \times \{0 \}) \end{array}
$$

we get two monomorphisms:

$$
\begin{array}{r l} & {\widetilde {g} _ {\mathrm{X}, \mathrm{Z}}: \mathrm{X} / (\mathrm{X} - \mathrm{Z}) \to \mathrm{B} (\mathrm{X}, \mathrm{Z}) / (\mathrm{B} (\mathrm{X}, \mathrm{Z}) - f (\mathrm{Z} \times \mathbf {A} ^ {1}))} \\ & {\alpha_ {\mathrm{X}, \mathrm{Z}}: T h (\mathrm{N} _ {\mathrm{X}, \mathrm{Z}}) \to \mathrm{B} (\mathrm{X}, \mathrm{Z}) / (\mathrm{B} (\mathrm{X}, \mathrm{Z}) - f (\mathrm{Z} \times \mathbf {A} ^ {1})).} \end{array}
$$

Theorem 2.23 is then a consequence of the following:

Proposition 2.24. — Let $i: \mathbf{Z} \to \mathbf{X}$ be a closed embedding of smooth schemes over S. Then the two morphisms $\widetilde{g}_{\mathbf{X},\mathbf{Z}}$ and $\alpha_{\mathbf{X},\mathbf{Z}}$ are $\mathbf{A}^{1}$-weak equivalences.

To prove this proposition, we proceed in several steps. Let's recall first some well known facts. Let X be a smooth S-scheme and  $X \to A_{X}^{n}$  the zero section. Then the blow-up of X in  $A_{X}^{n}$  is isomorphic to the total space  $\mathrm{E}(\lambda_{\mathrm{X}}^{n-1}) = (\mathbf{A}^{n} - \{0\})_{\mathrm{X}} \times_{\mathbf{G}_{m}} \mathbf{A}^{1}$  of the canonical line bundle  $\lambda_{X}^{n-1}$  over  $P_{X}^{n-1}$ ; indeed almost by construction, this blow-up, denoted Y, is isomorphic to the closed subscheme of  $A^{n} \times P^{n-1} \times X$  given by the equations  $x_{i}, y_{j} = x_{j}, y_{i}$  where  $x_{i}$  are the coordinate functions of  $A_{X}^{n}$  and  $y_{j}$  are the standard sections of the canonical vector bundle of rank one over  $P_{X}^{n-1}$ . Then the obvious morphism

$$
\mathbf {E} (\lambda_ {\mathbf {X}} ^ {n - 1}) \rightarrow \mathbf {A} ^ {n} \times \mathbf {P} ^ {n - 1} \times \mathbf {X}
$$

is seen to be an isomorphism. One easily deduces:

Lemma 2.25. — For any smooth S-scheme X and any  $n \geqslant 1$ , denote by  $p : E \to A_{X}^{n}$  the blow-up of X in  $A_{X}^{n}$  (where X is embedded via the zero section). Then the canonical morphism  $q : E \to P_{X}^{n-1}$  has the following properties:

1. let  $i: A_{X}^{1} \rightarrow E$  be the closed embedding which corresponds by the universal property of blow-ups to the embedding  $A_{X}^{1} \rightarrow A_{X}^{n}$  of the form  $t \mapsto (0, \ldots, 0, t)$ . Then the following square is cartesian

![](images/page_72_image_2.jpg)

(here the left vertical arrow is the canonical projection and the right one is $q$);

2. the restriction of $q$ to $p^{-1}(\mathbf{X})$ coincides with the canonical isomorphism $p^{-1}(\mathbf{X}) \to \mathbf{P}_{\mathrm{X}}^{n - 1}$.

In order to prove Proposition 2.24 let's first prove a particular case.

Lemma 2.26. — For any smooth S-scheme X and any  $n \geqslant 0$  the Proposition 2.24 holds for the closed embedding  $X \rightarrow A_{X}^{n}$  corresponding to the  $(0, ..., 0)$ -section.

Proof. — Consider the projection  $\mathbf{B}(\mathbf{A}_{\mathrm{X}}^{n},\mathbf{X})\to\mathbf{P}_{\mathrm{X}}^{n}$  given by the identification of  $\mathbf{B}(\mathbf{A}_{\mathrm{X}}^{n},\mathbf{X})$  with  $\mathbf{E}(\lambda_{\mathrm{X}}^{n})$  (see above). By the first point of Lemma 2.25 above, it maps  $\mathbf{B}(\mathbf{A}_{\mathrm{X}}^{n},\mathbf{X})-\{0,\ldots,0\}\times\mathbf{A}_{\mathrm{X}}^{1}$  to  $P_{X}^{n}-X$, and both of these maps are projections from a vector bundle and thus  $A^{1}$ -weak equivalences by Example 2.2. Therefore the morphism

$$
q ^ {\prime}: \mathbf {B} (\mathbf {A} _ {\mathrm{X}} ^ {n}, \mathbf {X}) / (\mathbf {B} (\mathbf {A} _ {\mathrm{X}} ^ {n}, \mathbf {X}) - \{0, \dots , 0 \} \times \mathbf {A} _ {\mathrm{X}} ^ {1}) \to \mathbf {P} _ {\mathrm{X}} ^ {n} / (\mathbf {P} _ {\mathrm{X}} ^ {n} - \mathbf {X})
$$

is an  $A^{1}$ -weak equivalence. It is then clear that  $q' \circ \alpha$  is the canonical isomorphism of sheaves so that  $\alpha$  is an  $A^{1}$ -weak equivalence.

On the other hand composing our projection with the immersion  $g: A_{X}^{n} \to B(A_{X}^{n}, X)$  we get the canonical (open) embedding  $A_{X}^{n} \to P_{X}^{n}$  which takes  $\{0, ..., 0\}$  to the class of  $\{0, ..., 0, 1\}$ . Thus by Lemma 1.6 the corresponding morphism

$$
\mathbf {A} _ {\mathrm{X}} ^ {n} / (\mathbf {A} _ {\mathrm{X}} ^ {n} - \{0, \dots , 0 \} _ {\mathrm{X}}) \rightarrow \mathbf {P} _ {\mathrm{X}} ^ {n} / (\mathbf {P} _ {\mathrm{X}} ^ {n} - \mathbf {X})
$$

is an isomorphism which proves that  $\widetilde{g}$  is also an  $A^{1}$ -weak equivalence (in fact we have proven that  $q'\circ\widetilde{g}$  and  $q'\circ\alpha$  are both isomorphisms).

Let $\phi : U \to X$ be an étale morphism. Denote $\phi^{-1}(Z)$ by $Z_{U}$. Since all our constructions commute with base changes along étale morphisms for any such $\phi$ we have a commutative diagram

$$
\begin{array}{c c c c c} \mathrm {U / (U- U_ {Z})} & \stackrel {{\widetilde {g} _ {\mathrm{U}, Z _ {\mathrm{U}}}}} {{\longrightarrow}} & \mathrm {B(U, Z_ {U}) / (B(U, Z_ {U}) - f(Z_ {U} \times A^ {1}))} & \stackrel {{\alpha_ {\mathrm{U}, Z _ {\mathrm{U}}}}} {{\longleftarrow}} & T h (\mathrm {N_ {U, Z_ {U}}}) \\ \Big \downarrow & & \Big \downarrow & & \Big \downarrow \\ \mathrm {X / (X- Z)} & \stackrel {{\widetilde {g} _ {\mathrm{X}, Z}}} {{\longrightarrow}} & \mathrm {B(X, Z) / (B(X, Z) - f(Z\times A^ {1}))} & \stackrel {{\alpha_ {\mathrm{X}, Z}}} {{\longleftarrow}} & T h (\mathrm {N_ {X, Z}}) \end{array}
$$

and one can verify immediately that the following statement holds.

Lemma 2.27. — Let $\phi: \mathbf{U} \to \mathbf{X}$ be an étale morphism such that the morphism $Z_{\mathbf{U}} \to Z$ is an isomorphism. Then the vertical arrows in the diagram presented above are isomorphisms. In particular proposition 2.24 holds for $Z \to X$ if and only if it holds for $Z_{\mathbf{U}} \to U$.

Lemma 2.28. — Let $i: \mathbf{Z} \to \mathbf{X}$ be a closed embedding such that there exists an étale morphism $q: \mathbf{X} \to \mathbf{A}^n$ such that $i(\mathbf{Z}) = q^{-1}(\mathbf{A}^{n-c} \times \{0, ..., 0\})$ for some $c$. Then Proposition 2.24 holds for $i$.

Proof. — Consider the fiber product  $\mathbf{X} \times_{\mathbf{A}^{n}} (\mathbf{Z} \times \mathbf{A}^{c})$  where the morphism  $Z \times A^{c} \to A^{n}$  is  $(q \circ i) \times Id$ . The fiber of the projection  $\mathbf{X} \times_{\mathbf{A}^{n}} (\mathbf{Z} \times \mathbf{A}^{c}) \to \mathbf{A}^{n}$  over  $A^{n-c} \times \{0, ..., 0\}$  is the closed subscheme  $Z \times_{A^{n-c}} Z$  of  $\mathbf{X} \times_{\mathbf{A}^{n}} (\mathbf{Z} \times \mathbf{A}^{c})$ . Since the morphism  $Z \to A^{n-c}$  is étale, this fiber is disjoint union of the image of the diagonal embedding  $\Delta : Z \to Z \times_{A^{n-c}} Z$  and a closed subscheme Y (which is thus also closed in  $\mathbf{X} \times_{\mathbf{A}^{n}} (\mathbf{Z} \times \mathbf{A}^{c})$ ). Set  $U = X \times_{\mathbf{A}^{n}} (Z \times \mathbf{A}^{c}) - Y$ . We have two étale projections

$$
\begin{array}{l} p r _ {1}: \mathbf {U} \to \mathbf {X} \\ p r _ {2}: \mathbf {U} \to \mathbf {Z} \times \mathbf {A} ^ {c} \end{array}
$$

such that  $pr_{1}^{-1}(i(Z)) \to i(Z)$  and  $pr_{2}^{-1}(Z \times \{0\}) \to Z \times \{0\}$  are isomorphisms. The statement of the lemma follows now from Lemmas 2.27, 2.26.

To prove the general case we proceed as follows. Fisrt of all since  $Z \to X$  is a closed embedding of smooth schemes there exists a finite Zariski open covering  $X = \cup U_i$  such that for any i the embedding  $Z \cap U_i \to U_i$  satisfies the condition of Lemma 2.28. Note also that if this condition holds for  $Z \to X$  it also holds for  $Z \cap U \to U$  where U is any open subset of X. In particular, it holds for all intersections of the form  $U_{i_1} \cap \ldots \cap U_{i_k}$ . Consider the simplicial sheaf K with terms of the form  $(\coprod U_i)^{n+1}_X$ . It maps to X and by Lemma 1.15 this map is a simplicial weak equivalence. We also have a simplicial sheaf Z with terms  $(\coprod (U_i \cap Z))^{n+1}$  and we can form a simplicial sheaf B applying the construction of  $\mathrm{B}(X, Z)$  termwise to the closed embedding  $Z \to U$ . It gives us a commutative diagram

$$
\begin{array}{c c c c c}\mathcal {K} / (\mathcal {K} - \mathcal {Z})&\xrightarrow [ \rightarrow ]{\widetilde {g} _ {\mathcal {K} , \mathcal {Z}}}&\mathcal {B} / (\mathcal {B} - f (\mathcal {Z} \times \mathbf {A} ^ {1}))&\stackrel {{\alpha_ {\mathcal {K}, \mathcal {Z}}}} {{\longleftarrow}}&T h (\mathrm{N} _ {\mathcal {X}, \mathcal {Z}})\\\Big \downarrow&&\Big \downarrow&&\Big \downarrow\\\mathrm{X} / (\mathrm{X} - \mathrm{Z})&\xrightarrow [ ]{\widetilde {g} _ {\mathrm{X,Z}}}&\mathrm{B} (\mathrm{X,Z}) / (\mathrm{B} (\mathrm{X,Z}) - f (\mathrm{Z} \times \mathbf {A} ^ {1}))&\stackrel {{\alpha_ {\mathrm{X,Z}}}} {{\longleftarrow}}&T h (\mathrm{N} _ {\mathrm{X,Z}})\end{array}
$$

where the vertical arrows are simplicial weak equivalences by Lemma 2.11 and the upper horizontal ones are  $A^{1}$ -weak equivalences by Lemma 2.28 and Proposition 2.14. Therefore the lower horizontal arrows are  $A^{1}$ -weak equivalences, which finishes the proof of Proposition 2.24.

Proposition 2.29. — Let $i: \mathbf{Z} \to \mathbf{X}$ be a closed embedding of smooth schemes over $\mathbf{S}$, $p: \mathbf{X}_{\mathbf{Z}} \to \mathbf{X}$ be the blow-up of $i(\mathbf{Z})$ in $\mathbf{X}$ and $\mathbf{U} = \mathbf{X} - i(\mathbf{Z}) = \mathbf{X}_{\mathbf{Z}} - p^{-1}(i(\mathbf{Z}))$. Then the square

$$
\begin{array}{c c c} p ^ {- 1} (\mathrm{Z}) & \longrightarrow & \mathrm {X_ {Z} /U} \\ \Big \downarrow & & \Big \downarrow \\ \mathrm{Z} & \longrightarrow & \mathrm{X/U} \end{array}
$$

is homotopy cocartesian, i.e. the morphism $(\mathbf{X}_{\mathbb{Z}} / \mathbf{U})\coprod_{p^{-1}(\mathbb{Z})}\mathbf{Z}\to \mathbf{X} / \mathbf{U}$ is an $\mathbf{A}^1$-weak equivalence.

Proof. — Applying the same technique as in the proof of Theorem 2.23 one reduces the problem to the case of the embedding  $S \rightarrow A_{S}^{n}$  corresponding to the point  $(0, \ldots, 0)$ . Then our result follows from Lemma 2.25.

Remark 2.30. — We do not know whether or not under the assumptions of Proposition 2.29 the square

$$
\begin{array}{c c c} p ^ {- 1} (\mathbf {Z}) & \longrightarrow & \mathbf {X} _ {\mathbf {Z}} \\ \Big \downarrow & & \Big \downarrow \\ \mathbf {Z} & \longrightarrow & \mathbf {X} \end{array}
$$

is homotopy cocartesian. However, Proposition 2.29 does imply that the following diagram of pointed simplicial sheaves is homotopy cocartesian

$$
\begin{array}{c c c} \Sigma_ {s} (\not p ^ {- 1} (Z) _ {+}) & \longrightarrow & \Sigma_ {s} ((X _ {Z}) _ {+}) \\ \Big \downarrow & & \Big \downarrow \\ \Sigma_ {s} (Z _ {+}) & \longrightarrow & \Sigma_ {s} (X _ {+}). \end{array}
$$

## 3.3. Some realization functors

## G-equivariant homotopy categories of spaces

Let G be a finite group and  $\Delta^{op}(G-Sets)$  be the category of simplicial G-sets. Define two types of weak equivalences in  $\Delta^{op}(G-Sets)$  as follows:

\- a coarse weak equivalence is a G-equivariant morphism which is a weak equivalence in $\Delta^{op}$ Sets;

\- a fine weak equivalence is a G-equivariant morphism $f \colon \mathbf{X} \to \mathbf{Y}$ such that for any subgroup H of G the morphism $\mathbf{X}^{\mathrm{H}} \to \mathbf{Y}^{\mathrm{H}}$ is a weak equivalence in $\Delta^{op}Sets$.

The localizations of  $\Delta^{op}(\mathbf{G}-Sets)$  with respect to these two types of weak equivalences are called the coarse and fine G-equivariant homotopy categories respectively and are denoted by  $\mathcal{H}_{c}(\mathbf{G})$  and  $\mathcal{H}_{f}(\mathbf{G})$ . Clearly for G=e the two types of weak equivalences coincide and the resulting homotopy categories are both equivalent to the usual homotopy category H.

We are going to show now how the categories  $\mathcal{H}_{c}(\mathbf{G})$  and  $\mathcal{H}_{f}(\mathbf{G})$  can be described as homotopy categories of appropriate sites with intervals.

Definition 3.1. — Let T be a topological G-space. We say that an open covering  $T = \cup U_i$  is good if all the open subsets  $U_i$  are G-invariant and for any i the map  $U_i \to \pi_0(U_i)$  is a G-homotopy equivalence. We say that a G-space T is good if any covering of T by G-invariant open subsets has a good refinement.

Denote the category of good G-spaces and G-equivariant continuous maps by G - Tlc. We define the coarse (c) and fine (f) topologies on G - Tlc as follows:

\- a coarse covering is a G-equivariant morphism $\mathbf{X} \to \mathbf{Y}$ such that for any point $y$ of $Y$ there exists an open neighborhood $U$ of $y$ in $Y$ such that the projection $\mathbf{X} \times_{\mathbf{Y}} \mathbf{U} \to \mathbf{U}$ splits as a morphism of topological spaces;

\- a fine covering is a G-equivariant morphism $\mathbf{X} \to \mathbf{Y}$ such that for any point $y$ of $\mathbf{Y}$ there exists a G-invariant open neighborhood $\mathbf{U}$ of $y$ in $\mathbf{Y}$ and a G-equivariant splitting of the projection $\mathbf{X} \times_{\mathbf{Y}} \mathbf{U} \to \mathbf{U}$.

Example 3.2. — The morphism  $G \rightarrow pt$  is a coarse covering but a fine covering only for G the trivial group.

In the case when G = e the fine and coarse topologies coincide and are equivalent to the usual open topology. We denote in this case the category G - Tlc by Tlc and the topology by Op. Note that Tlc is precisely the category of locally contractible topological spaces.

Proposition 3.3. — Let G be a finite group and I $^{1}$ be the unit interval which we consider as a G-space with trivial G-action. Then there are canonical equivalences of homotopy categories

$$
\begin{array}{r l} & {\mathcal {H} \left((\mathbf {G} - \mathrm{T} l c) _ {c}, \mathbf {I} ^ {1}\right) \cong \mathcal {H} _ {c} (\mathbf {G})} \\ & {\mathcal {H} \left((\mathbf {G} - \mathrm{T} l c) _ {f}, \mathbf {I} ^ {1}\right) \cong \mathcal {H} _ {f} (\mathbf {G}).} \end{array}
$$

Proof. — Every G-set may be considered as a topological space with the discrete topology which gives us functors

$$
\begin{array}{l} \pi^ {*}: \Delta^ {o p} (\mathbf {G} - S e t s) \to \Delta^ {o p} (S h v _ {c} (\mathbf {G} - \mathbf {T l c})) \\ \pi^ {*}: \Delta^ {o p} (\mathbf {G} - S e t s) \to \Delta^ {o p} (S h v _ {f} (\mathbf {G} - \mathbf {T l c})) \end{array}
$$

(where the latter one is just the composition of the former one with the embedding $\Delta^{op}(Shv_c(\mathbf{G} - \mathrm{Tlc})) \to \Delta^{op}(Shv_f(\mathbf{G} - \mathrm{Tlc}))$). One can check easily that the first functor takes coarse weak equivalences to simplicial weak equivalences in $\Delta^{op}(Shv_c(\mathbf{G} - \mathrm{Tlc}))$ and the second one takes fine weak equivalences to simplicial weak equivalences in $\Delta^{op}(Shv_f(\mathbf{G} - \mathrm{Tlc}))$. We claim that they define the required equivalences. In what follows we consired only the case of the fine topology. The coarse topology is analyzed similarly. Note first that any object in the image of $\pi^*$ is I$^1$-local and that the functor

$$
\pi^ {*}: \mathcal {H} _ {f} (\mathrm{G}) \rightarrow \mathcal {H} _ {s} (S h v _ {f} (\mathrm{G} - \mathrm{T} l c))
$$

is a full embedding. Thus, the only thing we have to show is that any simplicial sheaf on  $Shv_{f}$  (G - Tlc) is  $I^{1}$ -weakly equivalent to a simplicial sheaf which belongs to the image of  $\pi^{*}$ .

Our definition of a good G-space together with Lemma 1.16 implies that any simplicial sheaf $\mathcal{X}$ on $(\mathrm{G} - \mathrm{Tlc})_f$ is simplicially weakly equivalent to a simplicial sheaf $\mathcal{X}'$ whose terms are direct sums of sheaves represented by G-spaces $\mathrm{U}_{\alpha}$ such that $\mathrm{U}_{\alpha} \to \pi_0(\mathrm{U}_{\alpha})$ is a G-homotopy equivalence. Applying the functor $\pi_0$ to $\mathcal{X}'$ termwise we get a new simplicial sheaf $\pi_0(\mathcal{X}')$ which clearly belongs to the image of $\pi^*$. On the other hand the morphism $\mathcal{X}' \to \pi_0(\mathcal{X}')$ is an I$^1$-weak equivalence termwise and therefore an I$^1$-weak equivalence “globaly” by Lemma 2.14 which finishes the proof of the proposition.

## C-realizations - definition and examples

Consider the category $Sm / \mathbf{C}$ of smooth schemes over $\mathbf{C}$. The functor $\phi_{\mathbf{C}}^{-1}: X \mapsto \mathrm{X}(\mathbf{C})$ defines a continuous map of sites $\phi_{\mathbf{C}}: (\mathrm{T}lc)_{Op} \to (Sm / \mathbf{C})_{Nis}$.

Lemma 3.4. — The map of sites $\Phi_{\mathbf{C}}:(\mathrm{Tlc})_{Op}\to (\mathrm{Sm} / \mathbf{C})_{\mathcal{Nis}}$ is reasonable (see Definition 1.55).

Proof. — Follows easily from Proposition 1.16.

Since $\mathbf{A}^{1}(\mathbf{C})$ is contractible and the functor $\phi_{\mathbf{C}}^{-1}$ commutes with products $\phi_{\mathbf{C}}$ is a reasonable continuous map of sites with intervals (Definition 3.16) $((\mathrm{Tlc})_{Op}, \mathrm{I}^{1}) \to ((Sm / \mathbf{C})_{\mathcal{Nis}}, \mathbf{A}^{1})$. By Proposition 3.17 we conclude that there exists the functor of total inverse image $\mathbf{L}\phi_{\mathbf{C}}^{*}$ which we denote by $t^{\mathbf{C}}$. By Proposition 3.3 it takes values in the usual homotopy category $\mathcal{H}$.

More generally for any base scheme S and a C-point  $x: \text{Spec}(\mathbf{C}) \to \mathbf{S}$  we have a functor of C-realization

$$
t _ {x} ^ {\mathbf {C}}: \mathcal {H} (\mathrm{S}) \to \mathcal {H}
$$

defined as the composition  $t^{C} \circ Lx^{*}$ . Using Proposition 1.57(2) one can easily see that for any simplicial scheme X on Sm/S the value of  $t_{x}^{C}$  on X is the class of the geometrical realization of the simplicial topological space  $\mathcal{X}(\mathbf{C})$  in H. Note in particular that one has canonical isomorphisms in H of the form

$$
\begin{array}{r} t ^ {\mathbf {C}} (\mathbf {S} _ {s} ^ {1}) \cong \mathbf {S} ^ {1} \\ t ^ {\mathbf {C}} (\mathbf {S} _ {t} ^ {1}) \cong \mathbf {S} ^ {1} \end{array}
$$

and

$$
t ^ {\mathbf {C}} (\mathbf {B G}) \cong \mathbf {B} (\mathbf {G} (\mathbf {C}))
$$

for any smooth group scheme G over S.

## R-realization - definition and examples

Consider the category Sm/R of smooth schemes over R.

Lemma 3.5. — Let X be a smooth scheme over R. Then the topological space X(C) considered as a Z/2-space with respect to the complex conjugation action is good (see 3.1).

Lemma 3.5 shows that we have a functor $\phi_{\mathbf{R}}^{-1}: Sm / \mathbf{R} \to \mathbf{Z} / 2 - Tlc$ which takes a smooth variety $\mathbf{X}$ over $\mathbf{R}$ to the space $\mathrm{X}(\mathbf{C})$ where $\mathbf{Z} / 2$ acts by the complex conjugation.

Lemma 3.6. — The functor $\Phi_{\mathbf{R}}^{-1}$ defines a reasonable continuous map of sites $\Phi_{\mathbf{R}} : (\mathbf{Z}/2 - \mathrm{T}lc)_f \to (Sm/\mathbf{R})_{\mathcal{Nis}}$.

Proof. — To show that  $\phi_{R}$  is indeed a continuous map of sites, i.e. that for any sheaf F on  $(\mathbf{Z}/2 - Tlc)_{f}$  the presheaf  $(\phi_{\mathbf{R}})_{*}$  on Sm/S is a Nisnevich sheaf it is sufficient to verify that for an elementary distinguished square as in 1.3 the corresponding morphism  $\mathrm{U}(\mathbf{C})\coprod\mathrm{V}(\mathbf{C}) \to \mathrm{X}(\mathbf{C})$  is a covering in the fine topology. This is an easy exercise. The fact that  $\phi_{R}$  is reasonable follows from Proposition 1.16.

Since $\mathbf{A}^1 (\mathbf{R})$ is contractible and the functor $\phi_{\mathbf{R}}^{-1}$ commutes with products $\phi_{\mathbf{R}}$ is a reasonable continuous map of sites with intervals (Definition 3.16) $((\mathbf{Z} / 2 - \mathrm{Tlc})_f,\mathbf{I}^1)\to ((Sm / \mathbf{R})_{\mathcal{Nis}},\mathbf{A}^1)$. By Proposition 3.17 we conclude that there exists the functor of total inverse image $\mathbf{L}\phi_{\mathbf{R}}^{*}$ which we denote by $t^{\mathbf{R}}$. By Proposition 3.3 it takes values in the fine $\mathbf{Z} / 2$-equivariant homotopy category $\mathcal{H}_f(\mathbf{Z} / 2)$.

More generally for any base scheme S and an R-point  $x: \text{Spec}(\mathbf{R}) \to \mathbf{S}$  we have a functor of R-realization

$$
t _ {x} ^ {\mathbf {R}}: \mathcal {H} (\mathbf {S}) \to \mathcal {H} _ {f} (\mathbf {Z} / 2)
$$

defined as the composition  $t^{R} \circ Lx^{*}$ . Using Proposition 1.57(2) one can easily see that for any simplicial scheme X on Sm/S the value of  $t_{x}^{C}$  on X is the class of the diagonal simplicial set of the bisimplicial set  $\text{Sing}(\mathcal{X}(\mathbf{C}))$  in  $\mathcal{H}_{f}(\mathbf{Z}/2)$ .

## 4. Classifying spaces of algebraic groups

This section may be considered as an illustration of how one applies the general technique developed above. Its main results are Proposition 2.6, Theorem 3.13 and Proposition 3.14. Proposition 2.6 provides in particular a geometrical construction of a space which represents in $\mathcal{H}(\mathrm{S})$ the functor $\mathrm{H}_{et}^{1}(-,\mathrm{G})$ for étale group schemes $\mathbf{G}$ of order prime to char(S). Theorem 3.13 shows that algebraic K-theory of a regular scheme S can be described in terms of morphisms in $\mathcal{H}(\mathrm{S})$ with values in the infinite Grassmannian. Finally Proposition 3.14 shows how one can use $\mathbf{A}^{1}$-homotopy theory together with basic functoriality for simplicial sheaves on smooth sites to give a definition of Quillen-Thomason K-theory for all Noetherian schemes.

## 4.1. Generalities

## Classifying “spaces” of groups and monoids

In this section we prove some general results on the classifying spaces of sheaves of groups and monoids on a fixed site T.

If $\mathcal{X}$ is a simplicial sheaf (of sets) we denote by $\mathrm{F}_{Mon}(\mathcal{X})$ (resp. $\mathrm{F}(\mathcal{X})$) the free sheaf of simplicial monoids on $\mathcal{X}$. We say that a simplicial sheaf of monoids $\mathbf{M}$ is termwise free if any term $\mathbf{M}_i$ is a free monoid on a sheaf of sets. The same terminology is used for sheaves of simplicial groups.

We denote the category of sheaves of monoids (resp. groups) on T by  $Mon(T)$  (resp.  $Gr(T)$ ) and  $M \mapsto M^{+}$ ,  $\Delta^{op}Mon(T) \to \Delta^{op}Gr(T)$  the group completion functor, left adjoint to the inclusion  $\Delta^{op}Gr(T) \to \Delta^{op}Mon(T)$ .

Using the same technique as in the proof of 1.16 (applied to the class of free monoids on representable sheaves) one gets:

Lemma 1.1. — There exists a functor

$$
\Phi_ {M o n}: M o n (\Delta^ {o p} S h v (\mathrm{T})) \rightarrow M o n (\Delta^ {o p} S h v (\mathrm{T}))
$$

and a natural transformation $\Phi_{Mon} \to Id$ such that for any sheaf of simplicial monoids M one has:

1. for any $i \geqslant 0$ the sheaf of monoids $\Phi_{Mon}(\mathbf{M})_i$ is freely generated by a direct sum of representable sheaves (in particular $\Phi_{Mon}(\mathbf{M})$ is termwise free);

2. the morphism $\Phi_{Mon}(\mathbf{M}) \to \mathbf{M}$ is a trivial local fibration (as a morphism of simplicial sheaves).

More generally, any morphism $g: \mathbf{F} \to \mathbf{M}$ of simplicial sheaves of monoids, with $\mathbf{F}$ termwise freely generated by a direct sum of representable sheaves, admits a functorial factorisation: $\mathbf{F} \xrightarrow{\widetilde{g}} \widetilde{\Phi}_{Mon}(g) \xrightarrow{p_g} \mathbf{M}$ such that:

1. for any $i \geqslant 0$ the sheaf of monoids $\widetilde{\Phi}_{Mon}(g)_i$ is freely generated by a direct sum of representable sheaves;

2. the morphism $p_g: \widetilde{\Phi}_{Mon}(g) \to \mathbf{M}$ is a trivial local fibration (as a morphism of simplicial sheaves).

(Observe that the first part is a particular case of the second one by setting $\Phi_{Mon}(\mathbf{M}):= \widetilde{\Phi}_{Mon}(\emptyset \to \mathbf{M}).$

Let $\mathbf{M}$ be a sheaf of simplicial monoids on $\mathbf{T}$. We define the classifying space $\mathbf{BM}$ of $\mathbf{M}$ as the diagonal simplicial sheaf of the bisimplicial sheaf which maps $\mathbf{U}$ to the bisimplicial set $\mathbf{BM}(\mathbf{U}): n \mapsto \mathbf{N}(\mathbf{M}_n)$, where $\mathbf{N}(\mathbf{M}_n)$ is the nerve of the category associated to the monoid $\mathbf{M}_n$. It has terms $(\mathbf{M}_i)^i$ for $i \geqslant 0$ (with the convention that $(\mathbf{M}_0)^0 = pt$) and faces and degeneracy morphisms defined in the usual way using diagonals and product ([27]).

There is a canonical morphism of pointed simplicial sheaves of sets $\Sigma_s(\mathbf{M}) \to \mathbf{BM}$ which defines a morphism:

$$
\mathbf {M} \rightarrow \boldsymbol {\Omega} _ {s} ^ {1} (\mathbf {B M})
$$

where  $\Omega_{s}^{1}(-)$  is the right adjoint to  $\Sigma_{s}(-)$ . This morphism is seen to be a weak equivalence when M is a simplicial sheaf of groups, using points of T and the corresponding fact in the category of simplicial sets. We denote  $\mathbf{R}\Omega_{s}^{1}(-)$  the total right derived functor of  $\Omega_{s}^{1}(-)$  which is right adjoint to the suspension functor in the pointed simplicial homotopy category.  $\mathbf{R}\Omega_{s}^{1}(-)$  is thus the functor  $\mathcal{H}_{\bullet}^{s}(\mathrm{T})\to\mathcal{H}_{\bullet}^{s}(\mathrm{T})$  induced by the functor  $\Omega_{s}^{1}\circ Ex$  (which preserves weak equivalences).

Lemma 1.2. — Let M be a termwise free sheaf simplicial monoids. Then the morphism

$$
\mathbf {B M} \rightarrow \mathbf {B} (\mathbf {M} ^ {+})
$$

is a weak equivalence. Thus, there is a canonical isomorphism in $\mathcal{H}_{\bullet}^{s}(\mathrm{T})$ of the form

$$
\mathbf {M} ^ {+} \cong \mathbf {R} \boldsymbol {\Omega} _ {s} ^ {1} \mathbf {B M}.
$$

Proof. — Using the fact that the morphism is the diagonal of an (obvious) morphism of bisimplicial sheaves with terms of the form:  $\mathbf{B}(\mathbf{M}_{i}) \to \mathbf{B}(\mathbf{M}_{i})^{+}$  one easily reduces to the case M is simplicially constant which follows, using points of T, from the analogous statement for simplicial monoids of sets.

The following proposition is nontrivial because the functor of total inverse image does not commute in general with the loop space functor.

Proposition 1.3. — Let $f: \mathrm{T}_{1} \to \mathrm{T}_{2}$ be a reasonable morphism of sites. Assume in addition that $\mathrm{T}_{2}$ has products (but not fiber products!) and that the functor $f^{-1}$ commutes with them. Let further $\mathbf{M}$ be a sheaf of simplicial monoids on $\mathrm{T}_{2}$ such that all the terms $\mathbf{M}_{i}$ of $\mathbf{M}$ considered as sheaves of sets are direct sums of representable sheaves. Then there is a natural (in $\mathbf{M}$) isomorphism in $\mathcal{H}_{\bullet}^{s}(\mathrm{T}_{1})$ of the form

$$
\mathbf {L} f ^ {*} (\mathbf {R} (\Omega_ {s} ^ {1}) (\mathbf {B M})) \rightarrow \mathbf {R} (\Omega_ {s} ^ {1}) \mathbf {B} (f ^ {*} (\mathbf {M})).
$$

Proof. — Using Lemma 1.1 and Proposition 1.57(2) we may assume that each term of M is the sheaf of monoids freely generated by a direct sum of representable sheaves of sets. Since  $f^{-1}$  commutes with products of representable sheaves  $f^{*}(\mathbf{M})$  is again a monoid with the same property. By Lemma 1.2 it remains to define an isomorphism  $\mathbf{L}f^{*}(\mathbf{M}^{+})\to(f^{*}(\mathbf{M}))^{+}$ . We clearly have  $(f^{*}(\mathbf{M}))^{+}=f^{*}(\mathbf{M}^{+})$  which means by Proposition 1.52 that all we have to show is that  $M^{+}$ is admissible with respect to f (see Definition 1.49). This follows from Proposition 1.54 and the lemma below.

Lemma 1.4. — Let U be a direct sum of representable sheaves. Then the free group F(U) generated by U is admissible with respect to f.

Proof. — We are going to prove our result inductively using Lemma 1.53. Let  $l_{N}$  be the subsheaf in F(U) which consists of words of length less than or equal to N, i.e.  $l_{N}$  is the image of the canonical morphism

$$
\coprod_ {(i _ {1}, j _ {1}, \dots , i _ {n}, j _ {m})} \mathrm{U} ^ {i _ {1}} \times \mathrm{U} ^ {j _ {1}} \times \dots \times \mathrm{U} ^ {i _ {n}} \times \mathrm{U} ^ {j _ {m}} \rightarrow \mathrm{F} (\mathrm{U})
$$

where the coproduct is taken over all sequences such that $i_k, j_l > 0$ and $\sum i_1 + \sum j_1 \leqslant N$ for $N > 0$ and $l_0 = pt$.

Using Lemma 1.53(1) we see that it is sufficient to prove that for each N the sheaf  $l_{N}$  is admissible with respect to f. We already now that it is true for N=0. For

N = 1 we have  $l_{N} = pt \coprod U \coprod U$  which is admissible. Consider the diagram

$$
\begin{array}{c c c c c c c c} & & l _ {\mathrm{N-1}} \times \mathbf {U} & & & l _ {\mathrm{N-1}} \times \mathbf {U} & \\ l _ {\mathrm{N}} \times \mathbf {U} & \swarrow & & \searrow & \swarrow & & \searrow \\ & \searrow & & l _ {\mathrm{N}} & & & & l _ {\mathrm{N}} \times \mathbf {U} \\ & & l _ {\mathrm{N+1}} ^ {+} & \swarrow & \searrow & & \swarrow \\ & & & \searrow & l _ {\mathrm{N+1}} ^ {-} & & \end{array}
$$

where  $l_{N+1}^{+}$  and  $l_{N+1}^{-}$  are defined by the condition that the corresponding squares are cocartesian,  $l_{N-1} \to l_{N+1}$  is the obvious inclusion and two morphisms  $l_{N-1} \times U \to l_{N+1}$  are given by  $(x, a) \mapsto xa$  and  $(x, a) \mapsto xa^{-1}$  respectively. One can easily see that for any N > 1 the lower square is also cocartesian (which is equivalent to the fact that if  $xa = yb^{-1}$  then there exists a word w of length  $\leqslant N - 1$  such that  $x = wa^{-1}, y = wb$ ). Under our assumption on f the functor of the inverse image commutes with products it thus follows easily from 1.52 that the product of any admissible simplicial sheaf with U is still admissible. Thus by induction and Lemma 1.53(2) it suffices to verify that  $f^{*}(l_{N-1}) \to f^{*}(l_{N})$  is a monomorphism which can be easily done using the same diagram.

Lemma 1.5. — Let $i: \mathbf{A} \to \mathbf{B}$ be a monomorphism of simplicial sheaves which is a (simplicial) weak equivalence. Then $\mathrm{F}_{Mon}(i)$ (resp. $\mathrm{F}(i)$) is a simplicial weak equivalence. Moreover given any morphism of simplicial monoids $\mathrm{F}_{Mon}(\mathbf{A}) \to \mathbf{M}$ the morphism of simplicial monoids $\mathbf{M} \to \Sigma$ from $\mathbf{M}$ to the amalgamated sum $\Sigma$ of $\mathbf{M}$ and $\mathrm{F}_{Mon}(\mathbf{B})$ over $\mathrm{F}_{Mon}(\mathbf{A})$ is also a weak equivalence.

The analogous statement holds for simplicial sheaves of groups instead of simplicial sheaves of monoids.

Using points, it is sufficient to check it for T = Sets in which case it is not difficult, using the results of [26, II.4].

As was shown by Jardine ([18, Lemma 2.4]) there exists a subset  $B_{0}$  in  $C \cap W_{s}$  such that a simplicial sheaf X is simplicially fibrant if and only if the projection  $X \rightarrow pt$  has the right lifting property with respect to morphisms in  $B_{0}$ . Using the standard transfinite analogue of the small object argument (see the method after Corollary 2.18) and previous Lemma one gets:

Lemma 1.6. — There is a functor $Ex^{Mon}(-): \Delta^{op}Mon(T) \to \Delta^{op}Mon(T)$ (resp. $Ex^{Gr}(-): \Delta^{op}Gr(T) \to \Delta^{op}Gr(T)$) and a natural transformation $\theta^{Mon}: Id \to Ex^{Mon}$ (resp. $\theta^{Gr}: Id \to Ex^{Gr}$) such that for any $M \in \Delta^{op}Mon(T)$ (resp. $\in \Delta^{op}Gr(T)$) then $Ex^{Mon}(M)$ (resp. $Ex^{Gr}(M)$) is a fibrant simplicial sheaf and $\theta^{Mon}(M)$ (resp. $\theta^{Gr}(M)$) a (simplicial) weak equivalence.

Assume now that I is an interval on T (3). Using the previous Lemma, the fact that the functor  $Sing_{*}$  preserves finite products 3 and the same method as in the proof of Lemma 3.21 one obtains:

Lemma 1.7. — There is a functor $Ex_{\mathrm{I}}^{Mon}(-): \Delta^{op}Mon(\mathrm{T}) \to \Delta^{op}Mon(\mathrm{T})$ (resp. $Ex_{\mathrm{I}}^{Gr}(-): \Delta^{op}Gr(\mathrm{T}) \to \Delta^{op}Gr(\mathrm{T})$) and a natural transformation $\theta_{\mathrm{I}}^{Mon}: Id \to Ex_{\mathrm{I}}^{Mon}$ (resp. $\theta_{\mathrm{I}}^{Gr}: Id \to Ex_{\mathrm{I}}^{Gr}$) such that for any $\mathbf{M} \in \Delta^{op}Mon(\mathrm{T})$ (resp. $\in \Delta^{op}Gr(\mathrm{T})$) then $Ex_{\mathrm{I}}^{Mon}(\mathbf{M})$ (resp. $Ex_{\mathrm{I}}^{Gr}(\mathbf{M})$) is a fibrant I-local simplicial sheaf and $\theta_{\mathrm{I}}^{Mon}(\mathbf{M})$ (resp. $\theta_{\mathrm{I}}^{Gr}(\mathbf{M})$) an I-weak equivalence.

## Group completion of graded pointed simplicial monoids

Definition 1.8. — A pointed simplicial sheaf of monoids (on T) is a pair  $(\mathbf{M}, \alpha)$  consisting of a simplicial sheaf of monoids M on T and a morphism  $\alpha : N \to M$  (in  $\Delta^{op}Mon(Shv(T))$ ). A graded pointed simplicial sheaf of monoids is a triple  $(\mathbf{M}, \alpha, f)$  consisting of a pointed simplicial sheaf of monoids  $(\mathbf{M}, \alpha)$  together with a morphism (in  $\Delta^{op}Mon(Shv(T))$ )  $f: M \to N$  such that  $f \circ \alpha = Id$ .

Let $(\mathbf{M}, \alpha, f)$ be a graded pointed simplicial sheaf of monoids. Set $\mathbf{M}_n = f^{-1}(n)$. Multiplication with $\alpha(1)$ gives morphisms $\mathbf{M}_n \to \mathbf{M}_{n+1}$ and we set $\mathbf{M}_\infty$ to be the colimit of the corresponding system.

The triple  $(\widetilde{\Phi}_{Mon}(\alpha), \widetilde{\alpha}, f \circ p_{\alpha})$  is also a graded pointed simplicial sheaf of monoids. For simplicity, let  $\widetilde{M}$  denote from now on the simplicial sheaf of monoids  $\widetilde{\Phi}_{Mon}(\alpha)$ . Each of the morphisms  $p_{n}: \widetilde{M}_{n} \to M_{n}$  being the pull-back of a trivial local fibration is again a trivial local fibration and thus the obvious morphism  $\widetilde{M}_{\infty} \to M_{\infty}$  is a colimit of weak equivalences and therefore a weak equivalence 2.13. Consider now the group completion  $\widetilde{M}^{+}$  and let  $q: \widetilde{M}_{\infty} \times Z \to \widetilde{M}^{+}$  be the map

$$
(x _ {n}, m) \mapsto \widetilde {\alpha} ^ {m - n} x
$$

where $x_{n}\in \widetilde{\mathbf{M}}_{n}$ and $m\in \mathbf{Z}$. We have the following diagram:

$$
\begin{array}{c c c} \widetilde {\mathbf {M}} _ {\infty} \times \mathbf {Z} & \longrightarrow & \widetilde {\mathbf {M}} ^ {+} \\ \Big \downarrow & & \Big \downarrow \\ \mathbf {M} _ {\infty} \times \mathbf {Z} & & \mathbf {R} \Omega_ {s} ^ {1} \mathrm{B(M)} \end{array}
$$

where the vertical arrows are simplicial weak equivalences (the right hand side one by Lemma 1.2) and therefore we get a canonical morphism of the form  $\mathbf{M}_{\infty} \times \mathbf{Z} \to \mathbf{R}\Omega_{s}^{1}\mathbf{B}(\mathbf{M})$  in the pointed simplicial homotopy category of T.

Proposition 1.9. — Let  $(\mathbf{M}, \alpha, f)$  be a graded pointed simplicial sheaf of monoids and assume in addition that

1.  $a\underline{\pi}_{0}(f):a\underline{\pi}_{0}(\mathbf{M})\to\mathbf{N}$  is a bijection;

2. M is commutative in $\mathcal{H}_s(\mathbf{T})$.

Then the canonical morphism $\mathbf{M}_{\infty}\times \mathbf{Z}\rightarrow \mathbf{R}\Omega_s^1\mathrm{B}(\mathbf{M})$ is a simplicial weak equivalence.

Proof. — Clearly, we may assume that M is termwise free. Using our assumption that T has enough points we reduce the problem to the case of simplicial sets. The first condition of the lemma implies that one has

$$
\mathrm{H} _ {*} (\mathbf {M} _ {\infty} \times \mathbf {Z}) = \mathrm{H} _ {*} (\mathbf {M}) [ \alpha^ {- 1} ] = \mathrm{H} _ {*} (\mathbf {M}) [ \pi_ {0} (\mathbf {M}) ^ {- 1} ]
$$

and the second one implies that  $\mathrm{H}_{*}(\mathbf{M})$  is a commutative ring. Therefore, by [12, Theorem Q4, p. 97] the map  $M_{\infty} \times Z \to M^{+}$  gives an isomorphism on homology groups. On the other hand the condition that M is commutative implies that  $M_{\infty}$  has a (possibly non associative) multiplication as an object of the homotopy category. Since it is connected (by our first condition) we conclude that  $a\pi_{1}$  of  $M_{\infty}$  is abelian and acts trivially on all the higher homotopy groups which implies that the required map is a weak equivalence by Whitehead theorem.

Now we go back to our  $A^{1}$ -homotopy theory of smooth scheme over a noetherian scheme of finite dimension S, in the Nisnevich topology (in fact the result which follows may hold in the more general context of site with interval).

Theorem 1.10. — Let  $(\mathbf{M}, \alpha, f)$  be a graded pointed simplicial sheaf of monoids and assume that the following two conditions hold:

1. the map $a\underline{\pi}_0^{\mathbf{A}^1}(f): a\underline{\pi}_0^{\mathbf{A}^1}(\mathbf{M}) \to \mathbf{N}$ is a bijection

2. M is a commutative monoid in $\mathcal{H}(\mathbf{S})$

Then the canonical morphism $\mathbf{M}_{\infty}\times \mathbf{Z}\rightarrow \mathbf{R}\Omega_s^1\mathbf{B}(\mathbf{M})$ is an $\mathbf{A}^1$-weak equivalence.

Proof. — We apply Lemma 2.36 to the  $A^{1}$ -weak equivalence  $\mathbf{M} \to Ex_{\mathbf{A}^{1}}^{Mon}(\mathbf{M})$  given by 1.7. Observe that  $\mathbf{N} := Ex_{\mathbf{A}^{1}}^{Mon}(\mathbf{M})$  is graded (because its  $\pi_{0}$  is N) and obviously pointed. Thus each morphism  $M_{n} \to N_{n}$  is an  $A^{1}$ -weak equivalence (because a sum of morphisms is an  $A^{1}$ -weak equivalence if and only if each member is an  $A^{1}$ -weak equivalence). It follows (from 2.13) that  $M_{\infty} \to N_{\infty}$  is also an  $A^{1}$ -weak equivalence. The theorem follows now from Proposition 1.9.

## Homotopical classification of G-torsors

Let T be a site and G be a sheaf of simplicial groups on a site T. A right (resp. left) action of G on a simplicial sheaf X is a morphism  $a : X \times G \to X$  (resp.  $a : G \times X \to X$ ) such that the usual diagrams commute. A (left) action is called

(categorically) free if the morphism $\mathbf{G} \times \mathcal{X} \to \mathcal{X} \times \mathcal{X}$ of the form $(g, x) \mapsto (a(g, x), x)$ is a monomorphism.

For any right action of G on X define the quotient X/G as the coequilizer of the morphisms  $pr_{2}$  and a from  $X \times G$  to X.

A principal G-bundle (or equivalently a G-torsor) over X is a morphism  $Y \to X$  together with a free (right) action of G on Y over X such that the canonical morphism  $Y/G \to X$  is an isomorphism. Denote the set of isomorphism classes of principal G-bundles over X by P(X, G). This set is pointed by the trivial G-bundle  $G \times X \to X$ . If  $X' \to X$  is a morphism of simplicial sheaves and  $Y \to X$  is a principal G-bundle over X then  $Y \times X X'$  has a canonical structure of a principal G-bundle over  $X'$  which makes the correspondence  $X \mapsto P(X, G)$  into a contravariant functor from  $\Delta^{op}Shv(T)$  to the category of pointed sets.

Example 1.11. — Let X be a sheaf of sets on T. Denote by E(X) the simplicial sheaf of sets with n-th term  $X^{n+1}$  and with faces (resp. degeneracies) induced by partial projections (resp. diagonals). It has the characteristic property that for any simplicial sheaf Y the map:

$$
H o m _ {\Delta^ {o p} S h v (\mathrm{T})} (\mathcal {Y}, \operatorname{E} (\mathrm{X})) \rightarrow H o m _ {S h v (\mathrm{T})} (\mathcal {Y} _ {0}, \mathrm{X})
$$

is bijective.

When G is a sheaf of groups then  $\mathrm{E}(\mathrm{G})$  becomes a simplicial sheaf of groups (by functoriality observe that one has natural isomorphisms  $\mathrm{E}(\mathrm{X} \times \mathrm{Y}) \cong \mathrm{E}(\mathrm{X}) \times \mathrm{E}(\mathrm{Y})$ ), whose subgroup of vertices is G; in particular it gets right and left action by G. The morphism

$$
\begin{array}{l} \mathrm{E(G)} \to \mathrm{B(G)} \\ (g _ {0}, g _ {1},..., g _ {n}) \mapsto (g _ {0} g _ {1} ^ {- 1}, g _ {1} g _ {2} ^ {- 1},..., g _ {n - 1} g _ {n} ^ {- 1}, g _ {n}) \end{array}
$$

obviously induces an isomorphism:

$$
\mathbf {E} (\mathbf {G}) / \mathbf {G} \cong \mathbf {B} (\mathbf {G}).
$$

If G is a simplicial sheaf of groups, then taking the diagonal of the bisimplicial group  $(n, m) \mapsto \mathrm{E}(\mathrm{G}_{n})_{m}$  defines a sheaf of simplicial groups denoted  $\mathrm{E}(\mathrm{G})$  which again contains G as a subgroup.

Again the diagonal of the above morphism defines a morphism  $\mathrm{E}(\mathrm{G}) \to \mathrm{B}(\mathrm{G})$  which induces an isomorphism  $\mathrm{E}(\mathrm{G})/\mathrm{G} \cong \mathrm{B}(\mathrm{G})$ . This G-torsor  $\mathrm{E}(\mathrm{G}) \to \mathrm{B}(\mathrm{G})$  is called the universal G-torsor over  $\mathrm{B}(\mathrm{G})$ .

Lemma 1.12. — Let G be a simplicial sheaf of groups, and let E a G-torsor over a simplicial sheaf X. Then there is a trivial local fibration Y → X and a morphism Y → B(G) such that the pull-back of E to Y is isomorphic to the pull-back of E(G) to Y.

Proof. — Let  $Y_{E}$  be the quotient of the product  $\mathcal{E} \times \mathrm{E}(\mathrm{G})$  by the (right) diagonal action of G. The obvious projection  $p_{E}: Y_{E} \to X$  is clearly a trivial local fibration (it is a local fibration with “fibers” the locally fibrant and weakly contractible simplicial sheaf  $\mathrm{E}(\mathrm{G})$ ). But clearly by construction the pull-back of E to Y via  $p_{E}$  is isomorphic to the pull-back of  $\mathrm{E}(\mathrm{G})$  via the obvious morphism  $f_{E}: Y \to \mathrm{B}(\mathrm{G})$ .

Lemma 1.13. — Assume that G has simplicial dimension zero and $f: \mathcal{X} \to \mathcal{Y}$ is a trivial local fibration. Then the corresponding map $\mathrm{P}(\mathcal{Y}, \mathrm{G}) \to \mathrm{P}(\mathcal{X}, \mathrm{G})$ is a bijection.

Proof. — First recall that on the category of simplicial sets over a given simplicial set B, one can define the relative  $\pi_{0}$  functor,  $\pi_{0}(-)$ , as follows. Let  $f: E \to B$  be a map. Define  $\pi_{0}(f)$  as the simplicial set over X which sends n to the set  $\pi_{0}(E^{\Delta^{n}} \times_{B^{\Delta^{n}}} B_{n})$  of connected components of the fiber product  $E^{\Delta^{n}} \times_{B^{\Delta^{n}}} B_{n}$ . There is an obvious surjective map  $E \to \pi_{0}(f)$  of simplicial sets over B.

If p is a principal covering over X for a group G, and  $f: X \to Y$  a trivial Kan fibration, one checks immediately that the action of G on the simplicial set  $\pi_{0}(f \circ p)$  over Y makes  $\pi_{0}(f \circ p)$  into a principal covering over Y with group G.

By sheafifying this process, we get the relative  $\pi_{0}(-)$  functor, from the category of simplicial sheaves over X to itself. Given any principal G-bundle  $p: E \to X$  over X and a trivial local fibration  $f: X \to Y$ , it follows from what we said above (using points) that the action of G on  $\pi_{0}(f)$  define the structure of a G-torsor on the Y-simplicial sheaf  $\pi_{0}(f)$ , and this yields a map:

$$
\mathrm{P} (\mathcal {X}, \mathrm{G}) \rightarrow \mathrm{P} (\mathcal {Y}, \mathrm{G})
$$

which is the required inverse.

Using the same method as in the previous proof, one gets:

Lemma 1.14. — Assume that G has simplicial dimension zero, then for any simplicial sheaf $\mathcal{X}$, the map $\mathrm{P}(\mathcal{X},\mathrm{G})\to \mathrm{P}(\mathcal{X}\times \Delta^1,\mathrm{G})$ is a bijection. In particular, the functor $\mathrm{P}(-,\mathrm{G})$ is homotopy invariant.

Using Proposition 1.13 and the construction used in the proof of 1.12 one gets a natural transformation of pointed sets

$$
\begin{array}{l} \mathrm{P} (\mathcal {X}, \mathrm{G}) \to H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathcal {X}, \mathrm{BG}) \\ \mathcal {E} \mapsto f _ {\mathcal {E}} \circ (p _ {\mathcal {E}}) ^ {- 1}. \end{array}
$$

Let $BG \to BG$ be a trivial cofibration such that $BG$ is fibrant. Lemmas 1.14, 1.13, together with Proposition 1.13 easily imply, using the standard technique, the following result:

Proposition 1.15. — For any G of simplicial dimension zero the natural map

$$
\mathrm{P} (\mathcal {X}, \mathrm{G}) \rightarrow H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathcal {X}, \mathrm{BG})
$$

is a bijection. Thus, there exists a principal G-bundle $\mathcal{E}\mathrm{G}\to \mathcal{B}\mathrm{G}$ such that for any $\mathcal{X}$ the map

$$
\operatorname{Hom} (\mathscr {X}, \mathscr {B G}) \rightarrow \mathrm{P} (\mathscr {X}, \mathrm{G})
$$

given by $f\mapsto f^{*}(\mathcal{E}\mathbf{G}\to \mathcal{B}\mathbf{G})$ defines a bijection

$$
H o m _ {\mathcal {H} _ {s} (\mathrm{T})} (\mathcal {X}, \mathcal {B G})) \cong \mathrm{P} (\mathcal {X}, \mathrm{G}).
$$

The following results are then clear.

Proposition 1.16. — For any G of simplicial dimension zero and any object U of T one has

$$
\pi_ {i} (\mathcal {B} \mathrm{G} (\mathrm{U}), *) = \left\{ \begin{array}{l l} \mathrm{H} ^ {1} (\mathrm{U}, \mathrm{G}) := \mathrm{P} (\mathrm{U}, \mathrm{G}) & \text {for} i = 0 \\ \mathrm{G} (\mathrm{U}) & \text {for} i = 1 \\ 0 & \text {for} i > 0. \end{array} \right.
$$

Proposition 1.17. — Under the assumption of Proposition 1.15 two morphisms $f, g: \mathcal{X} \to \mathcal{BG}$ coincide in $\mathcal{H}_{s}(T)$ if and only if there exists a morphism $H: \mathcal{X} \to (\mathcal{E}G \times \mathcal{E}G)/G$ such that $pr_{1} \circ H = f$ and $pr_{2} \circ H = g$ where $pr_{1}, pr_{2}$ are the two canonical projections $(\mathcal{E}G \times \mathcal{E}G)/G \to \mathcal{BG}$.

## The étale classifying space  $B_{et}G$

From now on, S denotes a noetherian scheme of finite Krull dimension.

Let G be a sheaf of groups on  $(Sm/S)_{Nis}$ . Using the étale topology and the pair of adjoint functors between the simplicial homotopy categories associated with the obvious morphism of sites

$$
\pi : (S m / S) _ {e t} \rightarrow (S m / S) _ {\mathcal {N i s}}
$$

(see Proposition 1.47) we may define for any such $\mathbf{G}$ the object

$$
\mathbf {B} _ {e t} \mathbf {G} = \mathbf {R} \pi_ {*} \boldsymbol {\pi} ^ {*} (\mathbf {B G})
$$

of  $\mathcal{H}_{s}((Sm/S)_{Nis})$ . Note that if  $B_{et}G$  is a fibrant model for  $\mathrm{B}(\mathrm{G}_{et})$  in the category of simplicial étale sheaves, then  $\mathrm{B}_{et}(\mathrm{G})\cong\mathcal{B}_{et}G$  (where  $B_{et}G$  is now considered as a (fibrant) simplicial Nisnevich sheaf). By Proposition 1.16 for any sheaf of groups G on  $(Sm/S)_{Nis}$  and any smooth scheme U over S one has:

$$
H o m _ {\mathcal {H} _ {\bullet} ^ {s} ((S m / \mathrm{S}) _ {\bar {N} s})} (\Sigma_ {s} ^ {n} \mathrm{U} _ {+}, (\mathrm{BG}, *)) = \left\{ \begin{array}{l l} \mathrm{H} _ {\bar {N} s} ^ {1} (\mathrm{U}, \mathrm{G}) & \text {for} n = 0 \\ \mathrm{G} (\mathrm{U}) & \text {for} n = 1 \\ 0 & \text {for} n > 1 \end{array} \right.
$$

$$
H o m _ {\mathcal {H} _ {\bullet} ^ {s} ((S m / \mathrm{S}) _ {N i s})} (\boldsymbol {\Sigma} _ {s} ^ {n} \mathbf {U} _ {+}, (\mathbf {B} _ {e t} \mathbf {G}, *)) = \left\{ \begin{array}{l l} \mathbf {H} _ {e t} ^ {1} (\mathbf {U}, \mathbf {G}) & \text {for n = 0} \\ \mathbf {G} _ {e t} (\mathbf {U}) & \text {for n = 1} \\ 0 & \text {for n > 1.} \end{array} \right.
$$

In particular we have the following criterion for the morphism  $BG \rightarrow B_{et}G$  to be an isomorphism in  $\mathcal{H}_{s}((Sm/S)_{\mathcal{Nis}})$ .

Lemma 1.18. — The canonical morphism BG → B$_{et}$G is an isomorphism (in $\mathcal{H}_{s}((Sm/S)_{\tilde{N}\tilde{s}})$) if and only if G is a sheaf in the étale topology and one of the following equivalent conditions holds:

1. for any smooth scheme U over S one has $\mathrm{H}_{\mathcal{N}s}^{1}(\mathrm{U},\mathrm{G}) = \mathrm{H}_{et}^{1}(\mathrm{U},\mathrm{G});$

2. for any smooth scheme $\mathbf{X}$ over $\mathrm{S}$ and a point $x$ of $\mathbf{X}$ one has

$$
\mathbf {H} _ {e t} ^ {1} (S p e c (\mathcal {O} _ {\mathrm{X}, x} ^ {h}), \mathbf {G}) = *. \nonumber
$$

In some cases the object  $B_{et}G$  of  $\mathcal{H}_{s}((Sm/S)_{\bar{N}\bar{s}})$  has an “explicit” model in  $\Delta^{op}Shv_{\bar{N}\bar{s}}(Sm/S)$ . Let F be an étale sheaf on Sm/S with a free G-action (as Nisnevich sheaf). Then G acts freely on E(F) (see 1.11) and we set  $B(F, G)_{et}$  to be the quotient simplicial sheaf  $E(F)/G_{et}$  where et means that we consider the quotient in the étale topology. For any such F the morphism  $E(F) \to B(F, G)_{et}$  is clearly an étale principal  $G_{et}$-bundle. If  $B_{et}G$  is a fibrant model for  $B(G_{et})$  (in the category of simplicial étale sheaves) we have (by Proposition 1.15) a cartesian square (in the category of simplicial étale sheaves and thus also in the category of simplicial Nisnevich sheaves) of the form:

$$
\begin{array}{c c c} \mathrm{E(F)} & \longrightarrow & \mathcal {E} _ {e t} G \\ \Big \downarrow & & \Big \downarrow \\ \mathrm{B(F,G)} _ {e t} & \stackrel {{\phi}} {{\longrightarrow}} & \mathcal {B} _ {e t} \mathrm{G} \end{array}
$$

where $\phi$ is well defined up to a simplicial homotopy. Note also that $\phi$ becomes an isomorphism in $\mathcal{H}_s((Sm/S)_{et})$ for any F such that the morphism $F \to pt$ is an epimorphism (in the étale topology). Moreover one has the following result.

Lemma 1.19. — For any étale sheaf F with a free G-action the morphism $\phi: \mathrm{B}(\mathrm{F}, \mathrm{G})_{et} \to \mathrm{B}_{et}\mathrm{G} = \mathcal{B}_{et}\mathrm{G}$ is a monomorphism in $\mathcal{H}_s((Sm/S)_{\text{Nis}})$.

Proof. — By Proposition 1.13 it is sufficient to show that for any two morphisms $f, g: \mathcal{K} \to \mathrm{B}(\mathrm{F}, \mathrm{G})_{et}$ in $\Delta^{op}Shv_{\mathbb{N}is}(Sm/S)$ such that $\phi \circ f = \phi \circ g$ in $\mathcal{H}_s((Sm/S)_{\mathbb{N}is})$ we have $f = g$ in $\mathcal{H}_s((Sm/S)_{\mathbb{N}is})$. Propositions 1.17 and 1.15 imply that for any such $f$ and $g$ there exists a morphism $\mathrm{H}: \mathcal{K} \to ((\mathrm{E}(\mathrm{F}) \times \mathrm{E}(\mathrm{F})) / \mathrm{G})_{et}$ such that $pr_1 \circ \mathrm{H} = f$ and $pr_2 \circ \mathrm{H} = g$ where $pr_1, pr_2$ are the canonical projections $((\mathrm{E}(\mathrm{F}) \times \mathrm{E}(\mathrm{F})) / \mathrm{G})_{et} \to \mathrm{B}(\mathrm{F}, \mathrm{G})_{et}$. Thus what we have to show is that $pr_1 = pr_2$ in $\mathcal{H}_s((Sm/S)_{\mathbb{N}is})$. In order to do it

it is sufficient to show that there exists a G-equivariant simplicial homotopy connecting two projections from  $\mathbf{E}(\mathbf{F}) \times \mathbf{E}(\mathbf{F})$  to  $\mathbf{E}(\mathbf{F})$ . Using the observation that for any X one has  $Hom(\mathcal{X}, \mathbf{E}(\mathbf{F})) \cong Hom(\mathcal{X}_{0}, \mathbf{F})$ , the existence of such a homotopy is clear.

The following proposition gives a necessary and sufficient condition on F for  $\phi$  to be an isomorphism in  $\mathcal{H}_{s}((Sm/S)_{\mathcal{Nis}})$ .

Proposition 1.20. — Let G be an étale sheaf of groups on Sm/S and F be an étale sheaf with a free G-action. Then the following conditions are equivalent:

1. the morphism $\phi : \mathbf{B}(\mathbf{F}, \mathbf{G})_{et} \to \mathbf{B}_{et}\mathbf{G}$ is an isomorphism in the homotopy category $\mathcal{H}_s((Sm/S)_{\mathcal{Nis}})$;

2. for any smooth scheme X over S and an étale principal G-bundle  $E \rightarrow X$  the canonical morphism  $((E \times F)/G)_{et} \rightarrow X$  is an epimorphism in the Nisnevich topology.

Proof. — To prove that the first condition implies the second, what we have to show is that if S is henselian local and  $E \to S$  is an étale principal G-bundle over S then the morphism  $((E \times F)/G)_{et} \to S$  splits. In order to find such a splitting it is sufficient to find a G-equivariant morphism  $E \to F$ . Since  $B(F, G)_{et}$  is isomorphic to  $B_{et}G$  in  $\mathcal{H}_{s}((Sm/S)_{\tilde{N}s})$  Proposition 1.15 implies that there exists a cartesian square of the form

$$
\begin{array}{c c c} \mathbf {E} & \longrightarrow & \mathbf {E} (\mathbf {F},   \mathbf {G}) \\ \Big \downarrow & & \Big \downarrow \\ \mathbf {S} & \longrightarrow & \mathbf {B} (\mathbf {F},   \mathbf {G}) _ {e t} \end{array}
$$

where the upper horizontal arrow is G-equivariant. Since  $(\mathrm{E}(\mathrm{F}, \mathrm{G}))_{0} = \mathrm{F}$  this is the required morphism.

Assume now that the second condition holds. First observe that to prove $\Phi$ is an isomorphism in $\mathcal{H}_s((Sm/S)_{\mathcal{Nis}})$ it is sufficient to show that for any étale simplicial sheaf $\mathcal{X}$ and an étale principal G-bundle $\mathrm{E} \to \mathcal{X}$ there exists a weak equivalence $\mathcal{X}' \to \mathcal{X}$ in the Nisnevich topology and a G-equivariant morphism from $\mathrm{E}' = \mathcal{X}' \times_{\mathcal{X}} \mathrm{E}$ to $\mathrm{E}(\mathrm{F})$. Indeed, this implies that there is a section $s$ to $\Phi$ in $\mathcal{H}_s((Sm/S)_{\mathcal{Nis}})$; but this fact together with lemma 1.19 does imply formally that $\Phi$ is an isomorphism in $\mathcal{H}_s((Sm/S)_{\mathcal{Nis}})$.

To prove the assertion below, let $\mathcal{X}$ be an étale simplicial sheaf and $\mathrm{E} \to \mathcal{X}$ an étale principal G-bundle. Consider the restriction $\mathrm{E}_0 \to \mathcal{X}_0$ of $\mathrm{E}$ to $\mathcal{X}_0$. Since $\mathrm{F}$ satisfies the second condition of the proposition the morphism of sheaves in étale topology $p_0: \mathcal{X}_0' := (\mathrm{E}_0 \times_{\mathrm{G}} \mathrm{F})_{et} \to \mathcal{X}_0'$ is seen to be an epimorphism in Nisnevich topology. Moreover, there is an obvious G-equivariant morphism $\mathcal{X}_0' \times_{\mathcal{X}_0} \mathrm{E}_0 \to \mathrm{F}$.

Our result follows now from the Lemma 1.18 and the observation that for any $\mathcal{X}$ one has $Hom(\mathcal{X},\mathrm{E}(\mathrm{F})) = Hom(\mathcal{X}_0,\mathrm{F})$.

## 4.2. Geometrical models for $B_{et}G$ in $\mathcal{H}(S)$

Let G be a linear algebraic group over S i.e. a closed subgroup in  $GL_{n}$  over S for some n. For a fixed (closed) embedding  $i: G \to GL_{n}$  define the geometric classifying space  $\mathbf{B}_{gm}(G, i)$  of G with respect to i as follows. For  $m \geqslant 1$  let  $U_{m}$  be the open subscheme of  $A_{S}^{nm}$  where the diagonal action of G determined by i is free ( $U_{m}$  is the open subset in  $A_{S}^{nm}$  consisting of points  $x \in A_{S}^{nm}$  such that the action of the action of G defines a closed immersion  $\mathbf{G}_{\kappa(x)} \to \mathbf{A}_{\kappa(x)}^{nm}$ ). Let  $A^{nm}/G$  be the quotient S-scheme of the (diagonal) action of G on  $A_{S}^{nm}$,  $V_{m}$  be the image of  $U_{m}$  in  $A^{nm}/G$, an open subscheme; the projection  $U_{m} \to V_{m}$  defines  $V_{m}$  as the quotient scheme of  $U_{m}$  by the free action of G and  $V_{m}$  is thus a smooth S-scheme.

We have closed embeddings  $U_{m} \rightarrow U_{m+1}$  and  $V_{m} \rightarrow V_{m+1}$  corresponding to the embeddings  $Id \times \{0\} : A^{nm} \rightarrow A^{nm} \times A^{n}$  and we set

$$
\begin{array}{r} \mathbf {E} _ {g m} (\mathbf {G}, i) = c o l i m _ {m \in \mathbf {N}} \mathbf {U} _ {m} \\ \mathbf {B} _ {g m} (\mathbf {G}, i) = c o l i m _ {m \in \mathbf {N}} \mathbf {V} _ {m} \end{array}
$$

where the colimit is taken in the category of sheaves on  $(Sm/S)_{Nis}$  (or  $(Sm/S)_{et}$ ).

In this section we will show that the étale sheaf with G-action  $\mathrm{E}_{gm}(\mathbf{G},\imath)$  satisfies the conditions of Proposition 1.20 and that moreover as an object of the  $A^{1}$ -homotopy category, the geometrical classifying space  $\mathrm{B}_{gm}(\mathbf{G},\imath)$  for G is isomorphic to  $\mathrm{B}_{et}(\mathbf{G})$, and in particular, does not depend on the choice of embedding  $i:\mathbf{G}\to\mathbf{GL}_{n}$. This will allow us to relate  $\mathrm{H}_{et}^{1}(-,\mathbf{G})$  with the functor represented by  $\mathrm{B}_{gm}(\mathbf{G},\imath)$.

## An $\mathbf{A}^1$-contractibility result

The goal of this section is to prove the Proposition 2.3 which will be used below to give a geometric construction of objects in $\mathcal{H}(\mathrm{S})$ representing the classifying spaces $\mathbf{B}_{\ell}\mathbf{G}$ for subgroups $\mathbf{G}$ in $\mathrm{GL}_n$.

Definition 2.1. — Let X be a smooth scheme over S. An admissible gadget over X is a sequence  $(\mathcal{E}_{i}, \mathrm{U}_{i}, f_{i})_{i \geqslant 1}$  where  $E_{i}$  are vector bundles over X,  $U_{i}$  are open subschemes in  $E_{i}$  and  $f_{i}$  are monomorphisms  $U_{i} \to U_{i+1}$  over X such that the following conditions hold:

1. for any point $x: \operatorname{Spec}(k) \to \mathbf{X}$ of $\mathbf{X}$ there exists $i \geqslant 1$ such that $\mathbf{U}_i \times_{\mathbf{X}} \operatorname{Spec}(k)$ has a $k$-rational point;

2. let  $Z_{i}$  be the closed subset  $E_{i}-U_{i}$  in  $E_{i}$ , then for any i there exists j>i such that the morphism  $U_{i}=E_{i}-Z_{i}\to E_{j}-Z_{j}=U_{j}$  factors through the morphism  $E_{i}-Z_{i}\to E_{i}^{2}-Z_{i}^{2}$  of the form  $v\mapsto(0,v)$ .

For an admissible gadget  $(\mathcal{E}_{i},\mathrm{U}_{i},f_{i})$  we denote by  $U_{\infty}$  the inductive limit of sheaves represented by  $U_{i}$  with respect to morphisms  $f_{i}$ .

Example 2.2. — If  $i: G \to GL_{n}$  is a closed embedding of some algebraic S-group as a subgroup of  $GL_{n}$  then with the notations as in the introduction above one checks that  $(\mathbf{A}^{n}m_{\mathrm{S}}, \mathbf{U}_{m}, \mathbf{U}_{m} \to \mathbf{U}_{m+1})_{m \geqslant 1}$  is an admissible gadget over S.

Proposition 2.3. — Let  $(\mathcal{E}_{i}, U_{i}, f_{i})$  be an admissible gadget over a smooth S-scheme X. Then the canonical morphism  $U_{\infty} \to X$  is an  $A^{1}$ -weak equivalence.

Proof. — Let  $p: X \to S$  be the canonical morphism. Then  $p_{\#}(U_{\infty}/X) = U_{\infty}/S$  and  $p_{\#}(X/X) = X/S$  and therefore by Proposition 2.9 it is sufficient to show that the morphism  $U_{\infty} \to X$  is an  $A^{1}$ -weak equivalence of sheaves over X. In other words we may assume that X = S. Consider the simplicial sheaf  $Sing_{*}(U_{\infty})$ . By Lemma 3.8 the morphism  $s: U_{\infty} \to Sing_{*}(U_{\infty})$  is an  $A^{1}$ -weak equivalence. Thus in order to prove the proposition it is sufficient to show that the canonical morphism  $Sing_{*}(U_{\infty}) \to pt$  is an  $A^{1}$ -weak equivalence.

By definition for any smooth scheme V over S we have

$$
\operatorname{Sing} _ {n} \left(\mathrm{U} _ {\infty}\right) (\mathrm{V}) = \operatorname{colim} _ {i \rightarrow \infty} \operatorname{Hom} _ {\mathrm{S}} \left(\mathrm{V} \times \mathbf {A} ^ {n}, \mathrm{U} _ {i}\right).
$$

We will show that it is in fact a simplicial weak equivalence. Using the characterization of simplicial weak equivalences given in Lemma 1.11 and the fact that all our constructions commute with smooth base changes we see that it is sufficient to verify that if S a henselian local scheme then $Sing_{*}(\mathrm{U}_{\infty})(\mathrm{S})$ is a contractible simplicial set. Since the $\mathrm{U}_i$'s are smooth over S the first condition of our proposition implies that if S is a henselian local scheme then for some $i$ there exists an S-point $x: \mathrm{S} \to \mathrm{U}_i$ of $\mathrm{U}_i$ and therefore $Sing_{*}(\mathrm{U}_{\infty})(\mathrm{S})$ is nonempty.

In order to prove that it is contractible it is sufficient to show that for any  $n \geqslant 1$  any morphism  $\partial\Delta^{n} \to Sing_{*}(U_{\infty})(S)$  can be extended to a morphism  $\Delta^{n} \to Sing_{*}(U_{\infty})(S)$  (the case n=0 corresponds to the fact, already checked, that it is non empty). Let  $\partial\Delta_{A^{1}}^{n}$  be the subscheme in  $A_{S}^{n+1}$  given by the equation  $x_{1} \ldots x_{n}(\sum_{i=1}^{n} x_{i}-1)=0$ . Then the set  $Hom(\partial\Delta^{n}, Sing_{*}(U_{\infty})(S))$  coincides with the inductive limit of the sets of morphisms from  $(\partial\Delta_{A^{1}}^{n} \text{ to } U_{i} \text{ and similarly } Hom(\Delta^{n}, Sing_{*}(U_{\infty})(S)))$  coincides with the inductive limit of sets of morphisms from  $A_{S}^{n} = \Delta_{A^{1}}^{n}$  to  $U_{i}$ .

Since S is affine the morphism $\partial\Delta_{\mathbf{A}^{1}}^{n}\to\mathbf{A}_{\mathrm{S}}^{n}$ induces a surjective map $Hom(\mathbf{A}_{\mathrm{S}}^{n},\mathcal{E})\to Hom(\partial\Delta_{\mathbf{A}^{1}}^{n},\mathcal{E})$ for any vector bundle $\mathcal{E}$ on S. Let then $f\colon\partial\Delta_{\mathbf{A}^{1}}^{n}\to\mathrm{U}_{i}$ be a morphism. From what we just said, $f$ can be extended to a morphism $f^{\prime}:\mathbf{A}_{\mathrm{S}}^{n}\to\mathcal{E}_{i}$. Let $\mathrm{Z}_{i}$ be the closed subset $\mathcal{E}_{i}-\mathrm{U}_{i}$ which we consider as a reduced closed subscheme in $\mathcal{E}_{i}$. Since $(f^{\prime})^{-1}(\mathrm{Z}_{i})\cap\partial\Delta_{\mathbf{A}^{1}}^{n}=\emptyset$ there exists a morphism $\phi:\mathbf{A}_{\mathrm{S}}^{n}\to\mathcal{E}_{i}$ which is the constant morphism corresponding to 0 on $\partial\Delta_{\mathbf{A}^{1}}^{n}$ and is the constant morphism corresponding to the point $x$ of $\mathrm{U}_{i}$ on $(f^{\prime})^{-1}(\mathrm{Z}_{i})$. The product $\phi\times f^{\prime}:\mathbf{A}_{\mathrm{S}}^{n}\to\mathcal{E}_{i}^{2}$ takes

values in the complement to  $Z_{i}^{2}$  and coincides on  $\partial\Delta_{A^{1}}^{n}$  with the composition of f with the morphism  $\{0\}\times Id:\mathcal{E}_{i}\to\mathcal{E}_{i}^{2}$  which finishes the proof of the proposition.

## A geometric construction of $\mathbf{B}_{et}\mathbf{G}$

Let G be an étale sheaf of groups on Sm/S and U be a smooth scheme over S with G-action. For a class e in  $\mathrm{H}_{et}^{1}(\mathrm{S},\mathrm{G})$  represented by an étale principal G-bundle  $E\to S$  over S define  $U_{e}$  as the (étale) sheaf  $((E\times U)/G)_{et}$ .

Definition 2.4. — Let $(\mathcal{E}_i, \mathrm{U}_i, f_i)$ be an admissible gadget over S. A nice action of G on $(\mathcal{E}_i, \mathrm{U}_i, f_i)$ is a sequence of homomorphisms $\mathbf{G} \to \mathrm{GL}(\mathcal{E}_i)$ such that the following conditions hold:

1. for each  $i \geqslant 1$ ,  $U_{i}$  is G-invariant open subschemes in  $E_{i}$ , the morphisms  $f_{i}$  is G-equivariant and the factorizations required in Definition 2.1(2) can be chosen in the class of G-equivariant morphisms;

2. the action of $\mathbf{G}$ on $\mathbf{U}_i$ is free;

3. for any smooth scheme $\mathbf{X}$ over $\mathbf{S}$ and class $e \in \mathrm{H}_{et}^{1}(\mathbf{X}, \mathbf{G})$ there exists $i$ such that the morphism $(\mathbf{U}_i \times_{\mathbf{S}} \mathbf{X})_e \to \mathbf{X}$ is an epimorphism in the Nisnevich topology.

The following lemma is an immediate corollary of our definition and Proposition 1.20.

Lemma 2.5. — Let G be an étale sheaf of groups over S and  $(\mathcal{E}_{i}, U_{i}, f_{i})$  be an admissible gadget over S with a nice G-action. Then the canonical morphism

$$
\mathbf {B} (\mathrm{U} _ {\infty}, \mathbf {G}) _ {e t} \rightarrow \mathbf {B} _ {e t} \mathbf {G}
$$

is an isomorphism in $\mathcal{H}_s((Sm/S)_{\mathcal{N}is})$.

Proposition 2.6. — Let G be an étale sheaf of groups and  $(\mathcal{E}_{i}, \mathrm{U}_{i}, f_{i})$  be an admissible gadget over S with a nice G-action. Then there is a canonical isomorphism in H(S) of the form

$$
(\mathbf {U} _ {\infty} / \mathbf {G}) _ {e t} \cong \mathbf {B} _ {e t} \mathbf {G}.
$$

Remark 2.7. — It follows that for any linear algebraic group G over S the geometric classifying space defined above using an embedding into some  $GL_{n}$  over S doesn't depend on this embedding (up to isomorphism in  $\mathcal{H}(S)$ ) and moreover is isomorphic to its étale classifying space  $\mathrm{B}_{et}(\mathrm{G})$ .

Proof. — We start with the following lemmas.

Lemma 2.8. — Let  $E \to S$  be an étale principal G-bundle. Then the sheaves  $((\mathbf{E} \times \mathcal{E}_{i}) / \mathbf{G})_{et}$  are representable by vector bundles  $E_{i}'$  over S, the sheaves  $((\mathbf{E} \times \mathbf{U}_{i}) / \mathbf{G})_{et}$  by some open subschemes  $U_{i}'$  in  $E_{i}'$  and  $(\mathcal{E}_{i}', U_{i}', f_{i}')$  is again an admissible gadget over S.

Proof. — This follows immediately from the standard étale descent theory for vector bundles and our definitions.

Lemma 2.9. — Let X be a scheme with free G-action. Then the morphism of sheaves

$$
((\mathbf {U} _ {\infty} \times \mathbf {X}) / \mathbf {G}) _ {e t} \rightarrow (\mathbf {X} / \mathbf {G}) _ {e t}
$$

is an $\mathbf{A}^1$-weak equivalence.

Proof. — Let Y be a smooth scheme over S and  $\mathbf{Y}\to(\mathbf{X}/\mathbf{G})_{et}$  be a morphism. By Lemma 2.16 it is sufficient to verify that the projection  $((\mathbf{U}_{\infty}\times\mathbf{X})/\mathbf{G})_{et}\times_{(\mathbf{X}/\mathbf{G})_{et}}\mathbf{Y}\to\mathbf{Y}$  is an  $A^{1}$ -weak equivalence. Let  $\widetilde{Y}=Y\times_{(\mathbf{X}/\mathbf{G})_{et}}X$ . Then  $\widetilde{Y}$  is a principal étale G-bundle over Y and  $((\mathbf{U}_{\infty}\times\mathbf{X})/\mathbf{G})_{et}\times_{(\mathbf{X}/\mathbf{G})_{et}}Y$  is isomorphic over Y to  $((U_{\infty}\times\widetilde{\mathbf{Y}})/\mathbf{G})_{et}$  which implies the result we need by Lemma 2.8 and Proposition 2.3.

By Lemma 2.5 we have an isomorphism in $\mathcal{H}_s((Sm/S)_{Nis})$ of the form

$$
\mathbf {B} (\mathrm{U} _ {\infty}, \mathbf {G}) _ {e t} \cong \mathbf {B} _ {e t} \mathbf {G}.
$$

We have an obvious morphism $u: (\mathrm{U}_{\infty} / \mathrm{G})_{et} \to \mathrm{B}(\mathrm{U}_{\infty}, \mathrm{G}_{et})$ such that $u_n: (\mathrm{U}_{\infty} / \mathrm{G})_{et} \to (\mathrm{U}_{\infty}^{n+1} / \mathrm{G})_{et}$ is the diagonal morphism and it remains to show that this morphism is an $\mathbf{A}^1$-weak equivalence. By Proposition 2.14 it is sufficient to show that each $u_n$ is an $\mathbf{A}^1$-weak equivalence. In order to do it it is sufficient to show that the projection $(\mathrm{U}_{\infty}^{n+1} / \mathrm{G})_{et} \to (\mathrm{U}_{\infty}^n / \mathrm{G})_{et}$ is an $\mathbf{A}^1$-weak equivalence for any $n > 0$ which follows from Lemma 2.9.

It follows from Lemma 2.8 that in the case when all the residue fields of S are infinite the last condition of Definition 2.4 is automatically satisfied. The following example shows that in the case when finite field may be present it is not so.

Example 2.10. — Let  $S = \text{Spec}(\mathbf{F}_{2})$  and Z be the closed subset in  $A^{2}$  which is the union of the line x = y with the closed subset  $Z_{0}$  of dimension zero given by the equations

$$
\begin{array}{l} x + y = 1 \\ x y = 1 \end{array}
$$

Set  $\mathcal{E}_{i}=(\mathbf{A}^{2})^{i},\mathbf{U}_{i}=\mathbf{A}^{2i}-\mathbf{Z}^{i}$  and let  $f_{i}$  be the embeddings of the form  $x\mapsto(0,x)$ . Then  $(\mathcal{E}_{i},\mathbf{U}_{i},f_{i})$  is an admissible gadget over  $F_{2}$ . Consider the action of Z/2 on  $A^{2}$  of the form  $\sigma(x,y)=(y,x)$ . The corresponding action of Z/2 on  $(\mathcal{E}_{i},\mathbf{U}_{i},f_{i})$  satisfies the first two conditions of the definition of a nice action. Let now e be the only nontrivial element in  $\mathrm{H}_{el}^{1}(\mathbf{F}_{2},\mathbf{Z}/2)$ . Then  $(\mathbf{A}^{n}-\mathbf{Z})_{e}$  is the complement to  $Z_{e}$  which is the union of the line x=y with two rational points (1,0) and (0,1). In particular it means that for

any i the scheme  $(\mathbf{U}_{i})_{e}=\mathbf{A}^{2i}-(\mathbf{Z}_{e})^{i}$  has no  $F_{2}$ -rational points which means that the last condition of Definition 2.4 is not satisfied.

## 4.3. Examples

## étale group schemes

Proposition 3.1. — Let G be a finite étale group scheme over S of order prime to the characteristic of S. Then the object  $B_{et}G$  in  $\Delta^{op}Shv_{Nis}(Sm/S)$  is  $A^{1}$ -local.

Proof. — By definition  $\mathbf{B}_{et}\mathbf{G}=\mathbf{R}\pi_{*}(\mathbf{BG})$  where  $\pi:(Sm/S)_{et}\to(Sm/S)_{Nis}$  is the obvious morphism of sites. Since the third condition of Lemma 3.15 clearly holds for  $\pi$  so does the first and therefore it is sufficient to show that BG is  $A^{1}$ -local in  $\Delta^{op}Shv_{et}(Sm/S)$ . Let BG be a simplicially fibrant model for BG. Using Lemma 2.8(2) we see that it is sufficient to show that for any strictly henselian local scheme S and a finite étale group scheme G over S of order prime to  $char(S)$  the map of simplicial sets  $\mathcal{BG}(S)\to\mathcal{BG}(\mathbf{A}_{S}^{1})$  is a weak equivalence. Since S is strictly henselian G is just a finite group. In particular we obviously have  $\mathrm{G}(\mathrm{S})=\mathrm{G}(\mathbf{A}_{\mathrm{S}}^{1})$ . We also have  $\mathrm{H}_{et}^{1}(\mathrm{S},\mathrm{G})=*$  and  $\mathrm{H}_{et}^{1}(\mathbf{A}_{\mathrm{S}}^{1},\mathbf{G})=*$  where the second equality holds because of the homotopy invariance of the completion of  $\pi_{1}^{et}$  outside of characteristic ([13]) and therefore our map is a weak equivalence by Proposition 1.16.

Corollary 3.2. — Let G be a finite étale group scheme over S of order prime to the characteristic of S. Then for any smooth scheme U over S one has, for  $m, n \geqslant 0$ :

$$
H o m _ {\mathcal {H} _ {\bullet (\mathrm{S})}} \left(\Sigma_ {t} ^ {m} \Sigma_ {s} ^ {n} \left(\mathrm{U} _ {+}\right), \left(\mathrm{B} _ {e t} \mathrm{G}, *\right)\right) =
$$

$$
= \left\{ \begin{array}{l l} \mathbf {H} _ {e t} ^ {1} (\mathbf {U}, \mathbf {G}) & \text {for m, n = 0} \\ \mathbf {G} (\mathbf {U}) & \text {for m = 0, n = 1} \\ k e r (\mathbf {H} _ {e t} ^ {1} ((\mathbf {A} ^ {1} - \{0 \}) _ {\mathrm{S}}, \mathbf {G}) \to \mathbf {H} _ {e t} ^ {1} (\mathbf {S}, \mathbf {G})) & \text {for m = 1, n = 0} \\ 0 & \text {otherwise.} \end{array} \right.
$$

Proof. — Use Propositions 3.17, 3.1, 1.16.

Proposition 3.3. — Let $k$ be a field of characteristic $p > 0$ and $G$ be an étale $p$-group scheme over $\operatorname{Spec}(k)$. Then $B_{et}G \cong pt$ in $\mathcal{H}(\operatorname{Spec}(k))$.

Remark 3.4. — If k is a field of characteristic p > 0 and G is a finite étale group over k whose order is divisible by p but not equal to a power of p the structure of  $\mathbf{B}_{et}\mathbf{G}$  in  $\mathcal{H}(\mathbf{S})$  may be rather nontrivial.

We also have the following simple result which we give without a proof since we never use it.

Proposition 3.5. — Let G be a finite étale group scheme over S. Then the object BG in $\Delta^{op}Shv_{\mathcal{N}s}(Sm/S)$ is $\mathbf{A}^1$-local.

## $\mathrm{GL}_n,\mathrm{GL}_{\infty}$ and algebraic K-theory

Let us start with the following obvious analog of Hilbert's Theorem 90.

Lemma 3.6. — For any Noetherian scheme S and any n > 0 the canonical maps

$$
\mathrm{H} _ {\mathcal {Z} a r} ^ {1} (\mathrm{S}, \mathrm{GL} _ {n}) \rightarrow \mathrm{H} _ {\mathcal {N i s}} ^ {1} (\mathrm{S}, \mathrm{GL} _ {n}) \rightarrow \mathrm{H} _ {e t} ^ {1} (\mathrm{S}, \mathrm{GL} _ {n})
$$

are bijections.

Let $V_{n,i}$ be the linear space of linear morphisms $\mathcal{O}_S^n \to \mathcal{O}_S^i$ over S and $U_{n,i}$ be the open subscheme of monomorphisms in $V_{n,i}$. Denote by $Z_{n,i}$ the complement to $U_{n,i}$ in $V_{n,i}$. For any i we have a closed embedding $U_{n,i} \to U_{n,i+1}$ of the form $\phi \mapsto \{0\} \oplus \phi$. For any $n \geqslant 0$ the sequence $(V_{n,i}, U_{n,i}, f_i)$ is an admissible gadget over S and the natural action of $GL_n$ on it is nice. Note that $(U_{n,i}/GL_n)_et$ is representable by the Grassmannian $G(n,i)$ and correspondingly $(U_{n,\infty}/GL_n)_et$ by the infinite Grassmannian $G(n,\infty)$. Combining Proposition 2.6 with Lemmas 1.18 and 3.6 we get the following result.

## Proposition 3.7. — There are canonical isomorphisms in $\mathcal{H}(\mathrm{S})$ of the form

$$
\mathrm{BGL} _ {n} \cong \mathrm{B} _ {e t} \mathrm{GL} _ {n} \cong \mathrm{G} (n, \infty).
$$

In the case when n=1 we have  $BG_{m} \cong P^{\infty}$  and using the homotopy invariance of  $O^{*}$  and Pic on regular schemes and the same argument as in the proof of Proposition 3.1 we get the following result.

Proposition 3.8. — Let S be a regular scheme. Then for any smooth scheme U over S one has

$$
H o m _ {\mathcal {H} _ {\bullet (\mathrm{S})}} (\Sigma_ {s} ^ {n} \Sigma_ {t} ^ {m} \mathrm{U} _ {+}, (\mathbf {P} ^ {\infty}, *) = \left\{ \begin{array}{l l} P i c (\mathrm{U}) & \text {for m, n = 0} \\ \mathcal {O} ^ {*} (\mathrm{U}) & \text {for m = 0, n = 1} \\ \mathrm{H} ^ {0} (\mathrm{U}, \mathbf {Z}) & \text {for m = 1, n = 1} \\ 0 & \text {otherwise.} \end{array} \right.
$$

For n > 1 the objects  $BGL_{n} = B_{et}GL_{n}$  in  $\mathcal{H}_{s}((Sm/S)_{Nis})$  are not known to be  $A^{1}$ -local and it is not clear in general how to compute morphisms to  $BGL_{n}$  in  $\mathcal{H}(S)$  for  $1 < n < \infty$ . In the stable case of  $GL_{\infty}$  these morphisms are closely related to algebraic K-theory.

Consider the simplicial sheaf $\coprod_{n\geqslant 0}\mathrm{BGL}_n$. We have natural group homomorphisms $\mathrm{GL}_n\times \mathrm{GL}_m\to \mathrm{GL}_{n + m}$ which make this coproduct into a (non-commutative) monoid.

Let $\mathbf{B}(\coprod_{n\geqslant 0}\mathbf{BGL}_{n})$ be its classifying space. The following proposition is not much more than a reformulation of [30, Theorem 10.8]. As above, let us denote $\mathbf{R}\Omega_{s}^{1}(-)$ the right adjoint to the suspension: $\Sigma_{s}:\mathcal{H}_{\bullet}^{s}((Sm/S)_{Nis})\to\mathcal{H}_{\bullet}^{s}((Sm/S)_{Nis})$.

Proposition 3.9. — For any Noetherian base scheme S of finite dimension, smooth scheme X over S and  $n \geqslant 0$  one has a canonical isomorphism

$$
\operatorname{Hom} _ {\mathscr {H} _ {\bullet} \left((S m / S) _ {N i s}\right)} \left(\Sigma_ {s} ^ {n} \left(\mathrm{X} _ {+}\right), \left(\mathbf {R} \Omega_ {s} ^ {1}\right) \mathrm{B} \left(\coprod_ {n \geqslant 0} \mathrm{BGL} _ {n}\right)\right) \cong \mathrm{K} _ {n} (\mathrm{X})
$$

where  $\mathbf{K}_{n}(\mathbf{X})$  is the K-theory of perfect complexes (see [30, Definition 3.1]). In particular if X has an ample family of line bundles (say, is quasi-projective over an affine scheme) we have

$$
H o m _ {\mathcal {H} _ {\bullet} \left(\left(S m / S\right) _ {\mathcal {N} _ {i s}}\right)} \left(\Sigma_ {s} ^ {n} \left(\mathrm{X} _ {+}\right), \left(\mathbf {R} \Omega_ {s} ^ {1}\right) \mathrm{B} \left(\coprod_ {n \geqslant 0} \mathrm{BGL} _ {n}\right)\right) \cong \mathrm{K} _ {n} ^ {\mathrm{Q}} (\mathrm{X})
$$

where $\mathbf{K}_n^{\mathrm{Q}}(-)$ is the Quillen's K-theory.

Proof. — The second part of the proposition follows from the first one by [30, Corollary 3.9]. Let P(X) be the category of vector bundles and isomorphisms on a scheme X and N(P(X)) be the nerve of this category. The symmetric monoidal structure on P(X) given by  $\oplus$  defines a structure of a monoid on N(P(X)) (we ignore the fact that in order to make this statement precise one has first to replace P(X) by an equivalent small category with a strictly associative monoidal structure). If X is affine then  $\pi_{i+1}(B(N(P(X))),*)=:K_{i}^{Q}(X)=K_{i}(X)$ . We have a canonical morphism  $\phi:B(\coprod_{n\geqslant0}BGL_{n})(X)\to B(N(P(X)))$  which corresponds to the inclusion of the category of trivial bundles to the category of all bundles. Since any vector bundle is locally trivial in the Zariski and therefore the Nisnevich topology we conclude that  $\phi$  is a simplicial weak equivalence in  $\Delta^{op}Shv_{Nis}(Sm/S)$ . The statement of the proposition follows now in a formal way from [30, Theorem 10.8].

Consider the canonical morphism of the form

$$
\mathrm{BGL} _ {\infty} \times \mathbf {Z} \rightarrow \mathbf {R} \Omega_ {s} ^ {1} \mathrm{B} (\coprod_ {n \geqslant 0} \mathrm{BGL} _ {n})
$$

in $\mathcal{H}_s((Sm/S)_{Nis})$ (see the discussion before Proposition 1.9).

Proposition 3.10. — For any Noetherian scheme S of finite dimension the canonical morphism  $BGL_{\infty} \times Z \to R\Omega_{s}^{1}B(\coprod_{n \geqslant 0} BGL_{n})$  is an  $A^{1}$ -weak equivalence.

Proof. — Our result follows from Proposition 1.10 and the following two lemmas.

Lemma 3.11. — $a\underline{\pi}_0^{\mathbf{A}^1}(\mathrm{BGL}_n) = *$.

Proof. — This follows from the fact that $\underline{\pi}_0(\mathrm{BGL}_n) = *$ and Corollary 3.22.

Lemma 3.12. The simplicial monoid $\coprod$ BGL$_n$ is commutative in $\mathcal{H}$ (S).

Proof. — Follows easily from Proposition 3.7 by constructing explicit $\mathbf{A}^1$-homotopies for Grassmannians.

Theorem 3.13. — For any smooth scheme X over a regular scheme S and any $n, m \geqslant 0$ one has a canonical isomorphism

$$
H o m _ {\mathcal {H} _ {\bullet} (\mathrm{S})} \left(\boldsymbol {\Sigma} _ {t} ^ {m} \boldsymbol {\Sigma} _ {s} ^ {n} \mathbf {X} _ {+}, \left(\mathrm{BGL} _ {\infty} \times \mathbf {Z}, *\right)\right) = \mathrm{K} _ {n - m} (\mathbf {X})
$$

where for $n < m$ the groups $\mathbf{K}_{n - m}$ are zero.

Proof. — For m=0 this follows immediately from Propositions 3.9, 3.10, homotopy invariance of algebraic K-theory over regular schemes and Proposition 3.19 applied to a fibrant model of  $(\mathbf{R}\Omega_{s}^{1})\mathbf{B}(\coprod_{n\geqslant0}\mathbf{BGL}_{n})$ . For m>0 one has to use [30, Theorem 7.5(b)].

When S is not regular the situation becomes more complicated since Quillen's K-theory is not  $A^{1}$ -homotopy invariant on Sm/S and therefore the object  $(\mathbf{R}\Omega_{s}^{1})\mathrm{B}(\coprod_{n\geqslant0}\mathrm{BGL}_{n})$  is not  $A^{1}$ -local anymore. Nevertheless, it turns out to be possible, as the following proposition shows, to describe nonnegative algebraic K-theory of any Noetherian scheme of finite dimension purely in terms of basic functoriality of the simplicial homotopy categories and the  $A^{1}$ -homotopy theory.

Proposition 3.14. — Let S be a Noetherian scheme of finite dimension and  $p_{\mathrm{S}} : \mathrm{S} \to \operatorname{Spec}(\mathbf{Z})$  be the canonical morphism. Let further  $Ex_{\mathbf{A}^{1}}(\mathrm{G}(\infty, \infty))$  be an  $A^{1}$ -local model of the infinite Grassmannian  $\mathrm{G}(\infty, \infty)$  in the simplicial homotopy category  $\mathcal{H}_{s}((\mathrm{Sm}/\operatorname{Spec}(\mathbf{Z}))_{\mathcal{Nis}})$ . Then for any smooth scheme X over S and any  $n \geqslant 0$  one has a canonical isomorphism

$$
\mathrm{K} _ {n} (\mathrm{X}) = \operatorname{Hom} _ {\mathcal {H} _ {\bullet} ^ {s} ((S m / S) _ {\mathcal {N i s}})} \left(\Sigma_ {s} ^ {n} \mathrm{X} _ {+}, \mathrm{L} p _ {\mathrm{S}} ^ {*} \left(E x _ {\mathrm{A} ^ {1}} (\mathrm{G} (\infty , \infty)) \times \mathrm{Z}, *\right)\right)
$$

Proof. — By homotopy invariance of algebraic K-theory on regular schemes and Proposition 3.19 applied to a fibrant model of  $(\mathbf{R}\Omega_{s}^{1})\mathbf{B}(\coprod_{n\geqslant0}\mathbf{BGL}_{n})$  we conclude that this object is  $A^{1}$ -local and thus by Proposition 3.10 it is an  $A^{1}$ -local model for  $\mathbf{G}(\infty,\infty)\times\mathbf{Z}$ . Our result follows now from Propositions 3.9 and 1.3.

Remark 3.15. — For a scheme S which is not regular the object

$$
\mathbf {L} p _ {\mathrm{S}} ^ {*} (E x _ {\mathbf {A} ^ {1}} (\mathbf {G} (\infty , \infty), *))
$$

which represents by the previous proposition the algebraic K-theory over S is not  $A^{1}$ -local anymore and the theory it represents as an object of  $\mathcal{H}(S)$  is different from

the one it represents as an object of the simplicial homotopy category. This theory is some version of the homotopy invariant K-theory  $KH_{*}$  introduced in [33], but it is not clear whether or not it coincides with  $KH_{*}$  for an arbitrary S.

Finally let us mention the following result which shows that over regular base schemes one may replace  $Ex_{\mathbf{A}^{1}}(\mathbf{G}(\infty,\infty))$  by the more “accessible” object  $Sing_{*}(\mathbf{G}(\infty,\infty))$ .

Proposition 3.16. — Let S be a regular scheme. Then the canonical morphism

$$
\operatorname{Sing} _ {*} (\mathrm{G} (\infty , \infty)) \rightarrow E x _ {\mathbf {A} ^ {1}} (\mathrm{G} (\infty , \infty))
$$

is a simplicial weak equivalence.

Proof. — We will only give a sketch. As usually we may assume that S is local henselian and by Proposition 3.13 we have to show that the maps

$$
\pi_ {i} ((S i n g _ {*} (\mathbf {G} (\infty , \infty)) \times \mathbf {Z}) (\mathbf {S}), *) \to \mathbf {K} _ {i} (\mathbf {S})
$$

are isomorphisms. Observe first that for any affine scheme S one has

$$
\pi_ {0} ((S i n g _ {*} (\mathbf {G} (\infty , \infty)) \times \mathbf {Z}) (\mathbf {S}), *) = c o e q (\mathbf {K} _ {0} (\mathbf {S} \times \mathbf {A} ^ {1}) \rightrightarrows \mathbf {K} _ {0} (\mathbf {S}))
$$

where the two arrows are restrictions to points 0 and 1. This proves the isomorphism for i=0. It is also not hard to show that for any affine S the simplicial set  $Sing_{*}(\mathbf{G}(\infty,\infty))(S)$  is fibrant. Thus we may compute its homotopy groups by taking naive homotopy classes of maps from  $\partial\Delta_{s}^{*}$ . As was remarked at the end of the proof of Proposition 2.3 such classes correspond to  $A^{1}$ -homotopy classes of maps from the affine scheme  $\partial\Delta_{A^{1}}^{n}$  over S to  $\mathbf{G}(\infty,\infty)$ . Combining these facts together we conclude that for any affine S and any i>0 we have

$$
\pi_ {i} (S i n g _ {*} (\mathbf {G} (\infty , \infty)) (\mathbf {S}), *) = c o e q (\widetilde {\mathbf {K}} _ {0} (\partial \Delta_ {\mathbf {A} ^ {1}} ^ {i + 1} \times \mathbf {A} ^ {1}) \rightrightarrows \widetilde {\mathbf {K}} _ {0} (\partial \Delta_ {\mathbf {A} ^ {1}} ^ {i + 1}))
$$

where  $\widetilde{K}_{0}$  means that we consider the direct summand which consists of elements whose restriction to the distinguished point of  $\partial\Delta_{A^{1}}^{i+1}$  is zero. If S is regular and affine then one has a canonical isomorphisms  $\mathbf{K}_{i}(\mathbf{S})=\widetilde{\mathbf{K}}_{0}(\partial\Delta_{\mathbf{A}^{1}}^{i+1})$  ([8, 2.3]) which together with the homotopy invariance over regular schemes finishes the proof of the proposition.

## REFERENCES

[1] M. ARTIN, On the joins of Hensel rings, Advances in Math. 7 (1971), 282-296.

[2] A. K. BOUSFIELD and E. M. FRIEDLANDER, Homotopy theory of  $\Gamma$ -spaces, spectra, and bisimplicial sets, Lecture Notes in Math. 658 (1978), 80-130.

[3] A. K. BOUSFIELD and D. M. KAN, Homotopy limits, completions and localizations, Lecture Notes in Math. 304 (1972), Springer-Verlag.

[4] A. K. BOUSFIELD, Constructions of factorization systems in categories, J. Pure Appl. Alg. 9 (1977), 207-220.

[5] A. K. BOUSFIELD, Homotopical localizations of spaces, American J. of Math. 119 (1997), 1321-1354.

[6] K. S. BROWN, Abstract homotopy theory and generalized sheaf cohomology, Trans. A.M.S., vol. 186 (1973), 419-458.

[7] K. S. BROWN and S. M. GERSTEN, Algebraic K-theory and generalized sheaf cohomology, Lecture Notes in Math. 341 (1973), 266-292.

[8] B. DAYTON, K-theory of tetrahedra, J. Algebra (1979), 129-144.

[9] W. G. DWYER, P. S. HIRSCHHORN, and D. M. KAN, Model categories and general abstract homotopy theory, In preparation.

[10] E. DROR-FARJOUN, Cellular Spaces, Null Spaces and Homotopy Localizations, Lecture Notes in Math. 1622 (1973), Springer-Verlag.

[11] R. FRITSCH and R. A. PICCININI, Cellular structures in topology, Cambridge, Cambridge Univ. Press, 1990.

[12] E. M. FRIEDLANDER and B. MAZUR, Filtrations on the homology of algebraic varieties, vol. 529 of Memoir of the AMS, AMS, Providence, RI, 1994.

[13] A. GROTHENDIECK, M. ARTIN and J.-L. VERDIER, Théorie des topos et cohomologie étale des schémas (SGA 4), Lecture Notes in Math. 269, 270, 305 (1972-1973), Heidelberg, Springer.

[14] A. GROTHENDIECK and J. DIEUDONNÉ, Étude globale élémentaire de quelques classes de morphismes (EGA 2), Publ. Math. IHES 8, 1961.

[15] A. GROTHENDIECK and J. DIEUDONNÉ, Étude locale des schémas et des morphismes de schémas (EGA 4), Publ. Math. IHES 20, 24, 28, 32, 1964-1967.

[16] M. Hovey, B. Shipley and J. Smith, Symmetric spectra, Preprint, 1996.

[17] J. F. JARDINE, Simplicial objects in a Grothendieck topos, Contemporary Math. 55(1) (1986), 193-239.

[18] J. F. JARDINE, Simplicial presheaves, J. Pure Appl. Algebra 47 (1987), 35-87.

[19] J. F. JARDINE, Stable homotopy theory of simplicial presheaves, Canadian J. Math. 39(3) (1987), 733-747.

[20] A. JOYAL, Letter to A. Grothendieck (1984).

[21] S. MACLANE, Categories for working mathematician, vol. 5 of Graduate texts in Mathematics, Springer-Verlag, 1971.

[22] J. P. MAY, Simplicial objects in algebraic topology, Van Nostrand, 1968.

[23] J. P. MEYER, Cosimplicial homotopies, Proc. AMS 108(1) (1990), 9-17.

[24] J. S. MILNE, étale Cohomology, Princeton Math. Studies 33, Princeton University Press (1980).

[25] Y. NISNEVICH, The completely decomposed topology on schemes and associated descent spectral sequences in algebraic K-theory. In Algebraic K-theory: connections with geometry and topology, p. 241-342. Kluwer Acad. Publ., Dordrecht, 1989.

[26] D. QUILLEN, Homotopical algebra, Lecture Notes in Math. 43 (1973), Berlin, Springer-Verlag.

[27] G. B. SEGAL, Classifying spaces and spectral sequences, Publ. Math. IHES 34 (1968), 105-112.

[28] A. SUSLIN, and V. VOEVODSKY, Singular homology of abstract algebraic varieties, Invent. math. 123 (1996), 61-94.

[29] R. THOMASON, Algebraic K-theory and étale cohomology, Ann. Sci. ENS 18 (1985), 437-552.

[30] R. THOMASON and T. TROBAUGH, Higher algebraic K-theory of schemes and of derived categories, In The Grothendieck festchrift, vol. 3 (1990), 247-436, Boston, Birkhauser.

[31] V. VOEVODSKY, Homology of schemes, Selecta Mathematica, New Series 2(1) (1996), 111-153.

[32] V. VOEVODSKY, The  $A^{1}$ -homotopy theory, Proceedings of the international congress of mathematicians, Berlin, 1998.

[33] C. WEIBEL, Homotopy K-theory, Contemp. Math. 83 (1987), 461-488. Theorem

F. M.
Institut de Mathématiques de Jussieu
Université Paris 7 Denis Diderot
Case Postale 7012
2, place Jussieu
75251 Paris cedex

V. V.
Institute for Advanced Study
Olden Lane
Princeton, NJ08540
U.S.A.

Manuscrit reçu le 23 octobre 1998.