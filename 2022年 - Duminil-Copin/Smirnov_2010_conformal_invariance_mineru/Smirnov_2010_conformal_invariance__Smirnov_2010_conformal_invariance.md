# Conformal invariance of lattice models

Hugo Duminil-Copin and Stanislav Smirnov

November 27, 2024

## Abstract

These lecture notes provide an (almost) self-contained account on conformal invariance of the planar critical Ising and FK-Ising models. They present the theory of discrete holomorphic functions and its applications to planar statistical physics (more precisely to the convergence of fermionic observables). Convergence to SLE is discussed briefly. Many open questions are included.

## Contents

1 Introduction 2
1.1 Organization of the notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2 Two-dimensional Ising model 8
2.1 Boundary conditions, infinite-volume measures and phase transition . . 8
2.2 Low and high temperature expansions of the Ising model. 10
2.3 Spin-Dobrushin domain, fermionic observable and results on the Ising model 13
3 Two-dimensional FK-Ising model 15
3.1 FK percolation 15
3.2 FK-Ising model and Edwards-Sokal coupling 18
3.3 Loop representation of the FK-Ising model and fermionic observable 20
4 Discrete complex analysis on graphs 24
4.1 Preharmonic functions. 25
4.2 Preholomorphic functions. 30
4.3 Isaacs's definition of preholomorphic functions 30
4.4 s-holomorphic functions. 31
4.5 Isoradial graphs and circle packings. 34
5 Convergence of fermionic observables 35
5.1 Convergence of the FK fermionic observable 35
5.2 Convergence of the spin fermionic observable 41
6 Convergence to chordal SLE(3) and chordal SLE(16/3) 43
6.1 Tightness of interfaces for the FK-Ising model 44
6.2 sub-sequential limits of FK-Ising interfaces are Loewner chains 46
6.3 Convergence of FK-Ising interfaces to SLE(16/3). 47
6.4 Convergence to SLE(3) for spin Ising interfaces 49

7 Other results on the Ising and FK-Ising models 49  
7.1 Massive harmonicity away from criticality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
7.2 Russo-Seymour-Welsh Theorem for FK-Ising . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53  
7.3 Discrete singularities and energy density of the Ising model 55  
8 Many questions and a few answers 56  
8.1 Universality of the Ising model 56  
8.2 Full scaling limit of critical Ising model 58  
8.3 FK percolation for general cluster-weight $q\geq 0$ 58  
8.4 $O(n)$ models on the hexagonal lattice 60  
8.5 Discrete observables in other models 63

## 1 Introduction

The celebrated Lenz-Ising model is one of the simplest models of statistical physics exhibiting an order-disorder transition. It was introduced by Lenz in [Len20] as an attempt to explain Curie’s temperature for ferromagnets. In the model, iron is modeled as a collection of atoms with fixed positions on a crystalline lattice. Each atom has a magnetic spin, pointing in one of two possible directions. We will set the spin to be equal to 1 or 1. Each configuration of spins has an intrinsic energy, which takes into account −the fact that neighboring sites prefer to be aligned (meaning that they have the same spin), exactly like magnets tend to attract or repel each other. Fix a box$\Lambda \subset \mathbb { Z } ^ { 2 }$of size n. Let$\sigma \in \{ - 1 , 1 \} ^ { \Lambda }$⊂be a configuration of spins 1 or 1. The energy of the configuration ∈ {− }σ is given by the Hamiltonian

$$
E _ {\Lambda} (\sigma) := - \sum_ {x \sim y} \sigma_ {x} \sigma_ {y}
$$

where$x \sim y$means that$x$and$y$are neighbors in Λ. The energy is, up to an additive ∼constant, twice the number of disagreeing neighbors. Following a fundamental principle of physics, the spin-configuration is sampled proportionally to its Boltzmann weight: at an inverse-temperature$\beta ,$, the probability$\mu _ { \beta , \Lambda }$of a configuration σ satisfies

$$
\mu_ {\beta , \Lambda} (\sigma) := \frac {\mathrm{e} ^ {- \beta E _ {\Lambda} (\sigma)}}{Z _ {\beta , \Lambda}}
$$

where

$$
Z _ {\beta , \Lambda} := \sum_ {\tilde {\sigma} \in \{- 1, 1 \} ^ {\Lambda}} \mathrm{e} ^ {- \beta E _ {\Lambda} (\tilde {\sigma})}
$$

is the so-called partition function defined in such a way that the sum of the weights over all possible configurations equals 1. Above a certain critical inverse-temperature$\beta _ { c } ,$ the model has a spontaneous magnetization while below$\beta _ { c }$does not (this phenomenon will be described in more detail in the next section). When$\beta _ { c }$lies strictly between 0 and , the Ising model is said to undergo a phase transition between an ordered and ∞a disordered phase. The fundamental question is to study the phase transition between the two regimes.

Lenz’s student Ising proved the absence of phase transition in dimension one (meaning$\beta _ { c } = \infty )$in his PhD thesis [Isi25], wrongly conjecturing the same picture in higher = ∞dimensions. This belief was widely shared, and motivated Heisenberg to introduce his famous model [Hei28]. However, some years later Peierls [Pei36] used estimates on the length of interfaces between spin clusters to disprove the conjecture, showing a phase transition in the two-dimensional case. Later, Kramers and Wannier [KW41a, KW41b] derived nonrigorously the value of the critical temperature.

![](images/page_2_image_0.jpg)

Figure 1: Ising configurations at$\beta < \beta _ { c }$, at$\beta = \beta _ { c } .$, and$\beta > \beta _ { c }$respectively.

In 1944, Onsager [Ons44] computed the partition function of the model, followed by further computations with Kaufman, see [KO50] for instance<sup>1</sup>. In the physical approach to statistical models, the computation of the partition function is the first step towards a deep understanding of the model, enabling for instance the computation of the free energy. The formula provided by Onsager led to an explosion in the number of results on the 2D Ising model (papers published on the Ising model can now be counted in the thousands). Among the most noteworthy results, Yang derived rigorously the spontaneous magnetization [Yan52] (the result was derived nonrigorously by Onsager himself). McCoy and Wu [MW73] computed many important quantities of the Ising model, including several critical exponents, culminating with the derivation of two-point correlations between sites 0, 0 and$( n , n )$in the whole plane. See the more recent book of Palmer ( ) ( )for an exposition of these and other results [Pal07].

The computation of the partition function was accomplished later by several other methods and the model became the most prominent example of an exactly solvable model. The most classical techniques include the transfer-matrices technique developed by Lieb and Baxter [Lie67, Bax89], the Pfafian method, initiated by Fisher and Kasteleyn, using a connection with dimer models [Fis66, Kas61], and the combinatorial approach to the Ising model, initiated by Kac and Ward [KW52] and then developed by Sherman [She60] and Vdovichenko [Vdo65]; see also the more recent [DZM+99, Cim10].

Despite the number of results that can be obtained using the partition function, the impossibility of computing it explicitly enough in finite volume made the geometric study of the model very hard to perform while using the classical methods. The lack of understanding of the geometric nature of the model remained mathematically unsatisfying for years.

The arrival of the renormalization group formalism (see [Fis98] for a historical exposition) led to a better physical and geometrical understanding, albeit mostly non-rigorous. It suggests that the block-spin renormalization transformation (coarse-graining, e.g. replacing a block of neighboring sites by one site having a spin equal to the dominant spin in the block) corresponds to appropriately changing the scale and the temperature of the model. The Kramers-Wannier critical point then arises as the fixed point of the renormalization transformations. In particular, under simple rescaling the Ising model at the critical temperature should converge to a scaling limit, a continuous version of the originally discrete Ising model, corresponding to a quantum field theory. This leads to the idea of universality: the Ising models on diferent regular lattices or even more general planar graphs belong to the same renormalization space, with a unique critical point, and so at criticality the scaling limit and the scaling dimensions of the Ising model should always be the same (it should be independent of the lattice whereas the critical temperature depends on it).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>This result represented a shock for the community: it was the first mathematical evidence that the mean-field behavior was inaccurate in low dimensions.</span></small>

Being unique, the scaling limit at the critical point must satisfy translation, rotation and scale invariance, which allows one to deduce some information about correlations [PP66, Kad66]. In seminal papers [BPZ84b, BPZ84a], Belavin, Polyakov and Zamolodchikov suggested a much stronger invariance of the model. Since the scaling-limit quantum field theory is a local field, it should be invariant by any map which is locally a composition of translation, rotation and homothety. Thus it becomes natural to postulate full conformal invariance (under all conformal transformations<sup>2</sup> of subregions). This prediction generated an explosion of activity in conformal field theory, allowing nonrigorous explanations of many phenomena; see [ISZ88] for a collection of the original papers of the subject.

To summarize, Conformal Field Theory asserts that the Ising model admits a scaling limit at criticality, and that this scaling limit is a conformally invariant object. From a mathematical perspective, this notion of conformal invariance of a model is ill-posed, since the meaning of scaling limit is not even clear. The following solution to this problem can be implemented: the scaling limit of the model could simply retain the information given by interfaces only. There is no reason why all the information of a model should be encoded into information on interfaces, yet one can hope that most of the relevant quantities can be recovered from it. The advantage of this approach is that there exists a mathematical setting for families of continuous curves.

In the Ising model, there is a canonical way to isolate macroscopic interfaces. Consider a simply-connected domain Ω with two points a and b on the boundary and approximate it by a discrete graph$\Omega _ { \delta } \subset \delta \mathbb { Z } ^ { 2 }$. The boundary of$\Omega _ { \delta }$determines two arcs $\partial _ { a b }$and$\partial _ { b a }$⊂and we can fix the spins to be 1 on the arc$\partial _ { a b }$and 1 on the arc$\partial _ { b a }$ + −(this is called Dobrushin boundary conditions). In this case, there exists an interface3 separating 1 and 1 going from a to b and the prediction of Conformal Field Theory + −then translates into the following predictions for models: interfaces in$\Omega _ { \delta }$converge when δ goes to 0 to a random continuous non-selfcrossing curve$\gamma _ { ( \Omega , a , b ) }$between a and b in Ω which is conformally invariant in the following way:

For any$( \Omega , a , b )$and any conformal map$\psi : \Omega \to \mathbb { C }$, the random curve ψ$\circ \ \gamma _ { ( \Omega , a , b ) }$ ( )has the same law as$\gamma _ { ( \psi ( \Omega ) , \psi ( a ) , \psi ( b ) ) }$

In 1999, Schramm proposed a natural candidate for the possible conformally invariant families of continuous non-selfcrossing curves. He noticed that interfaces of models further satisfy the domain Markov property, which, together with the assumption of conformal invariance, determine the possible families of curves. In [Sch00], he introduced the Schramm-Loewner Evolution (SLE for short): for$\kappa > 0$, the$\operatorname { S L E } ( \kappa )$is the random Loewner Evolution with driving process$\sqrt { \kappa } B _ { t }$, where$\left( B _ { t } \right)$is a standard Brownian ( )motion (see Befara’s course in this volume). In our case, it implies that the random continuous curve$\gamma _ { ( \Omega , a , b ) }$described previously should be an SLE.

( )<sub>Proving convergence of interfaces to an SLE is fundamental. Indeed, SLE processes</sub> are now well-understood and their path properties can be related to fractal properties of the critical phase. Critical exponents can then be deduced from these properties via the so-called scaling relations. These notes provide an (almost) self-contained proof of convergence to SLE for the two-dimensional Ising model and its random-cluster representation the FK-Ising model (see Section 3 for a formal definition).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∂<sub>ab</sub>.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>i.e. one-to-one holomorphic maps.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>In fact the interface is not unique. In order to solve this issue, consider the closest interface to</span></small>

![](images/page_4_image_0.jpg)

Figure 2: An interface between and in the Ising model.

Main result 1 (Theorem 2.10) The law ofinterfaces ofthe critical Ising model converges in the scaling limit to a conformally invariant limit described by the Schramm-Loewner Evolution of parameter$\kappa = 3$

=Main result 2 (Theorem 3.13) The law of interfaces of the critical FK-Ising model converges in the scaling limit to a conformally invariant limit described by the Schramm-Loewner Evolution of parameter$\kappa = 1 6 / 3$

Even though we now have a mathematical framework for conformal invariance, it remains dificult to prove convergence of interfaces to SLEs. Observe that working with interfaces ofers a further simplification: properties of these interfaces should also be conformally invariant. Therefore, one could simply look at a discrete observable of the model and try to prove that it converges in the scaling limit to a conformally covariant object. Of course, it is not clear that this observable would tell us anything about critical exponents, yet it already represents a significant step toward conformal invariance.

In 1994, Langlands, Pouliot and Saint-Aubin [LPSA94] published a number of numerical values in favor of conformal invariance (in the scaling limit) of crossing probabilities in the percolation model. More precisely, they checked that, taking diferent topological rectangles, the probability$C _ { \delta } ( \Omega , A , B , C , D )$of having a path of adjacent open edges ( )from AB to CD converges when δ goes to 0 towards a limit which is the same for $( \Omega , A , B , C , D )$and$\left( \Omega ^ { \prime } , A ^ { \prime } , B ^ { \prime } , C ^ { \prime } , D ^ { \prime } \right)$if they are images of each other by a conformal ( ) ( )map. The paper [LPSA94], while only numerical, attracted many mathematicians to the domain. The same year, Cardy [Car92] proposed an explicit formula for the limit of percolation crossing probabilities. In 2001, Smirnov proved Cardy’s formula rigorously for critical site percolation on the triangular lattice [Smi01], hence rigorously providing a concrete example of a conformally invariant property of the model. A somewhat incredible consequence of this theorem is that the mechanism can be reversed: even though Cardy’s formula seems much weaker than convergence to SLE, they are actually equivalent. In other words, conformal covariance of one well-chosen observable of the model can be suficient to prove conformal invariance of interfaces.

It is also possible to find an observable with this property in the Ising case (see Definition 2.9). This observable, called the fermionic observable, is defined in terms of the so-called high temperature expansion of the Ising model. Specific combinatorial properties of the Ising model translate into local relations for the fermionic observable. In particular, the observable can be proved to converge when taking the scaling limit. This convergence result (Theorem 2.11) is the main step in the proof of conformal invariance. Similarly, a fermionic observable can be defined in the FK-Ising case, and its convergence implies the convergence of interfaces.

Archetypical examples of conformally covariant objects are holomorphic solutions to boundary value problems such as Dirichlet or Riemann problems. It becomes natural to expect that discrete observables which are conformally covariant in the scaling limit are naturally preharmonic or preholomorphic functions, i.e. relevant discretizations of harmonic and holomorphic functions. Therefore, the proofs of conformal invariance harness discrete complex analysis in a substantial way. The use of discrete holomorphicity appeared first in the case of dimers [Ken00] and has been extended to several statistical physics models since then. Other than being interesting in themselves, preholomorphic functions have found several applications in geometry, analysis, combinatorics, and probability. We refer the interested reader to the expositions by Lovász [Lov04], Stephenson [Ste05], Mercat [Mer01], Bobenko and Suris [BS08]. Let us finish by mentioning that the previous discussion sheds a new light on both approaches described above: combinatorial properties of the discrete Ising model allow us to prove the convergence of discrete observables to conformally covariant objects. In other words, exact integrability and Conformal Field Theory are connected via the proof of the conformal invariance of the Ising model.

Acknowledgments These notes are based on a course on conformal invariance of lattice models given in Búzios, Brazil, in August 2010, as part of the Clay Mathematics Institute Summer School. The course consisted of six lectures by the second author. The authors wish to thank the organisers of both the Clay Mathematics Institute Summer School and the XIV Brazilian Probability School for this milestone event. We are particularly grateful to Vladas Sidoravicius for his incredible energy and the constant efort put into the organization of the school. We thank Stéphane Benoist, David Cimasoni and Alan Hammond for a careful reading of previous versions of this manuscript. The two authors were supported by the EU Marie-Curie RTN CODY, the ERC AG CONFRA, as well as by the Swiss FNS. The research of the second author is supported by the Chebyshev Laboratory (Department of Mathematics and Mechanics, St. Petersburg State University) under RF Government grant 11.G34.31.0026.

## 1.1 Organization of the notes

Section 2 presents the necessary background on the spin Ising model. In the first subsection, we recall general facts on the Ising model. In the second subsection, we introduce the low and high temperature expansions, as well as Kramers-Wannier duality. In the last subsection, we use the high-temperature expansion in spin Dobrushin domains to define the spin fermionic observable. Via the Kramers-Wannier duality, we explain how it relates to interfaces of the Ising model at criticality and we state the conformal invariance result for Ising.

Section 3 introduces the FK-Ising model. We start by defining general FK percolation models and we discuss planar duality. Then, we explain the Edwards-Sokal coupling, an important tool relating the spin Ising and FK-Ising models. Finally, we introduce the loop representation of the FK-Ising model in FK Dobrushin domains. It allows us to define the FK fermionic observable and to state the conformal invariance result for the FK-Ising model.

Section 4 is a brief survey of discrete complex analysis. We first deal with preharmonic functions and a few of their elementary properties. These properties will be used in Section 6. In the second subsection, we present a brief historic of preholomorphic functions. The third subsection is the most important, it contains the definition and several properties of s-holomorphic (or spin-holomorphic) functions. This notion is crucial in the proof of conformal invariance: the fermionic observables will be proved to be s-holomorphic, a fact which implies their convergence in the scaling limit. We also include a brief discussion on complex analysis on general graphs.

Section 5 is devoted to the convergence of the fermionic observables. First, we show that the FK fermionic observable is s-holomorphic and that it converges in the scaling limit. Second, we deal with the spin fermionic observable. We prove its s-holomorphicity and sketch the proof of its convergence.

Section 6 shows how to harness the convergence of fermionic observables in order to prove conformal invariance of interfaces in the spin and FK-Ising models. It mostly relies on tightness results and certain properties of Loewner chains.

Section$7$is intended to present several other applications of the fermionic observables. In particular, we provide an elementary derivation of the critical inversetemperature.

Section 8 contains a discussion on generalizations of this approach to lattice models. It includes a subsection on the Ising model on general planar graphs. It also gathers conjectures regarding models more general than the Ising model.

## 1.2 Notations

## 1.2.1 Primal, dual and medial graphs

We mostly consider the (rotated) square lattice L with vertex set$\mathrm { e } ^ { i \pi / 4 } \mathbb { Z } ^ { 2 }$and edges between nearest neighbors. An edge with end-points x and y will be denoted by$[ x y ]$ If there exists an edge e such that$e = [ x y ]$, we write$x \sim y$[ ]. Finite graphs G will always = [ ] ∼be subgraphs of L and will be called primal graphs. The boundary of$G ,$, denoted by $\partial G ,$, will be the set of sites of G with fewer than four neighbors in$G _ { \ l }$

The dual graph$G ^ { \star }$of a planar graph G is defined as follows: sites of$G ^ { \star }$correspond to faces of$G$(for convenience, the infinite face will not correspond to a dual site), edges of$G ^ { \star }$connect sites corresponding to two adjacent faces of G. The dual lattice of$\mathbb { L }$is denoted by$\mathbb { L } ^ { \star }$

The medial lattice$\mathbb { L } ^ { \circ }$is the graph with vertex set being the centers of edges of$\mathbb { L } ,$ and edges connecting nearest vertices, see Fig. 6. The medial graph$G ^ { \circ }$is the subgraph of$\mathbb { L } ^ { \circ }$composed of all the vertices of$\mathbb { L } ^ { \diamond }$corresponding to edges of$G .$. Note that$\mathbb { L } ^ { \circ }$is a rotated and rescaled (by a factor$1 / \sqrt { 2 } )$version of$\mathbb { L } ,$and that it is the usual square /lattice. We will often use the connection between the faces of$\mathbb { L } ^ { \circ }$and the sites of L and $\mathbb { L } ^ { \star }$. We say that a face of the medial lattice is black if it corresponds to a vertex of$\mathbb { L } ,$ and white otherwise. Edges of$\mathbb { L } ^ { \circ }$are oriented counterclockwise around black faces.

## 1.2.2 Approximations of domains

We will be interested in finer and finer graphs approximating continuous domains. For $\delta > 0$, the square lattice$\sqrt { 2 } \delta \mathbb { L }$of mesh-size$\sqrt { 2 } \delta$will be denoted by$\mathbb { L } _ { \delta }$. The definitions >of dual and medial lattices extend to this context. Note that the medial lattice$\mathbb { L } _ { \delta } ^ { \diamond }$has mesh-size δ.

For a simply connected domain Ω in the plane, we set$\Omega _ { \delta } \ : = \ : \Omega \cap \mathbb { L } _ { \delta }$. The edges connecting sites of$\Omega _ { \delta }$are those included in Ω. The graph$\Omega _ { \delta }$= ∩should be thought of as a discretization of Ω (we avoid technicalities concerning the regularity of the domain). More generally, when no continuous domain Ω is specified,$\Omega _ { \delta }$stands for a finite simply connected (meaning that the complement is connected) subgraph of$\mathbb { L } _ { \delta }$

We will be considering sequences of functions on$\Omega _ { \delta }$for$\delta$going to 0. In order to make functions live in the same space, we implicitly perform the following operation: for a function$f$on$\Omega _ { \delta }$, we choose for each square a diagonal and extend the function to Ω in a piecewise linear way on every triangle (any reasonable way would do). Since no confusion will be possible, we denote the extension by$f$as well.

## 1.2.3 Distances and convergence

Points in the plane will be denoted by their complex coordinates, Re z and Im z will ( ) ( )be the real and imaginary parts of z respectively. The norm will be the usual complex modulus . Unless otherwise stated, distances between points (even if they belong to ∣ ⋅ ∣a graph) are distances in the plane. The distance between a point z and a closed set $F$is defined by

$$
d (z, F) := \inf _ {y \in F} | z - y |.\tag{1.1}
$$

Convergence of random parametrized curves (say with time-parameter in$[ 0 , 1 ] )$is in [ ]the sense of the weak topology inherited from the following distance on curves:

$$
d (\gamma_ {1}, \gamma_ {2}) = \inf _ {\phi} \sup _ {u \in [ 0, 1 ]} | \gamma_ {1} (u) - \gamma_ {2} (\phi (u)) |,\tag{1.2}
$$

where the infimum is taken over all reparametrizations$( i . e .$. strictly increasing continuous functions$\phi \colon [ 0 , 1 ]  [ 0 , 1 ]$with$\phi ( 0 ) = 0$and$\phi ( 1 ) = 1 )$.

## 2 Two-dimensional Ising model

## 2.1 Boundary conditions, infinite-volume measures and phase transition

