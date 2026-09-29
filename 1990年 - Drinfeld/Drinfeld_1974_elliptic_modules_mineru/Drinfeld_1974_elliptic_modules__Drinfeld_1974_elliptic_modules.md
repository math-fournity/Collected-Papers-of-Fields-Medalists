# ELLIPTIC MODULES

UDC 519.49

## V. G. DRINFEL'D

Abstract. The notion of elliptic module is introduced, generalizing the concept of an elliptic curve, and an analog of the theory of elliptic and modular curves is constructed. Here the role of the group  $GL(2,Q)$  is played by  $GL(2,k)$, where k is a function field. A theorem on the coincidence of L-functions of modular curves and Jacquet-Langlands L-functions corresponding to k is proved.

Bibliography: 14 items.

## Introduction

A) Statement of the problem and main result. Let $k$ be a global field, $\infty$ a place of $k$, $d$ a natural number, and $k_{\infty}$ the completion of $k$ at $\infty$.

Definition. The triple $(k, \infty, d)$ is called admissible if a) all places of $k$, except perhaps $\infty$, are nonarchimedean, and b) $d \leq [\overline{k}_{\infty} : k_{\infty}]$.

Admissible triples are of the following types:

1) $k = \mathbf{Q},\infty$ is the archimedean norm, and $d = 1$

2) $k = \mathbf{Q},\infty$ is the archimedean norm, and $d = 2$

3) $k$ is an imaginary quadratic extension of $\mathbf{Q}$, $\infty$ is the archimedean norm, and $d = 1$;

4) $k$ is a function field, and $\infty$ and $d$ are arbitrary.

The goal of this paper is the generalization of three classical theorems (connected with the first three types of admissible triples): 1) the Kronecker-Weber theorem, 2) the Eichler-Shimura theorem on $\zeta$-functions of modular curves, and 3) the fundamental theorem on complex multiplication. This generalization is connected with the fourth type of admissible triple.

Let $(k, \infty, d)$ be an admissible triple. We introduce the following notation: A is the ring of elements of k which are integral at all places except $\infty$; U is the ring of adèles of k; and $\mathfrak{A}_f$ is the ring of adèles without the $\infty$ component. We formulate the classical theorems 1)-3) in a form suitable for generalization. First we introduce some necessary definitions.

Let $(k,\infty,d)$ be an admissible triple of type 1)-3), and let K be a field over A (i.e. there is given a homomorphism $i:A\to K$).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">AMS (MOS) subject classifications (1970). Primary 10D25, 12A65; Secondary 14K22.</span></small>

Definition. An elliptic A-module of rank d over K is the following: in case 1), a homogeneous torus over K; in case 2), an elliptic curve over K; and in case 3), an elliptic curve X over K together with a homomorphism $\phi$: $A \to \operatorname{End} X$ such that $i = D \circ \phi$, where $D$: $\operatorname{End} X \to K$ is a differential.

In the same way we introduce the concept of an elliptic A-module of rank d over S, where S is a scheme over A.

Definition. Let $S$ be a scheme over $k$, $I \subset A$ a nonzero ideal, and $X$ an elliptic $A$-module of rank $d$ over $S$. A structure of level $I$ on $X$ is an isomorphism (of $A$-modules over $S$) ($I^{-1} / A$)$^d \times S \stackrel{\sim}{\to} X_I$, where $X_I \subset X$ is the annihilator of $I$.

If $I$ is sufficiently small, then the functor that associates to the scheme $S$ over $k$ the set of isomorphism classes of elliptic $A$-modules of rank $d$ over $S$ with structure of level $I$ is representable by a smooth $(d - 1)$-dimensional manifold $N_I$. We set $N = \lim_{\leftarrow} N_I$. We can define in a natural way an action of the group $GL(d, \mathfrak{A}_f)$ on $N$.

Theorem 1. Let $(k, \infty, d)$ be a triple of type 1) or 3). Then $N$ is the spectrum of the maximal abelian extension of $k$, which is completely split over $\infty$. The action of $\mathfrak{A}_f^*$ coincides with the action from class field theory.

Theorem 2. Let $(k, \infty, d)$ be a triple of type 2), let $\overline{N}$ be a smooth compactification of $N$, and let $l$ be a prime number. Then $H^{1}(\overline{N}, \overline{\mathbf{Q}}_{l}) \simeq \bigoplus_{i} U_{i} \otimes W_{i}$, where $U_{i}$ is an irreducible representation of $\mathrm{GL}(2, \mathfrak{A}_{f})$ over $\overline{\mathbf{Q}}$, and $W_{i}$ is a representation of $\mathrm{Gal}(\overline{\mathbf{Q}} / \mathbf{Q})$ in the space $\mathbf{Q}_{l}^{2}$. Let $U_{i} = \bigotimes U_{i}^{p}$, where $U_{i}^{p}$ is an irreducible representation of $\mathrm{GL}(2, \mathbf{Q}_{p})$, and let $W_{i}^{p}$ be the restriction of $W_{i}$ on $\mathrm{Gal}(\overline{\mathbf{Q}}_{p} / \mathbf{Q}_{p})$.

1) If $p \neq l$ and $U_i^p$ is a representation of class 1 (cf. [1]), then $W_i^p$ is unramified and $L(s, W_i^p) = L(s - \frac{1}{2}, \hat{U}_i^p)$. Here $\hat{U}_i^p$ is the representation contragredient to $U_i^p$, and the L-functions are taken in the sense of Serre and Jacquet-Langlands.

2) $\bigoplus_{i} U_{i} \otimes_{\overline{\mathbf{Q}}} \mathbf{C} \simeq \operatorname{Hom}_{GL(2, \mathbb{R})} (\Pi, A_0)$, where $\Pi$ is a representation of $GL(2, \mathbb{R})$ in the space of functions on $\mathbf{P}_1(\mathbb{R})$, factored out by the constants, and $A_0$ is the space of parabolic forms\* on $GL(2, \mathfrak{A})$ in the sense of [10].

In this paper the concept of elliptic module for triples of type 4) is introduced, modular varieties are constructed, and analogs of Theorems 1 and 2 are proved for $d = 1, 2$.

B) Outline of the paper. The concept of elliptic module is introduced in §2. In §3 an analytic theorem is proved on the uniformization of an elliptic module over $\overline{k}_{\infty}$ with the help of a lattice in $\overline{k}_{\infty}$. In §5 a universal family of elliptic $A$-modules of rank $d$ is constructed. The proof of smoothness of the modular varieties uses properties of formal modules (cf. §§1 and 4) (a formal module is the analog of a formal group). Also in §5, a congruence relation of the form [14] is proved. In §6 the modular varieties are constructed analytically (as factors of some domain $\Omega^d$ by a discrete group). The domain $\Omega^d$ is closely connected with the Bruhat-Tits complex of the group $GL(d, k_{\infty})$. In §7 elliptic modules over complete discrete normed fields are studied. In §8 an analog of Theorem 1 is studied. In §9 the compactifications of

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*Editor's note. In English the common term is cusp form.</span></small>

modular surfaces (for $d = 2$) are constructed; this uses results of §7. In §§10 and 11 the analog of Theorem 2 is proved.

This article was written under the influence of the paper [14] and also of conversations with I. I. Pjateckiš-Sapiro. However, modular varieties have been constructed algebraically (as in [6]). The analytic description of modular varieties is based on ideas from [3] (although the congruence subgroups of $GL(2, A)$ are not Schottky groups).

The author expresses his deep gratitude to Ju. I. Manin and I. I. Pjateckiš-Sapiro for their valuable remarks and attention to this paper.

## §1. Formal modules

A) Definitions and notation. A formal group over a ring $B$ is, by definition, a formal series $F \in B[[x, y]]$ such that $F(x, y) = F(y, x)$, $F(x, 0) = x$, and $F(x, F(y, z)) = F(F(x, y), z)$. A homomorphism from a formal group $F$ into a formal group $G$ is a series $\beta \in B[[x]]$ such that $\beta(F(x, y)) = G(\beta(x), \beta(y))$. For any formal group $F$ over $B$ there is a canonical homomorphism $D$: End $F \to B$ that sends the endomorphism $\phi$ to the number $\phi'(0)$.

Example. $F(x, y) = x + y$; this group is called additive.

Let $B$ have characteristic $p$. Every endomorphism of the additive group over $B$ is defined by a series $\sum_{i=0}^{\infty} b_i x^{p^i}$. Henceforth we shall identify the element $b \in B$ with the endomorphism of multiplication by $b$. The Frobenius endomorphism (corresponding to the series $x^p$) will be denoted by $\tau$. Thus the ring of endomorphisms of the additive group consists of “series” $\sum_{0}^{\infty} b_i \tau^i$ with the commutation rule $\tau b = b^p \tau$. We denote this ring by $B\{\{\tau\}\}$.

Let $O$ be a ring, $B$ an algebra over $O$, and $\gamma: O \to B$ the natural homomorphism. Definition. A formal $O$-module over $B$ is a pair $(F, f)$, where $F$ is a formal group over $B$, and $f$ is a homomorphism from $O$ to End $F$ such that $D \circ f = \gamma$.

Example.  $F(x, y) = x + y$  and  $f_{a}(x) = ax$  for  $a \in O$  (we write  $f_{a}$  instead of  $f(a)$ ). This module is called additive.

The germ of a formal O-module over B mod deg n is a pair  $(F, f)$ , where  $F \in B[[x, y]]/(x, y)^{n}$  and  $f_{a} \in B[[x]]/(x^{n})$ , and all relations between F and f which arise from the definition of a formal module are satisfied mod deg n.

We consider the following functor from the category of O-algebras to the category of sets:  $B \mapsto$  set of formal O-modules over B. We can clearly represent this functor by some algebra  $\Lambda_{O}$ . (The generators of  $\Lambda_{O}$  are the “indeterminate coefficients” of the series F and  $f_{a}$ , and the relations between them are those which are required for  $(F, f)$  to be a formal O-module.)

$\Lambda_{O}$ has a natural gradation. It is easy to check that the set of germs of formal O-modules over B mod $\deg(n+1)$ is canonically isomorphic to the set of O-module homomorphisms $\bigoplus_{k=0}^{n-1}\Lambda_{O}^{k}\stackrel{\psi}{\rightarrow}B$ such that $\psi(ab)=\psi(a)\psi(b)$ and $\psi(1)=1$. Elements of the form ab, where $a\in\Lambda_{O}, b\in\Lambda_{O}, \deg a>1$ and $\deg b>1$, generate a homogeneous ideal. We denote by $\widetilde{\Lambda_{O}}$ the factor of $\Lambda_{O}$ by this ideal.

Proposition 1.1. Let $n \geq 2$. Then $\Lambda_O^{n-1}$ (as an O-module) can be defined by generators $a$ and $h(a)$ (for all $a \in O$) and the relations

$$
\alpha (a ^ {n} - a) = \left\{ \begin{array}{l l} h (a), & \text { if   } n \text {   is   not   a   power   of   a   prime   number } \\ h (a) \circ p, & \text { if   } n = p ^ {k}, \end{array} \right.\tag{1}
$$

$$
h (a + b) - h (a) - h (b) = \alpha C _ {n} (a, b),\tag{2}
$$

$$
a h (b) + b ^ {n} h (a) = h (a, b).\tag{3}
$$

(Here $C_n(x, y) = (x + y)^n - x^n - y^n$ if $n$ is not a power of a prime number, and

$$
C _ {n} (x, y) = ((x + y) ^ {n} - x ^ {n} - y ^ {n}) / p \text {   if   } n = p ^ {k}).
$$

Proof. Clearly, $\Lambda_O^{n-1}$ can be defined by the generators $b(a)$ and $c_i$ ($0 < i < n$) with the relations

$$
\begin{array}{c} a (x + y + \Phi (x, y)) + h (a) (x + y) ^ {n} = a x + a y + h (a) x ^ {n} + h (a) y ^ {n} + \Phi (a x, a y), \\ a x + h (a) x ^ {n} + b x + h (b) x ^ {n} + \Phi (a x, b x) = (a + b) x + h (a + b) x ^ {n}, \end{array}
$$

$$
\begin{array}{c} a b x + h (a b) x ^ {n} = a (b x + h (b) x ^ {n}) + h (a) (b x) ^ {n}, \\ \Phi (x, y) = \Phi (y, x), \Phi (y, z) + \Phi (x, y + z) = \Phi (x, y) + \Phi (x + y, z) \end{array}
$$

(where $\Phi(x, y) \stackrel{\text{def}}{=} \sum_{1}^{n} c_i x^i y^{n-i}$). It is well known that from the last two relations follows $\Phi(x, y) = \alpha C_n(x, y)$ (cf. [7]). $\square$

B) The case when $O$ is a field.

Proposition 1.2. 1) If $O$ is a field, then every formal $O$-module is isomorphic to an additive module.

2) If $O$ is infinite, then there exists a unique isomorphism with an additive module, whose derivative at zero equals 1. In this case $\Lambda_O \simeq O[c_1, c_2, \ldots]$, where $\deg c_i = i$.

Proof. The case of characteristic zero is well known (cf. [7]). Let $\operatorname{char} O = p$, let $B$ be an algebra over $O$, and let $(F, f)$ be a formal $O$-module over $B$. Then multiplication by $p$ in $F$ is zero; therefore (cf. [7]) $F$ is isomorphic to an additive group. We can assume that $F$ is additive. Let $f: O \to B\{\{\tau\}\}$ have the form $f(a) \equiv a + \phi(a)\tau^k (\bmod \tau^{k+1})$. We shall prove that there exists an $s \in B$ such that $(1 + s\tau^k)f(a)(1 + s\tau^k)^{-1} \equiv a (\bmod \tau^{k+1})$ for all $a \in O$. Indeed, since $f$ is a homomorphism then $\phi(a + b) = \phi(a) + \phi(b)$ and $\phi(a \circ b) = a\phi(b) + b^{p^k}\phi(a)$, and so $(b^{p^k} - b)\phi(a) = (a^{p^k} - a)\phi(b)$. If $O \subset \mathbf{F}_{p^k}$, then the existence and uniqueness of $s$ is clear ($s = \phi(a)/(a^{p^k} - a)$, where $a \in O$, $a \notin \mathbf{F}_{p^k}$). If $O \subset \mathbf{F}_{p^k}$, then $\phi$ is differentiation; therefore $\phi = 0$.

C) Computation of $\Lambda_{O}$, when $O$ is the ring of integers of a local nonarchimedean field. From now on, $O$ will be the ring of integers of a local nonarchimedean field $K$, $\pi$ will be a prime element of $O$, $p$ the characteristic of $O / (\pi)$ and $q$ the order of $O / (\pi)$.

Proposition 1.3. $\widetilde{\Lambda}_O^{n - 1}\simeq O$ . More precisely:

1) If $n$ is not a power of $q$, then $b(a) = (a^n - a)u$ and $\alpha C_n(x, y) = u[(x + y)^n - x^n - y^n]$, where $u$ is a generator of $\widetilde{\Lambda}_O^{n-1}$.

2) If $n = q^k$, then $h(a) = (a^n - a)u / \pi$ and $\alpha = pu / \pi$, where $u$ is a generator of $\widetilde{\Lambda}_O^{n-1}$.

Proof. 1) If $n$ is not a power of $p$, then $b(a)$ can be expressed through $a$ by

using formula (1). If $n$ is a power of $p$, but not a power of $q$, then there exists $a \in O$ such that $a^n - a \notin (\pi)$: from (3) it follows that $(a^n - a)b(b) = (b^n - b)b(a)$; $\alpha$ can be determined from (2).

2) Let $n$ be a power of $q$. There exists an epimorphism $\widetilde{\Lambda}_O^{n-1} \to O$ sending $b(a)$ to $(a^n - a)/\pi$, and $a \mapsto f/\pi$. It remains to prove that $\widetilde{\Lambda}_O^{n-1}$ is generated by $b(\pi)$. Let $M = \widetilde{\Lambda}_O^{n-1}/\{b(\pi)\}$. If $x \in \widetilde{\Lambda}_O^{n-1}$, then we denote by $\overline{x}$ the image of $x$ in $M$. Since

$b(\pi^{b}) = \pi b(b) = \pi^{n}b(b)$, then $\overline{b}(\pi b) = 0$ for any $b \in O$. In particular, $\overline{b}(p) = 0$. But $h(p) = (p^{n-1} - 1)\alpha$, and so $\overline{\alpha} = 0$. Then $M$ is an $O/(\pi)$-module, and $\overline{b} \colon O/(\pi) \to M$ is differentiation. Therefore $\overline{b} = 0$, i.e. $M = 0$.

Proposition 1.4. $\Lambda_O \simeq O[g_1, g_2, \ldots]$, $\deg g_i = i$.

Proof. It follows from Proposition 1.3 that there exists an epimorphism $O[g_1, g_2, \ldots] \to \Lambda_O$ consistent with the gradation. Proposition 1.2 implies that $\Lambda_0 \otimes K \simeq K[c_1, c_2, \ldots]$ and $\deg c_i = i$. Therefore the epimorphism we have constructed is an isomorphism. $\square$

Corollary. 1) Every germ of a formal O-module arises from a formal O-module.

2) If $B \to C$ is an epimorphism of O-algebras, then every formal O-module over $C$ arises from an O-module over $B$.

Proposition 1.5. 1) Let $(F, f)$ and $(G, g)$ be formal O-modules over $B$, and let $(F, f) \equiv (G, g) \mod \deg n$.

a) If $n$ is not a power of $g$, then

$$
F (x, y) \equiv G (x, y) + v [ (x + y) ^ {n} - x ^ {n} - y ^ {n} ] \mod \deg (n + 1),
$$

$$
f _ {a} (x) \equiv g _ {a} (x) + v \left(a ^ {n} - a\right) x ^ {n} \bmod \deg (n + 1), v \in B;
$$

b) If $n$ is a power of $q$, then

$$
F (x, y) \equiv G (x, y) + h \frac {p}{\pi} C _ {n} (x, y) \mod \deg (n + 1),
$$

$$
f _ {a} (x) \equiv g _ {a} (x) + h \frac {a ^ {n} - a}{\pi} x ^ {n} \mod \deg (n + 1), h \in B.
$$

2) Let

