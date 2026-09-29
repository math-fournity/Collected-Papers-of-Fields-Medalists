# Finite extinction time for the solutions to the Ricci flow on certain three-manifolds

Grisha Perelman<sup>∗</sup>

November 26, 2024

In our previous paper we constructed complete solutions to the Ricci flow with surgery for arbitrary initial riemannian metric on a (closed, oriented) three-manifold [P,6.1], and used the behavior of such solutions to classify threemanifolds into three types [P,8.2]. In particular, the first type consisted of those manifolds, whose prime factors are difeomorphic copies of spherical space forms and$\mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 1 }$; they were characterized by the property that they admit metrics, that give rise to solutions to the Ricci flow with surgery, which become extinct in finite time. While this classification was suficient to answer topological questions, an analytical question of significant independent interest remained open, namely, whether the solution becomes extinct in finite time for every initial metric on a manifold of this type.

In this note we prove that this is indeed the case. Our argument (in conjunction with [P,§1-5]) also gives a direct proof of the so called ”elliptization conjecture”. It turns out that it does not require any substantially new ideas: we use only a version of the least area disk argument from [H,§11] and a regularization of the curve shortening flow from$\left[ \mathrm { A } \mathrm { - } \mathrm { G } \right]$

## 1 Finite time extinction

1.1 Theorem. Let M be a closed oriented three-manifold, whose prime decomposition contains no aspherical factors. Then for any initial metric on M the solution to the Ricci flow with surgery becomes extinct in finite time.

Proof for irreducible M. Let ΛM denote the space of all contractible loops in $C ^ { 1 } ( \mathbb { S } ^ { 1 } \to M )$. Given a riemannian metric g on M and$c \in \Lambda M ,$define$A ( c , g )$to be the infimum of the areas of all lipschitz maps from$\mathbb { D } ^ { 2 }$to M, whose restriction to$\partial \mathbb { D } ^ { 2 } = \mathbb { S } ^ { 1 }$is c. For a family$\Gamma \subset \Lambda M$let$A ( \Gamma , g )$be the supremum of$A ( c , g )$ over all$c \in \Gamma$. Finally, for a nontrivial homotopy class$\alpha \in \pi _ { * } ( \Lambda M , M )$let $A ( \alpha , g )$be the infimum of$A ( \Gamma , g )$over all$\Gamma \in \alpha$. Since M is not aspherical, it follows from a classical (and elementary) result of Serre that such a nontrivial homotopy class exists.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>∗</sup>St.Petersburg branch of Steklov Mathematical Institute, Fontanka 27, St.Petersburg 191023, Russia. Email: perelman@pdmi.ras.ru or perelman@math.sunysb.edu</span></small>

1.2 Lemma. (cf. [H,§11])$H g ^ { t }$is a smooth solution to the Ricci flow, then for any α the rate of change of the function$A ^ { t } = A ( \alpha , g ^ { t } )$satisfies the estimate

$$
\frac {d}{d t} A ^ {t} \leq - 2 \pi - \frac {1}{2} R _ {\mathrm{min}} ^ {t} A ^ {t}
$$

(in the sense of the lim sup of the forward diference quotients), where$R _ { \operatorname* { m i n } } ^ { t }$ denotes the minimum of the scalar curvature of the metric$g ^ { t }$

A rigorous proof of this lemma will be given in$\ S 3 .$, but the idea is simple and can be explained here. Let us assume that at time t the value$A ^ { t }$is attained by the family Γ, such that the loops$c \in \Gamma$where$A ( c , g ^ { t } )$is close to$A ^ { t }$are embedded and suficiently smooth. For each such c consider the minimal disk $D _ { c }$with boundary c and with area$A ( c , g ^ { t } )$. Now let the metric evolve by the Ricci flow and let the curves c evolve by the curve shortening flow (which moves every point of the curve in the direction of its curvature vector at this point) with the same time parameter. Then the rate of change of the area of$D _ { c }$can be computed as

$$
\int_ {D _ {c}} (- \mathrm{Tr} (\mathrm{Ric} ^ {\mathrm{T}})) + \int_ {c} (- k _ {g})
$$

