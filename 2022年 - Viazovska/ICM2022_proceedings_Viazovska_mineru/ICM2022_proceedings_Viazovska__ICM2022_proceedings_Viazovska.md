# On discrete Fourier uniqueness sets in Euclidean space

Maryna Viazovska

Abstract In this paper we present a new construction of a discrete Fourier uniqueness set in Euclidean space.

Mathematics Subject Classification 2020 Primary 11F67; Secondary 11F41, 11G40

Keywords Fourier uniqueness, harmonic analysis

## 1. Introduction

The goal of this paper give a new construction of a closed discrete Fourier uniqueness set in$\mathbb { R } ^ { d }$. Let us start with a definition of Fourier uniqueness. For a Schwartz function$f$: $\mathbb { R } ^ { d } \to \mathbb { C }$its Fourier transform is defined as

$$
\widehat {f} (y) := \int_ {\mathbb {R} ^ {d}} f (x) e ^ {- 2 \pi i x y} d x, \quad y \in \mathbb {R} ^ {d}.
$$

Definition 1.1. A set$X \subset \mathbb { R } ^ { d }$is a Fourier uniqueness set if for a Schwartz function$f$the conditions

$$
f \mid_ {X} \equiv 0 \quad \widehat {f} \mid_ {X} \equiv 0
$$

imply$f \equiv 0$

In [3] we have shown that the set$X = \{ \mathrm { s i g n } ( n ) \sqrt { | n | } \} _ { n \in \mathbb { Z } }$is essentially a uniqueness set in R. More precisely, we have proven that the conditions$f \mid _ { X } \equiv 0 , { \widetilde { f } } \mid _ { X } \equiv 0$together with one more linear constrain$f ^ { \prime } ( 0 ) = 0$imply the vanishing of$f$on the whole real line. M. Stoller [4] has extended this result to$\mathbb { R } ^ { d }$in the following way. For a positive real number$r$let$S ( r )$denote the sphere in$\mathbb { R } ^ { d }$with center at the origin and radius$r$. Stoller has proven that the set$X : = \textstyle \bigcup _ { n = 1 } ^ { \infty } S ( { \sqrt { n } } )$is a Fourier uniqueness set in$\mathbb { R } ^ { d }$for$d \ge 5$. The following theorem is proven in [4]

Theorem 1.2. Let �$\geq 5$be an integer. Suppose that$f : \mathbb { R } ^ { d }  \mathbb { C }$is a Schwartzfunction such that$f \mid _ { S ( { \sqrt { n } } ) } \equiv 0$and$\widehat { f } | _ { S ( \sqrt { n } ) } \equiv 0$for all$n \in \mathbb { Z } _ { \geq 1 }$. Then � is identically zero.

Moreover, recently Stoller and J. P. G. Ramos have shown the existence of a closed discrete Fourier uniqueness set in$\mathbb { R } ^ { d }$[5, Theorem 2, Remark 1.1].

A natural question is: how “big” is this discrete Fourier uniqueness set? More pre-cisely, for a closed discrete subset$X \subset \mathbb { R } ^ { d }$we would like to analyse the function$M _ { X } ( r )$ $r \in \mathbb { R } _ { > 0 }$, that counts the number of elements of$X$inside of the ball of radius$r$about the origin. For the Fourier uniqueness set constructed in [5, Theorem 2, Remark 1.1] the function $M _ { X } ( r )$grows superexponentially in$r$.

The goal of this paper is to construct a closed discrete Fourier uniqueness set$X$such that the function$M _ { X } ( r )$grows at most polynomially in$r$.

## 1.1. Construction of a discrete Fourier uniqueness set

In this paper we will show that for a family of suficiently uniformly distributed finite subsets$X _ { n } \subset S ( 1 ) , n \in \mathbb { Z } _ { \geq 1 }$, the union

$$
X := \bigcup_ {n \geq 1} \sqrt {n} X _ {n}\tag{1.1}
$$

is a Fourier uniqueness set. Let us give one possible quantitative description of the term “uniformly distributed”.

Definition 1.3. Afinite subset$X \subset S ( 1 )$is a spherical design of strength$s$if for all polynomials$p$in$d$variables and total degree at most$s$the following holds:

$$
\int_ {S (1)} p (\zeta) d \zeta = \frac {1}{| X |} \sum_ {x \in X} p (x).
$$

Here$d \zeta$denotes the Lebesgue measure on$S ( 1 )$normalized so that$\int _ { S ( 1 ) } 1 d \zeta = 1$

The main result of this paper is

Theorem 1.4. For each dimension$d$there exist positive constants$\widetilde { A } = \widetilde { A } ( d )$and$\widetilde { B } = \widetilde { B } ( d )$ with the following property. If$( X _ { n } ) _ { n = 1 } ^ { \infty }$is a collection of finite subsets of$S ( 1 )$such that each set$X _ { n }$is a spherical design of strength$\widetilde { B } n ^ { \widetilde { A } }$then the set

$$
X := \bigcup_ {n \geq 1} \sqrt {n} X _ {n}
$$

is a Fourier uniqueness set.

It is known [?] that for a dimension$d$there exists a constant$c _ { d }$such that for all nonnegative integers$s$there exists a spherical design of strength$s$with at most$c _ { d } \ : s ^ { d }$points. Therefore, the above theorem implies the existence of a closed discrete Fourier uniqueness set with polynomially bounded function$M _ { X } ( r )$

## 2. Auxiliary results from Fourier analysis

Our proof of Theorem (1.4) relies on several facts from Fourier analysis and the theory of modular forms. First, we will use the following statements about the decomposition of a Schwartz function in$\mathbb { R } ^ { d }$. Let$\mathcal { H } _ { m } = \mathcal { H } _ { m } ( \mathbb { R } ^ { d } )$be the space of homogenous harmonic polynomials of total degree$m$on$\mathbb { R } ^ { d }$. Let${ \mathcal { B } } _ { m }$be an orthonormal basis of$\mathcal { H } _ { m }$with respect to the standard$L _ { 2 }$product on the unit sphere$S ( 1 )$. Set$\textstyle { \mathcal { B } } : = \bigcup _ { m \geq 0 } { \mathcal { B } } _ { m }$. Each Schwartz function $f : \mathbb { R } ^ { d } \to \mathbb { C }$has the unique decomposition

