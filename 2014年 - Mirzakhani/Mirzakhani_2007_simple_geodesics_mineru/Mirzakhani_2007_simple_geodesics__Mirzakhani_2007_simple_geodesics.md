# Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces

Maryam Mirzakhani

July 12, 2005

1 Introduction 1  
2 Background material 8  
3 Geometry of pairs of pants 13  
4 Generalized McShane identity for bordered surfaces 18  
5 Statement of the recursive formula for volumes 27  
6 Polynomial behavior of the Weil-Petersson volume 30  
7 Leading coefficients of volume polynomials 34  
8 Integration over the moduli space 36  
9 Volumes of moduli spaces of bordered Riemann surfaces 43

## 1 Introduction

In this paper we investigate the Weil-Petersson volume of the moduli space of curves with marked points. We develop a method for integrating geometric functions over these moduli spaces, and obtain an efective recursive formula for the volume$V _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$of the moduli space$\mathcal { M } _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$ of hyperbolic Riemann surfaces of genus$g$with n geodesic boundary components. We show that$V _ { g , n } ( L )$is a polynomial whose coeficients are rational multiples of powers of$\pi .$The constant term of the polynomial$V _ { g , n } ( L )$is the Weil-Petersson volume of the traditional moduli space of closed surfaces of genus g with n marked points.

In forthcoming papers, we will use these results to investigate problems related to the distribution of the lengths of simple closed geodesics on hyperbolic surfaces, volume of - thin part of the moduli space and intersection theory on moduli spaces of curves.

Volume of the moduli space. When studying volumes of moduli spaces of hyperbolic Riemann surfaces with cusps, it proves fruitful to consider more generally bordered hyperbolic Riemann surfaces with geodesic boundary components. Given$L = ( L _ { 1 } , \ldots , L _ { n } ) \in ( \mathbb { R } _ { > 0 } ) ^ { n }$, the mapping class group $\operatorname { M o d } _ { g , n }$acts on the Teichm¨uller space$\mathcal { T } _ { g , n } ( L )$of hyperbolic structures with geodesic boundary components of length$L _ { 1 } , \ldots , L _ { n }$. We study the Weil-Petersson volume of the quotient space

$$
\mathcal {M} _ {g, n} (L) = \mathcal {T} _ {g, n} (L) / \operatorname{Mod} _ {g, n}.
$$

Our main result, obtained in$\ S 6 .$, is:

Theorem 1.1. The volume$V _ { g , n } ( L _ { 1 } , \ldots , L _ { n } ) = \operatorname { V o l } _ { w p } ( \mathcal { M } _ { g , n } ( L ) )$is a polynomial in$L _ { 1 } , \ldots , L _ { n } ;$namely we have:

$$
V_{g,n}(L) = \sum_{\substack{\alpha \\ |\alpha |\leq 3g - 3 + n}}C_{\alpha}\cdot L^{2\alpha},
$$

where$C _ { \alpha } > 0$lies in$\pi ^ { 6 g - 6 + 2 n - | 2 \alpha | } \cdot \mathbb { Q }$Q.

Here the exponent$\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ranges over elements in$( \mathbb { Z } _ { \geq 0 } ) ^ { n }$9 $L ^ { \alpha } = L _ { 1 } ^ { \alpha _ { 1 } } \cdot \cdot \cdot L _ { n } ^ { \alpha _ { n } }$, and$| \alpha | = \sum _ { i = 1 } ^ { n } \alpha _ { i }$

Moreover, in$\ S 5$we give an explicit recursive formula for calculating these volumes. For example, we have:

$$
V _ {1, 1} (L) = L ^ {2} / 2 4 + \pi^ {2} / 6.
$$

For more examples see Table 1.

In particular, the Weil-Petersson volume of the moduli space of curves of genus g with n marked point, the constant term of$V _ { g , n } ( L )$, is a rational multiple of$\pi ^ { 6 g - 6 + 2 n }$. This result was previously obtained by S. Wolpert [Wol2]. A formula for${ \mathrm { V o l } } _ { 0 , n } ( 0 )$, the Weil-Petersson volume of$\mathcal { M } _ { 0 , n } .$, was obtained in [Zo].

Remark. Note that there is a diference in the normalization of the volume form; in$[ \mathrm { Z o } ]$the Weil-Petersson K¨ahler form is$1 / 2$the imaginary part of the Weil-Petersson pairing, while here we work with the imaginary part of the pairing. So our answers are diferent by a power of 2.

Table 1. Volumes of moduli spaces of curves

| g | n | $V_{g,n}(L)$ |
| --- | --- | --- |
| 0 | 3 | 1 |
| 1 | 1 | $\frac{1}{24}(L^2 + 4\pi^2)$ |
| 0 | 4 | $\frac{1}{2}(4\pi^2 + L_1^2 + L_2^2 + L_3^2 + L_4^2)$ |
| 1 | 2 | $\frac{1}{192}(4\pi^2 + L_1^2 + L_2^2)(12\pi^2 + L_1^2 + L_2^2)$ |
| 0 | 5 | $\frac{1}{8}\left(80\pi^4 + \sum_{i=1}^{5} L_i^4 + 4 \sum_{1 \leq i < j \leq 5} L_i^2 L_j^2 + 24\pi^2 \sum_{i=1}^{5} L_i^2\right)$ |
| 2 | 1 | $\frac{1}{2211840}\left(4\pi^2 + L_1^2\right)\left(12\pi^2 + L_1^2\right)\left(6960\pi^4 + 384\pi^2 L_1^2 + 5 L_1^4\right)$ |

We approach the calculation of these volumes by studying the lengths of simple closed geodesics on$X \in \mathcal { M } _ { g , n }$. Our main tool is a generalization of McShane’s identity [M], which gives us a way to calculate the volume of the moduli space$\mathcal { M } _ { g , n } = \mathcal { T } _ { g , n } / \mathrm { M o d } _ { g , n }$without having to find a fundamental domain for the action of the mapping class group on Teichm¨uller space. McShane identity. Our point of departure for calculating these volume polynomials is the following result [M]:

Theorem 1.2 (McShane). Let X be a hyperbolic once-punctured torus. Then we have

$$
\sum_ {\gamma} (1 + e ^ {\ell_ {\gamma} (X)}) ^ {- 1} = \frac {1}{2},\tag{1.1}
$$

where the sum is over all simple closed geodesics$\gamma$on$X$.

Calculation of$\mathrm { V o l } ( \mathcal { M } _ { 1 , 1 } )$. We briefly explain the relation between Mc-Shane’s identity and Weil-Petersson volumes by treating the case$g = n = 1$

Consider the space of pairs:

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

For any simple closed curve α on a hyperbolic once punctured torus, we have$\mathcal { M } _ { 1 . 1 } ^ { \ast } = \mathcal { T } _ { 1 , 1 } / \mathrm { S t a b } ( \alpha )$. Now we use the Fenchel-Nielsen coordinates for $\mathcal { T } _ { 1 , 1 }$about α; Any element$( X , \gamma ) \in \mathcal { M } _ { 1 , 1 } ^ { * }$is determined by the pair$( \ell , \tau )$，the length and the twisting parameter of$X$around$\gamma$. Note that we have $\phi _ { \gamma } ( \ell , \tau ) = ( \ell , \ell + \tau )$, where$\phi _ { \gamma }$denotes a right Dehn twist around$\gamma$. Hence we have

$$
\mathcal {M} _ {1, 1} ^ {*} \cong \left\{(\ell , \tau) | 0 \leq \ell \leq \tau \right\} / (x, 0) \sim (x, x).
$$

The Weil-Petersson symplectic form in Fenchel-Nielsen coordinates is given by$\pi ^ { * } ( \omega _ { w p } ) = d \ell \wedge d \tau$. Therefore, we have

$$
\int_ {\mathcal {M} _ {1, 1}} \sum_ {\pi (Y) = X} f (\ell (Y)) d X = \int_ {\mathcal {M} _ {1, 1} ^ {*}} f (\ell (Y)) d Y = \int_ {0} ^ {\infty} f (x) \int_ {0} ^ {x} 1 d y d x.
$$

Integrating McShane’s identity (1.2) over$\mathcal { M } _ { 1 , 1 }$against the Weil-Petersson volume form, we obtain

$$
\operatorname{Vol} \left(\mathcal {M} _ {1, 1}\right) = 2 \int_ {0} ^ {\infty} \ell f (\ell) d \ell = 2 \int_ {0} ^ {\infty} \frac {\ell}{1 + e ^ {\ell}} d \ell = \frac {\pi^ {2}}{6}.
$$

Calculation of$V _ { g , n }$. To carry out a similar analysis for${ \mathcal { M } } _ { g , n }$we will:

(I): Generalize McShane identity (Theorem 1.2) to arbitrary hyperbolic surfaces with geodesic boundary components ( 4), and

(II): Develop a method to integrate functions given in terms of the hyperbolic length functions over the moduli space ( 8).

The result is a recursive formula for the volume polynomial$V _ { g , n } ( L )$obtained in 9.

We now turn into a more detailed account of two main steps of the proof: (I): Generalized McShane’s identity. McShane [M] gives a version of formula (1.1) for punctured Riemann surfaces of higher genus. In our discussion, we need a further generalization to bordered Riemann surfaces with geodesic boundary components. Roughly speaking, we want to find a function defined on Teichm¨uller space such that the sum of its values over the elements of each orbit of$\operatorname { M o d } _ { g , n }$is a constant independent of the orbit. In 3 we introduce two auxiliary functions$\mathcal { D } , \mathcal { R } : \mathbb { R } _ { + } ^ { 3 }  \mathbb { R } _ { + }$related to the geometry of hyperbolic pairs of pants. A central role in our approach to volumes of moduli spaces is played by the following result ( 4 ):

Theorem 1.3. For any hyperbolic surface X with n geodesic boundary components$\beta _ { 1 } , \ldots , \beta _ { n }$of lengths$L _ { 1 } , \ldots , L _ { n }$, we have

$$
\sum_ {\{\alpha_ {1}, \alpha_ {2} \}} \mathcal {D} (L _ {1}, \ell_ {\alpha_ {1}} (X), \ell_ {\alpha_ {2}} (X)) + \sum_ {i = 2} ^ {n} \sum_ {\gamma} \mathcal {R} (L _ {1}, L _ {i}, \ell_ {\gamma} (X)) = L _ {1}.\tag{1.3}
$$

Here the first sum is over all unordered pairs of simple closed geodesics $\{ \alpha _ { 1 } , \alpha _ { 2 } \}$bounding a pair of pants with$\beta _ { 1 }$, and the second sum is over simple closed geodesics γ bounding a pairs of pants with$\beta _ { 1 }$and$\beta _ { i }$.

In the formula above, we also allow$\beta _ { i }$to be a cusp of$X$, by regarding it as a geodesic of length 0.

As a special case, for any hyperbolic surface X of genus one with one geodesic boundary component of length L, we get

$$
\sum_ {\gamma} \mathcal {D} (L, \ell_ {\gamma} (X), \ell_ {\gamma} (X)) = L,\tag{1.4}
$$

where the sum is over all simple closed geodesics$\gamma$on$X$. On the other hand, we have ( 3)

$$
\mathcal {D} (x, y, y) \sim \frac {2 x}{1 + e ^ {y}}
$$

as$x \to 0$, therefore our formula for genus one hyperbolic surfaces with one geodesic boundary component (1.4) implies the original McShane identity (1.1) when$L \to 0$

(II): Integration over the moduli space. In$\ S 8$, we develop a method for integrating the right hand side of the identity for the lengths of simple closed geodesics (1.3) over${ \mathcal { M } } _ { g , n } ( L )$. Working with bordered Riemann surfaces allows us to exploit the existence of commuting Hamiltonian$S ^ { 1 }$-actions on certain coverings of the moduli space in order to integrate certain geometric functions over the moduli space of curves.

Let$S _ { g , n }$be a closed surface of genus$g$with n boundary components and $Y \in \mathcal { T } _ { g , n }$. For any simple closed curve$\gamma$on$S _ { g , n } ,$, let$[ \gamma ]$denote the homotopy class of$\gamma$and let$\ell _ { \gamma } ( Y )$denote the hyperbolic length of the geodesic representative of [γ] on$Y$.

To each simple closed curve$\gamma$on$S _ { g , n }$, we associate the set

$$
\mathcal {O} _ {\gamma} = \{[ \alpha ] | \alpha \in \operatorname{Mod} _ {g, n} \cdot \gamma \}
$$

of homotopy classes of simple closed curves in the$\mathrm { M o d } _ { g , n ^ { - 0 } }$rbit of$\gamma$on $X \in \mathcal { M } _ { g , n }$. For any function$f : \mathbb { R } _ { + } \longrightarrow \mathbb { R } _ { + }$，

$$
f _ {\gamma} (X) = \sum_ {[ \alpha ] \in \mathcal {O} _ {\gamma}} f (\ell_ {\alpha} (X)),
$$

defines a function

$$
f _ {\gamma}: \mathcal {M} _ {g, n} \to \mathbb {R}.
$$

Here we sketch the main idea of calculating the integral of$f _ { \gamma }$over${ \mathcal { M } } _ { g , n }$with respect to the Weil-Petersson volume form when$\gamma$is a connected simple closed curve. See Theorem 8.1 for the general case.

First, consider the covering space of${ \mathcal { M } } _ { g , n }$

$\pi ^ { \gamma } : \mathcal { M } _ { g , n } ^ { \gamma } = \{ ( X , \alpha ) \ | \ X \in \mathcal { M } _ { g , n }$, and α$\in { \mathcal { O } } _ { \gamma }$is a geodesic on$X \} \to { \mathcal { M } } _ { g , n }$ where$\pi ^ { \gamma } ( X , \alpha ) = X$. The hyperbolic length function descends to the function,

$$
\ell : \mathcal {M} _ {g, n} ^ {\gamma} \to \mathbb {R}
$$

defined by$\ell ( X , \eta ) = \ell _ { \eta } ( X )$. Therefore, we have

$$
\int_ {\mathcal {M} _ {g, n}} f _ {\gamma} (X) d X = \int_ {\mathcal {M} _ {g, n} ^ {\gamma}} f \circ \ell (Y) d Y.
$$

On the other hand, The function$f$is constant on each level set of$\ell$and we have

$$
\int_ {\mathcal {M} _ {g, n} ^ {\gamma}} f \circ \ell (Y) d Y = \int_ {0} ^ {\infty} f (t) \operatorname{Vol} (\ell^ {- 1} (t)) d t,
$$

where the volume is taken with respect to the volume form$- * d \ell$on$\ell ^ { - 1 } ( t )$

The main idea for integrating over$\mathcal { M } _ { g , n } ^ { \gamma }$is that the decomposition of the surface along γ gives rise to a description of$\mathcal { M } _ { g , n } ^ { \gamma }$in terms of moduli spaces corresponding to simpler surfaces. This leads to formulas for the integral of$f _ { \gamma }$in terms of the Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces and the function$f$

Let$S _ { g , n } ( \gamma )$be the result of cutting the surface$S _ { g , n }$along$\gamma ;$that is $S _ { g , n } ( \gamma ) \cong S _ { g , n } - U _ { \gamma }$, where$U _ { \gamma }$is an open neighborhood of$\gamma$homeomorphic to$\gamma \times ( 0 , 1 )$. Thus$S _ { g , n } ( \gamma )$is a possibly disconnected compact surface with $n + 2$boundary components. We define$\mathcal { M } ( S _ { g , n } ( \gamma ) , \ell _ { \gamma } = t )$to be the moduli space of Riemann surfaces homeomorphic to$S _ { g , n } ( \gamma )$such that the lengths of the 2 boundary components corresponding to$\gamma$are equal to t. We have a natural circle bundle

$$
\begin{array}{c} \ell^ {- 1} (t) \subset \mathcal {M} _ {g, n} ^ {\gamma} \\ \Big \downarrow \\ \mathcal {M} (S _ {g, n} (\gamma), \ell_ {\gamma} = t) \end{array}
$$

We will study the$S ^ { 1 }$-action on the level set$\ell ^ { - 1 } ( t ) \subset \mathcal { M } _ { g , n } ^ { \gamma }$induced by twisting the surface along$\gamma .$The quotient space$\ell ^ { - 1 } ( t ) / S ^ { 1 }$inherits a symplectic form from the Weil-Petersson symplectic form. On the other hand, $\mathcal { M } ( S _ { g , n } ( \gamma ) , \ell _ { \gamma } = t )$is equipped with the Weil-Petersson symplectic form. By investigating these$S ^ { 1 }$-actions in more detail in$\ S 8$we show that

$$
\ell^ {- 1} (t) / S ^ {1} \cong \mathcal {M} (S _ {g, n} (\gamma), \ell_ {\gamma} = t)
$$

as symplectic manifolds. So we expect to have

$$
\mathrm{Vol} (\ell^ {- 1} (t)) = t \mathrm{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\gamma} = t)).
$$

