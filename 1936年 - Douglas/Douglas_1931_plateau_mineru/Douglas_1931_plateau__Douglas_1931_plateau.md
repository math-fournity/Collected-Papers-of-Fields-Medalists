# SOLUTION OF THE PROBLEM OF PLATEAU\*

BY
JESSE DOUGLAS

1. Introduction. The problem of Plateau is to prove the existence of a minimal surface bounded by a given contour. This memoir presents the first solution of this problem for the most general kind of contour: an arbitrary Jordan curve in n-dimensional euclidean space. Topological complications in the contour, as well as the dimensionality n of the containing space, are without consequence for either method or result. Naturally, an arrangement of knots in the contour will produce corresponding complications in the minimal surface, such as self-intersections and branch points.

The method used is entirely novel, representing a complete departure from the classical modes of attack hitherto employed. In this introduction we shall outline three of the classic methods (wherein n is always 3) and, fourth, the method of the present paper, which we believe to furnish the key to the problem. That this is the fact will become even clearer when, in future papers, we apply this method to the case of several contours and of various topological structures of the minimal surface, $^{\dagger}$ for instance, a Möbius leaf with a prescribed boundary.

It is to be signalized that the solution here given is strictly elementary, employing only the most simple and usual parts of analysis, and that the presentation is self-sufficient, requiring no special preliminary knowledge.

(1) First to be considered, in this introductory survey, is the method based on the ideas of Riemann, Weierstrass and Schwarz.‡ Here the given

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* This work, in successive stages of its development, was presented to the Society at various meetings from December, 1926, to December, 1929. Abstracts appear in the Bulletin of the American Mathematical Society as follows: vol. 33 (1927), pp. 143, 259; vol. 34 (1928), p. 405; vol. 35 (1929), p. 292; vol. 36 (1930), pp. 49–50, 189–190. Received by the editors, Parts I–IV in August and Part V in December, 1930.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Various phases of the work were also presented in the seminars of Hadamard at Paris (January 18 and December 17, 1929), Courant and Herglotz at Göttingen (June 4, 11, 18; 1929), and Blaschke at Hamburg (July 26, 1929). The second presentation in Hadamard's seminar was in the present form.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† See the abstract A general formulation of the problem of Plateau, Bulletin of the American Mathematical Society, vol. 36 (1930), p. 50, which gives methods adequate to solve this most general form of the problem. The cases of two contours, a Möbius leaf, and three contours have already been worked out by the author and the results presented to this Society; abstracts are in the Bulletin of the American Mathematical Society, vol. 36 (1930), p. 797, and vol. 37 (1931).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ Riemann, Werke, Leipzig, 1892, pp. 301–337, 445–454; Weierstrass, Werke, Berlin, 1903, vol. 3, pp. 39–52, 219–220, 221–238; Schwarz, Gesammelte Mathematische Abhandlungen, Berlin, 1890, vol. 1. See also Darboux, Théorie des Surfaces (2d edition, Paris, 1914), pp. 490–601.</span></small>

contour is a polygon  $\Pi$ . The problem is made to depend on a linear differential equation of second order

$$
\frac {d ^ {2} \theta}{d w ^ {2}} + p \frac {d \theta}{d w} + q \theta = 0\tag{1.1}
$$

where the coefficients p, q are rational functions of the complex variable w with, at first, undetermined coefficients. The monodromy group G of this equation (this is the group of linear transformations undergone by a fundamental set of solutions  $\theta_{1}(w)$ ,  $\theta_{2}(w)$  when w performs circuits about the singular points of the equation) is known as soon as the polygonal contour is given. The monodromy group problem of Riemann is to determine the coefficients in p, q so that (1.1) shall have the prescribed monodromy group G. But the solution of this problem is not all that is required, for that gives only a minimal surface whose polygonal boundary  $\Pi_{1}$  has its sides parallel to those of  $\Pi$ . It remains further to arrange that the sides of  $\Pi_{1}$  shall have the same lengths as those of  $\Pi$ . All this is reduced by Riemann and Weierstrass to a complicated system of transcendental equations in the coefficients of p, q, which they and Schwarz succeed in solving only in special cases.

To these ideas attaches the solution given by R. Garnier for the problem of Plateau. In a preliminary memoir\* he first gives his form of solution of the Riemann monodromy group problem, previously solved by Hilbert, Plemelj and Birkhoff. In a following memoir† he deals with the supplementary conditions relating to lengths of sides of the polygonal boundary, and concludes the existence of a solution of the above mentioned system of transcendental equations. The Plateau problem being thus solved for a polygon, Garnier passes to the case of a more general contour Γ by regarding Γ as a limit of polygons Π. He shows that the solution of the Riemann group problem with the supplementary conditions varies continuously with the data, so that the minimal surface determined by Π approaches to a minimal surface bounded by Γ. To insure the validity of the limit process, Γ is restricted to have bounded curvature by segments.

Subsequent to the presentation by the present writer to this Society‡ of a series of papers containing the substance of the memoir at hand, T. Radó published a note§ showing how the part of Garnier's work concerned with the passage from polygons to more general contours could be materially simpli-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* Annales Scientifiques de l'Ecole Normale Supérieure, (3), vol. 43 (1926), pp. 177–307.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Le problème de Plateau, ibid., vol. 45 (1928), pp. 53–144.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ Annual meeting, at Bethlehem, Pa., December 27, 1929.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ Proceedings of the National Academy of Sciences, vol. 16 (1930), pp. 242–248.</span></small>

fied, and rendering the restriction on  $\Gamma$  less stringent by requiring only rectifiability.

