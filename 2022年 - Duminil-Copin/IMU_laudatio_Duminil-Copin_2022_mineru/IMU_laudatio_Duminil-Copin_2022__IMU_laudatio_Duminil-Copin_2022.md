# The work of Hugo Duminil-Copin

Martin Hairer

## Abstract

The past decade has seen tremendous progress in our understanding of the behaviour of many probabilistic models at or near their “critical point”. On the 5th of July 2022, Hugo Duminil-Copin was awarded the Fields medal for the crucial role he played in many of these developments. In this short review article, we will try to put his work into context and present a small selection of his results.

Mathematics Subject Classification 2020 Primary 82B20; Secondary 82B26, 82B43

Keywords Ising model, Potts model, percolation

## 1. Introduction

Hugo Duminil-Copin was awarded the Fields medal in Helsinki during the opening ceremony of the 2022 virtual ICM. In this short note, I will try to put his work into context and to give the reader a glimpse of why the questions it addresses are not only very interesting from a purely mathematical perspective, but also contribute to further our understanding of nature at a fundamental level. I should start first of all with a disclaimer. Hugo Duminil-Copin is an astounding problem solver and, while his interest falls squarely into the general area of probability theory and in particular the type of probabilistic problems that arise when studying microscopic models for statistical mechanics, I will not be able to do justice to the breadth of his contributions. Furthermore, my own area of expertise is somewhat tangential to that of Duminil-Copin, so this note should be taken as the point of view of an interested outsider. In particular, any misrepresentations of his results and / or techniques will be entirely due to my own ignorance.

In its broadest form, classical statistical mechanics can be thought of as the study of the global behaviour of “large” systems (of “size”$N \gg 1 )$) that are comprised of many identical “small” subsystems interacting with each other. One typically indexes the subsystems by a discrete set$\Lambda _ { N }$with lim$_ { \cdot N  \infty } | \Lambda _ { N } | = \infty$and one is interested in quantities that are stable as$N \to \infty$. In many cases of interest, one has$\Lambda _ { N } \subset \Lambda$for Λ a discrete subset of Euclidean space (typically a regular lattice) and its elements are interpreted as a physical location of the corresponding subsystem; the interaction between subsystems may then depend on their locations. (In most models they actually depend only on their relative positions, a notion tha generalises very well to locations taking values in more general symmetric spaces.)

Let us write � for the state space of one single such subsystem, so that the state space for the full system is${ S } _ { N } \stackrel { \mathrm { d e f } } { = } { S } ^ { \Lambda _ { N } }$. In equilibrium statistical mechanics, we furthermore assume that � is equipped with a “reference” probability measure$\mu$(think of$\mu$as being normalised counting measure if � is a finite set, normalised volume measure if it is a compact manifold, etc) and that our system is described by an energyfunction${ H ^ { ( N ) } } : S _ { N } \to \mathbf { R }$, which is typically comprised of a contribution for each subsystem, as well as additional interaction terms. In full generality, one would have something like

$$
H ^ {(N)} (\sigma) = \sum_ {A \subset \mathcal {S} _ {N}} H _ {A} (\sigma_ {A}),\tag{1.1}
$$

where$\sigma _ { A }$denotes the restriction of$\sigma \in S ^ { \Lambda _ { N } }$to$S ^ { A }$and the function$H _ { A }$typically only depends on the “shape” of the subset �, so satisfies natural invariance properties under translations and possibly reflections and / or discrete rotations. In many classical models, the only non-vanishing terms in (1.1) are those with$| A | \le 2$

Given such an energy function, we obtain a probability measure$\mu _ { \beta , N }$on$S _ { N }$by setting

$$
\mu_ {\beta , N} (d \sigma) = Z _ {\beta , N} ^ {- 1} \exp \bigl (- \beta H ^ {(N)} (\sigma) \bigr) \prod_ {u \in \Lambda_ {N}} \mu (d \sigma_ {u}),\tag{1.2}
$$

where$Z _ { \beta , N }$is chosen in such a way that$\mu _ { \beta , N } ( S _ { N } ) = 1$. Physically, the parameter$\beta > 0$ appearing in this expression is the inverse of the temperature of the system. To a large extent, (equilibrium) statistical mechanics is the study of$\mu _ { \beta , N }$as$N \to \infty$with a particular emphasis on the behaviour under$\mu _ { \beta , N }$of observables that take a “macroscopic” (of the order of the size of the domain$\Lambda _ { N } )$) or “mesoscopic” (tending to infinity as$N \to \infty$but much smaller than$\vert \Lambda _ { N } \vert )$number of components of$\sigma$into account.

## 1.1. Bernoulli percolation

The simplest such example is that of$S = \{ - 1 , 1 \} , H _ { N } = 0$, and$\begin{array} { r } { \mu ( \{ - 1 \} ) = \mu ( \{ 1 \} ) = \frac { 1 } { 2 } } \end{array}$ Regarding the index set$\Lambda _ { N }$, we consider the case of the even elements of a large box in${ \bf Z } ^ { 2 }$ namely$\Lambda _ { N } = \{ u \in \{ - N , \ldots , N \} ^ { 2 } : u _ { 1 } + u _ { 2 } \mathrm { e v e n } \}$. (The reason why we make this strange choice rather than simply taking all elements of$\{ - N , \ldots , N \} ^ { 2 }$will soon become clear.)

One of the simplest kind of “global” observables for this system is given by the following kind of linear statistics. Given a smooth function$\phi \colon [ - 1 , 1 ] ^ { 2 }  \mathbf { R }$, we define $I _ { \phi } ^ { N } : S _ { N } \to \mathbf { R }$by

$$
I _ {\phi} ^ {N} (\sigma) = N ^ {- \alpha} \sum_ {u \in \Lambda_ {N}} \sigma_ {u} \phi (u / N).\tag{1.3}
$$

Note that this is exhaustive: for any fixed �, if we know$I _ { \phi } ^ { N } ( \sigma )$for every smooth function$\phi ,$, then we can in principle recover the argument$\sigma$itself. A version of the central limit theorem then immediately yields the following result:

Theorem 1.1. Setting$\alpha = 1$, the joint distribution of$I _ { \phi } ^ { N } ( \sigma )$for anyfinite collection oftes functions � as above converges as$N \to \infty$to the law ofa collection ofjointly centred Gaussian random variables$I _ { \phi }$such that

$$
\mathbf {E} I _ {\phi} I _ {\psi} = \frac {1}{2} \int_ {[ - 1, 1 ] ^ {2}} \phi (x) \psi (x) d x.
$$

(The factor$\frac { 1 } { 2 }$appearing here comes from the fact that the local density of$\Lambda _ { N }$in$\mathbf { Z } ^ { 2 } \mathrm { i s } \ \frac { 1 } { 2 } . )$

A much more interesting kind of global observables is given by the connectivity properties of$\sigma _ { \mathrm { { : } } }$, which were first studied by Broadbent and Hammersley [12]. These are however much harder to analyse and, even though the model just described appears at first sight to be somewhat trivial, most of its results already lead us squarely into 21st century mathematics. In order to describe what we mean by “connectivity” in this context, instead of interpreting elements$u \in \Lambda _ { N }$as points in${ \bf Z } ^ { 2 }$, we interpret them as nearest-neighbour edges of a suitable sublattice of${ \bf Z } ^ { 2 }$by associating to � the unique edge$e _ { u }$of$\mathbf { Z } _ { \mathrm { e v e n } } \times \mathbf { Z } _ { \mathrm { o d d } }$ with midpoint �. We will also write$e _ { u } ^ { * }$for the edge of$\mathbf { Z } _ { \mathrm { o d d } } \times \mathbf { Z } _ { \mathrm { e v e n } }$with midpoint �. In other words, we set

