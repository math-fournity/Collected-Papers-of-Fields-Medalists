# THREE DIMENSIONAL MANIFOLDS, KLEINIAN GROUPS AND HYPERBOLIC GEOMETRY

BY WILLIAM P. THURSTON

1. A conjectural picture of 3-manifolds. A major thrust of mathematics in the late 19th century, in which Poincaré had a large role, was the uniformization theory for Riemann surfaces: that every conformal structure on a closed oriented surface is represented by a Riemannian metric of constant curvature. For the typical case of negative Euler characteristic (genus greater than 1) such a metric gives a hyperbolic structure: any small neighborhood in the surface is isometric to a neighborhood in the hyperbolic plane, and the surface itself is the quotient of the hyperbolic plane by a discrete group of motions. The exceptional cases, the sphere and the torus, have spherical and Euclidean structures.

Three-manifolds are greatly more complicated than surfaces, and I think it is fair to say that until recently there was little reason to expect any analogous theory for manifolds of dimension 3 (or more)—except perhaps for the fact that so many 3-manifolds are beautiful. The situation has changed, so that I feel fairly confident in proposing the

1.1. CONJECTURE. The interior of every compact 3-manifold has a canonical decomposition into pieces which have geometric structures.

In §2, I will describe some theorems which support the conjecture, but first some explanation of its meaning is in order.

For the purpose of conservation of words, we will henceforth discuss only oriented 3-manifolds. The general case is quite similar to the orientable case.

1. The decomposition referred to really has two stages. The first stage is the prime decomposition, obtained by repeatedly cutting a 3-manifold  $M^{3}$  along 2-spheres embedded in  $M^{3}$  so that they separate the manifold into two parts neither of which is a 3-ball, and then gluing 3-balls to the resulting boundary components, thus obtaining closed 3-manifolds which are “simpler”. Kneser [Kn] proved that this process terminates after a finite number of steps. The resulting pieces, called the prime summands of  $M^{3}$, are uniquely determined by  $M^{3}$  up to homeomorphism; cf. Milnor, [Mil 1].

The second stage of the decomposition involves cutting along tori. This was discovered much more recently, by Johannson [Joh] and Jaco and Shalen [Ja, Sh], even though the elementary theory of the torus decomposition does not

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Presented to the Symposium on the Mathematical Heritage of Henri Poincaré, April 7–10, 1980; received by the editors July 20, 1981.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1980 Mathematics Subject Classification. Primary 57M99, 30F40, 57S30; Secondary 57M25, 20H15.</span></small>

require any deep techniques. In the torus decomposition, one cuts along certain tori embedded nontrivially in  $M^{3}$ , thus obtaining a 3-manifold whose boundary consists of tori. There is no canonical procedure to close off the boundary components, so they are left alone. The interested reader can learn the details elsewhere.

2. One way to think of a geometric structure on a manifold M is that it is given by a complete, locally homogeneous Riemannian metric. It is better, however, to define a geometric structure to be a space modelled on a homogeneous space  $(X, G)$ , where X is a manifold and G is a group of diffeomorphisms of X such that the stabilizer of any point  $x \in X$  is a compact subgroup of G. For example, X might be Euclidean space and G the group of Euclidean isometries. M is equipped with a family of “coordinate maps” into X which differ only up to elements of G. We make the assumption that M is complete. If X is simply-connected, this condition says that M must be of the form  $X/\Gamma$ , where  $\Gamma$  is a discrete subgroup of G without fixed points.

There are precisely eight homogeneous spaces  $(X, G)$  which are needed for geometric structures on 3-manifolds. These eight homogeneous spaces are determined by the following conditions:

(a) The space X is simply-connected. A manifold modelled on a non-simply-connected homogeneous space is also modelled on its universal cover.

(b) The group G is unimodular, that is, there is a measure on G invariant by multiplication on the right or the left. Otherwise, X would possess a vector field invariant by G which expands volume, so there could be no  $(X, G)$ -manifolds which are compact or which even have finite volume.

(c) G is a maximal group of homeomorphisms of X with compact stabilizers. If G were contained in a larger group  $G'$ , then any  $(X, G)$ -manifold would be an  $(X, G')$ -manifold, so  $(X, G)$  would be redundant.

We will describe these eight geometries in §4. For the moment, it will suffice to say that of these eight, hyperbolic geometry is by far the most interesting, the most complex, and the most useful. The other seven come into play only in exceptional cases.

Conjecture 1.1 subsumes the Poincaré conjecture, which was posed by Poincaré not as a conjecture but as a question: Is every 3-manifold with trivial fundamental group homeomorphic to the 3-sphere? Poincaré raised the question in [Poin], but he did not pursue it, for as he said, “cette question nous entraînerait trop loin”. Conjecture 1.1, just as the Poincaré conjecture, is likely not to be resolved quickly, but I hope it will be a more productive guide to research on 3-manifolds than Poincaré’s question has proven to be. My hope is based on the fact that it applies to all 3-manifolds, so there are many examples which arise. To find a geometric structure for a particular manifold is a great help in understanding that manifold.

2. Supporting evidence. As I hinted earlier, Conjecture 1.1 can be proven in many cases. For instance, I will state a simple necessary and sufficient topological condition for the interior of a 3-manifold with nonempty boundary to have a hyperbolic structure. This theorem will imply Conjecture 1.1 for prime manifolds with nonempty boundary. There is a similar theorem for

closed manifolds which satisfy a technical hypothesis (which is not necessary but frequently true).

A surface  $N^{2}$  embedded in a 3-manifold  $M^{3}$  is two-sided if  $N^{2}$  cuts a regular neighborhood of  $N^{2}$  into two pieces, i.e., the normal bundle to  $N^{2}$  is oriented. Since we are assuming that  $M^{3}$  is oriented, this is equivalent to the condition that  $N^{2}$  is oriented. A two-sided surface is incompressible if every simple curve on  $N^{2}$  which bounds a disk in  $M^{3}$  with interior disjoint from  $N^{2}$  also bounds a disk on  $N^{2}$ .

A 3-manifold $M^3$ is geometrically atoroidal if every incompressible torus embedded in $M^3$ is isotopic to a boundary component.

A 3-manifold $M^3$ is homotopically atoroidal if every map of $T^2$ to $M^3$ which acts injectively on the fundamental group is homotopic to $\partial M$. Homotopically atoroidal implies geometrically atoroidal; the converse is not quite true.

The condition that M is homotopically atoroidal can be rephrased in terms of the fundamental group. Assuming that  $\partial M$  is incompressible, the condition that M is homotopically atoroidal is equivalent to the condition that, first,  $\pi_{1}(M)$  is not expressible as a free product, (this is guaranteed if M is prime), and second, that any subgroup of  $\pi_{1}(M)$  isomorphic to  $Z^{2}$  is conjugate to a subgroup of the fundamental group of some torus boundary component.

Here are two simple examples of homotopically atoroidal manifolds. They are nonrepresentative because their interiors have Euclidean structures.

2.1. EXAMPLE. $M^3 = T^2 \times I$. The interior of $M^3$ is homeomorphic to $\mathbf{E}^3 / \Gamma$, where $\mathbf{E}^3$ is Euclidean 3-space and $\Gamma$ is generated by

$$
(x, y, z) \rightarrow (x + 1, y, z) \quad \text { and } \quad (x, y, z) \rightarrow (x, y + 1, z).
$$

2.2. EXAMPLE.  $M^{3} = T^{2} \times I / (\mathbf{Z}/2)$ , where the Z/2 action flips I and acts as a covering transformation of  $T^{2}$  over the Klein bottle. Its interior is the quotient of  $E^{3}$  by the group  $\Gamma$  generated by

$$
(x, y, z) \rightarrow (x + 1, y, z) \quad \text { and } \quad (x, y, z) \rightarrow (- x, y + 1, - z).
$$

2.3. THEOREM [Th 2]. The interior of a compact 3-manifold $M^3$ with nonempty boundary has a hyperbolic structure iff $M^3$ is prime, homotopically atoroidal and not homeomorphic to Example 2.2.