$$
f (x) = \sum_ {p \in \mathcal {B}} p (x) g _ {p} (\| x \|),
$$

where$g _ { p }$are radial Schwartz functions. For$p \in { \mathcal { B } }$we denote

$$
f _ {p} (x) := p (x)   g _ {p} (\| x \|).\tag{2.1}
$$

Theorem 2.1. Let$f : \mathbb { R } ^ { d } \to \mathbb { C }$be a Schwartz function. For$p \in { \mathcal { B } }$and$n \in \mathbb { Z } _ { \geq 1 }$we set

$$
\phi_ {p, n} = \phi_ {p, n} (f) := \sup _ {x \in S (\sqrt {n})} | f _ {p} (x) |.
$$

For all$\alpha , \beta > 0$we have

$$
\sup _ {p \in \mathcal {B}, n \in \mathbb {Z} _ {\geq 1}} \left(\deg (p) ^ {\alpha} n ^ {\beta} \phi_ {p, n}\right) <   \infty .
$$

Proof. We have

$$
\phi_ {p, n} = \sup _ {x \in S (\sqrt {n})} | f _ {p} (x) | = n ^ {\frac {\deg (p)}{2}} | g _ {p} (\sqrt {n}) | \sup _ {\zeta \in S (1)} | p (\zeta) |.
$$

The number$g _ { p } ( { \sqrt { n } } )$can be computed as follows

$$
\begin{array}{l} \int_ {S (1)} f (\sqrt {n} \zeta)   p (\zeta)   d \zeta \\ = \int_ {S (1)} g _ {p} (\sqrt {n})   p (\sqrt {n} \zeta)   \overline {{p (\zeta)}}   d \zeta \\ = n ^ {\frac {\deg (p)}{2}}   g _ {p} (\sqrt {n}). \end{array}\tag{2.2}
$$

Therefore

$$
\begin{array}{l} \phi_ {p, n} = \left| \int_ {S (1)} f (\sqrt {n} \zeta)   p (\zeta)   d \zeta \right| \cdot \sup _ {\zeta \in S (1)} | p (\zeta) | \\ \leq \sup _ {x \in S (\sqrt {n})} | f (x) | \sup _ {\zeta \in S (1)} | p (\zeta) | ^ {2}. \end{array}\tag{2.3}
$$

Note that there exist positive constants$C _ { 1 }$and$C _ { 2 }$depending only on dimension$d$such that $\begin{array} { r } { \operatorname* { s u p } _ { \zeta \in S ( 1 ) } | p ( \zeta ) | \le C _ { 1 } \deg ( p ) ^ { C _ { 2 } d } } \end{array}$for all$p \in { \mathcal { B } }$. This gives us an estimate

$$
\phi_ {p, n} \leq C _ {1} \deg (p) ^ {2 C _ {2}} \sup _ {x \in S (\sqrt {n})} | f (x) |.\tag{2.4}
$$

Let$\beta$be a fixed positive number. Since$f$is a Schwartz function, we have

$$
\sup _ {x \in \mathbb {R} ^ {d}} \| x \| ^ {\beta} | f (x) | <   \infty .\tag{2.5}
$$

Estimates (2.4) and (2.5) imply

$$
\sup _ {p \in \mathcal {B}, n \in \mathbb {Z} _ {\geq 1}} \left(\deg (p) ^ {- 2 C _ {2}} n ^ {\beta} \phi_ {p, n}\right) <   \infty .\tag{2.6}
$$

Our next goal is to replace$- 2 C _ { 2 }$with an arbitrary positive constant$\alpha$. Let$\Delta =$ $\begin{array} { r } { \frac { \partial ^ { 2 } } { \partial x _ { 1 } ^ { 2 } } + . . . + \frac { \partial ^ { 2 } } { \partial x _ { 1 } ^ { 2 } } } \end{array}$be the Laplace operator on$\mathbb { R } ^ { d }$. For a point$x \in \mathbb { R } ^ { d } \setminus \{ 0 \}$we define its polar coordinates$r = \| x \|$and$\zeta = x / \| x \|$. Consider the following diferential operator

$$
\Delta_ {S ^ {d - 1}} f := r ^ {2} \Delta f - (d - 1) r \frac {\partial}{\partial r} f - r ^ {2} \frac {\partial^ {2}}{\partial r ^ {2}} f.
$$

An important property of this operator is that it maps Schwartz functions to the Schwartz functions. Indeed, we compute in polar coordinates$x = r \zeta$

$$
\begin{array}{l} r \frac {\partial}{\partial r} f (r \zeta_ {1}, \ldots , r \zeta_ {d}) = r \zeta_ {1} \frac {\partial}{\partial x _ {1}} f + \ldots + r \zeta_ {d} \frac {\partial}{\partial x _ {d}} f \\ = x _ {1} \frac {\partial}{\partial x _ {1}} f + \ldots + x _ {d} \frac {\partial}{\partial x _ {d}} f \end{array}
$$

and analogously

$$
\begin{array}{l} {r ^ {2} \frac {\partial^ {2}}{\partial r ^ {2}} f (r \zeta_ {1}, \ldots , r \zeta_ {d}) = r ^ {2} \zeta_ {1} ^ {2} \frac {\partial^ {2}}{\partial x _ {1} ^ {2}} f + \ldots + r ^ {2} \zeta_ {d} ^ {2} \frac {\partial^ {2}}{\partial x _ {d} ^ {2}} f} \\ {= x _ {1} ^ {2} \frac {\partial^ {2}}{\partial x _ {1} ^ {2}} f + \ldots + x _ {d} ^ {2} \frac {\partial^ {2}}{\partial x _ {d} ^ {2}} f.} \end{array}
$$

Thus, if$f$is a Schwartz function so is$\Delta _ { S ^ { d - 1 } } f$. Suppose that$g$is a radial Schwartz function and$p$is a homogenous harmonic polynomial on$\mathbb { R } ^ { d }$of total degree$\deg ( p )$. Then a straightforward computation shows that

$$
\Delta_ {S _ {d}} (g (r) p (x)) = - \deg (p) (\deg (p) + d - 2) g (r) p (x).\tag{2.7}
$$

We define$\lambda _ { m } : = - m ( m + d - 2 )$. Clearly,$\left| \lambda _ { m } \right| \sim m ^ { 2 }$as � goes to infinity.

