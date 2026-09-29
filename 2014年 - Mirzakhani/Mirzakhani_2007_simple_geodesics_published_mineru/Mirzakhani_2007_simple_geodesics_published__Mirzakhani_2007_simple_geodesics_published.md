# Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces

Maryam Mirzakhani

Department of Mathematics, Princeton University, Fine Hall, Washington Road, Princeton, NJ 08544, USA (e-mail: mmirzakh@math.princeton.edu)

Oblatum 19-VII-2005 & 17-VII-2006

Published online: 12 October 2006 – © Springer-Verlag 2006

## Contents

1 Introduction ..... 179
2 Background material ..... 186
3 Geometry of pairs of pants ..... 190
4 Generalized McShane identity for bordered surfaces ..... 194
5 Statement of the recursive formula for volumes ..... 203
6 Polynomial behavior of the Weil-Petersson volume ..... 206
7 Integration over the moduli space ..... 211
8 Volumes of moduli spaces of bordered Riemann surfaces ..... 217

## 1. Introduction

In this paper we investigate the Weil-Petersson volume of the moduli space of curves with marked points. We develop a method for integrating geometric functions over the moduli space of curves, and obtain an effective recursive formula for the volume${ \bar { V } } _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$of the moduli space$\mathcal { M } _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$of hyperbolic Riemann surfaces of genus g with n geodesic boundary components. We show that$V _ { g , n } ( L )$is a polynomial whose coefficients are rational multiples of powers of π. The constant term of the polynomial$V _ { g , n } ( L )$is the Weil-Petersson volume of the moduli space of closed surfaces of genus g with n marked points.

Volume of the moduli space of curves. When studying volumes of moduli spaces of hyperbolic Riemann surfaces with cusps, it proves fruitful to consider more generally bordered hyperbolic Riemann surfaces with geodesic boundary components. Given$L = ( L _ { 1 } , \ldots , L _ { n } ) \in ( \mathbb { R } _ { > 0 } ) ^ { n }$, the mapping class group$\mathbf { M o d } _ { g , n }$acts on the Teichmüller space${ \mathcal { T } } _ { g , n } ( L )$of hyperbolic structures with geodesic boundary components of length$L _ { 1 } , \ldots , L _ { n }$. We study the Weil-Petersson volume of the quotient space

$$
\mathcal {M} _ {g, n} (L) = \mathcal {T} _ {g, n} (L) / \mathrm{Mod} _ {g, n}.
$$

Our main result, obtained in Sect. 6, is:

Theorem 1.1. The volume$V _ { g , n } ( L _ { 1 } , \ldots , L _ { n } ) = \operatorname { V o l } _ { w p } ( \mathcal { M } _ { g , n } ( L ) )$is a polynomial in$L _ { 1 } ^ { 2 } , \ldots , L _ { n } ^ { 2 } ,$; namely we have:

$$
V_{g,n}(L) = \sum_{\substack{\alpha \\ |\alpha |\leq 3g - 3 + n}}C_{\alpha}\cdot L^{2\alpha},
$$

where$C _ { \alpha } > 0$lies in$\pi ^ { 6 g - 6 + 2 n - | 2 \alpha | } \cdot \mathbb { Q } .$

Here the exponent$\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ranges over elements in$( \mathbb { Z } _ { \geq 0 } ) ^ { n }$ $L ^ { \alpha } = L _ { 1 } ^ { \alpha _ { 1 } } \cdot \cdot \cdot L _ { n } ^ { \alpha _ { n } }$, and$| \alpha | = \sum _ { i = 1 } ^ { n } \alpha _ { i }$

Moreover, in Sect. 5 we give an explicit recursive formula for calculating these volumes. For example, we have:

$$
V _ {1, 1} (L) = L ^ {2} / 2 4 + \pi^ {2} / 6.
$$

For more examples, see Table 1.

In particular, the Weil-Petersson volume of the moduli space of curves of genus g with n marked points, i.e. the constant term of$V _ { g , n } ( L )$, is a rational multiple of$\pi ^ { 6 g - 6 + 2 n }$. This result was previously obtained by S. Wolpert [Wol2].

A closed formula for${ \mathrm { V o l } } _ { 0 , n } ( 0 )$, the Weil-Petersson volume of$\mathcal { M } _ { 0 , n }$, was obtained in [Zo].

Remark. Note that there is a small difference in the normalization of the volume form; in [Zo] the Weil-Petersson Kähler form is$1 / 2$the imaginary part of the Weil-Petersson pairing, while here the factor$1 / 2$does not appear. So our answers are different by a power of 2.

Table 1. Volumes of moduli spaces of curves

| g | n | $V_{g,n}(L)$ |
| --- | --- | --- |
| 0 | 3 | 1 |
| 1 | 1 | $\frac{1}{24}\left(L^{2}+4\pi^{2}\right)$ |
| 0 | 4 | $\frac{1}{2}\left(4\pi^{2}+L_{1}^{2}+L_{2}^{2}+L_{3}^{2}+L_{4}^{2}\right)$ |
| 1 | 2 | $\frac{1}{192}\left(4\pi^{2}+L_{1}^{2}+L_{2}^{2}\right)\left(12\pi^{2}+L_{1}^{2}+L_{2}^{2}\right)$ |
| 0 | 5 | $\frac{1}{8}\left(80\pi^{4}+\sum_{i=1}^{5}L_{i}^{4}+4\sum_{1\leq i<j\leq 5}L_{i}^{2}L_{j}^{2}+24\pi^{2}\sum_{i=1}^{5}L_{i}^{2}\right)$ |
| 2 | 1 | $\frac{1}{2211840}\left(4\pi^{2}+L_{1}^{2}\right)\left(12\pi^{2}+L_{1}^{2}\right)\left(6960\pi^{4}+384\pi^{2}L_{1}^{2}+5L_{1}^{4}\right)$ |

We approach the calculation of these volumes by studying the lengths of simple closed geodesics on$X \in \mathcal { M } _ { g , n }$. Our main tool is a generalization of McShane’s identity [M]. It gives us a way to calculate the volume of the moduli space$\mathcal { M } _ { g , n } = \mathcal { T } _ { g , n } / \mathrm { M o d } _ { g , n }$without having to find a fundamental domain for the action of the mapping class group on Teichmüller space.

McShane identity. Our point of departure for calculating these volume polynomials is the following result [M]:

Theorem 1.2 (McShane). Let X be a hyperbolic once-punctured torus. Then we have

$$
\sum_ {\gamma} (1 + e ^ {\ell_ {\gamma} (X)}) ^ {- 1} = \frac {1}{2},\tag{1.1}
$$

where the sum is over all simple closed geodesics γ on$X .$

Calculation of$\mathrm { V o l } ( \mathcal { M } _ { 1 , 1 } )$. We briefly explain the relation between Mc-Shane’s identity and Weil-Petersson volumes by treating the case$g = n = 1$ Consider the space of pairs:

$$
\mathcal {M} _ {1, 1} ^ {*} = \{(X, \gamma) \mid X \in \mathcal {M} _ {1, 1}, \gamma \text {   a   simple   closed   geodesic   on   } X \},
$$

and let

$$
\pi : \mathcal {M} _ {1, 1} ^ {*} \to \mathcal {M} _ {1, 1}
$$

be the projection map, defined by$\pi ( X , \gamma ) = X$. Also, define$\ell : \mathcal { M } _ { 1 , 1 } ^ { * } \to$R by

$$
\ell (X, \gamma) = \ell_ {\gamma} (X).
$$

Then we can rewrite (1.1) as

$$
\sum_ {\pi (Y) = X} f (\ell (Y)) = \frac {1}{2},\tag{1.2}
$$

where$f ( x ) = ( 1 + e ^ { x } ) ^ { - 1 }$

For any simple closed curve α on a hyperbolic once punctured torus, we have$\mathcal { M } _ { 1 , 1 } ^ { \ast } = \bar { \mathcal { T } } _ { 1 , 1 } / \mathrm { S t a b } ( \alpha )$. Now we use the Fenchel-Nielsen coordinates for$\mathcal { T } _ { 1 , 1 }$about α; any element$( X , \gamma ) \in \mathcal { M } _ { 1 , 1 } ^ { * }$is determined by the pair$( \ell , \tau )$ the length and the twisting parameter of X around$\gamma .$. Note that we have $\phi _ { \gamma } ( \ell , \tau ) = ( \ell , \ell + \tau )$, where$\phi _ { \gamma }$denotes a right Dehn twist around$\gamma$. Hence we have

$$
\mathcal {M} _ {1, 1} ^ {*} \cong \left\{(\ell , \tau) | 0 \leq \ell \leq \tau \right\} / (x, 0) \sim (x, x).
$$

On the other hand, the Weil-Petersson symplectic form in Fenchel-Nielsen coordinates is given by$\pi ^ { * } ( \omega _ { w p } ) = d \ell \wedge$dτ. Therefore, we have

$$
\int_ {\mathcal {M} _ {1, 1}} \sum_ {\pi (Y) = X} f (\ell (Y)) d X = \int_ {\mathcal {M} _ {1, 1} ^ {*}} f (\ell (Y)) d Y = \int_ {0} ^ {\infty} f (x) \int_ {0} ^ {x} 1 d y d x.
$$

Integrating McShane’s identity (1.2) over$\mathcal { M } _ { 1 , 1 }$against the Weil-Petersson volume form, we obtain

$$
\operatorname{Vol} \left(\mathcal {M} _ {1, 1}\right) = 2 \int_ {0} ^ {\infty} \ell f (\ell) d \ell = 2 \int_ {0} ^ {\infty} \frac {\ell}{1 + e ^ {\ell}} d \ell = \frac {\pi^ {2}}{6}.
$$

Calculation of$V _ { g , n }$. To carry out a similar analysis for${ \mathcal { M } } _ { g , n }$we will:

(I): Generalize McShane identity (Theorem 1.2) to arbitrary hyperbolic surfaces with geodesic boundary components (Sect. 4), and

(II): Develop a method to integrate functions given in terms of the hyperbolic length.

We now turn to a more detailed account of the two main steps in the proof:

(I): Generalized McShane’s identity. McShane [M] gives a version of formula (1.1) for punctured Riemann surfaces of higher genus. In our discussion, we need a further generalization to bordered Riemann surfaces with geodesic boundary components. Roughly speaking, we want to find a function defined on Teichmüller space such that the sum of its values over the elements of each orbit of$\mathbf { M o d } _ { g , n }$is a constant independent of the orbit. In Sect. 3 we introduce two auxiliary functions D,$\mathcal { R } : \mathbb { R } _ { + } ^ { 3 }  \mathbb { R } _ { + }$related to the geometry of hyperbolic pairs of pants. A central role in our approach to volumes of moduli spaces is played by the following result (Sect. 4):

Theorem 1.3. For any hyperbolic surface X with n geodesic boundary components$\beta _ { 1 } , \ldots , \beta _ { n }$of lengths$L _ { 1 } , \ldots , L _ { n }$, we have

$$
\sum_ {\{\gamma_ {1}, \gamma_ {2} \}} \mathcal {D} (L _ {1}, \ell_ {\gamma_ {1}} (X), \ell_ {\gamma_ {2}} (X)) + \sum_ {i = 2} ^ {n} \sum_ {\gamma} \mathcal {R} (L _ {1}, L _ {i}, \ell_ {\gamma} (X)) = L _ {1}.\tag{1.3}
$$

Here, the first sum is over all unordered pairs of simple closed geodesics $\{ \gamma _ { 1 } , \gamma _ { 2 } \}$bounding a pair ofpants with$\beta _ { 1 }$, and the second sum is over simple closed geodesics γ bounding a pair of pants with$\beta _ { 1 }$and$\beta _ { i }$.

In the formula above, we also allow$\beta _ { i }$to be a cusp of X, by regarding it as a geodesic of length 0.

As a special case, for any hyperbolic surface X of genus one with one geodesic boundary component of length L, we get

$$
\sum_ {\gamma} \mathcal {D} (L, \ell_ {\gamma} (X), \ell_ {\gamma} (X)) = L,\tag{1.4}
$$

where the sum is over all non-peripheral simple closed geodesics$\gamma$on$X$. On the other hand, we have (Sect. 3)

$$
\mathcal {D} (x, y, y) \sim \frac {2 x}{1 + e ^ {y}}
$$

as$x \to 0$. Therefore our formula for hyperbolic surfaces of genus one with one geodesic boundary component (equation (1.4)) implies the original McShane identity (1.1) when$L \to 0$

(II): Integration over the moduli space. In Sect. 7, we develop a method for integrating the right hand side of the identity for the lengths of simple closed geodesics (equation (1.3)) over${ \mathcal { M } } _ { g , n } ( L )$

Let$S _ { g , n }$be a closed surface of genus g with n boundary components and$Y \in \mathcal { T } _ { g , n }$. For any simple closed curve$\gamma$on$S _ { g , n }$, let [γ ] denote the homotopy class of$\gamma .$, and let$\ell _ { \gamma } ( Y )$denote the hyperbolic length of the geodesic representative of$[ \gamma ]$on Y.

To each simple closed curve$\gamma$on$S _ { g , n }$, we associate the set

$$
\mathcal {O} _ {\gamma} = \{[ \alpha ] | \alpha \in \operatorname{Mod} _ {g, n} \cdot \gamma \}
$$

of homotopy classes of simple closed curves in the$\mathbf { M o d } _ { g , n } { \mathrm { - o r b i t } }$of$\gamma$on $X \in \mathcal { M } _ { g , n }$. For any function$f : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$

$$
f _ {\gamma} (X) = \sum_ {[ \alpha ] \in \mathcal {O} _ {\gamma}} f (\ell_ {\alpha} (X))
$$

defines a function

$$
f _ {\gamma}: \mathcal {M} _ {g, n} \to \mathbb {R} _ {+}.
$$

Our goal is to calculate the integral of$f _ { \gamma }$over$\mathcal { M } _ { g , n }$with respect to the Weil-Petersson volume form. Here we consider the case when$\gamma$is a connected simple closed curve; see Theorem 7.1 for the general case.

First, consider the covering space of$\mathcal { M } _ { g , n }$

$\pi ^ { \gamma } : \mathcal { M } _ { g , n } ^ { \gamma } = \{ ( X , \alpha ) \ : | \ : X \in \mathcal { M } _ { g , n }$, and$\alpha \in \mathcal { O } _ { \gamma }$is a geodesic on$X \}  \mathcal { M } _ { g , n }$ where$\pi ^ { \gamma } ( X , \alpha ) \ = \ X$. The hyperbolic length function descends to the function

$$
\ell : \mathcal {M} _ {g, n} ^ {\gamma} \to \mathbb {R} _ {+}
$$

defined by$\ell ( X , \eta ) = \ell _ { \eta } ( X )$. Therefore, we have

$$
\int_ {\mathcal {M} _ {g, n}} f _ {\gamma} (X) d X = \int_ {\mathcal {M} _ {g, n} ^ {\gamma}} f \circ \ell (Y) d Y.
$$

On the other hand, the function$f$is constant on each level set of$\ell$and we have

$$
\int_ {\mathcal {M} _ {g, n} ^ {\gamma}} f \circ \ell (Y) d Y = \int_ {0} ^ {\infty} f (t) \mathrm{Vol} (\ell^ {- 1} (t)) d t,
$$

where the volume is taken with respect to the volume form induced on $\ell ^ { - 1 } ( t )$

The main idea for integrating over$\mathcal { M } _ { g , n } ^ { \gamma }$is that the decomposition of the surface along the simple closed curve$\gamma$gives rise to a description of $\mathcal { M } _ { g , n } ^ { \gamma }$in terms of moduli spaces corresponding to simpler surfaces. This observation leads to formulas for the integral of$f _ { \gamma }$in terms of the Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces and the function$f$as follows.

Let$S _ { g , n } ( \gamma )$denote the surface obtained by cutting the surface$S _ { g , n }$ along$\gamma ;$that is$S _ { g , n } ( \gamma ) \cong S _ { g , n } - U _ { \gamma }$, where$U _ { \gamma }$is an open neighborhood of$\gamma$ homeomorphic to$\gamma \times ( 0 , 1 )$. Thus$S _ { g , n } ( \gamma )$is a possibly disconnected compact surface with$n { + 2 }$boundary components. We define M$\mathbf { \xi } ( S _ { g , n } ( \gamma ) , \ell _ { \gamma } = t )$ to be the moduli space of Riemann surfaces homeomorphic to$S _ { g , n } ( \gamma )$such that the lengths of the 2 boundary components corresponding to$\gamma$are equal to t. We have a natural circle bundle

$$
\begin{array}{c} \ell^ {- 1} (t) \subset \mathcal {M} _ {g, n} ^ {\gamma} \\ \Big \downarrow \\ \mathcal {M} (S _ {g, n} (\gamma), \ell_ {\gamma} = t). \end{array}
$$

