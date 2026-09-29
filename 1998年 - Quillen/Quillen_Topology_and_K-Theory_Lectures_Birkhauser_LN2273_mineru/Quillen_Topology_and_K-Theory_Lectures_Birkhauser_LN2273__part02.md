## Chapter 36 Long Exact Sequences of $K$-Groups

## Recall

Theorem A: $f:\mathcal{C}\to\mathcal{C}'$ is a homotopy equivalence provided any of the following hold for all $Y$ in $\mathcal{C}'$

(i)  $f/Y \simeq *,$

(i') f is pre-cofibered and  $f^{-1}Y \simeq *,$

(ii)  $Y \setminus f \simeq *,$

(ii') $f$ is pre-fibered and $f^{-1}Y\simeq *$.

Pre-cofibered means “there are cobase change operations,” i.e., given  $u: Y \to Y'$  in  $C'$ , we have a cobase change functor  $u_{*}: f^{-1}(Y) \to f^{-1}(Y')$ , that is,  $f^{-1}Y \hookrightarrow f/Y$  has an adjoint, namely,  $(X, fX \stackrel{u}{\longmapsto} Y) \longmapsto u_{*}(X)$ .

Suppose $\mathcal{M}$ is an exact category. Let $\mathcal{E}(\mathcal{M})$ denote the category of short exact sequences $M' \hookrightarrow M \twoheadrightarrow M''$ in $\mathcal{M}$. $\mathcal{E}(\mathcal{M})$ is itself an exact category, and we have three exact functors $s, t, q$ from $\mathcal{E}(\mathcal{M})$ to $\mathcal{M}$:

$s(M^{\prime} \hookrightarrow M \twoheadrightarrow M^{\prime\prime}) = \text{sub-object} = M^{\prime},$

$$
t (M ^ {\prime} \hookrightarrow M \twoheadrightarrow M ^ {\prime \prime}) = \text { total   object } = M,
$$

$q(M' \hookrightarrow M \twoheadrightarrow M'') = \text{quotient object} = M''.$

Remark Exact functors induce maps on $Q$-categories and hence on $K$-groups.

Theorem  $(s,q):\mathcal{E}(\mathcal{M})\to\mathcal{M}\times\mathcal{M}$  induces a homotopy equivalence on Q-categories, i.e.,  $Q(\mathcal{E}(\mathcal{M}))\simeq Q\mathcal{M}\times Q\mathcal{M}$ .

(†) Corollary: Given an exact category N and an exact sequence of exact functors  $0 \rightarrow F' \rightarrow F \rightarrow F'' \rightarrow 0$  from N into M. Then on K-groups, we have  $F_{*} = F_{*}' + F_{*}'' : K_{i}(\mathcal{N}) \rightarrow K_{i}(\mathcal{M})$ .

Proof We have the diagram

$$
\begin{array}{c} Q (\mathcal {E} (\mathcal {M})) \xrightarrow [ (s , q) ]{t} Q \mathcal {M} \\ \hline \end{array} Q \mathcal {M} \times Q \mathcal {M}
$$

and a section $\eta$ of $\mathcal{E}(\mathcal{M})\xrightarrow{(s,q)}\mathcal{M}\times \mathcal{M}$ by

$$
(M ^ {\prime}, M ^ {\prime \prime}) \mapsto (M ^ {\prime} \hookrightarrow M ^ {\prime} \oplus M ^ {\prime \prime} \twoheadrightarrow M ^ {\prime \prime}).
$$

Thus adding  $Q(\eta)$  to the diagram, we get the result.

Proof of Theorem It is sufficient by Theorem A to show that for any $(M', M'') \in Q\mathcal{M} \times Q\mathcal{M}$, we have $Q(\mathcal{E}(M))(M', M'') \simeq *$. The typical element is

![](images/page_1_image_5.jpg)

By pulling back with respect to $\eta$ and pushing forward by $\xi$, we retract $Q(\mathcal{E}(\mathcal{M})) / (M', M'')$ into the full subcategory of diagrams

![](images/page_1_image_7.jpg)

But this full subcategory has the initial object

![](images/page_1_image_9.jpg)

Theorem B: Let $f: \mathcal{C} \to \mathcal{C}'$ and suppose that for any $Y \to Y'$ in $\mathcal{C}'$, the induced functor $f/Y \to f/Y$ is a homotopy equivalence. Then the homotopy fiber of $Bf: BC \to BC'$ over $Y$ is homotopy equivalent to $B(f/Y)$.

Geometrical Example Let $g: K \to L$ be a map of simplicial complexes. Take $\mathcal{C}$ to be the poset of simplices in $K, \mathcal{C}'$ to be the poset of simplices in $L$ and suppose $y$ is a simplex in $L$. Then

$$
\begin{array}{r l} f / y & = \{\text { simplices } x \text { in } K: f x \subset y \} \\ & = \{\text { simplices   in } f ^ {- 1} \overline {{y}} \}, \end{array}
$$

and  $f^{-1}y' \simeq f^{-1}y$  for all  $y' \leq y$  implies that  $f^{-1}y \simeq$  homotopy fiber.

Localization Theorem Suppose $\mathcal{A}$ is an abelian category and $\mathcal{B}$ a Serre subcategory with $\mathcal{A} / \mathcal{B}$ the quotient abelian category. Then

$$
B Q \mathcal {B} \simeq \text { homotopy   fiber   of } (B Q \mathcal {A} \longrightarrow B Q (\mathcal {A} / \mathcal {B})).
$$

Proof From Theorem B plus lots of work, we have a short exact sequence

$$
Q \mathcal {B} \longrightarrow Q \mathcal {A} \longrightarrow Q (\mathcal {A} / \mathcal {B}).
$$

See Quillen's paper.

□

Corollary There is an exact sequence of $K$-groups

$$
\dots \longrightarrow K _ {i} \mathcal {B} \longrightarrow K _ {i} \mathcal {A} \longrightarrow K _ {i} \mathcal {A} / \mathcal {B} \longrightarrow K _ {i - 1} \mathcal {B} \longrightarrow \dots
$$

□

Remark Suppose $V \in \mathcal{A} / \mathcal{B}$. We have

$$
S B \operatorname{Aut} V \longrightarrow B Q (\mathcal {A} / \mathcal {B}),
$$

so

$$
B \operatorname{Aut} V \longrightarrow \Omega B Q (\mathcal {A} / \mathcal {B}),
$$

and we get

$$
\begin{array}{c} \Omega B Q (\mathcal {A} / \mathcal {B}) \longrightarrow B Q \mathcal {B} \longrightarrow B Q \mathcal {A} \longrightarrow B Q (\mathcal {A} / \mathcal {B}). \\ \uparrow \\ B \text {Aut} V \end{array}
$$

We exhibit this map. Given $V \in \mathcal{A} / \mathcal{B}$, take $\mathcal{A} = \operatorname{Modf} A, \mathcal{B} = S$-torsion and $\mathcal{A} / \mathcal{B} = \operatorname{Modf}(S^{-1}A)$, where $A$ is a noetherian ring.

Construction: Take the poset $JV$ of all finitely generated $A$-submodules in $M \subset V$ so that $V = S^{-1}(M)$. $J(V) \simeq *$ because we can take suprema. Let $\widetilde{JV} = \text{poset of layers in } JV$. We have a functor

$$
\begin{array}{c} \widetilde {J} V \longrightarrow Q \mathcal {B} \\ (M _ {0}, M _ {1}) \longmapsto M _ {1} / M _ {0}. \end{array}
$$

Now form the cofibered category $\widetilde{JV}$ Aut $V$ over Aut $V$ with fiber $\widetilde{JV}$. The objects are still $(M_0, M_1)$ but now morphisms

$$
(M _ {0} ^ {\prime}, M _ {1} ^ {\prime}) \longrightarrow (M _ {0}, M _ {1})
$$

are automorphisms $\theta$ of $V$ so that $(\theta M_0', \theta M_1') \leq (M_0, M_1)$. We have a functor

$$
\begin{array}{c} \widetilde {J}   V \text {Aut}   V \longrightarrow Q \mathcal {B} \\ \Biggl \downarrow_ {\text {homotopy equivalence by Theorem A}} \\ \text {Aut}   V \end{array}
$$

Example 1 Recall if $A$ is regular noetherian, then

$$
K _ {0} A \cong K _ {0} A [ T ].
$$

This generalizes with a proof as before, so

$$
K _ {n} A \cong K _ {n} A [ T ].
$$

Example 2 For $A$ regular, consider $K_{*}A[T,T^{-1}]$. We have

$$
K _ {*} (\mathcal {P} _ {A}) = K _ {*} (\text { Modf   } A) \text {   for   } A \text {   and   also   for   } A [ T ]
$$

and consider

$$
\begin{array}{c} \text {Modf} A [ T ] \longrightarrow \text {Modf} A ([ T ]) \longrightarrow \text {Modf} A [ T, T ^ {- 1} ]. \\ _ {T - \text {torsion}} \\ \mathcal {B} \end{array}
$$

By Devissage, $\mathcal{B}$ has the same $K$-groups as $A[T]$-modules killed by $T$, and so

$$
K _ {*} \mathcal {B} = K _ {*} A.
$$

We get the long exact sequence

$$
\begin{array}{c} \dots \longrightarrow K _ {i} A \xrightarrow {\alpha} K _ {i} A [ T ] \longrightarrow K _ {i} A [ T, T ^ {- 1} ] \longrightarrow K _ {i - 1} A \longrightarrow \dots . \\ \Bigg \| \\ K _ {i} A \end{array}
$$

To compute $\alpha$, take $M \in \operatorname{Modf} A \subset \mathcal{B}$. We have the exact sequence

$$
0 \longrightarrow \overbrace {A [ T ] \otimes_ {A}} ^ {F} M \stackrel {\times T} {\longrightarrow} A [ T ] \otimes_ {A} M \longrightarrow M \longrightarrow 0
$$

of exact functors from Modf A to Modf A[T].

By Corollary (†), we conclude that  $\alpha = 0$ , i.e.,  $F_{*} = F_{*} + \alpha$ , and so finally

$$
K _ {i} A [ T, T ^ {- 1} ] \cong K _ {i} A \oplus K _ {i - 1} A.
$$

Let

X = algebraic variety over a field k,

$M_{X} = (\text{abelian})$ category of coherent sheaves on X,

$P_{X}$  = category of locally free sheaves on X.

("vector-bundles")

If

X = Spec A, for A a finitely generated k-algebra,

$M_{X}$  = finitely generated modules over A,

$P_{X}$  = finitely generated projective modules over A,

then  $K_{i} X \stackrel{d}{=} K_{i} P_{X}$  is a contravariant functor in X because  $f : X \to Y$  induces an exact functor  $f^{*} : P_{Y} \to P_{X}$ .

Let us also define $K_{i}^{\prime}X \stackrel{a}{=} K_{i}\mathcal{M}_{X}$, a covariant functor in $X$ for proper maps. This holds because of Grothendieck's argument for $i = 0$: If $f: X \to Y$ and $F$ is a coherent sheaf on $X$, then $R^{q}f_{*}F$ are coherent sheaves on $Y$ and vanish for $q > \dim X$. So we can form

$$
\sum_ {q \geq 0} (- 1) ^ {q} \left[ R ^ {q} f _ {*} F \right] \in K _ {0} \mathcal {M} _ {Y}.
$$

This gives a map $\mathcal{M}_X \to K_0\mathcal{M}_Y$ which is additive for short exact sequences, namely, the Euler characteristic, and so induces $K_0\mathcal{M}_X \to K_0\mathcal{M}_Y$.

For higher $K$-groups, assume that $X$ is quasi-projective, i.e., $X$ can be embedded in projective space, so a proper morphism $f: X \to Y$ is projective, i.e., factors as a composition $X \stackrel{\epsilon}{\hookrightarrow} Y \times P^n \stackrel{p}{\to} Y$ with $i\epsilon$ a closed embedding and $p$ the projection.

Then the map $\epsilon_{*}:K_{i}^{\prime}(X)\to K_{i}^{\prime}(Y\times P^{n})$ is induced by the embedding $\mathcal{M}_X\to \mathcal{M}_{Y\times P^n}$. The map $p_*:K_i(Y\times P^n)\to K_i(Y)$ can be defined using Serre's theorem

$$
R ^ {q} p _ {*} (F (n)) = 0, \text { for } q > 0
$$

where

$$
F (n) = F \otimes \mathcal {O} (1) ^ {\otimes n}.
$$

This shows that large chunks of $\mathcal{M}_{Y\times P^n}$ (and thus of $\mathcal{M}_X$) map, by $R^0 p_*$ (resp. by $R^0 f_*$) into $\mathcal{M}_Y$, in a way preserving short exact sequences, and that is sufficient. For a more detailed and sophisticated explanation see §6.2 of Quillen's paper [10].

Suppose $A \xrightarrow{f} B$ is a map between noetherian rings. This induces an exact functor $\mathcal{P}_A \to \mathcal{P}_B$, where $P \mapsto P \otimes_A B$, and hence a map $K_i A \to K_i B$.

However in general, the map Modf $A \to \text{Modf } B$ given by $M \mapsto B \otimes_A M$ is not exact. But assume that $B_A$ has finite Tor dimension, i.e., the $i$th left derived functor $\text{Tor}_i(B, M) = 0$ for all sufficiently large $i$. Then we can define a map

$$
\begin{array}{c} K _ {0} \operatorname{Modf} A \longrightarrow K _ {0} \operatorname{Modf} B \\ M \longmapsto \sum_ {q \geq 0} (- 1) ^ {q} [ \operatorname{Tor} _ {i} ^ {A} (B, M) ]. \end{array}
$$

For higher K-groups, introduce a filtration

$$
F _ {0} \mathcal {M} _ {A} \subset \dots \subset F _ {p} \mathcal {M} _ {A} \subset \dots \subset \operatorname{Modf} A = \mathcal {M} _ {A},
$$

where  $M \in F_{p} M_{A}$  if and only if  $\operatorname{Tor}_{i}^{A}(B, M) = 0$  for i > p. Then

$$
M \mapsto \operatorname{Tor} _ {0} = B \otimes_ {A} M
$$

is exact from $F_{0}\mathcal{M}_{A}$ to $\mathcal{M}_B$ and so induces a map

$$
K _ {i} F _ {0} \mathcal {M} _ {A} \longrightarrow K _ {0} \mathcal {M} _ {B}.
$$

Now, we use the

Resolution Theorem Suppose we have a category closed under extensions

$$
0 \longrightarrow M ^ {\prime} \longrightarrow M \longrightarrow M ^ {\prime \prime} \longrightarrow 0.
$$

Then we have an induced exact sequence

$$
\dots \longrightarrow \operatorname{Tor} _ {p} ^ {A} (B, M ^ {\prime}) \longrightarrow \operatorname{Tor} _ {p} ^ {A} (B, M) \longrightarrow \operatorname{Tor} _ {p} ^ {A} (B, M ^ {\prime \prime}) \longrightarrow \operatorname{Tor} _ {p - 1} ^ {A} (B, M ^ {\prime}) \longrightarrow \dots .
$$

Moreover, if $M$ in a subcategory implies that $M'$ is also in the subcategory, then we find

$$
K _ {i} F _ {p - 1} \mathcal {M} _ {A} \cong K _ {i} F _ {p} \mathcal {M} _ {A}
$$

and get an induced map in higher K-groups.

Example of Localization Theorem Let $\mathbb{Q}$ be the quotient field of $\mathbb{Z}$. Then we have the exact sequence

$$
\mathcal {T} = \text { finitely   generated   torsion } \mathbb {Z} \text {-modules } \longrightarrow \mathcal {M} _ {\mathbb {Z}} \longrightarrow \mathcal {M} _ {\mathbb {Q}},
$$

and

$K_{*} \mathcal{M}_{\mathbb{Z}} = K_{*} \mathbb{Z}$ since $\mathbb{Z}$ is regular by the Resolution Theorem

and similarly for  $K_{*}$  Q.

Now

$$
\mathcal {T} = \prod_ {p} \mathcal {T} _ {p},
$$

where the product is over primes p and  $T_{p}$  denotes the p-torsion finite abelian groups, whence

$$
K _ {*} \mathcal {T} = \bigoplus_ {p} K _ {*} \mathcal {T} _ {p}.
$$

Use Devissage to get

$$
K _ {*} \operatorname{Modf} (\mathbb {Z} / p \mathbb {Z}) \approx K _ {*} T _ {p},
$$

whence from localization

$$
\dots \longrightarrow \bigoplus_ {p} K _ {i} \mathbb {Z} / p \longrightarrow K _ {i} \mathbb {Z} \longrightarrow K _ {i} \mathbb {Q} \longrightarrow \bigoplus_ {p} K _ {i - 1} \mathbb {Z} / p \longrightarrow \dots .
$$

There is an obvious generalization

$$
\dots \longrightarrow \bigoplus_ {m} K _ {i} A / m \longrightarrow K _ {i} A \longrightarrow K _ {i} F \longrightarrow \bigoplus_ {m} K _ {i - 1} A / m \longrightarrow \dots
$$

to a Dedekind domain A with quotient field F.

Facts:

[Quillen]

$$
K _ {i} (\mathbb {F} _ {q}) = \left\{ \begin{array}{c c} \mathbb {Z}, & i = 0, \\ \mathbb {F} _ {q} ^ {*} \cong \mathbb {Z} / (q - 1), & i = 1, \\ 0, & i \text {even}, \\ \mathbb {Z} / (q ^ {j} - 1), & i = 2 j - 1, \text {for} j \geq 1. \end{array} \right.
$$

Suppose A is the ring of integers in a number field F with  $r_{1}$  real places and  $r_{2}$  complex places. Then

[Borel]

$$
\text { rank } K _ {i} A = \left\{ \begin{array}{c c} 1, & i = 0, \\ r _ {1} + r _ {2} - 1, & i = 1, \\ 0, & i = \text { even }, \\ r _ {2}, & i = 3, 7, 1 1, 1 5, \dots , \\ r _ {1} + r _ {2}, & i = 5, 9, 1 3, \dots . \end{array} \right.
$$

A general fact [Bass] is that $K_{1}A = A^{*}$ for integers in number fields.

From [Quillen], we get

$$
K_{i}(\overline{\mathbb{F}}_{p}) = \left\{ \begin{array}{ll}\mathbb{Z}, & i = 0,\\ 0, & i\equiv 0(2),\\ \bigoplus_{\substack{i\neq p\\ \text{prime}}}\mathbb{Q}_{\ell} / \mathbb{Z}_{\ell}, & i\text{odd}, \end{array} \right.
$$

and in fact  $Q_{\ell}/Z_{\ell}=\bigcup_{n\geq0}Z/\ell^{n}Z$ .

Example Suppose $k = \overline{\mathbb{F}}_p$ and let $X$ be a complete non singular curve over $k$. We have

$$
\begin{array}{c c} k [ T ^ {- 1} ] \subset A _ {-} \\ \cap & \cap \\ k (T) \subset F \\ \cup & \cup \\ k [ T ] \subset A _ {+} \end{array}
$$

where  $A_{\pm}$  is the integral closure of  $k[T^{\pm1}]$  in F, and we set  $B = A_{+}A_{-} \subset F$ .

Then $X = \operatorname{Spec} A_{+} \cup \operatorname{Spec} A_{-}$ is a finite ramified cover of $\mathbb{P}_1(k)$, and we have $\mathcal{P}_X = (P_+, P_-, \alpha)$, for $P_{\pm} \in \mathcal{P}_{A_{\pm}}$, where $\alpha$ an isomorphism of $P_{+} \otimes B$ with $P_{-} \otimes B$.

This is like a Dedekind domain where we have the following “localization”

$$
\dots \longrightarrow \bigoplus_ {\substack {\text {closed points} \\ x \text {in} X}} K _ {i} k (x) \longrightarrow K _ {i} X \longrightarrow K _ {i} F \longrightarrow \dots ,
$$

and note that $k(x) \cong \overline{\mathbb{F}}_p$ because $k$ is algebraically closed.

Take

D = the group of divisors on curve
= free abelian group on closed points,

whence

$$
\bigoplus_ {x \in X} K _ {i} (k) = D \bigotimes_ {\mathbb {Z}} K _ {i} (k).
$$

This gives

$$
\dots \longrightarrow D \otimes K _ {i} k \longrightarrow K _ {i} X \longrightarrow K _ {i} F \longrightarrow D \otimes K _ {i - 1} k \longrightarrow \dots ,
$$

ending

$$
\begin{array}{c} K _ {1} F \longrightarrow D \otimes K _ {0} k \longrightarrow K _ {0} X \longrightarrow K _ {0} F \longrightarrow 0 \\ \Big \| \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ F ^ {*} \longrightarrow D \end{array}
$$

with this bottom map associating to F its divisor

$$
D = \mathbb {Z} \bigoplus D _ {0}
$$

of zeros and poles, where  $D_{0}$  are divisors with total degree zero and the summand Z captures the degree. Let J be the Jacobian of the curve. Then it is well-known that  $D_{0}/Im F^{*} = J$ , and so

$$
K _ {0} X = \underset {\text { rank }} {\mathbb {Z}} \bigoplus \underset {\text { degree }} {\mathbb {Z}} \bigoplus J.
$$

Note that $J$ is divisible.

# Chapter 38 The Plus Construction, $K_{1}$ and $K_{2}$

An acyclic map $f:X\to Y$ is one so that either of the following two equivalent conditions holds

(i) the homotopy fiber of f is acyclic,

(ii) for all local coefficient systems L, we have  $H_{*}(X, f^{-1}L) \simeq H_{*}(Y, L)$ .

Theorem Given X and a perfect normal subgroup N of  $\pi_{1}X$ , there is a unique acyclic map  $f: X \to Y$  with kernel N. Also, there is the following universal property in the homotopy category

![](images/page_10_image_5.jpg)

with a unique h making the diagram commute if and only if  $N < Ker \pi_{1} g$ .

Recall that the set of acyclic maps is closed under push out and pull back.

Take $X = BGL(A)$ and so $\pi_1 X = GL(A)$ with $\pi_q X = 0$ for all $q \geq 2$. Take $N = E(A)$, which is perfect and the commutator subgroup by Whitehead. Denote the unique acyclic map $f: X \to Y$ with $\operatorname{Ker} \pi_1 f = E(A)$ by

$$
f: B G L (A) \longrightarrow B G L (A) ^ {+}.
$$

Review of $K_{1}A$ [Bass] and $K_{2}A$ [Milnor], see Milnor's book:

According to Bass, $K_{1}$ is

$$
K _ {1} A \stackrel {{d}} {{=}} G L (A) ^ {a b} = G L (A) / E (A) = \pi_ {1} (B G L A ^ {+}).
$$

One way of defining Milnor's $K_{2}$ is

$$
\begin{array}{c} K _ {2} A \stackrel {{d}} {{=}} H _ {2} (E (A), \mathbb {Z}) \\ = H _ {2} (B E A, \mathbb {Z}). \end{array}
$$

Meanwhile we have the pull back

$$
\begin{array}{c} B E A = \overline {{B G L A}} \xrightarrow {\text {   acyclic   }} \widetilde {B G L A ^ {+}} \\ \Bigg \downarrow \\ B G L A \xrightarrow {} B G L A ^ {+} \end{array}
$$

and

$$
\begin{array}{r l} \pi_ {2} B G L A ^ {+} & = \pi_ {2} \widetilde {B G L A ^ {+}} \\ & = H _ {2} \widetilde {B G L A ^ {+}}, \text { by   Hurewicz } \\ & = H _ {2} \overline {{B G L A}} \\ & = H _ {2} B E A. \end{array}
$$

Note that  $\Omega BQ P_{A} = K_{0} A \times BGLA^{+}$ .

The Schur multiplier and the universal central extension of a perfect group Recall from day one that  $H^{2}(G, M)$  is the collection of extensions

$$
* \longrightarrow M \longrightarrow E \longrightarrow G \longrightarrow *
$$

of $G$ by $M$, and the extension is central if and only if $G$ acts trivially on $M$. If $M$ is a trivial $G$-module, then we have a Universal Coefficient Theorem

$$
0 \longrightarrow \operatorname{Ext} ^ {1} \left(H _ {1} G, M\right) \longrightarrow H ^ {2} (G, M) \longrightarrow \operatorname{Hom} \left(H _ {2} G, M\right) \longrightarrow 0,
$$

and G perfect implies Ext = 0, so

$$
H ^ {2} (G, M) = \operatorname{Hom} (H _ {2} G, M).
$$

Translation: there exists a canonical central extension $\xi \in H^{2}(G, H_{2}G)$ so that any other extension is induced by a unique map from $H_{2}G$ to $M$:

$$
\begin{array}{c} \xi : \\ * \longrightarrow H _ {2} G \longrightarrow \widetilde {G} \longrightarrow G \longrightarrow * \\ * \longrightarrow M \longrightarrow E \longrightarrow G \longrightarrow * \end{array}
$$

For $G$ perfect,

$\widetilde{G}$ is the universal central extension of $G$, and

$H_{2}$  G is the Schur multiplier of G,

and in particular for EA,

$\widetilde{EA}$ is the Steinberg group, and

$$
H _ {2} E A = \operatorname{Ker} \{\widetilde {E A} \longrightarrow E A \} = K _ {2} A.
$$

EA is generated by  $I + a E_{ij} = e_{ij}(a)$ , and the commutators are

$[e_{ij}a, e_{jk}b] = e_{ik}(ab)$, for $i, j, k$ pairwise distinct.

In fact, Milnor uses this to show  $K_{2}(\mathbb{F}_{q}) = 0$ .

Exercise $\pi_3(BGLA^+) = H_3(\widetilde{EA},\mathbb{Z})$

BGLA is not an H-space since  $\pi_{1}$  is not abelian. Put  $N = \{1, 2, \ldots\}$  and let  $\theta : N \hookrightarrow N$  be any embedding. Then  $\theta$  induces a map  $GLA \to GLA$  given by

$$
\alpha_ {i j} \mapsto \left\{ \begin{array}{l l} \delta_ {i j}, & \text { if   } i \text {   or   } j \notin \operatorname{Im} \theta , \\ \alpha_ {\theta^ {- 1} (i) \theta^ {- 1} (j)}, & \text { else }, \end{array} \right.
$$

which for instance simply shifts  $\alpha$  diagonally  $\alpha\mapsto\begin{pmatrix}1&0\\0&\alpha\end{pmatrix}$  in case  $\theta(n)=n+1$ .

We get

![](images/page_12_image_14.jpg)

and have

Lemma $\theta \simeq \mathrm{id}$.

Proof

Step 1: Show the homotopy equivalence. We have

$$
\begin{array}{c} G L _ {n} A \longrightarrow G L A \\ \Biggl \downarrow_ {\theta} \\ G L A \end{array}
$$

and there exists an $\alpha \in EA$ so that conjugation by $\alpha$ and the map $\theta$ have the same effect on $GL_{n}A$. Thus the diagram

![](images/page_13_image_0.jpg)

commutes because conjugation acts trivially. So $\theta_{*}$ acts identically with the same argument showing that $\theta_{*} = \mathrm{id}$ on $H_{*}(GLA, M)$ for $M$ any (GLA/EA)-module, and meanwhile

$$
H _ {*} (G L A, M) = H _ {*} (B G L A, M) = H _ {*} (B G L A ^ {+}, M).
$$

It follows that  $\theta$  induces an isomorphism on  $BGLA^{+}$  for all kinds of homology, and so it is a homotopy equivalence.

Step 2 (Exercise) Any self-homomorphism of the monoid $M$ of all embeddings $\theta : \mathbb{N} \to \mathbb{N}$ is trivial.

This proves the lemma.

Proposition BGLA $^{+}$ is a homotopy commutative associative H-space.

Proof Choose $\mathbb{N} \coprod \mathbb{N} \hookrightarrow \mathbb{N}$. This gives a homomorphism $GLA \times GLA \to GLA$ and hence a map $B(GLA \times GLA)^{+} \to BGLA^{+}$. But

$$
B (G L A \times G L A) ^ {+} = (B G L A \times B G L A) ^ {+} = B G L A ^ {+} \times B G L A ^ {+},
$$

which gives a product. The previous lemma shows independence of the choice of $\mathbb{N}\coprod\mathbb{N}\hookrightarrow\mathbb{N}$. Also, the restriction of the product to both of $*\times BGLA^{+}$ and $BGLA^{+}\times *$ are homotopic to the identity by the lemma again. We thus have an $H$-space.

Example For  $F = \overline{F}_{p}$ , compute  $\pi_{*} BGLF^{+} = K_{*} F$ .

To this end, following [R. Brauer], construct a map $BG \to BU$ using character theory starting from a representation of a finite group $G$ over $F$. Namely, suppose given $G \xrightarrow{\rho} GL_n F$. Then choose an embedding

$$
F ^ {*} \subset \{\text { roots   of   unity } \} \subset \mathbb {C},
$$

where $F^{*} = \coprod_{\ell \neq p}\mathbb{Q}_{\ell} / \mathbb{Z}_{\ell}$. Define the Brauer character $\chi$ to be

$\chi(\rho)(g) = \text{the sum of the eigenvalues of } \rho(g) \text{ in } \mathbb{C}^*.$

Theorem (Brauer) $\chi(\rho)$ is the character of a virtual representation of $G$ over $\mathbb{C}$, that is

$$
\chi (\rho) = \chi V _ {1} - \chi V _ {2}.
$$

We get $BGLF \to BU$ hence $BGLF^{+} \to BU$ since $BU$ is simply connected, and this is almost a homology equivalence.

## \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

As noted in the Foreword, the class and the notes ended abruptly and embarrassedly here with this vague remark on homology equivalence owing to the end of class time, which Quillen always meticulously respected. The precise statement proved in Quillen's 1972 paper [9] is that this map lifts to the homotopy fiber of $\Psi^q - 1$, where $\Psi$ is an Adams operation, and this lift is almost a homotopy equivalence.

# Afterword by Mikhail Karpranov

This volume contains the notes of a course given by Daniel Quillen at MIT in 1979/80, almost 40 years ago. The goal of the course was to provide an introduction to Quillen's fundamental work on higher algebraic K-theory. It begins from scratch, making very minimal requirements on the mathematical background of the participants (only an elementary knowledge of groups, rings etc. is assumed), and in the space of 38 lectures brings them to the subject matter of Quillen's original work. Among the subjects covered are:

\- Group cohomology.

• Homological algebra. Derived categories.

\- Simplicial sets and simplicial homotopy theory.

\- Homotopy theory of categories via classifying spaces.

\- Higher K-theory via Quillen's Q-construction.

\- Sketches of relations to other techniques:

\- Tits complexes (used in Quillen's proof of the finite generation of K-groups for algebraic integers and curves over finite fields).

\- The definition of higher K-groups via the Plus construction.

Most of this material is available in modern textbooks and in Quillen's original and excellently written papers [9–11]. For further study the reader will definitely need to master these as well. Among the standard modern references on homological algebra one can name the books of Gelfand–Manin [2] and Weibel [15] as well as the classic [1] of Cartan–Eilenberg. The basics of simplicial homotopy theory can also be found in Gelfand–Manin [2] and a more systematic treatment in the book of Goerss–Jardine [3]. The books of Srinivas [13] and Weibel [16] provide systematic treatments of various approaches to higher K-theory.

The present volume gives a shortened overview of the subject which may be useful and less intimidating for the beginner than a more fundamental course of reading which can come later.

Comparison of modern treatments shows how difficult it is to improve on Quillen. The sheer perfection of his work is almost frightening. As far as the foundations of

K-theory go, one important later development is the S-construction of Segal and Waldhausen [14, 16] which can be viewed as a somewhat more flexible analog of the Q-construction, applicable to a wider class of categories. Quillen famously expressed hope [10] that the techniques around his theorems A and B will some day be incorporated into a general homotopy theory for toposes. One can see Lurie's theory of $\infty$-categories and $\infty$-toposes [7] as a confirmation of this hope.

These notes, with their informal style, provide a direct window into the way of operation of a great mind. Their preservation, owing to the effort of Robert Penner, will be very much appreciated by the readers.

1. H. Cartan, S. Eilenberg, Homological Algebra (Princeton University Press, Princeton, 1956)

2. S.I. Gelfand, Y.I. Manin, Methods of Homological Algebra (Springer, Berlin, 1997)

3. P.G. Goerss, J.F. Jardine, Simplicial Homotopy Theory (Birkhäuser, Basel, 1999)

4. D. Grayson, Higher algebraic K-theory II (after Daniel Quillen). Lecture Notes in Mathematics, vol. 551 (Springer, Berlin, 1976), pp. 217–240

5. D. Grayson, Finite generation of K-groups of a curve over a finite field (after Daniel Quillen), vol. 966, Lecture Notes in Mathematics (Springer, Berlin, 1982), pp. 69–90

6. A. Grothendieck, J.-L. Verdier, Préfaisceaux (SGA4 Éxp. 1), Lecture Notes in Mathematics, vol. 269 (Springer, Berlin, 1972), pp. 17–233

7. J. Lurie, Higher Topos Theory (Princeton University Press, Princeton, 2009)

8. J. Milnor, Introduction to Algebraic K-Theory, Annals of Mathematics Studies, vol. 72 (Princeton University Press, Princeton, 1971)

9. D. Quillen, On the cohomology and K-theory of the general linear groups over a finite field. Ann. Math. 96, 552–586 (1972)

10. D. Quillen, Algebraic K-theory I, vol. 341, Lecture Notes in Mathematics (Springer, Berlin, 1973), pp. 85–147

11. D. Quillen, Finite generation of the groups  $K_{i}$  of rings of algebraic integers, vol. 341, Lecture Notes in Mathematics (Springer, Berlin, 1973), pp. 179–198

12. J.-P. Serre, Local Fields (Springer, Berlin, 1979)

13. V. Srinivas, Algebraic K-Theory (Birkäuser, Basel, 1996)

14. F. Waldhausen, Algebraic K-theory of generalized free products. Ann. Math. 108, 135–204 (1978)

15. C.A. Weibel, Introduction to Homological Algebra (Cambridge University Press, Cambridge, 1994)

16. C.A. Weibel, The K-book: An Introduction to Algebraic K-theory (American Mathematical Society Publishing, Providence, 2013)

## A

Abelian category, 51, 55  
Acyclic map, 201  
Additive category, 54  
Additive functor, 23  
Additive non-abelian category, 57  
Adjoint functors, 43  
Adjunction formula, 127  
Admissible layer, 172  
Admissible morphism, 144  
Arrow, 6  
Axioms for simplicial objects, 10

## B

Bi-simplicial set, 179  
Burnside ring, 103

## C

Cartesian morphism, 63  
Category, 6  
Category object, 156  
Classifying space, 156  
1-coboundary, 6  
2-cocycle, 3  
Co-chain complex, 4  
Cofibered category, 64  
Cogroup structure, 52  
Cohomology of cyclic groups, 28  
Cohomology of free groups, 22  
Cokernel, 54  
Complex in abelian category, 72  
Conical contractibility, 17  
Conical contraction, 170  
Connecting homomorphism, 23

Contractibility, 169  
Crossed homomorphism, 5

## D

$\delta$ -functor, 23  
Derivation, 5, 22  
Derived category, 91  
Devissage Theorem, 106  
Direct limit, 42  
Direct sum, 42  
Discrete category, 47, 69  
Dold-Thom Theorem, 182

## E

Effaceable functor, 21  
Equalizer, 41  
Exact category, 143  
Exact sequence of $K$-groups, 191

## F

Fiber, 47  
Fibered category, 63  
Final object, 40  
First homotopy property, 95  
Full subcategory, 73  
Functor, 7

## G

Generalized Kan formula, 134  
Geometric realization, 155  
Grothendieck group, 102  
Group completion, 101

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">© Springer Nature Switzerland AG 2020<br>R. Penner, Topology and K-Theory, Lecture Notes in Mathematics 2262, https://doi.org/10.1007/978-3-030-43996-5</span></small>

Group extension, 1  
Groupoid, 7  
G-set, 41

## H

Higher K-groups, 161
Hochschild–Serre spectral sequence, 140
Homology groups with coefficients in a module, 13
Homology of category with values in a functor, 12
Homology of cyclic groups, 27
Homology of simplicial complex, 16
Homotopy between functors, 72
Homotopy equivalence, 169
Hyper-homology spectral sequence, 126

## I

Increasing filtration, 123  
Initial object, 40  
Injective object, 71

## K

Kan formula, 47  
Kernel, 55

## L

Layer, 170  
Left-derived functor, 91  
Left-fiber, 47  
Leray spectral sequence, 133  
Localization, 101  
Localization Theorem, 191

## M

Mackey formula, 35  
Mapping cone, 87  
Mapping cylinder, 85  
Modules, 2  
Monoid, 6  
Morphisms, 6

## N

Nerve of a category, 7  
Nerve of topological category, 156  
Normalization Theorem, 15

O Objects, 6

## P

Plus construction, 201  
Poset, 6  
Postnikov filtration, 123  
Pre-cofibered category, 64  
Pre-fibered category, 63  
Projective object, 71  
Projective resolution, 73  
Puppe sequence, 111

## Q

Quasi-fibration, 182  
Quasi-isomorphism, 72  
Quis, 72

## R

Representable functor, 40  
Resolution of a complex, 73  
Resolution Theorem, 107, 144, 196  
Right fiber, 47

## s

Schreier Lemma, 106  
Schur multiplier, 203  
Schur-Zassenhaus Theorem, 36  
Second cohomology group, 4  
Section, 3  
Semi-simplicial space, 155  
Serpent Lemma, 59  
Simplex in a category, 7  
Simplicial abelian group, 10  
Simplicial object, 9  
Simplicial set, 7  
Small category, 6  
Spectral sequence, 115  
Split extension, 22  
s.s., 155  
Steinberg group, 203  
Steinberg module, 177

## T

Theorem A, 189  
Theorem B, 191  
Thick subcategory, 147  
Tits building, 177  
Tits complex, 187

Topological category, 156

Transfer map, 33

Y

Yoneda Lemma, 39

## U

Universal central extension, 203