# Ricci flow with surgery on three-manifolds

Grisha Perelman<sup>∗</sup>

February 1, 2008

This is a technical paper, which is a continuation of [I]. Here we verify most of the assertions, made in [I, 13]; the exceptions are (1) the statement that a 3-manifold which collapses with local lower bound for sectional curvature is a graph manifold - this is deferred to a separate paper, as the proof has nothing to do with the Ricci flow, and (2) the claim about the lower bound for the volumes of the maximal horns and the smoothness of the solution from some time on, which turned out to be unjustified, and, on the other hand, irrelevant for the other conclusions.

The Ricci flow with surgery was considered by Hamilton [H 5, 4,5]; unfortunately, his argument, as written, contains an unjustified statement$( R _ { M A X } = \Gamma$ on page 62, lines 7-10 from the bottom), which I was unable to fix. Our approach is somewhat diferent, and is aimed at eventually constructing a canonical Ricci flow, defined on a largest possible subset of space-time, - a goal, that has not been achieved yet in the present work. For this reason, we consider two scale bounds: the cutof radius$h ,$which is the radius of the necks, where the surgeries are performed, and the much larger radius$r ,$such that the solution on the scales less than r has standard geometry. The point is to make h arbitrarily small while keeping$r$bounded away from zero.

## Notation and terminology

$\boldsymbol { B } ( \boldsymbol { x } , t , \boldsymbol { r } )$denotes the open metric ball of radius$r ,$with respect to the metric at time$t ,$centered at x.

$P ( x , t , r , \Delta t )$denotes a parabolic neighborhood, that is the set of all points $( \boldsymbol { x } ^ { \prime } , t ^ { \prime } )$with$x ^ { \prime } \in B ( x , t , r )$and$t ^ { \prime } \in [ t , t + \triangle t ]$or$t ^ { \prime } \in [ t + \Delta t , t ]$, depending on the sign of$\triangle t .$

A ball$B ( x , t , \epsilon ^ { - 1 } r )$is called an ǫ-neck, if, after scaling the metric with factor $r ^ { - 2 }$, it is ǫ-close to the standard neck$\mathbb { S } ^ { 2 } \times \mathbb { I }$, with the product metric, where$\mathbb { S } ^ { 2 }$ has constant scalar curvature one, and I has length$2 \epsilon ^ { - 1 }$; here ǫ-close refers to $C ^ { N }$topology, with$N > \epsilon ^ { - 1 }$

A parabolic neighborhood$P ( x , t , \epsilon ^ { - 1 } r , r ^ { 2 } )$is called a strong ǫ-neck, if, after scaling with factor$\bar { r } ^ { - 2 }$, it is ǫ-close to the evolving standard neck, which at each time$t ^ { \prime } \in [ - 1 , 0 ]$has length$2 \epsilon ^ { - 1 }$and scalar curvature$( 1 - t ^ { \prime } ) ^ { - 1 }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>∗</sup>St.Petersburg branch of Steklov Mathematical Institute, Fontanka 27, St.Petersburg 191011, Russia. Email: perelman@pdmi.ras.ru or perelman@math.sunysb.edu</span></small>

A metric on$\mathbb { S } ^ { 2 } \times \mathbb { I } .$such that each point is contained in some ǫ-neck, is called an ǫ-tube, or an ǫ-horn, or a double ǫ-horn, if the scalar curvature stays bounded on both ends, stays bounded on one end and tends to infinity on the other, and tends to infinity on both ends, respectively.

A metric on$\mathbb { B } ^ { 3 }$or$\mathbb { R P } ^ { 3 } \setminus \bar { \mathbb { B } } ^ { 3 }$, such that each point outside some compact subset is contained in an ǫ-neck, is called an ǫ-cap or a capped ǫ-horn, if the scalar curvature stays bounded or tends to infinity on the end, respectively.

We denote by$\epsilon \mathrm { ~ a ~ }$fixed small positive constant. In contrast, δ denotes a positive quantity, which is supposed to be as small as needed in each particular argument.

## 1 Ancient solutions with bounded entropy

1.1 In this section we review some of the results, proved or quoted in [I, 11], correcting a few inaccuracies. We consider smooth solutions$g _ { i j } ( t )$to the Ricci flow on oriented 3-manifold M, defined for$- \infty < t \leq 0$, such that for each t the metric$g _ { i j } ( t )$is a complete non-flat metric of bounded nonnegative sectional curvature, κ-noncollapsed on all scales for some fixed$\kappa > 0 ;$such solutions will be called ancient κ-solutions for short. By Theorem I.11.7, the set of all such solutions with fixed κ is compact modulo scaling, that is from any sequence of such solutions$( M ^ { \alpha } , g _ { i j } ^ { \alpha } ( t ) )$) and points$( x ^ { \alpha } , 0 )$with$R ( x ^ { \alpha } , 0 ) = 1$,we can extract a smoothly (pointed) convergent subsequence, and the limit$( M , g _ { i j } ( t ) )$ belongs to the same class of solutions. (The assumption in I.11.7. that$M ^ { \alpha }$ be noncompact was clearly redundant, as it was not used in the proof. Note also that M need not have the same topology as$M ^ { \alpha } . )$Moreover, according to Proposition I.11.2, the scalings of any ancient κ-solution$g _ { i j } ( t )$with factors $( - t ) ^ { - 1 }$about appropriate points converge along a subsequence of$t \to - \infty$to a non-flat gradient shrinking soliton, which will be called an asymptotic soliton of the ancient solution. If the sectional curvature of this asymptotic soliton is not strictly positive, then by Hamilton’s strong maximum principle it admits local metric splitting, and it is easy to see that in this case the soliton is either the round infinite cylinder, or its$\mathbb { Z } _ { 2 }$quotient, containing one-sided projective plane. If the curvature is strictly positive and the soliton is compact, then it has to be a metric quotient of the round 3-sphere, by [H 1]. The noncompact case is ruled out below.

1.2 Lemma. There is no (complete oriented 3-dimensional) noncompact κ-noncollapsed gradient shrinking soliton with bounded positive sectional curvature.

Proof. A gradient shrinking soliton$g _ { i j } ( t ) , - \infty < t < 0$, satisfies the equation

$$
\nabla_ {i} \nabla_ {j} f + R _ {i j} + \frac {1}{2 t} g _ {i j} = 0\tag{1.1}
$$

Diferentiating and switching the order of diferentiation, we get

$$
\nabla_ {i} R = 2 R _ {i j} \nabla_ {j} f\tag{1.2}
$$

Fix some$t < 0$, say$t = - 1$, and consider a long shortest geodesic$\gamma ( s ) , 0 \leq$ $s \leq { \bar { s } } ;$let$x = \gamma ( 0 ) , \bar { x } = \gamma ( \bar { s } ) , X ( s ) = \dot { \gamma } ( s )$. Since the curvature is bounded and positive, it is clear from the second variation formula that$\begin{array} { r } { \int _ { 0 } ^ { \bar { s } } \operatorname { R i c } ( X , X ) d s \leq } \end{array}$ const. Therefore,$\begin{array} { r } { \int _ { 0 } ^ { \bar { s } } | \mathrm { R i c } ( X , \cdot ) | ^ { 2 } d s \leq } \end{array}$const, and$\begin{array} { r } { \int _ { 0 } ^ { \bar { s } } | \mathrm { R i c } ( X , Y ) | d s \leq } \end{array}$const$( \sqrt { \bar { s } } +$ 1) for any unit vector field Y along$\gamma ,$orthogonal to$X ,$. Thus by integrating (1.1) we get$\begin{array} { r } { X \cdot f ( \gamma ( \bar { s } ) ) \geq \frac { \bar { s } } { 2 } + } \end{array}$const,$| Y \cdot f ( \gamma ( { \bar { s } } ) ) | \leq \mathrm { c o n s t } ( { \sqrt { \bar { s } } } + 1 )$). We conclude that at large distances from$x _ { 0 }$the function$f$has no critical points, and its gradient makes small angle with the gradient of the distance function from$x _ { 0 }$

Now from (1.2) we see that R is increasing along the gradient curves of$f ,$ in particular,$\bar { R } = \operatorname * { l i m }$sup$R > 0$. If we take a limit of our soliton about points $( x ^ { \alpha } , - 1 )$where$R ( x ^ { \alpha } )  \bar { R }$, then we get an ancient κ-solution, which splits of a line, and it follows from I.11.3, that this solution is the shrinking round infinite cylinder with scalar curvature$\bar { R }$at time$t = - 1$. Now comparing the evolution equations for the scalar curvature on a round cylinder and for the asymptotic scalar curvature on a shrinking soliton we conclude that$\bar { R } = 1$ Hence,$R ( x ) < 1$when the distance from x to$x _ { 0 }$is large enough, and$R ( x )  1$ when this distance tends to infinity.

Now let us check that the level surfaces of$f ,$suficiently distant from$x _ { 0 }$, are convex. Indeed, if$Y$is a unit tangent vector to such a surface, then$\nabla _ { Y } \nabla _ { Y } f =$ ${ \textstyle { \frac { 1 } { 2 } } } - \operatorname { R i c } ( Y , Y ) \geq { \textstyle { \frac { 1 } { 2 } } } - { \frac { R } { 2 } } > 0$. Therefore, the area of the level surfaces grows as$f$ increases, and is converging to the area of the round sphere of scalar curvature one. On the other hand, the intrinsic scalar curvature of a level surface turns out to be less than one. Indeed, denoting by X the unit normal vector, this intrinsic curvature can be computed as

$$
R - 2 \mathrm{Ric} (X, X) + 2 \frac {\det (\mathrm{Hess} f)}{| \nabla f | ^ {2}} \leq R - 2 \mathrm{Ric} (X, X) + \frac {(1 - R + \mathrm{Ric} (X , X)) ^ {2}}{2 | \nabla f | ^ {2}} <   1
$$

when R is close to one and$| \nabla f |$is large. Thus we get a contradiction to the Gauss-Bonnet formula.

1.3 Now, having listed all the asymptotic solitons, we can classify the ancient κ-solutions. If such a solution has a compact asymptotic soliton, then it is itself a metric quotient of the round 3-sphere, because the positive curvature pinching can only improve in time [H 1]. If the asymptotic soliton contains the one-sided projective plane, then the solution has a$\mathbb { Z } _ { 2 }$cover, whose asymptotic soliton is the round infinite cylinder. Finally, if the asymptotic soliton is the cylinder,then the solution can be either noncompact (the round cylinder itself, or the Bryant soliton, for instance), or compact. The latter possibility, which was overlooked in the first paragraph of [I.11.7], is illustrated by the example below, which also gives the negative answer to the question in the very end of [I.5.1].

1.4 Example. Consider a solution to the Ricci flow, starting from a metric on${ \mathbb S } ^ { 3 }$that looks like a long round cylinder$\mathbb { S } ^ { 2 } \times \mathbb { I }$(say, with radius one and length$L > > 1 )$, with two spherical caps, smoothly attached to its boundary components. By [H 1] we know that the flow shrinks such a metric to a point in time, comparable to one (because both the lower bound for scalar curvature and the upper bound for sectional curvature are comparable to one) , and after normalization, the flow converges to the round 3-sphere. Scale the initial metric and choose the time parameter in such a way that the flow starts at time$t _ { 0 } =$ $t _ { 0 } ( L ) < 0$, goes singular at$t = 0$, and at$t = - 1$has the ratio of the maximal sectional curvature to the minimal one equal to$1 + \epsilon$. The argument in [I.7.3] shows that our solutions are κ-noncollapsed for some$\kappa > 0$independent of$L .$ We also claim that$t _ { 0 } ( L ) \longrightarrow - \infty$as$L \to \infty$. Indeed, the Harnack inequality of Hamilton [H 3] implies that$\begin{array} { r } { R _ { t } \geq \frac { R } { t _ { 0 } - t } } \end{array}$hence$\begin{array} { r } { R \leq { \frac { 2 ( - 1 - t _ { 0 } ) } { t - t _ { 0 } } } \operatorname { f o r } t \leq - 1 } \end{array}$ and then the distance change estimate$\begin{array} { r } { \frac { d } { d t } \mathrm { d i s t } _ { t } ( x , y ) \geq - \mathrm { c o n s t } \sqrt { R _ { \operatorname* { m a x } } ( t ) } } \end{array}$ from [H 2, 17] implies that the diameter of$g _ { i j } ( t _ { 0 } )$does not exceed const t , which is less than$L _ { \mathrm { { V } } } { = } t _ { 0 }$unless$t _ { 0 }$is large enough. Thus, a subsequence of our solutions with$L  \infty$converges to an ancient κ-solution on${ \mathbb S } ^ { 3 }$, whose asymptotic soliton can not be anything but the cylinder.

