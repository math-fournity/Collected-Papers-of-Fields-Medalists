# Projective manifolds with ample tangent bundles

By SHIGEFUMI MORI\*

## 0. Introduction

Our main purpose is to prove Hartshorne's conjecture [5]:

THEOREM 8 (H$_{n}$). Every irreducible n-dimensional non-singular projective variety with ample tangent bundle defined over an algebraically closed field k of characteristic $\geq 0$ is isomorphic to the projective space P$_{k}^{n}$.

In the case $k = \mathbf{C}$ (the field of complex numbers), it is known that the positivity of sectional curvature implies the ampleness of tangent bundle [6, §8]. Thus Theorem 8 proves Frankel's conjecture [1] in complex differential geometry:

$(F_{n})$ Every $n$-dimensional compact Kähler manifold with positive sectional curvature is biholomorphic to the projective space $P_{c}^{n}$.

These conjectures for  $n \leq 3$  have been proved by earlier works: They are obvious if n = 1.  $H_{2}$  was proved by R. Hartshorne [5], and  $F_{2}$  by T. T. Frankel and A. Andreotti [1]. As for n = 3, T. Mabuchi [7] proved  $H_{3}$  in characteristic 0 under the assumption that the second Betti number is 1, which implies  $F_{3}$ . Later on, the assumption on the second Betti number was removed and an alternate proof for n = 3, char k = 0 was given by H. Sumihiro and myself [8].

Here is the outline of the proof of Theorem 8. For a projective manifold $X$ with ample tangent bundle, we show that $X$ contains a rational curve (Theorem 6 in §2) and study the rational curves with minimal degree (Corollary 7 in §2). Let $P$ be a point in $X$. A slight modification $Z$ of a maximal connected family of rational curves with minimal degree passing through $P$ is parametrized in a $1 - 1$ way by $\mathbf{P}^{n-1}$ ((8.1) in §3). The family $Z$ which is thus a $\mathbf{P}^1$-bundle over $\mathbf{P}^{n-1}$ dominates $X$, and the morphism $Z \to X$ is studied ((8.2) in §3). Then easy arguments show that $X \simeq \mathbf{P}_k^n$ (§3). In Section 1, we prove a result (Proposition 3) essential to our whole proof,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">0003-486X/79/0110-3/0593/014 \$ 00.70/1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">© 1979 by Princeton University Mathematics Department</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">For copying information, see inside back cover.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* Partially supported by the Sakkokai Foundation and NSF Grant No. MCS 73-08412.</span></small>

which is an analogue to Theorem (2.3.3) of Mumford in [12]. Section 4 is devoted to the proof of the existence of a projective variety $Y$ parametrizing the family $Z$.

The only properties of the ampleness of $T_{X}$ which are used here are: (i) the anticanonical line bundle $\wedge^{n}T_{X}$ is ample, and (ii) for any non-constant map from $\mathbf{P}^1$ to $X$, the pull-back of $T_{X}$ to $\mathbf{P}^1$ is a sum of ample line bundles. For a general vector bundle, these properties are far weaker than ampleness, so our theorem is stronger than stated.

The author expresses his sincere thanks to Professors H. Hironaka and H. Sumihiro who gave him useful advice and encouragement.

After submitting the paper, the author succeeded in removing the assumption of positive characteristic in Theorem 5. So we have the stronger version of the existence theorem of the rational curve in arbitrary characteristic. The proof will be published elsewhere in the near future.

## Notation and conventions

The words Cartier divisors, invertible sheaves, and line bundles are used interchangeably, and locally free sheaves and vector bundles, too. We use the notation and the language of [2], and thus, vector bundle  $\mathbf{V}(E)$  and projective bundle  $\mathbf{P}(E)$  are used in the sense of [2] for a locally free sheaf E on a scheme X.

For a scheme $X$ and a closed point $x$ of $X$,

$$
\dim_ {x} X = \text {   the   dimension   of   } X \text {   at   } x, \text {   and   }
$$

$$
T _ {x, X} = \text {   the   Zariski   tangent   space   to   } X \text {   at   } x.
$$

For a morphism $X \to Y$ of finite type,

$T_{X / Y} =$ the relative tangent bundle if $X$ is smooth over $Y$,

$K_{X / Y} =$ the dual of the determinant bundle of $T_{X / Y}$, i.e., the relative canonical bundle

$(T_{X / Y}$ and $K_{X / Y}$ may be written as $T_{X}$ and $K_{X}$, respectively if $Y = \operatorname{Spec} k$, where $k$ is a field),

$X_{R} = X \times_{Y} R$ (or $X \times_{Y} \operatorname{Spec} R$) for $Y$-schemes $R$ (or $\operatorname{Spec} R$), and

$X(R) =$ the set of $R$-valued points for $Y$-schemes $R$ (or $\operatorname{Spec} R$).

For a scheme $X$ proper over a field $k$,

$H^{i}(X,F) =$ the $i^{\mathrm{th}}$ cohomology group for a coherent sheaf $F$ on $X$,

$$
\begin{array}{c} h ^ {i} (X, F) = \dim_ {k} H ^ {i} (X, F), \text {   i.e.,   the   dimension   of   the   vector   space } \\ H ^ {i} (X, F), \end{array}
$$

$$
\chi (X, F) = \Sigma_ {i} (- 1) ^ {i} h ^ {i} (X, F),
$$

$$
P _ {a} (X) = 1 - \chi (X, \mathcal {O} _ {X}) \text {   for   a   curve   } X,
$$

and if $X$ is smooth and irreducible,

$Y \cdot Z =$ the intersection product of cycles $Y$ and $Z$ of $X$ intersecting properly, and

$(Y \cdot Z) =$ the intersection number of cycles $Y$ and $Z$ of $X$ such that $\dim Y + \dim Z = \dim X$.

## 1. Preliminaries on deformation of morphisms

Let $X$ and $Y$ be schemes of finite type over a Noetherian scheme $S$, and $Z$ a closed subscheme of $X$. Let $p: Z \to Y$ be an $S$-morphism. Now let

$$
\operatorname{Hom} _ {s} (X, Y; p) \colon (L N S c h / S) ^ {\circ} \longrightarrow (\text { Sets })
$$

be the contravariant functor from the category of locally Noetherian S-schemes to the category of sets, defined by

$$
\operatorname{Hom} _ {S} (X, Y; p) (T) = \{f: X _ {T} \longrightarrow Y _ {T} | f \text {   is   a   } T \text {-morphism   and   } f | _ {Z _ {T}} = p _ {T} \}
$$

for $T \in (LNSch / S)$. Then

PROPOSITION 1. If $X$ and $Z$ are projective and flat over $S$ and if $Y$ is quasi-projective over $S$, then $\operatorname{Hom}_S(X, Y; p)$ is represented by a closed subscheme of $\operatorname{Hom}_S(X, Y)$ (cf. [3, n°221]).

Proof. Consider the restriction morphism res: $\operatorname{Hom}_s(X, Y) \to \operatorname{Hom}_s(Z, Y)$, and a section $[p]: S \to \operatorname{Hom}_s(Z, Y)$ induced by $p$. Since $[p]$ is a closed immersion, the fiber product of res and $[p]$ over $\operatorname{Hom}_s(Z, Y)$ gives us the closed immersion $\operatorname{Hom}_s(X, Y; p) \to \operatorname{Hom}_s(X, Y)$. q.e.d.