$$
e _ {u} = \left\{\begin{array}{c l}(u _ {\downarrow}, u _ {\uparrow})&\text {if u_{1} is even,}\\(u _ {\leftarrow}, u _ {\rightarrow})&\text {if u_{1} is odd,}\end{array}\right. \qquad e _ {u} ^ {*} = \left\{\begin{array}{c l}(u _ {\leftarrow}, u _ {\rightarrow})&\text {if u_{1} is even,}\\(u _ {\downarrow}, u _ {\uparrow})&\text {if u_{1} is odd.}\end{array}\right.
$$

Here, given$u = ( u _ { 1 } , u _ { 2 } ) \in \mathbf { Z } ^ { 2 }$, we write$u _ {  } = ( u _ { 1 } - 1 , u _ { 2 } )$, etc. The endpoints of these edges do belong to the stated sublattices of${ \bf Z } ^ { 2 }$since$u _ { 1 } + u _ { 2 }$is even, so either both$u _ { 1 }$and$u _ { 2 }$are even or both are odd.

Given a configuration$\sigma \in S _ { N }$, we interpret edges$e _ { u }$with$\sigma _ { u } = - 1$as “open” and draw them in black, while the remaining edges are considered “closed” and are drawn in ligh grey. This yields a picture like shown on the left in Figure 1. We can then ask for example what is the probability$p _ { N }$that it is possible to go from the left boundary of the light gray graph to the right boundary (the "boundary" here consists of the ends of the dangling edges) while only traversing black edges. It turns out that this probability does take non-trivial values even for large values for �. As a matter of fact, it is independent of � as the following classical result (see for example [36, Lem. 11.21]) shows.

![](images/page_3_image_0.jpg)

![](images/page_3_image_1.jpg)

Figure 1

On the left, we draw a typical percolation configuration for$N = 1 1$. On the right, the same configuration is drawn together with its dual configuration in light blue

Theorem 1.2. One has$\begin{array} { r } { p _ { N } = \frac { 1 } { 2 } f o r e \nu e r y N . } \end{array}$

Proof. The trick is to observe that given a configuration$\sigma \in S _ { N }$, if we draw the dual config uration$\sigma ^ { * } \in S _ { N }$defined by$\sigma _ { u } ^ { * } = - \sigma _ { u }$by colouring (in blue, say) the edges$e _ { u } ^ { * }$with$\sigma _ { u } ^ { * } = - 1$ then we obtain a drawing with the property that blue edges never intersect black edges. As a consequence, it is possible to cross the square from left to right by traversing only black edges if and only if it is not possible to cross it from top to bottom by traversing only blue edges. (See Figure 1.) On the other hand, the law of the collection of blue edges is the same as that of the collection of black edges, only rotated by$9 0 ^ { \circ }$, so that we must have$p _ { N } = 1 - p _ { N }$as claimed.■

Remark 1.3. If, instead of choosing edges to be open with probability$\frac { 1 } { 2 }$, we choose them to be open with some probability$p ,$, then we have$p _ { N } \to 1$for$\begin{array} { r } { p > \frac { 1 } { 2 } } \end{array}$and$p _ { N } \to 0$for$\begin{array} { r } { p < { \frac { 1 } { 2 } } } \end{array}$ This is an example of phase transition: an abrupt change in the behaviour of some global observables as a parameter of the model is varied continuously. In this specific example, we were able to determine the critical value$\begin{array} { r } { p _ { c } = \frac { 1 } { 2 } } \end{array}$explicitly by exploiting an exact duality.

It is similarly possible to obtain a large collection of interesting global observables by taking a shape$\mathcal { U } \subset [ - 1 , 1 ] ^ { 2 }$difeomorphic to a square and considering the analogous event $A _ { \mathcal { U } } ^ { ( N ) } \subset S _ { N }$asking whether it is possible to connect the left and right edges of �U (withou ever leaving �U) by a path following only open edges of a given configuration$\sigma \in S _ { N }$ Again, the knowledge of these events is an exhaustive statistics for any given fixed value of �. It is furthermore known that for any finite number of such shapes$\{ \mathcal { U } _ { i } \} _ { i \in I }$(for � some finite index set) the random variables$\{ [ A _ { \mathcal { U } _ { i } } ^ { ( N ) } ] \} _ { i \in I }$converge in law to a non-degenerate limit $\{ [ A { _ { { \mathscr U } } } _ { i } ] \} _ { i \in I }$as$N \to \infty$[56]. (Here, we write [�] for the indicator function of an event �.) An amazing fact is that this scaling limit is conformally invariant: if$\phi \colon D \to D ^ { \prime }$is a conformal map between two smooth simply connected domains �,$D ^ { \prime } \subset \mathbf { C }$such that$[ - 1 , 1 ] ^ { 2 } \subset D$and such that$\mathcal { V } _ { i } \overset { \mathrm { d e f } } { = } \phi ( \mathcal { U } _ { i } ) \subset [ - 1 , 1 ] ^ { 2 }$, then the joint law of the random variables$\{ [ A \gamma _ { i } ] \} _ { i \in I }$is the same as that of$\{ [ A _ { { \mathcal { U } } _ { i } } ] \} _ { i \in I }$

This conformal invariance turns out to be a crucial feature of the scaling limits of many equilibrium statistical mechanics models in two dimensions. It provides a link to conformal field theory which, at a purely mathematical level, can be thought of as the study of irreducible representations of the Virasoro algebra. In particular, it strongly suggests that the possible large-scale behaviours one can see for two-dimensional equilibrium models come in a one-parameter family of “universality classes” parametrised by the central charge of the corresponding conformal field theory. (In the case of percolation, it turns out that this central charge is given by$c = 0 . \mathrm { ~ , ~ }$)

## 1.2. The Ising model

The next-“simplest” model of statistical mechanics falling into the category of equilibrium models described above is the Ising model . (See also the review article [16] in these proceedings which contains a more detailed account of the various developments spawned by this model.) In this case, the index set is given by$\Lambda _ { N } = \{ - N , \ldots , N \} ^ { d }$for some$d \geq 1$, the reference measure$\mu$and local state space � are as above, but this time one has$H _ { A } = 0$unless$A = \{ u , v \}$with$u , v \in \mathbf { Z } ^ { d }$such that$\left| u - v \right| = 1$, in which case one sets $H _ { A } ( \sigma ) = - \sigma _ { u } \sigma _ { v }$. This time, the model has a non-trivial dependence on the parameter$\beta$ appearing in (1.2), which plays a role somewhat similar to the parameter$p$that appeared in Remark 1.3.

At a very qualitative level, the situation is somewhat similar to what happened in the case for percolation: in every dimension$d \ge 2$there exists a critical (dimension-dependent) value$\beta _ { c }$which delineates two diferent regimes. At “high temperature”, namely for$\beta < \beta _ { c }$ the spontaneous magnetisation, namely the random quantity$\begin{array} { r } { N ^ { - d } \sum _ { i \in \Lambda _ { N } } \sigma _ { i } } \end{array}$, converges to 0 in probability as$N \to \infty$. For$\beta > \beta _ { c }$on the other hand, it converges in probability to a limiting random variable that can take exactly two possible values$\pm h _ { \beta } \neq 0$with equal probabilities. The actual value of$\beta _ { c }$is only known in dimension 2 where it equals$\beta _ { c } = \log \sqrt { 1 + \sqrt { 2 } }$[50]. (There is no phase transition at all in dimension 1 and the spontaneous magnetisation always vanishes, so in some sense$\beta _ { c } = + \infty \mathrm { t h e r e . } )$0

It is again possible to ask the same questions as in the case of Bernoulli percolation. This time however even the analogue of Theorem 1.1, which was an essentially trivial consequence of the central limit theorem (or at least a version thereof), is already highly non-trivial. It was shown in a recent series of works [13,14] that if one chooses$\beta = \beta _ { c }$and $\alpha = 1 5 / 8$in the expression (1.3) in dimension$d = 2$, then it converges in law to non-trivial limiting random variables, jointly for any fixed number of test functions. This time however the limiting distributions are not Gaussian (they actually exhibit an even faster decaying tail behaviour). Note that the exponent � is closely related to the behaviour of$\mathbf { E } _ { c } \sigma _ { u } \sigma _ { v }$(where $\mathbf { E } _ { c }$denotes the expectation under the Gibbs measure (1.2) for the critical value of the inverse temperature$\beta )$since, assuming that${ \bf E } _ { c } \sigma _ { u } \sigma _ { v } \approx | u - v | ^ { - \delta }$, one finds that

$$
\mathbf {E} _ {c} \left(I _ {\phi} ^ {N} (\sigma)\right) ^ {2} = N ^ {- 2 \alpha} \sum_ {u, v} \phi (u / N) \phi (v / N) \mathbf {E} _ {c} \sigma_ {u} \sigma_ {v} \lesssim N ^ {- 2 \alpha} \sum_ {u, v} | u - v | ^ {- \delta} \approx N ^ {2 d - (\delta \wedge d) - 2 \alpha},
$$

so that one expects the relation$\alpha = d - ( \delta \wedge d ) / 2$, which (correctly) leads to the prediction $\begin{array} { r } { \delta = \frac { 1 } { 4 } } \end{array}$. This and a number of other properties of the Ising model at criticality allow to associat it to the conformal field theory with central charge$\begin{array} { r } { c = \frac { 1 } { 2 } } \end{array}$

The picture in higher dimensions is much less clear however. For$d \ge 5$, it was shown in [1, 2, 29] that the correct scaling exponent to use in (1.3) at$\beta = \beta _ { c }$is$\begin{array} { r } { \alpha = 1 + \frac { d } { 2 } } \end{array}$and that the limit is a Gaussian Free Field, namely the Gaussian random distribution with correlation function given by the Green’s function of the Laplacian (with Neuman boundary conditions on the square). In dimension$d = 3$, virtually nothing is known rigorously about the critical Ising model, not even the value of its scaling exponents, although much progress has been made at a non-rigorous level with the development of the “conformal bootstrap” [23, 24]. Regarding the case$d = 4 .$, it was somewhat unclear until very recently whether the Ising model at criticality should be “trivial” (i.e. described by Gaussian distributions) or not. This was eventually settled by Aizenman and Duminil-Copin in the work [3] where they show that any subsequential limit for expressions of the form (1.3) as$N \to \infty ( \mathrm { a n d } \beta \to \beta _ { c } )$must necessarily be Gaussian.

In fact, some of the results just mentioned are shown for the “lattice$\Phi ^ { 4 }$model” which is the equilibrium model with$S = \mathbf { R }$, as well as

$$
H _ {\{u \}} (\sigma) = V (\sigma_ {u}) \stackrel {\mathrm{def}} {=} \sigma_ {u} ^ {4} - \alpha \sigma_ {u} ^ {2}, \qquad H _ {\{u, v \}} (\sigma) = \frac {1}{2} (\sigma_ {u} - \sigma_ {v}) ^ {2},
$$

again provided that � and � are nearest-neighbours, and with � an additional parameter. While this appears to be very diferent from the Ising model at first sight, we can see that it is actually a generalisation of it: if the constant � is large, then the potential � has two very deep wells with minima located at$\pm \sqrt { \alpha }$, so its efect is to impose that$\sigma _ { u } \approx \pm \sqrt { \alpha }$with high probability. The main contribution then comes from the cross-term of the square in the two-body term which is the same as for the Ising model. These kind of considerations lead one to expect that, since these models exhibit long-range correlations at the critical temperature (in the sense that the correlation$\mathbf { E } \sigma _ { x } \sigma _ { y }$decays slowly in$\left| x - y \right|$as already pointed out earlier) which should furthermore lead to some form of self-averaging, the Ising model and the$\Phi ^ { 4 }$model exhibit the same behaviour at criticality.

## 1.3. A general picture

The general picture that should by now be emerging from our discussion can be summarised as follows:

(1) Many of the simplest local equilibrium systems do exhibit a phase transition, namely there exists a critical value$\beta _ { c }$at which the qualitative large scale behaviour of the system changes abruptly. In general, a system may depend on additional parameters in which case one may see a more complicated phase diagram with several regions in parameter space where the global behaviour of the system displays qualitatively diferent behaviour. In any case, the “high temperature / small � phase” is expected to behave in such a way that what happens in well separated regions of space is very close to independent.

(2) In dimension 2, many of these systems appear to exhibit a form of conformal invariance at criticality, even though no rotation symmetry is built a priori into their description. When this happens, the link to 2� conformal field theories (and the associated probabilistic objects like SLE [55], QLE [45], etc) provides a hugely powerful machinery to predict – and in a number of cases also rigorously prove – their behaviour.

(3) The universe of local statistical mechanics models can be subdivided into broad classes of models that exhibit a shared large-scale behaviour at criticality. These are called “universality classes” and, in the 2� equilibrium case, they are expected to come in families parametrised by a real parameter, the central charge. (For certain values of the central charge, one expects to have several “subclasses”, but we will not discuss this kind of subtlety here.)

(4) Although one still expects conformal invariance at criticality in higher dimensions, this is a much smaller symmetry there and therefore appears to provide somewhat less insight1. One also expects the situation there to be more rigid than in two dimensions, with fewer universality classes. (Possibly only a discrete family.)

(5) Models that have “obvious” variants in every dimension typically have a critical dimension above which their behaviour at criticality is “trivial” in the sense tha it exhibits Gaussian behaviour. (Typically with correlation function given by the Green’s function of the Laplacian.) In the case of the Ising universality class, this critical dimension is 4, while in the case of Bernoulli percolation it is 6.

One important branch of modern probability theory aims to put this general picture onto rigorous mathematical footing. The remainder of this article is devoted to a short overview of some of Hugo Duminil-Copin’s many contributions to this vast programme. This represents of course a mere sliver of his work and completely ignores very substantial chunks of it.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1See however the recent breakthrough made in the approximation of the critical exponents o the 3� Ising model using the “conformal bootstrap” [23, 24] already mentioned above.</span></small>

![](images/page_7_image_0.jpg)

Figure 2

Typical Ising configurations for$\beta < \beta _ { c }$(left) and$\beta > \beta _ { c }$(right).

By presenting not just a long laundry list of results that he proved and conjectures that he settled but instead an overview of the strategy of proof for a few select results, I hope to be able to convey one of the features of Duminil-Copin’s body of work, namely that he has a knack for finding just the right way of looking at a problem that had hitherto been overlooked. In many cases, this only provides small cracks in the problem’s armour that still require tremendous technical skill to be wedged open, but in some cases it results in surprisingly simple but ingenious proofs. Either way, I am very much looking forward to learning more from Duminil-Copin’s insights for many years to come.

## 2. (Dis)continuity of phase transitions

One very natural question in this area is whether one can take the limit$N \to \infty$in (1.2). At this stage, we note that the definition of$H ^ { ( N ) }$given in (1.1) is not necessarily the most natural one since it restricts the sum over those clusters � that are constrained to entirely lie in$S _ { N }$. Another possibility that appears just as natural would be to restrict the sum over clusters that merely intersect$S _ { N }$, but to specify some fixed “boundary condition”$\bar { \boldsymbol { \sigma } } \in S ^ { \Lambda }$ that is used to compute the values of the$H _ { A }$with � intersecting both$\Lambda _ { N }$and$\mathbf { \Lambda } \Lambda \setminus \Lambda _ { N }$in the sense that we interpret$\sigma _ { A }$in (1.1) as$\sigma _ { A , x } = \sigma _ { x }$for$x \in A \cap \Lambda _ { N }$and$\sigma _ { A , x } = \bar { \sigma } _ { x }$otherwise.

In many examples of interest (including the case of the Ising model, but not the case of percolation), the measure$\begin{array} { r } { \mu _ { \beta } = \operatorname* { l i m } _ { N \to \infty } \mu _ { \beta , N } } \end{array}$is well-defined (i.e. independent of the choice of boundary condition) for$\beta < \beta _ { c }$while one can obtain several distinct limits in the case$\beta > \beta _ { c }$. Figure 2 shows typical samples drawn from$\mu _ { \beta }$for the Ising model with $\bar { \sigma } \equiv 1$. In the case$\beta > \beta _ { c }$, the resulting sample clearly “remembers” the bias introduced by $\bar { \sigma }$in the sense that a typical configuration consists of a “sea” of spins taking the dominant value +1 (brown) with small “islands” of spins taking the value −1 (yellow). Had we set $\bar { \sigma } \equiv - 1$, we would have obtained a sample with the opposite behaviour, which illustrates the non-uniqueness of the infinite-volume measure$\mu _ { \beta }$in this case. In the case$\beta < \beta _ { c }$on the other hand, each one of the two possible spin values is about equally represented and the measure is symmetric under the substitution$1  - 1$, which illustrates the uniqueness of$\mu _ { \beta }$. It is in fact a theorem in the case of the Ising model that for$\beta > \beta _ { c }$there exist exactly two translation invariant infinite volume measures$\mu _ { \beta } ^ { \pm }$corresponding to boundary conditions$\bar { \sigma } \equiv \pm 1$and that every accumulation point of$\mu _ { \beta , N }$for any suficiently homogeneous boundary condition as$N \to \infty$is a convex combination of$\mu _ { \beta } ^ { + }$and$\mu _ { \beta } ^ { - }$

This raises the question of the uniqueness of$\mu _ { \beta }$at$\beta = \beta _ { c }$. If it is, then we say that the phase transition is continuous, otherwise it is said to be discontinuous. The reason for this terminology is that continuity in this sense turns out to be equivalent to the continuity of the maps$\beta \mapsto \mu _ { \beta } ^ { \pm } \operatorname { a t } \beta = \beta _ { c }$. It has been known for quite some time [5,60] that the phase transition for the Ising model is continuous in dimensions$d = 1 , 2$as well as$d \ge 4$. The reason why dimensions 1 and 2 are typically much better understood is that the Ising model is “solvable” in these dimensions in the sense that explicit expressions can be derived for the expectation of a large number of observables under$\mu _ { \beta , N }$(this solution is straightforward in$d = 1$[41] where no phase transition is present, but it was a major breakthrough when Onsager obtained his exact solution for$d = 2 [ 5 0 ] ,$). Dimension$d = 4$on the other hand is the “upper critical dimension” beyond which the model is expected to be “trivial” (i.e. described by Gaussian random variables in the scaling limit) which allows to use a number of powerful techniques including for example the lace expansion [39,54].

This leaves the case$d = 3$which is of course the physically most interesting one since the Ising model is a toy model of ferromagnetism and its dimensions represent the usual spatial dimensions. Heuristic considerations suggest that the phase transition is also continuous there, and this is consistent with physical experiments, assuming that the Ising model belongs to the same universality class as that of a genuine physical magnet. In the article [4], Duminil-Copin et al. gave the first rigorous proof that this is indeed the case. The proof relies on the introduction of the quantity

$$
M (\beta) = \inf _ {B \subset \mathbf {Z} ^ {3}} \frac {1}{| B | ^ {2}} \sum_ {x, y \in B} \int \sigma_ {x} \sigma_ {y} \mu_ {\beta} ^ {0} (d \sigma),
$$

where$\mu _ { \beta } ^ { 0 }$denotes the infinite volume limit obtained from using “free” conditions, as well as three main steps. First, they rely on results of [30,31] to argue that the Fourier transform of$x \mapsto \int \sigma _ { 0 } \sigma _ { x } \mu _ { \beta } ^ { 0 } ( d \sigma )$) belongs to$L ^ { 1 }$at$\beta = \beta _ { c }$, which implies tha$M ( \beta _ { c } ) = 0$. Then, and this is the main step, they show that having$M ( \beta ) = 0$implies that a certain percolation model with long-range correlations constructed from the Ising model admits no infinite clusters. Finally, they use a variant of the “switching lemma” [35] to show that the quantity $\begin{array} { r l } { \int \sigma _ { 0 } \sigma _ { x } \mu _ { \beta } ^ { + } ( d \sigma ) - \int \sigma _ { 0 } \sigma _ { x } \mu _ { \beta } ^ { 0 } ( d \sigma ) } \end{array}$is dominated by an explicit function times the probability of the origin belonging to an infinite cluster in the above mentioned model and therefore has to vanish at$\beta = \beta _ { c }$. Once this is known, it is not too dificult to show that the spontaneous magnetisation of the Ising model at criticality must vanish (namely one has$\int \sigma _ { 0 } \mu _ { \beta _ { c } } ^ { + } ( d \sigma ) = 0 )$), which in turn yields the desired uniqueness statement.

