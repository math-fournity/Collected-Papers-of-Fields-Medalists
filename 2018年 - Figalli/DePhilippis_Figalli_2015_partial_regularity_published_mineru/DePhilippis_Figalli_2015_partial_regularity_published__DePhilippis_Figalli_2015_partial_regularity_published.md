# PARTIAL REGULARITY FOR OPTIMAL TRANSPORT MAPS by GUIDO De PHILIPPIS and ALESSIO FIGALLI

## ABSTRACT

We prove that, for general cost functions on R<sup>n</sup>, or for the cost$d ^ { 2 } / 2$on a Riemannian manifold, optimal transport maps between smooth densities are always smooth outside a closed singular set of measure zero

## 1. Introduction

A natural and important issue in optimal transport theory is the regularity of optimal transport maps. Indeed, apart from being a typical PDE/analysis question, knowing whether optimal maps are smooth or not is an important step towards a qualitative understanding of them.

It is by now well known that, for the smoothness of optimal maps, conditions on both the cost function and on the geometry of the supports of the measures are needed.

In the special case$c ( x , y ) = | x - y | ^ { 2 } / 2$on R<sup>n</sup>, Caffarelli [3–6] proved regularity of optimal maps under suitable assumptions on the densities and on the geometry of their support. More precisely, in its simplest form, Caffarelli’s result states as follows:

Theorem 1.1. — Letf and g be smooth probability densities, respectively bounded awayfrom zero and infinity on two bounded open sets X and Y, and let$\mathrm { T } : \mathrm { X }  \mathrm { Y }$denote the unique optimal transport mapfromf to gfor the quadratic cost$| x - y | ^ { 2 } / 2$. If Y is convex, then T is smooth inside X. On the other hand, if Y is not convex, then there exist smooth densitiesf and g (both bounded awayfrom zero and infinity on X and Y, respectively)for which the map T is not continuous.

A natural question which arises from the previous result is whether one may prove some partial regularity on T when the convexity assumption on Y is removed. In [16, 18] the authors proved the following result:

Theorem 1.2. — Letf and g be smooth probability densities, respectively bounded awayfrom zero and infinity on two bounded open sets X and Y, and let$\mathrm { T } : \mathrm { X }  \mathrm { Y }$denote the unique optimal transport mapfromf to gfor the quadratic cost$\vert x - y \vert ^ { 2 } / 2$. Then there exist two open sets$\mathrm { X } ^ { \prime } \subset \mathrm { X }$and $\mathrm { Y } ^ { \prime } \subset \mathrm { Y } ,$, with$| \mathrm { X } \setminus \mathrm { X ^ { \prime } } | = | \mathrm { Y } \setminus \mathrm { Y ^ { \prime } } | = 0 .$, such that$\mathrm { T } : \mathrm { X } ^ { \prime } \to \mathrm { Y } ^ { \prime }$is a smooth diffeomorphism.

In the case of general cost functions on R<sup>n</sup>, or when$c ( x , y ) = d ( x , y ) ^ { 2 } / 2$on a Riemannian manifold M$( d ( x , y )$being the Riemannian distance), the situation is much more complicated. Indeed, as shown by Ma, Trudinger, and Wang [33], and Loeper [31], in addition to suitable convexity assumptions on the support of the target density (or on the cut locus of the manifold when$\operatorname { s u p p } ( g ) = \mathbf { M } [ 2 4 ] )$, a very strong structural condition on the cost function, the so-called MTWcondition, is needed to ensure the smoothness of the map.

More precisely, ifthe MTW condition holds (together with some suitable convexity assumptions on the target domain), then the optimal map is smooth [19, 21, 30, 35, 36]. On the other hand, if the MTW condition fails at one point, then one can construct smooth densities (both supported on domains which satisfy the needed convexity assumptions) for which the optimal transport map is not continuous [31] (see also [15]).

In the case of Riemannian manifolds, the MTW condition for$c = d ^ { 2 } / 2$is very restrictive: indeed, as shown by Loeper [31], it implies that M has non-negative sectional curvature, and actually it is much stronger than the latter [23, 28]. In particular, if M has negative sectional curvature, then the MTW condition fails at every point. Let us also mention that, up to now, the MTW condition is known to be satisfied only for very special classes of Riemannian manifolds, such as spheres, their products, their quotients and submersions, and their perturbations [10, 11, 20, 22, 25, 29, 32], and for instance it is known to fail on sufficiently flat ellipsoids [23].

The goal of the present paper is to show that, even without any condition on the cost function or on the supports of the densities, optimal transport maps are always smooth outside a closed singular set of measure zero. In order to state our results, we first have to introduce some basic assumptions on the cost functions which are needed to ensure existence and uniqueness of optimal maps. As before, X and Y denote two open subsets of R<sup>n</sup>.

(C0) The cost function$c : \mathrm { X } \times \mathrm { Y }  \mathbf { R }$is of class$\mathrm { C ^ { 2 } }$with$\| c \| _ { \mathrm { C ^ { 2 } ( X \times Y ) } } < \infty$

(C1) For any$x \in \mathrm { X } .$, the map$\mathrm { Y } \ni \ j \mapsto - \mathrm { D } _ { \boldsymbol { x } } c ( \boldsymbol { x } , \boldsymbol { y } ) \in \mathbf { R } ^ { n }$is injective.

(C2) For any y ∈ Y, the map$\mathrm { X } \ni x \mapsto - \mathrm { D } _ { v } c ( x , y ) \in \mathbf { R } ^ { n }$is injective.

(C3) det$( \mathrm { D } _ { x y } c ) ( x , y ) \neq 0$for all$( x , y ) \in \mathrm { X } \times \mathrm { Y }$

Here are our main results:

Theorem$\mathbf { 1 . 3 . { \_ { L e t } \mathrm { X , Y } \subset \mathbf { R } ^ { n } } }$be two bounded open sets, and let$f : \mathrm { X } \to \mathbf { R } ^ { + }$and$g :$ $\mathrm { \bf Y } \to { \bf R } ^ { + }$be two continuous probability densities, respectively bounded awayfrom zero and infinity on X and Y. Assume that the cost c :$\mathbf { X } \times \mathbf { Y }  \mathbf { R }$satisfies (C0)–(C3), and denote by T :$\mathrm { X } \to \mathrm { Y }$the unique optimal transport map sendingf onto g. Then there exist two relatively closed sets$\Sigma _ { \mathrm { X } } \subset \mathrm { X } , \Sigma _ { \mathrm { Y } } \subset \mathrm { Y }$ ofmeasure zero such that$\operatorname { T } : \operatorname { X } \setminus  \sum _ { \operatorname { X } }  \operatorname { Y } \setminus \Sigma _ { \operatorname { Y } }$is a homeomorphism ofclass$\mathrm { C } _ { \mathrm { l o c } } ^ { 0 , \beta } \ f o r$any$\beta < 1$ In addition,$i f c \in \mathrm { C } _ { \mathrm { l o c } } ^ { k + 2 , \alpha } ( \mathrm { X } \times \mathrm { Y } ) , f \in \mathrm { C } _ { \mathrm { l o c } } ^ { k , \alpha } ( \mathrm { X } )$, and$g \in \mathbf { C } _ { \mathrm { l o c } } ^ { k , \alpha } ( \mathbf { \bar { Y } } )$for some$k \geq 0$and$\alpha \in ( 0 , 1 )$, then T :$: \mathrm { X } \setminus \Sigma _ { \mathrm { X } } \to \mathrm { Y } \setminus \Sigma _ { \mathrm { Y } }$is a diffeomorphism ofclass$\mathrm { C } _ { \mathrm { l o c } } ^ { k + 1 , \alpha }$

Theorem 1.4. — Let M be a smooth Riemannian manifold, and letf,$g : \mathrm { M } \to \mathbf { R } ^ { + }$be two continuous probability densities, locally bounded awayfrom zero and infinity on M. Let$\mathrm { T } : \mathrm { M } \to \mathrm { M }$ denote the optimal transport map for the cost$c = d ^ { 2 } / 2$sendingf onto$g .$Then there exist two closed sets$Z _ { \mathrm { { X } } } , Z _ { \mathrm { { Y } } } \subset \mathrm { { M } }$ofmeasure zero such that$\mathrm { T } : \mathrm { M } \setminus \Sigma _ { \mathrm { X } } \to \mathrm { M } \setminus \Sigma _ { \mathrm { Y } }$is a homeomorphism ofclass $\mathrm { C } _ { \mathrm { l o c } } ^ { 0 , \beta }$for any$\beta < 1$. In addition, ifbothf and g are ofclass$\mathrm { C } ^ { k , \alpha }$, then$\mathrm { T } : \mathrm { M } \setminus \Sigma _ { \mathrm { X } } \to \mathrm { M } \setminus \Sigma _ { \mathrm { Y } }$is a diffeomorphism ofclass$\mathrm { C } _ { \mathrm { l o c } } ^ { k + 1 , \alpha }$

The paper is structured as follows: in the next section we introduce some notation and preliminary results. Then, in Section 3, we show how both Theorem 1.3 and Theorem 1.4 are a direct consequence of some local regularity results around differentiability points of T, see Theorems 4.3 and 5.3. Finally, Sections 4 and 5 are devoted to the proof of these local results.

## 2. Notation and preliminary results

Through a well established procedure, maps that solve optimal transport problems derive from a c-convex potential, itself solution to a Monge-Ampère type equation.

More precisely, given a cost function$c : \mathrm { X } \times \mathrm { Y }  \mathbf { R } .$, a function u :$\mathbf X \to \mathbf R$is said c-convex if it can be written as

$$
u (x) = \sup _ {y \in \mathrm{Y}} \left\{- c (x, y) + \lambda_ {y} \right\},\tag{2.1}
$$

for some constants$\lambda _ { y } \in \mathbf { R } \cup \{ - \infty \}$

Similarly to the subdifferential for convex function, for c-convex functions one can talk about their c-subdifferential: if$u : \mathrm { X }  \mathbf { R }$is a c-convex function as above, the$c -$ subdifferential of u at x is the (nonempty) set

$$
\partial_ {c} u (x) := \left\{y \in \overline {{\mathrm{Y}}} \colon u (z) \geq - c (z, y) + c (x, y) + u (x) \forall z \in \mathrm{X} \right\}.\tag{2.2}
$$

If$x _ { 0 } \in \mathrm { X }$and$y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$, we will say that the function

$$
\mathrm{C} _ {x _ {0}, y _ {0}} (\cdot) := - c (\cdot , y _ {0}) + c (x _ {0}, y _ {0}) + u (x _ {0})\tag{2.3}
$$

is a c-support for u at$x _ { 0 }$. We also define the Frechet subdifferential of u at x as

$$
\partial^ {-} u (x) := \left\{p \in \mathbf {R} ^ {n}: u (z) \geq u (x) + p \cdot (z - x) + o (| z - x |) \right\}.
$$

We will use the following notation: if$\mathrm { E } \subset \mathrm { X }$then

$$
\partial_ {c} u (\mathrm{E}) := \bigcup_ {x \in \mathrm{E}} \partial_ {c} u (x), \quad \partial^ {-} u (\mathrm{E}) := \bigcup_ {x \in \mathrm{E}} \partial^ {-} u (x).
$$

It is easy to check that, if c is of class$\mathrm { C } ^ { 1 }$, then the following inclusion holds:

$$
y \in \partial_ {c} u (x) \quad \Longrightarrow \quad - \mathrm{D} _ {x} c (x, y) \in \partial^ {-} u (x).\tag{2.4}
$$

In addition, if c satisfies (C0)–(C2), then we can define the c-exponential map:

$$
\text { for   any } x \in \mathrm{X}, y \in \mathrm{Y}, p \in \mathbf {R} ^ {n}, \quad \left\{ \begin{array}{l l} \mathrm{c} - \exp_ {x} (p) = y & \Leftrightarrow \quad p = - \mathrm{D} _ {x} c (x, y) \\ \mathrm{c} ^ {*} - \exp_ {y} (p) = x & \Leftrightarrow \quad p = - \mathrm{D} _ {y} c (x, y) \end{array} \right.\tag{2.5}
$$

Using (2.5), we can rewrite (2.4) as

$$
\partial_ {c} u (x) \subset \mathrm{c} - \exp_ {x} \left(\partial^ {-} u (x)\right).\tag{2.6}
$$

Notice that, if$c \in \mathrm { C } ^ { 1 }$and Y is bounded, it follows immediately from (2.1) that c-convex functions are Lipschitz, so in particular they are differentiable a.e.

The following notation will be convenient: given a c-convex function$u : \mathrm { X }  \mathbf { R } .$, we define (at almost every point) the map$\mathrm { T } _ { u } : \mathrm { X } \to \mathrm { Y }$as

$$
\mathrm{T} _ {u} (x) := \mathrm{c} - \exp_ {x} (\nabla u (x)).\tag{2.7}
$$

(Of course$\mathrm { T } _ { u }$depends also on$c ,$but to keep the notation lighter we prefer not to make this dependence explicit. The reader should keep in mind that, whenever we write$\mathrm { T } _ { u } ,$ the cost c is always the one for which u is c-convex.)

Finally, let us observe that if c satisfies (C0) and Y is bounded, then it follows from (2.1) that u is semiconvex (i.e., there exists a constant$\mathrm { ~ C ~ } > 0$such that$u + \mathrm { C } | x | ^ { 2 } / 2$is convex, see for instance [13]). In particular, by Alexandrov’s Theorem, c-convex functions are twice differentiable a.e. (see [37, Theorem 14.25] for a list of different equivalent definitions of this notion).

The following is a basic result in optimal transport theory (see for instance [37, Chapter 10]):

Theorem 2.1.$\_ L e t c : \mathrm { X } \times \mathrm { Y } \to \mathbf { R }$satisfy (C0)–(C1). Given two probability densitiesf and g supported on X and Y respectively, there exists a c-convexfunction u :$\mathbf X \to \mathbf R$such that$\mathrm { T } _ { u } : \mathrm { X } \to \mathrm { Y }$ is the unique optimal transport map sending f onto g.

In the particular case$c ( x , y ) = - x \cdot y$(which is equivalent to the quadratic cost $| x - y | ^ { 2 } / 2 )$, c-convex functions are convex and the above result takes the following simple form [2]:

Theorem 2.2.$- \mathit { L e t } \mathit { c ( x , y ) } = - x \cdot y$. Given two probability densities f and g supported on X and Y respectively, there exists a convexfunction$v : \mathrm { X } \to \mathbf { R }$such that$\mathrm { T } _ { v } = \nabla v : \mathrm { X } \to \mathrm { Y }$is the unique optimal transport map sending f onto g.

Although on Riemannian manifolds the cost function$c = d ^ { 2 } / 2$is not smooth everywhere, one can still prove existence of optimal maps [13, 17, 34] (let us remark that, in this case, the c-exponential map coincides with the classical exponential map in Riemannian geometry):

Theorem 2.3. — Let M be a smooth Riemannian manifold, and$c = d ^ { 2 } / 2$. Given two probability densitiesf and g supported on M, there exists a c-convexfunction$u : \mathrm { M } \to \mathbf { R } \cup \{ + \infty \}$such that u is differentiablef-a.e., and$\mathrm { T } _ { u } ( x ) = \mathrm { e x p } _ { x } ( \nabla u ( x ) )$is the unique optimal transport map sending f onto g.

We conclude this section by recalling that c-convex functions arising in optimal transport problems solve a Monge-Ampère type equation almost everywhere, referring to [1, Section 6.2], [37, Chapters 11 and 12], and [15] for more details.

Whenever c satisfies (C0)–(C3), then the transport condition$( \mathrm { T } _ { u } ) _ { \sharp } f = g \mathrm { g i v e s }$5

$$
\left| \det \bigl (\mathrm{DT} _ {u} (x) \bigr) \right| = \frac {f (x)}{g (\mathrm{T} _ {u} (x))} \quad \mathrm{a.e.}\tag{2.8}
$$

In addition, the c-convexity of u implies that, at every point x where u is twice differentiable,

$$
\mathrm{D} ^ {2} u (x) + \mathrm{D} _ {x x} c \left(x, \mathrm{c} - \exp_ {x} (\nabla u (x))\right) \geq 0.\tag{2.9}
$$

Hence, writing (2.7) as

$$
- \mathrm{D} _ {x} c (x, \mathrm{T} _ {u} (x)) = \nabla u (x),
$$

differentiating the above relation with respect to x, and using (2.8) and (2.9), we obtain

$$
\begin{array}{l} \det \bigl (\mathrm{D} ^ {2} u (x) + \mathrm{D} _ {x x} c \bigl (x, \mathrm{c} - \exp_ {x} \bigl (\nabla u (x) \bigr) \bigr) \bigr) \\ = \bigl | \det \bigl (\mathrm{D} _ {x y} c \bigl (x, \mathrm{c} - \exp_ {x} \bigl (\nabla u (x) \bigr) \bigr) \bigr) \bigr | \frac {f (x)}{g (\mathrm{c} - \exp_ {x} (\nabla u (x)))} \end{array}\tag{2.10}
$$

at every point x where u it is twice differentiable. In particular, when$c ( x , y ) = - x \cdot y .$, the convex function v provided by Theorem 2.2 solves the classical Monge-Ampère equation

$$
\det \bigl (\mathrm{D} ^ {2} v (x) \bigr) = \frac {f (x)}{g (\nabla v (x))} \quad \mathrm{a.e.}
$$

## 3. The localization argument and proof of the results

The goal of this section is to prove Theorems 1.3 and 1.4 by showing that the assumptions of Theorems 4.3 and 5.3 below are satisfied near almost every point.

The rough idea is the following: if x¯ is a point where the semiconvex function u is twice differentiable, then around that point u looks like a parabola. In addition, by looking close enough to${ \overline { { x } } } ,$the cost function c will be very close to the linear one and the densities will be almost constant there. Hence we can apply Theorem 4.3 to deduce that u is of class$\mathrm { C } ^ { 1 , \beta }$in neighborhood of x¯ (resp. u is ofclass$\bar { \mathrm { C } } ^ { k + 2 , \alpha }$by Theorem 5.3, if$c \in \mathrm { C } _ { \mathrm { l o c } } ^ { k + 2 , \alpha }$and $f , g \in \mathbf { C } _ { \mathrm { l o c } } ^ { k , \alpha } )$, which implies in particular that$\mathrm { T } _ { u }$is of class$\mathrm { \dot { C } } ^ { 0 , \beta }$in neighborhood of x¯ (resp. $\mathrm { T } _ { u }$is of class$\mathrm { C } ^ { k + 1 , \alpha }$by Theorem 5.3, if$\cdot _ { c \in \mathbf { C } _ { \mathrm { l o c } } ^ { k + 2 , \alpha } }$and$f , g \in \mathbf { C } _ { \mathrm { l o c } } ^ { k , \alpha } )$. Being our assumptions completely symmetric in x and$y ,$we can apply the same argument to the optimal map $\mathrm { T ^ { * } }$sending g onto$f .$. Since$\mathrm { T } ^ { * } = ( \mathrm { T } _ { u } ) ^ { - 1 }$(see the discussion below), it follows that$\mathrm { T } _ { u }$is a global homeomorphism of class$\mathrm { C } _ { \mathrm { l o c } } ^ { 0 , \beta }$(resp.$\mathrm { T } _ { u }$is a global diffeomorphism of class$\mathrm { C } _ { \mathrm { l o c } } ^ { k + 1 , \alpha } )$ outside a closed set of measure zero.

We now give a detailed proof.

ProofofTheorem$I . 3 . { \mathrm { - L e t } }$us introduce the “c-conjugate” of$u ,$that${ \mathrm { i s } } ,$the function $u ^ { c } : \mathrm { Y }  \mathbf { R }$defined as

$$
u ^ {c} (y) := \sup _ {x \in \mathrm{X}} \left\{- c (x, y) - u (x) \right\}.
$$

Then$u ^ { c }$is c<sup>∗</sup>-convex, where

$$
c ^ {*} (y, x) := c (x, y), \quad \text { and } \quad x \in \partial_ {c ^ {*}} u ^ {c} (y) \quad \Longleftrightarrow \quad y \in \partial_ {c} u (x)\tag{3.1}
$$

(see for instance [37, Chapter 5]).

Being our assumptions completely symmetric in x and$y , c ^ { * }$satisfies the same assumptions as c. In particular, by Theorem 2.1, there exists an optimal map$\mathrm { T ^ { * } }$(with respect to$c ^ { * } )$sending g onto$f .$. In addition, it is well-known that$\mathrm { T ^ { * } }$is actually equal to

$$
\mathrm{T} _ {u ^ {c}} (y) = \mathrm{c} ^ {*} - \exp_ {y} \left(\nabla u ^ {c} (y)\right),
$$

and that$\mathrm { T } _ { u }$and$\mathrm { T } _ { u ^ { c } }$are inverse to each other, that is

$$
\mathrm{T} _ {u ^ {c}} \left(\mathrm{T} _ {u} (x)\right) = x, \quad \mathrm{T} _ {u} \left(\mathrm{T} _ {u ^ {c}} (y)\right) = y \quad \text { for   a.e. } x \in \mathrm{X}, y \in \mathrm{Y}\tag{3.2}
$$

(see, for instance, [1, Remark 6.2.11]).

Since semiconvex functions are twice differentiable$\mathrm { a . e . , }$there exist sets$\mathrm { X } _ { 1 } \subset$ $\mathrm { X } , \mathrm { Y } _ { 1 } \subset \mathrm { Y }$of full measure such that (3.2) holds for every$x \in \mathrm { X } _ { 1 }$and$y \in \mathrm { Y } _ { 1 }$, and in addition u is twice differentiable for every$x \in \mathrm { X } _ { 1 }$and$u ^ { c }$is twice differentiable for every $\boldsymbol { y } \in \mathrm { Y } _ { 1 }$. Let us define

$$
\mathrm{X} ^ {\prime} := \mathrm{X} _ {1} \cap (\mathrm{T} _ {u}) ^ {- 1} (\mathrm{Y} _ {1}).
$$

Using that$\mathrm { T } _ { u }$transports$f$on$g$and that the two densities are bounded away from zero and infinity, we see that X<sup></sup> is of full measure in$\mathrm { X }$

We fix a point$\bar { x } \in \mathrm { X } ^ { \prime }$. Since u is differentiable at$\bar { x }$(being twice differentiable), it follows by (2.6) that the set$\partial _ { c } u ( \bar { x } )$is a singleton, namely$\partial _ { c } u ( \bar { x } ) = \{ \mathrm { c } \mathrm { - } \mathrm { e x p } _ { \bar { x } } ( \nabla u ( \bar { x } ) ) \}$}. Set $\bar { y } : = \mathrm { c } \mathrm { - } \mathrm { e x p } _ { \bar { x } } ( \nabla u ( \bar { x } ) )$. Since$\bar { y } \in \mathrm { Y } _ { 1 }$(by definition of$\mathrm { X } ^ { \prime } )$,$u ^ { c }$is twice differentiable at$\bar { y }$and $\overline { { x } } = \mathrm { T } _ { u ^ { c } } ( \overline { { y } } )$. Up to a translation in the system of coordinates (both in x and$y )$we can assume that both$\bar { x }$and$\bar { \mathcal { D } }$coincide with the origin 0.