We will study the$S ^ { 1 }$-action on the level set$\ell ^ { - 1 } ( t ) \subset \mathcal { M } _ { g , n } ^ { \gamma }$induced by twisting the surface along$\gamma .$. The quotient space$\ell ^ { - 1 } ( t ) / S ^ { 1 }$inherits a symplectic form from the Weil-Petersson symplectic form. On the other hand, $\mathbf { \bar { \mathcal { M } } } ( S _ { g , n } ( \gamma ) , \ell _ { \gamma } = t )$is equipped with the Weil-Petersson symplectic form. By investigating these$S ^ { 1 }$-actions in more detail in Sect. 7 we show that

$$
\ell^ {- 1} (t) / S ^ {1} \cong \mathcal {M} (S _ {g, n} (\gamma), \ell_ {\gamma} = t)
$$

as symplectic manifolds. So we expect to have

$$
\operatorname{Vol} \left(\ell^ {- 1} (t)\right) = t \operatorname{Vol} \left(\mathcal {M} \left(S _ {g, n} (\gamma), \ell_ {\gamma} = t\right)\right).
$$

But as we will see in Sect. 7, the situation is different when$\gamma$separates off a one-handle in which case the length of the fiber of the$S ^ { 1 }$-action at a point is in fact$t / 2$instead of t. Hence, for any connected simple closed curve γ on$S _ { g , n }$, we have

$$
\int_ {\mathcal {M} _ {g, n}} f _ {\gamma} (X) d X = 2 ^ {- M (\gamma)} \int_ {0} ^ {\infty} f (t) t \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\gamma} = t)) d t,\tag{1.5}
$$

where$M ( \gamma ) = 1 \operatorname { i f } \gamma$separates off a one-handle, and$M ( \gamma ) = 0$otherwise.

An alternative proof of Theorem 1.1. The method of symplectic reduction can be used to show that$V _ { g , n } ( L )$is a polynomial in L. In a sequel [Mirz2], we obtain a formula for$V _ { g , n } ( \breve { L } )$in terms of intersection numbers of tautological classes over${ \overline { { \mathcal { M } } } } _ { g , n }$. However, this symplectic method does not lead us to a recursive algorithm for calculating the volumes explicitly.

Applications. In forthcoming papers, we will study the connection of the polynomial$V _ { g , n } ( L )$with the length distribution of simple closed geodesics on a hyperbolic surface [Mirz1]. We also relate the coefficients of the volume polynomial$V _ { g , n } ( L )$to intersection numbers of tautological line classes on$\overline { { \mathcal { M } } } _ { g , n } \left[ \mathrm { M i r z } 2 \right]$. The algorithm for calculating$V _ { g , n } ( L )$presented in Sect. 5 leads to a new proof of the Virasoro constraints for a point which is equivalent to the Witten-Kontsevich formula [K]. The discussion in [Mirz2] suggests some similarities between$\mathcal { M } _ { g , n }$and the variety${ \mathrm { H o m } } ( \pi _ { 1 } ( S ) , G ) / G$ of representations of the fundamental group of the oriented surface S in a compact Lie group G, up to conjugacy. See [D], [BL], and [JK].

In [LM], F. Labourie and G. McShane generalize the length identities to arbitrary cross ratios; as a result they obtain new identities for the Hitchin representations of surface groups in$S L ( n , \mathbb { R } )$

Notes and references. The Weil-Petersson volume of the moduli space of punctured Riemann surfaces arises naturally in different contexts [KMZ]. A recursive formula for the Weil-Petersson volume of the moduli space of punctured spheres was obtained by Zograf [Zo]. Moreover, Zograf and Manin have obtained generating functions for the Weil-Petersson volume of $\mathcal { M } _ { g , n } \left[ \mathrm { M a Z } \right]$. Also, R. Penner has developed a different method for calculating the Weil-Petersson volume of the moduli spaces of curves with marked points by using decorated Teichmüller theory [Pen]. The volume polynomial $V _ { 1 , 1 } ( L )$was also previously obtained in [NN] by finding a fundamental domain for the action of the mapping class group on Teichmüller space. It is possible to generalize the results of this paper for some hyperbolic surfaces with finitely many cone singularities [NN]. See [TWZ2] and [TWZ1] for generalizing McShane identities for surfaces with cone singularities.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Acknowledgements. I would like to thank Curt McMullen for his invaluable help and many stimulating discussions over the course of this work. I am also grateful to Said Akbari, Izzet Coskun, Chiu-Chu Melissa Liu, Andrei Okounkov, and Igor Riven for helpful discussions.</span></small>

I would like to thank Greg McShane and Scott Wolpert for many helpful comments and discussions. I would also like to thank the Max Planck Institute of Mathematics in Leipzig and the Institute for Studies in Theoretical Physics and Mathematics (IPM) in Tehran for their hospitality during the writing of this paper. I am grateful to the referee for many useful comments. The author is supported by a Clay fellowship.

## 2. Background material

In this section, we recall some basic facts and results in hyperbolic geometry and moduli spaces of bordered Riemann surfaces. See [IT] and [Bus] for more details.

Teichmüller space. A point in the Teichmüller space$\mathcal { T } ( S )$is a complete hyperbolic surface X equipped with a diffeomorphism$f : S  X$. The map f provides a marking on X by S. Two marked surfaces$f : S \to X$and $g : \ S \to Y$define the same point in$\mathcal { T } ( S )$if and only if$f \circ g ^ { - 1 } : Y \to X$ is isotopic to a conformal map. When ∂S is nonempty, consider hyperbolic Riemann surfaces homeomorphic to S with geodesic boundary components of fixed length. Let$A = \partial S$and$L = ( L _ { \alpha } ) _ { \alpha \in A } \in \mathbb { R } _ { + } ^ { | A | }$. A point$X \in \mathcal { T } ( S , L )$ is a marked hyperbolic surface with geodesic boundary components such that for each boundary component$\beta \in \partial S$, we have

$$
\ell_ {\beta} (X) = L _ {\beta}.
$$

Let$S _ { g , n }$be an oriented connected surface of genus g with n boundary components$( \beta _ { 1 } , \ldots , \beta _ { n } )$. Then let

$$
\mathcal {T} _ {g, n} (L _ {1}, \ldots , L _ {n}) = \mathcal {T} (S _ {g, n}, L _ {1}, \ldots , L _ {n})
$$

denote the Teichmüller space of hyperbolic structures on$S _ { g , n }$with geodesic boundary components of length$L _ { 1 } , \ldots , L _ { n }$. Let Mod(S) denote the mapping class group of S, or in other words the group of isotopy classes of orientation preserving self homeomorphisms of S leaving each boundary component set wise fixed. The mapping class group$\mathbf { M o d } _ { g , n } ^ { - } = \mathbf { M o d } ( S _ { g , n } )$ acts on${ \mathcal { T } } _ { g , n } ( L )$by changing the marking. The quotient space

$$
\mathcal {M} _ {g, n} (L) = \mathcal {M} (S _ {g, n}, \ell_ {\beta_ {i}} = L _ {i}) = \mathcal {T} _ {g, n} (L _ {1}, \dots , L _ {n}) / \operatorname{Mod} _ {g, n}
$$

is the moduli space of Riemann surfaces homeomorphic to$S _ { g , n }$with n boundary components of length$\ell _ { \beta _ { i } } = L _ { i }$

By convention, a geodesic of length zero is a cusp and we have

$$
\mathcal {T} _ {g, n} = \mathcal {T} _ {g, n} (0, \dots , 0),
$$

and

$$
\mathcal {M} _ {g, n} = \mathcal {M} _ {g, n} (0, \dots , 0).
$$

For a disconnected surface$\textstyle S = \bigcup _ { i = 1 } ^ { k } S _ { i }$such that$A _ { i } = \partial S _ { i } \subset \partial S$, we have

$$
\mathcal {M} (S, L) = \prod_ {i = 1} ^ {k} \mathcal {M} (S _ {i}, L _ {A _ {i}}),
$$

where$L _ { A _ { i } } = ( L _ { s } ) _ { s \in A _ { i } }$

The Weil-Petersson symplectic form. Recall that a symplectic structure on a manifold M is a non-degenerate closed 2-form$\omega \overset { \cdot } { \in } \dot { \Omega } ^ { 2 } ( M )$. The n-fold wedge product

$$
\frac {1}{n !} \omega \wedge \dots \wedge \omega
$$

never vanishes and defines a volume form on M. By work ofGoldman [Gol], the space$\mathcal { T } _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$carries a natural symplectic form invariant under the action of the mapping class group. This symplectic form is called Weil-Petersson symplectic form, and denoted by ω or$\omega _ { w p }$. In this paper, we are interested in calculating the volume of the moduli space with respect to the volume form induced by the Weil-Petersson symplectic form. Note that when S is disconnected, we have

$$
\operatorname{Vol} (\mathcal {M} (S, L)) = \prod_ {i = 1} ^ {k} \operatorname{Vol} (\mathcal {M} (S _ {i}, L _ {A _ {i}})).
$$

The Fenchel-Nielsen coordinates. A pants decomposition of S is a set of disjoint simple closed curves which decompose the surface into pairs of pants. Fix a system of pants decomposition of$S _ { g , n } , \mathcal { P } = \{ \alpha _ { i } \} _ { i = 1 } ^ { k }$, where $\bar { k } = 3 g - 3 + \bar { n }$. For a marked hyperbolic surface$\check { X } \in \mathcal { T } _ { g , n } ( L )$, the Fenchel-Nielsen coordinates associated with P,$\{ \ell _ { \alpha _ { 1 } } ( X ) , \ldots , \ell _ { \alpha _ { k } } ( X ) , \tau _ { \alpha _ { 1 } } ( X )$ $\dots , \tau _ { \alpha _ { k } } ( X ) \}$, consist of the set of lengths of all geodesics used in the decomposition and the set of the twisting parameters used to glue the pieces. We have an isomorphism [Bus]

$$
\mathcal {T} _ {g, n} (L) \cong \mathbb {R} _ {+} ^ {\mathcal {P}} \times \mathbb {R} ^ {\mathcal {P}}
$$

by the map

$$
X \to (\ell_ {\alpha_ {i}} (X), \tau_ {\alpha_ {i}} (X)).
$$

By work of Wolpert, over Teichmüller space the Weil-Petersson symplectic structure has a simple form in Fenchel-Nielsen coordinates [Wol1].

Theorem 2.1 (Wolpert). The Weil-Petersson symplectic form is given by

$$
\omega_ {w p} = \sum_ {i = 1} ^ {k} d \ell_ {\alpha_ {i}} \wedge d \tau_ {\alpha_ {i}}.
$$

Hamiltonian circle actions. Let$( M , \omega )$be a symplectic manifold$( M , \omega )$ Then for any smooth function$H : M \to \mathbb { R }$, the vector field$X _ { H }$determined by

$$
\omega (X _ {H},.) = d H (.)
$$

is called the Hamiltonian vectorfield associated to H. Let$\psi _ { t }$be the integral ofthe vector field$X _ { H }$. Here we are interested in the case where$X _ { H }$generates an$S ^ { 1 }$action on$M ;$; in this case,$\psi _ { 1 } = \mathrm { i d } ,$. The Hamiltonian function H in this case is called the moment map of the action. See [McD] for more details.

Twisting. Given a simple closed geodesic α on$X \in \mathcal { T } _ { g , n } ( L )$and$t \in \mathbb { R }$, one can deform X as follows. Cut the surface along α, turn the left hand side of α in the positive direction by distance t and reglue back. Let us denote the new surface by$\mathrm { t w } _ { \alpha } ^ { t } ( X )$. As t varies, the resulting continuous path in Teichmüller space is the Fenchel-Nielsen deformation of X along α. For $t = \ell _ { \alpha } ( X )$, we have

$$
\mathrm{tw} _ {\alpha} ^ {t} (X) = \phi_ {\alpha} (X),
$$

where$\phi _ { \alpha } \in \operatorname { M o d } ( S _ { g , n } )$is a right Dehn twist about$\alpha .$

By Wolpert’s result (Theorem 2.1), the vector field generated by twisting around α is symplectically dual to the exact one form$d \ell _ { \alpha }$. In other words, $\mathrm { t w } _ { \alpha } ^ { t }$is the Hamiltonian flow of the length function of$\alpha .$.

Splitting along a multicurve. We say$\textstyle \gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i }$is a multicurve on $S _ { g , n }$if$\gamma _ { i } \mathrm { { ' s } }$are disjoint, essential, non-peripheral simple closed curves, no two of which are in the same homotopy class, and$c _ { i } \geq 0$for$1 \leq i \leq k$. Fix

![](images/page_9_image_8.jpg)

Fig. 1

a multicurve$\gamma _ { : }$, and consider the surface$S _ { g , n } ( \gamma )$obtained by cutting$S _ { g , n }$ along$\gamma _ { 1 } , \ldots , \gamma _ { k }$. Then$S _ { g , n } ( \gamma )$is a (possibly disconnected) surface with $n + 2 k$boundary components and$s = s ( \gamma )$connected components. Each connected component$\gamma _ { i }$of$\gamma$gives rise to 2 boundary components,$\gamma _ { i } ^ { 1 }$and $\gamma _ { i } ^ { 2 }$on$S _ { g , n } ( \gamma )$, and we have

$$
\partial (S _ {g, n} (\gamma)) = \{\beta_ {1}, \dots , \beta_ {n} \} \cup \left\{\gamma_ {1} ^ {1}, \gamma_ {1} ^ {2}, \dots , \gamma_ {k} ^ {1}, \gamma_ {k} ^ {2} \right\}.
$$

Given$\boldsymbol { \Gamma } = ( \gamma _ { 1 } , \ldots , \gamma _ { k } ) , L = ( L _ { 1 } , \ldots , L _ { n } )$and$\mathbf { x } = ( x _ { 1 } , \ldots , x _ { k } ) \in \mathbb { R } _ { + } ^ { k }$ we consider the moduli space

$$
\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)
$$

of hyperbolic Riemann surfaces homeomorphic to$S _ { g , n } ( \gamma )$such that$\ell _ { \gamma _ { i } } = x _ { i }$ and$\ell _ { \beta _ { i } } = L _ { i }$. Also, we define$V _ { g , n } ( \Gamma , { \bf x } , \beta , L )$by

$$
V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) = \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)).
$$

The surface$S _ { g , n } ( \gamma )$can be written as a union of its connected components

$$
S _ {g, n} (\gamma) = \bigcup_ {i = 1} ^ {s} S _ {g _ {i}, n _ {i}}, A _ {i} = \partial S _ {i} \subset \mathcal {B},\tag{2.1}
$$

and we have

$$
\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L) \cong \prod_ {i = 1} ^ {s} \mathcal {M} _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}}),
$$

where$\ell _ { A _ { i } } = ( \ell _ { \alpha } ) _ { \alpha \in A _ { i } }$. Hence we get

$$
V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) = \prod_ {i = 1} ^ {s} V _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}}).
$$

Symmetry group of a multicurve. For a given set A of homotopy classes of simple closed curves on$S _ { g , n }$, Stab(A) is defined by

$$
\operatorname{Stab} (A) = \left\{h \in \operatorname{Mod} _ {g, n} \mid h \cdot A = A \right\} \subset \operatorname{Mod} _ {g, n}.
$$

Given a multicurve$\begin{array} { r } { \gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i } } \end{array}$, we define the symmetry group of$\gamma .$, $\operatorname { S y m } ( \gamma )$, by

$$
\operatorname{Sym} (\gamma) = \operatorname{Stab} (\gamma) / \cap_ {i = 1} ^ {k} \operatorname{Stab} (\gamma_ {i}).
$$

If$\alpha$is a connected simple closed curve, then$| \mathrm { S y m } ( \alpha ) | = 1 . \mathrm { I f } \alpha = \gamma _ { 1 } \cup \gamma _ { 2 }$ then

$$
| \operatorname{Sym} (\gamma_ {1} + \gamma_ {2}) | = 2
$$

if and only if$S _ { g , n } ( \gamma _ { 1 } )$is homeomorphic to$S _ { g , n } ( \gamma _ { 2 } )$. Here we consider the homeomorphisms which fix each boundary component of$\partial ( S _ { g , n } )$setwise, and send$\gamma _ { 1 }$to$\gamma _ { 2 }$

We remark that the condition$| \operatorname { S y m } ( \gamma ) | \neq 1$for$\textstyle \gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i }$imposes a nontrivial condition on the$c _ { i } ^ { \prime } \mathbf { s } ;$for example if$| \operatorname { S y m } ( { \overline { { \gamma ) } } } | = k !$then$c _ { 1 } =$ $c _ { 2 } = . . . = c _ { k }$

In this paper, we are mostly interested in the case where$\gamma = \gamma _ { 1 } + \gamma _ { 2 }$ bounds a pair of pants with a boundary component of$S _ { g , n }$. In this case, it is easy to check that$| \operatorname { S y m } ( \gamma _ { 1 } + \gamma _ { 2 } ) | = 2$if and only if either$S _ { g , n } ( \gamma )$is connected or

$$
S _ {g, n} (\gamma) \cong S _ {g _ {1}, 1} \cup S _ {g _ {1}, 1}.
$$