Now let$\alpha$be a positive integer. Given a Schwartz function$f$we define a new Schwartz function$\widetilde { f } : = \Delta _ { S ^ { d - 1 } } ^ { \alpha } f$. Suppose that$f$has decomposition$\begin{array} { r } { f = \sum _ { p \in \mathcal { B } } f _ { p } , } \end{array}$, then by equation (2.7) the new function$\widetilde { f }$has decomposition$\begin{array} { r } { \widetilde { f } = \sum _ { p \in \mathcal { B } } \widetilde { f _ { p } } } \end{array}$where$\widetilde { f _ { p } } = \lambda _ { \mathrm { d e g } ( p ) } ^ { \alpha } f _ { p } .$ Also the numbers$\widetilde { \phi } _ { p , n } : = \mathrm { m a x } _ { x \in S ( \sqrt { n } ) } \vert \widetilde { f } _ { p } ( x ) \vert$satisfy

$$
\widetilde {\phi} _ {p, n} = | \lambda_ {\deg (p)} | ^ {\alpha} \phi_ {p, n}.
$$

Finally, we apply estimate (2.6) to the function$\widetilde { f }$and derive

$$
\sup _ {p \in \mathcal {B}, n \in \mathbb {Z} _ {\geq 1}} \left(\deg (p) ^ {2 \alpha - 2 C _ {2}} n ^ {\beta} \phi_ {p, n}\right) <   \infty
$$

for arbitrary positive$\alpha$and$\beta .$. This finishes the proof of the theorem.

## 3. Auxiliary results from the theory of modular forms

Let$k$be a half integer. We denote by$S _ { k } ( \Gamma ( 2 ) , \chi _ { k } )$the space of holomorphic cusp forms$h$satisfying the transformation rule

$$
\left\{ \begin{array}{l} h (\tau + 2) = h (\tau) \\ \widetilde {h} := (- i \tau) ^ {k} \widetilde {h} (\tau) \\ \widetilde {h} (\tau + 2) = \widetilde {h} (\tau). \end{array} \right.
$$

The following statement is known as Voronoi summation formula.

Theorem 3.1. Let$h$be a cusp form in$S _ { d / 2 } ( \Gamma ( 2 ) , \chi _ { d } )$) and let$\widetilde { h } ( \tau ) : = ( - i \tau ) ^ { - d / 2 } h ( \frac { - 1 } { \tau } )$. Then for a radial Schwartzfunction$f : \mathbb { R } ^ { d } \to \mathbb { C }$the following summation formula holds

$$
\sum_ {n = 1} ^ {\infty} f (\sqrt {n}) c _ {h} (n) = \sum_ {n = 1} ^ {\infty} \widehat {f} (\sqrt {n}) c _ {\widetilde {h}} (n).
$$

For a half integer$k$and a positive number$\epsilon$we define

$$
N (k, \epsilon) := \left(\frac {\epsilon \Gamma (k - 1 / 2)}{(2 \pi) ^ {k - 1} \zeta (k - 2)   4 \pi}\right) ^ {1 / k}.
$$

A straight forward consequence of the Stirling formula is that

$$
N (k, \epsilon) \sim \frac {k}{2 \pi e} \mathrm{as} k \rightarrow \infty .
$$

The main technical tool in our proof of Theorem 1.4 is the following statement about the space of modular forms$S _ { k } ( \Gamma ( 2 ) , \chi _ { k } )$.

Theorem 3.2. Fix a number$\epsilon \in ( 0 , 1 / 2 )$and for a half-integer$k$set$N ( k ) : = \lfloor N ( k , \epsilon ) \rfloor$. For each half-integral weight$k \geq 5 / 2$there exist element$\left( h _ { m } \right) _ { m = 1 } ^ { N ( k ) - 1 }$in the space$S _ { k } ( \Gamma ( 2 ) , \chi _ { d } )$ such that:

(1) the function$h _ { m }$has the Fourier expansion

$$
h_{m}(\tau) = e^{\pi im\tau} + \sum_{\substack{n\in \mathbb{Z}\\ n\geq N(k)}}c_{h_{m}}(n)e^{\pi in\tau}
$$

(2) the function$\begin{array} { r } { \widetilde { h } _ { m } : = ( - i \tau ) ^ { - k } h _ { m } ( \frac { - 1 } { \tau } ) } \end{array}$has the Fourier expansion

$$
\widetilde{h}_{m}(\tau) = \sum_{\substack{n\in \mathbb{Z}\\ n\geq N(k)}}c_{\widetilde{h}_{m}}(n)e^{\pi in\tau}
$$

(3) the Fourier coeficients$c _ { h _ { m } } ( n )$and$c _ { \widetilde { h } _ { m } } ^ { } \left( n \right)$satisfy the following estimates

$$
\left| c _ {h _ {m}} (n) \right| \leq C m ^ {- k / 2 + \alpha} n ^ {k / 2 + \alpha}
$$

$$
| c _ {\widetilde {h} _ {m}} (n) | \leq C m ^ {- k / 2 + \alpha} n ^ {k / 2 + \alpha}.
$$

Here$C$and$\alpha$are positive constants independent of$k$, $m$, and $n$ and depending on$\epsilon$.

## 4. Proof of Theorem 3.2

Let$P _ { k , \chi , m }$be the Poincare series for the group Γ(2) and multiplier system$\chi _ { k }$(see [2, ${ \mathsf { p } } . 4 7 ,$equation (3.2)]). The Fourier coeficients of the Poincare series can be explicitly computed by the Petersson formula:

$$
c _ {P _ {k, \chi , m}} (n) = \delta_ {m, n} + \sum_ {c > 0} S (m, n, c) \mathcal {J} _ {c} (m, n).\tag{4.1}
$$

Here$\mathcal { J } _ { c } ( m , n )$is the following sum

$$
\mathcal {J} _ {c} (m, n) = \frac {2 \pi}{i ^ {k} c} \left(\frac {n}{m}\right) ^ {\frac {k - 1}{2}} J _ {k - 1} \left(\frac {4 \pi \sqrt {m n}}{c}\right),
$$

the function$J _ { \nu }$is the Bessel J-function given by the power series

$$
J _ {\nu} (x) = \sum_ {\ell = 0} ^ {\infty} \frac {(- 1) ^ {\ell}}{\ell !   \Gamma (\ell + 1 + \nu)} \left(\frac {x}{2}\right) ^ {\nu + 2 \ell}.
$$

