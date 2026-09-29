# The work of Maryna Viazovska

Henry Cohn

## Abstract

On July 5th, 2022, Maryna Viazovska was awarded a Fields Medal for her solution of the sphere packing problem in eight dimensions, as well as further contributions to related extremal problems and interpolation problems in Fourier analysis. This article explains some of the ideas behind her work to a broad mathematical audience.

Mathematics Subject Classification 2020 Primary 52C17; Secondary 11F03, 11H31

Keywords Sphere packing, modular forms

![](images/page_1_image_0.jpg)

Figure 1 An optimal packing of cannonballs.

## 1. Introduction

The sphere packing problem asks how we can fill as large a fraction of space as possible with congruent balls, if they are not allowed to overlap except tangentially.1 This problem sits at the interface between many branches of mathematics, and of science more generally, with connections ranging from materials science to information theory. Sphere packing is a natural problem in Euclidean geometry, with a simple statement, and one might expect an equally elementary and self-contained solution. Instead, the topic is dominated by unexpected connections.

Before Viazovska’s breakthrough work, the optimal sphere packing density was known only in one, two, and three dimensions. One dimension is trivial, because intervals can tile the real line with density 1. Two dimensions is not trivial, but Thue [26] showed that arranging six neighbors around each disk is optimal, with density$\pi / { \sqrt { 1 2 } } = 0 . 9 0 6 8 \dots$. Three dimensions was solved by Hales [16] via an ingenious and elaborate computer-assisted proof, which has since been formally verified [17]. The unsurprising answer is shown in Figure 1: optimal two-dimensional layers are nestled together as densely as possible, to achieve density $\pi / { \sqrt { 1 8 } } = 0 . 7 4 0 4$

These prior results paint a misleading picture of what happens in higher dimensions. Stacking optimal layers from the previous dimension generally produces suboptimal packings, and nobody has any idea what the densest sphere packings might be in most dimensions. We do not even know whether they should be crystalline or disordered.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1To state the problem precisely, “as large a fraction as possible” must be made precise. One way to do so is by taking a limit of the packing problem in a bounded region as its size grows relative to the sphere radius. The sphere packing problem turns out to be very robust in the sense that just about all reasonable formulations are equivalent.</span></small>

High-dimensional packings are not merely of pure mathematical interest, but also important for practical applications, because sphere packings are error-correcting codes for a continuous communication channel (such as radio). In this model, the packing is in an abstract signal space, whose dimension is the number of measurements used to characterize the signal and is generally much larger than three.

There does not seem to be any simple pattern in the optimal packings that persists across many dimensions, and the best upper and lower bounds known for the packing density $\mathbb { R } ^ { d }$remain exponentially far apart as$d$grows. However, a handful of dimensions stand out as special, most notably eight and twenty-four dimensions. These dimensions feature exceptional packings, namely the$E _ { 8 }$root lattice and the Leech lattice$\Lambda _ { 2 4 }$, with remarkable symmetries and numerous connections to diferent branches of mathematics. Thanks to Viazovska’s work [10,27], we now know that they are truly optimal. The jump from three dimensions to eight and twenty-four in the known solutions is remarkable, and it illustrates the exceptional nature of these packings.

The$E _ { 8 }$and Leech lattices had long been viewed as the most compelling candidates for further solutions of the sphere packing problem. However, a direct geometric proof seems infeasible: it is natural to try to work with a decomposition of space into cells, but the curse of dimensionality means we are faced with an unmanageable number of potential cell shapes and ways they could adjoin each other. Perhaps there exists a proof along these lines, but nobody has found a workable approach.

Instead, Viazovska proved the optimality of$E _ { 8 }$via a dramatic new connection to the theory of modular forms, following which she and several collaborators extended her ideas to the case of the Leech lattice:

Theorem 1.1 (Viazovska [27]). The$E _ { 8 }$root lattice achieves the optimal sphere packing density in$\mathbb { R } ^ { 8 }$, namely$\pi ^ { 4 } / 3 8 4$

Theorem 1.2 (Cohn, Kumar, Miller, Radchenko, and Viazovska [10]). The Leech lattice$\Lambda _ { 2 4 }$ achieves the optimal sphere packing density in$\mathbb { R } ^ { 2 4 }$, namely$\pi ^ { 1 2 } / 1 2 !$

As Peter Sarnak said at the time [19], her paper [27] is “stunningly simple, as all great things are.” This simplicity is characteristic of Viazovska’s work: she has a gift for linking concepts and posing bold conjectures, and these insights lead her to striking arguments. Her proofs engage directly with the heart of the matter, without any extraneous complications. Of course, simple is very much not the same thing as easy. What makes her work extraordinary is how diferent her ideas are from what came before.

In the remainder of this article, we will examine Viazovska’s proof of the optimality of$E _ { 8 }$, as well as its motivation and place in mathematics more broadly. In particular, this article can serve as an introduction and guide to Viazovska’s techniques, alongside other expositions [6,20]. For background on sphere packing and lattices, see [12,15,25].

Of course we should keep in mind that this topic represents only one strand of Viazovska’s research. For example, [3] is a beautiful and decisive paper on a quite diferent topic. What will she be known for in twenty or thirty years? I look forward to finding out.

## 2. The past

Before we turn to Viazovska’s proof, we will need some background. In this section, we will construct the$E _ { 8 }$lattice and explain a method for proving upper bounds for the sphere packing density.

Sphere packings can be constructed in many ways, among which lattice packings are the simplest possibility. A lattice packing of spheres centers the spheres at the points of a lattice Λ in$\mathbb { R } ^ { d }$, i.e., a discrete subgroup of$\mathbb { R } ^ { d }$of rank$d ,$, or equivalently the integral span of a basis of$\mathbb { R } ^ { d }$. There is no reason why an optimal sphere packing should have this algebraic structure, and for example the best sphere packing known in$\mathbb { R } ^ { 1 0 }$does not. However, many of the best sphere packings known in low dimensions are lattice packings.

To form a packing from a lattice Λ, we must choose the sphere radius � so that neighboring spheres do not overlap. Specifically, we should take

$$
r = \frac {1}{2} \min _ {x \in \Lambda \backslash \{0 \}} | x |.
$$

The volume of a sphere of radius � in$\mathbb { R } ^ { d }$is$\pi ^ { d / 2 } r ^ { n } / ( d / 2 ) !$!, where$( d / 2 )$! means$\Gamma ( d / 2 + 1 )$ when � is odd, and the density of the overall packing (i.e., the fraction of space covered by the balls) is the sphere volume times the number of spheres per unit volume in space. Let vol$\left( \mathbb { R } ^ { d } / \Lambda \right)$denote the covolume of the lattice, i.e., the volume of the quotient torus, or equivalently the absolute value of the determinant of a lattice basis. Then the number of spheres per unit volume in space is$1 / \mathrm { v o l } \big ( \mathbb { R } ^ { d } / \Lambda \big )$, and so the lattice packing density is

$$
\frac {\pi^ {d / 2} r ^ {n}}{(d / 2) ! \operatorname{vol} \left(\mathbb {R} ^ {d} / \Lambda\right)}.
$$

One of the most remarkable lattices is the$E _ { 8 }$root lattice, which originated in Lie theory but has since become widespread across mathematics. We will see below how to obtain $E _ { 8 }$as a modification of the$D _ { d }$lattice, the checkerboard lattice in � dimensions, which is defined by

$$
D _ {d} = \left\{\left(x _ {1}, \dots , x _ {d}\right) \in \mathbb {Z} ^ {d}: x _ {1} + \dots + x _ {d} \text {is even} \right\}.
$$

In other words,$D _ { d }$simply omits every other point in the cubic lattice$\mathbb { Z } ^ { d }$. As a special case, $D _ { 3 }$is the face-centered cubic lattice in three dimensions, which Hales showed achieves the optimal sphere packing density [16], and$D _ { 4 }$and$D _ { 5 }$are the best packings known in their dimensions. However,$D _ { d }$is not optimal beyond five dimensions.

The problem with$D _ { d }$in higher dimensions is that its holes are too large. A hole is a point in space that is a local maximum for distance from the lattice. There are two types of holes in$D _ { d } .$, shallow holes at distance 1 from the lattice, such as$( 1 , 0 , \ldots , 0 )$), and deep holes at distance$\sqrt { d / 4 }$from the lattice, such as$\big ( \frac { 1 } { 2 } , \frac { 1 } { 2 } , \dots , \frac { 1 } { 2 } \big )$. As$d \to \infty$, so does$\sqrt { d / 4 }$ and so the deep holes become large enough to fit enormous numbers of additional spheres. In particular,$D _ { d }$cannot be optimal when � is large.

When$d = 8$, something beautiful happens. The distance$\sqrt { 8 / 4 }$from a deep hole to the lattice exactly equals the distance$\sqrt { 2 }$between lattice points in$D _ { 8 }$, and that means the deep holes are just large enough to be filled with additional spheres. If we plug these holes with spheres, then the resulting packing is the union of$D _ { 8 }$with its translate$D _ { 8 } + { \bigl ( } { \frac { 1 } { 2 } } , { \frac { 1 } { 2 } } , \ldots , { \frac { 1 } { 2 } } { \bigr ) }$). It is not hard to check that this packing is a lattice (it amounts to the fact that$2 \cdot ( { \frac { 1 } { 2 } } , { \frac { 1 } { 2 } } , \ldots , { \frac { 1 } { 2 } } ) \in$ $D _ { 8 } )$, which is called the$E _ { 8 }$root lattice.