A hyperbolic structure on the interior of a compact manifold  $M^{3}$  has finite volume iff  $\partial M^{3}$  consists of tori, with the single exception of Example 2.1, which has no hyperbolic structure of finite volume.

2.4. COROLLARY. Conjecture 1.1 is true for all compact, prime 3-manifolds with nonempty boundary.

A good class of examples arises from knots in  $S^{3}$ . (A knot is an embedding of  $S^{1}$  in  $S^{3}$ .) The complement of a knot is homeomorphic to the interior of a manifold whose boundary is a torus.

A torus knot is a knot which can be placed on an ordinary torus in  $S^{3}$ .

![](images/page_3_image_0.jpg)

FIGURE 1. A torus knot of type (3, 8). It can be placed on a torus so that it winds 3 times around the short way while going 8 times around the long way.

With any nontrivial knot K there is associated a whole collection of other knots, known as satellites of K; these are knots which are obtained by a nontrivial embedding of a circle in a small solid torus neighborhood of K. Here, “nontrivial” means that the embedding is not isotopic to K itself and is not contained within a ball inside the solid torus. A knot is a satellite knot if it is a satellite of a nontrivial knot.

![](images/page_3_image_3.jpg)

FIGURE 2. A knot and a satellite of it.

2.5. COROLLARY. If  $K \subset S^{3}$  is a knot,  $S^{3} - K$  has a geometric structure iff K is not a satellite knot. It has a hyperbolic structure iff, in addition, K is not a torus knot.

Indeed, the complement of a knot is always prime, and the torus decomposition is nontrivial exactly when K is a satellite.

Corollary 2.5 was first conjectured by R. Riley [Ri 1] based on his construction of a number of beautiful examples, with the aid of the computer. His work gave a big impetus to me to prove Theorem 2.3.

In order to give the statement for closed manifolds, we need some more terminology.

A 3-manifold  $M^{3}$  is called a Haken manifold if it is prime and it contains a 2-sided incompressible surface (whose boundary, if any, is on  $\partial M$ ) which is not a 2-sphere. A prime 3-manifold whose boundary is not empty is always Haken (with the trivial exception of the 3-ball, which is often considered to be Haken anyway). Any prime 3-manifold whose first homology has positive rank is Haken.

2.5. THEOREM [Th 2]. Conjecture 1.1 is true for Haken manifolds. A closed Haken manifold has a hyperbolic structure iff it is homotopically atoroidal.

It is hard to say how general the class of Haken manifolds is. There are many closed manifolds which are Haken and many which are not. Haken manifolds can be analyzed by inductive processes, because as Haken proved [Hak], a Haken manifold can be cut successively along incompressible surfaces until one is left with a collection of 3-balls. The condition that a 3-manifold has an incompressible surface is useful in proving that it has a hyperbolic structure (when it does), but intuitively it really seems to have little to do with the question of existence of a hyperbolic structure.

A link L in a 3-manifold  $M^{3}$  is a 1-dimensional compact submanifold. A 3-manifold  $N^{3}$  is said to be obtained from  $M^{3}$  by Dehn surgery along L if  $N^{3}$  is obtained by removing a regular neighborhood of L, and gluing it back in by some new identification. The new identification is determined by choosing a diffeomorphism of the torus for each component of L. Two choices of diffeomorphisms  $\phi$  and  $\psi$  give rise to diffeomorphic manifolds if  $\psi^{-1}\phi$  extends to a diffeomorphism of a solid torus (the regular neighborhood of the component of L).

![](images/page_4_image_4.jpg)

FIGURE 3. Modifying a 3-manifold by Dehn surgery. Plugging in a solid torus by $\varphi$ gives a result diffeomorphic to plugging by $\psi$ iff the diffeomorphism of the torus $\psi^{-1} \circ \varphi$ extends to a diffeomorphism of the solid torus.

There remains, for each component of L, a countably infinite set of essentially distinct choices.

2.6. THEOREM [Th 1]. Suppose $L \subset M^3$ is a link such that $M - L$ has a hyperbolic structure. Then most manifolds obtained from $M$ by Dehn surgery along $L$ have hyperbolic structures. In fact, if we exclude, for each component of $L$, a finite set of choices of identification maps (up to the appropriate equivalence relation as mentioned above), all the remaining Dehn surgeries yield hyperbolic manifolds.

It has been proven that for many knots or links, most Dehn surgeries give rise to non-Haken manifolds (see Thurston [Th 1], Hatcher and Thurston [H, T], Culler, Jaco and Rubinstein [C, J, R], Floyd and Hatcher [F, H], Hatcher [Hat]), so Theorem 2.6 yields many hyperbolic manifolds not covered by Theorem 2.5.

Every closed 3-manifold is obtained from the three-sphere  $S^{3}$  by Dehn surgery along some link whose complement is hyperbolic, so in some sense Theorem 2.6 says that most 3-manifolds are hyperbolic. The most promising approach to Conjecture 1.1 seems to be to try to eliminate the vagueness from Theorem 2.6, and analyze exactly what happens under all Dehn surgeries. This can be studied by analytic continuation through families of geometric structures on M - L which become singular at L. For certain examples (see [Th 1]) this has been successfully accomplished, so that here we have geometric structures for all manifolds obtained by Dehn surgeries along L.

It is quite feasible to use computers to study Conjecture 1.1 for classes of manifolds obtained by Dehn surgery. In fact, I have undertaken such a project in order to gain more feeling for the evolution of geometric structures on 3-manifolds. The examples I studied were arbitrary torus bundles over the circle, with Dehn surgery performed along a section of this bundle. Troels Jørgensen was the first to prove that the complement of such a section has a hyperbolic structure, in most cases. I wrote a computer program which found hyperbolic structures for particular Dehn surgeries on particular torus bundles over the circle. With the aid of the program, I found the pattern of which Dehn surgeries give rise to hyperbolic manifolds, and I could then show by hand that those examples for which the program was not producing hyperbolic structures in fact had other geometric structures. For sufficiently complicated torus bundles, the empirical observation is that all but the trivial Dehn surgery gives a hyperbolic manifold.

The geometric structures turn out to be very beautiful when you learn to see them. Often, the information which determines a geometric structure can be expressed in terms of some construction in plane Euclidean geometry. For instance, the output from my computer program which performs Dehn surgery on torus bundles over the circle is a tessellation of the plane minus the origin by triangles. The combinatorial pattern is predetermined, together with rules that certain triangles are similar. If such a pattern exists, then the manifold in question has a hyperbolic structure. $^{1}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$ Added in proof. I can now prove that 1.1 is true for all prime 3-manifolds with a symmetry having fixed point set of dimension  $\geqslant 1$ . This includes the examples above.</span></small>

![](images/page_6_image_0.jpg)

FIGURE 4. Three o'clock sky.

3. Applications. Theorems 2.3 and 2.5, or better yet, the conviction that Conjecture 1.1 is true, have many applications to the understanding of 3-manifolds.

First, we should point out the well-known Mostow rigidity theorem, which asserts that hyperbolic structure on closed manifolds, or more generally, any hyperbolic structure of finite volume, is canonical, provided the dimension is at least 3. (The original theorem, which does not include the case of noncompact manifolds, was proven by Mostow [Mos]. The proof for the noncompact case was completed by Prasad [Pra].)

3.1. MOSTOW RIGIDITY THEOREM. Suppose $M_1$ and $M_2$ are hyperbolic manifolds of finite volume for which there is an isomorphism

$$
\phi \colon \pi_ {1} (M _ {1}) \to \pi_ {1} (M _ {2}).
$$

Then there is an isometry $F: M_{1} \to M_{2}$ which induces the isomorphism $\phi$ (up to conjugacy) between the fundamental groups.

The homotopy type of a hyperbolic manifold is determined by its fundamental group. Theorem 3.1 says that any invariant of the geometry of a hyperbolic manifold is actually an invariant of its homotopy type. This gives a powerful tool for distinguishing 3-manifolds.