To illustrate the fact that continuity of the phase transition, whatever the dimension, is a rather non-trivial property that isn’t necessarily expected in general, a good example is that of the Potts model [53]. This is defined similarly to the Ising model, but this time the local state space � is given by$S = \{ 1 , \ldots , q \}$for some$q \geq 2$endowed again with the normalised counting measure as its reference measure. As in the Ising model, one sets$H _ { A } = 0$unless $A = \{ u , v \}$with$u , v \in \mathbf { Z } ^ { d }$such that$\left| u - v \right| = 1$, in which case one sets$H _ { A } ( \sigma ) = \mathbf { 1 } _ { \sigma _ { u } = \sigma _ { v } }$. For $q = 2$this is equivalent to the Ising model since their energy functionals only difer by a constant. Let us also remark that there is an essentially equivalent model called the random cluster model (or sometimes the FK model after Fortuin and Kasteleyn who introduced it in [28]) in which one directly considers partitions of${ \mathbf { Z } } ^ { d }$into connected “clusters” (which one should think of as the edge-connected components of the sets$\{ u : \sigma _ { u } = i \}$for$i \in S$and a given configuration$\sigma$of the Potts model) and which makes sense also for non-integer values of$q \geq 1$. (In the case$q = 1$the FK model actually reduces to regular Bernoulli percolation.) See (4.1) below for a more precise definition of this model.

It was conjectured by Baxter in the$7 0 ^ { \circ } { \bf s } [ 8 , 9 ]$that the Potts model on${ \bf Z } ^ { 2 }$exhibits a continuous phase transition if and only if$q \leq 4$. The pair of articles [17,21] by Duminil-Copin et al. provides proofs of both directions of this conjecture. For the sake of brevity we will no comment on the proofs in any detail, but we note that the proof of continuity of the phase transition for$q \leq 4$is almost completely disjoint from that in the case of the 3� Ising model. A milestone is again to show that the model at criticality with boundary condition set to one fixed element of � admits no infinite cluster. However both the proof of this fact (exploiting a form of discrete holomorphicity of certain cleverly chosen observables) and the proof of its equivalence with the uniqueness of the infinite-volume measure at criticality (actually they show equivalence of a list of 5 quite distinct properties which are of independent interest for the study of the critical Potts model) are completely diferent.

Regarding the proof of discontinuity when$q > 4$, the main tool is a close relation, first discovered by Temperley–Lieb [59] in a restricted context and then by Baxter et al. [10] in more generality, between the FK model on${ \bf Z } ^ { 2 }$to the so-called six-vertex model. Configurations of the latter can be visualised as jigsaws where one assigns to each vertex of${ \bf Z } ^ { 2 }$(or a subset thereof) one of the six (oriented) tiles