$$
\varphi \in B [ [ x ] ], \varphi (x) \equiv x - v x ^ {n} \mod \deg (n + 1),
$$

$$
G (\varphi (x), \varphi (y)) = \varphi (F (x, y)), g _ {a} (\varphi (x)) = \varphi (f _ {a} (x)).
$$

Then

$$
F (x, y) \equiv G (x, y) + v [ (x + y) ^ {n} - x ^ {n} - y ^ {n} ] \mod \deg (n + 1),
$$

$$
f _ {a} (x) \equiv g _ {a} (x) + v (a ^ {n} - a) x ^ {n} \bmod \deg (n + 1).
$$

Proof. Statement 1 is a reformulation of Proposition 1.3, and statement 2 can be checked directly. □

Corollary. The formal O-module $(F, f)$ is isomorphic to an additive module if and only if the coefficients of $f_{\pi}$ are divisible by $\pi$.

D) Classification of formal O-modules over fields of "finite characteristic."

A homomorphism of formal O-modules is a homomorphism of formal groups that commutes with the action of O.

Let $E$ be a field over $O / (\pi)$ and let $\phi$ be a homomorphism of formal $O$-modules over $E$. It is known [7] that if $\phi \neq 0$, then $\phi(x) = \psi(x^{p^k})$ and $\psi'(0) \neq 0$. Since $\phi$ commutes with the action of $O$, it follows that $\log_p q|k$. The number $k / \log_p q$ is called the height of $\phi$; the height of the zero homomorphism is $\infty$. The height of a formal $O$-module is the height of the endomorphism of multiplication by $\pi$.

Remark. If  $O'$  is the integral closure of O in a finite extension of K and  $n = [O': O]$ , then every formal  $O'$ -module is also an O-module, and its O-height is n times its  $O'$ -height.

Proposition 1.6. 1) There exist modules of arbitrary height.

2) There exist nonzero homomorphisms only between modules of the same height.

3) A formal O-module of height $h$ is isomorphic to the additive module mod $\deg q^h$.

Proof. 1) We consider a homomorphism $\lambda: \Lambda_0 \simeq O[g_1, g_2, \ldots] \to E$ such that $\lambda(g_{q^b - 1}) \neq 0$ and $\lambda(g_i) = 0$ for $i < q^b - 1$. To this corresponds a formal $O$-module over $E$ of height $b$.

2) This follows from the fact that the height of the composition of homomorphisms equals the sum of their heights.

3) This follows from Proposition 1.5. $\square$

Proposition 1.7. 1) All formal O-modules of height $h < \infty$ over a separably closed field $E$ are isomorphic.

2) The ring of endomorphisms of such a module is isomorphic to the ring of integers of a central division algebra over K with invariant 1/h.

Proof. A formal O-module  $(F, f)$  will be called normal if the following conditions are satisfied:

1) $f_{\pi}(x) = x^{q^b}$,

2) $F \in \mathbf{F}_{ab}[[x, y]], f_a \in \mathbf{F}_{ab}[[x]$ for $a \in O$,

3) $F(x, y) \equiv x + y \mod \deg q^b$; $f_{\alpha}(x) \equiv ax \mod \deg q^b$.

a) Every formal $O$-module over $E$ of height $b$ is isomorphic to a normal one. Indeed, as in [7], by means of a change of variables we will have $f_{\pi}(x) \equiv x^{q^b}$. Then conditions 1) and 2) will be satisfied. By Proposition 1.6 we perform a change of variables with coefficients from $\mathbf{F}_{q^b}$, after which condition 3) is satisfied (and, as before, conditions 1) and 2)).

b) With the help of Proposition 1.5 it can be shown that between any two normal formal O-modules of height b there exists an isomorphism which is the identity mod  $\deg(q^{b} + 1)$ .

c) Let $L$ be the ring of endomorphisms of a normal formal $O$-module of height $b$. Clearly, $O \subset L$, $L$ contains no divisors of zero, and $L$ is complete in the $\pi$-adic topology. It follows from b) that every germ of an endomorphism of our module mod $\deg q^b$ with coefficients from $\mathbf{F}_{a^b}$ arises from an endomorphism. Therefore

it follows that $\dim L / \pi L = b^2$, and that the center of $L / \pi L$ coincides with $O / (\pi)$. Therefore $L \otimes K$ is a central division algebra of dimension $b^2$. The height is a norm on $L \otimes K$, and so $L$ is a maximal order in $L \otimes K$. It follows from the relation $\tau^{\log p^q} a = a^q \tau^{\log p^q}$ that the invariant of $L \otimes K$ equals $1 / b$.

## §2. Elliptic modules (algebraic approach)

A) Definitions and notation. Let $B$ be a ring of characteristic $p$. We denote by $\tau$ the endomorphism of the (algebraic) additive group over $B$ that sends $t$ to $t^p$ (just as in §1). We shall identify the element $b \in B$ with the endomorphism of multiplication by $b$. Every endomorphism of the (algebraic) additive group over $B$ has the form $\sum_0^n b_i \tau^i$, and, moreover, $\tau b = b^p \tau$. We denote the ring of such “polynomials” by $B\{\tau\}$. We have two homomorphisms: $\epsilon: B \to B\{\tau\}$, $\epsilon(b) = b$, and $D: B\{\tau\} \to B$, $D(\sum_0^n b_i \tau^i) = b_0$.

The following notation will be used throughout this paper. $k$ is a global field of characteristic $p; \infty$ is a fixed place of $k$; $k_{\nu}$ is the completion of $k$ corresponding to the place $\nu$; $|_{\nu}$ is the normed absolute value corresponding to $\nu$ (or its continuation to a finite extension $k_{\nu}$); we write $|_{\nu}$ for $|_{\infty}$; $A = \{x \in k | |x|_{\nu} \leq 1 \text{ for } \nu \neq \infty\}$; if $\nu \in \operatorname{Spec} A$, then $A_{\nu}$ is the completion of $A$ at $|_{\nu}$.

Let $K$ be a field over $A$ (i.e. there is defined $i: A \to K$). We call the place $i^*(\operatorname{Spec} K) \in \operatorname{Spec} A$ (i.e. the ideal $\operatorname{Ker} i$) the “characteristic” (notation: “char”). Thus $i$ is an imbedding if and only if $K$ has general “characteristic.”

Definition. An elliptic $A$-module over $K$ is a homomorphism $\phi: A \to K\{\tau\}$ such that $i = D \circ \phi$ and $\phi \neq \epsilon \circ i$.

B) Rank and places of finite order. We define a mapping $\deg: K\{\tau\} \to \mathbf{Z}$ in the following way: $\deg \sum_{0}^{n} a_{i} r^{i} = p^{n}$ for $a_{n} \neq 0$; $\deg 0 = 0$.

Proposition 2.1. a) $\phi$ is an imbedding.

b) There exists $d > 0$ such that $\deg \phi(a) = |a|^d$ for $a \in A$.

Proof. a) If $\operatorname{Ker} \phi \neq 0$, then $\operatorname{Ker} \phi$ would be a maximal ideal (since $K\{\tau\}$ has no divisors of zero), and so $\operatorname{Im} \phi$ would be a field, i.e. $\operatorname{Im} \phi \subset \epsilon(K)$ and so $\phi = \epsilon \circ i$.

b) Clearly

$\deg \dot{\varphi}(ab) = \deg \varphi(a) \cdot \deg \varphi(b), \quad \deg \varphi(a + b) \leqslant \max(\deg \varphi(a), \deg \varphi(b)), \deg \phi(a) = 0$ if and only if $a = 0$, $\deg \phi(a) \geq 1$ for $a \neq 0$, and $\deg \phi(a) > 1$ for some $a \in A$. Therefore $\deg \circ \phi$ extends to a nontrivial absolute value on $k$, which cannot correspond to a finite place.

Definition. d is called the rank of the elliptic A-module  $\phi$ .

Example. Let $A = \mathbf{F}_q[x]$. Then $\phi|_{\mathbf{F}_q} = \epsilon \circ i|_{\mathbf{F}_q}$. The representation of $\phi$ is equivalent to the representation of $\phi(x) \in K\{\tau\}$. In place of $\phi(x)$ one can take any element of the form $(x) + \sum_{j=1}^{d} a_j r^{j \log p q}$, where $d \geq 1, a_d \neq 0, a_j \in K$. The rank of such a module equals $d$.

The representation of an elliptic A-module over K changes any K-algebra into an A-module. Let K be the algebraic closure of K.

Proposition 2.2. Let $K$ be a divisible $A$-module. If $a \in A$, $a \neq 0$, then the number

of points of order $a$ in $K$ does not exceed $|a|^d$, where $d$ is the rank of the elliptic $A$-module. Equality holds if and only if $i(a) \neq 0$. The torsion submodule in $\overline{K}$ is isomorphic to $\bigoplus_{\nu \in \operatorname{Spec} A}(K_{\nu} / A_{\nu})^{j\nu}$, where $j_\nu < d$ for $\nu \neq \text{"char"} K$.

Proof. Every divisible torsion $A$-module is isomorphic to $\bigoplus_{\nu \in \operatorname{Spec} A}(K_{\nu} / A_{\nu})^{1\nu}$, where the $j_{\nu}$ are found by counting the number of places of order $a$.

Corollary. The rank of an elliptic A-module is a natural number.

Remark. Since $K\{\tau\} \subset K\{\{\tau\}\}$, every elliptic $A$-module over $K$ defines a formal $A$-module over $K$. If $K$ has general characteristic, then every formal $A$-module over $K$ uniquely extends to a formal $k$-module. If “char” $K = v \in \operatorname{Spec} A$, then every formal $A$-module over $K$ is uniquely extended from an $A_v$-module. The height of the formal $A_v$-module corresponding to the elliptic $A$-module is equal to $d - j_v$.

C) Isogenies. Let $\phi: A \to K\{\tau\}$ and $\psi: A \to K\{\tau\}$ be elliptic $A$-modules over $K$. A homomorphism from $\phi$ to $\psi$ is an element $\alpha \in K\{\tau\}$ such that $\alpha \phi(a) = \psi(a)\alpha$ for $a \in A$. A nonzero homomorphism is called an isogeny.

Remark. By comparing powers, it follows that isogenies exist only between modules of the same rank.

Every homomorphism of elliptic A-modules is also a homomorphism of their additive groups, and so one can consider the kernel of a homomorphism of elliptic modules.

The kernel of an isogeny is a finite A-invariant group subscheme in the additive group.

Proposition 2.3. Let $\phi$ be an elliptic $A$-module. For a finite group subscheme $H$ of the additive group, invariant with respect to $A$, to be the kernel of an isogeny from $\phi$ to some other module, it is necessary and sufficient that

a) if $K$ has general "characteristic", then $H$ must be reduced;

b) if  $\nu = "char"$$K \in Spec A$  and q is the order of the residue field of v, then  $H_{loc} = Spec K[t]/(t^{qb})$ , where  $H_{loc}$  is the connected component of H.

Proof. An additive group is obtained by factoring the additive group by $H$. Let $u \in K\{\tau\}$ be a homomorphism whose kernel is $H$. Since $H$ is invariant with respect to $A$, there exists a unique homomorphism $\psi: A \to K\{\tau\}$ such that $u\phi(a) = \psi(a)u$ for $a \in A$. Clearly $\psi \neq \epsilon \circ i$, and $D(\psi(a)) = [i(a)]^n$, where $n$ is the order of $H_{\mathrm{loc}}$. Therefore, for $\psi$ to be an elliptic module, it is necessary and sufficient that $i(a^n) = i(a)$ for $a \in A$.

Corollary. Any isogeny can be multiplied by another isogeny to an endomorphism which is multiplication by  $a \in A$ ,  $a \neq 0$ .

Proposition 2.4. Let X and Y be elliptic A-modules of rank d over K. Then $\operatorname{Hom}(X, Y)$ is a projective A-module of finite dimension (not exceeding $d^2$). If $v \in \operatorname{Spec} A$, $v \neq$ "char" K, then the homomorphism $\operatorname{Hom}(X, Y) \otimes_A A_v \to \operatorname{Hom}_{A_v}(T_v X, T_v Y)$ is injective (here $T_v X$ is the v-component of the torsion submodule of K), and its cokernel is torsion-free.

Proof (cf. [2]). 1) $\operatorname{Hom}(X, Y)$ is a torsion-free $A$-module. If $u, w \in \operatorname{Hom}(X, Y)$, then

$\deg (u + w)\leq \max (\deg u,\deg w)$ and $\deg (au) = |a|^d\deg u,\deg u\geq 1$ for $u\neq 0$. Therefore, if $V\subset \operatorname {Hom}(X,Y)\otimes_Ak$ is a finite-dimensional subspace, then $V\cap \operatorname {Hom}(X,Y)$ is a module of finite type.

2) Let $a \in A$ such that $|a|_{\nu} < 1$ and $|a|_{w} = 1$ for $w \neq \nu, \infty$. Then the homomorphism $\operatorname{Hom}(X, Y)/(a^k) \to \operatorname{Hom}_{A_\nu}(T_\nu X, T_\nu Y)/(a^k)$ is injective, and so $\varprojlim \operatorname{Hom}(X, Y)/(a^k) \hookrightarrow \operatorname{Hom}_{A_\nu}(T_\nu X, T_\nu Y)$. On the other hand, $\operatorname{Hom}(X, Y) \otimes_A A_\nu \to \varprojlim \operatorname{Hom}(X, Y)/(a^k)$ is a monomorphism.

Corollary. Let X be an elliptic A-module of rank d over K. Then End X is a projective module, dim End  $X \leq d^{2}$ , and End  $X \otimes_{A} k_{\infty}$  is a division ring. If K has general “characteristic”, then End X is commutative and dim End  $X \leq d$ .

## §3. Elliptic modules (analytic approach)

Let $L$ be a finite extension of $k_{\infty}$, and let $L^s$ be the separable closure of $L$. A lattice over $L$ is a finitely-generated discrete $A$-submodule in $L^s$, invariant with respect to $\operatorname{Gal}(L^s / L)$. Let $\Gamma_1$ and $\Gamma_2$ be lattices over $L$ of dimension $d$. A morphism from $\Gamma_1$ into $\Gamma_2$ is a number $\alpha \in L$ such that $\alpha \Gamma_1 \subset \Gamma_2$. Composition of morphisms is defined by multiplication of numbers.

Proposition 3.1. The category of elliptic modules of rank d over L is isomorphic to the category of lattices of dimension d over L.

Proof. 1) Let $L$ be a lattice of dimension $d$ over $L$. We set

$$
f(z) = z\prod_{\substack{a\in \Gamma \\ a\neq 0}}\left(1 - \frac{z}{a}\right).
$$

(This product clearly converges uniformly in every circle, since $f$ is an entire function.) First we prove the following lemma.

Lemma. Let $E$ be a field, char $E = p$, and let $\Delta$ be a finite subgroup of $E$. Let $g(z) = \prod_{\alpha \in \Delta} (z - \alpha)$. Then $g(z + w) = g(z) + g(w)$.

Proof. Clearly $g(z + w) - g(z) - g(w) = 0$ for $z \in \Delta$ or $w \in \Delta$. Therefore $g(z)g(w)$ divides $g(z + w) - g(z) - g(w)$. Comparing powers, we obtain $g(z + w) = g(z) + g(w)$.

Since $\Gamma$ is the union of an increasing sequence of finite subgroups, we see that $f(z + w) = f(z) + f(w)$. Clearly $f$ induces a group isomorphism $\overline{L} / \Gamma \simeq \overline{L}$. Since $\Gamma$ is an $A$-module, the structure of an $A$-module passes over from $\overline{L} / \Gamma$ to $\overline{L}$. If $a \in A$ and $a \neq 0$ then $f(az)$ and $\prod_{\beta \in (1/a)\Gamma / \Gamma}(f(z) - f(\beta))$ are analytic functions of $z$ with the same divisors. Therefore $f(az) = P_a(f(z))$, where $P_a$ is a polynomial of degree $|a|^d$.

2) Let $\phi$ be an elliptic $A$-module of rank $d$ over $L$. There is a corresponding formal $k$-module over $L$ (cf. the remark at the end of §2B). According to Proposition 1.2, there exists a unique $f = 1 + \sum_{1}^{\infty} b_i r^i \in L \{\{\tau\}\}$ such that $fa = \phi(a)f$ for $a \in A$. We shall prove that the formal homomorphism $f$ is an analytic homomorphism. Let $a \in A$, $|a| > 1$ and $\phi(a) = a + \sum_{1}^{s} a_j r^j$. Let $i > s$. From the identity $fa = \phi(a)f$ we obtain

$$
(a ^ {i} - a) b _ {i} = \sum_ {j = 1} ^ {s} a _ {j} b _ {i - j} ^ {p j}.
$$

Let $c_{i} = |b_{i}|^{p - i}$. Then $|a|c_{i} \leq \max_{1 \leq j \leq s} (|a_{j}|^{p - i}c_{i - j})$. Let $1 / |a| < \theta < 1$, and $c_{i} \leq \theta \cdot \max_{1 \leq j \leq s} c_{i - j}$ for sufficiently large $i$. Therefore $c_{i} \to 0$. Let $\Gamma \subset \overline{L}$ be the kernel of $f$. Clearly $\Gamma \subset L^{s}$, $\Gamma$ is invariant with respect to $\operatorname{Gal}(L^{s}/L)$, $\Gamma$ is an $A$-module, and $(1/a)\Gamma/\Gamma \simeq (A/(a))^{d}$. Since $\Gamma$ is discrete, $\Gamma$ is a lattice over $L$ of dimension $d$.

3) Let $\Gamma_{1}$ and $\Gamma_{2}$ be lattices of dimension $d$ over $L$, $\alpha \in L$, and $\alpha \Gamma_{1} \subset \Gamma_{2}$. Let $f_{1}$ and $f_{2}$ be the entire functions constructed in 1) from the lattices $\Gamma_{1}$ and $\Gamma_{2}$. The function $f_{2}(\alpha z)$ is invariant with respect to $\Gamma_{1}$. Repeating the discussion from step 1), we get $f_{2}(\alpha z) = P(f_{1}(z))$, where $P$ is a polynomial. $P$ defines a homomorphism of elliptic $A$-modules. On the other hand, let the polynomial $P$ define a homomorphism of elliptic $A$-modules. Then $P \circ f_{1}$ is a formal homomorphism from an additive $k$-module into a formal $k$-module corresponding to the second elliptic $A$-module. It follows from Proposition 1.2 that $P(f_{1}(z)) = f_{2}(\alpha z)$ for a uniquely defined $\alpha \in L$. Clearly, $\alpha \Gamma_{1} \subset \Gamma_{2}$.