1.5 The important conclusion from the classification above and the proof of Proposition I.11.2 is that there exists$\kappa _ { 0 } > 0$, such that every ancient κ-solution is either$\kappa _ { 0 } { \mathrm { - s o l u t i o n } }$, or a metric quotient of the round sphere. Therefore, the compactness theorem I.11.7 implies the existence of a universal constant$\eta .$, such that at each point of every ancient κ-solution we have estimates

$$
| \nabla R | <   \eta R ^ {\frac {3}{2}}, | R _ {t} | <   \eta R ^ {2}\tag{1.3}
$$

Moreover, for every suficiently small$\epsilon > 0$one can find$C _ { 1 , 2 } = C _ { 1 , 2 } ( \epsilon )$, such that for each point$( x , t )$in every ancient κ-solution there is a radius$r , 0 < r <$ $C _ { 1 } R ( x , t ) ^ { - \frac { 1 } { 2 } }$, and a neighborhood B,$B ( x , t , r ) \subset B \subset B ( x , t , 2 r )$, which falls into one of the four categories:

(a) B is a strong ǫ-neck (more precisely, the slice of a strong ǫ-neck at its maximal time), or

(b) B is an ǫ-cap, or

(c) B is a closed manifold, difeomorphic to${ \mathbb S } ^ { 3 }$or$\mathbb { R } ^ { \mathbb { P } ^ { 3 } }$, or

(d) B is a closed manifold of constant positive sectional curvature;

furthermore, the scalar curvature in$B$at time t is between${ C } _ { 2 } ^ { - 1 } R ( x , t )$and $C _ { 2 } R ( x , t )$, its volume in cases$( \mathrm { a } ) , ( \mathrm { b } ) , ( \mathrm { c } )$is greater than$C _ { 2 } ^ { - 1 } R ( x , t ) ^ { - \frac { 3 } { 2 } }$, and in case (c) the sectional curvature in B at time t is greater than${ C } _ { 2 } ^ { - 1 } R ( x , t )$

## 2 The standard solution

Consider a rotationally symmetric metric on$\mathbb { R } ^ { 3 }$with nonnegative sectional curvature, which splits at infinity as the metric product of a ray and the round 2-sphere of scalar curvature one. At this point we make some choice for the metric on the cap, and will refer to it as the standard cap; unfortunately, the most obvious choice, the round hemisphere, does not fit, because the metric on $\mathbb { R } ^ { 3 }$would not be smooth enough, however we can make our choice as close to it as we like. Take such a metric on$\mathbb { R } ^ { 3 }$as the initial data for a solution$g _ { i j } ( t )$ to the Ricci flow on some time interval$[ 0 , T )$, which has bounded curvature for each$t \in [ 0 , T )$.

Claim 1. The solution is rotationally symmetric for all t.

Indeed, if$u ^ { i }$is a vector field evolving by$u _ { t } ^ { i } = \triangle u ^ { i } + R _ { i } ^ { i } u ^ { j }$, then$v _ { i j } = \nabla _ { i } u _ { j }$ evolves by$( v _ { i j } ) _ { t } = \triangle v _ { i j } + 2 R _ { i k j l } v _ { k l } - R _ { i k } v _ { k j } - R _ { k j } v _ { i k }$. Therefore, if$u ^ { i }$was a Killing field at time zero, it would stay Killing by the maximum principle. It is also clear that the center of the cap, that is the unique maximum point for the Busemann function, and the unique point, where all the Killing fields vanish, retains these properties, and the gradient of the distance function from this point stays orthogonal to all the Killing fields. Thus, the rotational symmetry is preserved.

Claim 2. The solution converges at infinity to the standard solution on the round infinite cylinder of scalar curvature one. In particular,$T \leq 1$

Claim 3. The solution is unique.

Indeed, using Claim 1, we can reduce the linearized Ricci flow equation to the system of two equations on$( - \infty , + \infty )$of the following type

$$
f _ {t} = f ^ {\prime \prime} + a _ {1} f ^ {\prime} + b _ {1} g ^ {\prime} + c _ {1} f + d _ {1} g, \quad g _ {t} = a _ {2} f ^ {\prime} + b _ {2} g ^ {\prime} + c _ {2} f + d _ {2} g,
$$

where the coeficients and their derivatives are bounded, and the unknowns$f , g$ and their derivatives tend to zero at infinity by Claim 2. So we get uniqueness by looking at the integrals$\textstyle \int _ { - A } ^ { A } ( f ^ { 2 } + g ^ { 2 } )$as$A \to \infty$

Claim 4. The solution can be extended to the time interval [0, 1).

Indeed, we can obtain our solution as a limit of the solutions on${ \mathbb S } ^ { 3 }$, starting from the round cylinder$\mathbb { S } ^ { 2 } \times \mathbb { I }$of length L and scalar curvature one, with two caps attached; the limit is taken about the center$p$of one of the caps,$L \to \infty$ Assume that our solution goes singular at some time$T < 1$. Take$T _ { 1 } ~ < ~ T$ very close to T,$T - T _ { 1 } < < 1 - T$. By Claim$2 ,$, given$\delta > 0$, we can find $\bar { L } , \bar { D } < \infty$, depending on$\delta$and$T _ { 1 }$, such that for any point x at distance$\bar { D }$ from$p$at time zero, in the solution with$L \geq \bar { L }$, the ball$B ( x , T _ { 1 } , 1 )$is δ-close to the corresponding ball in the round cylinder of scalar curvature$( 1 - T _ { 1 } ) ^ { - 1 }$ We can also find$r = r ( \delta , T )$, independent of$T _ { 1 }$, such that the ball$B ( x , T _ { 1 } , r )$ is δ-close to the corresponding euclidean ball. Now we can apply Theorem I.10.1 and get a uniform estimate on the curvature at$x$as$t  T$, provided that$T - T _ { 1 } < \epsilon ^ { 2 } r ( \delta , T ) ^ { 2 }$. Therefore, the$t  T$limit of our limit solution on the capped infinite cylinder will be smooth near$x .$Thus, this limit will be a positively curved space with a conical point. However, this leads to a contradiction via a blow-up argument; see the end of the proof of the Claim 2 in I.12.1.

The solution constructed above will be called the standard solution.

Claim 5. The standard solution satisfies the conclusions of 1.5 , for an appropriate choice$o f \epsilon , \eta , C _ { 1 } ( \epsilon ) , C _ { 2 } ( \epsilon )$, except that the ǫ-neck neighborhood need not be strong; more precisely, we claim that$i f \left( x , t \right)$has neither an ǫ-cap neighborhood as in$\boldsymbol { 1 . 5 ( b ) }$, nor a strong ǫ-neck neighborhood as in$1 . 5 ( a )$, then x is not in$B ( p , 0 , \epsilon ^ { - 1 } )$$t < 3 / 4$, and there is an ǫ-neck$B ( x , t , \epsilon ^ { - 1 } r )$, such that the solution in$P ( x , t , \epsilon ^ { - 1 } r , - t )$is, after scaling with factor$r ^ { - 2 }$, ǫ-close to the appropriate piece of the evolving round infinite cylinder.

Moreover, we have an estimate$R _ { \mathrm { m i n } } ( t ) \geq \mathrm { c o n s t } \cdot ( 1 - t ) ^ { - 1 }$

Indeed, the statements follow from compactness and Claim 2 on compact subintervals of [0, 1), and from the same arguments as for ancient solutions, when t is close to one.

## 3 The structure of solutions at the first singular time

Consider a smooth solution$g _ { i j } ( t )$to the Ricci flow on$M \times [ 0 , T )$, where M is a closed oriented 3-manifold,$T < \infty$. Assume that curvature of$g _ { i j } ( t )$does not stay bounded as$t \to T$. Recall that we have a pinching estimate Rm$\geq - \phi ( R ) R$ for some function φ decreasing to zero at infinity [H$^ { 4 , \ S 4 ] }$], and that the solution is κ-noncollapsed on the scales$\leq r$for some$\kappa > 0 , r > 0 [ \mathrm { I }$, 4].Then by Theorem I.12.1 and the conclusions of 1.5 we can find$r = r ( \epsilon ) > 0$, such that each point $( x , t )$with$R ( x , t ) \geq r ^ { - 2 }$satisfies the estimates (1.3) and has a neighborhood, which is either an ǫ-neck, or an ǫ-cap, or a closed positively curved manifold. In the latter case the solution becomes extinct at time$T ,$, so we don’t need to consider it any more.

If this case does not occur, then let Ω denote the set of all points in$M ,$ where curvature stays bounded as$t \to T$. The estimates (1.3) imply that$\Omega$is open and that$R ( x , t )  \infty { \mathrm { ~ a s ~ } } t  T$for each$x \in M \backslash \Omega$. If Ω is empty, then the solution becomes extinct at time$T$and it is entirely covered by ǫ-necks and caps shortly before that time, so it is easy to see that M is difeomorphic to either${ \mathbb S } ^ { 3 }$, or$\mathbb { R } \mathbb { P } ^ { 3 }$, or$\mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 1 }$, or$\mathbb { R P } ^ { 3 } \sharp \mathbb { R P } ^ { 3 }$

Otherwise, if Ω is not empty, we may (using the local derivative estimates due to W.-X.Shi, see$\mathrm { [ H 2 , \ S 1 3 ] ) }$consider a smooth metric$\bar { g } _ { i j }$on$\Omega$, which is the limit of$g _ { i j } ( t )$as$t \to T$. Let$\Omega _ { \rho }$for some$\rho < r$denotes the set of points$x \in \Omega$ where the scalar curvature$\bar { R } ( \dot { x } ) \le \rho ^ { - 2 }$. We claim that$\Omega _ { \rho }$is compact. Indeed, if $\bar { R } ( x ) \le \rho ^ { - 2 }$, then we can estimate the scalar curvature$R ( x , t )$on$[ T - \eta ^ { - 1 } \rho ^ { 2 } , T )$ using (1.3), and for earlier times by compactness, so x is contained in Ω with a ball of definite size, depending on$\rho .$

Now take any ǫ-neck in$( \Omega , \bar { g } _ { i j } )$and consider a point x on one of its boundary components. If$x \in \Omega \backslash \Omega _ { \rho } .$, then there is either an ǫ-cap or an ǫ-neck, adjacent to the initial ǫ-neck. In the latter case we can take a point on the boundary of the second ǫ-neck and continue. This procedure can either terminate when we reach a point in$\Omega _ { \rho }$or an ǫ-cap, or go on indefinitely, producing an ǫ-horn. The same procedure can be repeated for the other boundary component of the initial ǫ-neck. Therefore, taking into account that Ω has no compact components, we conclude that each ǫ-neck of$( \Omega , \bar { g } _ { i j } )$is contained in a subset of Ω of one of the following types:

(a) An ǫ-tube with boundary components in$\Omega _ { \rho } .$, or

(b) An ǫ-cap with boundary in$\Omega _ { \rho } ,$or

(c) An ǫ-horn with boundary in$\Omega _ { \rho } ,$or

(d) A capped ǫ-horn, or

(e) A double ǫ-horn.

Clearly, each ǫ-cap, disjoint from$\Omega _ { \rho } .$, is also contained in one of the subsets above. It is also clear that there is a definite lower bound (depending on$\rho )$for the volume of subsets of types$( \mathrm { a } ) , ( \mathrm { b } ) , ( \mathrm { c } )$, so there can be only finite number of them. Thus we can conclude that there is only a finite number of components of Ω, containing points of$\Omega _ { \rho } .$, and every such component has a finite number of ends, each being an ǫ-horn. On the other hand, every component of$\Omega$ containing no points of$\Omega _ { \rho } ,$is either a capped ǫ-horn, or a double ǫ-horn.

Now, by looking at our solution for times t just before T, it is easy to see that the topology of M can be reconstructed as follows: take the components $\Omega _ { j } , 1 \le j \le i$of Ω which contain points of$\Omega _ { \rho } ,$, truncate their ǫ-horns, and glue to the boundary components of truncated$\Omega _ { j }$a collection of tubes$\mathbb { S } ^ { 2 } \times \mathbb { I }$and caps $\mathbb { B } ^ { 3 } \ \mathrm { o r } \ \mathbb { R P } ^ { 3 } \backslash \bar { \mathbb { B } } ^ { 3 }$. Thus, M is difeomorphic to a connected sum of$\bar { \Omega } _ { j } , 1 \le j \le i ,$ with a finite number of$\mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 1 }$(which correspond to gluing a tube to two boundary components of the same$\Omega _ { j } )$, and a finite number of$\mathbb { R } \mathbb { P } ^ { 3 }$; here$\bar { \Omega } _ { j }$ denotes$\Omega _ { j }$with each ǫ-horn one point compactified.