![](images/page_9_image_3.jpg)

and one enforces the admissibility constraint that the tiles fit together seamlessly. One further postulates that the probability of seeing a given admissible configuration is proportional to $c ^ { \# p }$, where$\# p$denotes the number of purple tiles in the configuration and � is some fixed constant. The relation between the six-vertex model and the critical FK model holds for the specific choice$c = { \sqrt { 2 + { \sqrt { q } } } }$. The advantage gained from this relation is that the six-vertex model is “solvable” in a certain sense using the transfer matrix formalism. This doesn’t get one out of the woods since the transfer matrices$V _ { N }$involved are very large: they act on a vector space of dimension$2 ^ { N }$, but are block diagonal with each block$V _ { N } ^ { [ n ] }$acting on a subspace of dimension$\binom { n } { N }$. Each of these blocks is irreducible with positive entries and therefore admits a Perron–Frobenius vector. The main technical result of [21] is a very sharp asymptotic for the Perron–Frobenius eigenvalues of$V _ { N } ^ { [ N / 2 - r ] }$for fixed$r$as$N \to \infty$. Interestingly, the authors are able to prove that the ratios between these values converge to finite (and explicit, at least as explicit convergent series) limits as$N \to \infty$and that the values themselves diverge exponentially in � with known exponent, but the common lower-order behaviour of that divergence is not known. This asymptotic is however suficient to obtain good control over the partition function of the six vertex model and to exploit it to compute an explicit expression for the inverse correlation length of the critical Potts model with free boundary conditions when$q > 4$. The finiteness of that expression finally allows to deduce the discontinuity of the phase transition.

To conclude this section, I would like to mention the beautiful article [20] which, although not quite dealing with the question of continuity of the phase transition, does have a related flavour. The question there is that of the “sharpness” of the phase transition which in this particular case is couched as the question whether it is really true that the measure $\mu _ { \beta }$has exponentially decaying correlations (in the sense that the covariance between$f ( \sigma _ { 0 } )$ and$f ( \sigma _ { x } )$decays exponentially fast as$| x | \to \infty$for any “nice enough” function$f \colon S  \mathbf { R } )$ for every$\beta < \beta _ { c }$and not just for small enough values where a perturbation argument around $\beta = 0$(where$f ( \sigma _ { 0 } )$and$f ( \sigma _ { x } )$are independent under$\mu _ { 0 }$as soon as$x \neq 0 )$may apply. One dificulty with this type of statements is that one will in general not know any closed-form expression for$\beta _ { c } .$: in the case of the FK model on the square lattice such an expression can be derived by a duality argument [11], but it is not known for more general situations. The main result of [20] is that the phase transition of the FK model on any vertex-transitive infinite graph is sharp.

The main tool in their proof is a novel and far-reaching generalisation of the OSSS inequality [49]. The context here is that of increasing random variables$f \colon \{ 0 , 1 \} ^ { E }  [ 0 , 1 ]$ (for a finite set � and for the natural coordinate-wise partial order on$\{ 0 , 1 \} ^ { E } )$) where$\{ 0 , 1 \} ^ { E }$ is furthermore equipped with a probability measure P that is itself monotonic in the sense that for every$F \subset E$and every$e \in E \setminus F$, the conditional probabilities${ \bf P } ( w _ { e } = 1 | \mathcal { F } _ { F } )$) are increasing functions. (Here$\mathcal { F } _ { F }$denotes the �-algebra generated by the evaluations$w \mapsto w _ { e }$ for$e \in F . )$One then considers any algorithm that reveals one by one the values of an input $w \in \{ 0 , 1 \} ^ { E }$in such a way that the coordinate to be revealed next depends in a deterministic way on the information gleaned from the revealement up to that point. (In particular, the first coordinate to be revealed is always the same since no information has been obtained yet at that point.) The algorithm stops once the revealed values are suficient to determine the value of$f ( w )$, thus yielding a random set${ \hat { E } } \subset E$of revealed values. The result of [20] is then that one has the inequality

$$
\operatorname{Var} (f) \leq \sum_ {e \in E} \mathbf {P} (e \in \hat {E}) \operatorname{Cov} (f, w _ {e}),\tag{2.1}
$$

which looks formally the same as the result of [49], but the assumption there was that the measure P is simply the uniform measure. Since the latter is clearly monotonic (it is such tha ${ \bf P } ( w _ { e } = 1 | \mathcal { F } _ { F } )$is constant), the results of [49] follow as a special case.

Using this result, [20] then obtain the following dichotomy which yields the desired sharpness statement.

Theorem 2.1. Let � be any transitive graph and let$\mathbf { P } _ { \beta , n }$be the FK measure on the ball$\Lambda _ { n }$ of radius � in �. Then, there exists$\beta _ { c } \in \mathbf { R }$such that, for every$\beta < \beta _ { c }$there exists$c _ { \beta } > 0$ such that${ \bf P } _ { \beta , n } ( 0  \partial \Lambda _ { n } ) \ne e ^ { - c _ { \beta } n }$, uniformly in �. For$\beta > \beta _ { c }$on the other hand, there exists $c > 0$such that$\mathbf { P } _ { \beta , n } ( 0  \partial \Lambda _ { n } ) \geq c \operatorname* { m i n } \{ 1 , \beta - \beta _ { c } \}$

Once (2.1) is known, the proof is surprisingly simple and relies on two ingredients. First, one can show that the measures$\mathbf { P } _ { \beta , n }$and the function${ \bf 1 } _ { 0  \partial \Lambda _ { n } }$satisfy the assumptions of (2.1). Setting$\theta _ { n } ( \beta ) = { \bf P } _ { \beta , n } ( 0  \partial \Lambda _ { n } )$, a clever choice of search algorithm for the (potential) cluster connecting the origin 0 to$\partial \Lambda _ { n }$then allows to show that one has the bound

$$
\theta_ {n} ^ {\prime} (\beta) \gtrsim \sum_ {e \in E} \operatorname{Cov} _ {\beta} \left(\mathbf {1} _ {0 \leftrightarrow \partial \Lambda_ {n}}, w _ {e}\right) \geq \frac {n}{8 \Sigma_ {n} (\beta)} \theta_ {n} (\beta) (1 - \theta_ {n} (\beta)).\tag{2.2}
$$

where$\begin{array} { r } { \Sigma _ { n } = \sum _ { k = 0 } ^ { n - 1 } \theta _ { n } } \end{array}$. The fact that the first inequality holds is known and can be checked in an elementary way. The second fact is that any sequence of functions$\beta \mapsto \theta _ { n } ( \beta )$satisfying a diferential inequality of the form (2.2) necessarily satisfies a dichotomy of the type appearing in the statement of Theorem 2.1. Since we are not interested in the regime where$\theta _ { n }$is large, we can rewrite (2.2) as$\begin{array} { r } { \theta _ { n } ^ { \prime } \geq \frac { c n } { \Sigma _ { n } } \theta _ { n } } \end{array}$. The fact that the$\theta _ { n }$then should satisfy such a dichotomy is quite clear: if$\beta$is such that they converge to a non-vanishing limit �, then$\Sigma _ { n } / n \sim \theta$and one must have$\theta ^ { \prime } \geq c$. If on the other hand they converge to 0 on a whole interval$[ a , b ]$ then that convergence must take place suficiently fast so that$\Sigma _ { n } / n \gg \theta _ { n }$(since otherwise the previous argument applies). Since$\Sigma _ { n } / n \sim \theta _ { n }$for$\theta _ { n } \sim n ^ { - \alpha }$as soon as$\alpha < 1$, it is then plausible that for any$c < b$one has$\theta _ { n } \ll n ^ { - 1 / 2 }$(say), implying$\theta _ { n } ^ { \prime } \gtrsim \sqrt { n } \theta _ { n }$and therefore $\theta _ { n } \lesssim e ^ { - \sqrt { n } \left( c - \beta \right) }$for$\beta < c$. This shows that$\Sigma _ { n }$is bounded for$\beta < c$, leading to$\theta _ { n } ^ { \prime } \gtrsim n \theta _ { n }$and therefore an exponentially (in �) small bound as claimed.

## 3. Triviality of$\Phi _ { 4 } ^ { 4 }$

It has been known since the groundbreaking work of Osterwalder and Schrader [51, 52] that, at least in some cases, the construction of a (bosonic) quantum field theory satisfying the Wightman axioms is equivalent to the construction of a probability measure on the space of distributions satisfying a number of natural properties. One of the pinnacles of that line of enquiry was the construction in the seventies of the$\Phi _ { 2 } ^ { 4 }$and$\Phi _ { 3 } ^ { 4 }$measures [22,25,27,33,34,47,48,57], which corresponds to the simplest case of an interacting theory in two or three space-time dimensions with one type of boson.

At a heuristic level, the$\Phi _ { d } ^ { 4 }$measure is the measure$\mu ^ { ( d ) }$on the space of Schwartz distributions$S ^ { \prime } ( \mathbf { R } ^ { d } )$(or on the �-dimensional torus) given by

$$
\mu^ {(d)} (d \Phi) = Z ^ {- 1} \exp \left(- \frac {1}{2} \int \left(| \nabla \Phi (x) | ^ {2} - C \Phi^ {2} (x) + \Phi^ {4} (x)\right) d x\right) d \Phi ,
$$

where$\mathbf { \ddot { \psi } } d \Phi ^ { \prime }$denotes the infinite-dimensional Lebesgue measure on$S ^ { \prime } ( \mathbf { R } ^ { d } )$. This expression is of course problematic at many levels: infinite-dimensional Lebesgue measure does not exist, distributions cannot be squared, etc. If it were only for the term$| \nabla \Phi | ^ { 2 }$, one could reasonably interpret this expression as the Gaussian measure$\mu _ { 0 }$with covariance operator given by the Green’s function of the Laplacian, which is a well-defined probability measure (modulo technicalities arising from the constant mode which can easily be fixed). The measure$\mu _ { 0 }$is called the Gaussian Free Field (GFF) since it corresponds to a quantum field theory in which particles are free, i.e. do not interact with each other at all.

This suggests that a more refined interpretation of the$\Phi _ { d } ^ { 4 }$measure could be given by

$$
\mu^ {(d)} (d \Phi) = Z ^ {- 1} \exp \left(- \frac {1}{2} \int \Phi^ {4} (x) d x\right) \mu_ {0} (d \Phi).\tag{3.1}
$$