Infinitesimal properties of $\operatorname{Hom}_s(X, Y; p)$ are studied similarly to those of $\operatorname{Hom}_s(X, Y)$.

PROPOSITION 2. Assume that $Z$ is flat over $S$, and that $Y$ is smooth over $S$. Let $\bar{T} = \operatorname{Spec}(A / I) \subset T = \operatorname{Spec} A$ be $S$-schemes with $I^2 = 0$, and $\bar{f} \in \operatorname{Hom}_S(X, Y; p)(\bar{T})$. Then the obstruction to extending $\bar{f}$ to $X_T \to Y_T$ lies in $H^1(X_{\bar{T}}, G)$, where

$$
G = \bar {f} * \left((T _ {Y / S}) _ {\overline {{T}}}\right) \otimes_ {\mathcal {O} _ {X \overline {{T}}}} (I _ {z}) _ {\overline {{T}}} \otimes_ {\mathcal {O} \overline {{T}}} I,
$$

$I_{z} \subset \mathfrak{O}_{x}$ is the sheaf of the defining ideal of $Z$ in $X$. If $\bar{f}$ is extendable, any $f \in \operatorname{Hom}_{s}(X, Y; p)(T)$ extending $\bar{f}$ gives a bijection

$$
\ell (f) \colon H ^ {0} (X _ {\overline {{{T}}}}, G) \longrightarrow \operatorname{Hom} _ {S} (X, Y; p) _ {\bar {f}} (T),
$$

where $\operatorname{Hom}_S(X, Y; p)_{\bar{f}}(T) = \{f \in \operatorname{Hom}_S(X, Y; p) | f_{\bar{T}} = \bar{f}\}$.

If we forget the base condition $f|_{z} = p$, this is contained in [4, Exposé III, Corollaire 5.2]. The proposition is proved in the same way. We will give the proof for the readers' convenience, assuming the separatedness of $X$ over $S$, which is enough for later use.

Proof. First, we consider the case where $X$ is affine over $S$. By the above remark, $\operatorname{Hom}_S(X, Y)_{\bar{f}}(T) \neq \emptyset$. In order to prove the first assertion, it is enough to show the restriction map $\operatorname{Hom}_S(X, Y)_{\bar{f}}(T) \to \operatorname{Hom}_S(Z, Y)_{\bar{f}}(T)$ is surjective. Again by the above remark, this is reduced to the surjectivity of

$$
H ^ {0} \left(X _ {\bar {T}}, \bar {f} * \left(\left(T _ {Y / S}\right) _ {\bar {T}}\right) \otimes_ {\mathcal {O} \bar {T}} I\right) \longrightarrow H ^ {0} \left(Z _ {\bar {T}}, \bar {f} * \left(\left(T _ {Y / S}\right) _ {\bar {T}}\right) \otimes \mathcal {O} _ {Z _ {\bar {T}}} \otimes_ {\mathcal {O} \bar {T}} I\right),
$$

which is obvious since $X_{\overline{T}}$ is affine. The second assertion follows from the exact sequence (Z is flat over S),

$$
0 \longrightarrow G \longrightarrow \bar {f} * \left((T _ {Y / S}) _ {\overline {{T}}}\right) \otimes_ {\mathcal {O} \overline {{T}}} I \longrightarrow [ \bar {f} * \left((T _ {Y / S}) _ {\overline {{T}}} | _ {Z _ {\overline {{T}}}}\right) ] \otimes_ {\mathcal {O} \overline {{T}}} I \longrightarrow 0,
$$

since  $X_{\overline{T}}$  is affine. Now considering a general X, we will cover X with affine open sets  $U_{i} (i = 1, \cdots, n)$ . The second assertion follows immediately from the second assertion for  $\operatorname{Hom}_{S}(U_{i}, Y; p|_{U_{i}})$ . We have an exact sequence of functors

$$
\operatorname{Hom} _ {S} (X, Y; p) \longrightarrow \prod_ {i} \operatorname{Hom} _ {S} (U _ {i}, Y; p | _ {U _ {i}}) \xrightarrow [ \beta ]{\alpha} \prod_ {i j} \operatorname{Hom} _ {S} (U _ {i} \cap U _ {j}, Y; p | _ {U _ {i} \cap U _ {j}})
$$

with naturally induced mappings. By the above results for the affine case, we take  $f_{i} \in \operatorname{Hom}_{S}(U_{i}, Y; p|_{U_{i}})(T)$  extending  $\bar{f}|_{U_{i}} (i = 1, \cdots, n)$ . By definition,

$$
\alpha (\prod f _ {i}) _ {i, j} = f _ {i} | _ {(U _ {i} \cap U _ {j}) _ {T}} \quad \text { and } \quad \beta (\prod f _ {i}) _ {i, j} = f _ {j} | _ {(U _ {i} \cap U _ {j}) _ {T}}.
$$

By the results for the affine case, we set

$$
\dot {\varphi} _ {i, j} = \ell (f _ {j} | _ {(U _ {i} \cap U _ {j}) _ {T}}) ^ {- 1} (f _ {i} | _ {(U _ {i} \cap U _ {j}) _ {T}}) \in G ((U _ {i} \cap U _ {j}) _ {\overline {{T}}}).
$$

Actually, this means that ${}^t f_i$ and ${}^t f_j$, the associated $\mathcal{O}_s$-algebra homomorphisms $\mathcal{O}_Y \to \mathcal{O}_{(U_i) \cup U_j)_T}$, have the relation

$$
{ } ^ { t } f _ { i } | _ { ( U _ { i } \cap U _ { j } ) \overline { { T } } } = { } ^ { t } f _ { j } | _ { ( U _ { i } \cap U _ { j } ) \overline { { T } } } + \dot { \phi } _ { i , j } .
$$

Since we have

$$
\dot {\phi} _ {i, i} = 0, \quad \dot {\phi} _ {i, j} = - \dot {\phi} _ {j, i}, \quad \text { and } \quad \dot {\phi} _ {i, j} + \dot {\phi} _ {j, k} + \phi_ {k, i} = 0
$$

on  $(U_{i} \cap U_{j} \cap U_{k})_{\overline{T}}$ ,  $\{\phi_{i,j}\}$  gives a cocycle in  $Z^{1}(\mathfrak{U}, G)$ , where  $\mathfrak{U} = \{(U_{1})_{\overline{T}}, \cdots, (U_{n})_{\overline{T}}\}$ . Its class  $\phi \in \check{H}^{1}(\mathfrak{U}, G) = H^{1}(X_{\overline{T}}, G)$  does not depend on the choice of  $f_{i}$ . If  $\phi = 0$ , then there are  $D_{i} \in G((U_{i})_{\overline{T}})(i = 1, \cdots, n)$  such that

$$
\phi_ {i, j} = D _ {i} \left| _ {(U _ {i} \cap U _ {j}) \overline {{T}}} - D _ {j} \right| _ {(U _ {i} \cap U _ {j}) \overline {{T}}} \text {   for   any   } i \text {   and   } j.
$$

By considering

$$
\boldsymbol {g} _ {i} = \ell (f _ {i} | _ {(U _ {i} \cap U _ {j}) _ {T}}) (- D _ {i}) \in \operatorname{Hom} _ {S} (U _ {i}, Y; p | _ {U _ {i}}) (T) \quad (i = 1, \dots , n),
$$

