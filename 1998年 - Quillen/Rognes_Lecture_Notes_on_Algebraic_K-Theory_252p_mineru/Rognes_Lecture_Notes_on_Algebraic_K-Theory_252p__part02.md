Example 7.1.13. Each object X of$\mathcal { C }$corresponds to a 0-cell, each non-identity morphism$f \colon X \to Y$corresponds to a 1-cell$[ f ] X$connecting X and$Y _ { ; }$, and each pair of non-identity morphisms$f \colon X \to { \dot { Y } }$and$g \colon Y \to Z$corresponds to a 2-cell$[ g | f ] X$attached along [f]X, [g]Y and$[ g f ] X$

![](images/page_0_image_1.jpg)

Remark 7.1.14. Our notation follows Waldhausen [68]. Other authors, including Quillen [55], write BC for the classifying space of C. [[Comment on the case$B G = | \mathcal { B } G | . ] ]$

Lemma 7.1.15. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be an isomorphism of small categories. Then

$$
| F | \colon | \mathcal {C} | \xrightarrow {\cong} | \mathcal {D} |
$$

is an isomorphism of CW complexes.

Proof. The inverse functor$G \colon { \mathcal { D } }  { \mathcal { C } }$induces the inverse cellular homeomorphism$| G | \colon | \mathcal { D } | \to | \mathcal { C } |$□

Lemma 7.1.16. The classifying space functor$| - | \colon \mathbf { C a t } \to \mathbf { C W }$respects finite products. Given small categories$\mathcal { C }$and$\mathcal { D }$, the projections

$$
\mathcal {C} \longleftarrow \mathcal {C} \times \mathcal {D} \longrightarrow \mathcal {D}
$$

induce a homeomorphism

$$
| \mathcal {C} \times \mathcal {D} | \xrightarrow {\cong} | \mathcal {C} | \times | \mathcal {D} |,
$$

where the target is topologized as the product of CW complexes.

Proof. This is the composite of the two homeomorphisms

$$
\left| N _ {\bullet} (\mathcal {C} \times \mathcal {D}) \right| \cong \left| N _ {\bullet} \mathcal {C} \times N _ {\bullet} \mathcal {D} \right| \cong \left| N _ {\bullet} \mathcal {C} \right| \times \left| N _ {\bullet} \mathcal {D} \right|
$$

from Lemma 7.1.8 and Proposition 6.4.3.

The following useful observation was publicized by Segal [59].

Proposition 7.1.17. Let φ:$F \Rightarrow G$be a natural transformation of functors $F , G \colon \mathcal { C } \to \mathcal { D }$between small categories. The nerve of the corresponding functor $\Phi \colon \mathcal { C } \times [ 1 ] \to \mathcal { D }$induces a simplicial homotopy

$$
N _ {\bullet} \Phi \colon N _ {\bullet} \mathcal {C} \times \Delta_ {\bullet} ^ {1} \longrightarrow N _ {\bullet} \mathcal {D}
$$

between$N _ { \bullet } F$and$N _ { \bullet } G \colon N _ { \bullet } \mathcal { C } \to N _ { \bullet } \mathcal { D }$, and a homotopy

$$
| \Phi |: | \mathcal {C} | \times I \longrightarrow | \mathcal {D} |
$$

between$| F |$and$| G | \colon | \mathcal { C } | \to | \mathcal { D } |$

Proof. This is clear from Lemma 3.1.12, the identity$N _ { \bullet } [ 1 ] = \Delta _ { \bullet } ^ { 1 }$, the identification$| \Delta _ { \bullet } ^ { 1 } | = \Delta ^ { 1 } \cong I$, and the commutation of nerves and classifying spaces with (finite) products.□

Example 7.1.18. The simplicial homotopy can be illustrated as follows. Let $f \colon X \to Y$and$g \colon Y \to Z$be composable morphisms in$\mathcal { C }$. The functor$\Phi \colon \mathcal { C } \times$ $[ 1 ]  \mathcal { D }$maps the diagram

![](images/page_1_image_2.jpg)

in$\mathcal { C } \times [ 1 ]$to the diagram

![](images/page_1_image_4.jpg)

in${ \mathcal { D } } .$. The reader may visualize how the image of$\Delta _ { \bullet } ^ { 2 } \times \Delta _ { \bullet } ^ { 1 }$in$N _ { \bullet } ( \mathcal { C } \times [ 1 ] )$is mapped to$N _ { \bullet } ( \mathcal { D } )$, or how the image of$\Delta ^ { 2 } \times \bar { \Delta } ^ { 1 }$in$\vert \mathcal { C } \times [ 1 ] \vert$is mapped to$| \mathcal D |$

Lemma 7.1.19. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be an equivalence of small categories. Then

$$
| F |: | \mathcal {C} | \xrightarrow {\simeq} | \mathcal {D} |
$$

is a homotopy equivalence.

Proof. Let$G \colon { \mathcal { D } }  { \mathcal { C } }$be an inverse equivalence. The natural isomorphisms $G \circ F \cong i d _ { \mathcal { C } }$and$F \circ G \cong i d _ { \mathcal { D } }$induce homotopies$| G | \circ | F | \simeq i d _ { | \mathcal { C } | }$and$| F | \circ | G | \simeq$ $i d _ { | \mathcal { D } | }$, exhibiting$| F |$and$| G |$as homotopy inverses.□

Definition 7.1.20. Let$\mathcal { C }$be a category with a small skeleton$\mathcal { C } ^ { \prime }$, as in Definition 3.2.11. Then we can define$\lvert \mathcal { C } \rvert$, up to homotopy equivalence, to be$\left| \mathcal { C } ^ { \prime } \right|$ For any other skeleton$\mathcal { C } ^ { \prime \prime }$the composite equivalence$\mathcal { C } ^ { \prime } \subseteq \mathcal { C } \longrightarrow \mathcal { C } ^ { \prime \prime }$induces a homotopy equivalence$| \mathcal { C } ^ { \prime } | \simeq | \mathcal { C } ^ { \prime \prime } |$, well-defined up to homotopy.

Lemma 7.1.21. Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$and$G \colon { \mathcal { D } } \to { \mathcal { C } }$be an adjoint pair of functors between small categories. Then

$$
| F | \colon | \mathcal {C} | \xrightarrow {\simeq} | \mathcal {D} |
$$

and

$$
| G | \colon | \mathcal {D} | \xrightarrow {\simeq} | \mathcal {C} |
$$

are mutually inverse homotopy equivalences.

Proof. The natural transformations η :$i d _ { \mathcal { C } } \Rightarrow G \circ F$and$\epsilon \colon F \circ G \Rightarrow i d _ { \mathcal { D } }$induce homotopies$i d _ { | \mathcal { C } | } \simeq | G | \circ | F |$and$\vert F \vert \circ \vert G \vert \simeq i d _ { \vert \mathcal { D } \vert }$, exhibiting |F| and$| G |$as homotopy inverses.□

Definition 7.1.22. A functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$between (skeletally) small categories is called a homotopy equivalence if$| F | \colon | \mathcal { C } | \to | \mathcal { D } |$is a homotopy equivalence of spaces. A category$\mathcal { C }$is said to be contractible$\mathrm { i f } \ | { \mathcal { C } } |$is a contractible space.

Lemma 7.1.23. Suppose that$\mathcal { C }$has an initial object or a terminal object. Then $\mathcal { C }$is contractible.

Proof. Suppose that$X$is initial in$\mathcal { C } .$. The composite$\mathcal { C } \to * \to \mathcal { C }$taking each object Y in$\mathcal { C }$to$X$, and each morphism in$\mathcal { C }$to$i d _ { X }$, is the constant functor const(X). The unique morphisms$\epsilon _ { Y } \colon X \to Y$, for all$Y$in$\mathcal { C }$, define a natural transformation$\epsilon :$const$( X ) \Rightarrow i d _ { \mathcal { C } }$. Passing to classifying spaces, |ǫ is a homotopy from the constant map to$X$, viewed as a 0-cell in$\lvert \mathcal { C } \rvert$, to the identity map$i d _ { | \mathcal { C } | }$. Hence$\lvert \mathcal { C } \rvert$is contractible.

The case with a terminal object is dual.

Example 7.1.24. Let$\mathcal { C } = [ p ]$, with terminal object$p .$The unique morphisms $\eta _ { i } ~ = ~ ( i ~ \leq ~ p )$for$i ~ \in ~ [ p ]$define a natural transformation$\eta \colon i d _ { [ p ] } \ \Rightarrow \ \mathrm { c o n s t } _ { p }$ from the identity to the constant functor at$p .$The corresponding (bi-)functor $H \colon [ p ] \times [ 1 ]  [ p ]$is given by$H ( i , 0 ) = i$and$H ( i , 1 ) = p ,$for$i \in [ p ]$. Its nerve

$$
N _ {\bullet} H \colon \Delta_ {\bullet} ^ {p} \times \Delta_ {\bullet} ^ {1} \longrightarrow \Delta_ {\bullet} ^ {p}
$$

is a simplicial homotopy from$i d _ { \Delta _ { \bullet } ^ { p } }$to the constant simplicial map to the vertex $p$in$\Delta _ { \bullet } ^ { p } .$. It is given in simplicial degree n by$N _ { n } H \colon \Delta _ { n } ^ { p } \times \Delta _ { n } ^ { 1 } \to \Delta _ { n } ^ { p }$, mapping ($x \colon [ n ] \to [ p ] , \zeta \colon [ n ] \to [ 1 ] )$to$N _ { n } H ( \alpha , \zeta ) = \beta \colon [ n ] \to [ p ]$, given by