This is still ill-defined since the GFF is supported on distributions rather than functions for any dimension$d \ge 2$. However, setting$\Phi _ { \varepsilon } = \rho _ { \varepsilon } \star \Phi$, the Wick power

$$
: \Phi^ {4} := \lim _ {\varepsilon \to 0} \left(\Phi_ {\varepsilon} ^ {4} - 3 \Phi_ {\varepsilon} ^ {2} \mathbf {E} \Phi_ {\varepsilon} ^ {2}\right),\tag{3.2}
$$

turns out to be a well-defined random Schwartz distribution (i.e. the limit exists and is independent of the choice of$\rho _ { \varepsilon } )$in dimensions$d < 4 .$. In dimension 2, Nelson showed in [47] that the Radon–Nikodym factor appearing in (3.1) with$\Phi ^ { 4 }$replaced by$\cdot \Phi ^ { 4 }$: yields an integrable random variable, thus leading to a definition of$\mu ^ { ( 2 ) }$. In particular, the$\Phi _ { 2 } ^ { 4 }$measure is equivalent to the GFF. In dimension 3, this turns out not to be the case, but it is still possible to show that the measure

$$
\mu^ {(3)} (d \Phi) = \lim _ {\varepsilon \to 0} Z _ {\varepsilon} ^ {- 1} \exp \left(- \frac {1}{2} \int \Phi_ {\varepsilon} ^ {4} (x) - C _ {\varepsilon} \Phi_ {\varepsilon} ^ {2} (x) d x\right) \mu_ {0} (d \Phi),\tag{3.3}
$$

is well-defined for a suitable choice of the constant$C _ { \varepsilon }$which difers from the choice$3 { \bf E } \Phi _ { \varepsilon } ^ { 2 } \sim$ $\varepsilon ^ { - 1 }$suggested by (3.2) by a logarithmically divergent term. (An alternative construction of this measure was recently obtained by completely diferent techniques in [37,38,46].)

This discussion begs the question of what happens for$d \ge 4$and especially when $d = 4$which is the physically most interesting case from the QFT perspective (remember that dimension here corresponds to space-time). Regarding the case$d > 4 ,$, it was already shown in the eighties by Aizenman and Fröhlich [1,2,29] that pretty much any “reasonable” definition of the$\Phi _ { d } ^ { 4 }$measure actually coincides with the GFF. This still left the case$d = 4$ which has always been expected to be the hard case since it is “critical” in the sense that, at least at a formal level, the terms$\Phi ^ { 4 }$and$| \nabla \Phi | ^ { 2 }$scale in the same way in the following sense. Writing$S _ { \lambda }$for the transformation$( S _ { \lambda } F ) ( x ) = F ( \lambda x )$, the GFF has the self-similarity property$S _ { \lambda } \Psi \overset { \mathrm { l a w } } { = } \lambda ^ { \frac { 2 - d } { 2 } } \Psi$for Ψ drawn from$\mu _ { 0 }$. Pretending that Ψ behaves like a function (even though it really is a random distribution), we deduce that

$$
\mathcal {S} _ {\lambda} | \nabla \Psi | ^ {2} = \lambda^ {- 2} | \nabla \mathcal {S} _ {\lambda} \Psi | ^ {2} \stackrel {\mathrm{law}} {=} \lambda^ {- d} | \nabla \Psi | ^ {2}, \qquad \mathcal {S} _ {\lambda} (\Psi^ {4}) = (\mathcal {S} _ {\lambda} \Psi) ^ {4} \stackrel {\mathrm{law}} {=} \lambda^ {4 - 2 d} \Psi^ {4}.
$$

These exponents are indeed equal if and only if$d = 4$. A heuristic calculation actually suggests that, at higher order, the term$| \nabla \Psi | ^ { 2 }$dominates the term$\Psi ^ { 4 }$at large scales. Variants of this observation have been made rigorous in a number of works [26,32,40], including most recently in an impressive series of works by Bauerschmidt–Brydges–Slade (see$[ 6 , 7 ]$and the references therein).

One way of formulating one of their main results is the framework given in our introduction with$S = \mathbf { R } , \mu$being Lebesgue measure,$\begin{array} { r } { H _ { \{ x \} } ( \phi ) = \frac { g } { 4 } \phi _ { x } ^ { 4 } + \frac { \nu } { 2 } \phi _ { x } ^ { 2 } , H _ { \{ x , y \} } ( \phi ) = } \end{array}$ $| \phi _ { x } - \phi _ { y } | ^ { 2 }$when � and � are neighbouring lattice sites in${ \mathbf Z } ^ { 4 }$, and$H _ { A } = 0$otherwise. This model behaves in a way that is very similar to the Ising model, to which it degenerates in the regime$g \to \infty$and$\nu = - g$. Traditionally, one considers the$\Phi ^ { 4 }$model with$\beta = 1$, since one can always reduce oneself to this case by adjusting$g$and$\nu ,$and possibly rescaling the $\phi _ { x } \mathbf { \ ' } _ { \mathbf { S } }$by a factor. One typically also considers � fixed, it is therefore the parameter � that is tuneable and plays the role of a “temperature” in this model. Just like the Ising model, it exhibits a phase transition at some value$\nu _ { c } \in \mathbf { R } ;$: for$\nu > \nu _ { c }$, there exists a unique infinite volume measure which is symmetric under$\phi \mapsto - \phi$. For$\nu < \nu _ { c }$on the other hand, one finds two distinct infinite-volume measures (as well as their convex combinations) depending on the boundary conditions one chooses.

A state$\phi \in S ^ { \Lambda _ { N } }$with$\Lambda _ { N } = \{ - N , . . . , N \} ^ { 4 }$is viewed as a distribution$\iota \phi$on the torus (of size 2) by setting, for every smooth test function$f \colon \mathbf { T } ^ { 4 }  \mathbf { R }$,

$$
\big (\iota \phi \big) (f) = \sum_ {x \in \Lambda_ {N}} \sigma_ {N} \phi_ {x} f (x / N),
$$

for a sequence of values$\sigma _ { N }$chosen in such a way that${ \bf E } \big ( ( \iota \phi ) ( 1 ) ^ { 2 } \big ) = 1$. It is then shown in [6] that$\operatorname { i f } g$is suficiently small and$\nu$is chosen in a suitable way (close but not quite equal to the critical value$\nu _ { c } )$, then$\iota \phi$converges to a massive GFF, namely the Gaussian field with covariance given by$( m ^ { 2 } - \Delta ) ^ { - 1 }$for some${ \bf { \nabla } } m \in { \bf { \bf { R } } }$(which depends on the specific way in which $\nu$is being tuned to approach$\nu _ { c }$as$N \to \infty )$

While this result strongly suggests that there exists no non-trivial$\Phi _ { 4 } ^ { 4 }$measure, it doesn’t rule out the possibility of having a non-trivial scaling limit for the discrete field we just described at (or near) criticality when the constant$g$is suficiently large (in other words “at strong coupling”). The technique of proof of [6] was to implement a rigorous version of the “renormalisation group technique”, which relies on a subtle analysis of the behaviour of the renormalisation map near the fixed point given by the GFF. This is unfortunately perturbative in nature and$\mathbf { S O }$has little hope of being able to deal with arbitrary$g .$. In the recent work [3] however, Aizenman and Duminil-Copin finally succeeded in showing the following result.

Theorem 3.1. For every way ofadjusting$g = g _ { N }$and$\nu = \nu _ { N }$as$N \to \infty$such that$\nu _ { N } \ge \nu _ { c , N }$ every$M _ { N }$∞ with$1 \ll M _ { N } \ll N$and every smooth compactly supported testfunction$f ,$ the law$\begin{array} { r } { o f \xi _ { N } ^ { f } = \sum _ { x \in \Lambda _ { N } } \phi _ { x } f ( x / M _ { N } ) } \end{array}$), normalised so that its variance is one, converges to a normal distribution.

Remark 3.2. The condition$\nu _ { N } \ge \nu _ { c , N }$can actually be slightly relaxed but not too much. This is because, in the “low temperature” regime and with free (or periodic) boundary conditions, one would expect the law of$\xi _ { N } ^ { f }$to converge to a Bernoulli random variable rather than a Gaussian.

At a high level, the main reason why [3] can deal with arbitrary couplings is that one can think of their setting as being more akin to “perturbing around$g = \infty ^ { \mathrm { , , } }$rather than around $g = 0$. In the setting of the introduction, they start by considering the Ising model as described there (i.e. with$\begin{array} { r } { \mu = \frac { 1 } { 2 } ( \delta _ { 1 } + \delta _ { - 1 } ) } \end{array}$), but then expand their class of models to allow for each site to represent a collection of spins with arbitrary ferromagnetic interactions within a site, instead of a single spin. This has the efect of replacing$\mu$by any measure that can be obtained as the law of$\delta \textstyle \sum _ { i = 1 } ^ { K } s _ { i }$for some$\delta > 0$and$K \in \mathbf { N } ,$, and where the$s _ { i } \in \{ - 1 , 1 \}$are random variables with a joint distribution proportional to ex$\begin{array} { r } { \gamma ( - \sum _ { i j } a _ { i j } s _ { i } s _ { j } ) } \end{array}$for some arbitrary but positive coeficients$a _ { i j }$. As was shown already in the$7 0 \mathrm { { ^ { \circ } s } }$[58, Thm 1], all probability measures on R of the type$Z ^ { - 1 } \exp ( c x ^ { 2 } - g x ^ { 4 } )$�� can be obtained as limits of such measures, so that the discrete$\Phi _ { 4 } ^ { 4 }$model can be viewed as a limit of block-spin models.

Recall that to show that a collection$\{ X _ { a } \} _ { a \in A }$of real-valued random variables is jointly Gaussian it sufices to show that all joint fourth cumulants${ \bf E } _ { c } \{ X _ { a _ { 1 } } , \ldots , X _ { a _ { 4 } } \}$} with $a _ { i } \in A$vanish. It is therefore not surprising that fourth cumulants of the spin variables play an important role in any proof of Gaussianity for Ising-type models. In dimension$d \ge 5$, the proof in [2] relied on two very important facts. First, writing$C ( x , y ) = \mathbf { E } \big ( \sigma _ { x } \sigma _ { y } \big )$for the spin correlation function, one shows that for any temperature any any Ferromagnetic interaction, one has the bound