## 4 Ricci flow with cutof

4.1 Suppose we are given a collection of smooth solutions$g _ { i j } ( t )$to the Ricci flow, defined on$M _ { k } \times [ t _ { k } ^ { - } , t _ { k } ^ { + } )$, which go singular as$t  t _ { k } ^ { + }$. Let$( \Omega _ { k } , \bar { g } _ { i j } ^ { k } )$be the limits of the corresponding solutions as$t  t _ { k } ^ { + }$, as in the previous section. Suppose also that for each k we have$t _ { k } ^ { - } = t _ { k - 1 } ^ { + }$, and$( \Omega _ { k - 1 } , \bar { g } _ { i j } ^ { k - 1 } )$and$( M _ { k } , g _ { i j } ^ { k } ( t _ { k } ^ { - } ) )$1 contain compact (possibly disconnected) three-dimensional submanifolds with smooth boundary, which are isometric. Then we can identify these isometric submanifolds and talk about the solution to the Ricci flow with surgery on the union of all$[ t _ { k } ^ { - } , t _ { k } ^ { + } )$

Fix a small number$\epsilon > 0$which is admissible in sections 1,2. In this section we consider only solutions to the Ricci flow with surgery, which satisfy the following a priori assumptions:

(pinching) There exists a function$\phi ,$decreasing to zero at infinity, such that $R m \ge - \phi ( R ) R$2

(canonical neighborhood) There exists$r > 0$, such that every point where scalar curvature is at least$r ^ { - 2 }$has a neighborhood, satisfying the conclusions of 1.5. (In particular, this means that if in case (a) the neighborhood in question is$B ( x _ { 0 } , t _ { 0 } , \epsilon ^ { - 1 } r _ { 0 } )$, then the solution is required to be defined in the whole $P ( x _ { 0 } , t _ { 0 } , \epsilon ^ { - 1 } r _ { 0 } , - r _ { 0 } ^ { 2 } )$; however, this does not rule out a surgery in the time interval$\left( { { t _ { 0 } } - r _ { 0 } ^ { 2 } , t _ { 0 } } \right)$, that occurs suficiently far from$x _ { 0 } . )$

Recall that from the pinching estimate of Ivey and Hamilton, and Theorem I.12.1, we know that the a priori assumptions above hold for a smooth solution on any finite time interval. For Ricci flow with surgery they will be justified in the next section.

4.2 Claim 1. Suppose we have a solution to the Ricci flow with surgery, satisfying the canonical neighborhood assumption, and let$Q = R ( x _ { 0 } , t _ { 0 } ) + r ^ { - 2 }$. Then we have estimate$R ( x , t ) \leq 8 Q$for those$( x , t ) \in P ( x _ { 0 } , t _ { 0 } , { \frac { 1 } { 2 } } \eta ^ { - 1 } Q ^ { - { \frac { 1 } { 2 } } } , - { \frac { 1 } { 8 } } \eta ^ { - 1 } Q ^ { - 1 } )$, for which the solution is defined.

Indeed, this follows from estimates (1.3).

Claim 2. For any$A < \infty$one can find$Q = Q ( A ) < \infty$and$\xi = \xi ( A ) > 0$ with the following property. Suppose we have a solution to the Ricci flow with surgery, satisfying the pinching and the canonical neighborhood assumptions. Let$\gamma$be a shortest geodesic in$g _ { i j } \big ( t _ { 0 } \big )$with endpoints$x _ { 0 }$and$x ,$such that$R ( y , t _ { 0 } ) ~ > ~ r ^ { - 2 }$for each$y \in \gamma ,$and$Q _ { 0 } ~ = ~ R ( x _ { 0 } , t _ { 0 } )$is so large that $\phi ( Q _ { 0 } ) < \xi$. Finally, let$z \in \gamma$be any point satisfying$R ( z , t _ { 0 } ) > 1 0 C _ { 2 } R ( x _ { 0 } , t _ { 0 } )$ Then dis$\ u _ { \cdot t _ { 0 } } ( x _ { 0 } , z ) \geq A Q _ { 0 } ^ { - \frac 1 2 }$whenever$R ( x , t _ { 0 } ) > Q Q _ { 0 }$

The proof is exactly the same as for Claim 2 in Theorem I.12.1; in the very end of it, when we get a piece of a non-flat metric cone as a blow-up limit, we get a contradiction to the canonical neighborhood assumption, because the canonical neighborhoods of types other than (a) are not close to a piece of metric cone, and type (a) is ruled out by the strong maximum principle, since the ǫ-neck in question is strong.

4.3 Suppose we have a solution to the Ricci flow with surgery, satisfying our a priori assumptions, defined on [0, T), and going singular at time T. Choose a small$\delta > 0$and let$\rho = \delta r$. As in the previous section, consider the limit$( \Omega , \bar { g } _ { i j } )$ of our solution as$t \to T$, and the corresponding compact set$\Omega _ { \rho }$

Lemma. There exists a radius$h , 0 < h < \delta \rho$, depending only on$\delta , \rho$and the pinching function φ, such that for each point x with$h ( x ) = \bar { R } ^ { - \frac 1 2 } ( x ) \le h$in an ǫ- horn of$( \Omega , \bar { g } _ { i j } )$with boundary in$\Omega _ { \rho } .$, the neighborhood$P ( x , T , \delta ^ { - 1 } h ( x ) , - h ^ { 2 } ( x ) )$1 is a strong δ-neck.

Proof. An argument by contradiction. Assuming the contrary, take a sequence of solutions with limit metrics$( \Omega ^ { \alpha } , \bar { g } _ { i j } ^ { \alpha } )$and points$x ^ { \alpha }$with$h ( x ^ { \alpha } ) \to 0$ Since$x ^ { \alpha }$lies deeply inside an ǫ-horn, its canonical neighborhood is a strong ǫ-neck. Now Claim 2 gives the curvature estimate that allows us to take a limit of appropriate scalings of the metrics$g _ { i j } ^ { \alpha }$on$[ T - h ^ { 2 } ( x ^ { \alpha } ) , T ]$about$x ^ { \alpha }$, for a subsequence of$\alpha \to \infty$. By shifting the time parameter we may assume that the limit is defined on [ 1, 0]. Clearly, for each time in this interval, the limit is a complete manifold with nonnegative sectional curvature; moreover, since$x ^ { \alpha }$was contained in an ǫ-horn with boundary in$\Omega _ { \rho } ^ { \alpha }$, and$h ( x ^ { \alpha } ) / \rho \to 0$, this manifold has two ends. Thus, by Toponogov, it admits a metric splitting$\mathbb { S } ^ { 2 } \times \mathbb { R }$. This implies that the canonical neighborhood of the point$( x ^ { \alpha } , T - h ^ { 2 } ( x ^ { \alpha } ) )$is also of type (a), that is a strong ǫ-neck, and we can repeat the procedure to get the limit, defined on [ 2, 0], and so on. This argument works for the limit in any finite time interval$[ - A , 0 ]$, because$h ( x ^ { \alpha } ) / \rho \to 0$. Therefore, we can construct a limit on$[ - \infty , 0 ]$; hence it is the round cylinder, and we get a contradiction.

4.4 Now we can specialize our surgery and define the Ricci flow with$\delta \mathrm { \cdot }$-cutof. Fix$\delta > 0$, compute$\rho = \delta r$and determine h from the lemma above. Given a smooth metric$g _ { i j }$on a closed manifold, run the Ricci flow until it goes singular at some time$t ^ { + } ;$form the limit$( \Omega , \bar { g } _ { i j } )$. If$\Omega _ { \rho }$is empty, the procedure stops here, and we say that the solution became extinct. Otherwise we remove the components of Ω which contain no points of$\Omega _ { \rho } .$, and in every ǫ-horn of each of the remaining components we find a δ-neck of radius$h ,$cut it along the middle two-sphere, remove the horn-shaped end, and glue in an almost standard cap in such a way that the curvature pinching is preserved and a metric ball of radius$( \delta ^ { \prime } ) ^ { - 1 } h$centered near the center of the cap is, after scaling with factor $h ^ { - 2 } , \delta ^ { \prime }$-close to the corresponding ball in the standard capped infinite cylinder, considered in section 2. (Here$\delta ^ { \prime }$is a function of δ alone, which tends to zero with δ.)

The possibility of capping a δ-neck preserving a certain pinching condition in dimension four was proved by Hamilton [H$5 , \ S 4 ] ;$his argument works in our case too (and the estimates are much easier to verify). The point is that we can change our δ-neck metric near the middle of the neck by a conformal factor $e ^ { - f }$, where$f = f ( z )$is positive on the part of the neck we want to remove, and zero on the part we want to preserve, and z is the coordinate along I in our parametrization$\mathbb { S } ^ { 2 } \times \mathbb { I }$of the neck. Then, in the region near the middle of the neck, where f is small, the dominating terms in the formulas for the change of curvature are just positive constant multiples of$f ^ { \prime \prime }$, so the pinching improves, and all the curvatures become positive on the set where$f > \delta ^ { \prime }$

Now we can continue our solution until it becomes singular for the next time. Note that after the surgery the manifold may become disconnected; in this case, each component should be dealt with separately. Furthermore, let us agree to declare extinct every component which is ǫ-close to a metric quotient of the round sphere; that allows to exclude such components from the list of canonical neighborhoods. Now since every surgery reduces the volume by at least$h ^ { 3 }$, the sequence of surgery times is discrete, and, taking for granted the a priori assumptions, we can continue our solution indefinitely, not ruling out the possibility that it may become extinct at some finite time.

4.5 In order to justify the canonical neighborhood assumption in the next section, we need to check several assertions.

Lemma. For any$A < \infty , 0 < \theta < 1$, one can find$\bar { \delta } = \bar { \delta } ( A , \theta )$with the following property. Suppose we have a solution to the Ricci flow with$\delta \mathrm { - } c u t o f f ,$ satisfying the a priori assumptions on [0, T], with$\delta < \bar { \delta }$Suppose we have a surgery at time$T _ { 0 } \in ( 0 , T )$, let$p$correspond to the center of the standard cap, and let$T _ { 1 } =$min$( T , T _ { 0 } + \theta h ^ { 2 } )$. Then either

(a) The solution is defined on$P ( p , T _ { 0 } , A h , T _ { 1 } - T _ { 0 } )$, and is, after scaling with factor$h ^ { - 2 }$and shifting time$T _ { 0 }$to zero,$A ^ { - 1 }$-close to the corresponding subset on the standard solution from section${ \it 2 } ,$or

(b) The assertion$( a )$holds with$T _ { 1 }$replaced by some time$t ^ { + } \in [ T _ { 0 } , T _ { 1 } )$, where $t ^ { + }$is a surgery time; moreover, for each point in$B ( p , T _ { 0 } , A h )$), the solution is defined$f o r t \in [ T _ { 0 } , t ^ { + } )$and is not defined past$t ^ { + }$.

Proof. Let Q be the maximum of the scalar curvature on the standard solution in the time interval$[ 0 , \theta ]$, let$\triangle t = N ^ { - 1 } ( T _ { 1 } - T _ { 0 } ) < \epsilon \eta ^ { - 1 } Q ^ { - 1 } h ^ { 2 }$, and let$t _ { k } = T _ { 0 } + k \triangle t , k = 0 , . . . , N$

Assume first that for each point in$B ( p , T _ { 0 } , A _ { 0 } h )$, where$A _ { 0 } = \epsilon ( \delta ^ { \prime } ) ^ { - 1 }$, the solution is defined on$[ t _ { 0 } , t _ { 1 } ]$. Then by (1.3) and the choice of$\triangle t$we have a uniform curvature bound on this set for$h ^ { - 2 }$-scaled metric. Therefore we can define$A _ { 1 }$, depending only on$A _ { 0 }$and tending to infinity with$A _ { 0 } .$, such that the solution in$P ( p , T _ { 0 } , A _ { 1 } h , t _ { 1 } - t _ { 0 } )$is, after scaling and time shifting,$A _ { 1 } ^ { - 1 } .$ close to the corresponding subset in the standard solution. In particular, the scalar curvature on this subset does not exceed$2 Q h ^ { - 2 }$. Now if for each point in $B ( p , T _ { 0 } , A _ { 1 } h )$the solution is defined on$[ t _ { 1 } , t _ { 2 } ]$, then we can repeat the procedure, defining$A _ { 2 }$etc. Continuing this way, we eventually define$A _ { N }$, and it would remain to choose δ so small, and correspondingly$A _ { 0 }$so large, that$A _ { N } > A$