we see $\alpha (\prod g_i) = \beta (\prod g_i)$, and we can find an $f\in \mathrm{Hom}_S(X,Y;p)_{\bar{f}}(T)$.

q.e.d.

Suppose furthermore that $S = \operatorname{Spec} k$ ($k$ is an algebraically closed field), $X$ is projective over $S$, and $Y$ is quasi-projective over $S$. Let $[f]$ be a closed point of $\operatorname{Hom}_s(X, Y; p)$ corresponding to a morphism $f: X \to Y$. By Proposition 1, $\operatorname{Hom}_s(X, Y; p)$ can be considered as a scheme over $S$. Let $(R, N)$ be the completion of the local ring of $\operatorname{Hom}_s(X, Y; p)$ at $[f]$. We express $R$ as $A / I$, where $A$ is a formal power series ring over $k$ with maximal ideal $M$ such that $M / M^2 \simeq N / N^2$, i.e., $I \subset M^2$. Then

PROPOSITION 3.

$$
T _ {[ f ], \operatorname{Hom} _ {S} (X, Y; p)} \simeq H ^ {0} \left(X, f ^ {*} \left(T _ {Y ^ {\prime} K}\right) \otimes_ {\mathfrak {O} _ {X}} I _ {Z}\right),
$$

and $I$ is generated by at most $h^1(X, f^*(T_Y) \otimes I_Z)$ elements. Hence

$$
\dim_ {[ f ]} \operatorname{Hom} _ {S} (X, Y; p) \geq h ^ {0} \left(X, f ^ {*} \left(T _ {Y}\right) \otimes I _ {Z}\right) - h ^ {1} \left(X, f ^ {*} \left(T _ {Y}\right) \otimes I _ {Z}\right).
$$

Proof. The first assertion follows from Proposition 2 applied to $\bar{T} = \operatorname{Spec} k \subset T = \operatorname{Spec} k[t] / (t^2)$. Since the last assertion is an immediate corollary to the first two, we have only to prove that $I$ has a generators, where $a = h^{1}(X, f^{*}(T_{Y}) \otimes I_{Z})$. By the lemma of Artin-Rees, we take a sufficiently large $n$ such that

$$
\boldsymbol {I} \cap \boldsymbol {M} ^ {n} = \boldsymbol {M} (\boldsymbol {I} \cap \boldsymbol {M} ^ {n - 1}) \subset \boldsymbol {M I}.
$$

Let $J = I + M^n / MI + M^n \subset B = A / MI + M^n$. Then $J$ is an ideal of $B$ and $MJ = 0$. Corresponding to the natural map $R \to B / J = A / I + M^n$, there is a $B / J$-valued point $\bar{g}$ of $\operatorname{Hom}_s(X, Y; p)$. By Proposition 2, the obstruction to extend $\bar{g}$ to a $B$-valued point is given by $\phi \in H^1(X, f^*(T_Y) \otimes I_Z) \otimes_k J$, since $MJ = 0$ and $\bar{g}|_{X_{(B/J)}} = f$. Now $\phi = \sum_{i=1}^{a} \phi_i \otimes \bar{r}_i$ for a basis $\{\phi_i\}$ of $H^1(X, f^*(T_Y) \otimes I_Z)$ and $\bar{r}_i \in J (i = 1, \cdots, a)$. Let $\bar{r}_i = r_i$ modulo $MI + M^n$, where $r_i \in I + M^n (i = 1, \cdots, a)$. If we extend $\bar{g}$ to a $B / (\bar{r}_1, \cdots, \bar{r}_a)$-valued point, the obstruction is given by $\bar{\phi} = \text{the natural image of } \phi \in H^1(X, f^*(T_Y) \otimes I_Z) \otimes_k J / (\bar{r}_1, \cdots, \bar{r}_a)$ (see the proof of Proposition 2). Since $\phi = \sum \phi_i \otimes \bar{r}_i, \bar{\phi} = 0$, and thus we have a $k$-algebra homomorphism $\alpha$ which makes the diagram commutative.

$$
\begin{array}{l} A / I \xrightarrow {\text { nat. }} B / J = A / I + M ^ {n} \\ \Big \backslash_ {\alpha} \Big \downarrow \uparrow \text { nat. } \\ B / (\bar {r} _ {1}, \dots , \bar {r} _ {a}) = A / M I + M ^ {n} + (r _ {1}, \dots , r _ {a}). \end{array}
$$

Since $I \subset M^2$, $\alpha$ is surjective by the above diagram. Since $A$ is a formal

power series ring over $k$, there is a $k$-automorphism $\sigma$ of $A$ which makes the diagram commutative.

$$
\begin{array}{c} A / I \xrightarrow {\alpha} A / M I + M ^ {n} + (r _ {1}, \dots , r _ {a}) \\ \text { nat. } \Bigg | \quad \text { nat. } \Bigg | \\ A \xrightarrow {\sigma} A \end{array}
$$

From the two commutative diagrams, $r - \sigma(r) \in I + M^n$ for any $r \in A$. Considering $r \in \sigma^{-1}(I)$, we have $\sigma^{-1}(I) \subset I + M^n$. Operating $\sigma$, we have $I \subset \sigma(I) + M^n$ because $\sigma(M) = M$. Thus from the second diagram,

$$
\sigma (I) \subset M I + M ^ {n} + \left(r _ {1}, \dots , r _ {a}\right) \subset M \sigma (I) + M ^ {n} + \left(r _ {1}, \dots , r _ {a}\right).
$$

Since $\sigma$ is an automorphism, we have $\sigma(I) \cap M^n \subset M\sigma(I)$. Hence the images of $r_1, \cdots, r_a$ ($\in I + M^n \subset \sigma(I) + M^n$) generate

$$
\sigma (I) + M ^ {n} / M \sigma (I) + M ^ {n} \simeq \sigma (I) / M \sigma (I) + (\sigma (I) \cap M ^ {n}) \simeq \sigma (I) / M \sigma (I).
$$