where$\mathrm { R i c ^ { T } }$is the Ricci tensor of M restricted to the tangent plane of$D _ { c } ,$and $k _ { g }$is the geodesic curvature of c with respect to$D _ { c }$(cf. [A-G, Lemma 3.2]). In three dimensions the first integrand equals$- \frac { 1 } { 2 } R - ( K - \dot { \operatorname * { d e t } \mathrm { I I } } )$, where K is the intrinsic curvature of$D _ { c }$and det II, the determinant of the second fundamental form, is nonpositive, because$D _ { c }$is minimal. Thus, the rate of change of the area of$D _ { c }$can be estimated from above by

$$
\int_ {D _ {c}} \left(- \frac {1}{2} R - K\right) + \int_ {c} (- k _ {g}) = \int_ {D _ {c}} \left(- \frac {1}{2} R\right) - 2 \pi
$$

by the Gauss-Bonnet theorem, and the statement of the lemma follows.

The problem with this argument is that if Γ contains curves, which are not immersed (for instance, a curve could pass an arc once in one direction and then make an about turn and pass the same arc in the opposite direction), then it is not clear how to define curve shortening flow so that it would be continuous both in the time parameter and in the family parameter. In §3 we’ll explain how to circumvent this dificulty, essentially by adding one dimension to the ambient manifold. This regularization of the curve shortening flow has been worked out by Altschuler and Grayson [A-G] (who were interested in approximating the singular curve shortening flow on the plane and obtained for that case more precise results than what we need).

1.3 Now consider the solution to the Ricci flow with surgery. Since M is assumed irreducible, the surgeries are topologically trivial, that is one of the components of the post-surgery manifold is difeomorphic to the pre-surgery manifold, and all the others are spheres. Moreover, by the construction of the surgery [P,4.4], the difeomorphism from the pre-surgery manifold to the post-surgery one can be chosen to be distance non-increasing ( more precisely, $( 1 + \xi ) \mathrm { - l i p s c h i t z }$, where$\xi > 0$can be made as small as we like). It follows that the conclusion of the lemma above holds for the solutions to the Ricci flow with surgery as well.

Now recall that the evolution equation for the scalar curvature

$$
\frac {d}{d t} R = \triangle R + 2 | \mathrm{Ric} | ^ {2} = \triangle R + \frac {2}{3} R ^ {2} + 2 | \mathrm{Ric} ^ {\circ} | ^ {2}
$$

implies the estimate$\begin{array} { r } { R _ { \mathrm { m i n } } ^ { t } \geq - \frac { 3 } { 2 } \frac { 1 } { t + \mathrm { c o n s t } } } \end{array}$. It follows that$\begin{array} { r } { \hat { A } ^ { t } = \frac { A ^ { t } } { t + \mathrm { c o n s t } } } \end{array}$satisfies $\begin{array} { r } { \frac { d } { d t } \hat { A } ^ { t } \leq - \frac { 2 \pi } { t + \mathrm { c o n s t } } } \end{array}$, which implies finite extinction time since the right hand side is non-integrable at infinity whereas$\hat { A } ^ { t }$can not become negative.

1.4 Remark. The finite time extinction result for irreducible non-aspherical manifolds already implies (in conjuction with the work in [P,§1-5] and the Kneser finiteness theorem) the so called ”elliptization conjecture”, claiming that a closed manifold with finite fundamental group is difeomorphic to a spherical space form. The analysis of the long time behavior in [P,§6-8] is not needed in this case; moreover the argument in [P,§5] can be slightly simplified, replacing the sequences$r _ { j } , \kappa _ { j } , \bar { \delta } _ { j }$by single values$r , \kappa , \bar { \delta } .$, since we already have an upper bound on the extinction time in terms of the initial metric.

In fact, we can even avoid the use of the Kneser theorem. Indeed, if we start from an initial metric on a homotopy sphere (not assumed irreducible), then at each surgery time we have (almost) distance non-increasing homotopy equivalences from the pre-surgery manifold to each of the post-surgery components, and this is enough to keep track of the nontrivial relative homotopy class of the loop space.