$$
\beta (i) = \left\{ \begin{array}{l l} \alpha (i) & \text { if } \zeta (i) = 0 \\ p & \text { if } \zeta (i) = 1. \end{array} \right.
$$

Setting$\zeta = \zeta _ { k } ^ { n }$for$0 \leq k \leq n + 1$, we can rewrite this as$h _ { n } ^ { k } ( \alpha ) = N _ { n } H ( \alpha , \zeta _ { k } ^ { n } ) =$ $\beta ,$where

$$
\beta (i) = \left\{ \begin{array}{l l} \alpha (i) & \text { if } 0 \leq i <   k \\ p & \text { if } k \leq i \leq n. \end{array} \right.
$$

In Waldhausen’s formulation, with$X = \Delta _ { \bullet } ^ { p } .$, the functor$X ^ { \ast } \colon ( \Delta / [ 1 ] ) ^ { o p }$Set maps$( [ n ] , \zeta \colon [ n ] \to [ 1 ] )$to$X _ { n } = \Delta _ { n } ^ { p }$. The corresponding natural transformation $h \colon X ^ { * } \Rightarrow X ^ { * }$has components$h _ { \zeta } \colon \Delta _ { n } ^ { p } \to \Delta _ { n } ^ { p }$given by$h _ { \zeta } ( \alpha ) = N _ { n } H ( \alpha , \zeta ) = \beta$ with$\beta$equal to the composite

$$
[ n ] \stackrel {(\alpha , \zeta)} {\longrightarrow} [ p ] \times [ 1 ] \stackrel {H} {\longrightarrow} [ p ].
$$

[[Since [p] has the initial object$0 ,$there is a dual simplicial homotopy to the identity of$\Delta _ { \bullet } ^ { p }$, from the constant simplicial map to the vertex$0 . ] ]$

Lemma 7.1.25. Let$\mathcal { C }$be a small category. There is a natural bijection

$$
\pi_ {0} (\mathcal {C}) \cong \pi_ {0} (| \mathcal {C} |).
$$

Proof. Recall Definition 3.5.6. The bijection takes the equivalence class of an object$X$of$\mathcal { C }$, which we can view as a 0-simplex in$N _ { \bullet } \mathcal { C }$, to the path component of the corresponding 0-cell (X) in |C |. If$f \colon X \to Y$is a morphism in$\mathcal { C }$, so $X \sim Y$, then the 1-simplex$[ f ] X$in$N _ { \bullet } \mathcal { C }$maps to a path$( f )$from$( X )$to$( Y )$ in |C |, so (X) and$( Y )$lie in the same path component. By induction, if$X \simeq Y$ are related by a chain of morphisms in$\mathcal { C }$, then$( X )$and (Y ) still lie in the same path component.

Conversely, any point in$\lvert \mathcal { C } \rvert$is in the image of a simplex$\{ x \} \times \Delta ^ { n }  | \mathcal { C } |$, for some x:$[ n ] \to \mathcal { C } .$, and is in the same path component as the 0-cell corresponding to the object$X _ { 0 } = x ( 0 )$. Given two objects$X$and Y of$\mathcal { C }$, if (X) and (Y ) lie in the same path component of$\lvert \mathcal { C } \rvert$, then there exists a path in |C| from$( X )$ to$( Y )$, and this path can be homotoped into the 1-skeleton of$\lvert \mathcal { C } \rvert$. Hence it is homotopic to the path sum of a chain of paths$( f )$, or reverse paths$\overline { { ( f ) } }$ for morphisms$f$in$\mathcal { C }$. This means that$X$and$Y$are connected by a chain of morphisms in$\mathcal { C } .$so$X \simeq Y$and$X$and Y represent the same element in $\pi _ { 0 } ( \mathcal { C } )$□

Lemma 7.1.26. Consider a small category$\mathcal { C }$with a chosen object$X$. There is a natural group isomorphism

$$
\mathcal {C} [ \mathcal {C} ^ {- 1} ] (X, X) \cong \pi_ {1} (| \mathcal {C} |, X).
$$

Hence,${ \mathcal { C } } ( X , X ) \cong \pi _ { 1 } ( | { \mathcal { C } } | , X )$if$\mathcal { C }$is a groupoid.

Proof.$\mathrm { B y }$the van Kampen theorem, the fundamental group$\pi _ { 1 } ( | \mathcal { C } | , X )$is known to be generated by the edge paths in$\lvert \mathcal { C } \rvert$, which are words$( f _ { m } ^ { \pm 1 } , \ldots , f _ { 1 } ^ { \pm 1 } )$in the edges of$| \mathcal { C } | ,$or equivalently, in the morphisms of$\mathcal { C }$and their formal inverses, subject to the cancellation rules normally generated by the 2-cells in$\lvert \mathcal { C } \rvert$, i.e., the 2-simplices associated to each pair of composable morphisms$f$and$g$in$\mathcal { C }$ These rules assert that going round two of the edges of this triangle gives a path that is homotopic to going directly across the third edge.

Letting$h = g f .$, and taking into account the six possible orientations of the edges of the triangle, one gets the relations

$$
\begin{array}{l} (g ^ {- 1}, h ^ {+ 1}) \sim (f ^ {+ 1}) \\ (h ^ {- 1}, g ^ {+ 1}) \sim (f ^ {- 1}) \end{array} \qquad \begin{array}{l} (h ^ {+ 1}, f ^ {- 1}) \sim (g ^ {+ 1}) \\ (f ^ {+ 1}, h ^ {- 1}) \sim (g ^ {- 1}) \end{array} \qquad \begin{array}{l} (g ^ {+ 1}, f ^ {+ 1}) \sim (h ^ {+ 1}) \\ (f ^ {- 1}, g ^ {- 1}) \sim (h ^ {- 1}). \end{array}
$$

These may be simplified to$\left( g ^ { + 1 } , f ^ { + 1 } \right) \sim ( h ^ { + 1 } ) , \left( f ^ { - 1 } , g ^ { - 1 } \right) \sim ( h ^ { - 1 } ) , ( g ^ { + 1 } , g ^ { - 1 } ) \sim$ $( i d ^ { + 1 } )$and$( g ^ { - 1 } , g ^ { + 1 } ) \sim ( i d ^ { + 1 } )$. But these are precisely the generating relations among morphisms imposed in the definition of${ \mathcal { C } } [ { \mathcal { C } } ^ { - 1 } ]$□

## 7.2 The bar construction

Definition 7.2.1. Let M be a monoid with unit element e and multiplication $\mu \colon M \times M \to M$taking$( m , m ^ { \prime } )$to$\mu ( m , m ^ { \prime } ) = m m ^ { \prime }$. Let BM be the category with one object ∗, and one morphism$[ m ] \colon * \to *$for each$m \in M$, with identity [e], and composition$[ m ] \cdot [ m ^ { \prime } ] = [ m \dot { m } ^ { \prime } ]$for$m , m ^ { \prime } \in M$. The simplicial bar construction on M is the nerve

$$
B _ {\bullet} M = N _ {\bullet} \mathcal {B} M.
$$

It is the simplicial set with n-simplices the set

$$
B _ {n} M = \left\{\left[ m _ {n} \right| \dots \left| m _ {1} \right] \mid m _ {i} \in M \right\} = M ^ {n},
$$

face maps$d _ { i } \colon B _ { n } M \to B _ { n - 1 } M$given by

$$
d _ {i} ([ m _ {n} | \ldots | m _ {1} ]) = \left\{ \begin{array}{l l} [ m _ {n} | \ldots | m _ {2} ] & \text {for i = 0 ,} \\ [ m _ {n} | \ldots | m _ {i + 1} m _ {i} | \ldots | m _ {1} ] & \text {for 0 <   i <   n ,} \\ [ m _ {n - 1} | \ldots | m _ {1} ] & \text {for i = n ,} \end{array} \right.
$$

and degeneracy maps$s _ { j } \colon B _ { n } M \to B _ { n + 1 } M$given by

$$
s _ {j} ([ m _ {n} | \ldots | m _ {1}) = [ m _ {n} | \ldots | m _ {j + 1} | e | m _ {j} | \ldots | m _ {1} ]
$$

for$0 \leq j \leq n$. The bar construction on M is the topological realization

$$
B M = | B _ {\bullet} M | = | \mathscr {B} M |.
$$

It is a CW complex with one n-cell$[ m _ { n } | \ldots | m _ { 1 } ]$for each n-tuple of non-identity elements in M.

Given a monoid homomorphism$f \colon M \to N$, let$B _ { \bullet } f \colon B _ { \bullet } M \to B _ { \bullet } N$be the simplicial map of nerves$B _ { \bullet } f = N _ { \bullet } ( { \mathcal { B } } f )$, given in degree n by

$$
(B _ {n} f) ([ m _ {n} | \dots | m _ {1} ]) = [ f (m _ {n}) | \dots | f (m _ {1}) ].
$$

Let$B f \colon B M \to B N$be the cellular map$B f = | B _ { \bullet } f | = | { \mathcal { B } } f |$

Example 7.2.2. The bar construction on the trivial monoid$\{ e \}$is a point. The bar construction$B C _ { 2 }$on a group with two elements$\{ e , T \}$has one n-cell $[ T | \dots | T ]$for each$n \geq 0$

Lemma 7.2.3. The composite$B _ { \bullet } = N _ { \bullet } \circ \mathcal { B }$: Mon → sSet is a full and$f a i t h f u l$ functor, and$B = | - | \circ B _ { \bullet }$: Mon → CW is a (faithful) functor.

Proof. This is clear from Lemmas 2.8.5, 6.3.26 and 7.1.6.

Lemma 7.2.4. The projections$M \gets M \times N \to N$induce a natural simplicial isomorphism

$$
B _ {\bullet} (M \times N) \xrightarrow {\cong} B _ {\bullet} M \times B _ {\bullet} N
$$

and a natural homeomorphism of CW complexes

$$
B (M \times N) \xrightarrow {\cong} B M \times B N.
$$

Proof. This is clear from Lemmas 2.8.7 and 7.1.16.

Lemma 7.2.5. If M is commutative, then the unit map$\{ e \}  M$and the multiplication map$\mu \colon M \times M \to M$induce simplicial maps$\ast = B _ { \bullet } \{ e \} \to B _ { \bullet } M$ and

$$
B _ {\bullet} \mu \colon B _ {\bullet} M \times B _ {\bullet} M \cong B _ {\bullet} (M \times M) \longrightarrow B _ {\bullet} M,
$$

making$B _ { \bullet } M$a commutative monoid in sSet. Passing to CW realizations, the maps$* \to B M$and

$$
B \mu \colon B M \times B M \cong B (M \times M) \longrightarrow B M
$$

make BM a commutative monoid in CW.

[[Proof]]

[[Can iterate, to form$B ^ { n } M . ] ]$

Definition 7.2.6 (Translation category). Let M be a monoid and$Y \textrm { a }$left M-set. Let${ \mathcal { B } } ( M , Y )$be the small category with objects the$y \in Y ,$and with a morphism [m]y from y to my for each$m \in M , y \in Y$. We call${ \mathcal { B } } ( M , Y )$the translation category of the M-action on Y. If$M = G$is a group, then${ \mathcal { B } } ( G , Y )$ is a groupoid, called the translation groupoid.

Definition 7.2.7. In the special case$Y = M .$, let$\mathcal { E } ( M ) = \mathcal { B } ( M , M )$be the translation category for M acting from the left on itself, and let$E M = | \mathcal { E } ( M ) |$ be its classifying space. The right action of M on$Y \ = \ M$induces a right action on$\mathcal { E } ( M )$and on EM. [[Free action when$M = G$is a group, with orbits$E G / G = B G . ] ]$Note that$\mathcal { E } ( M )$has the initial object$e ,$with a unique morphism$[ m ] e$from e to any other object m. Hence EM is contractible.

Lemma 7.2.8.$| \mathcal { B } ( M , Y ) | \cong E M \times _ { M } Y$. When$M = G$is a group, there is a fiber bundle$Y  E G \times _ { G } Y  B G$

[[Same for simplicial monoids/groups acting on simplicial sets.]]

[[One-sided bar construction.$E _ { \bullet } G = B _ { \bullet } ( * , G , G )$contractible. fiber sequence$G  E G  B G . ] ]$

[[Form two-sided bar construction$B ( X , M , Y )$as classifying space of the category with objects$X \times Y$and a morphism from$( x \cdot m , y )$to$( x , m \cdot y )$, or vice versa.]]

Definition 7.2.9. Let M be a monoid, X a right M-set and Y a left M-set. Let${ \mathcal { B } } ( X , M , Y )$be the small category with objects the pairs$( x , y ) \in X \times Y$，and one morphism$x [ m ] y$from$( x m , y )$to$( x , m y )$for each$x \in X , m \in M$and $y \in Y$. The composite of$x [ m ] y$and [[ETC]]

[[Compute$\pi _ { 0 }$and$\pi _ { 1 }$of |C|, at least for groupoids.]]

## 7.3 Quillen’s theorem A

Quillen [55, p. 93] found the following useful suficient condition for a functor to be a homotopy equivalence.

Theorem 7.3.1 (Quillen’s theorem A). Let$F \colon { \mathcal { C } } \to { \mathcal { D } }$be a functor of small categories. Suppose that the left fiber$F / Y$is contractible for each object Y of D. Then F is a homotopy equivalence.

Proof. Let$T _ { \bullet , \bullet } ( F )$be the bisimplicial set with$( m , n )$-bisimplices the diagrams

![](images/page_6_image_1.jpg)

where the upper row lies in$\mathcal { C }$and the lower row lies in${ \mathcal { D } } .$In other words, an element of$T _ { m , n } ( F )$is a triple$( x , f , y )$, where$x \colon [ m ] \to \mathcal { C } , y \colon [ n ] \to \mathcal { D }$and $f \colon F ( X _ { m } )  Y _ { 0 }$is a morphism in D, where we set$X _ { i } = x ( i )$and$Y _ { j } = y ( j )$for $i \in [ m ] , j \in [ n ] ,$

The bisimplicial structure map$( \alpha , \beta ) ^ { * }$, for$\alpha \colon [ p ]  [ m ] , \beta \colon [ q ]  [ n ]$, takes $( x , f , y )$to

$$
(\alpha , \beta) ^ {*} (x, f, y) = (\alpha^ {*} (x), g, \beta^ {*} (y))
$$

in$T _ { p , q } ( F )$, where$g \colon F ( \alpha ^ { * } ( x ) _ { p } ) \to \beta ^ { * } ( y ) _ { 0 }$is the composite

$$
F (X _ {\alpha (p)}) \longrightarrow F (X _ {m}) \stackrel {f} {\longrightarrow} Y _ {0} \longrightarrow Y _ {\beta (0)}  .
$$

Hence the i-th left hand face map deletes$X _ { i } .$, and replaces$F ( X _ { m } )  Y _ { 0 }$with the composite$F ( X _ { m - 1 } ) \to F ( X _ { m } ) \to Y _ { 0 } { \mathrm { ~ i f ~ } } i = m$. The j-th left hand degeneracy map repeats$X _ { j }$. The i-th right hand face map deletes$Y _ { i }$, and replaces$F ( X _ { m } )$ $Y _ { 0 }$with the composite$F ( X _ { m } ) \ \to \ Y _ { 0 } \ \to \ Y _ { 1 }$if$i \ = \ 0$. The j-th right hand degeneracy map repeats$Y _ { j }$

For each$m \geq 0 .$, the simplicial set$T _ { m , \bullet } ( F )$decomposes as the disjoint union

$$
T _ {m, \bullet} (F) \cong \coprod_ {x \in N _ {m} \mathscr {C}} N _ {\bullet} (F (X _ {m}) / \mathscr {D}).
$$

indexed on the$x \colon [ m ] \to \mathcal { C }$. Each category$F ( X _ { m } ) / \mathcal { D }$has an initial object, hence is contractible by Lemma 7.1.23. Thus the simplicial map

$$
s _ {m, \bullet} \colon T _ {m, \bullet} (F) \cong \coprod_ {x \in N _ {m} \mathcal {C}} N _ {\bullet} (F (X _ {m}) / \mathcal {D}) \stackrel {{\simeq}} {{\longrightarrow}} \coprod_ {x \in N _ {m} \mathcal {C}} * \cong N _ {m} \mathcal {C}
$$

collapsing each summand$N _ { \bullet } ( F ( X _ { m } ) / \mathcal { D } )$to a point$* \cong \Delta _ { \bullet } ^ { 0 }$, is a weak homotopy equivalence. Here the set$N _ { m } \mathcal { C }$is viewed as a simplicial set in a trivial way, with n-simplices$N _ { m } \mathcal { C }$for all$n \geq 0$, and identity maps as simplicial structure maps.

Likewise, we view$N _ { \bullet } \mathcal { C }$as a bisimplicial set in a trivial way, with$( m , n ) \cdot$ simplices$N _ { m } \mathcal { C }$for all$m , n \geq 0$. In functorial terms, we are considering the composite functor

$$
\Delta^ {o p} \times \Delta^ {o p} \xrightarrow {p r _ {1}} \Delta^ {o p} \xrightarrow {N _ {\bullet} \mathcal {C}} \mathbf {S e t}.
$$

The weak homotopy equivalences$s _ { m , \bullet } \colon T _ { m , \bullet } ( F ) \to N _ { m } \mathcal { C }$for$m \geq 0$combine to a bisimplicial map

$$
s _ {\bullet , \bullet} \colon T _ {\bullet , \bullet} (F) \xrightarrow {\simeq} N _ {\bullet} \mathscr {C}.
$$

By the realization lemma,$s _ { \bullet , \bullet }$is a weak homotopy equivalence.

On the other hand, for each$n \geq 0$, the simplicial set$T _ { \bullet , n } ( F )$decomposes as the disjoint union

$$
T _ {\bullet , n} (F) \cong \coprod_ {y \in N _ {n} \mathscr {D}} N _ {\bullet} (F / Y _ {0})
$$

indexed on the$y \colon [ n ]  \mathcal { D }$. By hypothesis, each left fiber category$F / Y _ { 0 }$is contractible. Thus the simplicial map

$$
t _ {\bullet , n} \colon T _ {\bullet , n} (F) \cong \coprod_ {y \in N _ {n} \mathcal {D}} N _ {\bullet} (F / Y _ {0}) \xrightarrow {\simeq} \coprod_ {y \in N _ {n} \mathcal {D}} * \cong N _ {n} \mathcal {D}
$$

collapsing each summand$N _ { \bullet } ( F / Y _ { 0 } )$to a point, is a weak homotopy equivalence.

Now we view$N _ { \bullet } \mathcal { D }$as a bisimplicial set in the “other” trivial way, with $( m , n )$-simplices$N _ { n } \mathcal { D }$for all$m , n \geq 0$. The weak homotopy equivalences$t _ { \bullet , n }$ combine to a bisimplicial map

$$
t _ {\bullet , \bullet} \colon T _ {\bullet , \bullet} (F) \xrightarrow {\simeq} N _ {\bullet} \mathscr {D}.
$$

$\mathrm { B y }$the realization lemma, in its reflected form,$t _ { \bullet , \bullet }$is a weak homotopy equivalence.

Note that the maps$s _ { \bullet , \bullet }$and$t _ { \bullet , \bullet }$are natural in$F _ { ; }$, in the sense that the diagram

$$
\begin{array}{c} N _ {\bullet} \mathcal {C} \xleftarrow [ \simeq ]{s _ {\bullet , \bullet}} T _ {\bullet , \bullet} (F) \xrightarrow [ \simeq ]{t _ {\bullet , \bullet}} N _ {\bullet} \mathcal {D} \\ N _ {\bullet} F \Bigg \downarrow \qquad \qquad \qquad \qquad \Bigg \downarrow \qquad \qquad \qquad \Bigg \downarrow = \\ N _ {\bullet} \mathcal {D} \xleftarrow [ s _ {\bullet , \bullet} ]{\simeq} T _ {\bullet , \bullet} (i d _ {\mathcal {D}}) \xrightarrow [ t _ {\bullet , \bullet} ]{\simeq} N _ {\bullet} \mathcal {D} \end{array}
$$

commutes. The middle vertical map takes$( x , f , y )$in$T _ { m , n } ( F )$to$( F \circ x , f , y )$in $T _ { m , n } ( i d _ { \mathcal { D } } )$, realized by the diagram

$$
\begin{array}{c} F (X _ {0}) \longrightarrow \dots \longrightarrow F (X _ {m}) \\ \Big \downarrow \\ F (X _ {m}) \xrightarrow {f} Y _ {0} \longrightarrow \dots \longrightarrow Y _ {n}. \end{array}
$$

It is clear that each left fiber$i d _ { \mathcal { D } } / Y$is contractible, as this is the same as the overcategory${ \mathcal { D } } / Y$, with the terminal object id :$Y  Y$. Hence the arguments above, for$i d _ { \mathcal { D } }$in place of$F _ { \mathrm { { ; } } }$show that also the lower maps$s _ { \bullet , \bullet }$<sub>•</sub> and$t _ { \bullet , }$<sub>•</sub> are weak homotopy equivalences.

Chasing the diagram, it follows that$N _ { \bullet } F$is a weak homotopy equivalence, so$F \colon { \mathcal { C } } \to { \mathcal { D } }$is a homotopy equivalence.□

Corollary 7.3.2. Let$F \colon { \mathcal { C } }  { \mathcal { D } }$be a functor of small categories. Suppose that the right fiber$Y / F$is contractible for each object Y of$\mathcal { D }$. Then$F$is a homotopy equivalence.

Proof. This is clear from the other form of Quillen’s theorem A by duality.

Recall Definitions 4.4.1 and 4.4.2.

Corollary 7.3.3. Let$\mathcal { C }$be a precofibered (or prefibered) category over$\mathcal { D } _ { i }$, via a functor$F \colon \mathcal { C }  \mathcal { D }$, and that the fiber$F ^ { - 1 } ( Y )$is contractible for each object $Y \ o f \ \mathcal { D }$. Then$F$is a homotopy equivalence.

Proof. This is clear by the assumed existence of a left adjoint to$F ^ { - 1 } ( Y ) \to F / Y$ (or right adjoint to$F ^ { - 1 } ( Y ) \to Y / F )$, Lemma 7.1.21 and Quillen’s theorem A. □

## 7.4 Theorem$\mathbf { A } ^ { * }$

Jones, Kim, Mhoon, Santhanam, Walker and Grayson [31] extended Quillen’s proof to get a suficient condition for a functor to a product of categories to be a homotopy equivalence. This theorem$\mathrm { A ^ { * } }$can sometimes replace the use of Quillen’s more general theorem B, and its proof only relies on the realization lemma, instead of the theory of quasi-fibrations.

Theorem 7.4.1 (Theorem$\mathbf { A } ^ { * } )$. Let$F \colon \mathcal { C }  \mathcal { D }$and$G \colon { \mathcal { C } } \to { \mathcal { E } }$be functors of small categories. Suppose that the composite functor

$$
F / Y \longrightarrow \mathcal {C} \stackrel {G} {\longrightarrow} \mathcal {E}
$$

taking$( X , f \colon F ( X ) \to Y )$to$G ( X )$, is a homotopy equivalence for each object Y of D. Then$( F , G ) \colon \mathcal { C } \to \mathcal { D } \times \mathcal { E }$is a homotopy equivalence.

Proof. We keep the notation from the proof of Quillen’s theorem A, and note that$s _ { \bullet , \bullet } \colon T _ { \bullet , \bullet } ( F ) \to N _ { \bullet } \mathcal { C }$is a weak homotopy equivalence, as before.

We also decompose$T _ { \bullet , n } ( F )$for each$n \geq 0$as before:

$$
T _ {\bullet , n} (F) \cong \coprod_ {y \in N _ {n} \mathscr {D}} N _ {\bullet} (F / Y _ {0}).
$$

By hypothesis, the composite simplicial map$N _ { \bullet } ( F / Y _ { 0 } )  N _ { \bullet } \mathcal { C }  N _ { \bullet } \mathcal { C }$is a weak homotopy equivalence for each$Y _ { 0 }$in$\mathcal { D }$. Thus the simplicial map

$$
u _ {\bullet , n} \colon T _ {\bullet , n} (F) \cong \coprod_ {y \in N _ {n} \mathscr {D}} N _ {\bullet} (F / Y _ {0}) \xrightarrow {\simeq} \coprod_ {y \in N _ {n} \mathscr {D}} N _ {\bullet} \mathscr {E} \cong N _ {\bullet} \mathscr {E} \times N _ {n} \mathscr {D}
$$

taking$( x \colon [ m ] \to \mathcal { C } , f \colon F ( X _ { m } ) \to Y _ { 0 } , y \colon [ n ] \to \mathcal { D } )$to

$$
(G \circ x \colon [ m ] \to \mathcal {E}, y \colon [ n ] \to \mathcal {D})
$$

is a weak equivalence. We now view

$$
[ n ] \mapsto N _ {\bullet} \mathcal {E} \times N _ {n} \mathcal {D}
$$

as a bisimplicial set, with$( m , n )$)-simplices$N _ { m } \mathcal { E } \times N _ { n } \mathcal { D }$. This is the external product of$N _ { \bullet } \mathcal { E }$and$N _ { \bullet } \mathcal { D }$, denoted$N _ { \bullet } \mathcal { E } \boxtimes N _ { \bullet } \mathcal { D }$. Its diagonal is the usual categorical product$N _ { \bullet } \mathcal { E } \times N _ { \bullet } \mathcal { D }$in sSet.

The weak homotopy equivalences$u _ { \bullet , n }$combine to a bisimplicial map

$$
u _ {\bullet , \bullet} \colon T _ {\bullet , \bullet} (F) \xrightarrow {\simeq} N _ {\bullet} \mathcal {E} \boxtimes N _ {\bullet} \mathcal {D},
$$

and by the realization lemma,$u _ { \bullet , \bullet }$is a weak homotopy equivalence.

We now use naturality of$s _ { \bullet , \bullet }$and$u _ { \bullet , \bullet }$in$F$and$G ,$, in the sense that the diagram

$$
\begin{array}{c} N _ {\bullet} \mathcal {C} \xleftarrow [ \simeq ]{s _ {\bullet , \bullet}} T _ {\bullet , \bullet} (F) \xrightarrow [ \simeq ]{u _ {\bullet , \bullet}} N _ {\bullet} \mathcal {E} \boxtimes N _ {\bullet} \mathcal {D} \\ N _ {\bullet} (F, G) \Bigg \downarrow \qquad \qquad \qquad \qquad \Bigg \downarrow \qquad \qquad \qquad \Bigg \downarrow = \\ N _ {\bullet} (\mathcal {D} \times \mathcal {E}) \xleftarrow [ s _ {\bullet , \bullet} ]{\simeq} T _ {\bullet , \bullet} (p r _ {1}) \xrightarrow [ u _ {\bullet , \bullet} ]{\simeq} N _ {\bullet} \mathcal {E} \boxtimes N _ {\bullet} \mathcal {D} \end{array}
$$

commutes. The middle vertical map takes$( x , f , y )$to$( ( F \circ x , G \circ x ) , f , y )$in $T _ { m , n } ( p r _ { 1 } )$, realized by the diagram

$$
\begin{array}{c} (F (X _ {0}), G (X _ {0})) \longrightarrow \dots \longrightarrow (F (X _ {m}), G (X _ {m})) \\ \Biggl \downarrow \\ F (X _ {m}) \xrightarrow {f} Y _ {0} \longrightarrow \dots \longrightarrow Y _ {n}. \end{array}
$$

The lower map$u _ { \bullet , \bullet }$is associated to the projection functors$p r _ { 1 } \colon \mathcal { D } \times \mathcal { E }  \mathcal { D }$ and$p r _ { 2 } \colon \mathcal { D } \times \mathcal { E } \longrightarrow \mathcal { E }$

For each object$Y$of${ \mathcal { D } } _ { : }$the left fiber$p r _ { 1 } / Y$is isomorphic to the product category$\mathcal { D } / Y \times \mathcal { E }$, where${ \mathcal { D } } / Y$has a terminal object, so pr<sub>2</sub> :$\mathcal { D } / Y \times \mathcal { E }  \mathcal { E }$ is a homotopy equivalence, as is easily seen. Hence the arguments above also show that the lower maps$s _ { \bullet , \bullet }$and$u _ { \bullet , }$are weak homotopy equivalences.

Chasing the diagram, it follows that$N _ { \bullet } ( F , G )$is a weak homotopy equivalence, so$( F , G ) : \mathcal { C } \to \mathcal { D } \times \mathcal { E }$is a homotopy equivalence of categories.□

## 7.5 Quillen’s theorem B

[[Using Grothendieck construction and quasi-fibrations.]]

## 7.6 The simplex category

Up to weak homotopy equivalence, every simplicial set is the nerve of a small category. We shall use this to obtain Waldhausen’s versions of Quillen’s theorems$\mathrm { A } , \mathrm { A } ^ { * }$and B for simplicial maps. We follow the notation from [60, p. 308], see also [68, p. 337].

Definition 7.6.1. Let$X _ { \bullet }$be a simplicial set. The simplex category simp(X) has objects the pairs$( n , x )$, where$n \geq 0$and$x \in X _ { n }$is an n-simplex in X. A morphism$( m , y ) \to ( n , x )$in simp(X) is a morphism α :$[ m ]  [ n ]$in$\Delta$, such that$\alpha ^ { * } ( x ) = y .$

Every morphism in simp(X) has the form α :$\{ m , \alpha ^ { * } ( x ) ) \  \ ( n , x )$The composite of α and$\beta \colon ( p , \beta ^ { * } ( \alpha ^ { * } ( x ) ) )  ( m , \alpha ^ { * } ( x ) )$, with$\beta \colon [ p ]  [ m ]$in ∆, is $\alpha \beta \colon ( p , ( \alpha \beta ) ^ { * } ( x ) )  ( n , x )$

$$
\begin{array}{c} (p, (\alpha \beta) ^ {*} (x)) \xrightarrow {\beta} (m, \alpha^ {*} (x)) \xrightarrow {\alpha} (n, x) \\ \Biggl \downarrow \\ [ p ] \xrightarrow {\beta} [ m ] \xrightarrow {\alpha} [ n ] \end{array}
$$

Let$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$be a simplicial map. The simplex functor

$$
\operatorname{simp} (f) \colon \operatorname{simp} (X) \longrightarrow \operatorname{simp} (Y)
$$

takes the object$( n , x )$to the object$( n , f _ { n } ( x ) )$, and the morphism α :$( m , \alpha ^ { * } ( x ) )$ $( n , x )$to the morphism$\alpha \colon ( m , f _ { m } ( \alpha ^ { * } ( x ) ) = ( m , \alpha ^ { * } ( f _ { n } ( x ) ) ) \to ( n , f _ { n } ( x ) )$). We get a functor

$$
\operatorname{simp} \colon \mathbf {s S e t} \longrightarrow \mathbf {C a t}.
$$

[[Can view simp(X) as a category over$\Delta ,$the Grothendieck construction ${ \Delta } \wr { \bar { X }                               p } { \mathrm { ~ o f ~ } } X ^ { o p } \colon { \Delta } { \mathrm { ~  ~ } } { \mathbf { S e t } } ^ { o p } . { \mathrm { ] ] } }$

Remark 7.6.2. We can view an object$( n , x )$of$\operatorname { s i m p } ( X )$as a simplicial map $x _ { \bullet } \colon \Delta _ { \bullet } ^ { n } \to X _ { \bullet }$, and a morphism α as a commutative triangle

![](images/page_10_image_2.jpg)

in sSet. The functor simp(f) then takes an object$x _ { \bullet }$to the composite map

![](images/page_10_image_4.jpg)

Remark 7.6.3. The functor simp is not the left adjoint$\mathcal { L }$to the nerve functor. Instead, it is a kind of subdivision of this functor, with better homotopical properties.

Lemma 7.6.4. There is a natural isomorphism

$$
\operatorname * {c o l i m} _ {(n, x) \in \operatorname{simp} (X)} \Delta_ {\bullet} ^ {n} \xrightarrow {\cong} X _ {\bullet}
$$

taking$\zeta \in \Delta _ { p } ^ { n }$, in the copy indexed by$( n , x )$, to$x _ { \bullet } ( \zeta ) \in X _ { p }$

Proof. The colimit equals the coequalizer

$$
\coprod_ {\alpha : [ m ] \to [ n ]} X _ {n} \times \Delta_ {\bullet} ^ {m} \xrightarrow [ t ]{\stackrel {{s}} {{\longrightarrow}}} \coprod_ {n \geq 0} X _ {n} \times \Delta_ {\bullet} ^ {n}
$$

that we identified with$X _ { \bullet }$in Corollary 6.4.2. The inverse isomorphism takes $x \in X _ { n }$to$i d _ { [ n ] } \in \Delta _ { n } ^ { n }$in the copy indexed by$( n , x )$□

This is a special case of the general result that presheaves of sets are colimits of representable presheaves. [[How about more general topoi?]]

Definition 7.6.5. Let the last vertex map

$$
d _ {\bullet}: N _ {\bullet} \operatorname{simp} (X) \longrightarrow X _ {\bullet}
$$

be the simplicial map (see the following lemma) taking a q-simplex

$$
(n _ {0}, x _ {0}) \xrightarrow {\alpha_ {1}} (n _ {1}, x _ {1}) \xrightarrow {\alpha_ {2}} \dots \xrightarrow {\alpha_ {q}} (n _ {q}, x _ {q})\tag{7.1}
$$

in

$$
N _ {q} \operatorname{simp} (X) \cong \coprod_ {n \in N _ {q} \Delta} X _ {n (q)}
$$

to the q-simplex$\zeta ^ { * } ( x _ { q } )$of$X _ { \bullet }$, where$\zeta \colon [ q ]  [ n _ { q } ]$is given by the images of the last vertices$n _ { i } \in [ n _ { i } ]$, for$i \in [ q ]$:

$$
\zeta (i) = (\alpha_ {q} \dots \alpha_ {i + 1}) (n _ {i}).
$$

This makes sense, since$\alpha _ { i } ( n _ { i - 1 } ) \leq n _ { i }$for all$0 < i \leq q$

Remark 7.6.6. In terms of represented simplicial sets,$d _ { q }$takes the q-simplex given by the upper row

![](images/page_11_image_1.jpg)

to the diagonal arrow.

Lemma 7.6.7. The last vertex map$d _ { \bullet } \colon N _ { \bullet } \operatorname { s i m p } ( X ) \to X _ { \bullet }$is a simplicial map, natural in$X _ { \bullet }$

Proof. For each morphism$\beta \colon [ p ]  [ q ] , \beta ^ { * }$takes the q-simplex displayed in (7.1) to the p-simplex

$$
\left(n _ {\beta (0)}, x _ {\beta (0)}\right) \longrightarrow \dots \longrightarrow \left(n _ {\beta (p)}, x _ {\beta (p)}\right)
$$

with last vertex image$\xi ^ { * } ( x _ { \beta ( p ) } )$, where$\xi \colon [ p ] \ [ n _ { \beta ( p ) } ]$is given by the images of the$n _ { \beta ( j ) } \in [ n _ { \beta ( j ) } ]$for$j \in [ p ]$. Note that$\zeta \beta = \gamma \xi .$where$\gamma = \alpha _ { q } \cdot \cdot \cdot \cdot \alpha _ { \beta ( p ) + 1 }$ Hence$\beta ^ { * }$applied to the last vertex image$\zeta ^ { * } ( x _ { q } )$of the displayed$q \mathrm { - }$simplex equals$\beta ^ { * } \zeta ^ { * } ( x _ { q } ) = \xi ^ { * } \gamma ^ { * } ( x _ { q } ) = \xi ^ { * } ( x _ { \beta ( p ) } )$

If$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$is a simplicial map,$f _ { q } ( \zeta ^ { * } ( x _ { q } ) ) = \zeta ^ { * } ( f _ { n _ { q } } ( x _ { q } ) )$, hence$d _ { \bullet }$is natural.□

Example 7.6.8. Consider the case$X _ { \bullet } = N _ { \bullet } \mathcal { C }$for a small category$\mathcal { C } .$. The simplex category simp$\mathbf { \chi } ^ { \prime } X ) = \operatorname* { s i m p } ( N \mathcal { C } ) = N _ { \bullet } \mathcal { D }$is the nerve of the category$\mathcal { D }$ with objects pairs$( n , x )$with$n \geq 0$and x:$[ n ] \to \mathcal { C }$, and morphisms$\alpha \colon ( m , x \circ$ $\alpha )  ( n , x )$for α :$[ m ]  [ n ]$. There is a functor d :$\mathcal { D }  \mathcal { C }$, taking$( n , x )$to the last vertex$x ( n )$and α to$x ( \alpha ( m ) \leq n ) \colon ( x \circ \alpha ) ( m ) \to x ( n )$. The last vertex map

$$
d _ {\bullet} = N _ {\bullet} d \colon N _ {\bullet} \operatorname{simp} (N \mathcal {C}) \to N _ {\bullet} \mathcal {C}
$$

is the nerve of$d .$

[[Relate to subdivisions?]]

Lemma 7.6.9. The functor$X _ { \bullet } \mapsto N _ { \bullet } \operatorname { s i m p } ( X )$commutes with all small colim$i t s .$

Proof. Let$F \colon { \mathcal { C } } \to \mathbf { s S e t }$be a$\mathcal { C } .$-shaped diagram of simplicial sets. The natural simplicial map

$$
\underset {c \in \mathcal {C}} {\operatorname{colim}} N _ {\bullet} \operatorname{simp} (F (c)) \longrightarrow N _ {\bullet} \operatorname{simp} (\underset {c \in \mathcal {C}} {\operatorname{colim}} F (c))
$$

is given in simplicial degree q by the bijection

$$
\operatorname * {c o l i m} _ {c \in \mathcal {C}} \coprod_ {n \in N _ {q} \Delta} F (c) _ {n (q)} \xrightarrow {\cong} \coprod_ {n \in N _ {q} \Delta} \operatorname * {c o l i m} _ {c \in \mathcal {C}} F (c) _ {n (q)}.
$$

Lemma 7.6.10. The functor$X _ { \bullet } \mapsto N _ { \bullet } \operatorname { s i m p } ( X )$preserves cofibrations of simplicial sets.

Proof. If$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$is injective in each simplicial degree, then so is

$$
N _ {q} \operatorname{simp} (f) \colon \coprod_ {n \in N _ {q} \Delta} X _ {n (q)} \longrightarrow \coprod_ {n \in N _ {q} \Delta} Y _ {n (q)}
$$

for each$q \geq 0 .$

We can now represent each weak homotopy type of simplicial sets by nerves. Up to weak homotopy equivalence, the category of simplicial sets is a retract of the category of small categories. The proof is essentially that of Segal [60, p. 309] and Waldhausen [68, p. 359]. See also [70, 2.2.17].

Proposition 7.6.11. The last vertex map$d _ { \bullet } \colon N _ { \bullet } \operatorname { s i m p } ( X ) \ { \stackrel { \simeq } { \longrightarrow } } \ X _ { \bullet }$<sub>•</sub> is a weak homotopy equivalence.

Proof. When$X _ { \bullet } = \Delta _ { \bullet } ^ { n }$the simplex category simp(∆<sup>n</sup><sub>•</sub> ) has the terminal object $( n , i d _ { [ n ] } )$, hence is contractible. The simplicial map$d _ { \bullet } \colon N _ { \bullet } \operatorname { s i m p } ( \Delta _ { \bullet } ^ { n } ) \to \Delta _ { \bullet } ^ { n }$is thus trivially a weak homotopy equivalence.

Now consider a general simplicial set$X _ { \bullet } ,$viewed as the colimit of its simplicial skeleta$X _ { \bullet } ^ { ( n ) }$. For each$n \geq 0 , X _ { \bullet } ^ { ( n ) }$is the pushout of a diagram

$$
\amalg \Delta_ {\bullet} ^ {n} \longleftarrow \amalg \partial \Delta_ {\bullet} ^ {n} \longrightarrow X _ {\bullet} ^ {(n - 1)}
$$

where both coproducts range over the non-degenerate n-simplices in X. Then $N _ { \bullet } \operatorname { s i m p } ( X ^ { ( n ) } )$is the pushout of the induced diagram

$$
\coprod N _ {\bullet} \operatorname{simp} (\Delta^ {n}) \longleftarrow \coprod N _ {\bullet} \operatorname{simp} (\partial \Delta^ {n}) \longrightarrow N _ {\bullet} \operatorname{simp} (X ^ {(n - 1)})
$$

by Lemma 7.6.9. The left hand map is a cofibration of simplicial sets by Lemma 7.6.10. By induction on n and the special case considered at the outset, each map$\int N _ { \bullet } \operatorname { s i m p } ( \Delta ^ { n } ) \to \coprod \Delta _ { \bullet } ^ { n } , \ \coprod N _ { \bullet } \operatorname { s i m p } ( \partial \Delta ^ { n } ) \to \lVert \partial \Delta _ { \bullet } ^ { n }$and $N _ { \bullet }$$\left. \cdot \operatorname* { s i m p } ( X ^ { ( n - 1 ) } ) \to X _ { \bullet } ^ { ( n - 1 ) } \right.$is a weak equivalence. Hence, by the gluing lemma, $N _ { \bullet } \operatorname { s i m p } ( X ^ { ( n ) } ) \to X _ { \bullet } ^ { ( n ) }$is a weak equivalence. Passing to colimits over$n ,$using Lemma$5 . 5 . 7 , N _ { \bullet } \operatorname { s i m p } ( X ) \to X _ { \bullet }$is a weak equivalence.□

We can therefore translate Quillen’s theorems$\mathrm { A } , \mathrm { A } ^ { * }$and B to statements about simplicial sets, as in [68, 1.4.A, 1.4.B] and$\left[ 3 1 , \mathrm { p } . \ 1 8 5 \right]$. First we need the analogue of the left fiber.

Definition 7.6.12. Let$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$be a map of simplicial sets, and let$y \in Y _ { n }$ be an n-simplex, so that$( n , y )$is an object in simp(Y ). By the Yoneda lemma, Lemma 6.3.4, there is a unique characteristic map$y _ { \bullet } \colon \Delta _ { \bullet } ^ { n } \to Y _ { \bullet }$taking$i d _ { [ n ] }$to y in simplicial degree n. Let the fiber of$f _ { \bullet }$at$y$be the pullback

$$
\begin{array}{c} f _ {\bullet} / (n, y) \longrightarrow X _ {\bullet} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow f _ {\bullet} \\ \Delta_ {\bullet} ^ {n} \xrightarrow {y _ {\bullet}} Y _ {\bullet} \end{array}
$$

in sSet. We may also write$\operatorname { f i b } ( f _ { \bullet } , y )$for$f _ { \bullet } / ( n , y )$

Lemma 7.6.13 (Lemma$\mathbf { A } )$. Let$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$be a map of simplicial sets. Suppose that$f _ { \bullet } / ( n , y )$is weakly contractible for each$n \geq 0$and$y \in Y _ { n }$. Then $f _ { \bullet }$is a weak homotopy equivalence.

Proof. In view of the commutative square

$$
\begin{array}{c} N _ {\bullet} \operatorname{simp} (X) \xrightarrow [ \simeq ]{d _ {\bullet}} X _ {\bullet} \\ N _ {\bullet} \operatorname{simp} (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow f _ {\bullet} \\ N _ {\bullet} \operatorname{simp} (Y) \xrightarrow [ \simeq ]{d _ {\bullet}} Y _ {\bullet} \end{array}
$$

and Proposition 7.6.11, it sufices to prove that the functor simp(f) : simp(X) → simp$( Y )$is a homotopy equivalence.

The left fiber of this functor at an object$( n , y )$in simp(Y ) is the category with objects$( m , x , \alpha )$, where$m \geq 0 , x \in X _ { m } , \alpha \colon [ m ]  [ n ]$and$\alpha ^ { * } ( y ) = f _ { m } ( x )$ We can rewrite the latter condition as$y _ { m } ( \alpha ) = f _ { m } ( x )$, where we view α as an m-simplex in$\Delta _ { \bullet } ^ { n }$. Hence$( x , \alpha )$is precisely an m-simplex in$f _ { \bullet } / ( n , y )$. The morphisms in the left fiber category are of the form$( p , \beta ^ { * } ( x ) , \alpha \beta ) \to ( m , x , \alpha )$，for$\beta \colon [ p ]  [ m ]$. Since$\beta ^ { * } ( x , \alpha ) = ( \beta ^ { * } ( x ) , \alpha \beta )$in the simplicial set$f _ { \bullet } / ( n , y )$, these correspond precisely to the morphisms in simp$( f / ( n , y ) )$

It follows that there is an isomorphism of categories

$$
\operatorname{simp} (f) / (n, y) \cong \operatorname{simp} (f / (n, y)).
$$

Using Proposition 7.6.11 again, there is a weak homotopy equivalence

$$
N _ {\bullet} \operatorname{simp} (f / (n, y)) \xrightarrow {\simeq} f _ {\bullet} / (n, y)
$$

and by hypotheses the right hand side is weakly contractible. Hence the categories$\mathrm { s i m p } ( f / ( n , y ) )$and simp($f ) / ( n , y )$are contractible, so simp(f) is a homotopy equivalence by Quillen’s theorem A.□

Lemma 7.6.14 (Lemma$\mathbf { A } ^ { * } )$. Let$f _ { \bullet } \colon X _ { \bullet } \to Y _ { \bullet }$and$g _ { \bullet } \colon X _ { \bullet } \to Z _ { \bullet }$be maps of simplicial sets. Suppose that the composite map

$$
f _ {\bullet} / (n, y) \longrightarrow X _ {\bullet} \stackrel {g _ {\bullet}} {\longrightarrow} Z _ {\bullet}
$$

is a weak homotopy equivalence for each$( n , y )$. Then$( f _ { \bullet } , g _ { \bullet } ) \colon X _ { \bullet } \to Y _ { \bullet } \times Z _ { \bullet }$is a weak homotopy equivalence.

Proof. By Lemma 7.1.8 and Proposition 7.6.11, it sufices to prove that the functor

$$
(\operatorname{simp} (f), \operatorname{simp} (g)) \colon \operatorname{simp} (X) \xrightarrow {\simeq} \operatorname{simp} (Y) \times \operatorname{simp} (Z)
$$

is a homotopy equivalence. By theorem$\mathrm { A ^ { * } }$, it is enough to check that the composite functor

$$
\operatorname{simp} (f) / (n, y) \longrightarrow \operatorname{simp} (X) \stackrel {\operatorname{simp} (g)} {\longrightarrow} \operatorname{simp} (Z)
$$

is a homotopy equivalence, for each object$( n , y )$in simp(Y ). As in the previous proof we can identify this composite with simp applied to the two simplicial maps

$$
p _ {\bullet} \colon f _ {\bullet} / (n, y) \longrightarrow X _ {\bullet} \stackrel {g _ {\bullet}} {\longrightarrow} Z _ {\bullet}.
$$

Using Proposition 7.6.11 again, the assumption that$p _ { \bullet }$is a weak homotopy equivalence implies that simp(p) is a homotopy equivalence, as desired.□

[[

[[Lemma B.]]

## 7.7 ∞-categories

![](images/page_14_image_3.jpg)

## Chapter 8

## Waldhausen K-theory

Let$\mathcal { C }$be a category, with a suitable subcategory wC of weak equivalences. We wish to define the algebraic K-theory of$\mathcal { C }$as a based loop space$K ( \mathcal { C } ) = \Omega Y$ equipped with a loop completion map$\iota \colon | w \mathcal { C } |  K ( \mathcal { C } )$from the classifying space of the subcategory$w \mathcal { C }$. For example, each object X of$\mathcal { C }$will correspond to a point in$\vert w \mathcal { C } \vert .$, which in turn corresponds to a loop$\iota ( X ) \colon S ^ { 1 } \to Y$. We shall ask that the pairing$K ( \mathcal { C } ) \times K ( \mathcal { C } )  K ( \mathcal { C } )$given by the loop space composition $* \colon \Omega Y \times \Omega Y  \Omega Y$is compatible with a suitable extension structure on$\mathcal { C }$, in the sense that for certain pushout squares

![](images/page_15_image_3.jpg)

in$\mathcal { C } _ { : }$, expressing$X$as a kind of extension of$X ^ { \prime }$and$X ^ { \prime \prime }$, the loop$\iota ( X ) \colon S ^ { 1 } \to Y$ is homotopic to the composite of the loops$\iota ( X ^ { \prime } ) \colon S ^ { 1 } \to Y$and$\iota ( X ^ { \prime \prime } ) \colon S ^ { 1 } \to Y$

![](images/page_15_image_5.jpg)

so that$\iota ( X ) \simeq \iota ( X ^ { \prime } ) * \iota ( X ^ { \prime \prime } )$. For example, X might be the coproduct$X ^ { \prime } \vee X ^ { \prime \prime }$ of two objects in$\mathcal { C } _ { : }$, and the loop space completion map ι will then respect the monoidal pairing on$\lvert w \mathcal { C } \rvert$induced by the coproduct, since we ask that

$$
\iota (X ^ {\prime} \vee X ^ {\prime \prime}) \simeq \iota (X ^ {\prime}) * \iota (X ^ {\prime \prime}).
$$

The coherent commutativity of the categorical coproduct$( X ^ { \prime } \vee X ^ { \prime \prime } \cong X ^ { \prime \prime } \vee X ^ { \prime } )$ will imply that we get even more: the loop space$K ( \mathcal { C } ) = \Omega Y$is in fact an infinite loop space, so that$K ( \mathcal { C } )$is the underlying infinite loop space of a spectrum${ \bf K } ( \mathcal { C } )$, the algebraic K-theory spectrum of C .

We now follow Waldhausen’s foundational paper [68], to make sense of what we mean by suitable extension structures and suitable weak equivalences.

## 8.1 Categories with cofibrations

In this section we follow [68, 1.1].

Waldhausen axiomatized the extension structure, i.e., which pushout squares to consider, in terms of conditions on the horizontal map$X ^ { \prime }  X$, which determines$X ^ { \prime \prime }$as the pushout$X \cup _ { X ^ { \prime } } * = X ( X ^ { \prime }$. The allowable horizontal maps$X ^ { \prime }  X$are called cofibrations, as motivated by the similarity of the following axioms with standard properties of cofibrations for well-based spaces in homotopy theory, or for cofibrant objects in a Quillen (closed) model category [52].

Definition 8.1.1 (Pointed category). A category$\mathcal { C }$is pointed if it has a chosen zero object, i.e., an object ∗ that is both initial and terminal. Let Cat be the category of small pointed categories and functors preserving the zero objects.

We may denote a pointed category by$( \mathcal { C } , \ast )$, but usually abbreviate this to$\mathcal { C }$when the zero object is clear from the context. Given any two objects $X , Y$in$\mathcal { C }$there are then unique morphisms$X  *$and$*  Y$in$\mathcal { C } .$. Their composite$X  *  Y$is called the zero morphism from X to$Y$.

Definition 8.1.2 (Category with cofibrations). A category with cofibrations is a pointed category$( \mathcal { C } , \ast )$with a subcategory$c o \mathcal { C } \subseteq \mathcal { C }$, whose morphisms are called cofibrations and denoted$X \longmapsto Y$, such that:

(a) The isomorphisms of$\mathcal { C }$are cofibrations.

(b) For every object X in$\mathcal { C }$the unique morphism$*  X$is a cofibration.

(c) Cofibrations admit cobase change: For every cofibration$X \longmapsto Y$and every morphism$X  Z$in$\mathcal { C }$the pushout$Y \cup _ { X } Z$exists in$\mathcal { C }$, and the morphism $Z \longmapsto Y \cup _ { X } Z$is a cofibration.

![](images/page_16_image_9.jpg)

Remark 8.1.3. Conditions (a) and (b) each imply that$c o \mathcal { C }$has the same objects as$\mathcal { C } ,$so the emphasis is on the morphisms, the cofibrations. In$\mathrm { ( c ) }$ the pushouts$Y \cup _ { X } Z$are only asserted to exist, with no preferred choice being made. We denote the category with cofibrations by$( { \mathcal { C } } , c o { \mathcal { C } } )$, or just$\mathcal { C }$when the subcategory coC is clear from the context.

Definition 8.1.4 (Cofiber sequence). When$X \longmapsto Y$is a cofibration in$\mathcal { C } _ { : }$ we can form the cobase change along the unique map$X \to *$

![](images/page_16_image_12.jpg)

We write$Y / X$for the pushout$Y \cup _ { X } * ,$and call the induced map$Y \to Y / X$a quotient map. For example, the terminal map$Y  *$is a quotient map, induced by the identity cofibration$Y \longmapsto Y$. In general$Y \to Y / X$is only defined up to isomorphism in$Y / \mathcal { C }$. The quotient maps are not assumed to form a category.

A diagram of the form

$$
X \longrightarrow Y \longrightarrow Y / X,
$$

where the first map is a cofibration and the second map is an associated quotient map, is called a cofiber sequence. On the other hand, a diagram of the form

$$
X _ {1} \longmapsto X _ {2} \longmapsto \dots \longmapsto X _ {q}
$$

is called a sequence of cofibrations.

Lemma 8.1.5. A diagram isomorphic to a cofiber sequence is a cofiber sequence.

Proof. Consider a commutative diagram

![](images/page_17_image_8.jpg)

where the top row is a cofiber sequence and the vertical maps are isomorphisms. The isomorphisms${ \bar { X } } \ \mapsto \ X$and$Y \ \mapsto \ { \bar { Y } }$are cofibrations, so the composite ${ \bar { X } }  { \bar { Y } }$is a cofibration. The pushout map$\bar { Y } \cup _ { \bar { X } } *  \bar { Z }$is the composite of the isomorphisms${ \bar { Y } } \cup _ { { \bar { X } } } * \cong Y \cup _ { X } * \cong Z \cong { \bar { Z } }$, hence$\bar { X } \longmapsto \bar { Y } \twoheadrightarrow \bar { Z }$is a cofiber sequence.□

Lemma 8.1.6. Let$X \ \mapsto \ Y$be a cofibration, and suppose that the pushout $X \cup _ { W } Z$of a given diagram$X \left. W \right. Z$exists. (For example,$W  X$or $W \to Z$might be a cofibration.) Then the pushout

$$
X \cup_ {W} Z \mapsto Y \cup_ {W} Z
$$

of$X \longmapsto Y$along$W \to Z$is a cofibration.

Proof. Consider the two pushout squares:

![](images/page_17_image_14.jpg)

The pushout map in question is the cobase change of$X \ \mapsto \ Y$along$X$ $X \cup _ { W } Z ,$since$Y \cup _ { X } ( X \cup _ { W } Z ) \cong Y \cup _ { W } Z$□

Example 8.1.7. If$\mathcal { C }$is a pointed category such that for any two objects $X , Y$the pushout$X \vee Y = X \cup _ { * } Y$exists, then there is a minimal choice of a category of cofibrations coC, consisting of all morphisms that are isomorphic to the canonical inclusion$Y \longmapsto X \lor Y$. These are the cobase changes of$*  X$ along$* \to Y$. The cobase change of$Y \longmapsto X \lor Y$along$Y  Z$is the canonical inclusion$Z \longmapsto X \lor Z$

Example 8.1.8. (a) Fix a one-element set ∗, and let Set<sub>∗</sub> be the pointed category of based sets and based (= base-point preserving) functions. Let coSet be the subcategory of injective functions. Then$\mathbf { ( S e t _ { * } , } c o \mathbf { S e t _ { * } } )$is a category with cofibrations.

(b) Let$\mathbf { F i n } _ { * }$be the category of based, finite sets and based functions. Let coFin be the subcategory of injective functions. Then$\left( \mathbf { F i n } _ { * } , c o \mathbf { F i n } _ { * } \right)$is a category with cofibrations, since the pushout of finite sets is finite.

(c) Let$\mathcal { F } _ { * }$be the category with objects the finite sets

$$
n _ {+} = \{0, 1, 2, \dots , n \}
$$

for$n \geq 0$, based at$0 \in n _ { + }$, and based functions α:$m _ { + } \to n _ { + }$. Let$c o \mathcal { F } ,$∗ be the subcategory of injective functions. Then$\left( \mathcal { F } _ { * } , c o \mathcal { F } _ { * } \right)$is a small category with cofibrations, since pushouts exist within$\mathcal { F } _ { * }$

[[The category$\mathcal { F } _ { * }$agrees with Segal’s category Γ from [60], or rather the opposite category$\Gamma ^ { o p } . | |$

[[The functor$( - ) _ { + } \colon \mathcal { F }  \mathcal { F } _ { * }$taking n to$n _ { + }$induces an isomorphism of isomorphism groupoids iso$\boldsymbol { \cdot } ( \mathcal { F } ) \cong \mathrm { i s o } ( \mathcal { F } _ { \ast } ) . ] \mathrm { \Omega }$

Example 8.1.9. (a) Let G be a finite group, and let${ \cal G } { - } \mathbf { S e t }$be the category of based G-sets, with a G-fixed base point, and based G-equivariant functions. The one-element G-set ∗ is a zero object. Let coG−Set<sub>∗</sub> be the subcategory of injective functions. Then$\left( G \mathrm { - } \mathbf { S e t } _ { \ast } , c o G \mathrm { - } \mathbf { S e t } _ { \ast } \right)$is a category with cofibrations.

(b) Let$G \mathrm { - } \mathbf { F i n _ { * } }$be the category of finite based G-sets and based G-equivariant functions. Let coG−Fin be the subcategory of injective functions. Then $\left( G \mathrm { - } \mathbf { F i n _ { * } } , c o G \mathrm { - } \mathbf { F i n _ { * } } \right)$is a category with cofibrations.

(c) Let$G - { \mathcal { F } } ,$<sub>∗</sub> be the category with objects the finite sets$n _ { + }$for$n \geq 0$ equipped with a base-point preserving G-action, and based G-equivariant functions. Let$c o G \mathrm { - } \mathcal { F } _ { * }$be the subcategory of injective functions. Then $\left( G \mathrm { - } \mathbf { F i n _ { * } } , c o G \mathrm { - } \mathbf { F i n _ { * } } \right)$is a small category with cofibrations.

Definition 8.1.10 (Category with cofibrations$\mathcal { P } ( R ) )$. Let R be a ring, and let${ \mathcal { P } } ( R )$be the category of finitely generated projective (left) R-modules, and R-module homomorphisms. The zero module 0 is a zero object in${ \mathcal { P } } ( R )$ Let$c o \mathcal { P } ( R )$be the subcategory of injective R-module homomorphisms$f \colon P \mapsto$ Q such that the cokernel$Q / P$is (finitely generated) projective. The pair $( { \mathcal { P } } ( R ) , c o { \mathcal { P } } ( R ) )$is then a category with cofibrations.

To check the axioms, note that (a) the cokernel of any isomorphism$P \cong Q$ is zero, (b) the cokernel of$0  Q$is$Q ,$, which is projective, and (c) given $f \colon P \mapsto Q$with projective cokernel and any$g \colon P  L$, the pushout$Q \oplus _ { P } L$ exists as an R-module, the cokernel of$L \to Q \oplus _ { P } L$is isomorphic to$Q / P ;$, thus projective, hence$Q \oplus _ { P } L \cong ( Q / P ) \oplus L$is finitely generated projective.

![](images/page_18_image_12.jpg)

Lemma 8.1.11. The cofibrations in${ \mathcal { P } } ( R )$are precisely the split injective Rmodule homomorphisms,$i . e .$, the R-module homomorphisms$f \colon P \ \to \ Q$for which there exists a left inverse$r \colon Q \to P$with$r f = i d _ { P }$

Proof. If f is split injective, then$Q \cong P \oplus Q / P$, so$Q / P$is a direct summand of a projective module, hence projective.

$$
P \xrightarrow [ r ]{f} Q \xrightarrow [ s ]{g} Q / P
$$

Conversely, if f is injective and$Q / P$is projective then the quotient homomorphism$g \colon Q \to Q / P$admits a right inverse (= section) s, which implies that $P  Q$admits a left inverse$( = { \mathrm { r e t r a c t i o n } } ) \ r ,$with$f r + s g = i d _ { Q }$□

Definition 8.1.12 (Category with cofibrations$\mathcal { M } ( R ) )$. Let R be a ring, and let$\mathcal { M } ( R ) \ : = \ : R { - } \mathbf { M } \mathbf { o } \mathbf { d } _ { f g }$be the category of finitely generated (left) Rmodules, and R-module homomorphisms. The zero module 0 is a zero object in${ \mathcal { M } } ( R )$. Let$c o \mathcal { M } ( R )$be the subcategory of injective R-module homomorphisms$f \colon M \to N$. Then$( { \mathcal { M } } ( R ) , c o { \mathcal { M } } ( R ) )$is a category with cofibrations. [[Explain?]]

[[(Pseudo-)coherent modules?]]

Example 8.1.13. Let$R _ { f } ( * )$be the category of finite based simplicial sets, or more precisely, the finite simplicial sets$X _ { \bullet }$containing a fixed one-point simplicial set ∗ as a retract. It is pointed at the zero object ∗. Let$c o R _ { f } ( * )$be the subcategory of (degreewise) injective based simplicial maps$X _ { \bullet } \ \longmapsto \ Y _ { \bullet }$. Then $( R _ { f } ( * ) , c o R _ { f } ( * ) )$) is a category with cofibrations. For if$X _ { \bullet }  Z _ { \bullet }$is any based simplicial map, the cobase change$Z _ { \bullet } \longmapsto Y _ { \bullet } \cup _ { X _ { \bullet } } Z _ { \bullet }$can be constructed degreewise, and is degreewise injective.

This is the minimal example for Waldhausen’s algebraic K-theory of spaces. See [68, 2.1] for more general examples along these lines.

Example 8.1.14. Let R be a ring, and let$\mathcal { C } ^ { b } ( \mathcal { P } ( R ) )$be the category of bounded chain complexes of finitely generated projective R-modules, and chain maps. The objects$( P _ { * } , d )$are diagrams

$$
\dots \xrightarrow {d} P _ {n} \xrightarrow {d} P _ {n - 1} \xrightarrow {d} \dots
$$

with$d ^ { 2 } = 0$, each$P _ { n }$a finitely generated projective R-module, and$P _ { n } = 0$for all n suficiently positive or suficiently negative. The morphisms$f _ { * } \colon ( P _ { * } , d ) \to$ $( Q _ { * } , d )$are commutative diagrams

$$
\begin{array}{c} \dots \xrightarrow {d} P _ {n} \xrightarrow {d} P _ {n - 1} \xrightarrow {d} \dots \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \dots \xrightarrow {d} Q _ {n} \xrightarrow {d} Q _ {n - 1} \xrightarrow {d} \dots \end{array}
$$

The zero object is the complex of zero modules. Let$c o \mathcal { C } ^ { b } ( \mathcal { P } ( R ) )$be the subcategory of chain maps$f _ { * }$such that each$f _ { n } \colon P _ { n } \ \mapsto \ Q _ { n }$is a cofibration in ${ \mathcal { P } } ( R )$, i.e., an injective R-module homomorphism with (finitely generated) projective cokernel$Q _ { n } / P _ { n }$Equivalently, each$f _ { n }$is split injective. Then $( \mathcal { C } ^ { b } ( \mathcal { P } ( R ) ) , c o \mathcal { C } ^ { b } ( \mathcal { P } ( R ) ) )$is a category with cofibrations.

Example 8.1.15. Let R be a ring, and let$\mathcal { C } ^ { b } ( \mathcal { M } ( R ) )$be the category of bounded chain complexes of finitely generated R-modules, and chain maps. The objects$( M _ { * } , d )$are diagrams

$$
\dots \xrightarrow {d} M _ {n} \xrightarrow {d} M _ {n - 1} \xrightarrow {d} \dots
$$

with$d ^ { 2 } \ = \ 0$, each$M _ { n }$a finitely generated R-module, and$M _ { n } \ = \ 0$for all n suficiently positive or suficiently negative. The morphisms$f _ { * } \colon ( M _ { * } , d ) \to$ $( N _ { * } , d )$are commutative diagrams

$$
\begin{array}{c} \dots \xrightarrow {d} M _ {n} \xrightarrow {d} M _ {n - 1} \xrightarrow {d} \dots \\ f _ {n} \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow f _ {n - 1} \\ \dots \xrightarrow {d} N _ {n} \xrightarrow {d} N _ {n - 1} \xrightarrow {d} \dots \end{array}
$$

The zero object is the complex of zero modules. Let$c o \mathcal { C } ^ { b } ( \mathcal { M } ( R ) )$be the subcategory of chain maps$f _ { * }$such that each$f _ { n } \colon M _ { n } \mapsto N _ { n }$is a cofibration in${ \mathcal { M } } ( R )$), i.e., an injective R-module homomorphism. Then$( \mathcal { C } ^ { b } ( \mathcal { M } ( R ) ) , c o \mathcal { C } ^ { b } ( \mathcal { M } ( R ) ) )$is a category with cofibrations.

See Thomason–Trobaugh [65, §2] for many more examples of categories with cofibrations given by complexes of modules, or objects in more general abelian categories.

Definition 8.1.16 (Exact functor). Let$( { \mathcal { C } } , c o { \mathcal { C } } )$and$( { \mathcal { D } } , c o { \mathcal { D } } )$be categories with cofibrations. A functor$F \colon \mathcal { C }  \mathcal { D }$is said to be exact if it preserves all the relevant structure, i.e., if it takes ∗ to ∗ and coC to$c o \mathcal { D }$, and if for each pushout square

![](images/page_20_image_7.jpg)

in${ \mathcal { C } } _ { : }$, with$X \longmapsto Y$a cofibration, the image

![](images/page_20_image_9.jpg)

is a pushout square in D. Hence$F ( Y ) \cup _ { F ( X ) } F ( Z ) \cong F ( Y \cup _ { X } Z )$. Composites of exact functors are exact, so small categories with cofibrations and exact functors form a category. [[No notation?]]

Remark 8.1.17. In the following examples, we follow the variance conventions of ring theory, opposite to those of algebraic geometry. If a ring homomorphism$\phi \colon R  T$(of commutative rings) is viewed as a map$f \colon X \ =$ $\operatorname { S p e c } ( T ) \to \operatorname { S p e c } ( R ) = Y$of afine schemes, the functor$\phi _ { * } \colon { \mathcal { P } } ( R ) \to { \mathcal { P } } ( T )$of finitely generated projective modules corresponds to the inverse image functor $f ^ { * } \colon \mathbf { V e c } ( Y ) \to \mathbf { V e c } ( X )$of algebraic vector bundles, while$\phi ^ { * } \colon \mathcal { M } ( T )  \mathcal { M } ( R )$ corresponds to the direct image functor$f _ { * } \colon \mathbf { C o h } ( X ) \to \mathbf { C o h } ( Y )$of coherent sheaves, when defined.

Example 8.1.18. Let$\phi \colon R \to T$be a ring homomorphism. The inverse image functor$\phi _ { * } \colon { \mathcal { P } } ( R ) \to { \mathcal { P } } ( T )$takes a finitely generated projective R-module$P$ to the finitely generated projective T-module

$$
\phi_ {*} (P) = T \otimes_ {R} P.
$$

It is exact, since it maps each cofiber sequence$P  Q \Rightarrow Q / P$to a cofiber sequence

$$
T \otimes_ {R} P \mapsto T \otimes_ {R} Q \twoheadrightarrow T \otimes_ {R} (Q / P),
$$

by flatness of projective modules, which implies that for any pushout square

![](images/page_21_image_5.jpg)

with horizontal cofibrations in${ \mathcal { P } } ( R )$, the image

![](images/page_21_image_7.jpg)

is a pushout square with horizontal cofibrations in$\mathcal { P } ( T )$

Example 8.1.19. Let$\phi \colon R \to T$be a ring homomorphism, making$T$flat as a right R-module. The inverse image functor$\phi _ { * } \colon \mathcal { M } ( R ) \to \mathcal { M } ( T )$takes a finitely generated R-module M to the finitely generated T-module

$$
\phi_ {*} (M) = T \otimes_ {R} M.
$$

It is exact, since it maps each cofiber sequence$M \longmapsto N \to N / M$to a cofiber sequence

$$
T \otimes_ {R} M \mapsto T \otimes_ {R} N \twoheadrightarrow T \otimes_ {R} (N / M),
$$

by the assumed flatness of$T .$

Example 8.1.20. Let$\phi \colon R \to T$be a ring homomorphism, making T a finitely generated projective (left) R-module. The direct image functor$\phi ^ { * } \colon { \mathcal { P } } ( T ) \to$ ${ \mathcal { P } } ( R )$takes a finitely generated projective T-module$P$to the same abelian group, viewed as an R-module through φ:

$$
\phi^ {*} (P) = P.
$$

This functor is clearly exact.

Example 8.1.21. Let$\phi \colon R \to T$be a ring homomorphism, making$T$a finitely generated (left) R-module. The direct image functor$\phi ^ { * } \colon \mathcal { M } ( T )  \mathcal { M } ( R )$takes a finitely generated T-module M to the same abelian group, viewed as an$R -$ module through φ:

$$
\phi^ {*} (M) = M.
$$

This functor is clearly exact.

[[Similar constructions for categories of chain complexes.]]

Definition 8.1.22 (Subcategory with cofibrations). Let$( \mathcal { C } , c o \mathcal { C } )$and $( \mathcal { D } , c o \mathcal { D } )$be categories with cofibrations, with$\mathcal { C }$a subcategory of${ \mathcal { D } } .$We say that$\mathcal { C }$is a subcategory with cofibrations of$\mathcal { D }$if the inclusion functor${ \mathcal { C } } \subseteq { \mathcal { D } }$is exact and, furthermore, a morphism$X  Y$in$\mathcal { C }$is a cofibration in$\mathcal { C }$if (and only if) it is a cofibration in$\mathcal { D }$and the quotient$Y / X$in$\mathcal { D }$is isomorphic to an object in$\mathcal { C } .$

Example 8.1.23. Let R be a ring. The category${ \mathcal { P } } ( R )$of finitely generated projective R-modules is a subcategory with cofibrations of the category$\mathcal { M } ( R )$ of finitely generated R-modules.

The category$\mathcal { C } ^ { b } ( \mathcal { P } ( R ) )$is a subcategory with cofibrations of the category $\mathcal { C } ^ { b } ( \mathcal { M } ( R ) )$

We are very much interested in the following category$S _ { 2 } \mathcal { C }$of extensions, or cofiber sequences, in$\mathcal { C } .$. The notation will be explained in Section 8.3. Another notation for$S _ { 2 } \mathcal { C }$is$E ( \mathcal { C } )$.

Definition 8.1.24 (Category$S _ { 2 } \mathcal { C } )$. Let$S _ { 2 } \mathcal { C }$be the category with objects the cofiber sequences

$$
X ^ {\prime} \longmapsto X \longrightarrow X ^ {\prime \prime}
$$

in$( { \mathcal { C } } , c o { \mathcal { C } } )$, and morphisms from$X ^ { \prime }  X \twoheadrightarrow X ^ { \prime \prime }$to$Y ^ { \prime }  Y \twoheadrightarrow Y ^ { \prime \prime }$the commutative diagrams

![](images/page_22_image_8.jpg)

in$\mathcal { C } .$. It is pointed at the cofiber sequence$* \longmapsto * \to *$

Definition 8.1.25 (Cofibration category$c o S _ { 2 } \mathcal { C } )$. Let co$S _ { 2 } \mathcal { C } \subseteq S _ { 2 } \mathcal { C }$be the subcategory of morphism$( f ^ { \prime } , f , f ^ { \prime \prime } )$such that both$f ^ { \prime } \colon X ^ { \prime } \mapsto Y ^ { \prime }$and the pushout morphism$X \cup _ { X ^ { \prime } } Y ^ { \prime } \mapsto Y$are cofibrations in$\mathcal { C } ( =$morphisms in$c o \mathcal { C } )$

![](images/page_22_image_11.jpg)

These assumptions imply that$f \colon X \mapsto Y$and$f ^ { \prime \prime } \colon X ^ { \prime \prime } \mapsto Y ^ { \prime \prime }$are cofibrations, since$f$is the composite$X \longmapsto X \cup _ { X ^ { \prime } } Y ^ { \prime } \longmapsto Y$of the cobase change of$f ^ { \prime }$along $X ^ { \prime }  X$and the pushout morphism, and$f ^ { \prime \prime }$is the cobase change of the pushout morphism along the quotient map$X \cup _ { X ^ { \prime } } Y ^ { \prime } \twoheadrightarrow X \cup _ { X ^ { \prime } } Y ^ { \prime } / Y ^ { \prime } \cong X ^ { \prime \prime }$

Remark 8.1.26. We view objects in$S _ { 2 } \mathcal { C }$as short filtrations$X ^ { \prime } \mapsto X$in$\mathcal { C } .$ together with a choice of filtration quotient$X  X ^ { \prime \prime }$. A cofibration$( f ^ { \prime } , f , f ^ { \prime \prime } )$ is then a bifiltered object, or lattice, in$\mathcal { C }$, together with choices of quotients. As

Waldhausen comments, the lattice condition that$X \cup _ { X ^ { \prime } } Y ^ { \prime } \longmapsto Y$is a cofibration serves as a replacement for the condition that$X ^ { \prime }$is the pullback of X and$Y ^ { \prime }$ in$Y .$, which does not generally make sense in the present context.

Definition 8.1.27 (Lattice square). A commutative square

![](images/page_23_image_2.jpg)

is a lattice square if$X ^ { \prime }  X , X ^ { \prime }  Y ^ { \prime }$and the pushout morphism$X \cup _ { X ^ { \prime } } Y ^ { \prime } \mapsto$ $Y$are all cofibrations. We indicate this by the central label$^ { 6 6 } L ^ { 3 }$. [[Consider using$\boxed { \begin{array} { r l } \end{array} }$in place of$L . ] ]$It follows that$X \longmapsto Y$and$Y ^ { \prime } \longmapsto Y$are cofibrations.

Proposition 8.1.28.$( S _ { 2 } \mathcal { C } , c o S _ { 2 } \mathcal { C } )$is a category with cofibrations.

Proof. To see that$c o S _ { 2 } \mathcal { C }$is category, consider the diagram

![](images/page_23_image_6.jpg)

where$f ^ { \prime } , g ^ { \prime } , X \cup _ { X ^ { \prime } } Y ^ { \prime } \longmapsto Y$and$Y \cup _ { Y ^ { \prime } } Z ^ { \prime } \longmapsto Z$are cofibrations. Then$g ^ { \prime } f ^ { \prime }$is obviously a cofibration, and the pushout morphism$X \cup _ { X ^ { \prime } } Z ^ { \prime }  Z$factors as the composite

$$
X \cup_ {X ^ {\prime}} Z ^ {\prime} \mapsto Y \cup_ {Y ^ {\prime}} Z ^ {\prime} \mapsto Z
$$

of the pushout of$X \cup _ { X ^ { \prime } } Y ^ { \prime } \longmapsto Y$along$g ^ { \prime } \colon Y ^ { \prime } \to Z ^ { \prime }$(using Lemma 8.1.6), and $Y \cup _ { Y ^ { \prime } } Z ^ { \prime } \longmapsto Z$, hence is a cofibration.

To see that cofibrations in$S _ { 2 } \mathcal { C }$admits cobase change, consider the diagram

![](images/page_23_image_11.jpg)

(8.1)

where$f ^ { \prime }$and$X \cup _ { X ^ { \prime } } Y ^ { \prime } \longmapsto Y$are cofibrations, viewed a vertical cofibration $( f ^ { \prime } , f , f ^ { \prime \prime } )$and a vertical morphism$( g ^ { \prime } , g , g ^ { \prime \prime } )$in$S _ { 2 } \mathcal { C }$. As discussed above, it follows that$f$and$f ^ { \prime \prime }$are cofibrations, so the pushouts$Y ^ { \prime } \cup _ { X ^ { \prime } } Z ^ { \prime } , Y \cup _ { X } Z$and $Y ^ { \prime \prime } \cup _ { X ^ { \prime \prime } } Z ^ { \prime \prime }$all exist in$\mathcal { C }$. To see that the induced diagram

$$
Y ^ {\prime} \cup_ {X ^ {\prime}} Z ^ {\prime} \longrightarrow Y \cup_ {X} Z \longrightarrow Y ^ {\prime \prime} \cup_ {X ^ {\prime \prime}} Z ^ {\prime \prime}
$$

is the pushout in$S _ { 2 } \mathcal { C }$of the diagram above, we need to check that the left hand morphism is a cofibration, and that the right hand morphism is the associated quotient map.

The left hand morphism is the composite of the pushout

$$
Y ^ {\prime} \cup_ {X ^ {\prime}} Z ^ {\prime} \mapsto Y ^ {\prime} \cup_ {X ^ {\prime}} Z
$$

of$Z ^ { \prime } \mapsto Z$along$f ^ { \prime } \colon X ^ { \prime } \to Y ^ { \prime }$, and the pushout

$$
Y ^ {\prime} \cup_ {X ^ {\prime}} Z \cong (Y ^ {\prime} \cup_ {X ^ {\prime}} X) \cup_ {X} Z \mapsto Y \cup_ {X} Z
$$

of$Y ^ { \prime } \cup _ { X ^ { \prime } } X \longmapsto Y$along$g \colon X \to Z ,$hence is a cofibration. To see that the right hand morphism is a quotient map, we compute the colimit of the diagram

![](images/page_24_image_5.jpg)

in two diferent ways: Taking vertical colimits first and horizontal colimits thereafter leads to$( Y \cup _ { X } Z ) / ( Y ^ { \prime } \cup _ { X ^ { \prime } } Z ^ { \prime } )$, while taking horizontal colimits first and vertical colimits thereafter leads to$Y ^ { \prime \prime } \cup _ { X ^ { \prime \prime } } Z ^ { \prime \prime }$, as desired.

Lastly, we need to check that the cobase change

![](images/page_24_image_8.jpg)

of the cofibration$( f ^ { \prime } , f , f ^ { \prime \prime } )$along$( g ^ { \prime } , g , g ^ { \prime \prime } )$is a cofibration in$S _ { 2 } \mathcal { C }$, i.e., that $Z ^ { \prime } \longmapsto Y ^ { \prime } \cup _ { X ^ { \prime } } Z ^ { \prime }$and

$$
\left(Y ^ {\prime} \cup_ {X ^ {\prime}} Z ^ {\prime}\right) \cup_ {Z ^ {\prime}} Z \cong Y ^ {\prime} \cup_ {X ^ {\prime}} Z \mapsto Y \cup_ {X} Z
$$

are cofibrations. The first is the cobase change of$f ^ { \prime } \colon X ^ { \prime } \mapsto Y ^ { \prime }$along$g ^ { \prime } \colon X ^ { \prime } \to$ $Z ^ { \prime }$, so this is clear. The second is the pushout of$Y ^ { \prime } \cup _ { X ^ { \prime } } X \longmapsto Y$along$g \colon X \to Z ,$ so this is also clear.□

Lemma 8.1.29. The source, target and quotient functors$s , t , q \colon S _ { 2 } \mathcal { C } \to \mathcal { C }$ taking$X ^ { \prime } \left. X \right. X ^ { \prime \prime }$to$X ^ { \prime }$, X and$X ^ { \prime \prime }$, respectively, are all exact.

Proof. The requisite conditions, which the reader should identify, have all been checked in the previous proof.□

Lemma 8.1.30. An exact functor$F \colon ( \mathcal { C } , c o \mathcal { C } )  ( \mathcal { D } , c o \mathcal { D } )$induces an exact functor$S _ { 2 } F \colon ( S _ { 2 } \mathcal { C } , c o S _ { 2 } \mathcal { C } )  ( S _ { 2 } \mathcal { D } , c o S _ { 2 } \mathcal { D } )$

Proof. The functor$S _ { 2 } F \colon S _ { 2 } \mathcal { C } \to S _ { 2 } \mathcal { D }$takes a cofiber sequence$X ^ { \prime }  X \twoheadrightarrow X ^ { \prime \prime }$ to$F ( X ^ { \prime } ) \ \longmapsto \ F ( X ) \ \twoheadrightarrow \ F ( X ^ { \prime \prime } )$, which is again a cofiber sequence by exactness. If$( f ^ { \prime } , f , f ^ { \prime \prime } )$is a cofibration in$S _ { 2 } \mathcal { C }$, then$F ( f ^ { \prime } ) \colon F ( X ^ { \prime } ) \longmapsto F ( Y ^ { \prime } )$and

$F ( X ) \cup _ { F ( X ^ { \prime } ) } F ( Y ^ { \prime } ) \cong F ( X \cup _ { X ^ { \prime } } Y ^ { \prime } ) \longmapsto F ( Y )$are cofibrations, again by exactness, so$( F ( f ^ { \prime } ) , F ( f ) , F ( f ^ { \prime \prime } )$is a cofibration in$S _ { 2 } \mathcal { D }$. Applying$S _ { 2 } F$to the diagram (8.1), we get the diagram

$$
F (Y ^ {\prime}) \longmapsto F (Y) \longrightarrow F (Y ^ {\prime \prime})
$$

$$
F (f ^ {\prime}) \Bigg \uparrow \qquad L \qquad \Bigg \uparrow F (f) \qquad \qquad \Bigg \uparrow F (f ^ {\prime \prime})
$$

$$
F (X ^ {\prime}) \longmapsto F (X) \longrightarrow F (X ^ {\prime \prime})
$$

$$
F (g ^ {\prime}) \Bigg \downarrow \qquad \qquad \Bigg \downarrow F (g) \qquad \qquad \Bigg \downarrow F (g ^ {\prime \prime})
$$

$$
F (Z ^ {\prime}) \longmapsto F (Z) \longrightarrow F (Z ^ {\prime \prime})
$$

with pushout

$$
F (Y ^ {\prime}) \cup_ {F (X ^ {\prime})} F (Z ^ {\prime}) \longmapsto F (Y) \cup_ {F (X)} F (Z) \longrightarrow F (Y ^ {\prime \prime}) \cup_ {F (X ^ {\prime \prime})} F (Z ^ {\prime \prime})
$$

isomorphic to$S _ { 2 } F$applied to the pushout of diagram (8.1).

[[Also consider$\bar { S } _ { 2 } \mathcal { C }$, forgetting quotients?]]

Lemma 8.1.31. The (categorical) product of two categories with cofibrations $( \mathcal { D } , c o \mathcal { D } )$and (E, coE) is$( \mathcal { D } \times \mathcal { E } , c o \mathcal { D } \times c o \mathcal { E } )$. More generally, if$F \colon { \mathcal { D } }  { \mathcal { C } }$ and$G \colon { \mathcal { E } } \to { \mathcal { C } }$are exact functors, the pullback of

$$
\left(\mathscr {D}, c o \mathscr {D}\right) \xrightarrow {F} \left(\mathscr {C}, c o \mathscr {C}\right) \xleftarrow {G} \left(\mathscr {E}, c o \mathscr {E}\right)
$$

is$( { \mathcal { D } } \times \mathcal { C } ~ { \mathcal { E } } ^ { \mathcal { O } }$, co$\mathcal { D } \times _ { c o \mathcal { C } } c o \mathcal { E } )$, consisting of pairs$f \colon X ^ { \prime } \mapsto X$and$g \colon Y ^ { \prime } \mapsto Y$of cofibrations in$\mathcal { D }$and$\boldsymbol { \mathcal { E } } _ { : } ^ { \circ }$, respectively, with$F ( f ) = G ( g )$in$\mathcal { C }$.

[[Clear?]]

Lemma 8.1.32. Let$( \mathcal { C } , c o \mathcal { C } )$be a category with cofibrations. The coproduct functor

$$
\vee : (\mathscr {C}, c o \mathscr {C}) \times (\mathscr {C}, c o \mathscr {C}) \longrightarrow (\mathscr {C}, c o \mathscr {C})
$$

taking (X, Y ) to$X \vee Y = X \cup _ { * } Y$is exact.

[[Clear?]]

Definition 8.1.33 (Category of extensions$E ( \mathcal { D } , \mathcal { C } , \mathcal { E } ) )$. Let$\mathcal { C } , \mathcal { D } , \mathcal { E }$be categories with cofibrations, and suppose that$\mathcal { D } \subseteq \mathcal { C }$and${ \mathcal { E } } ^ { \circ } \subseteq { \mathcal { C } }$are exact inclusion functors of subcategories. Let$E ( \mathcal { D } , \mathcal { C } , \mathcal { E } )$be the category of cofiber sequences

$$
X \mapsto Y \twoheadrightarrow Z
$$

in${ \mathcal { C } } _ { : }$, with X in$\mathcal { D }$and$Z$in$\mathcal { E } ^ { \mathcal { C } } .$. It is the pullback of the diagram

$$
\begin{array}{c} E (\mathcal {D}, \mathcal {C}, \mathcal {E}) \xrightarrow {} \mathcal {D} \times \mathcal {E} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \\ S _ {2} \mathcal {C} \xrightarrow {(s , q)} \mathcal {C} \times \mathcal {C}. \end{array}
$$

As a special case,$E ( \mathcal { C } , \mathcal { C } , \mathcal { C } ) = E ( \mathcal { C } ) = S _ { 2 } \mathcal { C } ,$

Lemma 8.1.34.$E ( \mathcal { D } , \mathcal { C } , \mathcal { E } )$is a category with cofibrations, and the inclusion functor$E ( { \mathcal { D } } , { \mathcal { C } } , { \mathcal { E } } ) \subseteq S _ { 2 } { \mathcal { C } }$is exact.

[[Fiber products, colimits of categories with cofibrations.]]

Definition 8.1.35 (Fiber product). Let$F \colon { \mathcal { D } }  { \mathcal { C } }$and$G \colon { \mathcal { E } } \ \to \ { \mathcal { C } }$be functors. The fiber product$\mathcal { D } \times _ { \mathcal { C } } ^ { i } \ \mathcal { E } ^ { \mathcal { C } }$is the category with objects$( X , h , Y )$ with X and$Y$objects in$\mathcal { D }$and${ \mathcal { E } } ,$, respectively, and$h \colon F ( X ) \ \cong \ G ( Y )$an isomorphism in$\mathcal { C } .$A morphism$( f , g ) \colon ( X , h , Y ) \to ( X ^ { \prime } , h ^ { \prime } , Y ^ { \prime } )$is a pair of morphisms$f \colon X \to X ^ { \prime }$and$g \colon Y \to Y ^ { \prime }$in$\mathcal { D }$and${ \mathcal { E } } ,$respectively, such that the square

$$
\begin{array}{c} F (X) \xrightarrow [ \cong ]{h} G (Y) \\ F (f) \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow G (g) \\ F (X ^ {\prime}) \xrightarrow [ \cong ]{h ^ {\prime}} G (Y ^ {\prime}) \end{array}
$$

commutes in$\mathcal { C }$. There are projection functors$p r _ { 1 } \colon \mathcal { D } \times _ { \mathcal { C } } ^ { i } \mathcal { E } \longrightarrow \mathcal { D }$and$p r _ { 2 } \colon \mathcal { D } \times _ { \mathcal { C } } ^ { i }$ $\mathcal { E } ^ { \mathcal { O } }  \mathcal { E } ^ { \mathcal { O } } ,$, and the two composites$F \circ p r _ { 1 } , G \circ p r _ { 2 } \colon \mathscr { D } \times _ { \mathcal { C } } ^ { i } \mathcal { E }  \mathcal { C }$are naturally isomorphic. [[Continue with cofibration structure.]]

## 8.2 Categories of weak equivalences

In this section we follow [68, 1.2]

In forming the algebraic K-theory of a category$\mathcal { C } _ { : }$we wish to view certain objects in$\mathcal { C }$as “equivalent”. Waldhausen axiomatized this equivalence structure in terms of a subcategory w$\mathcal { C } \subseteq \mathcal { C }$of weak equivalences, so that the equivalent pairs of objects are precisely those that can be connected by a finite chain of morphisms in$w \mathcal { C }$. At the level of classifying spaces, this means that we view points in the same path component of$| w \mathcal { C } |$as equivalent.

Definition 8.2.1 (Category of weak equivalences). Let$\mathcal { C }$be a category with cofibrations. A category of weak equivalences in$\mathcal { C }$is a subcategory$w \mathcal { C } \subseteq$ $\mathcal { C } _ { : }$, whose morphisms are denoted$X \xrightarrow { \sim } Y$, such that:

(a) The isomorphisms of$\mathcal { C }$are weak equivalences.

(b) The gluing lemma holds: Given a commutative diagram

![](images/page_26_image_11.jpg)

where the two horizontal morphisms on the left are cofibrations and the three vertical morphisms are weak equivalences, then the pushout morphism

$$
Y \cup_ {X} Z \stackrel {\sim} {\longrightarrow} \bar {Y} \cup_ {\bar {X}} \bar {Z}
$$

is also a weak equivalence.

Remark 8.2.2. Condition (a) implies that$w \mathcal { C }$has the same objects as$\mathcal { C }$ so again the emphasis is on the morphisms, the weak equivalences. Note that condition (b) depends on the implicit subcategory coC of cofibrations in$\mathcal { C }$

Definition 8.2.3 (Waldhausen category). A category with cofibrations and weak equivalences$\mathbf { \tau } ( = \mathrm { a }$Waldhausen category) is a category with cofibrations $( { \mathcal { C } } , c o { \mathcal { C } } )$with a chosen category of weak equivalences wC. We usually abbreviate$( \mathcal { C } , c o \mathcal { C } , w \mathcal { C } )$to$( \mathcal { C } , w \mathcal { C } )$

Example 8.2.4. The minimal example of a category of weak equivalences is the isomorphism subcategory, which we in this context denote as$i \mathcal { C } = \mathrm { i s o } ( \mathcal { C } ) \subseteq$ $\mathcal { C } .$. This is the standard choice of weak equivalences on the categories with cofibrations$\mathcal { F } _ { * } , \mathcal { P } ( R )$and${ \mathcal { M } } ( R )$. These make$( \mathcal { F } _ { * } , i \mathcal { F } _ { * } ) , ~ ( \mathcal { P } ( R ) , i \mathcal { P } ( R ) )$ and$( { \mathcal { M } } ( R ) , i { \mathcal { M } } ( R ) )$into Waldhausen categories.

Example 8.2.5. Let$h R _ { f } ( * ) \subset R _ { f } ( * )$be the subcategory of based simplicial maps$X _ { \bullet } \xrightarrow { \sim } Y _ { \bullet }$that are weak homotopy equivalences. Then$( R _ { f } ( * ) , h R _ { f } ( * ) )$is a Waldhausen category. To prove the gluing lemma, apply CW realization and use the gluing lemma for topological spaces and homotopy equivalences, using Lemma 6.3.28.

Example 8.2.6. Let$s R _ { f } ( * ) \subset R _ { f } ( * )$be the subcategory of based simplicial maps$X _ { \bullet } \xrightarrow { \sim _ { s } } Y _ { \bullet }$that are simple maps, meaning that the point inverses of$| X _ { \bullet } |$ $| Y _ { \bullet } |$are all contractible. Then$( R _ { f } ( * ) , s R _ { f } ( * ) )$is a Waldhausen category. The fact that$s R _ { f } ( * )$is closed under composition, and the requisite gluing lemma, are proved in [70, Prop. 2.1.3(d)].

Example 8.2.7. Let$q \mathcal { C } ^ { b } ( \mathcal { P } ( R ) ) \subseteq \mathcal { C } ^ { b } ( \mathcal { P } ( R ) )$be the subcategory of chain maps$f _ { * } \colon P _ { * } \ \xrightarrow { \sim } \ Q ,$<sub>∗</sub> that are quasi-isomorphisms,$\mathrm { i . e . }$, that induce isomorphisms$f _ { * } \colon H _ { n } ( P _ { * } ) \ \to \ H _ { n } ( Q _ { * } )$on homology in all degrees$n \in \mathbb { Z }$. Then $( \mathcal { C } ^ { b } ( \mathcal { P } ( R ) ) , q \mathcal { C } ^ { b } ( \mathcal { P } ( R ) ) )$is a Waldhausen category. To prove the gluing lemma, construct and use the long exact Mayer–Vietoris sequence

$$
\dots \to H _ {n} (P _ {*}) \to H _ {n} (Q _ {*}) \oplus H _ {n} (L _ {*}) \to H _ {n} (Q _ {*} \oplus_ {P _ {*}} L _ {*}) \xrightarrow {\partial} H _ {n - 1} (P _ {*}) \to \ldots .
$$

Example 8.2.8. Let$q \mathcal { C } ^ { b } ( \mathcal { M } ( R ) ) \subseteq \mathcal { C } ^ { b } ( \mathcal { M } ( R ) )$) be the subcategory of quasi-isomorphisms$f _ { * } \colon M _ { * } \ \xrightarrow { \sim } { N _ { * } }$. Then$( \mathcal { C } ^ { b } ( \mathcal { M } ( R ) ) , q \mathcal { C } ^ { b } ( \mathcal { M } ( R ) ) )$is a Waldhausen category.

[[Perfect complexes.]]

[[Saturation axiom, extension axiom.]]

Definition 8.2.9 (Exact functor). A functor$F \colon ( \mathcal { C } , w \mathcal { C } ) \to ( \mathcal { D } , w \mathcal { D } )$between Waldhausen categories is exact if it preserves all relevant structure, i.e., if it is exact as a functor between categories with cofibrations and, furthermore, it takes$w \mathcal { C }$to$w \mathcal { D }$. The composite of two exact functors is exact. We get a category Wald of small Waldhausen categories and exact functors.

Example 8.2.10. In Examples 8.1.18 through 8.1.21, φ and$\phi ^ { * }$are exact as functors of Waldhausen categories (with isomorphisms as weak equivalences) whenever they are defined and exact as functors of categories with cofibrations. For example, the inverse image functor

$$
\phi_ {*} \colon (\mathcal {P} (R), i \mathcal {P} (R)) \longrightarrow (\mathcal {P} (T), i \mathcal {P} (T))
$$

is exact for each ring homomorphism$\phi \colon R \to T$

Example 8.2.11. In Examples 8.2.5 and 8.2.6, each simple map is a weak homotopy equivalence, so the identity functor on$R _ { f } ( * )$defines an exact functor $( R _ { f } ( \ast ) , s R _ { f } ( \ast ) )  ( R _ { f } ( \ast ) , h R _ { f } ( \ast ) )$.

Definition 8.2.12 (Waldhausen subcategory). Let$( \mathcal { C } , w \mathcal { C } )$and$( \mathcal { D } , w \mathcal { D } )$ be Waldhausen categories, and suppose that$( \mathcal { C } , c o \mathcal { C } )$is a subcategory with cofibrations of$( \mathcal { D } , c o \mathcal { D } )$. We say that$\mathcal { C }$is a subcategory with cofibrations and weak equivalences$( = \mathrm { a }$Waldhausen subcategory) if the inclusion functor${ \mathcal { C } } \subseteq { \mathcal { D } }$ is exact and, furthermore, a morphism$X  Y$in$\mathcal { C }$is a weak equivalence in$\mathcal { C }$ if (and only if) it is a weak equivalence in${ \mathcal { D } } .$

Example 8.2.13. Let R be a ring. The Waldhausen category$( \mathcal { P } ( R ) , i \mathcal { P } ( R ) )$ of finitely generated projective R-modules and isomorphisms is a Waldhausen subcategory of the Waldhausen category$( { \mathcal { M } } ( R ) , i { \mathcal { M } } ( R ) )$of finitely generated R-modules and isomorphisms.

The Waldhausen category$( \mathcal { C } ^ { b } ( \mathcal { P } ( R ) ) , q \mathcal { C } ^ { b } ( \mathcal { P } ( R ) ) )$is a Waldhausen subcategory of the Waldhausen category$( { \mathcal { C } } ^ { b } ( { \mathcal { M } } ( R ) ) , q { \mathcal { C } } ^ { b } ( { \mathcal { M } } ( R ) ) )$).

[[Example: Compact objects in a closed model category.]]

Definition 8.2.14 (Weak equivalence category$w S _ { 2 } \mathcal { C } )$. Let w$S _ { 2 } { \mathcal { C } } \subseteq S _ { 2 } { \mathcal { C } }$ be the subcategory of morphisms$( f ^ { \prime } , f , f ^ { \prime \prime } )$such that both$f ^ { \prime } \colon X ^ { \prime } \xrightarrow { \sim } Y ^ { \prime }$and $f \colon X \xrightarrow { \sim } Y$are weak equivalences in$\mathcal { C } ( =$morphisms in$w \mathcal { C } )$).

![](images/page_28_image_6.jpg)

These assumptions imply that$f ^ { \prime \prime } \colon X ^ { \prime \prime } \ \xrightarrow { \sim } \ Y ^ { \prime \prime }$is a weak equivalence by the gluing lemma, since$f ^ { \prime \prime }$is the pushout morphism

$$
X \cup_ {X ^ {\prime}} * \stackrel {{\sim}} {{\longrightarrow}} Y \cup_ {Y ^ {\prime}} *
$$

of$f$and$* \xrightarrow { \sim } *$along$f ^ { \prime } .$

Proposition 8.2.15.$( S _ { 2 } \mathcal { C } , w S _ { 2 } \mathcal { C } )$is a Waldhausen category.

Proof. We must check the gluing lemma. Consider a vertical map from diagram (8.1), where$f ^ { \prime } \colon X ^ { \prime } \mapsto Y ^ { \prime }$and$X \cup _ { X ^ { \prime } } Y ^ { \prime } \longmapsto Y$are cofibrations, to the diagram

![](images/page_28_image_12.jpg)

where$\bar { f } ^ { \prime } \colon \bar { X } ^ { \prime } \mapsto \bar { Y } ^ { \prime }$and${ \bar { X } } \cup _ { \bar { X } ^ { \prime } } { \bar { Y } } ^ { \prime } \longmapsto { \bar { Y } }$are cofibrations, such that each of the maps$\check { Y } ^ { \prime } \ \stackrel { \sim } { \longrightarrow } \ \bar { Y } ^ { \prime } , \ Y \ \stackrel { \sim } { \longrightarrow } \ \bar { Y } , \ \stackrel { \sim } { X } ^ { \prime } \ \stackrel { \sim } { \longrightarrow } \ \bar { X } ^ { \prime } , \ X \ \stackrel { \sim } { \longrightarrow } \ \bar { X } , \ Z ^ { \prime } \ \stackrel { \sim } { \longrightarrow } \ \bar { Z } ^ { \prime }$and$Z \longrightarrow \bar { Z }$ are weak equivalences. Then by the gluing lemma in$\mathcal { C }$the pushout maps

$Y ^ { \prime } \cup _ { X ^ { \prime } } Z ^ { \prime } \xrightarrow { \sim } \bar { Y } ^ { \prime } \cup _ { \bar { X } ^ { \prime } } \bar { Z } ^ { \prime }$and$Y \cup _ { X } Z \xrightarrow { \sim } \bar { Y } \cup _ { \bar { X } } \bar { Z }$are weak equivalences. Hence the vertical pushout map

![](images/page_29_image_1.jpg)

is a weak equivalence in$S _ { 2 } \mathcal { C }$

Lemma 8.2.16. The source, target and quotient functors$s , t , q \colon ( S _ { 2 } \mathcal { C } , w S _ { 2 } \mathcal { C } )$ $( \mathcal { C } , w \mathcal { C } )$, taking$X ^ { \prime } \left. X \right. X ^ { \prime \prime }$to$X ^ { \prime } , X$and$X ^ { \prime \prime }$, respectively, are all exact.

Proof. If$( f ^ { \prime } , f , f ^ { \prime \prime } )$is a weak equivalence in$S _ { 2 } \mathcal { C } _ { \bf { \theta } }$, we have already seen that$f ^ { \prime } ,$ $f$and$f ^ { \prime \prime }$are weak equivalences in$\mathcal { C }$□

Lemma 8.2.17. An exact functor$F \colon ( \mathcal { C } , w \mathcal { C } ) \to ( \mathcal { D } , w \mathcal { C } )$induces an exact functor$S _ { 2 } F \colon ( S _ { 2 } \mathcal { C } , w S _ { 2 } \mathcal { C } )  ( S _ { 2 } \mathcal { D } , w S _ { 2 } \mathcal { D } )$

Proof. Given a weak equivalence$( f ^ { \prime } , f , f ^ { \prime \prime } )$in$S _ { 2 } \mathcal { C }$, its image$( F ( f ^ { \prime } ) , F ( f ) , F ( f ^ { \prime \prime } ) )$ is clearly a weak equivalence in$S _ { 2 } \mathcal { D }$, since F preserves weak equivalences.

Lemma 8.2.18. The (categorical) product oftwo Waldhausen categories$( \mathcal { D } , w \mathcal { D } )$ and$( \mathcal { E } , w \mathcal { E } ) \ i s \ ( \mathcal { D } \times \mathcal { E } , w \mathcal { D } \times w \mathcal { E } )$. More generally, if F and G are exact functors, the pullback$o f$

$$
(\mathcal {D}, w \mathcal {D}) \xrightarrow {F} (\mathcal {C}, w \mathcal {C}) \xleftarrow {G} (\mathcal {E}, w \mathcal {E})
$$

is$\left( \mathcal { D } \times _ { \mathcal { C } } \mathcal { E } , w \mathcal { D } \times _ { w \mathcal { C } } w \mathcal { E } \right)$, consisting of pairs$f \colon X ^ { \prime } \xrightarrow { \sim } X$and$g \colon Y ^ { \prime } \xrightarrow { \sim } Y$of weak equivalences in$\mathcal { D }$and$\boldsymbol { \mathcal { E } } _ { : } ^ { \circ }$, respectively, with$F ( f ) = G ( g )$in$\mathcal { C }$

[[Clear?]]

Lemma 8.2.19. Let$\mathcal { C } , \mathcal { D } , \mathcal { E }$be Waldhausen categories, and suppose that$\mathcal { D } \subseteq$ $\mathcal { C }$and${ \mathcal { E } } ^ { \mathcal { O } } \subseteq { \mathcal { C } }$are exact inclusion functors. Then$E ( \mathcal { D } , \mathcal { C } , \mathcal { E } )$is a Waldhausen category, and the inclusion functor$E ( \mathcal { D } , \mathcal { C } , \mathcal { E } ) \subseteq S _ { 2 } \mathcal { C }$is exact.

[[Clear?]]

Lemma 8.2.20. Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. The coproduct functor

$$
\vee \colon (\mathcal {C}, w \mathcal {C}) \times (\mathcal {C}, w \mathcal {C}) \longrightarrow (\mathcal {C}, w \mathcal {C})
$$

taking (X, Y ) to$X \vee Y = X \cup _ { * } Y$is exact.

Proof. If$( X , Y ) \ { \stackrel { \sim } { \longrightarrow } } \ ( { \bar { X } } , { \bar { Y } } )$is a weak equivalence, each map$X \xrightarrow { \sim } \bar { X }$and $Y \xrightarrow { \sim } \bar { Y }$is a weak equivalence, so by the gluing lemma applied to the diagram

![](images/page_29_image_17.jpg)

the pushout map$X \vee Y { \overset { \sim } { \longrightarrow } } { \bar { X } } \vee { \bar { Y } }$is a weak equivalence.

Lemma 8.2.21. The topological realization

$$
| \vee |: | w \mathcal {C} | \times | w \mathcal {C} | \cong | w \mathcal {C} \times w \mathcal {C} | \longrightarrow | w \mathcal {C} |
$$

induces the homomorphism

$$
\pi_ {i} | \vee |: \pi_ {i} | w \mathscr {C} | \times \pi_ {i} | w \mathscr {C} | \longrightarrow \pi_ {i} | w \mathscr {C} |
$$

taking$( x , y )$to$x + y$in the group structure on$\pi _ { i } | w \mathcal { C } | , f o r \ : i \geq 1$. In particular, $\pi _ { 1 } | w \mathcal { C } |$is abelian. The same pairing makes$\pi _ { 0 } | w \mathcal { C } |$a commutative monoid.

Proof. The natural isomorphisms$* \vee X \cong X \cong X \vee *$lead to the commutative diagram

![](images/page_30_image_6.jpg)

in Cat. For$i \geq 1$, let$G = \pi _ { i } | w \mathcal { C } |$with neutral element 0. Then$\pi _ { i } | \vee | : G \times G \longrightarrow$ $G$is a group homomorphism, mapping$( 0 , y ) \mapsto y$and$( x , 0 ) \mapsto x$. The product of$( x , 0 )$and$( 0 , y )$, in either order, equals$( x , y )$, hence$( x , y ) \mapsto x + y = y + x$ In particular G is abelian for$i = 1$. When$i = 0$let$M = \pi _ { 0 } | w \mathcal { C } |$. The pairing $\pi _ { 0 } | \vee | \colon M \times M \to M$defines a monoid structure on$M ,$with neutral element the class of the zero object ∗. It is commutative and associative, due to the isomorphisms$X \vee Y \cong Y \vee X$and$( X \vee Y ) \vee Z \cong X \vee ( Y \vee Z )$□

Exercise 8.2.22. Compute the commutative monoids$\pi _ { 0 } | i \mathcal { P } ( \mathbb { Z } ) |$| and$\pi _ { 0 } | i { \mathcal { M } } ( \mathbb { Z } ) |$, and the homomorphism induced by the inclusion$i \mathcal { P } ( \mathbb { Z } ) \subset i \mathcal { M } ( \mathbb { Z } )$

[[Fiber products, colimits of Waldhausen categories?]]

## 8.3 The S<sub>•</sub>-construction

This section is based on [68, 1.3].

The objects of$S _ { 2 } \mathcal { C }$are cofiber sequences$X _ { 1 }  X _ { 2 } \twoheadrightarrow X _ { 2 } / X _ { 1 }$, which we either think of a short filtration$X _ { 1 }  X _ { 2 }$of the object$X _ { 2 }$, together with a choice of filtration quotient$X _ { 2 } / X _ { 1 }$, or as an extension of the two objects$X _ { 1 }$ and$X _ { 2 } / X _ { 1 }$

For the purpose of higher algebraic K-theory, we must generalize this to consider sequences of cofibrations

$$
X _ {1} \longmapsto \dots \longmapsto X _ {q - 1} \longmapsto X _ {q},
$$

viewed as a longer filtration of the object$X _ { q } ,$together with choices of filtration quotients$X _ { j } / X _ { i }$for all$1 \leq i < j \leq q .$Alternatively, we view these as compatible extensions of the q objects$X _ { 1 } , X _ { 2 } / X _ { 1 } , \ldots , X _ { q } / X _ { q - 1 }$. These are the objects of a category$S _ { q } \mathcal { C }$, and taken together for varying$q \geq 0$, we get a simplicial category$S _ { \bullet } \mathcal { C }$, known as Waldhausen’s$S _ { \bullet }$-construction.

It is convenient to add$X _ { 0 } ~ = ~ *$to the sequence of subobjects, and to set $X _ { j } / X _ { i } = * \operatorname { f o r } i = j$. The objects of$S _ { q } \mathcal { C }$are then certain commutative diagrams

![](images/page_31_image_1.jpg)

in$\mathcal { C } .$, with one entry$X _ { i , j } = X _ { j } / X _ { i }$for each$0 \leq i \leq j \leq q .$We view$i \leq j$as a morphism in$[ q ] ,$, or rather as an object in the arrow category$\mathrm { A r } [ q ]$, so that diagrams like the one above are given by functors$X \colon \mathrm { A r } [ q ]  \mathcal { C }$

[[Only extensions$X _ { j } / X _ { i }$of consecutive objects$X _ { i + 1 } / X _ { i } , \dots , X _ { j } / X _ { j - 1 }$are considered.]]

Definition 8.3.1 (Arrow category on$[ q ] )$. Let$[ q ] = \{ 0 < 1 < \cdots < q \}$for $q \geq 0$. The arrow category$\mathrm { A r } [ q ] \cong \mathbf { F u n } ( [ 1 ] , [ q ] )$has objects the pairs$( i , j )$with $i , j \in [ q ]$and$i \le j$, corresponding to the arrow$i  j$in$[ q ] ,$, or the functor $[ 1 ]  [ q ]$mapping$0 \mapsto i$and$1 \mapsto j .$There is a unique morphism$( i , j )  ( i ^ { \prime } , j ^ { \prime } )$ in$\mathrm { A r } [ q ]$if and only if$i \leq i ^ { \prime }$and$j \le j ^ { \prime }$, corresponding to the commutative square

![](images/page_31_image_5.jpg)

in$[ q ]$. In particular there are morphisms$( i , j ) \to ( i , k )$and$( i , k ) \to ( j , k )$for all triples$i \leq j \leq k .$and every other morphism in$\mathrm { A r } [ q ]$is a composite of these generating morphisms.

We shall view [q] as a full subcategory of$\mathrm { A r } [ q ]$, by mapping$j ~ \in ~ [ q ]$to $( 0 , j ) \in \operatorname { A r } [ q ]$. Given a morphism$\alpha \colon [ p ]  [ q ]$in$\Delta .$, there is an induced functor $\operatorname { A r } ( \alpha )$$\mathrm { A r } [ p ] \to \mathrm { A r } [ q ]$taking$( i , j )$to$( \alpha ( i ) , \alpha ( j ) )$, defining a functor$\mathrm { A r } \colon \Delta$ Cat.

Example 8.3.2. Here is a picture of$\mathrm { A r [ 3 ] }$, with a generating set of morphisms:

![](images/page_32_image_1.jpg)

The category$[ 3 ] = \{ 0 < 1 < 2 < 3 \}$is embedded as the top row in this diagram. The identity arrows$( j , j )$in [q] appear along the diagonal, and the indecomposable arrows$( j - 1 , j )$in [q] appear on the adjacent “superdiagonal”.

Definition 8.3.3 (Category$S _ { q } \mathcal { C } )$. Let$\mathcal { C }$be a category with cofibrations. Consider the category Fun$( \mathrm { A r } [ q ] , \mathcal { C } )$of$\mathrm { A r } [ q ]$-shaped diagrams in${ \mathcal { C } } _ { : }$i.e., functors

$$
X \colon \operatorname{Ar} [ q ] \longrightarrow \mathscr {C}
$$

taking$( i , j )$to$X _ { i , j }$for$i \leq j$in [q], and natural transformations between these. Let

$$
S _ {q} \mathcal {C} \subseteq \mathbf {F u n} (\operatorname{Ar} [ q ], \mathcal {C})
$$

be the full subcategory generated by the diagrams$X \colon \mathrm { A r } [ q ]  \mathcal { C }$such that

(a)$X _ { j , j } = *$for each$j \in [ q ]$

(b)$X _ { i , j } \longmapsto X _ { i , k } \twoheadrightarrow X _ { j , k }$is a cofiber sequence for each triple$i < j < k$in$[ q ]$. A morphism$f \colon X \to Y$in$S _ { q } \mathcal { C }$is a map of$\mathrm { A r } [ q ]$-shaped diagrams, consisting of morphisms$f _ { i , j } \colon X _ { i , j } \to Y _ { i , j }$in$\mathcal { C }$for all$i \leq j$in$[ q ]$, making the square

![](images/page_32_image_10.jpg)

commute for each morphism$( i , j ) \  \ ( i ^ { \prime } , j ^ { \prime } )$in$\mathrm { A r } [ q ]$. The category$S _ { q } \mathcal { C }$is pointed at the constant diagram at ∗.

Remark 8.3.4. Condition (b) holds trivially i${ \dot { \ } } i = j \ \mathrm { o r } \ j = k$, since$* \$ $X _ { i , k } = X _ { i , k }$and$X _ { i , k } = X _ { i , k } \to *$are cofiber sequences. It can be rewritten as saying that$X _ { i , j }  X _ { i , k }$is a cofibration and the square

$$
\begin{array}{c} X _ {i, j} \xrightarrow {} X _ {i, k} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \\ X _ {j, j} \xrightarrow {} X _ {j, k} \end{array}
$$

is a pushout, for each triple$i \le j \le k$in$[ q ]$.

Example 8.3.5. An object in$S _ { 0 } \mathcal { C }$is the diagram

∗

in$\mathcal { C } _ { : }$, with$X _ { 0 , 0 } = *$. Hence$S _ { 0 } \mathcal { C }$is the one-morphism category, also denoted ∗. Example 8.3.6. An object in$S _ { 1 } \mathcal { C }$is any (trivially commutative) diagram

![](images/page_33_image_3.jpg)

in${ \mathcal { C } } _ { : }$, with$X _ { 0 , 0 } = X _ { 1 , 1 } = *$. We view it as the object$X _ { 0 , 1 }$in$\mathcal { C } .$, with no filtration. Hence$S _ { 1 } \mathcal { C }$is naturally isomorphic to$\mathcal { C }$.

Example 8.3.7. An object in$S _ { 2 } \mathcal { C }$is a commutative diagram

![](images/page_33_image_6.jpg)

in${ \mathcal { C } } _ { : }$where each horizontal morphism is a cofibration, and the square is a pushout. We view it as the object$X _ { 0 , 2 }$with the short filtration$X _ { 0 , 1 }  X _ { 0 , 2 }$ together with the choice of quotient map$X _ { 0 , 2 } \twoheadrightarrow X _ { 1 , 2 }$. Alternatively, we can view it as a choice of extension$X _ { 0 , 2 }$of the objects$X _ { 0 , 1 }$and$X _ { 1 , 2 }$. Hence$S _ { 2 } \mathcal { C }$ is naturally isomorphic to the category defined in Definition 8.1.24.

Example 8.3.8. An object in$S _ { 3 } \mathcal { C }$is a commutative diagram

![](images/page_33_image_9.jpg)

in${ \mathcal { C } } _ { : }$, where each horizontal morphism is a cofibration, and each square is a pushout. (See Lemma 8.3.9 for the upper right hand square.) We view it as the object$X _ { 0 , 3 }$with the three-stage filtration$X _ { 0 , 1 }  X _ { 0 , 2 }  X _ { 0 , 3 }$, together will all choices of subquotients. Alternatively, we can view it as a compatible system of choices of extensions of all consecutive subsets of the three objects$X _ { 0 , 1 } , X _ { 1 , 2 }$ and$X _ { 2 , 3 }$. (No extension of the non-consecutive objects$X _ { 0 , 1 }$and$X _ { 2 , 3 }$is part of the data.)

Lemma 8.3.9. Let$X \colon \mathrm { A r } [ q ]  \mathcal { C }$be an object in$S _ { q } \mathcal { C }$. Then

![](images/page_34_image_1.jpg)

is a pushout square with horizontal cofibrations and vertical quotient maps,$f o r$ each$i \leq j \leq k \leq \ell$in [q].

Proof. Consider the subdiagram

![](images/page_34_image_4.jpg)

of$X$. By the defining condition for$i \le j \le k$the upper left hand square is a pushout and$X _ { i , k } \ \to \ X _ { j , k }$is a quotient map. By the condition for$i \le k \le \ell$ the morphism$X _ { i , k } \mathrel { \mathop  } X _ { i , \ell }$is a cofibration, and by the condition for$j \le k \le \ell$ the morphism$X _ { j , k } \mathrel { \mathop  } X _ { j , \ell }$is a cofibration. By the condition for$i \le j \le \ell$the upper rectangle is a pushout and$X _ { i , \ell } \twoheadrightarrow X _ { j , \ell }$is a quotient map. It follows that the upper right hand square is a pushout, since

$$
X _ {j, k} \cup_ {X _ {i, k}} X _ {i, \ell} \cong X _ {j, j} \cup_ {X _ {i, j}} X _ {i, k} \cup_ {X _ {i, k}} X _ {i, \ell} \cong X _ {j, j} \cup_ {X _ {i, j}} X _ {i, \ell}
$$

maps isomorphically to$X _ { j , \ell }$

Definition 8.3.10 (Cofibration category co$S _ { q } \mathcal { C } )$. Let$( { \mathcal { C } } , c o { \mathcal { C } } )$be a category with cofibrations. Let co$S _ { q } \mathcal { C } \subseteq S _ { q } \mathcal { C }$be the subcategory with morphisms $f \colon X \mapsto Y$the maps of$\operatorname { A r } [ q ] .$-shaped diagrams such that the pushout morphism

$$
X _ {0, j} \cup_ {X _ {0, j - 1}} Y _ {0, j - 1} \mapsto Y _ {0, j}
$$

is a cofibration in$\mathcal { C }$, for each$1 \leq j \leq q$

![](images/page_34_image_11.jpg)

Remark 8.3.11. The assumption that$f$is a cofibration in$S _ { q } \mathcal { C }$implies that each$f _ { 0 , j }$is a cofibration in$\mathcal { C }$, so each diagram

![](images/page_34_image_13.jpg)

is a lattice square. This implies the seemingly more general statement below.

Lemma 8.3.12. Let$f \colon X \mapsto Y$be a morphism in co$S _ { q } \mathcal { C }$. The diagram

![](images/page_35_image_2.jpg)

is a lattice square for each$i \le j \le k$in$[ q ]$. In particular, each component $f _ { i , j } \colon X _ { i , j } \mapsto Y _ { i , j }$is a cofibration.

Proof. We first prove that

$$
X _ {0, k} \cup_ {X _ {0, j}} Y _ {0, j} \hookrightarrow Y _ {0, k}\tag{8.2}
$$

a cofibration for all$j \le k$in$[ q ]$. This is trivially true for$j = k$. If$j < k$, we may assume by induction on$\left( k - j \right)$that

$$
X _ {0, k - 1} \cup_ {X _ {0, j}} Y _ {0, j} \hookrightarrow Y _ {0, k - 1}
$$

is a cofibration. By pushout along$X _ { 0 , k - 1 } \ \longmapsto \ X _ { 0 , k }$, using Lemma 8.1.6), it follows that

$$
X _ {0, k} \cup_ {X _ {0, j}} Y _ {0, j} \rightharpoonup X _ {0, k} \cup_ {X _ {0, k - 1}} Y _ {0, k - 1}
$$

is a cofibration. By assumption

$$
X _ {0, k} \cup_ {X _ {0, k - 1}} Y _ {0, k - 1} \hookrightarrow Y _ {0, k}
$$

is a cofibration, hence the composite map (8.2) is also a cofibration, completing the inductive step.

There is a vertical map of cofiber sequences

$$
\begin{array}{c} Y _ {0, i} \cup_ {X _ {0, i}} X _ {0, i} \longrightarrow Y _ {0, j} \cup_ {X _ {0, j}} X _ {0, k} \longrightarrow Y _ {i, j} \cup_ {X _ {i, j}} X _ {i, k} \\ \cong \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \\ Y _ {0, i} \xrightarrow {} Y _ {0, k} \xrightarrow {} Y _ {i, k} \end{array}
$$

where the left hand vertical map is an isomorphism. Hence the right hand square is a pushout. We have just shown that the middle vertical map is a cofibration, so the right hand vertical map is also a cofibration, by cobase change.

The horizontal maps$X _ { i , j }  X _ { i , k }$and$Y _ { i , j }  Y _ { i , k }$were shown to be cofibrations in Lemma 8.3.9. It remains to prove that the vertical maps$X _ { i , j }  Y _ { i , j }$ are cofibrations for all$i \leq j$in [q]. But this map can be rewritten as

$$
X _ {i, j} \cong Y _ {i, i} \cup_ {X _ {i, i}} X _ {i, j} \mapsto Y _ {i, j}
$$

since$X _ { i , i } ~ \longrightarrow ~ Y _ { i , i }$is the identity map$*  *$, which we have just shown is a cofibration.□

Lemma 8.3.13.$( S _ { q } \mathcal { C } , c o S _ { q } \mathcal { C } )$is a category with cofibrations.

Proof. The proof is similar to the case$q = 2 \colon$The composite of two cofibrations $f \colon X \mapsto Y$and$g \colon Y \mapsto Z$is a cofibration, since for each$1 \leq j \leq q$, the three pushout squares

![](images/page_36_image_1.jpg)

exist, three morphisms are cofibrations by assumption, and the remaining three morphisms are cofibrations by cobase change.

Isomorphisms and initial morphisms in$S _ { q } \mathcal { C }$are obviously cofibrations. Concerning cobase change, suppose given a cofibration$f \colon X \mapsto Y$and any morphism$g \colon X \to Z$in$S _ { q } \mathcal { C }$. Each component$f _ { i , j } \colon X _ { i , j } \ \longmapsto \ Y _ { i , j }$is a cofibration, by Lemma$8 . 3 . 1 2$, so each pushout$W _ { i , j } = Y _ { i , j } \cup _ { X _ { i , j } } \bar { Z _ { i , j } }$exists. These assemble to a functor W :$\mathrm { A r } [ q ] \to \mathcal { C }$by the universal property of pushouts. If$i = j ,$, we may assume that we chose$W _ { j , j } = *$as the pushout$* \cup _ { * } * .$. For each$i < j < k$ in [q], we claim that the diagram

$$
W _ {i, j} \longrightarrow W _ {i, k} \longrightarrow W _ {j, k}
$$

is a cofiber sequence. The left hand morphism factors as the composite of two cofibrations, as in the following diagram

$$
\begin{array}{c} Z _ {i, j} \xrightarrow {} Z _ {i, k} \\ f _ {i, j} \cup i d \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow f _ {i, j} \cup i d \\ Y _ {i, j} \cup_ {X _ {i, j}} Z _ {i, j} \xrightarrow {} Y _ {i, j} \cup_ {X _ {i, j}} Z _ {i, k} \xrightarrow {} Y _ {i, k} \cup_ {X _ {i, k}} Z _ {i, k} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ Y _ {i, j} \cup_ {X _ {i, j}} X _ {i, k} \xrightarrow {} Y _ {i, k} \end{array}
$$

with two pushout squares, where the upper and lower horizontal arrows are cofibrations by Lemmas 8.3.9 and 8.3.12, respectively. The proof that$W _ { i , k } / W _ { i , j } \cong$ $W _ { j , k }$is by commutation of colimits, just as for$q = 2$. Hence W is the pushout of f and g in$S _ { q } \mathcal { C }$

Finally, to see that the induced map f∪id:$Z \to Y \cup _ { X } Z = W$is a cofibration, we must check that the pushout map$W _ { 0 , j - 1 } \cup _ { Z _ { 0 , j - 1 } } Z _ { 0 , j } \to W _ { 0 , j }$is a cofibration, for$1 \le j \le q$. This follows from the pushout square

$$
\begin{array}{c} Y _ {0, j - 1} \cup_ {X _ {0, j - 1}} X _ {0, j} \xrightarrow {} Y _ {0, j} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \\ Y _ {0, j - 1} \cup_ {X _ {0, j - 1}} Z _ {0, j} \xrightarrow {} Y _ {0, j} \cup_ {X _ {0, j}} Z _ {0, j} \end{array}
$$

Definition 8.3.14 (Weak equivalence category w$S _ { q } \mathcal { C } )$. Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. Let$w S _ { q } \mathcal { C } \subseteq S _ { q } \mathcal { C }$be the subcategory with morphisms $f \colon X \xrightarrow { \sim } Y$the maps of$\mathrm { A r } [ q ]$-shaped diagrams such that

$$
f _ {0, j} \colon X _ {0, j} \xrightarrow {\sim} Y _ {0, j}
$$

is a weak equivalence in$\mathcal { C }$for each$1 \leq j \leq q$

Lemma 8.3.15. Let$f \colon X \xrightarrow { \sim } Y$be a morphism in w$S _ { q } \mathcal { C }$. Each component

$$
f _ {i, j} \colon X _ {i, j} \xrightarrow {\sim} Y _ {i, j}
$$

is a weak equivalence in${ \mathcal { C } } ,$for$i \leq j$in$[ q ]$.

Proof. This is immediate from the gluing lemma applied to the diagram

$$
\begin{array}{c} X _ {0, j} \longleftarrow X _ {0, i} \longrightarrow * \\ \simeq \Biggl \downarrow \qquad \qquad \simeq \Biggl \downarrow \qquad = \Biggl \downarrow \\ Y _ {0, j} \longleftarrow Y _ {0, i} \longrightarrow *, \end{array}
$$

giving the weak equivalence$X _ { i , j } \cong X _ { 0 , j } \cup _ { X _ { 0 , i } } * \xrightarrow { \sim } Y _ { 0 , j } \cup _ { Y _ { 0 , i } } * \cong Y _ { i , j }$□

Lemma 8.3.16.$( S _ { q } \mathcal { C } , w S _ { q } \mathcal { C } )$is a Waldhausen category.

[[Proof]]

Definition 8.3.17 (Simplicial category$S _ { \bullet } \mathcal { C } )$. Let$\mathcal { C }$be a category with cofibrations. For each morphism$\alpha \colon [ p ]  [ q ]$in$\Delta$, let

$$
\alpha^ {*} \colon S _ {q} \mathcal {C} \longrightarrow S _ {p} \mathcal {C}
$$

take$X \colon \mathrm { A r } [ q ]  \mathcal { C }$to the composite functor

$$
\alpha^ {*} (X) = X \circ \operatorname{Ar} (\alpha): \operatorname{Ar} [ p ] \longrightarrow \operatorname{Ar} [ q ] \longrightarrow \mathscr {C}.
$$

Hence$\alpha ^ { * } ( X ) \colon \operatorname { A r } [ p ] \to \ell$takes$( i , j )$to$X _ { \alpha ( i ) , \alpha ( j ) }$. This defines an object in $S _ { p } \mathcal { C }$, since

$$
\alpha^ {*} (X) _ {j, j} = X _ {\alpha (j), \alpha (j)} = *
$$

for all$j \in [ p ]$, and

$$
\alpha^ {*} (X) _ {i, j} \mapsto \alpha^ {*} (X) _ {i, k} \twoheadrightarrow \alpha^ {*} (X) _ {j, k}
$$

equals the cofiber sequence

$$
X _ {\alpha (i), \alpha (j)} \hookrightarrow X _ {\alpha (i), \alpha (k)} \twoheadrightarrow X _ {\alpha (j), \alpha (k)}
$$

for each triple$i < j < k$in$[ p ]$. These rules define a simplicial pointed category

$$
S _ {\bullet} \mathcal {C}: [ q ] \longmapsto S _ {q} \mathcal {C}
$$

called the$S _ { \bullet }$-construction on$\mathcal { C }$

[[Explain face and degeneracy maps.]]

Lemma 8.3.18. Let$\mathcal { C }$be a category with cofibrations. Each functor

$$
\alpha^ {*} \colon S _ {q} \mathcal {C} \to S _ {p} \mathcal {C}
$$

is exact. Hence$S _ { \bullet } \mathcal { C }$is a simplicial category with cofibrations.

[[Proof]]

Lemma 8.3.19. An exact functor$F \colon \mathcal { C }  \mathcal { D }$of categories with cofibrations induces a (simplicial) exact functor$S _ { \bullet } F \colon S _ { \bullet } \mathcal { C } \to S _ { \bullet } \mathcal { D }$of simplicial categories with cofibrations.

[[Proof]]

Proposition 8.3.20. Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. Each functor

$$
\alpha^ {*} \colon S _ {q} \mathcal {C} \to S _ {p} \mathcal {C}
$$

is exact. Hence$( S _ { \bullet } \mathcal { C } , w S _ { \bullet } \mathcal { C } )$is a simplicial Waldhausen category.

[[Proof]]

Proposition 8.3.21. An exact functor$F \colon ( \mathcal { C } , w \mathcal { C } )  ( \mathcal { D } , w \mathcal { D } )$of Waldhausen categories induces a (simplicial) exact functor

$$
S _ {\bullet} F \colon (S _ {\bullet} \mathcal {C}, w S _ {\bullet} \mathcal {C}) \longrightarrow (S _ {\bullet} \mathcal {D}, w S _ {\bullet} \mathcal {D})
$$

of simplicial Waldhausen categories. In particular, it induces a (simplicial) functor

$$
w S _ {\bullet} F \colon w S _ {\bullet} \mathcal {C} \longrightarrow w S _ {\bullet} \mathcal {D}
$$

of simplicial pointed categories. We get functors$S _ { \bullet }$: Wald → sWald and wS : Wald$\xrightarrow { } s \mathbf { C a t } _ { * }$k

[[Proof]]

[[Show that$S _ { q } \mathcal { C }$is determined by its 2-faces α :$[ 2 ]  [ q ] . ] ]$

## 8.4 Algebraic K-groups

Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. The nerve of the simplicial category w$S _ { \bullet } \mathcal { C }$is the bisimplicial set$N _ { \bullet } w S _ { \bullet } \mathcal { C }$with$( p , q )$-bisimplices the chains of p composable weak equivalences of length q sequences of cofibrations:

![](images/page_38_image_19.jpg)

together with choices of subquotients$X _ { i , j } ^ { k } \cong X _ { j } ^ { k } / X _ { i } ^ { k }$for each$i \leq j$in$[ q ] , k \in [ p ]$

Lemma 8.4.1. The inclusion of the right 1-skeleton defines a natural bisimplicial map

$$
N _ {\bullet} w \mathcal {C} \wedge S _ {\bullet} ^ {1} \longrightarrow N _ {\bullet} w S _ {\bullet} \mathcal {C},
$$

inducing a based map

$$
\sigma \colon \Sigma | w \mathscr {C} | \longrightarrow | w S _ {\bullet} \mathscr {C} |
$$

on classifying spaces.

Proof. We view$N _ { \bullet } w S _ { \bullet } \mathcal { C }$as the simplicial object

$$
[ q ] \mapsto N _ {\bullet} w S _ {q} \mathcal {C}
$$

in simplicial sets, treating the right hand index,$q ,$as the external grading.$[ [ \mathrm { A s }$ opposed to in the proof of the realization lemma, where the left hand index was the external grading.]] For$q = 0$, w$S _ { 0 } \mathcal { C } = S _ { 0 } \mathcal { C } = *$is the one-morphism category, so$N _ { \bullet w S _ { 0 } } \mathcal { C } = *$is the simplicial point. For$q = 1$，$w S _ { 1 } \mathcal { C } \cong w \mathcal { C }$. The right 1-skeleton of$N _ { \bullet } w S _ { \bullet } \mathcal { C }$is the image of the canonical map

$$
\coprod_ {q \leq 1} N _ {\bullet} w S _ {q} \mathcal {C} \times \Delta_ {\bullet} ^ {q} \longrightarrow N _ {\bullet} w S _ {\bullet} \mathcal {C},
$$

which equals the reduced suspension

$$
N _ {\bullet} w \mathcal {C} \wedge S _ {\bullet} ^ {1} = \frac {N _ {\bullet} w \mathcal {C} \times \Delta_ {\bullet} ^ {1}}{\{* \} \times \Delta_ {\bullet} ^ {1} \cup N _ {\bullet} w \mathcal {C} \times \partial \Delta_ {\bullet} ^ {1}}.
$$

[[The degeneracy map$s _ { 0 }$collapses$\{ * \} \times \Delta _ { \bullet } ^ { 1 }$. The face maps$d _ { 0 }$and$d _ { 1 }$collapse $\ddot { N } _ { \bullet } w \mathcal { C } \times \mathsf { \bar { \partial } } \Delta _ { \bullet } ^ { 1 } . ] ]$□

Definition 8.4.2 (Algebraic K-theory). Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. The algebraic K-theory space

$$
K (\mathcal {C}, w) = \Omega | w S _ {\bullet} \mathcal {C} |
$$

is the loop space of the classifying space of the simplicial pointed category$w S _ { \bullet } \mathcal { C }$2 i.e., of the topological realization of the bisimplicial set$N _ { \bullet } w S _ { \bullet } \mathcal { C }$. Let

$$
\iota \colon | w \mathscr {C} | \longrightarrow K (\mathscr {C}, w)
$$

be right adjoint to the based map σ above.

Let$F \colon ( \mathcal { C } , w \mathcal { C } ) \ \to \ ( \mathcal { D } , w \mathcal { D } )$be an exact functor. The induced map in algebraic K-theory

$$
K (F) = \Omega | w S _ {\bullet} F | \colon K (\mathcal {C}, w) \longrightarrow K (\mathcal {D}, w)
$$

is the loop map of the classifying map of the simplicial functor w$S _ { \bullet } F _ { \bullet }$. These rules define the algebraic K-theory functor

$$
K \colon \operatorname{Wald} \longrightarrow \operatorname{Top} _ {*}.
$$

Definition 8.4.3 (Algebraic K-groups). The algebraic K-groups

$$
K _ {i} (\mathcal {C}, w) = \pi_ {i} K (\mathcal {C}, w)
$$

of a Waldhausen category$( \mathcal { C } , w \mathcal { C } )$are the homotopy groups, for$i \geq 0$, of the algebraic K-theory space. The induced homomorphism

$$
K _ {i} (F) \colon K _ {i} (\mathcal {C}, w) \longrightarrow K _ {i} (\mathcal {D}, w)
$$

of an exact functor$F \colon ( \mathcal { C } , w \mathcal { C } ) \to ( \mathcal { D } , w \mathcal { D } )$, is the homomorphism$K _ { i } ( F ) =$ $\pi _ { i } K ( F )$induced by the based map of algebraic K-theory spaces. These rules define the algebraic K-group functors

$$
K _ {i} \colon \mathbf {W a l d} \to \mathbf {A b}.
$$

Remark 8.4.4. The space$| w S _ { \bullet } \mathcal { C } |$is connected, since w$S _ { 0 } \mathcal { C } = *$in simplicial degree 0 and all higher simplices are attached to this point. Hence no homotopical information is lost by passing to the loop space$\Omega | w S _ { \bullet } \mathcal { C } |$

Remark 8.4.5. It is clear that$K _ { i } ( \mathcal { C } , w ) = \pi _ { i + 1 } | w S _ { \bullet } \mathcal { C } |$is abelian for$i \geq 1$ The assertion that$K _ { 0 } ( \mathcal { C } , w )$is abelian follows from the next lemma, since the (split) cofiber sequences$X ^ { \prime } \stackrel { \prime } { \longmapsto } X ^ { \prime } \vee X ^ { \prime \prime } \twoheadrightarrow X ^ { \prime \prime }$and$X ^ { \prime \prime } \longmapsto X ^ { \prime } \vee X ^ { \prime \prime } \twoheadrightarrow X ^ { \prime }$imply $[ \tilde { X ^ { \prime } } ] \cdot \dot { [ X ^ { \prime \prime } ] } = [ \tilde { X ^ { \prime } \vee } X ^ { \prime \prime } ] = [ X ^ { \prime \prime } ] [ X ^ { \prime } ]$. We therefore write the group operation in $K _ { i } ( \mathcal { C } , w )$additively, also for$i = 0$

Lemma 8.4.6. The group$K _ { 0 } ( \mathcal { C } , w )$is generated by classes [X] for each object X in C , subject to the relations$[ \dot { X ^ { \prime } } ] + \dot { [ } X ^ { \prime \prime } ] = [ \dot { X } ]$for each cofiber sequence $X ^ { \prime }  X \twoheadrightarrow X ^ { \prime \prime }$, and$[ X ] \ = \ [ Y ]$for each weak equivalence$X \xrightarrow { \sim } Y$. The homomorphism$K _ { 0 } ( F ) \colon K _ { 0 } ( \mathcal { C } , w ) \to K _ { 0 } ( \mathcal { D } , w )$takes [X] to$\left[ F ( X ) \right]$

Proof. We compute the fundamental group of the topological realization of $N _ { \bullet } w S _ { \bullet } \mathcal { C }$, based at the single$( 0 , 0 ) { \mathrm { - s i m p l e x ~ } } *$. The realization has a CW structure [[Explain!]] with one 1-cell for each (0, 1)-simplex X, a 2-cell for each (0, 2)-simplex${ \ddot { X } } ^ { \prime } \stackrel { } { \longrightarrow } X \twoheadrightarrow X ^ { \prime \prime }$(attached to the 1-cells$X ^ { \prime \prime } , X$and$X ^ { \prime } )$, and a 2-cell for each (1, 1)-simplex$X \xrightarrow { \cdot \sim } Y$(attached to the 1-cells X and$Y )$. The remaining cells are of higher dimension, hence do not afect the fundamental group.

The bisimplicial map$N _ { \bullet } w S _ { \bullet } \mathcal { C }  N _ { \bullet } w S _ { \bullet } \mathcal { D }$takes each (0, 1)-simplex X to the (0, 1)-simplex$F ( X )$, which determines$K _ { 0 } ( F )$on the generators.□

Definition 8.4.7 (Algebraic K-theory of rings). Let R be a ring. The algebraic K-theory space of R is

$$
K (R) = K (\mathscr {P} (R), i) = \Omega | i S _ {\bullet} \mathscr {P} (R) |
$$

is the algebraic K-theory space of the Waldhausen category$( \mathcal { P } ( R ) , i \mathcal { P } ( R ) )$ of finitely generated projective R-modules, injective R-module homomorphisms with projective cokernel, and R-module homomorphisms. The algebraic$K \cdot$ theory groups of R are

$$
K _ {i} (R) = K _ {i} (\mathscr {P} (R), i) = \pi_ {i + 1} | i S _ {\bullet} \mathscr {P} (R) |
$$

for$i \geq 0$

For each ring homomorphism$\phi \colon R \to T$the inverse image (= base change) functor$\phi _ { * } \colon { \mathcal { P } } ( R ) \to { \mathcal { P } } ( T )$induces the natural map$K ( \phi _ { * } ) \colon K ( R ) \to K ( T )$2 and the natural homomorphisms

$$
\phi_ {*} = K _ {i} (\phi_ {*}) \colon K _ {i} (R) \longrightarrow K _ {i} (T)
$$

for each$i \geq 0$. If T is finitely generated projective over$R ,$the direct image$( =$ forgetful) functor$\phi ^ { * } \colon { \mathcal { P } } ( T ) \to { \mathcal { P } } ( R )$induces the transfer map$K ( \phi ^ { * } ) \colon K ( T ) \to$ $K ( R )$and the transfer homomorphisms

$$
\phi^ {*} = K _ {i} (\phi^ {*}) = K _ {i} (T) \longrightarrow K _ {i} (R).
$$

Definition 8.4.8 (Algebraic G-theory of rings). Let R be a Noetherian ring. The algebraic G-theory space of$R$is

$$
G (R) = K (\mathcal {M} (R), i) = \Omega | i S _ {\bullet} \mathcal {M} (R) |
$$

is the algebraic K-theory space of the Waldhausen category$( { \mathcal { M } } ( R ) , i { \mathcal { M } } ( R ) )$ of finitely generated R-modules, injective R-module homomorphisms, and$R -$ module homomorphisms. The algebraic G-theory groups of R are

$$
G _ {i} (R) = K _ {i} (\mathcal {M} (R), i) = \pi_ {i + 1} | i S _ {\bullet} \mathcal {M} (R) |
$$

for$i \geq 0 .$. [[Discuss the immediate functoriality properties of G-theory.]] The exact functor$\mathcal { P } ( R ) \subseteq \mathcal { M } ( R )$induces a natural map$K ( R ) \to G ( R )$ and natural homomorphism${ \cal K } _ { i } ( R ) \longrightarrow G _ { i } ( R )$for$i \geq 0$

Remark 8.4.9. Another name for G-theory is$K ^ { \prime } \cdot$theory. Under suitable regularity hypotheses on$R ,$the natural map$K ( R ) \to G ( R )$is a homotopy equivalence. [[View K-theory as a cohomology theory on schemes, with corresponding Borel–Moore/locally finite homology theory given by G-theory. A homotopy equivalence$K ( R ) \simeq G ( R )$is then a form of Poincar´e duality.]]

[[For non-Noetherian$R ,$one should work with coherent, or pseudo-coherent, R-modules.]]

Exercise 8.4.10. Let$c o ^ { \oplus } \mathcal { M } ( \mathbb { Z } ) \subset c o \mathcal { M } ( \mathbb { Z } )$be the subcategory consisting of split injective Z-module homomorphisms. Determine the groups

$$
G _ {0} (\mathbb {Z}) = K _ {0} \left(\mathcal {M} (\mathbb {Z}), c o \mathcal {M} (\mathbb {Z}), i \mathcal {M} (\mathbb {Z})\right)
$$

and

$$
G _ {0} ^ {\oplus} (\mathbb {Z}) = K _ {0} \big (\mathcal {M} (\mathbb {Z}), c o ^ {\oplus} \mathcal {M} (\mathbb {Z}), i \mathcal {M} (\mathbb {Z}) \big),
$$

and the induced homomorphisms$K _ { 0 } ( \mathbb { Z } ) \to G _ { 0 } ^ { \oplus } ( \mathbb { Z } ) \to G _ { 0 } ( \mathbb { Z } )$

Exercise 8.4.11. Let$\mathcal { M } ^ { q } ( \mathbb { Z } ) \subset \mathcal { M } ( \mathbb { Z } )$be the full subcategory consisting of finite abelian groups (= rationally trivial finitely generated Z-modules). Consider it as a Waldhausen subcategory of$( \mathcal { M } ( \mathbb { Z } ) , c o \mathcal { M } ( \mathbb { Z } ) , i \mathcal { M } ( \mathbb { Z } ) )$. Determine the group

$$
K _ {0} (\mathcal {M} ^ {q} (\mathbb {Z}), i)
$$

and the induced homomorphism to$G _ { 0 } ( \mathbb { Z } )$

[[Relate coproduct in$\mathcal { C }$with group structure on$K _ { i } ( \mathcal { C } ) . ] ]$

## 8.5 The additivity theorem

The following theorem is fundamental in the development of higher algebraic K-theory. [[Refer to Grayson, Stafeldt, McCarthy.]] It was proved by Quillen in the setting of exact categories [55, §3], and generalized by Waldhausen. We follow Waldhausen’s presentation [68, 1.4], but make use of the simplification found by Grayson et al [31], which relies on theorem$\mathrm { A ^ { * } }$instead of Quillen’s theorem B.

Theorem 8.5.1 (Additivity theorem). Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. The exact functor

$$
(s, q) \colon S _ {2} \mathscr {C} \longrightarrow \mathscr {C} \times \mathscr {C}
$$

taking$X ^ { \prime }  X \twoheadrightarrow X ^ { \prime \prime }$to$( X ^ { \prime } , X ^ { \prime \prime } )$induces a homotopy equivalence

$$
w S _ {\bullet} (s, q) \colon w S _ {\bullet} S _ {2} \mathscr {C} \xrightarrow {\simeq} w S _ {\bullet} \mathscr {C} \times w S _ {\bullet} \mathscr {C}.
$$

Hence

$$
K (s, q) \colon K (S _ {2} \mathscr {C}, w) \xrightarrow {\simeq} K (\mathscr {C}, w) \times K (\mathscr {C}, w).
$$

Corollary 8.5.2. The two exact functors of Waldhausen categories

$$
t, s \vee q: S _ {2} \mathcal {C} \longrightarrow \mathcal {C}
$$

taking$X ^ { \prime }  X \Rightarrow X ^ { \prime \prime }$to X and$X ^ { \prime } \vee X ^ { \prime \prime }$, respectively, induce homotopic functors

$$
w S _ {\bullet} t \simeq w S _ {\bullet} (s \vee q) \colon w S _ {\bullet} S _ {2} \mathscr {C} \longrightarrow w S _ {\bullet} \mathscr {C}.
$$

Hence

$$
K (t) \simeq K (s \vee q) \colon K (S _ {2} \mathscr {C}, w) \longrightarrow K (\mathscr {C}, w)
$$

and

$$
K _ {i} (t) = K _ {i} (s) + K _ {i} (q): K _ {i} \left(S _ {2} \mathscr {C}, w\right) \longrightarrow K _ {i} (\mathscr {C}, w)
$$

for each$i \geq 0$

Proof. Let$\sigma \colon { \mathcal { C } } \times { \mathcal { C } } \to S _ { 2 } { \mathcal { C } }$be the exact functor of Waldhausen categories taking$( X ^ { \prime } , X ^ { \prime \prime } )$to the (split) cofiber sequence$X ^ { \prime } \left. X ^ { \prime } \vee X ^ { \prime \prime } \right. X ^ { \prime \prime }$. The composite$( s , q )$◦ σ is the identity on${ \mathcal { C } } \times { \mathcal { C } }$, and the two composites$( s \lor q ) \circ \sigma$2 $t \circ \sigma \colon \mathcal { C } \times \mathcal { C } \to \mathcal { C }$are equal, so we get a diagram

![](images/page_42_image_18.jpg)

in Wald. By the additivity theorem,$w S _ { \bullet } ( s , q )$is a homotopy equivalence, so $v S _ { \bullet } \sigma$is a homotopy equivalence. Since w$\begin{array} { r } { \mathrm { ~ \phantom { ~ } } ; S _ { \bullet } ( s \vee q ) \circ w S _ { \bullet } \sigma = w S _ { \bullet } t \circ w S _ { \bullet } \sigma } \end{array}$, it follows that$w S _ { \bullet } ( s \vee q )$and$w S _ { \bullet } t$are homotopic. [[Relate$\lor \mathrm { ~ t o ~ + ~ }$in$K _ { i \cdot } ] ]$□

Definition 8.5.3 (Cofiber sequence of exact functors). Let$F ^ { \prime } , F , F ^ { \prime \prime } { : \mathcal { C } } \longrightarrow$ D be exact functors of Waldhausen categories. A pair of natural transformations $F ^ { \prime } \Rightarrow F \Rightarrow F ^ { \prime \prime }$is a cofiber sequence of exact functors, denoted$F ^ { \prime }  F \Rightarrow F ^ { \prime \prime }$<sup>′</sup>, if (a) for each object X in$\mathcal { C }$the sequence

$$
F ^ {\prime} (X) \mapsto F (X) \twoheadrightarrow F ^ {\prime \prime} (X)
$$

is a cofiber sequence in${ \mathcal { D } } .$, and

(b) for each cofibration$X ^ { \prime } \mapsto X$in$\mathcal { C }$, the diagram

![](images/page_43_image_4.jpg)

is a lattice square in${ \mathcal { D } } ,$in the sense that the pushout morphism

$$
F (X ^ {\prime}) \cup_ {F ^ {\prime} (X ^ {\prime})} F ^ {\prime} (X) \mapsto F (X)
$$

is a cofibration.

Equivalently, the rule sending X in$\mathcal { C }$to$F ^ { \prime } ( X ) \longmapsto F ( X ) \twoheadrightarrow F ^ { \prime \prime } ( X )$in$S _ { 2 } \mathcal { D }$ defines an exact functor$( \mathcal { C } , w \mathcal { C } )  ( S _ { 2 } \mathcal { D } , w S _ { 2 } \mathcal { D } )$

Corollary 8.5.4. If$F ^ { \prime }  F \Rightarrow F ^ { \prime \prime }$is a cofiber sequence of exact functors of Waldhausen categories, then the two exact functors F,$F ^ { \prime } \vee F ^ { \prime \prime } \colon \mathcal { C }  \mathcal { D }$induce homotopic functors

$$
w S _ {\bullet} F \simeq w S _ {\bullet} (F ^ {\prime} \vee F ^ {\prime \prime}) \colon w S _ {\bullet} \mathcal {C} \longrightarrow w S _ {\bullet} \mathcal {D}.
$$

Hence

$$
K (F) \simeq K (F ^ {\prime} \vee F ^ {\prime \prime}) \colon K (\mathcal {C}, w) \longrightarrow K (\mathcal {D}, w)
$$

and

$$
K _ {i} (F) = K _ {i} \left(F ^ {\prime}\right) + K _ {i} \left(F ^ {\prime \prime}\right): K _ {i} (\mathscr {C}, w) \longrightarrow K _ {i} (\mathscr {D}, w)
$$

for each$i \geq 0$

Proof. The cofiber sequence of exact functors defines an exact functor$G \colon { \mathcal { C } } \to$ S<sub>2</sub>D. By the previous corollary, and composition, the two exact functors$( s \vee$ $q ) \circ G = F ^ { \prime } \vee F ^ { \prime \prime }$and$t \circ G = F$induce homotopic functors, as claimed.□

[[Relate to sum in K-groups, using$K ( F ^ { \prime } \vee F ^ { \prime \prime } ) = K ( F ^ { \prime } ) \vee K ( F ^ { \prime \prime } ) \simeq K ( F ^ { \prime } )$∗ $K ( F ^ { \prime \prime } )$, so that$K _ { * } ( F ) = K _ { * } ( F ^ { \prime } ) + K _ { * } ( F ^ { \prime \prime } ) . ] ]$

Waldhausen’s proof of the additivity theorem separates into one part concerning the cofibrations and a second part involving the weak equivalences.

Definition 8.5.5 (Simplicial set$s _ { \bullet } \mathcal { C } )$. If$\mathcal { C }$is a small category with cofibrations, let$s _ { q } \mathcal { C } = \mathrm { o b j } ( S _ { q } \mathcal { C } )$for each$q \geq 0$, so that$[ q ] \mapsto s _ { q } \mathcal { C }$defines a simplicial set$s _ { \bullet } \mathcal { C }$. Each exact functor$F \colon { \mathcal { C } } \to { \mathcal { D } }$of categories with cofibrations induces a simplicial map$s _ { \bullet } F \colon s _ { \bullet } \mathcal { C } \to s _ { \bullet } \mathcal { D }$. In simplicial degree$q$it takes the object $X \colon \mathrm { A r } [ q ]  \mathcal { C }$to the object$F \circ X \colon \mathrm { A r } [ q ]  { \mathcal { D } }$

Lemma 8.5.6. A natural isomorphism φ:$F \Longrightarrow G$of exact functors$F , G \colon \mathcal { C }$ D induces a simplicial homotopy$s _ { \bullet } F \simeq s _ { \bullet } G \colon s _ { \bullet } \mathcal { C } \to s _ { \bullet } \mathcal { D }$

Proof. Write the natural isomorphism as a functor Φ:${ \mathcal { C } } \times [ 1 ] \to { \mathcal { D } }$. We describe the simplicial homotopy using Waldhausen’s notation from Definition 6.4.9, as a natural transformation

$$
\phi^ {*} \colon (s _ {\bullet} \mathcal {C}) ^ {*} \Longrightarrow (s _ {\bullet} \mathcal {D}) ^ {*}
$$

of functors$( \Delta / [ 1 ] ) ^ { o p } \ \longrightarrow \ \mathbf { S e t }$. Its component at$\zeta \colon [ q ]  [ 1 ]$is the function $\phi _ { \zeta } ^ { * } \colon s _ { q } \mathcal { C } \to s _ { q } \mathcal { D }$taking$X \colon \mathrm { A r } [ q ]  \mathcal { C }$in$s _ { q } \mathcal { C }$to$Y \colon \mathrm { A r } [ q ]  { \mathcal { D } }$, defined as the composite

$$
\operatorname{Ar} [ q ] \stackrel {(X, \operatorname{Ar} (\zeta))} {\longrightarrow} \mathcal {C} \times \operatorname{Ar} [ 1 ] \stackrel {i d \times t} {\longrightarrow} \mathcal {C} \times [ 1 ] \stackrel {\Phi} {\longrightarrow} \mathcal {D}.
$$

Here t :$\mathrm { A r } [ 1 ]  [ 1 ]$takes$( i , j )$to$j ,$for all$i \leq j$in [1].

The object$Y _ { j , j }$equals$F ( * )$or$G ( * )$, depending on the value of$\zeta ( j )$, and both values equal ∗ by exactness of F and G. For$i \le j \le k$in$[ q ]$, the diagram $Y _ { i , j }  Y _ { i , k }  Y _ { j , k }$equals one of the diagrams

$$
\begin{array}{l} F (X _ {i, j}) \hookrightarrow F (X _ {i, k}) \twoheadrightarrow F (X _ {j, k}) \\ F (X _ {i, j}) \hookrightarrow G (X _ {i, k}) \twoheadrightarrow G (X _ {j, k}) \\ G (X _ {i, j}) \hookrightarrow G (X _ {i, k}) \twoheadrightarrow G (X _ {j, k}), \end{array}
$$

depending on the values of$\zeta ( j )$and$\zeta ( k )$. The first and third diagrams are cofiber sequences, by exactness of$F$and G. The second diagram is also a cofiber sequence, since$\phi$is a natural isomorphism. Hence Y lies in$s _ { q } \mathcal { D }$. [[Elaborat$\it { : 7 ] }$

To check naturality, let$\alpha \colon [ p ]  [ q ]$in$\Delta ,$and note that the diagram

$$
\begin{array}{c} \operatorname{Ar} [ p ] \xrightarrow {(\alpha^ {*} (X) , \operatorname{Ar} (\zeta \alpha))} \mathcal {C} \times \operatorname{Ar} [ 1 ] \xrightarrow {i d \times t} \mathcal {C} \times [ 1 ] \xrightarrow {\Phi} \mathcal {D} \\ \operatorname{Ar} (\alpha) \Biggl \downarrow \\ \operatorname{Ar} [ q ] \xrightarrow {(X , \operatorname{Ar} (\zeta))} \mathcal {C} \times \operatorname{Ar} [ 1 ] \xrightarrow {i d \times t} \mathcal {C} \times [ 1 ] \xrightarrow {\Phi} \mathcal {D} \end{array}
$$

commutes. Hence the square

$$
\begin{array}{c} s _ {q} \mathcal {C} \xrightarrow {\phi_ {\zeta} ^ {*}} s _ {q} \mathcal {D} \\ \alpha^ {*} \Biggl \downarrow \\ s _ {p} \mathcal {C} \xrightarrow {\phi_ {\zeta \alpha} ^ {*}} s _ {p} \mathcal {D} \end{array}
$$

commutes.

Remark 8.5.7. To illustrate, for a 1-simplex X in$s _ { \bullet } \mathcal { C }$, the simplicial homotopy traces out the square

![](images/page_44_image_14.jpg)

in$s _ { \bullet } \mathcal { D }$, where the lower 2-simplex is given by the cofiber sequence

$$
F (X) \xrightarrow {\phi_ {X}} G (X) \longrightarrow *
$$

and the upper 2-simplex is given by the cofiber sequence

$$
* \longrightarrow G (X) \stackrel {=} {\longrightarrow} G (X).
$$

For a q-simplex$X \colon \mathrm { A r } [ q ]  \mathcal { C } .$, as ζ ranges through$\Delta _ { q } ^ { 1 }$the q-simplices$\phi _ { \zeta } ^ { * } ( X )$ range from$F \circ X$to$G \circ X$. When$\zeta = \zeta _ { k } ^ { q }$takes$\left\{ 0 , \ldots , k ^ { \stackrel { - } { - } 1 } \right\}$to 0 and$\{ k , \ldots , q \}$ to$1 , \phi _ { \zeta } ^ { * } ( X ) \colon \mathrm { A r } [ q ]  { \mathcal { D } }$takes the values$F ( X _ { i , j } )$at the$( i , j )$with$j < k ,$, and the values$G ( X _ { i , j } )$at the$( i , j )$with$j \geq k$. In other words,$\phi _ { \zeta } ^ { * } ( X )$is given by the cofiber sequence

$$
* \mapsto F (X _ {1}) \mapsto \dots \mapsto F (X _ {k - 1}) \mapsto G (X _ {k}) \mapsto \dots \mapsto G (X _ {q}),
$$

together with the choices of subquotients$F ( X _ { j } ) / F ( X _ { i } ) = F ( X _ { i , j } )$for$i \leq j <$ $k , G ( X _ { j } ) / F ( X _ { i } ) = G ( X _ { i , j } )$for$i < k \le j$and$G ( X _ { j } ) / G ( X _ { i } ) \ = \ G ( X _ { i , j } )$for $k \leq i \leq j .$

Remark 8.5.8. Lemma 8.5.6 is not just a special case of Segal’s Proposition 7.1.17, since$s _ { \bullet } \mathcal { C }$can be identified with the subcategory of identity morphisms in$S _ { \bullet } \mathcal { C }$, not the subcategory$i S _ { \bullet } \mathcal { C }$of isomorphisms. The lemma relies essentially on the closure of cofiber sequences under isomorphism.

Corollary 8.5.9. An exact equivalence$F \colon \mathcal { C } \stackrel { \simeq } { \longrightarrow } \mathcal { D } \ o f$categories with cofibrations [[with exact inverse]] induces a simplicial homotopy equivalence

$$
s _ {\bullet} F \colon s _ {\bullet} \mathcal {C} \stackrel {{\simeq}} {{\longrightarrow}} s _ {\bullet} \mathcal {D}.
$$

Proof. Let$G \colon { \mathcal { D } } \xrightarrow { \simeq } { \mathcal { C } }$be an exact inverse equivalence. Then$s _ { \bullet } G \colon s _ { \bullet } \mathcal { D } \longrightarrow s _ { \bullet } \mathcal { C }$ provides the simplicial homotopy inverse, by Lemma 8.5.6.□

Corollary 8.5.10. Let$( \mathcal { C } , i \mathcal { C } )$be a Waldhausen category, where$i \mathcal { C }$is the subcategory of isomorphisms. There is a homotopy equivalence

$$
s _ {\bullet} \mathcal {C} \stackrel {{\simeq}} {{\longrightarrow}} i S _ {\bullet} \mathcal {C}.
$$

Proof. Consider the simplicial object

$$
[ m ] \mapsto N _ {m} i S _ {\bullet} \mathcal {C}
$$

in sSet, and note that$s _ { \bullet } \mathcal { C } = N _ { 0 } i S _ { \bullet } \mathcal { C }$. Recall Example 6.6.8. Viewing$s _ { \bullet } \mathcal { C }$as a constant simplicial object, there is a simplicial map$s _ { \bullet } \mathcal { C } \to N _ { \bullet } i S _ { \bullet } \mathcal { C }$given in simplicial degree m by the m-fold degeneracy map

$$
\rho_ {m} ^ {*} \colon s _ {\bullet} \mathcal {C} \longrightarrow N _ {m} i S _ {\bullet} \mathcal {C}
$$

where$\rho _ { m } \colon [ m ] \ \to \ [ 0 ]$is (the unique morphism) in ∆. Here$N _ { m } i S _ { \bullet } { \mathcal { C } }$is$s _ { \bullet } \mathcal { D }$ for the category with cofibrations$\mathcal { D } = N _ { m } i \mathcal { C }$, and$\rho _ { m } ^ { * }$is induced by the exact functor$\mathcal { C } \longrightarrow N _ { m } i \mathcal { C }$taking each object to m copies of the identity isomorphism on that object. [[Explain the cofibration structure on$N _ { m } i \mathcal { C } ? ]$

Let$\epsilon _ { m } \colon [ 0 ] \\to [ m ]$take 0 to m. The exact functor$\epsilon _ { m } ^ { * } \colon N _ { m } i \mathcal { C } \to \mathcal { C }$takes a chain

$$
X _ {0} \xrightarrow {\cong} \dots \xrightarrow {\cong} X _ {n}
$$

of m composable isomorphisms in$\mathcal { C }$to the target object$X _ { m }$. The composite $\epsilon _ { m } ^ { * } \rho _ { m } ^ { * }$is the identity on${ \mathcal { C } } ,$while the composite$\rho _ { m } ^ { * } \epsilon _ { m } ^ { * }$is naturally isomorphic to the identity on$N _ { m } i \mathcal { C } .$. [[Elaborate?]] Hence$\rho _ { m } ^ { * }$is a weak homotopy equivalence, by Lemma 8.5.6. Since this holds for each$m \geq 0$, the inclusion$s _ { \bullet } \mathcal { C } \to N _ { \bullet } i S _ { \bullet } \mathcal { C }$ is a weak homotopy equivalence by the realization lemma.□

The additivity theorem will be deduced from the following lemma.

Lemma 8.5.11. Let$\mathcal { C }$be a category with cofibrations. The simplicial map

$$
s _ {\bullet} (s, q) \colon s _ {\bullet} S _ {2} \mathcal {C} \xrightarrow {\simeq} s _ {\bullet} \mathcal {C} \times s _ {\bullet} \mathcal {C}
$$

is a weak homotopy equivalence.

Proof. We apply Lemma$\mathrm { A ^ { * } }$to the simplicial maps$f _ { \bullet } = s _ { \bullet } s \colon s _ { \bullet } S _ { 2 } \mathcal { C } \to s _ { \bullet } \mathcal { C }$ and$g _ { \bullet } = s _ { \bullet } q \colon s _ { \bullet } S _ { 2 } \mathcal { C } \to s _ { \bullet } \mathcal { C }$

An n-simplex in$f _ { \bullet } / ( q , X ^ { \prime } )$consists of a morphism$\alpha \colon [ n ]  [ q ]$and a cofiber sequence$X \longmapsto Y \twoheadrightarrow Z$in$S _ { n } \mathcal { C }$, such that$X = \alpha ^ { * } ( X ^ { \prime } )$.

![](images/page_46_image_9.jpg)

We must prove that for each$q \geq 0$and$X ^ { \prime } \in s _ { q } \mathcal { C }$, the composite map

$$
p _ {\bullet} \colon f _ {\bullet} / (q, X ^ {\prime}) \longrightarrow s _ {\bullet} S _ {2} \mathcal {C} \stackrel {g _ {\bullet}} {\longrightarrow} s _ {\bullet} \mathcal {C}
$$

is a weak homotopy equivalence. The map$p _ { \bullet }$takes$( \alpha , X \longmapsto Y \twoheadrightarrow Z )$to the n-simplex$Z$in$s _ { \bullet } \mathcal { C }$. In fact,$p _ { \bullet }$is a simplicial deformation retraction. Let

$$
j _ {\bullet} \colon s _ {\bullet} \mathcal {C} \to f _ {\bullet} / (q, X ^ {\prime})
$$

map$Z \in s _ { n } \mathcal { C }$to$( \epsilon _ { q } \rho _ { n } , * \left. Z \stackrel { = } { \right. } Z )$, where$\epsilon _ { q } \rho _ { n } \colon [ n ] \\to [ q ]$takes each$i \in [ n ]$ to the last vertex$q \in [ q ]$This makes sense, since$\epsilon _ { q } ^ { * } ( X ^ { \prime } ) = * \mathrm { ~ i n ~ } s _ { 0 } \mathcal { C }$, which degenerates by$\rho _ { n } ^ { * }$to ∗ in$s _ { n } \mathcal { C }$

The composite$p _ { \bullet } \circ j _ { \bullet } \colon s _ { \bullet } \mathcal { C } \ \to \ s _ { \bullet } \mathcal { C }$is the identity, while the composite $j _ { \bullet } \circ p _ { \bullet } \colon f _ { \bullet } / ( q , X ^ { \prime } ) \to f _ { \bullet } / ( q , X ^ { \prime } )$takes$( \alpha , X \longmapsto Y \twoheadrightarrow Z )$to$( \epsilon _ { q } \rho _ { n } , * \left. Z \right. Z )$ Following Waldhausen, we shall construct an explicit simplicial homotopy from the identity on$f _ { \bullet } / ( q , X ^ { \prime } )$to the composite$j _ { \bullet } \circ p _ { \bullet }$

This simplicial homotopy lifts the simplicial contraction of Example 7.1.24, from the identity on$\Delta _ { \bullet } ^ { q }$to the constant map$\epsilon _ { q } \rho _ { \bullet }$to the terminal vertex q. Let the functor$H \colon [ q ] \times [ 1 ] \to [ q ]$be given by${ \cal H } ( i , \bar { 0 } ) = i$and$H ( i , 1 ) = q$, for$i \in [ q ]$2 representing the natural transformation from the identity on [q] to the constant functor to q. The simplicial contraction is given by the natural transformation $h \colon ( \Delta ^ { q } ) ^ { * } \Longrightarrow ( \Delta ^ { q } ) ^ { * }$with components$h _ { \zeta }$for$\zeta \colon [ n ]  [ 1 ]$, taking$\alpha \colon [ n ]  [ q ]$to $\bar { \alpha } = h _ { \zeta } ( \alpha )$equal to the composite

$$
\bar {\alpha} \colon [ n ] \stackrel {(\alpha , \zeta)} {\longrightarrow} [ q ] \times [ 1 ] \stackrel {H} {\longrightarrow} [ q ].
$$

The lifted simplicial homotopy

$$
\tilde {h} \colon (f _ {\bullet} / (q, X ^ {\prime})) ^ {*} \Longrightarrow (f _ {\bullet} / (q, X ^ {\prime})) ^ {*}
$$

will be defined to have components$\tilde { h } _ { \zeta } ,$, taking$( \alpha , X \longmapsto Y \twoheadrightarrow Z )$to

$$
(\bar {\alpha}, \bar {X} \mapsto \bar {Y} \twoheadrightarrow \bar {Z}).
$$

Here$\bar { \alpha } \colon [ n ]  [ q ]$is as above, and${ \bar { X } } = { \bar { \alpha } } ^ { * } ( X ^ { \prime } )$

To define$\bar { Y } , \bar { Z }$and the cofiber sequence$\bar { X } \ \longmapsto \ \bar { Y } \ \twoheadrightarrow \ \bar { Z } .$, we shall use a preferred morphism$X  { \bar { X } }$in$S _ { n } \mathcal { C }$. We have$\alpha ( i ) \leq \bar { \alpha } ( i )$in [q] for all$i \in [ n ]$ hence there is a (unique) natural transformation Ar α =⇒ Ar ¯α of functors $\mathrm { A r } [ n ] \to \mathrm { A r } [ q ]$, and an induced natural transformation$\alpha ^ { * } ( X ^ { \prime } ) \implies \bar { \alpha } ^ { * } ( X ^ { \prime } )$of functors$\mathrm { A r } [ n ] \to \mathcal { C }$. This is the preferred morphism$X  { \bar { X } }$. Its components are

$$
X _ {i, j} = X _ {\alpha (i), \alpha (j)} ^ {\prime} \longrightarrow X _ {\bar {\alpha} (i), \bar {\alpha} (j)} ^ {\prime} = \bar {X} _ {i, j}
$$

for all$i \leq j$in [n]. The cofiber sequence$\bar { X } \longmapsto \bar { Y } \twoheadrightarrow \bar { Z }$is now defined by cobase change from$X \longmapsto Y \twoheadrightarrow Z$along$X \to { \bar { X } }$

![](images/page_47_image_8.jpg)

This involves making choices of pushouts. To ensure naturality in$\zeta \colon [ n ]  [ 1 ]$9 these choices should be made in$\mathcal { C } ,$and extended pointwise to the diagram category$S _ { 2 } \mathcal { C }$. Then, to check that$\tilde { h }$is a natural transformation, consider a morphism$\beta \colon [ m ]  [ n ]$in$\Delta .$, viewed as a morphism from$\zeta \beta$to ζ in$\Delta / [ 1 ]$. The composite$\beta ^ { * } \circ \tilde { h } _ { \zeta }$takes$( \alpha , X \longmapsto Y \to Z ) \ \mathrm { t o } \ ( \bar { \beta } ^ { * } \bar { \alpha } , \beta ^ { * } \bar { X } \longmapsto \beta ^ { * } \bar { Y } \longmapsto \beta ^ { * } \bar { Z } )$, which is also the value of$\tilde { h } _ { \zeta \beta }$on$( \beta ^ { * } \alpha , \beta ^ { * } X  \beta ^ { * } Y \twoheadrightarrow \beta ^ { * } Z )$. [[See [68, p. 340] for further discussion.]]

When$\zeta ( i ) = 0$for all$i \in [ n ] , \alpha = \bar { \alpha }$and${ \bar { X } } = X$. When$\zeta ( i ) = 1$for all$i ,$ $\alpha = \epsilon _ { q } \rho _ { n }$and$\bar { X } = *$. If we additionally ensure that the pushout are chosen so that${ \bar { Y } }  { \bar { Y } }$is the identity$\mathrm { i f } X  \bar { X }$is the identity, and$\bar { Y }  \bar { Z }$is the identity if$\bar { X } = *$, then$\tilde { h }$is indeed a simplicial homotopy from the identity to$j _ { \bullet } \circ p _ { \bullet }$ [[Slight issue: if$X _ { i , j } = \bar { X } _ { i , j } = *$, should the pushout of$\bar { X } _ { i , j } \left. X _ { i , j } \right. Y _ { i , j }$be $Y _ { i , j }$or$Z _ { i , j } ?$May be allowed to depend on$\zeta ( i ) . ] ]$□

[[Comment: The simplicial homotopy$\tilde { h }$fibers over$s _ { \bullet } \mathcal { C }$via$p _ { \bullet }$, which should mean that$| p _ { \bullet } |$has contractible point inverses. The simplicial sets involved are rarely finite, but are$p _ { \bullet }$and$s _ { \bullet } ( s , q )$simple homotopy equivalences in any useful sense?]]

Proof of the additivity theorem. We wish to prove that the bisimplicial map

$$
(s, q) _ {\bullet , \bullet} \colon N _ {\bullet} w S _ {\bullet} S _ {2} \mathscr {C} \longrightarrow N _ {\bullet} w S _ {\bullet} \mathscr {C} \times N _ {\bullet} w S _ {\bullet} \mathscr {C}
$$

is a weak homotopy equivalence. We view this as a map of simplicial objects in sSet, given in simplicial degree m by

$$
(s, q) _ {m, \bullet} \colon N _ {m} w S _ {\bullet} S _ {2} \mathcal {C} \longrightarrow N _ {m} w S _ {\bullet} \mathcal {C} \times N _ {m} w S _ {\bullet} \mathcal {C}.
$$

For each$m \geq 0$, let${ \mathcal { C } } ( m , w ) \subseteq \mathbf { F u n } ( [ m ] , { \mathcal { C } } )$be the full subcategory generated by the functors that takes values in$w \mathcal { C }$, i.e., the diagrams

$$
X ^ {0} \stackrel {{\sim}} {{\longrightarrow}} X ^ {1} \stackrel {{\sim}} {{\longrightarrow}} \dots \stackrel {{\sim}} {{\longrightarrow}} X ^ {m}.
$$

Then$\mathcal { C } ( m , w )$is a subcategory with cofibrations of$\mathbf { F u n } ( [ m ] , \mathcal { C } )$, and$[ m ] \mapsto$ $\mathcal { C } ( m , w )$defines a simplicial category with cofibrations. There are simplicial isomorphisms

$$
N _ {m} w S _ {\bullet} \mathcal {C} \cong s _ {\bullet} \mathcal {C} (m, w)
$$

and

$$
N _ {m} w S _ {\bullet} S _ {2} \mathcal {C} \cong s _ {\bullet} S _ {2} \mathcal {C} (m, w),
$$

and the map$( s , q ) _ { m , \bullet }$<sub>•</sub> can be rewritten as the map

$$
s _ {\bullet} (s, q) \colon s _ {\bullet} S _ {2} \mathscr {C} (m, w) \longrightarrow s _ {\bullet} \mathscr {C} (m, w) \times s _ {\bullet} \mathscr {C} (m, w)
$$

of Lemma 8.5.11, for the category with cofibrations$\mathcal { C } ( m , w )$. Hence$( s , q ) _ { m , \bullet }$is a weak equivalence for each$m \geq 0$, and the bisimplicial map$( s , q ) _ { \bullet , \bullet }$is a weak equivalence by the realization lemma.□

## 8.6 Delooping K-theory

[[Introduction, reference to [68, 1.5]]]

Definition 8.6.1. Let$P \colon \Delta \to \Delta$be the shift functor taking [q] to$P [ q ] =$ $[ q + 1 ]$and$\alpha \colon [ p ]  [ q ]$to$P \alpha \colon [ p + 1 ] \ \to \ [ q + 1 ]$, given by$P \alpha ( 0 ) = 0$and $P \alpha ( i + 1 ) = \alpha ( i ) + 1 { \mathrm { ~ f o r ~ } } i \in [ p ]$

Given a simplicial object$X _ { \bullet }$in a category D, i.e., a functor$X \colon \Delta ^ { o p }  { \mathcal { D } }$ let the path object$P X$<sub>•</sub> be given by the composite functor$X \circ P ^ { o p } \colon \Delta ^ { o p }  \mathcal { D }$ so that$( P X ) _ { q } = X _ { q + 1 }$for all$q \geq 0$

The 0-th face maps$\delta _ { 0 } ^ { q + 1 } \colon [ q ] \ \to \ [ q + 1 ]$induce a natural transformation $i d \Longrightarrow P$and a simplicial map

$$
d _ {0} \colon P X _ {\bullet} \longrightarrow X _ {\bullet},
$$

given by$d _ { 0 } \colon P X _ { q } = X _ { q + 1 }  X _ { q }$for each$q \geq 0$. The inclusion of zero-simplices induces maps$X _ { 1 } = P X _ { 0 }  P X _ { }$<sub>•</sub> and$X _ { 0 }  X _ { \bullet }$, and the square

$$
\begin{array}{c} X _ {1} \longrightarrow P X _ {\bullet} \\ d _ {0} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ X _ {0} \longrightarrow X _ {\bullet} \end{array}
$$

commutes.

[[Discuss P sing(Y)<sub>•</sub> as an example.]]

Lemma 8.6.2. There is a simplicial homotopy equivalence$P X \simeq X _ { 0 }$

[[See [68, 1.5.1].]]

We apply this when$X _ { \bullet } = w S _ { \bullet } \mathcal { C }$for a Waldhausen category$( \mathcal { C } , w \mathcal { C } )$. Then $X _ { 0 } = w S _ { 0 } \mathcal { C } = *$and$X _ { 1 } = w S _ { 1 } \mathcal { C } \cong w \mathcal { C }$, so we have a diagram of simplicial categories

$$
w \mathcal {C} \longrightarrow P (w S _ {\bullet} \mathcal {C}) \stackrel {d _ {0}} {\longrightarrow} w S _ {\bullet} \mathcal {C},\tag{8.3}
$$

with constant composite. By the lemma above,$P ( w S _ { \bullet } \mathcal { C } )$is simplicially contractible. A choice of contraction of$| P ( w S _ { \bullet } \mathcal { C } ) |$thus determines a map

$$
\iota \colon | w \mathscr {C} | \longrightarrow \Omega | w S _ {\bullet} \mathscr {C} | = K (\mathscr {C}, w).
$$

Lemma 8.6.3. The simplicial contraction of$P ( w S _ { \bullet } \mathcal { C } )$can be chosen so that ι is (homotopic to) the map from Definition$\ 8 . 4 . \mathcal { Q } .$

[[See [68, 1.5.2].]]

In general ι is not a homotopy equivalence, so diagram (8.3) is not a fibration up to homotopy. This situation improves greatly after applying the$S _ { \bullet }$ construction one more time.

Proposition 8.6.4. Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. The diagram

$$
w S _ {\bullet} \mathcal {C} \longrightarrow P (w S _ {\bullet} S _ {\bullet} \mathcal {C}) \stackrel {d _ {0}} {\longrightarrow} w S _ {\bullet} S _ {\bullet} \mathcal {C}
$$

is a fibration up to homotopy. Hence the map

$$
\iota \colon | w S _ {\bullet} \mathcal {C} | \xrightarrow {\simeq} \Omega | w S _ {\bullet} S _ {\bullet} \mathcal {C} |
$$

is a homotopy equivalence.

[[See [68, 1.5.3].]]

Proof. We may assume that the path object construction acts on the second of the two$S _ { \bullet }$constructions. We use the fibration criterion of Proposition 6.8.2. It sufices to show that

$$
w S _ {\bullet} \mathcal {C} \longrightarrow P (w S _ {\bullet} S _ {\bullet} \mathcal {C}) _ {q} \stackrel {d _ {0}} {\longrightarrow} w S _ {\bullet} S _ {q} \mathcal {C}
$$

is a fibration up to homotopy for each$q \geq 0 ,$since w$S _ { \bullet } S _ { q } \mathcal { C }$is connected for each q. In view of the definition of the path object functor, we can rewrite this diagram as

$$
w S _ {\bullet} \mathcal {C} \longrightarrow w S _ {\bullet} S _ {q + 1} \mathcal {C} \stackrel {d _ {0}} {\longrightarrow} w S _ {\bullet} S _ {q} \mathcal {C}.
$$

This is the diagram we obtain by applying w$\therefore S _ { \bullet } ( - )$to

$$
\mathcal {C} \longrightarrow S _ {q + 1} \mathcal {C} \stackrel {d _ {0}} {\longrightarrow} S _ {q} \mathcal {C},
$$

and we shall use the additivity theorem to see that this is homotopy equivalent to the product fibration obtained by applying$w S _ { \bullet } ( - )$to

$$
\mathcal {C} \longrightarrow \mathcal {C} \times S _ {q} \mathcal {C} \stackrel {p r _ {2}} {\longrightarrow} S _ {q} \mathcal {C}.
$$

Let$\eta _ { 1 } ^ { * } \colon S _ { q + 1 } \mathcal { C } \to \mathcal { C }$take$X \colon \operatorname { A r } [ q + 1 ] \to \ell$to$X _ { 0 , 1 }$. (It is induced by the morphism$\eta _ { 1 } \colon [ 1 ] \to [ q + 1 ]$from Definition 7.1.5.) We get a commutative diagram

![](images/page_49_image_22.jpg)

where$\tau = ( \eta _ { 1 } ^ { * } , d _ { 0 } )$takes an object

$$
X _ {0, 1} \rightharpoonup X _ {0, 2} \rightharpoonup \dots \rightharpoonup X _ {0, q + 1}
$$

(plus choices of subquotients) in$S _ { q + 1 } { \mathcal { C } }$to

$$
(X _ {0, 1}, X _ {1, 2} \rightharpoonup \dots \rightharpoonup X _ {1, q + 1})
$$

(plus choices of subquotients) in$\mathcal { C } \times S _ { q } \mathcal { C }$

We can identify$\mathcal { C }$with the full subcategory of$S _ { q + 1 } { \mathcal { C } }$where all cofibrations $X _ { 0 , j - 1 } \ \longmapsto \ X _ { 0 , j }$are identities and all subquotients are ∗. Similarly, we can identify$S _ { q } \mathcal { C }$with the full subcategory of$S _ { q + 1 } { \mathcal { C } }$where$X _ { 0 , 1 } = *$and the quotient maps$X _ { 0 , j } \twoheadrightarrow X _ { 1 , j }$are identities. Using these identifications, the exact functor $\tau \colon S _ { q + 1 } \mathcal { C } \to \mathcal { C } \times S _ { q } \mathcal { C }$has an exact section σ given by the composite

$$
\mathcal {C} \times S _ {q} \mathcal {C} \subset S _ {q + 1} \mathcal {C} \times S _ {q + 1} \mathcal {C} \stackrel {\vee} {\longrightarrow} S _ {q + 1} \mathcal {C},
$$

taking$( X _ { 0 , 1 } , X _ { 1 , 2 } \dots \longmapsto . . . \longmapsto X _ { 1 , q + 1 } )$(with choices of subquotients) to

$$
X _ {0, 1} \rightharpoonup X _ {0, 1} \vee X _ {1, 2} \rightharpoonup \dots \rightharpoonup X _ {0, 1} \vee X _ {1, q + 1}
$$

(with the evident choices of subquotients).

The composite$\tau \circ \sigma$is the identity, while the composite$\sigma \circ \tau \colon S _ { q + 1 } \mathcal { C }$ $S _ { q + 1 } { \mathcal { C } }$is the wedge sum of the two exact functors

$$
F ^ {\prime}, F ^ {\prime \prime} \colon S _ {q + 1} \mathcal {C} \to S _ {q + 1} \mathcal {C}
$$

taking$X _ { 0 , 1 } \longmapsto X _ { 0 , 2 } \longmapsto \ldots \longmapsto X _ { 0 , q + 1 }$to

$$
X _ {0, 1} \stackrel {{=}} {{\longrightarrow}} X _ {0, 1} \stackrel {{=}} {{\longrightarrow}} \dots \stackrel {{=}} {{\longrightarrow}} X _ {0, 1}
$$

and

$$
* \mapsto X _ {1, 2} \mapsto \dots \mapsto X _ {1, q + 1},
$$

respectively. Let F be the identity functor on$S _ { q + 1 } { \mathcal { C } }$. Then there is a cofiber sequence of exact functors

$$
F ^ {\prime} \rightarrow F \twoheadrightarrow F ^ {\prime \prime}
$$

with components$X _ { 0 , 1 } \ \longmapsto \ { X _ { 0 , j } } \  \ { X _ { 1 , j } }$. Hence, by the additivity theorem (Corollary 8.5.4), there is a homotopy

$$
w S _ {\bullet} \sigma \circ w S _ {\bullet} \tau = w S _ {\bullet} (F ^ {\prime} \vee F ^ {\prime \prime}) \simeq w S _ {\bullet} F
$$

to the identity on w$S _ { \bullet } S _ { q + 1 } { \mathcal { C } }$. It follows that w$S _ { \bullet } \tau$is a homotopy equivalence, and we get the commutative diagram

$$
\begin{array}{c} w S _ {\bullet} \mathcal {C} \xrightarrow {} w S _ {\bullet} S _ {q + 1} \mathcal {C} \xrightarrow {d _ {0}} w S _ {\bullet} S _ {q} \mathcal {C} \\ = \Biggl \downarrow \qquad \simeq \Biggl \downarrow w S _ {\bullet} \tau \qquad \Biggl \downarrow = \\ w S _ {\bullet} \mathcal {C} \xrightarrow {} w S _ {\bullet} \mathcal {C} \times w S _ {\bullet} S _ {q} \mathcal {C} \xrightarrow {p r _ {2}} w S _ {\bullet} S _ {q} \mathcal {C}. \end{array}
$$

The lower row is clearly a fibration up to homotopy, hence so it the upper row.□

## 8.7 The iterated S<sub>•</sub>-construction

We can encode the fact that the algebraic K-theory space$K ( \mathcal { C } , w ) = \Omega | w S _ { \bullet } \mathcal { C } |$ is an infinite loop space in an algebraic K-theory spectrum. To discuss multiplicative properties, it is useful to use Jef Smith’s notion of a symmetric spectrum, see Hovey–Shipley–Smith [27].

Definition 8.7.1. A symmetric spectrum X (in topological spaces) is a sequence $\{ n \mapsto X _ { n } \}$of based Σ -spaces, with structure maps$\sigma \colon X _ { n } \wedge S ^ { 1 } \to X _ { n + 1 }$such that the k-fold iterate$\sigma ^ { k } \colon X _ { n } \wedge S ^ { k } \to X _ { n + k }$is$\left( \Sigma _ { n } \times \Sigma _ { k } \right)$-equivariant for each $n , k \geq 0$. Here$\Sigma _ { k }$acts on$S ^ { k } = S ^ { 1 } \wedge \cdot \cdot \cdot \wedge S ^ { 1 }$by permuting the smash factors, and$\Sigma _ { n } \times \Sigma _ { k }$is viewed as a subgroup of$\Sigma _ { n + k }$in the obvious way.

A map$\mathbf { f } : \mathbf { X }  \mathbf { Y }$of symmetric spectra is a sequence$\{ n \mapsto f _ { n } \colon X _ { n } \to Y _ { n } \}$ of based$\Sigma _ { n }$-equivariant maps, such that the square

$$
\begin{array}{c} X _ {n} \wedge S ^ {1} \xrightarrow {f _ {n} \wedge i d} Y _ {n} \wedge S ^ {1} \\ \sigma \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \sigma \\ X _ {n + 1} \xrightarrow {f _ {n + 1}} Y _ {n + 1} \end{array}
$$

commutes for each$n \geq 0$Let$\mathrm { S p ^ { \Sigma } }$be the category of symmetric spectra.

[[Level equivalence, stable equivalence.]]

The following constructions are discussed in [68, p. 330] and$[ 5 7 , \ \ S 1 ]$. The symmetric structure is emphasized in [21, §6].

Definition 8.7.2. Let$( \mathcal { C } , w \mathcal { C } )$be a Waldhausen category. The external n-fold $S _ { \bullet }$-construction on$\mathcal { C }$is the n-multisimplicial Waldhausen category

$$
(S _ {\bullet} \dots S _ {\bullet} \mathscr {C}, w S _ {\bullet} \dots S _ {\bullet} \mathscr {C}).
$$

In multidegree$( q _ { 1 } , \ldots , q _ { n } )$, it has objects the$\mathrm { A r } [ q _ { 1 } ] \times \cdot \cdot \cdot \times \mathrm { A r } [ q _ { n }$]-shaped diagrams

$$
X \colon \operatorname{Ar} [ q _ {1} ] \times \dots \times \operatorname{Ar} [ q _ {n} ] \longrightarrow \mathcal {C}
$$

such that

(a)

$$
X (i _ {1} \leq j _ {1}, \dots , i _ {n} \leq j _ {n}) = *
$$

if$i _ { t } = j _ { t }$in [q<sub>t</sub>] for some$1 \leq t \leq n$

(b)

$$
X (\dots , i _ {t} \leq j _ {t}, \dots) \mapsto X (\dots , i _ {t} \leq k _ {t}, \dots) \twoheadrightarrow X (\dots , j _ {t} \leq k _ {t}, \dots)
$$

is a cofiber sequence in the$( n - 1 )$-fold iterated$S _ { \bullet }$-construction, for each triple$i _ { t } \le j _ { t } \le k _ { t }$in$[ q _ { t } ]$

Let the internal n-fold$S _ { \bullet }$-construction

$$
(S _ {\bullet} ^ {(n)} \mathcal {C}, w S _ {\bullet} ^ {(n)} \mathcal {C})
$$

be the diagonal simplicial Waldhausen category, with q-simplices

$$
(S _ {q} ^ {(n)} \mathcal {C}, w S _ {q} ^ {(n)} \mathcal {C}) = (S _ {q} \dots S _ {q} \mathcal {C}, w S _ {q} \dots S _ {q} \mathcal {C}).
$$

It has objects the$( \operatorname { A r } [ q ] ) ^ { n } = \operatorname { A r } ( [ q ] ^ { n } )$-shaped diagrams

$$
X \colon \operatorname{Ar} [ q ] ^ {n} \longrightarrow \mathcal {C}
$$

such that

(a)

$$
X (i _ {1} \leq j _ {1}, \dots , i _ {n} \leq j _ {n}) = *
$$

if$i _ { t } = j _ { t }$in [q] for some$1 \leq t \leq n$

(b)

$$
X (\dots , i _ {t} \leq j _ {t}, \dots) \mapsto X (\dots , i _ {t} \leq k _ {t}, \dots) \twoheadrightarrow X (\dots , j _ {t} \leq k _ {t}, \dots)
$$

is a cofiber sequence in the$( n - 1 )$-fold iterated$S _ { \bullet }$-construction, for each triple$i _ { t } \le j _ { t } \le k _ { t }$in [q].

The symmetric group$\Sigma _ { n }$acts simplicially on$S _ { \bullet } ^ { ( n ) } \mathcal { C }$, by permuting the n copies of [q] in$\mathrm { A r } [ q ] ^ { n }$. More explicitly, for$\pi \in \Sigma _ { n }$

$$
(\pi \cdot X) (\dots , i _ {t} \leq j _ {t}, \dots) = X (\dots , i _ {\pi^ {- 1} (t)} \leq j _ {\pi^ {- 1} (t)}, \dots).
$$

Definition 8.7.3. The (symmetric) algebraic K-theory spectrum${ \bf K } ( \mathcal { C } , w )$of a small Waldhausen category$( \mathcal { C } , w \mathcal { C } )$has n-th space

$$
K (\mathcal {C}, w) _ {n} = | w S _ {\bullet} ^ {(n)} \mathcal {C} |
$$

based at$^ { * , }$with the$\Sigma _ { n }$-action induced by permuting the order of the$S _ { \bullet }$ constructions. The structure map$\sigma$is the composite

$$
\left| w S _ {\bullet} ^ {(n)} \mathcal {C} \right| \wedge S ^ {1} \cong \left| w S _ {\bullet} ^ {(n)} S _ {\bullet} \mathcal {C} \right| ^ {(1)} \subset \left| w S _ {\bullet} ^ {(n)} S _ {\bullet} \mathcal {C} \right| \cong \left| w S _ {\bullet} ^ {(n + 1)} \mathcal {C} \right|,
$$

where the superscript <sup>(1)</sup> indicates the 1-skeleton with respect to the last simplicial direction. See Lemma 8.4.1. The k-fold iterated structure map$\sigma ^ { k }$is then the composite

$$
\left| w S _ {\bullet} ^ {(n)} \mathcal {C} \right| \wedge S ^ {k} \cong \left| w S _ {\bullet} ^ {(n)} S _ {\bullet} \dots S _ {\bullet} \mathcal {C} \right| ^ {(1, \dots , 1)} \subset \left| w S _ {\bullet} ^ {(n)} S _ {\bullet} \dots S _ {\bullet} \mathcal {C} \right| \cong \left| w S _ {\bullet} ^ {(n + k)} \mathcal {C} \right|,
$$

where the superscript$( 1 , . . . , 1 )$indicates the multi-1-skeleton with respect to the k last simplicial directions. This map is clearly$\left( \Sigma _ { n } \times \Sigma _ { k } \right)$-equivariant.

Lemma 8.7.4. The algebraic K-theory spectrum is positively fibrant$( = a$semi-Ω-spectrum), in the sense that the adjoint structure maps

$$
K (\mathcal {C}, w) _ {n} \xrightarrow {\simeq} \Omega K (\mathcal {C}, w) _ {n + 1}
$$

are homotopy equivalences for all$n \geq 1$. Hence there are isomorphisms

$$
K _ {i} (\mathcal {C}, w) = \pi_ {i + 1} K (\mathcal {C}, w) _ {1} \cong \pi_ {i} \mathbf {K} (\mathcal {C}, w)
$$

for all$i \geq 0$

Proof. This is the map$\iota \colon | w S _ { \bullet } \mathcal { D } |  \Omega | w S _ { \bullet } S _ { \bullet } \mathcal { D } |$for$\mathscr { D } = S _ { \bullet } ^ { ( n - 1 ) } \mathscr { C }$, which is a homotopy equivalence by Proposition 8.6.4.□

Remark 8.7.5. We can also define${ \bf K } ( \mathcal { C } , w )$as a symmetric spectrum in simplicial sets, letting$K ( \mathcal { C } , w ) _ { n }$be the diagonal of$N _ { \bullet } w S _ { \bullet } ^ { ( n ) } \mathcal { C }$. Note that this is not a fibrant simplicial set (= a Kan complex) in most cases.

[[Reference for model structures?]]

[[Biexact functors$\mathcal { D } \times \mathcal { E }  \mathcal { C }$induce pairing$\mathbf { K } ( { \mathcal { D } } ) \wedge \mathbf { K } ( { \mathcal { E } } )  \mathbf { K } ( { \mathcal { C } } )$, taking $w S _ { \bullet } ^ { ( m ) } \mathcal { D } \times w S _ { \bullet } ^ { ( n ) } \mathcal { E }$to$w S _ { \bullet } ^ { ( m + n ) } \mathcal { C }$. Swallowing lemma.]]

## 8.8 The spectrum level rank filtration

[[Reference to$[ 5 7 ] . ] ]$

Definition 8.8.1. Let$\mathcal { C }$be a small category with cofibrations. We call

$$
\operatorname{rank} \colon \operatorname{obj} (\mathcal {C}) \to \mathbb {N} _ {0} = \{0, 1, 2, \dots \}
$$

a rank function if

(a) rank(X) = 0 if and only if$X \cong *$is a zero object.

(b) If$f \colon X \mapsto Y$is a cofibration then ran$\tau ( X ) \leq \mathrm { r a n k } ( Y )$, with$\operatorname { r a n k } ( X ) =$ rank(Y) only if$f$is an isomorphism.

(c) If$f \colon X \mapsto Y$is a cofibration then rank$( Y ) \geq \mathrm { r a n k } ( Y / X )$, with rank$( Y ) =$ rank$\boldsymbol { \mathsf { \Sigma } } ( Y / X )$only if$X \cong *$

Remark 8.8.2. If$f \colon X { \xrightarrow { \cong } } Y$is an isomorphism, then f and$f ^ { - 1 }$are cofibrations, so rank$\left( X \right) \leq \mathrm { r a n k } ( Y )$and ran$\mathfrak { z } ( Y ) \le \mathrm { r a n k } ( X )$, so rank$\iota ( X ) = \mathrm { r a n k } ( Y )$

Example 8.8.3. For a commutative ring$R ,$let${ \mathcal { C } } = { \mathcal { F } } ( R )$be the category of finitely generated free R-modules, with split injective cofibrations, and let rank$( R ^ { k } ) = k$. [[This also works for certain reasonable, non-commutative rings.]]

Example 8.8.4. Let$\mathcal { C } ~ = ~ \mathcal { F } _ { * }$<sub>∗</sub> be the category of finite pointed sets, with injective cofibrations, and let rank$( k _ { + } ) = k$, where$k _ { + } = \{ 0 , 1 , 2 , \ldots , k \}$is based at 0.

We consider the algebraic K-theory$K ( \mathcal { C } ) = K ( \mathcal { C } , i \mathcal { C } )$of$\mathcal { C }$with respect to the subcategory$i \mathcal { C } = \mathrm { i s o } ( \mathcal { C } )$of weak equivalences.

Definition 8.8.5. For each$k \geq 0$let$F _ { k } { \mathcal { C } } \subset { \mathcal { C } }$be the full pointed subcategory generated by the objects X with ran$\mathfrak { c } ( X ) \leq k$. For each level$n \geq 0$and degree $q \geq 0$let

$$
F _ {k} i S _ {q} ^ {(n)} \mathcal {C} \subset i S _ {q} ^ {(n)} \mathcal {C}
$$

be the full pointed subgroupoid generated by the objects$X \colon \mathrm { A r } [ q ] ^ { n }  \mathcal { C }$in $S _ { q } ^ { ( n ) } \mathcal { C }$that factor through$F _ { k } { \mathcal { C } } \subset { \mathcal { C } }$. Then$F _ { k } i S _ { \bullet } ^ { ( n ) } \mathcal { C } \subset i S _ { \bullet } ^ { ( n ) } \mathcal { C }$is a simplicial pointed subgroupoid, and we let

$$
F _ {k} \mathbf {K} (\mathcal {C}) \subset \mathbf {K} (\mathcal {C})
$$

be the symmetric subspectrum with n-th space

$$
F _ {k} K (\mathcal {C}) _ {n} = | F _ {k} i S _ {\bullet} ^ {(n)} \mathcal {C} | \subset | i S _ {\bullet} ^ {(n)} \mathcal {C} | = K (\mathcal {C}) _ {n}.
$$

It is clear that the Σ -action on$K ( \mathcal { C } ) _ { n }$restricts to$F _ { k } K ( { \mathcal { C } } ) _ { n } ,$and that the structure maps σ :$K ( \mathcal { C } ) _ { n } \wedge S ^ { 1 } \to K ( \mathcal { C } ) _ { n + 1 }$restrict to$\sigma \colon F _ { k } K ( \mathcal { C } ) _ { n } \wedge S ^ { 1 } \$ $F _ { k } K ( \mathcal { C } ) _ { n + 1 }$, satisfying the required equivariance property.

As k varies, we obtain a diagram of symmetric spectra

$$
F _ {0} \mathbf {K} (\mathcal {C}) \mapsto F _ {1} \mathbf {K} (\mathcal {C}) \mapsto \dots \mapsto F _ {k - 1} \mathbf {K} (\mathcal {C}) \mapsto F _ {k} \mathbf {K} (\mathcal {C}) \mapsto \dots \mapsto \mathbf {K} (\mathcal {C})
$$

where each map is a levelwise cofibration, and colim$F _ { k } \mathbf { K } ( \mathcal { C } ) \cong \mathbf { K } ( \mathcal { C } )$. This is the spectrum level rank filtration of$\mathbf { K } ( { \mathcal { C } } )$. In particular,

$$
\operatorname * {c o l i m} _ {k} \pi_ {i} F _ {k} \mathbf {K} (\mathcal {C}) \xrightarrow {\cong} \mathbf {K} _ {i} (\mathcal {C})
$$

for all$i \geq 0$

Lemma 8.8.6. There is a levelwise equivalence$F _ { 0 } \mathbf { K } ( \mathcal { C } ) \simeq *$

Proof. By condition (a) in the definition of a rank function,$F _ { 0 } i S _ { q } ^ { ( n ) } \mathcal { C }$is the pointed groupoid of diagrams$X \colon \mathrm { A r } [ q ] ^ { n } \to F _ { 0 } \mathcal { C }$, all uniquely isomorphic to the constant diagram at the chosen zero object ∗. Hence$F _ { 0 } i S _ { q } ^ { ( n ) } \mathcal { C }$is contractible for each q, so$| F _ { 0 } i S _ { \bullet } ^ { ( n ) } \mathcal { C } | = F _ { 0 } \mathbf { K } ( \mathcal { C } ) _ { n }$is contractible by the realization lemma.

Lemma 8.8.7. Let$k \geq 1$. An object$X \colon \mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$in$S _ { q } ^ { ( n ) } \mathcal { C }$lies in$F _ { k } i S _ { q } ^ { ( n ) } \mathcal { C }$ but not in$F _ { k - 1 } i S _ { q } ^ { ( n ) } \mathcal { C } \ i f$and only if

$$
\operatorname{rank} X (0 \leq q, \dots , 0 \leq q) = k.
$$

Proof. In view of the cofibration

$$
X (0 \leq j _ {1}, \dots , 0 \leq j _ {n}) \mapsto X (0 \leq q, \dots , 0 \leq q)
$$

and quotient map [[Explain?]]

$$
X (0 \leq j _ {1}, \dots , 0 \leq j _ {n}) \twoheadrightarrow X (i _ {1} \leq j _ {1}, \dots , i _ {n} \leq j _ {n})
$$

it is clear that

$$
\operatorname{rank} X \left(i _ {1} \leq j _ {1}, \dots , i _ {n} \leq j _ {n}\right) \leq X (0 \leq q, \dots , 0 \leq q)
$$

for all$( i _ { 1 } \leq j _ { 1 } , \ldots , i _ { n } \leq j _ { n } )$in$\mathrm { A r } [ q ] ^ { n }$. Hence X factors through$F _ { k } \mathcal { C }$if and only if rank$X ( 0 \leq q , \ldots , 0 \leq q ) \leq k$口

Definition 8.8.8. For each object X :$\operatorname { A r } [ q ] ^ { n } \to \mathcal { C }$in$S _ { q } ^ { ( n ) } \mathcal { C }$we call

$$
X (0 \leq q, \dots , 0 \leq q)
$$

the top object of X. Its rank is the top rank of$X$.

Definition 8.8.9. For$k \geq 1$, let

$$
\bar {F} _ {k} \mathbf {K} (\mathcal {C}) = F _ {k} \mathbf {K} (\mathcal {C}) / F _ {k - 1} \mathbf {K} (\mathcal {C})
$$

be the k-th subquotient spectrum in the rank filtration. It has n-th space $\bar { F } _ { k } K ( \mathcal { C } ) _ { n } = | \bar { F } _ { k } i S _ { \bullet } ^ { ( n ) } \mathcal { C } |$where

$$
\bar {F} _ {k} i S _ {\bullet} ^ {(n)} \mathcal {C} = F _ {k} i S _ {\bullet} ^ {(n)} \mathcal {C} / F _ {k - 1} i S _ {\bullet} ^ {(n)} \mathcal {C}
$$

is the simplicial pointed groupoid obtained from$F _ { k } i S _ { \bullet } ^ { ( n ) } \mathcal { C }$by identifying all $X \colon \mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$with top rank$< k$to the base point object, with trivial automorphism group.

In simplicial degree$q ,$the pointed groupoid$\bar { F } _ { k } i S _ { q } ^ { ( n ) } \mathcal { C }$has objects the base point, together with the diagrams$X \colon \mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$in$S _ { q } ^ { ( n ) } \mathcal { C }$with top rank k. For each α:$[ p ]  [ q ]$the simplicial operator$\alpha ^ { * }$takes$X$to

$$
X \circ \operatorname{Ar} (\alpha) ^ {n} \colon \operatorname{Ar} [ p ] ^ {n} \to \mathscr {C}
$$

in$S _ { p } ^ { ( n ) } \mathcal { C }$whenever this has top rank k, and to the base point object otherwise. Note that if$\alpha ( 0 ) = a$and$\alpha ( p ) = b$, then the top object of$X \circ \operatorname { A r } ( \alpha ) ^ { n }$is $X ( a \leq b , \ldots , a \leq b )$

Definition 8.8.10. The embedding$[ q ] \to \operatorname { A r } [ q ]$induces embeddings$[ q ] ^ { n }$ $\mathrm { A r } [ q ] ^ { n }$taking$( j _ { 1 } , \ldots , j _ { n } )$to$( 0 \leq j _ { 1 } , \ldots , 0 \leq j _ { n } )$, for all$n \geq 0$The ndimensional cube$[ q ] ^ { n }$is partially ordered with the product ordering, so that $u = ( i _ { 1 } , \ldots , i _ { n } )$and$v = ( j _ { 1 } , \ldots , j _ { n } )$satisfy$u \leq v$if and only i$i _ { 1 } \leq j _ { 1 } , \ldots , i _ { n } \leq$ $j _ { n }$. For$X \colon \mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$let its restriction

$$
\bar {X} \colon [ q ] ^ {n} \to \mathcal {C}
$$

be the composite$[ q ] ^ { n } \to \mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$. The top object of$\bar { X }$is the top object

$$
\bar {X} (q, \dots , q) = X (0 \leq q, \dots , 0 \leq q)
$$

of X.

Definition 8.8.11. We say that${ \bar { X } } \colon [ q ] ^ { n } \to \mathcal { C }$is a lattice$( n - )$cube if

(a)$\bar { X } ( i _ { 1 } , \ldots , i _ { n } ) = *$whenever some$i _ { t } = 0 , 1 \le t \le n .$

(b) For each$v \in [ q ] ^ { n }$the canonical map

$$
\underset {u <   v} {\operatorname{colim}} \bar {X} (u) \mapsto \bar {X} (v)
$$

is a cofibration in$\mathcal { C }$, where the colimit ranges over the$u \in [ q ] ^ { n }$that are strictly smaller than v in the product partial ordering.

[[Explain why the colimit exists, by induction on$v . ] ]$

Lemma 8.8.12. A diagram${ \bar { X } } \colon [ q ] ^ { n } \to \mathcal { C }$is the restriction of an object X in $S _ { q } ^ { ( n ) } \mathcal { C } \ i f$and only$i f { \bar { X } }$is a lattice cube.

Proof. For$n = 1$, an object X :$\operatorname { A r } [ q ] \to \mathcal { C }$in$S _ { q } \mathcal { C }$consists of a sequence

$$
X _ {0} \longrightarrow X _ {1} \longrightarrow \dots \longrightarrow X _ {q}
$$

in$\mathcal { C } _ { : }$where$X _ { 0 } ~ = ~ *$and each$X _ { i - 1 } \ \longmapsto \ X _ { i }$is a cofibration, together with compatible choices of quotients$X ( i \leq j ) \cong X _ { j } / X _ { i }$. The restriction$X \mapsto { \bar { X } }$ forgets the choices of quotients.

For$n = 2 .$, an object$X \colon \mathrm { A r } [ q ] ^ { 2 } \to \mathcal { C }$in$S _ { q } ^ { ( 2 ) } \mathcal { C }$consists of a$q \times q$square

![](images/page_55_chart_16.jpg)

in$\mathcal { C } .$, where$X _ { i _ { 1 } , 0 } = X _ { 0 , i _ { 2 } } = *$and each pushout morphism

$$
X _ {i _ {1}, i _ {2} - 1} \cup_ {X _ {i _ {1} - 1, i _ {2} - 1}} X _ {i _ {1} - 1, i _ {2}} \mapsto X _ {i _ {1}, i _ {2}}
$$

is a cofibration, together with compatible choices of quotients. By induction each morphism$X _ { i _ { 1 } , i _ { 2 } - 1 } \ \longmapsto \ X _ { i _ { 1 } , i _ { 2 } }$and$X _ { i _ { 1 } - 1 , i _ { 2 } } \ \longmapsto \ X _ { i _ { 1 } , i _ { 2 } }$is a cofibration, so each pushout exists, and the$q \times q$square is a diagram of lattice squares.

For$n \geq 3$, an object X :$\operatorname { A r } [ q ] ^ { n } \to \mathcal { C }$in$S _ { q } ^ { ( n ) } \mathcal { C }$consists of a$q \times q$square as above, in$S _ { q } ^ { ( n - 2 ) } \mathcal { C }$, where$X _ { i _ { 1 } , 0 } = X _ { 0 , i _ { 2 } } = *$and each pushout morphism

$$
X _ {i _ {1}, i _ {2} - 1} \cup_ {X _ {i _ {1} - 1, i _ {2} - 1}} X _ {i _ {1} - 1, i _ {2}} \hookrightarrow X _ {i _ {1}, i _ {2}}
$$

is a cofibration in$S _ { q } ^ { ( n - 2 ) } \mathcal { C }$, together with compatible choices of quotients. $\mathrm { [ [ E T C ] ] }$□

Definition 8.8.13 (Category of subobjects). Let$Z$be an object in a category with cofibrations$( \mathcal { C } , c o \mathcal { C } )$. The over category$c o \mathcal { C } / Z$has objects cofibrations$X  Z$with target Z, and morphisms$( { \bar { X } } ^ { \prime } \stackrel { \cdot  } { \longrightarrow } Z ) \stackrel { \cdot } {  } ( X \stackrel { \cdot  } {  } Z )$given by cofibrations$X ^ { \prime } \mapsto X$making the triangle

![](images/page_56_image_5.jpg)

commute. By a category of subobjects$\mathbf { S u b } ( Z )$we mean a skeleton of the over category$c o \mathcal { C } / Z$, containing the objects$*  Z$and$i d _ { Z } \colon Z \mapsto Z$. In other words,$\mathbf { S u b } ( Z )$is to be a full subcategory of$c o \mathcal { C } / Z$that contains exactly one object in each isomorphism class. The inclusion

$$
\operatorname{Sub} (Z) \xrightarrow {\simeq} c o \mathscr {C} / Z
$$

is then an equivalence of categories. We think of the preferred element in the isomorphism class of$X  Z$as the image of X in$Z .$

[[If the cofibrations are categorical monomorphisms, then$c o \mathcal { C } / Z$and Sub(Z) will be a preorder and a partially ordered set, respectively.]]

Example 8.8.14. For a [[reasonable]] ring$R ,$the free R-module$R ^ { k }$has a category of subobjects (= submodules) Sub$\mathbf { \xi } ^ { \prime } R ^ { k } ) \subset c o \mathcal { F } ( R ) / R ^ { k }$given by the partially ordered set of free submodules$L \subseteq R ^ { k }$with free quotient$R ^ { k } / L$, where $L ^ { \prime } \leq L$if and only if$L ^ { \prime } \subseteq L$with$L / L ^ { \prime }$free.

Example 8.8.15. The finite pointed set$k _ { + }$has a category of subobjects$( =$ subsets) Sub$( k _ { + } ) \subset c o \mathcal { F } _ { * } / k _ { + }$given by the partially ordered set of pointed subsets$X \subseteq k _ { + }$, with$X ^ { \prime } \leq X$if and only if$X ^ { \prime } \subseteq X$

Example 8.8.16. A finite pointed G-set Z has a category of subobjects$\mathbf { S u b } ( Z ) \subset$ $G - \mathcal { F } _ { * } / Z$given by the partially ordered set of pointed G-equivariant subsets $X \subseteq Z$, with$X ^ { \prime } \leq X$if and only if$X ^ { \prime } \subseteq X$

Definition 8.8.17 (Stable building). Let Z be an object in$\mathcal { C }$with rank$\left( Z \right) =$ $k \geq 1$, and fix a subcategory$\mathbf { S u b } ( Z ) \subseteq c o \mathcal { C } / Z$of subobjects. For$n \geq 0$let $D _ { \bullet } ( Z ) _ { n }$be the simplicial set with q-simplices a base point, together with all lattice cubes${ \bar { X } } : [ q ] ^ { \bar { n } } \to \mathcal { C }$such that

(a)$X ( q , \dots , q ) = Z$

(b)$X ( v ) \mapsto Z$is an object in$\mathbf { S u b } ( Z )$, for each$v \in [ q ] ^ { n }$

For$\alpha \colon [ p ]  [ q ]$in ∆ the simplicial operator$\alpha ^ { * } \colon D _ { q } ( Z ) _ { n } \to D _ { p } ( Z ) _ { n }$takes X<sup>¯</sup> to${ \bar { Y } } = { \bar { X } } \circ \alpha ^ { n }$if$\bar { Y } ( i _ { 1 } , \dots , i _ { n } ) = *$whenever some$i _ { t } = 0$and$\bar { Y } ( p , . . . , p ) = Z$4 and to the base point otherwise.

The stable building$\mathbf { D } ( Z )$is the symmetric spectrum with n-th space$D ( Z ) _ { n } =$ $| D _ { \bullet } ( Z ) _ { n } | .$. [[Evident symmetric group action and spectrum structure maps.]]

[[The automorphism group$\operatorname { A u t } ( Z )$of$Z$acts naturally on$\mathbf { D } ( Z ) . ] ]$

Example 8.8.18. For a [[reasonable]] ring R, the q-simplices of$D _ { \bullet } ( R ^ { k } ) _ { n }$are the base point, together with the diagrams${ \bar { X } } \colon [ q ] ^ { n } \to { \mathcal { F } } ( R )$such that

(a)$\bar { X } ( i _ { 1 } , \ldots , i _ { n } ) = 0$whenever some$i _ { t } = 0$

(b)${ \bar { X } } ( q , \dots , q ) = R ^ { k } .$

(c)${ \bar { X } } ( u ) \to { \bar { X } } ( v )$is an inclusion of free R-modules, with free quotient, for each$u \leq v$in$[ q ] ^ { n }$

(d)$\mathrm { c o l i m } _ { u < v } \bar { X } ( u ) \mathrel { \mathop { \longleftrightarrow } } \bar { X } ( v )$is injective with free quotient, for each$v \in [ q ] ^ { n }$

Example 8.8.19. The q-simplices of$D _ { \bullet } ( k _ { + } ) _ { n }$are the base point, together with the diagrams$\bar { X } \colon [ q ] ^ { n } \to \mathcal { F } _ { * }$such that

(a)$\bar { X } ( i _ { 1 } , \ldots , i _ { n } ) = 0 _ { + }$whenever some$i _ { t } = 0$

(b)$\bar { X } ( q , \ldots , q ) = k _ { + }$

(c)${ \bar { X } } ( u ) \to { \bar { X } } ( v )$is an inclusion of pointed sets for each$u \leq v$in$[ q ] ^ { n }$

(d) colim$\mathfrak { 1 } _ { u < v } \bar { X } ( u ) \longmapsto \bar { X } ( v )$is injective for each$v \in [ q ] ^ { n }$

[[Also G-sets?]]

Proposition 8.8.20. There is a levelwise equivalence

$$
\bar {F} _ {k} \mathbf {K} (\mathcal {C}) \simeq \bigvee_ {Z} E \operatorname{Aut} (Z) _ {+} \wedge_ {\operatorname{Aut} (Z)} \mathbf {D} (Z)
$$

of symmetric spectra, where the wedge sum runs over representatives for the isomorphism classes of objects of rank k in$\mathcal { C }$, and$\operatorname { A u t } ( Z )$is the automorphism group of Z.

Proof. Step 1: Let$\mathcal { E } _ { q } \subset \bar { F } _ { k } i S _ { q } ^ { ( n ) } \mathcal { C }$be the full subgroupoid generated by the base point object, together with the$X \colon \mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$such that each quotient map

$$
X (u \leq w) \twoheadrightarrow X (v \leq w)
$$

that is an isomorphism is actually an identity morphism, for all$u \leq v \leq w$in $[ q ] ^ { n }$. Each object in$\bar { F } _ { k } i S _ { q } ^ { ( n ) } \mathcal { C }$is isomorphic to an object in the subgroupoid, so the inclusion is an equivalence of categories. [[For each fixed$w .$, choose the $X ( u \leq w )$appropriately for increasing u.]]

The simplicial operators respect the subgroupoids, hence these assemble to a simplicial pointed groupoid$\mathcal { E } _ { \bullet } ^ { o } .$, and the inclusion$\mathcal { E } _ { \bullet } \subset \bar { F } _ { k } i S _ { \bullet } ^ { ( n ) } \mathcal { C }$is a homotopy equivalence by the realization lemma.

Step 2: Let$\bar { \mathcal { E } } _ { q }$be the pointed groupoid with objects a base point, together with the lattice cubes${ \bar { X } } : { \bar { [ q ] } } ^ { n } \to { \mathcal { C } }$with top rank$k .$There is a pointed functor $\mathcal { E } _ { q } \to \bar { \mathcal { E } } _ { q }$taking$X \colon \mathrm { A r } [ q ] ^ { \dot { n } } \stackrel { \cdot } {  } \mathcal { C }$to its restriction${ \bar { X } } \colon [ q ] ^ { n } \to \mathcal { C }$. This functor is full, faithful and (essentially) surjective on objects, hence an equivalence of categories. [[Since choices of quotients exist, and are unique up to isomorphism.]] We claim that the$\bar { \mathcal { E } } _ { q }$assemble to a simplicial pointed groupoid$\bar { \mathcal { E } } _ { \bullet } ^ { \phantom { \dagger } } .$, such that the functors above combine to a simplicial functor$\mathcal { E } _ { \bullet } ^ { \circ }  \bar { \mathcal { E } } _ { \bullet } ^ { \circ }$, which is then a homotopy equivalence by the realization lemma.

Consider a morphism α:$[ p ]  [ q ]$in$\Delta .$. We must define a functor$\alpha ^ { * } \colon \bar { \mathcal { E } } _ { q }$ $\bar { \mathcal { E } } _ { p }$so that the square

![](images/page_58_image_2.jpg)

commutes. We let$\alpha ( 0 ) = a$and$\alpha ( p ) = b ,$so$\alpha ^ { n } \colon [ p ] ^ { n } \to [ q ] ^ { n }$takes$( 0 , \ldots , 0 )$to $( a , \ldots , a )$and$( p , \ldots , p )$to$( b , \ldots , b )$

Let X :$\mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$in$\mathcal { E } _ { q } ^ { \mathcal { ( o } }$be any object other than the base point, with restriction${ \bar { X } } \colon [ q ] ^ { n } \to \mathcal { C }$in$\bar { \mathcal { E } } _ { q } .$. The image$\alpha ^ { * } ( X )$in$\mathcal { E } _ { p } ^ { \mathrm { { ~ \scriptsize ~ \mathcal ~ } } }$equals

$$
Y = X \circ \operatorname{Ar} (\alpha) ^ {n} \colon \operatorname{Ar} [ p ] ^ {n} \to \mathscr {C},
$$

unless the resulting top module

$$
Y (0 \leq p, \dots , 0 \leq p) = X (a \leq b, \dots , a \leq b)
$$

has rank$< k .$, in which case$\alpha ^ { * } ( X )$is the base point object. There is a cofiber sequence

$$
\underset {w} {\operatorname{colim}} \bar {X} (w) \mapsto \bar {X} (b, \dots , b) \twoheadrightarrow X (a \leq b, \dots , a \leq b),
$$

where w ranges over the$( j _ { 1 } , \ldots , j _ { n } )$in$[ q ] ^ { n }$where each$j _ { t } \in \{ a , b \}$, but w$\neq$ $( b , \ldots , b )$. [[Better: index w by proper subsets of$\{ 1 , \ldots , n \} . ] ]$In view of condition (b) in the definition of a rank function, the first case happens if and only if each$\bar { X } ( w )$has rank 0 and${ \bar { X } } ( b , \ldots , b )$has rank k. The restriction in$\bar { \mathcal { E } } _ { p }$of $\alpha ^ { * } ( X )$is therefore given by${ \bar { Y } } \colon [ p ] ^ { n } \to { \mathcal { C } }$taking$\left( i _ { 1 } , \ldots , i _ { n } \right)$to

$$
X (a \leq \alpha (i _ {1}), \dots , a \leq \alpha (i _ {n})),
$$

if each$\bar { X } ( w )$has rank 0 and${ \bar { X } } ( b , \ldots , b )$has rank k, and to the base point object otherwise.

We now define the functor$\alpha ^ { * } \colon \bar { \mathcal { E } } _ { q } \to \bar { \mathcal { E } } _ { p }$by mapping a lattice cube${ \bar { X } } \colon [ q ] ^ { n } \to$ $\mathcal { C }$to$\bar { X } \circ \alpha ^ { n } \colon [ p ] ^ { n } \to \mathcal { C }$taking$( i _ { 1 } , \ldots , i _ { n } )$to

$$
\bar {X} (\alpha (i _ {1}), \dots , \alpha (i _ {n})),
$$

if each$\bar { X } ( w )$has rank 0 and${ \bar { X } } ( b , \ldots , b )$has rank k, and to the base point object otherwise. The behavior on (iso-)morphisms is obvious.

To show that this definition makes the square above commute, we must check that for each$X \colon \mathrm { A r } [ q ] ^ { n } \to \mathcal { C }$in$\mathcal { E } _ { q }$with each$\bar { X } ( w )$of rank 0 and$\bar { X } ( b , \ldots , b )$of rank$k ,$, the lattice cubes$[ p ] ^ { n }  \mathcal { C }$taking$( i _ { 1 } , \ldots , i _ { n } )$to$X ( a \leq \alpha ( i _ { 1 } ) , \ldots , a \leq$ $\alpha ( i _ { n } ) )$and to$\bar { X } ( \alpha ( i _ { 1 } ) , \ldots , \overset { \cdot } { \alpha } ( i _ { n } ) )$are equal. There is a cofiber sequence

$$
\operatorname * {c o l i m} _ {v} \bar {X} (v) \mapsto \bar {X} (\alpha (i _ {1}), \dots , \alpha (i _ {n})) \twoheadrightarrow X (a \leq \alpha (i _ {1}), \dots , a \leq \alpha (i _ {n})),
$$

where v ranges over the$( j _ { 1 } , \ldots , j _ { n } )$$[ q ] ^ { n }$where each$j _ { t } \in \{ a , \alpha ( i _ { t } ) \}$, but $v \neq ( \alpha ( i _ { 1 } ) , \ldots , \alpha ( i _ { n } ) )$. [[Better: index v by proper subsets of$\{ 1 , \ldots , n \} . ] ]$For each v there is a w as above with$v \leq w .$, so each$\bar { X } ( v )$has rank 0 and the colimit is a zero object. Hence the quotient map is an isomorphism by condition (c) in the definition of a rank function, and therefore is an identity map by the definition of$\mathcal { E } _ { \bullet }$

It is now easy to check that$( \beta \alpha ) ^ { * } = \alpha ^ { * } \beta ^ { * }$for any other morphism$\beta \colon [ q ]$ [r] in$\Delta .$so$\mathcal { E } _ { \bullet } ^ { o } \to \bar { \mathcal { E } } _ { \bullet } ^ { o }$is a well-defined simplicial functor.

Step 3: Each lattice cube${ \bar { X } } \colon [ q ] ^ { n } \to \mathcal { C }$factors uniquely through$c o \mathcal { C } \subseteq \mathcal { C }$ If$\bar { X } ( q , \ldots , q ) = Z$, then for each$v \in [ q ] ^ { n }$the chosen morphisms$\bar { X } ( v ) \mapsto Z$lift X<sup>¯</sup> through coC$\mathcal { P } / Z \to c o \mathcal { C }$

For each object Z of rank k, let$\mathcal { D } _ { q } ( Z ) \subseteq \bar { \mathcal { E } } _ { q }$be the full subgroupoid generated by the lattice cubes${ \bar { X } } \colon [ q ] ^ { n } \to \mathcal { C }$with top object$\bar { X } ( q , \ldots , q ) = Z ;$such that the preferred lift$[ q ] ^ { n } \to c o \mathcal { C } / Z$factors through Su$\mathbf { \delta } \mathbf { { \mathsf { o } } } ( Z ) \subseteq c o \mathcal { C } / Z$In other words,$\mathcal { D } _ { q } ( Z )$is the pointed groupoid with objects a base point, together with the lattice cubes${ \bar { X } } \colon [ q ] ^ { n } \to \mathcal { C }$such that$\bar { X } ( q , \ldots , q ) = Z$and each$\bar { X } ( v )$is a subobject of Z.

The (iso-)morphisms${ \bar { X } } ^ { \prime } \cong { \bar { X } }$are determined by the automorphism$f \colon Z =$ $\bar { X } ^ { \prime } ( q , \dots , q ) \cong \bar { X } ( q , \dots , q ) = Z$, since then$\bar { X } ^ { \prime } ( v )$is the image of the composite

$$
\bar {X} ^ {\prime} (v) \mapsto Z \xrightarrow {f} Z
$$

for all$v \in [ q ] ^ { n }$. The base point object admits only the identity automorphism. Hence$\mathcal { D } _ { q } ( Z )$is the based translation groupoid for the action of$\operatorname { A u t } ( Z )$on the object set$\mathrm {  ~ \ p j { } ( } \mathcal { D } _ { q } ( Z ) )$. In particular,

$$
\left| \mathscr {D} _ {q} (Z) \right| \cong E \operatorname{Aut} (Z) _ {+} \wedge_ {\operatorname{Aut} (Z)} \operatorname{obj} \left(\mathscr {D} _ {q} (Z)\right).
$$

Letting$q \geq 0$vary,$\mathcal { D } _ { \bullet } ( Z ) \subseteq \bar { \mathcal { E } } _ { \bullet }$is a simplicial full subgroupoid. To see that $\alpha ^ { * } \colon \bar { \mathcal { E } } _ { q } \to \bar { \mathcal { E } } _ { p } ^ { - }$takes$\mathcal { D } _ { q } ( Z )$to$\mathcal { D } _ { p } ( Z )$, consider a lattice cube${ \bar { X } } \colon [ q ] ^ { n } \to \mathbf { S u b } ( Z )$ with top object$Z ,$and let$b = { \overset { \cdot } { \alpha } } ( p )$. If the top object${ \bar { X } } ( b , \ldots , b )$of$\bar { X } \circ \alpha ^ { n }$has rank$< k .$, then$\alpha ^ { * } ( { \bar { X } } )$is the base point object. Otherwise,

$$
\bar {X} (b, \dots , b) \mapsto X (q, \dots , q) = Z
$$

is an isomorphism by condition (c) in the definition of a rank function, hence it equals the identity since$\mathbf { S u b } ( Z )$is skeletal and contains$i d _ { Z } \colon Z \ \mapsto \ Z .$ Thus$\alpha ^ { * } ( { \bar { X } } )$is an object in$\mathcal { D } _ { p } ( Z )$. It follows that$\mathcal { D } _ { \bullet } ( Z )$is the simplicia based translation groupoid for the action of$\operatorname { A u t } ( Z )$on the simplicial object set $\operatorname { o b j } ( \mathcal { D } _ { \bullet } ( Z ) ) = D _ { \bullet } ( Z ) _ { n }$. Hence

$$
\left| \mathscr {D} _ {\bullet} (Z) \right| \cong E \operatorname{Aut} (Z) _ {+} \wedge_ {\operatorname{Aut} (Z)} D (Z) _ {n}.
$$

Letting$Z$range over the isomorphism classes of objects of rank k in$\mathcal { C }$, the full inclusion

$$
\bigvee_ {Z} \mathcal {D} _ {\bullet} (Z) \xrightarrow {\simeq} \bar {\mathcal {E}} _ {\bullet}
$$

is a degreewise equivalence of pointed groupoids, since each lattice cube${ \bar { X } } \colon [ q ] ^ { n } \to$ $\mathcal { C }$in$\mathcal { E } _ { q } ^ { \mathrm { ~ ~ } }$is isomorphic to a lattice cube in$\mathcal { D } _ { q } ( Z )$for a unique$Z .$. By the realization lemma, we get a homotopy equivalence of simplicial pointed groupoids.

Hence there is a chain of homotopy equivalences

$$
\begin{array}{c} \bar {F} _ {k} \mathbf {K} (\mathcal {C}) _ {n} = | \bar {F} _ {k} i S _ {\bullet} ^ {(n)} \mathcal {C} | \xleftarrow {\simeq} | \mathcal {E} _ {\bullet} | \xrightarrow {\simeq} | \bar {\mathcal {E}} _ {\bullet} | \\ \xleftarrow {\simeq} \bigvee_ {Z} | \mathcal {D} _ {\bullet} (Z) | \cong \bigvee_ {Z} E   \mathrm{Aut} (Z) _ {+} \wedge_ {\mathrm{Aut} (Z)} D (Z) _ {n}. \end{array}
$$

These are compatible with the evident$\Sigma _ { n }$-actions and the spectrum structure maps, leding to the asserted levelwise equivalence.□

Corollary 8.8.21. There is a levelwise equivalence

$$
\bar {F} _ {k} \mathbf {K} (\mathcal {F} (R)) \simeq E G L _ {k} (R) _ {+} \wedge_ {G L _ {k} (R)} \mathbf {D} (R ^ {k})
$$

of symmetric spectra, for each$k \geq 1$

## 8.9 Algebraic K-theory of finite sets

[[Using spectrum level rank filtration [57].]]

Proposition 8.9.1.$D ( k _ { + } ) _ { n } \cong S ^ { k n }$for all$k \geq 1 , n \geq 1$

Proof. Consider first the case$k = 1$and$n = 1 .$, recalling Exercise 6.3.12. A q-simplex in$D _ { \bullet } ( 1 _ { + } ) _ { 1 }$is a diagram$\bar { X } \colon [ q ]  \mathbf { S u b } ( 1 _ { + } )$, taking the values$0 _ { + }$or $1 _ { + }$at each vertex, such that$\bar { X } ( j - 1 ) \subseteq \bar { X } ( j )$for each$j .$. If$\bar { X } ( 0 ) = 1 _ { + } \neq 0 _ { + }$or $\bar { X } ( q ) = 0 _ { + } \not = 1 _ { + }$, we identify X<sup>¯</sup> with the base point. For each such chain

$$
X _ {0} \subseteq X _ {1} \subseteq \dots \subseteq X _ {q}
$$

of pointed subsets of$1 _ { + }$there is a unique$i ,$with$0 \leq i \leq q + 1$, such that $X _ { j } = 1 _ { + }$if and only if$i \le j$. The end cases$i = 0$and$i = q + 1$are then identified with the base point, since they correspond to the cases$\bar { X } ( 0 ) = 1 _ { + }$ and$\bar { X } ( q ) = 0 _ { + }$, respectively. Each such chain also corresponds to a morphism $\zeta \colon [ q ]  [ 1 ]$in$\Delta .$, or a q-simplex in$\Delta _ { \bullet } ^ { 1 }$, via the formula$X _ { j } = \zeta ( j ) _ { + }$. The case $\bar { X } ( 0 ) = 1 _ { + }$then corresponds to the constant morphism$\zeta$to 1, while the case $\bar { X } ( q ) = 0 _ { + }$corresponds to the constant morphism$\zeta$to 0. Thus the$\zeta$in the simplicial subset$\partial \Delta _ { \bullet } ^ { 1 } \subset \Delta _ { \bullet } ^ { 1 }$are collapsed to the base point. There is therefore a simplicial isomorphism

$$
D _ {\bullet} (1 _ {+}) _ {1} \cong \Delta_ {\bullet} ^ {1} / \partial \Delta_ {\bullet} ^ {1} = S _ {\bullet} ^ {1}.
$$

Next consider the case$k = 1$and$n \geq 1$. A q-simplex in$D _ { \bullet } ( 1 _ { + } ) _ { n }$is a diagram ${ \bar { X } } \colon [ q ] ^ { n } \to \mathbf { S u b } ( 1 _ { + } )$, still taking the values$0 _ { + }$or$1 _ { + }$at each vertex, subject to the lattice conditions. These ensure that there exists a unique$u = ( i _ { 1 } , \ldots , i _ { n } )$ with$0 \leq i _ { t } \leq q + 1$for each$t ,$such that$\bar { X } ( v ) = 1 _ { + }$if and only if$u \leq v .$. To see this, consider two vertices$v , v ^ { \prime }$in$[ q ] ^ { n }$with$\bar { X } ( v ) = \bar { X } ( v ^ { \prime } ) = 1 _ { + }$, let$u \in [ q ] ^ { n }$be maximal with$u \leq v , u \leq v ^ { \prime }$, and let$v \in [ q ] ^ { n }$be minimal with$v \leq w , v ^ { \prime } \leq w$ Clearly then$\bar { X } ( w ) = 1 _ { + }$. There is then a lattice square

![](images/page_60_image_14.jpg)

which means that$\bar { X } ( u )$cannot be$0 _ { + }$, since$1 _ { + } \cup _ { 0 _ { + } } 1 _ { + } \cong 2 _ { + }$does not map by a cofibration to$1 _ { + }$. Hence$\bar { X } ( u ) = 1 _ { + }$

Writing$u = ( i _ { 1 } , \ldots , i _ { n } )$, each$i _ { t }$corresponds to a q-simplex$\zeta _ { t } \colon [ q ]  [ 1 ]$in $\Delta _ { \bullet } ^ { 1 } , \mathrm { g i v e n }$by$\zeta _ { t } ( j ) = 1$if and only i${ \mathrm { : } } j \geq i _ { t }$. The n-tuple$\left( \zeta _ { 1 } , \ldots , \zeta _ { n } \right)$corresponds to a q-simplex in$\Delta _ { \bullet } ^ { 1 } \times \cdots \times \Delta _ { \bullet } ^ { 1 }$. However, if$i _ { t } = 0$or$i _ { t } = q + 1$for some$t ,$then $\zeta _ { t }$is constant at 0 or 1, and the q-simplex is identified with the base point, due to the boundary conditions. This means that there is a simplicial isomorphism

$$
D _ {\bullet} (1 _ {+}) _ {n} \cong S _ {\bullet} ^ {1} \wedge \dots \wedge S _ {\bullet} ^ {1} = S _ {\bullet} ^ {n}.
$$

In the general case,$k \geq 1$and$n \geq 1$, a q-simplex in$D _ { \bullet } ( k _ { + } ) _ { n }$is a diagram ${ \bar { X } } \colon [ q ] ^ { n } \to \mathbf { \bar { S } } \mathbf { u b } ( k _ { + } )$, taking values that are pointed subsets of$k _ { + }$at each vertex, subject to the lattice conditions. These conditions are independent for each element s in$k _ { + }$, so X<sup>¯</sup> can be viewed as a k-tuple of diagrams${ \bar { X } } ^ { 1 } , \dotsc , { \bar { X } } ^ { k } \colon [ q ] ^ { n }$ $\mathbf { S u b } ( 1 _ { + } )$, where$\bar { X } ^ { s } ( v ) = 1 _ { + }$if and only if$s \in \bar { X } ( v )$. We have$\bar { X } ( v ) = 0 _ { + }$if and only if each$\bar { X } ^ { s } ( v ) = 0 _ { + }$, and$\bar { X } ( v ) = k _ { + }$if and only if each$\bar { X } ^ { s } ( v ) = 1 _ { + }$ Hence there is a simplicial isomorphism

$$
D _ {\bullet} (k _ {+}) _ {n} \cong D _ {\bullet} (1 _ {+}) _ {n} \wedge \dots \wedge D _ {\bullet} (1 _ {+}) _ {n},
$$

and$D ( k _ { + } ) _ { n } \cong D ( 1 _ { + } ) _ { n } \wedge \cdots \wedge D ( 1 _ { + } ) _ { n } \cong S ^ { n } \wedge \cdots \wedge S ^ { n } \cong S ^ { k n } .$

Corollary 8.9.2.$\mathbf { D } ( 1 _ { + } ) \cong \mathbb { S }$is the sphere spectrum$\{ n \mapsto S ^ { n } \}$, while$\begin{array} { r } { \mathbf { D } ( k _ { + } ) \simeq } \end{array}$ ∗ is stably trivial for$k \geq 2$

Proof. It is easy to check that$\Sigma _ { n }$permutes the n simplicial circles in$D _ { \bullet } ( 1 _ { + } ) _ { n } \cong$ $S _ { \bullet } ^ { n }$, and that the spectrum structure map is the usual identification$S ^ { n } \wedge S ^ { 1 } \cong$ $S ^ { n + 1 }$

For$k \geq 2 .$, the n-th space$D ( k _ { + } ) _ { n } \cong S ^ { k n }$is at least$( 2 n - 1 )$-connected, hence$\pi _ { i + n } ( D ( k _ { + } ) _ { n } ) = 0$for all$n > i .$, so$\pi _ { i } \mathbf { D } ( k _ { + } ) = 0$in all degrees i. This implies that$\mathbf { D } ( k _ { + } )$is stably trivial.□

We can now prove that the algebraic K-theory of finite sets is the sphere spectrum, which is one form of the Barratt–Priddy–Quillen theorem.

Theorem 8.9.3.

$$
\mathbf {K} (\mathcal {F} _ {*}) \simeq \mathbb {S},
$$

$$
\text {   so   } K _ {i} (\mathcal {F} _ {*}) \cong \pi_ {i} (\mathbb {S}) = \operatorname{colim} _ {m} \pi_ {i + m} (S ^ {m}) \text {   for   all   } i \geq 0.
$$

Proof. By Proposition 8.8.20, there are levelwise equivalences

$$
\bar {F} _ {k} \mathbf {K} (\mathcal {F} _ {*}) \simeq E \Sigma_ {k +} \wedge_ {\Sigma_ {k}} \mathbf {D} (k _ {+})
$$

for$k \geq 1$. For$k = 1$we get levelwise equivalences$F _ { 1 } \mathbf { K } ( \mathcal { F } _ { * } ) \simeq \bar { F } _ { 1 } \mathbf { K } ( \mathcal { F } _ { * } ) \simeq$ $\mathbf { D } ( 1 _ { + } ) \cong \mathbb { S }$, while for$k \geq 2$we get stable equivalences$\bar { F } _ { k } \mathbf { K } ( \mathcal { F } _ { * } ) \simeq E \Sigma _ { k + } \wedge _ { \Sigma _ { k } } * \simeq$ $^ * \cdot$. It follows that$F _ { k - 1 } \mathbf { K } ( \mathcal { F } _ { * } ) \longrightarrow F _ { k } \mathbf { K } ( \mathcal { F } _ { * } )$is a stable equivalence for each$k \geq 2 ,$ hence in the colimit$F _ { 1 } \mathbf { K } ( \mathcal { F } _ { * } )  \mathbf { K } ( \mathcal { F } _ { * } )$is a stable equivalence.□

Corollary 8.9.4.$\begin{array} { r } { K ( \mathcal { F } _ { * } ) _ { n } \simeq Q ( S ^ { n } ) = \mathrm { c o l i m } _ { m } \Omega ^ { m } S ^ { n + m } } \end{array}$for all$n \geq 0$. In particular, for n = 0 the loop space completion map$\iota \colon | i \mathcal { F } _ { * } |  K ( \mathcal { F } _ { * } )$is homotopy equivalent to$\begin{array} { r } { \operatorname { I I } _ { n > 0 } B \Sigma _ { n } \to Q ( S ^ { 0 } ) } \end{array}$

[[The rank$\leq 1$inclusion$S ^ { 0 } \simeq B \Sigma _ { 1 + } \subset \mathrm { ~ \sqcup ~ } _ { n > 0 } B \Sigma _ { n } \to K ( \mathcal { F } _ { * } ) _ { 0 }$is right adjoint to the spectrum map$\mathbb { S } \to \mathbf { K } ( \mathcal { F } _ { * } )$\` that is an equivalence.]]

[[The map$\begin{array} { r } { \operatorname { I I } _ { n > 0 } B \Sigma _ { n } \to Q ( S ^ { 0 } ) } \end{array}$has interesting geometric constructions, in-\`volving operads, and induces a homology isomorphism after inverting the generator of$H _ { 0 } ( B \Sigma _ { 1 } )$in$\begin{array} { r } { H _ { * } ( \prod _ { n \geq 0 } B \Sigma _ { n } ) } \end{array}$. Hence there is an equivalence$\mathbb { Z } \times B \Sigma _ { \infty } ^ { + } \simeq$ $Q ( S ^ { 0 } ) . ] ]$

Corollary 8.9.5 (May–Milgram filtration). For n$\geq 1$there is a filtration

$$
* \simeq F _ {0, n} \mapsto \dots \mapsto F _ {k - 1, n} \mapsto F _ {k, n} \mapsto \dots \mapsto K (\mathscr {F} _ {*}) _ {n} \simeq Q (S ^ {n})
$$

with filtration quotients

$$
F _ {k, n} / F _ {k - 1, n} \simeq E \Sigma_ {k +} \wedge_ {\Sigma_ {k}} S ^ {n k}
$$

for$k \geq 1$, where$\Sigma _ { k }$permutes the copies of$S ^ { n }$in$S ^ { n k } \cong S ^ { n } \wedge \cdot \cdot \cdot \wedge S ^ { n }$

Proof. Let$F _ { k , n } = F _ { k } K ( \mathcal { F } _ { * } ) _ { n }$

Definition 8.9.6. For$\textit { G a }$finite group, let$G - \mathcal { F } _ { * }$be the category of finite pointed G-sets and G-equivariant base-point preserving functions. Let$c o G { - } \mathcal { F } ,$∗ be the subcategory of injective functions, and let rank$\left( X _ { + } \right) = k$when$\boldsymbol { X } \cong$ $\textstyle \prod _ { s = 1 } ^ { k } G / H _ { i }$is the disjoint union of k orbits.

The following is a form of the Segal–tom Dieck splitting. [[reference]]

Theorem 8.9.7.

$$
\mathbf {K} (G - \mathcal {F} _ {*}) \simeq \bigvee_ {(H)} \mathbb {S} [ B W _ {G} (H) ],
$$

where the wedge sum runs over the conjugacy classes of subgroups H of G, and $W _ { G } ( H ) = N _ { G } ( H ) / H$is the Weyl group of H in$G ,$, where$N _ { G } ( H ) = \{ n \in G \mid$ $n H = H n \}$is the normalizer of H in$G .$

Proof. The finite pointed G-sets of rank 1 are of the form$G / H _ { + }$, as H ranges over all subgroups of G. There is an isomorphism$G / H \cong G / K$taking eH to cK if and only if$H = c K c ^ { - 1 } { , }$, i.e., if H and K are conjugate subgroups. The automorphism group of$Z = G / H _ { + }$consists of the G-equivariant functions$G / H \to G / H$taking eH to nH, where$n \in G$must normalize H and is only defined modulo H, so$\operatorname { A u t } ( Z ) \cong W _ { G } ( H )$. Hence by Lemma 8.8.6 and Proposition 8.8.20 for$k = 1$, there is an equivalence

$$
F _ {1} \mathbf {K} (G - \mathcal {F} _ {*}) \simeq \bigvee_ {(H)} E W _ {G} (H) _ {+} \wedge_ {W _ {G} (H)} \mathbf {D} (G / H _ {+}).
$$

We claim that there is an isomorphism${ \mathbf { D } } ( G / H _ { + } ) \cong  { \mathbf { D } } ( 1 _ { + } ) \cong \mathbb { S }$, with the trivial$W _ { G } ( H )$-action. For any diagram$\bar { X } \colon [ q ] ^ { n } \to \mathbf { S u b } ( G / H _ { + } )$takes the values ∗ and$G / H _ { + }$<sub>+</sub> only, of rank 0 and 1, respectively. Hence the isomorphism $\mathbf { S u b } ( G / H _ { + } ) \cong \mathbf { S u b } ( 1 _ { + } )$taking ∗ and$G / H _ { + }$to$0 _ { + }$and$1 _ { + }$, respectively, induces the claimed isomorphism. Thus

$$
F _ {1} \mathbf {K} (G - \mathcal {F} _ {*}) \simeq \bigvee_ {(H)} \mathbb {S} [ B W _ {G} (H) ].
$$

More generally, we claim that there is an isomorphism$\mathbf { D } ( Z _ { + } ) \cong \mathbf { D } ( k _ { + } ) \simeq *$ for any$\begin{array} { r } { Z \cong \coprod _ { s = 1 } ^ { k } G / H _ { s } } \end{array}$. Again, any subobject of$Z _ { + }$has the form$X _ { + }$, where $X$\`is the coproduct of a subset of the s with$1 \ \leq \ s \ \leq \ k .$, and the isomorphism Sub${ \bf \nabla } ( Z _ { + } ) \cong { \bf S u b } ( k _ { + } )$taking$X _ { + }$with$\begin{array} { r } { X = \coprod _ { s \in U } G / H _ { \ S } } \end{array}$<sub>s</sub> to$U _ { + }$with $U \subseteq \{ 1 , \ldots , k \}$\`induces the claimed isomorphism. Hence by Proposition 8.8.20 for$k \geq 2 .$, there is are stable equivalences

$$
\bar {F} _ {k} \mathbf {K} (G - \mathcal {F} _ {*}) \simeq \bigvee_ {Z} E \operatorname{Aut} (Z) _ {+} \wedge_ {\operatorname{Aut} (Z)} \mathbf {D} (k _ {+}) \simeq *,
$$

so that all of the maps

$$
\begin{array}{c} F _ {1} \mathbf {K} (G - \mathcal {F} _ {*}) \xrightarrow {\simeq} \ldots \xrightarrow {\simeq} F _ {k - 1} \mathbf {K} (G - \mathcal {F} _ {*}) \xrightarrow {\simeq} F _ {k - 1} \mathbf {K} (G - \mathcal {F} _ {*}) \xrightarrow {\simeq} \ldots \\ \xrightarrow {\simeq} \mathbf {K} (G - \mathcal {F} _ {*}) \end{array}
$$

are stable equivalences.

[[Note how$\begin{array} { r } { K _ { 0 } ( G - \mathcal { F } _ { * } ) \cong { \coprod \mathop { } } _ { ( H ) } \mathbb { Z } \cong A ( G ) } \end{array}$is the free abelian group generated by the$G / H , { \mathrm { i . e . } } ,$\` the Burnside ring.]]

[[The rank$\leq 1$inclusion$( \coprod _ { ( H ) } \bar { B } W _ { G } ( H ) ) _ { + } \subset | i ( G - \mathscr { F } _ { * } ) | \to K ( G - \mathscr { F } _ { * } )$is \`right adjoint to the spectrum map$\vee _ { ( H ) } \mathbb { S } [ B W _ { G } ( H ) ]  \mathbf { K } ( G - \mathscr { F } _ { * } )$that is an equivalence.]]

[[One can also identify$\mathbf { K } ( G - { \mathcal { F } } _ { * } )$with the$G .$-fixed point spectrum$( \mathbb { S } _ { G } ) ^ { G }$of the G-equivariant sphere spectrum$\mathbb { S } _ { G }$. The loop space completion map takes $| i ( G { - } \mathcal { F } _ { * } ) | \simeq \coprod _ { | Z | } B \operatorname { A u t } ( Z )$to$Q _ { G } ( \bar { S } ^ { 0 } ) ^ { G } = { \mathrm { c o l i m } } _ { V } ( \Omega ^ { V } S ^ { V } ) ^ { \hat { G } }$where$V$ranges over${ ^ { 6 } \mathrm { a l l } } ^ { 5 5 } \ \mathrm { \it G } .$-representations, and$( \Omega ^ { V } S ^ { V } ) ^ { G }$is the space of based G-equivariant maps$S ^ { V } \to S ^ { \hat { V } } . ] ]$

Definition 8.9.8. Let$\mathcal { F } _ { * } ( G )$be the category of finite free pointed$G \mathrm { . }$-sets,$\mathrm { i . e . } .$ finite G-sets$X _ { + }$where$G$acts freely on$X$and fixes the base point$^ { * , }$and$G \mathrm { - }$ equivariant base-point preserving functions. Let$c o { \mathcal { F } } _ { * } ( G )$be the subcategory of injective functions, and let ran$\mathfrak { r } ( X _ { + } ) = k$when$\textstyle X \cong \operatorname { L I } _ { s = 1 } ^ { k } G$. Then$\mathcal { F } _ { * } ( G )$ is a subcategory with cofibrations of$G - { \mathcal { F } } _ { * }$∗

The following variant is known as the Barratt–Priddy–Quillen–Segal theorem.

Theorem 8.9.9.$\mathbf { K } ( { \mathcal { F } } _ { * } ( G ) ) \simeq \mathbb { S } [ B G ]$

Proof. This is much like the previous proof, but only the case$H = e$with $W _ { G } ( e ) = G$appears.□

[[Exercise: Use the additivity theorem to prove that

$$
\mathbf {K} (G - \mathcal {F} _ {*}) \simeq \bigvee_ {(H)} \mathbf {K} (\mathcal {F} _ {*} (G, H)) \simeq \bigvee_ {(H)} \mathbf {K} (\mathcal {F} _ {*} (W _ {G} (H))) \simeq \bigvee_ {(H)} \mathbb {S} [ B W _ {G} (H) ]
$$

where$\mathcal { F } _ { * } ( G , H ) \subset G - \mathcal { F } _ { * }$is the Waldhausen subcategory of finite based G-sets with stabilizers conjugate to$H .$. Hint: Do the case$G = C _ { p }$first. In general, refine the partially ordered set of conjugacy classes to a linear ordering, and use an induction.]]

[[The multiplicative structure of$\mathbf { K } ( G - { \mathcal { F } } _ { * } )$and$\mathbf { K } ( { \mathcal { F } } _ { * } ( G ) )$is not fully understood. These are commutative$\mathrm { \mathbb { S } } \mathrm { - a l g e b r a s } = E _ { \infty }$ring spectra.]]

Chapter 9

# Abelian and exact categories

## 9.1 Additive categories

[[[40, I.8, VIII.2].]]

[[Define Ab-category. Zero map.]] [[Initial object = terminal object = zero object.]]

Lemma 9.1.1. Let X, Y be objects in an Ab-category A .$I f p \colon X \times Y \to X$ and$q \colon X \times Y \to Y$make$X \times Y$a product of X and Y in A, then

(a)$i = ( i d _ { X } , 0 ) \colon X \to X \times Y$and$j = ( 0 , i d _ { Y } ) \colon Y  X \times Y$make$X \times Y$a coproduct of X and Y.

(b) the diagram

$$
X \xrightarrow [ p ]{i} X \times Y \xrightarrow [ j ]{q} Y
$$

with$q i = 0 , p j = 0$and$i p + j q = i d$makes$X \times Y$a biproduct of X and Y.

[[Additive category is an Ab-category with finite products (= finite coproducts, including a zero object).]]

## 9.2 Abelian categories

[[[40, VIII.3], [72, 1.2, 1.6].]]

Definition 9.2.1. A kernel of a morphism$f \colon X \to Y$in an additive category $\mathcal { A }$is an equalizer k :$K  X$of f and the zero map$0 \colon X \to Y$

$$
K \xrightarrow {k} X \xrightarrow [ 0 ]{f} Y
$$

Hence$f k = 0$and any map$t \colon T \to X$with$f t = 0$factors uniquely as$t = k u$ with u :$T  K$. In other words,

$$
0 \to \mathscr {A} (T, K) \xrightarrow {k _ {*}} \mathscr {A} (T, X) \xrightarrow {f _ {*}} \mathscr {A} (T, Y)
$$

is an exact sequence of abelian groups, for any$T .$

A morphism k :$K  X$in$\mathcal { A }$is called a monomorphism if$k u = 0$only if $u = 0$, for u :$T  K$. In other words,

$$
0 \to \mathscr {A} (T, K) \xrightarrow {k _ {*}} \mathscr {A} (T, X)
$$

is an exact sequence of abelian groups, for any T. A kernel is clearly a monomorphism.

Definition 9.2.2. A cokernel of a morphism$f \colon X \to Y$in an additive category $\mathcal { A }$is a coequalizer$c \colon Y \to C$of$f$and the zero map$0 \colon X \to Y$

$$
X \xrightarrow [ 0 ]{\stackrel {f} {\longrightarrow}} Y \xrightarrow [ ]{c} C
$$

Hence$c f = 0$and any map$t \colon Y \to T$with$t f = 0$factors uniquely as$t = u c$ with$u \colon C \to T$. In other words,

$$
0 \to \mathcal {A} (C, T) \xrightarrow {c ^ {*}} \mathcal {A} (Y, T) \xrightarrow {f ^ {*}} \mathcal {A} (X, T)
$$

is an exact sequence of abelian groups, for any$T .$

A morphism$c \colon Y  C$in$\mathcal { A }$is called an epimorphism if$u c = 0$only if $u = 0$, for$u \colon C \to T$. In other words,

$$
0 \to \mathcal {A} (C, T) \xrightarrow {c ^ {*}} \mathcal {A} (Y, T)
$$

is an exact sequence of abelian groups, for any T. A cokernel is clearly an epimorphism.

[[Kernels and cokernels are well-defined up to unique isomorphism, like all other limits and colimits.]]

[[Some authors say monic or epi instead of monomorphism and epimorphism, respectively.]]

Definition 9.2.3 (Abelian category). An abelian category is an additive category$\mathcal { A }$such that

(a) Every morphism in A has a kernel and a cokernel.

(b) Every monomorphism in$\mathcal { A }$is a kernel.

(c) Every epimorphism in$\mathcal { A }$is a cokernel.

[[It follows that every monomorphism m :$X \longmapsto Y$is the kernel of its cokernel $c \colon Y \to C$, and that every epimorphism$e \colon X \to Y$is the cokernel of its kernel $k \colon K \longmapsto X . ] ]$

[[Image of$f \colon X \to Y$is the kernel of its cokernel$c \colon Y \to C$. It is isomorphic to the cokernel of its kernel$k \colon K \mapsto X$, i.e., the coimage:

$$
X \twoheadrightarrow \operatorname{coim} (f) \cong \operatorname{im} (f) \mapsto Y
$$

We can talk about exact sequences in an abelian category$\mathcal { A } .$, hence do homological algebra.

Example 9.2.4. Let R be a ring. The category R−Mod of left R-modules is an abelian category. In particular, Ab is abelian.

Example 9.2.5. The category${ \mathcal { M } } ( R )$of finitely generated R-modules is an additive category, which is abelian if R is Noetherian. [[More generally, the category of coherent R-modules is abelian, also for non-noetherian$R . ] ]$

The category${ \mathcal { P } } ( R )$of finitely generated projective R-modules is additive, but usually not abelian.

Example 9.2.6. The category of finite abelian groups is abelian. So is the subcategory if finite abelian p-groups, for each prime$p ,$and the subcategory of elementary abelian p-groups.

Definition 9.2.7. A functor$F \colon \mathcal { A }  \mathcal { B }$between Ab-categories is additive if $F \colon \mathcal { A } ( X , Y ) \to \mathcal { B } ( F ( X ) , F ( Y ) )$) is a group homomorphism for all objects X, Y in A.

An additive functor$F \colon { \mathcal { A } }  { \mathcal { B } }$between abelian categories is exact if it preserves exact sequences, i.e., if$F ( X ) \to F ( Y ) \to F ( Z )$is exact in$\mathcal { B }$whenever $X  Y  Z$is exact in$\mathcal { A } .$

Theorem 9.2.8 (Freyd–Mitchell embedding theorem). Let A be a small abelian category. There exists a ring R and an exact, fully faithful functor from $\mathcal { A }$to R−Mod, embedding$\mathcal { A }$as a full subcategory.

## 9.3 Exact categories

[[[55, §2].]]

[[We follow Quillen.]]

Definition 9.3.1. Let$\mathcal { A }$be an abelian category, and let$\mathcal { P } \subset \mathcal { A }$be an additive full subcategory. Suppose that$\mathcal { P }$is closed under extensions in$\mathcal { A } .$, in the sense that if

$$
0 \to X \mapsto Y \twoheadrightarrow Z \to 0
$$

is a short exact sequence in${ \mathcal { A } } ,$and X and$Z$are isomorphic to objects in$\mathcal { P }$ the Y is isomorphic to an object in$\mathcal { P }$. Let$\mathcal { E }$be the class of sequences

$$
0 \to X \mapsto Y \twoheadrightarrow Z \to 0
$$

in$\mathcal { P }$that are exact in${ \mathcal { A } } .$The morphisms$X \longmapsto Y$in$\mathcal { P }$that occur at the left in some sequence in$\mathcal { E } ^ { \mathcal { C } }$are called admissible monomorphisms, and the morphisms $Y  Z$in$\mathcal { P }$that occur at the right in some sequence in$\mathcal { E }$are called admissible epimorphisms.

Lemma 9.3.2.$( a )$Any sequence in$\mathcal { P }$isomorphic to a sequence in$\mathcal { E } ^ { \mathcal { C } }$is in E . For any X, Z in$\mathcal { P }$the sequence

$$
0 \to X \stackrel {i} {\longrightarrow} X \oplus Z \stackrel {q} {\longrightarrow} Z \to 0
$$

is in$\mathcal { E } ^ { \mathcal { C } } .$For any sequence

$$
0 \to X \mapsto Y \twoheadrightarrow Z \to 0
$$

in${ \mathcal { E } } , X \longmapsto Y$is a kernel$f o r Y \twoheadrightarrow Z$and$Y  Z$is a cokernel for$X \longmapsto Y$ in the additive category$\mathcal { P }$

(b) The class of admissible epimorphisms is closed under composition and under base change by arbitrary morphisms in$\mathcal { P }$. Dually, the class of admissible monomorphisms is closed under composition and under cobase change by arbitrary morphisms in$\mathcal { P }$

(c) Let$Y  Z$be a morphism with a kernel in$\mathcal { P }$. If there exists a morphism $T  Y$in$\mathcal { P }$such that the composite$T  Z$is an admissible epimorphism, then$Y  Z$is an admissible epimorphism. Dually for admissible monomorphisms.

Definition 9.3.3. An exact category is an additive category$\mathcal { P }$equipped with a family$\mathcal { E } ^ { \mathcal { C } }$of exact sequences, called the short exact sequences of$\mathcal { P } _ { : }$, such that the properties (a), (b) and$( \mathrm { c ) }$of the lemma above hold. An exact functor $F \colon { \mathcal { P } }  { \mathcal { Q } }$between exact categories is an additive functor carrying exact sequences in$\mathcal { P }$into exact sequences in${ \mathcal { Q } } .$

Quillen proves that any (small?) exact category$( \mathcal { P } , \mathcal { E } )$occurs as an additive full subcategory of an abelian category${ \mathcal { A } } .$, with$\mathcal { E } ^ { \mathcal { O } }$equal to the class of sequences in$\mathcal { P }$that are exact in${ \mathcal { A } } ,$as above.

Example 9.3.4. The additive category${ \mathcal P } = { \mathcal P } ( R )$of finitely generated projective R-modules, viewed as a full subcategory of the abelian category$\mathcal { A } =$ R−Mod of all$R ^ { - }$-modules, is an exact category. The class$\mathcal { E }$consists of the short exact sequences of finitely generated projective R-modules.

# Chapter 10 Quillen K-theory

10.1 The Q-construction

[[[55, §2], [68, 1.9].]]

[[Start with Segal subdivision of S<sub>•</sub>-construction.]] [[Additivity theorem [55, §3].]]

10.2 The cofinality theorem

[[[68, 1.5], [61, §2].]]

10.3 The resolution theorem

[[[55, §4], [61, §3].]]

10.4 The devissage theorem

[[[55, §5], [61, §4].]]

10.5 The localization sequence

[[[55, §5], [61, §5].]]

## Bibliography

[1] J. F. Adams, On the non-existence of elements of Hopf invariant one, Ann. of Math. (2) 72 (1960), 20–104.

[2] J. F. Adams and M. F. Atiyah, K-theory and the Hopf invariant, Quart. J. Math. Oxford Ser. (2) 17 (1966), 31–38.

[3] Michael Artin, Alexandre Grothendieck, and Jean-Louis Verdier, S´eminaire de G´eom´etrie Alg´ebrique du Bois Marie – 1963-64 – Th´eorie des topos et cohomologie ´etale des sch´emas – (SGA 4) – vol. 1, 1972, http://www.math.polytechnique.fr/∼laszlo/sga4.html.

[4] M. F. Atiyah and F. Hirzebruch, Riemann-Roch theorems for diferentiable manifolds, Bull. Amer. Math. Soc. 65 (1959), 276–281.

[5] Michael Barratt and Stewart Priddy, On the homology of non-connected monoids and their associated groups, Comment. Math. Helv. 47 (1972), 1–14.

[6] Armand Borel and Jean-Pierre Serre, Le th´eor\`eme de Riemann-Roch, Bull. Soc. Math. France 86 (1958), 97–136. (French)

[7] Armand Borel, Stable real cohomology of arithmetic groups, Ann. Sci. Ecole Norm. Sup.<sup>´</sup> (4) 7 (1974), 235–272 (1975).

[8] A. K. Bousfield and E. M. Friedlander, Homotopy theory of Γ-spaces, spectra, and bisimplicial sets (1978), 80–130.

[9] Lawrence Breen, Tannakian categories (1994), 337–376.

[10] Ruth M. Charney, Homology stability for GLn of a Dedekind domain, Invent. Math. 56 (1980), 1–17.

[11] Frederick R. Cohen, Thomas J. Lada, and J. Peter May, The homology of iterated loop spaces, Lecture Notes in Mathematics, Vol. 533, Springer-Verlag, Berlin, 1976.

[12] Albrecht Dold and Ren´e Thom, Quasifaserungen und unendliche symmetrische Produkte, Ann. of Math. (2) 67 (1958), 239–281. (German)

[13] William G. Dwyer and Eric M. Friedlander, Algebraic and etale K-theory, Trans. Amer. Math. Soc. 292 (1985), 247–280.

[14] W. G. Dwyer and S. A. Mitchell, On the K-theory spectrum of a smooth curve over a finite field, Topology 36 (1997), 899–929.

[15]On the K-theory spectrum of a ring of algebraic integers, K-Theory 14 (1998), 201–263.

[16] Eldon Dyer and R. K. Lashof, Homology of iterated loop spaces, Amer. J. Math. 84 (1962), 35–88.

[17] Samuel Eilenberg and Norman Steenrod, Foundations of algebraic topology, Princeton University Press, Princeton, New Jersey, 1952.

[18] Samuel Eilenberg and J. A. Zilber, Semi-simplicial complexes and singular homology, Ann. of Math. (2) 51 (1950), 499–513.

[19] Steve Ferry and Andrew Ranicki, A survey of Wall’s finiteness obstruction (2001), 63–79.

[20] Rudolf Fritsch and Renzo A. Piccinini, Cellular structures in topology, Cambridge Studies in Advanced Mathematics, vol. 19, Cambridge University Press, Cambridge, 1990.

[21] Thomas Geisser and Lars Hesselholt, Topological cyclic homology of schemes (1999), 41–87.

[22] Paul G. Goerss and John F. Jardine, Simplicial homotopy theory, Progress in Mathematics, vol. 174, Birkh¨auser Verlag, Basel, 1999.

[23] Daniel Grayson, Higher algebraic K-theory. II (after Daniel Quillen) (1976), 217–240. Lecture Notes in Math., Vol. 551.

[24] Alexandre Grothendieck, S´eminaire de G´eom´etrie Alg´ebrique – 1960/61 – Revˆetements ´etales et groupe fondamental – (SGA 1), 1971.

[25] A. E. Hatcher, Higher simple homotopy theory, Ann. of Math. (2) 102 (1975), 101–137.

[26] Allen Hatcher, Algebraic topology, Cambridge University Press, Cambridge, 2002.

[27] Mark Hovey, Brooke Shipley, and Jef Smith, Symmetric spectra, J. Amer. Math. Soc. 13 (2000), 149–208.

[28] Dale Husemoller, Fibre bundles, 2nd ed., Springer-Verlag, New York, 1975, Graduate Texts in Mathematics, No. 20.

[29] Kenkichi Iwasawa, A class number formula for cyclotomic fields, Ann. of Math. (2) 76 (1962), 171–179.

[30] Kiyoshi Igusa, The stability theorem for smooth pseudoisotopies, K-Theory 2 (1988), vi+355.

[31] Kevin Charles Jones, Youngsoo Kim, Andrea H. Mhoon, Rekha Santhanam, Barry J. Walker, and Daniel R. Grayson, The additivity theorem in K-theory, K-Theory 32 (2004), 181–191.

[32] Daniel M. Kan, A combinatorial definition of homotopy groups, Ann. of Math. (2) 67 (1958), 282–312.

[33] , Adjoint functors, Trans. Amer. Math. Soc. 87 (1958), 294–329.

[34] R. C. Kirby and L. C. Siebenmann, On the triangulation of manifolds and the Hauptvermutung, Bull. Amer. Math. Soc. 75 (1969), 742–749.

[35] M. Kre˘ın, A principle of duality for bicompact groups and quadratic block algebras, Doklady Akad. Nauk SSSR (N.S.) 69 (1949), 725–728. (Russian)

[36] Tatsuji Kudo and Shˆorˆo Araki, On H<sub>∗</sub>(Ω<sup>N</sup> (S<sup>n</sup>); Z2), Proc. Japan Acad. 32 (1956), 333–335.

[37] Masato Kurihara, Some remarks on conjectures about cyclotomic fields and K-groups of Z, Compositio Math. 81 (1992), 223–236.

[38] Joachim Lillig, A union theorem for cofibrations, Arch. Math. (Basel) 24 (1973), 410–415.

[39] Ronnie Lee and R. H. Szczarba, On the torsion in$K _ { 4 } ( \mathbf { Z } )$and$K _ { 5 } ( \mathbf { Z } )$, Duke Math. J. 45 (1978), 101–129.

[40] Saunders Mac Lane, Categories for the working mathematician, 2nd ed., Graduate Texts in Mathematics, vol. 5, Springer-Verlag, New York, 1998.

[41] Ib Madsen and R. James Milgram, The classifying spaces for surgery and cobordism of manifolds, Annals of Mathematics Studies, vol. 92, Princeton University Press, Princeton, N.J., 1979.

[42] J. Peter May, Simplicial objects in algebraic topology, Van Nostrand Mathematical Stud ies, No. 11, D. Van Nostrand Co., Inc., Princeton, N.J.-Toronto, Ont.-London, 1967.

[43] J. P. May, A concise course in algebraic topology, Chicago Lectures in Mathematics, University of Chicago Press, Chicago, IL, 1999.

[44] Randy McCarthy, On fundamental theorems of algebraic K-theory, Topology 32 (1993), 325–328.

[45] M. C. McCord, Classifying spaces and infinite symmetric products, Trans. Amer. Math. Soc. 146 (1969), 273–298.

[46] D. McDuf and G. Segal, Homology fibrations and the “group-completion” theorem, Invent. Math. 31 (1975/76), 279–284.

[47] John Milnor, The geometric realization of a semi-simplicial complex, Ann. of Math. (2) 65 (1957), 357–362.

[48], Introduction to algebraic K-theory, Princeton University Press, Princeton, N.J., 1971, Annals of Mathematics Studies, No. 72.

[49] Minoru Nakaoka, Decomposition theorem for homology groups of symmetric groups, Ann. of Math. (2) 71 (1960), 16–42.

[50] , Homology of the infinite symmetric group, Ann. of Math. (2) 73 (1961), 229–257.

[51] J¨urgen Neukirch, Algebraic number theory, Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 322, Springer-Verlag, Berlin, 1999, Translated from the 1992 German original and with a note by Norbert Schappacher; With a foreword by G. Harder.

[52] Daniel G. Quillen, Homotopical algebra, Lecture Notes in Mathematics, No. 43, Springer-Verlag, Berlin, 1967.

[53] Daniel Quillen, On the (co-) homology of commutative rings (1970), 65–87.

[54]On the cohomology and K-theory of the general linear groups over a finite field, Ann. of Math. (2) 96 (1972), 552–586.

[55] , Higher algebraic K-theory. I (1973), 85–147. Lecture Notes in Math., Vol. 341.

[56], Finite generation of the groups K<sub>i</sub> of rings of algebraic integers (1973), 179–198. Lecture Notes in Math., Vol. 341.

[57] John Rognes, A spectrum level rank filtration in algebraic K-theory, Topology 31 (1992), 813–845.

[58] , K4(Z) is the trivial group, Topology 39 (2000), 267–281.

[59] Graeme Segal, Classifying spaces and spectral sequences, Inst. Hautes Etudes Sci. Publ.<sup>´</sup> Math. (1968), 105–112.

[60] , Categories and cohomology theories, Topology 13 (1974), 293–312.

[61] Ross E. Stafeldt, On fundamental theorems of algebraic K-theory, K-Theory 2 (1989), 511–532.

[62] N. E. Steenrod, A convenient category of topological spaces, Michigan Math. J. 14 (1967), 133–152.

[63] , Milgram’s classifying space of a topological group, Topology 7 (1968), 349–368.

[64] T. Tannaka, Uber den Dualit¨atssatz der nichtkommutativen topologisc <sup>¨</sup> hen Gruppen, Tˆohoku math. J. 45 (1938), 1–12. (German)

[65] R. W. Thomason and Thomas Trobaugh, Higher algebraic K-theory of schemes and of derived categories (1990), 247–435.

[66] Vladimir Voevodsky, Motivic cohomology with Z/2-coeficients, Publ. Math. Inst. Hautes Etudes Sci. (2003), 59–104.<sup>´</sup>

[67] Friedhelm Waldhausen, Algebraic K-theory of generalized free products, Ann. of Math. (2) 108 (1978), 135–256.

[68] , Algebraic K-theory of spaces (1985), 318–419.

[69], On the construction of the Kan loop group, Doc. Math. 1 (1996), No. 05, 121–126 (electronic).

[70] Friedhelm Waldhausen, Bjørn Jahren, and John Rognes, Spaces of PL manifolds and categories of simple maps, http://folk.uio.no/rognes/papers/plmf.pdf.

[71] C. T. C. Wall, Finiteness conditions for CW-complexes, Ann. of Math. (2) 81 (1965), 56–69.

[72] Charles A. Weibel, An introduction to homological algebra, Cambridge Studies in Ad vanced Mathematics, vol. 38, Cambridge University Press, Cambridge, 1994.

[73] Michael Weiss and Bruce Williams, Automorphisms of manifolds (2001), 165–220.

[74] N. H. Williams, On Grothendieck universes, Compositio Math. 21 (1969), 1–3.