Simple closed curves on$X \in \mathcal { M } _ { g , n } . \operatorname { L e t } \left[ \gamma \right]$denote the homotopy class of a simple closed curve$\gamma$on$S _ { g , n }$. Although there is no canonical simple closed geodesic on$X \in \mathcal { M } _ { g , n }$corresponding to$[ \gamma ]$, the set

$$
\mathcal {O} _ {\gamma} = \{[ \alpha ] | \alpha \in \operatorname{Mod} \cdot \gamma \},
$$

of homotopy classes of simple closed curves in the Mod$_ { g , n }$-orbit of$\gamma$on$X ,$is determined by$\gamma$. In other words,$\mathcal { O } _ { \gamma }$is the set of$[ \phi ( \gamma ) ]$where$\phi : S _ { g , n } \to X$ is a marking of X. Let$\ell _ { \alpha } ( X )$denote the hyperbolic length of α on X. Here, we study functions of the form

$$
\begin{array}{c} f _ {\gamma}: \mathcal {M} _ {g, n} \to \mathbb {R} _ {+} \\ X \to \sum_ {\alpha \in \mathcal {O} _ {\gamma}} f (\ell_ {\alpha} (X)), \end{array}
$$

where$f : \mathbb { R } \to \mathbb { R } _ { + }$

As an example, for$f = \chi [ 0 , L )$, the characteristic function of$[ 0 , L )$ $f _ { \gamma } ( X )$is equal to the number of elements of$\mathcal { O } _ { \gamma }$of length less than L on X.

## 3. Geometry of pairs of pants

In this section we study infinite simple geodesic rays on a hyperbolic pair of pants. For background on hyperbolic geometry, see [Bus].

A pair ofpants is an oriented compact surface homeomorphic to$S _ { 0 , 3 }$ a surface of genus 0 with three boundary components.

Let$\mathcal { C } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$be the unique hyperbolic pair of pants with geodesic boundary curves$( \beta _ { i } ) _ { i = 1 } ^ { 3 }$such that$\ell _ { \beta _ { i } } ( \mathcal { C } ) = x _ { i } , i = 1 , 2 , 3$. We also allow the degenerate case in which one or more of the lengths vanish.

There are two canonical points on each boundary component of$\mathscr { C }$ namely the endpoints of the length-minimizing geodesics connecting it to the other two boundary components.

On the other hand, we can construct$\mathcal { C } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$by pasting two copies of the (unique) right angled geodesic hexagons with pairwise non-adjacent sides of length$x _ { 1 } / 2 , x _ { 2 } / 2$and$x _ { 3 } / 2$along the remaining three sides. Thus $\mathcal { C } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$admits a reflection involution$\sigma$which interchanges the two hexagons.

![](images/page_12_image_0.jpg)

Fig. 2

Complete geodesics on hyperbolic a pair of pants. A hyperbolic pair of pants contains$5$complete geodesics disjoint from$\beta _ { 2 } , \beta _ { 3 }$and orthogonal to$\beta _ { 1 }$. More precisely, two of these geodesics meet$\beta _ { 1 }$respectively at$y _ { 1 }$ and$y _ { 2 }$and spiral around$\beta _ { 3 }$, the other two meet$\beta _ { 1 }$respectively at$z _ { 1 }$ and$z _ { 2 }$and spiral around$\beta _ { 2 }$. There is also a unique common geodesic perpendicular from$\beta _ { 1 }$to itself meeting$\beta _ { 1 }$perpendicularly at two points, $w _ { 1 }$and$w _ { 2 }$. Note that we have$\sigma ( w _ { 1 } ) = w _ { 2 } , \sigma ( z _ { 1 } ) = z _ { 2 }$, and$\sigma ( y _ { 1 } ) = y _ { 2 }$ See Fig. 2.

Definitions. Define$\mathcal { R } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$to be the geodesic length of$( y _ { 1 } , y _ { 2 } )$, the interval between$y _ { 1 }$and$y _ { 2 }$on$\beta _ { 1 }$containing both$w _ { 1 }$and$w _ { 2 }$. In the universal cover of$\mathcal { C } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$

$$
x _ {1} - \mathcal {R} (x _ {1}, x _ {2}, x _ {3})
$$

is equal to the geodesic length of the projection of$\beta _ { 3 }$on$\beta _ { 1 }$. See Fig. 3. Note that this length does not depend on the choice of the lift of C in H.

Also, define$\mathcal { D } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$to be the sum of the geodesic length of$( y _ { 1 } , z _ { 1 } )$ and$( y _ { 2 } , z _ { 2 } )$. Here$( y _ { i } , z _ { i } )$is the interval between$y _ { i }$and$z _ { i }$containing$w _ { i }$ on$\beta _ { 1 } . S 0$the function$\mathcal { D } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$is twice the geodesic distance between two geodesics perpendicular to$\beta _ { 1 }$spiraling around$\beta _ { 2 }$and$\beta _ { 3 }$. Equivalently, in the universal cover of$\mathcal { C } , \mathcal { D } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$equals 2 times the distance between the projection of$\beta _ { 2 }$and$\beta _ { 3 }$on$\beta _ { 1 }$

Define the function$H : \mathbb { R } ^ { 2 }  \mathbb { R }$by

$$
H (x, y) = \frac {1}{1 + e ^ {\frac {x + y}{2}}} + \frac {1}{1 + e ^ {\frac {x - y}{2}}}.
$$

![](images/page_13_image_0.jpg)

Basic properties of D and$\mathcal { R }$. It can be easily checked that the functions $\mathcal { D }$and R satisfy

$$
\mathcal {D} (x _ {1}, x _ {2}, x _ {3}) = \mathcal {D} (x _ {1}, x _ {3}, x _ {2}),
$$

and

$$
\mathcal {R} (x _ {1}, x _ {2}, x _ {3}) + \mathcal {R} (x _ {1}, x _ {3}, x _ {2}) = x _ {1} + \mathcal {D} (x _ {1}, x _ {2}, x _ {3}).
$$

Moreover, one can explicitly calculate these functions and show that:

Lemma 3.1. Thefunctions$\mathcal { D }$and R are given by

$$
\mathcal {D} (x, y, z) = 2 \log \left(\frac {e ^ {\frac {x}{2}} + e ^ {\frac {y + z}{2}}}{e ^ {\frac {- x}{2}} + e ^ {\frac {y + z}{2}}}\right),\tag{3.1}
$$

and

$$
\mathcal {R} (x, y, z) = x - \log \left(\frac {\cosh \left(\frac {y}{2}\right) + \cosh \left(\frac {x + z}{2}\right)}{\cosh \left(\frac {y}{2}\right) + \cosh \left(\frac {x - z}{2}\right)}\right).\tag{3.2}
$$

Proof. It is enough to calculate$\mathcal { R } ( x , y , z )$. Using basic trigonometry (e.g. Theorem 2.3.1 of [Bus]), in any geodesic quadrilateral with three right angles and consecutive sides of lengths a, b, infinity and infinity (when one vertex is on the boundary at infinity), we have

$$
\operatorname{Sinh} (a) \cdot \operatorname{Sinh} (b) = 1.
$$

In Fig. 3, we can apply this equation for geodesic quadrilateral$r _ { 1 } r _ { 3 } p _ { 3 } p _ { 1 }$ and$r _ { 2 } r _ { 3 } p _ { 3 } p _ { 2 }$. Hence, we obtain

$$
\mathcal {R} (x _ {1}, x _ {2}, x _ {3}) = x _ {1} - 2 \operatorname{arcsinh} \left(\frac {1}{\sinh (d (\beta_ {1} , \beta_ {3}))}\right).
$$

On the other hand, by cutting the pairs of pants along the shortest geodesics joining distinct boundary components, we obtain two convex right-angled geodesic hexagons with consecutive sides of lengths$x _ { 1 } / 2 , d ( \beta _ { 1 } , \beta _ { 2 } ) , x _ { 2 } / 2$ $d ( \beta _ { 2 } , \beta _ { 3 } ) , x _ { 3 } / 2$and$d ( \beta _ { 3 } , \beta _ { 1 } )$. Hence the numbers$x _ { 1 } , x _ { 2 }$and$x _ { 3 }$uniquely determine$d ( \beta _ { 1 } , \beta _ { 3 } )$as follows. Therefore, we get

$$
\cosh (d (\beta_ {1}, \beta_ {3})) = \frac {\cosh \left(\frac {x _ {2}}{2}\right) + \cosh \left(\frac {x _ {3}}{2}\right) \cosh \left(\frac {x _ {1}}{2}\right)}{\sinh \left(\frac {x _ {3}}{2}\right) \sinh \left(\frac {x _ {1}}{2}\right)}.
$$

See Sect. 2 of [Bus] for more details.

Finally, we have

$$
\begin{array}{c} 2 \operatorname{arcsinh} \left(\frac {1}{\sinh (\alpha)}\right) = 2 \log \left(\frac {1}{\sinh (\alpha)} + \frac {\cosh (\alpha)}{\sinh (\alpha)}\right) \\ = \log \left(\frac {\cosh (\alpha) + 1}{\cosh (\alpha) - 1}\right). \end{array}
$$

Hence,

$$
\mathcal {R} (x _ {1}, x _ {2}, x _ {3}) = x _ {1} - \log \left(\frac {\cosh (d (\beta_ {1} , \beta_ {3}) + 1}{\cosh (d (\beta_ {1} , \beta_ {3})) - 1}\right),
$$

which implies equation (3.2).

See [LM] for a different proof of the preceding lemma.

Next lemma will allow us to simplify integrals involving functions D and R:

Lemma 3.2. The functions$\mathcal { D } , \mathcal { R } : \mathbb { R } _ { + }  \mathbb { R } _ { + }$satisfy the following equations:

$$
\frac {\partial}{\partial x} \mathcal {D} (x, y, z) = H (y + z, x),\tag{3.3}
$$

and

$$
\frac {\partial}{\partial x} \mathcal {R} (x, y, z) = \frac {1}{2} (H (z, x + y) + H (z, x - y)).\tag{3.4}
$$

Proof. Using equation (3.1), we have

$$
\frac {\partial}{\partial x} \mathcal {D} (x, y, z) = \frac {e ^ {x / 2}}{e ^ {x / 2} + e ^ {(y + z) / 2}} + \frac {e ^ {- x / 2}}{e ^ {- x / 2} + e ^ {(y + z) / 2}} = H (y + z, x).
$$

Using Lemma 3.1 one can show that

$$
\mathcal {D} (x, y, z) + \mathcal {D} (x, - y, z) = 2 \mathcal {R} (x, y, z).
$$

Therefore, equation (3.3) implies equation (3.4).

Asymptotic behavior of D and R. Functions D and$\mathcal { R }$are continuous on $\mathbb { R } _ { + } ^ { 3 } . \mathrm { ~ A s ~ } 0 \mathrm { ~ < ~ } \mathcal { D } ( x , y , z ) \mathrm { ~ \le ~ } x$and$0 < \mathcal { R } ( x , y , z ) \leq x .$, both$D ( x , y , z )$and $\mathcal { R } ( x , y , z )$go to zero when$x \to 0$. Using Lemma 3.2, it is easy to verify that

$$
\mathcal {D} (x, y, z) \sim x H (y + z, x) \sim \frac {2 x}{1 + e ^ {\frac {y + z}{2}}},\tag{3.5}
$$

$$
\mathcal {R} (x, y, z) \sim x \left(\frac {1}{1 + e ^ {\frac {z + y}{2}}} + \frac {1}{1 + e ^ {\frac {z - y}{2}}}\right).\tag{3.6}
$$

as$x \to 0 .$

Also, when x and y are fixed numbers, we have

$$
\mathcal {R} (x, y, z) \to 0,
$$

as$z  \infty$. Similarly, when x is a fixed number as

$$
\mathcal {D} (x, y, z) \to 0,
$$

y, z → ∞.

## 4. Generalized McShane identity for bordered surfaces

In this section, we discuss an identity for the lengths of certain types of simple closed geodesics on bordered hyperbolic Riemann surfaces with geodesic boundary components.

Embedded pairs ofpants. We say three isotopy classes ofconnected simple closed curves,$\alpha _ { 1 } , \alpha _ { 2 }$, and$\alpha _ { 3 }$on$S _ { g , n }$, bound a pair of pants if there exists an embedded pair of pants$\Sigma \subset S _ { g , n }$such that$\partial \Sigma = \{ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } \}$. Here$\alpha _ { i }$ may be a boundary component, and a closed geodesic of length 0 is a cusp.

The statement of Theorem 1.3 motivates the following definitions. For $1 \leq i \leq n$, let$\mathcal { F } _ { i }$denote the set of unordered pairs of isotopy classes of non-peripheral simple closed curves$\{ \gamma _ { 1 } , \gamma _ { 2 } \}$bounding a pair of pants with$\beta _ { i }$ Similarly, for$\bar { 1 } \leq i \neq j \leq n$, let$\mathcal { F } _ { i , j }$denote the set of isotopy classes of simple closed curves γ bounding a pair of pants containing$\beta _ { i }$and$\beta _ { j }$

An identity for lengths of simple closed geodesics. First we state an identity for lengths of simple closed geodesics on hyperbolic punctured surfaces due to G. McShane [M]:

Theorem 4.1. Let$\{ p _ { 1 } , \ldots , p _ { n } \}$be the set of punctures of$X \in \mathcal { T } _ { g , n }$. Then we have

$$
\sum_ {\{\gamma_ {1}, \gamma_ {2} \} \in \mathcal {F} _ {1}} \frac {1}{1 + e ^ {\frac {\ell \gamma_ {1} (X) + \ell \gamma_ {2} (X)}{2}}} + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \frac {1}{1 + e ^ {\frac {\ell \gamma (X)}{2}}} = \frac {1}{2}.
$$

We will use the properties of functions$\mathcal { D } , \mathcal { R } : \mathbb { R } _ { + } ^ { 3 }  \mathbb { R } _ { + }$, and the geometry of complete simple geodesics on a hyperbolic surface to get a similar result for hyperbolic bordered Riemann surfaces with geodesic boundary components:

Theorem 4.2 (Generalized McShane identity for bordered surfaces). For any$X \in { \mathcal { T } } _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$with$3 g - 3 + n > 0$, we have

$$
\sum_ {\{\gamma_ {1}, \gamma_ {2} \} \in \mathcal {F} _ {1}} \mathcal {D} (L _ {1}, \ell_ {\gamma_ {1}} (X), \ell_ {\gamma_ {2}} (X)) + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \mathcal {R} (L _ {1}, L _ {i}, \ell_ {\gamma} (X)) = L _ {1}.\tag{4.1}
$$

We remark that as$L _ { 1 } \to 0$both sides of equation (4.1) tend to zero and$\beta _ { 1 }$ becomes a puncture. Using equation (3.5) and equation (3.6), the following corollary is an immediate result of Theorem 4.2:

Corollary 4.3. For any$X \in { \mathcal { T } } _ { g , n } ( 0 , L _ { 2 } , \ldots , L _ { n } )$with$3 g - 3 + n > 0 ,$, we have

$$
\sum_ {\left\{\gamma_ {1}, \gamma_ {2} \right\} \in \mathcal {F} _ {1}} \frac {1}{1 + e ^ {\frac {\ell \gamma_ {1} (X) + \ell \gamma_ {2} (X)}{2}}} + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \frac {1}{2} \left(\frac {1}{1 + e ^ {\frac {\ell \gamma (X) + L _ {i}}{2}}} + \frac {1}{1 + e ^ {\frac {\ell \gamma (X) - L _ {i}}{2}}}\right) = \frac {1}{2}.\tag{4.2}
$$

Note that Corollary 4.3 implies Theorem 4.1.

Remark. To prove Theorem 4.2, we basically follow the proof presented in [M] almost line by line. See also [B] for a related result for the lengths of common orthogonals of two totally geodesic hypersurfaces on a hyperbolic manifold.

Union of complete simple geodesics. Let$E ( X ) \subset X$denote the union of all simple complete geodesics meeting one or two boundary components of X perpendicularly. Let$E _ { i } = E \cap \beta _ { i }$. Given$x \in E _ { i }$, let$\gamma _ { x }$, the geodesic emanating from x, denote the complete simple geodesic perpendicular to $\beta _ { i }$such that$x \in \gamma _ { x }$. Note that$\gamma _ { x }$may be a finite arc joining two boundary components perpendicularly.

Lemma 4.4. The set$E _ { i } \subset \beta _ { i }$, defined as above, has measure zero.

Proof. By a result due to Birman and Series [BS], the union of all complete geodesics on a closed surface has Hausdorff dimension 1. Doubling the bordered surface along its boundary components shows that the same statement holds for a bordered surface. That is$\mu ( E ) = 0$. Let$U _ { \beta _ { i } }$denote the collar neighborhood around$\beta _ { i }$. Then the set$E \cap U _ { \beta _ { i } }$has measure zero. On the other hand, we have

$$
\mu (E \cap U _ {\beta_ {i}}) = \sinh r \times \mu (E _ {i}),
$$