And$S ( m , n , c )$is the Kloosterman sum defined in [2, p. 51, equation (3.13)]. The following estimate can be found in [4].

Lemma 4.1. For a half-integer weight$k \geq 5 / 2$and positive integers$m$, $n$the Fourier coefficients ofPoincare series satisfy:

$$
\left| c _ {P _ {k, n}} (m) - \delta_ {m, n} \right| \leq \left(\frac {m}{n}\right) ^ {\frac {k - 1}{2}} \varepsilon^ {- 2} n ^ {1 + \varepsilon} m ^ {1 + \varepsilon} C
$$

$$
\left| c _ {\tilde {P} _ {k, n}} (m) \right| \leq \left(\frac {m}{n}\right) ^ {\frac {k - 1}{2}} \varepsilon^ {- 2} n ^ {1 + \varepsilon} m ^ {1 + \varepsilon} C.
$$

Here $C$ is an absolute constant and$\varepsilon$is any number in the interval$( 0 , \textstyle { \frac { 1 } { 8 } } ]$

Lemma 4.2. For a half-integer weight$k \geq 5 / 2$and positive integers$m$, $n$lying in the interval $[ 1 , N ( k , \epsilon ) ]$the Fourier coefficients of Poincare series satisfy:

(1)

$$
\left| c _ {P _ {k, n}} (m) - \delta_ {m, n} \right| \left(\frac {n}{m}\right) ^ {\frac {k - 1}{2}} \leq \frac {\epsilon}{N (k , \epsilon)};
$$

(2)

$$
\left| c _ {\tilde {P} _ {k, n}} (m) \right| \left(\frac {n}{m}\right) ^ {\frac {k - 1}{2}} \leq \frac {\epsilon}{N (k , \epsilon)}.
$$

Proof. Part (1) of the lemma in an immediate consequence of Stirling’s formula.

The Mehler-Sonine formula [1] gives the following integral representation of the Bessel �-function

$$
J _ {\nu} (z) = \frac {(z / 2) ^ {\nu}}{\Gamma (\nu + 1 / 2) \sqrt {\pi}} \int_ {- 1} ^ {1} e ^ {i z s} (1 - s ^ {2}) ^ {\nu - \frac {1}{2}} d s, \quad \nu > \frac {- 1}{2}, z \in \mathbb {C}.
$$

This integral representation implies an estimate

$$
\left| J _ {\nu} (z) \right| \leq \frac {(z / 2) ^ {\nu} 2}{\Gamma (\nu + 1 / 2) \sqrt {\pi}}.
$$

Also we use the trivial estimate for the Kloosterman sums (see [2][eq. 3.13])

$$
| S (m, n, c) | <   c ^ {2}.
$$

We combine these two estimates with the Petersson formula (4.1) for the Fourier coefficients of the Poincare series and obtain

$$
\begin{array}{l} \left| c _ {P _ {k, n}} (m) - \delta_ {m, n} \right| \left(\frac {n}{m}\right) ^ {\frac {k - 1}{2}} \\ \leq 2 \pi \sum_ {c > 0} c \left| J _ {k - 1} \left(\frac {4 \pi \sqrt {m n}}{c}\right) \right| \\ \leq 4 \pi \sum_ {c > 0} c \left| \frac {(2 \pi / c) ^ {k - 1}}{\Gamma (\nu + 1 / 2)} \right| (m n) ^ {\frac {k - 1}{2}} \\ \leq 4 \pi \frac {\zeta (k - 2) (2 \pi) ^ {k - 1}}{\Gamma (k - 1 / 2)} (m n) ^ {\frac {k - 1}{2}}. \end{array}\tag{4.2}
$$

Note that$\sqrt { m n } \le N ( k , \epsilon )$, therefore inequality (4.2) and our choise of the function$N ( k , \epsilon )$ imply part (2) of the lemma. Proof of part (3) is analogous.

Proof of Theorem 3.2.

Fix a half integral weight � and$\epsilon \in ( 0 , 1 / 2 )$and set$N : = \lfloor N ( k , \epsilon ) \rfloor$. Consider a matrix $A = ( a _ { m , n } ) _ { m , n = 1 } ^ { 2 N }$with entries defined by the coeficients of the Poincare series$\mathcal { P } _ { m } : = \mathcal { P } _ { k , m }$ as