Therefore, $I$ is generated by $a$ elements (Nakayama's lemma).

q.e.d.

## 2. The existence of rational curves

First we need to consider how to choose an appropriate one among the rational curves in a variety $X$ if there is one.

THEOREM 4. Let X be a non-singular projective variety of dimension n over an algebraically closed field k, and let C be a rational curve (which may be singular) in X. If  $(K_{X}^{-1} \cdot C) \geq n + 2$ , then the cycle C can be deformed to a cycle which is a sum of  $\nu$  rational curves (which may not be distinct) with  $\nu \geq 2$ .

Proof. Let $P$ and $Q$ be two smooth points $(P \neq Q)$ of $C$, and let $\phi: \mathbf{P}^1 \to C \subset X$ be a resolution such that $\phi(0) = P$ and $\phi(\infty) = Q$. Let $i = \phi|_{\{0, \infty\}}: \{0, \infty\} \to X$. Then $H = \operatorname{Hom}_k(\mathbf{P}^1, X; i)$ is of dimension $\geq 2$ at $[\phi]$ because the Riemann-Roch theorem shows

$$
\dim_ {[ \phi ]} H \geq \chi (\mathbf {P} ^ {1}, \phi^ {*} T _ {X} \otimes \mathcal {O} _ {P ^ {1}} (- 2)) = n + (K _ {X} ^ {- 1} \cdot C) - 2 n \geq 2,
$$

by Proposition 3. Since $\operatorname{Aut} \mathbf{P}_{0,\infty}^{1} = \{g \in \operatorname{Aut} \mathbf{P}^{1} | g(0) = 0, g(\infty) = \infty\}$ is $\mathbf{G}_m$, we can find a finite morphism $\alpha: D \to H$ such that $D$ is a non-singular curve, $[\phi] \in \alpha(D)$, and $\alpha(D) \not\subset \mathbf{G}_m[\phi]$ ($\mathbf{G}_m$-orbit). Let $F$ be the induced morphism $F: \mathbf{P}^{1} \times D \to X \times D$. Then

(4.1) $(p_{1} \circ F)(\mathbf{P}^{1} \times D)$ is two-dimensional, where $p_{1}$ is the first projection.

Indeed, if $\dim \operatorname{Im}(p_1 \circ F) \leq 1$, $\operatorname{Im}(p_1 \circ F) = C$, since $[\phi] \in \alpha(D)$. Thus $p_1 \circ F$ is a composition of some morphism $F'$: $\mathbf{P}^1 \times D \to \mathbf{P}^1$ and the normalization $\phi: \mathbf{P}^1 \to C \subset X$. Then $F'(0 \times D) = 0$ and $F'(\infty \times D) = \infty$ because $F(0 \times D) = P$,

$F(\infty \times D) = Q$, and $C$ is smooth at $P$ and $Q$. Since $[\phi] \in \alpha(D)$, $F'$ is induced from $D \to \text{Aut } \mathbf{P}_{0,\infty}^{1}$ because $\text{Aut } \mathbf{P}_{0,\infty}^{1}$ is a connected component of $\text{Hom}_k(\mathbf{P}^1, \mathbf{P}^1, \text{id}_{\{0,\infty\}})$. This contradicts $\alpha(D) \not\subset \mathbf{G}_m[\phi]$, which proves (4.1).

Let $D \subset \bar{D}$ be the smooth compactification of $D$, and $Y$ the closure of $F(\mathbf{P}^1 \times D)$ in $X \times \bar{D}$. Let $\tilde{Y} \to Y$ be the normalization and $\pi: \tilde{Y} \to Y \subset X \times \bar{D} \xrightarrow{p_2} \bar{D}$.

$$
\mathbf {P} ^ {1} \times D \simeq \pi^ {- 1} (D).\tag{4.2}
$$

It is enough to show that $F|_{U}$ is an immersion for some open set $U$ of $\mathbf{P}^1 \times D$ because $F$ is finite. Let $t \in D$ be such that $\alpha(t) = [\phi]$. Since $F|_{\mathbf{P}^1 \times t} = \phi$, $F$ is unramified at $0 \times t$ and $F^{-1}F(0 \times t) = \{0 \times t\}$. There is an open neighborhood $W \subset X \times D$ of $F(0 \times t)$ such that $F|_{V}$ is unramified for $V = F^{-1}(W)$ ($F$ is finite). The first projection $p_1: V \times_{X \times D} V \to V$ is proper. Now the diagonal map $\Delta: V \to V \times_{X \times D} V$ is an open immersion and $p_1(V \times_{X \times D} V - \Delta(V))$ is a closed set not containing $0 \times t$ because $p_1^{-1}(0 \times t) = \text{one point}$. If we set $U = V - p_1(V \times_{X \times D} V - \Delta(V))$, $U$ is an open neighborhood of $0 \times t$ and $F|_{U}$ is unramified and radical because $U = U \times_{X \times D} U$. Hence $F|_{U}$ is an immersion, and (4.2) is proved.

Since general fibers of $\pi$ are $\mathbf{P}^1$ by (4.2), any irreducible component of the fibers of $\pi$ is a rational curve, and any fiber of $Y$ over $\bar{D}$ is a union of rational curves. Thus we are done if we show that the cycle $Y \cdot (X \times t)$ is not an irreducible curve for some $t \in \bar{D}$. Let us assume to the contrary, and we will get a contradiction. First of all, the singular locus of $Y$ does not contain any fiber of $Y$ over $\bar{D}$. Hence for any $t \in \bar{D}$, the morphism of the fibers $\tilde{Y}_t \to Y_t$ induces an isomorphism of an open dense subset of $\tilde{Y}_t$ to its image. Since $Y \cdot (X \times t)$ is an irreducible curve by the assumption, $\tilde{Y}_t$ is an irreducible reduced subscheme because $\tilde{Y}_t$ has no embedded primes ($\tilde{Y}$ is normal and $\bar{D}$ is a non-singular curve). By the flatness of $\pi$, $p_a(\tilde{Y}_t) = p_a(\mathbf{P}^1) = 0$ by (4.2), whence $Y_t \simeq \mathbf{P}^1$. From (4.2), $F(0 \times D)$ and $F(\infty \times D)$ provide us with two sections $s_0$ and $s_\infty$, and $\tilde{Y}$ is a $\mathbf{P}^1$-bundle for Zariski topology. Thus there is a divisor $S$ on $\bar{D}$ such that $s_0 - s_\infty$ is linearly equivalent to $\pi^{-1}(S)$. In particular, $(s_0^2) - 2(s_0 \cdot s_\infty) + (s_\infty^2) = 0$. By the induced morphism $\sigma: \tilde{Y} \to Y \subset X \times \bar{D} \xrightarrow{p_1} X$, $s_0$ and $s_\infty$ are sent to $P$ and $Q$, respectively. Since $\sigma(\tilde{Y})$ is a surface by (4.1), $(s_0^2) < 0$, $(s_0 \cdot s_\infty) = 0$, $(s_\infty^2) < 0$ by a result of Mumford [11]. This contradicts $(s_0^2) - 2(s_0 \cdot s_\infty) + (s_\infty^2) = 0$. q.e.d.

We have a better form of the existence theorem for rational curves in characteristic $p$ than in characteristic 0. We recall that a Cartier divisor $D$ of a complete variety $X$ is said to be numerically effective if $(D \cdot Z) \geq 0$ for any irreducible curve $Z$ of $X$.

THEOREM 5. Let X be a non-singular projective variety over an algebraically closed field k of characteristic p > 0. Then X contains a rational curve unless the canonical divisor  $K_{x}$  is numerically effective.

Proof. If $K_{X}$ is not numerically effective, there is an irreducible curve $Z$ of $X$ such that $(K_{X} \cdot Z) < 0$. Let $i: Z_{1} \to Z \subset X$ be the normalization of $Z$. Let $\nu$ be a natural number such that

$$
- \dim X p _ {a} (Z _ {1}) - p ^ {\nu} (K _ {X} \cdot Z) \geq 1.
$$

For a power $q$ of $p$, let $Z_q \to \operatorname{Spec} k$ be the base change of $Z_1 \to \operatorname{Spec} k$ by the $(1/q)^{\text{th}}$ power endomorphism $\pi: \operatorname{Spec} k \to \operatorname{Spec} k$. Since $\pi$ is flat, $H^1(Z_q, \mathcal{O}_{Z_q}) = \pi^* H^1(Z_1, \mathcal{O}_{Z_1})$ whence $p_a(Z_q) = p_a(Z_1)$. Now we let $q = p^\nu$, $C = Z_q$, and $f: C \to Z_1$ the $q^{\text{th}}$ power $k$-morphism. Let $P$ be a $k$-rational point of $C$ and $j: P \to (i \circ f)(P) \in X$. Then since $\deg f = q$, we have

$$
\begin{array}{r l} \dim_ {[ i \circ f ]} \mathrm{Hom} _ {k} (C, X; j) & \geq \chi \bigl (C, (i \circ f) ^ {*} T _ {X} \otimes \mathcal {O} _ {C} (- P) \bigr) \\ & = - \dim \chi p _ {a} (C) - q (K _ {X} \cdot Z) \geq 1 \end{array}
$$

by Proposition 3 and the Riemann-Roch theorem. Hence we can find a non-singular curve $D$ and a finite morphism $g: D \to \operatorname{Hom}_k(C, X; j)$ with $[i \circ f] \in g(D)$. We claim that $D$ is not complete. Assuming to the contrary, let $F: C \times D \to X$ be the morphism induced by $g$. By the definition of $\operatorname{Hom}_k(C, X; j)$, $F(P \times D) = (i \circ f)(P)$. Hence $F(y \times D) = (i \circ f)(y)$ for any closed point $y$ of $C$, by the rigidity lemma [9, §4]. This means that $g(D) = [i \circ f]$, which is a contradiction, whence our claim is proved. Let $D \subset D'$ be a smooth compactification of $D$. Since $g$ does not extend to $D'$, the above morphism $F: C \times D \to X$ does not extend to $C \times D'$. Hence we have a rational mapping $F': C \times D' \to X$ which is not a morphism. From the final blowing-up in the process of elimination of indeterminacy of $F'$, we have a rational curve which is sent to a rational curve in $X$. q.e.d.

We obtain our result in characteristic $\geq 0$ by reducing it to Theorem 5 in characteristic $p$.

THEOREM 6. Let $X$ be a non-singular projective variety over an algebraically closed field $k$. If the anti-canonical divisor $K_X^{-1}$ is ample, $X$ contains a rational curve.

Proof. We can find an integral domain $A$ in $k$ which is finitely generated over $\mathbf{Z}$, and a projective smooth morphism $\pi: V \to S = \operatorname{Spec} A$ such that $V_{k} \simeq X$, and the dual $K_{V / S}^{-1}$ of the relative canonical sheaf is $\pi$-ample. Then for any geometric point $s$ of $S$ lying over a closed point of $S$, the field $k(s)$ of $s$ is of characteristic $>0$, whence $V_{s}$ contains a rational curve by Theorem

5.  $V_{s}$  contains a rational curve C such that  $(K_{V_{s}}^{-1} \cdot C) \leq \dim X + 1$  by Theorem 4. Let  $T \subset \operatorname{Hom}_{S}(\mathbf{P}_{S}^{1}, V)$  be the open and closed subscheme consisting of all the points  $f: P_{s}^{1} \to V$  ( $s \in S$  is the point dominated by f) such that  $0 < \deg_{P^{1}} f^{*} K_{V/S}^{-1} \leq \dim X + 1$ . Since  $K_{V/S}^{-1}$  is  $\pi$ -ample, T is quasi-projective [3, n°221]. Now T has at least one closed point over any closed point of S, whence so does  $T_{k}$  over k. Thus X contains a rational curve. q.e.d.

For Hartshorne's conjecture, all we need in this section is

COROLLARY 7. Let $X$ be an $n$-dimensional non-singular projective variety over an algebraically closed field $k$ such that the tangent bundle $T_{X}$ is ample. Then

i) $X$ contains a rational curve and any rational curve can be deformed as a cycle to a sum of rational curves $C$ such that $(C \cdot K_X^{-1}) = n + 1$.

