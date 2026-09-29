# ON THE THEORY OF GENERAL PARTIAL DIFFERENTIAL OPERATORS

## BY LARS HÖRMANDER

## in Lund

## CONTENTS

PREFACE 162
CHAPTER I. Differential operators from an abstract point of view.
1.0. Introduction 163
1.1. Definitions and results from the abstract theory of operators 164
1.2. The definition of differential operators 167
1.3. Cauchy data and boundary problems 171
CHAPTER II. Minimal differential operators with constant coefficients.
2.0. Introduction 174
2.1. Notations and formal properties of differential operators with constant coefficients 176
2.2. Estimates by Laplace transforms 177
2.3. The differential operators weaker than a given one 178
2.4. The algebra of energy integrals 180
2.5. Analytical properties of energy integrals 182
2.6. Estimates by energy integrals 183
2.7. Some special cases of Theorem 2.2 185
2.8. The structure of the minimal domain 189
2.9. Some theorems on complete continuity 201
2.10. On some sets of polynomials 207
2.11. Remarks on the case of non-bounded domains 208
CHAPTER III. Maximal differential operators with constant coefficients.
3.0. Introduction 210
3.1. Comparison of the domains of maximal differential operators 211
3.2. The existence of null solutions 216
3.3. Differential operators of local type 218
3.4. Construction of a fundamental solution of a complete operator of local type 222
3.5. Proof of Theorem 3.3 229
11-553810. Acta Mathematica. 94. Imprimé le 26 septembre 1955.

## LARS HÖRMANDER

3.6. The differentiability of the solutions of a complete operator of local type . . 230
3.7. Spectral theory of complete self-adjoint operators of local type . . . . . . . 233
3.8. Examples of operators of local type . . . . . . . . . . . . . . . . . . 238
3.9. An approximation theorem . . . . . . . . . . . . . . . . . . . . . . . . 241

CHAPTER IV. Differential operators with variable coefficients.
4.0. Introduction ..... 242
4.1. Preliminaries ..... 242
4.2. Estimates of the minimal operator ..... 244

REFERENCES ..... 247

## PREFACE

0.1. The main interest in the theory of partial differential equations has always been concentrated on elliptic and normally hyperbolic equations. During the last few years the theory of these equations has attained a very satisfactory form, at least where Dirichlet's and Cauchy's problems are concerned. There is also a vivid interest in other differential equations of physical importance, particularly in the mixed elliptic-hyperbolic equations of the second order. Very little, however, has been written concerning differential equations of a general type. Petrowsky ([25], p. 7, pp. 38–39) stated in 1946 that "it is unknown, even for most of the very simplest non-analytical equations, whether even one solution exists", and "there is, in addition, a sizable class of equations for which we do not know any correctly posed boundary problems. The so-called ultra-hyperbolic equation

$$
\frac {\partial^ {2} u}{\partial x _ {1} ^ {2}} + \dots + \frac {\partial^ {2} u}{\partial x _ {p} ^ {2}} = \frac {\partial^ {2} u}{\partial y _ {1} ^ {2}} + \dots + \frac {\partial^ {2} u}{\partial y _ {p} ^ {2}},
$$

with  $p \geq 2$  appears, for example, to be one of these." Some important papers have appeared since then. In particular, we wish to mention the proof by Malgrange [19] that any differential equation with constant coefficients has a fundamental solution. (Explicit constructions of distinguished fundamental solutions have been performed for the ultra-hyperbolic equations by de Rham [27] and others.) Apart from this result, however, no efforts to explore the properties of general differential operators seem to have been made. The principal aim of this paper is to make an approach to such a study. The general point of view may perhaps illuminate the theory of elliptic and hyperbolic equations also.

0.2. A pervading characteristic of the modern theory of differential equations is the use of the abstract theory of operators in Hilbert space. Our point of view here is also purely operator theoretical. To facilitate the reading of this paper we have included an exposition

of the necessary abstract theory in the first chapter, where we introduce our main problems. $^{1}$  Using the abstract methods we prove that the answer to our questions depends on the existence of so-called a priori inequalities. The later chapters are to a great extent devoted to the proof of such inequalities. In Chapters II and IV the proofs are based on the energy integral method in a general form, i.e. on the study of the integrals of certain quadratic forms in the derivatives of a function. For the wave equation, where it has a physical interpretation as the conservation of energy, this method was introduced by Friedrichs and Lewy [6]. Recently Leray [19] has found a generalization which applies to normally hyperbolic equations of higher order. In Chapter II we study systematically the algebraic aspects of the energy integral method. This chapter deals only with equations with constant coefficients. The extension to a rather wide class of equations with variable coefficients is discussed in Chapter IV.

In Chapter III we chiefly study a class of differential operators with constant coefficients, which in several respects appears to be the natural class for the study of problems usually treated only for elliptic operators. For example, Weyl's lemma holds true in this class, i.e. all (weak) solutions are infinitely differentiable. Our main arguments use a fundamental solution which is constructed there. The results do not seem to be accessible by energy integral arguments in the general case, although many important examples can be treated by a method due to Friedrichs [5].

0.3. A detailed exposition of the results would not be possible without the use of the concepts introduced in Chapter I. However, this chapter, combined with the introductions of each of the following ones, gives a summary of the contents of the whole paper.

0.4. It is a pleasure for me to acknowledge the invaluable help which professor B. L. van der Waerden has given me in connection with the problems of section 3.1. I also want to thank professor A. Seidenberg, who called my attention to one of his papers, which is very useful in section 3.4.

## CHAPTER I

## Differential Operators from an Abstract Point of View

## 1.0. Introduction

In the preface we have pointed out that the present chapter has the character of an introduction to the whole paper. Accordingly we do not sum up the contents here, but

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Chapter I, particularly section 1.3, overlaps on several points with a part of an important paper by Višik ([34]) on general boundary problems for elliptic equations of the second order.</span></small>

merely present the general plan. First, in section 1.1, we recall some well-known theorems and definitions from functional analysis. Then in section 1.2 we define differential operators in Hilbert space and specialize the theorems of section 1.1 to the case of differential operators. A discussion of the meaning of boundary data and boundary problems is given in section 1.3. This study has many ideas in common with Višik [34]. It is not logically indispensable for the rest of the paper but it serves as a general background.

## 1.1. Definitions and results from the abstract theory of operators

Let $B_{0}$ and $B_{1}$ be two complex Banach spaces, i.e. two normed and complete complex vector spaces. A linear transformation (operator) T from $B_{0}$ to $B_{1}$ is a function defined in a linear set $D_{T}$ in $B_{0}$ with values in $B_{1}$ such that

$$
T (\alpha x + \beta y) = \alpha T x + \beta T y\tag{1.1.1}
$$

for $x, y \in \mathcal{D}_T$ and complex $\alpha, \beta$. It follows from (1.1.1) that the range of values $\mathcal{R}_T$ is a linear set in $B_{1}$:

The set $B_0 \times B_1$ of all pairs $x = [x_0, x_1]$ with $x_i \in B_i$ ($i = 0, 1$), where we introduce the natural vector operations and the norm$^{1}$

$$
\left| x \right| = (\left| x _ {0} \right| ^ {2} + \left| x _ {1} \right| ^ {2}) ^ {\frac {1}{2}},\tag{1.1.2}
$$

is also a Banach space, called the direct sum of $B_0$ and $B_1$. If $T$ is a linear transformation from $B_0$ to $B_1$, the set in $B_0 \times B_1$ defined by

$$
G _ {T} = \{[ x _ {0}, T x _ {0} ], x _ {0} \in \mathcal {D} _ {T} \}\tag{1.1.3}
$$

is linear and contains no element of the form  $[0, x_{1}]$  with  $x_{1} \neq 0$ . The set  $G_{T}$  is called the graph of T. A linear set G in  $B_{0} \times B_{1}$ , containing no element of the form  $[0, x_{1}]$  with  $x_{1} \neq 0$ , is the graph of one and only one linear transformation T.

A linear transformation $T$ is said to be closed, if the graph $G_{T}$ is closed. We shall also say that a linear transformation $T$ is pre-closed, if the closure $\bar{G}_{T}$ of the graph $G_{T}$ is a graph, i.e. does not contain any element of the form $[0, x_{1}]$ with $x_{1} \neq 0$. The transformation with the graph $\bar{G}_{T}$ is then called the closure of $T$. Thus $T$ is pre-closed if and only if, whenever $x_{n} \to 0$ in $B_{0}$ and $Tx_{n} \to y$ in $B_{1}$, we have $y = 0$. We also note that any linear restriction of a linear pre-closed operator is pre-closed.

The following theorem gives a useful form of the theorem on the closed graph, which states that a closed transformation from $B_0$ to $B_1$ must be continuous, if $\mathcal{D}_T = B_0$. (Cf. Bourbaki, Espaces vectoriels topologiques, Chap. I, § 3 (Paris 1953).)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$B_{0}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{B}_{1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{B}_0\times \mathbf{B}_1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Any equivalent norm in  $B_{0} \times B_{1}$  can be used, but this choice has the advantage of giving a Hilbert norm, if  $B_{0}$  and  $B_{1}$  have Hilbert norms.</span></small>

THEOREM 1.1. Let $B_{i}$ ($i = 0, 1, 2$) be Banach spaces and $T_{i}$ ($i = 1, 2$) be linear transformations from $B_{0}$ to $B_{i}$. Then, if $T_{1}$ is closed, $T_{2}$ pre-closed and $\mathcal{D}_{T_1} \subset \mathcal{D}_{T_2}$, there exists a constant $C$ such that

$$
\left| T _ {2} u \right| ^ {2} \leq C \left(\left| T _ {1} u \right| ^ {2} + \left| u \right| ^ {2}\right), \quad u \in \mathcal {D} _ {T _ {1}}.\tag{1.1.4}
$$

PROOF. The graph  $G_{T_{1}}$  of  $T_{1}$  is by assumption closed. Hence the mapping

$$
G _ {T _ {1}} \ni [ u, T _ {1} u ] \rightarrow T _ {2} u \in B _ {2}\tag{1.1.5}
$$

is defined in a Banach space. We shall prove that the mapping is closed. Thus suppose that  $[u_{n}, T_{1}u_{n}]$  converges in  $G_{T_{1}}$  and that  $T_{2}u_{n}$  converges in  $B_{2}$ . Since  $T_{1}$  is closed, there is an element  $u \in D_{T_{1}}$  such that  $u_{n} \to u$  and  $T_{1}u_{n} \to T_{1}u$ . In virtue of the assumptions, u is in  $D_{T_{1}}$  and, since  $T_{2}$  is pre-closed, the existing limit of  $T_{2}u_{n}$  can only be  $T_{2}u$ . Hence the mapping (1.1.5) is closed and defined in the whole of a Banach space, so that it is continuous in virtue of the theorem on the closed graph. This proves the theorem.

Theorem 1.1 is the only result we need for other spaces than Hilbert spaces; it will also be used when some of the spaces $B_{i}$ are spaces of continuous functions with uniform norm. In the rest of this section we shall only consider transformations from a Hilbert space $H$ to itself. In that case the graph is situated in $H \times H$, which is also a Hilbert space, the inner product of $x = [x_0, x_1]$ and $y = [y_0, y_1]$ being given by

$$
(x, y) = (x _ {0}, y _ {0}) + (x _ {1}, y _ {1}).
$$

For the definition of adjoints, products of operators and so on, we refer the reader to Nagy ([23], p. 27 ff.).

LEMMA 1.1. The range $\mathcal{R}_T$ of a closed densely defined linear operator $T$ is equal to $H$ if and only if $T^{* - 1}$ exists and is continuous, and consequently is defined in a closed subspace.

PROOF. We first establish the necessity of the condition. Thus suppose that $\mathcal{R}_T = H$. Since $T^* u = 0$ implies that $(Tv, u) = (v, T^* u) = 0$ for every $v \in \mathcal{D}_T$, it follows that $T^* u = 0$ only if $u = 0$. Hence $T^{*-1}$ is defined. Now for any element $v$ in $H$ we can find an element $w$ such that $Tw = v$. Hence we have, if $u \in \mathcal{D}_{T^*}$,

$$
(u, v) = (u, T w) = \left(T ^ {*} u, w\right),
$$

so that for fixed v

$$
\left| (u, v) \right| \leq C \| T ^ {*} u \|, \quad u \in \mathcal {D} _ {T ^ {*}}.
$$

Let $u_n$ be a sequence of elements in $\mathcal{D}_{T^*}$ such that $\| T^* u_n \|$ is bounded. Since $|(u_n, v)|$ is then bounded for every fixed $v$, it follows from Banach-Steinhaus' theorem (cf. Nagy [23],

p. 9) that $\| u_n\|$ must be bounded. Hence $T^{*-1}$ is continuous, and since it is obviously closed, we conclude that $T^{*-1}$ is defined in a closed subspace.

The sufficiency of the condition is easily proved directly but follows also as a corollary of the next lemma.

LEMMA 1.2. The densely defined closed operator T has a bounded right inverse S if and only if  $T^{*-1}$  exists and is continuous. $^{1}$

PROOF. Since $TS = I$ implies that $\mathcal{R}_T = H$, it follows from the part of Lemma 1.1, which we have proved, that a bounded right inverse can only exist if $T^{* - 1}$ is continuous. The remaining part of Lemma 1.1 will also follow when we have constructed the right inverse in Lemma 1.2.

In virtue of a well-known theorem of von Neumann [24], the operator  $TT^{*}$  is self-adjoint and positive. Under the conditions of the lemma we have

$$
(T T ^ {*} u, u) = (T ^ {*} u, T ^ {*} u) \geq C ^ {2} (u, u), \quad u \in \mathcal {D} _ {T T ^ {*}},
$$

where C is a positive constant. Hence  $TT^{*} \geq C^{2}I$ . Let A be the positive square root of  $TT^{*}$ . Since  $A^{2} \geq C^{2}I$ , it follows from the spectral theorem that  $O < A^{-1} \leq C^{-1}I$ . The operator  $A^{-1}$  is bounded and self-adjoint,  $\|A^{-1}\| \leq C^{-1}$ . Furthermore, the operator  $T^{*}A^{-1}$  is isometric according to von Neumann's theorem. Now we define

$$
S = T ^ {*} (T T ^ {*}) ^ {- 1} = T ^ {*} A ^ {- 1} A ^ {- 1}.\tag{1.1.6}
$$

Since S is the product of an isometric operator and  $A^{-1}$ , it must be bounded, and we have  $\|S\|\leq C^{-1}$ . Finally, it is obvious that TS=I.

LEMMA 1.3. The densely defined closed operator T has a completely continuous right inverse S if and only if  $T^{*-1}$  exists and is completely continuous.

PROOF. We first note that the operator S given by (1.1.6) is completely continuous if  $T^{*-1}$  and consequently  $A^{-1}$  is completely continuous. This proves one half of the lemma. Now suppose that there exists a completely continuous right inverse S. If  $u \in D_{T*}$ , we have for any  $v \in H$

$$
(u, v) = (u, T S v) = \left(S ^ {*} T ^ {*} u, v\right),
$$

and therefore $u = S^{*}T^{*}u$. Hence, if $v \in \mathcal{R}_{T^*}$, we have $T^{*-1}v = S^{*}v$, which proves that $T^{*-1}$ is completely continuous, since it is a restriction of a completely continuous operator.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">H,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  This means that S is continuous and defined in the whole of H, and satisfies the equality TS = I, where I is the identity operator.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$TS = I,$</span></small>

## 1.2. The definition of differential operators

Let $\Omega$ be a $\nu$-dimensional infinitely differentiable manifold. We shall denote by $C^{\infty}(\Omega)$ the set of infinitely differentiable functions defined in $\Omega$, and by $C_0^\infty (\Omega)$ the set of those functions in $C^\infty (\Omega)$ which vanish outside a compact set in $\Omega$. When no confusion seems to be possible, we also write simply $C^\infty$ and $C_0^\infty$.

A transformation P from  $C^{\infty}(\Omega)$  to itself is called a differential operator, if, in local coordinate systems  $(x^{1},\ldots,x^{n})$ , it has the form

$$
p u = \sum a ^ {\alpha_ {1}} \dots^ {\alpha_ {k}} (x) \frac {1}{i} \frac {\partial}{\partial x ^ {\alpha_ {1}}} \dots \frac {1}{i} \frac {\partial}{\partial x ^ {\alpha_ {k}}} u,\tag{1.2.1}
$$

where the sum contains only a finite number of terms $\neq 0$, and the coefficients $a^{\alpha_1\ldots \alpha_k}$ are infinitely differentiable functions of $x$ which do not change if we permute the indices $\alpha_{j}$. We shall denote the sequence $(\alpha_{1},\ldots ,\alpha_{k})$ of indices between 1 and $\nu$ by $\alpha$ and its length $k$ by $|\alpha|$. Furthermore, we set

$$
D _ {i} = \frac {1}{i} \frac {\partial}{\partial x ^ {i}}, \quad D _ {\alpha} = D _ {\alpha_ {1}} \dots D _ {\alpha_ {k}}.
$$

Formula (1.2.1) then takes a simplified form, which will be used throughout:

$$
P u = \sum a ^ {\alpha} (x) D _ {\alpha} u.\tag{1.2.2}
$$

Here the summation shall be performed over all sequences  $\alpha$ .

We shall say that we have a differential operator with constant coefficients, if  $\Omega$  is a domain in the v-dimensional real vector space  $R^{v}$ , and the coefficients in (1.2.2) are constant, when the coordinates are linear.

Let $\varrho$ be a fixed density in $\Omega$, i.e. $\varrho(x)$ is a positive function, defined in every local coordinate system, such that $\varrho(x)dx^{1}\ldots dx^{\nu}$ is an invariant measure, which will be denoted $dx$. We require that $\varrho(x)$ shall be infinitely differentiable, and, in cases where $P$ has constant coefficients, we always take $\varrho(x)=\text{constant}$.

The differential operators shall be studied in the Hilbert space  $L^{2}$  of all (equivalence classes of) square integrable functions with respect to the measure dx, the scalar product in this space being

$$
(u, v) = \int u (x) \overline {{v (x)}} d x.\tag{1.2.3}
$$

With respect to this scalar product we define the algebraic adjoint $\widetilde{P}$ of $P$ as follows.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">are,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  We restrict ourselves to the infinitely differentiable case for simplicity in statements; most arguments and results are, however, more general and will later, in Chapter IV, be used under the weaker condition of a sufficient degree of differentiability.</span></small>

Let $v \in C^{\infty}$ and let u be any function in $C_0^\infty$. Integrating $(Pu, v)$ by parts, we find that there is a unique differential operator $\overline{p}$ such that

$$
(P u, v) = (u, \bar {P} v).\tag{1.2.4}
$$

In fact, we obtain

$$
\overline {{{P}}} v = \varrho^ {- 1} \sum D _ {\alpha} (\varrho \bar {a} ^ {\alpha} v).
$$

When the coefficients are constant we thus obtain  $\bar{p}$  by conjugating the coefficients, which motivates our notation.

LEMMA 1.4. The operator P, defined for those functions u in  $C^{\infty}$  for which u and Pu are square integrable, is pre-closed in  $L^{2}$ .

Proof. Let $u_{n}$ be a sequence of functions in this domain such that $u_{n} \to 0$ and $P u_{n} \to v$ (with $L^2$-convergence). Then we have for any $f \in C_0^\infty$

$$
(v, f) = \lim (P u _ {n}, f) = \lim (u _ {n}, \bar {P} f) = 0.
$$

Hence v = 0, which proves the lemma.

REMARK. It follows from the trivial proof that Lemma 1.4 would also hold if, for example, we consider P as an operator from  $L^{2}$  to C, the space of continuous functions with the uniform norm.

Lemma 1.4 justifies the following important definition.

DEFINITION 1.1. The closure $P_0$ of the operator in $L^2$ with domain $C_0^\infty$, defined by $P$, is called the minimal operator defined by $P$. The adjoint $P$ of the minimal operator $\overline{P}_0$, defined by $\overline{P}$, is called the maximal operator defined by $P$.

The definition of the maximal operator means that $u$ is in $\mathcal{D}_P$ and $Pu = f$ if and only if $u$ and $f$ are in $L^2$, and for any $v \in C_0^\infty$ we have

$$
(f, v) = (u, \overline {{{P}}} v).
$$

Operators defined in this way are often called weak extensions. In terms of the more general concept of distributions (see Schwartz [28]), we might also say that the domain consists of those functions u in  $L^{2}$  for which Pu in the sense of the theory of distributions is a function in  $L^{2}$ .

If $u \in C^{\infty}$ and $u$ and $P u$ are square integrable, it follows from (1.2.4) that $P u$ exists and equals $P u$. This is of course the idea underlying the definition. Since $P$ is an adjoint operator, it is closed and therefore an extension of $P_0$.

It is unknown to the author whether in general P is the closure of its restriction to  $D_{P} \cap C^{\infty}$ . For elliptic second order equations in domains with a smooth boundary this follows from the results of Birman [1]. If P is a homogeneous operator with constant coefficients and  $\Omega$  is starshaped with respect to every point in an open set, it is also easily proved by regularization. In section 3.9 we shall prove an affirmative result for a class of differential operators with constant coefficients, when  $\Omega$  is any domain.

We now illustrate Definition 1.1 by an elementary example. Let $\Omega$ be the finite interval $(a, b)$ of the real axis, and let $P$ be the differential operator $d^n / dx^n$. It is immediately verified that the domain of $P$ consists of those $n-1$ times continuously differentiable functions for which $u^{(n-1)}$ is absolutely continuous and has a square integrable derivative. The domain of $P_0$ consists of those functions in the domain of $P$ for which

$$
u (a) = \dots = u ^ {(n - 1)} (a) = 0, \quad u (b) = \dots = u ^ {(n - 1)} (b) = 0,
$$

that is, those which have vanishing Cauchy data in the classical sense at a and b with respect to the differential operator P.

The same result is true under suitable regularity conditions for any ordinary differential operator of order n. Hence, in general, the maximal (minimal) domain of an ordinary differential operator is contained in the maximal (minimal) domain of any ordinary differential operator of lower or equal order. For partial differential operators, this result is no longer valid, but we shall find a satisfactory substitute. Our results are most conveniently described in terms of the following definition.

DEFINITION 1.2. If $\mathcal{D}_{P_{0}}\subset\mathcal{D}_{Q_{0}}$, we shall say that the operator $P$ is stronger than the operator $Q$ and that $Q$ is weaker than $P$. If $P$ is both weaker and stronger than $Q$, i.e., if $\mathcal{D}_{P_{0}}=\mathcal{D}_{Q_{0}}$, we shall say that $P$ and $Q$ are equally strong.$^{1}$

We now pose the problem to determine the set of those operators Q which are weaker than a given operator P. It is clear that the answer is closely connected with the regularity properties and the boundary properties of the functions in  $D_{P_{0}}$ . The question is reduced to a concrete problem by the following lemma.

LEMMA 1.5. The operator Q is weaker than the operator P if and only if there is a constant C such that

$$
\| Q u \| ^ {2} \leq C (\| P u \| ^ {2} + \| u \| ^ {2}), \quad u \in C _ {0} ^ {\infty}.\tag{1.2.5}
$$

PROOF. If $Q$ is weaker than $P$, it follows from Theorem 1.1 that

$$
\left\| Q _ {0} u \right\| ^ {2} \leq C (\left\| P _ {0} u \right\| ^ {2} + \left\| u \right\| ^ {2}), \quad u \in \mathcal {D} _ {P _ {0}},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Note that these notions depend on the basic manifold  $\Omega$ .</span></small>

which implies (1.2.5). On the other hand, suppose that (1.2.5) is valid. If $u \in \mathcal{D}_{P_0}$, we can find a sequence $u_n$ of functions in $C_0^\infty$ such that

$$
u _ {n} \rightarrow u, \quad P u _ {n} \rightarrow P _ {0} u.
$$

Applying (1.2.5) to the functions $u_{n} - u_{m}$ we find that $Qu_{n}$ is a Cauchy sequence. Since $Q_{0}$ is closed, it follows that $u \in \mathcal{D}_{Q_{\bullet}}$.

We shall repeatedly use the criterion given by Lemma 1.5 in the following chapters. In Chapter II we shall find a simple and complete description of the operators Q with constant coefficients which are weaker than a given operator P with constant coefficients, when  $\Omega$  is a bounded domain in  $R^{r}$ . (The answer is then independent of  $\Omega$ .) In Chapter IV analogous results will be proved for a class of operators with variable coefficients.

REMARK. If $\mathcal{D}_{P_{\bullet}} \subset \mathcal{D}_{Q}$, it follows from Theorem 1.1 in the same way as in the proof of Lemma 1.5 that (1.2.5) is valid. Hence $\mathcal{D}_{P_{\bullet}} \subset \mathcal{D}_{Q}$, so that $Q$ is weaker than $P$. This shows that in Definition 1.2 we might replace the condition $\mathcal{D}_{P_{\bullet}} \subset \mathcal{D}_{Q}$ by the apparently weaker condition $\mathcal{D}_{P_{\bullet}} \subset \mathcal{D}_{Q}$. It should also be observed that, in Definition 1.2 and in most of our arguments here, we use the minimal and not the maximal differential operators in view of the fact that the relation $\mathcal{D}_{P} \subset \mathcal{D}_{Q}$ is very exceptional for partial differential operators, as will be proved in Chapter III.

We shall next deduce the conditions in order that $Q u$ should be continuous after correction on a null set for every $u \in D_{P_*}$, the operator $Q$ being interpreted in the distribution sense. Such results form a stepping-stone from the weak concept of a solution of a differential equation to the classical one. Sobolev has studied similar questions (see [30]), but our results overlap very little with his.

LEMMA 1.6. In order that $Qu$ should equal a bounded function in the distribution sense for every $u \in D_{P_0}$, it is necessary and sufficient that there is a constant $C$ such that

$$
\sup _ {\Omega} | Q u | ^ {2} \leq C (\| \mathcal {P} u \| ^ {2} + \| u \| ^ {2}), \quad u \in C _ {0} ^ {\infty}.\tag{1.2.6}
$$

If (1.2.6) is satisfied, $Qu$ is a uniformly continuous function in $\Omega$ after correction on a null set, if $u \in \mathcal{D}_{P_0}$, and $Qu$ tends to zero at the boundary in the sense that to every $\varepsilon > 0$ there is a compact set $K$ in $\Omega$, so that $|Qu(x)| < \varepsilon$ in $\Omega - K$.

PROOF. That (1.2.6) is a necessary condition follows, if we consider Q as an operator from  $L^{2}$  to  $L^{\infty}$  and apply Theorem 1.1, which is possible in virtue of the remark following Lemma 1.4. Conversely, let (1.2.6) be satisfied. If  $u_{n}$  is a sequence of functions in  $C_{0}^{\infty}$  such that  $u_{n} \to u$  and  $P u_{n} \to P_{0} u$, where u is an arbitrary function in  $D_{P_{0}}$, it follows that  $Qu_{n}$

is uniformly convergent. Since the limit must equal $Qu$ a.e., the last statement of the lemma follows.

The last assertion of the lemma may also be formulated as follows: Qu is continuous and vanishes at infinity in the Alexandrov compactification of  $\Omega$ .

We now turn to another matter, the existence of solutions of differential equations. Lemma 1.1 and the definition of P as the adjoint of  $\overline{P}_{0}$  prove the following result.

LEMMA 1.7. The equation $Pu = f$ has, for any $f \in L^2$, at least one solution $u \in \mathcal{D}_p$, if, and only if, $\overline{P}_0$ has a continuous inverse, i.e., if

$$
(u, u) \leq C ^ {2} (\bar {P} u, \bar {P} u), \quad u \in C _ {0} ^ {\infty},\tag{1.2.7}
$$

where $C$ is a constant.

In Chapters II and IV it will be proved that (1.2.7) is valid under very mild assumptions about p.

## 1.3. Cauchy data and boundary problems

The example on page 169 makes it justifiable to say that the functions in $\mathcal{D}_P$, are those which have vanishing Cauchy data with respect to the operator $P$, and we are thus led to the following definition.

DEFINITION 1.3. The quotient space

$$
C = G _ {P} / G _ {P _ {\bullet}}\tag{1.3.1}
$$

with the quotient norm is called the Cauchy space of $P$. If $u \in \mathcal{D}_p$, the residue class of the pair $[u, Pu]$ is an element of $C$, which is called the Cauchy datum of $u$ and is denoted by $\Gamma u$.

It follows from the definition that two functions in  $D_{p}$ , which only differ by a function in  $C_{0}^{\infty}(\Omega)$ , have the same Cauchy data. When the coefficients are constant it is easy to prove (Lemma 2.11) that every function in  $D_{p}$ , which vanishes outside a compact set in  $\Omega$ , is also in  $D_{p}$ . It then follows that two functions in  $D_{p}$ , which are identical outside a compact set in  $\Omega$ , have the same Cauchy data. It is of course natural to expect that this is valid for very general operators though we have not obtained any proof.

The example on page 169 also suggests the following definition.

DEFINITION 1.4. Let $B$ be a linear manifold in the Cauchy space $C$ of $P$. The problem to find a solution $f$ of

$$
P f = g, \Gamma f \in B,\tag{1.3.2}
$$

for arbitrarily given  $g \in L^{2}$  is called a linear homogeneous boundary problem.  $\Gamma f \in B$  is the boundary condition.

Let $\hat{P}$ be the restriction of $P$ to those $f$ for which $\Gamma f \in B$. Then $\hat{P}$ is linear and

$$
P _ {0} \subset \hat {P} \subset P.
$$

Conversely, any linear operator  $\hat{P}$  with this property corresponds to exactly one linear manifold B in C.

DEFINITION 1.5. The boundary problem (1.3.2) is said to be (completely) correctly posed, if $\hat{P}$ has a (completely) continuous inverse, defined in the whole of $L^2$.

This definition and the following result are essentially due to Višik [34], who also considers less restrictive definitions.

THEOREM 1.2. There exist (completely) correctly posed boundary problems for the operator P if and only if  $P_{0}$  and  $\overline{P}_{0}$  have (completely) continuous inverses.

PROOF. Suppose that there exists a (completely) correctly posed boundary problem, and let  $\hat{P}$  be the corresponding operator. Since  $\hat{P}^{-1}$  is (completely) continuous and  $\hat{P} \supset P_{0}$ , it follows that  $P_{0}^{-1}$  must be (completely) continuous, and since  $\hat{P}^{-1}$  is a right inverse of P, it follows from Lemma 1.2 (Lemma 1.3) that  $\overline{P}_{0}^{-1}$  is (completely) continuous.

Now assume that  $P_{0}^{-1}$  and  $\bar{P}_{0}^{-1}$  are (completely) continuous. In virtue of the continuity of  $P_{0}^{-1}$, the range  $R_{P_{0}}$  of  $P_{0}$  is closed. Let  $\pi$  be the orthogonal projection on  $R_{P_{0}}$. If S is the right inverse of P constructed in Lemma 1.2 (Lemma 1.3), the operator T defined by

$$
T f = P _ {0} ^ {- 1} (\pi f) + S ((I - \pi) f), \quad f \in L ^ {2},
$$

is (completely) continuous. Since

$$
P T f = \pi f + (I - \pi) f = f,
$$

the operator $T$ has an inverse $\hat{P}$, and $\hat{P} \subset P$. Furthermore, $T \supset P_0^{-1}$ and hence $\hat{P} \supset P_0$, so that $P_0 \subset \hat{P} \subset P$. Since $\hat{P}^{-1}$ is (completely) continuous and defined in the whole of $L^2$, the proof is completed.

We shall next derive a description of the correctly posed boundary conditions, which differs from Višik's. Let U be the set of all solutions u of the homogeneous equation Pu = 0. This is a closed subspace of  $L^{2}$ , since P is a closed operator.

LEMMA 1.8. Suppose that $P_0^{-1}$ is continuous. Then the restriction $\gamma$ of the boundary operator $\Gamma$ to $U$ maps $U$ topologically onto a closed subspace $\Gamma U$ of $C$.

Proof. Let $A$ be a constant such that

$$
\left\| P _ {0} f \right\| \geq A \| f \|, \quad f \in \mathcal {D} _ {P _ {0}}.
$$

Then we have, if $u \in U$,

$$
\begin{array}{r l} \| u \| ^ {2} & \geq \| \Gamma u \| ^ {2} = \inf _ {f \in D _ {P _ {0}}} (\| u - f \| ^ {2} + \| P _ {0} f \| ^ {2}) \geq \inf _ {f \in L ^ {2}} (\| u - f \| ^ {2} + A ^ {2} \| f \| ^ {2}) \\ & = \inf \left\{(1 + A ^ {2}) \left\| f - \frac {u}{1 + A ^ {2}} \right\| ^ {2} + \| u \| ^ {2} A ^ {2} / (1 + A ^ {2}) \right\} = \| u \| ^ {2} A ^ {2} / (1 + A ^ {2}). \end{array}
$$

This proves the lemma.

THEOREM 1.3. Suppose that $P_0^{-1}$ and $\overline{P}_0^{-1}$ are continuous. Let $B$ be a linear manifold in $C$, and let $\hat{P}$ be the corresponding operator. Then $\hat{P}$ is closed if and only if $B$ is closed. $\hat{P}^{-1}$ exists if and only if $B$ and $\Gamma U$ have only the origin in common. $\hat{P}^{-1}$ is continuous and defined in the whole of $L^2$ if and only if $C$ is the topological sum of $B$ and $\Gamma U$.

PROOF. The first assertion follows at once from the definition of the topology in quotient spaces. In fact, a set in a quotient space is by definition open (closed) if and only if its inverse image is open (closed).

$\hat{P}^{-1}$ has a sense if and only if $\hat{P}f \neq 0$ when $0 \neq f \in \mathcal{D}_{\hat{p}}$, that is, if no solution $u \neq 0$ of $Pu = 0$ satisfies the boundary condition. But this means that $0$ is the only common element of $\Gamma U$ and $B$.

Now suppose that C is the topological sum of  $\Gamma U$  and B. From the preceding remark it follows that  $\hat{P}^{-1}$  exists, and we have to prove that it is bounded. The assumption means that there exists a bounded (oblique) projection  $\pi$  of C on  $\Gamma U$  along B. Let S be the bounded right inverse of P, which was constructed in Lemma 1.2, and let  $\gamma$  be the restriction of  $\Gamma$  to U, which was studied in Lemma 1.7. Then the operator

$$
T g = S ^ {- 1} g - \gamma^ {- 1} \pi \Gamma S ^ {- 1} g
$$

is defined in the whole of $L^2$ and is a continuous operator. Obviously, $Tg \in \mathcal{D}_P$ and $PTg = g - 0$. Furthermore,

$$
\Gamma T g = \Gamma S ^ {- 1} g - \pi \Gamma S ^ {- 1} g \in B,
$$

so that $Tg \in \mathcal{D}_{\hat{P}}$ and $\hat{P}Tg = PTg = g$. Hence $\hat{P}^{-1} = T$, which proves the assertion.

On the other hand, suppose that $\hat{P}^{-1}$ is continuous and defined everywhere. Then the mapping

$$
G _ {P} \ni [ f, P f ] \rightarrow f - \hat {P} ^ {- 1} P f \in U
$$

is continuous. We have $f - \hat{P}^{-1} Pf = 0$ if and only if $f \in \mathcal{D}_{\hat{P}}$. The mapping

$$
G _ {P} \ni [ f, P f ] \rightarrow \Gamma (f - \hat {P} ^ {- 1} P f) \in \Gamma U
$$