![](images/page_4_image_0.jpg)

Figure 2

A two-dimensional cross section of$\mathbb { R } ^ { 8 }$through a Coxeter plane of$E _ { 8 }$, colored according to the squared distance to the nearest point in$E _ { 8 }$(dark is close) and inspired by [22]

The$E _ { 8 }$lattice packing has packing radius$r = \sqrt { 2 } / 2$and covolume vol$\left( { \mathbb { R } } ^ { 8 } / E _ { 8 } \right) =$ vol$\left( \mathbb { R } ^ { 8 } / D _ { 8 } \right) / 2 = 1$, and so it has a packing density of$\pi ^ { 4 } / 3 8 4 = 0 . 2 5 3 6 \dots { \mathrm { ~ I t } }$is by no means obvious that this construction is optimal. In fact, the construction feels a little ad hoc. However, the$E _ { 8 }$lattice turns out to be far more beautiful and symmetric than its construction indicates. For example, see Figure 2 for a view of$E _ { 8 }$with 30-fold symmetry. This is a common pattern with exceptional structures in mathematics: they are typically obtained by piecing together several substructures that each have less symmetry individually.

Now that we have the$E _ { 8 }$lattice, the next question is how we could try to obtain a matching upper bound for the sphere packing density in eight dimensions. Obtaining a matching bound seems completely infeasible in most dimensions, but in a few special dimensions bounds based on harmonic analysis work remarkably well. This idea, called the linear programming bound, goes back to a fundamental paper by Delsarte [13] on error-correcting codes, and the corresponding bound for sphere packings was developed by Cohn and Elkies [7].

The linear programming bound is formulated in terms of the Fourier transform$\widehat { f }$ of an integrable function$f \colon  { \mathbb { R } ^ { d } } \to  { \mathbb { C } }$, which we will normalize as

$$
\widehat {f} (y) = \int_ {\mathbb {R} ^ {d}} f (x) e ^ {- 2 \pi i \langle x, y \rangle} d x,
$$

where$\langle \cdot , \cdot \rangle$is the usual inner product on$\mathbb { R } ^ { d }$. Recall that the Fourier transform decomposes $f$into complex exponentials; in signal processing terms, it amounts to identifying the fre quencies that occur in a signal and their relative magnitudes. This decomposition amounts to the Fourier inversion theorem: if$\widehat { f }$is integrable as well, then

$$
f (x) = \int_ {\mathbb {R} ^ {d}} \widehat {f} (y) e ^ {2 \pi i \langle x, y \rangle} d y.
$$

In other words, the Fourier transform is very nearly its own inverse, with a single sign change being the only diference. Note that$\widehat { f }$is generally complex-valued, even if$f$is real-valued, but$\widehat { f }$is real-valued if$f$is real-valued and an even function.

We will also need a few types of well-behaved functions. A function$f \colon  { \mathbb { R } ^ { d } } \to$R is called rapidly decreasing if$f ( x ) = O { \bigl ( } | x | ^ { - c } { \bigr ) }$as$| x | \to \infty$for every constant$c > 0$, and a Schwartz function is a smooth function such that it and all its iterated partial derivatives (of every order) are rapidly decreasing. Schwartz functions are arguably the best-behaved functions in harmonic analysis. Much of what we will discuss can be generalized somewhat beyond Schwartz functions, but they are all Viazovska needed to solve the sphere packing problem.

We can now state the linear programming bound for sphere packing:

Theorem 2.1 (Cohn and Elkies [7]). Let$f \colon  { \mathbb { R } ^ { d } } \to  { \mathbb { R } }$be an even Schwartzfunction and � a positive real number.$H$

(1)$f ( x ) \leq 0$for all$\boldsymbol { x } \in \mathbb { R } ^ { d }$satisfying$| x | \geq r$

(2)${ \widehat { f } } ( y ) \geq 0 .$for all$\boldsymbol { y } \in \mathbb { R } ^ { d }$, and

(3)$f ( 0 ) = { \widehat { f } } ( 0 ) = 1 ,$

then the optimal sphere packing density in$\mathbb { R } ^ { d }$is at most vol$\left( { B } _ { r / 2 } ^ { d } \right) = \pi ^ { d / 2 } ( r / 2 ) ^ { d } / ( d / 2 ) !$

This theorem produces an upper bound for the packing density from a function$f$ satisfying certain inequalities, but it says nothing about how to choose$f$to optimize the bound. Numerical optimization can produce good choices for$f ,$which yield the bounds shown in Figure 3. These bounds are rigorous, but it is possible that other functions may produce even better bounds.

As one can see in Figure 3, the bounds in eight and twenty-four dimensions appear sharp. Numerical optimization will not yield an exactly sharp bound, but it seems to come as close as desired. Based on data of this sort as well as analogies with other problems in coding theory, Cohn and Elkies conjectured the existence of magicfunctions$f$that would solve the sphere packing problem exactly in$\mathbb { R } ^ { 8 }$and$\mathbb { R } ^ { 2 4 }$, by achieving$r = { \sqrt { 2 } }$and$r = 2$, respectively. Note that this is not because the bound dips lower in these dimensions, but rather because the optimal packings rise up to meet it. No other dimensions greater than 2 seem to have a sharp linear programming bound, and it seems unlikely that others exist, but no proof is known, and the bound has been exactly optimized only for$d = 1 , 8 .$, and 24.

![](images/page_6_chart_0.jpg)

A plot of the numerically computed linear programming bound [1] and the best sphere packing density currently known [12].

The heart of Viazovska’s breakthrough lies in the construction of the magic functions. What should � look like if we are to obtain a sharp bound? There are some simple criteria, which we can obtain from the proof of Theorem 2.1. In this article we will examine a proof for just the special case of lattices, but the theorem can be proved in full generality by combining the same technique with a little additional algebra. The argument is based on the Poisson summationformula, which says that if$f \colon  { \mathbb { R } ^ { d } } \to  { \mathbb { C } }$is a Schwartz function, Λ is a lattice in$\mathbb { R } ^ { d }$, and$\Lambda ^ { * }$is its dual lattice (i.e., the lattice generated by the dual basis of any basis of Λ with respect to the inner product$\langle \cdot , \cdot \rangle )$), then

$$
\sum_ {x \in \Lambda} f (x) = \frac {1}{\operatorname{vol} \left(\mathbb {R} ^ {d} / \Lambda\right)} \sum_ {y \in \Lambda^ {*}} \widehat {f} (y).
$$

ProofofTheorem 2.1for lattice packings. The sphere packing problem is scaling-invariant, and so we can use spheres of radius$r / 2$. Let Λ be any lattice packing with packing radius $r / 2$, which means$| x | \geq r \mathrm { f o r } x \in \Lambda \setminus \{ 0 \}$. If � satisfies the hypotheses of Theorem 2.1, then $f ( x ) \leq 0$for$x \in \Lambda \backslash \{ 0 \}$and${ \widehat { f } } ( y ) \geq 0$for all �, from which it follows tha

![](images/page_7_image_0.jpg)

Figure 4

This schematic diagram, which is taken from [6], shows the roots of the magic function � and its Fourie transform$\widehat { f }$in eight dimensions. It is not a plot of the actual function, which decreases very rapidly. See Figure 5 for an actual plot.

$$
1 = f (0) \geq \sum_ {x \in \Lambda} f (x) = \frac {1}{\operatorname{vol} \left(\mathbb {R} ^ {d} / \Lambda\right)} \sum_ {y \in \Lambda^ {*}} \widehat {f} (y) \geq \frac {\widehat {f} (0)}{\operatorname{vol} \left(\mathbb {R} ^ {d} / \Lambda\right)} = \frac {1}{\operatorname{vol} \left(\mathbb {R} ^ {d} / \Lambda\right)}.
$$

Therefore the packing density vol$\left( B _ { r / 2 } ^ { d } \right) / \mathrm { v o l } \left( \mathbb { R } ^ { d } / \Lambda \right)$is bounded above by vo$\left( B _ { r / 2 } ^ { d } \right)$, as desired.■

A first observation is that we can assume without loss of generality that � is radial, i.e., �(�) depends only on |�|. This reason is that we can replace � with the average of its rotations about the origin, because all the constraints are linear and rotation-invariant. One might wonder whether non-radial functions could be helpful conceptually even if they are not needed, but so far the answer appears to be no. Instead, Viazovska’s work turns out to lead to a wonderful new theory of interpolation for radial functions. We will henceforth assume $f$is radial, and when$t \in [ 0 , \infty )$we will write$f ( t )$for the common value$f ( x )$with$| x | = t ,$ as well as$f ^ { \prime } ( t )$for the radial derivative.

