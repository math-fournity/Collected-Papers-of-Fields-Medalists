# PARTIAL REGULARITY FOR OPTIMAL TRANSPORT MAPS

GUIDO DE PHILIPPIS AND ALESSIO FIGALLI

Abstract. We prove that, for general cost functions on$\mathbb { R } ^ { n }$, or for the cost$d ^ { 2 } / 2$on a Riemannian manifold, optimal transport maps between smooth densities are always smooth outside a closed singular set of measure zero.

## 1. Introduction

A natural and important issue in optimal transport theory is the regularity of optimal transport maps. Indeed, apart from being a typical PDE/analysis question, knowing whether optimal maps are smooth or not is an important step towards a qualitative understanding of them.

It is by now well known that, for the smoothness of optimal maps, conditions on both the cost function and on the geometry of the supports of the measures are needed.

In the special case$c ( x , y ) = | x - y | ^ { 2 } / 2$on$\mathbb { R } ^ { n }$, Cafarelli [3, 4, 5, 6] proved regularity of optimal maps under suitable assumptions on the densities and on the geometry of their support. More precisely, in its simplest form, Cafarelli’s result states as follows:

Theorem 1.1. Let f and g be smooth probability densities, respectively bounded away from zero and infinity on two bounded open sets X and$Y$, and let$T : X  Y$denote the unique optimal transport map from f to g for the quadratic cost$\vert x - y \vert ^ { 2 } / 2$. If Y is convex, then T is smooth inside $X$. On the other hand, if Y is not convex, then there exist smooth densities f and g (both bounded away from zero and infinity on X and${ \cal Y } ,$respectively) for which the map T is not continuous.

A natural question which arises from the previous result is whether one may prove some partial regularity on$T$when the convexity assumption on$Y$is removed. In [16, 18] the authors proved the following result:

Theorem 1.2. Let$f$and g be smooth probability densities, respectively bounded away from zero and infinity on two bounded open sets X and$Y _ { i }$, and let$T : X  Y$denote the unique optimal transport map from f to g for the quadratic cost$\vert x - y \vert ^ { 2 } / 2$. Then there exist two open sets$X ^ { \prime } \subset X$ and$Y ^ { \prime } \subset Y$, with$| X \setminus X ^ { \prime } | = | Y \setminus Y ^ { \prime } | = 0$, such that$T : X ^ { \prime } \to Y ^ { \prime }$is a smooth difeomorphism.

In the case of general cost functions on$\mathbb { R } ^ { n }$, or when$c ( x , y ) \ : = \ : d ( x , y ) ^ { 2 } / 2$on a Riemannian manifold M$( d ( x , y )$being the Riemannian distance), the situation is much more complicated. Indeed, as shown by Ma, Trudinger, and Wang [33], and Loeper [31], in addition to suitable convexity assumptions on the support of the target density (or on the cut locus of the manifold when supp(g) = M [24]), a very strong structural condition on the cost function, the so-called MTW condition, is needed to ensure the smoothness of the map.

More precisely, if the MTW condition holds (together with some suitable convexity assumptions on the target domain), then the optimal map is smooth [35, 36, 21, 30, 19]. On the other hand, if the MTW condition fails at one point, then one can construct smooth densities (both supported on domains which satisfy the needed convexity assumptions) for which the optimal transport map is not continuous [31] (see also [15]).

In the case of Riemannian manifolds, the MTW condition for$c = d ^ { 2 } / 2$is very restrictive: indeed, as shown by Loeper [31], it implies that M has non-negative sectional curvature, and actually it is much stronger than the latter [28, 23]. In particular, if M has negative sectional curvature, then the MTW condition fails at every point. Let us also mention that, up to now, the MTW condition is known to be satisfied only for very special classes of Riemannian manifolds, such as spheres, their products, their quotients and submersions, and their perturbations [32, 22, 10, 29, 25, 20, 11], and for instance it is known to fail on suficiently flat ellipsoids [23].

The goal of the present paper is to show that, even without any condition on the cost function or on the supports of the densities, optimal transport maps are always smooth outside a closed singular set of measure zero. In order to state our results, we first have to introduce some basic assumptions on the cost functions which are needed to ensure existence and uniqueness of optimal maps. As before, X and Y denote two open subsets of$\mathbb { R } ^ { n }$

(C0) The cost function$c : X \times Y  \mathbb { R }$is of class$C ^ { 2 , \alpha }$for some$\alpha \in ( 0 , 1 )$, with$\| c \| _ { C ^ { 2 , \alpha } ( X \times Y ) } < \infty$

(C1) For any$x \in X$, the map$Y \ni y \mapsto - D _ { x } c ( x , y ) \in \mathbb { R } ^ { n }$is injective.

(C2) For any$y \in Y$, the map$X \ni x \mapsto - D _ { u } c ( x , y ) \in \mathbb { R } ^ { n }$is injective.

(C3)$\operatorname* { d e t } ( D _ { x y } c ) ( x , y ) \neq 0$for all$( x , y ) \in X \times Y$

Here are our main results:

Theorem 1.3. Let X,$Y \subset \mathbb { R } ^ { n }$be two bounded open sets, and let$f : X \to \mathbb { R } ^ { + }$and$g : Y \to \mathbb { R } ^ { + }$ be two continuous probability densities, respectively bounded away from zero and infinity on X and Y. Assume that the cost$c : X \times Y \to \mathbb { R }$satisfies (C0)-(C3), and denote by$T : X  Y$ the unique optimal transport map sending f onto g. Then there exist two relatively closed sets $\Sigma _ { X } \subset X , \Sigma _ { Y } \subset Y$of measure zero such that$T : X \setminus \Sigma _ { X } \to Y \setminus \Sigma _ { Y }$is a homeomorphism of class $C _ { \mathrm { l o c } } ^ { 0 , \beta }$for any$\beta < 1$. In addition, i$f c \in C _ { \mathrm { l o c } } ^ { k + 2 , \alpha } ( X \times Y ) , f \in C _ { \mathrm { l o c } } ^ { k , \alpha } ( X )$, and$g \in C _ { \mathrm { l o c } } ^ { k , \alpha } ( Y )$for some $k \geq 0$and$\alpha \in ( 0 , 1 )$, then$T : X \setminus \Sigma _ { X } \to Y \setminus \Sigma _ { Y }$is a difeomorphism of class$C _ { \mathrm { l o c } } ^ { k + 1 , \alpha }$

Theorem 1.4. Let M be a smooth Riemannian manifold, and let$f , g : M \to \mathbb { R } ^ { + }$be two continuous probability densities, locally bounded away from zero and infinity on M. Let$T : M \to M$denote the optimal transport map for the cost$c = d ^ { 2 } / 2$sending f onto g. Then there exist two closed sets $\Sigma _ { X } , \Sigma _ { Y } \subset M$of measure zero such that$T : M \setminus \Sigma _ { X }  M \setminus \Sigma _ { Y }$is a homeomorphism of class$C _ { \mathrm { l o c } } ^ { 0 , \beta }$ for any$\beta < 1$. In addition, if both f and g are of class$C ^ { k , \alpha }$, then$T : M \setminus \Sigma _ { X } \to M \setminus \Sigma _ { Y }$is a difeomorphism of class$C _ { \mathrm { l o c } } ^ { k + 1 , \alpha }$

The paper is structured as follows: in the next section we introduce some notation and preliminary results. Then, in Section 3, we show how both Theorem 1.3 and Theorem 1.4 are a direct consequence of some local regularity results around diferentiability points of$T$, see Theorems 4.3 and 5.3. Finally, Sections 4 and 5 are devoted to the proof of these local results.

Acknowledgements: We wish to thank Luigi Ambrosio for his careful reading of a preliminary version of this manuscript. AF is partially supported by NSF Grant DMS-0969962. Both authors acknowledge the support of the ERC ADG Grant GeMeThNES.

## 2. Notation and preliminary results