$$
a _ {m, n} = \left\{ \begin{array}{l l} c _ {\mathcal {P} _ {m}} (n) \left(\frac {m}{n}\right) ^ {\frac {k - 1}{2}} & \text {if} m, n \in [ 1, N ] \\ c _ {\bar {\mathcal {P}} _ {m}} (n - N) \left(\frac {m}{n - N}\right) ^ {\frac {k - 1}{2}} & \text {if} m \in [ 1, N ], n \in [ N + 1, 2 N ] \\ c _ {\tilde {\mathcal {P}} _ {m - N}} (n) \left(\frac {m - N}{n}\right) ^ {\frac {k - 1}{2}} & \text {if} m \in [ N + 1, 2 N ], n \in [ 1, N ] \\ c _ {\tilde {\mathcal {P}} _ {m - N}} (n - N) \left(\frac {m - N}{n - N}\right) ^ {\frac {k - 1}{2}} & \text {if} m, n \in [ N + 1, 2 N ]. \end{array} \right.
$$

From Lemma 4.2 we know that � is diagonally dominated and therefore invertible. Moreover, the inverse matrix$B = ( b _ { m , n } ) _ { m , n = 1 } ^ { 2 N } : = A ^ { - 1 }$satisfies

$$
\left| b _ {m, n} - \delta_ {m, n} \right| <   \sum_ {k = 1} ^ {\infty} (2 \epsilon) ^ {k} = \frac {2 \epsilon}{1 - 2 \epsilon}.\tag{4.3}
$$

Consider modular forms

$$
h _ {\ell} := \ell^ {\frac {1 - k}{2}} \sum_ {n = 1} ^ {N} \left(b _ {\ell , n} P _ {n} + b _ {\ell , n + N} \widetilde {P} _ {n}\right) n ^ {\frac {k - 1}{2}}, \qquad \ell = 1, \dots , N.\tag{4.4}
$$

From the definition of coefficients$b _ { \ell , n }$we see

$$
c _ {h _ {\ell}} (m) = \delta_ {\ell , m} \quad \text { for } \ell , m = 1, \dots N.
$$

For the functions$\widetilde { h } _ { \ell } ( \tau ) : = ( - i \tau ) ^ { - k } h _ { \ell } ( - 1 / \tau )$we find

$$
\widetilde {h} _ {\ell} := \ell^ {\frac {1 - k}{2}} \sum_ {n = 1} ^ {N} \left(b _ {\ell , n} \widetilde {P} _ {n} + b _ {\ell , n + N} P _ {n}\right) n ^ {\frac {k - 1}{2}}, \qquad \ell = 1, \dots , N.\tag{4.5}
$$

The matrix$A$has symmetries$a _ { m , n } = a _ { m + N , n + N }$and$a _ { m + N , n } = a _ { m , n + N }$for$m$, $n = 1 , \ldots N$. Same symmetries are inherited by$B$, namely$b _ { m , n } = b _ { m + N , n + N } , b _ { m + N , n } = b _ { m , n + N }$under same assumptions on indices$m$and$n$. Hence, we can rewrite (4.5) as

$$
\widetilde {h} _ {\ell} := \ell^ {\frac {1 - k}{2}} \sum_ {n = 1} ^ {N} \left(b _ {\ell + N, n} P _ {n} + b _ {\ell + N, n + N} \widetilde {P} _ {n}\right) n ^ {\frac {k - 1}{2}}, \qquad \ell = 1, \dots , N.
$$

Thus, we see that

$$
c _ {\widetilde {h} _ {\ell}} (m) = \delta_ {\ell , m + N} = 0 \quad \mathrm{for} \ell , m = 1, \ldots N.
$$

Finally, we prove part (3) of the theorem. Let$\ell$and$m$be integers such that$\ell \in [ 1 , N ]$ and$m \in ( N , \infty )$. We apply definition (4.4) and estimate the$m$-th Fourier coefficient of$h _ { \ell }$

$$
\left| c _ {h _ {\ell}} (m) \right| \ell^ {\frac {k - 1}{2}} m ^ {\frac {1 - k}{2}} \leq \sum_ {n = 1} ^ {N} \left(\left| b _ {\ell , n} \right| \left| c _ {P _ {n}} (m) \right| n ^ {\frac {k - 1}{2}} m ^ {\frac {1 - k}{2}} + \left| b _ {\ell , n + N} \right| \left| c _ {\tilde {P} _ {n}} (m) \right| n ^ {\frac {k - 1}{2}} m ^ {\frac {1 - k}{2}}\right).
$$

Now we apply Lemma 4.1 and estimate (4.3) in order to obtain

$$
\left| c _ {h _ {\ell}} (m) \right| \ell^ {\frac {k - 1}{2}} m ^ {\frac {1 - k}{2}} \leq \frac {2}{1 - 2 \epsilon} \sum_ {n = 1} ^ {N} \varepsilon^ {- 2} n ^ {1 + \varepsilon} m ^ {1 + \varepsilon} C \leq \frac {2 C}{(1 - 2 \epsilon) \varepsilon^ {2}} N ^ {2 + \varepsilon} m ^ {1 + \varepsilon}.
$$

Analogosly, we show that

$$
\left| c _ {\widetilde {h} _ {\ell}} (m) \right| \ell^ {\frac {k - 1}{2}} m ^ {\frac {1 - k}{2}} \leq \frac {2 C}{(1 - 2 \epsilon) \varepsilon^ {2}} N ^ {2 + \varepsilon} m ^ {1 + \varepsilon}.
$$

This finishes the proof of Theorem 3.2.

## 5. Proof of Theorem 1.4

Lemma 5.1. Let$\left( X _ { n } \right) _ { n = 1 } ^ { \infty }$be a sequence ofsubsets$o f S ( 1 )$such that$X _ { n }$is a spherical design of strength$D ( n )$and let$X : = \cup _ { n = 1 } ^ { \infty } { \sqrt { n } } X _ { n }$. Suppose that$f$is a Schwartz function such that $f \mid _ { X } = 0$. There exist an absolute positive constant$C$independent of$f$and$p$and a positive number$\beta ,$which depends linearly on dimension$d ,$such that for all$p \in { \mathcal { B } }$and$n \in \mathbb { Z } _ { \geq 1 }$

$$
\phi_{p,n}\leq C\deg (p)^{\beta}\sum_{\substack{q\in \mathcal{B}\\ \deg (q) > D(n) - \deg (p)}}\phi_{q,n}.
$$

Proof. By (2.3) we have

$$
\phi_ {p, n} = \left| \int_ {S (1)} f (\sqrt {n} \zeta) p (\zeta) d \zeta \right| \cdot \sup _ {\zeta \in S (1)} | p (\zeta) |.
$$

For$M \in \mathbb { Z } _ { \geq 0 }$we define the “head” of$f$as

$$
h_{M}:= \sum_{\substack{p\in \mathcal{B}\\ \deg (p)\leq M}}f_{p}
$$

and the “tail” as

$$
t_{M}:= \sum_{\substack{p\in \mathcal{B}\\ \deg (p) > M}}f_{p}.
$$

The integral in (2.3) can be written as

$$
\begin{array}{l} \int_ {S (1)} f (\sqrt {n} \zeta)   p (\zeta)   d \zeta = \\ \int_ {S (1)} (h _ {M} (\sqrt {n} \zeta) + t _ {M} (\sqrt {n} \zeta))   p (\zeta)   d \zeta . \end{array}
$$

For a finite set$Z \subset S ( 1 )$and a function$g : S ( 1 ) \to \mathbb { C }$we will use the notation

$$
\int_ {Y} g (\zeta) d \zeta := \frac {1}{| Y |} \sum_ {y \in Y} g (y).
$$

Suppose that the integer$M$is chosen so that$M + \deg ( p ) \leq D ( n )$. Then our assumption that the set$X _ { n }$is a spherical design of strength$D ( n )$implies that

$$
\begin{array}{l} \int_ {S (1)} h _ {M} (\sqrt {n} \zeta)) p (\zeta) d \zeta = \\ \int_ {X _ {n}} h _ {M} (\sqrt {n} \zeta) p (\zeta) d \zeta . \end{array}
$$

Thus, we can write the integral (2.2) as