Now if we examine the central inequality in the proof of Theorem 2.1 for lattices, we can see when it could be sharp. To obtain a sharp bound, all of the discarded terms in the inequality must vanish: we must have$f ( x ) = 0 \mathrm { f o r } x \in \Lambda \backslash \{ 0 \}$and${ \widehat { f } } ( y ) = 0$for$y \in \Lambda ^ { * } \setminus \{ 0 \}$ In other words, � must vanish on the nonzero distances between lattice points, and$\widehat { f }$must vanish on the nonzero distances between dual lattice points.

One can check directly from the construction of$E _ { 8 }$given above that$E _ { 8 } ^ { * } = E _ { 8 }$and that the vector lengths in$E _ { 8 }$are all square roots of even integers. Furthermore, it turns out that each distance$\sqrt { 2 n }$with$n \geq 0$actually occurs in$E _ { 8 }$. We should therefore have$r = \sqrt { 2 }$in Theorem 2.1, and the magic function � should have a sign change at radius${ \sqrt { 2 } } ,$, followed by double roots at$\sqrt { 2 n }$for$n \geq 2$, as indicated in Figure 4. In other words, we wish to control the behavior of$f$and$\widehat { f }$to second order at these points, i.e., control both the values$f ( { \sqrt { 2 n } } )$ and${ \widehat { f } } ( { \sqrt { 2 n } } )$and the radial derivatives$f ^ { \prime } ( { \sqrt { 2 n } } )$and${ \widehat { f } } ^ { \prime } ( { \sqrt { 2 n } } )$

How can one construct such a function$f 2$The reason this task is dificult is that it involves controlling both$f$and$\widehat { f }$simultaneously. Either one is of course easy on its own, but handling both at once introduces profound dificulties. The underlying issue here is Heisenberg’s uncertainty principle: in loose terms, whenever you try to pin down �, you lose control over${ \widehat { f } } ,$and vice versa. More precisely, we run into Bourgain, Clozel, and Kahane’s uncertainty principle for controlling the signs of functions [4, 8]. These seemingly simple inequalities on$f$and$\widehat { f }$therefore turn out to be far more subtle than they initially appear.

![](images/page_8_image_0.jpg)

Figure 5

Two plots of Viazovska’s magic function in eight dimensions. The first plot is scaled correctly, but it decreases so rapidly that the roots become invisible. The second plot introduces a rescaling to make them visible, based on th asymptotic decay rate.

When Elkies and I proposed this method in 1999, Viazovska was still in secondary school. Without realizing how profoundly dificult the remaining step was, I imagined that we had almost solved the sphere packing problem in eight and twenty-four dimensions, and our inability to find the magic functions was extremely frustrating. At first, I worried that someone else would find an easy solution and leave me feeling foolish for not doing it myself. Over time I became convinced that obtaining these functions was in fact dificult, and others also reached the same conclusion. For example, Thomas Hales has said that$^ { 6 6 } \mathrm { I }$felt that it would take a Ramanujan to find$\mathrm { i t } ^ { \prime \prime }$[19]. Eventually, instead of worrying that someone else would solve it, I began to fear that nobody would solve it, and that I would someday die without knowing the outcome. I am grateful that Viazovska found such a satisfying and beautiful solution, and that she introduced wonderful new ideas for the mathematical community to explore.

## 3. Modular forms

Viazovska’s magic function is constructed using modular forms, certain special functions that play an important role in number theory. The theory of modular forms has a reputation for being somewhat forbidding, but the basics are not so dificult, and that is all that is needed for Viazovska’s proof. We will outline the needed theory here. For a down to earth introduction to the case of$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$, see Chapter VII in [24], and for more detailed and general treatments, see [5,14,28].

We begin with an example of a modular form, namely Eisenstein series. Recall that the Riemann zeta function is defined by

$$
\zeta (s) = \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {s}}
$$

when this sum converges, i.e., when$\operatorname { R e } ( s ) > 1$. Here we are summing inverse powers of the arithmetic progression 1, 2, . . . , and Euler obtained an exact formula when � is an even integer. What if we instead wanted to sum inverse powers of a lattice in the complex plane? Setting aside the question of why we would want to do this (the result has deeper significance than one might guess), we could write the result as the Eisenstein series

$$
E _ {k} (z) = \frac {1}{2 \zeta (k)} \sum_ {(m, n) \in \mathbb {Z} ^ {2} \backslash \{(0, 0) \}} \frac {1}{(m z + n) ^ {k}}\tag{3.1}
$$

for Im$z > 0$, where we are summing over the lattice$\{ m z + n : m , n \in \mathbb { Z } \}$, with the exception of the point$( 0 , 0 )$at which the summand blows up. Up to scaling by a complex factor, all two-dimensional lattices are of this form.

The factor of$1 / ( 2 \zeta ( k ) )$in the definition is merely a convenient normalizing factor, which plays no essential role in the study of$E _ { k }$. Unfortunately, the notation$E _ { k }$conflicts with our name for the$E _ { 8 }$root lattice, but that will not cause any ambiguity in practice.

We will restrict our attention to positive integers$k ,$, so that$( m z + n ) ^ { k }$is single-valued. The series (3.1) converges absolutely when$k \geq 3$, but just conditionally when$k = 2$. For odd �, the$( m , n )$and$\left( - m , - n \right)$terms cancel and we obtain$E _ { k } ( z ) = 0$, and so only the even cases are interesting.2 Thus, we will focus on$E _ { k }$for � even and at least 4.

What does an Eisenstein series look like? Figure 6 is a plot of$E _ { 4 }$, in which black is zero, white is infinity, and color indicates complex phase [21], with the sharp transitions in color occurring at positive real values. The fractal structure visible in this plot can be explained using two functional equations:

$$
E _ {k} (z + 1) = E _ {k} (z) \quad \text { and } \quad E _ {k} (- 1 / z) = z ^ {k} E _ {k} (z).
$$

These symmetries follow from rearranging the defining series (3.1) when$k > 2 .$, and they are the central equations in the theory of modular forms.

The mappings$z \mapsto z + 1$and$z \mapsto - 1 / z$that occur in these functional equations generate a discrete group of linear fractional transforms of the upper half-plane$\mathcal { H } = \{ z \in$ $\mathbb { C } : \operatorname { I m } z > 0 \}$. To put it into a broader context of matrix groups, we can let the matrix${ \textstyle \binom { a \ b } { c \ d } }$ act on H via

$$
\left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \cdot z = \frac {a z + b}{c z + d}.
$$

Then the matrices$\begin{array} { r } { T = \left( \begin{array} { l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right) } \end{array}$and$\begin{array} { r } { S = \left( \begin{array} { c c } { 0 } & { - 1 } \\ { 1 } & { 0 } \end{array} \right) } \end{array}$satisfy$T \cdot z = z + 1$and$S \cdot z = - 1 / z$, and they turn out to generate the group${ \mathrm { S L } } _ { 2 } ( \mathbb { Z } )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">k > 1.� > 1.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Í<sub>�∈Z\{0}</sub> �</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2This parity phenomenon is essentially the same as in Euler’s formula for the zeta function at even integers, which can be viewed as computing <sup>−�</sup> explicitly for all integers</span></small>

Figure 6

![](images/page_10_image_1.jpg)

![](images/page_10_image_2.jpg)

A plot of the Eisenstein series$E _ { 4 } ( z )$for$- 1 \leq \mathsf { R e } z \leq 1$and$0 <$< Im$z \leq 1$(above) and the same plot overlaid with a tiling of Husing fundamental domains for the action of$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$(below).

The weight � action of$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$on functions$f \colon { \mathcal { H } } \to \mathbb { C }$is defined by

$$
(f | _ {k} \gamma) (z) = (c z + d) ^ {- k} f \left(\frac {a z + b}{c z + d}\right)
$$

for$\gamma = \left( { a \atop c d } b \right)$. In this notation, the functional equations$E _ { k } ( z + 1 ) = E _ { k } ( z )$and$E _ { k } { \left( - 1 / z \right) } =$ $z ^ { k } E _ { k } ( z )$imply that the Eisenstein series$E _ { k }$satisfies$E _ { k } | _ { k } \gamma = E _ { k }$for all$\gamma \in \mathrm { S L } _ { 2 } ( \mathbb { Z } )$when $k > 2$

A modularform ofweight � for$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$is a holomorphic function$f \colon { \mathcal { H } } \to \mathbb { C }$such that$f | _ { k } \gamma = f$for all$\gamma \in \mathrm { S L } _ { 2 } ( \mathbb { Z } )$) and one additional condition holds, called being holomorphic at infinity. To state this condition, note that taking$\gamma = T$shows that$f ( z + 1 ) = f ( z )$, and thus we can expand � as a Fourier series

$$
f (z) = \sum_ {n \in \mathbb {Z}} a _ {n} e ^ {2 \pi i n z}.
$$

We say � is meromorphic at infinity if there are only finitely many nonzero coeficient$a _ { n }$ with$n < 0$, and holomorphic at infinity if$a _ { n } = 0$for all$n < 0$. The name reflects the fact that this Fourier series governs the behavior of$f ( z )$as Im � grows, because$e ^ { 2 \pi i z }  0$as Im$z \longrightarrow \infty$. The Fourier series of a modular form is often known as its -series, with$q = e ^ { 2 \pi i z }$

