# The sphere packing problem in dimension 24

By Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska

## Abstract

Building on Viazovska’s recent solution of the sphere packing problem in eight dimensions, we prove that the Leech lattice is the densest packing of congruent spheres in twenty-four dimensions and that it is the unique optimal periodic packing. In particular, we find an optimal auxiliary function for the linear programming bounds, which is an analogue of Viazovska’s function for the eight-dimensional case.

## 1. Introduction

The sphere packing problem asks how to arrange congruent balls as densely as possible without overlap between their interiors. The density is the fraction of space covered by the balls, and the problem is to find the maximal possible density. This problem plays an important role in geometry, number theory, and information theory. See [5] for background and references on sphere packing and its applications.

Although many interesting constructions are known, provable optimality is very rare. Aside from the trivial case of one dimension, the optimal density was previously known only in two [11], three [7], [8], and eight [12] dimensions, with the latter result being a recent breakthrough due to Viazovska; see [1], [9] for expositions. Building on her work, we solve the sphere packing problem in twenty-four dimensions:

Theorem 1.1. The Leech lattice achieves the optimal sphere packing density in$\mathbb { R } ^ { 2 4 }$, and it is the only periodic packing in$\mathbb { R } ^ { 2 4 }$with that density, up to scaling and isometries.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Miller’s research was supported by National Science Foundation grants DMS-1500562 and CNS-1526333.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">© 2017 by the authors. This paper may be reproduced, in its entirety, for noncommercial purposes.</span></small>

In particular, the optimal sphere packing density in$\mathbb { R } ^ { 2 4 }$is that of the Leech lattice, namely

$$
\frac {\pi^ {1 2}}{1 2 !} = 0. 0 0 1 9 2 9 5 7 4 3 \dots .
$$

For an appealing construction of the Leech lattice, see Section 2.8 of [6].

It is unknown in general whether optimal packings have any special structure, but our theorem shows that they do in$\mathbb { R } ^ { 2 4 }$. The optimality and uniqueness of the Leech lattice were previously known only among lattice packings [3], which is a far more restrictive setting. Recall that a lattice is a discrete subgroup of$\mathbb { R } ^ { n }$of rank$n ,$and a lattice packing uses spheres centered at the points of a lattice, while a periodic packing is the union of finitely many translates of a lattice. Lattices are far more algebraically constrained, and it is widely believed that they do not achieve the optimal density in most dimensions. (For example, see$[ 5 , \mathrm { p } . 1 4 0 ]$for an example in$\mathbb { R } ^ { 1 0 }$of a periodic packing that is denser than any known lattice.)$\mathrm { B y }$contrast, periodic packings at least come arbitrarily close to the optimal sphere packing density.

The proof of Theorem 1.1 will be based on the linear programming bounds for sphere packing, as given by the following theorem.

Theorem 1.2 (Cohn and Elkies [2]). Let$f \colon  { \mathbb { R } } ^ { n } \ \to \  { \mathbb { R } } ^ { n }$be a Schwartz function and r a positive real number such that$f ( 0 ) = { \widehat { f } } ( 0 ) = 1 , f ( x ) \leq 0$for $| x | \geq r$, and${ \widehat { f } } ( y ) \geq 0$for all$y .$Then the sphere packing density in$\mathbb { R } ^ { n }$is at most

$$
\frac {\pi^ {n / 2}}{(n / 2) !} \left(\frac {r}{2}\right) ^ {n}.
$$

Here$( n / 2 ) !$means$\Gamma ( n / 2 + 1 )$when n is odd, and the Fourier transform is normalized by

$$
\widehat {f} (y) = \int_ {\mathbb {R} ^ {n}} f (x) e ^ {- 2 \pi i \langle x, y \rangle} d x,
$$

where$\langle \cdot , \cdot \rangle$denotes the usual inner product on$\mathbb { R } ^ { n }$. Without loss of generality, we can radially symmetrize$f ,$in which case$\widehat { f }$is radial as well. We will often tacitly identify radial functions on$\mathbb { R } ^ { 2 4 }$with functions on$[ 0 , \infty )$and vice versa, by using$f ( r )$with$r \in [ 0 , \infty )$to denote the common value$f ( x )$with$| x | = r$ All Fourier transforms will be in$\mathbb { R } ^ { 2 4 }$unless otherwise specified. In other words, if f is a function of one variable defined on$[ 0 , \infty )$, then$\widehat { f } ( r )$means

$$
\int_ {\mathbb {R} ^ {2 4}} f (| x |) e ^ {- 2 \pi i \langle x, y \rangle} d x,
$$

where$y \in \mathbb { R } ^ { 2 4 }$satisfies$| y | = r$

Optimizing the bound from Theorem 1.1 requires choosing the right auxiliary function$f .$It was not previously known how to do so except in one dimension [2] or eight [12], but Cohn and Elkies conjectured the existence of an auxiliary function proving the optimality of the Leech lattice [2]. We prove this conjecture by developing an analogue for the Leech lattice of Viazovska’s construction for the$E _ { 8 }$root lattice.

In the case of the Leech lattice, proving optimality amounts to achieving $r = 2$, which requires that$f$and$\widehat { f }$have roots on the spheres of radius$\sqrt { 2 k }$ about the origin for$k = 2 , 3 , \ldots { } ,$. See [2] for further explanation and discussion of this condition. Furthermore, the argument in Section 8 of [2] shows that if $f$has no other roots at distance 2 or more, then the Leech lattice is the unique optimal periodic packing in$\mathbb { R } ^ { 2 4 }$. Thus, the proof of Theorem 1.1 reduces to constructing such a function.

The existence of an optimal auxiliary function in$\mathbb { R } ^ { 2 4 }$has long been anticipated, and Cohn and Miller made further conjectures in [4] about special values of the function, which we also prove. Our approach is based on a new connection with quasimodular forms discovered by Viazovska [12], and our proof techniques are analogous to hers. In Sections 2 and 3 we will build two radial Fourier eigenfunctions in$\mathbb { R } ^ { 2 4 }$, one with eigenvalue 1 constructed using a weakly holomorphic quasimodular form of weight −8 and depth 2 for$\operatorname { S L _ { 2 } } ( \mathbb { Z } )$ and one with eigenvalue −1 constructed using a weakly holomorphic modular form of weight −10 for the congruence subgroup$\Gamma ( 2 )$. We will then take a linear combination of these eigenfunctions in Section 4 to construct the optimal auxiliary function. Throughout the paper, we will make free use of the standard definitions and notation for modular forms from [12], [13].

## 2. The +1 eigenfunction

We begin by constructing a radial eigenfunction of the Fourier transform in$\mathbb { R } ^ { 2 4 }$with eigenvalue 1 in terms of the quasimodular form

$$
\begin{array}{l} \varphi = \frac {\left(2 5 E _ {4} ^ {4} - 4 9 E _ {6} ^ {2} E _ {4}\right) + 4 8 E _ {6} E _ {4} ^ {2} E _ {2} + \left(- 4 9 E _ {4} ^ {3} + 2 5 E _ {6} ^ {2}\right) E _ {2} ^ {2}}{\Delta^ {2}} \\ = - 3 6 5 7 8 3 0 4 0 0 q - 3 1 4 5 7 3 4 1 4 4 0 0 q ^ {2} - 1 3 7 1 6 8 6 4 0 0 0 0 0 0 q ^ {3} + O \big (q ^ {4} \big), \end{array}\tag{2.1}
$$

