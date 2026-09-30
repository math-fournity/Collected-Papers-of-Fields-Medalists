# WEIL-PETERSSON VOLUMES AND INTERSECTION THEORY ON THE MODULI SPACE OF CURVES

MARYAM MIRZAKHANI

## 1. Introduction

In this paper, we establish a relationship between the Weil-Petersson volume $V _ { g , n } ( b )$of the moduli space${ \mathcal { M } } _ { g , n } ( b )$of hyperbolic Riemann surfaces with geodesic boundary components of lengths$b _ { 1 } , \ldots , b _ { n }$, and the intersection numbers of tautological classes on the moduli space${ \overline { { \mathcal { M } } } } _ { g , n }$of stable curves. As a result, by using the recursive formula for$V _ { g , n } ( b )$obtained in [22], we derive a new proof of the Virasoro constraints for a point. This result is equivalent to the Witten-Kontsevich formula [14].

Intersection theory of${ \overline { { \mathcal { M } } } } _ { g , n }$. Let${ \mathcal { M } } _ { g , n }$be the moduli space of genus g curves with n distinct marked points and${ \overline { { \mathcal { M } } } } _ { g , n }$its Deligne-Mumford compactification. The space${ \overline { { \mathcal { M } } } } _ { g , n }$is a connected complex orbifold of dimension$3 g - 3 + n$[9]. These moduli spaces are endowed with natural cohomology classes. An example of such a class is the Chern class of a vector bundle on the moduli space. There are n tautological line bundles defined over${ \overline { { \mathcal { M } } } } _ { g , n }$: for each marked point i, there exists a canonical line bundle$\mathcal { L } _ { i }$in the orbifold sense whose fiber at the point$( C , x _ { 1 } , \dots , x _ { n } ) \in { \overline { { \mathcal { M } } } } _ { g , n }$ is the cotangent space of$C$at$x _ { i }$. The first Chern class of this bundle is denoted by$\psi _ { i } = c _ { 1 } ( \mathcal { L } _ { i } )$. Note that although the complex curve$C$may have nodes,$x _ { i }$never coincides with the singular points.

For any set$\{ d _ { 1 } , \ldots , d _ { n } \}$of integers define the top intersection number of$\psi$classes by

$$
\langle \tau_ {d _ {1}}, \ldots , \tau_ {d _ {n}} \rangle_ {g} = \int_ {\overline {{\mathcal {M}}} _ {g, n}} \prod_ {i = 1} ^ {n} \psi_ {i} ^ {d _ {i}}.
$$

Such products are well defined when the$d _ { i }$’s are nonnegative integers and$\sum _ { i = 1 } ^ { n } d _ { i } =$ $3 g - 3 + n$. In other cases$\langle \tau _ { d _ { 1 } } , \dots , \tau _ { d _ { n } } \rangle _ { g }$is defined to be zero. Since we are in the orbifold setting, these intersection numbers are rational numbers. See [15] and [9] for more details.

Introduce formal variables$t _ { i } , i \geq 0$, and define$F _ { g }$, the generating function of all top intersections of$\psi$classes in genus$g$, by

$$
F _ {g} (t _ {0}, t _ {1}, \dots) = \sum_ {\{d _ {i} \}} \langle \prod \tau_ {d _ {i}} \rangle_ {g} \prod_ {r > 0} t _ {r} ^ {n _ {r}} / n _ {r}!,
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Received by the editors April 6, 2004.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2000 Mathematics Subject Classification. Primary 32G15, 14H15.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">The author is supported by a Clay fellowship.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">c 2006 American Mathematical Society Reverts to public domain 28 years from publication</span></small>

where the sum is over all sequences of nonnegative integers$\{ d _ { i } \}$with finitely many nonzero terms, and$n _ { r } = \mathrm { C a r d } ( i : d _ { i } = r )$. The generating function

$$
F = \sum_ {g = 0} ^ {\infty} \lambda^ {2 g - 2} F _ {g}
$$

arises as a partition function in two-dimensional quantum gravity.

Witten [28] conjectured a recursive formula for the intersections of tautological classes in the form of KdV diferential equations satisfied by$F$. Witten’s conjecture implies that$e ^ { F }$is annihilated by a sequence of diferential operators

$$
L _ {- 1}, L _ {0}, \ldots , L _ {n}, \ldots
$$

satisfying the Virasoro relations

$$
[ L _ {m}, L _ {k} ] = (m - k) L _ {m + k}.
$$

See [5] and [1]. Also, for the definition of the$L _ { i }$'s, see §6.

The Virasoro constraints determine the intersection numbers of tautological line bundles in all genera.

In [14], Kontsevich introduces a matrix model as the generating function for the intersection numbers on the moduli space to prove Witten’s conjecture by expressing intersection numbers in terms of sums over ribbon graphs. Also, A. Okounkov and R. Pandharipande gave a diferent proof by using the relation between the Gromov-Witten theory of$\mathbb { P } ^ { 1 }$and Hurwitz numbers [25]. For expository accounts of these proofs, see [15] and [24].

In this paper we prove that$F$, the generating function of the intersection numbers, satisfies the Virasoro constraints. Our proof relies on the Weil-Petersson symplectic geometry of the moduli space of curves and results of G. McShane [20] on lengths of simple closed geodesics on hyperbolic surfaces.

Weil-Petersson geometry of${ \overline { { \mathcal { M } } } } _ { g , n }$. The key tool for obtaining the recursive formula for the intersections of the tautological classes is understanding the relationship between the tautological classes and the Weil-Petersson symplectic form.

This form is the symplectic form of a Kähler, noncomplete metric on the moduli space of curves introduced by A. Weil [10]. In [18], Masur obtained growth estimates for the coeficients of the Weil-Petersson metric close to the boundary of the moduli space. In [33], Wolpert showed that the Weil-Petersson symplectic form has a simple expression in terms of the Fenchel-Nielsen twist-length coordinates (see §2). Moreover, he showed that the Weil-Petersson Kähler form ω extends as a closed form to${ \overline { { \mathcal { M } } } } _ { g , n }$and defines a cohomology class$[ \omega ] \in H ^ { 2 } ( \overline { { \mathcal { M } } } _ { g , n } , \mathbb { R } )$. See §2 for more details.

Volumes of moduli spaces of bordered Riemann surfaces. The Weil-Petersson volume of the moduli space${ \mathcal { M } } _ { g , n }$is a finite number and its value as a function of$g$and n arises naturally in diferent contexts.

In order to integrate certain types of geometric functions over the moduli space [22], we find it fruitful to consider more generally the moduli space$\mathcal { M } _ { g , n } ( b _ { 1 } , \ldots , b _ { n } )$ of hyperbolic bordered Riemann surfaces with the geodesic boundary components $\beta _ { 1 } , \ldots , \beta _ { n }$of length$b _ { 1 } , \ldots , b _ { n }$. We calculate the Weil-Petersson volume$V _ { g , n } ( b )$of the moduli space$\mathcal { M } _ { g , n } ( b )$using two diferent methods.

(I): In [22], we approach the study of the volumes of these moduli spaces via the length functions of simple closed geodesics on a hyperbolic surface and show that$V _ { g , n } ( b )$is a polynomial in b. We also give an explicit recursive method for calculating these polynomials (see §5).

(II): In §4, we use the symplectic geometry of moduli spaces of bordered Riemann surfaces to calculate these volumes. This method allows us to read off the intersection numbers of tautological line bundles from the volume polynomials.

(I): A recursive formula for volumes. By using an identity for lengths of simple closed geodesics on a bordered Riemann surface which generalizes the result in [20], we obtain a recursive formula for$V _ { g , n } ( b )$in terms of$V _ { g _ { 1 } , n _ { 1 } } ( b )$'s where $2 g _ { 1 } + n _ { 1 } < 2 g + n$(see equation (5.5)).

As a result, we establish:

Theorem 1.1. The volume$V _ { g , n } ( b ) = \mathrm { V o l } ( \mathcal { M } _ { g , n } ( b _ { 1 } , \ldots , b _ { n } ) )$is a polynomial in $b _ { 1 } , \ldots , b _ { n }$, namely:

$$
V _ {g, n} (b) = \sum_ {| \alpha | \leq 3 g - 3 + n} C _ {g} (\alpha) \cdot b ^ {2 \alpha},
$$

where$C _ { g } ( \alpha ) > 0$lies in$\pi ^ { 6 g - 6 + 2 n - 2 | \alpha | } \cdot \mathbb { Q }$

Here the exponent$\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ranges over elements in$( \mathbb { Z } _ { \geq 0 } ) ^ { n } , \ b ^ { \alpha } \ =$ $b _ { 1 } ^ { \alpha _ { 1 } } \cdot \cdot \cdot b _ { n } ^ { \alpha _ { n } }$, and$\textstyle | { \boldsymbol { \alpha } } | = \sum _ { i = 1 } ^ { n } { \boldsymbol { \alpha } } _ { i }$