1.5 Proof oftheorem 1.1 for general M. The Kneser theorem implies that our solution undergoes only finitely many topologically nontrivial surgeries, so from some time$T$on all the surgeries are trivial. Moreover, by the Milnor uniqueness theorem, each component at time$T$satisfies the assumption of the theorem. Since we already know from 1.4 that there can not be any simply connected prime factors, it follows that every such component is either irreducible, or has nontrivial$\pi _ { 2 } ;$in either case the proof in 1.1-1.3 works.

## 2 Preliminaries on the curve shortening flow

In this section we rather closely follow [A-G].

2.1 Let M be a closed n-dimensional manifold,$n \geq 3 .$, and let$g ^ { t }$be a smooth family of riemannian metrics on M evolving by the Ricci flow on a finite time interval$[ t _ { 0 } , t _ { 1 } ]$. It is known [B] that$g ^ { t }$for$t > t _ { 0 }$are real analytic. Let$c ^ { t }$be a solution to the curve shortening flow in$( M , g ^ { t } )$, that is$c ^ { t }$satisfies the equation $\begin{array} { r } { \frac { d } { d t } c ^ { t } ( x ) \ = \ H ^ { t } ( x ) } \end{array}$, where$x$is the parameter on$\mathbb { S } ^ { 1 }$, and$H ^ { t }$is the curvature vector field of$c ^ { t }$with respect to$g ^ { t }$. It is known [G-H] that for any smoothly immersed initial curve c the solution$c ^ { t }$exists on some time interval$[ t _ { 0 } , t _ { 1 } ^ { \prime } )$, each $c ^ { t }$for$t > t _ { 0 }$is an analytic immersed curve, and either$t _ { 1 } ^ { \prime } = t _ { 1 }$, or the curvature $k ^ { t } = g ^ { t } ( H ^ { t } , H ^ { t } ) ^ { \frac { 1 } { 2 } }$is unbounded when$t  t _ { 1 } ^ { \prime }$

Denote by$X ^ { t }$the tangent vector field to$c ^ { t }$, and let$S ^ { t } = g ^ { t } ( X ^ { t } , X ^ { t } ) ^ { - \frac { 1 } { 2 } } X ^ { t }$ be the unit tangent vector field; then$H = \nabla _ { S } S$(from now on we drop the superscript t except where this omission can cause confusion). We compute

$$
\frac {d}{d t} g (X, X) = - 2 \mathrm{Ric} (X, X) - 2 g (X, X) k ^ {2},\tag{1}
$$

which implies

$$
[ H, S ] = (k ^ {2} + \operatorname{Ric} (S, S)) S\tag{2}
$$

Now we can compute

$$
\frac {d}{d t} k ^ {2} = (k ^ {2}) ^ {\prime \prime} - 2 g ((\nabla_ {S} H) ^ {\perp}, (\nabla_ {S} H) ^ {\perp}) + 2 k ^ {4} + \dots ,\tag{3}
$$

where primes denote diferentiation with respect to the arclength parameter$s ,$ and where dots stand for the terms containing the curvature tensor of$^ { g , }$which can be estimated in absolute value by const$( k ^ { 2 } + k )$. Thus the curvature$k$ satisfies

$$
\frac {d}{d t} k \leq k ^ {\prime \prime} + k ^ {3} + \mathrm{const} \cdot (k + 1)\tag{4}
$$

Now it follows from (1) and (4) that the length L and the total curvature $\Theta = \int k d s$satisfy

$$
\frac {d}{d t} L \leq \int (\mathrm{const} - k ^ {2}) d s,\tag{5}
$$

$$
\frac {d}{d t} \Theta \leq \int \mathrm{const} \cdot (k + 1) d s\tag{6}
$$

In particular, both quantities can grow at most exponentially in t (they would be non-increasing in a flat manifold).