where r is the width of the collar neighborhood. So$\mu ( E \cap U _ { \beta _ { i } } ) = 0$implies that$\mu ( E _ { i } ) = 0$

Later we show that [M]:

Theorem 4.5. Each$E _ { i }$is homeomorphic to the Cantor set union countably many isolated points.

Characterization of boundary and isolated points in$E _ { i }$. In this part we will give a characterization of boundary and isolated points in$E _ { i }$. We say a lamination$\gamma$spirals to a lamination$\Omega ( \gamma )$iff$\Omega ( \gamma )$is in the closure of$\gamma$ It can be easily checked that when$\gamma$is a ray,$\Omega ( \gamma )$is actually a minimal lamination [CEG]. Note that for$x \in E _ { i }$, the corresponding simple geodesic ray,$\gamma _ { x }$falls into exactly one of the following two classes.

1. The other end spirals into a compact minimal lamination inside the surface, which will be denoted by$\Omega ( \gamma _ { x } )$

2. The other end also approaches a (not necessarily distinct) boundary component$\beta _ { i }$; either the ray$\gamma _ { x }$meets$\beta _ { i }$perpendicularly or spirals around it.

We will prove the following classification of points in$E _ { i }$in terms of the behavior of the corresponding complete simple geodesics [M]:

Theorem 4.6. For any$x \in E _ { i }$, exactly one of the following holds:

a) If the other end of$\gamma _ { x }$approaches a boundary component, then the point x is an isolated point of$E _ { i }$.

b)$H \Omega ( \gamma _ { x } )$is a simple closed curve inside the surface, then the point x is a boundary point of$E _ { i }$.

c)$H \Omega ( \gamma _ { x } )$is not a simple closed curve, then x is neither a boundary point nor an isolated point in$E _ { i }$

Simple arcs in embedded pairs of pants. There is a one-to-one correspondence between simple common perpendiculars between two (not necessarily distinct) boundary components$\beta _ { 1 }$and$\beta _ { j }$of$X$, and embedded pairs of pants containing$\beta _ { 1 }$and$\beta _ { j }$as follows.

As shown in Fig. 4, if$\gamma$is a simple arc joining two boundary components of the surface X, then there exists a unique embedded pair of pants on X containing$\gamma$and these (not necessarily distinct) boundary components. Conversely, if Σ is a pair of pants containing two (not necessarily distinct) boundary components$\beta _ { 1 }$and$\beta _ { j }$, then there exists a unique simple geodesic arc in$\Sigma$joining$\beta _ { 1 }$and$\beta _ { j }$perpendicularly; this is the shortest simple arc in Σ joining$\beta _ { 1 }$to$\beta _ { j }$.

![](images/page_17_image_12.jpg)

![](images/page_17_image_13.jpg)

Fig. 4

ProofofTheorem$4 . 6 ( a )$. Let$x _ { 1 } \in E _ { 1 }$be such that the other end of$\gamma _ { x _ { 1 } }$goes up to$\beta _ { 1 }$, and let$x _ { 2 } \in { \beta } _ { 1 }$be the other end of$\gamma _ { x _ { 1 } } ;$; so we have$\gamma _ { x _ { 1 } } \cap \beta _ { 1 } =$ $\{ x _ { 1 } , x _ { 2 } \}$. One can easily modify the argument for other cases. Let Σ denote the pair of pants containing$\gamma _ { x _ { 1 } }$such that$\partial \Sigma = \{ \beta _ { 1 } , \alpha _ { 1 } , \alpha _ { 2 } \}$, and both$\alpha _ { 1 }$ and$\alpha _ { 2 }$are non-peripheral simple closed curves.

There are exactly four infinite geodesic rays in Σ meeting$\beta _ { 1 }$perpendicularly at one point (as in Fig. 1). Let$\gamma _ { y _ { i } }$and$\gamma _ { z _ { i } }$be the ones spiraling around$\alpha _ { i }$for$i = 1 , 2$such that$x _ { 1 } \in E _ { 1 } \cap ( y _ { 1 } , y _ { 2 } )$and$x _ { 2 } \in E _ { 1 } \cap ( z _ { 1 } , z _ { 2 } )$ We claim that

$$
E _ {1} \cap (y _ {1}, y _ {2}) = x _ {1},
$$

and

$$
E _ {1} \cap (z _ {1}, z _ {2}) = x _ {2}.
$$

Assume$\gamma _ { z }$is a simple geodesic ray such that$z \not \in \{ x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } , z _ { 1 } , z _ { 2 } \}$ Then$\gamma _ { z }$must leave$\hat { \Sigma }$and hence it meets$\alpha _ { 1 } \cup \alpha _ { 2 }$. Without loss of generality, we can assume that$\gamma _ { z }$meets$\alpha _ { 1 }$first. In the universal cover of this pair of pants, as shown in Fig. 5, let$\tilde { \beta }$, joining$s _ { 1 }$and$\infty$, be a lift of$\beta _ { 1 }$. Also, let $\tilde { \alpha } _ { 1 }$, joining$r _ { 1 }$and$r _ { 2 }$, be the outermost lift of$\alpha _ { 1 }$meeting$\tilde { \gamma } _ { z }$. Consider$\psi _ { 1 }$ and$\psi _ { 2 }$, two geodesics perpendicular to$\tilde { \beta }$at$a _ { 1 }$and$a _ { 2 }$, and passing through the two endpoints of$\tilde { \alpha } _ { 1 }$. And let$\eta _ { 1 }$(resp.$\eta _ { 2 } )$be the piecewise geodesic path going from$\tilde { z }$to h along$\tilde { \gamma } _ { z }$and from h to$r _ { 1 }$(resp.$r _ { 2 } )$along$\tilde { \alpha } _ { 1 }$. As both $\alpha _ { 1 }$and$\gamma _ { z }$are simple on$X$, the projection of$\eta _ { 1 }$and$\eta _ { 2 }$are simple rays on the surface. On the other hand, since$\tilde { \alpha } _ { 1 }$is the outermost lift of$\alpha _ { 1 }$meeting $\gamma _ { z }$, the projections of$\eta _ { 1 }$and$\eta _ { 2 }$are disjoint from both$\alpha _ { 1 }$and$\alpha _ { 2 }$. Therefore, the projections are infinite simple geodesic rays on the pair of pants$\Sigma$

Furthermore,$\eta _ { 1 }$(resp.$\eta _ { 2 } )$is homotopic to$\psi _ { 1 }$(resp.$\psi _ { 2 } )$. This shows that the projections of$\psi _ { 1 }$and$\psi _ { 2 }$are complete simple geodesics on$\Sigma$. Since both$\psi _ { 1 }$and$\psi _ { 2 }$are asymptotic to a lift of$\alpha _ { 1 }$, their images spiral to$\alpha _ { 1 }$ Therefore$a _ { 1 }$and$a _ { 2 }$are actually pre-images of$z _ { 1 }$and$y _ { 1 }$. Also, for any $x \in [ a _ { 1 } , a _ { 2 } ]$the curve$\gamma _ { x }$meets$\alpha .$Therefore, we have$z \in [ y _ { 1 } , z _ { 1 } ]$

![](images/page_18_chart_8.jpg)

Next, assume that$\gamma _ { x }$spirals into a compact minimal lamination$\Omega ( \gamma _ { x } )$ The proof of part (b) is exactly the same as the proof of the corresponding statement for punctured surfaces in [M].

To prove part (c) of Theorem 4.6, we construct a sequence$\{ x _ { j } \} \subset E _ { i }$ getting close to x. So we need to approximate$\gamma _ { x }$with simple complete geodesics$\gamma _ { x _ { j } }$, and understand when the point$x _ { j }$lies on the right (left) side of x on$\beta _ { i }$.

Quasi-geodesics. Let$d ( x , y )$denote the hyperbolic distance between two points x,$y \in \mathbb { H } .$. Let$\alpha ( t )$be a path parameterized by arclength in the upper half plane H. We say α is a quasi-geodesic if there exists$k > 0$such that

$$
d (\alpha (s), \alpha (t)) > k | s - t |
$$

for all s and t. Recall that any quasi-geodesic is a bounded distance away from a unique geodesic. If L is much bigger than$\theta _ { : }$then any$( L , \theta )$polygon path α of segments of length at least L and bends at most$\theta < \pi$is a quasi-geodesic. See [CEG] for more details.

Now assume that$\tilde { \gamma }$is a geodesic perpendicular to a fixed geodesic$\tilde { \beta }$ in H such that$\tilde { \gamma } \cap \tilde { \beta } = \{ x \}$. Let$\tilde { \alpha }$be an$( L , \theta )$polygon path such that$\tilde { \alpha }$ and$\tilde { \beta }$also meet at x, and the straightening of$\tilde { \alpha }$meets$\tilde { \gamma }$in$x _ { \alpha }$. Then as $( L , \theta )  ( \infty , 0 )$the distance from$x _ { \alpha }$to x tends to zero. Moreover, if the bending angles are all positive (negative), then$x _ { \alpha }$is on the right (left) side of x on$\tilde { \beta }$. See Fig. 6.

![](images/page_19_image_7.jpg)

Fig. 6

![](images/page_20_image_0.jpg)

Fig. 7

Finding quasi-geodesics. In this part, we discuss a method for approximating$\gamma _ { x }$with simple complete geodesics using quasi-geodesics:

I): Good geodesic segments. Let$\alpha ( t )$be the arc length parameterization of a simple geodesic segment on X. Also let$c : [ 0 , 1 ] \to X$be a differentiable arc transverse to α such that

$$
c (0) = \alpha (t _ {0}), \quad c (1) = \alpha (t _ {1}),
$$

where$t _ { 0 } < t _ { 1 } \in \mathbb { R }$. We say that$( \alpha , t _ { 0 } , t _ { 1 } , c )$is an -good geodesic arc iff $\ell ( c ) \leq \epsilon .$

• The arc c is almost perpendicular to α, that is

$$
\begin{array}{l} \left| \angle (c ^ {\prime} (0), \alpha^ {\prime} (t _ {0})) - \frac {\pi}{2} \right| \leq \epsilon , \\ \left| \angle (c ^ {\prime} (1), \alpha^ {\prime} (t _ {1})) - \frac {\pi}{2} \right| \leq \epsilon , \end{array}
$$

and

• The arc c meets the geodesic arc α in only two points, that is we have

$$
c \cap \{\alpha (t) \mid t _ {0} \leq t \leq t _ {1} \} = \{\alpha (t _ {0}), \alpha (t _ {1}) \}.
$$

Consider the vectors$\alpha ^ { \prime } ( t _ { 0 } )$and$c ^ { \prime } ( 0 )$at point$c ( 0 ) = \alpha ( t _ { 0 } )$, and$\alpha ^ { \prime } ( t _ { 1 } )$and $c ^ { \prime } ( 1 )$at the point$c ( 1 ) = \alpha ( t _ { 1 } )$. If$( \alpha , t _ { 0 } , t _ { 1 } , c )$is a good geodesic segment, then the two tangent vectors to α at$\alpha ( t _ { 1 } )$and$\alpha ( t _ { 0 } )$are almost parallel. Therefore if$( \alpha , t _ { 0 } , t _ { 1 } , c )$is a good geodesic segment, then the orientations of$( \alpha ^ { \prime } ( t _ { 1 } ) , c ^ { \prime } ( 1 ) )$and$( \alpha ^ { \prime } ( t _ { 0 } ) , c ^ { \prime } ( 0 ) )$are the same. We say$( \alpha , t _ { 0 } , t _ { 1 } , c )$is positive (negative) if the orientation of the pair

$$
(\alpha^ {\prime} (t _ {0}), c ^ {\prime} (0))
$$

is the same as (different from) the orientation of the underlying surface. Note that positivity only depends on the image of α. In particular, it is independent of the parameterization of the path α.

II): Complete simple geodesics. Fix$x \in \beta _ { i }$. Let$( \alpha , t _ { 0 } , t _ { 1 } , c )$be an -good geodesic segment such that

$$
\alpha \cap \gamma_ {x} = \emptyset , \quad \gamma_ {x} \cap c [ 0, 1 ] \neq \emptyset ,
$$

and let

$$
t _ {2} = \inf \{t \mid \gamma_ {x} (t) \in c [ 0, 1 ] \}.
$$

Let$\psi ( \alpha , t _ { 0 } , t _ { 1 } , c )$denote the simple closed curve which goes along c from $\alpha ( t _ { 1 } )$to$\alpha ( t _ { 0 } )$, and then goes back to$\alpha ( t _ { 1 } )$along α. One can construct a complete simple curve, η, which starts at x, goes along$\gamma ( t )$for$t \ \leq \ t _ { 2 } .$ and then spirals around$\psi ( \alpha , t _ { 0 } , t _ { 1 } , c )$. It is easy to check that, possibly by changing the direction of$\alpha , \eta$will be a quasi-geodesic and consequently lie within a bounded distance of a unique complete simple geodesic. More precisely, we have:

## Lemma 4.7. Assume that

$$
c \cap \{\gamma_ {x} (t) \mid 0 \leq t <   t _ {2} \} = \emptyset .
$$

For any$\epsilon > 0$there exist$\delta , L > 0$such that if$( \alpha , t _ { 0 } , t _ { 1 } , c )$is a δ-good geodesic segment and$L \leq t _ { 1 } - t _ { 0 }$, then η is a simple quasi geodesic.$\bar { L } e t \widehat { \eta }$ denote the geodesic representative ofη and$y = \widehat { \eta } \cap \beta _ { i }$. Then

$$
d (y, x) <   \epsilon .
$$

Furthermore, y lies on the right$( l e f t )$side of x if and only$i f \left( \alpha , t _ { 0 } , t _ { 1 } , c \right)$is positive (negative).

Now we can prove that if$\Omega ( \gamma _ { x } )$is not a simple closed curve, then x is not a boundary point of$E _ { i }$.

Sketch of the proof of Theorem$4 . 6 ( c )$. Let$\lambda = \Omega ( \gamma _ { x } )$. The proof has two steps. First we show that if λ is not a simple closed curve, then one can find positive -good geodesic segments inside λ. This allows one to construct complete simple geodesics approximating$\gamma _ { x }$in the second step.

1. Given$y \in \lambda ,$, let$\phi _ { y }$denote the arc length parameterization of the leaf of λ such that$\phi _ { y } ( 0 ) = y$. We claim that for any ,$L > 0$there exist$0 < t ,$ a transverse arc c, and$y \in c \cap \lambda$such that:

$( \phi _ { y } , 0 , t , c )$is a positive -good geodesic segment,

$L \leq | t |$, and

• the points$y = \phi _ { y } ( 0 )$and$\phi _ { y } ( t )$are not boundary points in$\lambda \cap c$

To prove the claim, choose a transverse almost perpendicular arc$c _ { 1 }$ such that$\lambda \cap c _ { 1 } \neq \varnothing$. Since λ is not a simple closed curve,$\lambda \cap c _ { 1 }$is an uncountable set with only countably many boundary points [HP]. Therefore one can choose$x _ { 0 } \in \lambda \cap c _ { 1 }$so that$\phi _ { x _ { 0 } } \cap c _ { 1 }$does not contain any boundary points of$\lambda \cap c _ { 1 }$. Let$\phi = \phi _ { x _ { 0 } }$. Choose a small transverse subarc$c : [ - r , + r ]  X , \ r > 0 , \ c ( 0 ) = x _ { 0 }$such that for$\phi ( a ) \ \neq$ $\phi ( b ) \in c [ - r , r ]$, we have$| a - b | > L$. Without loss of generality, we can assume that the orientation of the pair

![](images/page_22_image_0.jpg)

$$
(\phi_ {0} ^ {\prime}, c _ {0} ^ {\prime})
$$

agrees with the orientation of X. Let

$$
t _ {1} = \inf \{t > 0 \mid \phi (t) \in c [ - r, 0) \}.
$$

Then there is a number$x _ { 1 }$such that$\phi ( t _ { 1 } ) = c ( x _ { 1 } )$. Similarly, as$\phi ( t _ { 1 } )$is not boundary point, there exists$t > t _ { 1 }$such that$\phi ( t ) \in c ( x _ { 1 } , 0 )$. Define

$$
t _ {2} = \inf \{t > t _ {1} \mid \phi (t) \in c (x _ {1}, 0) \}.
$$

As in Fig. 8, at least one of$( \phi , 0 , t _ { 1 } , c ) , ( \phi , t _ { 1 } , t _ { 2 } , c )$and$( \phi , 0 , t _ { 2 } , c )$is a positive -good geodesic segment. Also, we have

$$
\min \{| t _ {1} - t _ {2} |, t _ {1}, t _ {2} \} \geq L.
$$

2. Now let$( \alpha , t _ { 1 } , t _ { 2 } , c )$be an -good geodesic segment in λ such that $\alpha ( t _ { i } ) = c ( r _ { i } )$, and$\alpha ( t _ { 1 } )$is not a boundary point of$\lambda \cap c$

