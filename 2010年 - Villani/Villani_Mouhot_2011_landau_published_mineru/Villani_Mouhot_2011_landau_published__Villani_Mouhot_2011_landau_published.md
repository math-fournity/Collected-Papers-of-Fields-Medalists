## On Landau damping

by

Clement Mouhot´

Cedric Villani´

University of Cambridge Cambridge, U.K.

Institut Henri Poincar´e & Universit´e de Lyon Lyon, France

Dedicated to Vladimir Arnold and Carlo Cercignani.

## Contents

1. Introduction to Landau damping 32  
1.1. Discovery 32  
1.2. Interpretation 35  
1.3. Range of validity 36  
1.4. Conceptual problems 40  
1.5. Previous mathematical results 41  
2. Main result 42  
2.1. Modeling 42  
2.2. Linear damping 44  
2.3. Non-linear damping 46  
2.4. Comments 48  
2.5. Interpretation 52  
2.6. Main ingredients 52  
2.7. About phase mixing 53  
3. Linear damping 54  
4. Analytic norms 64  
4.1. Single-variable analytic norms 65  
4.2. Analytic norms in two variables 71  
4.3. Relations between functional spaces 73  
4.4. Injections 75  
4.5. Algebra property in two variables 79  
4.6. Composition inequality 80  
4.7. Gradient inequality 82  
4.8. Inversion 83  
4.9. Sobolev corrections 85  
4.10. Individual mode estimates 86  
4.11. Measuring solutions of kinetic equations in large time 87  
4.12. Linear damping revisited 88

5. Deflection estimates ..... 90
    5.1. Formal expansion ..... 91
    5.2. Main result ..... 92
6. Bilinear regularity and decay estimates ..... 96
    6.1. Basic bilinear estimate ..... 98
    6.2. Short-term regularity extortion by time cheating ..... 99
    6.3. Long-term regularity extortion ..... 101
7. Control of the time-response ..... 106
    7.1. Qualitative discussion ..... 107
    7.2. Exponential moments of the kernel ..... 113
    7.3. Dual exponential moments ..... 117
    7.4. Growth control ..... 119
8. Approximation schemes ..... 134
    8.1. The natural Newton scheme ..... 135
    8.2. Battle plan ..... 136
9. Local-in-time iteration ..... 140
10. Global in time iteration ..... 144
    10.1. The statement of the induction ..... 144
    10.2. Preparatory remarks ..... 146
    10.3. Estimates on the characteristics ..... 149
    10.4. Estimates on the density and distribution along characteristics ..... 157
    10.5. Convergence of the scheme ..... 170
11. Coulomb–Newton interaction ..... 172
    11.1. Estimates on exponentially large times ..... 172
    11.2. Mode-by-mode estimates ..... 173
12. Convergence in large time ..... 177
13. Non-analytic perturbations ..... 180
14. Expansions and counterexamples ..... 185
    14.1. Simple excitation ..... 186
    14.2. General perturbation ..... 188
15. Beyond Landau damping ..... 191
Appendix ..... 193
    A.1. Calculus in dimension d ..... 193
    A.2. Multi-dimensional differential calculus ..... 193
    A.3. Fourier transform ..... 194
    A.4. Fixed-point theorem ..... 195
    A.5. Plemelj formula ..... 195
References ..... 197

Landau damping may be the single most famous mystery of classical plasma physics. For the past sixty years it has been treated in the linear setting at various degrees of rigor; but its non-linear version has remained elusive, since the only available results [13], [41] prove the existence of some damped solutions, without telling anything about their genericity.

In the present work we close this gap by treating the non-linear version of Landau damping in arbitrarily large times, under assumptions which cover both attractive and repulsive interactions, of any regularity down to Coulomb–Newton.

This will lead us to discover a distinctive mathematical theory of Landau damping, complete with its own functional spaces and functional inequalities. Let us make it clear that this study is not just for the sake of mathematical rigor: indeed, we shall get new insights into the physics of the problem, and identify new mathematical phenomena.

The plan of the paper is as follows.

In 1 we provide an introduction to Landau damping, including historical comments and a review of the existing literature. Then in 2 we state and comment on our main result about “non-linear Landau damping” (Theorem 2.6).

In 3 we provide a rather complete treatment of linear Landau damping, slightly improving on the existing results both in generality and simplicity. This section can be read independently of the rest.

In 4 we define the spaces of analytic functions which are used in the remainder of the paper. The careful choice of norms is one of the keys of our analysis; the complexity of the problem will naturally lead us to work with norms having up to five parameters. As a first application, we shall revisit linear Landau damping within this framework.

In 5–7 we establish four types of new estimates (deflection estimates, short-term and long-term regularity extortion, echo control); these are the key sections containing in particular the physically relevant new material.

In 8 we adapt the Newton algorithm to the setting of the non-linear Vlasov equation. Then in 9–11 we establish some iterative estimates along this scheme. ( 11 is devoted specifically to a technical refinement allowing us to handle Coulomb–Newton interaction.)

From these estimates our main theorem is easily deduced in 12.

An extension to non-analytic perturbations is presented in 13.

Some counterexamples and asymptotic expansions are studied in 14.

Final comments about the scope and range of applicability of these results are provided in 15.

Even though it basically proves one main result, this paper is very long. This is due partly to the intrinsic complexity and richness of the problem, partly to the need to develop an adequate functional theory from scratch, and partly to the inclusion of remarks, explanations and comments intended to help the reader to understand the proof and the scope of the results. The whole process culminates in the extremely technical iteration performed in 10 and 11. A short summary of our results and methods of proofs can be found in the expository paper [69].

This project started from an unlikely conjunction of discussions of the authors with various people, most notably Yan Guo, Dong Li, Freddy Bouchet and Etienne Ghys.<sup>´</sup> We also got crucial inspiration from the books [9] and [10] by James Binney and Scott Tremaine; and [2] by Serge Alinhac and Patrick G´erard. Warm thanks to Julien Barr´e, Jean Dolbeault, Thierry Gallay, Stephen Gustafson, Gregory Hammett, Donald Lynden-Bell, Michael Sigal, Eric S´<sup>´</sup> er´e and especially Michael Kiessling for useful exchanges and references; and to Francis Filbet and Irene Gamba for providing numerical simulations. We are also grateful to Patrick Bernard, Freddy Bouchet, Emanuele Caglioti, Yves Elskens, Yan Guo, Zhiwu Lin, Michael Loss, Peter Markowich, Govind Menon, Yann Ollivier, Mario Pulvirenti, Jef Rauch, Igor Rodnianski, Peter Smereka, Yoshio Sone, Tom Spencer, and the team of the Princeton Plasma Physics Laboratory for further constructive discussions about our results. Finally, we acknowledge the generous hospitality of several institutions: Brown University, where the first author was introduced to Landau damping by Yan Guo in early 2005; the Institute for Advanced Study in Princeton, who ofered the second author a serene atmosphere of work and concentration during the best part of the preparation of this work; Cambridge University, who provided repeated hospitality to the first author thanks to the Award No. KUK-I1-007-43, funded by the King Abdullah University of Science and Technology; and the University of Michigan, where conversations with Jef Rauch and others triggered a significant improvement of our results.

Our deep thanks go to the referees for their careful examination of the manuscript. We dedicate this paper to two great scientists who passed away during the elaboration of our work. The first one is Carlo Cercignani, one of the leaders of kinetic theory, author of several masterful treatises on the Boltzmann equation, and a long-time personal friend of the second author. The other one is Vladimir Arnold, a mathematician of extraordinary insight and influence; in this paper we shall uncover a tight link between Landau damping and the theory of perturbation of completely integrable Hamiltonian systems, to which Arnold has made major contributions.

## 1. Introduction to Landau damping

## 1.1. Discovery

Under adequate assumptions (collisionless regime, non-relativistic motion, heavy ions, no magnetic field), a dilute plasma is well described by the non-linear Vlasov–Poisson equation

$$
\frac {\partial f}{\partial t} + v \cdot \nabla_ {x} f + \frac {F}{m} \cdot \nabla_ {v} f = 0,\tag{1.1}
$$

where$f = f ( t , x , v ) \geqslant 0$is the density of electrons in phase space (x is the position and v the velocity), m is the mass of an electron, and$F { = } F ( t , x )$is the mean-field (self-consistent) electrostatic force:

$$
F = - e E, \quad E = \nabla \Delta^ {- 1} (4 \pi \varrho).\tag{1.2}
$$

Here$e > 0$is the absolute electron charge,$E = E ( t , x )$is the electric field, and${ \varrho = \varrho ( t , x ) }$ is the density of charges

$$
\varrho = \varrho_ {i} - e \int_ {\mathbb {R} ^ {3}} f d v,\tag{1.3}
$$

$\varrho _ { i }$being the density of charges due to ions. This model and its many variants are of tantamount importance in plasma physics [1], [5], [49], [54].

In contrast to models incorporating collisions [92], the Vlasov–Poisson equation is time-reversible. However, in 1946 Landau [52] stunned the physical community by pre-dicting an irreversible behavior on the basis of this equation. This “astonishing result” (as it was called in [88]) relied on the solution of the Cauchy problem for the linearized Vlasov–Poisson equation around a spatially homogeneous Maxwellian (Gaussian) equilibrium. Landau formally solved the equation by means of Fourier and Laplace transforms, and after a study of singularities in the complex plane, concluded that the electric field decays exponentially fast; he further studied the rate of decay as a function of the wave vector k. Landau’s computations are reproduced in [54, 34] and [1, 4.2].

An alternative argument appears in [54, 30]: there the thermodynamical formalism is used to compute the amount of heat$Q$which is dissipated when a (small) oscillating electric field$E ( t , x ) { = } E e ^ { i ( k \cdot x - \omega t ) }$(k is a wave vector and$\omega > 0$a frequency) is applied to a plasma whose distribution$f ^ { 0 }$is homogeneous in space and isotropic in velocity space; the result is

$$
Q = - | E | ^ {2} \frac {\pi m e ^ {2} \omega}{| k | ^ {2}} \phi^ {\prime} \bigg (\frac {\omega}{| k |} \bigg),\tag{1.4}
$$

where

$$
\phi (v _ {1}) = \int_ {\mathbb {R} ^ {3}} \int_ {\mathbb {R} ^ {3}} f ^ {0} (v _ {1}, v _ {2}, v _ {3}) d v _ {2} d v _ {3}.
$$

In particular, (1.4) is always positive (see the last remark in [54, 30]), which means that the system reacts against the perturbation, and thus possesses some “active” stabilization mechanism.

A third argument [54, 32] consists of studying the dispersion relation, or equivalently searching for the (generalized) eigenmodes of the linearized Vlasov–Poisson equation, now with complex frequency ω. After appropriate selection, these eigenmodes are all decaying (Im$\omega < 0 )$as$t \to \infty$. This again suggests stability, although in a somewhat weaker sense than the computation of heat release.

The first and third arguments also apply to the gravitational Vlasov–Poisson equation, which is the main model for non-relativistic galactic dynamics. This equation is similar to (1.1), but now m is the mass of a typical star (!), and$f$is the density of stars in phase space; moreover the first equation of (1.2) and the relation (1.3) should be replaced by

$$
F = - \mathcal {G} m E \quad \mathrm{and} \quad \varrho = m \int_ {\mathbb {R} ^ {3}} f d v,\tag{1.5}
$$

where$\mathcal { G }$is the gravitational constant,$E$is the gravitational field and$\varrho$is the density of mass. The books [9] and [10] by Binney and Tremaine constitute excellent references about the use of the Vlasov–Poisson equation in stellar dynamics—where it is often called the “collisionless Boltzmann equation”, see footnote on p. 276 in [10]. On “intermediate” time scales, the Vlasov–Poisson equation is thought to be an accurate description of very large star systems [28], which are now accessible to numerical simulations.

Since the work of Lynden-Bell [58] it has been recognized that Landau damping, and wilder collisionless relaxation processes generically dubbed “violent relaxation”, constitute a fundamental stabilizing ingredient of galactic dynamics. Without these still poorly understood mechanisms, the surprisingly short time scales for relaxation of the galaxies would remain unexplained.

One main diference between the electrostatic and the gravitational interactions is that in the latter case Landau damping should occur only at wavelengths smaller than the Jeans length [10, 5.2]; beyond this scale, even for Maxwellian velocity profiles, the Jeans instability takes over and governs planet and galaxy aggregation.(<sup>1</sup>)

On the contrary, in (classical) plasma physics, Landau damping should hold at al scales under suitable assumptions on the velocity profile; and in fact one is in general not interested in scales smaller than the Debye length, which is roughly defined in the same way as the Jeans length.

Nowadays, not only has Landau damping become a cornerstone of plasma physics,(<sup>2</sup>) but it has also made its way into other areas of physics (astrophysics, but also wind waves, fluids, superfluids, etc.) and even biophysics. One may consult the concise survey papers [76], [81] and [91] for a discussion of its influence and some applications.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>1</sup>) Or at least would do, if galactic matter was smoothly distributed; in presence of “microscopic” heterogeneities, a phase transition for aggregation can occur far below this scale [48]. In the language of statistical mechanics, the Jeans length corresponds to a “spinodal point” rather than a phase transition [87].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>2</sup>) Ryutov [81] estimated in 1998 that “approximately every third paper on plasma physics and its applications contains a direct reference to Landau damping”.</span></small>

## 1.2. Interpretation

True to his legend, Landau deduced the damping efect from a mathematical-style study,(<sup>3</sup>) without bothering to give a physical explanation of the underlying mechanism. His arguments anyway yield exact formulae, which in principle can be checked experimentally, and indeed provide good qualitative agreement with observations [59].

A first set of problems in the interpretation is related to the arrow of time. In the thermodynamic argument, the exterior field is awkwardly imposed from time onwards; moreover, reconciling a positive energy dissipation with the reversibility of the equation is not obvious. In the dispersion argument, one has to arbitrarily impose the location of the singularities taking into account the arrow of time (via the Plemelj formula); then the spectral study requires some thinking. All in all, the most convincing argument remains Landau’s original one, since it is based only on the study of the Cauchy problem, which makes more physical sense than the study of the dispersion relation (see the remark in [9, p. 682]).

A more fundamental issue resides in the use of analytic function theory, with contour integration, singularities and residue computation, which has played a major role in the theory of the Vlasov–Poisson equation ever since Landau [54, Chapter 32], see also [10, 5.2.4], and helps little, if at all, to understand the underlying physical mechanism.(<sup>4</sup>)

The most popular interpretation of Landau damping considers the phenomenon from an energetic point of view, as the result of the interaction of a plasma wave with particles of nearby velocity [36, p. 18], [10, p. 412], [1, 4.2.3], [54, p. 127]. In a nutshell, the argument says that dominant exchanges occur with those particles which are “trapped” by the wave because their velocity is close to the wave velocity. If the distribution function is a decreasing function of v , among trapped particles more are accelerated than are decelerated, so the wave loses energy to the plasma—or the plasma surfs on the wave—and the wave is damped by the interaction.

Appealing as this image may seem, to a mathematically-oriented mind it will probably make little sense at first hearing.(<sup>5</sup>) A more down-to-earth interpretation emerged in the fifties from the “wave packet” analysis of van Kampen [45] and Case [14]: Landau damping would result from phase mixing. This phenomenon, well known in galactic dynamics, describes the damping of oscillations occurring when a continuum is transported in phase space along an anharmonic Hamiltonian flow [10, pp. 379–380]. The mixing results from the simple fact that particles following diferent orbits travel at diferent angular(<sup>6</sup>) speeds, so perturbations start “spiraling” (see Figure 4.27 on p. 379 in [10]) and homogenize by fast spatial oscillation. From the mathematical point of view, phase mixing results in weak convergence; from the physical point of view, this is just the convergence of observables, defined as averages over the velocity space (this is sometimes called “convergence in the mean”).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>3</sup>) Not completely rigorous from the mathematical point of view, but formally correct, in contrast to the previous studies by Landau’s fellow physicists—as Landau himself pointed out without mercy [52].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>4</sup>) van Kampen [45] summarizes the conceptual problems posed to his contemporaries by Landau’s treatment, and comments on more or less clumsy attempts to resolve the apparent paradox caused by the singularities in the complex plane.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>5</sup>) Escande [25, Chapter 4, footnote 6] points out some misconceptions associated with the surfer image.</span></small>

At first sight, both points of view seem hardly compatible: Landau’s scenario suggests a very smooth process, while phase mixing involves tremendous oscillations. The coexistence of these two interpretations did generate some speculation on the nature of the damping, and on its relation to phase mixing, see e.g. [46] or [10, p. 413]. There is actually no contradiction between the two points of view: many physicists have rightly pointed out that Landau damping should come with filamentation and oscillations of the distribution function [45, p. 962], [54, p. 141], [1, Vol. 1, pp. 223–224], [57, pp. 294–295]. Nowadays these oscillations can be visualized spectacularly due to deterministic numerical schemes, see e.g. [95], [39, Figure 3] and [27]. In Figure 1.2 we reproduce some examples provided by Filbet.

In any case, there is still no definite interpretation of Landau damping: as noted by Ryutov [81, 9], papers devoted to the interpretation and teaching of Landau damping were still appearing regularly fifty years after its discovery; to quote just a couple of more recent examples let us mention works by Elskens and Escande [23], [24], [25]. The present paper will also contribute a new point of view.

## 1.3. Range of validity

The following issues are addressed in the literature [42], [46], [61], [95] and slightly controversial:

Does Landau damping really hold for gravitational interaction? The case seems thinner in this situation than for plasma interaction, all the more as there are many instability results in the gravitational context; up to now there has been no consensus among mathematical physicists [79]. (Numerical evidence is not conclusive because of the dificulty of accurate simulations in very large time—even in one dimension of space.)

Does the damping hold for unbounded systems? Counterexamples from [30] and [31] show that some kind of confinement is necessary, even in the electrostatic case. More precisely, Glassey and Schaefer show that a solution of the linearized Vlasov–Poisson equation in the whole space (linearized around a homogeneous equilibrium$f ^ { 0 }$of infinite mass) decays at best like$O ( t ^ { - 1 } )$, modulo logarithmic corrections, for$f ^ { 0 } ( v ) { = } c / ( 1 { + } | v | ^ { 2 } )$; and like$O ( ( \log t ) ^ { - \alpha } )$if$f ^ { 0 }$is a Gaussian. In fact, Landau’s original calculations already indicated that the damping is extremely weak at large wavenumbers; see the discussion in [54, 32]. Of course, in the gravitational case, this is even more dramatic because of the Jeans instability.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>6</sup>) “Angular” here refers to action-angle variables, and applies even for straight trajectories in a torus.</span></small>

![](images/page_8_chart_0.jpg)

![](images/page_8_chart_1.jpg)

Figure 1. A slice of the distribution function (relative to a homogeneous equilibrium) for gravitational Landau damping, at two diferent times.

Does convergence hold in infinite time for the solution of the$\mathrm { { \dot { \Omega } f u l l } } ^ { \mathrm { { \dagger } v } }$non-linear equation? This is not clear at all since there is no mechanism that would keep the distribution close to the original equilibrium for all times. Some authors do not believe that there is convergence as$t \to \infty ;$others believe that there is convergence but argue that it should be very slow [42], say$O ( 1 / t )$. In the first mathematically rigorous study of the subject, Backus [4] notes that in general the linear and non-linear evolution break apart after some (not very large) time, and questions the validity of the linearization.(<sup>7</sup>) O’Neil [75] argues that relaxation holds in the “quasilinear regime” on larger time scales, when the “trapping time” (roughly proportional the inverse square root of the size of the perturbation) is much smaller than the damping time. Other speculations and arguments related to trapping appear in many sources, e.g. [61] and [64]. Kaganovich [44] argues that non-linear efects may quantitatively afect Landau damping related phenomena by several orders of magnitude.

![](images/page_9_chart_0.jpg)

Figure 2. Time-evolution of the norm of the field, for electrostatic (left) and gravitational (right) interactions. Notice the fast Langmuir oscillations in the electrostatic case.

The so-called “quasilinear relaxation theory” [54, 49], [1, 9.1.2], [49, Chapter 10] uses second-order approximation of the Vlasov equation to predict the convergence of the spatial average of the distribution function. The procedure is most esoteric, involving averaging over statistical ensembles, and difusion equations with discontinuous coeficients, acting only near the resonance velocity for particle-wave exchanges. Because of these discontinuities, the predicted asymptotic state is discontinuous, and collisions are invoked to restore smoothness. Linear Fokker–Planck equations(<sup>8</sup>) in velocity space have also been used in astrophysics [58, p. 111], but only on phenomenological grounds (the ad-hoc addition of a friction term leading to a Gaussian stationary state); and this procedure has been exported to the study of 2-dimensional incompressible fluids [15], [16].

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>7</sup>) From the abstract: “The linear theory predicts that in stable plasmas the neglected term wil grow linearly with time at a rate proportional to the initial disturbance amplitude, destroying the validit of the linear theory, and vitiating positive conclusions about stability based on it.”</span></small>

Even if it were more rigorous, quasilinear theory only aims at second-order corrections, but the efect of higher-order perturbations might be even worse. Think of something like

$$
e ^ {- t} \sum_ {n \in \mathbb {N} _ {0}} \frac {\varepsilon^ {n} t ^ {n}}{\sqrt {n !}}
$$

(where$\mathbb { N } _ { 0 } { = } \{ 0 , 1 , 2 , \ldots \} \rangle$, then truncation at any order in ε converges exponentially fast as t , but the whole sum diverges to infinity.

Careful numerical simulation [95] seems to show that the solution of the non-linear Vlasov–Poisson equation does converge to a spatially homogeneous distribution, but only as long as the size of the perturbation is small enough. We shall call this phenomenon non-linear Landau damping. This terminology summarizes the problem well, still it is subject to criticism since (a) Landau himself sticked to the linear case and did not discuss the large-time convergence of the distribution function; (b) damping is expected to hold when the regime is close to linear, but not necessarily when the non-linear term dominates;(<sup>9</sup>) and (c) this expression is also used to designate related but diferent phenomena [1, 10.1.3]. It should be kept in mind that in the present paper, non-linearity does manifest itself, not because there is a significant initial departure from equilibrium (our initial data will be very close to equilibrium), but because we are addressing very large times, and this is all the more tricky to handle, as the problem is highly oscillating.

Is Landau damping related to the more classical notion of stability in orbital sense? Orbital stability means that the system, slightly perturbed at initial time from an equilibrium distribution, will always remain close to this equilibrium. Even in the favorable electrostatic case, stability is not granted; the most prominent phenomenon being the Penrose instability [77] according to which a distribution with two deep bumps may be unstable. In the more subtle gravitational case, various stability and instability criteria are associated with the names of Chandrasekhar, Antonov, Goodman, Doremus, Feix, Baumann, etc. [10, 7.4]. There is a widespread agreement (see e.g. the comments in [95]) that Landau damping and stability are related, and that Landau damping cannot be hoped for if there is no orbital stability.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>8</sup>) These equations act on some ensemble average of the distribution; they are diferent from the Vlasov–Landau equation.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>9</sup>) Although phase mixing might still play a crucial role in violent relaxation or other unclassified non-linear phenomena</span></small>

## 1.4. Conceptual problems

Summarizing, we can identify three main conceptual obstacles which make Landau damping mysterious, even sixty years after its discovery:

(i) The equation is time-reversible, yet we are looking for an irreversible behavior as t (or t ). The value of the entropy does not change in time, which physically speaking means that there is no loss of information in the distribution function. The spectacular experiment of the “plasma echo” illustrates this conservation of microscopic information [32], [60]: a plasma which is apparently back to equilibrium after an initial disturbance, will react to a second disturbance in a way that shows that it has not forgotten the first one.(<sup>10</sup>) And at the linear level, if there are decaying modes, there also have to be growing modes!

(ii) When one perturbs an equilibrium, there is no mechanism forcing the system to go back to this equilibrium in large time; so there is no justification in the use of linearization to predict the large-time behavior.

(iii) At the technical level, Landau damping (in Landau’s own treatment) rests on analyticity, and its most attractive interpretation is in terms of phase mixing. But both phenomena are incompatible in the large-time limit: phase mixing implies an irreversible deterioration of analyticity. For instance, it is easily checked that free transport induces an exponential growth of analytic norms as t —except if the initial datum is spatially homogeneous. In particular, the Vlasov–Poisson equation is unstable (in large time) in any norm incorporating velocity regularity. (Space-averaging is one of the ingredients used in the quasilinear theory to formally get rid of this instability.)

How can we respond to these issues?

One way to solve the first problem (time-reversibility) is to appeal to van Kampen modes as in [10, p. 415]; however these are not so physical, as noticed in [9, p. 682]. A simpler conceptual solution is to invoke the notion of weak convergence: reversibility manifests itself in the conservation of the information contained in the density function; but information may be lost irreversibly in the limit when we consider weak convergence. Weak convergence only describes the long-time behavior of arbitrary observables, each of which does not contain as much information as the density function.(<sup>11</sup>) As a very simple illustration, consider the time-reversible evolution defined by$u ( t , x ) { = } e ^ { i t x } u _ { i } ( x )$, and notice that it does converge weakly to 0 as$t \to \pm \infty$; this convergence is even exponentially fast if the initial datum$u _ { i }$is analytic. (Our example is not chosen at random: although it is extremely simple, it may be a good illustration of what happens in phase mixing.) In a way, microsocopic reversibility is compatible with macroscopic irreversibility, provided that the “microscopic regularity” is destroyed asymptotically.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>10</sup>) Interestingly enough, this experiment was suggested as a way to evaluate the strength of irreversible phenomena going on inside a plasma, e.g. the collision frequency, by measuring attenuations with respect to the predicted echo. See [86] for an interesting application and striking pictures.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>11</sup>) In Lynden-Bell’s appealing words [57, p. 295], “a system whose density has achieved a steady</span></small>

Still in respect to this reversibility, it should be noted that the “dual” mechanism of radiation, according to which an infinite-dimensional system may lose energy towards very large scales, is relatively well understood and recognized as a crucial stability mechanism [3], [85].

The second problem (lack of justification of the linearization) only indicates that there is a wide gap between the understanding of linear Landau damping, and that of the non-linear phenomenon. Even if unbounded corrections appear in the linearization procedure, the efect of the large terms might be averaged over time or other variables.

The third problem, maybe the most troubling from an analyst’s perspective, does not dismiss the phase mixing explanation, but suggests that we shall have to keep track of the initial time, in the sense that a rigorous proof cannot be based on the propagation of some phenomenon. This situation is of course in sharp contrast with the study of dissipative systems possessing a Lyapunov functional, as do many collisional kinetic equations [92], [93]; it will require completely diferent mathematical techniques.

## 1.5. Previous mathematical results

At the linear level, the first rigorous treatments of Landau damping were performed in the sixties; see Saenz [82] for rather complete results and a review of earlier works. The theory was rediscovered and renewed at the beginning of the eighties by Degond [20], and Maslov and Fedoryuk [63]. In all these works, analytic arguments play a crucial role (for instance for the analytic extension of resolvent operators), and asymptotic expansions for the electric field associated with the linearized Vlasov–Poisson equation are obtained.

Also at the linearized level, there are counterexamples by Glassey–Schaefer [30], [31] showing that there is in general no exponential decay for the linearized Vlasov–Poisson equation without analyticity, or without confining.

In a non-linear setting, the only rigorous treatments so far are those by Caglioti– Mafei [13], and later Hwang–V´elazquez [41]. Both sets of authors work in the 1- dimensional torus and use fixed-point theorems and perturbative arguments to prove the existence of a class of analytic solutions behaving, asymptotically as$t \to \infty ,$and in a strong sense, like perturbed solutions of free transport. Since solutions of free transport weakly converge to spatially homogeneous distributions, the solutions constructed by this “scattering” approach are indeed damped. The weakness of these results is that they say nothing about the initial perturbations leading to such solutions, which could be very special. In other words: damped solutions do exist, but do we ever reach them?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">state will have information about its birth still stored in the peculiar velocities of its stars.”</span></small>

Sparse as it may seem, this list is kind of exhaustive. On the other hand, there is a rather large mathematical literature on the orbital stability problem, due to Guo, Rein, Strauss, Wolansky and Lemou–M´ehats–Rapha¨el. In this respect see for instance [35] for the plasma case, and [34] and [53] for the gravitational case; these sources contain many references on the subject. This body of works has confirmed the intuition of physicists, although with quite diferent methods. The gap between a formal, linear treatment and a rigorous, non-linear one is striking: compare the appendix of [34] to the rest of the paper. In the gravitational case, these works do not consider homogeneous equilibria, but only localized solutions.

Our treatment of Landau damping will be performed from scratch, and will not rely on any of these results.

## 2. Main result

## 2.1. Modeling

We shall work in adimensional units throughout the paper, in d dimensions of space and d dimensions of velocity$( d \in \mathbb { N } { = } \{ 1 , 2 , \dots \} )$.

As should be clear from our presentation in$\ S 1$, to observe Landau damping, we need to put a restriction on the length scale (anyway plasmas in experiments are usually confined). To achieve this we shall take the position space to be the d-dimensional torus of sidelength$L ,$namely$\mathbb { T } _ { L } ^ { d } { = } \mathbb { R } ^ { d } / L \mathbb { Z } ^ { d }$. This is admittedly a bit unrealistic, but it is commonly done in plasma physics (see e.g. [5]).

In a periodic setting the Poisson equation has to be reinterpreted, since$\Delta ^ { - 1 } \varrho$is not well defined unless$\int _ {  { \mathbb { T } } _ { L } ^ { d } } \varrho d x { = } 0$. The natural solution consists of removing the mean value of$\varrho ,$independently of any “neutrality” assumption. Let us sketch a justification in the important case of Coulomb interaction: due to the screening phenomenon, we may replace the Coulomb potential V by a potential$V _ { \varkappa }$exhibiting a “cutof” at large distances (typically$V _ { \varkappa }$could be of Debye type [5]; anyway the choice of approximation has no influence on the result). If$\nabla V _ { \varkappa } \in L ^ { 1 } ( \mathbb { R } ^ { d } )$, then$\nabla V _ { \varkappa } \ast \varrho$makes sense for a periodic $\varrho ,$and moreover

$$
(\nabla V _ {\varkappa} * \varrho) (x) = \int_ {\mathbb {R} ^ {d}} \nabla V _ {\varkappa} (x - y) \varrho (y) d y = \int_ {[ 0, L ] ^ {d}} \nabla V _ {\varkappa} ^ {(L)} (x - y) \varrho (y) d y,
$$

where$\begin{array} { r } { V _ { \pmb { \mathscr { \kappa } } } ^ { ( L ) } ( z ) { = } \sum _ { l \in \mathbb { Z } ^ { d } } V _ { \pmb { \mathscr { \kappa } } } ( z { + } l L ) } \end{array}$. Passing to the limit as$\varkappa { \to } 0$yields

$$
\int_ {[ 0, L ] ^ {d}} \nabla V ^ {(L)} (x - y) \varrho (y) d y = \int_ {[ 0, L ] ^ {d}} \nabla V ^ {(L)} (x - y) (\varrho - \langle \varrho \rangle) (y) d y = - \nabla \Delta_ {L} ^ {- 1} (\varrho - \langle \varrho \rangle),
$$

where$\Delta _ { L } ^ { - 1 }$is the inverse Laplace operator on$\mathbb { T } _ { L } ^ { d }$

In the case of galactic dynamics there is no screening; however it is customary to remove the zeroth-order term of the density. This is known as the Jeans swindle, a trick considered as eficient but logically absurd. In 2003, Kiessling [47] reopened the case and acquitted Jeans, on the basis that his “swindle” can be justified by a simple limit procedure, similar to the one presented above; however, the physical basis for the limit is less transparent and subject to debate. For our purposes, it does not matter much: since anyway periodic boundary conditions are not realistic in a cosmological setting, we may just as well say that we adopt the Jeans swindle as a simple phenomenological model.

More generally, we may consider any interaction potential$W$on$\mathbb { T } _ { L } ^ { d }$, satisfying the natural symmetry assumption$W ( - z ) { = } W ( z )$(that is, W is even), as well as certain regularity assumptions. Then the self-consistent field will be given by

$$
F = - \nabla W * \varrho , \quad \varrho (x) = \int_ {\mathbb {R} ^ {d}} f (x, v) d v,
$$

where now denotes the convolution on$\mathbb { T } _ { L } ^ { d }$

In accordance with our conventions from Appendix A.3, we shall write

$$
\widehat {W} ^ {(L)} (k) = \int_ {\mathbb {T} _ {L} ^ {d}} e ^ {- 2 i \pi k \cdot x / L} W (x) d x.
$$

In particular, if$W$is the periodization of a potential$\mathbb { R } ^ { d }$<sup>R</sup> (still denoted$W$by abuse of notation), i.e.,

$$
W (x) = W ^ {(L)} (x) = \sum_ {l \in \mathbb {Z} ^ {d}} W (x + l L),
$$

then

$$
\widehat {W} ^ {(L)} (k) = \widehat {W} \left(\frac {k}{L}\right),\tag{2.1}
$$

where

$$
\widehat {W} (\xi) = \int_ {\mathbb {R} ^ {d}} e ^ {- 2 i \pi \xi \cdot x} W (x) d x
$$

is the original Fourier transform in the whole space.

## 2.2. Linear damping

It is well known that Landau damping requires some stability assumptions on the unperturbed homogeneous distribution function, say$f ^ { 0 } ( v )$. In this paper we shall use a very general assumption, expressed in terms of the Fourier transform

$$
\tilde {f} ^ {0} (\eta) = \int_ {\mathbb {R} ^ {d}} e ^ {- 2 i \pi \eta \cdot v} f ^ {0} (v) d v,\tag{2.2}
$$

the length$L ,$and the interaction potential W. To state it, we define, for$t \geqslant 0$and$k \in  { \mathbb { Z } ^ { d } }$,

$$
K ^ {0} (t, k) = - 4 \pi^ {2} \widehat {W} ^ {(L)} (k) \tilde {f} ^ {0} \left(\frac {k t}{L}\right) \frac {| k | ^ {2} t}{L ^ {2}};\tag{2.3}
$$

and, for any$\xi \in \mathbb { C }$, we define a function$\mathcal { L }$via the following Fourier–Laplace transform of $K ^ { 0 }$in the time variable:

$$
\mathcal {L} (\xi , k) = \int_ {0} ^ {\infty} e ^ {2 \pi \xi^ {*} | k | t / L} K ^ {0} (t, k) d t,\tag{2.4}
$$

where$\xi ^ { * }$is the complex conjugate to$\xi .$Our linear damping condition is expressed as follows:

(L) There are constants$C _ { 0 } , \lambda , \varkappa { > } 0$such that$| \tilde { f } ^ { 0 } ( \eta ) | \leqslant C _ { 0 } e ^ { - 2 \pi \lambda | \eta | }$for any$\eta \in \mathbb { R } ^ { d }$; and for any$\xi \in \mathbb { C }$with$0 \leqslant \operatorname { R e } \xi < \lambda$,

$$
\inf _ {k \in \mathbb {Z} ^ {d}} | \mathcal {L} (\xi , k) - 1 | \geqslant \varkappa .
$$

We shall prove in 3 that (L) implies Landau damping. For the moment, let us give a few suficient conditions for (L) to be satisfied. The first one can be thought of as a smallness assumption on either the length, or the potential, or the velocity distribution. The other conditions involve the marginals of$f ^ { 0 }$along arbitrary wave vectors k:

$$
\varphi_ {k} (v) = \int_ {k v / | k | + k ^ {\perp}} f ^ {0} (w) d w, \quad v \in \mathbb {R}.\tag{2.5}
$$

All studies known to us are based on one of these assumptions, so (L) appears as a unifying condition for linear Landau damping around a homogeneous equilibrium.

Proposition 2.1. Let$f ^ { 0 } = f ^ { 0 } ( \boldsymbol { v } )$be a velocity distribution such that$\tilde { f } ^ { 0 }$decays exponentially fast at infinity, let$L > 0$and let W be an even interaction potential on$\mathbb { T } _ { L } ^ { d }$ $W \in L ^ { 1 } (  { \mathbb { T } } ^ { d } )$. If any of the following conditions is satisfied:

(a) smallness:

$$
4 \pi^ {2} \Big (\max _ {k \in \mathbb {Z} _ {*} ^ {d}} | \widehat {W} ^ {(L)} (k) | \Big) \sup _ {| \sigma | = 1} \int_ {0} ^ {\infty} | \tilde {f} ^ {0} (r \sigma) | r d r <   1;\tag{2.6}
$$

(b) repulsive interaction and decreasing marginals: for all$k \in  { \mathbb { Z } ^ { d } }$and$v \in \mathbb { R }$

$$
\widehat {W} ^ {(L)} (k) \geqslant 0 \quad a n d \quad \varphi_ {k} ^ {\prime} (v) \left\{ \begin{array}{l l} > 0, & i f v <   0, \\ <   0, & i f v > 0, \end{array} \right.\tag{2.7}
$$

(c) generalized Penrose condition on marginals: for all$k \in  { \mathbb { Z } ^ { d } }$2

$$
\varphi_ {k} ^ {\prime} (w) = 0 \implies \widehat {W} ^ {(L)} (k) \left(\text { p.v. } \int_ {\mathbb {R}} \frac {\varphi_ {k} ^ {\prime} (v)}{v - w}   d v\right) <   1 \quad \text { for   all   } w \in \mathbb {R};\tag{2.8}
$$

then (L) holds true for some$C _ { 0 } , \lambda , \varkappa { > } 0$

Remark 2.2. ([54, problem in 30]) If$f ^ { 0 }$is radially symmetric and positive, and $d { \geqslant } 3$, then all marginals of$f ^ { 0 }$are decreasing functions of v . Indeed, if

$$
\varphi (v) = \int_ {\mathbb {R} ^ {d - 1}} f \left(\sqrt {v ^ {2} + | w | ^ {2}}\right) d w,
$$

then after diferentiation and integration by parts we find that

$$
\varphi^ {\prime} (v) = \left\{ \begin{array}{l l} - (d - 3) v \int_ {\mathbb {R} ^ {d - 1}} f \big (\sqrt {v ^ {2} + | w | ^ {2}} \big)   \frac {d w}{| w | ^ {2}}, & \text { if } d \geqslant 4, \\ - 2 \pi v f (| v |), & \text { if } d = 3. \end{array} \right.
$$

Example 2.3. Take a gravitational interaction and Mawellian background:

$$
\widehat {W} (k) = - \frac {\mathcal {G}}{\pi | k | ^ {2}} \quad \mathrm{and} \quad f ^ {0} (v) = \varrho^ {0} \frac {e ^ {- | v | ^ {2} / 2 T}}{(2 \pi T) ^ {d / 2}}.
$$

Recalling (2.1), we see that (2.6) becomes

$$
L <   \sqrt {\frac {\pi T}{\mathcal {G} \varrho^ {0}}} =: L _ {J} (T, \varrho^ {0}).\tag{2.9}
$$

The length$L _ { J }$is the celebrated Jeans length [10], [47], so criterion (a) can be applied, all the way up to the onset of the Jeans instability.

Example 2.4. If we replace the gravitational interaction by the electrostatic interaction, the same computation yields

$$
L <   \sqrt {\frac {\pi T}{e ^ {2} \varrho^ {0}}} =: L _ {D} (T, \varrho^ {0}),\tag{2.10}
$$

and now$L _ { D }$is essentially the Debye length. Then criterion (a) becomes quite restrictive, but because the interaction is repulsive we can use criterion (b) as soon as$f ^ { 0 }$is a strictly monotone function of v ; this covers in particular Maxwellian distributions, independently of the size of the box. Criterion (b) also applies if$d { \geqslant } 3$and$f ^ { 0 }$has radial symmetry. For a given$L > 0$, the condition (L) being open, it will also be satisfied if$f ^ { 0 }$is a small (analytic) perturbation of a profile satisfying (b); this includes the so-called “small bump on tail” stability. Then if the distribution presents two large bumps, the Penrose instability will take over.

Example 2.5. For the electrostatic interaction in dimension 1, (2.8) becomes

$$
(f ^ {0}) ^ {\prime} (w) = 0 \quad \Longrightarrow \quad \int_ {\mathbb {R}} \frac {(f ^ {0}) ^ {\prime} (v)}{v - w} d v <   \frac {\pi}{e ^ {2} L ^ {2}}.\tag{2.11}
$$

This is a variant of the Penrose stability condition [77]. This criterion is in general sharp for linear stability (up to the replacement of the strict inequality by the non-strict one, and assuming that the critical points of$f ^ { 0 }$are non-degenerate); see [55, Appendix] for precise statements.

We shall show in 3 that (L) implies linear Landau damping (Theorem 3.1); then we shall prove Proposition 2.1 at the end of that section. The general ideas are close to those appearing in previous works, including Landau himself; the only novelties lie in the more general assumptions, the elementary nature of the arguments, and the slightly more precise quantitative results.

## 2.3. Non-linear damping

As others have done before in the study of the Vlasov–Poisson equation [13], we shal quantify the analyticity by means of natural norms involving Fourier transform in both variables (also denoted with a tilde in the sequel). So we define

$$
\| f\|_{\lambda ,\mu} = \sup_{\substack{k\in \mathbb{Z}^{d}\\ \eta \in \mathbb{R}^{d}}}|\tilde{f}^{(L)}(k,\eta)|e^{2\pi \lambda |\eta |}e^{2\pi \mu |k| / L},\tag{2.12}
$$

where k varies in$\mathbb { Z } ^ { d } , \eta \in \mathbb { R } ^ { d }$, λ and μ are positive parameters, and we recall the dependence of the Fourier transform on L (see Appendix A.3 for conventions). Now we can state our main result as follows.

Theorem 2.6. (Non-linear Landau damping) Let$f ^ { 0 } \colon  { \mathbb { R } ^ { d } } \to  { \mathbb { R } }$be an analytic velocity profile. Let$L > 0$and let$W : \mathbb { T } _ { L } ^ { d } \to \mathbb { R }$be an even interaction potential satisfying

$$
| \widehat {W} ^ {(L)} (k) | \leqslant \frac {C _ {W}}{| k | ^ {1 + \gamma}} \quad f o r a l l k \in \mathbb {Z} ^ {d}\tag{2.13}
$$

for some constants$C _ { W } > 0$and$\gamma \geqslant 1$. Assume that$f ^ { 0 }$and W satisfy the stability condition (L) from 2.2, with some constants$\lambda , \varkappa > 0$; further assume that, for the same parameter λ,

$$
\sup _ {\eta \in \mathbb {R} ^ {d}} | \tilde {f} ^ {0} (\eta) | e ^ {2 \pi \lambda | \eta |} \leqslant C _ {0} \quad a n d \quad \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \| \nabla_ {v} ^ {n} f ^ {0} \| _ {L ^ {1} (\mathbb {R} ^ {d})} \leqslant C _ {0} <   \infty .\tag{2.14}
$$

Then for any$0 { < } \lambda ^ { \prime } { < } \lambda , \beta { > } 0$and$0 < \mu ^ { \prime } < \mu .$, there is

$$
\varepsilon = \varepsilon (d, L, C _ {W}, C _ {0}, \varkappa , \lambda , \lambda^ {\prime}, \mu , \mu^ {\prime}, \beta , \gamma)
$$

with the following property: if$f _ { i } = f _ { i } ( x , v )$is an initial datum satisfying

$$
\delta := \| f _ {i} - f ^ {0} \| _ {\lambda , \mu} + \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} | f _ {i} - f ^ {0} | e ^ {\beta | v |} d v d x \leqslant \varepsilon ,\tag{2.15}
$$

then

the unique classical solution f to the non-linear Vlasov equation

$$
\frac {\partial f}{\partial t} + v \cdot \nabla_ {x} f - (\nabla W * \varrho) \cdot \nabla_ {v} f = 0, \quad \varrho = \int_ {\mathbb {R} ^ {d}} f d v,\tag{2.16}
$$

with initial datum$f ( 0 , \cdot ) { = } f _ { i }$, converges in the weak topology as$t \to \pm \infty ,$, with rate $O ( e ^ { - 2 \pi \lambda ^ { \prime } | t | } )$, to a spatially homogeneous equilibrium$f _ { \pm \infty }$(that is, it converges to$f _ { \infty }$ as$t \to \infty ,$, and to$f _ { - \infty } \ a s \ t {  } { - \infty } )$;

the distribution function composed with the backward free transport$f ( t , x + v t , v )$ converges strongly to$f _ { \pm \infty }$as$t \to \pm \infty ;$

the density$\scriptstyle \varrho ( t , x ) = \int _ { \mathbb { R } ^ { d } } f ( t , x , v )$) dv converges in the strong topology as$t \to \pm \infty$, with rate$O ( e ^ { - 2 \pi \lambda ^ { \prime } | t | } )$, to the constant density

$$
\varrho_ {\infty} = \frac {1}{L ^ {d}} \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x, v) d v d x;
$$

in particular the force$F { = } { - } \nabla W * \varrho$converges exponentially fast to$0 ;$

the space average$\textstyle \langle f \rangle ( t , v ) = \int _ { \mathbb { T } _ { r } ^ { d } } f ( t , x , v )$) dx converges in the strong topology as $t \to \pm \infty ,$, with rate$O ( e ^ { - 2 \pi \lambda ^ { \prime } | t | } )$, to$f _ { \pm \infty }$L

More precisely, there are$C { > } 0 .$, and spatially homogeneous distributions$f _ { \infty } ( v )$and $f _ { - \infty } ( v )$, depending continuously on$f _ { i }$and W, such that

$$
\begin{array}{c} \sup _ {t \in \mathbb {R}} \| f (t, x + v t, v) - f ^ {0} (v) \| _ {\lambda^ {\prime}, \mu^ {\prime}} \leqslant C \delta , \\ | \tilde {f} _ {\pm \infty} (\eta) - \tilde {f} ^ {0} (\eta) | \leqslant C \delta e ^ {- 2 \pi \lambda^ {\prime} | \eta |} \quad \text { for all } \eta \in \mathbb {R} ^ {d} \end{array}\tag{2.17}
$$

and

$$
\left| L ^ {- d} \tilde {f} ^ {(L)} (t, k, \eta) - \tilde {f} _ {\pm \infty} (\eta) 1 _ {k = 0} \right| = O \left(e ^ {- 2 \pi \lambda^ {\prime} | t | / L}\right) \quad a s t \rightarrow \pm \infty , f o r a l l (k, \eta) \in \mathbb {Z} ^ {d} \times \mathbb {R} ^ {d},
$$

$$
\| f (t, x + v t, v) - f _ {\pm \infty} (v) \| _ {\lambda^ {\prime}, \mu^ {\prime}} = O (e ^ {- 2 \pi \lambda^ {\prime} | t | / L}) \quad a s t \to \pm \infty ,
$$

$$
\| \varrho (t, \cdot) - \varrho_ {\infty} \| _ {C ^ {r} (\mathbb {T} ^ {d})} = O (e ^ {- 2 \pi \lambda^ {\prime} | t | / L}) \quad a s | t | \to \infty , f o r a l l r \in \mathbb {N},\tag{2.18}
$$

$$
\| F (t, \cdot) \| _ {C ^ {r} (\mathbb {T} ^ {1} d)} = O (e ^ {- 2 \pi \lambda^ {\prime} | t | / L}) \quad a s | t | \to \infty , f o r a l l r \in \mathbb {N},\tag{2.19}
$$

$$
\| \langle f (t, \cdot , v) \rangle - f _ {\pm \infty} \| _ {C _ {\sigma} ^ {r} (\mathbb {R} _ {v} ^ {d})} = O (e ^ {- 2 \pi \lambda^ {\prime} | t | / L}) \quad \text { as } t \to \pm \infty , \text { for   all } r \in \mathbb {N} \text { and } \sigma > 0.\tag{2.20}
$$

In this statement$C ^ { r }$stands for the usual norm on r-times continuously diferentiable functions, and$C _ { \sigma } ^ { r }$involves in addition moments of order$\sigma ,$namely

$$
\| f\|_{C^{\frac{r}{\sigma}}} = \sup_{\substack{r^{\prime}\leqslant r\\ v\in \mathbb{R}^{d}}}|f^{(r^{\prime})}(v)(1 + |v|^{\sigma})|.
$$

These results can be reformulated in a number of alternative norms, both for the strong and for the weak topology.

## 2.4. Comments

Let us start with a list of remarks about Theorem 2.6.

The decay of the force field, statement (2.19), is the experimentally measurable phenomenon which may be called Landau damping.

Since the energy

$$
E = \frac {1}{2} \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {T} _ {L} ^ {d}} \varrho (x) \varrho (y) W (x - y) d x d y + \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f (x, v) \frac {| v | ^ {2}}{2} d v d x
$$

(= potential + kinetic energy) is conserved by the non-linear Vlasov evolution, there is a conversion of potential energy into kinetic energy as t (kinetic energy goes up for Coulomb interaction and goes down for Newton interaction). Similarly, the entropy

$$
S = - \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f \log f d v d x = - \left(\int_ {\mathbb {T} _ {L} ^ {d}} \varrho \log \varrho d x + \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f \log \frac {f}{\varrho} d v d x\right)
$$

(= spatial + kinetic entropy) is preserved, and there is a transfer of information from spatial to kinetic variables in large time.

Our result covers both attractive and repulsive interactions, as long as the linear damping condition is satisfied; it covers the Newton–Coulomb potential as a limit case $( \gamma = 1$in (2.13)). The proof breaks down for$\gamma < 1 ;$this is a non-linear efect, as any$\gamma > 0$ would work for the linearized equation. The singularity of the interaction at short scales will be the source of important technical problems.(<sup>12</sup>)

Condition (2.14) could be replaced by

$$
| \tilde {f} ^ {0} (\eta) | \leqslant C _ {0} e ^ {- 2 \pi \lambda | \eta |} \quad \mathrm{and} \quad \int_ {\mathbb {R} ^ {d}} f ^ {0} (v) e ^ {\beta | v |} d v \leqslant C _ {0}.\tag{2.21}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>12</sup>) In a related subject, this singularity is also the reason why the Vlasov–Poisson equation is stil far from being established as a mean-field limit of particle dynamics (see [37] for partial results covering much less singular interactions).</span></small>

But condition (2.14) is more general, in view of Theorem 4.20 below. For instance, $f ^ { 0 } ( v ) { = } 1 / ( 1 { + } v ^ { 2 } )$in dimension d=1 satisfies (2.14) but not (2.21); this distribution is commonly used in theoretical and numerical studies, see e.g. [39]. We shall also establish slightly more precise estimates under slightly more stringent conditions on$f ^ { 0 } ,$, see (12.1).

Our conditions are expressed in terms of the initial datum, which is a considerable improvement over [13] and [41]. Still it is of interest to pursue the “scattering” program started in [13], e.g. in hope of better understanding of the non-perturbative regime.

The smallness assumption on$f _ { i } - f ^ { 0 }$is expected, for instance in view of the work of O’Neil [75], or the numerical results of [95]. We also make the standard assumption that$f _ { i } - f ^ { 0 }$is well localized.

No convergence can be hoped for if the initial datum is only close to$f ^ { 0 }$in the weak topology: indeed there is instability in the weak topology, even around a Maxwellian [13].

The well-posedness of the non-linear Vlasov–Poisson equation in dimension d3 was established by Pfafelmoser [78] and Lions–Perthame [56] in the whole space. Pfaffelmoser’s proof was adapted to the case of the torus by Batt and Rein [6]; however, like Pfafelmoser, these authors imposed a stringent assumption of uniformly bounded velocities. Building on Schaefer’s simplification [84] of Pfafelmoser’s argument, Horst [40] proved well-posedness in the whole space assuming only inverse polynomial decay in the velocity variable. Although this has not been done explicitly, Horst’s proof can easily be adapted to the case of the torus, and covers in particular the setting which we use in the present paper. (The adaptation of [56] seems more delicate.) Propagation of analytic regularity is not studied in these works. In any case, our proof will provide a new perturbative existence theorem, together with regularity estimates which are considerably stronger than what is needed to prove the uniqueness. We shall not come back to these issues which are rather irrelevant for our study: uniqueness only needs local-in-time regularity estimates, while all the dificulty in the study of Landau damping consists in handling (very) large time.

We note in passing that while blow-up is known to occur for certain solutions of the Newtonian Vlasov–Poisson equation in dimension 4, blow-up does not occur in this perturbative regime, whatever the dimension. There is no contradiction since blow-up solutions are constructed with negative energy initial data, and a nearly homogeneous solution automatically has positive energy. (Also, blow-up solutions have been constructed only in the whole space, where the virial identity is available; but it is plausible, although not obvious, that blow-up is still possible in bounded geometry.)

$f ( t , \cdot )$is not close to$f ^ { 0 }$in analytic norm as$t \to \infty$, and does not converge to anything in the strong topology, so the conclusion cannot be improved much. Still we shall establish more precise quantitative results, and the limit profiles$f _ { \pm \infty }$are obtained

by a constructive argument.

Estimate (2.17) expresses the orbital “traveling stability” around$f ^ { 0 } ;$it is much stronger than the usual orbital stability in Lebesgue norms [34], [35]. An equivalent formulation is that if$( T _ { t } ) _ { t \in \mathbb { R } }$stands for the non-linear Vlasov evolution operator, and $( T _ { t } ^ { 0 } ) _ { t \in \mathbb { R } }$for the free transport operator, then in a neighborhood of a homogeneous equilibrium satisfying the stability criterion (L),$T _ { - t } ^ { 0 } \circ T _ { t }$remains uniformly close to Id for al t. Note the important diference: unlike in the usual orbital stability theory, our conclusions are expressed in functional spaces involving smoothness, which are not invariant under the free transport semigroup. This a source of dificulty (our functional spaces are sensitive to the filamentation phenomenon), but it is also the reason for which this “analytic” orbital stability contains much more information, and in particular the damping of the density.

Compared with known non-linear stability results, and even forgetting about the smoothness, estimate (2.17) is new in several respects. In the context of plasma physics, it is the first one to prove stability for a distribution which is not necessarily a decreasing function of v (“small bump on tail”); while in the context of astrophysics, it is the first one to establish stability of a homogeneous equilibrium against periodic perturbations with wavelength smaller than the Jeans length.

While analyticity is the usual setting for Landau damping, both in mathematical and physical studies, it is natural to ask whether this restriction can be dispensed with. (This can be done only at the price of losing the exponential decay.) In the linear case, this is easy, as we shall recall later in Remark 3.5; but in the non-linear setting, leaving the analytic world is much more tricky. In 13, we shall present the first results in this direction.

With respect to the questions raised above, our analysis brings the following answers:

(a) Convergence of the distribution f does hold for t ; it is indeed based on phase mixing, and therefore involves very fast oscillations. In this sense it is right to consider Landau damping as a “wild” process. But on the other hand, the spatial density (and therefore the force field) converges strongly and smoothly.

(b) The space average f does converge in large time. However the conclusions are quite diferent from those of quasilinear relaxation theory, since there is no need for extra randomness, and the limiting distribution is smooth, even without collisions.

(c) Landau damping is a linear phenomenon, which survives non-linear perturbation due to the structure of the Vlasov–Poisson equation. The non-linearity manifests itself by the presence of echoes. Echoes were well known to specialists of plasma physics [54, 35], [1, 12.7], but were not identified as a possible source of unstability. Controlling the echoes will be a main technical dificulty; but the fact that the response appears in this form, with an associated time-delay and localized in time, will in the end explain the stability of Landau damping. These features can be expected in other equations exhibiting oscillatory behavior.

(d) The large-time limit is in general diferent from the limit predicted by the linearized equation, and depends on the interaction and initial datum (more precise statements will be given in 14); still the linearized equation, or higher-order expansions, do provide a good approximation. We shall also set up a systematic recipe for approximating the large-time limit with arbitrarily high precision as the strength of the perturbation becomes small. This justifies a posteriori many known computations.

(e) From the point of view of dynamical systems, the non-linear Vlasov equation exhibits a truly remarkable behavior. It is not uncommon for a Hamiltonian system to have many, or even countably many heteroclinic orbits (there are various theories for this, a popular one being the Melnikov method); but in the present case we see that heteroclinic/homoclinic orbits(<sup>13</sup>) are so numerous as to fill up a whole neighborhood of the equilibrium. This is possible only because of the infinite-dimensional nature of the system, and the possibility to work with non-equivalent norms; such a behavior has already been reported for other systems [50], [51], in relation with infinite-dimensional KAM (Kolmogorov–Arnold–Moser) theory.

(f) As a matter of fact, non-linear Landau damping has strong similarities with the KAM theory. It has been known since the early days of the theory that the linearized Vlasov equation can be reduced to an infinite system of uncoupled Volterra equations, which makes this equation completely integrable in some sense. (Morrison [66] gave a more precise meaning to this property.) To see a parallel with classical KAM theory, one step of our result is to prove the preservation of the phase-mixing property under non-linear perturbation of the interaction. (Although there is no ergodicity in phase space, the mixing will imply an ergodic behavior for the spatial density.) The analogy is reinforced by the fact that the proof of Theorem 2.6 shares many features with the proof of the KAM theorem in the analytic (or Gevrey) setting. (Our proof is close to Kolmogorov’s original argument, exposed in [18].) In particular, we shall invoke a Newton scheme to overcome a loss of “regularity” in analytic norms, only in a trickier sense than in KAM theory. If one wants to push the analogy further, one can argue that the resonances which cause the phenomenon of small divisors in KAM theory find an analogue in the time-resonances which cause the echo phenomenon in plasma physics. A notable diference is that in the present setting, time-resonances arise from the non-linearity at the level of the partial diferential equation, whereas small divisors in KAM theory arise at the level of the ordinary diferential equation. Another major diference is that in the present situation there is a time-averaging which is not present in KAM theory.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>13</sup>) Here we use these words just to designate solutions connecting two distinct/equal equilibria, without any mention of stable or unstable manifolds.</span></small>

Thus we see that three of the most famous paradoxical phenomena from twentieth century classical physics: Landau damping, echoes and the KAM theorem are intimately related (only in the non-linear variant of Landau’s linear argument!). This relation, which we did not expect, is one of the main discoveries of the present paper.

## 2.5. Interpretation

A successful point of view adopted in this paper is that Landau damping is a relaxation by smoothness and by mixing. In a way, phase mixing converts the smoothness into decay. Thus Landau damping emerges as a rare example of a physical phenomenon in which regularity is not only crucial from the mathematical point of view, but also can be “measured” by a physical experiment.

## 2.6. Main ingredients

Some of our ingredients are similar to those in [13]: in particular, the use of the Fourier transform to quantify analytic regularity and to implement phase mixing. New ingredients used in our work include the following.

The introduction of a time-shift parameter to keep memory of the initial time ( 4 and 5), thus getting uniform estimates in spite of the loss of regularity in large time. We call this the gliding regularity: it shifts in phase space from low to high modes. Gliding regularity automatically comes with an improvement of the regularity in x, and a deterioration of the regularity in v, as time passes by.

The use of carefully designed flexible analytic norms behaving well with respect to composition ( 4). This requires care, because analytic norms are very sensitive to composition, contrary to, say, Sobolev norms.

A control of the deflection of trajectories induced by the force field, to reduce the problem to homogenization of free flow ( 5) via composition. The physical meaning is the following: when a background with gliding regularity acts on (say) a plasma, the trajectories of plasma particles are asymptotic to free transport trajectories.

New functional inequalities of bilinear type, involving analytic functional spaces, integration in time and velocity variables, and evolution by free transport ( 6). These inequalities morally mean the following: when a plasma acts (by forcing) on a smooth background of particles, the background reacts by lending a bit of its (gliding) regularity to the plasma, uniformly in time. Eventually the plasma will exhaust itself (the force will decay). This most subtle efect, which is at the heart of Landau’s damping, will be mathematically expressed in the formalism of analytic norms with gliding regularity.

A new analysis of the time response associated with the Vlasov–Poisson equation ( 7), aimed ultimately at controlling the self-induced echoes of the plasma. For any interaction less singular than that of Coulomb–Newton, this will be done by analyzing time-integral equations involving a norm of the spatial density. To treat the Coulomb– Newton potential we shall refine the analysis, considering individual modes of the spatial density.

A Newton iteration scheme, solving the non-linear evolution problem as a succession of linear ones ( 10). Picard iteration schemes still play a role, since they are run at each step of the iteration process, to estimate the deflection.

It is only in the linear study of 3 that the length scale L will play a crucial role, via the stability condition (L). In all the rest of the paper we shall normalize L to 1 for simplicity.

## 2.7. About phase mixing

A physical mechanism transferring energy from large scales to very fine scales, asymptotically in time, is sometimes called weak turbulence. Phase mixing provides such a mechanism, and in a way our study shows that the Vlasov–Poisson equation is subject to weak turbulence. But the phase mixing interpretation provides a more precise picture. While one often sees weak turbulence as a “cascade” from low to high Fourier modes, the relevant picture would rather be a 2-dimensional figure with an interplay between spatial Fourier modes and velocity Fourier modes. More precisely, phase mixing transfers the energy from each non-zero spatial frequency k, to large velocity frequences η, and this transfer occurs at a speed proportional to k. This picture is clear from the solution of free transport in Fourier space, and is illustrated in Figure 3. (Note the resemblance with a shear flow.) So there is transfer of energy from one variable (here x) to another (here v); homogenization in the first variable going together with filamentation in the second one. The same mechanism may also underlie other cases of weak turbulence.

The fact that the high modes are ultimately damped by some “random” microscopic process (collisions, difusion, etc.) not described by the Vlasov–Poisson equation is certainly undisputed in plasma physics [54, 41],(<sup>14</sup>) but is the object of debate in galactic dynamics; anyway this is a diferent story. Some mathematical statistical theories of Euler and Vlasov–Poisson equations do postulate the existence of some small-scale coarse graining mechanism, but resulting in mixing rather than dissipation [80], [90].

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>14</sup>) See [54, Problem 41]: due to Landau damping, collisions are expected to smooth the distribution quite eficiently; this is a hypoellipticity issue.</span></small>

![](images/page_25_image_0.jpg)

initial configuration (t=0)

Figure 3. Schematic picture of the evolution of energy by free transport, or perturbation thereof; marks indicate localization of energy in phase space. The energy of the spatial mode k is concentrated in large time around η kt.

![](images/page_25_image_3.jpg)

Figure 4. The distribution function in phase space (position, velocity) at a given time; notice how the fast oscillations in v contrast with the slower variations in x.

## 3. Linear damping

In this section we establish Landau damping for the linearized Vlasov equation. Beforehand, let us recall that the free transport equation

$$
\frac {\partial f}{\partial t} + \boldsymbol {v} \cdot \nabla_ {\boldsymbol {x}} f = 0\tag{3.1}
$$

has a strong mixing property: any solution of (3.1) converges weakly in large time to a spatially homogeneous distribution equal to the space-averaging of the initial datum.

Let us sketch the proof.

If$f$solves (3.1) in$\mathbb { T } ^ { d } \times \mathbb { R } ^ { d }$, with initial datum$f _ { i } { = } f ( 0 , \cdot )$, then

$$
f (t, x, v) = f _ {i} (x - v t, v),
$$

so the space-velocity Fourier transform of$f$is given by the formula

$$
\tilde {f} (t, k, \eta) = \tilde {f} _ {i} (k, \eta + k t).\tag{3.2}
$$

On the other hand, if$f _ { \infty }$is defined by

$$
f _ {\infty} (v) = \langle f _ {i} (\cdot , v) \rangle = \int_ {\mathbb {T} ^ {d}} f _ {i} (x, v) d x,
$$

then$\widetilde { f } _ { \infty } ( k , \eta ) = \widetilde { f } _ { i } ( 0 , \eta ) 1 _ { k = 0 }$. So, by the Riemann–Lebesgue lemma, for any fixed$( k , \eta )$ we have

$$
| \tilde {f} (t, k, \eta) - \tilde {f} _ {\infty} (k, \eta) | \to 0 \quad \mathrm{as} | t | \to \infty ,
$$

which shows that$f$converges weakly to$f _ { \infty }$. The convergence holds as soon as$f _ { i }$is merely integrable; and by (3.2), the rate of convergence is determined by the decay of $\tilde { f } _ { i } ( k , \eta ) \mathrm { a s } | \eta | \mathrm { \to } \infty$, or equivalently the smoothness in the velocity variable. In particular, the convergence is exponentially fast if (and only if)$f _ { i } ( x , v )$is analytic in v.

This argument obviously works independently of the size of the box. But when we turn to the Vlasov equation, length scales will matter, so we shall introduce a length$L { > } 0 .$ and work in$\mathbb { T } _ { L } ^ { d } { = } \mathbb { R } ^ { d } / L \mathbb { Z } ^ { d }$. Then the length scale will appear in the Fourier transform: see Appendix A.3. (This is the only section in this paper where the scale will play a non-trivial role, so in all the rest of the paper we shall take$L { = } 1 . 1$)

Any velocity distribution$f ^ { 0 } = f ^ { 0 } ( \boldsymbol { v } )$defines a stationary state for the non-linear Vlasov equation with interaction potential W. Then the linearization of that equation around$f ^ { 0 }$yields

$$
\left\{ \begin{array}{l} \frac {\partial f}{\partial t} + v \cdot \nabla_ {x} f - (\nabla W * \varrho) \cdot \nabla_ {v} f ^ {0} = 0, \\ \varrho = \int_ {\mathbb {R} ^ {d}} f d v. \end{array} \right.\tag{3.3}
$$

Note that there is no force term in (3.3), due to the fact that$f ^ { 0 }$does not depend on x. This equation describes what happens to a plasma density f which tries to force a stationary homogeneous background$f ^ { 0 } { } ;$; equivalently, it describes the reaction exerted by the background which is acted upon. (Imagine that there is an exchange of matter between the forcing gas and the forced gas, and that this exchange exactly compensates the efect of the force, so that the density of the forced gas does not change after all.)

Theorem 3.1. (Linear Landau damping) Let$f ^ { 0 } { = } f ^ { 0 } ( v ) , L { > } 0 , W { : } \mathbb { T } _ { L } ^ { d } { \to } \mathbb { R }$be such that$W ( - z ) { = } W ( z )$and$\| \nabla W \| _ { L ^ { 1 } } \leqslant C _ { W } < \infty$and let$f _ { i } { = } f _ { i } ( x , v )$be such that

(i) condition (L) from 2.2 holds for some constants$\lambda , \varkappa > 0 ;$

(ii) for all$\eta \in \mathbb { R } ^ { d } , \ | \tilde { f } ^ { 0 } ( \eta ) | \leqslant C _ { 0 } e ^ { - 2 \pi \lambda | \eta | }$for some constant$C _ { 0 } > 0 ;$

(iii) for all$k \in  { \mathbb { Z } ^ { d } }$and all$\eta \in \mathbb { R } ^ { d } , | \tilde { f } _ { i } ^ { ( L ) } ( k , \eta ) | \leqslant C _ { i } e ^ { - 2 \pi \alpha | \eta | } \ f o r \ s o m e \ \alpha , C _ { i } > 0 .$

Then, as$t \to \infty$, the solution$f ( t , \cdot )$to the linearized Vlasov equation (3.3) with initial datum$f _ { i }$converges weakly to$f _ { \infty } = \langle f _ { i } \rangle$defined by

$$
f _ {\infty} (v) = \frac {1}{L ^ {d}} \int_ {\mathbb {T} _ {L} ^ {d}} f _ {i} (x, v) d x;
$$

and$\scriptstyle \varrho ( x ) = \int _ { \mathbb { R } ^ { d } } f ( x , v )$dv converges strongly to the constant

$$
\varrho_ {\infty} = \frac {1}{L ^ {d}} \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x, v) d v d x.
$$

More precisely, for any$\lambda ^ { \prime } { < } \operatorname* { m i n } \{ \lambda , \alpha \}$,

$$
\left\{ \begin{array}{l l} \| \varrho (t, \cdot) - \varrho_ {\infty} \| _ {C ^ {r}} = O (e ^ {- 2 \pi \lambda^ {\prime} | t | / L}) & \text {for all r\in\mathbb {N}}, \\ | \tilde {f} ^ {(L)} (t, k, \eta) - \tilde {f} _ {\infty} ^ {(L)} (k, \eta) | = O (e ^ {- 2 \pi \lambda^ {\prime} | k t | / L}) & \text {for all (k,\eta)\in\mathbb {Z} ^{d} \times\mathbb {Z} ^{d}}. \end{array} \right.
$$

Remark 3.2. Even if the initial datum is more regular than analytic, the convergence will in general not be better than exponential (except in some exceptional cases [38]). See [10, pp. 414–416] for an illustration. Conversely, if the analyticity width α for the initial datum is smaller than the “Landau$\mathrm { r a t e } ^ { \prime \prime } \lambda ,$then the rate of decay will not be better than${ \cal O } ( e ^ { - \alpha t } )$. See [7] and [19] for a discussion of this fact, often overlooked in the physical literature.

Remark 3.3. The fact that the convergence is to the average of the initial datum will not survive non-linear perturbation, as shown by the counterexamples in 14.

Remark 3.4. Dimension does not play any role in the linear analysis. This can be attributed to the fact that only longitudinal waves occur, so everything happens “in the direction of the wave vector”. Transversal waves arise in plasma physics only when magnetic efects are taken into account [1, Chapter 5].

Remark 3.5. The proof can be adapted to the case when$f ^ { 0 }$and$f _ { i }$are only$C ^ { \infty }$; then the convergence is not exponential, but still$O ( t ^ { - \infty } )$. The regularity can also be further decreased, down to$W ^ { s , 1 }$, at least for any$s > 2 ;$; more precisely, if$f ^ { 0 } \in W ^ { s _ { 0 } , 1 }$and$f _ { i } \in W ^ { s _ { i } , 1 }$, there will be damping with a rate$O ( t ^ { - \varkappa } )$for any$\varkappa { < } \mathrm { m a x } \{ s _ { 0 } - 2 , s _ { i } \}$. (Compare with [1, Volume 1, p. 189].) This is independent of the regularity of the interaction.

The proof of Theorem 3.1 relies on the following elementary estimate for Volterra equations. We use the notation of 2.2.

Lemma 3.6. Assume that (L) holds true for some constants$C _ { 0 } , \varkappa , \lambda { > } 0$. Let

$$
C _ {W} = \left\| W \right\| _ {L ^ {1} (\mathbb {T} _ {L} ^ {d})}
$$

and let$K ^ { 0 }$be defined by (2.3). Then any solution$\varphi ( t , k )$of

$$
\varphi (t, k) = a (t, k) + \int_ {0} ^ {t} K ^ {0} (t - \tau , k) \varphi (\tau , k) d \tau\tag{3.4}
$$

satisfies, for any$k \in  { \mathbb { Z } ^ { d } }$and any$\lambda ^ { \prime } { < } \lambda$

$$
\sup _ {t \geqslant 0} | \varphi (t, k) | e ^ {2 \pi \lambda^ {\prime} | k | t / L} \leqslant (1 + C _ {0} C _ {W} C (\lambda , \lambda^ {\prime}, \varkappa)) \sup _ {t \geqslant 0} | a (t, k) | e ^ {2 \pi \lambda | k | t / L}.
$$

Here$C ( \lambda , \lambda ^ { \prime } , \varkappa ) { = } C ( 1 { + } \varkappa ^ { - 1 } ( 1 { + } ( \lambda { - } \lambda ^ { \prime } ) ^ { - 2 } ) )$for some universal constant C.

Remark 3.7. It is standard to solve these Volterra equations by Laplace transforms; but, with a view to the non-linear setting, we shall prefer a more flexible and quantitative approach.

Proof. If$k { = } 0$this is obvious since$K ^ { 0 } ( t , 0 ) = 0$; so we assume$k { \neq } 0$. Consider$\lambda ^ { \prime } { < } \lambda$ multiply (3.4) by$e ^ { 2 \pi \lambda ^ { \prime } | k | t / L } .$and write

$$
\Phi (t, k) = \varphi (t, k) e ^ {2 \pi \lambda^ {\prime} | k | t / L} \quad \text { and } \quad A (t, k) = a (t, k) e ^ {2 \pi \lambda^ {\prime} | k | t / L};
$$

then (3.4) becomes

$$
\Phi (t, k) = A (t, k) + \int_ {0} ^ {t} K ^ {0} (t - \tau , k) e ^ {2 \pi \lambda^ {\prime} | k | (t - \tau) / L} \Phi (\tau , k) d \tau .\tag{3.5}
$$

A particular case. The proof is extremely simple if we make the stronger assumption

$$
\int_ {0} ^ {\infty} | K ^ {0} (\tau , k) | e ^ {2 \pi \lambda^ {\prime} | k | \tau / L} d \tau \leqslant 1 - \varkappa , \quad \varkappa \in (0, 1).
$$

Then from (3.5),

$$
\begin{array}{l} \sup _ {0 \leqslant t \leqslant T} | \Phi (t, k) | \leqslant \sup _ {0 \leqslant t \leqslant T} | A (t, k) | \\ \qquad + \left(\sup _ {0 \leqslant t \leqslant T} \int_ {0} ^ {t} | K ^ {0} (t - \tau , k) | e ^ {2 \pi \lambda^ {\prime} | k | (t - \tau) / L}   d \tau\right) \sup _ {0 \leqslant \tau \leqslant T} | \Phi (\tau , k) |, \end{array}
$$

whence

$$
\sup _ {0 \leqslant \tau \leqslant t} | \Phi (\tau , k) | \leqslant \frac {\sup _ {0 \leqslant \tau \leqslant t} | A (\tau , k) |}{1 - \int_ {0} ^ {\infty} | K ^ {0} (\tau , k) | e ^ {2 \pi \lambda^ {\prime} | k | \tau / L} d \tau} \leqslant \frac {\sup _ {0 \leqslant \tau \leqslant t} | A (\tau , k) |}{\varkappa},
$$

and therefore

$$
\sup _ {t \geqslant 0} | \varphi (t, k) | e ^ {2 \pi \lambda^ {\prime} | k | t / L} \leqslant \frac {\sup _ {t \geqslant 0} | a (t , k) | e ^ {2 \pi \lambda^ {\prime} | k | t / L}}{\varkappa}.
$$

The general case. To treat the general case we take the Fourier transform in the time variable, after extending K, A and Φ by 0 at negative times. (This presentation was suggested to us by Sigal, and appears to be technically simpler than the use of the Laplace transform.) Denoting the Fourier transform with a hat and recalling (2.4), we have, for$\xi = \lambda ^ { \prime } + i \omega L / | k |$,

$$
\widehat {\Phi} (\omega , k) = \widehat {A} (\omega , k) + \mathcal {L} (\xi , k) \widehat {\Phi} (\omega , k).
$$

By assumption${ \mathcal { L } } ( \xi , k ) \neq 1$, so

$$
\widehat {\Phi} (\omega , k) = \frac {\hat {A} (\omega , k)}{1 - \mathcal {L} (\xi , k)}.
$$

From there, it is traditional to apply the Fourier (or Laplace) inversion transform. Instead, we apply Plancherel’s identity to find (for each k)

$$
\| \Phi \| _ {L ^ {2} (d t)} \leqslant \frac {\| A \| _ {L ^ {2} (d t)}}{\varkappa}.
$$

We then plug this into the equation (3.5) to get

$$
\begin{array}{c} \| \Phi \| _ {L ^ {\infty} (d t)} \leqslant \| A \| _ {L ^ {\infty} (d t)} + \| K ^ {0} e ^ {2 \pi \lambda^ {\prime} | k | t / L} \| _ {L ^ {2} (d t)}   \| \Phi \| _ {L ^ {2} (d t)} \\ \leqslant \| A \| _ {L ^ {\infty} (d t)} + \frac {\| K ^ {0} e ^ {2 \pi \lambda^ {\prime} | k | t / L} \| _ {L ^ {2} (d t)}   \| A \| _ {L ^ {2} (d t)}}{\varkappa}. \end{array}\tag{3.6}
$$

It remains to bound the second term. On the one hand,

$$
\begin{array}{l} \| A \| _ {L ^ {2} (d t)} = \biggl (\int_ {0} ^ {\infty} | a (t, k) | ^ {2} e ^ {4 \pi \lambda^ {\prime} | k | t / L} d t \biggr) ^ {1 / 2} \\ \leqslant \biggl (\int_ {0} ^ {\infty} e ^ {- 4 \pi (\lambda - \lambda^ {\prime}) | k | t / L} d t \biggr) ^ {1 / 2} \sup _ {t \geqslant 0} | a (t, k) | e ^ {2 \pi \lambda | k | t / L} \\ = \biggl (\frac {L}{4 \pi | k | (\lambda - \lambda^ {\prime})} \biggr) ^ {1 / 2} \sup _ {t \geqslant 0} | a (t, k) | e ^ {2 \pi \lambda | k | t / L}. \end{array}\tag{3.7}
$$

On the other hand,

$$
\begin{array}{c} \| K ^ {0} e ^ {2 \pi \lambda^ {\prime} | k | t / L} \| _ {L ^ {2} (d t)} = 4 \pi^ {2} | \widehat {W} ^ {(L)} (k) | \frac {| k | ^ {2}}{L ^ {2}} \bigg (\int_ {0} ^ {\infty} e ^ {4 \pi \lambda^ {\prime} | k | t / L} \bigg | \tilde {f} ^ {0} \bigg (\frac {k t}{L} \bigg) \bigg | ^ {2} t ^ {2} d t \bigg) ^ {1 / 2} \\ = 4 \pi^ {2} | \widehat {W} ^ {(L)} (k) | \frac {| k | ^ {1 / 2}}{L ^ {1 / 2}} \bigg (\int_ {0} ^ {\infty} e ^ {4 \pi \lambda^ {\prime} u} | \tilde {f} ^ {0} (\sigma u) | ^ {2} u ^ {2} d u \bigg) ^ {1 / 2}, \end{array}\tag{3.8}
$$

where$\sigma { = } k / | k |$and$u = | k | t / L$. The estimate follows since

$$
\int_ {0} ^ {\infty} e ^ {- 4 \pi (\lambda - \lambda^ {\prime}) u} u ^ {2} d u = O ((\lambda - \lambda^ {\prime}) ^ {- 3 / 2}).
$$

(Note that the factor$| k | ^ { - 1 / 2 }$in (3.7) cancels with$| k | ^ { 1 / 2 }$in (3.8).)

It seems that we only used properties of the function$\mathcal { L }$in a strip Re$\xi \simeq \lambda ;$but this is an illusion. Indeed, we have taken the Fourier transform of Φ without checking that it belongs to$( L ^ { 1 } + L ^ { 2 } ) ( d t )$, so what we have established is only an a-priori estimate. To convert it into a rigorous result, one can use a continuity argument after replacing$\lambda ^ { \prime }$by a parameter$\alpha$which varies from ε to$\lambda ^ { \prime } .$. (By the integrability of$K ^ { 0 }$and Gr¨onwall’s lemma,$\varphi$is obviously bounded as a function of$t ;$so$\varphi ( k , t ) e ^ { - \varepsilon | k | t / L }$is integrable for any $\varepsilon > 0 .$, and continuous as$\varepsilon  0 . )$Then assumption (L) guarantees that our bounds are uniform in the strip$0 \leqslant \operatorname { R e } \xi \leqslant \lambda ^ { \prime }$, and the proof goes through.□

Proof of Theorem 3.1. Without loss of generality, we assume$t \geqslant 0$. Considering (3.3) as a perturbation of free transport, we apply Duhamel’s formula to get

$$
f (t, x, v) = f _ {i} (x - v t, v) + \int_ {0} ^ {t} [ (\nabla W * \varrho) \cdot \nabla_ {v} f ^ {0} ] (\tau , x - v (t - \tau), v) d \tau .\tag{3.9}
$$

Integration in v yields

$$
\varrho (t, x) = \int_ {\mathbb {R} ^ {d}} f _ {i} (x - v t, v) d v + \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} [ (\nabla W * \varrho) \cdot \nabla_ {v} f ^ {0} ] (\tau , x - v (t - \tau), v) d v d \tau .\tag{3.10}
$$

Of course,

$$
\int_ {\mathbb {T} _ {L} ^ {d}} \varrho (t, x) d x = \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x, v) d v d x.
$$

For$k { \neq } 0$, taking the Fourier transform of (3.10), we obtain

$$
\begin{array}{l} \widehat {\varrho} ^ {(L)} (t, k) = \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x - v t, v) e ^ {- 2 i \pi k \cdot x / L} d v d x \\ \qquad + \int_ {0} ^ {t} \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} [ (\nabla W * \varrho) \cdot \nabla_ {v} f ^ {0} ] (\tau , x - v (t - \tau), v) e ^ {- 2 i \pi k \cdot x / L} d v d x d \tau \\ = \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x, v) e ^ {- 2 i \pi k \cdot x / L} e ^ {- 2 i \pi k \cdot v t / L} d v d x \\ \qquad + \int_ {0} ^ {t} \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} [ (\nabla W * \varrho) \cdot \nabla_ {v} f ^ {0} ] (\tau , x, v) e ^ {- 2 i \pi k \cdot x / L} e ^ {- 2 i \pi k \cdot v (t - \tau) / L} d v d x d \tau \\ = \widetilde {f} _ {i} ^ {(L)} \bigg (k, \frac {k t}{L} \bigg) + \int_ {0} ^ {t} (\widehat {\nabla W * \varrho}) ^ {(L)} (\tau , k) \cdot \widetilde {\nabla_ {v} f ^ {0}} \bigg (\frac {k (t - \tau)}{L} \bigg) d \tau \\ = \widetilde {f} _ {i} ^ {(L)} \bigg (k, \frac {k t}{L} \bigg) + \int_ {0} ^ {t} \bigg (2 i \pi \frac {k}{L} \widehat {W} ^ {(L)} (k) \widehat {\varrho} ^ {(L)} (\tau , k) \bigg) \cdot \bigg (2 i \pi \frac {k (t - \tau)}{L} \widetilde {f} ^ {0} \bigg (\frac {k (t - \tau)}{L} \bigg) \bigg) d \tau . \end{array}
$$

In conclusion, we have established the closed equation for$\hat { \varrho } ^ { ( L ) }$:

$$
\hat {\varrho} ^ {(L)} (t, k) = \tilde {f} _ {i} ^ {(L)} \left(k, \frac {k t}{L}\right) - 4 \pi^ {2} \widehat {W} ^ {(L)} (k) \int_ {0} ^ {t} \hat {\varrho} ^ {(L)} (\tau , k) \tilde {f} ^ {0} \left(\frac {k (t - \tau)}{L}\right) \frac {| k | ^ {2}}{L ^ {2}} (t - \tau) d \tau .\tag{3.11}
$$

Recalling (2.3), this is the same as

$$
\hat {\varrho} ^ {(L)} (t, k) = \tilde {f} _ {i} ^ {(L)} \left(k, \frac {k t}{L}\right) + \int_ {0} ^ {t} K ^ {0} (t - \tau , k) \hat {\varrho} ^ {(L)} (\tau , k) d \tau .
$$

Without loss of generality$\lambda { \leqslant } \alpha ,$, where α appears in Theorem 3.1. By assumption (L) and Lemma 3.6,

$$
| \hat {\varrho} ^ {(L)} (t, k) | \leqslant C _ {0} C _ {W} C (\lambda , \lambda^ {\prime}, \varkappa) C _ {i} e ^ {- 2 \pi \lambda^ {\prime} | k | t / L}.
$$

In particular, for k=0 we have

$$
| \hat {\varrho} ^ {(L)} (t, k) | = O (e ^ {- 2 \pi \lambda^ {\prime \prime} t / L} e ^ {- 2 \pi (\lambda^ {\prime} - \lambda^ {\prime \prime}) | k | / L}) \quad \text { for   all } t \geqslant 1;
$$

so any Sobolev norm of$\varrho - \varrho _ { \infty }$converges to zero like$O ( e ^ { - 2 \pi \lambda ^ { \prime \prime } t / L } )$, where$\lambda ^ { \prime \prime }$is arbitrarily close to$\lambda ^ { \prime }$and therefore also to λ. By Sobolev embedding, the same is true for any$C ^ { r }$ norm.

Next, we go back to (3.9) and take the Fourier transform in both variables x and v,

to find

$$
\begin{array}{l} \tilde {f} ^ {(L)} (t, k, \eta) = \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x - v t, v) e ^ {- 2 i \pi k \cdot x / L} e ^ {- 2 i \pi \eta \cdot v} d v d x \\ \qquad + \int_ {0} ^ {t} \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} (\nabla W * \varrho) (\tau , x - v (t - \tau)) \cdot \nabla_ {v} f ^ {0} (v) e ^ {- 2 i \pi k \cdot x / L} e ^ {- 2 i \pi \eta \cdot v} d v d x d \tau \\ = \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x, v) e ^ {- 2 i \pi k \cdot x / L} e ^ {- 2 i \pi k \cdot v t / L} e ^ {- 2 i \pi \eta \cdot v} d v d x \\ \qquad + \int_ {0} ^ {t} \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} (\nabla W * \varrho) (\tau , x) \cdot \nabla_ {v} f ^ {0} (v) \\ \qquad \times e ^ {- 2 i \pi k \cdot x / L} e ^ {- 2 i \pi k \cdot v (t - \tau) / L} e ^ {- 2 i \pi \eta \cdot v} d v d x d \tau \\ = \widetilde {f} _ {i} ^ {(L)} \left(k, \eta + \frac {k t}{L}\right) + \int_ {0} ^ {t} \widehat {\nabla W} ^ {(L)} (k) \widehat {\varrho} ^ {(L)} (\tau , k) \cdot \widehat {\nabla_ {v} f ^ {0}} \left(\eta + \frac {k (t - \tau)}{L}\right) d \tau . \end{array}
$$

So

$$
\tilde {f} ^ {(L)} \left(t, k, \eta - \frac {k t}{L}\right) = \tilde {f} _ {i} ^ {(L)} (k, \eta) + \int_ {0} ^ {t} \widehat {\nabla W} ^ {(L)} (k) \hat {\varrho} ^ {(L)} (\tau , k) \cdot \widetilde {\nabla_ {v} f ^ {0}} \left(\eta - \frac {k \tau}{L}\right) d \tau .\tag{3.12}
$$

In particular, for any$\eta \in \mathbb { R } ^ { d }$

$$
\tilde {f} ^ {(L)} (t, 0, \eta) = \tilde {f} _ {i} ^ {(L)} (0, \eta);\tag{3.13}
$$

in other words,$\scriptstyle \langle f \rangle = L ^ { - d } \int _ { \mathbb { T } _ { r } ^ { d } } f$dx remains equal to$\langle f _ { i } \rangle$for all times.

On the other hand, if$k { \neq } 0$, then

$$
\begin{array}{l} \left| \tilde {f} ^ {(L)} \bigg (t, k, \eta - \frac {k t}{L} \bigg) \right| \\ \leqslant | \tilde {f} _ {i} ^ {(L)} (k, \eta) | + \int_ {0} ^ {t} | \widehat {\nabla W} ^ {(L)} (k) |   | \hat {\varrho} ^ {(L)} (\tau , k) |   \left| \widetilde {\nabla_ {v} f ^ {0}} \bigg (\eta - \frac {k \tau}{L} \bigg) \right| d \tau \\ \leqslant C _ {i} e ^ {- 2 \pi \alpha | \eta |} + \int_ {0} ^ {t} C _ {W} C (\lambda , \lambda^ {\prime}, \varkappa) C _ {i} e ^ {- 2 \pi \lambda^ {\prime} | k | \tau / L} \bigg (2 \pi C _ {0} \bigg | \eta - \frac {k \tau}{L} \bigg | e ^ {- 2 \pi \lambda | \eta - k \tau / L |} \bigg) d \tau \\ \leqslant C \bigg (e ^ {- 2 \pi \alpha | \eta |} + \int_ {0} ^ {t} e ^ {- 2 \pi \lambda^ {\prime} | k | \tau / L} e ^ {- \pi (\lambda^ {\prime} + \lambda) | \eta - k \tau / L |}   d \tau \bigg), \end{array}\tag{3.14}
$$

where we have used that$\lambda ^ { \prime } < \frac { 1 } { 2 } \bigl ( \lambda ^ { \prime } + \lambda \bigr ) < \lambda$, and$C$only depends on$C _ { W } , C _ { i } , \lambda , \lambda ^ { \prime }$and$\varkappa .$ In the end,

$$
\begin{array}{c} \int_ {0} ^ {t} e ^ {- 2 \pi \lambda^ {\prime} | k | \tau / L} e ^ {- \pi (\lambda^ {\prime} + \lambda) | \eta - k \tau / L |} d \tau \leqslant \int_ {0} ^ {t} e ^ {- 2 \pi \lambda^ {\prime} | \eta |} e ^ {- \pi (\lambda - \lambda^ {\prime}) | \eta - k \tau / L |} d \tau \\ \leqslant \frac {L}{\pi (\lambda - \lambda^ {\prime})} e ^ {- 2 \pi [ \lambda^ {\prime} - (\lambda - \lambda^ {\prime}) / 2 ] | \eta |}. \end{array}
$$

Plugging this back into (3.14), we obtain, with$\scriptstyle { \lambda ^ { \prime \prime } = \lambda ^ { \prime } - { \frac { 1 } { 2 } } ( \lambda - \lambda ^ { \prime } ) }$1

$$
\left| \tilde {f} ^ {(L)} \left(t, k, \eta - \frac {k t}{L}\right) \right| \leqslant C e ^ {- 2 \pi \lambda^ {\prime \prime} | \eta |}.\tag{3.15}
$$

In particular, for any fixed η and$k { \neq } 0 .$

$$
| \tilde {f} ^ {(L)} (t, k, \eta) | \leqslant C e ^ {- 2 \pi \lambda^ {\prime \prime} | \eta + k t / L |} = O (e ^ {- 2 \pi \lambda^ {\prime \prime} | t | / L}).
$$

We conclude that$\tilde { f } ^ { ( L ) }$converges pointwise, exponentially fast, to the Fourier transform of$\langle f _ { i } \rangle$. Since$\lambda ^ { \prime }$and then$\lambda ^ { \prime \prime }$can be taken as close to λ as wanted, this ends the proof.

We close this section by proving Proposition 2.1.

Proof of Proposition 2.1. First assume (a). Since$\tilde { f } ^ { 0 }$decreases exponentially fast, we can find$\lambda , \varkappa > 0$such that

$$
4 \pi^ {2} \max \left| \widehat {W} ^ {(L)} (k) \right| \sup _ {| \sigma | = 1} \int_ {0} ^ {\infty} | \tilde {f} ^ {0} (r \sigma) | r e ^ {2 \pi \lambda r} d r \leqslant 1 - \varkappa .
$$

Performing the change of variables$k t / L { = } r \sigma$inside the integral, we deduce that

$$
\int_ {0} ^ {\infty} 4 \pi^ {2} | \widehat {W} ^ {(L)} (k) | \left| \tilde {f} ^ {0} \left(\frac {k t}{L}\right) \right| \frac {| k | ^ {2} t}{L ^ {2}} e ^ {2 \pi \lambda | k | t / L} d t \leqslant 1 - \varkappa ,
$$

and this obviously implies (L).

The choice$w { = } 0$in (2.8) shows that condition (b) is a particular case of$\mathrm { ( c ) }$, so we only treat the latter assumption. The reasoning is more subtle than for case (a). Throughout the proof we shall abbreviate$\widehat { W } ^ { ( L ) } \ \mathrm { b y } \ \widehat { W }$. As a start, let us assume$d { = } 1$ and$k > 0$(so$k \in \mathbb { N } )$). Then we compute: for any$\omega \in \mathbb { R }$,

$$
\begin{array}{l} \int_ {0} ^ {\infty} e ^ {2 i \pi \omega k t / L} K ^ {0} (t, k)   d t \\ = \lim _ {\lambda \to 0 ^ {+}} \int_ {0} ^ {\infty} e ^ {- 2 \pi \lambda k t / L} e ^ {2 i \pi \omega k t / L}   K ^ {0} (t, k)   d t \\ = - 4 \pi^ {2} \widehat {W} (k) \lim _ {\lambda \to 0 ^ {+}} \int_ {0} ^ {\infty} \int_ {\mathbb {R}} f ^ {0} (v) e ^ {- 2 i \pi k v t / L} e ^ {- 2 \pi \lambda k t / L} e ^ {2 i \pi \omega k t / L} \frac {k ^ {2}}{L ^ {2}} t   d v   d t \\ = - 4 \pi^ {2} \widehat {W} (k) \lim _ {\lambda \to 0 ^ {+}} \int_ {0} ^ {\infty} \int_ {\mathbb {R}} f ^ {0} (v) e ^ {- 2 i \pi v t} e ^ {- 2 \pi \lambda t} e ^ {2 i \pi \omega t} t   d v   d t. \end{array}\tag{3.16}
$$

Then by integration by parts, assuming that$( f ^ { 0 } ) ^ { \prime }$is integrable,

$$
\int_ {\mathbb {R}} f ^ {0} (v) e ^ {- 2 i \pi v t} t d v = \frac {1}{2 i \pi} \int_ {\mathbb {R}} (f ^ {0}) ^ {\prime} (v) e ^ {- 2 i \pi v t} d v.
$$

Plugging this back into (3.16), we obtain the expression

$$
2 i \pi \widehat {W} (k) \lim _ {\lambda \rightarrow 0 ^ {+}} \int_ {\mathbb {R}} (f ^ {0}) ^ {\prime} (v) \int_ {0} ^ {\infty} e ^ {- 2 \pi [ \lambda + i (v - \omega) ] t} d t d v.
$$

Next, recall that for any$\lambda { > } 0$

$$
\int_ {0} ^ {\infty} e ^ {- 2 \pi [ \lambda + i (v - \omega) ] t} d t = \frac {1}{2 \pi [ \lambda + i (v - \omega) ]};
$$

indeed, both sides are holomorphic functions of$z = \lambda + i ( v - \omega )$in the half-plane$\{ z \in \mathbb { C }$ $\operatorname { R e } z > 0 \}$, and they coincide on the real half-axis$\{ z \in \mathbb { R } { : } z > 0 \}$, so they have to coincide everywhere. We conclude that

$$
\int_ {0} ^ {\infty} e ^ {2 i \pi \omega k t / L} K ^ {0} (t, k) d t = \widehat {W} (k) \lim _ {\lambda \rightarrow 0 ^ {+}} \int_ {\mathbb {R}} \frac {(f ^ {0}) ^ {\prime} (v)}{v - \omega - i \lambda} d v.\tag{3.17}
$$

The celebrated Plemelj formula states that

$$
\frac {1}{z - i 0} = \mathrm{p.v.} \left(\frac {1}{z}\right) + i \pi \delta_ {0},\tag{3.18}
$$

where the left-hand side should be understood as the limit, in weak sense, of$1 / ( z - i \lambda )$as $\lambda \to 0 ^ { + }$. The abbreviation p.v. stands for principal value, that is, simplifying the possibly divergent part by using compensations by symmetry when the denominator vanishes. Formula (3.18) is proven in Appendix A.5, where the notion of principal value is also precisely defined. Combining (3.17) and (3.18), we end up with the identity

$$
\int_ {0} ^ {\infty} e ^ {2 i \pi \omega k t / L} K ^ {0} (t, k) d t = \widehat {W} (k) \bigg [ \bigg (\text {p.v.} \int_ {\mathbb {R}} \frac {(f ^ {0}) ^ {\prime} (v)}{v - \omega} d v \bigg) + i \pi (f ^ {0}) ^ {\prime} (\omega) \bigg ].\tag{3.19}
$$

Since$W$is even,$\widehat { W }$is real-valued, so the above formula yields the decomposition of the limit into real and imaginary parts. The problem is to check that the real part cannot approach 1 at the same time as the imaginary part approaches 0.

As soon as$( f ^ { 0 } ) ^ { \prime } ( v ) { = } O ( 1 / | v | )$, we have

$$
\int_ {\mathbb {R}} \frac {(f ^ {0}) ^ {\prime} (v)}{v - \omega} d v = O \left(\frac {1}{| \omega |}\right) \quad \text { as } | \omega | \to \infty ,
$$

so the real part in the right-hand side of (3.19) becomes small when$| \omega |$is large, and we can restrict to a bounded interval$| \omega | \leqslant \Omega$

Then the imaginary part,$\widehat { W } ( k ) \pi ( f ^ { 0 } ) ^ { \prime } ( \omega )$, can become small only in the limit$k \to \infty$ (but then also the real part becomes small) or if$\omega$approaches one of the zeroes of$( f ^ { 0 } ) ^ { \prime }$ Since$\omega$varies in a compact set, by continuity it will be suficient to check the condition only at the zeroes of$( f ^ { 0 } ) ^ { \prime }$. In the end, we have obtained the following stability criterion: for any k <sup>N</sup>,

$$
(f ^ {0}) ^ {\prime} (\omega) = 0 \implies \widehat {W} (k) \int_ {\mathbb {R}} \frac {(f ^ {0}) ^ {\prime} (v)}{v - \omega} d v \neq 1 \quad \text { for   all } \omega \in \mathbb {R}.\tag{3.20}
$$

Now, if$k { < } 0 .$, we can restart the computation as follows:

$$
\begin{array}{l} \int_ {0} ^ {\infty} e ^ {2 i \pi \omega | k | t / L} K ^ {0} (t, k) d t \\ = - 4 \pi^ {2} \widehat {W} (k) \lim _ {\lambda \to 0 ^ {+}} \int_ {0} ^ {\infty} \int_ {\mathbb {R}} f ^ {0} (v) e ^ {- 2 i \pi k v t / L} e ^ {- 2 \pi \lambda | k | t / L} e ^ {2 i \pi \omega | k | t / L} \frac {| k | ^ {2}}{L ^ {2}} t d v d t. \end{array}
$$

Then the change of variable$v \mapsto - v$brings us back to the previous computation with k replaced by$| k |$(except in the argument of$W )$and$f ^ { 0 } ( v )$replaced by$f ^ { 0 } ( - v )$. However, it is immediately checked that (3.20) is invariant under reversal of velocities, that is, if $f ^ { 0 } ( v )$is replaced by$f ^ { 0 } ( - v )$

Finally, let us generalize this to several dimensions. If$k \in \mathbb { Z } ^ { d } \backslash \{ 0 \}$and$\xi \in \mathbb { C }$, we can use the splitting

$$
v = \frac {k}{| k |} r + w, \quad w \bot k, \quad r = \frac {k}{| k |} \cdot v
$$

and Fubini’s theorem to rewrite

$$
\begin{array}{l} \mathcal {L} (\xi , k) \\ = - 4 \pi^ {2} \widehat {W} (k) \frac {| k | ^ {2}}{L ^ {2}} \int_ {0} ^ {\infty} \int_ {\mathbb {R} ^ {d}} f ^ {0} (v) e ^ {- 2 i \pi k t \cdot v / L} t e ^ {2 \pi | k | \xi^ {*} t / L} d v d t \\ = - 4 \pi^ {2} \widehat {W} (k) \frac {| k | ^ {2}}{L ^ {2}} \int_ {0} ^ {\infty} \int_ {\mathbb {R}} \biggl (\int_ {k r / | k | + k ^ {\perp}} f ^ {0} \biggl (\frac {k}{| k |} r + w \biggr) d w \biggr) e ^ {- 2 i \pi | k | r t / L} t e ^ {2 \pi | k | \xi^ {*} t / L} d r d t, \end{array}
$$

where$k ^ { \perp }$is the hyperplane orthogonal to k. So everything is expressed in terms of the 1-dimensional marginals of$f ^ { 0 }$. If$f$is a given function of$v \in \mathbb { R } ^ { d }$, and$\sigma$is a unit vector, let us write$\sigma ^ { \perp }$for the hyperplane orthogonal to$\sigma _ { : }$, and

$$
f _ {\sigma} (v) = \int_ {v \sigma + \sigma^ {\perp}} f (w) d w \quad \text { for   all } v \in \mathbb {R}.\tag{3.21}
$$

Then the computation above shows that the multi-dimensional stability criterion reduces to the 1-dimensional criterion in each direction$k / | k |$, and the claim is proven.□

## 4. Analytic norms

In this section we introduce some functional spaces of analytic functions on the spaces $\mathbb { R } ^ { d } , \ \mathbb { T } ^ { d } { = } \mathbb { R } ^ { d } / \mathbb { Z } ^ { d }$and most importantly$\mathbb { T } ^ { d } \times \mathbb { R } ^ { d }$. (Changing the sidelength of the torus only results in some changes in the constants.) Then we establish a number of functional inequalities which will be crucial in the subsequent analysis. At the end of this section we shall reformulate the linear study in this new setting.

Throughout the whole section, d is a positive integer. Working with analytic functions will force us to be careful with combinatorial issues, and proofs will at times involve summation over many indices.

## 4.1. Single-variable analytic norms

Here “single-variable” means that the variable lives in either$\mathbb { R } ^ { d }$or$\mathbb { T } ^ { d }$, but d may be greater than 1.

Among many possible families of norms for analytic functions, two will be of particular interest for us; they will be denoted by$\mathcal { C } ^ { \lambda ; p }$and$\mathcal { F } ^ { \lambda ; p }$. The$\mathcal { C } ^ { \lambda ; p }$norms are defined for functions on$\mathbb { R } ^ { d }$or$\mathbb { T } ^ { d } .$, while the$\mathcal { F } ^ { \lambda ; p }$norms are defined only for$\mathbb { T } ^ { d }$(although we could easily cook up a variant in$\mathbb { R } ^ { d } )$. We shall write$\mathbb { N } _ { 0 } ^ { d }$for the set of d-tuples of integers (the subscript being here to insist that 0 is allowed). If$\boldsymbol { n } \in  { \mathbb { N } } _ { 0 } ^ { d }$and$\lambda { \geqslant } 0$we shall write $\lambda ^ { n } { = } \lambda ^ { | n | }$. Conventions about the Fourier transform and multi-dimensional diferential calculus are gathered in the appendix.

Definition 4.1. (One-variable analytic norms) For any$p { \in } [ 1 , \infty ]$and$\lambda { \geqslant } 0$, we define

$$
\| f \| _ {\mathcal {C} ^ {\lambda ; p}} := \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \| f ^ {(n)} \| _ {L ^ {p}} \quad \text { and } \quad \| f \| _ {\mathcal {F} ^ {\lambda ; p}} := \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} e ^ {2 \pi \lambda p | k |} | \hat {f} (k) | ^ {p} \bigg) ^ {1 / p},\tag{4.1}
$$

the latter expression standing for$\scriptstyle \operatorname* { s u p } _ { k \in \mathbb { Z } ^ { d } } | { \hat { f } } ( k ) | e ^ { 2 \pi \lambda | k | } { \mathrm { ~ i f ~ } } p = \infty$. We further write

$$
\mathcal {C} ^ {\lambda} := \mathcal {C} ^ {\lambda ; \infty} \quad \text { and } \quad \mathcal {F} ^ {\lambda} := \mathcal {F} ^ {\lambda ; 1}.\tag{4.2}
$$

Remark 4.2. The parameter λ can be interpreted as a radius of convergence.

Remark 4.3. The norms$\mathcal { C } ^ { \lambda }$and${ \mathcal { F } } ^ { \lambda }$are of particular interest because they are algebra norms.

We shall sometimes abbreviate$\| \cdot \| _ { \mathcal { C } ^ { \lambda ; p } } \ \mathrm { o r } \ \| \cdot \| _ { \mathcal { F } ^ { \lambda ; p } }$into$\| \cdot \| _ { \lambda ; p }$when no confusion is possible, or when the statement works for either norm.

The norms in (4.1) extend to vector-valued functions in a natural way: if$f$is valued in$\mathbb { R } ^ { d }$or$\mathbb { T } ^ { d }$or$\mathbb { Z } ^ { d }$, define$f ^ { ( n ) } { = } ( f _ { 1 } ^ { ( n ) } , { \ldots } , f _ { d } ^ { ( n ) } )$and$\hat { f } ( k ) { = } ( \hat { f } _ { 1 } ( k ) , { \ldots } , \hat { f } _ { d } ( k ) )$; then the formulae in (4.1) make sense provided that we choose a norm on$\mathbb { R } ^ { d }$or$\mathbb { T } ^ { d }$or$\mathbb { Z } ^ { d }$ Which norm we choose will depend on the context; the choice will always be done in such a way to get the duality right in the inequality$| a \cdot b | \leqslant \left\| a \right\| \left\| b \right\| .$. For instance if f is valued in$\mathbb { Z } ^ { d }$and$g$in$\mathbb { T } ^ { d } .$, and we have to estimate$f \cdot g$, we may norm$\mathbb { Z } ^ { d }$by$\scriptstyle | k | = \sum _ { j = 1 } ^ { d } | k _ { j } |$and $\mathbb { T } ^ { d }$by$| x | { = } \mathrm { s u p } _ { j } | x _ { j } | . ( ^ { 1 5 } )$This will not pose any problem, and the reader can forget about this issue; we shall just make remarks about it whenever needed. For the rest of this section, we shall focus on scalar-valued functions for simplicity of exposition.

Next, we define “homogeneous” analytic seminorms by removing the zeroth-order term. We write${ \mathbb { N } } _ { * } ^ { d } { = }  { \mathbb { N } } _ { 0 } ^ { d } \backslash \{ 0 \}$and$\mathbb { Z } _ { * } ^ { d } { = } \mathbb { Z } ^ { d } \backslash \{ 0 \}$

Definition 4.4. (One-variable homogeneous analytic seminorms) For$p \in [ 1 , \infty ]$and $\lambda { \geqslant } 0$we write

$$
\| f \| _ {\dot {\mathcal {C}} ^ {\lambda ; p}} = \sum_ {n \in \mathbb {N} _ {*} ^ {d}} \frac {\lambda^ {n}}{n !} \| f ^ {(n)} \| _ {L ^ {p}} \quad \text { and } \quad \| f \| _ {\dot {\mathcal {F}} ^ {\lambda ; p}} = \bigg (\sum_ {k \in \mathbb {Z} _ {*} ^ {d}} e ^ {2 \pi \lambda p | k |} | \hat {f} (k) | ^ {p} \bigg) ^ {1 / p}.
$$

It is interesting to note that afine functions$x { \mapsto } a \cdot x + b$can be included in$\dot { \mathcal { C } } ^ { \lambda } { = } \dot { \mathcal { C } } ^ { \lambda ; \infty }$ even though they are unbounded; in particular$\| a \cdot x + b \| _ { \dot { \mathcal { C } } ^ { \lambda } } = \lambda | a |$. On the other hand, linear forms$x { \mapsto } a \cdot x$do not naturally belong to$\dot { \mathcal { F } } ^ { \lambda }$, because their Fourier expansion is not even summable (it decays like$1 / k )$

The spaces$\mathcal { C } ^ { \lambda ; p }$and$\mathcal { F } ^ { \lambda ; p }$enjoy remarkable properties, summarized in Propositions 4.5, 4.8 and 4.10 below. Some of these properties are well known, others not so.

Proposition 4.5. (Algebra property) (i) For any$\lambda { \geqslant } 0$and$p , q , r \in [ 1 , \infty ]$such that $1 / p + 1 / q { = } 1 / r$, we have

$$
\| f g \| _ {\mathcal {C} ^ {\lambda ; r}} \leqslant \| f \| _ {\mathcal {C} ^ {\lambda ; p}} \| g \| _ {\mathcal {C} ^ {\lambda ; q}}.
$$

(ii) For any$\lambda { \geqslant } 0$and$p , q , r \in [ 1 , \infty ]$such that$1 / p + 1 / q = 1 / r + 1$, we have

$$
\left\| f g \right\| _ {\mathcal {F} ^ {\lambda ; r}} \leqslant \left\| f \right\| _ {\mathcal {F} ^ {\lambda ; p}} \left\| g \right\| _ {\mathcal {F} ^ {\lambda ; q}}.
$$

(iii) As a consequence, for any$\lambda { \geqslant } 0 , \mathcal { C } ^ { \lambda } { = } \mathcal { C } ^ { \lambda ; \infty }$and$\mathcal { F } ^ { \lambda } { = } \mathcal { F } ^ { \lambda ; 1 }$are normed algebras: for either space,

$$
\| f g \| _ {\lambda} \leqslant \| f \| _ {\lambda} \| g \| _ {\lambda}.
$$

In particular,$\| f ^ { n } \| _ { \lambda } \leqslant \| f \| _ { \lambda } ^ { n }$for any$\textstyle n \in \mathbb { N } _ { 0 } .$, and$\left\| e ^ { f } \right\| _ { \lambda } { \leqslant } e ^ { \left\| f \right\| _ { \lambda } }$

Remark 4.6. Ultimately, property (iii) relies on the fact that$L ^ { \infty }$and$L ^ { 1 }$are normed algebras for the multiplication and convolution, respectively.

Remark 4.7. It follows from the Fourier inversion formula and Proposition 4.5 that $\| f \| _ { C ^ { \lambda } } \leqslant \| f \| _ { \mathcal { F } ^ { \lambda } }$(and$\| f \| _ { \dot { \mathcal { C } } ^ { \lambda } } \leqslant \| f \| _ { \dot { \mathcal { F } } ^ { \lambda } } )$; this is a special case of Proposition$4 . 8 ( \mathrm { i v } )$below. The reverse inequality does not hold, because$\| f \| _ { \infty }$does not control$\| \hat { f } \| _ { L ^ { 1 } }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">R<sup>d</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>15</sup>) Of course all norms are equivalent, still the choice is not innocent when the estimates are iterated infinitely many times; an advantage of the supremum norm on is that it has the algebra property.</span></small>

Analytic norms are very sensitive to composition; think that if$a > 0$then

$$
\| f \circ (a \operatorname{Id}) \| _ {\mathcal {C} ^ {\lambda ; p}} = a ^ {- d / p} \| f \| _ {\mathcal {C} ^ {a \lambda ; p}};
$$

so we typically lose on the functional space. This is a major diference with more traditional norms used in partial diferential equations theory, such as H¨older or Sobolev norms, for which composition may afect constants but not regularity indices. The next proposition controls the loss of regularity implied by composition.

Proposition 4.8. (Composition inequality) (i) For any$\lambda { > } 0$and any$p \in [ 1 , \infty ]$

$$
\| f \circ H \| _ {\mathcal {C} ^ {\lambda ; p}} \leqslant \| (\det \nabla H) ^ {- 1} \| _ {\infty} ^ {1 / p} \| f \| _ {\mathcal {C} ^ {\nu ; p}}, \quad \nu = \| H \| _ {\dot {\mathcal {C}} ^ {\lambda}},
$$

where H is possibly unbounded.

(ii) For any$\lambda { > } 0$, any$p { \in } [ 1 , \infty ]$and any$a > 0$

$$
\| f \circ (a \operatorname{Id} + G) \| _ {\mathcal {C} ^ {\lambda ; p}} \leqslant a ^ {- d / p} \| f \| _ {\mathcal {C} ^ {a \lambda + \nu ; p}}, \quad \nu = \| G \| _ {\mathcal {C} ^ {\lambda}}.
$$

(iii) For any$\lambda { > } 0$•

$$
\| f \circ (\operatorname{Id} + G) \| _ {\mathcal {F} ^ {\lambda}} \leqslant \| f \| _ {\mathcal {F} ^ {\lambda + \nu}}, \quad \nu = \| G \| _ {\dot {\mathcal {F}} ^ {\lambda}}.
$$

(iv) For any$\lambda { > } 0$and any$a > 0$,

$$
\left\| f \circ (a \operatorname{Id} + G) \right\| _ {\mathcal {C} ^ {\lambda}} \leqslant \left\| f \right\| _ {\mathcal {F} ^ {a \lambda + \nu}}, \quad \nu = \| G \| _ {\dot {\mathcal {C}} ^ {\lambda}}.
$$

Remark 4.9. Inequality$( \mathrm { i v } )$, with on the left and$\mathcal { F }$on the right, will be most useful. The reverse inequality is not likely to hold, in view of Remark 4.7.

The last property of interest for us is the control of the loss of regularity involved by diferentiation.

Proposition 4.10. (Control of gradients) For any$\bar { \lambda } > \lambda$and any$p { \in } [ 1 , \infty ]$

$$
\| \nabla f \| _ {\mathcal {C} ^ {\lambda ; p}} \leqslant \frac {1}{\lambda e \log (\bar {\lambda} / \lambda)} \| f \| _ {\dot {\mathcal {C}} ^ {\bar {\lambda}; p}},\tag{4.3}
$$

$$
\| \nabla f \| _ {\mathcal {F} ^ {\lambda ; p}} \leqslant \frac {1}{2 \pi e (\bar {\lambda} - \lambda)} \| f \| _ {\dot {\mathcal {F}} ^ {\bar {\lambda}; p}}.\tag{4.4}
$$

The proofs of Propositions 4.5–4.10 will be preparations for the more complicated situations considered in the sequel.

Proof of Proposition 4.5. (i) Denoting the norm of$\mathcal { C } ^ { \lambda ; p }$by$\| \cdot \| _ { \lambda ; p }$and using the multi-dimensional Leibniz formula from Appendix A.2, we have

$$
\begin{aligned} \| fg\|_{\lambda ;r} & = \sum_{l\in \mathbb{N}_{0}^{d}}\|(fg)^{(l)}\|_{L^{r}}\frac{\lambda^{l}}{l!}\\ & \leqslant \sum_{\substack{l,m\in \mathbb{N}_{0}^{d}\\ m\leqslant l}}\binom {l}{m}\| f^{(m)}g^{(l - m)}\|_{L^{r}}\frac{\lambda^{l}}{l!}\\ & \leqslant \sum_{\substack{l,m\in \mathbb{N}_{0}^{d}\\ m\leqslant l}}\binom {l}{m}\| f^{(m)}\|_{L^{p}}\| g^{(l - m)}\|_{L^{q}}\frac{\lambda^{l}}{l!}\\ & = \sum_{\substack{l,m\in \mathbb{N}_{0}^{d}\\ m\leqslant l}}\frac{\|f^{(m)}\|_{L^{p}}\lambda^{m}}{m!}\frac{\|g^{(l - m)}\|_{L^{q}}\lambda^{l - m}}{(l - m)!}\\ & = \| f\|_{\lambda ;p}\| g\|_{\lambda ;q}. \end{aligned}
$$

(ii) Denoting now the norm of$\mathcal { F } ^ { \lambda ; p }$by$\| \cdot \| _ { \lambda ; p }$and applying Young’s convolution inequality, we get

$$
\begin{array}{l} \| f g \| _ {\lambda ; r} = \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} | \widehat {f g} (k) | ^ {r} e ^ {2 \pi \lambda r | k |} \bigg) ^ {1 / r} \\ \leqslant \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} \bigg (\sum_ {l \in \mathbb {Z} ^ {d}} | \hat {f} (l) |   | \hat {g} (k - l) | e ^ {2 \pi \lambda | k - l |} e ^ {2 \pi \lambda | l |} \bigg) ^ {r} \bigg) ^ {1 / r} \\ \leqslant \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} | \hat {f} (k) | ^ {p} e ^ {2 \pi \lambda p | k - l |} \bigg) ^ {1 / p} \bigg (\sum_ {l \in \mathbb {Z} ^ {d}} | \hat {g} (l) | ^ {q} e ^ {2 \pi \lambda q | l |} \bigg) ^ {1 / q}. \end{array}
$$

Proof of Proposition 4.8. (i) We use the (multi-dimensional) Fa\`a di Bruno formula:

$$
(f \circ H) ^ {(n)} = \sum_ {\sum_ {j = 1} ^ {n} j m _ {j} = n} \frac {n !}{m _ {1} ! \dots m _ {n} !} (f ^ {(m _ {1} + \dots + m _ {n})} \circ H) \prod_ {j = 1} ^ {n} \left(\frac {H ^ {(j)}}{j !}\right) ^ {m _ {j}};
$$

so

$$
\| (f \circ H) ^ {(n)} \| _ {L ^ {p}} \leqslant \sum_ {\sum_ {j = 1} ^ {n} j m _ {j} = n} \frac {n !}{m _ {1} ! \dots m _ {n} !} \| f ^ {(m _ {1} + \dots + m _ {n})} \circ H \| _ {L ^ {p}} \prod_ {j = 1} ^ {n} \left\| \frac {H ^ {(j)}}{j !} \right\| _ {\infty} ^ {m _ {j}};
$$

and thus

$$
\begin{aligned} & \sum_{n\geqslant 1}\frac{\lambda^{n}}{n!}\| (f\circ H)^{(n)}\|_{L^{p}}\\ & \leqslant \| (\det \nabla H)^{-1}\|_{\infty}^{1 / p}\sum_{k = 1}^{\infty}\| f^{(k)}\|_{L^{p}}\sum_{\substack{\sum_{j = 1}^{n}jm_{j} = n\\ \sum_{j = 1}^{n}m_{j} = k}}\frac{\lambda^{n}}{m_{1}!\ldots m_{n}!}\prod_{j = 1}^{n}\bigg\| \frac{H^{(j)}}{j!}\bigg\|_{\infty}^{m_{j}}\\ & = \| (\det \nabla H)^{-1}\|_{\infty}^{1 / p}\sum_{k\geqslant 1}\| f^{(k)}\|_{L^{p}}\frac{1}{k!}\bigg(\sum_{|l|\geqslant 1}\frac{\lambda^{l}}{l!}\| H^{(l)}\|_{\infty}\bigg)^{k}, \end{aligned}
$$

where the last step follows from the multi-dimensional binomial formula.

(ii) We decompose$h ( x ) { : = } f ( a x { + } G ( x ) )$as

$$
h (x) = \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {f ^ {(n)} (a x)}{n !} G (x) ^ {n}
$$

and we apply$\nabla ^ { k }$:

$$
\nabla^{k}h(x) = \sum_{\substack{k_{1},k_{2}\in \mathbb{N}_{0}^{d}\\ k_{1} + k_{2} = k}}\sum_{n\in \mathbb{N}_{0}^{d}}\frac{k!a^{k_{1}}}{k_{1}!k_{2}!n!}\nabla^{k_{1} + n}f(ax)\nabla^{k_{2}}G^{n}(x).
$$

Then we take the$L ^ { p }$norm, multiply by$\lambda ^ { k } / k !$and sum over$k \colon$

$$
\begin{array}{l} \| h \| _ {\mathcal {C} ^ {\lambda ; p}} \leqslant | a | ^ {- d / p} \sum_ {k _ {1}, k _ {2}, n \geqslant 0} \frac {\lambda^ {k _ {1} + k _ {2}} | a | ^ {k _ {1}}}{k _ {1} ! k _ {2} ! n !} \| \nabla^ {k _ {1} + n} f \| _ {L ^ {p}} \| \nabla^ {k _ {2}} G ^ {n} \| _ {\infty} \\ = | a | ^ {- d / p} \sum_ {k _ {1}, n \geqslant 0} \frac {\lambda^ {k _ {1}} | a | ^ {k _ {1}}}{k _ {1} ! n !} \| \nabla^ {k _ {1} + n} f \| _ {L ^ {p}} \| G ^ {n} \| _ {\mathcal {C} ^ {\lambda}} \\ \leqslant | a | ^ {- d / p} \sum_ {k _ {1}, n \geqslant 0} \frac {\lambda^ {k _ {1}} | a | ^ {k _ {1}}}{k _ {1} ! n !} \| \nabla^ {k _ {1} + n} f \| _ {L ^ {p}} \| G \| _ {\mathcal {C} ^ {\lambda}} ^ {n} \\ = | a | ^ {- d / p} \sum_ {m \geqslant 0} \frac {(a \lambda + \| G \| _ {\mathcal {C} ^ {\lambda}}) ^ {m}}{m !} \| \nabla^ {m} f \| _ {L ^ {p}}, \end{array}
$$

where Proposition 4.5 (iii) was used in the second-last step.

(iii) In this case we write, with$G _ { 0 } = \widehat { G } ( 0 )$,

$$
h (x) = f (x + G (x)) = \sum_ {k \in \mathbb {Z} ^ {d}} \hat {f} (k) e ^ {2 i \pi k \cdot x} e ^ {2 i \pi k \cdot G _ {0}} e ^ {2 i \pi k \cdot (G (x) - G _ {0})};
$$

so

$$
\hat {h} (l) = \sum_ {k \in \mathbb {Z} ^ {d}} \hat {f} (k) e ^ {2 i \pi k \cdot G _ {0}} [ e ^ {2 i \pi k \cdot (G - G _ {0})} ] ^ {\wedge} (l - k).
$$

Then, using again Proposition 4.5,

$$
\begin{array}{l} \sum_ {l \in \mathbb {Z} ^ {d}} | \hat {h} (l) | e ^ {2 \pi \lambda | l |} \leqslant \sum_ {l, k \in \mathbb {Z} _ {d}} | \hat {f} (k) | e ^ {2 \pi \lambda | k |} e ^ {2 \pi \lambda | l - k |} | [ e ^ {2 i \pi k \cdot (G - G _ {0})} ] ^ {\wedge} (l - k) | \\ = \sum_ {k \in \mathbb {Z} ^ {d}} | \hat {f} (k) | e ^ {2 \pi \lambda | k |} \| e ^ {2 i \pi k \cdot (G - G _ {0})} \| _ {\lambda} \\ \leqslant \sum_ {k \in \mathbb {Z} _ {d}} | \hat {f} (k) | e ^ {2 \pi \lambda | k |} e ^ {\| 2 \pi k \cdot (G - G _ {0}) \| _ {\lambda}} \\ \leqslant \sum_ {k \in \mathbb {Z} ^ {d}} | \hat {f} (k) | e ^ {2 \pi \lambda | k |} e ^ {2 \pi | k | \| G - G _ {0} \| _ {\lambda}} \\ = \| f \| _ {\lambda + \| G - G _ {0} \| _ {\lambda}} \\ = \| f \| _ {\lambda + \nu}, \end{array}
$$

where$\nu { = } \| G \| _ { \dot { \mathcal { F } } ^ { \lambda } }$

(iv) We actually have the more precise result

$$
\| f \circ H \| _ {\mathcal {C} ^ {\lambda}} \leqslant \sum_ {k \in \mathbb {Z} ^ {d}} | \hat {f} (k) | e ^ {2 \pi | k | \| H \| _ {\dot {\mathcal {C}} ^ {\lambda}}}.\tag{4.5}
$$

Writing$\textstyle f \circ H = \sum _ { k \in \mathbb { Z } ^ { d } } { \hat { f } } ( k ) e ^ { 2 i \pi k \cdot H }$, we see that (4.5) follows from

$$
\| e ^ {i h} \| _ {\mathcal {C} ^ {\lambda}} \leqslant e ^ {\| h \| _ {\dot {\mathcal {C}} ^ {\lambda}}}.\tag{4.6}
$$

To prove (4.6), let$P _ { n }$be the polynomial in the variables$X _ { m } , \ m \leqslant n ,$defined by the identity

$$
(e ^ {f}) ^ {(n)} = P _ {n} ((f ^ {(m)}) _ {m \leqslant n}) e ^ {f};
$$

this polynomial (which can be made more explicit from the Fa\`a di Bruno formula) has non-negative coeficients, so$\| ( e ^ { i f } ) ^ { ( n ) } \| _ { \infty } \leqslant P _ { n } ( ( \| f ^ { ( m ) } \| ) _ { m \leqslant n } )$. The conclusion will follow from the identity (between formal series!)

$$
1 + \sum_ {n \in \mathbb {N} _ {*} ^ {d}} \frac {\lambda^ {n}}{n !} P _ {n} ((X _ {m}) _ {m \leqslant n}) = \exp \biggl (\sum_ {k \in \mathbb {N} _ {*} ^ {d}} \frac {\lambda^ {k}}{k !} X _ {k} \biggr).\tag{4.7}
$$

To prove (4.7), it is suficient to note that the left-hand side is the expansion of$e ^ { g }$in powers of λ at 0, where

$$
g (\lambda) = \sum_ {k \in \mathbb {N} _ {*} ^ {d}} \frac {\lambda^ {k}}{k !} X _ {k}.
$$

Proof of Proposition 4.10. (a) Writing$\| \cdot \| _ { \lambda ; p } { = } \| \cdot \| _ { \mathcal { C } ^ { \lambda ; p } }$, we have

$$
\| \partial_ {j} f \| _ {\lambda ; p} = \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \| \partial_ {x} ^ {n} \partial_ {j} f \| _ {L ^ {p}},
$$

where$\partial _ { j } = \partial / \partial x _ { j }$. If$1 _ { j }$is the d-tuple of integers with 1 in position$j$and 0 elsewhere, then$( n + 1 _ { j } ) ! \leqslant ( | n | + 1 ) n !$, so

$$
\| \partial_ {j} f \| _ {\lambda ; p} \leqslant \sup _ {n \in \mathbb {N} _ {0} ^ {d}} \frac {(| n | + 1) \lambda^ {n}}{\bar {\lambda} ^ {n + 1}} \sum_ {| m | \geqslant 1} \frac {\bar {\lambda} ^ {m}}{m !} \| \nabla^ {m} f \| _ {L ^ {p}},
$$

and the proof of (4.3) follows easily.

(b) Writing$\| \cdot \| _ { \lambda ; p } { = } \| \cdot \| _ { \mathcal { F } ^ { \lambda ; p } }$, we have

$$
\begin{array}{l} \| \partial_ {j} f \| _ {\lambda ; p} = \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} | k _ {j} | ^ {p} | \hat {f} (k) | ^ {p} e ^ {2 \pi \lambda p | k |} \bigg) ^ {1 / p} \\ \leqslant \bigg (\sup _ {k \in \mathbb {Z} ^ {d}} | k | e ^ {2 \pi (\lambda - \bar {\lambda}) | k |} \bigg) \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} | \hat {f} (k) | ^ {p} e ^ {2 \pi \bar {\lambda} p | k |} \bigg) ^ {1 / p}, \end{array}
$$

and (4.4) follows.

## 4.2. Analytic norms in two variables

To estimate solutions and trajectories of kinetic equations we will work on the phase space $\mathbb { T } _ { x } ^ { d } \times \mathbb { R } _ { v } ^ { d }$, and use three parameters: λ (gliding analytic regularity),$\mu$(analytic regularity in x) and$\tau$(time-shift along the free transport semigroup). The regularity quantified by $\lambda$is said to be gliding because for$\tau { = } 0$this is an analytic regularity in$v ,$, but as$\tau$grows the regularity is progressively transferred from velocity to spatial modes, according to the evolution by free transport. This catch is crucial to our analysis: indeed, the solution of a transport equation like free transport or Vlasov cannot be uniformly$\mathrm { a n a l y t i c } ( ^ { 1 6 } )$in v as time goes by—except of course if it is spatially homogeneous. Instead, the best we can do is compare the solution at time$\tau$to the solution of free transport at the same time.

The parameters$\lambda$and$\mu$will be non-negative; τ will vary in$\mathbb { R } ,$, but often be restricted to$\mathbb { R } _ { + }$, just because we shall work in positive time. When$\tau$is not specified, this means $\tau { = } 0$. Sometimes we shall abuse notation by writing$\| f ( x , v ) \|$instead of$\| f \|$, to stress the dependence of$f$on the two variables.

Putting aside the time-shift for a moment, we may generalize the norms$\mathcal { C } ^ { \lambda }$and${ \mathcal { F } } ^ { \lambda }$ in an obvious way.

(<sup>16</sup>)$\mathrm { B y }$this we mean of course that some norm or seminorm quantifying the degree of analytic smoothness in v will remain uniformly bounded.

Definition 4.11. (Two-variables analytic norms) For any$\lambda , \mu \geqslant 0$, we define

$$
\| f \| _ {\mathcal {C} ^ {\lambda , \mu}} = \sum_ {m \in \mathbb {N} _ {0} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \frac {\mu^ {m}}{m !} \| \nabla_ {x} ^ {m} \nabla_ {v} ^ {n} f \| _ {L ^ {\infty} (\mathbb {T} _ {x} ^ {d} \times \mathbb {R} _ {v} ^ {d})},\tag{4.8}
$$

$$
\| f \| _ {\mathcal {F} ^ {\lambda , \mu}} = \sum_ {k \in \mathbb {Z} ^ {d}} \int_ {\mathbb {R} ^ {d}} | \tilde {f} (k, \eta) | e ^ {2 \pi \lambda | \eta |} e ^ {2 \pi \mu | k |} d \eta .\tag{4.9}
$$

Of course one might also introduce variants based on$L ^ { p }$or$\ell ^ { p \ }$norms (with two additional parameters$p$and$q ,$, since one can make diferent choices for the space and velocity variables).

The norm (4.9) is better adapted to the periodic nature of the problem, and is very well suited to estimate solutions of kinetic equations (with fast decay as$| v | \to \infty )$; but in the sequel we shall also have to estimate characteristics (trajectories) which are unbounded functions of$v .$. We could hope to play with two diferent families of norms, but this would entail considerable technical dificulties. Instead, we shall mix the two recipes to get the following hybrid norms.

Definition 4.12. (Hybrid analytic norms) For any$\lambda , \mu \geqslant 0$, let

$$
\| f \| _ {\mathcal {Z} ^ {\lambda , \mu}} = \sum_ {l \in \mathbb {Z} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} e ^ {2 \pi \mu | l |} \| \widehat {\nabla_ {v} ^ {n}} f (l, v) \| _ {L ^ {\infty} (\mathbb {R} _ {v} ^ {d})}.\tag{4.10}
$$

More generally, for any$p { \in } [ 1 , \infty ]$, we define

$$
\| f \| _ {\mathcal {Z} ^ {\lambda , \mu ; p}} = \sum_ {l \in \mathbb {Z} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} e ^ {2 \pi \mu | l |} \| \widehat {\nabla_ {v} ^ {n}} f (l, v) \| _ {L ^ {p} (\mathbb {R} _ {v} ^ {d})}.\tag{4.11}
$$

Now let us introduce the time-shift τ. We denote by$( S _ { \tau } ^ { 0 } ) _ { \tau \geqslant 0 }$the geodesic semigroup: $( S _ { \tau } ^ { 0 } ) ( x , v ) { = } ( x { + } v \tau , v )$. Recall that the backward free transport semigroup is defined by $( f \circ S _ { \tau } ^ { 0 } ) _ { \tau \geqslant 0 }$, and the forward semigroup by$( f \circ S _ { - \tau } ^ { 0 } ) _ { \tau \geqslant 0 }$

Definition 4.13. (Time-shift pure and hybrid analytic norms)

$$
\| f \| _ {\mathcal {C} _ {\tau} ^ {\lambda , \mu}} = \| f \circ S _ {\tau} ^ {0} \| _ {\mathcal {C} ^ {\lambda , \mu}} = \sum_ {m \in \mathbb {N} _ {0} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \frac {\mu^ {m}}{m !} \| \nabla_ {x} ^ {m} (\nabla_ {v} + \tau \nabla_ {x}) ^ {n} f \| _ {L ^ {\infty} (\mathbb {T} _ {x} ^ {d} \times \mathbb {R} _ {v} ^ {d})},\tag{4.12}
$$

$$
\| f \| _ {\mathcal {F} _ {\tau} ^ {\lambda , \mu}} = \| f \circ S _ {\tau} ^ {0} \| _ {\mathcal {F} ^ {\lambda , \mu}} = \sum_ {k \in \mathbb {Z} ^ {d}} \int_ {\mathbb {R} ^ {d}} | \tilde {f} (k, \eta) | e ^ {2 \pi \lambda | k \tau + \eta |} e ^ {2 \pi \mu | k |} d \eta ,\tag{4.13}
$$

$$
\| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} = \| f ^ {\circ} S _ {\tau} ^ {0} \| _ {\mathcal {Z} ^ {\lambda , \mu}} = \sum_ {l \in \mathbb {Z} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} e ^ {2 \pi \mu | l |} \| (\nabla_ {v} + 2 i \pi \tau l) ^ {n} \hat {f} (l, v) \| _ {L ^ {\infty} (\mathbb {R} _ {v} ^ {d})},\tag{4.14}
$$

$$
\| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} = \sum_ {l \in \mathbb {Z} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} e ^ {2 \pi \mu | l |} \| (\nabla_ {v} + 2 i \pi \tau l) ^ {n} \hat {f} (l, v) \| _ {L ^ {p} (\mathbb {R} _ {v} ^ {d})}.\tag{4.15}
$$

This choice of norms is one of the cornerstones of our analysis: first, because of their hybrid nature, they will connect well to both periodic (in x) estimates on the force field, and uniform (in v) estimates on the “deflection maps” studied in$\ S 5$. Secondly, they are well behaved with respect to the properties of free transport, allowing us to keep track of the initial time. Thirdly, they will satisfy the algebra property (for$p { = } \infty )$, the composition inequality and the gradient inequality (for any$p \in [ 1 , \infty ] )$). Before going on with the proof of these properties, we note the following alternative representations.

Proposition 4.14. The norm$\mathcal { Z } _ { \tau } ^ { \lambda , \mu ; p }$admits the following alternative representations:

$$
\| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} = \sum_ {l \in \mathbb {Z} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} e ^ {2 \pi \mu | l |} \| \nabla_ {v} ^ {n} (\hat {f} (l, v) e ^ {2 i \pi \tau l \cdot v}) \| _ {L ^ {p} (\mathbb {R} _ {v} ^ {d})},\tag{4.16}
$$

$$
\| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} = \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \| (\nabla_ {v} + \tau \nabla_ {x}) ^ {n} f \| _ {\mu ; p},\tag{4.17}
$$

where

$$
\| g \| _ {\mu ; p} = \sum_ {l \in \mathbb {Z} ^ {d}} e ^ {2 \pi \mu | l |} \| \hat {g} (l, v) \| _ {L ^ {p} (\mathbb {R} _ {v} ^ {d})}.\tag{4.18}
$$

## 4.3. Relations between functional spaces

The next propositions are easily checked.

Proposition 4.15. With the notation from 4.2, for any$\tau \in \mathbb { R }$,

(i) if f is a function only of x then

$$
\| f \| _ {\mathcal {C} _ {\tau} ^ {\lambda , \mu}} = \| f \| _ {\mathcal {C} ^ {\lambda | \tau | + \mu}} \quad a n d \quad \| f \| _ {\mathcal {F} _ {\tau} ^ {\lambda , \mu}} = \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} = \| f \| _ {\mathcal {F} ^ {\lambda | \tau | + \mu}};
$$

(ii) if f is a function only of v then

$$
\| f \| _ {\mathcal {C} _ {\tau} ^ {\lambda , \mu ; p}} = \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} = \| f \| _ {\mathcal {C} ^ {\lambda ; p}} \quad a n d \quad \| f \| _ {\mathcal {F} _ {\tau} ^ {\lambda , \mu}} = \| f \| _ {\mathcal {F} ^ {\lambda}};
$$

(iii) for any function$f { = } f ( x , v )$, if stands for spatial average then

$$
\left\| \left\langle f \right\rangle \right\| _ {\mathcal {C} ^ {\lambda ; p}} \leqslant \left\| f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}};
$$

(iv) for any function$f = f ( x , v )$

$$
\left\| \int_ {\mathbb {R} ^ {d}} f d v \right\| _ {\mathcal {F} ^ {\lambda | \tau | + \mu}} \leqslant \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}}.
$$

Remark 4.16. Note, in Proposition 4.15 (i) and$( \mathrm { i v } )$, how the regularity in x is improved by the time-shift.

Proof. Only (iv) requires some explanations. Let

$$
\varrho (x) = \int_ {\mathbb {R} ^ {d}} f (x, v) d v.
$$

Then for any$k \in  { \mathbb { Z } ^ { d } }$

$$
\hat {\varrho} (k) = \int_ {\mathbb {R} ^ {d}} \hat {f} (k, v) d v;
$$

so for any$\boldsymbol { n } \in  { \mathbb { N } } _ { 0 } ^ { d }$

$$
(2 i \pi t k) ^ {n} \hat {\varrho} (k) = \int_ {\mathbb {R} ^ {d}} (2 i \pi t k) ^ {n} \hat {f} (k, v) d v = \int_ {\mathbb {R} ^ {d}} (\nabla_ {v} + 2 i \pi t k) ^ {n} \hat {f} (k, v) d v.
$$

Recalling the conventions from Appendix A.1 we deduce

$$
\sum_{\substack{k\in \mathbb{Z}^{d}\\ n\in \mathbb{N}_{0}^{d}}}e^{2\pi \mu |k|}\frac{|2\pi\lambda tk|^{n}}{n!} |\hat{\varrho} (k)|\leqslant \sum_{\substack{k\in \mathbb{Z}^{d}\\ n\in \mathbb{N}_{0}^{d}}}e^{2\pi \mu |k|}\frac{\lambda^{n}}{n!}\int_{\mathbb{R}^{d}}|( \nabla_{v} + 2i\pi tk)^{n}\hat{f} (k,v)|  dv = \| f\|_{\mathcal{Z}_{t}^{\lambda ,\mu ;1}}.\square
$$

Proposition 4.17. With the notation from 4.2,

$$
\lambda \leqslant \lambda^ {\prime} a n d \mu \leqslant \mu^ {\prime} \quad \Longrightarrow \quad \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda^ {\prime}, \mu^ {\prime}}}.
$$

Moreover, for$\tau , \bar { \tau } { \in } \mathbb { R }$and any$p { \in } [ 1 , \infty ]$,

$$
\left\| f \right\| _ {\mathcal {Z} _ {\bar {\tau}} ^ {\lambda , \mu ; p}} \leqslant \left\| f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu + \lambda | \bar {\tau} - \tau |; p}}.\tag{4.19}
$$

Remark 4.18. Note carefully that the spaces$\mathcal { Z } _ { \tau } ^ { \lambda , \mu }$are not ordered with respect to the parameter$\tau ,$, which cannot be thought of as a regularity index. We could dispend with this parameter if we were working in time$O ( 1 )$; but (4.19) is of course of absolutely no use. This means that errors on the exponent τ should remain somehow small, in order to be controllable by small losses on the exponent$\mu .$

Finally we state an easy proposition which follows from the time invariance of the free transport equation.

Proposition 4.19. For any$X \in \{ \mathcal { C } , \mathcal { F } , \mathcal { Z } \}$and any$t , \tau { \in } \mathbb { R }$

$$
\left\| f \circ S _ {t} ^ {0} \right\| _ {X _ {\tau} ^ {\lambda , \mu}} = \left\| f \right\| _ {X _ {t + \tau} ^ {\lambda , \mu}}.
$$

Now we shall see that the hybrid norms, and certain variants thereof, enjoy properties rather similar to those of the single-variable analytic norms studied before. This will sometimes be technical, and the reader who would like to reconnect to physical problems is advised to go directly to 4.11.

## 4.4. Injections

In this section we relate$\mathcal { Z } _ { \tau } ^ { \lambda , \mu ; p }$norms to more standard norms entirely based on Fourie space. In the next theorem we write

$$
\| f \| _ {\mathcal {Y} _ {\tau} ^ {\lambda , \mu}} := \| f \| _ {\mathcal {F} _ {\tau} ^ {\lambda , \mu ; \infty}} = \sup _ {k \in \mathbb {Z} ^ {d}} \sup _ {\eta \in \mathbb {R} ^ {d}} e ^ {2 \pi \mu | k |} e ^ {2 \pi \lambda | \eta + k \tau |} | \tilde {f} (k, \eta) |.\tag{4.20}
$$

Theorem 4.20. (Injections between analytic spaces) (i)$I f ~ \lambda , \mu \geqslant 0$and$\tau \in \mathbb { R }$then

$$
\| f \| _ {\mathcal {Y} _ {\tau} ^ {\lambda , \mu}} \leqslant \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}}.\tag{4.21}
$$

(ii) I$\scriptstyle f \ 0 < \lambda < \bar { \lambda } , \ 0 < \mu < \bar { \mu } \leqslant M$and$\tau \in \mathbb { R }$, then

$$
\| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant \frac {C (d , \bar {\mu})}{(\bar {\lambda} - \lambda) ^ {d} (\bar {\mu} - \mu) ^ {d}} \| f \| _ {\mathcal {Y} _ {\tau} ^ {\bar {\lambda}, \bar {\mu}}}.\tag{4.22}
$$

(iii) If$0 < \lambda < \bar { \lambda } \leqslant \Lambda , \ 0 < \mu < \bar { \mu } \leqslant M$and$b { \leqslant } \beta { \leqslant } B$, then there is$C = C ( \Lambda , M , b , B , d )$ such that

$$
\begin{array}{l} \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}} \leqslant C ^ {1 / \min \{\bar {\lambda} - \lambda , \bar {\mu} - \mu \}} \\ \qquad \times \bigg (\| f \| _ {\mathcal {Y} _ {\tau} ^ {\bar {\lambda}, \bar {\mu}}} + \max \bigg \{\int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} | f (x, v) | e ^ {\beta | v |}   d v   d x, \left(\int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} | f (x, v) | e ^ {\beta | v |}   d v   d x\right) ^ {2} \bigg \} \bigg). \end{array}
$$

Remark 4.21. The combination of (ii) and (iii), plus elementary Lebesgue interpolation, enables us to control all norms$\mathcal { Z } _ { \tau } ^ { \lambda , \mu ; p } , 1 { \leqslant } p { \leqslant } \infty$

Proof. By the invariance under the action of free transport, it is suficient to do the proof for$\tau { = } 0$

By integration by parts in the Fourier transform formula, we have

$$
\tilde {f} (k, \eta) = \int_ {\mathbb {R} ^ {d}} \hat {f} (k, v) e ^ {- 2 i \pi \eta \cdot v} d v = \int_ {\mathbb {R} ^ {d}} \nabla_ {v} ^ {m} \hat {f} (k, v) \frac {e ^ {- 2 i \pi \eta \cdot v}}{(2 i \pi \eta) ^ {m}} d v.
$$

So

$$
| \tilde {f} (k, \eta) | \leqslant \frac {1}{(2 \pi | \eta |) ^ {m}} \int_ {\mathbb {R} ^ {d}} | \nabla_ {v} ^ {m} \hat {f} (k, v) | d v;
$$

and therefore

$$
\begin{array}{c} e ^ {2 \pi \mu | k |} e ^ {2 \pi \lambda | \eta |} | \tilde {f} (k, \eta) | \leqslant e ^ {2 \pi \mu | k |} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {(2 \pi \lambda) ^ {n}}{n !} | \eta | ^ {n} | \tilde {f} (k, \eta) | \\ \leqslant e ^ {2 \pi \mu | k |} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \int_ {\mathbb {R} ^ {d}} | \nabla_ {v} ^ {n} \tilde {f} (k, v) |   d v. \end{array}
$$

This establishes (i).

Next, by diferentiating the identity

$$
\hat {f} (k, v) = \int_ {\mathbb {R} ^ {d}} \tilde {f} (k, \eta) e ^ {2 i \pi \eta \cdot v} d \eta ,
$$

we get

$$
\nabla_ {v} ^ {m} \hat {f} (k, v) = \int_ {\mathbb {R} ^ {d}} \tilde {f} (k, \eta) (2 i \pi \eta) ^ {m} e ^ {2 i \pi \eta \cdot v} d \eta .\tag{4.23}
$$

Then we deduce (ii) by writing

$$
\begin{array}{l}\sum_{\substack{k\in \mathbb{Z}^{d}\\ m\in \mathbb{N}_{0}^{d}}}e^{2\pi \mu |k|}\frac{\lambda^{m}}{m!}\| \nabla_{v}^{m}\hat{f} (k,v)\|_{L^{\infty}(dv)}\\ \leqslant \sum_{k\in \mathbb{Z}^{d}}e^{2\pi \mu |k|}\int_{\mathbb{R}^{d}}e^{2\pi \lambda |\eta |}|\tilde{f} (k,\eta)|  d\eta \\ \leqslant \left(\sum_{k\in \mathbb{Z}^{d}}e^{-2\pi (\bar{\mu} -\mu)|k|}\right)\left(\int_{\mathbb{R}^{d}}e^{-2\pi (\bar{\lambda} -\lambda)|\eta |}  d\eta\right)\sup_{\substack{k\in \mathbb{Z}^{d}\\ \eta \in \mathbb{R}^{d}}}|\tilde{f} (k,\eta)|e^{2\pi \bar{\lambda} |\eta |}e^{2\pi \bar{\mu} |k|}. \end{array}
$$

The proof of (iii) is the most tricky. We start again from (4.23), but now we integrate by parts in the η variable:

$$
\nabla_ {v} ^ {m} \hat {f} (k, v) = (- 1) ^ {q} \int_ {\mathbb {R} ^ {d}} \nabla_ {\eta} ^ {q} [ \tilde {f} (k, \eta) (2 i \pi \eta) ^ {m} ] \frac {e ^ {2 i \pi \eta \cdot v}}{(2 i \pi v) ^ {q}} d v,\tag{4.24}
$$

where$q { = } q ( v )$is a multi-index to be chosen.

We split$\mathbb { R } _ { v } ^ { d }$into$2 ^ { d }$disjoint regions$\Delta ( i _ { 1 } , . . . , i _ { n } )$, where$i _ { 1 } , . . . , i _ { n }$are distinct indices in$\{ 1 , . . . , d \}$:

$$
\Delta (I) = \{v \in \mathbb {R} ^ {d}: | v _ {j} | \geqslant 1 \text {   for   all   } j \in I \text {   and   } | v _ {j} | <   1 \text {   for   all   } j \notin I \}.
$$

If$v \in \Delta ( i _ { 1 } , . . . , i _ { n } )$we apply (4.24) with the multi-index q defined by

$$
q _ {j} = \left\{ \begin{array}{l l} 2, & \text { if } j \in \{i _ {1},..., i _ {n} \}, \\ 0, & \text { otherwise }. \end{array} \right.
$$

This gives

$$
\begin{array}{l}\int_{\Delta (i_{1},\ldots ,i_{n})}|\nabla_{v}^{m}\hat{f} (k,v)|  dv\\ \qquad \leqslant \left(\frac{1}{(2\pi)^{2n}}\int_{\Delta (i_{1},\ldots ,i_{n})}\frac{dv_{i_{1}}\ldots dv_{i_{n}}}{|v_{i_{1}}|^{2}\ldots|v_{i_{n}}|^{2}}\right)\sup_{\substack{k\in \mathbb{Z}^{d}\\ \eta \in \mathbb{R}^{d}}}|\nabla_{\eta}^{q}[\tilde{f} (k,\eta)(2i\pi \eta)^{m}]|. \end{array}
$$

Summing up all pieces and using the Leibniz formula, we get

$$
\int_{\mathbb{R}^{d}}|\nabla_{v}^{m}\hat{f} (k,v)|  dv\leqslant C(d)(1 + m^{2d})\sup_{\substack{k\in \mathbb{Z}^{d}\\ \eta \in \mathbb{R}^{d}}}\sup_{|q|\leqslant 2d}|\nabla_{\eta}^{q}\tilde{f} (k,\eta)|  |2\pi \eta |^{m - q}.
$$

At this point we apply Lemma 4.22 below with

$$
\varepsilon = \frac {1}{4} \min \biggl \{\frac {\bar {\lambda} - \lambda}{\bar {\lambda}}, \frac {\bar {\mu} - \mu}{\bar {\mu}} \biggr \},
$$

and we get, for$q \leqslant 2 d .$

$$
\begin{array}{l}|\nabla_{\eta}^{q}\tilde{f} (k,\eta)|\leqslant C(d)^{\max \{\bar{\lambda} /(\bar{\lambda} - \lambda),\bar{\mu} /(\bar{\mu} - \mu)\}}K(b,B)e^{-\pi (\lambda +\bar{\lambda})|\eta |}\Big(\sup_{\eta \in \mathbb{R}^{d}}|\tilde{f} (k,\eta)|e^{2\pi \bar{\lambda} |\eta |}\Big)^{1 - \varepsilon}\\ \\ \times \max \bigg\{\left(\sup_{\substack{l\in \mathbb{N}_{0}^{d}\\ \eta \in \mathbb{R}^{d}}}\frac{\beta^{l}\|\nabla_{\eta}^{l}\tilde{f}\|_{\infty}}{l!}\right)^{\varepsilon},\left(\sup_{\substack{l\in \mathbb{N}_{0}^{d}\\ \eta \in \mathbb{R}^{d}}}\frac{\beta^{l}\|\nabla_{\eta}^{l}\tilde{f}\|_{\infty}}{l!}\right)^{2\varepsilon}\bigg\} . \end{array}
$$

Of course,

$$
\begin{array}{r l} & {\frac {\beta^ {l} | \nabla_ {\eta} ^ {l} \tilde {f} (k , \eta) |}{l !} \leqslant (2 \pi \beta) ^ {l} \int_ {\mathbb {R} ^ {d}} | \hat {f} (k, v) | \frac {| v | ^ {l}}{l !} d v} \\ & {\quad \leqslant \int_ {\mathbb {R} ^ {d}} | f (x, v) | (2 \pi \beta) ^ {l} \frac {| v | ^ {l}}{l !} d v \leqslant \int_ {\mathbb {R} ^ {d}} | f (x, v) | e ^ {2 \pi \beta | v |} d v.} \end{array}
$$

So, all in all,

$$
\begin{array}{l} \sum_ {\substack {k \in \mathbb {Z} ^ {d} \\ m \in \mathbb {N} _ {0} ^ {d}}} e ^ {2 \pi \mu | k |} \frac {\lambda^ {m}}{m !} \int_ {\mathbb {R} ^ {d}} | \nabla_ {v} ^ {m} \hat {f} (k, v) |   d v \\ \leqslant \sum_ {| q | \leqslant 2 d} C (d, \Lambda , M, b, B) ^ {1 / \min \{\bar {\lambda} - \lambda , \bar {\mu} - \mu \}} \\ \times \bigg (\sup_ {\eta \in \mathbb {R} ^ {d}} e ^ {- \pi (\lambda + \bar {\lambda}) | \eta |} \sum_ {m \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {m} (1 + m) ^ {2 d} | 2 \pi \eta | ^ {m - q}}{m !} \bigg) \\ \times \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} e ^ {- 2 \pi (\bar {\mu} (1 - \varepsilon) - \mu) | k |} \bigg) \bigg (\sup_ {\substack {k \in \mathbb {Z} ^ {d} \\ \eta \in \mathbb {R} ^ {d}}} | \tilde {f} (k, \eta) | e ^ {2 \pi \bar {\mu} | k |} e ^ {2 \pi \bar {\lambda} | \eta |} \bigg) ^ {1 - \varepsilon} \\ \times \max \bigg \{\bigg (\int_ {\mathbb {R} ^ {d}} | f (x, v) | e ^ {\beta | v |}   d v \bigg) ^ {\varepsilon}, \bigg (\int_ {\mathbb {R} ^ {d}} | f (x, v) | e ^ {\beta | v |}   d v \bigg) ^ {2 \varepsilon} \bigg \}. \\ \sum_ {m \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {m} (1 + m) ^ {2 d} | 2 \pi \eta | ^ {m - q}}{m !} \leqslant C (q, \Lambda) e ^ {\pi (\lambda + \bar {\lambda}) | \eta |} \\ \end{array}
$$

Since

and

$$
\sum_ {k \in \mathbb {Z} ^ {d}} e ^ {- 2 \pi (\bar {\mu} (1 - \varepsilon) - \mu) | k |} \leqslant \sum_ {k \in \mathbb {Z} ^ {d}} e ^ {- \pi (\bar {\mu} - \mu) | k |} \leqslant \frac {C}{(\bar {\mu} - \mu) ^ {d}},
$$

we easily end up with the desired result.

Lemma 4.22. Let$f \colon  { \mathbb { R } ^ { d } } \to  { \mathbb { C } }$and let$\alpha { > } 0 , A { \geqslant } 1$and$q \in \mathbb { N } _ { 0 } ^ { d }$. Let further$\beta$be such that$0 < b \leqslant \beta \leqslant B$$I f \ | f ( x ) | { \leqslant } A e ^ { - \alpha | x | }$for all$x ,$then for any$\varepsilon \in \left( 0 , { \frac { 1 } { 4 } } \right)$, one has

$$
\begin{array}{l} | \nabla^ {q} f (x) | \leqslant C (q, d) ^ {1 / \varepsilon} K (b, B) A ^ {1 - \varepsilon} e ^ {- (1 - 2 \varepsilon) \alpha | x |} \\ \qquad \times \sup _ {r \in \mathbb {N} _ {0} ^ {d}} \max \biggl \{\left(\beta^ {r} \frac {\| \nabla^ {r} f \| _ {\infty}}{r !}\right) ^ {\varepsilon}, \left(\beta^ {r} \frac {\| \nabla^ {r} f \| _ {\infty}}{r !}\right) ^ {2 \varepsilon} \biggr \}. \end{array}\tag{4.25}
$$

Remark 4.23. One may conjecture that the optimal constant in the right-hand side of (4.25) is in fact polynomial in$1 / \varepsilon ;$if this conjecture holds true, then the constants in Theorem 4.20 (iii) can be improved accordingly. Mironescu communicated to us a derivation of polynomial bounds for the optimal constant in the related inequality

$$
\| f ^ {(k)} \| _ {L ^ {\infty} (\mathbb {R})} \leqslant C (k) \| f \| _ {L ^ {1} (\mathbb {R})} ^ {1 / (k + 2)} \| f ^ {(k + 1)} \| _ {L ^ {\infty} (\mathbb {R})} ^ {(k + 1) / (k + 2)},
$$

based on a real interpolation method.

Proof. Let us first see$f$as a function of$x _ { 1 }$, and treat$x ^ { \prime } { = } ( x _ { 2 } , . . . , x _ { d } )$as a parameter. Thus the assumption is$| f ( x _ { 1 } , x ^ { \prime } ) | \leqslant ( A e ^ { - \alpha | x ^ { \prime } | } ) e ^ { - \alpha | x _ { 1 } | }$. By a more or less standard interpolation inequality [22, Lemma$\mathrm { A . 1 } ]$,

$$
\left| \partial_ {1} f \left(x _ {1}, x ^ {\prime}\right) \right| \leqslant 2 \sqrt {A e ^ {- \alpha | x ^ {\prime} |}} \sqrt {e ^ {- \alpha | x _ {1} |}} \| \partial_ {1} ^ {2} f \left(x _ {1}, x ^ {\prime}\right) \| _ {\infty} ^ {1 / 2} = 2 \sqrt {A e ^ {- \alpha | x |}} \sqrt {\| \partial_ {1} ^ {2} f \| _ {\infty}}.\tag{4.26}
$$

Let$C _ { q _ { 1 } , r _ { 1 } }$be the optimal constant (not smaller than 1) such that

$$
\left| \partial_ {1} ^ {q _ {1}} f \left(x _ {1}, x ^ {\prime}\right) \right| \leqslant C _ {q _ {1}, r _ {1}} \left(A e ^ {- \alpha | x |}\right) ^ {1 - q _ {1} / r _ {1}} \| \partial_ {r} ^ {r _ {1}} f \left(x _ {1}, x ^ {\prime}\right) \| _ {\infty} ^ {q _ {1} / r _ {1}}.\tag{4.27}
$$

By iterating (4.26), we find$C _ { q _ { 1 } , r _ { 1 } } { \leqslant } 2 \sqrt { C _ { q _ { 1 } - 1 , r _ { 1 } } C _ { q _ { 1 } + 1 , r _ { 1 } } } .$It follows by induction that

$$
C _ {q, r} \leqslant 2 ^ {q (r - q)}.
$$

Next, using (4.27) and interpolating according to the second variable$x _ { 2 }$as in (4.26), we get

$$
\begin{array}{l} | \partial_ {2} ^ {q _ {2}} \partial_ {1} ^ {q _ {1}} f (x) | \\ \leqslant C _ {q _ {2}, r _ {2}} (C _ {q _ {1}, r _ {1}} (A e ^ {- \alpha | x |}) ^ {1 - q _ {1} / r _ {1}} \| \partial_ {1} ^ {r _ {1}} f \| _ {\infty} ^ {q _ {1} / r _ {1}}) ^ {1 - q _ {2} / r _ {2}} \| \partial_ {2} ^ {r _ {2}} \partial_ {1} ^ {q _ {1}} f \| _ {\infty} ^ {q _ {2} / r _ {2}} \\ \leqslant C _ {q _ {1}, r _ {1}} C _ {q _ {2}, r _ {2}} (A e ^ {- \alpha | x |}) ^ {(1 - q _ {1} / r _ {1}) (1 - q _ {2} / r _ {2})} \| \partial_ {1} ^ {r _ {1}} f \| _ {\infty} ^ {(q _ {1} / r _ {1}) (1 - q _ {2} / r _ {2})} \| \partial_ {2} ^ {r _ {2}} \partial_ {1} ^ {q _ {1}} f \| _ {\infty} ^ {q _ {2} / r _ {2}}. \end{array}
$$

We repeat this until we get

$$
\begin{array}{l} \left| \nabla^ {q} f (x) \right| \leqslant C _ {q _ {1}, r _ {1}} \dots C _ {q _ {d}, r _ {d}} \left(A e ^ {- \alpha | x |}\right) ^ {\left(1 - q _ {1} / r _ {1}\right) \dots \left(1 - q _ {d} / r _ {d}\right)} \\ \times \| \partial_ {1} ^ {r _ {1}} f \| _ {\infty} ^ {\left(q _ {1} / r _ {1}\right) \left(1 - q _ {2} / r _ {2}\right) \dots \left(1 - q _ {d} / r _ {d}\right)} \| \partial_ {1} ^ {q _ {1}} \partial_ {2} ^ {r _ {2}} f \| ^ {\left(q _ {2} / r _ {2}\right) \left(1 - q _ {3} / r _ {3}\right) \dots \left(1 - q _ {d} / r _ {d}\right)} \\ \dots \| \partial_ {1} ^ {q _ {1}} \partial_ {2} ^ {q _ {2}} \dots \partial_ {d - 1} ^ {q _ {d - 1}} \partial_ {d} ^ {r _ {d}} f \| ^ {q _ {d} / r _ {d}}. \end{array} \tag {4}\tag{4.28}
$$

Choose$r _ { j } , 1 { \leqslant } j { \leqslant } d ,$in such a way that

$$
\frac {\varepsilon}{d} \leqslant \frac {q _ {j}}{r _ {j}} \leqslant \frac {2 \varepsilon}{d};
$$

this is always possible for$\textstyle \varepsilon < { \frac { 1 } { 4 } } d .$. Then$C _ { q _ { j } , r _ { j } } \leqslant ( 2 ^ { d q _ { j } ^ { 2 } } ) ^ { 1 / \varepsilon }$, and (4.28) implies that

$$
| \nabla^ {q} f (x) | \leqslant (2 ^ {d | q | ^ {2}}) ^ {1 / \varepsilon} (A e ^ {- \alpha | x |}) ^ {1 - \varepsilon} \max _ {s \leqslant r + q} \{\| \nabla^ {s} f \| _ {\infty} ^ {\varepsilon}, \| \nabla^ {s} f \| _ {\infty} ^ {2 \varepsilon} \}.
$$

Then, since$2 ( r + q ) \varepsilon \leqslant 3 d q$, we have, by a crude application of Stirling’s formula (in quantitative form), for$s { \leqslant } r { \ + } q$

$$
\| \nabla^ {s} f \| _ {\infty} ^ {\varepsilon} \leqslant \left(\frac {\beta^ {s} \| \nabla^ {s} f \| _ {\infty}}{s !}\right) ^ {\varepsilon} \left(\frac {s !}{\beta^ {s}}\right) ^ {\varepsilon} \leqslant \left(\sup _ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\beta^ {n} \| \nabla^ {n} f \| _ {\infty}}{n !}\right) ^ {\varepsilon} C (\beta , q, d) \varepsilon^ {- 3 d q},
$$

and the result easily follows.

## 4.5. Algebra property in two variables

In this section we only consider the norms$\mathcal { Z } _ { \tau } ^ { \lambda , \mu ; p } ;$; but similar results would hold true for the two-variables spaces and${ \mathcal F } ,$and could be proven with the same methods as those used for the one-variable spaces${ \mathcal { F } } ^ { \lambda }$and$\mathcal { C } ^ { \lambda }$, respectively (note that the Leibniz formula still applies because$\nabla _ { x }$and$\nabla _ { v } + \tau \nabla _ { x }$commute).

Proposition 4.24. (i) For any$\lambda , \mu \geqslant 0$, any$\tau \in \mathbb { R }$and any$p , q , r \in [ 1 , \infty ]$such that $1 / p + 1 / q { = } 1 / r$, we have

$$
\left\| f g \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; r}} \leqslant \left\| f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \left\| g \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; q}}.
$$

(ii) As a consequence,$\mathcal { Z } _ { \tau } ^ { \lambda , \mu } { = } \mathcal { Z } _ { \tau } ^ { \lambda , \mu ; \infty }$is a normed algebra:

$$
\left\| f g \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant \left\| f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \left\| g \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.
$$

In particular,$\| f ^ { n } \| _ { \mathcal { Z } _ { \tau } ^ { \lambda , \mu } } \leqslant \| f \| _ { \mathcal { Z } _ { \tau } ^ { \lambda , \mu } } ^ { n }$<sub>μ</sub> for any$\textstyle n \in \mathbb { N } _ { 0 }$, and$\| e ^ { f } \| _ { \mathcal { Z } _ { \tau } ^ { \lambda , \mu } } \leqslant e ^ { \| f \| _ { \mathcal { Z } _ { \tau } ^ { \lambda , \mu } } }$

Proof. First we note that (with the notation$\left( 4 . 1 8 \right) \ \Downarrow \cdot \| _ { \mu ; r }$satisfies the$\ ^ { \left. \right)} ( p , q , r$ property”: whenever$p , q , r \in [ 1 , \infty ]$satisfy$1 / p + 1 / q = 1 / r$, we have

$$
\begin{array}{l} \| f g \| _ {\mu ; r} = \sum_ {l \in \mathbb {Z} ^ {d}} e ^ {2 \pi \mu | l |} \| \hat {f} g (l, \cdot) \| _ {L ^ {r} (\mathbb {R} _ {v} ^ {d})} \\ \qquad = \sum_ {l \in \mathbb {Z} ^ {d}} e ^ {2 \pi \mu | l |} \bigg \| \sum_ {k \in \mathbb {Z} ^ {d}} \hat {f} (k, \cdot) \hat {g} (l - k, \cdot) \bigg \| _ {L ^ {r} (\mathbb {R} _ {v} ^ {d})} \\ \qquad \leqslant \sum_ {l \in \mathbb {Z} ^ {d}} \sum_ {k \in \mathbb {Z} ^ {d}} e ^ {2 \pi \mu | k |} e ^ {2 \pi \mu | l - k |} \| \hat {f} (k, \cdot) \| _ {L ^ {p} (\mathbb {R} _ {v} ^ {d})} \| \hat {g} (l - k, \cdot) \| _ {L ^ {q} (\mathbb {R} _ {v} ^ {d})} \\ \qquad = \| f \| _ {\mu ; p} \| g \| _ {\mu ; q}. \end{array}
$$

Next, we write

$$
\begin{array}{l} \left\| f g \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; r}} = \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \left\| (\nabla_ {v} + \tau \nabla_ {x}) ^ {n} (f g) \right\| _ {\mu ; r} \\ \qquad = \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \left\| \sum_ {m \leqslant n} \binom {n} {m} (\nabla_ {v} + \tau \nabla_ {x}) ^ {m} f (\nabla_ {v} + \tau \nabla_ {x}) ^ {n - m} g \right\| _ {\mu ; r} \\ \qquad \leqslant \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \sum_ {m \leqslant n} \binom {n} {m} \left\| (\nabla_ {v} + \tau \nabla_ {x}) ^ {m} f \right\| _ {\mu ; p} \left\| (\nabla_ {v} + \tau \nabla_ {x}) ^ {n - m} g \right\| _ {\mu ; q} \\ \qquad = \bigg (\sum_ {m \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {m}}{m !} \| (\nabla_ {v} + \tau \nabla_ {x}) ^ {m} f \| _ {\mu ; p} \bigg) \sum_ {l \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {l}}{l !} \| (\nabla_ {v} + \tau \nabla_ {x}) ^ {l} f \| _ {\mu ; q} \\ \qquad = \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \| g \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; q}}. \end{array}
$$

(We could also reduce to$\tau { = } 0$by means of Proposition 4.19.)

## 4.6. Composition inequality

Proposition 4.25. (Composition inequality in two variables) For any$\lambda , \mu \geqslant 0$and any$p \in [ 1 , \infty ] , \tau \in \mathbb { R } , \sigma \in \mathbb { R } , a \in \mathbb { R } \backslash \{ 0 \}$and$b \in \mathbb { R }$,

$$
\left\| f (x + b v + X (x, v), a v + V (x, v)) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant | a | ^ {- d / p} \| f \| _ {\mathcal {Z} _ {\sigma} ^ {\alpha , \beta ; p}},\tag{4.29}
$$

where

$$
\alpha = \lambda | a | + \| V \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \quad a n d \quad \beta = \mu + \lambda | b + \tau - a \sigma | + \| X - \sigma V \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.\tag{4.30}
$$

Remark 4.26. The norms in (4.30) for X and V have to be based on$L ^ { \infty }$, not just any$L ^ { p }$. Also note that the fact that the second argument of f has the form$a v { + V }$(and not$a v + c x + V )$is related to Remark 4.7.

Proof. The proof is a combination of the arguments in Proposition 4.8. In a first step, we do it for the case$\scriptstyle { \tau = \sigma = 0 }$, and we write$\| \cdot \| _ { \lambda , \mu ; p } = \| \cdot \| _ { \mathcal { Z } _ { 0 } ^ { \lambda , \mu ; p } }$

From the expansion$\begin{array} { r } { f ( x , v ) { = } \sum _ { k \in \mathbb { Z } ^ { d } } \hat { f } ( k , v ) e ^ { 2 i \pi k \cdot x } } \end{array}$we deduce that

$$
\begin{array}{l}h(x,v):= f(x + bv + X(x,v),av + V(x,v))\\ = \sum_{k\in \mathbb{Z}^{d}}\hat{f} (k,av + V)e^{2i\pi k\cdot (x + bv + X)}\\ = \sum_{\substack{k\in \mathbb{Z}^{d}\\ m\in \mathbb{N}_{0}^{d}}}\nabla_{v}^{m}\hat{f} (k,av)\cdot \frac{V^{m}}{m!} e^{2i\pi k\cdot x}e^{2i\pi k\cdot bv}e^{2i\pi k\cdot X}. \end{array}
$$

Taking the Fourier transform in x, we see that for any$l \in \mathbb { Z } ^ { d }$,

$$
\hat{h} (l,v) = \sum_{\substack{k\in \mathbb{Z}^{d}\\ m\in \mathbb{N}_{0}^{d}}}\nabla_{v}^{m}\hat{f} (k,av)e^{2i\pi k\cdot bv}\sum_{j\in \mathbb{Z}^{d}}\frac{(\widehat{V^{m}})(j)}{m!}(e^{2i\pi k\cdot X})^{\wedge}(l - k - j).
$$

Diferentiating n times via the Leibniz formula (here applied to a product of four func tions), we get

$$
\begin{array}{l}\nabla_{v}^{n}\hat{h} (l,v) = \sum_{\substack{k,j\in \mathbb{Z}^{d}\\ m,n_{1},n_{2},n_{3},n_{4}\in \mathbb{N}_{0}^{d}\\ n_{1} + n_{2} + n_{3} + n_{4} = n}}\frac{n!a^{n_{1}}}{n_{1}!n_{2}!n_{3}!n_{4}!}\nabla_{v}^{m + n_{1}}\hat{f} (k,av)\\ \\ \times \frac{\nabla_{v}^{n_{2}}(\widehat{V^{m}})(j)}{m!}\nabla_{v}^{n_{3}}(e^{2i\pi k\cdot X})^{\wedge}(l - k - j,v)(2i\pi bk)^{n_{4}}e^{2i\pi k\cdot bv}. \end{array}
$$

Multiplying by$\lambda ^ { n } e ^ { 2 \pi \mu | l | } / n !$and summing over n and$l ,$taking$L ^ { p }$norms and using $\| f g \| _ { L ^ { p } } \leqslant \| f \| _ { L ^ { p } } \| g \| _ { L ^ { \infty } }$, we finally obtain

$$
\begin{array} { l } h \| _ { \lambda , \mu } \\ \leqslant | a | ^ { - d / p } \sum _ { k , j , l \in \mathbb { Z } ^ { d } } \frac { \lambda ^ { n } e ^ { 2 \pi \mu | l | } | a | ^ { n _ { 1 } } } { n _ { 1 } ! n _ { 2 } ! n _ { 3 } ! n _ { 4 } ! } \| \nabla _ { v } ^ { m + n _ { 1 } } \hat { f } ( k , \cdot ) \| _ { L ^ { p } } \left\| \frac { \nabla _ { v } ^ { n _ { 2 } } ( \widehat { V ^ { m } } ) ( j ) } { m ! } \right\| _ { \infty } \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \times \| \nabla _ { v } ^ { n _ { 3 } } ( e ^ { 2 i \pi k \cdot X } ) ^ { \wedge } ( l - k - j ) \| _ { \infty } ( 2 \pi | b |   | k | ) ^ { n _ { 4 } } \\ = | a | ^ { - d / p } \sum _ { k , j , l \in \mathbb { Z } ^ { d } } \frac { \lambda ^ { n _ { 1 } + n _ { 2 } + n _ { 3 } + n _ { 4 } } e ^ { 2 \pi \mu | k | } e ^ { 2 \pi \mu | j | } e ^ { 2 \pi \mu | l - k - j | } | a | ^ { n _ { 1 } } } { n _ { 1 } ! n _ { 2 } ! n _ { 3 } ! n _ { 4 } ! } \| \nabla _ { v } ^ { m + n _ { 1 } } \hat { f } ( k , \cdot ) \| _ { L ^ { p } } \\ \qquad \qquad \qquad \qquad \qquad \times \left\| \frac { \nabla _ { v } ^ { n _ { 2 } } ( \widehat { V ^ { m } } ) ( j ) } { m ! } \right\| _ { \infty } \| \nabla _ { v } ^ { n _ { 3 } } ( e ^ { 2 i \pi k \cdot X } ) ^ { \wedge } ( l - k - j ) \| _ { \infty } ( 2 \pi | b |   | k | ) ^ { n _ { 4 } } \\ \leqslant | a | ^ { - d / p } \sum _ { k \in \mathbb { Z } ^ { d } } \frac { \lambda ^ { n _ { 1 } } | a | ^ { n _ { 1 } } } { n _ { 1 } ! } \| \nabla _ { v } ^ { n _ { 1 } + m } \hat { f } ( k , \cdot ) \| _ { L ^ { p } } e ^ { 2 \pi \mu | k | } \\ \qquad \qquad \qquad \times \left( \frac { 1 } { m ! } \sum _ { j \in \mathbb { Z } ^ { d } } \frac { \lambda ^ { n _ { 2 } } } { n _ { 2 } ! } e ^ { 2 \pi \mu | j | } \| \nabla _ { v } ^ { n _ { 2 } } ( \widehat { V ^ { m } } ) ( j ) \| _ { \infty }\right) \\ \qquad \qquad \qquad \times \left( \sum _ { h \in \mathbb { Z } ^ { d } } \frac { \lambda ^ { n _ { 3 } } } { n _ { 3 } ! } e ^ { 2 \pi \mu | h | } \| \nabla _ { v } ^ { n _ { 3 } } ( e ^ { 2 i \pi k \cdot X } ) ^ { \wedge } ( h ) \| _ { \infty }\right) \sum _ { n _ { 4 } \in \mathbb { N } _ { 0 } ^ { d } } \frac { ( 2 \pi \lambda | b |   | k | ) ^ { n _ { 4 } } } { n _ { 4 } ! } \\ = | a | ^ {- d / p} \sum _ { k \in \mathbb { Z } ^ { d } } \frac { ( \lambda | a | ) ^ { n _ { 1 } } } { n _ { 1 } ! } e ^ { 2 \pi \mu | k | } \| \nabla _ { v } ^ { n _ { 1} + m} \hat { f } ( k , \cdot ) \| _ { L ^ { p }} \frac {\| V ^ { m} \| _ {\lambda , \mu}}{m !} \| e ^ { 2 i \pi k \cdot X } \| _ {\lambda , \mu} e ^ { 2 \pi \lambda | b |   | k | } \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y ] [ z ] [ w ] [ x ] [ y] [ z ] [ w ] [ x ] [ y] [ z ] [ w ] [ x ] [ y] [ z] [ w ] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] [ y] [ z] [ w] [ x] {[ x ]} {[ y ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ x ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ t ]} {[ s t r i g e c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r c o r s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s a l l i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i n i l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l l / a. \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = | a | ^ {- d / p} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {\bigl (} {{\bf k}, {\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{\bf k}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}} {{8}}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & ={| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^ {- d / p}} \\ & = {| a | ^{- d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}} \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {| a |^{ - d / p}}, \\ & = {\bigl (}
$$

$$
\begin{array}{l}\leqslant |a|^{-d / p}\sum_{\substack{k\in \mathbb{Z}^{d}\\ n_{1},m\in \mathbb{N}_{0}^{d}}}\frac{(\lambda|a|)^{n_{1}}}{n_{1}!} e^{2\pi (\mu +\lambda |b|)|k|}\| \nabla_{v}^{n_{1} + m}\hat{f} (k,\cdot)\|_{L^{p}}\frac{\|V\|_{\lambda,\mu}^{m}}{m!} e^{2\pi |k|\| X\|_{\lambda ,\mu}}\\ \\ = |a|^{-d / p}\sum_{\substack{k\in \mathbb{Z}^{d}\\ n\in \mathbb{N}_{0}^{d}}}\frac{1}{n!} (\lambda |a| + \| V\|_{\lambda ,\mu})^{n}\| \nabla_{v}^{n}\hat{f} (k,\cdot)\|_{L^{\bar{p}}}  e^{2\pi |k|(\mu +\lambda |b| + \| X\|_{\lambda ,\mu})}\\ \\ = |a|^{-d / p}\| f\|_{\lambda |a| + \| V\|_{\lambda ,\mu},\mu +\lambda |b| + \| X\|_{\lambda ,\mu}}. \end{array}
$$

Now we generalize this to arbitrary values of σ and τ. By Proposition 4.19,

$$
\begin{array}{l} \| f (x + b v + X (x, v), a v + V (x, v)) \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \\ \quad = \| f (x + v (b + \tau) + X (x + v \tau , v), a v + V (x + v \tau , v)) \| _ {\mathcal {Z} ^ {\lambda , \mu ; p}} \\ \quad = \| f \circ S _ {\sigma} ^ {0} \circ S _ {- \sigma} ^ {0} (x + v (b + \tau) + X (x + v \tau , v), a v + V (x + v \tau , v)) \| _ {\mathcal {Z} ^ {\lambda , \mu ; p}} \\ \quad = \| (f \circ S _ {\sigma} ^ {0}) (x + v (b + \tau - a \sigma) + (X - \sigma V) (x + v \tau , v), a v + V (x + v \tau , v)) \| _ {\mathcal {Z} ^ {\lambda , \mu ; p}} \\ \quad = \| (f \circ S _ {\sigma} ^ {0}) (x + v (b + \tau - a \sigma) + Y (x, v), a v + W (x, v)) \| _ {\mathcal {Z} ^ {\lambda , \mu ; p}}, \end{array}
$$

where

$$
W (x, v) = V \circ S _ {\tau} ^ {0} (x, v) \quad \text { and } \quad Y (x, v) = (X - \sigma V) \circ S _ {\tau} ^ {0} (x, v).
$$

Applying the result for$\tau { = } 0$, we deduce that the norm of

$$
h (x, v) = f (x + b v + X (x, v), a v + V (x, v))
$$

in$\mathcal { Z } _ { \tau } ^ { \lambda , \mu }$is bounded by

$$
\left\| f \circ S _ {\sigma} ^ {0} \right\| _ {\mathcal {Z} ^ {\alpha , \beta ; p}} = \left\| f \right\| _ {\mathcal {Z} _ {\sigma} ^ {\alpha , \beta ; p}},
$$

where

$$
\alpha = \lambda | a | + \| V \circ S _ {\tau} ^ {0} \| _ {\mathcal {Z} ^ {\lambda , \mu}} = | a | \lambda + \| V \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}
$$

and

$$
\beta = \mu + \lambda | b + \tau - a \sigma | + \| (X - \sigma V) \circ S _ {\tau} ^ {0} \| _ {\mathcal {Z} ^ {\lambda , \mu}} = \mu + \lambda | b + \tau - a \sigma | + \| X - \sigma V \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.
$$

This establishes the desired bound.

## 4.7. Gradient inequality

In the next proposition we shall write

$$
\| f \| _ {\dot {\mathcal {Z}} _ {\tau} ^ {\lambda , \mu}} = \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \| (\nabla_ {v} + 2 i \pi \tau l) ^ {n} \hat {f} (l, v) \| _ {L ^ {\infty} (\mathbb {R} _ {v} ^ {d})} e ^ {2 \pi \mu | l |}.\tag{4.31}
$$

This is again a homogeneous (in the x variable) seminorm.

Proposition 4.27. For$\bar { \lambda } { > } { \lambda } { \geqslant } 0$and$\bar { \mu } { > } \mu { \geqslant } 0$, we have the functional inequalities

$$
\begin{array}{c} \| \nabla_ {x} f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant \frac {C (d)}{\bar {\mu} - \mu} \| f \| _ {\dot {\mathcal {Z}} _ {\tau} ^ {\lambda , \bar {\mu}; p}}, \\ \| (\nabla_ {v} + \tau \nabla_ {x}) f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant \frac {C (d)}{\lambda \log (\bar {\lambda} / \lambda)} \| f \| _ {\mathcal {Z} _ {\tau} ^ {\bar {\lambda}, \mu ; p}}. \end{array}
$$

In particular, for$\tau { \geqslant } 0$we have

$$
\left\| \nabla_ {v} f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant C (d) \left(\frac {1}{\lambda \log (\bar {\lambda} / \lambda)} \| f \| _ {\mathcal {Z} _ {\tau} ^ {\bar {\lambda}, \bar {\mu}; p}} + \frac {\tau}{\bar {\mu} - \mu} \| f \| _ {\dot {\mathcal {Z}} _ {\tau} ^ {\bar {\lambda}, \bar {\mu}; p}}\right).
$$

The proof is similar to that of Proposition 4.10; the constant$C ( d )$arises in the choice of norm on$\mathbb { R } ^ { d }$. As a consequence, if$1 < \bar { \lambda } / \lambda \leqslant 2$, we have$\mathrm { e . g . }$the bound

$$
\| \nabla f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant C (d) \left(\frac {1}{\bar {\lambda} - \lambda} + \frac {1 + \tau}{\bar {\mu} - \mu}\right) \| f \| _ {\mathcal {Z} _ {\tau} ^ {\bar {\lambda}, \bar {\mu}; p}}.
$$

## 4.8. Inversion

From the composition inequality follows an inversion estimate.

Proposition 4.28. (Inversion inequality) (i) Let$\lambda , \mu \geqslant 0 , \tau \in$<sup>R</sup> and consider a function$F \colon  { \mathbb { T } } ^ { d } \times  { \mathbb { R } } ^ { d } \to  { \mathbb { T } } ^ { d } \times  { \mathbb { R } } ^ { d }$. Then there is$\varepsilon { = } \varepsilon ( d )$such that if F satisfies

$$
\left\| \nabla (F - \operatorname{Id}) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant \varepsilon (d),
$$

where

$$
\lambda^ {\prime} = \lambda + 2 \| F - \operatorname{Id} \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \quad a n d \quad \mu^ {\prime} = \mu + 2 (1 + | \tau |) \| F - \operatorname{Id} \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}},
$$

then$F$is invertible and

$$
\left\| F ^ {- 1} - \operatorname{Id} \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant 2 \| F - \operatorname{Id} \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.\tag{4.32}
$$

(ii) More generally, if$F , G \colon  { \mathbb { T } } ^ { d } \times  { \mathbb { R } } ^ { d } {  }  { \mathbb { T } } ^ { d } \times  { \mathbb { R } } ^ { d }$are such that

$$
\left\| \nabla (F - \mathrm{Id}) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant \varepsilon (d),\tag{4.33}
$$

where

$$
\lambda^ {\prime} = \lambda + 2 \| F - G \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \quad a n d \quad \mu^ {\prime} = \mu + 2 (1 + | \tau |) \| F - G \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}},
$$

then F is invertible and

$$
\left\| F ^ {- 1} \circ G - \operatorname{Id} \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant 2 \| F - G \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.\tag{4.34}
$$

Remark 4.29. The conditions become very stringent as τ becomes large: basically, F Id (or$F { - } G$in case (ii)) should be of order$o ( 1 / \tau )$for Proposition 4.28 to be applicable.

Remark 4.30. By Proposition 4.27, a suficient condition for (4.33) to hold is that there be$\lambda ^ { \prime \prime }$and$\mu ^ { \prime \prime }$such that$\lambda \leqslant \lambda ^ { \prime \prime } \leqslant 2 \lambda$,$\mu { \leqslant } \mu ^ { \prime \prime }$and

$$
\| F - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau} ^ {\lambda^ {\prime \prime}, \mu^ {\prime \prime}}} \leqslant \frac {\varepsilon^ {\prime} (d)}{1 + \tau} \min \{\lambda^ {\prime \prime} - \lambda^ {\prime}, \mu^ {\prime \prime} - \mu^ {\prime} \}.
$$

However, this condition is in practice hard to fulfill.

Proof. We prove only (ii), being (i) a particular case. Let$f { = } F { - } \mathrm { I d } , h { = } F ^ { - 1 } { \circ } G { - } \mathrm { I d }$ and$g { = } G { - } \operatorname { I d }$, so that${ \mathrm { I d } } + g = ( { \mathrm { I d } } + f ) \circ ( { \mathrm { I d } } + h )$, or equivalently

$$
h = g - f \circ (\mathrm{Id} + h).
$$

Thus h is a fixed point of

$$
\Phi \colon Z \longmapsto g - f \circ (\operatorname{Id} + Z).
$$

Note that$\Phi ( 0 ) { = } g - f$. If Φ is$\scriptstyle { \frac { 1 } { 2 } } - \mathrm { L i p s c h i t z }$on the ball$B ( 0 , 2 \| f - g \| )$in$\mathcal { Z } _ { \tau } ^ { \lambda , \mu }$, then (4.34) will follow by fixed-point iteration as in Theorem A.2. (Here$B ( x , r ) { : = } \{ y { : } \| x { - } y \| { \leqslant } r \} . )$

So let$Z$and$\widetilde { Z }$be given with

$$
\left\| Z \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}, \left\| \widetilde {Z} \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant 2 \| f - g \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.
$$

We have

$$
\Phi (Z) - \Phi (\widetilde {Z}) = f (\mathrm{Id} + \widetilde {Z}) - f (\mathrm{Id} + Z) = (\widetilde {Z} - Z) \cdot \int_ {0} ^ {1} \nabla f (\mathrm{Id} + (1 - \theta) Z + \theta \widetilde {Z}) d \theta .
$$

By Proposition 4.24,

$$
\| \Phi (Z) - \Phi (\widetilde {Z}) \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant \| \widetilde {Z} - Z \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \int_ {0} ^ {1} \| \nabla f (\mathrm{Id} + (1 - \theta) Z + \theta \widetilde {Z}) \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} d \theta .
$$

For any$\theta \in [ 0 , 1 ]$, by Proposition 4.25,

$$
\left\| \nabla f (\mathrm{Id} + (1 - \theta) Z + \theta \widetilde {Z}) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant \left\| \nabla f \right\| _ {\mathcal {Z} _ {\tau} ^ {\hat {\lambda}, \hat {\mu}}},
$$

where

$$
\hat {\lambda} = \lambda + \max \{\| Z \|, \| \widetilde {Z} \| \} \leqslant \lambda + 2 \| f - g \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}
$$

and, writing${ Z = } ( Z _ { x } , Z _ { v } )$and$\widetilde { Z } = ( \widetilde { Z } _ { x } , \widetilde { Z } _ { v } )$,

$$
\hat {\mu} = \mu + \max \{\| Z _ {x} - \tau Z _ {v} \|, \| \widetilde {Z} _ {x} - \tau \widetilde {Z} _ {v} \| \} \leqslant \mu + 2 (1 + | \tau |) \| f - g \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.
$$

If$F$and G satisfy the assumptions of Proposition 4.28, we deduce that

$$
\left\| \Phi \right\| _ {\operatorname{Lip} (B (0, 2))} \leqslant C (d) \varepsilon (d),
$$

and this is bounded above by$\textstyle { \frac { 1 } { 2 } } { \mathrm { ~ i f ~ } } \varepsilon ( d )$is small enough.

## 4.9. Sobolev corrections

We shall need to quantify Sobolev regularity corrections to the analytic regularity, in the x variable.

Definition 4.31. (Hybrid analytic norms with Sobolev corrections) For$\lambda , \mu , \gamma \geqslant 0$, $\tau \in \mathbb { R }$and$p { \in } [ 1 , \infty ]$we define

$$
\begin{array}{c} \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma); p}} = \sum_ {l \in \mathbb {Z} ^ {d}} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} e ^ {2 \pi \mu | l |} (1 + | l |) ^ {\gamma} \| (\nabla_ {v} + 2 i \pi \tau l) ^ {n} \hat {f} (l, v) \| _ {L ^ {p} (\mathbb {R} _ {v} ^ {d})}, \\ \| f \| _ {\mathcal {F} ^ {\lambda , \gamma}} = \sum_ {k \in \mathbb {Z} ^ {d}} e ^ {2 \pi \lambda | k |} (1 + | k |) ^ {\gamma} | \hat {f} (k) |. \end{array}
$$

Proposition 4.32. Let$\lambda , \mu , \gamma \geqslant 0 , \tau \in \mathbb { R }$and$p { \in } [ 1 , \infty ]$. We have the following functional (in)equalities.

(i)$\| f \| _ { \mathcal { Z } _ { t + \tau } ^ { \lambda , ( \mu , \gamma ) ; p } } = \| f \circ S _ { t } ^ { 0 } \| _ { \mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) ; p } } ;$

(ii)$I f { \ 1 / p + 1 / q = 1 / r }$then$\left\| f g \right\| _ { \mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) ; r } } \leqslant \left\| f \right\| _ { \mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) ; p } } \left\| g \right\| _ { \mathcal { Z } _ { \tau } ^ { \lambda } }$,(μ,γ);q , and therefore in particular$\mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) } { = } \mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) ; \infty }$is a normed algebra;

(iii) If f depends only on x then$\| f \| _ { \mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) } } = \| f \| _ { \mathcal { F } ^ { \lambda | \tau | + \mu , \gamma } } .$

(iv)$\begin{array} { r } { \left. f \right. _ { \mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) ; p } } \leqslant \left. f \right. _ { \mathcal { Z } _ { \tau } ^ { \lambda , ( \mu + \lambda | \tau - \bar { \tau } | , \gamma ) ; p } } ; } \end{array}$

(v) For any$\sigma { \in } \mathbb { R } , a { \in } \mathbb { R } \backslash \{ 0 \}$and$b \in \mathbb { R }$

$$
\left\| f (x + b v + X (x, v), a v + V (x, v)) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma); p}} \leqslant | a | ^ {- d / p} \| f \| _ {\mathcal {Z} _ {\sigma} ^ {\alpha , (\beta , \gamma); p}},
$$

where

$$
\alpha = \lambda | a | + \| V \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma)}} \quad a n d \quad \beta = \mu + \lambda | b \tau - a \sigma | + \| X - \sigma V \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma)}};
$$

(vi) Gradient inequality:

$$
\begin{array}{l} \| \nabla_ {x} f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma); p}} \leqslant \frac {C (d)}{\bar {\mu} - \mu} \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\bar {\mu}, \gamma); p}}, \\ \| \nabla f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma); p}} \leqslant C (d) \left(\frac {1}{\bar {\lambda} - \lambda} + \frac {1 + \tau}{\bar {\mu} - \mu}\right) \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\bar {\mu}, \gamma); p}}; \end{array}
$$

(vii) Inversion: if$F , G \colon  { \mathbb { T } } ^ { d } \times  { \mathbb { R } } ^ { d } {  }  { \mathbb { T } } ^ { d } \times  { \mathbb { R } } ^ { d }$are such that

$$
\left\| \nabla (F - \operatorname{Id}) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda^ {\prime}, (\mu^ {\prime}, \gamma)}} \leqslant \varepsilon (d),
$$

where

$$
\lambda^ {\prime} = \lambda + 2 \| F - G \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma)}} \quad a n d \quad \mu^ {\prime} = \mu + 2 (1 + | \tau |) \| F - G \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma)}},
$$

then

$$
\left\| F ^ {- 1} \circ G - \operatorname{Id} \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma)}} \leqslant 2 \left\| F - G \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma)}}.\tag{4.35}
$$

Proof. The proofs are the same as for the “plain” hybrid norms; the only notable point is that for the proof of (ii) we use, in addition to$e ^ { 2 \pi \lambda | k | } \leqslant e ^ { 2 \pi \lambda | k - l | } e ^ { 2 \pi \lambda | l | }$, the inequality

$$
(1 + | k |) ^ {\gamma} \leqslant (1 + | k - l |) ^ {\gamma} (1 + | l |) ^ {\gamma}.
$$

Remark 4.33. Of course, some of the estimates in Proposition 4.32 can be “improved” by taking advantage of$\gamma ; \mathrm { e . g . }$for$\gamma \geqslant 1$we have

$$
\left\| \nabla_ {x} f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant C (d) \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , (\mu , \gamma); p}}.
$$

## 4.10. Individual mode estimates

To handle very singular cases, we shall at times need to estimate Fourier modes individually, rather than full norms. If$f = f ( x , v )$, we write

$$
(P _ {k} f) (x, v) = \hat {f} (k, v) e ^ {2 i \pi k \cdot x}.\tag{4.36}
$$

In particular the following estimates will be useful.

Proposition 4.34. For any$\lambda , \mu \geqslant 0 , \tau \in \mathbb { R }$, Lebesgue exponents$1 / r { = } 1 / p { + } 1 / q$and $k \in  { \mathbb { Z } ^ { d } }$, we have the estimate

$$
\| P _ {k} (f g) \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; r}} \leqslant \sum_ {l \in \mathbb {Z} ^ {d}} \| P _ {l} f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \| P _ {k - l} g \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; q}}.
$$

Proposition 4.35. For any$\lambda > 0 , \bar { \mu } \geqslant \mu \geqslant 0 , \tau \in \mathbb { R } , p \in [ 1 , \infty ]$and$k \in  { \mathbb { Z } ^ { d } }$, we have the estimate

$$
\| P _ {k} [ f (x + X (x, v), v) ] \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant \sum_ {l \in \mathbb {Z} ^ {d}} e ^ {- 2 \pi (\bar {\mu} - \mu) | k - l |} \| P _ {l} f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \nu ; p}}, \quad \nu = \mu + \| X \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \bar {\mu}}}.
$$

These estimates also have variants with Sobolev corrections. Note that when$\mu { = } \bar { \mu }$, Proposition 4.35 is a direct consequence of Proposition 4.25 with$V { = } 0 , b { = } 0$and$a { = } 1 { : }$

$$
\left\| P _ {k} [ f (x + X (x, v), v) ] \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant \left\| f (x + X (x, v), v) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; p}} \leqslant \left\| f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \nu ; p}}, \quad \nu = \mu + \| X \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}.
$$

Proof of Propositions 4.34 and 4.35. The proof of Proposition 4.34 is quite similar to the proof of Proposition 4.24. (It is no restriction to choose$\tau { = } 0$because$P _ { k }$commutes with the free transport semigroup.) Proposition 4.35 needs a few words of explanation. As in the proof of Proposition 4.25 we let$h ( x , v ) { = } f ( x { + } X ( x , v ) , v )$), and readily obtain

$$
\begin{array}{l}\| P_{k}h\|_{\mathcal{Z}_{\tau}^{\lambda ,\mu ;p}} = \sum_{n\in \mathbb{N}_{0}^{d}}\frac{\lambda^{n}e^{2\pi\mu|k|}}{n!}\| \nabla_{v}^{n}\hat{h} (k,v)\|_{L^{p}(dv)}\\ \\ \leqslant \sum_{\substack{n\in \mathbb{N}_{0}^{d}\\ l\in \mathbb{Z}^{d}}}\frac{\lambda^{n}e^{2\pi\mu|k|}}{n!}\| \nabla_{v}^{n}\hat{f} (l,v)\|_{L^{p}(dv)}\sum_{m\in \mathbb{N}_{0}^{d}}\frac{\lambda^{m}}{m!}\| \nabla_{v}^{m}(e^{2i\pi lX})^{\wedge}(k - l,v)\|_{L^{\infty}(dv)}. \end{array}
$$

At this stage we write

$$
e ^ {2 \pi \mu | k |} \leqslant e ^ {2 \pi \mu | l |} e ^ {- 2 \pi (\bar {\mu} - \mu) | k - l |} e ^ {2 \pi \bar {\mu} | k - l |},
$$

and use the following crude bound, which holds for all$l \in \mathbb { Z } ^ { d }$

$$
e ^ {2 \pi \bar {\mu} | k - l |} \| \nabla_ {v} ^ {m} (e ^ {2 i \pi l X}) ^ {\wedge} (k - l, v) \| _ {L ^ {\infty} (d v)} \leqslant \sum_ {j \in \mathbb {Z} ^ {d}} e ^ {2 \pi \bar {\mu} | j |} \| \nabla_ {v} ^ {m} (e ^ {2 i \pi l X}) ^ {\wedge} (j, v) \| _ {L ^ {\infty} (d v)}.
$$

The rest of the proof is as in Proposition 4.25.

## 4.11. Measuring solutions of kinetic equations in large time

As we already discussed, even for the simplest kinetic equation, namely free transport, we cannot hope to have uniform-in-time regularity estimates in the velocity variable: rather, because of filamentation, we may have$\| \nabla _ { v } f ( t , \cdot ) \| = O ( t ) , \ \| \nabla _ { v } ^ { 2 } f ( t , \cdot ) \| = O ( t ^ { 2 } )$, etc. For analytic norms we may at best hope for exponential growth

But the invariance of the “gliding” norms$\mathcal { Z } _ { \tau } ^ { \lambda , \mu }$under free transport (Proposition 4.19) makes it possible to look for uniform estimates such as

$$
\left\| f (\tau , \cdot) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} = O (1) \quad \text { as } \tau \to \infty .\tag{4.37}
$$

Of course, by Proposition 4.27, (4.37) implies that

$$
\left\| \nabla_ {v} f (\tau , \cdot) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda^ {\prime}, \mu^ {\prime}}} = O (\tau) \quad \text { for } \lambda^ {\prime} <   \lambda \text { and } \mu^ {\prime} <   \mu ,\tag{4.38}
$$

and nothing better as far as the asymptotic behavior of$\nabla _ { v } f$is concerned; but (4.37) is much more precise than (4.38). For instance it implies that

$$
\left\| \left(\nabla_ {v} + \tau \nabla_ {x}\right) f (\tau , \cdot) \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda^ {\prime}, \mu^ {\prime}}} = O (1) \quad \text { for } \lambda^ {\prime} <   \lambda \text { and } \mu^ {\prime} <   \mu .
$$

Another way to get rid of filamentation is to average over the spatial variable$x ,$a common sense procedure which has already been used in physics [54, 49]. Think that, if f evolves according to free transport, or even according to the linearized Vlasov equation (3.3), then its space-average

$$
\langle f \rangle (\tau , v) := \int_ {\mathbb {T} ^ {d}} f (\tau , x, v) d x\tag{4.39}
$$

is time-invariant. (We used these infinite number of conservation laws to determine the long-time behavior in Theorem 3.1.)

The bound (4.37) easily implies a bound on the space average: indeed,

$$
\| \langle f \rangle (\tau , \cdot) \| _ {\mathcal {C} ^ {\lambda}} = \| \langle f \rangle (\tau , \cdot) \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} \leqslant \| f (\tau , \cdot) \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} = O (1) \quad \text { as } \tau \to \infty ;\tag{4.40}
$$

and in particular, for$\lambda ^ { \prime } { < } \lambda$

$$
\| \langle \nabla_ {v} f \rangle (\tau , \cdot) \| _ {\mathcal {C} ^ {\lambda^ {\prime}}} = O (1) \quad \text { as } \tau \to \infty .\tag{4.41}
$$

Again, (4.37) contains a lot more information than (4.41).

Remark 4.36. The idea to estimate solutions of a non-linear equation by comparison with some unperturbed (reversible) linear dynamics is already present in the definition of Bourgain spaces$X ^ { s , b } \ [ 1 2 ]$. The analogy stops here, since time is a dummy variable in $X ^ { s , b }$spaces, while in$\mathcal { Z } _ { t } ^ { \lambda , \mu }$spaces it is frozen and appears as a parameter, on which we shall play later.

## 4.12. Linear damping revisited

As a simple illustration of the functional analysis introduced in this section, let us recast the linear damping (Theorem 3.1) in this language. This will be the first step for the study of the non-linear damping. For simplicity we set$L { = } 1$

Theorem 4.37. (Linear Landau damping again) Let$f ^ { 0 } = f ^ { 0 } ( \boldsymbol { v } )$,$W \colon  { \mathbb { T } } ^ { d } \to  { \mathbb { R } }$with $\| \nabla W \| _ { L ^ { 1 } } \leqslant C _ { W }$and$f _ { i } ( x , v )$be such that

(i) condition (L) from 2.2 holds for some constants$C _ { 0 } , \lambda , \varkappa { > } 0 ;$

(ii)$\| f ^ { 0 } \| _ { \mathcal { C } ^ { \lambda ; 1 } } \leqslant C _ { 0 } ;$

(iii)$\| f _ { i } \| _ { \mathcal { Z } ^ { \lambda , \mu ; 1 } } \leqslant \delta$for some$\mu , \delta > 0 ;$

Then for any$\lambda ^ { \prime } { < } \lambda$and$\mu ^ { \prime } { < } \mu .$, the solution of the linearized Vlasov equation (3.3) satisfies

$$
\sup _ {t \in \mathbb {R}} \| f (t, \cdot) \| _ {\mathcal {Z} _ {t} ^ {\lambda^ {\prime}, \mu^ {\prime}; 1}} \leqslant C \delta\tag{4.42}
$$

for some constant$C { = } C ( d , C _ { W } , C _ { 0 } , \lambda , \lambda ^ { \prime } , \mu , \mu ^ { \prime } , \varkappa )$. In particular,$\scriptstyle \varrho = \int _ { \mathbb { R } ^ { d } } f$dv satisfies

$$
\sup _ {t \in \mathbb {R}} \| \varrho (t, \cdot) \| _ {\mathcal {F} ^ {\lambda^ {\prime} | t | + \mu^ {\prime}}} \leqslant C \delta .\tag{4.43}
$$

As a consequence, as$| t | \to \infty ,$ converges strongly to

$$
\varrho_ {\infty} = \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} f _ {i} (x, v) d v d x,
$$

and f converges weakly to$\begin{array} { r } { \langle f _ { i } \rangle { = } \int _ {  { \mathbb { T } } _ { d } } f _ { i } d x , } \end{array}$at rate$O ( e ^ { - \lambda ^ { \prime \prime } | t | } )$for any${ \lambda } ^ { \prime \prime } { < } { \lambda } ^ { \prime }$

If moreover$\| f ^ { 0 } \| _ { C ^ { \lambda ; p } } \leqslant C _ { 0 }$and$\| f _ { i } \| _ { \mathcal { Z } ^ { \lambda , \mu ; p } } \leqslant \delta$for all p in some interval$[ 1 , \bar { p } ]$, then (4.42) can be reinforced into

$$
\sup _ {t \in \mathbb {R}} \| f (t, \cdot) \| _ {\mathcal {Z} _ {t} ^ {\lambda^ {\prime}, \mu^ {\prime}; p}} \leqslant C \delta , \quad 1 \leqslant p \leqslant \bar {p}.\tag{4.44}
$$

Remark 4.38. The notions of weak and strong convergence are the same as those in Theorem 3.1. With respect to that statement, we have added an extra analyticity assumption in the x variable; in this linear context this is an overkill (as the proof will show), but later in the non-linear context this will be important.

Proof. Without loss of generality we restrict our attention to$t \geqslant 0$. Although (4.43) follows from (4.42) by Proposition 4.15, we shall establish (4.43) first, and deduce (4.42) due to the equation. We shall write C for various constants depending only on the parameters in the statement of the theorem.

As in the proof of Theorem 3.1, we have

$$
\hat {\varrho} (t, k) = \tilde {f} _ {i} (k, k t) + \int_ {0} ^ {t} K ^ {0} (t - \tau , k) \hat {\varrho} (\tau , k) d \tau
$$

for any$t \geqslant 0$and$k \in  { \mathbb { Z } ^ { d } } .$. By Lemma 3.6, for any$\lambda ^ { \prime } { < } \lambda$and$\mu ^ { \prime } { < } \mu .$

$$
\begin{array}{l} \sup _ {t \geqslant 0} \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} | \hat {\varrho} (t, k) | e ^ {2 \pi (\lambda^ {\prime} t + \mu^ {\prime}) | k |} \bigg) \\ \quad \leqslant C (\lambda , \lambda^ {\prime}, \varkappa) \bigg (\sum_ {k \in \mathbb {Z} ^ {d}} e ^ {- 2 \pi (\mu - \mu^ {\prime}) | k |} \bigg) \sup _ {t \geqslant 0} \sup _ {k \in \mathbb {Z} ^ {d}} | \tilde {f} _ {i} (k, k t) | e ^ {2 \pi (\lambda^ {\prime} t + \mu) | k |} \\ \quad \leqslant \frac {C (\lambda , \lambda^ {\prime} , \varkappa)}{(\mu - \mu^ {\prime}) ^ {d}} \sup _ {t \geqslant 0} \sum_ {k \in \mathbb {Z} ^ {d}} | \tilde {f} _ {i} (k, k t) | e ^ {2 \pi (\lambda t + \mu) | k |}. \end{array}
$$

Equivalently,

$$
\sup _ {t \geqslant 0} \| \varrho (t, \cdot) \| _ {\mathcal {F} ^ {\lambda^ {\prime} t + \mu^ {\prime}}} \leqslant C \sup _ {t \geqslant 0} \left\| \int_ {\mathbb {R} ^ {d}} f _ {i} \circ S _ {- t} ^ {0} d v \right\| _ {\mathcal {F} ^ {\lambda t + \mu}}.\tag{4.45}
$$

By Propositions 4.15 and 4.19,

$$
\left\| \int_ {\mathbb {R} ^ {d}} f _ {i} \circ S _ {- t} ^ {0} d v \right\| _ {\mathcal {F} ^ {\lambda t + \mu}} \leqslant \| f _ {i} \circ S _ {- t} ^ {0} \| _ {\mathcal {Z} _ {t} ^ {\lambda , \mu ; 1}} = \| f _ {i} \| _ {\mathcal {Z} _ {0} ^ {\lambda , \mu ; 1}} \leqslant \delta .
$$

This and (4.45) imply (4.43).

To deduce (4.42), we first write

$$
f (t, \cdot) = f _ {i} \circ S _ {- t} ^ {0} + \int_ {0} ^ {t} ((\nabla W * \varrho_ {\tau}) \circ S _ {- (t - \tau)} ^ {0}) \cdot \nabla_ {v} f ^ {0} d \tau ,
$$

where$\varrho _ { \tau } { = } \varrho ( \tau , \cdot )$. Then for any$\lambda ^ { \prime \prime } { < } \lambda ^ { \prime }$we have, by Propositions 4.24 and 4.15, for all $t \geqslant 0$

$$
\begin{array}{l} \| f \| _ {\mathcal {Z} _ {t} ^ {\lambda^ {\prime \prime}, \mu^ {\prime}; 1}} \leqslant \| f _ {i} \circ S _ {- t} ^ {0} \| _ {\mathcal {Z} _ {t} ^ {\lambda^ {\prime \prime}, \mu ; 1}} + \int_ {0} ^ {t} \| (\nabla W * \varrho_ {\tau}) \circ S _ {- (t - \tau)} ^ {0} \| _ {\mathcal {Z} _ {t} ^ {\lambda^ {\prime \prime}, \mu^ {\prime}; \infty}} \| \nabla_ {v} f ^ {0} \| _ {\mathcal {Z} _ {t} ^ {\lambda^ {\prime \prime}, \mu ; 1}} d \tau \\ = \| f _ {i} \| _ {\mathcal {Z} ^ {\lambda^ {\prime \prime}, \mu ; 1}} + \| \nabla_ {v} f ^ {0} \| _ {\mathcal {C} ^ {\lambda^ {\prime \prime}; 1}} \int_ {0} ^ {t} \| \nabla W * \varrho_ {\tau} \| _ {\mathcal {F} ^ {\lambda^ {\prime \prime} \tau + \mu^ {\prime}}} d \tau . \end{array} \tag {4}\tag{4.46}
$$

Since$\widehat { \nabla W } ( 0 ) = 0$, we have, for any$\tau { \geqslant } 0$

$$
\begin{array}{r l} & {\| \nabla W * \varrho_ {\tau} \| _ {\mathcal {F} ^ {\lambda^ {\prime \prime} \tau + \mu}} \leqslant e ^ {- 2 \pi (\lambda^ {\prime \prime} - \lambda^ {\prime}) \tau} \| \nabla W * \varrho_ {\tau} \| _ {\mathcal {F} ^ {\lambda^ {\prime} \tau + \mu^ {\prime}}}} \\ & {\quad \leqslant \| \nabla W \| _ {L ^ {1}} e ^ {- 2 \pi (\lambda^ {\prime \prime} - \lambda^ {\prime}) \tau} \| \varrho_ {\tau} \| _ {\mathcal {F} ^ {\lambda^ {\prime} \tau + \mu^ {\prime}}}} \\ & {\quad \leqslant C _ {W} C \delta e ^ {- 2 \pi (\lambda^ {\prime \prime} - \lambda^ {\prime}) \tau};} \end{array}
$$

in particular

$$
\int_ {0} ^ {t} \left\| \nabla W * \varrho_ {\tau} \right\| _ {\mathcal {F} ^ {\lambda^ {\prime \prime} + \mu^ {\prime}}} d \tau \leqslant \frac {C \delta}{\lambda^ {\prime \prime} - \lambda^ {\prime}}.\tag{4.47}
$$

Also, by Proposition 4.10, for$1 < \lambda ^ { \prime } / \lambda ^ { \prime \prime } { \leqslant } 2$we have

$$
\| \nabla_ {v} f ^ {0} \| _ {\mathcal {C} ^ {\lambda^ {\prime \prime}; 1}} \leqslant \frac {C}{\lambda - \lambda^ {\prime \prime}} \| f ^ {0} \| _ {\mathcal {C} ^ {\lambda ; 1}} \leqslant \frac {C C _ {0}}{\lambda - \lambda^ {\prime \prime}}.\tag{4.48}
$$

Plugging (4.47) and (4.48) into (4.46), we deduce (4.42). The end of the proof is an easy exercise if one recalls that$\langle f ( t , \cdot ) \rangle = \langle f _ { i } \rangle$for all t.□

## 5. Deflection estimates

Let a small time-dependent force field, denoted by$\varepsilon F ( t , x )$, be given on$\mathbb { T } ^ { d } \times \mathbb { R } ^ { d }$, whose analytic regularity improves linearly in time. (Think of$\varepsilon F$as the force created by a damped density.) This force field perturbs the trajectories$S _ { \tau , t } ^ { 0 }$of the free transport (τ is the initial time and t the current time) into trajectories$S _ { \tau , t }$. The goal of this section is to get an estimate on the maps$\Omega _ { t , \tau } { = } S _ { t , \tau ^ { \circ } } S _ { \tau , t } ^ { 0 }$(so that$S _ { t , \tau } { = } \Omega _ { t , \tau ^ { \circ } } S _ { t , \tau } ^ { 0 } )$. These bounds should be in an analytic class about as good as$F$, with a loss of analyticity depending on ε; they should also be, for$0 \leqslant \tau \leqslant t$

uniform in$t \geqslant \tau$,

small as$\tau {  } \infty$

small as$\tau  t$

We shall call$\Omega _ { t , \cdot }$the deflection map (from time τ to time t). The idea is to compare the free (= without interaction) evolution to the true evolution is at the basis of the interaction representation, wave operators, and most famously the scattering transforms (in which the whole evolution from$t \to - \infty$to$t \to \infty$is replaced by well-chosen asymptotics). For all these methods which are of constant use in classical and quantum physics one can consult [21].

Remark 5.1. The order of composition in$\Omega _ { t , \tau } { = } S _ { t , \tau ^ { \mathrm { o } } } S _ { \tau , t } ^ { 0 }$is the only one which leads to useful asymptotics: it is easy to check that in general$S _ { \tau , t } ^ { 0 } { \circ } S _ { t , }$does not converge to anything as t , even if the force is compactly supported in time.

## 5.1. Formal expansion

Before stating the main result, we sketch a heuristic perturbation study. Let us write a formal expansion of$V _ { 0 , t } ( x , \boldsymbol { v } )$as a perturbation series:

$$
V _ {0, t} (x, v) = v + \varepsilon v ^ {(1)} (t, x, v) + \varepsilon^ {2} v ^ {(2)} (t, x, v) + \dots .
$$

Then we deduce that

$$
X _ {0, t} (x, v) = x + v t + \varepsilon \int_ {0} ^ {t} v ^ {(1)} (s, x, v) d s + \varepsilon^ {2} \int_ {0} ^ {t} v ^ {(2)} (s, x, v) d s + \dots ,
$$

with$\scriptstyle v ^ { ( i ) } ( t = 0 ) = 0$

So

$$
\frac {\partial^ {2} X _ {0 , t}}{\partial t ^ {2}} = \varepsilon \frac {\partial v ^ {(1)}}{\partial t} + \varepsilon^ {2} \frac {\partial v ^ {(2)}}{\partial t} + \dots .
$$

On the other hand,

$$
\begin{array}{l} \varepsilon F (t, X _ {0, t}) = \varepsilon \sum_ {k \in \mathbb {Z} ^ {d}} \widehat {F} (t, k) e ^ {2 i \pi k \cdot x} e ^ {2 i \pi k \cdot v t} e ^ {2 i \pi k \cdot (\varepsilon \int_ {0} ^ {t} v ^ {(1)} d s + \varepsilon^ {2} \int_ {0} ^ {t} v ^ {(2)} d s + \ldots)} \\ = \varepsilon \sum_ {k \in \mathbb {Z} ^ {d}} \widehat {F} (t, k) e ^ {2 i \pi k \cdot x} e ^ {2 i \pi k \cdot v t} \\ \qquad \times \bigg (1 + 2 i \pi \varepsilon k \cdot \int_ {0} ^ {t} v ^ {(1)} d s + 2 i \pi \varepsilon^ {2} k \cdot \int_ {0} ^ {t} v ^ {(2)} d s - (2 \pi) ^ {2} \varepsilon^ {2} \bigg (k \cdot \int_ {0} ^ {t} v ^ {(1)} d s \bigg) ^ {2} + \ldots \bigg). \end{array}
$$

By successive identification,

$$
\begin{array}{r l} & {\frac {\partial v ^ {(1)}}{\partial t} = \sum_ {k \in \mathbb {Z} ^ {d}} \widehat {F} (t, k) e ^ {2 i \pi k \cdot x} e ^ {2 i \pi k \cdot v t},} \\ & {\frac {\partial v ^ {(2)}}{\partial t} = \sum_ {k \in \mathbb {Z} ^ {d}} \widehat {F} (t, k) e ^ {2 i \pi k \cdot x} e ^ {2 i \pi k \cdot v t} 2 i \pi k \cdot \int_ {0} ^ {t} v ^ {(1)} d s,} \\ & {\frac {\partial v ^ {(3)}}{\partial t} = \sum_ {k \in \mathbb {Z} ^ {d}} \widehat {F} (t, k) e ^ {2 i \pi k \cdot x} e ^ {2 i \pi k \cdot v t} \bigg (2 i \pi k \cdot \int_ {0} ^ {t} v ^ {(2)} d s - (2 \pi) ^ {2} \varepsilon^ {2} \bigg (k \cdot \int_ {0} ^ {t} v ^ {(1)} d s \bigg) ^ {2} \bigg),} \end{array}
$$

etc.

In particular notice that

$$
\left| \frac {\partial v ^ {(1)}}{\partial t} \right| \leqslant \sum_ {k \in \mathbb {Z} ^ {d}} | \widehat {F} (t, k) |,
$$

so

$$
\begin{array}{l} \int_ {0} ^ {\infty} \left| \frac {\partial v ^ {(1)}}{\partial t} \right| d t \leqslant \int_ {0} ^ {\infty} \sum_ {k \in \mathbb {Z} ^ {d}} | \widehat {F} (t, k) |   d t \\ \leqslant \int_ {0} ^ {\infty} \sum_ {k \in \mathbb {Z} ^ {d}} | \widehat {F} (t, k) | e ^ {2 \pi \mu t} e ^ {- 2 \pi \mu t}   d t \leqslant C _ {F} \int_ {0} ^ {\infty} e ^ {- 2 \pi \mu t}   d t = \frac {C _ {F}}{2 \pi \mu}. \end{array}
$$

Thus, under our uniform analyticity assumptions we expect$V _ { 0 , t } ( x , \boldsymbol { v } )$to be a uniformly bounded analytic perturbation of v.

## 5.2. Main result

On$\mathbb { T } _ { x } ^ { d }$we consider the dynamical system

$$
\frac {d ^ {2} X}{d t ^ {2}} = \varepsilon F (t, X);
$$

its phase space is$\mathbb { T } ^ { d } \times \mathbb { R } ^ { d }$. Although this system is reversible, we shall only consider$t \geqslant 0$ The parameter ε is here only to recall the perturbative nature of the estimate.

For any$( x , v ) \in \mathbb { T } ^ { d } \times \mathbb { R } ^ { d }$and any two times$\tau , t \in \mathbb { R } _ { + }$, let$S _ { \tau , t }$be the transform mapping the state of the system at time$\tau$to the state of the system at time t. In more precise terms,$S _ { \tau , t }$is described by the equations

$$
S _ {\tau , t} (x, v) = (X _ {\tau , t} (x, v), V _ {\tau , t} (x, v)), \quad X _ {\tau , \tau} (x, v) = x, \quad V _ {\tau , \tau} (x, v) = v,
$$

$$
\frac {d}{d t} X _ {\tau , t} (x, v) = V _ {\tau , t} (x, v) \quad \mathrm{and} \quad \frac {d}{d t} V _ {\tau , t} (x, v) = \varepsilon F (t, X _ {\tau , t} (x, v)).\tag{5.1}
$$

From the definition we have the composition identity

$$
S _ {t _ {2}, t _ {3}} \circ S _ {t _ {1}, t _ {2}} = S _ {t _ {1}, t _ {3}};\tag{5.2}
$$

in particular$S _ { t , \tau }$is the inverse of$S _ { \tau , t }$

We also write$S _ { \tau , t } ^ { 0 }$for the same transform in the case of the free dynamics$( \varepsilon { = } 0 )$; in this case there is an explicit expression:

$$
S _ {\tau , t} ^ {0} (x, v) = (x + v (t - \tau), v),\tag{5.3}
$$

where$x + v ( t - \tau )$) is evaluated modulo$\mathbb { Z } ^ { d }$. Finally, we define the deflection map associated with$\varepsilon F { \mathrm { : } }$

$$
\Omega_ {t, \tau} = S _ {t, \tau} \circ S _ {\tau , t} ^ {0}.\tag{5.4}
$$

(There is no simple semigroup property for the transforms$\Omega _ { t , \tau } . )$

In this section we establish the following estimates.

Theorem 5.2. (Analytic estimates on deflection in hybrid norms) Let$\varepsilon > 0$and let $F { = } F ( t , x )$on$\mathbb { R } _ { + } \times \mathbb { T } ^ { d }$satisfy

$$
\widehat {F} (t, 0) = 0 \quad a n d \sup _ {t \geqslant 0} (\| F (t, \cdot) \| _ {\mathcal {F} ^ {\lambda t + \mu}} + \| \nabla_ {x} F (t, \cdot) \| _ {\mathcal {F} ^ {\lambda t + \mu}}) \leqslant C _ {F}\tag{5.5}
$$

for some parameters$\lambda , \mu > 0$and$C _ { F } > 0$. Let$t \geqslant \tau \geqslant 0$and let

$$
\Omega_ {t, \tau} = (\Omega X _ {t, \tau}, \Omega V _ {t, \tau})
$$

be the deflection associated with$\varepsilon F .$. Let$0 \leqslant \lambda ^ { \prime } < \lambda , 0 \leqslant \mu ^ { \prime } < \mu$and$\tau ^ { \prime } \geqslant 0$be such that

$$
\lambda^ {\prime} (\tau^ {\prime} - \tau) \leqslant \frac {1}{2} (\mu - \mu^ {\prime}).\tag{5.6}
$$

Let

$$
\left\{ \begin{array}{l} R _ {1} (\tau , t) = C _ {F} e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) \tau} \min \{t - \tau , (2 \pi (\lambda - \lambda^ {\prime})) ^ {- 1} \}, \\ R _ {2} (\tau , t) = C _ {F} e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) \tau} \min \{\frac {1}{2} (t - \tau) ^ {2}, (2 \pi (\lambda - \lambda^ {\prime})) ^ {- 2} \}. \end{array} \right.
$$

Assume that

$$
\varepsilon R _ {2} (\tau , t) \leqslant \frac {1}{4} \left(\mu - \mu^ {\prime}\right) \quad f o r a l l 0 \leqslant \tau \leqslant t,\tag{5.7}
$$

and

$$
\varepsilon C _ {F} \leqslant 2 \pi^ {2} (\lambda - \lambda^ {\prime}) ^ {2}.\tag{5.8}
$$

Then

$$
\left\| \Omega X _ {t, \tau} - \mathrm{Id} \right\| _ {\mathcal {Z} _ {\tau^ {\prime}} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant 2 \varepsilon R _ {2} (\tau , t) \quad f o r a l l 0 \leqslant \tau \leqslant t,\tag{5.9}
$$

and

$$
\left\| \Omega V _ {t, \tau} - \operatorname{Id} \right\| _ {\mathcal {Z} _ {\tau^ {\prime}} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant \varepsilon R _ {1} (\tau , t) \quad f o r a l l 0 \leqslant \tau \leqslant t.\tag{5.10}
$$

Remark 5.3. The proof of Theorem 5.2 is easily adapted to include Sobolev corrections. It is important to note that the deflection map is smooth uniformly in time, not just in gliding regularity$( \tau ^ { \prime } { = } 0$is admissible in (5.6)).

Proof. For a start, let us make the ansatz

$$
S _ {t, \tau} (x, v) = (x - v (t - \tau) + \varepsilon Z _ {t, \tau} (x, v), v + \varepsilon \partial_ {\tau} Z _ {t, \tau} (x, v)),
$$

with

$$
Z _ {t, t} (x, v) = 0 \quad \text { and } \quad \partial_ {\tau} Z _ {t, \tau} | _ {\tau = t} (x, v) = 0.
$$

Then it is easily checked that

$$
\Omega_ {t, \tau} - \mathrm{Id} = \varepsilon (Z, \partial_ {\tau} Z) \circ S _ {t - \tau} ^ {0};
$$

in particular

$$
\left\| \Omega_ {t, \tau} - \mathrm{Id} \right\| _ {\mathcal {Z} _ {\tau^ {\prime}} ^ {\lambda^ {\prime}, \mu^ {\prime}}} = \varepsilon \left\| (Z, \partial_ {\tau} Z) \right\| _ {\mathcal {Z} _ {t + \tau^ {\prime} - \tau} ^ {\lambda^ {\prime}, \mu^ {\prime}}}.
$$

To estimate this we shall use a fixed-point argument based on the equation for$S _ { t , \tau }$ namely

$$
\frac {d ^ {2} X _ {t , \tau}}{d \tau^ {2}} = \varepsilon F (\tau , X _ {t, \tau}),
$$

or equivalently

$$
\frac {d ^ {2} Z _ {t , \tau}}{d \tau^ {2}} = F (\tau , x - v (t - \tau) + \varepsilon Z _ {t, \tau}).
$$

So let us fix t and define

$$
\Psi \colon (W _ {t, \tau}) _ {0 \leqslant \tau \leqslant t} \longmapsto (Z _ {t, \tau}) _ {0 \leqslant \tau \leqslant t}
$$

such that$( Z _ { t , \tau } ) _ { 0 \leqslant \tau \leqslant t }$is the solution of

$$
\left\{ \begin{array}{l} \frac {\partial^ {2} Z _ {t , \tau}}{\partial \tau^ {2}} = F (\tau , x - v (t - \tau) + \varepsilon W _ {t, \tau}), \\ Z _ {t, t} = 0, \\ (\partial_ {\tau} Z _ {t, \tau}) | _ {\tau = t} = 0. \end{array} \right.\tag{5.11}
$$

What we are after is an estimate of the fixed point of Ψ. We do this in two steps.

Step 1. Estimate of$\Psi ( 0 )$. Let$Z ^ { 0 } = \Psi ( 0 )$. By integration of (5.11) (for$W { = } 0 )$we have

$$
Z _ {t, \tau} ^ {0} = \int_ {\tau} ^ {t} (s - \tau) F (s, x - v (t - s)) d s.
$$

Let σ be such that λ-σ$\leqslant \frac { 1 } { 2 } \left( \mu - \mu ^ { \prime } \right)$. Applying the$\mathcal { Z } _ { t + \sigma } ^ { \lambda ^ { \prime } , \mu ^ { \prime } }$norm and using Proposition 4.19, we get

$$
\| Z _ {t, \tau} ^ {0} \| _ {\mathcal {Z} _ {t + \sigma} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant \int_ {\tau} ^ {t} (s - \tau) \| F (s, \cdot) \| _ {\mathcal {Z} _ {s + \sigma} ^ {\lambda^ {\prime}, \mu^ {\prime}}} d s = \int_ {\tau} ^ {t} (s - \tau) \| F (s, \cdot) \| _ {\mathcal {F} ^ {\lambda^ {\prime} s + \lambda^ {\prime} \sigma + \mu^ {\prime}}} d s.
$$

Of course$\lambda ^ { \prime } \sigma + \mu ^ { \prime } \leqslant \mu$, so in particular

$$
\lambda^ {\prime} s + \lambda^ {\prime} \sigma + \mu^ {\prime} \leqslant - (\lambda - \lambda^ {\prime}) s + \lambda s + \mu .
$$

Combining this with the assumption$\widehat { F } ( s , 0 ) = 0$yields

$$
\| F (s, \cdot) \| _ {\mathcal {F} ^ {\lambda^ {\prime} s + \lambda^ {\prime} \sigma + \mu^ {\prime}}} \leqslant \| F (s, \cdot) \| _ {\mathcal {F} ^ {\lambda s + \mu}} e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) s} \leqslant C _ {F} e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) s}.
$$

So

$$
\begin{array}{r l} & {\| Z _ {t, \tau} ^ {0} \| _ {\mathcal {Z} _ {t + \sigma} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant C _ {F} \int_ {\tau} ^ {t} (s - \tau) e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) s} d s} \\ & {\quad \leqslant C _ {F} e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) \tau} \min \biggl \{\frac {(t - \tau) ^ {2}}{2}, \frac {1}{(2 \pi (\lambda - \lambda^ {\prime})) ^ {2}} \biggr \} \leqslant R _ {2} (\tau , t).} \end{array}
$$

With t still fixed, we define the norm

$$
\left\| \left(Z _ {t, \tau}\right) _ {0 \leqslant \tau \leqslant t} \right\| := \sup \left\{\frac {\left\| Z _ {t , \tau} \right\| _ {\mathcal {Z} _ {t + \sigma} ^ {\lambda^ {\prime} , \mu^ {\prime}}}}{R _ {2} (\tau , t)}: 0 \leqslant \tau \leqslant t, \sigma + t \geqslant 0 \text {and} \lambda^ {\prime} \sigma \leqslant \frac {\mu - \mu^ {\prime}}{2} \right\}.\tag{5.12}
$$

The above estimates show that$\| \Psi ( 0 ) \| \leqslant 1$. (Since$t + ( \tau ^ { \prime } - \tau ) \geq t - \tau \geq 0$, we may assume that$t + \sigma \geqslant 0$, and we aim at finally choosing$\sigma { = } \tau ^ { \prime } { - } \tau . )$

Step 2. Lipschitz constant of Ψ. We shall prove that under our assumptions, Ψ is <sup>1</sup> -Lipschitz on the ball$B ( 0 , 2 )$in the norm$\| \cdot \|$. Let$W , \widetilde { W } { \in } B ( 0 , 2 ) , ~ Z { = } \Psi ( W )$and ${ \widetilde { Z } } { = } \Psi ( { \widetilde { W } } )$. By solving the diferential inequality for$Z - { \widetilde { Z } } .$#, we get

$$
Z _ {t, \tau} - \widetilde {Z} _ {t, \tau} = \varepsilon (W _ {t, s} - \widetilde {W} _ {t, s}) \cdot \int_ {0} ^ {1} \int_ {\tau} ^ {t} (s - \tau) \nabla_ {x} F (s, x - v (t - s) + \varepsilon (\theta W _ {t, s} + (1 - \theta) \widetilde {W} _ {t, s})) d s d \theta .
$$

We divide by$R _ { 2 } ( \tau , t )$, take the$\mathcal { Z }$norm and note that$R _ { 2 } ( s , t ) { \leqslant } R _ { 2 } ( \tau , t )$to obtain

$$
\left\| \left(Z _ {t, \tau} - \widetilde {Z} _ {t, \tau}\right) _ {0 \leqslant \tau \leqslant t} \right\| \leqslant \varepsilon \left\| \left(W _ {t, s} - \widetilde {W} _ {t, s}\right) _ {0 \leqslant s \leqslant t} \right\| A (t)
$$

with

$$
A (t) = \sup _ {\sigma , \tau} \int_ {0} ^ {1} \int_ {\tau} ^ {t} (s - \tau) \| \nabla_ {x} F (s, x - v (t - s) + \varepsilon (\theta W _ {t, s} + (1 - \theta) \widetilde {W} _ {t, s})) \| _ {\mathcal {Z} _ {t + \sigma} ^ {\lambda^ {\prime}, \mu^ {\prime}}} d s d \theta .
$$

By Proposition 4.25 (composition inequality),

$$
A (t) \leqslant \int_ {\tau} ^ {t} (s - \tau) \| \nabla_ {x} F (s, \cdot) \| _ {\mathcal {Z} _ {s + \sigma} ^ {\lambda^ {\prime}, \mu^ {\prime} + e (t, s, \sigma)}} d s = \int_ {\tau} ^ {t} (s - \tau) \| \nabla_ {x} F (s, \cdot) \| _ {\mathcal {F} ^ {\lambda^ {\prime} s + \lambda^ {\prime} \sigma + \mu^ {\prime} + e (t, s, \sigma)}} d s,
$$

with

$$
e (t, s, \sigma) := \varepsilon \| \theta W _ {t, s} + (1 - \theta) \widetilde {W} _ {t, s} \| _ {\mathcal {Z} _ {t + \sigma} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant 2 \varepsilon R _ {2} (s, t) \leqslant 2 \varepsilon R _ {2} (\tau , t).
$$

Using (5.7), we get

$$
\lambda^ {\prime} s + \lambda^ {\prime} \sigma + \mu^ {\prime} + e (s, t, \sigma) \leqslant \lambda^ {\prime} s + \lambda^ {\prime} \sigma + \mu^ {\prime} + 2 \varepsilon R _ {2} (\tau , t) \leqslant \lambda^ {\prime} s + \mu = (\lambda s + \mu) - (\lambda - \lambda^ {\prime}) s.
$$

By again using the bound on$\nabla _ { x } F$and the assumption$\widehat { F } ( s , 0 ) = 0$, we deduce that

$$
A (t) \leqslant \sup _ {\tau} \int_ {\tau} ^ {t} (s - \tau) C _ {F} e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) s} d s \leqslant R _ {2} (0, t) \leqslant \frac {C _ {F}}{4 \pi^ {2} (\lambda - \lambda^ {\prime}) ^ {2}}.
$$

Using (5.8), we conclude that

$$
\left\| \left(Z _ {t, \tau} - \widetilde {Z} _ {t, \tau}\right) _ {0 \leqslant \tau \leqslant t} \right\| \leqslant \frac {1}{2} \left\| \left(W _ {t, s} - \widetilde {W} _ {t, s}\right) _ {0 \leqslant s \leqslant t} \right\|.
$$

So$\Psi$is$\frac { 1 } { 2 } \mathrm { - I }$ipschitz on$B ( 0 , 2 )$, and we can conclude the proof of (5.9) by applying Theorem$\mathrm { A . 2 }$and choosing$\sigma { = } \tau ^ { \prime } { - } \tau$

It remains to control the velocity component of Ω, i.e., establish (5.10); this will follow from the control of the position component. Indeed, if we write

$$
Q _ {t, \tau} = \varepsilon^ {- 1} (\Omega V _ {t, \tau} - \mathrm{Id}) (x, v),
$$

we have

$$
Q _ {t, \tau} = \int_ {\tau} ^ {t} F (s, x - v (t - s) + \varepsilon W _ {t, s}) d s,
$$

so we can estimate as before

$$
\| Q _ {t, \tau} \| _ {\mathcal {Z} _ {t + (\tau^ {\prime} - \tau)} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant \int_ {\tau} ^ {t} \| F (s, \cdot) \| _ {\mathcal {F} ^ {\lambda^ {\prime} s + \lambda^ {\prime} (\tau^ {\prime} - \tau) + \mu^ {\prime} + e (t, s, \tau^ {\prime} - \tau)}} d s
$$

to get

$$
\left\| Q _ {t, \tau} \right\| _ {\mathcal {Z} _ {t + (\tau^ {\prime} - \tau)} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant \int_ {\tau} ^ {t} C _ {F} e ^ {- 2 \pi (\lambda - \lambda^ {\prime}) s} d s \leqslant R _ {1} (\tau , t).
$$

Thus the proof is complete.

Remark 5.4. Instead of directly studying$S _ { t , \tau ^ { \circ } } S _ { \tau , t } ^ { 0 }$, one can study$S _ { t , \tau } ^ { 0 } { ^ { \circ } S } _ { \tau , t }$and then invert with the help of Proposition 4.28 (inversion inequality); in the end the results are similar.

Remark 5.5. Loss and Bernard independently suggested to compare the estimates in the present section with the Nekhoroshev theorem in dynamical systems theory [71], [72]. The latter theorem roughly states that for a perturbation of a completely integrable system, trajectories remain close to those of the unperturbed system for a time growing exponentially in the inverse of the size of the perturbation (unlike KAM theory, this result is not global in time; but it is more general in the sense that it also applies outside invariant tori). In the present setting the situation is better since the perturbation decays.

## 6. Bilinear regularity and decay estimates

To introduce this crucial section, let us reproduce and improve a key computation from$\ S 3 .$ Let$G$be a function of$v ,$and$R$a time-dependent function of$x$with$\widehat { R } ( 0 ) = 0 ;$; both$G$ and R are vector-valued in$\mathbb { R } ^ { d }$. (Think of$G ( v )$as$\nabla _ { v } f ( v )$and of$R ( \tau , x )$as$\nabla W * \varrho ( \tau , x ) . )$ From now on we shall always use the supremum norm over the coordinates in the following sense

$$
\| F \| _ {\mathcal {Z}} := \max _ {1 \leqslant j \leqslant d} \| F _ {j} \| _ {\mathcal {Z}} \quad \text { and } \quad \| F \| _ {\mathcal {F}} := \max _ {1 \leqslant j \leqslant d} \| F _ {j} \| _ {\mathcal {F}}.
$$

Let further

$$
\sigma (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} G (v) \cdot R (\tau , x - v (t - \tau)) d v d \tau .
$$

Then

$$
\begin{array}{l} \hat {\sigma} (t, k) = \int_ {0} ^ {t} \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} G (v) \cdot R (\tau , x - v (t - \tau)) e ^ {- 2 i \pi k \cdot x} d v d x d \tau \\ \qquad = \int_ {0} ^ {t} \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} G (v) \cdot R (\tau , x) e ^ {- 2 i \pi k \cdot x} e ^ {- 2 i \pi k \cdot v (t - \tau)} d v d x d \tau \\ \qquad = \int_ {0} ^ {t} \widetilde {G} (k (t - \tau)) \cdot \widehat {R} (\tau , k) d \tau . \end{array}
$$

Let us assume that G has a$\mathrm { \ddot { \hbar } h i g h } ^ { \mathrm { \ ' } }$gliding analytic regularity$\bar { \lambda } ,$, and estimate$\sigma$in regularity$\lambda t ,$, with$\lambda { < } \bar { \lambda }$. Let$\scriptstyle \alpha = \alpha ( t , \tau )$satisfy

$$
0 \leqslant \alpha (t, \tau) \leqslant (\bar {\lambda} - \lambda) (t - \tau).
$$

Then, with$\mathbb { Z } _ { * } ^ { d } { = } \mathbb { Z } ^ { d } \backslash \{ 0 \}$,

$$
\begin{array}{l} \| \sigma (t) \| _ {\mathcal {F} ^ {\lambda t}} \leqslant d \sum_ {k \in Z _ {*} ^ {d}} \int_ {0} ^ {t} e ^ {2 \pi \lambda t | k |} | \widetilde {G} (k (t - \tau)) |   | \widehat {R} (\tau , k) |   d \tau \\ \quad \leqslant d \int_ {0} ^ {t} \Big (\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | \widetilde {G} (k (t - \tau)) | e ^ {2 \pi (\lambda (t - \tau) + \alpha) | k |} \Big) \Bigg (\sum_ {k \in \mathbb {Z} ^ {d}} e ^ {2 \pi (\lambda \tau - \alpha) | k |} | \widehat {R} (\tau , k) | \Bigg)   d \tau \\ \quad \leqslant d \Big (\sup _ {\eta \in \mathbb {Z} ^ {d}} e ^ {2 \pi \bar {\lambda} | \eta |} | \widetilde {G} (\eta) | \Big) \Big (\sup _ {0 \leqslant \tau \leqslant t} \| R (\tau , \cdot) \| _ {\mathcal {F} ^ {\lambda \tau - \alpha}} \Big) \int_ {0} ^ {t} e ^ {- 2 \pi ((\bar {\lambda} - \lambda) (t - \tau) - \alpha)}   d \tau , \end{array}
$$

where we have used that

$$
k \in \mathbb {Z} _ {*} ^ {d} \quad \Longrightarrow \quad 2 \pi (\lambda (t - \tau) + \alpha) | k | \leqslant 2 \pi \bar {\lambda} | k | (t - \tau) - ((\bar {\lambda} - \lambda) (t - \tau) - \alpha).
$$

Let us choose

$$
\alpha (t, \tau) = \frac {1}{2} (\bar {\lambda} - \lambda) \min \{1, t - \tau \}.
$$

Then

$$
\int_ {0} ^ {t} e ^ {- 2 \pi ((\bar {\lambda} - \lambda) (t - \tau) - \alpha)} d \tau \leqslant \int_ {0} ^ {t} e ^ {- \pi (\bar {\lambda} - \lambda) (t - \tau)} d \tau \leqslant \frac {1}{\pi (\bar {\lambda} - \lambda)}.
$$

So in the end

$$
\| \sigma (t) \| _ {\mathcal {F} ^ {\lambda t}} \leqslant \frac {d \| G \| _ {\mathcal {X} ^ {\bar {\lambda}}}}{\pi (\bar {\lambda} - \lambda)} \sup _ {0 \leqslant \tau \leqslant t} \| R (\tau) \| _ {\mathcal {F} ^ {\lambda \tau - \alpha (t, \tau)}},
$$

where$\begin{array} { r } { \| G \| _ { \mathcal { X } ^ { \bar { \lambda } } } = \operatorname* { s u p } _ { \eta \in \mathbb { Z } ^ { d } } | \widetilde { G } ( \eta ) | e ^ { 2 \pi \bar { \lambda } | \eta | } . } \end{array}$

!In the preceding computation there are three important things to notice, which lie at the heart of Landau damping:

The natural index of analytic regularity of$\sigma$in x increases linearly in time: this is an automatic consequence of the gliding regularity, already observed in 4.

A bit$\alpha ( t , \tau )$of analytic regularity of$G$was transferred from$G$to$R ,$however no more than a fraction of$( \bar { \lambda } - \lambda ) ( t - \tau )$. We call this the regularity extortion: if$f$forces ${ \bar { f } } ,$i.e. if it satisfies an equation of the form$\partial _ { t } f + v \cdot \nabla _ { x } f + F [ f ] \cdot \nabla _ { v } \bar { f } = S$, then$\bar { f }$will give away some (gliding) smoothness to$\begin{array} { r } { \varrho = \int _ { \mathbb { R } ^ { d } } f d v } \end{array}$

The combination of higher regularity of$G$and the assumption$\widehat { R } ( 0 )$=0 has been converted into a time-decay, so that the time-integral is bounded, uniformly as$t \to \infty$ Thus there is decay by regularity.

The main goal of this section is to establish quantitative variants of these efects in some general situations when G is not only a function of v and R not only a function of t and x. Note that we shall have to work with regularity indices depending on t and τ!

Regularity extortion is related to velocity-averaging regularity, well known in kinetic theory [43]; what is unusual though is that we are working in analytic regularity, and in large time, while velocity-averaging regularity is mainly a short-time efect. In fact we shall study two distinct mechanisms for the extortion: the first one will be well suited for short times (t τ small), and will be crucial later to get rid of small deteriorations in the functional spaces due to composition; the second one will be well adapted to large times$\left( t - \tau \to \infty \right)$and will ensure convergence of the time-integrals.

The estimates in this section lead to a serious twist on the popular view on Landau damping, according to which the wave gives energy to the particles that it forces; instead, the picture here is that the wave gains regularity from the background, and regularity is converted into decay.

For the sake of pedagogy, we shall first establish the basic, simple bilinear estimate, and then discuss the two mechanisms once at a time.

## 6.1. Basic bilinear estimate

Proposition 6.1. (Basic bilinear estimate in gliding regularity) Let${ \cal G } { = } G ( \tau , x , v )$ and$R { = } R ( \tau , x , v )$be valued$i n \mathbb { R } ^ { d }$,

$$
\begin{array}{l} \beta (\tau , x) = \int_ {\mathbb {R} ^ {d}} (G \cdot R) (\tau , x - v (t - \tau), v) d v, \\ \sigma (t, x) = \int_ {0} ^ {t} \beta (\tau , x) d \tau . \end{array}
$$

Then

$$
\left\| \beta (\tau , \cdot) \right\| _ {\mathcal {F} ^ {\lambda t + \mu}} \leqslant d \| G \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}} \| R \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}};\tag{6.1}
$$

and

$$
\left\| \sigma (t, \cdot) \right\| _ {\mathcal {F} ^ {\lambda t + \mu}} \leqslant d \int_ {0} ^ {t} \left\| G \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}} \left\| R \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}} d \tau .\tag{6.2}
$$

Proof. Obviously (6.2) follows from (6.1). To prove (6.1) we apply successively Propositions 4.15, 4.19 and 4.24, obtaining

$$
\begin{array}{l} \| \beta (\tau , \cdot) \| _ {\mathcal {F} ^ {\lambda t + \mu}} \leqslant \left\| \int_ {\mathbb {R} ^ {d}} (G \cdot R) \circ S _ {\tau - t} ^ {0} d v \right\| _ {\mathcal {F} ^ {\lambda t + \mu}} \leqslant \| (G \cdot R) \circ S _ {\tau - t} ^ {0} \| _ {\mathcal {Z} _ {t} ^ {\lambda , \mu ; 1}} \\ = \| G \cdot R \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}} \leqslant d \| G \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}} \| R \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu}}. \end{array}
$$

## 6.2. Short-term regularity extortion by time cheating

Proposition 6.2. (Short-term regularity extortion) Let$G = G ( x , v )$and$R = R ( x , v )$ be valued in$\mathbb { R } ^ { d }$, and

$$
\beta (x) = \int_ {\mathbb {R} ^ {d}} (G \cdot R) (x - v (t - \tau), v) d v.
$$

Then for any$\lambda , \mu , t { \geqslant } 0$and any$b > - 1$, we have

$$
\left\| \beta \right\| _ {\mathcal {F} ^ {\lambda t + \mu}} \leqslant d \| G \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu ; 1}} \| R \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu}}.\tag{6.3}
$$

Moreover, if$P _ { k }$stands for the projection on the k-th Fourier mode as in (4.36), one has

$$
e ^ {2 \pi (\lambda t + \mu) | k |} | \hat {\beta} (k) | \leqslant d \sum_ {l \in \mathbb {Z} ^ {d}} \| P _ {l} G \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu ; 1}} \| P _ {k - l} R \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu}}.\tag{6.4}
$$

Remark 6.3. If R only depends on t and$x ,$then the norm of R in the right-hand side of (6.3) is$\| R \| _ { \mathcal { F } ^ { \nu } }$with

$$
\nu = \lambda (1 + b) \left| \tau - \frac {b t}{1 + b} \right| + \mu = (\lambda \tau + \mu) - b (t - \tau),
$$

as soon as$\tau \geqslant b t / ( 1 + b )$. Thus, some regularity has been gained with respect to Proposition 6.1. Even if R is not a function of t and x alone, but rather a function of t and x composed with a function depending on all the variables, this gain will be preserved through the composition inequality.

Proof. By applying successively Propositions 4.15 (iv), 4.19 and 4.24 (i), we get

$$
\begin{array}{l} \left\| \int_ {\mathbb {R} ^ {d}} (G \cdot R) (x - v (t - \tau), v)   d v \right\| _ {\mathcal {F} ^ {\lambda t + \mu}} \leqslant \| (G \cdot R) (x - v (t - \tau , v)) \| _ {\mathcal {Z} _ {t / (1 + b)} ^ {\lambda (1 + b), \mu ; 1}} \\ = \| G \cdot R \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu ; 1}} \\ \leqslant d \| G \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu ; 1}}   \| R \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu ; \infty}}, \end{array}
$$

which is the desired result (6.3).

Inequality (6.4) is obtained in a similar way with the help of Proposition 4.34.

Remark 6.4. Let us sketch an alternative proof of Proposition 6.2, which is longer but has the interest to rely on commutators involving$\nabla _ { v } , \nabla _ { x }$and the transport semigroup, al of them classically related to hypoelliptic regularity and velocity averaging. Let$S { = } S _ { \tau - t } ^ { 0 } ,$ so that$R \circ S ( x , v ) { = } R ( x - v ( t - \tau ) , v )$; and let

$$
D = D _ {\tau , t, b} := (\tau - b (t - \tau)) \nabla_ {x} + (1 + b) \nabla_ {v}.
$$

Then, by direct computation,

$$
t \nabla_ {x} (R \circ S) = (D R) \circ S - (1 + b) \nabla_ {v} (R \circ S);\tag{6.5}
$$

and since$\nabla _ { x }$commutes with$\nabla _ { v }$and$D ,$and with the composition by$S$as well, this can be generalized by induction into

$$
(t\nabla_{x})^{n}(R\circ S) = \sum_{\substack{m\in \mathbb{N}_{0}^{d}\\ m\leqslant n}}\binom {n}{m}[-(1 + b)\nabla_{v}]^{m}((D^{n - m}R)\circ S).\tag{6.6}
$$

Applying this formula with R replaced by$G \cdot R$and integrating in v yields

$$
(t \nabla_ {x}) ^ {n} \int_ {\mathbb {R} ^ {d}} (G \cdot R) \circ S _ {\tau - t} ^ {0} d v = \int_ {\mathbb {R} ^ {d}} D ^ {n} (G \cdot R) \circ S _ {\tau - t} ^ {0} d v = \int_ {\mathbb {R} ^ {d}} D ^ {n} (G \cdot R) d v.
$$

It follows by taking Fourier transform that

$$
(2 i \pi t k) ^ {n} \hat {\beta} (k) = \int_ {\mathbb {R} ^ {d}} [ D ^ {n} (G \cdot R) ] ^ {\wedge} d v = \int_ {\mathbb {R} ^ {d}} ((1 + b) \nabla_ {v} + 2 i \pi (\tau - b (t - \tau)) k) ^ {n} (\widehat {G \cdot R}) (k, v) d v,
$$

whence

$$
\begin{array}{l}\sum_{\substack{k\in \mathbb{Z}^{d}\\ n\in \mathbb{N}_{0}^{d}}}e^{2\pi \mu |k|}\frac{|2\pi\lambda tk|^{n}}{n!} |\hat{\beta} (k)|\\ \leqslant \sum_{\substack{k\in \mathbb{Z}^{d}\\ n\in \mathbb{N}_{0}^{d}}}e^{2\pi \mu |k|}\frac{(\lambda(1 + b))^{n}}{n!}\bigg\| \bigg[\nabla_{v} + 2i\pi \bigg(\tau -\frac{bt}{1 + b}\bigg)k\bigg]^{n}(\widehat{G\cdot R})(k,v)\bigg\|_{L^{1}(dv)}\\ \\ = \| G\cdot R\|_{\mathcal{Z}_{\tau -bt / (1 + b)}^{\lambda (1 + b),\mu ;1}}, \end{array}
$$

and then (6.3) follows by Proposition 4.24.

Let us conclude this subsection with some comments on Proposition 6.2. When we wish to apply it, what constraints on$b ( t , \tau )$(assumed to be non-negative to fix the ideas) does this presuppose? First, b should be small, so that$\lambda ( 1 + b ) \leqslant { \bar { \lambda } } .$. But most importantly, we have estimated$G _ { \tau }$in a norm$\mathcal { Z } _ { \tau ^ { \prime } }$instead of$\mathcal { Z } _ { \tau }$(this is the time cheating), where $\vert \tau ^ { \prime } - \tau \vert = b t / ( 1 + b )$. To compensate for this discrepancy, we may apply (4.19), but for this to work$b t / ( 1 + b )$should be small, otherwise we would lose a large index of analyticity in$x ,$or at best we would inherit an undesirable exponentially growing constant. So all we are allowed is$b ( t , \tau ) { = } O ( 1 / ( 1 { + } t ) )$. This is not enough to get the time-decay which would lead to Landau damping. Indeed, if$R { = } R ( x )$with$\widehat { R } ( 0 ) = 0$, then

$$
\left\| R \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), \mu}} = \left\| R \right\| _ {\mathcal {F} ^ {\lambda \tau + \mu - \lambda b (t - \tau)}} \leqslant e ^ {- \lambda b (t - \tau)} \| R \| _ {\mathcal {F} ^ {\lambda \tau + \mu}};
$$

so we gain a coeficient$e ^ { - \lambda b ( t - \tau ) }$, but then

$$
\int_ {0} ^ {t} e ^ {- \lambda b (t - \tau)} d \tau \geqslant \int_ {0} ^ {t} e ^ {- \lambda \varepsilon (t - \tau) / t} d \tau = \left(\frac {1 - e ^ {- \lambda \varepsilon}}{\lambda \varepsilon}\right) t,
$$

which of course diverges in large time.

To summarize: Proposition 6.2 is helpful when$t - \tau { = } O ( 1 )$, or when some extra time-decay is available. This will already be very useful; but for long-time estimates we need another, complementary mechanism.

## 6.3. Long-term regularity extortion

To search for the extra decay, let us refine the computation of the beginning of this section. Assume that$G _ { \tau } { = } \nabla _ { v } g _ { \tau }$, where$( g _ { \tau } ) _ { \tau \geqslant 0 }$solves a transport-like equation, so $\widetilde { G } ( \tau , k , \eta ) { = } 2 i \pi \eta \widetilde { g } ( \tau , k , \eta )$, and

$$
| \widetilde {G} (\tau , k, \eta) | \lesssim 2 \pi | \eta | e ^ {- 2 \pi \bar {\mu} | k |} e ^ {- 2 \pi \bar {\lambda} | \eta + k \tau |}.
$$

Up to slightly increasing λ<sup>¯</sup> and$\bar { \mu } ,$we may assume that

$$
| \widetilde {G} (\tau , k, \eta) | \lesssim (1 + \tau) e ^ {- 2 \pi \bar {\mu} | k |} e ^ {- 2 \pi \bar {\lambda} | \eta + k \tau |}.\tag{6.7}
$$

Let then$\scriptstyle \varrho ( \tau , x ) = \int _ { \mathbb { R } ^ { d } } f ( \tau , x , v )$dv, where also$f$solves a transport equation, but has a lower analytic regularity; and$R { = } \nabla W * \varrho .$Assuming that$\widehat { | \nabla W ( k ) | } = O ( | k | ^ { - \gamma } )$for some $\gamma \geqslant 0 ,$, we have

$$
| \widehat {R} (\tau , k) | \lesssim \frac {e ^ {- 2 \pi (\lambda \tau + \mu) | k |} 1 _ {k \neq 0}}{1 + | k | ^ {\gamma}}.\tag{6.8}
$$

Let again

$$
\sigma (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} G (\tau , x - v (t - \tau), v) \cdot R (\tau , x - v (t - \tau)) d v d \tau .
$$

As$t \to \infty , G$in the integrand of σ oscillates wildly in phase space, so it is not clear that it will help at all. But let us compute

$$
\begin{array}{l} \hat {\sigma} (t, k) = \int_ {0} ^ {t} \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} G (\tau , x - v (t - \tau), v) \cdot R (\tau , x - v (t - \tau)) e ^ {- 2 i \pi k \cdot x} d v d x d \tau \\ \qquad = \int_ {0} ^ {t} \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} G (\tau , x, v) \cdot R (\tau , x) e ^ {- 2 i \pi k \cdot x} e ^ {- 2 i \pi k \cdot v (t - \tau)} d v d x d \tau \\ \qquad = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} \widehat {G \cdot R} (\tau , k, v) e ^ {- 2 i \pi k \cdot v (t - \tau)} d v d \tau \\ \qquad = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {G} (\tau , l, v) \cdot \widehat {R} (\tau , k - l) e ^ {- 2 i \pi k \cdot v (t - \tau)} d v d \tau \\ \qquad = \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widetilde {G} (\tau , l, k (t - \tau)) \cdot \widehat {R} (\tau , k - l) d \tau . \end{array}
$$

At this level, the diference with respect to the beginning of this section lies in the fact that there is a summation over$l \in \mathbb { Z } ^ { d }$, instead of just choosing l=0. Note that

$$
\hat {\sigma} (t, 0) = \int_ {0} ^ {t} \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} G (\tau , x, v) \cdot R (\tau , x) d v d x d \tau = 0,
$$

because G is a v-gradient.

From (6.7) and (6.8) we deduce that

$$
\sum_{k\in \mathbb{Z}^{d}}|\tilde{\sigma} (t,k)|e^{2\pi (\lambda t + \mu)|k|}\\ \lesssim \int_{0}^{t}(1 + \tau)\sum_{\substack{k,l\in \mathbb{Z}^{d}\\ 0\neq k\neq l}}e^{2\pi \mu |k|}e^{2\pi \lambda t|k|}e^{-2\pi \bar{\mu}|l|}e^{-2\pi \bar{\lambda} |k(t - \tau) + l\tau |}e^{-2\pi \mu |k - l|}\frac{e^{-2\pi\lambda\tau|k - l|}}{1 + |k - l|^{\gamma}}  d\tau .
$$

Using the inequalities

$$
e ^ {- 2 \pi \mu | k - l |} e ^ {2 \pi \mu | k |} e ^ {- 2 \pi \bar {\mu} | l |} \leqslant e ^ {- 2 \pi (\bar {\mu} - \mu) | l |}
$$

and

$$
e ^ {- 2 \pi \lambda \tau | k - l |} e ^ {2 \pi \lambda t | k |} e ^ {- 2 \pi \bar {\lambda} | k (t - \tau) + l \tau |} \leqslant e ^ {- 2 \pi (\bar {\lambda} - \lambda) | k (t - \tau) + l \tau |},
$$

we end up with

$$
\| \sigma (t)\|_{\mathcal{F}^{\lambda t + \mu}}\lesssim \sum_{\substack{k,l\in \mathbb{Z}^{d}\\ 0\neq k\neq l}}\frac{e^{-2\pi(\bar{\mu} - \mu)|l|}}{1 + |k - l|^{\gamma}}\int_{0}^{t}e^{-2\pi (\bar{\lambda} - \lambda)|k(t - \tau) + l\tau |}(1 + \tau)  d\tau .
$$

If it were not for the negative exponential, the time-integral would be$O ( t ^ { 2 } )$as$t \to \infty$ The exponential helps only a bit: its argument vanishes$\mathrm { e . g . }$for$d { = } 1$, k>0,$l < 0$and $\tau { = } k t / ( k { + } | l | )$. Thus we have the essentially optimal bounds

$$
\int_ {0} ^ {t} e ^ {- 2 \pi (\bar {\lambda} - \lambda) | k (t - \tau) + l \tau |} d \tau \leqslant \frac {1}{\pi (\bar {\lambda} - \lambda) | k - l |}\tag{6.9}
$$

and

$$
\int_ {0} ^ {t} e ^ {- 2 \pi (\bar {\lambda} - \lambda) | k (t - \tau) + l \tau |} \tau d \tau \leqslant \frac {1}{2 \pi^ {2} (\bar {\lambda} - \lambda) ^ {2} | k - l | ^ {2}} + \frac {1}{\pi (\bar {\lambda} - \lambda)} \frac {| k | t}{| k - l |}.\tag{6.10}
$$

From this computation we conclude that:

The higher regularity of G has allowed us to reduce the time-integral due to a factor $e ^ { - \alpha | k ( t - \tau ) + l \tau | }$|; but this factor is not small when$\tau / t$is equal to$k / ( k { - } l )$. As discussed in the next section, this reflects an important physical phenomenon called (plasma) echo, which can be assimilated to a resonance.

If we had (in “gliding” norm)$\| G _ { \tau } \| { = } O ( 1 )$this would ensure a uniform bound on the integral, as soon as$\gamma > 0$, due to (6.9) and

$$
\sum_ {k, l \in \mathbb {Z} ^ {d}} \frac {e ^ {- \alpha | l |}}{(1 + | k - l |) ^ {1 + \gamma}} <   \infty .
$$

But$G _ { \tau }$is a velocity gradient, so (unless of course G depends only on v)$\| G _ { \tau } \|$ diverges like$O ( \tau )$as$\tau {  } \infty$, which implies a divergence of our bounds in large time, as can be seen from (6.10).$\mathrm { I f } \ \gamma \leqslant 1$this comes with a divergence in the k variable, since in this case

$$
\sum_ {k, l \in \mathbb {Z} ^ {d}} \frac {e ^ {- \alpha | l |} | k |}{(1 + | k - l |) ^ {1 + \gamma}} = \infty .
$$

(The Coulomb case corresponds to$\gamma = 1$, so in this respect it has a borderline divergence.)

The following estimate adapts this computation to the formalism of hybrid norms, and at the same time allows for a time cheating similar to the one in Proposition 6.2. Fortunately, we shall only need to treat the case when$R { = } R ( \tau , x )$; the more general case with$R { = } R ( \tau , x , v )$would be much more tricky.

Theorem 6.5. (Long-term regularity extortion) Let$G { = } G ( \tau , x , v ) , R { = } R ( \tau , x )$and

$$
\sigma (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} G (\tau , x - v (t - \tau), v) \cdot R (\tau , x - v (t - \tau)) d v d \tau .
$$

Let$\lambda , \bar { \lambda } , \mu , \bar { \mu } , \mu ^ { \prime } { = } \mu ^ { \prime } ( t , \tau )$and$M \geqslant 1$be such that$( 1 + M ) \lambda \geqslant \bar { \lambda } > \lambda > 0$and$\bar { \mu } \geqslant \mu ^ { \prime } > \mu > 0$ and let$\gamma \geqslant 0$and$b { = } b ( t , \tau ) { \geqslant } 0$. Then

$$
\| \sigma (t, \cdot) \| _ {\dot {\mathcal {F}} ^ {\lambda t + \mu}} \leqslant \int_ {0} ^ {t} K _ {0} ^ {G} (t, \tau) \| R _ {\tau} \| _ {\mathcal {F} ^ {\nu}} d \tau + \int_ {0} ^ {t} K _ {1} ^ {G} (t, \tau) \| R _ {\tau} \| _ {\mathcal {F} ^ {\nu , \gamma}} d \tau ,\tag{6.11}
$$

where

$$
\nu = \max \left\{\lambda \tau + \mu^ {\prime} - \frac {1}{2} \lambda b (t - \tau), 0 \right\},\tag{6.12}
$$

$$
K _ {0} ^ {G} (t, \tau) = d e ^ {- \pi (\bar {\lambda} - \lambda) (t - \tau)} \left\| \int_ {\mathbb {T} ^ {d}} G (\tau , x, \cdot) d x \right\| _ {\mathcal {C} ^ {\bar {\lambda} (1 + b); 1}},\tag{6.13}
$$

$$
K _ {1} ^ {G} (t, \tau) = \left(\sup _ {0 \leqslant \tau \leqslant t} \frac {\| G _ {\tau} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\bar {\lambda} (1 + b) , \bar {\mu}}}}{1 + \tau}\right) K _ {1} (t, \tau),\tag{6.14}
$$

$$
\begin{array}{l} K _ {1} (t, \tau) \\ = (1 + \tau) d \sup _ {k, l \in \mathbb {Z} _ {*} ^ {d}} \frac {e ^ {- \pi (\bar {\mu} - \mu) | l |} e ^ {- \pi (\bar {\lambda} - \lambda) | k (t - \tau) + l \tau | / M} e ^ {- 2 \pi [ \mu^ {\prime} - \mu + \lambda b (t - \tau) / 2 ] | k - l |}}{1 + | k - l | ^ {\gamma}}. \end{array}\tag{6.15}
$$

Remark 6.6. It is essential in (6.11) to separate the contribution of$\widehat { G } ( \tau , 0 , v )$from the rest. Indeed, if we removed the restriction$l { \neq } 0$in (6.15) the kernel$K _ { 1 }$would be too large to be correctly controlled in large time. What makes this separation reasonable is that, although in cases of application$G ( \tau , x , v )$is expected to grow like$O ( \tau )$in large time, the spatial average$\textstyle \int _ { \mathbb { T } ^ { d } } G ( \tau , x , v )$dx is expected to be bounded. Also, we will not need to take advantage of the parameter$\gamma$to handle this term.

Proof. Without loss of generality we may assume that$G$and R are scalar-valued. (This explains the constant$d$in front of the right-hand sides of (6.13) and (6.15).) First we assume that$\widehat { G } ( \tau , 0 , v ) = 0$, and we write as before

$$
\begin{array}{c} \hat {\sigma} (t, k) = \int_ {0} ^ {t} \bigg (\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \int_ {\mathbb {R} ^ {d}} \widehat {G} (\tau , l, v) \widehat {R} (\tau , k - l) e ^ {- 2 i \pi k \cdot v (t - \tau)} d v \bigg) d \tau , \\ | \hat {\sigma} (t, k) | \leqslant \int_ {0} ^ {t} \bigg (\sum_ {l \in \mathbb {Z} ^ {d}} \Big | \int_ {\mathbb {R} ^ {d}} \widehat {G} (\tau , l, v) e ^ {- 2 i \pi k \cdot v (t - \tau)} d v \Big | | \widehat {R} (\tau , k - l) | \bigg) d \tau . \end{array}\tag{6.16}
$$

Next we let$\scriptstyle { \tau ^ { \prime } = \tau - b ( t - \tau ) }$and write

$$
\begin{array}{r} e ^ {2 \pi (\lambda t + \mu) | k |} \leqslant e ^ {- 2 \pi (\bar {\mu} - \mu) | l |} e ^ {- 2 \pi \lambda (\tau - \tau^ {\prime}) | k - l |} e ^ {- 2 \pi (\mu^ {\prime} - \mu) | k - l |} e ^ {- 2 \pi (\bar {\lambda} - \lambda) | k (t - \tau^ {\prime}) + l \tau^ {\prime} |} \\ \times e ^ {2 \pi \bar {\mu} | l |} e ^ {2 \pi (\lambda \tau + \mu^ {\prime}) | k - l |} e ^ {2 \pi \bar {\lambda} | k (t - \tau^ {\prime}) + l \tau^ {\prime} |}. \end{array}\tag{6.17}
$$

Since$0 \leqslant \bar { \lambda } - \lambda \leqslant M \lambda$, we have

$$
e ^ {- 2 \pi (\bar {\lambda} - \lambda) | k (t - \tau^ {\prime}) + l \tau^ {\prime} |} \leqslant e ^ {- \pi (\bar {\lambda} - \lambda) | k (t - \tau) + l \tau | / M} e ^ {\pi \lambda (\tau - \tau^ {\prime}) | k - l |};
$$

so (6.17) implies that

$$
\begin{array}{r l} & e ^ {2 \pi (\lambda t + \mu) | k |} \leqslant e ^ {- 2 \pi (\bar {\mu} - \mu) | l |} e ^ {- \pi (\bar {\lambda} - \lambda) | k (t - \tau) + l \tau | / M} e ^ {- 2 \pi [ \mu^ {\prime} - \mu + \lambda (\tau - \tau^ {\prime}) / 2 ] | k - l |} \\ & \qquad \times e ^ {2 \pi \bar {\mu} | l |} e ^ {2 \pi (\lambda \tau + \mu^ {\prime}) | k - l |} \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {| 2 i \pi \bar {\lambda} (k (t - \tau^ {\prime}) + l \tau^ {\prime}) | ^ {n}}{n !}. \end{array}\tag{6.18}
$$

For each$\boldsymbol { n } \in \mathbb { N } _ { 0 } ^ { d }$

$$
\begin{array}{l} \frac {| 2 i \pi \bar {\lambda} (k (t - \tau^ {\prime}) + l \tau^ {\prime}) | ^ {n}}{n !} \bigg | \int_ {\mathbb {R} ^ {d}} \widehat {G} (\tau , l, v) e ^ {- 2 i \pi k \cdot v (t - \tau)} d v \bigg | \\ = \frac {\bar {\lambda} ^ {n}}{n !} \bigg | \int_ {\mathbb {R} ^ {d}} \widehat {G} (\tau , l, v) [ 2 i \pi (k (t - \tau^ {\prime}) + l \tau^ {\prime}) ] ^ {n} e ^ {- 2 i \pi k \cdot v (t - \tau)} d v \bigg | \\ = \frac {\bar {\lambda} ^ {n}}{n !} \left(\frac {t - \tau^ {\prime}}{t - \tau}\right) ^ {n} \bigg | \int_ {\mathbb {R} ^ {d}} \widehat {G} (\tau , l, v) \bigg [ 2 i \pi \bigg (k (t - \tau) + l \tau^ {\prime} \bigg (\frac {t - \tau}{t - \tau^ {\prime}} \bigg) \bigg) \bigg ] ^ {n} e ^ {- 2 i \pi k \cdot v (t - \tau)} d v \bigg | \\ = \frac {\bar {\lambda} ^ {n}}{n !} \left(\frac {t - \tau^ {\prime}}{t - \tau}\right) ^ {n} \bigg | \int_ {\mathbb {R} ^ {d}} \widehat {G} (\tau , l, u) \bigg [ - \nabla_ {v} + 2 i \pi l \tau^ {\prime} \bigg (\frac {t - \tau}{t - \tau^ {\prime}} \bigg) \bigg ] ^ {n} e ^ {- 2 i \pi k \cdot v (t - \tau)} d v \bigg | \\ = \frac {\bar {\lambda} ^ {n}}{n !} \left(\frac {t - \tau^ {\prime}}{t - \tau}\right) ^ {n} \bigg | \int_ {\mathbb {R} ^ {d}} \bigg [ \nabla_ {v} + 2 i \pi l \tau^ {\prime} \bigg (\frac {t - \tau}{t - \tau^ {\prime}} \bigg) \bigg ] ^ {n} \widehat {G} (\tau , l, v) e ^ {- 2 i \pi k \cdot v (t - \tau)} d v \bigg | \\ \leqslant \frac {\bar {\lambda} ^ {n}}{n !} \left(\frac {t - \tau^ {\prime}}{t - \tau}\right) ^ {n} \| (\nabla_ {v} + 2 i \pi l \tau^ {\prime} \bigg (\frac {t - \tau}{t - \tau^ {\prime}} \bigg)) ^ {n} \widehat {G} (\tau , l, v) \| _ {L ^ {1} (d v)} \\ = \frac {\bar {\lambda} ^ {n} (1 + b) ^ {n}}{n !} \| (\nabla_ {v} + 2 i \pi l (\tau - \frac {b t}{1 + b})) ^ {n} \widehat {G} (\tau , l, v) \| _ {L ^ {1} (d v)}. \end{array}
$$

Combining this with (6.16) and (6.18), and summing over$k ,$, we deduce that

$$
\begin{array}{l}\| \sigma (t,\cdot)\|_{\dot{\mathcal{F}}^{\lambda t + \mu}}\\ = \sum_{k\in \mathbb{Z}_{*}^{d}}e^{2\pi (\lambda t + \mu)|k|}|\hat{\sigma} (t,k)|\\ \leqslant \int_{0}^{t}\sum_{\substack{k,l\in \mathbb{Z}^{d}\\ n\in \mathbb{N}_{0}^{d}}}\frac{e^{-2\pi(\bar{\mu} - \mu)|l|}e^{-\pi(\bar{\lambda} - \lambda)|k(t - \tau) + l\tau| / M}e^{-2\pi[\mu^{\prime} - \mu + \lambda(\tau - \tau^{\prime}) / 2] |k - l|}}{1 + |k - l|^{\gamma}}\\ \times e^{2\pi \bar{\mu}|l|}e^{2\pi [\lambda \tau + \mu^{\prime} - \lambda b(t - \tau) / 2]|k - l|}\frac{\bar{\lambda}^{n}(1 + b)^{n}}{n!} |\widehat{R} (\tau ,k - l)|\\ \times \bigg\| \bigg(\nabla_{v} + 2i\pi l\bigg(\tau -\frac{bt}{1 + b}\bigg)\bigg)^{n}\widehat{G} (\tau ,l,v)\bigg\|_{L^{1}(dv)}d\tau , \end{array}
$$

and the desired estimate follows readily.

Finally we consider the contribution of

$$
\widehat {G} (\tau , 0, v) = \int_ {\mathbb {T} ^ {d}} G (\tau , x, v) d x.
$$

This is done in the same way, noting that

$$
\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \frac {e ^ {- 2 \pi (\bar {\lambda} - \lambda) | k | (t - \tau)}}{1 + | k | ^ {\gamma}} \leqslant e ^ {- 2 \pi (\bar {\lambda} - \lambda) (t - \tau)}.
$$

To conclude this section we provide a “mode-by-mode” variant of Theorem$6 . 5 ;$this will be useful for very singular interactions$( \gamma = 1$in Theorem 2.6).

Theorem 6.7. Under the same assumptions as in Theorem 6.5, for all$k \in  { \mathbb { Z } ^ { d } }$we have the estimate

$$
\begin{array}{r l} & e ^ {2 \pi (\lambda t + \mu) | k |} | \hat {\sigma} (t, k) | \leqslant \int_ {0} ^ {t} K _ {0} ^ {G} (t, \tau) (e ^ {2 \pi \nu | k |} | \widehat {R} (\tau , k) |) d \tau \\ & \qquad + \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} K _ {k, l} ^ {G} (t, \tau) e ^ {2 \pi \nu | k - l |} (1 + | k - l | ^ {\gamma}) | \widehat {R} (\tau , k - l) | d \tau , \end{array}\tag{6.19}
$$

where$K _ { 0 } ^ { G }$is defined by (6.13), ν by (6.12) and

$$
\begin{array}{l} K _ {k, l} ^ {G} (t, \tau) = \bigg (\sup _ {0 \leqslant \tau \leqslant t} \frac {\| G \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\bar {\lambda} (1 + b) , \bar {\mu} ; 1}}}{1 + \tau} \bigg) K _ {k, l} (t, \tau), \\ K _ {k, l} (t, \tau) = \frac {(1 + \tau) d e ^ {- 2 \pi (\bar {\mu} - \mu) | l |} e ^ {- \pi (\bar {\lambda} - \lambda) | k (t - \tau) + l \tau | / M} e ^ {- 2 \pi [ \mu^ {\prime} - \mu + \lambda b (t - \tau) / 2 ] | k - l |}}{1 + | k - l | ^ {\gamma}}. \end{array}
$$

Proof. The proof is similar to that of Theorem 6.5, except that$k$is fixed and we use, for each$l ,$the crude bound

$$
\begin{array}{c} e ^ {2 \pi \bar {\mu} | l |} \bigg \| \bigg (\nabla_ {v} + 2 i \pi l \bigg (\tau - \frac {b t}{1 + b} \bigg) \bigg) ^ {n} \widehat {G} (\tau , l, v) \bigg \| _ {L ^ {1} (d v)} \\ \leqslant \sum_ {j \in \mathbb {Z} ^ {d}} e ^ {2 \pi \bar {\mu} | j |} \bigg \| \bigg (\nabla_ {v} + 2 i \pi j \bigg (\tau - \frac {b t}{1 + b} \bigg) \bigg) ^ {n} \widehat {G} (\tau , j, v) \bigg \| _ {L ^ {1} (d v)}. \end{array}
$$

## 7. Control of the time-response

To motivate this section, let us start from the linearized equation (3.3), but now assume that$f ^ { 0 }$depends on$t , x$and$v ,$and that there is an extra source term$S ,$, decaying in time. Thus the equation is

$$
\frac {\partial f}{\partial t} + v \cdot \nabla_ {x} f - (\nabla W * \varrho) \cdot \nabla_ {v} f ^ {0} = S,
$$

and the equation for the density$\varrho ,$as in the proof of Theorem 3.1, is

$$
\begin{array}{l} \varrho (t, x) = \int_ {\mathbb {R} ^ {d}} f _ {i} (x - v t, v) d v \\ \qquad + \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} \nabla_ {v} f ^ {0} (\tau , x - v (t - \tau), v) \cdot (\nabla W * \varrho) (\tau , x - v (t - \tau)) d v d \tau \\ \qquad + \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} S (\tau , x - v (t - \tau), v) d v d \tau . \end{array}\tag{7.1}
$$

Hopefully we may apply Theorem 6.5 to deduce from (7.1) an integral inequality on $\varphi ( t ) : = \| \varrho ( t ) \| _ { \mathcal { F } ^ { \lambda t + \mu } }$, which will look like

$$
\varphi (t) \leqslant A + c \int_ {0} ^ {t} K (t, \tau) \varphi (\tau) d \tau ,\tag{7.2}
$$

where A is the contribution of the initial datum and the source term, and$K ( t , \tau )$is a kernel looking like, say, (6.15).

How do we proceed from (7.2)? Assume for a start that a smallness condition of the form$\mathrm { ( a ) }$in Proposition 2.1 is satisfied. Then the simple and natural way, as in$\ S 3 .$, would be to write

$$
\varphi (t) \leqslant A + c \left(\int_ {0} ^ {t} K (t, \tau) d \tau\right) \sup _ {0 \leqslant \tau \leqslant t} \varphi (\tau)
$$

and deduce that

$$
\varphi (t) \leqslant \frac {A}{1 - c \int_ {0} ^ {t} K (t , \tau) d \tau}\tag{7.3}
$$

(assuming of course the denominator to be positive). However, if K is given by (6.15), it is easily seen that$\textstyle \int _ { 0 } ^ { t } K ( t , \tau ) d \tau \geq varkappa t$as$t \to \infty$, where$\varkappa > 0 ;$then (7.3) is useless. In fact (7.2) does not prevent$\varphi$from tending to as$t \to \infty$. Nevertheless, its growth may be controlled under certain assumptions, as we shall see in this section. Before embarking on cumbersome calculations, we shall start with a qualitative discussion.

## 7.1. Qualitative discussion

The kernel K in (6.15) depends on the choice of$\mu ^ { \prime } { = } \mu ( t , \tau )$. How large$\mu ^ { \prime } - \mu$can be depends in turn on the amount of regularization ofered by the convolution with the interaction W. We shall distinguish several cases according to the regularity of the interaction.

## 7.1.1. Analytic interaction

If W is analytic, there is$\sigma > 0$such that

$$
\| \varrho * \nabla W \| _ {\mathcal {F} ^ {\nu + \sigma}} \leqslant C \| \varrho \| _ {\mathcal {F} ^ {\nu}} \quad \text { for   all } \nu \geqslant 0;
$$

then in (6.15) we can aford to choose, say,$\mu ^ { \prime } { - } \mu { = } \sigma$and$\gamma = 0$. Thus, assuming that

$$
b = \frac {B}{1 + t}
$$

with B so small that$\begin{array} { r } { ( \mu ^ { \prime } - \mu ) - \lambda b ( t - \tau ) \geqslant \frac { 1 } { 2 } \sigma , } \end{array}$, K is bounded by

$$
\overline {{K}} ^ {(\alpha)} (t, \tau) = (1 + \tau) \sup _ {l, k \in \mathbb {Z} _ {*} ^ {d}} e ^ {- \alpha | l |} e ^ {- \alpha | k - l |} e ^ {- \alpha | k (t - \tau) + l \tau |},\tag{7.4}
$$

where$\scriptstyle \alpha = { \frac { 1 } { 2 } } \operatorname* { m i n } \{ { \bar { \lambda } } - \lambda , { \bar { \mu } } - \mu , \sigma \}$. To fix ideas, let us work in dimension$d { = } 1$. The goal is to estimate solutions of

$$
\varphi (t) \leqslant a + c \int_ {0} ^ {t} \overline {{{K}}} ^ {(\alpha)} (t, \tau) \varphi (\tau) d \tau .\tag{7.5}
$$

Whenever$\tau / t$is a rational number distinct from 0 or 1, there are$k , l \in \mathbb { Z }$such that $| k ( t - \tau ) + l \tau | = 0 .$, and the size of$\overline { { K } } ^ { ( \alpha ) } ( t , \tau )$mainly depends on the minimum admissible values of$k$and$k - l .$. Looking at values of$\tau / t$of the form$1 / ( n + 1 ) { \mathrm { ~ o r ~ } } n / ( n + 1 )$suggests the approximation

$$
\overline {{K}} ^ {(\alpha)} \lesssim (1 + \tau) \min \{e ^ {- \alpha \tau / (t - \tau)} e ^ {- 2 \alpha}, e ^ {- 2 \alpha (t - \tau) / \tau} e ^ {- \alpha} \}.\tag{7.6}
$$

But this estimate is terrible: the time-integral of the right-hand side is much larger than the integral of$\overline { { K } } ^ { ( \alpha ) }$. In fact, the fast variation and “wiggling” behavior of$\overline { { K } } ^ { ( \alpha ) }$are essential to get decent estimates.

To get a better feeling for$\overline { { K } } ^ { ( \alpha ) }$, let us only retain the term for$k { = } 1$and$l { = } { - } 1 ;$this seems reasonable since we have an exponential decay as$k$or l tend to infinity (anyway, throwing away all other terms can only improve the estimates). So we look at

$$
\widetilde {K} ^ {(\alpha)} (t, \tau) = (1 + \tau) e ^ {- 3 \alpha} e ^ {- \alpha | t - 2 \tau |}.
$$

Let us time-rescale by setting$k _ { t } ( \theta ) = t \widetilde { K } ^ { ( \alpha ) } ( t , t \theta )$for$\theta \in [ 0 , 1 ]$(the t factor appears because $d \tau { = } t d \theta )$!; then it is not hard to see that

$$
\frac {k _ {t}}{t} \rightarrow \frac {e ^ {- 3 \alpha}}{2 \alpha} \delta_ {1 / 2}.
$$

This suggests the following baby model for (7.5):

$$
\varphi (t) \leqslant a + c t \varphi \left(\frac {1}{2} t\right).\tag{7.7}
$$

The important point in (7.7) is that, although the kernel has total mass$O ( t )$, this mass is located far from the endpoint$\tau { = } t ;$this is what prevents the fast growth of$\varphi .$ Compare with the inequality$\varphi ( t ) \leqslant a + c t \varphi ( t )$, which implies no restriction at all on$\varphi .$

To be slightly more quantitative, let us look for a power series

$$
\Phi (t) = \sum_ {k = 0} ^ {\infty} a _ {k} t ^ {k}
$$

![](images/page_80_chart_0.jpg)

![](images/page_80_chart_1.jpg)

![](images/page_80_chart_2.jpg)

Figure 5. The kernel$\overline { { K } } ^ { ( \alpha ) } ( t , \tau ) .$, together with the approximate upper bound in (7.6), for α=0.5 and$t = 1 0 , t = 1 0 0$and t=1000, respectively.

achieving equality in (7.7). This yields$a _ { 0 } { = } a$and$a _ { k + 1 } = c a _ { k } 2 ^ { - k }$, so

$$
\Phi (t) = a \sum_ {k = 0} ^ {\infty} \frac {c ^ {k} t ^ {k}}{2 ^ {k (k - 1) / 2}}.\tag{7.8}
$$

The function$\Phi$exhibits a truly remarkable behavior: it grows faster than any polynomial, but slower than any fractional exponential exp$\displaystyle ( c t ^ { \nu } ) , \nu \in ( 0 , 1 )$; essentially it behaves like $A ^ { \left( \log t \right) ^ { 2 } }$(as can also be seen directly from (7.7)). One may conjecture that solutions of (7.5) exhibit a similar kind of growth.

Let us interpret these calculations. Typically, the kernel K controls the time variation of (say) the spatial density  which is due to binary interaction of waves. When two waves of distinct frequencies interact, the efect over a long time-period is most of the time very small; this is a consequence of the oscillatory nature of the evolution, and the resulting time-averaging. But at certain particular times, the interaction becomes strong: this is known in plasma physics as the plasma echo, and can be thought of as a kind of resonance. Spectacular experiments by Malmberg and collaborators are based on this efect [32], [60]. Namely, if one starts a wave at frequency l at time$0 ,$and forces it at time$\tau$by a wave of frequency$k - l ,$a strong response is obtained at time t and frequency k such that

$$
k (t - \tau) + l \tau = 0\tag{7.9}
$$

(which of course is possible only if k and l are parallel to each other, with opposite directions).

In the present non-linear setting, whatever variation the density function is subject to, will result in echoes at later times. Even if each echo in itself will eventually decay, the problem is whether the accumulation of echoes will trigger an uncontrolled growth (unstability). As long as the expected growth is eaten by the time-decay coming from the linear theory, non-linear Landau damping is expected. In the present case, the growth of (7.8) is very slow in regard of the exponential time-decay due to the analytic regularity.

## 7.1.2. Sobolev interaction

If W only has Sobolev regularity, we cannot aford in (6.15) to take$\mu ^ { \prime } ( t , \tau )$larger than $\mu { + } \eta ( t { - } \tau ) / t$(because the amount of regularity transferred in the bilinear estimates is only$O ( ( t - \tau ) / t )$, recall the discussion at the end of 6.2). On the other hand, we have $\gamma > 0$such that

$$
\| \nabla W * \varrho \| _ {\mathcal {F} ^ {\nu , \gamma}} \leqslant C \| \varrho \| _ {\mathcal {F} ^ {\nu}} \quad \text { for   all } \nu \geqslant 0.
$$

and then we can choose this$\gamma$in (6.15). So, assuming$\scriptstyle b = B / ( 1 + t )$with B so small that $( \mu ^ { \prime } - \mu ) - \lambda b ( t - \tau ) \geqslant \eta ( t - \tau ) / 2 t , K$in (6.15) will be controlled by

$$
K ^ {(\alpha), \gamma} (t, \tau) = (1 + \tau) d \sup _ {l, k \in \mathbb {Z} _ {*}} \frac {e ^ {- \alpha | l |} e ^ {- \alpha (t - \tau) | k - l | / t} e ^ {- \alpha | k (t - \tau) + l \tau |}}{1 + | k - l | ^ {\gamma}},\tag{7.10}
$$

where$\scriptstyle \alpha = { \frac { 1 } { 2 } } \operatorname* { m i n } \{ { \bar { \lambda } } - \lambda , { \bar { \mu } } - \mu , \eta \}$. The equation we are considering now is

$$
\varphi (t) \leqslant a + \int_ {0} ^ {t} K ^ {(\alpha), \gamma} (t, \tau) \varphi (\tau) d \tau .\tag{7.11}
$$

For, say,$\tau \leqslant { \frac { 1 } { 2 } } t .$, we have$K ^ { ( \alpha ) } \leqslant \overline { { K } } ^ { ( \alpha / 2 ) }$, and the discussion is similar to that in 7.1.1. But when τ aproaches t, the term$e ^ { - \alpha ( t - \tau ) | k - l | / t }$hardly helps. Keeping only$k > 0$and $l { = } { - } 1$(because of the exponential decay in l) leads us to consider the kernel (for simplicity we set$d { = } 1$without loss of generality)

$$
\check {K} ^ {(\alpha)} (t, \tau) = (1 + \tau) \sup _ {k \in \mathbb {Z} _ {*}} \frac {e ^ {- \alpha | k t - (k + 1) \tau |}}{1 + (k + 1) ^ {\gamma}}.
$$

Once again we perform a time-rescaling, setting$\check { k } _ { t } ( \theta ) = t \check { K } ^ { ( \alpha ) } ( t , t \theta )$, and let$t \to \infty$. In this limit each exponential$e ^ { - \alpha | k t - ( k + 1 ) \tau | }$becomes localized in a neighborhood of size $O ( t / k )$around$\scriptstyle \theta = k / ( k + 1 )$, and contributes a Dirac mass at$\scriptstyle \theta = k / ( k + 1 )$, with amplitude $2 / \alpha ( k { + } 1 )$). We get that

$$
\frac {\check {k} _ {t}}{t} \rightarrow \frac {2}{\alpha} \sum_ {k \in \mathbb {Z}} \frac {1}{1 + (k + 1) ^ {\gamma}} \frac {k}{(k + 1) ^ {2}} \delta_ {1 - 1 / (k + 1)} \quad \mathrm{as} t \rightarrow \infty .
$$

This leads us to the following baby model for (7.11):

$$
\varphi (t) \leqslant a + c t \sum_ {k = 1} ^ {\infty} \frac {1}{k ^ {1 + \gamma}} \varphi \left(\left(1 - \frac {1}{k}\right) t\right).\tag{7.12}
$$

If we search for$\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } t ^ { n }$achieving equality, this yields

$$
a _ {0} = a, \quad a _ {n + 1} = c \left(\sum_ {k = 1} ^ {\infty} \frac {1}{k ^ {1 + \gamma}} \left(1 - \frac {1}{k}\right) ^ {n}\right) a _ {n}.
$$

To estimate the behavior of the$\textstyle \sum _ { k }$above, we compare it with

$$
\int_ {1} ^ {\infty} \frac {1}{t ^ {1 + \gamma}} \left(1 - \frac {1}{t}\right) ^ {n} d t = \int_ {0} ^ {t} u ^ {\gamma - 1} (1 - u) ^ {n} d u = B (\gamma , n + 1) = \frac {\Gamma (\gamma) \Gamma (n + 1)}{\Gamma (n + \gamma + 1)} = O \left(\frac {1}{n ^ {\gamma}}\right),
$$

where$B ( \gamma , n + 1 )$is the beta function. All in all, we may expect$\varphi$in (7.11) to behave qualitatively like

$$
\Phi (t) = a \sum_ {n = 0} ^ {\infty} \frac {c ^ {n} t ^ {n}}{(n !) ^ {\gamma}}.
$$

Notice that Φ is subexponential for$\gamma > 1$(it grows essentially like the fractional exponential$\exp ( t ^ { 1 / \gamma } ) )$and exponential for$\gamma = 1$. In particular, as soon as$\gamma > 1$, we expect non-linear Landau damping again.

## 7.1.3. Coulomb–Newton interaction$( \gamma { = } 1 )$

When$\gamma = 1$, as is the case for Coulomb or Newton interaction, the previous analysis becomes borderline, since we expect (7.12) to be compatible with an exponential growth, and the linear decay is also exponential. To handle this more singular case, we shall work mode-by-mode, rather than on just one norm. Starting again from (7.1), we consider, for each$k \in  { \mathbb { Z } ^ { d } }$,

$$
\varphi_ {k} (t) = e ^ {2 \pi (\lambda t + \mu) | k |} | \hat {\varrho} (t, k) |,
$$

and hope to$\mathrm { g e t }$, via Theorem$6 . 7 ,$an inequality which will roughly take the form

$$
\varphi_ {k} (t) \leqslant A _ {k} + c \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} K _ {k, l} (t, \tau) \varphi_ {k - l} (\tau) d \tau .\tag{7.13}
$$

(Note that summing over$k$would yield an inequality worse than (7.11).) To fix the ideas, let us work in dimension$d { = } 1$, and set$k \geqslant 1$and$l { = } { - } 1$. Reasoning as in 7.1.2, we obtain the baby model

$$
\varphi_ {k} (t) \leqslant A _ {k} + \frac {c t}{(k + 1) ^ {1 + \gamma}} \varphi_ {k + 1} \left(\frac {k t}{k + 1}\right).\tag{7.14}
$$

The gain with respect to (7.12) is clear: for diferent values of$k ,$the “dominant times” are distinct. From the physical point of view, we are discovering that, in some sense, echoes occurring at distinct frequencies are asymptotically well separated.

Let us search again for power series solutions: we set

$$
\varphi_ {k} (t) = \sum_ {m = 0} ^ {\infty} a _ {k, m} t ^ {m}, \quad a _ {k, 0} = A _ {k}.
$$

By identification,

$$
a _ {k, m} = a _ {k + 1, m - 1} c (k + 1) ^ {- (1 + \gamma)} \left(\frac {k}{k + 1}\right) ^ {m - 1},
$$

and by induction

$$
a _ {k, m} = A _ {k + m} c ^ {m} \left(\frac {k !}{(k + m) !}\right) ^ {1 + \gamma} \frac {k ^ {m - 1} c ^ {m}}{(k + 1) (k + 2) \dots (k + m)} \simeq A _ {k + m} \left(\frac {k !}{(k + m) !}\right) ^ {\gamma + 2} k ^ {m - 1} c ^ {m}.
$$

We may expect that$A _ { k + m } { \lesssim } A e ^ { - a ( k + m ) }$; then

$$
a _ {k, m} \lesssim A (k e ^ {- a k}) k ^ {m} c ^ {m} \frac {e ^ {- a m}}{(m !) ^ {\gamma + 2}},
$$

and in particular

$$
\varphi_ {k} (t) \lesssim A e ^ {- a k / 2} \sum_ {m = 0} ^ {\infty} \frac {(c k t) ^ {m}}{(m !) ^ {\gamma + 2}} \lesssim A e ^ {(1 - \alpha) (c k t) ^ {\alpha}}, \quad \alpha = \frac {1}{\gamma + 2}.
$$

This behaves like a fractional exponential even for$\gamma = 1$, and we can now believe in non-linear Landau damping for such interactions! (The argument above works even for more singular interactions; but in the proof later the condition$\gamma \geqslant 1$will be required for other reasons, see pp. 152 and 161.)

## 7.2. Exponential moments of the kernel

Now we start to estimate the kernel$K ^ { ( \alpha ) , \gamma }$from (7.10), without any approximation this time. Eventually, instead of proving that the growth is at most fractionally exponential, we shall compare it with a slow exponential$e ^ { \varepsilon t }$. For this, the first step consists in estimating exponential moments of the kernel$\begin{array} { r } { e ^ { - \varepsilon t } \int _ { 0 } ^ { t } K ( t , \tau ) e ^ { \varepsilon \tau } d \tau } \end{array}$. (To get more precise estimates, one can study$\begin{array} { r } { e ^ { - \varepsilon t ^ { \alpha } } \int _ { 0 } ^ { t } K ( t , \tau ) e ^ { \varepsilon \tau ^ { \alpha } } d \tau } \end{array}$, but such a refinement is not needed for the proof of Theorem 2.6.)

The first step consists of estimating exponential moments.

Proposition 7.1. (Exponential moments of the kernel) Let$\gamma \in [ 1 , \infty )$be given. For any$\alpha \in ( 0 , 1 )$, let$K ^ { ( \alpha ) , \gamma }$be defined by (7.10). Then for any$\gamma < \infty$there is$\overline { { \alpha } } = \overline { { \alpha } } ( \gamma ) > 0$ such that if α${ \leqslant } \overline { { \alpha } }$and$\varepsilon \in ( 0 , 1 )$, then for any$t > 0$,

$$
\begin{array}{l} e ^ {- \varepsilon t} \int_ {0} ^ {t} K ^ {(\alpha), \gamma} (t, \tau) e ^ {\varepsilon \tau} d \tau \\ \leqslant C \left(\frac {1}{\alpha \varepsilon^ {\gamma} t ^ {\gamma - 1}} + \frac {1}{\alpha \varepsilon^ {\gamma} t ^ {\gamma}} \log \frac {1}{\alpha} + \frac {1}{\alpha^ {2} \varepsilon^ {1 + \gamma} t ^ {1 + \gamma}} + \left(\frac {1}{\alpha^ {3}} + \frac {1}{\alpha^ {2} \varepsilon} \log \frac {1}{\alpha}\right) e ^ {- \varepsilon t / 4} + \frac {e ^ {- \alpha t / 2}}{\alpha^ {3}}\right), \end{array}
$$

where$C { = } C ( \gamma )$. In particular,

$i f \gamma > 1$and$\varepsilon \leqslant \alpha$, then

$$
e ^ {- \varepsilon t} \int_ {0} ^ {t} K ^ {(\alpha), \gamma} (t, \tau) e ^ {\varepsilon \tau} d \tau \leqslant \frac {C (\gamma)}{\alpha^ {3} \varepsilon^ {1 + \gamma} t ^ {\gamma - 1}};
$$

$i f \ \gamma { = } 1$then

$$
e ^ {- \varepsilon t} \int_ {0} ^ {t} K ^ {(\alpha), \gamma} (t, \tau) e ^ {\varepsilon \tau} d \tau \leqslant \frac {C}{\alpha^ {3}} \left(\frac {1}{\varepsilon} + \frac {1}{\varepsilon^ {2} t}\right).
$$

Remark 7.2. Much stronger estimates can be obtained if the interaction is analytic; that is, when$K ^ { ( \alpha ) , \gamma }$is replaced by$\overline { { K } } ^ { ( \alpha ) }$defined in (7.4). A notable point about Proposition 7.1 is that for$\gamma = 1$we do not have any time-decay as$t \to \infty$

Proof. To simplify notation we shall not recall the dependence of$K$on$\gamma _ { ; }$, and we shall set$d { = } 1$without loss of generality. We first assume that$\gamma < \infty$, and consider$\tau \leqslant \frac { 1 } { 2 } t$ which is the favorable case. We write

$$
K^{(\alpha)}(t,\tau)\leqslant (1 + \tau)\sup_{\substack{l\in \mathbb{Z}\\ k\in \mathbb{Z}_{*}}}e^{-\alpha |l|}e^{-\alpha |k - l| / 2}e^{-\alpha |k(t - \tau) + l\tau |}.
$$

Since we got rid of the condition$l { \neq } 0 .$, the right-hand side is now a non-increasing function of$d .$(To see this, pick up a non-zero component of$k ,$, and recall our norm conventions from Appendix A.1.) So we assume$d { = } 1$. By symmetry we may also assume that$k > 0$

Explicit computations yield

$$
\int_ {0} ^ {t / 2} e ^ {- \alpha | k (t - \tau) + l \tau |} (1 + \tau)   d \tau \leqslant \left\{ \begin{array}{l l} \frac {1}{\alpha (l - k)} + \frac {1}{\alpha^ {2} (l - k) ^ {2}}, & \text {if} l > k, \\ e ^ {- \alpha k t} \bigg (\frac {t}{2} + \frac {t ^ {2}}{8} \bigg), & \text {if} l = k, \\ \frac {e ^ {- \alpha (k + l) t / 2}}{\alpha | k - l |} \bigg (1 + \frac {t}{2} \bigg), & \text {if} - k \leqslant l <   k, \\ \frac {2}{\alpha | k - l |} + \frac {2 k t}{\alpha | k - l | ^ {2}} + \frac {1}{\alpha^ {2} | k - l | ^ {2}}, & \text {if} l <   - k. \end{array} \right.
$$

In all cases,

$$
\begin{array}{r l} & {\int_ {0} ^ {t / 2} e ^ {- \alpha | k (t - \tau) + l \tau |} (1 + \tau) d \tau} \\ & {\qquad \leqslant \bigg (\frac {3}{\alpha | k - l |} + \frac {1}{\alpha^ {2} | k - l | ^ {2}} + \frac {2 t}{\alpha | k - l |} \bigg) 1 _ {k \neq l} + e ^ {- \alpha k t} \bigg (\frac {t}{2} + \frac {t ^ {2}}{8} \bigg) 1 _ {l = k}.} \end{array}
$$

So

$$
\begin{array}{r l} & e ^ {- \varepsilon t} \int_ {0} ^ {t / 2} e ^ {- \alpha | k (t - \tau) + l \tau |} (1 + \tau) e ^ {\varepsilon \tau} d \tau \\ & \qquad \leqslant e ^ {- \varepsilon t / 2} \bigg (\frac {3}{\alpha | k - l |} + \frac {1}{\alpha^ {2} | k - l | ^ {2}} + \frac {2 t}{\alpha | k - l |} \bigg) 1 _ {k \neq l} + e ^ {- \alpha k t} \bigg (\frac {t}{2} + \frac {t ^ {2}}{8} \bigg) 1 _ {l = k} \\ & \qquad \leqslant e ^ {- \varepsilon t / 4} \bigg (\frac {3}{\alpha | k - l |} + \frac {1}{\alpha^ {2} | k - l | ^ {2}} + \frac {8 z}{\alpha \varepsilon | k - l |} \bigg) 1 _ {k \neq l} + e ^ {- t \alpha / 2} \bigg (\frac {z}{\alpha} + \frac {8 z ^ {2}}{\alpha^ {2}} \bigg) 1 _ {l = k}, \end{array}
$$

where$\scriptstyle z = \operatorname* { s u p } _ { x } x e ^ { - x } = e ^ { - 1 }$. Then

$$
\begin{array}{l}e^{\varepsilon t}\int_{0}^{t / 2}K^{(\alpha)}(t,\tau)e^{\varepsilon \tau}  d\tau \leqslant e^{-\varepsilon t / 4}\sum_{\substack{l,k\in \mathbb{Z}\\ 0\neq k\neq l}}e^{-\alpha |l|}e^{-\alpha |k - l| / 2}\bigg(\frac{3}{\alpha|k - l|} +\frac{1}{\alpha^{2}|k - l|^{2}} +\frac{8z}{\alpha\varepsilon|k - l|}\bigg)\\ \\ +e^{-t\alpha /2}\sum_{l\in \mathbb{Z}}e^{-\alpha |l|}\bigg(\frac{z}{\alpha} +\frac{8z^{2}}{\alpha^{2}}\bigg). \end{array}
$$

Using the bounds (for α 0<sup>+</sup>)

$$
\sum_ {l \in \mathbb {Z}} e ^ {- \alpha l} = O \bigg (\frac {1}{\alpha} \bigg), \quad \sum_ {l \in \mathbb {Z}} \frac {e ^ {- \alpha l}}{l} = O \bigg (\log \frac {1}{\alpha} \bigg) \quad \mathrm{and} \quad \sum_ {l \in \mathbb {Z}} \frac {e ^ {- \alpha l}}{l ^ {2}} = O (1),
$$

we end up, for$\alpha \leqslant \frac { 1 } { 4 }$, with a bound like

$$
\begin{array}{r l r} & & {C e ^ {- \varepsilon t / 4} \bigg (\frac {1}{\alpha^ {2}} \log \frac {1}{\alpha} + \frac {1}{\alpha^ {3}} + \frac {1}{\alpha^ {2} \varepsilon} \log \frac {1}{\alpha} \bigg) + C e ^ {- \alpha t / 2} \bigg (\frac {1}{\alpha^ {2}} + \frac {1}{\alpha^ {3}} \bigg)} \\ & & {\leqslant C \bigg [ e ^ {- \varepsilon t / 4} \bigg (\frac {1}{\alpha^ {3}} + \frac {1}{\alpha^ {2} \varepsilon} \log \frac {1}{\alpha} \bigg) + \frac {e ^ {- \alpha t / 2}}{\alpha^ {3}} \bigg ].} \end{array}
$$

(Note that the last term is$O ( t ^ { - 3 } )$, so it is anyway negligible in front of the other terms $\mathrm { i f } \ \gamma \leqslant 4 ;$in this case the restriction$\varepsilon \leqslant \alpha$can be dispended with.)

Next we turn to the more delicate contribution of$\tau \geqslant { \frac { 1 } { 2 } } t$. For this case we write

$$
K ^ {(\alpha)} (t, \tau) \leqslant (1 + \tau) \sup _ {l \in \mathbb {Z} _ {*} ^ {d}} e ^ {- \alpha | l |} \sup _ {k \in \mathbb {Z} ^ {d}} \frac {e ^ {- \alpha | k (t - \tau) + l \tau |}}{1 + | k - l | ^ {\gamma}},\tag{7.15}
$$

and the upper bound is a non-increasing function of$d ,$so we assume that$d { = } 1$. Without loss of generality, we restrict the supremum to$l > 0$

The function$x { \mapsto } ( 1 { + } | x { - } l | ^ { \gamma } ) ^ { - 1 } e ^ { - \alpha | x ( t { - } \tau ) + l \tau | }$is decreasing for$x \geqslant l .$, increasing for $x { \leqslant } { - } l \tau / ( t { - } \tau )$; and on the interval$[ - l \tau / ( t - \tau ) , l ]$its logarithmic derivative goes

$$
\mathrm{from} \left(- \alpha + \frac {\gamma / l t}{1 + ((t - \tau) / l t) ^ {\gamma}}\right) (t - \tau) \quad \mathrm{to} - \alpha (t - \tau).
$$

${ \mathrm { S o } } ,$, if$t \geqslant \gamma / \alpha$, there is a unique maximum at$x { = } { - } l \tau / ( t { - } \tau )$, and the supremum in (7.15) is achieved for k equal to either the lower integer part, or the upper integer part of $- l \tau / ( t - \tau )$. Thus a given integer k occurs in the supremum only for some times$\tau$ satisfying$k { - } 1 { < } { - } l \tau / ( t { - } \tau ) { < } k { + } 1$. Since only negative values of k occur, let us change the sign so that k is non-negative. The equation

$$
k - 1 <   \frac {l \tau}{t - \tau} <   k + 1
$$

is equivalent to

$$
\frac {k - 1}{k + l - 1} t <   \tau <   \frac {k + 1}{k + l + 1} t.
$$

Moreover,$\tau > { \frac { 1 } { 2 } } t$implies that$k \geqslant l .$. Thus, for$t \geqslant \gamma / \alpha .$, we have

$$
\begin{array}{l} e ^ {- \varepsilon t} \int_ {t / 2} ^ {t} K ^ {(\alpha)} (t, \tau) e ^ {\varepsilon \tau} d \tau \\ \qquad \leqslant e ^ {- \varepsilon t} \sum_ {l = 1} ^ {\infty} e ^ {- \alpha l} \sum_ {k = l} ^ {\infty} \int_ {(k - 1) t / (k + l - 1)} ^ {(k + 1) t / (k + l + 1)} (1 + \tau) \frac {e ^ {- \alpha | k (t - \tau) - l \tau |} e ^ {\varepsilon \tau}}{1 + (k + l) ^ {\gamma}} d \tau . \end{array}\tag{7.16}
$$

For$t \leqslant \gamma / \alpha$we have the trivial bound

$$
e ^ {- \varepsilon t} \int_ {t / 2} ^ {t} K ^ {(\alpha)} (t, \tau) e ^ {\varepsilon \tau} d \tau \leqslant \frac {\gamma}{2 \alpha};
$$

so in the sequel we shall just focus on the estimate of (7.16).

To evaluate the integral in the right-hand side of (7.16), we separate according to whether τ is smaller or larger than$k t / ( k { + } l ) ;$we use trivial bounds for$e ^ { \varepsilon \tau }$inside the integral, and in the end we get the explicit bounds

$$
\begin{array}{r l} & e ^ {- \varepsilon t} \int_ {(k - 1) t / (k + l - 1)} ^ {k t / (k + l)} (1 + \tau) e ^ {- \alpha | k (t - \tau) - l \tau |} e ^ {\varepsilon \tau} d \tau \leqslant e ^ {- \varepsilon l t / (k + l)} \bigg (\frac {1}{\alpha (k + l)} + \frac {k t}{\alpha (k + l) ^ {2}} \bigg), \\ & e ^ {- \varepsilon t} \int_ {k t / (k + l)} ^ {(k + 1) t / (k + l + 1)} (1 + \tau) e ^ {- \alpha | k (t - \tau) - l \tau |} e ^ {\varepsilon \tau} d \tau \leqslant e ^ {- \varepsilon l t / (k + l + 1)} \\ & \qquad \times \bigg (\frac {1}{\alpha (k + l)} + \frac {k t}{\alpha (k + l) ^ {2}} + \frac {1}{\alpha^ {2} (k + l) ^ {2}} \bigg). \end{array}
$$

All in all, there is a numeric constant C such that (7.16) is bounded above by

$$
C \sum_ {l = 1} ^ {\infty} e ^ {- \alpha l} \sum_ {k = l} ^ {\infty} \left(\frac {1}{\alpha^ {2} (k + l) ^ {2 + \gamma}} + \frac {1}{\alpha (k + l) ^ {1 + \gamma}} + \frac {k t}{\alpha (k + l) ^ {2 + \gamma}}\right) e ^ {- \varepsilon l t / (k + l)},\tag{7.17}
$$

together with an additional similar term where$e ^ { - \varepsilon l t / ( k + l ) }$is replaced by$e ^ { - \varepsilon l t / ( k + l + 1 ) }$, and which will satisfy similar estimates.

We consider separately the three contributions in the right-hand side of (7.17). The first one is

$$
\frac {1}{\alpha^ {2}} \sum_ {l = 1} ^ {\infty} e ^ {- \alpha l} \sum_ {k = l} ^ {\infty} \frac {e ^ {- \varepsilon l t / (k + l)}}{(k + l) ^ {2 + \gamma}}.
$$

To evaluate the behavior of this sum, we compare it to the 2-dimensional integral

$$
I (t) = \frac {1}{\alpha^ {2}} \int_ {1} ^ {\infty} e ^ {- \alpha x} \int_ {x} ^ {\infty} \frac {e ^ {- \varepsilon x t / (x + y)}}{(x + y) ^ {2 + \gamma}} d y d x.
$$

We change variables$( x , y ) \mapsto ( x , u )$, where$\scriptstyle u ( x , y ) = \varepsilon x t / ( x + y )$. This has Jacobian determinant dx dy/dx$d u { = } \varepsilon x t / u ^ { 2 }$, and we find that

$$
I (t) = \frac {1}{\alpha^ {2} \varepsilon^ {1 + \gamma} t ^ {1 + \gamma}} \int_ {1} ^ {\infty} \frac {e ^ {- \alpha x}}{x ^ {1 + \gamma}} d x \int_ {0} ^ {\varepsilon t / 2} e ^ {- u} u ^ {\gamma} d u = O \left(\frac {1}{\alpha^ {2} \varepsilon^ {1 + \gamma} t ^ {1 + \gamma}}\right).
$$

The same computation for the second integral in the right-hand side of (7.17) yields

$$
\frac {1}{\alpha \varepsilon^ {\gamma} t ^ {\gamma}} \int_ {1} ^ {\infty} \frac {e ^ {- \alpha x}}{x ^ {\gamma}} d x \int_ {0} ^ {\varepsilon t / 2} e ^ {- u} u ^ {\gamma - 1} d u = O \left(\frac {1}{\alpha \varepsilon^ {\gamma} t ^ {\gamma}} \log \frac {1}{\alpha}\right).
$$

(The logarithmic factor arises only for$\gamma { = } 1 . )$

The third exponential in the right-hand side of (7.17) is the worst. It yields a contribution

$$
\frac {t}{\alpha} \sum_ {l = 1} ^ {\infty} e ^ {- \alpha l} \sum_ {k = l} ^ {\infty} \frac {e ^ {- \varepsilon l t k / (k + l)}}{(k + l) ^ {2 + \gamma}}.\tag{7.18}
$$

We compare this with the integral

$$
\frac {t}{\alpha} \int_ {1} ^ {\infty} e ^ {- \alpha x} \int_ {x} ^ {\infty} \frac {e ^ {- \varepsilon x t / (x + y)} y}{(x + y) ^ {2 + \gamma}} d y d x,
$$

and the same change of variables as before equates this with

$$
\begin{array}{c} \frac {1}{\alpha \varepsilon^ {\gamma} t ^ {\gamma - 1}} \int_ {1} ^ {\infty} \frac {e ^ {- \alpha x}}{x ^ {\gamma}} d x \int_ {0} ^ {\varepsilon t / 2} e ^ {- u} u ^ {\gamma - 1} d u - \frac {1}{\alpha \varepsilon^ {1 + \gamma} t ^ {\gamma}} \int_ {1} ^ {\infty} \frac {e ^ {- \alpha x}}{x ^ {\gamma}} d x \int_ {0} ^ {\varepsilon t / 2} e ^ {- u} u ^ {\gamma} d u \\ = O \bigg (\frac {1}{\alpha \varepsilon^ {\gamma} t ^ {\gamma - 1}} \log \frac {1}{\alpha} \bigg). \end{array}
$$

(Again the logarithmic factor arises only for$\gamma = 1 .$)

The proof of Proposition 7.1 follows by collecting all these bounds and keeping only the worst one.□

Remark 7.3. It is not easy to catch (say numerically) the behavior of (7.18), because it comes as a superposition of exponentially decaying modes; any truncation in k would lead to a radically diferent time-asymptotics.

From Proposition 7.1 we deduce$L ^ { 2 }$exponential bounds.

Corollary 7.4.$( L ^ { 2 }$exponential moments of the kernel) With the same notation as in Proposition 7.1,

$$
e ^ {- 2 \varepsilon t} \int_ {0} ^ {t} K ^ {(\alpha), \gamma} (t, \tau) ^ {2} e ^ {2 \varepsilon \tau}   d \tau \leqslant \left\{ \begin{array}{l l} \frac {C (\gamma)}{\alpha^ {4} \varepsilon^ {1 + 2 \gamma} t ^ {2 (\gamma - 1)}}, & \text { if } \gamma > 1, \\ C \bigg (\frac {1}{\alpha^ {3} \varepsilon^ {2}} + \frac {1}{\alpha^ {2} \varepsilon^ {3} t} \bigg), & \text { if } \gamma = 1. \end{array} \right.\tag{7.19}
$$

Proof. This follows easily from Proposition 7.1 and the obvious bound

$$
K ^ {(\alpha), \gamma} (t, \tau) ^ {2} \leqslant C (1 + t) K ^ {(2 \alpha), 2 \gamma} (t, \tau).
$$

## 7.3. Dual exponential moments

Proposition 7.5. With the same notation as in Proposition 7.1, for any$\gamma \geqslant 1$we have

$$
\sup _ {\tau \geqslant 0} e ^ {\varepsilon \tau} \int_ {\tau} ^ {\infty} e ^ {- \varepsilon t} K ^ {(\alpha), \gamma} (t, \tau) d t \leqslant C (\gamma) \left(\frac {1}{\alpha^ {2} \varepsilon} + \frac {1}{\alpha \varepsilon^ {\gamma}} \log \frac {1}{\alpha}\right).\tag{7.20}
$$

Remark 7.6. The corresponding computation for the baby model considered in 7.1.2 is

$$
e ^ {\varepsilon \tau} \frac {1 + \tau}{\alpha} \sum_ {k = 1} ^ {\infty} \frac {e ^ {- \varepsilon (k + 1) \tau / k}}{k ^ {1 + \gamma}} \simeq \frac {1 + \tau}{\alpha} \int_ {1} ^ {\infty} \frac {e ^ {- \varepsilon \tau / x}}{x ^ {1 + \gamma}} d x = \frac {1 + \tau}{\tau^ {\gamma}} \frac {1}{\alpha \varepsilon^ {\gamma}} \int_ {0} ^ {\varepsilon \tau} e ^ {- u} u ^ {\gamma - 1} d u.
$$

So we expect the dependence upon ε in (7.20) to be sharp as$\gamma \to 1$

![](images/page_89_chart_0.jpg)

![](images/page_89_chart_1.jpg)

Figure 6. The function (7.18) for$\gamma = 1$, truncated at$l { = } 1$and$k { \leqslant } K ,$, for$K = 5 , 1 0 ,$, 100, 1000. The decay is slower and slower, but still exponential (picture above); however, the maximum value occurs on a much slower time scale and slowly increases with the truncation parameter (picture below, which is a zoom on shorter times).

Proof. We first reduce to$d { = } 1$, and split the integral as

$$
e ^ {\varepsilon \tau} \int_ {\tau} ^ {\infty} e ^ {- \varepsilon t} K ^ {(\alpha), \gamma} (t, \tau) d t = \underbrace {e ^ {\varepsilon \tau} \int_ {2 \tau} ^ {\infty} e ^ {- \varepsilon t} K ^ {(\alpha) , \gamma} (t , \tau) d t} _ {:= I _ {1}} + \underbrace {e ^ {\varepsilon \tau} \int_ {\tau} ^ {2 \tau} e ^ {- \varepsilon t} K ^ {(\alpha) , \gamma} (t , \tau) d t} _ {:= I _ {2}}.
$$

The first term$I _ { 1 }$is easy: for$2 \tau \leqslant t \leqslant \infty$we have

$$
K ^ {(\alpha), \gamma} (t, \tau) \leqslant (1 + \tau) \sum_ {k = 2} ^ {\infty} \sum_ {l \in \mathbb {Z} _ {*}} e ^ {- \alpha | l | - \alpha | k - l | / 2} \leqslant \frac {C (1 + \tau)}{\alpha^ {2}},
$$

and thus

$$
e ^ {\varepsilon \tau} \int_ {2 \tau} ^ {\infty} e ^ {- \varepsilon t} K ^ {(\alpha), \gamma} (t, \tau) d t \leqslant \frac {C (1 + \tau)}{\alpha^ {2}} e ^ {- \varepsilon \tau} \leqslant \frac {C}{\varepsilon \alpha^ {2}}.
$$

We treat the second term$I _ { 2 }$as in the proof of Proposition 7.1:

$$
\begin{array}{c} e ^ {\varepsilon \tau} \int_ {\tau} ^ {2 \tau} K ^ {(\alpha), \gamma} (t, \tau) e ^ {- \varepsilon t} d t \leqslant e ^ {\varepsilon \tau} (1 + \tau) \sum_ {l = 1} ^ {\infty} e ^ {- \alpha l} \sum_ {k = l} ^ {\infty} \int_ {(k + l + 1) \tau / (k + 1)} ^ {(k + l - 1) \tau / (k - 1)} \frac {e ^ {- \alpha | k (t - \tau) - l \tau |}}{1 + (k + l) ^ {\gamma}} e ^ {- \varepsilon t} d t \\ \leqslant (1 + \tau) \sum_ {l = 1} ^ {\infty} e ^ {- \alpha l} \sum_ {k = l} ^ {\infty} \frac {e ^ {- \varepsilon l \tau / k}}{k ^ {\gamma}} \frac {2}{k \alpha}. \end{array}
$$

We compare this with

$$
\begin{array}{c} \frac {2 (1 + \tau)}{\alpha} \int_ {1} ^ {\infty} e ^ {- \alpha x} \int_ {x} ^ {\infty} \frac {e ^ {- \varepsilon x \tau / y}}{y ^ {1 + \gamma}} d y d x = \frac {2}{\alpha \varepsilon^ {\gamma}} \frac {1 + \tau}{\tau^ {\gamma}} \int_ {1} ^ {\infty} \frac {e ^ {- \alpha x}}{x ^ {\gamma}} \int_ {0} ^ {\varepsilon \tau} e ^ {- u} u ^ {\gamma - 1} d u d x \\ \leqslant \frac {C}{\alpha \varepsilon^ {\gamma}} \log \frac {1}{\alpha}, \end{array}
$$

where we used the change of variable$\scriptstyle u = \varepsilon x \tau / y .$.The desired conclusion follows. Note that as before the term$\log ( 1 / \alpha )$only occurs when$\gamma = 1$, and that, for$\gamma > 1$, one could improve the estimate above into a time-decay of the form$O ( \tau ^ { - ( \gamma - 1 ) } )$□

## 7.4. Growth control

We will now state the main result of this section. For a sequence of functions$\Phi ( k , t )$, $k \in \mathbb { Z } _ { * } ^ { d } { = } \mathbb { Z } ^ { d } \backslash \{ 0 \}$and$t \in \mathbb { R }$, we set

$$
\| \Phi (t) \| _ {\lambda} = \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | \Phi (k, t) | e ^ {2 \pi \lambda | k |}.
$$

We shall use$K ( s ) \Phi ( t )$as a shorthand for$( K ( k , s ) \Phi ( k , t ) ) _ { k \in \mathbb { Z } _ { * } ^ { d } }$, etc.

Theorem 7.7. (Growth control via integral inequalities) Assume that$f ^ { 0 } = f ^ { 0 } ( \boldsymbol { v } )$ and$W { = } W ( x )$satisfy condition (L) from 2.2 with constants$C _ { 0 } , \lambda _ { 0 }$and$\varkappa ;$in particular $| \tilde { f } ^ { 0 } ( \eta ) | \leqslant C _ { 0 } e ^ { - 2 \pi \lambda _ { 0 } | \eta | }$. Let further

$$
C _ {W} = \max \bigg \{\sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | \widehat {W} (k) |, \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | k |   | \widehat {W} (k) | \bigg \}.
$$

Let$A { \geqslant } 0 , \ \mu { \geqslant } 0$and$\lambda \in ( 0 , \lambda ^ { * } ]$with$0 < \lambda ^ { * } < \lambda _ { 0 }$. Let$( \Phi ( k , t ) ) _ { k \in \mathbb { Z } _ { * } ^ { d } , t \geq 0 }$be a continuous function of$t \geqslant 0$, valued in$\mathbb { C } ^ { \mathbb { Z } _ { * } ^ { d } }$, such that

$$
\begin{array}{l} \left\| \Phi (t) - \int_ {0} ^ {t} K ^ {0} (t - \tau) \Phi (\tau) d \tau \right\| _ {\lambda t + \mu} \\ \leqslant A + \int_ {0} ^ {t} \bigg (K _ {0} (t, \tau) + K _ {1} (t, \tau) + \frac {c _ {0}}{(1 + \tau) ^ {m}} \bigg) \| \Phi (\tau) \| _ {\lambda \tau + \mu} d \tau \quad f o r a l l t \geqslant 0, \end{array}\tag{7.21}
$$

where$c _ { 0 } { \geqslant } 0 , m { > } 1$, and$K _ { 0 } ( t , \tau )$and$K _ { 1 } ( t , \tau )$are non-negative kernels. Let

$$
\varphi (t) = \left\| \Phi (t) \right\| _ {\lambda t + \mu}.
$$

Then, we have the following:

(i) Assume that$\gamma > 1$and$K _ { 1 } = c K ^ { ( \alpha ) , \gamma }$for some$c { > } 0 , \alpha { \in } ( 0 , \bar { \alpha } ( \gamma ) )$, where$K ^ { ( \alpha ) , \gamma }$is defined by (7.10), and$\overline { { \alpha } } ( \gamma )$appears in Proposition 7.1. Then there are positive constants C and$\chi ,$depending only on γ, λ∗, λ , , c , C and m, uniform as$\gamma \to 1$, such that if

$$
\sup _ {t \geqslant 0} \int_ {0} ^ {t} K _ {0} (t, \tau) d \tau \leqslant \chi\tag{7.22}
$$

and

$$
\sup _ {t \geqslant 0} \left(\int_ {0} ^ {t} K _ {0} (t, \tau) ^ {2} d \tau\right) ^ {1 / 2} + \sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} K _ {0} (t, \tau) d t \leqslant 1,\tag{7.23}
$$

then for any$\varepsilon \in ( 0 , \alpha )$,

$$
\varphi (t) \leqslant C A \frac {1 + c _ {0} ^ {2}}{\sqrt {\varepsilon}} e ^ {C c _ {0}} \left(1 + \frac {c}{\alpha \varepsilon}\right) e ^ {C T} e ^ {C c (1 + T ^ {2})} e ^ {\varepsilon t} \quad f o r a l l t \geqslant 0,\tag{7.24}
$$

where

$$
T = C \max \biggl \{\left(\frac {c ^ {2}}{\alpha^ {5} \varepsilon^ {2 + \gamma}}\right) ^ {1 / (\gamma - 1)}, \left(\frac {c}{\alpha^ {2} \varepsilon^ {\gamma + 1 / 2}}\right) ^ {1 / (\gamma - 1)}, \left(\frac {c _ {0} ^ {2}}{\varepsilon}\right) ^ {1 / (2 m - 1)} \biggr \}.\tag{7.25}
$$

(ii) Assume that$\begin{array} { r } { K _ { 1 } { = } \sum _ { j { = 1 } } ^ { N } c _ { j } K ^ { ( \alpha _ { j } ) , 1 } } \end{array}$for some$\alpha _ { j } \in ( 0 , \bar { \alpha } ( 1 ) )$), where$\overline { { \alpha } } ( 1 )$appears in Proposition 7.1; then there is a numeric constant$\Gamma > 0$such that whenever

$$
1 \geqslant \varepsilon \geqslant \Gamma \sum_ {j = 1} ^ {N} \frac {c _ {j}}{\alpha_ {j} ^ {3}},
$$

one$h a s ,$with the same notation as in (i),

$$
\varphi (t) \leqslant C A \frac {1 + c _ {0} ^ {2}}{\sqrt {\varepsilon}} e ^ {C c _ {0}} e ^ {C T} e ^ {C c (1 + T ^ {2})} e ^ {\varepsilon t} \quad f o r a l l t \geqslant 0,\tag{7.26}
$$

where

$$
c = \sum_ {j = 1} ^ {N} c _ {j} \quad a n d \quad T = C \max \biggl \{\frac {1}{\varepsilon^ {2}} \sum_ {j = 1} ^ {N} \frac {c _ {j}}{\alpha_ {j} ^ {3}}, \left(\frac {c _ {0} ^ {2}}{\varepsilon}\right) ^ {1 / (2 m - 1)} \biggr \}.
$$

Remark 7.8. Apart from the term$c _ { 0 } / ( 1 + \tau ) ^ { m }$which will appear as a technical correction, there are three diferent kernels appearing in Theorem 7.7: the kernel$K ^ { 0 }$, which is associated with the linearized Landau damping; the kernel$K _ { 1 }$, describing non-linear echoes (due to interaction between diferent Fourier modes); and the kernel$K _ { 0 }$, describing the instantaneous response (due to interaction between identical Fourier modes).

We shall first prove Theorem 7.7 assuming

$$
c _ {0} = 0\tag{7.27}
$$

and

$$
\int_ {0} ^ {\infty} \sup _ {k \in \mathbb {Z} ^ {d}} | K ^ {0} (k, t) | e ^ {2 \pi \lambda_ {0} | k | t} d t \leqslant 1 - \varkappa , \quad \varkappa \in (0, 1),\tag{7.28}
$$

which is a reinforcement of condition (L). Under these assumptions the proof of Theorem 7.7 is much simpler, and its conclusion can be substantially simplified too:$\chi$depends only on$\varkappa { : }$condition (7.23) on$K _ { 0 }$can be dropped; and the factor$e ^ { C T } ( 1 + c / \alpha \varepsilon ^ { 3 / 2 } )$in (7.24) can be omitted. If$\widehat { W } \leqslant 0$(as for gravitational interaction) and$\tilde { f } ^ { 0 } { \geqslant } 0$(as for Maxwellian background), these additional assumptions do not constitute a loss of generality, since (7.28) becomes essentially equivalent to (L), and for$c _ { 0 }$small enough the term$c _ { 0 } ( 1 + \tau ) ^ { - m }$can be incorporated inside$K _ { 0 }$

Proof of Theorem 7.7 under (7.27) and (7.28). We have

$$
\varphi (t) \leqslant A + \int_ {0} ^ {t} \left(| K ^ {0} | (t - \tau) + K _ {0} (t, \tau) + K _ {1} (t, \tau)\right) \varphi (\tau) d \tau ,\tag{7.29}
$$

where$\scriptstyle | K ^ { 0 } ( t ) | = \operatorname* { s u p } _ { k \in \mathbb { Z } ^ { d } } | K ^ { 0 } ( k , t ) |$. We shall estimate$\varphi$by a maximum principle argument. Let$\psi ( t ) = B e ^ { \varepsilon t }$, where B will be chosen later. If ψ satisfies, for some$T \geqslant 0$,

$$
\left\{ \begin{array}{l l} \varphi (t) <   \psi (t), & \text { for } 0 \leqslant t \leqslant T, \\ \psi (t) \geqslant A + \int_ {0} ^ {t} (| K ^ {0} | (t, \tau) + K _ {0} (t, \tau) + K _ {1} (t, \tau)) \psi (\tau) d \tau , & \text { for } t \geqslant T, \end{array} \right.\tag{7.30}
$$

then$u ( t ) { : = } \psi ( t ) - \varphi ( t )$is positive for$t { \leqslant } T$, and satisfies$\begin{array} { r } { u ( t ) \geqslant \int _ { 0 } ^ { t } K ( t , \tau ) u ( \tau ) } \end{array}$dτ for$t \geqslant T$ with$K = | K ^ { 0 } | + K _ { 0 } + K _ { 1 } > 0 ;$; this prevents u from vanishing at later times, so u$\geqslant 0$and $\varphi \leqslant \psi$. Thus it is suficient to establish (7.30).

(i) By Proposition 7.1, and since$\begin{array} { r } { \int _ { 0 } ^ { t } ( | K ^ { 0 } | + K _ { 0 } ) d \tau \leqslant 1 - \frac { 1 } { 2 } \varkappa \left( \mathrm { f o r } \ \chi \leqslant \frac { 1 } { 2 } \varkappa \right) . } \end{array}$

$$
\begin{array}{c} A + \int_ {0} ^ {t} (| K ^ {0} | (t, \tau) + K _ {0} (t, \tau)) \psi (\tau) d \tau + c \int_ {0} ^ {t} K ^ {(\alpha), \gamma} (t, \tau) \psi (\tau) d \tau \\ \leqslant A + \left(1 - \frac {\varkappa}{2} + \frac {c C (\gamma)}{\alpha^ {3} \varepsilon^ {1 + \gamma} t ^ {\gamma - 1}}\right) B e ^ {\varepsilon t}. \end{array}\tag{7.31}
$$

For$t \geqslant T : = ( 4 c C ( \alpha ^ { 3 } \varepsilon ^ { 1 + \gamma } \varkappa ) ) ^ { 1 / ( \gamma - 1 ) }$, this is bounded above by$A + \left( 1 - { \frac { 1 } { 4 } } \varkappa \right) B e ^ { \varepsilon t }$, which in turn is bounded by$B e ^ { \varepsilon t }$as soon as$B { \geqslant } 4 A / \varkappa$

On the other hand, from the inequality

$$
\varphi (t) \leqslant A + \left(1 - \frac {\varkappa}{2}\right) \sup _ {0 \leqslant \tau \leqslant t} \varphi (\tau) + c (1 + t) \int_ {0} ^ {t} \varphi (\tau) d \tau
$$

we deduce that

$$
\varphi (t) \leqslant \frac {2 A}{\varkappa} (1 + t) e ^ {2 c (t + t ^ {2} / 2) / \varkappa}.
$$

In particular, if

$$
\frac {4 A}{\varkappa} e ^ {c ^ {\prime} (T + T ^ {2})} \leqslant B
$$

with$c ^ { \prime } { = } c ^ { \prime } ( c , { \varkappa } )$large enough, then for$0 \leqslant t \leqslant T$we have$\varphi ( t ) \leqslant { \frac { 1 } { 2 } } \psi ( t )$, and (7.30) holds.

(ii)$\begin{array} { r } { K _ { 1 } { = } \sum _ { j { = 1 } } ^ { N } c _ { j } K ^ { ( \alpha _ { j } ) , 1 } } \end{array}$. We use the same reasoning, replacing the right-hand side in (7.31) by

$$
A + \left(1 - \frac {\varkappa}{2} + C \left(\sum_ {j = 1} ^ {N} \frac {c _ {j}}{\alpha_ {j} ^ {3} \varepsilon} + \sum_ {j = 1} ^ {N} \frac {c _ {j}}{\alpha_ {j} ^ {3} \varepsilon^ {2} t}\right)\right) B e ^ {\varepsilon t}.
$$

To conclude the proof, we may first impose a lower bound on$\varepsilon$to ensure that

$$
C \sum_ {j = 1} ^ {N} \frac {c _ {j}}{\alpha_ {j} ^ {3} \varepsilon} \leqslant \frac {\varkappa}{8},\tag{7.32}
$$

and then choose t large enough to guarantee that

$$
C \sum_ {j = 1} ^ {N} \frac {c _ {j}}{\alpha_ {j} ^ {3} \varepsilon^ {2} t} \leqslant \frac {\varkappa}{8};\tag{7.33}
$$

this yields (ii).

Proof of Theorem 7.7 in the general case. We only treat (i), since the reasoning for (ii) is rather similar; and we only establish the conclusion as an a-priori estimate, skipping the continuity/approximation argument needed to turn it into a rigorous estimate. Then the proof is done in three steps.

Step 1. Crude pointwise bounds. From (7.21) we have

$$
\begin{array}{r l} & {\varphi (t) = \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | \Phi (k, t) | e ^ {2 \pi (\lambda t + \mu) | k |}} \\ & {\quad \leqslant A + \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} \int_ {0} ^ {t} | K ^ {0} (k, t - \tau) | e ^ {2 \pi (\lambda t + \mu) | k |} | \Phi (t, \tau) | d \tau} \\ & {\qquad + \int_ {0} ^ {t} \bigg (K _ {0} (t, \tau) + K _ {1} (t, \tau) + \frac {c _ {0}}{(1 + \tau) ^ {m}} \bigg) \varphi (\tau) d \tau} \\ & {\leqslant A + \int_ {0} ^ {t} \bigg (K _ {0} (t, \tau) + K _ {1} (t, \tau) + \frac {c _ {0}}{(1 + \tau) ^ {m}} + \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | K ^ {0} (k, t - \tau) | e ^ {2 \pi \lambda (t - \tau) | k |} \bigg) \varphi (\tau) d \tau .} \end{array}\tag{7.34}
$$

We note that for any$k \in \mathbb { Z } _ { * } ^ { d }$and$t \geqslant 0$

$$
\begin{array}{c} | K ^ {0} (k, t - \tau) | e ^ {2 \pi \lambda | k | (t - \tau)} \leqslant 4 \pi^ {2} | \widehat {W} (k) | C _ {0} e ^ {- 2 \pi (\lambda_ {0} - \lambda) | k | t} | k | ^ {2} t \\ \leqslant \frac {C C _ {0}}{\lambda_ {0} - \lambda} \sup _ {k \in \mathbb {Z} ^ {d}} | k |   | \widehat {W} (k) | \leqslant \frac {C C _ {0} C _ {W}}{\lambda_ {0} - \lambda}, \end{array}
$$

where (here and below) C stands for a numeric constant which may change from line to line. Assuming that$\textstyle \int _ { 0 } ^ { t } K _ { 0 } ( t , \tau ) d \tau \leqslant { \frac { 1 } { 2 } }$, we deduce from (7.34) that

$$
\varphi (t) \leqslant A + \frac {1}{2} \sup _ {0 \leqslant \tau \leqslant t} \varphi (\tau) + C \int_ {0} ^ {t} \left(\frac {C _ {0} C _ {W}}{\lambda_ {0} - \lambda} + c (1 + t) + \frac {c _ {0}}{(1 + \tau) ^ {m}}\right) \varphi (\tau) d \tau ,
$$

and, by Gr¨onwall’s lemma,

$$
\varphi (t) \leqslant 2 A e ^ {C (C _ {0} C _ {W} t / (\lambda_ {0} - \lambda) + c (t + t ^ {2}) + c _ {0} C _ {m})},\tag{7.35}
$$

where$\begin{array} { r } { C _ { m } = \int _ { 0 } ^ { \infty } ( 1 + \tau ) ^ { - m } d \tau } \end{array}$

Step 2.$L ^ { 2 }$bound. This is the step where the smallness assumption (7.22) will be most important. For all$k \in \mathbb { Z } _ { * } ^ { d }$and$t \geqslant 0$we define

$$
\Psi_ {k} (t) = e ^ {- \varepsilon t} \Phi (k, t) e ^ {2 \pi (\lambda t + \mu) | k |},\tag{7.36}
$$

$$
\mathcal {K} _ {k} ^ {0} (t) = e ^ {- \varepsilon t} K ^ {0} (k, t) e ^ {2 \pi (\lambda t + \mu) | k |},\tag{7.37}
$$

$$
R _ {k} (t) = e ^ {- \varepsilon t} \left(\Phi (k, t) - \int_ {0} ^ {t} K ^ {0} (k, t - \tau) \Phi (k, \tau) d \tau\right) e ^ {2 \pi (\lambda t + \mu) | k |} = \left(\Psi_ {k} - \Psi_ {k} * \mathcal {K} _ {k} ^ {0}\right) (t),\tag{7.38}
$$

and we extend all these functions by 0 for negative values of t. Taking Fourier transform in the time-variable yields$\widehat { R } _ { k } = ( 1 - \widehat { K } _ { k } ^ { 0 } ) \widehat { \Psi } _ { k } ;$since condition (L) implies that$| 1 - \widehat { K } _ { k } ^ { 0 } | \geqslant \varkappa .$ we deduce that$\| \widehat { \Psi } _ { k } \| _ { L ^ { 2 } } \leqslant \varkappa ^ { - 1 } \| \widehat { R } _ { k } \| _ { L ^ { 2 } }$, i.e.,

$$
\left\| \Psi_ {k} \right\| _ {L ^ {2} (d t)} \leqslant \frac {\left\| R _ {k} \right\| _ {L ^ {2} (d t)}}{\varkappa}.\tag{7.39}
$$

Plugging (7.39) into (7.38), we deduce that

$$
\| \Psi_ {k} - R _ {k} \| _ {L ^ {2} (d t)} \leqslant \frac {\| \mathcal {K} _ {k} ^ {0} \| _ {L ^ {1} (d t)}}{\varkappa} \| R _ {k} \| _ {L ^ {2} (d t)} \quad \text { for   all } k \in \mathbb {Z} _ {*} ^ {d}.\tag{7.40}
$$

Then

$$
\begin{array}{l} \| \varphi (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)} = \bigg \| \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | \Psi_ {k} | \bigg \| _ {L ^ {2} (d t)} \\ \qquad \leqslant \bigg \| \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | R _ {k} | \bigg \| _ {L ^ {2} (d t)} + \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} \| R _ {k} - \Psi_ {k} \| _ {L ^ {2} (d t)} \\ \qquad \leqslant \bigg \| \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | R _ {k} | \bigg \| _ {L ^ {2} (d t)} \bigg (1 + \frac {1}{\varkappa} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \| \mathcal {K} _ {l} ^ {0} \| _ {L ^ {1} (d t)} \bigg). \end{array}\tag{7.41}
$$

(Note that we bounded$\begin{array} { r } { \Vert R _ { l } \Vert \ \mathrm { b y } \ \Vert \sum _ { k \in \mathbb { Z } _ { * } ^ { d } } | R _ { k } | \Vert } \end{array}$, which seems very crude; but the decay of$\mathcal { K } _ { k } ^ { 0 }$as a function of$k$ will save us.) Next, we note that

$$
\left\| \mathcal {K} _ {k} ^ {0} \right\| _ {L ^ {1} (d t)} \leqslant 4 \pi^ {2} | \widehat {W} (k) | \int_ {0} ^ {\infty} C _ {0} e ^ {- 2 \pi (\lambda_ {0} - \lambda) | k | t} | k | ^ {2} t d t \leqslant 4 \pi^ {2} | \widehat {W} (k) | \frac {C _ {0}}{(\lambda_ {0} - \lambda) ^ {2}},
$$

so

$$
\sum_ {k \in \mathbb {Z} _ {*} ^ {d}} \| \mathcal {K} _ {k} ^ {0} \| _ {L ^ {1} (d t)} \leqslant 4 \pi^ {2} \bigg (\sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | \widehat {W} (k) | \bigg) \frac {C _ {0}}{(\lambda_ {0} - \lambda) ^ {2}}.
$$

Plugging this into (7.41) and using (7.21) again, we obtain

$$
\begin{array}{l} \| \varphi (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)} \\ \leqslant \left(1 + \frac {C C _ {0} C _ {W}}{\varkappa (\lambda_ {0} - \lambda) ^ {2}}\right) \bigg \| \sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | R _ {k} | \bigg \| _ {L ^ {2} (d t)} \\ \leqslant \left(1 + \frac {C C _ {0} C _ {W}}{\varkappa (\lambda_ {0} - \lambda) ^ {2}}\right) \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(A + \int_ {0} ^ {t} \left(K _ {1} + K _ {0} + \frac {c _ {0}}{(1 + \tau) ^ {m}}\right) \varphi (\tau) d \tau\right) ^ {2} d t\right) ^ {1 / 2}. \end{array}\tag{7.42}
$$

We separate this (by Minkowski’s inequality) into various contributions which we estimate separately. First, of course,

$$
\left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} A ^ {2} d t\right) ^ {1 / 2} = \frac {A}{\sqrt {2 \varepsilon}}.\tag{7.43}
$$

Next, for any$T \geqslant 1$, by Step 1 and

$$
\int_ {0} ^ {t} K _ {1} (t, \tau) d \tau \leqslant \frac {C c (1 + t)}{\alpha},
$$

we have

$$
\begin{array}{l} \left(\int_ {0} ^ {T} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {t} K _ {1} (t, \tau) \varphi (\tau)   d \tau\right) ^ {2} d t\right) ^ {1 / 2} \\ \leqslant \Big (\sup _ {0 \leqslant t \leqslant T} \varphi (t) \Big) \left(\int_ {0} ^ {T} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {t} K _ {1} (t, \tau)   d \tau\right) ^ {2} d t\right) ^ {1 / 2} \\ \leqslant C A e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}))} \frac {c}{\alpha} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} (1 + t) ^ {2}   d t\right) ^ {1 / 2} \\ \leqslant C A \frac {c}{\alpha \varepsilon^ {3 / 2}} e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}))}. \end{array}\tag{7.44}
$$

Invoking Jensen’s inequality and Fubini’s theorem, we also have

$$
\begin{array}{l} \left(\int_ {T} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {t} K _ {1} (t, \tau) \varphi (\tau)   d \tau\right) ^ {2} d t\right) ^ {1 / 2} \\ = \left(\int_ {T} ^ {\infty} \left(\int_ {0} ^ {t} K _ {1} (t, \tau) e ^ {- \varepsilon (t - \tau)} e ^ {- \varepsilon \tau} \varphi (\tau)   d \tau\right) ^ {2} d t\right) ^ {1 / 2} \\ \leqslant \left(\int_ {T} ^ {\infty} \left(\int_ {0} ^ {t} K _ {1} (t, \tau) e ^ {- \varepsilon (t - \tau)}   d \tau\right) \left(\int_ {0} ^ {t} K _ {1} (t, \tau) e ^ {- \varepsilon (t - \tau)} e ^ {- 2 \varepsilon \tau} \varphi (\tau) ^ {2}   d \tau\right) d t\right) ^ {1 / 2} \\ \leqslant \left(\sup _ {t \geqslant T} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {1} (t, \tau) e ^ {\varepsilon \tau}   d \tau\right) ^ {1 / 2} \\ \quad \times \left(\int_ {T} ^ {\infty} \int_ {0} ^ {t} K _ {1} (t, \tau) e ^ {- \varepsilon (t - \tau)} e ^ {- 2 \varepsilon \tau} \varphi (\tau) ^ {2}   d \tau   d t\right) ^ {1 / 2} \\ = \left(\sup _ {t \geqslant T} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {1} (t, \tau) e ^ {\varepsilon \tau}   d \tau\right) ^ {1 / 2} \\ \quad \times \left(\int_ {0} ^ {\infty} \int_ {\max \{\tau , T \}} ^ {\infty} K _ {1} (t, \tau) e ^ {- \varepsilon (t - \tau)} e ^ {- 2 \varepsilon \tau} \varphi (\tau) ^ {2}   d t   d \tau\right) ^ {1 / 2} \\ \leqslant \left(\sup _ {t \geqslant T} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {1} (t, \tau) e ^ {\varepsilon \tau}   d \tau\right) ^ {1 / 2} \\ \quad \times \left(\sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} e ^ {\varepsilon \tau} K _ {1} (t, \tau) e ^ {- \varepsilon t}   d t\right) ^ {1 / 2} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon \tau} \varphi (\tau) ^ {2}   d \tau\right) ^ {1 / 2}. \end{array}\tag{7.45}
$$

(Basically we copied the proof of Young’s inequality.) Similarly,

$$
\begin{array}{l} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {t} K _ {0} (t, \tau) \varphi (\tau)   d \tau\right) ^ {2} d t\right) ^ {1 / 2} \\ \leqslant \left(\sup _ {t \geqslant 0} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {0} (t, \tau) e ^ {\varepsilon \tau}   d \tau\right) ^ {1 / 2} \\ \quad \times \left(\sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} e ^ {\varepsilon \tau} K _ {0} (t, \tau) e ^ {- \varepsilon t}   d t\right) ^ {1 / 2} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon \tau} \varphi (\tau) ^ {2}   d \tau\right) ^ {1 / 2} \\ \leqslant \left(\sup _ {t \geqslant 0} \int_ {0} ^ {t} K _ {0} (t, \tau)   d \tau\right) ^ {1 / 2} \left(\sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} K _ {0} (t, \tau)   d t\right) ^ {1 / 2} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon \tau} \varphi (\tau) ^ {2}   d \tau\right) ^ {1 / 2}. \end{array}\tag{7.46}
$$

The last term is also split, this time according to$\tau \leqslant T$or$\tau > T$

$$
\begin{array}{l} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {T} \frac {c _ {0} \varphi (\tau)}{(1 + \tau) ^ {m}} d \tau\right) ^ {2} d t\right) ^ {1 / 2} \\ \leqslant c _ {0} \Big (\sup _ {0 \leqslant \tau \leqslant T} \varphi (\tau) \Big) \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {T} \frac {d \tau}{(1 + \tau) ^ {m}}\right) ^ {2} d t\right) ^ {1 / 2} \\ \leqslant c _ {0} \frac {C A}{\sqrt {\varepsilon}} e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}))} C _ {m}, \end{array}\tag{7.47}
$$

and

$$
\begin{array}{l} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {T} ^ {t} \frac {c _ {0} \varphi (\tau) d \tau}{(1 + \tau) ^ {m}}\right) ^ {2} d t\right) ^ {1 / 2} \\ = c _ {0} \left(\int_ {0} ^ {\infty} \left(\int_ {T} ^ {t} e ^ {- \varepsilon (t - \tau)} \frac {e ^ {- \varepsilon \tau} \varphi (\tau)}{(1 + \tau) ^ {m}} d \tau\right) ^ {2} d t\right) ^ {1 / 2} \\ \leqslant c _ {0} \left(\int_ {0} ^ {\infty} \left(\int_ {T} ^ {t} \frac {e ^ {- 2 \varepsilon (t - \tau)}}{(1 + \tau) ^ {2 m}} d \tau\right) \left(\int_ {T} ^ {t} e ^ {- 2 \varepsilon \tau} \varphi (\tau) ^ {2} d \tau\right) d t\right) ^ {1 / 2} \\ \leqslant c _ {0} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \varphi (t) ^ {2} d t\right) ^ {1 / 2} \left(\int_ {0} ^ {\infty} \int_ {T} ^ {t} \frac {e ^ {- 2 \varepsilon (t - \tau)}}{(1 + \tau) ^ {2 m}} d \tau d t\right) ^ {1 / 2} \\ = c _ {0} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \varphi (t) ^ {2} d t\right) ^ {1 / 2} \left(\int_ {T} ^ {\infty} \frac {1}{(1 + \tau) ^ {2 m}} \int_ {\tau} ^ {\infty} e ^ {- 2 \varepsilon (t - \tau)} d t d \tau\right) ^ {1 / 2} \\ = c _ {0} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \varphi (t) ^ {2} d t\right) ^ {1 / 2} \left(\int_ {T} ^ {\infty} \frac {d \tau}{(1 + \tau) ^ {2 m}}\right) ^ {1 / 2} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon s} d s\right) ^ {1 / 2} \\ = \frac {C _ {2 m} ^ {1 / 2} c _ {0}}{T ^ {m - 1 / 2} \sqrt {\varepsilon}} \left(\int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \varphi (t) ^ {2} d t\right) ^ {1 / 2}. \end{array}\tag{7.48}
$$

Gathering estimates (7.43)–(7.48), we deduce from (7.42) that

$$
\begin{array}{r l} & {\| \varphi (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)} \leqslant \bigg (1 + \frac {C C _ {0} C _ {W}}{\pmb {\varkappa} (\lambda_ {0} - \lambda) ^ {2}} \bigg) \frac {C A}{\sqrt {\varepsilon}} \Big (1 + \frac {c}{\alpha \varepsilon} + c _ {0} C _ {m} \Big)} \\ & {\qquad \times e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}))} + a \| \varphi (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)},} \end{array}\tag{7.49}
$$

where

$$
\begin{array}{l} a = \left(1 + \frac {C C _ {0} C _ {W}}{\varkappa (\lambda_ {0} - \lambda) ^ {2}}\right) \left[ \left(\sup _ {t \geqslant T} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {1} (t, \tau) e ^ {\varepsilon \tau} d \tau\right) ^ {1 / 2} \left(\sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} e ^ {\varepsilon \tau} K _ {1} (t, \tau) e ^ {- \varepsilon t} d t\right) ^ {1 / 2} \right. \\ \left. + \left(\sup _ {t \geqslant 0} \int_ {0} ^ {t} K _ {0} (t, \tau) d \tau\right) ^ {1 / 2} \left(\sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} K _ {0} (t, \tau) d t\right) ^ {1 / 2} + \frac {C _ {2 m} ^ {1 / 2} c _ {0}}{T ^ {m - 1 / 2} \sqrt {\varepsilon}} \right]. \end{array}
$$

Using Propositions 7.1$( \mathrm { c a s e } \gamma > 1 )$and 7.5, as well as assumptions (7.22) and (7.23), we see that$a { \leqslant } \frac { 1 } { 2 }$for$\chi$small enough and$T$satisfying (7.25). Then from (7.49) follows that

$$
\| \varphi (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)} \leqslant \left(1 + \frac {C C _ {0} C _ {W}}{\varkappa (\lambda_ {0} - \lambda) ^ {2}}\right) \frac {C A}{\sqrt {\varepsilon}} \left(1 + \frac {c}{\alpha \varepsilon} + c _ {0} C _ {m}\right) e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}))}.
$$

Step 3. Refined pointwise bounds. Let us use (7.21) a third time, now for$t { \geqslant } T$:

$$
\begin{array}{l} e ^ {- \varepsilon t} \varphi (t) \leqslant A e ^ {- \varepsilon t} + \int_ {0} ^ {t} \Big (\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | K ^ {0} (k, t - \tau) | e ^ {2 \pi \lambda (t - \tau) | k |} \Big) \varphi (\tau) e ^ {- \varepsilon \tau} d \tau \\ \qquad + \int_ {0} ^ {t} \bigg (K _ {0} (t, \tau) + \frac {c _ {0}}{(1 + \tau) ^ {m}} \bigg) \varphi (\tau) e ^ {- \varepsilon \tau} d \tau \\ \qquad + \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {1} (t, \tau) e ^ {\varepsilon \tau} \varphi (\tau) e ^ {- \varepsilon \tau} d \tau \\ \leqslant A e ^ {- \varepsilon t} + \bigg [ \bigg (\int_ {0} ^ {t} \Big (\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | K ^ {0} (k, t - \tau) | e ^ {2 \pi \lambda (t - \tau) | k |} \Big) ^ {2} d \tau \bigg) ^ {1 / 2} \\ \qquad + \bigg (\int_ {0} ^ {t} K _ {0} (t, \tau) ^ {2} d \tau \bigg) ^ {1 / 2} + \bigg (\int_ {0} ^ {\infty} \frac {c _ {0} ^ {2}}{(1 + \tau) ^ {2 m}} d \tau \bigg) ^ {1 / 2} \\ \qquad + \bigg (\int_ {0} ^ {t} e ^ {- 2 \varepsilon t} K _ {1} (t, \tau) ^ {2} e ^ {2 \varepsilon \tau} d \tau \bigg) ^ {1 / 2} \bigg ] \bigg (\int_ {0} ^ {\infty} \varphi (\tau) ^ {2} e ^ {- 2 \varepsilon \tau} d \tau \bigg) ^ {1 / 2}. \end{array}\tag{7.50}
$$

We note that, for any$k \in \mathbb { Z } _ { * } ^ { d }$

$$
\begin{array}{r l} (| K ^ {0} (k, t) | e ^ {2 \pi \lambda | k | t}) ^ {2} & \leqslant 1 6 \pi^ {4} | \widehat {W} (k) | ^ {2} | \tilde {f} ^ {0} (k t) | ^ {2} | k | ^ {4} t ^ {2} e ^ {4 \pi \lambda | k | t} \\ & \leqslant C C _ {0} ^ {2} | \widehat {W} (k) | ^ {2} e ^ {- 4 \pi (\lambda_ {0} - \lambda) | k | t} | k | ^ {4} t ^ {2} \\ & \leqslant \frac {C C _ {0} ^ {2}}{(\lambda_ {0} - \lambda) ^ {2}} | \widehat {W} (k) | ^ {2} e ^ {- 2 \pi (\lambda_ {0} - \lambda) | k | t} | k | ^ {2} \\ & \leqslant \frac {C C _ {0} ^ {2}}{(\lambda_ {0} - \lambda) ^ {2}} C _ {W} ^ {2} e ^ {- 2 \pi (\lambda_ {0} - \lambda) | k | t} \\ & \leqslant \frac {C C _ {0} ^ {2}}{(\lambda_ {0} - \lambda) ^ {2}} C _ {W} ^ {2} e ^ {- 2 \pi (\lambda_ {0} - \lambda) t}; \end{array}
$$

so

$$
\int_ {0} ^ {t} \Big (\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | K ^ {0} (k, t - \tau) | e ^ {2 \pi \lambda (t - \tau) | k |} \Big) ^ {2} d \tau \leqslant \frac {C C _ {0} ^ {2} C _ {W} ^ {2}}{(\lambda_ {0} - \lambda) ^ {3}}.
$$

Then the conclusion follows from (7.50), Corollary 7.4, conditions (7.25) and (7.23), and Step 2.□

Remark 7.9. Theorem 7.7 leads to enormous constants, and it is legitimate to ask about their sharpness, say with respect to the dependence in ε. We expect the constant to be roughly of the order of

$$
\sup _ {t} (e ^ {(c t) ^ {1 / \gamma}} e ^ {- \varepsilon t}) \simeq \exp (\varepsilon^ {- 1 / (\gamma - 1)}).
$$

Our bound is roughly like$\exp ( \varepsilon ^ { - ( 4 + 2 \gamma ) / ( \gamma - 1 ) } )$; this is worse, but displays the expected behavior as an exponential of an inverse power of$\varepsilon ,$with a power that diverges like $O ( ( 1 - \gamma ) ^ { - 1 } ) { \mathrm { ~ a s ~ } } \gamma \to 1$

Remark 7.10. Even in the case of an analytic interaction, a similar argument suggests constants that are at best like$( \log ( 1 / \varepsilon ) ) ^ { \log ( 1 / \varepsilon ) }$<sup>)</sup>, and this grows faster than any inverse power of$1 / \varepsilon$

To obtain sharper results, in 11 we shall later “break the norm” and work directly on the Fourier modes of, say, the spatial density. In this subsection we establish the estimates which will be used later; the reader who does not particularly care about the case$\gamma = 1$in Theorem 2.6 can skip them.

For any$\gamma \geqslant 1 , \alpha > 0 , k , l \in \mathbb { Z } _ { * } ^ { d }$and$0 \leqslant \tau \leqslant t .$, we define

$$
K _ {k, l} ^ {(\alpha), \gamma} (t, \tau) = \frac {(1 + \tau) d e ^ {- \alpha | l |} e ^ {- \alpha (t - \tau) | k - l | / t} e ^ {- \alpha | k (t - \tau) + l \tau |}}{1 + | k - l | ^ {\gamma}}.\tag{7.51}
$$

We start by exponential moment estimates.

Proposition 7.11. Let$\gamma \in [ 1 , \infty )$. For any$\alpha \in ( 0 , 1 )$and$k , l \in \mathbb { Z } _ { * } ^ { d }$, let$K _ { k , l } ^ { ( \alpha ) , \gamma }$be defined by (7.51). Then there is$\overline { { \alpha } } = \overline { { \alpha } } ( \gamma ) > 0$such that if$\alpha \leqslant \overline { { \alpha } }$and$\varepsilon \in \left( 0 , { \frac { 1 } { 4 } } \alpha \right)$then for any$t > 0$

$$
\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} e ^ {- \varepsilon t} \int_ {0} ^ {t} K _ {k, l} ^ {(\alpha), \gamma} (t, \tau) e ^ {\varepsilon \tau} d \tau \leqslant \frac {C (d , \gamma)}{\alpha^ {1 + d} \varepsilon^ {\gamma + 1} t ^ {\gamma}},\tag{7.52}
$$

$$
\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} e ^ {- \varepsilon t} \biggl (\int_ {0} ^ {t} K _ {k, l} ^ {(\alpha), \gamma} (t, \tau) ^ {2} e ^ {2 \varepsilon \tau} d \tau \biggr) ^ {1 / 2} \leqslant \frac {C (d , \gamma)}{\alpha^ {d} \varepsilon^ {\gamma + 1 / 2} t ^ {\gamma - 1 / 2}},\tag{7.53}
$$

$$
\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \sup _ {\tau \geqslant 0} e ^ {\varepsilon \tau} \int_ {\tau} ^ {\infty} K _ {k, l} ^ {(\alpha), \gamma} e ^ {- \varepsilon t} d t \leqslant \frac {C (d , \gamma)}{\alpha^ {2 + d} \varepsilon}.\tag{7.54}
$$

Proof. We first reduce to the case$d { = } 1$. Monotonicity cannot be used now, but we note that

$$
K _ {k, l} ^ {(\alpha), \gamma} (t, \tau) \leqslant \sum_ {j = 1} ^ {d} e ^ {- \alpha | l _ {1} |} e ^ {- \alpha | l _ {2} |} \dots e ^ {- \alpha | l _ {j - 1} |} K _ {k _ {j}, l _ {j}} ^ {(\alpha), \gamma} (t, \tau) e ^ {- \alpha | l _ {j + 1} |} \dots e ^ {- \alpha | l _ {d} |},
$$

where$K _ { k _ { j } , l _ { j } }$stands for a 1-dimensional kernel. Thus

$$
\begin{array}{l} \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {k, l} ^ {(\alpha), \gamma} (t, \tau) e ^ {\varepsilon \tau}   d \tau \\ \qquad \leqslant \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \bigg (\sum_ {m \in \mathbb {Z} ^ {d}} e ^ {- \alpha | m |} \bigg) ^ {d - 1} \sum_ {j = 1} ^ {d} \sum_ {l _ {j} \in \mathbb {Z}} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {k _ {j}, l _ {j}} ^ {(\alpha), \gamma} (t, \tau) e ^ {\varepsilon \tau}   d \tau \\ \qquad \leqslant \frac {C (d)}{\alpha^ {d - 1}} \sup _ {1 \leqslant j \leqslant d} \sup _ {k _ {j} \in \mathbb {Z}} \sum_ {l _ {j} \in \mathbb {Z}} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {k _ {j}, l _ {j}} ^ {(\alpha , \gamma)} (t, \tau) e ^ {\varepsilon \tau}   d \tau . \end{array}
$$

In other words, for (7.52) we may just consider the 1-dimensional case, provided we allow for an extra multiplicative constant$C ( d ) / \alpha ^ { d - 1 }$. A similar reasoning holds for (7.53) and (7.54). From now on we focus on the case$d { = } 1$

Without loss of generality we assume that$k > 0$, and only treat the worst case$l < 0$ (The other case$k , l > 0$is simpler and yields an exponential decay in time of the form $e ^ { - c \operatorname* { m i n } \{ \alpha , \varepsilon \} t } )$. For simplicity we also write$K _ { k , l } = K _ { k , l } ^ { ( \alpha ) , \gamma }$. An easy computation yields

$$
e ^ {- \varepsilon t} \int_ {0} ^ {t} K _ {k, l} (t, \tau) e ^ {\varepsilon \tau} d \tau \leqslant \frac {C e ^ {- \alpha | l |}}{1 + | k - l | ^ {\gamma}} \left(\frac {1}{\alpha | k - l |} + \frac {| k | t}{\alpha | k - l | ^ {2}} + \frac {1}{\alpha^ {2} | k - l | ^ {2}}\right) e ^ {- \varepsilon | l | t / | k - l |}.
$$

Then, for any$k \geqslant 1$, we have (crudely writing$\alpha ^ { 2 } { = } O ( \alpha ) )$)

$$
\sum_ {l = - \infty} ^ {- 1} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {k, l} (t, \tau) e ^ {\varepsilon \tau} d \tau \leqslant C \bigg (\sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)}}{\alpha^ {2} (k + l) ^ {1 + \gamma}} + \sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)}}{\alpha (k + l) ^ {2 + \gamma}} k t \bigg).\tag{7.55}
$$

For the first sum in the right-hand side of (7.55) we write

$$
\sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)}}{(k + l) ^ {1 + \gamma}} \leqslant \sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l}}{l ^ {1 + \gamma}} \left(\frac {\varepsilon l t}{k + l}\right) ^ {1 + \gamma} e ^ {- \varepsilon l t / (k + l)} \frac {1}{(\varepsilon t) ^ {1 + \gamma}} \leqslant \frac {C (\gamma)}{(\varepsilon t) ^ {1 + \gamma}}.\tag{7.56}
$$

For the second sum in the right-hand side of (7.55) we separate according to$1 \leqslant l \leqslant k$k or$l { \geqslant } k + 1$

$$
\begin{array}{l} \sum_ {l = 1} ^ {k} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)}}{(k + l) ^ {2 + \gamma}} k t \leqslant \sum_ {l = 1} ^ {k} \frac {e ^ {- \alpha l} e ^ {- \varepsilon t / (k + 1)}}{(k + 1) ^ {2 + \gamma}} k t \\ \qquad \leqslant \frac {C}{\alpha} e ^ {- \varepsilon t / (k + 1)} \left(\frac {\varepsilon t}{k + 1}\right) ^ {1 + \gamma} \frac {k}{k + 1} \frac {t}{(\varepsilon t) ^ {1 + \gamma}} \\ \qquad \leqslant \frac {C}{\alpha \varepsilon^ {1 + \gamma} t ^ {\gamma}} \end{array}\tag{7.57}
$$

and

$$
\sum_ {l = k + 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)}}{(k + l) ^ {2 + \gamma}} k t \leqslant C \sum_ {l = k + 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon t / 2}}{k ^ {2 + \gamma}} k t \leqslant \frac {C}{\alpha} \frac {e ^ {- \varepsilon t / 4}}{\varepsilon k ^ {1 + \gamma}} \leqslant \frac {C}{\alpha \varepsilon^ {1 + \gamma} t ^ {\gamma}}.\tag{7.58}
$$

The combination of (7.55)–(7.58) completes the proof of (7.52).

Now we turn to (7.53). The estimates are rather similar, since

$$
K _ {k, l} (t, \tau) ^ {2} \leqslant C (1 + t) K _ {k, l} (t, \tau)
$$

with$\gamma \mapsto 2 \gamma$and$\alpha \mapsto 2 \alpha$. So (7.55) should be replaced by

$$
\begin{array}{l} \sum_ {l \in \mathbb {Z}} e ^ {- \varepsilon t} \bigg (\int_ {0} ^ {t} K _ {k, l} (t, \tau) ^ {2} e ^ {2 \varepsilon \tau} d \tau \bigg) ^ {1 / 2} \\ \leqslant C \bigg (\sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)} (1 + t) ^ {1 / 2}}{\alpha (k + l) ^ {\gamma + 1 / 2}} + \sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)} (k t) ^ {1 / 2} (1 + t) ^ {1 / 2}}{\alpha^ {1 / 2} (k + l) ^ {1 + \gamma}} \bigg). \end{array}\tag{7.59}
$$

For the first sum we use (7.56) with γ replaced by$\begin{array} { r } { \gamma - \frac { 1 } { 2 } ; } \end{array}$: for$t \geqslant 1$

$$
(1 + t) ^ {1 / 2} \sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)}}{(k + l) ^ {1 + \gamma - 1 / 2}} \leqslant \frac {C (\gamma) t ^ {1 / 2}}{(\varepsilon t) ^ {\gamma + 1 / 2}} \leqslant \frac {C (\gamma)}{\varepsilon^ {\gamma + 1 / 2} t ^ {\gamma}}.\tag{7.60}
$$

For the second sum in the right-hand side of (7.59) we write

$$
\begin{array}{c} \sum_ {l = 1} ^ {k} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)} k ^ {1 / 2} t}{(k + l) ^ {1 + \gamma}} \leqslant C \sum_ {l = 1} ^ {\infty} e ^ {- \alpha l} e ^ {- \varepsilon t / (k + 1)} \left(\frac {\varepsilon t}{k + 1}\right) ^ {\gamma + 1 / 2} \frac {k ^ {1 / 2}}{(1 + k) ^ {1 / 2}} \frac {t}{(\varepsilon t) ^ {\gamma + 1 / 2}} \\ \leqslant \frac {C}{\alpha \varepsilon^ {\gamma + 1 / 2} t ^ {\gamma - 1 / 2}} \end{array}
$$

and

$$
\sum_ {l = k + 1} ^ {\infty} \frac {e ^ {- \alpha l} e ^ {- \varepsilon l t / (k + l)} k ^ {1 / 2} t}{(k + l) ^ {1 + \gamma}} \leqslant C \sum_ {l = 1} ^ {\infty} \frac {e ^ {- \alpha l}}{l ^ {\gamma + 1 / 2}} e ^ {- \varepsilon t / 2} t \leqslant C e ^ {- \varepsilon t / 4} \leqslant \frac {C}{(\varepsilon t) ^ {\gamma - 1 / 2} \varepsilon}.
$$

With this, (7.53) is readily obtained.

Finally we consider (7.54). As in Proposition 7.5, one easily shows that

$$
\sup _ {k \in \mathbb {Z} _ {*}} \sum_ {l \in \mathbb {Z} _ {*}} \sup _ {\tau \geqslant 0} e ^ {\varepsilon \tau} \int_ {2 \tau} ^ {\infty} K _ {k, l} (t, \tau) e ^ {- \varepsilon t} d t \leqslant \frac {C}{\varepsilon \alpha^ {2}} \sum_ {l \in \mathbb {Z} _ {*}} e ^ {- \alpha | l |} \leqslant \frac {C}{\varepsilon \alpha^ {3}}.
$$

Then one has

$$
e ^ {\varepsilon \tau} \int_ {\tau} ^ {2 \tau} e ^ {- \alpha | k (t - \tau) + l \tau |} e ^ {- \varepsilon t} d t \leqslant \frac {C}{\alpha^ {2} k} + \frac {C}{\alpha \varepsilon k} + \frac {C}{\alpha k} e ^ {- \varepsilon l \tau / k}.
$$

So the problem amounts to estimate

$$
\sum_ {l \in \mathbb {Z} _ {*}} \sup _ {\tau \geqslant 0} (1 + \tau) \frac {e ^ {- \alpha l} e ^ {- \varepsilon l \tau / k}}{\alpha k (k + l) ^ {\gamma}} \leqslant \sum_ {l \in \mathbb {Z} _ {*}} e ^ {- \alpha l} \bigg (\frac {1}{\alpha} + \frac {1}{\varepsilon l (k + l) ^ {\gamma}} e ^ {- \varepsilon l \tau / k} \frac {\varepsilon l \tau}{k} \bigg) \leqslant C \bigg (\frac {1}{\alpha^ {2}} + \frac {1}{\varepsilon} \bigg),
$$

and the proof is complete.

We conclude this section with a mode-by-mode analogue of Theorem 7.7.

Theorem 7.12. Let$f ^ { 0 } = f ^ { 0 } ( \boldsymbol { v } )$and$W { = } W ( x )$satisfy condition (L) from 2.2 with constants$C _ { 0 } , \lambda _ { 0 }$and$\varkappa ;$in particular$| \tilde { f } ^ { 0 } ( \eta ) | \leqslant C _ { 0 } e ^ { - 2 \pi \lambda _ { 0 } | \eta | }$|. Further let

$$
C _ {W} = \max \biggl \{\sum_ {k \in \mathbb {Z} _ {*} ^ {d}} | \widehat {W} (k) |, \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | k |   | \widehat {W} (k) | \biggr \}.
$$

Let$( A _ { k } ) _ { k \in  { \mathbb { Z } ^ { d } } _ { * } } , \mu \geqslant 0$and$\lambda \in ( 0 , \lambda ^ { * } ]$with$0 < \lambda ^ { * } < \lambda _ { 0 }$. Let$( \Phi ( k , t ) ) _ { k \in \mathbb { Z } ^ { d } , t \geq 0 }$be a continuous function of$t \geqslant 0$, valued in$\mathbb { C } ^ { \mathbb { Z } ^ { d } }$, such that for all$\scriptstyle t \geqslant 0 , \ \Phi ( 0 , t ) = 0$and for any $k \in \mathbb { Z } _ { * } ^ { d }$,

$$
\begin{array}{l} e ^ {2 \pi (\lambda t + \mu) | k |} \bigg | \Phi (k, t) - \int_ {0} ^ {t} K ^ {0} (k, t - \tau) \Phi (k, \tau)   d \tau \bigg | \\ \leqslant A _ {k} + \int_ {0} ^ {t} K _ {0} (t, \tau) e ^ {2 \pi (\lambda \tau + \mu) | k |} | \Phi (k, \tau) |   d \tau \\ \qquad + \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \bigg (c K _ {k, l} ^ {(\alpha), \gamma} (t, \tau) + \frac {c _ {l}}{(1 + \tau) ^ {m}} \bigg) e ^ {2 \pi (\lambda \tau + \mu) | k - l |} | \Phi (k - l, \tau) |   d \tau , \end{array}\tag{7.61}
$$

where$c > 0 , \ c _ { l } \geqslant 0 \ ( f o r \ l \in \mathbb Z _ { * } ^ { d } ) , \ m > 1 , \ \gamma \geqslant 1 , \ K _ { 0 } ( t , \tau )$is a non-negative kernel,$K _ { k , l } ^ { ( \alpha ) , \gamma }$is defined$b y$(7.51) and$\alpha { < } \overline { { \alpha } } ( \gamma )$is defined in Proposition 7.11. Then there are positive constants$C$and$\chi ,$, depending only on$\gamma , \lambda ^ { * } , \lambda _ { 0 } , \varkappa .$

$$
\bar {c} := \max \biggl \{\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} c _ {l}, \biggl (\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} c _ {l} ^ {2} \biggr) ^ {1 / 2} \biggr \},
$$

$C _ { W }$and m such that if

$$
\sup _ {t \geqslant 0} \int_ {0} ^ {t} K _ {0} (t, \tau) d \tau \leqslant \chi\tag{7.62}
$$

and

$$
\sup _ {t \geqslant 0} \left(\int_ {0} ^ {t} K _ {0} (t, \tau) ^ {2} d \tau\right) ^ {1 / 2} + \sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} K _ {0} (t, \tau) d t \leqslant 1,\tag{7.63}
$$

then for any$\varepsilon \in \left( 0 , { \frac { 1 } { 4 } } \alpha \right)$and for any t-0,

$$
\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | \Phi (k, t) | e ^ {2 \pi (\lambda t + \mu) | k |} \leqslant C \bar {A} \frac {(1 + \bar {c} ^ {2})}{\sqrt {\varepsilon}} e ^ {C \bar {c}} \left(1 + \frac {c}{\alpha^ {2} \varepsilon}\right) e ^ {C T} e ^ {C c (1 + T ^ {2}) / \alpha} e ^ {\varepsilon t},\tag{7.64}
$$

where$\bar { A } { : = } \operatorname* { s u p } _ { k } A _ { k }$and

$$
T = C \max \biggl \{\left(\frac {c ^ {2}}{\alpha^ {3 + 2 d} \varepsilon^ {\gamma + 2}}\right) ^ {1 / \gamma}, \left(\frac {c}{\alpha^ {d} \varepsilon^ {\gamma + 1 / 2}}\right) ^ {1 / (\gamma - 1 / 2)}, \left(\frac {\bar {c} ^ {2}}{\varepsilon}\right) ^ {1 / (2 m - 1)} \biggr \}.\tag{7.65}
$$

Proof. The proof is quite similar to the proof of Theorem$7 . 7 ,$so we shall only point out the diferences. As in the proof of Theorem 7.7, we start by crude pointwise bounds obtained by Gr¨onwall’s inequality; but this time on the quantity

$$
\varphi (t) = \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | \Phi (k, t) | e ^ {2 \pi (\lambda t + \mu) | k |}.
$$

Since

$$
\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} K _ {k, l} (t, \tau) = O \bigg (\frac {1 + \tau}{\alpha} \bigg),
$$

we find that

$$
\varphi (t) \leqslant 2 \bar {A} e ^ {C (C _ {0} C _ {W} t / (\lambda_ {0} - \lambda) + c (t + t ^ {2}) / \alpha + \bar {c} C _ {m})}.\tag{7.66}
$$

We next define$\Psi _ { k } , \ : \mathcal { K } _ { k } ^ { 0 }$and$R _ { k }$as in Step 2 of the proof of Theorem 7.7, and we deduce (7.39) and$( 7 . 4 0 )$. Let

$$
\varphi_ {k} (t) = | \Phi (k, t) | e ^ {2 \pi (\lambda t + \mu) | k |}.\tag{7.67}
$$

Then

$$
\| \varphi_ {k} (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)} \leqslant \| R _ {k} \| _ {L ^ {2} (d t)} \left(1 + \frac {\| \mathcal {K} _ {k} ^ {0} \| _ {L ^ {1} (d t)}}{\varkappa}\right) \leqslant \| R _ {k} \| _ {L ^ {2} (d t)} \left(1 + \frac {C C _ {W} C _ {0}}{\varkappa}\right);
$$

whence

$$
\begin{array}{r} \| \varphi_ {k} (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)} \leqslant \left(1 + \frac {C C _ {0} C _ {W}}{\pmb {\varkappa} (\lambda_ {0} - \lambda) ^ {2}}\right) \left[ \int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(A _ {k} + \int_ {0} ^ {t} K _ {0} (t, \tau) \varphi_ {k} (\tau) d \tau \right. \right. \\ \left. + \sum_ {l \in \mathbb {Z} ^ {d}} \int_ {0} ^ {t} \left(c K _ {k, l} (t, \tau) + \frac {c _ {l}}{(1 + \tau) ^ {m}}\right) \varphi_ {k - l} (\tau) d \tau\right) ^ {2} d t \bigg ] ^ {1 / 2}. \end{array}\tag{7.68}
$$

We separate this into various contributions as in the proof of Theorem 7.7. In particular, using (7.66) and

$$
\int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} K _ {k, l} d \tau = O \left(\frac {1 + t}{\alpha^ {2}}\right),
$$

we find that

$$
\begin{array}{l} \left[ \int_ {0} ^ {T} e ^ {- 2 \varepsilon t} \biggl (\int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} K _ {k, l} (t, \tau) \varphi_ {k - l} (\tau)   d \tau \biggr) ^ {2} d t \right] ^ {1 / 2} \\ \leqslant \Bigl (\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \sup _ {0 \leqslant t \leqslant T} \varphi_ {k} (t) \Bigr) \biggl (\int_ {0} ^ {T} e ^ {- 2 \varepsilon t} \biggl (\int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} K _ {k, l} (t, \tau)   d \tau \biggr) ^ {2} d t \biggr) ^ {1 / 2} \\ \leqslant C \bar {A} \frac {c}{\alpha^ {2} \varepsilon^ {3 / 2}} e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}) / \alpha)}. \end{array}\tag{7.69}
$$

Also,

$$
\begin{array}{r l} & {\left[ \int_ {T} ^ {\infty} e ^ {- 2 \varepsilon t} \biggl (\int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} K _ {k, l} (t, \tau) \varphi_ {k - l} (\tau) d \tau \biggr) ^ {2} d t \right] ^ {1 / 2}} \\ & {\qquad \leqslant \biggl (\sup _ {t \geqslant T} \int_ {0} ^ {t} e ^ {- \varepsilon t} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} K _ {k, l} (t, \tau) e ^ {\varepsilon \tau} d \tau \biggr) ^ {1 / 2}} \\ & {\qquad \times \biggl (\int_ {T} ^ {\infty} \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} K _ {k, l} (t, \tau) e ^ {- \varepsilon (t - \tau)} e ^ {- 2 \varepsilon \tau} \varphi_ {k - l} (\tau) ^ {2} d \tau d t \biggr) ^ {1 / 2},} \end{array}
$$

and the last term inside the parentheses is

$$
\begin{array}{l} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \int_ {0} ^ {\infty} \biggl (\int_ {\max \{\tau , T \}} ^ {\infty} K _ {k, l} (t, \tau) e ^ {- \varepsilon (t - \tau)} d t \biggr) e ^ {- 2 \varepsilon \tau} \varphi_ {k - l} (\tau) ^ {2} d \tau \\ \qquad \leqslant \biggl (\sum_ {l \in \mathbb {Z} ^ {d}} \sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} K _ {k, l} (t, \tau) e ^ {- \varepsilon (t - \tau)} d t \biggr) \biggl (\sup _ {l \in \mathbb {Z} _ {*} ^ {d}} \int_ {0} ^ {\infty} e ^ {- 2 \varepsilon \tau} \varphi_ {l} (\tau) ^ {2} d \tau \biggr). \end{array}
$$

The computation for$K _ { 0 }$is the same as in the proof of Theorem$7 . 7 ,$and the terms in$( 1 + \tau ) ^ { - m }$are handled in essentially the same way: simple computations yield

$$
\begin{array}{l} \left[ \int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {T} \frac {\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} c _ {l} \varphi_ {k - l} (\tau)}{(1 + \tau) ^ {m}} d \tau\right) ^ {2} d t \right] ^ {1 / 2} \\ \leqslant \left(\sup _ {0 \leqslant \tau \leqslant T} \sup _ {l \in \mathbb {Z} _ {*} ^ {d}} \varphi_ {l} (\tau)\right) \left[ \int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {0} ^ {T} \frac {\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} c _ {l}}{(1 + \tau) ^ {m}} d \tau\right) ^ {2} d t \right] ^ {1 / 2} \\ \leqslant \bar {c} \frac {C _ {m} \bar {A}}{\sqrt {\varepsilon}} e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}) / \alpha)} \end{array}\tag{7.70}
$$

and

$$
\begin{array}{l} \left[ \int_ {0} ^ {\infty} e ^ {- 2 \varepsilon t} \left(\int_ {T} ^ {t} \frac {\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} c _ {l} \varphi_ {k - l} (\tau)   d \tau}{(1 + \tau) ^ {m}}\right) ^ {2} d t \right] ^ {1 / 2} \\ \leqslant \left[ \sup _ {t \geqslant 0} \sup _ {l \in \mathbb {Z} _ {*} ^ {d}} \left(\int_ {T} ^ {t} e ^ {- 2 \varepsilon \tau} \varphi_ {l} (\tau) ^ {2}   d \tau\right) \left(\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} c _ {l}\right) ^ {2} \int_ {0} ^ {\infty} \int_ {T} ^ {t} \frac {e ^ {- 2 \varepsilon (t - \tau)}}{(1 + \tau) ^ {2 m}}   d \tau   d t \right] ^ {1 / 2} \\ \leqslant \bar {c} \left(\frac {C _ {2 m}}{\varepsilon T ^ {2 m - 1}}\right) ^ {1 / 2} \left(\sup _ {l \in \mathbb {Z} _ {*} ^ {d}} \int_ {0} ^ {\infty} e ^ {- 2 \varepsilon \tau} \varphi_ {l} (\tau) ^ {2}   d \tau\right) ^ {1 / 2}. \end{array}\tag{7.71}
$$

All in all, we end up with

$$
\begin{array}{l} \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \| \varphi_ {k} (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)} \\ \qquad \leqslant \bigg (1 + \frac {C C _ {0} C _ {W}}{\varkappa (\lambda_ {0} - \lambda) ^ {2}} \bigg) \frac {C A}{\sqrt {\varepsilon}} \Big (1 + \frac {c}{\alpha^ {2} \varepsilon} + \bar {c} C _ {m} \Big) e ^ {C (C _ {0} C _ {W} T / (\lambda_ {0} - \lambda) + c (T + T ^ {2}) / \alpha)} \\ \qquad + a \sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \| \varphi_ {k} (t) e ^ {- \varepsilon t} \| _ {L ^ {2} (d t)}, \end{array}\tag{7.72}
$$

where

$$
\begin{array}{l} a = \bigg (1 + \frac {C C _ {0} C _ {W}}{\varkappa (\lambda_ {0} - \lambda) ^ {2}} \bigg) \bigg [ c ^ {2} \bigg (\sup _ {t \geqslant T} \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \int_ {0} ^ {t} e ^ {- \varepsilon t} K _ {k, l} (t, \tau) e ^ {\varepsilon \tau}   d \tau \bigg) ^ {1 / 2} \\ \times \bigg (\sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} e ^ {\varepsilon \tau} K _ {k, l} (t, \tau) e ^ {- \varepsilon t}   d t \bigg) ^ {1 / 2} \\ + \bigg (\sup _ {t \geqslant 0} \int_ {0} ^ {t} K _ {0} (t, \tau)   d \tau \bigg) ^ {1 / 2} \bigg (\sup _ {\tau \geqslant 0} \int_ {\tau} ^ {\infty} K _ {0} (t, \tau)   d t \bigg) ^ {1 / 2} + \frac {C _ {2 m} ^ {1 / 2} \bar {c} _ {0}}{T ^ {m - 1 / 2} \sqrt {\varepsilon}} \bigg ]. \end{array}
$$

Applying Proposition 7.11, we see that$a \leqslant \frac 1 2$, as soon as T satisfies (7.65), and then we deduce from (7.72) a bound on$\begin{array} { r } { \operatorname* { s u p } _ { k \in \mathbb Z _ { * } ^ { d } } \| \varphi _ { k } ( t ) e ^ { - \varepsilon t } \| _ { L ^ { 2 } ( d t ) } } \end{array}$

Finally we conclude as in Step 3 of the proof of Theorem 7.7: from (7.61), we get

$$
\begin{array}{l} e ^ {- \varepsilon t} \varphi_ {k} (t) \leqslant A _ {k} e ^ {- \varepsilon t} + \Bigg [ \bigg (\int_ {0} ^ {t} \Big (\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} | K ^ {0} (k, t - \tau) | e ^ {2 \pi \lambda (t - \tau) | k |} \Big) ^ {2} d \tau \bigg) ^ {1 / 2} \\ \qquad + \bigg (\int_ {0} ^ {t} K _ {0} (t, \tau) ^ {2} d \tau \bigg) ^ {1 / 2} + \bar {c} \bigg (\int_ {0} ^ {\infty} \frac {d \tau}{(1 + \tau) ^ {2 m}} \bigg) ^ {1 / 2} \\ \qquad + c \sum_ {l \in \mathbb {Z} _ {*} ^ {d}} \bigg (\int_ {0} ^ {t} e ^ {- 2 \varepsilon t} K _ {k, l} (t, \tau) ^ {2} e ^ {2 \varepsilon \tau} d \tau \bigg) ^ {1 / 2} \Bigg ] \\ \qquad \times \bigg (\sup _ {k \in \mathbb {Z} _ {*} ^ {d}} \int_ {0} ^ {\infty} \varphi_ {k} (\tau) ^ {2} e ^ {- 2 \varepsilon \tau} d \tau \bigg) ^ {1 / 2}, \end{array}\tag{7.73}
$$

and the conclusion follows by a new application of Proposition 7.11.

## 8. Approximation schemes

Having defined a functional setting ( 4) and identified several mathematical/physica mechanisms ( 5–7), we are prepared to fight the Landau damping problem. For that we need an approximation scheme solving the non-linear Vlasov equation. The problem is not to prove the existence of solutions (this is much easier), but to devise the scheme in such a way that it leads to relevant estimates for our study.

The first idea which may come to mind is a classical Picard scheme for quasilinear equations:

$$
\partial_ {t} f ^ {n + 1} + v \cdot \nabla_ {x} f ^ {n + 1} + F [ f ^ {n} ] \cdot \nabla_ {v} f ^ {n + 1} = 0.\tag{8.1}
$$

This has two drawbacks: first,$f ^ { n + 1 }$evolves by the characteristics created by$F [ f ^ { n } ]$, and this will deteriorate the estimates in analytic regularity. Secondly, there is no hope to get a closed (or approximately closed) equation on the density associated with$f ^ { n + 1 }$. More promising, and more in the spirit of the linearized approach, would be a scheme like

$$
\partial_ {t} f ^ {n + 1} + v \cdot \nabla_ {x} f ^ {n + 1} + F [ f ^ {n + 1} ] \cdot \nabla_ {v} f ^ {n} = 0.\tag{8.2}
$$

(Physically,$f ^ { n + 1 }$forces$f ^ { n }$, and the question is whether the reaction will exhaust$f ^ { n + 1 }$ in large time.) But when we write (8.2) we are implicitly treating a higher-order term $( \nabla _ { v } f )$of the equation in a perturbative way; so this has no reason to converge.

To circumvent these dificulties, we shall use a Newton iteration: not only will this provide more flexibility in the regularity indices, but at the same time it will yield an extremely fast rate of convergence (something like$O ( \varepsilon ^ { 2 ^ { n } } ) )$which will be most welcome to absorb the large constants coming from Theorem 7.7 or 7.12.

## 8.1. The natural Newton scheme

Let us adapt the abstract Newton scheme to an abstract evolution equation in the form

$$
\frac {\partial f}{\partial t} = Q (f),
$$

around a stationary solution$f ^ { 0 } \ ( \mathrm { s o } \ Q ( f ^ { 0 } ) { = } 0 )$. Write the Cauchy problem with initial datum$f _ { i } \simeq f ^ { 0 }$in the form

$$
\Phi (f) := (\partial_ {t} f - Q (f), f (0, \cdot)) - (0, f _ {i}).
$$

Starting from$f ^ { 0 }$, the Newton iteration consists in solving inductively

$$
\Phi (f ^ {n - 1}) + \Phi^ {\prime} (f ^ {n - 1}) \cdot (f ^ {n} - f ^ {n - 1}) = 0 \quad \text { for } n \geqslant 1.
$$

More explicitly, writing$h ^ { n } { = } f ^ { n } { - } f ^ { n - 1 }$, we should solve

$$
\left\{ \begin{array}{l} \partial_ {t} h ^ {1} = Q ^ {\prime} (f ^ {0}) \cdot h ^ {1}, \\ h ^ {1} (0, \cdot) = f _ {i} - f ^ {0}, \end{array} \right.
$$

and, for all$n { \geqslant } 1$,

$$
\left\{ \begin{array}{l} \partial_ {t} h ^ {n + 1} = Q ^ {\prime} (f ^ {n}) \cdot h ^ {n + 1} - [ \partial_ {t} f ^ {n} - Q (f ^ {n}) ], \\ h ^ {n + 1} (0, \cdot) = 0. \end{array} \right.
$$

By induction, for$n { \geqslant } 1$, this is the same as

$$
\left\{ \begin{array}{l} \partial_ {t} h ^ {n + 1} = Q ^ {\prime} (f ^ {n}) \cdot h ^ {n + 1} + [ Q (f ^ {n - 1} + h ^ {n}) - Q (f ^ {n - 1}) - Q ^ {\prime} (f ^ {n - 1}) \cdot h ^ {n} ], \\ h ^ {n + 1} (0, \cdot) = 0. \end{array} \right.
$$

This is easily applied to the non-linear Vlasov equation, for which the non-linearity is quadratic. So we define the natural Newton scheme for the non-linear Vlasov equation as follows:

$$
f ^ {0} = f ^ {0} (v) \mathrm{isgiven(homogeneousstationarystate)}
$$

and

$$
f ^ {n} = f ^ {0} + h ^ {1} + \dots + h ^ {n},
$$

where

$$
\left\{ \begin{array}{l} \partial_ {t} h ^ {1} + v \cdot \nabla_ {x} h ^ {1} + F [ h ^ {1} ] \cdot \nabla_ {v} f ^ {0} = 0, \\ h ^ {1} (0, \cdot) = f _ {i} - f ^ {0}, \end{array} \right.\tag{8.3}
$$

and, for all$n { \geqslant } 1$

$$
\left\{ \begin{array}{l} \partial_ {t} h ^ {n + 1} + v \cdot \nabla_ {x} h ^ {n + 1} + F [ f ^ {n} ] \cdot \nabla_ {v} h ^ {n + 1} + F [ h ^ {n + 1} ] \cdot \nabla_ {v} f ^ {n} = - F [ h ^ {n} ] \cdot \nabla_ {v} h ^ {n}, \\ h ^ {n + 1} (0, \cdot) = 0. \end{array} \right.\tag{8.4}
$$

Here$F [ f ]$is the force field created by the particle distribution$f ,$namely

$$
F [ f ] (t, x) = - \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} \nabla W (x - y) f (t, y, w) d w d y.\tag{8.5}
$$

Note also that all the$\varrho ^ { n } { = } \int _ { \mathbb { R } ^ { d } } h ^ { n }$dv for$n { \geqslant } 1$have zero spatial average.

## 8.2. Battle plan

The treatment of (8.3) was performed in 4.12. Now the problem is to handle all equations appearing in (8.4). This is much more complicated, because for$n { \geqslant } 1$the background density$f ^ { n }$depends on t and$x ,$instead of just v. As a consequence,

(a) equation (8.4) cannot be considered as a perturbation of free transport, because of the presence of$\nabla _ { v } h ^ { n + 1 }$in the left-hand side;

(b) the reaction term$F [ h ^ { n + 1 } ] \cdot \nabla _ { v } f ^ { n }$no longer has the simple product structure (function of x) (function of v), so it becomes harder to get hands on the homogenization phenomenon;

(c) because of spatial inhomogeneities, echoes will appear; they are all the more dangerous that,$\nabla _ { v } f ^ { n }$is unbounded as$t \to \infty$, even in gliding regularity. (It grows like $O ( t )$, which is reminiscent of the observation made by Backus [4].)

The estimates in$\ S \ S 5 \mathrm { - } 7$have been designed precisely to overcome these problems; however we still have a few conceptual dificulties to solve before applying these tools.

Recall the discussion in 4.11: the natural strategy is to propagate the bound

$$
\sup _ {\tau \geqslant 0} \| f _ {\tau} \| _ {\mathcal {Z} _ {\tau} ^ {\lambda , \mu ; 1}} <   \infty\tag{8.6}
$$

along the scheme; this estimate contains in particular two crucial pieces of information:

a control of$\varrho _ { \tau } { = } \int _ { \mathbb { R } ^ { d } } f _ { \tau }$dv in${ \mathcal { F } } ^ { \lambda \tau + \mu }$norm,

a control of$\textstyle \langle f _ { \tau } \rangle = \int _ { \mathbb { T } ^ { d } } f _ { \tau }$dx in$\mathcal { C } ^ { \lambda ; 1 }$norm.

So the plan would be to try to inductively get estimates of each$h ^ { n }$in a norm like the one in (8.6), in such a way that$h ^ { n }$is extremely small as$n {  } \infty$, and allowing a slight deterioration of the indices λ and$\mu$as$n {  } { \infty }$. Let us try to see how this would work: assuming that

$$
\sup _ {\tau \geqslant 0} \| h _ {\tau} ^ {k} \| _ {\mathcal {Z} _ {\tau} ^ {\lambda_ {k}, \mu_ {k}; 1}} \leqslant \delta_ {k} \quad \text { for   all } 0 \leqslant k \leqslant n,
$$

we should try to bound$h _ { \tau } ^ { n + 1 }$. To “solve” (8.4), we apply the classical method of characteristics: as in$\ S 5$, we define$( X _ { \tau , t } ^ { n } , V _ { \tau , t } ^ { n } )$as the solution of

$$
\left\{ \begin{array}{l l} \frac {d}{d t} X _ {\tau , t} ^ {n} (x, v) = V _ {\tau , t} ^ {n} (x, v), & \frac {d}{d t} V _ {\tau , t} ^ {n} (x, v) = F [ f ^ {n} ] (t, X _ {\tau , t} ^ {n} (x, v)), \\ X _ {\tau , \tau} ^ {n} (x, v) = x, & V _ {\tau , \tau} ^ {n} (x, v) = v. \end{array} \right.
$$

Then (8.4) is equivalent to

$$
\frac {d}{d t} h ^ {n + 1} (t, X _ {0, t} ^ {n}, V _ {0, t} ^ {n} (x, v)) = \Sigma^ {n + 1} (t, X _ {0, \tau} ^ {n} (x, v), V _ {0, \tau} ^ {n} (x, v)),\tag{8.7}
$$

where

$$
\Sigma^ {n + 1} (t, x, v) = - F [ h ^ {n + 1} ] \cdot \nabla_ {v} f ^ {n} - F [ h ^ {n} ] \cdot \nabla_ {v} h ^ {n}.\tag{8.8}
$$

Integrating (8.7) in time and recalling that$h ^ { n + 1 } ( 0 , \cdot ) { = } 0$, we get

$$
h ^ {n + 1} (t, X _ {0, t} ^ {n} (x, v), V _ {0, t} ^ {n} (x, v)) = \int_ {0} ^ {t} \Sigma^ {n + 1} (\tau , X _ {0, \tau} ^ {n} (x, v), V _ {0, \tau} ^ {n} (x, v)) d \tau .
$$

Composing with$( X _ { t , 0 } ^ { n } , V _ { t , 0 } ^ { n } )$and using (5.2) yields

$$
h ^ {n + 1} (t, x, v) = \int_ {0} ^ {t} \Sigma^ {n + 1} (\tau , X _ {t, \tau} ^ {n} (x, v), V _ {t, \tau} ^ {n} (x, v)) d \tau .
$$

We rewrite this using the deflection map

$$
\Omega_ {t, \tau} ^ {n} (x, v) = (X _ {t, \tau} ^ {n}, V _ {t, \tau} ^ {n}) (x + v (t - \tau), v) = S _ {t, \tau} ^ {n} \circ S _ {\tau , t} ^ {0};
$$

then we finally obtain

$$
\begin{array}{l} h ^ {n + 1} (t, x, v) = \int_ {0} ^ {t} (\Sigma_ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) (x - v (t - \tau), v) d \tau \\ \qquad = - \int_ {0} ^ {t} [ (F [ h _ {\tau} ^ {n + 1} ] \circ \Omega_ {t, \tau} ^ {n}) \cdot ((\nabla_ {v} f _ {\tau} ^ {n}) \circ \Omega_ {t, \tau} ^ {n}) ] (x - v (t - \tau), v) d \tau \\ \qquad - \int_ {0} ^ {t} [ (F [ h _ {\tau} ^ {n} ] \circ \Omega_ {t, \tau} ^ {n}) \cdot ((\nabla_ {v} h _ {\tau} ^ {n}) \circ \Omega_ {t, \tau} ^ {n}) ] (x - v (t - \tau), v) d \tau . \end{array}\tag{8.9}
$$

Since the unknown$h ^ { n + 1 }$appears on both sides of (8.9), we need to get a self-consistent estimate. For this we have little choice but to integrate in v and get an integral equation on$\varrho [ h ^ { n + 1 } ] { = } \int _ { \mathbb { R } ^ { d } } h ^ { n }$dv, namely

$$
\begin{array}{c} \varrho [ h ^ {n + 1} ] (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} [ ((\varrho [ h _ {\tau} ^ {n + 1} ] * \nabla W) \circ \Omega_ {t, \tau} ^ {n}) \cdot G _ {\tau , t} ^ {n} ] \circ S _ {\tau - t} ^ {0} (x, v)   d v   d \tau \\ + (\text {terms from stage n}), \end{array}\tag{8.10}
$$

where$G _ { \tau , t } ^ { n } { = } \nabla _ { v } f _ { \tau } ^ { n } { \circ } \Omega _ { t , \tau } ^ { n }$. By induction hypothesis,$G _ { \tau , t } ^ { n }$is smooth with regularity indices roughly equal to$\lambda _ { n }$and$\mu _ { n } ;$so if we accept to lose just a bit more on the regularity we may hope to apply the long-term regularity extortion and decay estimates from$\ S 6$, and then time-response estimates of$\ S 7 ,$, and get the desired damping.

However, we are facing a major problem: composition of$\varrho [ h _ { \tau } ^ { n + 1 } ] * \nabla W$by$\Omega _ { t , \tau } ^ { n }$implies a loss of regularity in the right-hand side with respect to the left-hand side, which is of course unacceptable if one wants a closed estimate. The short-term regularity extortion from 6 remedies this, but the price to pay is that$G ^ { n }$should now be estimated at time$\tau ^ { \prime } { = } \tau { - } b t / ( 1 { + } b )$instead of$\tau _ { \mathrm { { i } } }$, and with index of gliding analytic regularity roughly equal to$\lambda _ { n } ( 1 + b )$rather than$\lambda _ { n }$. Now the catch is that the error induced by composition by$\Omega ^ { n }$depends on the whole distribution$f ^ { n }$, not just$h ^ { n }$. Thus, if the parameter b should control this error it should stay of order 1 as$n \to \infty .$, instead of converging to 0.

So it seems we are sentenced to lose a fixed amount of regularity (or rather of radius of convergence) in the transition from stage n to stage$n { + 1 } ;$this is reminiscent of the “Nash–Moser syndrom” [2]. The strategy introduced by Nash [70] to remedy such a problem (in his case arising in the construction of$C ^ { \infty }$isometric embeddings) consisted of combining a Newton scheme with regularization; his method was later developed by Moser [67] for the$C ^ { \infty }$KAM theorem (see [68, pp. 19–21] for some interesting historical comments). A clear and concise proof of the Nash–Moser implicit function theorem, together with its application to the$C ^ { \infty }$embedding problem, can be found in [83]. The Nash–Moser method is arguably the most powerful perturbation technique known to this day. However, despite significant efort, we were unable to set up any relevant regularization procedure (in gliding regularity, of course) which could be used in Nash– Moser style, because of three serious problems:

The convergence of the Nash–Moser scheme is no longer as fast as that of the “raw” Newton iteration; instead, it is determined by the regularity of the data, and the resulting rates would be unlikely to be fast enough to win over the gigantic constants coming from 7.

Analytic regularization in the v variable is extremely costly, especially if we wish to keep a good localization in velocity space, as the one appearing in Theorem 4.20 (iii), that is exponential integrability in$v ;$then the uncertainty principle basically forces us to pay${ \cal O } ( e ^ { C / \varepsilon ^ { 2 } } )$), where ε is the strength of the regularization.

Regularization comes with an increase of amplitude (there is as usual a tradeof between size and regularity); if we regularize before composition by$\Omega ^ { n }$, this will devastate the estimates, because the analytic regularity of f g depends not only on the regularity of f and$^ { g , }$but also on the amplitude of$g - \mathrm { I d }$

Fortunately, it turned out that a “raw” Newton scheme could be used; but this required us to give up the natural estimate (8.6), and replace it by the pair of estimates

$$
\left\{ \begin{array}{l} \sup _ {\tau \geqslant 0} \| \varrho_ {\tau} \| _ {\mathcal {F} ^ {\lambda \tau + \mu}} <   \infty , \\ \sup _ {0 \leqslant \tau \leqslant t} \| f _ {\tau} \circ \Omega_ {t, \tau} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\bar {\chi} (1 + b), \bar {\mu}; 1}} <   \infty . \end{array} \right.\tag{8.11}
$$

Here$b { = } b ( t )$takes the form constan$\cdot / ( 1 { + } t )$, and is kept fixed all along the scheme; moreover$\lambda$and$\mu$will be slightly larger than$\bar { \lambda }$and$\bar { \mu } ,$so that none of the two estimates in (8.11) implies the other one. Note carefully that there are now two times (t and τ) explicitly involved, so this is much more complex than (8.6). Let us explain why this strategy is nonetheless workable.

![](images/page_110_chart_0.jpg)

Figure 7. Indices of gliding regularity appearing throughout our Newton scheme, in the norm of$\varrho [ h _ { \tau } ]$and in the norm of$h _ { \tau } \circ \Omega _ { t , \tau }$, respectively, plotted as functions of t.

First, the density$\varrho ^ { n } { = } \textstyle \int _ { \mathbb { R } ^ { d } } f ^ { n }$dv determines the characteristics at stage$n ,$, and therefore the associated deflection$\Omega ^ { n }$. If$\varrho _ { \tau } ^ { n }$is bounded in$\mathcal { F } ^ { \lambda _ { n } \tau + \mu }$, then by Theorem 5.2 we can estimate$\Omega _ { t , \tau } ^ { n }$in$\mathcal { Z } _ { \tau ^ { \prime } } ^ { \lambda _ { n } ^ { \prime } , \mu _ { n } ^ { \prime } }$, as soon as (essentially)$\lambda _ { n } ^ { \prime } \tau ^ { \prime } + \mu _ { n } ^ { \prime } \leqslant \lambda _ { n } \tau + \mu _ { n }$and$\lambda _ { n } ^ { \prime } < \lambda _ { n } .$ and these bounds are uniform in t.

Of course, we cannot apply this theorem in the present context, because$\bar { \lambda } _ { n } ( 1 + b )$ is not bounded above by$\lambda _ { n }$. However, for large times t we may aford$\bar { \lambda } _ { n } ( 1 + b ( t ) ) < \lambda _ { n }$ while$\bar { \lambda } _ { n } ( 1 + b ) ( \tau - b t / ( 1 + b ) ) \leqslant \lambda _ { n } \tau$for all times; this will be suficient to repeat the arguments in 5, getting uniform estimates in a regularity which depends on t. (The constants are uniform in$t ;$but the index of regularity goes decreases with t.) We can also do this while preserving the other good properties from Theorem 5.2, namely exponential decay in τ, and vanishing near$\tau { = } t$

Figure$7$summarizes schematically the way we choose and estimate the gliding regularity indices.

Besides being uniform in$t ,$our bounds need to be uniform in n. For this we shall have to stratify all our estimates, that is decompose$\varrho [ f ^ { n } ] { = } \varrho [ h ^ { 1 } ] { + } . . . + \varrho [ h ^ { n } ]$], and consider separately the influence of each term in the equations for characteristics. This can work only if the scheme converges very fast.

Once we have estimates on$\Omega _ { t , \tau } ^ { n }$in a time-varying regularity, we can work with the kinetic equation to derive estimates on$h _ { \tau } ^ { n _ { 0 } } \mathrm { O } \Omega _ { t , \tau } ^ { n } ;$; and then on all$h _ { \tau } ^ { k } \circ \Omega _ { t , \tau } ^ { n }$, also in a norm of time-varying regularity. We can also estimate their spatial average, in a norm$\mathcal { C } ^ { \bar { \lambda } ( 1 + b ) ; 1 }$; due to the exponential convergence of the deflection map as$\tau {  } \infty$these estimates will turn out to be uniform in τ.

Next, we can use all this information, in conjunction with Theorem 6.5, to get an integral inequality on the norm of$\varrho [ h _ { \tau } ^ { n + 1 } ]$in${ \mathcal { F } } ^ { \lambda \tau + \mu }$, where λ and$\mu$are only slightly smaller than$\lambda _ { n }$and$\mu _ { n }$. Then we can go through the response estimates of$\ S 7 _ { \cdot }$, this gives us an arbitrarily small loss in the exponential decay rate, at the price of a huge constant which will eventually be wiped out by the fast convergence of the scheme. So we have an estimate on$\varrho [ h ^ { n + 1 } ]$, and we are in business to continue the iteration. (To ensure the propagation of the linear damping condition, or equivalently of the smallness of$K _ { 0 }$in Theorem 7.7, throughout the scheme, we shall have to stratify the estimates once more.)

## 9. Local-in-time iteration

Before working out the core of the proof of Theorem 2.6 in 10, we shall need a short-time estimate, which will act as an “initial regularity layer” for the Newton scheme. (This will give us room later to allow the regularity index to depend on$t . )$So we run the whole scheme once in this section, and another time in the next section.

Short-time estimates in the analytic class are not new for the non-linear Vlasov equation: see in particular the work of Benachour [8] on the Vlasov–Poisson equation. His arguments can probably be adapted for our purpose; also the Cauchy–Kovalevskaya method could certainly be applied. We shall provide here an alternative method, based on the analytic function spaces from 4, but not needing the apparatus from 5–7. Unlike the more sophisticated estimates which will be performed in 10, these ones are “almost” Eulerian (the only characteristics are those of free transport). The main tool is given by the following lemma.

Lemma 9.1. Let f be an analytic function,$\lambda ( t ) { = } \lambda { - } K t$and$\mu ( t ) { = } \mu { - } K t ;$let$T > 0$ be so small that$\lambda ( t ) , \mu ( t ) { > } 0$for 0tT. Then for any$\tau { \in } [ 0 , T ]$and any$p { \geqslant } 1$，

$$
\left. \frac {d ^ {+}}{d t} \right| _ {t = \tau} \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda (t), \mu (t); p}} \leqslant - \frac {K}{1 + \tau} \| \nabla f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda (\tau), \mu (\tau); p}},\tag{9.1}
$$

where$d ^ { + } / d t$stands for the upper right derivative.

Remark 9.2. Time-diferentiating Lebesgue integrability exponents is common practice in certain areas of analysis; see e.g. [33]. Time-diferentiation with respect to regularity exponents is less common; however, as pointed out to us by Strain, Lemma 9.1 is strongly reminiscent of a method recently used by Chemin [17] to derive local analytic regularity bounds for the Navier–Stokes equation. We expect that similar ideas can be applied to more general situations of Cauchy–Kovalevskaya type, especially for first-order equations, and maybe this has already been done.

Proof. For notational simplicity, let us assume$d { = } 1$. The left-hand side of (9.1) is

$$
\begin{array}{l} \sum_ {\stackrel {k \in \mathbb {Z} ^ {d}} {n \in \mathbb {N} _ {0} ^ {d}}} e ^ {2 \pi \mu (\tau) | k |} 2 \pi \dot {\mu} (\tau) | k | \frac {\lambda^ {n} (\tau)}{n !} \| (\nabla_ {v} + 2 i \pi k \tau) ^ {n} \hat {f} (k, v) \| _ {L ^ {p} (d v)} \\ \qquad + \sum_ {\stackrel {k \in \mathbb {Z} ^ {d}} {n \in N _ {0} ^ {d}}} e ^ {2 \pi \mu (\tau) | k |} \dot {\lambda} (\tau) \frac {\lambda^ {n - 1} (\tau)}{(n - 1) !} \| (\nabla_ {v} + 2 i \pi k \tau) ^ {n} \hat {f} (k, v) \| _ {L ^ {p} (d v)} \\ \qquad \leqslant - K \sum_ {\stackrel {k \in \mathbb {Z} ^ {d}} {n \in \mathbb {N} _ {0} ^ {d}}} e ^ {2 \pi \mu (\tau) | k |} 2 \pi | k | \frac {\lambda^ {n} (\tau)}{n !} \| (\nabla_ {v} + 2 i \pi k \tau) ^ {n} \hat {f} (k, v) \| _ {L ^ {p} (d v)} \\ \qquad - K \sum_ {\stackrel {k \in \mathbb {Z} ^ {d}} {n \in \mathbb {N} _ {0} ^ {d}}} e ^ {2 \pi \mu (\tau) | k |} \frac {\lambda^ {n} (\tau)}{n !} \| (\nabla_ {v} + 2 i \pi k \tau) ^ {n + 1} \hat {f} (k, v) \| _ {L ^ {p} (d v)} \\ \qquad \leqslant - K \sum_ {\stackrel {k \in \mathbb {Z} ^ {d}} {n \in \mathbb {N} _ {0} ^ {d}}} e ^ {2 \pi \mu (\tau) | k |} \frac {\lambda^ {n} (\tau)}{n !} \| (\nabla_ {v} + 2 i \pi k \tau) ^ {n} \widehat {\nabla_ {x}} f (k, v) \| _ {L ^ {p} (d v)} \\ \qquad + \frac {K \tau}{1 + \tau} \sum_ {\stackrel {k \in \mathbb {Z} ^ {d}} {n \in \mathbb {N} _ {0} ^ {d}}} e ^ {2 \pi \mu (\tau) | k |} \frac {\lambda^ {n} (\tau)}{n !} \| (\nabla_ {v} + 2 i \pi k \tau) ^ {n} \widehat {\nabla_ {\boldsymbol x}} f (k, v) \| _ {L ^ {p} (d v)} \\ \qquad - \frac {K}{1 + \tau} \sum_ {\stackrel {k \in \mathbb {Z} ^ {d}} {n \in \mathbb {N} _ {0} ^ {d}}} e ^ {2 \pi \mu (\tau) | k |} \frac {\lambda^ {n} (\tau)}{n !} \| (\nabla_ {v} + 2 i \pi k \tau) ^ {n} \wideetilde {\nabla_ {\boldsymbol v}} f (k, v) \| _ {L ^ {p} (d v)}, \end{array}
$$

where in the last step we used that

$$
\| (\nabla_ {v} + 2 i \pi k \tau) h \| \geqslant \frac {\| \nabla_ {v} h \| - \tau \| 2 i \pi k h \|}{1 + \tau}.
$$

The conclusion follows.

Now let us see how to propagate estimates through the Newton scheme described in 10. The first stage of the iteration$( h ^ { 1 }$in the notation of (8.3)) was considered in 4.12, so we only need to care about higher orders. For any$k \geqslant 1$, we solve

$$
\partial_ {t} h ^ {k + 1} + v \cdot \nabla_ {x} h ^ {k + 1} = \widetilde {\Sigma} ^ {k + 1},
$$

where

$$
\widetilde {\Sigma} ^ {k + 1} = - \big (F [ h ^ {k + 1} ] \cdot \nabla_ {v} f ^ {k} + F [ f ^ {k} ] \cdot \nabla_ {v} h ^ {k + 1} + F [ h ^ {k} ] \cdot \nabla_ {v} h ^ {k} \big)
$$

(note the diference with (8.7)–(8.8)). Recall that$f ^ { k } = f ^ { 0 } + h ^ { 1 } + . . . + h ^ { k }$. We define

$$
\lambda_ {k} (t) = \lambda_ {k} - 2 K t \quad \text { and } \quad \mu_ {k} (t) = \mu_ {k} - K t,
$$

where$( \lambda _ { k } ) _ { k = 1 } ^ { \infty }$and$( \mu _ { k } ) _ { k = } ^ { \infty }$are decreasing sequences of positive numbers.

We assume inductively that at stage n of the iteration, we have constructed$( \lambda _ { k } ) _ { k = 1 } ^ { n }$, $( \mu _ { k } ) _ { k = 1 } ^ { n }$and$( \delta _ { k } ) _ { k = 1 } ^ { n }$such that

$$
\sup _ {0 \leqslant t \leqslant T} \| h ^ {k} (t, \cdot) \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {k} (t), \mu_ {k} (t); 1}} \leqslant \delta_ {k} \quad \text { for   all } 1 \leqslant k \leqslant n
$$

for some fixed$T > 0$. The issue is to construct$\lambda _ { n + 1 } , \mu _ { n + 1 }$and$\delta _ { n + 1 }$so that the induction hypothesis is satisfied at stage$n { \mathrel { + { 1 } } }$

At$t { = } 0 , h ^ { n + 1 } { = } 0$. Then we estimate the time-derivative of$\| h ^ { n + 1 } \| _ { \mathcal { Z } _ { \star } ^ { \lambda _ { n + 1 } ( t ) , \mu _ { n + 1 } ( t ) ; 1 } }$ Let us first pretend that the regularity indices$\lambda _ { n + 1 }$and$\mu _ { n + 1 }$do not depend on$t ;$then

$$
h ^ {n + 1} (t) = \int_ {0} ^ {t} \widetilde {\Sigma} ^ {n + 1} \circ S _ {- (t - \tau)} ^ {0} d \tau ,
$$

so, by Proposition 4.19,

$$
\begin{array}{l} \left\| h ^ {n + 1} \right\| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}} \leqslant \int_ {0} ^ {t} \left\| \widetilde {\Sigma} _ {\tau} ^ {n + 1} \circ S _ {- (t - \tau)} ^ {0} \right\| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}} d \tau \\ \leqslant \int_ {0} ^ {t} \left\| \widetilde {\Sigma} _ {\tau} ^ {n + 1} \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}} d \tau , \end{array}
$$

and thus

$$
\frac {d ^ {+}}{d t} \| h ^ {n + 1} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}} \leqslant \left\| \widetilde {\Sigma} _ {t} ^ {n + 1} \right\| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}}.
$$

Finally, according to Lemma 9.1, to this estimate we should add a negative multiple of the norm of$\nabla h ^ { n + 1 }$to take into account the time-dependence of$\lambda _ { n + 1 }$and$\mu _ { n + 1 }$

All in all, after application of Proposition 4.24, we get

$$
\begin{array}{r l} & {\frac {d ^ {+}}{d t} \| h ^ {n + 1} (t, \cdot) \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1} (t), \mu_ {n + 1} (t); 1}} \leqslant \| F [ h _ {t} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n + 1} t + \mu_ {n + 1}}} \| \nabla_ {v} f _ {t} ^ {n} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}}} \\ & {\qquad + \| F [ f _ {t} ^ {n} ] \| _ {\mathcal {F} ^ {\lambda_ {n + 1} t + \mu_ {n + 1}}} \| \nabla_ {v} h _ {t} ^ {n + 1} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}}} \\ & {\qquad + \| F [ h _ {t} ^ {n} ] \| _ {\mathcal {F} ^ {\lambda_ {n + 1} t + \mu_ {n + 1}}} \| \nabla_ {v} h _ {t} ^ {n} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}}} \\ & {\qquad - K \| \nabla_ {x} h _ {t} ^ {n + 1} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}} - K \| \nabla_ {v} h _ {t} ^ {n + 1} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}},} \end{array}
$$

where$K > 0 ,$, t is suficiently small, and all exponents$\lambda _ { n + 1 }$and$\mu _ { n + 1 }$in the right-hand side actually depend on t.

From Proposition 4.15 (iv) we easily get$\| F [ h ] \| _ { \mathcal { F } ^ { \lambda t + \mu } } \leqslant C \| \nabla h \| _ { \mathcal { Z } _ { t } ^ { \lambda , \mu ; 1 } }$. Moreover, by Proposition 4.10,

$$
\| \nabla f ^ {n} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}} \leqslant \sum_ {k = 1} ^ {n} \| \nabla h ^ {k} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1}, \mu_ {n + 1}; 1}} \leqslant C \sum_ {k = 1} ^ {n} \frac {\| h ^ {k} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {k + 1} , \mu_ {k + 1} ; 1}}}{\min \{\lambda_ {k} - \lambda_ {n + 1} , \mu_ {k} - \mu_ {n + 1} \}}.
$$

We end up with the bound

$$
\begin{array}{l} \frac {d ^ {+}}{d t} \| h ^ {n + 1} (t, \cdot) \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1} (t), \mu_ {n + 1} (t); 1}} \\ \qquad \leqslant \bigg (C \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\min \{\lambda_ {k} - \lambda_ {n + 1} , \mu_ {k} - \mu_ {n + 1} \}} - K \bigg) \| \nabla h ^ {n + 1} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {n + 1} (t), \mu_ {n + 1} (t); 1}} \\ \qquad + \frac {\delta_ {n} ^ {2}}{\min \{\lambda_ {n} - \lambda_ {n + 1} , \mu_ {n} - \mu_ {n + 1} \}}. \end{array}
$$

We conclude that if

$$
\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\min \left\{\lambda_ {k} - \lambda_ {n + 1} , \mu_ {k} - \mu_ {n + 1} \right\}} \leqslant \frac {K}{C},\tag{9.2}
$$

then we may choose

$$
\delta_ {n + 1} = \frac {\delta_ {n} ^ {2}}{\min \{\lambda_ {n} - \lambda_ {n + 1} , \mu_ {n} - \mu_ {n + 1} \}}.\tag{9.3}
$$

This is our first encounter with the principle of “stratification” of errors, which will be crucial in the next section: to control the error at stage$n { \mathrel { + { 1 } } }$, we use not only the smallness of the error from stage$n ,$but also an information about all previous errors; namely the fact that the convergence of the size of the error is much faster than the convergence of the regularity loss. Let us see how this works. We choose$\lambda _ { k } - \lambda _ { k + 1 } = \mu _ { k } - \mu _ { k + 1 } = \Lambda / k ^ { 2 }$, where $\Lambda { > } 0$is arbitrarily small. Then for k$n , \lambda _ { k } - \lambda _ { n + 1 } \geqslant \Lambda / k ^ { 2 }$, and therefore$\delta _ { n + 1 } \leqslant \delta _ { n } ^ { 2 } n ^ { 2 } / \Lambda$ The problem is to check that

$$
\sum_ {n = 1} ^ {\infty} n ^ {2} \delta_ {n} <   \infty .\tag{9.4}
$$

Indeed, then we can choose K large enough for (9.2) to be satisfied, and then$T$small enough that, say,$\lambda ^ { * } - 2 K T \geqslant \lambda ^ { \sharp }$and$\mu ^ { * } - K T \geqslant \mu ^ { \sharp }$, where$\lambda ^ { \sharp } < \lambda ^ { * }$and$\mu ^ { \sharp } < \mu ^ { * }$have been fixed in advance.

If$\delta _ { 1 } = \delta$, the general term in the series of (9.4) is

$$
n ^ {2} \frac {\delta^ {2 ^ {n}}}{\Lambda^ {n}} (2 ^ {2}) ^ {2 ^ {n - 1}} (3 ^ {2}) ^ {2 ^ {n - 2}} (4 ^ {2}) ^ {2 ^ {n - 2}} \dots ((n - 1) ^ {2}) ^ {2} n ^ {2}.
$$

To prove the convergence for$\delta$small enough, we assume by induction that$\delta _ { n } \leqslant z ^ { a ^ { n } }$, where a is fixed in the interval (1, 2) (say a=1.5); and we claim that this condition propagates if$z > 0$is small enough. Indeed,

$$
\delta_ {n + 1} \leqslant \frac {z ^ {2 a ^ {n}}}{\Lambda} n ^ {2} \leqslant z ^ {a ^ {n + 1}} \frac {z ^ {(2 - a) a ^ {n}} n ^ {2}}{\Lambda},
$$

and this is bounded above by$z ^ { a ^ { n + 1 } }$if z is so small that

$$
z ^ {(2 - a) a ^ {n}} \leqslant \frac {\Lambda}{n ^ {2}} \quad \mathrm{forall} n \in \mathbb {N}.
$$

This concludes the iteration argument. Note that the convergence is still extremely fast—like$O ( z ^ { a ^ { n } } )$for any$a < 2$. (Of course, when a approaches 2, the constants become huge, and the restriction on the size of the perturbation becomes more and more stringent.)

Remark 9.3. The method used in this section can certainly be applied to more general situations of Cauchy–Kovalevskaya type. Actually, as pointed out to us by Bony and G´erard, the use of a regularity index which decays linearly in time, combined with a Newton iteration, was used by Nirenberg [73] to prove an abstract Cauchy–Kovalevskaya theorem. Nirenberg uses a time-integral formulation, so there is nothing in [73] comparable to Lemma$9 . 1 .$, and the details of the proof of convergence difer from ours; but the general strategy is similar. Nirenberg’s proof was later simplified by Nishida [74] with a clever fixed-point argument; in the present section anyway, our final goal is to provide short-term estimates for the successive corrections arising from the Newton scheme.

## 10. Global in time iteration

Now let us implement the scheme described in$\ S 8$, with some technical modifications. If $f$is a given kinetic distribution, we write

$$
\varrho [ f ] = \int_ {\mathbb {R} ^ {d}} f d v \quad \mathrm{and} \quad F [ f ] = - \nabla W * \varrho [ f ].
$$

We let

$$
f ^ {n} = f ^ {0} + h ^ {1} + \dots + h ^ {n},\tag{10.1}
$$

where the successive corrections$h ^ { k }$are defined by the natural Newton scheme introduced in$\ S 8 .$. As in$\ S 5 ,$, we define$\Omega _ { t , \tau } ^ { k }$as the deflection from time t to time τ, generated by the force field$F [ f ^ { k } ] = - \nabla W * \varrho [ f ^ { k } ]$. (Note that$\Omega ^ { 0 } { = } \mathrm { I d } . )$)

## 10.1. The statement of the induction

We shall fix$\bar { p } { \in } [ 1 , \infty ]$and make the following assumptions:

Regularity of the background: there are$\lambda { > } 0$and$C _ { 0 } > 0$such that

$$
\| f ^ {0} \| _ {\mathcal {C} ^ {\lambda ; p}} \leqslant C _ {0} \quad \text { for   all } p \in [ 1, \bar {p} ].
$$

Linear damping condition: The stability condition (L) from 2.2 holds with parameters$C _ { 0 } , \lambda$(the same as above) and$\varkappa > 0$

Regularity of the interaction: There are$\gamma > 1$and$C _ { F } > 0$such that for any$\nu > 0$2

$$
\left\| \nabla W * \varrho \right\| _ {\mathcal {F} ^ {\nu , \gamma}} \leqslant C _ {F} \| \varrho \| _ {\dot {\mathcal {F}} ^ {\nu}}.\tag{10.2}
$$

Initial layer of regularity (coming from 9): having chosen$\lambda ^ { \sharp } < \lambda$and$\mu ^ { \sharp } < \mu$, we assume that for all$p \in [ 1 , \bar { p } ]$

$$
\sup _ {0 \leqslant t \leqslant T} (\| h _ {t} ^ {k} \| _ {\mathcal {Z} ^ {\lambda^ {\sharp}, \mu^ {\sharp}; p}} + \| \varrho [ h _ {t} ^ {k} ] \| _ {\mathcal {F} ^ {\mu^ {\sharp}}}) \leqslant \zeta_ {k} \quad \text { for   all } k \geqslant 1,\tag{10.3}
$$

where$T$is some positive time, and$\zeta _ { k }$converges to zero extremely fast:$\zeta _ { k } { = } O ( z _ { I } ^ { a _ { I } ^ { k } } )$, $z _ { I } \leqslant C \delta < 1 , \ 1 < a _ { I } < 2 \ ( a _ { I }$chosen in advance, arbitrarily close to 2).

Smallness of the solution of the linearized equation (coming from 4.12): given $\lambda _ { 1 } < \lambda ^ { \sharp }$and$\mu _ { 1 } < \mu ^ { \sharp }$, we assume that

$$
\left\{ \begin{array}{l l} \sup _ {\tau \geqslant 0} \| \varrho [ h _ {\tau} ^ {1} ] \| _ {\mathcal {F} ^ {\lambda_ {1} \tau + \mu_ {1}}} \leqslant \delta_ {1}, \\ \sup _ {0 \leqslant \tau \leqslant t} \| h _ {\tau} ^ {1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {1} (1 + b), \mu_ {1}; p}} \leqslant \delta_ {1} & \text { for all } p \in [ 1, \bar {p} ], \end{array} \right.\tag{10.4}
$$

where$\delta _ { 1 } \leqslant C \delta$

Then we prove the following induction for any$n { \geqslant } 1$,

$$
\left\{ \begin{array}{l l} \sup _ {\tau \geqslant 0} \| \varrho [ h _ {\tau} ^ {k} ] \| _ {\mathcal {F} ^ {\lambda_ {k} \tau + \mu_ {k}}} \leqslant \delta_ {k}, \\ \sup _ {0 \leqslant \tau \leqslant t} \| h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; p}} \leqslant \delta_ {k}, \end{array} \right. \quad \text { for   all } k \in \{1,..., n \} \text { and } p \in [ 1, \bar {p} ],\tag{10.5}
$$

where

$( \delta _ { k } ) _ { k = 1 } ^ { \infty }$is a sequence satisfying$0 { < } C _ { F } \zeta _ { k } { \leqslant } \delta _ { k }$, and$\delta _ { k } { = } O ( z ^ { a ^ { k } } ) , z { < } z _ { I } , 1 { < } a { < } a _ { I }$(a arbitrarily close to$a _ { I } )$;

$\left( \lambda _ { k } , \mu _ { k } \right)$are decreasing to$\left( \lambda _ { \infty } , \mu _ { \infty } \right)$, where$\left( \lambda _ { \infty } , \mu _ { \infty } \right)$are arbitrarily close to $( \lambda _ { 1 } , \mu _ { 1 } )$; in particular we impose

$$
\lambda^ {\sharp} - \lambda_ {\infty} \leqslant \min \left\{1, \frac {1}{2} \lambda_ {\infty} \right\} \quad \text { and } \quad \mu^ {\sharp} - \mu_ {\infty} \leqslant \min \left\{1, \frac {1}{2} \mu_ {\infty} \right\};\tag{10.6}
$$

●$T$is some small positive time in (10.3); we impose

$$
\lambda^ {\#} T \leqslant \frac {1}{2} (\mu^ {\sharp} - \mu_ {1});\tag{10.7}
$$

$b { = } b ( t ) { = } \frac { B } { 1 { + } t } ,$where$B \in ( 0 , T )$is a (small) constant.

## 10.2. Preparatory remarks

As announced in (10.5), we shall propagate the following “primary” controls on the density and distribution:

$$
\sup _ {\tau \geqslant 0} \| \varrho [ h _ {\tau} ^ {k} ] \| _ {\mathcal {F} ^ {\lambda_ {k} \tau + \mu_ {k}}} \leqslant \delta_ {k} \quad \text { for   all } k \in \{1,..., n \}\tag{\(\left(\mathbf{E}_{\varrho}^{\mathbf{n}}\right)\}
$$

and

$$
\sup _ {0 \leqslant \tau \leqslant t} \| h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; p}} \leqslant \delta_ {k} \quad \text { for   all } k \in \{1,..., n \} \text { and } p \in [ 1, \bar {p} ].\tag{\( \left(\mathbf{E}_{\mathbf{h}}^{\mathbf{n}}\right) \}
$$

Estimate$( \mathbf { E } _ { \varrho } ^ { \mathbf { n } } )$obviously implies, via (10.2), up to a multiplicative constant,

$$
\sup _ {\tau \geqslant 0} \| F [ h _ {\tau} ^ {k} ] \| _ {\mathcal {F} ^ {\lambda_ {k} \tau + \mu_ {k}, \gamma}} \leqslant \delta_ {k} \quad \text { for   all } k \in \{1,..., n \}.\tag{\((\widetilde{\mathbf{E}}_{\varrho}^{\mathbf{n}})\}
$$

Before we can go from there to stage$n { \mathrel { + { 1 } } }$, we need an additional set of estimates on the deflection maps$( \Omega ^ { k } ) _ { k = 1 } ^ { n } ,$, which will be used to

(1) update the control on$\Omega _ { t , \tau } ^ { k } - \mathrm { I d } ;$

(2) establish the needed control along the characteristics for the background

$$
(\nabla_ {v} f _ {\tau} ^ {n}) \circ \Omega_ {t, \tau} ^ {n}
$$

(same index for the distribution and the deflection);

(3) update some technical controls allowing us to exchange (asymptotically) gradient and composition by$\Omega _ { t , \tau } ^ { k }$; this will be crucial to handle the contribution of the zero mode of the background after composition by characteristics.

This set of deflection estimates falls into three categories. The first group expresses the closeness of$\Omega ^ { k }$to Id:

$$
\left\{ \begin{array}{l l} \sup _ {0 \leqslant \tau \leqslant t} \| \Omega^ {k} X _ {t, \tau} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} ^ {*} (1 + b), (\mu_ {k} ^ {*}, \gamma)}} \leqslant 2 \mathcal {R} _ {2} ^ {k} (\tau , t), \\ \sup _ {0 \leqslant \tau \leqslant t} \| \Omega^ {k} V _ {t, \tau} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} ^ {*} (1 + b), (\mu_ {k} ^ {*}, \gamma)}} \leqslant \mathcal {R} _ {1} ^ {k} (\tau , t), & \text { for   all } k \in \{1,..., n \}, \end{array} \right.\tag{\(\left(\mathbf{E}_{\Omega}^{\mathbf{n}}\right)\}
$$

with$\lambda _ { k } > \lambda _ { k } ^ { * } > \lambda _ { k + 1 } , \mu _ { k } > \mu _ { k } ^ { * } > \mu _ { k + 1 }$and

$$
\left\{ \begin{array}{l} \mathcal {R} _ {1} ^ {k} (\tau , t) = \bigg (\sum_ {j = 1} ^ {k} \frac {\delta_ {j} e ^ {- 2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*}) \tau}}{2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})} \bigg) \min \{t - \tau , 1 \} \\ \mathcal {R} _ {2} ^ {k} (\tau , t) = \bigg (\sum_ {j = 1} ^ {k} \frac {\delta_ {j} e ^ {- 2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*}) \tau}}{(2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})) ^ {2}} \bigg) \min \Big \{\frac {(t - \tau) ^ {2}}{2}, 1 \Big \}. \end{array} \right.\tag{10.8}
$$

The second group of estimates expresses the fact that$\Omega ^ { n } - \Omega ^ { k }$is very small when k is large:

$$
\left\{ \begin{array}{l} \sup _ {0 \leqslant \tau \leqslant t} \| \Omega^ {n} X _ {t, \tau} - \Omega^ {k} X _ {t, \tau} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), (\mu_ {n} ^ {*}, \gamma)}} \leqslant 2 \mathcal {R} _ {2} ^ {k, n} (\tau , t), \\ \sup _ {0 \leqslant \tau \leqslant t} \| \Omega^ {n} V _ {t, \tau} - \Omega^ {k} V _ {t, \tau} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), (\mu_ {n} ^ {*}, \gamma)}} \leqslant \mathcal {R} _ {1} ^ {k, n} (\tau , t) + \mathcal {R} _ {2} ^ {k, n} (\tau , t), \\ \sup _ {0 \leqslant \tau \leqslant t} \| (\Omega_ {t, \tau} ^ {k}) ^ {- 1} \circ \Omega_ {t, \tau} ^ {n} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 4 (\mathcal {R} _ {1} ^ {k, n} (\tau , t) + \mathcal {R} _ {2} ^ {k, n} (\tau , t)), \end{array} \right.\tag{\((\widetilde{\mathbf{E}}_{\Omega}^{\mathbf{n}})\}
$$

with

$$
\left\{ \begin{array}{l} \mathcal {R} _ {1} ^ {k, n} (\tau , t) = \bigg (\sum_ {j = k + 1} ^ {n} \frac {\delta_ {j} e ^ {- 2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*}) \tau}}{2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})} \bigg) \min \{t - \tau , 1 \} \\ \mathcal {R} _ {2} ^ {k, n} (\tau , t) = \bigg (\sum_ {j = k + 1} ^ {n} \frac {\delta_ {j} e ^ {- 2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*}) \tau}}{(2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})) ^ {2}} \bigg) \min \Bigl \{\frac {(t - \tau) ^ {2}}{2}, 1 \Bigr \}. \end{array} \right.\tag{10.9}
$$

(Choosing$k { = } 0$brings us back to the previous estimates$( { \bf E } _ { \Omega } ^ { \bf n } ) . )$

The last group of estimates expresses the fact that the diferential of the deflection map is uniformly close to the identity (in a way which is more precise than what would follow from the first group of estimates):

$$
\left\{ \begin{array}{l} \sup _ {0 \leqslant \tau \leqslant t} \| \nabla \Omega^ {k} X _ {t, \tau} - (I, 0) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} ^ {*} (1 + b), \mu_ {k} ^ {*}}} \leqslant 2 \mathcal {R} _ {2} ^ {k} (\tau , t), \\ \sup _ {0 \leqslant \tau \leqslant t} \| \nabla \Omega^ {k} V _ {t, \tau} - (0, I) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} ^ {*} (1 + b), \mu_ {k} ^ {*}}} \leqslant \mathcal {R} _ {1} ^ {k} (\tau , t) + \mathcal {R} _ {2} ^ {k} (\tau , t), \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {for all k\in\{1,\ldots,n\}}, \end{array} \right.\tag{\((\mathbf{E}_{\nabla \Omega}^{\mathbf{n}})\}
$$

where${ \nabla } = ( \nabla _ { x } , \nabla _ { v } )$, and I is the identity matrix.

An important property of the functions$\mathcal { R } _ { 1 } ^ { k , n } ( \tau , t )$and$\mathcal { R } _ { 2 } ^ { k , n } ( \tau , t )$is their fast decay as$\tau {  } \infty$and as$k \to \infty$, uniformly in$n \geqslant k ;$this is due to the fast convergence of the sequence$( \delta _ { k } ) _ { k = 1 } ^ { \infty }$. Eventually, i$\cdot _ { r \in \mathbb { N } }$is given, we shall have

$$
\mathcal {R} _ {1} ^ {k, n} (\tau , t) \leqslant \omega_ {k, n} ^ {r, 1} (\tau , t) \text { and } \mathcal {R} _ {2} ^ {k, n} (\tau , t) \leqslant \omega_ {k, n} ^ {r, 2} (\tau , t) \quad \text { for   all } r \geqslant 1,\tag{10.10}
$$

with

$$
\omega_ {k, n} ^ {r, 1} (\tau , t) := C _ {\omega} ^ {r} \left(\sum_ {j = k + 1} ^ {n} \frac {\delta_ {j}}{(2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})) ^ {1 + r}}\right) \frac {\min \{t - \tau , 1 \}}{(1 + \tau) ^ {r}}
$$

and

$$
\omega_ {k, n} ^ {r, 2} (\tau , t) := C _ {\omega} ^ {r} \bigg (\sum_ {j = k + 1} ^ {n} \frac {\delta_ {j}}{(2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})) ^ {2 + r}} \bigg) \frac {\min \left\{\frac {1}{2} (t - \tau) ^ {2} , 1 \right\}}{(1 + \tau) ^ {r}}
$$

for some absolute constant$C _ { \omega } ^ { r }$depending only on$r$(we also denote$\omega _ { 0 , n } ^ { r , 1 } \mathrm { = } \omega _ { n } ^ { r , 1 }$and $\omega _ { 0 , n } ^ { r , 2 } \ L { = } \omega _ { n } ^ { r , 2 } )$

From the estimates on the characteristics and$( \bf E _ { h } ^ { n } )$will follow the following “secondary controls” on the distribution function:

$$
\left\{ \begin{array}{l} \sup _ {0 \leqslant \tau \leqslant t} \| (\nabla_ {x} h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; p}} \leqslant \delta_ {k}, \\ \sup _ {0 \leqslant \tau \leqslant t} \| \nabla_ {x} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; p}} \leqslant \delta_ {k}, \\ \| ((\nabla_ {v} + \tau \nabla_ {x}) h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; p}} \leqslant \delta_ {k}, \\ \| (\nabla_ {v} + \tau \nabla_ {x}) (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; p}} \leqslant \delta_ {k}, \\ \sup _ {0 \leqslant \tau \leqslant t} \frac {1}{(1 + \tau) ^ {2}} \| (\nabla \nabla h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; 1}} \leqslant \delta_ {k}, \\ \sup _ {0 \leqslant \tau \leqslant t} (1 + \tau) ^ {2} \| (\nabla h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {k - 1} - \nabla (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; 1}} \leqslant \delta_ {k}. \end{array} \right.\tag{\((\widetilde{\mathbf{E}}_{\mathbf{h}}^{\mathbf{n}})\}
$$

for all$k \in \{ 1 , . . . , n \}$and$p \in [ 1 , \bar { p } ]$

The transition from stage n to stage$n { \mathrel { + { 1 } } }$can be summarized as follows:

$$
\begin{array}{r l} (\widetilde {\mathbf {E}} _ {\varrho} ^ {\mathbf {n}}) & \stackrel {{(\mathbf {A} _ {\mathbf {n}})}} {{\Longrightarrow}} (\mathbf {E} _ {\Omega} ^ {\mathbf {n}}) + (\widetilde {\mathbf {E}} _ {\Omega} ^ {\mathbf {n}}) + (\mathbf {E} _ {\nabla \Omega} ^ {\mathbf {n}}), \\ (\mathbf {E} _ {\varrho} ^ {\mathbf {n}}) + (\mathbf {E} _ {\Omega} ^ {\mathbf {n}}) + (\widetilde {\mathbf {E}} _ {\Omega} ^ {\mathbf {n}}) + (\mathbf {E} _ {\nabla \Omega} ^ {\mathbf {n}}) + (\mathbf {E} _ {\mathbf {h}} ^ {\mathbf {n}}) + (\widetilde {\mathbf {E}} _ {\mathbf {h}} ^ {\mathbf {n}}) & \stackrel {{(\mathbf {B} _ {\mathbf {n}})}} {{\Longrightarrow}} (\mathbf {E} _ {\varrho} ^ {\mathbf {n + 1}}) + (\widetilde {\mathbf {E}} _ {\varrho} ^ {\mathbf {n + 1}}) + (\mathbf {E} _ {\mathbf {h}} ^ {\mathbf {n + 1}}) + (\widetilde {\mathbf {E}} _ {\mathbf {h}} ^ {\mathbf {n + 1}}). \end{array}
$$

The first implication$\left( \mathbf { A _ { n } } \right)$is proven by an amplification of the technique used in$\ S 5 ;$ ultimately, it relies on repeated application of Picard’s fixed-point theorem in analytic norms. The second implication$\left( \mathbf { B _ { n } } \right)$is the harder part; it uses the machinery from$\ S 6$ and$\ S 7 _ { ; }$, together with the idea of simultaneously propagating a shifted$\mathcal { Z }$norm for the kinetic distribution and an$\mathcal { F }$norm for the density.

In both implications, the stratification of error estimates will prevent the blow up of constants. So we shall decompose the force fieldF<sup>n</sup>$F ^ { n }$generated by$f ^ { n }$as

$$
F ^ {n} = F [ f ^ {n} ] = E ^ {1} + \ldots + E ^ {n},
$$

where$E ^ { k } = F [ h ^ { k } ] = - \nabla W * \varrho [ h ^ { k } ]$

The plan of the estimates is as follows. We shall inductively construct a sequence of constant coeficients

$$
\begin{array}{l} \lambda^ {\sharp} > \lambda_ {1} > \lambda_ {1} ^ {*} > \lambda_ {2} > \ldots > \lambda_ {n} > \lambda_ {n} ^ {*} > \lambda_ {n + 1} > \ldots , \\ \mu^ {\sharp} > \mu_ {1} > \mu_ {1} ^ {*} > \mu_ {2} > \ldots > \mu_ {n} > \mu_ {n} ^ {*} > \mu_ {n + 1} > \ldots \end{array}
$$

(where$\lambda _ { n }$and$\mu _ { n }$will be fixed in the proof of$\left( \mathbf { A _ { n } } \right)$, and$\lambda _ { n + 1 }$and$\mu _ { n + 1 }$in the proof of$\left( \mathbf { B _ { n } } \right) )$) converging respectively to$\lambda _ { \infty }$and$\mu _ { \infty } ;$and a sequence$( \delta _ { k } ) _ { k = } ^ { \infty }$decreasing very fast to zero. For simplicity we shall let

$$
\mathcal {R} ^ {n} (\tau , t) = \mathcal {R} _ {1} ^ {n} (\tau , t) + \mathcal {R} _ {2} ^ {n} (\tau , t) \quad \text { and } \quad \mathcal {R} ^ {k, n} (\tau , t) = \mathcal {R} _ {1} ^ {k, n} (\tau , t) + \mathcal {R} _ {2} ^ {k, n} (\tau , t),
$$

and assume that$2 \pi ( \lambda _ { j } - \lambda _ { j } ^ { * } ) { \leqslant } 1$; so

$$
\mathcal {R} ^ {k, n} (\tau , t) \leqslant C _ {\omega} ^ {r} \left(\sum_ {j = k + 1} ^ {n} \frac {\delta_ {j}}{(2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})) ^ {2 + r}}\right) \frac {\min \{t - \tau , 1 \}}{(1 + \tau) ^ {r}} \quad \text { and } \quad \mathcal {R} ^ {0, n} = \mathcal {R} ^ {n}.\tag{10.11}
$$

It will be suficient to work with some fixed$r ,$large enough (as we shall see,$r { = } 4$will do).

To go from stage n to stage$n { \mathrel { + { 1 } } }$, we shall do as follows:

Implication$\left( \mathbf { A _ { n } } \right)$<sup>(</sup>§<sup>10.3):</sup>

Step 1. Estimate$\Omega ^ { n } - \operatorname { I d }$(the bound should be uniform in n).

Step 2. Estimate$\Omega ^ { n } - \Omega ^ { k } ~ ( k \leqslant n - 1 )$; the error should be small when$k \to \infty )$

Step 3. Estimate$\nabla \Omega ^ { n } - I$

Step 4. Estimate$( \Omega ^ { k } ) ^ { - 1 } \circ \Omega ^ { n }$

Implication$\mathbf { \left( B _ { n } \right) \ ( \ S 1 0 . 4 ) }$

Step 5. Estimate$h ^ { k }$and its derivatives along the composition by$\Omega ^ { n }$

Step 6. Estimate$\varrho [ h ^ { n + 1 } ]$, using 6 and$\ S 7 .$

Step 7. Estimate$F [ h ^ { n + 1 } ]$from$\varrho [ h ^ { n + 1 } ]$

Step 8. Estimate$h ^ { n + 1 } \circ \Omega ^ { n }$

Step 9. Estimate derivatives of$h ^ { n + 1 }$composed with$\Omega ^ { n }$

Step 10. Show that for$h ^ { n + 1 }$, and composition by$\Omega ^ { n }$asymptotically commute.

## 10.3. Estimates on the characteristics

In this subsection, we assume that$( \mathbf { E } _ { \varrho } ^ { \mathbf { n } } )$is proven, and establish$( \mathbf { E _ { \Omega } ^ { n } } ) + ( \widetilde { \mathbf { E } } _ { \Omega } ^ { \mathbf { n } } ) + ( \mathbf { E } _ { \nabla \Omega } ^ { \mathbf { n } } )$ Let${ \lambda } _ { n } ^ { * } < { \lambda } _ { n }$and$\mu _ { n } ^ { * } < \mu _ { n }$to be fixed later on.

## 10.3.1. Step 1. Estimate of$\Omega ^ { n } - \mathbf { I d }$

This is the first and archetypal estimate. We shall bound$\Omega ^ { n } X _ { t , \tau } - x$in the hybrid norm $\mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \mu _ { n } ^ { * } }$. The Sobolev correction$\gamma$will play no role here in the proofs, and for simplicity we shall forget it in the computations, just recall it in the final results. (Use Proposition 4.32 whenever needed.)

Since we expect the characteristics for the force field$F ^ { n }$to be close to the free transport characteristics, it is natural to write

$$
X _ {t, \tau} ^ {n} (x, v) = x - v (t - \tau) + Z _ {t, \tau} ^ {n} (x, v),\tag{10.12}
$$

where$Z _ { t , \tau } ^ { n }$solves

$$
\left\{ \begin{array}{l} \frac {\partial^ {2}}{\partial \tau^ {2}} Z _ {t, \tau} ^ {n} (x, v) = F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n} (x, v)) \\ Z _ {t, t} ^ {n} (x, v) = 0, \quad \partial_ {\tau} Z _ {t, \tau} ^ {n} | _ {t = \tau} (x, v) = 0. \end{array} \right.\tag{10.13}
$$

(With respect to$\ S 5$we have dropped the parameter$\varepsilon ,$to take advantage of the “stratified” nature of$F ^ { n } { \mathrm { ; } }$; anyway this parameter was cosmetic.) So if we fix$t > 0 , ( Z _ { t , \tau } ^ { n } ) _ { 0 \leqslant \tau \leqslant t }$is a fixed point of the map

$$
\Psi \colon (W _ {t, \tau}) _ {0 \leqslant \tau \leqslant t} \longmapsto (Z _ {t, \tau}) _ {0 \leqslant \tau \leqslant t}
$$

defined by

$$
\left\{ \begin{array}{l} \frac {\partial^ {2}}{\partial \tau^ {2}} Z _ {t, \tau} = F ^ {n} (\tau , x - v (t - \tau) + W _ {t, \tau}) \\ Z _ {t, t} = 0, \quad \partial_ {\tau} Z _ {t, \tau} | _ {\tau = t} = 0. \end{array} \right.\tag{10.14}
$$

The goal is to estimate$Z _ { t , \tau } ^ { n } - x$in the hybrid norm$\mathcal { Z } _ { t - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \mu _ { n } ^ { * } }$

We first bound$( Z _ { 0 } ^ { n } ) _ { t , \tau } { = } \Psi ( 0 )$. Explicitly,

$$
(Z _ {0} ^ {n}) _ {t, \tau} (x, v) = \int_ {\tau} ^ {t} (s - \tau) F ^ {n} (s, x - v (t - s)) d s.
$$

By Propositions 4.15 (i) and 4.19,

$$
\begin{array}{r l} & {\| (Z _ {0} ^ {n}) _ {t, \tau} \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \int_ {\tau} ^ {t} (s - \tau) \| F ^ {n} (s, x - v (t - s)) \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} d s} \\ & {\qquad = \int_ {\tau} ^ {t} (s - \tau) \| F ^ {n} (s, \cdot) \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} d s} \\ & {\qquad = \int_ {\tau} ^ {t} (s - \tau) \| F ^ {n} (s, \cdot) \| _ {\mathcal {F} ^ {\nu (s, t)}} d s,} \end{array}\tag{10.15}
$$

where

$$
\nu (s, t) = \lambda_ {n} ^ {*} | s - b (t - s) | + \mu_ {n} ^ {*}.\tag{10.16}
$$

Case 1. If$s { \geqslant } b t / ( 1 { + } b )$, then

$$
\nu (s, t) \leqslant \lambda_ {n} ^ {*} s + \mu_ {n} ^ {*} \leqslant \lambda_ {k} s + \mu_ {k} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s, \quad k \in \{1,..., n \}.\tag{10.17}
$$

Case 2. If$s { < } b t / ( 1 { + } b )$, then necessarily$s { \leqslant } B { \leqslant } T$. Taking into account (10.6), we have

$$
\nu (s, t) = \lambda_ {n} ^ {*} b t + \mu_ {n} ^ {*} - \lambda_ {n} ^ {*} (1 + b) s\tag{10.18}
$$

$$
\leqslant \lambda_ {n} ^ {*} B + \mu_ {n} ^ {*} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s.\tag{10.19}
$$

(Of course, the assumption$\lambda ^ { \sharp } - \lambda _ { \infty } \leqslant \operatorname* { m i n } \big \{ 1 , \frac { 1 } { 2 } \lambda _ { \infty } \big \}$implies that$\lambda _ { k } - \lambda _ { n } ^ { * } \leqslant \lambda _ { n } ^ { * } . )$In particular, by (10.7),

$$
\nu (s, t) \leqslant \mu^ {\sharp} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s, \quad k \in \{1,..., n \}.\tag{10.20}
$$

We plug these bounds into (10.15), then use$\widehat { E } ^ { k } ( s , 0 ) = 0$and the bounds$( \widetilde { \mathbf { E } } _ { \varrho } ^ { \mathbf { n } } )$and (10.17) (for large times), and (10.3) and (10.20) (for short times). This yields

$$
\begin{array}{r l} & {\| (Z _ {0} ^ {n}) _ {t, \tau} \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}} \\ & {\quad \leqslant \sum_ {k = 1} ^ {n} \Bigg (\int_ {\tau \vee b t / (1 + b)} ^ {t} (s - \tau) \| E ^ {k} (s, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {k} s + \mu_ {k} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s}} d s} \\ & {\qquad \qquad \qquad \qquad + \int_ {\tau} ^ {\tau \vee b t / (1 + b)} (s - \tau) \| E ^ {k} (s, \cdot) \| _ {\mathcal {F} ^ {\mu^ {\sharp} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s}} d s \Bigg)} \\ & {\leqslant \sum_ {k = 1} ^ {n} \Bigg (\int_ {\tau \vee b t / (1 + b)} ^ {t} (s - \tau) e ^ {- 2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) s} \| E ^ {k} (s, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {k} s + \mu_ {k}}} d s} \\ & {\qquad \qquad \qquad \qquad + \int_ {\tau} ^ {\tau \vee b t / (1 + b)} (s - \tau) e ^ {- 2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) s} \| E ^ {k} (s, \cdot) \| _ {\mathcal {F} ^ {\mu^ {\sharp}}} d s \Bigg)} \\ & {\leqslant \sum_ {k = 1} ^ {n} \delta_ {k} \int_ {\tau} ^ {t} (s - \tau) e ^ {- 2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) s} d s} \\ & {\leqslant \sum_ {k = 1} ^ {n} \delta_ {k} e ^ {- 2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) \tau} \min \biggl \{\frac {(t - \tau) ^ {2}}{2}, \frac {1}{(2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*})) ^ {2}} \biggr \}} \\ & {\leqslant \mathcal {R} _ {2} ^ {n} (\tau , t).} \end{array}\tag{10.21}
$$

Let us define the norm

$$
\left\| \left(Z _ {t, \tau}\right) _ {0 \leqslant \tau \leqslant t} \right\| _ {n} := \sup _ {0 \leqslant \tau \leqslant t} \frac {\left\| Z _ {t , \tau} \right\| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b) , \mu_ {n} ^ {*}}}}{\mathcal {R} _ {2} ^ {n} (\tau , t)}.
$$

(Note the diference with$\ S 5 \mathrm { : }$: now the regularity exponents depend on$\mathrm { t i m e ( s ) . ) }$Inequality (10.21) means that$\| \Psi ( 0 ) \| _ { n } \leqslant 1$. We shall check that$\Psi$is${ \frac { 1 } { 2 } } .$-Lipschitz on the ball$B ( 0 , 2 )$ in the norm$\| \cdot \| _ { n }$. This will be subtle: the uniform bounds on the size of the force field, coming from the preceding steps, will allow us to get good decaying exponentials, which in turn will imply uniform error bounds at the present stage.

So let$W , \widetilde { W } \in B ( 0 , 2 )$, and let$Z { = } \Psi ( W )$and${ \widetilde { Z } } { = } \Psi ( { \widetilde { W } } )$. As in$\ S 5$, we write

$$
Z _ {t, \tau} - \widetilde {Z} _ {t, \tau} = \int_ {0} ^ {1} \int_ {\tau} ^ {t} (s - \tau) \nabla_ {x} F ^ {n} (s, x - v (t - s) + \theta W _ {t, s} + (1 - \theta) \widetilde {W} _ {t, s}) \cdot (W _ {t, s} - \widetilde {W} _ {t, s}) d s d \theta ,
$$

and deduce that

$$
\left\| \left(Z _ {t, \tau} - \widetilde {Z} _ {t, \tau}\right) _ {0 \leqslant \tau \leqslant t} \right\| _ {n} \leqslant A (t) \left\| \left(W _ {t, s} - \widetilde {W} _ {t, s}\right) _ {0 \leqslant s \leqslant t} \right\| _ {n},
$$

where

$$
\begin{array}{r l} & A (t) = \sup _ {0 \leqslant \tau \leqslant s \leqslant t} \frac {\mathcal {R} _ {2} ^ {n} (s , t)}{\mathcal {R} _ {2} ^ {n} (\tau , t)} \\ & \qquad \times \int_ {0} ^ {1} \int_ {\tau} ^ {t} (s - \tau) \| \nabla_ {x} F ^ {n} (s, x - v (t - s) + \theta W _ {t, s} + (1 - \theta) \widetilde {W} _ {t, s}) \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} d s d \theta . \end{array}
$$

For$\tau \leqslant s$we have$\mathcal { R } _ { 2 } ^ { n } ( s , t ) \leqslant \mathcal { R } _ { 2 } ^ { n } ( \tau , t )$. Also, by Proposition 4.25 (applied with$V { = } 0 .$ $b { = } { - } ( t { - } s )$and$\sigma { = } 0$in that statement) and Proposition 4.15,

$$
A (t) \leqslant \sup _ {0 \leqslant \tau \leqslant t} \int_ {\tau} ^ {t} (s - \tau) \| \nabla_ {x} F ^ {n} (s, \cdot) \| _ {\mathcal {F} ^ {\nu (s, t) + e (s, t)}} d s,
$$

where$\nu$is defined by (10.16) and the “error”$e ( s , t )$arising from composition is given by

$$
e (s, t) = \sup _ {0 \leqslant \theta \leqslant 1} \| \theta W _ {t, s} + (1 - \theta) \widetilde {W} _ {t, s} \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 2 \mathcal {R} _ {2} ^ {n} (s, t).
$$

Since

$$
\mathcal {R} _ {2} ^ {n} (s, t) \leqslant \omega_ {n} ^ {1, 2} (s, t) := C _ {\omega} ^ {1} \bigg (\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {3}} \bigg) \frac {\min \left\{\frac {1}{2} (t - s) ^ {2} , 1 \right\}}{1 + s},
$$

we have, for all$0 \leqslant s \leqslant t$

$$
2 \mathcal {R} _ {2} ^ {n} (s, t) \leqslant \frac {\lambda_ {n} ^ {*} b (t - s)}{2} 1 _ {s \geqslant b t / (1 + b)} + \frac {\mu^ {\sharp} - \mu_ {n} ^ {*}}{2} 1 _ {s \leqslant b t / (1 + b)},\tag{10.22}
$$

as soon as

$$
2 C _ {\omega} ^ {1} \left(\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*})) ^ {3}}\right) \leqslant \min \left\{\frac {\lambda_ {n} ^ {*} B}{6}, \frac {\mu^ {\sharp} - \mu_ {n} ^ {*}}{2} \right\} \quad \text { for   all } n \geqslant 1.\tag{\( (\mathbf{C}_{1}) \}
$$

We shall check later in$\ S 1 0 . 5$the feasibility of condition (C )—as well as a number of other forthcoming ones.

The extra error term in the exponent is suficiently small to be absorbed by what we throw away in (10.17) or in (10.18)–(10.20). So we obtain, as in the estimate of$Z _ { 0 } ^ { n }$ for any$k \in \{ 1 , . . . , n \}$,

$$
(\nu + e) (s, t) \leqslant \left\{ \begin{array}{l l} \lambda_ {k} s + \mu_ {k} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s & \text { for } s \geqslant b t / (1 + b), \\ \mu^ {\sharp} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s & \text { for } s \leqslant b t / (1 + b), \end{array} \right.
$$

and we deduce (using$( \widetilde { \mathbf { E } } _ { \rho } ^ { \mathbf { n } } )$and$\gamma \geqslant 1 )$that

$$
\begin{array}{l} A (t) \leqslant \sup _ {0 \leqslant \tau \leqslant t} \sum_ {k = 1} ^ {n} \biggl (\int_ {\tau \vee b t / (1 + b)} ^ {t} (s - \tau) \| \nabla_ {x} E ^ {k} (s, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {k} s + \mu_ {k} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s}} d s \\ \qquad \qquad \qquad \qquad + \int_ {\tau} ^ {\tau \vee b t / (1 + b)} (s - \tau) \| \nabla_ {x} E ^ {k} (s, \cdot) \| _ {\mathcal {F} ^ {\mu^ {\sharp} - (\lambda_ {k} - \lambda_ {n} ^ {*}) s}} d s \biggr) \\ \leqslant \sup _ {0 \leqslant \tau \leqslant t} \sum_ {k = 1} ^ {n} \delta_ {k} \int_ {\tau} ^ {t} (s - \tau) e ^ {- (\lambda_ {k} - \lambda_ {n} ^ {*}) s} d s \\ \leqslant \sup _ {0 \leqslant \tau \leqslant t} \mathcal {R} _ {2} ^ {n} (\tau , t) = \mathcal {R} _ {2} ^ {n} (0, t) \\ \leqslant \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*})) ^ {2}}. \end{array}
$$

If the latter quantity is bounded above by${ \frac { 1 } { 2 } } ;$, then Ψ is${ \frac { 1 } { 2 } } \cdot$-Lipschitz and we may apply the fixed-point result from Theorem A.2. Therefore, under the condition (whose feasibility will be checked later)

$$
\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*})) ^ {2}} \leqslant \frac {1}{2} \quad \text { for   all } n \geqslant 1,\tag{\( (\mathbf{C}_{2}) \}
$$

we deduce that

$$
\left\| Z _ {t, \tau} ^ {n} \right\| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 2 \mathcal {R} _ {2} ^ {n} (\tau , t).
$$

After that, the estimates on the deflection map are obtained exactly as in$\ S 5 \colon$writing $\Omega _ { t , \tau } ^ { n } = ( \Omega ^ { n } X _ { t , \tau } , \Omega ^ { n } V _ { t , \tau } )$, recalling the dependence on γ again, we end up with

$$
\left\{ \begin{array}{l} \| \Omega^ {n} X _ {t, \tau} - x \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), (\mu_ {n} ^ {*}, \gamma)}} \leqslant 2 \mathcal {R} _ {2} ^ {n} (\tau , t), \\ \| \Omega^ {n} V _ {t, \tau} - v \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), (\mu_ {n} ^ {*}, \gamma)}} \leqslant \mathcal {R} _ {1} ^ {n} (\tau , t). \end{array} \right.\tag{10.23}
$$

## 10.3.2. Step 2. Estimate of$\Omega ^ { n } - \Omega ^ { k }$

In this step our goal is to estimate$\Omega ^ { n } - \Omega ^ { k }$for$1 \leqslant k \leqslant n - 1$. The point is that the error should be small as$k \to \infty$, uniformly in$n ,$, so we cannot just write

$$
\left\| \Omega^ {n} - \Omega^ {k} \right\| \leqslant \left\| \Omega^ {n} - \operatorname{Id} \right\| + \left\| \Omega^ {k} - \operatorname{Id} \right\|.
$$

Instead, we start again from the diferential equation satisfied by$Z ^ { k }$and$Z ^ { n }$:

$$
\begin{array}{r l} & {\frac {\partial^ {2}}{\partial \tau^ {2}} (Z _ {t, \tau} ^ {n} - Z _ {t, \tau} ^ {k}) (x, v) = F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n} (x, v)) - F ^ {k} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {k} (x, v))} \\ & {\qquad = F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n}) - F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {k})} \\ & {\qquad + (F ^ {n} - F ^ {k}) (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {k}).} \end{array}
$$

This, together with the boundary conditions$Z _ { t , t } ^ { n } - Z _ { t , t } ^ { k } { = } 0$and$\partial _ { \tau } ( Z _ { t , \tau } ^ { n } - Z _ { t , \tau } ^ { k } ) | _ { \tau = t } = 0$, implies that

$$
\begin{array}{r} Z _ {t, \tau} ^ {n} - Z _ {t, \tau} ^ {k} = \int_ {0} ^ {1} \int_ {\tau} ^ {t} (s - \tau) \nabla_ {x} F ^ {n} (s, x - v (t - s) + \theta Z _ {t, s} ^ {k} + (1 - \theta) Z _ {t, s} ^ {n}) \cdot (Z _ {t, s} ^ {n} - Z _ {t, s} ^ {k}) d s d \theta \\ + \int_ {\tau} ^ {t} (s - \tau) (F ^ {n} - F ^ {k}) (s, x - v (t - s) + Z _ {t, s} ^ {k} (x, v)) d s. \end{array}
$$

We fix t and define the norm

$$
\| (Z _ {t, \tau}) _ {0 \leqslant \tau \leqslant t} \| _ {k, n} := \sup _ {0 \leqslant \tau \leqslant t} \frac {\| Z _ {t , \tau} \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b) , \mu_ {n} ^ {*}}}}{\mathcal {R} _ {2} ^ {k , n} (\tau , t)},
$$

where$\mathcal { R } _ { 2 } ^ { k , n }$is defined in (10.9). Using the bounds on$Z ^ { n }$and$Z ^ { k }$in$\| \cdot \| _ { n }$(since $\| \cdot \| _ { n } \leqslant \| \cdot \| _ { k }$by using the fact that$\mathcal { R } _ { 2 } ^ { k } \leqslant \mathcal { R } _ { 2 } ^ { n } )$and proceeding as before, we get that

$$
\begin{array}{r l} & {\left\| \left(Z _ {t, \tau} ^ {n} - Z _ {t, \tau} ^ {k}\right) _ {0 \leqslant \tau \leqslant t} \right\| _ {k, n}} \\ & {\quad \leqslant \frac {1}{2} \left\| \left(Z _ {t, \tau} ^ {n} - Z _ {t, \tau} ^ {k}\right) _ {0 \leqslant \tau \leqslant t} \right\| _ {k, n}} \\ & {\qquad + \left\| \left(\int_ {\tau} ^ {t} (s - \tau) (F ^ {n} - F ^ {k}) (s, x - v (t - s) + Z _ {t, s} ^ {k}) d s\right) _ {0 \leqslant \tau \leqslant t} \right\| _ {k, n}.} \end{array}\tag{10.24}
$$

Next we estimate

$$
\begin{array}{r l} & {\| (F ^ {n} - F ^ {k}) (s, x - v (t - s) + Z _ {t, s} ^ {k}) \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} = \| (F ^ {n} - F ^ {k}) (s, X _ {t, s} ^ {k}) \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}} \\ & {\qquad \qquad \qquad \qquad = \| (F ^ {n} - F ^ {k}) (s, \Omega_ {t, s} ^ {k}) \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}} \\ & {\qquad \qquad \qquad \qquad \leqslant \| (F ^ {n} - F ^ {k}) (s, \cdot) \| _ {\mathcal {F} ^ {\nu (s, t) + e (s, t)}},} \end{array}
$$

where the last inequality follows from Proposition 4.25, ν is again given by (10.16), and

$$
e (s, t) = \| \Omega^ {k} X _ {t, s} - \mathrm{Id} \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 2 \mathcal {R} _ {2} ^ {k} (s, t) \leqslant 2 \mathcal {R} _ {2} ^ {n} (s, t).
$$

The same reasoning as in Step 1 yields, under assumptions$\bf ( C _ { 1 } )$and$\bf ( C _ { 2 } )$, for $k + 1 { \leqslant } j { \leqslant } n$

$$
(\nu + e) (s, t) \leqslant \left\{ \begin{array}{l l} \lambda_ {j} s + \mu_ {j} - (\lambda_ {j} - \lambda_ {n} ^ {*}) s & \text { for } s \geqslant b t / (1 + b), \\ \mu^ {\sharp} - (\lambda_ {j} - \lambda_ {n} ^ {*}) s & \text { for } s \leqslant b t / (1 + b), \end{array} \right.
$$

and so

$$
\left\| F _ {s} ^ {n} - F _ {s} ^ {k} \right\| _ {\mathcal {F} ^ {\nu + e}} \leqslant \sum_ {j = k + 1} ^ {n} \delta_ {j} e ^ {- 2 \pi \left(\lambda_ {j} - \lambda_ {n} ^ {*}\right) s}.
$$

For any$\tau { \geqslant } 0$, by integrating in time we find that

$$
\begin{array}{l} \left\| \int_ {\tau} ^ {t} (s - \tau) (F ^ {n} - F ^ {k}) (s, x - v (t - s) + Z _ {t, s} ^ {k})   d s \right\| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \\ \qquad \leqslant \int_ {\tau} ^ {t} (s - \tau) \sum_ {j = k + 1} ^ {n} \delta_ {j} e ^ {- 2 \pi (\lambda_ {j} - \lambda_ {n} ^ {*}) s}   d s \leqslant \mathcal {R} _ {2} ^ {k, n} (\tau , t). \end{array}
$$

Therefore

$$
\left\| \left\| \left(\int_ {\tau} ^ {t} (s - \tau) (F ^ {n} - F ^ {k}) (s, x - v (t - s) + Z _ {t, s} ^ {k})   d s\right) _ {0 \leqslant \tau \leqslant t} \right\| \right\| _ {k, n} \leqslant 1
$$

and, by(10.24),

$$
\left\| \left(Z _ {t, \tau} ^ {n} - Z _ {t, \tau} ^ {k}\right) _ {0 \leqslant \tau \leqslant t} \right\| _ {k, n} \leqslant 2.
$$

Recalling the Sobolev correction, we conclude that

$$
\left\| \Omega^ {n} X _ {t, \tau} - \Omega^ {k} X _ {t, \tau} \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), (\mu_ {n} ^ {*}, \gamma)}} \leqslant 2 \mathcal {R} _ {2} ^ {k, n} (\tau , t).\tag{10.25}
$$

For the velocity component, say$U ,$, we write

$$
\begin{array}{r l} & {\frac {\partial}{\partial \tau} (U _ {t, \tau} ^ {n} - U _ {t, \tau} ^ {k}) (x, v) = F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n} (x, v)) - F ^ {k} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {k} (x, v))} \\ & {\qquad = F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n}) - F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {k})} \\ & {\qquad + (F ^ {n} - F ^ {k}) (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {k}),} \end{array}
$$

where$Z ^ { n }$and$Z ^ { k }$were estimated above, and the boundary conditions are${ U _ { t , t } ^ { n } } - { U _ { t , t } ^ { k } } = 0$ Thus

$$
\begin{array}{r l} & U _ {t, \tau} ^ {n} - U _ {t, \tau} ^ {k} = \int_ {0} ^ {1} \int_ {\tau} ^ {t} \nabla_ {x} F ^ {n} (s, x - v (t - s) + \theta Z _ {t, s} ^ {k} + (1 - \theta) Z _ {t, s} ^ {n}) \cdot (Z _ {t, s} ^ {n} - Z _ {t, s} ^ {k}) d s d \theta \\ & \qquad + \int_ {\tau} ^ {t} (F ^ {n} - F ^ {k}) (s, x - v (t - s) + Z _ {t, s} ^ {k} (x, v)) d s, \end{array}
$$

and from this one easily derives the similar estimates

$$
\left\{ \begin{array}{l} \| \Omega^ {n} X _ {t, \tau} - \Omega^ {k} X _ {t, \tau} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 2 \mathcal {R} _ {2} ^ {k, n} (t, \tau), \\ \| \Omega^ {n} V _ {t, \tau} - \Omega^ {k} V _ {t, \tau} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \mathcal {R} _ {1} ^ {k, n} (t, \tau) + \mathcal {R} _ {2} ^ {k, n} (t, \tau). \end{array} \right.
$$

## 10.3.3. Step 3. Estimate of$\nabla \Omega ^ { n }$

We now establish a control on the derivative of the deflection map. Of course, we could deduce such a control from the bound on$\Omega ^ { n } - \operatorname { I d }$and Proposition 4.32 (vi): for instance, if$\lambda _ { n } ^ { * * } < \lambda _ { n } ^ { * }$and$\mu _ { n } ^ { * * } < \mu _ { n } ^ { * }$, then

$$
\| \nabla \Omega_ {t, \tau} ^ {n} - I \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {* *} (1 + b), (\mu_ {n} ^ {* *}, \gamma)}} \leqslant \frac {C \mathcal {R} _ {2} ^ {n} (\tau , t)}{\min \{\lambda_ {n} ^ {*} - \lambda_ {n} ^ {* *} , \mu_ {n} ^ {*} - \mu_ {n} ^ {* *} \}}.\tag{10.26}
$$

But this bound involves very large constants, and is useless in our argument. Better estimates can be obtained by using again equation (10.13). Writing

$$
(\Omega_ {t, \tau} ^ {n} - \mathrm{Id}) (x, v) = (Z _ {t, \tau} ^ {n} (x + v (t - \tau), v), \dot {Z} _ {t, \tau} ^ {n} (x + v (t - \tau), v)),
$$

where the dot stands for$\partial / \partial \tau$, we get by diferentiation

$$
\nabla_ {x} \Omega_ {t, \tau} ^ {n} - (I, 0) = (\nabla_ {x} Z _ {t, \tau} ^ {n} (x + v (t - \tau), v), \nabla_ {x} \dot {Z} _ {t, \tau} ^ {n} (x + v (t - \tau), v)),
$$

$$
\nabla_ {v} \Omega_ {t, \tau} ^ {n} - (0, I) = ((\nabla_ {v} + (t - \tau) \nabla_ {x}) Z _ {t, \tau} ^ {n} (x + v (t - \tau), v),
$$

$$
(\nabla_ {v} + (t - \tau) \nabla_ {x}) \dot {Z} _ {t, \tau} ^ {n} (x + v (t - \tau), v)).
$$

Let us estimate for instance$\nabla _ { x } \Omega - ( I , 0 )$, or equivalently$\nabla _ { x } Z _ { t , \tau } ^ { n }$. By diferentiating (10.13), we obtain

$$
\frac {\partial^ {2}}{\partial \tau^ {2}} \nabla_ {x} Z _ {t, \tau} ^ {n} (x, v) = \nabla_ {x} F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n} (x, v)) \cdot (\mathrm{Id} + \nabla_ {x} Z _ {t, \tau} ^ {n}).
$$

So$\nabla _ { x } Z _ { t , \tau } ^ { n }$<sub>τ</sub> is a fixed point of$\Psi \colon W \mapsto Q$, where$W$and$Q$are functions of$\tau \in [ 0 , t ]$satisfying

$$
\left\{ \begin{array}{l} \frac {\partial^ {2} Q}{\partial \tau^ {2}} = \nabla_ {x} F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n}) (I + W), \\ Q (t) = 0, \quad \partial_ {\tau} Q (t) = 0. \end{array} \right.
$$

We treat this in the same way as in Steps 1 and 2, and find for$Q _ { x }$(the x component of$Q )$the same estimates as we had previously on the x component of Ω. For the velocity component, a direct estimate from the integral equation expressing the velocity in terms of F yields a control by$\mathcal { R } _ { 1 } ^ { n } { + } \mathcal { R } _ { 2 } ^ { n }$. Finally for$\nabla _ { v } \Omega$this is similar, noting that $( \nabla _ { v } + ( t - \tau ) \nabla _ { x } ) ( x - v ( t - \tau ) ) { = } 0$, the diferential equation being for instance:

$$
\frac {\partial^ {2}}{\partial \tau^ {2}} (\nabla_ {v} + (t - \tau) \nabla_ {x}) Z _ {t, \tau} ^ {n} (x, v) = \nabla_ {x} F ^ {n} (\tau , x - v (t - \tau) + Z _ {t, \tau} ^ {n} (x, v)) \cdot ((\nabla_ {v} + (t - \tau) \nabla_ {x}) Z _ {t, \tau} ^ {n}).
$$

In the end we obtain

$$
\left\{ \begin{array}{l} \sup _ {0 \leqslant \tau \leqslant t} \| \nabla \Omega^ {n} X _ {t, \tau} - (I, 0) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 2 \mathcal {R} _ {2} ^ {n} (\tau , t), \\ \sup _ {0 \leqslant \tau \leqslant t} \| \nabla \Omega^ {n} V _ {t, \tau} - (0, I) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \mathcal {R} _ {1} ^ {n} (\tau , t) + \mathcal {R} _ {2} ^ {n} (\tau , t). \end{array} \right.\tag{10.27}
$$

## 10.3.4. Step 4. Estimate of$( \Omega ^ { k } ) ^ { - 1 } \circ \Omega ^ { n }$

We do this by applying Proposition 4.28 with$F { = } \Omega ^ { k }$and$G { = } \Omega ^ { n }$. (Note that we cannot exchange the roles of$\Omega ^ { k }$and$\Omega ^ { n }$in this step, because we have better information on the regularity of$\Omega ^ { k } . )$) Let$\varepsilon { = } \varepsilon ( d )$be the small constant appearing in Proposition 4.28. If

$$
3 \mathcal {R} _ {2} ^ {k} (\tau , t) + \mathcal {R} _ {1} ^ {k} (\tau , t) \leqslant \varepsilon \quad \text { for   all } k \geqslant 1,\tag{\( (\mathbf{C}_{3}) \}
$$

then$\| \nabla \Omega _ { t , \tau } ^ { k } - I \| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { k } ^ { * } ( 1 + b ) , \mu _ { k } ^ { * } } } \leqslant \varepsilon ;$if in addition

$$
\begin{array}{r l} & 2 (1 + \tau) (1 + B) (3 \mathcal {R} _ {2} ^ {k, n} + \mathcal {R} _ {1} ^ {k, n}) (\tau , t) \leqslant \max \{\lambda_ {k} ^ {*} - \lambda_ {n} ^ {*}, \mu_ {k} ^ {*} - \mu_ {n} ^ {*} \} \\ & \qquad \text {for all k\in\{1,\ldots,n - 1\} and all t\geqslant\tau}, \end{array}\tag{\( (\mathbf{C}_{4}) \}
$$

then

$$
\left\{ \begin{array}{l} \lambda_ {n} ^ {*} (1 + b) + 2 \| \Omega^ {n} - \Omega^ {k} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \lambda_ {k} ^ {*} (1 + b), \\ \mu_ {n} ^ {*} + 2 \bigg (1 + \bigg | \tau - \frac {b t}{1 + b} \bigg | \bigg) \| \Omega^ {n} - \Omega^ {k} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \mu_ {k} ^ {*}. \end{array} \right.
$$

(Once again, short times should be treated separately. Further note that the need for the factor$1 + \tau$$\left( \mathbf { C _ { 4 } } \right)$ultimately comes from the fact that we are composing also in the v variable, see the coeficient σ in the last norm of (4.30).) Then Proposition 4.28 (ii) yields

$$
\| (\Omega_ {t, \tau} ^ {k}) ^ {- 1} \circ \Omega_ {t, \tau} ^ {n} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 2 \| \Omega_ {t, \tau} ^ {k} - \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant 4 (\mathcal {R} _ {1} ^ {k, n} + \mathcal {R} _ {2} ^ {k, n}) (\tau , t).
$$

## 10.3.5. Partial conclusion

At this point we have established$( \mathbf { E _ { \Omega } ^ { n } } ) + ( \widetilde { \mathbf { E } } _ { \Omega } ^ { \mathbf { n } } ) + ( \mathbf { E } _ { \nabla \Omega } ^ { \mathbf { n } } )$

## 10.4. Estimates on the density and distribution along characteristics

In this subsection we establish$( \mathbf { E } _ { \varrho } ^ { \mathbf { n } + \mathbf { 1 } } ) + ( \widetilde { \mathbf { E } } _ { \varrho } ^ { \mathbf { n } + \mathbf { 1 } } ) + ( \mathbf { E } _ { \mathbf { h } } ^ { \mathbf { n } + \mathbf { 1 } } ) + ( \widetilde { \mathbf { E } } _ { \mathbf { h } } ^ { \mathbf { n } + \mathbf { 1 } } )$

## 10.4.1. Step 5. Estimate of$h ^ { k } \circ \Omega ^ { n }$and$( \nabla h ^ { k } ) \circ \Omega ^ { n } , k \leqslant n$

Let$k \in \{ 1 , . . . , n \}$. Since

$$
h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {n} = (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \circ ((\Omega_ {t, \tau} ^ {k - 1}) ^ {- 1} \circ \Omega_ {t, \tau} ^ {n}),
$$

the control on$h ^ { k _ { \mathrm { o } } } \Omega ^ { n }$will follow from the control on$h ^ { k _ { \mathrm { o } } } \Omega ^ { k - 1 }$in$( \bf E _ { h } ^ { n } )$), together with the control on$( \Omega ^ { k - 1 } ) ^ { - 1 } \circ \Omega ^ { n }$in$( \widetilde { \mathbf { E } } _ { \Omega } ^ { \mathbf { n } } )$. If

$$
(1 + \tau) \| (\Omega_ {t, \tau} ^ {k - 1}) ^ {- 1} \circ \Omega_ {t, \tau} ^ {n} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \min \{\lambda_ {k} - \lambda_ {n} ^ {*}, \mu_ {k} - \mu_ {n} ^ {*} \},\tag{10.28}
$$

then we can apply Proposition 4.25 and get, for any$p \in [ 1 , \bar { p } ]$, and$t \geqslant \tau \geqslant 0$,

$$
\left\| h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {n} \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; p}} \leqslant \left\| h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1} \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; p}} \leqslant \delta_ {k}.\tag{10.29}
$$

In turn, (10.28) is satisfied if

$$
\begin{array}{c} 4 (1 + \tau) (\mathcal {R} _ {1} ^ {k, n} (\tau , t) + \mathcal {R} _ {2} ^ {k, n} (\tau , t)) \leqslant \min \{\lambda_ {k} - \lambda_ {n} ^ {*}, \mu_ {k} - \mu_ {n} ^ {*} \} \\ \text {for all k\in\{1,\ldots,n\} and all \tau\in[0,t] ;} \end{array}\tag{\( (\mathbf{C}_{5}) \}
$$

we shall check later the feasibility of this condition.

Then, by the same argument, we also have

$$
\sup _ {0 \leqslant \tau \leqslant t} \| (\nabla_ {x} h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; p}} + \| ((\nabla_ {v} + \tau \nabla_ {x}) h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; p}} \leqslant \delta_ {k}
$$

$$
\text {   for   all   } k \in \{1,..., n \} \text {   and   all   } p \in [ 1, \bar {p} ].
$$

## 10.4.2. Step 6. Estimate on$\varrho [ h ^ { n + 1 } ]$

This step is the first where we shall use the Vlasov equation. Starting from (8.4), we apply the method of characteristics to get, as in$\ S 8$

$$
h ^ {n + 1} (t, X _ {0, t} ^ {n} (x, v), V _ {0, t} ^ {n} (x, v)) = \int_ {0} ^ {t} \Sigma^ {n + 1} (\tau , X _ {0, \tau} ^ {n} (x, v), V _ {0, \tau} ^ {n} (x, v)) d \tau ,\tag{10.30}
$$

where

$$
\Sigma^ {n + 1} = - (F [ h ^ {n + 1} ] \cdot \nabla_ {v} f ^ {n} + F [ h ^ {n} ] \cdot \nabla_ {v} h ^ {n}).
$$

We compose this with$( X _ { t , 0 } ^ { n } , V _ { t , 0 } ^ { n } )$and apply (5.2) to get

$$
h ^ {n + 1} (t, x, v) = \int_ {0} ^ {t} \Sigma^ {n + 1} (\tau , X _ {t, \tau} ^ {n} (x, v), V _ {t, \tau} ^ {n} (x, v)) d \tau ,
$$

and$\mathrm { s o . }$, by integration in the v variable,

$$
\begin{array}{c} \varrho [ h ^ {n + 1} ] (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} \Sigma^ {n + 1} (\tau , X _ {t, \tau} ^ {n} (x, v), V _ {t, \tau} ^ {n} (x, v))   d v   d \tau \\ = - \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} (R _ {\tau , t} ^ {n + 1} \cdot G _ {\tau , t} ^ {n}) (x - v (t - \tau), v)   d v   d \tau \\ - \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} (R _ {\tau , t} ^ {n} \cdot H _ {\tau , t} ^ {n}) (x - v (t - \tau), v)   d v   d \tau , \end{array}\tag{10.31}
$$

where (with a slight inconsistency in the notation)

$$
\left\{ \begin{array}{l l} R _ {\tau , t} ^ {n + 1} = F [ h ^ {n + 1} ] \circ \Omega_ {t, \tau} ^ {n}, & R _ {\tau , t} ^ {n} = F [ h ^ {n} ] \circ \Omega_ {t, \tau} ^ {n}, \\ G _ {\tau , t} ^ {n} = (\nabla_ {v} f ^ {n}) \circ \Omega_ {t, \tau} ^ {n}, & H _ {\tau , t} ^ {n} = (\nabla_ {v} h ^ {n}) \circ \Omega_ {t, \tau} ^ {n}. \end{array} \right.\tag{10.32}
$$

Since the free transport semigroup and$\Omega _ { t , \tau } ^ { n }$are measure-preserving, for all$0 \leqslant \tau \leqslant t$ we have

$$
\begin{array}{l} \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} (R _ {\tau , t} ^ {n + 1} \cdot G _ {\tau , t} ^ {n}) (x - v (t - \tau), v) d v d x = \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} R _ {\tau , t} ^ {n + 1} \cdot G _ {\tau , t} ^ {n} d v d x \\ \qquad = \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} F [ h ^ {n + 1} ] \cdot \nabla_ {v} f ^ {n} d v d x \\ \qquad = \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} \nabla_ {v} \cdot (F [ h ^ {n + 1} ] f ^ {n}) d v d x \\ \qquad = 0, \end{array}
$$

and similarly

$$
\int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} (R _ {\tau , t} ^ {n} \cdot H _ {\tau , t} ^ {n}) (x - v (t - \tau), v) d v d x = 0 \quad \text {for all} 0 \leqslant \tau \leqslant t.
$$

This will allow us to apply the inequalities from$\ S 6$

Substep a. Let us first deal with the source term

$$
\sigma^ {n, n} (t, x) := \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} (R _ {\tau , t} ^ {n} \cdot H _ {\tau , t} ^ {n}) (x - v (t - \tau), v) d v d \tau .\tag{10.33}
$$

By Proposition 6.2,

$$
\| \sigma^ {n, n} (t, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant \int_ {0} ^ {t} \| R _ {\tau , t} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \| H _ {\tau , t} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} d \tau .\tag{10.34}
$$

On the one hand, we have from Step 5 that

$$
\left\| H _ {\tau , t} ^ {n} \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \leqslant 2 (1 + \tau) \delta_ {n}.
$$

On the other hand, under condition$\bf ( C _ { 1 } )$, we may apply Proposition 4.25 (with $\sigma { = } 0 )$to get

$$
\left\| R _ {\tau , t} ^ {n} \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \left\| F [ h _ {\tau} ^ {n} ] \right\| _ {\mathcal {F} ^ {\nu_ {n}}},
$$

where

$$
\begin{array}{c} \nu_ {n} (t, \tau) = \mu_ {n} ^ {*} + \lambda_ {n} ^ {*} (1 + b) \bigg | \tau - \frac {b t}{1 + b} \bigg | + \| \Omega^ {n} X _ {t, \tau} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \\ \leqslant \mu_ {n} ^ {*} + \lambda_ {n} ^ {*} (1 + b) \bigg | \tau - \frac {b t}{1 + b} \bigg | + 2 \mathcal {R} _ {2} ^ {n} (\tau , t). \end{array}
$$

Proceeding as in Step 1 (treating small times separately), we deduce that

$$
\begin{array}{r l} & {\| R _ {\tau , t} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant \| F [ h _ {\tau} ^ {n} ] \| _ {\mathcal {F} ^ {\nu_ {n}}} \leqslant e ^ {- 2 \pi (\lambda_ {n} - \lambda_ {n} ^ {*}) \tau} \| F [ h _ {\tau} ^ {n} ] \| _ {\mathcal {F} ^ {\bar {\nu} _ {n}}}} \\ & {\qquad \leqslant C _ {F} e ^ {- 2 \pi (\lambda_ {n} - \lambda_ {n} ^ {*}) \tau} \| \varrho [ h _ {\tau} ^ {n} ] \| _ {\mathcal {F} ^ {\bar {\nu} _ {n}}} \leqslant C _ {F} e ^ {- 2 \pi (\lambda_ {n} - \lambda_ {n} ^ {*}) \tau} \delta_ {n},} \end{array}
$$

with

$$
\bar {\nu} _ {n} (\tau , t) := \left\{ \begin{array}{l l} \mu^ {\sharp}, & \text {when 0\leqslant\tau\leqslant\frac{bt}{1 + b}}, \\ \lambda_ {n} \tau + \mu_ {n}, & \text {when \tau\geqslant\frac{bt}{1 + b}}. \end{array} \right.\tag{10.35}
$$

(We have used the gradient structure of the force to convert (gliding) regularity into decay.) Thus

$$
\begin{array}{r l r} & & {\int_ {0} ^ {t} \| R _ {\tau , t} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \| H _ {\tau , t} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} d \tau \leqslant 2 C _ {F} \delta_ {n} ^ {2} \int_ {0} ^ {t} e ^ {- 2 \pi (\lambda_ {n} - \lambda_ {n} ^ {*}) \tau} (1 + \tau) d \tau} \\ & & {\leqslant \frac {2 C _ {F} \delta_ {n} ^ {2}}{(\pi (\lambda_ {n} - \lambda_ {n} ^ {*})) ^ {2}}.} \end{array}\tag{10.36}
$$

(Note that this is the power$2$which is responsible for the very fast convergence of the Newton scheme.)

Substep b. Now let us handle the term

$$
\sigma^ {n, n + 1} (t, x) := \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} \left(R _ {\tau , t} ^ {n + 1} \cdot G _ {\tau , t} ^ {n}\right) (x - v (t - \tau), v) d v d \tau .\tag{10.37}
$$

This is the focal point of all our analysis, because it is in this term that the self-consistent nature of the Vlasov equation appears. In particular, we will make crucial use of the time-cheating trick to overcome the loss of regularity implied by composition; and also the other bilinear estimates (regularity extortion) from$^ { \ S 6 , }$as well as the time-response study from$\ S 7 .$. Particular care should be given to the zero spatial mode of$G ^ { n }$, which is associated with instantaneous response (no echo). In the linearized equation we did not see this problem because the contribution of the zero mode was vanishing!

We start by introducing

$$
\overline {{G}} _ {\tau , t} ^ {n} = \nabla_ {v} f ^ {0} + \sum_ {k = 1} ^ {n} \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}),\tag{10.38}
$$

and we decompose$\sigma ^ { n , n + 1 }$as

$$
\sigma^ {n, n + 1} = \bar {\sigma} ^ {n, n + 1} + \mathcal {E} + \bar {\mathcal {E}},\tag{10.39}
$$

where

$$
\overline {{\sigma}} ^ {n, n + 1} (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} F [ h _ {\tau} ^ {n + 1} ] \cdot \overline {{G}} _ {\tau , t} ^ {n} (x - v (t - \tau), v) d v d \tau\tag{10.40}
$$

and the error terms$\mathcal { E }$and$\bar { \mathcal { E } }$are defined by

$$
\mathcal {E} (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} ((F [ h _ {\tau} ^ {n + 1} ] \circ \Omega_ {t, \tau} ^ {n} - F [ h _ {\tau} ^ {n + 1} ]) \cdot G ^ {n}) (\tau , x - v (t - \tau), v) d v d \tau ,\tag{10.41}
$$

$$
\overline {{\mathcal {E}}} (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} (F [ h _ {\tau} ^ {n + 1} ] \cdot (G ^ {n} - \overline {{G}} ^ {n})) (\tau , x - v (t - \tau), v) d v d \tau .\tag{10.42}
$$

We shall first estimate$\mathcal { E }$and${ \bar { \mathcal { E } } } .$

Control of$\varepsilon .$This is based on the time-cheating trick from$\ S 6 ,$, and the regularity of the force. By Proposition 6.2,

$$
\left\| \mathcal {E} (t, \cdot) \right\| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant \int_ {0} ^ {t} \left\| F [ h _ {\tau} ^ {n + 1} ] \circ \Omega_ {t, \tau} ^ {n} - F [ h _ {\tau} ^ {n + 1} ] \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \left\| G ^ {n} \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} d \tau .\tag{10.43}
$$

From (10.1) and Step 5,

$$
\begin{array}{l} \| G ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \leqslant \| \nabla_ {v} f ^ {0} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} + \sum_ {k = 1} ^ {n} \| \nabla_ {v} h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \\ \leqslant C _ {0} ^ {\prime} + \biggl (\sum_ {k = 1} ^ {n} \delta_ {k} \biggr) (1 + \tau), \end{array}\tag{10.44}
$$

where$C _ { 0 } ^ { \prime }$comes from the contribution of$f ^ { 0 }$.

Next, by Propositions 4.24 and 4.25 (with$V { = } 0 , \tau { = } \sigma$and$b { = } 0 )$),

$$
\begin{array}{l} \| F [ h _ {\tau} ^ {n + 1} ] \circ \Omega_ {t, \tau} ^ {n} - F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \\ \leqslant \| \Omega_ {t, \tau} ^ {n} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \int_ {0} ^ {1} \| \nabla F [ h _ {\tau} ^ {n + 1} ] \circ (\mathrm{Id} + \theta (\Omega_ {t, \tau} ^ {n} - \mathrm{Id})) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} d \theta \\ \leqslant \| \nabla F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\nu_ {n}}} \| \Omega_ {t, \tau} ^ {n} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}, \end{array}\tag{10.45}
$$

where

$$
\nu_ {n} = \mu_ {n} ^ {*} + \lambda_ {n} ^ {*} (1 + b) \left| \tau - \frac {b t}{1 + b} \right| + \| \Omega^ {n} X _ {t, \tau} - x \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}.
$$

Small times are taken care of, as usual, by the initial regularity layer, so we only focus on the case$\tau \geqslant b t / ( 1 + b )$; then

$$
\begin{array}{l} \nu_ {n} \leqslant \lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*} - \lambda_ {n} ^ {*} b (t - \tau) + 2 \mathcal {R} ^ {n} (\tau , t) \\ \leqslant \lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*} - \lambda_ {n} ^ {*} \frac {B (t - \tau)}{1 + t} + 4 C _ {\omega} ^ {1} \bigg (\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {3}} \bigg) \frac {\min \{t - \tau , 1 \}}{1 + \tau}. \end{array}
$$

To make sure that$\nu _ { n } \leqslant \lambda _ { n } ^ { * } \tau + \mu _ { n } ^ { * }$, we assume that

$$
4 C _ {\omega} ^ {1} \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {3}} \leqslant \frac {\lambda_ {\infty} ^ {*} B}{3},\tag{\( (\mathbf{C}_{6}) \}
$$

and we note that

$$
\frac {\min \{t - \tau , 1 \}}{1 + \tau} \leqslant 3 \frac {t - \tau}{1 + t}.
$$

(This is easily seen by separating four cases: (a)$t \leqslant 2$, (b)$t \geqslant 2$and$t - \tau { \leqslant } 1$, (c)$t \geqslant 2$, $t - \tau \geqslant 1$and$\tau \leqslant { \frac { 1 } { 2 } } t$, (d) t-2,$t - \tau \geqslant 1$and$\tau \geqslant \frac { 1 } { 2 } t . )$

Then, since$\gamma \geqslant 1$, we have

$$
\begin{array}{r l} & {\| \nabla F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\nu_ {n}}} \leqslant \| \nabla F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}}} \\ & {\qquad \leqslant \| F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*} \cdot \gamma}} \leqslant C _ {F} \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}}.} \end{array}\tag{10.46}
$$

(Note that applying Proposition 4.10 instead of the regularity coming from the interaction would consume more regularity than we can aford to.)

Plugging this back into (10.45), we get

$$
\begin{array}{r l} & {\| F [ h _ {\tau} ^ {n + 1} ] \circ \Omega_ {t, \tau} ^ {n} - F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}} \\ & {\qquad \leqslant 2 \mathcal {R} ^ {n} (\tau , t) C _ {F} \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}}} \\ & {\qquad \leqslant 2 C _ {\omega} ^ {3} C _ {F} \bigg (\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {5}} \bigg) \frac {1}{(1 + \tau) ^ {3}} \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}}.} \end{array}
$$

Recalling (10.41) and (10.44), applying Proposition 4.24, we conclude that

$$
\begin{array}{l} \| \mathcal {E} (t, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \\ \leqslant 2 C _ {\omega} ^ {3} C _ {F} \bigg (C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \left(\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {5}}\right) \int_ {0} ^ {t} \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}} \frac {d \tau}{(1 + \tau) ^ {2}}. \end{array}\tag{10.47}
$$

(We could be a bit more precise; anyway we cannot go further since we do not yet have an estimate on$\varrho [ h ^ { n + 1 } ]$. Recall that the latter quantity has zero mean, so the$\mathcal { F }$norm above could be replaced by a$\dot { \mathcal { F } }$norm.)

Control of$\bar { \mathcal { E } } .$This will use the control on the derivatives of$h ^ { k }$. We start again from Proposition 6.2,

$$
\| \overline {{\mathcal {E}}} (t, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant \int_ {0} ^ {t} \| G ^ {n} - \overline {{G}} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \| F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\beta_ {n}}} d \tau ,\tag{10.48}
$$

where

$$
\beta_ {n} = \lambda_ {n} ^ {*} (1 + b) \left| \tau - \frac {b t}{1 + b} \right| + \mu_ {n} ^ {*}.
$$

We focus again on the case$\tau \geqslant b t / ( 1 + b )$, so that (with crude estimates)

$$
\| F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\beta_ {n}}} \leqslant \| F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}} \leqslant C _ {F} \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}},
$$

and the problem is to control$G ^ { n } - \overline { { G } } ^ { n }$

$$
\begin{array}{l} \| G ^ {n} - \overline {{G}} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \leqslant \| (\nabla_ {v} f ^ {0}) \circ \Omega_ {t, \tau} ^ {n} - \nabla_ {v} f ^ {0} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \\ \qquad + \sum_ {k = 1} ^ {n} \| (\nabla_ {v} h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {n} - (\nabla_ {v} h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \\ \qquad + \sum_ {k = 1} ^ {n} \| (\nabla_ {v} h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {k - 1} - \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}}. \end{array}\tag{10.49}
$$

By induction hypothesis$( \widetilde { \mathbf { E } } _ { \mathbf { h } } ^ { \mathbf { n } } )$, and since the$\mathcal { Z } _ { \tau } ^ { \lambda , \mu }$norms are increasing as a function of$\lambda$and$\mu ,$

$$
\sum_ {k = 1} ^ {n} \| (\nabla_ {v} h _ {\tau} ^ {k}) \circ \Omega_ {t, \tau} ^ {k - 1} - \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \leqslant \left(\sum_ {k = 1} ^ {n} \delta_ {k}\right) \frac {1}{(1 + \tau) ^ {2}}.
$$

It remains to treat the first and second terms in the right-hand side of (10.49). This is done by inversion/composition as in Step$5 ;$let us consider for instance the contribution of$h ^ { k } , k \geqslant 1$,

$$
\begin{array}{l} \| \nabla_ {v} h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {n} - \nabla_ {v} h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \\ \leqslant \int_ {0} ^ {1} \| \nabla \nabla_ {v} h _ {\tau} ^ {k} \circ ((1 - \theta) \Omega_ {t, \tau} ^ {n} + \theta \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \| \Omega_ {t, \tau} ^ {n} - \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} d \theta \\ \leqslant 2 \| \nabla \nabla_ {v} h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} ^ {*} (1 + b), \mu_ {k} ^ {*}; 1}} \| \Omega_ {t, \tau} ^ {n} - \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \\ \leqslant 4 \delta_ {k} (1 + \tau) ^ {2} \mathcal {R} ^ {k - 1, n} (\tau , t) \\ \leqslant 4 C _ {\omega} ^ {4} \delta_ {k} \left(\sum_ {j = k} ^ {n} \frac {\delta_ {j}}{(2 \pi (\lambda_ {j} - \lambda_ {j} ^ {*})) ^ {6}}\right) \frac {1}{(1 + \tau) ^ {2}}, \end{array}
$$

where in the second-last step we used$( \widetilde { \mathbf { E } } _ { \Omega } ^ { \mathbf { n } } ) , \ ( \widetilde { \mathbf { E } } _ { \varrho } ^ { \mathbf { n } } )$, Propositions 4.24 and 4.28, condition$\bf ( C _ { 5 } )$!and the same reasoning as in Step 5.

Summing up all contributions and inserting into (10.48) yields

$$
\begin{array}{l} \| \overline {{\mathcal {E}}} (t, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant 4 C _ {F} \bigg [ C _ {\omega} ^ {4} \bigg (C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \bigg (\sum_ {j = 1} ^ {n} \frac {\delta_ {j}}{(2 \pi (\lambda_ {j} - \lambda_ {n} ^ {*})) ^ {6}} \bigg) + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg ] \\ \times \int_ {0} ^ {t} \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}} \frac {d \tau}{(1 + \tau) ^ {2}}. \end{array}\tag{10.50}
$$

Main contribution. Now we consider$\bar { \sigma } ^ { n , n + 1 }$<sup>1</sup>, which we decompose as

$$
\overline {{\sigma}} _ {t} ^ {n, n + 1} = \overline {{\sigma}} _ {t, 0} ^ {n, n + 1} + \sum_ {k = 1} ^ {n} \overline {{\sigma}} _ {t, k} ^ {n, n + 1},
$$

where

$$
\begin{array}{r l} & {\bar {\sigma} _ {t, 0} ^ {n, n + 1} (x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} F [ h ^ {n + 1} ] (\tau , x - v (t - \tau), v) \cdot \nabla_ {v} f ^ {0} (v) d v d \tau ,} \\ & {\bar {\sigma} _ {t, k} ^ {n, n + 1} (x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} (F [ h _ {\tau} ^ {n + 1} ] \cdot \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1})) (\tau , x - v (t - \tau), v) d v d \tau .} \end{array}
$$

Note that their zero modes vanish. For any$k \geqslant 1$, we apply Theorem 6.5 (with$M { = } 1 )$to get

$$
\| \overline {{\sigma}} _ {t, k} ^ {n, n + 1} \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant \int_ {0} ^ {t} K _ {1} ^ {n, h ^ {k}} (t, \tau) \| F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\nu_ {n} ^ {\prime}, \gamma}} d \tau + \int_ {0} ^ {t} K _ {0} ^ {n, h ^ {k}} (t, \tau) \| F [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\nu_ {n} ^ {\prime}, \gamma}} d \tau ,
$$

where

$$
\nu_ {n} ^ {\prime} = \lambda_ {n} ^ {*} (1 + b) \left| \tau - \frac {b t}{1 + b} \right| + \mu_ {n} ^ {\prime}
$$

and

$$
\begin{array}{l} K _ {1} ^ {n, h ^ {k}} (t, \tau) = K _ {1} ^ {n, k} (t, \tau) \sup _ {0 \leqslant s \leqslant t} \frac {\| \nabla_ {v} (h _ {s} ^ {k} \circ \Omega_ {t , s} ^ {k - 1}) - \langle \nabla_ {v} (h _ {s} ^ {k} \circ \Omega_ {t , s} ^ {k - 1}) \rangle \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {\lambda_ {k} (1 + b) , \mu_ {k}}}}{1 + s}, \\ K _ {1} ^ {n, k} (t, \tau) = (1 + \tau) d \sup _ {l, m \in \mathbb {Z} _ {*} ^ {d}} e ^ {- \pi (\mu_ {k} - \mu_ {n} ^ {*}) | m |} \frac {e ^ {- 2 \pi (\mu_ {n} ^ {\prime} - \mu_ {n} ^ {*}) | l - m |}}{1 + | l - m | ^ {\gamma}} e ^ {- \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) | l (t - \tau) + m \tau |}, \\ K _ {0} ^ {n, h ^ {k}} (t, \tau) = K _ {0} ^ {n, k} (t, \tau) \sup _ {0 \leqslant s \leqslant t} \| \nabla_ {v} \langle h _ {s} ^ {k} \circ \Omega_ {t, s} ^ {k - 1} \rangle \| _ {\mathcal {C} ^ {\lambda_ {k} (1 + b); 1}}, \\ K _ {0} ^ {n, k} (t, \tau) = d e ^ {- \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) (t - \tau)}. \end{array}
$$

We assume that

$$
\mu_ {n} ^ {\prime} = \mu_ {n} ^ {*} + \eta \left(\frac {t - \tau}{1 + t}\right), \quad \eta > 0 \text {   small },\tag{10.51}
$$

and check that$\nu _ { n } ^ { \prime } \leqslant \lambda _ { n } ^ { * } \tau + \mu _ { n } ^ { * }$. Leaving apart the small-time case, we assume$\tau { \geqslant } b t / ( 1 { + } b )$, so that

$$
\nu_ {n} ^ {\prime} = (\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}) - \frac {B \lambda_ {n} ^ {*} (t - \tau)}{1 + t} + \eta \left(\frac {t - \tau}{1 + t}\right),
$$

which is indeed bounded above by$\lambda _ { n } ^ { * } \tau + \mu _ { n } ^ { * }$as soon as

$$
\eta \leqslant B \lambda_ {\infty} ^ {*}.\tag{10.52}
$$

Then, with the notation (7.10),

$$
K _ {1} ^ {n, k} (t, \tau) \leqslant K _ {1} ^ {(\alpha_ {n, k}), \gamma} (t, \tau),\tag{10.53}
$$

with

$$
\alpha_ {n, k} = \pi \min \{\mu_ {k} - \mu_ {n} ^ {*}, \lambda_ {k} - \lambda_ {n} ^ {*}, 2 \eta \}.\tag{10.54}
$$

From the controls on$h ^ { k }$(assumption$( \widetilde { \mathbf { E } } _ { \mathbf { h } } ^ { \mathbf { n } } ) )$we have that

$$
\| \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) - \langle \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \rangle \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; 1}} \leqslant \| \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b), \mu_ {k}; 1}} \leqslant \delta_ {k} (1 + \tau)
$$

and

$$
\begin{array}{c} \| \langle \nabla_ {v} (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \rangle \| _ {\mathcal {C} ^ {\lambda_ {k} (1 + b); 1}} = \| \langle (\nabla_ {v} + \tau \nabla_ {x}) (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \rangle \| _ {\mathcal {C} ^ {\lambda_ {k} (1 + b); 1}} \\ \leqslant \| (\nabla_ {v} + \tau \nabla_ {x}) (h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {k} (1 + b); 1}} \leqslant \delta_ {k}. \end{array}
$$

After controlling$F [ h ^ { n + 1 } ]$by$\varrho [ h ^ { n + 1 } ]$, we end up with

$$
\begin{array}{r l} & {\| \overline {{\sigma}} _ {t, k} ^ {n, n + 1} \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant C _ {F} \int_ {0} ^ {t} \bigg (\sum_ {k = 1} ^ {n} \delta_ {k} K _ {1} ^ {(\alpha_ {n, k}), \gamma} (t, \tau) \bigg) \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}} d \tau} \\ & {\qquad + C _ {F} \int_ {0} ^ {t} \bigg (\sum_ {k = 1} ^ {n} \delta_ {k} e ^ {- \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) (t - \tau)} \bigg) \| \varrho [ h _ {\tau} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}} d \tau ,} \end{array}\tag{10.55}
$$

with$\alpha _ { n , k }$defined by (10.54).

Substep c. Gathering all previous controls, we obtain the following integral inequality for$\scriptstyle \varphi = \varrho [ h ^ { n + 1 } ]$:

$$
\begin{array}{r l} & {\left\| \varphi (t, x) - \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} (\nabla W * \varphi) (\tau , x - v (t - \tau)) \cdot \nabla_ {v} f ^ {0} (v) d v d \tau \right\| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}}} \\ & {\qquad \leqslant A _ {n} + \int_ {0} ^ {t} \bigg (K _ {1} ^ {n} (t, \tau) + K _ {0} ^ {n} (t, \tau) + \frac {c _ {0} ^ {n}}{(1 + \tau) ^ {2}} \bigg) \| \varphi (\tau , \cdot) \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} \tau + \mu_ {n} ^ {*}}} d \tau ,} \end{array}\tag{10.56}
$$

where, by (10.36), (10.47) and (10.50),

$$
\begin{array}{c} A _ {n} = \sup _ {t \geqslant 0} \| \sigma^ {n, n} (t, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant \frac {2 C _ {F} \delta_ {n} ^ {2}}{(\pi (\lambda_ {n} - \lambda_ {n} ^ {*})) ^ {2}}, \\ K _ {1} ^ {n} (t, \tau) = \bigg (C _ {F} \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) K _ {1} ^ {(\alpha_ {n}), \gamma} (t, \tau), \\ \alpha_ {n} = \alpha_ {n, n} = \pi \min \{(\mu_ {n} - \mu_ {n} ^ {*}), (\lambda_ {n} - \lambda_ {n} ^ {*}), 2 \eta \}, \\ K _ {0} ^ {n} (t, \tau) = C _ {F} \sum_ {k = 1} ^ {n} \delta_ {k} e ^ {- \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) (t - \tau)}, \\ c _ {0} ^ {n} = 3 C _ {F} C _ {\omega} ^ {4} \bigg (C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \bigg (\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {6}} \bigg) + \sum_ {k = 1} ^ {n} \delta_ {k}. \end{array}\tag{10.57}
$$

(We are cheating a bit when writing (10.56), because in fact one should take into account small times separately; but this does not cause any dificulty.)

We easily estimate$K _ { 0 } ^ { n }$:

$$
\begin{array}{c} \int_ {0} ^ {t} K _ {0} ^ {n} (t, \tau) d \tau \leqslant C _ {F} \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\pi (\lambda_ {k} - \lambda_ {n} ^ {*})}, \\ \int_ {\tau} ^ {\infty} K _ {0} ^ {n} (t, \tau) d t \leqslant C _ {F} \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\pi (\lambda_ {k} - \lambda_ {n} ^ {*})}, \\ \left(\int_ {0} ^ {t} K _ {0} ^ {n} (t, \tau) ^ {2} d \tau\right) ^ {1 / 2} \leqslant C _ {F} \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\sqrt {2 \pi (\lambda_ {k} - \lambda_ {n} ^ {*})}}. \end{array}
$$

Let us assume that$\alpha _ { n }$is smaller than$\overline { { \alpha } } ( \gamma )$appearing in Theorem$7 . 7 ,$and that

$$
3 C _ {F} C _ {\omega} ^ {4} \left(C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} + 1\right) \left(\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {6}}\right) \leqslant \frac {1}{4},\tag{\( (\mathbf{C}_{7}) \}
$$

$$
C _ {F} \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\sqrt {2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})}} \leqslant \frac {1}{2},\tag{\( (\mathbf{C}_{8}) \}
$$

$$
C _ {F} \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\pi (\lambda_ {k} - \lambda_ {k} ^ {*})} \leqslant \max \biggl \{\frac {1}{4}, \chi \biggr \},\tag{\( (\mathbf{C}_{9}) \}
$$

(note that in these conditions we have strenghtened the inequalities by replacing$\lambda _ { k } - \lambda _ { n } ^ { * }$ by$\lambda _ { k } - \lambda _ { k } ^ { * }$where$\chi > 0$is also defined by Theorem 7.7). Applying Theorem 7.7 with $\lambda _ { 0 } = \lambda$and$\lambda ^ { * } { = } \lambda _ { 1 }$, we deduce that for any$\varepsilon \in ( 0 , \alpha _ { n } )$and$t \geqslant 0$,

$$
\| \varrho_ {t} ^ {n + 1} \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}} \leqslant C A _ {n} \frac {(1 + c _ {0} ^ {n}) ^ {2}}{\sqrt {\varepsilon}} e ^ {C c _ {0} ^ {n}} \left(1 + \frac {c _ {n}}{\alpha_ {n} \varepsilon}\right) e ^ {C T _ {\varepsilon , n}} e ^ {C c _ {n} (1 + T _ {\varepsilon , n} ^ {2})} e ^ {\varepsilon t},\tag{10.58}
$$

where

$$
c _ {n} = 2 C _ {F} \sum_ {k = 1} ^ {n} \delta_ {k}
$$

and

$$
T _ {\varepsilon , n} = C _ {\gamma} \max \biggl \{\left(\frac {c _ {n} ^ {2}}{\alpha_ {n} ^ {5} \varepsilon^ {2 + \gamma}}\right) ^ {1 / (\gamma - 1)}, \left(\frac {c _ {n}}{\alpha_ {n} ^ {2} \varepsilon^ {\gamma + 1 / 2}}\right) ^ {1 / (\gamma - 1)}, \frac {(c _ {0} ^ {n}) ^ {2 / 3}}{\varepsilon^ {1 / 3}} \biggr \}.
$$

Pick up${ \lambda } _ { n } ^ { \dagger } < { \lambda } _ { n } ^ { * }$such that$2 \pi ( \lambda _ { n } ^ { * } - \lambda _ { n } ^ { \dagger } ) \leqslant \alpha _ { n }$, and choose$\varepsilon { = } 2 \pi ( \lambda _ { n } ^ { * } { - } \lambda _ { n } ^ { \dagger } )$; recalling that $\hat { \varrho } ^ { n + 1 } ( t , 0 ) = 0$, and that our conditions imply an upper bound on$c _ { n }$and$c _ { 0 } ^ { n }$, we deduce the uniform control

$$
\begin{array}{r l} & {\| \varrho_ {t} ^ {n + 1} \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {\dagger} t + \mu_ {n} ^ {*}}} \leqslant e ^ {- 2 \pi (\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\dagger}) t} \| \varrho_ {t} ^ {n + 1} \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}}}} \\ & {\quad \leqslant C A _ {n} \bigg (1 + \frac {1}{\alpha_ {n} (\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\dagger}) ^ {3 / 2}} \bigg) e ^ {C T _ {n} ^ {2}},} \end{array}\tag{10.59}
$$

where

$$
T _ {n} = C \bigg (\frac {1}{\alpha_ {n} ^ {5} (\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\dagger}) ^ {2 + \gamma}} \bigg) ^ {1 / (\gamma - 1)}.\tag{10.60}
$$

## 10.4.3. Step 7. Estimate on$F [ h ^ { n + 1 } ]$

As an immediate consequence of (10.2) and (10.59), we have

$$
\sup _ {t \geqslant 0} \| F [ \varrho_ {t} ^ {n + 1} ] \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {\dagger} t + \mu_ {n} ^ {*}, \gamma}} \leqslant C A _ {n} \left(1 + \frac {1}{\alpha_ {n} (\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\dagger}) ^ {3 / 2}}\right) e ^ {C T _ {n} ^ {2}}.\tag{10.61}
$$

## 10.4.4. Step 8. Estimate of$h ^ { n + 1 } \circ \Omega ^ { n }$

In this step we shall again use the Vlasov equation. We rewrite (10.30) as

$$
h ^ {n + 1} (\tau , X _ {0, \tau} ^ {n} (x, v), V _ {0, \tau} ^ {n} (x, v)) = \int_ {0} ^ {\tau} \Sigma^ {n + 1} (s, X _ {0, s} ^ {n} (x, v), V _ {0, s} ^ {n} (x, v)) d s;
$$

but now we compose with$( X _ { t , 0 } ^ { n } , V _ { t , 0 } ^ { n } )$, where$t \geqslant \tau$is arbitrary. This gives

$$
h ^ {n + 1} (\tau , X _ {t, \tau} ^ {n} (x, v), V _ {t, \tau} ^ {n} (x, v)) = \int_ {0} ^ {\tau} \Sigma^ {n + 1} (s, X _ {t, s} ^ {n} (x, v), V _ {t, s} ^ {n} (x, v)) d s.
$$

Then for any$p \in [ 1 , \bar { p } ]$and${ \lambda } _ { n } ^ { \flat } < { \lambda } _ { n } ^ { \dagger }$, using Propositions 4.19 and 4.24, and the notation (10.32), we get

$$
\begin{array}{r l} & {\| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}; p}} = \| h _ {\tau} ^ {n + 1} \circ (X _ {t, \tau} ^ {n}, V _ {t, \tau} ^ {n}) \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}; p}}} \\ & {\qquad \leqslant \int_ {0} ^ {\tau} \| \Sigma^ {n + 1} (s, X _ {t, s} ^ {n}, V _ {t, s} ^ {n}) \| _ {\mathcal {Z} _ {t - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}; p}} d s} \\ & {\qquad = \int_ {0} ^ {\tau} \| \Sigma^ {n + 1} (s, \Omega_ {t, s} ^ {n}) \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}; p}} d s} \\ & \qquad \leqslant \int_ {0} ^ {\tau} \| R _ {s, t} ^ {n + 1} \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}} \| G _ {s, t} ^ {n} \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}; p}} d s} \\ & \qquad + \int_ {0} ^ {\tau} \| R _ {s, t} ^ {n} \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}} \| H _ {s, t} ^ {n} \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}; p}} d s.} \end{array}
$$

Then (proceeding as in Step 6 to check that the exponents lie in the appropriate range)

$$
\| R _ {s, t} ^ {n + 1} \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}}} \leqslant C _ {F} e ^ {- 2 \pi (\lambda_ {n} ^ {\dagger} - \lambda_ {n} ^ {\flat}) s} \| \varrho_ {s} ^ {n + 1} \| _ {\mathcal {F} ^ {\bar {\nu} _ {n} (s)}}
$$

and

$$
\| R _ {s, t} ^ {n} \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda^ {b}, \mu_ {n} ^ {*}}} \leqslant C _ {F} e ^ {- 2 \pi (\lambda_ {n} ^ {\dagger} - \lambda_ {n} ^ {b}) s} \| \varrho_ {s} ^ {n} \| _ {\mathcal {F} ^ {\bar {\nu} _ {n} (s)}} \leqslant C _ {F} e ^ {- 2 \pi (\lambda_ {n} ^ {\dagger} - \lambda_ {n} ^ {b}) s} \delta_ {n},
$$

with

$$
\bar {\nu} _ {n} (s, t) := \left\{ \begin{array}{l l} \mu^ {\sharp}, & \text {when s\leqslant\frac {bt}{1 + b}}, \\ \lambda_ {n} ^ {\dagger} s + \mu_ {n} ^ {*}, & \text {when s\geqslant\frac {bt}{1 + b}}. \end{array} \right.
$$

On the other hand, from the induction assumption$( \bf E _ { h } ^ { n } ) - ( \bf \widetilde E _ { h } ^ { n } )$(and again control of composition via Proposition 4.25),

$$
\left\| H _ {s, t} ^ {n} \right\| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}, \mu_ {n} ^ {*}; p}} \leqslant 2 (1 + s) \delta_ {n}
$$

and

$$
\left\| G _ {s, t} ^ {n} \right\| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {b}, \mu_ {n} ^ {*}; p}} \leqslant 2 (1 + s) \sum_ {k = 1} ^ {n} \delta_ {k}.
$$

We deduce that

$$
y (t, \tau) := \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {b}, \mu_ {n} ^ {*}; p}}
$$

satisfies

$$
\begin{array}{l} y (t, \tau) \leqslant 2 C _ {F} \bigg (\sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \int_ {0} ^ {\tau} e ^ {- 2 \pi (\lambda_ {n} ^ {\dagger} - \lambda_ {n} ^ {\flat}) s} \| \varrho_ {s} ^ {n + 1} \| _ {\mathcal {F} ^ {\tilde {\nu} _ {n} (s)}} (1 + s) d s \\ \qquad + 2 C _ {F} \delta_ {n} ^ {2} \int_ {0} ^ {\tau} e ^ {- 2 \pi (\lambda_ {n} ^ {\dagger} - \lambda_ {n} ^ {\flat}) s} (1 + s) d s; \end{array}
$$

so, for all$0 \leqslant \tau \leqslant t$

$$
\| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {(1 + b) \lambda_ {n} ^ {\flat}; \mu_ {n} ^ {*}; p}} \leqslant \frac {4 C _ {F} \max \{\sum_ {k = 1} ^ {n} \delta_ {k} , 1 \}}{(2 \pi (\lambda_ {n} ^ {\dagger} - \lambda_ {n} ^ {\flat})) ^ {2}} \Bigl (\delta_ {n} ^ {2} + \sup _ {s \geqslant 0} \| \varrho_ {s} ^ {n + 1} \| _ {\mathcal {F} ^ {\nu_ {n} (s)}} \Bigr).\tag{10.62}
$$

## 10.4.5. Step 9. Crude estimates on the derivatives of$\scriptstyle h ^ { n + 1 }$

Again we choose$p \in [ 1 , \bar { p } ]$. From the previous step and Proposition 4.27 we deduce, for any$\lambda _ { n } ^ { \ddag }$such that$\lambda _ { n } ^ { \ddag } < \lambda _ { n } ^ { \flat } < \lambda _ { n } ^ { \ddag }$, and any$\mu _ { n } ^ { \ddag } < \mu _ { n } ^ { * }$, that

$$
\begin{array}{r l} & {\| \nabla_ {x} (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; p}} + \| (\nabla_ {v} + \tau \nabla_ {x}) (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; p}}} \\ & {\qquad \leqslant \frac {C (d)}{\min \{\lambda_ {n} ^ {b} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \}} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {b} (1 + b), \mu_ {n} ^ {*}; p}}} \end{array}\tag{10.63}
$$

and

$$
\| \nabla (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; p}} \leqslant \frac {C (d) (1 + \tau)}{\min \{\lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \}} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\flat} (1 + b), \mu_ {n} ^ {*}; p}}.\tag{10.64}
$$

Similarly,

$$
\| \nabla \nabla (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; p}} \leqslant \frac {C (d) (1 + \tau) ^ {2}}{\min \{\lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \} ^ {2}} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\flat} (1 + b), \mu_ {n} ^ {*}; p}}.\tag{10.65}
$$

## 10.4.6. Step 10. Chain-rule and refined estimates on derivatives of$\scriptstyle h ^ { n + 1 }$

From Step 3 we have

$$
\| \nabla \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} + \| (\nabla \Omega_ {t, \tau} ^ {n}) ^ {- 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}} \leqslant C (d)\tag{10.66}
$$

and (via Proposition 4.27)

$$
\begin{array}{r l} & {\| \nabla \nabla \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}}} \leqslant \frac {C (d) (1 + \tau)}{\min \{\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \}} \| \nabla \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}} \\ & {\quad \leqslant \frac {C (d) (1 + \tau)}{\min \{\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \}}.} \end{array}\tag{10.67}
$$

Combining these bounds with Step 9, Proposition 4.24 and the identities

$$
\left\{ \begin{array}{l} (\nabla h) \circ \Omega = (\nabla \Omega) ^ {- 1} \nabla (h \circ \Omega), \\ (\nabla^ {2} h) \circ \Omega = (\nabla \Omega) ^ {- 2} \nabla^ {2} (h \circ \Omega) - (\nabla \Omega) ^ {- 1} \nabla^ {2} \Omega (\nabla \Omega) ^ {- 1} (\nabla h \circ \Omega), \end{array} \right.\tag{10.68}
$$

we get

$$
\begin{array}{l} \| (\nabla h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; 1}} \leqslant C (d) \| \nabla (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; 1}} \\ \leqslant \frac {C (d) (1 + \tau)}{\min \{\lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \}} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\flat} (1 + b), \mu_ {n} ^ {*}; 1}} \end{array}\tag{10.69}
$$

and

$$
\begin{array}{r l} & {\| (\nabla^ {2} h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; 1}}} \\ & {\quad \leqslant C (d) \Big [ \| \nabla^ {2} (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; 1}}} \\ & {\qquad + \| \nabla^ {2} \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; 1}} \| (\nabla h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; 1}} \Big ]} \\ & {\leqslant \frac {C (d) (1 + \tau) ^ {2}}{\min \{\lambda_ {n} ^ {b} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \} ^ {2}} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {b} (1 + b), \mu_ {n} ^ {*}; p}}.} \end{array}\tag{10.70}
$$

This gives us the bounds

$$
\| (\nabla h ^ {n + 1}) \circ \Omega^ {n} \| = O (1 + \tau) \quad \mathrm{and} \quad \| (\nabla^ {2} h ^ {n + 1}) \circ \Omega^ {n} \| = O ((1 + \tau) ^ {2}),
$$

which are optimal if one does not distinguish between the x and v variables. We shall now refine these estimates. We first write

$$
\nabla (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) - (\nabla h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} = \nabla (\Omega_ {t, \tau} ^ {n} - \mathrm{Id}) \cdot [ (\nabla h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} ],
$$

and we deduce (via Propositions 4.24 and 4.27)

$$
\begin{array}{l} \| \nabla (h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n}) - (\nabla h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; p}} \\ \leqslant \| \nabla (\Omega_ {t, \tau} ^ {n} - \mathrm{Id}) \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}}} \| (\nabla h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger} (1 + b), \mu_ {n} ^ {\ddagger}; p}} \\ \leqslant C (d) \left(\frac {1 + \tau}{\min \{\lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\dagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\dagger} \}}\right) ^ {2} \| \Omega_ {t, \tau} ^ {n} - \mathrm{Id} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\flat} (1 + b), \mu_ {n} ^ {*}}; p} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\flat} (1 + b), \mu_ {n} ^ {*}; p}} \\ \leqslant \frac {C (d) C _ {\omega} ^ {4}}{\min \{\lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\dagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\dagger} \} ^ {2}} \left(\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {6}}\right) (1 + \tau) ^ {- 2} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\flat} (1 + b), \mu_ {n} ^ {*}; p}}. \end{array} \tag {10.7}
$$

(Note that$\Omega ^ { n } - \operatorname { I d }$brings the time-decay, while$h ^ { n + 1 }$brings the smallness.)

This shows that$( \nabla h ^ { n + 1 } ) \circ \Omega ^ { n } { \simeq } \nabla ( h ^ { n + 1 } \circ \Omega ^ { n } )$as$\tau {  } \infty$. In view of Step 9, this also implies the refined gradient estimates

$$
\begin{array}{r l r} & & {\| (\nabla_ {x} h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger}, \mu_ {n} ^ {\ddagger}; p}} + \| ((\nabla_ {v} + \tau \nabla_ {x}) h _ {\tau} ^ {n + 1}) \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\ddagger}, \mu_ {n} ^ {\ddagger}; p}}} \\ & & {\leqslant \overline {{C}} \| h _ {\tau} ^ {n + 1} \circ \Omega_ {t, \tau} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {\flat} (1 + b), \mu_ {n} ^ {*}; p}},} \end{array}\tag{10.72}
$$

with

$$
\overline {{C}} = C (d) \bigg (\frac {C _ {\omega} ^ {4}}{\min \{\lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \} ^ {2}} \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {6}} + \frac {1}{\min \{\lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\ddagger} , \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} \}} \bigg).
$$

## 10.4.7. Conclusion

Given$\lambda _ { n + 1 } < \lambda _ { n } ^ { * }$and$\mu _ { n + 1 } < \mu _ { n } ^ { * }$, we define

$$
\lambda_ {n + 1} = \lambda_ {n} ^ {\ddagger} \quad \text { and } \quad \mu_ {n + 1} = \mu_ {n} ^ {\ddagger},
$$

and we impose that

$$
\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\dagger} = \lambda_ {n} ^ {\dagger} - \lambda_ {n} ^ {\flat} = \lambda_ {n} ^ {\flat} - \lambda_ {n} ^ {\ddagger} = \frac {1}{3} (\lambda_ {n} ^ {*} - \lambda_ {n + 1}) \quad \text { and } \quad \mu_ {n} ^ {*} - \mu_ {n} ^ {\ddagger} = \mu_ {n} ^ {*} - \mu_ {n + 1}.
$$

Then from (10.59), (10.61)–(10.63) and (10.70)–(10.72) we see that$( \mathbf { E } _ { \varrho } ^ { \mathbf { n } + \mathbf { 1 } } ) , ~ ( \widetilde { \mathbf { E } } _ { \varrho } ^ { \mathbf { n } + \mathbf { 1 } } )$, $( \mathbf { E _ { h } ^ { n + 1 } } )$and$( \widetilde { \mathbf { E } } _ { \mathbf { h } } ^ { \mathbf { n } + \mathbf { 1 } } )$) have all been established in the present subsection, with

$$
\delta_ {n + 1} = \frac {C (d) C _ {F} (1 + C _ {F}) (1 + C _ {\omega} ^ {4}) e ^ {C T _ {n} ^ {2}}}{\min \{\lambda_ {n} ^ {*} - \lambda_ {n + 1} , \mu_ {n} ^ {*} - \mu_ {n + 1} \} ^ {9}} \max \biggl \{1, \sum_ {k = 1} ^ {n} \delta_ {k}, \biggr \} \left(1 + \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {6}}\right) \delta_ {n} ^ {2}.\tag{10.73}
$$

## 10.5. Convergence of the scheme

For any$n { \geqslant } 1$, we set

$$
\lambda_ {n} - \lambda_ {n} ^ {*} = \lambda_ {n} ^ {*} - \lambda_ {n + 1} = \mu_ {n} - \mu_ {n} ^ {*} = \mu_ {n} ^ {*} - \mu_ {n + 1} = \frac {\Lambda}{n ^ {2}}\tag{10.74}
$$

for some$\Lambda { > } 0$. By choosing Λ small enough, we can make sure that the conditions

$$
2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*}) <   1 \quad \mathrm{and} \quad 2 \pi (\mu_ {k} - \mu_ {k} ^ {*}) <   1
$$

are satisfied for all$k ,$as well as the other smallness assumptions made throughout this section. Moreover, we have$\lambda _ { k } - \lambda _ { k } ^ { * } { \geq } \Lambda / k ^ { 2 }$, so conditions$\bf ( C _ { 1 } ) { - } ( C _ { 9 } )$will be satisfied if

$$
\sum_ {k = 1} ^ {n} k ^ {1 2} \delta_ {k} \leqslant \Lambda^ {6} \omega \quad \text { and } \quad \sum_ {j = k + 1} ^ {n} j ^ {6} \delta_ {j} \leqslant \Lambda^ {3} \omega \left(\frac {1}{k ^ {2}} - \frac {1}{n ^ {2}}\right)
$$

for some small explicit constant$\omega > 0$, depending on the other constants appearing in the problem. Both conditions are satisfied if

$$
\sum_ {k = 1} ^ {\infty} k ^ {1 2} \delta_ {k} \leqslant \Lambda^ {6} \omega .\tag{10.75}
$$

Then from (10.60) we have that$T _ { n } { \leqslant } C _ { \gamma } ( n ^ { 2 } / \Lambda ) ^ { ( 7 + \gamma ) / ( \gamma - 1 ) }$, so the induction relation on$\delta _ { n }$gives

$$
\delta_ {1} \leqslant C \delta \quad \text { and } \quad \delta_ {n + 1} = C \left(\frac {n ^ {2}}{\Lambda}\right) ^ {9} e ^ {C (n ^ {2} / \Lambda) ^ {(1 4 + 2 \gamma) / (\gamma - 1)}} \delta_ {n} ^ {2}.\tag{10.76}
$$

To establish this relation we also assumed that$\delta _ { n }$is bounded below by$C _ { F } \zeta _ { n }$, the error coming from the short-time iteration; but this follows easily by construction, since the constraints imposed on$\delta _ { n }$are much worse than those on$\zeta _ { n }$

Having fixed$\Lambda ,$we will check that for δ small enough, (10.76) implies both the fast convergence of$( \delta _ { k } ) _ { k = 1 } ^ { \infty }$, and the condition (10.75), which will justify a posteriori the derivation of (10.76). (An easy induction is enough to turn this into a rigorous reasoning.)

For this we fix$a \in ( 1 , a _ { I } ) , 0 < z < z _ { I } < 1$, and we check by induction that

$$
\delta_ {n} \leqslant \Delta z ^ {a ^ {n}} \quad \text { for   all } n \geqslant 1.\tag{10.77}
$$

If$\Delta$is given, (10.77) holds for$n { = } 1$as soon as$\delta \leqslant ( \Delta / C ) z ^ { a }$. Then, to go from stage n to stage$n { \mathrel { + { 1 } } }$, we should check that

$$
\frac {C n ^ {1 8}}{\Lambda^ {9}} e ^ {C n ^ {(2 8 + 4 \gamma) / (\gamma - 1)} / \Lambda^ {(1 4 + 2 \gamma) / (\gamma - 1)}} \Delta^ {2} z ^ {2 a ^ {n}} \leqslant \Delta z ^ {a ^ {n + 1}};
$$

this is true if

$$
\frac {1}{\Delta} \geqslant \frac {C}{\Lambda^ {9}} \sup _ {n \in \mathbb {N}} n ^ {1 9} e ^ {C n ^ {(2 8 + 4 \gamma) / (\gamma - 1)} / \Lambda^ {(1 4 + 2 \gamma) / (\gamma - 1)}} z ^ {(2 - a) a ^ {n}}.
$$

Since$a < 2$, the supremum on the right-hand side is finite, and we just have to choose $\Delta$small enough. Then, reducing$\Delta$further if necessary, we can ensure (10.75). This concludes the proof.

Remark 10.1. This argument almost fully exploits the bi-exponential convergence of the Netwon scheme: a convergence like, say,$O ( e ^ { - n ^ { 1 0 0 0 } } )$) would not be enough to treat values of$\gamma$which are close to 1. In 11.2 we shall present a more cumbersome approach which is less greedy in the convergence rate, but still needs convergence like$O ( e ^ { - n ^ { \alpha } } )$) for α large enough.

## 11. Coulomb–Newton interaction

In this section we modify the scheme of$\ S 1 0$to treat the case$\gamma = 1$. We provide two diferent strategies. The first one is quite simple and will only come close to treat this case, since it will hold on (nearly) exponentially large times in the inverse of the perturbation size. The second one, somewhat more involved, will hold up to infinite times.

## 11.1. Estimates on exponentially large times

In this subsection we adapt the estimates of 10 to the case$\gamma = 1$, under the additional restriction that$0 \leqslant t \leqslant A ^ { 1 / \delta ( \log \delta ) ^ { 2 } }$for some constant$A { > } 1$

In the iterative scheme, the only place where we used$\gamma > 1$(and not just$\gamma \geqslant 1 )$) is in Step$6 ,$when it comes to the echo response via Theorem 7.7. Now, in the case$\gamma = 1$, the formula for$K _ { 1 } ^ { n }$should be

$$
K _ {1} ^ {n} (t, \tau) = \sum_ {k = 1} ^ {n} \delta_ {k} K _ {1} ^ {(\alpha_ {n, k}), 1} (t, \tau),
$$

with$\alpha _ { n , k } { = } \pi$min$\left\{ \mu _ { k } - \mu _ { n } ^ { * } , \lambda _ { k } - \lambda _ { n } ^ { * } , 2 \eta \right\}$. By Theorem$7 . 7 ( \mathrm { i i } )$this induces, in addition to other well-behaved factors, an uncontrolled exponential growth$O ( e ^ { \varepsilon _ { n } t } )$, with

$$
\varepsilon_ {n} = \Gamma \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{\alpha_ {n , k} ^ {3}};
$$

in particular$\varepsilon _ { n }$will remain bounded and$O ( \delta )$throughout the scheme.

Let us replace (10.74) by

$$
\lambda_ {n} - \lambda_ {n} ^ {*} = \lambda_ {n} ^ {*} - \lambda_ {n + 1} = \mu_ {n} - \mu_ {n} ^ {*} = \mu_ {n} ^ {*} - \mu_ {n + 1} = \frac {\Lambda}{n (\log (e + n)) ^ {2}},
$$

where$\Lambda { > } 0$is very small. (This is allowed since the series

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{n (\log (e + n)) ^ {2}}
$$

converges—the power 2 could of course be replaced by any$r { > } 1 . )$Then during the first stages of the iteration we can absorb the$O ( e ^ { \varepsilon _ { n } t } )$factor by the loss of regularity if, say,

$$
\varepsilon_ {n} \leqslant \frac {\Lambda}{2 n (\log (e + n)) ^ {2}}.
$$

Recalling that$\scriptstyle { \varepsilon _ { n } = O ( \delta ) }$, this is satisfied as soon as

$$
n \leqslant N := \frac {K}{\delta (\log (1 / \delta)) ^ {2}},\tag{11.1}
$$

where$K > 0$is a positive constant depending on the other parameters of the problem but of course not on δ. So during these first stages we get the same long-time estimates as in 10.

For$n > N$we cannot rely on the loss of regularity any longer; at this stage the error is about

$$
\delta_ {N} \leqslant C \delta^ {a ^ {N}},
$$

where$1 < a < 2$. To get the bounds for larger values of$n _ { \mathrm { : } }$, we impose a restriction on the time-interval, say$0 \leqslant t \leqslant T _ { \mathrm { m a x } }$. Allowing for a degradation of the rate$\delta ^ { a ^ { n } }$into$\delta ^ { \underline { { a } } ^ { n } }$with $\underline { { a } } < \boldsymbol { a }$, we see that the new factor$e ^ { \varepsilon _ { n } T _ { \mathrm { m a x } } }$can be eaten up by the scheme if

$$
e ^ {\varepsilon_ {n} T _ {\max}} \delta^ {(a - \underline {{a}}) \underline {{a}} ^ {n}} \leqslant 1 \quad \text { for   all } n \geqslant N.
$$

This is satisfied if

$$
T _ {\max} = O \left(\underline {{a}} ^ {N} \frac {1}{\delta} \log \frac {1}{\delta}\right).
$$

Recalling (11.1), we see that the latter condition holds true if

$$
T _ {\max} = O \left(A ^ {1 / \delta (\log \delta) ^ {2}} \frac {1}{\delta} \log \frac {1}{\delta}\right)
$$

for some well-chosen constant$A { > } 1$. Then we can complete the iteration, and end up with a bound like

$$
\left\| f _ {t} - f _ {i} \right\| _ {\mathcal {Z} _ {t} ^ {\lambda^ {\prime}, \mu^ {\prime}}} \leqslant C \delta \quad \text { for   all } t \in [ 0, T _ {\max} ],
$$

where$C$is another constant independent of δ. The conclusion follows easily.

## 11.2. Mode-by-mode estimates

Now we shall change the estimates of 10 a bit more in depth to treat arbitrarily large times for$\gamma = 1$. The main idea is to work mode-by-mode in the estimate of the spatial density, instead of looking directly for norm estimates.

Steps 1–5 remain the same, and the changes mainly occur in Step 6.

Substep 6 (a) is unchanged, but we only retain from that substep

$$
e ^ {2 \pi (\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}) | l |} \left| \widehat {\sigma_ {t} ^ {n , n}} (l) \right| \leqslant \frac {2 C _ {F} \delta_ {n} ^ {2}}{(\pi (\lambda_ {n} - \lambda_ {n} ^ {*})) ^ {2}} \quad \text { for   all } l \in \mathbb {Z} ^ {d}.\tag{11.2}
$$

Substep (b) is more deeply changed. Let$\hat { \mu } _ { n } < \mu _ { n } ^ { * }$

First, for each$l \in \mathbb { Z } ^ { d }$, we have, by Propositions 4.34 and 4.35, and the last part of Proposition 6.2,

$$
\begin{array} { r l } & e ^ { 2 \pi ( \lambda _ { n } ^ { * } t + \hat { \mu } _ { n } ) | l | } | \widehat { \mathcal { E } } ( t , l ) | \\ & \quad \leqslant \int _ { 0 } ^ { t } \sum _ { m \in \mathbb { Z } ^ { d } } \| P _ { m } ( F [ h _ { \tau } ^ { n + 1 } ] \circ \Omega _ { t , \tau } ^ { n } - F [ h _ { \tau } ^ { n + 1 } ] ) \| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \hat { \mu } _ { n } } } \\ & \qquad \times \| P _ { l - m } G _ { \tau , t } ^ { n } \| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \hat { \mu } _ { n } ; 1 } } d \tau \\ & \leqslant \int _ { 0 } ^ { t } \sum _ { m , m ^ { \prime } \in \mathbb { Z } ^ { d } } \left\| P _ { m - m ^ { \prime } } \int _ { 0 } ^ { 1 } \nabla F [ h _ { \tau } ^ { n + 1 } ] \circ ( \mathrm{Id} + \theta ( \Omega _ { t , \tau } ^ { n } - \mathrm{Id} ) ) d \theta \right\| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \hat { \mu } _ { n } } } \\ & \qquad \times \| P _ { m ^ { \prime } } ( \Omega _ { t , \tau } ^ { n } - \mathrm{Id} ) \| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \hat { \mu } _ { n } } } \| P _ { l - m } G _ { \tau , t } ^ { n } \| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \hat { \mu } _ { n } ; 1 } } d \tau \\ & \leqslant \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { t } \| G _ { \tau , t } ^ { n } \| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \mu _ { n } ^ { * } ; 1 } } \left\| \Omega _ { t , \tau } ^ { n } - \mathrm{Id} \right\| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \mu _ { n } ^ { * } } } \sum _ { m , m ^ { \prime } \in \mathbb { Z } ^ { d } } e ^ { - 2 \pi ( \mu _ { n } ^ { * } - \hat { \mu } _ { n } ) | l - m | } \\ & \qquad \times e ^ { - 2 \pi ( \mu _ { n } ^ { * } - \hat { \mu } _ { n } ) | m ^ { \prime } | } \| P _ { m - m ^ { \prime } } ( \nabla F [ h _ { \tau } ^ { n + 1 } ] \circ ( \mathrm{Id} + \theta ( \Omega _ { t , \tau } ^ { n } - \mathrm{Id} ) ) ) \| _  \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \hat { \mu } _ { n } } d \tau d \theta \\ & \leqslant \int _ { 0 } ^ { t } | G ^ { n } \| _  \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \mu _ { n } ^ { * } ; 1 } \| \Omega _ { t , \tau } ^ { n } - \mathrm{Id} \| _ { \mathcal { Z } _ { \tau - b t / ( 1 + b ) } ^ { \lambda _ { n } ^ { * } ( 1 + b ) , \mu _ { n } ^ * } } \\ & \qquad \times \sum _ { m , m ^ { \prime }, q \in \mathbb { Z } ^ { d } } e ^ { - 2 \pi ( \mu _ { n } ^ { * } - \hat { \mu } _ { n } ) | l - m | } e ^ { - 2 \pi ( \mu _ { n } ^ { * } - \hat { \mu } _ { n } ) | m ^ { \prime } | } \\ & \qquad \times e ^  - 2 \pi ( \mu _ { n } ^ { * } - \hat { \mu } _ { n } ) | m - m ^ { \prime } - q | \| P _ { q } ( \nabla F [ h _ { \tau } ^ { n + 1} ] ) \| _ { {\mathcal F} ^ {\tilde {\nu} _ { n}}} d \tau , \\ & = \| P _ {\tilde {\nu} _ {\alpha}} \| _ {\mathcal F} . \\ & = \| P _ {\tilde {\nu} _ {\beta}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\gamma}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^ {\prime}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta} ^ {\prime}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^ {\prime} ^ {\prime}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta} ^ {\prime} ^ {\prime} ^ {\prime}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^ {\prime} ^ {\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta} ^ {\prime} ^ {\prime} ^ {\prime}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^ {\prime} ^ {\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta} ^ {\prime} ^ {\prime} ^{\prime}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^{\prime} ^{\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta} ^{\prime} ^{\epsilon} ^{\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^{\prime} ^{\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta} ^{\prime} ^{\epsilon} ^{\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^{\prime} ^{\epsilon} ^{\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\eta} ^{\prime} ^{\epsilon} ^{\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ {\tilde {\nu} _ {\epsilon} ^{\prime} ^{\epsilon} ^{\epsilon}} \| _ {\mathcal F}. \\ & = \| P _ \tilde {\nu} _ {\eta} ^{ *}, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q, q , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , q , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p , p   . \\ & = \| P (\boldsymbol f) - P (\boldsymbol g) - P (\boldsymbol k) - P (\boldsymbol l) - P (\boldsymbol m) - P (\boldsymbol n) - P (\boldsymbol o) - P (\boldsymbol w) - P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol z) - P (\boldsymbol w) - P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol z) - P (\boldsymbol w) - P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) + P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) - P (\boldsymbol x) + P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol y) + P (\boldsymbol x) - P (\boldsymbol y) - P (\boldsymbol x) - P (\boldsymbol x) + P (\boldsymbol x) - P (\boldsymbol y) + P (\boldsymbol x) - P (\boldsymbol y) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) + P (\boldsymbol x) . \\ & = \| Q (t, s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (t). \\ & = \| Q (t, s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (s), Q (t). \\ & = \| Q (t, s), Q (s), S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S | | S |
end{array}
$$

where

$$
\hat {\nu} _ {n} = \hat {\mu} _ {n} + \lambda_ {n} ^ {*} (1 + b) \left| \tau - \frac {b t}{1 + b} \right| + \left\| \Omega^ {n} X _ {t, \tau} - x \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}}}.
$$

For$\alpha \leqslant 1$we have

$$
\sum_ {m, m ^ {\prime} \in \mathbb {Z} ^ {d}} e ^ {- 2 \pi \alpha | l - m |} e ^ {- 2 \pi \alpha | m ^ {\prime} |} e ^ {- 2 \pi \alpha | m - m ^ {\prime} - q |} \leqslant \frac {C (d)}{\alpha^ {d}} e ^ {- \pi \alpha | l - q |},
$$

and we can argue as in Substep 6 (b) of 10 to get

$$
\begin{array}{l} e ^ {2 \pi (\lambda_ {n} ^ {*} t + \mu_ {n} ^ {*}) | l |} | \widehat {\mathcal {E}} (t, l) | \\ \leqslant \frac {C}{(\mu_ {n} ^ {*} - \hat {\mu} _ {n}) ^ {d}} \bigg (C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \bigg (\sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {5}} \bigg) \\ \times \sum_ {q \in \mathbb {Z} ^ {d}} e ^ {- \pi (\mu_ {n} ^ {*} - \hat {\mu} _ {n}) | l - q |} \int_ {0} ^ {t} e ^ {2 \pi (\lambda_ {n} ^ {*} \tau + \hat {\mu} _ {n}) | q |} \big | \widehat {\varrho [ h _ {\tau} ^ {n + 1} ] (q)} \big | \frac {d \tau}{(1 + \tau) ^ {2}}. \end{array}\tag{11.3}
$$

Next, we use again Proposition 4.34 and simple estimates to bound$\bar { \mathcal { E } } ,$

$$
\begin{array}{r l} & e ^ {2 \pi (\lambda_ {n} ^ {*} t + \hat {\mu} _ {n}) | l |} \big | \widehat {\overline {{\mathcal {E}}}} (t, l) \big | \leqslant \int_ {0} ^ {t} \| G ^ {n} - \overline {{G}} ^ {n} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {n} ^ {*} (1 + b), \mu_ {n} ^ {*}; 1}} \\ & \qquad \times \sum_ {m \in \mathbb {Z} ^ {d}} e ^ {- 2 \pi (\mu_ {n} ^ {*} - \hat {\mu} _ {n}) | m |} \| P _ {l - m} (F [ h _ {\tau} ^ {n + 1} ]) \| _ {\mathcal {F} ^ {\hat {\beta} _ {n}}} d \tau , \end{array}
$$

where

$$
\hat {\beta} _ {n} = \lambda_ {n} ^ {*} (1 + b) \bigg | \tau - \frac {b t}{1 + b} \bigg | + \hat {\mu} _ {n}.
$$

Reasoning as in Substep 6 (b) of$\ S 1 0$, we arrive at

$$
\begin{array}{l} e ^ {2 \pi (\lambda_ {n} ^ {*} t + \hat {\mu} _ {n}) | l |} \big | \widehat {\mathcal {E}} (t, l) \big | \\ \leqslant C \bigg (C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \bigg (\sum_ {j = 1} ^ {n} \frac {\delta_ {j}}{(2 \pi (\lambda_ {j} - \lambda_ {n} ^ {*})) ^ {6}} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \\ \times \sum_ {m \in \mathbb {Z} ^ {d}} e ^ {- 2 \pi (\mu_ {n} ^ {*} - \hat {\mu} _ {n}) | m |} \int_ {0} ^ {t} e ^ {2 \pi (\lambda_ {n} ^ {*} \tau + \hat {\mu} _ {n}) | l - m |} \big | \widehat {\varrho [ h _ {\tau} ^ {n + 1} ]} (l - m) \big | \frac {d \tau}{(1 + \tau) ^ {2}}. \end{array}\tag{11.4}
$$

Then we consider the “main contribution”$\bar { \sigma } ^ { n , n + 1 }$, which we decompose as in$\ S 1 0 \colon$

$$
\overline {{\sigma}} _ {t} ^ {n, n + 1} = \overline {{\sigma}} _ {t, 0} ^ {n, n + 1} + \sum_ {k = 1} ^ {n} \overline {{\sigma}} _ {t, k} ^ {n, n + 1},
$$

and we write, for$k \geqslant 1$

$$
\begin{array}{r l} & e ^ {2 \pi (\lambda_ {n} ^ {*} t + \hat {\mu} _ {n})} \big | \widehat {\overline {{\sigma}} _ {t , k} ^ {n , n + 1}} (l) \big | \leqslant \sum_ {m \in \mathbb {Z} ^ {d}} \int_ {0} ^ {t} K _ {l, m} ^ {n, h ^ {k}} (t, \tau) \| P _ {l - m} (F [ h _ {\tau} ^ {n + 1} ]) \| _ {\mathcal {F} ^ {\nu_ {n} ^ {\prime}, \gamma}} d \tau \\ & \qquad + \int_ {0} ^ {t} K _ {0} ^ {n, h ^ {k}} (t, \tau) \| P _ {l} (F [ h _ {\tau} ^ {n + 1} ]) \| _ {\mathcal {F} ^ {\nu_ {n} ^ {\prime}, \gamma}} d \tau , \end{array}
$$

where

$$
\begin{array}{c} \nu_ {n} ^ {\prime} = \lambda_ {n} ^ {*} (1 + b) \bigg | \tau - \frac {b t}{1 + b} \bigg | + \mu_ {n} ^ {\prime}, \\ K _ {l, m} ^ {n, h ^ {k}} (t, \tau) = K _ {l, m} ^ {n, k} (t, \tau) \sup _ {0 \leqslant s \leqslant t} \frac {\| \nabla_ {v} (h _ {s} ^ {k} \circ \Omega_ {t , s} ^ {k - 1}) - \langle \nabla_ {v} (h _ {s} ^ {k} \circ \Omega_ {t , s} ^ {k - 1}) \rangle \| _ {\mathcal {Z} _ {s - b t / (1 + b)} ^ {\lambda_ {k} (1 + b) , \mu_ {k}}}}{1 + s}, \\ K _ {l, m} ^ {n, k} (t, \tau) = (1 + \tau) e ^ {- \pi (\mu_ {k} - \hat {\mu} _ {n}) | m |} \frac {e ^ {- 2 \pi (\mu_ {n} ^ {\prime} - \hat {\mu} _ {n}) | l - m |}}{1 + | l - m | ^ {\gamma}} e ^ {- \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) | l (t - \tau) + m \tau |}, \end{array}
$$

and the formula for$K _ { 0 } ^ { n , h ^ { k } }$is unchanged with respect to 10.

Assuming that$\mu _ { n } ^ { \prime } { = } \hat { \mu } _ { n } { + } \eta ( t { - } \tau ) / ( 1 { + } t )$and reasoning as in Substep 6 (b) of$\ S 1 0$, we end up with the following estimate on the “main term”:

$$
\begin{array}{l} e ^ {2 \pi (\lambda_ {n} ^ {*} t + \hat {\mu} _ {n}) | l |} \big | \widehat {\overline {{\sigma}} _ {t , k} ^ {n , n + 1}} (l) \big | \\ \leqslant C \sum_ {m \in \mathbb {Z} ^ {d}} \int_ {0} ^ {t} \bigg (\sum_ {k = 1} ^ {n} \delta_ {k} K _ {l, m} ^ {(\alpha_ {n, k}), \gamma} (t, \tau) \bigg) e ^ {2 \pi (\lambda_ {n} ^ {*} \tau + \hat {\mu} _ {n}) | l - m |} \big | \widehat {\varrho [ h _ {\tau} ^ {n + 1} ]} (l - m) \big | d \tau \\ + C \sum_ {m \in \mathbb {Z} ^ {d}} \int_ {0} ^ {t} \bigg (\sum_ {k = 1} ^ {n} \delta_ {k} e ^ {- \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) (t - \tau)} \bigg) e ^ {2 \pi (\lambda_ {n} ^ {*} \tau + \hat {\mu} _ {n}) | l |} \big | \widehat {\varrho [ h _ {\tau} ^ {n + 1} ]} (l - m) \big | d \tau . \end{array}\tag{11.5}
$$

Then Substep$6 ( \mathrm { c ) }$becomes, with$\Phi ( l , \tau ) { = } \widehat { \varrho [ h _ { \tau } ^ { n + 1 } ] } ( l )$

$$
\begin{array}{l} e ^ {2 \pi (\lambda_ {n} ^ {*} t + \hat {\mu} _ {n}) | l |} \bigg | \Phi (l, t) - \int_ {0} ^ {t} K ^ {0} (l, t - \tau) \Phi (l, \tau) d \tau \bigg | \\ \leqslant \frac {C \delta_ {n} ^ {2}}{(\lambda_ {n} - \lambda_ {n} ^ {*}) ^ {2}} + \sum_ {m \in \mathbb {Z} ^ {d}} \int_ {0} ^ {t} \bigg (K _ {l, m} ^ {n} (t, \tau) + \frac {c _ {m} ^ {n}}{(1 + \tau) ^ {2}} \bigg) e ^ {2 \pi (\lambda_ {n} ^ {*} \tau + \hat {\mu} _ {n}) | l - m |} | \Phi (l - m, \tau) | d \tau \\ + \int_ {0} ^ {t} K _ {0} ^ {n} (t, \tau) e ^ {2 \pi (\lambda_ {n} ^ {*} \tau + \hat {\mu} _ {n}) | l |} | \Phi (l, \tau) | d \tau , \end{array}
$$

with

$$
\begin{array}{r l} & K _ {l, m} ^ {n} (t, \tau) = C \sum_ {k = 1} ^ {n} \delta_ {k} K _ {l, m} ^ {(\widehat {\alpha} _ {n}), \gamma} (t, \tau), \\ & \qquad \widehat {\alpha} _ {n} = \pi \min \{\mu_ {n} - \widehat {\mu} _ {n}, \lambda_ {n} - \lambda_ {n} ^ {*}, 2 \eta \}, \\ & K _ {0} ^ {n} (t, \tau) = C \sum_ {k = 1} ^ {n} \delta_ {k} e ^ {- \pi (\lambda_ {k} - \lambda_ {n} ^ {*}) (t - \tau)}, \\ & \qquad c _ {m} ^ {n} = \frac {C}{(\mu_ {n} ^ {*} - \widehat {\mu} _ {n}) ^ {d}} \bigg (C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \bigg (1 + \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {6}} \bigg) e ^ {- \pi (\mu_ {n} ^ {*} - \widehat {\mu} _ {n}) | m |}. \end{array}
$$

Note that

$$
\sum_ {m \in \mathbb {Z} ^ {d}} c _ {m} ^ {n} + \bigg (\sum_ {m \in \mathbb {Z} ^ {d}} (c _ {m} ^ {n}) ^ {2} \bigg) ^ {1 / 2} \leqslant \frac {C}{(\mu_ {n} ^ {*} - \hat {\mu} _ {n}) ^ {2 d}} \bigg (C _ {0} ^ {\prime} + \sum_ {k = 1} ^ {n} \delta_ {k} \bigg) \bigg (1 + \sum_ {k = 1} ^ {n} \frac {\delta_ {k}}{(2 \pi (\lambda_ {k} - \lambda_ {k} ^ {*})) ^ {6}} \bigg).
$$

Then, being$\Phi ( 0 , t ) { = } 0$, we can apply Theorem 7.12 and deduce (taking already into account, for the sake of readability of the formula, that$\scriptstyle \sum _ { k = 1 } ^ { n } \delta _ { k }$and${ \textstyle \sum _ { k = 1 } ^ { n } \delta _ { k } } / ( \lambda _ { k } - \lambda _ { k } ^ { * } )$ are uniformly bounded)

$$
e ^ {2 \pi (\lambda_ {n} ^ {*} t + \hat {\mu} _ {n}) | l |} \left| \widehat {\varrho_ {t} ^ {n + 1}} (l) \right| \leqslant C \frac {\delta_ {n} ^ {2}}{(\lambda_ {n} - \lambda_ {n} ^ {*}) ^ {2} \widehat {\alpha} _ {n} \varepsilon^ {3 / 2} (\mu_ {n} ^ {*} - \hat {\mu} _ {n}) ^ {2 d}} \exp \left(\frac {C (1 + \widehat {T} _ {\varepsilon , n} ^ {2})}{(\mu_ {n} ^ {*} - \hat {\mu} _ {n}) ^ {2 d}}\right) e ^ {\varepsilon t},
$$

where

$$
\widehat {T} _ {\varepsilon , n} = C \max \biggl \{\left(\frac {1}{\alpha_ {n} ^ {3 + 2 d} \varepsilon^ {\gamma + 2}}\right) ^ {1 / \gamma}, \left(\frac {1}{\alpha_ {n} ^ {d} \varepsilon^ {\gamma + 1 / 2}}\right) ^ {1 / (\gamma - 1 / 2)}, \left(\frac {1}{\varepsilon} \left(\sum_ {m \in \mathbb {Z} ^ {d}} c _ {m} ^ {n}\right) ^ {2}\right) ^ {1 / 3} \biggr \}.
$$

If${ \lambda } _ { n } ^ { \dagger } < { \lambda } _ { n } ^ { * }$and$\mu _ { n } ^ { \dagger } < \hat { \mu } _ { n }$are chosen as before and$\varepsilon { = } 2 \pi ( \lambda _ { n } ^ { * } { - } \lambda ^ { \dagger } )$, this implies a uniform bound on C

$$
\| \varrho_ {t} ^ {n + 1} \| _ {\mathcal {F} ^ {\lambda_ {n} ^ {\dagger} t + \mu_ {n} ^ {\dagger}}} \leqslant \frac {C}{(\hat {\mu} _ {n} - \mu_ {n} ^ {\dagger}) ^ {d}} \sup _ {l \in \mathbb {Z} ^ {d}} e ^ {2 \pi (\lambda_ {n} ^ {*} t + \hat {\mu} _ {n}) | l |} \big | \widehat {\varrho_ {t} ^ {n + 1}} (l) \big |
$$

obtained with the formula above with

$$
\widehat {T} _ {\varepsilon , n} = \widehat {T} _ {n} = C \max \left\{\frac {1}{\lambda_ {n} ^ {*} - \lambda_ {n} ^ {\dagger}}, \frac {1}{\lambda_ {n} - \lambda_ {n} ^ {*}}, \frac {1}{\mu_ {n} - \mu_ {n} ^ {*}}, \frac {1}{\mu_ {n} ^ {*} - \hat {\mu} _ {n}} \right\} ^ {a},
$$

where

$$
a = \max \biggl \{\frac {5 + \gamma + 2 d}{\gamma}, \frac {d + \gamma + \frac {1}{2}}{\gamma - \frac {1}{2}}, \frac {4 d + 1}{3} \biggr \}.
$$

Then Steps 7–10 of the iteration can be repeated with the only modification that $\mu _ { n } ^ { * }$is replaced by$\mu _ { n } ^ { \dagger }$

The convergence ( 10.5) works just the same, except that now we need more intermediate regularity indices$\mu _ { n }$:

$$
\mu_ {n + 1} = \mu_ {n} ^ {\ddagger} <   \mu_ {n} ^ {\dagger} <   \hat {\mu} _ {n} <   \mu_ {n} ^ {*};
$$

the obvious choice being to let$\mu _ { n } ^ { \dagger } - \mu _ { n } ^ { \dagger } = \hat { \mu } _ { n } - \mu _ { n } ^ { \dagger } = \mu _ { n } ^ { * } - \hat { \mu } _ { n }$

Choosing$\lambda _ { n } - \lambda _ { n + 1 }$and$\mu _ { n } - \mu _ { n + 1 }$of the order of$\Lambda / n ^ { 2 }$, we arrive in the end at the induction

$$
\delta_ {n + 1} \leqslant C \left(\frac {n ^ {2}}{\Lambda}\right) ^ {9 + 6 d} e ^ {C (n ^ {2} / \Lambda) ^ {\xi (d, \gamma)}} \delta_ {n} ^ {2},
$$

where

$$
\xi (d, \gamma) := 2 d + 2 \max \biggl \{\frac {5 + \gamma + 2 d}{\gamma}, \frac {d + \gamma + \frac {1}{2}}{\gamma - \frac {1}{2}}, \frac {4 d + 1}{3} \biggr \}.\tag{11.6}
$$

Then the convergence of the scheme (and a-posteriori justification of all the assumptions) is done exactly as in 10.

## 12. Convergence in large time

In this section we prove Theorem 2.6 as a simple consequence of the uniform bounds established in 10 and 11.

So let$f ^ { 0 } , L$and W satisfy the assumptions of Theorem 2.6. To simplify the notation we assume that$L { = } 1$

The second part of Assumption (2.14) precisely means that$f ^ { 0 } \in { \mathcal { C } } ^ { \lambda ; 1 }$. We shall actually assume a slightly more precise condition, namely that for some$\bar { p } { \in } [ 1 , \infty ]$,

$$
\sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \| \nabla_ {v} ^ {n} f ^ {0} \| _ {L ^ {p} (\mathbb {R} ^ {d})} \leqslant C _ {0} <   \infty \quad \text { for   all } p \in [ 1, \bar {p} ].\tag{12.1}
$$

(It is suficient to take$\bar { p } { = } 1$to get Theorem 2.6; but if this bound is available for some $\bar { p } { > } 1$then it will be propagated by the iteration scheme, and will result in more precise bounds.) Then we pick up$\underline { { \lambda } } \in ( 0 , \lambda )$),$\mu \in ( 0 , \mu )$,$\beta > 0$and$\beta ^ { \prime } \in ( 0 , \beta )$. By symmetry, we only consider non-negative times.

If$f _ { i }$is an initial datum satisfying the smallness condition (2.15), then by Theorem 4.20, we have a smallness estimate on$\| f _ { i } - f ^ { 0 } \| _ { \mathcal { Z } ^ { \lambda ^ { \prime } , \mu ^ { \prime } ; p } }$for all$p { \in } [ 1 , \bar { p } ] , \lambda ^ { \prime } { < } \lambda$and $\mu ^ { \prime } { < } \mu$. Then, as in 4.12 we can estimate the solution$h ^ { 1 }$to the linearized equation

$$
\left\{ \begin{array}{l} \partial_ {t} h ^ {1} + v \cdot \nabla_ {x} h ^ {1} + F [ h ^ {1} ] \cdot \nabla_ {v} f ^ {0} = 0, \\ h ^ {1} (0, \cdot) = f _ {i} - f ^ {0}, \end{array} \right.\tag{12.2}
$$

and we recover uniform bounds in$\mathcal { Z } ^ { \hat { \lambda } , \hat { \mu } ; p }$spaces, for any$\hat { \lambda } \in ( \underline { { \lambda } } , \lambda )$and${ \hat { \mu } } \in \left( \mu , \mu \right)$. More precisely,

$$
\sup _ {t \geqslant 0} \| \varrho [ h _ {t} ^ {1} ] \| _ {\mathcal {F} ^ {\hat {\lambda} t + \hat {\mu}}} + \sup _ {t \geqslant 0} \| h ^ {1} (t, \cdot) \| _ {\mathcal {Z} _ {t} ^ {\hat {\lambda}, \hat {\mu}; p}} \leqslant C \delta ,\tag{12.3}
$$

with$C { = } C ( d , \lambda ^ { \prime } , \hat { \lambda } , \mu ^ { \prime } , \hat { \mu } , W , f ^ { 0 } )$(this is of course assuming ε in Theorem 2.6 to be small enough).

We now set$\lambda _ { 1 } = \lambda ^ { \prime }$, and we run the iterative scheme of 9–11 for all$n { \geqslant } 2 . \ \operatorname { I f } \ \varepsilon$is small enough, up to slightly lowering$\lambda _ { 1 }$, we may choose all parameters in such a way that

$$
\lambda_ {k}, \lambda_ {k} ^ {*} \rightarrow \lambda_ {\infty} > \underline {{\lambda}} \text {and} \mu_ {k}, \mu_ {k} ^ {*} \rightarrow \mu_ {\infty} > \underline {{\mu}} \text {as} k \rightarrow \infty ;
$$

then we pick up B>0 such that

$$
\mu_ {\infty} - \lambda_ {\infty} (1 + B) B \geqslant \mu_ {\infty} ^ {\prime} > \underline {{\mu}},
$$

and we let$b ( t ) { = } B / ( 1 { + } t )$

As a result of the scheme, we have, for all$k \geqslant 2 .$

$$
\sup _ {0 \leqslant \tau \leqslant t} \| h _ {\tau} ^ {k} \circ \Omega_ {t, \tau} ^ {k - 1} \| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda_ {\infty} (1 + b), \mu_ {\infty}; 1}} \leqslant \delta_ {k},\tag{12.4}
$$

where$\textstyle \sum _ { k = 2 } ^ { \infty } \delta _ { k } \leqslant C \delta$and$\Omega ^ { k }$is the deflection associated with the force field generated by $h ^ { 1 } + \ldots + h ^ { k }$. Choosing$t { = } \tau$in (12.4) yields

$$
\sup _ {t \geqslant 0} \| h _ {t} ^ {k} \| _ {\mathcal {Z} _ {t - B t / (1 + B + t)} ^ {\lambda_ {\infty} (1 + B), \mu_ {\infty}; 1}} \leqslant \delta_ {k}.
$$

By Proposition 4.17, this implies that

$$
\sup _ {t \geqslant 0} \left\| h _ {t} ^ {k} \right\| _ {\mathcal {Z} _ {t} ^ {\lambda_ {\infty} (1 + B), \mu_ {\infty} - \lambda_ {\infty} (1 + B) B; 1}} \leqslant \delta_ {k}.
$$

In particular, we have a uniform estimate on$h _ { t } ^ { k }$in$\mathcal { Z } _ { t } ^ { \lambda _ { \infty } , \mu _ { \infty } ^ { \prime } ; 1 }$. Summing up over k yields for$f = f ^ { 0 } + \textstyle \sum _ { k = 1 } ^ { \infty } h ^ { k }$the estimate

$$
\sup _ {t \geqslant 0} \| f (t, \cdot) - f ^ {0} \| _ {\mathcal {Z} _ {t} ^ {\lambda_ {\infty}, \mu_ {\infty} ^ {\prime}; 1}} \leqslant C \delta .\tag{12.5}
$$

Passing to the limit in the Newton scheme, one shows that$f$solves the non-linear Vlasov equation with initial datum$f _ { i }$. (Once again we do not check the details; to be rigorous one would need to establish moment estimates, locally in time, before passing to the limit.) This implies in particular that$f$stays non-negative at all times.

Applying Theorem 4.20 again, we deduce from (12.5) that

$$
\sup _ {t \geqslant 0} \| f (t, \cdot) - f ^ {0} \| _ {\mathcal {Y} _ {t} ^ {\underline {{\lambda}}, \underline {{\mu}}}} \leqslant C \delta ;
$$

or equivalently, with the notation used in Theorem 2.6,

$$
\sup _ {t \geqslant 0} \| f (t, x - v t, v) - f ^ {0} (v) \| _ {\underline {{\lambda}}, \underline {{\mu}}} \leqslant C \delta .\tag{12.6}
$$

Moreover,$\varrho { = } \textstyle \int _ { \mathbb { R } ^ { d } } f$dv satisfies similarly

$$
\sup _ {t \geqslant 0} \| \varrho (t, \cdot) \| _ {\mathcal {F} ^ {\lambda_ {\infty} t + \mu_ {\infty}}} \leqslant C \delta .
$$

It follows that$\vert \hat { \varrho } ( t , k ) \vert \leqslant C \delta e ^ { - 2 \pi \lambda _ { \infty } \vert k \vert t } e ^ { - 2 \pi \mu _ { \infty } \vert k \vert }$for any$k { \neq } 0$. On the one hand, by Sobolev embedding, we deduce that for any$r \in \mathbb { N } .$

$$
\left\| \varrho (t, \cdot) - \langle \varrho \rangle \right\| _ {C ^ {r} (\mathbb {T} ^ {d})} \leqslant C _ {r} \delta e ^ {- 2 \pi \lambda^ {\prime} t};
$$

on the other hand, multiplying$\hat { \varrho }$by the Fourier transform of$\nabla W$, we see that the force $F { = } F [ f ]$satisfies

$$
| \widehat {F} (t, k) | \leqslant C \delta e ^ {- 2 \pi \lambda^ {\prime} | k | t} e ^ {- 2 \pi \mu^ {\prime} | k |} \quad \text { for   all } t \geqslant 0 \text { and   all } k \in \mathbb {Z} ^ {d},\tag{12.7}
$$

for some$\lambda ^ { \prime } { > } \lambda$and$\mu ^ { \prime } { > } \mu$

Now, from (12.6) we have, for any$( k , \eta ) \in \mathbb { Z } ^ { d } \times \mathbb { R } ^ { d }$and any$t \geqslant 0$

$$
| \tilde {f} (t, k, \eta + k t) - \tilde {f} ^ {0} (\eta) | \leqslant C \delta e ^ {- 2 \pi \mu^ {\prime} | k |} e ^ {- 2 \pi \lambda^ {\prime} | \eta |};\tag{12.8}
$$

so

$$
| \tilde {f} (t, k, \eta) | \leqslant | \tilde {f} ^ {0} (\eta + k t) | + C \delta e ^ {- 2 \pi \mu^ {\prime} | k |} e ^ {- 2 \pi \lambda^ {\prime} | \eta + k t |}.\tag{12.9}
$$

In particular, for any$k { \neq } 0$, and any$\eta \in \mathbb { R } ^ { d }$

$$
\tilde {f} (t, k, \eta) = O (e ^ {- 2 \pi \lambda^ {\prime} t}).\tag{12.10}
$$

Thus$f$is asymptotically close (in the weak topology) to its spatial average

$$
g = \langle f \rangle = \int_ {\mathbb {T} ^ {d}} f d x.
$$

Taking$k { = } 0$in (12.8) shows that, for any$\eta \in \mathbb { R } ^ { d }$

$$
| \tilde {g} (t, \eta) - \tilde {f} ^ {0} (\eta) | \leqslant C \delta e ^ {- 2 \pi \lambda^ {\prime} | \eta |}.\tag{12.11}
$$

Also, from the non-linear Vlasov equation, for any$\eta \in \mathbb { R } ^ { d }$we have

$$
\begin{array}{l} \tilde {g} (t, \eta) = \tilde {f} _ {i} (0, \eta) - \int_ {0} ^ {t} \int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} F (\tau , x) \cdot \nabla_ {v} f (\tau , x, v) e ^ {- 2 i \pi \eta \cdot v}   d v   d x   d \tau \\ = \tilde {f} _ {i} (0, \eta) - 2 i \pi \sum_ {l \in \mathbb {Z} ^ {d}} \int_ {0} ^ {t} \widehat {F} (\tau , l) \cdot \eta \tilde {f} (\tau , - l, \eta)   d \tau . \end{array}
$$

Using the bounds (12.7) and (12.10), it is easily shown that the above time-integral converges exponentially fast as$t \to \infty$, with rate$O ( e ^ { - \lambda ^ { \prime \prime } t } )$for any$\lambda ^ { \prime \prime } { < } \lambda ^ { \prime }$, to its limit

$$
\tilde {g} _ {\infty} (\eta) = \tilde {f} _ {i} (0, \eta) - 2 i \pi \sum_ {l \in \mathbb {Z} ^ {d}} \int_ {0} ^ {\infty} \widehat {F} (\tau , l) \cdot \eta \tilde {f} (\tau , - l, \eta) d \tau .\tag{12.12}
$$

By passing to the limit in (12.11) we see that

$$
| \tilde {g} _ {\infty} (\eta) - \tilde {f} ^ {0} (\eta) | \leqslant C \delta e ^ {- 2 \pi \lambda^ {\prime} | \eta |},
$$

and this concludes the proof of Theorem 2.6.

## 13. Non-analytic perturbations

Although the vast majority of studies of Landau damping assume that the perturbation is analytic, it is natural to ask whether this condition can be relaxed. As we noticed in Remark 3.5, this is the case for the linear problem. As for non-linear Landau damping, once the analogy with KAM theory has been identified, it is anybody’s guess that the answer might come from a Moser-type argument. However, this is not so simple, because the “loss of convergence” in our argument is much more severe than the “loss of regularity” which Moser’s scheme allows one to overcome.

For instance, the second-order correction$h ^ { 2 }$satisfies

$$
\partial_ {t} h ^ {2} + v \cdot \nabla_ {x} h ^ {2} + F [ f ^ {1} ] \cdot \nabla_ {v} h ^ {2} + F [ h ^ {2} ] \cdot \nabla_ {v} f ^ {1} = - F [ h ^ {1} ] \cdot \nabla_ {v} h ^ {1}.
$$

The action of$F [ f ^ { 1 } ]$is to curve trajectories, which does not help in our estimates. Discarding this efect and solving by Duhamel’s formula and Fourier transform, we obtain, with$S = - F [ h ^ { 1 } ] \cdot \nabla _ { v } h ^ { 1 }$and$\scriptstyle \varrho ^ { 2 } = \int _ { \mathbb { R } ^ { d } } h ^ { 2 } d v$,

$$
\begin{array}{l} \hat {\varrho} ^ {2} (t, k) \simeq \int_ {0} ^ {t} K ^ {0} (t - \tau , k) \hat {\varrho} ^ {2} (\tau , k)   d \tau \\ \qquad + 2 i \pi \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} (k - l) \widehat {W} (k - l) \hat {\varrho} ^ {2} (\tau , k - l) \widetilde {\nabla_ {v} h ^ {1}} (\tau , l, k (t - \tau))   d \tau \\ \qquad + \int_ {0} ^ {t} \widetilde {S} (\tau , k, k (t - \tau))   d \tau . \end{array}\tag{13.1}
$$

(The term with$K ^ { 0 }$includes the contribution of$\nabla _ { v } f ^ { 0 } . )$

Our regularity/decay estimates on$h ^ { 1 }$will never be better than those on the solution of the free transport equation, i.e.,$h _ { i } ( x - v t , v )$, where$h _ { i } = f _ { i } - f ^ { 0 }$. Let us forget about the efect of$K ^ { 0 }$in (13.1), replace the contribution of S by a decaying term$A ( k t )$. Let us choose$d { = } 1$and assume that$\hat { h } _ { i } ( l , \cdot ) = 0$if$l { \neq } \pm 1$. For$k > 0$, let us use the long-time approximation

$$
\tilde {h} _ {i} (- 1, k (t - \tau) - \tau)   1 _ {[ 0, t ]} (\tau)   d \tau \simeq \frac {c}{k + 1} \delta_ {k t / (k + 1)}, \quad c = \int_ {\mathbb {R}} \tilde {h} _ {i} (- 1, s)   d s = \hat {h} _ {i} (- 1, 0).
$$

Note that$c { \neq } 0$in general. Plugging all these simplifications into estimate (13.1) and choosing$\widehat { W } ( k ) = 1 / | k | ^ { 1 + \gamma }$suggests the a-priori simpler equation

$$
\varphi (t, k) = A (k t) + \frac {c k t}{(k + 1) ^ {\gamma + 2}} \varphi \left(\frac {k t}{k + 1}, k + 1\right).\tag{13.2}
$$

Replacing$\varphi ( t , k )$by$\varphi ( t , k ) / A ( k t )$reduces to$A { = } 1$, and then we can solve this equation by power series as in 7.1.3, obtaining

$$
\varphi (t, k) \simeq A (k t) e ^ {(c k t) ^ {1 / (\gamma + 2)}}.\tag{13.3}
$$

With a polynomial deterioration of the rate, we could use a regularization argument, but the fractional exponential is much worse.

However, our bounds are still good enough to establish decay for Gevrey perturbations. Let us agree that a function$f { = } f ( x , v )$lies in the Gevrey class$\mathcal { G } ^ { \nu } , \nu \geqslant 1$, if

$$
| \tilde {f} (k, \eta) | = O (\exp (- c | (k, \eta) | ^ {1 / \nu})) \quad \mathrm{forsome} c > 0;
$$

in particular$\mathcal { G } ^ { 1 }$means analytic. (An alternative convention would be to require the nth derivative to be$O ( ( n ! ) ^ { \nu } ) . )$As we shall explain, we can still get non-linear Landau damping if the initial datum$f _ { i }$lies in$\mathcal G ^ { \nu }$for ν close enough to 1. Although this is still quite demanding, it already shows that non-linear Landau damping is not tied to analyticity or quasi-analyticity, and holds for a large class of compactly supported perturbations.

Theorem 13.1. Let$\lambda { > } 0$. Let$f ^ { 0 } = f ^ { 0 } ( \boldsymbol { v } ) \geqslant 0$be an analytic homogeneous profile such that

$$
\sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\lambda^ {n}}{n !} \| \nabla_ {v} ^ {n} f ^ {0} \| _ {L ^ {1} (\mathbb {R} ^ {d})} <   \infty ,
$$

and let$W { = } W ( x ) \ s a t i s f y \ | \widehat { W } ( k ) | { = } O ( 1 / | k | ^ { 2 } )$. Assume that condition (L) from 2.2 holds. Let$\nu \in ( 1 , 1 + \theta )$with$\theta { = } 1 / \xi ( d , \gamma )$, where ξ was defined in (11.6). Let$\beta > 0$and$\alpha { < } 1 / \nu$ Then there is$\varepsilon > 0$such that if

$$
\delta := \sup_{\substack{k\in \mathbb{Z}^{d}\\ \eta \in \mathbb{R}^{d}}}|\left(\tilde{f}_{i} - \tilde{f}^{0}\right)(k,\eta)|e^{\lambda |\eta |^{1 / \nu}}e^{\lambda |k|^{1 / \nu}} + \int_{\mathbb{T}^{d}}\int_{\mathbb{R}^{d}}|(f_{i} - f^{0})(x,v)|e^{\beta |v|}  dv  dx\leqslant \varepsilon ,
$$

then as$t \to + \infty$the solution$f = f ( t , x , v )$of the non-linear Vlasov equation on$\mathbb { T } ^ { d } \times \mathbb { R } ^ { d }$ with interaction potential W and initial datum$f _ { i }$satisfies

$$
| \tilde {f} (t, k, \eta) - \tilde {f} _ {\infty} (\eta) | = O (\delta e ^ {- c t ^ {\alpha}}) \quad f o r a l l (k, \eta) \in \mathbb {Z} ^ {d} \times \mathbb {R} ^ {d}
$$

and

$$
\| F (t, \cdot) \| _ {C ^ {r} (\mathbb {T} ^ {d})} = O \bigl (\delta e ^ {- c t ^ {\alpha}} \bigr) \quad f o r a l l r \in \mathbb {N}
$$

for some$c > 0$and some homogeneous Gevrey profile$f _ { \infty }$, where F stands for the self-consistent force.

Remark 13.2. In view of (13.3), one may hope that the result remains true for$\theta { = } 2$ Proving this would require much more precise estimates, including among other things a qualitative improvement of the constants in Theorem 4.20 (recall Remark 4.23).

Remark 13.3. One could also relax the analyticity of$f ^ { 0 }$, but there is little incentive to do so.

Sketch of proof. We first decompose$h _ { i } = f _ { i } - f ^ { 0 }$, using truncation by a smooth partition of unity in Fourier space,

$$
h _ {i} = \sum_ {n = 0} ^ {\infty} \mathcal {F} ^ {- 1} (\tilde {h} _ {i} \chi_ {n}) \equiv \sum_ {n = 0} ^ {\infty} h _ {i} ^ {n},
$$

where$\mathcal { F }$is the Fourier transform. Each bump function$\chi _ { n }$should be localized around the domain (in Fourier space)

$$
D _ {n} = \left\{\left(k, \eta\right) \in \mathbb {Z} ^ {d} \times \mathbb {R} ^ {d}: n ^ {K} \leqslant | (k, \eta) | \leqslant (n + 1) ^ {K} \right\},
$$

for some exponent$K > 1 ;$but at the same time$\mathcal { F } ^ { - 1 } ( \chi _ { n } )$should be exponentially decreasing in v. To achieve this, we let

$$
\chi_ {n} = 1 _ {D _ {n}} * \gamma \quad \mathrm{and} \quad \gamma (\eta) = e ^ {- \pi | \eta | ^ {2}}.
$$

Then$\scriptstyle { \mathcal { F } } ^ { - 1 } ( \chi _ { n } ) = { \mathcal { F } } ^ { - 1 } ( 1 _ { D _ { n } } ) \gamma$has Gaussian decay, independently of$n ;$so there is a uniform bound on

$$
\int_ {\mathbb {T} ^ {d}} \int_ {\mathbb {R} ^ {d}} | h _ {i} ^ {n} (x, v) | e ^ {\beta | v |} d v d x
$$

for some$\beta > 0$

On the other hand, if$( k , \eta ) \in D _ { n }$and$( k ^ { \prime } , \eta ^ { \prime } ) \notin D _ { n - 1 } \cup D _ { n } \cup D _ { n + 1 }$, then

$$
| k - k ^ {\prime} | + | \eta - \eta^ {\prime} | \geqslant c n ^ {K - 1}
$$

for some$c > 0$. From this one obtains, after simple computations,

$$
\left| \chi_ {n} (k, \eta) \right| \leqslant 1 _ {(n - 1) ^ {K} \leqslant | (k, \eta) | \leqslant (n + 2) ^ {K}} + C e ^ {- c n ^ {2 (K - 1)}} e ^ {- c \left(| k | ^ {2} + | \eta | ^ {2}\right)}.
$$

So (with constants$C$and c changing from line to line)

$$
\begin{array}{l} | \tilde {h} _ {i} ^ {n} (k, \eta) | \leqslant C e ^ {- \lambda | k | ^ {1 / \nu}} e ^ {- \lambda | \eta | ^ {1 / \nu}} 1 _ {(n - 1) ^ {K} \leqslant | (k, \eta) | \leqslant (n + 2) ^ {K}} + C e ^ {- c n ^ {2 (K - 1)}} e ^ {- c (| k | + | \eta |)} \\ \leqslant C \max \bigl \{e ^ {- \lambda (n - 1) ^ {K / \nu} / 2}, e ^ {- c n ^ {2 (K - 1)}} \bigr \} e ^ {- \bar {\lambda} _ {n} (| k | + | \eta |)}, \end{array}
$$

where

$$
\bar {\lambda} _ {n} \sim \frac {1}{2} \lambda (n + 2) ^ {- (1 - 1 / \nu) K}.
$$

If$K \geqslant 2$then$2 ( K - 1 ) { > } K / \nu ;$so

$$
\left\| h _ {i} ^ {n} \right\| _ {\mathcal {Y} ^ {\bar {\lambda} _ {n}, \bar {\lambda} _ {n}}} \leqslant C e ^ {- \lambda n ^ {K / \nu} / 2}.
$$

Then we may apply Theorem 4.20 to get a bound on$h _ { i } ^ { n }$in the space$\mathcal { Z } ^ { \hat { \lambda } _ { n } , \hat { \lambda } _ { n } ; 1 }$with $\hat { \lambda } _ { n } { = } \frac { 1 } { 2 } \bar { \lambda } _ { n }$, at the price of a constant exp$( C ( n + 2 ) ^ { ( 1 - 1 / \nu ) K } )$. Assuming$K \nu { > } ( 1 { - } 1 / \nu ) K$ $\mathrm { i . e . , } \nu { < } 2$, we end up with

$$
\left\| h _ {i} ^ {n} \right\| _ {\mathcal {Z} ^ {\hat {\lambda} _ {n}, \hat {\lambda} _ {n}; 1}} = O \big (e ^ {- c n ^ {K / \nu}} \big), \quad \hat {\lambda} _ {n} = \frac {1}{2} \bar {\lambda} _ {n}.\tag{13.4}
$$

Then we run the iteration scheme of$\ S 8$with the following modifications: (1) instead of$h ^ { n } ( 0 , \cdot ) { = } 0$, choose$h ^ { n } ( 0 , \cdot ) { = } h _ { i } ^ { n }$, and (2) choose regularity indices$\lambda _ { n } \sim \hat { \lambda } _ { n }$which tend to zero as n tends to infinity. This generates an additional error term of size$O ( e ^ { - c n ^ { K / \nu } } )$, and imposes that$\lambda _ { n } - \lambda _ { n + 1 }$be of order$n ^ { - [ ( 1 - 1 / \nu ) K + 1 ] }$. When we apply the bilinear estimates from$\ S 6 ,$, we can take$\bar { \lambda } - \lambda$to be of the same order; so$\alpha { = } \alpha _ { n }$and$\varepsilon = \varepsilon _ { n }$can be chosen proportional to$n ^ { - [ ( 1 - 1 / \nu ) K + 1 ] }$. Then the large constants coming from the time-response will be, as in 11, of order$n ^ { q } e ^ { c n ^ { r } }$, with$q \in \mathbb { N }$and$r { = } [ ( 1 { - } 1 / \nu ) K { + } 1 ] \xi$, and the scheme will still converge like$O ( e ^ { - c n ^ { s } } )$for any$s { < } K / \nu ,$provided that$K / \nu > r ,$, i.e.,

$$
\nu - 1 + \frac {\nu}{K} <   \frac {1}{\xi}.
$$

The rest of the argument is similar to what we did in 10–12. In the end the decay rate of any non-zero mode of the spatial density$\varrho$is controlled by

$$
\sum_ {n = 0} ^ {\infty} e ^ {- c n ^ {s}} e ^ {- \lambda_ {n} t} \leqslant \left(\sum_ {n = 0} ^ {\infty} e ^ {- c n ^ {s}}\right) \sup _ {n \geqslant 0} e ^ {- c n ^ {s}} e ^ {- c n ^ {- (1 - 1 / \nu)} t} \leqslant C e ^ {- c t ^ {s / K}},
$$

and the result follows since$s / K$is arbitrarily close to$1 / \nu .$

Remark 13.4. An alternative approach to Gevrey regularity consists in rewriting the whole proof with the help of Gevrey norms such as

$$
\| f \| _ {\mathcal {C} _ {\nu} ^ {\lambda}} = \sum_ {n = 0} ^ {\infty} \frac {\lambda^ {n} \| f ^ {(n)} \| _ {\infty}}{n ! ^ {\nu}} \quad \text { and } \quad \| f \| _ {\mathcal {F} _ {\nu} ^ {\lambda}} = \sum_ {k \in \mathbb {Z}} e ^ {2 \pi \lambda | k | ^ {1 / \nu}} | \hat {f} (k) |,
$$

which satisfy the algebra property for any$\nu \geqslant 1$. Then one can hybridize these norms, rewrite the time-response in this setting, estimate fractional exponential moments of the kernel, etc. The only part which does not seem to adapt to this strategy is$\ S 9$where the analyticity is crucially used for the local result.

Remark 13.5. In a more general$C ^ { r }$context, we do not know whether decay holds for the non-linear Vlasov–Poisson equation. Speculations about this issue can be found in [55] where it is shown that (unlike in the linearized case) one needs more than one derivative on the perturbation. As a first step in this direction, we mention that our methods imply a bound like$O ( \delta / ( 1 + t ) ^ { r - \bar { r } } )$for times$\scriptstyle t = O ( 1 / \delta )$, where ¯r is a constant and$r > { \bar { r } } ,$as soon as the initial perturbation has norm δ in a functional space$\mathcal { W } ^ { r }$involving r derivatives in a certain sense. The reason why this is non-trivial is that the natural time scale for non-linear efects in the Vlasov–Poisson equation is not${ \cal O } ( 1 / \delta )$, but$O ( 1 / \sqrt { \delta } )$, as predicted by O’Neil [75] and very well checked in numerical simulations$[ 6 1 ] . ( ^ { 1 7 } )$Let us sketch the argument in a few lines. Assume that (for some positive constants c and C)

$$
h _ {i} = \sum_ {n = 0} ^ {\infty} h _ {i} ^ {n}, \quad \| h _ {i} ^ {n} \| _ {\mathcal {Z} ^ {\lambda_ {n}, \lambda_ {n}; 1}} \leqslant \frac {C ^ {n}}{2 ^ {r n}} \quad \text { and } \quad \lambda_ {n} = \frac {c n}{2 ^ {n}}.\tag{13.5}
$$

Then we may run the Newton scheme again choosing$\alpha _ { n } { \sim } c n / 2 ^ { n } , c _ { n } { = } O ( \delta 2 ^ { - ( r - r _ { 1 } ) n } )$and $\varepsilon _ { n } = c ^ { \prime } \delta$. Over a time-interval of length${ \cal O } ( 1 / \delta )$, Theorem$7 . 7 ( \mathrm { i i } )$only yields a multiplicative constant$O ( e ^ { c \delta t } / \alpha _ { n } ^ { 9 } ) { = } O ( 2 ^ { 1 0 n } )$. In the end, after Sobolev injection again, we recover a time-decay on the force$F$like

$$
\delta \sum_ {n = 0} ^ {\infty} 2 ^ {n r _ {2}} 2 ^ {- n r} e ^ {- \lambda_ {n} t} \leqslant C \delta \sup _ {n \geqslant 0} (2 ^ {- n (r - r _ {3})} e ^ {- \lambda_ {n} t}) \leqslant \frac {C \delta}{(1 + t) ^ {r - r _ {4}}},
$$

as desired. Equation (13.5) means that$h _ { i }$is of size$O ( \delta )$in a functional space$\mathcal { W } ^ { r }$whose definition is close to the Littlewood–Paley characterization of a Sobolev space with$r$ derivatives. In fact, if the conjecture formulated in Remark 4.23 holds true, then it can be shown that$\mathcal { W } ^ { r }$contains all functions in the Sobolev space$W ^ { r + r _ { 0 } , 2 }$satisfying an adequate moment condition, for some constant$r _ { 0 }$.

## 14. Expansions and counterexamples

A most important consequence of the proof of Theorem 2.6 is that the asymptotic behavior of the solution of the non-linear Vlasov equation can in principle be determined at arbitrary precision as the size of the perturbation tends to 0. Indeed, if we define$g _ { \infty } ^ { k } ( v )$as the large-time limit of$h ^ { k }$(say in positive time), then$\| g ^ { k } \| { = } O ( \delta _ { k } )$, so$f ^ { 0 } + g _ { \infty } ^ { 1 } + \ldots + g _ { \infty } ^ { n }$ converges very fast to$f _ { \infty }$. In other words, to investigate the properties of the timeasymptotics of the system, we may freely exchange the limits$t \to \infty$and$\delta \to 0$, perform expansions, etc. This at once puts on rigorous grounds many asymptotic expansions used by various authors—who so far implicitly postulated the possibility of this exchange.

With this in mind, let us estimate the first corrections to the linearized theory, in the regime of a very small perturbation and small interaction strength (which can be achieved by a proper scaling of physical quantities). We shall work in dimension$d { = } 1$ and in a periodic box of length$L { = } 1$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>O(1/</sub>√<sub>δ</sub> <sub>)</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">O(1/δ)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">O(1/δ)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>17</sup>) Passing from to is arguably an infinite-dimensional counterpart of Laplace’s averaging principle, which yields stability for certain Hamiltonian systems over time-intervalsO(1/δ<sup>2</sup>) rather than .</span></small>

## 14.1. Simple excitation

For a start, let us consider the case where the perturbation afects only the first spatial frequency. We let

$f ^ { 0 } ( v ) { = } e ^ { - \pi v ^ { 2 } }$be the homogeneous (Maxwellian) distribution;

${ \varepsilon } \varrho _ { i } ( x ) { = } { \varepsilon } \cos ( 2 \pi x )$be the initial space density perturbation;

$\varepsilon \varrho _ { i } ( x ) \theta ( v )$be the initial perturbation of the distribution function; we denote by $\varphi$the Fourier transform of$\theta ;$

αW be the interaction potential, with$W ( - x ) { = } W ( x )$. We do not specify its form, but it should satisfy the assumptions in Theorem 2.6.

We work in the asymptotic regime$\varepsilon \to 0$and$\alpha \to 0$. The parameter ε measures the size of the perturbation, while α measures the strength of the interaction; after dimensional change, if W is an inverse power, α can be thought of as an inverse power of the ratio (Debye length)/(perturbation wavelength). We will not write norms explicitly, but all our computations can be made in the norms introduced in$\ S 4$, with small losses in the regularity indices—as we have done throughout the paper.

The first-order correction$h ^ { 1 } { = } O ( \varepsilon ) \ t o \ f ^ { 0 }$is provided by the solution of the linearized equation (3.3), here taking the form

$$
\partial_ {t} h ^ {1} + v \cdot \nabla_ {x} h ^ {1} + F [ h ^ {1} ] \cdot \nabla_ {v} f ^ {0} = 0,
$$

with initial datum$h ^ { 1 } ( 0 , \cdot ) = h _ { i } { : = } f _ { i } - f ^ { 0 }$. As in$\ S 3$we get a closed equation for the associated density$\varrho [ h ^ { 1 } ]$

$$
\hat {\varrho} [ h ^ {1} ] (t, k) = \tilde {h} _ {i} (k, k t) - 4 \pi^ {2} \alpha \widehat {W} (k) \int_ {0} ^ {t} \hat {\varrho} [ h ^ {1} ] (\tau , k) e ^ {- \pi (k (t - \tau)) ^ {2}} (t - \tau) k ^ {2} d \tau .
$$

It follows that$\hat { \varrho } [ h ^ { 1 } ] ( t , k ) = 0$for$k \neq \pm 1$, so the behavior of$\hat { \varrho } [ h ^ { 1 } ]$is entirely determined by $u _ { 1 } ( t ) = \hat { \varrho } [ h ^ { 1 } ] ( t , 1 )$and$u _ { - 1 } ( t ) = \hat { \varrho } [ h ^ { 1 } ] ( t , - 1 )$), which satisfy

$$
u _ {1} (t) = \frac {\varepsilon}{2} \varphi (t) - 4 \pi^ {2} \alpha \widehat {W} (1) \int_ {0} ^ {t} u _ {1} (\tau) e ^ {- \pi (t - \tau) ^ {2}} (t - \tau) d \tau = \frac {\varepsilon}{2} [ \varphi (t) + O (\alpha) ].\tag{14.1}
$$

(This equation can be solved explicitly [11, equation (6)], but we only need the expansion.) Similarly,

$$
u _ {- 1} (t) = \frac {\varepsilon}{2} \varphi (- t) - 4 \pi^ {2} \alpha \widehat {W} (1) \int_ {0} ^ {t} u _ {- 1} (\tau) e ^ {- \pi (t - \tau) ^ {2}} (t - \tau) d \tau = \frac {\varepsilon}{2} [ \varphi (- t) + O (\alpha) ].\tag{14.2}
$$

The corresponding force, in Fourier transform, is given by

$$
\widehat {F} ^ {1} (t, 1) = - 2 i \pi \alpha \widehat {W} (1) u _ {1} (t) \quad \text { and } \quad \widehat {F} ^ {1} (t, - 1) = 2 i \pi \alpha \widehat {W} (1) u _ {- 1} (t).
$$

From this we also deduce the Fourier transform of$h ^ { 1 }$itself:

$$
\tilde {h} ^ {1} (t, k, \eta) = \tilde {h} _ {i} (k, \eta + k t) - 4 \pi^ {2} \alpha \widehat {W} (k) \int_ {0} ^ {t} \hat {\varrho} [ h ^ {1} ] (\tau , k) e ^ {- \pi (\eta + k (t - \tau)) ^ {2}} (\eta + k (t - \tau)) \cdot k d \tau .\tag{14.3}
$$

This is 0 if$k \neq \pm 1$, while

$$
\begin{array}{c} \tilde {h} ^ {1} (t, 1, \eta) = \frac {\varepsilon}{2} \varphi (\eta + t) - 4 \pi^ {2} \alpha \widehat {W} (1) \int_ {0} ^ {t} u _ {1} (\tau) e ^ {- \pi (\eta + (t - \tau)) ^ {2}} (\eta + (t - \tau))   d \tau \\ = \frac {\varepsilon}{2} [ \varphi (\eta + t) + O (\alpha) ] \end{array}\tag{14.4}
$$

and

$$
\begin{array}{c} \tilde {h} ^ {1} (t, - 1, \eta) = \frac {\varepsilon}{2} \varphi (\eta - t) + 4 \pi^ {2} \alpha \widehat {W} (1) \int_ {0} ^ {t} u _ {- 1} (\tau) e ^ {- \pi (\eta - (t - \tau)) ^ {2}} (\eta - (t - \tau))   d \tau \\ = \frac {\varepsilon}{2} [ \varphi (\eta - t) + O (\alpha) ]. \end{array}\tag{14.5}
$$

To get the next order correction, we solve, as in$\ S 1 0$,

$$
\partial_ {t} h ^ {2} + v \cdot \nabla_ {x} h ^ {2} + F [ h ^ {1} ] \cdot \nabla_ {v} h ^ {2} + F [ h ^ {2} ] \cdot (\nabla_ {v} f ^ {0} + \nabla_ {v} h ^ {1}) = - F [ h ^ {1} ] \cdot \nabla_ {v} h ^ {1},
$$

with zero initial datum. Since$h ^ { 2 } { = } O ( \varepsilon ^ { 2 } )$, we may neglect the terms$F [ h ^ { 1 } ] \cdot \nabla _ { v } h ^ { 2 }$and $F [ h ^ { 2 } ] \cdot \nabla _ { v } h ^ { 1 }$which are both$O ( \alpha \varepsilon ^ { 3 } )$. So it is suficient to solve

$$
\partial_ {t} h _ {2} ^ {\prime} + v \cdot \nabla_ {x} h _ {2} ^ {\prime} + F [ h _ {2} ^ {\prime} ] \cdot \nabla_ {v} f ^ {0} = - F [ h ^ {1} ] \cdot \nabla_ {v} h ^ {1}\tag{14.6}
$$

with vanishing initial datum. As$t \to \infty$, we know that the solution$h _ { 2 } ^ { \prime } ( t , x , v )$is asymptotically close to its spatial average$\langle h _ { 2 } ^ { \prime } \rangle = \int _ { \mathbb { T } ^ { d } } h _ { 2 } ^ { \prime }$dx. Taking the integral over$\mathbb { T } ^ { d }$in (14.6) yields

$$
\partial_ {t} \langle h _ {2} ^ {\prime} \rangle = - \langle F [ h ^ {1} ] \cdot \nabla_ {v} h ^ {1} \rangle .
$$

Since$h ^ { 1 }$converges to$\left. h _ { i } \right.$, the deviation of$f$to$\langle f _ { i } \rangle$is given, at order$\varepsilon ^ { 2 } .$, by

$$
g (v) = - \int_ {0} ^ {\infty} \langle F [ h _ {1} ] \cdot \nabla_ {v} h ^ {1} \rangle (t, v) d t = - \int_ {0} ^ {\infty} \sum_ {k \in \mathbb {Z}} \widehat {F} [ h ^ {1} ] (t, - k) \cdot \nabla_ {v} \hat {h} ^ {1} (t, k, v) d t.
$$

Applying the Fourier transform and using (14.1), (14.2), (14.4) and (14.5), we deduce

$$
\begin{array}{l} \widetilde {g} (\eta) = - \int_ {0} ^ {\infty} \sum_ {k \in \mathbb {Z}} \widehat {F} [ h ^ {1} ] (t, - k) \cdot \widetilde {\nabla_ {v} h ^ {1}} (t, k, \eta) d t \\ = - \int_ {0} ^ {\infty} \widehat {F} [ h ^ {1} ] (t, - 1) (2 i \pi \eta) \widetilde {h} ^ {1} (t, 1, \eta) d t - \int_ {0} ^ {\infty} \widehat {F} [ h ^ {1} ] (t, 1) (2 i \pi \eta) \widetilde {h} ^ {1} (t, - 1, \eta) d t \\ = \pi^ {2} \varepsilon^ {2} \alpha \widehat {W} (1) \eta \biggl (\int_ {0} ^ {\infty} \varphi (- t) \varphi (\eta + t) d t - \int_ {0} ^ {\infty} \varphi (t) \varphi (\eta - t) d t + O (\alpha) \biggr) \\ = - \pi^ {2} \varepsilon^ {2} \alpha \widehat {W} (1) \eta \biggl (\int_ {- \infty} ^ {\infty} \varphi (t) \varphi (\eta - t) \operatorname{sign} (t) d t + O (\alpha) \biggr). \end{array}
$$

Summarizing,

$$
\left\{ \begin{array}{l} \lim _ {t \to \infty} \tilde {f} (t, k, \eta) = 0, \quad \text {if} k \neq 0, \\ \lim _ {t \to \infty} \tilde {f} (t, 0, \eta) = \tilde {f} _ {i} (t, 0, \eta) - \varepsilon^ {2} \alpha (\pi^ {2} \widehat {W} (1)) \eta \bigg (\int_ {- \infty} ^ {\infty} \varphi (t) \varphi (\eta - t) \operatorname{sign} (t) d t + O (\alpha) \bigg). \end{array} \right.\tag{14.7}
$$

Since$\varphi$is an arbitrary analytic profile, this simple calculation already shows that the asymptotic profile is not necessarily the spatial mean of the initial datum.

Assuming$\varepsilon \ll \alpha$, higher-order expansions in α can be obtained by bootstrap on the equations (14.1), (14.2), (14.4) and (14.5); for instance,

$$
\begin{array}{r l} & {\underset {t \to \infty} {\lim} \tilde {f} (t, 0, \eta)} \\ & {\quad = \tilde {f} _ {i} (0, \eta) - \varepsilon^ {2} \alpha (\pi^ {2} \widehat {W} (1)) \eta \int_ {- \infty} ^ {\infty} \varphi (t) \varphi (\eta - t) \operatorname{sign} (t) d t} \\ & {\qquad - \varepsilon^ {2} \alpha^ {2} (2 \pi^ {2} \widehat {W} (1)) ^ {2} \eta \int_ {0} ^ {\infty} \int_ {0} ^ {t} \big [ (\varphi (\eta + t) \varphi (- \tau) - \varphi (\eta - t) \varphi (\tau)) e ^ {- \pi (t - \tau) ^ {2}} (t - \tau)} \\ & {\qquad + \varphi (\tau) \varphi (- t) e ^ {- \pi (\eta + (t - \tau)) ^ {2}} (\eta + t - \tau)} \\ & {\qquad + \varphi (- \tau) \varphi (t) e ^ {- \pi (\eta - (t - \tau)) ^ {2}} (\eta - t - \tau) \big ] d \tau d t + O (\varepsilon^ {2} \alpha^ {3}).} \end{array}
$$

What about the limit in negative time? Reversing time is equivalent to changing $f ( t , x , v )$into$f ( t , x , - v )$and letting time go forward. So we define$S ( v ) { : = } - v$and

$$
T (\varphi) (\eta) := \varepsilon^ {2} \alpha \pi^ {2} \widehat {W} (1) \eta \int_ {- \infty} ^ {\infty} \varphi (t) \varphi (\eta - t) \mathrm{sign} (t) d t;
$$

then$T ( \varphi \circ S ) { = } T ( \varphi ) \circ S .$, which means that the solutions constructed above are always homoclinic at order$O ( \varepsilon ^ { 2 } \alpha )$. The same is true for the more precise expansions at order $O ( \varepsilon ^ { 2 } \alpha ^ { 2 } )$, and in fact it can be checked that the whole distribution$f ^ { 2 }$is homoclinic; in other words,$f$is homoclinic up to possible corrections of order$O ( \varepsilon ^ { 4 } )$. To exhibit heteroclinic deviations, we shall consider more general perturbations.

## 14.2. General perturbation

Let us now consider a “general” initial datum$f _ { i } ( x , v )$close to$f ^ { 0 } ( v )$, and expand the solution$f .$. We write$\varepsilon \varphi _ { k } ( \eta ) = ( f _ { i } - f ^ { 0 } ) ^ { \sim } ( k , \eta )$and$\varrho ^ { m } = \varrho [ h ^ { m } ]$. The interaction potential is assumed to be of the form αW with$\alpha \ll 1$and$W ( x ) { = } W ( - x )$. The first equations of the Newton scheme are

$$
\hat {\varrho} ^ {1} (t, k) = \varepsilon \varphi_ {k} (k t) - 4 \pi^ {2} \alpha \widehat {W} (k) \int_ {0} ^ {t} \hat {\varrho} ^ {1} (\tau , k) \tilde {f} ^ {0} (k (t - \tau)) | k | ^ {2} (t - \tau) d \tau ,\tag{14.8}
$$

(14.9)

$$
\begin{array}{l} \tilde {h} ^ {1} (t, k, \eta) = \varepsilon \varphi_ {k} (\eta + k t) - 4 \pi^ {2} \alpha \widehat {W} (k) \int_ {0} ^ {t} \hat {\varrho} ^ {1} (\tau , k) \tilde {f} ^ {0} (\eta + k (t - \tau)) k \cdot (\eta + k (t - \tau))   d \tau , \\ \tilde {h} ^ {2} (t, k, \eta) = - 4 \pi^ {2} \alpha \widehat {W} (k) \int_ {0} ^ {t} \hat {\varrho} ^ {2} (\tau , k) \tilde {f} ^ {0} (\eta + k (t - \tau)) k \cdot (\eta + k (t - \tau))   d \tau \\ \qquad - 4 \pi^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \hat {\varrho} ^ {1} (\tau , l) \tilde {h} ^ {1} (\tau , k - l, \eta + k (t - \tau)) l \cdot (\eta + k (t - \tau))   d \tau \\ \qquad - 4 \pi^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \hat {\varrho} ^ {2} (\tau , l) \tilde {h} ^ {1} (\tau , k - l, \eta + k (t - \tau)) l \cdot (\eta + k (t - \tau))   d \tau \\ \qquad - 4 \pi^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (i) \hat {\varrho} ^ {1} (\tau , i) \tilde {h} ^ {2} (\tau , k - l, \eta + k (t - \tau)) i \cdot (\eta + k (t - \tau))   d \tau , \end{array}\tag{14.10}
$$

$$
\begin{array}{r l} & {\widehat {\varrho} ^ {2} (t, k) = - 4 \pi^ {2} \alpha \widehat {W} (k) \int_ {0} ^ {t} \widehat {\varrho} ^ {2} (\tau , k) \tilde {f} ^ {0} (k (t - \tau)) | k | ^ {2} (t - \tau) d \tau} \\ & {- 4 \pi^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \widehat {\varrho} ^ {1} (\tau , l) \tilde {h} ^ {1} (\tau , k - l, k (t - \tau)) l \cdot k (t - \tau) d \tau} \\ & {- 4 \pi^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \widehat {\varrho} ^ {2} (\tau , l) \tilde {h} ^ {1} (\tau , k - l, k (t - \tau)) l \cdot k (t - \tau) d \tau} \\ & {- 4 \pi^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \widehat {\varrho^ {1}} (\tau , l) \tilde {h} ^ {2} (\tau , k - l, k (t - \tau)) l \cdot k (t - \tau) d \tau .} \end{array}\tag{14.11}
$$

Here$k$runs over$\mathbb { Z } ^ { d }$

From (14.8) and (14.9) we see that$\varrho ^ { 1 }$and$h ^ { 1 }$depend linearly on$\varepsilon ,$and that

$$
\hat {\varrho} ^ {1} (t, k) = \varepsilon [ \varphi_ {k} (k t) + O (\alpha) ] \quad \text { and } \quad \tilde {h} ^ {1} (t, k, \eta) = \varepsilon [ \varphi_ {k} (\eta + k t) + O (\alpha) ].\tag{14.12}
$$

Then from (14.10) and (14.11),$\varrho ^ { 2 }$and$h ^ { 2 }$are$O ( \varepsilon ^ { 2 } \alpha )$; so by plugging (14.12) into these equations we obtain

$$
\widehat {\varrho} ^ {2} (t, k) = - 4 \pi^ {2} \varepsilon^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \varphi_ {l} (l \tau) \varphi_ {k - l} (k t - l \tau) l \cdot k (t - \tau) d \tau + O (\varepsilon^ {2} \alpha^ {2}) + O (\varepsilon^ {3} \alpha)\tag{14.13}
$$

and

$$
\begin{array}{l} \tilde {h} ^ {2} (t, k, \eta) = - 4 \pi^ {2} \varepsilon^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \varphi_ {l} (l \tau) \varphi_ {k - l} (\eta + k t - l \tau) l \cdot (\eta + k (t - \tau))   d \tau \\ \qquad + O (\varepsilon^ {2} \alpha^ {2}) + O (\varepsilon^ {3} \alpha). \end{array}\tag{14.14}
$$

We plug these bounds again into the right-hand side of (14.10) to find tha

$$
\tilde {h} ^ {2} (t, 0, \eta) = \mathbb {I} _ {\varepsilon} (t, \eta) + \mathbb {I I I} _ {\varepsilon} (t, \eta) + O (\varepsilon^ {3} \alpha^ {3}),\tag{14.15}
$$

where

$$
\mathbb {I} _ {\varepsilon} (t, \eta) = - 4 \pi^ {2} \alpha \int_ {0} ^ {t} \sum_ {l \in \mathbb {Z} ^ {d}} (l \cdot \eta) \widehat {W} (l) \widehat {\varrho} ^ {1} (\tau , l) \tilde {h} ^ {1} (\tau , - l, \eta) d \tau
$$

is quadratic in$\varepsilon ,$and$\textstyle \mathbb { I I } _ { \varepsilon } ( t , \eta )$is a third-order correction:

$$
\begin{array}{r l} & {\mathrm{III} _ {\varepsilon} (t, \eta) = 1 6 \pi^ {4} \varepsilon^ {3} \alpha^ {2} \sum_ {m, l \in \mathbb {Z} ^ {d}} \widehat {W} (l) \widehat {W} (m)} \\ & {\qquad \times \int_ {0} ^ {t} \int_ {0} ^ {\tau} \varphi_ {m} (m s) \big [ \varphi_ {l - m} (l \tau - m s) \varphi_ {- l} (\eta - l \tau) (l \cdot m) (\tau - s)} \\ & {\qquad + \varphi_ {l} (l \tau) \varphi_ {- l - m} (\eta - l \tau - m s) m \cdot (\eta - l (\tau - s)) \big ] (l \cdot \eta) d s d \tau .} \end{array}\tag{14.16}
$$

If$\tilde { f } ^ { 0 }$is even, changing$\varphi _ { k }$into$\varphi _ { k } ( - \cdot )$and η into$- \eta$amounts to change k into $- k$at the level of (14.8) and (14.9); but then$\mathbb { I } _ { \varepsilon }$is invariant under this operation. We conclude that$f$is always homoclinic at second order in$\varepsilon ,$, and we consider the influence of the third-order term (14.16). Let

$$
C [ \varphi ] (\eta) := \lim _ {t \to \infty} \operatorname{III} _ {\varepsilon} (t, \eta).
$$

After some relabeling, we find that

$$
\begin{array}{r l} & C [ \varphi ] (\eta) = 1 6 \pi^ {4} \varepsilon^ {3} \alpha^ {2} \sum_ {k, l \in \mathbb {Z} ^ {d}} \widehat {W} (k) \widehat {W} (l) \\ & \qquad \times \int_ {0} ^ {\infty} \int_ {0} ^ {t} \varphi_ {l} (l \tau) \left[ \varphi_ {k - l} (k t - l \tau) \varphi_ {- k} (\eta - k t) (k \cdot l) (t - \tau) + \varphi_ {k} (k t) \varphi_ {- k - l} (\eta - k t - l \tau) l \cdot (\eta - k (t - \tau)) \right] (k \cdot \eta) d \tau d t. \end{array}\tag{14.17}
$$

Now assume that$\varphi _ { - k } = \sigma \varphi _ { k }$with$\sigma = \pm 1 \ ( \sigma = 1$means that the perturbation is even in$x ,$ $\sigma { = } { - } 1$that it is odd.) Using the symmetry$( k , l )  ( - k , - l )$one can check that

$$
C [ \varphi \circ S ] \circ S = \sigma C [ \varphi ],
$$

where$S ( z ) { = } { - } z$. In particular, if the perturbation is odd in$x ,$then the third-order correction imposes a heteroclinic behavior for the solution, as soon as$C [ \varphi ] { \neq } 0$

To construct an example where$C [ \varphi ] { \neq } 0 .$, we set$d { = } 1 , f ^ { 0 } { = } ($Gaussian,

$$
f _ {i} - f ^ {0} = \sin (2 \pi x) \theta_ {1} (v) + \sin (4 \pi x) \theta_ {2} (v),
$$

$\varphi _ { 1 } = - \varphi _ { - 1 } = \frac { 1 } { 2 } \tilde { \theta } _ { 1 }$and$\varphi _ { 2 } { = } { - } \varphi _ { - 2 } { = } \frac { 1 } { 2 } \tilde { \theta } _ { 2 }$. The six pairs$( k , l )$contributing to (14.17) are $( - 1 , 1 ) , ( 1 , - 1 ) , ( 1 , 2 ) , ( 2 , 1 ) , ( - 1 , - 2 )$and$( - 2 , - 1 )$), By playing with the respective sizes of$\widehat { W } ( 1 )$and$\widehat W ( 2 )$(which amounts in fact to changing the size of the box), it is suficient  to consider the terms with coeficient${ \widehat { W } } ( 1 ) ^ { 2 }$, i.e., the pairs$( - 1 , 1 )$and$( 1 , - 1 )$). Then the corresponding bit of$C [ \varphi ] ( \eta )$is

$$
\begin{array}{r l} & {- 1 6 \pi^ {4} \varepsilon^ {3} \alpha^ {2} \widehat {W} (1) ^ {2} \eta \int_ {0} ^ {\infty} \int_ {0} ^ {t} \left[ \varphi_ {1} (\tau) \varphi_ {1} (\eta + t) \varphi_ {2} (- t + \tau) (t - \tau) \right.} \\ & {\qquad \qquad \qquad \qquad \qquad \qquad + \varphi_ {1} (\tau) \varphi_ {1} (t) \varphi_ {2} (\eta + t - \tau) (\eta + t - \tau)} \\ & {\qquad \qquad \qquad \qquad \qquad + \varphi_ {1} (- \tau) \varphi_ {1} (\eta - t) \varphi_ {2} (t + \tau) (t - \tau)} \\ & {\qquad \qquad \qquad \qquad \qquad \left. + \varphi_ {1} (- \tau) \varphi_ {1} (t) \varphi_ {2} (\eta - t + \tau) (t - \tau - \eta) \right] d \tau d t.} \end{array}
$$

If we let$\varphi _ { 1 }$and$\varphi _ { 2 }$vary in such a way that they become positive and almost concentrated on$\mathbb { R } _ { + }$, the only remaining term is the one in$\varphi _ { 1 } ( \tau ) \varphi _ { 2 } ( \eta + t - \tau ) \varphi _ { 1 } ( t )$, and its contribution is negative for$\eta { > } 0$. So, at least for certain values of$W ( 1 )$and$W ( 2 )$there is a choice of analytic functions$\varphi _ { 1 }$and$\varphi _ { 2 }$, such that$C [ \varphi ] { \neq } 0$. This demonstrates the existence of heteroclinic trajectories.

To summarize: At first order in ε, the convergence is to the spatial average; at second order there is a homoclinic correction; at third order, if at least three modes with zero sum are excited, there is a possibility for heteroclinic behavior.

Remark 14.1. As pointed out to us by Bouchet, the existence of heteroclinic trajectories implies that the asymptotic behavior cannot be predicted on the basis of the invariants of the equation and the interaction; indeed, the latter do not distinguish between the forward and backward solutions.

## 15. Beyond Landau damping

We conclude this paper with some general comments about the physical implications of Landau damping.

Remark 14.1 show in particular that there is no “universal” large-time behavior of the solution of the non-linear Vlasov equation in terms of just, say, conservation laws and the initial datum; the dynamics also have to enter explicitly. One can also interpret this as a lack of ergodicity: the non-linearity is not suficient to make the system explore the space of all “possible” distributions and to choose the most favorable one, whatever this means. Failure of ergodicity for a system of finitely many particles was already known to occur, in relation to the KAM theorem; this is mentioned e.g. in [62, p. 257] for the vortex system. There it is hoped that such behavior disappears as the dimension tends to infinity; but now we see that it also exists even in the infinite-dimensional setting of the Vlasov equation.

At first, this seems to be bad news for the statistical theory of the Vlasov equation, pioneered by Lynden-Bell [58] and explored by various authors [16], [65], [80], [89], [94], since even the sophisticated variants of this theory try to predict the likely final states in terms of just the characteristics of the initial data. In this sense, our results provide support for an objection raised by Isichenko [42, p. 2372] against the statistical theory.

However, looking more closely at our proofs and results, proponents of the statistica theory will have a lot to rejoice about.

To start with, our results are the first to rigorously establish that the non-linear Vlasov equation does enjoy some asymptotic “stabilization” property in large time, without the help of any extra difusion or ensemble averaging.

Next, the whole analysis is perturbative: each stable spatially homogeneous distribution will have its small “basin of damping”, and it may be that some distributions are “much more stable” than others, say in the sense of having a larger basin.

Even more importantly, in 7 we have crucially used the smoothness to overcome the potentially destabilizing non-linear efects. So any theory based on non-smooth functions might not be constrained by Landau damping. This certainly applies to a statistica theory, for which smooth functions should be a zero-probability set.

Finally, to overcome the non-linearity, we had to cope with huge constants (even qualitatively larger than those appearing in classical KAM theory). If one believes in the explanatory virtues of proofs, these large constants might be the indication that Landau damping is a thin efect, which might be neglected when it comes to predict the “final” state in a “turbulent” situation.

Further work needs to be done to understand whether these considerations apply equally to the electrostatic and gravitational cases, or whether the electrostatic case is favored in these respects; and what happens in “low” regularity.

Although the underlying mathematical and physical mechanisms difer, non-linear Landau damping (as defined by Theorem 2.6) may arguably be to the theory of the Vlasov equation what the KAM theorem is to the theory of Hamiltonian systems. Like the KAM theorem, it might be conceptually important in theory and practice, and stil be severely limited.(<sup>18</sup>)

Beyond the range of application of KAM theory lies the softer, more robust weak KAM theory developed by Fathi [26] in relation to Aubry–Mather theory. By a nice co-incidence, a Vlasov version of the weak KAM theory has just been developed by Gangbo and Tudorascu [29], although with no relation to Landau damping. Making the connection is just one of the many developments which may be explored in the future.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(<sup>18</sup>) It is a well-known scientific paradox that the KAM theorem was at the same time tremendously influential in the science of the twentieth century, and so restrictive that its assumptions are essentially never satisfied in practice</span></small>

## Appendix

In this appendix we gather some elementary tools, our conventions, and some reminders about calculus. We write$\mathbb { N } _ { 0 } = \{ 0 , 1 , 2 , \dots \}$

## A.1. Calculus in dimension d

For$\boldsymbol { n } \in  { \mathbb { N } } _ { 0 } ^ { d }$we define

$$
n! = n _ {1}! \dots n _ {d}!
$$

and for$n , m \in  { \mathbb { N } } _ { 0 } ^ { d }$we set

$$
\binom{n}{m} = \binom{n _ {1}}{m _ {1}} \dots \binom{n _ {d}}{m _ {d}}.
$$

For$\boldsymbol { z } \in \mathbb { C } ^ { d }$and$n \in \mathbb { Z } ^ { d }$we let

$$
\| z \| = | z _ {1} | + \dots + | z _ {d} |, \quad z ^ {n} = z _ {1} ^ {n _ {1}} \dots z _ {n} ^ {n _ {d}} \in \mathbb {C} \quad \text { and } \quad | z | ^ {n} = | z ^ {n} |.
$$

In particular, for$\boldsymbol { z } \in \mathbb { C } ^ { d }$we have

$$
e ^ {\| z \|} = e ^ {| z _ {1} | + \dots + | z _ {d} |} = \sum_ {n \in \mathbb {N} _ {0} ^ {d}} \frac {\| z \| ^ {n}}{n !}.
$$

We may write$e ^ { | z | }$instead of$e ^ { \| z \| }$

## A.2. Multi-dimensional diferential calculus

The Leibniz formula for functions$f , g \colon  { \mathbb { R } } \to  { \mathbb { R } }$is

$$
(f g) ^ {(n)} = \sum_ {m = 0} ^ {n} {\binom {n} {m}} f ^ {(m)} g ^ {(n - m)},
$$

where of course$f ^ { ( n ) } { = } d ^ { n } f / d x ^ { n }$. The expression of derivatives of composed functions is given by the Fa\`a di Bruno formula:

$$
(f \circ G) ^ {(n)} = \sum_ {\sum_ {j} j m _ {j} = n} \frac {n !}{m _ {1} ! \dots m _ {n} !} (f ^ {(m _ {1} + \dots + m _ {n})} \circ G) \prod_ {j = 1} ^ {n} \left(\frac {G ^ {(j)}}{j !}\right) ^ {m _ {j}}.
$$

These formulae remain valid in several dimensions, provided that one defines, for a multi-index$n { = } ( n _ { 1 } , { \ldots } , n _ { d } )$,

$$
f ^ {(n)} = \frac {\partial^ {n _ {1}}}{\partial x _ {1} ^ {n _ {1}}} \dots \frac {\partial^ {n _ {d}}}{\partial x _ {d} ^ {n _ {d}}} f.
$$

They also remain true if$( \partial _ { 1 } , . . . , \partial _ { d } )$is replaced by a d-tuple of commuting derivation operators.

As a consequence, we shall establish the following Leibniz-type formula for operators which are combinations of gradients and multiplications.

Lemma A.1. Let f and g be functions of$v \in \mathbb { R } ^ { d }$and$a , b \in \mathbb { C } ^ { d }$. Then for any$\boldsymbol { n } \in \mathbb { N } ^ { d }$

$$
(\nabla_ {v} + (a + b)) ^ {n} (f g) = \sum_ {0 \leqslant m \leqslant n} \binom {n} {m} (\nabla_ {v} + a) ^ {m} f (\nabla_ {v} + b) ^ {n - m} g.
$$

Proof. The right-hand side is equal to

$$
\sum_{\substack{0\leqslant q\leqslant m\leqslant n\\ 0\leqslant r\leqslant n - m}}\binom {n}{m}\binom {m}{q}\binom {n - m}{r}\nabla_{v}^{q}f\nabla_{v}^{r}ga^{m - q}b^{n - m - r}.
$$

After changing indices$\scriptstyle p = q + r$and$s { = } m { - } q$, this becomes

$$
\sum_{\substack{0\leqslant r\leqslant p\leqslant n\\ 0\leqslant s\leqslant n - p}}\binom {n}{p}\binom {p}{r}\binom{n - p}{s}\nabla^{r}_{v}g\nabla^{p - r}_{v}fa^{s}b^{n - p - s} = \sum_{p}\binom {n}{p}\nabla^{p}_{v}(fg)(a + b)^{n - p}\\ = (\nabla_{v} + (a + b))^{n}(fg).
$$

## A.3. Fourier transform

For a function$f \colon  { \mathbb { R } ^ { d } } \to  { \mathbb { R } }$, we define

$$
\tilde {f} (\eta) = \int_ {\mathbb {R} ^ {d}} e ^ {- 2 i \pi \eta \cdot v} f (v) d v.\tag{A.1}
$$

Then we have the usual formulae

$$
f (v) = \int_ {\mathbb {R} ^ {d}} \widetilde {f} (\eta) e ^ {2 i \pi \eta \cdot v} d \eta \quad \mathrm{and} \quad \widetilde {\nabla} f (\eta) = 2 i \pi \eta \widetilde {f} (\eta).
$$

Let$\mathbb { T } _ { L } ^ { d } { = } \mathbb { R } ^ { d } / L \mathbb { Z } ^ { d }$. For a function$f \colon  { \mathbb { T } } _ { L } ^ { d } \to  { \mathbb { R } }$, we define

$$
\hat {f} ^ {(L)} (k) = \int_ {\mathbb {T} _ {L} ^ {d}} e ^ {- 2 i \pi k \cdot x / L} f (x) d x.\tag{A.2}
$$

Then we have

$$
f (x) = \frac {1}{L ^ {d}} \sum_ {k \in \mathbb {Z} ^ {d}} \hat {f} ^ {(L)} (k) e ^ {2 i \pi k \cdot x / L} \quad \text {and} \quad \widehat {\nabla f} ^ {(L)} (k) = 2 i \pi \frac {k}{L} \hat {f} ^ {(L)} (k).
$$

For a function$f \colon  { \mathbb { T } } _ { L } ^ { d } \times  { \mathbb { R } ^ { d } } \to  { \mathbb { R } }$, we define

$$
\tilde {f} ^ {(L)} (k, \eta) = \int_ {\mathbb {T} _ {L} ^ {d}} \int_ {\mathbb {R} ^ {d}} e ^ {- 2 i \pi k \cdot x / L} e ^ {- 2 i \pi \eta \cdot v} f (x, v) d v d x,\tag{A.3}
$$

so that the reconstruction formula reads

$$
f (x, v) = \frac {1}{L ^ {d}} \sum_ {k \in \mathbb {Z} ^ {d}} \int_ {\mathbb {R} ^ {d}} \tilde {f} ^ {(L)} (k, \eta) e ^ {2 i \pi k \cdot x / L} e ^ {2 i \pi \eta \cdot v} d v.
$$

When L=1 we do not specify it: so we just write

$$
\hat {f} = \hat {f} ^ {(1)} \quad \mathrm{and} \quad \tilde {f} = \tilde {f} ^ {(1)}.
$$

(There is no risk of confusion since, in that case, (A.3) and (A.1) coincide.)

## A.4. Fixed-point theorem

The following theorem is one of the many variants of the Picard fixed-point theorem. We write$B ( 0 , R )$for the closed ball of center 0 and radius R.

Theorem A.2. (Fixed-point theorem) Let E be a Banach space,$F \colon E \to E$and $R { = } 2 \| F ( 0 ) \|$. If F: B(0, R) E is <sup>1</sup> -Lipschitz, then it has a unique fixed point in$B ( 0 , R )$

Proof. Uniqueness is obvious. To prove existence, run the classical Picard iterative scheme initialized at 0:$x _ { 0 } { = } 0 , x _ { 1 } { = } F ( 0 ) , x _ { 2 } { = } F ( F ( 0 ) )$, etc. It is clear that$( x _ { n } ) _ { n = 1 } ^ { \infty }$is a Cauchy sequence and$\| x _ { n } \| \leqslant \| F ( 0 ) \| ( 1 + \ldots + 1 / 2 ^ { n } ) \leqslant 2 \| F ( 0 ) \|$, so$x _ { n }$converges in$B ( 0 , R )$ to a fixed point of F.□

## A.5. Plemelj formula

The Plemelj formula states that, in$\mathcal { D } ^ { \prime } ( \mathbb { R } )$,

$$
\frac {1}{x - i 0} = \text { p   .   v   . } \left(\frac {1}{x}\right) + i \pi \delta_ {0},\tag{A.4}
$$

or, equivalently,

$$
\frac {1}{x + i 0} = \text { p   .   v   . } \left(\frac {1}{x}\right) - i \pi \delta_ {0}.\tag{A.5}
$$

Let us give a complete proof of this formula which plays a crucial role in plasma physics.

Proof of (A.4). First we recall that

$$
\text { p   .   v   . } \left(\frac {1}{x}\right) = \lim _ {\varepsilon \rightarrow 0} \frac {1 _ {| x | \geqslant \varepsilon}}{x}.
$$

A more explicit expression can be given for this limit. Let$\chi$be an even function on <sup>R</sup> with$\chi ( 0 ) { = } 1 , \chi { \in } \mathrm { L i p } \cap L ^ { 1 } ( \mathbb { R } )$; in particular

$$
\int_ {\mathbb {R}} \frac {1 _ {| x | \geqslant \varepsilon}}{x} \chi (x) d x = 0
$$

and$( 1 - \chi ( x ) ) / x$is bounded. Then for any$\varphi \in \mathrm { L i p } ( \mathbb { R } ) \cap L ^ { 1 } ( \mathbb { R } )$

$$
\begin{array}{r l}&{\int_ {| x | \geqslant \varepsilon} \frac {\varphi (x)}{x} d x = \int_ {| x | \geqslant \varepsilon} \frac {\varphi (x)}{x} \chi (x) d x + \int_ {| x | \geqslant \varepsilon} \varphi (x) \frac {1 - \chi (x)}{x} d x}\\&{\qquad = \int_ {| x | \geqslant \varepsilon} \frac {\varphi (x) - \varphi (0)}{x} \chi (x) d x + \int_ {| x | \geqslant \varepsilon} \varphi (x) \frac {1 - \chi (x)}{x} d x}\\&{\qquad \rightarrow \int_ {\mathbb {R}} \frac {\varphi (x) - \varphi (0)}{x} \chi (x) d x + \int_ {\mathbb {R}} \varphi (x) \frac {1 - \chi (x)}{x} d x \quad \mathrm{as} \varepsilon \to 0.}\end{array}\tag{A.6}
$$

Then$\left( \mathrm { { A . 4 } } \right)$can be rewritten in the following more explicit way: for any$\varphi \in \mathrm { L i p } ( \mathbb { R } ) \cap L ^ { 1 } ( \mathbb { R } )$ and any χ satisfying the above assumptions,

$$
\lim _ {\lambda \rightarrow 0 ^ {+}} \int_ {\mathbb {R}} \frac {\varphi (x)}{x - i \lambda} d x = \int_ {\mathbb {R}} \frac {\varphi (x) - \varphi (0)}{x} \chi (x) d x + \int_ {\mathbb {R}} \varphi (x) \frac {1 - \chi (x)}{x} d x + i \pi \varphi (0).\tag{A.7}
$$

Now, to prove$\left( \mathrm { A } . 7 \right)$, let us pick such a function$\chi$and write, for$\lambda { > } 0$

$$
\int_ {\mathbb {R}} \frac {\varphi (x)}{x - i \lambda} d x = \int_ {\mathbb {R}} \frac {\varphi (x) - \varphi (0)}{x - i \lambda} \chi (x) d x + \int_ {\mathbb {R}} \varphi (x) \frac {1 - \chi (x)}{x - i \lambda} d x + \varphi (0) \int_ {\mathbb {R}} \frac {\chi (x)}{x - i \lambda} d x.
$$

As$\lambda {  } 0 .$, the first two integrals on the right-hand side converge to the right-hand side of (A.6), and there is an extra term proportional to$\varphi ( 0 ) ;$; so it only remains to check that

$$
\int_ {\mathbb {R}} \frac {\chi (x)}{x - i \lambda} d x \rightarrow i \pi \quad \mathrm{as} \lambda \rightarrow 0 ^ {+}.\tag{A.8}
$$

If (A.8) holds for some particular$\chi$satisfying the requested conditions, then (A.4) follows and it implies that (A.8) holds for any such$\chi .$. So let us pick one particular$\chi ,$say $\chi ( x ) { = } e ^ { - x ^ { 2 } }$, which can be extended throughout the complex plane into a holomorphic function. Then, since the complex integral is invariant under contour deformation,

$$
\int_ {\mathbb {R}} \frac {e ^ {- x ^ {2}}}{x - i \lambda} d x = \int_ {C _ {\varepsilon}} \frac {e ^ {- z ^ {2}}}{z - i \lambda} d z,
$$

where$C _ { \varepsilon }$is the complex contour made of the straight line$( - \infty , - \varepsilon )$, followed by the halfcircle$D _ { \varepsilon } { = } \{ - \varepsilon e ^ { i \theta } { : } 0 { \leqslant } \theta { \leqslant } \pi \}$, followed by the straight line$( \varepsilon , \infty )$. The contributions o both straight lines cancel each other by symmetry, and only the integral on the half-circle $D _ { \varepsilon }$remains.$\mathrm { A s } \lambda {  } 0$this integral approaches$\int _ { D _ { \varepsilon } } e ^ { - z ^ { 2 } } d z / z$, which as$\varepsilon \to 0$becomes close to$\scriptstyle \int _ { D _ { \varepsilon } } d z / z = i \pi$, as was claimed.□

## References

[1] Akhiezer, A., Akhiezer, I., Polovin, R., Sitenko, A. & Stepanov, K., Plasma Electrodynamics. Vol. I: Linear Theory. Vol. II: Non-Linear Theory and Fluctuations. Pergamon Press, Oxford–New York, 1975.

[2] Alinhac, S. & Gerard, P.<sup>´</sup> , Pseudo-Diferential Operators and the Nash–Moser Theorem. Graduate Studies in Mathematics, 82. Amer. Math. Soc., Providence, RI, 2007.

[3] Bach, V., Frohlich, J. & Sigal, I. M.<sup>¨</sup> , Spectral analysis for systems of atoms and molecules coupled to the quantized radiation field. Comm. Math. Phys., 207 (1999), 249–290.

[4] Backus, G., Linearized plasma oscillations in arbitrary electron velocity distributions. J. Math. Phys., 1 (1960), 178–191; erratum, 559.

[5] Balescu, R., Statistical Mechanics of Charged Particles. Monographs in Statistical Physics and Thermodynamics, 4. Wiley, London–New York–Sydney, 1963.

[6] Batt, J. & Rein, G., Global classical solutions of the periodic Vlasov–Poisson system in three dimensions. C. R. Acad. Sci. Paris S´er. I Math., 313 (1991), 411–416.

[7] Belmont, G., Mottez, F., Chust, T. & Hess, S., Existence of non-Landau solutions for Langmuir waves. Phys. of Plasmas, 15 (2008), 052310, 1–14.

[8] Benachour, S., Analyticit´e des solutions des ´equations de Vlasov–Poisson. Ann. Sc. Norm. Super. Pisa Cl. Sci., 16 (1989), 83–104.

[9] Binney, J. & Tremaine, S., Galactic Dynamics. First edition. Princeton Series in Astrophysics. Princeton University Press, Princeton, 1987.

[10] — Galactic Dynamics. Second edition. Princeton Series in Astrophysics. Princeton University Press, Princeton, 2008.

[11] Bouchet, F., Stochastic process of equilibrium fluctuations of a system with long-range interactions. Phys. Rev. E, 70 (2004), 036113, 1–4.

[12] Bourgain, J., Fourier transform restriction phenomena for certain lattice subsets and applications to nonlinear evolution equations. I. Schr¨odinger equations. Geom. Funct. Anal., 3 (1993), 107–156.

[13] Caglioti, E. & Maffei, C., Time asymptotics for solutions of Vlasov–Poisson equation in a circle. J. Stat. Phys., 92 (1998), 301–323.

[14] Case, K. M., Plasma oscillations. Ann. Physics, 7 (1959), 349–364.

[15] Chavanis, P. H., Quasilinear theory of the 2D Euler equation. Phys. Rev. Lett., 84:24 (2000), 5512–5515.

[16] Chavanis, P. H., Sommeria, J., & Robert, R., Statistical mechanics of two-dimensional vortices and collisionless stellar systems. Astrophys. J., 471 (1996), 385–399

[17] Chemin, J. Y., Le syst\`eme de Navier–Stokes incompressible soixante dix ans apr\`es Jean Leray, in Actes des Journ´ees Math´ematiques \`a la M´emoire de Jean Leray, S´emin. Congr., 9, pp. 99–123. Soc. Math. France, Paris, 2004.

[18] Chierchia, L., A. N. Kolmogorov’s 1954 paper on nearly-integrable Hamiltonian systems. A comment on: “On conservation of conditionally periodic motions for a small change in Hamilton’s function” [Dokl. Akad. Nauk SSSR, 98 (1954), 527–530]. Regul. Chaotic Dyn., 13 (2008), 130–139.

[19] Chust, T., Belmont, G., Mottez, F. & Hess, S., Landau and non-Landau linear damping: Physics of the dissipation. Phys. Plasmas, 16 (2009), 092104, 13 pp.

[20] Degond, P., Spectral theory of the linearized Vlasov–Poisson equation. Trans. Amer. Math. Soc., 294 (1986), 435–453.

[21] Derezinski, J. & G<sup>´</sup> erard, C.<sup>´</sup> , Scattering Theory of Classical and Quantum N-Particle Systems. Texts and Monographs in Physics. Springer, Berlin–Heidelberg, 1997.

[22] Desvillettes, L. & Villani, C., On the trend to global equilibrium in spatially inhomogeneous entropy-dissipating systems: the linear Fokker–Planck equation. Comm. Pure Appl. Math., 54 (2001), 1–42.

[23] Elskens, Y., Irreversible behaviours in Vlasov equation and many-body Hamiltonian dynamics: Landau damping, chaos and granularity, in Topics in Kinetic Theory, Fields Inst. Commun., 46, pp. 89–108. Amer. Math. Soc., Providence, RI, 2005.

[24] Elskens, Y. & Escande, D. F., Microscopic Dynamics of Plasmas and Chaos. Institute of Physics, Bristol, 2003.

[25] Escande, D. F., Wave-particle interaction in plasmas: a qualitative approach, in Long-Range Interacting Systems, pp. 13–14, 469–506. Oxford University Press, Oxford, 2010.

[26] Fathi, A., Weak KAM Theory in Lagrangian Dynamics. Cambridge University Press, Cambridge, 2010.

[27] Filbet, F., Numerical simulations. Available online at http://math.univ-lyon1.fr/\~filbet/publication.html.

[28] Fridman, A. M. & Polyachenko, V. L., Physics of Gravitating Systems. Vol. I: Equilibrium and Stability. Vol. II: Nonlinear Collective Processes. Astrophysical Applications. Springer, New York, 1984.

[29] Gangbo, W. & Tudorascu, A., Lagrangian dynamics on an infinite-dimensional torus; a weak KAM theorem. Adv. Math., 224 (2010), 260–292.

[30] Glassey, R. & Schaeffer, J., Time decay for solutions to the linearized Vlasov equation. Transport Theory Statist. Phys., 23 (1994), 411–453.

[31] — On time decay rates in Landau damping. Comm. Partial Diferential Equations, 20 (1995), 647–676.

[32] Gould, R., O’Neil, T. & Malmberg, J., Plasma wave echo. Phys. Rev. Letters, 19:5 (1967), 219–222.

[33] Gross, L., Logarithmic Sobolev inequalities. Amer. J. Math., 97 (1975), 1061–1083.

[34] Guo, Y. & Rein, G., A non-variational approach to non-linear stability in stellar dynamics applied to the King model. Comm. Math. Phys., 271 (2007), 489–509.

[35] Guo, Y. & Strauss, W. A., Nonlinear instability of double-humped equilibria. Ann. Inst. H. Poincar´e Anal. Non Lin´eaire, 12 (1995), 339–352.

[36] ter Haar, D., Men of Physics: L. D. Landau. Selected Reading of Physics, 2. Pergamon Press, Oxford–New York, 1969.

[37] Hauray, M. & Jabin, P. E., N-particles approximation of the Vlasov equations with singular potential. Arch. Ration. Mech. Anal., 183 (2007), 489–524.

[38] Hayes, J. N., On non-Landau damped solutions to the linearized Vlasov equation. Nuovo Cimento, 10:30 (1963), 1048–1063.

[39] Heath, R., Gamba, I., Morrison, P. & Michler, C., A discontinuous Galerkin method for the Vlasov–Poisson system. To appear in J. Comput. Phys.

[40] Horst, E., On the asymptotic growth of the solutions of the Vlasov–Poisson system. Math. Methods Appl. Sci., 16 (1993), 75–86.

[41] Hwang, H. J. & Velazquez, J. J. L.<sup>´</sup> , On the existence of exponentially decreasing solutions of the nonlinear Landau damping problem. Indiana Univ. Math. J., 58:6 (2009), 2623–2660.

[42] Isichenko, M., Nonlinear Landau damping in collisionless plasma and inviscid fluid. Phys. Rev. Lett., 78:12 (1997), 2369–2372.

[43] Jabin, P. E., Averaging lemmas and dispersion estimates for kinetic equations. Riv. Mat. Univ. Parma, 1 (2009), 71–138.

[44] Kaganovich, I. D., Efects of collisions and particle trapping on collisionless heating. Phys. Rev. Lett., 82:2 (1999), 327–330.

[45] van Kampen, N. G., On the theory of stationary waves in plasmas. Physica, 21 (1955), 949–963.

[46] Kandrup, H., Violent relaxation, phase mixing, and gravitational Landau damping. Astrophys. J., 500 (1998), 120–128.

[47] Kiessling, M. K.-H., The “Jeans swindle”: a true story—mathematically speaking. Adv. in Appl. Math., 31 (2003), 132–149.

[48] — Personal communication, 2009.

[49] Krall, N. & Trivelpiece, A., Principles of Plasma Physics. San Francisco Press, San Francisco, 1986.

[50] Kuksin, S. B., Nearly Integrable Infinite-Dimensional Hamiltonian Systems. Lecture Notes in Mathematics, 1556. Springer, Berlin–Heidelberg, 1993.

[51] — Analysis of Hamiltonian PDEs. Oxford Lecture Series in Mathematics and its Applications, 19. Oxford University Press, Oxford, 2000.

[52] Landau, L., On the vibrations of the electronic plasma. Akad. Nauk SSSR. Zhurnal Eksper. Teoret. Fiz., 16 (1946), 574–586 (Russian); English translation in Acad. Sci. USSR. J. Phys., 10 (1946), 25–34. Reproduced in [36].(<sup>19</sup>)

[53] Lemou, M., Mehats, F. & Rapha<sup>´</sup> el, P.<sup>¨</sup> , Orbital stability of spherical galactic models. To appear in Invent. Math.

[54] Lifshitz, E. M. & Pitaevski<sup>˘</sup>ı, L. P., Course of Theoretical Physics [“Landau–Lifshits”]. Vol. 10. Nauka, Moscow, 1979. English translation in Pergamon International Library of Science, Technology, Engineering and Social Studies. Pergamon Press, Oxford–New York, 1981.

[55] Lin, Z. & Zeng, C., BGK waves and non-linear Landau damping. To appear in Comm. Math. Phys.

[56] Lions, P. L. & Perthame, B., Propagation of moments and regularity for the 3- dimensional Vlasov–Poisson system. Invent. Math., 105 (1991), 415–430.

[57] Lynden-Bell, D., The stability and vibrations of a gas of stars. Mon. Not. R. Astr. Soc., 124 (1962), 279–296.

[58] — Statistical mechanics of violent relaxation in stellar systems. Mon. Not. R. Astr. Soc., 136 (1967), 101–121.

[59] Malmberg, J. & Wharton, C., Collisionless damping of electrostatic plasma waves. Phys. Rev. Lett., 13:6 (1964), 184–186.

[60] Malmberg, J., Wharton, C., Gould, R. & O’Neil, T., Plasma wave echo experiment. Phys. Rev. Letters, 20:3 (1968), 95–97.

[61] Manfredi, G., Long-time behavior of non-linear Landau damping. Phys. Rev. Lett., 79:15 (1997), 2815–2818.

[62] Marchioro, C. & Pulvirenti, M., Mathematical Theory of Incompressible Nonviscous Fluids. Applied Mathematical Sciences, 96. Springer, New York, 1994.

[63] Maslov, V. P. & Fedoryuk, M. V., The linear theory of Landau damping. Mat. Sb., 127(169) (1985), 445–475, 559 (Russian); English translation in Math. USSR–Sb., 55 (1986), 437–465.

[64] Medvedev, M. V., Diamond, P. H., Rosenbluth, M. N. & Shevchenko, V. I., Asymptotic theory of non-linear Landau damping and particle trapping in waves of finite amplitude. Phys. Rev. Lett., 81:26 (1998), 5824–5827.

[65] Miller, J., Statistical mechanics of Euler equations in two dimensions. Phys. Rev. Lett., 65:17 (1990), 2137–2140

[66] Morrison, P. J., Hamiltonian description of Vlasov dynamics: action-angle variables for the continuous spectrum, in Proceedings of the Fifth International Workshop on Mathematical Aspects of Fluid and Plasma Dynamics (Maui, HI, 1998), Transport Theory Statist. Phys., 29, pp. 397–414. Taylor & Francis, Philadelphia, PA, 2000.

[67] Moser, J., A rapidly convergent iteration method and non-linear diferential equations. II. Ann. Sc. Norm. Super. Pisa Cl. Sci., 20 (1966), 499–535

[68] — Recollections, in The Arnoldfest (Toronto, ON, 1997), Fields Inst. Commun., 24, pp. 19–21. Amer. Math. Soc., Providence, RI, 1999.

[69] Mouhot, C. & Villani, C., Landau damping. J. Math. Phys., 51 (2010), 015204, 7.

[70] Nash, J., The imbedding problem for Riemannian manifolds. Ann. of Math., 63 (1956), 20–63.

[71] Nekhoroshev, N. N., An exponential estimate of the time of stability of nearly integrable Hamiltonian systems. Uspekhi Mat. Nauk, 32 (1977), 5–66, 287 (Russian); English translation in Russian Math. Surveys, 32 (1977), 1–65.

[72] — An exponential estimate of the time of stability of nearly integrable Hamiltonian systems. II. Trudy Sem. Petrovsk., (1979), 5–50 (Russian); English translation in Topics in Modern Mathematics, pp. 1–58, Contemporary Soviet Mathematics, Consultants Bureau, New York, 1985.

[73] Nirenberg, L., An abstract form of the nonlinear Cauchy–Kowalewski theorem. J. Differential Geom., 6 (1972), 561–576.

[74] Nishida, T., A note on a theorem of Nirenberg. J. Diferential Geom., 12 (1977), 629–633 (1978).

[75] O’Neil, T. M., Collisionless damping of nonlinear plasma oscillations. Phys. Fluids, 8 (1965), 2255–2262.

[76] O’Neil, T. M. & Coroniti, F. V., The collisionless nature of high-temperature plasmas. Rev. Modern Phys., 71:2 (1999), S404–S410.

[77] Penrose, O., Electrostatic instability of a non-Maxwellian plasma. Phys. Fluids, 3 (1960), 258–265.

[78] Pfaffelmoser, K., Global classical solutions of the Vlasov–Poisson system in three dimensions for general initial data. J. Diferential Equations, 95 (1992), 281–303.

[79] Rein, G., Personal communication, 2008.

[80] Robert, R., Statistical mechanics and hydrodynamical turbulence, in Proceedings of the International Congress of Mathematicians (Z¨urich, 1994), Vol. 2, pp. 1523–1531. Birkh¨auser, Basel, 1995.

[81] Ryutov, D. D., Landau damping: half a century with the great discovery. Plasma Phys. Control. Fusion, 41 (1999), A1–A12.

[82] Saenz, A. W.<sup>´</sup> , Long-time behavior of the electric potential and stability in the linearized Vlasov theory. J. Math. Phys., 6 (1965), 859–875.

[83] Saint Raymond, X., A simple Nash–Moser implicit function theorem. Enseign. Math., 35 (1989), 217–226.

[84] ScHAEFFER, J., Global existence of smooth solutions to the Vlasov–Poisson system in three dimensions. Comm. Partial Diferential Equations, 16 (1991), 1313–1335.

[85] Soffer, A. & Weinstein, M. I., Multichannel nonlinear scattering for nonintegrable equations. Comm. Math. Phys., 133 (1990), 119–146.

[86] Spentzouris, L., Ostiguy, J. & Colestock, P., Direct measurement of difusion rates in high energy synchrotrons using longitudinal beam echoes. Phys. Rev. Lett., 76:4 (1996), 620–623.

[87] Stahl, B., Kiessling, M. K.-H. & Schindler, K., Phase transitions in gravitating systems and the formation of condensed objects. Planet. Space Sci., 43 (1995), 271–282.

[88] Stix, T. H., The Theory of Plasma Waves. McGraw-Hill, New York, 1962.

[89] Tremaine, S., Henon, M. & Lynden-Bell, D.<sup>´</sup> , H-functions and mixing in violent relaxation. Mon. Not. R. Astr. Soc., 219 (1986), 285–297.

[90] Turkington, B., Statistical equilibrium measures and coherent states in two-dimensional turbulence. Comm. Pure Appl. Math., 52 (1999), 781–809.

[91] Vekstein, G. E., Landau resonance mechanism for plasma and wind-generated water waves. Amer. J. Phys., 66:10 (1998), 886–892.

[92] Villani, C., A review of mathematical topics in collisional kinetic theory, in Handbook of Mathematical Fluid Dynamics, Vol. I, pp. 71–305. North-Holland, Amsterdam, 2002.

[93] — Hypocoercivity. Mem. Amer. Math. Soc., 202 (2009), iv+141.

[94] Wiechen, H., Ziegler, H. J. & Schindler, K., Relaxation of collisionless self-gravitating matter – the lowest energy state. Mon. Not. R. Astr. Soc., 232 (1988), 623–646.

[95] Zhou, T., Guo, Y. & Shu, C.-W., Numerical study on Landau damping. Phys. D, 157 (2001), 322–333.

Clement Mouhot´

University of Cambridge

DPMMS, Centre for Mathematical Sciences

Wilberforce Road

Cambridge CB3 0WA

U.K.

C.Mouhot@dpmms.cam.ac.uk

Cedric Villani´

Institut Henri Poincar´e & Universit´e de Lyon

Institut Camille Jordan, Universit´e Claude Bernard

43 Boulevard du 11 novembre 1918

FR-69622 Villeurbanne Cedex

France

villani@math.univ-lyon1.fr

Received December 10, 2009

Received in revised form July 10, 2011