But as we will see in$\ S 8 .$, the situation is diferent when$\gamma$seperates of a one-handle in which case the length of the fiber at a point is in fact$t / 2$ instead of t. For any connected simple closed curve$\gamma$on$S _ { g , n } ,$we have

$$
\int_ {\mathcal {M} _ {g, n}} f _ {\gamma} (X) d X = 2 ^ {- M (\gamma)} \int_ {0} ^ {\infty} f (t) t \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\gamma} = t)) d t,\tag{1.5}
$$

where$M ( \gamma ) = 1 { \mathrm { i f } } \gamma$seperates of a one-handle, and$M ( \gamma ) = 0$otherwise. An alternative proof of Theorem 1.1. The method of symplectic reduction can be used to show that$V _ { g , n } ( L )$is a polynomial in$L .$In a sequel, we obtain a formula for$V _ { g , n } ( L )$in terms of intersection numbers of tautological classes over${ \overline { { \mathcal { M } } } } _ { g , n }$. However, this symplectic method does not lead us to a recursive algorithm for calculating the volumes explicitly.

Applications. In forthcoming papers, we will study the connection of the polynomial$V _ { g , n } ( L )$with the length distribution of simple closed geodesics on a hyperbolic surface [Mirz1]. We also relate the coeficients of the volume polynomial$V _ { g , n } ( L )$to intersection numbers of tautological line classes on ${ \overline { { \mathcal { M } } } } _ { g , n }$[Mirz2]. The algorithm for calculating$V _ { g , n } ( L )$presented in 5 leads to a new proof of the Virasoro constraints for a point which is equivalent to the Witten-Kontsevich formula [K].

Notes and references. The Weil-Petersson volume of the moduli space of punctured Riemann surfaces arises naturally in diferent contexts[KMZ]. A recursive formula for the Weil-Petersson volume of the moduli space of punctured spheres was obtained by Zograf [Zo]. Moreover, Zograf and Manin have obtained generating functions for the Weil-Petersson volume of${ \mathcal { M } } _ { g , n }$ [MaZ]. Also, R. Penner has developed a diferent method for calculating the Weil-Petersson volume of the moduli spaces of curves with marked points by using decorated Teichm¨uller theory and calculated the Weil-Petersson volume of$\mathcal { M } _ { 1 , 2 }$[Pen]. The volume polynomial$V _ { 1 , 1 } ( L )$was also previously obtained in [NN] by finding a fundamental domain for the action of the mapping class group on Teichm¨uller space.

Acknowledgments. I would like to thank Curt McMullen for his invaluable help and many stimulating discussions over the course of this work. I am also grateful to Said Akbari, Izzet Coskun, Maxim Kontsevich, Chiu-Chu Melissa Liu, Andrei Okounkov, Rahul Pandharipandeh, S.T. Yau and Igor Riven for helpful discussions. I would like to thank Greg McShane and Scott Wolpert for many helpful comments and dscussions. The author would also like to thank the Max Planck Institute of Mathematics in Leipzig and the Institute for Studies in Theoretical Physics and Mathematics (IPM) in Tehran for their hospitality during the writing of this paper.

## 2 Background material

In this section, We present some familiar concepts in a less familiar setting about the symplectic structure of the moduli space of bordered Riemann surfaces and the space of measured geodesic laminations. we also recall some basic facts and results on hyperbolic geometry.

Recall that a symplectic structure on a manifold M is a non-degenerate

closed 2-form$\omega \in \Omega ^ { 2 } ( M )$. The n-fold wedge product

$$
\frac {1}{n !} \omega \wedge \dots \wedge \omega
$$

never vanishes and defines a volume form on$M .$

Teichm¨uller Space. Here we briefly summarize the background material on Teichm¨uller theory of Reimann surfaces with geodesic boundary components.

A point in the Teichm¨uller space$\boldsymbol { \mathcal { T } } ( \boldsymbol { S } )$is a complete hyperbolic surface X equipped with a difeomorphism$f : S  X$. The map$f$provides a marking on X by S. Two marked surfaces$f : \ S \to X$and$g : \ S \to Y$define the same point in$\boldsymbol { \mathcal { T } } ( \boldsymbol { S } )$if and only if$f \circ g ^ { - 1 } : Y \to X$is isotopic to a conformal map. When ∂S is nonempty, consider hyperbolic Riemann surfaces homeomorphic to S with geodesic boundary components of fixed length. Let$A = \partial S$and$L = ( L _ { \alpha } ) _ { \alpha \in A } \in \mathbb { R } _ { + } ^ { | A | }$. A point$X \in \mathcal { T } ( S , L )$is a marked hyperbolic surface with geodesic boundary components such that for each boundary component$\beta \in \partial S$, we have

$$
\ell_ {\beta} (X) = L _ {\beta}.
$$

Let$S _ { g , n }$be an oriented connected surface of genus$g$with n boundary components$( \beta _ { 1 } , \ldots , \beta _ { n } )$. Then

$$
\mathcal {T} _ {g, n} (L _ {1}, \ldots , L _ {n}) = \mathcal {T} (S _ {g, n}, L _ {1}, \ldots , L _ {n}),
$$

denote the Teichm¨uller space of hyperbolic structures on$S _ { g , n }$with geodesic boundary components of length$L _ { 1 } , \ldots , L _ { n }$. By convention, a boundary geodesic of length zero is a cusp and we have

$$
\mathcal {T} _ {g, n} = \mathcal {T} _ {g, n} (0, \dots , 0).
$$

Let Mod(S) denote the mapping class group of$S _ { i }$, or the group of isotopy classes of orientation preserving self homeomorphisms of S leaving each boundary component set wise fixed. The mapping class group${ \mathrm { M o d } } _ { g , n } =$ Mod$( S _ { g , n } )$acts on$\mathcal { T } _ { g , n } ( L )$by changing the marking. The quotient space

$$
\mathcal {M} _ {g, n} (L) = \mathcal {M} (S _ {g, n}, \ell_ {\beta_ {i}} = L _ {i}) = \mathcal {T} _ {g, n} (L _ {1}, \ldots , L _ {n}) / \mathrm{Mod} _ {g, n}
$$

is the moduli space of Riemann surfaces homeomorphic to$S _ { g , n }$with n boundary components of length$\ell _ { \beta _ { i } } = L _ { i }$. Also, we have

$$
\mathcal {M} _ {g, n} = \mathcal {M} _ {g, n} (0, \dots , 0).
$$

For a disconnected surface$S = \bigcup _ { i = 1 } ^ { k } S _ { i }$such that$A _ { i } = \partial S _ { i } \subset \partial S$, we have

$$
\mathcal {M} (S, L) = \prod_ {i = 1} ^ {k} \mathcal {M} (S _ {i}, L _ {A _ {i}}),
$$

where$L _ { A _ { i } } = ( L _ { s } ) _ { s \in A _ { i } }$

The Weil-Petersson symplectic form. By work of Goldman [Gol], the space$T _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$carries a natural symplectic form invariant under the action of the mapping class group. Th is symplectic form is called Weil-Petersson symplectic form, and denoted by$\omega$or$\omega _ { w p }$. In this paper, we are interested in calculating the volume of the moduli space with respect to the volume form induced by the Weil-Petersson symplectic form. Note that when S is disconnected, we have

$$
\operatorname{Vol} (\mathcal {M} (S, L)) = \prod_ {i = 1} ^ {k} \operatorname{Vol} (\mathcal {M} (S _ {i}, L _ {A _ {i}})).
$$

The Fenchel-Nielsen coordinates. A pants decomposition of$S$is a set of disjoint simple closed curves which decompose the surface into pairs of pants. Fix a system of pants decomposition of$S _ { g , n } , \mathcal { P } = \{ \alpha _ { i } \} _ { i = 1 } ^ { k }$, where$k = 6 g - 6 +$ 2n. For a marked hyperbolic surface$X \in \mathcal { T } _ { g , n } ( L )$, the Fenchel-Nielsen coordinates associated with ,$\{ \ell _ { \alpha _ { 1 } } ( X ) , \ldots , \ell _ { \alpha _ { k } } ( X ) , \tau _ { \alpha _ { 1 } } ( X ) , \ldots , \tau _ { \alpha _ { k } } ( X ) \}$, consists of the set of lengths of all geodesics used in the decomposition and the set of the twisting parameters used to glue the pieces. We have an isomorphism

$$
\mathcal {T} _ {g, n} (L) \cong \mathbb {R} _ {+} ^ {\mathcal {P}} \times \mathbb {R} ^ {\mathcal {P}}
$$

by the map

$$
X \to (\ell_ {\alpha_ {i}} (X), \tau_ {\alpha_ {i}} (X)).
$$

By work of Wolpert, over Teichm¨uller space the Weil-Petersson symplectic structure has a simple form in Fenchel-Nielsen coordinates [Wol1].

Theorem 2.1 (Wolpert). The Weil-Petersson symplectic form is given by

$$
\omega_ {w p} = \sum_ {i = 1} ^ {k} d \ell_ {\alpha_ {i}} \wedge d \tau_ {\alpha_ {i}}.
$$

Twisting. For any simple closed geodesic α on$X \in \mathcal { T } _ { g , n } ( L )$and$t \in \mathbb { R }$, we can deform the hyperbolic structure as follows. We cut the surface along α, turn left hand side of α in the positive direction the distance t and reglue back. Let us denote the new surface by$t w _ { t \alpha } ( X )$. As t varies, the resulting continuous path in Teichm¨uller space is the Fenchel-Nielsen deformation of X along α. For$t = \ell _ { \alpha } ( X )$, we have

$$
t w _ {t \alpha} (X) = \phi_ {\alpha} (X),
$$

where$\phi _ { \alpha } \in \operatorname { M o d } ( S _ { g , n } )$is a right Dehn twist about α.

$\mathrm { B y }$Wolpert’s result (Theorem 2.1), the vector field generated by twisting around α is symplectically dual to the exact one form$d \ell _ { \alpha }$. In other words, $t w _ { t \alpha }$is the Hamiltonian flow of the length function.

Splitting along a simple closed curve.

![](images/page_10_image_5.jpg)

Figure 1. Cutting the surface

Let γ

$$
\gamma = \sum_ {i = 1} ^ {k} c _ {i} \gamma_ {i},
$$

where$\gamma _ { 1 } , \ldots$. and$\gamma _ { k }$are distinct, disjoint simple closed curves, be the isotopy class of a multi curve on$S _ { g , n } .$

Consider the surface$S _ { g , n } - U _ { \gamma }$, where$U _ { \gamma }$is an open set homeomorphic to${ \textstyle \bigcup _ { 1 } ^ { k } ( 0 , 1 ) } \times \gamma _ { i }$around γ. We denote this surface by$S _ { g , n } ( \gamma )$, which is a (possibly disconnected) surface with$n + 2 k$boundary components and $s = s ( \gamma )$connected components. Each connected component$\gamma _ { i }$of γ, gives rise to 2 boundary components,$\gamma _ { i } ^ { 1 }$and$\gamma _ { i } ^ { 2 }$on$S _ { g , n } ( \gamma )$. Namely,

$$
\partial (S _ {g, n} (\gamma)) = \{\beta_ {1}, \dots , \beta_ {n} \} \cup \{\gamma_ {1} ^ {1}, \gamma_ {1} ^ {2}, \dots , \gamma_ {k} ^ {1}, \gamma_ {k} ^ {2} \}.
$$

Now for$\Gamma = ( \gamma _ { 1 } , \ldots , \gamma _ { k } ) , L = ( L _ { 1 } , \ldots , L _ { n } )$and$\mathbf { x } = ( x _ { 1 } , \ldots , x _ { k } ) \in \mathbb { R } _ { + } ^ { k }$, let

$$
\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)
$$

be the moduli space of hyperbolic Riemann surfaces homeomorphic to$S _ { g , n } ( \gamma )$ such that$\ell _ { \gamma _ { i } } = x _ { i }$and$\ell _ { \beta _ { i } } = L _ { i }$. Also, define$V _ { g , n } ( \Gamma , \mathbf { x } , \beta , L )$by

$$
V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) = \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)).
$$

We can write$S _ { g , n } ( \gamma )$as a union of its connected components

$$
S _ {g, n} (\gamma) = \bigcup_ {i = 1} ^ {s} S _ {g _ {i}, n _ {i}}, A _ {i} = \partial S _ {i} \subset \mathcal {B}.\tag{2.1}
$$

Then in terms of the above notation, we have

$$
\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L) \cong \prod_ {i = 1} ^ {s} \mathcal {M} _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}}),
$$

where$\ell _ { A _ { i } } = ( \ell _ { \alpha } ) _ { \alpha \in A _ { i } }$, and consequently we get

$$
V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) = \prod_ {i = 1} ^ {s} V _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}}).
$$

Symmetry group of a multi curve. For any set A of homotopy classes of simple closed curves on$S _ { g , n }$, define$\operatorname { S t a b } ( A )$by

$$
\operatorname{Stab} (A) = \left\{h \in \operatorname{Mod} _ {g, n} \mid h \cdot A = A \right\} \subset \operatorname{Mod} _ {g, n}.
$$

For$\gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i }$, define the symmetry group of$\gamma , \operatorname { S y m } ( \gamma )$, by

$$
\operatorname{Sym} (\gamma) = \operatorname{Stab} (\gamma) / \cap_ {i = 1} ^ {k} \operatorname{Stab} (\gamma_ {i}).
$$

In fact, when$\gamma$has extra symmetry

$$
\bigcap_ {i = 1} ^ {k} \operatorname{Stab} (\gamma_ {i}) \neq \operatorname{Stab} (\gamma).
$$

First, for any connected simple closed curve$\alpha , | \mathrm { S y m } ( \alpha ) | = 1$

Note$| \operatorname { S y m } ( \gamma ) | \neq 1$for

$$
\gamma = \sum_ {i = 1} ^ {k} c _ {i} \gamma_ {i}
$$

will put a non trivial condition on the$c _ { i } ^ { \prime } \mathrm { s }$. For example$| \operatorname { S y m } ( \gamma ) | = k !$ implies that$c _ { 1 } = c _ { 2 } = . . . = c _ { k }$

When$k = 2$, by the definition

$$
| \mathrm{Sym} (\gamma_ {1} + \gamma_ {2}) | = 2
$$

if and only if$S _ { g , n } ( \gamma _ { 1 } )$is homeomorphic to$S _ { g , n } ( \gamma _ { 2 } )$. Here we want the homemorphisem to fix each boundary component of$\partial ( S _ { g , n } )$setwise, and send$\gamma _ { 1 }$to$\gamma _ { 2 }$.

Later we will be interested in the case where$\gamma$bounds a pair of pants with a boundary component of$S _ { g , n }$. It is easy to check that$| \mathrm { S y m } ( \gamma _ { 1 } + \gamma _ { 2 } ) | = 2$ if and only either$S _ { g , n } ( \gamma )$is connected or

$$
S _ {g, n} (\gamma) \cong S _ {g _ {1}, 1} \cup S _ {g _ {1}, 1}.
$$

Simple closed curves on$X \in \mathcal { M } _ { g , n } .$. Let [γ] denotes the homotopy class of a simple closed curve γ on$S _ { g , n }$. Although there is no canonical simple closed geodesic on$X \in \mathcal { M } _ { g , n }$corresponding to [γ], the set

$$
\mathcal {O} _ {\gamma} = \{[ \alpha ] | \alpha \in \operatorname{Mod} \cdot \gamma \},
$$

of homotopy classes of simple closed curves in the${ \mathrm { M o d } } _ { g , n ^ { - } } { \mathrm { o r b i t } }$of γ on X, is determined by γ. In other words,$\mathcal { O } _ { \gamma }$is the set of$\left[ \phi ( \gamma ) \right]$where$\phi : S _ { g , n } \to X$ is a marking of X. Let$\ell _ { \alpha } ( X )$denote the hyperbolic length of α on X. Here, we study functions of the form

$$
f _ {\gamma}: \mathcal {M} _ {g, n} \to \mathbb {R} _ {+}
$$

$$
X \to \sum_ {\alpha \in \mathcal {O} _ {\gamma}} f (\ell_ {\alpha} (X)),
$$

where$f : \mathbb { R } \to \mathbb { R } _ { + }$

As an example, for$f = \chi [ 0 , L )$, the characteristic function of$[ 0 , L ) , f _ { \gamma } ( X )$ is equal to the number of elements of$\mathcal { O } _ { \gamma }$of length less than L on$X$

## 3 Geometry of pairs of pants

In this section we study infinite simple geodesic rays on a hyperbolic pair of pants. For background on hyperbolic geometry see [Bus].

A pair of pants is an oriented compact surface homeomorphic to$S _ { \mathrm { 0 , 3 } }$, a surface of genus-0 with three boundary components.

Let$\mathcal { C } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$be the unique hyperbolic pair of pants with geodesic boundary curves$( \beta _ { i } ) _ { i = 1 } ^ { 3 }$such that$\ell _ { \beta _ { i } } ( \mathcal { C } ) = x _ { i } , i = 1 , 2 , 3$. We also allow the degenerate case in which one or more of the lengths vanish.