3.2. COROLLARY. Let M be a homotopically atoroidal Haken manifold. Then there are only a finite number of isotopy classes of homeomorphisms  $\phi: M \to M$ . The group of isotopy classes of self-homeomorphisms of M lifts to a group of actual homeomorphisms.

OUTLINE OF PROOF. The group of isometries of any Riemannian manifold of finite volume is compact. An isometry of a hyperbolic manifold of finite

volume which is near the identity actually equals the identity, so the group of isometries is finite. An isometry homotopic to the identity is equal to the identity, so the group of isometries is isomorphic to the group of automorphisms of the fundamental group. Waldhausen [Wa 1] showed that a homeomorphism inducing the identity on  $\pi_{1}$  (up to conjugacy) is isotopic to the identity, so the group of isometries is also isomorphic to the group of isotopy classes of homeomorphisms.

REMARK. When M is not geometrically atoroidal, there are self-homeomorphisms of M supported in a neighborhood of a torus which have infinite order up to isotopy.

A group G is called residually finite if for each  $g \in G$  there is some finite quotient map  $f: G \to F$  such that  $f(g) \neq 1$ . If  $G = \pi_{1}(M)$ , an equivalent condition is that every compact subset of the universal covering space of M maps homeomorphically to some finite sheeted covering space.

3.3. THEOREM. The fundamental group of a Haken manifold, or of any manifold for which Conjecture 1.1 holds, is residually finite.

It is a standard fact that a finitely generated subgroup of  $GL_{n}(\mathbf{C})$  is residually finite. Using this, one easily sees that the fundamental group of any geometric 3-manifold is residually finite. After a certain amount of fussing, one can assemble finite quotients of the fundamental groups of pieces of a geometric decomposition of a 3-manifold to obtain finite quotients of the fundamental group of the entire manifold.

One difficulty in the study of 3-manifolds has been the lack of any good invariants, such as the Euler characteristic for 2-manifolds. (The Euler characteristic of a closed 3-manifold is always 0.) Just as the area of a complete hyperbolic 2-manifold is a topological invariant (proportional to the Euler characteristic), so the volume of a hyperbolic 3-manifold is a topological invariant, which in some sense is a single measure of complexity of the manifold. One indication of this is the following theorem, whose basic core is due to Gromov, and which was sharpened in Thurston [Th 1] to give parts (b) and (c).

3.4. THEOREM. (a) Suppose $f \colon M \to N$ is a map of nonzero degree between closed hyperbolic 3-manifolds. Then $\text{volume}(M) \geqslant |\text{degree}(f)|\text{volume}(N)$.

(b) If equality holds in (a), then $f$ is homotopic to a covering map which is a local isometry.

(c) Suppose $M$ is a hyperbolic manifold of finite volume, and $N$ is a hyperbolic manifold containing a (nonempty) link $L$ such that $M \approx N - L$. Then volume $(N) < \text{volume}(M)$.

The situation in part (c) is not unusual.

3.5. THEOREM (Jørgensen). For any constant $C$, let $\mathcal{K}_C$ denote the set of hyperbolic 3-manifolds of volume $\leqslant C$. Then there is a finite subset $\mathfrak{M} \subset \mathcal{K}_C$ such that any element $N \in \mathcal{K}_C$ contains a link $L \subset N$ whose components consist of short geodesics such that $N - L$ is homeomorphic to some element $M \in \mathfrak{M}$.

![](images/page_8_image_0.jpg)

Intuitively, there is a finite set of great-grandmothers whose offspring are all the hyperbolic manifolds of volume  $\leqslant C$ .

If the link $L$ has a short total length, one can show that the volumes of $M$ and $N$ are close. With this information, Theorems 3.4 and 3.5 imply

3.6. THEOREM. The set of volumes of hyperbolic manifolds is a well-ordered subset of $\mathbf{R}$. The set of manifolds with any given volume is finite.

Using the Existence Theorem, 2.6, for hyperbolic Dehn surgeries, one deduces

3.7. THEOREM (SEE [Th 1]). The order type of the set of all volumes of hyperbolic manifolds is $\omega^{\omega}$.

Note. The notation  $\omega^{\omega}$  is that of ordinals, not cardinals:  $\omega^{\omega}$  is the countable ordinal which describes the order type of polynomials (of finite degree) in the symbol  $\omega$  with natural number coefficients, ordered by the limiting order of the values when higher and higher integers are substituted for  $\omega$ .

In other words, there is some lowest volume  $v_{1}$ ; some second lowest volume  $v_{2}$ ; a third lowest volume  $v_{3}$ , and so on until the first accumulation point of volumes  $v_{\omega}$ , which is the smallest volume of a hyperbolic manifold with one cusp. There is a next highest volume  $v_{\omega+1}$ , and so on until the second accumulation point  $v_{2\omega}$ . The first accumulation point of accumulation points is called  $v_{\omega^{2}}$ , and it is the smallest volume of a hyperbolic manifold with two cusps. And so on.

The structure of the set of volumes is significant, but it seems impractical to actually compute the real numbers  $v_{\alpha}$ , for  $\alpha$  a typical ordinal, and probably silly to try for very many ordinals. It would be interesting to know a few simple cases, like  $v_{1}$  and  $v_{\omega}$ , however. Based on a not at all exhaustive examination I made of a few examples and some computer computations of likely classes of examples by Bob Meyerhoff, it seems plausible that  $v_{\omega}$  could be the volume of the complement of the figure eight knot, 2.0...,

the volume

FIGURE 5.

The best candidate for  $v_{1}$  so far is the volume of a manifold obtained by Dehn surgery along the figure eight knot; its volume is about .98.

There is another promising invariant of oriented hyperbolic 3-manifolds, about which practically nothing has been known until recently. This is the eta invariant, or the Chern-Simons invariant which is obtained by reducing the eta invariant mod a constant. The eta invariant should probably be thought of as the imaginary part of a complex constant, of which the volume is the real part. The eta invariant changes sign under reversal of orientation, while the volume is fixed.

Unfortunately, the eta invariant, unlike the volume, has been very difficult to compute, basically because in its definition some very arbitrary choices are involved, and these choices are difficult to make in any reasonable way. Recently, however, Bob Meyerhoff [Mey] has developed some good formulas for the Chern-Simons invariant. Among other things, he has shown that the set of values of the Chern-Simons invariant is dense in the circle—in fact, the manifolds obtained by Dehn surgery on any link with hyperbolic complement have Chern-Simons invariants whose values are dense.

The solution of the Smith conjecture is a development in which several mathematicians were fairly directly involved and in which Theorem 2.3 played an essential part, along with the equivariant loop theorem of Meeks and Yau [M, Y].

3.4. THEOREM. Suppose $\phi: S^3 \to S^3$ is an orientation-preserving diffeomorphism such that $\phi^n = 1$ and for some $x$, $\phi x = x$. Then the fixed point set of $\phi$ is an unknotted circle, and $\phi$ is conjugate to an isometry.$^2$

For an explanation of the various parts of the proof and the somewhat complex way they fit together, see the proceedings of the Smith conjecture conference [Smi].

Conjecture 1.1 leads to a very concrete method of analyzing 3-manifolds. Eventually, it should be practical to begin with any of the usual descriptions of a 3-manifold M (e.g., a description of M using Dehn surgery along a link) and by a routine procedure on the computer, calculate its geometric decomposition (assuming that it has one). The first case to implement should be the case that M is hyperbolic. Robert Riley has, in fact, found hyperbolic structures for a variety of knot complements by computer, but his calculations are not routine except in special cases. Riley's work makes it clear that there is a rigorous, but not generally practical, algorithm for computing hyperbolic structures. The first step in this algorithm is to calculate representations of  $\pi_{1}(M)$  in  $PSL_{2}(\mathbf{C})$ , which is the group of isometries of  $H^{3}$ . One wants a discrete, faithful representation; such a representation is unique up to conjugacy if it exists. Conjugacy classes of representations correspond to solutions of a system of polynomials in a number of variables; one need check only isolated solutions, of which there are only a finite number. An algorithm certainly exists for finding them, but unfortunately, it is not practical for a complicated 3-manifold since the number of variables becomes large and the degree of the polynomials grows exponentially large with the complexity of the 3-manifold. For many less complicated 3-manifolds, however, the set of all representations can be computed practically.