ii) If $C (\subset X)$ is a rational curve such that $(C \cdot K_X^{-1}) = n + 1$, the resolution $f: \mathbf{P}^1 \to C$ is unramified and $f^*(T_X|_C) \simeq \mathcal{O}(2) \oplus \mathcal{O}(1)^{n-1}$.

Proof. Theorem 6 implies the first part of i). For any rational curve C of X, let $f: \mathbf{P}^1 \to C$ be the resolution. Since $f^*(T_X|_C)$ is ample, $f^*(T_X|_C) = \bigoplus_{i=1}^n \mathcal{O}(a_i)$ for $a_1 \geq a_2 \geq \cdots \geq a_n > 0$. We see $a_1 \geq 2$, since the natural homomorphism $T_{\mathbf{P}^1} \simeq \mathcal{O}(2) \to f^*(T_X|_C)$ is non-zero. Thus $(C \cdot K_X^{-1}) = \sum_{i=1}^n a_i \geq n + 1$, whence we obtain i) by Theorem 4. If $(C \cdot K_X^{-1}) = n + 1$, we see $a_1 = 2$, $a_2 = \cdots = a_n = 1$, and $T_{\mathbf{P}^1} \to f^*(T_X|_C)$ is an isomorphism to a direct summand of $f^*(T_X|_C)$ by the above argument. Hence for any closed point $P \in C$, the tangent map $T_{P\mathbf{P}^1} \to T_{f(\mathbf{P}),X}$ is injective, which implies that $f$ is unramified. q.e.d.

## 3. Proof of Hartshorne's conjecture

THEOREM 8. Let $X$ be an $n$-dimensional non-singular projective variety over an algebraically closed field $k$. If $T_X$ is ample, $X \simeq \mathbf{P}_k^n$.

Proof. By Corollary 7, there is a morphism $f \colon \mathbf{P}^1 \to X$ such that $f^*(K_X^{-1}) \simeq \mathcal{O}(n + 1)$. Hence we may assume that $n \geq 2$. Let $P$ be a closed point of $\mathbf{P}^1$ such that $f(\mathbf{P}^1)$ is smooth at $Q = f(P)$, and let $i \colon P \to Q \in X$. Let $V$ be the connected component of $\operatorname{Hom}_k(\mathbf{P}^1, X; i)$ containing $[f]$. We see $v^*(K_X^{-1}) \simeq \mathcal{O}(n + 1)$ for any closed point $v \in V$ by the connectivity of $V$, and $v^*(T_X) \otimes \mathcal{O}(-P) \simeq \mathcal{O}(1) \oplus \mathcal{O}^{n-1}$ by Corollary 7. Hence $V$ is smooth and irreducible of dimension $n + 1$ by Proposition 3. Let $G = \{g \in \operatorname{Aut} \mathbf{P}^1 | g(P) = P\}$. Since $G$ is connected, the natural action of $G$ on $\operatorname{Hom}_k(\mathbf{P}^1, X; i)$ induces the action $\sigma$ of $G$ on its connected component $V$:

$$
\sigma \colon G \times V \longrightarrow V, \sigma (g, v) (x) = v (g ^ {- 1} x), g \in G, v \in V, x \in \mathbf {P} ^ {1}.
$$

G also acts on  $V \times P^{1}$ :

$$
\tau \colon G \times V \times \mathbf {P} ^ {1} \longrightarrow V \times \mathbf {P} ^ {1}, \tau (g, v, x) = (\sigma (g, v), g x),
$$