$$
\left| \mathbf {E} _ {c} \{\sigma_ {x _ {1}}, \dots , \sigma_ {x _ {4}} \} \right| \leq 2 \sum_ {y \in \mathbf {Z} ^ {d}} C (x _ {1}, y) \dots C (x _ {4}, y).\tag{3.4}
$$

One then observes that at the critical temperature, the function � is bounded by

$$
C (x, y) \lesssim | x - y | ^ {2 - d}.\tag{3.5}
$$

Consider now four smooth compactly supported test functions$f _ { i }$and define

$$
X _ {i} = \sum_ {x \in \mathbf {Z} ^ {d}} \sigma_ {x} f _ {i} (x / M).
$$

In particular, the sum ranges over$O ( M ^ { d } )$sites. If one assumes that (3.5) is sharp, then one expects to have$\mathbf { E } X _ { i } ^ { 2 } \approx M ^ { d + 2 }$, so that the “correct” normalisation for the$X _ { i } { ^ \mathrm { { \rangle } } \mathrm { s } }$to have unit variance is expected to be$\xi _ { i } = M ^ { - \frac { d + 2 } 2 } X _ { i }$. On the other hand, combining the covariance bound with the bound on the fourth cumulant, a powercounting argument shows that${ \bf E } _ { c } \{ \xi _ { 1 } , \dots , \xi _ { 4 } \} \lesssim$ $M ^ { - 2 ( d + 2 ) } M ^ { d + 8 } = M ^ { 4 - d }$, which does indeed converge to 0 as$M \to \infty$when �$> 4$, thus showing that the$\xi _ { i } { { \bf \bar { s } } }$are jointly Gaussian in the limit.

Clearly this calculation does not allow us to conclude anything when$d = 4$. The main contribution of [3] is to show that (3.4) can actually be improved to a bound of the type

$$
\left| \mathbf {E} _ {c} \{\sigma_ {x _ {1}}, \dots , \sigma_ {x _ {4}} \} \right| \lesssim \frac {\sum_ {y \in \mathbf {Z} ^ {d}} C (x _ {1} , y) \cdots C (x _ {4} , y)}{\left(\sum_ {| x | \leq M} C (0 , x) ^ {2}\right) ^ {c}},\tag{3.6}
$$

for some (possibly very small)$c > 0$. Here, one assumes that the$x _ { i } { ' } s$are all at distances at least � of each other.

Remark 3.3. If one believes that the bound (3.5) represents the correct behaviour of � at criticality, then the denominator appearing in (3.6) is of order$( \log M ) ^ { c }$in dimension 4. This however is not known and is also not used by [3], whether for deriving (3.6) or for deducing Theorem 3.1 from it.

The proof of (3.6) relies on the “random current” representation of the Ising model in which the configuration space consists of “currents”, namely maps n:$E \to \mathbf { N }$where � denotes the set of (unoriented) nearest-neighbour pairs in our lattice. The Ising measure then naturally leads to a weight � on currents defined by$\begin{array} { r } { w ( \mathbf { n } ) = \prod _ { e \in E } \frac { \beta ^ { \mathbf { n } ( e ) } } { \mathbf { n } ( e ) ! } } \end{array}$as well as the notion of “source” of a current given by

$$
\partial \mathbf {n} \stackrel {{\text { def }}} {{=}} \left\{x: \sum_ {e \ni x} \mathbf {n} (e) \text {   is   odd } \right\}.
$$

The link between currents and the Ising model is the following formula. Given any finite set $A \subset \mathbf { Z } ^ { d }$, one has

$$
\mathbf {E} \prod_ {a \in A} \sigma_ {a} = \frac {\sum_ {\mathbf {n} : \partial \mathbf {n} = A} w (\mathbf {n})}{\sum_ {\mathbf {n} : \partial \mathbf {n} = \emptyset} w (\mathbf {n})}.
$$

A natural notion then is that of a “random current with source$A ^ { \prime \prime }$for which the probability of seeing a given current n is non-vanishing only when$\partial \mathbf { n } = A$in which case it is proportional to$w ( \mathbf { n } )$. When$A = \{ x , y \}$, a current n with source � can be interpreted (not uniquely!) as the occupation measure of a collection of loops in${ \mathbf { Z } } ^ { d }$, together with a non self-intersecting path joining � and . In particular, the restriction of n to the collection of loops connected (either directly or indirectly through other loops) to the path joining � and � can be thought of as the occupation measure of one single random path joining � to �.

The bound (3.6) can then be reformulated in terms of intersection properties of such random paths. From a heuristic perspective, one gets a lot of mileage from thinking of these random paths as simple random walk trajectories. Note that dimension 4 is critical for the question whether the traces of two random walk trajectories intersect or not: in$d < 4$, the trajectories of two independent random walks with any two starting points will intersect almost surely. In$d > 4$on the other hand, they only intersect with positive probability (going to 0 as the two starting points are taken far from each other) and, if they do, they only have a finite number of intersection points. In dimension$d = 4$, the probability that two random walks starting at distance of order � from each other do intersect decays like$1 / { \log M }$, but the expected number of intersection times remains of order one as$M  \infty$. This shows that if they do intersect, then the number of intersection points is typically quite large, of order log �.

The bulk of the hard work performed in [3] is to show that the random paths arising in the random cluster representation of the Ising model at criticality exhibit a similar behaviour, but with log � replaced by some quantity of size at least (log$M ) ^ { c }$for some$c > 0 .$. The argument is a masterpiece combining a delicate multiscale analysis, topological arguments, and probabilistic reasoning. One of the main problem the authors have to overcome is the fact that these random paths are very far from being simple random walks and only satisfy some spatial version of the Markov property.

## 4. Rotational invariance for the critical FK models

As already mentioned a number of times, a crucial feature of 2� equilibrium statistica mechanics is the fact that most models are expected to obey a form of conformal invariance (or equivariance) when considering large-scale observables at the critical temperature. This expectation and the resulting link to the well understood world of$2 d$conformal field theories allows to generate a plethora of conjectures regarding the large-scale behaviour of these models, but these are in many cases extremely hard to prove. Consider for example the �-step 2� self-avoiding random walk which is simply the uniform measure on all functions $h \colon \{ 0 , \ldots , N \} \to \mathbf { Z } ^ { 2 }$such that$h ( 0 ) = 0$and such that$| h ( i + 1 ) - h ( i ) | = 1$for all$i < N$ Exploiting the expected conformal invariance of its suitably rescaled large-� limit, one expects the size of$h ( N )$to be of order$N ^ { 3 / 4 }$and its rescaling by$N ^ { 3 / 4 }$to converge to a specific continuous random curve, namely$\mathrm { S L E } _ { 8 / 3 }$[42]. Rigorously, almost nothing non-trivial is known: although the diameter of the range of ℎ trivially has to be at least$\sqrt { N / \pi }$, the current best lower bound on the endpoint does not even match that! Instead, one only knows the bound $\begin{array} { r } { ( \mathbf { E } | h ( N ) | ^ { p } ) ^ { 1 / p } \geq \frac { 1 } { 6 } N ^ { p / ( 2 p + 2 ) } } \end{array}$that was recently obtained by Madras [44]. Similarly, while one trivially has$| h ( N ) | \leq N$, the best non-trivial upper bound is pretty much the weakest possible improvement, namely that for every$p \geq 1$one has lim$_ { N  \infty } N ^ { - 1 } ( { \bf E } | h ( N ) | ^ { p } ) ^ { 1 / p } = 0$, obtained around the same time by Duminil-Copin and Hammond [18]. One main obstruction is that there is at the moment no proof showing that the self-avoiding random walk is conformally invariant at large scales.

While this illustrates the importance of showing that statistical models are conformally invariant (or at least rotationally invariant as a crucial first step) at criticality, the strategy of proof for such claims has so far mostly relied on finding a large enough collection of observables that already satisfy a discrete analogue of conformal invariance, typically by solving a discrete analogue of the Cauchy–Riemann equations. See for example Chelkak and Smirnov’s proof of conformal invariance for the Ising model on isoradial graphs [15] and Smirnov’s proof of conformal invariance for critical percolation [56]. The two-dimensional FK model with$q \leq 4$already mentioned in Section 2 is one of the simplest models where conformal invariance at criticality is expected, but where it is not known how to obtain this from a suitable discrete conformal invariance. In the recent work [19], Duminil-Copin et al. show that the large-scale behaviour of these models is indeed rotationally invariant.

To define the notion of “large-scale behaviour”, we recall that the configuration space of the FK model is the same as that for regular percolation, see Figure 1. Such a configuration can alternatively be described as a collection of non self-intersecting loops separating the percolation clusters from the clusters of the dual configuration. (Actually it naturally yields two collections of loops, depending on whether the loop encloses a percolation cluster of the primary or of the dual configuration, but we will ignore this detail for the sake of our exposition.) Given two collections$\mathcal { F }$and$\bar { \mathcal F }$of non self-intersecting loops in the plane, one then defines a distance between them in the following way. Given (small)$\eta > 0 .$, write$\mathcal { B } _ { \eta } \subset { \bf R } ^ { 2 }$ for a large chunk of a fine lattice in${ \bf R } ^ { 2 }$, for example$\mathcal { B } _ { \eta } = \eta \mathbf { Z } ^ { 2 } \cap [ - \eta ^ { - 1 } , \eta ^ { - 1 } ] ^ { 2 }$. Given a loop $\gamma$and assuming that its image doesn’t intersect the set$\mathcal { B } _ { \eta }$, one then denotes by$[ \eta ] _ { \gamma }$its homotopy class in$\mathbf { R } ^ { 2 } \setminus \mathcal { B } _ { \eta }$. One then postulates that$d _ { H } ( \mathcal { F } , \bar { \mathcal { F } } ) \leq \eta$if and only if, for every $\gamma \in { \mathcal { F } }$that encloses at least two elements of$\mathcal { B } _ { \eta }$but not all of it, there exists$\bar { \gamma } \in \bar { \mathcal F }$such that $[ \gamma ] _ { \eta } = [ \bar { \gamma } ] _ { \eta }$and vice-versa. (The � here stands for ‘homotopy’.)

![](images/page_17_image_0.jpg)

Figure 3

Examples of graphs$L ( \alpha )$. On the left is a generic � while on the right � is constant but non-zero. The graph itself is drawn in black, the vertices of its dual graph are drawn in white, and the associated diamond graph is light gray. In red, we draw one of the symmetry axes of the second graph.

Given a metric space$( M , d )$, the metric � lifts naturally to a metric on the space of probability measures on � which metrises the topology of weak convergence (at least when � is “nice”, for example Polish). This is done by considering the Wasserstein (also sometimes called Kantorovich–Rubinstein or Monge–Kantorovich) distance

$$
d (\mu , \nu) = \inf _ {\mathbf {P} \in \mathcal {C} (\mu , \nu)} \int d (x, y)   \mathbf {P} (d x, d y)  ,
$$

where$C ( \mu _ { 1 } , \mu _ { 2 } )$denotes the set of all couplings between$\mu _ { 1 }$and$\mu _ { 2 }$, that is probability measures on$M ^ { 2 }$with �th marginal equal to$\mu _ { i }$. Note that with this definition, the map that assigns to � the probability measure$\delta _ { x }$concentrated at � is an isometry.

Fix now once and for all$q \in [ 1 , 4 ]$and consider a smooth bounded simply connected domain$\Omega \subset \mathbf { R } ^ { 2 }$. For$\varepsilon > 0$, write$\mathbf { P } _ { \varepsilon , \Omega }$for the critical FK measure (viewed as a measure on collections of loops) on$\varepsilon \mathbf { Z } ^ { 2 } \cap \Omega$with free boundary conditions. We also write$\mathbf { P } _ { \varepsilon }$for the limit of$\mathbf { P } _ { \varepsilon , \Omega }$as$\Omega \to \mathbf { R } ^ { 2 }$. Given an angle$\boldsymbol \theta \in \mathbf { R }$, we also write$R _ { \theta }$for the rotation by �, which naturally acts on loops in${ \bf R } ^ { 2 }$. The large-scale rotational invariance of the critical FK model can then be formulated as follows.

Theorem 4.1. For every domain$\Omega \subset \mathbf { R } ^ { 2 }$as above and every angle � one has

$$
\lim _ {\varepsilon \to 0} d _ {H} \big (R _ {\theta} ^ {*} \mathbf {P} _ {\varepsilon , \Omega}, \mathbf {P} _ {\varepsilon , R _ {\theta} \Omega} \big) = 0.
$$

Furthermore, one has lim$\begin{array} { r } { 1 _ { \varepsilon \to 0 } d _ { H } \big ( R _ { \theta } ^ { * } \mathbf { P } _ { \varepsilon } , \mathbf { P } _ { \varepsilon } \big ) = 0 . } \end{array}$

We only focus on the second statement since it turns out that the first one can be deduced from it without too much efort. In fact, the authors of [19] show a type of universality statement for the FK model on rectangular lattices, but its formulation requires some preparation. We start by defining a specific class of isoradial embeddings of the two dimensional square lattice into the plane. Recall that a planar graph embedded in the plane is isoradial if, for each face$f ,$, there exists a circle of radius 1 containing all the vertices of$f .$ (For example, the canonical embedding of the square lattice is isoradial.)

Given a bi-infinite sequence � :$\mathbf { Z } \to ( - \frac { \pi } { 2 } , \frac { \pi } { 2 } )$, we consider the map$\iota _ { \alpha } \colon { \mathbf { Z } } ^ { 2 } \to { \mathbf { R } } ^ { 2 }$ given by

$$
\iota_ {\alpha} \colon (x, y) \mapsto \left(x + s _ {y}, c _ {y}\right), \quad s _ {y} = \sum_ {k \in (0, y ]} \sin (\alpha_ {k}), \quad c _ {y} = \sum_ {k \in (0, y ]} \cos (\alpha_ {k}),
$$

with the convention that for$\begin{array} { r } { y < 0 , \sum _ { ( 0 , y ] } = - \sum _ { ( y , 0 ] } } \end{array}$. This defines an isoradial graph$L ( \alpha )$by considering the embedding of$\{ ( x , y ) : x + y { \mathrm { e v e n } } \}$(joined by diagonal edges) under$\iota _ { \alpha }$(see Figure 3). The dual graph$L ^ { * } ( \alpha )$of$L ( \alpha )$is then given by the embedding of$\{ ( x , y ) : x + y$odd}. The associated “diamond graph” has as its vertices both the vertices of$L ( \alpha )$and the centres of its faces, and its edges are given by all pairs$( v , f )$with � a vertex and � a face such that $v \in f$. The diamond graph is simply given by the embedding of the usual lattice${ \bf Z } ^ { 2 }$with nearest-neighbour edges under$\iota _ { \alpha }$

It is crucial at this stage to note that the critical FK model on$L ( \alpha )$is not given by simply pushing forward the critical FK model on${ \bf Z } ^ { 2 }$under the map$\iota _ { \alpha }$. Instead, one reweighs each edge of the graph in a very specific way that depends on the length of the edge. More specifically, viewing a configuration of the FK model as a subset$\omega \subset E$of the set of edges of the (finite) graph on which the model is considered, the probability of seeing a given configuration � is proportional to

$$
\Big (\prod_ {e \in \omega} p _ {e} \Big) \Big (\prod_ {e \in E \setminus \omega} (1 - p _ {e}) \Big) q ^ {k (\omega)},\tag{4.1}
$$

where$k ( \omega )$denotes the number of connected components of the subgraph �. The formula for$p _ { e }$as a function of$q$and the length of the edge � is explicit but not relevant for the sake of this discussion.

The most important step in the proof is to show that the large-scale connectivity properties of the critical FK model on$L ( \alpha )$are very close to those of the model on$L ( T _ { j } \alpha )$ where$T _ { j }$swaps the �th and$( j + 1 )$)th component:

$$
(T _ {j} \alpha) _ {k} = \left\{ \begin{array}{l l} \alpha_ {j + 1} & \text { if } k = j, \\ \alpha_ {j} & \text { if } k = j + 1, \\ \alpha_ {k} & \text { otherwise }. \end{array} \right.
$$

Furthermore, there exists a natural coupling between the FK measures on the two lattices which implements this “closedness”. This part of the proof exploits the link to the six vertex model and its “solvability” using the transfer matrix formalism. One then deduces from this that the model on the standard lattice$L ( 0 )$is very close to that on a rotated rectangular lattice$L ( \alpha )$with$k \mapsto \alpha _ { k }$constant (see the right half of Figure 3). This works by fixing some large$N > 0$(which is then eventually sent to infinity) and starting from$\alpha _ { k } ^ { ( i ) } = \alpha \mathbf { 1 } _ { k \geq N }$ and then swapping components in such a way as to move some of the non-zero components down until une ends up with$\alpha _ { k } ^ { ( f ) } = \alpha \big ( \mathbf { 1 } _ { | k | \leq N } + \mathbf { 1 } _ { k > 3 N } \big )$. Since one has$L ( 0 ) \approx L ( \alpha ^ { ( i ) } )$) and $L ( \alpha ) \approx L ( \alpha ^ { ( f ) } )$, the desired statement follows if one can control the error made at each step of the argument. This turns out to be extremely delicate and one has to exploit subtle stochastic cancellations along the way. One trick is to allow the vertices of the set$\mathcal { B } _ { \eta }$around which the homotopy classes are computed to move a little bit with each application of a swapping operator$T _ { j }$and to show that this motion ends up being difusive (and therefore “slow”) rather than ballistic.

Once one knows that$\begin{array} { r } { \operatorname* { l i m } _ { \varepsilon \to 0 } d _ { H } ( \mathbf { P } _ { \varepsilon , L ( 0 ) } , \mathbf { P } _ { \varepsilon , L ( \alpha ) } ) = 0 } \end{array}$, the second part of The orem 4.1 follows at once. The idea is simply to note that$L ( \alpha )$is invariant under reflection along a line with angle$\textstyle { \frac { \pi } { 4 } } - { \frac { \alpha } { 2 } }$, but that the efect of this reflection on$L ( 0 )$is the same as tha of a rotation by angle � (since it is itself invariant under reflection along a line with angle$\textstyle { \frac { \pi } { 4 } } )$), so that

$$
d _ {H} (\mathbf {P} _ {\varepsilon}, R _ {\alpha} ^ {*} \mathbf {P} _ {\varepsilon}) \leq d _ {H} (\mathbf {P} _ {\varepsilon , L (0)}, \mathbf {P} _ {\varepsilon , L (\alpha)}) + d _ {H} (\mathbf {P} _ {\varepsilon , L (\alpha)}, R _ {\alpha} ^ {*} \mathbf {P} _ {\varepsilon , L (0)}) = 2 d _ {H} (\mathbf {P} _ {\varepsilon , L (0)}, \mathbf {P} _ {\varepsilon , L (\alpha)})
$$

and the claim follows.

## Funding

This work was partially supported by the Royal Society through a research professorship.

## References

[1]M. Aizenman, Proof of the triviality of$\varphi _ { d } ^ { 4 }$field theory and some mean-field features of Ising models for � > 4. Phys. Rev. Lett. 47 (1981), no. 1, 1–4

[2]M. Aizenman, Geometric analysis of$\varphi ^ { 4 }$fields and Ising models. I, II. Comm. Math. Phys. 86 (1982), no. 1, 1–48

[3]M. Aizenman and H. Duminil-Copin, Marginal triviality of the scaling limits of critical 4D Ising and$\phi _ { 4 } ^ { 4 }$models. Ann. ofMath. (2) 194 (2021), no. 1, 163–235

[4]M. Aizenman, H. Duminil-Copin, and V. Sidoravicius, Random currents and continuity of Ising model’s spontaneous magnetization. Comm. Math. Phys. 334 (2015), no. 2, 719–742

[5]M. Aizenman and R. Fernández, On the critical behavior of the magnetization in high-dimensional Ising models. J. Statist. Phys. 44 (1986), no. 3-4, 393–454

[6]R. Bauerschmidt, D. C. Brydges, and G. Slade, Scaling limits and critical behaviour of the 4-dimensional �-component$| \phi | ^ { 4 }$spin model. J. Stat. Phys. 157 (2014), no. 4-5, 692–742

[7]R. Bauerschmidt, D. C. Brydges, and G. Slade, A renormalisation group method. III. Perturbative analysis. J. Stat. Phys. 159 (2015), no. 3, 492–529

[8]R. J. Baxter, Generalized ferroelectric model on a square lattice. Studies in Appl. Math. 50 (1971), 51–69