(II): Symplectic geometry of$\mathcal { M } _ { g , n } ( b )$. To understand the symplectic geometry of$\mathcal { M } _ { g , n } ( b )$, we study a natural$T ^ { n }$-bundle over the compactification of this space. The space$\mathcal { M } _ { g , n } ( b )$has a natural orbifold structure. Moreover, the tautological line bundle$\mathcal { L } _ { i }$over${ \overline { { \mathcal { M } } } } _ { g , n }$can be generalized to the following circle bundle (in the orbifold sense) over${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$

$$
\begin{array}{c} S ^ {1} \longrightarrow \{(X, p) \mid p \in \beta_ {i}, X \in \overline {{\mathcal {M}}} _ {g, n} (b) \} \\ \Big \downarrow \\ \overline {{\mathcal {M}}} _ {g, n} (b) \end{array}
$$

where$S ^ { 1 }$acts by moving the point$p$on$\beta _ { i }$. This shows that${ \overline { { \mathcal { M } _ { g , n } } } } ( b )$is a reduced space. Hence we can use the method of symplectic reduction, discussed in §3, to relate the volumes of moduli spaces of curves to the intersection numbers of tautological classes on${ \overline { { \mathcal { M } } } } _ { g , n }$ (§4).

Note that the picture is a bit diferent when$g = n = 1$, in which case all elements of$\mathcal { M } _ { 1 , 1 } ( b )$have nontrivial automorphisms of order 2; namely, every$X \in \mathcal { M } _ { 1 , 1 } ( b )$ comes with an elliptic involution.

When$( g , n ) \neq ( 1 , 1 )$, a generic element of${ \mathcal { M } } _ { g , n } ( b )$does not have any non trivial automorphism which leaves the boundary components setwise fixed. In this case, the coeficient$C _ { g } ( \alpha )$in Theorem 1.1 is given by

$$
C _ {g} (\alpha) = \frac {1}{2 ^ {| \alpha |} | \alpha | ! (3 g - 3 + n - | \alpha |) !} \int_ {\overline {{\mathcal {M}}} _ {g, n}} \psi_ {1} ^ {\alpha_ {1}} \dots \psi_ {n} ^ {\alpha_ {n}} \cdot \omega^ {3 g - 3 + n - | \alpha |},\tag{1.1}
$$

where$\psi _ { i }$is the first Chern class of the i-th tautological line bundle, ω is the Weil-Petersson symplectic form,$\textstyle \alpha ! = \prod _ { i = 1 } ^ { n } \alpha _ { i } !$, and$\textstyle | { \boldsymbol { \alpha } } | = \sum _ { i = 1 } ^ { n } { \boldsymbol { \alpha } } _ { i }$

Remark. By a result of Wolpert [31],

$$
\kappa_ {1} = \frac {[ \omega ]}{2 \pi},
$$

where$\kappa _ { 1 }$is the first Mumford tautological class on$\overline { { \mathcal { M } _ { g , n } } }$

Examples. Using the recursive formula in Section$5 ,$one can show that

$$
V _ {0, 4} (b _ {1}, b _ {2}, b _ {3}, b _ {4}) = \frac {1}{2} (4 \pi^ {2} + b _ {1} ^ {2} + b _ {2} ^ {2} + b _ {3} ^ {2} + b _ {4} ^ {2}).
$$

Therefore, we have

$$
\mathrm{Vol} (\mathcal {M} _ {0, 4}) = 2 \pi^ {2}
$$

and

$$
\int_ {\overline {{\mathcal {M}}} _ {0, 4}} \psi_ {1} = 1.
$$

Also, it can be shown that

$$
V _ {2, 1} (b _ {1}) = \frac {(4 \pi^ {2} + b _ {1} ^ {2}) \cdot (1 2 \pi^ {2} + b _ {1} ^ {2}) \cdot (6 9 6 0 \pi^ {2} + 3 8 4 \pi^ {2} b _ {1} ^ {2} + 5 b _ {1} ^ {4})}{2 2 1 1 8 4 0},
$$

which implies that

$$
\int_ {\overline {{\mathcal {M}}} _ {2, 1}} \psi_ {1} ^ {4} = \frac {2 ^ {4} \cdot 4 ! \cdot 5}{2 2 1 1 8 4 0} = \frac {1}{2 4 ^ {2} \cdot 2}.
$$

Remark. It is known [11] that, in general,

$$
\int_ {\overline {{\mathcal {M}}} _ {g, 1}} \psi_ {1} ^ {3 g - 2} = \frac {1}{2 4 ^ {g} \cdot g !}.
$$

A closed formula for$V _ { 0 , n } ( 0 )$, the Weil-Petersson volume of$\mathcal { M } _ { 0 , n }$, is known [34]. Also see [17], [26], and [12] for diferent results on Weil-Petersson volumes. Note that there is a small diference in the normalization of the volume form; in [34] the Weil-Petersson Kähler form is$1 / 2$the imaginary part of the Weil-Petersson pairing, while here the factor$1 / 2$does not appear. So our answers are diferent by a power of 2.

There is an exceptional case which arises for$g = n = 1$. In this case a generic $X \in \mathcal { M } _ { 1 , 1 }$has a symmetry of order 2 which acts nontrivially on the cotangent space of$X$at the marked point. See [28]. Therefore, the integral of$\psi _ { 1 }$is half of what equation (1.1) predicts. In$\ S 5$, we show that

$$
V _ {1, 1} (b) = b ^ {2} / 2 4 + \pi^ {2} / 6.
$$

Hence, we get

$$
\mathrm{Vol} (\mathcal {M} _ {1, 1}) = \pi^ {2} / 6
$$

and

$$
\int_ {\overline {{\mathcal {M}}} _ {1, 1}} \psi_ {1} = \frac {1}{2} \times \frac {1}{1 2} = \frac {1}{2 4},
$$

which agree with the known results [9].

The main result. By combining equation (1.1) and the recursive formula for the$V _ { g , n } ( b ) \mathrm { { s } }$obtained in [22], we prove that the generating function for all top intersections of$\psi$classes in all genera satisfies the Virasoro constraints (§6).

Analogies with moduli spaces of stable bundles. The discussion above suggests some similarities between${ \mathcal { M } } _ { g , n }$and the variety$\mathrm { H o m } ( \pi _ { 1 } ( S ) , G ) / G$ of representations of the fundamental group of the oriented surface S in a compact Lie group G, up to conjugacy. This space is naturally equipped with a symplectic structure [6]. For$G = \mathrm { S U } ( 2 )$, the representation variety is identified with the moduli space of semi-stable holomorphic rank 2 vector bundles over a fixed Riemann surface.

$$
\theta_ {1}, \dots , \theta_ {n} \in G
$$

$$
R _ {g, n} (\theta_ {1}, \dots , \theta_ {n})
$$

be the variety of representations of$\pi _ { 1 } ( S _ { g , n } )$in$S U ( 2 )$such that the monodromy around$\beta _ { i }$lies in the conjugacy class of$\theta _ { i }$. Here, fixing the conjugacy class of the monodromy around a boundary component$\beta$corresponds to fixing the length of$\beta$ in the case of${ \mathcal { M } } _ { g , n } ( b )$.

As in our argument for proving Theorem 6.1, it is possible to derive recursive formulas for intersection numbers of line bundles on$R _ { g , n }$by relating these numbers to the symplectic volume of$R _ { g , n } ( \theta _ { 1 } , \ldots , \theta _ { n } )$. This approach was first suggested by Witten [29], and also used in [27]

An important diference is that the action of the mapping class does not enter in the$R _ { g , n }$case. The space$R _ { g , n }$is analogous to Teichmüller space, but it has finite volume. Also, the action of the mapping class group on$R _ { g , n } ( \theta )$is ergodic [7].

## 2. Background material

In this section, we briefly summarize basic background material in the Teichmüller theory of Riemann surfaces with geodesic boundary components. For further background, see [10] and [4].

Teichmüller space. Let$S$be an oriented smooth surface of negative Euler characteristic. A point in the Teichmüller space$\boldsymbol { \mathcal { T } } ( \boldsymbol { S } )$is a complete hyperbolic surface X equipped with a diffeomorphism$f : S \to X$. The map$f$ provides a marking on X by$S$. Two marked surfaces$f : S \to X$and$g : S  Y$define the same point in $\mathcal { T } ( S )$if and only if$f \circ g ^ { - 1 } : Y \to X$is isotopic to a conformal map. When ∂S is nonempty, consider hyperbolic Riemann surfaces homeomorphic to S with geodesic boundary components of fixed length. Let$A = \partial S$and$b = ( b _ { \alpha } ) _ { \alpha \in A } \in \mathbb { R } _ { + } ^ { | A | }$. A point $X \in \mathcal { T } ( S , b )$is a marked hyperbolic surface with geodesic boundary components such that for each boundary component$\beta \in \partial S$, we have

$$
\ell_ {\beta} (X) = b _ {\beta}.
$$

Let$S _ { g , n }$be an oriented smooth connected surface of genus g with n boundary components$( \beta _ { 1 } , \ldots , \beta _ { n } )$). Then the Teichmüller space of hyperbolic structures on $S _ { g , n }$with geodesic boundary components of length$b _ { 1 } , \ldots , b _ { n }$is defined by

$$
\mathcal {T} _ {g, n} (b _ {1}, \dots , b _ {n}) = \mathcal {T} (S _ {g, n}, b _ {1}, \dots , b _ {n}).
$$

Let$\operatorname { M o d } ( S )$denote the mapping class group of$S$, or the group of isotopy classes of orientation-preserving self-homeomorphisms of S leaving each boundary component setwise fixed. The mapping class group$\mathrm { M o d } _ { g , n } = \mathrm { M o d } ( S _ { g , n } )$acts on$\mathcal { T } _ { g , n } ( b )$by changing the marking. The quotient space

$$
\mathcal {M} _ {g, n} (b) = \mathcal {M} (S _ {g, n}, \ell_ {\beta_ {i}} = b _ {i}) = \mathcal {T} _ {g, n} (b _ {1}, \ldots , b _ {n}) / \mathrm{Mod} _ {g, n}
$$

is the moduli space of Riemann surfaces homeomorphic to$S _ { g , n }$with n boundary components of length$\ell _ { \beta _ { i } } = b _ { i }$. By convention, a geodesic of length zero is a cusp, and we have

$$
\mathcal {T} _ {g, n} = \mathcal {T} _ {g, n} (0, \dots , 0)
$$

and

$$
\mathcal {M} _ {g, n} = \mathcal {M} _ {g, n} (0, \dots , 0).
$$

For a disconnected surface$S = \bigcup _ { i = 1 } ^ { k } S _ { i }$such that$A _ { i } = \partial S _ { i } \subset \partial S$, we have

$$
\mathcal {M} (S, b) = \prod_ {i = 1} ^ {k} \mathcal {M} (S _ {i}, b _ {A _ {i}}),
$$

where$b _ { A _ { i } } = ( b _ { s } ) _ { s \in A _ { i } }$

The Weil-Petersson symplectic form. Recall that a symplectic form on a manifold M is a nondegenerate closed 2-form$\omega \in \Omega ^ { 2 } ( M )$. The n-fold wedge product

$$
\frac {1}{n !} \omega \wedge \dots \wedge \omega
$$

never vanishes, and defines a volume form on M. By work of Goldman [6], the space ${ \mathcal { T } } _ { g , n } ( b _ { 1 } , \ldots , b _ { n } )$carries a natural symplectic form invariant under the action of the mapping class group. This symplectic form is called the Weil-Petersson symplectic form, and denoted by ω or$\omega _ { w p }$. We investigate the volume of the moduli space with respect to the volume form induced by the Weil-Petersson symplectic form. If S is disconnected, then

$$
\operatorname{Vol} (\mathcal {M} (S, b)) = \prod_ {i = 1} ^ {k} \operatorname{Vol} (\mathcal {M} (S _ {i}, b _ {A _ {i}})).
$$

When$L = 0$, there is a natural complex structure on$\mathcal { T } _ { g , n } .$, and this symplectic form is in fact the Kähler form of a Kähler metric [10].

The Fenchel-Nielsen coordinates. A pants decomposition of S is a set of disjoint simple closed curves which decomposes the surface into pairs of pants. Fix a system of pants decomposition of$S _ { g , n }$, $\mathcal { P } = \{ \alpha _ { i } \} _ { i = 1 } ^ { k }$, where$k = 3 g - 3 + n$. For a marked hyperbolic surface$X \in \mathcal { T } _ { g , n } ( b )$, the Fenchel-Nielsen coordinates associated with $\mathcal { P } , \ \{ \ell _ { \alpha _ { 1 } } ( X ) , \ldots , \ell _ { \alpha _ { k } } ( X ) , \tau _ { \alpha _ { 1 } } ^ { \cdots } ( X ) , \ldots , \tau _ { \alpha _ { k } } ( X ) \}$, consist of the set of lengths of all geodesics used in the decomposition and the set of the twisting parameters used to glue the pieces [10]. There is an isomorphism

$$
\mathcal {T} _ {g, n} (b) \cong \mathbb {R} _ {+} ^ {\mathcal {P}} \times \mathbb {R} ^ {\mathcal {P}}
$$

by the map

$$
X \to (\ell_ {\alpha_ {i}} (X), \tau_ {\alpha_ {i}} (X)) _ {i = 1} ^ {k}.
$$

By work of Wolpert, the Weil-Petersson symplectic structure has a simple form in Fenchel-Nielsen coordinates [30].

Theorem 2.1 (Wolpert). The Weil-Petersson symplectic form is given by

$$
\omega_ {w p} = \sum_ {i = 1} ^ {k} d \ell_ {\alpha_ {i}} \wedge d \tau_ {\alpha_ {i}}.
$$