Now assume that for some$k , 0 \leq k < N$, and for some$x \in B ( p , T _ { 0 } , A _ { k } h )$the solution is defined on$[ t _ { 0 } , t _ { k } ]$but not on$[ t _ { k } , t _ { k + 1 } ]$. Then we can find a surgery time$t ^ { + } \in [ t _ { k } , t _ { k + 1 } ]$, such that the solution on$B ( p , T _ { 0 } , A _ { k } h )$is defined on$[ t _ { 0 } , t ^ { + } )$ but for some points of this ball it is not defined past$t ^ { + }$. Clearly, the$A _ { k + 1 } ^ { - 1 } -$ closeness assertion holds on$P ( p , T _ { 0 } , A _ { k + 1 } h , t ^ { + } - T _ { 0 } )$. On the other hand, the solution on$B ( p , T _ { 0 } , A _ { k } h )$is at least ǫ-close to the standard one for all$t \in [ t _ { k } , t ^ { + } )$ hence no point of this set can be the center of a δ-neck neighborhood at time $t ^ { + }$. However, the surgery is always done along the middle two-sphere of such a neck. It follows that for each point of$B ( p , T _ { 0 } , A _ { k } h )$the solution terminates at $t ^ { + }$

4.6 Corollary. For any$l < \infty$one can find$A = A ( l ) < \infty$and$\theta \ : = \ :$ $\theta ( l ) , 0 < \theta < 1$, with the following property. Suppose we are in the situation of the lemma above, with$\delta ~ < ~ \bar { \delta } ( A , \theta )$. Consider smooth curves$\gamma$in the set $B ( p , T _ { 0 } , A h )$, parametrized by$t \in \mathsf { [ } T _ { 0 } , T _ { \gamma } ]$, such that$\gamma ( T _ { 0 } ) \in B ( p , T _ { 0 } , A h / 2 )$ and either$T _ { \gamma } ~ = ~ T _ { 1 } ~ < ~ T _ { \ }$, or$T _ { \gamma } ~ < ~ T _ { 1 }$and$\gamma ( T _ { \gamma } ) ~ \in ~ \partial B ( p , T _ { 0 } , A h )$. Then $\begin{array} { r } { \int _ { T _ { 0 } } ^ { T _ { \gamma } } ( R ( \gamma ( t ) , t ) + | \dot { \gamma } ( t ) | ^ { 2 } ) d t > l . } \end{array}$

Proof. Indeed, if$T _ { \gamma } = T _ { 1 }$, then on the standard solution we would have $\begin{array} { r } { \int _ { T _ { 0 } } ^ { T _ { \gamma } } R ( \gamma ( t ) , t ) d t \geq \mathrm { c o n s t } \int _ { 0 } ^ { \theta } ( 1 - t ) ^ { - 1 } d t = - \mathrm { c o n s t } \cdot ( \log ( 1 - \theta ) ) ^ { - 1 } } \end{array}$, so by choosing θ suficiently close to one we can handle this case. Then we can choose A so large that on the standard solution di$\mathrm { { s t } } _ { t } ( p , \partial B ( p , 0 , A ) ) \geq 3 A / 4$for each$t \in [ 0 , \theta ]$ Now${ \mathrm { i f } } \gamma ( T _ { \gamma } ) \in \partial B ( p , T _ { 0 } , A h )$then$\textstyle \int _ { T _ { 0 } } ^ { T _ { \gamma } } | \dot { \gamma } ( t ) | ^ { 2 } d t \geq A ^ { 2 } / 1 0 0$, so by taking A large enough, we can handle this case as well.

4.7 Corollary. For any$Q < \infty$there exists$\theta = \theta ( Q ) , 0 < \theta < 1$with the following property. Suppose we are in the situation of the lemma above, with$\delta < \bar { \delta } ( A , \theta ) , A > \epsilon ^ { - 1 }$. Suppose that for some point$x \in B ( p , T _ { 0 } , A h )$the solution is defined at x (at least) on$[ T _ { 0 } , T _ { x } ] , T _ { x } \leq T$, and satisfies$Q ^ { - 1 } R ( x , t ) \leq$ $R ( x , T _ { x } ) \leq Q ( T _ { x } - T _ { 0 } ) ^ { - 1 }$for$a l l \ t \in [ T _ { 0 } , T _ { x } ]$. Then$T _ { x } \le T _ { 0 } + \theta h ^ { 2 }$

Proof. Indeed, if$T _ { x } > T _ { 0 } + \theta h ^ { 2 }$, then by lemma$R ( x , T _ { 0 } + \theta h ^ { 2 } ) \ge$ const$( 1 - \theta ) ^ { - 1 } h ^ { - 2 }$, whence$R ( x , T _ { x } ) \ge \mathrm { c o n s t } \cdot Q ^ { - 1 } ( 1 - \theta ) ^ { - 1 } h ^ { - 2 }$, and$T _ { x } - T _ { 0 } \leq$ const$Q ^ { 2 } ( 1 - \theta ) h ^ { 2 } < \theta h ^ { 2 }$if θ is close enough to one.

## 5 Justification of the a priori assumption

5.1 Let us call a riemannian manifold$( M , g _ { i j } )$normalized if M is a closed oriented 3-manifold, the sectional curvatures of$g _ { i j }$do not exceed one in absolute value, and the volume of every metric ball of radius one is at least half the volume of the euclidean unit ball. For smooth Ricci flow with normalized initial data we have, by [H 4, 4.1], at any time$t > 0$the pinching estimate

$$
R m \geq - \phi (R (t + 1)) R,\tag{5.1}
$$

where$\phi$is a decreasing function, which behaves at infinity like$\textstyle { \frac { 1 } { \log } }$. As explained in$4 . 4 ,$this pinching estimate can be preserved for Ricci flow with δ-cutof. Justification of the canonical neighborhood assumption requires additional arguments. In fact, we are able to construct solutions satisfying this assumption only allowing r and δ be functions of time rather than constants; clearly, the arguments of the previous section are valid in this case, if we assume that r(t), δ(t) are non-increasing, and bounded away from zero on every finite time interval.

Proposition. There exist decreasing sequences$0 < r _ { j } < \epsilon ^ { 2 } , \kappa _ { j } > 0 , 0 <$ $\bar { \delta } _ { j } < \epsilon ^ { 2 } , j = 1 , 2 , \ldots$, such that for any normalized initial data and any function $\delta ( t )$, satisfying$0 < \delta ( t ) < \bar { \delta } _ { j }$for$t \in [ 2 ^ { j - 1 } \epsilon , 2 ^ { j } \epsilon ]$, the Ricci flow with$\delta ( t ) - c u t o f f$ is defined for$t \in [ 0 , + \infty ]$and satisfies the$\kappa _ { j }$-noncollapsing assumption and the canonical neighborhood assumption with parameter$r _ { j }$on the time interval$[ 2 ^ { j - 1 } \epsilon , 2 ^ { j } \epsilon ] . ($Recall that we have excluded from the list of canonical neighborhoods the closed manifolds, ǫ-close to metric quotients of the round sphere. Complete extinction of the solution in finite time is not ruled out.)

The proof of the proposition is by induction: having constructed our sequences for$1 \leq j \leq i$we make one more step, defining$r _ { i + 1 } , \kappa _ { i + 1 } , \bar { \delta } _ { i + 1 }$, and redefining$\bar { \delta } _ { i } = \bar { \delta } _ { i + 1 } ;$each step is analogous to the proof of Theorem I.12.1.

First we need to check a κ-noncollapsing condition.

5.2 Lemma. Suppose we have constructed the sequences, satisfying the proposition for$1 \leq j \leq i$. Then there exists$\kappa > 0 .$, such that for any$r , 0 < r <$ $\epsilon ^ { 2 }$, one can find$\bar { \delta } = \bar { \delta } ( r ) > 0$, which may also depend on the already constructed sequences, with the following property. Suppose we have a solution to the Ricci flow with δ(t)-cutof on a time interval$[ 0 , T ]$, with normalized initial data, satisfying the proposition on$[ 0 , 2 ^ { i } \epsilon ]$, and the canonical neighborhood assumption with parameter r$o n \left[ 2 ^ { i } \epsilon , T \right]$, where$2 ^ { i } \epsilon \le T \le 2 ^ { i + 1 } \epsilon$ǫ,$0 < \delta ( t ) < \bar { \delta }$for$t \in [ 2 ^ { i - 1 } \epsilon , T ]$ Then it is κ-noncollapsed on all scales less than ǫ.

Proof. Consider a neighborhood$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } , - r _ { 0 } ^ { 2 } ) , 2 ^ { i } \epsilon < t _ { 0 } \leq T , 0 < r _ { 0 } <$ $\epsilon ,$where the solution is defined and satisfies$| R m | \leq r _ { 0 } ^ { - 2 }$. We may assume $r _ { 0 } \geq r ,$since otherwise the lower bound for the volume of the ball$B ( x _ { 0 } , t _ { 0 } , r _ { 0 } )$ follows from the canonical neighborhood assumption. If the solution was smooth everywhere, we could estimate from below the volume of the ball$B ( x _ { 0 } , t _ { 0 } , r _ { 0 } )$ using the argument from [I.7.3]: define$\tau ( t ) = t _ { 0 } - t$and consider the reduced volume function using the -exponential map from x ; take a point$( x , \epsilon )$where the reduced distance l attains its minimum for$\tau = t _ { 0 } - \epsilon , ~ l ( x , \tau ) \leq 3 / 2$; use it to obtain an upper bound for the reduced distance to the points of$B ( x , 0 , 1 )$, thus getting a lower bound for the reduced volume at$\tau = t _ { 0 }$, and apply the monotonicity formula. Now if the solution undergoes surgeries, then we still can measure the -length, but only for admissible curves, which stay in the region, unafected by surgery. An inspection of the constructions in [I, 7] shows that the argument would go through if we knew that every barely admissible curve, that is a curve on the boundary of the set of admissible curves, has reduced length at least$3 / 2 + \kappa ^ { \prime }$for some fixed$\kappa ^ { \prime } > 0$. Unfortunately, at the moment I don’t see how to ensure that without imposing new restrictions on$\delta ( t )$for all $t \in [ 0 , T ]$, so we need some additional arguments.

Recall that for a curve γ, parametrized by t, with$\gamma ( t _ { 0 } ) ~ = ~ x _ { 0 }$, we have $\begin{array} { r } { \mathcal L ( \gamma , \tau ) = \int _ { t _ { 0 } - \tau } ^ { t _ { 0 } } \sqrt { t _ { 0 } - t } ( R ( \gamma ( t ) , t ) + | \dot { \gamma } ( t ) | ^ { 2 } ) d t } \end{array}$. We can also define$\mathcal { L } _ { + } ( \gamma , \tau )$by replacing in the previous formula R with$R _ { + } = \operatorname* { m a x } ( R , 0 )$. Then$\mathcal { L } _ { + } \leq \mathcal { L } { + } 4 T \sqrt { T }$ because$R \geq - 6$by the maximum principle and normalization. Now suppose we could show that every barely admissible curve with endpoints$( x _ { 0 } , t _ { 0 } )$and$( x , t )$ where$t \in [ 2 ^ { i - 1 } \epsilon , T )$, has$\begin{array} { r } { \mathcal { L } _ { + } > 2 \epsilon ^ { - 2 } T \sqrt { T } ; } \end{array}$then we could argue that either there exists a point$( x , t ) , t \in [ 2 ^ { i - 1 } \epsilon , 2 ^ { i } \epsilon ]$, such that$R ( x , t ) \leq r _ { i } ^ { - 2 }$and$\begin{array} { r } { \mathcal { L } _ { + } \le \epsilon ^ { - 2 } T \sqrt { T } } \end{array}$ in which case we can take this point in place of$( x , \epsilon )$in the argument of the previous paragraph, and obtain (using Claim 1 in 4.2) an estimate for κ in terms of$r _ { i } , \kappa _ { i } , T .$, or for any γ, defined on$[ 2 ^ { i - 1 } \epsilon , t _ { 0 } ] , \gamma ( t _ { 0 } ) = x _ { 0 }$, we have$\mathcal { L } _ { + } \geq$ min$( \epsilon ^ { - 2 } T \sqrt { T } , { \textstyle \frac { 2 } { 3 } } ( 2 ^ { i - 1 } \epsilon ) ^ { \frac { 3 } { 2 } } r _ { i } ^ { - 2 } ) > \epsilon ^ { - 2 } T \sqrt { T }$, which is in contradiction with the assumed bound for barely admissible curves and the bound min$l ( x , t _ { 0 } - 2 ^ { i - 1 } \epsilon ) \le$ $3 / 2$, valid in the smooth case. Thus, to conclude the proof it is suficient to check the following assertion.