![](images/page_13_image_0.jpg)

Figure 2. complete geodesics in a pair of pants

Each boundary component of has two canonical points, the end points of the length minimizing geodesics connecting it to the other two boundary components.

On the other hand, we can obtain$\mathcal { C } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$by pasting two copies of the (unique) right angled geodesic hexagons with pairwise non-adjacent sides of length$x _ { 1 } / 2 , x _ { 2 } / 2$and$x _ { 3 } / 2$along the remaining three sides. Thus $\mathcal { C } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$admits a reflection involution$\sigma$which interchanges the two hexagons.

Complete geodesics on hyperbolic a pair of pants. A hyperbolic pair of pants contains 5 complete geodesics disjoint from$\beta _ { 2 } , \beta _ { 3 }$and orthogonal to$\beta _ { 1 }$. More precisely, 2 of these geodesics meet$\beta _ { 1 }$at$y _ { 1 }$and$y _ { 2 }$and spiral around$\beta _ { 3 }$, the other 2 meet$\beta _ { 1 }$at$z _ { 1 }$and$z _ { 2 }$and spiral around$\beta _ { 2 }$. There is also a unique common simple geodesic perpendicular from$\beta _ { 1 }$to itself meeting$\beta _ { 1 }$perpendicularly at 2 points,$w _ { 1 }$and$w _ { 2 }$. Note that we have $\sigma ( w _ { 1 } ) = w _ { 2 } , \sigma ( z _ { 1 } ) = z _ { 2 }$, and$\sigma ( y _ { 1 } ) = y _ { 2 }$. See Figure 2.

Definitions. Define$\mathcal { R } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$to be the geodesic length of$( y _ { 1 } , y _ { 2 } )$, the interval between$y _ { 1 }$and$y _ { 2 }$along$\beta _ { 1 }$containing$w _ { 1 }$and$w _ { 2 }$. For caclulating the function$\mathcal { R }$, we consider the universal cover of . Then it is easy to check that

$$
x _ {1} - \mathcal {R} (x _ {1}, x _ {2}, x _ {3})
$$

is equal to the geodesic length of the projection of$\beta _ { 3 }$on$\beta _ { 1 }$. See Figure 3. Note that this length does not depend on the choice of the lift of$\mathcal { C } .$.

Also, define$\mathcal { D } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$to be the sum of the geodesic length of$( y _ { 1 } , z _ { 1 } )$ and$( y _ { 2 } , z _ { 2 } )$, the interval between$y _ { i }$and$z _ { i }$containing$w _ { i }$on$\beta _ { 1 }$. So the function$\mathcal { D } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$is twice the geodesic distance between two geodesics perpendicular to$\beta _ { 1 }$spiraling around$\beta _ { 2 }$and$\beta _ { 3 }$. Equivalently in the universal cover of$\mathcal { C } , \mathcal { D } ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$equals 2 times the distance between the projection of$\beta _ { 2 }$and$\beta _ { 3 }$on$\beta _ { 1 }$.

![](images/page_14_chart_0.jpg)

Figure 3. Projection of a geodesic

Also, define$H : \mathbb { R } ^ { 2 }  \mathbb { R }$by

$$
H (x, y) = \frac {1}{1 + e ^ {\frac {x + y}{2}}} + \frac {1}{1 + e ^ {\frac {x - y}{2}}}.
$$

Basic properties of  and$\mathcal { R }$. It can be easily checked that the functions $\mathcal { D }$and  satisfy

$$
\mathcal {D} (x _ {1}, x _ {2}, x _ {3}) = \mathcal {D} (x _ {1}, x _ {3}, x _ {2}),
$$

and

$$
\mathcal {R} (x _ {1}, x _ {2}, x _ {3}) + \mathcal {R} (x _ {1}, x _ {3}, x _ {2}) = x _ {1} + \mathcal {D} (x _ {1}, x _ {2}, x _ {3}).
$$

Moreover, one can explicitly calculate these functions and show that:

Lemma 3.1. The functions  and  are given by

$$
\mathcal {D} (x, y, z) = 2 \log \left(\frac {e ^ {\frac {x}{2}} + e ^ {\frac {y + z}{2}}}{e ^ {\frac {- x}{2}} + e ^ {\frac {y + z}{2}}}\right),\tag{3.1}
$$

and

$$
\mathcal {R} (x, y, z) = x - \log \left(\frac {\cosh (\frac {y}{2}) + \cosh (\frac {x + z}{2})}{\cosh (\frac {y}{2}) + \cosh (\frac {x - z}{2})}\right).\tag{3.2}
$$

Proof. It is enough to calculate$\mathcal { R } ( x , y , z )$. Using basic trigonometry$\left( \mathrm { e . g . } \right.$ Theorem 2.3.1 of [Bus]) in any geodesic quadrilateral with three right angles and consecutive sides of lengths$a , b ,$infinity and infinity (when one vertex is on the boundary at infinity ), we have

$$
\operatorname{Sinh} (a) \cdot \operatorname{Sinh} (b) = 1.\tag{3.3}
$$

Let$r _ { 3 } \ p _ { 3 }$be the unique geodesic perpendicular to$\beta _ { 3 }$and$\beta _ { 1 }$. Now by applying formula (3.3) to two geodesic quadrilaterals$r _ { 1 } \ r _ { 3 } \ p _ { 1 } \ p _ { 3 }$and$r _ { 3 } \ r _ { 2 }$p<sub>3</sub> p<sub>2</sub> in Figure 3, we have

$$
\mathcal {R} \left(x _ {1}, x _ {2}, x _ {3}\right) = x _ {1} - 2 \operatorname{arcsinh} \left(\frac {1}{\sinh \left(d \left(\beta_ {1} , \beta_ {3}\right)\right)}\right).
$$

On the other hand by cutting the pairs of pants along the shortest geodesics joining distinst boundary components, we obtain two convex right-angled geodesic hexagons with consecutive sides of lengths$x _ { 1 } / 2 , \ d ( \beta _ { 1 } , \beta _ { 2 } ) , \ x _ { 2 } / 2$2 $d ( \beta _ { 2 } , \beta _ { 3 } ) , x _ { 3 } / 2$and$d ( \beta _ { 3 } , \beta _ { 1 } )$. This means that$x _ { 1 } , \ x _ { 2 }$and$x _ { 3 }$uniquely determine$d ( \beta _ { 1 } , \beta _ { 3 } )$. Using basic trigonometry of hyperbolic hexagons ( e.g. Theorem 2.4.1 in [Bus] ), we get

$$
\cosh (d (\beta_ {1}, \beta_ {3})) = \frac {\cosh (\frac {x _ {2}}{2}) + \cosh (\frac {x _ {3}}{2}) \cosh (\frac {x _ {1}}{2})}{\sinh (\frac {x _ {3}}{2}) \sinh (\frac {x _ {1}}{2})}.
$$

See 2 of [Bus] for more details.

On the other hand, since arcsinh$. ( z ) = \log ( z + \sqrt { z ^ { 2 } + 1 } )$we have

$$
2 \operatorname{arcsinh} \left(\frac {1}{\sinh (\alpha)}\right) = 2 \log \left(\frac {1}{\sinh (\alpha)} + \frac {\cosh (\alpha)}{\sinh (\alpha)}\right) = \log \left(\frac {\cosh (\alpha) + 1}{\cosh (\alpha) - 1}\right),
$$

$$
\mathcal {R} (x _ {1}, x _ {2}, x _ {3}) = x _ {1} - \log \left(\frac {\cosh (d (\beta_ {1} , \beta_ {3}) + 1}{\cosh (d (\beta_ {1} , \beta_ {3})) - 1}\right),
$$

which implies equation 3.2.

Remark. Equation (3.1) shows that is a function of x and$y + z$. Next lemma allows us to simplify integrals involving  and$\mathcal { R }$:

Lemma 3.2. The functions$\mathcal { D } , \mathcal { R } : \mathbb { R } _ { + }  \mathbb { R } _ { + }$satisfy the following equations:

$$
\frac {\partial}{\partial x} \mathcal {D} (x, y, z) = H (y + z, x),\tag{3.4}
$$

and

$$
\frac {\partial}{\partial x} \mathcal {R} (x, y, z) = \frac {1}{2} (H (z, x + y) + H (z, x - y)).\tag{3.5}
$$

Proof. Equation (3.4) is a straight forward calculation from equation (3.1), since we have

$$
\frac {\partial}{\partial x} \mathcal {D} (x, y, z) = \frac {e ^ {x / 2}}{e ^ {x / 2} + e ^ {(y + z) / 2}} + \frac {e ^ {- x / 2}}{e ^ {- x / 2} + e ^ {(y + z) / 2}} = H (y + z, x).
$$

On the other hand, using Lemma 3.1, one can show that

$$
\mathcal {D} (x, y, z) + \mathcal {D} (x, - y, z) = 2 \mathcal {R} (x, y, z)
$$

which implies (3.5).

Asymptotic behavior of and . Functions and are continuous on R<sup>3</sup><sub>+</sub>. As$0 < \mathcal { D } ( x , y , z ) \le$x and$0 < \mathcal { R } ( x , y , z ) \leq x .$both$D ( x , y , z )$and $\mathcal { R } ( x , y , z )$go to zero when$x \to 0$. By using Lemma 3.2 it is easy to verify that

$$
\mathcal {D} (x, y, z) \sim x H (y + z, x) \sim \frac {2 x}{1 + e ^ {\frac {y + z}{2}}},\tag{3.6}
$$

$$
\mathcal {R} (x, y, z) \sim x \left(\frac {1}{1 + e ^ {\frac {z + y}{2}}} + \frac {1}{1 + e ^ {\frac {z - y}{2}}}\right), \mathcal {R} (x, x, z) \sim \frac {2 x}{1 + e ^ {\frac {z}{2}}},\tag{3.7}
$$

as$x \longrightarrow 0 .$

Moreover, we have:

Lemma 3.3. There are constants$c _ { 1 } , c _ { 2 } > 0$such that for any$x \leq 1$we have

$$
\begin{array}{c} \left| \frac {\mathcal {D} (x , y , z)}{x} - \frac {1}{1 + e ^ {\frac {y + z}{2}}} \right| \leq c _ {1} x e ^ {\frac {- (y + z)}{2}}, \\ \left| \frac {\mathcal {R} (x , y , z)}{x} - \left(\frac {1}{1 + e ^ {\frac {z + y}{2}}} + \frac {1}{1 + e ^ {\frac {z - y}{2}}}\right) \right| \leq c _ {2} x e ^ {\frac {- z}{2}}. \end{array}
$$

Also, when x and y are fixed numbers as$z  \infty$, we have

$$
\mathcal {R} (x, y, z) \to 0,
$$

similarly, when x is a fixed number as$y , z \to \infty$2

$$
\mathcal {D} (x, y, z) \to 0.
$$

## 4 Generalized McShane identity for bordered surfaces

In this section, we generalize McShane’s identity for bordered hyperbolic Riemann surfaces with geodesic boundary components.

Embedded Pairs of pants. We say three isotopy classes of connected simple closed curves,$( \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } )$on$S _ { g , n }$, bound a pair of pants if there exists an embedded pair of pants$\Sigma \subset S _ { g , n }$such that$\partial \Sigma = \{ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } \}$ Here$\alpha _ { i }$can be a boundary component and we consider punctures as simple closed geodesics of length$0 .$The statement of Theorem 1.3 motivates the following definitions.

For$1 \leq i \leq n ,$let${ \mathcal { F } } _ { i }$be the set of unordered pairs of isotopy classes of simple closed curves$\{ \alpha _ { 1 } , \alpha _ { 2 } \}$bounding a pairs of pants with$\beta _ { i }$such that$\alpha _ { 1 } , \alpha _ { 2 }$∉$\partial ( S _ { g , n } )$;

For$1 \leq i \neq j \leq n .$, let$\mathcal { F } _ { i , j }$be the set of isotopy classes of simple closed curves$\gamma$bounding a pairs of pants containing$\beta _ { i }$and$\beta _ { j }$

An identity for lengths of simple closed geodesics. First we state an identity for lengths of simple closed geodesics on hyperbolic punctured surfaces due to G. McShane [M]:

Theorem 4.1. Let$\{ p _ { i } \} _ { 1 } ^ { n }$be the set of punctures of$X \in \mathcal { T } _ { g , n }$. Then we have

$$
\sum_ {\{\alpha_ {1}, \alpha_ {2} \} \in \mathcal {F} _ {1}} \frac {1}{1 + e ^ {\frac {\ell_ {\alpha_ {1}} (X) + \ell_ {\alpha_ {2}} (X)}{2}}} + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \frac {1}{1 + e ^ {\frac {\ell_ {\gamma} (X)}{2}}} = \frac {1}{2}.
$$

We will use the properties of functions$\mathcal { D } , \mathcal { R } : \mathbb { R } _ { + } ^ { 3 }  \mathbb { R } _ { + }$, defined in the preceding section, and the geometry of complete simple geodesics on a hyperbolic surface to get the following result for hyperbolic bordered Riemann surfaces with geodesic boundary components:

Theorem 4.2 (Generalized McShane identity for bordered surfaces). For any$X \in { \mathcal { T } } _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$with$3 g - 3 + n > 0$, we have

$$
\sum_ {\{\alpha_ {1}, \alpha_ {2} \} \in \mathcal {F} _ {1}} \mathcal {D} (L _ {1}, \ell_ {\alpha_ {1}} (X), \ell_ {\alpha_ {2}} (X)) + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \mathcal {R} (L _ {1}, L _ {i}, \ell_ {\gamma} (X)) = L _ {1}.\tag{4.1}
$$

Note that as$L _ { 1 } \to 0$both sides of (4.1) tend to zero and$\beta _ { 1 }$tends to a puncture$p _ { 1 }$. Using (3.6) and (3.7), the following Corollary is an immediate result of Theorem 4.2 :

Corollary 4.3. For any$X \in \mathcal { T } _ { g , n } ( 0 , L _ { 2 } , \ldots , L _ { n } )$with$3 g - 3 + n > 0$, we have

$$
\sum_ {\{\alpha_ {1}, \alpha_ {2} \} \in \mathcal {F} _ {1}} \frac {1}{1 + e ^ {\frac {\ell_ {\alpha_ {1}} (X) + \ell_ {\alpha_ {2}} (X)}{2}}} + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \frac {1}{2} \left(\frac {1}{1 + e ^ {\frac {\ell_ {\gamma} (X) + L _ {i}}{2}}} + \frac {1}{1 + e ^ {\frac {\ell_ {\gamma} (X) - L _ {i}}{2}}}\right) = \frac {1}{2}.\tag{4.2}
$$

Notice that corollary 4.3 implies Theorem 4.1.

Remark. To prove Theorem 4.2, we basically follow the proof presented in [M] almost line for line by relating the topology of the union of complete simple geodesics perpendicular to all boundary components to the global behavior of simple closed geodesics. See also [B] for a related result for the lengths of common orthogonals of two totally geodesic hypersurfaces on a hyperbolic manifold.

Union of complete simple geodesics. Let$E ( X )$be the union of all simple complete geodesics perpendicular to all boundary components and

$$
E _ {i} = E \cap \beta_ {i}.
$$

Given$x \in E _ { i }$, let$\gamma _ { x }$, the geodesic emanating from$x ,$, denote the complete simple geodesic perpendicular to$\beta _ { i }$such that$x \in \gamma _ { x }$

Theorem 4.4. The set$E _ { i } \subset \beta _ { i }$, defined as above, has measure zero.

Proof. By a result due to Birman and Series [BS], the union of all complete geodesics on a closed surface has Hausdorf dimension 1. Doubling the bordered surface along its boundary components shows that the same statement holds for a bordered surface. That is$\mu ( E ) = 0$. Therefore,$E \cap U _ { \beta _ { i } }$ has measure zero , where$U _ { \beta _ { i } }$is the collar neighborhood around$\beta _ { i }$. Because of the structure of the collar neighborhood we have

$$
\mu (E \cap U _ {\beta_ {i}}) = \sinh r \times \mu (E _ {i}),
$$

where r is the width of the collar neighborhood. So$\mu ( E \cap U _ { \beta _ { i } } ) = 0$implies that$\mu ( E _ { i } ) = 0$✷

Later we show that:

Theorem 4.5. Each$E _ { i }$is homeomorphic to the Cantor set union countably many isolated points.

Characterization of boundary and isolated points in$E _ { i }$. In this part we give a characterization of boundary and isolated points in$E _ { i }$. We say a lamination$\gamma$spirals to a lamination$\Omega ( \gamma )$if$\Omega ( \gamma )$is in the closure of$\gamma .$ It can be easily checked that when$\gamma$is a ray,$\Omega ( \gamma )$is actually a minimal lamination. Note that for$x \in E _ { i }$, the corresponding simple geodesic ray,$\gamma _ { x }$ falls into exactly one of the following two classes.