where$q = e ^ { 2 \pi i z }$and the variable z lies in the upper half plane. As mentioned in the introduction, we follow the notation of [12]. In particular,$E _ { k }$denotes the Eisenstein series

$$
E _ {k} (z) = 1 + \frac {2}{\zeta (1 - k)} \sum_ {n = 1} ^ {\infty} \sum_ {d \mid n} d ^ {k - 1} e ^ {2 \pi i n z},
$$

which is a modular form of weight k for$\operatorname { S L _ { 2 } } ( \mathbb { Z } )$when k is even and greater than 2 (and a quasimodular form when$k = 2 )$. Furthermore, we normalize$\Delta$ by

$$
\Delta = \frac {E _ {4} ^ {3} - E _ {6} ^ {2}}{1 7 2 8} = q - 2 4 q ^ {2} + 2 5 2 q ^ {3} + O (q ^ {4}).
$$

Recall that$\Delta$vanishes nowhere in the upper half plane.

This function$\varphi$is a weakly holomorphic quasimodular form of weight$^ { - 8 }$ and depth 2 for the full modular group. Specifically, because

$$
z ^ {- 2} E _ {2} \biggl (- \frac {1}{z} \biggr) = E _ {2} (z) - \frac {6 i}{\pi z},
$$

we have the quasimodularity relation

$$
z ^ {8} \varphi \biggl (- \frac {1}{z} \biggr) = \varphi (z) + \frac {\varphi_ {1} (z)}{z} + \frac {\varphi_ {2} (z)}{z ^ {2}},\tag{2.2}
$$

where

$$
\begin{array}{r l} \varphi_ {1} & = - \frac {6 i}{\pi} 4 8 \frac {E _ {6} E _ {4} ^ {2}}{\Delta^ {2}} - \frac {1 2 i}{\pi} \frac {E _ {2} (- 4 9 E _ {4} ^ {3} + 2 5 E _ {6} ^ {2})}{\Delta^ {2}} \\ & = \frac {i}{\pi} \left(7 2 5 7 6 0 q ^ {- 1} + 1 1 3 2 1 8 5 6 0 + 1 9 6 9 1 3 2 0 3 2 0 q + O (q ^ {2})\right) \end{array}
$$

and

$$
\begin{array}{l} \varphi_ {2} = - \frac {3 6 (- 4 9 E _ {4} ^ {3} + 2 5 E _ {6} ^ {2})}{\pi^ {2} \Delta^ {2}} \\ = \frac {1}{\pi^ {2}} \Big (8 6 4 q ^ {- 2} + 2 2 1 8 7 5 2 q ^ {- 1} + 2 2 3 1 4 0 0 9 6 + 2 3 3 6 8 1 1 7 2 4 8 q + O (q ^ {2}) \Big). \end{array}
$$

It follows from setting$z = i t$in (2.2) that

$$
\varphi (i / t) = O \left(t ^ {- 1 0} e ^ {4 \pi t}\right)\tag{2.3}
$$

as$t \to \infty ,$, while the q-series (2.1) for$\varphi$shows that

$$
\varphi (i / t) = O \bigl (e ^ {- 2 \pi / t} \bigr)\tag{2.4}
$$

as$t \to 0$. We define

$$
a (r) = - 4 \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {i \infty} \varphi \left(- \frac {1}{z}\right) z ^ {1 0} e ^ {\pi i r ^ {2} z} d z\tag{2.5}
$$

for$r > 2$, which converges absolutely by these bounds.

Lemma 2.1. The function$r \mapsto a ( r )$analytically continues to a holomorphic function on a neighborhood$o f \mathbb { R }$. Its restriction to R is a Schwartz function and a radial eigenfunction of the Fourier transform in$\mathbb { R } ^ { 2 4 }$with eigenvalue 1.

Proof. We follow the approach of [12], adapted to use modular forms of diferent weight. Substituting

$$
- 4 \sin (\pi r ^ {2} / 2) ^ {2} = e ^ {\pi i r ^ {2}} - 2 + e ^ {- \pi i r ^ {2}}
$$

yields