As$\gamma _ { x }$spirals to$\lambda , \gamma _ { x } \cap c [ r _ { 1 } , r _ { 2 } ]$is non-empty. Let

$$
t _ {0} = \inf \{t \mid \gamma_ {x} (t) \in c [ r _ {1}, r _ {2} ] \}.
$$

Now Lemma 4.7 implies the result.

A similar argument shows that one can find a sequence of complete simple geodesics approximating$\gamma _ { x }$from one side if$\Omega ( \gamma _ { x } )$is a non-peripheral simple closed curve. Hence in this case by the proof of part (a), x is a boundary point of$E _ { i }$

As a result, the set of non-isolated points of$E _ { i }$is topologically homeomorphic to the Cantor set.

Proof of Theorem 4.5. Recall that any perfect totally disconnected compact metric space is homeomorphic to the Cantor set [HY].

By Theorem 4.6, apart from countably many points, corresponding to the simple geodesics joining boundary components, points in$E _ { i }$are limit points. The result follows since non-isolated points of$E _ { i }$form a compact totally disconnected perfect subset of$\beta _ { i }$

Connection with embedded pairs of pants. Let$x \in E _ { i }$such that the ray $\gamma _ { x }$spirals into a simple closed geodesic$\alpha _ { 1 }$. Then it is easy to see that there is a unique embedded pair of pants$\Sigma _ { x }$on$X$such that$\gamma _ { x } \subset \Sigma _ { x }$. In other words, there exists a unique simple closed geodesic$\alpha _ { 2 }$bounding a pair of pants$\Sigma _ { x }$ with$\beta _ { i }$and$\alpha _ { 1 }$such that$\gamma _ { x } \subset \Sigma _ { x }$. The curve$\alpha _ { 2 }$could be peripheral.

Let$I _ { i }$be the set of isolated points in$E _ { i }$. Then we can write

$$
I _ {i} \cup (\beta_ {i} - E _ {i}) = \bigcup_ {h \in H} (a _ {h}, b _ {h}),
$$

where$H$is the set of connected components of$I _ { i } \cup ( \beta _ { i } - E _ { i } )$, and$a _ { h } , b _ { h }$ are the end points of$h \in H$; note that by the definition both$a _ { h }$and$b _ { h }$are boundary points of$E _ { i }$. There is a correspondence between embedded pairs of pants containing$\beta _ { i }$and elements of H as follows.

Fix$h \in H$, Theorem 4.6 implies that$\gamma _ { a _ { h } }$spirals into a non-peripheral simple closed curve. Let$\Sigma _ { h }$be the unique pair of pants containing$\gamma _ { a _ { h } }$such that

$$
\partial (\Sigma_ {h}) = \{\beta_ {i}, \Omega (\gamma_ {a _ {h}}), \alpha \}.
$$

We claim that$\gamma _ { b _ { h } } \subset \Sigma _ { h }$. First, assume that$\alpha$is non-peripheral. Then by Theorem 4.6,$\gamma _ { b _ { h } } \subset \Sigma _ { h }$; otherwise we could find$y \in ( a _ { h } , b _ { h } )$such that $\gamma _ { \mathrm { y } } \subset \Sigma _ { h }$spirals into α which is not possible. So$\alpha = \Omega ( \gamma _ { b _ { h } } )$which means that$\Omega ( \gamma _ { a _ { h } } ) , \Omega ( \gamma _ { b _ { h } } )$and$\beta _ { i }$bound a pair of pants.

Similarly the claim holds when$\alpha = \beta _ { j }$is a boundary component. In this case$\beta _ { i } , \beta _ { j }$and$\Omega ( \gamma _ { a _ { h } } ) = \Omega ( \gamma _ { b _ { h } } )$bound an embedded pair of pants inside the surface. Using this correspondence and Lemma 4.4, we prove the main result of this section.

Proof of Theorem 4.2. Let

$$
I _ {i} \cup (\beta_ {i} - E _ {i}) = \bigcup_ {h} (a _ {h}, b _ {h}),
$$

where$a _ { h } , b _ { h } \in \beta _ { i }$. Then by Lemma 4.4 we have:

$$
L _ {i} = \ell_ {\beta_ {i}} (X) = \sum_ {h \in H} | b _ {h} - a _ {h} |,\tag{4.3}
$$

where$\left| a _ { h } - b _ { h } \right|$is the geodesic distance between$a _ { h }$and$b _ { h }$along$\beta _ { i }$. Now by the preceding argument about the embedded pairs of pants, for each h exactly one of the following holds:

1. There exists$j \neq i$such that the three curves$\gamma = \Omega ( \gamma _ { a _ { h } } ) = \Omega ( \gamma _ { b _ { h } } ) , \beta _ { j }$ and$\beta _ { i }$bound a pair of pants in X. In this case, we have

$$
\mathcal {R} (L _ {i}, L _ {j}, \ell_ {\gamma} (X)) = | a _ {h} - b _ {h} |.\tag{4.4}
$$

2. The two curves$\gamma _ { 1 } = \Omega ( \gamma _ { a _ { h } } )$and$\gamma _ { 2 } = \Omega ( \gamma _ { b _ { h } } )$are distinct; in this case $\gamma _ { 1 }$and$\gamma _ { 2 }$bound a pair of pants containing$\beta _ { i }$. Moreover, we have:

$$
\frac {1}{2} \mathcal {D} (L _ {i}, \ell_ {\gamma_ {1}} (X), \ell_ {\gamma_ {2}} (X)) = | a _ {h} - b _ {h} |.\tag{4.5}
$$

Note that as in Sect. 3, there is another interval$( a _ { h ^ { \prime } } , b _ { h ^ { \prime } } ) \in H$such that $\Sigma _ { h } = \Sigma _ { h ^ { \prime } }$, and$| a _ { h } - b _ { h } | = | a _ { h ^ { \prime } } - b _ { h ^ { \prime } } |$; the ray$\gamma _ { a _ { h ^ { \prime } } }$spirals around$\Omega ( \gamma _ { a _ { h } } )$ in a different direction.

Using equation (4.4) and equation (4.5), we can rewrite equation (4.3) as

$$
L_{i}(X) = \sum_{\{\gamma_{1},\gamma_{2}\} \in \mathcal{F}_{i}}\mathcal{D}(L_{i},\ell_{\gamma_{1}}(X),\ell_{\gamma_{2}}(X)) + \sum_{\substack{j\\ j\neq i}}\sum_{\gamma \in \mathcal{F}_{i,j}}\mathcal{R}(L_{i},L_{j},\ell_{\gamma}(X)).
$$

## 5. Statement of the recursive formula for volumes

In this section we state a recursive formula for$V _ { g , n } ( L )$, the Weil-Petersson volume of$\mathcal { M } _ { g , n } ( L )$. The proof is given later in Sect. 8.

Observe that the volume function$V _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$is a symmetric function in$L _ { 1 } , \ldots , L _ { n }$. Given a set A of positive numbers$A = \{ a _ { 1 } , \ldots , a _ { n } \}$ define$V _ { g , n } ( A )$by

$$
V _ {g, n} (A) = V _ {g, n} \left(a _ {1}, \dots , a _ {n}\right).
$$

Statement of the recursive formula. The function$V _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$for any g and n$( 2 g - 2 + n > 0 )$is determined recursively as follows.

• For any$L _ { 1 } , L _ { 2 } , L _ { 3 } \geq 0$, set

$$
V _ {0, 3} (L _ {1}, L _ {2}, L _ {3}) = 1
$$

and

$$
V _ {1, 1} (L _ {1}) = \frac {L _ {1} ^ {2}}{2 4} + \frac {\pi^ {2}}{6}.
$$

The first equation holds since the moduli space$\mathcal { M } _ { 0 , 3 } ( L _ { 1 } , L _ { 2 } , L _ { 3 } )$consists of only one point. For the calculation of$V _ { 1 , 1 } ( L )$see Sect. 6.

• For$L = ( L _ { 1 } , \ldots , L _ { n } )$, let$\widehat { L } = ( L _ { 2 } , \ldots , L _ { n } )$. When$( g , n ) \neq ( 1 , 1 )$ $( 0 , 3 )$, the volume$V _ { g , n } ( L ) = \operatorname { V o l } ( \mathcal { M } _ { g , n } ( L ) )$satisfies

$$
\frac {\partial}{\partial L _ {1}} L _ {1} V _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L _ {1}, \widehat {L}) + \mathcal {A} _ {g, n} ^ {d c o n} (L _ {1}, \widehat {L}) + \mathcal {B} _ {g, n} (L _ {1}, \widehat {L}),\tag{5.1}
$$

where we have

$$
\mathcal {A} _ {g, n} ^ {c o n} (L _ {1}, \widehat {L}) = \frac {1}{2} \big (\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x y \widehat {\mathcal {A}} _ {g, n} ^ {c o n} (x, y, L _ {1}, \widehat {L}) d x d y \big),\tag{5.2}
$$

$$
\mathcal {A} _ {g, n} ^ {d c o n} (L _ {1}, \widehat {L}) = \frac {1}{2} \big (\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x y \widehat {\mathcal {A}} _ {g, n} ^ {d c o n} (x, y, L _ {1}, \widehat {L}) d x d y \big),\tag{5.3}
$$

and

$$
\mathcal {B} _ {g, n} (L _ {1}, \widehat {L}) = \int_ {0} ^ {\infty} x \cdot \widehat {\mathcal {B} _ {g , n}} (x, L _ {1}, \widehat {L}) d x.\tag{5.4}
$$

Now we define the functions

$$
\widehat {\mathcal {A}} _ {g, n} ^ {c o n}: \mathbb {R} _ {+} ^ {n + 2} \to \mathbb {R} _ {+},
$$

$$
\widehat {\mathcal {A}} _ {g, n} ^ {d c o n}: \mathbb {R} _ {+} ^ {n + 2} \to \mathbb {R} _ {+},
$$

and

$$
\widehat {\mathcal {B}} _ {g, n}: \mathbb {R} _ {+} ^ {n + 1} \to \mathbb {R} _ {+}.
$$

As in the introduction, let

$$
m (g, n) = \delta (g - 1) \times \delta (n - 1).
$$

So$m ( g , n ) = 0$unless$g = 1$and$n = 1$

I): Definition of$\widehat { \mathcal { A } } _ { g , n } ^ { c o n }$. Define$\widehat { \mathcal { A } } _ { g , n } ^ { c o n } : \mathbb { R } _ { + } ^ { n + 2 }  \mathbb { R } _ { + }$by

$$
\widehat {\mathcal {A}} _ {g, n} ^ {c o n} (x, y, L _ {1}, \dots , L _ {n}) = \frac {1}{2 ^ {m (g - 1 , n + 1)}} V _ {g - 1, n + 1} (x, y, \widehat {L}) \cdot H (x + y, L _ {1}).
$$

II): Definition of$\widehat { \mathcal { A } _ { g , n } } ^ { d c o n }$. Let$\tau _ { g , n }$be the set of ordered paris

$$
a = ((g _ {1}, I _ {1}), (g _ {2}, I _ {2})),
$$

where$I _ { 1 } , I _ { 2 } \subset \{ 2 , \ldots , n \}$and$0 \leq g _ { 1 } , g _ { 2 } \leq g$such that

1. the two sets$I _ { 1 }$and$I _ { 2 }$are disjoint and$\{ 2 , 3 , \dots , n \} = I _ { 1 } \sqcup I _ { 2 }$

2. the numbers$g _ { 1 } , g _ { 2 } \ge 0$and$n _ { 1 } = | I _ { 1 } | , n _ { 2 } = | I _ { 2 } |$satisfy

$$
2 \leq 2 g _ {1} + n _ {2},
$$

$$
2 \leq 2 g _ {2} + n _ {2},
$$

and

$$
g _ {1} + g _ {2} = g.
$$

For notational convenience, given$L = ( L _ { 1 } , \ldots , L _ { n } )$and$I \subset \{ 1 , \ldots , n \}$ with$| I | = k$, define$L _ { I }$by

$$
L _ {I} = (L _ {j _ {1}}, \dots , L _ {j _ {k}}),
$$

where$I = \{ j _ { 1 } , \ldots , j _ { k } \}$. Now for each

$$
a = ((g _ {1}, I _ {1}), (g _ {2}, I _ {2})) \in \mathfrak {I} _ {g, n},
$$

let

$$
V (a, x, y, \widehat {L}) = \frac {V _ {g _ {1} , n _ {1} + 1} (x , L _ {I _ {1}})}{2 ^ {m (g _ {1} , n _ {1} + 1)}} \times \frac {V _ {g _ {2} , n _ {2} + 1} (y , L _ {I _ {2}})}{2 ^ {m (g _ {2} , n _ {2} + 1)}}.
$$

As we will see later, the reason we have to divide by 2 in this case is that every$X \in \mathcal { M } _ { 1 , 1 } ( L )$is hyperelliptic.

Finally, define$\widehat { \mathcal { A } } _ { g , n } ^ { d c o n } : \mathbb { R } _ { + } ^ { n + 2 }  \mathbb { R } _ { + }$by

$$
\widehat {\mathcal {A}} _ {g, n} ^ {d c o n} (x, y, L _ {1}, \widehat {L}) = \sum_ {a \in \mathcal {I} _ {g, n}} V (a, x, y, \widehat {L}) \cdot H (x + y, L _ {1}).
$$

III): Definition of$\widehat { \mathcal { B } } _ { g , n }$. Define$\widehat { \mathcal { B } } _ { g , n } : \mathbb { R } _ { + } ^ { n + 1 } \to \mathbb { R } _ { + }$by

$$
\begin{array}{l} \widehat {\mathcal {B}} _ {g, n} (x, L _ {1}, \widehat {L}) = \frac {1}{2 ^ {m (g , n - 1)}} \sum_ {j = 2} ^ {n} \frac {1}{2} (H (x, L _ {1} + L _ {j}) + H (x, L _ {1} - L _ {j})) \\ \cdot V _ {g, n - 1} (x, L _ {2}, \dots , \widehat {L} _ {j}, \dots , L _ {n}). \end{array} \tag {5}\tag{5.5}
$$

Remark. The functions$\mathcal { A } _ { g , n } ^ { c o n } , \mathcal { A } _ { g , n } ^ { d c o n }$and${ \mathcal { B } } _ { g , n }$are determined by the functions$\{ V _ { i , j } \}$where$3 i + j < 3 g + n$. Therefore equation (5.1) is a recursive formula for calculating$V _ { g , n } ( L )$. In Sect. 6 we will simplify this recursive formula and use it to prove that$V _ { g , n } ( L )$is a polynomial in L (Theorem 1.1).

Connection with topology of the set of pairs of pants. The recursive formula 5.1 is closely related to the topology of different types of embedded pairs of pants in$S _ { g , n }$. In fact, this formula gives us the volume of${ \mathcal { M } } _ { g , n } ( L )$ in terms of volumes of moduli spaces of Riemann surfaces that we get by removing pairs of pants containing the boundary component$\beta _ { 1 }$of$S _ { g , n }$ See Fig. 9. We remark that the second condition in the definition of$\boldsymbol { \mathscr { I } } _ { g , n }$is equivalent to the condition that both complementary regions of the corresponding pair of pants have negative Euler characteristics. See Sect. 8 for more details.

## 6. Polynomial behavior of the Weil-Petersson volume

In this section we use the recursive formula for the volumes of moduli spaces stated in Sect. 5 to establish the following result:

Theorem 6.1. Thefunction$V _ { g , n } ( L )$is apolynomial in$L _ { 1 } ^ { 2 } , \ldots , L _ { n } ^ { 2 }$, namely:

$$
V _ {g, n} (L) = \sum_ {\stackrel {\alpha} {| \alpha | \leq 3 g - 3 + n}} C _ {\alpha} \cdot L ^ {2 \alpha},
$$

where$C _ { \alpha } > 0$lies in$\pi ^ { 6 g - 6 + 2 n - | 2 \alpha | }$· Q.

Calculation of$V _ { 1 , 1 } ( L )$. First, we elaborate on the main idea of the calculation of the volume polynomials through an example when$g = n = 1$ In this case, Theorem 4.2 for a hyperbolic surface of genus one with one geodesic boundary component implies that for any$X \in \mathcal { T } ( S _ { 1 , 1 } , L )$

$$
\sum_ {\gamma} \mathcal {D} (L, \ell_ {\gamma} (X), \ell_ {\gamma} (X)) = L,
$$

where the sum is over all non-peripheral simple closed curves γ on$S _ { 1 , 1 }$. By Lemma 3.2, we have

$$
\frac {\partial}{\partial L} \mathcal {D} (L, x, x) = \frac {1}{1 + e ^ {x - \frac {L}{2}}} + \frac {1}{1 + e ^ {x + \frac {L}{2}}}.
$$

Integrating over$\mathcal { M } _ { 1 , 1 } ( L )$, as in the calculation of$\mathrm { V o l } ( \mathcal { M } _ { 1 , 1 } )$in the Introduction, we get:

$$
L \cdot V _ {1, 1} (L) = \int_ {0} ^ {\infty} x \mathcal {D} (L, x, x) d x.
$$