is also continuous and, since it vanishes in  $G_{P_{0}}$ , it defines a continuous mapping  $\pi$  from  $G_{P}/G_{P_{0}} = C$  to  $\Gamma U$ . We have  $\pi\varphi = 0$  if and only if  $\varphi \in B$ . Now  $\pi$  leaves the elements of  $\Gamma U$  invariant. Hence  $\pi$  is a projection on  $\Gamma U$  along B, and from the continuity of  $\pi$  our assertion follows.

We finally sketch a similar study of the completely correctly posed boundary problems, when  $P_{0}$  and  $\bar{P}_{0}$  have completely continuous inverses, by introducing a new mode of convergence in C. We shall say that a sequence  $[u_{n}, v_{n}]$  of elements in  $L^{2} \times L^{2}$  is w-convergent, if  $u_{n}$  converges strongly and  $v_{n}$  converges weakly. In C we define the quotient w-convergence: a sequence  $\varphi_{n}$  of elements in C is w-convergent, if there exists a w-convergent sequence  $[f_{n}, Pf_{n}] \in G_{P}$  such that  $\Gamma f_{n} = \varphi_{n}$ .

We shall prove that the operator  $\gamma$  from U to  $\Gamma U$  transforms the  $L^{2}$ -convergent sequences in U and the w-convergent sequences in  $\Gamma U$  into each other. In fact,  $\Gamma u_{n}$  is obviously w-convergent if  $u_{n}$  is convergent. Conversely, if  $\Gamma u_{n}$  is w-convergent, there exist elements  $f_{n} \in D_{P_{0}}$ , so that  $u_{n} - f_{n}$  converges strongly and  $P_{0}f_{n}$  converges weakly. Since we have  $f_{n} = P_{0}^{-1}(P_{0}f_{n})$ , it follows from the weak convergence of  $P_{0}f_{n}$  and the complete continuity of  $P_{0}^{-1}$  that  $f_{n}$  is strongly convergent. Hence  $u_{n}$  is strongly convergent, which proves our assertion. Using Lemma 1.8 we now see that in  $\Gamma U$  the w-convergence is equivalent to strong convergence.

A slight modification of the proof of Theorem 1.3 shows that the operator $\hat{P}$, corresponding to a linear manifold $B$ in $C$, has a completely continuous inverse, defined in the whole of $L^2$, if and only if $C$ is the direct sum of $B$ and $\Gamma U$, and the projection $\pi$ of $C$ on $\Gamma U$ along $B$ is $w$-continuous in the sense that it transforms $w$-convergent sequences into $w$-convergent (and hence strongly convergent) sequences.

## CHAPTER II

## Minimal Differential Operators with Constant Coefficients

## 2.0. Introduction

Let P be a differential operator with constant coefficients and let  $\Omega$  be a domain in  $R^{v}$ . In Chapter I we introduced the minimal differential operator  $P_{0}$  in  $L^{2}(\Omega)$ , defined by P. The object of this chapter is to study  $P_{0}$  more closely, We first restrict ourselves to the case where  $\Omega$  is bounded, and can then obtain fairly complete results. Some remarks on the case of non-bounded domains are given at the end of the chapter.

We first establish the boundedness of the inverse of a minimal differential operator with constant coefficients for bounded  $\Omega$  by means of the Laplace transformation, using

a lemma by Malgrange [20]. This result shows that Lemma 1.7 is always applicable, i.e. that the equation $Pu = f$ has a square integrable solution $u$ for any $f \in L^2(\Omega)$.

We then turn to the exact determination of the differential operators which are weaker than P. With  $D = (D_{1}, \ldots, D_{\nu})$ , where  $D_{t} = i^{-1} \partial/\partial x^{t}$ , we may write  $P = P(D)$ , where  $P(\xi)$  is a polynomial in the vector  $\xi = (\xi_{1}, \ldots, \xi_{\nu})$ . Now set

$$
\tilde {P} (\xi) = \left(\Sigma \mid P ^ {(\alpha)} (\xi) \right\rvert^ {2}) ^ {\frac {1}{2}},
$$

where  $P^{(\alpha)}$  are derivatives of P, and the summation extends over all  $\alpha$ . Then Q is weaker than P if and only if

$$
\frac {\tilde {Q} (\xi)}{\tilde {P} (\xi)} <   C.\tag{2.0.1}
$$

To prove this result we use a generalization of the energy integral method. For equations of higher order than two, this method was first used by Leray [19]. In the general case considered here, where the lower order terms of the operators have great importance, it has been necessary to develop an algebra of energy integrals in a systematic manner. It may be remarked that, for some special second order equations, similar questions have been posed and solved by Ladyzenskaja [18], even under less restrictive boundary conditions.

As a consequence of our result we find that the product of a function $u \in \mathcal{D}_{P_0}$ and a function $\psi$, which is $C^\infty$ in a neighbourhood of $\overline{\Omega}$, is in $\mathcal{D}_{P_0}$. Hence we find that the relation $u \in \mathcal{D}_{P_0}$ has a local character. We then study this relation in the interior and at the boundary of $\overline{\Omega}$.

The inequalities derived by the energy integral method also make it possible to determine those operators Q for which Qu is continuous after correction on a null set for every  $u \in D_{P_{0}}$ . In fact, this is the case if and only if

$$
\int \frac {\tilde {Q} (\xi) ^ {2}}{\tilde {P} (\xi) ^ {2}} d \xi <   \infty .\tag{2.0.2}
$$

The inequalities (2.0.1) and (2.0.2) only involve the quotient $\tilde{Q}(\xi)/\tilde{P}(\xi)$. In section 2.8 we also give conditions in terms of this quotient in order that $Qu\in L^{q}$ for every $u\in\mathcal{D}_{P_{q}}$ and in order that $Qu$ should exist in manifolds of dimension less than $\nu$.

We can also prove that the inverse of  $P_{0}$  is completely continuous, if  $P(\xi)$  really depends on all variables. More generally, we prove that the operator  $Q_{0}P_{0}^{-1}$  is completely continuous if and only if

$$
\frac {\tilde {Q} (\xi)}{\tilde {P} (\xi)} \rightarrow 0 \quad \text { when } \xi \rightarrow \infty .\tag{2.0.3}
$$

## 2.1. Notations and formal properties of differential operators with constant coefficients

Let $R^{\nu}$ be the real $\nu$-dimensional space with elements $x = (x^{1},\ldots ,x^{\nu})$ and let $C_{\nu}$ be the complex $\nu$-dimensional space with elements $\zeta = (\zeta_1,\dots ,\zeta_\nu)$. In precisely one way we can write $\zeta = \xi +i\eta$, where $\xi$ and $\eta$, as in the whole paper, denote real vectors. The variables $x$ and $\zeta$ will be considered as dual with respect to the bilinear form

$$
\langle x, \zeta \rangle = \sum_ {1} ^ {\nu} x ^ {k} \zeta_ {k}.
$$

A polynomial $P(\zeta)$ can be written as a finite sum

$$
P (\zeta) = \sum a ^ {\alpha} \zeta_ {\alpha},\tag{2.1.1}
$$

where  $\alpha=(\alpha_{1},\ldots,\alpha_{k})$  is a sequence of indices between 1 and  $\nu$, the  $a^{\alpha}$  are complex constants which do not change, if the indices in  $\alpha$  are permuted, and  $\zeta_{\alpha}=\zeta_{\alpha_{1}}\cdots\zeta_{\alpha_{k}}$. The length k of the sequence  $\alpha$  is denoted by  $|\alpha|$. The polynomial (2.1.1) defines a differential operator  $\mathcal{P}=P(D)$  operating on the functions in  $R^{\nu}$,

$$
P (D) = \sum a ^ {\alpha} D _ {\alpha}\tag{2.1.2}
$$

(see section 1.2). The polynomials in $C_v$ and the differential operators in $R^\nu$ are thus in a one-to-one correspondence, and this correspondence is in fact independent of the choice of coordinates since

$$
P (D) e ^ {i \langle x, \zeta \rangle} = P (\zeta) e ^ {i \langle x, \zeta \rangle}.
$$

By S we denote the space of infinitely differentiable rapidly decreasing functions introduced by L. Schwartz [28]. Denoting the Fourier transform of a function u in S by  $\hat{u}$ ,

$$
\hat {u} (\xi) = (2 \pi) ^ {- \nu / 2} \int u (x) e ^ {- i \langle x, \xi \rangle} d x,\tag{2.1.3}
$$

the Fourier transform of $P(D)u$ is $P(\xi)\hat{u} (\xi)$, and it follows from Parseval's formula that

$$
\int | P (D) u | ^ {2} d x = \int | P (\xi) \hat {u} (\xi) | ^ {2} d \xi .\tag{2.1.4}
$$

We shall repeatedly need the analogue of Leibniz' formula for general differential polynomials

$$
P (D) (u v) = P \left(D _ {u} + D _ {v}\right) u v.\tag{2.1.5}
$$

The interpretation of this formula is that, after  $P(D_{u} + D_{v})$  has been expanded in powers of  $D_{u}$  and  $D_{v}$ , we shall let  $D_{u}$  operate only on u and  $D_{v}$  operate only on v. Formula (2.1.5)

is, of course, an immediate consequence of the rule for differentiating a product. Now we have by Taylor's formula

$$
P (\xi + \eta) = \sum \frac {\eta_ {\alpha}}{| \alpha | !} P ^ {(\alpha)} (\xi),
$$

where

$$
P ^ {(\alpha)} = \frac {\partial^ {| \alpha |} P}{\partial \xi_ {\alpha}} = \frac {\partial^ {k} P}{\partial \xi_ {\alpha_ {1}} \cdots \partial \xi_ {\alpha_ {k}}}.
$$

For $|\alpha| = k$ the $k$ indices in $\alpha$ shall run independently from 1 to $\nu$. Leibniz' formula (2.1.5) now takes the more explicit form

$$
P (D) (u v) = \sum \frac {D _ {\alpha} v}{| \alpha | !} P ^ {(\alpha)} (D) u.\tag{2.1.6}
$$

## 2.2. Estimates by Laplace transforms

Let $\Omega$ be a bounded domain in $R^{\nu}$, and let $P(D)$ be a differential operator with constant coefficients. We shall prove the continuity of the inverse of the minimal operator $P_{0}$.

THEOREM 2.1. The operator $P_0$ has a continuous inverse, i.e. there exists a constant $C$ such that

$$
\left\| u \right\| \leq C \left\| P (D) u \right\|, \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{2.2.1}
$$

PROOF. We form the Laplace transform of u, defined by

$$
\hat {u} (\zeta) = \hat {u} (\xi + i \eta) = (2 \pi) ^ {- r / 2} \int e ^ {- i \langle x, \xi + i \eta \rangle} u (x) d x.
$$

This is an entire analytic function since u has compact support. The Laplace transform of  $P(D)u$  is  $P(\zeta)\hat{u}(\zeta)$ . Now the proof of (2.2.1) follows easily from the following lemma on analytic functions of one variable, analogous to one used previously by Malgrange [20].

LEMMA 2.1. If $g(z)$ is an analytic function of a complex variable $z$ for $|z| \leq 1$, and $r(z)$ is a polynomial with highest coefficient $A$, then

$$
\left| A g (0) \right| ^ {2} \leq (2 \pi) ^ {- 1} \int_ {0} ^ {2 \pi} \left| g \left(e ^ {i \theta}\right) r \left(e ^ {i \theta}\right) \right| ^ {2} d \theta .\tag{2.2.2}
$$

PROOF OF LEMMA 2.1. Let $z_{j}$ be the zeros of $r(z)$ in the unit circle and set

$$
r (z) = q (z) \prod_ {j} \frac {z - z _ {j}}{\bar {z} _ {j} z - 1}.
$$

On the unit circle we have $|r(z)| = |q(z)|$, and $q(z)$ is analytic in the circle. Hence we have

$$
(2 \pi) ^ {- 1} \int | g (e ^ {i \theta}) r (e ^ {i \theta}) | ^ {2} d \theta = (2 \pi) ^ {- 1} \int | g (e ^ {i \theta}) q (e ^ {i \theta}) | ^ {2} d \theta \geq | g (0) q (0) | ^ {2}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12 - 553810. Acta Mathematica. 94. Imprimé le 26 septembre 1955.</span></small>

Now $q(0) / A$ is, apart from a factor $\pm 1$, the product of the zeros of $r(z)$ outside the unit circle. Hence $|q(0)| \geq |A|$, which proves the lemma.

We now complete the proof of the theorem. Choose a real vector  $\xi_{0}$  such that  $p(\xi_{0}) \neq 0$ , where p is the principal part of P, that is, the homogeneous part of highest degree of P. Applying the lemma to the analytic function  $\hat{u}(\zeta + t\xi_{0})$  and the polynomial  $P(\zeta + t\xi_{0})$ , considered as functions of the complex variable t, we get

$$
\left| \hat {u} (\zeta) p (\xi_ {0}) \right| ^ {2} \leq (2 \pi) ^ {- 1} \int \left| \hat {u} (\zeta + e ^ {i \theta} \xi_ {0}) P (\zeta + e ^ {i \theta} \xi_ {0}) \right| ^ {2} d \theta .
$$

Letting $\zeta = \xi$ be real and integrating with respect to $\xi$ we obtain

$$
\begin{array}{r l} \left| p (\xi_ {0}) \right| ^ {2} \int | \hat {u} (\xi) | ^ {2} d \xi & \leq (2 \pi) ^ {- 1} \iint | \hat {u} (\xi + e ^ {i \theta} \xi_ {0}) P (\xi + e ^ {i \theta} \xi_ {0}) | ^ {2} d \xi d \theta \\ & = (2 \pi) ^ {- 1} \int d \theta \int | \hat {u} (\xi + i \xi_ {0} \sin \theta) P (\xi + i \xi_ {0} \sin \theta) | ^ {2} d \xi . \end{array}
$$

By Parseval's formula we can calculate the integrals with respect to $\xi$, which gives

$$
\left| p \left(\xi_ {0}\right) \right| ^ {2} \int | u (x) | ^ {2} d x \leq (2 \pi) ^ {- 1} \int d \theta \int | P (D) u (x) | ^ {2} e ^ {2 \langle x, \xi_ {0} \rangle \sin \theta} d x.
$$

Let $C$ be the supremum of $e^{|\langle x, \xi_0\rangle|} / |p(\xi_0)|$ when $x \in \Omega$. Then we have

$$
\int \left| u (x) \right| ^ {2} d x \leq C ^ {2} \int \left| P (D) u (x) \right| ^ {2} d x,
$$

which proves (2.2.1).

By choosing  $\xi_{0}$  in a suitable fashion we could get a good estimate of the magnitude of the constant C. We shall not do so, since still better results can be obtained by a different method later in this chapter.

## 2.3. The differential operators weaker than a given one

Let $P(D)$ be a differential operator with constant coefficients and let $\Omega$ be a bounded domain. We shall determine those operators $Q(D)$ with constant coefficients which are weaker than $P(D)$ in the sense of Definition 1.2, i.e. such that with some constant C

$$
\left\| Q (D) u \right\| ^ {2} \leq C (\left\| P (D) u \right\| ^ {2} + \left\| u \right\| ^ {2}), \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{2.3.1}
$$

In virtue of Theorem 2.1 this is equivalent to

$$
\left\| Q (D) u \right\| ^ {2} \leq C ^ {\prime} \left\| P (D) u \right\| ^ {2}, \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{2.3.1)'}
$$

In formulating the result it is convenient to use the function

$$
\tilde {P} (\xi) = \left(\sum \left| P ^ {(\alpha)} (\xi) \right| ^ {2}\right) ^ {\frac {1}{2}}.\tag{2.3.2}
$$

This notation will be retained in the whole chapter, also with $P$ replaced by other letters.

THEOREM 2.2. A necessary and sufficient condition in order that $Q(D)$ should be weaker than $P(D)$ in a bounded domain $\Omega$ is that

$$
\frac {\tilde {Q} (\xi)}{\tilde {P} (\xi)} <   C,\tag{2.3.3}
$$

for every real $\xi$, where $C$ is a constant.

REMARK. We shall even prove that $Q(D)$ is weaker than $P(D)$ if $|Q(\xi)| / \tilde{P}(\xi) < C$. Hence this condition is equivalent to (2.3.3), with a different constant $C$.

Theorem 2.2 has a central role in this chapter. The full proof is long and will fill the next sections. That (2.3.3) follows from (2.3.1) is proved in this section. In 2.4 we develop some algebraic aspects of energy integrals, and the analytical consequences are given in section 2.5. Using these results we complete the proof of Theorem 2.2 in section 2.6. At the same time we get a new proof of Theorem 2.1, that does not use Laplace transforms.

We now prove that (2.3.3) follows, if we suppose that (2.3.1) holds true. To make use of this inequality, take a function  $\psi\in C_{0}^{\infty}(\Omega)$ ,  $\psi\neq0$ , and set with real constant  $\xi$

$$
u (x) = \psi (x) e ^ {i \langle x, \xi \rangle}.\tag{2.3.4}
$$

This function is in $C_0^\infty(\Omega)$, and from Leibniz' formula (2.1.6) it follows that

$$
P (D) u (x) = e ^ {i \langle x, \xi \rangle} \sum P ^ {(\alpha)} (\xi) \frac {D _ {\alpha} \psi (x)}{| \alpha | !},\tag{2.3.5}
$$

and similarly with $P$ replaced by $Q$. If we introduce the notation

$$
\psi_ {\alpha \beta} = \frac {1}{| \alpha | ! | \beta | !} \int D _ {\alpha} \psi \overline {{{{D _ {\beta} \psi}}}} d x,\tag{2.3.6}
$$

the inequality (2.3.1) gives

$$
\sum Q ^ {(\alpha)} (\xi) \overline {{Q ^ {(\beta)}}} (\xi) \psi_ {\alpha \beta} \leq C (\sum P ^ {(\alpha)} (\xi) \overline {{P ^ {(\beta)}}} (\xi) \psi_ {\alpha \beta} + \psi_ {0 0}).\tag{2.3.7}
$$