Let us define

$$
\bar {u} (z) := u (z) - u (\mathbf {0}) + c (z, \mathbf {0}) - c (\mathbf {0}, \mathbf {0}),
$$

$$
\bar {c} (z, w) := c (z, w) - c (z, \mathbf {0}) - c (\mathbf {0}, w) + c (\mathbf {0}, \mathbf {0}),
$$

$$
\bar {u} ^ {\bar {c}} (w) := u ^ {c} (w) - u (\mathbf {0}) + c (\mathbf {0}, w) - c (\mathbf {0}, \mathbf {0}).
$$

Then u¯ is a ¯c-convex function,$\bar { u } ^ { \bar { c } }$is its ¯c-conjugate,$\mathrm { T } _ { \bar { u } } = \mathrm { T } _ { u } ,$, and$\mathrm { T } _ { \bar { u } ^ { c } } = \mathrm { T } _ { u ^ { c } }$, so in particular$( \mathrm { T } _ { \bar { u } } ) _ { \sharp } f = g$and$( \mathrm { T } _ { \bar { u } \bar { c } } ) _ { \sharp } g = f$. In addition, because by assumption$\mathbf { 0 } \in \mathrm { X } ^ { \prime } , \bar { u }$is twice differentiable at 0 and u¯<sup>¯c</sup> is twice differentiable at$\mathbf { 0 } = \mathrm { T } _ { \bar { u } } ( \mathbf { 0 } )$. Let us define$\mathrm { P } : = \mathrm { D } ^ { 2 } \bar { u } ( \mathbf { 0 } )$), and$\mathrm { M } : = \mathrm { D } _ { x y } \overline { { c } } ( \mathbf { 0 } , \mathbf { 0 } )$. Then, since$\bar { c } ( \cdot , \mathbf { 0 } ) = \bar { c } ( \mathbf { 0 } , \cdot ) \equiv 0$and$\overline { c } \in { \mathrm { C } } ^ { 2 }$, a Taylor expansion gives

$$
\bar {u} (z) = \frac {1}{2} \mathrm{P} z \cdot z + o \bigl (| z | ^ {2} \bigr), \qquad \bar {c} (z, w) = \mathrm{M} z \cdot w + o \bigl (| z | ^ {2} + | w | ^ {2} \bigr).
$$

Let us observe that, since by assumptionf and g are bounded away from zero and infinity, by (C3) and (2.10) applied to u¯ and ¯c we get that det(P), det(M) = 0. In addition (2.9) implies that P is a positive definite symmetric matrix. Hence, we can perform a second change of coordinates:$z \mapsto \tilde { z } : = \mathrm { P } ^ { 1 / 2 } z , w \mapsto \tilde { w } : = - \mathrm { P } ^ { - 1 / 2 } \mathrm { M } ^ { * } w$(M<sup>∗</sup> being the transpose of M), so that, in the new variables,

$$
\tilde {u} (\tilde {z}) := \bar {u} (z) = \frac {1}{2} | \tilde {z} | ^ {2} + o \big (| \tilde {z} | ^ {2} \big), \qquad \tilde {c} (\tilde {z}, \tilde {w}) := \bar {c} (z, w) = - \tilde {z} \cdot \tilde {w} + o \big (| \tilde {z} | ^ {2} + | \tilde {w} | ^ {2} \big).\tag{3.3}
$$

By an easy computation it follows that$( \mathrm { T } _ { \tilde { u } } ) _ { \sharp } \tilde { f } = \tilde { g }$, where<sup>1</sup>

$$
\tilde {f} (\tilde {z}) := \det \left(\mathrm{P} ^ {- 1 / 2}\right) f \left(\mathrm{P} ^ {- 1 / 2} \tilde {z}\right), \quad \tilde {g} (\tilde {w}) := \left| \det \left(\left(\mathrm{M} ^ {*}\right) ^ {- 1} \mathrm{P} ^ {1 / 2}\right) \right| g \left(- \left(\mathrm{M} ^ {*}\right) ^ {- 1} \mathrm{P} ^ {1 / 2} \tilde {w}\right).\tag{3.4}
$$

Notice that

$$
\mathrm{D} _ {\tilde {z} \tilde {z}} \tilde {c} (\mathbf {0}, \mathbf {0}) = \mathrm{D} _ {\tilde {w} \tilde {w}} \tilde {c} (\mathbf {0}, \mathbf {0}) = \mathbf {0} _ {n \times n}, \qquad - \mathrm{D} _ {\tilde {z} \tilde {w}} \tilde {c} (\mathbf {0}, \mathbf {0}) = \mathrm{Id}, \qquad \mathrm{D} ^ {2} \tilde {u} (\mathbf {0}) = \mathrm{Id},\tag{3.5}
$$

so, using (2.10), we deduce that

$$
\frac {\tilde {f} (\mathbf {0})}{\tilde {g} (\mathbf {0})} = \frac {\det (\mathrm{D} ^ {2} \tilde {u} (\mathbf {0}) + \mathrm{D} _ {\tilde {z} \tilde {z}} \tilde {c} (\mathbf {0} , \mathbf {0}))}{| \det (\mathrm{D} _ {\tilde {z} \tilde {w}} \tilde {c} (\mathbf {0} , \mathbf {0})) |} = 1.\tag{3.6}
$$

To ensure that we can apply Theorems 4.3 and 5.3, we now perform the following dilation: for$\rho > 0$we define

$$
u _ {\rho} (\tilde {z}) := \frac {1}{\rho^ {2}} \bar {u} (\rho \tilde {z}), \qquad c _ {\rho} (\tilde {z}, \tilde {w}) := \frac {1}{\rho^ {2}} \bar {c} (\rho \tilde {z}, \rho \tilde {w}).
$$

We claim that, provided$\rho$is sufficiently small,$u _ { \rho }$and$c _ { \rho }$satisfy the assumptions of Theorems 4.3 and 5.3.

Indeed, it is immediate to check that$u _ { \rho }$is a$c _ { \rho }$-convex function. Also, by the same argument as above, from the relation$( \mathrm { T } _ { \tilde { u } } ) _ { \sharp } \tilde { f } = \tilde { g }$we deduce that$\mathrm { T } _ { u _ { \rho } }$sends$\tilde { \ b { f } } ( \rho \tilde { \ b { z } } )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">μ :=f(x)dx</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ν := g(y)dy</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup> An easy way to check this is to observe that the measures and are independent of the choice of coordinates, hence (3.4) follows from the identitie</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f (x)dx = <sup>˜</sup>f (x˜)dx˜, g(y)dy = ˜g(y˜)dy˜.</span></small>

onto$\tilde { g } ( \rho \tilde { w } )$). In addition, since we can freely multiply both densities by a same constant, it actually follows from (3.6) that$( \mathrm { T } _ { u _ { \rho } } ) _ { \sharp } f _ { \rho } = g _ { \rho }$, where

$$
f _ {\rho} (\tilde {z}) := \frac {\tilde {f} (\rho \tilde {z})}{\tilde {f} (\mathbf {0})}, \qquad g _ {\rho} (\tilde {w}) := \frac {\tilde {g} (\rho \tilde {w})}{\tilde {g} (\mathbf {0})}.
$$

In particular, sincef and$g$are continuous, we get

$$
\left| f _ {\rho} - 1 \right| + \left| g _ {\rho} - 1 \right|\rightarrow 0 \quad \text { inside } \mathrm{B} _ {3}\tag{3.7}
$$

as$\rho \to 0 . \mathrm { A l s o } .$, by (3.3) we get that, for any$\tilde { z } , \tilde { w } \in \mathrm { B _ { 3 } }$小

$$
u _ {\rho} (\tilde {z}) = \frac {1}{2} | \tilde {z} | ^ {2} + o (1), \qquad c _ {\rho} (\tilde {z}, \tilde {w}) = - \tilde {z} \cdot \tilde {w} + o (1),\tag{3.8}
$$

where$o ( 1 )  0 \mathrm { a s } \rho  0$. In particular, (4.9) and (4.10) hold with any positive constants $\delta _ { 0 } , \eta _ { 0 }$provided$\rho$is small enough.

Furthermore, by the second order differentiability of$\cdot \tilde { u }$at 0 it follows that the multivalued map$\tilde { z } \mapsto \partial ^ { - } \bar { u } ( \tilde { z } )$is differentiable at 0 (see [37, Theorem 14.25]) with gradient equal to the identity matrix (see (3.3)), hence

$$
\partial^ {-} u _ {\rho} (\tilde {z}) \subset \mathrm{B} _ {\gamma_ {\rho}} (\tilde {z}) \quad \forall \tilde {z} \in \mathrm{B} _ {2},
$$

where$\gamma _ { \rho } \to 0$as$\rho \to 0$. Since$\partial _ { c _ { \rho } } u _ { \rho } \subset \mathrm { c } _ { \rho } \mathrm { - e x p } ( \partial ^ { - } u _ { \rho } )$(by (2.6)) and$\| \mathrm { c } _ { \rho } \mathrm { - e x p - I d } \| _ { \infty } =$ o(1) (by (3.8)), we get

$$
\partial_ {c _ {\rho}} u _ {\rho} (\tilde {z}) \subset \mathrm{B} _ {\delta_ {\rho}} (\tilde {z}) \quad \forall \tilde {z} \in \mathrm{B} _ {3},\tag{3.9}
$$

with$\delta _ { \rho } = o ( 1 )$as$\rho \to 0$. Moreover, the$c _ { \rho } ^ { \ }$-conjugate of$u _ { \rho }$is easily seen to be

$$
u _ {\rho} ^ {c _ {\rho}} (\tilde {w}) = \bar {u} ^ {\bar {c}} \big (\rho \big (\mathrm{M} ^ {*} \big) ^ {- 1} \mathrm{P} ^ {1 / 2} \tilde {w} \big).
$$

Since$u ^ { c }$is twice differentiable at$\mathbf { 0 , }$so is$u _ { \rho } ^ { c _ { \rho } }$. In addition, an easy computation<sup>2</sup> shows that $\mathrm { D } ^ { 2 } u _ { \rho } ^ { c _ { \rho } } ( \mathbf { 0 } ) = \mathrm { I d }$. Hence, arguing as above we obtain that

$$
\partial_ {c _ {\rho} ^ {*}} u _ {\rho} ^ {c _ {\rho}} (\tilde {w}) \subset \mathrm{B} _ {\delta_ {\rho} ^ {\prime}} (\tilde {w}) \quad \forall \tilde {w} \in \mathrm{B} _ {3},\tag{3.10}
$$

with$\delta _ { \rho } ^ { \prime } = o ( 1 )$as$\rho \to 0$

We now define

$$
\mathcal {C} _ {1} := \overline {{\mathrm{B}}} _ {1}, \qquad \mathcal {C} _ {2} := \partial_ {c _ {\rho}} u _ {\rho} (\mathcal {C} _ {1}).
$$

$$
\mathrm{D} _ {\tilde {z}} c _ {\rho} \big (\tilde {z}, \mathrm{T} _ {u _ {\rho}} (\tilde {z}) \big) = - \nabla u _ {\rho} (\tilde {z}) \quad \text { and } \quad \mathrm{D} _ {\tilde {w}} c _ {\rho} \big (\mathrm{T} _ {u _ {\rho} ^ {c _ {\rho}}} (\tilde {w}), \tilde {w} \big) = - \nabla u _ {\rho} ^ {c _ {\rho}} (\tilde {w})
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup> For instance, this follows by differentiating both relations</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">at 0, and using then (3.5) and the fact that ∇T cρ (0) = [∇T<sub>uρ</sub> (0)]<sup>−1</sup> and D<sup>2</sup>u<sub>ρ</sub> (0) = Id.</span></small>

Observe that both$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$are closed (since the c-subdifferential of a compact set is closed). Also, thanks to (3.9), by choosing$\rho$small enough we can ensure that$\mathrm { { B } } _ { 1 / 3 } \subset$ $\mathcal { C } _ { 2 } \subset \mathrm { B } _ { 3 }$. Finally, it follows from (2.6) that

$$
(\mathrm{T} _ {u _ {\rho}}) ^ {- 1} (\mathcal {C} _ {2}) \setminus \mathcal {C} _ {1} \subset (\mathrm{T} _ {u _ {\rho}}) ^ {- 1} \big (\big \{\text { points   of   non - differentiability   of } u _ {\rho} ^ {c _ {\rho}} \big \} \big),
$$

and since this latter set has measure zero, a simple computation shows that

$$
\left(\mathrm{T} _ {u _ {\rho}}\right) _ {\sharp} \left(f _ {\rho} \mathbf {1} _ {\mathcal {C} _ {1}}\right) = g _ {\rho} \mathbf {1} _ {\mathcal {C} _ {2}}.
$$

Thus, thanks to (4.8), we get that for any$\beta < 1$the assumptions of Theorem 4.3 are satisfied, provided we choose$\rho$sufficiently small. Moreover, if in addition $c \in \mathrm { C } _ { \mathrm { l o c } } ^ { k + 2 , \alpha } ( \mathrm { X } \times \mathrm { Y } ) , f \in \mathrm { C } _ { \mathrm { l o c } } ^ { k , \alpha } ( \mathrm { X } )$, and$g \in \mathbf { C } _ { \mathrm { l o c } } ^ { k , \alpha } ( \mathrm { Y } )$, then also the assumptions of Theorem 5.3 are satisfied.