So we have

$$
\frac {\partial}{\partial L} L \cdot V _ {1, 1} (L) = \int_ {0} ^ {\infty} x \cdot \left(\frac {1}{1 + e ^ {x + \frac {L}{2}}} + \frac {1}{1 + e ^ {x - \frac {L}{2}}}\right) d x.
$$

By setting$y _ { 1 } = x + L / 2$and$y _ { 2 } = x - L / 2$, we get

$$
\begin{array}{l} \int_ {0} ^ {\infty} x \cdot \left(\frac {1}{1 + e ^ {x + \frac {L}{2}}} + \frac {1}{1 + e ^ {x - \frac {L}{2}}}\right) d x \\ = \int_ {L / 2} ^ {\infty} \frac {y _ {1} - L / 2}{1 + e ^ {y _ {1}}} d y _ {1} + \int_ {- L / 2} ^ {\infty} \frac {y _ {2} + L / 2}{1 + e ^ {y _ {2}}} d y _ {2} \\ = 2 \int_ {0} ^ {\infty} \frac {y}{1 + e ^ {y}} d y + \int_ {0} ^ {L / 2} \frac {y - L / 2}{1 + e ^ {y}} d y + \int_ {0} ^ {- L / 2} \frac {y + L / 2}{1 + e ^ {y}} d y \\ = \frac {\pi^ {2}}{6} + \int_ {0} ^ {L / 2} (y - L / 2) \left(\frac {1}{1 + e ^ {y}} + \frac {1}{1 + e ^ {- y}}\right) d y = \frac {\pi^ {2}}{6} + \frac {L ^ {2}}{8}. \end{array}
$$

Since we have

$$
\frac {1}{1 + e ^ {y}} + \frac {1}{1 + e ^ {- y}} = 1.
$$

Therefore, we have:

$$
V _ {1, 1} (L) = \frac {L ^ {2}}{2 4} + \frac {\pi^ {2}}{6}.\tag{6.1}
$$

Remark. This result agrees with the result obtained in [NN].

Polynomial behavior of H and$V _ { g , n } . 0$ur goal is to simplify both sides of the equation (5.1)

$$
\frac {\partial}{\partial L _ {1}} L _ {1} V _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L) + \mathcal {A} _ {g, n} ^ {d c o n} (L) + \mathcal {B} _ {g, n} (L),
$$

and prove that$V _ { g , n } ( L ) , \mathcal { A } _ { g , n } ^ { c o n } ( L ) , \mathcal { A } _ { g , n } ^ { d c o n } ( L )$and${ \mathcal { B } } _ { g , n } ( L )$are polynomials in $L _ { 1 } , \ldots , L _ { n }$

Definition. For$i \in \mathbb N$, define$F _ { 2 i + 1 } : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$by

$$
F _ {2 k + 1} (t) = \int_ {0} ^ {\infty} x ^ {2 k + 1} \cdot H (x, t) d x.
$$

A straightforward calculation shows

$$
\begin{array}{l} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (x + y, t) d x d y \\ = \frac {(2 i + 1) ! \cdot (2 j + 1) !}{(2 i + 2 j + 3) !} F _ {2 i + 2 j + 3} (t). \end{array}\tag{6.2}
$$

To prove equation (6.2), note that for any$m , n \in \mathbb { N }$, we have

$$
\int_ {0} ^ {T} y ^ {m} (T - y) ^ {n} d y = \frac {m ! n !}{(m + n + 1) !} T ^ {m + n + 1}.
$$

By setting$Z = x + y$, it follows that

$$
\begin{array}{l} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (x + y, t) d x d y \\ = \int_ {0} ^ {\infty} \int_ {0} ^ {Z} (Z - y) ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (Z, t) d y d Z \\ = \frac {(2 i + 1) ! \cdot (2 j + 1) !}{(2 i + 2 j + 3) !} \int_ {0} ^ {\infty} Z ^ {2 i + 2 j + 3} H (Z, t) d Z. \end{array}
$$

These functions play a key role in the calculation of$V _ { g , n } ( L )$. We will show that:

Lemma 6.2. For any$k \geq 0$, we have

$$
\frac {F _ {2 k + 1} (t)}{(2 k + 1) !} = \sum_ {i = 0} ^ {k + 1} \zeta (2 i) (2 ^ {2 i + 1} - 4) \frac {t ^ {2 k + 2 - 2 i}}{(2 k + 2 - 2 i) !}.
$$

Therefore,$F _ { 2 k + 1 } ( t )$is a polynomial in$t ^ { 2 }$of degree$k + 1$, and the coefficient $o f t ^ { 2 k + 2 - 2 i }$lies in$\pi ^ { 2 i } \cdot \mathbb { Q } _ { > 0 }$

Remark. Since$\zeta ( 0 ) = - 1 / 2$, the leading coefficient of$F _ { 2 k + 1 } ( t )$is$t ^ { 2 k + 2 } /$ $( 2 k + 2 )$).

Proof. Similarly to the calculation of$V _ { 1 , 1 } ( L )$in the beginning of this section, we have

$$
\begin{array}{l} \int_ {0} ^ {\infty} x ^ {2 k + 1} \cdot \left(\frac {1}{1 + e ^ {x + t}} + \frac {1}{1 + e ^ {x - t}}\right) d x \\ = \int_ {0} ^ {\infty} \left(\frac {(x + t) ^ {2 k + 1} + (x - t) ^ {2 k + 1}}{1 + e ^ {x}}\right) d x \\ \quad + \int_ {0} ^ {t} - \frac {(x - t) ^ {2 k + 1}}{1 + e ^ {x}} + \frac {(- x + t) ^ {2 k + 1}}{1 + e ^ {- x}} d x \\ = \frac {t ^ {2 k + 2}}{2 k + 2} + \sum_ {i = 1} ^ {k + 1} 2 t ^ {2 k + 2 - 2 i} \cdot \binom {2 k + 1} {2 i - 1} \cdot \int_ {0} ^ {\infty} \frac {x ^ {2 i - 1}}{1 + e ^ {x}} d x. \end{array}
$$

On the other hand, one can verify

$$
2 \int_ {0} ^ {\infty} \frac {x ^ {2 i - 1}}{1 + e ^ {x}} d x = \zeta (2 i) (2 i - 1)! (2 - 2 ^ {- 2 i + 2}).
$$

As a result, we get

$$
\begin{array}{c} \frac {F _ {2 k + 1} (t)}{(2 k + 1) !} = \frac {1}{(2 k + 1) !} \int_ {0} ^ {\infty} x ^ {2 k + 1} \cdot \left(\frac {1}{1 + e ^ {(x + t) / 2}} + \frac {1}{1 + e ^ {(x - t) / 2}}\right) d x \\ = \frac {t ^ {2 k + 2}}{(2 k + 2) !} + \sum_ {i = 1} ^ {k + 1} \frac {t ^ {2 k + 2 - 2 i}}{(2 k + 2 - 2 i) !}   \zeta (2 i) (2 ^ {2 i + 1} - 4). \end{array}
$$

Now we can use the preceding lemma to prove that$V _ { g , n } ( L )$is a polynomial in L.

Sketch of the Proof of Theorem 6.1. The proof is by induction on$3 g + n$ Using equation (5.1), it suffices to prove that$\mathcal { A } _ { g , n } ^ { c o n } ( L ) , \mathcal { A } _ { g , n } ^ { d c o n } ( L )$and${ \mathcal { B } } _ { g , n } ( L )$ are polynomials in$L _ { 1 } ^ { 2 } , \ldots , L _ { n } ^ { 2 }$. Here we prove that${ \mathcal { B } } _ { g , n } ( L )$is a polynomial in$L _ { i } ^ { 2 } \mathrm { { ^ , s } ; }$a similar argument shows that$\mathcal { A } _ { g , n } ^ { d c o n } ( L )$and$\mathcal { A } _ { g , n } ^ { c o n } ( L )$are also polynomials in$L _ { 1 } ^ { 2 } , \ldots , L _ { n } ^ { 2 }$. By the induction hypothesis, for any$2 \leq j \leq n$ the volume$V _ { g , n - 1 } ( x , L _ { 2 } , \dots , L _ { j - 1 } , L _ { j + 1 } , \dots , L _ { n } )$is a polynomial in$x ^ { 2 }$ and$L _ { 2 } ^ { 2 } , \ldots , L _ { n } ^ { 2 }$. On the other hand, Lemma 6.2 implies that for$i \geq 0$

$$
\begin{array}{c} \int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot (H (x, L _ {1} + L _ {j}) + H (x, L _ {1} - L _ {j}))   d x \\ = F _ {2 i + 1} (L _ {1} + L _ {j}) + F _ {2 i + 1} (L _ {1} - L _ {j}) \end{array}
$$

is a polynomial in$L _ { 1 } ^ { 2 }$and$L _ { j } ^ { 2 }$. Hence, equations (5.5) and (5.4) imply that ${ \mathcal { B } } _ { g , n } ( L )$is a polynomial in$L _ { 1 } ^ { \dot { 2 } } , \dots , L _ { n } ^ { 2 }$. Moreover, this argument shows that the coefficient of$L _ { 1 } ^ { 2 \alpha _ { 1 } } \cdots L _ { n } ^ { 2 \alpha _ { n } }$in$V _ { g , n } ( L )$lies in$\pi ^ { 6 g - 6 + 2 n - 2 | \alpha | } \cdot \mathbb { Q } _ { + }$

Definition. Let$C _ { g } ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$be the coefficient of$L _ { 1 } ^ { 2 \alpha _ { 1 } } \cdots L _ { n } ^ { 2 \alpha _ { n } }$in the polynomial$V _ { g , n } ( L )$. To simplify notation, set

$$
(\alpha_ {1}, \dots , \alpha_ {n}) _ {g} = C _ {g} (\alpha) \times \prod_ {i = 1} ^ {n} \alpha_ {i}! \times 2 ^ {| \alpha |},
$$

where$\textstyle | \alpha | = \sum _ { i = 1 } ^ { n } \alpha _ { i }$

The recursive formula for volume polynomials (Sect. 5) simplifies when $\textstyle \sum _ { i = 1 } ^ { n } 2 \alpha _ { i } = 6 g - 6 + 2 n$; in this case, we get a recursive formula in terms of the leading coefficients of$\{ V _ { h , m } \}$with$3 h - m < 3 g - n$. If one of the $\alpha _ { i } \mathrm { ^ { * } s }$is 0 or 1, the recursive formula simplifies even further.

Theorem 6.3. For$n > 0 ,$, we have

$$
(1, \alpha_ {1}, \dots , \alpha_ {n}) _ {g} = (2 g + n - 2) (\alpha_ {1}, \dots , \alpha_ {n}) _ {g},
$$

where$\textstyle \sum _ { i = 1 } ^ { n } \alpha _ { i } = 3 g - 3 + n .$

Theorem 6.4. For$n > 0 ,$, we have

$$
(0, \alpha_ {1}, \dots , \alpha_ {n}) _ {g} = \sum_ {\alpha_ {i} \neq 0} (\alpha_ {1}, \dots , \alpha_ {i} - 1, \dots , \alpha_ {n}) _ {g},
$$

where$\textstyle \sum _ { i = 1 } ^ { n } \alpha _ { i } = 3 g - 2 + n .$

Proofof Theorem 6.3. To prove the theorem, we calculate the coefficient of $L _ { 0 } ^ { 2 } \cdot L _ { 1 } ^ { 2 \alpha _ { 1 } } \cdot \cdot \cdot L _ { n } ^ { 2 \alpha _ { n } }$in both sides of equation (5.1) for$\mathcal { M } _ { g , n + 1 } ( L _ { 0 } , \ldots , L _ { n } )$ It is easy to check that the coefficient of$L _ { 0 } ^ { 2 } \cdot L _ { 1 } ^ { 2 \alpha _ { 1 } } \cdot \cdot \cdot L _ { n } ^ { 2 \alpha _ { n } }$in both $\widehat { \mathcal { A } } ^ { c o n } ( L _ { 0 } , L _ { 1 } , \cdots , L _ { n } )$and$\widehat { \mathcal { A } } _ { g , n } ^ { d c o n } ( L _ { 0 } , L _ { 1 } , \cdot \cdot \cdot , \bar { L } _ { n } )$equals zero. By Lemma 6.2, the leading coefficient of$F _ { 2 i + 1 } ( t )$equals$1 / ( 2 i + 2 )$. Therefore, the coefficient of$L _ { 0 } ^ { 2 } \cdot \dot { L } _ { 1 } ^ { 2 \alpha _ { 1 } } \cdot \cdot \cdot L _ { n } ^ { 2 \alpha _ { n } }$in

$$
\sum_ {j = 1} ^ {n} \int_ {0} ^ {\infty} \frac {1}{2} x \cdot (H (x, L _ {0} + L _ {j}) + H (x, L _ {0} - L _ {j})) \cdot V _ {g, n - 1} (x, L _ {T _ {n} - \{j \}}) d x
$$

equals

$$
\sum_ {j = 1} ^ {n} \frac {\binom {2 \alpha_ {j} + 2} {2}}{2   \alpha_ {j} + 2} \cdot \frac {(\alpha_ {1} , \ldots , \alpha_ {n}) _ {g}}{\alpha ! \times 2 ^ {3 g - 3 + n}} = \frac {3   (2 g - 2 + n)}{2}   \times \frac {(\alpha_ {1} , \ldots , \alpha_ {n}) _ {g}}{\alpha ! \times 2 ^ {3 g - 3 + n}},
$$

where$T _ { n } ~ = ~ \{ 1 , 2 , \dots , n \}$. On the other hand, the coefficient of$L _ { 0 } ^ { 2 }$ $L _ { 1 } ^ { 2 \alpha _ { 1 } } \cdots L _ { n } ^ { 2 \alpha _ { n } }$on the left hand side of equation (5.1) equals

$$
\frac {3 (1 , \alpha_ {1} , \ldots , \alpha_ {n}) _ {g}}{\alpha ! \times 2 ^ {3 g - 3 + n + 1}},
$$

where$\alpha ! = \alpha _ { 1 } ! \cdot \cdot \cdot \alpha _ { n } !$. Hence, we have

$$
3 \left(1, \alpha_ {1}, \dots , \alpha_ {n}\right) _ {g} = 3 (2 g + n - 2) (\alpha_ {1}, \dots , \alpha_ {n}) _ {g}.
$$

The proof of Theorem 6.4 follows similar lines.

Note that when$\textstyle g = 0 , \sum _ { i = 1 } ^ { n } \alpha _ { i } = n - 3$. Hence at least one ofthe integers $\alpha _ { 1 } , \cdots , \alpha _ { n }$is equal to 0. Therefore, Theorem 6.4 and the initial condition $( 0 , 0 , 0 ) _ { 0 } = 1$determine$( \alpha _ { 1 } , \ldots , \alpha _ { n } ) _ { 0 }$inductively. One can easily verify that

Corollary 6.5. For$n \geq 3 .$, we have

$$
(\alpha_ {1}, \ldots , \alpha_ {n}) _ {0} = \binom{\alpha_ {1} + \dots + \alpha_ {n}}{\alpha_ {1}, \dots , \alpha_ {n}},
$$

where$\textstyle \sum _ { i = 1 } ^ { n } \alpha _ { i } = n - 3$

Remark. Equations in Theorem 6.3 and Theorem 6.4 are reminiscent of the dilaton and string equations for the intersection pairings over the moduli spaces [Har]. In a sequel we prove that

$$
(\alpha_ {1}, \ldots , \alpha_ {n}) _ {g} = \int_ {\overline {{\mathcal {M}}} _ {g, n}} \psi_ {1} ^ {\alpha_ {1}} \dots \psi_ {n} ^ {\alpha_ {n}},
$$

where$\psi _ { i }$denotes the Chern class of the ith tautological line bundle over ${ \overline { { \mathcal { M } } } } _ { g , n }$[Mirz2].

## 7. Integration over the moduli space

In this section, we investigate the Weil-Petersson symplectic structure of the moduli space${ \mathcal { M } } _ { g , n } ( L )$

For a multicurve$\textstyle \gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i }$, we have

$$
\ell_ {\gamma} (X) = \sum_ {i = 1} ^ {k} c _ {i} \ell_ {\gamma_ {i}} (X).
$$

Given a continuous function$f : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$

$$
f _ {\gamma} (X) = \sum_ {[ \alpha ] \in \operatorname{Mod} \cdot [ \gamma ]} f (\ell_ {\alpha} (X)),\tag{7.1}
$$

defines a function$f _ { \gamma } : \mathcal { M } _ { g , n } ( L )  \mathbb { R } _ { + }$

We establish the following result for integrating the function$f _ { \gamma }$over ${ \mathcal { M } } _ { g , n } ( L )$

Theorem 7.1. For any multicurve$\begin{array} { r } { \gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i } } \end{array}$, the integral of$f _ { \gamma }$over ${ \mathcal { M } } _ { g , n } ( L )$with respect to the Weil-Petersson volume form is given by