where $g \in G$, $v \in V$, $x \in \mathbf{P}^1$. Let $\text{Chow}_X^d$ be the Chow variety parametrizing 1-dimensional effective cycles $C$ of $X$ such that $(C \cdot K_X^{-1}) = d$. For any $v \in V$, we see that $v: \mathbf{P}^1 \to v(\mathbf{P}^1)$ is birational, because otherwise $(v(\mathbf{P}^1), K_X^{-1}) < \deg v^* K_X^{-1} = n + 1$, which is a contradiction to Corollary 7, i). Hence $(v(\mathbf{P}^1), K_X^{-1}) = n + 1$, and we have a morphism $\alpha: V \to \text{Chow}_X^{n+1}$ by $\alpha(v) = \text{the cycle } v(\mathbf{P}^1)$, $v \in V$. We see that the induced morphism $\alpha: V \to \overline{\alpha(V)}$ is $G$-invariant, where $\overline{\alpha(V)}$ is the closure of $\alpha(V)$ in $\text{Chow}_X^{n+1}$. The morphism $\alpha$ induces $\gamma: V \to Y$, where $Y \to \overline{\alpha(V)}$ is the normalization of $\overline{\alpha(V)}$ in the field $k(V)^G$ of $G$-invariant rational functions on $V$. (In the proof of Lemma 9, ii), it will be clear that $k(V)^G$ is finite over $k(\overline{\alpha(V)})$.) Then we use a lemma which will be proved in the next section.

LEMMA 9. i) $\sigma$ is a free action, and

ii) $(Y, \gamma)$ is the geometric quotient of $V$ by $G$ in the sense of [10].

Thus $V$ is a principal fiber bundle over $Y$ with group $G$ [10, Proposition 0.9]; in other words, $V$ is flat over $Y$, and $(\sigma, p_2): G \times V \to V \times_Y V$ is an isomorphism. Thus, in particular, $Y$ is a non-singular projective variety of dimension $n - 1$. (Chow$_X^{n+1}$ is projective, and hence so is $Y$.) We claim

$$
Y \simeq \mathbf {P} (T _ {Q, X} ^ {*}) \simeq \mathbf {P} ^ {n - 1}.\tag{8.1}
$$

Fixing a parameter $t$ of $\mathcal{O}_{\mathbf{P}^1,P}$, we introduce a morphism

$$
\Phi \colon V \longrightarrow \mathbf {V} (T _ {Q, X} ^ {*}) \simeq A ^ {n},   \Phi (v) = (d v) _ {P} \left(\frac {d}{d t}\right),   v \in V.
$$

For any closed point $v \in V$, we consider $\Phi^{-1}\Phi(v)$. For any finite type $k$-scheme $T$ and for any morphism $T \to V \subset \operatorname{Hom}_k(\mathbf{P}^1, X; i)$ over $k$, $T \to V$ factors through $\Phi^{-1}\Phi(v) \to V$ if and only if the morphism $\mathbf{P}_T^1 \to X_T$ coincides on $\operatorname{Spec}(\mathcal{O}_{\mathbf{P}^1, P}/I_{\mathbf{P}^1, P}^2)$ with $v_T$, where $I_{\mathbf{P}^1, P}$ is the maximal ideal of $\mathcal{O}_{\mathbf{P}^1, P}$. This is because $V$ is a connected component of $\operatorname{Hom}_k(\mathbf{P}^1, X; i)$ and a morphism $\operatorname{Spec}(\mathcal{O}_{\mathbf{P}^1, P}/I_{\mathbf{P}^1, P}^2) \simeq \operatorname{Spec} k[t]/(t^2) \to X$ consists of a point $x$ of $X$ and a tangent vector at $x$. Thus

$$
\Phi^ {- 1} \Phi (v) \simeq V \cap \operatorname{Hom} _ {k} (\mathbf {P} ^ {1}, X; v _ {1}) \text {   for   any   } v,
$$

where $v_{1}$ is the restriction of $v$ to $\operatorname{Spec}(\mathcal{O}_{\mathbf{P}^{1},P}/I_{\mathbf{P}^{1},P}^{2})$. We see that $\Phi^{-1}\Phi(v)$ is smooth and of dimension 1 at $v$ by Proposition 3, because $V \cap \operatorname{Hom}_{k}(\mathbf{P}^{1}, X; v_{1})$ is open in $\operatorname{Hom}_{k}(\mathbf{P}^{1}, X; v_{1})$, $h^{0}(\mathbf{P}^{1}, v^{*}(T_{X}) \otimes \mathcal{O}(-2)) = 1$, and $h^{1}(\mathbf{P}^{1}, v^{*}(T_{X}) \otimes \mathcal{O}(-2)) = 0$ by Corollary 7, ii). Now $\Phi$ is equi-dimensional, whence $\Phi$ is flat [2, Chapitre IV, Proposition (15.4.2)]. We see, furthermore, that $\Phi$ is smooth

because any fiber of $\Phi$ is smooth [4, Exposé II, Théorème 2.1]. For any $v \in V$, $\Phi(v) \neq 0$ because $v: \mathbf{P}^1 \to X$ is unramified by Corollary 7, ii). Thus we have a smooth morphism $\Phi: V \to V(T_{Q,X}^*) - \{0\}$, which induces morphism $V \to \mathbf{P}(T_{Q,X}^*) \simeq \mathbf{P}^{n-1}$. The morphism $V \to \mathbf{P}^{n-1}$ is $G$-invariant, whence we have the induced smooth morphism $Y \to \mathbf{P}^{n-1}$. Now $Y$ is proper étale over $\mathbf{P}^{n-1}$ because $\dim Y = n - 1$. This implies that $Y \simeq \mathbf{P}^{n-1}$ because $\mathbf{P}^{n-1}$ is simply connected, which proves our claim (8.1).

Let us consider a $G$-invariant morphism

$$
F \colon V \times \mathbf {P} ^ {1} \longrightarrow Y \times X, \quad F (v, x) = (\gamma (v), v (x)), v \in V, x \in \mathbf {P} ^ {1}.
$$

Let $Z = \operatorname{Spec}_{Y \times X}[(F_{*}\mathcal{O}_{V \times \mathbf{P}^{1}})^G]$. Then $Z$ is the geometric quotient $V \times \mathbf{P}^{1}/G$ and is a $\mathbf{P}^{1}$-bundle over $Y$ for the étale topology. These can be easily checked after the base change by $V \to Y$ because $V$ is a principal $G$-bundle over $Y$. We obtain a section $S$ of $Z$ over $Y$, via the morphism $V \ni v \mapsto (v, P) \in V \times \mathbf{P}^{1}$. Then $\psi: Z \to Y$ is a $\mathbf{P}^{1}$-bundle for Zariski topology because $Z \simeq \mathbf{P}(\psi_{*}\mathcal{O}_{Z}(S))$. Let us introduce a proper morphism $\pi: Z \to X$ via the $G$-invariant morphism II: $V \times \mathbf{P}^{1} \ni (v, x) \mapsto v(x) \in X$. Then we claim

$$
\pi \text {   is   étale   on   } Z - S \text {   and   } \pi (S) = Q .\tag{8.2}
$$