Corollary. For any $A$ and $d$ there exist elliptic $A$-modules of rank $d$ over $k_{\infty}^{s}$.

## §4. Universal deformations of formal modules

A) Deformations of zero level (cf. [13]). We shall use the same notation as in §1C. Let $O^{nr}$ be a maximal unramified extension of $O$, and let $\hat{O}^{nr}$ be the completion of $O^{nr}$. We consider the category $C$ whose objects are complete local $\hat{O}^{nr}$-algebras whose residue fields are isomorphic to $\hat{O}^{nr}/(\pi)$. The morphisms of $C$ are local homomorphisms of $\hat{O}^{nr}$-algebras.

Let $(G, g)$ be a formal $O$-module over $\hat{O}^{nr}/(\pi)$, and let $R \in C$. A deformation of the module $(G, g)$ with basis $R$ is a formal $O$-module $(F, f)$ over $R$ whose reduction modulo a maximal ideal is $(G, g)$.

Proposition 4.1. Let $(F, f)$ and $(F', f')$ be deformations of the modules $(G, g)$ and $(G', g')$ with basis $R$. Let $\phi: (F, f) \to (F', f')$ be a homomorphism inducing the zero homomorphism $(G, g) \to (G', g')$. If the height of $(G, g)$ is finite, then $\phi = 0$.

Proof. Let $m \subset R$ be a maximal ideal. It suffices to consider the case when $m^{r+1} = 0$ and $\phi \equiv 0 \mod m^r$, $r \geq 1$. Then $F'(\phi(x), \phi(y)) = \phi(x) + \phi(y)$, $f_a'(\phi(x)) = a\phi(x)$, and so $\phi(F(x, y)) = \phi(x) + \phi(y)$ and $\phi(f_a(x)) = a\phi(x)$. Let $l: m^r \to R/m$ be a linear function, $\phi' = l(\phi)$. Then $\phi'$ is a homomorphism from $(G, g)$ into an additive $O$-module, and so $\phi' = 0$.

Deformations $(F_{1}, f_{1})$ and $(F_{2}, f_{2})$ of the module $(G, g)$ are called isomorphic if there exists an isomorphism $(F_{1}, f_{1}) \cong (F_{2}, f_{2})$ inducing the identity automorphism on $(G, g)$. (If $(G, g)$ has finite height, then such an isomorphism is unique.)

Proposition 4.2. Let $(G, g)$ be a formal $O$-module over $\hat{O}^{nr}$ of finite height $h$. The functor that associates to $R \in C$ the set of deformations of the module $(G, g)$ up to isomorphism is represented by the algebra $\hat{O}^{nr}[[t_1, \ldots, t_{b-1}]]$.

Proof. Let $O[g_1, g_2, \ldots] = \Lambda_O \to \hat{O}^{nr} / (\pi)$ be the homomorphism corresponding to $(G, g)$. We can assume that under this homomorphism $g_i \to 0$ for $i < q^b - 1$. Let

$(F^0, f^0)$ be a deformation of $(G, g)$ with basis $\hat{O}^{nr}[[t_1, \ldots, t_{b-1}]]$ such that the corresponding homomorphism $\Lambda_O \to \hat{O}^{nr}[[t_1, \ldots, t_{b-1}]]$ sends $g_i$ into $t_i$ for $1 \leq i \leq b-1$ and $g_j$ into zero for $j < q^b - 1$, $j \neq q^i - 1$. We shall show that $(F^0, f^0)$ is a universal deformation.

Let $M$ be a vector space over $\hat{O}^{nr}/(\pi)$. A 2-dimensional cocycle of the module $(G, g)$ with coefficients in $M$ is a set $\{\Delta \in M[[x, y]], \delta_a \in M[[x]] \text{ for } a \in O\}$ such that

$$
\Delta (y, z) + \Delta (x, G (y, z)) = \Delta (x, y) + \Delta (G (x, y), z), \quad \Delta (x, y) = \Delta (y, x),
$$

$$
\delta_ {a} (x) + \delta_ {a} (y) + \Delta \left(g _ {a} (x), g _ {a} (y)\right) = a \Delta (x, y) + \delta_ {a} (G (x, y)),
$$

$$
\delta_ {a} (x) + \delta_ {b} (x) + \Delta \left(g _ {a} (x), g _ {b} (x)\right) = \delta_ {a + b} (x), \quad a \delta_ {b} (x) + \delta_ {a} \left(g _ {b} (x)\right) = \delta_ {a b} (x).
$$

A coboundary of the series $\psi \in M[[x]]$ is a cocycle $(\Delta, \delta)$, where

$$
\Delta (x, y) = \psi (G (x, y)) - \psi (x) - \psi (y), \delta_ {a} (x) = \psi (g _ {a} (x)) - a \psi (x).
$$

Let $R \in C$, $m \subset R$ a maximal ideal, $m^{r+1} = 0$, $r > 1$, and $(F, f)$ a deformation of the module $(G, g)$ with basis $R$.

Lemma. 1) The exists a one-to-one correspondence between formal O-modules $(F^{\prime}, f^{\prime})$ over $R$ that are congruent to $(F, f)$ modulo $m^r$ and 2-dimensional cocycles of the module $(G, g)$ with coefficients in $m^r$. To the cocycle $(\Delta, \delta)$ corresponds the module $(F^{\prime}, f^{\prime})$, where $F^{\prime}(x, y) = F(F(x, y), \Delta(x, y))$, $f_a'(x) = F(f_a(x), \delta_a(x))$.

2) Two cocycles with coefficients in  $m^{r}$  are cohomologous if and only if the corresponding deformations are isomorphic.

Proof. If $(F', f') \equiv (F'', f'') \mod m'$, then the isomorphism of the deformations $(F', f')$ and $(F'', f'')$ is the identity mod $m'$ (by Proposition 4.1). The remaining assertions can be verified directly. $\square$

Let $\phi: \hat{O}^{nr}[[t_1, \ldots, t_{b-1}]] \to R$ be a homomorphism such that $\phi(F^0, f^0) \equiv (F, f) \mod m^r$. For the proof of the proposition it suffices to show the existence and uniqueness of a homomorphism $\psi: \hat{O}^{nr}[[t_1, \ldots, t_{b-1}]] \to R$ such that $\psi \equiv \phi \mod m^r$ and $\psi_*(F^0, f^0) \approx (F, f)$. Let $\psi: \hat{O}^{nr}[[t_1, \ldots, t_{b-1}]] \to R$ be a homomorphism such that $\psi(t_i) = \phi(t_i) + \epsilon_i, \epsilon_i \in m^r$. Then the difference between the cocycles corresponding to $\phi_*(F^0, f^0)$ and $\psi_*(F^0, f^0)$ has the form $\Sigma_{i=1}^{b-1} \epsilon_i(\Delta_i, \delta_i)$, where $(\Delta_i, \delta_i)$ is a cocycle with coefficients in $\hat{O}^{nr}/(\pi)$ (which depends neither on $\epsilon_i$ nor on $r$). Then

$$
\left(\Delta_ {i}, \delta_ {i}\right) \equiv 0 \bmod \deg q ^ {i}, \left(\Delta_ {i}, \delta_ {i}\right) \not \equiv 0 \bmod \deg \left(q ^ {i} + 1\right).
$$

It remains to show that the classes  $(\Delta_{i}, \delta_{i})$  form a basis for the cohomology with coefficients in  $\hat{O}^{nr}/(\pi)$ . This follows from the following two assertions (the first is clear, and the second was essentially proved in §1B).

a) The coboundary $x^n$ is congruent to

$$
\{(x + y) ^ {n} - x ^ {n} - y ^ {n}, (a ^ {n} - a) x ^ {n} \} \mod \deg (n + 1),
$$

The coboundary $x^{q^i}$ is congruent to

$$
\left\{h _ {i} \frac {p}{\pi} C _ {q ^ {i + h}} (x, y), h _ {i} \frac {a ^ {q ^ {i + h}} - a}{\pi} x ^ {q ^ {i + h}} \right\} \mod \deg (q ^ {i + h} + 1), h _ {i} \neq 0.
$$

b) Let $(\Delta, \delta)$ be a cocycle, and let $(\Delta, \delta) \equiv 0 \mod \deg n$. If $n$ is not a power of $q$, then

$$
(\Delta , \delta) \equiv \{v [ (x + y) ^ {n} - x ^ {n} - y ^ {n}, v (a ^ {n} - a) x ^ {n} \} \mod \deg (n + 1).
$$

If $n$ is a power of $q$, then

$$
(\Delta , \delta) \equiv \left\{h \cdot \frac {p}{\pi} C _ {n} (x, y), h \cdot \frac {a ^ {n} - a}{\pi} x ^ {n} \right\} \mod \deg (n + 1).
$$

B) Deformations of arbitrary level. Let $R \in C$, and let $m \subset R$ be a maximal ideal. The assignment of a formal $O$-module $(F, f)$ over $R$ turns $m$ into an $O$-module. Let the reduction of $(F, f)$ modulo $m$ have finite height $b$. Let $n \in \mathbf{Z}$, $n \geq 0$.

Definition. A structure of level $n$ on a formal $O$-module $(F, f)$ is an $O$-module homomorphism $\phi: ((1 / \pi^n)O / O)^b \to m$ such that $f_{\pi}(x)$ is divisible by

$$
\prod_ {\alpha \in \left(\frac {1}{\pi} O / O\right) ^ {h}} (x - \varphi (\alpha)).
$$

For $n \geq 1$ it follows that $f_{\pi}(x)$ and $\Pi_{\alpha \in ((1 / \pi)O/O)b}(x - \phi(\alpha))$ divide each other. In the case $R = \hat{O}^{n\tau}/(\pi)$ there exists exactly one structure of level $n$. Let $(G, g)$ be a formal $O$-module over $\hat{O}^{n\tau}/(\pi)$ of finite height $b$. A deformation of the module $(G, g)$ with structure of level $n$ will be called a deformation of level $n$.

Proposition 4.3. 1) The functor that associates to $R \in C$ the set of deformations of level $n$ of the module $(G, g)$ up to isomorphism is represented by some ring $D_n$. 2) $D_n$ is a regular ring. Let $n \geq 1$, and let $e_i$ ($i = 1, \ldots, h$) be a basis for $((1/\pi^n)O/O)^h$ as an $O/(\pi)^n$-module. The images of $e_i$ in $D_n$ under the universal deformation of level $n$ form a system of local parameters.

3) Let $m \leq n$. The homomorphism $D_m \to D_n$ is finite and flat.

Proof. a) Let $(F, f)$ be a universal deformation with basis $D_0 \simeq \hat{O}^{nr}[[t_1, \ldots, t_{h-1}]]$. Let $0 \leq r \leq h$. Consider the functor $\Phi_r$ that associates to each $D_0$-algebra $R \in C$ the set of homomorphisms $\phi$ from $((1/\pi)O/O)^r$ into a maximal ideal of $R$ such that $f_\pi(x)$ is divisible by

$$
\prod_ {\alpha \in \left(\frac {1}{\pi} O / O\right) ^ {r}} (x - \varphi (\alpha)).
$$

Lemma. $\Phi_r$ is represented by a ring $L_r$ having the following properties: 1) $L_r$ is a regular ring. Let $e_i (i = 1, \ldots, r)$ be a basis for $((1/\pi)O/O)^r$. Then the images of $e_i$ in $L_r$ and also $t_r, \ldots, t_{b-1}$ form a system of local parameters. 2) The homomorphism $L_{r-1} \to L_r$ is finite and flat.

Proof. For $r = 0$ the lemma is true. Suppose that $r \geq 1$ and that the lemma has been proved for $\Phi_{r-1}$. Let $\phi_{r-1}: ((1/\pi)O/O)^{r-1} \to L_{r-1}$ be the homomorphism mentioned in the definition of $\Phi_{r-1}$. We set $\theta_i = \phi_{r-1}(e_i) (1 \leq i \leq r-1)$ and

$$
g (x) = \frac {f _ {\pi} (x)}{\prod_ {\alpha \in \left(\frac {1}{\pi} O / O\right) ^ {r - 1}} \left(x - \varphi_ {r - 1} (\alpha)\right)}.
$$

Let $L_{r} = L_{r-1}[[\theta_r]]/g(\theta_r)$. We define a homomorphism

$$
\varphi_ {r}: \left(\frac {1}{\pi} O / O\right) ^ {r - 1} \oplus \left(\frac {1}{\pi} O / O\right)\rightarrow L _ {r}
$$

so that the restriction of $\phi_r$ to the first summand coincides with $\phi_{r-1}$ and the restriction of $\phi_r$ to the second summand sends $1/\pi$ into $\theta_r$. Clearly, $L_r$ is finite and flat over $L_{r-1}$; furthermore,

$$
L _ {r} / \left(\theta_ {1}, \dots , \theta_ {r}, t _ {r}, \dots , t _ {h - 1}\right) = \hat {O} ^ {n r} / (\pi),
$$

and so  $L_{r}$  is regular, and  $\theta_{1},\ldots,\theta_{r},t_{r},\ldots,t_{b-1}$  form a system of local parameters. It remains to prove that  $L_{r}$  represents  $\Phi_{r}$ . It is enough to show that  $f_{\pi}(x)$  is divisible by

$$
\prod_ {a \in \left(\frac {1}{\pi}! O / O\right) ^ {r}} (x - \varphi_ {r} (a)).
$$

Indeed, $f_{\pi}(x)$ is divisible by $x - \phi_r(\alpha)$ for $\alpha \in ((1 / \pi)O / O)^r$. Since $L_r$ is regular, it remains to show that $\phi_r$ is injective. Indeed, if $\phi_r(\Sigma_1^r\alpha_i e_i) = 0$, then $\Sigma \alpha_i\theta_i$ belongs to the square of the maximal ideal of $L_r$, and so $\alpha_i \in (\pi)$.

Setting $r = b$, we obtain assertions 1)-3) for $n = 1$.

b) Suppose that $n \geq 1$ and that statements 1) and 2) about $D_{n}$ have been proved. Let $e_{i}(1 \leq i \leq b)$ be a basis for $((1 / \pi^{n})O / O)^{b}$, and let $b_{i}$ be the image of $e_{i}$ in $D_{n}$. Clearly

$$
D _ {n + 1} = D _ {n} \left[ \left[ y _ {1}, \dots , y _ {n} \right] \right] / \left(f _ {\pi} \left(y _ {1}\right) - b _ {1}, \dots , f _ {\pi} \left(y _ {h}\right) - b _ {h}\right).
$$

Therefore $D_{n+1}$ is regular, $(y_1, \ldots, y_b)$ is a system of local parameters in $D_{n+1}$, and the homomorphism $D_n \to D_{n+1}$ is finite and flat. □

Proposition 4.4. Let $(F, f)$ be a formal O-module over $R \in C$ with structure $\phi$ of level $n$. Let $P \subset ((1/\pi^n)O/O)^b$ be a submodule. Then

$$
H \stackrel {\text { def }} {=} \operatorname{Spf} R [ [ x ] ] / \prod_ {\alpha \in P} (x - \varphi (\alpha)) \subset \operatorname{Spf} R [ [ x ] ]
$$

is an O-invariant group subscheme, and the factor $G = F / H$ is a formal O-module. If

$$
\left(\frac {1}{\pi^ {m}} O / O\right) ^ {h} \rightarrow \left(\frac {1}{\pi^ {n}} O / O\right) ^ {h} / P
$$

is an imbedding, then the corresponding homomorphism from  $((1/\pi^{m})O/O)^{b}$  into the maximal ideal of R is a structure of level m.

Proof. It is enough to consider the case $R = D_n$ (cf. Proposition 4.3). Clearly $H$ is the minimal closed subscheme in $\operatorname{Spf} R[[x]]$ containing $\operatorname{Spf} R[[x]] / (x - \phi(\alpha))$ for all $\alpha \in P$. Since $F(\phi(\alpha), \phi(\beta)) = \phi(\alpha + \beta)$ and $\operatorname{Spf} R[[x]] / (x - \phi(\alpha + \beta))$ is contained in $H$

for $\alpha, \beta \in P$, it follows that $H$ is invariant under addition. Similarly it is proved that $H$ is invariant under the action of $O$. Since $\phi(\alpha) \neq 0$ for $\alpha \neq 0$, the homomorphism from $F$ to $G$ induces a nonzero tangent mapping. Since $D_n$ has no divisors of zero, $G$ is a formal $O$-module. Since the homomorphism from $((1/\pi^m)O/O)^b$ into the maximal ideal $D_n$ is injective, and $D_n$ is regular, it follows that this homomorphism is a structure of level $m$.

C) Deformations of divisible modules. In this section, a formal group will be a group object in the category of formal schemes. (For example, a discrete group is a formal group.) Let $R \in C$. A divisible O-module over $R$ is a formal group $F$ over $R$ together with a homomorphism $f \colon O \to \operatorname{End} F$ such that $F_{\text{loc}}$ is a formal O-module, and

$$
F / F _ {\mathrm{loc}} \simeq \operatorname{Spf} R \times (K / O) ^ {j}
$$

$(j < \infty)$. (For $R = \hat{O}^{nr} / (\pi)$, the sequence $0 \to F_{\mathrm{loc}} \to F \to F / F_{\mathrm{loc}} \to 0$ splits.)

Let the reduction of $F_{\mathrm{loc}}$ modulo the maximal ideal have finite height $h$. A structure of level $n$ on the divisible module $(F, f)$ is a homomorphism $((1 / \pi^n)O / O)^{j + b} \stackrel{\phi}{\to} \operatorname{Mor}(\operatorname{Spf} R, F)$, including a structure of level $n$ on $F_{\mathrm{loc}}$ and an epimorphism