$$
\int_ {\mathcal {M} _ {g, n} (L)} f _ {\gamma} (X)   d X = \frac {2 ^ {- M (\gamma)}}{| \operatorname{Sym} (\gamma) |} \int_ {\mathbf {x} \in \mathbb {R} _ {+} ^ {k}} f (| \mathbf {x} |) V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) \mathbf {x} \cdot d \mathbf {x},
$$

where$\begin{array} { r } { \Gamma = ( \gamma _ { 1 } , \ldots , \gamma _ { k } ) , | { \bf x } | = \sum _ { i = 1 } ^ { k } c _ { i } \mathrm { ~ } x _ { i } \mathrm { , ~ } { \bf x } \cdot d { \bf x } = x _ { 1 } \cdot \cdot \cdot x _ { k } \cdot d x _ { 1 } \wedge \cdot \cdot \cdot \wedge d x _ { k } , } \end{array}$ and

M(γ) = |{i|γ separates offa one-handle from$S _ { g , n } \} |$

Recall that given${ \bf x } = ( x _ { 1 } , \ldots , x _ { k } ) \in \mathbb { R } _ { + } ^ { k } , V _ { g , n } ( \Gamma , { \bf x } , \beta , L )$is defined by

$$
V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) = \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)).
$$

Also,

$$
V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) = \prod_ {i = 1} ^ {s} V _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}}),
$$

where

$$
S _ {g, n} (\gamma) = \bigcup_ {i = 1} ^ {s} S _ {i},\tag{7.2}
$$

$S _ { i } \cong S _ { g _ { i } , n _ { i } }$, and$A _ { i } = \partial S _ { i }$

By Theorem 7.1 integrating$f _ { \gamma } ,$, even for a compact Riemann surface, reduces to the calculation of volumes of moduli spaces of bordered Riemann surfaces.

Remark. Let$g \in \mathrm { S y m } ( \gamma )$, where$\textstyle \gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i }$. Then$g ( \gamma _ { i } ) = \gamma _ { j }$implies that$c _ { i } = c _ { j }$

Integration and covering. Let

$$
\pi : X _ {1} \to X _ {2}
$$

be a covering map, and$v _ { 2 }$a volume form on$X _ { 2 }$. Then$v _ { 2 }$defines a volume form$v _ { 1 }$on$X _ { 1 }$. If$f$is in$L ^ { 1 } ( X _ { 1 } , v _ { 1 } )$, then the push forward$\pi _ { * } f : X _ { 2 } \to$R defined by

$$
(\pi_ {*} f) (x) = \sum_ {y \in \pi^ {- 1} \{x \}} f (y)\tag{7.3}
$$

is a function in$L ^ { 1 } ( X _ { 2 } , v _ { 2 } )$such that

$$
\int_ {X _ {2}} \left(\pi_ {*} f\right) d v _ {2} = \int_ {X _ {1}} f d v _ {1}.\tag{7.4}
$$

Coverings and volume forms of the$\mathcal { M } _ { g , n } ( L ) ^ { \bullet }$. An element$h \in \operatorname { M o d } _ { g , n }$ acts on Γ by

$$
h. \Gamma = (h \cdot \gamma_ {1}, \dots , h \cdot \gamma_ {k}).
$$

As in Sect. 2, let$\mathcal { O } _ { \Gamma }$be the set of homotopy classes of elements of Mod ·Γ. Consider$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$defined by the following space of pairs:

$$
\{(X, \eta) \mid X \in \mathcal {M} _ {g, n} (L), \eta = (\eta_ {1}, \dots , \eta_ {k}) \in \mathcal {O} _ {\Gamma},
$$

$\eta _ { i } \mathrm { ^ { * } s }$are closed geodesics on$X \}$.

Then

$$
\mathcal {M} _ {g, n} (L) ^ {\Gamma} = \mathcal {T} _ {g, n} (L) / G _ {\Gamma},
$$

where

$$
G _ {\Gamma} = \bigcap_ {i = 1} ^ {k} \operatorname{Stab} (\gamma_ {i}) \subset \operatorname{Mod} (S _ {g, n}).
$$

Let$\pi ^ { \Gamma } : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathcal { M } _ { g , n } ( L )$be the projection map defined by

$$
\pi^ {\Gamma} (X, \eta) = X.
$$

As the Weil-Petersson symplectic structure on Teichmüller space is invariant under the action ofthe mapping class group, it induces a symplectic structure on$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$which is the same as the form$\pi ^ { \Gamma * } ( w _ { w p } )$

The key tool in our approach is the existence of k commuting Hamiltonian$S ^ { 1 }$-actions on$\mathcal { M } _ { g , n } ( \hat { L } ) ^ { \Gamma }$induced by twisting along connected components of$\gamma$. We will discuss how the corresponding quotient space is related to the moduli space of hyperbolic structures over$S _ { g , n } ( \gamma )$

Twisting and the Weil-Petesson symplectic form. Let$\ell _ { \Gamma } : \mathcal { T } _ { g , n } \to \mathbb { R } _ { + } ^ { k }$ denote the length vector

$$
\ell_ {\Gamma} (X) = (\ell_ {\gamma_ {1}} (X), \dots , \ell_ {\gamma_ {k}} (X)).
$$

Then the Weil-Petersson volume form induces a natural measure on the level set$\ell _ { \Gamma } ^ { - 1 } ( a )$. Here we consider the length-normalized twist flow, given by

$$
\phi_ {\alpha} ^ {t} (X) = \mathrm{tw} _ {\alpha} ^ {t \cdot \ell_ {\alpha} (X)} (X).
$$

Since$\ell _ { \alpha } ( X ) = \ell _ { \alpha } ( \mathrm { t w } _ { \alpha } ^ { t } ( X ) )$, Theorem 2.1 implies that the map

$$
\phi_ {\gamma} ^ {(t _ {1}, \dots , t _ {k})}: \ell_ {\Gamma} ^ {- 1} (a) \to \ell_ {\Gamma} ^ {- 1} (a)
$$

gives rise to an action of$\mathbb { R } ^ { k }$on the level set$\ell _ { \Gamma } ^ { - 1 } ( a )$preserving the Weil-Petersson symplectic form.

Twisting flows on$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$. The length function$\ell _ { \Gamma }$descends to a function $\mathcal { L } _ { \Gamma }$on$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$

$$
\begin{array}{c} \mathbb {R} _ {+} ^ {k} \xleftarrow {\mathcal {L} _ {\Gamma}} \mathcal {M} _ {g, n} (L) ^ {\Gamma} \\ \Big \downarrow_ {\pi^ {\Gamma}} \\ \mathcal {M} _ {g, n} (L) \end{array}
$$

where for$( X , ( \eta _ { 1 } , \dots , \eta _ { k } ) ) \in \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } , \mathcal { L } _ { i } ( X , \eta ) = \ell _ { \eta _ { i } } ( X )$, and

$$
\mathcal {L} _ {\Gamma} (X, \eta) = (\mathcal {L} _ {i} (X)).
$$

We remark that the construction of the Fenchel-Nielsen flow defined on Teichmüller space is equivariant with respect to the action of the mapping class group. Therefore, we have:

• Each level set

$$
\mathcal {M} _ {g, n} (L) ^ {\Gamma} [ a ] = \mathcal {L} ^ {- 1} (a _ {1}, \dots , a _ {k}) \subset \mathcal {M} _ {g, n} (L) ^ {\Gamma}
$$

carries a natural volume form$v _ { a }$.

• Consider the twist flows defined by

$$
\mathrm{tw} _ {i} ^ {t} (X, \eta) = \big (\mathrm{tw} _ {\eta_ {i}} ^ {t} (X), \eta \big),
$$

where$\operatorname { t w } _ { \eta _ { i } } ^ { t } ( X )$is obtained by cutting X along$\eta _ { i }$, twisting to the right by hyperbolic length t and regluing the boundaries. By Theorem 2.1,${ \mathrm { t w } } _ { i }$is the Hamiltonian flow of the function$\mathscr { L } _ { i }$. This flow has closed orbits on $\mathcal { M } _ { g , n } ^ { \Gamma } ( L )$. More precisely, when$t _ { i } = \mathcal { L } _ { i } ( Y ) , \mathrm { t w } _ { i } ^ { t _ { i } ( Y ) }$is the Dehn twist of Y along$\eta _ { i }$. Hence for$Y \in \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } , Y = \mathfrak { t w } _ { i } ^ { t _ { i } ( Y ) } ( Y )$

Therefore, the Hamiltonian flow of$\mathcal { L } ^ { 2 } / 2 : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathbb { R } _ { + } ^ { k }$gives rise to the action of$T ^ { k } = S ^ { 1 } \times \cdots \times S ^ { 1 }$by twisting along γ proportionally to its length.

The quotient space,

$$
\mathcal {M} _ {g, n} (L) ^ {\Gamma *} [ a ] = \mathcal {M} _ {g, n} (L) ^ {\Gamma} [ a ] / T ^ {k},
$$

where$\begin{array} { r } { T ^ { k } = \prod _ { i = 1 } ^ { k } S ^ { 1 } } \end{array}$, inherits a symplectic structure from the symplectic structure of$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$. Let$\pi$denote the projection map

$$
\pi : \mathcal {M} _ {g, n} (L) ^ {\Gamma} [ a ] \to \mathcal {M} _ {g, n} (L) ^ {\Gamma *} [ a ].
$$

In general the twisting parameter along$\gamma _ { i }$can be between 0 and$\ell _ { \gamma _ { i } }$. However, in the case of a simple geodesic$\gamma _ { i }$separating off a one-handle (the elliptic tail case) Stab$( \gamma _ { j } )$contains a half twist and so τ varies within a fundamental region$\begin{array} { r } { \{ 0 \le \tau \le \frac { 1 } { 2 } \ell _ { \gamma _ { i } } \} } \end{array}$. The reason is that every$X \in \mathcal { M } _ { 1 , 1 } ( L )$ comes with an elliptic involution, but when$( g , n ) \neq ( 1 , 1 )$, a generic point in${ \mathcal { M } } _ { g , n } ( L )$does not have any non trivial automorphism fixing the boundary components set wise. Hence for an open set$U \subset { \mathcal { M } } _ { g , n } ( L ) ^ { \Gamma * } [ a ]$, we have

$$
\operatorname{Vol} \left(\pi^ {- 1} (U)\right) = 2 ^ {- M (\gamma)} \operatorname{Vol} (U) \cdot a _ {1} \dots a _ {k},\tag{7.5}
$$

where$M ( \gamma )$is the number of connected components γ separating off a onehandle.

On the other hand, by cutting$X \in \ell _ { \Gamma } ^ { - 1 } ( a _ { 1 } , \dots , a _ { k } )$along connected components of$\gamma ,$we obtain a surface$s _ { \gamma } ( \boldsymbol X ) \in \mathcal { T } ( S ( \gamma ) , \ell _ { \Gamma } = \mathbf { x } , \ell _ { \beta } = L )$ with geodesic boundary components. Observe that for any$( t _ { 1 } \ldots t _ { k } ) \in \mathbb { R } ^ { k }$

$$
s _ {\gamma} (X) = s _ {\gamma} \bigl (\phi_ {\gamma} ^ {(t _ {1}, \dots , t _ {k})} (X) \bigr).
$$

Since the map$s _ { \gamma }$is mapping class group equivariant, it induces a map on$\mathcal { M } _ { g , n } ^ { \Gamma }$as follows. For$( X , \eta ) \ \in \ \mathcal { M } _ { g , n } ( L ) ^ { \Gamma * } [ a ]$, let$s ( Y ) = s _ { \gamma } ( X ) \ \in$ $\mathcal { M } ( S _ { g , n } ( \gamma ) , \ell _ { \Gamma } = a , L _ { \beta } = L )$. Now as in equation (7.2), let

$$
S _ {g, n} (\gamma) = \bigcup_ {i = 1} ^ {s} S _ {g _ {i}, n _ {i}}, A _ {i} = \partial S _ {i} \subset \mathcal {B}.
$$

Then Theorem 2.1 implies:

Lemma 7.2. For any multicurve$\gamma ,$, the canonical isomorphism

$$
s: \mathcal {M} _ {g, n} (L) ^ {\Gamma *} [ a ] \to \mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = a, L _ {\beta} = L) \cong \prod_ {i = 1} ^ {s} \mathcal {M} _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}})
$$

is a symplectomorphism.

Remark. By the discussion above, the function$\mathcal { L } ^ { 2 } / 2$is the moment map for the$T ^ { k }$action, and the space$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma * } [ a ]$is a symplectic quotient space. In [Mirz2], we exploit this fact to relate the volume polynomials to the intersection pairings of tautological classes over the moduli space. See [Ki].

Integrating geometric functions. Now we can use the preceding lemma to integrate certain functions over the covering space$\hat { \mathscr { M } } _ { g , n } ( L ) ^ { \Gamma }$

Lemma 7.3. For any function$F : \mathbb { R } ^ { k } \to \mathbb { R } _ { + }$and$\Gamma = \left( \gamma _ { 1 } , \cdots , \gamma _ { k } \right)$, define $F _ { \Gamma } : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathbb { R }$by

$$
F _ {\Gamma} (Y) = F (\mathcal {L} _ {\Gamma} (Y)).
$$

Then the integral of$F _ { \Gamma }$over$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$is given by

$$
\int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma}} F _ {\Gamma} (Y)   d Y = 2 ^ {- M (\Gamma)} \int_ {\mathbf {x} \in \mathbb {R} _ {+} ^ {k}} F (\mathbf {x}) \mathrm{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\beta} = L, \ell_ {\Gamma} = \mathbf {x}))   \mathbf {x}   d \mathbf {x},
$$

where$\mathbf { x } = ( x _ { 1 } , \ldots , x _ { k } )$, and$\mathbf { x } \cdot d \mathbf { x } = x _ { 1 } \cdot \cdot \cdot x _ { k } \cdot d x _ { 1 } \wedge \cdot \cdot \cdot \wedge d x _ { k }$

Proof. Note that the function$F _ { \Gamma }$is constant on each level set of$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma } [ \mathbf { x } ]$ of$\mathcal { L } _ { \Gamma }$. For$\mathbf { x } \in \mathbb { R } _ { + } ^ { k }$, let

$$
I (\mathbf {x}) = \int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma} [ \mathbf {x} ]} F (\mathcal {L} _ {\Gamma} (Y)) d Y.
$$

By Theorem 2.1,

$$
\int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma}} F _ {\Gamma} (Y) d Y = \int_ {\mathbf {x} \in \mathbb {R} _ {+} ^ {k}} I (\mathbf {x}) d \mathbf {x}.
$$

To calculate$I ( \mathbf { x } )$, note that using Lemma 7.2 and equation (7.5), we have

$$
\begin{array}{l} \operatorname{Vol} \big (\mathcal {L} ^ {- 1} (x _ {1}, \dots , x _ {k}) \big) \\ \qquad = 2 ^ {- M (\Gamma)}   x _ {1} \dots x _ {k} \cdot \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\beta} = L, \ell_ {\Gamma} = \mathbf {x})). \end{array}
$$

Hence,

$$
I (\mathbf {x}) = 2 ^ {- M (\Gamma)} \cdot F (\mathbf {x}) \cdot \operatorname{Vol} \left(\mathcal {M} \left(S _ {g, n} (\gamma), \ell_ {\beta} = L, \ell_ {\Gamma} = \mathbf {x}\right)\right) \cdot x _ {1} \dots x _ {k}.
$$

Now we prove the main result of this section:

Proofof Theorem 7.1. Fix$\Gamma = ( \gamma _ { 1 } , \dots , \gamma _ { k } )$. Then let$\pi ^ { \Gamma } : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to$ ${ \mathcal { M } } _ { g , n } ( L )$denote the projection map. Consider the function

$$
F: \mathbb {R} _ {+} ^ {k} \to \mathbb {R} _ {+}
$$

given by$F ( x _ { 1 } , \dots , x _ { k } ) = f ( \sum _ { i = 1 } ^ { k } c _ { i } x _ { i } )$. Then we define functions$F _ { \Gamma }$: $\mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathbb { R } _ { + }$, and

$$
\pi_ {*} ^ {\Gamma} F _ {\Gamma}: \mathcal {M} _ {g, n} (L) \to \mathbb {R} _ {+}
$$

as in Lemma 7.3 and equation (7.3). Applying equation (7.4) and Lemma 7.2, we obtain

$$
\int_ {\mathcal {M} _ {g, n} (L)} \pi_ {*} ^ {\Gamma} F _ {\Gamma} (X) d X = \int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma}} F _ {\Gamma} (Y) d Y.
$$

Hence, Lemma 7.3 implies that

$$
\begin{array}{l} \int_ {\mathcal {M} _ {g, n} (L)} \pi_ {*} ^ {\Gamma} F _ {\Gamma} (X) d X \\ = 2 ^ {- M (\gamma)} \iint_ {\mathbf {x} \in \mathbb {R} _ {+} ^ {k}} f (| \mathbf {x} |) \mathrm{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)) \cdot \mathbf {x} \cdot d \mathbf {x}. \end{array}
$$