If $m$ is the highest of the orders of $P$ and $Q$, the sums in (2.3.7) only contain terms with $|\alpha| \leq m$ and $|\beta| \leq m$. Now let $t = (t_{\alpha})$ be an "array" of complex numbers, $0 \leq |\alpha| \leq m$, such that $t_{\alpha} = t_{\alpha'}$, when $\alpha'$ is a permutation of $\alpha$. The quadratic form in $t$ defined by

$$
\sum_ {| \alpha | \leq m} \sum_ {| \beta | \leq m} t _ {\alpha} \bar {t} _ {\beta} \psi_ {\alpha \beta} = \int \left| \sum_ {| \alpha | \leq m} \frac {t _ {\alpha} D _ {\alpha} \psi}{| \alpha | !} \right| ^ {2} d x = \int \left| \sum_ {| \alpha | \leq m} \frac {t _ {\alpha} \xi_ {\alpha}}{| \alpha | !} \right| ^ {2} | \hat {\psi} (\xi) | ^ {2} d \xi\tag{2.3.8}
$$

is positive, unless the polynomial $\sum t_{\alpha}\xi_{\alpha} / |\alpha|!$ vanishes identically, i.e. every $t_{\alpha} = 0$. Hence it follows that there is a constant $C'$ such that

$$
\sum_ {| \alpha | \leq m} \left| t _ {\alpha} \right| ^ {2} \leq C ^ {\prime} \sum_ {| \alpha | \leq m} \sum_ {| \beta | \leq m} t _ {\alpha} \bar {t} _ {\beta} \psi_ {\alpha \beta}.\tag{2.3.9}
$$

With $t_{\alpha} = Q^{(\alpha)}(\xi)$ we now get from (2.3.9) and (2.3.7) that

$$
\sum \left| Q ^ {(\alpha)} (\xi) \right| ^ {2} \leq C ^ {\prime} \sum Q ^ {(\alpha)} (\xi) \overline {{{Q ^ {(\beta)} (\xi)}}} \psi_ {\alpha \beta} \leq C C ^ {\prime} \left(\sum P ^ {(\alpha)} (\xi) \overline {{{P ^ {(\beta)} (\xi)}}} \psi_ {\alpha \beta} + \psi_ {0 0}\right),
$$

so that with a third constant $C''$

$$
\tilde {Q} (\xi) \leq C ^ {\prime \prime} \tilde {P} (\xi).
$$

## 2.4. The algebra of energy integrals

In this section we shall study some algebraic aspects of quadratic forms with constant coefficients in the derivatives of a function $u$. Such a form can be written

$$
\sum_ {\alpha , \beta} a ^ {\alpha \beta} D _ {\alpha} u \overline {{{D _ {\beta} u}}},\tag{2.4.1}
$$

where  $D_{\alpha}$  and  $D_{\beta}$  are defined in section 1.2, and  $a^{\alpha\beta}$  is invariant for permutations within  $\alpha$  or  $\beta$ . With this quadratic differential form we associate the polynomial

$$
F (\zeta , \bar {\zeta}) = \sum a ^ {\alpha \beta} \zeta_ {\alpha} \bar {\zeta} _ {\beta},\tag{2.4.2}
$$

where $\zeta = \xi + i\eta$ and $\overline{\zeta} = \xi - i\eta$. Since the value of the form (2.4.1) for $u(x) = e^{i\langle x, \zeta \rangle}$ is $e^{-2\langle x, \eta \rangle}F(\zeta, \overline{\zeta})$, the correspondence between the form (2.4.1) and the polynomial (2.4.2) is one to one and invariant for coordinate transformations. This justifies the following shorter notation

$$
F (D, \bar {D}) u \bar {u} = \sum_ {\alpha , \beta} a ^ {\alpha \beta} D _ {\alpha} u \overline {{{{D _ {\beta} u}}}}.\tag{2.4.3}
$$

In section 2.1 we introduced a correspondence between the differential operators in $R^{\nu}$ and the complex-valued polynomials in $C_{\nu}$, considered as a $\nu$-dimensional vector space with complex structure. We have now seen that the quadratic differential forms in $R^{\nu}$ can be associated with the complex-valued polynomials in $C_{\nu}$, considered as a $2\nu$-dimensional vector space with real structure.

If $\overline{F}(\zeta, \bar{\zeta})$ is the polynomial whose coefficients are the complex conjugates of those of $F(\zeta, \bar{\zeta})$, it is readily verified that

$$
\overline {{{F (D , \bar {D}) u \bar {u}}}} = \overline {{{F}}} (\bar {D}, D) u \bar {u}.\tag{2.4.4}
$$

Hence $F(D, \bar{D})u\bar{u}$ is real for every $u$ if and only if

$$
\boldsymbol {F} (\zeta , \overline {{\zeta}}) = \overline {{\boldsymbol {F}}} (\overline {{\zeta}}, \zeta) = \overline {{\boldsymbol {F} (\zeta , \overline {{\zeta}})}},
$$

i.e. if $F(\zeta, \bar{\zeta})$ is always real.

We shall need a formula for the differentiation of a quadratic differential form  $F(D, \bar{D}) u \bar{u}$ . Elementary product differentiation gives

$$
\frac {\partial}{\partial x ^ {k}} (F (D, \bar {D}) u \bar {u}) = i (D _ {k} - \bar {D} _ {k}) F (D, \bar {D}) u \bar {u}.
$$

Hence, if $G = (G^k)$ is a vector whose components are quadratic differential forms, we have

$$
\operatorname{div} (G (D, \bar {D}) u \bar {u}) = \sum_ {1} ^ {\nu} \frac {\partial}{\partial x ^ {k}} (G ^ {k} (D, \bar {D}) u \bar {u}) = F (D, \bar {D}) u \bar {u},\tag{2.4.5}
$$

where

$$
F (\zeta , \bar {\zeta}) = i \sum_ {1} ^ {\nu} (\zeta_ {k} - \bar {\zeta} _ {k}) G ^ {k} (\zeta , \bar {\zeta}) = - 2 \sum_ {1} ^ {\nu} \eta_ {k} G ^ {k} (\zeta , \bar {\zeta}).\tag{2.4.6}
$$

LEMMA 2.2. A polynomial $F(\zeta, \bar{\zeta})$ in $\zeta = \xi + i\eta$ and $\bar{\zeta} = \xi - i\eta$ can be written in the form

$$
F (\zeta , \bar {\zeta}) = - 2 \sum_ {1} ^ {\nu} \eta_ {k} G ^ {k} (\zeta , \bar {\zeta}),
$$

where $G^k$ are polynomials, if and only if $F(\xi, \xi) = 0$ when $\xi$ is real.

PROOF. That  $F(\xi, \xi) = 0$  is a necessary condition is obvious. To prove its sufficiency we observe that if  $F(\xi + i\eta, \xi - i\eta) = 0$  when  $\eta = 0$ , there are no terms free from  $\eta$  in the expansion of  $F(\xi + i\eta, \xi - i\eta)$  in powers of  $\xi$  and  $\eta$ . Hence we can write

$$
F (\xi + i \eta , \xi - i \eta) = - 2 \sum_ {1} ^ {\nu} \eta_ {k} g ^ {k} (\xi , \eta),
$$

where  $g^{k}$  are polynomials. Returning to the variables  $\zeta$  and  $\bar{\zeta}$  in  $g^{k}$ , the lemma is proved.

From the proof it follows that the vector  $(G^{1}(\zeta,\bar{\zeta}),\ldots,G^{\nu}(\zeta,\bar{\zeta}))$  is not uniquely determined in general. We shall now determine the degree of indeterminacy, that is, we shall find all vector differential forms with divergence zero.

LEMMA 2.3. If the polynomials $G^i(\zeta, \bar{\zeta})$ satisfy the identity

$$
\sum_ {1} ^ {\nu} \eta_ {i} G ^ {i} (\zeta , \overline {{\xi}}) \equiv 0,
$$

$$
G ^ {i} (\zeta , \zeta) = - 2 \sum_ {1} ^ {\nu} \eta_ {k} G ^ {i k} (\zeta , \bar {\zeta}).
$$

then there exist polynomials $G^{ik}(\zeta, \bar{\zeta})$ such that $G^{ik}(\zeta, \bar{\zeta}) = -G^{ki}(\zeta, \bar{\zeta})$ and

PROOF. If we write $G^i(\xi + i\eta, \xi - i\eta) = g^i(\xi, \eta)$, the assumption means that

$$
\sum_ {1} ^ {v} \eta_ {i} g ^ {i} (\xi , \eta) = 0.\tag{2.4.7}
$$

Since the identity (2.4.7) must also be satisfied by the parts of  $g^{i}(\xi,\eta)$ , which are homogeneous of the same degree with respect to  $\eta$ , we may suppose in the proof that the  $g^{i}$  are all homogeneous of degree m with respect to  $\eta$ . Then Euler's identity gives

$$
m g ^ {k} = \sum_ {1} ^ {\nu} \eta_ {i} \frac {\partial g ^ {k}}{\partial \eta_ {i}}.
$$

Differentiation of (2.4.7) with respect to $\eta_{k}$ gives

$$
g ^ {k} + \sum_ {1} ^ {\nu} \eta_ {i} \frac {\partial g ^ {i}}{\partial \eta_ {k}} = 0.
$$

Now addition of these two relations shows that

$$
(m + 1) g ^ {k} = \sum_ {\nu} ^ {1} \eta_ {i} \left(\frac {\partial g ^ {k}}{\partial \eta_ {i}} - \frac {\partial g ^ {i}}{\partial \eta_ {k}}\right),
$$

and therefore

$$
g ^ {i k} = \frac {1}{2 (m + 1)} \left(\frac {\partial g ^ {k}}{\partial \eta_ {i}} - \frac {\partial g ^ {i}}{\partial \eta_ {k}}\right)
$$

has the desired properties when  $\zeta$  and  $\bar{\zeta}$  are introduced as variables again.

From Lemma 2.3 it follows, in particular, that, although the polynomials $G^i(\zeta, \bar{\zeta})$ figuring in Lemma 2.2 are not uniquely determined, the values $G^i(\xi, \xi)$ for real arguments are. This is also easily proved directly. For differentiating (2.4.6) and putting $\eta = 0$ afterwards gives

$$
G ^ {k} (\xi , \xi) = - \frac {1}{2} \frac {\partial F (\xi + i \eta , \xi - i \eta)}{\partial \eta_ {k}} _ {(\eta = 0)}.\tag{2.4.8}
$$

This formula is most important in the application below.

## 2.5. Analytical properties of energy integrals

Let $u$ be a function in $S$ and let $\hat{u}$ be its Fourier transform. Using the definition (2.4.3) and Parseval's formula, we obtain

$$
\int F (D, \bar {D}) u \bar {u} d x = \int F (\xi , \xi) | \hat {u} (\xi) | ^ {2} d \xi .\tag{2.5.1}
$$

As a first application of this formula we prove

LEMMA 2.4. If for every $u \in C_0^\infty(\Omega)$, where $\Omega$ is a fixed domain, we have

$$
\int F (D, \bar {D}) u \bar {u} d x = 0,\tag{2.5.2}
$$

then it follows that

$$
F (\xi , \xi) = 0, f o r r e a l \xi .\tag{2.5.3}
$$

Conversely, (2.5.3) implies (2.5.2) for any $\Omega$.

PROOF. The last statement follows at once from (2.5.1). On the other hand, let (2.5.2) be valid. Let $u \neq 0$ be a fixed function in $C_0^\infty(\Omega)$. For fixed $\eta$, the function $u(x)e^{i\langle x,\eta\rangle}$ is in $C_0^\infty(\Omega)$ and has the Fourier transform $\hat{u}(\xi - \eta)$, so that it follows from (2.5.1) that

$$
\int F (\xi + \eta , \xi + \eta) | \hat {u} (\xi) | ^ {2} d \xi = 0.\tag{2.5.4}
$$

Denote the polynomial $F(\xi, \xi)$ by $\pi(\xi)$, and the principal part of $\pi(\xi)$ by $\pi_m(\xi)$. It follows from (2.5.4), which is valid for every $\eta$, that

$$
\pi_ {m} (\eta) \int | \hat {u} | ^ {2} d \xi = 0
$$

for every $\eta$. Hence $\pi_m$ and consequently $\pi$ is identically zero.

Combining Lemmas 2.4 and 2.2 we obtain the following lemma.

LEMMA 2.5. A quadratic differential form $F(D, \bar{D})$ u $\bar{u}$ is the divergence of a quadratic differential vector form if and only if

$$
\int F (D, \bar {D}) u \bar {u} d x = 0,
$$

when $u \in C_0^\infty(\Omega)$ for some domain $\Omega$.

We could also deduce from Lemma 2.3:

LEMMA 2.6. A quadratic differential vector with the components $G^k(D, \bar{D})$ u $\bar{u}$ is the divergence of a quadratic differential skew symmetric tensor form if and only if for any $u \in C^\infty$ and any closed surface $S$ we have

$$
\int_ {S} \left(G ^ {k} (D, \bar {D}) u \tilde {u}\right) d S _ {k} = 0.
$$

The analogy between these two lemmas and the theory of exterior differential forms is obvious. In order to show this connection we have in fact proved more results on the energy integrals than we really need to prove Theorem 2.2.

## 2.6. Estimates by energy integrals

Let $P(D)$ and $Q(D)$ be two differential operators with constant coefficients and form

$$
F (D, \bar {D}) u \bar {u} = (P (D) Q (\bar {D}) - Q (D) P (\bar {D})) u \bar {u}.\tag{2.6.1}
$$

We have $F(\xi, \xi) = P(\xi)Q(\xi) - Q(\xi)P(\xi) = 0$, so that in virtue of Lemma 2.2 we can write

$$
F (D, \bar {D}) u \bar {u} = \sum_ {k = 1} ^ {\nu} \frac {\partial}{\partial x ^ {k}} (G ^ {k} (D, \bar {D}) u \bar {u}).
$$

Formula (2.4.8) gives that

$$
G ^ {k} (\xi , \xi) = - i (P ^ {(k)} (\xi) Q (\xi) - Q ^ {(k)} (\xi) P (\xi)),\tag{2.6.2}
$$

where, in accordance with our general notations,  $P^{(k)}$  and  $Q^{(k)}$  are the partial derivatives of P and Q with respect to  $\xi_{k}$ .

Let $\Omega$ be a fixed bounded domain, and let $u$ be a function in $C_0^\infty (\Omega)$. We shall integrate the identity

$$
- i x ^ {k} F (D, \bar {D}) u \bar {u} = - i x ^ {k} \sum_ {j} \frac {\partial}{\partial x ^ {j}} (G ^ {j} (D, \bar {D}) u \bar {u})
$$

over $\Omega$. In doing so, we can integrate the right-hand side by parts, so that the integral equals $i\int G^{k}(D,\bar{D})u\bar{u}dx$. Now it follows from (2.6.2) and Lemma 2.4 that

$$
\begin{array}{r l} \int G ^ {k} (D, \bar {D}) u \bar {u} d x & = - i \int (P ^ {(k)} (D) Q (\bar {D}) - P (D) Q ^ {(k)} (\bar {D})) u \bar {u} d x \\ & = - i \bigl \{(P ^ {(k)} (D) u, \bar {Q} (D) u) - (P (D) u, \bar {Q} ^ {(k)} (D) u) \bigr \}, \end{array}
$$

where ( , ) denotes scalar product in  $L^{2}(\Omega)$ . Hence we get the formula

$$
\begin{array}{r l} (P ^ {(k)} (D) u, \bar {Q} (D) u) - (P (D) u, \bar {Q} ^ {(k)} (D) u) & \\ = \int - i x ^ {k} (P (D) u \overline {{\bar {Q} (D) u}} - Q (D) u \overline {{\bar {P} (D) u}}) d x. \end{array}\tag{2.6.3}
$$

By estimating the right-hand side of the equality (2.6.3) we can obtain a useful inequality. In fact, noting that it follows from (2.1.4) that

$$
\left\| P (D) u \right\| = \left\| \overline {{P}} (D) u \right\|, \quad \left\| Q (D) u \right\| = \left\| \bar {Q} (D) u \right\|,
$$

and denoting by $\delta$ an upper bound of $|x^k|$ in $\Omega$, we obtain

$$
\left| \left(P ^ {(k)} (D) u, \bar {Q} (D) u\right) \right| \leq \left\| P (D) u \right\| \left(\left\| \bar {Q} ^ {(k)} (D) u \right\| + 2 \delta \left\| \bar {Q} (D) u \right\|\right)\tag{2.6.4}
$$

by using Schwarz' inequality. When $Q = \overline{P}^{(k)}$ this inequality reduces to

$$
\left\| P ^ {(k)} (D) u \right\| ^ {2} \leq \left\| P (D) u \right\| \left(\left\| P ^ {(k k)} (D) u \right\| + 2 \delta \left\| P ^ {(k)} (D) u \right\|\right),\tag{2.6.5}
$$

where  $P^{(kk)}(\xi)$  is the second derivative of  $P(\xi)$  with respect to  $\xi_{k}$ . The inequality (2.6.5) gives a proof of the following lemma.

LEMMA 2.7. Let $B^k$ be the breadth of $\Omega$ in the direction $x^k$, i.e.

$$
B ^ {k} = \sup _ {x, y \in \Omega} | x ^ {k} - y ^ {k} |.
$$

Then, if $P(\xi)$ is of degree $m$ with respect to $\xi_k$, we have

$$
\left\| P ^ {(k)} (D) u \right\| \leq m B ^ {k} \| P (D) u \|, \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{2.6.6}
$$

PROOF. After a convenient choice of the origin we may suppose that  $|x^{k}| \leq B^{k}/2$  in  $\Omega$ , so that we may put  $2\delta = B^{k}$  in inequality (2.6.5). If m = 1, the second derivative  $P^{(kk)}$  is zero, and (2.6.5) reduces to (2.6.6), if we delete a factor  $\|P^{(k)}(D)u\|$ . Now suppose that the inequality (2.6.6) has already been proved for all polynomials of smaller degree than m in  $\xi_{k}$ . Then we have, in particular,

$$
\left\| P ^ {(k k)} (D) u \right\| \leq (m - 1) B ^ {k} \| P ^ {(k)} (D) u \|.
$$

If we use this estimate in the right-hand side of (2.6.5), it follows that

$$
\left\| P ^ {(k)} (D) u \right\| \leq m B ^ {k} \| P (D) u \|,
$$

which completes the proof.

It follows from the proof that (2.6.6) remains valid for non-bounded domains $\Omega$ if only $B^k < \infty$. We shall later come back to the case of infinite domains (section 2.11), but for the moment we confine ourselves to the simpler case of a bounded domain $\Omega$.

LEMMA 2.8. For any derivative $P^{(\alpha)}$ of $P$ there is a constant $C$ such that

$$
\left\| P ^ {(\alpha)} (D) u \right\| \leq C \left\| P (D) u \right\|, \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{2.6.7}
$$

PROOF. Iteration of the result of Lemma 2.7 proves Lemma 2.8 immediately, and also gives an estimate of the constant C, which we do not care to write out explicitly.

Since a suitable derivative of $P$ is a constant, Lemma 2.8 contains Theorem 2.1, which has thus been proved without the use of the Laplace transform.

We can now complete the proof of Theorem 2.2 and the remark following it. Thus suppose that

$$
\left| Q (\xi) \right| ^ {2} \leq C ^ {2} \sum \left| P ^ {(\alpha)} (\xi) \right| ^ {2}.\tag{2.6.8}
$$

If $\hat{u}$ is the Fourier transform of a function $u\in C_0^\infty (\Omega)$, we have in virtue of (2.1.4) and (2.6.8)

$$
\int | Q (D) u | ^ {2} d x = \int | Q (\xi) | ^ {2} | \hat {u} | ^ {2} d \xi \leq C ^ {2} \sum \int | P ^ {(\alpha)} (\xi) | ^ {2} | \hat {u} | ^ {2} d \xi = C ^ {2} \sum \int | P ^ {(\alpha)} (D) u | ^ {2} d x.
$$

It now follows from (2.6.7) that with a suitable constant $C'$

$$
\left\| Q (D) u \right\| ^ {2} \leq C ^ {\prime} \| P (D) u \| ^ {2}, \quad u \in C _ {0} ^ {\infty} (\Omega),
$$

so that (2.3.1)' is proved.

## 2.7. Some special cases of Theorem 2.2

The problem of finding all differential operators  $Q(D)$ , which are weaker than a given differential operator  $P(D)$ , has been reduced by Theorem 2.2 to the purely algebraic study of inequality (2.3.3). In studying this inequality, it is convenient to say that the polyno-

mial P is stronger than the polynomial Q, if this inequality is valid. We shall first give two explicit examples.

EXAMPLE 1. The Schrödinger equation for a free particle corresponds to the polynomial $P(\xi) = \xi_1^2 + \cdots + \xi_{\nu-1}^2 - \xi_\nu$. This polynomial is stronger than those polynomials $Q(\xi)$ for which

$$
\left| Q (\xi) \right| ^ {2} <   C \left(\left(\xi_ {1} ^ {2} + \dots + \xi_ {\nu - 1} ^ {2} - \xi_ {\nu}\right) ^ {2} + \xi_ {1} ^ {2} + \dots + \xi_ {\nu - 1} ^ {2} + 1\right).\tag{2.7.1}
$$

Evidently (2.7.1) requires that $Q(\xi)$ is of degree two at most and not of higher degree than one in $\xi_v$, so we may write

$$
Q (\xi) = a _ {0} + \sum_ {i = 1} ^ {\nu} a _ {i} \xi_ {i} + \sum_ {i, k = 1} ^ {\nu} a _ {i k} \xi_ {i} \xi_ {k},\tag{2.7.2}
$$

where  $a_{ik}=a_{ki}$  and  $a_{\nu\nu}=0$ . If we set  $\xi_{\nu}=\xi_{1}^{2}+\cdots+\xi_{\nu-1}^{2}$ , it follows from (2.7.1) that (2.7.2) must become a polynomial of degree one at most in the remaining variables  $\xi_{1},\ldots,\xi_{\nu-1}$ . Hence  $Q(\xi)$  must have the form

$$
Q (\xi) = a _ {0} + \sum_ {k = 1} ^ {\nu - 1} a _ {k} \xi_ {k} + a _ {\nu} \left(\xi_ {\nu} - \xi_ {1} ^ {2} - \dots - \xi_ {\nu - 1} ^ {2}\right).\tag{2.7.3}
$$

Conversely, it is obvious that every polynomial of the form (2.7.3) satisfies the inequality (2.7.1).

EXAMPLE 2. The equation of heat corresponds to the polynomial $P(\xi) = \xi_1^2 + \cdots + \xi_{\nu-1}^2 + i\xi_\nu$. This polynomial is stronger than those polynomials $Q(\xi)$ for which

$$
\left| Q (\xi) \right| ^ {2} <   C ((\xi_ {1} ^ {2} + \dots + \xi_ {\nu - 1} ^ {2}) ^ {2} + \xi_ {1} ^ {2} + \dots + \xi_ {\nu - 1} ^ {2} + \xi_ {\nu} ^ {2} + 1).\tag{2.7.4}
$$

This inequality is evidently fulfilled if and only if $Q(\xi)$ has the form

$$
Q (\xi) = a _ {0} + \sum_ {k = 1} ^ {\nu} a _ {k} \xi_ {k} + \sum_ {i, k = 1} ^ {\nu - 1} a _ {i k} \xi_ {i} \xi_ {k}.\tag{2.7.5}
$$

The two examples show clearly that the lower order terms may have a decisive influence on the strength of an operator. $^{1}$  It is this fact that compelled us to develop such a strong generalization of the usual technique of energy integrals, which essentially works with the principal part of the operator, i.e. the homogeneous part of highest degree. The usual technique would, however, be successful within the class of operators satisfying the following definition.

DEFINITION 2.1. The differential operator $P(D)$ (and the polynomial $P(\xi)$) is said to be of principal type, if it is equally strong as any other operator with the same principal part.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  A similar fact has been observed by GARDING [8], who has shown that the correctness of Cauchy's problem can be affected by lower order terms.</span></small>

The definition only involves restrictions on the principal part. This fact is explicitly expressed by the following theorem.

THEOREM 2.3. A necessary and sufficient condition in order that $P(\xi)$ should be of principal type is that the partial derivatives $\partial p(\xi) / \partial \xi_i$ of the principal part $p(\xi)$ do not vanish simultaneously for any real $\xi \neq 0$.

PROOF. Let  $P(\xi)$  be of principal type. Then the same is true of  $p(\xi)$ , so that  $p(\xi)$  is stronger than  $p(\xi) + \xi_{\alpha}$  and consequently stronger than  $\xi_{\alpha}$ , if  $|\alpha| = m - 1$ , where m is the degree of  $p(\xi)$ . Hence it follows from Theorem 2.2 that

$$
\frac {(\xi_ {1} ^ {2} + \cdots + \xi_ {\nu} ^ {2}) ^ {m - 1}}{\sum | p ^ {(\alpha)} (\xi) | ^ {2}} <   C ^ {\prime}.\tag{2.7.6}
$$

Suppose that all the derivatives $\partial p(\eta) / \partial \eta$ vanish for some real $\eta \neq 0$. Then we have also $p(\eta) = 0$ in virtue of Euler's formula for homogeneous polynomials. Hence, if we set $\xi = t\eta$ in (2.7.6), the denominator is of degree less than $2(m - 1)$ in $t$, which gives a contradiction when $t \to \infty$. This proves one half of the theorem.

Now suppose that  $P(\xi)$  satisfies the condition in Theorem 2.3 and let  $Q(\xi)$  have the same principal part as  $P(\xi)$ . Dropping positive terms in the definition of  $\tilde{P}(\xi)^{2}$ , we obtain

$$
\tilde {P} (\xi) ^ {2} > \sum_ {1} ^ {v} \left| \frac {\partial P (\xi)}{\partial \xi_ {k}} \right| ^ {2} = \pi (\xi) + r (\xi),
$$

where $r(\xi)$ is of degree less than $2(m - 1)$ and

$$
\pi (\xi) = \sum_ {1} ^ {\nu} \left| \frac {\partial p (\xi)}{\partial \xi_ {k}} \right| ^ {2}.
$$

In virtue of the assumptions we have  $\pi(\xi)\neq0$ , if  $\xi\neq0$ , and therefore  $r(\xi)/\pi(\xi)\to0$  when  $\xi\to\infty$ , so that  $|r(\xi)|/\pi(\xi)<\frac{3}{4}$  for large  $\xi$ . We note that

$$
\frac {\left| Q (\xi) \right|}{\tilde {P} (\xi)} \leq \frac {\left| Q (\xi) - P (\xi) \right|}{\tilde {P} (\xi)} + \frac {\left| P (\xi) \right|}{\tilde {P} (\xi)}.
$$

Since the last term is always less than 1 and

$$
\varlimsup_ {\xi \rightarrow \infty} \frac {| Q (\xi) - P (\xi) |}{\tilde {P} (\xi)} \leq \varliminf_ {\xi \rightarrow \infty} \frac {2 | Q (\xi) - P (\xi) |}{\sqrt {\pi (\xi)}} <   \infty ,
$$

it follows that  $Q(\xi)$  is weaker than  $P(\xi)$ . Changing P for Q we conclude that P and Q are equally strong.

Our interest in differential operators of principal type is due to the fact that they have simple properties even when the coefficients are variable. We postpone the study of this

case to Chapter IV, and pass to another class of differential operators with constant coefficients. As is well known, a differential operator  $P(D)$  is called elliptic, if the principal part  $p(\xi)$  does not vanish for any real  $\xi \neq 0$ . We give an equivalent property:

THEOREM 2.4. The differential operator $P(D)$ is elliptic if and only if it is stronger than any operator of order not exceeding that of $P$.

This is an almost obvious consequence of Theorem 2.2, so that we may omit the proof. In particular, Theorem 2.4 shows that all elliptic operators of the same order are equally strong.

We shall now study an operator with separable variables,

$$
P (\xi) = P \left(\xi_ {1}, \dots , \xi_ {\nu}\right) = P _ {1} \left(\xi_ {1}, \dots , \xi_ {\mu}\right) P _ {2} \left(\xi_ {\mu + 1}, \dots , \xi_ {\nu}\right) \quad (\mu <   \nu).
$$

The vector  $\xi$  is the sum of the two components

$$
\xi^ {\prime} = (\xi_ {1}, \dots , \xi_ {\mu}, 0, \dots , 0), \xi^ {\prime \prime} = (0, \dots , 0, \xi_ {\mu + 1}, \dots , \xi_ {\nu}).
$$

Let $W'$ be the set of polynomials $Q(\xi')$, which are weaker than $P_1(\xi')$, and let $W''$ be the set of polynomials $Q(\xi'')$ which are weaker than $P_2(\xi'')$.

THEOREM 2.5. The set W of polynomials  $Q(\xi)$  weaker than  $P(\xi)$  is the linear hull of the set  $W'W''$  of products of polynomials in  $W'$  and  $W''$ .

PROOF. Since $\tilde{P} (\xi)^2 = \sum |P^{(\alpha)}(\xi)|^2$ differs from

$$
\tilde {P} _ {1} (\xi^ {\prime}) ^ {2} \tilde {P} _ {2} (\xi^ {\prime \prime}) ^ {2} = \sum \left| P _ {1} ^ {(\beta)} (\xi^ {\prime}) \right| ^ {2} \left| P _ {2} ^ {(\gamma)} (\xi^ {\prime \prime}) \right| ^ {2}
$$

only in the magnitude of the coefficients, we have

$$
0 <   A \leq \frac {\tilde {P} (\xi)}{\tilde {P} _ {1} \left(\xi^ {\prime}\right) \tilde {P} _ {2} \left(\xi^ {\prime \prime}\right)} \leq B <   \infty .
$$

Hence $Q(\xi)$ is weaker than $P(\xi)$ if and only if

$$
\frac {\left| Q \left(\xi^ {\prime} , \xi^ {\prime \prime}\right) \right|}{\tilde {P} _ {1} \left(\xi^ {\prime}\right) \tilde {P} _ {2} \left(\xi^ {\prime \prime}\right)} <   C.\tag{2.7.7}
$$

It now follows that the linear hull of $W'W''$ is in $W$. Inequality (2.7.7) also shows, if $Q \in W$, that $Q(\xi', \xi'')$ is in $W'$ as a function of $\xi'$, for fixed $\xi''$, and in $W''$ as a function of $\xi''$, for fixed $\xi'$. Let $p_1(\xi'), \ldots, p_n(\xi')$ be a basis in the finite dimensional vector space $W'$ and set

$$
Q \left(\xi^ {\prime}, \xi^ {\prime \prime}\right) = \sum_ {k = 1} ^ {n} a _ {k} \left(\xi^ {\prime \prime}\right) p _ {k} \left(\xi^ {\prime}\right).
$$

It remains to prove that the coefficients $a_{k}(\xi^{\prime \prime})$ are in $W^{\prime \prime}$. Since $p_{k}(\xi^{\prime})$ are linearly independent functions, there exist values $\xi_1', \ldots, \xi_n'$ such that the matrix $(p_k(\xi_l'))$ is not singular. Then the system of equations

$$
Q \left(\xi_ {l} ^ {\prime}, \xi^ {\prime \prime}\right) = \sum_ {k = 1} ^ {n} a _ {k} \left(\xi^ {\prime \prime}\right) p _ {k} \left(\xi_ {l} ^ {\prime}\right), l = 1, \dots , n,
$$

can be solved for $a_{k}(\xi^{\prime \prime})$. Hence $a_{k}(\xi^{\prime \prime})$ is a linear combination of the functions $Q(\xi_l', \xi''')$ and consequently is in $W''$.

It is obvious how the theorem can be generalized, if a polynomial decomposes in this way into several factors.

## 2.8. The structure of the minimal domain

The first topic in this section concerns the continuity of the functions in  $D_{P_{0}}$  and their derivatives. From an abstract point of view this was already studied in Chapter I. We shall assume in the whole section that  $\Omega$  is a bounded domain.

THEOREM 2.6. If $Q(D)u$ is a continuous function after correction on a null set, for any $u \in \mathcal{D}_{P_*}$, then

$$
\int \frac {\left| Q (\xi) \right| ^ {2}}{\tilde {P} (\xi) ^ {2}} d \xi <   \infty .\tag{2.8.1}
$$

Conversely, if (2.8.1) is valid, then $Q(D)u$ is uniformly continuous after correction on a null set and tends to zero at the boundary of $\Omega$, for any $u \in \mathcal{D}_{P_0}$, in the sense that to every $\varepsilon > 0$ there exists a compact set $K$ in $\Omega$ such that $|Q(D)u(x)| < \varepsilon$ in $\Omega - K$.

PROOF. First suppose that $Q(D)u$ is always continuous when $u \in \mathcal{D}_{P_0}$. There is then only one obstacle to using Lemma 1.6: although the functions are continuous they need not a priori be bounded. Therefore we take a function $\psi(x) \in C_0^\infty(\Omega)$ and apply Lemma 1.6 to the differential operators $P(D)$ and

$$
Q = \psi (x) Q (D).
$$

It follows that there is a constant $C$ such that

$$
\sup _ {x \in \Omega} | \psi (x) Q (D) u (x) | ^ {2} \leq C (\| P (D) u \| ^ {2} + \| u \| ^ {2}), \quad u \in C _ {0} ^ {\infty} (\Omega).
$$

We may suppose without restriction that $0 \in \Omega$ and that $\psi(0) = 1$. Then it follows that

$$
\left| Q (D) u (0) \right| ^ {2} \leq C (\left\| P (D) u \right\| ^ {2} + \| u \| ^ {2}), \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{2.8.2}
$$

Now take a function $\varphi (\xi)\in S$ and form

$$
v (x) = (2 \pi) ^ {- \nu / 2} \int \frac {\varphi (\xi)}{\tilde {P} (\xi)} e ^ {i \langle x, \xi \rangle} d \xi .
$$

Parseval's formula gives

$$
\left\| P ^ {(\alpha)} (D) v \right\| ^ {2} = \int \frac {\left| \varphi (\xi) \right| ^ {2}}{\tilde {P} (\xi) ^ {2}} \left| P ^ {(\alpha)} (\xi) \right| ^ {2} d \xi \leq \int \left| \varphi (\xi) \right| ^ {2} d \xi .\tag{2.8.3}
$$

Furthermore, $v$ is also in $S$. Now take a fixed function $\chi(x) \in C_{\theta}^{\infty}(\Omega)$, which equals 1 in a neighbourhood of the origin, and set

$$
u (x) = \chi (x) v (x).
$$

We then have $u \in C_0^\infty(\Omega)$ and, in virtue of Leibniz' formula and (2.8.3),

$$
\left\| P (D) u \right\| \leq C \| \varphi \|.\tag{2.8.4}
$$

Noting that $Q(D)u(0) = Q(D)v(0)$, we deduce from (2.8.2) and (2.8.4) that

$$
\left| (2 \pi) ^ {- \nu / 2} \int \frac {Q (\xi)}{\tilde {P} (\xi)} \varphi (\xi) d \xi \right| ^ {2} \leq C ^ {\prime 2} \int | \varphi (\xi) | ^ {2} d \xi .
$$

But this inequality implies that $Q(\xi) / \tilde{P}(\xi)$ is square integrable, which proves (2.8.1).

Now assume that (2.8.1) is valid. Estimating by Schwarz' inequality we get for $u \in C_0^\infty(\Omega)$

$$
\begin{array}{l} \left| Q (D) u (x) \right| ^ {2} = \left| (2 \pi) ^ {- \nu / 2} \int Q (\xi) \hat {u} (\xi) e ^ {i \langle x, \xi \rangle} d \xi \right| ^ {2} \\ \leq (2 \pi) ^ {- \nu} \int \frac {\left| Q (\xi) \right| ^ {2}}{\tilde {P} (\xi) ^ {2}} d \xi \int \tilde {P} (\xi) ^ {2} | \hat {u} (\xi) | ^ {2} d \xi = C ^ {2} \sum \| P ^ {(\alpha)} (D) u \| ^ {2}. \end{array}
$$

Lemma 2.8 now shows that

$$
\left| Q (D) u (x) \right| ^ {2} \leq C ^ {\prime 2} \| P (D) u \| ^ {2}, \quad u \in C _ {0} ^ {\infty} (\Omega),\tag{2.8.5}
$$

for any $x$. Hence the second half of the theorem follows from Lemma 1.6.

The formulations of Theorems 2.2 and 2.6 are closely related. This leads us to the following theorem.

THEOREM 2.7. $Q(D)u$ is a function in $L^p$ ($2 \leq p \leq \infty$) for every $u \in \mathcal{D}_{P_0}$, if $Q(\xi)/\tilde{P}(\xi) \in L^{2p/(p-2)}$ in $R_\nu$.

PROOF. In virtue of the theorem of Titchmarsh and M. Riesz on Fourier transforms of functions in  $L^{p}$  (cf. Zygmund [35], p. 316), we have for  $u \in C_{0}^{\infty}(\Omega)$

$$
\left\| Q (D) u \right\| _ {p} \leq C \left\| Q (\xi) \hat {u} (\xi) \right\| _ {p ^ {\prime}},
$$

where  $p'$  is defined by  $p^{-1} + p'^{-1} = 1$ . We may suppose that  $2 < p < \infty$ , since the extreme cases have already been treated. Then we have  $p' < 2$ , and Hölder's inequality proves that

$$
\int | Q (\xi) \hat {u} (\xi) | ^ {p ^ {\prime}} d \xi \leq \left(\int | \tilde {P} (\xi) \hat {u} (\xi) | ^ {2} d \xi\right) ^ {p ^ {\prime} / 2} \left(\int \left| \frac {Q (\xi)}{\tilde {P} (\xi)} \right| ^ {2 p ^ {\prime} / (2 - p ^ {\prime})} d \xi\right) ^ {1 - \frac {p ^ {\prime}}{2}}.
$$

Since $2p' / (2 - p') = 2p / (p - 2)$, we obtain, if $u \in C_0^\infty(\Omega)$,

$$
\left\| Q (D) u \right\| _ {p} \leq C ^ {\prime} \left\| \tilde {P} (\xi) \hat {u} (\xi) \right\| \leq C ^ {\prime \prime} \left\| P (D) u \right\|,\tag{2.8.6}
$$

where the last estimate follows from the proof of Theorem 2.6. It is clear that (2.8.6) gives the asserted result.

The theorem cannot be reversed since Sobolev's results (cf. [30], p. 64) are stronger for elliptic operators. We give two examples of non-elliptic operators.

EXAMPLE 1. If $P(\xi) = \xi_1^2 + \cdots + \xi_{\nu-1}^2 - \xi_\nu$, we have $1 / \tilde{P}(\xi) \in L^q$ if and only if $q > \nu$. In particular, when $\nu = 2$, it follows that the functions in $\mathcal{D}_{P_*}$ are in $L^q$ for every $q < \infty$ but are not all continuous.

EXAMPLE 2. If $P(\xi) = \xi_1^2 + \cdots + \xi_{\nu - 1}^2 + i\xi_\nu$, we have $1 / \tilde{P}(\xi) \in L^q$ if and only if $q > \frac{1}{2} (\nu + 1)$. In particular, every function in the domain of $P_0$ is continuous when $\nu = 2$.

In the proof of Theorem 2.6 we found that $Q(D)u$ is continuous for any $u \in \mathcal{D}_{P_{\bullet}}$ if and only if (2.8.2) is fulfilled, i.e., if the value of $Q(D)u$ at a fixed point is a continuous function of $[u, P(D)u] \in G_{P_{\bullet}}$ ($u \in C_0^\infty(\Omega)$). When we now pass to studying $Q(D)u$ on varieties of dimensions between 1 and $\nu - 1$, we examine a condition similar to (2.8.2) from the outset. Thus let $\Sigma$ be a variety in $\Omega$ and let $d\sigma$ be the element of area of $\Sigma$. If the inequality

$$
\int_ {\Sigma} \left| Q (D) u \right| ^ {2} d \sigma \leq C (\left\| P (D) u \right\| ^ {2} + \left\| u \right\| ^ {2}), \quad u \in C _ {0} ^ {\infty} (\Omega),\tag{2.8.7}
$$

holds good, the restriction of $Q(D)u$ to $\Sigma$ may be defined when $u \in \mathcal{D}_P$, in the usual way: We take a sequence $u_n \in C_0^\infty$ such that $u_n \to u$ and $P(D)u_n \to P_0u$. In virtue of (2.8.7) the sequence $Q(D)u_n$ is convergent in $L^2(\Sigma)$. The limit in $L^2(\Sigma)$, which does not depend on the sequence $u_n$, which we have have chosen, is the desired restriction of $Q(D)u$ to $\Sigma$. Somewhat roughly we may say that $Q(D)u$ exists in $\Sigma$ for $u \in \mathcal{D}_{P_*}$, when the inequality (2.8.7) is valid.

Our methods only permit us to study the case when $\Sigma$ is a linear variety of dimension $\mu$, $1 \leq \mu \leq \nu - 1$. We may of course assume that $\Sigma$ has points in common with $\Omega$. By $\Sigma'$ we denote any one of the varieties in $R_{\nu}$, orthogonal to $\Sigma$. The surface element in $\Sigma'$ is denoted $d\sigma'$.

THEOREM 2.8. A necessary and sufficient condition in order that $Q(D)u$ should exist in $\Sigma$ for $u \in \mathcal{D}_{P_0}$ is that $Q(\xi) / \tilde{P}(\xi)$ is uniformly square integrable in the varieties $\Sigma'$, i.e.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R_{\nu}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  For simplicity in statements we may suppose that  $R^{\nu}$  and  $R_{\nu}$  have (dual) euclidean geometries. Then surface elements and norms of vectors are defined.</span></small>

$$
\int_ {\Sigma^ {\prime}} \frac {| Q (\xi) | ^ {2}}{\tilde {P} (\xi) ^ {2}} d \sigma^ {\prime} <   C,\tag{2.8.8}
$$

where the constant does not depend on the choice of the variety $\Sigma'$, orthogonal to $\Sigma$.

The statement is still true, if $\Sigma$ has dimension 0 or $\nu$. It then reduces to Theorem 2.6 and Theorem 2.2, respectively.

PROOF. Passing, if necessary, to another system of coordinates, we may assume that  $\Sigma$  is defined by the equations

$$
x ^ {u + 1} = 0, \dots , x ^ {\nu} = 0.
$$

First suppose that (2.8.7) is valid. In virtue of Theorem 2.1 we then also have (with a different constant $C$)

$$
\int_ {\Sigma} | Q (D) u | ^ {2} d x ^ {1} \dots d x ^ {\mu} \leq C \int_ {\Omega} | P (D) u | ^ {2} d x ^ {1} \dots d x ^ {\nu} \quad (u \in C _ {0} ^ {\infty} (\Omega)).\tag{2.8.9}
$$

By using a combination of the arguments in the proofs of Theorems 2.2 and 2.6, we shall prove that (2.8.8) follows.

Take a function $\varphi(\xi)$ in $S$ and set for fixed $\xi_1, \ldots, \xi_\mu$

$$
v (x) = \int \frac {\varphi (\xi)}{\tilde {P} (\xi)} e ^ {i \langle x, \xi \rangle} d \sigma^ {\prime} = e ^ {i (x ^ {1} \xi_ {1} + \dots + x ^ {\mu} \xi_ {\mu})} \int \frac {\varphi (\xi)}{\tilde {P} (\xi)} e ^ {i (x ^ {\mu + 1} \xi_ {\mu + 1} + \dots + x ^ {\nu} \xi_ {\nu})} d \sigma^ {\prime},\tag{2.8.10}
$$

where  $d\sigma' = d\xi_{\mu+1} \cdots d\xi_{\nu}$ . Thus  $v(x)$  is a function with spectrum in a variety  $\Sigma'$ , orthogonal to  $\Sigma$ .

Differentiation under the integral sign gives

$$
P ^ {(\alpha)} (D) v (x) = \int \frac {\varphi (\xi) P ^ {(\alpha)} (\xi)}{\tilde {P} (\xi)} e ^ {i \langle x, \xi \rangle} d \sigma^ {\prime},
$$

and since $\left|P^{(\alpha)}(\xi)\right| \leq \tilde{P}(\xi)$, it follows from Parseval's formula that

$$
\int \left| P ^ {(\alpha)} (D) v (x) \right| ^ {2} d x ^ {\mu + 1} \dots d x ^ {\nu} \leq (2 \pi) ^ {\nu - \mu} \int \left| \varphi (\xi) \right| ^ {2} d \sigma^ {\prime}.\tag{2.8.11}
$$

Let $\psi$ be a function in $C_0^\infty (\Omega)$ and set

$$
u (x) = v (x) \psi (x).\tag{2.8.12}
$$

It is clear that $u \in C_0^\infty(\Omega)$, and by virtue of (2.8.11) and Leibniz' formula we have

$$
\int | P (D) u | ^ {2} d x \leq C \int | \varphi (\xi) | ^ {2} d \sigma^ {\prime}.\tag{2.8.13}
$$

(Thus far, the argument is parallel to the proof of Theorem 2.6.)

In the plane $\Sigma$ we have

$$
Q ^ {(\alpha)} (D) v \left(x ^ {1}, \dots , x ^ {\mu}, 0, \dots , 0\right) = e ^ {i \left(x ^ {1} \xi_ {1} + \dots + x ^ {\mu} \xi_ {\mu}\right)} \int \frac {Q ^ {(\alpha)} (\xi)}{\tilde {P} (\xi)} \varphi (\xi) d \sigma^ {\prime}.\tag{2.8.14}
$$

Assuming, as we may, that the function $\psi \in C_0^\infty(\Omega)$ does not vanish identically in $\Sigma$ and that $\psi$ is a function of $x^1, \ldots, x^\mu$ only in a neighbourhood of $\Sigma$, we can argue as in section 2.3. For Leibniz' formula shows that, when $x \in \Sigma$,

$$
Q (D) u (x) = \sum^ {*} \frac {D _ {\alpha} \psi}{| \alpha | !} Q ^ {(\alpha)} (D) v (x),
$$

where $\Sigma^{*}$ means a sum only over sequences of the indices 1, ..., $\mu$. Setting

$$
t _ {\alpha} = \int \frac {Q ^ {(\alpha)} (\xi)}{\tilde {P} (\xi)} \varphi (\xi) d \sigma^ {\prime},\tag{2.8.15}
$$

we deduce from (2.8.14) that

$$
\int_ {\Sigma} \left| Q (D) u (x) \right| ^ {2} d x ^ {1} \dots d x ^ {\mu} = \sum_ {\alpha} ^ {*} \sum_ {\beta} ^ {*} \psi_ {\alpha \beta} t _ {\alpha} \tilde {t} _ {\beta},\tag{2.8.16}
$$

where

$$
\psi_ {\alpha \beta} = \frac {1}{| \alpha | ! | \beta | !} \int_ {\Sigma} D _ {\alpha} \psi \overline {{{{D _ {\beta} \psi}}}} d x ^ {1} \dots d x ^ {\mu}.
$$

Now we proved in section 2.3 that the quadratic form $\sum^{*}\psi_{\alpha\beta}t_{\alpha}\bar{t}_{\beta}$ is a positive definite form in the array $t=(t_{\alpha})$, where $\alpha$ only contains the indices 1, ..., $\mu$. In particular,

$$
\left| t _ {0} \right| ^ {2} \leq C \sum_ {\alpha} ^ {*} \sum_ {\beta} ^ {*} \psi_ {\alpha \beta} t _ {\alpha} \bar {t} _ {\beta},
$$

and this inequality combined with (2.8.16), (2.8.9), (2.8.13) and the definition (2.8.15) of $t$ gives that

$$
\left| \int \frac {Q (\xi)}{\tilde {P} (\xi)} \varphi (\xi) d \sigma^ {\prime} \right| ^ {2} \leq C \int | \varphi (\xi) | ^ {2} d \sigma^ {\prime}\tag{2.8.17}
$$

for any choice of the function $\varphi(\xi) \in \mathcal{S}$ and for any $\xi_1, \ldots, \xi_\mu$. (We denote by $C$ different constants, different times.) Hence (2.8.8) follows.

Now suppose that (2.8.8) is fulfilled. For $u \in C_0^\infty(\Omega)$ we have

$$
Q (D) u \left(x ^ {1}, \dots , x ^ {\mu}, 0, \dots , 0\right) = (2 \pi) ^ {- v / 2} \int Q (\xi) \hat {u} (\xi) e ^ {i \left(x ^ {1} \xi_ {1} + \dots + x ^ {\mu} \xi_ {\mu}\right)} d \xi ,
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13-553810. Acta Mathematica. 94. Imprimé le 27 septembre 1955.</span></small>

so that the Fourier transform of the function $Q(D)u(x^1,\dots,x^\mu,0,\dots,0)$ as a function of $x^1,\dots,x^\mu$ is

$$
(2 \pi) ^ {- (\nu - \mu) / 2} \int Q (\xi) \hat {u} (\xi) d \xi_ {\mu + 1} \dots d \xi_ {\nu}.
$$

Schwarz' inequality and (2.8.8) show that the square of this function of $\xi_{1},\ldots ,\xi_{\mu}$ is less than

$$
\begin{array}{r l} (2 \pi) ^ {- (\nu - \mu)} \int \frac {| Q (\xi) | ^ {2}}{\tilde {P} (\xi) ^ {2}} d \sigma^ {\prime} \int \tilde {P} (\xi) ^ {2} | \hat {u} (\xi) | ^ {2} d \xi_ {\mu + 1} \dots d \xi_ {\nu} \\ & \leq C \int \tilde {P} (\xi) ^ {2} | \hat {u} (\xi) | ^ {2} d \xi_ {\mu + 1} \dots d \xi_ {\nu}. \end{array}
$$

It now follows from Parseval's formula that

$$
\int_ {\Sigma} | Q (D) u | ^ {2} d \sigma \leq C \int d \xi_ {1} \dots d \xi_ {\mu} \int \tilde {P} (\xi) ^ {2} | \hat {u} (\xi) | ^ {2} d \xi_ {\mu + 1} \dots d \xi_ {\nu} = C \int \tilde {P} (\xi) ^ {2} | \hat {u} (\xi) | ^ {2} d \xi ,
$$

and using Lemma 2.8 as in the proof of Theorem 2.6 we obtain

$$
\int_ {\Sigma} \left| Q (D) u \right| ^ {2} d \sigma \leq C \int \left| P (D) u \right| ^ {2} d x, \quad u \in C _ {0} ^ {\infty} (\Omega),
$$

which completes the proof.

The special case of Theorem 2.8, where $\Sigma$ is a hyperplane, is most important. In that case $Q(D)u$ exists in $\Sigma$ for every $u\in\mathcal{D}_{P_{0}}$ if and only if

$$
\int_ {- \infty} ^ {+ \infty} \frac {\left| Q (\xi + t N) \right| ^ {2}}{\tilde {P} (\xi + t N) ^ {2}} d t \leq C\tag{2.8.18}
$$

for every real $\xi$, where $\mathbf{N}$ is the normal of $\Sigma$.

LEMMA 2.9. If $p(t)$ is a polynomial of degree $n$ in a real variable $t$, we have

$$
\int_ {- \infty} ^ {+ \infty} \frac {\left| p ^ {\prime} (t) \right| ^ {2}}{\left| p (t) \right| ^ {2} + \left| p ^ {\prime} (t) \right| ^ {2}} d t \leq 4 n ^ {2}.\tag{2.8.19}
$$

Proof. Logarithmic differentiation gives that

$$
\frac {p ^ {\prime} (t)}{p (t)} = \sum_ {1} ^ {n} \frac {1}{t - t _ {k}},
$$

where $t_k$ are the zeros of $p(t)$. The integral (2.8.19) can be divided into two parts $I_1$ and $I_2$, where $I_1$ is the integral over the intervals where $|\operatorname{Re}(t - t_k)| \leq 1$ for some $k$, and $I_2$ is the

integral over the rest of the real axis. Since the integrand is  $\leq1$  everywhere, and the total length of the intervals, over which the integral  $I_{1}$  is extended, is at most 2n, we have  $I_{1}\leq2n$ . In the integral  $I_{2}$  we have the estimate

$$
\frac {\left| p ^ {\prime} (t) \right| ^ {2}}{\left| p (t) \right| ^ {2} + \left| p ^ {\prime} (t) \right| ^ {2}} \leq \left| \frac {p ^ {\prime} (t)}{p (t)} \right| ^ {2} \leq n \sum_ {k = 1} ^ {n} \frac {1}{\left| t - t _ {k} \right| ^ {2}}
$$

in virtue of Cauchy's inequality. Since $|t - t_k|^2 \geq |t - \operatorname{Re} t_k|^2$, this gives

$$
I _ {2} \leq n ^ {2} \int_ {| t | \geq 1} \frac {d t}{t ^ {2}} = 2 n ^ {2},
$$

so that $I_{1} + I_{2}\leq 4n^{2}$

Using this lemma and Theorem 2.8 in the form (2.8.18) we obtain

THEOREM 2.9. If $\Sigma$ is a hyperplane with normal $\mathbf{N}$, we have $\int |P_{\mathbf{N}}^{(\alpha)}(D)u|^2 d\sigma \leq C\int |P(D)u|^2 dx$, $u \in C_0^\infty(\Omega)$, where $P_{\mathbf{N}}^{(\alpha)}(\xi) = \sum N_k \partial P^{(\alpha)}(\xi)/\partial \xi_k$. Thus the restrictions to $\Sigma$ of all $P_{\mathbf{N}}^{(\alpha)}(D)u$ can be defined when $u \in \mathcal{D}_{P_0}$.

In the case where  $P(\xi) = (\xi, \xi)$  is a regular quadratic form, the covariant vector N has contravariant components also, and  $P_{\mathrm{N}}(D)$  is the operator of differentiating along the contravariant normal. For operators of higher order than two, the operator  $P_{N}$  appears to be an appropriate substitute for the normal derivative.

An element u in  $D_{P_{0}}$  is, strictly speaking, an equivalence class of square integrable functions, and by the function  $u(x)$  we have always meant any representative of this equivalence class. Thus  $u(x)$  has only been defined for almost all x. It is then obvious that the function  $u(x)$ ,  $x \in \Sigma$ , does not in general define the restriction of u to  $\Sigma$ , if the restriction exists in the above sense.

A representative $u(x)$ of an element $u$ in $\mathcal{D}_{P_0}$ will be called distinguished, if the restriction of $u$ to any variety $\Sigma$ is defined by the function $u(x), x \in \Sigma$, whenever it exists in the above sense. We shall prove that every element $u$ in $\mathcal{D}_{P_0}$ has a distinguished representative. In fact, we can find a sequence of functions $u_n \in C_0^\infty(\Omega)$ such that

$$
\left\| u _ {n} - u \right\|\rightarrow 0, \quad \left\| P (D) u _ {n} - P _ {0} u \right\|\rightarrow 0,
$$

and

$$
\sum 2 ^ {n} \left\| u _ {n} - u _ {n + 1} \right\| <   \infty , \quad \sum 2 ^ {n} \left\| P (D) u _ {n} - P (D) u _ {n + 1} \right\| <   \infty .
$$

If the restriction of $u$ to $\Sigma$ exists, the inequality (2.8.7) is valid with $Q = 1$, and it follows that

$$
\sum 2 ^ {n} \left\| u _ {n} - u _ {n + 1} \right\| _ {\Sigma} <   \infty .
$$

Denoting the open set in $\Sigma$ where $|u_n(x) - u_{n+1}(x)| > 2^{-n}$ by $e_n$, we have the estimate $2^{-n}\sigma(e_n)\leq \|u_n - u_{n+1}\|_\Sigma$, where $\sigma(e_n)$ is the Lebesgue measure in $\Sigma$ of $e_n$. Writing $\omega_{n} = \bigcup_{k > n}e_{k}$, we obtain

$$
\sigma \left(\omega_ {n}\right) \leqslant \sum_ {n} ^ {\infty} \sigma \left(e _ {k}\right) \leqslant \sum_ {n} ^ {\infty} 2 ^ {k} \left| \left| u _ {k} - u _ {k + 1} \right| \right| _ {\Sigma},
$$

which tends to 0 with $n^{-1}$. Hence the set $\omega = \cap \omega_n$ has measure zero in $\Sigma$, and $\lim u_n(x)$ obviously exists if $x \in \Sigma - \omega$. Now set $u(x) = \lim u_n(x)$ for any $x \in \Omega$ such that the limit exists, and define $u(x)$ arbitrarily elsewhere. We have proved that the limit exists almost everywhere in any variety $\Sigma$ such that (2.8.7) is valid. Hence it follows that the strong limit of $u_n$ in $L^2(\Sigma)$, which by definition is the restriction of $u$ to $\Sigma$, is defined by the function $u(x)$, $x \in \Sigma$.

The same arguments apply to the definition of  $Q_{0}u$  when  $u \in D_{P_{0}}$  and  $Q(D)$  is weaker than  $P(D)$ . Thus the equivalence class  $Q_{0}u$  always contains a distinguished function  $Q_{0}u(x)$ ; the restriction of  $Q_{0}u$  to a variety  $\Sigma$  is then defined by the function  $Q_{0}u(x)$ ,  $x \in \Sigma$ , whenever it exists. Note that, in particular, the distinguished function  $Q_{0}u(x)$  is continuous, if (2.8.1) is valid.

More precise results have been obtained by Deny and Lions [4] for the Beppo Levi functions. The results proved here could probably be improved in the same direction by means of a generalized notion of capacity, but the results already proved are sufficient for us.

We now prove a result which in particular contains a localization principle for $\mathcal{D}_{P_0}$.

THEOREM 2.10. The product of a function $u \in \mathcal{D}_{P_0}$ and a function $\psi \in C^\infty(\overline{\Omega})^1$ is in $\mathcal{D}_{P_0}$, and there is a constant $C$ depending on $\psi$ such that

$$
\left\| P _ {0} (\psi u) \right\| \leq C \left\| P _ {0} u \right\|, \quad u \in \mathcal {D} _ {P _ {0}}.\tag{2.8.20}
$$

Proof. Using Leibniz' formula and Lemma 2.8 we obtain the inequality (2.8.20) if $u \in C_0^\infty(\Omega)$. This evidently gives the desired result.

Theorem 2.10 may seem evident at first sight, but to display its significance we give two examples showing that, if a function u is in  $D_{P}$ , where P is the maximal operator defined by  $P(D)$ , and  $\psi \in C_{0}^{\infty}(\overline{\Omega})$ , it need not be true that  $\psi u \in D_{P}$ , even for the simplest operators.

EXAMPLE 1. Let $P(D)$ be the Laplace operator in two variables, and let $u(x^1, x^2)$ be a harmonic function in the circle $r = (x^{1^2} + x^{2^2})^{\frac{1}{2}} < 1$ such that $u \in L^2$ but $\partial u / \partial r \notin L^2$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ψ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  This means that  $\psi$  is  $C^{\infty}$  in a neighbourhood of  $\overline{\Omega}$ .</span></small>

A well-known example of a function with these properties is due to Hadamard. Now let  $\psi$  be a function in  $C^{\infty}$  such that  $\psi = r$  outside a neighbourhood of the origin. We have

$$
\Delta (\psi u) = u \Delta \psi + 2 (\operatorname{grad} u, \operatorname{grad} \psi).
$$

The first term is square integrable but the second is not, since it equals $2\partial u / \partial r$ outside a neighbourhood of the origin. Hence $u \in \mathcal{D}_P$ but $\psi u \notin \mathcal{D}_P$.

EXAMPLE 2. Let $P(D)$ be the wave operator $\partial^2 / \partial x^1 \partial x^2$ in two variables, and let $u = u(x^1)$ be an absolutely continuous function of $x^1$, whose derivative is not square integrable in the neighbourhood of any point. Since we have

$$
P (D) (\psi u) = \frac {\partial u}{\partial x ^ {1}} \frac {\partial \psi}{\partial x ^ {2}} + u \frac {\partial^ {2} \psi}{\partial x ^ {1} \partial x ^ {2}},
$$

it follows that $\psi u \notin \mathcal{D}_P$ unless $\psi$ is a function of $x^1$, although we have $u \in \mathcal{D}_P$. In particular, $\psi u \notin \mathcal{D}_P$, if $0 \neq \psi \in C_0^\infty(\Omega)$.

After these two examples we leave the maximal operators, which will be discussed in the next chapter. However, to clarify the contents of Theorem 2.10, we shall also prove that Lemma 2.8, which was the essential tool in the proof of Theorem 2.2, is a consequence of Theorem 2.10. In fact, if we take $\psi(x) = e^{i\langle x,\eta\rangle}$, Theorem 2.10 shows that the polynomial $P(\xi)$ is stronger than the polynomial $P(\xi + \eta)$. Hence $P(\xi)$ is also stronger than any linear combination of the translated polynomials $P(\xi + \eta)$, with fixed $\eta$, and our assertion follows from the following lemma.

LEMMA 2.10. A linear set I of polynomials is invariant for differentiation if and only if it is invariant for translation.

PROOF. That invariance for differentiation implies invariance for translation follows at once from Taylor's formula. On the other hand, if I is invariant for translation and  $P \in I$  is of degree  $\mu$ , the set I contains all functions of the form

$$
\sum_ {i = 1} ^ {m} t _ {i} P (\xi + \eta^ {i}) = \sum_ {| \alpha | \leq \mu} P ^ {(\alpha)} (\xi) \frac {1}{| \alpha | !} \sum_ {i = 1} ^ {m} t _ {i} \eta_ {\alpha} ^ {i},
$$

where  $\eta^{i}$  are arbitrary vectors, and  $t_{i}$  are arbitrary complex numbers. Now the coefficients  $\sum_{i=1}^{m} t_{i} \eta_{\alpha}^{i}, |\alpha| \leq \mu$ , can be given arbitrary values, which are symmetric in  $\alpha$ , by a convenient choice of m,  $t_{i}$  and  $\eta^{i}$ . For otherwise there would exist constants  $c_{\alpha}, |\alpha| \leq \mu$ , symmetric in  $\alpha$  and not all equal to zero, such that

$$
\sum_ {| \alpha | \leq \mu} c _ {\alpha}   \eta_ {\alpha} = 0    \text { for   every }   \eta .
$$

But this is impossible. Hence I contains all  $P^{(\alpha)}(\xi)$ , which was to be proved.

THEOREM 2.11. The conditions for a function $u$ to be in $\mathcal{D}_{P_0}$ have a local character in $\overline{\Omega}$. More precisely, if $u$ is a function such that to every point in $\overline{\Omega}$ there exists a neighbourhood $U$, and a function $v_U \in \mathcal{D}_{P_0}$, so that $u(x) = v_U(x)$ a.e. in $U \cap \Omega$, then $u \in \mathcal{D}_{P_0}$.

PROOF. We can cover $\bar{\Omega}$ by a finite number of neighbourhoods $U_{i}, i = 1, \ldots, m$, of the type given by the theorem. Now take functions $\alpha_{i}(x) \in C_{0}^{\infty}(U_{i})$ such that

$$
\sum_ {1} ^ {m} \alpha_ {i} (x) = 1, \quad x \in \overline {{{{\Omega}}}}.
$$

Since $u(x) = \sum u(x)\alpha_i(x)$, and $u(x)\alpha_i(x) = v_{U_i}(x)\alpha_i(x)$ is in $\mathcal{D}_{P_0}$ in virtue of Theorem 2.10, it follows that $u$ is in $\mathcal{D}_{P_0}$.

The properties of the functions in  $D_{P_{0}}$  in the neighbourhood of a point in  $\Omega$  are described by the following theorem.

THEOREM 2.12. A function $u$ in $L^2(\Omega)$ is equal to a function in $\mathcal{D}_{P_0}$ in a neighbourhood of a point $x \in \Omega$ if and only if all $P^{(\alpha)}(D)u$ are square integrable functions in a neighbourhood of $x$.

PROOF. First suppose that u equals a function v in  $D_{P_{0}}$  in a neighbourhood of the point x. Then we have in this neighbourhood

$$
P ^ {(\alpha)} (D) u = P ^ {(\alpha)} (D) v
$$

and, since  $P^{(\alpha)}(D)v$  is square integrable over  $\Omega$  in virtue of Theorem 2.2, the assertion of the theorem follows.

Conversely, suppose that $P^{(\alpha)}(D)u$ is square integrable for every $\alpha$ in a neighbourhood $U$ of $x$. Let $\psi \in C_0^\infty(U)$ equal 1 in a neighbourhood $V$ of $x$. Then $v(x) = u(x)\psi(x)$ equals $u(x)$ in $V$, and in virtue of Leibniz' formula we have in the weak sense

$$
P (D) v = \sum \frac {D _ {\alpha} \psi}{| \alpha | !} P ^ {(\alpha)} (D) u \in L ^ {2}.
$$

Hence the proof reduces to the proof of the following lemma, already referred to in Chapter I.

LEMMA 2.11. A function $u \in \mathcal{D}_P$, which has compact support in $\Omega$, is in $\mathcal{D}_{P_0}$.

PROOF. Let $\psi \in C_0^\infty (R^\nu)$ and $\int \psi (x)dx = 1$. We form the convolutions $u_{\varepsilon} = u*\psi_{\varepsilon}$, where $\psi_{\varepsilon}(x) = \varepsilon^{-\nu}\psi (x / \varepsilon)$. When $\varepsilon$ is sufficiently small, we have $u_{\varepsilon} \in C_0^\infty (\Omega)$, and it is well known that $u_{\varepsilon} \to u$ in $L^2$. Furthermore, when $\varepsilon \to 0$, we have

$$
P (D) u _ {\varepsilon} = (P (D) u) * \psi_ {\varepsilon} \rightarrow P (D) u
$$

in $L^2$. Hence by definition $u \in \mathcal{D}_{P_0}$.

We shall now deduce a corresponding result for a point x on the boundary. In doing so we restrict ourselves to a point on a plane portion of the boundary, where we can use our

Theorem 2.9. It would no doubt be possible to treat a much more general case by generalizing that theorem, but we shall refrain from studying that question here.

Let $\Sigma$ be a plane surface with compact closure in $\Omega$. It follows from Theorem 2.12 and Theorem 2.9 that $P_{N}^{(\alpha)}(D)u$ exists in $\Sigma$ and is square integrable there, if $u$ is such that $P^{(\alpha)}(D)u$ is square integrable in a neighbourhood of $\Sigma$ for every $\alpha$. We can now announce our result.

THEOREM 2.13. Let $x_0$ be a point on a plane portion $\Sigma$ of the boundary of $\Omega$, the distance from $x_0$ to the rest of the boundary being positive. Then a function $u$ in $L^2(\Omega)$ equals a function in $\mathcal{D}_{P_0}$ in a neighbourhood of $x_0$ if and only if all $P^{(\alpha)}(D)u$ are square integrable functions in a neighbourhood of $x_0$ in $\overline{\Omega}$, and the restrictions of $P_{\mathrm{N}}^{(\alpha)}(D)u$ to parallel surfaces to $\Sigma$ tend to zero strongly in a neighbourhood of $x_0$ when the surfaces approach $\Sigma$.

The last statement needs perhaps some explanation. Let $y$ be a fixed transversal direction to $\Sigma$, i.e. $\langle y, \mathbf{N} \rangle \neq 0$. We may suppose that $y$ points from $\Sigma$ to $\Omega$. If $x$ is in a suitable neighbourhood $U$ of $x_0$ in $\Sigma$ and $\delta$ is a sufficiently small positive number, the function $P_{\mathbf{N}}^{(\alpha)}(D)u(x + \delta y)$ is square integrable in $U$. The second half of the condition in the theorem is that this function tends strongly to zero in $L^2(U)$ when $\delta \to 0$. — Note that Sobolev [30] has given similar results in connection with elliptic operators.

PROOF OF THE THEOREM. First, let $v$ be a function in $\mathcal{D}_{P_0}$. For given $\varepsilon$ we can find a function $v_{\varepsilon} \in C_0^\infty(\Omega)$ such that $\| P(D)(v - v_{\varepsilon}) \| < \varepsilon$. In virtue of Theorem 2.9 there is a constant $C$ such that on all planes $\Sigma_1$ with normal $N$ we have

$$
\left\| P _ {N} ^ {(\alpha)} (D) (v - v _ {\varepsilon}) \right\| _ {\Sigma_ {1}} <   C \varepsilon
$$

for every $\varepsilon$. Since $v_{\varepsilon}$ vanishes in a neighbourhood of the boundary, we have with the notation introduced above

$$
\left\| P _ {N} ^ {(\alpha)} (D) v (x + \delta y) \right\| _ {U} <   C \varepsilon ,
$$

if $\delta$ is small enough. This proves the necessity of the conditions given in the theorem.

Conversely, let the conditions of the theorem be fulfilled. Since they are still valid for the function $u\varphi$, where $\varphi \in C^{\infty}$ and vanishes outside a neighbourhood of $x$, we may suppose that $u$ vanishes outside the neighbourhoods mentioned in the theorem. Let $\psi \in C_0^\infty$ with respect to the half space $\langle x, \mathbf{N} \rangle \langle y, \mathbf{N} \rangle > 0$, where $y$ is the vector mentioned above, and $\int \psi dx = 1$. It is then easily proved that the convolution $u_{\varepsilon} = u * \psi_{\varepsilon}$, where $\psi_{\varepsilon}(x) = \varepsilon^{-\nu} \psi(x / \varepsilon)$, is in $C_0^\infty(\Omega)$ for small $\varepsilon$ and that $u_{\varepsilon} \to u$ and $P(D)u_{\varepsilon} = P(D)u * \psi_{\varepsilon} \to P(D)u$ when $\varepsilon \to 0$. This completes the proof. The details may be left to the reader.

In particular we may note that a function u which is sufficiently differentiable in  $\Omega$  equals a function in  $D_{P_{0}}$  in a neighbourhood of a point on a plane portion of the boundary

of $\overline{\Omega}$ if and only if it vanishes there together with $m - 1$ transversal derivatives, where $m$ is the degree of $P(\xi + t\mathbf{N})$ in $t$ when $\xi$ is an indeterminate.

One of the most important results in the theory of partial differential operators is the lemma of H. Weyl to the effect that any solution of the equation Pu = 0, where P is a maximal elliptic operator, must be infinitely differentiable (after correction on a null set). This is only true for a certain class of differential operators P, which will be determined in the next chapter. For that class it will turn out that, more generally, any function, which is in the domain of  $P^{n}$  for any n, is infinitely differentiable. This result has an analogue for general minimal differential operators, which we shall now discuss. We start with two definitions and a lemma, showing how the strength of the powers of an operator increases.

DEFINITION 2.2. The linear manifold

$$
\Lambda (P) = \{\eta ; \eta \text {   is   real   and   } P (\xi + t \eta) = P (\xi) \text {   for   any   } \xi \text {   and   } t \}\tag{2.8.21}
$$

is called the lineality space of the polynomial $P$.

DEFINITION 2.3. A polynomial $P$ is called complete, if the lineality space consists of the origin only.

Thus P is complete, if it really depends on all variables. The two definitions are essentially borrowed from Gårding [8].

LEMMA 2.12. The operator $P(D)^n$ is stronger than any product $Q_1(D) \ldots Q_k(D), k \leq n$, of operators which are weaker than $P$.

Proof. First note that for $0 \leq k \leq n$ we have

$$
\left\| P (D) ^ {k} u \right\| ^ {2} \leq \frac {k}{n} \left\| P (D) ^ {n} u \right\| ^ {2} + \left(1 - \frac {k}{n}\right) \| u \| ^ {2}, \quad u \in C _ {0} ^ {\infty} (\Omega).
$$

In fact, this inequality is equivalent to

$$
\int | P (\xi) | ^ {2 k} | \hat {u} (\xi) | ^ {2} d \xi \leq \frac {k}{n} \int | P (\xi) | ^ {2 n} | \hat {u} (\xi) | ^ {2} d \xi + \left(1 - \frac {k}{n}\right) \int | \hat {u} (\xi) | ^ {2} d \xi ,
$$

which follows from the inequality between geometric and arithmetic means. Hence to prove the lemma it is sufficient to show that for any k

$$
\left\| Q _ {1} (D) \dots Q _ {k} (D) u \right\| ^ {2} \leq C \left(\left\| P (D) ^ {k} u \right\| ^ {2} + \dots + \left\| u \right\| ^ {2}\right), \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{2.8.22}
$$

For $k = 1$, this is only the definition of a weaker operator. Assuming as we may that (2.8.22) has already been proved when $k$ is replaced by $k - 1$, we find by substituting $P(D)u$ for $u$ that

$$
\left\| Q _ {1} (D) \dots Q _ {k - 1} (D) P (D) u \right\| ^ {2} \leq C (\left\| P (D) ^ {k} u \right\| ^ {2} + \dots + \left\| P (D) u \right\| ^ {2}), \quad u \in C _ {0} ^ {\infty} (\Omega).
$$

Using the fact that the operators all commute, and having recourse to the definition of a weaker operator again, we obtain (2.8.22).

THEOREM 2.14. A function u which is in the minimal domain of  $P(D)^{n}$  for every n, where P is a complete polynomial, is infinitely differentiable in  $\Omega$ , and every derivative tends to zero at the boundary.

PROOF. Let R be the algebra generated by the polynomials which are weaker than P. It follows from Lemma 2.12 that the function u of the theorem is in the minimal domain of  $Q(D)$ , if  $Q \in R$ . Now the assumption that P is complete implies that the algebra R is the whole polynomial ring. We shall prove this assertion in section 2.10. Since to any polynomial Q we can find another  $Q_{1}$  such that  $|Q(\xi)|/\tilde{Q}_{1}(\xi)$  is square integrable, it follows from Theorem 2.6 that  $Q(D)u$  is continuous after correction on a null set and tends to zero at the boundary of  $\Omega$ . It now easily follows (see also Schwartz [28], Tome I, p. 62) that u is infinitely differentiable in the classical sense.

REMARK. We can also prove that  $u \in C^{\infty}$ , if we suppose that u is in the domain of  $P_{0}^{n}$  for every n. For if  $\Omega'$  is a bounded domain which contains  $\bar{\Omega}$ , and we extend u to a function  $u'$  in  $\Omega'$  by setting  $u' = u$  in  $\Omega$  and  $u' = 0$  elsewhere, the assumptions of Theorem 2.14 are satisfied by  $u'$  in  $L^{2}(\Omega')$ . (After the above was written, the question whether the domain of  $P_{0}^{n}$  always coincides with the minimal domain of  $P(D)^{n}$  was answered in the negative by J. L. Lions.)

## 2.9. Some theorems on complete continuity

Theorem 2.2 gave the necessary and sufficient conditions for the continuity of the mapping

$$
\mathcal {R} _ {P _ {0}} \ni P _ {0} u \rightarrow Q _ {0} u \in \mathcal {R} _ {Q _ {0}}.\tag{2.9.1}
$$

We shall now derive the conditions for complete continuity. Such results are important in proving that vibration problems have a discrete spectrum. We remark that some results, similar to the theorems which we are going to prove, have been given previously by Kondrachov (see Sobolev [30]) with different proofs, based on potential theory.

THEOREM 2.15. The mapping (2.9.1) is completely continuous if and only if

$$
\frac {\tilde {Q} (\xi)}{\tilde {P} (\xi)} \rightarrow 0 \text {   when   } \xi \rightarrow \infty .\tag{2.9.2}
$$

PROOF. We first prove that the complete continuity of the mapping (2.9.1) follows from (2.9.2). The proof is a combination of Theorem 2.2 with the proof by Gårding ([9], p. 59) of a special case.

Suppose that (2.9.2) is fulfilled. Then we have also $|Q(\xi)| / \tilde{P}(\xi) < C$. Take any sequence $u_{n} \in C_0^{\infty}(\Omega)$ such that

$$
\left\| P (D) u _ {n} \right\| \leq 1.\tag{2.9.3}
$$

We shall prove that  $Q(D)u_{n'}$  converges if  $n'$  is a suitable subsequence of the sequence n. In virtue of Theorem 2.2 we have

$$
\left\| Q (D) u _ {n} \right\| \leq C.\tag{2.9.4}
$$

Since all  $Q(D)u_{n}$  vanish outside the bounded set  $\Omega$ , it follows from (2.9.4), if we denote the Fourier transform of  $u_{n}$  by  $\hat{u}_{n}$ , that the functions  $Q(\xi)\hat{u}_{n}(\xi)$  are uniformly bounded and uniformly continuous. Hence we can find a subsequence  $n'$  such that  $Q(\xi)\hat{u}_{n'}(\xi)$  is uniformly convergent on every compact set. Now we have

$$
\left\| Q (D) u _ {n ^ {\prime}} - Q (D) u _ {m ^ {\prime}} \right\| ^ {2} = \int | Q (\xi) \hat {u} _ {n ^ {\prime}} (\xi) - Q (\xi) \hat {u} _ {m ^ {\prime}} (\xi) | ^ {2} d \xi .
$$

Let $K$ be a compact set such that $|Q(\xi)| / \tilde{P}(\xi) < \varepsilon$ in the complement $K'$ of $K$. Then it follows from (2.9.3) and Lemma 2.8 (see proof at the end of section 2.6) that

$$
\int_ {K ^ {\prime}} \left| Q (\xi) \right| ^ {2} \left| \hat {u} _ {n ^ {\prime}} (\xi) - \hat {u} _ {m ^ {\prime}} (\xi) \right| ^ {2} d \xi \leq \varepsilon^ {2} \int \tilde {P} (\xi) ^ {2} \left| \hat {u} _ {n ^ {\prime}} (\xi) - \hat {u} _ {m ^ {\prime}} (\xi) \right| ^ {2} d \xi \leq A \varepsilon^ {2},
$$

where $A$ is a constant. Furthermore,

$$
\int_ {K} \left| Q (\xi) \hat {u} _ {n ^ {\prime}} (\xi) - Q (\xi) \hat {u} _ {m ^ {\prime}} (\xi) \right| ^ {2} d \xi \rightarrow 0, \text {   when   } n ^ {\prime} \text {   and   } m ^ {\prime} \rightarrow \infty ,
$$

in virtue of the uniform convergence. Hence

$$
\varlimsup_ {n ^ {\prime}, m ^ {\prime} \rightarrow \infty} \| Q (D) u _ {n ^ {\prime}} - Q (D) u _ {m ^ {\prime}} \| ^ {2} \leq A \varepsilon^ {2}
$$

for every $\varepsilon$, which proves that $Q(D)u_n$ is convergent. This proves the complete continuity of the mapping (2.9.1), since the functions $P(D)u$, $u \in C_0^\infty(\Omega)$, are dense in $\mathcal{R}_{P_n}$.

Now suppose that the mapping (2.9.1) is completely continuous. We have to prove that (2.9.2) must be valid. This can be achieved by modifying the technique of section 2.3. It is obviously sufficient to prove that, if $\xi_{n}$ is a sequence tending to infinity, such that $\tilde{Q} (\xi_n) / \tilde{P} (\xi_n)$ tends to a limit, then the limit must be zero. Since we may, if necessary, pass to a subsequence, it is also permitted to suppose that

$$
\xi_ {n} - \xi_ {m} \rightarrow \infty \text {   when   } n, m \rightarrow \infty \text {   and   } n \neq m.\tag{2.9.5}
$$

This assumption is essential in the proof.

Let $\psi$ be a fixed function in $C_0^\infty (\Omega)$, and form the sequence of functions

$$
u _ {n} (x) = \psi (x) \frac {e ^ {i \langle x , \xi_ {n} \rangle}}{\tilde {P} (\xi_ {n})}.\tag{2.9.6}
$$

In virtue of Leibniz' formula there is a constant $C$ such that

$$
\left\| P (D) u _ {n} \right\| \leq C.\tag{2.9.7}
$$

Using (2.3.5), we can write

$$
\left\| Q (D) u _ {n} - Q (D) u _ {m} \right\| ^ {2} = \left\| Q (D) u _ {n} \right\| ^ {2} + \left\| Q (D) u _ {m} \right\| ^ {2} - \delta_ {n m},\tag{2.9.8}
$$

where

$$
\delta_ {n m} = 2 \operatorname{Re} \left\{\sum_ {\alpha , \beta} \frac {Q ^ {(\alpha)} (\xi_ {n})}{\tilde {P} (\xi_ {n})} \overline {{\frac {Q ^ {(\beta)} (\xi_ {m})}{\tilde {P} (\xi_ {m})}}} \frac {1}{| \alpha | ! | \beta | !} \int D _ {\alpha} \psi \overline {{D _ {\beta} \psi}} e ^ {i \langle x, \xi_ {n} - \xi_ {m} \rangle} d x \right\}.\tag{2.9.9}
$$

Now, since the mapping (2.9.1) is completely continuous, it is also continuous, so that $Q^{(\alpha)}(\xi) / \tilde{P} (\xi)$ is bounded in virtue of Theorem 2.2. Hence it follows from (2.9.5) and Riemann-Lebesgue's lemma in its very simplest form that $\delta_{nm}\to 0$ when $n,m\to \infty$ and $n\neq m$.

By the assumption, there is a sequence $n'$ such that $Q(D)u_n$ is convergent. Then it follows from (2.9.8) that

$$
\left\| Q (D) u _ {n ^ {\prime}} \right\| ^ {2} = \sum_ {\alpha , \beta} \frac {Q ^ {(\alpha)} (\xi_ {n ^ {\prime}}) \overline {{Q ^ {(\beta)} (\xi_ {n ^ {\prime}})}}}{\tilde {P} (\xi_ {n ^ {\prime}}) ^ {2}} \psi_ {\alpha \beta} \rightarrow 0 \quad \text { when } n ^ {\prime} \rightarrow \infty ,\tag{2.9.10}
$$

where $\psi_{\alpha \beta}$ is defined by (2.3.6). It now follows from (2.3.9) that also

$$
\sum_ {\alpha} \frac {\left| Q ^ {(\alpha)} \left(\xi_ {n ^ {\prime}}\right)\right| ^ {2}}{\tilde {P} \left(\xi_ {n ^ {\prime}}\right) ^ {2}} = \frac {\tilde {Q} \left(\xi_ {n ^ {\prime}}\right) ^ {2}}{\tilde {P} \left(\xi_ {n ^ {\prime}}\right) ^ {2}} \rightarrow 0 \quad \text { when } n ^ {\prime} \rightarrow \infty .
$$

The proof is complete.

THEOREM 2.16. Let $\Sigma$ be a plane of dimension less than $v$. Then the mapping

$$
\mathcal {R} _ {P _ {0}} \ni P (D) u \rightarrow \{Q (D) u \} _ {\Sigma} \in L ^ {2} (\Sigma),\tag{2.9.11}
$$

where $\{Q(D)u\}_{\Sigma}$ is the restriction of $Q(D)u$ to $\Sigma$, is completely continuous if and only if

$$
\int_ {\Sigma^ {\prime}} \frac {| Q (\xi) | ^ {2}}{\tilde {P} (\xi) ^ {2}} d \sigma^ {\prime} \rightarrow 0\tag{2.9.12}
$$

when the normal variety $\Sigma' \to \infty$.

The reader will have no difficulty in carrying out the proof, which does not require any ideas beyond the proofs of Theorem 2.8 and Theorem 2.15.

THEOREM 2.17. The inverse $P_0^{-1}$ of a minimal differential operator is completely continuous if and only if $P$ is a complete polynomial.

PROOF. If $P$ is not a complete polynomial, there exists a real vector $\eta \neq 0$ such that $P(\xi + t\eta) \equiv P(\xi)$. Differentiating repeatedly with respect to $\xi$, we obtain that $\tilde{P}(\xi + t\eta) =$

$= \tilde{P}(\xi)$, so that $\tilde{P}(\xi + t\eta)$ is bounded when $t \to \infty$. Hence Theorem 2.15 with $Q(\xi) \equiv 1$ shows that $P_0^{-1}$ is not completely continuous.

Now suppose that $P$ is a complete polynomial, i.e. that $\Lambda(P) = \{0\}$, where $\Lambda(P)$ is defined by (2.8.21). We shall prove that $\tilde{P}(\xi) \to \infty$ with $\xi$ or, equivalently, that

$$
M _ {C} = \{\xi ; \tilde {P} (\xi) \leq C \}
$$

is a bounded set for every $C$. The polynomial $P(\xi)$ can be written as the sum of its homogeneous parts,

$$
P (\xi) = \sum_ {0} ^ {m} P _ {k} (\xi),
$$

where $P_{k}(\xi)$ is homogeneous of degree $k$ and $P_{m}(\xi) \not\equiv 0$. It is easy to prove that, for every polynomial $P$,

$$
\Lambda (P) = \bigcap_ {k = 1} ^ {m} \Lambda (P _ {k}).\tag{2.9.13}
$$

For, if $\eta \in \bigcap_{k=1}^{m} \Lambda(P_k)$, we have $P_k(\xi + t\eta) \equiv P_k(\xi)$ and consequently $P(\xi + t\eta) \equiv P(\xi)$, so that $\eta \in \Lambda(P)$. Hence $\bigcap_{k=1}^{m} \Lambda(P_k) \subset \Lambda(P)$. Now let $\eta \in \Lambda(P)$. Then we have

$$
\sum_ {0} ^ {m} P _ {k} (\xi + t \eta) \equiv \sum_ {0} ^ {m} P _ {k} (\xi).
$$

Replacing $\xi$ by $\tau\xi$ and $t$ by $\tau t$ and identifying the powers of $\tau$, we obtain $P_{k}(\xi + t\eta) \equiv \equiv P_{k}(\xi)$, so that $\eta \in \Lambda(P_{k})$. Hence $\Lambda(P) \subset \bigcap_{k=1}^{m} \Lambda(P_{k})$, which proves (2.9.13).

From our assumption that $P$ is complete, it thus follows that $\bigcap_{k=1}^{m} \Lambda(P_k) = \{0\}$. Hence it will follow that the set $M_C$ is bounded, if we only prove that $M_C$ is bounded modulo $\Lambda(P_k)$ for every $k$. We need a simple lemma on homogeneous polynomials in the proof.

LEMMA 2.13. Let $Q$ be a homogeneous polynomial of degree $m$. Then a real vector $\eta$, such that $D_{\alpha}Q(\eta) = 0$ for every $\alpha$ of length $m - 1$, is in $\Lambda(Q)$.

PROOF. The lemma is obvious, if m = 1, and we shall prove it in general by induction over m. Suppose that the assumptions of the lemma are satisfied and m > 1. Then the assumptions hold good also for the polynomials  $\partial Q/\partial\xi_{i}$ . Assuming, as we may, that the lemma is already proved for polynomials of degree less than m, we obtain

$$
\partial Q (\xi + t \eta) / \partial \xi_ {i} \equiv \partial Q (\xi) / \partial \xi_ {i}.
$$

Hence $Q(\xi + t\eta) - Q(\xi)$ is independent of $\xi$, so that we have

$$
Q (\xi + t \eta) - Q (\xi) \equiv Q (t \eta).
$$

Setting $t = 1$ and $\xi = \eta$ we obtain $2Q(\eta) = 2^{m}Q(\eta)$. Hence $Q(\eta) = 0$ and thus $Q(\xi + t\eta) = Q(\xi)$, which means that $\eta \in \Lambda(Q)$.

We can now prove that $M_C$ is bounded modulo $\Lambda(P_k)$ for every $k$, if $P$ is any polynomial. Since this is obvious if the degree $m$ of $P$ is 1, it is sufficient to prove that it is true for $P$, if it is true for all polynomials of degree less than $m$.

That $\tilde{P}(\xi) \leq C$ in $M_c$, implies that $|P^{(\alpha)}(\xi)| \leq C$ there. In particular, this is true when $|\alpha| = m - 1$, and then $P^{(\alpha)}(\xi)$ differs from $P_m^{(\alpha)}(\xi)$ only by a constant term. Hence we have $|P_m^{(\alpha)}(\xi)| < C'$ in $M_c$ if $|\alpha| = m - 1$. In virtue of Lemma 2.13, the linear forms $P_m^{(\alpha)}(\xi)$ vanish simultaneously only in $\Lambda(P_m)$. Hence $M_c$ is bounded modulo $\Lambda(P_m)$. But since $P_m^{(\alpha)}(\xi)$ is constant modulo $\Lambda(P_m)$ for every $\alpha$, we conclude that $\tilde{P}_m(\xi)$ is bounded in $M_c$. Now form the polynomial

$$
R (\xi) = P (\xi) - P _ {m} (\xi) = P _ {m - 1} (\xi) + \dots + P _ {0}.
$$

$R(\xi)$ is of degree $m - 1$, and since

$$
\tilde {R} (\xi) \leq \tilde {P} (\xi) + \tilde {P} _ {m} (\xi),
$$

we have $\tilde{R}(\xi) < C''$ in $M_C$. Using the assumption that our assertion is proved for polynomials of degree less than $m$, it follows that $M_C$ is bounded modulo $\Lambda(P_k)$, $k \leq m - 1$. This completes the proof of Theorem 2.17.

The proof also shows that, if P is complete, there exists a constant c > 0 such that  $\tilde{P}(\xi) > (\xi_{1}^{2} + \cdots + \xi_{\nu}^{2})^{c}$ . Hence  $1/\tilde{P}(\xi)$  is in  $L^{q}$  for large q, which permits the use of Theorem 2.7. A fairly precise result is given by the following lemma, which includes Theorem 2.17 but has a much more difficult proof.

LEMMA 2.14. If $P^1(\xi), \ldots, P^n(\xi)$ is a set of polynomials such that

$$
\bigcap_ {k = 1} ^ {n} \Lambda (P ^ {k}) = \{0 \},
$$

then  $(\tilde{P}^{1^{2}} + \cdots + \tilde{P}^{n^{2}})^{-\frac{1}{2}}$  is in  $L^{q}$  if q > v.

Note that Example 1 on page 191 shows that the constant v of the lemma cannot be replaced by any smaller one. We also remark, that we shall only use Lemma 2.14 when n = 1, but the more general statement is necessary for our proof. Using this special case of Lemma 2.14 and Theorem 2.7, we obtain

THEOREM 2.18. We have $u \in L^q$, if $u$ is in the minimal domain of a complete differential operator and $q < 2\nu / (\nu - 2)$, if $\nu > 2$, $q < \infty$. if $\nu = 2$.

As a preparation for the proof of Lemma 2.14 we introduce a new notation, which supplements the definition of $\Lambda(P)$,

$$
\underline {{{{\Lambda}}}} (P) = \bigcap_ {k = 2} ^ {m} \Lambda (P _ {k}) = \Lambda (P - P _ {1}).\tag{2.9.14}
$$

The last equality follows from (2.9.13). We shall prove that

$$
\underline {{\Lambda}} (P) = \bigcap_ {i = 1} ^ {\nu} \Lambda (\partial P / \partial \xi_ {i}).\tag{2.9.15}
$$

First suppose that $P$ is homogeneous of degree $m > 1$. Since it is obvious that $\Lambda(\partial P / \partial \xi_i) \supset \Lambda(P)$, we obtain by using Lemma 2.13

$$
\Lambda (P) \subset \bigcap_ {i = 1} ^ {\nu} \Lambda (\partial P / \partial \xi_ {i}) \subset \bigcap_ {| \alpha | = m - 1} \Lambda (D _ {\alpha} P) \subset \Lambda (\mathrm{P}).
$$

Hence (2.9.15) is valid in this case. Using this result and (2.9.13), we obtain for a general $P = \Sigma P_k$

$$
\bigcap_ {i = 1} ^ {v} \Lambda (\partial P / \partial \xi_ {i}) = \bigcap_ {i = 1} ^ {v} \bigcap_ {k = 1} ^ {m} \Lambda (\partial P _ {k} / \partial \xi_ {i}) = \bigcap_ {k = 1} ^ {m} \bigcap_ {i = 1} ^ {v} \Lambda (\partial P _ {k} / \partial \xi_ {i}) = \bigcap_ {k = 2} ^ {m} \Lambda (P _ {k}) = \underline {{\Lambda}} (P),
$$

since all $\partial P_1 / \partial \xi_i$ are constants. This proves (2.9.15).

Before the proof we also extend our terminology slightly. We shall say that a system  $P^{1}, \ldots, P^{n}$  of polynomials is complete, if  $\bigcap_{i=1}^{n} \Lambda(P^{i}) = \{0\}$ . The system  $Q^{1}, \ldots, Q^{l}$  will be said to be weaker than the system  $P^{1}, \ldots, P^{n}$ , if we have

$$
\tilde {P} ^ {1 ^ {2}} + \dots + \tilde {P} ^ {n ^ {2}} \geq \tilde {Q} ^ {1 ^ {2}} + \dots + \tilde {Q} ^ {l ^ {2}}.
$$

PROOF OF LEMMA 2.14. By repeated application of the following two operations, we shall construct a system, which is weaker than the given one and for which the assertion of the lemma is valid:

A) If $\bigcap_{k\neq l}\Lambda (P_k) = \{0\}$, we obtain a weaker complete system by omitting $P_{l}$.

B) If $\underline{\Lambda}(P_l) \cap (\bigcap_{k \neq l} \Lambda(P_k)) = \{0\}$, we obtain a weaker complete system, if we replace $P_l$ by all the polynomials $\partial P_l / \partial \xi_i$ ($i = 1, \ldots, \nu$). This follows from formula (2.9.15).

To the system of polynomials, given in the formulation of Lemma 2.14, we first apply operation A until this is no longer possible. Then we apply operation B—if possible—to one of the remaining polynomials of highest degree, and then apply the operation A again as many times as it is possible. The new system is still complete, and either the highest degree occurring among the polynomials in the system, or else the number of polynomials of highest degree, has diminished. Hence we must after a finite number of steps come to a system  $Q^{1},\ldots,Q^{l}$ , which is complete and weaker than the original system, such that A

cannot be applied any more and B is not applicable to some of the polynomials—in fact to none of those of highest degree. Let one of these be  $Q^{1}$ . Then we have

$$
\Lambda = \underline {{\Lambda}} (Q ^ {1}) \cap \Lambda (Q ^ {2}) \cap \dots \cap \Lambda (Q ^ {l}) \neq \{0 \},\tag{2.9.16}
$$

whereas

$$
\Lambda \cap \Lambda (Q _ {1} ^ {1}) = \{0 \},\tag{2.9.17}
$$

where  $Q^{1}_{1}$  is the linear part of  $Q^{1}$ . Since  $\Lambda(Q^{1}_{1})$  cannot have a co-dimension greater than one, it follows from (2.9.16) and (2.9.17) that  $\Lambda$  is one-dimensional. Let us suppose that the coordinates are chosen such that  $\Lambda$  is the  $\xi_{1}$ -axis. In virtue of (2.9.16), the polynomials  $Q^{1}-Q^{1}_{1}, Q^{2},\ldots,Q^{l}$  are then independent of  $\xi_{1}$ , that is, they are polynomials in  $\xi_{2},\ldots,\xi_{r}$ . It follows from (2.9.17) that  $Q^{1}_{1}$  is not independent of  $\xi_{1}$ , so we can set

$$
Q ^ {1} (\xi) = c \xi_ {1} + R (\xi),
$$

where $c \neq 0$ and $R$ is independent of $\xi_1$. Now we can write

$$
\tilde {Q} ^ {2} = \tilde {Q} ^ {1 ^ {2}} + \dots + \tilde {Q} ^ {l ^ {2}} = | c \xi_ {1} + R | ^ {2} + \sum_ {i = 1} ^ {\nu} (\partial \widetilde {Q ^ {1} / \partial \xi_ {i}}) ^ {2} + \tilde {Q} ^ {2 ^ {2}} + \dots + \tilde {Q} ^ {l ^ {2}} = | c \xi_ {1} + R | ^ {2} + \tilde {Q} ^ {\prime^ {2}}.
$$

This gives, if we perform the integration over  $\xi_{1}$  explicitly,

$$
\int \frac {1}{\tilde {Q} ^ {q}} d \xi_ {1} \dots d \xi_ {\nu} \leq \frac {1}{| c |} \int_ {- \infty} ^ {+ \infty} \frac {d \tau}{(\tau^ {2} + 1) ^ {q / 2}} \int \frac {1}{\tilde {Q} ^ {\prime (q - 1)}} d \xi_ {2} \dots d \xi_ {\nu}.
$$

Since $q > \nu \geq 1$, the first integral is convergent. Furthermore, since it follows from (2.9.16) that the polynomials $\partial Q^1 / \partial \xi_1, \ldots, \partial Q^1 / \partial \xi_\nu, Q^2, \ldots, Q^l$ form a complete system in the variables $\xi_2, \ldots, \xi_\nu$, the convergence of the last integral follows from the validity of Lemma 2.14 in a space of dimension $\nu - 1$. Hence the lemma is true for any number of variables, since it is true when $\nu = 1$.

## 2.10. On some sets of polynomials

Let $P$ be a fixed polynomial. We have studied the set of polynomials $Q$ such that $Q(D)u$ exists for $u \in \mathcal{D}_{P_{\bullet}}$ in one sense or another (Theorems 2.2, 2.6, 2.7, 2.8, 2.15, 2.16). In all cases, the set $I$ of polynomials $Q$, which we have obtained, has the following two properties:

a) $I$ is linear and invariant for translation.