$$
\left(\frac {1}{\pi^ {n}} O / O\right) ^ {j + h} \rightarrow \left(\frac {1}{\pi^ {n}} O / O\right) ^ {j} \subset F / F _ {\text { loc }}.
$$

The concept of a deformation of level n is introduced as for formal modules. Proposition 4.1 is easily generalized to the case of divisible modules.

Proposition 4.5. Let $(G, g)$ be a divisible $O$-module over $\hat{O}^{nr}/(\pi)$ with structure of level $n$ such that $G_{\mathrm{loc}}$ has height $h$, and $G/G_{\mathrm{loc}} \approx (K/O)^j$.

Let $n \in \mathbf{Z}$, $n \geq 0$. The functor that associates to $R \in C$ the set of deformations of level $n$ of the module $(G, g)$ with basis $R$ up to isomorphism is represented by the ring $E_n \simeq D_n[[d_1, \ldots, d_j]]$, where $D_n$ is defined as in Proposition 4.3. In particular, $E_n$ is a regular ring of dimension $j + b$, and $E_0$ is smooth over $\hat{O}^{nr}$. If $m \leq n$, then the homomorphism $E_m \to E_n$ is finite and flat.

Proof. Let $R \in C$, and let $(F, f)$ be a deformation of level $n$ of the formal module $G_{\mathrm{loc}}$. Clearly its extensions by a deformation of the divisible module $G$ are classified by the elements of $\operatorname{Exp}(\Gamma, \operatorname{Mor}(\operatorname{Spf} R, F))$, where $\Gamma$ is a factor of $G / G_{\mathrm{loc}}$ by elements of order $\pi^n$. If $M$ is a module over $O$, complete in the $\pi$-adic topology, then $M = \operatorname{Exp}(K/O, M)$. Therefore, fixing an isomorphism $\Gamma \approx (K/O)^j$, we can identify

$$
\operatorname{Exp} (\Gamma , \operatorname{Mor} (\operatorname{Spf} R, F))
$$

with  $[\mathrm{Mor}(\mathrm{Spf}\ R,\ F)]^{j}$ . □

Remark. Let $O'$ be the integral closure of $O$ in a finite extension of $K$. By $O^{nr}$ we mean the maximal unramified extension of $O$ in $O'^{nr}$. Let $(G, g)$ be a divisible $O'$-module such that $G_{\text{loc}}$ has finite height, and let $E'$ be the basis of a universal deformation (of level zero) of $(G, g)$. We can consider $(G, g)$ as an $O$-module; let $E$ be the basis of a universal deformation of the $O$-module $(G, g)$. Clearly the group of automorphisms of $(G, g)$ acts on $E$, and, in particular, $O'^*$ acts on $E$. It is easy to show that if $\Gamma \subset O'^*$ is a subgroup which generates $O'$ as an $O$-module, then $\operatorname{Spf} E' = (\operatorname{Spf} E)^{\Gamma}$.

## §5. Modular manifolds

A) Endomorphisms of the additive group.

Proposition 5.1. Let $B$ be a ring of characteristic $p$ with $\operatorname{Spec} B$ connected. Let $f_1, f_2 \in B\{\tau\}$, $f_j = \sum_{i=0}^{d_j} a_{ij}\tau^i$, $d_1 > 0$, $a_{d_jj}$ invertible for $j = 1, 2$. Let $b \in B\{\tau\}$ and $bf_1 = f_2b$. If $d_1 \neq d_2$, then $b = 0$.

2) If $d_1 = d_2$ and $b \neq 0$, then $b$ has the form $\sum_{i=0}^{d_3} b_i \tau^i$, and $b_{d_3}$ is invertible.

Proof. It suffices to consider the case when B is a local Artinian ring. We proceed by induction on the length of B.

1) Assume that the coefficients of $b$ are nilpotent. (This is also true if $d_1 \neq d_2$). We shall show that $b = 0$. Let $M \subset B$ be an ideal such that $m^2 = 0$ and $b = \sum_0^n b_i \tau^i$, $b_i \in m$. Then $bf_1 = f_2b = a_{02}b$. Since $d_1 > 0$, we have $b_n = 0$.

2) Let $d = d_2 = d$ and $h = \sum_{0}^{n} b_i r^i$; let $m \subset B$ be an ideal, $m^2 = 0$, $h_n \in m$. Equating the coefficients for $r^{d + n}$, we obtain $h_n = 0$.

Proposition 5.2. Let $B$ be a ring, char $B = p$. Let $f = \sum_{0}^{n} a_i \tau^i \in B\{\tau\}$, and let $d > 0$, with $a_d$ invertible and $a_i$ nilpotent for $i > d$. Then there exists a unique element of the form $1 + \sum_{1}^{m} \alpha_j \tau^j \in B\{\tau\}$ such that the $\alpha_j$ are nilpotent and

$$
\left(1 + \sum_ {j} \alpha_ {i} \tau^ {j}\right) f \left(1 + \sum_ {j} \alpha_ {j} \tau^ {j}\right) ^ {- 1}
$$

has degree d.

Proof. The uniqueness follows from Proposition 5.1.

Let $m \subset B$ be an ideal, $m^2 = 0$, $a_i \in m$ for $i > d$, and $n > d$. Then the degree of

$$
\left(1 - \frac {a _ {n}}{a _ {d} ^ {p ^ {n - 1}}} \tau^ {n - d}\right) f \left(1 - \frac {a _ {n}}{a _ {d} ^ {p ^ {n - 1}}} \tau^ {n - d}\right) ^ {- 1}
$$

is less than n. From this follows the existence. □

B) Construction of modular schemes.

Definition. Let $S$ be a scheme over $A$. An elliptic $A$-module over $S$ of rank $d$ is a line bundle $L$ over $S$ together with a homomorphism $\psi: A \to \operatorname{End} L$ (where $\operatorname{End} L$ is the ring of endomorphisms of $L$ as a group scheme over $S$) such that 1) for any $a \in A$ the differential of $\psi(a)$ is multiplication by $a$; and 2) for any field $K$ and morphism $\operatorname{Spec} K \to S$, the corresponding homomorphism $A \to K\{\tau\}$ is an elliptic module of rank $d$ in the sense of §1. A homomorphism of elliptic modules is a homomorphism of group schemes over $S$ that agrees with the action of $A$.

Remark. An elliptic module over $S$ is called standard if for every $a \in A$ the endomorphism $\psi(a)$ has the form $\sum_{i=0}^{d\log p|a|} b_i \tau^i$, where $b_i \in H^0(S, L^{1-p^i})$. According to Proposition 5.2, every elliptic module is isomorphic to a standard module, and every isomorphism of a standard module is linear.

Let $I \subset A$ be an ideal. We denote by $V(I)$ the set of simple ideals containing $I$. Let $X$ be an elliptic module over $S$ of rank $d$; let $I \neq 0$, and let $X_I \subset X$ be the annihilator of $I$. Clearly $X_I$ is a finite flat group scheme over $S$. If the image of $S$ in $\operatorname{Spec} A$ does not intersect $V(I)$, then $X_I$ is étale over $S$.

Definition. A structure of level $I$ on $X$ is a homomorphism of $A$-modules $\psi: (I^{-1}/A)^{d} \to \operatorname{Mor}(S, X)$ such that, for any $m \in V(I)$, $X_{m}$ as a divisor coincides with the sum of the divisors $\psi(\alpha)$, $\alpha \in m^{-1}/A$.

Remark. If the image of $S$ in $\operatorname{Spec} A$ does not intersect $V(I)$, then a structure of level $I$ is an isomorphism $(I^{-1} / A)^d \times S \cong X_r$.

Proposition 5.3. Let $I \subset A$ be an ideal such that $I \neq 0$ and $V(I)$ contains more than one element. The functor that associates to the scheme $S$ over $A$ the set of elliptic $A$-modules of rank $d$ with structure of level $I$ up to isomorphism is represented by a scheme $M_I^d$ of finite type over $A$.

Proof. Let $m \in V(I)$. It is enough to prove that the restriction of our functor to the category of schemes over $\operatorname{Spec} A - m$ is representable. Indeed, if $S$ is a scheme over $\operatorname{Spec} A - m$ and $X$ is an elliptic $A$-module of rank $d$ over $S$ with structure of level $I$, then a choice of nonzero elements $(m^{-1}/A)^d$ defines a trivialization of the bundle $X$.

C) Deformations of elliptic modules. Let $V \in \operatorname{Spec} A$ and $O = A_{\nu}$. The definition of the category $C$ was given in §4. Let $X$ be an elliptic module of rank $d$ over $\hat{A}_{\nu}^{nr} / \nu$ with structure of level $\nu^n$.

We consider the functor that associates to $R \in C$ the set of deformations of level $\nu^n$ of the module $X$ with basis $R$ up to isomorphism. This functor can be represented in the following way: Let $I \subset A$ be nonzero ideal, $V(I) \not\supseteq \nu$, $I \neq A$. We lift in any way the structure of level $\nu^n$ on $X$ to a structure of level $lv^n$. Let $y$ be the corresponding point in $M_{I\nu^n}^d \otimes A_\nu^{nr}$, and $F_n$ its completion at a local ring. Then $F_n$ represents our functor.

Let $R \in C$, and let $Y$ be an elliptic module over $R$. Then $\hat{Y} = \varinjlim Y_{\nu^n}$ is a divisible $A_{\nu}$-module. A structure of level $\nu^n$ on $Y$ defines a structure of level $n$ on $\hat{Y}$. Thus there is a homomorphism $E_n \to F_n$, where $E_n$ was defined in §4C).

Proposition 5.4. This homomorphism $E_{n} \to F_{n}$ is an isomorphism.

Proof. a) If $R \in C$ and $Y$ is an elliptic module over $R$, $\hat{Y} = \varinjlim_{\nu^n} Y_{\nu^n}$, then a structure of level $n$ on $\hat{Y}$ defines a structure of level $\nu^n$ on $Y$. Thus it suffices to prove the proposition for $n = 0$.

b) We reduce the proof to the case $A = \mathbf{F}_p[x]$, $v = (x)$. Let $x \in v$. We may consider an elliptic $A$-module as an $\mathbf{F}_p[x]$-module, and a divisible $A_v$-module as an $\mathbf{F}_p[[x]]$-module. Let $E_0'$ be a basis of the universal deformation of the $\mathbf{F}_p[[x]]$-module $\hat{X}$, and $F_0'$ a basis of the universal deformation of the $\mathbf{F}_p[x]$-module $X$. The diagram

$$
\begin{array}{c} E _ {0} \to F _ {0} \\ \uparrow \qquad \qquad \qquad \qquad \uparrow \\ E _ {0} ^ {\prime} \to F _ {0} ^ {\prime} \end{array}
$$

is commutative.

Let $A_x$ be the localization of $A$ by the set of elements of $A$ which are relatively prime to $x$. We define an action of $A_x^*$ on $F_0'$. Let $a \in A \cap A_x^*$, and let $Y$ be a deform-

tion of the elliptic $\mathbf{F}_p[x]$-module $X$ with $R \in C$. Then there exists a unique, up to isomorphism, deformation $Y'$ with basis $R$ for which the endomorphism $X \overset{a}{\to} X$ extends to a homomorphism $Y \to Y'$. ($Y'$ is obtained in the following way: Let $b \in \mathbf{F}_p[x]$, $b(0) \neq 0$, $a|b$. Since $Y_{(b)}$ is étale over $\operatorname{Spec} R$, the subscheme $X_{(a)} \subset X_{(b)}$ uniquely extends to a subscheme $H \subset Y_{(b)}$, étale and finite over $\operatorname{Spec} R$. Let $Y' = Y/H$.) Thus the subgroup $A_x^* \cap A$ acts on $F_0'$, and $A_x^* \cap \mathbf{F}_p[x]$ acts trivially. This allows us to define an action of $A_x^*$ on $F_0'$. It follows from Proposition 5.1 that $\operatorname{Spf} F_0 = (\operatorname{Spf} F_0')^{A_x^*}$. On the other hand (cf. §4C)), the group $A_x^* \subset A_v^*$ acts on $E_0'$, and $\operatorname{Spf} E_0 = (\operatorname{Spf} E_0')^{A_x^*}$. Thus the homomorphism $E_0' \to F_0'$ is consistent with the action of $A_x^*$. Since the bottom row of the commutative diagram is an isomorphism, so is the upper row.

c) It remains to clear up the case $n=0$, $A=\mathbf{F}_{p}[x]$, $\nu=(x)$. Suppose the elliptic $\mathbf{F}_{p}[x]$-module $X$ is defined by a homomorphism $\mathbf{F}_{p}[x]\to\overline{\mathbf{F}}_{p}\{\tau\}$, where $x\to\Sigma_{i=b}^{d-1}a_{i}\tau^{i}+\tau^{d}$, with $a_{b}\neq0$. Clearly, $F_{0}=\overline{\mathbf{F}}_{p}[[x,\alpha_{1},\ldots,\alpha_{d-1}]]$, and the universal deformation of the elliptic module $X$ has the form $x\mapsto x+\Sigma_{i=1}^{d-1}a_{i}\tau^{i}+\tau^{d}$. Since $E_{0}\approx F_{0}$, it suffices to show that a morphism $\operatorname{Spf}F_{0}\to\operatorname{Spf}E_{0}$ induces a monomorphism of tangent spaces. In other words, we must prove that if $\beta_{1},\ldots,\beta_{d-1}\in\overline{\mathbf{F}}_{p}$ and the deformation

$$
x \mapsto \sum_ {i = 1} ^ {d - 1} \beta_ {i} \varepsilon \tau^ {i} + \sum_ {i = h} ^ {d - 1} a _ {i} \tau^ {i} + \tau^ {d}
$$

with basis $\overline{\mathbf{F}}_p[x] / (\epsilon^2)$ induces the trivial deformation of the divisible module $\hat{X}$, then $\beta_i = 0$ for $1 \leq i \leq b - 1$. Indeed, it follows from the triviality of the deformation of the formal module $\hat{X}_{\mathrm{loc}}$ that $\beta_i = 0$ for $1 \leq i \leq b - 1$. Let $r \in \overline{\mathbf{F}}_p$ be a point of order $x$ of the module $X$. Then it follows from the triviality of the deformation $\hat{X}$ that

$$
\sum_ {i = h} ^ {d - 1} \left(a _ {i} + \beta_ {i} \varepsilon\right) r ^ {p ^ {i}} + r ^ {p ^ {d}} = 0.
$$

and so $\sum_{i=b}^{d-1} \beta_i r^{p^i} = 0$. Since $r$ can assume $p^{d-b}$ different values, it follows that $\beta_i = 0$ for $h \leq i \leq d - 1$. $\square$

Corollary. Suppose the conditions of Proposition 5.3 are satisfied. Then $M_I^d$ is a smooth $d$-dimensional manifold. The morphism $M_I^d \to \operatorname{Spec} A$ is smooth over $\operatorname{Spec} A - V(I)$. If $J \subset I$, then the morphism $M_I^d \to M_I^d$ is finite and flat.

D) Group actions. We set $M^d = \varprojlim M_I^d$. Let $\mathfrak{A}$ be the ring of adèles of $k$, and let $\mathfrak{A}_f$ be the ring of adèles without the component at $\infty$. (Thus $\mathfrak{A} = \mathfrak{A}_f \times k_\infty$ and $\hat{A} = \varprojlim A / I$.)

We define an action of the group $GL(d, \mathfrak{A}_f) / k^*$ on $M^d$. Let $S$ be a scheme over $A$, and let $X$ be an elliptic module over $S$ of rank $d$ together with a homomorphism $\psi: (k/A)^d \to \text{Mor}(S, X)$ such that for any nonzero ideal $I \subset A$ the restriction of $\psi$ to $(I^{-1}/A)^d$ is a structure of level $I$. Let $g \in GL(d, \mathfrak{A}_f)$ be a matrix with coefficients in $\hat{A}$. We can regard $g$ as an endomorphism of $(k/A)^d$. Its kernel $P$ is finite. It follows from Proposition 4.4 that the divisor $H \subset P$, which is equal to the sum of the divisors $\psi(\alpha), \alpha \in P$, is an $A$-invariant group subscheme, and $X/H$ is an elliptic $A$-module. We define $\psi_1: (k/A)^d \to \text{Mor}(S, X/H)$ so the diagram

$$
\begin{array}{c} (k / A) ^ {d} \xrightarrow {\psi} \operatorname{Mor} (S, X) \\ g \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \downarrow \\ (k / A) ^ {d} \xrightarrow {\psi_ {1}} \operatorname{Mor} (S, X / H) \end{array}
$$

is commutative.

It follows from Proposition 4.4 that for any $I$ the restriction of $\psi_{1}$ to $(I^{-1}/A)^{d}$ is a structure of level $I$. We obtain a left action on $M^{d}$ of the subgroup of matrices in $GL(d, \mathfrak{U}_{f})$ with coefficients in $\hat{A}$. Since the subgroup of nonzero elements of $A$ acts trivially on $M^{d}$, we obtain an action of $GL(d, \mathfrak{U}_{f})/k^{*}$.

Let $I \subset A$ be an ideal satisfying the conditions of Proposition 5.3, and let $U_I$ be the kernel of the homomorphism $GL(d, \hat{A}) \to GL(d, A/I)$. Then $M_I^d = U_I \setminus M^d$. Indeed, if $J \subset I$, then the morphism

$$
M _ {J} ^ {d} \times_ {\text { Spec } A} (\text { Spec } A - V (J)) \rightarrow M _ {I} ^ {d} \times_ {\text { Spec } A} (\text { Spec } A - V (J))
$$

is a bundle with structure group $U_{I} / U_{J}$. It follows from the normality of $M_{I}^{d}$ that $M_{I}^{d} = U_{I} \setminus M_{I}^{d}$.

E) Congruence relations. Recall the construction of the induced ring [4]. Let $G$ be a topological group, $H \subset G$ a closed subgroup, and $B$ a discrete ring on which the group $H$ acts continuously on the right. Consider the ring $C$ of continuous functions $f: G \to B$ such that $f(gh) = f(g) \cdot h$ for $g \in G$ and $h \in H$. This is called the induced ring; $G$ acts on it by the formula $f(g) \cdot (g') = f(gg')$. We shall say that $\operatorname{Spec} C$ is induced by the scheme $\operatorname{Spec} B$.