Hence, by applying Theorem 4.3 (resp. Theorem 5.3) we deduce that$u _ { \rho } \in$ $\mathrm { C } ^ { 1 , \beta } ( \mathbf { B } _ { 1 / 7 } )$(resp.$u _ { \rho } \in \mathrm { C } ^ { k + 2 , \alpha } ( \mathbf { B } _ { 1 / 9 } ) \big )$, so going back to the original variables we get the existence of a neighborhood$\mathcal { U } _ { \bar { x } }$of x¯ such that$u \in \mathrm { C } ^ { 1 , \beta } ( \mathcal { U } _ { x } )$(resp.$u \in \mathrm { C } ^ { k + 2 , \alpha } ( \mathcal { U } _ { \bar { x } } ) \bar { ) }$. This implies in particular that$\mathrm { T } _ { u } \in \mathrm { C } ^ { 0 , \beta } ( \mathcal { U } _ { \bar { x } } )$(resp.$\mathrm { T } _ { u } \in \mathrm { C } ^ { k + 1 , \alpha } ( \mathcal { U } _ { \overline { { x } } } ) ;$). Moreover, it follows by Corollary 4.6 that$\mathrm { T } _ { u } ( { \mathcal { U } } _ { \overline { { x } } } )$contains a neighborhood ofy¯.

We now observe that, by symmetry, we can also apply Theorem 4.3 (resp. Theorem 5.3) to$u _ { \rho } ^ { c _ { \rho } }$. Hence, there exists a neighborhood$\mathcal { V } _ { \bar { y } }$ofy¯ such that$\mathrm { T } _ { u ^ { c } } \in \mathrm { C } ^ { 0 , \beta } ( \mathcal { V } _ { \overline { { y } } } )$. Since $\mathrm { T } _ { u }$and$\mathrm { T } _ { u ^ { c } }$are inverse to each other (see (3.2)) we deduce that, possibly reducing the size of$\mathcal { U } _ { \bar { x } } , ~ \mathrm { T } _ { u }$is a homeomorphism (resp. diffeomorphism) between$\mathcal { U } _ { \bar { x } }$and$\mathrm { T } _ { u } ( { \cal U } _ { x } )$. Let us consider the open sets

$$
\mathrm{X} ^ {\prime \prime} := \bigcup_ {\bar {x} \in \mathrm{X} ^ {\prime}} \mathcal {U} _ {\bar {x}}, \quad \mathrm{Y} ^ {\prime \prime} := \bigcup_ {\bar {x} \in \mathrm{X} ^ {\prime}} \mathrm{T} _ {u} (\mathcal {U} _ {\bar {x}}),
$$

and define the (relatively) closed$\Sigma _ { \mathrm { X } } : = \mathrm { X } \setminus \mathrm { X } ^ { \prime \prime } , \Sigma _ { \mathrm { Y } } : = \mathrm { Y } \setminus \mathrm { Y } ^ { \prime \prime }$. Since$\mathrm { X } ^ { \prime \prime } \supset \mathrm { X } ^ { \prime } , \mathrm { X } ^ { \prime \prime }$is a set of full measure, so$| \Sigma _ { \mathrm { X } } | = 0$. In addition, since$\Sigma _ { \mathrm { Y } } = \mathrm { Y } \setminus \mathrm { Y ^ { \prime \prime } } \subset \mathrm { Y } \setminus \mathrm { T } _ { u } ( \mathrm { X ^ { \prime } } )$and$\mathrm { T } _ { u } ( \mathrm { X } ^ { \prime } )$ has full measure in Y, we also get that$| \Sigma _ { \mathrm { Y } } | = 0$

Finally, since$\mathrm { T } _ { u } : \mathrm { X } \setminus \backslash \Sigma _ { \mathrm { X } }   \mathrm { Y } \setminus \Sigma _ { \mathrm { Y } }$is a local homeomorphism (resp. diffeomorphism), by (3.2) it follows that$\mathrm { T } _ { u } : \mathrm { X } \setminus \backslash \Sigma _ { \mathrm { X } }   \mathrm { Y } \setminus \Sigma _ { \mathrm { Y } }$is a global homeomorphism (resp. diffeomorphism), which concludes the proof.-

ProofofTheorem 1.4. — The only difference with respect to the situation in Theorem 1.3 is that now the cost function$c = d ^ { 2 } / 2$is not smooth on the whole$\mathbf { M } \times \mathbf { M }$ However, even if$d ^ { 2 } / 2$is not everywhere smooth and M is not necessarily compact, it is still true that the c-convex function u provided by Theorem 2.3 is locally semiconvex $( \mathrm { i . e . , }$, it is locally semiconvex when seen in any chart) [13, 17]. In addition, as shown in [9, Proposition 4.1] (see also [14, Section 3]), if u is twice differentiable at$x ,$then the point$\mathrm { T } _ { u } ( x )$is not in the cut-locus of x. Since the cut-locus is closed and$d ^ { 2 } / 2$is smooth outside the cut-locus, we deduce the existence of a set X of full measure such that, if$x _ { 0 } \in \mathrm { X }$, then: (1) u is twice differentiable at$x _ { 0 } ; ( 2 )$there exists a neighborhood $\mathcal { U } _ { x _ { 0 } } \times \mathcal { V } _ { \mathrm { T } _ { u } ( x _ { 0 } ) } \subset \mathrm { M } \times \mathrm { M }$of$( x _ { 0 } , \mathrm { T } _ { u } ( x _ { 0 } ) )$such that$c \in \mathrm { C } ^ { \infty } ( \mathcal { U } _ { x _ { 0 } } \times \mathcal { V } _ { \mathrm { T } _ { u } ( x _ { 0 } ) } )$. Hence, by taking a local chart around$( x _ { 0 } , \mathrm { T } _ { u } ( x _ { 0 } ) )$, the same proof as the one of Theorem 1.3 shows that$\mathrm { T } _ { u }$ is a local homeomorphism (resp. diffeomorphism) around almost every point. Using as before that$\mathrm { T } _ { u } : \mathrm { M } \to \mathrm { M }$is invertible$\mathrm { a . e . , }$it follows that$\mathrm { T } _ { u }$is a global homeomorphism (resp. diffeomorphism) outside a closed singular set of measure zero. We leave the details to the interested reader.-

## 4.$\mathbf { C } ^ { 1 , \beta }$regularity and strict c-convexity

In this and the next section we prove that, if in some open set a c-convex function u is sufficiently close to a parabola and the cost function is close to the linear one, then u is smooth in some smaller set.

The idea of the proof (which is reminiscent of the argument introduced by Caffarelli in [6] to show$\mathrm { W } ^ { 2 , p }$and$\mathrm { C ^ { 2 , \alpha } }$estimates for the classical Monge-Ampère equation, though several additional complications arise in our case) is the following: since the cost function is close to the linear one and both densities are almost constant, u is close to a convex function v solving an optimal transport problem with linear cost and constant densities (Lemma 4.1). In addition, since u is close to a parabola, so is v. Hence, by [18] and Caffarelli’s regularity theory, v is smooth, and we can use this information to deduce that u is even closer to a second parabola (given by the second order Taylor expansion of v at the origin) inside a small neighborhood around of origin. By rescaling back this neighborhood at scale 1 and iterating this construction, we obtain that u is$\bar { \mathrm { C } } ^ { 1 , \beta }$at the origin for some$\beta \in ( 0 , 1 )$). Since this argument can be applied at every point in a neighborhood ofthe origin, we deduce that u is$\mathrm { C } ^ { 1 , \beta }$there, see Theorem 4.3. (A similar strategy has also been used in [7] to show regularity optimal transport maps for the cost$| x - y | ^ { p }$, either when$\boldsymbol { p }$is close to 2 or when X and Y are sufficiently far from each other.)

Once this result is proved, we know that$\partial ^ { - } u$is a singleton at every point, so it follows from (2.6) that

$$
\partial_ {c} u (x) = \mathrm{c} - \exp_ {x} \left(\partial^ {-} u (x)\right),
$$

see Remark 4.4 below. (The above identity is exactly what in general may fail for general c-convex functions, unless the MTW condition holds [31].) Thanks to this fact, we obtain that u enjoys a comparison principle (Proposition 5.2), and this allows us to use a second approximation argument with solutions of the classical Monge-Ampère equation (in the spirit of [6, 27]) to conclude that u is$\mathrm { C } ^ { 2 , \sigma ^ { \prime } }$in a smaller neighborhood, for some$\sigma ^ { \prime } > 0$ Then higher regularity follows from standard elliptic estimates, see Theorem 5.3.

(4.1)

Lemma 4.1.$- L e t \mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$be two closed sets such that

$$
\mathrm{B} _ {1 / \mathrm{K}} \subset \mathcal {C} _ {1}, \quad \mathcal {C} _ {2} \subset \mathrm{B} _ {\mathrm{K}}
$$

for some$\mathrm { K } \geq 1 , f$and$g$two densities supported respectively in$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$, and$u : { \mathcal { C } } _ { 1 }  \mathbf { R }$a cconvex function such that$\partial _ { c } u ( \mathcal { C } _ { 1 } ) \subset \mathbf { B } _ { \mathrm { K } }$and$( \mathrm { T } _ { u } ) _ { \sharp } f = g .$. Let$\rho > 0$be such that$| \mathcal { C } _ { 1 } | = | \rho \mathcal { C } _ { 2 } |$ (where$\rho \mathcal { C } _ { 2 }$denotes the dilation$o f { \mathcal { C } } _ { 2 }$with respect to the origin), and let v be a convexfunction such that $\nabla v _ { \sharp } \mathbf { 1 } _ { { \mathcal { C } } _ { 1 } } = \mathbf { 1 } _ { \rho { \mathcal { C } } _ { 2 } }$and$v ( \mathbf { 0 } ) = u ( \mathbf { 0 } )$). Then there exists an increasingfunction ω :$\mathbf { R } ^ { + }  \mathbf { R } ^ { + }$, depending only K, and satisfying$\omega ( \delta ) \ge \delta$and$\omega ( 0 ^ { + } ) = 0$, such that, if

$$
\| f - \mathbf {1} _ {\mathcal {C} _ {1}} \| _ {\infty} + \| g - \mathbf {1} _ {\mathcal {C} _ {2}} \| _ {\infty} \leq \delta\tag{4.2}
$$

and

$$
\left\| c (x, y) + x \cdot y \right\| _ {\mathrm{C} ^ {2} (\mathrm{B} _ {\mathrm{K}} \times \mathrm{B} _ {\mathrm{K}})} \leq \delta ,\tag{4.3}
$$

then

$$
\left\| u - v \right\| _ {\mathrm{C} ^ {0} \left(\mathrm{B} _ {1 / \mathrm{K}}\right)} \leq \omega (\delta).
$$

Proof. — Assume the lemma is false. Then there exists$\varepsilon _ { 0 } > 0$, a sequence of closed sets${ \mathcal { C } } _ { 1 } ^ { h } , { \mathcal { C } } _ { 2 } ^ { h }$satisfying (4.1), functions$f _ { h } , g _ { h }$satisfying (4.2) with$\delta = 1 / h$, and costs$c _ { h }$converging in$\mathrm { C ^ { 2 } ~ t o ~ } { - x \cdot y }$, such that

$$
u _ {h} (\mathbf {0}) = v _ {h} (\mathbf {0}) = 0 \quad \text { and } \quad \| u _ {h} - v _ {h} \| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {1 / \mathrm{K}})} \geq \varepsilon_ {0},
$$

where$u _ { h }$and$v _ { h }$are as in the statement. First, we extend$u _ { h }$an$v _ { h }$to$\mathrm { B _ { K } }$as

$$
u _ {h} (x) := \sup _ {z \in \mathcal {C} _ {1} ^ {h}, y \in \partial_ {c _ {h}} u _ {h} (z)} \left\{u _ {h} (z) - c _ {h} (x, y) + c _ {h} (z, y) \right\},
$$

$$
v _ {h} (x) := \sup _ {z \in \mathcal {C} _ {1} ^ {h}, p \in \partial^ {-} v _ {h} (z)} \left\{v _ {h} (z) + p \cdot (x - z) \right\}.
$$

Notice that, since by assumption$\partial _ { c _ { h } } u _ { h } ( { \mathcal { C } } _ { 1 } ^ { h } ) \subset \mathbf { B } _ { \mathrm { K } }$, we have$\partial _ { c _ { h } } u _ { h } ( \mathbf { B } _ { \mathrm { K } } ) \subset \mathbf { B } _ { \mathrm { K } }$. Also, $( \mathrm { T } _ { u _ { h } } ) _ { \sharp } f _ { h } = g _ { h }$gives that$\textstyle \int f _ { h } = \int g _ { h }$, so it follows from (4.2) that

$$
\rho_ {h} = \left(\left| \mathcal {C} _ {1} ^ {h} \right| / \left| \mathcal {C} _ {2} ^ {h} \right|\right) ^ {1 / n} \rightarrow 1 \quad \text { as } h \rightarrow \infty ,
$$

which implies that$\partial ^ { - } v _ { h } ( \mathbf { B } _ { \mathrm { K } } ) \subset \mathbf { B } _ { \rho _ { h } \mathrm { K } } \subset \mathbf { B } _ { \mathrm { 2 K } }$for h large. Thus, since the$\mathrm { C ^ { 1 } - n o r m }$of$c _ { h }$is uniformly bounded, we deduce that both$u _ { h }$and$v _ { h }$are uniformly Lipschitz. Recalling that$u _ { h } ( \mathbf { 0 } ) = v _ { h } ( \mathbf { 0 } ) = 0$, we get that, up to a subsequence,$u _ { h }$and$v _ { h }$uniformly converge inside$\mathrm { B _ { K } }$to$u _ { \infty }$and$v _ { \infty }$respectively, where

$$
u _ {\infty} (\mathbf {0}) = v _ {\infty} (\mathbf {0}) = 0 \quad \text { and } \quad \| u _ {\infty} - v _ {\infty} \| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {1 / \mathrm{K}})} \geq \varepsilon_ {0}.\tag{4.4}
$$

In addition$f _ { h }$(resp.$g _ { h } )$weak-∗ converge in$\mathrm { L } ^ { \infty }$to some density$f _ { \infty } \ ( \mathrm { r e s p . } \ g _ { \infty } )$supported in$\overline { { \mathrm { B } } } _ { \mathrm { K } }$. Also, since$\rho _ { h } \to 1$, using (4.2) we get that$\mathbf { 1 } _ { \mathcal { C } _ { 1 } ^ { h } } \left( \mathrm { r e s p . } \ \mathbf { 1 } _ { \rho _ { h } \mathcal { C } _ { 2 } ^ { h } } \right)$weak-∗ converges in$\mathrm { L } ^ { \infty }$ to$f _ { \infty } \mathrm { ( r e s p . } g _ { \infty } )$. Finally we remark that, because of (4.2) and the fact that$\mathcal { C } _ { 1 } ^ { h } \supset \mathbf { B } _ { \mathrm { 1 / K } }$, we also have

$$
f _ {\infty} \geq \mathbf {1} _ {\mathrm{B} _ {1 / \mathrm{K}}}.
$$

In order to get a contradiction we have to show that$u _ { \infty } = v _ { \infty }$in$\mathbf { B } _ { \mathrm { l / K } }$. To see this, we apply [37, Theorem 5.20] to deduce that both$\nabla u _ { \infty }$and$\nabla \boldsymbol { v } _ { \infty }$are optimal transport maps for the linear cost$- x \cdot y$sending$f _ { \infty }$onto$g _ { \infty }$. By uniqueness of the optimal map (see Theorem 2.2) we deduce that$\nabla \boldsymbol { v } _ { \infty } = \nabla u _ { \infty }$almost everywhere inside$\mathbf { B } _ { 1 / \mathrm { K } } \subset \mathrm { s p t } f _ { \infty } ,$ hence$u _ { \infty } = v _ { \infty }$in$\bf { B } _ { \mathrm { { l / K } } }$(since$u _ { \infty } ( \mathbf { 0 } ) = v _ { \infty } ( \mathbf { 0 } ) = 0 )$, contradicting (4.4).-

Here and in the sequel, we use$\mathcal { N } _ { r } ( \mathrm { E } )$to denote the r-neighborhood of a set E.

Lemma 4.2. — Let u and v be, respectively, c-convex and convex, let$\mathbf { D } \in \mathbf { R } ^ { n \times n }$be a symmetric matrix satisfying

$$
\mathrm{Id} / \mathrm{K} \leq \mathrm{D} \leq \mathrm{KId}\tag{4.5}
$$

for some$\mathrm { K } \geq 1$, and define the ellipsoid

$$
\mathrm{E} \left(x _ {0}, h\right) := \left\{x: \mathrm{D} \left(x - x _ {0}\right) \cdot \left(x - x _ {0}\right) \leq h \right\}, \quad h > 0.
$$

Assume that there exist small positive constants ε, δ such that