The normalization factor$1 / ( 2 \zeta ( k ) )$in (3.1) ensures that the �-series of$E _ { k }$has rational coeficients, and even integral coeficients when � is small. For example, one can show that$\begin{array} { r } { E _ { 4 } ( z ) = 1 + 2 4 0 \sum _ { n \geq 1 } \sigma _ { 3 } ( n ) q ^ { n } } \end{array}$and$\begin{array} { r } { E _ { 6 } ( z ) = 1 - 5 0 4 \sum _ { n \geq 1 } \sigma _ { 5 } ( n ) q ^ { n } } \end{array}$, where$\sigma _ { k } ( n )$ denotes the sum of the �-th powers of the divisors of �.

The product of modular forms of weights � and ℓ is a modular form of weight$k + \ell ,$ and modular forms therefore form a graded ring. For${ \mathrm { S L } } _ { 2 } ( \mathbb { Z } )$, one can show that this ring is generated by$E _ { 4 }$and$E _ { 6 }$. In other words, the vector space of modular forms of weight � for $\mathrm { S L } _ { 2 } ( Z )$is spanned by the modular forms$E _ { 4 } ^ { j } E _ { 6 } ^ { \ell }$with$4 j + 6 \ell = k$

In addition to using Eisenstein series directly, Viazovska also uses the modular discriminant$\Delta ,$, which is given by

$$
\Delta (z) = \frac {E _ {4} (z) ^ {3} - E _ {6} (z) ^ {2}}{1 7 2 8} = q \prod_ {n = 1} ^ {\infty} (1 - q ^ {n}) ^ {2 4}.\tag{3.2}
$$

Its key property is that it vanishes nowhere in the upper half plane, while it vanishes at infinity (in the sense that its �-series has no constant term).

Turán said that special functions should instead be called useful functions, and modular forms are no exception to this principle. The reason we study modular forms is not that we have a special love for Eisenstein series, but rather that the functional equations $f ( z + 1 ) = f ( z )$and$f ( - 1 / z ) = z ^ { k } f ( z )$arise far more often than one might expect. For example, the$E _ { 8 }$lattice has an important modular form associated with it, namely its theta series

$$
\Theta_ {E _ {8}} (z) = \sum_ {n = 0} ^ {\infty} N _ {n} e ^ {2 \pi i n z},
$$

where$N _ { n } = \# \{ x \in E _ { 8 } : | x | ^ { 2 } = 2 n \}$. In other words, the theta series is a generating function that counts the number of vectors of each length in$E _ { 8 }$

This theta series satisfies both functional equations:$\Theta _ { E _ { 8 } } ( z + 1 ) = \Theta _ { E _ { 8 } } ( z )$follows from the definition of$\Theta _ { E _ { 8 } }$as a Fourier series, while$\Theta _ { E _ { 8 } } ( - 1 / z ) = z ^ { 4 } \Theta _ { E _ { 8 } }$amounts to Poisson summation over$E _ { 8 }$for the complex Gaussian$x \mapsto e ^ { \pi i z | x | ^ { 2 } }$, which has eight-dimensional Fourier transform$y \mapsto z ^ { - 4 } e ^ { \pi i ( - 1 / z ) | y | ^ { 2 } }$. These functional equations tell us that$\Theta _ { E _ { 8 } }$is a modular form for$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$of weight 4, and it must therefore be proportional to$E _ { 4 }$. In fact,$\Theta _ { E _ { 8 } } = E _ { 4 }$, because$N _ { 0 } = 1$. Thus, we obtain the beautiful formula$2 4 0 \sigma _ { 3 } ( n )$) for the number of vectors in$E _ { 8 }$of squared norm 2�.

The theory ofmodular forms extends to other discrete groups, ifone carefully defines what being holomorphic at infinity means.3 Viazovska’s proof makes use of one more group,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">� |<sub>�</sub> �</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">SL<sub>2</sub> (Z)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>�</sub> ∈ SL<sub>2</sub> (Z)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">( � |<sub>� �</sub>) ( � )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(�|<sub>� �</sub>) (� + 1) =</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">( � |<sub>� �</sub>) ( � + �) = ( � |<sub>� �</sub>) ( � )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3If Γ is a subgroup of finite index in , then the condition is that for each , should be holomorphic at infinity. Note that �|<sub>�</sub> � need not satisfy, but one can check that it always satisfies for some positive integer � and thus has a Fourier expansion in .�<sup>2���/�</sup> = <sub>�</sub><sup>1/�</sup></span></small>

namely

$$
\Gamma (2) = \left\{\gamma \in \mathrm{SL} _ {2} (\mathbb {Z}): \gamma \equiv \left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right) \pmod {2} \right\},
$$

which has index 6 in$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$. If we let

$$
U (z) = \left(\sum_ {n \in \mathbb {Z}} e ^ {\pi i n ^ {2} z}\right) ^ {4},
$$

$W = U | _ { 2 } T$, and$V = U - W$, then �, �, and$W$are modular forms of weight 2 for$\Gamma ( 2 )$that satisfy$U = V + W$and

$$
\begin{array}{l l} U | _ {2} T = W, & V | _ {2} T = - V, \quad W | _ {2} T = U, \\ U | _ {2} S = - U, & V | _ {2} S = - W, \quad W | _ {2} S = - V. \end{array}\tag{3.3}
$$

These identities will play a key role in the construction of Viazovska’s magic function. It turns out that$U$and � generate the ring of modular forms for Γ(2), and therefore every modular form of weight 2� for Γ(2) is a linear combination of$U ^ { k } , U ^ { k - 1 } W , U ^ { k - 2 } W ^ { 2 }$ $W ^ { k }$

Because modular forms are so closely connected with lattices, it is natural to turn to modular forms when attempting to construct the magic functions. However, it is entirely unclear where we should even start, because modular forms are completely diferent sorts of objects from radial Schwartz functions. Figure 6 looks nothing whatsoever like Figures 4 or 5, and there is no familiar transformation that makes it look any more similar.

## 4. Viazovska’s construction for single roots

The first step in Viazovska’s construction of the magic function � is to split � into eigenfunctions of the Fourier transform. Radial functions satisfy${ \widehat { \widehat { f } } } \ = f$, and so we can write � as$f = f _ { + } + f _ { - }$, where$f _ { + } : = ( f + \widehat { f } ) / 2$satisfies$\widehat { f } _ { + } = f _ { + }$and$f _ { - } : = ( f - \widehat { f } ) / 2$satisfies $\widehat { f _ { - } } = - f _ { - }$. If � is the magic function in eight dimensions, then$f$and$\widehat { f }$both have roots at $\sqrt { 2 n }$for integers$n \geq 1$, and therefore$f _ { + }$and$f _ { - }$do as well. Thus, we are looking for radial Fourier eigenfunctions with specified roots. Specifically, each of$f _ { \pm }$should have a single root at$\sqrt { 2 }$and double roots at$\sqrt { 2 n }$for$n \geq 2$. These roots turn out to provide enough information to determine$f _ { \pm }$up to scaling, and they can then be combined to obtain$f .$

Before we construct the actual magic function, it is worth examining a simpler variant as a warm-up exercise. Instead of trying to control the behavior of$f$to second order at ${ \sqrt { 2 n } } .$, we will instead control the behavior of a function$g$to first order at${ \sqrt { n } } .$. This construction has no known applications to sphere packing, but it is nevertheless of intrinsic interest in Fourier analysis. We will also focus on the −1 eigenfunction (i.e., the case${ \widehat { g } } = - g )$in the single-root case, for the sake of specificity.

Viazovska found a remarkable integral transform that can construct such functions. We will write a radial function$g : \mathbb { R } ^ { 8 } \to \mathbb { C }$as a continuous linear combination of complex Gaussians$x \mapsto e ^ { \pi i z | x | ^ { 2 } }$with$z \in { \mathcal { H } }$via the contour integra

$$
g (x) = \frac {1}{2} \int_ {- 1} ^ {1} \psi (z) e ^ {\pi i z | x | ^ {2}} d z,\tag{4.1}
$$

where$\psi$is a holomorphic function on$\mathcal { H }$and the contour is a semicircle centered at the origin. Under which conditions on$\psi$will$g$be a Fourier eigenfunction, and how can we control its values at${ \sqrt { n } } ?$

We can obtain the values$g \left( { \sqrt { n } } \right)$by imposing periodicity on$\psi$as follows. Suppose $\psi ( z + 2 ) = \psi ( z )$for all$z \in \mathcal H$, so that$\psi$has a Fourier series of the form

$$
\psi (z) = \sum_ {n \in \mathbb {Z}} a _ {n} e ^ {\pi i n z}.\tag{4.2}
$$

Then for integers$n \geq 0$

$$
g (\sqrt {n}) = \frac {1}{2} \int_ {- 1} ^ {1} \psi (z) e ^ {\pi i n z} d z = a _ {- n}
$$

by orthogonality, provided that we can interchange the sum and integral. If the Fourier expansion (4.2) has only finitely many negative terms, then$g \left( { \sqrt { n } } \right)$will vanish for all but finitely many �.

To compute the Fourier transform of$g _ { : }$, we can interchange the contour integral and Fourier transform, again assuming the integral is suficiently well behaved. Then