1. The other end spirals into a compact minimal lamination inside the surface, which will be denoted by$\Omega ( \gamma _ { x } )$

2. The other end also approaches a (not necessarily distinct) boundary component$\beta _ { i }$in which case either the ray$\gamma _ { x }$meets$\beta _ { i }$perpendicularly or spirals around it.

We will prove the following classification of points in$E _ { i }$in terms of the behavior of the corresponding complete simple geodesics (See [M]) :

Theorem 4.6. For any$x \in E _ { i }$, exactly one of the following holds:

$\mathbf { a } )$The point x is an isolated point of$E _ { i }$if the other end$o f \gamma _ { x }$approaches a boundary component.

b)$I f \Omega ( \gamma _ { x } )$is a not a simple closed curve then x is neither a boundary nor an isolated point in$E _ { i }$

c) The point x is a boundary point of$E _ { i } \ i f \ \Omega ( \gamma _ { x } )$is a simple closed curve inside the surface.

![](images/page_19_image_8.jpg)

Figure 4. Finding the pair of pants containing a simple geodesic

Notice that, as shown in Figure 4, for any$\gamma$joining two boundary components, there exists a unique embedded pair of pants containing$\gamma$and these (not necessarily distinct) boundary components.

Also in each pair of pants containing two (not necessarily distinct) boundary components, there exists a unique simple geodesic joining them perpendicularly.

Proof of Theorem$4 . 6 ( \mathbf { a } )$. let$x = x _ { 1 } \in X _ { 1 }$be such that the other end of $\gamma _ { x }$goes up to$\beta _ { 1 }$and let$x _ { 2 } \in \beta _ { 1 }$be such that

$$
\gamma_ {x} \cap \beta_ {1} = \{x, x _ {2} \}.
$$

One can easily modify the argument for other cases. Let Σ denote the pair of pants containing$\gamma _ { x _ { 1 } }$such that$\partial \Sigma = \{ \beta _ { 1 } , \alpha _ { 1 } , \alpha _ { 2 } \}$. There are precisely 4 infinite geodesic rays in Σ meeting$\beta _ { 1 }$perpendicularly at one point (as in Figure 1). Let$\gamma _ { y _ { i } }$and$\gamma _ { z _ { i } }$be the ones spiraling around$\alpha _ { i }$for$i = 1 , 2$such that$x _ { 1 } \in X _ { 1 } \cap ( y _ { 1 } , z _ { 1 } )$and$x _ { 2 } \in X _ { 1 } \cap ( y _ { 2 } , z _ { 2 } )$. We claim that

$$
X _ {1} \cap (y _ {1}, z _ {1}) = x _ {1},
$$

and

$$
X _ {1} \cap (y _ {2}, z _ {2}) = x _ {2}.
$$

if$\gamma _ { z }$is a simple geodesic ray and$z \not \in \{ x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } , w _ { 1 } , w _ { 2 } \} , \gamma _ { z }$must leave

![](images/page_20_chart_7.jpg)

Figure 5. Universal cover of a pair of pants

Σ and hence meet$\alpha _ { 1 } \cup \alpha _ { 2 }$. Without loss of generality, we can assume that$\gamma _ { z }$ meet$\alpha _ { 1 }$first. In the universal cover of this pair of pants, as shown in Figure $5 ,$let${ \dot { \beta } } ,$joining$s _ { 1 }$and$\infty .$, be a lift of$\beta _ { 1 }$. Also, let$\tilde { \alpha } _ { 1 }$, joining$r _ { 1 }$and$r _ { 2 } .$ be the outermost lift of$\alpha _ { 1 }$meeting$\tilde { \gamma } _ { z }$. Consider$\psi _ { 1 }$and$\psi _ { 2 }$, two geodesics perpendicular to$\tilde { \beta }$passing through the two end points of$\tilde { \alpha } _ { 1 }$. And let$\eta _ { 1 }$ (resp.$\eta _ { 2 } )$be the piecewise geodesic path going from$\tilde { z }$to h along$\tilde { \gamma } _ { z }$and from h to$r _ { 1 }$(resp. r<sub>2</sub>) along$\tilde { \alpha } _ { 1 }$As both$\alpha _ { 1 }$and$\gamma _ { z }$are simple, the projection of$\eta _ { 1 }$and$\eta _ { 2 }$are simple rays on the surface. On the other hand, since$\tilde { \alpha } _ { 1 }$is the outermost lift of$\alpha _ { 1 }$meeting$\gamma _ { z }$the projection of$\eta _ { 1 }$and$\eta _ { 2 }$are disjoint from both$\alpha _ { 1 }$and$\alpha _ { 2 }$. Therefore, the projections are infinite simple geodesic rays on Σ.

Furthermore,$\eta _ { 1 }$(resp.$\eta _ { 2 } )$is homotopic to$\psi _ { 2 } \big ( \mathrm { ~ r e s p . ~ } \ \eta _ { 2 } \big )$. This shows that the projections of$\psi _ { 1 }$and$\psi _ { 2 }$are complete simple geodesics on Σ. Since both$\psi _ { 1 }$and$\psi _ { 2 }$are asymptotic to a lift of$\alpha _ { 1 }$, their images spiral to$\alpha _ { 1 }$ Therefore$a _ { 1 }$and$a _ { 2 }$are actually pre images of$z _ { 1 }$and$y _ { 1 }$. Also, for any $x \in [ a _ { 1 } , a _ { 2 } ]$the curve$\gamma _ { x }$meets$\alpha$. Therefore, we have$z \in [ y _ { 1 } , z _ { 1 } ]$✷

Next, assume that$\gamma _ { x }$spirals into a compact minimal lamination$\Omega ( \gamma _ { x } )$ which is not a simple closed curve. To prove part (b) we construct a sequence $\{ x _ { j } \} \subset E _ { i }$getting close to$x$from both side on$\beta _ { i }$. So roughly, we need to approximate$\gamma _ { x }$with simple complete geodesics from both sides.

Quasi-geodesics. Later, we construct paths with uniformly bounded small curvature approximating a complete simple geodesic.

A path$\alpha ( t )$in H, parameterized by arclength, is a quasi geodesic if

$$
d (\alpha (s), \alpha (t)) > \epsilon | s - t |
$$

for all s and t. One can show that any quasi geodesic is a bounded distance from a unique geodesic. See [CEG] for more details.

The main point is that it is easier to construct quasi geodesics approximating a complete geodesic.

Lemma 4.7. A polygon path α of segments of length at least L and bends at most$\theta < \pi$is a quasi-geodesic when L is long enough compared to θ. Also as$( L , \theta ) \to ( \infty , 0 )$the distance from α to its straightening tends to zero.

In the next 3 parts, we show how one can approximate$\gamma _ { x }$with simple complete geodesics using quasi geodesics:

I): Good geodesic segments. Let$\alpha ( t )$be the arc length parameterization of a simple geodesic segment on X,$t _ { 0 } < t _ { 1 } \in \mathbb { R } , \epsilon > 0$and$c : [ 0 , 1 ] \to X$be a diferentiable arc transverse to α such that

$$
c (0) = \alpha (t _ {0}), c (1) = \alpha (t _ {1}).
$$

We say that$( \alpha , t _ { 0 } , t _ { 1 } , c )$is an --good geodesic arc if

$$
\ell (c) \leq \epsilon ,
$$

The arc c is almost perpendicular to$\alpha ,$, that is

$$
| \angle (c ^ {\prime} (0), \alpha^ {\prime} (t _ {0})) - \frac {\pi}{2} | \leq \epsilon ,
$$

![](images/page_22_image_0.jpg)

Figure 6. A good geodesic segment

$$
| \angle (c ^ {\prime} (1), \alpha^ {\prime} (t _ {1})) - \frac {\pi}{2} | \leq \epsilon ,
$$

and

The arc c meets the geodesic arc α in only two points,

$$
c \cap \{\alpha (t) | t _ {0} \leq t \leq t _ {1} \} = \{\alpha (t _ {0}), \alpha (t _ {1}) \}.
$$

Consider the vectors$\alpha ^ { \prime } ( t _ { 0 } )$and$c ^ { \prime } ( 0 ) )$at point$c ( 0 ) = \alpha ( t _ { 0 } )$, and$\alpha ^ { \prime } ( t _ { 1 } )$ and$c ^ { \prime } ( 1 ) )$at the point$c ( 1 ) = \alpha ( t _ { 1 } )$

We say$( \alpha , t _ { 0 } , t _ { 1 } , c )$is positive (negative) if the orientation of the pairs

$$
(\alpha^ {\prime} (t _ {0}), c ^ {\prime} (0)), (\alpha^ {\prime} (t _ {1}), c ^ {\prime} (1))
$$

agree. Note that positivity only depends on the image of α and is independent of the parameterization. So if$( \alpha , t _ { 0 } , t _ { 1 } , c )$is a positive pair the two tangent vectors to α at$\alpha ( t _ { 1 } )$and$\alpha ( t _ { 2 } )$are almost parallel, that is we have

$$
\parallel V _ {c} (\alpha_ {t _ {1}} ^ {\prime}) - \alpha_ {t _ {0}} ^ {\prime} \parallel \leq \epsilon ,
$$

where$V _ { c } ( v )$is the parallel transport of vector v along c.

II): Complete simple geodesics. Let$( \alpha , t _ { 0 } , t _ { 1 } , c )$be an --good geodesic segment such that

$$
\alpha \cap \gamma_ {x} = \emptyset , \gamma_ {x} \cap c [ 0, 1 ] \neq \emptyset ,
$$

and let

$$
t _ {0} = \inf \{t \mid \gamma_ {x} (t) \in c [ 0, 1 ] \}.
$$

Then we construct a complete simple curve, η, which starts at x and goes along$\gamma ( t )$for$\textit { t } \leq \ t _ { 0 }$then spirals around$\psi ( \alpha , t _ { 0 } , t _ { 1 } , c )$, the simple closed curve which goes along c from$\alpha ( t _ { 1 } )$to$\alpha ( t _ { 0 } )$, and then goes back to $\alpha ( t _ { 1 } )$along$\alpha .$In fact, by possibly changing the direction of$\alpha , ~ \eta$will be a quasi-geodesic and consequently lies within a bounded distance of a unique complete simple geodesic. More precisely, we have:

## Lemma 4.8. Assume that

$$
c \cap \{\alpha (t) | 0 \leq t <   t _ {1} \} = \emptyset .
$$

For any$\epsilon > 0$there exist$\delta , L > 0$such that if$( \alpha , t _ { 0 } , t _ { 1 } , c )$is a$\delta _ { - }$good geodesic segment and$L \leq t _ { 1 } - t _ { 0 }$, then η is a simple quasi geodesic. Also, if η˜ denote its geodesic representative and$y = \widetilde { \eta } \cap \beta _ { i }$, then

$$
d (y, x) <   \epsilon .
$$

Furthermore, y lies on the$r i g h t ( l e f t )$side of x if and only$i f \left( \alpha , t _ { 0 } , t _ { 1 } , c \right)$is positive(negative).

We will use this lemma to approximate$\gamma _ { x }$with complete simple geodesics. III): Good geodesic sub-segments in a minimal geodesic lamination. In this part, we want to find good geodesic segments in a non-trivial minimal lamination$\Omega ( \gamma _ { x } ) = \lambda$in order to construct complete simple geodesics.

Given$y \in \lambda$, let$\phi _ { y }$denote the arc length parameterization of the leaf of λ such that$\phi _ { y } ( 0 ) = y$. Then we have:

Lemma 4.9. For any$\epsilon , L > 0$there exist$0 \leq s < t$and a transverse arc c and$y \in c \cap \lambda$, such that$( \phi _ { y } , s , t , c )$is a positive --good geodesic segment, $\phi ( s )$and$\phi ( t )$are not boundary points in$\lambda \cap c ,$and we have

$$
L \leq | s - t |.
$$

Sketch of the proof. Take a transverse almost perpendicular arc c such that$\lambda \cap c \neq \emptyset$. Note that λ is a minimal lamination, and it is not a simple closed curve. Hence,$\lambda \cap c$is uncountable with only countably many boundary points. Therefore one can choose$x _ { 0 } \in \lambda \cap c$so that$\phi _ { x _ { 0 } } \cap$c does not contain any boundary points of$\lambda \cap c$. Let$\phi = \phi _ { x _ { 0 } }$and$c : [ - r , + r ] \to$ X ,$r > 0 , c ( 0 ) = x _ { 0 }$be a small enough transverse arc such that for $\phi ( a ) , \phi ( b ) \in c [ - r , r ]$we have$| a - b | > L$or$a = b$. Without loss of generality, we can assume that the orientation of the pair

$$
(\phi_ {0} ^ {\prime}, c _ {0} ^ {\prime})
$$

![](images/page_24_image_0.jpg)

Figure 7. Finding good-geodesic segments

agrees with the orientation of X. Now define$t _ { 1 } , t _ { 2 }$as follows. Let

$$
t _ {1} = \inf \{t > 0 | \phi (t) \in c [ - r, 0) \},
$$

and$\phi ( t _ { 1 } ) = c ( x _ { 1 } )$. Similarly, as$\phi ( t _ { i } )$is not a boundary point for$i = 1$, 2 we can define

$$
t _ {2} = \inf \{t > t _ {1} | \phi (t) \in c (x _ {1}, 0) \}.
$$

Then as in Figure 7 at least one of$( \phi , 0 , t _ { 1 } , c ) , ( \phi , t _ { 1 } , t _ { 2 } , c )$and$( \phi , 0 , t _ { 2 } , c )$is a positive --good geodesic segment. Also, we have

$$
\min \{| t _ {1} - t _ {2} |, t _ {1}, t _ {2} \} \geq L.
$$

Now we can prove part b that if$\Omega ( \gamma _ { x } )$is a non simple closed curve then x is not a boundary point.

Proof of part (b) and (c) of Theorem 4.6. The main idea is to apply Lemma 4.9 to find positive --good geodesic segments inside λ and use it to construct complete simple geodesics.

Let$( \alpha , t _ { 1 } , t _ { 2 } , c )$be an --good geodesic segment in λ constructed in Lemma 4.9 such that$\alpha ( t _ { i } ) = c ( r _ { i } )$, and$\alpha ( t _ { 1 } )$is not a boundary point of$\lambda \cap c$

As$\gamma _ { x }$spirals to$\lambda , \gamma _ { x } \cap c [ r _ { 1 } , r _ { 2 } ]$is non-empty. Let

$$
t _ {0} = \inf \{t | \gamma_ {x} (t) \in c [ r _ {1}, r _ {2} ] \}.
$$

Then from Lemma 4.8 the result is immediate.

Using the same method, one can find a sequence of complete simple geodesics approximating$\gamma _ { x }$from one side if$\Omega ( \gamma _ { x } )$is a simple closed curve inside the surface in which case, by the proof of part$\mathrm { ( a ) }$, x will be a boundary point of$E _ { i }$.✷

Now, we can show that the set of non-isolated points of$E _ { i }$is topologically homeomorphic to the Cantor set.

Proof of Theorem 4.5. Recall that we have a topological characterization of the Cantor set. That is any perfect totally disconnected compact metric space is homeomorphic to the Cantor set.

By Theorem$4 . 6 ,$apart from countably many points, corresponding to the simple geodesics joining boundary components, points in$E _ { i }$are limit points. The result follows since non-isolated points of$E _ { i }$form a compact totally disconnected perfect subset of$\beta _ { i }$✷

Connection with embedded pairs of pants. Let$x \ \in \ E _ { i }$such that the ray$\gamma _ { x }$spirals into a simple closed geodesic$\alpha _ { 1 }$. Then there is a unique embedded pair of pants$\Sigma _ { x }$on$X$such that$\gamma _ { x } \subset \Sigma _ { x }$. In other words, there exists a unique simple closed geodesic$\alpha _ { 2 }$bounding a pair of pants$\Sigma _ { x }$with $\beta _ { 1 }$and$\alpha _ { 1 }$such that$\gamma _ { x } \subset \Sigma _ { x }$

Let$I _ { i }$be the set of isolated points in$E _ { i }$. Then we can write

$$
I _ {i} \cup (\beta_ {i} - E _ {i}) = \bigcup_ {h} (a _ {h}, b _ {h}),
$$

where$a _ { h } , b _ { h }$are both boundary points of$E _ { i }$. We find a natural one to one correspondence between embedded pairs of pants containing$\beta _ { 1 }$and complementary intervals of$E _ { i } - I _ { i }$as follows.

For any$h ,$let$\Sigma _ { h }$be the unique pairs of pants containing$\gamma _ { a _ { h } }$such that

$$
\partial (\Sigma) = \{\beta_ {1}, \Omega (\gamma_ {a _ {h}}), \alpha \}.
$$

$$
X
$$

$$
\Sigma_ {h}
$$

$$
y \in (a _ {h}, b _ {h})
$$

$$
\gamma_ {b _ {h}} \subset
$$

$$
\gamma_ {y} \subset \Sigma_ {h}
$$