Twisting. Given a simple closed geodesic α on$X \in \mathcal { T } _ { g , n } ( b )$, and$t \in \mathbb { R }$, we can deform the hyperbolic structure of X by a right twist along α as follows. First, cut X along α, and then reglue back after twisting distance t to the right. We observe that the hyperbolic structure of the complement of the cut extends to a new hyperbolic structure$\operatorname { t w } _ { t \alpha } ( X )$on S. The resulting continuous path in Teichmüller space is the Fenchel-Nielsen deformation of X along α which is generated by the Fenchel-Nielsen vector field. For$t = \ell _ { \alpha } ( X )$), we have

$$
\mathrm{tw} _ {t \alpha} (X) = \phi_ {\alpha} (X),
$$

where$\phi _ { \alpha } \in \operatorname { M o d } ( S _ { g , n } )$is a right Dehn twist along α. It is known that the vector field generated by twisting around α is symplectically dual to the exact 1-form$d \ell _ { \alpha }$; as a consequence of Theorem 2.1 [30], we have

Corollary 2.2. The right twist flow defined by

$$
t \to \mathrm{tw} _ {t \alpha} (X)
$$

is the Hamiltonian flow ofthe length function ofα with respect to the Weil-Petersson symplectic form.

Compactification of the moduli space. The Deligne-Mumford compactification${ \overline { { \mathcal { M } } } } _ { g , n }$of the moduli space$\mathcal { M } _ { g , n } \left[ 9 \right]$can be constructed by adjoining hyperbolic surfaces with simple closed geodesics of length zero.