$$
\widehat {g} (y) = \frac {1}{2} \int_ {- 1} ^ {1} \psi (z) z ^ {- 4} e ^ {\pi i (- 1 / z) | y | ^ {2}} d z,
$$

because the �-dimensional Fourier transform of the complex Gaussian$x \mapsto e ^ { \pi i z | x | ^ { 2 } }$with $z \in \mathcal H$is given by$y \mapsto ( i / z ) ^ { d / 2 } e ^ { \pi i ( - 1 / z ) | y | ^ { 2 } }$, and$d = 8$here. Changing variables to$u = - 1 / z$ shows that

$$
\widehat {g} (y) = - \frac {1}{2} \int_ {- 1} ^ {1} \psi (- 1 / u) u ^ {2} e ^ {\pi i u | y | ^ {2}} d u.
$$

In other words, taking the Fourier transform of$g$amounts to replacing$\psi$with$- \psi | _ { - 2 } S$, and we obtain${ \widehat { g } } = - g \ i f \psi | _ { - 2 } S = \psi$

Let Γ be the subgroup of${ \mathrm { S L } } _ { 2 } ( \mathbb { Z } )$generated by � and$T ^ { 2 }$, which has index 3 in ${ \mathrm { S L } } _ { 2 } ( \mathbb { Z } )$. Then the conditions that$\psi | _ { - 2 } T ^ { 2 } = \psi \ ( { \mathrm { i . e . , } } \psi ( z + 2 ) = \psi ( z ) )$) and$\psi | _ { - 2 } S = \psi$mean that$\psi$is weakly modular of weight −2 for Γ. The reason why$\psi$is less than a full-fledged modular form is that it is only meromorphic at infinity (this is unavoidable, since the weight is negative). We furthermore require$\psi$to vanish at ±1, which will be enough to justify our integral manipulations and show that$g$is a Schwartz function. In terms of Fourier series, this vanishing says that$\left| \psi \right| _ { - 2 } T S$has no negative terms in its$q \cdot$-series, because$T S$maps the cusp �∞ to 1.

We will construct an example of the form$\psi = \psi _ { 0 } / \Delta$using the$\Delta$function from (3.2), where$\psi _ { 0 }$is a genuine modular form of weight 10 for Γ. Note that the denominator of Δ causes no dificulties in$\mathcal { H } ,$, since$\Delta ( z ) \neq 0$for all$z \in \mathcal H$, and the zero of$\Delta$at infinity will lead to a pole of$\psi$.

The function$\psi _ { 0 }$is modular of weight 10 for Γ, and thus also for Γ(2) because$\Gamma ( 2 )$is a subgroup of Γ. In particular,$\psi _ { 0 }$must be a linear combination of$U ^ { 5 } , U ^ { 4 } W , U ^ { 3 } W ^ { 2 } , . . . , W ^ { 5 }$ because$U$and$W$generate the ring of modular forms for$\Gamma ( 2 )$. The relations (3.3) specify the action of$s$and �, and they imply that the subspace invariant under � is spanned by

$$
\begin{array}{l} \alpha := U ^ {5} - 6 U ^ {3} W ^ {2} + 4 U ^ {2} W ^ {3}, \\ \beta := U ^ {4} W - 3 U ^ {3} W ^ {2} + 2 U ^ {2} W ^ {3}, \text {and} \\ \gamma := - U ^ {3} W ^ {2} + 4 U ^ {2} W ^ {3} - 5 U W ^ {4} + 2 W ^ {5}, \end{array}
$$

with �-expansions

$$
\begin{array}{l l} \frac {\alpha}{\Delta} = - q ^ {- 1} - 4 0 q ^ {- 1 / 2} + 7 5 2 + \dots , & \quad \frac {\alpha}{\Delta} \Big | _ {- 2} T S = - 1 0 2 4 + 9 0 1 1 2 q + \dots , \\ \frac {\beta}{\Delta} = - 1 6 q ^ {- 1 / 2} + 2 5 6 + \dots , & \quad \frac {\beta}{\Delta} \Big | _ {- 2} T S = - 5 1 2 - 2 0 4 8 0 q + \dots , \\ \frac {\gamma}{\Delta} = 2 5 6 - 1 0 2 4 0 q ^ {1 / 2} + \dots , & \quad \frac {\gamma}{\Delta} \Big | _ {- 2} T S = - 2 q ^ {- 1} - 3 2 + \dots \end{array}
$$

in terms of$q ^ { 1 / 2 } = e ^ { \pi i z }$. Now requiring � to vanish at$\pm 1$determines it up to scaling as

$$
\psi = \frac {2 \beta - \alpha}{\Delta} = q ^ {- 1} + 8 q ^ {- 1 / 2} - 2 4 0 - 6 1 7 6 q ^ {1 / 2} - \dots ,\tag{4.3}
$$

which yields a radial Schwartz function$g : \mathbb { R } ^ { 8 } \to \mathbb { R }$such that${ \widehat { g } } = - g$and