It is enough to show $\Pi$ is smooth on $V \times (\mathbf{P}^1 - \{P\})$. Also it is enough to show that $\Pi|_{V \times x} \colon V \simeq V \times x \to X$ is smooth for any $x \in \mathbf{P}^1 - \{P\}$. By the same argument as we used for (8.1), it is enough to show $V \cap \operatorname{Hom}_k(\mathbf{P}^1, X; v|_{\{P,x\}})$ is smooth of dimension 1 at $v$ for any $v \in V$. We see that

$$
h ^ {0} \left(\mathbf {P} ^ {1}, v ^ {*} \left(T _ {X}\right) \otimes \mathcal {O} (- 2)\right) = 1 \quad \text { and } \quad h ^ {1} \left(\mathbf {P} ^ {1}, v ^ {*} \left(T _ {X}\right) \otimes \mathcal {O} (- 2)\right) = 0
$$

by Corollary 7, ii).

This proves our claim (8.2) by Proposition 3.

Thus $\pi^{-1}(X - \{Q\})$ is finite étale over $X - \{Q\}$, whence the Stein factorization $U = \operatorname{Spec}_X(\pi_*\mathcal{O}_Z) \to X$ is unramified at the points over $X - \{Q\}$. By the purity of branch loci, $U$ is finite étale over $X$ since $\dim X = n \geq 2$. The morphism $\phi: Z \to U$ contracts $S \simeq \mathbf{P}^{n-1}$ to a point $R$ of the smooth variety $U$ and induces an isomorphism $Z - S \stackrel{\sim}{\to} U - \{R\}$ [2, Chapitre III, Proposition (4.4.1)].

$$
\mathcal {O} _ {S} \otimes \mathcal {O} (S) \simeq \mathcal {O} _ {\mathbf {p} ^ {n - 1}} (- 1).\tag{8.3}
$$

Let $L \simeq \mathbf{P}^{n-2} \subset Y$ be a hyperplane and $C \simeq \mathbf{P}^1 \subset S$ be a straight line such that $\psi(C) \not\subset L$. Let $D = \psi^{-1}(L)$, and then $(C \cdot D) = 1$. Since $R \in \phi(D)$, $\phi^{-1}\phi(D) = D + aS$ as divisors for some $a > 0$. By the projection formula, $(C \cdot \phi^{-1}\phi(D)) = (\phi(C) \cdot D) = 0$. Thus $0 = 1 + a(S \cdot C)$, whence $(S \cdot C) = -1$. This proves (8.3). Then we claim

$$
U \simeq \mathbf {P} ^ {n}.\tag{8.4}
$$

By taking the direct image under $\psi$ of the exact sequence (see (8.3))

$$
0 \longrightarrow \mathcal {O} _ {z} \longrightarrow \mathcal {O} _ {z} (S) \longrightarrow \mathcal {O} _ {s} (- 1) \longrightarrow 0,
$$

we have the exact sequence

$$
0 \longrightarrow \mathcal {O} _ {Y} \longrightarrow \psi_ {*} \mathcal {O} _ {Z} (S) \longrightarrow \mathcal {O} _ {Y} (- 1) \longrightarrow 0,
$$

(we note $\mathcal{R}^1\psi_*\mathcal{O}_Z = 0$). Since $\operatorname{Ext}_{\mathbf{P}^{n-1}}^1 (\mathcal{O}(-1),\mathcal{O}) = 0$, $\psi_*\mathcal{O}_Z(S) = \mathcal{O}_Y\oplus \mathcal{O}_Y(-1)$. Thus $Z\simeq \mathbf{P}_{\mathbf{P}^{n-1}}(\mathcal{O}\oplus \mathcal{O}(-1))$ and the section $S$ corresponds to $\mathcal{O}\oplus \mathcal{O}(-1)\to$$\mathcal{O}(-1)$. Now it is easy to see that the linear system attached to $\psi^*\mathcal{O}(1)\otimes$$\mathcal{O}(S)$ gives us a morphism $Z\to \mathbf{P}^n$ contracting $S$ to a point and inducing an isomorphism on $Z - S$. Thus the birational correspondence $\mathbf{P}^n\to U$ via $\mathbf{P}^n\gets Z\to U$ is an isomorphism by Zariski's main theorem. This proves our claim (8.4).

Since $\mathbf{P}^n$ is simply connected, $U \simeq \mathbf{P}^n \to X$ is a Galois covering. Thus $\mathbf{P}^n \simeq X$ because any automorphism of $\mathbf{P}^n$ has a fixed point.

q.e.d.

## 4. Proof of Lemma 9

Let $X, n, k, f, P, Q, V, G, \sigma, \alpha, \gamma$, and $Y$ (symbols which appeared before Lemma 9) be as in Section 3.

(i): First, we show that $\Psi = (p_2, \sigma) \colon G \times V \to V \times V$ is proper. Let $A$ be an arbitrary discrete valuation ring over $k$ with quotient field $K$. Let $g \in G(K)$ and $v \in V(K)$ satisfy $\Psi(g, v) = (v, \sigma(g, v)) \in V(A) \times V(A)$. $\Psi$ will be proper by the valuative criterion if we show $g \in G(A)$. Setting $w = \sigma(g, v)$, we have two morphisms $v$, $w \colon \mathbf{P}_A^1 \to X_A$. Two morphisms $v_K$ and $w_K$ have the same image in $X_K$ by the definition of $w$. Since $\mathbf{P}_A^1$ is proper over $A$, $\operatorname{Im} v = \operatorname{Im} w (= \text{the closure of } \operatorname{Im}(v_K))$. As we have seen at the beginning of Section 3, $v_K$ and $w_K$ are the normalizations of $\operatorname{Im}(v_K)$ over $K$. Thus both $v$ and $w$ are finite and birational, whence $v$ and $w$ are normalizations of $\operatorname{Im} v$ in its function field. Hence there is an $A$-automorphism $h \colon \mathbf{P}_A^1 \to \mathbf{P}_A^1$ such that $w = v \circ h^{-1}$. We see $h_k = g$ and $h \in G(A)$ because $G$ is closed in $\operatorname{Aut} \mathbf{P}^1$. Now $\Psi$ is proved to be proper. It is obvious that $\Psi$ induces an injection of the sets of $k$-rational points $G(k) \times V(k) \to V(k) \times V(k)$. This means that $\Psi$ is radical, and now we have only to show $(d\Psi)_{(e,v)}$ is injective for any $v \in V(k)$ and the identity $e \in G(k)$ (a proper radical unramified morphism is a closed immersion). We see $T_{e,G} = H^0(\mathbf{P}^1, T_{\mathbf{P}^1} \otimes \mathcal{O}(-P))$, $T_{v,V} = H^0(\mathbf{P}^1, v^*(T_X) \otimes \mathcal{O}(-P))$ (Proposition 3), and

$$
(d \Psi) _ {(e, V)} (x \oplus y) = y \oplus (y - v _ {*} x) \quad \text { for } \quad x \in T _ {e, G} \text {   and   } y \in T _ {v, V},
$$

where  $v_{*}$  is the natural homomorphism  $v_{*}: T_{P^{1}} \otimes \mathcal{O}(-P) \to v^{*}(T_{X}) \otimes \mathcal{O}(-P)$ . Since  $v: P^{1} \to v(P^{1})$  is birational,  $v_{*}$  and hence  $(d\Psi)_{(e,V)}$  are injective. This proves that  $\Psi$  is a closed immersion. q.e.d.