$$
\alpha = \Omega (\gamma_ {b _ {h}})
$$

$$
\Omega (\gamma_ {a _ {h}}), \Omega (\gamma_ {b _ {h}})
$$

$$
\beta_ {1}
$$

Similarly if$\alpha = \beta _ { j }$is a boundary component, then$\gamma _ { b _ { h } } \subset \Sigma _ { h }$which means that$\beta _ { 1 } , \beta _ { j }$and$\Omega ( \gamma _ { a _ { h } } ) = \Omega ( \gamma _ { b _ { h } } )$bound an embedded pair of pants inside the surface.

We will use this fact and Lemma 4.4 to prove the main result of this section.

Proof of Theorem 4.2. Let

$$
I _ {i} \cup (\beta_ {i} - E _ {i}) = \bigcup_ {h} (a _ {h}, b _ {h}),
$$

where$a _ { h } , b _ { h } \in \beta _ { i }$. Then by Theorem 4.4 we have:

$$
L _ {i} = \ell_ {\beta_ {i}} (X) = \sum_ {h} | b _ {h} - a _ {h} |,\tag{4.3}
$$

where$\left| a _ { h } - b _ { h } \right|$is the geodesic distance between$a _ { h }$and$b _ { h }$along$\beta _ { i }$.

For each$1 \leq h$one of the following holds:

1. There exists$j$such that$\gamma = \Omega ( \gamma _ { a _ { h } } ) = \Omega ( \gamma _ { b _ { h } } ) , \beta _ { j }$and$\beta _ { i }$bound a pair of pants in$X$

2. The two curves$\alpha = \Omega ( \gamma _ { a _ { h } } )$and$\beta = \Omega ( \gamma _ { b _ { h } } )$are distinct and bound a pair of pants containing$\beta _ { i }$.

By the definition the functions and in$\ S 3$in the first case we have

$$
\mathcal {R} (L _ {i}, L _ {j}, \ell_ {\gamma} (X)) = | a _ {h} - b _ {h} |,\tag{4.4}
$$

and in the second case, we have:

$$
\frac {1}{2} \mathcal {D} (L _ {i}, \ell_ {\alpha} (X), \ell_ {\beta} (X)) = | a _ {h} - b _ {h} |.\tag{4.5}
$$

Now we can use (4.4) and (4.5) to rewrite (4.3) as

$$
L_{i}(X) = \sum_{\{\alpha_{1},\alpha_{2}\}}\mathcal{D}(L_{i},\ell_{\alpha_{1}}(X),\ell_{\alpha_{2}}(X)) + \sum_{\substack{j\\ j\neq i}}\sum_{\gamma}\mathcal{R}(L_{i},L_{j},\ell_{\gamma}(X)),
$$

where the first sum is over unordered$\{ \alpha _ { 1 } , \alpha _ { 2 } \}$bounding a pairs of pants with$\beta _ { i }$in$X$and the second some is over$\gamma$bounding a pair of pants with $\beta _ { i }$and$\beta _ { j }$.

## 5 Statement of the recursive formula for volumes

In this section we state a recursive formula for$V _ { g , n } ( L )$, the Weil-Petersson volume of${ \mathcal { M } } _ { g , n } ( L )$. The proof is given later in$\ S 9$

The volume function$V _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$is a symmetric function in$L _ { 1 } , \ldots , L _ { n }$ Hence for any set A of positive numbers with$| A | = n$, we can define$V _ { g , n } ( A )$ by

$$
V _ {g, n} (A) = V _ {g, n} \left(a _ {1}, \dots , a _ {n}\right),
$$

where$\{ a _ { 1 } , \ldots , a _ { n } \} = A$

Statement of the recursive formula. The function$V _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$for any g and n$( 2 g - 2 + n > 0 )$is determined recursively as follows :

For any$L _ { 1 } , L _ { 2 } , L _ { 3 } \geq 0$, set

$$
V _ {0, 3} (L _ {1}, L _ {2}, L _ {3}) = 1,
$$

and

$$
V _ {1, 1} (L _ {1}) = \frac {L _ {1} ^ {2}}{2 4} + \frac {\pi^ {2}}{6}.
$$

The first equation holds since the moduli space$\mathscr { M } _ { 0 , 3 } ( L _ { 1 } , L _ { 2 } , L _ { 3 } )$consists of only one point. For the calculation of$V _ { 1 , 1 } ( L )$see$\ S 6$

Let${ \widehat { L } } = ( L _ { 2 } , \ldots , L _ { n } )$. When$( g , n ) \neq ( 1 , 1 ) , ( 0 , 3 )$, the volume$V _ { g , n } ( L ) =$ Vol$( \mathcal { M } _ { g , n } ( L ) )$is inductively determined by :

$$
\frac {\partial}{\partial L _ {1}} L _ {1} V _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L _ {1}, \widehat {L}) + \mathcal {A} _ {g, n} ^ {d c o n} (L _ {1}, \widehat {L}) + \mathcal {B} _ {g, n} (L _ {1}, \widehat {L}),\tag{5.1}
$$

where the functions

$$
\mathcal {A} _ {g, n} ^ {c o n} (L _ {1}, \widehat {L}) = \frac {1}{2} (\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x y \widehat {\mathcal {A}} _ {g, n} ^ {c o n} (x, y, L _ {1}, \widehat {L}) d x d y),\tag{5.2}
$$

$$
\mathcal {A} _ {g, n} ^ {d c o n} (L _ {1}, \widehat {L}) = \frac {1}{2} (\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x y \widehat {\mathcal {A}} _ {g, n} ^ {d c o n} (x, y, L _ {1}, \widehat {L}) d x d y),\tag{5.3}
$$

and

$$
\mathcal {B} _ {g, n} (L _ {1}, \widehat {L}) = \int_ {0} ^ {\infty} x \cdot \widehat {\mathcal {B} _ {g , n}} (x, L _ {1}, \widehat {L}) d x,\tag{5.4}
$$

are defined in terms of the$V _ { h , m } ( L ) \mathrm { { \bar { s } } }$with$3 h + m < 3 g + n$as follows. We define the functions

$$
\widehat {\mathcal {A}} _ {g, n} ^ {c o n}: \mathbb {R} _ {+} ^ {n + 2} \to \mathbb {R} _ {+},
$$

and

$$
\widehat {\mathcal {A}} _ {g, n} ^ {d c o n}: \mathbb {R} _ {+} ^ {n + 2} \to \mathbb {R} _ {+},
$$

$$
\widehat {\mathcal {B}} _ {g, n}: \mathbb {R} _ {+} ^ {n + 1} \to \mathbb {R} _ {+}.
$$

To do this, we need the function$H : \mathbb { R } \to \mathbb { R } _ { + }$defined in$\ S 3$by

$$
H (x, y) = \frac {1}{1 + e ^ {\frac {x + y}{2}}} + \frac {1}{1 + e ^ {\frac {x - y}{2}}}.
$$

Also as before, let

$$
m (g, n) = \delta (g - 1) \times \delta (n - 1).
$$

So$m ( g , n ) = 0$unless$g = 1$and$n = 1$

I) : Definition of$\widehat { A } _ { g , n } ^ { c o n }$. Define$\widehat { A } _ { g , n } ^ { c o n } : \mathbb { R } _ { + } ^ { n + 2 } \longrightarrow \mathbb { R } _ { + }$by

$$
\widehat {\mathcal {A}} _ {g, n} ^ {c o n} (x, y, L _ {1}, \ldots , L _ {n}) = \frac {1}{2 ^ {m (g - 1 , n + 1)}} V _ {g - 1, n + 1} (x, y, \widehat {L}) \cdot H (x + y, L _ {1}).
$$

See Figure$8 ( b )$

II) : Definition of$\widehat { \mathcal { A } _ { g , n } } ^ { d c o n }$. Let$\mathcal { T } _ { g , n }$be the set of ordered paris

$$
a = ((g _ {1}, I _ {1}), (g _ {2}, I _ {2}))
$$

where$I _ { 1 } , I _ { 2 } \subset \{ 2 , \ldots , n \}$and$0 \leq g _ { 1 } , g _ { 2 } \leq g$such that the followings hold:

1. The two sets$I _ { 1 }$and$I _ { 2 }$are disjoint and$\{ 2 , 3 , \dots , n \} = I _ { 1 } \sqcup I _ { 2 }$

2. The numbers$g _ { 1 } , g _ { 2 } \ge 0$and$n _ { 1 } = | I _ { 1 } | , n _ { 2 } = | I _ { 2 } |$satisfy

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

For notational convenience, given$L = \left( L _ { 1 } , \ldots , L _ { n } \right)$and$I \subset \{ 1 , \ldots , n \}$with $| I | = k ,$, define$L _ { I }$by

$$
L _ {I} = (L _ {j _ {1}}, \dots , L _ {j _ {k}}),
$$

where$I = \{ j _ { 1 } , \ldots , j _ { k } \}$. Now for each

$$
a = ((g _ {1}, I _ {1}), (g _ {2}, I _ {2})) \in \mathcal {I} _ {g, n},
$$

let

$$
V (a, x, y, \widehat {L}) = \frac {V _ {g _ {1} , n _ {1} + 1} (x , L _ {I _ {1}})}{2 ^ {m (g _ {1} , n _ {1} + 1)}} \times \frac {V _ {g _ {2} , n _ {2} + 1} (y , L _ {I _ {2}})}{2 ^ {m (g _ {2} , n _ {2} + 1)}}.
$$

As we will see later, the reason we have to divide by 2 in this case is that every$X \in \mathcal { M } _ { 1 , 1 } ( L )$has a symmetry of order 2.

Note that as the function$V _ { g , n } ( L )$is symmetric, the function$V ( a , x , y , \widehat { L } )$ is well defined. Now define$\widehat { A } _ { g , n } ^ { d c o n } : \mathbb { R } _ { + } ^ { n + 2 } \longrightarrow \mathbb { R } _ { + }$by

$$
\widehat {\mathcal {A}} _ {g, n} ^ {d c o n} (x, y, L _ {1}, \widehat {L}) = \sum_ {a \in \mathcal {I} _ {g, n}} V (a, x, y, \widehat {L}) \cdot H (x + y, L _ {1}).
$$

See Figure$8 ( a )$

III) : Definition of$\widehat { B } _ { g , n }$. Finally, define$\widehat { B } _ { g , n } : \mathbb { R } _ { + } ^ { n + 1 } \to \mathbb { R } _ { + }$by

$$
\widehat {\mathcal {B}} _ {g, n} (x, L _ {1}, \widehat {L}) = \frac {1}{2 ^ {m (g , n - 1)}}
$$

$$
\sum_ {j = 2} ^ {n} \frac {1}{2} (H (x, L _ {1} + L _ {j}) + H (x, L _ {1} - L _ {j})) \cdot V _ {g, n - 1} (x, L _ {2}, \dots , \hat {L} _ {j}, \dots , L _ {n}).\tag{5.5}
$$

See Figure$8 ( c )$

Connection with topology of the set of pairs of pants. Although the recursive formula 5.1 has been described in purely combinatorial terms, as in Figure 8, it is closely related to the topology of diferent types of pairs of pants in$S _ { g , n }$. In fact, this formula gives us the volume of${ \mathcal { M } } _ { g , n } ( L )$in terms of volumes of moduli spaces of Riemann surfaces that we get by removing a pair of pants containing at least one boundary component of$S _ { g , n }$. Also, the second condition in the definition of$\mathcal { T } _ { g , n }$is equivalent to the condition that both complementary regions of the pair of pants have negative Euler characteristics. See 9 for more details.

Remark. The functions$\mathcal { A } _ { g , n } ^ { c o n } , \mathcal { A } _ { g , n } ^ { d c o n }$and$B _ { g , n }$are determined by the functions$\{ V _ { i , j } \}$where$3 i + j < 3 g + n$. Therefore equation (5.1) is a recursive formula for calculating$V _ { g , n } ( L )$. In 6 we will simplify this recursive formula and use it to prove that$V _ { g , n } ( L )$is a polynomial in L (Theorem 1.1).

## 6 Polynomial behavior of the Weil-Petersson volume

In this section we use the recursive formula for the volumes of moduli spaces stated in$\ S 5$to establish the following result:

Theorem 6.1. The function$V _ { g , n } ( L )$is a polynomial in$L _ { 1 } , \ldots , L _ { n }$, namely:

$$
V_{g,n}(L) = \sum_{\substack{\alpha \\ |\alpha |\leq 3g - 3 + n}}C_{\alpha}\cdot L^{2\alpha},
$$

where$C _ { \alpha } > 0$lies in$\pi ^ { 6 g - 6 + 2 n - | 2 \alpha | } \cdot \mathbb { Q }$Q.

We will also calculate the leading coeficients of$V _ { 0 , n } ( L )$

Calculation of$V _ { 1 , 1 } ( L )$. Before proving Theorem 6.1, we elaborate the main idea of the calculation of the$V _ { g , n } ( L )$’s through an example when$g = n = 1$ In this case, using Theorem 4.2 for a hyperbolic surface of genus one with one geodesic boundary component implies that for any$X \in \mathcal { T } ( S _ { 1 , 1 } , L )$, we have

$$
\sum_ {\gamma} \mathcal {D} (L, \ell_ {\gamma} (X), \ell_ {\gamma} (X)) = L,
$$

where the sum is over all simple closed curves$\gamma$on$S _ { 1 , 1 }$. Also, by Lemma 3.2, we have

$$
\frac {\partial}{\partial L} \mathcal {D} (L, x, x) = \frac {1}{1 + e ^ {x - \frac {L}{2}}} + \frac {1}{1 + e ^ {x + \frac {L}{2}}}.
$$

Integrating over$\mathcal { M } _ { 1 , 1 } ( L )$, as in the calculation of$\mathrm { V o l } ( \mathcal { M } _ { 1 , 1 } )$in the Introduction, we get:

$$
L \cdot V _ {1, 1} (L) = \int_ {0} ^ {\infty} x \mathcal {D} (L, x, x) d x.
$$

So we have

$$
\frac {\partial}{\partial L} L \cdot V _ {1, 1} (L) = \int_ {0} ^ {\infty} x \cdot (\frac {1}{1 + e ^ {x + \frac {L}{2}}} + \frac {1}{1 + e ^ {x - \frac {L}{2}}}) d x.
$$

By setting$y _ { 1 } = x + L / 2$and$y _ { 2 } = x - L / 2$, we get

$$
\begin{array}{c} \int_ {0} ^ {\infty} x \cdot (\frac {1}{1 + e ^ {x + \frac {L}{2}}} + \frac {1}{1 + e ^ {x - \frac {L}{2}}}) d x = \int_ {L / 2} ^ {\infty} \frac {y _ {1} - L / 2}{1 + e ^ {y _ {1}}} d y _ {1} + \int_ {- L / 2} ^ {\infty} \frac {y _ {2} + L / 2}{1 + e ^ {y _ {2}}} d y _ {2} = \\ = 2 \int_ {0} ^ {\infty} \frac {y}{1 + e ^ {y}} d y + \int_ {0} ^ {L / 2} \frac {y - L / 2}{1 + e ^ {y}} d y + \int_ {0} ^ {- L / 2} \frac {y + L / 2}{1 + e ^ {y}} d y = \\ \frac {\pi^ {2}}{6} + \int_ {0} ^ {L / 2} (y - L / 2) (\frac {1}{1 + e ^ {y}} + \frac {1}{1 + e ^ {- y}}) d y = \frac {\pi^ {2}}{6} + \frac {L ^ {2}}{8}, \end{array}
$$

Since we have

$$
\frac {1}{1 + e ^ {y}} + \frac {1}{1 + e ^ {- y}} = 1.
$$

Therefore, we have:

$$
V _ {1, 1} (L) = \frac {L ^ {2}}{2 4} + \frac {\pi^ {2}}{6}.\tag{6.1}
$$

Remark. This result agrees with the result obtained in [NN]. It seems straightforward to generalize our calculation for hyperbolic surfaces with finitely many cone singularities [NN].

Polynomial behavior of H and$V _ { g , n }$. At first glance the equation in 5.1 looks too complicated to be useful, but by using the following elementary lemmas we will be able to simplify both sides of the equation 5.1

$$
\frac {\partial}{\partial L _ {1}} L _ {1} V _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L) + \mathcal {A} _ {g, n} ^ {d c o n} (L) + \mathcal {B} _ {g, n} (L),
$$

and prove that$V _ { g , n } ( L )$is actually a polynomial in L.

The following easy observation shows that it sufices to prove that${ \mathcal { A } } _ { g , n } ^ { c o n } ( L )$, ${ \mathcal { A } } _ { g , n } ^ { d c o n } ( L )$and$B _ { g , n } ( L )$are polynomials in$L .$

Lemma 6.2. For any diferentiable function$F : \mathbb { R } ^ { n } \longrightarrow \mathbb { R }$, define$P ( F )$by:

$$
P _ {i} (F) = \frac {\partial}{\partial x _ {i}} (x _ {i} F (x _ {1},..., x _ {n})).
$$