$$
g \big (\sqrt {n} \big) = \left\{ \begin{array}{l l} - 2 4 0 & \text {if n = 0 ,} \\ 8 & \text {if n = 1 ,} \\ 1 & \text {if n = 2 , and} \\ 0 & \text {if n\geq 3 .} \end{array} \right.
$$

Note that we do not have much flexibility here: the values$g ( 0 ) , g ( 1 )$, and$g \big ( \sqrt { 2 } \big )$are uniquely determined by Poisson summation over$\mathbb { Z } ^ { 8 }$and$E _ { 8 }$, up to scaling.

We can rewrite the definition of$f$in another useful form as follows. If$| x |$is large enough (in fact,$| x | ^ { 2 } > 2$will sufice), then

$$
\begin{array}{l} g (x) = \frac {1}{2} \int_ {- 1} ^ {1} \psi (z) e ^ {\pi i z | x | ^ {2}} d z \\ \qquad = \frac {1}{2} \int_ {- 1} ^ {i} \psi (z) e ^ {\pi i z | x | ^ {2}} d z - \frac {1}{2} \int_ {1} ^ {i} \psi (z) e ^ {\pi i z | x | ^ {2}} d z \\ \qquad = \frac {1}{2} \int_ {- 1} ^ {- 1 + i \infty} \psi (z) e ^ {\pi i z | x | ^ {2}} d z - \frac {1}{2} \int_ {1} ^ {1 + i \infty} \psi (z) e ^ {\pi i z | x | ^ {2}} d z \\ \qquad = \frac {e ^ {- \pi i | x | ^ {2}} - e ^ {\pi i | x | ^ {2}}}{2} \int_ {0} ^ {i \infty} \psi (u + 1) e ^ {\pi i u | x | ^ {2}} d u. \end{array}
$$

In these manipulations, the second line merely breaks the integral in two, the third line uses the fact that 1 + i B

$$
\int_ {- 1 + i R} ^ {1 + i R} \psi (z) e ^ {\pi i z | x | ^ {2}} d z \to 0
$$

as$R \to \infty$(which holds if$| x | ^ { 2 }$is large enough), and the fourth line uses$\psi ( u - 1 ) = \psi ( u + 1 )$

In other words,$g ( x )$is given by si$( \pi | x | ^ { 2 } )$times the Laplace transform of$t \mapsto$ $\psi ( i t + 1 )$evaluated at$\pi | x | ^ { 2 }$:

$$
g (x) = \sin (\pi | x | ^ {2}) \int_ {0} ^ {\infty} \psi (i t + 1) e ^ {- \pi t | x | ^ {2}} d t.\tag{4.4}
$$

While the original integral (4.1) converges for all$x ,$, this integral converges only when$| x | ^ { 2 }$is large enough for the Gaussian factor$e ^ { - \pi t | x | ^ { 2 } }$to counteract the growth of$\psi ( i t + 1 )$as$t \to \infty$ In particular, (4.3) implies that

$$
\psi (i t + 1) = e ^ {2 \pi t} - 8 e ^ {\pi t} - 2 4 0 + 6 1 7 6 e ^ {- \pi t} - \dots
$$

as$t \to \infty$, which means we need$| x | ^ { 2 } > 2$. We can use this expansion to analytically continue $g$by removing the divergent terms:

$$
\begin{array}{l} g (x) = \sin (\pi | x | ^ {2}) \int_ {0} ^ {\infty} (e ^ {2 \pi t} - 8 e ^ {\pi t} - 2 4 0) e ^ {- \pi t | x | ^ {2}} d t \\ \qquad + \sin (\pi | x | ^ {2}) \int_ {0} ^ {\infty} (\psi (i t + 1) - e ^ {2 \pi t} + 8 e ^ {\pi t} + 2 4 0) e ^ {- \pi t | x | ^ {2}} d t \\ \qquad = \frac {\sin (\pi | x | ^ {2})}{\pi (| x | ^ {2} - 2)} - \frac {8 \sin (\pi | x | ^ {2})}{\pi (| x | ^ {2} - 1)} - \frac {2 4 0 \sin (\pi | x | ^ {2})}{\pi | x | ^ {2}} \\ \qquad + \sin (\pi | x | ^ {2}) \int_ {0} ^ {\infty} (\psi (i t + 1) - e ^ {2 \pi t} + 8 e ^ {\pi t} + 2 4 0) e ^ {- \pi t | x | ^ {2}} d t, \end{array}
$$

and this last formula holds regardless of$| x |$, with removable singularities at$| x | = 0 , 1$, and $\sqrt { 2 }$

## 5. Viazovska’s construction for double roots

We are now in a position to obtain the magic function in eight dimensions. First, we will obtain the −1 eigenfunction$f _ { - }$. It is not immediately clear how to generalize the contour integral (4.1) from single to double roots, but the Laplace transform formula (4.4) generalizes elegantly. To obtain$f _ { - }$, we will look for a special function$\psi$such that

$$
f _ {-} (x) = - 4 i \sin (\pi | x | ^ {2} / 2) ^ {2} \int_ {0} ^ {i \infty} \psi (z) e ^ {\pi i z | x | ^ {2}} d z
$$

when$| x |$is large enough. If we write −4 sin$( \pi | x | ^ { 2 } / 2 ) ^ { 2 } = e ^ { - \pi i | x | ^ { 2 } } + e ^ { \pi i | x | ^ { 2 } } - 2$, we find that

$$
\begin{array}{c} f _ {-} (x) = \int_ {- 1} ^ {- 1 + i \infty} \psi (z + 1) e ^ {\pi i | x | ^ {2} z} d z + \int_ {1} ^ {1 + i \infty} \psi (z - 1) e ^ {\pi i | x | ^ {2} z} d z \\ - 2 \int_ {0} ^ {i \infty} \psi (z) e ^ {\pi i | x | ^ {2} z} d z. \end{array}
$$

We will construct a function$\psi$such that$\psi$is holomorphic on$\mathcal { H }$and$\psi ( z )$is exponentially bounded as Im$z \to \infty$. Under these conditions, when$| x |$is suficiently large we can shift the contours and combine the integrals to obtain

$$
\begin{array}{r l} & f _ {-} (x) = \int_ {- 1} ^ {i} \psi (z + 1) e ^ {\pi i | x | ^ {2} z} d z + \int_ {1} ^ {i} \psi (z - 1) e ^ {\pi i | x | ^ {2} z} d z \\ & \qquad - 2 \int_ {0} ^ {i} \psi (z) e ^ {\pi i | x | ^ {2} z} d z + \int_ {i} ^ {i \infty} \big (\psi (z + 1) + \psi (z - 1) - 2 \psi (z) \big) e ^ {\pi i | x | ^ {2} z} d z, \end{array}
$$

with the contours shown in Figure 7. This formula will be the analogue of (4.1), and it will define$f _ { - } ( x )$for all$x .$.

![](images/page_16_image_0.jpg)

Figure 7

The contours used to obtain � (�), labeled with their integrands (omitting$e ^ { \pi i | x | ^ { 2 } z } d z )$

Taking the Fourier transform amounts to replacing$e ^ { \pi i | x | ^ { 2 } z }$with$z ^ { - 4 } e ^ { \pi i | y | ^ { 2 } ( - 1 / z ) }$in the formula defining$f _ { - }$:

$$
\begin{array}{l} \widehat {f _ {-}} (y) = \int_ {- 1} ^ {i} \psi (z + 1) z ^ {- 4} e ^ {\pi i | y | ^ {2} (- 1 / z)} d z + \int_ {1} ^ {i} \psi (z - 1) z ^ {- 4} e ^ {\pi i | y | ^ {2} (- 1 / z)} d z \\ \qquad - 2 \int_ {0} ^ {i} \psi (z) z ^ {- 4} e ^ {\pi i | y | ^ {2} (- 1 / z)} d z \\ \qquad + \int_ {i} ^ {i \infty} \big (\psi (z + 1) + \psi (z - 1) - 2 \psi (z) \big) z ^ {- 4} e ^ {\pi i | y | ^ {2} (- 1 / z)} d z. \end{array}
$$

We can now set$u = - 1 / z ,$, which exchanges the four contours in pairs. The simplest way to obtain$\widehat { f _ { - } } = - f _ { - }$would be if the resulting formula is exactly the negative of the formula with which we began. That amounts to the functional equations

$$
\psi | _ {- 2} T S = - \psi | _ {- 2} T ^ {- 1}
$$

and

$$
2 \psi | _ {- 2} S = 2 \psi - \psi | _ {- 2} T - \psi | _ {- 2} T ^ {- 1}.
$$

Note that the structure of these equations reflects the integrands.

Now the question is which sorts of functions$\psi$satisfy these functional equations. The simplest possibility would be some sort of modular form. The functional equations are not consistent with invariance under � and$T _ { \ast }$, and so$\psi$cannot be modular for the full group $\mathrm { S L } _ { 2 } ( \mathbb { Z } )$. Let us suppose instead that$\psi$is weakly modular of weight −2 for Γ(2) (i.e., invariant under Γ(2) but only meromorphic at infinity). Then$\psi | _ { - 2 } T = \psi | _ { - 2 } T ^ { - 1 }$, because$T ^ { 2 } \in \Gamma ( 2 )$, and our functional equations become$\psi | _ { - 2 } T S = - \psi | _ { - 2 } T$and$\psi = \psi \vert _ { - 2 } T + \psi \vert _ { - 2 } S$. Furthermore, the second equation implies the first, because$S ^ { 2 } = I .$. We will therefore obtain the eigenfunction equation${ \widehat { f _ { - } } } = - f _ { - }$as long as$\psi$is weakly modular of weight −2 for Γ(2) and satisfies$\psi =$ $\psi | _ { - 2 } T + \psi | _ { - 2 } S$

As in the single-root case, it is natural to multiply$\psi$by$\Delta$to try to eliminate a pole at infinity. Then �Δ will be a genuine modular form of weight 10 for$\Gamma ( 2 )$, and thus a linear combination of$U ^ { 5 } , U ^ { 4 } W , U ^ { 3 } W ^ { 2 } , \dots , W ^ { 5 }$. One can check that the solutions of the remaining functional equation form a two-dimensional subspace, spanned b

$$
\alpha := 2 U ^ {4} W - 4 U ^ {3} W ^ {2} + U ^ {2} W ^ {3} + U W ^ {4} \quad \text {and} \quad \beta := 5 U ^ {4} W - 1 0 U ^ {3} W ^ {2} + 5 U ^ {2} W ^ {3} + W ^ {5},
$$

with

$$
\frac {\alpha}{\Delta} = - 1 6 q ^ {- 1 / 2} + 7 6 8 + \dots \quad \text { and } \quad \frac {\beta}{\Delta} = q ^ {- 1} - 4 0 q ^ {- 1 / 2} + 2 0 6 4 + \dots .
$$

We will take

$$
\psi = \frac {- 5 \alpha + 2 \beta}{\Delta} = 2 q ^ {- 1} + 2 8 8 + \dots ,
$$

so that we eliminate the$q ^ { - 1 / 2 }$term in the$q { \mathrm { - s e r i e s } }$. The motivation for eliminating that term is that it prevents$f _ { - }$from having a pole at radius 1. To see why, let us analytically continue

$$
f _ {-} (x) = 4 \sin (\pi | x | ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} \psi (i t) e ^ {- \pi t | x | ^ {2}} d t
$$

as in the single-root case. If$\psi ( i t ) = a _ { 2 } e ^ { 2 \pi t } + a _ { 1 } e ^ { \pi t } + a _ { 0 } + \cdot \cdot \cdot \mathrm {  ~ \ a s \ } t \to \infty ,$, then

$$
\begin{array}{l} f _ {-} (x) = \frac {4 a _ {2} \sin (\pi | x | ^ {2} / 2) ^ {2}}{\pi (| x | ^ {2} - 2)} - \frac {4 a _ {1} \sin (\pi | x | ^ {2} / 2) ^ {2}}{\pi (| x | ^ {2} - 1)} - \frac {4 a _ {0} \sin (\pi | x | ^ {2} / 2) ^ {2}}{\pi | x | ^ {2}} \\ \qquad + 4 \sin (\pi | x | ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} (\psi (i t) - a _ {2} e ^ {2 \pi t} - a _ {1} e ^ {\pi t} - a _ {0}) e ^ {- \pi t | x | ^ {2}} d t. \end{array}
$$

Here the$a _ { 1 }$term has a pole unless$a _ { 1 } = 0$. For our choice of$\psi , ( a _ { 2 } , a _ { 1 } , a _ { 0 } ) = ( 2 , 0 , 2 8 8 )$, and thus$f _ { - }$has a single root at$\sqrt { 2 }$and double roots at$\sqrt { 2 n }$for$n \geq 2$. One can also check that $\psi ( i t )$vanishes as$t  0 +$(equivalently,$\left. \psi \right| _ { - 2 } S$vanishes at infinity), which is enough for$f _ { - }$ to be a Schwartz function and to justify all our integral manipulations.

We have therefore obtained a magic eigenfunction$f _ { - }$as

$$
f _ {-} (x) = 4 \sin (\pi | x | ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} \psi (i t) e ^ {- \pi t | x | ^ {2}} d t
$$

for$| x | ^ { 2 } > 2$, where

$$
\psi = \frac {W ^ {3} (5 U ^ {2} - 5 U W + 2 W ^ {2})}{\Delta}.\tag{5.1}
$$

Our scaling here does not yet match the magic function for sphere packing, but aside from that we have exactly what we need.

Equation (5.1) implies that$\psi ( i t ) > 0$for all$t \in ( 0 , \infty )$). (Specifically,$\Delta ( i t ) > 0$ thanks to its product formula,$W ( i t ) > 0$since it is the fourth power of a real quantity, and $5 U ( i t ) ^ { 2 } - 5 U ( i t ) W ( i t ) + 2 W ( i t ) ^ { 2 } > 0$since it is a positive-definite quadratic form.) It follows that$f _ { - }$never changes sign beyond radius${ \sqrt { 2 } } ,$, in accordance with our expectations. However, note that our eigenfunction is positive beyond radius${ \sqrt { 2 } } ,$, and so we will have to correct its sign later to match the magic function.