\*(1') Later, after the dispatch to the editors of this journal of the manuscript of the present paper, two other papers by Radó† appeared in which he gives a solution of the Plateau problem, in the first for a rectifiable contour, and in the second for any contour capable of spanning a finite area (three-dimensional space). As its author states, this work is a continuation of the classic ideas, being based on the least-area characterization of a minimal surface and the theory of conformal mapping, especially the Koebe theory—relating to abstract Riemann manifolds—in the form of the theorem that it is possible to map any simply-connected polyhedral surface conformally on the interior of a circle, the map remaining one-one and continuous as between the boundary of the polyhedral surface and the circumference of the circle.

The present work, on the other hand, apart from its advantage of complete generality of the contour, breaks completely with the hitherto classic methods, replacing the area functional by an entirely new and much simpler functional, and carrying through the existence proof without assuming any of the theory of conformal mapping even for ordinary plane regions; on the contrary, in Part IV our results are applied to give new proofs of the classic theorems concerning conformal mapping essentially simpler than the classic proofs, a demonstration of the superior fundamental character of the present mode of attack.

In Part V, after the existence of the minimal surface has been established, the Koebe mapping theorem plays a rôle beside the formulas of Part III in a brief proof of the least-area property. However, we regard this treatment only as a stop-gap, having under development a disposal of the least-area part of the problem not using the Koebe or any other conformal mapping theorem. Such an independent treatment is desirable because the Koebe theory of conformal mapping is comparable in difficulty with the Plateau problem. The avoidance of the former will bring the solution of the least area problem to rest directly on the axioms of analysis, as has already been done in this paper with the proof of the existence of the minimal surface.

(2) A second class of methods is based on the partial differential equation of minimal surfaces (Lagrange)

$$
(1 + q ^ {2}) r - 2 p q s + (1 + p ^ {2}) t = 0.\tag{1.2}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* Article (1') added in proof.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Annals of Mathematics, (2), vol. 31 (1930), pp. 457–469. Mathematische Zeitschrift, vol. 32 (1930), pp. 762–796.</span></small>

Here belongs the work of S. Bernstein\* and Ch. H. Müntz.† The surface is assumed in the restricted form $z = f(x, y)$, and the problem is regarded as a generalized Dirichlet problem, with (1.2) replacing Laplace's equation. Besides the restriction on the representation of the surface, it is assumed that the contour has a convex projection on the $xy$-plane. The work of Müntz has been criticized by Radó.‡

(3) Minimal surfaces first presented themselves in mathematics, and were named, by their property of having least area among all surfaces bounded by a given contour:

$$
\iint (1 + p ^ {2} + q ^ {2}) ^ {1 / 2} d x d y = \text { minimum }.\tag{1.3}
$$

It is in this way that minimal surfaces appear in the pioneer memoir of Lagrange§ on the calculus of variations for double integrals.

In recent years A. Haar|| has treated the Plateau problem from this point of view, using the direct methods of the calculus of variations introduced by Hilbert. Haar assumes the surface in the form $z = f(x, y)$ and the contour subject to the following restriction: any plane containing three points of the contour has a slope with respect to the xy-plane that is less than a fixed finite upper bound, an assumption occurring first in the work of Lebesgue.

(4) The method of the present memoir is as follows. The contour  $\Gamma$  being taken as any Jordan curve in euclidean space of n dimensions, we consider the class of all possible ways of representing  $\Gamma$  as topological image of the unit circle C:

$$
x _ {i} = g _ {i} (\theta)
$$

$$
(i = 1, 2, \dots , n).
$$

This class forms an L-set in the sense of Fréchet's thesis, $^{**}$  and is compact and closed after “improper” topological representations of  $\Gamma$  have been adjoined: these are limits of proper ones and cause arcs of  $\Gamma$  to correspond to single points of C, or vice-versa ( $\S3$ ). The principal idea is then to introduce the functional ( $\S5$ )

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* Mathematische Annalen, vol. 69 (1910), pp. 82–136, especially § 18.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Mathematische Annalen, vol. 94 (1925), pp. 53–96.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ Mathematische Annalen, vol. 96 (1927), pp. 587–596.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ Miscellanea Taurinensia, vol. 2 (1760–61); also Oeuvres, vol. 1; p. 335.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|| Ueber das Plateausche Problem, Mathematische Annalen, vol. 97 (1927), pp. 124–158.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">¶ Intégrale, longueur, aire, Annali di Matematica, (3), vol. 7, pp. 231–359; see chapter VI, especially p. 348.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*\* Sur quelques points du calcul fonctionnel, Rendiconti del Circolo Matematico di Palermo, vol. 22 (1906), pp. 1–74.</span></small>

$$
A (g) = \frac {1}{4 \pi} \int_ {C} \int_ {C} \frac {\sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2}}{4 \sin^ {2} \frac {\theta - \phi}{2}} d \theta d \phi ,\tag{1.4}
$$

where the integrand has the following simple geometric interpretation: square of chord of contour divided by square of corresponding chord of the unit circle. This improper double integral has a determinate positive value, finite or $+\infty$, for every representation $g$. It is readily shown (§9) that $A(g)$ is lower semi-continuous; therefore, by a theorem of Fréchet† to the effect that a lower semi-continuous functional on a compact closed set attains its minimum value, the minimum of $A(g)$ is attained for a certain representation $x_{i}=g_{i}^{*}(\theta)$. If

(1.4 $_{1}$ )

$$
x _ {i} = H _ {i} (u, v) = \Re F _ {i} (w)\tag{\((w = u + iv)\}
$$

are the harmonic functions in the interior of the unit circle determined according to Poisson's integral by the boundary functions

$$
x _ {i} = g _ {i} ^ {*} (\theta)\tag{1.42}
$$

it is then proved (§§11–16) that

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = 0;\tag{1.43}
$$

briefly speaking, this condition expresses that the first variation of $A(g)$ vanishes for the minimizing $g = g^*$. According to the formulas of Weierstrass, the condition (1.4$_3$) expresses that (1.4$_1$) defines a minimal surface. After it has been shown (§§17, 18) that $g^*$ is a proper representation of $\Gamma$, it follows that this minimal surface is bounded by $\Gamma$, since by the properties of Poisson's integral the functions (1.4$_1$) then attach continuously to the boundary values (1.4$_2$).

One consideration is necessary to validate the preceding argument: we must be sure that  $A(g)$  is not identically  $=+\infty$ , that it takes a finite value for some g. This is what makes it necessary to divide the discussion into two parts. In Part I we assume that there exists a parametric representation g of the given contour such that  $A(g)$  is finite. It will be seen from Parts III and V that this means, more concretely, that it is possible to span some surface of finite area in the given contour. A sufficient condition for the property “there exists a g for which  $A(g)$  is finite” (which, in anticipation of the discussion of Parts III and V, we will call the finite-area-spanning property) is that

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Loc. cit., §11, p. 9.</span></small>

the contour be rectifiable. For if the contour have length L, and we choose as parameter  $\theta=2\pi s/L$ , s being arc-length reckoned from any fixed initial point, then it will be readily seen from the fact that a chord is not greater than its arc that the integrand in  $A(g)$  stays bounded, hence  $A(g)$  is finite for this parameter. In particular, every polygon has the finite-area-spanning property. That, however, a finite-area-spanning contour is superior in generality to a rectifiable contour may be seen by taking any simply-connected portion of a surface, having finite area, and drawing upon it any non-rectifiable Jordan curve (e.g., a non-rectifiable Jordan curve on a sphere).

Part II deals with the case of an arbitrary Jordan contour, where generally  $A(g) \equiv +\infty$ , meaning that no finite area whatever can be spanned in the given contour; an example of such a contour is given in §27. The existence theorem is extended to a contour of this type by an easy limit process, wherein the given contour is regarded as a limit of polygons. In this case the minimal surface can be defined only by the Weierstrass equations, the least-area characterization becoming meaningless.†

The distinctive feature of the present work is the determination of the minimal surface by the minimizing of the functional  $A(g)$ , decidedly simpler of treatment than the classic area functional.  $A(g)$  has a simple relation to the area functional, dealt with in Part III. If  $S(g)$  denote the area of the surface  $x_{i}=H_{i}(u,v)$ , these being the harmonic functions in  $u^{2}+v^{2}<1$  determined by the boundary functions  $x_{i}=g_{i}(\theta)$ , then  $A(g)\geq S(g)$ , and the relation of equality holds when and only when the surface is minimal. Thus  $A(g)$ , not equal to area in general, is capable of giving information about area in the case of a minimal surface. Part III, moreover, provides the basis for the easy proof in Part V that the minimal surface whose existence is proved in Parts I and II has the least area of any surface bounded by  $\Gamma$ .

An interesting and important consideration, unremarked before the writer's work, is that the Riemann conformal mapping problem is included as the special case n=2 in the problem of Plateau. The Riemann mapping theorem relating to the interiors of two Jordan regions is supplemented by the theorem of Osgood‡ and Carathéodory§ to the effect that the conformal correspondence between the interiors induces a topological correspondence between the boundaries. In Part IV a proof is given of the combined theorems of Riemann and Osgood-Carathéodory, independent of any previous treatment, and more elementary and perspicuous.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† But see the footnote at the end of this paper.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ Osgood and E. H. Taylor, Conformal transformations on the boundaries of their regions of definition, these Transactions, vol. 14 (1913), pp. 277–298.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ Carathéodory, Ueber die gegenseitige Beziehung der Ränder bei der konformen Abbildung des Innern einer Jordanschen Kurve auf einen Kreis, Mathematische Annalen, vol. 73 (1913), pp. 305–320.</span></small>

Examples show that the solution of the Plateau problem may not be unique.† The question of the degree of multiplicity of the solution is not dealt with here. As indicated above, the minimal surface whose existence is here assured is the one which furnishes an absolute minimum for the area.

2. Formulation. For definition of a minimal surface we adopt the formulas given, for n=3, by Weierstrass:

$$
x _ {i} = \Re F _ {i} (w)\tag{2.1}
$$

$$
(i = 1, 2, \dots , n)
$$

with

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = 0.\tag{2.2}
$$

The problem of Plateau may then be formulated precisely as follows.

Given any contour $\Gamma$ in the form of a Jordan curve in euclidean space of $n$ dimensions. To prove the existence of $n$ functions $F_{1}, F_{2}, \cdots, F_{n}$ of the complex variable $w$, holomorphic in the interior of the unit circle $C$, satisfying there the condition

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = 0
$$

identically, and whose real parts

$$
x _ {i} = \Re F _ {i} (w)
$$

attach continuously to boundary values on. C

$$
x _ {i} = g _ {i} (\theta)
$$

which represent $\Gamma$ as a topological image of $C$.

As defined by (2.1), (2.2), the minimal surface appears in a representation on the circular region  $|w|<1$  which is conformal except at those (necessarily isolated) points where simultaneously

$$
F _ {1} ^ {\prime} (w) = 0, \quad F _ {2} ^ {\prime} (w) = 0, \quad \dots , \quad F _ {n} ^ {\prime} (w) = 0.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† The following example was communicated to the writer by N. Wiener. Two co-axial circles may be so placed that the area of the catenoidal segment determined by them is greater than the sum of the areas of the two circles (Goldschmidt discontinuous solution). Consider the contour formed by two meridians of the catenoid, very close together, and the arcs remaining on the circles after the small arcs intercepted between the meridians have been removed. One solution of the Plateau problem for this contour is the intercepted part of the catenoid. But the surface formed of the two circles and the narrow catenoidal strip between the meridians has a smaller area. Consequently, there will be a second minimal surface bounded by the given contour, varying slightly from the surface just described: this second surface will have the absolutely least area.</span></small>

On this remark is based the inclusion of the Riemann mapping problem in the Plateau problem as the special case n=2. We show that for n=2 the conformality is free of singular points, but for n>2 their absence cannot be guaranteed.†

## I. A FINITE-AREA-SPANNING CONTOUR

Hypothesis. Part I is based on the hypothesis that there exists a parametric representation g of the given contour for which  $A(g)$  is finite.

3. Topological correspondences between  $\Gamma$  and C.  $\Gamma$  may be supposed

![](images/page_7_chart_4.jpg)

FIG. 1. Torus of representation $R = \Gamma C$

given in some initial representation  $x_{i}=f_{i}(t)$ , from which its most general representation may be derived by a relation  $t=t(\theta)$  defining a one-one continuous transformation of C into itself. The two-dimensional manifold  $(t,\theta)$  of pairs of points one on  $\Gamma$ , one on C, forms a torus  $\Gamma C$ , which will be called the torus of representation and denoted by R. This torus is depicted in the annexed figure as a square where points opposite one another on parallel sides, such as A and  $A'$ , B and  $B'$ , are to be regarded as identical. Rectilinear transversals of the square parallel to C will be termed parallels, those parallel to  $\Gamma$  meridians. A topological correspondence between  $\Gamma$  and C is represented by a continuous closed curve, such as  $A B B'A'$ , which is intersected in one and only one point by each parallel and by each meridian; such a curve may be described as cyclically monotonic. We will denote by P the totality of these curves, which, we will say, represent proper topological correspondences between  $\Gamma$  and C. In the corresponding equations  $x_{i}=g_{i}(\theta)$  of  $\Gamma$  the functions  $g_{i}$  are continuous, and are not all constant on any arc of C.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$x_{1} = \Re w^{2}, x_{2} = \Re -iw^{2}, x_{3} = \Re w^{3}, x_{4} = \Re -iw^{3};\left|w\right|\leq 1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|w| < 1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Example: $x_{1} = \Re w^{2}, x_{2} = \Re - iw^{2}, x_{3} = \Re w^{3}, x_{4} = \Re - iw^{3}, |w| \leq 1$. This is a minimal surface bounded by the contour $x_{1} = \cos 2\theta, x_{2} = \sin 2\theta, x_{3} = \cos 3\theta, x_{4} = \sin 3\theta$. Neither the minimal surface nor the contour is self-intersecting. The representation on $|w| < 1$ is conformal except at the origin, where angles are multiplied by 2.</span></small>

A disadvantage in dealing with $\mathfrak{P}$ is that it is not a closed set: a sequence of curves of $\mathfrak{P}$ may converge to a limit not belonging to $\mathfrak{P}$. For instance, we may obtain as limit of curves of $\mathfrak{P}$ a curve such as $ODEFGO''$, containing a segment of meridian $DE$ or a segment of parallel $FG$, as well as properly monotonic arcs. An extreme case is that indicated by the dotted curve, where the limit is $OO'O''$, consisting of a parallel together with a meridian.

A correspondence between  $\Gamma$  and C whose graph contains, besides properly monotonic arcs, a meridian-segment less than an entire meridian, or a parallel-segment less than an entire parallel, will be called an improper topological correspondence.

In the graph ODEFGO'', the meridian-segment DE represents an arc  $Q'Q''$  of  $\Gamma$  which corresponds to a single point P of C. In the corresponding equations of  $\Gamma$, the functions  $g_i$  have one-sided limits at P equal respectively to the coördinates of  $Q'$  and  $Q''$; and at least one of these functions is discontinuous (the vector g is discontinuous) since,  $\Gamma$  having by hypothesis no double points,  $Q'$  and  $Q''$  are distinct. A monotonic function has at most a denumerable infinity of discontinuities, each in the form of distinct one-sided limits; therefore in an improper representation the functions  $g_i$  have at most a denumerable infinity of discontinuities, all of the so-called first kind, that is, where one-sided limits exist but are unequal. This observation will assure us in §5 of the existence for an improper representation of the Riemann integrals used in defining  $A(g)$.

The parallel-segment FG represents an arc  $P^{\prime}P^{\prime\prime}$  of C which corresponds to a single point Q of  $\Gamma$ . The functions  $g_{i}$  are constant on the arc  $P^{\prime}P^{\prime\prime}$ , where they are equal to the coordinates of Q.

The class of all improper representations of $\Gamma$ will be denoted by $\mathfrak{F}$, and will be divided according to the above description into the two sub-classes $\mathfrak{F}_1$ and $\mathfrak{F}_2$, not mutually exclusive:

$\mathfrak{J}_{1}$, improper representations of the first kind, in which an arc of $\Gamma$ less than all of $\Gamma$ corresponds to a single point of $C$.

$\Im_{2}$ , improper representations of the second kind, in which an arc of C less than all of C corresponds to a single point of  $\Gamma$ .

Special attention must now be given to the correspondences between $\Gamma$ and $C$ whose graph consists of a parallel together with a meridian, such as $OO'O''$. Here the whole of $\Gamma$ corresponds to a single point of $C$, and the whole of $C$ to a single point of $\Gamma$. Such a representation will be termed degenerate; there are evidently $\infty^2$ degenerate representations, obtained by varying the distinguished points on $\Gamma$ and $C$. In the corresponding equations of $\Gamma$ the functions $g$; reduce to constants. The functional $A(g)$ will not be defined for the degenerate representations.

Three fixed points. After having established in §6 a certain invariance property of  $A(g)$ , we shall be led to consider the class of those proper or improper representations of  $\Gamma$  wherein three distinct fixed points  $P_{1}, P_{2}, P_{3}$ , of C, correspond to three distinct fixed points  $Q_{1}, Q_{2}, Q_{3}$ , of  $\Gamma$ . These representations are pictured on the torus  $R = \Gamma C$  by proper or improper cyclically monotonic curves passing through three fixed points no two of which lie on the same parallel or the same meridian.

The preceding discussion leads us to distinguish the following classes of representations of  $\Gamma$  on C.

(1) The class of all representations: proper, improper, and degenerate,

$$
\mathfrak {R} = \mathfrak {P} + \mathfrak {I} + \mathfrak {D}.
$$

(2) The class of all proper and improper representations:

$$
\mathfrak {M} = \mathfrak {P} + \mathfrak {I}.
$$

This is not a closed set, since a sequence of representations of M may tend to a degenerate representation as limit. M will serve as the range of the argument in the functional  $A(g)$ .

(3) The class of all proper and improper representations whereby three distinct fixed points of  $\Gamma$  correspond to three distinct fixed points of C:

$$
\mathfrak {M} ^ {\prime} = \mathfrak {P} ^ {\prime} + \mathfrak {I} ^ {\prime}.
$$

It is important to observe the following two properties of  $M'$ : it is closed; it does not contain any degenerate representation.

4. Harmonic surfaces. Each representation  $x_{i}=g_{i}(\theta)$  of  $\Gamma$  determines a surface  $x_{i}=\Re F_{i}(w)$ , where the harmonic functions  $\Re F_{i}(w)$  are those defined by Poisson's integral based on the respective boundary functions  $g_{i}(\theta)$ . We will refer to this surface as the harmonic surface determined by the representation g.

The limit of Poisson's integral when $w$ approaches to a point $\theta$ of $C$ where $g_i(\theta)$ is continuous is $g_i(\theta)$. If $g_i(\theta)$ has unequal one-sided limits at the point $\theta$, then the limiting value of Poisson's integral in the approach of $w$ to $\theta$ varies between these one-sided limits in a manner that depends linearly on the angle made by the direction of approach with the radius to the point $\theta$.†

It follows that the harmonic surface determined by any proper representation of  $\Gamma$  is bounded by  $\Gamma$ . For an improper representation of the first kind, where the point P of C corresponds to the arc  $Q'Q''$  of  $\Gamma$ , it is evident that the boundary points of the harmonic surface obtained by allowing w to approach

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† A result due to Schwarz; cf. Picard, Traité d'Analyse, vol. 1 (3d edition, Paris, 1922), pp. 315–319.</span></small>

to P in all the possible directions form the chord  $Q'Q''$ . In an improper representation of the second kind, the point w approaching to any point of an arc  $P'P''$  of C gives the same boundary point Q for the harmonic surface.

It is to be observed from this that in the case of an improper representation of the first kind the corresponding harmonic surface will not be bounded by  $\Gamma$ , but by a curve derived from  $\Gamma$  by replacing certain of its arcs (at most a denumerable infinity) by their chords, which chords will correspond to single points of C. In the case of an improper representation of the second kind, the boundary point corresponding to each arc  $P^{\prime}P^{\prime\prime}$  lies on  $\Gamma$ , but then  $\Gamma$  is not in one-one relation with C.

Example 1. The graph of the correspondence between  $\Gamma$  and C may consist of k parallel-segments alternating with k meridian-segments. The boundary of the corresponding harmonic surface is a polygon of k sides and k vertices inscribed in  $\Gamma$ . The sides of the polygon correspond respectively to k points of C, and the vertices to the k arcs into which these points divide C. If k=2, the harmonic surface reduces to a chord of  $\Gamma$ . If k=1, the case of a degenerate representation, the harmonic surface reduces to a point of  $\Gamma$ .

Example 2. The correspondence $t = t(\theta)$ between $\Gamma$ and $C$ may be defined by the frequently cited monotonic function based on Cantor's perfect set.† Here the boundary of the harmonic surface consists of a denumerable infinity of chords of $\Gamma$ together with the nowhere-dense perfect set of points of $\Gamma$ which remain after the arcs of these chords have been removed. On $C$ we have an everywhere-dense denumerable infinity of points of discontinuity of $x_{i} = g_{i}(\theta)$, corresponding respectively to the above-mentioned chords of $\Gamma$.

It will be seen from these examples that the harmonic surface determined by a given representation of $\Gamma$ cannot be regarded as bounded by $\Gamma$ unless this representation is proper. It is for this reason that after establishing the existence of a representation $x_{i} = g_{i}^{*}(\theta)$ such that the corresponding harmonic surface obeys the condition $\sum_{i=1}^{n} F_{i}^{\prime 2}(w) = 0$, it is necessary (as is done in §§17, 18) to prove that the representation $g^{*}$ is proper before we can say we have a minimal surface bounded by $\Gamma$.

5. The fundamental functional  $A(g)$ . The functional  $A(g)$  is defined on the set  $M = P + J$  of all proper and improper representations of  $\Gamma$  by the formula

$$
A (g) = \frac {1}{1 6 \pi} \int_ {c} \int_ {c} \frac {\sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2}}{\sin^ {2} \frac {\theta - \phi}{2}} d \theta d \phi .\tag{5.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† See Carathéodory, Vorlesungen über reelle Funktionen, Leipzig, 1918, §156, p. 159.</span></small>

The domain of integration CC is a torus, which will be denoted by T. This torus of integration is to be carefully distinguished from the torus of representation R of §3.

The integrand is defined everywhere on T except on the diagonal  $\theta=\phi$ , where it takes the indeterminate form 0/0. Let us isolate the diagonal from the rest of the torus by means of two regular curves† symmetrically disposed

![](images/page_11_chart_2.jpg)

FIG. 2. Torus of integration T = CC

on either side of it, enclosing a region $\tau_{1}$ which we delete from the torus, leaving $T_{1} = T - \tau_{1}$.

In case $g$ is proper, or improper only of the second kind, the integrand of (5.1) is defined and continuous on $T_{1}$.

If g is improper of the first kind, the integrand is discontinuous at the points of certain parallels and meridians, symmetrically disposed with respect to the diagonal, and at most denumerably infinite in number. At a point belonging to a parallel but not to a meridian of discontinuity (or vice-versa), the discontinuity is in the form of distinct limits $^{\ddagger}$ according as the point is approached from one side or the other of the parallel (or meridian). At a point of intersection of a parallel of discontinuity with a meridian of discontinuity, there are four distinct limits $^{\ddagger}$ according to the quadrant within which the point is approached.

In any event, the discontinuities of the integrand in  $T_{1}$  form at most a set of zero measure.

Let $d$ denote the diameter (greatest chord) of $\Gamma$, and $\delta>0$ the smallest value of $|\theta-\phi|$ in $T_{1}$; then the integrand of (5.1) is bounded on $T_{1}$, being

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† The only curves which will come into consideration in this connection will be straight lines parallel to the diagonal and images of them by the regular analytic transformations (6.1), (12.1).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ Some of these may accidentally be equal.</span></small>

$$
\leq \frac {d ^ {2}}{\sin^ {2} \frac {\delta}{2}}.
$$

These two remarks insure the existence of the Riemann integral taken over  $T_{1}$  of the integrand of (5.1).

Imagine now an infinite sequence of regions

$$
\tau_ {1}, \tau_ {2}, \dots , \tau_ {r}, \dots
$$

each contained in the preceding and shrinking to the diagonal as limit, so that the complementary regions

$$
T _ {1}, T _ {2}, \dots , T _ {r}, \dots
$$

swell continually and tend to the entire torus T as limit. Then, because every element of the integral (5.1) is positive (wide sense) the proper Riemann integrals

$$
\iint_ {T _ {1}}, \iint_ {T _ {2}}, \dots , \iint_ {T _ {r}}, \dots
$$

form a continually increasing† sequence of positive† numbers. Hence they approach either to a finite positive limit or to +∞; and this limit is by definition A(g), which thus appears as an improper integral. The same fact of the positivity of each element proves easily that the value obtained for A(g) is independent of the particular sequence of regions τ used in its definition; in fact, A(g) may be defined uniquely as the upper bound of the integral over any region of T to which the diagonal is exterior.

$A(g)$ as an infinite series. For greater definiteness in determining $A(g)$, we proceed to divide the torus T into an infinite number of strips (Fig. 2) by means of the lines

$$
\left| \theta - \phi \right| = \frac {\pi}{r}
$$

$$
(r = 1, 2, 3, \dots). \ddagger
$$

The region defined by the inequality

$$
\frac {\pi}{r + 1} \leq | \theta - \phi | \leq \frac {\pi}{r},\tag{5.2}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">g</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\Delta_{r}^{*}(g)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† That “increasing” and “positive” may here be taken in the strict sense follows by the same proof given a little later on to show that  $\Delta_{r}^{*}(g)$  is strictly positive. The only assumption to be made is that g is not a degenerate representation.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">By $|\theta -\phi |$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">φ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\ddagger$  By  $|\theta-\phi|$  we shall understand the minor arc intercepted between the points  $\theta$  and  $\phi$  on the unit circle C.</span></small>

consisting of a pair of strips symmetric with respect to the diagonal, will be denoted by  $\Delta_{r}$ . We then define the functional

$$
\Delta_ {r} (g) = \frac {1}{1 6 \pi} \iint_ {\Delta_ {r}} \frac {\sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2}}{\sin^ {2} \frac {\theta - \phi}{2}} d \theta d \phi .\tag{5.3}
$$

This is a proper Riemann integral since the integrand stays bounded on $\Delta_r$, being

$$
\leq \frac {d ^ {2}}{\sin^ {2} \frac {\pi}{2 (r + 1)}}.
$$

[Certainly $\Delta_r(g) \geq 0$; but it is interesting (though not necessary for the sequel) to prove the strict inequality $\Delta_r(g) > 0$.

First we see that we could have $\Delta_r(g) = 0$ only by having $\sum_{i=1}^{n}[g_i(\theta) - g_i(\phi)]^2$ identically zero in $\Delta_r$. For if $\sum_{i=1}^{n}[g_i(\theta) - g_i(\phi)]^2 = p > 0$ at some interior point of $\Delta_r$, it would be $>p/2$ in at least a sufficiently small square in the corner of one of the quadrants about this point; therefore this square makes a contribution $>0$ to the value of the integral, which cannot be neutralized by the non-negative contribution of the other elements; hence $\Delta_r(g) > 0$, contrary to the hypothesis $\Delta_r(g) = 0$.

Thus $\Delta_r(g) = 0$ implies $g_i(\theta) = g_i(\phi)$ ($i = 1, 2, \cdots, n$) for all $(\theta, \phi)$ obeying (5.2). Now it is easy to see that, for every $\phi_1, \phi_2$ such that

$$
\left| \phi_ {1} - \phi_ {2} \right| \leq \frac {\pi}{r} - \frac {\pi}{r + 1},\tag{5.4}
$$

a $\theta$ exists such that $(\theta, \phi_1)$ and $(\theta, \phi_2)$ obey (5.2). On account of the transitivity of the relation $g_i(\theta) = g_i(\phi)$, it follows that $\Delta_r(g) = 0$ implies $g_i(\phi_1) = g_i(\phi_2)$ for all $(\phi_1, \phi_2)$ obeying (5.4).

Now any two points whatever $\theta$, $\phi$ of $C$ can be made the first and last of a finite sequence $\theta, \phi_1, \phi_2, \cdots, \phi_m$, $\phi$ any two consecutive terms of which obey (5.4). Consequently $\Delta_r(g) = 0$ implies $g_i(\theta) = g_i(\phi)$ for all $\theta, \phi$; but then $g$ would be a degenerate representation; however, such are excluded from the range of the argument in $A(g)$.]

The functional  $A(g)$  may now be defined as the finite or positively infinite sum of the infinite series of positive terms

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† At a point of discontinuity this will mean that one of the two or four limiting values is equal to p</span></small>

1931]

$$
A (g) = \Delta_ {1} (g) + \Delta_ {2} (g) + \dots + \Delta_ {r} (g) + \dots .\tag{5.5}
$$

6. The invariance of  $A(g)$ . This section is devoted to proving the important observation that  $A(g)$  is invariant under the transformation

$$
\tan \frac {\bar {\theta}}{2} = \frac {a \tan \frac {\theta}{2} + b}{c \tan \frac {\theta}{2} + d} \quad (a, b, c, d \text {   real }; a d - b c \neq 0)\tag{6.1}
$$

of the circumference of the unit circle into itself.

In the expression (5.1) for  $A(g)$  make the substitution

$$
x = \tan {\frac {\theta}{2}}, \quad y = \tan {\frac {\phi}{2}} \cdot \dagger\tag{6.2}
$$

We have

$$
\begin{array}{r l} \frac {d \theta d \phi}{\sin^ {2} \frac {\theta - \phi}{2}} & = \frac {d \theta d \phi}{\left(\sin \frac {\theta}{2} \cos \frac {\phi}{2} - \cos \frac {\theta}{2} \sin \frac {\phi}{2}\right) ^ {2}} \\ & = \frac {\sec^ {2} \frac {\theta}{2} d \theta \cdot \sec^ {2} \frac {\phi}{2} d \phi}{\left(\tan \frac {\theta}{2} - \tan \frac {\phi}{2}\right) ^ {2}} = \frac {4 d x d y}{(x - y) ^ {2}}. \end{array}
$$

When  $\theta$  and  $\phi$  vary independently over C from  $-\pi$  to  $+\pi$ , x and y vary independently from  $-\infty$  to  $+\infty$ ; so that, denoting by  $h_{i}(x)$ ,  $h_{i}(y)$  the functions which result from  $g_{i}(\theta)$ ,  $g_{i}(\phi)$  by the substitutions inverse to (6.2):

$$
h _ {i} (x) = g _ {i} (2 \operatorname{arc} \tan x), h _ {i} (y) = g _ {i} (2 \operatorname{arc} \tan y),
$$

we have as transformed expression for $A(g)$:

$$
A (g) = \frac {1}{4 \pi} \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} \sum_ {i = 1} ^ {n} [ h _ {i} (x) - h _ {i} (y) ] ^ {2} \frac {d x d y}{(x - y) ^ {2}}.\tag{6.3}
$$

In terms of the variables (6.2), the transformation (6.1) is

$$
\bar {x} = \frac {a x + b}{c x + d}, \quad \bar {y} = \frac {a y + b}{c y + d}.\tag{6.4}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† This may be interpreted as replacing the unit circle by a half-plane, its circumference by the edge of the half-plane.</span></small>

Let $\bar{g}_i(\overline{\theta}), \overline{h}_i(\bar{x})$ be the functions that result from $g_i(\theta), h_i(x)$ by the respective transformations (6.1), (6.4); then

$$
A (\bar {g}) = \frac {1}{4 \pi} \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} \sum_ {i = 1} ^ {n} [ \bar {h} _ {i} (\bar {x}) - \bar {h} _ {i} (\bar {y}) ] ^ {2} \frac {d \bar {x} d \bar {y}}{(\bar {x} - \bar {y}) ^ {2}}.\tag{6.5}
$$

The domain of integration in (6.3) is the entire real plane  $(x, y)$ , and the entire real plane  $(\bar{x}, \bar{y})$  is the domain of integration in (6.5), because (6.4) sets up a one-one correspondence between all finite and infinite real values of x and of  $\bar{x}$ , and the same for y and  $\bar{y}$ .

The following simple calculations now lead to the desired result:

$$
\begin{array}{r l} d \bar {x} & = \frac {a d - b c}{(c x + d) ^ {2}} d x, \quad d \bar {y} = \frac {a d - b c}{(c y + d) ^ {2}} d y; \\ \bar {x} - \bar {y} & = \frac {(a d - b c) (x - y)}{(c x + d) (c y + d)}; \\ \frac {d \bar {x} d \bar {y}}{(\bar {x} - \bar {y}) ^ {2}} & = \frac {d x d y}{(x - y) ^ {2}}. \end{array}
$$

Therefore, by comparison of (6.5) with (6.3),

$$
A (\bar {g}) = A (g).
$$

Equivalent representations. Three fixed points. Let us designate as equivalent any two representations g,  $\bar{g}$  which are related to one another by a transformation (6.1). On account of the presence of three essential parameters in the transformation, it is possible to find for every non-degenerate representation g an equivalent  $\bar{g}$  which causes any chosen three distinct points of C to correspond to any chosen three distinct points of  $\Gamma$ . In the notation of §3: every element of M has an equivalent in  $M'$ .

Since $A(g)$ has the same value for two equivalent $g$'s, it follows that the lower bound $M$ of $A(g)$ on $\mathfrak{M}$ is equal to the lower bound $M'$ of $A(g)$ on $\mathfrak{M}'$; and if we can prove that $M'$ is attained for a certain $\bar{g}$, then obviously $M$ is attained for every $g$ equivalent to $\bar{g}$. As already pointed out, the advantage of referring from $\mathfrak{M}$ to $\mathfrak{M}'$ is that the latter is a closed set not containing any degenerate representation, while the former is an open set, having the degenerate representations among its limit elements.

7. Fréchet's thesis; compact closed sets. We now have the problem of proving that $A(g)$ attains its minimum on $\mathfrak{M}'$. This will be accomplished by means of the simple and general ideas of Fréchet's thesis,$^{\dagger}$ which concerns real-valued functions on sets of a very general nature.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† For reference, see the Introduction.</span></small>

Suppose we have a set A of elements a of any nature. Fréchet terms this an L-set under the following conditions. Every infinite sequence

$$
a _ {1}, a _ {2}, \dots , a _ {m}, \dots
$$

of elements of A is definitely designated as convergent or divergent, and with each convergent sequence there is associated a unique element of A called the limit of the sequence. Every sub-sequence of a convergent sequence must itself be convergent and have the same limit as the original sequence. Every infinite sequence all of whose elements are identical with the same element of A is convergent and has this element for limit.

An L-set is termed compact if it obeys the Bolzano-Weierstrass theorem: every infinite sub-set of the given set contains a convergent sequence of distinct elements, or has a limit element.

An L-set is termed closed provided every limit of an infinite sequence of elements of the set belongs to the set. Evidently the notion of closure has meaning only when the given set is considered as part of a larger set.

An L-set both compact and closed is termed by Fréchet an extremal set, because the fundamental theorem of Weierstrass that a continuous function on a closed interval in the ordinary real domain attains its extreme values, maximum and minimum, applies to such a set. This is easily proved in the cited thesis after the following definition of continuous function on an L-set has been given.

A real-valued function  $U(a)$  of the elements of a set A is termed continuous if whenever the sequence of elements

$$
a _ {1}, a _ {2}, \dots , a _ {m}, \dots
$$

converges to the element a as limit, then the sequence of functional values

$$
U (a _ {1}), U (a _ {2}), \dots , U (a _ {m}), \dots
$$

converges in the ordinary sense to the value  $U(a)$ . This means, of course, that for every  $\epsilon > 0$  there is an index  $m_{\epsilon}$  such that, for every  $m > m_{\epsilon}$ ,

$$
U (a) - \epsilon <   U (a _ {m}) <   U (a) + \epsilon .
$$

If we require only the first of these two inequalities, we have the notion of lower semi-continuity: a function  $U(a)$  is lower semi-continuous if, with the conventions of the preceding paragraph, we have

$$
U (a _ {m}) > U (a) - \epsilon\tag{7.1}
$$

for $m > m_{\epsilon}$.

An alternative statement is:

$$
\begin{array}{c}a _ {1},   a _ {2},   \dots ,   a _ {m},   \dots \rightarrow a,\\U (a _ {1}),   U (a _ {2}),   \dots ,   U (a _ {m}),   \dots \rightarrow L,\\U (a) \leq L,\end{array}\tag{7.2) if}
$$

a condition also expressed in the form

$$
U (a) \leqslant \liminf _ {m \to \infty} U (a _ {m}).
$$

It is shown by Fréchet† that a lower semi-continuous function on a compact closed L-set attains its minimum value. Our proof that  $A(g)$  attains its minimum will be a particular application of this general theorem. However, for the sake of completeness, we will not assume this easily proved theorem, but shall establish it in §10 with the actual set  $M'$  and functional  $A(g)$  here under consideration.

8. The topological correspondences between $\Gamma$ and $C$ as an $L$-set. With a natural definition of limit, the set $\Re$ of all (proper, improper, and degenerate) representations of $\Gamma$ as topological image of $C$ is an $L$-set, as are also its sub-sets $\mathfrak{M}$ and $\mathfrak{M}'$. We will say, namely, that a sequence of representations

$$
g ^ {(1)}, g ^ {(2)}, \dots , g ^ {(m)}, \dots
$$

converges to a certain representation g as limit when the graphs of  $g^{(1)}$ ,  $g^{(2)}$ ,  $\cdots$ ,  $g^{(m)}$ ,  $\cdots$  on the torus  $R=\Gamma C$  (Fig. 1) converge in the ordinary sense to the graph of g; this will mean that if  $R_{e}$  denote the region covered by a circle of radius  $\epsilon$  whose center describes the graph of g, then for all sufficiently large values of m the graph of  $g^{(m)}$  lies within  $R_{e}$ .

The L-set R (and, automatically, its sub-sets M and M') has the important property of compactness, the proof of which results directly from the following theorem:‡

An infinite set of curves contained in a finite domain is compact if the curves are rectifiable and their lengths less than a fixed finite upper bound.

The torus R which contains all the graphs of R is a finite domain.

Suppose a rectilinear polygon inscribed in the graph of any representation g. Then, resolving each side into its projections along a parallel and along a meridian, and adding, we obtain

length of inscribed polygon $\leq$ length of parallel + length of meridian,

where the cyclically monotonic character of the graph insures that each projection is counted once and only once. It follows from this inequality that each

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Loc. cit., §11, p. 9.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ Fréchet, loc. cit., p. 65.</span></small>

curve of $\Re$ is rectifiable and has a length $\leq$ the finite upper bound: length of parallel + length of meridian.

Thus R obeys all the conditions of the above theorem, and is compact.

$M'$ is an extremal set: compact and closed.

9. The lower semi-continuity of  $A(g)$ . In (5.5) we have expressed  $A(g)$  as the sum of an infinite series of positive terms. Defining the partial sums

$$
A _ {r} (g) = \Delta_ {1} (g) + \Delta_ {2} (g) + \dots + \Delta_ {r} (g) = \frac {1}{1 6 \pi} \int \int_ {T _ {r}} \frac {\sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2}}{\sin^ {2} \frac {\theta - \phi}{2}} d \theta d \phi ,\tag{9.1}
$$

where  $T_{r}$  denotes the domain

$$
\frac {\pi}{r + 1} \leq | \theta - \phi | \leq \pi ,
$$

we may also express $A(g)$ as the limit of the sequence

$$
A _ {1} (g), A _ {2} (g), \dots , A _ {r} (g), \dots ,
$$

which, since each $\Delta_r(g) > 0$, is continually increasing:

$$
A _ {1} (g) <   A _ {2} (g) <   \dots <   A _ {r} (g) <   \dots .
$$

It is easily seen that each  $A_{r}(g)$  is a continuous functional of g: if a sequence of representations

$$
g ^ {(1)}, g ^ {(2)}, \dots , g ^ {(m)}, \dots
$$

tends to $g$ as limit, then

$$
A _ {r} (g ^ {(1)}), A _ {r} (g ^ {(2)}), \dots , A _ {r} (g ^ {(m)}), \dots
$$

tends to $A_r(g)$. For the integrand in (9.1) is uniformly bounded, being

$$
\leq \frac {d ^ {2}}{\sin^ {2} \frac {\pi}{2 (r + 1)}},
$$

where d is the diameter of  $\Gamma$ , and under this condition it is permissible to pass to the limit under the sign of integration.

The lower semi-continuity of  $A(g)$  now results from the following general theorem.

THEOREM. If a sequence of continuous† functions on an L-set tend, in increasing (wide sense), to a limit function (finite or infinite valued), then this limit function is lower semi-continuous.

Let $a$ denote an arbitrary element of the $L$-set, and

$$
U _ {1} (a) \leq U _ {2} (a) \leq \dots \leq U _ {r} (a) \leq \dots ,\tag{9.2}
$$

the increasing sequence of functions tending to the limit  $U(a)$ . Let

$$
a _ {1}, a _ {2}, \dots , a _ {m}, \dots
$$

be any sequence of elements converging to a as limit.

Case 1: $U(a)$ finite. If $\epsilon > 0$ be assigned arbitrarily, there exists an $r_{\epsilon}$ such that for $r > r_{\epsilon}$.

$$
U _ {r} (a) > U (a) - \epsilon / 2.\tag{9.3}
$$

We suppose that in this inequality r has a fixed value  $>r_{e}$ , for instance,  $r=r_{e}+1$ .

By hypothesis, the function  $U_{r}$  is continuous; this implies the existence of an  $m_{e}$  such that for  $m > m_{e}$

$$
U _ {r} (a _ {m}) > U _ {r} (a) - \epsilon / 2.\tag{9.4}
$$

Combining the inequalities (9.3) and (9.4), we have

$$
U _ {r} (a _ {m}) > U (a) - \epsilon\tag{9.5}
$$

for $m > m_{\epsilon}$.

Now, by (9.2), each of the functions  $U_{r}$  is, for any fixed value of the argument, not greater than the limit function U; thus

$$
U (a _ {m}) \geq U _ {r} (a _ {m})\tag{9.6}
$$

for every $m$, in particular for $m > m_{\epsilon}$.

From (9.5) and (9.6) it follows that

$$
U (a _ {m}) > U (a) - \epsilon
$$

for $m > m_{\epsilon}$; but this is the definition of lower semi-continuity, according to (7.1).

Case 2:  $U(a)=+\infty$ . Here lower semi-continuity becomes identical with continuity: if  $a_{1}, a_{2}, \cdots, a_{m}, \cdots$  is any sequence of elements converging to a, then

$$
U (a _ {1}), U (a _ {2}), \dots , U (a _ {m}), \dots
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">to +∞</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">tends to $+\infty$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† The theorem still remains valid if the functions of the sequence are merely lower semi-continuous. Cf. Carathéodory, Vorlesungen über reelle Funktionen, Leipzig, 1918, p. 175, where this theorem is proved for functions of n real variables.</span></small>

For the proof, let G be an arbitrarily assigned finite positive number; then since by hypothesis

$$
\lim _ {r \rightarrow \infty} U _ {r} (a) = + \infty ,
$$

an index $r$ exists such that

$$
U _ {r} (a) > 2 G.\tag{9.7}
$$

Because of the continuity of the function  $U_{r}$ , there exists an index  $m_{G}$  such that for  $m > m_{G}$

$$
U _ {r} (a _ {m}) > U _ {r} (a) - G.\tag{9.8}
$$

Combining (9.7) and (9.8), we have

$$
U _ {r} (a _ {m}) > G
$$

for $m > m_G$. From this and (9.6), it follows that

$$
U (a _ {m}) > G
$$

for $m > m_G$, that is,

$$
\lim _ {m \rightarrow \infty} U (a _ {m}) = + \infty ,
$$

which was to be proved.

Since  $A(g)$  obeys all the conditions of the theorem just proved, its lower semi-continuity is established. $^{\dagger}$

10.  $A(g)$  attains its minimum. In this section we prove that  $A(g)$ , as a lower semi-continuous function on the compact closed set  $M'$ , must attain its minimum value on  $M'$ .

Since the values of $A(g)$ are all positive, and some are finite, they have a finite lower bound $M \geq 0. \ddagger$. By definition of lower bound, $A(g)$ cannot take any value less than $M$, but can approach to $M$ from above as closely as we please. On this basis we can construct a minimizing sequence

$$
g ^ {(1)}, g ^ {(2)}, \dots , g ^ {(m)}, \dots ,\tag{10.1}
$$

that is, one such that

$$
A (g ^ {(1)}), A (g ^ {(2)}), \dots , A (g ^ {(m)}), \dots\tag{10.2}
$$

tends to the limit M; the construction of such a sequence is the first step in the direct treatment of any calculus of variations problem.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$g^{\bullet}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\geq A(g^{0})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">+∞)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$A(g)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">M>0.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† It is easy to prove that by making g approach suitably to  $g^{0}$ , any number whatever  $\geq A(g^{0})$  (including  $+\infty$ ) can be made the limit of  $A(g)$ .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\dagger$ After it has been proved that M is attained, it results that M>0.</span></small>

Now the sequence (10.1) may not converge to a limit, but since the set $\mathfrak{M}'$ is compact, we can select a sub-sequence