Then$P _ { i } ( F )$determines$F _ { i }$, and we have$F \in \mathbb { R } [ x _ { 1 } , . . , x _ { n } ]$if and only if $P _ { i } ( F ) \in \mathbb { R } [ x _ { 1 } , . . , x _ { n } ]$

Definition. For$i \in \mathbb N$, define$F _ { 2 i + 1 } : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$by

$$
F _ {2 k + 1} (t) = \int_ {0} ^ {\infty} x ^ {2 k + 1} \cdot H (x, t) d x.
$$

We easily find in the following that

$$
\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (x + y, t) d x d y = \frac {(2 i + 1) ! \cdot (2 j + 1) !}{(2 i + 2 j + 3) !} F _ {2 i + 2 j + 3} (t).\tag{6.2}
$$

To prove equation 6.2, note that for any$m , n \in \mathbb { N }$, we have

$$
\int_ {0} ^ {T} y ^ {m} (T - y) ^ {n} d y = \frac {m ! n !}{(m + n + 1) !} T ^ {m + n + 1}.
$$

Now we can simplify the left hand side of the equation 6.2, as follows. By setting$Z = x + y$, we get

$$
\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (x + y, t) d x d y = \int_ {0} ^ {\infty} \int_ {0} ^ {Z} (Z - y) ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (Z, t) d y d Z =
$$

$$
= \frac {(2 i + 1) ! \cdot (2 j + 1) !}{(2 i + 2 j + 3) !} \int_ {0} ^ {\infty} Z ^ {2 i + 2 j + 3} H (Z, t) d Z.
$$

These functions play a key role in the calculation of$V _ { g , n } ( L )$. In fact, using equations (5.2), (5.3) and (5.4) we can express the functions${ \mathcal { A } } _ { g , n } ^ { d c o n } ( L )$, ${ \mathcal { A } } _ { g , n } ^ { c o n } ( L )$and$B _ { g , n } ( L )$in terms of the$F _ { 2 k + 1 } ( t )$’s and the volumes of moduli spaces of simpler Riemann surfaces.

The following lemma helps us to proceed to the calculation of$V _ { g , n } ( L )$

Lemma 6.3. For any$k \geq 0$, we have

$$
\frac {F _ {2 k + 1} (t)}{(2 k + 1) !} = \sum_ {i = 0} ^ {k + 1} \zeta (2 i) (2 ^ {2 i + 1} - 4) \frac {t ^ {2 k + 2 - 2 i}}{(2 k + 2 - 2 i) !}.
$$

Therefore$F _ { 2 k + 1 } ( t )$is a polynomial in$t ^ { 2 }$of degree$k + 1$such that the coefficient of$m ^ { 2 k + 2 - 2 i }$lies in$\pi ^ { 2 i } \cdot \mathbb { Q } _ { > 0 }$

Remark. Since$\zeta ( 0 ) = - 1 / 2$, therefore the leading coeficient of$F _ { 2 k + 1 } ( t )$ is$t ^ { 2 k + 2 } / ( 2 k + 2 )$

Proof. Simplifying$F _ { 2 k + 1 } ( t )$, exactly as in the calculation of$V _ { 1 , 1 } ( L )$in the beginning of this section, we have

$$
\begin{array}{c} \int_ {0} ^ {\infty} x ^ {2 k + 1} \cdot \left(\frac {1}{1 + e ^ {x + t}} + \frac {1}{1 + e ^ {x - t}}\right) d x = \\ = \int_ {0} ^ {\infty} (\frac {(x + t) ^ {2 k + 1} + (x - t) ^ {2 k + 1}}{1 + e ^ {x}}) d x + \int_ {0} ^ {t} - \frac {(x - t) ^ {2 k + 1}}{1 + e ^ {x}} + \frac {(- x + t) ^ {2 k + 1}}{1 + e ^ {- x}} d x \\ = \frac {t ^ {2 k + 2}}{2 k + 2} + \sum_ {i = 0} ^ {k} 2 t ^ {2 k - 2 i} \cdot \binom {2 k + 1} {2 i + 1} \cdot \int_ {0} ^ {\infty} \frac {x ^ {2 i + 1}}{1 + e ^ {x}} d x, \end{array}
$$

which is a polynomial in$t ^ { 2 }$whose leading term is$\frac { m ^ { 2 k + 2 } } { 2 k + 2 }$. So the equality

$$
2 \int_ {0} ^ {\infty} \frac {x ^ {2 i + 1}}{1 + e ^ {x}} d x = \zeta (2 i + 2) (2 i + 1)! (2 - 2 ^ {- 2 i})
$$

implies that

$$
\frac {F _ {2 k + 1} (2 t)}{(2 k + 1) !} = 2 ^ {2 k + 2} (\frac {t ^ {2 k + 2}}{(2 k + 2) !} + \sum_ {i = 0} ^ {k} \frac {t ^ {2 k - 2 i}}{(2 k - 2 i) !} \cdot \zeta (2 i + 2) (2 - 2 ^ {- 2 i}))
$$

which implies the result.

Now we can use the preceding lemma to prove that$V _ { g , n } ( L )$is a polynomial in$L$.

Proof of Theorem 6.1. The proof is by induction on$3 g + n$. Using equation 5.1, and Lemma 6.2, it sufices to prove that$\mathcal { A } _ { g , n } ^ { c o n } ( L ) , \mathcal { A } _ { g , n } ^ { d c o n } ( L )$ and$B _ { g , n } ( L )$are polynomials in L. We prove that$\mathscr { A } _ { g , n } ^ { c o n } ( L )$is a polynomial in$L .$, the proof for$\mathcal { A } _ { g , n } ^ { d c o n }$and$B _ { g , n }$is similar. Let$T _ { n } = \{ 1 , 2 , \dots , n \}$and$L = ( L _ { 1 } , \ldots , L _ { n } )$. By the induction hypothesis $V _ { g , n - 1 } ( x , L _ { T _ { n } - \{ 1 , j \} } )$is a polynomial in$x ^ { 2 }$and$\{ L _ { k } \} _ { k \in T _ { n } } - \{ 1 , j \}$. Therefore, to complete the proof we have to show that

$$
\int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot \left(H (x, L _ {1} + L _ {j}) + H (x, L _ {1} - L _ {j})\right) d x
$$

is a polynomial in$L _ { 1 }$and$L _ { j }$which is immediate from Lemma 6.3.✷

## 7 Leading coeficients of volume polynomials

In this section, we find a recursive method for calculating the coeficients of $V _ { g , n } ( L )$and calculate the leading coeficients of$V _ { 0 , n } ( L )$

Definition. Let

$$
C _ {g} (\alpha_ {1}, \dots , \alpha_ {n})
$$

be the coeficient of$L _ { 1 } ^ { 2 \alpha _ { 1 } } \cdot \cdot \cdot L _ { n } ^ { 2 \alpha _ { n } }$in the polynomial$V _ { g , n } ( L )$. Also, let

$$
(\alpha_ {1}, \dots , \alpha_ {n}) _ {g} = C _ {g} (\alpha) \times \prod_ {i = 1} ^ {n} \alpha_ {i}! \times 2 ^ {| \alpha |},
$$

where$| \alpha | = \sum _ { i = 1 } ^ { n } \alpha _ { i }$

The recursive formula 5 simplifies when$\sum _ { i = 1 } ^ { n } 2 \alpha _ { i } = 6 g - 6 +$2n in which case we get a recursive formula in terms of the leading coeficients of$\{ V _ { h , m } \}$ with$3 h - m < 3 g - n$. Also, if one of the$\alpha _ { i } \mathrm { ^ { * } s }$is 0 or 1, the coeficient of $L ^ { 2 \alpha }$in$\widehat { A } ^ { c o n } ( L )$and$\widehat { A } _ { g , n } ^ { d c o n } ( L )$equals zero and we have:

Theorem 7.1.$I f \sum _ { i = 1 } ^ { n } \alpha _ { i } = 3 g - 3 + n$, then we have

$$
(1, \alpha_ {1}, \dots , \alpha_ {n}) _ {g} = (2 g + n - 2) (\alpha_ {1}, \dots , \alpha_ {n}) _ {g}.
$$

Theorem 7.2.$I f \sum _ { i = 1 } ^ { n } \alpha _ { i } = 3 g - 2 + n$, then we have

$$
(0, \alpha_ {1}, \dots , \alpha_ {n}) _ {g} = \sum_ {\alpha_ {i} \neq 0} (\alpha_ {1}, \dots , \alpha_ {i} - 1, \dots , \alpha_ {n}) _ {g}.
$$

Proof of Theorem 7.1. We prove the Theorem by induction on n. To do this, we calculate the coeficient of$L _ { 1 } ^ { 2 } \cdots L _ { n + 1 } ^ { 2 \alpha _ { n } }$in$V _ { g , n + 1 } ( L )$by using the recursive formula for the volume polynomials. The coeficient of$L _ { 1 } ^ { 2 } \cdots L _ { n + 1 } ^ { 2 \alpha _ { n } }$ on the left hand side of equation 5.1 equals

$$
\frac {3 (1 , \alpha_ {1} , \ldots , \alpha_ {n}) _ {g}}{\alpha ! \times 2 ^ {3 g - 3 + n + 1}},
$$

where α!$= \alpha _ { 1 } ! \cdots \alpha _ { n } !$

As in the proof of Lemma 6.3, the leading coeficient of$F _ { 2 i + 1 } ( m )$equals $1 / 2 i + 2$. It can be easily verified that the coeficient of$L _ { 1 } ^ { 2 } \cdot \cdot \cdot L _ { n + 1 } ^ { 2 \alpha _ { n } }$in

$$
\sum_ {j = 2} ^ {n + 1} \int_ {0} ^ {\infty} \frac {1}{2} x \cdot (H (x, L _ {1} + L _ {j}) + H (x, L _ {1} - L _ {j})) \cdot V _ {g, n - 1} (x, L _ {T - \{1, j \}}) d x
$$

equals

$$
\sum_ {j = 1} ^ {n} \frac {\binom {2   \alpha_ {j} + 2} {2}}{2   \alpha_ {i} + 2} \cdot \frac {(\alpha_ {1} , \ldots , \alpha_ {n}) _ {g}}{\alpha ! \times 2 ^ {3 g - 3 + n}} = \frac {3   (2 g - 2 + n)}{2} \times \frac {(\alpha_ {1} , \ldots , \alpha_ {n}) _ {g}}{\alpha ! \times 2 ^ {3 g - 3 + n}}.
$$

On the other hand, there is no$L _ { 1 } ^ { 2 \alpha _ { 1 } } \cdot \cdot \cdot L _ { n + 1 } ^ { 2 \alpha _ { n } }$term in${ \mathcal { A } } _ { g , n } ^ { d c o n } ( L )$and$B _ { g , n } ( L )$ Therefore, we have

$$
3 \left(1, \alpha_ {1}, \ldots , \alpha_ {n}\right) _ {g} = 3 \left(2 g + n - 2\right) (\alpha_ {1}, \ldots , \alpha_ {n}) _ {g}
$$

which implies the result.

We omit the proof of Theorem 7.2 since it is quite similar.

These two recursive formulas are actually enough for determining $( \alpha _ { 1 } , \ldots , \alpha _ { n } ) _ { g }$when$g = 0$. In this case, by induction on n it can be easily proved that:

Corollary 7.3. When$\sum _ { i = 1 } ^ { n } \alpha _ { i } = n - 3$, we have

$$
(\alpha_ {1}, \ldots , \alpha_ {n}) _ {0} = \binom{\alpha_ {1} + \dots + \alpha_ {n}}{\alpha_ {1}, \dots , \alpha_ {n}}.
$$

Remark. Equations in Theorem 7.1 and Theorem 7.2 are reminiscent of the dilaton and string equations for the intersection pairings over the moduli spaces [Har]. In a sequel we prove that

$$
(\alpha_ {1}, \ldots , \alpha_ {n}) _ {g} = \int_ {\overline {{\mathcal {M}}} _ {g, n}} \psi_ {1} ^ {\alpha_ {1}} \dots \psi_ {n} ^ {\alpha_ {n}},
$$

where$\psi _ { i }$denotes the Chern class of the ith tautological line bundle over $\overline { { \mathcal { M } } } _ { g , n } \ [ \mathrm { M i r z 2 } ]$

## 8 Integration over the moduli space

In this section, we investigate the Weil-Petersson symplectic structure of ${ \mathcal { M } } _ { g , n } ( L )$

For

$$
\gamma = \sum_ {i = 1} ^ {k} c _ {i} \gamma_ {i},
$$

where$c _ { i } > 0$and$\gamma _ { 1 } , \dots , \gamma _ { k }$are disjoint non homotopic simple closed curves on$S _ { g , n }$, let$\Gamma = \left( \gamma _ { 1 } , \dots , \gamma _ { k } \right)$.

For any$f : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$

$$
f _ {\gamma} (X) = \sum_ {[ \alpha ] \in \operatorname{Mod} \cdot [ \gamma ]} f (\ell_ {\alpha} (X)),
$$

where$\ell _ { \boldsymbol { \alpha } } ( \boldsymbol { X } ) = \sum _ { i = 1 } ^ { k } c _ { i } \ell _ { \gamma _ { i } } ( \boldsymbol { X } )$, defines a function$f _ { \gamma } : \mathcal { M } _ { g , n } ( L ) \longrightarrow \mathbb { R }$

In this section we establish the following result for integrating the function$f _ { \gamma }$over${ \mathcal { M } } _ { g , n } ( L )$

Theorem 8.1. For any$\gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i }$, the integral of$f _ { \gamma }$over${ \mathcal { M } } _ { g , n } ( L )$with respect to the Weil-Petersson volume form is given by

$$
\int_ {\mathcal {M} _ {g, n} (L)} f _ {\gamma} (X)   d X = \frac {2 ^ {- M (\gamma)}}{| \operatorname{Sym} (\gamma) |} \iint_ {\mathbf {x} \in \mathbb {R} _ {+} ^ {k}} f (| \mathbf {x} |) V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) \mathbf {x} \cdot d \mathbf {x}   d t,
$$

where$| \mathbf { x } | = \sum _ { i = 1 } ^ { k } c _ { i } \ x _ { i } ,$and

$M ( \gamma ) = | \{ i | \gamma _ { i }$seperates of a one-handle from$S _ { g , n } \} |$

Here x$d \mathbf { x } = x _ { 1 } \cdot \cdot \cdot x _ { n } \cdot d x _ { 1 } \wedge \cdot \cdot \cdot \wedge d x _ { n }$, and for any$\mathbf { x } = ( x _ { 1 } , \ldots , x _ { k } ) \in \mathbb { R } _ { + } ^ { k }$，$V _ { g , n } ( \Gamma , \mathbf { x } , \beta , L )$is given by

$$
\mathrm{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)).
$$

We can write$S _ { g , n } ( \gamma )$as a union of its connected components

$$
S _ {g, n} (\gamma) = \bigcup_ {i = 1} ^ {s} S _ {i},\tag{8.1}
$$

where$S _ { i } \cong S _ { g _ { i } , n _ { i } }$, and$A _ { i } = \partial S _ { i }$. Then we have

$$
V _ {g, n} (\Gamma , \mathbf {x}, \beta , L) = \prod_ {i = 1} ^ {k} V _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}}).
$$

Remark 1. The terms$\operatorname { S y m } ( \gamma )$and$M ( \gamma )$appear when$\gamma$has some extra symmetry. See 2 for the definition of$\operatorname { S y m } ( \gamma )$, the symmetry group of $\textstyle \gamma = \sum _ { i = 1 } ^ { k } c _ { i } \gamma _ { i }$. In fact$| \operatorname { S y m } ( \gamma ) | \neq 1$will put a non trivial restriction on the $c _ { i } \mathrm { ^ { * } s }$. More precisely, if$g ( \gamma _ { i } ) = \gamma _ { j }$for$g \in \mathrm { S y m } ( \gamma )$then$c _ { i } = c _ { j }$. Hence we have

$$
\sum_ {i = 1} ^ {k} c _ {i} \ell_ {\gamma_ {i}} = \sum_ {i = 1} ^ {k} c _ {i} \ell_ {g \cdot \gamma_ {i}}
$$

Remark 2. Since later will use lemma 8.1 to integrate the left hand side of equation 4.1 over${ \mathcal { M } } _ { g , n } ( L )$, it is essential that$\mathcal { D } ( x , y , z )$is in fact a function of x and$y + z \ ( \ S 3 )$.

By Theorem 8.1 integrating$f _ { \gamma }$, even for a compact Riemann surface, reduces to the calculation of volumes of moduli spaces of bordered Riemann surfaces.

Hamiltonian circle actions. Let$( M , \omega )$be a symplectic manifold. Then for any smooth function$H : M \to \mathbb { R }$, the vector field$X _ { H }$determined by

$$
\omega (X _ {H},.) = d H (.)
$$