All that remains is to construct a magic eigenfunction$f _ { + }$and take a suitable linear combination of$f _ { + }$and$f _ { - }$to obtain$f .$Constructing$f _ { + }$is very much like constructing$f _ { - }$. If we define$f _ { + }$for$| x |$suficiently large by

$$
f _ {+} (x) = - 4 i \sin (\pi | x | ^ {2} / 2) ^ {2} \int_ {0} ^ {i \infty} \phi (z) e ^ {\pi i z | x | ^ {2}} d z
$$

for some holomorphic function$\phi \colon { \mathcal { H } } \to \mathbb { C }$, then the eigenfunction equation${ \widehat { f } } _ { + } = f _ { + }$will follow from the functional equations

$$
\phi | _ {- 2} T S = \phi | _ {- 2} T ^ {- 1}
$$

and

$$
2 \phi | _ {- 2} S = - 2 \phi + \phi | _ {- 2} T + \phi | _ {- 2} T ^ {- 1}.
$$

These are the same functional equations as we required for$\psi$, except for a factor of −1.

A little manipulation using$( S T ) ^ { 3 } = I$shows that the first functional equation is equivalent to$\phi | _ { - 2 } S T = \phi | _ { - 2 } S$. Thus, if we set$\chi : = \phi | _ { - 2 } S$, then$\chi$must be invariant under �. However, the second functional equation is more subtle. A short calculation shows that ${ \mathrm { i f ~ } } \chi | _ { 0 } S = \chi$(equivalently,$( \chi | \lrcorner S ) ( z ) = z ^ { 2 } \chi ( z ) )$, then the second functional equation holds. In other words, it is enough for$\chi$to be weakly modular of weight 0 for$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$. However, such functions turn out not to be suficient to obtain$f _ { + }$. If one tries to solve for undetermined coeficients to construct$f _ { + }$, as in the$f _ { - }$case, one finds that there is no solution with the needed properties.

Instead, we can use quasimodular forms, not just modular forms. Recall that the Eisenstein series$E _ { 2 }$was not a modular form of weight 2, because conditional convergence interfered with the series manipulations needed to prove modularity. If we let

$$
E _ {2} (z) = 1 - 2 4 \sum_ {n \geq 1} \sigma_ {1} (n) q ^ {n},
$$

then$E _ { 2 }$turns out to satisfy

$$
z ^ {- 2} E _ {2} (- 1 / z) = E _ {2} (z) - \frac {6 i}{\pi z},
$$

with the$6 i / ( \pi z )$term amounting to the deviation from modularity. A quasimodularform of weight � and depth ℓ for${ \mathrm { S L } } _ { 2 } ( \mathbb { Z } )$is a sum$f _ { k } + f _ { k - 2 } E _ { 2 } + \cdot \cdot \cdot + f _ { k - \ell } E _ { 2 } ^ { \ell }$, where each$f _ { j }$is a modular form of weight$k - 2 j$

Instead of just a weakly modular form of weight 0, one can check that the function $\chi$can be a weakly quasimodular form of weight 0 and depth 2 for$\mathrm { S L } _ { 2 } ( \mathbb { Z } )$. Now we have enough flexibility to construct$f _ { + }$, and calculations much like those in the$f _ { - }$case lead to

$$
\chi = \frac {(E _ {2} E _ {4} - E _ {6}) ^ {2}}{\Delta},
$$

up to scaling. See Figure 8 for plots of the quasimodular forms that yield$f _ { - }$and$f _ { + }$.

Now that we have obtained both magic eigenfunctions, we can construct the magic function$f$as a linear combination of them. First, we rescale$\phi$so that$f _ { + } ( 0 ) = 1$, and then we rescale$\psi$so that$f _ { - } ^ { \prime } \left( \sqrt { 2 } \right) = f _ { + } ^ { \prime } \left( \sqrt { 2 } \right)$, to obtain a double root at$\sqrt { 2 }$for${ \widehat { f } } .$. Using these scalings, the eight-dimensional magic function is given by

$$
f (x) = 4 \sin (\pi | x | ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} (\phi (i t) + \psi (i t)) e ^ {- \pi t | x | ^ {2}} d t
$$

for$| x | ^ { 2 } > 2$, and the eigenfunction property implies that

$$
\widehat {f} (y) = 4 \sin (\pi | y | ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} (\phi (i t) - \psi (i t)) e ^ {- \pi t | y | ^ {2}} d t
$$

![](images/page_19_image_0.jpg)

![](images/page_19_image_1.jpg)

Figure 8

Plots of$\psi ( z ) \Delta ( z )$(above) and$\left( \varphi | _ { - 2 } S \right) ( z ) \Delta ( z )$) (below) for$- 1 \leq \mathsf { R e } z \leq 1$and$0 < \operatorname { I m } z \leq 1$

for all$y \neq 0$(this integral turns out to converge whenever$| y | > 0$, because the exponentia growth in$\phi ( i t )$and$\psi ( i t )$as � → ∞ cancels).

The final step in the proof of Theorem 1.1 is to check the inequalities that are needed for Theorem 2.1, namely$f ( x ) \leq 0$for$| x | \geq 2$and${ \widehat { f } } ( y ) \geq 0$for all , to make sure there are no unexpected sign changes between the roots${ \sqrt { 2 n } } .$. In principle that might seem dificult, because integral transforms of quasimodular forms could be complicated. However, these inequalities hold for the simplest reason one could hope for:

$$
\phi (i t) + \psi (i t) <   0 \quad \mathrm{and} \quad \phi (i t) - \psi (i t) > 0
$$

for all$t > 0$. In other words, the desired inequalities hold directly at the level of the quasimodular forms themselves. This can be checked rigorously in any of several ways. For example, one can use asymptotics to check the inequalities as$t \to 0 \mathrm { o r } t \to \infty$, and then use interva arithmetic to verify them on the remaining bounded interval.

Overall, this proof feels like a miracle. Everything falls beautifully into place, with Viazovska’s constructions having just enough flexibility to complete the proof in a unique way. What I find most impressive is the number of ingenious ideas required for the full proof. The single-root construction is itself remarkable, generalizing it to$f _ { - }$is even more so, and still more ideas are required for$f _ { + }$. Viazovska is a master of special functions, whose work would surely have excited Jacobi and Ramanujan.

## 6. Interpolation and consequences

Along the way to proving the optimality of$E _ { 8 }$, Viazovska made the bold conjecture that the magic function is uniquely determined by its required roots, and that more generally a radial Schwartz function on$\mathbb { R } ^ { 8 }$is uniquely determined by its values and radial derivatives at the radii$\sqrt { 2 n }$and those of its Fourier transform. It is far from obvious that it is possible in principle to reconstruct a radial Schwartz function from discrete data of this sort.

Radchenko and Viazovska took a major step in this direction by proving a onedimensional analogue for first-order interpolation, and the second-order theorem was proved by Cohn, Kumar, Miller, Radchenko, and Viazovska.

Theorem 6.1 (Radchenko and Viazovska [23]). There exist Schwartz functions$a _ { n } \colon \mathbb { R } \to \mathbb { R }$ such thatfor every Schwartzfunction$f \colon \mathbb { R } \to$R and$x \in \mathbb { R }$,

$$
f (x) = \sum_ {n \in \mathbb {Z}} f (\sqrt {n}) a _ {n} (x) + \sum_ {n \in \mathbb {Z}} \widehat {f} (\sqrt {n}) \widehat {a} _ {n} (x).
$$

Theorem 6.2 (Cohn, Kumar, Miller, Radchenko, and Viazovska [11]). Let$( d , n _ { 0 } )$) be$( 8 , 1 )$ or (24, 2). Then every radial Schwartz function$f \colon  { \mathbb { R } ^ { d } } \to  { \mathbb { R } }$is uniquely determined by the values$f ( { \sqrt { 2 n } } ) , f ^ { \prime } ( { \sqrt { 2 n } } ) , { \widehat { f } } ( { \sqrt { 2 n } } )$, and${ \widehat { f } } ^ { \prime } ( { \sqrt { 2 n } } )$for integers$n \geq n _ { 0 }$. Specifically, there exists an interpolation basis$a _ { n } , b _ { n } f o r n \ge n _ { 0 }$such thatfor every radial Schwartzfunction � and $\boldsymbol { x } \in \mathbb { R } ^ { d }$