Let $v \in \operatorname{Spec} A$, and let $M_{(\nu)}^{d}$ be the fiber of $M^{d}$ over $\nu$. To each point of $M_{(\nu)}^{d}$ there corresponds an elliptic $A$-module, to which in turn corresponds a formal $A_{\nu}$-module. Let $W \subset M_{(\nu)}^{d}$ be the set of points for which the corresponding formal $A_{\nu}$-module has height 1.

Proposition 5.5. 1) W is an open, affine, everywhere dense  $GL(d, \mathfrak{A}_{f})$ -invariant subset.

2) Let $B \subset GL(d, k_v)$ be a group of matrices $(a_{ij})$ such that $a_{i1} = 0$ for $i > 1$. Let $B'$ be the preimage of $B$ in $GL(d, \mathfrak{U}_j)$. Then the $GL(d, \mathfrak{U}_f)$-scheme $W$ induced by any $B'$-scheme $W^0$ has the following properties:

a) The matrices $(a_{ij}) \in B \subset B'$ for which $|a_{11}|_{\nu} = 1$ and the lower right corner $(i, j > 1)$ coincides with the identity matrix acts trivially on $W_{\mathrm{red}}^0$.

b) Let $\pi$ be a simple element of $A_{\nu}$. The matrix

$$
\left( \begin{array}{c c c} \pi & & 0 \\ 1. & & \\ 0 & \ddots & 1 \end{array} \right)
$$

acts on $W_{\mathrm{red}}^0$ like the Frobenius of the field $A_{\nu} / (\pi)$.

Proof. Statement 1) is clear (the density of W follows from Proposition 5.4).

2) To each point $w \in W$ corresponds an elliptic module $X$ and a homomorphism $(k_{\nu} / A_{\nu})^d \to X$ whose kernel is isomorphic to $k_{\nu} / A_{\nu}$. This defines a $GL(d, \mathfrak{A}_f)$-invariant mapping of the set $W \to GL(d, \mathfrak{A}_f) / B'$. Let $I \subset A$ be an ideal, $I \neq 0$. The mapping

$U_{I} \backslash W \rightarrow GL(d, \mathfrak{A}_{f}) / B'$ is clearly continuous. Let $W_{I}^{0}$ be the preimage in $U_{I} \backslash W$ of the image of the identity in $U_{I} \backslash GL(d, \mathfrak{A}_{f}) / B'$. We set $W^{0} = \varprojlim W_{I}^{0}$. Then $W^{0}$ is invariant with respect to $B'$, and $W$ is induced by the scheme $W^{0}$. Every morphism $W_{\text{red}}^{0} \rightarrow W_{\text{red}}^{0}$ is uniquely defined by its action on the set of places. Statements a) and b) follow from this. $\square$

## §6. Uniformization of modular manifolds

A) Three analogs of the upper half-plane. Let $K$ be a local nonarchimedean field, $O \subset K$ its ring of integers, and $\pi \in O$ a prime element. Let $d$ be a natural number.

1) “Analytic” analog. Let  $P_{K}^{d-1}$  be projective space, considered as a rigid analytic space. The group  $GL(d, K)$  acts on  $P_{K}^{d-1}$  according to the formula

$$
(g; (z _ {1}, \dots , z _ {d})) \rightarrow (z _ {1}, \dots , z _ {d}) \cdot g ^ {- 1}.
$$

Let $\Omega^d$ be a set of points of $\mathbf{P}_K^{d - 1}$ not lying in any hyperplane defined over $K$. The set $\Omega^d$ is a $GL(d,K)$-invariant subset of $\mathbf{P}_K^{d - 1}$.

2) “Homogeneous” analog [5]. Let $S^d = GL(d, K)/GL(d, O)$. The group $GL(d, K)$ acts on the left on $K^d$, and so the elements of $S^d$ can be interpreted as similarity classes of free $d$-dimensional $O$-submodules in $K^d$. We introduce a metric $\rho$ on $S^d$. Let $M \subset K^d$, $N \subset K^d$, $M \approx N \approx O^d$, $M \supset N \supset \pi^k M$, $N \not\subset M$ and $N \not\ni \pi^{k-1} M$. Let $\{M\}$ and $\{N\}$ be the corresponding elements of $S^d$. We set $\rho(\{M\}, \{N\}) = k$.

A simplex is a subset $\Delta \subset S^d$ that satisfies one of the following equivalent conditions: a) $\rho(x, y) \leq 1$ for $x, y \in \Delta$; b) there exist submodules $M_i \subset K^d$ ($1 \leq i \leq k$) such that $M_i \approx O^d$, $M_i \supset M_{i+1}$ for $i < k$, $M_k \supset \pi M_1$, and $\Delta = \{\{M_1\}, \ldots, \{M_k\}\}$. Thus $S^d$ is a simplicial scheme of codimension $d-1$. The corresponding polyhedron is denoted $S^d(\mathbf{R})$, and the set of points of $S^d(\mathbf{R})$ with rational barycentric coordinates is denoted $S^d(\mathbf{Q})$.

3) “Topological” analog [9]. We fix a norm || on K, and use the same symbol to denote the extension of this norm to  $\overline{K}$ . We set  $q = |\pi^{-1}|$ . We call the norm  $\nu$  on  $K^{d}$  integral (rational) if for every  $x \in K^{d}$ ,  $x \neq 0$ , we have  $\log_{q} \nu(x) \in \mathbf{Z}$  (respectively  $\log_{q} \nu(x) \in \mathbf{Q}$ ). It can be shown that the set of norms on  $K^{d}$  up to similarity can be identified with  $S^{d}(\mathbf{R})$ ; the class of rational norms corresponds to  $S^{d}(\mathbf{Q})$  and the class of integral norms corresponds to  $S^{d}$ . Here is the construction. Let  $K^{d} \supset M_{1} \supset M_{2} \supset \cdots \supset M_{k} \supset \pi M_{1}, \alpha_{1}, \ldots, \alpha_{k} \geq 0, \Sigma_{1}^{k} \alpha_{i} = 1$ . Let  $\nu_{i}$  be the norm on  $K^{d}$  corresponding to  $M_{i}$ . To the point of  $S^{d}(\mathbf{R})$  with coordinates  $(\alpha_{1}, \ldots, \alpha_{k})$  corresponds the class of norms  $\nu = \max_{1 \leq i \leq k} \{ q^{\alpha_{i} + \cdots + \alpha_{k}} \nu_{i} \}$ . The metric  $\rho$  on  $S^{d}$  extends to a metric on  $S^{d}(\mathbf{R})$  which we shall also denote by  $\rho$: If  $\nu_{1}$  and  $\nu_{2}$  are norms on  $K^{d}$ , then

$$
\rho \left(\left\{\mathbf {v} _ {1} \right\}, \left\{\mathbf {v} _ {2} \right\}\right) \stackrel {{\text { def }}} {{=}} \log_ {q} \left\{\sup _ {K ^ {d}} \frac {\mathbf {v} _ {1}}{\mathbf {v} _ {2}} \cdot \underset {K ^ {d}} {\mathrm{s} _ {\mathrm{llp}}} \frac {\mathbf {v} _ {2}}{\mathbf {v} _ {1}} \right\}.
$$

If $(z_{1},\ldots ,z_{d})\in \Omega^{d}$, then the function $(a_{1},\ldots ,a_{d})\mapsto |\Sigma_{1}^{d}a_{i}z_{i}|$ is a rational norm on $K^d$. This defines a $GL(d,K)$-invariant mapping $\lambda \colon \Omega^d\to S^d (\mathbf{Q})$. (It is easy to check that $\lambda$ is surjective.)

Proposition 6.1. 1) Let $x_{1},\ldots ,x_{k}\in S^{d}$ and $c\in \mathbf{Q}$. Let

$$
X _ {c} = \left\{z \in \Omega^ {d} \middle | \sum_ {i = 1} ^ {k} \rho (x _ {i}, \lambda (z)) \leqslant c \right\}.
$$

Then $X_{c}$ is an open affine subset of $\mathbf{P}_{K}^{d-1}$. If $c_{1} < c_{2}$, then $X_{c_{1}}$ is in the interior of $X_{c_{2}}$.

2) $\Omega^d$ is an admissible open subset of $\mathbf{P}_K^{d-1}$.

Proof. Let $n$ be a natural number, $n > c$. For each $i$ ($1 \leq i \leq k$), let $\nu_i$ be a norm on $K^d$ whose class is $x_i$, let $C_i = \{y \in K^d | \nu_i(y) = 1\}$, and let $P_i \subset C_i$ be a finite $q^{-n}$-net. To each pair $(a, b)$, where $a = (a_1, \ldots, a_d) \in K^d$ and $b = (b_1, \ldots, b_d) \in K^d$, there corresponds a rational function $r_b^a$ on $\mathbf{P}_K^{d-1}$:

$$
r _ {b} ^ {a} \left(z _ {1}, \dots , z _ {d}\right) = \frac {\sum a _ {i} z _ {i}}{\sum b _ {i} z _ {i}}.
$$

Let $W \subset \mathbf{P}_K^{d-1}$ be the intersection of the domains of definition of the functions $r_b^a$, where $a, b \in P_i$, $1 \leq i \leq k$. It is easy to check that the set of functions $\Pi_1^k r_{\nu_i}^{u_i}$ (where $u_i, \nu_i \in P_i$) induces a closed imbedding of $W$ into an affine space. Clearly $X_c$ is the preimage of the polydisc of radius $q^c$ under this mapping. From this, 1) follows.

To deduce 2) from 1), it is sufficient to prove that if $B$ is a Tate algebra over $K$, and $\phi \colon \operatorname{Max} B \to \mathbf{P}_K^{d-1}$ is a morphism such that $\operatorname{Im} \phi \subset \Omega^d$, then $\operatorname{Im}(\lambda \circ \phi)$ is a bounded subset of $S^d(\mathbf{Q})$. Indeed, let $\phi$ be defined by functions $t_i \in B (1 \leq i \leq d)$, $|t_i| \leq 1$. Let

$$
\psi \left(a _ {1}, \dots , a _ {d}\right) = \inf _ {x \in \operatorname{Max} B} \left| \sum_ {i = 1} ^ {d} a _ {i} t _ {i} (x) \right|.
$$

Then $\psi$ is a continuous function on $K^d$, and $\psi$ vanishes only at zero. Let

$$
\mathrm{v} \left(a _ {1}, \dots , a _ {d}\right) = \max _ {1 \leqslant i \leqslant d} | a _ {i} |,
$$

and let $\{\nu\}$ be the corresponding element of $S^d$, and $\epsilon = \inf_{\nu(a) = 1} \psi(a)$. Clearly $\operatorname{Im}(\lambda \circ \phi)$ is contained in a ball with center $\{\nu\}$ and radius $\log_a \epsilon$.

Let $\overline{S}^d$ be the barycentric subdivision of $S^d$ (i.e. the points of $\overline{S}^d$ are the simplices of $S^d$; if $\Delta_1, \ldots, \Delta_m$ are simplices of $S^d$ such that $\Delta_1 \supset \Delta_2 \supset \ldots \supset \Delta_m$, then $\{\Delta_1, \ldots, \Delta_m\}$ is a simplex of $\overline{S}^d$.

Proposition 6.2. Let $c \in \mathbf{Q}$, $0 < c < 1$. For each simplex $\Delta \subset S^d$ of codimension $k - 1$, set

$$
V _ {\Delta} ^ {c} = \left\{y \in S ^ {d} (\mathbf {Q}) | \rho (y, x) \leqslant 1 - \frac {3 - c}{4 ^ {k}} f o r x \in \Delta , \sum_ {x \in \Delta} \rho (y, x) \leqslant k - 1 + \frac {1 + c}{4 ^ {k}} \right\},
$$

$U_{\Delta}^{c} = \lambda^{-1}(V_{\Delta}^{c})$. The sets $U_{\Delta}^{c}$ generate a GL(d, K)-invariant admissible affine covering of $\Omega^{d}$ with nerve $\overline{S}^{d}$. If $c_{1} < c_{2}$, then $U_{\Delta}^{c1} \Subset U_{\Delta}^{c2}$.

Proof. We shall show that the sets $V_{\Delta}^{c}$ form a covering of $S^{d}(\mathbf{Q})$ with nerve $\widetilde{S}^d$. (This is sufficient by Proposition 6.1.)

Let $\Phi \subset S^d$ be a simplex of dimension $d - 1$, and let $\Phi(\mathbf{Q})$ be the corresponding

closed subset of $S^d(\mathbf{Q})$. If $x \in \Phi(\mathbf{Q})$ has barycentric coordinates $(\alpha_1, \ldots, \alpha_d)$, then it is easy to check that the distance from $x$ to the $i$th point of $\Phi$ equals $1 - \alpha_i$. If $V_\Delta^c \cap \Phi(\mathbf{Q}) \neq \emptyset$, then $\Delta \subset \Phi$. Indeed, if $y \in \Delta, z \in \Phi$ and $x \in V_\Delta^c \cap \Phi(\mathbf{Q})$, then $\rho(x, y) < 1$, $\rho(z, x) \leq 1$, and so $\rho(y, z) < 2$. Consequently $\Delta \cup \Phi$ is a simplex, and $\Delta \subset \Phi$. Let $\Delta_1 \subset \Phi$ and $\Delta_2 \subset \Phi$ be simplices of dimensions $k_1 - 1$ and $k_2 - 1$, $k_2 \leq k_1$, with $\Delta_2 \not\supseteq \Delta_1$. Let the $j$th point of $\Phi$ lie in $\Delta_1 - \Delta_2$. If a point of $\Phi(\mathbf{Q})$ with coordinates $(\alpha_1, \ldots, \alpha_2)$ lies in $V_\Delta_1^c \cap V_\Delta_2^c$, then

$$
\alpha_ {j} \geqslant \frac {3 - c}{4 ^ {k _ {1}}} \text { and } \sum_ {i \neq j} \alpha_ {i} \geqslant 1 - \frac {1 + c}{4 ^ {k _ {2}}},
$$

This verifies the condition $\Sigma_1^d\alpha_i = 1$.

Denote by $M_k$ the set of the first $k$ points of the simplex $\Phi$. Clearly a point of $\Phi(\mathbf{Q})$ with coordinates $(\alpha_1, \ldots, \alpha_d)$, where $\alpha_i = (3 - c)/4^i$ for $i > 1$, will lie in $\bigcap_{k=1}^{d} V_{M_k}^c$. It remains to show that the sets $V_\Delta^c$ cover $S^d(\mathbf{Q})$. Let $x \in \Phi(\mathbf{Q})$ have coordinates $(\alpha_1, \ldots, \alpha_d)$, $\alpha_1 \geq \alpha_2 \geq \cdots \geq \alpha_d$. There exists $n \geq 1$ such that $\alpha_n \geq (3 - c)/4^n$ and $\alpha_i < (3 - c)/4^n$ for $i > n$. Then $x \in V_{M_n}^c$.

B) Factorization of rigid analytic spaces by the action of a discrete group. Let K be a field which is complete with respect to a nonarchimedean absolute value.

Proposition 6.3. Let B be a Tate algebra over K, and let the finite group G act on B. Then  $B^{G}$  is a Tate algebra and B is finite over  $B^{G}$ .

Proof. We represent $B$ as a factor of the algebra of convergent power series $R$. Let $C$ be a tensor product of copies of $R$ which correspond to elements of $G$. Then $G$ acts on $C$, and there exists a $G$-invariant epimorphism $C \to B$. It is easy to check that $C^G$ is a Tate algebra and $C$ is finite over $C^G$. Therefore $B$ is finite over $C^G$, and $B^G$ is finite over $C^G$. It follows from this that $B^G$ is a Tate algebra and $B$ is finite over $B^G$.

Proposition 6.4. Let $B_1$ and $B_2$ be Tate algebras, and $\operatorname{Max} B_2 \subset \operatorname{Max} B_1$ an open affine subset. Let the finite group $G$ act on $B_1$, with $\operatorname{Max} B_2$ invariant with respect to $G$. Then the morphism $\operatorname{Max} B_2^G \to \operatorname{Max} B_1^G$ is an open imbedding. If $\operatorname{Max} B_2 \Subset \operatorname{Max} B_1$, then $\operatorname{Max} B_2^G \Subset \operatorname{Max} B_1^G$.

Proof. Clearly the morphism $\operatorname{Max} B_2^G \to \operatorname{Max} B_1^G$ induces a one-to-one correspondence between sets of points and isomorphisms of complete local rings. By a basis theorem [8] this morphism is an open imbedding. If $\operatorname{Max} B_2 \Subset \operatorname{Max} B_1$, then there exists a closed imbedding $\phi: \operatorname{Max} B_1 \to \operatorname{Max} K\{t_1, \ldots, t_r\}$ such that $\phi(\operatorname{Max} B_2)$ is contained in the set $|t_i| \leq 1 - \epsilon$, $\epsilon > 0$. Let $s_{ij}$ be the $j$th symmetric function in translations $\phi^*(t_i)$ by elements of $G$. The functions $s_{ij}$ define a finite morphism from $\operatorname{Max} B_1^G$ into the identity polydisc which sends $\operatorname{Max} B_2^G$ into the polydisc of radius $1 - \epsilon$.

If $B$ is a Tate algebra under the action of a finite group $G$, we shall write $G \backslash \text{Max } B$ in place of $\text{Max } B^G$. Let $X$ be an affine analytic space under the action of the finite group $G$, let $Y = G \backslash X$, and let $Z$ be a separable space. Let $\phi: X \to Z$ be a morphism invariant under the action of $G$. Then there exists a unique morphism $\psi: Y \to Z$ such that $\phi = \psi \circ \pi$, where $\pi: X \to Y$ is the projection. Indeed, let $Z = \bigcup Z_i$

be an admissible affine covering. Then the sets $X_{i} = \psi^{-1}(Z_{i})$ are affine and $G$-invariant, and a finite number of sets $X_{i}$ cover $X$. We set $Y_{i} = G \setminus X_{i} = \pi(X_{i})$. The sets $Y_{i}$ form an admissible covering $Y$. It remains to check that for each $i$ there exists an identity morphism $\psi_{i}: Y_{i} \to Z$ consistent with $\phi$.