$$
\| v - u \| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, h))} \leq \varepsilon , \quad \| c + x \cdot y \| _ {\mathrm{C} ^ {2} (\mathrm{E} (x _ {0}, h) \times \partial_ {c} u (\mathrm{E} (x _ {0}, h))} \leq \delta .\tag{4.6}
$$

Then

$$
\partial_ {c} u \big (\mathrm{E} (x _ {0}, h - \sqrt {\varepsilon}) \big) \subset \mathcal {N} _ {\mathrm{K} ^ {\prime} (\delta + \sqrt {h \varepsilon})} \big (\partial v \big (\mathrm{E} (x _ {0}, h) \big) \big) \quad \forall 0 <   \varepsilon <   h ^ {2} \leq 1,\tag{4.7}
$$

where K<sup></sup> depends only on K.

Proof. — Up to a change of coordinates we can assume that$x _ { 0 } = \mathbf { 0 }$, and to simplify notation we set$\mathrm { E } _ { h } : = \mathrm { E } ( x _ { 0 } , h )$. Let us define

$$
\bar {v} (x) := v (x) + \varepsilon + 2 \sqrt {\varepsilon} (\mathrm{D} x \cdot x - h),
$$

so that$\bar { v } \ge u$outside$\mathrm { E } _ { h }$, and$\bar { v } \le u$inside$\mathrm { E } _ { h - \sqrt { \varepsilon } }$. Then, taking a c-support to u in$\mathrm { E } _ { h - \sqrt { \varepsilon } }$ $( \mathrm { i . e . , a }$function$\mathrm { C } _ { x , y }$as in (2.3), with$x \in \operatorname { E } _ { h - { \sqrt { \varepsilon } } }$and$y \in \partial _ { c } u ( x ) )$, moving it down and then lifting it up until it touches v¯ from below, we see that it has to touch the graph of$\bar { v }$at some point$\overline { { x } } \in \operatorname { E } _ { h } \colon$in other words<sup>3</sup>

$$
\partial_ {c} u (\mathrm{E} _ {h - \sqrt {\varepsilon}}) \subset \partial_ {c} \bar {v} (\mathrm{E} _ {h}).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∂<sub>c</sub>v(¯ x) ⊂ c-exp (∂<sup>−</sup>v(¯ x))</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup> Even if v¯ is not c-convex, it still makes sense to consider his c-subdifferential (notice that the c-subdifferential of v¯ may be empty at some points). In particular, the inclusion still holds.</span></small>

By (4.5) we see that diam$\mathrm { E } _ { h } \le 2 \sqrt { \mathrm { K } h } .$, so by a simple computation (using again (4.5)) we get

$$
\partial^ {-} \bar {v} (\mathrm{E} _ {h}) \subset \mathcal {N} _ {4 \mathrm{K} \sqrt {\mathrm{Kh} \varepsilon}} \bigl (\partial^ {-} v (\mathrm{E} _ {h}) \bigr).
$$

Thus, since$\partial _ { c } \bar { v } ( \mathrm { E } _ { h } ) \subset \mathrm { c } \mathrm { - e x p } ( \partial ^ { - } \bar { v } ( \mathrm { E } _ { h } ) )$(by (2.6)) and$\| \mathrm { c - e x p } - \mathrm { I d } \| _ { \mathrm { C } ^ { 0 } } \leq \delta$(by (4.6)), we easily deduce that

$$
\partial_ {c} u (\mathrm{E} _ {h - \sqrt {\varepsilon}}) \subset \mathcal {N} _ {\mathrm{K} ^ {\prime} (\delta + \sqrt {h \varepsilon})} \bigl (\partial^ {-} v (\mathrm{E} _ {h}) \bigr),
$$

proving (4.7).

Theorem 4.3. — Let$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$be two closed sets satisfying

$$
\mathrm{B} _ {1 / 3} \subset \mathcal {C} _ {1}, \quad \mathcal {C} _ {2} \subset \mathrm{B} _ {3},
$$

let f , g be two densities supported in$\mathcal { C } _ { 1 }$and$\mathcal { C } _ { 2 }$respectively, and let$u : { \mathcal { C } } _ { 1 }  \mathbf { R }$be a c-convexfunction such that$\partial _ { c } u ( \mathcal { C } _ { 1 } ) \subset \mathbf { B } _ { 3 }$and$( \mathrm { T } _ { u } ) _ { \sharp } f = g$. Then,for every$\beta \in ( 0 , 1 )$there exist constants$\delta _ { \mathrm { 0 } } , \eta _ { \mathrm { 0 } } > 0$ such that thefollowing holds:$i f$

(4.8)

$$
\| f - \mathbf {1} _ {\mathcal {C} _ {1}} \| _ {\infty} + \| g - \mathbf {1} _ {\mathcal {C} _ {2}} \| _ {\infty} \leq \delta_ {0},\tag{4.9}
$$

$$
\left\| c (x, y) + x \cdot y \right\| _ {\mathrm{C} ^ {2} \left(\mathrm{B} _ {3} \times \mathrm{B} _ {3}\right)} \leq \delta_ {0},
$$

and

$$
\left\| u - \frac {1}{2} | x | ^ {2} \right\| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {3})} \leq \eta_ {0},\tag{4.10}
$$

then$u \in \mathrm { C } ^ { 1 , \beta } ( \mathbf { B } _ { 1 / 7 } )$

Proof. — We divide the proof into several steps.

• Step 1: u is close to a strictly convex solution ofthe Monge Ampère equation.

Let$v : \mathbf { R } ^ { n } \to \mathbf { R }$be a convex function such that$\nabla v _ { \sharp } \mathbf { 1 } _ { \mathcal { C } _ { 1 } } = \mathbf { 1 } _ { \rho \mathcal { C } _ { 2 } }$with$\rho = ( | \mathcal { C } _ { 1 } | / | \mathcal { C } _ { 2 } | ) ^ { 1 / n }$(see Theorem 2.2). Up to adding a constant to$v ,$without loss of generality we can assume that$v ( \mathbf { 0 } ) = u ( \mathbf { 0 } )$. Hence, we can apply Lemma 4.1 to obtain

$$
\| v - u \| _ {\mathrm{C} ^ {0} \left(\mathrm{B} _ {1 / 3}\right)} \leq \omega \left(\delta_ {0}\right)\tag{4.11}
$$

for some (universal) modulus of continuity$\omega : \mathbf { R } ^ { + }  \mathbf { R } ^ { + }$, which combined with (4.10) gives

$$
\left\| v - \frac {1}{2} | x | ^ {2} \right\| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {1 / 3})} \leq \eta_ {0} + \omega (\delta_ {0}).
$$

Also, since$\textstyle { \int _ { { \mathcal { C } } _ { 1 } } f = \int _ { { \mathcal { C } } _ { 9 } } g } .$, it follows easily from (4.8) that$| \rho - 1 | \leq 3 \delta _ { 0 }$. By these two facts we get that$\partial ^ { - } v ( \mathrm { B } _ { 1 / 4 } ) \subset \mathrm { B } _ { 7 / 2 4 } \subset \rho \mathcal { C } _ { 2 }$provided$\delta _ { 0 }$and$\eta _ { 0 }$are small enough (recall that v is convex and that$\mathbf { B } _ { 1 / 3 } \subset \mathcal { C } _ { 2 } )$, so we can apply [18, Proposition 3.4] to deduce that v is a strictly convex Alexandrov solution to the Monge-Ampère equation

$$
\det \mathrm{D} ^ {2} v = 1 \quad \text { in } \mathrm{B} _ {1 / 4}.\tag{4.12}
$$

In addition, by a simple compactness argument, we see that the modulus of strict convexity of v inside$\mathrm { { B } } _ { 1 / 4 }$is universal. So, by classical Pogorelov and Schauder estimates, we obtain the existence of a universal constant$\mathrm { K } _ { 0 } \geq 1$such that

$$
\| v \| _ {\mathrm{C} ^ {3} \left(\mathrm{B} _ {1 / 5}\right)} \leq \mathrm{K} _ {0}, \quad \operatorname{Id} / \mathrm{K} _ {0} \leq \mathrm{D} ^ {2} v \leq \mathrm{K} _ {0} \operatorname{Id} \quad \text { in } \mathrm{B} _ {1 / 5}.\tag{4.13}
$$

In particular, there exists a universal value$\bar { h } > 0$such that, for all$x \in \mathrm { B } _ { 1 / 7 }$,

$$
\mathrm{Q} (x, v, h) := \left\{z: v (z) \leq v (x) + \nabla v (x) \cdot (z - x) + h \right\} \Subset \mathrm{B} _ {1 / 6} \quad \forall h \leq \bar {h}.
$$

• Step 2: Sections ofu are close to sections ofv.

Given$x \in \mathrm { B } _ { 1 / 7 }$and$y \in \partial _ { c } u ( x )$, we define

$$
\mathrm{S} (x, y, u, h) := \left\{z: u (z) \leq u (x) - c (z, y) + c (x, y) + h \right\}.
$$

We claim that, if$\delta _ { 0 }$is small enough, then for all$x \in { \bf B } _ { 1 / 7 } , y \in \partial _ { c } u ( x )$, and$h \leq \bar { h } / 2$, it holds

$$
\mathrm{Q} \left(x, v, h - \mathrm{K} _ {1} \sqrt {\omega \left(\delta_ {0}\right)}\right) \subset \mathrm{S} (x, y, u, h) \subset \mathrm{Q} \left(x, v, h + \mathrm{K} _ {1} \sqrt {\omega \left(\delta_ {0}\right)}\right),\tag{4.14}
$$

where$\mathrm { K } _ { 1 } > 0$is a universal constant.

Let us show the first inclusion. For this, take$x \in \mathbf { B } _ { 1 / 7 } , y \in \partial _ { c } u ( x )$, and define

$$
p _ {x} := - \mathrm{D} _ {x} c (x, y) \in \partial^ {-} u (x).
$$

Since v has universal$\mathrm { C ^ { 2 } }$bounds (see (4.13)) and u is semi-convex (with a universal bound), a simple interpolation argument gives

$$
\left| p _ {x} - \nabla v (x) \right| \leq \mathrm{K} ^ {\prime} \sqrt {\| u - v \| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {1 / 5})}} \leq \mathrm{K} ^ {\prime} \sqrt {\omega (\delta_ {0})} \quad \forall x \in \mathrm{B} _ {1 / 7}.\tag{4.15}
$$

In addition, by (4.9),

$$
\left| y - p _ {x} \right| \leq \left\| \mathrm{D} _ {x} c + \operatorname{Id} \right\| _ {\mathrm{C} ^ {0} \left(\mathrm{B} _ {3} \times \mathrm{B} _ {3}\right)} \leq \delta_ {0},\tag{4.16}
$$

hence

$$
\left| z \cdot p _ {x} + c (z, y) \right| \leq | z \cdot p _ {x} - z \cdot y | + \left| z \cdot y + c (z, y) \right| \leq 2 \delta_ {0} \quad \forall x, z \in \mathrm{B} _ {1 / 7}.\tag{4.17}
$$

Thus,$\mathrm { i f } z \in \mathrm { Q } ( x , v , h - \mathrm { K } _ { 1 } \sqrt { \omega ( \delta _ { 0 } ) } )$, by (4.11), (4.15), and (4.17) we get

$$
\begin{array}{r l} & u (z) \leq v (z) + \omega (\delta_ {0}) \leq v (x) + \nabla v (x) \cdot (z - x) + h - \mathrm{K} _ {1} \sqrt {\omega (\delta_ {0})} + \omega (\delta_ {0}) \\ & \quad \leq u (x) + p _ {x} \cdot z - p _ {x} \cdot x + h - \mathrm{K} _ {1} \sqrt {\omega (\delta_ {0})} + 2 \omega (\delta_ {0}) + 2 \mathrm{K} ^ {\prime} \sqrt {\omega (\delta_ {0})} \\ & \quad \leq u (x) - c (z, y) + c (x, y) + h - \mathrm{K} _ {1} \sqrt {\omega (\delta_ {0})} + 2 \omega (\delta_ {0}) \\ & \quad \quad + 2 \mathrm{K} ^ {\prime} \sqrt {\omega (\delta_ {0})} + 4 \delta_ {0} \\ & \quad \leq u (x) - c (z, y) + c (x, y) + h, \end{array}
$$

provided$\mathrm { K } _ { 1 } > 0$is sufficiently large. This proves the first inclusion, and the second is analogous.

• Step 3: Both the sections ofu and their images are close to ellipsoids with controlled eccentricity, and u is close to a smoothfunction near$x _ { 0 }$

We claim that there exists a universal constant$\mathrm { K _ { 2 } } \geq 1$such that the following holds: For every$\eta _ { 0 } > 0$small, there exist small positive constants$h _ { 0 } = h _ { 0 } ( \eta _ { 0 } )$and$\delta _ { 0 } = \delta _ { 0 } ( h _ { 0 } , \eta _ { 0 } )$ such that, for all$x _ { 0 } \in \mathrm { B } _ { 1 / 7 }$, there is a symmetric matrix A satisfying

$$
\mathrm{Id} / \mathrm{K} _ {2} \leq \mathrm{A} \leq \mathrm{K} _ {2} \mathrm{Id}, \quad \det (\mathrm{A}) = 1,\tag{4.18}
$$

and such that, for all$y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$,

$$
\begin{array}{l} \mathrm{A} \big (\mathrm{B} _ {\sqrt {h _ {0} / 8}} (x _ {0}) \big) \subset \mathrm{S} (x _ {0}, y _ {0}, u, h _ {0}) \subset \mathrm{A} \big (\mathrm{B} _ {\sqrt {8 h _ {0}}} (x _ {0}) \big), \\ \mathrm{A} ^ {- 1} \big (\mathrm{B} _ {\sqrt {h _ {0} / 8}} (y _ {0}) \big) \subset \partial_ {c} u \big (\mathrm{S} (x _ {0}, y _ {0}, u, h _ {0}) \big) \subset \mathrm{A} ^ {- 1} \big (\mathrm{B} _ {\sqrt {8 h _ {0}}} (y _ {0}) \big). \end{array}\tag{4.19}
$$

Moreover

$$
\left\| u - \mathrm{C} _ {x _ {0}, y _ {0}} - \frac {1}{2} \left| \mathrm{A} ^ {- 1} (x - x _ {0}) \right| ^ {2} \right\| _ {\mathrm{C} ^ {0} (\mathrm{A} (\mathrm{B} \sqrt {8 h _ {0}} (x _ {0})))} \leq \eta_ {0} h _ {0},\tag{4.20}
$$

where$\mathrm { C } _ { x _ { 0 } y _ { 0 } }$is a c-support function for u at$x _ { 0 } .$, see (2.3).

In order to prove the claim, take$h _ { 0 } \ll \bar { h }$small (to be fixed) and$\delta _ { 0 } \ll h _ { 0 }$such that $\mathrm { K } _ { 1 } \sqrt { \omega ( \delta _ { 0 } ) } \le h _ { 0 } / 2$, where$\mathrm { K } _ { 1 }$is as in Step 2, so that

$$
\mathrm{Q} (x _ {0}, v, h _ {0} / 2) \subset \mathrm{S} (x _ {0}, y _ {0}, u, h _ {0}) \subset \mathrm{Q} (x _ {0}, v, 3 h _ {0} / 2) \Subset \mathrm{B} _ {1 / 6}.\tag{4.21}
$$

By (4.13) and Taylor formula we get

$$
v (x) = v \left(x _ {0}\right) + \nabla v \left(x _ {0}\right) \cdot \left(x - x _ {0}\right) + \frac {1}{2} \mathrm{D} ^ {2} v \left(x _ {0}\right) \left(x - x _ {0}\right) \cdot \left(x - x _ {0}\right) + \mathrm{O} \left(\left| x - x _ {0} \right| ^ {3}\right),\tag{4.22}
$$

so that defining

$$
\mathrm{E} \left(x _ {0}, h _ {0}\right) := \left\{x: \frac {1}{2} \mathrm{D} ^ {2} v \left(x _ {0}\right) \left(x - x _ {0}\right) \cdot \left(x - x _ {0}\right) \leq h _ {0} \right\}\tag{4.23}
$$

and using (4.13), we deduce that, for every$h _ { 0 }$universally small,

$$
\mathrm{E} (x _ {0}, h _ {0} / 2) \subset \mathrm{Q} (x _ {0}, v, h _ {0}) \subset \mathrm{E} (x _ {0}, 2 h _ {0}).\tag{4.24}
$$

Moreover, always for$h _ { 0 }$small, thanks to (4.22) and the uniform convexity of$v$

$$
\nabla v \left(\mathrm{E} \left(x _ {0}, h _ {0}\right)\right) \subset \mathrm{E} ^ {*} \left(\nabla v \left(x _ {0}\right), 2 h _ {0}\right) \subset \nabla v \left(\mathrm{E} \left(x _ {0}, 3 h _ {0}\right)\right)\tag{4.25}
$$

where we have set

$$
\mathrm{E} ^ {*} (\bar {y}, h _ {0}) := \left\{y: \frac {1}{2} \left[ \mathrm{D} ^ {2} v (\bar {y}) \right] ^ {- 1} (y - \bar {y}) \cdot (y - \bar {y}) \leq h _ {0} \right\}.
$$

By Lemma 4.2, (4.24), and (4.25) applied with 3h in place of$h _ { 0 }$, we deduce that for $\delta _ { 0 } \ll h _ { 0 } \ll \bar { h }$

$$
\partial_ {c} u \left(\mathrm{S} \left(x _ {0}, y _ {0}, u, h _ {0}\right)\right) \subset \mathcal {N} _ {\mathrm{K} ^ {\prime \prime} \sqrt {\omega (\delta_ {0})}} \left(\nabla v \left(\mathrm{E} \left(x _ {0}, 3 h _ {0}\right)\right)\right) \subset \mathrm{E} ^ {*} \left(\nabla v \left(x _ {0}\right), 7 h _ {0}\right).\tag{4.26}
$$

Moreover, by (4.15), if$y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$and we set${ \boldsymbol { p } } _ { x _ { 0 } } : = -  { \mathrm { D } } _ { x } c ( x _ { 0 } , y _ { 0 } )$, then

$$
\left| y _ {0} - \nabla v (x _ {0}) \right| \leq \left| p _ {x _ {0}} - \nabla v (x _ {0}) \right| + \| \mathrm{D} _ {x} c + \mathrm{Id} \| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {3} \times \mathrm{B} _ {3})} \leq \mathrm{K} ^ {\prime} \sqrt {\omega (\delta_ {0})} + \delta_ {0}.
$$

Thus, choosing$\delta _ { 0 }$sufficiently small, it holds

$$
\mathrm{E} ^ {*} \big (\nabla v (x _ {0}), 7 h _ {0} \big) \subset \mathrm{E} ^ {*} (y _ {0}, 8 h _ {0}) \quad \forall y _ {0} \in \partial_ {c} u (x _ {0}).\tag{4.27}
$$

We now want to show that

$$
\mathrm{E} ^ {*} (y _ {0}, h _ {0} / 8) \subset \partial_ {c} u \big (\mathrm{S} (x _ {0}, y _ {0}, u, h _ {0}) \big) \quad \forall y _ {0} \in \partial_ {c} u (x _ {0}).
$$

Observe that, arguing as above, we get

$$
\mathrm{E} ^ {*} \left(y _ {0}, h _ {0} / 8\right) \subset \mathrm{E} ^ {*} \left(\nabla v \left(x _ {0}\right), h _ {0} / 7\right) \quad \forall y _ {0} \in \partial_ {c} u \left(x _ {0}\right)\tag{4.28}
$$

provided$\delta _ { 0 }$is small enough, so it is enough to prove that

$$
\mathrm{E} ^ {*} \big (\nabla v (x _ {0}), h _ {0} / 7 \big) \subset \partial_ {c} u \big (\mathrm{S} (x _ {0}, y _ {0}, u, h _ {0}) \big).
$$

For this, let us define the$c ^ { * }$-convex function$u ^ { c } : \mathrm { B } _ { 3 } \to \mathbf { R }$and the convex function $v ^ { * } : \mathrm { B } _ { 3 } \to \mathbf { R }$as

$$
u ^ {c} (y) := \sup _ {x \in \mathrm{B} _ {1 / 5}} \left\{- c (x, y) - u (x) \right\}, \quad v ^ {*} (y) := \sup _ {x \in \mathrm{B} _ {1 / 5}} \left\{x \cdot y - v (x) \right\}
$$

(see (3.1)). Then it is immediate to check that

$$
\left| u ^ {c} - v ^ {*} \right| \leq \omega (\delta_ {0}) + \delta_ {0} \leq 2 \omega (\delta_ {0}) \quad \text { on } \mathrm{B} _ {3}.\tag{4.29}
$$