2.2 In general the curvature of$c ^ { t }$may concentrate near certain points, creating singularities. However, if we know that this does not happen at some time$t ^ { * }$, then we can estimate the curvature and higher derivatives at times shortly thereafter. More precisely, there exist constants$\epsilon , C _ { 1 } , C _ { 2 } , \ldots$(which may depend on the curvatures of the ambient space and their derivatives, but are independent of$c ^ { t } )$, such that if at time$t ^ { * }$for some$r > 0$the length of$c ^ { t }$is at least r and the total curvature of each arc of length r does not exceed$\epsilon ,$then for every$t \in ( t ^ { * } , t ^ { * } + \epsilon r ^ { 2 } )$the curvature k and higher derivatives satisfy the estimates$k ^ { 2 } = g ( H , H ) \leq C _ { 0 } ( t - t ^ { * } ) ^ { - 1 } , g ( \nabla _ { S } H , \nabla _ { S } H ) \leq C _ { 1 } ( t - t ^ { * } ) ^ { - 2 }$ This can be proved by adapting the arguments of Ecker and Huisken [E-Hu]; see also [A-G,§4].

2.3 Now suppose that our manifold$( M , g ^ { t } )$is a metric product$( \bar { M } , \bar { g } ^ { t } ) \times \mathbb { S } _ { \lambda } ^ { 1 }$ where the second factor is the circle of constant length$\lambda ;$let U denote the unit tangent vector field to this factor. Then$u \ : = \ : g ( S , U )$satisfies the evolution equation

$$
\frac {d}{d t} u = u ^ {\prime \prime} + (k ^ {2} + \mathrm{Ric} (S, S)) u\tag{7}
$$

Assume that u was strictly positive everywhere at time$t _ { 0 }$(in this case the curve is called a ramp). Then it will remain positive and bounded away from zero as long as the solution exists. Now combining (4) and (7) we can estimate the right hand side of the evolution equation for the ratio$\textstyle { \frac { k } { u } }$and conclude that this ratio, and hence the curvature$k ,$stays bounded (see$[ \mathrm { A - G } , \ S 2 ] )$). It follows that$c ^ { t }$is defined on the whole interval$[ t _ { 0 } , t _ { 1 } ]$

2.4 Assume now that we have two ramp solutions$c _ { 1 } ^ { t } , c _ { 2 } ^ { t }$, each winding once around the$\mathbb { S } _ { \lambda } ^ { 1 }$factor. Let$\mu ^ { t }$be the infimum of the areas of the annuli with boundary$c _ { 1 } ^ { t } \cup c _ { 2 } ^ { t }$. Then

$$
\frac {d}{d t} \mu^ {t} \leq (2 n - 1) | \mathrm{Rm} ^ {t} | \mu^ {t},\tag{8}
$$

where$| \mathrm { R m } ^ { t } |$denotes a bound on the absolute value of sectional curvatures of$g ^ { t }$. Indeed, the curves$c _ { 1 } ^ { t }$and$c _ { 2 } ^ { t }$, being ramps, are embedded and without substantial loss of generality we may assume them to be disjoint. In this case the results of Morrey [M] and Hildebrandt [Hi] yield an analytic minimal annulus$A$ immersed, except at most finitely many branch points, with prescribed boundary and with area$\mu$. The rate of change of the area of A can be computed as

$$
\begin{array}{l} \int_ {A} (- \mathrm{Tr} (\mathrm{Ric} ^ {T})) + \int_ {\partial A} (- k _ {g}) \leq \int_ {A} (- \mathrm{Tr} (\mathrm{Ric} ^ {T}) + K) \\ \qquad \leq \int_ {A} (- \mathrm{Tr} (\mathrm{Ric} ^ {T}) + \mathrm{Rm} ^ {T}) \leq (2 n - 1) | \mathrm{Rm} | \mu , \end{array}
$$

where the first inequality comes from the Gauss-Bonnet theorem, with possible contribution of the branch points, and the second one is due to the fact that a minimal surface has nonpositive extrinsic curvature with respect to any normal vector.