Definition. Let X be a separable rigid analytic space. The action of a group  $\Gamma$  on X is called discrete if there exists a set I and an action of  $\Gamma$  on I and an admissible affine covering of X by sets  $X_{i} (i \in I)$  for which the following conditions are satisfied:

1) $\gamma(X_i) = X_{\gamma(i)}$ for $\gamma \in \Gamma$ and $i \in I$.

2) Let $i \in I$ and $\Gamma_{i} = \{\gamma \in \Gamma | \gamma(i) = i\}$. Then the group $\Gamma_{i}$ is finite.

3) If $\gamma \notin \Gamma_i$, then $X_i \cap X_{\gamma(i)} = \varnothing$. If $i \in I$ and $j \in I$, then $X_{(j)} \cap X_{\gamma(i)} = \varnothing$ for all but finitely many $\gamma \in \Gamma$.

4) Let $i \in I$. Then the covering of $\bigcup_{\gamma} X_{\gamma(i)}$ by the sets $X_{\gamma(i)}$ is admissible.

In the situation described by the definition, let $Y = \Gamma \backslash X$, and let $Y_i$ be the image of $X_i$ in $Y$. It is easy to check that in a unique way $Y$ can be made into a separable analytic space, and the mapping $X \to Y$ into a morphism such that the covering of $Y$ by the sets $Y_i$ is admissible and affine, and $Y_i$ coincides with $\Gamma_i \backslash X_i$ as a space. If $\phi$ is a $\Gamma$-invariant morphism from $X$ into the separable space $Z$, it is easy to check that there exists a unique morphism $\psi: Y \to Z$ consistent with $\phi$. It follows from Proposition 6.2 that the discrete subgroup $\Gamma \subset GL(d, K)/K^*$, where $K$ is a local nonarchimedean field, acts discretely on $\Omega^d$.

C) Uniformization of modular manifolds. In this subsection $K = k_{\infty}$. If the ideal $I \subset A$ satisfies the conditions of Proposition 5.3, we set $\mathfrak{M}_I^d = (M_I^d \otimes k_{\infty})_{an}$. Indeed, as is clear from the proof of Proposition 5.3, the manifold $\mathfrak{M}_I^d$ makes sense for any nonzero ideal $I, I \neq A$.

Let $\widetilde{\Omega}_{d} = GL(d, k) \backslash (\Omega^{d} \times GL(d, \mathfrak{A}_{f}))$. (Here $GL(d, \mathfrak{A}_{f})$ is considered as a discrete set.) We introduce a left action of the group $GL(d, \mathfrak{A}_{f}) / K^{*}$ on $\widetilde{\Omega}_{d}$. Also, $\Omega^{d}$ is an open-closed subset of $\widetilde{\Omega}^{d}$. In the same way we define $\widetilde{S}^{d}, \widetilde{S}^{d}(\mathbf{R})$, etc.

A projective $A$-module $P$ of dimension $d$ together with a norm $\nu$ on $P \otimes_A k_\infty$ will be called a metrized $A$-module of dimension $d$. Metrized $A$-modules $(P_1, \nu_1)$ and $(P_2, \nu_2)$ will be called similar if there exists an isomorphism $f: P \preceq P_2$ such that $\nu_1$ and $f^*(\nu_2)$ are proportional. Let $I \subset A$ be an ideal, $I \neq A, I \neq 0$. A structure of level $I$ on a $d$-dimensional metrized $A$-module $(P, \nu)$ is an isomorphism $\psi: (I^{-1}/A)^d \simeq I^{-1}P/P$. Clearly the set of similarity classes of $d$-dimensional metrized $A$-modules with structure of level $I$ can be identified with $U_I \backslash S^d(\mathbf{R})$.

Let $(P, \nu)$ be a metrized $A$-module. We define a function $\widetilde{\nu}$ on $P \otimes k_{\infty} / P$ by the formula $\overline{\nu}(u) = \inf_{\nu \in u} \nu(\nu)$. Let $x, y \in (I^{-1} / A)^d$, $x \neq 0$, $y \neq 0$. We set $\mu_{x,y} = \overline{\nu}(\psi(x)) / \overline{\nu}(\psi(y))$. Then $\mu_{x,y}$ can be considered as a function on $U_I \setminus S^d(\mathbf{R})$.

Proposition 6.5. The subset $H \subset U_I \setminus S^d(\mathbb{R})$ is bounded if and only if the functions $\mu_{x,y}|_H$ are bounded for $x, y \in (I^{-1}/A)^d$, $x \neq 0$, $y \neq 0$.

Proof. The necessity is clear. We shall prove sufficiency. Let $(P, \nu)$ be a metrized $d$-dimensional $A$-module, and let $e_1, \ldots, e_d$ be a basis for $I^{-1}P / P$. Let $e_i'$ be an element in the class of $e_i$ which is smallest in norm, and let $u$ be an element

of $I^{-1}P$ which is smallest in norm. Let $\mu_{x,y} \leq c$ for all $x$ and $y$. Then $e_i' / |u| \leq c_1$, where $c_1$ depends only on $c$. We define a norm $\nu'$ on $P \otimes k_\infty$ by the formula $\nu'(\Sigma a_i e_i') = \max_i |a_i|$. Then $\nu'(u) \geq 1 / c_1$. By Minkowski's lemma, the order of $I^{-1}P / \Sigma_{i=1}^d A e_i'$ is bounded by a constant depending only on $c$. On the other hand, it follows from Minkowski's lemma that $\rho(\{\nu\}, \{\nu'\})$ is bounded by a constant depending only on $c$. (For the definition of $\rho$, see §6A).

Proposition 6.6. Let $I \subset A$ be an ideal, $I \neq 0$, $I \neq A$. Then $U_I \setminus \Omega^d = \mathfrak{M}_I^d$. This identification is consistent with the projection $\mathfrak{M}_J^d \to \mathfrak{M}_I^d$ for $J \subset I$, and also with the action of the group $GL(d, \mathfrak{A}_f)$.

Proof. a) In §3 we essentially obtained the identity $\mathfrak{M}_I^d (\overline{k}_{\infty}) = U_I\backslash \widetilde{\Omega}^d (\overline{k}_{\infty})$ consistent with the projections and the action of $GL(d,\mathfrak{A}_f)$. (That is, a point of $\Omega^d$ with coordinates $(z_1,\ldots ,z_d)$ corresponds to the lattice $\Sigma_1^d Az_i$ with the natural structure of level $l$.) It is easy to check that the mapping $\widetilde{\Omega}^d (\overline{k}_\infty)\to \mathfrak{M}_I^d (\overline{k}_\infty)$ induces a morphism $\widetilde{\Omega}^d\to \mathfrak{M}_I^d$. Since this morphism is invariant with respect to $U_{I}$, there is a corresponding morphism $\phi \colon U_I\backslash \widetilde{\Omega}^d\to \mathfrak{M}_I^d$.

b) Let $x \in U_I \setminus \Omega^d$, $y = \phi(x)$, and let $O_x$ and $O_y$ be the completions of the local rings of the manifolds $U_I \setminus \widetilde{\Omega}^d$ and $\mathfrak{M}_I^d$ at the points $x$ and $y$. We shall prove that $\phi^* \colon O_y \to O_x$ is an isomorphism. Let $m_y \subset O_y$ be a maximal ideal, and let $n$ be a natural number. There is an elliptic $A$-module $X$ with structure of level $I$ over the ring $O_y / m_y^n$. Let $f \in O_y / M_y^n[[z]]$ be a formal isomorphism from the additive $A$-module into $X$ (cf. Proposition 1.2). Just as in §3, it can be verified that $f$ is an entire function. Let $O_y^{nr}$ be a maximal unramified extension of $O_y$, and let $\Gamma$ be the set of zeros of $f$ in the ring $O_y^{nr} / m_y^n$. Then $\Gamma$ is an $A$-module, the homomorphism $\Gamma \to O_y^{nr} / m_y$ is injective, and its image is a lattice. In this way we obtain a homomorphism $O_x \to O_y^{nr} / m_y^n$ that is invariant with respect to $\text{Gal}(O_y^{nr} / O_y)$. Thus there is constructed a homomorphism $\psi \colon O_x \to O_y$ such that $\phi^* \psi = \text{id}$. Since $\mathfrak{M}_I^d$ and $U_I \setminus \widetilde{\Omega}^d$ are smooth manifolds of the same dimension (cf. Proposition 5.4), it follows that $\phi^*$ is an isomorphism.

Lemma. Let $\Sigma \subset \mathfrak{M}_I^d$ be an affine open subset. Then the image of $\Sigma$ in $U_I \setminus \widetilde{S}^d(\mathbf{Q})$ is bounded.

Proof. It suffices to consider the case $I = (\beta)$ with $|\beta| > 1$. Let $x, y \in (I^{-1} / A)^d$, $x \neq 0$, $y \neq 0$, let $f_{x,y}$ be the function on $\mathfrak{M}_I^d$ equal to the quotient of the images of $x$ and $y$ in the universal elliptic $A$-module; and let $c = \sup_{x,y} \sup_{\Sigma} |f_{x,y}|$. To each element of $\Sigma(\overline{k}_{\infty})$ there corresponds a $d$-dimensional lattice $\Gamma \subset \overline{k}_{\infty}$ together with an isomorphism $\psi: (I^{-1} / A)^d \mathfrak{S} I^{-1}\Gamma / \Gamma$. Let $f(z) = z\Pi_{\alpha \in \Gamma}(1 - z / \alpha)$. Let $\overline{\psi}(x)$ be the smallest (in modulus) element in the class of $\psi(x)$, and let $u$ be the smallest (in modulus) element of $\Gamma$, $u \neq 0$. Then

$$
\left| f (\psi (x)) \right| \geqslant \left| \psi (x) \right|, \left| f \left(\frac {u}{\beta}\right) \right| = \left| \frac {u}{\beta} \right| = \inf _ {x \neq 0} \overline {{{{\psi}}}} (x).
$$

Therefore $|\overline{\psi}(x)/\overline{\psi}(y)| \leq c$ for $x, y \in (I^{-1}/A)^{d}, x \neq 0, y \neq 0$. It remains only to apply Proposition 6.5. □

It follows from the lemma that $\phi^{-1}(\Sigma)$ can be covered by a finite number of affine sets. It follows from the fundamental theorem of [8] that $\phi$ is an isomorphism. $\square$

## §7. Tate uniformization

Let $O$ be a complete discrete normed ring over $A$, $m \subset O$ a maximal ideal, $K$ the field of fractions of $O$, and $K^s$ the separable closure of $K$. In this section $| |$ denotes the norm on $K$ and not on $k_{\infty}$.

Let $\phi: A \to K\{\tau\}$ be an elliptic module of rank $d$. We shall say that $\phi$ has stable reduction if there exists an elliptic $A$-module $\phi': A \to K\{\tau\}$ such that $\phi' \simeq \phi$, $\phi'(A) \subset O\{\tau\}$, and the reduction of $\phi'$ modulo $m$ is an elliptic $A$-module (i.e. there exists an $a \in A$ such that the degree of the reduction of $\phi'(a)$ is greater than 1). Clearly the rank of the reduction $\phi'$ is not greater than $d$. In case of equality we shall say that $\phi$ has good reduction. Then $\phi$ has good reduction if and only if $\phi$ is obtained from some elliptic $A$-module over $O$ by an extension of the ring of scalars.

Proposition 7.1. Every elliptic A-module over K has potentially stable reduction.

Proof. Let v be an (additive) valuation in K. We set

$$
w \left(\sum a _ {i} \tau^ {i}\right) = = \inf _ {i > 0} \left\{\frac {1}{p ^ {i} - 1} v (a _ {i}) \right\}.
$$

Let $y_1, \ldots, y_k$ be generators of the ring $A$, and let $r = \inf_{1 \leq j \leq k} w(\phi(y_j))$. If $K'$ is a finite extension of $K$ such that $r \cdot e(K'/K) \in \mathbf{Z}$ (where $e(K'/K)$ is the index of ramification), then $\phi$ has stable reduction over $K'$.

Remark. For modules of rank 1 the concepts of stable and good reduction coincide.

Let $X$ be an elliptic $A$-module over $K$. By a lattice in $X$ we mean a projective Gal $(K^s / K)$-invariant $A$-submodule of finite type $\Gamma \subset X(K^s)$ such that a finite number of elements of $\Gamma$ are contained in every disc.

Proposition 7.2. The isomorphism classes of elliptic modules of rank d over K are in one-to-one correspondence with the isomorphism classes of pairs  $(X, \Gamma)$ , where X is an elliptic A-module over K of rank d  $(d_{1} \leq d)$  with potentially good reduction, and  $\Gamma$  is a lattice in X of dimension  $d - d_{1}$ .

Proof. 1) Just as in §3, one can construct an elliptic $A$-module of rank $d$ for the pair $(X, \Gamma)$.

2) Let $\phi: A \to O\{\tau\}$ be an elliptic $A$-module of rank $d$ over $K$, and let the reduction of $\phi$ modulo $m$ be an elliptic module of rank $d_1$. The existence and uniqueness of a pair $(\psi, u)$ follows from Proposition 5.2, where $\psi: A \to O\{\tau\}$ is an elliptic $A$-module over $O$ of rank $d_1$,

$$
u = 1 + \sum_ {i = 1} ^ {\infty} a _ {i} \tau^ {i} \in O \{\{\tau \} \}, u \psi (a) = \varphi (a) u
$$

for $a \in A$, $a_i \in m$, $a_i \to O$.

Lemma. u is an analytic homomorphism.

Proof. It follows from the relation $\phi(a)u = u\psi(a)$ that there exist $k$ and $s$ such that

$$
k \geqslant 1, | a _ {i} | \leqslant \max \left(| a _ {i + 1} |, \dots , | a _ {i + k} |, | a _ {i - 1} | ^ {p ^ {k + 1}}, \dots , | a _ {i - s} | ^ {p ^ {k + s}}\right)
$$

for $i > s$. Let $c_{i} = \sup_{j \geq 1} |a_{j}|$. Since $a_{i} \to O$, we have $c_{i} \leq \max_{1 \leq j \leq s} c_{i-j}$ for $i > s$. Let $d_{i} = c_{i}^{p-i}$. Then $d_{i} \leq \max_{1 \leq j \leq s} d_{i-j}^{p,k}$, $d_{i} < 1$ for $i > s$, and so $d_{i} \to 0$.

Let $\Gamma$ be the kernel of the homomorphism $u$. Clearly, $\Gamma \subset K^s$. If $\gamma \in \Gamma$, $\gamma \neq 0$, then $|\gamma| > 1$. Let $a \in A$, $|a|_{\infty} > 1$, be such that the image of $a$ in $O$ is not zero. We set $f = \psi(a)$. Clearly $f^{-1}(\Gamma) / \Gamma \simeq [A/(a)]^{d_1}$, and the kernel of the homomorphism $f^{-1}(\Gamma) / \Gamma \to \Gamma / f(\Gamma)$ is isomorphic to $[A/(a)]^{d_1}$. Therefore $\Gamma / f(\Gamma) \simeq [A/(a)]^{d - d_1}$. If $z \in K^s$, $|z| > 1$, then $|f(z)| = |z|^{|a|^d_1}$. It follows from this that $\Gamma$ is a lattice of dimension $d - d_1$.

3) Thus we have obtained a one-to-one correspondence between the isomorphism classes of elliptic $A$-modules of rank $d$ over $K$ having stable reduction, and the isomorphism classes of pairs $(X, \Gamma)$, where $X$ is an elliptic $A$-module over $K$ of rank $d_1$ ($d_1 \leq d$) with good reduction, and $\Gamma$ is a lattice in $X$ of dimension $d - d_1$. It remains only to apply Galois descent.

## §8. Complex multiplication (d = 1)

Theorem 1. The scheme $M^1$ is the spectrum of the ring of integers of the maximum abelian extension of $k$, completely split at $\infty$. The action of $\mathfrak{A}_f^* / k^*$ on $M^1$ coincides with the action in class field theory.

Proof. Let $I \subset A$ be an ideal satisfying the conditions of Proposition 5.3. It follows from Proposition 7.1 that the morphism $M_I^1 \to \operatorname{Spec} A$ is finite. It follows from Proposition 5.4 that $M_I^1$ is a smooth curve, and that the morphism $M_I^1 \to \operatorname{Spec} A$ ramifies only over $V(I)$. Let $v \in \operatorname{Spec} A$, $v \notin V(I)$, and let $\pi$ be a prime element in $A_v$. It follows from Proposition 5.5 that $\pi$ acts on the fiber of $M_I^1$ over $v$ like the Frobenius of the field $A_v / (\pi)$. Therefore each connected component of $M_I^1$ is invariant with respect to $\mathfrak{U}_f^*$. On the other hand, $M^1(k_\infty) = M^1(\overline{k}_\infty) = \mathfrak{U}_f^* / k^*$ (cf. §3), and this identification is consistent with the action of $\mathfrak{U}_f^* / k^*$. Therefore $M^1$ is connected, the action of $\mathfrak{U}_f^* / k^*$ on $M^1$ is exact, and $\mathfrak{U}_f^* / M^1 = \operatorname{Spec} A$. It remains only to apply class field theory.

Corollary. Over any algebraically closed field over A there exist elliptic A-modules of any rank.

## §9. Compactification of modular surfaces (d = 2)

A) Construction of the boundary. Let X be an elliptic module over S. We denote by  $\bar{X}$  the bundle of projective lines over S obtained by joining to X an infinitely distant section. The multiplicative semigroup A acts on X.

The functor that associates to the scheme $S$ over $A$ the set of isomorphism classes of elliptic $A$-modules $X$ of rank 1 over $S$, together with a consistent structure of level $I$ (for all $I \subset A, I \neq 0$) and homomorphism $k \to \operatorname{Mor}(S, \overline{X})$, is represented by a scheme $N^1$.

The group $B$, consisting of matrices of the form $\begin{pmatrix} x & y \\ 0 & 1 \end{pmatrix}$ with $x \in \mathfrak{A}_f^*$ and $y \in \mathfrak{A}_f$, acts on $N^1$. Let $I \subset A$ be an ideal satisfying the conditions of Proposition 5.3.