Also, in view of (4.13),$v ^ { * }$is a uniformly convex function of class$\mathrm { C ^ { 3 } }$on the open set $\nabla v ( \mathbf { B } _ { 1 / 5 } )$. In addition, since

$$
\mathrm{F} \subset \partial_ {c} u \left(\partial_ {c ^ {*}} u ^ {c} (\mathrm{F})\right) \quad \text {   for   any   set   } \mathrm{F},\tag{4.30}
$$

thanks to (4.21) and (4.24) it is enough to show

$$
\partial_ {c ^ {*}} u ^ {c} \left(\mathrm{E} ^ {*} \left(\nabla v \left(x _ {0}\right), h _ {0} / 7\right)\right) \subset \mathrm{E} \left(x _ {0}, h _ {0} / 4\right).\tag{4.31}
$$

For this, we apply Lemma 4.2 to u<sup>c</sup> and$v ^ { * }$to infer

$$
\begin{array}{c} \partial_ {c ^ {*}} u ^ {c} \big (\mathrm{E} ^ {*} \big (\nabla v (x _ {0}), h _ {0} / 7 \big) \big) \subset \mathcal {N} _ {\mathrm{K} ^ {\prime \prime \prime} \sqrt {\omega (\delta)}} \big (\nabla v ^ {*} \big (\mathrm{E} ^ {*} \big (\nabla v (x _ {0}), h _ {0} / 7 \big) \big) \big) \\ \subset \mathrm{E} (x _ {0}, h _ {0} / 4), \end{array}
$$

where we used that

$$
\nabla v ^ {*} = [ \nabla v ] ^ {- 1} \quad \text { and } \quad \mathrm{D} ^ {2} v ^ {*} \big (\nabla v (x _ {0}) \big) = \big [ \mathrm{D} ^ {2} v (x _ {0}) \big ] ^ {- 1}.
$$

Thus, recalling (4.26), we have proved that there exist$h _ { 0 }$universally small, and$\delta _ { 0 }$small depending on$h _ { 0 }$, such that

$$
\mathrm{E} ^ {*} \left(\nabla v \left(x _ {0}\right), h _ {0} / 7\right) \subset \partial_ {c} u \left(\mathrm{S} \left(x _ {0}, y _ {0}, u, h _ {0}\right)\right) \subset \mathrm{E} ^ {*} \left(\nabla v \left(x _ {0}\right), 7 h _ {0}\right) \quad \forall x _ {0} \in \mathrm{B} _ {1 / 7}.\tag{4.32}
$$

Using (4.21), (4.24), (4.27), and (4.28), this proves (4.19) with$\mathrm { A } : = [ \mathrm { D } ^ { 2 } v ( x _ { 0 } ) ] ^ { - 1 / 2 }$. Also, thanks to (4.12) and (4.13), (4.18) holds.

In order to prove the second part of the claim, we exploit (4.11), (4.9), (4.16), (4.15), (4.22), and (4.18) (recall that$\mathrm { C } _ { x _ { 0 } , y _ { 0 } }$is defined in (2.3) and that$\mathrm { A } = [ \mathrm { D } ^ { 2 } v ( x _ { 0 } ) ] ^ { - 1 / 2 } ) \mathrm { . }$

$$
\begin{array}{l} \left\| u - \mathrm{C} _ {x _ {0}, y _ {0}} - \frac {1}{2} \big | \mathrm{A} ^ {- 1} (x - x _ {0}) \big | ^ {2} \right\| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} \\ = \left\| u - \mathrm{C} _ {x _ {0}, y _ {0}} - \frac {1}{2} \mathrm{D} ^ {2} v (x _ {0}) (x - x _ {0}) \cdot (x - x _ {0}) \right\| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} \\ \leq 2 \| u - v \| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} + \left\| c (x, y _ {0}) + x \cdot y _ {0} \right\| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} \\ \quad + \left\| c (x _ {0}, y _ {0}) + x _ {0} \cdot y _ {0} \right\| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} + \left\| (y _ {0} - p _ {x _ {0}}) \cdot (x - x _ {0}) \right\| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} \\ \quad + \left\| \left(p _ {x _ {0}} - \nabla v (x _ {0})\right) \cdot (x - x _ {0}) \right\| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} \\ \quad + \left\| v - v (x _ {0}) - \nabla v (x _ {0}) \cdot (x - x _ {0}) \right. \\ \quad - \frac {1}{2} \mathrm{D} ^ {2} v (x _ {0}) (x - x _ {0}) \cdot (x - x _ {0}) \Big \| _ {\mathrm{C} ^ {0} (\mathrm{E} (x _ {0}, 8 h _ {0}))} \\ \leq 2 \omega (\delta_ {0}) + 3 \delta_ {0} + \mathrm{K} ^ {\prime} \sqrt {\omega (\delta_ {0})} + \mathrm{K} (\mathrm{K} _ {2} \sqrt {8 h _ {0}}) ^ {3} \leq \eta_ {0} h _ {0}, \end{array}
$$

where the last inequality follows by choosing first$h _ { 0 }$sufficiently small, and then$\delta _ { 0 }$much smaller than$h _ { 0 }$

## • Step 4: Afirst change ofvariables.

Fix$x _ { 0 } \in \mathbf { B } _ { 1 / 7 } , y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$, define$\mathrm { M } : = - \mathrm { D } _ { x y } c ( x _ { 0 } , y _ { 0 } )$, and consider the change ofvariables

$$
\left\{ \begin{array}{l} \bar {x} := x - x _ {0} \\ \bar {y} := \mathrm{M} ^ {- 1} (y - y _ {0}). \end{array} \right.
$$

Notice that, by (4.9), it follows that

$$
\left| \mathrm{M} - \mathrm{Id} \right| + \left| \mathrm{M} ^ {- 1} - \mathrm{Id} \right| \leq 3 \delta_ {0}\tag{4.33}
$$

for$\delta _ { 0 }$sufficiently small. We also define

$$
\begin{array}{c} \bar {c} (\bar {x}, \bar {y}) := c (x, y) - c (x, y _ {0}) - c (x _ {0}, y) + c (x _ {0}, y _ {0}), \\ \bar {u} (\bar {x}) := u (x) - u (x _ {0}) + c (x, y _ {0}) - c (x _ {0}, y _ {0}), \\ \bar {u} ^ {\bar {c}} (\bar {y}) := u ^ {c} (y) - u ^ {c} (y _ {0}) + c (x _ {0}, y) - c (x _ {0}, y _ {0}). \end{array}
$$

Then$\bar { u }$is ¯c-convex,$\bar { u } ^ { \bar { c } }$is$\bar { c } ^ { * }$-convex (where$\bar { c } ^ { * } ( \bar { y } , \bar { x } ) = \bar { c } ( \bar { x } , \bar { y } ) )$, and

$$
\bar {c} (\cdot , \mathbf {0}) = \bar {c} (\mathbf {0}, \cdot) \equiv 0, \quad \mathrm{D} _ {\bar {x} \bar {y}} \bar {c} (\mathbf {0}, \mathbf {0}) = - \operatorname{Id}.\tag{4.34}
$$

We also notice that

$$
\partial_ {\bar {c}} \bar {u} (\bar {x}) = \mathrm{M} ^ {- 1} \left(\partial_ {c} u (\bar {x} + x _ {0}) - y _ {0}\right).\tag{4.35}
$$

Thus, recalling (4.19), and using (4.33) and (4.35), for$\delta _ { 0 }$sufficiently small we obtain

$$
\begin{array}{l} \mathrm{A} (\mathrm{B} _ {\sqrt {h _ {0} / 9}}) \subset \mathrm{S} (\mathbf {0}, \mathbf {0}, \bar {u}, h _ {0}) \subset \mathrm{A} (\mathrm{B} _ {\sqrt {9 h _ {0}}}), \\ \mathrm{A} ^ {- 1} (\mathrm{B} _ {\sqrt {h _ {0} / 9}}) \subset \mathrm{M} ^ {- 1} \mathrm{A} ^ {- 1} (\mathrm{B} _ {\sqrt {h _ {0} / 8}}) \subset \partial_ {\bar {c}} \bar {u} \big (\mathrm{S} (\mathbf {0}, \mathbf {0}, \bar {u}, h _ {0}) \big) \subset \mathrm{M} ^ {- 1} \mathrm{A} ^ {- 1} (\mathrm{B} _ {\sqrt {8 h _ {0}}}) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{4.36}
$$

Since$( \mathrm { T } _ { u } ) _ { \sharp } f = g _ { \sharp }$, it follows that$\mathrm { T } _ { \bar { u } } = \bar { \mathrm { c } } \mathrm { - e x p } ( \nabla \bar { u } )$satisfies

$$
(\mathrm{T} _ {\bar {u}}) _ {\sharp} \bar {f} = \bar {g}, \quad \text {with} \bar {f} (\bar {x}) := f (\bar {x} + x _ {0}), \bar {g} (\bar {y}) := \det (\mathrm{M}) g (\mathrm{M} \bar {y} + y _ {0})
$$

(see for instance the footnote in the proof of Theorem 1.3). Notice that, since$| \mathrm { M } - \mathrm { I d } | \leq$ $\delta _ { 0 } ( \mathrm { b y } ( { \bf 4 . 9 } ) )$, we have$| \mathrm { d e t ( M ) } - 1 | \leq ( 1 + 2 n ) \delta _ { 0 }$(for$\delta _ { 0 }$small), so by (4.8) we get

$$
\| \bar {f} - \mathbf {1} _ {\mathcal {C} _ {1} - x _ {0}} \| _ {\infty} + \| \bar {g} - \mathbf {1} _ {\mathrm{M} ^ {- 1} (\mathcal {C} _ {2} - y _ {0})} \| _ {\infty} \leq 2 (1 + n) \delta_ {0}.\tag{4.37}
$$

• Step 5: A second change of variables and the iteration argument.

We now perform a second change of variable: we set

$$
\left\{ \begin{array}{l} \tilde {x} := \frac {1}{\sqrt {h _ {0}}} \mathrm{A} ^ {- 1} \bar {x}, \\ \tilde {y} := \frac {1}{\sqrt {h _ {0}}} \mathrm{A} \bar {y}, \end{array} \right.\tag{4.38}
$$

and define

$$
c _ {1} (\tilde {x}, \tilde {y}) := \frac {1}{h _ {0}} \bar {c} \bigl (\sqrt {h _ {0}} \mathrm{A} \tilde {x}, \sqrt {h _ {0}} \mathrm{A} ^ {- 1} \tilde {y} \bigr),
$$

$$
u _ {1} (\tilde {x}) := \frac {1}{h _ {0}} \bar {u} \bigl (\sqrt {h _ {0}} \mathrm{A} \tilde {x} \bigr),
$$

$$
u _ {1} ^ {c _ {1}} (\tilde {y}) := \frac {1}{h _ {0}} \bar {u} ^ {\bar {c}} \left(\sqrt {h _ {0}} A ^ {- 1} \tilde {y}\right).
$$

We also define

$$
f _ {1} (\tilde {x}) := \bar {f} \left(\sqrt {h _ {0}} \mathrm{A} \tilde {x}\right), \quad g _ {1} (\tilde {y}) := \bar {g} \left(\sqrt {h _ {0}} \mathrm{A} ^ {- 1} \tilde {y}\right).
$$

Since de$\mathrm { { t } } ( \mathrm { { A } } ) = 1$(see (4.18)), it is easy to check that$( \mathrm { T } _ { u _ { 1 } } ) _ { \sharp } f _ { 1 } = g _ { 1 }$(see the footnote in the proof of Theorem 1.3). Also, since$( \| \mathrm { A } \| + \| \mathrm { A } ^ { - 1 } \| ) \sqrt { h _ { 0 } } \ll 1$, it follows from (4.37) that

$$
\left| f _ {1} - 1 \right| + \left| g _ {1} - 1 \right| \leq 2 (1 + n) \delta_ {0} \quad \text { inside } B _ {3}.\tag{4.39}
$$

Moreover, defining

$$
\mathcal {C} _ {1} ^ {(1)} := \mathrm{S} (\boldsymbol {0}, \boldsymbol {0}, u _ {1}, 1), \quad \mathcal {C} _ {2} ^ {(1)} := \partial_ {c _ {1}} u _ {1} \left(\mathrm{S} (\boldsymbol {0}, \boldsymbol {0}, u _ {1}, 1)\right),
$$

both$\mathcal { C } _ { 1 } ^ { ( 1 ) }$and${ \mathcal { C } } _ { 2 } ^ { ( 1 ) }$are closed, and thanks to (4.36)

$$
\mathrm{B} _ {1 / 3} \subset \mathcal {C} _ {1} ^ {(1)}, \qquad \mathcal {C} _ {2} ^ {(1)} \subset \mathrm{B} _ {3}.\tag{4.40}
$$

Also, since$( \mathrm { T } _ { u _ { 1 } } ) _ { \sharp } f _ { 1 } = g _ { 1 }$, arguing as in the proof of Theorem 1.3 we get

$$
(\mathrm{T} _ {u _ {1}}) _ {\sharp} (f _ {1} \mathbf {1} _ {\mathcal {C} _ {1} ^ {(1)}}) = (g _ {1} \mathbf {1} _ {\mathcal {C} _ {2} ^ {(1)}}),
$$

and by (4.39)

$$
\left\| f _ {1} \mathbf {1} _ {\mathcal {C} _ {1} ^ {(1)}} - \mathbf {1} _ {\mathcal {C} _ {1} ^ {(1)}} \right\| _ {\infty} + \left\| g _ {1} \mathbf {1} _ {\mathcal {C} _ {2} ^ {(1)}} - \mathbf {1} _ {\mathcal {C} _ {2} ^ {(1)}} \right\| _ {\infty} \leq 2 (1 + n) \delta_ {0}.
$$

Finally, by (4.34) and (4.20), it is easy to check that

$$
\left\| c _ {1} (\tilde {x}, \tilde {y}) + \tilde {x} \cdot \tilde {y} \right\| _ {\mathrm{C} ^ {2} (\mathrm{B} _ {3} \times \mathrm{B} _ {3})} \leq \delta_ {0}, \quad \left\| u _ {1} - \frac {1}{2} | \tilde {x} | ^ {2} \right\| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {3})} \leq \eta_ {0}.
$$

This shows that$u _ { 1 }$satisfies the same assumptions as u with$\delta _ { 0 }$replaced by$2 ( 1 + n ) \delta _ { 0 }$ Hence, up to take$\delta _ { 0 }$slightly smaller, we can apply Step 3 to$u _ { 1 }$, and we find a symmetric matrix$\mathrm { A } _ { 1 }$satisfying

$$
\mathrm{Id} / \mathrm{K} _ {2} \leq \mathrm{A} _ {1} \leq \mathrm{K} _ {2} \mathrm{Id}, \quad \det (\mathrm{A} _ {1}) = 1,
$$

$$
\mathrm{A} _ {1} \left(\mathrm{B} _ {\sqrt {h _ {0} / 8}}\right) \subset \mathrm{S} (\mathbf {0}, \mathbf {0}, u _ {1}, h _ {0}) \subset \mathrm{A} _ {1} \left(\mathrm{B} _ {\sqrt {8 h _ {0}}}\right),
$$

$$
\mathrm{A} _ {1} ^ {- 1} \left(\mathrm{B} _ {\sqrt {h _ {0} / 8}}\right) \subset \partial_ {c _ {1}} u _ {1} \left(\mathrm{S} (\boldsymbol {0}, \boldsymbol {0}, u _ {1}, h _ {0})\right) \subset \mathrm{A} _ {1} ^ {- 1} \left(\mathrm{B} _ {\sqrt {8 h _ {0}}}\right),
$$

$$
\left\| u _ {1} - \frac {1}{2} \big | \mathrm{A} _ {1} ^ {- 1} \tilde {x} \big | ^ {2} \right\| _ {\mathrm{C} ^ {0} (\mathrm{A} _ {1} (\mathrm{B} (0, \sqrt {8 h _ {0}}))} \leq \eta_ {0} h _ {0}.
$$

(Here$\mathrm { K _ { 2 } }$and$h _ { 0 }$are as in Step 3.)

This allows us to apply to$u _ { 1 }$the very same construction as the one used above to define$u _ { 1 }$from$\bar { u } \colon$we set

$$
c _ {2} (\tilde {x}, \tilde {y}) := \frac {1}{h _ {0}} c _ {1} \bigl (\sqrt {h _ {0}} \mathrm{A} _ {1} \tilde {x}, \sqrt {h _ {0}} \mathrm{A} _ {1} ^ {- 1} \tilde {y} \bigr), \qquad u _ {2} (\tilde {x}) := \frac {1}{h _ {0}} u _ {1} \bigl (\sqrt {h _ {0}} \mathrm{A} _ {1} \tilde {x} \bigr),
$$

so that$( \mathrm { T } _ { u _ { 2 } } ) _ { \sharp } f _ { 2 } = g _ { 2 }$with

$$
f _ {2} (\tilde {x}) := f _ {1} \left(\sqrt {h _ {0}} \mathrm{A} _ {1} \tilde {x}\right), \quad g _ {2} (\tilde {y}) := \bar {g} \left(\sqrt {h _ {0}} \mathrm{A} _ {1} ^ {- 1} \tilde {y}\right).
$$

Arguing as before, it is easy to check that$u _ { 2 } , c _ { 2 } , f _ { 2 } , g _ { 2 }$satisfy the same assumptions as$u _ { 1 }$ $c _ { 1 } , f _ { 1 } , g _ { 1 }$with exactly the same constants.

So we can keep iterating this construction, defining for any$k \in \mathbf { N }$

$$
c _ {k + 1} (\tilde {x}, \tilde {y}) := \frac {1}{h _ {0}} c _ {k} \left(\sqrt {h _ {0}} \mathrm{A} _ {k} \tilde {x}, \sqrt {h _ {0}} \mathrm{A} _ {k} ^ {- 1} \tilde {y}\right), \quad u _ {k + 1} (\tilde {x}) := \frac {1}{h _ {0}} u _ {k} \left(\sqrt {h _ {0}} \mathrm{A} _ {k} \tilde {x}\right),
$$

where$\mathrm { A } _ { k }$is the matrix constructed in the k-th iteration. In this way, if we set

$$
\mathrm{M} _ {k} := \mathrm{A} _ {k} \cdot \dots \cdot \mathrm{A} _ {1}, \quad \forall k \geq 1,
$$

we obtain a sequence of symmetric matrices satisfying

$$
\mathrm{Id} / \mathrm{K} _ {2} ^ {k} \leq \mathrm{M} _ {k} \leq \mathrm{K} _ {2} ^ {k} \mathrm{Id}, \quad \det (\mathrm{M} _ {k}) = 1,\tag{4.41}
$$

and such that

$$
\mathrm{M} _ {k} \left(\mathrm{B} _ {\left(h _ {0} / 8\right) ^ {k / 2}}\right) \subset \mathrm{S} \left(\mathbf {0}, \mathbf {0}, u _ {k}, h _ {0} ^ {k}\right) \subset \mathrm{M} _ {k} \left(\mathrm{B} _ {\left(8 h _ {0}\right) ^ {k / 2}}\right).\tag{4.42}
$$

• Step$\delta \colon \mathrm { C } ^ { 1 , \beta }$regularity.

We now show that, for any$\beta \in ( 0 , 1 )$, we can choose$h _ { 0 }$and$\delta _ { 0 } = \delta _ { 0 } ( h _ { 0 } )$small enough so that$u _ { 1 }$is$\mathrm { C } ^ { 1 , \beta }$at the origin (here$u _ { 1 }$is the function constructed in the previous step).

This will imply that u is$\mathrm { C } ^ { 1 , \beta }$at$x _ { 0 }$with universal bounds, which by the arbitrariness of $x _ { 0 } \in \mathrm { B } _ { 1 / 7 }$gives$u \in \mathrm { C } ^ { 1 , \beta } ( \mathbf { B } _ { 1 / 7 } )$

Fix$\beta \in ( 0 , 1 )$. Then by (4.41) and (4.42) we get

$$
\mathrm{B} _ {(\sqrt {h _ {0}} / (\sqrt {8} \mathrm{K} _ {2})) ^ {k}} \subset \mathrm{S} \bigl (\mathbf {0}, \mathbf {0}, u _ {1}, h _ {0} ^ {k} \bigr) \subset \mathrm{B} _ {(\mathrm{K} _ {2} \sqrt {8 h _ {0}}) ^ {k}},\tag{4.43}
$$

so defining$r _ { 0 } : = \sqrt { h _ { 0 } } / ( \sqrt { 8 } \mathrm { K } _ { 2 } )$we obtain

$$
\| u _ {1} \| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {r _ {0} ^ {k}})} \leq h _ {0} ^ {k} = \left(\sqrt {8} \mathrm{K} _ {2} r _ {0}\right) ^ {2 k} \leq r _ {0} ^ {(1 + \beta) k},
$$