2.5 The estimate (8) implies that$\mu ^ { t }$can grow at most exponentially; in particular, if$c _ { 1 } ^ { t }$and$c _ { 2 } ^ { t }$were very close at time$t _ { 0 } .$then they would be close for all$t \in [ t _ { 0 } , t _ { 1 } ]$in the sense of minimal annulus area. In general this does not imply that the lengths of the curves are also close. However, an elementary argument shows that$\mathrm { i f } \ \epsilon > 0$is small then, given any$r > 0$, one can find$\bar { \mu } ,$ depending only on r and on upper bound for sectional curvatures of the ambient space, such that if the length of$c _ { 1 } ^ { t }$is at least$r ,$each arc of$c _ { 1 } ^ { t }$with length$r$has total curvature at most$\epsilon ,$and$\mu ^ { t } \leq \bar { \mu }$, then$L ( c _ { 2 } ^ { t } ) \geq ( 1 - 1 0 \bar { 0 } \epsilon ) L ( c _ { 1 } ^ { t } /$).

## 3 Proof of lemma 1.2

3.1 In this section we prove the following statement

Let M be a closed three-manifold, and let$( M , g ^ { t } )$be a smooth solution to the Ricci flow on a finite time interval$[ t _ { 0 } , t _ { 1 } ]$. Suppose that$\Gamma \subset \Lambda M$is a compact family. Then for any$\xi > 0$one can construct a continuous deformation$\Gamma ^ { t } , t \in$ $[ t _ { 0 } , t _ { 1 } ] , \Gamma ^ { t _ { 0 } } = \Gamma$, such that for each curve$c \in \Gamma$either the value$A ( c ^ { t _ { 1 } } , g ^ { t _ { 1 } } )$is bounded from above by ξ plus the value at$t = t _ { 1 }$of the solution to the ODE $\begin{array} { r } { \frac { d } { d t } w ( t ) = - 2 \pi - \frac { 1 } { 2 } R _ { \mathrm { m i n } } ^ { t } w ( t ) } \end{array}$with the initial data$w ( t _ { 0 } ) = A ( c ^ { t _ { 0 } } , g ^ { t _ { 0 } } )$or $\begin{array} { r } { \bar { L } ( c ^ { t _ { 1 } } ) \leq \xi ; } \end{array}$moreover,$i f c$was a constant map, then all$c ^ { t }$are constant maps.

It is clear that our statement implies lemma 1.2, because a family consisting of very short loops can not represent a nontrivial relative homotopy class.

3.2 As a first step of the proof of the statement we can replace Γ by a family, which consists of piecewise geodesic loops with some large fixed number of vertices and with each segment reparametrized in some standard way to make the parametrizations of the whole curves twice continuously diferentiable.

Now consider the manifold$M _ { \lambda } = M \times \mathbb { S } _ { \lambda } ^ { 1 } , 0 < \lambda < 1$, and for each$c \in \Gamma$ consider the smooth embedded closed curve$c _ { \lambda }$such that$p _ { 1 } c _ { \lambda } ( x ) = c ( x )$and $p _ { 2 } c _ { \lambda } ( x ) = \lambda x$mod λ, where$p _ { 1 }$and$p _ { 2 }$are projections of$M _ { \lambda }$to the first and second factor respectively, and x is the parameter of the curve c on the standard circle of length one. Using 2.3 we can construct a solution$c _ { \lambda } ^ { t } , t \in [ t _ { 0 } , t _ { 1 } ]$to the curve shortening flow with initial data$c _ { \lambda }$. The required deformation will be obtained as$\Gamma ^ { t } = p _ { 1 } \Gamma _ { \lambda } ^ { t }$(where$\Gamma _ { \lambda } ^ { t }$denotes the family consisting of$c _ { \lambda } ^ { t } )$for certain suficiently small$\lambda > 0$. We’ll verify that an appropriate λ can be found for each individual curve c, or for any finite number of them, and then show that if our λ works for all elements of a µ-net in$\Gamma ,$for suficiently small$\mu > 0$ then it works for all elements of Γ.

3.3 In the following estimates we shall denote by C large constants that may depend on metrics$g ^ { t }$, family Γ and ξ, but are independent of$\lambda , \mu$and a particular curve c.