Let $V_{I}$ be the group of matrices $\binom{x}{0}$, where $x, y \in \hat{A}$, $x \equiv 1 \mod I$, $y \equiv 0 \mod I$ and $N_{I}^{1} \stackrel{\text{def}}{=} V_{I} \setminus N^{1}$. It is easy to check that the morphism $N_{I}^{1} \to M_{I}^{1}$ is smooth. Let $\widetilde{N}_{I}^{1}$ be the completion of $N_{I}^{1}$ along an infinitely distant section. (We shall consider $\widetilde{N}_{I}^{1}$ as a scheme and not as a formal scheme.) Let $\hat{N}_{I}^{1} \subset \widetilde{N}_{I}^{1}$ be the complement at the infinitely distant section, and let $\widetilde{N}^{1} = \varprojlim \widetilde{N}_{I}^{1}$ and $\hat{N}^{1} = \varprojlim \hat{N}_{I}^{1}$. Let $\widetilde{M}^{2}$ and $\hat{M}^{2}$ be the schemes induces by the schemes $\widetilde{N}^{1}$ and $\hat{N}^{1}$ with respect to the imbedding $B \subset GL(2, \mathfrak{A}) / k^{*}$.

Let $I \subset A$ be an ideal satisfying the conditions of Proposition 5.3, and let $M_I^2 = U_I \setminus \widetilde{M}^2$ and $\hat{M}_I^2 = U_I \setminus M^2$. Let $O$ be a complete discrete normed ring over $A$ with field of fractions $K$.

Proposition 9.1. 1) The morphism $\operatorname{Spec} K \to M_I^2$ extends to a morphism $\operatorname{Spec} O \to M_I^2$ if and only if the corresponding elliptic module over $K$ has potentially good reduction.

2) There exists a unique $GL(2, \mathfrak{A}_I)$-invariant morphism $s \colon \hat{M}^2 \to M^2$ that induces a one-to-one mapping from the set of those morphisms $\operatorname{Spec} O \to \widetilde{M}_I^2$ such that the pre-image of $\hat{M}_I^2$ is $\operatorname{Spec} K$ into the set of those morphisms $\operatorname{Spec} K \to M_I^2$ which do not extend to morphisms $\operatorname{Spec} O \to M_I^2$.

Proof. Assertion 1) is clear. Let a morphism $\operatorname{Spec} K \to M_I^2$ not extend to a morphism $\operatorname{Spec} O \to M_I^2$. To this morphism corresponds an elliptic $A$-module over $K$ of rank 2, having potentially bad reduction, with structure of level $I$. This is the same (cf. Proposition 7.2) as an elliptic $A$-module $X$ over $K$ of rank 1 together with a one-dimensional lattice $\Gamma$ in $X$ such that $\operatorname{Gal}(K^s / K)$ acts on $I^{-1}\Gamma / \Gamma$ trivially and an epimorphism $(I^{-1}/A)^2 \to I^{-1}\Gamma / \Gamma$. (By definition, $I^{-1}\Gamma$ is the set of points of $X(K^s)$ that fall in $\Gamma$ under “multiplication” by any element $a \in I$.) Every automorphism of the $A$-module $I^{-1}\Gamma$ which is trivial on $I^{-1}\Gamma / \Gamma$ is the identity. Therefore $I^{-1}\Gamma \subset X(K)$. The bijection 2) is thus constructed. It is easy to check that it induced by a morphism $\hat{M}^2 \to M^2$.

Corollary. Let $v \in \operatorname{Spec} A$, $v \notin V(I)$, and let $Y$ be the fiber of $M_I^2$ over $v$ and $\overline{Y}$ a smooth compactification of $Y$. The completion of $\overline{Y}$ along $\overline{Y} - Y$ is canonically isomorphic to the fiber $\widetilde{M}_I^2$ over $v$.

B) Compactification of $M_I^2$.

Proposition 9.2. Let $X_{1}$ and $X_{2}$ be normal surfaces, $\pi_i \colon X_i \to \operatorname{Spec} A$ proper morphisms, $D_i \subset X_i$ closed subschemes finite over $\operatorname{Spec} A$, and $\phi \colon X_1 - D_1 \to X_2 - D_2$ a finite morphism over $\operatorname{Spec} A$. Then $\phi$ extends to a finite morphism $X_1 \to X_2$.

Proof. Let $G \subset X_1 \times X_2$ be the graph of $\phi$, and let $\overline{G}$ be its closure. Since $G$ is finite over $X_1 - D_1$ and $X_2 - D_2$, it follows that $G$ is closed in $(X_1 - D_1) \times X_2$ and $X_1 \times (X_2 - D_2)$. Therefore $\overline{G} - G$ is finite over $\operatorname{Spec} A$. It follows from this that the projection $\overline{G}_1 \to X_1$ is a finite morphism and birational isomorphism, i.e. $\overline{G} \approx X_1$.

Proposition 9.3. 1) Let $I \subset A$ be an ideal satisfying the conditions of Proposition 5.3. There exists a unique (up to isomorphism) smooth surface $\overline{M}_I^2$ containing $M_I^2$ as an open everywhere dense set such that the morphism $M_I^2 \to \operatorname{Spec} A$ extends to a proper morphism $\overline{M}_I^2 \to \operatorname{Spec} A$, and $\overline{M}_I^2 - M_I^2$ is finite over $\operatorname{Spec} A$.

2) If $J \subset I$, then the projection $M_J^2 \to M_I^2$ extends to a finite morphism $\overline{M}_J^2 \to \overline{M}_I^2$. Set $\overline{M}^2 = \varprojlim \overline{M}_I^2$. The action of $GL(2, \mathfrak{A}_f)$ on $M^2$ extends to an action on $\overline{M}^2$.

3) The completion of $\overline{M}_I^2$ along $\overline{M}_I^2 - M_I^2$ is canonically isomorphic to $\widetilde{M}_I^2$. In particular, the morphism $\overline{M}_I^2 \to \operatorname{Spec} A$ is smooth over $\operatorname{Spec} A - V(I)$.

Proof. Let $a \in A$, $|a| > 1$ and $k = \log_p |a|$. Let the image of $a$ have the form $\Sigma a_i \tau^i$ in the universal elliptic module over $M_I^2$.

We set $t = \alpha_k^{|a| + 1} / \alpha_{2k}$. We obtain a morphism $\phi \colon M_I^2 \to \operatorname{Spec} A[t]$. It follows from Proposition 9.1 that $\phi$ is a finite morphism. It is easy to check that $\phi$ is flat. On the other hand, it is easy to construct a finite flat morphism $\pi \colon M_I^2 \to \operatorname{Spec} A[[1/t]]$ such that $\phi \circ s$ coincides with the composition $\hat{M}_I^{2\pi'} \to \operatorname{Spec} A((1/t)) \to \operatorname{Spec} A[t]$. (Here $A((1/t))$ is the localization of $A[[1/t]]$ at $1/t$, and $\pi'$ is obtained from $\pi$ by change of basis.) There arises a morphism

$$
\sigma : \hat {M} _ {I} ^ {2} \rightarrow M _ {I} ^ {2} \times_ {\operatorname{Spec} A [ t ]} \operatorname{Spec} A \left(\left(\frac {1}{t}\right)\right).
$$

Lemma. Let $X = \{1, 2, 3\}$, and take the sets $\phi, X, \{1, 2\}, \{2, 3\}$ and $\{2\}$ to be open. Let $O_X$ be a sheaf of rings on $X$ such that

$$
H ^ {0} (\{1, 2 \}, O _ {x}) = A [ [ y ] ],
$$

$$
H ^ {0} (\{3, 2 \}, O _ {x}) = A [ y, y ^ {- 1} ], \quad H ^ {0} (\{2 \}, O _ {x}) = A ((y))
$$

The category of quasicoherent  $O_{X}$ -modules is equivalent to the category of A[y]-modules.

Proof. 1) Let $M$ be a module over $A[y]$. We set $H^0(U, \widetilde{M}) = H^0(U, O_X) \otimes_{A[y]} M$. $\widetilde{M}$ is a quasicoherent sheaf, and $M \mapsto \widetilde{M}$ is a functor. It remains to prove that the functorial homomorphisms $M \to H^0(X, \widetilde{M})$ and $H^0(X, F) \to F$ (where $F$ is a quasicoherent sheaf) are isomorphisms.

2) $0 \to A[y] \to A[y, y^{-1}] \times A[[y]] \to A((y)) \to 0$ is an exact sequence of flat $A[y]$-modules. Therefore $H^0(X, \widetilde{M}) = M$ and $H^1(X, \widetilde{M}) = 0$.

3) The restriction of the homomorphism $H^0(X, F) \stackrel{\sim}{\to} F$ on $\{2, 3\}$ is an isomorphism.

4) If $\operatorname{Supp} F \subset \{1\}$, then $H^0(X, F) \cong F$.

5) If $H^0(X, F) = 0$, then $F = 0$. (This follows from 3) and 4.)

6) Let $0 \to G_1 \to H^0(X, F) \to F \to G_2 \to 0$ be an exact sequence. Then $H_0(X, G_1) = 0$, and so $G_1 = 0$. Since $H^1(X, H^0(X, F)) = 0$, we have $H^0(X, G_2) = 0$. Therefore $G_2 = 0$.

It remains to check that $\sigma$ is an isomorphism. It is easy to check that $\deg \phi = \deg \pi$. (It is necessary to use the Corollary to Proposition 9.1.) It follows from Proposition 9.1 that the fibers of $\sigma$ consist of one point (and not necessarily reduced). On the other hand, one can check that the restriction of $\sigma$ to each connected component of $\hat{M}_I^2$ is a closed imbedding.

## § 10. Connection with automorphic forms (d = 2)

A) Étale cohomology of rigid analytic spaces. Let $K$ be a field complete with respect to a nonarchimedean absolute value, let $K^s$ be the separable closure of $K$,

and let $n$ be a natural number such that $1 / n \in K$. Let $X$ be a rigid analytic space over $K$.

Definition. 1) The set of pairs $(L, \phi)$, where $L$ is an invertible sheaf over $X$ and $\phi$: $O_x \cong L^n$, is denoted $H_{\mathfrak{et}}^1(X, \mu_n)$. (There is a group structure on $H_{\mathfrak{et}}^1(X, \mu_n)$.)
2) $H_{\mathfrak{et}}^0(X, \mathbf{Z}/(n)) \stackrel{\mathrm{def}}{=} H_{\mathrm{rigid}}^0(X, \mathbf{Z}/(n))$ and $H_{\mathfrak{et}}^0(X, \mu_n) \stackrel{\mathrm{def}}{=} H_{\mathrm{rigid}}^0(X, \mu_n)$.

(On the right side of these equalities $\mathbf{Z} / (n)$ is the constant sheaf and $\mu_{n}$ is the sheaf of $n$th roots of unity; this is a sheaf in the rigid topology.)

$$
H _ {\mathrm{et}} ^ {1} (X \otimes K ^ {s}, \mu_ {n}) \stackrel {{\text { def }}} {{=}} \lim _ {\overrightarrow {L}} H _ {\mathrm{et}} ^ {1} (X \otimes L, \mu_ {n}),\tag{3}
$$

where $K \subset L \subset K^s$ and $[L:K] < \infty$. In the same way we define $H_{\mathfrak{e}\mathfrak{t}}^0 (X\otimes K^s,\mu_n)$ and $H_{\mathfrak{e}\mathfrak{t}}^0 (X\otimes K^s,\mathbf{Z} / (n))$. (Gal$(K^s /K)$ acts on all of these groups.)

$$
H _ {\mathrm{et}} ^ {1} (X \otimes K ^ {s}, \mathbf {Z} / (n)) \stackrel {{\text { def }}} {{=}} H _ {\mathrm{et}} ^ {1} (X \otimes K ^ {s}, \mu_ {n}) \otimes \mu_ {n} ^ {- 1}.
$$

(Here $\mu_{n}^{-1}$ is a $\operatorname{Gal}(K^{s}/K)$-module homomorphism from the group of $n$th roots of unity of the field $K$ into $\mathbf{Z}/(n)$.

Properties of "étale cohomologies".

1) If $X = Y_{an}$, where $Y$ is a projective scheme over $K$, then the "cohomology" of $X$ coincides with the cohomology of $Y$. (This follows from theorems of type GAGA; cf. [11] and [12].)

2) There exists an exact sequence

$$
0 \to H ^ {0} (X, \mu_ {n}) \to H ^ {0} (X, O _ {X} ^ {*}) \stackrel {{n}} {{\to}} H ^ {0} (X, O _ {X} ^ {*}) \to H ^ {1} (X, \mu_ {n}) \to H ^ {1} (X, O _ {X} ^ {*}) \stackrel {{n}} {{\to}} H ^ {1} (X, O _ {X} ^ {*}).
$$

(Here $H^i (X,O_X)$ is the rigid cohomology.)

3) Let the sets  $X_{i}$  form an admissible open covering of X whose nerve has dimension not greater than 1. There exists an exact sequence

$$
\begin{array}{l} 0 \to H ^ {0} (X, \mu_ {n}) \to \prod_ {i} H ^ {0} (X _ {i}, \mu_ {n}) \to \prod_ {i \neq j} H ^ {0} (X _ {i} \cap X _ {j}, \mu_ {n}) \\ \to H ^ {1} (X, \mu_ {n}) \to \prod_ {i} H ^ {1} (X _ {i}, \mu_ {n}) \to \prod_ {i \neq j} H ^ {1} (X _ {i} \cap X _ {j}, \mu_ {n}). \end{array}
$$

4) If $X_1 \to X_2$ is a finite étale morphism of rigid analytic spaces with Galois group $G$ whose order is prime to $n$, then $H^1(X_2, \mu_n) = H^1(X_1, \mu_n)^G$.

Proposition 10.1. Let $z_{i} \in K$, $c_{i} \in K^{s}$ ($1 \leq i \leq k$) and $c \in K^{s}$. Let $|z_{i}| < |c|$, $0 < |c_{i}| < |c|$, and let $|z_{i} - z_{j}| > |c_{i}|$ for $i \neq j$. Set $X = \{z||z| \leq |c|, |z - z_{i}| \geq |c_{i}|\}$. Then

$$
H ^ {0} (X \otimes K ^ {s}, \quad \mathbf {Z} / (n)) = \mathbf {Z} / (n), \quad H ^ {1} (X \otimes K ^ {s}, \mu_ {n}) \simeq (\mathbf {Z} / (n)) ^ {k}.
$$

$(\operatorname{Gal}(K^s / K)$ acts trivially.)

Proof. a) The circle of radius $|c|$ is the union of circles of radius $|c_i|$ and sets $X$. Since the circle is connected, and the circles which intersect $X$ and circles of radius $|c_i|$ are connected, it follows that $X$ is connected. Analogously, $X \otimes L$ is connected if $L$ is a finite extension of $K$.

b) $H^{1}(X, O_{X}^{*}) = 0$ since every divisor on $X$ is principal. The set of rational functions without poles on $X$ is everywhere dense in $H^{0}(X, O_{X})$. Clearly, if $f \in H^{0}(X, O_{X})$

and $\sup_{z\in X}|f(z) - 1| < 1$, then $f = g^n$, where $g\in H^0 (X,O_X)$. Therefore every element of $H^0 (X,O_X^*)\otimes \mathbf{Z} / (n)$ can be represented as a rational function. It is easy to check that if $f$ is a rational function whose divisor on $\mathbf{P}_k^1$ is contained in one of the $k$ small circles or is outside of the large circle, then there exists $c\in K$ such that

$$
\sup _ {z \in X} | c f (z) - 1 | <   1.
$$

We obtain an epimorphism $\phi: (\mathbf{Z}/(n))^k \to H^1(X, \mu_n)/[K^*/(K^*)^n]$. Let $X_i$ be a circle of radius $|c_i|$. We consider the homomorphism $H^1(X, \mu_n) \to H^1(X_i, \mu_n)$. In order to prove that $\phi$ is an isomorphism, it is sufficient to check that $H^1(X_i, \mu_n)/[K^*/(K^*)^n] \simeq \mathbf{Z}/(n)$ for $1 \leq i \leq k$. This follows from the fact that $z^m$ is not an $n$th power in $K\{z, z^{-1}\}$ for $n + m$. (Indeed, if $f = \sum_{-\infty}^{\infty} a_\nu z^\nu \in K\{z, z^{-1}\}$ and $f^n = z^m$, then $\max_\nu |a_\nu| = 1$. We reduce the equation $f^n = z^m$ modulo the maximal ideal and obtain a contradiction.) Thus we obtain an exact sequence

$$
0 \rightarrow K ^ {*} / (K ^ {*}) ^ {n} \rightarrow H ^ {1} (X, \mu_ {n}) \rightarrow (\mathbf {Z} / (n)) ^ {k} \rightarrow 0,
$$

and so $H^1 (X\otimes K^s,\mu_n)\approx \mathbf{Z} / (n)^k$ □

B) Cohomology of $\Omega^2$. Let $C$ be an abelian group. A 1-cochain on a graph with coefficients in $C$ is an antisymmetric function on the set of oriented edges of the graph with values in $C$. A 1-cochain is harmonic if the sum of its values on all edges emanating from a single vertex of the graph is equal to 0.

Proposition 10.2. The group

$$
H ^ {0} \left(\Omega^ {2} \otimes k _ {\infty} ^ {s}, \mathbf {Z} / (n)\right) = \mathbf {Z} / (n) \cdot H ^ {1} \left(\Omega^ {2} \otimes k _ {\infty} ^ {s}, \mu_ {n}\right)
$$

is isomorphic to the group of harmonic 1-cochains on $S^2$ with coefficients in $\mathbf{Z} / (n)$. (The isomorphism is consistent with the action of $GL(2, k_{\infty})$; the action of $\operatorname{Gal}(k_{\infty}^{s} / k_{\infty})$ is trivial.)