The second step is the part which at first sounds dubious. However, it works theoretically and Riley has written a computer program which handles it quite nicely and practically. This step is to check whether a given representation is discrete and faithful. Riley's method (which originates from Poincaré) is to

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$ Added in proof. The result alluded to in the previous footnote generalizes this and gives a new, purely geometric proof. It implies for instance, that a diffeomorphism of finite order of a hyperbolic manifold has a fixed point set isotopic to a finite union of geodesics.</span></small>

find a fundamental domain for the group action, or else find enough group elements close to the identity to imply the group is not discrete. If a fundamental domain is obtained, that implies that the image of the representation is discrete; if all the relations which come from the combinatorics of the fundamental domain are implied by the relations in the original group, the representation is faithful.

![](images/page_10_image_1.jpg)

FIGURE 6. A fundamental domain for a discrete group of hyperbolic motions with compact quotient, generated by R. Riley's computer program. This is a projectively correct picture, using the Klein model for hyperbolic space.

To make the calculation of hyperbolic structures routine, what remains to be done is to find a practical general method of computing a likely candidate for the right representation of  $\pi_{1}(M)$  in  $PSL_{2}C$ . An approach using analytic continuation, depending on the theory of hyperbolic Dehn surgery, seems promising, but we will know whether it is successful only after it has been implemented on the computer.

There is an alternate approach to the second step, provided for the first step one calculates all representations of  $\pi_{1}(M)$  in  $PSL_{2}C$  and provided also that one knows ahead of time that M has a hyperbolic structure. There is a characteristic number associated to a representation, fairly readily computable, which equals the volume of the quotient space when the representation is discrete and faithful. This characteristic number takes its unique maximal value for a discrete, faithful representation.

Successful completion of the two steps outlined gives a hyperbolic manifold whose fundamental group is  $\pi_{1}(M)$ . Conjecture 1.1, or simply the validity of Conjecture 1.1 for M, would imply that the hyperbolic manifold obtained is homeomorphic to M. If one doubts Conjecture 1.1, then, in general, a third step remains: to check whether M is homeomorphic to the hyperbolic manifold. The method of hyperbolic Dehn surgery often guarantees this. There are

also very tedious algorithms which will eventually construct a homeomorphism provided it exists, but unfortunately there is no known algorithm which will show that the two manifolds are not homeomorphic.

There are indications that computations of other kinds of geometric structures may come as a byproduct of a method of computing hyperbolic structures: often there is a way to interpret these structures as degenerate hyperbolic structures.

4. Eight 3-dimensional geometries. As we promised in §1, we will now describe briefly the eight 3-dimensional homogeneous spaces, or geometries, which are needed to give geometric structures for 3-manifolds. We will in each case give a description of a simply-connected 3-manifold $X$, and a group $G$ of orientation-preserving diffeomorphisms of $X$ with compact stabilizers $G_{x}$. We will group them by the identity component of $G_{x}$: it is isomorphic either to $SO(3)$, to $SO(2)$, or to the trivial group $SO(1)$. For the first three geometries, $G_{x}$ is $SO(3)$.

1. SPHERICAL GEOMETRY. $X$ is the 3-sphere $S^3$ and $G$ is SO(4).

All 3-dimensional spherical manifolds have been classified. Cf. Seifert [Sei], for a complete enumeration.

The three-sphere  $S^{3}$  has the structure of a group: the group of unit quaternions. Therefore  $S^{3} \times S^{3}$  acts on  $S^{3}$  by the formula  $x \stackrel{(g,h)}{\rightarrow} gxh^{-1}$ . The kernel of this action is Z/2, generated by  $(-1,1)$  in quaternionic notation, and this produces an incredible isomorphism

$$
S ^ {3} \times S ^ {3} / \mathbf {Z} / 2 = S O (4).
$$

It is with the aid of this isomorphism that the structure of 3-dimensional spherical manifolds can be analyzed. The most beautiful is the Poincaré dodecahedral space, obtained from a dodecahedron by identifying opposite faces with a 1/10 right-handed rotation. This identification pattern forces the edges to be identified in triples. A regular dodecahedron in Euclidean space has dihedral angles somewhat less than  $120^{\circ}$ . Regular convex polyhedra in  $S^{3}$  have angles anywhere between the Euclidean value and  $180^{\circ}$ . To put a geometric structure on the Poincaré dodecahedral space, find the regular spherical dodecahedron with dihedral angles of  $120^{\circ}$ , and identify them in the given pattern. Note that the universal cover of the Poincaré dodecahedral space is  $S^{3}$ , with a tiling by 120 dodecahedra. (Poincaré first discussed this example in [Poin], in a very nongeometric form.)

It is a strange fact that all spherical manifolds also have a stronger structure, based on $X = S^3$ and $G = S^3 \times S^1 / \mathbf{Z} / 2$.

2. EUCLIDEAN GEOMETRY.  $X = E^{3}$ ,  $G = R^{3} \times SO(3)$ , the group of Euclidean isometries. There are only 10 nonhomeomorphic 3-dimensional Euclidean manifolds. Each one is finitely covered by the 3-torus.

3. HYPERBOLIC GEOMETRY (cf. the article by Milnor in this volume). One good picture of hyperbolic space is the Poincaré upper half space, $X = \{x, y, z | z > 0\}$. The group $G$ is the group $PGL_2(\mathbf{C})$ of nonsingular $2 \times 2$ complex matrices of determinant 1, up to multiplication by $\pm I$ scalars. The action of $G$ on $X$ may be defined as fractional linear transformation using quaternionic

notation, $q = x + yi + zj$. The formula is

$$
q \stackrel {\scriptstyle \begin{bmatrix} a & b \\ c & d \end{bmatrix}} {\rightarrow} (a q + b) (c q + d) ^ {- 1}.
$$

One easily-described example of a hyperbolic manifold is the Seifert-Weber dodecahedral space, obtained by identifying opposite faces of a dodecahedron by 3/10 right-handed rotations. One checks that edges of the dodecahedron are identified in quintuples. To form a geometric model, use the regular hyperbolic dodecahedron whose dihedral angles are  $72^{\circ}$ .

For the next four cases, the identity component of  $G_{x}$  is  $SO(2)$ .

4. $X = S^2 \times \mathbf{E}^1 = G$ consists of (spherical isometries) $\times$ (isometries of the Euclidean line). Note that an isometry which reverses the orientation of both factor preserves the total orientation. There are only two nonhomeomorphic examples of compact manifolds with this geometry; can the reader find them?

5. $X = \mathbf{H}^2 \times \mathbf{E}^1$, $G$ consists of (isometries of $\mathbf{H}^2$) $\times$ (isometries of $\mathbf{E}^1$). Every manifold modelled on this geometry is finitely covered by the product of a surface and a circle. Can the reader find an example which is not itself a product?

6. The space X is the universal covering space set of unit length vectors in the hyperbolic plane,  $T_{1}(\mathbf{H}^{2})$ , and the group G is  $R \times (\text{the universal covering of the group of isometries of } H^{2})$ . The isometries of  $H^{2}$  act by their derivatives, and R acts as simultaneous rotations of all vectors, keeping their based points fixed. Note that even orientation-reversing isometries of  $H^{2}$  preserve the orientation of  $T_{1}(\mathbf{H}^{2})$ . The space of unit tangent vectors to any hyperbolic surface is an example of a manifold with this geometry. Another example is the quotient of  $T_{1}(\mathbf{H}^{2})$  by, say, the group of orientation-preserving automorphisms of the regular (2, 3, 7) tiling.

![](images/page_12_image_7.jpg)

FIGURE 7. A tiling of the hyperbolic plane by congruent triangles with angles $\pi /2,\pi /3,\pi /7$. Upper half-space projection.