The first step in 3.2 implies that the lengths and total curvatures of$c _ { \lambda }$are uniformly bounded, so by 2.1 the same is true for all$c _ { \lambda } ^ { t }$. It follows that the area swept by$c _ { \lambda } ^ { t } , t \in [ t ^ { \prime } , t ^ { \prime \prime } ] \subset [ t _ { 0 } , t _ { 1 } ]$is bounded above by$\dot { C } ( t ^ { \prime \prime } - t ^ { \prime } )$, and therefore we have the estimates$A ( p _ { 1 } c _ { \lambda } ^ { t } , g ^ { t } ) \leq C , A ( p _ { 1 } c _ { \lambda } ^ { t ^ { \prime \prime } } , g ^ { t ^ { \prime \prime } } ) - A ( p _ { 1 } c _ { \lambda } ^ { t ^ { \prime } } , g ^ { t ^ { \prime } } ) \leq C ( t ^ { \prime \prime } - t ^ { \prime } )$

3.4 It follows from (5) that$\begin{array} { r } { \int _ { t _ { 0 } } ^ { t _ { 1 } } \int k ^ { 2 } d s d t \leq C } \end{array}$for any$c _ { \lambda } ^ { t }$. Fix some large constant B, to be chosen later. Then there is a subset$I _ { B } ( c _ { \lambda } ) ~ \subset ~ [ t _ { 0 } , t _ { 1 } ]$of measure at least$t _ { 1 } - t _ { 0 } - C B ^ { - 1 }$where$\textstyle \int k ^ { 2 } d s \leq B$, hence kds$\leq \epsilon$on any arc of length$\le \epsilon ^ { 2 } B ^ { - 1 }$. Assuming that$c _ { \lambda } ^ { t }$are at least that long, we can apply 2.2 and construct another subset$J _ { B } ( c _ { \lambda } ) \subset [ t _ { 0 } , t _ { 1 } ]$of measure at least$t _ { 1 } - t _ { 0 } - C B ^ { - 1 }$，consisting of finitely many intervals of measure at least$C ^ { - 1 } B ^ { - 2 }$each, such that for any$t \in J _ { B } ( c _ { \lambda } )$we have pointwise estimates on$c _ { \lambda } ^ { t }$for curvature and higher derivatives, of the form$k \leq C B , . .$

Now fix$c , B$, and consider any sequence of$\lambda  0$. Assume again that the lengths of$c _ { \lambda } ^ { t }$are bounded below by$\epsilon ^ { 2 } B ^ { - 1 }$, at least for$t \in [ t _ { 0 } , t _ { 2 } ]$, where$t _ { 2 } =$ $t _ { 1 } - B ^ { - 1 }$. Then an elementary argument shows that we can find a subsequence $\Lambda _ { c }$and a subset$J _ { B } ( c ) \subset [ t _ { 0 } , t _ { 2 } ]$of measure at least$t _ { 1 } - t _ { 0 } - C B ^ { - 1 }$, consisting of finitely many intervals, such that$J _ { B } ( c ) \subset J _ { B } ( c _ { \lambda } )$for all$\lambda \in \Lambda _ { c }$. It follows that on every interval of$J _ { B } ( c )$the curve shortening flows$c _ { \lambda } ^ { t }$smoothly converge (as$\lambda  0$in some subsequence of$\Lambda _ { c } { \bf \Psi } )$to a curve shortening flow in$M .$

Let$w _ { c } ( t )$be the solution of the ODE$\begin{array} { r } { \frac { d } { d t } w _ { c } ( t ) = - 2 \pi - \frac { 1 } { 2 } R _ { \mathrm { m i n } } ^ { t } w _ { c } ( t ) } \end{array}$with initial data$w _ { c } ( t _ { 0 } ) ~ = ~ A ( c , g ^ { t _ { 0 } } )$. Then for suficiently small$\lambda \ \in \ \Lambda _ { c }$we have $A ( p _ { 1 } c _ { \lambda } ^ { t } , g ^ { t } ) \leq w _ { c } ( t ) + \frac { 1 } { 2 } \xi$provided that$B > C \xi ^ { - 1 }$. Indeed, on the intervals of $J _ { B } ( c )$we can estimate the change of A for the limit flow using the minimal disk argument as in 1.2, and this implies the corresponding estimate for${ p } _ { 1 } { c } _ { \lambda } ^ { t }$if $\lambda \in \Lambda _ { c }$is small enough, whereas for the intervals of the complement of$J _ { B } ( c )$ we can use the estimate in 3.3.