Proof (cf. §6A). Let $0 < c < 1$, and let $\Delta_1 \subset S^2$ and $\Delta_2 \subset S^2$ be simplices. Let $F = U_{\Delta_1}^c \cap U_{\Delta_2}^c$; where $F$ is isomorphic to the space $X$ studied in Proposition 10.1. Since $F$ is absolutely irreducible and $S^2(\mathbf{R})$ is connected, we see that $\Omega^2$ is connected. We shall describe $H^1(F \otimes k_\infty^s, \mu_n)$ in invariant terms. Let $\nu$ be an (additive) valuation in $k_\infty^s$ such that $\nu(k_\infty^*) = \mathbf{Z}$. Let $k_\infty \subset L \subset k_\infty^s$ with $[L: k_\infty] < \infty$, and let $f$ be a holomorphic invertible function on $F \otimes L$. There exists a function $\overline{f}: \lambda(F) \to \mathbf{Q}$ such that $\overline{f} \circ \lambda = \nu \circ f$. The function $\overline{f}$ has the following properties:

1) $\overline{f}$ is linear on every edge intersecting $\lambda(F)$, and its "derivative" is an integer.

2) If $x \in \lambda(F) \cap S^2$, then the sum of its “derivatives” on directions emanating from $x$ is equal to 0.

Every function on $\lambda(F)$ satisfying 1) and 2) is equal to $\overline{f}$ for some $L$ and some function $f$ on $F \otimes L$. A function $f$ on $F \otimes L$ corresponds to the zero class in $H^{1}(F \otimes k_{\infty}^{s}, \mu_{n})$ if and only if the “derivative” of $\overline{f}$ on every edge is divisible by $n$. □ C) Cohomology of $\overline{M}^{2} \otimes K_{\infty}^{s}$.

Proposition 10.3. Let $\Pi$ be a representation of $GL(2, k_{\infty})$ in the space of locally constant functions $\mathbf{P}^1(k_{\infty}) \to \mathbf{Q}$, factored out by the constants, and let $A_0$ be the space

of parabolic automorphic forms on $GL(2,k)\backslash GL(2,\mathfrak{A})$ (cf. [10]). Let

$$
V = \operatorname{Hom} _ {G L (2, k _ {\infty})} (\pi , A _ {0}).
$$

Let $l \neq p$, and let $W^{\infty}$ be a 2-dimensional l-adic representation of $\operatorname{Gal}(k_{\infty}^{s}/k_{\infty})$ such that there exists a nonsplit exact sequence $0 \to \mathbf{Q}_{l} \to W^{\infty} \to \mathbf{Q}_{l}(-1) \to 0$. Then $H^{1}(\overline{M}^{2} \otimes k_{\infty}^{s}, \mathbf{Q}_{l}) \simeq V \otimes W^{\infty}$ (isomorphism of $GL(2, \mathfrak{A}_{f}) \times \operatorname{Gal}(k_{\infty}^{s}/k_{\infty})$-modules) and $H^{0}(\overline{M}^{2} \otimes k_{\infty}^{s}, \mathbf{Q}_{l})$ is isomorphic to the space of locally constant functions $k^{*} \setminus \mathfrak{A}_{f}^{*} \to \mathbf{Q}_{l}(\operatorname{Gal}(k_{\infty}^{s}/k_{\infty}))$ acts trivially, and $g \in GL(2, \mathfrak{A}_{f})$ acts according to the formula $(gf)(x) = f(x \det g))$.

Proof. a) Let $I \subset A$ be an ideal, $I \neq 0$, $I \neq A$. The images of the sets $U_{\Delta}^{c}$ and their $GL(2, \mathfrak{A}_{f})$-translates form an admissible open covering of $\Omega^2$. Clearly, the stabilizer in $U_{I}$ of any vertex or edge of $S_{2}$ is a $p$-group. Using properties 3) and 4) of the “étale cohomologies”, we obtain an isomorphism

$$
H ^ {0} \left(\mathcal {M} _ {I} ^ {2} \otimes k _ {\infty} ^ {s}, \mathbf {Z} / (n)\right) = H ^ {0} \left(U _ {I} \setminus \widetilde {S} ^ {2} (\mathbb {R}), \mathbf {Z} / (n)\right)
$$

and an exact sequence

$$
0 \rightarrow H ^ {1} \left(U _ {I} \setminus \widetilde {S} ^ {2} (\mathbb {R}), \mathbf {Z} / (n)\right)\rightarrow H ^ {1} \left(\mathcal {M} _ {I} ^ {2} \otimes k _ {\infty} ^ {s}, \mathbf {Z} / (n)\right)\rightarrow \left[ H ^ {1} \left(\widetilde {\Omega} \otimes k _ {\infty} ^ {s}, \mu_ {n}\right)\right] ^ {U _ {I}} \otimes \mu_ {n} ^ {- 1} \rightarrow 0,
$$

$H^{1}(\Omega \otimes \widetilde{k}_{\infty}^{s}, \mu_{n})$ coincides (cf. Proposition 10.2) with the group of harmonic 1-cochains on $\widetilde{S}^2$ with coefficients in $\mathbf{Z}/(n)$.

b) Let $I_0 \subset \operatorname{Gal}(k_\infty^s / k_\infty)$ be the inertial group. The mapping

$$
I _ {0} \times H ^ {1} \left(\mathcal {M} _ {I} ^ {2} \otimes k _ {\infty} ^ {s}, \quad \mathbf {Z} / (n)\right)\rightarrow H ^ {1} \left(U _ {I} \setminus \widetilde {S} ^ {2} (\mathbb {R}), \quad \mathbf {Z} / (n)\right)
$$

defined by the formula $(x, \sigma) \mapsto \sigma x - x$ is bilinear, and $\operatorname{Gal}(k_{\infty}^{s} / k_{\infty})$ is invariant. $I_0 / I_0^n$ and $\mu_n$ are isomorphic as $\operatorname{Gal}(k_{\infty}^{s} / k_{\infty})$-modules. Therefore there is a homomorphism

$$
[ H ^ {1} (\widetilde {\Omega} \otimes k _ {\infty} ^ {s}, \mu_ {n}) ] ^ {U _ {I}} \rightarrow H ^ {1} (U _ {I} \setminus \widetilde {S} ^ {2} (\mathbb {R}), \mathbf {Z} / (n)).
$$

It is easy to check that this homomorphism associates to a $U_{I}$-invariant harmonic 1-cochain on $\widetilde{S}^2$ the cohomology class of the corresponding cochain on $U_I \backslash \widetilde{\widetilde{S}}^2$.

c) Let $K$ be a complete archimedean field, $Y$ a smooth projective analytic curve over $K$, and $D \subset Y$ a finite subspace. It is easy to show that

$$
H ^ {0} (Y, \mathbf {Z} / (n)) = H ^ {0} (Y - D, \mathbf {Z} / (n)), H ^ {1} (Y \otimes k _ {\infty} ^ {s}, \mu_ {n}) \subset H ^ {1} ((Y - D) \otimes k _ {\infty} ^ {s}, \mu_ {n}).
$$

More precisely, if $Y - D = \bigcup_{i \in N} Y_i$ is an admissible affine covering such that $Y_i$ for each $i \in N$ intersects only a finite number of sets of the covering, then

$$
\begin{array}{c}H ^ {1} \left(Y \otimes k _ {\infty} ^ {s}, \mu_ {n}\right)\\= \bigcup_ {\Phi \subset N} \operatorname{Ker} \left[ H ^ {1} \left((Y - D) \otimes k _ {\infty} ^ {s}, \mu_ {n}\right)\rightarrow H ^ {1} \left(\left(\bigcup_ {i \subset N - \Phi} Y _ {i}\right) \otimes k _ {\infty} ^ {s}, \mu_ {n}\right)\right]\end{array}
$$

(where $\Phi$ runs through the finite subsets of $N$). Therefore

$$
H ^ {0} \left(\overline {{{M}}} _ {I} ^ {2} \otimes k _ {\infty} ^ {s}, \mathbf {Z} / (n)\right) = H ^ {0} \left(U _ {I} / \widetilde {S} ^ {2} (\mathbb {R}), \mathbf {Z} / (n)\right),
$$

and $H^1(\overline{M}_I^2 \otimes k_\infty^s, \mu_n)$ consists of those elements of $H^1(\mathfrak{M}_I^2 \otimes k_\infty^s, \mu_n)$ for which the corresponding harmonic 1-form is finite modulo $U_I$ (or, equivalently, parabolic).

d) Going to the limit, we obtain an isomorphism

$$
H ^ {0} \left(\overline {{{M}}} _ {I} ^ {2} \otimes k _ {\infty} ^ {s}, \mathbf {Q} _ {l}\right) = H ^ {0} \left(U _ {I} \setminus \widetilde {S} (\mathbb {R}), \mathbf {Q} _ {l}\right)
$$

and an exact sequence

$$
0 \rightarrow H ^ {1} (U _ {I} \backslash \widetilde {S} _ {0} ^ {2} (\mathbf {R}), \mathbf {Q} _ {l}) \rightarrow H ^ {1} (\overline {{M}} _ {I} ^ {2} \otimes k _ {\infty} ^ {s}, \mathbf {Q} _ {l}) \rightarrow V _ {I} \otimes \mathbf {Q} _ {l} (- 1) \rightarrow 0
$$

where $V_{I}$ is the space of parabolic $U_{I}$-invariant harmonic 1-cochains on $S^2$ with coefficients in $\mathbf{Q}$. It is easy to check that the homomorphism $U_{I} \to H^{1}(U_{I} \setminus \widetilde{S}^{2}(\mathbf{R}), \mathbf{Q})$ constructed in b) is an isomorphism. It follows from this that $H^{1}(\overline{M}^{2} \otimes k_{\infty}^{s}, \mathbf{Q}_{l}) \simeq V \otimes W^{\infty}$, where $\overline{V} = \varinjlim_{I} V_{I}$.

e) It remains to show that $\vec{V} = V$. For this it suffices to verify that the space of harmonic 1-cochains on $S^2$ with coefficients in $\mathbf{Q}$ is canonically isomorphic to $\operatorname{Hom}(\Pi, \mathbf{Q})$. This isomorphism is constructed in the following way. Let $x$ and $y$ be adjacent points in $S^2$, and let $P_{x,y}$ be the set of points $z \in \mathbf{P}^1(k_\infty)$ such that $y$ is between $x$ and $z$. If $\mu$ is a distribution on $\mathbf{P}^1(k_\infty)$ with values in $\mathbf{Q}$ such that $\int_{\mathbf{P}^1(k_\infty)} \mu = 0$, then the 1-cochain $l_\mu$ which has the value $\int_{P_x,y} \mu$ on $x\vec{y}$ is harmonic.

## § 11. Fundamental theorem

The group $\operatorname{Gal}(k^s / k) \times GL(2, \mathfrak{A}_f)$ acts on $H^{*}(\bar{\mathbf{M}}^{2} \otimes k^{s}, \mathbf{Q}_{l})$. (The group $GL(2, \mathfrak{A}_f)$ acts on $\bar{\mathbf{M}}^{2}$ on the left, and on the cohomology on the right; we shall consider the corresponding left action on the cohomology.) We set $V \otimes \overline{\mathbf{Q}} = \bigoplus_{i \in T} V_i$, where $V_i$ is an irreducible representation of $GL(2, \mathfrak{A}_f)$. (It is proved in [10] that $V_i \neq V_j$ for $i \neq j$). It follows from Proposition 10.3 that

$$
H ^ {1} \left(\overline {{{M}}} ^ {2} \otimes k _ {\infty} ^ {s}, \overline {{{\mathbf {Q}}}} _ {l}\right) \approx \underset {i} {\oplus} V _ {i} \otimes W _ {i},
$$

where $W_{i}$ is a representation of $\operatorname{Gal}(k^{s}/k)$ in the space $\overline{\mathbf{Q}}_{l}^{2}$. Let $V_{i} = \bigotimes_{\nu \in \operatorname{Spec} A} V_{i}^{\nu}$, and let $W_{i}^{\nu}$ be the restriction of $W_{i}$ on $\operatorname{Gal}(k_{\nu}^{s}/k_{\nu})$. Let $\hat{V}_{i}^{\nu}$ be the representation contragredient to $V_{i}^{\nu}$.

Theorem 2.1)

$$
H ^ {0} (\overline {{{M}}} ^ {2} \otimes k ^ {s}, \mathbf {Q} _ {l}) = H ^ {0} (M ^ {1} \otimes k ^ {s}, \mathbf {Q} _ {l}).
$$

(The group $GL(2, \mathfrak{A}_f)$ acts on $M^1$ by the homomorphism $\det: GL(2, \mathfrak{A}_f) \to \mathfrak{A}_f^*$.)

2) For any $i \in T$ and $v \in \operatorname{Spec} A$ such that $V_i^\nu$ is a representation of class 1, $W_i^\nu$ "coincides" with $\hat{V}_i^\nu$ (i.e., $W_i^\nu$ is unramified and $L(s, W_i^\nu) = L(s - \frac{1}{2}, \hat{V}_i^\nu)$).

Proof. 1) In §9A) we defined an imbedding $M^1 \to \bar{M}^2$ consistent with the action of the group $B \subset GL(2, \mathfrak{U}_f)$. It follows from Proposition 10.3 that the corresponding homomorphism

$$
H ^ {0} \left(\overline {{M}} ^ {2} \otimes k _ {\infty} ^ {s}, \mathbf {Q} _ {l}\right)\rightarrow H ^ {0} \left(M ^ {1} \otimes k _ {\infty} ^ {s}, \mathbf {Q} _ {l}\right)
$$

is an isomorphism.

2) Let

$$
L (s, \hat {V} _ {i} ^ {v}) = (1 - \mu_ {1} q ^ {- s}) ^ {- 1} (1 - \mu_ {2} q ^ {- s}) ^ {- 1}.
$$

Just as in [14], it is proved that $W_{i}^{\nu}$ is unramified and each eigenvalue of the Frobenius

(arithmetical) on $W_{i}^{\nu}$ coincides either with $\mu_1^{-1}q^{-\frac{1}{2}}$ or with $\mu_2^{-1}q^{-\frac{1}{2}}$. We shall show that if one of the eigenvalues of the Frobenius coincides with $\mu_1^{-1}q^{-\frac{1}{2}}$, then another is equal to $\mu_2^{-1}q^{-\frac{1}{2}}$. It is known that $\hat{V}_i \simeq V_j$ for some $j \in T$. If the restriction of $V_i$ to the center of the group $GL(2, \mathfrak{A}_f)$ is the multiple character $\omega \in \det$, then $\hat{V}_i \simeq V_i \otimes \omega^{-1}$ (cf. [10]). It follows from properties of the cup product that one of the eigenvalues of the Frobenius on $W_j^\nu$ coincides with $\mu_1q^{-\frac{1}{2}}$. Let $s \in H^0(\overline{M}^2 \otimes k^s, \overline{\mathbf{Q}}_l)$, $s \neq 0$, and $gs = \omega(\det g)s$ for $g \in GL(2, \mathfrak{A}_f)$. Multiplication by $s$ induces an automorphism of $H^1(\overline{M}^2 \otimes k_\infty^s, \overline{\mathbf{Q}}_l)$. It follows from assertion 1) and Theorem 1 that one of the eigenvalues of the Frobenius on $W_i^\nu$ is $\mu_1q^{-\frac{1}{2}}\omega(\pi)$, where $\pi$ is a prime element of $A_\nu$. But $\omega(\pi) = \mu_1^{-1}\mu_2^{-1}$.

Remark. The action of $GL(2, \mathfrak{A}_f)$ in [14] is different from the action described in §5D) on the outer automorphisms of $GL(2, \mathfrak{A}_f)$. This explains the different formulations of Theorem 2 and the corresponding theorem in [14].

Received 17/DEC/73

## BIBLIOGRAPHY

1. I. M. Gel'fand, M. I. Graev and I. I. Pjateckii-Sapiro, Generalized functions. Vol. 6: Representation theory and automorphic functions, "Nauka", Moscow, 1966; English transl., Saunders, Philadelphia, Pa., 1969. MR 36 #3725; 38 #2093.

2. D. Mumford, Abelian varieties, Tata Inst. Fund. Res. Studies in Math., no. 5, Oxford Univ. Press, London, 1970. MR 44 #219.

3. ——, An analytic construction of degenerating curves over complete local rings, Compositio Math. 24 (1972), 129–174.

4. I. I. Pjateckiš-Sapiro, Induced rings and the reduction of fields of Abelian modular functions, Izv. Akad. Nauk SSSR Ser. Mat. 34 (1970), 532–546 = Math. USSR Izv. 4 (1970), 536–550. MR 44 #155.

5. F. Bruhat and J. Tits, Groupes réductifs sur un corps local, Inst. Hautes Études Sci. Publ. Math. No. 41 (1972).

6. P. Deligne, Formes modulaires et représentations l-adiques, Séminaire Bourbaki 1968/69, Exposé 355, Lecture Notes in Math., no. 179, Springer-Verlag, Berlin, and New York, 1971, pp. 139–185. MR 42 #7460.

7. Albrecht Frölich, Formal groups, Lecture Notes in Math., no. 74, Springer-Verlag, Berlin and New York, 1968. MR 39 #4164.

8. Hans Grauert and Lothar Gerritzen, Die Azyklizität der affinoiden Überdeckungen, Global Analysis (Papers in Honor of K. Kodaira), Univ. of Tokyo Press, Tokyo, 1969, pp. 159–184. MR 41 #514.

9. O. Goldman and N. Iwahori, The space of p-adic norms, Acta Math. 109 (1963), 137–177. MR 26 #2430.

10. Hervé Jacquet and R. P. Langlands, Automorphic forms on GL(2), Lecture Notes in Math., no. 114, Springer-Verlag, Berlin and New York, 1970.

11. Rienhardt Kiehl, Der Endlichkeitssatz für eigentliche Abbildungen in der nichtarchimedischen Funktionentheorie, Invent. Math. 2 (1967), 191–214. MR 35 #1833.

12. \_\_\_\_, Theorem A und Theorem B in der nichtarchimedischen Funktionentheorie, Invent. Math. 2 (1967), 256–273. MR 35 #1834.

13. Jonathan Lubin and John Tate, Formal moduli for one-parameter formal Lie groups, Bull. Soc. Math. France 94 (1966), 49–59. MR 39 #214.

14. I. I. Pjateckiš-Sapiro, Zeta-functions of modular curves, preprint, Inst. Appl. Math., Moscow, 1972.