provided$h _ { 0 }$(and so$r _ { 0 } )$is sufficiently small. This implies the$\mathrm { C } ^ { 1 , \beta }$regularity of$u _ { 1 }$at$\mathbf { 0 } ,$ concluding the proof.-

Remark 4.4 (Local to global principle). — If u is differentiable at x and c satisfies (C0)– (C1), then every “local support” at x is also a “global c-support” at$x ,$that is,$\partial _ { c } u ( x ) =$ $\mathrm { c } { \cdot } \mathrm { e x p } _ { x } ( \partial ^ { - } u ( x ) )$. To see this, just notice that

$$
\emptyset \neq \partial_ {c} u (x) \subset \mathrm{c} - \exp_ {x} \left(\partial^ {-} u (x)\right) = \left\{\mathrm{c} - \exp_ {x} (\nabla u (x)) \right\}
$$

(recall (2.6)), so necessarily the two sets have to coincide.

Corollary 4.5. — Let u be as in Theorem 4.3. Then u is strictly c-convex in$\mathrm { B } _ { 1 / 7 }$. More precisely, for every$\gamma > 2$there exist$\eta _ { 0 } , \delta _ { 0 } > 0$depending only on$\gamma$such that, if the hypotheses of Theorem 4.3 are satisfied, then,for all$x _ { 0 } \in { \bf B } _ { 1 / 7 } , y _ { 0 } \in \partial _ { c } u ( x _ { 0 } )$, and$\mathrm { C } _ { x _ { 0 } , y _ { 0 } }$as in (2.3), we have

$$
\inf _ {\partial \mathrm{B} _ {r} (x _ {0})} \left\{u - \mathrm{C} _ {x _ {0}, y _ {0}} \right\} \geq c _ {0} r ^ {\gamma} \quad \forall r \leq \operatorname{dist} (x _ {0}, \partial \mathrm{B} _ {1 / 7}),\tag{4.44}
$$

with$c _ { 0 } > 0$universal.

Proof. — With the same notation as in the proof of Theorem 4.3, it is enough to show that

$$
\inf _ {\partial \mathrm{B} _ {r}} u _ {1} \geq r ^ {1 / \beta},
$$

where$u _ { 1 }$is the function constructed in Step 5 of the proof of Theorem 4.3. Defining $\varrho _ { \mathrm { 0 } } : = \mathrm { K _ { 2 } } \sqrt { 8 h _ { 0 } }$, it follows from (4.43) that

$$
\inf _ {\partial \mathrm{B} _ {\varrho_ {0} ^ {k}}} u _ {1} \geq h _ {0} ^ {k} = \left(\varrho_ {0} / \left(\sqrt {8} \mathrm{K} _ {2}\right)\right) ^ {2 k} \geq \varrho_ {0} ^ {\gamma k},
$$

provided$h _ { 0 }$is small enough.

A simple consequence of the above results is the following:

Corollary 4.6. — Let u be as in Theorem 4.3, then$\mathrm { T } _ { u } ( \mathbf { B } _ { 1 / 7 } )$is open.

Proof. — Since$u \in \mathrm { C } ^ { 1 , \beta } ( \mathbf { B } _ { 1 / 7 } )$we have that$\mathrm { T } _ { u } ( \mathrm { B } _ { 1 / 7 } ) = \partial _ { c } u ( \mathrm { B } _ { 1 / 7 } )$(see Remark 4.4). We claim that it is enough to show that$\mathrm { i f } \ y _ { 0 } \in \partial _ { c } u ( { \bf B } _ { 1 / 7 } )$, then there exists$\varepsilon = \varepsilon ( y _ { 0 } ) > 0$ small such that, for all$\vert y - y _ { 0 } \vert < \varepsilon .$, the function$u ( \cdot ) + c ( \cdot , y )$has a local minimum at some point$\bar { x } \in \mathrm { B } _ { 1 / 7 }$. Indeed, if this is the case, then

$$
\nabla u (\bar {x}) = - \mathrm{D} _ {x} c (\bar {x}, y),
$$

and so$y \in \partial _ { c } u ( \bar { x } )$(by Remark 4.4), hence$\mathbf { B } _ { \varepsilon } ( y _ { 0 } ) \subset \mathrm { T } _ { u } ( \mathbf { B } _ { 1 / 7 } )$

To prove the above fact, fix$r > 0$such that$\mathbf { B } _ { r } ( x _ { 0 } ) \subset \mathbf { B } _ { 1 / 7 }$, and pick x¯ a point in $\overline { { \mathbf { B } } } _ { r } ( x _ { 0 } )$where the function$u ( \cdot ) + c ( \cdot , y )$attains its minimum, i.e.,

$$
\bar {x} \in \underset {\overline {{\mathrm{B}}} _ {r} (x _ {0})} {\operatorname{argmin}} \bigl \{u (x) + c (x, y) \bigr \}.
$$

Since, by (4.44),

$$
\begin{array}{c} \min _ {x \in \partial \mathrm{B} _ {r} (x _ {0})} \bigl \{u (x) + c (x, y) \bigr \} \geq \min _ {x \in \partial \mathrm{B} _ {r} (x _ {0})} \bigl \{u (x) + c (x, y _ {0}) \bigr \} - \varepsilon \| c \| _ {\mathrm{C} ^ {1}} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}
$$

while

$$
u (x _ {0}) + c (x _ {0}, y) \leq c (x _ {0}, y _ {0}) + u (x _ {0}) + \varepsilon \| c \| _ {\mathrm{C} ^ {1}},
$$

choosing$\begin{array} { r } { \varepsilon < \frac { c _ { 0 } } { 2 \| c \| _ { C ^ { 1 } } } r ^ { \gamma } } \end{array}$we obtain that$\bar { x } \in \mathbf { B } _ { r } ( x _ { 0 } ) \subset \mathbf { B } _ { 1 / 7 }$. This implies that$\bar { x }$is a local minimum for$u ( \cdot ) + c ( \cdot , y )$C, concluding the proof.-

## 5. Comparison principle and$\mathbf { C } ^ { 2 , \alpha }$regularity

We begin this section with a change of variable formula for the c-exponential map.

Lemma 5.1. — Let Ω be an open set,$v \in \mathrm { C } ^ { 2 } ( \varOmega )$, and assume that$\nabla \boldsymbol { v } ( \boldsymbol { \mathcal { Q } } ) \subset$Domc- exp and that

$$
\mathrm{D} ^ {2} v (x) + \mathrm{D} _ {x x} c \left(x, \mathrm{c} - \exp_ {x} (\nabla v (x))\right) \geq 0 \quad \forall x \in \Omega .
$$

Then, for every Borel set$\mathrm { A } \subset \varOmega$,

$$
\left| \mathrm{c} - \exp (\nabla v (\mathrm{A})) \right| \leq \int_ {\mathrm{A}} \frac {\det (\mathrm{D} ^ {2} v (x) + \mathrm{D} _ {x x} c (x , \mathrm{c} - \exp_ {x} (\nabla v (x))))}{| \det (\mathrm{D} _ {x y} c (x , \mathrm{c} - \exp_ {x} (\nabla v (x)))) |} d x.
$$

In addition, if the map$x \mapsto \mathbf { c } \ – \exp _ { x } ( \nabla v ( x ) )$is injective, then equality holds.

Proof. — The result follows from a direct application of the Area Formula [12, Section 3.3.2, Theorem 1] once one notices that, differentiating the identity

$$
\nabla v (x) = - \mathrm{D} _ {x} c \left(x, \mathrm{c} - \exp_ {x} (\nabla v (x))\right)
$$

(see (2.5)), the Jacobian determinant of the$\mathrm { C } ^ { 1 }$map$x \mapsto \mathrm { c } { \mathrm { - } } \mathrm { e x p } _ { x } ( \nabla v ( x ) )$is given precisely by

$$
\frac {\det (\mathrm{D} ^ {2} v (x) + \mathrm{D} _ {x x} c (x , \mathrm{c} - \exp_ {x} (\nabla v (x))))}{| \det (\mathrm{D} _ {x y} c (x , \mathrm{c} - \exp_ {x} (\nabla v (x)))) |}.
$$

In the next proposition we show a comparison principle between$\mathrm { C ^ { 1 } }$c-convex functions and smooth solutions to the Monge-Ampère equation.<sup>4</sup> As already mentioned at the beginning of Section 4 (see also Remark 4.4), the$\mathrm { C ^ { 1 } }$regularity of u is crucial to ensure that the c-subdifferential coincides with its local counterpart$\mathrm { c - e x p } ( \partial ^ { - } u )$

Here and in the sequel, we use co[E] to denote the convex hull of a set E. Also, recall that$\mathcal { N } _ { r } ( \mathrm { E } )$denotes the r-neighborhood of E.

Proposition 5.2 (Comparison principle). — Let u be a c-convexfunction ofclass$\mathrm { C } ^ { 1 }$inside the set$\mathrm { S } : = \{ u < 1 \}$, and assume that$u ( \mathbf { 0 } ) = 0 , \mathbf { B } _ { \mathrm { 1 / K } } \subset \mathbf { S } \subset \mathbf { B } _ { \mathrm { K } }$, and that$\nabla u ( \mathrm { S } ) \Subset$Dom- exp. Let $f , g$be two densities such that

$$
\| f / \lambda_ {1} - 1 \| _ {\mathrm{C} ^ {0} (\mathrm{S})} + \| g / \lambda_ {2} - 1 \| _ {\mathrm{C} ^ {0} (\mathrm{T} _ {u} (\mathrm{S}))} \leq \varepsilon\tag{5.1}
$$

for some constants$\lambda _ { 1 } , \lambda _ { 2 } \in ( 1 / 2 , 2 )$and$\varepsilon \in ( 0 , 1 / 4 )$, and assume that$( \mathrm { T } _ { u } ) _ { \sharp } f = g$. Furthermore, suppose that

$$
\| c + x \cdot y \| _ {\mathrm{C} ^ {2} (\mathrm{B} _ {\mathrm{K}} \times \mathrm{B} _ {\mathrm{K}})} \leq \delta .\tag{5.2}
$$

Then there exist a universal constant$\gamma \in ( 0 , 1 )$, and$\delta _ { 1 } = \delta _ { 1 } ( \mathrm { K } ) > 0$small, such that thefollowing holds: Let v be the solution of

$$
\left\{ \begin{array}{l l} \det (\mathrm{D} ^ {2} v) = \lambda_ {1} / \lambda_ {2} & i n   \mathcal {N} _ {\delta^ {\gamma}} (\operatorname{co} [ \mathrm{S} ]), \\ v = 1 & o n   \partial (\mathcal {N} _ {\delta^ {\gamma}} (\operatorname{co} [ \mathrm{S} ])). \end{array} \right.
$$

Then

$$
\| u - v \| _ {\mathrm{C} ^ {0} (\mathrm{S})} \leq \mathrm{C} _ {\mathrm{K}} \left(\varepsilon + \delta^ {\gamma / n}\right) \quad p r o v i d e d \delta \leq \delta_ {1},\tag{5.3}
$$

where$\mathrm { C } _ { \mathrm { K } }$is a constant independent of$\lambda _ { 1 } , \lambda _ { 2 } , \varepsilon _ { \mathrm { { ; } } }$, and δ (but which depends on$\mathrm { K } )$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">c(x,y) = |x − y|<sup>p</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup> A similar result for the case appeared in [7, Theorem 6.2]. Here, however, we have to deal with some additional difficulties due to the fact that the c-exponential map is not necessarily defined on the whole R<sup>n</sup>.</span></small>

Proof. — First of all we observe that, since$u ( \mathbf { 0 } ) = 0 , u = 1 { \mathrm { ~ o n ~ } } \partial \mathrm { S , ~ S \subset B _ { K } }$, and $\| c + x \cdot y \| _ { \mathrm { C ^ { 2 } ( B _ { K } ) } } \le \delta \ll 1$, it is easy to check that there exists a universal constant$a _ { 1 } > 0$ such that

$$
\left| \mathrm{D} _ {x} c (x, y) \right| \geq a _ {1} \quad \forall x \in \partial \mathrm{S}, y = \mathrm{c} - \exp_ {x} (\nabla u (x)).\tag{5.4}
$$

Thanks to (5.4) and$( 5 . 2 ) ,$it follows from the Implicit Function Theorem that, for each $x \in \partial \mathrm { S }$, the boundary of the set

$$
\mathrm{E} _ {x} := \left\{z \in \mathrm{B} _ {\mathrm{K}}: c (z, y) - c (x, y) + u (x) \leq 1 \right\}
$$

is of class$\mathrm { C ^ { 2 } }$inside$\mathrm { B _ { K } }$, and its second fundamental form is bounded by$\mathrm { C } _ { \mathrm { K } } \delta$, where $\mathrm { C } _ { \mathrm { K } } > 0$depends only on K. Hence, since S can be written as

$$
\mathrm{S} := \bigcap_ {x \in \partial \mathrm{S}} \mathrm{E} _ {x},
$$

it follows that

$$
\mathrm{Sis} (\mathrm{C} _ {\mathrm{K}} \delta) \text {-semiconvexset},
$$

that is, for any couple of points$x _ { 0 } , x _ { 1 } \in \mathrm { S }$the ball centered at$x _ { 1 / 2 } : = ( x _ { 0 } + x _ { 1 } ) / 2$of radius $\mathrm { C } _ { \mathrm { K } } \delta | x _ { 1 } - x _ { 0 } | ^ { 2 }$intersects S. Since$\mathrm { ~ S ~ C ~ B _ { K } ~ }$, this implies that co$[ \mathrm { S } ] \subset \mathcal { N } _ { \mathrm { C } _ { \mathrm { K } } ^ { \prime } \delta } ( \mathrm { S } )$for some positive constant$\mathrm { C _ { K } ^ { \prime } }$depending only on K. Thus, for any$\gamma \in ( 0 , 1 )$we obtain

$$
\mathcal {N} _ {\delta^ {\gamma}} \left(\operatorname{co} [ S ]\right) \subset \mathcal {N} _ {(1 + C _ {K} ^ {\prime}) \delta^ {\gamma}} (S).
$$

Since$v = 1$on$\partial ( \mathcal { N } _ { \delta ^ { \gamma } } ( \mathrm { c o } [ \mathrm { S } ] ) )$and$\lambda _ { 1 } / \lambda _ { 2 } \in ( 1 / 4 , 4 )$, by standard interior estimates for solution of the Monge-Ampère equation with constant right hand side (see for instance [8, Lemma 1.1]), we obtain

(5.5)

$$
\underset {\mathrm{S}} {\mathrm{osc}}   v \leq \mathrm{C} _ {\mathrm{K}} ^ {\prime \prime}\tag{5.6}
$$

$$
1 - \mathrm{C} _ {\mathrm{K}} ^ {\prime \prime} \delta^ {\gamma / n} \leq v <   1 \quad \text { on } \partial \mathrm{S},\tag{5.7}
$$

$$
\mathrm{D} ^ {2} v \geq \delta^ {\gamma / \tau} \mathrm{Id} / \mathrm{C} _ {\mathrm{K}} ^ {\prime \prime} \quad \text { in   co[S], }
$$

for some$\tau > 0$universal, and some constant$\mathrm { C _ { K } ^ { \prime \prime } }$depending only on K.

Let us define

$$
v ^ {+} := \big (1 + 4 \varepsilon + 2 \sqrt {\delta} \big) v - 4 \varepsilon - 2 \sqrt {\delta},
$$

$$
v ^ {-} := \big (1 - 4 \varepsilon - \sqrt {\delta} / 2 \big) v + 4 \varepsilon + \sqrt {\delta} / 2 + 2 \mathrm{C} _ {\mathrm{K}} ^ {\prime \prime} \delta^ {\gamma / n}.
$$

Our goal is to show that we can choose$\gamma$universally small so that$v ^ { - } \geq u \geq v ^ { + }$on${ \mathrm { S } } .$ Indeed, if we can do so, then by (5.5) this will imply (5.3), concluding the proof.

First of all notice that, thanks to (5.6),$v ^ { - } > u > v ^ { + }$on ∂S. Let us show first that $v ^ { + } \leq v$

Assume by contradiction this is not the case. Then, since$u > v ^ { + }$on ∂S,

$$
\emptyset \neq \mathrm{Z} := \left\{u <   v ^ {+} \right\} \Subset \mathrm{S}.
$$

Since$v ^ { + }$is convex, taking any supporting plane to$v ^ { + }$at$x \in Z .$, moving it down and then lifting it up until it touches u from below, we deduce that

$$
\nabla v ^ {+} (\mathbf {Z}) \subset \nabla u (\mathbf {Z})\tag{5.8}
$$

(recall that both u and$v ^ { + }$are of class$\mathrm { C } ^ { 1 } )$, thus by Remark 4.4

$$
\left| \mathrm{c} - \exp \left(\nabla v ^ {+} (\mathrm{Z})\right) \right| \leq \left| \mathrm{T} _ {u} (\mathrm{Z}) \right|.\tag{5.9}
$$

We show that this is impossible. For this, using (5.7) and choosing$\gamma : = \tau / 4$, for any$x \in Z$ we compute

$$
\begin{array}{l} \mathrm{D} ^ {2} v ^ {+} (x) + \mathrm{D} _ {x x} c \big (x, \mathrm{c} - \exp_ {x} \big (\nabla v ^ {+} (x) \big) \big) \\ \geq \big (1 + \sqrt {\delta} + 4 \varepsilon \big) \mathrm{D} ^ {2} v + \sqrt {\delta} \mathrm{D} ^ {2} v - \delta   \mathrm{Id} \\ \geq \big (1 + \sqrt {\delta} + 4 \varepsilon \big) \mathrm{D} ^ {2} v + \big (\delta^ {3 / 4} / \mathrm{C} _ {\mathrm{K}} ^ {\prime \prime} - \delta \big)   \mathrm{Id} \\ \geq \big (1 + \sqrt {\delta} + 4 \varepsilon \big) \mathrm{D} ^ {2} v, \end{array}
$$

provided δ is sufficiently small, the smallness depending only on K. Thus, thanks (5.2) we have

$$
\begin{array}{r l} \frac {\det (\mathrm{D} ^ {2} v ^ {+} (x) + \mathrm{D} _ {x x} c (x , \mathrm{c} - \exp_ {x} (\nabla v ^ {+} (x))))}{| \det (\mathrm{D} _ {x y} c (x , \mathrm{c} - \exp_ {x} (\nabla v ^ {+} (x)))) |} & \geq \frac {\det ((1 + \sqrt {\delta} + 4 \varepsilon) \mathrm{D} ^ {2} v)}{1 + \delta} \\ & \geq \left(1 + \sqrt {\delta} + 4 \varepsilon\right) ^ {n} (1 - 2 \delta) \frac {\lambda_ {1}}{\lambda_ {2}} \\ & \geq (1 + 4 n \varepsilon) \frac {\lambda_ {1}}{\lambda_ {2}}. \end{array}
$$

In addition, thanks (5.7) and (5.2), since$\delta ^ { \gamma / \tau } = \delta ^ { 1 / 4 } \gg \delta$we see that

$$
\mathrm{D} ^ {2} v ^ {+} > \| \mathrm{D} _ {x x} c \| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {\mathrm{K}} \times \mathrm{B} _ {\mathrm{K}})} \operatorname{Id} \quad \text { inside   co[S] }.
$$