b) If $Q$ is a polynomial such that

$$
\left| Q (\xi) \right| \leq \sum_ {i = 1} ^ {n} \left| Q _ {i} (\xi) \right|
$$

for every real $\xi$, where $Q_{1}(\xi),\ldots ,Q_{n}(\xi)\in I$, then it follows that $Q(\xi)\in I$.

In virtue of Lemma 2.10, the property (a) is equivalent to

a') I is linear and invariant for differentiation.

That (b) is fulfilled is evident in all the cases, so that the only thing we need to prove is the invariance for translation. Let us verify this for the set of polynomials $Q$ such that $Q(\xi) / \tilde{P}(\xi)$ is in $L^q$. Let $Q(\xi) / \tilde{P}(\xi) \in L^q$. Then, for fixed $\eta$, the function

$$
\frac {Q (\xi + \eta)}{\tilde {P} (\xi)} = \frac {Q (\xi + \eta)}{\tilde {P} (\xi + \eta)} \frac {\tilde {P} (\xi + \eta)}{\tilde {P} (\xi)}
$$

is also in $L^q$, for it follows at once from Taylor's formula that $\tilde{P}(\xi + \eta) / \tilde{P}(\xi)$ is bounded for fixed $\eta$.

We also remark, without performing the comparatively easy proof, that, if $Q(\xi) / \tilde{P}(\xi)$ is in $L^q$, it follows that $Q(\xi) / \tilde{P}(\xi) \to 0$ when $\xi \to \infty$, and hence that $Q(\xi) / \tilde{P}(\xi)$ is in $L^r$ for $r \geq q$. This can partly be deduced also from our theorems above.