is called the Hamiltonian vector field associated to H. Here we are interested in the case where$X _ { H }$generates an$S ^ { 1 }$action on$M$. In other words,$\psi _ { 1 } = \mathrm { i d }$2 where$\psi _ { t }$is the integral of the vector field$X _ { H }$. The Hamiltonian function H in this case is called the moment map of the action. See$\mathrm { [ M c D ] }$for more details.

Integration and covering. Let

$$
\pi : X _ {1} \to X _ {2}
$$

be a covering and$v _ { 2 }$a volume form on$X _ { 2 }$. Then$v _ { 1 } = \pi ^ { - 1 } { * ( v _ { 2 } ) }$defines a volume form on$X _ { 1 }$. If$f$is in$L ^ { 1 } ( X _ { 1 } , v _ { 1 } )$, then the push forward

$$
(\pi_ {*} f) (x) = \sum_ {y \in \pi^ {- 1} \{x \}} f (y)
$$

defines a function in$L ^ { 1 } ( X _ { 2 } , v _ { 2 } )$and we have

$$
\int_ {X _ {2}} \left(\pi_ {*} f\right) d v _ {2} = \int_ {X _ {1}} f d v _ {1}.\tag{8.2}
$$

Next we construct coverings of${ \mathcal { M } } _ { g , n }$and functions defined over them whose push forward to$\mathcal { M } _ { g , n }$is constant.

Coverings and volume forms of the$\mathcal { M } _ { g , n } ( L ) \mathbf { \bar { s } }$. For$h \in \operatorname { M o d } _ { g , n }$let

$$
h. \Gamma = (h \cdot \gamma_ {1}, \dots , h \cdot \gamma_ {k}).
$$

As in$\ S 2$, let$\mathcal { O } _ { \Gamma }$be the set of homotopy classes of elements of the set Mod Γ. Consider$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$defined by the following space of pairs:

$\{ ( X , \eta ) | X \in \mathcal { M } _ { g , n } ( L ) , \eta = ( \eta _ { 1 } , \dots , \eta _ { k } ) \in \mathcal { O } _ { \Gamma } , \eta _ { i }$’s are closed geodesics on$X \}$

Let$\pi ^ { \Gamma } : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathcal { M } _ { g , n } ( L )$be the projection map defined by

$$
\pi^ {\Gamma} (X, \eta) = X.
$$

Let$\phi _ { \gamma } \in \operatorname { M o d } _ { g , n }$denote the Dehn twist along$\gamma$. Then

$$
G _ {\Gamma} = \bigcap_ {i = 1} ^ {s} \operatorname{Stab} (\gamma_ {i}) \subset \operatorname{Mod} (S _ {g, n})
$$

is generated by the$\phi _ { \gamma _ { i } }$’s and elements of the mapping class group of$S _ { g , n } ( \gamma )$，and

$$
\mathcal {M} _ {g, n} (L) ^ {\Gamma} = \mathcal {T} _ {g, n} (L) / G _ {\gamma}.
$$

As the Weil-Petersson symplectic structure on Teichm¨uller space is invariant under the action of the mapping class group, it induces a symplectic structure on$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$which is the same as the form$\pi ^ { \Gamma * } ( w _ { w p } )$ In fact, the space$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$is closely related to the moduli space of hyperbolic structures over$S _ { g , n }$cut along$\{ \gamma _ { 1 } , \ldots , \gamma _ { k } \}$

Twisting and the Weil-Petesson symplectic form. The results of this section will arise from the existence of k commuting Hamiltonian$S ^ { 1 }$-actions on$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$. induced by twisting the surface along connected components of γ. We first describe the corresponding R-action on$\mathcal { T } _ { g , n } ( L )$as defined in 2.

Consider the length-normalized twist flow, given by

$$
\phi_ {\alpha} ^ {t} (X) = t w _ {\alpha} ^ {t \cdot \ell_ {\alpha} (X)} (X).
$$

Then

$$
\phi_ {\alpha} ^ {1} = \phi_ {\alpha} \in \mathrm{Stab} (\alpha)
$$

is the Dehn-Twist around α. See$\ S 2$for more details. Let$\ell _ { \Gamma } : T _ { g , n } \to \mathbb { R } _ { + } ^ { k }$ denote the length function defined by

$$
\ell_ {\Gamma} (X) = (\ell_ {\gamma_ {1}} (X), \dots , \ell_ {\gamma_ {k}} (X)).
$$

Then the level set

$$
\mathcal {T} _ {g, n} (a) = \ell_ {\Gamma} ^ {- 1} (a)
$$

carries a natural volume form$- * ( d \ell _ { \gamma _ { 1 } } \wedge \cdot \cdot \cdot d \ell _ { \gamma _ { k } } )$

Since$\ell _ { \alpha } ( X ) = \ell _ { \alpha } ( t w _ { \alpha } ^ { t } ( X ) )$, the map

$$
\phi_ {\gamma} ^ {(t _ {1}, \dots , t _ {k})}: \mathcal {T} _ {g, n} (a) \to \mathcal {T} _ {g, n} (a)
$$

gives rise to an action of$\mathbb { R } ^ { k }$on the level set$\mathcal { T } _ { g , n } ( a )$preserving the Weil-Petersson symplectic form. By cutting the surface along γ we get a Riemann surface with geodesic boundary components. Now Theorem 2.1 implies the following result:

Lemma 8.2. For any$( a _ { 1 } , \ldots , a _ { k } ) \in \mathbb { R } _ { + } ^ { k }$, the canonical map

$$
s: \ell_ {\Gamma} ^ {- 1} (a _ {1}, \ldots , a _ {k}) / \mathbb {R} ^ {k} \to \prod_ {i = 1} ^ {s} \mathcal {T} (S _ {i}, L _ {A _ {i}})
$$

sending each point$X \in \mathcal { T } _ { g , n }$to the surface that we get by cutting X along components of γ, is a symplectomorphism.

Induced flows on$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$. The length function$\ell _ { \Gamma }$descends to a function $\mathcal { L } _ { \Gamma }$on$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$

$$
\begin{array}{c} \mathbb {R} ^ {k} \xleftarrow {\mathcal {L}} \mathcal {M} _ {g, n} (L) ^ {\Gamma} \\ \Big \downarrow^ {\pi} \\ \mathcal {M} _ {g, n} (L) \end{array}
$$

where$\mathcal { L } _ { \Gamma } ( X , \eta ) = ( \ell _ { \eta _ { i } } ( X ) )$. The construction of the Fenchel-Nielsen flow defined on Teichm¨uller space is equivariant with respect to the action of the mapping class group. Therefore, we have:

Each level set

$$
\mathcal {M} _ {g, n} (L) ^ {\Gamma} (a) = \mathcal {L} ^ {- 1} (a _ {1}, \ldots , a _ {k}) \subset \mathcal {M} _ {g, n} (L) ^ {\Gamma}
$$

carries a natural volume form$v _ { a }$induced by$- * d { \mathcal { L } } = - * ( \bigwedge _ { i } d \ell _ { \gamma _ { i } } )$

The Hamiltonian flow of$\mathcal { L } _ { i } , t w _ { i }$, has closed orbits on$\mathcal { M } _ { g , n } ^ { \Gamma } ( a _ { 1 } , \ldots , a _ { k } )$ That is we have

$$
t w _ {i} ^ {t} (X, \eta) = (t w _ {\eta_ {i}} ^ {t} (X), \eta),
$$

where$t w _ { \eta _ { i } } ^ { t } ( X )$is obtained by cutting X along$\eta _ { i } .$, twisting to the right by hyperbolic length t and regluing the boundaries. Then for$t _ { i } =$ $\overset { \cdot } { \mathcal { L } _ { i } } ( Y ) , \ t w _ { i } ^ { t _ { i } ( Y ) }$is the Dehn twist of Y along$\eta _ { i }$which equals Y in $\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$

Therefore, the Hamiltonian flow of$\mathcal { L } ^ { 2 } / 2 : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathbb { R } _ { + } ^ { k }$gives rise to the action of$T ^ { k } = S ^ { 1 } \times \cdot \cdot \cdot \times S ^ { 1 }$by twisting along γ<sub>i</sub> proportional to its length.

The quotient space,

$$
\mathcal {M} _ {g, n} (L) ^ {\Gamma *} (a) = \mathcal {M} _ {g, n} (L) ^ {\Gamma} (a) / T ^ {k},
$$

where$\begin{array} { r } { T ^ { k } = \prod _ { i = 1 } ^ { k } S ^ { 1 } } \end{array}$inherits a symplectic structure from the symplectic structure of$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$. For an open set$U \subset { \mathcal { M } } _ { g , n } ( L ) ^ { \Gamma * } ( a )$, and the projection map

$$
\pi : \mathcal {M} _ {g, n} (L) ^ {\Gamma} (a) \to \mathcal {M} _ {g, n} (L) ^ {\Gamma *} (a).
$$

Note in general the twisting parameter along$\gamma _ { i }$can be between 0 and$\ell _ { \gamma _ { i } }$. In the case of a simple geodesic$\gamma _ { i }$separating of a one-handle (the elliptic tail case)$\operatorname { S t a b } ( \gamma _ { j } )$contains a half twist and so τ varies with fundamental region $\{ 0 \le \tau \le \ell \gamma _ { i } / 2 \}$. The reason is that every$X \in \mathcal { M } _ { 1 , 1 } ( L )$comes with an elliptic involution, but when$( g , n ) \neq ( 1 , 1 )$, a generic point in${ \mathcal { M } } _ { g , n } ( L )$does not have any non trivial automorphism fixing the boundary components set wise. Therefore, since$- * d \mathcal { L } ^ { 2 } = - * d \mathcal { L } / \mathcal { L }$, we get

$$
\operatorname{Vol} (\pi^ {- 1} (U)) = 2 ^ {- M (\gamma)} \operatorname{Vol} (U) \cdot a _ {1} \dots a _ {k},\tag{8.3}
$$

where$M ( \gamma )$is the number of connected components$\gamma$separating of a onehandle.

$$
\begin{array}{c} \mathcal {M} _ {g, n} (L) ^ {\Gamma} (a) \xrightarrow {\pi} \mathcal {M} _ {g, n} (L) ^ {\Gamma *} (a) \cong \prod \mathcal {M} _ {g _ {i}, n _ {i}, A _ {i}} \\ \Big \downarrow \\ \mathcal {M} _ {g, n} (L) \end{array}
$$

Therefore, we have the following result:

Lemma 8.3. For any k-tuple$\Gamma = ( \gamma _ { 1 } , \dots , \gamma _ { k } )$of disjoint simple closed curves, the canonical isomorphism

$$
s: \mathcal {M} _ {g, n} (L) ^ {\Gamma *} (a) \to \mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = a, L _ {\beta} = L) \cong \prod_ {i = 1} ^ {s} \mathcal {M} _ {g _ {i}, n _ {i}} (\ell_ {A _ {i}})
$$

is a symplectomorphism.

Remark. By what we said,$\mathcal { L } ^ { 2 } / 2$is the moment map for the$T ^ { k }$action, and the space$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma * } ( a )$is a symplectic quotient space ( See [Ki]). In [Mirz2], we use this fact to relate the volume polynomials to the intersection pairings of tautological classes over the moduli space.

Integrating geometric functions. Now we can use the preceding lemma to integrate certain functions over the covering space$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$

Lemma 8.4. For any function$F : \mathbb { R } ^ { k }  \mathbb { R }$, define$F _ { \gamma } : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathbb { R }$by

$$
F _ {\gamma} (Y) = F (\mathcal {L} (Y)).
$$

Then the integral of$F _ { \gamma }$over$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma }$is given by

$$
\int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma}} F _ {\gamma} (Y) d Y = 2 ^ {- M (\gamma)} \int_ {\mathbf {x} \in \mathbb {R} _ {+} ^ {k}} F (\mathbf {x}) \mathrm{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\beta} = L, \ell_ {\Gamma} = \mathbf {x})) \textbf {x} d \mathbf {x},
$$

$$
w h e r e \mathbf {x} = (x _ {1}, \dots , x _ {n}) a n d \mathbf {x} \cdot d \mathbf {x} = x _ {1} \dots x _ {n} \cdot d x _ {1} \wedge \dots \wedge d x _ {n}.
$$

Proof. Note that the function$F _ { \gamma }$is constant on each level set of$\mathcal { M } _ { g , n } ( L ) ^ { \Gamma } ( a )$ of . Using Lemma 8.3 and equation 8.3, we get

$$
\operatorname{Vol} \left(\mathcal {L} ^ {- 1} \left(a _ {1}, \dots , a _ {k}\right)\right) = 2 ^ {- M (\gamma)} a _ {1} \dots a _ {k} \cdot \operatorname{Vol} \left(\mathcal {M} \left(S _ {g, n} (\gamma), \ell_ {\beta} = L, \ell_ {\Gamma} = a\right)\right),
$$

and as a result we get

$$
\begin{array}{c} I (a) = \int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma} (a)} F (\ell_ {\gamma} (X)) d X = 2 ^ {- M (\gamma)} \times \\ F (a) \cdot \mathrm{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\beta} = L, \ell_ {\gamma} = a)) \cdot a _ {1} \dots a _ {k}. \end{array}
$$

Now the result is immediate, since by Theorem 2.1, we have

$$
\int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma}} F _ {\gamma} (Y) d Y = \int_ {\mathbf {x} \in \mathbb {R} _ {+} ^ {k}} I (\mathbf {x}) d \mathbf {x}
$$

Now we are ready to prove the main result of this section Proof of Theorem 8.1. The function

$$
\pi_ {*} ^ {\Gamma} f: \mathcal {M} _ {g, n} (L) \to \mathbb {R} _ {+}
$$

is given by

$$
\pi_ {*} ^ {\Gamma} f (X) = \sum_ {h \in \operatorname{Mod} _ {g, n} / \cap \operatorname{Stab} (\gamma_ {i})} f (\ell_ {h \cdot \gamma} (X)).\tag{8.4}
$$

Therefore by using equation (8.2) and Lemma 8.3, using the notation of Lemma 8.4 the integral of$\pi _ { * } ^ { \Gamma } f$over the moduli space is given by

$$
\int_ {\mathcal {M} _ {g, n} (L)} \pi_ {*} ^ {\Gamma} f (X) d X = \int_ {\mathcal {M} _ {g, n} (L) ^ {\Gamma}} F _ {\gamma} (Y) d Y,
$$

where$F ( x _ { 1 } , \dots , x _ { k } ) = f ( \sum _ { i = 1 } ^ { k } c _ { i } x _ { i } )$. Now we can use Lemma 8.4 to see that

$$
\int_ {\mathcal {M} _ {g, n} (L)} \pi_ {*} ^ {\Gamma} f (X) d X
$$

equals

$$
2 ^ {- M (\gamma)} \iint_ {(\mathbf {x}, t) \in V} f (| \mathbf {x} |) \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma), \ell_ {\Gamma} = \mathbf {x}, \ell_ {\beta} = L)) \cdot \mathbf {x} \cdot d \mathbf {x}   d t.
$$

On the other hand, we have,

$$
\sum_ {g \in \operatorname{Mod} _ {g, n} / \cap \operatorname{Stab} (\gamma_ {i})} f (\ell_ {g}. \gamma (X)) = \operatorname{Sym} (\gamma) \cdot \sum_ {[ \alpha ] \in [ \gamma ] \cdot \operatorname{Mod} _ {g, n}} f (\ell_ {\alpha} (X),
$$

where

$$
\operatorname{Sym} (\gamma) = | \operatorname{Stab} (\gamma) / \cap \operatorname{Stab} (\gamma_ {i}) |.
$$

Hence we get

$$
\pi_ {*} ^ {\Gamma} f (X) = \mathrm{Sym} (\gamma) \cdot f _ {\gamma} (X).
$$

## 9 Volumes of moduli spaces of bordered Riemann surfaces

In this section we use the identity for lengths of simple closed geodesics in Theorem 4.2 to derive the recursive formula for the$V _ { g , n } ( L ) / \mathrm { s }$stated in 5. Idea of the calculation of$V _ { g , n } ( L )$. By Theorem 4.2, for any$X \in$ $T _ { g , n } ( L _ { 1 } , \ldots , L _ { n } )$we have

$$
\sum_ {\{\alpha_ {1}, \alpha_ {2} \} \in \mathcal {F} _ {1}} \mathcal {D} (L _ {1}, \ell_ {\alpha_ {1}} (X), \ell_ {\alpha_ {2}} (X)) + \sum_ {i = 2} ^ {n} \sum_ {\gamma \in \mathcal {F} _ {1, i}} \mathcal {R} (L _ {1}, L _ {i}, \ell_ {\gamma} (X)) = L _ {1},\tag{9.1}
$$

where as in$\ S 4 , \mathcal { F } _ { 1 }$and$\mathcal { F } _ { 1 , j }$are respectively in one to one correspondence with the set of pairs of pants containing$\beta _ { 1 }$and$\{ \beta _ { 1 } , \beta _ { j } \}$. Now let

$$
\tilde {\mathcal {R}} _ {j} (X) = \sum_ {\gamma \in \mathcal {F} _ {1, j}} \mathcal {R} (L _ {1}, L _ {j}, \ell_ {\gamma} (X)),\tag{9.2}
$$

and

$$
\tilde {\mathcal {D}} (X) = \sum_ {(\alpha_ {1}, \alpha_ {2}) \in \mathcal {F} _ {1}} \mathcal {D} (L _ {1}, \ell_ {\alpha} (X), \ell_ {\beta} (X)).
$$

Then from 9.1 we get

$$
\tilde {\mathcal {D}} (X) + \sum_ {j = 2} ^ {n} \tilde {\mathcal {R}} _ {j} (X) = L _ {1},
$$

where$\tilde { \mathcal { D } }$and$\mathcal { \tilde { R } } _ { j }$are functions defined on${ \mathcal { M } } _ { g , n } ( L )$

We use the description of$\mathcal { F } _ { i } / \operatorname { M o d } _ { g , n }$and$\mathcal { F } _ { i , j } / \operatorname { M o d } _ { g , n }$to reformulate $\mathcal { \tilde { R } } _ { j }$and$\tilde { \mathcal { D } }$as push forwards of functions defined over certain coverings of the moduli space of the form described in$\ S 8$. This enables us to apply Theorem 8.1 and integrate these functions over$\mathcal { M } _ { g , n } ( L )$

Topology of pairs of pants on a surface. We characterize the set of topologically diferent pairs of pants containing$\beta _ { 1 }$

![](images/page_43_image_0.jpg)

Figure 8. a): ∂(Σ)$\cap \partial S _ { g , n } | = 1$, separating case b): non-separating case <sup>c):</sup> |<sup>∂(Σ)</sup>$\cap \partial S _ { g , n } | = 2$