Hence, for any$x , z \in { \mathrm { Z } } , x \neq z$and$\begin{array} { r } { y = \mathrm { c } { - } \mathrm { e x p } _ { x } ( \nabla v ^ { + } ( x ) ) } \end{array}$(notice that$\mathrm { c - e x p } _ { x } ( \nabla v ^ { + } ( x ) )$is well-defined because of (5.8) and the assumption$\nabla u ( \mathrm { S } ) \Subset \mathrm { D o m c - e x p } )$, it follows

$$
\begin{array}{l} v ^ {+} (z) + c (z, y) \geq v ^ {+} (x) + c (x, y) + \frac {1}{2} \int_ {0} ^ {1} \big (\mathrm{D} ^ {2} v ^ {+} \big (t z + (1 - t) x \big) \\ \qquad \qquad + \mathrm{D} _ {x x} c \big (t z + (1 - t) x, y \big) \big) [ z - x, z - x ]   d t \\ > v ^ {+} (x) + c (x, y), \end{array}
$$

where we used that$\nabla v ^ { + } ( x ) + \mathrm { D } _ { x } c ( x , y ) = 0$. This means that the supporting function $\ z \mapsto - c ( z , y ) + c ( x , y ) + v ^ { + } ( x )$can only touch$v ^ { + }$from below at x, which implies that the map$\mathrm { Z } \ni x \mapsto \mathrm { c } \mathrm { - e x p } _ { x } ( \nabla v ^ { + } ( x ) )$is injective. Thus, by Lemma 5.1 we get

$$
\left| \mathrm{c} - \exp \bigl (\nabla v ^ {+} (\mathrm{Z}) \bigr) \right| \geq (1 + 4 n \varepsilon) \frac {\lambda_ {1}}{\lambda_ {2}} | \mathrm{Z} |.\tag{5.10}
$$

On the other hand, since u is$\mathrm { C } ^ { 1 }$, it follows from$( \mathrm { T } _ { u } ) _ { \sharp } f = g$and (5.1) that

$$
\left| \mathrm{T} _ {u} (\mathrm{Z}) \right| = \int_ {\mathrm{Z}} \frac {f (x)}{g \left(\mathrm{T} _ {u} (x)\right)} d x \leq \frac {\lambda_ {1} (1 + \varepsilon)}{\lambda_ {2} (1 - \varepsilon)} | \mathrm{Z} | \leq (1 + 3 \varepsilon) \frac {\lambda_ {1}}{\lambda_ {2}} | \mathrm{Z} |.
$$

This estimate combined with (5.10) shows that (5.9) is impossible unless Z is empty. This proves that$v ^ { + } \leq u$

The proof of the inequality$v ^ { - } \leq u$follows by the same argument except for a minor modification. More precisely, let us assume by contradiction that$\mathrm { W } : = \{ u > v ^ { - } \}$ is nonempty. In order to apply the previous argument we would need to know that $\nabla v ^ { - } ( \mathrm { W } ) \subset \mathrm { D o m c - e x p }$. However, since the gradient of v can be very large near ∂S, this may be a problem.

To circumvent this issue we argue as follows: since W is nonempty, there exists a positive constant$\bar { \mu }$such that u touches${ v ^ { - } + \bar { \mu } }$from below inside S. Let E be the contact set, i.e.,$\mathrm { E } : = \{ u = v ^ { - } + \bar { \mu } \}$. Since both u and$v ^ { - }$are$\mathrm { C } ^ { 1 }$,$\nabla \boldsymbol { u } = \nabla \boldsymbol { v } ^ { - }$on E. Thus, if$\eta > 0$ is small enough, then the set$\mathrm { W } _ { \eta } : = \{ u > v ^ { - } + \bar { \mu } - \eta \}$is nonempty and$\nabla \boldsymbol { v } ^ { - } ( \mathbf { W } _ { \eta } )$is contained in a small neighborhood of$\nabla u ( \mathbf { W } _ { \eta } )$, which is compactly contained in Domc-exp. At this point, one argues exactly as in the first part of the proof, with$\mathrm { W } _ { \eta }$in place of$\mathrm { ^ { - } Z } _ { \mathrm { ^ { + } } }$, to find a contradiction.-

Theorem 5.3. — Let$u , f , g , \eta _ { 0 } , \delta _ { 0 }$be as in Theorem 4.3, and assume in addition that$c \in$ $\mathrm { C } ^ { k , \alpha } ( \mathbf { B } _ { 3 } \times \mathbf { B } _ { 3 } )$and$f , g \in \mathrm { C } ^ { k , \alpha } ( \mathbf { B } _ { 1 / 3 } )$for some$k \geq 0$and$\alpha \in ( 0 , 1 )$. There exist small constants $\eta _ { 1 } \leq \eta _ { 0 }$and$\delta _ { 1 } \leq \delta _ { 0 }$such that, if

(5.11)

$$
\| f - \mathbf {1} _ {\mathcal {C} _ {1}} \| _ {\infty} + \| g - \mathbf {1} _ {\mathcal {C} _ {2}} \| _ {\infty} \leq \delta_ {1},\tag{5.12}
$$

$$
\left\| c (x, y) + x \cdot y \right\| _ {\mathrm{C} ^ {2} \left(\mathrm{B} _ {3} \times \mathrm{B} _ {3}\right)} \leq \delta_ {1},
$$

and

$$
\left\| u - \frac {1}{2} | x | ^ {2} \right\| _ {\mathrm{C} ^ {0} (\mathrm{B} _ {3})} \leq \eta_ {1},\tag{5.13}
$$

then$u \in { \mathrm { C } } ^ { k + 2 , \alpha } ( { \mathbf { B } } _ { 1 / 9 } )$

Proof. — We divide the proof in two steps.

• Step$I { \cdot } \mathrm { C } ^ { 1 , 1 }$regularity.

Fix a point$x _ { 0 } \in \mathrm { B } _ { 1 / 8 }$, and set$y _ { 0 } : = \mathrm { c } \mathrm { - e x p } _ { x _ { 0 } } ( \nabla u ( x _ { 0 } ) )$. Up to replace u (resp. c) with the function$u _ { 1 }$(resp.$c _ { 1 } )$constructed in Steps 4 and 5 in the proof of Theorem 4.3, we can assume that$u \geq 0 , u ( \mathbf { 0 } ) = 0$, that

$$
\mathrm{S} _ {h} := \mathrm{S} (\mathbf {0}, \mathbf {0}, u, h) = \{u \leq h \},
$$

and that

$$
\mathrm{D} _ {x y} c (\mathbf {0}, \mathbf {0}) = - \operatorname{Id}.\tag{5.14}
$$

Under these assumptions we will show that the sections of u are of “good shape”, i.e.,

$$
\mathrm{B} _ {\sqrt {h} / \mathrm{K}} \subset \mathrm{S} _ {h} \subset \mathrm{B} _ {\mathrm{K} \sqrt {h}} \quad \forall h \leq h _ {1},\tag{5.15}
$$

for some universal$h _ { 1 }$and K. Arguing as in Step 6 of Theorem 4.3, this will give that u is $\mathrm { C ^ { 1 , 1 } }$at the origin, and thus at every point in$\mathrm { { B } _ { 1 / 8 } }$

First ofall notice that, thanks to (5.13), for any$h _ { 1 } > 0$we can choose$\eta _ { 1 } = \eta _ { 1 } ( h _ { 1 } ) >$ 0 small enough such that (5.15) holds for$\mathrm { S } _ { h _ { 1 } }$with$\mathrm { K } = 2$. Hence, assuming without loss of generality that$\delta _ { 1 } \leq 1$, we see that

$$
\mathrm{B} _ {\sqrt {h _ {1}} / 3} \subset \mathcal {N} _ {\delta_ {1} ^ {\gamma} \sqrt {h _ {1}}} \bigl (\mathrm{co} [ \mathrm{S} _ {h _ {1}} ] \bigr) \subset \mathrm{B} _ {3 \sqrt {h _ {1}}},
$$

where$\gamma$is the exponent from Proposition 5.2. Let$v _ { 1 }$solve the Monge-Ampère equation

$$
\left\{ \begin{array}{l l} \det (\mathrm{D} ^ {2} v _ {1}) = f (\mathbf {0}) / g (\mathbf {0}) & \text { in } \mathcal {N} _ {\delta_ {1} ^ {\gamma} \sqrt {h _ {1}}} (\operatorname{co} [ \mathrm{S} _ {h _ {1}} ]), \\ v _ {1} = h _ {1} & \text { on } \partial \mathcal {N} _ {\delta_ {1} ^ {\gamma} \sqrt {h _ {1}}} (\operatorname{co} [ \mathrm{S} _ {h _ {1}} ]). \end{array} \right.
$$

Since$\mathbf { B } _ { 1 / 3 } \subset \mathrm { N } _ { \delta _ { 1 } ^ { \gamma } \sqrt { h _ { 1 } } } ( \mathrm { c o } [ \mathrm { S } _ { h _ { 1 } } ] ) / \sqrt { h _ { 1 } } \subset \mathrm { B } _ { 3 }$, by standard Pogorelov estimates applied to the function$v _ { 1 } ( \sqrt { h _ { 1 } } x ) / h _ { 1 }$(see for instance [26, Theorem 4.2.1]), it follows that$| \mathrm { D } ^ { 2 } v _ { 1 } ( 0 ) | \le$ M, with$\mathbf M > 0$some large universal constant.

Let$h _ { k } : = h _ { 1 } 2 ^ { - k }$and define$\bar { \mathrm { K } } \geq 3$to be the largest number such that any solution w of

$$
\left\{ \begin{array}{l l} \det (\mathrm{D} ^ {2} w) = f (\mathbf {0}) / g (\mathbf {0}) & \text {in Z}, \\ w = 1 & \text {on} \partial Z, \end{array} \right. \quad \text {with B_{1/ \bar {K}} \subset Z\subset B_{\bar {K}} ,}\tag{5.16}
$$

satisfies$| \mathrm { D } ^ { 2 } w ( 0 ) | \le \mathrm { M } + 1 . ^ { 5 }$We prove by induction that (5.15) holds with$\mathrm { K } = \bar { \mathrm { K } }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">K¯</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i.e., 3 ≤ K<sup>¯</sup> < ∞)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|D<sup>2</sup>w(0)|</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>K</sub>¯ <sub>≤</sub> √<sub>2(M + 1)</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup> The fact that is well defined follows by the following facts: first of all, by definition, M is an a-priori bound for whenever w is a solution of (5.16) with B ⊂ Z ⊂ B , so K<sup>¯</sup> ≥ 3. On the other handB1/3 ⊂ Z ⊂ B3, so K ≥ 3. Indeed, since 1/2 ≤f(0)/g(0) ≤ 2 (by (5.11)) and , the function1/2 ≤f(0)/g(0) ≤ 2 (by (5.11))M ≥ 1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">is a solution of (5.16) such that B<sub>1/</sub>√<sub>2(M+1)</sub> ⊂ B <sub>/</sub>√ <sub>+</sub> ⊂ { ¯w ≤ 1} ⊂ B√<sub>2(M+1)</sub> and |D<sup>2</sup>w(¯ 0)| = 2(M + 1).B1/√2(M+1) ⊂ B1/√M+1 ⊂ {⑩ ≤ 1} ⊂ B√2(M+1) and |D2ω(0)| = 2(M + 1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f (0)x<sup>2</sup> w¯ := (M + 1)x<sup>2</sup> ++ x<sup>2</sup> + · · · + x<sup>2</sup> g(0) M + 1</span></small>

If$\dot { h } = h _ { 1 }$then we already know that (5.15) holds with$\mathrm { K } = 2$(and so with$\mathrm { K } = \bar { \mathrm { K } } )$

Assume now that (5.15) holds with$h = h _ { k }$and$\mathrm { K } = \bar { \mathrm { K } }$, and we want to show that it holds with$h = h _ { k + 1 }$. For this, for any$k \in \mathbf { N }$we consider$u _ { k }$the solution of

$$
\left\{ \begin{array}{l l} \det (\mathrm{D} ^ {2} v _ {k}) = f (\mathbf {0}) / g (\mathbf {0}) & \text {in} \mathcal {N} _ {\delta_ {k} ^ {\gamma} \sqrt {h _ {k}}} (\operatorname{co} [ \mathrm{S} _ {h _ {k}} ]), \\ v _ {k} = h _ {1} 2 ^ {- k} & \text {on} \partial \mathrm{N} _ {\delta_ {k} ^ {\gamma} \sqrt {h _ {k}}} (\operatorname{co} [ \mathrm{S} _ {h _ {k}} ]), \end{array} \right.
$$

where

$$
\delta_ {k} := \left\| c (x, y) + x \cdot y \right\| _ {\mathrm{C} ^ {2} (\mathrm{S} _ {h _ {k}} \times \mathrm{T} _ {u} (\mathrm{S} _ {h _ {k}}))} \leq \delta_ {1}.
$$

Let us consider the rescaled functions

$$
\bar {u} _ {k} (x) := u \left(\sqrt {h _ {k}} x\right) / h _ {k}, \quad \bar {v} _ {k} (x) := v _ {k} \left(\sqrt {h _ {k}} x\right) / h _ {k}.
$$

Since by the inductive hypothesis$\mathbf { B } _ { 1 / \bar { \mathrm { K } } } \subset \bar { \mathrm { S } } _ { k } : = \{ \bar { u } _ { k } \leq 1 \} \subset \mathbf { B } _ { \bar { \mathrm { K } } }$, we can apply Proposition 5.2 to deduce that

$$
\| \bar {u} _ {k} - \bar {v} _ {k} \| _ {\mathrm{C} ^ {0} (\bar {\mathrm{S}} _ {k})} \leq \mathrm{C} _ {\bar {\mathrm{K}}} \Bigl (\underset {\mathrm{S} _ {h _ {k}}} {\mathrm{osc}} f + \underset {\mathrm{T} _ {u} (\mathrm{S} _ {h _ {k}})} {\mathrm{osc}} g + \delta_ {k} ^ {\gamma / n} \Bigr) \leq \mathrm{C} _ {\bar {\mathrm{K}}} \bigl (\delta_ {1} + \delta_ {1} ^ {\gamma / n} \bigr).\tag{5.17}
$$

This implies in particular that, if$\delta _ { 1 }$is sufficiently small,$\mathbf { B } _ { 1 / ( 2 \bar { \mathrm { K } } ) } \subset \{ \bar { v } _ { k } \leq 1 \} \subset \mathbf { B } _ { 2 \bar { \mathrm { K } } }$. By standard estimates on the sections ofsolutions to the Monge-Ampère equation, the shapes of$\{ \bar { v } _ { k } \le 1 \}$and$\{ \bar { v } _ { k } \le 1 / 2 \}$are comparable, and in addition sections are well included into each other [26, Theorem 3.3.8]: there exists a universal constant$\mathrm { ~ L > 1 ~ }$such that

$$
\begin{array}{l} \mathrm{B} _ {1 / (\mathrm{L} \bar {\mathrm{K}})} \subset \{\bar {v} _ {k} \leq 1 / 2 \} \subset \mathrm{B} _ {\mathrm{L} \bar {\mathrm{K}}}, \\ \mathrm{dist} \big (\{\bar {v} _ {k} \leq 1 / 4 \}, \partial \{\bar {v} _ {k} \leq 1 / 2 \} \big) \geq 1 / (\mathrm{LK}). \end{array}
$$

Using again (5.17) we deduce that, if$\dot { \delta } _ { 1 }$is sufficiently small,

$$
\begin{array}{l} \mathrm{B} _ {1 / (2 \mathrm{L} \bar {\mathrm{K}})} \subset \{\bar {u} _ {k} \leq 1 / 2 \} \subset \mathrm{B} _ {2 \mathrm{L} \bar {\mathrm{K}}}, \\ \operatorname{dist} \bigl (\{\bar {u} _ {k} \leq 1 / 4 \}, \partial \{\bar {u} _ {k} \leq 1 / 2 \} \bigr) \geq 1 / (2 \mathrm{LK}) \end{array}
$$

so, by scaling back,

$$
\mathrm{B} _ {\sqrt {h _ {k + 1}} / (2 \mathrm{L} \bar {\mathrm{K}})} \subset \mathrm{S} _ {h _ {k + 1}} \subset \mathrm{B} _ {2 \mathrm{L} \bar {\mathrm{K}}} \sqrt {h _ {k + 1}}, \quad \operatorname{dist} (\mathrm{S} _ {h _ {k + 2}}, \partial \mathrm{S} _ {h _ {k + 1}}) \geq \sqrt {h _ {k}} / (2 \mathrm{LK}).\tag{5.18}
$$

This allows us to apply Proposition 5.2 also to$\overline { { u } } _ { k + 1 }$to get

$$
\| \bar {u} _ {k + 1} - \bar {v} _ {k + 1} \| _ {\mathrm{C} ^ {0} (\bar {\mathrm{S}} _ {k + 1})} \leq \mathrm{C} _ {2 \mathrm{L} \bar {\mathrm{K}}} \Bigl (\underset {\mathrm{S} _ {h _ {k + 1}}} {\mathrm{osc}} f + \underset {\mathrm{T} _ {u} (\mathrm{S} _ {h _ {k + 1}})} {\mathrm{osc}} g + \delta_ {k + 1} ^ {\gamma / n} \Bigr).\tag{5.19}
$$

We now observe that, by (5.15) and the$\mathrm { C } ^ { 1 , \beta }$regularity of u (see Theorem 4.3), it follows that

$$
\operatorname{diam} \left(\mathrm{S} _ {h _ {k}}\right) + \operatorname{diam} \left(\mathrm{T} _ {u} \left(\mathrm{S} _ {h _ {k}}\right)\right) \leq \mathrm{Ch} _ {k} ^ {\beta / 2},
$$

so by the$\mathrm { C } ^ { 0 , \alpha }$regularity off and$g ,$and the$\mathrm { C ^ { 2 , \alpha } }$regularity of$c ,$we have (recall that $\gamma < 1 )$

$$
\underset {\mathrm{S} _ {h _ {k}}} {\operatorname{osc}} f + \underset {\mathrm{T} _ {u} (\mathrm{S} _ {h _ {k}})} {\operatorname{osc}} g + \delta_ {k} ^ {\gamma / n} \leq \mathrm{C} ^ {\prime} h _ {k} ^ {\sigma}, \quad \sigma := \frac {\alpha \beta \gamma}{2 n}.\tag{5.20}
$$

Hence, by (5.17) and (5.19),

$$
\| \bar {u} _ {k} - \bar {v} _ {k} \| _ {\mathrm{C} ^ {0} (\bar {\mathrm{S}} _ {k})} + \| \bar {u} _ {k + 1} - \bar {v} _ {k + 1} \| _ {\mathrm{C} ^ {0} (\bar {\mathrm{S}} _ {k + 1})} \leq \mathrm{C} (\mathrm{C} _ {\bar {\mathrm{K}}} + \mathrm{C} _ {2 \mathrm{L} \bar {\mathrm{K}}}) h _ {k} ^ {\sigma},
$$

from which we deduce (recall that$h _ { k } = 2 h _ { k + 1 } )$

$$
\begin{array}{r l} & {\| \boldsymbol {v} _ {k} - \boldsymbol {v} _ {k + 1} \| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 1}})} \leq \| \boldsymbol {v} _ {k} - \boldsymbol {u} \| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k}})} + \| \boldsymbol {u} - \boldsymbol {v} _ {k + 1} \| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 1}})}} \\ & {\qquad = h _ {k} \| \bar {\boldsymbol {u}} _ {k} - \bar {\boldsymbol {v}} _ {k} \| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {k})} + h _ {k + 1} \| \bar {\boldsymbol {u}} _ {k + 1} - \bar {\boldsymbol {v}} _ {k + 1} \| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {k + 1})}} \\ & {\qquad \leq \mathrm{C} (\mathrm{C} _ {\bar {\mathrm{K}}} + \mathrm{C} _ {2 \mathrm{L} \bar {\mathrm{K}}}) h _ {k} ^ {1 + \sigma}.} \end{array}
$$