5.3 Lemma. For any$\mathcal { L } \mathrm { ~ < ~ } \infty$one can find$\bar { \delta } = \bar { \delta } ( \mathcal { L } , r _ { 0 } ) > 0$with the following property. Suppose that in the situation of the previous lemma we have a curve γ, parametrized by$t \in [ T _ { 0 } , t _ { 0 } ] , 2 ^ { i - 1 } \epsilon \leq T _ { 0 } < t _ { 0 }$, such that$\gamma ( t _ { 0 } ) = x _ { 0 }$ $T _ { 0 }$is a surgery time, and$\gamma ( T _ { 0 } ) \in B ( p , T _ { 0 } , \epsilon ^ { - 1 } h )$, where p corresponds to the center of the cap, and h is the radius of the δ-neck. Then we have an estimate $\begin{array} { r } { \int _ { T _ { 0 } } ^ { t _ { 0 } } \sqrt { t _ { 0 } - t } ( R _ { + } ( \dot { \gamma } ( t ) , t ) + | \dot { \gamma } ( t ) | ^ { 2 } ) d t \ge \mathcal { L } } \end{array}$

Proof. It is clear that if we take$\triangle t = \epsilon r _ { 0 } ^ { 4 } { \mathcal { L } } ^ { - 2 }$, then either γ satisfies our estimate, or γ stays in$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } , - \triangle t )$for$t \in [ t _ { 0 } - \triangle t , t _ { 0 } ]$. In the latter case our estimate follows from Corollary 4.6, for$l = \mathcal { L } ( \triangle t ) ^ { - \frac { 1 } { 2 } }$, since clearly $T _ { \gamma } < t _ { 0 } - \triangle t$when δ is small enough.

5.4 Proof of proposition. Assume the contrary, and let the sequences$r ^ { \alpha } , \bar { \delta } ^ { \alpha \beta }$ be such that$r ^ { \alpha } \to 0$as$\alpha  \infty$，$\bar { \delta } ^ { \alpha \beta }  0$as$\beta \to \infty$with fixed$\alpha ,$and let $( M ^ { \alpha \beta } , g _ { i j } ^ { \alpha \beta } )$be normalized initial data for solutions to the Ricci flow with$\delta ( t ) .$ cutof,$\delta \bar { ( t ) } < \bar { \delta } ^ { \alpha \beta } \mathrm { o n } \left[ 2 ^ { i - 1 } \epsilon , 2 ^ { i + 1 } \epsilon \right]$, which satisfy the statement on$[ 0 , 2 ^ { i } \epsilon ]$, but violate the canonical neighborhood assumption with parameter$r ^ { \alpha }$on$[ 2 ^ { i } \epsilon , 2 ^ { i + 1 } \epsilon ]$ Slightly abusing notation, we’ll drop the indices$\alpha , \beta$when we consider an individual solution.

Let t<sup>¯</sup> be the first time when the assumption is violated at some point${ \bar { x } } ;$ clearly such time exists, because it is an open condition. Then by lemma 5.2 we have uniform κ-noncollapsing on [0, t<sup>¯</sup>]. Claims 1,2 in 4.2 are also valid on$[ 0 , { \vec { t } } ] ;$ moreover, since$h < < r .$it follows from Claim 1 that the solution is defined on the whole parabolic neighborhood indicated there in case$R ( x _ { 0 } , t _ { 0 } ) \leq r ^ { - 2 }$

Scale our solution about$( { \bar { x } } , { \bar { t } } )$with factor$R ( { \bar { x } } , { \bar { t } } ) \geq r ^ { - 2 }$and take a limit for subsequences of$\alpha , \beta \to \infty . \mathrm { ~ A t ~ }$t time$\bar { t } ,$which we’ll shift to zero in the limit, the curvature bounds at finite distances from ¯x for the scaled metric are ensured by Claim 2 in 4.2. Thus, we get a smooth complete limit of nonnegative sectional curvature, at time zero. Moreover, the curvature of the limit is uniformly bounded, since otherwise it would contain ǫ-necks of arbitrarily small radius.

Let$Q _ { 0 }$denote the curvature bound. Then, if there was no surgery, we could, using Claim 1 in 4.2, take a limit on the time interval$[ - \epsilon \eta ^ { - 1 } Q _ { 0 } ^ { - 1 } , 0 ]$. To prevent this, there must exist surgery times$T _ { 0 } \in [ \bar { t } - \epsilon \eta ^ { - 1 } \dot { Q _ { 0 } ^ { - 1 } } R ^ { - 1 } ( \bar { x } , \bar { t } ) , \bar { t } ]$and points x with dis$\mathrm { t } _ { T _ { 0 } } ^ { 2 } ( x , \bar { x } ) R ^ { - 1 } ( \bar { x } , \bar { t } )$uniformly bounded as$\alpha , \beta \to \infty$, such that the solution at x is defined on$[ T _ { 0 } , \vec { t } ]$, but not before$T _ { 0 } .$. Using Claim 2 from 4.2 at time$T _ { 0 }$, we see that$R ( \bar { x } , \bar { t } ) h ^ { 2 } ( T _ { 0 } )$must be bounded away from zero. Therefore, in this case we can apply Corollary 4.7, Lemma 4.5 and Claim 5 in section 2 to show that the point$( { \bar { x } } , { \bar { t } } )$in fact has a canonical neighborhood, contradicting its choice. (It is not excluded that the strong ǫ-neck neighborhood extends to times before$T _ { 0 } .$, where it is a part of the strong δ-neck that existed before surgery.)

Thus we have a limit on a certain time interval. Let$Q _ { 1 }$be the curvature bound for this limit. Then we either can construct a limit on the time interval $[ - \epsilon \eta ^ { - 1 } ( Q _ { 0 } ^ { - 1 } + Q _ { 1 } ^ { - 1 } ) , 0 ]$, or there is a surgery, and we get a contradiction as before. We can continue this procedure indefinitely, and the final part of the proof of Theorem I.12.1 shows that the bounds$Q _ { k }$can not$_ { \mathrm { g o } }$to infinity while the limit is defined on a bounded time interval. Thus we get a limit on$( - \infty , 0 ]$ which is κ-noncollapsed by Lemma 5.2, and this means that$( { \bar { x } } , { \bar { t } } )$has a canonical neighborhood by the results of section 1 - a contradiction.

## 6 Long time behavior I

6.1 Let us summarize what we have achieved so far. We have shown the existence of decreasing (piecewise constant) positive functions$r ( t )$and$\bar { \delta } ( t )$(which we may assume converging to zero at infinity), such that if$( M , g _ { i j } )$is a normalized manifold, and$0 < \delta ( t ) < \bar { \delta } ( t )$, then there exists a solution to the Ricci flow with$\delta ( t )$-cutof on the time interval$\lbrack 0 , + \infty ]$, starting from$( M , g _ { i j } )$and satisfying on each subinterval [0, t] the canonical neighborhood assumption with parameter$r ( t )$, as well as the pinching estimate (5.1).

In particular, if the initial data has positive scalar curvature, say$R \geq a > 0$2 then the solution becomes extinct in time at most$\frac { 3 } { 2 a }$, and it follows that M in this case is difeomorphic to a connected sum of several copies of$\mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 1 }$and metric quotients of round$\mathbb { S } ^ { 3 }$. ( The topological description of 3-manifolds with positive scalar curvature modulo quotients of homotopy spheres was obtained by Schoen-Yau and Gromov-Lawson more than 20 years ago, see [G-L] for instance; in particular, it is well known and easy to check that every manifold that can be decomposed in a connected sum above admits a metric of positive scalar curvature.) Moreover, if the scalar curvature is only nonnegative, then by the strong maximum principle it instantly becomes positive unless the metric is (Ricci-)flat; thus in this case, we need to add to our list the flat manifolds.

However, if the scalar curvature is negative somewhere, then we need to work more in order to understand the long tome behavior of the solution. To achieve this we need first to prove versions of Theorems I.12.2 and I.12.3 for solutions with cutof.

6.2 Correction to Theorem I.12.2. Unfortunately, the statement of Theorem I.12.2 was incorrect. The assertion I had in mind is as follows:

Given a function φ as above, for any$A < \infty$there exist$K = K ( A ) < \infty$ and$\rho = \rho ( A ) > 0$with the following property. Suppose in dimension three we have a solution to the Ricci flow with φ-almost nonnegative curvature, which satisfies the assumptions of theorem 8.2 for some$x _ { 0 } , r _ { 0 }$with$\phi \big ( r _ { 0 } ^ { - 2 } \big ) < \rho$. Then

$R ( x , r _ { 0 } ^ { 2 } ) \leq K r _ { 0 } ^ { - 2 }$whenever dist$_ { r _ { 0 } ^ { 2 } } ( x , x _ { 0 } ) < A r _ { 0 }$

It is this assertion that was used in the proof of Theorem I.12.3 and Corollary I.12.4.

6.3 Proposition. For any$A < \infty$one can find$\kappa = \kappa ( A ) > 0 , K _ { 1 } =$ $K _ { 1 } ( A ) < \infty , K _ { 2 } = K _ { 2 } ( A ) < \infty , \bar { r } = \bar { r } ( A ) > 0$, such that for any$t _ { 0 } < \infty$there exists$\bar { \delta } = \bar { \delta } _ { A } ( t _ { 0 } ) > 0$, decreasing in$t _ { 0 } .$with the following property. Suppose we have a solution to the Ricci flow with$\delta ( t )$-cutof on time interval$[ 0 , T ] , \delta ( t ) <$ $\bar { \delta } ( t ) \ o n [ 0 , T ] , \ \delta ( t ) < \bar { \delta } \ o n [ t _ { 0 } / 2 , t _ { 0 } ]$, with normalized initial data; assume that the solution is defined in the whole parabolic neighborhood$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } , - r _ { 0 } ^ { 2 } ) , \ 2 r _ { 0 } ^ { 2 } <$ $t _ { 0 }$, and satisfies$| R m | \leq r _ { 0 } ^ { - 2 }$there, and that the volume of the ball$B ( x _ { 0 } , t _ { 0 } , r _ { 0 } )$ is at least$A ^ { - 1 } r _ { 0 } ^ { 3 }$. Then

(a) The solution is κ-noncollapsed on the scales less than$r _ { 0 }$in the ball $B ( x _ { 0 } , t _ { 0 } , A r _ { 0 } )$

(b) Every point$x \in B ( x _ { 0 } , t _ { 0 } , A r _ { 0 } )$with$R ( x , t _ { 0 } ) \geq K _ { 1 } r _ { 0 } ^ { - 2 }$has a canonical neighborhood as in$4 . 1 .$

(c)$I f r _ { 0 } \leq \bar { r } \sqrt { t _ { 0 } }$then$R \leq K _ { 2 } r _ { 0 } ^ { - 2 }$in$B ( x _ { 0 } , t _ { 0 } , A r _ { 0 } )$

Proof. (a) This is an analog of Theorem I.8.2. Clearly we have κ-noncollapsing on the scales less than$r ( t _ { 0 } )$, so we may assume$r ( t _ { 0 } ) \leq r _ { 0 } \leq \sqrt { t _ { 0 } / 2 }$, and study the scales$\rho , r ( t _ { 0 } ) \leq \rho \leq r _ { 0 }$. In particular, for fixed$t _ { 0 }$we are interested in the scales, uniformly equivalent to one.

So assume that$x \in B ( x _ { 0 } , t _ { 0 } , A r _ { 0 } )$and the solution is defined in the whole $P ( x , t _ { 0 } , \rho , - \rho ^ { 2 } )$and satisfies$| R m | \leq \rho ^ { - 2 }$there. An inspection of the proof of I.8.2 shows that in order to make the argument work it sufices to check that for any barely admissible curve$\gamma _ { : }$, parametrized by$t \in [ t _ { \gamma } , t _ { 0 } ] , t _ { 0 } - r _ { 0 } ^ { 2 } \leq t _ { \gamma } \leq t _ { 0 }$ such that$\gamma ( t _ { 0 } ) = x$, we have an estimate

$$
2 \sqrt {t _ {0} - t _ {\gamma}} \int_ {t _ {\gamma}} ^ {t _ {0}} \sqrt {t _ {0} - t} (R (\gamma (t), t) + | \dot {\gamma} (t) | ^ {2}) d t \geq C (A) r _ {0} ^ {2}\tag{6.1}
$$

for a certain function$C ( A )$that can be made explicit. Now we would like to conclude the proof by using Lemma 5.3. However, unlike the situation in Lemma 5.2, here Lemma 5.3 provides the estimate we need only if$t _ { 0 } - t _ { \gamma }$is bounded away from zero, and otherwise we only get an estimate$\rho ^ { 2 }$in place of$C ( A ) r _ { 0 } ^ { 2 }$ Therefore we have to return to the proof of I.8.2.