$$
g ^ {(m _ {1})}, g ^ {(m _ {2})}, \dots , g ^ {(m _ {k})}, \dots\tag{10.1'}
$$

which converges to a limit  $g^{*}$ ; on account of the closure of  $M'$ ,  $g^{*}$  belongs to  $M'$ . The sequence of corresponding functional values

$$
A \left(g ^ {(m _ {1})}\right), A \left(g ^ {(m _ {2})}\right), \dots , A \left(g ^ {(m _ {k})}\right), \dots ,\tag{10.2'}
$$

being a sub-sequence of (10.2) with the limit M, must tend to the same limit M.

Using the lower semi-continuity of  $A(g)$  as expressed in (7.2), we therefore have

$$
A (g ^ {*}) \leq M;
$$

but the definition of lower bound makes  $A(g^{*}) < M$  impossible, consequently

$$
A (g ^ {*}) = M,
$$

that is: the minimum of $A(g)$ on $\mathfrak{M}'$ is attained for $g^*$.

By the discussion at the end of §6, it follows that the minimum of $A(g)$ on $\mathfrak{M}$ is attained for $g^*$ and all its equivalents.

11. Calculation of the power series  $\sum_{i=1}^{n}F_{i}^{'2}(w)$ . The rest of our argument is concerned with showing that the harmonic surface

$$
x _ {i} = \Re F _ {i} (w)
$$

determined by the minimizing representation  $g^{*}$  is minimal:

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = 0.
$$

This will be done by showing that, in a sense whose precise meaning appears in the sequel, the last condition expresses the vanishing of the first variation of  $A(g)$  for  $g = g^{*}$ .

The functions  $F_{i}(w)$  determined by the representation

$$
x _ {i} = g _ {i} (\theta)
$$

of $\Gamma$ are given by the power series, convergent (at least) in the interior of the unit circle $C$,

$$
F _ {i} (w) = \frac {a _ {i 0}}{2} + \sum_ {p = 1} ^ {\infty} (a _ {i p} - i b _ {i p}) w ^ {p}, \dagger\tag{11.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Throughout, the symbol i will be used in two senses: i the index running from 1 to n, and i the square root of -1. This notation should not lead to any confusion.</span></small>

where $a_{ip}, b_{ip}$ are the Fourier coefficients of $g_i(\theta)$:

$$
a _ {i p} = \frac {1}{\pi} \int_ {C} g _ {i} (\theta) \cos p \theta d \theta , b _ {i p} = \frac {1}{\pi} \int_ {C} g _ {i} (\theta) \sin p \theta d \theta .\tag{11.2}
$$

Instead of $\sum_{i=1}^{n} F_i'^2(w)$ we shall find it more convenient to work with $w^2 \sum_{i=1}^{n} F_i'^2(w)$; it will be easy to dispose of the factor $w^2$ when we wish. The latter expression is representable in the interior of $C$ by a power series, derivable from (11.1) by performing formally the operations indicated:

$$
w ^ {2} \sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = \sum_ {m = 2} ^ {\infty} \left(A _ {m} - i B _ {m}\right) w ^ {m}.\tag{11.3}
$$

The special object of this section is to calculate the coefficients $A_{m}, B_{m}$; the results appear in (11.15).

Since the power series (11.1) is convergent in the interior of C, we may differentiate termwise, and find

$$
w F _ {i} ^ {\prime} (w) = \sum_ {p = 1} ^ {\infty} p \left(a _ {i p} - i b _ {i p}\right) w ^ {p}.\tag{11.4}
$$

Rewriting this as

$$
w F _ {i} ^ {\prime} (w) = \sum_ {q = 1} ^ {\infty} q \left(a _ {i q} - i b _ {i q}\right) w ^ {q},\tag{11.4'}
$$

we obtain, on multiplying together (11.4) and (11.4') and summing as to i from 1 to n, the formula (11.3) with

$$
A _ {m} - i B _ {m} = \sum_ {i = 1} ^ {n} \sum_ {p, q} p (a _ {i p} - i b _ {i p}) \cdot q (a _ {i q} - i b _ {i q})\tag{11.5}
$$

where the range of the summation indices p, q is

$$
p \geq 1, q \geq 1, p + q = m.\tag{11.6}
$$

From (11.2),

$$
a _ {i p} - i b _ {i p} = \frac {1}{\pi} \int_ {C} g _ {i} (\theta) e ^ {- p i \theta} d \theta , a _ {i q} - i b _ {i q} = \frac {1}{\pi} \int_ {C} g _ {i} (\phi) e ^ {- q i \phi} d \phi .
$$

The product of the two parts of this formula, after multiplying the first by p, the second by q, may be expressed as a double integral:

$$
\begin{array}{r l} p (a _ {i p} - i b _ {i p}) \cdot q (a _ {i q} - i b _ {i q}) & \\ = \frac {1}{\pi^ {2}} \int_ {C} \int_ {C} g _ {i} (\theta) g _ {i} (\phi) \cdot p e ^ {- p i \theta} \cdot q e ^ {- q i \phi} \cdot d \theta d \phi . \end{array}\tag{11.7}
$$

We have obviously

$$
\int_ {C} \int_ {C} g _ {i} ^ {2} (\theta) \cdot p e ^ {- p i \theta} \cdot q e ^ {- q i \phi} \cdot d \theta d \phi = \int_ {C} g _ {i} ^ {2} (\theta) \cdot p e ^ {- p i \theta} d \theta \cdot \int_ {C} q e ^ {- q i \phi} d \phi = 0\tag{11.8}
$$

since the second factor vanishes; and similarly

$$
\int_ {c} \int_ {c} g _ {i} ^ {2} (\phi) \cdot p e ^ {- p i \theta} \cdot q e ^ {- q i \phi} \cdot d \theta d \phi = 0.\tag{11.8'}
$$

By the last three equations we may write

$$
\begin{array}{r l} p (a _ {i p} - i b _ {i p}) \cdot q (a _ {i q} - i b _ {i q}) & = - \frac {1}{2 \pi^ {2}} \int_ {C} \int_ {C} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \cdot p e ^ {- p i \theta} \cdot q e ^ {- q i \phi} \cdot d \theta d \phi , \end{array}\tag{11.9}
$$

for, on expanding the bracket squared, this reduces to (11.7) when account is taken of (11.8), (11.8').

Substituting (11.9) in (11.5), we have

$$
A _ {m} - i B _ {m} = - \frac {1}{2 \pi^ {2}} \int_ {C} \int_ {C} \sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2} \cdot \sum_ {p, q} p e ^ {- p i \theta} \cdot q e ^ {- q i \phi} \cdot d \theta d \phi .\tag{11.10}
$$

Accordingly, we have to calculate

$$
\sum_ {p, q} p e ^ {- p i \theta} \cdot q e ^ {- \stackrel {\bullet} {q} i \phi}\tag{11.11}
$$

where the range of $p, q$ is as defined in (11.6). Let

$$
e ^ {- i \theta} = \zeta , e ^ {- i \phi} = z,\tag{11.12}
$$

so that (11.11) becomes

$$
\begin{array}{r l} \sum_ {p, q} p \zeta^ {p} \cdot q z ^ {q} & = (m - 1) \zeta^ {m - 1} z + (m - 2) \zeta^ {m - 2} \cdot 2 z ^ {2} + \dots \\ & \quad + 2 \zeta^ {2} \cdot (m - 2) z ^ {m - 2} + \zeta \cdot (m - 1) z ^ {m - 1}. \end{array}\tag{11.11'}
$$

The value of the last expression can be found by starting with the geometric progression

$$
\zeta^ {m} + \zeta^ {m - 1} z + \zeta^ {m - 2} z ^ {2} + \dots + \zeta^ {2} z ^ {m - 2} + \zeta z ^ {m - 1} + z ^ {m} = \frac {\zeta^ {m + 1} - z ^ {m + 1}}{\zeta - z}.
$$

Applying to this the operator

$$
\zeta z \frac {\partial^ {2}}{\partial \zeta \partial z},
$$

we get

(11.13)

The calculation of the first and second terms of this expression is as follows.

First term. Let

$$
\sigma = \frac {\theta + \phi}{2}, \quad \delta = \frac {\theta - \phi}{2}.\tag{11.14}
$$

Then

$$
\zeta z = e ^ {- i (\theta + \phi)} = e ^ {- 2 i \sigma};
$$

$$
\begin{array}{r l} \zeta^ {m} + z ^ {m} & = (\cos m \theta + \cos m \phi) - i (\sin m \theta + \sin m \phi) \\ & = 2 \cos m \sigma \cos m \delta - 2 i \sin m \sigma \cos m \delta \\ & = 2 \cos m \delta e ^ {- m i \sigma}; \end{array}
$$

$$
\begin{array}{r l} \zeta - z & = (\cos \theta - \cos \phi) - i (\sin \theta - \sin \phi) \\ & = - 2 \sin \sigma \sin \delta - 2 i \cos \sigma \sin \delta \\ & = - 2 i \sin \delta e ^ {- i \sigma}; \end{array}
$$

$$
(\zeta - z) ^ {- 2} = - \frac {1}{4 \sin^ {2} \delta} e ^ {2 i \sigma};
$$

$$
\text { First   term } = - \frac {(m + 1) \cos m \delta}{2 \sin^ {2} \delta} e ^ {- m i \sigma}.
$$

Second term.

$$
\begin{array}{c} \zeta z = e ^ {- 2 i \sigma}; \\ \zeta^ {m + 1} - z ^ {m + 1} = - 2 i \sin (m + 1) \delta e ^ {- (m + 1) i \sigma}, \end{array}
$$

found from the above formula for $\zeta - z$ by replacing $\theta, \phi$ by $(m + 1)\theta$, $(m + 1)\phi$;

$$
(\zeta - z) ^ {- 3} = \frac {1}{8 i \sin^ {3} \delta} e ^ {3 i \sigma};
$$

$$
\text { Second   term } = \frac {\sin (m + 1) \delta}{2 \sin^ {3} \delta} e ^ {- m i \sigma}.
$$

Substituting these results in (11.13), we obtain

$$
\sum_ {p, q} p \zeta^ {p} \cdot q z ^ {q} = \left\{- \frac {(m + 1) \cos m \delta}{2 \sin^ {2} \delta} + \frac {\sin (m + 1) \delta}{2 \sin^ {3} \delta} \right\} e ^ {- m i \sigma}.
$$

The bracket is equal to

$$
\begin{array}{r l} & \frac {- (m + 1) \cdot 2 \cos m \delta \sin \delta + 2 \sin (m + 1) \delta}{4 \sin^ {3} \delta} \\ & = \frac {- (m + 1) \left\{\sin (m + 1) \delta - \sin (m - 1) \delta \right\} + 2 \sin (m + 1) \delta}{4 \sin^ {3} \delta} \\ & = - \frac {(m - 1) \sin (m + 1) \delta - (m + 1) \sin (m - 1) \delta}{4 \sin^ {3} \delta}; \end{array}
$$

so that, referring to the notation (11.12), we have finally for the expression (11.11):

$$
\sum_ {p, q} p e ^ {- p i \theta} \cdot q e ^ {- q i \phi} = - \frac {(m - 1) \sin (m + 1) \delta - (m + 1) \sin (m - 1) \delta}{4 \sin^ {3} \delta} e ^ {- m i \sigma}.
$$

Substituting this in (11.10), we get

$$
\begin{array}{r l} A _ {m} - i B _ {m} = & \frac {1}{8 \pi^ {2}} \int_ {C} \int_ {C} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \\ & \cdot \frac {(m - 1) \sin (m + 1) \delta - (m + 1) \sin (m - 1) \delta}{\sin^ {3} \delta} e ^ {- m i \sigma} d \theta d \phi . \end{array}
$$

Writing  $e^{-mi\sigma} = \cos m\sigma - i \sin m\sigma$ , separating the real and imaginary parts, and referring to the notation (11.14), we arrive at the final expressions for  $A_{m}, B_{m}$ :

$$
\begin{array}{l} A _ {m} = \frac {1}{8 \pi^ {2}} \int_ {C} \int_ {C} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \\ \cdot \frac {(m - 1) \sin [ (m + 1) \frac {\theta - \phi}{2} ] - (m + 1) \sin [ (m - 1) \frac {\theta - \phi}{2} ]}{\sin^ {3} \frac {\theta - \phi}{2}} \cos [ m \frac {\theta + \phi}{2} ] d \theta d \phi , \\ B _ {m} = \frac {1}{8 \pi^ {2}} \int_ {C} \int_ {C} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \\ \cdot \frac {(m - 1) \sin [ (m + 1) \frac {\theta - \phi}{2} ] - (m+ 1) \sin [ (m - 1) \frac {\theta - \phi}{2} ]}{\sin^ {3} \frac {\theta - \phi}{2}} \sin [ m \frac {\theta + \phi}{2} ] d \theta d \phi . \end{array}\tag{11.15}
$$

It may be observed that these are proper Riemann integrals, for the fraction, which takes for  $\theta=\phi$  the indeterminate form 0/0, has the limiting value  $-(2/3)m(m^{2}-1)$ .

12. The functions $C_m(\lambda), S_m(\lambda); C_{mr}(\lambda), S_{mr}(\lambda)$. Hypothesis. The work of §§12-15 is valid on the sole hypothesis that $g$ is a fixed representation for which the functional $A(g)$ has a finite value.† In particular, we may put $g = g^*$, the minimizing representation of $A(g)$, since $A(g^*)$ is finite.

Consider the transformations

$$
\bar {\theta} = \theta + \lambda \cos m \theta = c (\theta), \bar {\theta} = \theta + \lambda \sin m \theta = s (\theta),\tag{12.1}
$$

m any fixed positive integer,

of the unit circle C into itself  $\bar{C}$ . If  $\lambda$  is a real parameter restricted to the interval

$$
- \frac {1}{m} <   \lambda <   \frac {1}{m},\tag{12.2}
$$

then each of these transformations is one-one and continuous. This results from the fact that the respective derivatives

$$
\frac {d \bar {\theta}}{d \theta} = 1 - m \lambda \sin m \theta , \quad \frac {d \bar {\theta}}{d \theta} = 1 + m \lambda \cos m \theta
$$

are positive for all  $\theta$  under the condition (12.2). Consequently the transformations (12.1) have one-one continuous inverses

$$
\theta = c ^ {- 1} (\bar {\theta}), \theta = s ^ {- 1} (\bar {\theta}),\tag{12.1'}
$$

and applying these to the representation g, we get the family of representations  $g(c^{-1}(\overline{\theta}))$ ,  $g(s^{-1}(\overline{\theta}))$ , depending on the parameter  $\lambda$ .

The values of  $A(g)$  for these representations are respectively

$$
\frac {1}{1 6 \pi} \iint_ {\overline {{T}}} \frac {\sum_ {i = 1} ^ {n} \left[ g _ {i} (c ^ {- 1} (\bar {\theta})) - g _ {i} (c ^ {- 1} (\bar {\phi})) \right] ^ {2}}{\sin^ {2} \frac {\bar {\theta} - \bar {\phi}}{2}} d \bar {\theta} d \bar {\phi},
$$

$$
\frac {1}{1 6 \pi} \iint_ {\overline {{T}}} \frac {\sum_ {i = 1} ^ {n} \left[ g _ {i} (s ^ {- 1} (\bar {\theta})) - g _ {i} (s ^ {- 1} (\bar {\phi})) \right] ^ {2}}{\sin^ {2} \frac {\bar {\theta} - \bar {\phi}}{2}} d \bar {\theta} d \bar {\phi},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§17</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† It will follow from §17 that, in particular, g cannot be improper of the first kind.</span></small>

where the torus  $\overline{T}=\bar{C}\bar{C}$  corresponds to the torus T=CC by the equations (12.1). Making the change of variables (12.1) in these double integrals, we obtain two functions of  $\lambda$, which we will denote respectively by  $C_{m}(\lambda)$,  $S_{m}(\lambda)$:

$$
\begin{array}{l} C _ {m} (\lambda) = \frac {1}{1 6 \pi} \iint_ {T} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \frac {(1 - m \lambda \sin m \theta) (1 - m \lambda \sin m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2}\right)} d \theta d \phi , \\ S _ {m} (\lambda) = \frac {1}{1 6 \pi} \iint_ {T} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \frac {(1 + m \lambda \cos m \theta) (1 + m \lambda \cos m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\sin m \theta - \sin m \phi}{2}\right)} d \theta d \phi . \end{array} \tag {12.3}
$$

These are improper Riemann integrals (singular locus $\theta = \phi$).

As in §5, we express the torus T as the sum of an infinite number of strips:

$$
T = \Delta_ {1} + \Delta_ {2} + \dots + \Delta_ {r} + \dots ,
$$

defined by (5.2). Replacing the domain of integration T in (12.3) by  $\Delta_{r}$ , we derive the functions

$$
\begin{array}{l} C _ {m r} (\lambda) = \frac {1}{1 6 \pi} \iint_ {\Delta_ {r}} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \frac {(1 - m \lambda \sin m \theta) (1 - m \lambda \sin m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2}\right)} d \theta d \phi , \\ S _ {m r} (\lambda) = \frac {1}{1 6 \pi} \iint_ {\Delta_ {r}} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \frac {(1 + m \lambda \cos m \theta) (1 + m \lambda \cos m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\sin m \theta - \sin m \phi}{2}\right)} d \theta d \phi . \end{array} \tag {12.4}
$$

These are proper Riemann integrals since the domain $\Delta_r$ does not contain any singular points $\theta = \phi$.

In this way we have for definition of $C_m(\lambda), S_m(\lambda)$ the infinite series

$$
\begin{array}{l} C _ {m} (\lambda) = C _ {m 1} (\lambda) + C _ {m 2} (\lambda) + \dots + C _ {m r} (\lambda) + \dots , \\ S _ {m} (\lambda) = S _ {m 1} (\lambda) + S _ {m 2} (\lambda) + \dots + S _ {m r} (\lambda) + \dots . \end{array}\tag{12.5}
$$

Complex values of  $\lambda$ . We shall wish to make use of certain classic convergence theorems valid only in the complex domain; for this reason we now allow  $\lambda$  to be a complex variable:

$$
\lambda = \mu + \nu i,
$$

subject to the restriction

$$
\left| \lambda \right| <   1 / m \cdot\tag{12.6}
$$

The (open) circle in the complex plane defined by this inequality will be denoted by  $C_{m}$ . Evidently  $C_{m}$  contains the real interval (12.2).

The expressions (12.4) are still proper Riemann integrals defining the now complex-valued functions  $C_{mr}(\lambda)$ ,  $S_{mr}(\lambda)$ . To be assured of this, we must show that the denominators of the respective integrands do not vanish in the domain  $\Delta_{r}$ . These denominators are

$$
\begin{array}{l} \sin^ {2} \left(\frac {\theta - \phi}{2} + \mu \frac {\cos m \theta - \cos m \phi}{2} + i \nu \frac {\cos m \theta - \cos m \phi}{2}\right), \\ \sin^ {2} \left(\frac {\theta - \phi}{2} + \mu \frac {\sin m \theta - \sin m \phi}{2} + i \nu \frac {\sin m \theta - \sin m \phi}{2}\right). \end{array}
$$

Since the function  $\sin^{2}(z/2)$  vanishes when and only when  $z=2k\pi$  (k=0,  $\pm1$ ,  $\pm2$ ,  $\cdots$ ), it is evident that for these expressions to vanish we must have respectively

(12.7)

$$
\begin{array}{l} \theta + \mu \cos m \theta = \phi + \mu \cos m \phi , \\ \theta + \mu \sin m \theta = \phi + \mu \sin m \phi \end{array}\tag{mod 2π).}
$$

But $|\mu| \leq |\lambda| < 1/m$, and under this condition on the real parameter $\mu$ the equations (12.1), with $\mu$ in place of $\lambda$, define a one-one transformation. Hence each equation (12.7) implies

$$
\theta = \phi\tag{mod 2π);}
$$

but this condition is never satisfied in the domain $\Delta_r$.

The proof is thus complete that  $C_{mr}(\lambda)$ ,  $S_{mr}(\lambda)$  are well-defined by the formulas (12.4) for all values of  $\lambda$  in the interior of the circle  $C_{m}$ .

We now define  $C_{m}(\lambda)$ ,  $S_{m}(\lambda)$  for complex  $\lambda$  by the infinite series (12.5) provided these series are absolutely convergent. We shall prove that the series in question are indeed absolutely convergent for all  $\lambda$  in  $C_{m}$ , and then (what is of paramount importance) that  $C_{m}(\lambda)$ ,  $S_{m}(\lambda)$  are analytic functions of  $\lambda$  in  $C_{m}$ .

Plan. The proof of the analyticity of  $C_{m}(\lambda)$ ,  $S_{m}(\lambda)$  will consist of a direct application of the Weierstrass double-series theorem. $^{\dagger}$  We will show in §13 that each term  $C_{mr}(\lambda)$ ,  $S_{mr}(\lambda)$  of the series (12.5) is an analytic function of  $\lambda$  in  $C_{m}$ , and then in §14 that the series (12.5) is uniformly convergent in every circle concentric with and smaller than  $C_{m}$ . The result is to justify the formal operation of expanding in powers of  $\lambda$  the integrands in the formulas (12.3) for  $C_{m}(\lambda)$ ,  $S_{m}(\lambda)$ , and then performing termwise the double integration as to  $\theta$ ,  $\phi$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Cf. Knopp, Funktionentheorie, Berlin and Leipzig, 1918, vol. 1, p. 89.</span></small>

13. Analyticity of  $C_{mr}(\lambda)$ ,  $S_{mr}(\lambda)$ . Considering the formulas (12.4) for  $C_{mr}(\lambda)$ ,  $S_{mr}(\lambda)$ , we have just shown that the denominators of the fractions

$$
\frac {(1 - m \lambda \sin m \theta) (1 - m \lambda \sin m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2}\right)}, \frac {(1 + m \lambda \cos m \theta) (1 + m \lambda \cos m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\sin m \theta - \sin m \phi}{2}\right)} \tag {13.1}
$$

do not vanish for  $(\theta, \phi)$  in  $\Delta_{r}$  and  $\lambda$  in  $C_{m}$ ; therefore these fractions are holomorphic functions of  $\lambda$  in  $C_{m}$ , depending on the parameters  $\theta, \phi$ . They are developable in a series of powers of  $\lambda$  convergent in  $C_{m}$ , with coefficients functions of  $\theta, \phi$ . The developments may be obtained in the usual way as Taylor series, and are given by the following calculations, where we retain terms only as far as the first power of  $\lambda$ .

Returning to the notation (11.14),

$$
\sigma = \frac {1}{2} (\theta + \phi), \quad \delta = \frac {1}{2} (\theta - \phi),\tag{13.2}
$$

we have

$$
\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2} = \delta - \lambda \sin m \sigma \sin m \delta .
$$

Making in the Taylor expansion

$$
\frac {1}{\sin^ {2} (x + h)} = \frac {1}{\sin^ {2} x} - \frac {2 \cos x}{\sin^ {3} x} h + \dots
$$

the substitutions

$$
x = \delta , h = - \lambda \sin m \sigma \sin m \delta ,
$$

we get

$$
\begin{array}{r l} \frac {1}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2}\right)} & \\ = \frac {1}{\sin^ {2} \delta} + \lambda \frac {2 \cos \delta \sin m \sigma \sin m \delta}{\sin^ {3} \delta} + \dots . \end{array}\tag{13.3}
$$

For the numerator of (13.1) we have

$$
\begin{array}{r l} (1 - m \lambda \sin m \theta) (1 - m \lambda \sin m \phi) & \\ = 1 + \lambda (- 2 m \sin m \sigma \cos m \delta) + \text {term in} \lambda^ {2}. \end{array}\tag{13.4}
$$

Multiplying together (13.3) and (13.4), we get for the development of the first of (13.1)

$$
\frac {1}{\sin^ {2} \delta} + \lambda \left\{\frac {2 \cos \delta \sin m \sigma \sin m \delta}{\sin^ {3} \delta} - \frac {2 m \sin m \sigma \cos m \delta}{\sin^ {2} \delta} \right\} + \dots :
$$

The bracket reduces to

$$
\begin{array}{l} \frac {2 \cos \delta \sin m \delta - 2 m \cos m \sigma \sin \delta}{\sin^ {3} \delta} \sin m \sigma \\ = \frac {\left\{\sin (m + 1) \delta + \sin (m - 1) \delta \right\} - m \left\{\sin (m + 1) \delta - \sin (m - 1) \delta \right\}}{\sin^ {3} \delta} \sin m \sigma \\ = - \frac {(m - 1) \sin (m + 1) \delta - (m + 1) \sin (m - 1) \delta}{\sin^ {3} \delta} \sin m \sigma . \end{array}
$$

Thus we have finally, referring to (13.2),