(ii): Let $k(Q)$ be the residue field of $Q$ considered as an $\mathfrak{O}_X$-module, and then $v^*k(Q)$ is an $\mathfrak{O}_{\mathbf{P}^1}$-module of finite length for any $v \in V(k)$. The subset $M$ of $V(k)$ defined by $M = \{v \in V(k) | v^*k(Q) = k(P)\}$ is open, because $v(P) = Q$ for any $v \in V(k)$ and the function $V(k) \to \mathbf{Z}$ sending $v \in V(k)$ to the length of $v^*k(Q)$ is upper semicontinuous. We see $[f] \in M$ and $M$ is open dense in $V(k)$, because $f(\mathbf{P}^1)$ is smooth at $Q$. We claim that any non-empty fiber of $\alpha(k): V(k) \to \text{Chow}_X^{n+1}(k)$ is, as a set, a union of a finite number of $G(k)$-orbits of dimension 2 and that, $\alpha(k)^{-1}\alpha(k)(v)$ is a $G(k)$-orbit for any $v \in M$. For $v \in V(k)$, $\alpha(k)^{-1}\alpha(k)(v)$ is identified with the set of all the automorphisms of $\mathbf{P}^1$ which send $P$ into $v^{-1}(Q)$. The first claim follows from the finiteness of $v$, and the second from the definition of $M$. Hence $\gamma$ is equi-dimensional, and $\gamma: V \to Y$ is universally open by Chevalley's theorem [2, Chapitre IV, Corollaire (14.4.4)]. We claim that any non-empty fiber of $\gamma(k): V(k) \to Y(k)$ is a $G(k)$-orbit. Let $S = \{v \in V(k) | \gamma(k)^{-1}\gamma(k)(v) \text{ has more than one orbit}\}$. In other words, $S = p_1\{(V \times_Y V)(k) - \Psi(G \times V)(k)\}$, where $\Psi: G \times V \to V \times V$ is as in the proof of Lemma 9, i). $S$ is an open set of $V(k)$ since $\Psi$ is a closed immersion and $p_1: V \times_Y V \to V$ is an open morphism. Thus $S = \phi$ because $S$ is disjoint from the open dense subset $M$ of $V(k)$ by the above assertion. Thus we have shown that $\gamma: V \to \gamma(V)$ is the geometric quotient. (The property $(\gamma_*\mathcal{O}_V)^G \simeq \mathcal{O}_{(V)}$ is obvious by the definition of $Y$.) It remains to show that $\gamma$ is surjective. Let $A$ be a discrete valuation ring over $k$ with residue field $k'$ and quotient field $K$. Let $v$ be an arbitrary element of $V(k)$. For the surjectivity of $\gamma$, it is enough to find an element $g \in G(K)$ such that $\sigma(g, v) \in V(A)$. Let $C \subset X_A$ be the reduced closed subscheme obtained as the closure of $\text{Im}(v) (\subset X_K)$ in $X_A$. Then $C$ is flat over $A$. Let $N$ be the normalization of $C$ in its function field. We see $N_K \simeq P_K^1$ since $v: P_K^1 \to C_K^1$ is the normalization. From this, it is easy to see that any irreducible component of $C_{\bar{K}}'$, is a rational curve, where $\bar{k}'$ is the algebraic closure of $k'$. The 1-dimensional cycle $\bar{C}_{\bar{k'}}$ associated to $C_{\bar{k'}}$ is an irreducible curve by Corollary 7, i) and $(\bar{C}_{\bar{k'}} \cdot K_{\bar{X}_{\bar{k'}}^-1}) = (C_K \cdot K_{\bar{X}_K^-1}) = n + 1$. Thus $C$ has only finitely many points at which $C$ is not regular, whence $N_{k'} \to C_{k'}$ induces an isomorphism of some open dense subset of $N_{k'}$ to its image. In particular, $N_{\bar{k'}}$ is an irreducible curve as a cycle, and $N_{\bar{k'}}$ is irreducible reduced since $N_{\bar{k'}}$ has no embedded components ($N$ is normal). Thus $N_{\bar{k'}} \simeq P_k^1, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, w, x', y', z', d', e', f', g', h', i', j', k', l', m', n', o, p, q, r, s, t, u, v, x', y', z', d', e', f', g', h', u', v', z', u', p', q', r', s', u', v', z', u', q', r', s', u', v', z', u', p', q', r', s', u', v', z', u', p', q', r', u', v', z', u', p', q', r', u', v', z', u', p', q', r', u', v', z', u', p', q', r', u', v', z', u', p', q', r', u', v', z', u', p', q', r', u', v', z', u', p', q', r', u'', v'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', v''_A, v''_B, v''_C, v''_D, v''_E, v''_F, v''_G, v''_H, v''_I, v''_J, v''_K, v''_L, v''_M, v''_N, v''_O, v''_P, v''_Q, v''_R, v''_S, v''_T, v''_U, v''_V, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_W, v''_X, v''_Y, v''_Z, v''_{K'}$

and choose an isomorphism $h \colon N \xrightarrow{\sim} \mathbf{P}_A^1$ such that $h(S) = P \times \operatorname{Spec} A$. Let $w \colon \mathbf{P}_A^1 \xrightarrow{h^{-1}} N \to C \subset X_A$. Then $w_K \in G(K)v$, and hence $w \in V(A)$. q.e.d.

HARVARD UNIVERSITY, CAMBRIDGE, MA., AND

KYOTO UNIVERSITY, KYOTO, JAPAN

## REFERENCES

[1] T. T. FRANKEL, Manifolds with positive curvature, Pacific J. Math. 11 (1961), 165-174.

[2] A. GROTHENDIECK, Eléments de géométrie algébrique, Publ. Math. IHES, No. 4 (1960), No. 8 (1961), No. 17 (1961), et No. 28 (1966).

[3] ——, Fondements de la géométrie algébrique, Secrétariat Math. 11 Rue Pierre Curie, Paris 5$^{e}$ (1962).

[4] ——, Revêtements étales et groupe fondamental (SGA 1), Lecture Notes in Math. 224, Springer-Verlag (1971).

[5] R. HARTSHORNE, Ample subvarieties of algebraic varieties, Lecture Notes in Math. 156, Springer-Verlag (1970).

[6] S. KOBAYASHI and T. OCHIAI, On complex manifolds with positive tangent bundles, J. Math. Soc. Japan, 22 (1970), 499-525.

[7] T. MABUCHI, $\mathbf{C}^3$-actions and algebraic threefolds with ample tangent bundle, Nagoya Math. J. 69 (1978), 33-64.

[8] S. MORI and H. SUMIHIRO, On Hartshorne's conjecture, J. Math. Kyoto U. 18-3 (1978), 523-533.

[9] D. MUMFORD, Abelian Varieties, Oxford U. Press, 1974.

[10] ——, Geometric invariant theory, Ergeb. der Math. und ihrer Grenz. Bd. 34, Springer-Verlag, 1965.

[11] ——, The topology of normal singularities of an algebraic surface and a criterion of simplicity, Publ. Math. IHES, No. 9 (1961), 5-22.

[12] F. OORT, Finite groups schemes, local moduli for abelian varieties, and lifting problems, Algebraic Geometry, Oslo 1970, Molters-Noordhoff Groningen, the Netherlands, (1972), 223-254.

(Received January 8, 1979)