7. $X$ is a twisted product of $\mathbf{E}^1$ with $\mathbf{E}^2$, and $G$ is an extension of the group of isometries $\mathbf{E}^2$ by $\mathbf{R}$,

$$
\mathbf {R} \rightarrow G \rightarrow \text { isometries   of } \mathbf {E} ^ {2}.
$$

To see a picture of X, consider  $R^{3}$  with a certain 2-plane field  $\tau$ . Along the z-axis,  $\tau$  is horizontal (orthogonal to the axis). Along any ray emanating from the z-axis and orthogonal to it,  $\tau$  always contains the tangent to the ray, and its slope in the direction orthogonal to the ray increases linearly, so this slope always equals one half the distance from the z-axis. In coordinates, if  $e_{1}, e_{2}$  and  $e_{3}$  are the three coordinate vector fields in  $R^{3}$ ,  $\tau$  is spanned by

$$
e _ {1} - (1 / 2) y e _ {3}, \quad e _ {2} + (1 / 2) x e _ {3}.
$$

Any isometry of the x-y plane lifts to an affine map of  $R^{3}$  which preserves  $\tau$  and also preserves distances along lines parallel to the z-axis. In fact, there is a whole 1-parameter family of such lifts. (These affine maps may be thought of as obtained by an isometry of  $E^{3}$ , followed by some shearing map to adjust  $\tau$ .) These affine transformations of  $R^{3}$  constitute G. Note that an orientation-reversing isometry of  $E^{2}$  lifts only to maps which reverse the z-direction.

Any oriented circle bundle over a 2-torus which is not the 3-torus has this kind of geometric structure. The simplest circle bundle over the 2-torus is the one with Euler class 1, and it is obtained as the quotient of X by the discrete, nilpotent subgroup  $\Gamma$  of G generated by

$$
(x, y, z) \rightarrow (x + 1, y, z + y / 2) \quad \text { and } \quad (x, y, z) \rightarrow (x, y + 1, z - x / 2).
$$

Notice that the commutator of these two generators is the vertical translation

$$
(x, y, z) \rightarrow (x, y, z + 1).
$$

Every other example of a manifold with this geometry is finitely covered by a manifold homeomorphic to  $X/\Gamma$ .

An alternate description of this geometry is to define $X$ as the Heisenberg group,

$$
H = \left\{\left[ \begin{array}{c c c} 1 & x & z \\ & 1 & y \\ & & 1 \end{array} \right] \right\}
$$

and G as the semidirect product of H by  $S^{1}$  acting as a group of automorphisms of H which rotate the x-y plane. In this form, the group  $\Gamma$  can be taken as the subgroup of H where x, y and z are integers.

8. Finally, there is one example for which the identity component of $G_{x}$ is trivial. In this case, $X$ is very naturally a Lie group, the solvable Lie group

$$
\mathbf {R} ^ {2} \rightarrow X \rightarrow \mathbf {R}
$$

where$\mathbf{R}$acts on$\mathbf{R}^{2}$(by conjugation) with the formula

$$
(x, y) \rightarrow (e ^ {t} x, e ^ {- t} y).
$$

The group G is an extension of X by  $(\mathbf{Z}_{2})^{2}$  acting as a group of automorphisms, whose 3 nontrivial elements are the  $180^{\circ}$  rotations

$$
(x, y, t) \rightarrow (- x, - y, t), (x, y, t) \rightarrow (y, x, - t) \text {and} (x, y, t) \rightarrow (- y, - x, - t).
$$

Any torus bundle over  $S^{1}$  whose monodromy is a linear map with distinct real eigenvalues has a geometric structure of this form.

5. The varying geometry of Kleinian groups. The Mostow rigidity theorem applies only to hyperbolic 3-manifolds with finite volume, which are interiors of compact 3-manifolds whose boundary consists of tori. Hyperbolic structures for the interior of a manifold with more complicated boundary are not rigid, and there is a wonderful deformation theory for them. The proofs by induction of Theorems 2.3 and 2.5 involve a study of the varying geometry of such manifolds. The theory of this varying geometry is tricky and rich, and a number of intriguing and significant questions remain. Here we will outline a few of the considerations.

In §4 we mentioned the Poincaré upper half-space picture for  $H^{3}$ . If one adjoins a single point at  $\infty$  in  $R^{3}$ , then the action of the group  $PGL_{2}(\mathbf{C})$  extends to the closure of upper half-space, which is a ball. The boundary of the ball is the Riemann sphere

$$
\mathbf {C} = \mathbf {C} \cup \{\infty \} = \mathbf {C P} ^ {1},
$$

and the action of $PGL_2(\mathbf{C})$ is the usual action as Moebius transformations or complex projective transformations

$$
z \stackrel {[ a b ]} {\rightarrow} \frac {a z + b}{c z + d}.
$$

A Kleinian group  $\Gamma$  is a discrete subgroup of  $PGL_{2}(\mathbf{C})$ , that is, a subgroup for which each element has a neighborhood in the group containing only that point. If  $\Gamma$  has no elements of finite order, then it acts freely on  $H^{3}$ , and  $H^{3}/\Gamma$  is a complete hyperbolic manifold. Henceforth we will assume this to be the case.

Each orbit of  $\Gamma$  acting on C has accumulation points (provided  $\Gamma$  is not finite). The set of all accumulation points of orbits is called the limit set  $L_{\Gamma}$  of  $\Gamma$, while its complement is called the domain of discontinuity,  $D_{\Gamma}$. The Kleinian group  $\Gamma$  acts nicely on  $D_{\Gamma}$  (properly discontinuously) so that its quotient  $D_{\Gamma}/\Gamma$  is a surface, which inherits a conformal structure (= complex structure) from  $D_{\Gamma}$. In fact,  $D_{\Gamma}/\Gamma$  is the boundary of the three-manifold  $(H^{3} \cup D_{\Gamma})/\Gamma$. Sometimes this “Kleinian” 3-manifold is compact, and sometimes it isn’t.

The basic deformation theorem, developed by Ahlfors, Bers, Mostow, Sullivan and others, says that a certain class of relatively mild deformations of  $\Gamma$ , the quasi-conformal deformations of  $\Gamma$ , are controlled precisely by conformal structures on  $D_{\Gamma}/\Gamma$ . Except in degenerate cases (when  $\Gamma$  is abelian) the conformal structure on  $D_{\Gamma}/\Gamma$  is represented by a unique hyperbolic metric, by the classical uniformization theorem.

5.1. AHLFORS FINITE AREA THEOREM. The total hyperbolic area of $D_{\Gamma} / \Gamma$ is finite.

Thus one has a correspondence between the space of quasi-conformal deformations of  $\Gamma$  and the space of finite-area hyperbolic metrics on  $D_{\Gamma}/\Gamma$ , which is called the Teichmüller space of  $D_{\Gamma}/\Gamma$ .

![](images/page_15_image_0.jpg)

FIGURE 8. Six limit curves. The last curve is omnipresent.

Here are some computer sketches of examples in which the limit set is a curve. Poincaré was taken by the nondifferentiable nature of the curves which even have Hausdorff dimension $>1$, as described in Sullivan's article [Sul 1].

The first limit set is a circle. This means the group leaves invariant a hyperbolic plane inside  $H^{3}$ ; in Poincaré upper half-space, hyperbolic planes appear as Euclidean hemispheres resting on C. The other groups are obtained by bending the original group. All the curves except the last are Jordan curves; the last curve actually fills C, but to make the computer actually fill C would require an amount of computer money (and foolishness) approximating the “defense” budget.