The invariance for translation and differentiation proves the fact, already noticed in a remark following Theorem 2.2, that, for instance, the assumption that  $Q(\xi)/\tilde{P}(\xi)\to0$  is equivalent to  $\tilde{Q}(\xi)/\tilde{P}(\xi)\to0$  when  $\xi\to\infty$ . The same remark applies to the other theorems.

We now prove a result which was already used in section 2.8.

LEMMA 2.15. The algebra R, generated by the polynomials weaker than a polynomial P, consists of all polynomials with the lineality manifold  $\Lambda(P)$ .

PROOF. The statement is obvious, if P is of degree 1. To prove it for a polynomial  $P = \sum_{k=0}^{m} P_k$ , we may assume that it has already been proved for polynomials of degree less than m. Now the polynomials which are weaker than  $\partial P/\partial \xi_i$  are also weaker than P, and hence R contains all polynomials with the lineality manifold  $\Lambda(\partial P/\partial \xi_i)$ . Thus R contains all polynomials with the lineality manifold

$$
\bigcap_ {i = 1} ^ {v} \Lambda (\partial P / \partial \xi_ {i}) = \underline {{\Lambda}} (P) = \Lambda (P - P _ {1}).
$$

Since $R$ contains $P$ and $P - P_{1}$, the polynomial $P_{1}$ is also in $R$, which proves that $R$ also contains all polynomials with the lineality manifold $\Lambda(P_{1})$. This completes the proof.

## 2.11. Remarks on the case of non-bounded domains

We shall here study the minimal operator  $P_{0}$ , defined by a differential operator  $P(D)$ , when  $\Omega$  is not bounded, a case which has been excluded in all the previous theorems of this chapter. It seems difficult to give a perfect generalization of Theorem 2.2, but we can prove two theorems which replace Theorem 2.2 in some important cases.

THEOREM 2.19. Let $\Omega$ be a domain, which contains the direct sum of an open set $\Omega'$ in the plane $x^{\mu + 1} = \dots = x^{\nu} = 0$ ($\mu < \nu$) and the space $G = \{(0, \ldots, 0, x^{\mu + 1}, \ldots, x^{\nu})\}$. Then, if

$$
\left\| Q (D) u \right\| ^ {2} \leq C (\left\| P (D) u \right\| ^ {2} + \| u \| ^ {2}), \quad u \in C _ {0} ^ {\infty} (\Omega),\tag{2.11.1}
$$

it follows that

$$
\left| Q (\xi) \right| ^ {2} <   C ^ {\prime} \left(\sum_ {\alpha} ^ {*} \right\rvert P ^ {(\alpha)} (\xi) \left| ^ {2} + 1\right),\tag{2.11.2}
$$

where $\Sigma^{*}$ means a sum only over sequences of the indices $1,\ldots ,\mu$

PROOF. Let $\psi$ be a function in $C_0^\infty (\Omega' \times G)$ and consequently in $C_0^\infty (\Omega)$. Then the formula (2.3.7) must be valid. Now replace $\psi$ by $\psi^e$,

$$
\psi^ {\varepsilon} \left(x ^ {1}, \dots , x ^ {\nu}\right) = \varepsilon^ {(\nu - \mu) / 2} \psi \left(x ^ {1}, \dots , x ^ {\mu}, \varepsilon x ^ {\mu + 1}, \dots , \varepsilon x ^ {\nu}\right).
$$

An easy calculation shows that  $\psi^{\varepsilon}_{\alpha\beta} = \varepsilon^{k}\psi_{\alpha\beta}$ , where k is the total number of indices occurring in  $\alpha$  and  $\beta$ , which are not between 1 and  $\mu$ . Hence in the limit when  $\varepsilon \to 0$ , it follows from (2.3.7) that

$$
\sum_ {\alpha , \beta} ^ {*} Q ^ {(\alpha)} (\xi) \overline {{Q ^ {(\beta)} (\xi)}} \psi_ {\alpha \beta} \leq C \left(\sum_ {\alpha , \beta} ^ {*} P ^ {(\alpha)} (\xi) \overline {{P ^ {(\beta)} (\xi)}} \psi_ {\alpha \beta} + \psi_ {\mathbf {0 0}}\right).\tag{2.11.3}
$$

Now our result follows at once from (2.3.9).

REMARK. It is easy to see that the same result remains valid, if we replace G by an open set in G, which contains arbitrarily large spheres.

The same argument also gives that, if $\Omega$ satisfies the assumptions of Theorem 2.19 and the operator $P_0$ has a continuous inverse, we must have

$$
1 \leq C ^ {\prime} \sum_ {\alpha} ^ {*} | P ^ {(\alpha)} (\xi) | ^ {2}.\tag{2.11.4}
$$

THEOREM 2.20. If $x^1, \ldots, x^\mu$ are bounded in $\Omega$, it follows from (2.11.2) that (2.11.1) is valid. It also follows from (2.11.4) that the inverse of $P_0$ is continuous.

PROOF. It was remarked on page 185 that Lemma 2.7 is also true for infinite domains. This gives at once a proof of Theorem 2.20, if we repeat the arguments at the end of the proof of Theorem 2.2.

If $\Omega$ satisfies both the condition of Theorem 2.19 and that of Theorem 2.20, we may of course conclude that (2.11.2) is a necessary and sufficient condition for the validity of (2.11.1), and that (2.11.4) is a necessary and sufficient condition for the continuity of the inverse of $P_0$. The result concerning the continuity of $P_0^{-1}$ could partly be obtained from the proof of Theorem 2.1, but it is easy to give examples where that method does not work. 14-553810. Acta Mathematica. 94. Imprimé le 27 septembre 1955.

## CHAPTER III

## Maximal Differential Operators with Constant Coefficients

## 3.0. Introduction

Let $P$ and $Q$ be two maximal differential operators with constant coefficients. Our first question is: When is it true that $\mathcal{D}_P \subset \mathcal{D}_Q$? The corresponding problem for minimal differential operators was solved by Theorem 2.2. For the maximal operators we obtain the negative result that $\mathcal{D}_P \subset \mathcal{D}_Q$ implies either that $Q = aP + b$, with constant $a$ and $b$, or else that $P$ and $Q$ are ordinary differential operators, such that the degree of $Q$ is not greater than the degree of $P$. This is proved in section 3.1.

Although there exist no operators $Q$ (except for the trivial ones), such that $Qu \in L^2(\Omega)$ for every $u \in \mathcal{D}_P$, there may be operators $Q$, such that $Qu$ is locally square integrable in $\Omega$ for every $u \in \mathcal{D}_P$. There is in fact a class of operators $P$—the operators of local type—for which this is the case for every $Q$ weaker than $P$ in the sense of Chapter I. In that case the functions in $\mathcal{D}_P$ have the same regularity properties as the functions in $\mathcal{D}_{P_0}$. The class of operators of local type is determined in sections 3.3, 3.4 and 3.5. The main point is the construction of a fundamental solution in section 3.4. Elliptic operators are of local type. The complete operators of local type also turn out to possess all essential properties of elliptic operators. For instance, all solutions of the equation $Pu = 0$ are infinitely differentiable if and only if $P$ is complete and of local type. (Operators with this property are called elliptic by some authors, cf. Malgrange [21]. Thus our results give simple necessary and sufficient conditions for an operator to be elliptic in this sense.) We also estimate the magnitude of high derivatives of solutions, thus generalizing Holmgren's results for the equation of heat. As an application this gives us a result on the growth of null solutions. (The existence of null solutions is completely discussed for general operators in section 3.2.) Finally, in section 3.7, we establish a spectral theory of self-adjoint operators of local type. Examples of operators of local type are given in section 3.8.

A study of the asymptotic properties of the eigenfunctions (or rather spectral functions) of self-adjoint boundary problems, parallel to that given by Gårding [13] for elliptic operators, was originally planned. However, our results were not complete, since the Tauberian theorem of Ganelius [7], which was used by Gårding, is not sufficient in our general case. The author has therefore postponed the publication to another occasion.

## 3.1. Comparison of the domains of maximal differential operators

Let $P$ and $Q$ be two maximal differential operators with constant coefficients in $L^2(\Omega)$, where $\Omega$ is a bounded domain. Theorem 1.1 shows that, if $\mathcal{D}_P \subset \mathcal{D}_Q$, we must have

$$
\left\| Q u \right\| ^ {2} \leq C \left(\left\| P u \right\| ^ {2} + \left\| u \right\| ^ {2}\right), \quad u \in \mathcal {D} _ {P},\tag{3.1.1}
$$

where, as always, the norm is  $L^{2}$ -norm in  $\Omega$ . The condition (3.1.1) leads to the following theorem.

THEOREM 3.1. If the domain of P is part of the domain of Q, we have either  $Q = aP + b$  with constant a and b, or else  $P(\xi) = p(\langle x_{0}, \xi \rangle)$  and  $Q(\xi) = q(\langle x_{0}, \xi \rangle)$ , where  $x_{0}$  is a fixed real vector and the degree of the polynomial p is not less than the degree of the polynomial q.

In the first case it is obvious that  $D_{Q} \supset D_{P}$ , with equality unless a = 0. In the second case the same result follows from well-known facts concerning ordinary differential operators (see the example on page 169), if, for example,  $\Omega$  is a cylinder with axis in the  $x_{0}$ -direction.

To prove the theorem, we first note that (3.1.1) must hold for any infinitely differentiable function $u$. Hence we may set $u = e^{i\langle x,\zeta \rangle}$ with arbitrary complex $\zeta$, and then obtain

$$
\left| Q (\zeta) \right| ^ {2} \leq C \left(\left| P (\zeta) \right| ^ {2} + 1\right).\tag{3.1.2}
$$

Another necessary condition is obtained, if we set $u(x) = x^k e^{i\langle x,\xi \rangle}$ in (3.1.1):

$$
\int_ {\Omega} \left| x ^ {k} Q (\zeta) + i ^ {- 1} Q ^ {(k)} (\zeta) \right| ^ {2} e ^ {- 2 \langle x, \eta \rangle} d x \leq C \int_ {\Omega} (1 + \left| x ^ {k} P (\zeta) + i ^ {- 1} P ^ {(k)} (\zeta) \right| ^ {2}) e ^ {- 2 \langle x, \eta \rangle} d x.\tag{3.1.3}
$$

Using (3.1.2) and the boundedness of $x^{k}$ in $\Omega$, we now obtain

$$
\left| Q ^ {(k)} (\zeta) \right| ^ {2} \leq C ^ {\prime} \left(\left| P (\zeta) \right| ^ {2} + \left| P ^ {(k)} (\zeta) \right| ^ {2} + 1\right).\tag{3.1.4}
$$

The inequalities (3.1.2) and (3.1.4) are independent of each other. We first examine the consequences of (3.1.2) by algebraic methods.

LEMMA 3.1. Let $P(\zeta)$ and $Q(\zeta)$ be two polynomials in $\zeta = (\zeta_1, \ldots, \zeta_r)$ such that (3.1.2) is fulfilled for every complex $\zeta$. Then the polynomials must be algebraically dependent, that is, there exists a polynomial $R(s, t)$ in two complex variables $s$ and $t$ such that $R \neq 0$ and

$$
R (P, Q) = 0.\tag{3.1.5}
$$

PROOF. We may suppose without restriction that the polynomials are not constant, and choose the coordinate system such that in the developments

$$
P (\zeta) = \sum_ {0} ^ {n} a _ {k} \left(\zeta_ {2}, \dots , \zeta_ {\nu}\right) \zeta_ {1} ^ {k}, \quad Q (\zeta) = \sum_ {0} ^ {m} b _ {k} \left(\zeta_ {2}, \dots , \zeta_ {\nu}\right) \zeta_ {1} ^ {k}\tag{3.1.6}
$$

the highest coefficients $a_{n}$ and $b_{m}$ are constants $\neq 0$. Denote the resultant with respect to $\zeta_{1}$ of the two polynomials $P - \alpha$ and $Q - \beta$ by $R(\alpha, \beta, \zeta_{2}, \ldots, \zeta_{\nu})$. The resultant is a polynomial in $\alpha, \beta, \zeta_{2}, \ldots, \zeta_{\nu}$, and does not vanish identically. If the zeros of $P(\zeta) - \alpha$ for fixed $\zeta_{2}, \ldots, \zeta_{\nu}$ are $\zeta_{1} = t_{1}, \ldots, \zeta_{1} = t_{n}$, we have

$$
R = a _ {n} ^ {m} \prod_ {1} ^ {n} (Q (t _ {k}, \zeta_ {2}, \dots , \zeta_ {\nu}) - \beta).
$$

Since $P(t_k, \zeta_2, \ldots, \zeta_\nu) - \alpha = 0$, it follows from (3.1.2) that $|Q(t_k, \zeta_2, \ldots, \zeta_\nu)|^2 \leq C(1 + |\alpha|^2)$. Hence $R$ is bounded for fixed $\alpha$ and $\beta$, which proves that $R$ is independent of $\zeta_2, \ldots, \zeta_\nu$, so that we may write $R = R(\alpha, \beta)$. By definition, we have $R(\alpha, \beta) = 0$ if $P - \alpha$ and $Q - \beta$ have a common zero $\zeta_0$, that is, if $\alpha = P(\zeta_0)$, $\beta = Q(\zeta_0)$. Thus we obtain

$$
R \left(P \left(\zeta_ {0}\right), Q \left(\zeta_ {0}\right)\right) = 0,
$$

which completes the proof.

To proceed further we need a lemma, which is essentially a special case of Lüroth's theorem (cf. van der Waerden [33], § 63).

LEMMA 3.2. Let $R$ be a ring over a field $K$ such that $K \subset R \subset K[x]$, where $K[x]$ is the ring of polynomials in an indeterminate $x$ with coefficients in $K$. Then there is a polynomial $\vartheta \in R$ such that $R = K[\vartheta]$.

PROOF. Let $\vartheta$ be a not constant polynomial in $R$ of minimal degree. Then the polynomial $\vartheta(z) - \vartheta(x)$, considered as a polynomial in a second indeterminate $z$, has coefficients in $R$ and is irreducible in $R[z]$. For suppose that it decomposes in $R[z]$. The factors are then polynomials in $z$ with coefficients in $R$, so that a factor which is not independent of $x$ must be of at least the same degree in $x$ as $\vartheta$ is. Hence all factors except one must have coefficients in $K$, and since it is obvious that there are no such factors, the irreducibility follows. Hence, if $\eta(x)$ is any polynomial in $R$, the polynomial $\eta(z) - \eta(x)$ must be divisible by $\vartheta(z) - \vartheta(x)$ in $R[z]$, since both have the zero $z = x$. Denoting the term in the quotient, which is independent of $z$, by $\eta_1(x)$, we have $\eta_1 \in R$ and

$$
\eta (x) - \eta (0) = (\vartheta (x) - \vartheta (0)) \eta_ {1} (x).
$$

Assuming as we may that $\vartheta(0)=0$, we obtain

$$
\eta (x) = \eta (0) + \vartheta (x) \eta_ {1} (x), \quad \eta_ {1} (x) \in R.
$$

Now we can apply this result to the polynomial  $\eta_{1}$  and write

$$
\eta_ {1} (x) = \eta_ {1} (0) + \vartheta (x) \eta_ {2} (x), \quad \eta_ {2} (x) \in R,
$$

and so on. Since the degrees of the polynomials $\eta_1, \eta_2, \ldots$ decrease, we must after a finite number of steps come to a constant polynomial, which proves that $\eta \in K[\vartheta]$.

LEMMA 3.3.1 If two polynomials $P(\zeta)$ and $Q(\zeta)$ of $\zeta = (\zeta_1, \ldots, \zeta_r)$ are algebraically dependent, there exists a polynomial $W(\zeta)$ and two polynomials $p(t), q(t)$ in one variable, so that

$$
P (\zeta) = p (W (\zeta)), Q (\zeta) = q (W (\zeta)).\tag{3.1.7}
$$

Proof. By assumption we have

$$
\boldsymbol {F} (P (\zeta), Q (\zeta)) = \mathbf {0},
$$

where  $F(x, y)$  is a polynomial which may be supposed to be irreducible. Assuming as we may that P and Q are of the form (3.1.6) and setting  $\zeta_{1}=t$ ,  $\zeta_{2}=\cdots=\zeta_{\nu}=0$ , we find that the irreducible curve  $F(x, y)=0$  has a parametric representation  $x=x(t)$ ,  $y=y(t)$ , where  $x(t)$  and  $y(t)$  are polynomials in t. Now we apply Lemma 3.2 to the ring of polynomials generated by  $x(t)$  and  $y(t)$ . It follows that there is a polynomial  $\vartheta(t)$  in this ring, that is,  $\vartheta(t)=f(x(t), y(t))$ , where f is a polynomial, so that  $x(t)=p(\vartheta(t))$ ,  $y(t)=q(\vartheta(t))$ . Hence we have for any point on the curve

$$
x = p (f (x, y)), \quad y = q (f (x, y)),
$$

since this is true for a generic point. Setting  $x = P(\zeta)$ ,  $y = Q(\zeta)$  and denoting  $f(P(\zeta), Q(\zeta))$  by  $W(\zeta)$ , we obtain the desired result.

Combining Lemma 3.1 and Lemma 3.3, we conclude that the inequality (3.1.2) is valid if and only if there exists a polynomial $W(\zeta)$ and two polynomials $p(t)$ and $q(t)$, such that the degree of $q$ is not greater than the degree of $p$ and

$$
P (\zeta) = p (W (\zeta)), \quad Q (\zeta) = q (W (\zeta)).\tag{3.1.7}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  This lemma and another much deeper one, needed in an earlier version of this paper, were proved by Professor B. L. VAN DER WAERDEN in reply to a question from the author. His proof, which is based on Lüroth's theorem, includes in fact both Lemma 3.2 and Lemma 3.3, and differs only formally from the one given here,</span></small>

Polynomials of this form satisfy the inequality (3.1.4) if

$$
\left| \frac {\partial W}{\partial \zeta_ {k}} \right| ^ {2} \left(\left| q ^ {\prime} (W) \right| ^ {2} - C ^ {\prime} \mid p ^ {\prime} (W) \right| ^ {2}) \leq C ^ {\prime} (\left| p (W) \right| ^ {2} + 1).\tag{3.1.8}
$$

In studying this inequality we have to distinguish between two different cases.

I) If $|q'(t)|^2 - C' |p'(t)|^2 \leq 0$ for every complex $t$, it follows that any zero of $p'$ is a zero of $q'$ with at least the same multiplicity. Now $q'$ has not higher degree than $p'$, so it follows that $q'(t) = a p'(t)$ with some constant $a$. Hence $q(t) = a p(t) + b$ and $Q(\zeta) = a P(\zeta) + b$, so that we have one of the cases mentioned in Theorem 3.1.

II) Now suppose that the open set $U$ of all $t$ such that $|q'(t)|^2 - C' |p'(t)|^2 > 0$ is not empty. Then it follows from (3.1.8), if $\alpha$ and $\beta$ are fixed complex numbers such that $\alpha \in U$, that $|\partial W / \partial \zeta_k - \beta| < C''$ when $W - \alpha = 0$. Since the arguments of the proof of Lemma 3.1 apply under this weaker assumption, it follows that $W$ and $\partial W / \partial \zeta_k$ are algebraically dependent for any $k$. Hence $\partial W / \partial \zeta_k$ is constant for any $k$ on a piece of surface where $W(\zeta) = \text{constant}$. Thus the surface is a portion of a plane, and $W$ must be constant in the whole plane. Since two planes, where $W$ has different constant values, cannot meet, it follows that $W$ is constant in a set of parallel planes $\langle z_0, \zeta \rangle = \text{constant}$. Hence $W$ is a polynomial in $\langle z_0, \zeta \rangle$, and using (3.1.7) we obtain

$$
P (\zeta) = p \left(\langle z _ {0}, \zeta \rangle\right), Q (\zeta) = q \left(\langle z _ {0}, \zeta \rangle\right),\tag{3.1.9}
$$

where p and q may not be the same polynomials as in (3.1.7). Polynomials of the form (3.1.9) satisfy both (3.1.2) and (3.1.4). To prove the remaining part of the theorem, namely that  $z_{0}$  must be proportional to a real vector unless  $q = a p + b$ , we must therefore go back to the original condition (3.1.1).

Thus suppose that the polynomials P and Q are of the form (3.1.9) and that  $z_{0}$  is not proportional to any real vector. We shall prove that  $q'(t)=ap'(t)$ , or, equivalently, that a zero  $\tau$  of  $p'$  with multiplicity k is a zero of  $q'$  with the same multiplicity. It is sufficient to suppose that  $\tau=0$ . With a suitable complex vector  $\zeta$  and a real vector  $\eta$  we shall set

$$
u (x) = \langle x, \eta \rangle^ {k} e ^ {i \langle x, \zeta \rangle}.\tag{3.1.10}
$$

It easily follows from Leibniz' formula that

$$
P (D) u = p \left(\langle z _ {0}, D \rangle\right) u = \sum_ {j = 0} ^ {k} \binom {k} {j} \left\langle z _ {0}, \eta \right\rangle^ {j} \left\langle x, \eta \right\rangle^ {k - j} p ^ {(j)} \left(\left\langle z _ {0}, \zeta \right\rangle\right) e ^ {i \langle x, \zeta \rangle},\tag{3.1.11}
$$

where $p^{(j)}$ is the $j^{\mathrm{th}}$ derivative of $p$.

Since  $z_{0}$  is not proportional to a real vector, there exists a vector  $\zeta_{0}=\xi_{0}+i\eta_{0}$  such that  $\langle z_{0},\zeta_{0}\rangle=0$  but  $\langle z_{0},\eta_{0}\rangle\neq0$ . Denote by  $u_{t}$  the function obtained by setting  $\eta=\eta_{0}$  and  $\zeta=t\zeta_{0}$  with real fixed t in (3.1.10). Since we have assumed that

$$
p ^ {\prime} (0) = \dots = p ^ {(k)} (0) = 0,
$$

it follows from (3.1.11) that

$$
P (D) u _ {t} = p (0) \langle x, \eta_ {0} \rangle^ {k} e ^ {i \langle x, t \zeta_ {0} \rangle}.
$$

With the notation

$$
f (u) = \sum_ {j = 0} ^ {k} \binom {k} {j} \left\langle z _ {0}, \eta_ {0} \right\rangle^ {j} u ^ {k - j} q ^ {(j)} (0)
$$

we also obtain

$$
Q (D) u _ {t} = f (\langle x, \eta_ {0} \rangle) e ^ {i \langle x, t \zeta_ {0} \rangle},
$$

and to show that  $q'(0)=\cdots=q^{(k)}(0)=0$  we have to prove that  $f(u)$  cannot contain any term of lower order than  $u^{k}$ .

The inequality (3.1.1) gives when applied to the functions  $u_{t}$

$$
\int_ {\Omega} \left| f (\langle x, \eta_ {0} \rangle) \right| ^ {2} e ^ {- 2 t \langle x, \eta_ {0} \rangle} d x \leq C (1 + | p (0) | ^ {2}) \int_ {\Omega} \left| \langle x, \eta_ {0} \rangle \right| ^ {2 k} e ^ {- 2 t \langle x, \eta_ {0} \rangle} d x.\tag{3.1.12}
$$

Translating $\Omega$, if necessary, we may suppose that

$$
\inf _ {x \in \Omega} \langle x, \eta_ {0} \rangle = 0.\tag{3.1.13}
$$

Let $\alpha(u)$ be the measure of the set

$$
\{x; x \in \Omega , \langle x, \eta_ {0} \rangle \leq u \}.
$$

In virtue of (3.1.13) we have $\alpha(u)=0$, if $u\leq0$, and $\alpha(u)>0$, if $u>0$. Furthermore, $\alpha(u)$ is constant for large values of $u$. The inequality (3.1.12) now takes the form

$$
\int_ {0} ^ {\infty} | f (u) | ^ {2} e ^ {- 2 t u} d \alpha (u) \leq C ^ {\prime} \int_ {0} ^ {\infty} u ^ {2 k} e ^ {- 2 t u} d \alpha (u), \quad 0 <   t <   \infty .
$$

Suppose that $u^k$ is not a factor of $f(u)$. Then we can find $\varepsilon > 0$ such that $|f(u)|^2 > 2C'u^{2k}$ for $0 < u < \varepsilon$. Hence

$$
2 C ^ {\prime} \int_ {0} ^ {\varepsilon} u ^ {2 k} e ^ {- 2 t u} d \alpha (u) \leq \int_ {0} ^ {\infty} | f (u) | ^ {2} e ^ {- 2 t u} d \alpha (u) \leq C ^ {\prime} \int_ {0} ^ {\infty} u ^ {2 k} e ^ {- 2 t u} d \alpha (u),
$$

and consequently

$$
\int_ {0} ^ {\varepsilon} u ^ {2 k} e ^ {- 2 t u} d \alpha (u) \leq \int_ {\varepsilon} ^ {\infty} u ^ {2 k} e ^ {- 2 t u} d \alpha (u).
$$

Estimating the two sides of this inequality in an obvious fashion, we obtain