$$
\begin{array}{l} \int_ {X _ {n}} h _ {M} (\sqrt {n} \zeta) p (\zeta) d \zeta + \int_ {S (1)} t _ {M} (\sqrt {n} \zeta) p (\zeta) d \zeta = \\ \int_ {X _ {n}} (f - t _ {M}) (\sqrt {n} \zeta) p (\zeta) d \zeta + \int_ {S (1)} t _ {M} (\sqrt {n} \zeta) p (\zeta) d \zeta = \\ \int_ {X _ {n}} f (\sqrt {n} \zeta) p (\zeta) d \zeta + \left(\int_ {S (1)} - \int_ {X _ {n}}\right) t _ {M} (\sqrt {n} \zeta) p (\zeta) d \zeta \end{array}\tag{5.1}
$$

The first summand in the above line vanishes by assumption that$f \mid _ { X _ { n } } = 0$. Therefore, we can estimate the integral (2.2) in the following way

$$
\left| \int_ {S (1)} f (\sqrt {n} \zeta) p (\zeta) d \zeta \right| \leq 2 \sup _ {\zeta \in S (1)} | p (\zeta) | \sup _ {x \in S (\sqrt {n})} | t _ {M} (x) |.\tag{5.2}
$$

We observe that

$$
\sup_{x\in S(\sqrt{n})}\left|t_{M}(x)\right|\leq \sum_{\substack{q\in \mathcal{B}\\ \deg (q) > M}}\phi_{q,n}.
$$

This finishes the proof of Lemma 5.1.

Theorems 3.1 and 3.2 give us other inequalities between the numbers$\begin{array} { r } { \left( \phi _ { p , n } \right) _ { p \in \mathcal { B } , n \in \mathbb { Z } _ { \geq 1 } } . } \end{array}$

Lemma 5.2. Fix$\epsilon \in ( 0 , 1 / 2 )$and set$N ( k ) : = \lfloor N ( k , \epsilon ) \rfloor$. Suppose that a Schwartz function$f$is an eigenfunction of the Fourier transform. There exists an absolute positive constant$C$big enough such that for all$p \in { \mathcal { B } }$and all positive integers$m \leq N ( \deg ( p ) + d / 2 )$we have

$$
\phi_{p,m}\leq C  m^{\alpha -\frac{d}{4}}\sum_{\substack{n\in \mathbb{Z}\\ n > N  (\deg (p) + d / 2)}}n^{\alpha +\frac{d}{4}}  \phi_{p,n}.
$$

Proof. Let$f$be a Schwartz function in$\mathbb { R } ^ { d }$. As described in Section 2 this function has decomposition

$$
f (x) = \sum_ {p \in \mathcal {B}} f _ {p} (x), \quad f _ {p} (x) = p (x) g _ {p} (| x |).
$$

Here for each homogenous harmonic polynomial$p \in { \mathcal { B } }$the function$g _ { p } : \mathbb { R } _ { \geq 0 } \to \mathbb { C }$is such that the function$x \mapsto g _ { p } ( | x | )$on$\mathbb { R } ^ { d }$is a radial Schwartz function. A known result in analysis implies that$x \mapsto g _ { p } ( | x | )$is a Schwartz function on any Euclidean space${ \mathbb { R } } ^ { s }$. We denote by $\mathcal { F } _ { s }$the$s$-dimensional Fourier transform. We have

$$
\mathcal {F} _ {d} (f _ {p}) (x) = \mathcal {F} _ {d} (p (x) g _ {p} (| x |)) = (- i) ^ {\deg (p)} p (y) \mathcal {F} _ {d + 2 \deg (p)} (g _ {p}) (| y |).
$$

Let$\{ h _ { m } \} _ { m = 1 } ^ { N ( d / 2 + \deg ( p ) ) } \subset S _ { d / 2 + \deg ( p ) } ( \Gamma ( 2 ) , \chi )$be the modular forms constructed in Theorem 3.2. By Theorem 3.1 for each integer$m$on the interval$[ 1 , \dots , N ( d / 2 + \deg ( p ) ) ]$ we have the following linear relation between values of$g _ { p }$:

$$
\sum_ {n = 1} ^ {\infty} g _ {p} (\sqrt {n}) c _ {h _ {m}} (n) = \sum_ {n = 1} ^ {\infty} \mathcal {F} _ {d + 2 \deg (p)} (g _ {p}) (\sqrt {n}) c _ {\widetilde {h} _ {m}} (n).
$$

Therefore for each point$\zeta$on the sphere �(1) we have

$$
\sum_ {n = 1} ^ {\infty} g _ {p} (\sqrt {n}) p (\sqrt {n} \zeta) n ^ {\frac {- \deg (p)}{2}} c _ {h _ {m}} (n) =
$$

$$
(- i) ^ {\deg (p)} \sum_ {n = 1} ^ {\infty} \mathcal {F} _ {d + 2 \deg (p)} (g _ {p}) (\sqrt {n}) p (\sqrt {n} \zeta) n ^ {\frac {- \deg (p)}{2}} c _ {\widetilde {h} _ {m}} (n).
$$

This is equivalent to

$$
\sum_ {n = 1} ^ {\infty} f _ {p} (\sqrt {n} \zeta) n ^ {\frac {- \deg (p)}{2}} c _ {h _ {m}} (n) = (- i) ^ {\deg (p)} \sum_ {n = 1} ^ {\infty} \widehat {f _ {p}} (\sqrt {n} \zeta) n ^ {\frac {- \deg (p)}{2}} c _ {\widetilde {h} _ {m}} (n).
$$