A group whose limit set is a circle is called the Fuchsian group (because of Poincaré's modesty), and groups whose limit sets are Jordan curves are called quasi-Fuchsian groups; they are obtained by quasi-conformal deformations of Fuchsian groups. The final group in our sequence of pictures cannot be obtained by a quasi-conformal deformation of a Fuchsian group, since the topology of the limit set has changed. How can we explain limiting phenomena such as this?

First we need to know something about the limiting geometry of hyperbolic surfaces, as the hyperbolic structure goes to infinity in Teichmüller space. One way that hyperbolic structures can go to infinity is that a curve, or system of curves, can be pinched:

![](images/page_16_image_4.jpg)

FIGURE 9. A surface with a pinched waist.

The hyperbolic metric develops a long, skinny waist to accomplish this.

To describe more generally how surfaces can go to infinity in Teichmuller space one needs a generalization of the notion of a simple closed curve.

A geodesic lamination  $\lambda$  of a hyperbolic surface S is a closed subset of S which is a disjoint union of complete geodesics on S (called the leaves of  $\lambda$ ). A simple closed geodesic is one example of a geodesic lamination. To get other examples, consider a sequence of longer and longer simple closed geodesics. There is always a subsequence so that the pictures “converge”, usually to an uncountable set of geodesics. A typical local cross-section of a geodesic lamination is a Cantor set, but other behavior can also occur. The 2-dimensional Lebesgue measure of a geodesic lamination is always 0.

A transverse invariant measure,  $\mu$ , for a geodesic lamination can be thought of as a rule which assigns to each transverse arc  $\alpha$  to  $\lambda$  a measure that is supported on  $\lambda \cap \alpha$  and invariant under maps from one arc  $\alpha$  to another arc  $\beta$  which take each point of intersection of  $\alpha$  with a leaf of  $\lambda$  to a point of intersection of  $\beta$  with the same leaf. One can think of  $\mu$  as a weighted counting of the leaves of  $\lambda$ , or as a measure of the amount of exertion required to cross a certain set of leaves. A lamination equipped with a transverse invariant measure of full support is a measured lamination. We also include here the trivial lamination consisting of no leaves and having 0 measure.

There is a good topology for the set of measured laminations, making it a Hausdorff space. In this topology, a bunch of leaves can continuously get smaller and smaller measure until they vanish. Let  $\mathfrak{ML}(S)$  denote the space of measured laminations on S, and  $\mathfrak{ML}_{0}(S)$  denote the space of compactly supported measured laminations (in the case S is noncompact). Despite the apparently erratic behavior of laminations, we have

5.2. THEOREM [Th 1]. The space $\mathfrak{M}\mathcal{L}_0(S)$ is homeomorphic to Euclidean space of the same dimension as the Teichmüller space for $S$.

There are also projectivized versions of the lamination spaces. That is, any transverse invariant measure may be multiplied by a positive constant to give a new transverse measure. We define the projective lamination spaces

$$
P\mathcal{L}(S) = (\mathfrak{M}\mathcal{L}(S) - 0) / \text { multiplication   by   scalars }
$$

and

$$
P\mathcal{L}_0(S) = (\mathfrak{M}\mathcal{L}_0(S) - 0) / \text { multiplication   by   scalars }.
$$

5.3. THEOREM. There is a natural topology on $\mathfrak{T}(S) \cup P\mathcal{L}_0(S)$ which makes it a ball, where $\mathfrak{T}(S)$ is the Teichmuller space for $S$.

Intuitively, the interpretation is that a sequence of hyperbolic structures on S can go to infinity by “pinching” a certain geodesic lamination  $\lambda$ ; then it converges to  $\lambda$ . As a lamination is pinched toward 0, lengths of paths crossing it are forced toward infinity. The ratios of these lengths determine the transverse invariant measure. A good exposition of this theory may be found in the book by Fathi, Laudenbach, Poénaru et al [F,L,P], although this work deals with the closely related theory of measured foliations.

Geodesic laminations enter into the theory of hyperbolic 3-manifold in a number of guises, but we will describe only one result. Two compactly supported laminations  $\lambda_{1}$  and  $\lambda_{2}$  fill up S if  $S - \lambda_{1} \cup \lambda_{2}$  consists of chunks which, when lifted to S, are bounded if S is compact, or possibly contained in a horoball neighborhood of a cusp.

5.4. DOUBLE LIMIT THEOREM [Th 3]. Let $\lambda_{1}$ and $\lambda_{2}$ be a pair of projective laminations which fill up $S$. Then if $\{g_1^i\} \to \lambda_1$ and $\{g_2^i\}$ are sequences in $\mathfrak{T}(S)$ tending toward $\lambda_{1}$ and $\lambda_{2}$, the sequence of quasi-Fuchsian groups whose two components of $D_{\Gamma}/\Gamma$ have conformal structures given by $g_1^i$ and $g_2^i$ has a subsequence which converges algebraically to some Kleinian group $\Gamma$ isomorphic to $\pi_1(S)$.

This was proven first in the case S is a punctured torus by Jørgensen, [Jør].

This theorem implies the existence of many geometrical complicated Kleinian groups isomorphic to  $\pi_{1}(S)$ , since from the theory developed in [Th 1] the laminations  $\lambda_{1}$  and  $\lambda_{2}$  can be reconstructed from  $\Gamma$  although the information of the projective class of measures is lost.

A geodesic lamination is arational if it intersects every simple closed geodesic. When  $\lambda_{1}$  and  $\lambda_{2}$  are arational (which is the likely case), then the limit set of  $\Gamma$  is the entire 2-sphere.

There is one construction for 3-manifolds which relates very directly to the theory of surfaces, and which gave me considerable difficulty for a time in the proof of Theorem 2.5. In fact, when I first heard the suggestion that Theorem 2.5 was true (by one mathematician giving a distorted quote of another), I immediately came up with this class of 3-manifolds as “obvious” counterexamples.

This construction is the mapping torus construction, which produces a 3-manifold  $M_{\phi}$  depending on a diffeomorphism  $\phi: S \to S$  of a surface S. One simply forms the product  $S \times I$  and identifies each point  $(x, 1)$  to  $(\phi(x), 0)$ . It is easy to construct quite complicated diffeomorphisms  $\phi$  by taking compositions of simple diffeomorphisms, called Dehn twists, which are the identity outside the neighborhood of a simple closed curve on S.

The diffeomorphism $\phi$ of $S$ gives rise to a natural transformation of $\mathfrak{T}(S)$, which extends continuously to the ball $\overline{\mathfrak{T}}(S) = \mathfrak{T}(S) \cup \mathcal{PL}_0(S)$. By the Brouwer fixed point theorem, $\phi$ has at least one fixed point in $\overline{\mathfrak{T}}(S)$.

5.5 THEOREM. One of the following 3 alternatives holds:

(a) There is a fixed point in $\mathfrak{F}(S)$, and $\phi$ is isotopic to a diffeomorphism of finite order.

(b) There is a finite system of disjoint simple curves invariant (up to isotopy) by $\phi$.

(c) There are precisely two points in $P\mathcal{L}_0(S)$ fixed by $\phi$. These are arational laminations which together fill up $S$.

The deduction in part (a) that if  $\phi$  fixes a point in Teichmüller space,  $\phi$  is isotopic to a diffeomorphism of finite order is the same as the deduction of Corollary 3.2 from the Mostow rigidity Theorem 3.1.

Theorem 5.5 is part of the classification of conjugacy classes of diffeomorphisms of surfaces up to isotopy [Th 4] or [F, L, P], analogous to Jordan form. In case (b), one can cut the surface along the system of curves and analyze the diffeomorphism into diffeomorphisms of simpler surfaces. In case (c), there is a very nice, canonical representative of the isotopy class of $\phi$ (up to conjugacy), called a pseudo-Anosov homeomorphism.

5.6. THEOREM [Th 3]. The mapping torus $M_{\phi}$ has a hyperbolic structure if and only if $\phi$ satisfies condition (c) ($\phi$ is isotopic to a pseudo-Anosov homeomorphism).

This was proven first for the case S is a punctured torus by Jørgensen, [Jør]. This is a special case of Theorem 2.5 or 2.3. An exposition of this can also be found in [Su 2]. The proof in [Th 3] is by applying the double limit Theorem 5.4 to the two laminations in$P\mathcal{L}_{0}(S)$fixed by$\phi$. One obtains an action of  $\pi_{1}(S)$  on  $H^{3}$ , which by an extension of the Mostow rigidity theorem from [Th 1] or [Su 3] can be shown to be conjugate to the action obtained by composing with the automorphism  $\phi$ . The conjugating isometry, when adjoined to the isometries coming from  $\pi_{1}(S)$ , gives a discrete, faithful action of  $\pi_{1}(M_{\phi})$ . The quotient manifold is homeomorphic to  $M_{\phi}$  by 3-manifold theory. This was first proven by Stallings [Sta].

Consider now a copy of the surface S inside the 3-manifold  $M_{\phi}$ . The universal covering space S sits inside the universal covering space of  $M_{\phi}$ , which is  $H^{3}$ . The closure of S must contain all of C, because as we have indicated the limit set of  $\pi_{1}(S)$  is all of C. (This is also easy to deduce directly from the existence of a hyperbolic structure on  $M_{\phi}$ .) If we consider any hyperbolic metric on S, this gives a diffeomorphism of S to  $H^{2}$ . Does the map of  $H^{2}$  to  $H^{3}$  so defined extend continuously to a map of the 2-disk to the 3-ball? This question is more subtle than it first appears, but it was answered affirmatively by J. Cannon and me:

5.7. THEOREM [Can-Th]. The circle at infinity in the universal cover of a fiber of a mapping torus maps continuously to the sphere at infinity in  $H^{3}$ , to give a sphere-filling curve.

The topology of the map of  $S^{1}$  to  $S^{2}$  can be described exactly, as follows. Let  $\lambda_{1}$  and  $\lambda_{2}$  be the two geodesic laminations invariant by  $\phi$ . Put two copies of S on a 2-sphere, one filling the northern hemisphere and one filling the southern hemisphere, with corresponding points on the circles at infinity glued together. Put a copy of  $\lambda_{1}$  lifted to S on the northern hemisphere, and  $\lambda_{2}$  lifted to S on the southern hemisphere.

![](images/page_19_image_3.jpg)

FIGURE 10. A pattern of identifications of a circle, here represented as the equator, whose quotient space is topologically a sphere. This defines, topologically, a sphere-filling curve.

Now, form the identification space of  $S^{2}$  obtained by identifying the closure of each leaf of a lamination to a point and the closure of each component of the complement of the laminations to a point. It can be deduced readily from a theorem of R. L. Moore that the identification space is homeomorphic to the 2-sphere.

Since each equivalence class meets the equator, the image of the equator is the entire 2-sphere. This is the topological model we promised.

There are similar models for the possible behaviour of the boundary of S in all the cases covered by the double limit theorem. It is not hard to show that these are the correct topological models provided the maps of  $S^{1}$  are continuous, but continuity is not known in the general case.

We have already given one picture of a space-filling curve, which, indeed, came from this construction. The surface in question was a punctured torus in the figure eight knot complement.

![](images/page_20_image_1.jpg)

FIGURE 11. The figure eight knot is spanned by a surface (topologically, a punctured torus) which can be swept around through all of $S^3$-(the figure eight knot) and brought back to its starting position!

This knot complement is homeomorphic to the mapping torus of the diffeomorphism of the punctured torus determined by the linear map$\begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$of the torus. Here is another example. Note the definite sense of the spirals. This reflects the fact that, unlike in the case of the figure eight knot complement,  $M_{\phi}$  is not diffeomorphic to its mirror image. In this case,  $\phi$  is the diffeomorphism of the punctured torus coming from the linear map$\begin{bmatrix} 5 & 4 \\ 1 & 1 \end{bmatrix}$of the torus.

![](images/page_20_image_4.jpg)

FIGURE 12. The sphere-filling curve determined by the punctured torus bundle over the circle with monodromy$\begin{bmatrix} 5 & 4 \\ 1 & 1 \end{bmatrix}$ .

The double limit theorem is a powerful result for analyzing surface groups, which are among the most flexible of Kleinian groups. There are several other significant theorems which back up the double limit theorem by deriving information about the geometry of the quotient manifolds in the limits which the double limit theorem produces (see [Th 1] and [Th 2]). There are still many basic conjectures which have not been proven in general, however. Information about the infinitely complicated manifolds obtained by the double limit theorem has relevance because it relates to the geometry of closed manifolds, especially to the mapping tori $M_{\phi}$, but also to much more general manifolds.

We will now give a sample of a theorem which complements the double limit theorem by analyzing a certain class of Kleinian groups which are more complicated and more rigid than surface groups.

5.8. THEOREM [Th 2]. Let $\Gamma$ be a Kleinian group such that (a) the Kleinian manifold $M = (\mathbf{H}^3 \cup D_{\Gamma}) / \Gamma$ is compact,

(b) the components of $D_{\Gamma}$ are simply connected and

(c) the closures of any two components of $D_{\Gamma}$ are disjoint.

Then the space of discrete, faithful representations of  $\Gamma$  in  $PSL_{2}C$ , up to conjugacy, is compact.

Condition (b) is equivalent to the topological condition that  $\partial M$  is incompressible, and condition (c) is equivalent to the topological condition that M is acylindrical: there are no essential cylinders in M.

The space of conjugacy classes of discrete faithful representations of  $\Gamma$  is called the algebraic deformation space. For a precise definition of this and other topologies or sets of Kleinian groups, see [Th 2].

Since the quasi-conformal deformation space is noncompact, Theorem 5.8 produces many limits of sequences of quasi-conformal deformations of  $\Gamma$ , which are not themselves quasi-conformal deformations. Just as for the double limits of surface groups produced by Theorem 5.4, the limit set of most of the limiting groups is the entire sphere C, and there is an “ending lamination” associated to each component of  $\partial M$  such that the associated components of  $D_{\Gamma}$  collapse in the limit.

The limiting groups produced by Theorem 5.8, unlike the ones produced by 5.4, do not occur as subgroups of groups with compact quotients. Nonetheless, 5.8 is very important in the proof of Theorem 2.5 because it implies a good deal about what can happen, before passing to the limit. In the inductive proof of Theorem 2.5, this enables one to show that manifolds such as M can be deformed until they fit together to give closed hyperbolic manifolds.

Kleinian groups are very beautiful and rich, with an amazing variety of productive ways to think about them. (Compare the articles of Bers [Bers] and Sullivan [Sul 1] for two different points of view. These samples are not exhaustive.) We have seen a great deal of progress in understanding them, but we are still in the midst of a number of significant and intriguing problems. Perhaps by the year 2000 our understanding of 3-manifolds and Kleinian groups will be solid, and the phenomena we now expect will be proven.

6. Some open questions. Here are a few questions and projects concerning 3-manifolds and Kleinian groups which I find fascinating.

1. Do all 3-manifolds have decompositions into geometric pieces?

2. Is every finite group action on a 3-manifold equivalent to an action respecting the geometry? In particular, let $\phi: M \to M$ be a diffeomorphism of finite order of a hyperbolic manifold. Is there an equivariant isotopy of $\phi$ to an isometry? In particular, is the fixed point set of $\phi$ isotopic to a union of geodesics?$^{3}$

3. Does every 3-dimensional orbifold which contains no bad 2-dimensional suborbifolds admit a geometric decomposition? (For terminology, see [Th 1]. This question contains 2.) $^{3}$

4. Develop a global theory of hyperbolic Dehn surgery. Give specific general upper bounds for nonhyperbolic Dehn surgeries. Describe the limiting geometry which occurs when hyperbolic Dehn surgery breaks down. (See [Th 1]. From a number of examples, we know that the behavior in the limit can be very beautiful, but there is no general theory. This is a possible approach to solving 1 and 3.)

5. Are all Kleinian groups geometrically tame? (See [Th 1] for a definition, which should be extended appropriately to the general case.)

6. Is every Kleinian group a limit of geometrically finite groups? (In many cases, this implies 5.)

7. Develop a theory of Schottky groups and their limits analogous to the theory of quasi-fuchsian groups and their limits developed in [Th 1].

8. Analyze limits of quasi-fuchsian groups with accidental parabolics. (6, 7 and 8 would combine to prove 5 in a very satisfying way.)

9. Is  $H^{3}/\Gamma$ , where  $\Gamma$  is finitely generated, always homeomorphic to the interior of a compact manifold? (This was proven in many cases for geometrically tame groups in [Th 1].)

10. (AHLFORS MEASURE 0 PROBLEM). Does the limit set of a finitely-generated Kleinian group always have full measure or 0 measure, and in the former case does $\Gamma$ act ergodically? (This was proven for many cases of geometrically tame groups in [Th 1].)

11. Classify geometrically tame representations of a given group. Are they parametrized by their ending laminations and their parabolics, together with the conformal structure on the domain of discontinuity?

12. Describe the quasi-isometry type of an arbitrary Kleinian group. In other words, give a formula for a Riemannian manifold that has a diffeomorphism to  $H^{3}/\Gamma$  such that the metrics have a bounded ratio. (A good deal of information about the quasi-isometry types is already known, but it is not yet complete.)

13. If the limit set of a finitely-generated Kleinian group has Hausdorff dimension less than 2, is it geometrically finite? (This would probably be a consequence of 5.)

14. Suppose $\Gamma$ has the property that $(\mathbf{H}^3\cup D_{\Gamma}) / \Gamma$ is compact. Then is it true that the limit set of any other Kleinian group $\Gamma^{\prime}$ isomorphic to $\Gamma$ is the

homeomorphic image of the limit set of  $\Gamma$ , by a homeomorphism taking the fixed point of an element  $\gamma$  to the fixed points of the corresponding element  $\gamma'$ ? (Theorems 5.7 is a special case of this.) There are examples to show that there is no continuous map

$$
L _ {\Gamma} \times \{\text { algebraic   deformation   space   of } \Gamma \} \rightarrow S ^ {2}
$$

which parametrizes the limit sets. Perhaps, though, there is a parametrization which is continuous separately in the two factors.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$ Added in proof. This is now proven, provided, for (3), the complement of the singular locus is irreducible.</span></small>

15. Can finitely-generated subgroups of a finitely-generated Kleinian group be residually separated from the group? In other words, given a subgroup  $H \subset \Gamma$  and  $\gamma \in \Gamma - H$ , is there a finite quotient of  $\Gamma$  in which the image of  $\gamma$  is not in the image of H? Peter Scott proved this property for surface groups. It is useful for a number of topological arguments, even for special subgroups H.

16. Does every aspherical 3-manifold, or every hyperbolic 3-manifold, have a finite-sheeted cover which is Haken? This is related to (15). By applying Mostow's theorem, and (2.5), it is easy to see that a homotopically atoroidal manifold with a finite-sheeted cover which is Haken is homotopy equivalent to a hyperbolic manifold. Unfortunately, there seems to be little prospect of finding such finite-sheeted coverings without first knowing the manifold is hyperbolic.

17. Does every aspherical 3-manifold have a finite-sheeted cover with positive first Betti number? This is stronger than 16.

18. Does every hyperbolic 3-manifold have a finite-sheeted cover which fibers over the circle? This dubious-sounding question seems to have a definite chance for a positive answer.

19. Find topological and geometric properties of quotient spaces of arithmetic subgroups of  $PSL_{2}C$ . These manifolds often seem to have special beauty.

20. Develop a computer program to calculate the canonical form for a general diffeomorphism of a surface, and to calculate the action of the group of diffeomorphisms on  $P\mathcal{L}_{0}(S)$ . Use this to implement an algorithm for the word problem and the conjugacy problem in the group of isotopy classes of diffeomorphisms of a surface.

21. Develop a computer program to calculate hyperbolic structures on 3-manifolds.

22. Tabulate the volumes and the Chern-Simons invariants and other simple information for a bunch of 3-manifolds: for instance, the knots in the knot tables. Try to develop a practical feel for the well ordering.

23. Show that volumes of hyperbolic 3-manifolds are not all rationally related. Cf. [Mil 2].

24. Show that most 3-manifolds with Heegard diagrams of a given genus have hyperbolic structures—in analogy to the hyperbolic Dehn surgery theorem. This would be the next step after 7.

ACKNOWLEDGMENT. I would like to thank George Francis for the illustrations.

## BIBLIOGRAPHY

[Bers] L. Bers, Finite dimensional Teichmüller spaces and generalizations, Bull. Amer. Math. Soc. (N.S.) 5 (1981), 131–172.

[Can, Th] J. Cannon and W. Thurston, Sphere-filling curves and limit sets of Kleinian groups (to appear).

[C, J, S] M. Culler, W. Jaco and H. Rubinstein, Incompressible surfaces in once-punctured torus bundles (to appear).

[F, H] W. Floyd and A. Hatcher, Incompressible surfaces in 2-bridge link complements (to appear).

[F, L, P] A. Fathi, F. Laudenbach, V. Poénaru et al., Travaus de Thurston sur les surfaces, Astérisque 66-67, Société Mathématique de France, 1979.

[Hak] W. Haken, Theorie der Normal Flachen, Acta Math. 105 (1961), 5.

[Hat] A. Hatcher, Incompressible surfaces in once-punctured torus bundles (to appear).

[H, T] A. Hatcher and W. Thurston, Incompressible surfaces in 2-bridge knot complements, Invent. Math. (to appear).

[Ja, Sh] W. H. Jaco and P. B. Shalen, Seifert fibered spaces in 3-manifolds, Mem. Amer. Math. Soc. No. 2 (1979).

[Joh] K. Johannson, Homotopy equivalence of 3-manifolds with boundaries, Lecture Notes in Math., no. 7761, Springer-Verlag, Berlin, Heidelberg, New York, 1979.

[M, Y] W. Meeks and S-T Yau, Topology of three dimensional manifolds and the embedding problems in minimal surface theory, Ann. of Math. 112 (1980), 441-484.

[Mey] R. Meyerhoff, The Chern-Simons invariant for hyperbolic 3-manifolds, thesis, Princeton University, 1981.

[Mil 1] J. Milnor, A unique factorization theorem for 3-manifolds, Amer. J. Math. 84 (1962), 1-7.

[Mil 2] \_\_\_\_, Hyperbolic geometry: the first 150 years, proceedings.

[Mos 1] G. D. Mostow, Strong rigidity of locally symmetric spaces, Ann. Math. Studies, No. 78, Princeton Univ. Press, Princeton, N.J., 1973.

[Mos 2] G. D. Mostow, Inst. Hautes Études Sci. Publ. Math.

[Poin] H. Poincaré, Cinquième complément à l'analysis situs, Rend. Circ. Mat. Palermo 18 (1904), 45–110, or Oeuvres, t. VI, pp. 435–498.

[Pras] G. Prasad, Strong rigidity of $Q$-rank 1 lattices, Invent. Math., 5-6.

[Ril] R. Riley, Discrete parabolic representations of link groups, Mathematika 22 (1975), 141-150.

[Seif] H. Seifert, Topologie drei dimensionales gefasertei Raume, Acta Math. 60 (1933), 147–288.

[Smi] Proceedings of the Smith Conjecture Conference at Columbia University, (to appear).

[Sta] J. Stallings, On fibering certain 3-manifolds, Prentice-Hall, Engelwood Cliffs, N.J., 1962, pp. 95–100.

[Sul 1] D. Sullivan, Discrete conformal groups and measurable dynamics, these proceedings.

[Sul 2] ,

[Th 1] W. Thurston, The geometry and topology of 3-manifolds, preprint, Princeton Univ. Press (to appear).

[Th 2] \_\_\_\_, Hyperbolic structures on 3-manifolds, I: deformations of acylindrical manifolds, preprint.

[Th 3] \_\_\_\_, Hyperbolic structures on 3-manifolds, II: surface groups and 3-manifolds which fiber over the circle.

[Th 4] \_\_\_\_, On the geometry and dynamics of diffeomorphisms of surfaces, I, preprint.

[Wal] F. Waldhausen, On irreducible 3-manifolds which are sufficiently large, Ann. of Math. (2) 87 (1968), 56–88.

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF COLORADO, BOULDER, COLORADO 80309