Recall that in that proof we scaled the solution to make$r _ { 0 } = 1$and worked on the time interval$[ 1 / 2 , 1 ]$. The maximum principle for the evolution equation of the scalar curvature implies that on this time interval we have$R \geq - 3$. We considered a function of the form$h ( y , t ) = \phi ( \hat { d } ( y , t ) ) \hat { L } ( y , \tau )$, where φ is a certain cutof function,$\tau = 1 - t , \hat { d } ( y , t ) = \mathrm { d i s t } _ { t } ( x _ { 0 } , y ) - A ( 2 t - 1 ) , \hat { L } ( y , \tau ) = \bar { L } ( y , \tau ) + 7 .$ and$\bar { L }$was defined in$\left[ \mathrm { I } , ( 7 . 1 5 ) \right]$. Now we redefine$\hat { L } ,$, taking$\bar { L } ( y , \tau ) = \bar { L } ( y , \tau ) +$ $2 \sqrt { \tau }$. Clearly,$\hat { L } > 0$because$R \geq - 3$and$2 \sqrt { \tau } > 4 \tau ^ { 2 }$for$0 < \tau \le 1 / 2$. Then the computations and estimates of I.8.2 yield

$$
\Box h \geq - C (A) h - (6 + \frac {1}{\sqrt {\tau}}) \phi
$$

Now denoting by$h _ { 0 } ( \tau )$the minimum of$h ( y , 1 - t )$, we can estimate

$$
\frac {d}{d \tau} (\log (\frac {h _ {0} (\tau)}{\sqrt {\tau}})) \leq C (A) + \frac {6 \sqrt {\tau} + 1}{2 \tau - 4 \tau^ {2} \sqrt {\tau}} - \frac {1}{2 \tau} \leq C (A) + \frac {5 0}{\sqrt {\tau}},\tag{6.2}
$$

whence

$$
h _ {0} (\tau) \leq \sqrt {\tau} \exp (C (A) \tau + 1 0 0 \sqrt {\tau}),\tag{6.3}
$$

because the left hand side of (6.2) tends to zero as$\tau  0 +$

Now we can return to our proof, replace the right hand side of (6.1) by the $\mathrm { r i g h t }$hand side of (6.3) times$r _ { 0 } ^ { 2 }$, with$\tau = r _ { 0 } ^ { - 2 } ( t _ { 0 } - t _ { \gamma } )$, and apply Lemma$5 . 3$ C

(b) Assume the contrary, take a sequence$K _ { 1 } ^ { \alpha }$and consider the solutions violating the statement. Clearly,$K _ { 1 } ^ { \alpha } ( r _ { 0 } ^ { \alpha } ) ^ { - 2 } < ( r ( t _ { 0 } ^ { \alpha } ) ) ^ { - 2 }$, whence$t _ { 0 } ^ { \alpha } \to \infty ;$ When$K _ { 1 }$is large enough, we can, arguing as in the proof of Claim 1 in $[ \mathrm { I . 1 0 . 1 } ]$], find a point$( \bar { x } , \bar { t } ) , x \in B ( x _ { 0 } , \bar { t } , 2 A r _ { 0 } ) , \bar { t } \in [ t _ { 0 } - r _ { 0 } ^ { 2 } / 2 , t _ { 0 } ]$, such that$\bar { Q } =$ $\mathbf { \bar { \xi } } R ( \bar { x } , \bar { t } ) > K _ { 1 } r _ { 0 } ^ { - 2 } , \mathbf { \tau } ( \bar { x } , \bar { t } )$does not satisfy the canonical neighborhood assumption, but each point$( x , t ) \in \bar { P }$with$R ( x , t ) \geq 4 \bar { Q }$does, where$\bar { P }$is the set of all$( x , t )$ satisfying$\begin{array} { r } { \bar { t } - \frac { 1 } { 4 } K _ { 1 } \bar { Q } ^ { - 1 } \leq t \leq \bar { t } , } \end{array}$dis$\natural _ { t } ( x _ { 0 } , x ) \leq \mathrm { d i s t } _ { \bar { t } } ( x _ { 0 } , \bar { x } ) + K _ { 1 } ^ { \frac { 1 } { 2 } } \bar { Q } ^ { - \frac { 1 } { 2 } }$. (Note that$\bar { P }$is not a parabolic neighborhood.) Clearly we can use$\mathrm { ( a ) }$with slightly diferent parameters to ensure κ-noncollapsing in$\bar { P }$

Now we apply the argument from 5.4. First, by Claim 2 in 4.2, for any $\bar { A } < \infty$we have an estimate$R \leq Q ( { \bar { A } } ) { \bar { Q } }$in$B ( \bar { x } , \bar { t } , \bar { A } \bar { Q } ^ { - \frac { 1 } { 2 } } )$when$K _ { 1 }$is large enough; therefore we can take a limit as$\alpha \to \infty$of scalings with factor$\bar { Q }$about $( { \bar { x } } , { \bar { t } } )$, shifting the time$\bar { t }$to zero; the limit at time zero would be a smooth complete nonnegatively curved manifold. Next we observe that this limit has curvature uniformly bounded, say, by$Q _ { 0 }$, and therefore, for each fixed$\bar { A }$and for suficiently large$K _ { 1 }$<sub>1</sub>, the parabolic neighborhood$P ( \bar { x } , \bar { t } , \bar { A } \bar { Q } ^ { - \frac { 1 } { 2 } } , - \epsilon \eta ^ { - 1 } Q _ { 0 } ^ { - 1 } \bar { Q } ^ { - 1 } )$ is contained in${ \bar { P } } .$. (Here we use the estimate of distance change, given by Lemma $\mathrm { I . 8 . 3 ( a ) . }$) Thus we can take a limit on the interval$[ - \epsilon \eta ^ { - 1 } Q _ { 0 } ^ { - 1 } , 0 ]$. (The possibility of surgeries is ruled out as in$5 . 4 )$Then we repeat the procedure indefinitely, getting an ancient κ-solution in the limit, which means a contradiction.

(c) If$x \ \in \ B ( x _ { 0 } , t _ { 0 } , A r _ { 0 } )$has very large curvature, then on the shortest geodesic γ at time$t _ { 0 }$, that connects$x _ { 0 }$and$x ,$we can find a point$y ,$such that$R ( y , t _ { 0 } ) = K _ { 1 } ( A ) r _ { 0 } ^ { - 2 }$and the curvature is larger at all points of the segment of$\gamma$between x and$y .$. Then our statement follows from Claim 2 in 4.2, applied to this segment.

From now on we redefine the function$\bar { \delta } ( t )$to be min$( \bar { \delta } ( t ) , \bar { \delta } _ { 2 t } ( 2 t ) )$, so that the proposition above always holds for$A = t _ { 0 }$

6.4 Proposition. There exist$\tau > 0 , \bar { r } > 0 , K < \infty$with the following property. Suppose we have a solution to the Ricci flow with$\delta ( t ) - c u t o f f$on the time interval$[ 0 , t _ { 0 } ]$, with normalized initial data. Let$r _ { 0 } , t _ { 0 }$satisfy$2 C _ { 1 } h \leq r _ { 0 } \leq$ $\bar { r } \sqrt { t _ { 0 } } .$, where h is the maximal cutof radius for surgeries in$[ t _ { 0 } / 2 , t _ { 0 } ]$, and assume that the ball$B ( x _ { 0 } , t _ { 0 } , r _ { 0 } )$has sectional curvatures at least$- r _ { 0 } ^ { - 2 } \ a t$each point, and the volume of any subball$B ( x , t _ { 0 } , r ) \subset B ( x _ { 0 } , t _ { 0 } , r _ { 0 } )$with any radius$r > 0$is at least$( 1 - \epsilon )$times the volume of the euclidean ball of the same radius. Then the solution is defined in$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } / 4 , - \tau r _ { 0 } ^ { 2 } )$and satisfies$R < K r _ { 0 } ^ { - 2 }$there.

Proof. Let us first consider the case$r _ { 0 } \leq r ( t _ { 0 } )$. Then clearly$R ( x _ { 0 } , t _ { 0 } ) \leq$ $C _ { 1 } ^ { 2 } r _ { 0 } ^ { - 2 } ,$since an ǫ-neck of radius r can not contain an almost euclidean ball of radius$\geq r$. Thus we can take$K = 2 C _ { 1 } ^ { 2 } , \tau = \epsilon \eta ^ { - 1 } C _ { 1 } ^ { - 2 }$in this case, and since $r _ { 0 } \ge 2 C _ { 1 } h$, the surgeries do not interfere in$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } / 4 , - \tau r _ { 0 } ^ { 2 } )$

In order to handle the other case$r ( t _ { 0 } ) < r _ { 0 } \leq \bar { r } \sqrt { t _ { 0 } }$we need a couple of lemmas.

6.5 Lemma. There exist$\tau _ { 0 } > 0$and$K _ { 0 } < \infty$, such that$i f$we have a smooth solution to the Ricci flow in$P ( x _ { 0 } , 0 , 1 , - \tau ) , \tau \leq \tau _ { 0 }$, having sectional curvatures at least$- 1$, and the volume of the ball$B ( x _ { 0 } , 0 , 1 )$is at least$( 1 - \epsilon )$times the volume of the euclidean unit ball, then

(a)$R \leq K _ { 0 } \tau ^ { - 1 }$in$P ( x _ { 0 } , 0 , 1 / 4 , - \tau / 2 )$, and

(b) the ball$B ( x _ { 0 } , 1 / 4 , - \tau )$has volume at least$\textstyle { \frac { 1 } { 1 0 } }$times the volume of the euclidean ball of the same radius.

The proof can be extracted from the proof of Lemma I.11.6.

6.6 Lemma. For any$w > 0$there exists$\theta _ { 0 } = \theta _ { 0 } ( w ) > 0$, such that if $B ( x , 1 )$is a metric ball of volume at least$w ,$, compactly contained in a manifold without boundary with sectional curvatures at least 1, then there exists a ball $B ( y , \theta _ { 0 } ) \subset B ( x , 1 )$, such that every subball$B ( z , r ) \subset B ( y , \theta _ { 0 } )$of any radius r has volume at least$( 1 - \epsilon )$times the volume of the euclidean ball of the same radius.

This is an elementary fact from the theory of Aleksandrov spaces.

6.7 Now we continue the proof of the proposition. We claim that one can take$\tau =$min$( \tau _ { 0 } / 2 , \epsilon \eta ^ { - 1 } C _ { 1 } ^ { - 2 } ) , K = \operatorname* { m a x } ( 2 K _ { 0 } \tau ^ { - 1 } , 2 C _ { 1 } ^ { 2 } )$. Indeed, assume the contrary, and take a sequence of$\bar { r } ^ { \alpha } \to 0$and solutions, violating our assertion for the chosen$\tau , K .$. Let$t _ { 0 } ^ { \alpha }$be the first time when it is violated, and let$B ( x _ { 0 } ^ { \alpha } , t _ { 0 } ^ { \alpha } , r _ { 0 } ^ { \alpha } )$ be the counterexample with the smallest radius. Clearly$r _ { 0 } ^ { \alpha } ~ > ~ r ( t _ { 0 } ^ { \alpha } )$and $( r _ { 0 } ^ { \alpha } ) ^ { 2 } ( t _ { 0 } ^ { \alpha } ) ^ { - 1 } \to 0$as$\alpha \to \infty$

Consider any ball$B ( x _ { 1 } , t _ { 0 } , r ) \subset B ( x _ { 0 } , t _ { 0 } , r _ { 0 } ) , r < r _ { 0 }$. Clearly we can apply our proposition to this ball and get the solution in$P ( x _ { 1 } , t _ { 0 } , r / 4 , - \tau r ^ { 2 } )$with the curvature bound$R < K r ^ { - 2 }$. Now if$r _ { 0 } ^ { 2 } t _ { 0 } ^ { - 1 }$is small enough, then we can apply proposition$6 . 3 ( \mathrm { c ) }$to get an estimate$\bar { R ( x , t ) } \le K ^ { \prime } ( A ) r ^ { - 2 }$for$( x , t )$satisfying $t \ \in \ [ t _ { 0 } - \tau r ^ { 2 } / 2 , t _ { 0 } ] , \mathrm { d i s t } _ { t } ( x , x _ { 1 } ) \ < \ A r$, for some function$K ^ { \prime } ( A )$that can be made explicit. Let us choose$A = 1 0 0 r _ { 0 } r ^ { - 1 }$; then we get the solution with a curvature estimate in$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } , - \triangle t )$, where$\triangle t = \top ( A ) ^ { - 1 } r ^ { 2 }$. Now the pinching estimate implies$R m \ge - r _ { 0 } ^ { - 2 }$on this set, if$r _ { 0 } ^ { 2 } t _ { 0 } ^ { - 1 }$is small enough while$r r _ { 0 } ^ { - 1 }$is bounded away from zero. Thus we can use lemma$6 . 5 ( \mathrm { b } )$to estimate the volume of the ball$B ( x _ { 0 } , t _ { 0 } - \triangle t , r _ { 0 } / 4 )$by at least$\textstyle { \frac { 1 } { 1 0 } }$of the volume of the euclidean ball of the same radius, and then by lemma$6 . 6$we can find a subball$B ( x _ { 2 } , t _ { 0 } - \triangle t , \theta _ { 0 } ( \frac { 1 } { 1 0 } ) r _ { 0 } / 4 )$, satisfying the assumptions of our proposition. Therefore, if we put$r = \tilde { \theta _ { 0 } } ( \textstyle \frac { 1 } { 1 0 } ) r _ { 0 } / 4$, then we can repeat our procedure as many times as we like, until we reach the time$t _ { 0 } - \tau _ { 0 } r _ { 0 } ^ { 2 }$, when the lemma 6.5(b) stops working. But once we reach this time, we can apply lemma 6.5(a) and get the required curvature estimate, which is a contradiction.