By work of Wolpert [33], the Weil-Petersson symplectic form extends smoothly to the boundary with respect to the Fenchel-Nielsen coordinates. This form is closed and everywhere nondegenerate and therefore defines a symplectic form on ${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$. In [32] Wolpert showed that$\omega / \pi ^ { 2 } \in H ^ { 2 } ( \overline { { \mathcal { M } } } _ { g , n } , \mathbb { Q } )$, and by multiplying $[ \omega ] / \pi ^ { 2 }$by some integer, we get a positive line bundle over${ \overline { { \mathcal { M } } } } _ { g , n }$. As a result,${ \overline { { \mathcal { M } } } } _ { g , n }$ is a projective algebraic variety. See [32] for more details.

In a similar way, we can compactify the space$\mathcal { M } _ { g , n } ( b )$by allowing$\ell _ { \gamma } = 0$for a simple closed geodesic$\gamma$inside the surface. When$b \neq 0$, the moduli space${ \mathcal { M } } _ { g , n } ( b )$ does not have a natural complex structure. Nevertheless it has a real-analytic structure induced by the Fenchel-Nielsen coordinates [33]. As was pointed out to the author by the referee, the approach of describing stable nodal curves in terms of hyperbolic surfaces first appeared in a paper by Bers [2].

Orbifold structure of the moduli space. Since the action of the mapping class group on Teichmüller space can have fixed points, the space$\mathcal { M } _ { g , n } ( b )$is not always a manifold. But a complete hyperbolic surface can only have finitely many automorphisms. So the moduli space has a natural orbifold structure. The orbifold points of the moduli space correspond exactly to the Riemann surfaces where the automorphism group is nontrivial. We remark that a Riemann surface$X \in \mathcal { M } _ { 0 , n }$ does not have nontrivial automorphisms. Therefore, the moduli space$\mathcal { M } _ { 0 , n }$is a manifold. In general, the moduli space${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$is a compact orbifold, and the Deligne-Mumford compactification locus,$\overline { { \mathcal { M } } } _ { g , n } ( b ) - \mathcal { M } _ { g , n } ( b )$, is a union of finitely many lower-dimensional suborbifolds intersecting transversely [9].

To apply results known for manifolds in our setting (e.g. Corollary 3.3), it sufices to show that${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$has a finite cover with no orbifold points; the finite cover can be chosen as

$$
\mathcal {T} _ {g, n} (b) / H,
$$

where H is a torsion-free subgroup of$\operatorname { M o d } _ { g , n }$

More precisely, each finite quotient group G of the mapping class group determines a Galois cover$\mathcal { M } _ { g , n } ( b ) [ G ] \to \mathcal { M } _ { g , n } ( b )$, and as proved in [16] and [3], we have

Theorem 2.3. There exists a finite group G such that${ \overline { { \mathcal { M } } } } _ { g , n } ( b ) [ G ]$is a smooth manifold, and the compactification locus is a union of codimension-2 submanifolds.

This theorem allows us to use results of the next section on symplectic reduction and apply them to the moduli spaces of curves.

Coverings and volume forms of the$\mathcal { M } _ { g , n } ( b )$'s. Let$\gamma _ { 1 } , \gamma _ { 2 } , \ldots \gamma _ { k }$be a set of disjoint simple closed curves on$S _ { g , n }$, and$\Gamma = \left( \gamma _ { 1 } , \dots , \gamma _ { k } \right)$. Then$g \in { \mathrm { M o d } } _ { g , n }$acts on Γ by

$$
g \cdot \Gamma = (g \cdot \gamma_ {1}, \dots , g \cdot \gamma_ {k}).
$$

Let$\mathcal { O } _ { \Gamma }$be the set of homotopy classes of elements of the set Mod ·Γ. Consider $\mathcal { M } _ { g , n } ( b ) ^ { \mathrm { I } }$defined by the following space of pairs:

$\{ ( \boldsymbol { X } , \boldsymbol { \eta } ) | \boldsymbol { X } \in \mathcal { M } _ { g , n } ( { \boldsymbol { b } } ) \ , \ \boldsymbol { \eta } = ( \eta _ { 1 } , \ldots , \eta _ { k } ) \in \mathcal { O } _ { \Gamma } , \eta _ { i } \mathrm { \mathrm { ' s } }$are closed geodesics on$X \}$

Let$\pi ^ { \Gamma } : { \mathcal { M } } _ { g , n } ( b ) ^ { \Gamma } \to { \mathcal { M } } _ { g , n } ( b )$be the projection map defined by

$$
\pi^ {\Gamma} (X, \eta) = X.
$$

Then we have

$$
\mathcal {M} _ {g, n} (b) ^ {\Gamma} = \mathcal {T} _ {g, n} (b) / G _ {\Gamma},
$$

where

$$
G _ {\Gamma} = \bigcap_ {i = 1} ^ {s} \operatorname{Stab} (\gamma_ {i}) \subset \operatorname{Mod} (S _ {g, n}).
$$

The Weil-Petersson symplectic structure on Teichmüller space is invariant under the action of the mapping class group. Hence$\mathcal { M } _ { g , n } ( b ) ^ { \Gamma }$carries a symplectic structure defined by$\pi ^ { \Gamma * } ( \omega _ { w p } )$

## 3. Symplectic reduction

In this section we recall some definitions and known results about symplectic geometry of symplectic quotients [13] and Chern-Weil theory of principal circle bundles [21]. For an interesting exposition of general ideas surrounding symplectic quotients and some applications see [8].

3.1. Principal$S ^ { 1 }$-bundles. Let$P$and M be smooth manifolds, and$\pi : P  M$ be a map of$P$onto M. If there is an$S ^ { 1 }$action on$P _ { : }$then we say$( P , S ^ { 1 } , M )$is a Principal$S ^ { 1 }$-bundle if

(1)$S ^ { 1 }$acts freely on$P ;$

(2)$\pi ( p _ { 1 } ) = \pi ( p _ { 2 } )$if and only if there exists$g \in S ^ { 1 }$such that$p _ { 1 } \cdot g = p _ { 2 } ;$

(3)$P$is locally trivial over M.

A connection on a principal$S ^ { 1 }$-bundle is a smooth distribution H on P such that

(1)$T _ { p } P = H _ { p } \oplus V _ { p } , V _ { p } = \ker \pi _ { * }$, and

(2)$g ^ { * } H _ { p } = H _ { p \cdot g }$

Vectors in$H _ { p }$are called horizontal. For$v \in T _ { p } P ,$we denote the horizontal part by Hv. A connection is uniquely determined by an invariant 1-form A such that $A ( X ) = 1$, where X is the vector field generating the$S ^ { 1 }$action. We can choose the 1-form defined by

$$
A (v) = \frac {\langle v , X \rangle}{\langle X , X \rangle},
$$

where - ,  is an$S ^ { 1 }$-invariant metric on$P$.

Given a p-form ω on$P$, define$D \omega$by

$$
D \omega (v _ {1}, \dots , v _ {p + 1}) = d \omega (H v _ {1}, \dots , H v _ {p + 1}).
$$

If A is the connection form of$H , \Phi = D ( A )$is called the curvature form of$H$ Then the following result holds.

Lemma 3.1. There exists a unique closed 2-form Ω on M such that$\Phi = \pi ^ { * } \Omega$ Moreover, the cohomology class of Ω is independent of the choice of the connection form, and

$$
c _ {1} (P) = [ \Omega ] \in H ^ {2} (M, \mathbb {Z}).
$$

See [19] and [21] for more details.

3.2. Moment map. Let$( M , \omega )$be a symplectic manifold. The Hamiltonian vector field$\xi _ { H }$generated by the function$H : M \to \mathbb { R }$is the vector field determined by

$$
\omega (\xi_ {H},.) = d H (.)
$$

Suppose that a compact Lie group G with Lie algebra$g$acts smoothly on M and preserves the symplectic form$\omega .$. This action gives rise to an infinitesimal action of$g$associating to every$\xi \in g$a vector field$\xi ^ { \# }$. The moment map$\mu : M \to g ^ { * }$is defined by

$$
d \mu (Y) (X) = \omega (X ^ {\#}, Y),
$$

where$Y$is a vector field on M. In other words, the map$\mu _ { \xi } : M \to \mathbb { R }$defined so that

$$
\mu_ {\xi} (m) = \mu (m) \cdot \xi
$$

is a Hamiltonian function for the vector field on M induced by ξ. Assume that the map$\mu$is proper. Because the moment map$\mu$is G-invariant, G acts on each level set of$\mu$. The reduced space is the quotient

$$
M _ {a} = \mu^ {- 1} (a) / G
$$

for any$a = ( a _ { 1 } , \ldots , a _ { n } )$in the image of$\mu .$The space$M _ { a }$inherits a symplectic form$\omega _ { a }$from the symplectic structure on M.

Remark. If 0 is a regular value of$\mu ,$by the coisotropic embedding theorem there is a neighborhood of$\mu ^ { - 1 } ( 0 )$on which the symplectic form is given in a standard form [8]. This is a generalization of Darboux’s theorem stating that symplectic manifolds do not have any local invariants ([19]).

3.3. Variation of the reduced form and volume. When a is close to 0,$M _ { a }$is difeomorphic to$M _ { 0 }$. It is important to know how the symplectic geometry of$M _ { a }$ varies when one varies a.

When$G = T _ { n } = S _ { 1 } ^ { n }$, the action of G on the level set$\mu ^ { - 1 } ( a )$gives rise to n circle bundles,$\mathcal { C } _ { 1 } , \ldots , \mathcal { C } _ { n }$defined over$M _ { a }$

$$
\begin{array}{c} T ^ {n} \longrightarrow \mu^ {- 1} (a) \qquad \longrightarrow M \\ \Big \downarrow \\ M _ {a} = \mu^ {- 1} (a) / T ^ {n} \end{array}
$$

Fix a connection α on$\mu ^ { - 1 } ( 0 )$. Then the following result shows that$w _ { a }$varies linearly in a [8].

Theorem 3.2 (Normal form theorem). The space$( M _ { a } , w _ { a } )$is symplectomorphic to$M _ { 0 }$equipped with the symplectic form$w _ { 0 } + a \Omega$, where Ω is the curvature form of the connection α.

For$a = ( a _ { 1 } , \ldots , a _ { n } )$with$| a | \le \epsilon , M _ { a }$and$M _ { 0 }$are difeomorphic. Since$c _ { 1 } ( \mathcal { C } ) =$ [Ω], under this diffeomorphism the cohomology classes of the symplectic forms are related by

$$
[ w _ {a} ] = [ w ] + \sum_ {i = 1} ^ {n} a _ {i} \cdot [ \phi_ {i} ],
$$

where$\phi _ { i } = c _ { 1 } ( \mathcal { C } _ { i } )$

Remark. This theorem is closely related to a version of the Duistermaat-Heckman theorem asserting that the push-forward of the symplectic measure by the moment map for a torus action is a piecewise polynomial. For more details see [8].

Now by integrating the volume form induced by$\omega _ { a }$over the space$M _ { a } .$, we get:

Corollary 3.3. Let 0 be a regular value of the proper moment map$\mu : M \to \mathbb { R } ^ { n }$of the Hamiltonian action$o f T ^ { n }$on M. Then for suficiently small$\epsilon > 0$and$a \in \mathbb { R } _ { + } ^ { n }$ with$| a | \leq \epsilon$, the volume of$M _ { a } = \mu ^ { - 1 } ( a ) / T ^ { n }$is a polynomial in$a _ { 1 } , \ldots , a _ { n }$of degree $m = \dim ( M _ { a } ) / 2$, given by

$$
\sum_{\substack{\alpha \\ |\alpha |\leq m}}C(\alpha)\cdot a^{\alpha},
$$

where

$$
\alpha ! (m - | \alpha |)! C (\alpha) = \int_ {M _ {0}} \phi_ {1} ^ {\alpha_ {1}} \dots \phi_ {n} ^ {\alpha_ {n}} \cdot \omega^ {m - | \alpha |}.
$$

Here the exponent$\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ranges over elements in$\mathbb { Z } _ { > 0 } ^ { n } , a ^ { \alpha } = a _ { 1 } ^ { \alpha _ { 1 } } \cdot .$ $a _ { n } ^ { \alpha _ { n } } , | \alpha | = \sum _ { i = 1 } ^ { n } \alpha _ { i }$and$\alpha ! = \prod _ { i = 1 } ^ { n } \alpha _ { i } !$.

## 4. Volumes of moduli spaces of bordered Riemann surfaces

In this section we establish a relationship between the volume polynomials and intersection numbers of tautological classes over moduli space.

Collar curves. For any simple closed geodesic γ on a hyperbolic surface$X ,$there is a collar neighborhood of width

$$
\operatorname{arcsinh} \left(\frac {1}{\sinh (\ell_ {\gamma} (X) / 2)}\right)
$$

which is an embedded annulus. Moreover, two simple closed geodesics are disjoint if and only if their collars are disjoint [4]. Therefore, one can define a continuous function$F : \mathbb { R } _ { + } \longrightarrow \mathbb { R } _ { + }$such that

• for each boundary component$\beta _ { i }$of$X \in \mathcal { T } _ { g , n } ( b )$, there is a curve$\widetilde { \beta } _ { i }$of constant curvature of length$F ( \ell _ { \beta _ { i } } ( X ) )$inside the collar neighborhood of $\beta _ { i }$, and

$$
\bullet \lim _ {x \to 0} F (x) = 1 / 4.
$$

As$\ell _ { i } \to 0 , \widetilde { \beta } _ { i }$tends to a horocycle of length$1 / 4$around the corresponding puncture. When$\ell _ { \beta _ { i } } ( X ) > 0$, there is a canonical bijection between the points of$\widetilde { \beta } _ { i }$and$\beta _ { i }$.

Geometric circle bundles. The orientation on$S _ { g , n }$defines a canonical orientation on its boundary components as follows. Let$\beta _ { i }$be a boundary component of $X \in { \mathcal { T } } _ { g , n } ( b ) , x \in { \mathcal { \beta } } _ { i }$, and$N _ { x }$an outward vector normal to$\beta _ { i }$at x. Then we say a tangent vector$v _ { x }$to$\beta _ { i }$is positive if the pair$( v _ { x } , N _ { x } )$has positive orientation with respect to the orientation of$X$

Now let$\gamma _ { i } : [ 0 , b _ { i } ] \to \beta _ { i }$be an oriented arc length parametrization of$\beta _ { i }$. For any $t \in [ 0 , b _ { i } ]$define$\xi ^ { t } : \beta _ { i } \to \beta _ { i }$by

$$
\xi^ {t} (\gamma_ {i} (s)) = \gamma_ {i} (s + t \cdot b _ {i}).
$$

As$\xi ^ { t + 1 } = \xi ^ { t } , \xi$defines an$S ^ { 1 }$-action on$\beta _ { i }$

Let$\beta _ { i }$be a curve parallel to the boundary component$\beta _ { i }$ on$X \in \mathcal { T } _ { g , n } ( b )$. The advantage of using the parallel curve$\widetilde { \beta } _ { i }$instead of$\beta _ { i }$is that$\widetilde { \beta } _ { i }$has positive length even when the geodesic length of$\beta _ { i }$is zero; in this case${ \widetilde { \beta } } _ { i }$is a horocycle around the puncture$p _ { i }$. Otherwise, there is a canonical one-to-one map between$\widetilde { \beta } _ { i }$and $\beta _ { i }$. Note that when$i \neq j$, the curve$\widetilde { \beta } _ { i }$is disjoint from${ \widetilde { \beta } } _ { j }$. For a fixed$b = ( b _ { 1 } , \ldots , b _ { n } )$, define the space$S _ { i } ( \mathcal { T } _ { g , n } ( b ) )$by

$$
\mathcal {S} _ {i} \left(\mathcal {T} _ {g, n} (b)\right) = \left\{\left(X, p\right) \mid p \in \widetilde {\beta} _ {i}, X \in \mathcal {T} _ {g, n} (b) \right\}\rightarrow \mathcal {T} _ {g, n} (b).
$$

There is a natural action of${ \mathrm { M o d } } _ { g , n }$on$S _ { i } ( \mathcal { T } _ { g , n } ( b ) )$. Since the stabilizer of every point is finite, the quotient space$S _ { i } ( \mathcal { M } _ { g , n } ( b ) )$is a circle bundle over$\mathcal { M } _ { g , n } ( b )$in the orbifold sense. Also, this circle bundle can be extended to$X \in \overline { { \mathcal { M } _ { g , n } } } ( b )$where the length of some simple closed geodesic inside the surface can be zero. It is essential that the parallel curve${ \widetilde { \beta } } _ { i }$is always disjoint from the possible singular points of$X \in \overline { { \mathcal { M } } } _ { g , n } ( b )$. Therefore, we have

Lemma 4.1. For any$1 \leq i \leq n$and$b \in ( \mathbb { R } _ { + } ) ^ { n } , ( S _ { i } ( b ) , S ^ { 1 } , \overline { { \mathcal { M } } } _ { g , n } ( b ) )$is a principal circle bundle over${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$in the orbifold sense.

Tautological classes. Next we consider the case where the lengths of all boundary components are zero. Since${ \overline { { \mathcal { M } } } } _ { g , n }$is an orbifold, the first Chern class of the circle bundle$s _ { i }$defines an element of the cohomology class of the moduli space

$$
\left[ c _ {1} \left(\mathcal {S} _ {i}\right) \right] \in H ^ {2} \left(\overline {{\mathcal {M}}} _ {g, n}, \mathbb {Q}\right).
$$

We will relate the first Chern class of$s _ { i }$to the tautological class

$$
\psi_ {i} = c _ {1} (\mathcal {L} _ {i}).
$$

Recall that every finite hyperbolic surface defines a complex 1-manifold via its uniformization. Namely, for$X \in \mathcal { T } _ { g , n }$there is a unique compact complex curve$C$ and finitely many points$p _ { 1 } , \ldots , p _ { n }$on$C$such that X is conformally equivalent to $C - \{ p _ { 1 } , \ldots , p _ { n } \}$

Also, each cusp neighborhood of X is conformally equivalent to a punctured disk $\Delta - \{ 0 \} \subset \mathbb { C } \ [ 4 ]$. Consider the parallel curve${ \widetilde { \beta } } _ { i }$around the puncture$p _ { i }$. Then each element of the tangent space of$X$at$p _ { i }$corresponds to a point of${ \widetilde { \beta } } _ { i }$. However, the orientation on${ \widetilde { \beta } } _ { i }$defined earlier in this section is diferent from the one induced by the orientation on tangent vectors at$p _ { i }$

On the other hand, as$\mathcal { L } _ { i }$is a complex line bundle, the underlying real vector bundle has a canonical orientation. Therefore the duality between the tangent and cotangent spaces at$p _ { i }$gives rise to an orientation-reversing isomorphism between the circle bundle corresponding to the line bundle$\mathcal { L } _ { i }$and the circle bundle$S _ { i }$with reverse orientation.

Therefore, we can establish the following result.

Theorem 4.2. For any$1 \leq i \leq n$, we have

$$
[ c _ {1} (\mathcal {S} _ {i}) ] = [ \psi_ {i} ] \in H ^ {2} (\overline {{\mathcal {M}}} _ {g, n}, \mathbb {Q}),
$$

where$\psi _ { i }$is the ith tautological class over${ \overline { { \mathcal { M } } } } _ { g , n }$

Remark. Henceforth, we only deal with the circle bundle$s _ { i }$and forget about the complex structure of$\mathcal { L } _ { i }$. Later, we will use the Chern-Weil description of characteristic classes in terms of the curvature form for calculating the intersection numbers. See Appendix C of [21] for more details.

Moduli space of bordered Riemann surfaces. Consider the moduli spaces of bordered Riemann surfaces with marked points (without fixing the lengths of the boundary components) defined by

$$
\widehat {\mathcal {M} _ {g , n}} = \left\{\left(X, p _ {1}, \dots , p _ {n}\right) \mid p _ {i} \in \widetilde {\beta} _ {i}, X \in \overline {{\mathcal {M}}} _ {g, n} \left(b _ {1}, \dots , b _ {n}\right), b _ {i} > 0 \right\}.
$$

Define the map$\widehat { \ell : \widehat { \mathcal { M } _ { g , n } } } \to \mathbb { R } _ { + } ^ { n }$by

$$
\ell (X, p _ {1}, \dots , p _ {n}) = (\ell_ {\beta_ {1}} (X), \dots , \ell_ {\beta_ {n}} (X)).
$$

There is a natural action of$T ^ { n } = S _ { 1 } ^ { n }$on the space$\widehat { \mathcal { M } _ { g , n } }$as follows. For each $1 \leq i \leq n , S _ { 1 } ^ { i }$acts by moving$p _ { i }$on the curve${ \widetilde { \beta } } _ { i }$, that is,

$$
\xi_ {i} ^ {t} (X, p _ {1}, \dots , p _ {n}) = (X, p _ {1}, \dots , \xi^ {t} (p _ {i}), \dots , p _ {n}).
$$

The goal of this part is to show that this$T ^ { n }$action is the Hamiltonian flow of the function$\ell ^ { 2 } / 2$with respect to the symplectic form on$\widehat { \mathcal { M } _ { g , n } }$induced by the Weil-Petersson form.

Extension of the Weil-Petersson symplectic form to${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$. As we mentioned in$\ S 2 .$, the moduli space${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$has a natural real analytic structure arising from the Fenchel-Nielsen coordinates [33].

By work of Wolpert [33], the Weil-Petersson symplectic form has a smooth extension$\omega ^ { F N }$to${ \overline { { \mathcal { M } } } } _ { g , n } ( b )$(§2). Using the extension of the Weil-Petersson symplectic form, we can define a$T ^ { n }$-invariant symplectic form on$\widehat { \mathcal { M } _ { g , n } }$

Remark. There is a diferent method for extending the Weil-Petersson symplectic form to${ \overline { { \mathcal { M } } } } _ { g , n }$by using a closed current$\omega ^ { C }$relative to the complex structure of ${ \mathcal { M } } _ { g , n }$. In [33], Wolpert showed that$\omega ^ { F N }$and$\omega ^ { C }$determine the same cohomology class. We remark that the complex structure and the Fenchel-Nielsen coordinates do not induce the same smooth structure on${ \overline { { \mathcal { M } } } } _ { g , n }$

Theorem 4.3. The orbifold$\widehat { \mathcal { M } _ { g , n } }$has a natural$T ^ { n }$-invariant symplectic structure such that

(1) the map

$$
\ell^ {2} / 2 = (\ell_ {\beta_ {1}} (X) ^ {2} / 2, \dots , \ell_ {\beta_ {n}} (X) ^ {2} / 2)
$$

is the moment map for the action of$T ^ { n }$on$\widehat { \mathcal { M } _ { g , n } }$, and

(2) the canonical map

$$
s: \ell^ {- 1} (b _ {1}, \dots , b _ {n}) / T \to \overline {{\mathcal {M}}} _ {g, n} (b _ {1}, \dots , b _ {n})
$$

is a symplectomorphism.

Proof. Let$S _ { g , 2 n }$be a surface of genus g with 2n boundary components$\beta _ { 1 } , \ldots , \beta _ { 2 n }$ Fix n simple closed curves$\gamma _ { 1 } , \ldots , \gamma _ { n }$on$S _ { g , 2 n }$such that$\gamma _ { i }$bounds a pair of pants with$\beta _ { 2 i - 1 }$and$\beta _ { 2 i }$, and let$\Gamma = \left( \gamma _ { 1 } , \dots , \gamma _ { n } \right)$. Consider$\overline { { \mathcal { M } _ { g , 2 n } } } ^ { \Gamma }$defined by

$\{ ( X , \eta ) | X \in \overline { { \mathcal { M } } } _ { g , 2 n } \ , \ \eta = ( \eta _ { 1 } , \ldots , \eta _ { n } ) \in \mathcal { O } _ { \Gamma } , \eta _ { i }$’s are closed geodesics on$X \}$

where$\mathcal { O } _ { \Gamma }$is the set of homotopy classes of elements of the set${ \mathrm { M o d } } _ { g , 2 n } \cdot { \Gamma } .$. Note that by Wolpert’s result, the symplectic form induced by the Weil-Petersson form on$\mathcal { M } _ { g , 2 n } ^ { \Gamma }$extends to$\overline { { \mathcal { M } _ { g , 2 n } } } ^ { \Gamma } \left( \ S 2 \right)$. To prove the theorem, we study how$\overline { { \mathcal { M } _ { g , 2 n } } } ^ { \Gamma }$ and${ \widehat { \mathcal { M } } } _ { g , n } ^ { - }$are related.

Note that there are two canonical points on each boundary component α of a pair of pants; these points are the end points of the length-minimizing geodesics connecting α to the other two boundaries of$\Sigma$.

Fix$( X , p _ { 1 } , \dotsc , p _ { n } ) \in { \widehat { \mathcal { M } } } _ { g , n }$with geodesic boundary components$\gamma _ { 1 } , \ldots , \gamma _ { n }$. First we construct a surface$Y \in \mathcal { M } _ { g , 2 n }$by gluing n pairs of pants$\Sigma _ { 1 } , \ldots , \Sigma _ { n }$with boundary lengths$( \ell _ { \gamma _ { i } } ( X ) , 0 , 0 )$to boundary components of$X$; we glue$\Sigma _ { i }$to$\gamma _ { i }$ such that the point$p _ { i }$on$\gamma _ { i }$is adjacent to the canonical point on the boundary of $\Sigma _ { i }$corresponding to$\beta _ { 2 i - 1 }$

Therefore, we get a map

$$
f: \widehat {\mathcal {M} _ {g , n}} \to \overline {{\mathcal {M} _ {g , 2 n}}} ^ {\Gamma},
$$

defined by

$$
f (X, p _ {1}, \dots , p _ {n}) = (Y, (\gamma_ {1}, \dots , \gamma_ {n})).
$$

It is easy to check that the map$f$defines a symplectic form on$\widehat { \mathcal { M } _ { g , n } }$. By Corollary 2.2, the symplectic form induced by$f$on$\widehat { \mathcal { M } _ { g , n } }$satisfies both conditions in the statement of the theorem.

We remark that the extension of this symplectic form to$\overline { { \mathcal { M } } } _ { g , n } ( 0 , \ldots , 0 )$is just the Weil-Petersson symplectic form.

Now we can establish the main result of this section.

Theorem 4.4. The coeficients of the volume polynomial

$$
\operatorname{Vol} (\mathcal {M} _ {g, n} (b _ {1}, \ldots , b _ {n})) = \sum_ {| \alpha | \leq 3 g - 3 + n} C _ {g} (\alpha) \cdot b ^ {2 \alpha}
$$

are given by

$$
C _ {g} (\alpha_ {1}, \dots , \alpha_ {n}) = \frac {2 ^ {m (g , n) | \alpha |}}{2 ^ {| \alpha |} | \alpha | ! (3 g - 3 + n - | \alpha |) !} \int_ {\overline {{\mathcal {M}}} _ {g, n}} \psi_ {1} ^ {\alpha_ {1}} \dots \psi_ {n} ^ {\alpha_ {n}} \cdot \omega^ {3 g - 3 + n - | \alpha |},
$$

where$\psi _ { i }$is the first Chern class of the$_ { i - t h }$tautological line bundle and ω is the Weil-Petersson symplectic form. Here$\begin{array} { r } { m ( g , n ) = \delta ( g - 1 ) \times \delta ( n - 1 ) , \alpha ! = \prod _ { i = 1 } ^ { n } \alpha _ { i } ! } \end{array}$ and$\textstyle | { \boldsymbol { \alpha } } | = \sum _ { i = 1 } ^ { n } \alpha _ { i }$

Sketch of the proof. By Theorem 2.3, we can assume that the moduli space is a manifold. Fix$\epsilon _ { 1 } , \ldots , \epsilon _ { n } > 0$. By applying Theorem 3.3 to$\widehat { \mathcal { M } _ { g , n } }$with$\mu = \ell ^ { 2 } / 2$, we obtain a formula for$\operatorname { V o l } ( \mathcal { M } _ { g , n } ( b _ { 1 } , \dots , b _ { n } ) )$) in terms of

$$
\int_ {\overline {{\mathcal {M}}} _ {g, n} (\epsilon_ {1}, \ldots , \epsilon_ {n})} (c _ {1} (\mathcal {S} _ {1})) ^ {\alpha_ {1}} \dots (c _ {1} (\mathcal {S} _ {n})) ^ {\alpha_ {n}} \cdot \omega^ {3 g - 3 + n - | \alpha |}.
$$

We remark that by Lemma 4.1, each$s _ { i }$is a circle bundle over$\overline { { \mathcal { M } } } _ { g , n } ( \epsilon _ { 1 } , \ldots , \epsilon _ { n } )$ Consider the extension of the circle bundle$s _ { i }$to${ \overline { { \mathcal { M } } } } _ { g , n }$. Since$[ c _ { 1 } ( S _ { i } ) ] = [ \psi _ { i } ]$on ${ \overline { { \mathcal { M } } } } _ { g , n } .$we get the result by taking the limit as$\epsilon _ { i } \to 0$. See the introduction for the exceptional case when$g = n = 1$

## 5. A recursive formula for Weil-Petersson volumes

In this section we state a recursive formula for the$V _ { g , n } ( b )$’s obtained in [22]. This recursive formula (equation (5.5)) relates the volume polynomial$V _ { g , n } ( L )$to the volume polynomials of the moduli spaces of Riemann surfaces that we get by cutting one pair of pants from$S _ { g , n }$

An identity for the lengths of simple closed geodesics. Our point of departure for calculating these volume polynomials is an identity [20] for the lengths of simple closed geodesics on a punctured hyperbolic Riemann surface.

Theorem 5.1 (Generalized McShane identity for bordered surfaces). For any$X \in$ ${ \mathcal { T } } _ { g , n } ( b _ { 1 } , \ldots , b _ { n } )$with$3 g - 3 + n > 0$, we have

$$
\sum_ {(\alpha_ {1}, \alpha_ {2})} \mathcal {D} (b _ {1}, \ell_ {\alpha_ {1}} (X), \ell_ {\alpha_ {2}} (X)) + \sum_ {i = 2} ^ {n} \sum_ {\gamma} \mathcal {R} (b _ {1}, b _ {i}, \ell_ {\gamma} (X)) = b _ {1}.\tag{5.1}
$$

Here the first sum is over all unordered pairs of simple closed geodesics$\left( \alpha _ { 1 } , \alpha _ { 2 } \right)$ bounding a pair of pants with boundary component$\beta _ { 1 }$, and the second sum is over simple closed geodesics$\gamma$bounding a pair of pants with$\beta _ { 1 }$and$\beta _ { i }$.

The two functions$\mathcal { D } , \mathcal { R } : \mathbb { R } ^ { 3 } \to \mathbb { R } _ { + }$are defined by

$$
\mathcal {D} (x, y, z) = 2 \log \left(\frac {e ^ {\frac {x}{2}} + e ^ {\frac {y + z}{2}}}{e ^ {\frac {- x}{2}} + e ^ {\frac {y + z}{2}}}\right)
$$

and

$$
\mathcal {R} (x, y, z) = x - \log \left(\frac {\cosh (\frac {y}{2}) + \cosh (\frac {x + z}{2})}{\cosh (\frac {y}{2}) + \cosh (\frac {x - z}{2})}\right).
$$

Define$H : \mathbb { R } ^ { 2 } \to \mathbb { R }$by

$$
H (x, y) = \frac {1}{1 + e ^ {\frac {x + y}{2}}} + \frac {1}{1 + e ^ {\frac {x - y}{2}}}.\tag{5.2}
$$

It can be shown that

$$
\frac {\partial}{\partial x} \mathcal {D} (x, y, z) = H (y + z, x)\tag{5.3}
$$

and

$$
\frac {\partial}{\partial x} \mathcal {R} (x, y, z) = \frac {1}{2} (H (z, x + y) + H (z, x - y)).\tag{5.4}
$$

In order to calculate$V _ { g , n } ( b )$, we develop a method to integrate the generalized identity over certain coverings of$\mathcal { M } _ { g , n } ( b _ { 1 } , \ldots , b _ { n } )$[22].

Calculation of$V _ { 1 , 1 } ( b )$. We sketch the main idea of the calculation of the$V _ { g , n } ( b )$'s through an example when$g = n = 1$. In this case, Theorem 5.1 implies that for any$X \in \mathcal { T } ( S _ { 1 , 1 } , b )$, we have

$$
\sum_ {\gamma} \mathcal {D} (b, \ell_ {\gamma} (X), \ell_ {\gamma} (X)) = b,
$$

where the sum is over all nonperipheral simple closed curves on$S _ { 1 , 1 }$. From equation (5.3), the function$\mathcal { D }$ satisfies

$$
\frac {\partial}{\partial b} \mathcal {D} (b, x, x) = \frac {1}{1 + e ^ {x - \frac {b}{2}}} + \frac {1}{1 + e ^ {x + \frac {b}{2}}}.
$$

Using the method developed in [22] for integrating the left-hand side of the identity over$\mathcal { M } _ { 1 , 1 } ( b )$, we get

$$
b \cdot V _ {1, 1} (b) = \int_ {0} ^ {\infty} x \mathcal {D} (b, x, x) d x.
$$

So we have

$$
\frac {\partial}{\partial b} b \cdot V _ {1, 1} (b) = \int_ {0} ^ {\infty} x \cdot \left(\frac {1}{1 + e ^ {x + \frac {b}{2}}} + \frac {1}{1 + e ^ {x - \frac {b}{2}}}\right) d x.
$$

By setting$y _ { 1 } = x + b / 2$and$y _ { 2 } = x - b / 2$, we get

$$
\begin{array}{c} \int_ {0} ^ {\infty} x \cdot (\frac {1}{1 + e ^ {x + \frac {b}{2}}} + \frac {1}{1 + e ^ {x - \frac {b}{2}}}) d x = \int_ {b / 2} ^ {\infty} \frac {y _ {1} - b / 2}{1 + e ^ {y _ {1}}} d y _ {1} + \int_ {- b / 2} ^ {\infty} \frac {y _ {2} + b / 2}{1 + e ^ {y _ {2}}} d y _ {2} \\ = 2 \int_ {0} ^ {\infty} \frac {y}{1 + e ^ {y}} d y + \int_ {0} ^ {b / 2} \frac {y - b / 2}{1 + e ^ {y}} d y + \int_ {0} ^ {- b / 2} \frac {y + b / 2}{1 + e ^ {y}} d y \\ = \frac {\pi^ {2}}{6} + \int_ {0} ^ {b / 2} (y - b / 2) (\frac {1}{1 + e ^ {y}} + \frac {1}{1 + e ^ {- y}}) d y = \frac {\pi^ {2}}{6} + \frac {b ^ {2}}{8} \end{array}
$$

since we have

$$
\frac {1}{1 + e ^ {y}} + \frac {1}{1 + e ^ {- y}} = 1.
$$

As a result, we get

$$
V _ {1, 1} (b) = \frac {b ^ {2}}{2 4} + \frac {\pi^ {2}}{6}.
$$

Remark. This result agrees with the result obtained in [23].

Given a set A of positive numbers$A = \{ a _ { 1 } , \ldots , a _ { n } \}$, define$V _ { g , n } ( A )$by

$$
V _ {g, n} (A) = V _ {g, n} (a _ {1}, \ldots , a _ {n}).
$$

Statement of the recursive formula. In the simplest case when$n = 3$and$g = 0$, the moduli space$\mathcal { M } _ { 0 , 3 } ( b _ { 1 } , b _ { 2 } , b _ { 3 } )$consists of only one point, and by definition,

$$
V _ {0, 3} (b _ {1}, b _ {2}, b _ {3}) = 1.
$$

The function$V _ { g , n } ( b _ { 1 } , \ldots , b _ { n } )$for any$g$and n$( 2 g - 2 + n > 0 )$is determined recursively as follows.

• For any$b _ { 1 } , b _ { 2 } , b _ { 3 } \geq 0$, set

$$
V _ {0, 3} (b _ {1}, b _ {2}, b _ {3}) = 1
$$

and

$$
V _ {1, 1} (b _ {1}) = \frac {b _ {1} ^ {2}}{2 4} + \frac {\pi^ {2}}{6}.
$$

• For$b = ( b _ { 1 } , \ldots , b _ { n } )$, let$\widehat { b } = ( b _ { 2 } , \ldots , b _ { n } )$. When$( g , n ) \neq ( 1 , 1 ) , ( 0 , 3 )$, the volume$V _ { g , n } ( b ) = \mathrm { V o l } ( \mathcal { M } _ { g , n } ( b ) )$satisfies

$$
\frac {\partial}{\partial b _ {1}} b _ {1} V _ {g, n} (b) = \mathcal {A} _ {g, n} ^ {c o n} (b _ {1}, \widehat {b}) + \mathcal {A} _ {g, n} ^ {d c o n} (b _ {1}, \widehat {b}) + \mathcal {B} _ {g, n} (b _ {1}, \widehat {b}),\tag{5.5}
$$

where we have

$$
\mathcal {A} _ {g, n} ^ {c o n} (b _ {1}, \widehat {b}) = \frac {1}{2} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x y \widehat {\mathcal {A}} _ {g, n} ^ {c o n} (x, y, b _ {1}, \widehat {b}) d x d y,
$$

$$
\mathcal {A} _ {g, n} ^ {d c o n} (b _ {1}, \widehat {b}) = \frac {1}{2} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x y \widehat {\mathcal {A}} _ {g, n} ^ {d c o n} (x, y, b _ {1}, \widehat {b}) d x d y,
$$

and

$$
\mathcal {B} _ {g, n} (b _ {1}, \widehat {b}) = \int_ {0} ^ {\infty} x \widehat {\mathcal {B}} _ {g, n} (x, b _ {1}, \widehat {b}) d x.
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
\widehat {\mathcal {B}} _ {g, n}: \mathbb {R} _ {+} ^ {n + 1} \to \mathbb {R} _ {+}
$$

in terms of$V _ { h , m }$'s where$2 h + m < 2 g + n$. Let

$$
m (g, n) = \delta (g - 1) \times \delta (n - 1).
$$

Namely,$m ( g , n ) = 0$except for$g = n = 1$

I) : Definition of$\widehat { A } _ { g , n } ^ { c o n }$. Define$\widehat { A } _ { g , n } ^ { c o n } : \mathbb { R } _ { + } ^ { n + 2 } \longrightarrow \mathbb { R } _ { + }$by

$$
\widehat {\mathcal {A}} _ {g, n} ^ {c o n} (x, y, b _ {1}, \widehat {b}) = \frac {V _ {g - 1 , n + 1} (x , y , \widehat {b})}{2 ^ {m (g - 1 , n + 1)}} \cdot H (x + y, b _ {1}).
$$

The function H is defined by equation 5.2.

II) : Definition of$\widehat { A } _ { g , n } ^ { d c o n }$. Let$\mathcal { T } _ { g , n }$be the set of ordered pairs

$$
a = ((g _ {1}, I _ {1}), (g _ {2}, I _ {2})),
$$

where$I _ { 1 } , I _ { 2 } \subset \{ 2 , \ldots , n \}$and$0 \leq g _ { 1 } , g _ { 2 } \leq g$such that

(1) the two sets$I _ { 1 }$and$I _ { 2 }$are disjoint and$\{ 2 , 3 , \ldots , n \} = I _ { 1 } \cup I _ { 2 } ;$

(2) the numbers$g _ { 1 } , g _ { 2 } \ge 0$and$n _ { 1 } = | I _ { 1 } | , n _ { 2 } = | I _ { 2 } |$satisfy

$$
g _ {1} + g _ {2} = g,
$$

$$
2 \leq 2 g _ {1} + n _ {2},
$$

and

$$
2 \leq 2 g _ {2} + n _ {2}.
$$

For notational convenience, given$b = ( b _ { 1 } , \ldots , b _ { n } )$and$I = \{ j _ { 1 } , \dots , j _ { k } \} \subset \{ 1 , \dots , n \}$ define$b _ { I }$by

For

$$
b _ {I} = (b _ {j _ {1}}, \dots , b _ {j _ {k}}).
$$

$$
a = \left(\left(g _ {1}, I _ {1}\right), \left(g _ {2}, I _ {2}\right)\right) \in \mathcal {I} _ {g, n},
$$

let

$$
V (a, x, y, \widehat {b}) = \frac {V _ {g _ {1} , n _ {1} + 1} (x , b _ {I _ {1}})}{2 ^ {m (g _ {1} , n _ {1} + 1)}} \times \frac {V _ {g _ {2} , n _ {2} + 1} (y , b _ {I _ {2}})}{2 ^ {m (g _ {2} , n _ {2} + 1)}}.
$$

Finally, define$\widehat { A } _ { g , n } ^ { d c o n } : \mathbb { R } _ { + } ^ { n + 2 } \longrightarrow \mathbb { R } _ { + }$by

$$
\widehat {\mathcal {A}} _ {g, n} ^ {d c o n} (x, y, b _ {1}, \widehat {b}) = \sum_ {a \in \mathcal {I} _ {g, n}} V (a, x, y, \widehat {b}) \cdot H (x + y, b _ {1}).
$$

III) : Definition of$\widehat { B } _ { g , n }$. Define$\widehat { B } _ { g , n } : \mathbb { R } _ { + } ^ { n + 1 } \to \mathbb { R } _ { + }$by

$$
\begin{array}{c} \widehat {\mathcal {B}} _ {g, n} (x, b _ {1}, \widehat {b}) = \frac {1}{2 ^ {m (g , n - 1)}} \sum_ {j = 2} ^ {n} \frac {1}{2} (H (x, b _ {1} + b _ {j}) + H (x, b _ {1} - b _ {j})) \\ \cdot V _ {g, n - 1} (x, b _ {2}, \ldots , \widehat {b _ {j}}, \ldots , b _ {n}). \end{array}\tag{5.6}
$$

Remark. Note that in this recursive formula, the factor$1 / 2$appears in the case of$g = n = 1$. The main reason is that the stabilizer of a simple closed curve separating of a one-handle contains a half twist. See [22] for more details.

Connection with topology of the set of pairs of pants. The recursive formula (5.5) is closely related to the topology of diferent types of pairs of pants in a surface. In fact, this formula gives us the volume of$\mathcal { M } _ { g , n } ( b )$in terms of volumes of moduli spaces of Riemann surfaces that we get by removing pairs of pants containing the boundary component$\beta _ { 1 } ~ [ 2 2 ]$

Remark. The functions$\mathcal { A } _ { g , n } ^ { c o n } ( b ) , \mathcal { A } _ { g , n } ^ { d c o n } ( b )$and$B _ { g , n } ( b )$are determined by the functions$\{ V _ { i , j } \}$where$2 i + j < 2 g + n$. Therefore equation (5.5) is a recursive formula for calculating$V _ { g , n } ( b )$. Using (5.5), one can show that$V _ { g , n } ( b )$is a polynomial in b (Theorem 1.1).

Calculating the coeficients of$V _ { g , n } ( b )$. The following elementary observations are our main tools for simplifying the recursive formula.

For$i \in \mathbb N$, define$F _ { 2 i + 1 } : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$by

$$
F _ {2 k + 1} (t) = \int_ {0} ^ {\infty} x ^ {2 k + 1} \cdot H (x, t) d x.
$$

By setting$z = x + y ;$, we get

$$
\begin{array}{l} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (x + y, t) d x d y = \int_ {0} ^ {\infty} \int_ {0} ^ {z} (z - y) ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (z, t) d y d z \\ = \frac {(2 i + 1) ! \cdot (2 j + 1) !}{(2 i + 2 j + 3) !} \int_ {0} ^ {\infty} z ^ {2 i + 2 j + 3} H (z, t) d z. \end{array}
$$

Therefore, we have

$$
\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x ^ {2 i + 1} \cdot y ^ {2 j + 1} \cdot H (x + y, t) d x d y = \frac {(2 i + 1) ! \cdot (2 j + 1) !}{(2 i + 2 j + 3) !} F _ {2 i + 2 j + 3} (t).\tag{5.7}
$$

These functions play a key role in the calculation of$V _ { g , n } ( b )$. It is easy to calculate the function$F _ { 2 k + 1 }$explicitly.

Lemma 5.2. For$0 \leq k$, we have

$$
\frac {F _ {2 k + 1} (t)}{(2 k + 1) !} = \sum_ {i = 0} ^ {k + 1} \zeta (2 i) (2 ^ {2 i + 1} - 4) \cdot \frac {t ^ {2 k + 2 - 2 i}}{(2 k + 2 - 2 i) !}.
$$

Therefore, the function$F _ { 2 k + 1 } ( t )$is a polynomial in$t ^ { 2 }$of degree$k + 1$, and the coeficient of$m ^ { 2 k + 2 - 2 i }$lies in$\pi ^ { 2 i } \cdot \mathbb { Q } _ { > 0 }$

Remark. Here$\zeta ( 0 ) = - 1 / 2$, and therefore the leading coeficient of the polynomial $F _ { 2 k + 1 } ( t )$is$t ^ { 2 k + 2 } / ( 2 k + 2 )$

Leading coeficients of$V _ { g , n } ( b )$. As we will see later, calculating the leading coefficients of$V _ { g , n } ( b )$turns out to be easier than calculating other terms; the recursive formula simplifies when$\sum _ { i = 1 } ^ { n } \alpha _ { i } = 3 g - 3 + n$

Simplifying$\mathscr { A } _ { g , n } ^ { c o n }$and$\mathcal { A } _ { g , n } ^ { d c o n }$. Let$P ( x , y )$be a polynomial of degree d in$x ^ { 2 }$and $y ^ { 2 }$of the form

$$
P (x, y) = \sum_ {1 \leq i + j \leq d} C (i, j) x ^ {2 i} y ^ {2 j}.
$$

Then equation (5.7) and Lemma 5.2 imply that the function

$$
\widehat {P} (x) = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} y _ {1} y _ {2} H \left(y _ {1} + y _ {2}, x\right) P \left(y _ {1}, y _ {2}\right) d y _ {1} d y _ {2}
$$

is a polynomial in$x ^ { 2 }$; the leading term of$\widehat { P } ( x )$is equal to

$$
\sum_ {i + j = d} \frac {(2 i + 1) ! (2 j + 1) !}{(2 d + 4) !} C (i, j) x ^ {2 d + 4}.\tag{5.8}
$$

Simplifying$B _ { g , n }$. Let$Q ( x )$be a polynomial of degree d in$x ^ { 2 }$of the form

$$
Q (x) = \sum_ {i = 0} ^ {d} C (i) x ^ {2 i}.
$$

Then the function

$$
\widehat {Q} (x, y) = \frac {1}{2} \int_ {0} ^ {\infty} t Q (t) (H (t, x + y) + H (t, x - y)) d t
$$

is a polynomial of degree$d + 1$in$x ^ { 2 }$and$y ^ { 2 }$. Using Lemma 5.2, this polynomial can be explicitly calculated; when$i + j = d + 1$the term corresponding to$x ^ { 2 i } y ^ { 2 j }$ in$\widehat { Q } ( x , y )$is equal to

$$
(2 d + 1)! C (d) \frac {x ^ {2 i} y ^ {2 j}}{(2 i) ! (2 j) !}.\tag{5.9}
$$

Notation. Given$\mathbf { k } = ( k _ { 1 } , \ldots , k _ { n } ) \in \mathbb { Z } _ { + } ^ { n }$, let

$$
\widehat {C} (\mathbf {k}) = \frac {C _ {g} (\mathbf {k})}{2 ^ {m (g , n)}},
$$

where$g$is determined by$\textstyle { 3 g - 3 + n = \sum _ { i = 1 } ^ { n } k _ { i } }$. The factor$2 ^ { m ( g , n ) }$is important in the case of$g = n = 1$

Also, for$I \subset \{ 2 , \ldots n \}$, let$\mathbf { k } _ { I } = ( k _ { s } ) _ { s \in I }$, and$I ^ { c } = \{ 2 , \dots n \} - I$. For simplicity, we denote the coeficient of

$$
x _ {1} ^ {2 k _ {1}} \dots x _ {n} ^ {2 k _ {n}}
$$

in the polynomial$F ( x _ { 1 } , \ldots , x _ { n } )$by$F ( x _ { 1 } , \ldots , x _ { n } ) [ \mathbf { k } ]$. For example, by definition, $C _ { g } ( \mathbf { k } ) = V _ { g , n } ( b ) [ \mathbf { k } ]$

In terms of the above notation, the recursive formula for the leading coeficients of volume polynomials translates to the following statement.

Lemma 5.3. The leading coeficients of the polynomials$\mathcal { A } _ { g , n } ^ { d c o n } ( b ) , \ \mathcal { A } _ { g , n } ^ { c o n } ( b )$and $B _ { g , n } ( b )$are given by

$$
\begin{array}{l} \bullet \mathcal {A} _ {g, n} ^ {d c o n} (b) [ \mathbf {k} ] = \\ \frac {2 k _ {1} + 1}{2} \sum_ {i + j = k _ {1} - 2} \frac {(2 i + 1) ! (2 j + 1) !}{(2 k _ {1} + 1) !} \sum_ {I \subset \{2, \dots n \}} \widehat {C} (i, \mathbf {k} _ {I}) \cdot \widehat {C} (j, \mathbf {k} _ {I ^ {c}}), \\ \bullet \mathcal {A} _ {g, n} ^ {c o n} (b) [ \mathbf {k} ] = \\ \frac {2 k _ {1} + 1}{2} \sum_ {i + j = k _ {1} - 2} \frac {(2 i + 1) ! (2 j + 1) !}{(2 k _ {1} + 1) !} \widehat {C} (i, j, k _ {2}, \dots , k _ {n}), \end{array}
$$

and

$$
\begin{array}{l} \bullet \mathcal {B} _ {g, n} (b) [ \mathbf {k} ] = \\ (2 k _ {1} + 1) \sum_ {j = 2} ^ {n} \frac {(2 (k _ {1} + k _ {j} - 1) + 1) !}{(2 k _ {1} + 1) ! (2 k _ {j}) !} \widehat {C} (k _ {1} + k _ {j} - 1, k _ {2}, \dots , \widehat {k _ {j}}, \dots , k _ {n}). \end{array}
$$

Here$\mathbf { k } = ( k _ { 1 } , \ldots , k _ { n } ) \in \mathbb { Z } _ { + } ^ { n }$is such that$\textstyle \sum _ { i = 1 } ^ { n } k _ { i } = 3 g - 3 + n$

Sketch of the proof. To calculate the leading coeficients of$\mathcal { A } _ { g , n } ^ { d c o n } ( b )$, it is enough to find the coeficient of$b _ { 1 } ^ { 2 k _ { 1 } } \cdot \cdot \cdot b _ { n } ^ { 2 k _ { \tau } }$<sup>n</sup> in

$$
\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} x y V _ {g _ {1}, n _ {1}} (x, b _ {I _ {1}}) \times V _ {g _ {2}, n _ {2}} (x, b _ {I _ {2}}) H (x + y, b _ {1}) d x d y
$$

for any$a \in \mathcal { T } _ { g , n }$. Now using Theorem$1 . 1 , V _ { g _ { 1 } , n _ { 1 } } ( b _ { I _ { 1 } } ) \times V _ { g _ { 2 } , n _ { 2 } } ( b _ { I _ { 2 } } )$is a polynomial in $b _ { 1 } ^ { 2 } , \ldots , b _ { n } ^ { 2 }$. So we can use (5.8) to obtain the result. Similarly, the leading coeficients of$\mathcal { A } _ { g , n } ^ { c o n } ( b )$and$B _ { g , n } ( b )$can be calculated using equations (5.8) and (5.9).

## 6. Virasoro equations

In this section we use the relationship between the volume polynomials and the intersection numbers of tautological classes to derive the Virasoro equations.

String and dilaton equation. If one of the$\alpha _ { i }$'s is 0 or 1, the coeficients of $b _ { 1 } ^ { 2 \alpha _ { 1 } } \cdot \cdot \cdot b _ { n } ^ { 2 \alpha _ { n } }$in$\mathcal { A } _ { g , n } ^ { d c o n } ( b )$and$\mathcal { A } _ { g , n } ^ { c o n } ( b )$equal zero. Hence by using Lemma 5.3 and Theorem 4.4, we obtain the following:

• String equation:$\langle \tau _ { 1 } , \tau _ { \alpha _ { 1 } } , \ldots , \tau _ { \alpha _ { n } } \rangle _ { g } = ( 2 g + n - 2 ) \langle \tau _ { \alpha _ { 1 } } , \ldots , \tau _ { \alpha _ { n } } \rangle _ { g } ,$

• Dilaton equation:$\langle \tau _ { 0 } , \tau _ { \alpha _ { 1 } } , \ldots , \tau _ { \alpha _ { n } } \rangle _ { g } = \sum _ { \alpha _ { i } \ne 0 } \langle \tau _ { \alpha _ { 1 } } , \ldots , \tau _ { \alpha _ { i } - 1 } , \ldots \rangle _ { g } .$

Here$\textstyle \sum _ { i = 1 } ^ { n } \alpha _ { i } = 3 g - 3 + n$, and as in the Introduction,

$$
\langle \tau_ {\alpha_ {1}}, \ldots \tau_ {\alpha_ {n}} \rangle_ {g} = \int_ {\overline {{\mathcal {M}}} _ {g, n}} \psi_ {1} ^ {\alpha_ {1}} \dots \psi_ {n} ^ {\alpha_ {n}}.
$$

For a simple algebro-geometric proof of the preceding result see [9].

Virasoro constraints. Let

$$
F _ {g} (t _ {0}, t _ {1}, \dots) = \sum_ {\{d _ {i} \}} \langle \prod \tau_ {d _ {i}} \rangle_ {g} \prod_ {r > 0} t _ {r} ^ {n _ {r}} / n _ {r}!,
$$

where the sum is over all sequences of nonnegative integers with finitely many nonzero terms and$n _ { r } = \mathrm { C a r d } ( i : d _ { i } = r )$. Let

$$
F = \sum_ {g = 0} ^ {\infty} \lambda^ {2 g - 2} F _ {g}.
$$

Define the sequence of diferential operators$L _ { - 1 } , L _ { 0 } , . . . L _ { n } , . . .$. by

$$
L _ {- 1} = \frac {\partial}{\partial t _ {0}} + \frac {\lambda^ {- 2}}{2} t _ {0} ^ {2} + \sum_ {i = 1} ^ {\infty} t _ {i + 1} \frac {\partial}{\partial t _ {i}},
$$

$$
L _ {0} = \frac {3}{2} \frac {\partial}{\partial t _ {1}} + \sum_ {i = 1} ^ {\infty} \frac {2 i + 1}{2} \frac {\partial}{\partial t _ {i}} + \frac {1}{1 6},
$$

and for$n \geq 1$

$$
\begin{array}{l} L _ {n} = - \left(\frac {(2 n + 3) ! !}{2 ^ {n + 1}}\right) \frac {\partial}{\partial t _ {n + 1}} + \sum_ {i = 0} ^ {\infty} \left(\frac {(2 i + 2 n + 1) ! !}{(2 i - 1) ! ! 2 ^ {n + 1}}\right) t _ {i} \frac {\partial}{\partial t _ {i + n}} \\ \qquad + \frac {\lambda^ {2}}{2} \sum_ {i = 0} ^ {n - 1} \left(\frac {(2 i + 1) ! ! (2 n - 2 i - 1) ! !}{2 ^ {n + 1}}\right) \frac {\partial^ {2}}{\partial t _ {i} \partial t _ {n - 1 - i}}, \end{array}
$$

where$( 2 i + 1 ) ! ! = 1 \cdot 3 \dots \cdot ( 2 i + 1 )$

Theorem 6.1. For$k \geq - 1$, we have

$$
L _ {k} (\exp (F)) = 0.
$$

Remark. Since the sequence$\{ L _ { i } \}$satisfies

$$
[ L _ {m}, L _ {n} ] = (m - n) L _ {m + n},
$$

it is enough to show that$L _ { 2 } ( e ^ { F } ) = 0$. However, here we show$L _ { k } ( e ^ { F } ) = 0$for any $k \geq - 1$

Proof. Note that$L _ { - 1 }$and$L _ { 0 }$are equivalent to the dilaton and string equations. Using the recursive formula for the volume polynomials in equation (5.5), for any $\mathbf { k } = \left( k _ { 1 } , \ldots , k _ { n } \right)$we have

$$
(2 k _ {1} + 1) \cdot V _ {g, n} (b) [ \mathbf {k} ] = \mathcal {A} _ {g, n} ^ {c o n} (b) [ \mathbf {k} ] + \mathcal {A} _ {g, n} ^ {d c o n} (b) [ \mathbf {k} ] + \mathcal {B} _ {g, n} (b) [ \mathbf {k} ].\tag{6.1}
$$

Using Lemma 5.3, we can write$\mathcal { A } _ { g , n } ^ { c o n } ( b ) [ \mathbf { k } ] , \mathcal { A } _ { g , n } ^ { d c o n } ( b ) [ \mathbf { k } ]$and$B _ { g , n } ( b ) [ \mathbf { k } ]$in terms of $\widehat { C } ( \mathbf { k } ^ { \prime } ) ^ { \prime } \mathrm { s }$. On the other hand, by Theorem 4.4, we have

$$
\widehat {C} (\mathbf {k}) = \frac {C _ {g} (\mathbf {k})}{2 ^ {m (g , n)}} = \frac {1}{2 ^ {| \mathbf {k} |} \mathbf {k} !} \int_ {\overline {{\mathcal {M}}} _ {g, n}} \psi_ {1} ^ {k _ {1}} \dots \psi_ {n} ^ {k _ {n}} = \frac {\left\langle \tau_ {k _ {1}} , \ldots , \tau_ {k _ {n}} \right\rangle}{2 ^ {k _ {1}} k _ {1} ! \cdots 2 ^ {k _ {n}} k _ {n} !},
$$

where$3 g - 3 + n = \sum _ { i = 1 } ^ { n } k _ { i }$

Since

$$
\frac {(2 n) !}{2 ^ {n} n !} = (2 n - 1)!!,
$$

from equation (6.1) and Lemma$5 . 3 .$, we get

$$
\begin{array}{l} (2 k _ {1} + 1)!! \left\langle \tau_ {k _ {1}}, \ldots , \tau_ {k _ {n}} \right\rangle \\ = \frac {1}{2} \sum_ {i + j = k _ {1} - 2} (2 i + 1)!! (2 j + 1)!! \sum_ {I \subset \{2, \ldots n \}} \left\langle \tau_ {i}, \tau_ {\mathbf {k} _ {I}} \right\rangle \cdot \left\langle \tau_ {j}, \tau_ {\mathbf {k} _ {I ^ {c}}} \right\rangle \\ + \frac {1}{2} \sum_ {i + j = k _ {1} - 2} (2 i + 1)!! (2 j + 1)!! \left\langle \tau_ {i}, \tau_ {j}, \tau_ {k _ {2}}, \ldots , \tau_ {k _ {n}} \right\rangle \\ + \sum_ {j = 2} ^ {n} \frac {(2 (k _ {1} + k _ {j} - 1) + 1) ! !}{(2 k _ {j} - 1) ! !} \left\langle \tau_ {k _ {2}}, \ldots , \tau_ {k _ {j} + k _ {1} - 1}, \ldots , \tau_ {k _ {n}} \right\rangle . \end{array}\tag{6.2}
$$

It is easy to see that equation (6.2) implies$L _ { k _ { 1 } - 1 } ( e ^ { F } ) = 0$

## MARYAM MIRZAKHANI

## Acknowledgment

I would like to thank Curt McMullen for his invaluable help, encouragement, and many stimulating discussions. I would also like to thank Scott Wolpert for many helpful comments. I am grateful to Izzet Coskun, Melissa Liu, Andrei Okounkov, Rahul Pandharipande, Ravi Vakil, and Jonathan Weitsman for helpful discussions. I would also like to thank the referee for helpful comments and for pointing out some mistakes in the original draft of this paper and [22].

## References

1. E. Arbarello, Sketches of kdv, Symposium in Honor of C. H. Clemens (Salt Lake City, UT, 2000), Contemp. Math., vol. 312, Amer. Math. Soc., 2002, pp. 9–69. MR1941573 (2004i:14039)

2. L. Bers, Spaces of degenerating Riemann surfaces, Discontinuous groups and Riemann surfaces, Annals of Math. Studies, vol. 76, Princeton University Press, 1974, pp. 43–55. MR0361051 (50:13497)

3. M. Boggi and M. Pikaart, Galois covers of moduli of curves, Compositio Math. 120 (2000), 171–191. MR1739177 (2002a:14025)

4. P. Buser, Geometry and spectra of compact Riemann surfaces, Birkhäuser Boston, 1992. MR1183224 (93g:58149)

5. R. Dijkgraaf, E. Verlinde, and H. Verlinde, Loop equations and Virasoro constraints in nonperturbative two-dimensional quantum gravity, Nuclear Phys. B 384 (1991), 435–456. MR1083914 (92a:81171)

6. W. Goldman, The symplectic nature of fundamental groups of surfaces, Adv. Math. 54 (1984), 200–225. MR0762512 (86i:32042)

7., Ergodic theory on moduli spaces, Ann. of Math. 146 (1997), 475–507. MR1491446 (99a:58024)

8. V. Guillemin, Moment maps and combinatorial invariants of Hamiltonian $T^n$-spaces, Birkhäuser Boston, Inc., Boston, MA, 1994. MR1301331 (96e:58064)

9. J. Harris and I. Morrison, Moduli of curves, Graduate Texts in Mathematics, vol. 187, Springer-Verlag, 1998. MR1631825 (99g:14031)

10. Y. Imayoshi and M. Taniguchi, An introduction to Teichmüller spaces, Springer-Verlag, 1992. MR1215481 (94b:32031)

11. C. Itzykson and J. Zuber, Combinatorics of the modular group. II. The Kontsevich integrals, Internat. J. Modern Phys. A 7 (1992), 5661–5705. MR1180858 (94m:32029)

12. R. Kaufmann, Y. Manin, and D. Zagier, Higher Weil-Petersson volumes of moduli spaces of stable n-pointed curves, Comm. Math. Phys. 181 (1996), 736–787. MR1414310 (98i:14029)

13. F. Kirwan, Momentum maps and reduction in algebraic geometry, Diferential Geom. Appl. 9 (1998), 135–171. MR1636303 (99e:58072)

14. M. Kontsevich, Intersection on the moduli space of curves and the matrix Airy function., Comm. Math. Phys. 147 (1992). MR1171758 (93e:32027)

15. E. Looijenga, Intersection theory on Deligne-Mumford compactifications (after Witten and Kontsevich), Séminaire Bourbaki, 1992/93, Astérisque, volume 216, 1993, pp. 187–212. MR1246398 (95b:32033)

16., Smooth Deligne-Mumford compactification by means of Prym level structures, J. Algebraic Geom. 3 (1994), 283–293. MR1257324 (94m:14029)

17. Y. Manin and P. Zograf, Invertible cohomological field theories and Weil-Petersson volumes, Ann. Inst. Fourier (Grenoble) 50 (2000), 519–535. MR1775360 (2001g:14046)

18. H. Masur, The extension of the Weil-Petersson metric to the boundary of Teichmüller space, Duke Math. J. 43 (1976), 623–635. MR0417456 (54:5506)

19. D. McDuf, Introduction to symplectic topology, Amer. Math. Soc., Providence, RI, 1999. MR1702941 (2000e:53099)

20. G. McShane, Simple geodesics and a series constant over Teichmüller space, Invent. Math. 132 (1998), 607–632, MR1625712 (99i:32028)

21. J. Milnor and J. Stashef, Characteristic classes, Annals of Mathematics Studies. MR0440554 (55:13428)

Department of Mathematics<sub>,</sub> Princeton University<sub>,</sub> Princeton<sub>,</sub> NJ 08544 22. M. Mirzakhani, Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces, Preprint, 2003.

23. T. Nakanishi and M. Näätänen, Areas of two-dimensional moduli spaces, Proc. Amer. Math. Soc. 129 (2001), 3241–3252. MR1844999 (2002e:32020)

24. A. Okounkov, Random trees and moduli of curves, Asymptotic combinatorics with applications to mathematical physics, Lecture Notes in Mathematics, vol. 1815, Springer-Verlag, 2003, pp. 89–126. MR2009837 (2004m:14049)

25. A. Okounkov and R. Pandharipande, Gromov-Witten theory, Hurwitz theory, and matrix models, I, Preprint.

26. R. Penner, Weil-Petersson volumes, J. Diferential Geom. 35 (1992), 559–608. MR1163449 (93d:32029)

27. J. Weitsman, Geometry of the intersection ring of the moduli space of flat connections and the conjectures of Newstead and Witten, Topology 37 (1998). MR1480881 (99m:57030)

28. E. Witten, Two-dimensional gravity and intersection theory on moduli space, Surveys in diferential geometry, Lehigh Univ., Bethlehem, PA, 1991. MR1144529 (93e:32028)

29., Two dimensional gauge theories revisited, J. Geom. Phys. 9 (1992), 303–368. MR1185834 (93m:58017)

30. S. Wolpert, An elementary formula for the Fenchel-Nielsen twist, Comment. Math. Helv. 56 (1981), 132–135. MR0615620 (82k:32053)

31. , On the homology of the moduli space of stable curves, Ann. of Math.(2) 118 (1983), 491–523. MR0727702 (86h:32036)

32., On obtaining a positive line bundle from the Weil-Petersson class, Amer. J. Math. 107 (1985), 1485–1507. MR0815769 (87f:32058)

33., On the Weil-Petersson geometry of the moduli space of curves, Amer. J. Math. 107 (1985), 969–997. MR0796909 (87b:32040)

34. P. Zograf, The Weil-Petersson volume of the moduli space of punctured spheres, Mapping class groups and moduli spaces of Riemann surfaces, Contemp. Math., vol. 150, Amer. Math. Soc., 1993, pp. 367–372. MR1234274 (94g:32030)