$$
\begin{array}{l} \frac {(1 - m \lambda \sin m \theta) (1 - m \lambda \sin m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2}\right)} = \frac {1}{\sin^ {2} \frac {\theta - \phi}{2}} \\ - \lambda \frac {(m - 1) \sin [ (m + 1) \frac {\theta - \phi}{2} ] - (m + 1) \sin [ (m - 1) \frac {\theta - \phi}{2} ]}{\sin^ {3} \frac {\theta - \phi}{2}} \sin [ m \frac {\theta + \phi}{2} ] + \dots . \end{array} \tag {13.5}
$$

An entirely similar calculation gives for the second fraction (13.1):

$$
\begin{array}{l} (1 3. 5 ^ {\prime}) \frac {(1 + m \lambda \cos m \theta) (1 + m \lambda \cos m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\sin m \theta - \sin m \phi}{2}\right)} = \frac {1}{\sin^ {2} \frac {\theta - \phi}{2}} \\ + \lambda \frac {(m - 1) \sin [ (m + 1) \frac {\theta - \phi}{2} ] - (m + 1) \sin [ (m - 1) \frac {\theta - \phi}{2} ]}{\sin^ {3} \frac {\theta - \phi}{2}} \cos [ m \frac {\theta + \phi}{2} ] + \dots . \end{array}
$$

The following observation is now of prime importance: if  $\lambda$  is given any fixed value in  $C_{m}$ , so that

$$
\left| \lambda \right| = \rho_ {0} <   \frac {1}{m},\tag{13.6}
$$