6.8 Corollary. For any$w > 0$one can find$\tau = \tau ( w ) > 0 , K = K ( w ) <$ $\infty , \bar { r } = \bar { r } ( w ) > 0 , \theta = \theta ( w ) > 0$with the following property. Suppose we have a solution to the Ricci flow with$\delta ( t ) - c u t o f f$on the time interval$[ 0 , t _ { 0 } ]$, with normalized initial data. Let$t _ { 0 } , r _ { 0 }$satisfy$\theta ^ { - 1 } ( w ) h \le r _ { 0 } \le \bar { r } \sqrt { t _ { 0 } } ,$, and assume that the ball$B ( x _ { 0 } , t _ { 0 } , r _ { 0 } )$has sectional curvatures at least$- r _ { 0 } ^ { 2 }$at each point, and volume at least$w r _ { 0 } ^ { 3 }$. Then the solution is defined in$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } / 4 , - \tau r _ { 0 } ^ { 2 } )$ and satisfies$R < K r _ { 0 } ^ { - 2 }$there.

Indeed, we can apply proposition 6.4 to a smaller ball, provided by lemma 6.6, and then use proposition 6.3(c).

## 7 Long time behavior II

In this section we adapt the arguments of Hamilton [H 4] to a more general setting. Hamilton considered smooth Ricci flow with bounded normalized curvature; we drop both these assumptions. In the end of [I,13.2] I claimed that the volumes of the maximal horns can be efectively bounded below, which would imply that the solution must be smooth from some time on; however, the argu ment I had in mind seems to be faulty. On the other hand, as we’ll see below, the presence of surgeries does not lead to any substantial problems.

From now on we assume that our initial manifold does not admit a metric with nonnegative scalar curvature, and that once we get a component with nonnegative scalar curvature, it is immediately removed.

7.1 (cf. [H 4, 2,7]) Recall that for a solution to the smooth Ricci flow the scalar curvature satisfies the evolution equation

$$
\frac {d}{d t} R = \triangle R + 2 | R i c | ^ {2} = \triangle R + 2 | R i c ^ {\circ} | ^ {2} + \frac {2}{3} R ^ {2},\tag{7.1}
$$

where$R i c ^ { \circ }$is the trace-free part of Ric. Then$R _ { \mathrm { m i n } } ( t )$satisfies$\begin{array} { r } { \frac { d } { d t } R _ { \mathrm { m i n } } \geq \frac { 2 } { 3 } R _ { \mathrm { m i n } } ^ { 2 } , } \end{array}$ whence0

$$
R _ {\mathrm{min}} (t) \geq - \frac {3}{2} \frac {1}{t + 1 / 4}\tag{7.2}
$$

for a solution with normalized initial data. The evolution equation for the volume is$\begin{array} { r } { { \frac { d } { d t } } V = - \int R d V , } \end{array}$, in particular

$$
\frac {d}{d t} V \leq - R _ {\mathrm{min}} V,\tag{7.3}
$$

whence by (7.2) the function$V ( t ) ( t + 1 / 4 ) ^ { - \frac { 3 } { 2 } }$is non-increasing in t. Let$\bar { V }$denote its limit as$t \to \infty$

Now the scale invariant quantity$\hat { R } = R _ { \mathrm { m i n } } V ^ { \frac { 2 } { 3 } }$satisfies

$$
\frac {d}{d t} \hat {R} (t) \geq \frac {2}{3} \hat {R} V ^ {- 1} \int (R _ {\mathrm{min}} - R) d V,\tag{7.4}
$$

which is nonnegative whenever$R _ { \mathrm { m i n } } ~ \leq ~ 0$, which we have assumed from the beginning of the section. Let R<sup>¯</sup> denote the limit of$\hat { R } ( t )$as$t \to \infty$

Assume for a moment that$\bar { V } > 0$. Then it follows from (7.2) and (7.3) that $R _ { \mathrm { m i n } } ( t )$is asymptotic to$- \frac { 3 } { 2 t }$; in other words,$\bar { R } \bar { V } ^ { - \frac { 2 } { 3 } } = - \frac { 3 } { 2 }$. Now the inequality (7.4) implies that whenever we have a sequence of parabolic neighborhoods

$P ( x ^ { \alpha } , t ^ { \alpha } , r { \sqrt { t ^ { \alpha } } } , - r ^ { 2 } t ^ { \alpha } )$, for$t ^ { \alpha } \to \infty$and some fixed small$r > 0$, such that the scalings of our solution with factor$t ^ { \alpha }$smoothly converge to some limit solution, defined in an abstract parabolic neighborhood$P ( { \bar { x } } , 1 , r , - r ^ { 2 } )$, then the scalar curvature of this limit solution is independent of the space variables and equals $- \frac { 3 } { 2 t }$at time$t \in [ 1 - r ^ { 2 } , 1 ]$; moreover, the strong maximum principle for (7.1) implies that the sectional curvature of the limit at time t is constant and equals $- { \frac { 1 } { 4 t } }$. This conclusion is also valid without the a priori assumption that$\bar { V } > 0$ since otherwise it is vacuous.

Clearly the inequalities and conclusions above hold for the solutions to the Ricci flow with$\delta ( t )$-cutof, defined in the previous sections. From now on we assume that we are given such a solution, so the estimates below may depend on it.

7.2 Lemma. (a) Given$w > 0 , r > 0 , \xi > 0$one can find$T = T ( w , r , \xi ) <$ $\infty .$, such that if the ball$B ( x _ { 0 } , t _ { 0 } , r \sqrt { t _ { 0 } } )$at some time$t _ { 0 } ~ \ge ~ T$has volume at least$w r ^ { 3 }$and sectional curvature at least$- r ^ { - 2 } t _ { 0 } ^ { - 1 }$, then curvature at$x _ { 0 }$at time $t = t _ { 0 }$satisfies

$$
\left| 2 t R _ {i j} + g _ {i j} \right| <   \xi .\tag{7.5}
$$

(b) Given in addition$A < \infty$and allowing$T$to depend on$A .$we can ensure (7.5) for all points in$B ( x _ { 0 } , t _ { 0 } , A r \sqrt { t _ { 0 } } )$

(c) The same is true for$P ( x _ { 0 } , t _ { 0 } , A r \sqrt { t _ { 0 } } , A r ^ { 2 } t _ { 0 } )$

Proof. (a) If$T$is large enough then we can apply corollary 6.8 to the ball $B ( x _ { 0 } , t _ { 0 } , r _ { 0 } )$for$r _ { 0 } = \operatorname* { m i n } ( r , \bar { r } ( w ) ) \sqrt { t _ { 0 } } ;$; then use the conclusion of 7.1.

(b) The curvature control in$P ( x _ { 0 } , t _ { 0 } , r _ { 0 } / 4 , - \tau r _ { 0 } ^ { 2 } )$, provided by corollary 6.8, allows us to apply proposition$6 . 3 ( \mathrm { a } ) , ( \mathrm { b } )$to a controllably smaller neighborhood $P ( x _ { 0 } , t _ { 0 } , r _ { 0 } ^ { \prime } , - ( r _ { 0 } ^ { \prime } ) ^ { 2 } )$. Thus by 6.3(b) we know that each point in$B ( x _ { 0 } , t _ { 0 } , A r \sqrt { t _ { 0 } } )$ with scalar curvature at least$\dot { Q } = K _ { 1 } ^ { \prime } ( A ) r _ { 0 } ^ { - 2 }$has a canonical neighborhood. This implies that for T large enough such points do not exist, since if there was a point with R larger than$Q { \mathrm { . } }$, there would be a point having a canonical neighborhood with$R = Q$in the same ball, and that contradicts the already proved assertion (a). Therefore we have curvature control in the ball in question, and applying$6 . 3 ( \mathrm { a } )$we also get volume control there, so our assertion has been reduced to (a).

(c) If ξ is small enough, then the solution in the ball$B ( x _ { 0 } , t _ { 0 } , A r \sqrt { t _ { 0 } } )$would stay almost homothetic to itself on the time interval$[ t _ { 0 } , t _ { 0 } + A r ^ { 2 } t _ { 0 } ]$until (7.5) is violated at some (first) time$t ^ { \prime }$in this interval. However, if T is large enough, then this violation could not happen, because we can apply the already proved assertion (b) at time$t ^ { \prime }$for somewhat larger A.

7.3 Let$\rho ( x , t )$denote the radius$\rho$of the ball$B ( x , t , \rho )$where inf$R m =$ $- \rho ^ { - 2 }$. It follows from corollary 6.8, proposition$6 . 3 ( \mathrm { c ) }$, and the pinching estimate (5.1) that for any$w > 0$we can find$\bar { \rho } = \bar { \rho } ( w ) > 0$, such that if$\rho ( x , t ) < \bar { \rho } \sqrt { t }$ then

$$
\text { Vol } B (x, t, \rho (x, t)) <   w \rho^ {3} (x, t),\tag{7.6}
$$

provided that t is large enough (depending on w).

Let$M ^ { - } ( w , t )$denote the thin part of M, that is the set of$x \in M$where (7.6) holds at time t, and let$M ^ { + } ( w , t )$be its complement. Then for t large enough (depending on w) every point of$M ^ { + }$satisfies the assumptions of lemma 7.2.

Assume first that for some$w > 0$the set$M ^ { + } ( w , t )$is not empty for a sequence of$t \to \infty$. Then the arguments of Hamilton [H 4, 8-12] work in our situation. In particular, if we take a sequence of points$x ^ { \alpha } \in M ^ { + } ( w , t ^ { \alpha } ) , \ t ^ { \alpha } \to$ $\infty$, then the scalings of$g _ { i j } ^ { \alpha }$about$x ^ { \alpha }$with factors$( t ^ { \alpha } ) ^ { - 1 }$converge, along a subsequence of$\alpha  \infty$, to a complete hyperbolic manifold of finite volume. The limits may be diferent for diferent choices of$( x ^ { \alpha } , t ^ { \alpha } )$). If none of the limits is closed, and$H _ { 1 }$is such a limit with the least number of cusps, then, by an argument in [H 4, 8-10], based on hyperbolic rigidity, for all suficiently small $w ^ { \prime } , 0 < w ^ { \prime } < \bar { w } ( H _ { 1 } )$, there exists a standard truncation$H _ { 1 } ( w ^ { \prime } )$of$H _ { 1 }$, such that, for t large enough,$M ^ { + } ( w ^ { \prime } / 2 , t )$contains an almost isometric copy of$H _ { 1 } ( w ^ { \prime } )$ which in turn contains a component of$\boldsymbol { M } ^ { + } ( \boldsymbol { w } ^ { \prime } , t )$; moreover, this embedded copy of$H _ { 1 } ( w ^ { \prime } )$moves by isotopy as t increases to infinity. If for some$w > 0$the complement$M ^ { + } ( w , t ) \setminus H _ { 1 } ( w )$is not empty for a sequence of$t \to \infty ,$, then we can repeat the argument and get another complete hyperbolic manifold$H _ { 2 }$, etc., until we find a finite collection of$H _ { j } , 1 \leq j \leq i ,$, such that for each suficiently small w$> 0$the embeddings of$H _ { j } ( w )$cover$M ^ { + } ( w , t )$for all suficiently large t.

Furthermore, the boundary tori of$H _ { j } ( w )$are incompressible in M. This is proved [H 4, 11,12] by a minimal surface argument, using a result of Meeks and Yau. This argument does not use the uniform bound on the normalized curvature, and goes through even in the presence of surgeries, because the area of the least area disk in question can only decrease when we make a surgery.