Conditions (1) and (2) of Theorem 3.2 imply that for an integer$m$in the interval$[ 1 , N ( d / 2 + \deg ( p ) )$and a point$\zeta$on the sphere$S ( 1 )$

$$
f _ {p} (\sqrt {m} \zeta) m ^ {\frac {- \deg (p)}{2}} = \sum_ {n = 1} ^ {\infty} \left(f _ {p} (\sqrt {n} \zeta) c _ {h _ {m}} (n) + (- i) ^ {\deg (p)} \widehat {f _ {p}} (\sqrt {n} \zeta) c _ {\widetilde {h} _ {m}} (n)\right) n ^ {\frac {- \deg (p)}{2}}.
$$

Now condition (3) of Theorem 3.2 and the assumption that$f$is an eigenfunction of the Fourier transform implies that

$$
\left| f _ {p} (\sqrt {m} \zeta) m ^ {\frac {- \deg (p)}{2}} \right| \leq C \sum_ {n = N (d / 2 + \deg (p)) + 1} ^ {\infty} \left| f _ {p} (\sqrt {n} \zeta) \right| n ^ {\frac {- \deg (p)}{2}} n ^ {\frac {d}{4} + \frac {\deg (p)}{2} + \alpha} m ^ {- \frac {d}{4} - \frac {\deg (p)}{2} + \alpha}.
$$

We set$\widetilde { \alpha } : = \alpha + d / 4$. For all$p \in { \mathcal { B } }$and all positive integers$m \leq N ( \deg ( p ) + d / 2 )$ we have

$$
\phi_{p,m}\leq C  m^{\widetilde{\alpha}}\sum_{\substack{n\in \mathbb{Z}\\ n > N(\deg (p) + d / 2)}}n^{\widetilde{\alpha}}\phi_{p,n}.
$$

Now we are ready for the final step in the proof of Theorem 1.4. In particular, we will define the function$D : \mathbb { Z } _ { \geq 1 } \to \mathbb { R } _ { \geq 0 }$. We will show that for a suitable choice of$D$the growth condition of Theorem 2.1 combined with the inequalities of Lemmas 5.1 and 5.2 implies the vanishing of the numbers$( \phi _ { p , n } ) _ { p \in \mathcal { B } , n \in \mathbb { Z } _ { \geq 0 } }$. We search for the function$D$in the form

$$
D (n) = \widetilde {B} n ^ {\widetilde {A}},
$$

where$\widetilde { A }$and$\widetilde { B }$are positive numbers. For each$\epsilon \in ( 0 , 1 / 2 )$there exists a suficiently small positive number$b$such that

$$
N (k, \epsilon) \geq b k, \quad k \in \frac {1}{2} \mathbb {Z} _ {\geq 1}
$$

For a polynomial$p \in { \mathcal { B } }$we set

$$
\mathcal {N} (p) := b \deg (p).
$$

Note that

$$
\mathcal {N} (p) \leq N (\deg (p) + d / 2).
$$

Let$C ^ { \prime }$and$\gamma$be positive numbers (depending on dimension$d )$such that dim$\mathcal { H } _ { m } \le C ^ { \prime } n ^ { \gamma }$ We will need the following technical statement.

Lemma 5.3. For each dimension$d$we consider$D ( n ) : = 2 \widetilde { B } n ^ { \widetilde { A } }$, where

$$
\widetilde {B} > 2 \max (b + \frac {1}{b}, \frac {C C ^ {\prime}}{b ^ {\beta + \gamma + 1}}), \quad \widetilde {A} = 2 \widetilde {\alpha} + \beta + \gamma + 2.
$$

Then

(1) for$p , q \in { \mathcal { B } }$and$n \in \mathbb { Z } _ { \geq 1 }$the conditions$n \geq N ( p )$and$\deg ( q ) \geq D ( n ) - \deg ( p )$ imply$n \leq N ( q )$

(2) for all positive integers$m$and all$q \in { \mathcal { B } }$with$m \geq N ( q )$we have

$$
\sum_{\substack{n\in \mathbb{Z}_{\geq 1},p\in \mathcal{B}:\\ n\geq \mathcal{N}(p)\\ D(n) - \deg (p)\leq \deg (q)}}C\cdot \deg (p)^{\beta}\cdot n^{2\widetilde{\alpha} +1} <   m.
$$

Proof. Part (1) of the lemma follows immediately from our choice of$\widetilde { A }$and${ \widetilde { B } } .$We rewrite the sum in the part (2) in the following way

$$
\sum_{\substack{n\in \mathbb{Z}_{\geq 1}, p\in \mathcal{B}:\\ n\geq \mathcal{N}(p)\\ D(n) - \deg (p)\leq \deg (q)}}C\cdot \deg (p)^{\beta}\cdot n^{2\widetilde{\alpha} +1}\leq \\ \sum_{\substack{n\in \mathbb{Z}_{\geq 1}\\ D(n) - \frac{n}{b}\leq \deg (q)}}\sum_{\substack{p\in \mathcal{B}:\\ \deg (p)\leq \frac{n}{b}\\ \deg (p)\geq D(n) - \deg (q)}}C\cdot \deg (p)^{\beta}\cdot n^{2\widetilde{\alpha} +1}.
$$

Now we use that$\begin{array} { r } { D ( n ) - \frac { n } { b } \geq \widetilde { B } n ^ { \widetilde { A } } } \end{array}$and estimate the above expression by

$$
\sum_{\substack{n\in \mathbb{Z}_{\geq 1}\\ \widetilde{B}  n^{\widetilde{A}}\leq \deg (q)}}\sum_{\substack{p\in \mathcal{B}:\\ \deg (p)\leq \frac{n}{b}\\ \deg (p)\geq D(n) - \deg (q)}}C\cdot \deg (p)^{\beta}\cdot n^{2\widetilde{\alpha} +1}.
$$

Next we use the fact that the dimension of$\mathcal { H } _ { \mathrm { d e g } ( p ) }$is bounded by$C ^ { \prime } \deg ( p ) ^ { \gamma }$and bound the sum in part (2) by

$$
\leq \sum_{\substack{n\in \mathbb{Z}_{\geq 1}\\ \widetilde{B}  n^{\widetilde{A}}\leq \frac{m}{b}}}\sum_{\substack{s\in \mathbb{Z}_{\geq 1}:\\ D(n) - \frac{m}{b}\leq s\leq \frac{n}{b}}}C  C^{\prime}  s^{\beta +\gamma}\cdot n^{2\widetilde{\alpha} +1}.
$$

This sum does not exceed

$$
\sum_{\substack{n\in \mathbb{Z}_{\geq 1}\\ n\leq \left(\frac{m}{b\widetilde{B}}\right)^{1 / \widetilde{A}}}}C  C^{\prime}\left(\frac{1}{b}\right)\left(\frac{1}{b}\right)^{\beta +\gamma}n^{2\widetilde{\alpha} +1}.
$$

Finally, we crudely estimate each term ofthis sum by substituting$\begin{array} { r } { n \mapsto \left( \frac { m } { b \widetilde { B } } \right) ^ { 1 / \widetilde { A } } } \end{array}$and bounding the number of terms by$\left( \frac { m } { b \widetilde { B } } \right) ^ { 1 / \widetilde { A } }$. This gives us an upper bound

$$
\frac {C C ^ {\prime}}{b ^ {\beta + \gamma}} \left(\frac {m}{b \widetilde {B}}\right) ^ {\frac {2 \widetilde {\alpha} + \beta + \gamma + 2}{\widetilde {A}}}.
$$

Now our choice of$\widetilde { A }$and$\widetilde { B }$guarantees that the sum in the part (2) of the lemma is less than$m$.

Suppose that$f : \mathbb { R } ^ { d } \to \mathbb { C }$is a Schwartz function that satisfies

$$
f \mid_ {X} \equiv 0 \qquad \text { and } \qquad \widehat {f} \mid_ {X} \equiv 0.\tag{5.3}
$$

Then for each$n \in \mathbb { Z } _ { \geq 1 }$we have

$$
f \mid_ {\sqrt {n} X _ {n}} = \widehat {f} \mid_ {\sqrt {n} X _ {n}} = 0.
$$

Without loss of generality we assume that$f$is an eigenfunction of the Fourier transform.

Consider the sum

$$
\sum_{\substack{p\in \mathcal{B}, n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)}}\phi_{p,n}n^{\widetilde{\alpha} +1}.\tag{5.4}
$$