then the series (13.5), (13.5') are uniformly convergent when  $(\theta, \phi)$  varies over  $\Delta_{r}$ . To prove this, denote by  $F(\theta, \phi, \lambda)$  the first member of (13.5), and let  $\rho$  be any fixed positive number such that

$$
\rho_ {0} <   \rho <   \frac {1}{m}.\tag{13.7}
$$

Suppose $\theta, \phi, \lambda$ to vary arbitrarily subject to the conditions

$$
(\theta , \phi) \text {   in   } \Delta_ {r}, \quad | \lambda | = \rho .\tag{13.8}
$$

The three-dimensional domain so defined is evidently closed and bounded, and the positive real-valued function  $\left|F(\theta,\phi,\lambda)\right|$  is finite and continuous on this domain, for it has been shown that the denominator of  $F(\theta,\phi,\lambda)$  is never zero in (13.8). By a fundamental theorem,  $\left|F(\theta,\phi,\lambda)\right|$  has therefore a finite upper bound on (13.8):

$$
\mid F (\theta , \phi , \lambda) \mid \leq B,
$$

$B$ being a positive real number independent of $\theta, \phi, \lambda$.

We now apply the appraisal formula of Cauchy† for the coefficients in the power series expansion of an analytic function. According to this formula, if  $A_{k}(\theta, \phi)$  denote the coefficient of  $\lambda^{k}$  in the power series (13.5), then

$$
\left| A _ {k} (\theta , \phi) \right| \leq \frac {B}{\rho^ {k}}
$$

for all $(\theta, \phi)$ in $\Delta_r$. Hence, with (13.6),

$$
\left| A _ {k} (\theta , \phi) \lambda^ {k} \right| \leq B \left(\frac {\rho_ {0}}{\rho}\right) ^ {k}.
$$

Since the series of constant positive terms

$$
\sum_ {k = 0} ^ {\infty} B \left(\frac {\rho_ {0}}{\rho}\right) ^ {k}
$$

is convergent, being a geometric progression of ratio $< 1$ (by (13.7)), the conditions of a standard uniform convergence test of Weierstrass are satisfied, and we have proved the uniform convergence of (13.5) for $\lambda$ fixed in $\mathcal{C}_m$ and $(\theta, \phi)$ varying over $\Delta_r$. The same argument applies to $(13.5')$.

That this uniform convergence is not disturbed when, to obtain the integrands in (12.4) of  $C_{mr}(\lambda)$ ,  $S_{mr}(\lambda)$ , we multiply (13.5), (13.5') by  $\sum_{i=1}^{n}[g_{i}(\theta)-g_{i}(\phi)]^{2}$ , results from the fact that the multiplying factor is bounded:

$$
\sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2} \leq d ^ {2},
$$

where d is the diameter of  $\Gamma$ .

Consequently, after introducing this factor in (13.5), (13.5'), we may integrate as to  $\theta$ ,  $\phi$  over  $\Delta_{r}$  term by term, and find that  $C_{mr}(\lambda)$ ,  $S_{mr}(\lambda)$  are equal to power series in  $\lambda$ :

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Cf. Knopp, loc. cit., vol. 1. p. 84.</span></small>

$$
\begin{array}{l} C _ {m r} (\lambda) = \Delta_ {r} (g) + C _ {m r} ^ {\prime} (0) \lambda + \dots , \\ S _ {m r} (\lambda) = \Delta_ {r} (g) + S _ {m r} ^ {\prime} (0) \lambda + \dots , \end{array}\tag{13.9}
$$

convergent for $\lambda$ in $\mathcal{C}_m$.

We are especially interested in the values of the coefficients of the first power of  $\lambda$ , which, referring to (13.5), (13.5'), are seen to be

(13.10)

$$
\begin{array}{l} C _ {m r} ^ {\prime} (0) = - \frac {1}{1 6 \pi} \iint_ {\Delta_ {r}} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \\ \cdot \frac {(m - 1) \sin [ (m + 1) \frac {\theta - \phi}{2} ] - (m + 1) \sin [ (m - 1) \frac {\theta - \phi}{2} ]}{\sin^ {3} \frac {\theta - \phi}{2}} \sin [ m \frac {\theta - \phi}{2} ] d \theta d \phi , \\ . 1 0) \\ S _ {m r} ^ {\prime} (0) = \frac {1}{1 6 \pi} \iint_ {\Delta_ {r}} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \\ \cdot \frac {(m - 1) \sin [ (m + 1) \frac {\theta - \phi}{2} ] - (m + 1) \sin [ (n - 1) \frac {\theta - \phi}{2} ]}{\sin^ {3} \frac {\theta - \phi}{2}} \cos [ m \frac {\theta + \phi}{2} ] d \theta d \phi . \end{array}
$$

14. Analyticity of the functions  $C_{m}(\lambda)$ ,  $S_{m}(\lambda)$ . The function  $C_{m}(\lambda)$  is defined by the infinite series (12.5), each of whose terms has just been proved analytic in the circle  $C_{m}$ . We proceed to prove that this series is uniformly convergent in every smaller concentric circle

$$
\mid \lambda \mid \leq \rho , \rho <   \frac {1}{m}.\tag{14.1}
$$

The analyticity of  $C_{m}(\lambda)$  will then result immediately by the Weierstrass double-series theorem. The same argument applies to  $S_{m}(\lambda)$ .

Considering $C_{mr}(\lambda)$, we have from (12.4)

$$
\begin{array}{r l} \left| C _ {m r} (\lambda) \right| & \leqslant \frac {1}{1 6 \pi} \iint_ {\Delta_ {r}} \sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2} \\ & \cdot \left| \frac {(1 - m \lambda \sin m \theta) (1 - m \lambda \sin m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2}\right)} \right| d \theta d \phi . \end{array}\tag{14.2}
$$

Comparing this with the formula (5.3) for  $\Delta_{r}(g)$ , also a double integral over  $\Delta_{r}$  with positive real elements, we wish to prove that the quotient of the integrand of (14.2) by that of  $\Delta_{r}(g)$ ,

$$
Q (\theta , \phi , \lambda) = \left| \frac {(1 - m \lambda \sin m \theta) (1 - m \lambda \sin m \phi)}{\sin^ {2} \left(\frac {\theta - \phi}{2} + \lambda \frac {\cos m \theta - \cos m \phi}{2}\right)} \right| \sin^ {2} \frac {\theta - \phi}{2},\tag{14.3}
$$

has a finite upper bound when  $(\theta, \phi)$  varies over the entire torus T (not merely over  $\Delta_{r}$ ) and  $\lambda$  varies independently over the closed circle (14.1).

The expression (14.3) is not defined on the diagonal  $\theta=\phi$  of the torus T, taking there the indeterminate form 0/0; but it is seen directly that (14.3) has the limit value 1 for  $\theta=\phi$ :

$$
Q (\phi , \phi , \lambda) = 1.\tag{14.3'}
$$

The function $Q(\theta, \phi, \lambda)$ is thus defined on the closed domain (of four real dimensions)

$$
(\theta , \phi) \text {   on   } T, | \lambda | \leq \rho ,\tag{14.4}
$$

by (14.3) if $\theta \neq \phi$ and by (14.3') if $\theta = \phi$. As has been remarked several times, the denominator of (14.3) cannot vanish if $|\lambda| < 1/m$, $\theta \neq \phi$. Hence $Q(\theta, \phi, \lambda)$ is finite and continuous on the closed and bounded domain (14.4). It therefore has a finite positive upper bound $K$.

Consequently,

$$
\left| C _ {m r} (\lambda) \right| \leq K \dot {\Delta} _ {r} (g)\tag{14.5}
$$

where it is to be emphasized that $K$ is independent of $r$.

According to the hypothesis stated at the beginning of §12, g is a fixed representation for which  $A(g)$  is finite. It follows that

$$
K \Delta_ {1} (g) + K \Delta_ {2} (g) + \dots + K \Delta_ {r} (g) + \dots
$$

is a series of constant, positive terms, convergent to the sum  $KA(g)$ . By the inequality (14.5) this series dominates the series (12.5) for  $C_{m}(\lambda)$ . Therefore, by the same uniform convergence test of Weierstrass used in the preceding section, the series (12.5) for  $C_{m}(\lambda)$  is absolutely and uniformly convergent in the circle (14.1).

The conditions of the Weierstrass double-series theorem being now satisfied, we may assert that  $C_{m}(\lambda)$  is analytic in the circle  $C_{m}$ .

According to the same theorem, the coefficients in the power series representing  $C_{m}(\lambda)$  are to be found by adding together the coefficients of like powers of  $\lambda$  in the various terms  $C_{mr}(\lambda)$  (summation of the double series by columns). By §13, the coefficient of any given power of  $\lambda$  in the expansion of  $C_{mr}(\lambda)$  is a double integral taken over  $\Delta_{r}$  of an integrand that is the same for all r. Therefore the coefficient of this power of  $\lambda$  in  $C_{m}(\lambda)$  is the double

integral of the same integrand taken over the entire torus T. Consequently, referring to (13.9), (13.10), we have

$$
C _ {m} (\lambda) = A (g) + C _ {m} ^ {\prime} (0) \lambda + \dots\tag{14.6}
$$

with

$$
\begin{array}{l} (1 4. 7) C _ {m} ^ {\prime} (0) = - \frac {1}{1 6 \pi} \iint_ {T} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \\ \cdot \frac {(m - 1) \sin [ (m + 1) \frac {\theta - \phi}{2} ] - (m + 1) \sin [ (m - 1) \frac {\theta - \phi}{2} ]}{\sin^ {3} \frac {\theta - \phi}{2}} \sin [ m \frac {\theta + \phi}{2} ] d \theta d \phi . \end{array}
$$

The entire preceding argument applies to  $S_{m}(\lambda)$ , and gives

$$
S _ {m} (\lambda) = A (g) + S _ {m} ^ {\prime} (0) \lambda + \dots\tag{14.6'}
$$

with

$$
\begin{array}{l} (1 4. 7 ^ {\prime}) S _ {m} ^ {\prime} (0) = \frac {1}{1 6 \pi} \iint_ {T} \sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2} \\ \cdot \frac {(m - 1) \sin \left[ (m + 1) \frac {\theta - \phi}{2} \right] - (m + 1) \sin \left[ (m + 1) \frac {\theta - \phi}{2} \right]}{\sin^ {3} \frac {\theta - \phi}{2}} \cos \left[ m \frac {\theta - \phi}{2} \right] d \theta d \phi . \end{array}
$$

15. Relations between $A_{m}, B_{m}$ and $C_{m}'(0), S_{m}'(0)$. The ultimate purpose of the calculations of §§11-14 was to establish the following relations, observable immediately by comparing (11.5) with (14.7), (14.7'):

$$
A _ {m} = \frac {2}{\pi} S _ {m} ^ {\prime} (0), B _ {m} = - \frac {2}{\pi} C _ {m} ^ {\prime} (0).\tag{15}
$$

16. Existence of the minimal surface. The introduction of complex values of  $\lambda$  having served its purpose of establishing the power series (14.7), (14.7'), we now return to real values of  $\lambda$  in the interval (12.2),

$$
- \frac {1}{m} <   \lambda <   \frac {1}{m},\tag{16.1}
$$

where these power series remain valid, since this interval is part of the circle  $C_{m}$ .

By applying the one-one continuous transformations (12.1) to the fixed representation g, we obtained in §12 a family of representations depending on

the parameter  $\lambda$ , and containing, for  $\lambda=0$ , the original representation g. Thus the function  $C_{m}(\lambda)$  is a part of the functional  $A(g)$  in the sense that its values are those of  $A(g)$  on a certain part of the total range of g.

Suppose now  $g=g^{*}$ , the minimizing representation of  $A(g)$ . Then, a fortiori,  $C_{m}(\lambda)$ , considered as a function on the interval (16.1), has a minimum at  $\lambda=0$ , the value corresponding to  $g^{*}$ . Consequently,

$$
C _ {m} ^ {\prime} (0) = 0.\tag{16.2}
$$

Analogously,

$$
S _ {m} ^ {\prime} (0) = 0.\tag{16.2'}
$$

Therefore, by (15),

$$
A _ {m} = 0, B _ {m} = 0.\tag{16.3}
$$

Since $m$ may have any integral value, it follows that every coefficient in $w^2 \sum_{i=1}^{n} F_i'^2(w)$ vanishes, where $F_i(w)$ are the power series, convergent within the unit circle, determined by $g^*$ according to (11.1), (11.2). Hence, dividing out the non-identically vanishing factor $w^2$, we have

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = 0,\tag{16.4}
$$

which expresses that the harmonic surface

$$
x _ {i} = \Re F _ {i} (w)
$$

determined by  $g^{*}$  is minimal.

That this minimal surface is bounded by  $\Gamma$  will follow after we have shown in the next two sections that  $g^{*}$  is a proper representation of  $\Gamma$ .

17.  $g^{*}$  cannot be improper of the first kind. We will rule out the possibility that  $g^{*}$  be improper of the first kind by proving that for a g of this type

$$
A (g) = + \infty .
$$

Since, by the hypothesis governing Part I,  $A(g)$  takes a finite value for at least one representation g, the supposition that  $g^{*}$ , minimizing  $A(g)$ , could be improper of the first kind is thus reduced to an absurdity.

In an improper representation of the first kind, a point P of C corresponds to an arc  $Q'Q''$  of  $\Gamma$  less than all of  $\Gamma$ . Since, by hypothesis,  $\Gamma$  has no double points, the end points  $Q'$ ,  $Q''$  are distinct and their distance l is not equal to zero.

The (vector) function g will have a discontinuity at P, where the distinct one-sided limits  $Q'$ ,  $Q''$  will exist. Therefore if two points of C approach to P

from opposite sides, the distance between the corresponding points of  $\Gamma$  tends to l as limit. Consequently, if f denote any fixed proper fraction,

$$
\sum_ {i = 1} ^ {n} \left[ g _ {i} (\theta) - g _ {i} (\phi) \right] ^ {2} > f l ^ {2}\tag{17.1}
$$

under the conditions

$$
\alpha <   \theta \leq \alpha + \delta , \alpha - \delta \leq \phi <   \alpha ,\tag{17.2}
$$

where  $\alpha$  denotes the angular coordinate of P and  $\delta>0$  is fixed sufficiently small.

The domain  $(\theta,\phi)$  defined by (17.2) is a square S on the torus T, with one vertex  $\theta=\phi=\alpha$  on the diagonal of T.

![](images/page_36_image_6.jpg)

Since the double integral (5.1) defining  $A(g)$  is composed of non-negative elements, its value over T is not less than its value over S:

$$
A (g) \geq \frac {1}{1 6 \pi} \iint_ {S ^ {\prime}} \frac {\sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2}}{\sin^ {2} \frac {\theta - \phi}{2}} d \theta d \phi ;\tag{17.3}
$$

therefore, by (17.1),

$$
A (g) \geq m \iint_ {S} \frac {d \theta d \phi}{\sin^ {2} \frac {\theta - \phi}{2}}\tag{17.4}
$$

where $m = fl^2 / (16\pi)$ is a positive constant.

The integral (17.4) is improper, since the integrand becomes infinite at the vertex of S lying on the diagonal  $\theta=\phi$ ; hence this integral must be expressed as a limit:

[January

$$
\iint_ {S} \frac {d \theta d \phi}{\sin^ {2} \frac {\theta - \phi}{2}} = \lim _ {\epsilon \rightarrow 0} \iint_ {S _ {\epsilon}} \frac {d \theta d \phi}{\sin^ {2} \frac {\theta - \phi}{2}} = \lim _ {\epsilon \rightarrow 0} \int_ {\alpha + \epsilon} ^ {\alpha + \delta} \int_ {\alpha - \delta} ^ {\alpha - \epsilon} \frac {d \theta d \phi}{\sin^ {2} \frac {\theta - \phi}{2}}.\tag{17.5}
$$

Here  $S_{\epsilon}$  is the square indicated in Fig. 3, obtained from S by removing strips of width  $\epsilon$  along two of its sides.

We have for any double integral between constant limits the formula

$$
\int_ {a} ^ {b} \int_ {c} ^ {d} f (\theta , \phi) d \theta d \phi = F (b, d) - F (b, c) - F (a, d) + F (a, c),
$$

where $F(\theta, \phi)$ is any primitive of $f(\theta, \phi)$, that is, such that

$$
\frac {\partial^ {2} F}{\partial \theta \partial \phi} = f (\theta , \phi).
$$

In the case of (17.5),

$$
F = 4 \log \sin \frac {\theta - \phi}{2},
$$

and therefore

$$
\begin{array}{r l} \int_ {\alpha + \epsilon} ^ {\alpha + \delta} \int_ {\alpha - \delta} ^ {\alpha - \epsilon} \frac {d \theta d \phi}{\sin^ {2} \frac {\theta - \phi}{2}} & = 4 \log \sin \frac {\delta - \epsilon}{2} \\ & - 4 \log \sin \delta - 4 \log \sin \epsilon + 4 \log \sin \frac {\delta -}{2}. \end{array}
$$

If now  $\epsilon\to0$ , the limit of the third term is  $+\infty$ , while the other terms stay finite; therefore the double integral over S is equal to  $+\infty$ ; consequently, by (17.4),

$$
A (g) = + \infty .
$$

18.  $g^{*}$  cannot be improper of the second kind. That  $g^{*}$  cannot be improper of the second kind means that an arc  $P^{\prime}P^{\prime\prime}$  of C, less than all of C, cannot correspond by  $g^{*}$  to a single point Q of  $\Gamma$ . This will be established by showing that  $g^{*}$  cannot convert an arc  $P^{\prime}P^{\prime\prime}$  of C into a point Q of  $\Gamma$  without converting all of C into the point Q (degenerate representation).

The harmonic functions  $\Re F_{i}(w)$  determined by  $g^{*}$  are given by

$$
F _ {i} (w) = \frac {1}{2 \pi} \int_ {C} \frac {e ^ {i \theta} + w}{e ^ {i \theta} - w} g _ {i} ^ {*} (\theta) d \theta\tag{18.1}
$$

(equivalent to the integral of Poisson). It is permissible to differentiate under the integral sign, and we obtain

$$
w F _ {i} ^ {\prime} (w) = \frac {1}{2 \pi} \int_ {C} \frac {2 w e ^ {i \theta}}{(e ^ {i \theta} - w) ^ {2}} g _ {i} ^ {*} (\theta) d \theta .\tag{18.2}
$$

Writing  $w=\rho e^{i\alpha}$ , and taking the imaginary part of each side, we find

$$
\Im w F _ {i} ^ {\prime} (w) = - \frac {1}{2 \pi} \int_ {C} \frac {2 \rho (1 - \rho^ {2}) \sin (\theta - \alpha)}{\left[ 1 - 2 \rho \cos (\theta - \alpha) + \rho^ {2} \right] ^ {2}} g _ {i} ^ {*} (\theta) d \theta .\tag{18.3}
$$

Except for the minus sign, the last expression is identical with one studied by Fatou in his thesis.† Fatou shows that at every point where the derivative $g_{i}^{*\prime}(\theta)$ exists and is continuous the expression in question has a unique limit equal to $g_{i}^{*\prime}(\theta)$ when $(\rho, \alpha) \to (1, \theta)$.

Since in the present case  $g_{i}^{*}(\theta)$  is supposed constant on a certain arc  $P^{\prime}P^{\prime\prime}$ ,  $g_{i}^{*\prime}(\theta)$  has the continuous value zero on this arc; hence for  $\theta$  any point interior to  $P^{\prime}P^{\prime\prime}$ ,

$$
\lim _ {w \rightarrow e ^ {i \theta}} \Im w F _ {i} ^ {\prime} (w) = 0 \quad (i = 1, 2, \dots , n).\tag{18.4}
$$

We have proved in §16 that, $F_{i}(w)$ being determined by $g^{*}$,

$$
\sum_ {i = 1} ^ {n} w ^ {2} F _ {i} ^ {\prime 2} (w) = \sum_ {i = 1} ^ {n} \left[ \Re w F _ {i} ^ {\prime} (w) + i \Im w F _ {i} ^ {\prime} (w) \right] ^ {2} = 0;
$$

taking real parts, we have

$$
\sum_ {i = 1} ^ {n} \left[ \Re w F _ {i} ^ {\prime} (w) \right] ^ {2} = \sum_ {i = 1} ^ {n} \left[ \Im w F _ {i} ^ {\prime} (w) \right] ^ {2}.
$$

Therefore, by (18.4),

$$
\lim _ {w \rightarrow e ^ {i \theta}} \sum_ {i = 1} ^ {n} \left[ \Re w F _ {i} ^ {\prime} (w) \right] ^ {2} = 0;
$$

and since for each value of i

$$
\left| \Re w F _ {i} ^ {\prime} (w) \right| \leq \left\{\sum_ {i = 1} ^ {n} \left[ \Re w F _ {i} ^ {\prime} (w) \right] ^ {2} \right\} ^ {1 / 2},
$$

we have

(18.4')

$$
\lim _ {w \rightarrow e ^ {i \theta}} \Re w F _ {i} ^ {\prime} (w) = 0 \quad (i = 1, 2, \dots , n).
$$

By (18.4) and (18.4'),

$$
\lim _ {w \rightarrow e ^ {i \theta}} w F _ {i} ^ {\prime} (w) = 0\tag{18.5}
$$

$$
(i = 1, 2, \dots , n),
$$

for $\theta$ any interior point of $P'P''$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† P. Fatou, Séries trigonométriques et séries de Taylor, Acta Mathematica, vol. 30 (1906), pp. 347–348.</span></small>

Since the limiting value of the function $wF_{i}'(w)$ when $w$ approaches to any point of the circular arc $P'P''$ is real, we may apply the symmetry principle of Riemann-Schwarz† to prolong the function analytically across this arc, attaching conjugate imaginary values to points inverse with respect to the arc. The function $wF_{i}'(w)$ will then be equal to zero on an arc interior to a domain of regularity, and is therefore identically equal to zero. Hence $F_{i}(w)$ is identically equal to a constant, $F_{i}(w) = a_{i} + ib_{i}$.

It follows that  $x_{i}=g_{i}^{*}(\theta)$ , boundary values of  $\Re F_{i}(w)$ , makes all of C correspond to the point of coordinates  $a_{i}$ ; but this is contrary to hypothesis.

By this and the preceding section, the representation  $g^{*}$  is proper; and therefore the minimal surface of §16, determined by  $g^{*}$ , is bounded by  $\Gamma$ .

With this, we have completed the solution of the problem of Plateau for any finite-area-spanning contour in n-dimensional euclidean space.

## II. AN ARBITRARY JORDAN CONTOUR

19. The Jordan contour as a limit of polygons. The case of an arbitrary Jordan contour $\Gamma$, for which $A(g)$ is identically $+\infty$, will be dealt with by regarding $\Gamma$ as the limit of a sequence of non-self-intersecting polygons‡

$$
\Gamma^ {(1)}, \Gamma^ {(2)}, \dots , \Gamma^ {(m)}, \dots .\tag{19.1}
$$

Let $\Gamma$, referred to a fixed initial parameter $t$, have the equations

$$
x _ {i} = f _ {i} (t).\tag{19.2}
$$

Then the polygons can be represented parametrically by equations

$$
x _ {i} = f _ {i} ^ {(1)} (t), x _ {i} = f _ {i} ^ {(2)} (t), \dots , x _ {i} = f _ {i} ^ {(m)} (t), \dots ,\tag{19.3}
$$

so that $f_{i}^{(m)}(t)$ tends uniformly to $f_{i}(t)$ when $m \to \infty$.

Each polygon  $\Gamma^{(m)}$  has, by Part I, a parameter  $\theta$  such that the corresponding representation

$$
x _ {i} = g _ {i} ^ {(m)} (\theta)\tag{19.4}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">d'A</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Γ,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Cf. G. Julia, Principes Geométriques d'Analyse, Paris, 1930, pp. 44–48, especially paragraph e.<br>‡ See C. Jordan, Cours d'Analyse (2d edition, Paris, 1893), p. 93. The polygons may be only partially inscribed in Γ, being derived from inscribed polygons by removing possible loops.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$x_{i} = f_{i}(t)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$x_{i} = S_{im}(t)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\Gamma^{(m)}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">I,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$t = \omega_{m}(\theta)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">C,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">C</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§17</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">We could also proceed by expressing the continuous functions $x_{i} = f_{i}(t)$ representing $\Gamma$ as the limits of their Fejér trigonometric polynomials $x_{i} = S_{im}(t)$. The contours $\Gamma^{(m)}$ thus represented might have multiple points. By referring back to Part I, it will be seen that this does not prevent the existence of a representation $t = \omega_m(\theta)$ of $\Gamma^{(m)}$ on $C$ such that the parameter $\theta$ determines a minimal surface; only this representation might be improper in that a loop of $\Gamma^{(m)}$ could correspond to a single point of $C$, for the argument of §17 breaks down when $l = 0$, and only then. The reader will readily see that the use of an improper representation $t = \omega_m(\theta)$ of $\Gamma^{(m)}$ would not at all complicate the proof which follows.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">l=0,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$t = \omega_{m}(\theta)$</span></small>

determines a minimal surface bounded by $\Gamma^{(m)}$:

$$
x _ {i} = \Re F _ {i} ^ {(m)} (w),\tag{19.5}
$$

$$
\sum_ {i = 1} ^ {n} \left[ F _ {i} ^ {(m) ^ {\prime}} (w) \right] ^ {2} = 0.
$$

Each parameter  $\theta$  of (19.4) is related to the corresponding parameter t of (19.3) by a proper topological transformation

$$
t = \omega_ {1} (\theta), \quad t = \omega_ {2} (\theta), \quad \dots , \quad t = \omega_ {m} (\theta), \quad \dots\tag{19.6}
$$

of the unit circle C (considered as  $\theta$ -locus) into itself (considered as t-locus). By adjoining a linear fractional transformation (6.1), which, according to §6, changes nothing essential in the preceding relations, we can secure that each transformation (19.6) converts three distinct fixed points  $\theta_{1}, \theta_{2}, \theta_{3}$  into three distinct fixed points  $t_{1}, t_{2}, t_{3}$ .

The sequence (19.6) is thus part of the set $\mathfrak{M}'$ ($\S 3$) of topological transformations of $C$ into itself. Since $\mathfrak{M}'$ is compact and closed, we can select from (19.6) a sub-sequence converging to a limit

$$
t = \omega (\theta),\tag{19.7}
$$

which belongs to  $M'$ , and may be proper or improper but not degenerate, since  $M'$  contains no degenerate representations. To avoid complicating the notation, we will suppose that (19.6) already represents this convergent sub-sequence, and similarly in the formulas (19.1) to (19.5).

Let the (proper or improper) representation of  $\Gamma$  derived by applying the transformation (19.7) to (19.2) be

$$
x _ {i} = g _ {i} (\theta) = f ^ {i} (\omega (\theta));\tag{19.8}
$$

then we have

$$
\lim _ {m \rightarrow \infty} g _ {i} ^ {(m)} (\theta) = g _ {i} (\theta),\tag{19.9}
$$

abstraction being made, in case the representation g is improper of the first kind, of the values of  $\theta$ , at most denumerably infinite in number, where  $g_{i}(\theta)$  is discontinuous. (19.9) rests on the fact (whose proof is trivial) that if  $f_{i}^{(m)}(t)$  tends uniformly to the continuous  $f_{i}(t)$  when  $m\to\infty$ , then if  $t_{m}\to t$  as  $m\to\infty$ , we have  $\lim f_{i}^{(m)}(t_{m})=f_{i}(t)$  for  $m\to\infty$ .

The assertion is now easily proved that if

$$
x _ {i} = \Re F _ {i} (w)\tag{19.10}
$$

are the harmonic functions determined by  $g_{i}(\theta)$ , then

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = 0,\tag{19.11}
$$

so that the surface (19.10) is minimal.

For consider (18.2) without the factor w:

$$
F _ {i} ^ {(m) ^ {\prime}} (w) = \frac {1}{2 \pi} \int_ {C} \frac {2 e ^ {i \theta}}{(e ^ {i \theta} - w) ^ {2}} g _ {i} ^ {(m)} (\theta) d \theta .\tag{19.12}
$$

Since all the polygons $\Gamma^{(m)}$ are contained in a finite region of space, the functions $g_{i}^{(m)}(\theta)$ are uniformly bounded; and if $w$ is any fixed point interior to the unit circle, the denominator $(e^{i\theta} - w)^2$ remains superior in absolute value to a fixed positive quantity when $e^{i\theta}$ describes $C$. Therefore the integrand in (19.12) remains uniformly bounded during the limit process (19.9); consequently the limit of the integral is equal to the integral of the limit:

$$
\lim _ {m \rightarrow \infty} F _ {i} ^ {(m) ^ {\prime}} (w) = F _ {i} ^ {\prime} (w).\tag{19.13}
$$

It is evident that in case g is improper of the first kind this result is not affected by the circumstance that the points of discontinuity of  $g_{i}(\theta)$  are not considered in the limit relation (19.9), since these points, being at most denumerably infinite in number, form a set of zero measure.

The result (19.11) now follows from (19.13) and the subsistence of (19.5) for every m.

20. The minimal surface is bounded by $\Gamma$. To show that the minimal surface whose existence is proved in the preceding section is bounded by $\Gamma$, we must prove that the representation (19.8) of $\Gamma$ is proper. That it cannot be improper of the second kind is proved in §18, which, being based on the relation (19.11), applies here with full validity. We cannot however apply the argument of §17 to prove that (19.8) cannot be improper of the first kind. For although we would still have for a $g$ of this kind $A(g) = +\infty$, it would not be true in the case of a general Jordan contour that $A(g)$ sometimes takes finite values.

We therefore use the following argument, based on the relation (19.11), to obtain the desired result. Suppose that under g the point P of C corresponds to the arc  $Q'Q''$  of  $\Gamma$ . Since  $\Gamma$  is a Jordan curve,  $Q'$  and  $Q''$  are distinct: and if  $a_{i}$  denote the coordinates of  $Q'$ ,  $b_{i}$  of  $Q''$ , the distance  $Q'Q''$  or l with

$$
l ^ {2} = \sum_ {i = 1} ^ {n} (b _ {i} - a _ {i}) ^ {2}\tag{20.1}
$$

is not equal to zero.

There is no loss of generality in supposing P to be at w=1, for this may be achieved by a rotation of the unit circle, which changes nothing essential.

![](images/page_42_image_1.jpg)

Let O be any point on the diameter  $P'P$  prolonged; then we define the point transformation  $M \rightarrow M'$  (Fig. 4) by the condition

$$
O M \cdot O M ^ {\prime} = O A \cdot O A ^ {\prime}.\tag{20.2}
$$

If this be combined with a reflection  $M^{\prime}\rightarrow M^{\prime\prime}$  in  $P^{\prime}P$ , the resulting transformation  $M\rightarrow M^{\prime\prime}$ , to be called T, is a conformal transformation converting the interior and circumference of the unit circle into themselves respectively. T has the linear fractional form

$$
w ^ {\prime} = \frac {a w + b}{c w + d}.\tag{20.3}
$$

Suppose $\mathfrak{G}$ to act on the functions $F_{i}(w)$ of (19.10) and on the boundary values $g_{i}(\theta)$ of $\Re F_{i}(w)$. Then $F_{i}(w)$ is transformed into

$$
G _ {i} (w) = F _ {i} \left(\frac {a w + b}{c w + d}\right),\tag{20.4}
$$

and the boundary values of $\Re G_{i}(w)$ are $h_i(\theta)$ defined by

$$
h _ {i} (A ^ {\prime \prime}) = h _ {i} (A).\tag{20.5}
$$

Differentiating (20.4), we find

$$
G _ {i} ^ {\prime} (w) = \frac {a d - b c}{(c w + d) ^ {2}} F _ {i} ^ {\prime} \left(\frac {a w + b}{c w + d}\right),
$$

whence

$$
\sum_ {i = 1} ^ {n} G _ {i} ^ {\prime 2} (w) = \frac {(a d - b c) ^ {2}}{(c w + d) ^ {4}} \sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} \left(\frac {a w + b}{c w + d}\right).
$$

Since, according to (19.11), $\sum_{i=1}^{n} F_i'^2(w) = 0$ identically in the interior of the unit circle, we have, also identically in the interior of the unit circle,

$$
\sum_ {i = 1} ^ {n} G _ {i} ^ {\prime 2} (w) = 0.\tag{20.6}
$$

Imagine now that O takes a sequence of positions tending to P as limit. Then we obtain a sequence of functions  $G_{i}(w)$  constantly obeying (20.6). Consider the boundary values  $h_{i}(\theta)$  of  $\Re G_{i}(w)$  as defined by (20.5). It is evident that if  $A''$  is any fixed point of the circumference, its image A by  $T^{-1}$  tends to P from below or above according as  $A''$  lies on the upper or lower semi-circumference  $PP'$ . Hence, on account of the distinct limiting values,  $a_{i}$  and  $b_{i}$, of  $g_{i}(\theta)$  on the different sides of P, it follows that  $h_{i}(\theta)$  tends to a function equal to the constant  $a_{i}$  on the upper semi-circumference, and to the constant  $b_{i}$  on the lower semi-circumference.

We have by (19.12)

$$
G _ {i} ^ {\prime} (w) = \frac {1}{\pi} \int_ {C} \frac {e ^ {i \theta}}{(e ^ {i \theta} - w) ^ {2}} h _ {i} (\theta) d \theta .
$$

Since  $h_{i}(\theta)$ , because it always represents  $\Gamma$ , remains uniformly bounded, we may, as in connection with (19.12), pass to the limit under the integral sign; and so find that with the approach of O to P,

$$
\begin{array}{r l}G _ {i} ^ {\prime} (w)&\rightarrow \frac {1}{\pi} \int_ {0} ^ {\pi} \frac {e ^ {i \theta}}{(e ^ {i \theta} - w) ^ {2}} a _ {i} d \theta + \frac {1}{\pi} \int_ {\pi} ^ {2 \pi} \frac {e ^ {i \theta}}{(e ^ {i \theta} - w) ^ {2}} b _ {i} d \theta\\&= \frac {2 i (b _ {i} - a _ {i})}{\pi}. \frac {1}{1 - w ^ {2}}.\end{array}
$$

Hence, with the notation (20.1),

$$
\sum_ {i = 1} ^ {n} G _ {i} ^ {\prime 2} (w) \rightarrow \frac {- 4 l ^ {2}}{\pi^ {2}} \cdot \frac {1}{(1 - w ^ {2}) ^ {2}}.\tag{20.7}
$$

Here we have contradiction, for since  $l \neq 0$ , the last condition is incompatible with the fact that in the passage to the limit (20.6) is constantly obeyed.

Hence the representation  $x_{i}=g_{i}(\theta)$  of  $\Gamma$  is proper, and the minimal surface determined by it is bounded by  $\Gamma$ .

## III. THE RELATION OF  $A(g)$  TO THE AREA FUNCTIONAL

It is customary to characterize a minimal surface by the property of rendering area a minimum. Instead, we have minimized the simpler functional  $A(g)$ . This leads to the question of the relationship between these two functionals, with which this Part is occupied. We shall develop certain formulas interesting in themselves, and useful in Parts IV and V. The reader who is interested in the application of the present theory to conformal mapping and in the proof of the least-area property of the minimal surface whose existence has just been established may go on at once to Parts IV and V, referring back to this Part for the necessary results.

21. Other forms of $A(g)$. In this section we derive two further formulas for $A(g)$. The first of these is

$$
A (g) = \iint_ {D} \frac {1}{2} \sum_ {i = 1} ^ {n} | F _ {i} ^ {\prime} (w) | ^ {2} d \sigma ,\tag{21.1}
$$

where D denotes the interior of the unit circle, of which  $d\sigma$  is the element of area. The second expresses  $A(g)$  in terms of the Fourier coefficients of g:

$$
A (g) = \frac {\pi}{2} \sum_ {m = 1} ^ {\infty} m \sum_ {i = 1} ^ {n} \left(a _ {i m} ^ {2} + b _ {i m} ^ {2}\right).\tag{21.2}
$$

Proof of (21.1). Since the integrand of (21.1) may not be bounded in D, we need the following limit process to define the double integral. Let  $D_{\rho}$  denote the interior of the circle  $C_{\rho}$  of radius  $\rho < 1$  concentric with C. Then

$$
\iint_ {D _ {\rho}} \frac {1}{2} \sum_ {i = 1} ^ {n} \left| F _ {i} ^ {\prime} (w) \right| ^ {2} d \sigma
$$

is evidently an increasing function of  $\rho$ , since the element of integration is positive. Hence the limit as  $\rho\to1$  of this double integral exists, finite or infinite, and we define

$$
\iint_ {D} \frac {1}{2} \sum_ {i = 1} ^ {n} | F _ {i} ^ {\prime} (w) | ^ {2} d \sigma = \lim _ {\rho \rightarrow 1} \iint_ {D _ {\rho}} \frac {1}{2} \sum_ {i = 1} ^ {n} | F _ {i} ^ {\prime} (w) | ^ {2} d \sigma .\tag{21.3}
$$

Suppose $F_{i}(w)$ separated into its real and imaginary parts:

$$
F _ {i} (w) = U _ {i} (u, v) + i V _ {i} (u, v) \quad (w = u + i v).
$$

Then

$$
F _ {i} ^ {\prime} (w) = \frac {\partial U _ {i}}{\partial u} - i \frac {\partial U _ {i}}{\partial v}.\tag{21.4}
$$

Therefore

$$
\sum_ {i = 1} ^ {n} \left| F _ {i} ^ {\prime} (w) \right| ^ {2} = \sum_ {i = 1} ^ {n} \left[ \left(\frac {\partial U _ {i}}{\partial u}\right) ^ {2} + \left(\frac {\partial U _ {i}}{\partial v}\right) ^ {2} \right].\tag{21.5}
$$

Since $U_{i}$ is a harmonic function, we have by Green's formula†

$$
\iint_ {D _ {\rho}} \left[ \left(\frac {\partial U _ {i}}{\partial u}\right) ^ {2} + \left(\frac {\partial U _ {i}}{\partial v}\right) ^ {2} \right] d \sigma = \int_ {C _ {\rho}} U _ {i} \frac {\partial U _ {i}}{\partial \rho} d s.
$$

Whence, applying (21.5),

$$
\iint_ {D _ {\rho}} \frac {1}{2} \sum_ {i = 1} ^ {n} \left| F _ {i} ^ {\prime} (w) \right| ^ {2} d \sigma = \frac {1}{2} \int_ {0} ^ {2 \pi} \sum_ {i = 1} ^ {n} U _ {i} \frac {\partial U _ {i}}{\partial \rho} \rho d \theta .\tag{21.6}
$$

For  $U_{i}$  there is the formula

$$
U _ {i} = \frac {a _ {i 0}}{2} + \sum_ {p = 1} ^ {\infty} \rho^ {p} (a _ {i p} \cos p \theta + b _ {i p} \sin p \theta),\tag{21.7}
$$

derived by taking the real part of (11.1) after writing  $w = \rho e^{i\theta}$ . This series is uniformly convergent for all  $\theta$  and for  $\rho \leq \rho_{0}$ , with  $\rho_{0}$  fixed and <1. This observation makes it legitimate to perform term by term the operations of differentiation, multiplication and integration indicated in the second member of (21.6). We get first

$$
\rho \frac {\partial U _ {i}}{\partial \rho} = \sum_ {q = 1} ^ {\infty} q \rho^ {q} (a _ {i q} \cos q \theta + b _ {i q} \sin q \theta),\tag{21.8}
$$

and then, observing the relations

$$
\int_ {0} ^ {2 \pi} \cos p \theta \sin q \theta d \theta = 0, \int_ {0} ^ {2 \pi} \cos p \theta \cos q \theta d \theta = \int_ {0} ^ {2 \pi} \sin p \theta \sin q \theta d \theta = \left\{ \begin{array}{l l} \pi & \text { if } p = q, \\ 0 & \text { if } p \neq q, \end{array} \right.
$$

we obtain from (21.6), (21.7), (21.8):

$$
\iint_ {D _ {\rho}} \frac {1}{2} \sum_ {i = 1} ^ {n} \left| F _ {i} ^ {\prime} (w) \right| ^ {2} d \sigma = \frac {\pi}{2} \sum_ {m = 1} ^ {\infty} m \rho^ {2 m} \sum_ {i = 1} ^ {n} \left(a _ {i m} ^ {2} + b _ {i m} ^ {2}\right).\tag{21.9}
$$

This infinite series may be expressed as a double integral (formula (21.12)) in the following way. From the expressions (11.2) of the Fourier coefficients we easily derive in a manner analogous to (11.9):‡

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† See Picard, Traité d'Analyse, vol. 2 (3d edition, Paris, 1925), p. 22.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ Cf. Picard, Traité d'Analyse, vol. 1 (3d edition, Paris, 1922), p. 341.</span></small>

(21.11)

$$
\begin{array}{l} m \rho^ {2 m} \sum_ {i = 1} ^ {n} (a _ {i m} ^ {2} + b _ {i m} ^ {2}) \\ = - \frac {1}{2 \pi^ {2}} \int_ {0} ^ {2 \pi} \int_ {0} ^ {2 \pi} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \cdot m \rho^ {2 m} \cos m (\theta - \phi) d \theta d \phi . \end{array}\tag{21.10}
$$

Now by writing

$$
z = \rho^ {2} e ^ {i (\theta - \phi)}
$$

in the formula

$$
\sum_ {m = 1} ^ {\infty} m z ^ {m} = \frac {z}{(1 - z) ^ {2}}
$$

and taking real parts, we obtain after some reduction

$$
\sum_ {m = 1} ^ {\infty} m \rho^ {2 m} \cos m (\theta - \phi) = - \rho^ {2} \frac {(1 + \rho^ {2}) ^ {2} \sin^ {2} \frac {\theta - \phi}{2} - (1 - \rho^ {2}) ^ {2} \cos^ {2} \frac {\theta - \phi}{2}}{\left[ (1 + \rho^ {2}) ^ {2} \sin^ {2} \frac {\theta - \phi}{2} + (1 - \rho^ {2}) ^ {2} \cos^ {2} \frac {\theta - \phi}{2} \right] ^ {2}}.
$$

The convergence, moreover, is uniform for all  $\theta$ ,  $\phi$  if  $\rho$  be regarded as fixed <1, since the convergent series of constant positive terms

$$
\sum_ {m = 1} ^ {\infty} m \rho^ {2 m}
$$

is majorant for (21.11). Hence, after multiplying (21.11) by the bounded factor

$$
- \frac {1}{2 \pi^ {2}} \sum_ {i = 1} ^ {m} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2},
$$

which does not disturb the uniform convergence, we may integrate term by term, and get, with attention to (21.10), (21.9),

$$
\begin{array}{r l} \iint_ {D _ {\rho}} \frac {1}{2} & \sum_ {i = 1} ^ {n} | F _ {i} ^ {\prime} (w) | ^ {2} d \sigma \\ & = \frac {1}{4 \pi} \int_ {0} ^ {2 \pi} \int_ {0} ^ {2 \pi} \sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2} \rho^ {2} \\ & \cdot \frac {(1 + \rho^ {2}) ^ {2} \sin^ {2} \frac {\theta - \phi}{2} - (1 - \rho^ {2}) ^ {2} \cos^ {2} \frac {\theta - \phi}{2}}{\left[ (1 + \rho^ {2}) ^ {2} \sin^ {2} \frac {\theta - \phi}{2} + (1 - \rho^ {2}) ^ {2} \cos^ {2} \frac {\theta - \phi}{2} \right] ^ {2}} d \theta d \phi . \end{array}\tag{21.12}
$$

If in the last expression we write formally $\rho = 1$, there results

$$
\frac {1}{4 \pi} \int_ {0} ^ {2 \pi} \int_ {0} ^ {2 \pi} \frac {\sum_ {i = 1} ^ {n} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2}}{4 \sin^ {2} \frac {\theta - \phi}{2}} d \theta d \phi = A (g).\tag{21.13}
$$

To prove that (21.13) is the limit of (21.12) when  $\rho\to1$ , we first observe that if the second member of (21.12) and the first of (21.13) be abbreviated respectively as

$$
\frac {1}{4 \pi} \iint J (\rho ; \theta , \phi) d \theta d \phi , \quad \frac {1}{4 \pi} \iint I (\theta , \phi) d \theta d \phi ,
$$

then for all $\rho$ and $\theta \neq \phi$

(21.14)

$$
\left| J (\rho ; \theta , \phi) \right| <   I (\theta , \phi),
$$

since the ratio

$$
\begin{array}{r l} \frac {\left| J (\rho ; \theta , \phi) \right|}{I (\theta , \phi)} & = \frac {4 \rho^ {2} \sin^ {2} \frac {\theta - \phi}{2}}{(1 + \rho^ {2}) ^ {2} \sin^ {2} \frac {\theta - \phi}{2} + (1 - \rho^ {2}) ^ {2} \cos^ {2} \frac {\theta - \phi}{2}} \\ & \cdot \frac {\left| (1 + \rho^ {2}) ^ {2} \sin^ {2} \frac {\theta - \phi}{2} - (1 - \rho^ {2}) ^ {2} \cos^ {2} \frac {\theta - \phi}{2} \right|}{(1 + \rho^ {2}) ^ {2} \sin^ {2} \frac {\theta - \phi}{2} + (1 - \rho^ {2}) ^ {2} \cos^ {2} \frac {\theta - \phi}{2}} \end{array}
$$

is less than 1 (each denominator minus the corresponding numerator gives a positive quantity).

Suppose, as first case, that $A(g)$ is finite. Then (21.14) expresses that in the approach of $\rho$ to 1 the absolute value of $J(\rho; \theta, \phi)$ remains less than a summable function, and hence a theorem of Lebesgue† permits us to pass to the limit under the integral sign:

$$
\lim _ {\rho \rightarrow 1} \iint J (\rho ; \theta , \phi) d \theta d \phi = \iint I (\theta , \phi) d \theta d \phi ,
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Lebesgue, Leçons sur l'Intégration (2d edition, Paris, 1928), p. 131. In the present case all the functions involved are Riemann integrable (proper or improper), and the result in question may easily be established without recourse to the notion of Lebesgue integral.</span></small>

that is,

$$
\begin{array}{l l}\lim _ {\rho \rightarrow 1}&\iint_ {D _ {\rho}} \frac {1}{2} \sum_ {i = 1} ^ {n} | F _ {i} ^ {\prime} (w) | ^ {2} d \sigma\\\equiv&\iint_ {D} \frac {1}{2} \sum_ {i = 1} ^ {n} | F _ {i} ^ {\prime} (w) | ^ {2} d \sigma = A (g).\end{array}\tag{21.15}
$$

Thus (21.1) is proved in the case $A(g)$ finite. If $A(g) = +\infty$, a simple way of seeing that the $\iint_{D}$ is then also $= +\infty$ is to observe that $\iint_{D}$, as the limit of $\iint_{D\rho}$ which tends to it in increasing, is a lower semi-continuous functional of $g$, like $A(g)$. This remains true if $g$ is not restricted to represent $\Gamma$ but may be any parameterized contour. With this understanding, a $g$ such that $A(g) = +\infty$ may always be approached by a sequence of $g$'s such that $A(g)$ is finite. It is to be seen immediately that two lower semi-continuous functionals which coincide whenever the first has a finite value must also coincide in case this value is $+\infty$.

Proof of (21.2). Returning to (21.4) and (21.9), we have

$$
\iint_ {D} \frac {1}{2} \sum_ {i = 1} ^ {n} | F _ {i} ^ {\prime} (w) | ^ {2} = \lim _ {\rho \rightarrow 1} \frac {\pi}{2} \sum_ {m = 1} ^ {\infty} m \rho^ {2 m} \sum_ {i = 1} ^ {n} \left(a _ {i m} ^ {2} + b _ {i m} ^ {2}\right).
$$

Now

$$
\lim _ {\rho \rightarrow 1} \frac {\pi}{2} \sum_ {m = 1} ^ {\infty} m \rho^ {2 m} \sum_ {i = 1} ^ {n} (a _ {i m} ^ {2} + b _ {i m} ^ {2}) = \frac {\pi}{2} \sum_ {m = 1} ^ {\infty} m \sum_ {i = 1} ^ {n} (a _ {i m} ^ {2} + b _ {i m} ^ {2}).
$$

If the latter series is convergent, the justification for this is Abel's theorem asserting the continuity of the power series in the first member at the point of convergence $\rho = 1$. If the second member equals $+\infty$, it is easy to show, by taking account of the positive nature of all the terms, that this is also the value of the first member.

Combining the last two equations with (21.1), we have the desired result:

$$
A (g) = \frac {\pi}{2} \sum_ {m = 1} ^ {\infty} m \sum_ {i = 1} ^ {n} \left(a _ {i m} ^ {2} + b _ {i m} ^ {2}\right).
$$

22. The area functional  $S(g)$  and its relation to  $A(g)$ . We have seen how every representation g of  $\Gamma$  determines a harmonic surface

$$
x _ {i} = \Re F _ {i} (w) = U _ {i} (u, v).
$$

The linear element of this surface is

$$
d s ^ {2} = E d u ^ {2} + 2 F d u d v + G d v ^ {2}
$$

with

$$
E = \sum_ {i = 1} ^ {n} \left(\frac {\partial U _ {i}}{\partial u}\right) ^ {2}, F = \sum_ {i = 1} ^ {n} \frac {\partial U _ {i}}{\partial u} \frac {\partial U _ {i}}{\partial v}, G = \sum_ {i = 1} ^ {n} \left(\frac {\partial U _ {i}}{\partial v}\right) ^ {2},\tag{22.1}
$$

and its area is a functional of g which we denote by  $S(g)$ :

$$
S (g) = \iint_ {D} (E G - F ^ {2}) ^ {1 / 2} d \sigma .\tag{22.2}
$$

We have from (21.5)

$$
\sum_ {i = 1} ^ {n} \left| F _ {i} ^ {\prime} (w) \right| ^ {2} = \sum_ {i = 1} ^ {n} \left(\frac {\partial U _ {i}}{\partial u}\right) ^ {2} + \sum_ {i = 1} ^ {n} \left(\frac {\partial U _ {i}}{\partial v}\right) ^ {2} = E + G,
$$

so that by (21.1)

$$
A (g) = \iint_ {D} \frac {1}{2} (E + G) d \sigma .\tag{22.3}
$$

To the end of comparing the integrands in (22.2), (22.3), we observe

$$
\frac {1}{4} (E + G) ^ {2} - (E G - F ^ {2}) = \frac {1}{4} (E - G) ^ {2} + F ^ {2} \geq 0;
$$

therefore

$$
\frac {1}{2} (E + G) \geq (E G - F ^ {2}) ^ {1 / 2},\tag{22.4}
$$

the equality holding when and only when

$$
E - G = 0, F = 0.\tag{22.5}
$$

Since by (21.4) and (22.1),

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = (E - G) - 2 i F,
$$

the conditions (22.5) are equivalent to

$$
\sum_ {i = 1} ^ {n} F _ {i} ^ {\prime 2} (w) = 0,\tag{22.6}
$$

characteristic of a minimal surface.

Consequently,

$$
A (g) \geq S (g),\tag{22.7}
$$

and the equality holds when and only when the harmonic surface determined by g is minimal.

$$
\begin{array}{l} \text {IV. THE RIEMANN MAPPING THEOREM AND THE THEOREM} \\ \text {OF OSGOOD AND CARATHÉODORY} \end{array}
$$

23. The case n=2 of the problem of Plateau. Let the contour  $\Gamma$  be any Jordan curve in the plane  $(x_{1}, x_{2})$ ,  $\Delta$  the region bounded by  $\Gamma$ , C the unit

circle, and D the interior of the unit circle. Then the classic Riemann mapping theorem states the existence of a one-one continuous and conformal correspondence between D and  $\Delta$ . According to a theorem of Osgood† and Carathéodory,† it is possible to supplement this conformal map with a one-one continuous correspondence between C and  $\Gamma$ , so that the combination is one-one and continuous between  $D+C$  and  $\Delta+\Gamma$ .

We show in this Part how by merely writing n=2 in the preceding work we have an immediate proof of the theorem of Riemann together with the theorem of Osgood-Carathéodory.

In the cited papers of the last two authors a sharp distinction is drawn between the “interior problem” and the “boundary problem.” The existence of a conformal map of the interiors is supposed already established by the classic methods, and these authors then proceed to prove that this map of the interiors induces by continuity a topological correspondence between the boundaries.

It is characteristic of the method of the present paper to follow a directly opposite procedure: namely, we first distinguish a certain topological correspondence between the boundaries by the property of rendering  $A(g)$  a minimum; this topological correspondence found, the conformal map of the interiors can be expressed immediately (see the theorem stated at the end of this Part).

The work of Parts I and II, with n=2, assures us of the existence of a certain proper representation of  $\Gamma$ ,

$$
x _ {1} = g _ {1} ^ {*} (\theta), x _ {2} = g _ {2} ^ {*} (\theta),\tag{23.1}
$$

such that if

$$
x _ {1} = \Re F _ {1} (w), x _ {2} = \Re F _ {2} (w)\tag{23.2}
$$

are the harmonic functions determined by the boundary values (23.1), we have

$$
F _ {1} ^ {\prime 2} (w) + F _ {2} ^ {\prime 2} (w) = 0.\tag{23.3}
$$

The functions $F_{1}, F_{2}$ are given by the formula

$$
F _ {1} (w) = \frac {1}{2 \pi} \int_ {C} \frac {e ^ {i \theta} + w}{e ^ {i \theta} - w} g _ {1} ^ {*} (\theta) d \theta , F _ {2} (w) = \frac {1}{2 \pi} \int_ {C} \frac {e ^ {i \theta} + w}{e ^ {i \theta} - w} g _ {2} ^ {*} (\theta) d \theta .\tag{23.4}
$$

From (23.3),

$$
F _ {1} ^ {\prime} (w) = \pm i F _ {2} ^ {\prime} (w),
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Reference in the Introduction.</span></small>

and choosing the + sign (the - sign will lead to an inversely conformal transformation, easily discussed), we have by integration

$$
F _ {1} (w) = i F _ {2} (w) + a + i b
$$

where $a, b$ are real constants. Separating $F_{1}, F_{2}$ into their real and imaginary parts:

$$
F _ {1} = U _ {1} + i V _ {1}, \quad F _ {2} = U _ {2} + i V _ {2},
$$

this gives

$$
U _ {1} = - V _ {2} + a, \quad V _ {1} = U _ {2} + b.
$$

Consequently,

$$
x _ {1} + i x _ {2} = U _ {1} + i U _ {2} = U _ {1} + i V _ {1} - i b = F _ {1} (w) - i b = i F _ {2} (w) + a.
$$

Denote by  $F(w)$  the common value of the last two expressions:

$$
F (w) = F _ {1} (w) - i b, F (w) = i F _ {2} (w) + a;\tag{23.5}
$$

then

$$
x _ {1} + i x _ {2} \equiv W = F (w),\tag{23.6}
$$

a holomorphic function of w in the interior D of the unit circle. It will therefore be proved that the transformation defined by (23.6) or (23.2) is conformal in the domain D after we have shown a little later that  $F'(w) \neq 0$  at any point of D.

We will first prove that (23.6) maps D in a one-one way on  $\Delta$ . To this end, let  $W_{0}$  be any point in the complex plane  $x_{1} + ix_{2} \equiv W$  not on  $\Gamma$ ; what has to be shown is that the equation

$$
F (w) \dot {=} W _ {0}\tag{23.7}
$$

has exactly one solution w in D if  $W_{0}$  belongs to  $\Delta$ , and no solution w in D if  $W_{0}$  does not belong to  $\Delta$ .

Certainly there are only a finite number of solutions of (23.7) in any circle concentric with and smaller than C; therefore we can construct a sequence of circles  $C_{\rho}$  concentric with C and with radii  $\rho$  increasing to 1 as limit, such that no solution of (23.7) lies on a circumference  $C_{\rho}$ . The number of solutions of (23.7) in the interior of  $C_{\rho}$  is given by the formula of Cauchy:

$$
N _ {\rho} = \frac {1}{2 \pi i} \int_ {C _ {\rho}} \frac {F ^ {\prime} (w) d w}{F (w) - W _ {0}},\tag{23.8}
$$

applicable here with full validity because  $C_{\rho}$  is interior to a simply connected domain of regularity of  $F(w)$ . The number of solutions of (23.7) in the interior of C is evidently

$$
N = \lim _ {\rho \rightarrow 1} N _ {\rho}.\tag{23.9}
$$

With $W = F(w)$, formula (23.8) gives

$$
N _ {\rho} = \frac {1}{2 \pi i} [ \log (W - W _ {0}) ] _ {\Gamma_ {\rho}} = \text { order   of } W _ {0} \text { with   respect   to } \Gamma_ {\rho}.\tag{23.10}
$$

Here $\Gamma_{\rho}$ denotes the closed analytic curve† which is the image of $C_{\rho}$ by the transformation $W = F(w)$, the bracket denotes the variation of $\log (W - W_0)$ when $W$ describes $\Gamma_{\rho}$, and the order of $W_0$ with respect to $\Gamma_{\rho}$ is an integer equal to $1/(2\pi)$ times the variation in the angle made by the vector $W_0W$ with a fixed direction, followed continuously while $W$ describes $\Gamma_{\rho}$.

Now when $\rho\to1$, $\Gamma_{\rho}$ tends uniformly to $\Gamma$, for the formulas (23.2), (23.4) are equivalent to Poisson's integral, and the boundary functions (23.1) are continuous. Evidently then, the order of $W_{0}$ with respect to $\Gamma_{\rho}$ tends to the order of $W_{0}$ with respect to $\Gamma$; indeed, for $\rho$ near enough to 1 the former remains equal to the latter. Hence by (23.9), (23.10),

(23.11) $N =$ order of $W_{0}$ with respect to $\Gamma = \left\{ \begin{array}{ll}1$ if $W_{0}$ is interior to $\Gamma ,$ 0 if $W_{0}$ is exterior to $\Gamma .$

According to this, the image of a point w of D is never a point exterior to  $\Gamma$ . But neither can it be a point Q of  $\Gamma$ . For then a neighborhood of w would go over into a neighborhood of  $Q; \ddagger$  now every neighborhood of Q contains points exterior to  $\Gamma$ , so that we would have contradiction with the first statement of this paragraph. Hence the image of any point w of D is a point interior to  $\Gamma$ . Furthermore, by (23.11) every point interior to  $\Gamma$  is obtained, and exactly once, as image of a point w. Therefore the transformation  $W = F(w)$  is one-one as between D and  $\Delta$ .

To prove that this transformation is conformal without singular points, we must show that we cannot have  $F'(w)=0$  at any point w of D. If  $F'(w)=0$ , then a neighborhood of w is mapped on a multiply-covered neighborhood of W,§ but this contradicts the proof just given of the one-one nature of the correspondence between D and  $\Delta$ .

That the conformal correspondence thus established between D and  $\Delta$  attaches continuously to the topological correspondence (23.1) between C and  $\Gamma$  is an immediate consequence of the remark, already made, that the

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\Gamma_{\rho}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† It will result from the sequel that $\Gamma_{\rho}$ does not intersect itself but this fact is not necessary for the present argument.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$W = F(w)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\dagger$ This is by the region-preserving property (Gebietstreu) of transformations $W = F(w)$; cf. L. Bieberbach, Lehrbuch der Funktionentheorie, Leipzig and Berlin, 1921, pp. 187–188.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ Bieberbach, loc. cit., p. 188.</span></small>

formulas (23.2), (23.4) are equivalent to Poisson's integral based on the continuous boundary functions (23.1).

In sum, we have proved the combined theorems of Riemann and Osgood-Carathéodory.

Expression for  $F(w)$ . An expression for  $F(w)$  in the Cauchy form, more elegant than (23.2), (23.4), where real and imaginary parts are separated, may be obtained as follows.

Let $w$ be a fixed point of $D$; take $\rho > |w|$ and $< 1$; then by the formula of Cauchy,

$$
F (w) = \frac {1}{2 \pi i} \int_ {C _ {\rho}} \frac {F (z) d z}{z - w}.
$$

If now $\rho \to 1$, then $F(z)$ tends uniformly to

$$
f ^ {*} (z) = g _ {1} ^ {*} (\theta) + i g _ {2} ^ {*} (\theta)
$$

and  $1/(z-w)$  (z on  $C_{\rho}$ ) tends uniformly to  $1/(z-w)$  (z on C), wherein corresponding points on  $C_{\rho}$  and C are those with the same angular coordinate. Therefore

$$
F (w) = \frac {1}{2 \pi i} \int_ {C} \frac {f ^ {*} (z) d z}{z - w}.\tag{23.12}
$$

24. Range of values of  $A(g)$ . For a Jordan curve in the plane, we can easily obtain the exact range of values of  $A(g)$ , and see that finite values always occur among them.

For since the functions  $F_{1}(w)$ ,  $F_{2}(w)$  determined by the representation  $g^{*}$  (23.1) obey the condition (23.3)  $F_{1}^{\prime2}(w)+F_{2}^{\prime2}(w)=0$ , we have by the final statement of Part III:

$$
A (g ^ {*}) = \text { inner   area   of } \Gamma .
$$

The inner area† must be taken because $S(g)$, as defined by (22.2), is the limit of the area bounded by $\Gamma_{\rho}$, which approaches to $\Gamma$ from its interior.

To see that  $A(g)$  takes every value in the interval

$$
\text { inner   area   of } \Gamma \leq A (g) \leq + \infty
$$

(and, of course, no other values), consider a continuous series of representations $g$ connecting $g^*$ with a representation $g^0$ such that $A(g^0) = +\infty$ (example: $g^0$ improper of the first kind); it is easy to arrange that $A(g)$ be continuous on this series of $g$'s.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† The region bounded by a Jordan curve has in general distinct inner and outer areas, differing by an amount called the exterior content of the curve. The first example of a Jordan curve of positive exterior content was given by Osgood, these Transactions, vol. 4 (1903), pp. 107–112.</span></small>

25. The combined interior-boundary conformal mapping theorem. The results of this Part are summarized in the following theorem, combining the theorems of Riemann and Osgood-Carathéodory.

THEOREM. Let $\Gamma$ denote any Jordan curve in the plane, and

$$
x _ {1} = g _ {1} (\theta), x _ {2} = g _ {2} (\theta),
$$

or

$$
Z = f (z)
$$

with

$$
Z = x _ {1} + i x _ {2}, z = e ^ {i \theta},
$$

an arbitrary representation of  $\Gamma$  as topological image of the unit circle C.

The range of values of the functional

$$
\begin{array}{r l} A (g) & = \frac {1}{1 6 \pi} \int_ {c} \int_ {c} \frac {\sum_ {i = 1} ^ {2} [ g _ {i} (\theta) - g _ {i} (\phi) ] ^ {2}}{\sin^ {2} \frac {\theta - \phi}{2}} d \theta d \phi \\ & = \frac {1}{4 \pi} \int_ {c} \int_ {c} \frac {| f (z) - f (\zeta) | ^ {2}}{| z - \zeta | ^ {2}} | d z | | d \zeta | \end{array}
$$

when g or f varies over all possible representations of  $\Gamma$  consists of all positive real numbers (including  $+\infty$ ) greater than or equal to the inner area of the region enclosed by  $\Gamma$ . This minimum value is attained for a certain proper representation

$$
Z = f ^ {*} (z)
$$

(determined up to linear fractional transformation of $C$ into itself,

$$
z ^ {\prime} = (a z + b) / (\bar {b} z + \bar {a}).
$$

Then the transformation $w \to W$ defined by

$$
W = \frac {1}{2 \pi i} \int_ {C} \frac {f ^ {*} (z) d z}{z - w}
$$

produces a one-one, continuous and conformal map of the interior of  $\Gamma$  on the interior of C, which attaches continuously to the topological correspondence  $Z=f^{*}(z)$  between  $\Gamma$  and C.

The implications of this theorem for the Dirichlet problem are apparent. The Dirichlet problem for any continuous distribution of assigned values on a Jordan boundary is reduced to the same problem for a circle, and therefore solved by Poisson's integral. The Dirichlet functional

$$
D (\phi) = \iint_ {\Delta} \left[ \left(\frac {\partial \phi}{\partial x _ {1}}\right) ^ {2} + \left(\frac {\partial \phi}{\partial x _ {2}}\right) ^ {2} \right] d x _ {1} d x _ {2}
$$

is replaced by the functional  $A(g)$ , much simpler to deal with chiefly because the range of g is a compact closed set while the range of  $\phi$  is not. It was the latter fact alone which rendered valid the criticism of Weierstrass against Riemann's treatment of the Dirichlet problem based on minimizing the Dirichlet functional.

## V. ABSOLUTE MINIMUM OF AREA

26. Proof of the least-area property. We conclude this paper with the following brief proof, based on the formulas of Part III, that the minimal surface whose existence is proved in Part I has the least area of any surface bounded by the given contour.

Let the contour $\Gamma$ be, first, a polygon. Then let $\Pi$ be any polyhedral surface bounded by $\Gamma$. By the conformal mapping theorem of Koebe,$\dagger$$\Pi$ can be mapped conformally on the interior of the unit circle, the map attaching continuously to a topological correspondence between $\Gamma$ and the circumference. Let the parametric equations of $\Pi$ determined by this map be

$$
x _ {i} = x _ {i} (u, v)
$$

and of $\Gamma$

$$
x _ {i} = g _ {i} (\theta).\tag{26.1}
$$

The element of length of $\Pi$ is

$$
d s ^ {2} = E d u ^ {2} + 2 F d u d v + G d v ^ {2}
$$

with

$$
E = \sum_ {i = 1} ^ {n} \left(\frac {\partial x _ {i}}{\partial u}\right) ^ {2}, \quad F = \sum_ {i = 1} ^ {n} \left(\frac {\partial x _ {i}}{\partial u}\right) \left(\frac {\partial x _ {i}}{\partial v}\right), \quad G = \sum_ {i = 1} ^ {n} \left(\frac {\partial x _ {i}}{\partial v}\right) ^ {2};
$$

and by the conformality

$$
E = G, \quad F = 0;
$$

so that the area of $\Pi$ is

$$
\begin{array}{r l} S (\Pi) & = \iint (E G - F ^ {2}) ^ {1 / 2} d u d v = \frac {1}{2} \iint (E + G) d u d v \\ & = \frac {1}{2} \sum_ {i = 1} ^ {n} \iint \left\{\left(\frac {\partial x _ {i}}{\partial u}\right) ^ {2} + \left(\frac {\partial x _ {i}}{\partial v}\right) ^ {2} \right\} d u d v. \end{array}\tag{26.2}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Cf. T. Radó, Annals of Mathematics, (2), vol. 31 (1930), pp. 458–460.</span></small>

Consider the harmonic surface determined by the representation (26.1) of  $\Gamma$ , and denote by  $\overline{E}$ ,  $\overline{F}$ ,  $\overline{G}$  its fundamental quantities; then since a harmonic function gives the least value to the Dirichlet functional for fixed boundary values, we have

$$
\frac {1}{2} \iint (\overline {{{E}}} + \overline {{{G}}}) d u d v \leq \frac {1}{2} \iint (E + G) d u d v.\tag{26.3}
$$

By formula (22.3) of Part III,

$$
A (g) = \frac {1}{2} \iint (\overline {{{E}}} + \overline {{{G}}}) d u d v;\tag{26.4}
$$

and by the minimum property of  $g^{*}$ ,

$$
A (g ^ {*}) \leq A (g).\tag{26.5}
$$

By the chain (26.2)-(26.5),

$$
A (g ^ {*}) \leq S (\Pi):\tag{26.6}
$$

the minimum value of  $A(g) \leq$  the area of any polyhedral surface bounded by the polygon  $\Gamma$ .

Let now  $\Gamma$  denote an arbitrary Jordan curve and  $\Sigma$  any simply-connected surface bounded by  $\Gamma$ . According to the Lebesgue definition, the area  $S(\Sigma)$  of  $\Sigma$  is the lower limit (finite or  $+\infty$ ) of the areas of polyhedral surfaces which tend to  $\Sigma$ . There exists, then, a sequence of polyhedral surfaces  $\Pi_{m}$  tending to  $\Sigma$  such that

$$
S (\Pi_ {m}) \rightarrow S (\Sigma);\tag{26.7}
$$

the bounding polygons  $\Gamma^{(m)}$  tend to  $\Gamma$ .

Each polygon $\Gamma^{(m)}$ has a representation

$$
x _ {i} = g _ {i} ^ {(m *)} (\theta)\tag{26.8}
$$

minimizing $A(g)$ for that polygon, and by the procedure of §19 we can select a sub-sequence

$$
m = m _ {1}, m _ {2}, \dots , m _ {k}, \dots\tag{26.9}
$$

so that (26.8) tends to a proper representation. of $\Gamma$

$$
x _ {i} = g _ {i} ^ {*} (\theta).\tag{26.10}
$$

The harmonic surface determined by  $g^{*}$  will be minimal; consequently, by (22.7),

$$
S (g ^ {*}) = A (g ^ {*}).\tag{26.11}
$$

From the sequence (26.9) we can in turn select a sub-sequence

$$
m = m _ {1} ^ {\prime}, m _ {2} ^ {\prime}, \dots , m _ {k} ^ {\prime}, \dots\tag{26.12}
$$

so that $A(g^{(m)*})$ tends to a limit (finite or $+\infty$):

$$
A \left(g ^ {(m) *}\right)\rightarrow L.\tag{26.13}
$$

By the lower semi-continuity of  $A(g)$ , which holds for any sort of approach of one parameterized contour to another, as well when the contour itself is allowed to vary as when we have merely different parameterizations of the same contour, it follows (see (7.2)) that

$$
A (g ^ {*}) \leq L.\tag{26.14}
$$

By (26.6),

$$
A \left(g ^ {(m) *}\right) \leq S (\Pi_ {m});
$$

hence

$$
\lim A \left(g ^ {(m) *}\right) \leq \lim S (\Pi_ {m}),
$$

that is

$$
L \leq S (\Sigma).\tag{26.15}
$$

Combining this with (26.14) and (26.11), we obtain

$$
S (g ^ {*}) \leq S (\Sigma),\tag{26.16}
$$

which was to be proved.

It is easy to see that the  $g^{*}$  here obtained from approaching polygons is the same as the  $g^{*}$  which minimizes  $A(g)$  for  $\Gamma$ . For let  $g^{**}$  minimize  $A(g)$  for  $\Gamma$ ; then

$$
A (g ^ {* *}) \leq A (g ^ {*}).\tag{26.17}
$$

By (26.16),

$$
S (g ^ {*}) \leq S (g ^ {* *}),\tag{26.18}
$$

and by (22.7)

$$
A (g ^ {* *}) = S (g ^ {* *}) \text {   as   well   as   } A (g ^ {*}) = S (g ^ {*}),
$$

so that (26.18) may be expressed as

$$
A (g ^ {*}) \leq A (g ^ {* *}).\tag{26.19}
$$

From (26.19) and (26.17) it follows that

$$
A (g ^ {*}) = A (g ^ {* *}).
$$

27. A non-finite-area-spanning Jordan contour. It is important to note that if the Jordan contour is sufficiently tortuous, the least-area property of the minimal surface may become vacuous through the impossibility of spanning any finite area whatever within the given contour. The following example was constructed by the author in collaboration with P. Franklin.

Consider a broken line, broken at right angles and in the form of a spiral, whose successive segments have the lengths 1, $1/2^{1/2}$, $1/3^{1/2}$, $\cdots$. On each segment construct a square lying towards the outside of the spiral. In each square let there be a Peano curve starting at the initial point and ending at the terminal point of the corresponding segment. Let the unit interval $0 \leq t \leq 1$ be divided by the points $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \cdots$ into a denumerable infinity of sub-intervals, and let the $n$th Peano curve be represented as continuous image of the $n$th interval. If to the equations $x = \phi(t)$, $y = \psi(t)$, representing all these Peano curves laid end to end, we adjoin $z = t$, then we have a Jordan arc in space, being a one-one continuous image of the unit $t$-interval, end point $t = 1$ included. The desired example is formed of the four Jordan arcs $x = \phi(t)$, $y = \psi(t)$, $z = t$; $x = \phi(t)$, $y = \psi(t)$, $z = 2 - t$; $x = -\phi(t)$, $y = -\psi(t)$, $z = t$; $x = -\phi(t)$, $y = -\psi(t)$, $z = 2 - t$.

The proof results from the fact that the content of the orthogonal projection of this Jordan curve on the xy-plane, counting each point with its proper multiplicity, is four times the sum of the harmonic series. A fortiori, the content of the orthogonal projection of any surface spanned with the curve is  $+\infty$ , and this is, a fortiori, the area of the surface.

It thus appears that the separation of the existence proof into Parts I, II is inherent in the very nature of the problem, since it is futile to try to create distinctions with a functional which is identically  $+\infty$ . The limit process is absolutely essential for a non-finite-area-spanning Jordan contour, and the minimal surface can then be characterized only by the Weierstrass equations, the minimum-area property becoming meaningless. $^{\dagger}$

The corresponding situation in the Dirichlet problem is well known, having been pointed out by Hadamard‡ with the following example. If boundary values on the unit circle are defined by

$$
f (\theta) = \sum_ {p = 1} ^ {\infty} \frac {\cos 2 ^ {2 p} \theta}{2 ^ {p}},
$$

then the Dirichlet functional is identically $+\infty$, but a harmonic function as defined by Laplace's equation exists, being

$$
\sum_ {p = 1} ^ {\infty} \rho^ {2 ^ {2 p}} \frac {\cos 2 ^ {2 p} \theta}{2 ^ {p}}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Bulletin de la Société Mathématique de France, vol. 34 (1906), pp. 135–139.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ However, a good sense in which the least-area property continues to hold will be given in a supplementary note.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">MASSACHUSETTS INSTITUTE OF TECHNOLOGY,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">CAMBRIDGE, MASS.</span></small>