$$
\begin{array}{l} f (x) = \sum_ {n = n _ {0}} ^ {\infty} f (\sqrt {2 n}) a _ {n} (x) + \sum_ {n = n _ {0}} ^ {\infty} f ^ {\prime} (\sqrt {2 n}) b _ {n} (x) \\ \qquad + \sum_ {n = n _ {0}} ^ {\infty} \widehat {f} (\sqrt {2 n}) \widehat {a} _ {n} (x) + \sum_ {n = n _ {0}} ^ {\infty} \widehat {f} ^ {\prime} (\sqrt {2 n}) \widehat {b} _ {n} (x). \end{array}
$$

The proofs construct the interpolation bases explicitly, by combining Viazovska’s integral transform techniques with broader classes of special functions.

One consequence of radial Fourier interpolation is a stronger optimality theorem for$E _ { 8 }$and the Leech lattice. Instead of just taking into account local interactions between particles, as in the sphere packing problem, one can study optimization problems with longrange interactions. For example, one could ask for the ground state of particles interacting via an inverse power law. Cohn and Kumar [9] formulated a broad notion of optimality, called universal optimality, and radial Fourier interpolation yields corresponding magic functions:

Theorem 6.3 (Cohn, Kumar, Miller, Radchenko, and Viazovska [11]). The$E _ { 8 }$root lattice and the Leech lattice are universally optimal in$\mathbb { R } ^ { 8 }$and$\mathbb { R } ^ { 2 4 }$, respectively.

## 7. The future

Although Viazovska’s work has settled several major questions, much remains to be understood. For example, the theory of interpolation for radial Schwartz functions is rapidly developing, with noteworthy connections to uniqueness theory for the Klein-Gordon equation [2].

One puzzling issue is two dimensions. While the two-dimensional sphere packing problem can be settled by elementary geometry, universal optimality remains a tantalizing conjecture. There seems to be a magic function for$d = 2$in Theorem 2.1, with$r = ( 4 / 3 ) ^ { 1 / 4 }$; no proof is known, but numerical computations agree with the optimal packing density in $\mathbb { R } ^ { 2 }$to over one thousand decimal places. Furthermore, analogous magic functions seem to exist for universal optimality in$\mathbb { R } ^ { 2 }$. However, it is unclear what sort of function space might allow a suitable interpolation theory (see Section 7 in [11]).

There are also remarkable connections with conformal field theory and quantum gravity [18]. When � is even, the linear programming bound for the sphere packing density in $\mathbb { R } ^ { d }$turns out to be equivalent to the spinless modular bootstrap bound for the spectral gap in a theory of$d / 2$free bosons, and the conformal bootstrap program generalizes it to a family of related bounds. How these more general bounds might relate to discrete geometry remains a mystery.

## References

[1]N. Afkhami-Jeddi, H. Cohn, T. Hartman, D. de Laat, and A. Tajdini, Highdimensional sphere packing and the modular bootstrap, J. High Energy Phys. 2020 (2020), no. 12, Paper No. 066, 44 pp. arXiv:2006.02560 doi:10.1007/jhep12(2020)066

[2]A. Bakan, H. Hedenmalm, A. Montes-Rodríguez, D. Radchenko, and M. Viazovska, Fourier uniqueness in even dimensions, Proc. Natl. Acad. Sci. USA 118 (2021), no. 15, Paper No. 2023227118, 4 pp. doi:10.1073/pnas.2023227118

[3]A. Bondarenko, D. Radchenko, and M. Viazovska, Optimal asymptotic boundsfor spherical designs, Ann. of Math. (2) 178 (2013), no. 2, 443–452. arXiv:1009.4407 doi:10.4007/annals.2013.178.2.2

[4]J. Bourgain, L. Clozel, and J.-P. Kahane, Principe d’Heisenberg etfonctions posi tives, Ann. Inst. Fourier (Grenoble) 60 (2010), no. 4, 1215–1232. arXiv:0811.4360 doi:10.5802/aif.2552

[5]H. Cohen and F. Strömberg, Modular Forms: A Classical Approach, Graduate Studies in Mathematics 179, American Mathematical Society, Providence, RI, 2017.

[6]H. Cohn, A conceptual breakthrough in sphere packing, Notices Amer. Math. Soc 64 (2017), no. 2, 102–115. arXiv:1611.01685 doi:10.1090/noti1474

[7]H. Cohn and N. Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157 (2003), no. 2, 689–714. arXiv:math/0110009

[8]H. Cohn and F. Gonçalves, An optimal uncertainty principle in twelve dimensions via modularforms, Invent. Math. 217 (2019), no. 3, 799–831. arXiv:1712.04438 doi:10.1007/s00222-019-00875-4

[9]H. Cohn and A. Kumar, Universally optimal distribution ofpoints on spheres, J. Amer. Math. Soc. 20 (2007), no. 1, 99–148. arXiv:math/0607446 doi:10.1090/S0894-0347-06-00546-7

[10]H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24, Ann. of Math. (2) 185 (2017), no. 3, 1017–1033. arXiv:1603.06518 doi:10.4007/annals.2017.185.3.8

[11]H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, Universal optimality ofthe$E _ { 8 }$and Leech lattices and interpolationformulas, Annals of Mathematics, to appear. arXiv:1902.05438

[12] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, third edition, Grundlehren der Mathematischen Wissenschaften 290, Springer-Verlag, New York, 1999. doi:10.1007/978-1-4757-6568-7

[13] P. Delsarte, Boundsfor unrestricted codes, by linear programming, Philips Res. Rep. 27 (1972), 272–289.

[14]F. Diamond and J. Shurman, A First Course in Modular Forms, Graduate Texts in Mathematics 228, Springer-Verlag, New York, 2005. doi:10.1007/978-0-387-27226-9

[15]W. Ebeling, Lattices and Codes: A Course Partially Based on Lectures by Friedrich Hirzebruch, third edition, Advanced Lectures in Mathematics. Springer Spektrum, Wiesbaden, 2013. doi:10.1007/978-3-658-00360-9

[16]T. C. Hales, A proofofthe Kepler conjecture, Ann. of Math. (2) 162 (2005), no. 3, 1065–1185. doi:10.4007/annals.2005.162.1065

[17]T. Hales, M. Adams, G. Bauer, T. D. Dang, J. Harrison, L. T. Hoang, C. Kaliszyk, V. Magron, S. McLaughlin, T. T. Nguyen, Q. T. Nguyen, T. Nipkow, S. Obua, J. Pleso, J. Rute, A. Solovyev, T. H. A. Ta, N. T. Tran, T. D. Trieu, J. Urban, K. Vu, and R. Zumkeller, Aformal proofofthe Kepler conjecture, Forum Math. Pi 5 (2017), e2, 29 pp. arXiv:1501.02155 doi:10.1017/fmp.2017.1

[18]T. Hartman, D. Mazáč, and L. Rastelli, Sphere packing and quantum gravity, J. High Energy Phys. 2019 (2019), no. 12, 048, 66 pp. arXiv:1905.01319 doi:10.1007/jhep12(2019)048

[19]E. Klarreich, Sphere packing solved in higher dimensions, Quanta Magazine, March 30, 2016. https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/

[20] D. de Laat and F. Vallentin, A breakthrough in sphere packing: the search for magicfunctions, Nieuw Arch. Wiskd. (5) 17 (2016), no. 3, 184–192. arXiv:1607.02111

[21]D. Lowry-Duda, Visualizing modularforms, in Arithmetic Geometry, Number Theory, and Computation (J. S. Balakrishnan, N. Elkies, B. Hassett, B. Poonen, A. V. Sutherland, and J. Voight, eds.), Simons Symposia, Springer, 2021. arXiv:2002.05234 doi:10.1007/978-3-030-80914-0\_19

[22]D. Madore, Sections du diagramme de Voronoï du réseau � , David Madore’s WebLog, April 9, 2017. http://www.madore.org/\~david/weblog/d.2017-04-09.2433.html

[23]D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Études Sci. 129 (2019), 51–81. arXiv:1701.00265 doi:10.1007/s10240-018-0101-z

[24] J.-P. Serre, A Course in Arithmetic, Graduate Texts in Mathematics 7, Springer-Verlag, New York-Heidelberg, 1973. doi:10.1007/978-1-4684-9884-4

[25]T. M. Thompson, From Error-correcting Codes through Sphere Packings to Simple Groups, Carus Mathematical Monographs 21, Mathematical Association of America, Washington, DC, 1983.

[26] A. Thue, Om nogle geometrisk-taltheoretiske Theoremer, Forhandlingerne ved de Skandinaviske Naturforskeres 14 (1892), 352–353.

[27]M. S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. (2) 185 (2017), no. 3, 991–1015. arXiv:1603.04246 doi:10.4007/annals.2017.185.3.7

[28] D. Zagier, Elliptic modularforms and their applications, in The 1–2–3 ofMod ular Forms (K. Ranestad, ed.), pp. 1–103, Universitext, Springer, Berlin, 2008. doi:10.1007/978-3-540-74119-0\_1

## Henry Cohn

Microsoft Research New England, One Memorial Drive, Cambridge, MA 02140, USA, cohn@microsoft.com