$$
e ^ {- t \varepsilon} \int_ {0} ^ {\frac {\varepsilon}{2}} u ^ {2 k} d \alpha (u) \leq e ^ {- 2 t \varepsilon} \int_ {\varepsilon} ^ {\infty} u ^ {2 k} d \alpha (u),
$$

which gives a contradiction when  $t \to \infty$ , since the integral on the left-hand side does not vanish. Hence  $u^{k}$  is a factor of  $f(u)$ , so that  $q'(t)$  has a zero of multiplicity k for t = 0. This completes the proof.

REMARK. It also follows from the proof that there exists a uniformly continuous function u, so that  $P(D)u$  is uniformly continuous but  $Q(D)u$  is not uniformly continuous, unless we have one of the two exceptional cases of Theorem 3.1. In fact, if we substitute for  $L^{2}(\Omega)$  the space C of uniformly continuous functions in  $\Omega$, we still get the conditions (3.1.2) and (3.1.4), and we can also give a modification of the discussion at the end of the proof.

Somewhat roughly, we might formulate the result of this section as follows: Maximal partial differential operators with constant coefficients are characterized by their domains, apart from a linear combination with the identity operator.

## 3.2. The existence of null solutions

We shall call a function $u \neq 0$ a null solution of $P$, if it is infinitely differentiable, satisfies the equation $Pu = 0$, and vanishes in a half-space $\langle x, \xi \rangle \geq 0$, where $\xi$ is a given fixed vector $\neq 0$. It follows from Holmgren's uniqueness theorem (cf. John [16]) that a null solution cannot exist, unless the plane $\langle x, \xi \rangle = 0$ is characteristic, that is, $p(\xi) = 0$, where $p$ is the principal part of $P$. If $P$ is homogeneous, it is obvious that any function $f(\langle x, \xi \rangle)$, where $0 \neq f \in C^\infty$ and $f(t) = 0$ for $t > 0$, is then a null solution. For equations with lower order terms the existence of null solutions seems to have been proved only for special equations, in particular, the heat equation (Tychonov [32], Täcklind [31], see also Hille [14]). Following the proof of Hille [14] and using some series developments from Petrowsky [26], we can prove the following general existence theorem.

## THEOREM 3.2. There exist null solutions of P for every characteristic  $\xi^{1}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  For equations with variable coefficients it may happen, as has been proved by MYCHKIS [22], that a solution can only be continued in one way across the whole of some real characteristic, even if it can be locally continued in different ways.</span></small>

PROOF. Let us consider the equation  $P(s\xi+t\eta)=0$ , where  $\eta$  is a fixed non-characteristic vector and s and t are complex numbers. Since  $p(\xi)=0$ , it easily follows as in Petrowsky [26] that there is a root  $t=t(s)$ , such that  $t/s\to0$  when  $s\to\infty$ , and we can develop  $t(s)$  in a Puiseux series

$$
t = s ^ {k / p} \sum_ {j = 0} ^ {\infty} c _ {j} s ^ {- j / p},
$$

where $k$ and $p$ are positive integers and $k < p$. Hence $t(s)$ is analytic outside a circle $|s| = M$, and when $|s| \to \infty$ we have

$$
\left| t (s) \right| = O \left(\left| s \right| ^ {e}\right),
$$

where $\varrho < 1$. Let $\varrho'$ be a number such that $\varrho < \varrho' < 1$, and set with $\tau > M$

$$
u (x) = \int_ {i \tau - \infty} ^ {i \tau + \infty} e ^ {i \langle x, s \xi + t (s) \eta \rangle} e ^ {- (s / i) \varrho^ {\prime}} d s \quad (s = \sigma + i \tau).
$$

Here we define  $(s/i)^{e'}$  so that it is real and positive when s is on the positive imaginary axis, and use a fixed branch of  $t(s)$ . The integral is obviously convergent and independent of  $\tau$ , for when x is in a fixed bounded set we have

$$
\operatorname{Re} \left(i t (s) \langle x, \eta \rangle - \left(\frac {s}{i}\right) ^ {\varrho^ {\prime}}\right) \leq C | s | ^ {\varrho} - | s | ^ {\varrho^ {\prime}} \sin \frac {\pi \varrho^ {\prime}}{2} <   - c | s | ^ {\varrho^ {\prime}} \quad (\text { Im   } s > M),
$$

for large  $|s|$ , c being a positive constant. This estimate also proves that the integral is uniformly convergent after an arbitrary number of differentiations with respect to x, so that  $u(x)$  is infinitely differentiable and solves the equation  $P(D)u=0$ . It is also obvious that  $u\neq0$ . Now we have for sufficiently large  $\tau$

$$
\left| u (x) \right| \leq e ^ {- \tau \langle x, \xi \rangle} \int_ {- \infty} ^ {+ \infty} e ^ {- c | \sigma | ^ {\varrho^ {\prime}}} d \sigma .
$$

Hence, letting $\tau \to +\infty$, we conclude that $u(x) = 0$ if $\langle x, \xi \rangle > 0$.

The following corollary is a theorem by Petrowsky [26], who also considered systems of differential equations.

COROLLARY 3.1. If y is a direction which cuts some characteristic plane of the operator P, then there is a solution u of  $P(D)u=0$  such that  $u(x+ty)$  is not an analytic function of t.

In fact, a null solution u, which vanishes on one side of the characteristic plane, will possess the required property, since we could otherwise prove by analytic continuation that u=0.

## 3.3. Differential operators of local type

From Theorem 3.1 it follows that, if the operator $P(D)$ depends on more than one variable and $\Omega$ is a bounded domain, we can find a function $u \in \mathcal{D}_P$ and a function $\psi \in C^\infty(\overline{\Omega})$ such that $\psi u \notin \mathcal{D}_P$. For suppose that this were not possible, so that whenever $u \in \mathcal{D}_P$ and $\psi \in C^\infty(\overline{\Omega})$ we have $\psi u \in \mathcal{D}_P$. With $\psi = e^{i\langle x,\xi\rangle}$, $\xi \neq 0$, it would follow that any function $u \in \mathcal{D}_P$ is also in the maximal domain of the operator $P(D + \xi)$, which would contradict Theorem 3.1. This negative result, which contrasts with Theorem 2.10, was also proved in section 2.8 by means of explicit examples, when $P$ is the Laplace operator or the wave operator in two variables. For the wave operator we saw that $P(D)(\psi u)$ does not even need to be locally square integrable in $\Omega$, but for the Laplace operator we only proved that $P(D)(\psi u)$ may not be square integrable over the whole of $\Omega$. We now raise the problem to determine those operators for which only this situation can appear. More precisely, we seek those operators $P$ which satisfy the following definition.

DEFINITION 3.1. A differential operator $P(D)$ is said to be of local type, if the product of any function in $\mathcal{D}_P$ by any function in $C_0^\infty(\Omega)$ is in $\mathcal{D}_P$, and consequently, in virtue of Lemma 2.11, in $\mathcal{D}_{P_0}$.

An equivalent definition is that $P$ is of local type, if the functions in $\mathcal{D}_P$ and the functions in $\mathcal{D}_{P_0}$ have the same local regularity properties, that is, if any function in $\mathcal{D}_P$ equals some function in $\mathcal{D}_{P_0}$ in an arbitrary compact subset of $\Omega$. That this property follows from Definition 3.1 is obvious, for we can choose $\psi \in C_0^\infty$ such that $\psi = 1$ on any given compact set. Conversely, if $P$ has this property, it follows from Theorem 2.10 that Definition 3.1 is fulfilled. Thus Theorem 2.12 proves that a necessary and sufficient condition for an operator to be of local type is that $P^{(\alpha)}(D)u$ is a locally square integrable function for any $\alpha$ and any $u \in \mathcal{D}_P$. If $\Omega'$ is a domain with compact closure in $\Omega$, we can hence apply Theorem 1.1 to the mapping

$$
\mathcal {D} _ {P} \ni u \rightarrow P ^ {(\alpha)} (D) u \in L ^ {2} (\Omega^ {\prime}),
$$

and then obtain the following lemma.

LEMMA 3.4. If $P(D)$ is of local type and the domain $\Omega'$ has compact closure in $\Omega$, there exists a constant $C$ such that

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Ω,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Ω.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Observe that we require this property of the operator P for any domain  $\Omega$ . It will however follow from our results that it is sufficient to assume that the definition is fulfilled for one bounded domain  $\Omega$ , it then follows for any domain, bounded or not bounded.</span></small>

$$
\int_ {\Omega^ {\prime}} \left| P ^ {(\alpha)} (D) u \right| ^ {2} d x \leq C \left(\int_ {\Omega} \left| P (D) u \right| ^ {2} d x + \int_ {\Omega} \left| u \right| ^ {2} d x\right), \quad u \in \mathcal {D} _ {P}.\tag{3.3.1}
$$

Let $\Omega$ be a bounded domain. Setting $u(x) = e^{i\langle x,\zeta \rangle}$ in (3.3.1), $\zeta = \xi + i\eta$, we obtain

$$
\left| P ^ {(\alpha)} (\zeta) \right| ^ {2} \int_ {\Omega^ {\prime}} e ^ {- 2 \langle x, \eta \rangle} d x \leq C (1 + | P (\zeta) | ^ {2}) \int_ {\Omega} e ^ {- 2 \langle x, \eta \rangle} d x.\tag{3.3.2}
$$

If $\delta$ is the supremum of $2|x|$ when $x\in \Omega$, we have the two estimates

$$
\int_ {\Omega^ {\prime}} e ^ {- 2 \langle x, \eta \rangle} d x \geq e ^ {- \delta | \eta |} \int_ {\Omega^ {\prime}} d x = e ^ {- \delta | \eta |} m (\Omega^ {\prime}), \int_ {\Omega} e ^ {- 2 \langle x, \eta \rangle} d x \leq e ^ {\delta | \eta |} m (\Omega).
$$

Hence it follows from (3.3.2) that

$$
\left| P ^ {(\alpha)} (\zeta) \right| ^ {2} \leq C \frac {m (\Omega)}{m \left(\Omega^ {\prime}\right)} e ^ {2 \delta | \eta |} (1 + \left| P (\zeta) \right| ^ {2}).\tag{3.3.3}
$$

Adding the inequalities (3.3.3) for all $\alpha$, and using the notation $\tilde{P}(\zeta) = (\sum |P^{(\alpha)}(\zeta)|^2)^{\frac{1}{2}}$ again, we obtain the following lemma.

LEMMA 3.5. Let $P$ be of local type. Then for any $A$ there is a constant $C$ such that

$$
\tilde {P} (\zeta) ^ {2} \leq C (1 + | P (\zeta) | ^ {2}),\tag{3.3.4}
$$

when $|\operatorname{Im} \zeta| < A$.

The necessary condition for an operator to be of local type, which we have now derived, is in fact also sufficient. Before proving this, we shall deduce other equivalent conditions, which seem to be more natural and useful.

LEMMA 3.6. If a polynomial $P$ satisfies (3.3.4), we have

$$
\left| P (\xi + i \eta) \right|\rightarrow \infty \text {   when   } \xi \rightarrow \infty \text {   modulo   } \Lambda (P),\tag{3.3.5}
$$

and the convergence is uniform in  $\eta$ , if  $|\eta|<A$ , where A is an arbitrary fixed positive number.

Proof. Examination of the proof of Theorem 2.17 shows that

$$
\tilde {P} (\zeta) \rightarrow \infty \text {   when   } \zeta \rightarrow \infty \text {   modulo   } \Lambda^ {*} (P),
$$

where  $\Lambda^{*}(P)$  is the complex lineality space of P, defined by (2.8.21), if we omit the word “real”. Since  $\Lambda(P)$  is the set of real vectors in  $\Lambda^{*}(P)$ , the assertion now follows from (3.3.4).

We shall next prove two lemmas, which give a converse of Lemma 3.6 in a sharp form, which will be used later. For convenience we only formulate them for complete polynomials.

LEMMA 3.7. Suppose that for any positive number $A$ there exists a number $B$ such that

$$
P (\xi + i \eta) \neq 0, w h e n | \eta | <   A a n d | \xi | > B.\tag{3.3.6}
$$

Then the polynomial $P$ is complete, and for any fixed real vector $\vartheta$ we have

$$
\frac {P (\xi + \vartheta)}{P (\xi)} \rightarrow 1 \text {   when   } \xi \rightarrow \infty .\tag{3.3.7}
$$

PROOF. That P must be complete is obvious. In proving (3.3.7) we may assume that the coordinates are so chosen that  $\vartheta=(1,0,\ldots,0)$ . Now let  $\varepsilon$  be a fixed small positive number. In virtue of the assumptions we can find a number B such that

$$
P (\xi + i \eta) \neq 0 \text {   when   } | \eta | <   \varepsilon^ {- 1} \text {   and   } | \xi | > B.
$$

Then the inequality $|\xi - \zeta'| \geq \varepsilon^{-1}$ is valid, if $|\xi| > B + \varepsilon^{-1}$ and $P(\zeta') = 0$. For setting $\zeta' = \xi' + i\eta'$ we have either $|\eta'| \geq \varepsilon^{-1}$, or else $|\xi'| \leq B$ so that $|\xi - \xi'| \geq \varepsilon^{-1}$. Giving constant values to $\xi_2, \ldots, \xi_r$ we can write

$$
P (\xi) = E \prod_ {1} ^ {m} \left(\xi_ {1} - t _ {k}\right),
$$

where  $(t_{k}, \xi_{2}, \ldots, \xi_{\nu})$  is a zero of P. Hence we have  $|t_{k} - \xi_{1}| \geq \varepsilon^{-1}$  if  $|\xi| > B + \varepsilon^{-1}$ . Using this estimate in the formula

$$
\frac {P (\xi + \vartheta)}{P (\xi)} = \prod_ {1} ^ {m} \frac {\xi_ {1} + 1 - t _ {k}}{\xi_ {1} - t _ {k}} = \prod_ {1} ^ {m} \left(1 + \frac {1}{\xi_ {1} - t _ {k}}\right)
$$

we obtain

$$
\left| \frac {P (\xi + \vartheta)}{P (\xi)} - 1 \right| \leq m \varepsilon (1 + \varepsilon) ^ {m - 1}, | \xi | > B + \varepsilon^ {- 1},
$$

which proves the assertion.

LEMMA 3.8. If for every constant real vector $\vartheta$

$$
\frac {P (\xi + \vartheta)}{P (\xi)} \rightarrow 1 \text {   when   } \xi \rightarrow \infty ,\tag{3.3.7}
$$

then (3.3.7) is valid for every complex $\vartheta$, and the convergence is uniform in $\vartheta$, if $|\vartheta| < A$ for some fixed $A$. Furthermore, we have, if $|\alpha| \neq 0$,

$$
\frac {P ^ {(\alpha)} (\xi + \vartheta)}{P (\xi + \vartheta)} \rightarrow 0 \text {   when   } \xi \rightarrow \infty ,\tag{3.3.8}
$$

uniformly in $\vartheta$, if $|\vartheta| < A$.

Proof. In virtue of Lemma 2.10 we can write

$$
P ^ {(\alpha)} (\xi) = \sum_ {1} ^ {m} t _ {i} P (\xi + \vartheta_ {i}),\tag{3.3.9}
$$

where  $\vartheta_{i}$  are real vectors. Since the principal parts on the right-hand side must cancel out, if  $|\alpha| \neq 0$ , we have  $\sum t_{i} = 0$ . Hence we obtain in virtue of (3.3.7)

$$
\frac {P ^ {(\alpha)} (\xi)}{P (\xi)} \rightarrow \sum_ {1} ^ {m} t _ {i} = 0 \text {   when   } \xi \rightarrow \infty .\tag{3.3.10}
$$

From Taylor's formula it follows that

$$
\frac {P (\xi + \vartheta)}{P (\xi)} = 1 + \sum_ {| \alpha | \neq 0} \frac {P ^ {(\alpha)} (\xi)}{P (\xi)} \frac {\vartheta_ {\alpha}}{| \alpha | !},
$$

which proves that (3.3.7) is valid for arbitrary complex $\vartheta$, and also exhibits the asserted uniform convergence. Using this result and (3.3.9), we obtain

$$
\frac {P ^ {(\alpha)} (\xi + \vartheta)}{P (\xi + \vartheta)} = \sum_ {1} ^ {m} t _ {i} \frac {P (\xi + \vartheta + \vartheta_ {i})}{P (\xi)} \frac {P (\xi)}{P (\xi + \vartheta)} \rightarrow \sum_ {1} ^ {m} t _ {i} = 0 \text {when} \xi \rightarrow \infty ,
$$

uniformly in $\vartheta$.

THEOREM 3.3. The following five conditions on a polynomial $P$ are all equivalent:

I) For an arbitrary given $A$, the polynomial $P(\xi + i\eta)$ does not vanish, if $|\eta| < A$ and the distance from $\xi$ to $\Lambda(P)$ is sufficiently large.

II) For every real vector $\vartheta$ we have

$$
\frac {P (\xi + \vartheta)}{P (\xi)} \rightarrow 1
$$

when $\xi$ is real and $\rightarrow \infty$ modulo $\Lambda(P)$. The convergence is uniform in $\vartheta$, if $|\vartheta|$ is bounded.

III) For every $\alpha$ with $|\alpha| \neq 0$ we have

$$
\frac {P ^ {(\alpha)} (\xi)}{P (\xi)} \rightarrow 0,
$$

when $\xi$ is real and $\rightarrow \infty$ modulo $\Lambda(P)$.

IV) For any $A$ there is a constant $C$ such that when $|\eta| \leq A$.

$$
\tilde {P} (\xi + i \eta) ^ {2} \leq C (1 + | P (\xi + i \eta) | ^ {2}).
$$

V) When $\xi \to \infty$ modulo $\Lambda(P)$ we have $|P(\xi + i\eta)| \to \infty$, and the convergence is uniform in $\eta$ when $|\eta| \leq A$.

Each of these conditions is a necessary and sufficient condition for the operator P to be of local type.

PROOF. We first prove the equivalence of the five conditions. Lemmas 3.7 and 3.8 show that I implies II and that II implies III and IV. Furthermore, Lemma 3.6 proves that IV implies V, and I is obviously a consequence of V. Hence the conditions I, II, IV, V are all equivalent. Since III follows from II, and the proof of Lemma 3.8 shows that II follows from III, the equivalence of the conditions is established. In virtue of Lemma 3.5 the condition IV is a necessary condition for P to be of local type.

We note that, if P is complete, we may omit “modulo  $\Lambda(P)$ ” from the statement, and that the theorem states that a polynomial is of local type, if the complete polynomial which it induces in  $R^{\nu}/\Lambda(P)$  is of local type. The easy but space-consuming verification of this fact may be left to the reader. Thus in proving the sufficiency of the conditions I–V, we may restrict ourselves to the case of complete polynomials. In that case we shall carry out the proof in section 3.5, by means of a fundamental solution, which will be constructed in the next section.

## 3.4. Construction of a fundamental solution of a complete operator of local type

In this section we shall consistently use the theory of distributions, without explicit reference at every point. The definitions and results, which we use, can of course be found in Schwartz [28]. Our purpose is to construct a fundamental solution, that is, a distribution E such that

$$
E * (P (D) u) = u, \quad u \in C _ {0} ^ {\infty} (R ^ {\nu}),\tag{3.4.1}
$$

and to prove certain regularity properties of E. The results are stated in the following theorem.

THEOREM 3.4. Let $P$ be complete and satisfy the conditions I-V of Theorem 3.3. Then $P(D)$ has a fundamental solution $E$ with the properties:

I) In the domain $x \neq 0$ the distribution $E$ is an infinitely differentiable function $E(x)$.

## II) If $u$ is square integrable and has compact support, the convolution

$$
P ^ {(\alpha)} (D) E * u
$$

is a locally square integrable function.

REMARKS. 1. Every fundamental solution has the properties I and II. In fact, we shall see later that the difference between two fundamental solutions is infinitely differentiable.

2. Schwartz [28] has called a function $E(x)$, which is infinitely differentiable for $x \neq 0$ and integrable over a neighbourhood of the origin, a “noyau élémentaire”, if the distribution $E$ defined by

$$
E (u) = \int E (x) u (x) d x
$$

is a fundamental solution. He proved that all solutions of the equation $Pu = 0$ are infinitely differentiable if $P$ possesses a “noyau élémentaire”. We shall not prove here that the fundamental solution of a complete operator of local type is a “noyau élémentaire”, but we shall nevertheless prove that all solutions are infinitely differentiable.

If  $P(\xi)$  did not vanish for any real  $\xi$ , we could obtain a fundamental solution by writing

$$
E * u (x) = (2 \pi) ^ {- v / 2} \int e ^ {i \langle x, \xi \rangle} \frac {\hat {u} (\xi)}{P (\xi)} d \xi , u \in C _ {0} ^ {\infty},\tag{3.4.2}
$$

or equivalently

$$
E (\check {u}) = (2 \pi) ^ {- \nu / 2} \int \frac {\hat {u} (\xi)}{P (\xi)} d \xi , u \in C _ {0} ^ {\infty},\tag{3.4.3}
$$

where  $\check{u}$  is defined by  $\check{u}(x)=u(-x)$ . Now the polynomial  $P(\xi)$  has in general real zeros, and we must then give (3.4.3) a generalized sense.

We shall define (3.4.3) as a repeated integral, first an integral in the complex domain with respect to  $\xi_{1}$ , and then an integral with respect to the other real variables. We may then assume that the coordinates are chosen such that the highest power of  $\xi_{1}$  in  $P(\xi)$  has a constant coefficient.

In virtue of the condition V in Theorem 3.3 we have $|P(\xi)| \geq 1$, if $\xi$ is real and $|\xi| \geq C$, where $C$ is a suitable constant. Thus $|P(\xi)| \geq 1$, if $\xi_2^2 + \cdots + \xi_\nu^2 \geq C^2$. Since the zeros of a polynomial vary continuously with parameters which do not occur in the highest order term, we can find a second constant $C'$ such that $|P(\zeta_1, \xi_2, \cdots, \xi_\nu)| \geq 1$, if $\xi_2, \cdots, \xi_\nu$ are real, $\xi_2^2 + \cdots + \xi_\nu^2 \leq C^2$, and $|\zeta_1| \geq C'$.

Now we set for $u \in C_0^\infty (R^\nu)$

$$
E (\check {u}) = (2 \pi) ^ {- \nu / 2} \int d \xi_ {2} \dots d \xi_ {\nu} \oint \frac {\hat {u} (\xi)}{P (\xi)} d \xi_ {1} = (2 \pi) ^ {- \nu / 2} \oint \frac {\hat {u} (\xi)}{P (\xi)} d \xi .\tag{3.4.4}
$$

The integral with respect to $\xi_{1}$ shall be extended over the real axis, if $\xi_{2}^{2}+\cdots+\xi_{\nu}^{2}\geq C^{2}$, and over the real axis with the interval $(-C', C')$ replaced by a semi-circle in the lower half-plane, if $\xi_{2}^{2}+\cdots+\xi_{\nu}^{2}<C^{2}$. Thus we have $|P(\xi)|\geq 1$ everywhere in the integral.

Since $u \in C_0^\infty$, it follows that $\hat{u}$ is an entire analytic function, which decreases rapidly in the real domain. Hence the integral (3.4.4) is convergent. It is plain that the formula (3.4.2) is valid, if we interpret the integral in the way just defined. Thus, if $u \in C_0^\infty (R^n)$, we have

$$
E * (P (D) u) = (2 \pi) ^ {- \nu / 2} \oint e ^ {i \langle x, \xi \rangle} P (\xi) \hat {u} (\xi) / P (\xi) d \xi = (2 \pi) ^ {- \nu / 2} \oint e ^ {i \langle x, \xi \rangle} \hat {u} (\xi) d \xi .
$$

Since the integrand is an analytic function of  $\xi_{1}$ , we may shift the integration path back to the real axis. Hence we obtain

$$
E * (P (D) u) (x) = (2 \pi) ^ {- \nu / 2} \int e ^ {i \langle x, \xi \rangle} \hat {u} (\xi) d \xi = u (x),
$$

which proves that E is a fundamental solution.

We now divide the integral (3.4.4) into two parts in the following manner. If  $R = \sqrt{C^{2} + C'^{2}}$ , we have  $|\xi| < R$  in the part of the integral (3.4.4), where  $\xi$  is not real. Thus if we write

(3.4.5)

$$
\boldsymbol {E} = \boldsymbol {E _ {1}} + \boldsymbol {E _ {2}},\tag{3.4.6}
$$

$$
E _ {1} (\check {u}) = (2 \pi) ^ {- \nu / 2} \int_ {| \xi | \geq R} \frac {\hat {u} (\xi)}{P (\xi)} d \xi , E _ {2} (\check {u}) = (2 \pi) ^ {- \nu / 2} \oint_ {| \xi | \leq R} \frac {\hat {u} (\xi)}{P (\xi)} d \xi ,
$$

the variable $\xi$ only assumes real values in the integral defining $E_{1}$. The distribution $E_{2}$ is an entire analytic function, for when $u\in C_0^\infty$ we obtain in virtue of the definition of $\hat{u}$

$$
E _ {2} (\check {u}) = (2 \pi) ^ {- \nu} \oint_ {| \xi | \leq R} \frac {d \xi}{P (\xi)} \int u (x) e ^ {- i \langle x, \xi \rangle} d x = (2 \pi) ^ {- \nu} \int \check {u} (x) d x \oint_ {| \xi | \leq R} \frac {e ^ {i \langle x , \xi \rangle}}{P (\xi)} d \xi .
$$

The change of the order of integrations is justified by the fact that both integrals are only extended over compact sets. Hence  $E_{2}$  equals the function

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ξ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  There is a very large freedom in the choice of integration paths, and different choices give different fundamental solutions. Note that  $\xi$  is here a complex variable, whereas  $\xi$  always denotes a real vector elsewhere in this paper.</span></small>

$$
E _ {2} (x) = (2 \pi) ^ {- \nu} \oint_ {| \xi | \leq R} \frac {e ^ {i \langle x , \xi \rangle}}{P (\xi)} d \xi ,\tag{3.4.7}
$$

which is an entire analytic function, since the integral is uniformly convergent when $|x|$ is bounded.

Let $u \in L^2$ have a compact support. The convolution $P^{(\alpha)}(D)E_2 * u$ is then an analytic function. Thus the assertion II of Theorem 3.4 will follow, if we prove that $P^{(\alpha)}(D)E_1 * u$ is square integrable. Let $\varphi \in C_0^\infty$. Then the function $u * \varphi$ is also in $C_0^\infty$, and in virtue of (3.4.6) we obtain

$$
\left(P ^ {(\alpha)} (D) E _ {1} * u\right) (\check {\varphi}) = P ^ {(\alpha)} (D) E _ {1} * u * \varphi (0) = \int_ {| \xi | \geq R} \frac {P ^ {(\alpha)} (\xi)}{P (\xi)} \hat {u} (\xi) \hat {\varphi} (\xi) d \xi ,\tag{3.4.8}
$$

so that the Fourier transform of $P^{(\alpha)}(D)E_1*u$ is a function which vanishes when $|\xi| < R$ and equals $\hat{u}(\xi)P^{(\alpha)}(\xi)/P(\xi)$ when $|\xi| \geq R$. Noting that $P^{(\alpha)}(\xi)/P(\xi)$ is bounded when $|\xi| \geq R$ in virtue of condition III of Theorem 3.3, and that $\hat{u}(\xi)$ is square integrable, we conclude that the Fourier transform of $P^{(\alpha)}(D)E_1*u$ is a square integrable function. Hence $P^{(\alpha)}(D)E_1*u$ is also square integrable, which completes the proof of the assertion II of the theorem.

We now turn to the proof of assertion I. Since we have already proved that  $E_{2}$  is an entire analytic function, it remains to prove that  $E_{1}$  is an infinitely differentiable function for  $x=0$ . We need the following algebraic lemma, which gives a precise form of the condition I of Theorem 3.3.

LEMMA 3.9. Let $y \neq 0$ be a fixed vector in $R^{\nu}$, and set

$$
M (\tau) = \inf _ {\zeta , \xi} | \zeta - \xi |,\tag{3.4.9}
$$

where $\zeta$ is a vector in $C_{\nu}$ such that $P(\zeta) = 0$, and $\xi$ is a vector in $R_{\nu}$ such that $|\langle y, \xi \rangle| = \tau$. Then there exist positive numbers $a$ and $b$ such that

$$
M (\tau) \tau^ {- b} \rightarrow a w h e n \tau \rightarrow \infty .
$$

PROOF. It follows from condition I of Theorem 3.3 that the infimum in (3.4.9) is attained, and that  $M(\tau)$  is a continuous function of  $\tau$ . The system of equations

$$
P (\zeta) = 0, \langle y, \xi \rangle^ {2} = \tau^ {2}, | \zeta - \xi | ^ {2} = \mu^ {2}\tag{3.4.10}
$$

has a solution $\zeta \in C_{\nu}, \xi \in R_{\nu}$ if and only if $\mu \geq M(\tau)$. Considering $C_{\nu}$ as a 2$\nu$-dimensional real vector space and the equation $P(\zeta) = 0$ as two real equations, we can eliminate the variables $\zeta$ and $\xi$ from (3.4.10) by means of Theorem 3 of Seiden-15-553810. Acta Mathematica. 94. Imprimé le 27 septembre 1955.

berg [29]. $^{1}$  We then obtain a finite number of finite sets  $G_{1}, \ldots, G_{s}$  of polynomial equalities and inequalities in  $\mu$  and  $\tau$  such that there exist vectors  $\zeta$  and  $\xi$  satisfying (3.4.10) if and only if all equalities and inequalities of  $G_{i}$  are satisfied by  $\mu$  and  $\tau$, for at least one  $i=1,\ldots,s$. Since the existence of solutions  $\zeta, \xi$  of (3.4.10) is also equivalent to the inequality  $\mu\geq M(\tau)$, we may assume that  $G_{i}$  is of the form

$$
G _ {i k} (\mu , \tau) \geq 0, \quad k = 1, \dots , k _ {i}.
$$

$\mu = M(\tau)$ must make some of these inequalities to an equality. Let $G(\mu, \tau)$ be the product of all the polynomials $G_{ik}(\mu, \tau)$, which do not vanish identically, and let $H(\mu, \tau)$ be the polynomial with the same irreducible factors as $G(\mu, \tau)$ but all with multiplicity 1. Then we have $H(M(\tau), \tau) = 0$ for every $\tau$. For sufficiently large $\tau$, the degree in $\mu$ of $H(\mu, \tau)$ is independent of $\tau$, and the zeros $\mu_k(\tau)$ are different continuous functions of $\tau$, since $H$ has no multiple factors. Thus the index $k$, such that $M(\tau) = \mu_k(\tau)$, is independent of $\tau$, since $M(\tau)$ is continuous. Hence $M(\tau)$ is an algebraic function of $\tau$ for large $\tau$, and can be developed in a Puiseux series. In virtue of condition I of Theorem 3.3, we have $M(\tau) \to \infty$ with $\tau$. Hence the highest power of $\tau$ in the Puiseux series must be positive, which proves the assertion.$^{2}$

LEMMA 3.10. There exist positive constants $c$ and $d$ such that for sufficiently large $|\xi|$ we have

$$
\left| \zeta - \xi \right| \geq c \left| \xi \right| ^ {d}
$$

for any real $\xi$ and any $\zeta$ with $P(\zeta) = 0$.

PROOF. Choosing the vector $y$ of Lemma 3.9 as $(0, \ldots, 0, 1, 0, \ldots, 0)$, we obtain for large $|\xi_i|$

$$
\left| \zeta - \xi \right| \geq a _ {i} \left| \xi_ {i} \right| ^ {b _ {i}}
$$

where $a_i$ and $b_i$ are positive numbers. Hence, if $c' = \min a_i$ and $d = \min b_i$, we have

$$
\left| \zeta - \xi \right| \geq c ^ {\prime} (\max | \xi_ {i} |) ^ {d} \geq c | \xi | ^ {d}.
$$

LEMMA 3.11. Let $y \in R^{\nu}$ and $\eta \in R_{\nu}$ be two fixed vectors. Then there is a constant $C$ such that

$$
\left| \langle D, \eta \rangle^ {k + j} \left(\frac {1}{P (\xi)}\right) \right| <   \frac {(k + j) ! C ^ {k + j}}{| \xi | ^ {k d} (1 + | \langle y , \xi \rangle |) ^ {b j}}, \quad | \xi | \geq R, \quad j, k = 1, 2, \dots ,\tag{3.4.11}
$$

where $b$ and $d$ are the constants of the two preceding lemmas.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  This result bears some analogy to a lemma in GÄRDING [8].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  The restriction in this theorem that the coefficients must be rational is removed on page 372.</span></small>

PROOF. The quantity, which we shall estimate, is

$$
\langle D, \eta \rangle^ {k + j} \left(\frac {1}{P (\xi)}\right) = i ^ {- (k + j)} \frac {d ^ {k + j}}{d t ^ {k + j}} \left(\frac {1}{P (\xi + t \eta)}\right) _ {t = 0}.
$$

We can write $P(\xi + t\eta) = A \prod_{1}^{m} (t - t_r)$. Since $\zeta = \xi + t_r\eta$ is a zero of $P$ and $\zeta - \xi = t_r\eta$, the numbers $t_r$ can be estimated by either of Lemma 3.9 and Lemma 3.10:

$$
\left| t _ {r} \right| \geq a ^ {\prime} (1 + | \langle y, \xi \rangle |) ^ {b}, \quad \left| t _ {r} \right| \geq c ^ {\prime} | \xi | ^ {d}, \quad (\left| \xi \right| \geq R).\tag{3.4.12}
$$

Now the  $(k+j)^{\mathrm{th}}$  derivative of  $1/P(\xi+t\eta)$  for t=0 is a sum of terms which are each of the form  $A^{-1}$  divided by a product of  $k+j+m$  of the zeros  $t_{r}$ . The number of terms is

$$
m (m + 1) \dots (m + k + j - 1) = (k + j)! \binom {m + k + j - 1} {k + j} <   (k + j)! 2 ^ {m + k + j - 1}.
$$

Furthermore, A is independent of  $\xi$  as will be proved in section 3.8. Hence the lemma follows, if we estimate j of the zeros by the first inequality in (3.4.12), k of them by the second inequality, and the remaining m by a constant.

Let y and  $\eta$  be two fixed vectors, and let b and d be the same numbers as in the previous lemmas. We shall prove that the distribution

$$
F = \langle x, \eta \rangle^ {l} \langle y, D \rangle^ {k} E _ {1}\tag{3.4.13}
$$

is a continuous function, if

$$
l \geq \frac {k}{b} + r,\tag{3.4.14}
$$

where r is the least integer  $>\nu/d$ . This will complete the proof of Theorem 3.4, and estimating the absolute value of F we shall get an interesting refinement of this theorem.

The definition of $F$ means that

$$
F (\check {u}) = (2 \pi) ^ {- \nu / 2} \int_ {| \xi | \geq R} \frac {\langle y , \xi \rangle^ {k}}{P (\xi)} (\langle D, \eta \rangle^ {l} \hat {u} (\xi)) d \xi ,
$$

where D now denotes differentiation with respect to  $\xi$ . Integrating by parts, we obtain  $F(\check{u}) = G(\check{u}) + I(\check{u})$ , where

$$
G (\check {u}) = (2 \pi) ^ {- v / 2} \int_ {| \xi | \geq R} \hat {u} (\xi) \left(\langle - D, \eta \rangle^ {l} \left(\frac {\langle y , \xi \rangle^ {k}}{P (\xi)}\right)\right) d \xi\tag{3.4.15}
$$

and, dS being the vectorial element of area on the sphere  $|\xi|=R$ ,

$$
I (\check {u}) = i ^ {- 1} (2 \pi) ^ {- \nu / 2} \sum_ {j = 0} ^ {l - 1} \int_ {| \xi | = R} \left(\langle - D, \eta \rangle^ {j} \left\{\frac {\langle y , \xi \rangle^ {k}}{P (\xi)} \right\}\right) (\langle D, \eta) ^ {l - 1 - j} \hat {u} (\xi)) \langle d S, \eta \rangle .\tag{3.4.16}
$$