On the other hand, we have

$$
\sum_ {g \in \operatorname{Mod} _ {g, n} / \cap \operatorname{Stab} (\gamma_ {i})} f (\ell_ {g \cdot \gamma} (X)) = | \operatorname{Sym} (\gamma) | \cdot \sum_ {[ \alpha ] \in [ \gamma ] \cdot \operatorname{Mod} _ {g, n}} f (\ell_ {\alpha} (X)),
$$

where

$$
\operatorname{Sym} (\gamma) = \operatorname{Stab} (\gamma) / \cap \operatorname{Stab} \left(\gamma_ {i}\right).
$$

Hence$\pi _ { * } ^ { \Gamma } F _ { \Gamma } ( X ) = | \operatorname { S y m } ( \gamma ) | \cdot f _ { \gamma } ( X )$, and we are done.

## 8. Volumes of moduli spaces of bordered Riemann surfaces

In this section we use the identity for lengths of simple closed geodesics in Theorem 4.2 to derive the recursive formula for the volume polynomials stated in Sect. 5.

Idea of the calculation of$V _ { g , n } ( L )$. By Theorem 4.2, for any$X \in \mathcal { T } _ { g , n } ( L _ { 1 }$ $\ldots , L _ { n } )$we have

$$
\sum_ {\{\gamma_ {1}, \gamma_ {2} \} \in \mathcal {F} _ {1}} \mathcal {D} (L _ {1}, \ell_ {\gamma_ {1}} (X), \ell_ {\gamma_ {2}} (X)) + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \mathcal {R} (L _ {1}, L _ {i}, \ell_ {\gamma} (X)) = L _ {1},\tag{8.1}
$$

whereas in Sect. 4,$\mathcal { F } _ { 1 }$and$\mathcal { F } _ { 1 , j }$are respectively in one-to-one correspondence with the set of pairs of pants containing the boundary component$\beta _ { 1 }$ and$\{ \beta _ { 1 } , \beta _ { j } \}$. Now let

$$
\tilde {\mathcal {R}} _ {j} (X) = \sum_ {\gamma \in \mathcal {F} _ {1, j}} \mathcal {R} (L _ {1}, L _ {j}, \ell_ {\gamma} (X)),\tag{8.2}
$$

and

$$
\tilde {\mathcal {D}} (X) = \sum_ {(\gamma_ {1}, \gamma_ {2}) \in \mathcal {F} _ {1}} \mathcal {D} (L _ {1}, \ell_ {\gamma_ {1}} (X), \ell_ {\gamma_ {2}} (X)).
$$

Then from equation (8.1) we get

$$
\tilde {\mathcal {D}} (X) + \sum_ {j = 2} ^ {n} \tilde {\mathcal {R}} _ {j} (X) = L _ {1},
$$

where$\tilde { \mathcal { D } }$and$\tilde { \mathcal { R } } _ { j } : \mathrm { ~ s ~ }$are all functions defined on the moduli space$\mathcal { M } _ { g , n } ( L )$ Note that the mapping class group acts on both$\mathcal { F } _ { 1 }$and$\mathcal { F } _ { 1 , j }$. We use the description of$\mathcal { F } _ { 1 } / \mathbf { M o d } _ { g , n }$and$\mathcal { F } _ { 1 , j } / \mathrm { M o d } _ { g , n }$to reformulate$\mathcal { \tilde { R } } _ { j }$and$\tilde { \mathcal { D } }$ as push forwards of functions defined over certain coverings of the moduli space of the form described in Sect. 7. We remark that the action of$\mathbf { M o d } _ { g , n }$ on$\mathcal { F } _ { 1 }$is not transitive, nevertheless the orbits can be characterized by the topology of their complementary regions which is determined by the number of the connected components, genus and the number of boundary components of each connected component.

![](images/page_39_image_0.jpg)

Fig. 9 a):$| \partial ( \Sigma ) \cap \partial S _ { g , n } | = 1$, separating case b): non-separating case c):$| \partial ( \Sigma ) \cap \partial S _ { g , n } | = 2$

Theorem 8.1. For$( g , n ) \neq ( 1 , 1 ) , ( 0 , 3 )$, the volume function$V _ { g , n } ( L )$satisfies

$$
\frac {\partial}{\partial L _ {1}} L _ {1} V _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L) + \mathcal {A} _ {g, n} ^ {d c o n} (L) + \mathcal {B} _ {g, n} (L).\tag{8.3}
$$

Proof. By integrating both sides of the equation

$$
\tilde {\mathcal {D}} (X) + \sum_ {j = 2} ^ {n} \tilde {\mathcal {R}} _ {j} (X) = L _ {1}
$$

over${ \mathcal { M } } _ { g , n } ( L )$with respect to the volume form induced by the Weil-Petersson symplectic form, we get

$$
\sum_ {j = 2} ^ {n} \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {R}} _ {j} (X) d X + \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {D}} (X) d X = L _ {1} \cdot V _ {g, n} (L).\tag{8.4}
$$

Next we calculate the integrals

$$
\mathcal {R} _ {g, n} ^ {j} (L) = \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {R}} _ {j} (X) d X,
$$

and

$$
\mathcal {D} _ {g, n} (L) = \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {D}} (X) d X.
$$

I): Integrating$\mathcal { \tilde { R } } _ { j }$. For$1 \neq j$the mapping class group$\mathbf { M o d } _ { g , n }$acts transitively on$\mathcal { F } _ { 1 , j }$. So given$\gamma _ { j } \in \mathcal { F } _ { 1 , j }$, we have

$$
\operatorname{Mod} _ {g, n} \cdot \{\gamma_ {j} \} = \mathcal {F} _ {1, j}.
$$

Define$R ^ { j } : \mathbb { R } _ { + }  \mathbb { R } _ { + }$by

$$
R ^ {j} (x) = \mathcal {R} (L _ {1}, L _ {j}, x).
$$

Then by the definition (equation (7.1)), for any$X \in \mathcal { M } _ { g , n } ( L )$we have

$$
\tilde {\mathcal {R}} _ {j (x)} (X) = R _ {\gamma_ {j}} ^ {j} (X).
$$

Since$S _ { g , n } ( \gamma _ { j } ) \cong S _ { g , n - 1 }$, and$| \operatorname { S y m } ( \gamma _ { j } ) | = 1$, Theorem 7.1 implies that

$$
\begin{array}{l} \mathcal {R} _ {g, n} ^ {j} (L) \\ = 2 ^ {- m (g, n - 1)} \int_ {0} ^ {\infty} x \cdot \mathcal {R} (L _ {1}, L _ {j}, x) \cdot \mathrm{Vol} (\mathcal {M} (S _ {g, n} (\gamma_ {j}), \ell_ {\gamma_ {j}} = x, L))   d x \\ = 2 ^ {- m (g, n - 1)} \int_ {0} ^ {\infty} x \cdot \mathcal {R} (L _ {1}, L _ {j}, x) \cdot V _ {g, n - 1} (x, L _ {2}, \ldots , \hat {L _ {j}}, \ldots , L _ {n}) d x. \end{array}
$$

Using equation (3.4),$\begin{array} { r } { \frac { \partial } { \partial L _ { 1 } } \mathcal { R } _ { g , n } ^ { j } ( L ) } \end{array}$equals

$$
\begin{array}{c} \frac {2 ^ {- m (g , n - 1)}}{2} \int_ {0} ^ {\infty} x (H (x, L _ {1} - L _ {j}) + H (x, L _ {1} + L _ {j})) \\ \cdot V _ {g, n - 1} (x, L _ {2}, \ldots , \hat {L _ {j}}, \ldots , L _ {n}) d x. \end{array}
$$

Hence, from the definition of${ \mathcal { B } } _ { g , n }$in Sect. 5 we obtain

$$
\sum_ {j = 2} ^ {n} \frac {\partial}{\partial L _ {1}} \mathcal {R} _ {g, n} ^ {j} (L) = \mathcal {B} _ {g, n} (L).\tag{8.5}
$$

II): Integrating$\tilde { \mathcal { D } }$. Given$\{ \gamma _ { 1 } , \gamma _ { 2 } \} \in \mathcal { F } _ { 1 }$, let$\gamma = \gamma _ { 1 } + \gamma _ { 2 }$. We remark that by Lemma 3.1, the function$\mathcal { D } ( L _ { 1 } , \ell _ { \gamma _ { 1 } } ( X ) , \ell _ { \gamma _ { 2 } } ( X ) )$is a function of$L _ { 1 }$and $\ell _ { \gamma } ( X ) = \ell _ { \gamma _ { 1 } } ( X ) + \ell _ { \gamma _ { 2 } } ( X )$. So we can apply Theorem 7.1 for$\gamma = \gamma _ { 1 } + \gamma _ { 2 }$ as follows. Define$D : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$by

$$
D (x) = \mathcal {D} (L _ {1}, x, 0).
$$

1): Define$A ^ { c o n }$to be the set of$\gamma _ { 1 } + \gamma _ { 2 }$such that the complement of the pair of pants containing$\beta _ { 1 } , \gamma _ { 1 }$, and$\gamma _ { 2 }$is a connected surface of genus$g - 1$with $n + 1$boundary components. In this case,$| \mathrm { S y m } ( \gamma ) | = 2 ( \mathrm { S e c t . } 2 )$

2): For$a = ( ( g _ { 1 } , I ) , ( g _ { 2 } , J ) ) \in \mathcal { I } _ { g , n }$, let$A _ { a }$be the set of$\gamma = \gamma _ { 1 } + \gamma _ { 2 }$ such that the complement of the pair of pants containing$\beta _ { 1 } , \gamma _ { 1 }$and$\gamma _ { 2 }$is a disjoint union of two surfaces$S _ { 1 }$and$S _ { 2 }$, respectively homeomorphic to $S _ { g _ { 1 } , n _ { 1 } + 1 }$and$S _ { g - g _ { 1 } , n _ { 2 } + 1 }$, such that we have:

$$
\{\beta_ {i _ {1}}, \dots , \beta_ {i _ {n _ {1}}} \} \subset \partial S _ {1}, \{\beta_ {j _ {1}}, \dots , \beta_ {j _ {n _ {2}}} \} \subset \partial S _ {2}.
$$

See Fig. 9 and Sect. 5. The action of the mapping class group on$A ^ { c o n }$ and$A _ { a } ( a \in \mathcal { I } _ { g , n } )$is transitive. Let

$$
A ^ {d c o n} = \bigcup_ {a \in \mathcal {I} _ {g, n}} A _ {a}.
$$

For each$a \in \mathcal { I } _ { g , n }$, choose an element$\gamma _ { a }$of the set$A _ { a }$; also, choose$\gamma \in A ^ { c o n }$ Define the set of representatives of the distinct orbits of$\tau _ { g , n } , \mathcal { C }$by

$$
\mathcal {C} = \{\gamma_ {a} \mid a \in \mathfrak {I} _ {g, n} \} \cup \{\gamma \}.
$$

Then it is easy to see that by the definition (equation (7.1))

$$
\tilde {\mathcal {D}} (X) = \sum_ {\gamma = \gamma_ {1} + \gamma_ {2} \in \mathcal {C}} D _ {\gamma} (X).
$$

We remark that for$\gamma \in A _ { a }$we have$| \operatorname { S y m } ( \gamma ) | = 2$if and only if$I = J = \phi$ and$g _ { 1 } = g _ { 2 } ;$; otherwise$| \mathrm { S y m } ( \gamma ) | = 1 ( \mathrm { S e c t . } 2 )$

Therefore, equation (3.3) and Theorem 7.1 implies that

$$
\frac {\partial}{\partial L _ {1}} \mathcal {D} _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L) + \mathcal {A} _ {g, n} ^ {d c o n} (L).\tag{8.6}
$$

Now the result is immediate from equations (8.4), (8.5) and (8.6).

The term$1 / 2$in equation (5.2) and (5.3) is related to$\operatorname { S y m } ( \gamma )$when$\gamma$is nonseparating. Note that the sum in the definition of$\widehat { \mathcal { A } } _ { g , n } ^ { d c o \overline { { n } } }$is over ordered pairs

$$
((g _ {1}, I _ {1}), (g _ {2}, I _ {2})).
$$

Hence every term in the integral appears twice except for the term corresponding to the case where$g _ { 1 } = g _ { 2 }$, and$I _ { 1 } = I _ { 2 } = \phi$. So by considering $1 / 2$in equation (5.3), we will take care of the factor$\operatorname { S y m } ( \gamma )$

## References

[B]Basmajian, A.: The orthogonal spectrum of a hyperbolic manifold. Am. J. Math. 115, 1139–1159 (1993)

[BS] Birman, J.S., Series, C.: Geodesics with bounded intersection number on surfaces are sparsely distributed. Topology 24, 217–225 (1985)

[BL]Bismut, J.-M., Labourie, F.: Symplectic geometry and the Verlinde formulas. In: Surveys in Differential Geometry: Differential Geometry Inspired by String Theory, vol. 5 of Surv. Differ. Geom., pp. 97–331. Boston, MA: Int. Press 1999

[Bus] Buser, P.: Geometry and Spectra of Compact Riemann Surfaces. Boston: Birkhäuser 1992

[CEG] Canary, R.D., Epstein, D.B.A., Green, P.: Notes on notes of Thurston. In: Analytical and Geometric Aspects ofHyperbolic Space, pp. 3–92. Cambridge: Cambridge University Press 1987

[D]Donaldson, S.: Gluing techniques in the cohomology of moduli spaces. In: Topological Methods in Modern Mathematics, pp. 137–170. Houston, TX: Publish or Perish 1993

[Gol] Goldman, W.: The symplectic nature of fundamental groups of surfaces. Adv. Math. 54, 200–225 (1984)

[HP] Harer, J.L., Penner, R.C.: Combinatorics of Train Tracks. Annals of Math. Studies, vol. 125. Princeton, NJ: Princeton University Press 1992

[Har]Harris, J., Morrison, I.: Moduli of Curves. Graduate Texts in Mathematics, vol. 187. New York: Springer 1998

[HY] Hocking, J., Young, G.: Topology. New York: Dover Publication 1988

[IT]Imayoshi, Y., Taniguchi, M.: An Introduction to Teichmüller Spaces. Tokyo: Springer 1992

[JK]Jeffrey, L., Kirwan, F.: Intersection theory on moduli spaces of holomorphic bundles of arbitrary rank on a Riemann surface. Ann. Math. (2) 148, 109–196 (1998)

[KMZ] Kaufmann, R., Manin, Y., Zagier, D.: Higher Weil-Petersson volumes of moduli spaces of stable n-pointed curves. Commun. Math. Phys. 181, 736–787 (1996)

[Ki]Kirwan, F.: Momentum maps and reduction in algebraic geometry. Differ. Geom. Appl. 9, 135–171 (1998)

[K]Kontsevich, M.: Intersection on the moduli space of curves and the matrix airy function. Commun. Math. Phys. 147, 1–23 (1992)

[LM] Labourie, F., McShane, G.: Cross ratios and identities for higher Thurston theory. Preprint 2006

[MaZ] Manin, Y., Zograf, P.: Invertible cohomological field theories and Weil-Petersson volumes. Ann. Inst. Fourier 50, 519–535 (2000)

[McD] McDuff, D.: Introduction to Symplectic Topology. Providence, RI: Am. Math. Soc. 1999

[M]McShane, G.: Simple geodesics and a series constant over Teichmüller space. Invent. Math. 132, 607–632 (1998)

[Mirz1] Mirzakhani, M.: Growth of the number of simple closed geodesics on a hyperbolic surface. To appear in Ann. Math.

[Mirz2] Mirzakhani, M.: Weil-Petersson volumes and intersection theory on the moduli space of curves. To appear in J. Am. Math. Soc.

[NN] Nakanishi, T., Näätänen, M.: Areas of two-dimensional moduli spaces. Proc. Am. Math. Soc. 129, 3241–3252 (2001)

[Pen] Penner, R.: Weil-Petersson volumes. J. Differ. Geom. 35, 559–608 (1992)

[TWZ1] Tan, S.P., Wong, Y., Zhang, Y.: Necessary and sufficient conditions for McShane’s identity and variations. Preprint 2004

[TWZ2] Tan, S.P., Wong, Y., Zhang, Y.: Generalizations of McShane’s identity to hyperbolic cone-surfaces. J. Differ. Geom. 72, 73–111 (2006)

[Wol1] Wolpert, S.: The Fenchel-Nielsen deformation. Ann. Math. 115, 501–528 (1982)

[Wol2] Wolpert, S.: On the homology of the moduli space of stable curves. Ann. Math. (2) 118, 491–523 (1983)

[Zo]Zograf, P.: The Weil-Petersson volume of the moduli space of punctured spheres. In: Mapping Class Groups and Moduli Spaces of Riemann Surfaces. Contemp. Math., vol. 150, pp. 367–372. Providence, RI: Am. Math. Soc. 1993