Since$v _ { k }$and$v _ { k + 1 }$are two strictly convex solutions of the Monge Ampère equation with constant right hand side inside$\mathrm { S } _ { h _ { k + 1 } }$, and since$\mathrm { S } _ { h _ { k + 2 } }$is “well contained” inside$\mathrm { S } _ { h _ { k + 1 } }$, by classical Pogorelov and Schauder estimates we get

(5.21)

$$
\left\| \mathbf {D} ^ {2} \boldsymbol {v} _ {k} - \mathbf {D} ^ {2} \boldsymbol {v} _ {k + 1} \right\| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 2}})} \leq \mathrm{C} _ {\bar {\mathrm{K}}} ^ {\prime} h _ {k} ^ {\sigma},\tag{5.22}
$$

$$
\left\| \mathrm{D} ^ {3} v _ {k} - \mathrm{D} ^ {3} v _ {k + 1} \right\| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 2}})} \leq \mathrm{C} _ {\bar {\mathrm{K}}} ^ {\prime} h _ {k} ^ {\sigma - 1 / 2},
$$

where$\mathrm { C } _ { \bar { \mathrm { K } } } ^ { \prime }$is some constant depending only on$\bar { \mathrm { K } }$. By (5.21) applied to$v _ { j }$for all$j =$ $1 , \ldots , k$(this can be done since, by the inductive assumption, (5.15) holds for$h = h _ { j }$with $j = 1 , \ldots , k )$we obtain

$$
\begin{array}{l} \left| \mathrm{D} ^ {2} v _ {k + 1} (0) \right| \leq \left| \mathrm{D} ^ {2} v _ {1} (0) \right| + \sum_ {j = 1} ^ {k} \left| \mathrm{D} ^ {2} v _ {j} (0) - \mathrm{D} ^ {2} v _ {j + 1} (0) \right| \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq \mathrm{M} + \mathrm{C} _ {\bar {\mathrm{K}}} ^ {\prime} h _ {1} ^ {\sigma} \sum_ {j = 0} ^ {k} 2 ^ {- j \sigma} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq \mathrm{M} + \frac {\mathrm{C} _ {\bar {\mathrm{K}}} ^ {\prime}}{1 - 2 ^ {- \sigma}} h _ {1} ^ {\sigma} \leq \mathrm{M} + 1, \end{array}
$$

provided we choose$h _ { 1 }$small enough (recall that$h _ { k } = h _ { 1 } 2 ^ { - k } )$. By the definition of$\bar { \mathrm { K } }$it follows that also$\mathrm { S } _ { h _ { k + 1 } }$satisfies (5.15), concluding the proof of the inductive step.

## • Step 2: higher regularity.

Now that we know that$u \in \mathrm { C } ^ { 1 , 1 } ( \mathbf { B } _ { 1 / 8 } )$, Equation (2.10) becomes uniformly elliptic. So one may use Evans-Krylov Theorem to obtain that$u \in \mathrm { C } _ { \mathrm { l o c } } ^ { 2 , \sigma ^ { \prime } } ( \mathbf { B } _ { 1 / 9 } )$for some$\sigma ^ { \prime } > 0$, and then standard Schauder estimates to conclude the proof. However, for the convenience of the reader, we show here how to give a simple direct proof of the$\mathrm { C } ^ { 2 , \sigma ^ { \prime } }$regularity of u with$\sigma ^ { \prime } = 2 \sigma$

As in the previous step, it suffices to show that u is$\mathrm { C } ^ { 2 , \sigma ^ { \prime } }$at the origin, and for thi we have to prove that there exists a sequence of paraboloids$\mathrm { P } _ { k }$such that

$$
\sup _ {\mathrm{B} _ {r _ {0} ^ {k} / \mathrm{C}}} | u - \mathrm{P} _ {k} | \leq \mathrm{C} r _ {0} ^ {k (2 + \sigma^ {\prime})}\tag{5.23}
$$

for some$r _ { 0 } , \mathrm { C } > 0$

Let$v _ { k }$be as in the previous step, and let$\mathrm { P } _ { k }$be their second order Taylor expansion at 0:

$$
\mathrm{P} _ {k} (x) = v _ {k} (\mathbf {0}) + \nabla v _ {k} (\mathbf {0}) \cdot x + \frac {1}{2} \mathrm{D} ^ {2} v _ {k} (\mathbf {0}) x \cdot x.
$$

We observe that, thanks to (5.15),

$$
\left\| v _ {k} - \mathrm{P} _ {k} \right\| _ {\mathrm{C} ^ {0} (\mathrm{B} (0, \sqrt {h _ {k + 2}} / \mathrm{K}))} \leq \left\| v _ {k} - \mathrm{P} _ {k} \right\| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 2}})} \leq \mathrm{C} \left\| \mathrm{D} ^ {3} v _ {k} \right\| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 2}})} h _ {k} ^ {3 / 2}.\tag{5.24}
$$

In addition, by (5.22) applied with$j = 1 , \dots , k$and recalling that$h _ { k } = h _ { 1 } 2 ^ { - k }$and$2 \sigma < 1$ (see (5.20)), we get

$$
\left\| \mathrm{D} ^ {3} v _ {k} \right\| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 2}})} \leq \left\| \mathrm{D} ^ {3} v _ {1} \right\| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {3}})} + \sum_ {j = 1} ^ {k} \left\| \mathrm{D} ^ {3} v _ {j} - \mathrm{D} ^ {3} v _ {j + 1} \right\| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {j + 2}})}\tag{5.25}
$$

$$
\leq \mathrm{C} \left(1 + \sum_ {j = 1} ^ {k} h _ {j} ^ {(\sigma - 1 / 2)}\right) \leq \mathrm{C} h _ {k} ^ {\sigma - 1 / 2}.
$$

Combining (5.15), (5.24), (5.25), and recalling (5.17) and (5.20), we obtain

$$
\| u - \mathrm{P} _ {k} \| _ {\mathrm{C} ^ {0} (\mathrm{B} \sqrt {h _ {k + 2}} / \mathrm{K})} \leq \| v _ {k} - \mathrm{P} _ {k} \| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 2}})} + \| v _ {k} - u \| _ {\mathrm{C} ^ {0} (\mathrm{S} _ {h _ {k + 2}})} \leq \mathrm{C} h _ {k} ^ {1 + \sigma},
$$

so (5.23) follows with$r _ { 0 } = 1 / \sqrt { 2 }$and$\sigma ^ { \prime } = 2 \sigma$

## Acknowledgements

We wish to thank Luigi Ambrosio for his careful reading of a preliminary version ofthis manuscript. AF is partially supported by NSF Grant DMS-0969962. Both authors acknowledge the support of the ERC ADG Grant GeMeThNES.

## REFERENCES

1. L. A , N. G and G. S É, Gradient Flows in Metric Spaces and in the Space of Probability Measures, 2nd ed., Lectures in Mathematics ETH Zürich, Birkhäuser, Basel, 2008.

2. Y. BRENIER, Polar factorization and monotone rearrangement of vector-valued functions, Commun. Pure Appl. Math., 44 (1991), 375–417.

3. L. A. CAFFARELLI, A localization property of viscosity solutions to the Monge-Ampère equation and their strict convexity, Ann. Math. (2), 131 (1990), 129–134.

4. L. A. CAFFARELLI, Some regularity properties of solutions of Monge Ampère equation, Commun. Pure Appl. Math., 44 (1991), 965–969.

5. L. A. CAFFARELLI, The regularity of mappings with a convex potential, J. Am. Math. Soc., 5 (1992), 99–104.

6. L. A. CAFFARELLI, Interior W<sup>2,p</sup> estimates for solutions of the Monge-Ampère equation, Ann. Math. (2), 131 (1990), 135–150.

7. L. A. CAFFARELLI, M. M. GONZÁLES and T. NGUYEN, A perturbation argument for a Monge-Ampère type equation arising in optimal transportation. Preprint (2011).

8. L. A. CAFFARELLI and Y. Y. LI, A Liouville theorem for solutions of the Monge-Ampère equation with periodic data, Ann. Inst. Henri Poincaré, Anal. Non Linéaire, 21 (2004), 97–120.

9. D. CORDERO-ERAUSQUIN, R. J. MCCANN and M. SCHMUCKENSCHLÄGER, A Riemannian interpolation inequality à la Borell, Brascamp and Lieb, Invent. Math., 146 (2001), 219–257.

10. P. DELANOË and Y. GE, Regularity of optimal transportation maps on compact, locally nearly spherical, manifolds, J. Reine Angew. Math., 646 (2010), 65–115.

11. P. DELANOË and F. ROUVIÈRE, Positively curved Riemannian locally symmetric spaces are positively squared distance curved, Can. J. Math., 65 (2013), 757–767.

12. L. C. E and R. F. G , Measure Theory and Fine Properties ofFunctions, Studies in Advanced Mathematics, CRC Press, Boca Raton, 1992.

13. A. FATHI and A. FIGALLI, Optimal transportation on non-compact manifolds, Isr. J. Math., 175 (2010), 1–59.

14. A. FIGALLI, Existence, uniqueness, and regularity ofoptimal transport maps, SIAMJ. Math. Anal., 39 (2007), 126–137.

15. A. FIGALLI, Regularity of optimal transport maps [after Ma-Trudinger-Wang and Loeper]. (English summary) Séminaire Bourbaki. Volume 2008/2009. Exposés 997–1011. Astérisque No. 332 (2010), Exp. No. 1009, ix, 341–368.

16. A. FIGALLI, Regularity properties of optimal maps between nonconvex domains in the plane, Commun. Partial Differ. Equ., 35 (2010), 465–479.

17. A. FIGALLI and N. GIGLI, Local semiconvexity of Kantorovich potentials on non-compact manifolds, ESAIM Control Optim. Calc. Var., 17 (2011), 648–653.

18. A. FIGALLI and Y. H. KIM, Partial regularity of Brenier solutions of the Monge-Ampère equation, Discrete Contin. Dyn. Syst., 28 (2010), 559–565.

19. A. FIGALLI, Y. H. KIM and R.J. MCCANN, Hölder continuity and injectivity of optimal maps, Arch. Ration. Mech. Anal., 209 (2013), 747–795.

20. A. FIGALLI, Y. H. KIM and R. J. MCCANN, Regularity of optimal transport maps on multiple products of spheres, J. Eur. Math. Soc. (JEMS), 5 (2013), 1131–1166.

21. A. FIGALLI and G. LOEPER, C<sup>1</sup> regularity of solutions of the Monge-Ampère equation for optimal transport in dimension two, Calc. Var. Partial Differ. Egu., 35 (2009), 537–550.

22. A. FIGALLI and L. RIFFORD, Continuity of optimal transport maps and convexity of injectivity domains on small deformations of S<sup>2</sup>, Commun. Pure Appl. Math., 62 (2009), 1670–1706.

23. A. FIGALLI, L. RIFFORD and C. VILLANI, On the Ma-Trudinger-Wang curvature on surfaces, Calc. Var. Partial Differ. Equ., 39 (2010), 307–332.

24. A. FIGALLI, L. RIFFORD and C. VILLANI, Necessary and sufficient conditions for continuity of optimal transport maps on Riemannian manifolds, Tohoku Math. J. (2), 63 (2011), 855–876.

25. A. FIGALLI, L. RIFFORD and C. VILLANI, Nearly round spheres look convex, Am. J. Math., 134 (2012), 109–139.

26. C. GUTIERREZ, The Monge-Ampére Equation, Progress in Nonlinear Differential Equations and Their Applications, vol. 440, Birkhäuser, Boston, 2001.

27. H.-Y. JIAN and X.-J. WANG, Continuity estimates for the Monge-Ampère equation, SIAM J. Math. Anal., 39 (2007), 608–626.

28. Y.-H. KIM, Counterexamples to continuity ofoptimal transport maps on positively curved Riemannian manifolds, Int. Math. Res. Not. IMRN 2008, Art. ID rnn120, 15 pp.

29. Y.-H. KIM and R.J. MCCANN, Towards the smoothness ofoptimal maps on Riemannian submersions and Riemannian products (of round spheres in particular), 7. Reine Angew. Math., 664 (2012), 1–27.

30. J. LIU, N. S. TRUDINGER and X.-J. WANG, Interior C<sup>2,α</sup> regularity for potential functions in optimal transportation, Commun. Partial Differ. Equ., 35 (2010), 165–184.

31. G. LOEPER, On the regularity of solutions of optimal transportation problems, Acta Math., 202 (2009), 241–283.

32. G. LOEPER, Regularity ofoptimal maps on the sphere: The quadratic cost and the reflector antenna, Arch. Ration. Mech. Anal., 199 (2011), 269–289.

33. X. N. MA, N. S. TRUDINGER and X.J. WANG, Regularity of potential functions of the optimal transportation problem, Arch. Ration. Mech. Anal., 177 (2005), 151–183.

34. R.J. MCCANN, Polar factorization of maps on Riemannian manifolds, Geom. Funct. Anal., 11 (2001), 589–608.

35. N. S. TRUDINGER and X.-J. WANG, On the second boundary value problem for Monge-Ampère type equations and optimal transportation, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), 8 (2009), 143–174.

36. N. S. TRUDINGER and X.-J. WANG, On strict convexity and continuous differentiability ofpotential functions in optimal transportation, Arch. Ration. Mech. Anal., 192 (2009), 403–418.

37. C. VILLANI, Optimal Transport. Old andNew, Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 338, Springer, Berlin, 2009.

Scuola Normale Superiore, p.za dei Cavalieri 7, 56126 Pisa, Italy guido.dephilippis@sns.it

## G. P.

## A. F.

Department of Mathematics, The University of Texas at Austin, 1 University Station C1200, Austin, TX 78712, USA figalli@math.utexas.edu

Manuscrit reçu le 1 octobre 2012 Manuscrit accepté le 15juillet 2014 publié en ligne le 29juillet 2014.