$$
\begin{array}{r l} & {a (r) = \int_ {- 1} ^ {i \infty - 1} \varphi \Bigl (- \frac {1}{z + 1} \Bigr) (z + 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i \infty} \varphi \Bigl (- \frac {1}{z} \Bigr) z ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad + \int_ {1} ^ {i \infty + 1} \varphi \Bigl (- \frac {1}{z - 1} \Bigr) (z - 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {= \int_ {- 1} ^ {i} \varphi \Bigl (- \frac {1}{z + 1} \Bigr) (z + 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad + \int_ {i} ^ {i \infty} \varphi \Bigl (- \frac {1}{z + 1} \Bigr) (z + 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad - 2 \int_ {0} ^ {i} \varphi \Bigl (- \frac {1}{z} \Bigr) z ^ {1 0} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {i} ^ {i \infty} \varphi \Bigl (- \frac {1}{z} \Bigr) z ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad + \int_ {1} ^ {i} \varphi \Bigl (- \frac {1}{z - 1} \Bigr) (z - 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad + \int_ {i} ^ {i \infty} \varphi \Bigl (- \frac {1}{z - 1} \Bigr) (z - 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z,} \end{array}
$$

where we have shifted contours as in the proof of Proposition 2 in [12]. Now the quasimodularity relation (2.2) and periodicity modulo 1 show that

$$
\begin{array}{l} \varphi \biggl (- \frac {1}{z + 1} \biggr) (z + 1) ^ {1 0} - 2 \varphi \biggl (- \frac {1}{z} \biggr) z ^ {1 0} + \varphi \biggl (- \frac {1}{z - 1} \biggr) (z - 1) ^ {1 0} \\ \qquad = \varphi (z + 1) (z + 1) ^ {2} - 2 \varphi (z) z ^ {2} + \varphi (z - 1) (z - 1) ^ {2} \\ \qquad + \varphi_ {1} (z + 1) (z + 1) - 2 \varphi_ {1} (z) z + \varphi_ {1} (z - 1) (z - 1) \\ \qquad + \varphi_ {2} (z + 1) - 2 \varphi_ {2} (z) + \varphi_ {2} (z - 1) \\ \qquad = 2 \varphi (z). \end{array}
$$

Thus,

$$
\begin{array}{r l} & {a (r) = \int_ {- 1} ^ {i} \varphi \Bigl (- \frac {1}{z + 1} \Bigr) (z + 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad + \int_ {1} ^ {i} \varphi \Bigl (- \frac {1}{z - 1} \Bigr) (z - 1) ^ {1 0} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad - 2 \int_ {0} ^ {i} \varphi \Bigl (- \frac {1}{z} \Bigr) z ^ {1 0} e ^ {\pi i r ^ {2} z} d z + 2 \int_ {i} ^ {i \infty} \varphi (z) e ^ {\pi i r ^ {2} z} d z,} \end{array}\tag{2.6}
$$

which gives the analytic continuation of a to a neighborhood of R by (2.3) and (2.4). Essentially the same estimates as in Proposition 1 of [12] show that it is a Schwartz function. Specifically, the exponential decay of$\varphi ( z )$as the imaginary part of z tends to infinity sufices to bound all the terms in (2.6), which shows that a and all its derivatives decay exponentially.

Taking the 24-dimensional radial Fourier transform commutes with the integrals in (2.6) and amounts to replacing$e ^ { \pi i r ^ { 2 } z }$with$z ^ { - 1 2 } e ^ { \pi i r ^ { 2 } ( - 1 / z ) }$. Therefore

$$
\begin{array}{r l} & {\widehat {a} (r) = \int_ {- 1} ^ {i} \varphi \biggl (- \frac {1}{z + 1} \biggr) (z + 1) ^ {1 0} z ^ {- 1 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z} \\ & {\qquad + \int_ {1} ^ {i} \varphi \biggl (- \frac {1}{z - 1} \biggr) (z - 1) ^ {1 0} z ^ {- 1 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z} \\ & {\qquad - 2 \int_ {0} ^ {i} \varphi \biggl (- \frac {1}{z} \biggr) z ^ {- 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z + 2 \int_ {i} ^ {i \infty} \varphi (z) z ^ {- 1 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z.} \end{array}
$$

Now setting$w = - 1 / z$shows that

$$
\begin{array}{l} \widehat {a} (r) = \int_ {1} ^ {i} \varphi \biggl (- 1 - \frac {1}{w - 1} \biggr) \left(- \frac {1}{w} + 1\right) ^ {1 0} w ^ {1 0} e ^ {\pi i r ^ {2} w} d w \\ \qquad + \int_ {- 1} ^ {i} \varphi \biggl (1 - \frac {1}{w + 1} \biggr) \left(- \frac {1}{w} - 1\right) ^ {1 0} w ^ {1 0} e ^ {\pi i r ^ {2} w} d w \\ \qquad + 2 \int_ {i} ^ {i \infty} \varphi (w) e ^ {\pi i r ^ {2} w} d w - 2 \int_ {0} ^ {i} \varphi \biggl (- \frac {1}{w} \biggr) w ^ {1 0} e ^ {\pi i r ^ {2} w} d w. \end{array}
$$

Thus, (2.6) and the fact that$\varphi$is periodic modulo 1 show that$\widehat { a } = a$, as desired.□

For$r > 2 .$, we have

$$
a (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} \varphi (i / t) t ^ {1 0} e ^ {- \pi r ^ {2} t} d t\tag{2.7}
$$

by (2.5). By the quasimodularity relation (2.2),

$$
t ^ {1 0} \varphi (i / t) = t ^ {2} \varphi (i t) - i t \varphi_ {1} (i t) - \varphi_ {2} (i t).\tag{2.8}
$$

Thanks to the q-expansions with$q = e ^ { - 2 \pi t }$, we have

$$
t ^ {1 0} \varphi (i / t) = p (t) + O \left(t ^ {2} e ^ {- 2 \pi t}\right)\tag{2.9}
$$

as$t \to \infty$, where

$$
p (t) = - \frac {8 6 4}{\pi^ {2}} e ^ {4 \pi t} + \frac {7 2 5 7 6 0}{\pi} t e ^ {2 \pi t} - \frac {2 2 1 8 7 5 2}{\pi^ {2}} e ^ {2 \pi t} + \frac {1 1 3 2 1 8 5 6 0}{\pi} t - \frac {2 2 3 1 4 0 0 9 6}{\pi^ {2}}.
$$

Let

$$
\begin{array}{r l} & {\widetilde {p} (r) = \int_ {0} ^ {\infty} p (t) e ^ {- \pi r ^ {2} t} d t} \\ & {\quad = - \frac {8 6 4}{\pi^ {3} (r ^ {2} - 4)} + \frac {7 2 5 7 6 0}{\pi^ {3} (r ^ {2} - 2) ^ {2}} - \frac {2 2 1 8 7 5 2}{\pi^ {3} (r ^ {2} - 2)} + \frac {1 1 3 2 1 8 5 6 0}{\pi^ {3} r ^ {4}} - \frac {2 2 3 1 4 0 0 9 6}{\pi^ {3} r ^ {2}}.} \end{array}
$$

Then

$$
a (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \left(\widetilde {p} (r) + \int_ {0} ^ {\infty} (\varphi (i / t) t ^ {1 0} - p (t)) e ^ {- \pi r ^ {2} t} d t\right)\tag{2.10}
$$

for$r > 2$. The integral

$$
\int_ {0} ^ {\infty} \left(\varphi (i / t) t ^ {1 0} - p (t)\right) e ^ {- \pi r ^ {2} t} d t
$$

is analytic on a neighborhood of$[ 0 , \infty )$, and hence (2.10) holds for all$^ { r } \cdot$Note in particular that a maps R to iR by (2.10) (or by (2.5) via analytic continuation).

Equation (2.10) implies that$a ( r )$vanishes to second order whenever$r =$ $\sqrt { 2 k }$with$k > 2 .$, because$\widetilde { p }$has no poles at these points. Furthermore, this formula implies that

$$
\begin{array}{c} a (0) = \frac {1 1 3 2 1 8 5 6 0 i}{\pi}, \\ a (\sqrt {2}) = \frac {7 2 5 7 6 0 i}{\pi}, \\ a ^ {\prime} (\sqrt {2}) = \frac {- 4 4 3 7 5 0 4 \sqrt {2} i}{\pi}, \\ a (2) = 0, \end{array}
$$

and

$$
a ^ {\prime} (2) = \frac {- 3 4 5 6 i}{\pi}.
$$

The Taylor series expansion is

$$
a (r) = \frac {1 1 3 2 1 8 5 6 0 i}{\pi} - \frac {2 2 3 1 4 0 0 9 6 i}{\pi} r ^ {2} + O \left(r ^ {4}\right)
$$

around$r = 0$

If we rescale a so that its value at 0 is 1, then the value at$\sqrt { 2 }$becomes $1 / 1 5 6$and the derivative there becomes$- 1 0 7 \sqrt { 2 } / 2 7 3 0$, and the derivative at 2 becomes$- 1 / 3 2 7 6 0$. The Taylor series becomes

$$
1 - \frac {3 5 8 7}{1 8 2 0} r ^ {2} + O (r ^ {4}).
$$

However, the higher order terms in this Taylor series do not appear to be rational, because they involve contributions from the integral in (2.10).

We arrived at the definition (2.1) of$\varphi$via the Ansatz that$\Delta ^ { 2 } \varphi$should be a holomorphic quasimodular form of weight 16 and depth 2 for$\operatorname { S L _ { 2 } } ( \mathbb { Z } )$ The space of such forms is five-dimensional, spanned by$E _ { 4 } ^ { 4 } , E _ { 6 } ^ { 2 } E _ { 4 } , E _ { 6 } E _ { 4 } ^ { 2 } E _ { 2 }$ $E _ { 4 } ^ { 3 } E _ { 2 } ^ { 2 }$, and$E _ { 6 } ^ { 2 } E _ { 2 } ^ { 2 }$. Within this space, one can solve for$\varphi$in several ways. We initially found it by matching the numerical conjectures from [4], but in retrospect one can instead impose constraints on its behavior at 0 and i∞, namely, (2.3) and (2.4). This information is enough to determine$\varphi$and hence the eigenfunction a, up to a constant factor.

## 3. The −1 eigenfunction

Next we construct a radial eigenfunction of the Fourier transform in$\mathbb { R } ^ { 2 4 }$ with eigenvalue −1. We will use the notation

$$
\begin{array}{l} \Theta_ {0 0} (z) = \sum_ {n \in \mathbb {Z}} e ^ {\pi i n ^ {2} z}, \\ \Theta_ {0 1} (z) = \sum_ {n \in \mathbb {Z}} (- 1) ^ {n} e ^ {\pi i n ^ {2} z}, \end{array}
$$

and

$$
\Theta_ {1 0} (z) = \sum_ {n \in \mathbb {Z}} e ^ {\pi i (n + 1 / 2) ^ {2} z}
$$

for theta functions from [12]. These functions satisfy the transformation laws

$$
\begin{array}{l l l} \Theta_ {0 0} ^ {4} | _ {2} S = - \Theta_ {0 0} ^ {4}, & \Theta_ {0 1} ^ {4} | _ {2} S = - \Theta_ {1 0} ^ {4}, & \Theta_ {1 0} ^ {4} | _ {2} S = - \Theta_ {0 1} ^ {4}, \\ \Theta_ {0 0} ^ {4} | _ {2} T = \Theta_ {0 1} ^ {4}, & \Theta_ {0 1} ^ {4} | _ {2} T = \Theta_ {0 0} ^ {4}, & \Theta_ {1 0} ^ {4} | _ {2} T = - \Theta_ {1 0} ^ {4}, \end{array}
$$

where$S = \left( { \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix} } \right) , \ T = \left( { \begin{matrix} 1 & 1 \\ 0 & 1 \end{matrix} } \right)$, and

$$
\big (g | _ {k} M \big) (z) = (c z + d) ^ {- k} g \bigg (\frac {a z + b}{c z + d} \bigg)
$$

for a function g on the upper half plane and a matrix$M = { \left( \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right) } \in { \mathrm { S L } } _ { 2 } ( \mathbb { R } )$

Let

$$
\begin{array}{r l} \psi_ {I} & = \frac {7 \Theta_ {0 1} ^ {2 0} \Theta_ {1 0} ^ {8} + 7 \Theta_ {0 1} ^ {2 4} \Theta_ {1 0} ^ {4} + 2 \Theta_ {0 1} ^ {2 8}}{\Delta^ {2}} \\ & = 2 q ^ {- 2} - 4 6 4 q ^ {- 1} + 1 7 2 1 2 8 - 3 6 7 0 0 1 6 q ^ {1 / 2} + 4 7 2 3 8 4 6 4 q \\ & - 4 5 9 2 7 6 2 8 8 q ^ {3 / 2} + O (q ^ {2}), \end{array}\tag{3.1}
$$

which is a weakly holomorphic modular form of weight −10 for Γ(2), and let

$$
\begin{array}{r} \psi_ {S} = \psi_ {I} | _ {- 1 0} S = - \frac {7 \Theta_ {1 0} ^ {2 0} \Theta_ {0 1} ^ {8} + 7 \Theta_ {1 0} ^ {2 4} \Theta_ {0 1} ^ {4} + 2 \Theta_ {1 0} ^ {2 8}}{\Delta^ {2}} \\ = - 7 3 4 0 0 3 2 q ^ {1 / 2} - 9 1 8 5 5 2 5 7 6 q ^ {3 / 2} + O (q ^ {5 / 2}) \end{array}\tag{3.2}
$$

and

$$
\begin{array}{c} \psi_ {T} = \psi_ {I} | _ {- 1 0} T = \frac {7 \Theta_ {0 0} ^ {2 0} \Theta_ {1 0} ^ {8} - 7 \Theta_ {0 0} ^ {2 4} \Theta_ {1 0} ^ {4} + 2 \Theta_ {0 0} ^ {2 8}}{\Delta^ {2}} \\ = 2 q ^ {- 2} - 4 6 4 q ^ {- 1} + 1 7 2 1 2 8 + 3 6 7 0 0 1 6 q ^ {1 / 2} \\ + 4 7 2 3 8 4 6 4 q + 4 5 9 2 7 6 2 8 8 q ^ {3 / 2} + O (q ^ {2}). \end{array}
$$

Note that$\psi _ { S } + \psi _ { T } = \psi _ { I }$, which follows from the Jacobi identity$\Theta _ { 0 1 } ^ { 4 } + \Theta _ { 1 0 } ^ { 4 } = \Theta _ { 0 0 } ^ { 4 }$

Using these q-expansions, we find that

$$
\psi_ {I} (i t) = O \big (e ^ {4 \pi t} \big)\tag{3.3}
$$

as$t \to \infty ,$, and

$$
\psi_ {I} (i t) = O \big (t ^ {1 0} e ^ {- \pi / t} \big)\tag{3.4}
$$

as$t \to 0$. Let

$$
b (r) = - 4 \sin \left(\pi r ^ {2} / 2\right) ^ {2} \int_ {0} ^ {i \infty} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z
$$

for$r > 2$, where the integral converges by the above bounds.

Lemma 3.1. The function$r \mapsto b ( r )$analytically continues to a holomorphic function on a neighborhood$o f \mathbb { R }$. Its restriction to R is a Schwartz function and a radial eigenfunction of the Fourier transform in$\mathbb { R } ^ { 2 4 }$with eigenvalue −1.

Proof. As in the proof of Proposition 6 from [12], we substitute

$$
- 4 \sin (\pi r ^ {2} / 2) ^ {2} = e ^ {- \pi i r ^ {2}} - 2 + e ^ {\pi i r ^ {2}}
$$

and shift contours to show that for$r > 2$,

$$
\begin{array}{l} b (r) = \int_ {- 1} ^ {i \infty - 1} \psi_ {I} (z + 1) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i \infty} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z \\ \qquad + \int_ {1} ^ {i \infty + 1} \psi_ {I} (z - 1) e ^ {\pi i r ^ {2} z} d z \\ \qquad = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z \\ \qquad + 2 \int_ {i} ^ {i \infty} (\psi_ {T} (z) - \psi_ {I} (z)) e ^ {\pi i r ^ {2} z} d z. \end{array}
$$

Here, we have used$\psi _ { I } ( z + 1 ) = \psi _ { I } ( z - 1 ) = \psi _ { T } ( z )$, and we have shifted the endpoints from$i \infty \pm 1$to i∞ (which is justified because the inequality $r \ > \ 2$ensures that the integrand decays exponentially). Finally, applying $\psi _ { T } - \psi _ { I } = - \psi _ { S }$yields

$$
\begin{array}{r} b (r) = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z \\ - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) e ^ {\pi i r ^ {2} z} d z, \end{array}
$$

which yields the analytic continuation to$r \ \leq \ 2$, and essentially the same estimates prove that it is a Schwartz function.

To show that the 24-dimensional radial Fourier transform$\widehat { b } \mathrm { s a t i s f i e s } \widehat { b } = - b .$ we follow the approach of Proposition 5 from [12]. As in the proof of Lemma 2.1,

$$
\begin{array}{r l} & {\widehat {b} (r) = \int_ {- 1} ^ {i} \psi_ {T} (z) z ^ {- 1 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z + \int_ {1} ^ {i} \psi_ {T} (z) z ^ {- 1 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z} \\ & {\qquad - 2 \int_ {0} ^ {i} \psi_ {I} (z) z ^ {- 1 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) z ^ {- 1 2} e ^ {\pi i r ^ {2} (- 1 / z)} d z,} \end{array}
$$

and the change of variables$w = - 1 / z$yields

$$
\begin{array}{r l} & {\widehat {b} (r) = \int_ {1} ^ {i} \psi_ {T} \Bigl (- \frac {1}{w} \Bigr) w ^ {1 0} e ^ {\pi i r ^ {2} w} d w + \int_ {- 1} ^ {i} \psi_ {T} \Bigl (- \frac {1}{w} \Bigr) w ^ {1 0} e ^ {\pi i r ^ {2} w} d w} \\ & {\qquad + 2 \int_ {i} ^ {i \infty} \psi_ {I} \Bigl (- \frac {1}{w} \Bigr) w ^ {1 0} e ^ {\pi i r ^ {2} w} d w + 2 \int_ {0} ^ {i} \psi_ {S} \Bigl (- \frac {1}{w} \Bigr) w ^ {1 0} e ^ {\pi i r ^ {2} w} d w.} \end{array}
$$

Finally,${ \widehat { b } } = - b$follows from the equations

$$
\psi_ {I} | _ {- 1 0} S = \psi_ {S}, \quad \psi_ {S} | _ {- 1 0} S = \psi_ {I}, \quad \mathrm{and} \quad \psi_ {T} | _ {- 1 0} S = - \psi_ {T},
$$

where the first two equations amount to the definition of$\psi _ { S }$and the third follows from$\psi _ { S } + \psi _ { T } = \psi _ { I }$□

For$r > 2$, we have

$$
b (r) = - 4 i \sin \left(\pi r ^ {2} / 2\right) ^ {2} \int_ {0} ^ {\infty} \psi_ {I} (i t) e ^ {- \pi r ^ {2} t} d t.\tag{3.5}
$$

From the q-expansion, we have

$$
\psi_ {I} (i t) = 2 e ^ {4 \pi t} - 4 6 4 e ^ {2 \pi t} + 1 7 2 1 2 8 + O \left(e ^ {- \pi t}\right)
$$

as$t \to \infty$, and

$$
\int_ {0} ^ {\infty} \left(2 e ^ {4 \pi t} - 4 6 4 e ^ {2 \pi t} + 1 7 2 1 2 8\right) e ^ {- \pi r ^ {2} t} d t = \frac {2}{\pi (r ^ {2} - 4)} - \frac {4 6 4}{\pi (r ^ {2} - 2)} + \frac {1 7 2 1 2 8}{\pi r ^ {2}}.
$$

Thus, for all$r \geq 0$

$$
\begin{array}{l} b (r) = - 4 i \sin \bigl (\pi r ^ {2} / 2 \bigr) ^ {2} \Bigl (\frac {2}{\pi (r ^ {2} - 4)} - \frac {4 6 4}{\pi (r ^ {2} - 2)} + \frac {1 7 2 1 2 8}{\pi r ^ {2}} \\ \qquad + \int_ {0} ^ {\infty} \bigl (\psi_ {I} (i t) - 2 e ^ {4 \pi t} + 4 6 4 e ^ {2 \pi t} - 1 7 2 1 2 8 \bigr) e ^ {- \pi r ^ {2} t} d t \Bigr), \end{array}
$$

by analytic continuation.

This formula implies that$b ( r )$vanishes to second order whenever$r = { \sqrt { 2 k } }$ with$k > 2$. Furthermore, it implies that

$$
\begin{array}{c} b (0) = b \big (\sqrt {2} \big) = b (2) = 0, \\ b ^ {\prime} \big (\sqrt {2} \big) = 9 2 8 i \pi \sqrt {2}, \end{array}
$$

and

$$
b ^ {\prime} (2) = - 8 \pi i.
$$

The Taylor series expansion is

$$
b (r) = - 1 7 2 1 2 8 \pi i r ^ {2} + O \left(r ^ {4}\right)
$$

around$r = 0$, and b maps$\mathbb { R }$to$i \mathbb { R } .$.

To obtain the definition (3.1) of$\psi _ { I }$, we began with the Ansatz that$\Delta ^ { 2 } \psi _ { I }$ should be a holomorphic modular form of weight 14 for$\Gamma ( 2 )$The space of such forms is eight-dimensional, spanned by$\Theta _ { 0 1 } ^ { 4 i } \Theta _ { 1 0 } ^ { 2 8 - 4 i }$with$i = 0 , 1 , \ldots , 7 ,$ and the subspace of forms satisfying the linear constraint$\psi _ { S } + \psi _ { T } = \psi _ { I }$is three-dimensional. As in the case of$\varphi$in Section 2, one can solve for$\psi _ { I }$in several ways. In particular, within the subspace satisfying$\psi _ { S } + \psi _ { T } = \psi _ { I } .$ the asymptotic behavior specified by (3.3) and (3.4) determines$\psi _ { I }$up to a constant factor.

## 4. Proof of Theorem 1.1

We can now construct the optimal auxiliary function for use in Theorem 1.2. Let

$$
f (r) = - \frac {\pi i}{1 1 3 2 1 8 5 6 0} a (r) - \frac {i}{2 6 2 0 8 0 \pi} b (r).
$$

Then$f ( 0 ) = { \widehat { f } } ( 0 ) = 1$, and the quadratic Taylor coeficients of$f$and$\widehat { f }$are $- 1 4 3 4 7 / 5 4 6 0$and$- 2 0 5 / 1 5 6$, respectively, as conjectured in [4]. The functions $f$and$\widehat { f }$have roots at all of the vector lengths in the Leech lattice, i.e.,$\sqrt { 2 k }$ for$k = 2 , 3 , \dots { } .$These roots are double roots except for the root of$f$at$^ { 2 , }$ where$f ^ { \prime } ( 2 ) = - 1 / 1 6 3 8 0$(in accordance with Lemma 5.1 in [4]). Furthermore, $f$has the value$1 / 1 5 6$and derivative$- 1 4 6 \sqrt { 2 } / 4 0 9 5$at${ \sqrt { 2 } }$, while$\widehat { f }$has the value$1 / 1 5 6$and derivative$- 5 { \sqrt { 2 } } / 1 1 7$there.

We must still check that$f$satisfies the hypotheses of Theorem 1.2. We will do so using the approach of [12], with one extra complication at the end.

For$r > 2$, equations (2.7) and (3.5) imply that

$$
f (r) = \sin \bigl (\pi r ^ {2} / 2 \bigr) ^ {2} \int_ {0} ^ {\infty} A (t) e ^ {- \pi r ^ {2} t} d t,
$$

where

$$
\begin{array}{r} A (t) = \frac {\pi}{2 8 3 0 4 6 4 0} t ^ {1 0} \varphi (i / t) - \frac {1}{6 5 5 2 0 \pi} \psi_ {I} (i t) \\ = \frac {\pi}{2 8 3 0 4 6 4 0} t ^ {1 0} \varphi (i / t) + \frac {1}{6 5 5 2 0 \pi} t ^ {1 0} \psi_ {S} (i / t). \end{array}
$$

To show that$f ( r ) \leq 0$for$r \geq 2$with equality only at$r$of the form$\sqrt { 2 k }$ with$k = 2 , 3 , \ldots$, it sufices to show that$A ( t ) \leq 0$. Specifically,$A$cannot be identically zero since then$f$would vanish as well; given that$A$is continuous, nonpositive everywhere, and negative somewhere, it follows that

$$
\int_ {0} ^ {\infty} A (t) e ^ {- \pi r ^ {2} t} d t <   0
$$

for all r for which it converges$( \mathrm { i . e . , } r > 2 )$

Because

$$
A (t) = \frac {\pi}{2 8 3 0 4 6 4 0} t ^ {1 0} \left(\varphi (i / t) + \frac {4 3 2}{\pi^ {2}} \psi_ {S} (i / t)\right),
$$

showing that$A ( t ) \leq 0$amounts to showing that

$$
\varphi (i t) + \frac {4 3 2}{\pi^ {2}} \psi_ {S} (i t) \leq 0.\tag{4.1}
$$

The formula

$$
\psi_ {S} = - \frac {7 \Theta_ {1 0} ^ {2 0} \Theta_ {0 1} ^ {8} + 7 \Theta_ {1 0} ^ {2 4} \Theta_ {0 1} ^ {4} + 2 \Theta_ {1 0} ^ {2 8}}{\Delta^ {2}}
$$

immediately implies that$\psi _ { S } ( i t ) \leq 0$, and so to prove (4.1) it sufices to prove that$\varphi ( i t ) \leq 0$. We prove this inequality in Lemma A.1 by bounding the truncation error in the q-series and examining the leading terms (splitting into the cases$t \geq 1$and$t \leq 1 )$. It follows that$f ( r ) \leq 0$for$r \geq 2$, as desired.

For$r > 2 .$, the analogous formula for$\widehat { f }$is

$$
\widehat {f} (r) = \sin \bigl (\pi r ^ {2} / 2 \bigr) ^ {2} \int_ {0} ^ {\infty} B (t) e ^ {- \pi r ^ {2} t} d t,\tag{4.2}
$$

where

$$
\begin{array}{r} B (t) = \frac {\pi}{2 8 3 0 4 6 4 0} t ^ {1 0} \varphi (i / t) + \frac {1}{6 5 5 2 0 \pi} \psi_ {I} (i t) \\ = \frac {\pi}{2 8 3 0 4 6 4 0} t ^ {1 0} \varphi (i / t) - \frac {1}{6 5 5 2 0 \pi} t ^ {1 0} \psi_ {S} (i / t). \end{array}\tag{4.3}
$$

To show that${ \widehat { f } } ( r ) \geq 0$for$r > 2 .$, it sufices to show that$B ( t ) \geq 0$for all$t \geq 0$ i.e.,

$$
\varphi (i t) - \frac {4 3 2}{\pi^ {2}} \psi_ {S} (i t) \geq 0,\tag{4.4}
$$

for the same reason as we saw above with A(t). This inequality is Lemma A.2.

The formula (4.2) in fact holds for$r > { \sqrt { 2 } }$, not just$r > 2$. To see why, we must examine the asymptotics of$B ( t )$. There is no problem with the integral in (4.2) as$t  0$, because$B ( t )$vanishes in this limit by (2.4) and (3.4). However, the exponential growth of$B ( t )$as$t$∞ causes divergence when$r$is too small for$e ^ { - \pi r ^ { 2 } t }$to counteract this growth. To estimate the growth rate, note that by (2.9) and (3.1), the$e ^ { 4 \pi t }$terms cancel in the asymptotic expansion of$B ( t )$as $t \to \infty ,$, which means that$B ( t ) = O \bigl ( t e ^ { 2 \pi t } \bigr )$Thus, the formula (4.2) for$\widehat { f } ( r )$ converges when$r > { \sqrt { 2 } }$, and it must equal$\widehat { f } ( r )$by analytic continuation. Note that it cannot hold for the whole interval$( 0 , \infty )$, because that would force$\widehat { f }$ to vanish at${ \sqrt { 2 } }$, which does not happen.

Thus, (4.2) and the inequality$B ( t ) \geq 0$in fact prove that${ \widehat { f } } \geq 0$for all $r \geq \sqrt { 2 }$. When$0 < r < { \sqrt { 2 } }$, this inequality no longer implies that${ \widehat { f } } ( r ) \geq 0$ which is a complication that does not occur in [12]. Instead, we must analyze $B ( t )$more carefully.$\mathrm { A s } \ t \to \infty .$equations (2.9) and (3.1) show that

$$
B (t) = \frac {1}{3 9} t e ^ {2 \pi t} - \frac {1 0}{1 1 7 \pi} e ^ {2 \pi t} + O (t).
$$

We will ameliorate this behavior by subtracting these terms over the interval $\lbrack 1 , \infty )$. They contribute

$$
\int_ {1} ^ {\infty} \left(\frac {1}{3 9} t e ^ {2 \pi t} - \frac {1 0}{1 1 7 \pi} e ^ {2 \pi t}\right) e ^ {- \pi r ^ {2} t} d t = \frac {(1 0 - 3 \pi) (2 - r ^ {2}) + 3}{1 1 7 \pi^ {2} (r ^ {2} - 2) ^ {2}} e ^ {- \pi (r ^ {2} - 2)},
$$

which is nonnegative for$0 < r < \sqrt { 2 }$, and the remaining terms

$$
\int_ {0} ^ {1} B (t) e ^ {- \pi r ^ {2} t} d t + \int_ {1} ^ {\infty} \left(B (t) - \frac {1}{3 9} t e ^ {2 \pi t} + \frac {1 0}{1 1 7 \pi} e ^ {2 \pi t}\right) e ^ {- \pi r ^ {2} t} d t
$$

converge for all$r > 0$. The integrand$B ( t )$in the first integral is nonnegative, and thus to prove that${ \widehat { f } } ( r ) \geq 0$for$0 < r < \sqrt { 2 }$it sufices to prove that

$$
B (t) \geq \frac {1}{3 9} t e ^ {2 \pi t} - \frac {1 0}{1 1 7 \pi} e ^ {2 \pi t}\tag{4.5}
$$

for$t \geq 1$, which is Lemma A.3.

Combining the results of this section shows that f satisfies the hypotheses of Theorem 1.2, and thus that the Leech lattice is an optimal sphere packing in$\mathbb { R } ^ { 2 4 }$. Furthermore, f has no roots$r > 2$other than$r = { \sqrt { 2 k } }$with$k =$ $2 , 3 , \ldots$, and as in Section 8 of [2] this condition implies that the Leech lattice is the unique densest periodic packing in$\mathbb { R } ^ { 2 4 }$. This completes the proof of Theorem 1.1.

## Appendix A. Inequalities for quasimodular forms

The proof in Section 4 requires checking certain inequalities for quasimodular forms on the imaginary axis. Fortunately, these inequalities are not too delicate, because equality is never attained. The behavior at infinity is easily analyzed, which reduces the proof to verifying the inequalities on a compact interval, and that can be done by a finite calculation.

Thus, these inequalities are clearly provable if true. The proof of the analogous inequalities in [12] used interval arithmetic, but in this appendix we take a diferent approach, based on applying Sturm’s theorem to truncated q-series. We have documented the calculations carefully, to facilitate checking the proof. Computer code for verifying our calculations is contained in the ancillary file appendix.txt. The code can be obtained at https://doi.org/10.4007/annals.2017.185.3.8, as well as at the arXiv.org e-print archive, where this paper is available as arXiv 1603.06518. Our code is for the free computer algebra system PARI/GP (see [10]), but the calculations are simple enough that they are not dificult to check in any computer algebra system.

To prove each inequality, we approximate the modular form using q-series and prove error bounds for truncating the series, which we then incorporate by adding them to an appropriate term of the truncated series. The result is nearly a polynomial in$q ,$with the possible exceptions being factors of t (where $z = i t )$, and we bound those factors so as to reduce to the case of a polynomial in$q .$. Furthermore, we bound any factors of$\pi$so that the coeficients become rational. Finally, we use Sturm’s theorem with exact rational arithmetic to verify that the truncated series never changes sign.

To prove the error bounds, we need to control the growth of the coeficients. We first multiply by$\Delta ^ { 2 }$to clear the denominators that appear in (2.1), (3.1), and (3.2). The advantage of doing so is that the coeficients of the numerator grow only polynomially. To estimate the growth rate, we bound the coeficient of$q ^ { n }$in$E _ { 2 }$by$2 4 ( n + 1 ) ^ { 2 }$in absolute value, in$E _ { 4 }$by$2 4 0 ( n + 1 ) ^ { 4 }$, and in$E _ { 6 }$by$5 0 4 ( n + 1 ) ^ { 6 }$. It is also not dificult to show that the coeficient of$q ^ { n / 2 }$ in$\Theta _ { 0 0 } ^ { 4 } , \Theta _ { 0 1 } ^ { 4 }$or$\Theta _ { 1 0 } ^ { 4 }$is at most$2 4 ( n + 1 ) ^ { 2 }$in absolute value.<sup>1</sup> Multiplying series is straightforward: if$| a _ { n } | \leq ( n + 1 ) ^ { \ell }$and$| b _ { n } | \leq ( n + 1 ) ^ { m }$, then the coeficients of $\begin{array} { r } { \left( \sum _ { n } a _ { n } q ^ { n } \right) \left( \sum _ { n } b _ { n } q ^ { n } \right) } \end{array}$are bounded by$( n + 1 ) ^ { \ell + m + 1 }$. When we add two q-series with coeficients bounded by diferent powers of$n + 1$, we typically produce an upper bound by rounding up the lower power for simplicity. Using these techniques leads to explicit polynomial bounds for the coeficients of$\varphi \Delta ^ { 2 } , \psi _ { I } \Delta ^ { 2 }$ and$\psi _ { S } \Delta ^ { 2 }$by using their definitions in terms of Eisenstein series and theta functions. These bounds are ineficient, but they sufice for our purposes.

When$t \geq 1 , q = e ^ { - 2 \pi t }$is small enough that these coeficient bounds yield a reasonable error term. When$t \leq 1$, we replace it with$1 / t \ ( \mathrm { v i a } \ z \mapsto - 1 / z )$ and compute the corresponding q-expansion.

Lemma A.1. For$t > 0$2

$$
\varphi (i t) <   0.
$$

Proof. First, we prove this inequality for$t \geq 1$, in which case$q = e ^ { - 2 \pi t } <$ $1 / 5 3 5$. The bounds described above show that the coeficient of$q ^ { n }$in$\varphi \Delta ^ { 2 }$is at most$5 1 3 2 0 0 6 5 5 3 6 0 ( n + 1 ) ^ { 2 0 }$in absolute value, and exact computation shows that

$$
\sum_ {n = 5 0} ^ {\infty} \frac {5 1 3 2 0 0 6 5 5 3 6 0 (n + 1) ^ {2 0}}{5 3 5 ^ {n - 6}} <   1 0 ^ {- 5 0}.
$$

Thus, the sum of the absolute values of the terms in$\varphi \Delta ^ { 2 }$for$n \geq 5 0$amounts to at most$1 0 ^ { - 5 0 } q ^ { 6 }$. Let$\sigma$be the sum of the terms with$n < 5 0$. We use Sturm’s theorem to check that$\sigma + { 1 0 ^ { - 5 0 } } { q ^ { 6 } }$never changes sign on$( 0 , 1 / 5 3 5 )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Both Θ<sup>4</sup><sub>00</sub> and Θ<sup>4</sup><sub>10</sub> have nonnegative coefficients, and their sum is the theta series of the D<sub>4</sub> root lattice in the variable q<sup>1/2</sup>, from which one can bound their coefficients. Furthermore, Θ<sup>4</sup><sub>01</sub> = Θ<sup>4</sup><sub>00</sub> − Θ<sup>4</sup><sub>10</sub>.</span></small>

as a polynomial in$q ,$and we observe that it is negative in the limit as$q \to 0$ This proves that$\varphi ( i t ) < 0$for$t \geq 1$

Using (2.8), the bound for$t \leq 1$is equivalent to showing that

$$
- t ^ {2} \varphi (i t) + i t \varphi_ {1} (i t) + \varphi_ {2} (i t) > 0
$$

for$t \geq 1$. Again we multiply by$\Delta ^ { 2 }$to control the coeficients. This case is more complicated, because there are factors of t and$\pi .$. We replace factors of π with rational bounds, namely$\lfloor 1 0 ^ { 1 0 } \pi \rfloor / 1 0 ^ { 1 0 }$or$\lceil 1 0 ^ { 1 0 } \pi \rceil / 1 0 ^ { 1 0 }$based on the sign of the term and whether it is a positive power of$\pi$(so that we obtain a lower bound), and we similarly use the bounds$1 \leq t \leq 1 / \left( 2 3 q ^ { 1 / 2 } \right)$; the latter bound follows from$q = e ^ { - 2 \pi t }$and$t e ^ { - \pi t } \leq e ^ { - \pi } \leq 1 / 2 3$. To estimate the error bound from truncation, we use$q ^ { 1 / 2 } < 1 / 2 3 ;$the result is that the error from omitting the$q ^ { n }$terms with$n \geq 5 0$is at most$1 0 ^ { - 5 0 } q ^ { 6 }$. These observations reduce the problem to showing that a polynomial in$q ^ { 1 / 2 }$with rational coeficients is positive over the interval$( 0 , e ^ { - \pi } )$. Using Sturm’s theorem, we check that it holds over the larger interval$( 0 , 1 / 2 3 )$.□

Note that we could have avoided fractional powers of$q$in this proof if we had used a diferent upper bound for$t ,$but fractional powers will be needed to handle$\psi _ { S }$and$\psi _ { I }$in any case. We will use the bounds such as$1 \leq t \leq$ $1 / ( 2 3 q ^ { 1 / 2 } )$from the preceding proof systematically in the remaining proofs.

Lemma A.2. For$t > 0$

$$
\varphi (i t) - \frac {4 3 2}{\pi^ {2}} \psi_ {S} (i t) > 0.
$$

Proof. We use exactly the same technique as in the proof of Lemma A.1. For$t \geq 1$, removing the$q ^ { 5 0 }$and higher terms in the q-series for$\left( \varphi - 4 3 2 \psi _ { S } / \pi ^ { 2 } \right) \Delta ^ { 2 }$ introduces an error of at most$1 0 ^ { - 5 0 } q ^ { 6 }$, and Sturm’s theorem shows that the resulting polynomial has no sign changes. Note that$\psi _ { S }$involves powers of $q ^ { 1 / 2 }$, and so we must view the truncated series as a polynomial in$q ^ { 1 / 2 }$rather than$q .$

For$t \leq 1$, we apply relations (2.2) and (3.2) to reduce the problem to showing that

$$
- t ^ {2} \varphi (i t) + i t \varphi_ {1} (i t) + \varphi_ {2} (i t) - \frac {4 3 2}{\pi^ {2}} \psi_ {I} (i t) <   0
$$

for$t \geq 1$. When we multiply by$\Delta ^ { 2 }$and remove the$q ^ { 5 0 }$and higher terms, the error bound is at most$1 0 ^ { - 5 0 } q ^ { 6 }$, and Sturm’s theorem completes the proof. As in the previous proof, this case involves handling factors of t and$\pi _ { \mathrm { : } }$but they present no dificulties.□

Of course these proofs are by no means optimized. Instead, they were chosen to be straightforward and easy to describe.

The final inequality we must verify is (4.5):

Lemma A.3. For all$t \geq 1$

$$
B (t) > \frac {1}{3 9} t e ^ {2 \pi t} - \frac {1 0}{1 1 7 \pi} e ^ {2 \pi t}.
$$

Proof. As usual, we multiply

$$
B (t) - \left(\frac {1}{3 9} t e ^ {2 \pi t} - \frac {1 0}{1 1 7 \pi} e ^ {2 \pi t}\right)
$$

by$\Delta ^ { 2 }$and compute its$q \mathrm { - }$-series. Our usual truncation bounds show that removing the$q ^ { 5 0 }$and higher terms introduces an error bound of at most$1 0 ^ { - 5 0 } q ^ { 6 }$, and Sturm’s theorem again completes the proof.□

## References

[1] H. Cohn, A conceptual breakthrough in sphere packing, Notices Amer. Math. Soc. 64 (2017), 102–115. arXiv 1611.01685. https://doi.org/10.1090/noti1474.

[2] H. Cohn and N. Elkies, New upper bounds on sphere packings. I, Ann. of Math. 157 (2003), 689–714. MR 1973059. Zbl 1041.52011. arXiv math/0110009. https://doi.org/10.4007/annals.2003.157.689.

[3] H. Cohn and A. Kumar, Optimality and uniqueness of the Leech lattice among lattices, Ann. of Math. 170 (2009), 1003–1050. MR 2600869. Zbl 1213.11144. arXiv math.MG/0403263. https://doi.org/10.4007/annals.2009.170.1003.

[4] H. Cohn and S. D. Miller, Some properties of optimal functions for sphere packing in dimensions 8 and 24, preprint, 2016. arXiv 1603.04759.

[5] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, third ed., Grundl. Math. Wissen. 290, Springer-Verlag, New York, 1999. MR 1662447. Zbl 0915.52003. https://doi.org/10.1007/978-1-4757-6568-7.

[6] W. Ebeling, Lattices and Codes, A course partially based on lectures by Friedrich Hirzebruch, third ed., Adv. Lect. Math., Springer-Verlag, New York, 2013. MR 2977354. Zbl 1257.11066. https://doi.org/10.1007/978-3-658-00360-9.

[7] T. C. Hales, A proof of the Kepler conjecture, Ann. of Math. 162 (2005), 1065–1185. MR 2179728. Zbl 1096.52010. https://doi.org/10.4007/annals.2005.162.1065.

[8] T. Hales, M. Adams, G. Bauer, D. T. Dang, J. Harrison, T. L. Hoang, C. Kaliszyk, V. Magron, S. McLaughlin, T. T. Nguyen, T. Q. Nguyen, T. Nipkow<sub>,</sub> S. Obua<sub>,</sub> J. Pleso<sub>,</sub> J. Rute<sub>,</sub> A. Solovyev<sub>,</sub> A. H. T. Ta<sub>,</sub> T. N. Tran, D. T. Trieu, J. Urban, K. K. Vu, and R. Zumkeller, A formal proof of the Kepler conjecture, to appear in Forum of Mathematics, Pi. arXiv 1501. 02155.

[9] D. de Laat and F. Vallentin, A breakthrough in sphere packing: the search for magic functions, Nieuw Arch. Wiskd. 17 (2016), 184–192. arXiv 1607.02111.

[10] The PARI Group, PARI/GP version 2.9.1, 2016, Univ. Bordeaux. Available at http://pari.math.u-bordeaux.fr/.

[11] A. Thue, Om nogle geometrisk-taltheoretiske Theoremer, Forhandlingerne ved de Skandinaviske Naturforskeres 14 (1892), 352–353. Zbl 24.0259.01.

[12] M. S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. 185 (2017), 991–1015. arXiv 1603.04246. https://doi.org/10.4007/annals.2017.185.3.7.

[13] D. Zagier, Elliptic modular forms and their applications, in The 1-2-3 of Modular Forms, Universitext, Springer-Verlag, New York, 2008, pp. 1–103. MR 2409678. Zbl 1259.11042. https://doi.org/10.1007/978-3-540-74119-0 1.

(Received: May 23, 2016)

Microsoft Research New England<sub>,</sub> Cambridge<sub>,</sub> MA E-mail : cohn@microsoft.com

Stony Brook University<sub>,</sub> Stony Brook<sub>,</sub> NY E-mail : thenav@gmail.com

Rutgers University<sub>,</sub> Piscataway<sub>,</sub> NJ E-mail : miller@math.rutgers.edu

Max Planck Institute for Mathematics<sub>,</sub> Bonn<sub>,</sub> Germany Current address : The Abdus Salam International Centre for Theoretical Physics<sub>,</sub> Trieste<sub>,</sub> Italy E-mail : danradchenko@gmail.com

Berlin Mathematical School and Humboldt University of Berlin,

Berlin<sub>,</sub> Germany

Current address : École Polytechnique Fédérale de Lausanne,

Lausanne<sub>,</sub> Switzerland

E-mail : viazovska@gmail.com