By Theorem 2.1 this sum of non-negative numbers converges to a finite limit.

Suppose that a Schwartz function$f$satisfies vanishing conditions (5.3) and is an eigenfunction of the Fourier transform. Then by Lemma 5.1 we can estimate the sum (5.4)

$$
\sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)}}\phi_{p,n}  n^{\widetilde{\alpha} +1}\leq \sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)}}n^{\widetilde{\alpha} +1}  C  \deg (p)^{\beta}\cdot \sum_{\substack{q\in \mathcal{B}:\\ \deg (q) > D(n) - \deg (p)}}\phi_{q,n}.
$$

We have chosen the numbers$\widetilde { A }$and$\widetilde { B }$so that the conditions$n \geq N ( p )$and$\deg ( q ) \geq D ( n ) - \deg ( p )$ imply$n \leq N ( q )$. We apply Lemma 5.2 and estimate

$$
\sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)}}\phi_{p,n}  n^{\widetilde{\alpha} +1}\leq \sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)}}n^{\widetilde{\alpha} +1}  C  \deg (p)^{\beta}\cdot \\ \sum_{\substack{q\in \mathcal{B}:\\ \deg (q) > D(n) - \deg (p)}}\sum_{\substack{m\in \mathbb{Z}:\\ m\geq \mathcal{N}(q))}}m^{\widetilde{\alpha}}  n^{\widetilde{\alpha}}  \phi_{q,m}.
$$

Here � is a new constant and it is equal to the product of the constant$C$from Lemma 5.1 and the constant$C$from Lemma 5.2. We change the order of summation and arrive at

$$
\sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)}}\phi_{p,n}  n^{\widetilde{\alpha} +1}\leq \sum_{\substack{m\in \mathbb{Z},q\in \mathcal{B}:\\ m\geq \mathcal{N}(q))}}m^{\widetilde{\alpha}}  \phi_{q,m}\sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)\\ D(n) - \deg (p)\leq \deg (q)}}C  n^{2\widetilde{\alpha} +1}  \deg (p)^{\beta}.
$$

By Lemma 5.3 the inner sum on the right side of this inequality satisfies

$$
\sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq N(p)\\ D(n) - \deg (p)\leq \deg (q)}}C  n^{2\widetilde{\alpha} +1}\deg (p)^{\beta} <   m.
$$

This inequality is guaranteed by our choice of function$D$. Suppose that the non-negative numbers$( \phi _ { q , m } ) _ { m \in \mathbb { Z } , q \in \mathcal { B } }$are not all zero. Then

$$
\sum_{\substack{p\in \mathcal{B},n\in \mathbb{Z}:\\ n\geq \mathcal{N}(p)}}\phi_{p,n}  n^{\widetilde{\alpha} +1} <   \sum_{\substack{q\in \mathcal{B},m\in \mathbb{Z}:\\ m\geq \mathcal{N}(q)}}\phi_{q,m}  m^{\widetilde{\alpha} +1}.
$$

This is a contradiction. Therefore, our assumptions on the Schwartz function$f$imply that $\phi _ { q , m } = 0$whenever$m \geq N ( q )$. Moreover, Lemma 5.2 implies that$\phi _ { q , n } = 0$for all$q \in { \mathcal { B } }$ and$n \in \mathbb { Z } \geq 0$. Finally, we deduce from Theorem 1.2 that for all harmonic polynomials$p$in the basis B the functions$f _ { p }$in the decomposition (2.1) of the Schwartz function$f$vanish. Therefore,$f$is also identically zero. This finishes the proof of Theorem 1.4. □.

## Acknowledgments

I thank Martin Stoller and Joao Ramos for fruitful discussions and comments on the manuscript.

## Funding

The author is supported by SNSF grant.

## References

[1]Gradshteyn, Izrail Solomonovich; Ryzhik, Iosif Moiseevich; Geronimus, Yuri Veniaminovich; Tseytlin, Michail Yulyevich; Jefrey, Alan (2015) [October 2014]. "8.411.10.". In Zwillinger, Daniel; Moll, Victor Hugo (eds.). Table of Integrals, Series, and Products. Translated by Scripta Technica, Inc. (8 ed.). Academic Press, Inc. ISBN 978-0-12-384933-5. LCCN 2014010276.

[2]H. Iwaniec, Topics in classical authomorphic forms. Providence: American Math ematical Society, 1997.

[3]D. Radchenko, M. Viazovska, Fourier interpolation on the real line, preprint, 2017, arXiv:1701.00265

[4]M. Stoller, Fourier interpolationfrom spheres. Transactions ofthe American Mathematical Society (2021): 374(11), pp. 8045–8079.

[5]M. Stoller, J. P. G. Ramos, Perturbed Fourier uniqueness and interpolation results in higher dimensions, Journal of Functional Analysis (2022), Volume 282, Issue 12, 109448

## Maryna Viazovska

Institute of Mathematics, Ecole Polytechnique Federale de Lausanne, Lausanne, 1015, Switzerland, maryna.viazoivska@epfl.ch