In virtue of Lemma 3.11 we have the following estimate of the integrand in (3.4.15), which we denote by $g(\xi)$,

$$
\begin{array}{l} \left| g (\xi) \right| = \left| \sum_ {j = 0} ^ {k} \binom {l} {j} \frac {k !}{(k - j) !} \langle y, i \eta \rangle^ {j} \langle y, \xi \rangle^ {k - j} \left(\langle - D, \eta \rangle^ {l - j} \frac {1}{P (\xi)}\right) \right| \\ \leqslant \sum_ {j = 0} ^ {k} \binom {l} {j} \frac {k !}{(k - j) !} | \langle y, \eta \rangle | ^ {j} | \langle y, \xi \rangle | ^ {k - j} \frac {(l - j) ! C ^ {l - j}}{| \xi | ^ {r d} (1 + | \langle y , \xi \rangle |) ^ {b (l - j - r)}}. \end{array}
$$

Now it follows from (3.4.14) that

$$
b (l - j - r) - (k - j) = b \left(l - \frac {k}{b} - r\right) + j (1 - b) > 0,
$$

so that we obtain

$$
\left| g (\xi) \right| \leq \left| \xi \right| ^ {- r d} l! \sum_ {j = 0} ^ {k} \binom {k} {j} \left| \langle y, \eta \rangle \right| ^ {j} C ^ {l - j} = \left| \xi \right| ^ {- r d} l! C ^ {l} \left(\left| \langle y, \eta \rangle \right| / C + 1\right) ^ {k}.
$$

The function  $\left|\xi\right|^{-rd}$  is integrable over the domain  $\left|\xi\right|>R$ , since rd>v. Thus the distribution G must equal the continuous function

$$
G (x) = (2 \pi) ^ {- \nu} \int_ {| \xi | \geq R} g (\xi) e ^ {i \langle x, \xi \rangle} d \xi .
$$

With a new constant $C$ we have the estimate

$$
\left| G (x) \right| \leq C ^ {l} l!.\tag{3.4.17}
$$

Using in (3.4.16) the definition of  $\hat{u}$ , we find that the distribution I is defined by the analytic function

$$
I (x) = i ^ {- 1} (2 \pi) ^ {- \nu} \sum_ {j = 0} ^ {l - 1} \int_ {| \xi | = R} \langle x, \eta \rangle^ {l - 1 - j} e ^ {i \langle x, \xi \rangle} \left(\langle - D, \eta \rangle^ {j} \left\{\frac {\langle y , \xi \rangle^ {k}}{P (\xi)} \right\}\right) \langle d S, \eta \rangle .\tag{3.4.18}
$$

The proof is quite parallel to the previous study of the distribution  $E_{2}$ . Since  $1/P(\xi)$  is analytic in a complex neighbourhood of  $|\xi|=R$ , we have

$$
\left| \langle - D, \eta \rangle^ {s} \frac {1}{P (\xi)} \right| \leq s! A ^ {s}, | \xi | = R,
$$

with some constant A. Hence we obtain, when x is in a compact domain K, that, with suitable constants B and C

$$
\begin{array}{l} \left| I (x) \right| \leq \sum_ {j = 0} ^ {l - 1} C ^ {l - 1 - j} \sum_ {s = 0} ^ {\min (k, j)} \binom {j} {s} (j - s)! A ^ {j - s} B ^ {k} k! / (k - s)! \\ \leq \sum_ {j = 0} ^ {l - 1} C ^ {l - 1 - j} j! \sum_ {s = 0} ^ {k} \binom {k} {s} A ^ {j - s} B ^ {k} = \sum_ {j = 0} ^ {l - 1} C ^ {l - 1 - j} j! A ^ {j} (B + A ^ {- 1} B) ^ {k}. \end{array}
$$

Since $k < l$ and $\sum_{0}^{l - 1} j! < (l - 1)! l = l!$, we have with a new constant $C$.

$$
\left| I (x) \right| \leq C ^ {l} l!.\tag{3.4.19}
$$

Now  $F = G + I$ , so that we have proved that the distribution F, defined by (3.4.13), is a continuous function, if (3.4.14) is valid. We have also proved that the absolute value of F has an estimate of the form (3.4.17), (3.4.19), when x is in a compact set K. If we now choose l as the smallest integer such that (3.4.14) is valid, and recall that  $E(x) = E_{1}(x) + E_{2}(x)$ , where  $E_{2}(x)$  is an entire analytic function, the following theorem is proved.

THEOREM 3.5. Let y be a vector in  $R^{v}$  and b the number introduced in Lemma 3.9. Then, for any compact set K, which does not contain the origin, there exists a constant C such that

$$
\left| \langle y, D \rangle^ {k} E (x) \right| \leq C ^ {k} \Gamma \left(\frac {k}{b}\right), x \in K,\tag{3.4.20}
$$

where  $E(x)$  is the function which defines the fundamental solution of Theorem 3.4.

In constructing the fundamental solution we have used several ideas from the literature. The idea of estimating an expression of the form (3.4.13) has been taken over from a study of elliptic operators by Gårding [10]. For references to the very rich older literature on this subject, the reader should consult Schwartz [28].

## 3.5. Proof of Theorem 3.3

Let $P$ be complete and satisfy the conditions I–V of Theorem 3.3, and let $\Omega$ and $\Omega'$ be any domains such that $\Omega'$ has compact closure in $\Omega$. The domain $\Omega$ may be bounded or not be bounded. Then there exists a positive number $\varepsilon$ such that a sphere with radius $\varepsilon$ and centre at any point in $\Omega'$ is contained in $\Omega$. Let $\varrho(x)$ be a function in $C_0^\infty$, which vanishes for $|x| \geq \varepsilon$ and equals 1 in a neighbourhood of the origin. Instead of the fundamental solution constructed in Theorem 3.4, we shall use the “parametrix”

$$
\boldsymbol {F} = \varrho \boldsymbol {E}.\tag{3.5.1}
$$

The support of $F$ is contained in the sphere $|x| \leq \varepsilon$, and

$$
P (D) F = \delta_ {0} + \omega (x),\tag{3.5.2}
$$

where $\delta_0$ is the Dirac measure at the origin and $\omega(x)$ is an infinitely differentiable function, which vanishes for $|x| \geq \varepsilon$ and also in a neighbourhood of the origin. In fact, in a neighbourhood of the origin, where $\varrho = 1$, we have $F = E$ and thus $P(D)F = P(D)E = \delta_0$. Since $P(D)E$ is infinitely differentiable for $x \neq 0$, the formula (3.5.2) follows.

Now let $u \in \mathcal{D}_p$, which means that $u$ and $P(D)u$ are square integrable functions in the sense of the theory of distributions. In $\Omega'$ we have

$$
u = u * \delta_ {0} = u * (P (D) F - \omega) = F * (P (D) u) - \omega * u\tag{3.5.3}
$$

and consequently

$$
P ^ {(\alpha)} (D) u = \left(P ^ {(\alpha)} (D) F\right) * (P u) - \left(P ^ {(\alpha)} (D) \omega\right) * u.\tag{3.5.4}
$$

Since  $P^{(\alpha)}(D)\omega$  is continuous, the last term is bounded and hence square integrable in  $\Omega'$ . To study the other term in (3.5.4), we denote by  $\varphi$  the function which equals Pu in points with distance  $<\varepsilon$  to  $\Omega'$  and equals 0 elsewhere.  $\varphi$  is square integrable and has compact support. In  $\Omega'$  we have

$$
(P ^ {(\alpha)} (D) F) * (P u) = (P ^ {(\alpha)} (D) F) * \varphi = (P ^ {(\alpha)} (D) E) * \varphi + (P ^ {(\alpha)} (D) \{(\varrho - 1) E \}) * \varphi .
$$

Now $P^{(\alpha)}(D)E*\varphi$ is a square integrable function in $\Omega'$ in virtue of the assertion II of Theorem 3.4. Since $(\varrho -1)E$ is an infinitely differentiable function and $\varphi$ has compact support, it follows in particular that also $(P^{(\alpha)}(D)\{(\varrho -1)E\})*\varphi$ is square integrable in $\Omega'$. Hence $P^{(\alpha)}(D)u$ is locally square integrable in $\Omega$, for any $u\in D_p$, and thus the remarks following Definition 3.1 show that the operator $P$ is of local type.

We may also note that (3.5.3) shows that all distributions u, such that  $P(D)u=0$ , are infinitely differentiable functions. We shall refine this result in the next section.

## 3.6. The differentiability of the solutions of a complete operator of local type

We observed at the end of the previous section that all solutions of the equation Pu=0, where P is complete and of local type, are infinitely differentiable. More generally we can prove:

THEOREM 3.6. If u belongs to the domain of the operator  $P^{k}$  for every k, where P is a complete differential operator of local type, it follows that u is an infinitely differentiable function after correction on a null set.

PROOF. It follows from Theorem 3.3 (or else directly from Definition 3.1) that $P^k$ is also complete and of local type. Hence, if $\psi \in C_0^\infty(\Omega)$, the function $\psi u$ is in the minimal domain of $P(D)^k$ in any bounded domain $\Omega'$, containing the support of $\psi$. Thus $\psi u$ equals an infinitely differentiable function in virtue of Theorem 2.14. Since $\psi$ is an arbitrary function in $C_0^\infty$, we obtain the desired result.

The proof of Theorem 2.14 also gives the following more precise result: For any differential operator  $Q(D)$  there exists an integer k such that, if  $\Omega$  is a bounded domain, we have with some constant C

$$
\sup _ {x \in \Omega} | Q (D) u (x) | ^ {2} \leq C (\| (P ^ {k}) _ {0} u \| ^ {2} + \| u \| ^ {2}),
$$

when u is in the minimal domain of  $P(D)^{k}$ . Using this result and the proof of Theorem 3.6, we obtain the following useful estimate.

LEMMA 3.12. Let $P$ be complete and of local type, and let $Q$ be any differential operator with constant coefficients. Then there exists an integer $k$ with the following property: If $u \in \mathcal{D}_{P^k}$, the function $Q(D)u$ is continuous in $\Omega$, and for any domain $\Omega'$ with compact closure in $\Omega$ there is a constant $C$ such that

$$
\sup _ {x \in \Omega^ {\prime}} | Q (D) u (x) | ^ {2} \leq C (\| P ^ {k} u \| ^ {2} + \| u \| ^ {2}).\tag{3.6.1}
$$

THEOREM 3.7. Let $\Omega$ be a bounded domain. If all the solutions $u \in L^2(\Omega)$ of the equation $Pu = 0$ are infinitely differentiable after correction on a null set, the operator $P(D)$ must be complete and of local type.

PROOF. We shall prove that the first condition in Theorem 3.3 is fulfilled. This can be done my means of explicit constructions similar to those of Petrowsky [26]. However, we give a proof along the lines of this paper. Thus let $\Omega'$ be a domain with compact closure in $\Omega$. Since $P$ is a closed operator, the set $U$ of all solutions $u$ of the equation $Pu = 0$ is a closed subspace of $L^2(\Omega)$. The mapping

$$
U \ni u \rightarrow \partial u / \partial x ^ {k} \in L ^ {2} (\Omega^ {\prime})
$$

is closed, and by assumption it is defined in the whole of U. Hence it is continuous in virtue of the theorem on the closed graph, so that

$$
\int_ {\Omega^ {\prime}} \sum_ {k = 1} ^ {v} \left| \frac {\partial u}{\partial x ^ {k}} \right| ^ {2} d x \leq C \int_ {\Omega} | u | ^ {2} d x, u \in U.
$$

If we apply this inequality to the function $u = e^{i\langle x,\xi \rangle}$, where $\zeta = \xi + i\eta$ is a solution of the equation $P(\zeta) = 0$, we obtain

$$
\left(\sum_ {k = 1} ^ {v} \mid \zeta_ {k} \mid^ {2}\right) \int_ {\Omega^ {\prime}} e ^ {- 2 \langle x, \eta \rangle} d x \leq C \int_ {\Omega} e ^ {- 2 \langle x, \eta \rangle} d x.
$$

Hence when  $\eta$  is bounded,  $|\eta|<A$ , it follows that  $|\zeta|<C'$ , which proves that P is complete and satisfies the condition I of Theorem 3.3.

Theorems 3.6 and 3.7 show that all solutions of the equation Pu=0 are infinitely differentiable functions if and only if P is complete and of local type. Thus we have found the greatest class of operators, for which a generalization of Weyl's lemma holds true. We now turn to a more detailed study of the properties of the solutions of the equation Pu=0.

DEFINITION 3.2. An infinitely differentiable function u, defined in a domain  $\Omega$ , is said to be of class  $\varrho$  in the direction y, if to any compact set K in  $\Omega$  there is a constant C, so that

$$
\sup _ {x \in K} | \langle y, D \rangle^ {n} u (x) | <   C ^ {n} \Gamma (\varrho n).\tag{3.6.2}
$$

It is well known that solutions of elliptic equations are analytic and consequently of class 1 in every direction. There is also a classical result by Holmgren, which states that the solutions of the equation of heat are of class 2 in the time variable. We now state a result of this type for any equation of local type.

THEOREM 3.8. Let $P(D)$ be complete and of local type. Then every solution of the equation $Pu = 0$ is of class $\varrho(y)$ in the direction $y$, $y \neq 0$, if $\varrho(y)$ is the inverse of the exponent $b$ in Lemma 3.9, that is

$$
\varrho (y) = \overline {{\lim _ {| \langle y , \xi \rangle | \rightarrow \infty}}} \left(\sup _ {P (\zeta) = 0} \frac {\log | \langle y , \xi \rangle |}{\log | \zeta - \xi |}\right).\tag{3.6.3}
$$

PROOF. Let K be a compact set in  $\Omega$ , and take a function  $\psi\in C_{0}^{\infty}\left(\Omega\right)$ , which equals 1 in a neighbourhood of K. The function  $v=\psi u$  is then in  $C_{0}^{\infty}\left(\Omega\right)$  and equals u in K. Furthermore, the function  $\varphi=P(D)v\in C_{0}^{\infty}\left(\Omega\right)$  and vanishes in a neighbourhood of K. Denoting by E the fundamental solution given by Theorem 3.4, we have  $v=E*\varphi$  in virtue of (3.4.1). Hence

(3.6.4)

$$
u (x) = \int E (x ^ {\prime}) \varphi (x - x ^ {\prime}) d x ^ {\prime}, x \in K,\tag{3.6.5}
$$

$$
\langle y, D \rangle^ {n} u (x) = \int \left(\langle y, D ^ {\prime} \rangle^ {n} E \left(x ^ {\prime}\right)\right) \varphi \left(x - x ^ {\prime}\right) d x ^ {\prime}, x \in K,
$$

where  $D'$  is the operator of differentiating with respect to  $x'$ . Now we can find two positive numbers  $\varepsilon$  and A such that  $\varphi(x)=0$  in any point x with distance  $<\varepsilon$  or