The (spin) Ising model can be defined on any graph. However, we will restrict ourselves to the (rotated) square lattice. Let G be a finite subgraph of L, and$b \in \{ - 1 , + 1 \} ^ { \partial G }$ ∈ {−The Ising model with boundary conditions b is a random assignment of spins$\{ - 1 , + 1 \}$ (or simply$- / + )$to vertices of$G$such that$\sigma _ { x } = b _ { x }$on$\partial G$, where$\sigma _ { x }${− + }denotes the spin at −/+ =site x. The partition function of the model is denoted by

$$
Z _ {\beta , G} ^ {b} = \sum_ {\sigma \in \{- 1, 1 \} ^ {G}: \sigma = b \text {on} \partial G} \exp \left[ \beta \sum_ {x \sim y} \sigma_ {x} \sigma_ {y} \right],\tag{2.1}
$$

where$\beta$is the inverse-temperature of the model and the second summation is over all pairs of neighboring sites x, y in$G .$. The probability of a configuration$\sigma$is then equal to

$$
\mu_ {\beta , G} ^ {b} (\sigma) = \frac {1}{Z _ {\beta , G} ^ {b}} \exp \left[ \beta \sum_ {x \sim y} \sigma_ {x} \sigma_ {y} \right].\tag{2.2}
$$

Equivalently, one can define the Ising model without boundary conditions, also called free boundary conditions (it is the one defined in the introduction). The measure with free boundary conditions is denoted by$\mu _ { \beta , G } ^ { f }$

We will not ofer a complete exposition on the Ising model and we rather focus on crucial properties. The following result belongs to the folklore (see [FKG71] for the original paper). An event is called increasing if it is preserved by switching some spins from to .

Theorem 2.1 (Positive association at every temperature). The Ising model on a finite graph G at temperature$\beta > 0$satisfies the following properties:

• FKG inequality: For any boundary conditions b and any increasing events$A , B$

$$
\mu_ {\beta , G} ^ {b} (A \cap B) \geq \mu_ {\beta , G} ^ {b} (A) \mu_ {\beta , G} ^ {b} (B).\tag{2.3}
$$

• Comparison between boundary conditions: For boundary conditions$b _ { 1 } \leq b _ { 2 }$ (meaning that spins in$b _ { 1 }$are also in$b _ { 2 } )$and an increasing event A,

$$
\mu_ {\beta , G} ^ {b _ {1}} (A) \leq \mu_ {\beta , G} ^ {b _ {2}} (A).\tag{2.4}
$$

If (2.4) is satisfied for every increasing event, we say that$\mu _ { \beta , G } ^ { b _ { 2 } }$stochastically dominates$\mu _ { \beta , G } ^ { b _ { 1 } }$(denoted by$\mu _ { \beta , G } ^ { b _ { 1 } } \leq \mu _ { \beta , G } ^ { b _ { 2 } } )$. Two boundary conditions are extremal for the ≤stochastic ordering: the measure with all (resp. all ) boundary conditions, denoted by$\mu _ { \beta , G } ^ { + } ~ ( \mathrm { r e s p . } ~ \mu _ { \beta , G } ^ { - } )$+is the largest (resp. smallest).

Theorem 2.1 enables us to define infinite-volume measures as follows. Consider the nested sequence of boxes$\Lambda _ { n } = [ - n , n ] ^ { 2 }$. For any$N > 0$and any increasing event A depending only on spins in$\Lambda _ { N }$= [− ], the sequence$( \mu _ { \beta , \Lambda _ { n } } ^ { + } ( A ) ) _ { n \geq N }$is decreasi$\mathrm { { 1 g ^ { 4 } } }$. The limit, denoted by$\mu _ { \beta } ^ { + } ( A )$( ( )) ≥, can be defined and verified to be independent on$N$

(In this way,$\mu _ { \beta } ^ { + }$is defined for increasing events depending on a finite number of sites. It can be further extended to a probability measure on the σ-algebra spanned by cylindrical events (events measurable in terms of a finite number of spins). The resulting measure, denoted by$\mu _ { \beta } ^ { + }$, is called the infinite-volume Ising model with + boundary conditions.

Observe that one could construct (a priori) diferent infinite-volume measures, for instance with boundary conditions (the corresponding measure is denoted by$\mu _ { \beta } ^ { - } )$). If −infinite-volume measures are defined from a property of compatibility with finite volume measures, then$\mu _ { \beta } ^ { + }$and$\mu _ { \beta } ^ { - }$are extremal among infinite-volume measures of parameter $\beta .$In particular, if$\mu _ { \beta } ^ { + } = \mu _ { \beta } ^ { - }$, there exists a unique infinite volume measure.

=The Ising model in infinite-volume exhibits a phase transition at some critical inversetemperature$\beta _ { c }$:

Theorem 2.2. Let$\begin{array} { r } { \beta _ { c } = \frac { 1 } { 2 } \ln ( 1 + \sqrt { 2 } ) } \end{array}$. The magnetization$\mu _ { \beta } ^ { + } \lbrack \sigma _ { 0 } \rbrack$at the origin is strictly positive$f o r \ \beta > \beta _ { c }$= ( + )and equal to 0 when$\beta < \beta _ { c }$

In other words, when$\beta > \beta _ { c }$, there is long range memory, the phase is ordered. When $\beta < \beta _ { c } .$>the phase is called disordered. The existence of a critical temperature separating <the ordered from the disordered phase is a relatively easy fact [Pei36] (although at the time it was quite unexpected). Its computation is more dificult. It was identified without proof by Kramers and Wannier [KW41a, KW41b] using the duality between low and high temperature expansions of the Ising model (see the argument in the next section). The first rigorous derivation is due to Yang [Yan52]. He uses Onsager’s exact formula for the (infinite-volume) partition function to compute the spontaneous magnetization of the model. This quantity provides one criterion for localizing the critical point. The first probabilistic computation of the critical inverse-temperature is due to Aizenman, Barsky and Fernández [ABF87]. In Subsection 7.1, we present a short alternative proof of Theorem 2.2, using the fermionic observable.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Λn</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∂Λn</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>µ</sub>+<sub>β,Λn.</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>µ</sub>+<sub>β,Λn+1</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>Indeed, for any configuration of spins in ∂Λ<sub>n</sub> being smaller than all +, the restriction ofto Λ<sub>n</sub> is stochastically dominated by</span></small>

The critical inverse-temperature has also an interpretation in terms of infinite-volume measures (these measures are called Gibbs measures). For$\beta < \beta _ { c }$there exists a unique Gibbs measure, while for$\beta > \beta _ { c }$&lt;there exist several. The classification of Gibbs measures &gt;in the ordered phase is interesting: in dimension two, any infinite-volume measure is a convex combination of$\mu _ { \beta } ^ { + }$and$\mu _ { \beta } ^ { - }$(see [Aiz80, Hig81] or the recent proof [CV10]). This result is no longer true in higher dimension: non-translational-invariant Gibbs measures can be constructed using 3D Dobrushin domains [Dob72].

When$\beta > \beta _ { c }$, spin-correlations$\mu _ { \beta } ^ { + } \lbrack \sigma _ { 0 } \sigma _ { x } \rbrack$do not go to 0 when x goes to infinity. >There is long range memory. At$\beta _ { c }$[ ], spin-correlations decay to 0 following a power law [Ons44]:

$$
\mu_ {\beta_ {c}} ^ {+} \big [ \sigma_ {0} \sigma_ {x} \big ] \approx | x | ^ {- 1 / 4}
$$

when$x \to \infty$. When$\beta < \beta _ { c }$≈<sub>, spin-correlations decay exponentially fast in</sub>$| x | .$. More → ∞ <precisely, we will show the following result first due to [MW73]:

Theorem 2.3. For$\beta < \beta _ { c } ,$and$a = \mathrm { e } ^ { i \pi / 4 } ( x + i y ) \in \mathbb { C }$

$$
\tau_ {\beta} (a) = \lim _ {n \to \infty} - \frac {1}{n} \ln \mu_ {\beta} ^ {+} [ \sigma_ {0} \sigma_ {[ n a ]} ] = x \operatorname{arcsinh} (s x) + y \operatorname{arcsinh} (s y)
$$

where na is the site of L closest to na, and s solves the equation

$$
\sqrt {1 + s ^ {2} x ^ {2}} + \sqrt {1 + s ^ {2} y ^ {2}} = \sinh (2 \beta) + (\sinh (2 \beta)) ^ {- 1}.
$$

The quantity$\tau _ { \beta } ( z )$is called the correlation length in direction$z .$. When getting ( )closer to the critical point, the correlation length goes to infinity and becomes isotropic (it does not depend on the direction, thus giving a glimpse of rotational invariance at criticality):

Theorem 2.4 (see e.g. [Mes06]). For$z \in \mathbb { C }$, the correlation length satisfies the following equality

$$
\lim _ {\beta \nearrow \beta_ {c}} \frac {\tau_ {\beta} (z)}{(\beta_ {c} - \beta)} = 4 | z |.\tag{2.5}
$$

## 2.2 Low and high temperature expansions of the Ising model

The low temperature expansion of the Ising model is a graphical representation on the dual lattice. Fix a spin configuration σ for the Ising model on G with boundary conditions. The collection of contours of a spin configuration$\sigma$+is the set of interfaces (edges of the dual graph) separating  and  clusters. In a collection of contours, an + −even number of dual edges automatically emanates from each dual vertex. Reciprocally, any family of dual edges with an even number of edges emanating from each dual vertex is the collection of contours of exactly one spin configuration (since we fix boundary conditions).

The interesting feature of the low temperature expansion is that properties of the Ising model can be restated in terms of this graphical representation. We only give the example of the partition function on G but other quantities can be computed similarly. Let$\mathcal { E } _ { G ^ { \star } }$be the set of possible collections of contours, and let ω be the number of edges Eof a collection of contours ω, then

$$
Z _ {\beta , G} ^ {+} = \mathrm{e} ^ {\beta \# \mathrm{edgesin} G ^ {\star}} \sum_ {\omega \in \mathcal {E} _ {G ^ {\star}}} \left(\mathrm{e} ^ {- 2 \beta}\right) ^ {| \omega |}.\tag{2.6}
$$

The high temperature expansion of the Ising model is a graphical representation on the primal lattice itself. It is not a geometric representation since one cannot map a spin configuration$\sigma$to a subset of configurations in the graphical representation, but rather a convenient way to represent correlations between spins using statistics of contours. It is based on the following identity:

$$
\mathrm{e} ^ {\beta \sigma_ {x} \sigma_ {y}} = \cosh (\beta) + \sigma_ {x} \sigma_ {y} \sinh (\beta) = \cosh (\beta) [ 1 + \tanh (\beta) \sigma_ {x} \sigma_ {y} ]\tag{2.7}
$$

Proposition 2.5. Let$G$be a finite graph and$^ { a , }$b be two sites of G. At inversetemperature$\beta > 0$

$$
Z _ {\beta , G} ^ {f} = 2 ^ {\# \text {vertices} G} \cosh (\beta) ^ {\# \text {edges in} G} \sum_ {\omega \in \mathcal {E} _ {G}} \tanh (\beta) ^ {| \omega |}\tag{2.8}
$$

$$
\mu_ {\beta , G} ^ {f} \big [ \sigma_ {a} \sigma_ {b} \big ] = \frac {\sum_ {\omega \in \mathcal {E} _ {G} (a , b)} \tanh (\beta) ^ {| \omega |}}{\sum_ {\omega \in \mathcal {E} _ {G}} \tanh (\beta) ^ {| \omega |}},\tag{2.9}
$$

where$\mathcal { E } _ { G }$(resp.$\mathcal { E } _ { G } ( a , b ) )$is the set of families of edges of G such that an even number E E ( )of edges emanates from each vertex (resp. except at a and b, where an odd number of edges emanates).

The notation$\mathcal { E } _ { G }$coincides with the definition$\mathcal { E } _ { G ^ { \star } }$⋆ in the low temperature expansion Efor the dual lattice.

Proof Let us start with the partition function (2.8). Let$E$be the set of edges of$G .$ We know

$$
\begin{array}{r c l} Z _ {\beta , G} ^ {f} & = & \sum_ {\sigma} \prod_ {[ x y ] \in E} \mathrm{e} ^ {\beta \sigma_ {x} \sigma_ {y}} \\ & = & \cosh (\beta) ^ {\# \mathrm{edgesin} G} \sum_ {\sigma} \prod_ {[ x y ] \in E} [ 1 + \tanh (\beta) \sigma_ {x} \sigma_ {y} ] \\ & = & \cosh (\beta) ^ {\# \mathrm{edgesin} G} \sum_ {\sigma} \sum_ {\omega \subset E} \tanh (\beta) ^ {| \omega |} \prod_ {e = [ x y ] \in \omega} \sigma_ {x} \sigma_ {y} \\ & = & \cosh (\beta) ^ {\# \mathrm{edgesin} G} \sum_ {\omega \subset E} \tanh (\beta) ^ {| \omega |} \sum_ {\sigma} \prod_ {e = [ x y ] \in \omega} \sigma_ {x} \sigma_ {y} \end{array}
$$

where we used (2.7) in the second equality. Notice that$\begin{array} { r } { \sum _ { \sigma } \prod _ { e = [ x y ] \in \omega } \sigma _ { x } \sigma _ { y } } \end{array}$equals $2 ^ { \# }$<sup>vertices</sup> <sup>G</sup> if ω is in$\mathcal { E } _ { G }$∑, and 0 otherwise, hence proving (2.8).

Fix$a , b \in G$E. By definition,

$$
\mu_ {\beta , G} ^ {f} \big [ \sigma_ {a} \sigma_ {b} \big ] = \frac {\sum_ {\sigma} \sigma_ {a} \sigma_ {b} \mathrm{e} ^ {- \beta H (\sigma)}}{\sum_ {\sigma} \mathrm{e} ^ {- \beta H (\sigma)}} = \frac {\sum_ {\sigma} \sigma_ {a} \sigma_ {b} \mathrm{e} ^ {- \beta H (\sigma)}}{Z _ {\beta , G} ^ {f}},\tag{2.10}
$$

where$\begin{array} { r } { H ( \sigma ) = - \sum _ { i \sim j } \sigma _ { i } \sigma _ { j } } \end{array}$. The second identity boils down to proving that the right ( ) = − ∑ ∼hand terms of (2.9) and (2.10) are equal, i.e.

$$
\sum_ {\sigma} \sigma_ {a} \sigma_ {b} \mathrm{e} ^ {- \beta H (\sigma)} = 2 ^ {\# \text {vertices} G} \cosh (\beta) ^ {\# \text {edges in} G} \sum_ {\omega \in \mathcal {E} _ {G} (a, b)} \tanh (\beta) ^ {| \omega |}.\tag{2.11}
$$

The first lines of the computation for the partition function are the same, and we end up with

$$
\begin{array}{r c l} \sum_ {\sigma} \sigma_ {a} \sigma_ {b} \mathrm{e} ^ {- \beta H (\sigma)} & = & \cosh (\beta) ^ {\# \text {edges in} G} \sum_ {\omega \subset E} \tanh (\beta) ^ {| \omega |} \sum_ {\sigma} \sigma_ {a} \sigma_ {b} \prod_ {e = [ x y ] \in \omega} \sigma_ {x} \sigma_ {y} \\ & = & 2 ^ {\# \text {vertices} G} \cosh (\beta) ^ {\# \text {edges in} G} \sum_ {\omega \in \mathcal {E} _ {G} (a, b)} \tanh (\beta) ^ {| \omega |} \end{array}
$$

![](images/page_11_image_0.jpg)

Figure 3: The possible collections of contours for + boundary conditions in the lowtemperature expansion do not contain edges between boundary sites of$G .$. Therefore, they correspond to collections of contours in$\mathcal { E } _ { G ^ { \star } }$, which are exactly the collection of Econtours involved in the high-temperature expansion of the Ising model on$G ^ { \star }$with free boundary conditions.

since$\begin{array} { r } { \sum _ { \sigma } \sigma _ { a } \sigma _ { b } \prod _ { e = [ x y ] \in \omega } \sigma _ { x } \sigma _ { y } } \end{array}$equals$2 ^ { \# }$<sup>vertices</sup> <sup>G</sup> if$\omega \in { \mathcal { E } } _ { G } ( a , b )$, and 0 otherwise.

The set$\mathcal { E } _ { G }$is the set of collections of loops on G when forgetting the way we draw Eloops (since some elements of$\mathcal { E } _ { G }$, like a figure eight, can be decomposed into loops in several ways), while$\mathcal { E } _ { G } ( a , b )$Eis the set of collections of loops on$G$together with one curve from a to$b .$.

Proposition 2.6 (Kramers-Wannier duality). Let$\beta > 0$and define$\beta ^ { \star } \in ( 0 , \infty )$such that tanh$\left( \beta ^ { \star } \right) = \mathrm { e } ^ { - 2 \bar { \beta } }$, then for every graph G,

$$
2 ^ {\# \text { vertices } G ^ {\star}} \cosh (\beta^ {\star}) ^ {\# \text { edges in } G ^ {\star}} Z _ {\beta , G} ^ {+} = \left(\mathrm{e} ^ {\beta}\right) ^ {\# \text { edges in } G ^ {\star}} Z _ {\beta^ {\star}, G ^ {\star}} ^ {f}.\tag{2.12}
$$

Proof When writing the contour of connected components for the Ising model with$^ +$ boundary conditions, the only edges of$\mathbb { L } ^ { \star }$used are those of$G ^ { \star }$. Indeed, edges between boundary sites cannot be present since boundary spins are . Thus, the right and lefthand side terms of (2.12) both correspond to the sum on$\mathcal { E } _ { G ^ { \star } }$+of$( \mathrm { e } ^ { - 2 \dot { \beta } } ) ^ { | \omega | }$or equivalently of$\operatorname { t a n h } ( \beta ^ { \star } ) ^ { | \omega | }$, implying the equality (see Fig. 3).□

We are now in a position to present the argument of Kramers and Wannier. Physicists expect the partition function to exhibit only one singularity, localized at the critical point. If$\beta _ { c } ^ { \star } \neq \beta _ { c }$, there would be at least two singularities, at$\beta _ { c }$and$\beta _ { c } ^ { \star }$, thanks to the ≠previous relation between partition functions at these two temperatures. Thus,$\beta _ { c }$must equal$\beta _ { c } ^ { \star }$, which implies$\textstyle \beta _ { c } = { \frac { 1 } { 2 } } \ln ( 1 + { \sqrt { 2 } } )$. Of course, the assumption that there is a = (unique singularity is hard to justify.

Exercise 2.7. Extend the low and high temperature expansions to free and + boundary conditions respectively. Extend the high-temperature expansion to n-point spin correlations.

Exercise 2.8 (Peierls argument). Use the low and high temperature expansions to show that$\beta _ { c } \in ( 0 , \infty )$, and that correlations between spins decay exponentially fast when$\beta$is ∈ ( ∞small enough.

![](images/page_12_image_0.jpg)

Figure 4: An example of collection of contours in$\mathcal { E } ( a _ { \delta } , z _ { \delta } )$on the lattice$\Omega _ { \circ }$

## 2.3 Spin-Dobrushin domain, fermionic observable and results on the Ising model

In this section we discuss the scaling limit of a single interface between and at + −criticality. We introduce the fundamental notions of Dobrushin domains and the so called fermionic observable.

Let$( \Omega , a , b )$be a simply connected domain with two marked points on the boundary. Let$\Omega _ { \delta } ^ { \circ }$( )be the medial graph of$\Omega _ { \delta }$composed of all the vertices of$\mathbb { L } _ { \delta } ^ { \diamond }$bordering a black face associated to$\Omega _ { \delta } .$, see Fig 4. This definition is non-standard since we include medial vertices not associated to edges of$\Omega _ { \delta }$. Let$a _ { \delta }$and$b _ { \delta }$be two vertices of$\partial \Omega _ { \delta } ^ { \circ }$close to a and b. We further require that$b _ { \delta }$is the southeast corner of a black face. We call the triplet$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$a spin-Dobrushin domain.

Let$z _ { \delta } \in \Omega _ { \delta } ^ { \circ }$). Mimicking the high-temperature expansion of the Ising model on$\Omega _ { \delta } .$ let$\mathcal { E } ( a _ { \delta } , z _ { \delta } )$be the set of collections of contours drawn on$\Omega _ { \delta }$composed of loops and E( )one interface from$a _ { \delta }$to$z _ { \delta }$, see Fig. 4. For a loop configuration$\omega , \gamma ( \omega )$denotes the unique curve from$a _ { \delta }$to$z _ { \delta }$( )turning always left when there is an ambiguity. With these notations, we can define the spin-Ising fermionic observable.

Definition 2.9. On a spin Dobrushin domain$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$, the spin-Ising fermionic observable at$z _ { \delta } \in \Omega _ { \delta } ^ { \circ }$is defined by

$$
F _ {\Omega_ {\delta}, a _ {\delta}, b _ {\delta}} (z _ {\delta}) = \frac {\sum_ {\omega \in \mathcal {E} (a _ {\delta} , z _ {\delta})} \mathrm{e} ^ {- \frac {1}{2} i W _ {\gamma (\omega)} (a _ {\delta} , z _ {\delta})} (\sqrt {2} - 1) ^ {| \omega |}}{\sum_ {\omega \in \mathcal {E} (a _ {\delta} , b _ {\delta})} \mathrm{e} ^ {- \frac {1}{2} i W _ {\gamma (\omega)} (a _ {\delta} , b _ {\delta})} (\sqrt {2} - 1) ^ {| \omega |}},
$$

where the winding$W _ { \gamma } ( a _ { \delta } , z _ { \delta } )$is the (signed) total rotation in radians of the curve$\gamma$ between a and$z _ { \delta }$.

The complex modulus of the denominator of the fermionic observable is connected to the partition function of a conditioned critical Ising model. Indeed, fix$b _ { \delta } \in \partial \Omega _ { \delta } ^ { \circ }$ Even though$\mathcal { E } ( a _ { \delta } , b _ { \delta } )$∈is not exactly a high-temperature expansion (since there are two E( )half-edges starting from$a _ { \delta }$and$b _ { \delta }$respectively), it is in bijection with the set$\mathcal { E } ( a , b )$ E( )Therefore, (2.11) can be used to relate the denominator of the fermionic observable to the partition function of the Ising model on the primal graph with free boundary conditions conditioned on the fact that a and b have the same spin. Let us mention that the numerator of the observable also has an interpretation in terms of disorder operators of the critical Ising model.

![](images/page_13_image_0.jpg)

Figure 5: A high temperature expansion of an Ising model on the primal lattice together with the corresponding configuration on the dual lattice. The constraint that$a _ { \delta }$is connected to$b _ { \delta }$corresponds to the partition function of the Ising model with$+ / -$boundary conditions on the domain.

The weights of edges are critical (since$\sqrt { 2 } - 1 = \mathrm { e } ^ { - 2 \beta _ { c } } \bigr )$.Therefore, the Kramers-− =Wannier duality has an enlightening interpretation here. The high-temperature expansion can be thought of as the low-temperature expansion of an Ising model on the dual graph, where the dual graph is constructed by adding one layer of dual vertices around $\partial G$, see Fig. 5. Now, the existence of a curve between$a _ { \delta }$and$b _ { \delta }$is equivalent to the existence of an interface between pluses and minuses in this new Ising model. Therefore, it corresponds to a model with Dobrushin boundary conditions on the dual graph. This fact is not surprising since the dual boundary conditions of the free boundary conditions conditioned on$\sigma _ { a } = \sigma _ { b }$are the Dobrushin ones.

=From now on, the Ising model on a spin Dobrushin domain is the critical Ising model on$\Omega _ { \delta } ^ { \star }$with Dobrushin boundary conditions. The previous paragraph suggests a connection between the fermionic observable and the interface in this model. In fact, Section 6 will show that the fermionic observable is crucial in the proof that the unique interface γ going from$a _ { \delta }$to$b _ { \delta }$between the component connected to the arc$\partial _ { a b } ^ { \star }$and the component connected to$\partial _ { b a } ^ { \star }$+ −(preserve the convention that the interface turns left every time there is a choice) is conformally invariant in the scaling limit. Figures 1 (center picture) and 2 show two interfaces in domains with Dobrushin boundary conditions.

Theorem 2.10. Let$( \Omega , a , b )$be a simply connected domain with two marked points on the boundary. Let$\gamma _ { \delta }$( )be the interface of the critical Ising model with Dobrushin boundary conditions on the spin Dobrushin domain$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$. Then$( \gamma _ { \delta } ) _ { \delta > 0 }$converges weakly as$\delta \to 0$( ) ( ) >to the (chordal) Schramm-Loewner Evolution with parameter$\kappa = 3$

The proof of Theorem 2.10 follows the program below, see Section 6:

• Prove that the family of interfaces$( \gamma _ { \delta } ) _ { \delta > 0 }$is tight.

• Prove that$M _ { t } ^ { z _ { \delta } } = F _ { \Omega _ { \delta } ^ { \diamond } \setminus \gamma _ { \delta } [ 0 , t ] , \gamma _ { \delta } ( t ) , b _ { \delta } } \left( z _ { \delta } \right)$is a martingale for the discrete curve$\gamma _ { \delta } .$

• Prove that these martingales are converging when δ goes to 0. This provides us with a continuous martingale$( M _ { t } ^ { z } ) _ { t }$for any sub-sequential limit of the family $( \gamma _ { \delta } ) _ { \delta > 0 }$

• Use the martingales$( M _ { t } ^ { z } ) _ { t }$to identify the possible sub-sequential limits. Actually, ( )we will prove that the (chordal) Schramm-Loewner Evolution with parameter$\kappa = 3$ is the only possible limit, thus proving the convergence.

The third step (convergence of the observable) will be crucial for the success of this program. We state it as a theorem on its own. The connection with the other steps will be explained in detail in Section 6.

Theorem 2.11 ([CS09]). Let Ω be a simply connected domain and a, b two marked points on its boundary, assuming that the boundary is smooth in a neighborhood of b. We have that

$$
F _ {\Omega_ {\delta}, a _ {\delta}, b _ {\delta}} (\cdot) \rightarrow \sqrt {\frac {\psi^ {\prime} (\cdot)}{\psi^ {\prime} (b)}} \quad w h e n \delta \rightarrow 0\tag{2.13}
$$

uniformly on every compact subset of Ω, where ψ is any conformal map from Ω to the upper half-plane H, mapping a to and b to 0.

The fermionic observable is a powerful tool to prove conformal invariance, yet it is also interesting in itself. Being defined in terms of the high-temperature expansion of the Ising model, it expresses directly quantities of the model. For instance, we will explain in Section 6 how a more general convergence result for the observable enables us to compute the energy density.

Theorem 2.12 ([HS10]). Let Ω be a simply connected domain and$a \in \Omega$. If$e _ { \delta } = [ x y ]$ denotes the edge of$\Omega \cap \bar { \delta \mathbb { Z } } ^ { 2 }$closest to$^ { a , }$∈then the following equality holds:

$$
\mu_ {\beta_ {c}, \Omega \cap \delta \mathbb {Z} ^ {2}} ^ {f} [ \sigma_ {x} \sigma_ {y} ] = \frac {\sqrt {2}}{2} - \frac {\phi_ {a} ^ {\prime} (a)}{\pi} \delta + o (\delta),
$$

where$\mu _ { \beta _ { c } , \Omega _ { \delta } } ^ { f }$is the Ising measure at criticality and$\phi _ { a }$is the unique conformal map from Ω to the disk D sending a to 0 and such that$\phi _ { a } ^ { \prime } ( a ) > 0$

## 3 Two-dimensional FK-Ising model

In this section, another graphical representation of the Ising model, called the FK-Ising model, is presented in detail. Its properties will be used to describe properties of the Ising model in the following sections.

## 3.1 FK percolation

We refer to [Gri06] for a complete study on FK percolation (invented by Fortuin and Kasteleyn [FK72]). A configuration ω on G is a random subgraph of$G ,$composed of the same sites and a subset of its edges. The edges belonging to ω are called open, the others closed. Two sites x and y are said to be connected (denoted by$x  y )$, if there is an open$p a t h - \mathrm { a }$↔ path composed of open edges — connecting them. The maximal connected components are called clusters.

Boundary conditions$\xi$are given by a partition of$\partial G$. Let$o ( \omega ) \ ( \mathrm { r e s p . } \ c ( \omega ) )$denote the number of open (resp. closed) edges of$\omega$and$k ( \omega , \xi )$( ) ( )the number of connected components of the graph obtained from$\omega$( )by identifying (or wiring) the vertices in$\xi$ that belong to the same class of$\xi .$

The FK percolation$\phi _ { p , q , G } ^ { \xi }$on a finite graph$G$with parameters$p \in [ 0 , 1 ]$, and$q \in$ $( 0 , \infty )$and boundary conditions$\xi$is defined by

$$
\phi_ {p, q, G} ^ {\xi} (\omega) := \frac {p ^ {o (\omega)} (1 - p) ^ {c (\omega)} q ^ {k (\omega , \xi)}}{Z _ {p , q , G} ^ {\xi}},\tag{3.1}
$$

for any subgraph$\omega$of$G ,$where$Z _ { p , q , G } ^ { \xi }$is a normalizing constant called the partition function for the FK percolation. Here and in the following, we drop the dependence on $\xi$in$k ( \omega , \xi )$

( )The FK percolations with parameter$q < 1$and$q \geq 1$behave very diferently. For now, <we restrict ourselves to the second case. When$q \geq 1$, the FK percolation is positively ≥correlated: an event is called increasing if it is preserved by addition of open edges.

Theorem 3.1. For$q \geq 1$and$p \in [ 0 , 1 ]$, the FK percolation on$G$satisfies the following two properties:

$\pmb { F K G }$inequality: For any boundary conditions$\xi$and any increasing events$A , B$

$$
\phi_ {p, q, G} ^ {\xi} (A \cap B) \geq \phi_ {p, q, G} ^ {\xi} (A) \phi_ {p, q, G} ^ {\xi} (B).\tag{3.2}
$$

• Comparison between boundary conditions: for any ξ refinement of ψ and any increasing event A,

$$
\phi_ {p, q, G} ^ {\psi} (A) \geq \phi_ {p, q, G} ^ {\xi} (A).\tag{3.3}
$$

The previous result is very similar to Theorem 2.1. As in the Ising model case, one can define a notion of stochastic domination. Two boundary conditions play a special role in the study of FK percolation: the wired boundary conditions, denoted by$\xi = 1$ =are specified by the fact that all the vertices on the boundary are pairwise connected. The free boundary conditions, denoted by$\xi = 0 ,$, are specified by the absence of wirings =between boundary sites. The free and wired boundary conditions are extremal among all boundary conditions for stochastic ordering.

Infinite-volume measures can be defined as limits of measures on nested boxes. In particular, we set$\phi _ { p , q } ^ { 1 }$for the infinite-volume measure with wired boundary conditions and$\phi _ { p , q } ^ { 0 }$for the infinite-volume measure with free boundary conditions. Like the Ising model, the model exhibits a phase transition in the infinite-volume limit.

Theorem 3.2. For any$q \geq 1$, there exists$p _ { c } ( q ) \in ( 0 , 1 )$such that for any infinite volume measure$\phi _ { p , q }$,

$i f p < p _ { c } ( q )$, there is almost surely no infinite cluster under$\phi _ { p , q }$4

$i f p > p _ { c } ( q )$, there is almost surely a unique infinite cluster under$\phi _ { p , q }$

Note that$q = 1$is simply bond percolation. In this case, the existence of a phase =transition is a well-known fact. The existence of a critical point in the general case$q \geq 1$ is not much harder to prove: a coupling between two measures$\phi _ { p _ { 1 } , q , G }$and$\phi _ { p _ { 2 } , q , G }$≥can be constructed in such a way that$\phi _ { p _ { 1 } , q , G }$stochastically dominates$\phi _ { p _ { 2 } , q , G }$if$p _ { 1 } \geq p _ { 2 }$ (this coupling is not as straightforward as in the percolation case, see$e . g .$≥. [Gri06]). The determination of the critical value is a much harder task.

A natural notion of duality also exists for the FK percolation on the square lattice (and more generally on any planar graph). We present duality in the simplest case of wired boundary conditions. Construct a model on$G ^ { \star }$by declaring any edge of the dual graph to be open (resp. closed) if the corresponding edge of the primal graph is closed (resp. open) for the initial FK percolation model.

Proposition 3.3. The dual model of the FK percolation with parameters$( p , q )$with wired boundary conditions is the FK percolation with parameters$( p ^ { \star } , q )$( )and free boundary conditions on$G ^ { \star }$, where

$$
p ^ {\star} = p ^ {\star} (p, q) := \frac {(1 - p) q}{(1 - p) q + p}\tag{3.4}
$$

Proof Note that the state of edges between two sites of$\partial G$is not relevant when boundary conditions are wired. Indeed, sites on the boundary are connected via boundary conditions anyway, so that the state of each boundary edge does not alter the connectivity properties of the subgraph, and is independent of other edges. For this reason, forget about edges between boundary sites and consider only inner edges (which correspond to edges of$G ^ { \star } ) \colon o ( \omega )$and$c ( \omega )$then denote the number of open and closed inner edges.

Set$e ^ { \star }$for the dual edge of$G ^ { \star }$associated to the (inner) edge$e .$From the definition of the dual configuration$\omega ^ { \star }$of$\omega ,$we have$o ( \omega ^ { \star } ) = a - o ( \omega )$where a is the number of edges in$G ^ { \star }$and$o ( \omega ^ { \star } )$( ) = − ( )is the number of open dual edges. Moreover, connected components of $\omega ^ { \star }$( )correspond exactly to faces of$\omega _ { \mathrm { { i } } }$, so that$f ( \omega ) = k ( \omega ^ { \star } )$, where$f ( \omega )$is the number of ( ) = (faces (counting the infinite face). Using Euler’s formula

\# edges$+ \#$connected components$+ 1 = \# \mathrm { s i t e s ~ + ~ } \#$faces,

which is valid for any planar graph, we obtain, with s being the number of sites in$G _ { \ l }$

$$
k (\omega) = s - 1 + f (\omega) - o (\omega) = s - 1 + k \left(\omega^ {\star}\right) - a + o \left(\omega^ {\star}\right).
$$

The probability of$\omega ^ { \star }$is equal to the probability of ω under$\phi _ { G , p , q } ^ { 1 } , i . e$

$$
\begin{array}{r c l} \phi_ {G, p, q} ^ {1} (\omega) & = & \frac {1}{Z _ {G , p , q} ^ {1}} p ^ {o (\omega)} (1 - p) ^ {c (\omega)} q ^ {k (\omega)} \\ & = & \frac {(1 - p) ^ {a}}{Z _ {G , p , q} ^ {1}} [ p / (1 - p) ] ^ {o (\omega)} q ^ {k (\omega)} \\ & = & \frac {(1 - p) ^ {a}}{Z _ {G , p , q} ^ {1}} [ p / (1 - p) ] ^ {a - o (\omega^ {\star})} q ^ {s - 1 - a + k (\omega^ {\star}) + o (\omega^ {\star})} \\ & = & \frac {p ^ {a} q ^ {s - 1 - a}}{Z _ {G , p , q} ^ {1}} [ q (1 - p) / p ] ^ {o (\omega^ {\star})} q ^ {k (\omega^ {\star})} = \phi_ {p ^ {\star}, q, G ^ {\star}} ^ {0} (\omega^ {\star}) \end{array}
$$

since$q ( 1 - p ) / p = p ^ { \star } / ( 1 - p ^ { \star } )$, which is exactly the statement.

It is then natural to define the self-dual point$p _ { s d } ~ = ~ p _ { s d } ( q )$solving the equation $p _ { s d } ^ { \star } = p _ { s d }$, which gives

$$
p _ {s d} = p _ {s d} (q) := \frac {\sqrt {q}}{1 + \sqrt {q}}.
$$

Note that, mimicking the Kramers-Wannier argument, one can give a simple heuristic justification in favor of$p _ { c } ( q ) = p _ { s d } ( q )$. Recently, the computation of$p _ { c } ( q )$was performed for every$q \geq 1$4

Theorem 3.4 ([BDC10]). The critical parameter$p _ { c } ( q )$of the FK percolation on the square lattice equals$\textstyle p _ { s d } ( q ) = { \sqrt { q } } / ( 1 + { \sqrt { q } } )$for every$q \geq 1$

Exercise 3.5. Describe the dual of a FK percolation with parameters$( p , q )$and free ( )boundary conditions. What is the dual model of the FK percolation in infinite-volume with wired boundary conditions?

Exercise 3.6 (Zhang’s argument for FK percolation, [Gri06]). Consider the FK percolation with parameters$q \geq 1$and$p = p _ { s d } ( q )$. We suppose known the fact that infinite ≥ = ( )clusters are unique, and that the probability that there is an infinite cluster is 0 or 1.

Assume that there is a.s. an infinite cluster for the measure$\phi _ { p _ { s d } , q } ^ { 0 } .$

1) Let$\varepsilon < 1 / 1 0 0$. Show that there exists$n > 0$such that the$\phi _ { p _ { s d } , q } ^ { 0 }$-probability that < /the infinite cluster touches$[ - n , n ] ^ { 2 }$>is larger than$1 - \varepsilon$. Using the$F K G$inequality for [− ] −decreasing events (one can check that the FKG inequality holds for decreasing events as well), show that the$\phi _ { p _ { s d } , q } ^ { 0 } -$probability that the infinite cluster touches$\{ n \} \times [ - n , n ]$from the outside of$[ - n , n ] ^ { 2 }$is larger than$1 - \varepsilon ^ { \frac { 1 } { 4 } }$

[− ] −2) Using the uniqueness of the infinite cluster and the fact that the probability that there exists an infinite cluster equals 0 or 1 (can you prove these facts?), show that a.s. there is no infinite cluster for the FK percolation with free boundary conditions at the self-dual point.

3) Is the previous result necessarily true for the FK percolation with wired boundary conditions at the self-dual point? What can be said about$p _ { c } ( q ) \ell$

Exercise 3.7. Prove Euler’s formula.

## 3.2 FK-Ising model and Edwards-Sokal coupling

The Ising model can be coupled to the FK percolation with cluster-weight$q = 2 ~ [ \mathrm { E S 8 8 } ]$ For this reason, the$q \ : = \ : 2$=FK percolation model will be called the FK-Ising model. =We now present this coupling, called the Edwards-Sokal coupling, along with some consequences for the Ising model.

Let G be a finite graph and let ω be a configuration of open and closed edges on G. A spin configuration σ can be constructed on the graph G by assigning independently to each cluster of ω a  or  spin with probability$1 / 2$(note that all the sites of a cluster +receive the same spin).

Proposition 3.8. Let$p \in ( 0 , 1 )$and G a finite graph. Ifthe configuration ω is distributed ∈ ( )according to a FK measure with parameters$( p , 2 )$and free boundary conditions, then the ( )spin configuration σ is distributed according to an Ising measure with inverse-temperature $\begin{array} { r } { \beta = - \frac { 1 } { 2 } \ln ( 1 - p ) } \end{array}$and free boundary conditions.

Proof Consider a finite graph G, let$p \in ( 0 , 1 )$. Consider a measure P on pairs$( \omega , \sigma )$ ∈ ( ) ( )where ω is a FK configuration with free boundary conditions and σ is the corresponding random spin configuration, constructed as explained above. Then, for$( \omega , \sigma )$, we have:

$$
P \big [ (\omega , \sigma) \big ] = \frac {1}{Z _ {p , 2 , G} ^ {0}} p ^ {o (\omega)} (1 - p) ^ {c (\omega)} 2 ^ {k (\omega)} \cdot 2 ^ {- k (\omega)} = \frac {1}{Z _ {p , 2 , G} ^ {0}} p ^ {o (\omega)} (1 - p) ^ {c (\omega)}.
$$

Now, we construct another measure$\tilde { P }$on pairs of percolation configurations and spin configurations as follows. Let$\tilde { \sigma }$be a spin configuration distributed according to an Ising model with inverse-temperature$\beta$satisfying$\mathrm { e } ^ { - 2 \beta } = 1 - p$and free boundary conditions. We deduce$\tilde { \omega }$= −from σ˜ by closing all edges between neighboring sites with diferent spins, and by independently opening with probability p edges between neighboring sites with same spins. Then, for any$( \tilde { \omega } , \tilde { \sigma } )$,

$$
\tilde {P} [ (\tilde {\omega}, \tilde {\sigma}) ] = \frac {\mathrm{e} ^ {- 2 \beta r (\tilde {\sigma})} p ^ {o (\tilde {\omega})} (1 - p) ^ {a - o (\tilde {\omega}) - r (\tilde {\sigma})}}{Z _ {\beta , p} ^ {f}} = \frac {p ^ {o (\tilde {\omega})} (1 - p) ^ {c (\tilde {\omega})}}{Z _ {\beta , p} ^ {f}}
$$

where$a$is the number of edges of$G$and$r ( \tilde { \sigma } )$the number of edges between sites with diferent spins.

Note that the two previous measures are in fact defined on the same set of compatible pairs of configurations: if σ has been obtained from$\omega ,$then$\omega$can be obtained from$\sigma$ via the second procedure described above, and the same is true in the reverse direction for$\tilde { \omega }$and${ \tilde { \sigma } } .$. Therefore,$P = \tilde { P }$and the marginals of$P$are the FK percolation with parameters$( p , 2 )$=and the Ising model at inverse-temperature$\beta ,$which is the claim.

The coupling gives a randomized procedure to obtain a spin-Ising configuration from a FK-Ising configuration (it sufices to assign random spins). The proof of Proposition 3.8 provides a randomized procedure to obtain a FK-Ising configuration from a spin-Ising configuration.

If one considers wired boundary conditions for the FK percolation, the Edwards-Sokal coupling provides us with an Ising configuration with  boundary conditions (or $^ - ,$+the two cases being symmetric). We do not enter into details, since the generalization −is straightforward.

An important consequence of the Edwards-Sokal coupling is the relation between Ising correlations and FK connectivity properties. Indeed, two sites which are connected in the FK percolation configuration must have the same spin, while sites which are not have independent spins. This implies:

Corollary 3.9. For$p \in ( 0 , 1 )$, G a finite graph and$\begin{array} { r } { \beta = - \frac { 1 } { 2 } \ln ( 1 - p ) } \end{array}$, we obtain

$$
\begin{array}{r c l} \mu_ {\beta , G} ^ {f} [ \sigma_ {x} \sigma_ {y} ] & = & \phi_ {p, 2, G} ^ {0} (x \leftrightarrow y), \\ \mu_ {\beta , G} ^ {+} [ \sigma_ {x} ] & = & \phi_ {p, 2, G} ^ {1} (x \leftrightarrow \partial G). \end{array}
$$

In particular,$\begin{array} { r } { \beta _ { c } = - \frac { 1 } { 2 } \ln [ 1 - p _ { c } ( 2 ) ] } \end{array}$

Proof We leave the proof as an exercise.

The uniqueness of Ising infinite-volume measures was discussed in the previous section. The same question can be asked in the case of the FK-Ising model. First, it can be proved that$\phi _ { p , 2 } ^ { 1 }$and$\phi _ { p , 2 } ^ { 0 }$are extremal among all infinite-volume measures. Therefore, it is suficient to prove that$\phi _ { p , 2 } ^ { 1 } = \phi _ { p , 2 } ^ { 0 }$to prove uniqueness. Second, the absence of an infinite cluster for$\phi _ { p , 2 } ^ { 1 }$=can be shown to imply the uniqueness of the infinite-volume measure. Using the equality$p _ { c } = p _ { s d } .$, the measure is necessarily unique whenever$p < p _ { s d }$ since$\phi _ { p , 2 } ^ { 1 }$= <has no infinite cluster. Planar duality shows that the only value of p for which uniqueness could eventually fail is the (critical) self-dual point${ \sqrt { 2 } } / ( 1 + { \sqrt { 2 } } )$. It turns /( + )out that even for this value, there exists a unique infinite volume measure. Since this fact will play a role in the proof of conformal invariance, we now sketch an elementary proof due to W. Werner (the complete proof can be found in [Wer09]).

Proposition 3.10. There exists a unique infinite-volume FK-Ising measure with parameter$p _ { c } = \sqrt { 2 } / ( 1 + \sqrt { 2 } )$and there is almost surely no infinite cluster under this measure. = /( + )Correspondingly, there exists a unique infinite-volume spin Ising measure at$\beta _ { c }$

Proof As described above, it is suficient to prove that$\phi _ { p _ { s d } , 2 } ^ { 0 } = \phi _ { p _ { s d } , 2 } ^ { 1 }$. First note that there is no infinite cluster for$\phi _ { p _ { s d } , 2 } ^ { 0 }$=thanks to Exercise 3.6. Via the Edwards-Sokal coupling, the infinite-volume Ising measure with free boundary conditions, denoted by $\mu _ { \beta _ { c } } ^ { f }$, can be constructed by coloring clusters of the measure$\phi _ { p _ { s d } , 2 } ^ { 0 } .$Since there is no infinite cluster, this measure is obviously symmetric by global exchange of$+ / -$. In +/−particular, the argument of Exercise 3.6 can be applied to prove that there are neither nor infinite clusters. Therefore, fixing a box, there exists$\mathrm { ~ a ~ } +$star-connected circuit + − +surrounding the box with probability one (two vertices x and$y$are said to be starconnected if y is one of the eight closest neighbors to x).

One can then argue that the configuration inside the box stochastically dominates the Ising configuration for the infinite-volume measure with boundary conditions (roughly +speaking, the circuit of spin behaves like boundary conditions). We deduce that $\mu _ { \beta _ { c } } ^ { f }$+ +restricted to the box (in fact to any box) stochastically dominates$\mu _ { \beta _ { c } } ^ { + }$. This implies that$\mu _ { \beta _ { c } } ^ { f } \geq \mu _ { \beta _ { c } } ^ { + }$. Since the other inequality is obvious,$\mu _ { \beta _ { c } } ^ { f }$and$\mu _ { \beta _ { c } } ^ { + }$are equal.

≥Via Edwards-Sokal’s coupling again,$\phi _ { p _ { s d } , 2 } ^ { 0 } = \phi _ { p _ { s d } , 2 } ^ { 1 }$and there is no infinite cluster at criticality. Moreover,$\mu _ { \beta _ { c } } ^ { - } = \mu _ { \beta _ { c } } ^ { f } = \mu _ { \beta _ { c } } ^ { + }$=and there is a unique infinite-volume Ising measure at criticality.□

Remark 3.11. More generally, the FK percolation with integer parameter$q \geq 2$can ≥be coupled with Potts models. Many properties of Potts models are derived using FK percolation, since we have the FKG inequality at our disposal, while there is no equivalent of the spin-Ising FKG inequality for Potts models.

## 3.3 Loop representation of the FK-Ising model and fermionic observable

Let$( \Omega , a , b )$be a simply connected domain with two marked points on the boundary. Let$\Omega _ { \delta }$)be an approximation of$\Omega .$and let$\partial _ { a b }$and$\partial _ { b a }$denote the counterclockwise arcs in the boundary$\partial \Omega _ { \delta }$joining a to b (resp. b to$a )$. We consider a FK-Ising measure with wired boundary conditions on$\partial _ { b a } \textrm { -- }$all the edges are pairwise connected – and free boundary conditions on the arc$\partial _ { a b }$. These boundary conditions are called the Dobrushin boundary conditions. We denote by$\phi _ { \Omega _ { \delta } , p } ^ { a , b }$the associated FK-Ising measure with parameter$p .$

The dual boundary arc$\partial _ { b a } ^ { \star }$is the set of sites of$\Omega _ { \delta } ^ { \star }$adjacent to$\partial _ { b a }$while the dual boundary arc$\partial _ { a b } ^ { \star }$is the set of sites of$\mathbb { L } _ { \delta } ^ { \star } \setminus \Omega _ { \delta } ^ { \star }$adjacent to$\partial _ { a b } .$, see${ \mathrm { F i g . } }$. 6. A FK-Dobrushin domain$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$is given by

• a medial graph$\Omega _ { \delta } ^ { \circ }$defined as the set of medial vertices associated to edges of$\Omega _ { \delta }$ and to dual edges of$\partial _ { a b } ^ { \star }$

• medial sites$a _ { \delta } , b _ { \delta } \in \Omega _ { \delta } ^ { \circ }$between arcs$\partial _ { b a }$an$\partial _ { a b } ^ { \star } ,$, see Fig. 6 again,

with the additional condition that$b _ { \delta }$is the southeast corner of a black face belonging to the domain.

Remark 3.12. Note that the definition of$\Omega _ { \delta } ^ { \circ }$is not the same as in Section 1.2.1 since we added medial vertices associated to dual edges of$\partial _ { a b } ^ { \star }$. We chose this definition to make sites of the dual and the primal lattices play symmetric roles. The condition that $b _ { \delta }$is the south corner of a black face belonging to the domain is a technical condition.

Let$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$be a FK-Dobrushin domain. For any FK-Ising configuration with ( )Dobrushin boundary conditions on$\Omega _ { \delta }$, we construct a loop configuration on$\Omega _ { \delta } ^ { \circ }$as follows: The interfaces between the primal clusters and the dual clusters (i.e clusters in

![](images/page_20_image_0.jpg)

Figure 6: A domain$\Omega _ { \delta }$with Dobrushin boundary conditions: the vertices of the primal graph are black, the vertices of the dual graph$\Omega _ { \delta } ^ { \star }$are white, and between them lies the medial graph$\Omega _ { \delta } ^ { \circ }$. The arcs$\partial _ { b a }$and$\partial _ { a b } ^ { \star }$are the two outermost arcs. Moreover, arcs$\partial _ { b a } ^ { \star }$ and$\partial _ { a b }$are the arcs bordering$\partial _ { b a }$and$\partial _ { a b } ^ { \star }$from the inside. The arcs$\partial _ { a b }$and$\partial _ { b a }$(resp. $\partial _ { a b } ^ { \star }$and$\partial _ { b a } ^ { \star } )$are drawn in solid lines (resp. dashed lines)

![](images/page_21_image_0.jpg)

Figure 7: A FK percolation configuration in the Dobrushin domain$\left( \Omega _ { \delta } , a _ { \delta } , b _ { \delta } \right)$, together ( )with the corresponding interfaces on the medial lattice: the loops are grey, and the exploration path γ from$a _ { \delta }$to$b _ { \delta }$is black. Note that the exploration path is the interface between the open cluster connected to the wired arc and the dual-open cluster connected to the white faces of the free arc.

the dual model) form a family of loops together with a path from$a _ { \delta }$to$b _ { \delta }$. The loops are drawn as shown in Figure 7 following the edges of the medial lattice. The orientation of the medial lattice naturally gives an orientation to the loops, so that we are working with a model of oriented loops on the medial lattice.

The curve from$a _ { \delta }$to$b _ { \delta }$is called the exploration path and denoted by$\gamma = \gamma ( \omega )$. It is the interface between the open cluster connected to$\partial _ { b a }$= ( )and the dual-open cluster connected to$\partial _ { a b } ^ { \star } .$. As in the Ising model case, one can study its scaling limit when the mesh size goes to 0:

Theorem 3.13 (Conformal invariance of the FK-Ising model, [KS10]). Let Ω be a simply connected domain with two marked points a, b on the boundary. Let$\gamma _ { \delta }$be the interface of the critical FK-Ising with Dobrushin boundary conditions on$\left( \Omega _ { \delta } , a _ { \delta } , b _ { \delta } \right)$ Then the law of γ<sub>δ</sub> converges weakly, when$\delta  0$( ), to the chordal Schramm-Loewner Evolution with$\kappa = 1 6 / 3$

As in the Ising model case, the proof of this theorem also involves a discrete observ able, which converges to a conformally invariant object. We define it now.

Definition 3.14. The edge FK fermionic observable is defined on edges of$\Omega _ { \delta } ^ { \circ }$by

$$
F _ {\Omega_ {\delta} ^ {\diamond}, a _ {\delta}, b _ {\delta}, p} (e) = \mathbb {E} _ {\Omega_ {\delta}, p} ^ {a _ {\delta}, b _ {\delta}} \big [ \mathrm{e} ^ {\frac {1}{2} \cdot \mathrm{i} W _ {\gamma} (e, b _ {\delta})} 1 _ {e \in \gamma} \big ],\tag{3.5}
$$

where$W _ { \gamma } ( e , b _ { \delta } )$denotes the winding between the center of e and$b _ { \delta }$.

( )The vertex FK fermionic observable is defined on vertices of$\Omega _ { \delta } ^ { \circ } \setminus \partial \Omega _ { \delta } ^ { \circ }$by

$$
F _ {\Omega_ {\delta} ^ {\diamond}, a _ {\delta}, b _ {\delta}, p} (v) = \frac {1}{2} \sum_ {e \sim v} F _ {\Omega_ {\delta} ^ {\diamond}, a _ {\delta}, b _ {\delta}, p} (e)\tag{3.6}
$$

where the sum is over the four medial edges having v as an endpoint.

When we consider the observable at criticality (which will be almost always the case), we drop the dependence on$p$in the notation. More generally, if$( \Omega , a , b )$is fixed, we simply denote the observable on$( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } , p _ { s d } )$by$F _ { \delta }$

The quantity$F _ { \delta } ( e )$( )is a complexified version of the probability that e belongs to ( )the exploration path. The complex weight makes the link between$F _ { \delta }$and probabilistic properties less explicit. Nevertheless, the vertex fermionic observable$F _ { \delta }$converges when δ goes to 0:

Theorem 3.15. [Smi10a] Let$( \Omega , a , b )$be a simply connected domain with two marked points on the boundary. Let$F _ { \delta }$( )be the vertex fermionic observable in$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$. Then, we have

$$
\frac {1}{\sqrt {2 \delta}} F _ {\delta} (\cdot) \rightarrow \sqrt {\phi^ {\prime} (\cdot)} \quad w h e n \delta \rightarrow 0\tag{3.7}
$$

uniformly on any compact subset of$\Omega ,$, where$\phi$is any conformal map from Ω to the strip R$\times \left( 0 , 1 \right)$mapping a to and b to$\infty$

As in the case of the spin Ising model, this statement is the heart of the proof of conformal invariance. Yet, the observable itself can be helpful for the understanding of other properties of the FK-Ising model. For instance, it enables us to prove a statement equivalent to the celebrated Russo-Seymour-Welsh Theorem for percolation. This result will be central for the proof of compactness of exploration paths (an important step in the proof of Theorems 2.10 and 3.13).

Theorem 3.16 (RSW-type crossing bounds, [DCHN10]). There exists a constant$c > 0$ such that for any rectangle R of size 4n$\times n _ { \colon }$, one has

$$
\phi_ {p _ {s d}, 2, R} ^ {0} (\text { there   exists   an   open   path   from   left   to   right }) \geq c.\tag{3.8}
$$

Before ending this section, we present a simple yet crucial result: we show that it is possible to compute rather explicitly the distribution of the loop representation. In particular, at criticality, the weight of a loop configuration depends only on the number of loops.

Proposition 3.17. Let$p \in ( 0 , 1 )$and let$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$be a FK Dobrushin domain, then for any configuration$\omega ,$

$$
\phi_ {\Omega_ {\delta}, p} ^ {a _ {\delta}, b _ {\delta}} (\omega) = \frac {1}{Z} x ^ {o (\omega)} \sqrt {2} ^ {\ell (\omega)}\tag{3.9}
$$

where$x = p / [ \sqrt { 2 } ( 1 - p ) ] , \ell ( \omega )$is the number of loops in the loop configuration associated to$\omega , o ( \omega )$/[ ( − )] ( )is the number of open edges, and$Z$is the normalization constant.

Proof Recall that

$$
\phi_ {\Omega_ {\delta}, p} ^ {a _ {\delta}, b _ {\delta}} (\omega) = \frac {1}{Z} [ p / (1 - p) ] ^ {o (\omega)} 2 ^ {k (\omega)}.
$$

Using arguments similar to Proposition 3.3, the dual of$\phi _ { \Omega _ { \delta } , p } ^ { a _ { \delta } , b _ { \delta } }$can be proved to be$\phi _ { \Omega _ { \delta } ^ { \star } , p ^ { \star } } ^ { b _ { \delta } , a _ { \delta } }$ (in this sense, Dobrushin boundary conditions are self-dual). With$\omega ^ { \star }$being the dual configuration of$\omega ,$we find

$$
\begin{array}{r c l} \phi_ {\Omega_ {\delta}, p} ^ {a _ {\delta}, b _ {\delta}} (\omega) & = & \sqrt {\phi_ {\Omega_ {\delta} , p} ^ {a _ {\delta} , b _ {\delta}} (\omega) \phi_ {\Omega_ {\delta} ^ {*} , p ^ {*}} ^ {b _ {\delta} , a _ {\delta}} (\omega^ {*})} \\ & = & \frac {1}{\sqrt {Z Z ^ {*}}} \sqrt {p / (1 - p)} ^ {o (\omega)} \sqrt {2} ^ {k (\omega)} \sqrt {p ^ {*} / (1 - p ^ {*})} ^ {o (\omega^ {*})} \sqrt {2} ^ {k (\omega^ {*})} \\ & = & \frac {1}{\sqrt {Z Z ^ {*}}} \sqrt {\frac {p (1 - p ^ {*})}{(1 - p) p ^ {*}}} ^ {o (\omega)} \sqrt {p ^ {*} / (1 - p ^ {*})} ^ {o (\omega^ {*}) + o (\omega)} \sqrt {2} ^ {k (\omega) + k (\omega^ {*})} \\ & = & \frac {\sqrt {2} \sqrt {p ^ {*} / (1 - p ^ {*})}}{\sqrt {Z Z ^ {*}}} ^ {o (\omega) + o (\omega^ {*})} x ^ {o (\omega)} \sqrt {2} ^ {k (\omega) + k (\omega^ {*}) - 1} \end{array}
$$

where the definition of$p ^ { \star }$was used to prove that$\frac { p ( 1 - p ^ { \star } ) } { ( 1 - p ) p ^ { \star } } ~ = ~ x ^ { 2 }$. Note that$\ell ( \omega ) =$ $k ( \omega ) + k ( \omega ^ { \star } ) - 1$and

$$
\tilde {Z} = \frac {\sqrt {Z Z ^ {\star}}}{\sqrt {2} \sqrt {p ^ {\star} / (1 - p ^ {\star})} o (\omega) + o (\omega^ {\star})}
$$

does not depend on the configuration (the sum$o ( \omega ) + o ( \omega ^ { \star } )$being equal to the total (number of edges). Altogether, this implies the claim.□

## 4 Discrete complex analysis on graphs

Complex analysis is the study of harmonic and holomorphic functions in complex domains. In this section, we shall discuss how to discretize harmonic and holomorphic functions, and what are the properties of these discretizations.

There are many ways to introduce discrete structures on graphs which can be developed in parallel to the usual complex analysis. We need to consider scaling limits (as the mesh of the lattice tends to zero), so we want to deal with discrete structures which converge to the continuous complex analysis as finer and finer graphs are taken.

## 4.1 Preharmonic functions

## 4.1.1 Definition and connection with random walks.

Introduce the (non-normalized) discretization of the Laplacian operator$\begin{array} { r } { \Delta \ : = \ \frac { 1 } { 4 } \big ( \partial _ { x x } ^ { 2 } + } \end{array}$ $\partial _ { y y } ^ { 2 } )$in the case of the square lattice$\mathbb { L } _ { \delta }$. For u L and$f : \mathbb { L } _ { \delta } \to \mathbb { C }$, define

$$
\Delta_ {\delta} f (u) = \frac {1}{4} \sum_ {v \sim u} \bigl (f (v) - f (u) \bigr).
$$

The definition extends to rescaled square lattices in a straightforward way (for instance to$\mathbb { L } _ { \delta } ^ { \diamond } )$.

Definition 4.1. A function$h : \Omega _ { \delta } \to \mathbb { C }$is preharmonic$( r e s p$. pre-superharmonic, pre-subharmonic)$i f \Delta _ { \delta } h ( x ) = 0 \ ( r e s p . \ \leq 0 , \geq 0 )$for every$\boldsymbol { x } \in \Omega _ { \delta }$

One fundamental tool in the study of preharmonic functions is the classical relation between preharmonic functions and simple random walks:

Let$( X _ { n } )$be a simple random walk killed at the first time it exits$\Omega _ { \delta } ;$; then h is ( )preharmonic on$\Omega _ { \delta }$if and only if$\left( h ( X _ { n } ) \right)$is a martingale.

Using this fact, one can prove that harmonic functions are determined by their value on$\partial \Omega _ { \delta }$, that they satisfy Harnack’s principle, etc. We refer to [Law91] for a deeper study on preharmonic functions and their link to random walks. Also note that the set of preharmonic functions is a complex vector space. As in the continuum, it is easy to see that preharmonic functions satisfy the maximum and minimum principles.

## 4.1.2 Derivative estimates and compactness criteria.

For general functions, a control on the gradient provides regularity estimates on the function itself. It is a well-known fact that harmonic functions satisfy the reverse property: controlling the function allows us to control the gradient. The following lemma shows that the same is true for preharmonic functions.

Proposition 4.2. There exists$C > 0$such that, for any preharmonic function$h : \Omega _ { \delta } \to \mathbb { C }$ and any two neighboring sites$x , y \in \Omega _ { \delta }$,

$$
\left| h (x) - h (y) \right| \leq C \delta \frac {\sup _ {z \in \Omega_ {\delta}} | h (z) |}{d \left(x , \Omega^ {c}\right)}.\tag{4.1}
$$

Proof Let$x , y \in \Omega _ { \delta }$. The preharmonicity of$h$translates to the fact that$h ( X _ { n } )$is ∈a martingale (where$X _ { n }$(is a simple random walk killed at the first time it exits$\Omega _ { \delta } )$ Therefore, for$x , y$two neighboring sites of$\Omega _ { \delta }$, we have

$$
h (x) - h (y) = \mathbb {E} \big [ h (X _ {\tau}) - h (Y _ {\tau^ {\prime}}) \big ]\tag{4.2}
$$

where under E, X and$Y$are two simple random walks starting respectively at x and $y ,$and$\tau , \tau ^ { \prime }$are any stopping times. Let$2 r = d ( x , \Omega ^ { c } ) > 0$, so that$\boldsymbol { U } = \boldsymbol { x } + [ - r , r ] ^ { 2 }$is included in$\Omega _ { \delta }$. Fix τ and$\tau ^ { \prime }$= ( )to be the hitting times of$\partial U _ { \delta }$= + [− ]and consider the following coupling of X and Y (one has complete freedom in the choice of the joint law in (4.2)): $( X _ { n } )$is a simple random walk and$Y _ { n }$is constructed as follows,

• if$X _ { 1 } = y$, then$Y _ { n } = X _ { n + 1 }$for$n \geq 0 ,$

• if$X _ { 1 } \neq y$, then$Y _ { n } = \sigma ( X _ { n + 1 } )$, where σ is the orthogonal symmetry with respect to ≠ = ( + )the perpendicular bisector \` of$[ X _ { 1 } , y ]$, whenever$X _ { n + 1 }$does not reach \`. As soon as it does, set$Y _ { n } = X _ { n + 1 }$

It is easy to check that Y is also a simple random walk. Moreover, we have

$$
\left| h (x) - h (y) \right| \leq \mathbb {E} \left[ | h \left(X _ {\tau}\right) - h \left(Y _ {\tau^ {\prime}}\right) \mid 1 _ {X _ {\tau} \neq Y _ {\tau^ {\prime}}} \right] \leq 2 \left(\sup _ {z \in \partial U _ {\delta}} | h (z) |\right) \mathbb {P} \left(X _ {\tau} \neq Y _ {\tau^ {\prime}}\right)
$$

Using the definition of the coupling, the probability on the right is known: it is equal to the probability that X does not touch \` before exiting the ball and is smaller than $\begin{array} { r } { \frac { C ^ { \prime } } { r } \delta } \end{array}$(with$C ^ { \prime }$a universal constant), since$U _ { \delta }$is of radius$r / \delta$for the graph distance. We deduce that

$$
\left| h (x) - h (y) \right| \leq 2 \left(\sup _ {z \in \partial U _ {\delta}} | h (z) |\right) \frac {C ^ {\prime}}{r} \delta \leq 2 \left(\sup _ {z \in \Omega_ {\delta}} | h (z) |\right) \frac {C ^ {\prime}}{r} \delta
$$

□

Recall that functions on$\Omega _ { \delta }$are implicitly extended to$\Omega .$

Proposition 4.3. A family$\left( h _ { \delta } \right) _ { \delta > 0 }$of preharmonic functions on the graphs$\Omega _ { \delta }$is pre-( ) >compact for the uniform topology on compact subsets of Ω if one of the following properties holds:

$( 1 ) \ ( h _ { \delta } ) _ { \delta > 0 }$is uniformly bounded on any compact subset of$\Omega$,

(2) for any compact subset K of Ω, there exists$M = M ( K ) > 0$such that$f o r$any $\delta > 0$,

$$
\delta^ {2} \sum_ {x \in K _ {\delta}} | h _ {\delta} (x) | ^ {2} \leq M.
$$

Proof Let us prove that the proposition holds under the first hypothesis and then that the second hypothesis implies the first one.

We are faced with a family of continuous maps$h _ { \delta } : \Omega \to \mathbb { C }$and we aim to apply ∶ →the Arzelà-Ascoli theorem. It is suficient to prove that the functions$h _ { \delta }$are uniformly Lipschitz on any compact subset since they are uniformly bounded on any compact subset of Ω. Let K be a compact subset of Ω. Proposition 4.2 shows that$\left| h _ { \delta } ( x ) - h _ { \delta } ( y ) \right| \leq$ $C _ { K } \delta$for any two neighbors$x , y \in K _ { \delta } ,$, where

$$
C _ {K} = C \frac {\sup _ {\delta > 0} \sup _ {x \in \Omega : d (x , K) \leq r / 2} | h _ {\delta} (x) |}{d (K , \Omega^ {c})},
$$

implying that$| h _ { \delta } ( x ) - h _ { \delta } ( y ) | \le 2 C _ { K } | x - y |$for any$x , y \in K _ { \delta }$(not necessarily neighbors). ∣ ( ) − ( )∣ ≤ ∣ − ∣The Arzelá-Ascoli theorem concludes the proof.

Now assume that the second hypothesis holds, and let us prove that$\left( h _ { \delta } \right) _ { \delta > 0 }$is bounded on any compact subset of Ω. Take$K \subset \Omega$compact, let$2 r = d ( K , \Omega ^ { c } ) > 0$>and consider$\boldsymbol { x } \in K _ { \delta }$⊂. Using the second hypothesis, there exists$k : = k ( x )$= (such that$\begin{array} { r } { \frac { r } { 2 \delta } \le k \le \frac { r } { \delta } } \end{array}$ and

$$
\delta \sum_ {y \in \partial U _ {k \delta}} | h _ {\delta} (y) | ^ {2} \leq 2 M / r,\tag{4.3}
$$

where$U _ { k \delta } = x + [ - \delta k , \delta k ] ^ { 2 }$is the box of size k (for the graph distance) around x and $M = M \big ( y + [ - r , r ] ^ { 2 } \big )$]. Exercise 4.4 implies

$$
h _ {\delta} (x) = \sum_ {y \in \partial U _ {k \delta}} h _ {\delta} (y) H _ {U _ {k \delta}} (x, y)\tag{4.4}
$$

for every$x \in U _ { \delta k }$. Using the Cauchy-Schwarz inequality, we find

$$
\begin{array}{r c l} h _ {\delta} (x) ^ {2} & = & \left(\sum_ {y \in \partial U _ {k \delta}} h _ {\delta} (y) H _ {U _ {k \delta}} (x, y)\right) ^ {2} \\ & \leq & \left(\delta \cdot \sum_ {y \in \partial U _ {k \delta}} | h _ {\delta} (y) | ^ {2}\right) \left(\frac {1}{\delta} \cdot \sum_ {y \in \partial U _ {k \delta}} H _ {U _ {k \delta}} (x, y) ^ {2}\right) \leq 2 M / r \cdot C. \end{array}
$$

where$C$is a uniform constant. The last inequality used Exercise 4.5 to afirm that $H _ { U _ { k \delta } } ( x , y ) \leq C \delta$for some$C = C ( r ) > 0$□

Exercise 4.4. The discrete harmonic measure$H _ { \Omega _ { \delta } } ( \cdot , y )$of$y \in \partial \Omega _ { \delta }$is the unique harmonic function on$\Omega _ { \delta } \setminus \partial \Omega _ { \delta }$(⋅vanishing on the boundary$\partial \Omega _ { \delta }$∈, except at$y ,$where it equals 1. Equivalently,$H _ { \Omega _ { \delta } } ( x , y )$is the probability that a simple random walk starting from x exits$\Omega _ { \delta } \setminus \partial \Omega _ { \delta }$( )through y. Show that for any harmonic function$h : \Omega _ { \delta } \to \mathbb { C }$2

$$
h = \sum_ {y \in \partial \Omega_ {\delta}} h (y) H _ {\Omega_ {\delta}} (\cdot , y).
$$

Exercise 4.5. Prove that there exists$C > 0$such that$H _ { Q _ { \delta } } ( 0 , y ) \leq C \delta$for every$\delta > 0$ and$y \in \partial Q _ { \delta }$, where$Q = [ - 1 , 1 ] ^ { 2 }$

## 4.1.3 Discrete Dirichlet problem and convergence in the scaling limit.

Preharmonic functions on square lattices of smaller and smaller mesh size were studied in a number of papers in the early twentieth century (see e.g. [PW23, Bou26, Lus26]), culminating in the seminal work of Courant, Friedrichs and Lewy. It was shown in [CFL28] that solutions to the Dirichlet problem for a discretization of an elliptic operator converge to the solution of the analogous continuous problem as the mesh of the lattice tends to zero. A first interesting fact is that the limit of preharmonic functions is indeed harmonic.

Proposition 4.6. Any limit of a sequence of preharmonic functions on$\Omega _ { \delta }$converging uniformly on any compact subset of Ω is harmonic in Ω.

Proof Let$\left( h _ { \delta } \right)$be a sequence of preharmonic functions on$\Omega _ { \delta }$converging to h. Via ( )Propositions 4.2 and 4.3,$( \mathit { \Pi } _ { \overline { { \delta } } } ^ { 1 } [ h _ { \delta } ( \cdot + \mathit { \bar { \delta } } ) - h _ { \delta } ] ) _ { \delta > 0 }$is precompact. Since$\partial _ { x } h$is the only ( [ (⋅ + ) − ])possible sub-sequential limit of the sequence,$\textstyle \big ( \frac { 1 } { \sqrt { 2 } \delta } \big [ h _ { \delta } \big ( \cdot + \delta \big ) - h _ { \delta } \big ] \big ) _ { \delta > 0 }$converges (indeed its discrete primitive converges to$h )$( [ (⋅ + ) − ]) >. Similarly, one can prove convergence of discrete derivatives of any order. In particular,$\begin{array} { r } { 0 = \frac { 1 } { 2 \delta ^ { 2 } } \Delta _ { \delta } h _ { \delta } } \end{array}$converges to$\textstyle { \frac { 1 } { 4 } } \left[ \partial _ { x x } h + \partial _ { y y } h \right]$. Therefore, h is harmonic.□

In particular, preharmonic functions with a given boundary value problem converge in the scaling limit to a harmonic function with the same boundary value problem in a rather strong sense, including convergence of all partial derivatives. The finest result of convergence of discrete Dirichlet problems to the continuous ones will not be necessary in our setting and we state the minimal required result:

Theorem 4.7. Let Ω be a simply connected domain with two marked points a and b on the boundary, and$f$a bounded continuous function on the boundary of Ω. Let $f _ { \delta } : \partial \Omega _ { \delta }  \mathbb { C }$be a sequence of uniformly bounded functions converging uniformly away ∶ →from a and b to$f .$Let$h _ { \delta }$be the unique preharmonic map on$\Omega _ { \delta }$such that$( h _ { \delta } ) _ { | \partial \Omega _ { \delta } } = f _ { \delta }$ Then

$$
h _ {\delta} \longrightarrow h \quad w h e n \delta \rightarrow 0
$$

uniformly on compact subsets of Ω, where h is the unique harmonic function on$\Omega _ { i }$ continuous on${ \overline { { \Omega } } } ,$, satisfying$h _ { | \partial \Omega } = f$

Proof Since$( f _ { \delta } ) _ { \delta > 0 }$is uniformly bounded by some constant$M ,$, the minimum and ( ) >maximum principles imply that$\left( h _ { \delta } \right) _ { \delta > 0 }$is bounded by$M$. Therefore, the family$\left( h _ { \delta } \right)$is (precompact (Proposition 4.3). Let$\tilde { h }$) >be a sub-sequential limit. Necessarily,$\tilde { h }$( )is harmonic inside the domain (Proposition 4.6) and bounded. To prove that${ \tilde { h } } = h$, it sufices to show that$\ddot { h }$can be continuously extended to the boundary by$f .$

Let$x \in \partial \Omega \setminus \{ a , b \}$and$\varepsilon > 0$. There exists$R > 0$such that for$\delta$small enough,

$$
\left| f _ {\delta} \left(x ^ {\prime}\right) - f _ {\delta} (x) \right| <   \varepsilon \quad \text { for   every } x ^ {\prime} \in \partial \Omega \cap Q (x, R),
$$

where$Q ( x , R ) = x + [ - R , R ] ^ { 2 }$. For$r < R$and$y \in Q ( x , r )$, we have

$$
\left| h _ {\delta} (y) - f _ {\delta} (x) \right| = \mathbb {E} _ {y} \big [ f _ {\delta} (X _ {\tau}) - f _ {\delta} (x) \big ]
$$

for X a random walk starting at$y ,$and τ its hitting time of the boundary. Decomposing between walks exiting the domain inside$Q ( x , R )$and others, we find

$$
\left| h _ {\delta} (y) - f _ {\delta} (x) \right| \leq \varepsilon + 2 M \mathbb {P} _ {y} \left[ X _ {\tau} \notin Q (x, R) \right]
$$

Exercise 4.8 guarantees that$\mathbb { P } _ { y } [ X _ { \tau } \notin Q ( x , R ) ] \le ( r / R ) ^ { \alpha }$for some independent constant $\alpha > 0$. Taking$r = R ( \varepsilon / 2 M ) ^ { 1 / \alpha }$[ ∉ ( )] ≤ ( / )and letting δ go to 0, we obtain$| \tilde { h } ( y ) - f ( x ) | \leq 2 \varepsilon$for >every$y \in Q ( x , r )$□

Exercise 4.8. Show that there exists$\alpha > 0$such that for any 1$r > \delta > 0$and any curve$\gamma$inside$\mathbb { D } : = \{ z : | z | < 1 \}$from$C = \{ z : | z | = 1 \}$to$\left\{ z : | z | = r \right\}$≫ > >, the probability for a random walk on$\mathbb { D } _ { \delta }${ ∶ ∣ ∣ < }starting at 0 to exit$( { \mathbb D } \setminus \gamma ) _ { \delta }$= } {through$C$∣ ∣ = }is smaller than$r ^ { \alpha }$. To prove $t h i s ,$one can show that in any annulus$\{ z : x \leq | z | \leq 2 x \}$, the random walk trajectory has { ∶ ≤ ∣ ∣ ≤ }a uniformly positive probability to close a loop around the origin.

## 4.1.4 Discrete Green functions

This paragraph concludes the section by mentioning the important example of discrete Green functions. For$y \in \Omega _ { \delta } \setminus \partial \Omega _ { \delta } .$, let$G _ { \Omega _ { \delta } } ( \cdot , y )$be the discrete Green function in the domain$\Omega _ { \delta }$∈ ∖ (⋅ )with singularity at y, i.e. the unique function on$\Omega _ { \delta }$such that

• its Laplacian on$\Omega _ { \delta } \setminus \partial \Omega _ { \delta }$equals 0 except at$y ,$where it equals$1 ,$9

$G _ { \Omega _ { \delta } } ( \cdot , y )$vanishes on the boundary$\partial \Omega _ { \delta }$

The quantity$\mathbf { \sigma } - G _ { \Omega _ { \delta } } ( x , y )$is the number of visits at x of a random walk started at$y$and − ( )stopped at the first time it reaches the boundary. Equivalently, it is also the number of visits at$y$of a random walk started at x stopped at the first time it reaches the boundary. Green functions are very convenient, in particular because of the Riesz representation formula for (not necessarily harmonic) functions:

Proposition 4.9 (Riesz representation formula). Let$f : \Omega _ { \delta } \to \mathbb { C }$be a function vanishing on$\partial \Omega _ { \delta }$. We have

$$
f = \sum_ {y \in \Omega_ {\delta}} \Delta_ {\delta} f (y) G _ {\Omega_ {\delta}} (\cdot , y).
$$

Proof Note that$\begin{array} { r } { f - \sum _ { y \in \Omega _ { \delta } } \Delta _ { \delta } f ( y ) G _ { \Omega _ { \delta } } ( \cdot , y ) } \end{array}$is harmonic and vanishes on the boundary. −∑ ∈Hence, it equals 0 everywhere.□

Finally, a regularity estimate on discrete Green functions will be needed. This proposition is slightly technical. In the following,$a Q _ { \delta } = [ - a , a ] ^ { 2 } \cap \mathbb { L } _ { \delta }$and$\nabla _ { x } f ( x ) =$ $( f ( x + \delta ) - f ( x ) , f ( x + i \delta ) - f ( x ) )$

Proposition 4.10. There exists$C > 0$such that for any$\delta > 0$and$y \in \mathfrak { g } Q _ { \delta }$，

$$
\sum_ {x \in Q _ {\delta}} | \nabla_ {x} G _ {9 Q _ {\delta}} (x, y) | \leq C \delta \sum_ {x \in Q _ {\delta}} G _ {9 Q _ {\delta}} (x, y).
$$

Proof In the proof,$C _ { 1 } , . . . , C _ { 6 }$denote universal constants. First assume$y \in 9 Q _ { \delta } \setminus 3 Q _ { \delta }$ Using random walks, one can easily show that there exists$C _ { 1 } > 0$∈such that

$$
\frac {1}{C _ {1}} G _ {9 Q _ {\delta}} (x, y) \leq G _ {9 Q _ {\delta}} (x ^ {\prime}, y) \leq C _ {1} G _ {9 Q _ {\delta}} (x, y)
$$

for every$x , x ^ { \prime } \in 2 Q _ { \delta }$(this is a special application of Harnack’s principle). Using Propo-∈sition 4.2, we deduce

$$
\sum_ {x \in Q _ {\delta}} | \nabla_ {x} G _ {9 Q _ {\delta}} (x, y) | \leq \sum_ {x \in Q _ {\delta}} C _ {2} \delta \max _ {x \in 2 Q _ {\delta}} G _ {9 Q _ {\delta}} (x, y) \leq C _ {1} C _ {2} \delta \sum_ {x \in Q _ {\delta}} G _ {9 Q _ {\delta}} (x, y)
$$

which is the claim for$y \in 9 Q _ { \delta } \setminus 3 Q _ { \delta }$

Assume now that$y \in \mathrm { 3 Q } _ { \delta }$∖. Using the fact that$G _ { 9 Q _ { \delta } } ( x , y )$is the number of visits of ∈x for a random walk starting at$y$( )(and stopped on the boundary), we find

$$
\sum_ {x \in Q _ {\delta}} G _ {9 Q _ {\delta}} (x, y) \geq C _ {3} / \delta^ {2}.
$$

Therefore, it sufices to prove$\begin{array} { r } { \sum _ { x \in Q _ { \delta } } \left| \nabla G _ { 9 Q _ { \delta } } ( x , y ) \right| \le C _ { 4 } / \delta } \end{array}$. Let$G _ { \mathbb { L } _ { \delta } }$be the Green function ∑ ∈ ∣∇ ( )∣ ≤ /in the whole plane, i.e. the function with Laplacian equal to$\delta _ { x , y } ,$normalized so that $G _ { \mathbb { L } _ { \delta } } ( y , y ) = 0$, and with sublinear growth. This function has been widely studied, it was ( ) =proved in [MW40] that

$$
G _ {\mathbb {L} _ {\delta}} (x, y) = \frac {1}{\pi} \ln \left(\frac {| x - y |}{\delta}\right) + C _ {5} + o \left(\frac {\delta}{| x - y |}\right).
$$

Now,$\begin{array} { r } { G _ { \mathbb { L } _ { \delta } } ( \cdot , y ) - G _ { 9 Q _ { \delta } } ( \cdot , y ) - \frac { 1 } { \pi } \ln \left( \frac { 1 } { \delta } \right) } \end{array}$is harmonic and has bounded boundary conditions on$\partial 9 Q _ { \delta }$(⋅ ) − (⋅ ) − ( ). Therefore, Proposition 4.2 implies

$$
\sum_ {x \in Q _ {\delta}} \left| \nabla_ {x} \big (G _ {\mathbb {L} _ {\delta}} (x, y) - G _ {9 Q _ {\delta}} (x, y) \big) \right| \leq C _ {6} \delta \cdot 1 / \delta^ {2} = C _ {6} / \delta .
$$

Moreover, the asymptotic of$G _ { \mathbb { L } _ { \delta } } ( \cdot , y )$leads to

$$
\sum_ {x \in Q _ {\delta}} \left| \nabla_ {x} G _ {\mathbb {L} _ {\delta}} (x, y) \right| \leq C _ {7} / \delta .
$$

Summing the two inequalities, the result follows readily.

## 4.2 Preholomorphic functions

## 4.2.1 Historical introduction

Preholomorphic functions appeared implicitly in Kirchhof’s work [Kir47], in which a graph is modeled as an electric network. Assume every edge of the graph is a unit resistor and for$u \sim v$, let$F ( u v )$be the current from u to v. The first and the second ∼ ( )Kirchhof’s laws of electricity can be restated:

• the sum of currents flowing from a vertex is zero:

$$
\sum_ {v \sim u} F (u v) = 0,\tag{4.5}
$$

• the sum of the currents around any oriented closed contour$\gamma$is zero:

$$
\sum_ {[ u v ] \in \gamma} F (u v) = 0.\tag{4.6}
$$

Diferent resistances amount to putting weights into (4.5) and (4.6). The second law is equivalent to saying that F is given by the gradient of a potential function H, and the first equivalent to H being preharmonic.

Besides the original work of Kirchhof, the first notable application of preholomorphic functions is perhaps the famous article [BSST40] of Brooks, Smith, Stone and Tutte, where preholomorphic functions were used to construct tilings of rectangles by squares.

Preholomorphic functions distinctively appeared for the first time in the papers [Isa41, Isa52] of Isaacs, where he proposed two definitions (and called such functions mono-difric). Both definitions ask for a discrete version of the Cauchy-Riemann equations$\partial _ { i \alpha } F = i \partial _ { \alpha } F$or equivalently that the z¯-derivative is 0. In the first definition, the =equation that the function must satisfy is

$$
i [ f (E) - f (S) ] = f (W) - f (S)
$$

while in the second, it is

$$
i [ f (E) - f (W) ] = f (N) - f (S),
$$

where$N , E , S$and W are the four corners of a face. A few papers of his and other mathematicians followed, studying the first definition, which is asymmetric on the square lattice. The second (symmetric) definition was reintroduced by Ferrand, who also discussed the passage to the scaling limit and gave new proofs of Riemann uniformization and the Courant-Friedrichs-Lewy theorems [Fer44, LF55]. This was followed by extensive studies of Dufin and others, starting with [Duf56].

## 4.3 Isaacs’s definition of preholomorphic functions

We will be working with Isaacs’s second definition (although the theories based on both definitions are almost the same). The definition involves the following discretization of the$\bar { \partial } = \partial _ { x } + i \partial _ { y }$operator. For a complex valued function$f$on$\mathbb { L } _ { \delta }$(or on a finite subgraph =of it), and$\boldsymbol { x } \in \mathbb { L } _ { \delta } ^ { \star }$, define

$$
\bar {\partial} _ {\delta} f (x) = \frac {1}{2} [ f (E) - f (W) ] + \frac {i}{2} [ f (N) - f (S) ]
$$

where$N , E , S$and W denote the four vertices adjacent to the dual vertex x indexed in the obvious way.

Remark 4.11. When defining derivation, one uses duality between a graph and its dual. Quantities related to the derivative of a function on$G$are defined on the dual graph$G ^ { \star }$ Similarly, notions related to the second derivative are defined on the graph G again, whereas a primitive would be defined on$G ^ { \star }$

Definition 4.12. A function$f : \Omega _ { \delta } \to \mathbb { C }$is called preholomorphic if$\bar { \partial } _ { \delta } f ( x ) = 0$for every$\boldsymbol { x } \in \Omega _ { \delta } ^ { \star }$. For$x \in \Omega _ { \delta } ^ { \star } , \bar { \partial } _ { \delta } f ( x ) = 0$→ ( ) =is called the discrete Cauchy-Riemann equation at x.

The theory of preholomorphic functions starts much like the usual complex analysis. Sums of preholomorphic functions are also preholomorphic, discrete contour integrals vanish, primitive (in a simply-connected domain) and derivative are well-defined and are preholomorphic functions on the dual square lattice, etc. In particular, the (discrete) gradient of a preharmonic function is preholomorphic (this property has been proposed as a suitable generalization in higher dimensions).

Exercise 4.13. Prove that the restriction of a continuous holomorphic function to$\mathbb { L } _ { \delta }$ satisfies discrete Cauchy-Riemann equations up to$O ( \delta ^ { 3 } )$

Exercise 4.14. Prove that any preholomorphic function is preharmonic for a slightly modified Laplacian (the average over edges at distance$\sqrt { 2 } \delta$minus the value at the point). Prove that the (discrete) gradient of a preharmonic function is preholomorphic (this property has been proposed as a suitable generalization in higher dimensions). Prove that the limit of preholomorphic functions is holomorphic.

Exercise 4.15. Prove that the integral of a preholomorphic function along a discrete contour vanishes. Prove that the primitive and the diferential of preholomorphic functions are preholomorphic.

Exercise 4.16. Prove that$\frac { 1 } { \sqrt { 2 } \delta } \bar { \partial } _ { \delta }$and$\textstyle { \frac { 1 } { 2 \delta ^ { 2 } } } \Delta _ { \delta }$converge (when$\delta  0 )$to$\partial , { \bar { \partial } }$and$\Delta$in the sense of distributions.

## 4.4 s-holomorphic functions

As explained in the previous sections, the theory of preholomorphic functions starts like the continuum theory. Unfortunately, problems arrive quickly. For instance, the square of a preholomorphic function is no longer preholomorphic in general. This makes the theory of preholomorphic functions significantly harder than the usual complex analysis, since one cannot transpose proofs from continuum to discrete in a straightforward way. In order to partially overcome this dificulty, we introduce s-holomorphic functions (for spin-holomorphic), a notion that will be central in the study of the spin and FK fermionic observables.

## 4.4.1 Definition of s-holomorphic functions

To any edge of the medial lattice$e ,$we associate a line$\ell ( e )$passing through the origin and$\sqrt { \bar { e } }$( )(the choice of the square root is not important, and recall that e being oriented, it can be thought of as a complex number). The diferent lines associated with medial edges on$\mathbb { L } _ { \delta } ^ { \diamond }$are$\mathbb { R } , \ : \mathrm { e } ^ { i \pi / 4 } \mathbb { R }$, iR and$\mathrm { e } ^ { 3 i \pi / 4 } \mathbb { R }$, see Fig. 8.

Definition 4.17. A function$f : \Omega _ { \delta } ^ { \circ } \to \mathbb { C }$is s-holomorphic if for any edge e of$\Omega _ { \delta } ^ { \circ }$, we have

$$
P _ {\ell (e)} [ f (x) ] = P _ {\ell (e)} [ f (y) ]
$$

where$x , y$are the endpoints of e and$P _ { \ell }$is the orthogonal projection on$\ell .$

![](images/page_31_image_0.jpg)

Figure 8: Lines$\ell ( e )$for medial edges around a white face.

The definition of s-holomorphicity is not rotationally invariant. Nevertheless,$f$is s-holomorphic if and only if$\mathrm { e } ^ { i \pi \mathsf { \bar { I } } 4 } f ( i \cdot )$(resp.$i f ( - \cdot ) )$is s-holomorphic.

Proposition 4.18. Any s-holomorphic function$f : \Omega _ { \delta } ^ { \circ } \to \mathbb { C }$is preholomorphic on$\Omega _ { \delta } ^ { \circ }$

Proof Let$f : \Omega _ { \delta } ^ { \circ } \to \mathbb { C }$be a s-holomorphic function. Let v be a vertex of$\mathbb { L } _ { \delta } \cup \mathbb { L } _ { \delta } ^ { \star }$(this ∶ →is the vertex set of the dual of the medial lattice). Assume that v$\in \Omega _ { \delta } ^ { \star }$∪, the other case is similar. We aim to show that$\bar { \partial } _ { \delta } f ( \boldsymbol { v } ) = 0$∈. Let NW, NE, SE and SW be the four ( ) =vertices around v as illustrated in Fig. 8. Next, let us write relations provided by the s-holomorphicity, for instance

$$
P _ {\mathbb {R}} [ f (N W) ] = P _ {\mathbb {R}} [ f (N E) ].
$$

Expressed in terms of$f$and its complex conjugate$\bar { f }$only, we obtain

$$
f (N W) + \overline {{f (N W)}} = f (N E) + \overline {{f (N E)}}.
$$

Doing the same with the other edges, we find

$$
\begin{array}{r c l} f (N E) + i \overline {{f (N E)}} & = & f (S E) + i \overline {{f (S E)}} \\ f (S E) - \overline {{f (S E)}} & = & f (S W) - \overline {{f (S W)}} \\ f (S W) - i \overline {{f (S W)}} & = & f (N W) - i \overline {{f (N W)}} \end{array}
$$

Multiplying the second identity by i, the third by 1, the fourth by i, and then summing the four identities, we obtain

$$
0 = (1 - i) [ f (N W) - f (S E) + i f (S W) - i f (N E) ] = 2 (1 - i) \bar {\partial} _ {\delta} f (v)
$$

which is exactly the discrete Cauchy-Riemann equation in the medial lattice.

## 4.4.2 Discrete primitive of$F ^ { 2 }$

One might wonder why s-holomorphicity is an interesting concept, since it is more restrictive than preholomorphicity. The answer comes from the fact that a relevant discretization of$\textstyle { \mathrm { ~ \hat { \frac { 1 } { 2 } } I m } } { \bigl ( } \int ^ { z } f ^ { 2 } { \bigr ) }$can be defined for s-holomorphic functions$f .$

Theorem 4.19. Let$f : \Omega _ { \delta } ^ { \circ } \to \mathbb { C }$be an s-holomorphic function on the discrete simply connected domain$\Omega _ { \delta } ^ { \circ } { } _ { i }$∶, and$b _ { 0 } \in \Omega _ { \delta }$. Then, there exists a unique function$H : \Omega _ { \delta } \cup \Omega _ { \delta } ^ { \star }  \mathbb { C }$ such that

$$
\begin{array}{r c l} H (b _ {0}) & = & 1 \quad a n d \\ H (b) - H (w) & = & \delta \left| P _ {\ell (e)} [ f (x) ] \right| ^ {2} \left(= \delta \left| P _ {\ell (e)} [ f (y) ] \right| ^ {2}\right) \end{array}
$$

for every edge$e = [ x y ] ~ o f \Omega _ { \delta } ^ { \circ }$bordered by a black face$b \in \Omega _ { \delta }$and a white face w$\in \Omega _ { \delta } ^ { \star }$

![](images/page_32_image_0.jpg)

Figure 9: Arrows corresponding to contributions to$2 \Delta H ^ { \bullet }$. Note that arrows from black to white contribute negatively, those from white to black positively.

An elementary computation shows that for two neighboring sites$b _ { 1 } , b _ { 2 } \in \Omega _ { \delta }$, with v being the medial vertex at the center of$\left[ b _ { 1 } b _ { 2 } \right]$2

$$
H (b _ {1}) - H (b _ {2}) = \frac {1}{2} \mathrm{Im} [ f (v) ^ {2} \cdot (b _ {1} - b _ {2}) ],
$$

the same relation holding for sites of$\Omega _ { \delta } ^ { \star }$. This legitimizes the fact that H is a discrete analogue of${ \textstyle \frac { 1 } { 2 } } \mathrm { I m } \left( \int ^ { z } f ^ { 2 } \right)$

Proof The uniqueness of H is straightforward since$\Omega _ { \delta } ^ { \circ }$is simply connected. To obtain the existence, construct the value at some point by summing increments along an arbitrary path from$b _ { 0 }$to this point. The only thing to check is that the value obtained does not depend on the path chosen to define it. Equivalently, we must check the second Kirchhof’s law. Since the domain is simply connected, it is suficient to check it for elementary square contours around each medial vertex v (these are the simplest closed contours). Therefore, we need to prove that

$$
\left| P _ {\ell (n)} [ f (v) ] \right| ^ {2} - \left| P _ {\ell (e)} [ f (v) ] \right| ^ {2} + \left| P _ {\ell (s)} [ f (v) ] \right| ^ {2} - \left| P _ {\ell (w)} [ f (v) ] \right| ^ {2} = 0,\tag{4.7}
$$

where$n , e , s$and w are the four medial edges with endpoint$v ,$indexed in the obvious way. Note that$\ell ( n )$and$\ell ( s ) \ ( \mathrm { r e s p . } \ \ell ( e )$and$\ell ( w ) )$are orthogonal. Hence, (4.7) follows from

$$
\left| P _ {\ell (n)} [ f (v) ] \right| ^ {2} + \left| P _ {\ell (s)} [ f (v) ] \right| ^ {2} = | f (v) | ^ {2} = \left| P _ {\ell (e)} [ f (v) ] \right| ^ {2} + \left| P _ {\ell (w)} [ f (v) ] \right| ^ {2}.\tag{4.8}
$$

Even if the primitive of$f$is preholomorphic and thus preharmonic, this is not the case for H in general<sup>5</sup>. Nonetheless, H satisfies subharmonic and superharmonic properties. Denote by$H ^ { \bullet }$and$H ^ { \circ }$the restrictions of$H : \Omega _ { \delta } \cup \Omega _ { \delta } ^ { \star }  \mathbb { C }$to$\Omega _ { \delta }$(black faces) and$\Omega _ { \delta } ^ { \star }$ (white faces).

Proposition 4.20. If$f : \Omega _ { \delta } ^ { \circ } \to \mathbb { C }$is s-holomorphic, then$H ^ { \bullet }$and$H ^ { \circ }$are respectively ∶ →subharmonic and superharmonic.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>H is roughly (the imaginary part of) the primitive of the square of f.</span></small>

![](images/page_33_image_0.jpg)

Figure 10: The black graph is the isoradial graph. Grey vertices are the vertices on the dual graph. There exists a radius$r > 0$such that all faces can be put into an incircle >of radius r. Dual vertices have been drawn in such a way that they are the centers of these circles.

Proof Let B be a vertex of$\Omega _ { \delta } \setminus \partial \Omega _ { \delta }$. We aim to show that the sum of increments of $H ^ { \bullet }$between$B$∖and its four neighbors is positive. In other words, we need to prove that the sum of increments along the sixteen arrows drawn in Fig. 9 is positive. Let$a , b , c$ and d be the four values of$\sqrt { \delta } P _ { \ell ( e ) } [ f ( y ) ]$for every vertex$y \in \Omega _ { \delta } ^ { \circ }$around$B$and any edge$e = [ y z ]$bordering$B$( )[ ( )] ∈(there are only four diferent values thanks to the definition = [ ]of s-holomorphicity). An easy computation shows that the eight interior increments are thus$- a ^ { 2 } , \ - \bar { b ^ { 2 } } , \ - c ^ { 2 } , \ - d ^ { 2 }$(each appearing twice). Using the s-holomorphicity of$f$on −vertices of$\Omega _ { \delta } ^ { \circ }$− −around$B { \mathrm { , } }$, we can compute the eight exterior increments in terms of$a , b ,$ c and d: we obtain$( a { \sqrt { 2 } } - b ) ^ { 2 } , ( b { \sqrt { 2 } } - a ) ^ { 2 } , ( b { \sqrt { 2 } } - c ) ^ { 2 } , ( c { \sqrt { 2 } } - b ) ^ { 2 } , ( c { \sqrt { 2 } } - d ) ^ { 2 } , ( d { \sqrt { 2 } } - c ) ^ { 2 }$ $( d { \sqrt { 2 } } + a ) ^ { 2 } , ( a { \sqrt { 2 } } + { \dot { d } } ) ^ { 2 }$− ) ( − ) ( − ) ( − ). Hence, the sum S of increments equals

$$
{ S } { = } { 4 \big ( a ^ { 2 } + b ^ { 2 } + c ^ { 2 } + d ^ { 2 } \big ) - 4 \sqrt { 2 } \big ( a b + b c + c d - d a \big ) }\tag{4.9}
$$

$$
= 4 \left| \mathrm{e} ^ {- i \pi / 4} a - b + \mathrm{e} ^ {i 3 \pi / 4} c - i d \right| ^ {2} \geq 0.\tag{4.10}
$$

The proof for$H ^ { \circ }$follows along the same lines.

□

Remark 4.21. A subharmonic function in a domain is smaller than the harmonic function with the same boundary conditions. Therefore,$H ^ { \bullet }$is smaller than the harmonic function solving the same boundary value problem while$H ^ { \circ }$is bigger than the harmonic function solving the same boundary value problem. Moreover,$H ^ { \bullet } ( b )$is larger than $H ^ { \circ } ( w )$for two neighboring faces. Hence,$i f H ^ { \bullet }$and$H ^ { \circ }$( )are close to each other on the ( )boundary, then they are sandwiched between two harmonic functions with roughly the same boundary conditions. In this case, they are almost harmonic. This fact will be central in the proof of conformal invariance.

## 4.5 Isoradial graphs and circle packings

Dufin [Duf68] extended the definition of preholomorphic functions to isoradial graphs. Isoradial graphs are planar graphs that can be embedded in such a way that there exists $r > 0$so that each face has a circumcircle of same radius$r > 0$, see Fig. 10. When the > >embedding satisfies this property, it is said to be an isoradial embedding. We would like to point out that isoradial graphs form a rather large family of graphs. While not every topological quadrangulation (graph all of whose faces are quadrangles) admits a isoradial embedding, Kenyon and Schlenker [KS05] gave a simple necessary and suficient topological condition for its existence. It seems that the first appearance of a related family of graphs in the probabilistic context was in the work of Baxter [Bax89], where the eight-vertex model and the Ising model were considered on Z-invariant graphs, arising from planar line arrangements. These graphs are topologically the same as the isoradial ones, and though they are embedded diferently into the plane, by [KS05] they always admit isoradial embeddings. In [Bax89], Baxter was not considering scaling limits, and so the actual choice of embedding was immaterial for his results. However, weights in his models would suggest an isoradial embedding, and the Ising model was so considered by Mercat [Mer01], Boutilier and de Tilière [BdT11, BdT10], Chelkak and Smirnov [CS08] (see the last section for more details). Additionally, the dimer and the uniform spanning tree models on such graphs also have nice properties, see e.g. [Ken02]. Today, isoradial graphs seem to be the largest family of graphs for which certain lattice models, including the Ising model, have nice integrability properties (for instance, the star-triangle relation works nicely). A second reason to study isoradial graphs is that it is perhaps the largest family of graphs for which the Cauchy-Riemann operator admits a nice discretization. In particular, restrictions of holomorphic functions to such graphs are preholomorphic to higher orders. The fact that isoradial graphs are natural graphs both for discrete analysis and statistical physics sheds yet another light on the connection between the two domains.

In [Thu86], Thurston proposed circle packings as another discretization of complex analysis. Some beautiful applications were found, including yet another proof of the Riemann uniformization theorem by Rodin and Sullivan [RS87]. More interestingly, circle packings were used by He and Schramm [HS93] in the best result so far on the Koebe uniformization conjecture, stating that any domain can be conformally uniformized to a domain bounded by circles and points. In particular, they established the conjecture for domains with countably many boundary components. More about circle packings can be learned from Stephenson’s book [Ste05]. Note that unlike the discretizations discussed above, the circle packings lead to non-linear versions of the Cauchy-Riemann equations, see e.g. the discussion in [BMS05].

## 5 Convergence of fermionic observables

In this section, we prove the convergence of fermionic observables at criticality (Theorems 2.11 and 3.15). We start with the easier case of the FK-Ising model. We present the complete proof of the convergence, the main tool being the discrete complex analysis that we developed in the previous section. We also sketch the proof of the convergence for the spin Ising model.

## 5.1 Convergence of the FK fermionic observable

In this section, fix a simply connected domain$( \Omega , a , b )$with two points on the boundary. For$\delta > 0$( ), always consider a discrete FK Dobrushin domain$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$and the critical > ( )FK-Ising model with Dobrushin boundary conditions on it. Since the domain is fixed, set$F _ { \delta } = F _ { \Omega _ { \delta } ^ { \diamond } , a _ { \delta } , b _ { \delta } , p _ { s d } }$for the FK fermionic observable.

=The proof of convergence is in three steps:

• First, prove the s-holomorphicity of the observable.

• Second, prove the convergence of the function$H _ { \delta }$naturally associated to the sholomorphic functions$F _ { \delta } / \sqrt { 2 \delta }$

• Third, prove that$F _ { \delta } / \sqrt { 2 \delta }$converges to$\sqrt { \phi ^ { \prime } }$

## 5.1.1 s-holomorphicity of the (vertex) fermionic observable for FK-Ising.

The next two lemmata deal with the edge fermionic observable. They are the key steps of the proof of the s-holomorphicity of the vertex fermionic observable.

Lemma 5.1. For an edge$e \in \Omega _ { \delta } ^ { \circ } , F _ { \delta } ( e )$belongs to$\ell ( e )$

Proof The winding at an edge e can only take its value in the set$W + 2 \pi \mathbb { Z }$where W +is the winding at e of an arbitrary interface passing through e. Therefore, the winding weight involved in the definition of$F _ { \delta } ( e )$is always proportional to$\mathrm { e } ^ { \mathrm { i } W / 2 }$with a real coeficient, thus$F _ { \delta } ( e )$(is proportional to$\mathrm { e } ^ { i W / 2 }$. In any FK Dobrushin domain,$b _ { \delta }$is the ( )southeast corner and the last edge is thus going to the right. Therefore$\mathrm { e } ^ { i W / 2 }$belongs to$\ell ( e )$for any e and so does$F _ { \delta } ( e )$□

Even though the proof is finished, we make a short parenthetical remark: the definition of s-holomorphicity is not rotationally invariant, nor is the definition of FK Dobrushin domains, since the medial edge pointing to$b _ { \delta }$has to be oriented southeast. The latter condition has been introduced in such a way that this lemma holds true. Even though this condition seems arbitrary, it has no influence on the convergence result, meaning that one could perform a (slightly modified) proof with another orientation.

Lemma 5.2. Consider a medial vertex v in$\Omega _ { \delta } ^ { \circ } \setminus \partial \Omega _ { \delta } ^ { \circ }$. We have

$$
F _ {\delta} (N) - F _ {\delta} (S) = i \big [ F _ {\delta} (E) - F _ {\delta} (W) \big ]\tag{5.1}
$$

where$N , E , S$and W are the adjacent edges indexed in clockwise order.

Proof Let us assume that v corresponds to a primal edge pointing SE to$N W$, see Fig. 11. The case NE to$S W$is similar.

We consider the involution s (on the space of configurations) which switches the state (open or closed) of the edge of the primal lattice corresponding to v. Let e be an edge of the medial graph and set

$$
{e _ {\omega}} {:=} {\phi_ {\Omega_ {\delta} ^ {\diamond}, a _ {\delta}, b _ {\delta}, p _ {s d}} (\omega) \mathrm{e} ^ {\frac {\mathrm{i}}{2} W _ {\gamma} (e, b _ {\delta})} 1 _ {e \in \gamma}}
$$

the contribution of the configuration ω to$F _ { \delta } ( e )$. Since s is an involution, the following relation holds: 1

$$
F _ {\delta} (e) = \sum_ {\omega} e _ {\omega} = \frac {1}{2} \sum_ {\omega} [ e _ {\omega} + e _ {s (\omega)} ].
$$

In order to prove (5.1), it sufices to prove the following for any configuration ω:

$$
N _ {\omega} + N _ {s (\omega)} - S _ {\omega} - S _ {s (\omega)} = i \big [ E _ {\omega} + E _ {s (\omega)} - W _ {\omega} - W _ {s (\omega)} \big ].\tag{5.2}
$$

There are three possibilities:

Case 1: the exploration path$\gamma ( \omega )$does not go through any of the edges adjacent to v. (It is easy to see that neither does$\gamma ( s ( \omega ) )$. All the terms then vanish and (5.2) trivially holds.

Case$\mathbf { 2 } \colon \gamma ( \omega )$goes through two edges around v. Note that it follows the orientation of ( )the medial graph, and thus enters v through either W or E and leaves through N or S.

![](images/page_36_image_0.jpg)

Figure 11: Two associated configurations, one with one exploration path and a loop, one without the loop. One can go from one to the other by switching the state of the edge.

We assume that$\gamma ( \omega )$enters through the edge W and leaves through the edge$\textit { S } \left( i . e . \right.$ ( )that the primal edge corresponding to v is open). The other cases are treated similarly. It is then possible to compute the contributions of all the edges adjacent to v of ω and $s ( \omega )$in terms of$W _ { \omega }$. Indeed,

• The probability of$s ( \omega )$is equal to$1 / \sqrt { 2 }$times the probability of ω (due to the ( ) /fact that there is one less open edge of weight 1 – we are at the self-dual point – and one less loop of weight${ \sqrt { 2 } } .$, see Proposition 3.17);

• Windings of the curve can be expressed using the winding of W. For instance, the winding of N in the configuration ω is equal to the winding of W minus a$\pi / 2$ turn.

The contributions are given as:

| configuration | W | E | N | S |
| --- | --- | --- | --- | --- |
| ω | $W_{\omega}$ | 0 | 0 | $e^{i\pi/4}W_{\omega}$ |
| s(ω) | $W_{\omega}/\sqrt{2}$ | $e^{i\pi/2}W_{\omega}/\sqrt{2}$ | $e^{-i\pi/4}W_{\omega}/\sqrt{2}$ | $e^{i\pi/4}W_{\omega}/\sqrt{2}$ |

Using the identity$\mathrm { e } ^ { \mathrm { i } \pi / 4 } - \mathrm { e } ^ { - \mathrm { i } \pi / 4 } = i \sqrt { 2 } .$, we deduce (5.2) by summing (with the right − =weight) the contributions of all the edges around v.

Case 3:$\gamma ( \omega )$goes through the four medial edges around$v .$Then the exploration path of$s ( \omega )$( )goes through only two, and the computation is the same as in the second case. ( )In conclusion, (5.2) is always satisfied and the claim is proved.□

Recall that the FK fermionic observable is defined on medial edges as well as on medial vertices. Convergence of the observable means convergence of the vertex observable. The edge observable is just a very convenient tool in the proof. The two previous properties of the edge fermionic observable translate into the following result for the vertex fermionic observable.

Proposition 5.3. The vertex fermionic observable$F _ { \delta }$is s-holomorphic.

Proof Let v be a medial vertex and let N, E, S and W be the four medial edges around it. Using Lemmata 5.1 and 5.2, one can see that (5.1) can be rewritten (by taking the complex conjugate) as:

$$
F _ {\delta} (N) + F _ {\delta} (S) = F _ {\delta} (E) + F _ {\delta} (W).
$$

In particular, from (3.6),

$$
F _ {\delta} (v) := \frac {1}{2} \sum_ {e \text {adjacent}} F _ {\delta} (e) = F _ {\delta} (N) + F _ {\delta} (S) = F _ {\delta} (E) + F _ {\delta} (W).
$$

Using Lemma 5.1 again,$F _ { \delta } ( N )$and$F _ { \delta } ( S )$are orthogonal, so that$F _ { \delta } ( N )$is the projection of$F _ { \delta } ( v )$on$\ell ( N )$( ) ( ) ( )(and similarly for other edges). Therefore, for a medial edge $e = [ x y ] , F _ { \delta } ( e )$) ( )is the projection of$F _ { \delta } ( x )$and$F _ { \delta } ( y )$with respect to$\ell ( e )$, which proves = [ ] ( ) ( ) ( )that the vertex fermionic observable is s-holomorphic.□

The function$F _ { \delta } / \sqrt { 2 \delta }$is preholomorphic for every$\delta > 0$. Moreover, Lemma 5.1 /identifies the boundary conditions of$F _ { \delta } / \sqrt { 2 \delta }$>(its argument is determined) so that this /function solves a discrete Riemann-Hilbert boundary value problem. These problems are significantly harder to handle than the Dirichlet problems. Therefore, it is more convenient to work with a discrete analogue of Im$\textstyle \left( \int ^ { \bar { z } } [ F _ { \delta } ( z ) / \sqrt { 2 \delta } ] ^ { 2 } d z \right)$, which should solve an approximate Dirichlet problem.

## 5.1.2 Convergence of$( H _ { \delta } ) _ { \delta > 0 } .$

Let A be the black face (vertex of$\Omega _ { \delta } )$bordering$a _ { \delta }$, see Fig. 6. Since the FK fermionic observable$F _ { \delta } / \sqrt { 2 \delta }$is s-holomorphic, Theorem 4.19 defines a function$H _ { \delta } : \Omega _ { \delta } \cup \Omega _ { \delta } ^ { \star }$R such that

$$
\begin{array}{r c l} H _ {\delta} (A) & = & 1 \quad \text {and} \\ H _ {\delta} (B) - H _ {\delta} (W) & = & \left| P _ {\ell (e)} [ F _ {\delta} (x) ] \right| ^ {2} = \left| P _ {\ell (e)} [ F _ {\delta} (y) ] \right| ^ {2} \end{array}
$$

for the edge$e \ = \ [ x y ]$of$\Omega _ { \delta } ^ { \circ }$bordered by a black face$B \in \Omega _ { \delta }$and a white face W $\Omega _ { \delta } ^ { \star }$= [ ]. Note that its restriction$H ^ { \bullet }$to$\Omega _ { \delta }$∈is subharmonic and its restriction$H _ { \delta } ^ { \circ }$to$\Omega _ { \delta } ^ { \star }$∈is superharmonic.

Let us start with two lemmata addressing the question of boundary conditions for $H _ { \delta }$

Lemma 5.4. The function$H _ { \delta } ^ { \bullet }$is equal to 1 on the arc$\partial _ { b a }$. The function$H _ { \delta } ^ { \circ }$is equal to 0 on the arc$\partial _ { a b } ^ { \star }$

Proof We first prove that$H _ { \delta } ^ { \bullet }$is constant on$\partial _ { b a }$. Let B and$B ^ { \prime }$be two adjacent consecutive sites of$\partial _ { b a }$. They are both adjacent to the same dual vertex$W \in \Omega _ { \delta } ^ { \star }$, see Fig. 12. Let$\textit { e } \left( \mathrm { r e s p . ~ } \ e ^ { \prime } \right)$be the edge of the medial lattice between$W$∈and B (resp. B′). We deduce

$$
H _ {\delta} ^ {\bullet} (B) - H _ {\delta} ^ {\bullet} (B ^ {\prime}) = | F _ {\delta} (e) | ^ {2} - | F _ {\delta} (e ^ {\prime}) | ^ {2} = 0\tag{5.3}
$$

The second equality is due to$| F _ { \delta } ( e ) | = \phi _ { \Omega _ { \delta } ^ { \diamond } , p _ { s d } } ^ { a _ { \delta } , b _ { \delta } } ( W \ { \stackrel { \star } {  } } \partial _ { a b } ^ { \star } )$(see Lemma 7.3). Hence,$H _ { \delta } ^ { \bullet }$ ∣is constant along the arc. Since$H _ { \delta } ^ { \bullet } ( A ) = 1$( ↔ ), the result follows readily.

![](images/page_38_image_0.jpg)

Figure 12: Two adjacent sites$B$and$B ^ { \prime }$on$\partial _ { b a }$together with the notation needed in the proof of Lemma 5.4.

Similarly,$H _ { \delta } ^ { \circ }$is constant on the arc$\partial _ { a b } ^ { \star }$. Moreover, the dual white face$A ^ { \star } \in \partial _ { a b } ^ { \star }$ bordering$a _ { \delta }$(see Fig. 6) satisfies

$$
H _ {\delta} ^ {\circ} (A ^ {\star}) = H _ {\delta} ^ {\bullet} (A) - | F _ {\delta} (e) | ^ {2} = 1 - 1 = 0\tag{5.4}
$$

where e is the edge separating A and$A ^ { \star }$, which necessarily belongs to$\gamma$. Therefore $H _ { \delta } ^ { \circ } = 0$on$\partial _ { a b } ^ { \star }$□

Lemma 5.5. The function$H _ { \delta } ^ { \bullet }$converges to 0 on the arc$\partial _ { a b }$uniformly away from a and b,$H _ { \delta } ^ { \circ }$converges to 1 on the arc$\partial _ { b a } ^ { \star }$uniformly away from a and b.

Proof Once again, we prove the result for$H _ { \delta } ^ { \bullet }$. The same reasoning then holds for$H _ { \delta } ^ { \circ }$ Let B be a site of$\partial _ { a b }$at distance r of$\partial _ { b a }$(and therefore at graph distance$r / \delta$of$\partial _ { b a }$in $\Omega _ { \delta } )$. Let$W$be an adjacent site of$B$on$\partial _ { a b } ^ { \star }$. Lemma 5.4 implies$H _ { \delta } ^ { \circ } ( W ) = 0$/. From the definition of$H _ { \delta }$, we find

$$
H _ {\delta} ^ {\bullet} (B) = H _ {\delta} ^ {\circ} (W) + \left| P _ {\ell (e)} [ F _ {\delta} (e) ] \right| ^ {2} = \left| P _ {\ell (e)} [ F _ {\delta} (e) ] \right| ^ {2} = \phi_ {\Omega_ {\delta}, p _ {s d}} ^ {a _ {\delta}, b _ {\delta}} (e \in \gamma) ^ {2}.
$$

Note that$e \in \gamma$if and only if B is connected to the wired arc$\partial _ { b a }$. Therefore,$\phi _ { \Omega _ { \delta } , p _ { s d } } ^ { a _ { \delta } , b _ { \delta } } ( e \in$ $\gamma )$∈is equal to the probability that there exists an open path from$B$to$\partial _ { b a }$( ∈(the winding)is deterministic, see Lemma 7.3 for details). Since the boundary conditions on$\partial _ { a b }$are free, the comparison between boundary conditions shows that the latter probability is smaller than the probability that there exists a path from B to$\partial U _ { \delta }$in the box $U _ { \delta } = \left( B + [ - r , r ] ^ { 2 } \right) \cap \mathbb { L } _ { \delta }$with wired boundary conditions. Therefore,

$$
{H _ {\delta} ^ {\bullet} (B)} = {\phi_ {\Omega_ {\delta}, p _ {s d}} ^ {a _ {\delta}, b _ {\delta}} \big (e \in \gamma \big) ^ {2} \leq \phi_ {U _ {\delta}, p _ {s d}} ^ {1} \big (B \leftrightarrow \partial U _ {\delta} \big) ^ {2}.}
$$

Proposition 3.10 implies that the right hand side converges to 0 (there is no infinite cluster for$\phi _ { p _ { s d } , 2 } ^ { 1 } )$, which gives a uniform bound for B away from a and b.□

The two previous lemmata assert that the boundary conditions for$H _ { \delta } ^ { \bullet }$and$H _ { \delta } ^ { \circ }$are roughly 0 on the arc$\partial _ { a b }$and 1 on the arc$\partial _ { b a }$. Moreover,$H _ { \delta } ^ { \bullet }$and$H _ { \delta } ^ { \circ }$are almost harmonic. This should imply that$\left( H _ { \delta } \right) _ { \delta > 0 }$converges to the solution of the Dirichlet ( ) >problem, which is the subject of the next proposition.

Proposition 5.6. Let$( \Omega , a , b )$be a simply connected domain with two points on the boundary. Then,$\left( H _ { \delta } \right) _ { \delta > 0 }$)converges to$I m ( \phi )$uniformly on any compact subsets of Ω when δ goes to$\phantom { \frac { 1 } { 2 } } O ,$( ) >where$\phi$( )is any conformal map from Ω to$\mathbb { T } = \mathbb { R } \times ( 0 , 1 )$sending a to and b to .

Before starting, note that Im φ is the solution of the Dirichlet problem on$( \Omega , a , b )$ with boundary conditions 1 on$\partial _ { b a }$)and 0 on$\partial _ { a b }$

Proof From the definition of H,$H _ { \delta } ^ { \bullet }$is subharmonic, let$h _ { \delta } ^ { \bullet }$be the preharmonic function with same boundary conditions as$H _ { \delta } ^ { \bullet }$on$\partial \Omega _ { \delta }$. Note that$H _ { \delta } ^ { \bullet } \leq h _ { \delta } ^ { \bullet }$. Similarly,$h _ { \delta } ^ { \circ }$is defined ≤to be the preharmonic function with same boundary conditions as$H _ { \delta } ^ { \circ }$on$\partial \Omega _ { \delta } ^ { \star }$. If$K \subset \Omega$ is fixed, where K is compact, let$b _ { \delta } \in K _ { \delta }$and$w _ { \delta } \in K _ { \delta } ^ { \star }$any neighbor of$b _ { \delta }$, we have

$$
h _ {\delta} ^ {\circ} (w _ {\delta}) \leq H _ {\delta} ^ {\circ} (w _ {\delta}) \leq H _ {\delta} ^ {\bullet} (b _ {\delta}) \leq h _ {\delta} ^ {\bullet} (b _ {\delta}).\tag{5.5}
$$

Using Lemmata 5.4 and 5.5, boundary conditions for$H _ { \delta } ^ { \bullet }$(and therefore$h _ { \delta } ^ { \bullet } )$are uniformly converging to$0$on$\partial _ { a b }$and 1 on$\partial _ { b a }$away from a and$b .$Moreover,$| h _ { \delta } ^ { \bullet } |$is bounded by 1 everywhere. This is suficient to apply Theorem 4.7:$h _ { \delta } ^ { \bullet }$∣ ∣converges to Im φ on any compact subset of Ω when$\delta$goes to 0. The same reasoning applies to$h _ { \delta } ^ { \circ }$( ). The convergence for$H _ { \delta } ^ { \bullet }$and$H _ { \delta } ^ { \circ }$follows easily since they are sandwiched between$h _ { \delta } ^ { \bullet }$and $h _ { \delta } ^ { \circ }$□

## 5.1.3 Convergence of FK fermionic observables$( F _ { \delta } / \sqrt { 2 \delta } ) _ { \delta > 0 }$

This section contains the proof of Theorem 3.15. The strategy is straightforward: $( F _ { \delta } / \sqrt { 2 \delta } ) _ { \delta > 0 }$is proved to be a precompact family for the uniform convergence on com-( / ) >pact subsets of Ω. Then, the possible sub-sequential limits are identified using$H _ { \delta }$

Proof of Theorem 3.15 First assume that the precompactness of the family$( F _ { \delta } / \sqrt { 2 \delta } ) _ { \delta > 0 }$ has been proved. Let$( F _ { \delta _ { n } } / \sqrt { 2 \delta _ { n } } ) _ { n \in \mathbb { N } }$( / )be a convergent subsequence and denote its limit by$f .$Note that$f$( / ) ∈is holomorphic as it is a limit of preholomorphic functions. For two points$x , y \in \Omega$, we have:

$$
H _ {\delta_ {n}} (y) - H _ {\delta_ {n}} (x) = \frac {1}{2} \mathrm{Im} \left(\int_ {x} ^ {y} \frac {1}{\delta_ {n}} F _ {\delta_ {n}} ^ {2} (z) d z\right)
$$

(for simplici${ \mathrm { J } } ,$also denote the closest points of$x , y$in$\Omega _ { \delta _ { n } }$by$x , y )$. On the one hand, the convergence of$( F _ { \delta _ { n } } / \sqrt { 2 \delta _ { n } } ) _ { n \in \mathbb { N } }$being uniform on any compact subset of$\Omega .$, the right ( /hand side converges to Im$\textstyle { \left( \int _ { x } ^ { y } f ( z ) ^ { 2 } d z \right) }$. On the other hand, the left-hand side converges to Im$\mathcal { ( } \phi ( y ) - \phi ( x ) \it )$(∫ ( ) ). Since both quantities are holomorphic functions of$y ,$there exists $C \in \mathbb { R }$( ( ) −such that$\begin{array} { r } { \phi ( y ) - \phi ( x ) = C + \int _ { x } ^ { y } f ( z ) ^ { 2 } d z } \end{array}$for every$x , y \in \Omega$. Therefore$f$equals$\sqrt { \phi ^ { \prime } }$ ∈ ( ) − ( ) = + ∫ ( ) ∈Since this is true for any converging subsequence, the result follows.

Therefore, the proof boils down to the precompactness of$( F _ { \delta } / \sqrt { 2 \delta } ) _ { \delta > 0 }$. We will use ( / ) >the second criterion in Proposition 4.3. Note that it is suficient to prove this result for squares$Q \subset \Omega$such that a bigger square$9 Q$(with same center) is contained in Ω.

Fix$\delta > 0$. When jumping diagonally over a medial vertex$v ,$the function$H _ { \delta }$changes by Re$( F _ { \delta } ^ { 2 } ( v ) )$or Im$\left( F _ { \delta } ^ { 2 } ( v ) \right)$depending on the direction, so that

$$
\delta^ {2} \sum_ {v \in Q _ {\delta} ^ {\diamond}} \left| F _ {\delta} (v) / \sqrt {2 \delta} \right| ^ {2} = \delta \sum_ {x \in Q _ {\delta}} | \nabla H _ {\delta} ^ {\bullet} (x) | + \delta \sum_ {x \in Q _ {\delta} ^ {\star}} | \nabla H _ {\delta} ^ {\circ} (x) |\tag{5.6}
$$

where$\nabla H _ { \delta } ^ { \bullet } ( x ) = \left( H _ { \delta } ^ { \bullet } ( x + \delta ) - H _ { \delta } ^ { \bullet } ( x ) , H _ { \delta } ^ { \bullet } ( x + i \delta ) - H _ { \delta } ^ { \bullet } ( x ) \right)$, and$\nabla H _ { \delta } ^ { \circ }$is defined similarly for$H _ { \delta } ^ { \circ }$∇ ( ) = ( ( + ) − ( ) ( + ) − ( )) ∇. It follows that it is enough to prove uniform boundedness of the right hand side in (5.6). We only treat the sum involving$H _ { \delta } ^ { \bullet }$. The other sum can be handled similarly.

Write$H _ { \delta } ^ { \bullet } = S _ { \delta } + R _ { \delta }$where$S _ { \delta }$is a harmonic function with the same boundary conditions on$\partial 9 Q _ { \delta }$+as$H _ { \delta } ^ { \bullet }$. Note that$R _ { \delta } \leq 0$is automatically subharmonic. In order to prove that the sum of$| \nabla H _ { \delta } ^ { \bullet } |$on$Q _ { \delta }$≤is bounded by$C / \delta$, we deal separately with S and$| \nabla R _ { \delta } |$. First,

$$
\sum_ {x \in Q _ {\delta}} \left| \nabla S _ {\delta} (x) \right| \leq \frac {C _ {1}}{\delta^ {2}} \cdot C _ {2} \delta \left(\sup _ {x \in \partial Q _ {\delta}} | S _ {\delta} (x) |\right) \leq \frac {C _ {3}}{\delta} \left(\sup _ {x \in 9 Q _ {\delta}} | H _ {\delta} ^ {\bullet} (x) |\right) \leq \frac {C _ {4}}{\delta},
$$

where in the first inequality we used Proposition 4.2 and the maximum principle for $S _ { \delta } ,$and in the second the fact that$S _ { \delta }$and$H _ { \delta } ^ { \bullet }$share the same boundary conditions on $9 Q _ { \delta }$. The last inequality comes from the fact that$H _ { \delta } ^ { \bullet }$converges, hence remains bounded uniformly in$\delta .$

Second, recall that$G _ { 9 Q _ { \delta } } ( \cdot , y )$is the Green function in$9 Q _ { \delta }$with singularity at$y .$ Since$R _ { \delta }$(⋅ )equals 0 on the boundary, Proposition 4.9 implies

$$
{R _ {\delta} (x)} = {\sum_ {y \in 9 Q _ {\delta}} \Delta R _ {\delta} (y) G _ {9 Q _ {\delta}} (x, y),}\tag{5.7}
$$

thus giving

$$
\nabla R _ {\delta} (x) = \sum_ {y \in 9 Q _ {\delta}} \Delta R _ {\delta} (y) \nabla_ {x} G _ {9 Q _ {\delta}} (x, y)
$$

Therefore,

$$
\begin{array}{r c l} \sum_ {x \in Q _ {\delta}} \left| \nabla R _ {\delta} (x) \right| & = & \sum_ {x \in Q _ {\delta}} \Big | \sum_ {y \in 9 Q _ {\delta}} \Delta R _ {\delta} (y) \nabla_ {x} G _ {9 Q _ {\delta}} (x, y) \Big | \\ & \leq & \sum_ {y \in 9 Q _ {\delta}} \Delta R _ {\delta} (y) \sum_ {x \in Q _ {\delta}} | \nabla_ {x} G _ {9 Q _ {\delta}} (x, y) | \\ & \leq & \sum_ {y \in 9 Q _ {\delta}} \Delta R _ {\delta} (y) C _ {5} \delta \sum_ {x \in Q _ {\delta}} G _ {9 Q _ {\delta}} (x, y) \\ & = & C _ {5} \delta \sum_ {x \in Q _ {\delta}} \sum_ {y \in 9 Q _ {\delta}} \Delta R _ {\delta} (y) G _ {9 Q _ {\delta}} (x, y) \\ & = & C _ {5} \delta \sum_ {x \in Q _ {\delta}} R _ {\delta} (x) = C _ {6} / \delta \end{array}
$$

The second line uses the fact that$\Delta R _ { \delta } \ge 0$, the third Proposition 4.10, the fifth Propo-≥sition 4.9 again, and the last inequality the facts that$Q _ { \delta }$contains of order$1 / \delta ^ { 2 }$sites and that$R _ { \delta }$is bounded uniformly in δ (since$H _ { \delta }$and$S _ { \delta }$are).

Thus,$\delta \Sigma _ { x \in Q _ { \delta } } | \nabla H _ { \delta } ^ { \bullet } |$is uniformly bounded. Since the same result holds for$H _ { \delta } ^ { \circ }$ $( F _ { \delta } / \sqrt { 2 \delta } ) _ { \delta > 0 }$∈ ∣∇ ∣is precompact on$Q$(and more generally on any compact subset of Ω) and ( / ) >the proof is completed.□

## 5.2 Convergence of the spin fermionic observable

We now turn to the proof of convergence for the spin fermionic observable. Fix a simply connected domain$( \Omega , a , b )$with two points on the boundary. For$\delta > 0$, always consider ( ) >the spin fermionic observable on the discrete spin Dobrushin domain$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$. Since the domain is fixed, we set$F _ { \delta } = F _ { \delta _ { \delta } , a _ { \delta } , b _ { \delta } }$( ). We follow the same three steps as before, =beginning with the s-holomorphicity. The other two steps are only sketched, since they are more technical than in the FK-Ising case, see [CS09].

Proposition 5.7. For$\delta > 0 , F _ { \delta }$is s-holomorphic on$\Omega _ { \delta } ^ { \circ }$

![](images/page_41_image_0.jpg)

Figure 13: The diferent possible cases in the proof of Proposition 5.7: ω is depicted on the top, and$\omega ^ { \prime }$on the bottom.

Proof Let$x , y$two adjacent medial vertices connected by the edge$e = [ x y ]$. Let v be the vertex of$\Omega _ { \delta }$bordering the (medial) edge e. As before, set$x _ { \omega } ~ ( \mathrm { r e s p . } ~ y _ { \omega } )$for the contribution of ω to$F _ { \delta } ( x )$(resp.$F _ { \delta } ( y ) )$). We wish to prove that

$$
\sum_ {\omega} P _ {\ell (e)} (x _ {\omega}) = \sum_ {\omega} P _ {\ell (e)} (y _ {\omega}).\tag{5.8}
$$

Note that the curve$\gamma ( \omega )$finishes at$x _ { \omega }$or at$y _ { \omega }$so that ω cannot contribute to$F _ { \delta } ( x )$ and$F _ { \delta } ( y )$( ) ( )at the same time. Thus, it is suficient to partition the set of configurations ( )into pairs of configurations$( \omega , \omega ^ { \prime } )$, one contributing to$y ,$the other one to$x ,$such that $P _ { \ell ( e ) } ( x _ { \omega } ) = P _ { \ell ( e ) } ( y _ { \omega ^ { \prime } } )$

( )( ) = ( )( )Without loss of generality, assume that e is pointing southeast, thus$\ell ( e ) = \mathbb { R }$(other cases can be done similarly). First note that

$$
x _ {\omega} = \frac {1}{Z} \mathrm{e} ^ {- i \frac {1}{2} [ W _ {\gamma (\omega)} (a _ {\delta}, x _ {\delta}) - W _ {\gamma^ {\prime}} (a _ {\delta}, b _ {\delta}) ]} (\sqrt {2} - 1) ^ {| \omega |},
$$

where$\gamma ( \omega )$is the interface in the configuration$\omega , \gamma ^ { \prime }$is any curve from$a _ { \delta }$to$b _ { \delta }$(recall that$W _ { \gamma ^ { \prime } } ( a _ { \delta } , b _ { \delta } )$does not depend on$\gamma ^ { \prime } )$, and Z is a normalizing real number not ( )depending on the configuration. There are six types of pairs that one can create, see Fig. 13 depicting the four main cases. Case 1 corresponds to the case where the interface reaches x or$y$and then extends by one step to reach the other vertex. In Case 2, γ reaches v before x and$y ,$and makes an additional step to x or$y .$In Case$3 , \gamma$reaches x or y and sees a loop preventing it from being extended to the other vertex (in contrast to Case 1). In Case$4 , \gamma$reaches x or$y ,$, then goes away from v and comes back to the other vertex. Recall that the curve must always go to the left: in cases$1 ( \mathrm { a } ) , 1 ( \mathrm { b } )$, and 2 there can be a loop or even the past of$\gamma$passing through v. However, this does not change the computation.

We obtain the following table for$x _ { \omega }$and$y _ { \omega ^ { \prime } }$(we always express$y _ { \omega ^ { \prime } }$in terms of $x _ { \omega } )$. Moreover, one can compute the argument modulo π of contributions$x _ { \omega }$since the orientation of e is known. When upon projecting on R, the result follows.

| configuration | Case 1(a) | Case 1(b) | Case 2 | Case 3(a) | Case 3(b) | Case 4 |
| --- | --- | --- | --- | --- | --- | --- |
| $x_{\omega}$ | $x_{\omega}$ | $x_{\omega}$ | $x_{\omega}$ | $x_{\omega}$ | $x_{\omega}$ | $x_{\omega}$ |
| $y_{\omega'}$ | $(\sqrt{2}-1)\mathrm{e}^{i\pi/4}x_{\omega}$ | $\frac{\mathrm{e}^{i\pi/4}}{\sqrt{2}-1}x_{\omega}$ | $\mathrm{e}^{-i\pi/4}x_{\omega}$ | $\mathrm{e}^{3i\pi/4}x_{\omega}$ | $\mathrm{e}^{3i\pi/4}x_{\omega}$ | $\mathrm{e}^{-5i\pi/4}x_{\omega}$ |
| arg. $x_{\omega} \mod \pi$ | $5\pi/8$ | $\pi/8$ | $\pi/8$ | $5\pi/8$ | $5\pi/8$ | $5\pi/8$ |

Proof of Theorem 2.11 (Sketch). The proof is roughly sketched. We refer to [CS09] for a complete proof.

Since$F _ { \delta }$is s-harmonic, one can define the observable$H _ { \delta }$as in Theorem 4.19, with the requirement that it is equal to 0 on the white face adjacent to b. Then,$H _ { \delta } ^ { \circ }$is constant equal to 0 on the boundary as in the FK-Ising case. Note that$H _ { \delta }$should not converge to 0, even if boundary conditions are 0 away from a. Firstly,$H _ { \delta } ^ { \circ }$is superharmonic and not harmonic, even though it is expected to be almost harmonic (away from$a , H _ { \delta } ^ { \bullet }$and $H _ { \delta } ^ { \circ }$are close), this will not be true near a. Actually,$H _ { \delta }$should not remain bounded around a.

The main diference compared to the previous section is indeed the unboundedness of$H _ { \delta }$near$a _ { \delta }$which prevents us from the immediate use of Proposition 4.3. It is actually possible to prove that away from a,$H _ { \delta }$remains bounded, see [CS09]. This uses more sophisticated tools, among which are the boundary modification trick (see [DCHN10] for a quick description in the FK-Ising case, and [CS09] for the Ising original case). As before, boundedness implies precompactness (and thus boundedness) of$( F _ { \delta } ) _ { \delta > 0 }$away from a via Proposition 4.3. Since$H _ { \delta }$can be expressed in terms of$F _ { \delta }$( ) >, it is easy to deduce that$H _ { \delta }$is also precompact.

Now consider a convergent subsequence$( f _ { \delta _ { n } } , H _ { \delta _ { n } } )$converging to$( f , H )$. One can check that H is equal to 0 on$\partial \Omega \setminus \{ a \}$( ). Moreover, the fact that$H _ { \delta } ^ { \circ }$( )equals 0 on the ∖ { }boundary and is superharmonic implies that$H _ { \delta } ^ { \circ }$is greater than or equal to 0 everywhere, implying$H \geq 0$in Ω. This property of harmonic functions in a domain almost determines ≥them. There is only a one-parameter family of positive harmonic functions equal to 0 on the boundary. These functions are exactly the imaginary parts of conformal maps from Ω to the upper half-plane H mapping a to . We can further assume that b is ∞mapped to 0, since we are interested only in the imaginary part of these functions.

Fix one conformal map ψ from Ω to H, mapping a to and b to 0. There exists $\lambda > 0$∞such that H λImψ. As in the case of the FK-Ising model, one can prove that >Im$\left( \int ^ { z } f ^ { 2 } \right) = H$=, implying that$f ^ { 2 } = \lambda \psi ^ { \prime }$. Since$f ( b ) = 1$(it is obvious from the definition (that$F _ { \delta } \big ( b _ { \delta } \big ) = 1 \big )$, λ equals$\frac { 1 } { \psi ^ { \prime } ( b ) }$=. In conclusion,$f ( z ) = \sqrt { \psi ^ { \prime } ( z ) / \psi ^ { \prime } ( b ) }$for every$z \in \Omega$.

Note that some regularity hypotheses on the boundary near b are needed to ensure that the sequence$( f _ { \delta _ { n } } , H _ { \delta _ { n } } )$also converges near b. This is the reason for assuming that ( )the boundary near b is smooth. We also mention that there is no normalization here. The normalization from the point of view of b was already present in the definition of the observable.

## 6 Convergence to chordal SLE(3) and chordal SLE(16/3)

The strategy to prove that a family of parametrized curves converges to$\operatorname { S L E } ( \kappa )$follows three steps:

• First, prove that the family of curves is tight.

• Then, show that any sub-sequential limit is a time-changed Loewner chain with a continuous driving process (see Befara’s course for details on Loewner chains and driving processes).

• Finally, show that the only possible driving processes for the sub-sequential limits is$\sqrt { \kappa } B _ { t }$where$B _ { t }$is a standard Brownian motion.

The conceptual step is the third one. In order to identify the Brownian motion as being the only possible driving process for the curve, we find computable martingales expressed in terms of the limiting curve. These martingales will be the limits of fermionic observables. The fact that these (explicit) functions are martingales allows us to deduce martingale properties of the driving process. More precisely, we aim to use Lévy’s theorem: a continuous real-valued process$X$such that$X _ { t }$and$X _ { t } ^ { 2 } - a t$are martingales is necessarily$\sqrt { a } B _ { t }$

## 6.1 Tightness of interfaces for the FK-Ising model

In this section, we prove the following theorem:

Theorem 6.1. Fix a domain$( \Omega , a , b )$. The family$( \gamma _ { \delta } ) _ { \delta > 0 }$of random interfaces for the critical FK-Ising model in$( \Omega , a , b )$( ) >is tight for the topology associated to the curve distance.

The question of tightness for curves in the plane has been studied in the groundbreaking paper [AB99]. In that paper, it is proved that a suficient condition for tightness is the absence, at every scale, of annuli crossed back and forth an unbounded number of times.

More precisely, for$x \in \Omega$and$r < R ,$let$S _ { r , R } ( x ) = ( x + [ - R , R ] ^ { 2 } ) \setminus ( x + [ - r , r ] ^ { 2 } )$and define$\mathcal { A } _ { k } ( x ; r , R )$∈ < ( ) = ( + [− ] ) ∖ ( + [to be the event that there exist k crossings of the curve$\gamma _ { \delta }$] )between A ( )outer and inner boundaries of$S _ { r , R } ( x )$

Theorem 6.2 (Aizenman-Burchard [AB99]). Let Ω be a simply connected domain and let a and b be two marked points on its boundary. Denote by$\mathbb { P } _ { \delta }$the law of a random curve$\tilde { \gamma } _ { \delta }$on$\Omega _ { \delta }$from$a _ { \delta }$to$b _ { \delta }$. If there exist$k \in \mathbb { N } , C _ { k } < \infty$and$\Delta _ { k } > 2$such that for all $\delta < r < R$and$x \in \Omega$

$$
\mathbb {P} _ {\delta} \big (\mathcal {A} _ {k} (x; r, R) \big) \leq C _ {k} \Big (\frac {r}{R} \Big) ^ {\Delta_ {k}},
$$

then the family of curves$\left( \tilde { \gamma } _ { \delta } \right)$is tight.

We now show how to exploit this theorem in order to prove Theorem 6.1. The main tool is Theorem 3.16.

Lemma 6.3 (Circuits in annuli). Let$\mathcal { E } ( x , n , N )$be the probability that there exists an open path connecting the boundaries of$S _ { n , N } ( x )$). There exists a constant$c < 1$such that for all$n > 0$

$$
\phi_ {p _ {s d}, S _ {n, 2 n} (x)} ^ {1} \big (\mathcal {E} \big (x; n, 2 n \big) \big) \leq c.
$$

Note that the boundary conditions on the boundary of the annulus are wired. Via comparison between boundary conditions, this implies that the probability of an open path from the inner to the outer boundary is bounded uniformly on the configuration outside of the annulus. This uniform bound allows us to decouple what is happening inside the annulus with what is happening outside of it.

![](images/page_44_image_0.jpg)

Figure 14: Left: The event$A _ { 6 } ( x , r , R )$. In the case of exploration paths, it implies the ( )existence of alternating open and closed paths. Right: Rectangles$R _ { T } , R _ { R } , R _ { B }$and$R _ { L }$ crossed by closed paths in the longer direction. The combination of these closed paths prevents the existence of a crossing from the inner to the outer boundary of the annulus.

Proof Assume$x = 0$. The result follows from Theorem 3.16 (proved in Section 7.2) =applied in the four rectangles$R _ { B } = [ - 2 n , 2 n ] \times [ - n , - 2 n ] , \ R _ { L } = [ - 2 n , - n ] \times [ - 2 n , 2 n ] .$ $R _ { T } = \left[ - 2 n , 2 n \right] \times \left[ n , 2 n \right]$and$R _ { R } = \left[ n , 2 n \right] \times \left[ - 2 n , 2 n \right]$− ] = [− − ] × [− ], see Fig. 14. Indeed, if there exists = [− ] × [ ] = [ ] × [− ]a closed path crossing each of these rectangles in the longer direction, one can construct from them a closed circuit in$S _ { n , 2 n }$. Now, consider any of these rectangles,$R _ { B }$for instance. Its aspect ratio is$^ { 4 , }$so that Theorem 3.16 implies that there is a closed path crossing in the longer direction with probability at least$c _ { 1 } > 0$(the wired boundary >conditions are the dual of the free boundary conditions). The FKG inequality (3.2) implies that the probability of a circuit is larger than$c _ { 1 } ^ { 4 } > 0$. Therefore, the probability of a crossing is at most$c = 1 - c _ { 1 } ^ { 4 } < 1$□

We are now in a position to prove Theorem 6.1.

Proof of Theorem 6.1 Fix$x \in \Omega , \delta < r < R$and recall that we are on a lattice of ∈ < <mesh size δ. Let k to be fixed later. We first prove that

$$
\phi_ {\Omega_ {\delta}, p _ {s d}} ^ {a _ {\delta}, b _ {\delta}} \big (\mathcal {A} _ {2 k} (x; r, 2 r) \big) \leq c ^ {k}\tag{6.1}
$$

for some constant$c < 1$uniform in$x , k , r , \delta$and the configuration outside of$S _ { r , 2 r } ( x )$

If$\mathcal { A } _ { 2 k } ( x ; r , 2 r )$< ( )holds, then there are (at least) k open paths, alternating with k dual A ( )paths, connecting the inner boundary of the annulus to its outer boundary. Since the paths are alternating, one can deduce that there are k open crossings, each one being surrounded by closed crossings. Hence, using successive conditionings and the comparison between boundary conditions, the probability for each crossing is smaller than the probability that there is a crossing in the annulus with wired boundary conditions (since these boundary conditions maximize the probability of$\mathcal { E } ( x ; r , 2 r ) )$). We obtain

$$
\phi_ {\Omega_ {\delta}, p _ {s d}} ^ {a _ {\delta}, b _ {\delta}} \big (\mathcal {A} _ {2 k} (x; r, 2 r) \big) \leq \Big [ \phi_ {p _ {s d}, S _ {r, 2 r} (x)} ^ {1} \big (\mathcal {E} (x; r, 2 r) \big) \Big ] ^ {k}.
$$

Using Lemma 6.3,$\phi _ { p _ { s d } , S _ { r , 2 r } ( x ) } ^ { 1 } ( \mathcal { E } ( x ; r , 2 r ) ) \le c < 1$and and (6.1) follows.

(E( )) ≤ <One can further fix k large enough so that$c ^ { k } < { \frac { 1 } { 8 } }$. Now, one can decompose the annulus$S _ { r , R } ( x )$into roughly ln$( R / r )$<annuli of the form$S _ { r , 2 r } ( x )$, so that for the previous$k ,$

$$
\phi_ {\Omega_ {\delta}, p _ {s d}} ^ {a _ {\delta}, b _ {\delta}} (\mathcal {A} _ {2 k} (x; r, R)) \leq \left(\frac {r}{R}\right) ^ {3}.\tag{6.2}
$$

## 6.2 sub-sequential limits of FK-Ising interfaces are Loewner chains

This subsection requires basic knowledge of Loewner chains and we refer to Befara’s course in this volume for an overview on the subject. In the previous subsection, traces of interfaces in Dobrushin domains were shown to be tight. The natural discrete parametrization does not lead to a suitable continuous parametrization. We would prefer our sub-sequential limits to be parametrized as Loewner chains. In other words, we would like to parametrize the curve by its so-called h-capacity. In this case, we say that the curve is a time-changed Loewner chain.

Theorem 6.4. Any sub-sequential limit of the family$( \gamma _ { \delta } ) _ { \delta > 0 }$of FK-Ising interfaces is a time-changed Loewner chain.

Not every continuous curve is a time-changed Loewner chain. In the case of FK interfaces, the limiting curve is fractal-like and has many double points, so that the following theorem is not a trivial statement. A general characterization for a parametrized non-selfcrossing curve in$( \Omega , a , b )$to be a time-changed Loewner chain is the following:

• its h-capacity must be continuous,

• its h-capacity must be strictly increasing.

• the curve grows locally seen from infinity in the following sense: for any$t \geq 0$and for any$\varepsilon > 0$, there exists$\delta > 0$such that for any$s \leq t ,$, the diameter of$g _ { s } ( \Omega _ { s } \setminus \Omega _ { s + \delta } )$ >is smaller than ε, where$\Omega _ { s }$> ≤is the connected component of$\Omega \setminus \gamma [ 0 , s ]$( ∖ )containing b and$g _ { s }$is the conformal map from$\Omega _ { s }$∖ [ ]to H with hydrodynamical renormalization (see Befara’s course).

The first condition is automatically satisfied by continuous curves. The third one usually follows from the two others when the curve is continuous, so that the crucial condition to check is the second one. This condition can be understood as being the fact that the tip of the curve is visible from b at every time. In other words, the family of hulls created by the curve (i.e. the complement of the connected component of$\Omega \setminus \gamma _ { t }$containing b) ∖is strictly increasing. This is the case if the curve does not enter long fjords created by its past at every scale, see Fig. 15.

In the case of FK interfaces, this corresponds to so-called six arm event, and it boils down to proving that$\Delta _ { 6 } > 2 \quad$. A general belief in statistical physics is that many ex->ponents, called universal exponents, do not depend on the model. For instance, the so-called 5-arm exponent should equal 2. This would imply that${ \Delta _ { 6 } } > { \Delta _ { 5 } } = 2$. Unfor-> =tunately, computing the 5-arm exponent for the FK-Ising model is not an easy task. Therefore, we need to invoke a stronger structural theorem to prove that sub-sequential limits are Loewner chains. Recently, Kemppainen and the second author proved the required theorem, and we describe it now.

For a family of parametrized curves$( \gamma _ { \delta } ) _ { \delta > 0 }$, define Condition by:

Condition : There exist$C > 1$and$\Delta > 0$such that for any$0 < \delta < r < R / C$, for (⋆) >any stopping time τ and for any annulus$S _ { r , R } ( x )$not containing$\gamma _ { \tau }$< < < /, the probability that $\gamma _ { \delta }$crosses the annulus$S _ { r , R } ( x )$( )(from the outside to the inside) after time τ while it is not forced to enter$S _ { r , R } ( x )$again is smaller than$C ( r / R ) ^ { \Delta }$, see$F i g$. 15.

![](images/page_46_image_0.jpg)

Figure 15: Left: An example of a fjord. Seen from b, the h-capacity (roughly speaking, the size) of the hull does not grow much while the curve is in the fjord. The event involves six alternating open and closed crossings of the annulus. Right: Conditionally on the beginning of the curve, the crossing of the annulus is unforced on the left, while it is forced on the right (it must go ultimately to b).

Roughly speaking, the previous condition is a uniform bound on unforced crossings. Note that it is necessary to assume the fact that the crossing is unforced.

Theorem 6.5 ([KS10]). If a family of curves$\left( \gamma _ { \delta } \right)$satisfies Condition , then it is ( ) (⋆)tight for the topology associated to the curve distance. Moreover, any sub-sequential limit $\left( \gamma _ { \delta _ { n } } \right)$is to a time-changed Loewner chain.

Tightness is almost obvious, since Condition implies the hypothesis in Aizenman-(⋆)Burchard’s theorem. The hard part is the proof that Condition guarantees that the (⋆)h-capacity of sub-sequential limits is strictly increasing and that they create Loewner chains. The reader is referred to [KS10] for a proof of this statement. We are now in a position to prove Theorem 6.4:

Proof of Theorem 6.4 Lemma 6.3 allows us to prove Condition without dificulty. □

## 6.3 Convergence of FK-Ising interfaces to SLE(16/3)

The FK fermionic observable is now proved to be a martingale for the discrete curves and to identify the driving process of any sub-sequential limit of FK-Ising interfaces.

Lemma 6.6. Let$\delta > 0$. The FK fermionic observable$M _ { n } ^ { \delta } ( z ) = F _ { \Omega _ { \delta } \setminus \gamma [ 0 , n ] , \gamma _ { n } , b _ { \delta } } ( z )$is a >martingale with respect to$( \mathcal F _ { n } )$, where${ \mathcal { F } } _ { n }$( ) = ∖ [ ] ( )is the σ-algebra generated by the FK interface $\gamma [ 0 , n ]$

Proof For a Dobrushin domain$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$, the slit domain created by "removing" ( )the first n steps of the exploration path is again a Dobrushin domain. Conditionally on $\gamma [ 0 , n ]$, the law of the FK-Ising model in this new domain is exactly$\phi _ { \Omega _ { \delta } ^ { \diamond } \setminus \gamma [ 0 , n ] } ^ { \gamma _ { n } , b _ { \delta } } .$This observation implies that$M _ { n } ^ { \delta } ( z )$is the random variable$1 _ { z \in \gamma _ { \delta } } \mathrm { e } ^ { \frac { 1 } { 2 } i W _ { \gamma _ { \delta } } ( z , b ) }$conditionally on ${ \mathcal { F } } _ { n } ,$( )therefore it is automatically a martingale.□

Proposition 6.7. Any sub-sequential limit of$( \gamma _ { \delta } ) _ { \delta > 0 }$which is a Loewner chain is the ( ) >(chordal) Schramm-Loewner Evolution with parameter$\kappa = 1 6 / 3$

Proof Consider a sub-sequential limit$\gamma$in the domain$( \Omega , a , b )$which is a Loewner chain. Let$\phi$be a map from$( \Omega , a , b )$to$( \mathbb { H } , 0 , \infty )$( ). Our goal is to prove that$\widetilde \gamma = \phi ( \gamma )$is a chordal$\mathrm { S L E } ( 1 6 / 3 )$( ) (in the upper half-plane.

Since$\gamma$is assumed to be a Loewner chain,$\tilde { \gamma }$is a growing hull from 0 to parametrized by its h-capacity. Let$W _ { t }$∞be its continuous driving process. Also, define$g _ { t }$to be the conformal map from$\mathbb { H } \setminus \tilde { \gamma } [ 0 , t ]$to H such that$g _ { t } ( z ) = z + 2 t / z + O ( 1 / z ^ { 2 } )$ when z goes to .

Fix$z ^ { \prime } \in \Omega$∞. For$\delta > 0$, recall that$M _ { n } ^ { \delta } ( z ^ { \prime } )$is a martingale for$\gamma _ { \delta }$. Since the martingale ∈is bounded,$M _ { \tau _ { t } } ^ { \delta } ( z ^ { \prime } )$( )is a martingale with respect to$\mathcal { F } _ { \tau _ { t } }$, where$\tau _ { t }$is the first time at which$\phi ( \gamma _ { \delta } )$( ) Fhas an h-capacity larger than t. Since the convergence is uniform, $\begin{array} { r } { M _ { t } ( z ^ { \prime } ) : = \operatorname* { l i m } _ { \delta \to 0 } M _ { \tau _ { t } } ^ { \delta } ( z ^ { \prime } ) } \end{array}$is a martingale with respect to$\mathcal { G } _ { t }$, where$\mathcal { G } _ { t }$is the σ-algebra ( ) ∶= ( ) G Ggenerated by the curve γ˜ up to the first time its h-capacity exceeds t. By definition, this time is t, and$\mathcal { G } _ { t }$is the σ-algebra generated by$\tilde { \gamma } [ 0 , t ]$

Recall that$M _ { t } ( z ^ { \prime } )$is related to$\phi \left( z ^ { \prime } \right)$[ ]via the conformal map from$\mathbb { H } \setminus \tilde { \gamma } [ 0 , t ]$to $\mathbb { R } \times ( 0 , 1 )$( ), normalized to send$\tilde { \gamma } _ { t }$( )to and to . This last map is exactly$\begin{array} { r } { { \frac { 1 } { \pi } } \ln ( g _ { t } - W _ { t } ) } \end{array}$ ×( )Setting$z = \phi \bigl ( z ^ { \prime } \bigr )$, we obtain that

$$
\sqrt {\pi} M _ {t} ^ {z} := \sqrt {\pi} M _ {t} (z ^ {\prime}) = \sqrt {[ \ln (g _ {t} (z) - W _ {t}) ] ^ {\prime}} = \sqrt {\frac {g _ {t} ^ {\prime} (z)}{g _ {t} (z) - W _ {t}}}\tag{6.3}
$$

is a martingale. Recall that, when z goes to infinity,

$$
g _ {t} (z) = z + \frac {2 t}{z} + O \left(\frac {1}{z ^ {2}}\right) \quad \text { and } \quad g _ {t} ^ {\prime} (z) = 1 - \frac {2 t}{z ^ {2}} + O \left(\frac {1}{z ^ {3}}\right)\tag{6.4}
$$

For$s \leq t ,$

$$
\begin{array}{l l l} \sqrt {\pi} \cdot \mathbb {E} [ M _ {t} ^ {z} | \mathcal {G} _ {s} ] & = & \mathbb {E} \left[ \sqrt {\frac {1 - 2 t / z ^ {2} + O (1 / z ^ {3})}{z - W _ {t} + 2 t / z + O (1 / z ^ {2})}}   \Big |   \mathcal {G} _ {s} \right] \\ & = & \frac {1}{\sqrt {z}}   \mathbb {E} \left[ 1 + \frac {1}{2} W _ {t} / z + \frac {1}{8} \left(3 W _ {t} ^ {2} - 1 6 t\right) / z ^ {2} + O \left(1 / z ^ {3}\right)   \Big |   \mathcal {G} _ {s} \right] \\ & = & \frac {1}{\sqrt {z}} \left(1 + \frac {1}{2} \mathbb {E} [ W _ {t} | \mathcal {G} _ {s} ] / z + \frac {1}{8} \mathbb {E} [ 3 W _ {t} ^ {2} - 1 6 t | \mathcal {G} _ {s} ] / z ^ {2} + O \left(1 / z ^ {3}\right)\right). \end{array}
$$

Taking$s = t \mathrm { ~ y ~ }$ields

$$
\sqrt {\pi} \cdot M _ {s} ^ {z} = \frac {1}{\sqrt {z}} \left(1 + \frac {1}{2} W _ {s} / z + \frac {1}{8} (3 W _ {s} ^ {2} - 1 6 s) / z ^ {2} + O (1 / z ^ {3})\right).
$$

Since$\mathbb { E } [ M _ { t } ^ { z } | \mathcal { G } _ { s } ] = M _ { s } ^ { z }$, terms in the previous asymptotic development can be matched [ ∣G ]together so that$\mathbb { E } [ W _ { t } | \mathcal { G } _ { s } ] = W _ { s }$and E$\begin{array} { r } { W _ { t } ^ { 2 } - \frac { 1 6 } { 3 } t | \mathcal { \bar { G } } _ { s } \bar { ] } = W _ { s } ^ { 2 } - \frac { 1 6 } { 3 } s } \end{array}$. Since$W _ { t }$is continuous, $\mathrm { L e v y ` s }$=theorem implies that$W _ { t } = \sqrt { \frac { 1 6 } { 3 } } B _ { t }$−<sub>where</sub>$B _ { t }$= −<sub>is a standard Brownian motion.</sub>

=In conclusion, γ is the image by$\phi ^ { - 1 }$of the chordal Schramm-Loewner Evolution with parameter$\kappa = 1 6 / 3$in the upper half-plane. This is exactly the definition of the chordal = /Schramm-Loewner Evolution with parameter$\kappa = 1 6 / 3$in the domain$( \Omega , a , b )$□

Proof of Theorem 3.13$\mathrm { B y }$Theorem 4.3, the family of curves is tight. Using Theorem$6 . 4 ,$any sub-sequential limit is a time-changed Loewner chain. Consider such a sub-sequential limit and parametrize it by its h-capacity. Proposition 6.7 then implies that it is the Schramm-Loewner Evolution with parameter$\kappa = 1 6 / 3$. The possible limit being unique, the claim is proved.□

## 6.4 Convergence to SLE(3) for spin Ising interfaces

The proof of Theorem 2.10 is very similar to the proof of Theorem 3.13, except that we work with the spin Ising fermionic observable instead of the FK-Ising model one. The only point difering from the previous section is the proof that the spin fermionic observable is a martingale for the curve. We prove this fact now and leave the remainder of the proof as an exercise. Let γ be the interface in the critical Ising model with Dobrushin boundary conditions.

Lemma 6.8. Let$\delta > 0$, the spin fermionic observable$M _ { n } ^ { \delta } ( z ) = F _ { \Omega _ { \delta } ^ { \diamond } \setminus \gamma [ 0 , n ] , \gamma ( n ) , b _ { \delta } } ( z )$is a >martingale with respect to$\left( \mathcal { F } _ { n } \right)$, where${ \mathcal { F } } _ { n }$( ) = ( )is the σ-algebra generated by the exploration process$\gamma [ 0 , n ]$

Proof It is suficient to check that$F _ { \delta } ( z )$has the martingale property when$\gamma = \gamma ( \omega )$ makes one step$\gamma _ { 1 }$. In this case$\mathcal { F } _ { 0 }$( ) =is the trivial σ-algebra, so that we wish to prove

$$
\mu_ {\beta_ {c}, \Omega} ^ {a, b} \left[ F _ {\Omega_ {\delta} ^ {\diamond} \setminus [ a _ {\delta} \gamma_ {1} ], \gamma_ {1}, b _ {\delta}} (z) \right] = F _ {\Omega_ {\delta} ^ {\diamond}, a _ {\delta}, b _ {\delta}} (z),\tag{6.5}
$$

where$\mu _ { \beta _ { c } , \Omega } ^ { a , b }$is the critical Ising measure with Dobrushin boundary conditions in Ω. Write$Z _ { \Omega _ { \delta } ^ { \diamond } , a _ { \delta } , b _ { \delta } }$(resp.$Z _ { \Omega ^ { \diamond } \setminus [ a _ { \delta } x ] , x , b _ { \delta } } )$for the partition function of the Ising model ∖[ ]<sub>with Dobrushin boundary conditions on</sub>$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$(resp.$( \Omega ^ { \circ } \setminus [ a _ { \delta } x ] , x , b _ { \delta } ) )$, i.e. $\begin{array} { r } { Z _ { \Omega ^ { \diamond } \setminus [ a _ { \delta } x ] , x , b _ { \delta } } = \sum _ { \omega } ( \sqrt { 2 } - 1 ) ^ { | \omega | } } \end{array}$. Note that$Z _ { \Omega ^ { \diamond } \setminus [ a _ { \delta } x ] , x , b _ { \delta } }$( ∖ [ ] )is almost the denominator of $F _ { \Omega _ { \delta } ^ { \diamond } \setminus [ a _ { \delta } x ] , x , b _ { \delta } } ( z _ { \delta } )$∑ ( − ). By definition,

$$
\begin{array}{l} Z _ {\Omega_ {\delta} ^ {\diamond}, a _ {\delta}, b _ {\delta}} \mu_ {\beta_ {c}, \Omega} ^ {a, b} (\gamma_ {1} = x) = (\sqrt {2} - 1) Z _ {\Omega^ {\diamond} \setminus [ a _ {\delta} x ], x, b _ {\delta}} \\ = (\sqrt {2} - 1) \mathrm{e} ^ {i \frac {1}{2} W _ {\gamma} (x, b _ {\delta})} \frac {\sum_ {\omega \in \mathcal {E} _ {\Omega^ {\diamond} \setminus [ a _ {\delta} x ]} (x , z _ {\delta})} \mathrm{e} ^ {- i \frac {1}{2} W _ {\gamma} (x , z _ {\delta})} (\sqrt {2} - 1) ^ {| \omega |}}{F _ {\Omega_ {\delta} ^ {\diamond} \setminus [ a _ {\delta} x ] , x , b _ {\delta}} (z _ {\delta})} \\ = \mathrm{e} ^ {i \frac {1}{2} W _ {\gamma} (a _ {\delta}, b _ {\delta})} \frac {\sum_ {\omega \in \mathcal {E} _ {\Omega_ {\delta} ^ {\diamond}} (a _ {\delta} , z _ {\delta})} \mathrm{e} ^ {- i \frac {1}{2} W _ {\gamma} (a _ {\delta} , z _ {\delta})} (\sqrt {2} - 1) ^ {| \omega |} 1 _ {\{\gamma_ {1} = x \}}}{F _ {\Omega_ {\delta} ^ {\diamond} \setminus [ a _ {\delta} x ] , x , b _ {\delta}} (z _ {\delta})} \end{array}
$$

In the second equality, we used the fact that$\mathcal { E } _ { \Omega _ { \delta } ^ { \diamond } \setminus [ a _ { \delta } x ] } ( x , z _ { \delta } )$is in bijection with configurations of$\mathcal { E } _ { \Omega _ { s } ^ { \diamond } } ( a _ { \delta } , z _ { \delta } )$such that$\gamma _ { 1 } = x$E ( )(there is still a diference of weight of${ \sqrt { 2 } } - 1$ E ( ) =between two associated configurations). This gives

$$
\mu_ {\beta_ {c}, \Omega} ^ {a, b} (\gamma_ {1} = x) F _ {\Omega_ {\delta} ^ {\diamond} \setminus [ a _ {\delta} x ], x, b _ {\delta}} (z _ {\delta}) = \frac {\sum_ {\omega \in \mathcal {E} (a _ {\delta} , z _ {\delta})} \mathrm{e} ^ {- i \frac {1}{2} W _ {\gamma} (a _ {\delta} , z _ {\delta})} (\sqrt {2} - 1) ^ {| \omega |} 1 _ {\{\gamma_ {1} = x \}}}{\mathrm{e} ^ {- i \frac {1}{2} W _ {\gamma} (a _ {\delta} , b _ {\delta})} Z _ {\Omega_ {\delta} ^ {\diamond} , a _ {\delta} , b _ {\delta}}}.
$$

The same holds for all possible first steps. Summing over all possibilities, we obtain the expectation on one side of the equality and$F _ { \Omega _ { \delta } ^ { \diamond } , a _ { \delta } , b _ { \delta } } \left( z _ { \delta } \right)$on the other side, thus proving (6.5).□

Exercise 6.9. Prove that spin Ising interfaces converge to$\mathrm { S L E } ( 3 )$. For tightness and ( )the fact that sub-sequential limits are Loewner chains, it is suficient to check Condition. To do so, try to use Theorem 3.16 and the Edwards-Sokal coupling to prove an (⋆)intermediate result similar to Lemma 6.3.

## 7 Other results on the Ising and FK-Ising models

## 7.1 Massive harmonicity away from criticality

In this subsection, we consider the fermionic observable F for the FK-Ising model away from criticality. The Ising model is still solvable and the observable becomes massive harmonic$( i . e . \ \Delta f = \lambda ^ { 2 } f )$. We refer to [BDC11] for details on this paragraph. We start =with a lemma which extends Lemma 5.2 to$p \doteq p _ { s d } = \sqrt { 2 } / ( 1 + \sqrt { 2 } )$.

Lemma 7.1. Let$p \in ( 0 , 1 )$. Consider a vertex$v \in \Omega ^ { \circ } \setminus \partial \Omega ^ { \circ }$

$$
F (A) - F (C) = i \mathrm{e} ^ {\mathrm{i} \alpha} [ F (B) - F (D) ]\tag{7.1}
$$

where A is an adjacent (to v) medial edge pointing towards v and$B , \ C$and D are indexed in such a way that A, B, C and D are found in counterclockwise order. The parameter α is defined by

$$
\mathrm{e} ^ {i \alpha} = \frac {\mathrm{e} ^ {- \mathrm{i} \pi / 4} (1 - p) \sqrt {2} + p}{\mathrm{e} ^ {- \mathrm{i} \pi / 4} p + (1 - p) \sqrt {2}}.
$$

The proof of this statement follows along the same lines as the proof of Lemma 5.2.

Proposition 7.2. For$p < \sqrt { 2 } / ( 1 + \sqrt { 2 } )$, there exists$\xi = \xi ( p ) > 0$such that for every n,

$$
\phi_ {p} (0 \leftrightarrow \mathrm{i} n) \leq \mathrm{e} ^ {- \xi n},\tag{7.2}
$$

where the mesh size of the lattice L is 1.

In this proof, the lattices are rotated by an angle$\pi / 4$. We will be able to estimate /the connectivity probabilities using the FK fermionic observable. Indeed, the observable on the free boundary is related to the probability that sites are connected to the wired arc. More precisely:

Lemma 7.3. Fix$( G , a , b )$a Dobrushin domain and$p \in ( 0 , 1 )$. Let$u \in G$be a site on ( ) ∈ ( ) ∈the free arc, and e be a side of the black diamond associated to u which borders a white diamond of the free arc. Then,

$$
\left| F (e) \right| = \phi_ {p, G} ^ {a, b} (u \leftrightarrow \text { wired   arc }).\tag{7.3}
$$

Proof Let u be a site of the free arc and recall that the exploration path is the interface between the open cluster connected to the wired arc and the dual open cluster connected to the free arc. Since u belongs to the free arc, u is connected to the wired arc if and only if e is on the exploration path, so that

$$
\phi_ {p, G} ^ {a, b} \big (u \leftrightarrow \mathrm{wiredarc} \big) = \phi_ {p, G} ^ {a, b} \big (e \in \gamma \big).
$$

The edge e being on the boundary, the exploration path cannot wind around${ \mathrm { i t } } ,$so that the winding (denoted$W _ { 1 } )$of the curve is deterministic (and easy to write in terms of that of the boundary itself). We deduce from this remark that

$$
\begin{array}{c} | F (e) | = | \phi_ {p, G} ^ {a, b} (\mathrm{e} ^ {\frac {\mathrm{i}}{2} \mathrm{W} _ {1}} 1 _ {e \in \gamma}) | = | \mathrm{e} ^ {\frac {\mathrm{i}}{2} \mathrm{W} _ {1}} \phi_ {p, G} ^ {a, b} (e \in \gamma) | \\ = \phi_ {p, G} ^ {a, b} (e \in \gamma) = \phi_ {p, G} ^ {a, b} (u \leftrightarrow \text {wired arc}). \end{array}
$$

We are now in a position to prove Proposition 7.2. We first prove exponential decay in a strip with Dobrushin boundary conditions, using the observable. Then, we use classical arguments of FK percolation to deduce exponential decay in the bulk. We present the proof quickly (see [BDC11] for a complete proof).

Proof Let$p < p _ { s d }$, and consider the FK-Ising model of parameter p in the strip of <height \`, with free boundary conditions on the top and wired boundary conditions on the bottom (the measure is denoted by$\phi _ { p , S _ { \ell } } ^ { \infty , - \infty } )$). It is easy to check that one can define the FK fermionic observable$F$Sin this case, by using the unique interface from to −∞. This observable is the limit of finite volume observables, therefore it also satisfies ∞Lemma 7.1.

Let$e _ { k }$be the medial edge with center$i k + { \textstyle { \frac { 1 + i } { \sqrt { 2 } } } }$, see Fig. 16. A simple computation +using Lemmata 7.1 and 5.1 plus symmetries of the strip (via translation and horizontal reflection) implies

$$
F \left(e _ {k + 1}\right) = \frac {\left[ 1 + \cos (\pi / 4 - \alpha) \right] \cos (\pi / 4 - \alpha)}{\left[ 1 + \cos (\pi / 4 + \alpha) \right] \cos (\pi / 4 + \alpha)} F \left(e _ {k}\right).\tag{7.4}
$$

Using the previous equality inductively, we find for every$\ell > 0 .$

$$
\left| F (e _ {\ell}) \right| = \mathrm{e} ^ {- \xi \ell} \left| F (e _ {0}) \right| \leq \mathrm{e} ^ {- \xi \ell}
$$

with

$$
\xi := - \ln \frac {\left[ 1 + \cos (\pi / 4 - \alpha) \right] \cos (\pi / 4 - \alpha)}{\left[ 1 + \cos (\pi / 4 + \alpha) \right] \cos (\pi / 4 + \alpha)}.\tag{7.5}
$$

Since$e _ { \ell }$is adjacent to the free arc, Lemma 7.3 implies

$$
\phi_ {p, \mathcal {S} _ {\ell}} ^ {\infty , - \infty} [ \mathrm{i} \ell \leftrightarrow \mathbb {Z} ] = | F (e _ {\ell}) | \leq \mathrm{e} ^ {- \xi \ell}
$$

![](images/page_50_image_9.jpg)

![](images/page_50_image_10.jpg)

Figure 16: Left: Edges$e _ { k }$and$e _ { k + 1 }$. Right: A dual circuit surrounding an open path in the box$[ - a _ { 2 } , a _ { 2 } ] ^ { 2 }$+<sub>. Conditioning on to the most exterior such circuit gives no</sub> [− ]information on the state of the edges inside it.

Now, let$N \in \mathbb { N }$and recall that$\phi _ { p , N } ^ { 0 } : = \phi _ { p , 2 , [ - N , N ] ^ { 2 } } ^ { 0 }$converges to the infinite-volume ∈measure with free boundary conditions$\phi _ { p } ^ { 0 }$[− ]<sub>when N goes to infinity.</sub>

Consider a configuration in the box$[ - N , N ] ^ { 2 }$, and let$A _ { \mathrm { m a x } }$be the site of the cluster of the origin which maximizes the$\ell ^ { \infty }$[− ]-norm max$\cdot \{ | x _ { 1 } | , | x _ { 2 } | \}$(it could be equal to N). If {∣ ∣ ∣ ∣}there is more than one such site, we consider the greatest one in lexicographical order. Assume that$A _ { \mathrm { m a x } }$equals$a = a _ { 1 } + \mathrm { i } a _ { 2 }$with$a _ { 2 } \geq | a _ { 1 } |$(the other cases can be treated the = + ≥ ∣ ∣same way by symmetry, using the rotational invariance of the lattice).

By definition, if$A _ { \mathrm { m a x } }$equals a, a is connected to 0 in$[ - a _ { 2 } , a _ { 2 } ] ^ { 2 }$. In addition to this, [− ]because of our choice of the free boundary conditions, there exists a dual circuit starting from$a + \mathrm { i } / 2$in the dual of$[ - a _ { 2 } , a _ { 2 } ] ^ { 2 }$(which is the same as$\mathbb { L } ^ { * } \cap [ - a _ { 2 } - 1 / 2 , a _ { 2 } + 1 / 2 ] ^ { 2 } )$ + / [− ] ∩ [− − / +and surrounding both a and 0. Let Γ be the outermost such dual circuit: we get

$$
\phi_ {p, N} ^ {0} \big (A _ {\max} = a \big) = \sum_ {\gamma} \phi_ {p, N} ^ {0} \big (a \leftrightarrow 0 | \Gamma = \gamma \big) \phi_ {p, N} ^ {0} \big (\Gamma = \gamma \big),\tag{7.6}
$$

where the sum is over contours$\gamma$in the dual of$[ - a _ { 2 } , a _ { 2 } ] ^ { 2 }$that surround both a and 0.

The event$\{ \Gamma = \gamma \}$[− ] is measurable in terms of edges outside or on$\gamma .$In addition, { = }conditioning on this event implies that the edges of$\gamma$are dual-open. Therefore, from the domain Markov property, the conditional distribution of the configuration inside γ is a FK percolation model with free boundary conditions. Comparison between boundary conditions implies that the probability of$\{ a  0 \}$conditionally on$\{ \Gamma = \gamma \}$is smaller than the probability of$\{ a  0 \}${in the strip${ \boldsymbol { S } } _ { a _ { 2 } }$} { = }with free boundary conditions on the { ↔ } Stop and wired boundary conditions on the bottom. Hence, for any such$\gamma _ { ; }$, we get

$$
\phi_ {p, N} ^ {0} \big (a \leftrightarrow 0 | \Gamma = \gamma \big) \leq \phi_ {p, \mathcal {S} _ {a _ {2}}} ^ {\infty , - \infty} \big (a \leftrightarrow 0 \big) = \phi_ {p, \mathcal {S} _ {a _ {2}}} ^ {\infty , - \infty} \big (a \leftrightarrow \mathbb {Z} \big) \leq \mathrm{e} ^ {- \xi a _ {2}}
$$

(observe that for the second measure,$\mathbb { Z }$is wired, so that$\{ a  0 \}$and$\{ a  \mathbb { Z } \}$have the same probability). Plugging this into (7.6), we obtain

$$
\phi_ {p, N} ^ {0} \big (A _ {\max} = a \big) \leq \sum_ {\gamma} \mathrm{e} ^ {- \xi \max \{a _ {1}, a _ {2} \}} \phi_ {p, N} ^ {0} \big (\Gamma = \gamma \big) \leq \mathrm{e} ^ {- \xi a _ {2}} = \mathrm{e} ^ {- \xi \max \{a _ {1}, a _ {2} \}}.
$$

Fix$n \leq N$. We deduce from the previous inequality that there exists a constant $0 < c < \infty$≤such that

$$
\phi_ {p, N} ^ {0} \big (0 \leftrightarrow \mathbb {Z} ^ {2} \setminus [ - n, n ] ^ {2} \big) \leq \sum_ {a \in [ - N, N ] ^ {2} \setminus [ - n, n ] ^ {2}} \phi_ {p, N} ^ {0} \big (A _ {\max} = a \big) \leq c n e ^ {- \xi n}.
$$

Since the estimate is uniform in$N .$, we deduce that

$$
\phi_ {p} ^ {0} (0 \leftrightarrow i n) \leq \phi_ {p} ^ {0} (0 \leftrightarrow \mathbb {Z} ^ {2} \setminus [ - n, n ] ^ {2}) \leq c n e ^ {- \xi n}.\tag{7.7}
$$

Theorem 7.4. The critical parameter for the FK-Ising model is${ \sqrt { 2 } } / ( 1 + { \sqrt { 2 } } )$. The critical inverse-temperature for the Ising model is${ \scriptstyle { \frac { 1 } { 2 } } } \ln ( 1 + { \sqrt { 2 } } )$

Proof The inequality$p _ { c } \ge \sqrt { 2 } / ( 1 + \sqrt { 2 } )$follows from Proposition 7.2 since there is no infinite cluster for$\phi _ { p , 2 } ^ { 0 }$≥when$p < p _ { s d }$)(the probability that 0 and in are connected <converges to 0). In order to prove that$p _ { c } \leq \sqrt { 2 } / ( 1 + \sqrt { 2 } )$, we harness the following standard reasoning.

Let$A _ { n }$be the event that the point n N is in an open circuit which surrounds the ∈origin. Notice that this event is included in the event that the point$n \in \mathbb { N }$is in a cluster of radius larger than n. For$p < \sqrt { 2 } / ( 1 + \sqrt { 2 } )$∈, a modification of (7.7) implies that the probability of$A _ { n }$< /( + )decays exponentially fast. The Borel-Cantelli lemma shows that there is almost surely a finite number of n such that$A _ { n }$occurs. In other words, there is a.s. only a finite number of open circuits surrounding the origin, which enforces the existence of an infinite dual cluster whenever$p < \sqrt { 2 } / ( 1 + \sqrt { 2 } )$. Using duality, the primal model is supercritical whenever$p > \sqrt { 2 } / ( 1 + \sqrt { 2 } )$/( + ), which implies$p _ { c } \leq \sqrt { 2 } / ( 1 + \sqrt { 2 } )$□

In fact, the FK fermionic observable$F _ { \delta }$in a Dobrushin domain$\left( \Omega _ { \delta } ^ { \circ } , a _ { \delta } , b _ { \delta } \right)$is massive harmonic when$p \neq p _ { s d }$. More precisely,

Proposition 7.5. Let$p \neq p _ { s d }$

$$
\Delta_ {\delta} F _ {\delta} (v) = (\cos 2 \alpha - 1) F _ {\delta} (v)\tag{7.8}
$$

for every$v \in \Omega _ { \delta } ^ { \circ } \setminus \partial \Omega _ { \delta } ^ { \circ }$, where$\Delta _ { \delta }$is the average on sites at distance$\sqrt { 2 } \delta$minus the value ∈at the point.

When δ goes to 0, one can perform two scaling limits. If$p = p _ { s d } \big ( 1 - \lambda \delta \big )$goes to$p _ { s d }$as δ goes to$\begin{array} { r } { 0 , \frac { 1 } { \delta ^ { 2 } } \big ( \Delta _ { \delta } + \big [ 1 - \cos 2 \alpha \big ] I \big ) } \end{array}$converges to$\Delta + \lambda ^ { 2 } I$=. Then$F _ { \delta }$( − )(properly normalized) ( + [ − ] )should converge to a function f satisfying$\Delta f + \lambda ^ { 2 } f = 0$inside the domain. Except for $\lambda = 0$+ =, the limit will not be holomorphic, but massive harmonic. Discrete curves should =converge to a limit which is not absolutely continuous with respect to SLE(16/3). The study of this regime, connected to massive SLEs, is a very interesting subject.

If we fix$p < p _ { s d } ,$one can interpret massive harmonicity in terms of killed random <walks. Roughly speaking,$F _ { \delta } ( v )$is the probability that a killed random walk starting at v visits the wired arc$\partial _ { b a }$( ). Large deviation estimates on random walks allow to compute the asymptotic of$F _ { \delta }$inside the domain. In [BDC11], a surprising link (first noticed by Messikh [Mes06]) between correlation lengths of the Ising model and large deviations estimates of random walks is presented. We state the result in the following theorem:

Theorem 7.6. Fix$\beta < \beta _ { c }$(and α associated to it) and set

$$
m (\beta) := \cos (2 \alpha).
$$

For any$x \in$L,

$$
- \lim _ {n \to \infty} \frac {1}{n} \ln \mu_ {\beta} \bigl [ \sigma_ {0} \sigma (n x) \bigr ] = - \lim _ {n \to \infty} \frac {1}{n} \ln G _ {m (\beta)} (0, n x).\tag{7.9}
$$

Above,$G _ { m } ( 0 , x ) : = \mathbb { E } ^ { x } [ m ^ { \tau } ]$for any$x \in \mathbb { L }$and$m < 1$, where$\tau$is the hitting time of the origin and$\mathbb { P } ^ { x } \mathrm { ~ } _ { i s }$∶= [ ] ∈ < the law of a simple random walk starting at x.

The massive Green function$G _ { m } ( 0 , x )$on the right of (7.9) has been widely studied. ( )In particular, we can compute the rate of decay in any direction and deduce Theorem 2.3 and Theorem 2.4 (see e.g. [Mes06]).

Exercise 7.7. Prove Lemma 7.1 and the fact that F is massive harmonic inside the domain.

## 7.2 Russo-Seymour-Welsh Theorem for FK-Ising

In this section, we sketch the proof of Theorem 3.16; see [DCHN10] for details. We would like to emphasize that this result does not make use of scaling limits. Therefore, it is mostly independent of Sections 5 and 6.

We start by presenting a link between discrete harmonic measures and the probability for a point on the free arc$\partial _ { a b }$of a FK Dobrushin domain to be connected to the wired arc$\partial _ { b a }$

Let us first define a notion of discrete harmonic measure in a FK Dobrushin domain $\Omega _ { \delta }$which is slightly diferent from the usual one. First extend$\Omega _ { \delta } \cup \Omega _ { \delta } ^ { \star }$by adding two extra layers of vertices: one layer of white faces adjacent to$\partial _ { a b } ^ { \star } ,$∪and one layer of black faces adjacent to$\partial _ { b a }$. We denote the extended domains by$\tilde { \Omega } _ { \delta }$and$\tilde { \Omega } _ { \delta } ^ { \star }$

Define$( X _ { t } ^ { \bullet } ) _ { t \geq 0 }$to be the continuous-time random walk on the black faces that jumps ( ) ≥with rate 1 on neighbors, except for the faces on the extra layer adjacent to$\partial _ { a b }$onto which it jumps with rate$\rho : = 2 / ( \sqrt { 2 } + 1 )$. For$B \in \Omega _ { \delta }$, we denote by$\tilde { H } ^ { \bullet } ( \boldsymbol { B } )$the probability that the random walk$X _ { t } ^ { \bullet }$∶= /( + )starting at B hits$\partial \tilde { \Omega } _ { \delta }$on the wired arc$\partial _ { b a }$( )(in other words, if the random walk hits$\partial _ { b a }$before hitting the extra layer adjacent to$\partial _ { a b } ^ { \star } )$. This quantity is called the (modified) harmonic measure of$\partial _ { b a }$seen from B. Similarly, one can define a modified random walk$X _ { t } ^ { \circ }$and the associated harmonic measure of$\partial _ { a b } ^ { \star }$seen from w. We denote it by$H ^ { \circ } ( w )$

Proposition 7.8. Consider a FK Dobrushin domain$\left( \Omega _ { \delta } , a _ { \delta } , b _ { \delta } \right)$, for any site B on the free arc$\partial _ { a b }$

$$
\sqrt {\tilde {H} ^ {\circ} (W)} \leq \phi_ {\Omega_ {\delta}, p _ {s d}} ^ {a _ {\delta}, b _ {\delta}} [ B \leftrightarrow \partial_ {b a} ] \leq \sqrt {\tilde {H} ^ {\bullet} (B)},\tag{7.10}
$$

where W is any dual neighbor of B not on$\partial _ { a b } ^ { \star }$

This proposition raises a connection between harmonic measure and connectivity properties of the FK-Ising model. To study connectivity probabilities for the FK-Ising model, it sufices to estimate events for simple random walks (slightly repelled on the boundary). The proof makes use of a variant of the "boundary modification trick". This trick was introduced in [CS09] to prove Theorem$2 . 1 1$. It can be summarized as follows: one can extend the function H by 0 or 1 on the two extra layers, then$H ^ { \bullet } ~ ( \mathrm { r e s p . } ~ H ^ { \circ } )$ is subharmonic (resp. superharmonic) for the Laplacian associated to the random walk $X ^ { \bullet } \ ( \mathrm { r e s p . } \ X ^ { \circ } )$. Interestingly,$H ^ { \bullet }$is not subharmonic for the usual Laplacian. This trick allows us to fix the boundary conditions (0 or 1), at the cost of a slightly modified notion of harmonicity.

We can now give the idea of the proof of Theorem 3.16 (we refer to [DCHN10] for details). The proof is a second moment estimate on the number of pairs of connected sites on opposite edges of the rectangle. We mention that another road to Theorem 3.16 has been proposed in [KS10].

Proof of Theorem 3.16 (Sketch) Let$R _ { n } = [ 0 , 4 n ] \times [ 0 , n ]$be a rectangle and let $N$be the number of pairs$( x , y ) , \ x \ \in \ \{ 0 \} \times [ 0 , n ]$]and$y \in \{ 4 n \} \times [ 0 , n ]$such that x is connected to$y$( ) ∈ { } × [ ] ∈ { } × [ ]by an open path. The expectation of N is easy to obtain using the previous proposition. Indeed, it is the sum over all pairs$x , y$of the probability of$\{ x  y \}$ { ↔ }when the boundary conditions are free. Free boundary conditions can be thought of as a degenerate case of a Dobrushin domain, where$a = b = y$. In other words, we want to = =estimate the probability that x is connected to the wired arc$\partial _ { b a } = \{ y \}$. Except when x and$y$are close to the corners, the harmonic measure of$y$= { }seen from x is of order$1 / n ^ { 2 }$ so that the probability of$\{ x  y \}$is of order$1 / n$/. Therefore, there exists a universal constant$c > 0$such that$\phi _ { p _ { s d } , R _ { n } } ^ { f } [ N ] \geq c n$

> [ ] ≥The second moment estimate is harder to obtain, as usual. Nevertheless, it can be proved, using successive conditioning and Proposition 7.8, that$\phi _ { p _ { s d } , R _ { n } } ^ { f } [ N ^ { 2 } ] \leq C n ^ { 2 }$for some universal$C > 0 ;$[ ] ≤see [DCHN10] for a complete proof. Using the Cauchy-Schwarz inequality, we find

$$
\phi_ {p _ {s d}, R _ {n}} ^ {f} [ N > 0 ] \phi_ {p _ {s d}, R _ {n}} ^ {f} [ N ^ {2} ] \geq \phi_ {p _ {s d}, R _ {n}} ^ {f} [ N ] ^ {2}\tag{7.11}
$$

which implies

$$
\phi_ {R _ {n}, p _ {s d}} ^ {f} [ \exists \mathrm{opencrossing} ] = \phi_ {R _ {n}, p _ {s d}} ^ {f} [ N > 0 ] \geq c ^ {2} / C\tag{7.12}
$$

uniformly in n.

We have already seen that Theorem 3.16 is central for proving tightness of interfaces. We would also like to mention an elementary consequence of Theorem 3.16.

Proposition 7.9. There exist constants$0 < c , C , \delta , \Delta < \infty$such that for any sites$x , y \in \mathbb { L } ,$

$$
\frac {c}{| x - y | ^ {\delta}} \leq \mu_ {\beta_ {c}} [ \sigma_ {x} \sigma_ {y} ] \leq \frac {C}{| x - y | ^ {\Delta}}\tag{7.13}
$$

where$\mu _ { \beta _ { c } }$is the unique infinite-volume measure at criticality.

Proof Using the Edwards-Sokal coupling, (7.13) can be rephrased as

$$
\frac {c}{| x - y | ^ {\delta}} \leq \phi_ {p _ {s d}, 2} [ x \leftrightarrow y ] \leq \frac {C}{| x - y | ^ {\Delta}},
$$

where$\phi _ { p _ { s d } , 2 }$is the unique FK-Ising infinite-volume measure at criticality. In order to get the upper bound, it sufices to prove that$\phi _ { p _ { s d } , 2 } ( 0  \partial \Lambda _ { k } )$decays polynomially fast, where$\Lambda _ { k }$is the box of size$k = | x - y |$( ↔ )centered at x. We consider the annuli $A _ { n } = S _ { 2 ^ { n - 1 } , 2 ^ { n } } ( x )$for$n \leq \ln _ { 2 } k .$, and$\mathcal E ( A _ { n } )$− ∣the event that there is an open path crossing $A _ { n }$= ( ) ≤ E( )from the inner to the outer boundary. We know from Corollary 6.3 (which is a direct application of Theorem 3.16) that there exists a constant$c < 1$such that

$$
\phi_ {A _ {n}, p _ {s d}, 2} ^ {1} \big (\mathcal {E} (A _ {n}) \big) \leq c
$$

for all$n \geq 1$. By successive conditionings, we then obtain

$$
\phi_ {p _ {s d}, 2} \big (0 \leftrightarrow \partial \Lambda_ {k} \big) \leq \prod_ {n = 1} ^ {\ln_ {2} k} \phi_ {A _ {n}, p _ {s d}, 2} ^ {1} \big (\mathcal {E} \big (A _ {n} \big) \big) \leq c ^ {N},
$$

and the desired result follows. The lower bound can be done following the same kind of arguments (we leave it as an exercise).□

Therefore, the behavior at criticality (power law decay of correlations) is very diferent from the subcritical phase (exponential decay of correlations). Actually, the previous result is far from optimal. One can compute correlations between spins of a domain very explicitly. In particular,$\mu _ { \beta _ { c } } [ \sigma _ { x } \sigma _ { y } ]$behaves like$| x - y | ^ { - \alpha }$, where$\alpha = 1 / 4$. We mention [ ] ∣ − ∣ = /that α is one example of critical exponent. Even though we did not discuss how compute critical exponents, we mention that the technology developed in these notes has for its main purpose their computation.

To conclude this section, we mention that Theorem 3.16 leads to ratio mixing properties (see Exercise 7.10) of the Ising model. Recently, Lubetzky and Sly [LS10] used these spatial mixing properties in order to prove an important conjecture on the mixing time of the Glauber dynamics of the Ising model at criticality.

Exercise 7.10 (Spatial mixing). Prove that there exist$c , \Delta > 0$such that for any$r \leq R$,

$$
\left| \phi_ {p _ {s d}, 2} (A \cap B) - \phi_ {p _ {s d}, 2} (A) \phi_ {p _ {s d}, 2} (B) \right| \leq c \left(\frac {r}{R}\right) ^ {\Delta} \phi_ {p _ {s d}, 2} (A) \phi_ {p _ {s d}, 2} (B)\tag{7.14}
$$

for any event$A \ ( r e s p . \ B )$depending only on the edges in the box$[ - r , r ] ^ { 2 }$(resp. outside $[ - R , R ] ^ { 2 } )$

## 7.3 Discrete singularities and energy density of the Ising model

In this subsection, we would like to emphasize the fact that slight modifications of the spin fermionic observable can be used directly to compute interesting quantities of the model. Now, we briefly present the example of the energy density between two neighboring sites x and y (Theorem 2.12).

So far, we considered observables depending on a point a on the boundary of a domain, but we could allow more flexibility and move a inside the domain: for$a _ { \delta } \in \Omega _ { \delta } ^ { \circ }$, we define the fermionic observable$F _ { \Omega _ { \delta } } ^ { a _ { \delta } } ( z _ { \delta } )$for$z _ { \delta } \neq a _ { \delta }$by

$$
F _ {\Omega_ {\delta}} ^ {a _ {\delta}} (z _ {\delta}) = \lambda \frac {\sum_ {\omega \in \mathcal {E} (a _ {\delta} , z _ {\delta})} \mathrm{e} ^ {- \frac {1}{2} i W _ {\gamma (\omega)} (a _ {\delta} , z _ {\delta})} (\sqrt {2} - 1) ^ {| \omega |}}{\sum_ {\omega \in \mathcal {E}} (\sqrt {2} - 1) ^ {| \omega |}}\tag{7.15}
$$

where λ is a well-chosen explicit complex number. Note that the denominator of the observable is simply the partition function for free boundary conditions$Z _ { \beta _ { c } , G } ^ { f }$. Actually, using the high-temperature expansion of the Ising model and local rearrangements, the observable can be related to spin correlations [HS10]:

Lemma 7.11. Let xy be an horizontal edge of$\Omega _ { \delta }$. Then

$$
\lambda \mu_ {\beta_ {c}, \Omega_ {\delta}} ^ {f} [ \sigma_ {x} \sigma_ {y} ] = P _ {\ell (a c)} [ F _ {\Omega_ {\delta}} ^ {a} (c) ] + P _ {\ell (a d)} [ F _ {\Omega_ {\delta}} ^ {a} (d) ]
$$

where a is the center of xy ,$\begin{array} { r } { c = a + \delta \frac { 1 + i } { \sqrt { 2 } } } \end{array}$and$\begin{array} { r } { d = a - \delta \frac { 1 + i } { \sqrt { 2 } } } \end{array}$

If λ is chosen carefully, the function$F _ { \delta } ^ { a _ { \delta } }$is s-holomorphic on$\Omega _ { \delta } \setminus \{ a _ { \delta } \}$. Moreover, ∖ { }its complex argument is fixed on the boundary of the domain. Yet, the function is not s-holomorphic at$a _ { \delta }$(meaning that there is no way of defining$F _ { \Omega _ { \delta } } ^ { a } ( a _ { \delta } )$so that the function is s-holomorphic at$a _ { \delta } )$( ). In other words, there is a discrete singularity at$^ { a , }$ whose behavior is related to the spin-correlation.

We briefly explain how one can address the problem of discrete singularities, and we refer to [HS10] for a complete study of this case. In the continuum, singularities are removed by subtracting Green functions. In the discrete context, we will do the same. We thus need to construct a discrete s-holomorphic Green function. Preholomorphic Green functions<sup>6</sup> were already constructed in [Ken00]. These functions are not s-holomorphic but relevant linear combinations of them are, see [HS10]. We mention that the s-holomorphic Green functions are very explicit and their convergence when the mesh size goes to 0 can be studied.

Proof of Theorem 2.12 (Sketch) The function$F _ { \delta } ^ { a _ { \delta } } / \delta$converges uniformly on any compact subset of$\Omega \setminus \{ a \}$/. This fact is not helpful, since the interesting values of$F _ { \delta } ^ { a _ { \delta } }$are ∖{ }located at neighbors of the singularity. It can be proved that, subtracting a well-chosen s-holomorphic Green function$g _ { \Omega _ { \delta } } ^ { a _ { \delta } }$, one can erase the singularity at$a _ { \delta }$. More precisely, one can show that$[ F _ { \delta } ^ { a _ { \delta } } - g _ { \Omega _ { \delta } } ^ { a _ { \delta } } ] / \delta$converges uniformly on Ω towards an explicit conformal [ − ]/map. The value of this map at a is$\frac { \lambda } { \pi } \phi _ { a } ^ { \prime } ( a )$. Now,$\mu _ { \beta _ { c } , \Omega _ { \delta } } ^ { f } [ \sigma _ { x } \sigma _ { y } ]$can be expressed in terms of$F _ { \delta } ^ { a _ { \delta } }$for neighboring vertices of$a _ { \delta }$( ) [. Moreover, values of$g _ { \Omega _ { \delta } } ^ { a _ { \delta } }$for neighbors of$a _ { \delta }$ can be computed explicitly. Using the fact that

$$
F _ {\delta} ^ {a _ {\delta}} = g _ {\Omega_ {\delta}} ^ {a _ {\delta}} + \delta \cdot \frac {1}{\delta} \big [ F _ {\delta} ^ {a _ {\delta}} - g _ {\Omega_ {\delta}} ^ {a _ {\delta}} \big ],
$$

and Lemma 7.11, the convergence result described above translates into the following asymptotics for the spin correlation of two neighbors

$$
\mu_ {\beta_ {c}, \Omega_ {\delta}} ^ {f} [ \sigma_ {x} \sigma_ {y} ] = \frac {\sqrt {2}}{2} - \delta \frac {1}{\pi} \phi_ {a} ^ {\prime} (a) + o (\delta).
$$

## 8 Many questions and a few answers

## 8.1 Universality of the Ising model

Until now, we considered only the square lattice Ising model. Nevertheless, normalization group theory predicts that the scaling limit should be universal. In other words, the limit of critical Ising models on planar graphs should always be the same. In particular, the scaling limit of interfaces in spin Dobrushin domains should converge to SLE(3).

Of course, one should be careful about the way the graph is drawn in the plane. For instance, the isotropic spin Ising model of Section 2, when considered on a stretched square lattice (every square is replaced by a rectangle), is not conformally invariant (it is not invariant under rotations). Isoradial graphs form a large family of graphs possessing a natural embedding on which a critical Ising model is expected to be conformally invariant. More details are now provided about this fact.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>i.e. satisfying the Cauchy-Riemann equation except at a certain point.</span></small>

Definition 8.1. A rhombic embedding of a graph$G$is a planar quadrangulation satisfying the following properties:

• the vertices of the quadrangulation are the vertices of G and$G ^ { \star }$

• the edges connect vertices of G to vertices of$G ^ { \star }$corresponding to adjacent faces of G,

• all the edges of the quadrangulation have equal length, see Fig. 10.

A graph which admits a rhombic embedding is called isoradial.

Isoradial graphs are fundamental for two reasons. First, discrete complex analysis on isoradial graphs was extensively studied (see e.g. [Mer01, Ken02, CS08]) as explained in Section 4. Second, the Ising model on isoradial graphs satisfies very specific integrability properties and a natural critical point can be defined as follows. Let $J _ { x y } = \mathrm { a r c t a n h } [ \tan \left( \theta / 2 \right) ]$where θ is the half-angle at the corner x (or equivalently y) = [ ( / )]made by the rhombus associated to the edge xy . One can define the critical Ising model with Hamiltonian

$$
H (\sigma) = - \sum_ {x \sim y} J _ {x y} \sigma_ {x} \sigma_ {y}.
$$

This Ising model on isoradial graphs (with rhombic embedding) is critical and conformally invariant in the following sense:

Theorem 8.2 (Chelkak, Smirnov [CS09]). The interfaces of the critical Ising model on isoradial graphs converge, as the mesh size goes to 0, to the chordal Schramm-Loewner Evolution with$\kappa = 3$

Note that the previous theorem is uniform on any rhombic graph discretizing a given domain Ω, a, b , as soon as the edge-length of rhombi is small enough. This provides a ( )first step towards universality for the Ising model.

Question 8.3. Since not every topological quadrangulation admits a rhombic embedding [KS05], can another embedding with a suficiently nice version of discrete complex analysis always be found?

Question 8.4. Is there a more general discrete setup where one can get similar estimates, in particular convergence of preholomorphic functions to the holomorphic ones in the scaling limit?

In another direction, consider a biperiodic lattice (one can think of the universal Lcover of a finite graph on the torus), and define a Hamiltonian with periodic correlations $\left( J _ { x y } \right)$by setting$\begin{array} { r } { H ( \sigma ) ~ = ~ - \sum _ { x \sim y } J _ { x y } \sigma _ { x } \sigma _ { y } } \end{array}$. The Ising model with this Hamiltonian makes ( ) ( ) = − ∑ ∼perfect sense and there exists a critical inverse temperature separating the disordered phase from the ordered phase.

Question 8.5. Prove that there always exists an embedding of$\mathcal { L }$such that the Ising model on$\mathcal { L }$is conformally invariant.

![](images/page_57_chart_0.jpg)

Figure 17: The phase diagram of the FK percolation model on the square lattice.

## 8.2 Full scaling limit of critical Ising model

It has been proved in [KS10] that the scaling limit of Ising interfaces in Dobrushin domains is SLE(3). The next question is to understand the full scaling limit of the interfaces. This question raises interesting technical problems. Consider the Ising model with free boundary conditions. Interfaces now form a family of loops. By consistency, each loop should look like a SLE(3). In [HK11], Hongler and Kytolä made one step towards the complete picture by studying interfaces with$+ / - / \mathrm { f r e e }$boundary conditions.

+/−/Shefield and Werner [SW10a, SW10b] introduced a one-parameter family of processes of non-intersecting loops which are conformally invariant – called the Conformal Loop Ensembles CLE(κ) for$\kappa > 8 / 3$. Not surprisingly, loops of CLE(κ) are locally similar to$\operatorname { S L E } ( \kappa )$> /, and these processes are natural candidates for the scaling limits of planar models of statistical physics. In the case of the Ising model, the limits of interfaces all together should be a CLE(3).

## 8.3 FK percolation for general cluster-weight$q \geq 0$

The FK percolation with cluster-weight$q \in ( 0 , \infty )$is conjectured to be critical for$p _ { c } ( q ) =$ ${ \sqrt { q } } / ( 1 + { \sqrt { q } } )$(see [BDC10] for the case$q \geq 1 )$∞) ( ) =. Critical FK percolation is expected to /( + ) ≥exhibit a very rich phase transition, whose properties depend strongly on the value of q (see Fig. 17). We use generalizations of the FK fermionic observable to predict the critical behavior for general q.

## 8.3.1 Case$0 \leq q \leq 4 .$

The critical FK percolation in Dobrushin domains can be associated to a loop model exactly like the FK-Ising model: each loop receives a weight$\sqrt { q }$. In this context, one can define a natural generalization of the fermionic observable on medial edges, called a parafermionic observable, by the formula

$$
F (e) = \mathbb {E} _ {\Omega_ {\delta} ^ {\diamond}, a _ {\delta}, b _ {\delta}, p, q} [ \mathrm{e} ^ {\sigma \cdot \mathrm{i} W _ {\gamma} (e, b _ {\delta})} 1 _ {e \in \gamma} ],\tag{8.1}
$$

where$\sigma = \sigma ( q )$is called the spin$( \sigma$takes a special value described below). Lemma 5.2 = ( )has a natural generalization to any$q \in [ 0 , \infty )$:

Proposition 8.6. For$q \leq 4$and any FK Dobrushin domain, consider the observable F at criticality with spin$\begin{array} { r } { \sigma = 1 - \frac { 2 } { \pi } \operatorname { a r c c o s } ( \sqrt { q } / 2 ) } \end{array}$. For any medial vertex inside the domain,

$$
F (N) - F (S) = i [ F (E) - F (W) ]\tag{8.2}
$$

where N, E, S and W are the four medial edges adjacent to the vertex.

These relations can be understood as Cauchy-Riemann equations around some vertices. Importantly,$F$is not determined by these relations for general q (the number of variables exceeds the number of equations). For$q = 2$, which corresponds to$\sigma = 1 / 2$, the = = /complex argument modulo π of the observable ofers additional relations (Lemma 5.1) and it is then possible to obtain the preholomophicity (Proposition 5.3).

Parafermionic observables can be defined on medial vertices by the formula

$$
F (v) = \frac {1}{2} \sum_ {e \sim v} F (e)
$$

where the summation is over medial edges with v as an endpoint. Even though they are only weakly-holomorphic, one still expects them to converge to a holomorphic function. The natural candidate for the limit is not hard to find:

Conjecture 8.7. Let$q \leq 4$and$( \Omega , a , b )$be a simply connected domain with two points ≤on its boundary. For every$z \in \Omega$，

$$
\frac {1}{(2 \delta) ^ {\sigma}} F _ {\delta} (z) \rightarrow \phi^ {\prime} (z) ^ {\sigma} \quad w h e n \delta \rightarrow 0\tag{8.3}
$$

where$\begin{array} { r } { \sigma = 1 - \frac { 2 } { \pi } \operatorname { a r c c o s } ( \sqrt { q } / 2 ) , F _ { \delta } } \end{array}$is the observable (at$p _ { c } ( q ) )$in discrete domains with spin$\sigma ,$= − ( / ) and φ is any conformal map from Ω$t o \mathbb { R } \times ( 0 , 1 )$( )sending a to and b to .

Being mainly interested in the convergence of interfaces, one could try to follow the same program as in Section 6:

• Prove compactness of the interfaces.

• Show that sub-sequential limits are Loewner chains (with unknown random driving process$W _ { t } )$.

• Prove the convergence of discrete observables (more precisely martingales) of the model.

• Extract from the limit of these observables enough information to evaluate the conditional expectation and quadratic variation of increments of$W _ { t }$(in order to harness the Lévy theorem). This would imply that$W _ { t }$is the Brownian motion with a particular speed κ and so curves converge to$\operatorname { S L E } ( \kappa )$

The third step, corresponding to Conjecture 8.7, should be the most dificult. Note that the first two steps are also open for$q \neq 0 , 1 , 2$. Even though the convergence of ≠observables is still unproved, one can perform a computation similar to the proof of Proposition 6.7 in order to identify the possible limiting curves (this is the fourth step). The following conjecture is thus obtained:

Conjecture 8.8. For$q \leq 4 ,$, the law of critical FK interfaces converges to the Schramm-≤Loewner Evolution with parameter$\kappa = { 4 \pi } / \operatorname { a r c c o s } ( - \sqrt { q } / 2 )$

The conjecture was proved by Lawler, Schramm and Werner [LSW04a] for$q = 0 ,$ =when they showed that the perimeter curve of the uniform spanning tree converges to $\mathrm { S L E } ( 8 )$Note that the loop representation with Dobrushin boundary conditions still makes sense for$q \ : = \ : 0$(more precisely for the model obtained by letting$q  0$and $p / q \to 0 )$= →. In fact, configurations have no loops, just a curve running from a to b (which / →then necessarily passes through all the edges), with all configurations being equally probable. The$q = 2$case corresponds to Theorem 3.13. All other cases are wide open. The$q = 1$=case is particularly interesting, since it is actually bond percolation on the =square lattice.

## 8.3.2 Case$q > 4 .$

The picture is very diferent and no conformal invariance is expected to hold. The phase transition is conjectured to be of first order : there are multiple infinite-volume measures at criticality. In particular, the critical FK percolation with wired boundary conditions should possess an infinite cluster almost surely while the critical FK percolation with free boundary conditions should not (in this case, the connectivity probabilities should even decay exponentially fast). This result is known only for$q \geq 2 5 . 7 2$(see [Gri06] and references therein).

Note that the observable still makes sense in the$q > 4$case, providing σ is chosen so that$2 \sin ( \pi \sigma / 2 ) = { \sqrt { q } }$>. Interestingly, σ becomes purely imaginary in this case. A ( / ) =natural question is to relate this change of behavior for σ with the transition between conformally invariant critical behavior and first order critical behavior.

## <sub>8.4 O</sub>(<sub>n</sub>) <sub>models on the hexagonal lattice</sub>

The Ising fermionic observable was introduced in [Smi06] in the setting of general$O ( n )$ ( )models on the hexagonal lattice. This model, introduced in [DMNS81] on the hexagonal lattice, is a lattice gas of non-intersecting loops. More precisely, consider configurations of non-intersecting simple loops on a finite subgraph of the hexagonal lattice and introduce two parameters: a loop-weight n$\geq 0$(in fact$n \geq - 2 )$and an edge-weight$x > 0$, and ≥ ≥ −ask the probability of a configuration to be proportional to$n ^ { \# }$loops # edges

Alternatively, an interface between two boundary points could be added: in this case configurations are composed of non-intersecting simple loops and one self-avoiding interface (avoiding all the loops) from a to b.

The O 0 model is the self-avoiding walk, since no loop is allowed (there is still a self-( )avoiding path from a to b). The$O ( 1 )$model is the high-temperature expansion of the ( )Ising model on the hexagonal lattice. For integers$n .$, the$O ( n )$-model is an approximation of the high-temperature expansion of spin$O ( n )$( )-models (models for which spins are ndimensional unit vectors).

The physicist Bernard Nienhuis [Nie82, Nie84] conjectured that$O ( n )$-models in the range n 0, 2 (after certain modifications$n \in ( - 2 , 2 )$( )would work) exhibit a Berezinsky-∈ ( ) ∈ (−Kosterlitz-Thouless phase transition [Ber72, KT73]:

![](images/page_60_chart_0.jpg)

Figure 18: The phase diagram of the$O ( n )$model on the hexagonal lattice.

Conjecture 8.9. Let$x _ { c } ( n ) = 1 / \sqrt { 2 + \sqrt { 2 - n } }$. For$x < x _ { c } ( n )$(resp.$x \geq x _ { c } ( n ) )$the ( ) = / + − < ( ) ≥ ( )probability that two points are on the same loop decays exponentially fast (as a power law).

The conjecture was rigorously established for two cases only. When$n = 1$, the critical value is related to the critical temperature of the Ising model. When$n = 0$=, it was recently proved in [DCS10] that$\sqrt { 2 + { \sqrt { 2 } } }$=is the connective constant of the hexagonal lattice.

+It turns out that the model exhibits one critical behavior at$x _ { c } ( n )$and another on the interval$( x _ { c } ( n ) , + \infty )$( ), corresponding to dilute and dense phases (when in the limit ( ( ) +∞)the loops are simple and non-simple respectively), see Fig. 18. In addition to this, the two critical regimes are expected to be conformally invariant.

Exactly as in the case of FK percolation, the definition of the spin fermionic observable can be extended. For a discrete domain Ω with two points on the boundary a and $b ,$the parafermionic observable is defined on middle of edges by

$$
F (z) = \frac {\sum_ {\omega \in \mathcal {E} (a , z)} \mathrm{e} ^ {- \sigma i W _ {\gamma} (a , z)} x ^ {\# \text {edges in} \omega} n ^ {\# \text {loops in} \omega}}{\sum_ {\omega \in \mathcal {E} (a , b)} \mathrm{e} ^ {- \sigma i W _ {\gamma} (a , b)} x ^ {\# \text {edges in} \omega} n ^ {\# \text {loops in} \omega}}\tag{8.4}
$$

where$\mathcal { E } ( a , z )$is the set of configurations of loops with one interface from a to z. One E( )can easily prove that the observable satisfies local relations at the (conjectured) critical value if$\sigma$is chosen carefully.

Proposition 8.10.$I f x = x _ { c } ( n ) = 1 / \sqrt { 2 + \sqrt { 2 - n } } ;$let$F$be the parafermionic observable with spin$\begin{array} { r } { \sigma = \sigma ( n ) = 1 - \frac { 3 } { 4 \pi } } \end{array}$( )arccos$\left( - n / 2 \right)$+; then

$$
(p - v) F (p) + (q - v) F (q) + (r - v) F (r) = 0\tag{8.5}
$$

where$p , \ q$and r are the three mid-edges adjacent to a vertex v.

This relation can be seen as a discrete version of the Cauchy-Riemann equation on the triangular lattice. Once again, the relations do not determine the observable for general n. Nonetheless, if the family of observables is precompact, then the limit should be holomorphic and it is natural to conjecture the following:

Conjecture 8.11. Let$n \in [ 0 , 2 ]$and$( \Omega , a , b )$be a simply connected domain with two ∈points on the boundary. For$x = x _ { c } ( n )$,

$$
F _ {\delta} (z) \rightarrow \left(\frac {\psi^ {\prime} (z)}{\psi^ {\prime} (b)}\right) ^ {\sigma}\tag{8.6}
$$

where$\begin{array} { r } { \sigma = 1 - \frac { 3 } { 4 \pi } } \end{array}$arccos n 2 ,$F _ { \delta }$is the observable in the discrete domain with spin$\sigma$ and$\psi$= − (− / )is any conformal map from Ω to the upper half-plane sending a to and b to 0.

A conjecture on the scaling limit for the interface from a to b in the$O ( n )$model can also be deduced from these considerations:

Conjecture 8.12. For$n \in [ 0 , 2 )$and$x _ { c } ( n ) = 1 / \sqrt { 2 + \sqrt { 2 - n } } ;$, as the mesh size goes to zero, the law of$O ( n )$∈ [ ) ( ) = / + −interfaces converges to the chordal Schramm-Loewner Evolution with parameter$\kappa = 4 \pi / ( 2 \pi - \operatorname { a r c c o s } ( - n / 2 ) )$.

This conjecture is only proved in the case$n = 1$(Theorem 2.10). The other cases are open. The case$n = 0$=is especially interesting since it corresponds to self-avoiding =walks. Proving the conjecture in this case would pave the way to the computation of many quantities, including the mean-square displacement exponent; see [LSW04b] for further details on this problem.

The phase$x < x _ { c } ( n )$is subcritical and not conformally invariant (the interface con-< ( )verges to the shortest curve between a and b for the Euclidean distance). The critical phase$x \in \mathsf { \Gamma } ( x _ { c } ( n ) , \infty )$should be conformally invariant, and universality is pre-∈ ( ( ) ∞)dicted: the interfaces are expected to converge to the same SLE. The edge-weight $\tilde { x } _ { c } ( n ) \ = \ 1 / \sqrt { 2 - \sqrt { 2 - n } } .$, which appears in Nienhuis’s works [Nie82, Nie84], seems to ( ) = / − −play a specific role in this phase. Interestingly, it is possible to define a parafermionic observable at$\tilde { x } _ { c } ( n )$with a spin$\tilde { \sigma } ( n )$other than$\sigma ( n )$

Proposition 8.13. If$x = \tilde { x } _ { c } ( n )$let F be the parafermionic observable with spin$\tilde { \sigma } =$ $\begin{array} { r } { \tilde { \sigma } ( n ) = - \frac { 1 } { 2 } - \frac { 3 } { 4 \pi } } \end{array}$arccos$( - n / 2 ) ,$( ); then

$$
(p - v) F (p) + (q - v) F (q) + (r - v) F (r) = 0\tag{8.7}
$$

where$p , \ q$and r are the three mid-edges adjacent to a vertex v.

A convergence statement corresponding to Conjecture 8.11 for the observable with spin$\tilde { \sigma }$enables to predict the value of κ for$\tilde { x } _ { c } ( n )$, and thus for every$x > x _ { c } ( n )$thanks to universality.

Conjecture 8.14. For$n \in [ 0 , 2 )$and$x \in ( x _ { c } ( n ) , \infty )$, as the lattice step goes to zero, ∈ [ ) ∈ ( ( ) ∞)the law of O n interfaces converges to the chordal Schramm-Loewner Evolution with parameter$\kappa = 4 \pi / \operatorname { a r c c o s } ( - n / 2 )$

The case$n = 1$corresponds to the subcritical high-temperature expansion of the Ising =model on the hexagonal lattice, which also corresponds to the supercritical Ising model on the triangular lattice via Kramers-Wannier duality. The interfaces should converge to$\mathrm { S L E } ( 6 )$. In the case$n = 0 ;$, the scaling limit should be$\mathrm { S L E } ( 8 )$, which is space-filling. =For both cases, a (slightly diferent) model is known to converge to the corresponding SLE (site percolation on the triangular lattice for$\mathrm { S L E } ( 6 )$, and the perimeter curve of the uniform spanning tree for SLE(8)). Yet, the known proofs do not extend to this context. Proving that the whole critical phase$( x _ { c } ( n ) , \infty )$has the same scaling limit ( ( ) ∞)would be an important example of universality (not on the graph, but on the parameter this time).

The two previous sections presented a program to prove convergence of discrete curves towards the Schramm-Loewner Evolution. It was based on discrete martingales converging to continuous SLE martingales. One can study directly SLE martingales (i.e. with respect to$\sigma ( \gamma [ 0 , t ] ) )$). In particular,$g _ { t } ^ { \prime } ( z ) ^ { \alpha } [ g _ { t } ( z ) - W _ { t } ] ^ { \beta }$is a martingale for SLE(κ) where$\kappa = 4 ( \alpha - \beta ) / [ \beta ( \beta - 1 ) ]$( ) [ ( )− ]. All the limits in these notes are of the previous forms, = ( − )/[ ( − )]see e.g. Proposition 6.7. Therefore, the parafermionic observables are discretizations of very simple SLE martingales.

![](images/page_62_image_0.jpg)

Figure 19: Diferent possible plaquettes with their associated weights.

Question 8.15. Can new preholomorphic observables be found by looking at discretizations of more complicated SLE martingales?

Conversely, in [SS05], the harmonic explorer is constructed in such a way that a natural discretization of a SLE(4) martingale is a martingale of the discrete curve. This fact implied the convergence of the harmonic explorer to${ \mathrm { S L E } } ( 4 )$

Question 8.16. Can this reverse engineering be done for other values of κ in order to find discrete models converging to SLE?

## 8.5 Discrete observables in other models

The study can be generalized to a variety of lattice models, see the work of Cardy, Ikhlef, Riva, Rajabpour [IC09, RC07, RC06]. Unfortunately, the observable is only partially preholomorphic (satisfying only some of the Cauchy-Riemann equations) except for the Ising case. Interestingly, weights for which there exists a half-holomorphic observable which is not degenerate in the scaling limit always correspond to weights for which the famous Yang-Baxter equality holds.

Question 8.17. The approach to two-dimensional integrable models described here is in several aspects similar to the older approaches based on the Yang-Baxter relations [Bax89]. Can one find a direct link between the two approaches?

Let us give the example of the$O ( n )$model on the square lattice. We refer to [IC09] (for a complete study of the following.

It is tempting to extend the definition of$O ( n )$models to the square lattice in order to ( )obtain a family of models containing self-avoiding walks on$\mathbb { Z } ^ { 2 }$and the high-temperature expansion of the Ising model. Nevertheless, dificulties arise when dealing with$O ( n )$ ( )models on non-trivalent graphs. Indeed, the indeterminacy when counting intersecting loops prevents us from defining the model as in the previous subsection.

One can still define a model of loops on$G \subset \mathbb { L }$by distinguishing between local configurations: faces of$G ^ { \star } \subset \mathbb { L } ^ { \star }$⊂are filled with one of the nine plaquettes in Fig. 19. A weight$p _ { v }$⊂is associated to every face$v \in G ^ { \star }$depending on the type of the face (meaning its ∈plaquette). The probability of a configuration is then proportional to$n ^ { \# \log \mathrm { p s } } \prod _ { v \in \mathbb { L } ^ { \star } } p _ { v }$

Remark 8.18. The case$u _ { 1 } = u _ { 2 } = v = x , t = 1$and$w _ { 1 } = w _ { 2 } = n = 0$corresponds to = = = =vertex self-avoiding walks on the square lattice. The case$u _ { 1 } = u _ { 2 } = v = { \sqrt { w } } _ { 1 } = { \sqrt { w } } _ { 2 } = x$ and$n = t = 1$= = = = =corresponds to the high-temperature expansion of the Ising model. The case$t = u _ { 1 } = u _ { 2 } = v = 0 , w _ { 1 } = w _ { 2 } = 1$and$n > 0$corresponds to the FK percolation at = =criticality with$q = n$

A parafermionic observable can also be defined on the medial lattice:

$$
F (z) = \frac {\sum_ {\omega \in \mathcal {E} (a , z)} \mathrm{e} ^ {- i \sigma W _ {\gamma} (a , z)} n ^ {\# \mathrm{loops}} \prod_ {v \in \mathbb {L} ^ {\star}} p _ {v}}{\sum_ {\omega \in \mathcal {E}} n ^ {\# \mathrm{loops}} \prod_ {v \in \mathbb {L} ^ {\star}} p _ {v}}\tag{8.8}
$$

where$\mathcal { E }$corresponds to all the configurations of loops on the graph, and$\mathcal { E } ( a , z )$corre-Esponds to configurations with loops and one interface from a to z.

One can then look for a local relation for$F$around a vertex$v ,$which would be a discrete analogue of the Cauchy-Riemann equation:

$$
F (N) - F (S) = i [ F (E) - F (W) ],\tag{8.9}
$$

An additional geometric degree of freedom can be added: the lattice can be stretched, meaning that each rhombus is not a square anymore, but a rhombus with inside angle α.

As in the case of FK percolations and spin Ising, one can associate configurations by pairs, and try to check (8.9) for each of these pairs, thus leading to a certain number of complex equations. We possess degrees of freedom in the choice of the weights of the model, of the spin σ and of the geometric parameter α. Very generally, one can thus try to solve the linear system and look for solutions. This leads to the following discussion:

Case$v = 0$and$n = 1$: There exists a non-trivial solution for every spin σ, which = =is in bijection with a so-called six-vertex model in the disordered phase. The height function associated with this model should converge to the Gaussian free field. This is an example of a model for which interfaces cannot converge to SLE (in [IC09]; it is conjectured that the limit is described by$\mathrm { S L E } ( 4 , \rho ) )$.

Case$v = 0$and$n \neq 1 :$There exist unique weights associated to an observable with spin = ≠1. This solution is in bijection with the FK percolation at criticality with${ \sqrt { q } } = n + 1$ − = +Nevertheless, physical arguments tend to show that the observable with this spin should have a trivial scaling limit. It would not provide any information on the scaling limit of the model itself; see [IC09] for additional details.

Case$v \neq 0 :$Fix n. There exists a solution for$\begin{array} { r } { \sigma = \frac { 3 \eta } { 2 \pi } - \frac { 1 } { 2 } } \end{array}$where$\eta \in \left[ - \pi , \pi \right]$satisfies $\begin{array} { r } { - \frac { n } { 2 } \ = \ \cos 2 \eta . } \end{array}$= − ∈ [− ]. Note that there are a priori four possible choices for σ. In general the − =following weights can be found:

$$
\left\{ \begin{array}{l c l} t & = & - \sin (2 \phi - 3 \eta / 2) + \sin (5 \eta / 2) - \sin (3 \eta / 2) + \sin (\eta / 2) \\ u _ {1} & = & - 2 \sin (\eta) \cos (3 \eta / 2 - \phi) \\ u _ {2} & = & - 2 \sin (\eta) \sin (\phi) \\ v & = & - 2 \sin (\phi) \cos (3 \eta / 2 - \phi) \\ w _ {1} & = & - 2 \sin (\phi - \eta) \cos (3 \eta / 2 - \phi) \\ w _ {2} & = & 2 \cos (\eta / 2 - \phi) \sin (\phi) \end{array} \right.
$$

where$\phi = ( 1 + \sigma ) \alpha$. We now interpret these results:

When$\eta \in [ 0 , \pi ]$, the scaling limit has been argued to be described by a Coulomb gas ∈ [ ]with a coupling constant$2 \eta / \pi$. In other words, the scaling limit should be the same as the corresponding$O ( n )$/model on the hexagonal lattice. In particular, interfaces should ( )converge to the corresponding Schramm-Loewner Evolution.

When$\eta \in \left[ - \pi , 0 \right]$, the scaling limit curve cannot be described by SLE, and it pro-∈ [− ]vides yet another example of a two-dimensional model for which the scaling limit is not described via SLE.

## References

[AB99] M. Aizenman and A. Burchard, Hölder regularity and dimension bounds for random curves, Duke Math. J. 99 (1999), no. 3, 419–453.

[ABF87] M. Aizenman, D. J. Barsky, and R. Fernández, The phase transition in a general class of Ising-type models is sharp, J. Statist. Phys. 47 (1987), no. 3-4, 343–374.

[Aiz80] M. Aizenman, Translation invariance and instability of phase coexistence in the two-dimensional Ising system, Comm. Math. Phys. 73 (1980), no. 1, 83–94.

[Bax89] R.J. Baxter, Exactly solved models in statistical mechanics, Academic Press Inc. [Harcourt Brace Jovanovich Publishers], London, 1989, Reprint of the 1982 original.

[BDC10] V. Befara and H. Duminil-Copin, The self-dual point of the two-dimensional random-cluster model is critical for$q \geq 1$, to appear in PTRF (2010), 25 pages.

[BDC11], Smirnov’s fermionic observable away from criticality, to appear in Ann. Probab. (2011), 17 pages.

[BdT10] C. Boutillier and B. de Tilière, The critical Z-invariant Ising model via dimers: the periodic case, PTRF 147 (2010), no. 3-4, 379–413.

[BdT11], The critical Z-invariant Ising model via dimers: locality property, Comm. Math. Phys. 301 (2011), no. 2, 473–516.

[Ber72] V.L. Berezinskii, Destruction of long-range order in one-dimensional and two-dimensional systems possessing a continuous symmetry group. ii. quantum systems, Soviet Journal of Experimental and Theoretical Physics 34 (1972), 610 pages.

[BMS05] A.I. Bobenko, C. Mercat, and Y. B. Suris, Linear and nonlinear theories of discrete analytic functions. Integrable structure and isomonodromic Green’s function, J. Reine Angew. Math. 583 (2005), 117–161.

[Bou26] G. Bouligand, Sur le problème de Dirichlet., Ann. Soc. Pol. Math. 4 (1926), 59–112.

[BPZ84a] A. A. Belavin, A. M. Polyakov, and A. B. Zamolodchikov, Infinite conformal symmetry in two-dimensional quantum field theory, Nuclear Phys. B 241 (1984), no. 2, 333–380.

[BPZ84b], Infinite conformal symmetry of critical fluctuations in two dimensions, J. Statist. Phys. 34 (1984), no. 5-6, 763–774.

[BS08]A. I. Bobenko and Y. B. Suris, Discrete diferential geometry, Graduate Studies in Mathematics, vol. 98, American Mathematical Society, Providence, RI, 2008, Integrable structure.

[BSST40] R. L. Brooks, C. A. B. Smith, A. H. Stone, and W. T. Tutte, The dissection of rectangles into squares, Duke Math. J. 7 (1940), 312–340.

[Car92] J. L. Cardy, Critical percolation in finite geometries, J. Phys. A 25 (1992), no. 4, L201–L206.

[CFL28] R. Courant, K. Friedrichs, and H. Lewy, Über die partiellen Diferenzengleichungen der mathematischen Physik, Math. Ann. 100 (1928), no. 1, 32–74.

[Cim10] D. Cimasoni, A generalized Kac-Ward formula, to appear J. Stat. Mech. Theory Exp. (2010), 23 pages.

[CS08] D. Chelkak and S. Smirnov, Discrete complex analysis on isoradial graphs, to appear in Adv. in Math. (2008), 35 pages.

[CS09]Universality in the 2D Ising model and conformal invariance of fermionic observables, to appear in Inv. Math. (2009), 52 pages.

[CV10] L. Coquille and Y. Velenik, A finite-volume version of Aizenman-Higuchi theorem for the 2D Ising model, to appear in PTRF (2010), 16 pages.

[DCHN10] H. Duminil-Copin, C. Hongler, and P. Nolin, Connection probabilities and RSW-type bounds for the two-dimensional FK Ising model, to appear in Communications in Pure and Applied Mathematics (2010), 33 pages.

[DCS10] H. Duminil-Copin and S. Smirnov, The connective constant of the honeycomb lattice equals${ \sqrt { 2 + { \sqrt { 2 } } } } ,$, to appear in Ann. of Math. (2011), 12 pages.

[DMNS81] D. Domany, D. Mukamel, B. Nienhuis, and A. Schwimmer, Duality relations and equivalences for models with O(N) and cubic symmetry, Nuclear Physics B 190 (1981), no. 2, 279–287.

[Dob72] R. L. Dobrushin, Gibbs state, describing the coexistence of phases in the three-dimensional ising model., PTRF 17 (1972), 582–60.

[Duf56] R. J. Dufin, Basic properties of discrete analytic functions, Duke Math. J. 23 (1956), 335–363.

[Duf68], Potential theory on a rhombic lattice, J. Combinatorial Theory 5 (1968), 258–272.

[DZM 99] N.P. Dolbilin, Y.M. Zinovév, A. S. Mishchenko, M.A. Shtańko, and M.I. Shtogrin, The two-dimensional Ising model and the Kac-Ward determinant, Izv. Ross. Akad. Nauk Ser. Mat. 63 (1999), no. 4, 79–100.

[ES88]R. G. Edwards and A. D. Sokal, Generalization of the Fortuin-Kasteleyn-Swendsen-Wang representation and Monte Carlo algorithm, Phys. Rev. D (3) 38 (1988), no. 6, 2009–2012.

[Fer44] J. Ferrand, Fonctions préharmoniques et fonctions préholomorphes., Bull. Sci. Math. (2) 68 (1944), 152–180.

[Fis66] M. Fisher, On the dimer solution of planar Ising models, Journal of Mathematical Physics 7 (1966), no. 10, 1776–1781.

[Fis98], Renormalization group theory: its basis and formulation in statistical physics, Rev. Modern Phys. 70 (1998), no. 2, 653–681.

[FK72]C. M. Fortuin and P. W. Kasteleyn, On the random-cluster model. I. Introduction and relation to other models, Physica 57 (1972), 536–564.

[FKG71] C. M. Fortuin, P. W. Kasteleyn, and J. Ginibre, Correlation inequalities on some partially ordered sets, Comm. Math. Phys. 22 (1971), 89–103.

[Gri06] G.R. Grimmett, The random-cluster model, Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 333, Springer-Verlag, Berlin, 2006.

[Hei28] W. Heisenberg, Zür theorie des ferromagnetismus, Zeitschrift für Physik A Hadrons and Nuclei 49 (1928), no. 9, 619–636.

[Hig81]Y. Higuchi, On the absence of non-translation invariant Gibbs states for the two-dimensional Ising model, Random fields, Vol. I, II (Esztergom, 1979), Colloq. Math. Soc. János Bolyai, vol. 27, North-Holland, Amsterdam, 1981, pp. 517–534.

[HK11] C. Hongler and K. Kytolä, Dipolar SLE in the Ising model with plus/minus/free boundary conditions, 2011, 82 pages.

[HS93]Z.-X. He and O. Schramm, Fixed points, Koebe uniformization and circle packings, Ann. of Math. (2) 137 (1993), no. 2, 369–406.

[HS10] C. Hongler and S. Smirnov, The energy density in the planar ising model, to appear in Acta Math. (2012).

[IC09]Y. Ikhlef and J.L. Cardy, Discretely holomorphic parafermions and integrable loop models, J. Phys. A 42 (2009), no. 10, 102001, 11 pages.

[Isa41] R.P. Isaacs, A finite diference function theory, Univ. Nac. Tucumán. Revista A. 2 (1941), 177–201.

[Isa52], Monodifric functions. Construction and applications of conformal maps, Proceedings of a symposium (Washington, D. C.), National Bureau of Standards, Appl. Math. Ser., No. 18, U. S. Government Printing Ofice, 1952, pp. 257–266.

[Isi25] E. Ising, Beitrag zur theorie des ferromagnetismus., Z. Phys. 31 (1925), 253–258.

[ISZ88] C. Itzykson, H. Saleur, and J.-B. Zuber (eds.), Conformal invariance and applications to statistical mechanics, World Scientific Publishing Co. Inc., Teaneck, NJ, 1988.

[Kad66] L. P. Kadanof, Scaling laws for Ising model near t , Physics 2 (1966), no. 263.

[Kas61] P. W. Kasteleyn, The statistics of dimers on a lattice., PhysicA 27 (1961), 1209–1225.

[Ken00] R. Kenyon, Conformal invariance of domino tiling, Ann. Probab. 28 (2000), no. 2, 759–795.

[Ken02], The Laplacian and Dirac operators on critical planar graphs, Invent. Math. 150 (2002), no. 2, 409–439.

[Kir47] G. Kirchhof, über die auflösung der gleichungen, auf welche man bei der untersuchung der linearen vertheilung galvanischer ströme geführt wird., Annalen der Physik und Chemie 148 (1847), no. 12, 497–508.

[KO50] B. Kaufman and L. Onsager, Crystal statistics. IV. long-range order in a binary crystal, 1950.

[KS05] R. Kenyon and J.-M. Schlenker, Rhombic embeddings of planar quad-graphs, Trans. Amer. Math. Soc. 357 (2005), no. 9, 3443–3458 (electronic).

[KS10] A. Kemppainen and S. Smirnov, Random curves, scaling limits and loewner evolutions, in preparation (2010).

[KT73]J.M. Kosterlitz and D.J. Thouless, Ordering, metastability and phase transitions in two-dimensional systems, Journal of Physics C: Solid State Physics 6 (1973), 1181.

[KW41a] H.A. Kramers and G.H. Wannier, Statistics of the two-dimensional ferromagnet, I, Phys. Rev. 60 (1941), 252–262.

[KW41b], Statistics of the two-dimensional ferromagnet, II, Phys. Rev. 60 (1941), 263–276.

[KW52] M. Kac and J. C. Ward, A combinatorial solution of the two-dimensional ising model, Phys. Rev 88 (1952), 1332–1337.

[Law91] G. F. Lawler, Intersections of random walks, Probability and its Applications, Birkhäuser Boston Inc., Boston, MA, 1991.

[Len20] W. Lenz, Beitrag zum verständnis der magnetischen eigenschaften in festen körpern., Phys. Zeitschr. 21 (1920), 613–615.

[LF55] J. Lelong-Ferrand, Représentation conforme et transformations à intégrale de Dirichlet bornée, Gauthier-Villars, Paris, 1955.

[Lie67]E.H. Lieb, Exact solution of the problem of the entropy of two-dimensional ice, Physical Review Letters 18 (1967), no. 17, 692–694.

[Lov04] L. Lovász, Discrete analytic functions: an exposition, Surveys in diferential geometry. Vol. IX, Surv. Difer. Geom., IX, Int. Press, Somerville, MA, 2004, pp. 241–273.

[LPSA94] R. Langlands, P. Pouliot, and Y. Saint-Aubin, Conformal invariance in twodimensional percolation, Bull. Amer. Math. Soc. (N.S.) 30 (1994), no. 1, 1–61.

[LS10] E. Lubetzky and A. Sly, Critical Ising on the square lattice mixes in polynomial time, 2010, 26 pages.

[LSW04a] G. Lawler, O. Schramm, and W. Werner, Conformal invariance of planar loop-erased random walks and uniform spanning trees, Ann. Probab. 32 (2004), no. 1B, 939–995.

[LSW04b] G. F. Lawler, O. Schramm, and W. Werner, On the scaling limit of planar self-avoiding walk, Fractal geometry and applications: a jubilee of Benoît Mandelbrot, Part 2, Proc. Sympos. Pure Math., vol. 72, Amer. Math. Soc., Providence, RI, 2004, pp. 339–364.

[Lus26] L. Lusternik, über einege Anwendungen der direkten Methoden in Variationsrechnung., Recueil de la Société Mathématique de Moscou, 1926, pp. 173–201.

[Mer01] C. Mercat, Discrete Riemann surfaces and the Ising model, Comm. Math. Phys. 218 (2001), no. 1, 177–216.

[Mes06] R.J. Messikh, Surface tension near criticality of the 2d-Ising model., arXiv:math/0610636 (2006), 24 pages.

[MW40] W. H. McCrea and F. J. W. Whipple, Random paths in two and three dimensions, Proc. Roy. Soc. Edinburgh 60 (1940), 281–298.

[MW73] B.M. McCoy and T.T. Wu, The two-dimensional Ising model, Harvard University Press, Cambridge, MA, 1973.

[Nie82] B. Nienhuis, Exact critical point and critical exponents of o n models in two dimensions., Phys. Rev. Lett. 49 (1982), 1062–1065.

[Nie84], Coulomb gas description of 2D critical behaviour, J. Statist. Phys. 34 (1984), 731–761.

[Ons44] L. Onsager, Crystal statistics. i. a two-dimensional model with an orderdisorder transition., Phys. Rev. (2) 65 (1944), 117–149.

[Pal07] J. Palmer, Planar Ising correlations, Progress in Mathematical Physics, vol. 49, Birkhäuser Boston Inc., Boston, MA, 2007.

[Pei36] R. Peierls, On Ising’s model of ferromagnetism., Math. Proc. Camb. Phil. Soc. 32 (1936), 477–481.

[PP66]A.Z. Patashinskii and V.L. Pokrovskii, Behavior of ordered systems near the transition point, Soviet Physics JETP 23 (1966), no. 292, 292.

[PW23] H.B. Phillips and N. Wiener, Nets and the Dirichlet problem., Math. J. of Math. 2 (1923), 105–124.

[RC06] V. Riva and J.L. Cardy, Holomorphic parafermions in the Potts model and stochastic Loewner evolution, J. Stat. Mech. Theory Exp. (2006), no. 12, P12001, 19 pp. (electronic).

[RC07] M. A. Rajabpour and J.L. Cardy, Discretely holomorphic parafermions in lattice Z models, J. Phys. A 40 (2007), no. 49, 14703–14713.

[RS87] B. Rodin and D. Sullivan, The convergence of circle packings to the Riemann mapping, J. Diferential Geom. 26 (1987), no. 2, 349–360.

[Sch00] O. Schramm, Scaling limits of loop-erased random walks and uniform spanning trees, Israel J. Math. 118 (2000), 221–288.

[She60] S. Sherman, Combinatorial aspects of the Ising model for ferromagnetism. I. A conjecture of Feynman on paths and graphs, J. Mathematical Phys. 1 (1960), 202–217.

[Smi01] S. Smirnov, Critical percolation in the plane: conformal invariance, Cardy’s formula, scaling limits, C. R. Acad. Sci. Paris Sér. I Math. 333 (2001), no. 3, 239–244.

[Smi06], Towards conformal invariance of 2D lattice models, International Congress of Mathematicians. Vol. II, Eur. Math. Soc., Zürich, 2006, pp. 1421–1451.

[Smi10a]Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model, Ann. of Math. (2) 172 (2010), no. 2, 1435–1467.

[SS05] O. Schramm and S. Shefield, Harmonic explorer and its convergence to SLE , Ann. Probab. 33 (2005), no. 6, 2127–2148.

[Ste05] K. Stephenson, Introduction to circle packing, Cambridge University Press, Cambridge, 2005, The theory of discrete analytic functions.

[SW10a] S. Shefield and W. Werner, Conformal loop ensembles: Construction via loop-soups, Arxiv preprint arXiv:1006.2373 (2010), 21 pages.

[SW10b], Conformal loop ensembles: The Markovian characterization, Arxiv preprint arXiv:1006.2374 (2010), 60 pages.

[Thu86] W. P. Thurston, Zippers and univalent functions, The Bieberbach conjecture (West Lafayette, Ind., 1985), Math. Surveys Monogr., vol. 21, Amer. Math. Soc., Providence, RI, 1986, pp. 185–197.

[Vdo65] N. V. Vdovichenko, A calculation of the partition function for a plane dipole lattice, Soviet Physics JETP 20 (1965), 477–488.

[Wer09] W. Werner, Percolation et modèle d’Ising, Cours Spécialisés [Specialized Courses], vol. 16, Société Mathématique de France, Paris, 2009.

[Yan52] C.N. Yang, The spontaneous magnetization of a two-dimensional Ising model, Phys. Rev. (2) 85 (1952), 808–816.