Let Σ be a pair of pants such that$\beta _ { 1 } \in \partial ( \Sigma )$. Then as in Figure 8 one of the following holds.

I): Σ contains two boundary components. If$\partial ( \Sigma ) \cap \partial ( S _ { g , n } ) = \{ \beta _ { 1 } , \beta _ { j } \}$, as in Fig 7.c, then$\partial \Sigma \in \mathcal { F } _ { 1 , j }$, and$S _ { g , n } ( \Sigma )$is homeomorphic to$S _ { g , n - 1 }$(See also the definition of$B _ { g , n } )$

II): Σ contains one boundary component. If$\partial ( \Sigma ) \cap \partial ( S _ { g , n } ) = \{ \beta _ { 1 } \}$ then$\Sigma \in { \mathcal { F } } _ { 1 }$, and$S _ { g , n } ( \Sigma )$can have 1 or 2 connected components.

Σ is non-separating: In this case, as in Fig$7 . \mathrm { b } , S _ { g , n } ( \Sigma )$is homeomorphic to$S _ { g - 1 , n + 1 }$(See also the definition of$\boldsymbol { \mathcal { A } } _ { g , n } ^ { c o n } )$

Σ is separating: In this case , as in Fig 7.a, the elements of$\mathcal { T } _ { g , n }$are in oneto-one correspondence with diferent topological types of separating pairs of pants such that$\partial ( \Sigma ) \cap \partial ( S _ { g , n } ) = \{ \beta _ { 1 } \}$(See also the definition of$\mathcal { A } _ { g , n } ^ { d c o n } )$

The action of${ \mathrm { M o d } } _ { g , n }$on$\mathcal { F } _ { 1 }$is not transitive, nevertheless the orbits can be characterized by the topology of their complementary regions which is determined by the number of the connected components, genus and the number of boundary components of each connected component.

Proof of the recursive formula. Now we are ready to prove the recursive formula stated in 5.

Theorem 9.1. For$( g , n ) \neq ( 1 , 1 ) , ( 0 , 3 )$, the volume function$V _ { g , n } ( L )$satisfies

$$
\frac {\partial}{\partial L _ {1}} L _ {1} V _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L) + \mathcal {A} _ {g, n} ^ {d c o n} (L) + \mathcal {B} _ {g, n} (L).\tag{9.3}
$$

Proof. We can integrate both sides of the equation

$$
\tilde {\mathcal {D}} (X) + \sum_ {i = 2} ^ {n} \sum \tilde {\mathcal {R}} _ {i} (X) = L _ {1}
$$

over$\mathcal { M } _ { g , n } ( L )$with respect to the volume form induced by the Weil-Petersson symplectic form.

Therefore from equation 9.2 we get

$$
\sum_ {2 \leq j} \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {R}} _ {j} (X) d X + \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {D}} (X) d X = L _ {1} \cdot V _ {g, n} (L).\tag{9.4}
$$

Next we calculate the integrals

$$
\mathcal {R} _ {g, n} ^ {j} (L) = \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {R}} _ {j} (X) d X,
$$

and

$$
\mathcal {D} _ {g, n} (L) = \int_ {\mathcal {M} _ {g, n} (L)} \tilde {\mathcal {D}} (X) d X.
$$

$I )$: Integrating$\mathcal { \tilde { R } } _ { j }$. For$1 \neq j$the mapping class group$\operatorname { M o d } _ { g , n }$acts transitively on$\mathcal { F } _ { 1 , j }$and for any$\gamma \in \mathcal { F } _ { 1 , j }$we have

$$
\mathrm{Mod} _ {g, n} \cdot \{\gamma \} = \mathcal {F} _ {1, j}.
$$

Let$\gamma _ { j }$be a simple closed curve in$\mathcal { F } _ { 1 , j }$. Consider the map$\pi ^ { \gamma _ { j } } : \mathcal { M } _ { g , n } ( L ) ^ { \gamma _ { j } } \to$ ${ \mathcal { M } } _ { g , n } ( L )$, and define$\mathcal { R } _ { \gamma _ { j } } : \mathcal { M } _ { g , n } ( L ) ^ { \Gamma } \to \mathbb { R } _ { + }$by

$$
\mathcal {R} _ {\gamma_ {j}} (X) = \mathcal {R} (L _ {1}, L _ {j}, \ell_ {\gamma_ {j}} (X)).
$$

Hence, we get

$$
\pi_ {*} ^ {\gamma_ {j}} \mathcal {R} _ {\gamma_ {j}} (X) = \sum_ {\gamma \in \mathcal {F} _ {1, j} / \operatorname{Mod}} \mathcal {R} (L _ {1}, L _ {j}, \ell_ {\gamma} (X)),
$$

and

$$
\tilde {\mathcal {R}} _ {j} (X) = \pi_ {*} ^ {\gamma_ {j}} \mathcal {R} _ {\gamma_ {j}}.
$$

As$S _ { g , n } ( \gamma _ { j } ) = S _ { g , n - 1 }$, and$| \operatorname { S t a b } ( \gamma ) | = 1$, by using Theorem 8.1 to show that we have

$$
\mathcal {R} _ {g, n} ^ {j} (L) = 2 ^ {- m (g, n - 1)} \int_ {0} ^ {\infty} x \cdot \mathcal {R} (L _ {1}, L _ {j}, x) \cdot \operatorname{Vol} (\mathcal {M} (S _ {g, n} (\gamma_ {j}), \ell_ {\gamma_ {j}} = x, L)) d x
$$

$$
= 2 ^ {- m (g, n - 1)} \int_ {0} ^ {\infty} x \cdot \mathcal {R} (L _ {1}, L _ {j}, x) \cdot V _ {g, n - 1} (x, L _ {2}, \ldots , \hat {L _ {j}}, \ldots , L _ {n}) d x,
$$

which can be calculated in terms of$V _ { g , n - 1 }$

Therefore, from equation 3.5

$$
\frac {\partial}{\partial L _ {1}} \mathcal {R} _ {g, n} ^ {j} (L)
$$

equals

$$
\frac {2 ^ {- m (g , n - 1)}}{2} \int_ {0} ^ {\infty} x \left(H (x, L _ {1} - L _ {j}) + H (x, L _ {1} + L _ {j})\right) V _ {g, n - 1} (x, L _ {2}, \dots , \hat {L _ {j}}, \dots , L _ {n}) d x.
$$

Hence, from the definition of$B _ { g , n }$we have

$$
\sum_ {j = 2} ^ {n} \frac {\partial}{\partial L _ {1}} \mathcal {R} _ {g, n} ^ {j} (L) = \mathcal {B} _ {g, n} (L).\tag{9.5}
$$

$I I ) .$: Integrating$\tilde { \mathcal { D } }$. Here we sketch the calculation for$\tilde { \mathcal { D } }$. For$\{ \alpha _ { 1 } , \alpha _ { 2 } \} \in$ $\mathcal { F } _ { 1 }$, let$\alpha ~ = ~ \alpha _ { 1 } + \alpha _ { 2 }$. It is essential that by Lemma 3.1, the function ${ \mathcal { D } } ( L _ { 1 } , \ell _ { \alpha _ { 1 } } ( X ) , \ell _ { \alpha _ { 2 } } ( X ) )$is in fact a function of$L _ { 1 }$and$\ell _ { \alpha } ( X ) = \ell _ { \alpha 1 } ( X ) +$ $\ell _ { \alpha _ { 2 } } ( X )$. Therefore by classifying the${ \mathrm { M o d } } _ { g , n }$orbits of$\mathcal { F } _ { 1 }$, we can use Theorem 8.1 for$\alpha = \alpha _ { 1 } + \alpha _ { 2 }$

As in$\ S 5$, let$\mathcal { T } _ { g , n }$be the set of all possible combinations of the genus and set of boundary components of the complementary regions of elements of $\mathcal { F } _ { 1 }$. We can classify the orbits of the action of the mapping class group as follows.

Define$A ^ { c o n }$to be the set of$\alpha _ { 1 } + \alpha _ { 2 }$such that the complement of the pair of pants containing$\beta _ { 1 } , \alpha _ { 1 } , \alpha _ { 2 }$is a connected surface of genus$g - 1$ with$n { \mathrel { + { 1 } } }$boundary components. (See Figure 8). Then$\begin{array} { r } { | \operatorname { S y m } ( \alpha ) | = \frac { 1 } { 2 } } \end{array}$ See 2

For$a \in ( ( g _ { 1 } , I ) , ( g _ { 2 } , J ) ) \in \mathcal { T } _ { g , n } .$, let$A _ { a }$be the set of$\alpha = \alpha _ { 1 } + \alpha _ { 2 }$such that the complement of the pair of pants containing$\beta _ { 1 } , \alpha _ { 1 }$and$\alpha _ { 2 }$is a disjoint union of two surfaces$S _ { 1 }$and$S _ { 2 }$, respectively homeomorphic to$S _ { g _ { 1 } , n _ { 1 } + 1 }$and$S _ { g - g _ { 1 } , n _ { 2 } + 1 }$, such that we have:

$$
\left\{\beta_ {i _ {1}}, \dots , \beta_ {i _ {n _ {1}}} \right\} \subset \partial S _ {1}, \left\{\beta_ {j _ {1}}, \dots , \beta_ {j _ {n _ {2}}} \right\} \subset \partial S _ {2}.
$$

See Figure 8. The action of the mapping class group on${ \mathcal { A } } ^ { c o n }$and$A _ { a } \ ( a \in$ $\mathcal { T } _ { g , n } )$is transitive and we have

$$
\mathcal {F} _ {1} = A ^ {c o n} \bigcup A ^ {d c o n},
$$

where

$$
A ^ {d c o n} = \bigcup_ {a \in \mathcal {I} _ {g, n}} A _ {a}.
$$

Choose$\gamma \in A ^ { c o n }$and also, for each$a \in \mathcal { T } _ { g , n }$, choose$\alpha _ { a }$an element of the set$\mathcal { A } _ { a }$. Define the set of representatives of the distinct orbits of$\mathcal { T } _ { g , n } , \mathcal { C }$by

$$
\mathcal {C} = \{\alpha_ {a} \mid a \in \mathcal {I} _ {g, n} \} \cup \{\gamma \}.
$$

Hence${ \mathcal { C } } \cong { \mathcal { F } } _ { 1 } / \operatorname { M o d } _ { g , n }$, and we have:

$$
\tilde {\mathcal {D}} (X) = \sum_ {\alpha = \alpha_ {1} + \alpha_ {2} \in \mathcal {C}} \pi_ {*} ^ {\alpha} \mathcal {D} _ {\alpha} (X),
$$

where$\tilde { \mathcal { D } } : \mathcal { M } _ { g , n } ^ { \alpha } ( L ) \to \mathbb { R } _ { + }$is defined by

$$
\mathcal {D} _ {\alpha} (X) = \mathcal {D} (L _ {1}, \ell_ {\alpha_ {1}} (X), \ell_ {\alpha_ {2}} (X)).
$$

Also by what we showed in 2, for$\alpha \in A _ { a }$we have$| \operatorname { S y m } ( \alpha ) | = 2$if and only if$I = J = \phi$and$g _ { 1 } = g _ { 2 }$, otherwise$| \operatorname { S y m } ( \alpha ) | = 1$

Therefore, from eqaution 3.4 and the definition of${ \mathcal { A } } ^ { c o n }$and$A ^ { d c o n }$, we get

$$
\frac {\partial}{\partial L _ {1}} \mathcal {D} _ {g, n} (L) = \mathcal {A} _ {g, n} ^ {c o n} (L) + \mathcal {A} _ {g, n} ^ {d c o n} (L).\tag{9.6}
$$

Now the result is immediate from equations 9.4, 9.5 and 9.6.

Remark. The term$1 / 2$in equation 5.2 comes from sym(α) when α is non seperating. Also, as the sum in the definition of$\widehat { \mathcal { A } _ { g } , n } ^ { d c o n }$is over ordered pairs$\left( { \left( { { g _ { 1 } } , { I _ { 1 } } } \right) , \left( { { g _ { 2 } } , { I _ { 2 } } } \right) } \right)$in fact every term in the integral appears twice except for the term corresponding to the$g _ { 1 } = g _ { 2 }$, and$I _ { 1 } = I _ { 2 } = \phi$. So by considering$1 / 2$in equation 5.3, we will take care of the$\operatorname { S y m } ( \alpha )$

## References

[B] A. Basmajian. The orthogonal spectrum of a hyperbolic manifold. Amer. J. Math. 115(1993), 1139–1159.

[BS] J. S. Birman and C. Series. Geodesics with bounded intersection number on surfaces are sparsely distributed. Topology 24(1985), 217–225.

[Bus] P. Buser. Geometry and Spectra of Compact Riemann Surfaces. Birkh¨auser Boston, 1992.

[CEG] R. D. Canary, D. B. A. Epstein, and P. Green. Notes on notes of Thurston. In Analytical and Geometric Aspects of Hyperbolic Space, pages 3–92. Cambridge University Press, 1987.

[Gol] W. Goldman. The symplectic nature of fundamental groups of surfaces. Adv. Math. 54(1984), 200–225.

[Har] J. Harris and I. Morrison. Moduli of curves, volume 187 of Graduate Texts in Mathematics. Springer-Verlag, 1998.

[KMZ] R. Kaufmann, Y.Manin, and D. Zagier. Higher Weil-Petersson volumes of moduli spaces of stable n-pointed curves. Comm. Math. Phys. 181(1996), 736–787.

[Ki] F. Kirwan. Momentum maps and reduction in algebraic geometry. Diferential Geom.Appl. 9(1998), 135–171.

[K] M. Kontsevich. Intersection on the moduli space of curves and the matrix airy function. Comm. Math. Phys. 147(1992).

[MaZ] Y. Manin and P. Zograf. Invertible cohomological field theories and Weil-Petersson volumes. Ann. Inst. Fourier(Grenoble) 50(2000), 519–535.

[McD] D. McDuf. Introduction to symplectic topology. Amer. Math. Soc., Providence, RI, 1999.

[M] G. McShane. Simple geodesics and a series constant over Teichm¨uller space. Invent. math. 132(1998), 607–632.

[Mirz1] M. Mirzakhani. Growth of the number of simple closed geodesics on a hyperbolic surface. Preprint, 2003.

[Mirz2] M. Mirzakhani. Weil-Petersson volumes and intersection theory on the moduli space of curves. Preprint, 2003.

[NN] T. Nakanishi and M. N¨a¨at¨anen. Areas of two-dimensional moduli spaces. Proc. Amer. Math. Soc. 129(2001), 3241–3252.

[Pen] R. Penner. Weil-Petersson volumes. J. Diferential Geom. 35(1992), 559–608.

[Wol1] S. Wolpert. The Fenchel-Nielsen deformation. Annals of Math. 115(1982), 501–528.

[Wol2] S. Wolpert. On the homology of the moduli space of stable curves. Ann. of Math.(2) 118(1983), 491–523.

[Zo] P. Zograf. The Weil-Petersson volume of the moduli space of punctured spheres. In Mapping class groups and moduli spaces of Riemann surfaces, volume 150 of Contemp. Math., pages 367–372. Amer. Math. Soc., 1993.