7.4 Let us redefine the thin part in case the thick one isn’t empty,$M ^ { - } ( w , t ) =$ $M \backslash ( H _ { 1 } ( w ) \cup . . . \cup H _ { i } ( w ) )$. Then, for suficiently small$w > 0$and suficiently large t,$M ^ { - } ( w , t )$is difeomorphic to a graph manifold, as implied by the following general result on collapsing with local lower curvature bound, applied to the metrics$t ^ { - 1 } g _ { i j } ( t )$

Theorem. Suppose$( M ^ { \alpha } , g _ { i j } ^ { \alpha } )$is a sequence of compact oriented riemannian 3-manifolds, closed or with convex boundary, and$w ^ { \alpha } \to 0$. Assume that

(1) for each point$x \in M ^ { \alpha }$there exists a radius$\rho = \rho ^ { \alpha } ( x ) , 0 < \rho < 1$, not exceeding the diameter of the manifold, such that the ball$B ( x , \rho )$in the metric $g _ { i j } ^ { \alpha }$has volume at most$w ^ { \alpha } \rho ^ { 3 }$and sectional curvatures at$l e a s t - \rho ^ { - 2 }$;

(2) each component of the boundary of$M ^ { \alpha }$has diameter at most$w ^ { \alpha }$, and has a (topologically trivial) collar of length one, where the sectional curvatures are between$- 1 / 4 - \epsilon$and$- 1 / 4 + \epsilon ;$

(3) For every$w ^ { \prime } > 0$there exist$\bar { r } \ : = \ : \bar { r } ( w ^ { \prime } ) \ : > \ : 0$and$K _ { m } = K _ { m } ( w ^ { \prime } ) <$ $\infty , m = 0 , 1 , 2 . . . ,$such that if α is large enough,$0 < r \leq \bar { r }$, and the ball$B ( x , r )$ in$g _ { i j } ^ { \alpha }$has volume at least$w ^ { \prime } r ^ { 3 }$and sectional curvatures at least$- r ^ { 2 }$, then the curvature and its m-th order covariant derivatives at x,$m = 1 , 2 . . . ,$, are bounded by$K _ { 0 } r ^ { - 2 }$and$K _ { m } r ^ { - m - 2 }$respectively.

Then M<sup>α</sup> for suficiently large α are difeomorphic to graph manifolds.

Indeed, there is only one exceptional case, not covered by the theorem above, namely, when$M = M ^ { - } ( w , t )$, and$\rho ( x , t )$, for some$x \in M ,$, is much larger than the diameter$d ( t )$of the manifold, whereas the ratio$V ( t ) / d ^ { 3 } ( t )$is bounded away from zero. In this case, since by the observation after formula (7.3) the volume$V ( t )$can not grow faster than const$\cdot \ t ^ { \frac { 3 } { 2 } }$, the diameter does not grow faster than const$\cdot \ { \sqrt { t } } .$, hence if we scale our metrics$g _ { i j } ( t )$to keep the diameter equal to one, the scaled metrics would satisfy the assumption (3) of the theorem above and have the minimum of sectional curvatures tending to zero. Thus we can take a limit and get a smooth solution to the Ricci flow with nonnegative sectional curvature, but not strictly positive scalar curvature. Therefore, in this exceptional case M is difeomorphic to a flat manifold.

The proof of the theorem above will be given in a separate paper; it has nothing to do with the Ricci flow; its main tool is the critical point theory for distance functions and maps, see [P, 2] and references therein. The assumption (3) is in fact redundant; however, it allows to simplify the proof quite a bit, by avoiding 3-dimensional Aleksandrov spaces, and in particular, the non-elementary Stability Theorem.

Summarizing, we have shown that for large t every component of the solution is either difeomorphic to a graph manifold, or to a closed hyperbolic manifold, or can be split by a finite collection of disjoint incompressible tori into parts, each being difeomorphic to either a graph manifold or to a complete noncompact hyperbolic manifold of finite volume. The topology of graph manifolds is well understood$[ \mathrm { W } ]$; in particular, every graph manifold can be decomposed in a connected sum of irreducible graph manifolds, and each irreducible one can in turn be split by a finite collection of disjoint incompressible tori into Seifert fibered manifolds.

## 8 On the first eigenvalue of the operator$- 4 \triangle + R$

8.1 Recall from$[ \mathrm { I } , \ S 1 , 2 ]$that Ricci flow is the gradient flow for the first eigenvalue λ of the operator$- 4 \triangle + R ;$moreover,$\begin{array} { r } { \frac { d } { d t } \lambda ( t ) \geq \frac { 2 } { 3 } \lambda ^ { 2 } ( t ) } \end{array}$and$\lambda ( t ) V ^ { \frac { 2 } { 3 } } ( t )$is non-decreasing whenever it is nonpositive. We would like to extend these inequalities to the case of Ricci flow with$\delta ( t )$-cutof. Recall that we immediately remove components with nonnegative scalar curvature.

Lemma. Given any positive continuous function$\xi ( t )$one can chose$\delta ( t )$ in such a way that for any solution to the Ricci flow with$\delta ( t ) - c u t o f f ,$with normalized initial data, and any surgery time$T _ { 0 }$, after which there is at least one component, where the scalar curvature is not strictly positive, we have an estimate$\lambda ^ { + } ( T _ { 0 } ) - \lambda ^ { - } ( T _ { 0 } ) \geq \xi ( T _ { 0 } ) ( V ^ { + } ( T _ { 0 } ) - V ^ { - } ( T _ { 0 } ) )$), where$V ^ { - } , V ^ { + }$and$\lambda ^ { - } , \lambda ^ { + }$ are the volumes and the first eigenvalues$o f { - } 4 \triangle { + } R$before and after the surgery respectively.

Proof. Consider the minimizer a for the functional

$$
\int (4 | \nabla a | ^ {2} + R a ^ {2})\tag{8.1}
$$

under normalization$\textstyle \int a ^ { 2 } = 1$, for the metric after the surgery on a component where scalar curvature is not strictly positive. Clearly is satisfies the equation

$$
4 \triangle a = R a - \lambda^ {-} a\tag{8.2}
$$

Observe that since the metric contains an ǫ-neck of radius about$r ( T _ { 0 } )$, we can estimate$\lambda ^ { - } ( T _ { 0 } )$from above by about$r ( T _ { 0 } ) ^ { - 2 }$

Let$M _ { c a p }$denote the cap, added by the surgery. It is attached to a long tube, consisting of ǫ-necks of various radii. Let us restrict our attention to a maximal subtube, on which the scalar curvature at each point is at least $2 \lambda ^ { - } ( T _ { 0 } )$. Choose any ǫ-neck in this subtube, say, with radius$r _ { 0 } .$, and consider the distance function with range$[ 0 , 2 \epsilon ^ { - 1 } r _ { 0 } ]$], whose level sets$M _ { z }$are almost round two-spheres; let$M _ { z } ^ { + } \supset M _ { c a p }$be the part of$M$, chopped of by$M _ { z }$. Then

$$
\int_ {M _ {z}} - 4 a a _ {z} = \int_ {M _ {z} ^ {+}} (4 | \nabla a | ^ {2} + R a ^ {2} - \lambda^ {-} a ^ {2}) > r _ {0} ^ {- 2} / 2 \int_ {M _ {z} ^ {+}} a ^ {2}
$$

On the other hand,

$$
| \int_ {M _ {z}} 2 a a _ {z} - (\int_ {M _ {z}} a ^ {2}) _ {z} | \leq \mathrm{const} \cdot \int_ {M _ {z}} \epsilon r _ {0} ^ {- 1} a ^ {2}
$$

These two inequalities easily imply that

$$
\int_ {M _ {0} ^ {+}} a ^ {2} \geq \exp (\epsilon^ {- 1} / 1 0) \int_ {M _ {\epsilon^ {- 1} r _ {0}} ^ {+}} a ^ {2}
$$

Now the chosen subtube contains at least about$- \epsilon ^ { - 1 } \mathrm { l o g } ( \lambda ^ { - } ( T _ { 0 } ) h ^ { 2 } ( T _ { 0 } ) )$disjoint ǫ-necks, where$h$denotes the cutof radius, as before. Since h tends to zero with$\delta ,$whereas$r ( T _ { 0 } )$, that occurs in the bound for$\lambda ^ { - } ,$, is independent of$\delta ,$ we can ensure that the number of necks is greater then log$h ,$and therefore, $\textstyle \int _ { M _ { c a n } } a ^ { 2 } < h ^ { 6 }$, say. Then standard estimates for the equation (8.2) show that $| \boldsymbol { \nabla } a | ^ { 2 }$and$R a ^ { 2 }$are bounded by const$h$on$M _ { c a p } ,$which makes it possible to extend a to the metric before surgery in such a way that the functional (8.1) is preserved up to const$h ^ { 4 }$. However, the loss of volume in the surgery is at least $h ^ { 3 }$, so it sufices to take$\delta$so small that h is much smaller than ξ.

8.2 The arguments above lead to the following result

(a)$I f \left( M , g _ { i j } \right)$has$\lambda > 0$, then, for an appropriate choice of the cutof parameter, the solution becomes extinct in finite time. Thus, if M admits a metric with$\lambda > 0$then it is difeomorphic to a connected sum of a finite collection of $\mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 1 }$and metric quotients of the round${ \mathbb S } ^ { 3 }$. Conversely, every such connected sum admits a metric with$R > 0$, hence with$\lambda > 0$

(b) Suppose M does not admit any metric with$\lambda > 0$, and let$\bar { \lambda }$denote the supremum of$\lambda V ^ { \frac { 2 } { 3 } }$over all metrics on this manifold. Then$\bar { \lambda } = 0$implies that M is a graph manifold. Conversely, a graph manifold can not have$\bar { \lambda } < 0$

(c) Suppose$\bar { \lambda } < 0$and let$\bar { V } = \bar { ( - \frac { 2 } { 3 } \bar { \lambda } ) ^ { \frac { 3 } { 2 } } }$. Then V<sup>¯</sup> is the minimum of V, such that M can be decomposed in connected sum of a finite collection of$\mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 1 }$，metric quotients of the round$\mathbb { S } ^ { 3 }$, and some other components, the union of which will be denoted by$M ^ { \prime }$, and there exists a (possibly disconnected) complete hyperbolic manifold, with sectional curvature$- 1 / 4$and volume$V ,$which can be embedded in$M ^ { \prime }$in such a way that the complement$( i f$not empty) is a graph manifold. Moreover, if such a hyperbolic manifold has volume$\bar { V }$, then its cusps (if any) are incompressible in$M ^ { \prime }$

For the proof one needs in addition easily verifiable statements that one can put metrics on connected sums preserving the lower bound for scalar curvature [G-L], that one can put metrics on graph manifolds with scalar curvature bounded below and volume tending to zero [C-G], and that one can close a compressible cusp, preserving the lower bound for scalar curvature and reducing the volume, cf. [A,5.2]. Notice that using these results we can avoid the hyperbolic rigidity and minimal surface arguments, quoted in 7.3, which, however, have the advantage of not requiring any a priori topological information about the complement of the hyperbolic piece.

The results above are exact analogs of the conjectures for the Sigma constant, formulated by Anderson [A], at least in the nonpositive case.

## References

[I] G.Perelman The entropy formula for the Ricci flow and its geometric applications. arXiv:math.DG/0211159 v1

[A] M.T.Anderson Scalar curvature and geometrization conjecture for threemanifolds. Comparison Geometry (Berkeley, 1993-94), MSRI Publ. 30 (1997), 49-82.

[C-G] J.Cheeger, M.Gromov Collapsing Riemannian manifolds while keeping their curvature bounded I. Jour. Dif. Geom. 23 (1986), 309-346.

[G-L] M.Gromov, H.B.Lawson Positive scalar curvature and the Dirac operator on complete Riemannian manifolds. Publ. Math. IHES 58 (1983), 83-196.

[H 1] R.S.Hamilton Three-manifolds with positive Ricci curvature. Jour. Dif. Geom. 17 (1982), 255-306.

[H 2] R.S.Hamilton Formation of singularities in the Ricci flow. Surveys in Dif. Geom. 2 (1995), 7-136.

[H 3] R.S.Hamilton The Harnack estimate for the Ricci flow. Jour. Dif. Geom. 37 (1993), 225-243.

[H 4] R.S.Hamilton Non-singular solutions of the Ricci flow on three-manifolds. Commun. Anal. Geom. 7 (1999), 695-729.

[H 5] R.S.Hamilton Four-manifolds with positive isotropic curvature. Commun. Anal. Geom. 5 (1997), 1-92.

G.Perelman Spaces with curvature bounded below. Proceedings of ICM-1994, 517-525.

F.Waldhausen Eine Klasse von 3-dimensionalen Mannigfaltigkeiten I,II. Invent. Math. 3 (1967), 308-333 and 4 (1967), 87-117.