$>A$ from a point in $K$. Then $\varphi(x-x')=0$ if $x\in K$ and either $|x'|<\varepsilon$ or $|x'|>A$. Hence we may integrate only over the domain $\varepsilon\leq|x'|\leq A$ in (3.6.4) and (3.6.5). In this domain we can use Theorem 3.5, which gives

$$
\left| \langle y, D \rangle^ {n} u (x) \right| \leq \Gamma \left(\frac {n}{b}\right) C ^ {n} \int | \varphi (x - x ^ {\prime}) | d x ^ {\prime} = \Gamma (\varrho n) C ^ {n} \int | \varphi (x) | d x.
$$

The proof is complete.

An interesting application of Theorem 3.8 concerns the growth of null solutions of $P$. Suppose that $u$ is a null solution in $\Omega$, so that it vanishes when $x \in \Omega$ and $\langle x, \xi \rangle < 0$, where $\langle x, \xi \rangle = 0$ is a characteristic plane intersecting $\Omega$. Let $y$ be a direction which is not contained in this plane, that is, such that $\langle y, \xi \rangle \neq 0$. Then, if $K$ is a compact set in $\Omega$, we have

$$
\left| u (x) \right| \leq A e ^ {- c \langle x, \xi \rangle^ {- \alpha}}, \quad x \in K, \quad \langle x, \xi \rangle > 0,\tag{3.6.6}
$$

where $\alpha$ is defined by $\alpha^{-1} = \varrho(y) - 1$. For in virtue of Theorem 3.8 and Taylor's formula we have for any $n$, if $t = \langle x, \xi \rangle$,

$$
\left| u (x) \right| \leq \frac {C ^ {n} t ^ {n}}{n !} \Gamma (\varrho n), x \in K.\tag{3.6.7}
$$

If in (3.6.7) we let $n$ be the smallest integer larger than $(Ct)^{-\alpha}$ and use Stirling's formula, we obtain the desired estimate (3.6.6).

REMARK. We pointed out at the end of section 3.5, that all distributions $u$, which solve the equation $Pu = 0$, are infinitely differentiable functions, if $P$ is complete and of local type. Using our Theorem 3.6 and Théorème XXI in Schwartz [28], Chap. VI, we can also prove that a distribution $u$, such that $P(D)^n u$ is of bounded order when $n \to \infty$, is an infinitely differentiable function.

## 3.7. Spectral theory of complete self-adjoint operators of local type

We shall call the differential operator  $P(D)$  (formally) self-adjoint, if  $P(D)$  coincides with its algebraic adjoint, that is, if  $P(\xi)$  is real for real  $\xi$ .

LEMMA 3.13. If $P(D)$ is complete, formally self-adjoint and of local type, it follows that the operator $P_0$ is semi-bounded for an arbitrary domain $\Omega$, unless $P(D)$ is an ordinary differential operator of odd order.

PROOF. First suppose that  $P(D)$  is not ordinary, that is, that the dimension  $\nu$  of the space of  $\xi$  is greater than 1. From condition V of Theorem 3.3 it follows that  $|P(\xi)|\to\infty$  when the real vector  $\xi\to\infty$ . If there were points where  $P(\xi)$  is positive

and points where $P(\xi)$ is negative outside any sphere, there would also be points where $P(\xi) = 0$, since the complement of a sphere is connected. Now this is a contradiction, so that either $P(\xi) \to +\infty$ or else $P(\xi) \to -\infty$ when $\xi \to \infty$. We may restrict ourselves to the first case. Then $P(\xi) \geq c$ for some finite real $c$. If $u \in C_0^\infty(\Omega)$, we have in virtue of Parseval's formula

$$
(P (D) u, u) = \int P (\xi) | \hat {u} (\xi) | ^ {2} d \xi \geq c \int | \hat {u} (\xi) | ^ {2} d \xi = c (u, u).
$$

Hence $(P_0u, u) \geq c(u, u)$ when $u \in \mathcal{D}_{P_0}$. The same result is obviously valid, if $P(D)$ is an ordinary differential operator of even order.

Thus, if $P(D)$ is complete, formally self-adjoint and of local type but not an ordinary differential operator of odd order, the operator $P_0$ is symmetric and semi-bounded. Hence there exist self-adjoint semi-bounded extensions $\hat{P}$ of $P_0$ (see Nagy [23] or Krein [17], who gives a more detailed study). If $\hat{P}$ is any self-adjoint extension, we have $P_0 \subset \hat{P}$ and consequently $\hat{P} = \hat{P}^* \subset P_0^* = P$, so that $P_0 \subset \hat{P} \subset P$. Thus $\hat{P}$ is defined by a boundary problem in the sense of section 1.3. The case where $\hat{P}$ is the Friedrichs extension merits some comment. The degree of $P(\xi + t\mathbf{N})$ in $t$ for fixed $\mathbf{N} \in R_{\nu}$ and indeterminate $\xi$ is even, since $P(\xi)$ is semi-bounded. Denote this degree by $2m(\mathbf{N})$. Using the methods of section 2.8 we could show that the boundary conditions corresponding to $\hat{P}$ are, at least formally, the vanishing of $m(\mathbf{N}) - 1$ transversal derivatives at a point on the boundary with normal $\mathbf{N}$.

For ordinary differential operators P of odd order, the situation is different. In fact, when  $\Omega$  is a semi-axis, there are no self-adjoint extensions. These exceptional operators, which can be treated explicitly, will therefore be excluded in the sequel.

Thus for the rest of the section we assume that  $P(D)$  is complete, formally self-adjoint and of local type, but not an ordinary differential operator of odd order. Let  $\hat{P}$  be a fixed self-adjoint extension of  $P_{0}$ . The operator  $\hat{P}$  gives rise to a resolution of the identity  $E_{\lambda}$  such that

$$
\hat {P} = \int \lambda d E _ {\lambda}.\tag{3.7.1}
$$

We shall study certain functions of the operator $\hat{P}$, which will turn out to be integral operators. Let $\mathcal{B}_{\infty}$ be the set of all Borel measurable functions $\alpha(\lambda)$, $-\infty < \lambda < \infty$, such that the product $\alpha(\lambda)\lambda^{k}$ is bounded for every integer $k \geq 0$. The supremum of $|\alpha(\lambda)|$ is denoted by $|\alpha|$. Now form the operator

$$
\alpha (\hat {P}) = \int \alpha (\lambda) d E _ {\lambda}, \quad \alpha \in \mathcal {B} _ {\infty}.\tag{3.7.2}
$$

Since

$$
\hat {P} ^ {k} \propto (\hat {P}) = \int \lambda^ {k} \propto (\lambda) d E _ {\lambda},
$$

the operator $\hat{P}^k\propto (\hat{P})$ is bounded for every integer $k$;

$$
\left\| \hat {P} ^ {k} \alpha (\hat {P}) \right\| \leq \left| \lambda^ {k} \alpha \right|, k = 0, 1, 2, \dots\tag{3.7.3}
$$

Here $\lambda^k\alpha$ denotes the function $\lambda^k\alpha (\lambda)$, and $\| \cdot \|$ is the operator norm. Thus, if $g = \alpha (\hat{P})f$, it follows that $g\in \mathcal{D}_{\hat{P}^k}$ for any integer $k$, so that $g$ is an infinitely differentiable function in virtue of Theorem 3.6. Since

$$
\left\| \hat {P} ^ {k} g \right\| \leq \left| \lambda^ {k} \alpha \right| \| f \|,
$$

the second part of the following lemma also follows as a corollary of Lemma 3.12.

LEMMA 3.14. All functions in the range of $\alpha(\hat{P})$ are infinitely differentiable, if $\alpha\in\mathcal{B}_{\infty}$. Moreover, for any differential operator $Q(D)$ we have, when $K$ is a compact subset of $\Omega$,

$$
\sup _ {x \in K} | Q (D) (\alpha (\hat {P}) f (x)) | ^ {2} \leq C (| \alpha | ^ {2} + | \lambda^ {k} \alpha | ^ {2}) \| f \| ^ {2}.
$$

Here k is the same integer as in Lemma 3.12, and C is a constant, which may depend on K.

Applying this result to the operators $Q(D) = 1$ and $Q(D) = D_i$, we find that, for a certain integer $\varkappa$,

$$
\sup _ {x \in K} \left(\left| g (x) \right| ^ {2} + \sum_ {i = 1} ^ {\nu} \left| \partial g / \partial x ^ {i} \right| ^ {2}\right) \leq C ^ {2} \left(\left| \alpha \right| ^ {2} + \left| \lambda^ {\kappa} \alpha \right| ^ {2}\right) \| f \| ^ {2},\tag{3.7.4}
$$

where $g = \alpha(\hat{P})f$, and $K$ is a compact subset of $\Omega$. Hence the value $g(x)$ at a fixed point is a bounded linear functional of $f \in L^2$, so that we may write

$$
\alpha (\hat {P}) f (x) = (f, \varphi_ {x, \alpha}),\tag{3.7.5}
$$

where $\varphi_{x,\alpha}\in L^{2}$. In virtue of (3.7.4) we have, if $K$ is a compact set in $\Omega$,

$$
\left\| \varphi_ {x, \alpha} \right\| ^ {2} \leq C (\left| \alpha \right| ^ {2} + \left| \lambda^ {\varkappa} \alpha \right| ^ {2}), x \in K.\tag{3.7.6}
$$

Furthermore, if $K$ is also convex, it follows from (3.7.4) that

$$
\begin{array}{r l} \big | (f, (\varphi_ {x, \alpha} - \varphi_ {y, \alpha})) \big | ^ {2} & = \big | g (x) - g (y) \big | ^ {2} \leq \big | x - y \big | ^ {2} \sup _ {x ^ {\prime} \in K} \sum_ {1} ^ {\nu} \big | \partial g / \partial x ^ {\prime i} \big | ^ {2} \\ & \leq \big | x - y \big | ^ {2} C ^ {2} (\big | \alpha \big | ^ {2} + \big | \lambda^ {\kappa} \alpha \big | ^ {2}) \| f \| ^ {2}. \end{array}
$$

Hence we have

$$
\left\| \varphi_ {x, \alpha} - \varphi_ {y, \alpha} \right\| ^ {2} \leq | x - y | ^ {2} C ^ {2} (| \alpha | ^ {2} + | \lambda^ {\kappa} \alpha | ^ {2}).\tag{3.7.7}
$$

If $f \in \mathcal{D}_{\hat{P}^k}$, we can write $(\hat{P}^k \propto (\hat{P}))f(x) = \alpha(\hat{P})(\hat{P}^k f)(x)$, which with the notation (3.7.5) reduces to

$$
(f, \varphi_ {x, \lambda^ {k} \alpha}) = (\hat {P} ^ {k} f, \varphi_ {x, \alpha}), \quad f \in \mathcal {D} _ {\hat {P} ^ {k}}.
$$

Thus $\varphi_{x,\alpha} \in \mathcal{D}_{\hat{P}^k}$ and $\hat{P}^k \varphi_{x,\alpha} = \varphi_{x,\lambda^k\alpha}$, for any integer $k$. Hence it follows from Theorem 3.6 that $\varphi_{x,\alpha}$ is an infinitely differentiable function $\varphi_{x,\alpha}(x')$, $x' \in \Omega$, and if $K'$ is a compact set in $\Omega$, Lemma 3.12 shows that

$$
\left| \varphi_ {x, \alpha} \left(x ^ {\prime}\right) \right| ^ {2} + \sum_ {i = 1} ^ {v} \left| \partial \varphi_ {x, \alpha} \left(x ^ {\prime}\right) / \partial x ^ {\prime i} \right| ^ {2} \leq C ^ {2} \left(\left\| \varphi_ {x, \alpha} \right\| ^ {2} + \left\| \varphi_ {x, \lambda^ {*} \alpha} \right\| ^ {2}\right), \quad x ^ {\prime} \in K ^ {\prime}.
$$

Estimating the right-hand side of this inequality by means of (3.7.6), we thus obtain

$$
\left| \varphi_ {x, \alpha} \left(x ^ {\prime}\right) \right| ^ {2} + \sum_ {i = 1} ^ {\nu} \left| \partial \varphi_ {x, \alpha} \left(x ^ {\prime}\right) / \partial x ^ {\prime i} \right| ^ {2} \leq C ^ {2} \left(\left| \alpha \right| ^ {2} + \left| \lambda^ {2 \kappa} \alpha \right| ^ {2}\right), \quad x \in K, x ^ {\prime} \in K ^ {\prime}.\tag{3.7.8}
$$

Now set $\Theta(x', x, \alpha) = \overline{\varphi_{x,\alpha}(x')}$. In virtue of the definition (3.7.5) of $\varphi_{x,\alpha}$ we have

$$
\alpha (\hat {P}) f (x) = \int_ {\Omega} \Theta (x ^ {\prime}, x, \alpha) f (x ^ {\prime}) d x ^ {\prime}.\tag{3.7.9}
$$

We shall prove that $\Theta(x', x, \alpha)$ is a continuous function of $(x', x) \in \Omega \times \Omega$. Let $x_0$ and $x_0'$ be fixed points in $\Omega$ and take compact neighbourhoods $K$ and $K'$ of $x_0$ and $x_0'$. From (3.7.8) it follows that, for given $\varepsilon$, there exists an open neighbourhood $U' \subset K'$ such that

$$
\left| \Theta (x ^ {\prime}, x, \alpha) - \Theta (y ^ {\prime}, x, \alpha) \right| <   \varepsilon ,
$$

if $x \in K$ and $x', y' \in U'$. Furthermore, (3.7.7) shows that

$$
\int_ {U ^ {\prime}} \left| \Theta \left(x ^ {\prime}, x, \alpha\right) - \Theta \left(x ^ {\prime}, x _ {0}, \alpha\right) \right| ^ {2} d x ^ {\prime} <   \varepsilon^ {2} m U ^ {\prime},
$$

when $x$ is in a neighbourhood $U$ of $x_0$. Thus, if $x \in U$, there exists a point $y' \in U'$ so that $|\Theta(y', x, \alpha) - \Theta(y', x_0, \alpha)| < \varepsilon$. We also have

$$
\left| \Theta \left(x ^ {\prime}, x, \alpha\right) - \Theta \left(y ^ {\prime}, x, \alpha\right) \right| <   \varepsilon , \text {   if   } x ^ {\prime} \in U ^ {\prime}, \text {   and   } \left| \Theta \left(y ^ {\prime}, x _ {0}, \alpha\right) - \Theta \left(x _ {0} ^ {\prime}, x _ {0}, \alpha\right) \right| <   \varepsilon .
$$

Hence, if $(x', x) \in U' \times U$, we have

$$
\left| \Theta (x ^ {\prime}, x, \alpha) - \Theta (x _ {0} ^ {\prime}, x _ {0}, \alpha) \right| <   3 \varepsilon ,
$$

which proves the continuity of $\Theta(x', x, \alpha)$.

Let $\mathcal{B}_k$ be the set of bounded Borel functions $\alpha (\lambda)$ such that $|\lambda^k\alpha | < \infty$. Noting that we have only used the fact that $|\lambda^{2\times}\alpha| < \infty$, in constructing the function $\Theta (x', x, \alpha)$ and proving its continuity, we obtain the following theorem.

THEOREM 3.9. There exists an integer $k$ such that $\alpha(\hat{P})$ is an integral operator with a continuous Carleman kernel, if $\alpha \in \mathcal{B}_k$. Thus the kernel $\Theta(x', x, \alpha)$ in (3.7.9) is a continuous function of $(x', x) \in \Omega \times \Omega$, and the integrals

$$
\int_ {\Omega} \left| \Theta (x ^ {\prime}, x, \alpha) \right| ^ {2} d x, \quad \int_ {\Omega} \left| \Theta (x ^ {\prime}, x, \alpha) \right| ^ {2} d x ^ {\prime}\tag{3.7.10}
$$

exist and are continuous functions of $x'$ and $x$, respectively. For compact subsets $K$ of $\Omega$ we have

$$
\left| \Theta \left(x ^ {\prime}, x, \alpha\right) \right| \leq C \left(\left| \alpha \right| + \left| \lambda^ {k} \alpha \right|\right), \quad x, x ^ {\prime} \in K, \alpha \in \mathcal {B} _ {k}.\tag{3.7.11}
$$

PROOF. With $k = 2\pi$ we have proved that $\Theta(x', x, \alpha)$ is continuous and that (3.7.11) is valid. Since, with our previous notations, the second integral in (3.7.10) is $\| \varphi_{x,\alpha} \|^2$, it is finite and continuous in virtue of (3.7.6) and (3.7.7). Now we have

$$
\Theta (x ^ {\prime}, x, \alpha) = \overline {{\Theta}} (x, x ^ {\prime}, \bar {\alpha}),\tag{3.7.12}
$$

which proves the existence and continuity of the first integral (3.7.10).

We now return to the original assumption that $\alpha \in \mathcal{B}_{\infty}$. Let $J$ be the anti-linear operator $f \to \hat{f}$ in $L^2$, and set $\hat{P}' = J^{-1} \hat{P} J$. This means that $\hat{P}' f = \overline{\hat{P} \hat{f}}$, if $\hat{f} \in \mathcal{D}_{\hat{P}}$. We obviously have

$$
P _ {0} ^ {\prime} \subset \hat {P} ^ {\prime} \subset P ^ {\prime},
$$

where  $P_{0}^{\prime}$  and  $P^{\prime}$  are the minimal and maximal differential operators defined by  $P^{\prime}(D)=P(-D)$ . The relation  $\hat{P}\varphi_{x,\alpha}=\varphi_{x,\lambda\alpha}$ , which was proved above, now gives

$$
\hat {P} ^ {\prime} \Theta (x ^ {\prime}, x, \alpha) = \Theta (x ^ {\prime}, x, \lambda \alpha),\tag{3.7.13}
$$

since $\Theta(x', x, \alpha) = \overline{\varphi_{x,\alpha}(x')}$. Here $\hat{P'}$ operates on the variable $x'$. Using (3.7.12) we also find that

$$
\hat {P} \Theta (x ^ {\prime}, x, \alpha) = \Theta (x ^ {\prime}, x, \lambda \alpha),\tag{3.7.14}
$$

where $\hat{P}$ operates on $x$. From the last two formulas we obtain for any $n$

$$
(P (D) + P (- D ^ {\prime})) ^ {n} \Theta (x ^ {\prime}, x, \alpha) = 2 ^ {n} \Theta (x ^ {\prime}, x, \lambda^ {n} \alpha)
$$

in the distribution sense. Here $P(D)$ operates on $x$ and $P(-D')$ operates on $x'$. Now it follows from condition III of Theorem 3.3 (see also the next section) that the complete operator $P(D) + P(-D')$ is of local type in $\Omega \times \Omega$. If $\Omega'$ is a domain with compact closure in $\Omega$, the functions $\Theta(x', x, \lambda^n \alpha)$ are square integrable in $\Omega' \times \Omega'$. Hence Theorem 3.6 proves that $\Theta(x', x, \alpha)$ is infinitely differentiable in $\Omega' \times \Omega'$ and consequently in $\Omega \times \Omega$.

If $f \in C_0^\infty(\Omega)$, we find by differentiating (3.7.9) that

$$
Q (D) \alpha (\hat {P}) f (x) = \int_ {\Omega} (Q (D) \Theta (x ^ {\prime}, x, \alpha)) f (x ^ {\prime}) d x ^ {\prime},
$$

where  $Q(D)$  is a differential operator with constant coefficients. Hence the integral

$$
\int_ {\Omega} \left| Q (D) \Theta (x ^ {\prime}, x, \alpha) \right| ^ {2} d x ^ {\prime}
$$

is bounded on compact subsets of  $\Omega$ , in virtue of Lemma 3.14. Since the same result is valid for the operators  $D_{i}Q(D)$ , the integral is in fact continuous. Summing up, we have now proved the following theorem.

THEOREM 3.10. The kernel $\Theta(x', x, \alpha)$ of $\alpha(\hat{P})$ is infinitely differentiable, if $\alpha \in \mathcal{B}_{\infty}$. Furthermore, the integrals

$$
\int_ {\Omega} \left| Q (D) \Theta (x ^ {\prime}, x, \alpha) \right| ^ {2} d x ^ {\prime}, \quad \int_ {\Omega} \left| Q (D ^ {\prime}) \Theta (x ^ {\prime}, x, \alpha) \right| ^ {2} d x\tag{3.7.15}
$$

exist and are continuous functions of  $x \in \Omega$  and  $x' \in \Omega'$ , respectively, if  $Q(D)$  is any differential operator with constant coefficients.

For self-adjoint elliptic operators with variable coefficients, Theorem 3.9 and essentially also Theorem 3.10 were proved by Browder [2, 3] and Gårding [11, 12] in studying singular eigenfunction expansions. Our statements follow Gårding's closely. Gårding [12] proved the existence of an eigenfunction expansion for any self-adjoint operator $\hat{P}$, such that a function $\alpha(\hat{P})$, where $\alpha(\lambda) \neq 0$ a.e., is a Carleman integral operator. Hence his results apply to our case in virtue of Theorem 3.9. The precise statement may be omitted, since it does not differ in any respect from the results for elliptic operators in Browder [2] and Gårding [11, 12].

## 3.8. Examples of operators of local type

Elliptic operators are of local type, for it is easily seen that they satisfy condition III of Theorem 3.3. Since most of our results are not new for elliptic operators, we wish to give other examples. For convenience we shall say that a polynomial $P(\xi)$ is of local type, if the operator $P(D)$ is of local type, that is, if $P(\xi)$ satisfies conditions I–V of Theorem 3.3. We first prove some necessary conditions for an operator to be of local type.

Let $\eta$ be a fixed real vector and set

$$
P (\xi + t \eta) = \sum t ^ {k} P _ {k} (\xi , \eta).\tag{3.8.1}
$$

Denote by $\mu$ the degree in $t$ of $P(\xi + t\eta)$ for fixed $\eta$ and indeterminate $\xi$. We shall prove that $P_{\mu}(\xi, \eta)$ must then be independent of $\xi$, if $P$ is of local type and $\mu > 0$, that is, if $\eta \notin \Lambda(P)$. In fact, if this were not true, we should have for some real $\xi$ and some sequence $\alpha$ of indices with $|\alpha| \neq 0$

$$
\frac {\partial^ {| \alpha |} P _ {\mu} (\xi , \eta)}{\partial \xi_ {\alpha}} \neq 0.
$$

Then we should get when $t \to \infty$

$$
\frac {P ^ {(\alpha)} (\xi + t \eta)}{P (\xi + t \eta)} \rightarrow \frac {P _ {\mu} ^ {(\alpha)} (\xi , \eta)}{P _ {\mu} (\xi , \eta)} \neq 0,
$$

which would contradict condition III of Theorem 3.3. Hence our assertion follows.

Let $p(\xi)$ be the principal part of $P(\xi)$. Denote its order by m, and form with fixed $\eta$ the expansion

$$
p (\xi + t \eta) = \sum_ {0} ^ {m} t ^ {k} p _ {k} (\xi , \eta).\tag{3.8.2}
$$

We have evidently  $p_{m}(\xi, \eta) = p(\eta)$ . The polynomial  $p_{k}(\xi, \eta)$  either vanishes for all  $\xi$ , or else it is a homogeneous polynomial of degree m - k in  $\xi$ .

Now take a real vector $\eta \notin \Lambda(P)$ such that $p(\eta)=0$. Then the degree $\mu$ of $P(\xi+t\eta)$ in $t$ is less than $m$, and the degree of $p(\xi+t\eta)$ in $t$ cannot be greater than $\mu$. Since we have proved that the polynomial $P_{\mu}(\xi,\eta)$ must be independent of $\xi$, and we have $P_{\mu}(\xi,\eta)=p_{\mu}(\xi,\eta)+$ terms of degree less than $m-\mu$ in $\xi$, it follows that $p_{\mu}(\xi,\eta)=0$ for all $\xi$, so that the degree of $p(\xi+t\eta)$ in $t$ is less than $\mu$. Thus, if $P$ is of local type, the polynomial $p(\xi+t\eta)$ is at most of degree $m-2$ in $t$, if $p(\eta)=0$.

If  $P(\xi)$  is real, we can improve this result. For we may suppose that  $P(\xi)$  is not a polynomial in one variable only. Then the polynomial  $P(\xi)$  is semi-bounded (Lemma 3.13), and consequently its degree m and the degrees of  $P(\xi + t\eta)$  and  $p(\xi + t\eta)$  in t must be even. Hence  $\mu \leq m - 2$ , so that the degree of  $p(\xi + t\eta)$  in t is at most m - 4, if  $p(\eta) = 0$ .

From these results it follows that an operator of principal type can only be of local type, if it is elliptic. We also conclude that a homogeneous complete operator of local type must be elliptic. Finally, the results suggest the examples of self-adjoint operators of local type, which we shall now give.

THEOREM 3.11. Let $Q(\xi)$ be any real polynomial of order $m$, and let $k$ be a fixed integer $\geq 2$. Then the polynomial

$$
P (\xi) = Q (\xi) ^ {2 k} + R (\xi)\tag{3.8.3}
$$

is of local type, if $R(\xi)$ is a positive definite homogeneous polynomial of the order $2km - 2(k - 1)$.

In fact, the same result remains true, if  $R(\xi)$  is an inhomogeneous polynomial of this degree and, denoting the principal parts of Q and R by q and r, we have  $r(\xi) > 0$  for every  $\xi \neq 0$  such that  $q(\xi) = 0$ . Note that the principal part of the polynomial  $P(\xi)$  is  $q(\xi)^{2k}$ , and that  $q(\xi)$  is an arbitrary real homogeneous polynomial.

PROOF. We shall prove that condition III of Theorem 3.3 is fulfilled. Writing $Q(\xi)^{2k} = S(\xi)$, we have $P^{(\alpha)}(\xi) = S^{(\alpha)}(\xi) + R^{(\alpha)}(\xi)$, and since

$$
\frac {\left| R ^ {(\alpha)} (\xi) \right|}{P (\xi)} \leq \frac {\left| R ^ {(\alpha)} (\xi) \right|}{R (\xi)} \rightarrow 0, \text {   when   } \xi \rightarrow \infty , | \alpha | \neq 0,
$$

the only difficulty is to estimate  $S^{(\alpha)}$ . Now we can write

$$
S ^ {(\alpha)} (\xi) = \sum_ {j = 1} ^ {\min (2 k, | \alpha |)} Q (\xi) ^ {2 k - j} F _ {j} ^ {\alpha} (\xi),\tag{3.8.4}
$$

where  $F_{j}^{\alpha}(\xi)$  is a polynomial of degree  $jm-|\alpha|$  at most. In virtue of the inequality between geometric and arithmetic means we have

$$
\left| Q (\xi) \right| ^ {2 k - j} R (\xi) ^ {j / 2 k} \leq Q (\xi) ^ {2 k} + R (\xi) = P (\xi).\tag{3.8.5}
$$

Hence we obtain the following estimates for the terms in (3.8.4)

$$
\left| Q (\xi) ^ {2 k - j} F _ {j} ^ {\alpha} (\xi) \right| \leq C P (\xi) R (\xi) ^ {- j / 2 k} R (\xi) ^ {(j m - | \alpha |) / \mu},
$$

where $\mu = 2(km - (k - 1))$ is the degree of $R(\xi)$. The sum of the exponents of $R(\xi)$ is

$$
\frac {j (k - 1) - k | \alpha |}{k \mu} \leq - \frac {| \alpha |}{k \mu} <   0,
$$

when $j \leq |\alpha|$ and $|\alpha| \neq 0$. Hence $S^{(\alpha)}(\xi)/P(\xi) \to 0$, when $\xi \to \infty$, if $|\alpha| \neq 0$. Thus we obtain

$$
\frac {P ^ {(\alpha)} (\xi)}{P (\xi)} \rightarrow 0, \text {   when   } \xi \rightarrow \infty , \text {   if   } | \alpha | \neq 0.
$$

Hence the condition III of Theorem 3.3 is fulfilled.

Finally we remark that the product of two complete operators of local type is complete and of local type, and that the sum of two self-adjoint operators of local type, which are bounded from below, is self-adjoint and of local type. The easy verification may be left to the reader. It is also an immediate consequence of condition

II of Theorem 3.3, that if P is of local type and  $Q(\xi)/P(\xi)\to0$  when  $\xi\to\infty$ , then  $P+tQ$  is of local type for any complex number t. Combining these simple remarks with Theorem 3.11, we could construct a very wide class of differential operators of local type.

## 3.9. An approximation theorem

For operators of local type we shall now answer a question raised on page 169.

THEOREM 3.12. Let $P(D)$ be of local type and let $\Omega$ be an arbitrary domain. Then the operator $P$ is the closure of its restriction to $\mathcal{D}_P \cap C^\infty$.

We note that the restriction of P, mentioned in the theorem, is defined for those infinitely differentiable functions u such that u and  $P(D)u$  are square integrable. The value of Pu is then of course calculated in the classical way.

PROOF. Using an idea of Deny-Lions [4], p. 312, we shall for given $\varepsilon > 0$ and $u \in \mathcal{D}_P$ construct a function $v \in C^\infty$ such that

$$
\left\| v - u \right\| <   \varepsilon , \left\| P (D) v - P u \right\| <   \varepsilon .\tag{3.9.1}
$$

Since these inequalities obviously imply that $v \in L^2$ and that $P(D)v \in L^2$, the theorem will then follow. Choose a locally finite covering $\Omega_k$, $k = 1, 2, \ldots$, of $\Omega$ such that $\overline{\Omega}_k \subset \Omega$ for every $k$, and then take functions $\varphi_k \in C_0^\infty(\Omega_k)$ so that $\sum \varphi_k(x) = 1$ (cf. Schwartz [28], Théorème II, Chap. I). The function $u_k = \varphi_k u$ is in $D_P$ in virtue of Definition 3.1, and we have

$$
u = \sum u _ {k}, \quad P u = \sum P u _ {k}
$$

(almost everywhere); the series converge since only a finite number of terms do not vanish in a compact subset of $\Omega$. (However, the second series is not $L^2$-convergent if $u \notin D_{P_0}$.) Now Lemma 2.11 shows that $u_k \in D_{P_0}$, so that we can find a function $v_k \in C_0^\infty(\Omega)$ such that

$$
\left\| u _ {k} - v _ {k} \right\| <   2 ^ {- k} \varepsilon , \quad \left\| P u _ {k} - P v _ {k} \right\| <   2 ^ {- k} \varepsilon .\tag{3.9.2}
$$

It follows from the proof of Lemma 2.11 that we may assume that $v_{k}$ has also its support in $\Omega_{k}$. Since the covering $\Omega_{k}$ is locally finite, the series $\sum v_{k}(x)$ converges for every $x$, and the sum $v(x)$ is in $C^{\infty}(\Omega)$. Using (3.9.2) we obtain

$$
\left\| v - u \right\| \leq \sum \left\| v _ {k} - u _ {k} \right\| <   \varepsilon , \quad \left\| P (D) v - P u \right\| \leq \sum \left\| P v _ {k} - P u _ {k} \right\| <   \varepsilon ,
$$

which proves (3.9.1).

16 - 553810. Acta Mathematica. 94. Imprimé le 28 septembre 1955.

## CHAPTER IV

## Differential Operators with Variable Coefficients

## 4.0. Introduction

In the two preceding chapters we have exclusively studied differential operators with constant coefficients. However, we shall see that the methods of the proof of Theorem 2.2, which is the central theorem in Chapter II, also apply when the coefficients are variable, if suitable restrictions are imposed. In order to exclude cases where the lower order terms and the variation of the coefficients may influence the strength of the operator, we shall only study operators $\pmb{p}$ of principal type. This means that the characteristics have no real singular points. (When the coefficients are constant, this is equivalent to Definition 2.1 according to Theorem 2.3.) Furthermore, we shall assume that the coefficients of the principal part are real, which means that there is some self-adjoint operator with the same principal part as $\pmb{p}$, so that $\pmb{p}$ is approximately self-adjoint. (It is sufficient to require that $\pmb{p}$ is approximately normal in the sense that the order of $p\overline{p} -\overline{p} p$ is at least two units lower than that of $p\overline{p}$. We do not study this case here.) The minimal differential operator defined by $\pmb{p}$ in a sufficiently small domain is then stronger than all operators of lower order, and has a continuous inverse. The same result is true for the algebraic adjoint $\overline{p}$. Hence, in sufficiently small domains, the equation $Pu = f$ has a square integrable solution for any square integrable function $f$. In the sense of section 1.3 there also exist correctly posed abstract boundary problems for the operator $\pmb{p}$. It seems that this is the first existence proof for differential operators with non-analytic coefficients, which are not of a special type.

## 4.1. Preliminaries

Let $\pmb{P}$ be a differential operator of order $m$ in a manifold $\Omega^{1}$. In a local coordinate system we may write

$$
P = \sum_ {| \alpha | \leq m} a ^ {\alpha} (x) D _ {\alpha}.\tag{4.1.1}
$$

Now, if $\varphi$ is an infinitely differentiable function in $\Omega$, we have for real $t$

$$
P e ^ {i t \varphi} = t ^ {m} \sum_ {| \alpha | = m} a ^ {\alpha} \varphi_ {\alpha} + O (t ^ {m - 1})
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Ω</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R^{\nu}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  It is sufficient here to suppose that  $\Omega$  is a domain in  $R^{\prime\prime}$ .</span></small>

when $t \to \infty$, where $\varphi_k = \partial \varphi / \partial x^k$ and $\varphi_\alpha = \varphi_{\alpha_1} \ldots \varphi_{\alpha_m}$. Thus the polynomial

$$
p (x, \xi) = \sum_ {| \alpha | = m} a ^ {\alpha} (x) \xi_ {\alpha}\tag{4.1.2}
$$

is a scalar, if $\xi$ is a covariant vector field. $p(x, \xi)$ is called the characteristic polynomial of $P$. The coefficients $a^{\alpha}(|\alpha| = m)$ form a symmetric contravariant tensor.

The differential operator P is called elliptic in  $\Omega$ , if  $p(x, \xi) \neq 0$  for every  $x \in \Omega$  and every real  $\xi \neq 0$ , and it is said to be of principal type in  $\Omega$ , if all the partial derivatives  $\partial p(x, \xi)/\partial \xi_{i}$  do not vanish simultaneously for any  $x \in \Omega$  and real  $\xi \neq 0$ .

We shall now deduce some formulas, which replace the more implicit arguments of section 2.4 in the case considered here. Let $p(x, \xi^{(1)}, \ldots, \xi^{(m)})$ be the symmetric multilinear form in the vectors $\xi^{(1)}, \ldots, \xi^{(m)}$, which is defined by $p(x, \xi)$,

$$
p (x, \xi^ {(1)}, \dots , \xi^ {(m)}) = \sum_ {\alpha} a ^ {\alpha_ {1} \dots \alpha_ {m}} (x) \xi_ {\alpha_ {1}} ^ {(1)} \dots \xi_ {\alpha_ {m}} ^ {(m)}.
$$

If  $k_{1}, \ldots, k_{p}$  are positive integers,  $k_{1} + \cdots + k_{p} = m$ , we shall write  $p(x, \xi^{(1)^{k_{1}}}, \ldots, \xi^{(p)^{k_{p}}})$  for the multilinear form where  $k_{i}$  arguments are equal to  $\xi^{(i)}$ . Sometimes we also omit the variable x. Now set for indeterminate  $\xi$  and  $\eta$

(4.1.3)

$$
\sum_ {i, k = 1} ^ {\nu} R ^ {i k} (\zeta , \bar {\zeta}) \xi_ {i} \eta_ {k} = m \sum_ {j = 0} ^ {m - 1} p (\zeta^ {j}, \bar {\zeta} ^ {m - 1 - j}, \xi) p (\zeta^ {m - 1 - j}, \bar {\zeta} ^ {j}, \eta),\tag{4.1.4}
$$

$$
\sum_ {i, k = 1} ^ {\nu} S ^ {i k} (\zeta , \overline {{\zeta}}) \xi_ {i} \eta_ {k} = m \sum_ {j = 1} ^ {m - 1} p (\zeta^ {j}, \overline {{\zeta}} ^ {m - j}) p (\zeta^ {m - 1 - j}, \overline {{\zeta}} ^ {j - 1}, \xi , \eta),
$$

and  $T^{ik}=R^{ik}-S^{ik}$ . Evidently  $T^{ik}=T^{ik}(x,\zeta,\bar{\zeta})$  is a symmetric tensor which is a homogeneous polynomial of degree m-1 in both  $\zeta$  and  $\bar{\zeta}$ . Since

$$
p \left(\zeta^ {m}\right) = p (\zeta), \quad p \left(\zeta^ {m - 1}, \xi\right) = \frac {1}{m} \sum_ {i = 1} ^ {\nu} \xi_ {i} \frac {\partial p}{\partial \zeta_ {i}},
$$

it is easy to verify the following fundamental property of the tensor  $T^{i k}$

$$
\sum_ {i = 1} ^ {\nu} \left(\zeta_ {i} - \overline {{\zeta}} _ {i}\right) T ^ {i k} (\zeta , \overline {{\zeta}}) = p (\zeta) \frac {\partial p (\overline {{\zeta}})}{\partial \overline {{\zeta}} _ {k}} - \frac {\partial p (\zeta)}{\partial \overline {{\zeta}} _ {k}} p (\overline {{\zeta}}).\tag{4.1.5}
$$

The arguments of section 2.6 were based on the fact that, in virtue of Lemma 2.2, there exist polynomials $T^{ik}(\zeta, \overline{\zeta})$ satisfying the identity (4.1.5), even for a non-homogeneous polynomial $p$. The simple explicit formulas given above for $T^{ik}$ in the case of a homogeneous polynomial $p$, have the now essential advantage that $T^{ik}$ are

homogeneous of degree m-1 in  $\zeta$  and in  $\bar{\zeta}$ . For second order equations the “energy” tensor  $T^{ik}$  was given by Hörmander [15].

We shall also use the tensor $Q^{ijk}(\zeta, \bar{\zeta})$ defined by the formula

$$
\begin{array}{l} \text {(4.1.6)} \quad 2 \sum_ {i, j, k = 1} ^ {\nu} Q ^ {i j k} (\zeta , \bar {\zeta}) \vartheta_ {i} \xi_ {j} \eta_ {k} \\ \quad = m \sum_ {j = 1} ^ {m - 1} j \left\{p (\zeta^ {m - 1 - j}, \bar {\zeta} ^ {j}, \vartheta) p (\zeta^ {j - 1}, \bar {\zeta} ^ {m - 1 - j}, \xi , \eta) - p (\zeta^ {j}, \bar {\zeta} ^ {m - 1 - j}, \vartheta) p (\zeta^ {m - 1 - j}, \bar {\zeta} ^ {j - 1}, \xi , \eta) \right\} + \\ \quad + m \sum_ {j = 2} ^ {m - 1} (j - 1) \left\{p (\zeta^ {j}, \bar {\zeta} ^ {m - j}) p (\zeta^ {m - 1 - j}, \bar {\zeta} ^ {j - 2}, \vartheta , \xi , \eta) - p (\zeta^ {m - j}, \bar {\zeta} ^ {j}) p (\zeta^ {j - 2}, \bar {\zeta} ^ {m - 1 - j}, \vartheta , \xi , \eta) \right\}. \end{array}
$$

This tensor is symmetric in the last two indices, and we have

$$
\sum_ {i = 1} ^ {\nu} \left(\zeta_ {i} - \bar {\zeta} _ {i}\right) Q ^ {i j k} (\zeta , \bar {\zeta}) = S ^ {j k} (\zeta , \bar {\zeta}) - \frac {1}{2} \left(p (\zeta) \frac {\partial^ {2} p (\bar {\zeta})}{\partial \bar {\zeta} _ {j} \partial \bar {\zeta} _ {k}} + p (\bar {\zeta}) \frac {\partial^ {2} p (\zeta)}{\partial \zeta_ {j} \partial \zeta_ {k}}\right).\tag{4.1.7}
$$

## 4.2. Estimates of the minimal operator

We shall now prove that an analogue of Theorems 2.1 and 2.2 is valid for certain differential operators P with variable coefficients. Since our results are not valid in the large, we may assume from the outset that our operator P is defined in a neighbourhood of a sphere  $|x| \leq A$  in  $R^{v}$ .

THEOREM 4.1. Suppose that $p(x, \xi)$ is real for real $\xi$ and of principal type, that is, that all the partial derivatives $\partial p(x, \xi) / \partial \xi_i$ do not vanish simultaneously for any real $\xi \neq 0$. Let the coefficients of $p(x, \xi)$ be continuously differentiable and the other coefficients of $P$ be continuous. Then there exists an open neighbourhood $\Omega$ of the origin, such that

$$
\sum_ {| \alpha | <   m} \| D _ {\alpha} u \| ^ {2} \leq C \| P u \| ^ {2}, \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{4.2.1}
$$

PROOF. It follows from (4.1.5) and the assumption that $p(x, \xi)$ is real that

$$
- \sum_ {l = 1} ^ {r} \frac {\partial}{\partial x ^ {l}} \left(T ^ {l k} (x, D, \bar {D}) u \bar {u}\right) = 2 \operatorname{Im} (p (x, D) u \overline {{p ^ {(k)} (x , D) u}}) + F ^ {k} (x, D, \bar {D}) u \bar {u},
$$

where $p^{(k)}(x,\xi) = \partial p(x,\xi) / \partial \xi_k$ and

$$
F ^ {k} (x, \zeta , \bar {\zeta}) = - \sum_ {l = 1} ^ {\nu} \frac {\partial}{\partial x ^ {l}} (T ^ {l k} (x, \zeta , \bar {\zeta})).
$$

Thus $F^k(x, D, \bar{D})u\bar{u}$ is a quadratic form in the derivatives of $u$ of order $m-1$ and has continuous coefficients. Multiplying by $x^k$ and integrating over an open neighbourhood $\Omega$ of the origin, we obtain, if $u \in C_0^\infty(\Omega)$,

$$
\begin{array}{c} \int T ^ {k k} (x, D, \bar {D}) u \bar {u} d x \\ = \int 2 x ^ {k} \operatorname{Im} (p (x, D) u \overline {{p ^ {(k)} (x , D) u}}) d x + \int x ^ {k} F ^ {k} (x, D, \bar {D}) u \bar {u} d x. \end{array}\tag{4.2.2}
$$

Denote by $\delta$ an upper bound of $|x|$ in $\Omega$. We may suppose that $\delta \leq A$, and shall prove that (4.2.1) is valid, if $\delta$ is sufficiently small. If we use the notations

$$
\left| u \right| _ {n} ^ {2} = \sum_ {| \alpha | = n} \int \left| D _ {\alpha} u \right| ^ {2} d x, \quad \left| \right| u \| _ {n} ^ {2} = \sum_ {| \alpha | \leq n} \int \left| D _ {\alpha} u \right| ^ {2} d x\tag{4.2.3}
$$

and note that $p(x, D)u$ only differs from $P u$ by a sum of derivatives of $u$ of orders $< m$, the inequality (4.2.2) and Schwarz' inequality give

$$
\int T ^ {k k} (x, D, \bar {D}) u \bar {u} d x \leq C \delta (\| P u \| \| u \| _ {m - 1} + \| u \| _ {m - 1} ^ {2}),\tag{4.2.4}
$$

where $C$ is a constant. (We shall denote by $C$ different constants, different times.) Now we have $T^{kk} = R^{kk} - S^{kk}$, so that (4.2.4) gives, after summation,

$$
\begin{array}{l} \int \sum_ {1} ^ {\nu} R ^ {k k} (0, D, \bar {D}) u \bar {u} d x \leq \int \sum_ {1} ^ {\nu} (R ^ {k k} (0, D, \bar {D}) - R ^ {k k} (x, D, \bar {D})) u \bar {u} d x + \\ \quad + \int \sum_ {1} ^ {\nu} S ^ {k k} (x, D, \bar {D}) u \bar {u} d x + C \delta (\| P u \| \| u \| _ {m - 1} + \| u \| _ {m - 1} ^ {2}). \end{array}\tag{4.2.5}
$$

We shall prove (4.2.1) by estimating the terms in this inequality.

The definition (4.1.3) of $R^{i k}$ shows that

$$
\sum_ {k = 1} ^ {\nu} R ^ {k k} (0, \xi , \xi) = \sum_ {k = 1} ^ {\nu} (\partial p (0, \xi) / \partial \xi_ {k}) ^ {2}.
$$

This is a homogeneous positive definite polynomial, since p is of principal type. Hence we have

$$
\sum_ {k = 1} ^ {\nu} R ^ {k k} (0, \xi , \xi) \geq c (\xi_ {1} ^ {2} + \dots + \xi_ {\nu} ^ {2}) ^ {m - 1}
$$

for some positive constant $c$, and using Parseval's formula (cf. formula (2.5.1)), we thus obtain

$$
c \left| u \right| _ {m - 1} ^ {2} \leq \int \sum_ {1} ^ {\nu} R ^ {k k} (0, D, \bar {D}) u \bar {u} d x.\tag{4.2.6}
$$

It is easy to find an estimate of the first term on the right-hand side of (4.2.5). In fact, since the coefficients of  $R^{k k}(0, D, \bar{D}) - R^{k k}(x, D, \bar{D})$  are continuously differentiable and vanish for x = 0, they are  $O(|x|)$ . Hence

$$
\int \sum_ {1} ^ {\nu} (R ^ {k k} (0, D, \bar {D}) - R ^ {k k} (x, D, \bar {D})) u \bar {u} d x \leq C \delta | u | _ {m - 1} ^ {2}.\tag{4.2.7}
$$

(4.2.10)

In order to estimate the integral $\int S^{k k}(x, D, \bar{D})u\bar{u}dx$ we must first integrate it by parts. Formula (4.1.7) with $j = k$ shows that

$$
\begin{array}{c} S ^ {k k} (x, D, \bar {D}) u \bar {u} \\ = \operatorname{Re} (p (x, D) u \overline {{p ^ {(k k)} (x , D) u}}) + G ^ {k} (x, D, \bar {D}) u \bar {u} + \frac {1}{i} \sum_ {j = 1} ^ {\nu} \frac {\partial}{\partial x ^ {j}} (Q ^ {j k k} (x, D, \bar {D}) u \bar {u}). \end{array}\tag{4.2.8}
$$

Here

$$
G ^ {k} (x, \zeta , \bar {\zeta}) = - \frac {1}{i} \sum_ {j = 1} ^ {\nu} \frac {\partial}{\partial x ^ {j}} Q ^ {j k k} (x, \zeta , \bar {\zeta}),
$$

so that $G^k(x, D, \bar{D})u\tilde{u}$ is a sum of products of derivatives of the orders $m-2$ and $m-1$ of $u$. Hence Schwarz' inequality shows that

$$
\int G ^ {k} (x, D, \bar {D}) u \bar {u} d x \leq C | u | _ {m - 1} | u | _ {m - 2}.\tag{4.2.9}
$$

Furthermore, the integral of the last term in (4.2.8) is zero, and using again the fact that $p(x, D)u$ differs from $Pu$ only by derivatives of order $< m$ of $u$, we thus obtain

$$
\int S ^ {k k} (x, D, \bar {D}) u \bar {u} d x \leq C (\left| \left| P u \right| + \left| \left| u \right| _ {m - 1}\right) \mid u \right| _ {m - 2} + C \mid u \mid_ {m - 1} \mid u \mid_ {m - 2}. \tag {0}
$$

If the two sides of the inequality (4.2.5) are estimated by means of the inequalities (4.2.6), (4.2.7) and (4.2.10), it follows that

$$
\left| u \right| _ {m - 1} ^ {2} \leq C \left(\left\| P u \right\| + \left\| u \right\| _ {m - 1}\right) (\delta \left\| u \right\| _ {m - 1} + \left| u \right| _ {m - 2}), \quad u \in C _ {0} ^ {\infty} (\Omega).\tag{4.2.11}
$$

To prove (4.2.1) we have now only to invoke the inequality

$$
\left| u \right| _ {k - 1} \leq C \delta \left| u \right| _ {k}, u \in C _ {0} ^ {\infty} (\Omega), k = 1, \dots , m,\tag{4.2.12}
$$

which is an immediate consequence of Lemma 2.7 but also well known previously (see for example Gårding [9], p. 57). It follows from (4.2.12) that $|u|_{m-2} \leq C\delta |u|_{m-1} \leq \leq C\delta \|u\|_{m-1}$, and, since $\delta \leq A$, that $\|u\|_{m-1} \leq C|u|_{m-1}$. Hence (4.2.11) gives with a constant $K$

so that

$$
\left\| u \right\| _ {m - 1} ^ {2} \leq K \left(\left\| P u \right\| + \left\| u \right\| _ {m - 1}\right) \delta \left\| u \right\| _ {m - 1},\tag{4.2.13}
$$

$$
\left\| u \right\| _ {m - 1} (1 - K \delta) \leq K \delta \| P u \|.
$$

Thus the inequality (4.2.1) follows, if $K\delta < 1$.

In particular, it follows from Theorem 4.1 that the operator $P_0$ in $L^2(\Omega)$ has a continuous inverse, if $\Omega$ is a suitable neighbourhood of the origin. Now let the coefficients of $p$ be sufficiently differentiable, so that $\overline{p}$ also satisfies the hypotheses

of Theorem 4.1. Then the operator $\overline{P}_0^{-1}$ is also continuous. Hence the equation $Pu = f$ has a solution $u \in L^2(\Omega)$ for any $f \in L^2(\Omega)$ in virtue of Lemma 1.7. Furthermore, using Theorem 2.15 and Theorem 4.1 it is easy to see that $P_0^{-1}$ and $\overline{P}_0^{-1}$ are completely continuous. Thus we can apply all the results of section 1.3. In particular, it follows that there exist completely correctly posed boundary problems for the differential operator $P$.

## References

[1]. M. Š. BIRMAN, On the theory of general boundary problems for elliptic differential equations. Doklady Akad. Nauk SSSR (N.S.), 92 (1953), 205–208 (Russian).

[2]. F. E. BROWDER, The eigenfunction expansion theorem for the general self-adjoint singular elliptic partial differential operator. I. The analytical foundation. Proc. Nat. Acad. Sci. U.S.A., 40 (1954), 454–459.

[3]. ——, Eigenfunction expansions for singular elliptic operators. II. The Hilbert space argument; parabolic equations on open manifolds. Proc. Nat. Acad. Sci. U.S.A., 40 (1954), 459–463.

[4]. J. DENY and J. L. LIONS, Les espaces du type de Beppo Levi. Ann. Inst. Fourier Grenoble, 5 (1955), 305–370.

[5]. K. O. FRIEDRICHs, On the differentiability of the solutions of linear elliptic differential equations. Comm. Pure Appl. Math., 6 (1953), 299-326.

[6]. K. FRIEDRICHs and H. LEWY, Über die Eindeutigkeit und das Abhängigkeitsgebiet der Lösungen beim Anfangsproblem linearer hyperbolischer Differentialgleichungen. Math. Ann., 98 (1928), 192–204.

[7]. T. GANELIUS, On the remainder in a Tauberian theorem. Kungl. Fysiografiska Sällskapets i Lund Förhandlingar, 24, No. 20 (1954).

[8]. L. GARDING, Linear hyperbolic partial differential equations with constant coefficients. Acta Math., 85 (1951), 1–62.

[9]. ——, Dirichlet's problem for linear elliptic partial differential equations. Math. Scand., 1 (1953), 55–72.

[10]. ——, On the asymptotic distribution of the eigenvalues and eigenfunctions of elliptic differential operators. Math. Scand., 1 (1953), 237–255.

[11]. —, Eigenfunction expansions connected with elliptic differential operators. Comptes rendus du Douzième Congrès des Mathématiciens Scandinaves, Lund, 1953, 44–55.

[12]. ——, Applications of the theory of direct integrals of Hilbert spaces to some integral and differential operators. University of Maryland, The Institute for Fluid Dynamics and Applied Mathematics, Lecture Series, No. 11 (1954).

[13]. —, On the asymptotic properties of the spectral function belonging to a self-adjoint semi-bounded extension of an elliptic operator. Kungl. Fysiografiska Sällskapets i Lund förhandlingar, 24, No. 21 (1954).

[14]. E. HILLE, An abstract formulation of Cauchy's problem. Comptes rendus du Douzième Congrès des Mathématiciens Scandinaves, Lund, 1953, 79–89.

[15]. L. HÖRMANDER, Uniqueness theorems and estimates for normally hyperbolic partial differential equations of the second order. Comptes rendus du Douzième Congrès des Mathématiciens Scandinaves, Lund, 1953, 105–115.

[16]. F. JOHN, On linear partial differential equations with analytic coefficients. Unique continuation of data. Comm. Pure Appl. Math., 2 (1949), 209-253.

[17]. M. KREIN, Theory of the self-adjoint extensions of semi-bounded hermitian operators and its applications. I. Mat. Sbornik, 20[62] (1947), 431–495 (Russian, English summary).

[18]. O. LADYZENSKAJA, On the closure of the elliptic operator. Doklady Akad. Nauk SSSR (N.S.), 79 (1951), 723–725 (Russian).

[19]. J. LERAY, Hyperbolic Differential Equations. The Institute for Advanced Study, Princeton N.J. (1954).

[20]. B. MALGRANGE, Equations aux dérivées partielles à coefficients constants. 1. Solution élémentaire. C. R. Acad. Sci. Paris, 237 (1953), 1620–1622.

[21]. —, Existence et approximation des solutions des équations aux dérivées partielles et des équations de convolution. Thesis, Paris, June 1955.

[22]. A. MYCHKIS, Sur les domaines d'unicité pour les solutions des systèmes d'équations linéaires aux dérivées partielles. Mat. Sbornik (N.S.), 19[61] (1946), 489–522 (Russian, French summary).

[23]. B. v. Sz. NAGY, Spektraldarstellung linearer Transformationen des Hilbertsschen Raumes. Berlin, 1942.

[24]. J. v. NEUMANN, Über adjungierte Funktionaloperatoren. Ann. of Math., (2) 33 (1932), 294–310.

[25]. I. G. PETROWSKY, On some problems of the theory of partial differential equations. Amer. Math. Soc., Translation No. 12 (translated from Uspehi Matem. Nauk (N.S.), 1 (1946), No. 3-4 (13-14), 44-70).

[26]. —, Sur l'analyticité des solutions des systèmes d'équations différentielles. Mat. Sbornik, 5[47] (1939), 3–70 (French, Russian summary).

[27]. G. DE RHAM, Solution élémentaire d'équations aux dérivées partielles du second ordre à coefficients constants. Colloque Henri Poincaré (Octobre 1954).

[28]. L. SCHWARTZ, Théorie des distributions, I-II. Paris, 1950-1951.

[29]. A. SEIDENBERG, A new decision method for elementary algebra. Ann. of Math., (2) 60 (1954), 365-374.

[30]. S. L. SOBOLEV, Some Applications of Functional Analysis in Mathematical Physics. Le-ningrad, 1950 (Russian).

[31]. S. TÄCKLIND, Sur les classes quasianalytiques des solutions des équations aux dérivées partielles du type parabolique. Nova Acta Soc. Sci. Upsaliensis, (4) 10 (1936), 1–57.

[32]. A. TYCHONOV, Théorèmes d'unicité pour l'équation du chaleur. Mat. Sbornik, 42 (1935), 199–216.

[33]. B. L. VAN DER WAERDEN, Moderne Algebra, I. Berlin, 1950.

[34]. M. I. Višik, On general boundary problems for elliptic differential equations. Trudy Moskov. Mat. Obsč., 1 (1952), 187–246 (Russian).

[35]. A. ZYGMUND, Trigonometrical Series. Warszawa-Lwow, 1935.