On the other hand, if our assumption on the lower bound for lengths does not hold, then it follows from (5) that$\begin{array} { r } { L ( c _ { \lambda } ^ { t _ { 2 } } ) \leq C B ^ { - 1 } \leq \frac { 1 } { 2 } \xi } \end{array}$

3.5 Now apply the previous argument to all elements of some finite µ-net $\hat { \Gamma } \subset \Gamma$for small$\mu > 0$to be determined later. We get a$\lambda > 0$such that for each $\hat { c } \in \hat { \Gamma }$either$\begin{array} { r } { A ( p _ { 1 } \hat { c } _ { \lambda } ^ { t _ { 1 } } , g ^ { t _ { 1 } } ) \leq w _ { \hat { c } } ( t _ { 1 } ) + \frac { 1 } { 2 } \xi \mathrm { o r } L ( \hat { c } _ { \lambda } ^ { t _ { 2 } } ) \leq \frac { 1 } { 2 } \xi } \end{array}$. Now for any curve$c \in \Gamma$ pick a curve$\hat { c } \in \hat { \Gamma }$, µ-close to$c ,$and apply the result of 2.4. It follows that if $A ( p _ { 1 } \hat { c } _ { \lambda } ^ { t _ { 1 } } , g ^ { t _ { 1 } } ) \leq w _ { \hat { c } } ( t _ { 1 } ) + \frac 1 2 \xi$and$\mu \leq C ^ { - 1 } \xi ,$, then$A ( p _ { 1 } c _ { \lambda } ^ { t _ { 1 } } , g ^ { t _ { 1 } } ) \leq w _ { c } ( t _ { 1 } ) + \xi$. On the other hand, if$\begin{array} { r } { L ( \hat { c } _ { \lambda } ^ { t _ { 2 } } ) \leq \frac { 1 } { 2 } \xi } \end{array}$, then we can conclude that$L ( c _ { \lambda } ^ { t _ { 1 } } ) \leq \xi$provided that$\mu > 0$is small enough in comparison with$\xi$and$B ^ { - 1 }$. Indeed, if$L ( c _ { \lambda } ^ { t _ { 1 } } ) > \xi ,$ then$\begin{array} { r } { L ( c _ { \lambda } ^ { t } ) > \frac { 3 } { 4 } \xi } \end{array}$for all$t \in [ t _ { 2 } , t _ { 1 } ]$; on the other hand, using (5) we can find a $t \in [ t _ { 2 } , t _ { 1 } ]$], such that$\textstyle \int k ^ { 2 } d s \dot { \leq } C B$for$c _ { \lambda } ^ { t } ;$hence, applying 2.5, we get$\begin{array} { r } { L ( \hat { c } _ { \lambda } ^ { t } ) > \frac { 2 } { 3 } \xi } \end{array}$ for this t, which is incompatible with$\begin{array} { r } { L ( \hat { c } _ { \lambda } ^ { t _ { 2 } } ) \leq \frac { 1 } { 2 } \xi . } \end{array}$. The proof of the statement 3.1 is complete.

## References

[A-G] S.Altschuler, M.Grayson Shortening space curves and flow through singularities. Jour. Dif. Geom. 35 (1992), 283-298.

[B] S.Bando Real analyticity of solutions of Hamilton’s equation. Math. Zeit. 195 (1987), 93-97.

[E-Hu] K.Ecker, G.Huisken Interior estimates for hypersurfaces moving by mean curvature. Invent. Math. 105 (1991), 547-569.

[G-H] M.Gage, R.S.Hamilton The heat equation shrinking convex plane curves. Jour. Dif. Geom. 23 (1986), 69-96.

[H] R.S.Hamilton Non-singular solutions of the Ricci flow on three-manifolds. Commun. Anal. Geom. 7 (1999), 695-729.

[Hi] S.Hildebrandt Boundary behavior of minimal surfaces. Arch. Rat. Mech. Anal. 35 (1969), 47-82.

[M] C.B.Morrey The problem of Plateau on a riemannian manifold. Ann. Math. 49 (1948), 807-851.

[P] G.Perelman Ricci flow with surgery on three-manifolds.

arXiv:math.DG/0303109 v1