Through a well established procedure, maps that solve optimal transport problems derive from a c-convex potential, itself solution to a Monge-Amp\`ere type equation.

More precisely, given a cost function$c : X \times Y  \mathbb { R }$, a function u$: X \to \mathbb { R }$is said c-convex if it can be written as

$$
u (x) = \sup _ {y \in Y} \left\{- c (x, y) + \lambda_ {y} \right\},\tag{2.1}
$$

for some constants$\lambda _ { y } \in \mathbb { R } \cup \{ - \infty \}$

Similarly to the subdiferential for convex function, for c-convex functions one can talk about their c-subdiferential: if$u : X \to \mathbb { R }$is a c-convex function as above, the c-subdiferential of u at x is the (nonempty) set

$$
\partial_ {c} u (x) := \{y \in \overline {{Y}}: u (z) \geq - c (z, y) + c (x, y) + u (x) \quad \forall z \in X \}.\tag{2.2}
$$

If$x _ { 0 } \in X$and$y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$, we will say that the function

$$
C _ {x _ {0}, y _ {0}} (\cdot) := - c (\cdot , y _ {0}) + c (x _ {0}, y _ {0}) + u (x _ {0})\tag{2.3}
$$

is a c-support for u at$x _ { 0 }$. We also define the Frechet subdiferential of u at x as

$$
\partial^ {-} u (x) := \left\{p \in \mathbb {R} ^ {n}: u (z) \geq u (x) + p \cdot (z - x) + o (| z - x |) \right\}.
$$

We will use the following notation: if$E \subset X$then

$$
\partial_ {c} u (E) := \bigcup_ {x \in E} \partial_ {c} u (x), \quad \partial^ {-} u (E) := \bigcup_ {x \in E} \partial^ {-} u (x).
$$

It is easy to check that, if c is of class$C ^ { 1 }$, then the following inclusion holds:

$$
y \in \partial_ {c} u (x) \quad \Longrightarrow \quad - D _ {x} c (x, y) \in \partial^ {-} u (x).\tag{2.4}
$$

In addition, if c satisfies (C0)-(C2), then we can define the c-exponential map:

$$
\text {for any} x \in X, y \in Y, p \in \mathbb {R} ^ {n}, \qquad \left\{ \begin{array}{l l} \mathrm{c} \text {-exp} _ {x} (p) = y & \Leftrightarrow \quad p = - D _ {x} c (x, y) \\ \mathrm{c} ^ {*} \text {-exp} _ {y} (p) = x & \Leftrightarrow \quad p = - D _ {y} c (x, y) \end{array} \right.\tag{2.5}
$$

Using (2.5), we can rewrite (2.4) as

$$
\partial_ {c} u (x) \subset \mathrm{c-exp} _ {x} \left(\partial^ {-} u (x)\right).\tag{2.6}
$$

Notice that, if$c \in C ^ { 1 }$and Y is bounded, it follows immediately from (2.1) that c-convex functions are Lipschitz, so in particular they are diferentiable a.e.

The following notation will be convenient: given a c-convex function$u : X \to \mathbb { R }$, we define (at almost every point) the map$T _ { u } : X  Y$as

$$
T _ {u} (x) := \mathrm{c-exp} _ {x} (\nabla u (x)).\tag{2.7}
$$

(Of course$T _ { u }$depends also on$^ { c , }$but to keep the notation lighter we prefer not to make this dependence explicit. The reader should keep in mind that, whenever we write$T _ { u }$, the cost c is always the one for which u is c-convex.)

Finally, let us observe that if c satisfies (C0) and Y is bounded, then it follows from (2.1) that u is semiconvex (i.e., there exists a constant$C > 0$such that$u + C | x | ^ { 2 } / 2$is convex, see for instance [13]). In particular, by Alexandrov’s Theorem, c-convex functions are twice diferentiable a.e. (see [37, Theorem 14.25] for a list of diferent equivalent definitions of this notion).

The following is a basic result in optimal transport theory (see for instance [37, Chapter 10]):

Theorem 2.1. Let$c : X \times Y \to \mathbb { R }$satisfy (C0)-(C1). Given two probability densities$f$and g supported on X and Y respectively, there exists a c-convex function$u : X  \mathbb { R }$such that $T _ { u } : X  Y$is the unique optimal transport map sending f onto$g .$

In the particular case$c ( x , y ) = - x \cdot y$(which is equivalent to the quadratic cost$| x - y | ^ { 2 } / 2 )$，c-convex functions are convex and the above result takes the following simple form [2]:

Theorem 2.2. Let$c ( x , y ) = - x \cdot y$. Given two probability densities f and$g$supported on X and $Y$respectively, there exists a convex function$v : X  \mathbb { R }$such that$T _ { v } = \nabla v : X  Y$is the unique optimal transport map sending f onto$g .$

Although on Riemannian manifolds the cost function$c = d ^ { 2 } / 2$is not smooth everywhere, one can still prove existence of optimal maps [34, 13, 17] (let us remark that, in this case, the c-exponential map coincides with the classical exponential map in Riemannian geometry):

Theorem 2.3. Let M be a smooth Riemannian manifold, and$c = d ^ { 2 } / 2$. Given two probability densities f and g supported on M, there exists a c-convex function u :$M \to \mathbb { R } \cup \{ + \infty \}$such that u is diferentiable$f { \mathrm { - } } a . e .$, and$T _ { u } ( x ) = \mathrm { e x p } _ { x } ( \nabla u ( x ) )$is the unique optimal transport map sending f onto g.

We conclude this section by recalling that c-convex functions arising in optimal transport problems solve a Monge-Amp\`ere type equation almost everywhere, referring to [1, Section 6.2], [37, Chapters 11 and 12], and [15] for more details.

Whenever c satisfies (C0)-(C3), then the transport condition$( T _ { u } ) _ { \sharp } f = g$gives

$$
| \det (D T _ {u} (x)) | = \frac {f (x)}{g (T _ {u} (x))}\tag{2.8}
$$

In addition, the c-convexity of u implies that, at every point x where u is twice diferentiable,

$$
D ^ {2} u (x) + D _ {x x} c \bigl (x, \mathrm{c-exp} _ {x} (\nabla u (x)) \bigr) \geq 0.\tag{2.9}
$$

Hence, writing (2.7) as

$$
- D _ {x} c (x, T _ {u} (x)) = \nabla u (x),
$$

diferentiating the above relation with respect to x, and using (2.8) and (2.9), we obtain (2.10)

$$
\det \Big (D ^ {2} u (x) + D _ {x x} c \big (x, \mathrm{c-exp} _ {x} (\nabla u (x)) \big) \Big) = \left| \det \big (D _ {x y} c \big (x, \mathrm{c-exp} _ {x} (\nabla u (x)) \big) \big) \right| \frac {f (x)}{g (\mathrm{c-exp} _ {x} (\nabla u (x)))}
$$

at every point x where u it is twice diferentiable. In particular, when$c ( x , y ) = - x \cdot y .$, the convex function v provided by Theorem 2.2 solves the classical Monge-Amp\`ere equation

$$
\det \bigl (D ^ {2} v (x) \bigr) = \frac {f (x)}{g (\nabla v (x))}
$$

## 3. The localization argument and proof of the results

The goal of this section is to prove Theorems 1.3 and 1.4 by showing that the assumptions of Theorems 4.3 and 5.3 below are satisfied near almost every point.

The rough idea is the following: if ¯x is a point where the semiconvex function u is twice diferentiable, then around that point u looks like a parabola. In addition, by looking close enough to x¯, the cost function c will be very close to the linear one and the densities will be almost constant there. Hence we can apply Theorem 4.3 to deduce that u is of class$C ^ { 1 , \beta }$in neighborhood of ¯x (resp.

u is of class$C ^ { k + 2 , \alpha }$by Theorem 5.3, if$c \in C _ { \mathrm { l o c } } ^ { k + 2 , \alpha }$and$f , g \in C _ { \mathrm { l o c } } ^ { k , \alpha } )$, which implies in particular that $T _ { u }$is of class$C ^ { 0 , \beta }$in neighborhood of ¯x (resp.$T _ { u }$is of class$C ^ { k + 1 , \alpha }$by Theorem 5.3, if$c \in C _ { \mathrm { l o c } } ^ { k + 2 , \alpha }$ and$f , g \in C _ { \mathrm { l o c } } ^ { k , \alpha } )$. Being our assumptions completely symmetric in x and$y ,$we can apply the same argument to the optimal map$T ^ { * }$sending$g$onto$f .$. Since$T ^ { * } = ( T _ { u } ) ^ { - 1 }$(see the discussion below), it follows that$T _ { u }$is a global homeomorphism of class$C _ { \mathrm { l o c } } ^ { 0 , \beta }$(resp.$T _ { u }$is a global difeomorphism of class$C _ { \mathrm { l o c } } ^ { k + 1 , \alpha } )$outside a closed set of measure zero.

We now give a detailed proof.

Proof of Theorem 1.3. Let us introduce the “c-conjugate” of$u ,$that is, the function$u ^ { c } : Y  \mathbb { R }$ defined as

$$
u ^ {c} (y) := \sup _ {x \in X} \bigl \{- c (x, y) - u (x) \bigr \}.
$$

Then$u ^ { c }$is$c ^ { * } .$-convex, where

$$
c ^ {*} (y, x) := c (x, y), \quad \text { and } \quad x \in \partial_ {c ^ {*}} u ^ {c} (y) \quad \Leftrightarrow \quad y \in \partial_ {c} u (x)\tag{3.1}
$$

(see for instance [37, Chapter 5]).

Being our assumptions completely symmetric in x and$y , c ^ { * }$satisfies the same assumptions as c. In particular, by Theorem 2.1, there exists an optimal map$T ^ { * }$(with respect to$c ^ { * } )$sending g onto $f .$In addition, it is well-known that$T ^ { * }$is actually equal to

$$
T _ {u ^ {c}} (y) = \mathrm{c} ^ {*} \text {-exp} _ {y} \left(\nabla u ^ {c} (y)\right),
$$

and that$T _ { u }$and$\boldsymbol { T _ { u ^ { c } } }$are inverse to each other, that is

$$
T _ {u ^ {c}} \big (T _ {u} (x) \big) = x, \quad T _ {u} \big (T _ {u ^ {c}} (y) \big) = y \quad \text {   for   a.e.   } x \in X, y \in Y\tag{3.2}
$$

(see, for instance, [1, Remark 6.2.11]).

Since semiconvex functions are twice diferentiable$\mathrm { { a . e . } }$, there exist sets$X _ { 1 } \subset X , Y _ { 1 } \subset Y$of full measure such that (3.2) holds for every$x \in X _ { 1 }$and$y \in Y _ { 1 }$, and in addition u is twice diferentiable for every$x \in X _ { 1 }$and$u ^ { c }$is twice diferentiable for every$y \in Y _ { 1 }$. Let us define

$$
X ^ {\prime} := X _ {1} \cap (T _ {u}) ^ {- 1} (Y _ {1}).
$$

Using that$T _ { u }$transports$f$on$g$and that the two densities are bounded away from zero and infinity, we see that$X ^ { \prime }$is of full measure in$X$

We fix a point${ \bar { x } } \in X ^ { \prime }$. Since u is diferentiable at ¯x (being twice diferentiable), it follows by (2.6) that the set$\partial _ { c } { u } ( \bar { x } )$is a singleton, namely$\partial _ { c } u ( \bar { x } ) = \{ \mathrm { c } \mathrm { - } \mathrm { e x p } _ { \bar { x } } ( \nabla u ( \bar { x } ) ) \}$. Set$\bar { y } : = \mathrm { c } \mathrm { - } \mathrm { e x p } _ { \bar { x } } ( \nabla u ( \bar { x } ) )$ Since$\bar { y } \in Y _ { 1 }$(by definition of$X ^ { \prime } ) , u ^ { c }$is twice diferentiable at ¯y and$\bar { x } = T _ { u ^ { c } } ( \bar { y } )$. Up to a translation in the system of coordinates (both in x and$y )$we can assume that both ¯x and$\bar { y }$coincide with the origin 0.

Let us define

$$
\begin{array}{l} \bar {u} (z) := u (z) - u (\mathbf {0}) + c (z, \mathbf {0}) - c (\mathbf {0}, \mathbf {0}), \\ \bar {c} (z, w) := c (z, w) - c (z, \mathbf {0}) - c (\mathbf {0}, w) + c (\mathbf {0}, \mathbf {0}), \\ \bar {u} ^ {\bar {c}} (w) := u ^ {c} (w) - u (\mathbf {0}) + c (\mathbf {0}, w) - c (\mathbf {0}, \mathbf {0}). \end{array}
$$

Then ¯u is a ¯c-convex function,$\bar { u } ^ { \bar { c } }$is its ¯c-conjugate,$T _ { \bar { u } } = T _ { u } ,$and$T _ { \bar { u } ^ { \bar { c } } } ~ = ~ T _ { u ^ { c } }$, so in particular $( T _ { \bar { u } } ) _ { \sharp } f = g$and$( T _ { \bar { u } ^ { \bar { c } } } ) _ { \sharp } g = f$. In addition, because by assumption$\mathbf { 0 } \in X ^ { \prime }$, ¯u is twice diferentiable at 0 and$\bar { u } ^ { \bar { c } }$is twice diferentiable at${ \mathbf 0 } = T _ { \bar { u } } ( { \mathbf 0 } )$. Let us define$P : = D ^ { 2 } \bar { u } ( \mathbf { 0 } )$(0), and$M : = D _ { x y } \bar { c } ( \mathbf { 0 } , \mathbf { 0 } )$ Then, since$\bar { c } ( \cdot , { \bf 0 } ) = \bar { c } ( { \bf 0 } , \cdot ) \equiv 0$and$\bar { c } \in C ^ { 2 , \alpha }$, a Taylor expansion gives

$$
\bar {u} (z) = \frac {1}{2} P z \cdot z + o (| z | ^ {2}), \qquad \bar {c} (z, w) = M z \cdot w + O (| z | ^ {2 + \alpha} + | w | ^ {2 + \alpha}),
$$

Let us observe that, since by assumption$f$and g are bounded away from zero and infinity, by (C3) and (2.10) applied to ¯u and ¯c we get that de$\mathbf { \Gamma } ( P ) , \operatorname* { d e t } ( M ) \neq 0$. In addition (2.9) implies that $P$is a positive definite symmetric matrix. Hence, we can perform a second change of coordinates: $z \mapsto \tilde { z } : = P ^ { 1 / 2 } z , w \mapsto \tilde { w } : = - P ^ { - 1 / 2 } M ^ { * } w$(M∗ being the transpose of M), so that, in the new variables,

$$
\tilde {u} (\tilde {z}) := \bar {u} (z) = \frac {1}{2} | \tilde {z} | ^ {2} + o (| \tilde {z} | ^ {2}), \qquad \tilde {c} (\tilde {z}, \tilde {w}) := \bar {c} (z, w) = - \tilde {z} \cdot \tilde {w} + O (| z | ^ {2 + \alpha} + | w | ^ {2 + \alpha}).\tag{3.3}
$$

By an easy computation it follows that$( T _ { \tilde { u } } ) _ { \sharp } \tilde { f } = \tilde { g }$, where <sup>1</sup>

$$
\tilde {f} (\tilde {z}) := \det (P ^ {- 1 / 2}) f (P ^ {- 1 / 2} \tilde {z}), \quad \tilde {g} (\tilde {w}) := \left| \det \left((M ^ {*}) ^ {- 1} P ^ {1 / 2}\right) \right| g (- (M ^ {*}) ^ {- 1} P ^ {1 / 2} \tilde {w}).\tag{3.4}
$$

Notice that

$$
D _ {\tilde {z} \tilde {z}} \tilde {c} (\mathbf {0}, \mathbf {0}) = D _ {\tilde {w} \tilde {w}} \tilde {c} (\mathbf {0}, \mathbf {0}) = \mathbf {0} _ {n \times n}, - D _ {\tilde {z} \tilde {w}} \tilde {c} (\mathbf {0}, \mathbf {0}) = \mathrm{Id}, D ^ {2} \tilde {u} (\mathbf {0}) = \mathrm{Id},\tag{3.5}
$$

so, using (2.10), we deduce that

$$
\frac {\tilde {f} (\mathbf {0})}{\tilde {g} (\mathbf {0})} = \frac {\det \left(D ^ {2} \tilde {u} (\mathbf {0}) + D _ {\tilde {z} \tilde {z}} \tilde {c} (\mathbf {0} , \mathbf {0})\right)}{\left| \det \left(D _ {\tilde {z} \tilde {w}} \tilde {c} (\mathbf {0} , \mathbf {0})\right) \right|} = 1.\tag{3.6}
$$

To ensure that we can apply Theorems 4.3 and 5.3, we now perform the following dilation: for $\rho > 0$we define

$$
u _ {\rho} (\tilde {z}) := \frac {1}{\rho^ {2}} \tilde {u} (\rho \tilde {z}), \qquad c _ {\rho} (\tilde {z}, \tilde {w}) := \frac {1}{\rho^ {2}} \tilde {c} (\rho \tilde {z}, \rho \tilde {w}).
$$

We claim that, provided$\rho$is suficiently small,$u _ { \rho }$and$c _ { \rho }$satisfy the assumptions of Theorems 4.3 and 5.3.

Indeed, it is immediate to check that$u _ { \rho }$is a$c _ { \rho ^ { - } }$-convex function. Also, by the same argument as above, from the relation$( T _ { \tilde { u } } ) _ { \sharp } \tilde { f } = \tilde { g }$we deduce that$T _ { u _ { \rho } }$sends$\tilde { f } ( \rho \tilde { z } )$onto$\tilde { g } ( \rho \tilde { w } )$. In addition, since we can freely multiply both densities by a same constant, it actually follows from (3.6) that $( T _ { u _ { \rho } } ) _ { \sharp } f _ { \rho } = g _ { \rho }$, where

$$
f _ {\rho} (\tilde {z}) := \frac {\tilde {f} (\rho \tilde {z})}{\tilde {f} (\mathbf {0})}, \qquad g _ {\rho} (\tilde {w}) := \frac {\tilde {g} (\rho \tilde {w})}{\tilde {g} (\mathbf {0})}.
$$

In particular, since f and g are continuous, we get

$$
\left| f _ {\rho} - 1 \right| + \left| g _ {\rho} - 1 \right|\rightarrow 0 \quad \text { inside } B _ {3}\tag{3.7}
$$

as$\rho \to 0$. Also, by (3.3) we get that, for any$\tilde { z } , \tilde { w } \in B _ { 3 }$2

$$
u _ {\rho} (\tilde {z}) = \frac {1}{2} | \tilde {z} | ^ {2} + o (1), \qquad c _ {\rho} (\tilde {z}, \tilde {w}) = - \tilde {z} \cdot \tilde {w} + O (\rho^ {\alpha} | z | ^ {2 + \alpha} + \rho^ {\alpha} | w | ^ {2 + \alpha}).,\tag{3.8}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">µ := f(x)dx</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ν := g(y)dy</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f(x)dx = f<sup>˜</sup>(˜x)dx, g ˜ (y)dy = ˜g(˜y)dy.˜</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup> An easy way to check this is to observe that the measures µ := f(x)dx and ν := g(y)dy are independent of the choice of coordinates, hence (3.4) follows from the identities</span></small>

where$o ( 1 )  0$as$\rho \to 0$. In particular, it follows easily that (4.9) and (4.10) hold with any positive constants$\delta _ { 0 } , \eta _ { 0 }$provided$\rho$is small enough.

Furthermore, by the second order diferentiability of ˜u at 0 it follows that the multivalued map $\tilde { z } \mapsto \partial ^ { - } \bar { u } ( \tilde { z } )$is diferentiable at 0 (see [37, Theorem 14.25]) with gradient equal to the identity matrix (see (3.3)), hence

$$
\partial^ {-} u _ {\rho} (\tilde {z}) \subset B _ {\gamma_ {\rho}} (\tilde {z}) \quad \forall \tilde {z} \in B _ {2},
$$

where$\gamma _ { \rho } \to 0$as$\rho \to 0$. Since$\partial _ { c _ { \rho } } u _ { \rho } \subset \mathrm { c } _ { \rho ^ { - } } \mathrm { e x p } \left( \partial ^ { - } u _ { \rho } \right)$(by (2.6)) and$\| \mathrm { c } _ { \rho } \mathrm { - e x p - I d } \| _ { \infty } = o ( 1 )$(by (3.8)), we get

$$
\partial_ {c _ {\rho}} u _ {\rho} (\tilde {z}) \subset B _ {\delta_ {\rho}} (\tilde {z}) \quad \forall \tilde {z} \in B _ {3},\tag{3.9}
$$

with$\delta _ { \rho } = o ( 1 )$as$\rho \to 0$. Moreover, the$c _ { \rho ^ { - } }$-conjugate of$u _ { \rho }$is easily seen to be

$$
u _ {\rho} ^ {c _ {\rho}} (\tilde {w}) = \bar {u} ^ {\bar {c}} \bigl (\rho (M ^ {*}) ^ {- 1} P ^ {1 / 2} \tilde {w} \bigr).
$$

Since$u ^ { c }$is twice diferentiable at 0, so is$u _ { \rho } ^ { c _ { \rho } }$. In addition, an easy computation <sup>2</sup> shows that $D ^ { 2 } u _ { \rho } ^ { c _ { \rho } } ( \mathbf { 0 } ) = \mathrm { I d }$. Hence, arguing as above we obtain that

$$
\partial_ {c _ {\rho} ^ {*}} u _ {\rho} ^ {c _ {\rho}} (\tilde {w}) \subset B _ {\delta_ {\rho} ^ {\prime}} (\tilde {w}) \qquad \forall   \tilde {w} \in B _ {3},\tag{3.10}
$$

with$\delta _ { \rho } ^ { \prime } = o ( 1 )$as$\rho \to 0$

We now define

$$
\mathcal {C} _ {1} := \overline {{{B}}} _ {1}, \qquad \mathcal {C} _ {2} := \partial_ {c _ {\rho}} u _ {\rho} (\mathcal {C} _ {1}).
$$

Observe that both$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$are closed (since the c-subdiferential of a compact set is closed). Also, thanks to (3.9), by choosing$\rho$small enough we can ensure that$B _ { 1 / 3 } \subset \mathcal { C } _ { 2 } \subset B _ { 3 }$. Finally, it follows from (2.6) that

$$
(T _ {u _ {\rho}}) ^ {- 1} (\mathcal {C} _ {2}) \setminus \mathcal {C} _ {1} \subset (T _ {u _ {\rho}}) ^ {- 1} \bigl (\{\text { points   of   non - differentiability   of } u _ {\rho} ^ {c _ {\rho}} \} \bigr),
$$

and since this latter set has measure zero, a simple computation shows that

$$
\left(T _ {u _ {\rho}}\right) _ {\sharp} (f _ {\rho} \mathbf {1} _ {\mathcal {C} _ {1}}) = g _ {\rho} \mathbf {1} _ {\mathcal {C} _ {2}}.
$$

Thus, thanks to (4.8), we get that for any$\beta < 1$the assumptions of Theorem 4.3 are satisfied, provided we choose$\rho$suficiently small. Moreover, if in addition$c \in C _ { \mathrm { l o c } } ^ { k + 2 , \alpha } ( X \times Y ) , f \in C _ { \mathrm { l o c } } ^ { k , \alpha } ( X )$ and$g \in C _ { \mathrm { l o c } } ^ { k , \alpha } ( Y )$, then also the assumptions of Theorem 5.3 are satisfied.

Hence, by applying Theorem 4.3 (resp. Theorem 5.3) we deduce that$u _ { \rho } \in C ^ { 1 , \beta } ( B _ { 1 / 7 } )$(resp. $u _ { \rho } \in C ^ { k + 2 , \alpha } ( B _ { 1 / 9 } ) )$, so going back to the original variables we get the existence of a neighborhood$\mathcal { U } _ { \bar { x } }$ of ¯x such that$u \in C ^ { 1 , \beta } ( \mathcal { U } _ { \bar { x } } )$(resp.$u \in C ^ { k + 2 , \alpha } ( \mathcal { U } _ { \bar { x } } ) )$. This implies in particular that$T _ { u } \in C ^ { 0 , \beta } ( \mathcal { U } _ { \bar { x } } )$ (resp.$T _ { u } \in C ^ { k + 1 , \alpha } ( \mathcal { U } _ { \bar { x } } ) ,$). Moreover, it follows by Corollary 4.6 that$T _ { u } ( U _ { \bar { x } } )$contains a neighborhood of${ \bar { y } } .$

We now observe that, by symmetry, we can also apply Theorem 4.3 (resp. Theorem 5.3) to$u _ { \rho } ^ { c _ { \rho } }$ Hence, there exists a neighborhood$\mathcal { V } _ { \bar { y } }$of$\bar { y }$such that$T _ { u ^ { c } } \in C ^ { 0 , \beta } ( \mathcal { V } _ { \bar { y } } )$. Since$T _ { u }$and$\boldsymbol { T _ { u ^ { c } } }$are inverse

$$
D _ {\tilde {z}} c _ {\rho} \big (\tilde {z}, T _ {u _ {\rho}} (\tilde {z}) \big) = - \nabla u _ {\rho} (\tilde {z}) \quad \mathrm{and} \quad D _ {\tilde {w}} c _ {\rho} \big (T _ {u _ {\rho} ^ {c _ {\rho}}} (\tilde {w}), \tilde {w} \big) = - \nabla u _ {\rho} ^ {c _ {\rho}} (\tilde {w})
$$

at and using then (3.5) and the fact that$\nabla T _ { u _ { \rho } ^ { c _ { \rho } } } ( \mathbf { 0 } ) = [ \nabla T _ { u _ { \rho } } ( \mathbf { 0 } ) ] ^ { - 1 } \mathrm { ~ a n d ~ } D ^ { 2 } u _ { \rho } ( \mathbf { 0 } ) = \mathrm { I d }$ to each other (see (3.2)) we deduce that, possibly reducing the size of$\ d \mathcal { U } _ { \bar { x } } , \ d T _ { u }$is a homeomorphism (resp. difeomorphism) between$\mathcal { U } _ { \bar { x } }$and$T _ { u } ( u _ { \bar { x } } )$. Let us consider the open sets

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">0,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>For instance, this follows by diferentiating both relations</span></small>

$$
X ^ {\prime \prime} := \bigcup_ {\bar {x} \in X ^ {\prime}} \mathcal {U} _ {\bar {x}}, \qquad Y ^ {\prime \prime} := \bigcup_ {\bar {x} \in X ^ {\prime}} T _ {u} (\mathcal {U} _ {\bar {x}}),
$$

and define the (relatively) closed$\Sigma _ { X } : = X \setminus X ^ { \prime \prime } , \Sigma _ { Y } : = Y \setminus Y ^ { \prime \prime }$. Since$X ^ { \prime \prime } \supset X ^ { \prime } , X ^ { \prime \prime }$is a set of full measure, so$| \Sigma _ { X } | = 0$. In addition, since$\Sigma _ { Y } = Y \setminus Y ^ { \prime \prime } \subset Y \setminus T _ { u } ( X ^ { \prime } )$and$T _ { u } ( X ^ { \prime } )$has full measure in$Y .$, we also get that$\begin{array} { r } { | \Sigma _ { Y } | = 0 } \end{array}$

Finally, since$T _ { u } : X \setminus \Sigma _ { X } \to Y \setminus \Sigma _ { Y }$is a local homeomorphism (resp. difeomorphism), by (3.2) it follows that$T _ { u } : X \setminus \Sigma _ { X } \to Y \setminus \Sigma _ { Y }$is a global homeomorphism (resp. difeomorphism), which concludes the proof.

Proof of Theorem 1.4. The only diference with respect to the situation in Theorem 1.3 is that now the cost function$c = d ^ { 2 } / 2$is not smooth on the whole$M \times M$. However, even if$d ^ { 2 } / 2$is not everywhere smooth and M is not necessarily compact, it is still true that the c-convex function u provided by Theorem 2.3 is locally semiconvex (i.e., it is locally semiconvex when seen in any chart) [13, 17]. In addition, as shown in [9, Proposition 4.1] (see also [14, Section 3]), if u is twice diferentiable at x, then the point$T _ { u } ( x )$is not in the cut-locus of x. Since the cut-locus is closed and$d ^ { 2 } / 2$is smooth outside the cut-locus, we deduce the existence of a set X of full measure such that, if$x _ { 0 } \in X$, then: (1) u is twice diferentiable at x ; (2) there exists a neighborhood $\mathcal { U } _ { x _ { 0 } } \times \mathcal { V } _ { T _ { u } ( x _ { 0 } ) } \subset M \times M$of$( x _ { 0 } , T _ { u } ( x _ { 0 } ) )$such that$c \in C ^ { \infty } ( \mathcal { U } _ { x _ { 0 } } \times \mathcal { V } _ { T _ { u } ( x _ { 0 } ) } )$. Hence, by taking a local chart around$( x _ { 0 } , T _ { u } ( x _ { 0 } ) )$, the same proof as the one of Theorem 1.3 shows that$T _ { u }$is a local homeomorphism (resp. difeomorphism) around almost every point. Using as before that $T _ { u } : M \to M$is invertible a.e., it follows that$T _ { u }$is a global homeomorphism (resp. difeomorphism) outside a closed singular set of measure zero. We leave the details to the interested reader.

## 4. C<sup>1,β</sup> regularity and strict c-convexity

In this and the next section we prove that, if in some open set a c-convex function u is suficiently close to a parabola and the cost function is close to the linear one, then u is smooth in some smaller set.

The idea of the proof (which is reminiscent of the argument introduced by Cafarelli in [6] to show$W ^ { 2 , p }$and$C ^ { 2 , \alpha }$estimates for the classical Monge-Amp\`ere equation, though several additional complications arise in our case) is the following: since the cost function is close to the linear one and both densities are almost constant, u is close to a convex function v solving an optimal transport problem with linear cost and constant densities (Lemma 4.1). In addition, since u is close to a parabola, so is v. Hence, by [18] and Cafarelli’s regularity theory, v is smooth, and we can use this information to deduce that u is even closer to a second parabola (given by the second order Taylor expansion of v at the origin) inside a small neighborhood around of origin. By rescaling back this neighborhood at scale 1 and iterating this construction, we obtain that u is$C ^ { 1 , \beta }$at the origin for some$\beta \in ( 0 , 1 )$. Since this argument can be applied at every point in a neighborhood of the origin, we deduce that u is$C ^ { 1 , \beta }$there, see Theorem 4.3. (A similar strategy has also been used in [7] to show regularity optimal transport maps for the cost$| x - y | ^ { p }$, either when$p$is close to 2 or when X and Y are suficiently far from each other.)

Once this result is proved, we know that$\partial ^ { - } u$is a singleton at every point, so it follows from (2.6) that

$$
\partial_ {c} u (x) = \mathrm{c-exp} _ {x} (\partial^ {-} u (x)),
$$

see Remark 4.4 below. (The above identity is exactly what in general may fail for general c-convex functions, unless the MTW condition holds [31].) Thanks to this fact, we obtain that u enjoys a comparison principle (Proposition 5.2), and this allows us to use a second approximation argument with solutions of the classical Monge-Amp\`ere equation (in the spirit of$\left[ 6 , 2 7 \right] )$) to conclude that u is$C ^ { 2 , \sigma ^ { \prime } }$in a smaller neighborhood, for some$\sigma ^ { \prime } > 0$. Then higher regularity follows from standard elliptic estimates, see Theorem 5.3.

## Lemma 4.1. Let$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$be two closed sets such that

$$
B _ {1 / K} \subset \mathcal {C} _ {1}, \mathcal {C} _ {2} \subset B _ {K}\tag{4.1}
$$

for some$K \geq 1$, f and$g$two densities supported respectively in$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$, and$u : { \mathcal { C } } _ { 1 } \to$R a c-convex function such that$\partial _ { c } u ( \mathcal { C } _ { 1 } ) \subset B _ { K }$and$( T _ { u } ) _ { \sharp } f = g$. Let$\rho > 0$be such that$| \mathcal { C } _ { 1 } | = | \rho \mathcal { C } _ { 2 } |$ (where$\rho \mathcal { C } _ { 2 }$denotes the dilation of$\mathcal { C } _ { 2 }$with respect to the origin), and let v be a convex function such that$\nabla v _ { \sharp } \mathbf { 1 } _ { \mathcal { C } _ { 1 } } = \mathbf { 1 } _ { \rho \mathcal { C } _ { 2 } }$and$v ( \mathbf { 0 } ) = u ( \mathbf { 0 } )$. Then there exists an increasing function$\omega : \mathbb { R } ^ { + }  \mathbb { R } ^ { + }$ depending only K, and satisfying$\omega ( \delta ) \ge \delta$and$\omega ( 0 ^ { + } ) = 0$, such that, if

$$
\| f - \mathbf {1} _ {\mathcal {C} _ {1}} \| _ {\infty} + \| g - \mathbf {1} _ {\mathcal {C} _ {2}} \| _ {\infty} \leq \delta\tag{4.2}
$$

and

$$
\left\| c (x, y) + x \cdot y \right\| _ {C ^ {2} \left(B _ {K} \times B _ {K}\right)} \leq \delta ,\tag{4.3}
$$

then

$$
\left\| u - v \right\| _ {C ^ {0} (B _ {1 / K})} \leq \omega (\delta).
$$

Proof. Assume the lemma is false. Then there exists$\varepsilon _ { 0 } ~ > ~ 0$, a sequence of closed sets$\mathcal { C } _ { 1 } ^ { h } , \mathcal { C } _ { 2 } ^ { h }$ satisfying (4.1), functions$f _ { h } , \ g _ { h }$satisfying (4.2) with$\delta = 1 / h$, and costs$c _ { h }$converging in$C ^ { 2 }$to $- x \cdot y .$, such that

$$
u _ {h} (\mathbf {0}) = v _ {h} (\mathbf {0}) = 0 \quad \text { and } \quad \| u _ {h} - v _ {h} \| _ {C ^ {0} (B _ {1 / K})} \geq \varepsilon_ {0},
$$

where$u _ { h }$and$v _ { h }$are as in the statement. First, we extend$u _ { h }$an$v _ { h }$to$B _ { K }$as

$$
u _ {h} (x) := \sup _ {z \in \mathcal {C} _ {1} ^ {h}, y \in \partial_ {c _ {h}} u _ {h} (z)} \bigl \{u _ {h} (z) - c _ {h} (x, y) + c _ {h} (z, y) \bigr \}, \qquad v _ {h} (x) := \sup _ {z \in \mathcal {C} _ {1} ^ {h}, p \in \partial^ {-} v _ {h} (z)} \bigl \{v _ {h} (z) + p \cdot (x - z) \bigr \}.
$$

Notice that, since by assumption$\partial _ { c _ { h } } u _ { h } ( \mathcal { C } _ { 1 } ^ { h } ) \subset B _ { K }$, we have$\partial _ { c _ { h } } u _ { h } ( B _ { K } ) \subset B _ { K }$. Also,$( T _ { u _ { h } } ) _ { \sharp } f _ { h } = g _ { h }$ gives that$\textstyle \int f _ { h } = \int g _ { h }$, so it follows from (4.2) that

$$
\rho_ {h} = \left(| \mathcal {C} _ {1} ^ {h} | / | \mathcal {C} _ {2} ^ {h} |\right) ^ {1 / n} \to 1 \quad \text { as } h \to \infty ,
$$

which implies that ∂−$v _ { h } ( B _ { K } ) \subset B _ { \rho _ { h } K } \subset B _ { 2 K }$for h large. Thus, since the$C ^ { 1 }$-norm of$c _ { h }$is uniformly bounded, we deduce that both$u _ { h }$and$v _ { h }$are uniformly Lipschitz. Recalling that$u _ { h } ( \mathbf { 0 } ) = v _ { h } ( \mathbf { 0 } ) =$ 0, we get that, up to a subsequence,$u _ { h }$and$v _ { h }$uniformly converge inside$B _ { K }$to$u _ { \infty }$and$v _ { \infty }$ respectively, where

$$
u _ {\infty} (\mathbf {0}) = v _ {\infty} (\mathbf {0}) = 0 \quad \text { and } \quad \| u _ {\infty} - v _ {\infty} \| _ {C ^ {0} (B _ {1 / K})} \geq \varepsilon_ {0}.\tag{4.4}
$$

In addition$f _ { h } \ ( \mathrm { r e s p . } \ g _ { h } )$weak- converge in$L ^ { \infty }$to some density$f _ { \infty } \ ( \mathrm { r e s p . } \ g _ { \infty } )$supported in$\overline { { B } } _ { K }$ Also, since$\rho _ { h }  1$, using (4.2) we get that$\mathbf { 1 } _ { \mathcal { C } _ { 1 } ^ { h } } \ \mathrm { ( r e s p . } \ \mathbf { 1 } _ { \rho _ { h } \mathcal { C } _ { 2 } ^ { h } } \ \mathrm { ) }$weak- converges in$L ^ { \infty }$to$f _ { \infty } \ ( \mathrm { r e s p }$ $g _ { \infty } )$. Finally we remark that, because of (4.2) and the fact that$\mathcal { C } _ { 1 } ^ { h } \supset B _ { 1 / K }$, we also have

$$
f _ {\infty} \geq \mathbf {1} _ {B _ {1 / K}}.
$$

In order to get a contradiction we have to show that$u _ { \infty } = v _ { \infty }$in$B _ { 1 / K }$. To see this, we apply [37, Theorem 5.20] to deduce that both$\nabla u _ { \infty }$and$\nabla \boldsymbol { v } _ { \infty }$are optimal transport maps for the linear cost$- \boldsymbol { x } \cdot \boldsymbol { y }$sending$f _ { \infty }$onto$g _ { \infty }$. By uniqueness of the optimal map (see Theorem 2.2) we deduce that$\nabla \boldsymbol { v } _ { \infty } = \nabla \boldsymbol { u } _ { \infty }$almost everywhere inside$B _ { 1 / K } \subset \mathrm { s p t } f _ { \infty }$, hence$u _ { \infty } = v _ { \infty }$in$B _ { 1 / K }$(since $u _ { \infty } ( \mathbf { 0 } ) = v _ { \infty } ( \mathbf { 0 } ) = 0 )$, contradicting (4.4).

Here and in the sequel, we use$\mathcal { N } _ { r } ( E )$to denote the r-neighborhood of a set E.

Lemma 4.2. Let u and v be, respectively, c-convex and convex, let$D \in \mathbb { R } ^ { n \times n }$be a symmetric matrix satisfying

$$
\operatorname{Id} / K \leq D \leq K \operatorname{Id}\tag{4.5}
$$

for some$K \geq 1$, and define the ellipsoid

$$
E (x _ {0}, h) := \left\{x: D (x - x _ {0}) \cdot (x - x _ {0}) \leq h \right\}, \quad h > 0.
$$

Assume that there exist small positive constants$\varepsilon , \delta$such that

$$
\| v - u \| _ {C ^ {0} (E (x _ {0}, h))} \leq \varepsilon , \quad \| c + x \cdot y \| _ {C ^ {2} (E (x _ {0}, h) \times \partial_ {c} u (E (x _ {0}, h))} \leq \delta .\tag{4.6}
$$

Then

$$
\partial_ {c} u \big (E (x _ {0}, h - \sqrt {\varepsilon}) \big) \subset \mathcal {N} _ {K ^ {\prime} (\delta + \sqrt {h \varepsilon})} \big (\partial v (E (x _ {0}, h)) \big) \qquad \forall 0 <   \varepsilon <   h ^ {2} \leq 1,\tag{4.7}
$$

where$K ^ { \prime }$depends only on$K$.

Proof. Up to a change of coordinates we can assume that$x _ { 0 } = \mathbf { 0 }$, and to simplify notation we set $E _ { h } : = E ( x _ { 0 } , h )$. Let us define

$$
\bar {v} (x) := v (x) + \varepsilon + 2 \sqrt {\varepsilon} (D x \cdot x - h),
$$

so that$\bar { v } \geq u$outside$E _ { h }$, and$\bar { v } \leq u$inside$E _ { h - \sqrt { \varepsilon } }$. Then, taking a c-support to u in$E _ { h - \sqrt { \varepsilon } } \ ( \mathrm { i . e . , ~ a ~ }$ function$C _ { x , y }$as in (2.3), with$x \in E _ { h - \sqrt { \varepsilon } }$and$\dot { y } \in \partial _ { c } { u } ( x ) )$, moving it down and then lifting it up until it touches ¯v from below, we see that it has to touch the graph of ¯v at some point$\bar { x } \in E _ { h } ;$: in other words <sup>3</sup>

$$
\partial_ {c} u (E _ {h - \sqrt {\varepsilon}}) \subset \partial_ {c} \bar {v} (E _ {h}).
$$

By (4.5) we see that diam$E _ { h } \le 2 \sqrt { K h } .$, so by a simple computation (using again (4.5)) we get

$$
\partial^ {-} \bar {v} (E _ {h}) \subset \mathcal {N} _ {4 K \sqrt {K h \varepsilon}} \bigl (\partial^ {-} v (E _ {h}) \bigr).
$$

Thus, since$\partial _ { c } \bar { v } ( E _ { h } ) \subset \mathrm { c } \mathrm { - e x p } \big ( \partial ^ { - } \bar { v } ( E _ { h } ) \big )$(by (2.6)) and$\| \exp - \operatorname { I d } \| _ { C ^ { 0 } } \leq \delta \ ( \log \ ( 4 . 6 ) )$, we easily deduce that

$$
\partial_ {c} u (E _ {h - \sqrt {\varepsilon}}) \subset \mathcal {N} _ {K ^ {\prime} (\delta + \sqrt {h \varepsilon})} \big (\partial^ {-} v (E _ {h}) \big),
$$

proving (4.7).

Theorem 4.3. Let$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$be two closed sets satisfying

$$
B _ {1 / 3} \subset \mathcal {C} _ {1}, \mathcal {C} _ {2} \subset B _ {3},
$$

let$f , g$be two densities supported in$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$respectively, and let$u : { \mathcal { C } } _ { 1 } \to$R be a c-convex function such that$\partial _ { c } u ( \mathcal { C } _ { 1 } ) \subset B _ { 3 }$and$( T _ { u } ) _ { \sharp } f = g$. Assume also that$c \in C ^ { 2 , \alpha } ( B _ { 3 } \times B _ { 3 } )$for some $\alpha \in ( 0 , 1 )$. Then, for every$\beta \in ( 0 , 1 )$there exist constants$\delta _ { 0 } , \eta _ { 0 } > 0$such that the following holds: if

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∂<sub>c</sub>v¯(x)  c-exp<sub>x</sub>(∂−v¯(x))</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup> Even if ¯v is not c-convex, it still makes sense to consider his c-subdiferential (notice that the c-subdiferential of ¯v may be empty at some points). In particular, the inclusion  still holds.</span></small>

(4.8)

$$
\| f - \mathbf {1} _ {\mathcal {C} _ {1}} \| _ {\infty} + \| g - \mathbf {1} _ {\mathcal {C} _ {2}} \| _ {\infty} \leq \delta_ {0},\tag{4.9}
$$

$$
\left\| c (x, y) + x \cdot y \right\| _ {C ^ {2, \alpha} \left(B _ {3} \times B _ {3}\right)} \leq \delta_ {0},
$$

and

$$
\left\| u - \frac {1}{2} | x | ^ {2} \right\| _ {C ^ {0} (B _ {3})} \leq \eta_ {0},\tag{4.10}
$$

then$u \in C ^ { 1 , \beta } ( B _ { 1 / 7 } )$

Proof. We divide the proof into several steps.

Step$\mathit { 1 } \colon \ u$is close to a strictly convex solution of the Monge Amp\`ere equation. Let$v : \mathbb { R } ^ { n }$R be a convex function such that$\nabla v _ { \sharp } \mathbf { 1 } _ { \mathcal { C } _ { 1 } } = \mathbf { 1 } _ { \rho \mathcal { C } _ { 2 } }$with$\rho = ( | \mathcal { C } _ { 1 } | / | \mathcal { C } _ { 2 } | ) ^ { 1 / n }$(see Theorem 2.2). Up to adding a constant to v, without loss of generality we can assume that$v ( \mathbf { 0 } ) = u ( \mathbf { 0 } )$. Hence, we can apply Lemma 4.1 to obtain

$$
\| v - u \| _ {C ^ {0} (B _ {1 / 3})} \leq \omega (\delta_ {0})\tag{4.11}
$$

for some (universal) modulus of continuity$\omega : \mathbb { R } ^ { + }  \mathbb { R } ^ { + }$, which combined with (4.10) gives

$$
\left\| v - \frac {1}{2} | x | ^ {2} \right\| _ {C ^ {0} (B _ {1 / 3})} \leq \eta_ {0} + \omega (\delta_ {0}).
$$

Also, since$\textstyle { \int _ { { \mathcal { C } } _ { 1 } } f = \int _ { { \mathcal { C } } _ { 2 } } g } .$it follows easily from (4.8) that$| \rho - 1 | \leq 3 \delta _ { 0 }$. By these two facts we get that$\partial ^ { - } v ( B _ { 1 / 4 } ) \subset B _ { 7 / 2 4 } \subset \rho \mathcal { C } _ { 2 }$provided$\delta _ { 0 }$and$\eta _ { 0 }$are small enough (recall that v is convex and that$B _ { 1 / 3 } \subset { \mathcal { C } } _ { 2 } )$, so we can apply [18, Proposition 3.4] to deduce that v is a strictly convex Alexandrov solution to the Monge-Amp\`ere equation

$$
\det D ^ {2} v = 1 \quad \text { in } B _ {1 / 4}.\tag{4.12}
$$

In addition, by a simple compactness argument, we see that the modulus of strict convexity of v inside$B _ { 1 / 4 }$is universal. So, by classical Pogorelov and Schauder estimates, we obtain the existence of a universal constant$K _ { 0 } \geq 1$such that

$$
\| v \| _ {C ^ {3} (B _ {1 / 5})} \leq K _ {0}, \quad \mathrm{Id} / K _ {0} \leq D ^ {2} v \leq K _ {0} \mathrm{Id} \quad \text {in} B _ {1 / 5}.\tag{4.13}
$$

In particular, there exists a universal value$\bar { h } > 0$such that, for all$x \in B _ { 1 / 7 }$

$$
Q (x, v, h) := \left\{z: v (z) \leq v (x) + \nabla v (x) \cdot (z - x) + h \right\} \subset \subset B _ {1 / 6} \quad \forall h \leq \bar {h}.
$$

Step 2: Sections of u are close to sections of v. Given$x \in B _ { 1 / 7 }$and$y \in \partial _ { c } u ( x )$, we define

$$
S (x, y, u, h) := \left\{z: u (z) \leq u (x) - c (z, y) + c (x, y) + h \right\}.
$$

We claim that, if$\delta _ { 0 }$is small enough, then for all$x \in B _ { 1 / 7 } , y \in \partial _ { c } u ( x )$, and$h \leq \bar { h } / 2$, it holds

$$
Q (x, v, h - K _ {1} \sqrt {\omega (\delta_ {0})}) \subset S (x, y, u, h) \subset Q (x, v, h + K _ {1} \sqrt {\omega (\delta_ {0})}),\tag{4.14}
$$

where$K _ { 1 } > 0$is a universal constant.

Let us show the first inclusion. For this, take$x \in B _ { 1 / 7 } , y \in \partial _ { c } u ( x )$, and define

$$
p _ {x} := - D _ {x} c (x, y) \in \partial^ {-} u (x).
$$

Since v has universal$C ^ { 2 }$bounds (see (4.13)) and u is semi-convex (with a universal bound), a simple interpolation argument gives

$$
| p _ {x} - \nabla v (x) | \leq K ^ {\prime} \sqrt {\| u - v \| _ {C ^ {0} (B _ {1 / 5})}} \leq K ^ {\prime} \sqrt {\omega (\delta_ {0})} \quad \forall x \in B _ {1 / 7}.\tag{4.15}
$$

In addition, by (4.9),

$$
\left| y - p _ {x} \right| \leq \left\| D _ {x} c + \operatorname{Id} \right\| _ {C ^ {0} \left(B _ {3} \times B _ {3}\right)} \leq \delta_ {0},\tag{4.16}
$$

hence

$$
| z \cdot p _ {x} + c (z, y) | \leq | z \cdot p _ {x} - z \cdot y | + | z \cdot y + c (z, y) | \leq 2 \delta_ {0} \quad \forall x, z \in B _ {1 / 7}.\tag{4.17}
$$

Thus, i$: z \in Q ( x , v , h - K _ { 1 } \sqrt { \omega ( \delta _ { 0 } ) } )$, by (4.11), (4.15), and (4.17) we get

$$
\begin{array}{r l} & u (z) \leq v (z) + \omega (\delta_ {0}) \leq v (x) + \nabla v (x) \cdot (z - x) + h - K _ {1} \sqrt {\omega (\delta_ {0})} + \omega (\delta_ {0}) \\ & \quad \leq u (x) + p _ {x} \cdot z - p _ {x} \cdot x + h - K _ {1} \sqrt {\omega (\delta_ {0})} + 2 \omega (\delta_ {0}) + 2 K ^ {\prime} \sqrt {\omega (\delta_ {0})} \\ & \quad \leq u (x) - c (z, y) + c (x, y) + h - K _ {1} \sqrt {\omega (\delta_ {0})} + 2 \omega (\delta_ {0}) + 2 K ^ {\prime} \sqrt {\omega (\delta_ {0})} + 4 \delta_ {0} \\ & \quad \leq u (x) - c (z, y) + c (x, y) + h, \end{array}
$$

provided$K _ { 1 } > 0$is suficiently large. This proves the first inclusion, and the second is analogous.

Step 3: Both the sections of u and their images are close to ellipsoids with controlled eccentricity, and u is close to a smooth function near$x _ { 0 }$. We claim that there exists a universal constant $K _ { 2 } \geq 1$such that the following holds: For every$\eta _ { 0 } > 0$small, there exist small positive constants $h _ { 0 } = h _ { 0 } ( \eta _ { 0 } )$and$\delta _ { 0 } = \delta _ { 0 } ( h _ { 0 } , \eta _ { 0 } )$such that, for all$x _ { 0 } \in B _ { 1 / 7 }$, there is a symmetric matrix A satisfying

$$
\operatorname{Id} / K _ {2} \leq A \leq K _ {2} \operatorname{Id}, \quad \det (A) = 1,\tag{4.18}
$$

and such that, for all$y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$

$$
A \left(B _ {\sqrt {h _ {0} / 8}} (x _ {0})\right) \subset S (x _ {0}, y _ {0}, u, h _ {0}) \subset A \left(B _ {\sqrt {8 h _ {0}}} (x _ {0})\right),\tag{4.19}
$$

$$
A ^ {- 1} \left(B _ {\sqrt {h _ {0} / 8}} (y _ {0})\right) \subset \partial_ {c} u (S (x _ {0}, y _ {0}, u, h _ {0})) \subset A ^ {- 1} \left(B _ {\sqrt {8 h _ {0}}} (y _ {0})\right).
$$

Moreover

$$
\left\| u - C _ {x _ {0}, y _ {0}} - \frac {1}{2} \big | A ^ {- 1} (x - x _ {0}) \big | ^ {2} \right\| _ {C ^ {0} \Big (A \Big (B _ {\sqrt {8 h _ {0}}} (x _ {0}) \Big) \Big)} \leq \eta_ {0} h _ {0},\tag{4.20}
$$

where$C _ { x _ { 0 } y _ { 0 } }$is a c-support function for u at$x _ { 0 }$, see (2.3).

In order to prove the claim, take$h _ { 0 } \ll \bar { h }$small (to be fixed) and$\delta _ { 0 } \ll h _ { 0 }$such that$K _ { 1 } \sqrt { \omega ( \delta _ { 0 } ) } \le$ $h _ { 0 } / 2$, where$K _ { 1 }$is as in Step 2, so that

$$
Q (x _ {0}, v, h _ {0} / 2) \subset S (x _ {0}, y _ {0}, u, h _ {0}) \subset Q (x _ {0}, v, 3 h _ {0} / 2) \subset \subset B _ {1 / 6}.\tag{4.21}
$$

By (4.13) and Taylor formula we get

$$
v (x) = v (x _ {0}) + \nabla v (x _ {0}) \cdot (x - x _ {0}) + \frac {1}{2} D ^ {2} v (x _ {0}) (x - x _ {0}) \cdot (x - x _ {0}) + O (| x - x _ {0} | ^ {3}),\tag{4.22}
$$

so that defining

$$
E (x _ {0}, h _ {0}) := \left\{x: \frac {1}{2} D ^ {2} v (x _ {0}) (x - x _ {0}) \cdot (x - x _ {0}) \leq h _ {0} \right\}\tag{4.23}
$$

and using (4.13), we deduce that, for every$h _ { 0 }$universally small,

$$
E (x _ {0}, h _ {0} / 2) \subset Q (x _ {0}, v, h _ {0}) \subset E (x _ {0}, 2 h _ {0}).\tag{4.24}
$$

Moreover, always for$h _ { 0 }$small, thanks to (4.22) and the uniform convexity of v

$$
\nabla v \big (E (x _ {0}, h _ {0}) \big) \subset E ^ {*} (\nabla v (x _ {0}), 2 h _ {0}) \subset \nabla v \big (E (x _ {0}, 3 h _ {0}) \big)\tag{4.25}
$$

where we have set

$$
E ^ {*} (\bar {y}, h _ {0}) := \left\{y: \frac {1}{2} \big [ D ^ {2} v (\bar {y}) \big ] ^ {- 1} (y - \bar {y}) \cdot (y - \bar {y}) \leq h _ {0} \right\}.
$$

By Lemma 4.2, (4.24), and (4.25) applied with$3 h _ { 0 }$in place of$h _ { 0 }$, we deduce that for$\delta _ { 0 } \ll h _ { 0 } \ll \bar { h }$

$$
\partial_ {c} u \big (S (x _ {0}, y _ {0}, u, h _ {0}) \big) \subset \mathcal {N} _ {K ^ {\prime \prime} \sqrt {\omega (\delta_ {0})}} \big (\nabla v (E (x _ {0}, 3 h _ {0})) \big) \subset E ^ {*} (\nabla v (x _ {0}), 7 h _ {0}).\tag{4.26}
$$

Moreover, by (4.15), if$y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$and we set$p _ { x _ { 0 } } : = - D _ { x } c ( x _ { 0 } , y _ { 0 } )$, then

$$
| y _ {0} - \nabla v (x _ {0}) | \leq | p _ {x _ {0}} - \nabla v (x _ {0}) | + \| D _ {x} c + \mathrm{Id} \| _ {C ^ {0} (B _ {3} \times B _ {3})} \leq K ^ {\prime} \sqrt {\omega (\delta_ {0})} + \delta_ {0}.
$$

Thus, choosing$\delta _ { 0 }$suficiently small, it holds

$$
E ^ {*} (\nabla v (x _ {0}), 7 h _ {0}) \subset E ^ {*} (y _ {0}, 8 h _ {0}) \quad \forall y _ {0} \in \partial_ {c} u (x _ {0}).\tag{4.27}
$$

We now want to show that

$$
E ^ {*} (y _ {0}, h _ {0} / 8) \subset \partial_ {c} u \bigl (S (x _ {0}, y _ {0}, u, h _ {0}) \bigr) \quad \forall   y _ {0} \in \partial_ {c} u (x _ {0}).
$$

Observe that, arguing as above, we get

$$
E ^ {*} (y _ {0}, h _ {0} / 8) \subset E ^ {*} (\nabla v (x _ {0}), h _ {0} / 7) \quad \forall y _ {0} \in \partial_ {c} u (x _ {0})\tag{4.28}
$$

provided$\delta _ { 0 }$is small enough, so it is enough to prove that

$$
E ^ {*} (\nabla v (x _ {0}), h _ {0} / 7) \subset \partial_ {c} u \bigl (S (x _ {0}, y _ {0}, u, h _ {0}) \bigr).
$$

For this, let us define the c∗-convex function$u ^ { c } : B _ { 3 } \to$R and the convex function$v ^ { * } : B _ { 3 } \to$R as

$$
u ^ {c} (y) := \sup _ {x \in B _ {1 / 5}} \left\{- c (x, y) - u (x) \right\}, \quad v ^ {*} (y) := \sup _ {x \in B _ {1 / 5}} \left\{x \cdot y - v (x) \right\}
$$

(see (3.1)). Then it is immediate to check that

$$
\left| u ^ {c} - v ^ {*} \right| \leq \omega (\delta_ {0}) + \delta_ {0} \leq 2 \omega (\delta_ {0}) \quad \text { on } B _ {3}.\tag{4.29}
$$

Also, in view of (4.13),$v ^ { * }$is a uniformly convex function of class$C ^ { 3 }$on the open set$\nabla \boldsymbol { v } ( B _ { 1 / 5 } )$. In addition, since

$$
F \subset \partial_ {c} u (\partial_ {c ^ {*}} u ^ {c} (F)) \quad \text {   for   any   set   } F,\tag{4.30}
$$

thanks to (4.21) and (4.24) it is enough to show

$$
\partial_ {c ^ {*}} u ^ {c} (E ^ {*} (\nabla v (x _ {0}), h _ {0} / 7)) \subset E (x _ {0}, h _ {0} / 4).\tag{4.31}
$$

For this, we apply Lemma 4.2 to$u ^ { c }$and$v ^ { * }$to infer

$$
\partial_ {c ^ {*}} u ^ {c} (E ^ {*} (\nabla v (x _ {0}), h _ {0} / 7)) \subset \mathcal {N} _ {K ^ {\prime \prime \prime} \sqrt {\omega (\delta)}} \bigl (\nabla v ^ {*} (E ^ {*} (\nabla v (x _ {0}), h _ {0} / 7)) \bigr) \subset E (x _ {0}, h _ {0} / 4),
$$

where we used that

$$
\nabla v ^ {*} = [ \nabla v ] ^ {- 1} \quad \mathrm{and} \quad D ^ {2} v ^ {*} (\nabla v (x _ {0})) = [ D ^ {2} v (x _ {0}) ] ^ {- 1}.
$$

Thus, recalling (4.26), we have proved that there exist$h _ { 0 }$universally small, and$\delta _ { 0 }$small depending on$h _ { 0 }$, such that

$$
E ^ {*} (\nabla v (x _ {0}), h _ {0} / 7) \subset \partial_ {c} u (S (x _ {0}, y _ {0}, u, h _ {0})) \subset E ^ {*} (\nabla v (x _ {0}), 7 h _ {0}) \quad \forall x _ {0} \in B _ {1 / 7}.\tag{4.32}
$$

Using (4.21), (4.24), (4.27), and (4.28), this proves (4.19) with$A : = [ D ^ { 2 } v ( x _ { 0 } ) ] ^ { - 1 / 2 }$. Also, thanks to (4.12) and (4.13), (4.18) holds.

In order to prove the second part of the claim, we exploit (4.11), (4.9), (4.16), (4.15), (4.22), and (4.18) (recall that$C _ { x _ { 0 } , y _ { 0 } }$is defined in (2.3) and that$A = [ D ^ { 2 } v ( x _ { 0 } ) ] ^ { - 1 / 2 } )$

$$
\begin{array}{l} \left\| u - C _ {x _ {0}, y _ {0}} - \frac {1}{2} | A ^ {- 1} (x - x _ {0}) | ^ {2} \right\| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} \\ = \left\| u - C _ {x _ {0}, y _ {0}} - \frac {1}{2} D ^ {2} v (x _ {0}) (x - x _ {0}) \cdot (x - x _ {0}) \right\| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} \\ \leq 2 \| u - v \| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} + \| c (x, y _ {0}) + x \cdot y _ {0} \| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} + \| c (x _ {0}, y _ {0}) + x _ {0} \cdot y _ {0} \| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} \\ \quad + \left\| \big (y _ {0} - p _ {x _ {0}} \big) \cdot (x - x _ {0}) \right\| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} + \left\| \big (p _ {x _ {0}} - \nabla v (x _ {0}) \big) \cdot (x - x _ {0}) \right\| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} \\ \quad + \left\| v - v (x _ {0}) - \nabla v (x _ {0}) \cdot (x - x _ {0}) - \frac {1}{2} D ^ {2} v (x _ {0}) (x - x _ {0}) \cdot (x - x _ {0}) \right\| _ {C ^ {0} (E (x _ {0}, 8 h _ {0}))} \\ \leq 2 \omega (\delta_ {0}) + 3 \delta_ {0} + K ^ {\prime} \sqrt {\omega (\delta_ {0})} + K \left(K _ {2} \sqrt {8 h _ {0}}\right) ^ {3} \leq \eta_ {0} h _ {0}, \end{array}
$$

where the last inequality follows by choosing first$h _ { 0 }$suficiently small, and then$\delta _ { 0 }$much smaller than$h _ { 0 }$

Step 4: A first change of variables. Fix$x _ { 0 } \in B _ { 1 / 7 } , y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$, define$M : = - D _ { x y } c ( x _ { 0 } , y _ { 0 } )$, and consider the change of variables

$$
\left\{ \begin{array}{l} \bar {x} := x - x _ {0} \\ \bar {y} := M ^ {- 1} (y - y _ {0}). \end{array} \right.
$$

Notice that, by (4.9), it follows that

$$
\left| M - \operatorname{Id} \right| + \left| M ^ {- 1} - \operatorname{Id} \right| \leq 3 \delta_ {0}\tag{4.33}
$$

for$\delta _ { 0 }$suficiently small. We also define

$$
\begin{array}{c} \bar {c} (\bar {x}, \bar {y}) := c (x, y) - c (x, y _ {0}) - c (x _ {0}, y) + c (x _ {0}, y _ {0}), \\ \bar {u} (\bar {x}) := u (x) - u (x _ {0}) + c (x, y _ {0}) - c (x _ {0}, y _ {0}), \\ \bar {u} ^ {\bar {c}} (\bar {y}) := u ^ {c} (y) - u ^ {c} (y _ {0}) + c (x _ {0}, y) - c (x _ {0}, y _ {0}). \end{array}
$$

Then ¯u is ¯c-convex,$\bar { u } ^ { \bar { c } }$is ¯c∗-convex (where$\bar { c } ^ { * } ( \bar { y } , \bar { x } ) = \bar { c } ( \bar { x } , \bar { y } ) )$, and

$$
\bar {c} (\cdot , \mathbf {0}) = \bar {c} (\mathbf {0}, \cdot) \equiv 0, \qquad D _ {\bar {x} \bar {y}} \bar {c} (\mathbf {0}, \mathbf {0}) = - \operatorname{Id}.\tag{4.34}
$$

We also notice that

$$
\partial_ {\bar {c}} \bar {u} (\bar {x}) = M ^ {- 1} \bigl (\partial_ {c} u (\bar {x} + x _ {0}) - y _ {0} \bigr).\tag{4.35}
$$

Thus, recalling (4.19), and using (4.33) and (4.35), for$\delta _ { 0 }$suficiently small we obtain

$$
\begin{array}{l} A \left(B _ {\sqrt {h _ {0} / 9}}\right) \subset S (\mathbf {0}, \mathbf {0}, \bar {u}, h _ {0}) \subset A \left(B _ {\sqrt {9 h _ {0}}}\right), \\ A ^ {- 1} \left(B _ {\sqrt {h _ {0} / 9}}\right) \subset M ^ {- 1} A ^ {- 1} \left(B _ {\sqrt {h _ {0} / 8}}\right) \subset \partial_ {\bar {c}} \bar {u} (S (\mathbf {0}, \mathbf {0}, \bar {u}, h _ {0})) \subset M ^ {- 1} A ^ {- 1} \left(B _ {\sqrt {8 h _ {0}}}\right) \subset A ^ {- 1} \left(B _ {\sqrt {9 h _ {0}}}\right). \end{array}\tag{4.36}
$$

Since$( T _ { u } ) _ { \sharp } f = g _ { \ m }$, it follows that$T _ { \bar { u } } = \bar { \mathrm { c } } \mathrm { - e x p } ( \nabla \bar { u } )$satisfies

$$
(T _ {\bar {u}}) _ {\sharp} \bar {f} = \bar {g}, \quad \text { with } \quad \bar {f} (\bar {x}) := f (\bar {x} + x _ {0}), \quad \bar {g} (\bar {y}) := \det (M)   g (M \bar {y} + y _ {0})
$$

(see for instance the footnote in the proof of Theorem 1.3). Notice that, since$| M - \mathrm { I d } | \leq \delta _ { 0 }$(by (4.9)), we have  det$( M ) - 1 | \leq ( 1 + 2 n ) \delta _ { 0 }$(for$\delta _ { 0 }$small), so by (4.8) we get

$$
\| \bar {f} - \mathbf {1} _ {\mathcal {C} _ {1} - x _ {0}} \| _ {\infty} + \| \bar {g} - \mathbf {1} _ {M ^ {- 1} (\mathcal {C} _ {2} - y _ {0})} \| _ {\infty} \leq 2 (1 + n) \delta_ {0}.\tag{4.37}
$$

Step 5: A second change of variables and the iteration argument. We now perform a second change of variable: we set

$$
\left\{ \begin{array}{l} \tilde {x} := \frac {1}{\sqrt {h _ {0}}} A ^ {- 1} \bar {x} \\ \tilde {y} := \frac {1}{\sqrt {h _ {0}}} A \bar {y}, \end{array} \right.\tag{4.38}
$$

and define

$$
\begin{array}{c} c _ {1} (\tilde {x}, \tilde {y}) := \frac {1}{h _ {0}} \bar {c} \big (\sqrt {h _ {0}} A \tilde {x}, \sqrt {h _ {0}} A ^ {- 1} \tilde {y} \big), \\ u _ {1} (\tilde {x}) := \frac {1}{h _ {0}} \bar {u} (\sqrt {h _ {0}} A \tilde {x}), \\ u _ {1} ^ {c _ {1}} (\tilde {y}) := \frac {1}{h _ {0}} \bar {u} ^ {\bar {c}} (\sqrt {h _ {0}} A ^ {- 1} \tilde {y}). \end{array}
$$

We also define

$$
f _ {1} (\tilde {x}) := \bar {f} (\sqrt {h _ {0}} A \tilde {x}), \quad g _ {1} (\tilde {y}) := \bar {g} (\sqrt {h _ {0}} A ^ {- 1} \tilde {y}).
$$

Since$\operatorname* { d e t } ( A ) = 1$(see (4.18)), it is easy to check that$( T _ { u _ { 1 } } ) _ { \sharp } f _ { 1 } = g _ { 1 }$(see the footnote in the proof of Theorem 1.3). Also, since$\left( \| A \| + \| A ^ { - 1 } \| \right) \sqrt { h _ { 0 } } \ll 1$, it follows from (4.37) that

$$
\left| f _ {1} - 1 \right| + \left| g _ {1} - 1 \right| \leq 2 (1 + n) \delta_ {0} \quad \text { inside } B _ {3}.\tag{4.39}
$$

Moreover, defining

$$
\mathcal {C} _ {1} ^ {(1)} := S (\mathbf {0}, \mathbf {0}, u _ {1}, 1), \qquad \mathcal {C} _ {2} ^ {(1)} := \partial_ {c _ {1}} u _ {1} (S (\mathbf {0}, \mathbf {0}, u _ {1}, 1)),
$$

both$\mathcal { C } _ { 1 } ^ { ( 1 ) }$and$\mathcal { C } _ { 2 } ^ { ( 1 ) }$are closed, and thanks to (4.36)

$$
B _ {1 / 3} \subset \mathcal {C} _ {1} ^ {(1)}, \mathcal {C} _ {2} ^ {(1)} \subset B _ {3}.\tag{4.40}
$$

Also, since$( T _ { u _ { 1 } } ) _ { \sharp } f _ { 1 } = g _ { 1 }$, arguing as in the proof of Theorem 1.3 we get

$$
(T _ {u _ {1}}) _ {\sharp} \big (f _ {1} \mathbf {1} _ {\mathcal {C} _ {1} ^ {(1)}} \big) = \big (g _ {1} \mathbf {1} _ {\mathcal {C} _ {2} ^ {(1)}} \big),
$$

and by (4.39)

$$
\| f _ {1} \mathbf {1} _ {\mathcal {C} _ {1} ^ {(1)}} - \mathbf {1} _ {\mathcal {C} _ {1} ^ {(1)}} \| _ {\infty} + \| g _ {1} \mathbf {1} _ {\mathcal {C} _ {2} ^ {(1)}} - \mathbf {1} _ {\mathcal {C} _ {2} ^ {(1)}} \| _ {\infty} \leq 2 (1 + n) \delta_ {0}.
$$

Finally, using (4.34), (4.9), and (4.20), it is easy to check that

$$
\| c _ {1} (\tilde {x}, \tilde {y}) + \tilde {x} \cdot \tilde {y} \| _ {C ^ {2, \alpha} (B _ {3} \times B _ {3})} \leq \delta_ {0}, \quad \left\| u _ {1} - \frac {1}{2} | \tilde {x} | ^ {2} \right\| _ {C ^ {0} (B _ {3})} \leq \eta_ {0}
$$

provided$h _ { 0 }$is small enough. Indeed, the second inequality is just a direct consequence of (4.20), while (4.34) and a Taylor expansion yield

$$
c _ {1} (\tilde {x}, \tilde {y}) = \frac {1}{h _ {0}} \bar {c} \big (\sqrt {h _ {0}} A \tilde {x}, \sqrt {h _ {0}} A ^ {- 1} \tilde {y} \big) = \tilde {x} \cdot \tilde {y} + O (\delta_ {0} K _ {2} ^ {2} (K _ {2} \sqrt {h _ {0}}) ^ {\alpha}).
$$

so we can choose$h _ { 0 }$small enough to ensure that

$$
O (\delta_ {0} K _ {2} ^ {2} (K _ {2} \sqrt {h _ {0}}) ^ {\alpha}) \leq \delta_ {0}.\tag{4.41}
$$

This shows that$u _ { 1 }$satisfies the same assumptions as u with$\delta _ { 0 }$replaced by$2 ( 1 + n ) \delta _ { 0 }$. Hence, up to take$\delta _ { 0 }$slightly smaller, we can apply Step 3 to$u _ { 1 }$, and we find a symmetric matrix$A _ { 1 }$satisfying

$$
\operatorname{Id} / K _ {2} \leq A _ {1} \leq K _ {2} \operatorname{Id}, \quad \det (A _ {1}) = 1,
$$

$$
A _ {1} \left(B _ {\sqrt {h _ {0} / 8}}\right) \subset S (\mathbf {0}, \mathbf {0}, u _ {1}, h _ {0}) \subset A _ {1} \left(B _ {\sqrt {8 h _ {0}}}\right),
$$

$$
A _ {1} ^ {- 1} \left(B _ {\sqrt {h _ {0} / 8}}\right) \subset \partial_ {c _ {1}} u _ {1} (S (\mathbf {0}, \mathbf {0}, u _ {1}, h _ {0})) \subset A _ {1} ^ {- 1} \left(B _ {\sqrt {8 h _ {0}}}\right),
$$

$$
\left\| u _ {1} - \frac {1}{2} \big | A _ {1} ^ {- 1} \tilde {x} \big | ^ {2} \right\| _ {C ^ {0} (A _ {1} (B (0, \sqrt {8 h _ {0}}))} \leq \eta_ {0} h _ {0}.
$$

(Here$K _ { 2 }$and$h _ { 0 }$are as in Step 3.)

This allows us to apply to$u _ { 1 }$the very same construction as the one used above to define$u _ { 1 }$from u¯: we set

$$
c _ {2} (\tilde {x}, \tilde {y}) := \frac {1}{h _ {0}} c _ {1} \big (\sqrt {h _ {0}} A _ {1} \tilde {x}, \sqrt {h _ {0}} A _ {1} ^ {- 1} \tilde {y} \big), \qquad u _ {2} (\tilde {x}) := \frac {1}{h _ {0}} u _ {1} (\sqrt {h _ {0}} A _ {1} \tilde {x}),
$$

so that$( T _ { u _ { 2 } } ) _ { \sharp } f _ { 2 } = g _ { 2 }$with

$$
f _ {2} (\tilde {x}) := f _ {1} \left(\sqrt {h _ {0}} A _ {1} \tilde {x}\right), \quad g _ {2} (\tilde {y}) := \bar {g} \left(\sqrt {h _ {0}} A _ {1} ^ {- 1} \tilde {y}\right).
$$

Arguing as before, it is easy to check that$u _ { 2 } , c _ { 2 } , f _ { 2 } , g _ { 2 }$satisfy the same assumptions as$u _ { 1 } , c _ { 1 } , f _ { 1 } , g _ { 1 }$ with exactly the same constants, provided$h _ { 0 } \ll 1$satisfies (4.41).

So we can keep iterating this construction, defining for any$k \in \mathbb N$

$$
c _ {k + 1} (\tilde {x}, \tilde {y}) := \frac {1}{h _ {0}} c _ {k} \big (\sqrt {h _ {0}} A _ {k} \tilde {x}, \sqrt {h _ {0}} A _ {k} ^ {- 1} \tilde {y} \big), \qquad u _ {k + 1} (\tilde {x}) := \frac {1}{h _ {0}} u _ {k} (\sqrt {h _ {0}} A _ {k} \tilde {x}),
$$

where$A _ { k }$is the matrix constructed in the k-th iteration. In this way, if we set

$$
M _ {k} := A _ {k} \cdot \dots \cdot A _ {1}, \quad \forall k \geq 1,
$$

we obtain a sequence of symmetric matrices satisfying

$$
\mathrm{Id} / K _ {2} ^ {k} \leq M _ {k} \leq K _ {2} ^ {k} \mathrm{Id}, \quad \det (M _ {k}) = 1,\tag{4.42}
$$

and such that

$$
M _ {k} \left(B _ {(h _ {0} / 8) ^ {k / 2}}\right) \subset S (\mathbf {0}, \mathbf {0}, u _ {k}, h _ {0} ^ {k}) \subset M _ {k} \left(B _ {(8 h _ {0}) ^ {k / 2}}\right).\tag{4.43}
$$

Step$6 \colon C ^ { 1 , \beta }$regularity. We now show that, for any$\beta \in ( 0 , 1 )$, we can choose$h _ { 0 }$and$\delta _ { 0 } = \delta _ { 0 } ( h _ { 0 } )$ small enough so that$u _ { 1 }$is$C ^ { 1 , \beta }$at the origin (here$u _ { 1 }$is the function constructed in the previous step). This will imply that u is$C ^ { 1 , \beta }$at$x _ { 0 }$with universal bounds, which by the arbitrariness of $x _ { 0 } \in B _ { 1 / 7 }$gives$u \in C ^ { 1 , \beta } ( B _ { 1 / 7 } )$

Fix$\beta \in ( 0 , 1 )$. Then by (4.42) and (4.43) we get

$$
B _ {\left(\sqrt {h _ {0}} / (\sqrt {8} K _ {2})\right) ^ {k}} \subset S (\mathbf {0}, \mathbf {0}, u _ {1}, h _ {0} ^ {k}) \subset B _ {\left(K _ {2} \sqrt {8 h _ {0}}\right) ^ {k}},\tag{4.44}
$$

so defining$r _ { 0 } : = \sqrt { h _ { 0 } } / ( \sqrt { 8 } K _ { 2 } )$we obtain

$$
\left\| u _ {1} \right\| _ {C ^ {0} (B _ {r _ {0} ^ {k}})} \leq h _ {0} ^ {k} = \left(\sqrt {8} K _ {2} r _ {0}\right) ^ {2 k} \leq r _ {0} ^ {(1 + \beta) k},
$$

provided$h _ { 0 }$(and so$r _ { 0 } )$is suficiently small. This implies the$C ^ { 1 , \beta }$regularity of$u _ { 1 }$at$\mathbf { 0 } { \cdot }$concluding the proof.

Remark 4.4 (Local to global principle). If u is diferentiable at x and c satisfies$( { \bf C 0 } ) – ( { \bf C 1 } )$, then every “local support” at x is also a “global c-support” at$x ,$that is,$\partial _ { c } u ( x ) = \mathrm { c } \mathrm { - } \mathrm { e x p } _ { x } ( \partial ^ { - } u ( x ) )$. To see this, just notice that

$$
\emptyset \neq \partial_ {c} u (x) \subset \mathrm{c-exp} _ {x} (\partial^ {-} u (x)) = \{\mathrm{c-exp} _ {x} (\nabla u (x)) \}
$$

(recall (2.6)), so necessarily the two sets have to coincide.

Corollary 4.5. Let u be as in Theorem$4 { \cdot } 9 .$Then u is strictly c-convex in$B _ { 1 / 7 }$. More precisely, for every$\gamma > 2$there exist$\eta _ { 0 } , \delta _ { 0 } > 0$depending only on γ such that, if the hypotheses of Theorem $4 . 3$are satisfied, then, for all$x _ { 0 } \in B _ { 1 / 7 } , y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$, and$C _ { x _ { 0 } , y _ { 0 } }$as in (2.3), we have

$$
\inf _ {\partial B _ {r} (x _ {0})} \left\{u - C _ {x _ {0}, y _ {0}} \right\} \geq c _ {0} r ^ {\gamma} \quad \forall r \leq \operatorname{dist} (x _ {0}, \partial B _ {1 / 7}),\tag{4.45}
$$

with$c _ { 0 } > 0$universal.

Proof. With the same notation as in the proof of Theorem 4.3, it is enough to show that

$$
\inf _ {\partial B _ {r}} u _ {1} \geq r ^ {1 / \beta},
$$

where$u _ { 1 }$is the function constructed in Step 5 of the proof of Theorem 4.3. Defining$\varrho _ { 0 } : = K _ { 2 } \sqrt { 8 h _ { 0 } }$2 it follows from (4.44) that

$$
\inf _ {\partial B _ {\varrho_ {0} ^ {k}}} u _ {1} \geq h _ {0} ^ {k} = \left(\varrho_ {0} / (\sqrt {8} K _ {2})\right) ^ {2 k} \geq \varrho_ {0} ^ {\gamma^ {k}},
$$

provided$h _ { 0 }$is small enough.

A simple consequence of the above results is the following:

Corollary 4.6. Let u be as in Theorem 4.3, then$T _ { u } ( B _ { 1 / 7 } )$is open.

Proof. Since$u \in C ^ { 1 , \beta } ( B _ { 1 / 7 } )$we have that$T _ { u } ( B _ { 1 / 7 } ) = \partial _ { c } u ( B _ { 1 / 7 } )$(see Remark 4.4). We claim that it is enough to show that if$y _ { 0 } \in \partial _ { c } u ( B _ { 1 / 7 } )$, then there exists$\varepsilon = \varepsilon ( y _ { 0 } ) > 0$small such that, for all $\left| y - y _ { 0 } \right| < \varepsilon$, the function$u ( \cdot ) + c ( \cdot , y )$has a local minimum at some point$\bar { x } \in B _ { 1 / 7 }$. Indeed, if this is the case, then

$$
\nabla u (\bar {x}) = - D _ {x} c (\bar {x}, y),
$$

and so$y \in \partial _ { c } u ( \bar { x } )$(by Remark 4.4), hence$B _ { \varepsilon } ( y _ { 0 } ) \subset T _ { u } ( B _ { 1 / 7 } )$

To prove the above fact, fix$r > 0$such that$B _ { r } ( x _ { 0 } ) \subset B _ { 1 / 7 }$, and pick$\bar { x } \mathrm { ~ a ~ }$point in$\overline { { B } } _ { r } ( x _ { 0 } )$where the function$u ( \cdot ) + c ( \cdot , y )$attains its minimum, i.e.,

$$
\bar {x} \in \underset {\overline {{B}} _ {r} (x _ {0})} {\operatorname{argmin}} \left\{u (x) + c (x, y) \right\}.
$$

Since, by (4.45),

$$
\begin{array}{c} \min _ {x \in \partial B _ {r} (x _ {0})} \bigl \{u (x) + c (x, y) \bigr \} \geq \min _ {x \in \partial B _ {r} (x _ {0})} \bigl \{u (x) + c (x, y _ {0}) \bigr \} - \varepsilon \| c \| _ {C ^ {1}} \\ \geq u (x _ {0}) + c (x _ {0}, y _ {0}) + c _ {0} r ^ {\gamma} - \varepsilon \| c \| _ {C ^ {1}}, \end{array}
$$

while

$$
u (x _ {0}) + c (x _ {0}, y) \leq c (x _ {0}, y _ {0}) + u (x _ {0}) + \varepsilon \| c \| _ {C ^ {1}},
$$

choosing$\begin{array} { r } { \varepsilon < \frac { c _ { 0 } } { 2 \left\| c \right\| _ { C ^ { 1 } } } r ^ { \gamma } } \end{array}$we obtain that$\bar { x } \in B _ { r } ( x _ { 0 } ) \subset B _ { 1 / 7 }$. This implies that ¯x is a local minimum for$u ( \cdot ) + c ( \cdot , y )$, concluding the proof.

## 5. Comparison principle and$C ^ { 2 , \alpha }$regularity

We begin this section with a change of variable formula for the c-exponential map.

Lemma 5.1. Let Ω be an open set,$v \in C ^ { 2 } ( \Omega )$, and assume that$\nabla \boldsymbol { v } ( \Omega ) \subset$Dom c-exp and that

$$
D ^ {2} v (x) + D _ {x x} c \big (x, \mathrm{c} - \exp_ {x} (\nabla v (x)) \big) \geq 0 \quad \forall x \in \Omega .
$$

Then, for every Borel set$A \subset \Omega$2

$$
| \text { c - exp } (\nabla v (A)) | \leq \int_ {A} \frac {\det \left(D ^ {2} v (x) + D _ {x x} c (x , \text { c - exp } _ {x} (\nabla v (x)))\right)}{| \det \left(D _ {x y} c (x , \text { c - exp } _ {x} (\nabla v (x)))\right) |} d x.
$$

In addition, if the map$x \mapsto \mathrm { c } { - } \mathrm { e x p } _ { x } ( \nabla v ( x ) )$is injective, then equality holds.

Proof. The result follows from a direct application of the Area Formula [12, Section 3.3.2, Theorem 1] once one notices that, diferentiating the identity

$$
\nabla v (x) = - D _ {x} c \bigl (x, \mathrm{c-exp} _ {x} (\nabla v (x)) \bigr)
$$

(see (2.5)), the Jacobian determinant of the$C ^ { 1 }$map$x \mapsto \mathrm { c } { - } \mathrm { e x p } _ { x } ( \nabla v ( x ) )$is given precisely by

$$
\frac {\det \big (D ^ {2} v (x) + D _ {x x} c \big (x , \mathrm{c} - \exp_ {x} (\nabla v (x)) \big) \big)}{\big | \det \big (D _ {x y} c \big (x , \mathrm{c} - \exp_ {x} (\nabla v (x)) \big) \big) \big |}.
$$

In the next proposition we show a comparison principle between$C ^ { 1 }$c-convex functions and smooth solutions to the Monge-Amp\`ere equation. <sup>4</sup> As already mentioned at the beginning of Section 4 (see also Remark 4.4), the$C ^ { 1 }$regularity of u is crucial to ensure that the c-subdiferential coincides with its local counterpart$\mathrm { c - e x p } ( \partial ^ { - } u )$

Here and in the sequel, we use co[E] to denote the convex hull of a set E. Also, recall that$\mathcal { N } _ { r } ( E )$ denotes the r-neighborhood of E.

Proposition 5.2 (Comparison principle). Let u be a c-convex function of class$C ^ { 1 }$inside the set $S : = \{ u < 1 \}$, and assume that$u ( \mathbf { 0 } ) = 0 , B _ { 1 / K } \subset S \subset B _ { K }$, and that$\nabla u ( S ) \subset C$Dom c-exp. Let $f , g$be two densities such that

$$
\| f / \lambda_ {1} - 1 \| _ {C ^ {0} (S)} + \| g / \lambda_ {2} - 1 \| _ {C ^ {0} (T _ {u} (S))} \leq \varepsilon\tag{5.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">c(x, y) = |x − y|p</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>R</sub><sup>n</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4A</sup> <sup>similar</sup> <sup>result</sup> <sup>for</sup> <sup>the</sup> <sup>case</sup> <sup>c(x,</sup> <sup>y)</sup> <sup>=</sup> |<sup>x</sup> − <sup>y</sup>|<sup>p appeared</sup> <sup>in</sup> <sup>[7,</sup> <sup>Theorem</sup> <sup>6.2].</sup> <sup>Here,</sup> <sup>however,</sup> <sup>we</sup> <sup>have</sup> <sup>to</sup> <sup>deal</sup> <sup>with</sup> some additional dificulties due to the fact that the c-exponential map is not necessarily defined on the whole .</span></small>

for some constants$\lambda _ { 1 } , \lambda _ { 2 } \in ( 1 / 2 , 2 )$and$\varepsilon \in ( 0 , 1 / 4 )$, and assume that$( T _ { u } ) _ { \sharp } f = g$. Furthermore, suppose that

$$
\left\| c + x \cdot y \right\| _ {C ^ {2} (B _ {K} \times B _ {K})} \leq \delta .\tag{5.2}
$$

Then there exist a universal constant$\gamma \in ( 0 , 1 )$, and$\delta _ { 1 } = \delta _ { 1 } ( K ) > 0$small, such that the following holds: Let v be the solution of

$$
\left\{ \begin{array}{l l} \det (D ^ {2} v) = \lambda_ {1} / \lambda_ {2} & \quad i n   \mathcal {N} _ {\delta^ {\gamma}} (\operatorname{co} [ S ]), \\ v = 1 & \quad o n   \partial \big (\mathcal {N} _ {\delta^ {\gamma}} (\operatorname{co} [ S ]) \big). \end{array} \right.
$$

Then

$$
\| u - v \| _ {C ^ {0} (S)} \leq C _ {K} \left(\varepsilon + \delta^ {\gamma / n}\right) \quad \text {   provided   } \delta \leq \delta_ {1},\tag{5.3}
$$

where$C _ { K }$is a constant independent of$\lambda _ { 1 } , \lambda _ { 2 } , \varepsilon ,$and δ (but which depends on K).

Proof. First of all we observe that, since$u ( { \bf 0 } ) = 0 , u = 1$on$\partial S , S \subset B _ { K }$, and$\| c + x \cdot y \| _ { C ^ { 2 } ( B _ { K } ) } \leq$ $\delta \ll 1$, it is easy to check that there exists a universal constant$a _ { 1 } > 0$such that

$$
\left| D _ {x} c (x, y) \right| \geq a _ {1} \quad \forall x \in \partial S, y = \mathrm{c} - \exp_ {x} (\nabla u (x)).\tag{5.4}
$$

Thanks to (5.4) and (5.2), it follows from the Implicit Function Theorem that, for each$x \in \partial S$2 the boundary of the set

$$
E _ {x} := \left\{z \in B _ {K}: c (z, y) - c (x, y) + u (x) \leq 1 \right\}
$$

is of class$C ^ { 2 }$inside$B _ { K }$, and its second fundamental form is bounded by$C _ { K } \delta$, where$C _ { K } > 0$ depends only on K. Hence, since S can be written as

$$
S := \bigcap_ {x \in \partial S} E _ {x},
$$

it follows that

$$
S \text {   is   a   } (C _ {K} \delta) \text {-semiconvex   set, }
$$

that is, for any couple of points$x _ { 0 } , x _ { 1 } \in S$the ball centered at$x _ { 1 / 2 } : = ( x _ { 0 } + x _ { 1 } ) / 2$of radius $C _ { K } \delta | x _ { 1 } - x _ { 0 } | ^ { 2 }$intersects S. Since$S \subset B _ { K }$, this implies that co$[ S ] \subset { \mathcal { N } } _ { C _ { K } ^ { \prime } \delta } ( S )$for some positive constant$C _ { K } ^ { \prime }$depending only on K. Thus, for any$\gamma \in ( 0 , 1 )$we obtain

$$
\mathcal {N} _ {\delta^ {\gamma}} (\mathrm{co} [ S ]) \subset \mathcal {N} _ {(1 + C _ {K} ^ {\prime}) \delta^ {\gamma}} (S).
$$

Since$v = 1$on$\partial ( \mathcal { N } _ { \delta ^ { \gamma } } ( \cos [ S ] ) )$and$\lambda _ { 1 } / \lambda _ { 2 } \in ( 1 / 4 , 4 )$, by standard interior estimates for solution of   the Monge-Amp\`ere equation with constant right hand side (see for instance [8, Lemma 1.1]), we obtain

(5.5)

$$
\mathrm{osc} _ {S} v \leq C _ {K} ^ {\prime \prime}\tag{5.6}
$$

$$
1 - C _ {K} ^ {\prime \prime} \delta^ {\gamma / n} \leq v <   1 \quad \text { on } \partial S,\tag{5.7}
$$

$$
D ^ {2} v \geq \delta^ {\gamma / \tau} \operatorname{Id} / C _ {K} ^ {\prime \prime} \quad \text {   in   } \operatorname{co} [ S ],
$$

for some$\tau > 0$universal, and some constant$C _ { K } ^ { \prime \prime }$depending only on$K$.

Let us define

$$
v ^ {+} := (1 + 4 \varepsilon + 2 \sqrt {\delta}) v - 4 \varepsilon - 2 \sqrt {\delta}, \quad v ^ {-} := (1 - 4 \varepsilon - \sqrt {\delta} / 2) v + 4 \varepsilon + \sqrt {\delta} / 2 + 2 C _ {K} ^ {\prime \prime} \delta^ {\gamma / n}.
$$

Our goal is to show that we can choose$\gamma$universally small so that$v ^ { - } \geq u \geq v ^ { + }$on$S _ { ☉ }$. Indeed, if we can do so, then by (5.5) this will imply (5.3), concluding the proof.

First of all notice that, thanks to (5.6),$v ^ { - } > u > v ^ { + }$on ∂S. Let us show first that$v ^ { + } \leq v$ Assume by contradiction this is not the case. Then, since$u > v ^ { + }$on ∂S,

$$
\emptyset \neq Z := \left\{u <   v ^ {+} \right\} \subset \subset S.
$$

Since$v ^ { + }$is convex, taking any supporting plane to$v ^ { + }$at$x \in Z$, moving it down and then lifting it up until it touches u from below, we deduce that

$$
\nabla v ^ {+} (Z) \subset \nabla u (Z)\tag{5.8}
$$

(recall that both u and$v ^ { + }$are of class$C ^ { 1 } )$, thus by Remark 4.4

$$
| \mathrm{c} - \exp (\nabla v ^ {+} (Z)) | \leq | T _ {u} (Z) |.\tag{5.9}
$$

We show that this is impossible. For this, using (5.7) and choosing$\gamma : = \tau / 4$, for any$x \in Z$we compute

$$
\begin{array}{r l} & D ^ {2} v ^ {+} (x) + D _ {x x} c \big (x, \mathrm{c} - \exp_ {x} (\nabla v ^ {+} (x)) \big) \geq (1 + \sqrt {\delta} + 4 \varepsilon) D ^ {2} v + \sqrt {\delta} D ^ {2} v - \delta \operatorname{Id} \\ & \qquad \qquad \qquad \qquad \qquad \qquad \geq (1 + \sqrt {\delta} + 4 \varepsilon) D ^ {2} v + (\delta^ {3 / 4} / C _ {K} ^ {\prime \prime} - \delta) \operatorname{Id} \\ & \qquad \qquad \qquad \qquad \qquad \geq (1 + \sqrt {\delta} + 4 \varepsilon) D ^ {2} v, \end{array}
$$

provided$\delta$is suficiently small, the smallness depending only on K. Thus, thanks (5.2) we have

$$
\begin{array}{r l} \frac {\det \big (D ^ {2} v ^ {+} (x) + D _ {x x} c (x , \mathrm{c-exp} _ {x} (\nabla v ^ {+} (x))) \big)}{\big | \det \big (D _ {x y} c \big (x , \mathrm{c-exp} _ {x} (\nabla v ^ {+} (x)) \big) \big) \big |} & \geq \frac {\det \big ((1 + \sqrt {\delta} + 4 \varepsilon) D ^ {2} v \big)}{1 + \delta} \\ & \geq (1 + \sqrt {\delta} + 4 \varepsilon) ^ {n} (1 - 2 \delta) \frac {\lambda_ {1}}{\lambda_ {2}} \\ & \geq (1 + 4 n \varepsilon) \frac {\lambda_ {1}}{\lambda_ {2}}. \end{array}
$$

In addition, thanks (5.7) and (5.2), since$\delta ^ { \gamma / \tau } = \delta ^ { 1 / 4 } \gg \delta$we see that

$$
D ^ {2} v ^ {+} > \| D _ {x x} c \| _ {C ^ {0} (B _ {K} \times B _ {K})} \operatorname{Id} \quad \text { inside   co } [ S ].
$$

Hence, for any$x , z \in Z , x \neq z$and$y = \mathrm { c } { - } \mathrm { e x p } _ { x } ( \nabla v ^ { + } ( x ) )$(notice that$\mathrm { c - e x p } _ { x } ( \nabla v ^ { + } ( x ) )$is well-defined because of (5.8) and the assumption$\nabla u ( S ) \subset C$Dom c-exp), it follows

$$
\begin{array}{l} v ^ {+} (z) + c (z, y) \geq v ^ {+} (x) + c (x, y) \\ \qquad \qquad \qquad + \frac {1}{2} \int_ {0} ^ {1} \Big (D ^ {2} v ^ {+} \big (t z + (1 - t) x \big) + D _ {x x} c \big (t z + (1 - t) x, y \big) \Big) [ z - x, z - x ]   d t \\ \qquad > v ^ {+} (x) + c (x, y), \end{array}
$$

where we used that$\nabla v ^ { + } ( x ) + D _ { x } c ( x , y ) = 0$. This means that the supporting function$z \mapsto$ $- c ( z , y ) + c ( x , y ) + v ^ { + } ( x )$can only touch$v ^ { + }$from below at$x ,$which implies that the map$Z \ni x \mapsto$ $\mathrm { c - e x p } _ { x } ( \nabla v ^ { + } ( x ) )$is injective. Thus, by Lemma 5.1 we get

$$
| \mathrm{c} - \exp (\nabla v ^ {+} (Z)) | \geq (1 + 4 n \varepsilon) \frac {\lambda_ {1}}{\lambda_ {2}} | Z |.\tag{5.10}
$$

On the other hand, since u is$C ^ { 1 }$, it follows from$( T _ { u } ) _ { \sharp } f = g$and (5.1) that

$$
| T _ {u} (Z) | = \int_ {Z} \frac {f (x)}{g (T _ {u} (x))} d x \leq \frac {\lambda_ {1} (1 + \varepsilon)}{\lambda_ {2} (1 - \varepsilon)} | Z | \leq (1 + 3 \varepsilon) \frac {\lambda_ {1}}{\lambda_ {2}} | Z |.
$$

This estimate combined with (5.10) shows that (5.9) is impossible unless Z is empty. This proves that$v ^ { + } \leq u$

The proof of the inequality$v ^ { - } \leq u$follows by the same argument except for a minor modification. More precisely, let us assume by contradiction that$W : = \{ u > v ^ { - } \}$is nonempty. In order to apply the previous argument we would need to know that$\nabla v ^ { - } ( W ) \subset \operatorname { D o m } \operatorname { c - e x p }$. However, since the gradient of v can be very large near ∂S, this may be a problem.

To circumvent this issue we argue as follows: since W is nonempty, there exists a positive constant$\bar { \mu }$such that u touches$v ^ { - } + \bar { \mu }$from below inside S. Let E be the contact set, i.e., $E : = \{ u = v ^ { - } + \bar { \mu } \}$. Since both u and$v ^ { - }$are$C ^ { 1 } , \nabla u = \nabla v ^ { - }$on E. Thus, if$\eta > 0$is small enough, then the set$W _ { \eta } : = \{ u > v ^ { - } + \bar { \mu } - \eta \}$is nonempty and v−$( W _ { \eta } )$is contained in a small neighborhood of$\nabla u ( W _ { \eta } )$, which is compactly contained in Dom c-exp. At this point, one argues exactly as in the first part of the proof, with$W _ { \eta }$in place of$Z ,$to find a contradiction.

Theorem 5.3. Let$u , f , g , \eta _ { 0 } , \delta _ { 0 }$be as in Theorem$4 . 3 ,$and assume in addition that$c \in C ^ { k , \alpha } ( B _ { 3 } \times$ $B _ { 3 } )$and$f , g \in C ^ { k , \alpha } ( B _ { 1 / 3 } )$for some$k \geq 0$and$\alpha \in ( 0 , 1 )$. There exist small constants$\eta _ { 1 } \leq \eta _ { 0 }$and $\delta _ { 1 } \leq \delta _ { 0 }$such that, if

(5.11)

$$
\| f - \mathbf {1} _ {\mathcal {C} _ {1}} \| _ {\infty} + \| g - \mathbf {1} _ {\mathcal {C} _ {2}} \| _ {\infty} \leq \delta_ {1},\tag{5.12}
$$

$$
\left\| c (x, y) + x \cdot y \right\| _ {C ^ {2, \alpha} \left(B _ {3} \times B _ {3}\right)} \leq \delta_ {1},
$$

and

$$
\left\| u - \frac {1}{2} | x | ^ {2} \right\| _ {C ^ {0} (B _ {3})} \leq \eta_ {1},\tag{5.13}
$$

then$u \in C ^ { k + 2 , \alpha } ( B _ { 1 / 9 } )$

Proof. We divide the proof in two steps.

• <sup>Step</sup>$1 \colon { \cal C } ^ { 1 , 1 }$regularity. Fix a point$x _ { 0 } \in B _ { 1 / 8 }$, and set$y _ { 0 } : = \mathrm { c } \mathrm { - e x p } _ { x _ { 0 } } ( \nabla u ( x _ { 0 } ) )$. Up to replace u (resp. c) with the function u<sub>1</sub> (resp. c<sub>1</sub>) constructed in Steps 4 and 5 in the proof of Theorem 4.3, we can assume that$u \geq 0 , u ( \mathbf { 0 } ) = 0$, that

$$
S _ {h} := S (\mathbf {0}, \mathbf {0}, u, h) = \{u \leq h \},
$$

and that

$$
D _ {x y} c (\mathbf {0}, \mathbf {0}) = - \operatorname{Id}.\tag{5.14}
$$

Under these assumptions we will show that the sections of u are of “good shape”, i.e.,

$$
B _ {\sqrt {h} / K} \subset S _ {h} \subset B _ {K \sqrt {h}} \quad \forall h \leq h _ {1},\tag{5.15}
$$

for some universal$h _ { 1 }$and K. Arguing as in Step 6 of Theorem 4.3, this will give that u is$C ^ { 1 , 1 }$at the origin, and thus at every point in$B _ { 1 / 8 }$

First of all notice that, thanks to (5.13), for any$h _ { 1 } > 0$we can choose$\eta _ { 1 } = \eta _ { 1 } ( h _ { 1 } ) > 0$small enough such that (5.15) holds for$S _ { h _ { 1 } }$with$K = 2$. Hence, assuming without loss of generality that $\delta _ { 1 } \leq 1$, we see that

$$
B _ {\sqrt {h _ {1}} / 3} \subset \mathcal {N} _ {\delta_ {1} ^ {\gamma} \sqrt {h _ {1}}} (\mathrm{co} [ S _ {h _ {1}} ]) \subset B _ {3 \sqrt {h _ {1}}},
$$

$$
\left\{ \begin{array}{l l} \det (D ^ {2} v _ {1}) = f (\mathbf {0}) / g (\mathbf {0}) & \text { in } \mathcal {N} _ {\delta_ {1} ^ {\gamma} \sqrt {h _ {1}}} (\text { co } [ S _ {h _ {1}} ]), \\ v _ {1} = h _ {1} & \text { on } \partial \mathcal {N} _ {\delta_ {1} ^ {\gamma} \sqrt {h _ {1}}} (\text { co } [ S _ {h _ {1}} ]). \end{array} \right.
$$

where$\gamma$is the exponent from Proposition 5.2. Let$v _ { 1 }$solve the Monge-Amp\`ere equation

Since$B _ { 1 / 3 } \subset N _ { \delta _ { 1 } ^ { \gamma } \sqrt { h _ { 1 } } } ( \cos [ S _ { h _ { 1 } } ] ) / \sqrt { h _ { 1 } } \subset B _ { 3 }$, by standard Pogorelov estimates applied to the function $v _ { 1 } ( \sqrt { h _ { 1 } } x ) / h _ { 1 }$(see for instance [26, Theorem 4.2.1]), it follows that$| D ^ { 2 } v _ { 1 } ( 0 ) | \le M$, with$M > 0$ some large universal constant.

Let$h _ { k } : = h _ { 1 } 2 ^ { - k }$and define$\bar { K } \ge 3$to be the largest number such that any solution w of

$$
\left\{ \begin{array}{l l} \det (D ^ {2} w) = f (\mathbf {0}) / g (\mathbf {0}) & \text { in } Z, \\ w = 1 & \text { on } \partial Z, \end{array} \right. \quad \text { with } \quad B _ {1 / \bar {K}} \subset Z \subset B _ {\bar {K}},\tag{5.16}
$$

satisfies$| D ^ { 2 } w ( 0 ) | \le M + 1 . { \ 5 }$We prove by induction that (5.15) holds with$K = \bar { K }$

If$h = h _ { 1 }$then we already know that (5.15) holds with$K = 2$(and so with$K = { \bar { K } } )$

Assume now that (5.15) holds with$h = h _ { k }$and$K = \bar { K }$, and we want to show that it holds with $h = h _ { k + 1 }$. For this, for any$k \in \mathbb N$we consider$u _ { k }$the solution of

$$
\left\{ \begin{array}{l l} \det (D ^ {2} v _ {k}) = f (\mathbf {0}) / g (\mathbf {0}) & \text {in} \mathcal {N} _ {\delta_ {k} ^ {\gamma} \sqrt {h _ {k}}} (\text {co} [ S _ {h _ {k}} ]), \\ v _ {k} = h _ {1} 2 ^ {- k} & \text {on} \partial N _ {\delta_ {k} ^ {\gamma} \sqrt {h _ {k}}} (\text {co} [ S _ {h _ {k}} ]), \end{array} \right.
$$

where

$$
\delta_ {k} := \| c (x, y) + x \cdot y \| _ {C ^ {2} (S _ {h _ {k}} \times T _ {u} (S _ {h _ {k}}))} \leq \delta_ {1}.
$$

Let us consider the rescaled functions

$$
\bar {u} _ {k} (x) := u \big (\sqrt {h _ {k}} x \big) / h _ {k}, \quad \bar {v} _ {k} (x) := v _ {k} \big (\sqrt {h _ {k}} x \big) / h _ {k}.
$$

Since by the inductive hypothesis$B _ { 1 / \bar { K } } \subset \bar { S } _ { k } : = \{ \bar { u } _ { k } \leq 1 \} \subset B _ { \bar { K } }$, we can apply Proposition 5.2 to deduce that

$$
\| \bar {u} _ {k} - \bar {v} _ {k} \| _ {C ^ {0} (\bar {S} _ {k})} \leq C _ {\bar {K}} \Bigl (\underset {S _ {h _ {k}}} {\mathrm{osc}} f + \underset {T _ {u} (S _ {h _ {k}})} {\mathrm{osc}} g + \delta_ {k} ^ {\gamma / n} \Bigr) \leq C _ {\bar {K}} (\delta_ {1} + \delta_ {1} ^ {\gamma / n}).\tag{5.17}
$$

This implies in particular that, if$\delta _ { 1 }$is suficiently small,$B _ { 1 / ( 2 \bar { K } ) } \subset \{ \bar { v } _ { k } \leq 1 \} \subset B _ { 2 \bar { K } }$. By standard estimates on the sections of solutions to the Monge-Amp\`ere equation, the shapes of$\{ \bar { v } _ { k } \le 1 \}$and $\{ \bar { v } _ { k } \le 1 / 2 \}$are comparable, and in addition sections are well included into each other [26, Theorem 3.3.8]: there exists a universal constant$L > 1$such that

$$
B _ {1 / (L \bar {K})} \subset \{\bar {v} _ {k} \leq 1 / 2 \} \subset B _ {L \bar {K}}, \quad \operatorname{dist} \bigl (\{\bar {v} _ {k} \leq 1 / 4 \}, \partial \{\bar {v} _ {k} \leq 1 / 2 \} \bigr) \geq 1 / (L K).
$$

Using again (5.17) we deduce that, if$\delta _ { 1 }$is suficiently small,

$$
B _ {1 / (2 L \bar {K})} \subset \{\bar {u} _ {k} \leq 1 / 2 \} \subset B _ {2 L \bar {K}}, \quad \text {   dist   } (\{\bar {u} _ {k} \leq 1 / 4 \}, \partial \{\bar {u} _ {k} \leq 1 / 2 \}) \geq 1 / (2 L K)
$$

so, by scaling back,

$$
B _ {\sqrt {h _ {k + 1}} / (2 L \bar {K})} \subset S _ {h _ {k + 1}} \subset B _ {2 L \bar {K} \sqrt {h _ {k + 1}}}, \quad \text { dist } \bigl (S _ {h _ {k + 2}}, \partial S _ {h _ {k + 1}} \bigr) \geq \sqrt {h _ {k}} / (2 L K).\tag{5.18}
$$

This allows us to apply Proposition 5.2 also to$\bar { u } _ { k + 1 }$to get

$$
\| \bar {u} _ {k + 1} - \bar {v} _ {k + 1} \| _ {C ^ {0} (\bar {S} _ {k + 1})} \leq C _ {2 L \bar {K}} \Bigl ( \begin{array}{c} \text { osc } \\ S _ {h _ {k + 1}} \end{array} f + \begin{array}{c} \text { osc } \\ T _ {u} (S _ {h _ {k + 1}}) \end{array} g + \delta_ {k + 1} ^ {\gamma / n} \Bigr).\tag{5.19}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i.e., 3  K < <sup>¯</sup> )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|<sup>D2w(0)</sup>|</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>K¯</sup> ≤ <sup>p2(M</sup> <sup>+</sup> <sup>1)</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">B1/3 ⊂ Z ⊂ B3</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1/2</sup> ≤ <sup>f(0)/g(0)</sup> ≤ <sup>2</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>K¯</sup> ≥ <sup>3.</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">M ≥ 1,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">w¯ := (M + 1)x<sup>2</sup><sub>1</sub> +f(0)x<sup>2</sup><sub>2</sub>+ x<sup>2</sup><sub>3</sub> + . . . + x<sup>2</sup><sub>n</sub> g(0) M + 1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>is</sup> <sup>a</sup> <sup>solution</sup> <sup>of</sup> <sup>(5.16)</sup> <sup>such</sup> <sup>that</sup> <sup>B</sup>1/√2(M+1) ⊂ <sup>B</sup>1/√M+1 ⊂ {<sup>w¯</sup> ≤ <sup>1</sup>} ⊂ <sup>B</sup>√2(M+1) <sup>and</sup> |<sup>D2w¯(0)</sup>| <sup>=</sup> <sup>2(M</sup> <sup>+</sup> <sup>1)</sup> <sup>.</sup>B1/√2(M+1) ⊂ B1/√M+1 ⊂ {ω ≤ 1} ⊂ B√2(M+1) and |D2¯(0)| = 2(M + 1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>The fact that K<sup>¯</sup> is well defined follows by the following facts: first of all, by definition, M is an a-priori bound for whenever w is a solution of (5.16) with B<sub>1/3</sub> Z  B<sub>3</sub>, so  On the other hand. Indeed, since (by (5.11)) and M  1, the function</span></small>

We now observe that, by (5.15) and the$C ^ { 1 , \beta }$regularity of u (see Theorem 4.3), it follows that

$$
\operatorname{diam} (S _ {h _ {k}}) + \operatorname{diam} (T _ {u} (S _ {h _ {k}})) \leq C h _ {k} ^ {\beta / 2},
$$

so by the$C ^ { 0 , \alpha }$regularity of$f$and$^ { g , }$and the$C ^ { 2 , \alpha }$regularity of$c ,$we have (recall that$\gamma < 1 )$

$$
\underset {S _ {h _ {k}}} {\mathrm{osc}} f + \underset {T _ {u} (S _ {h _ {k}})} {\mathrm{osc}} g + \delta_ {k} ^ {\gamma / n} \leq C ^ {\prime} h _ {k} ^ {\sigma}, \quad \sigma := \frac {\alpha \beta \gamma}{2 n}\tag{5.20}
$$

Hence, by (5.17) and (5.19),

$$
\left\| \bar {u} _ {k} - \bar {v} _ {k} \right\| _ {C ^ {0} (\bar {S} _ {k})} + \left\| \bar {u} _ {k + 1} - \bar {v} _ {k + 1} \right\| _ {C ^ {0} (\bar {S} _ {k + 1})} \leq C \left(C _ {\bar {K}} + C _ {2 L \bar {K}}\right) h _ {k} ^ {\sigma},
$$

from which we deduce (recall that$h _ { k } = 2 h _ { k + 1 } )$

$$
\begin{array}{r l} & {\| v _ {k} - v _ {k + 1} \| _ {C ^ {0} (S _ {h _ {k + 1}})} \leq \| v _ {k} - u \| _ {C ^ {0} (S _ {h _ {k}})} + \| u - v _ {k + 1} \| _ {C ^ {0} (S _ {h _ {k + 1}})}} \\ & {\qquad = h _ {k} \| \bar {u} _ {k} - \bar {v} _ {k} \| _ {C ^ {0} (S _ {k})} + h _ {k + 1} \| \bar {u} _ {k + 1} - \bar {v} _ {k + 1} \| _ {C ^ {0} (S _ {k + 1})}} \\ & {\qquad \leq C \left(C _ {\bar {K}} + C _ {2 L \bar {K}}\right) h _ {k} ^ {1 + \sigma}.} \end{array}
$$

Since$v _ { k }$and$v _ { k + 1 }$are two strictly convex solutions of the Monge Amp\`ere equation with constant right hand side inside$S _ { h _ { k + 1 } }$, and since$S _ { h _ { k + 2 } }$is “well contained” inside$S _ { h _ { k + 1 } }$, by classical Pogorelov and Schauder estimates we get

(5.21)

$$
\| D ^ {2} v _ {k} - D ^ {2} v _ {k + 1} \| _ {C ^ {0} (S _ {h _ {k + 2}})} \leq C _ {\bar {K}} ^ {\prime} h _ {k} ^ {\sigma}\tag{5.22}
$$

$$
\| D ^ {3} v _ {k} - D ^ {3} v _ {k + 1} \| _ {C ^ {0} (S _ {h _ {k + 2}})} \leq C _ {\bar {K}} ^ {\prime} h _ {k} ^ {\sigma - 1 / 2},
$$

where$C _ { \hat { K } } ^ { \prime }$is some constant depending only on$\bar { K }$. By (5.21) applied to$v _ { j }$for all$j = 1 , \dots , k$(this can be done since, by the inductive assumption, (5.15) holds for$h = h _ { j }$with$j = 1 , \ldots , k )$we obtain

$$
\begin{array}{l} | D ^ {2} v _ {k + 1} (0) | \leq | D ^ {2} v _ {1} (0) | + \sum_ {j = 1} ^ {k} | D ^ {2} v _ {j} (0) - D ^ {2} v _ {j + 1} (0) | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}
$$

provided we choose$h _ { 1 }$small enough (recall that$h _ { k } = h _ { 1 } 2 ^ { - k } )$. By the definition of$\bar { K }$it follows that also$S _ { h _ { k + 1 } }$satisfies (5.15), concluding the proof of the inductive step.

Step 2: higher regularity. Now that we know that$u \in C ^ { 1 , 1 } ( B _ { 1 / 8 } )$, Equation (2.10) becomes uniformly elliptic. So one may use Evans-Krylov Theorem to obtain that$u \in C _ { \mathrm { l o c } } ^ { 2 , \sigma ^ { \prime } } ( B _ { 1 / 9 } )$for some $\sigma ^ { \prime } > 0$, and then standard Schauder estimates to conclude the proof. However, for the convenience of the reader, we show here how to give a simple direct proof of the$C ^ { 2 , \sigma ^ { \prime } }$regularity of u with $\sigma ^ { \prime } = 2 \sigma$

As in the previous step, it sufices to show that u is$C ^ { 2 , \sigma ^ { \prime } }$at the origin, and for this we have to prove that there exists a sequence of paraboloids$P _ { k }$such that

$$
\sup _ {B _ {r _ {0} ^ {k} / C}} | u - P _ {k} | \leq C r _ {0} ^ {k (2 + \sigma^ {\prime})}\tag{5.23}
$$

for some$r _ { 0 } , C > 0$

Let$v _ { k }$be as in the previous step, and let$P _ { k }$be their second order Taylor expansion at 0:

$$
P _ {k} (x) = v _ {k} (\mathbf {0}) + \nabla v _ {k} (\mathbf {0}) \cdot x + \frac {1}{2} D ^ {2} v _ {k} (\mathbf {0}) x \cdot x.
$$

We observe that, thanks to (5.15),

$$
\| v _ {k} - P _ {k} \| _ {C ^ {0} (B (0, \sqrt {h _ {k + 2}} / K))} \leq \| v _ {k} - P _ {k} \| _ {C ^ {0} (S _ {h _ {k + 2}})} \leq C \| D ^ {3} v _ {k} \| _ {C ^ {0} (S _ {h _ {k + 2}})} h _ {k} ^ {3 / 2}.\tag{5.24}
$$

In addition, by (5.22) applied with$j = 1 , \dots , k$and recalling that$h _ { k } = h _ { 1 } 2 ^ { - k }$and$2 \sigma < 1$(see (5.20)), we get

$$
\| D ^ {3} v _ {k} \| _ {C ^ {0} (S _ {h _ {k + 2}})} \leq \| D ^ {3} v _ {1} \| _ {C ^ {0} (S _ {h _ {3}})} + \sum_ {j = 1} ^ {k} \| D ^ {3} v _ {j} - D ^ {3} v _ {j + 1} \| _ {C ^ {0} (S _ {h _ {j + 2}})}\tag{5.25}
$$

$$
\leq C \left(1 + \sum_ {j = 1} ^ {k} h _ {j} ^ {(\sigma - 1 / 2)}\right) \leq C h _ {k} ^ {\sigma - 1 / 2}.
$$

Combining (5.15), (5.24), (5.25), and recalling (5.17) and (5.20), we obtain

$$
\| u - P _ {k} \| _ {C ^ {0} (B _ {\sqrt {h _ {k + 2}} / K})} \leq \| v _ {k} - P _ {k} \| _ {C ^ {0} (S _ {h _ {k + 2}})} + \| v _ {k} - u \| _ {C ^ {0} (S _ {h _ {k + 2}})} \leq C h _ {k} ^ {1 + \sigma},
$$

so (5.23) follows with$r _ { 0 } = 1 / \sqrt { 2 }$and$\sigma ^ { \prime } = 2 \sigma$

## References

[1] L. Ambrosio, N. Gigli, G. Savar´e. Gradient flows in metric spaces and in the space of probability measures. Second edition. Lectures in Mathematics ETH Z¨urich. Birkh¨auser Verlag, Basel, 2008.

[2] Y. Brenier. Polar factorization and monotone rearrangement of vector-valued functions. Comm. Pure Appl. Math. 44 (1991) 375-417.

[3] L. A. Cafarelli. A localization property of viscosity solutions to the Monge-Amp\`ere equation and their strict convexity. Ann. of Math. (2) 131 (1990), no. 1, 129-134.

[4] L. A. Cafarelli. Some regularity properties of solutions of Monge Amp\`ere equation. Comm. Pure Appl. Math. 44 (1991), no. 8-9, 965-969.

[5] L. A. Cafarelli. The regularity of mappings with a convex potential. J. Amer. Math. Soc. 5 (1992), no. 1, 99-104.

[6] L. A. Cafarelli. Interior$W ^ { 2 , p }$estimates for solutions of the Monge-Amp\`ere equation. Ann. of Math. (2) 131 (1990), no. 1, 135-150.

[7] L. A. Cafarelli, M. M. Gonz´ales, T. Nguyen. A perturbation argument for a Monge-Amp\`ere type equation arising in optimal transportation. Preprint, 2011.

[8] L. A. Cafarelli, Y. Y. Li. A Liouville theorem for solutions of the Monge-Amp\`ere equation with periodic data. Ann. Inst. H. Poincar´e Anal. Non Lin´eaire 21 (2004), no. 1, 97-120.

[9] D. Cordero-Erausquin, R. J. McCann, M. Schmuckenschl¨ager. A Riemannian interpolation inequality \`a la Borell, Brascamp and Lieb. Invent. Math. 146, 2, (2001), 219257.

[10] P. Delano¨e, Y. Ge. Regularity of optimal transportation maps on compact, locally nearly spherical, manifolds. J. Reine Angew. Math. 646 (2010), 65-115.

[11] P. Delano¨e, F. Rouvi\`ere. Positively curved Riemannian locally symmetric spaces are positively squared distance curved. Canad. J. Math., to appear.

[12] L. C. Evans, R. F. Gariepy. Measure theory and fine properties of functions. Studies in Advanced Mathematics. CRC Press, Boca Raton, FL, 1992.

[13] A. Fathi, A. Figalli. Optimal transportation on non-compact manifolds. Israel J. Math. 175 (2010), no. 1, 1-59.

[14] A. Figalli. Existence, uniqueness, and regularity of optimal transport maps. SIAM J. Math. Anal. 39 (2007), no. 1, 126-137.

[15] A. Figalli. Regularity of optimal transport maps [after Ma-Trudinger-Wang and Loeper]. (English summary) S´eminaire Bourbaki. Volume 2008/2009. Expos´es 997-1011. Ast´erisque No. 332 (2010), Exp. No. 1009, ix, 341-368.

[16] A. Figalli. Regularity properties of optimal maps between nonconvex domains in the plane. Comm. Partial Diferential Equations 35 (2010), no. 3, 465-479.

[17] A. Figalli, N. Gigli. Local semiconvexity of Kantorovich potentials on non-compact manifolds. ESAIM Control Optim. Calc. Var. 17 (2011), no. 3, 648-653.

[18] A. Figalli, Y. H. Kim. Partial regularity of Brenier solutions of the Monge-Amp\`ere equation, Discrete Contin. Dyn. Syst. 28 (2010), no. 2, 559-565.

[19] A. Figalli, Y. H. Kim, R. J. McCann. H¨older continuity and injectivity of optimal maps. Preprint, 2011.

[20] A. Figalli, Y. H. Kim, R. J. McCann. Regularity of optimal transport maps on multiple products of spheres. J. Eur. Math. Soc. (JEMS), to appear.

[21] A. Figalli, G. Loeper.$C ^ { 1 }$regularity of solutions of the Monge-Amp\`ere equation for optimal transport in dimension two. Calc. Var. Partial Diferential Equations 35 (2009), no. 4, 537–550.

[22] A. Figalli, L. Riford. Continuity of optimal transport maps and convexity of injectivity domains on smal deformations$\mathrm { o f ~ } \mathbb { S } ^ { 2 }$. Comm. Pure Appl. Math. 62 (2009), no. 12, 1670–1706.

[23] A. Figalli, L. Riford, C. Villani. On the Ma-Trudinger-Wang curvature on surfaces. Calc. Var. Partial Diferential Equations 39 (2010), no. 3-4, 307-332.

[24] A. Figalli, L. Riford, C. Villani. Necessary and suficient conditions for continuity of optimal transport maps on Riemannian manifolds. Tohoku Math. J. (2) 63 (2011), no. 4, 855-876.

[25] A. Figalli, L. Riford, C. Villani. Nearly round spheres look convex. Amer. J. Math. 134 (2012), no. 1, 109-139.

[26] C.Gutierrez. The Monge-Amp´ere equation. Progress in Nonlinear Diferential Equations and their Applications, 44. Birkh¨auser Boston, Inc., Boston, MA, 2001.

[27] H.-Y. Jian, X.-J. Wang. Continuity estimates for the Monge-Amp\`ere equation. SIAM J. Math. Anal. 39 (2007), no. 2, 608-626.

[28] Y.-H. Kim. Counterexamples to continuity of optimal transport maps on positively curved Riemannian manifolds. Int. Math. Res. Not. IMRN 2008, Art. ID rnn120, 15 pp.

[29] Y.-H. Kim, R. J. McCann. Towards the smoothness of optimal maps on Riemannian submersions and Riemannian products (of round spheres in particular). J. Reine Angew. Math., to appear.

[30] J. Liu, N.S. Trudinger, X.-J. Wang. Interior$C ^ { 2 , \alpha }$regularity for potential functions in optimal transportation. Comm. Partial Diferential Equations 35 (2010), no. 1, 165-184.

[31] G. Loeper. On the regularity of solutions of optimal transportation problems. Acta Math. 202 (2009), no. 2, 241-283.

[32] G. Loeper. Regularity of optimal maps on the sphere: The quadratic cost and the reflector antenna. Arch. Ration. Mech. Anal. 199 (2011), no. 1, 269–289.

[33] X. N. Ma, N. S. Trudinger, X. J. Wang. Regularity of potential functions of the optimal transportation problem. Arch. Ration. Mech. Anal. 177 (2005), no. 2, 151-183.

[34] R. J. McCann. Polar factorization of maps on Riemannian manifolds. Geom. Funct. Anal. 11 (2001), 589-608.

[35] N. S. Trudinger, X.-J. Wang. On the second boundary value problem for Monge-Amp\`ere type equations and optimal transportation. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 8 (2009), no. 1, 143–174.

[36] N. S. Trudinger, X.-J. Wang. On strict convexity and continuous diferentiability of potential functions in optimal transportation. Arch. Ration. Mech. Anal. 192 (2009), no. 3, 403–418.

[37] C. Villani. Optimal Transport. Old and New. Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], 338. Springer-Verlag, Berlin, 2009.

Department of Mathematics, The University of Texas at Austin, 1 University Station C1200, Austin TX 78712, USA