[9]R. J. Baxter, Potts model at the critical temperature. Journal ofPhysics C: Solid State Physics 6 (1973), no. 23, L445–L448

[10]R. J. Baxter, S. B. Kelland, and F. Y. Wu, Equivalence of the Potts model or Whitney polynomial with an ice-type model. Journal ofPhysics A: Mathematical and General 9 (1976), no. 3, 397–406

[11]V. Befara and H. Duminil-Copin, The self-dual point of the two-dimensional random-cluster model is critical for$q \geq 1$. Probab. Theory Related Fields 153 (2012), no. 3-4, 511–542

[12] S. R. Broadbent and J. M. Hammersley, Percolation processes: I. crystals and mazes. Mathematical Proceedings ofthe Cambridge Philosophical Society 53 (1957), no. 3, 629–64

[13] F. Camia, C. Garban, and C. M. Newman, Planar Ising magnetization field I. Uniqueness of the critical scaling limit. Ann. Probab. 43 (2015), no. 2, 528–571

[14] F. Camia, C. Garban, and C. M. Newman, Planar Ising magnetization field II. Properties of the critical and near-critical scaling limits. Ann. Inst. Henri Poincaré Probab. Stat. 52 (2016), no. 1, 146–161

[15] D. Chelkak and S. Smirnov, Universality in the 2D Ising model and conformal invariance of fermionic observables. Invent. Math. 189 (2012), no. 3, 515–580

[16] H. Duminil-Copin, 100 years of the (critical) Ising model on the hypercubic lattice. In Proceedings ofthe International Congress ofMathematicians. Vol. 1, pp.???–???, 2022

[17]H. Duminil-Copin, M. Gagnebin, M. Harel, I. Manolescu, and V. Tassion, Discontinuity of the phase transition for the planar random-cluster and Potts models with <sub>�</sub> > 4. Ann. Sci. Éc. Norm. Supér. (4) 54 (2021), no. 6, 1363–1413

[18] H. Duminil-Copin and A. Hammond, Self-avoiding walk is sub-ballistic. Comm Math. Phys. 324 (2013), no. 2, 401–423

[19] H. Duminil-Copin, K. K. Kozlowski, D. Krachun, I. Manolescu, and M. Oulamara, Rotational invariance in critical planar lattice models. arXiv preprint (2020)

[20] H. Duminil-Copin, A. Raoufi, and V. Tassion, Sharp phase transition for the random-cluster and Potts models via decision trees. Ann. ofMath. (2) 189 (2019), no. 1, 75–99

[21]H. Duminil-Copin, V. Sidoravicius, and V. Tassion, Continuity of the phase transition for planar random-cluster and Potts models with$1 \leq q \leq 4 .$. Comm. Math. Phys. 349 (2017), no. 1, 47–107

[22] J.-P. Eckmann and K. Osterwalder, On the uniqueness of the Hamiltionian and of the representation of the C�� for the quartic boson interaction in three dimen sions. Helv. Phys. Acta 44 (1971), 884–909

[23]S. El-Showk, M. F. Paulos, D. Poland, S. Rychkov, D. Simmons-Dufin, and A. Vichi, Solving the 3d Ising model with the conformal bootstrap. Phys. Rev D 86 (2012), 025022

[24] S. El-Showk, M. F. Paulos, D. Poland, S. Rychkov, D. Simmons-Dufin, and A. Vichi, Solving the 3d Ising model with the conformal bootstrap II. �-minimization and precise critical exponents. J. Stat. Phys. 157 (2014), no. 4-5, 869–914

[25] J. Feldman, The$\lambda \varphi _ { 3 } ^ { 4 }$field theory in a finite volume. Comm. Math. Phys. 37 (1974), 93–120

[26] J. Feldman, J. Magnen, V. Rivasseau, and R. Sénéor, Construction and Borel summability of infrared$\Phi _ { 4 } ^ { 4 }$by a phase space expansion. Comm. Math. Phys. 109 (1987), no. 3, 437–480

[27] J. S. Feldman and K. Osterwalder, The Wightman axioms and the mass gap for weakly coupled$( \Phi ^ { 4 } ) _ { 3 }$quantum field theories. Ann. Physics 97 (1976), no. 1, 80–135

[28] C. M. Fortuin and P. W. Kasteleyn, On the random-cluster model. I. Introduction and relation to other models. Physica 57 (1972), 536–564

[29] J. Fröhlich, On the triviality of$\lambda \varphi _ { d } ^ { 4 }$theories and the approach to the critical point in$d > 4$dimensions. Nuclear Phys. B 200 (1982), no. 2, 281–296

[30] J. Fröhlich, R. Israel, E. H. Lieb, and B. Simon, Phase transitions and reflection positivity. I. General theory and long range lattice models. Comm. Math. Phys. 62 (1978), no. 1, 1–34

[31] J. Fröhlich, B. Simon, and T. Spencer, Infrared bounds, phase transitions and continuous symmetry breaking. Comm. Math. Phys. 50 (1976), no. 1, 79–95

[32] K. Gawędzki and A. Kupiainen, Massless lattice$\varphi _ { 4 } ^ { 4 }$theory: a nonperturbative control of a renormalizable model. Phys. Rev. Lett. 54 (1985), no. 2, 92–94

[33] J. Glimm, Boson fields with the$\because \Phi ^ { 4 }$: interaction in three dimensions. Comm. Math. Phys. 10 (1968), 1–47

[34] J. Glimm and A. Jafe, Positivity of the$\phi _ { 3 } ^ { 4 }$Hamiltonian. Fortschr. Physik 21 (1973), 327–376

[35] R. B. Grifiths, C. A. Hurst, and S. Sherman, Concavity of magnetization of an Ising ferromagnet in a positive external field. J. Mathematical Phys. 11 (1970), 790–795

[36]G. Grimmett, Percolation. Second edn., Grundlehren der mathematischen Wis senschaften [Fundamental Principles of Mathematical Sciences] 321, Springer-Verlag, Berlin, 1999

[37] M. Hairer, A theory of regularity structures. Invent. math. 198 (2014), no. 2, 269–504

[38] M. Hairer and J. Mattingly, The strong Feller property for singular stochastic PDEs. Ann. Inst. H. Poincaré Probab. Statist. 54 (2018), no. 3, 1314–1340

[39]T. Hara and G. Slade, Mean-field behaviour and the lace expansion. In Probability and phase transition (Cambridge, 1993), pp. 87–122, NATO Adv. Sci. Inst. Ser. C: Math. Phys. Sci. 420, Kluwer Acad. Publ., Dordrecht, 1994

[40]T. Hara and H. Tasaki, A rigorous control of logarithmic corrections in fourdimensional$\phi ^ { 4 }$spin systems. II. Critical behavior of susceptibility and correlation length. J. Statist. Phys. 47 (1987), no. 1-2, 99–121

[41] E. Ising, Beitrag zur Theorie des Ferromagnetismus. Zeitschriftfur Physik 31 (1925), no. 1, 253–258

[42]G. F. Lawler, O. Schramm, and W. Werner, On the scaling limit of planar self-avoiding walk. In Fractal geometry and applications: ajubilee ofBenoît Mandelbrot, Part 2, pp. 339–364, Proc. Sympos. Pure Math. 72, Amer. Math. Soc., Providence, RI, 2004

[43] W. Lenz, Beitrag zum Verständnis der magnetischen Erscheinungen in festen Körpern. Z. Phys. 21 (1920), 613–615

[44] N. Madras, A lower bound for the end-to-end distance of the self-avoiding walk. Canad. Math. Bull. 57 (2014), no. 1, 113–118

[45] J. Miller and S. Shefield, Quantum Loewner evolution. Duke Math. J. 165 (2016), no. 17, 3241–3378

[46] A. Moinat and H. Weber, Space-time localisation for the dynamic$\Phi _ { 3 } ^ { 4 }$model. Communications on Pure and Applied Mathematics 73 (2020), no. 12, 2519–2555

[47] E. Nelson, A quartic interaction in two dimensions. In Mathematical Theory of Elementary Particles (Proc. Conf., Dedham, Mass., 1965), pp. 69–73, M.I.T. Press, Cambridge, Mass., 1966

[48] E. Nelson, Construction of quantum fields from Markof fields. J. Functional Analysis 12 (1973), 97–112

[49] R. O’Donnell, M. Saks, O. Schramm, and R. Servedio, Every decision tree has an influential variable. In 46th annual ieee symposium onfoundations ofcomputer science (focs’05), pp. 31–39, 2005

[50] L. Onsager, Crystal statistics. I. A two-dimensional model with an order-disorder transition. Phys. Rev. (2) 65 (1944), 117–149

[51] K. Osterwalder and R. Schrader, Axioms for Euclidean Green’s functions. Comm. Math. Phys. 31 (1973), 83–112

[52] K. Osterwalder and R. Schrader, Axioms for Euclidean Green’s functions II. Communications in Mathematical Physics 42 (1973), 281–305

[53] R. B. Potts, Some generalized order-disorder transformations. Proc. Cambridge Philos. Soc. 48 (1952), 106–109

[54] A. Sakai, Lace expansion for the Ising model. Comm. Math. Phys. 272 (2007), no. 2, 283–344

[55] O. Schramm, Scaling limits of loop-erased random walks and uniform spanning trees. Israel J. Math. 118 (2000), 221–288

[56] O. Schramm and S. Smirnov, On the scaling limits of planar percolation. Ann. Probab. 39 (2011), no. 5, 1768–1814

[57] B. Simon, The �(�)<sub>2</sub> Euclidean (quantum) field theory. Princeton Series in Physics, Princeton University Press, Princeton, N.J., 1974

[58] B. Simon and R. B. Grifiths, The$( \phi ^ { 4 } ) _ { 2 }$field theory as a classical Ising model. Comm. Math. Phys. 33 (1973), 145–164

[59]H. N. V. Temperley and E. H. Lieb, Relations between the “percolation” and “colouring” problem and other graph-theoretical problems associated with regular planar lattices: some exact results for the “percolation” problem. Proc. Roy. Soc. London Ser. A 322 (1971), no. 1549, 251–280

[60] C. N. Yang, The spontaneous magnetization of a two-dimensional Ising model. Phys. Rev. (2) 85 (1952), 808–816

## Martin Hairer

Imperial College London, UK, m.hairer@imperial.ac.uk