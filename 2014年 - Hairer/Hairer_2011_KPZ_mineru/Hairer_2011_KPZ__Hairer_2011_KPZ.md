# Solving the KPZ equation

November 27, 2024

Martin Hairer

The University of Warwick, Email: M.Hairer@Warwick.ac.uk

## Abstract

We introduce a new concept of solution to the KPZ equation which is shown to extend the classical Cole-Hopf solution. This notion provides a factorisation of the Cole-Hopf solution map into a “universal” measurable map from the probability space into an explicitly described auxiliary metric space, composed with a new solution map that has very good continuity properties. The advantage of such a formulation is that it essentially provides a pathwise notion of a solution, together with a very detailed approximation theory. In particular, our construction completely bypasses the Cole-Hopf transform, thus laying the groundwork for proving that the KPZ equation describes the fluctuations of systems in the KPZ universality class.

As a corollary of our construction, we obtain very detailed new regularity results about the solution, as well as its derivative with respect to the initial condition. Other byproducts of the proof include an explicit approximation to the stationary solution of the KPZ equation, a well-posedness result for the Fokker-Planck equation associated to a particle diffusing in a rough space-time dependent potential, and a new periodic homogenisation result for the heat equation with a space-time periodic potential. One ingredient in our construction is an example of a non-Gaussian rough path such that the area process of its natural approximations needs to be renormalised by a diverging term for the approximations to converge.

## Contents

1 Introduction 2  
2 Main results and ideas of proof 11  
3 Elements of rough path theory 26  
4 Fixed point argument 34  
5 Construction of the universal process 46  
6 Treatment of the constant Fourier mode 71  
7 Fine control of the universal process 80  
A Useful computations 93

## 1 Introduction

The aim of this article is to construct and describe solutions to the KPZ equation. At a purely formal level, this equation is given by

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + \lambda (\partial_ {x} h) ^ {2} - \infty + \xi ,\tag{1.1}
$$

where$\ " \infty$denotes an “infinite constant” required to renormalise the divergence appearing in the term$( \partial _ { x } h ) ^ { 2 }$and$\lambda > 0$is a “coupling strength”. Here,$\boldsymbol { h } ( \boldsymbol { x } , t )$is a continuous stochastic process with$x \in S ^ { 1 }$(which we usually identify with [0, 2π], but we will always assume periodic boundary conditions) and$\xi$denotes space-time white noise which is a distribution-valued Gaussian field with correlation function

$$
\mathbf {E} \xi (x, t) \xi (y, s) = 4 \pi \delta (x - y) \delta (t - s).\tag{1.2}
$$

The prefactor 1 in front of the term$\partial _ { x } ^ { 2 } h$and the strange-looking prefactor$4 \pi$in the definition of$\xi$are normalisation constants which could be set to any positive value by rescaling time, h and λ, but our particular choice will simplify some expressions in the sequel.

At this stage, it is of course completely unclear what (1.1) actually means and, in a way, this is the main question that will be addressed in this article. Originally, the equation (1.1) was proposed by Kardar, Parisi and Zhang as a model of surface growth [KPZ86]. However, it was later realised that it is a universal object that describes the fluctuations of a number of strongly interacting models of statistical mechanics with space-time dependencies. For example, it is known rigorously to arise as the fluctuation process for the weakly asymmetric simple exclusion process [BG97], as well as the partition function for directed polymer models [Kar85, IS11, ACQ11]. More generally, the solution to the KPZ equation is expected to describe the fluctuations of a much larger class of systems, namely the systems in the KPZ universality class which is associated to the dynamic scaling exponents$\frac { 3 } { 2 }$, see for example [BQS11]. We refer to the excellent review article [Cor12] for many more references and a more detailed historical account of the KPZ equation.

Over the past ten years or so, substantial progress has been made in the understanding of the solutions to (1.1) (especially in the extended case$x \in \mathbf { R } )$, but very few results had been established rigorously until an explosion of recent results yielding exact formulae for the one-point distribution of solutions to (1.1). A foundation for these results was laid by the groundbreaking work of Johansson [Joh00], who noted a link between discrete approximations to (1.1) and random matrix theory, and who used this to prove that the Tracy-Widom distribution arises as the long-time limit of this discrete model. One stunning recent result was the rigorous proof in [BQS11, ACQ11, CQ10] of the fact that, also for the continuous model (1.1), one has$u ( t ) \approx t ^ { 1 / 3 }$for large times (this had already been conjectured in [KPZ86] and the results in [Joh00] provided further evidence, but the lack of a good approximation theory for (1.1) had defeated earlier attempts) and that, at least for the “infinite wedge” and the “half-Brownian” initial distributions, the law of$t ^ { - 1 / 3 } u ( 0 , t )$, appropriately recentred, does converge, as$t \to \infty$, to the Tracy-Widom distribution. Another very recent achievement exploiting this link is the series of articles [SS09, SS10a, ACQ11, SS10b] in which the authors provide an exact formula for the law of the solution to the KPZ equation at a fixed time and fixed spatial location. These results built on a number of previous results using related ideas, in particular Tracy and Widom’s exact formulae for the asymmetric simple exclusion process [TW08a, TW08b, TW09].

Together with this explosion of exact results on the solutions to (1.1), there has been renewed interest in giving a rigorous interpretation of (1.1). Ever since the seminal work of Bertini and Giacomin [BG97], there has been an accepted notion of solution to (1.1) via the so-called “Cole-Hopf transform”, which had long been known to be useful in the study of the deterministic KPZ / Burgers equation [Hop50, Col51]. The idea is to consider the solution$Z$to the linear multiplicative stochastic heat equation

$$
d Z = \partial_ {x} ^ {2} Z d t + \lambda Z d W (t),\tag{1.3}
$$

where$W$is a cylindrical Brownian motion on$L ^ { 2 } ( S ^ { 1 } )$(i.e. it is the time integral of the space-time white noise$\xi ) .$. Here, the term$Z d W ( t )$should be interpreted as an Ito integral. It is well-known (see for example the monograph [ˆ DPZ92]) that the mild form of (1.3) admits a unique positive solution in a suitable space of adapted processes. One then defines the process h to be given by

$$
h (x, t) = \lambda^ {- 1} \log Z (x, t).\tag{1.4}
$$

In the sequel, we denote this solution by$h = S _ { \mathrm { C H } } ( h _ { 0 } , \omega )$, where$h _ { 0 } = \lambda ^ { - 1 }$log$Z _ { 0 }$ is an initial condition for (1.1). The map${ S _ { \mathrm { C H } } }$is a jointly measurable map from $\mathcal { C } \times \Omega$into$\mathcal { C } ( \mathbf { R } _ { + } , \mathcal { C } ^ { \alpha } )$for every$\begin{array} { r } { \alpha < \frac { 1 } { 2 } } \end{array}$

There are two powerful arguments for this to be the “correct” notion of solution to (1.1). First, one can consider the solution$Z _ { \varepsilon }$to (1.3) with W replaced by$W _ { \varepsilon }$ which is obtained by multiplying the kth Fourier component with$\varphi ( \varepsilon k )$for some smooth cut-off function$\varphi$with compact support and$\varphi ( 0 ) = 1$. Defining$h _ { \varepsilon }$via (1.4) and applying Ito’s formula, it is then possible to verify thatˆ$h _ { \varepsilon }$solves the equation

$$
\partial_ {t} h _ {\varepsilon} = \partial_ {x} ^ {2} h _ {\varepsilon} + \lambda (\partial_ {x} h _ {\varepsilon}) ^ {2} - \lambda C _ {\varepsilon} + \xi_ {\varepsilon},\tag{1.5}
$$

where the constant$C _ { \varepsilon }$is given by$\begin{array} { r } { C _ { \varepsilon } = \sum _ { k \in { \bf Z } } \varphi ^ { 2 } ( k \varepsilon ) \approx \frac { 1 } { \varepsilon } \int _ { \bf R } \varphi ^ { 2 } ( x ) } \end{array}$dx. Since $Z _ { \varepsilon } \to Z { \mathrm { ~ a s ~ } } \varepsilon \to 0$by standard SPDE arguments, it follows that$h _ { \varepsilon }$converges to a limiting process h which, in light of (1.5), does indeed formally solve (1.1).

The second argument in favour of the Cole-Hopf solution is that, as shown in [BG97], the fluctuations of the stationary weakly asymmetric simple exclusion process (WASEP) converge, under a suitable rescaling, to the Cole-Hopf solution to (1.1). This result was further improved recently in [ACQ11] where, among other things, the authors show that the fluctuations for the WASEP with “infinite wedge” initial condition are also given by the Cole-Hopf solution.

The problem with the Cole-Hopf solution is that it does not provide a satisfactory theory of approximations to (1.1). Indeed, all approximations to (1.1) must first be reinterpreted as approximations to (1.3), which is not always convenient. While it works well for the approximation by mollification of the noise that we just mentioned, it does not work at all for other natural approximations to (1.1), like for example adding a small amount of hyperviscosity or performing a spatio-temporal mollification of the noise. This is also why only the fluctuations of the WASEP have so far been shown to converge to the solutions to the KPZ equation: this is one of the rare discrete systems that behave well under the corresponding version of the Cole-Hopf transform.

As a consequence, there have been a number of, unfortunately unsuccessful, attempts over the past decade to provide a more natural notion of solution without making use of the Cole-Hopf transform. For example, as illustrated by (1.5), the Cole-Hopf solution really corresponds to an interpretation of the nonlinearity as a Wick product$\partial _ { x } h \diamond \partial _ { x } h$, where the Wick product is defined relative to the Gaussian structure given on the space of solutions by the linearised equation (i.e. the one where we simply drop the nonlinearity altogether). One could also imagine interpreting the nonlinearity as a Wick product with respect to the Gaussian structure given on the underlying probability space by the driving noise$\xi .$This yields a different concept of solution that was studied in [HØUZ96, Cha00]. In the spatially extended situation, this solution appears however to behave in a non-physical way in the sense that it does not exhibit the correct scaling exponents.

Following a similar line of though, one may try to apply “standard” renormalisation theory to interpret (1.1). This programme was initiated in [DPDT07], where the authors were able to treat a mollified version of (1.1), namely

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + (- \partial_ {x} ^ {2}) ^ {- 2 \alpha} ((\partial_ {x} h) ^ {2} - \infty) + (- \partial_ {x} ^ {2}) ^ {- \alpha} \xi .\tag{1.6}
$$

Unfortunately, the techniques used there seem to break down at$\textstyle \alpha = { \frac { 1 } { 8 } }$. We refer to Remark 5.4 below for an explanation why$\frac { 1 } { 8 }$is one natural barrier arising for “conventional” techniques and what other barriers (the largest of which being the passage from$\alpha > 0 \mathrm { t o } \alpha = 0 )$must be crossed before reaching (1.1).

Another way to make sense of (1.1) could be to formulate a corresponding martingale problem. This is a technique that was explored in [Ass02] for example. Very recently, a somewhat related notion of “weak energy solution” was introduced in [GJ10] and further refined in [Ass11], but there is so far no corresponding uniqueness result. Furthermore, this notion does not seem to provide any way of distinguishing solutions that differ by spatial constants.

Some recent progress has also been made in providing an approximation theory to variants of (1.3), but the results are only partial [PP12, Bal11]. To a large extent, this long-standing problem is solved (or at least a programme is established on how to solve some of its variants) by the results of this article. In particular, we provide a “pathwise” interpretation of (1.1), together with a robust approximation theory.

Before we state the theorem, we introduce some notation. We denote by$\bar { \mathcal { C } } ^ { \alpha }$the space$\mathcal { C ^ { \alpha } }$to which we add a “point at infinity” ∞ with neighbourhoods of the form $\{ h : \| h \| _ { \alpha } > R \} \cup \{ \infty \}$, which turns$\bar { \mathcal { C } } ^ { \alpha }$into a Polish space. We need to work with the space$\bar { \mathcal { C } } ^ { \alpha }$since our construction only provides local solution so that, for a given$\Psi \in { \mathcal { X } }$and a given initial condition$h _ { 0 }$, we cannot guarantee that solutions will not explode in finite time. However, if solutions do explode in finite time, it is always because the$\mathcal { C ^ { \alpha } }$-norm diverges. With this terminology in place, our result can be stated as follows:

Theorem 1.1 There exists a Polish space$x ,$, a measurable map$\Psi \colon \Omega  \mathcal { X }$and, for every$\beta \in ( 0 , \frac { 1 } { 2 } )$, a lower semicontinuous map$T _ { \star } \colon { \mathcal { C } } ^ { \beta } \times { \mathcal { X } } \to ( 0 , + \infty ]$and a map$S _ { \mathrm { R } } \colon { \mathcal { C } } ^ { \beta } \times { \mathcal { X } } \to { \mathcal { C } } ( \mathbf { R } _ { + } , { \bar { \mathcal { C } } } ^ { \frac { 1 } { 2 } - \beta } )$such that

$$
(t, h _ {0}, \Psi) \mapsto \mathcal {S} _ {\mathrm{R}} (h _ {0}, \Psi) (t),
$$

is continuous on all triples such that$t \in ( 0 , T _ { \star } ( h _ { 0 } , \Psi ) )$. Furthermore, for every $h _ { 0 } \in \mathcal { C } ^ { \beta }$, one has$T _ { \star } ( h _ { 0 } , \Psi ( \omega ) ) = +$∞ almost surely and the identity

$$
\mathcal {S} _ {\mathrm{CH}} (h _ {0}, \omega) = \mathcal {S} _ {\mathrm{R}} \big (h _ {0}, \Psi (\omega) \big),
$$

holdsfor almost every$\omega \in \Omega$

Finally, there exists a separable Frechet space´ W such that$\mathcal { X } \subset \mathcal { W }$(with the topology ofX given by the induced topology ofW) and such that,for every$\ell \in \mathcal { W } ^ { \star }$ the random variable$\ell ( \Psi ( \cdot ) )$belongs to the union ofthefirstfour Wiener chaoses of $\xi$(see Section A.1for a short reminder ofthe definition ofthe Wiener chaos).

Remark 1.2 The letter$\mathbf { \hat { R } } ^ { \prime }$in$S _ { \mathrm { R } }$stands for “Rough”. It will become clear later why we chose this terminology.

Remark 1.3 Loosely speaking, our result states that one can find a Polish space X and a jointly continuous map$S _ { \mathrm { R } }$such that the following diagram commutes, where arrows without label denote the identity:

$$
\begin{array}{c} \mathcal {X} \times \mathcal {C} ^ {\alpha} \xrightarrow {\mathcal {S} _ {\mathrm{R}}} \mathcal {C} (\mathbf {R} _ {+}, \mathcal {C} ^ {\alpha}) \\ \Psi \Bigg \uparrow \qquad \Bigg \uparrow \qquad \qquad \cdot \qquad \Bigg \downarrow \\ \Omega \times \mathcal {C} ^ {\alpha} \xrightarrow {\mathcal {S} _ {\mathrm{CH}}} \mathcal {C} (\mathbf {R} _ {+}, \mathcal {C} ^ {\alpha}) \end{array}\tag{1.7}
$$

As it turns out,$S _ { \mathrm { R } }$also extends the usual (deterministic) notion${ S _ { \mathrm { D } } }$of solution to the KPZ equation with regular data:

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + \lambda (\partial_ {x} h) ^ {2} + g (x, t).\tag{1.8}
$$

In other words, it is possible to find a map Φ such that the following commutes:

$$
\begin{array}{c c c c} \mathcal {X} & \times \mathcal {C} ^ {\alpha} & \xrightarrow {\mathcal {S} _ {\mathrm{R}}} \mathcal {C} (\mathbf {R} _ {+}, \mathcal {C} ^ {\alpha}) \\ \Phi \Big \uparrow & \Big \uparrow & . & \Big \downarrow \\ \mathcal {C} (\mathbf {R} _ {+}, \mathcal {C}) & \times \mathcal {C} ^ {\alpha} & \xrightarrow {\mathcal {S} _ {\mathrm{D}}} \mathcal {C} (\mathbf {R} _ {+}, \mathcal {C} ^ {\alpha}) \end{array}\tag{1.9}
$$

where the first argument to${ \mathcal { S } } _ { \mathrm { D } }$is the function$g$in (1.8). Interestingly, the choice of Φ in (1.9) is not unique. As we will see later, the map Ψ in (1.7) is given by the limit in probability of maps$\Phi _ { \varepsilon }$that are admissible for (1.9), applied to$\xi _ { \varepsilon } - C _ { \varepsilon }$for a suitable mollification$\xi _ { \varepsilon }$of$\xi$and constant$C _ { \varepsilon } \to \infty$

Remark 1.4 The space X will be given explicitly later on, but it is not a linear space. It is indeed not difficult to convince oneself that, even though the probability space associated to$\xi$carries a natural linear structure (one could take it to be given by the space of distributions over$S ^ { 1 } \times \mathbf { R }$for example), it is not possible to find a norm on it that would make the map$\mathcal { S } _ { \mathrm { C H } }$continuous.

Similarly, the reason why we did not simply formulate the statement of the theorem with$\mathcal { X }$replaced by W from the beginning is that, even though$S _ { \mathrm { R } }$is continuous on X, it does not extend continuously to all of$\mathcal { W }$

We also have a more explicit description of$S _ { \mathrm { R } }$as the solution to a fixed point argument, which in particular implies that the Cole-Hopf solutions of the KPZ equation can be realised as a continuous random dynamical system. This can for example be formulated as follows:

Proposition 1.5 Fix$\beta \in ( 0 , \frac { 1 } { 2 } )$. For every$T > 0$there exists a Banach space$B _ { \star , T }$ with a canonical projection π:$\mathcal { B } _ { \star , T } \to \mathcal { C } ( [ 0 , T ] , \mathcal { C } ^ { \frac 3 2 - \beta } )$, a closed algebraic variety $\mathcal { V } _ { \star , T } \subset \mathcal { X } \times \mathcal { B } _ { \star , T }$, continuous maps$h ^ { \star } \colon \mathcal { X } \to \mathcal { C } ( [ 0 , T ] , \mathcal { C } ^ { \frac { 1 } { 2 } - \beta } )$and

$$
\hat {\mathcal {M}} \colon \mathcal {C} ^ {\beta} \times \mathcal {Y} _ {\star , T} \to \mathcal {B} _ {\star , T},
$$

as well as a lower semi-continuous map$T _ { \star } \colon { \mathcal { C } } ^ { \beta } \times { \mathcal { X } } \to ( 0 , + \infty ]$with the following properties:

• The map$\hat { \mathcal { M } }$leaves$\mathcal { V } _ { \star , T }$invariant in the sense that$( \Psi , \hat { \mathcal { M } } ( h , \Psi , v ) ) \in \mathcal { V } _ { \star , T }$ for every pair$( \Psi , v ) \in \mathcal { V } _ { \star , T }$and every$h \in \mathcal { C } ^ { \beta }$

• For every$\Psi \in { \mathcal { X } } ,$, the space$\mathcal { B } _ { \Psi , T } = \{ v \in \mathcal { B } _ { \star , T } \ : \ ( \Psi , v ) \in \mathcal { V } _ { \star , T } \}$is a Banach subspace of$B _ { \star , T }$.

• For every$h _ { 0 } \in \mathcal { C } ^ { \beta } , \Psi _ { 0 } \in \mathcal { X } ,$, and$T < T _ { \star } ( h _ { 0 } , \Psi )$and neighbourhoods U of $h _ { 0 }$and$V o f \Psi _ { 0 }$such that,for every$\Psi \in V$and every$h \in U$, the restriction $o f S _ { \mathrm { R } } ( h , \Psi ) t o [ 0 , T ]$can be decomposed as

$$
\left. \mathcal {S} _ {\mathrm{R}} (h, \Psi) \right| _ {[ 0, T ]} = h ^ {\star} (\Psi) \big | _ {[ 0, T ]} + \pi \hat {\mathcal {S}} _ {\mathrm{R}} (h, \Psi),\tag{1.10}
$$

where${ \hat { S } } _ { \mathrm { R } } \colon U \times V \to { \mathcal { C } } ( [ 0 , T ] , { \mathcal { C } } ^ { { \frac { 1 } { 2 } } - \beta } )$is$a$continuous map that is the unique solution in$B _ { \Psi , T }$to thefixed point problem

$$
\hat {\mathcal {M}} (h, \Psi , \hat {\mathcal {S}} _ {\mathrm{R}} (h, \Psi)) = \hat {\mathcal {S}} _ {\mathrm{R}} (h, \Psi)  .
$$

$I f T _ { \star } ( h , \Psi ) < \infty ,$, then lim$\mathsf { i } _ { t \to T _ { \star } } \| S _ { \mathrm { R } } ( h , \Psi ) ( t ) \| _ { \beta } = \infty f o r e \nu e r y \beta > 0 .$

• There exists a group ofcontinuous transformations$\Theta _ { t } \colon { \mathcal { X } } \to { \mathcal { X } }$such that$h ^ { \star }$ and$\hat { S } _ { \mathrm { R } }$satisfy the cocycle property in the sense that the identities

$$
h ^ {\star} (\Psi) (t + s) = h ^ {\star} (\Theta_ {t} \Psi) (s), \quad \hat {\mathcal {S}} _ {\mathrm{R}} (h, \Psi) (t + s) = \hat {\mathcal {S}} _ {\mathrm{R}} \bigl (\hat {\mathcal {S}} _ {\mathrm{R}} (h, \Psi) (t), \Theta_ {t} \Psi \bigr) (s),
$$

hold for every$\Psi \in { \mathcal { X } } ,$, every$h _ { 0 } \in \mathcal { C } ^ { \beta }$and every$s , t > 0$with$s + t < T _ { \star }$

Remark 1.6 The reason for requiring the decomposition (1.10) instead of writing $S _ { \mathrm { R } }$itself as a solution to a fixed point problem is that$h ^ { \star }$does not belong to$B _ { \star , T }$in general. Note also that, quite unusually in the theory of partial differential equations, the space$B _ { \Psi , T }$in which we effectively solve our fixed point problem depends on the choice of Ψ!

Remark 1.7 In principle, Proposition 1.5 only provides a description of solutions up to the explosion time$T _ { \star }$. It is then natural to simply set$S _ { \mathrm { R } } ( h , \Psi ) ( t ) = \infty$for $t > T _ { \star } ( h , \Psi )$, which yields a continuous path by the definition of the topology on $\bar { \mathcal { C } } ^ { \frac { 1 } { 2 } - \beta }$and the fact that solutions explode when approaching$T _ { \star }$. In order to prove Theorem 1.1, it is therefore sufficient to construct$\hat { \mathcal { S } } _ { \mathrm { R } }$and$h ^ { \star }$with the properties stated in Proposition 1.5 and such that$S _ { \mathrm { C H } } = \pi \hat { S } _ { \mathrm { R } } + h ^ { \star }$for every initial condition and almost every realisation of Ψ. The fact that we know a priori that Cole-Hopf solutions are defined for all times ensures that, for every$h \in \mathcal { C } ^ { \beta }$, one has $T _ { \star } ( h , \Psi ( \omega ) ) = + \infty$almost surely, but we cannot rule out the existence of a non-trivial exceptional set that may depend on the initial condition.

Remark 1.8 As an abstract result, it is not clear how useful Proposition 1.5 really is. However, we will provide very explicit constructions of all the quantities appearing in its statement. As a consequence, in order to approximate the Cole-Hopf solutions to (1.1), it is enough to provide a good enough approximation to the fixed point map M in a suitable space, as well as an approximation to the map Ψ. For an example of how such programme can be implemented in the context of a different equation with similar regularity properties, see [HMW12].

Another drawback of the Cole-Hopf solution is that some properties of the solutions that seem natural in view of (1.1) turn out to be very difficult to prove at the level of (1.3). For example, due to the additive nature of the driving noise in (1.1), one would expect the difference between two solutions to exhibit better spatial and temporal regularity properties than the solutions themselves. However, such a statement turns into a statement about the regularity of the ratio between solutions to (1.3), which seems very difficult to obtain, although some very recent progress was obtained in this direction in [OW11].

As a corollary of the construction of$S _ { \mathrm { R } }$however, we obtain extremely detailed information about the solutions. In order to formulate our next result, we introduce the stationary mean zero solution to the stochastic heat equation

$$
\partial_ {t} X ^ {\bullet} = \partial_ {x} ^ {2} X ^ {\bullet} + \Pi_ {0} ^ {\perp} \xi ,
$$

where$\Pi _ { 0 } ^ { \perp } = 1 - \Pi _ { 0 }$, with$\Pi _ { 0 }$the orthogonal projection onto constant functions in$L ^ { 2 }$. (Adding this projection is necessary in order to have a stationary solution.) Another vital role will be played by the process$\Phi$given as the centred stationary solution to

$$
\partial_ {t} \Phi = \partial_ {x} ^ {2} \Phi + \partial_ {x} ^ {2} X ^ {\bullet}.
$$

Note that, for any fixed time t, both Φ and$X ^ { \bullet }$are equal in law to a Brownian bridge (in space!) which is centred so that its spatial average vanishes, but there are correlations between the two processes.

Remark 1.9 Both$X ^ { \bullet }$and Φ are a priori given as stochastic processes defined on the underlying probability space Ω. However, we will see below that$\mathcal { X }$is constructed in such a way that there are natural counterparts to$X ^ { \bullet }$and$\Phi$that are continuous functions from$\mathcal { X }$into$\mathcal { C } ( \mathbf { R } , \mathcal { C } ^ { \frac { 1 } { 2 } - \delta } )$for every$\delta > 0$

With this notation at hand, we have the following decomposition of the solutions:

Theorem 1.10 Let$\beta > 0$be arbitrarily small and, for$h _ { 0 } \in \mathcal { C } ^ { \beta }$and$\Psi \in { \mathcal { X } }$, set $h _ { t } = S _ { \mathrm { R } } ( h _ { 0 } , \Psi ) ( t )$and$T _ { \star } = \operatorname* { i n f } \{ t > 0 : h _ { t } = \infty \}$

Then,for every$t < T _ { \star }$, one has$h _ { t } - X _ { t } ^ { \bullet } \in \mathcal { C } ^ { 1 - \beta }$. Furthermore, there exists a continuous map$Q \colon { \mathcal { X } } \to { \mathcal { C } } ( \mathbf { R } _ { + } , { \mathcal { C } } ^ { - \beta } )$such that one has

$$
e ^ {- 2 \lambda \Phi_ {t}} \partial_ {x} (h _ {t} - X _ {t} ^ {\bullet}) - Q _ {t} \in \mathcal {C} ^ {1 - \beta},\tag{1.11}
$$

for every$t < T _ { \star }$

Proof. In view of the construction of Section 2, this is an immediate consequence of Proposition 4.10, provided that we set

$$
Q _ {t} = \lambda e ^ {- 2 \lambda \Phi_ {t}} \partial_ {x} (X _ {t} ^ {\mathsf {V}} + \lambda X _ {t} ^ {\mathsf {V}} + 4 \lambda^ {2} X _ {t} ^ {\mathsf {V}}) + 8 \lambda^ {4} \int_ {0} ^ {\cdot} e ^ {- 2 \lambda \Phi_ {t} (z)} \partial_ {x} X ^ {\mathsf {V}} (z) d \Phi_ {t} (z) .
$$

See Section 2 for a definition of the expressions appearing here, as well as Section 3 for a definition of the “rough integral” R. Actually, Proposition 4.10 provides an expression with two additional terms involving a process$\bar { X } ^ { \mathbb { Y } }$, but since$\bar { X } _ { t } ^ { \ C Y } \in \mathcal { C } ^ { 2 - \beta }$ and$\Phi _ { t } \in \mathcal { C } ^ { \frac { 3 } { 2 } - \beta }$for every fixed$t ,$one can check that the sum of these two terms belongs to$\mathcal { C } ^ { 1 - \beta }$□

Remark 1.11 The product appearing on the left hand side of (1.11) makes sense by Proposition$\mathsf { A } . 9$since$\Phi _ { t } \in \mathcal { C } ^ { \frac { 1 } { 2 } - \beta }$and$\partial _ { x } ( h _ { t } - X _ { t } ^ { \bullet } ) \in \mathcal { C } ^ { - \beta }$for every$\beta > 0$

Remark 1.12 Together with the explicit construction of$Y$given in Proposition 4.10 below, Theorem 1.10 provides a full description of the microscopic structure of the solutions to the KPZ equation, all the way down to the “level$\bar { \mathcal { C } } ^ { 2 - \beta \mathfrak { n } }$for every $\beta > 0$

As a simple consequence of this decomposition, we also have a sharp regularity result for the difference between two solutions with different initial conditions:

Corollary 1.13 Let$h _ { t }$and$\bar { h } _ { t }$be two solutions to$( l . l )$with different Holder con-¨ tinuous initial conditions, but driven by the same realisation ofthe noise. For every $\beta > 0 ,$, one then has$h _ { t } - \bar { h } _ { t } \in \mathcal { C } ^ { \frac { 3 } { 2 } - \beta }$and

$$
e ^ {- 2 \lambda \Phi_ {t}} \partial_ {x} (h _ {t} - \bar {h} _ {t}) \in \mathcal {C} ^ {1 - \beta},\tag{1.12}
$$

for every t less than the smaller ofthe two explosion times.

Proof. The bound (1.12) follows immediately from (1.11). The fact that$h _ { t } - \bar { h } _ { t } \in$ $\mathcal { C } ^ { \frac { 3 } { 2 } - \beta }$is then immediate since$\Psi _ { t } \in \mathcal { C } ^ { \frac { 1 } { 2 } - \beta }$□

In a recent article [OW11], O’Connell and Warren provided a “multilayer extension” of the solution to the stochastic heat equation (1.3). As a byproduct of their theory, it follows that$h _ { t } - \bar { h } _ { t } \in \mathcal { C } ^ { 1 }$so that Theorem 1.10 can be seen as a refinement of their results, even though the decomposition considered there is quite different. One object that arises in [OW11] is the solution to the linearised KPZ equation, namely

$$
\partial_ {t} u = \partial_ {x} ^ {2} u + \partial_ {x} u \partial_ {x} h,\tag{1.13}
$$

where$h$is itself a solution to (1.1) (see equation (20) in [OW11]). One byproduct of our construction is that we are able to provide a rigorous meaning to equations of the type (1.13) or, more generally, equations of the type

$$
\partial_ {t} u = \partial_ {x} ^ {2} u + G (t, u, \partial_ {x} u) \partial_ {x} X _ {t} ^ {\bullet} + F (t, u, \partial_ {x} u),
$$

where$F$and$G$are suitable nonlinearities; see Theorem 4.8 below. In particular, this theorem also allows to provide a rigorous meaning for the Fokker-Planck equation associated to a one-dimensional diffusion in the time-dependent potential$X _ { t } ^ { \bullet }$, which does not seem to be covered by existing techniques. Indeed, the well-posedness of such a Fokker-Planck equation is quite well-known in the time independent case, also with even weaker regularity assumptions, but the time-dependent case seems to be new and highly non-trivial. See for example [FRW04, RT07] for some results in the time-independent case, as well as [LBL08] for some previously known results that are very general (the authors allow non-constant diffusion coefficients and higher space dimensions for example), but do not appear to cover the situation at hand.

To conclude this introductory section, let us mention a few more byproducts of our construction that are of independent mathematical interest:

• We provide an example of a two-dimensional “geometric rough path” which is obtained in a natural way by approximations by smooth paths but where, in order to obtain a well-defined limit, a logarithmically divergent “area term” needs to be subtracted, see Section 7 below.

• Since the map$S _ { \mathrm { R } }$is continuous, it does not depend on any choice of measure on$\mathcal { X } .$. This allows us to use it for other type of convergence results, even in the case of deterministic drivers. As an example, we show in Section 2.4 how to obtain a new periodic homogenisation result for the heat equation with a very strong space-time periodic potential.

• It transpires that, besides the renormalisation$\begin{array} { r } { C _ { \varepsilon } \approx \frac { 1 } { \varepsilon } } \end{array}$observed in (1.5), two further renormalisations, this time with logarithmically divergent constants, are lurking underneath. The reason why this doesn’t seem to have been observed before (and the reason why only$C _ { \varepsilon }$appears when performing the Cole-Hopf transform of the multiplicative stochastic heat equation) is that these two logarithmically diverging constants cancel each other exactly, see Theorem 2.3 below. This appears to be due to a certain symmetry of the equation (1.1) which may not hold in general for other equations in the same class.

The remainder of this article is organised in the following way. In Section 2, we provide a more detailed mathematical formulation of the main results of this article and we explain the main ideas arising in the proof. In particular, we provide an explicit description of all the objects appearing in Proposition 1.5. In Section 3, we then introduce some the elements of the theory of (controlled) rough paths that are essential to our proof. This section also contains some of the regularising bounds on the heat kernel that we need in the sequel. This is followed in Section 4 by a solution theory for a class of rough stochastic PDEs that includes the type of equation arising when taking the difference between two solutions to (1.1).

In Section 5, we then build a “universal process” which provides a very good approximation to the stationary solution to (1.1), lying in the fourth Wiener chaos with respect to the driving noise$\xi .$This process is centred by construction (so it really approximates the corresponding Burgers equation), so in Section 6 we also construct its constant Fourier mode, in order to obtain an approximation to KPZ. Finally, in Section 7 we provide a more detailed control of the local fluctuations of one of the building blocks of the process built in Section 5.

## 1.1 Notation

We will often work with Fourier components. We adopt the usual convention $\begin{array} { r } { X ( x ) = \sum _ { k \in \mathbf { Z } } X _ { k } e ^ { i k x } } \end{array}$, so that one has the identity$\begin{array} { r } { ( X Y ) _ { k } = \sum _ { \ell \in \mathbf { Z } } X _ { \ell } Y _ { k - \ell } } \end{array}$. One feature of this normalisation is that the average of a function X is equal to$X _ { 0 }$and the average of$| X | ^ { 2 }$is given by$\textstyle \sum _ { k \in { \mathbf { Z } } } | X _ { k } | ^ { 2 }$

Throughout this article, we will consistently make use of Holder seminorms, so¨ that, for$X \colon S ^ { 1 } \to$R and$\alpha \in ( 0 , 1 ]$, we set

$$
\| X \| _ {\alpha} \stackrel {{\text { def }}} {{=}} \sup _ {x \neq y} \frac {| \delta X (x , y) |}{| x - y | ^ {\alpha}},
$$

where$\delta X ( x , y ) = X ( y ) - X ( x )$. We will also extend this to negative values of$\alpha .$

For$\alpha \in ( - 1 , 0 )$, we set

$$
\| X \| _ {\alpha} \stackrel {\mathrm{def}} {=} \sup _ {x \neq y} \frac {| \int_ {x} ^ {y} X (z) d z |}{| x - y | ^ {1 + \alpha}},
$$

and we denote by$\mathcal { C ^ { \alpha } }$the space of distributions obtained by closing${ \mathcal { C } } ^ { \infty }$under the above norm. We make a slight abuse of notation for the supremum norm by also writing

$$
\| X \| _ {\infty} \stackrel {{\text { def }}} {{=}} \sup _ {x} | X (x) |.
$$

We are sometimes lead to consider Holder norms instead of seminorms, so we set¨

$$
\| X \| _ {\mathcal {C} ^ {\alpha}} \stackrel {\mathrm{def}} {=} \| X \| _ {\alpha} + \| X \| _ {\infty}.
$$

A crucial ingredient in the theory of (controlled) rough paths used in this article is played by “area processes” and “remainder terms”, both of which are functions of two spatial variables. For such functions, we also set

$$
\| \mathbf {X} \| _ {\alpha} \stackrel {{\text { def }}} {{=}} \sup _ {x \neq y} \frac {| \mathbf {X} (x , y) |}{| x - y | ^ {\alpha}},\tag{1.14}
$$

which is a kind of Holder seminorm¨$^ { 6 6 } _ { 0 1 }$the diagonal” and we denote by$\mathcal { C } _ { 2 } ^ { \alpha }$ the closure of the space of smooth functions of two variables under the norm $\| \mathbf { X } \| _ { \mathcal { C } _ { 2 } ^ { \alpha } } = \| \mathbf { X } \| _ { \alpha } + \| \mathbf { X } \| _ { \infty }$. The advantage of only ever considering the closures of ${ \mathcal { C } } ^ { \infty }$under the above norms has the advantage that all the spaces appearing in this article are separable, so that no problem of measurability arises.

## Acknowledgements

I would like to thank Sigurd Assing, Jan Maas, Neil O’Connell, Jon Warren, and Jeremy Quastel for numerous discussions on this and related problems that helped deepen and clarifying the arguments presented here. Special thanks are due to Hendrik Weber for numerous suggestions and his careful reading of the draft manuscript, as well as to Gerard Ben Arous who suggested that the techniques´ developed in [Hai12, Hai11] might prove useful for analysing the KPZ equation.

Financial support was kindly provided by EPSRC grant EP/D071593/1, by the Royal Society through a Wolfson Research Merit Award, and by the Leverhulme Trust through a Philip Leverhulme Prize.

## 2 Main results and ideas of proof

The idea pursued in this article is to solve (1.1) by performing a Wild expansion [Wil51] of the solution in powers of λ but, instead of deriving an infinite series that may be extremely difficult to sum, we truncate it at a fixed level (after exactly 4 terms to be precise) and then use completely different techniques to treat the remainder. In order to appreciate how the techniques explained in this section can also apply to a concrete deterministic example, it may be helpful to simultaneously follow the calculations in Section 2.4 below.

Recall that$X _ { \varepsilon } ^ { \bullet }$is the stationary mean zero solution to the linearised equation

$$
\partial_ {t} X _ {\varepsilon} ^ {\bullet} = \partial_ {x} ^ {2} X _ {\varepsilon} ^ {\bullet} + \Pi_ {0} ^ {\perp} \xi_ {\varepsilon}.
$$

Here, the noise process$\xi _ { \varepsilon }$is a mollified version of$\xi ,$, obtained by choosing a function $\varphi : \mathbf { R }  \mathbf { R } _ { + }$that is even, smooth, compactly supported, decreasing on$\mathbf { R } _ { + }$, and such that$\varphi ( 0 ) = 1$, and then setting

$$
\xi_ {\varepsilon , k} = \varphi (\varepsilon k) \xi_ {k}.
$$

The$\xi _ { k }$are the Fourier components of$\xi ,$, which are complex-valued white noises with$\xi _ { - k } = \bar { \xi } _ { k }$and${ \bf E } \xi _ { k } ( s ) \xi _ { \ell } ( t ) = 2 \delta _ { k , - \ell } \delta ( t - s )$. The above properties of the mollifier$\varphi$will be assumed throughout the whole article without further mention.

A crucial ingredient of the construction performed in this article is a family$X _ { \varepsilon } ^ { \tau }$ of processes indexed by binary trees τ, where$" \bullet \bullet \bullet$denotes the “trivial” tree consisting of only its root. The process$X _ { \xi } ^ { \bullet }$associated to the trivial tree has already been defined, and we define the remaining processes recursively as follows. Denoting by$\mathcal { T } _ { 2 }$the set of all binary trees, any binary tree$\tau \in \mathcal { T } _ { 2 }$with$\tau \neq \cdot$• can be written as$\tau = [ \tau _ { 1 } , \tau _ { 2 } ] .$ i.e. τ consists of its root, with trees$\tau _ { 1 } , \tau _ { 2 } \in \mathcal { T } _ { 2 }$attached. For any such tree τ, we then define$X _ { \varepsilon } ^ { \tau }$as the stationary solution to

$$
\partial_ {t} X _ {\varepsilon} ^ {\tau} = \partial_ {x} ^ {2} X _ {\varepsilon} ^ {\tau} + \Pi_ {0} ^ {\perp} \bigl (\partial_ {x} X _ {\varepsilon} ^ {\tau_ {1}} \partial_ {x} X _ {\varepsilon} ^ {\tau_ {2}} \bigr).\tag{2.1}
$$

Remark 2.1 As before, the reason why we introduce the projection$\Pi _ { 0 } ^ { \perp }$is so that we can consider stationary solutions. Another possibility would have been to slightly modify the equation to replace$\partial _ { x } ^ { 2 }$by$\partial _ { x } ^ { 2 } - 1$for example, but it turns out that the current choice leads to simpler expressions. Since we only have derivatives of$X _ { \varepsilon } ^ { \tau }$ appearing in (2.1) anyway, the effect of$\Pi _ { 0 } ^ { \perp }$turns out to be rather harmless, see Remark 2.2.

We now add the constant terms back in. Set$Y _ { \varepsilon } ^ { \bullet } ( t ) = X _ { \varepsilon } ^ { \bullet } ( t ) + { \sqrt { 2 } } B ( t )$, where B is a standard Brownian motion. One of the main results of this article is that one can then find constants$C _ { \varepsilon } ^ { \tau }$for$\tau \neq \bullet$such that the solutions$Y _ { \varepsilon } ^ { \tau }$to

$$
\partial_ {t} Y _ {\varepsilon} ^ {\tau} = \partial_ {x} ^ {2} Y _ {\varepsilon} ^ {\tau} + \partial_ {x} Y _ {\varepsilon} ^ {\tau_ {1}} \partial_ {x} Y _ {\varepsilon} ^ {\tau_ {2}} - C _ {\varepsilon} ^ {\tau},\tag{2.2}
$$

with initial condition$Y _ { \varepsilon } ^ { \tau } ( 0 ) = X _ { \varepsilon } ^ { \tau } ( 0 )$, have a limit as$\varepsilon \to 0$that is independent of the choice of mollifier$\varphi .$

Remark 2.2 Since only derivatives of$Y _ { \varepsilon } ^ { \tau }$appear on the right hand side of (2.2), it follows that$X _ { \varepsilon } ^ { \tau } = \Pi _ { 0 } ^ { \perp } Y _ { \varepsilon } ^ { \tau }$. The reason for introducing the processes$X _ { \varepsilon } ^ { \tau }$is that it is easier, as a first step, to show that they converge to a limit. The constant Fourier mode will then be treated separately.

The reason for the definition of the processes$Y _ { \varepsilon } ^ { \tau }$is that, at least at a formal level, if one defines a process$h _ { \varepsilon } ( t )$by

$$
h _ {\varepsilon} (t) = \sum_ {\tau} \lambda^ {| \tau |} Y _ {\varepsilon} ^ {\tau} (t),\tag{2.3}
$$

where$| \tau |$denotes the number of inner nodes of τ (i.e. the number of nodes that are not leaves, with$| \bullet | = 0$by convention), then$h _ { \varepsilon }$solves the equation

$$
\partial_ {t} h _ {\varepsilon} = \partial_ {x} ^ {2} h _ {\varepsilon} + \lambda (\partial_ {x} h _ {\varepsilon}) ^ {2} + \xi_ {\varepsilon} - \sum_ {\tau} \lambda^ {| \tau |} C _ {\varepsilon} ^ {\tau},
$$

which is precisely (1.5). The problem with such an approach is twofold: first, we have no guarantee that the sum (2.3) actually converges. Then, even if it did converge for fixed$\varepsilon > 0$, we would have no guarantee that the sequence of processes$h _ { \varepsilon }$constructed in this way converges to a limit, even if we knew that each of the$Y _ { \varepsilon } ^ { \tau }$converges. See however [Wil51, McK67, CCG00] for an analysis of the corresponding expansion in the context of the Boltzmann equation, where the sum over all binary trees can actually be shown to converge.

The strategy pursued in this work is to truncate the expansion (2.3) at a fixed level and to then derive an equation for the remainder that can be solved by using techniques inspired from [Hai11].

## 2.1 Convergence of the processes$Y ^ { \tau }$

In this section, we state the precise convergence result that we obtain for the processes$Y _ { \varepsilon } ^ { \tau }$. The choice for$C _ { \varepsilon } ^ { \tau }$that we retain is$C _ { \varepsilon } ^ { \tau } = 0$for$\tau \not \in \{ \mathrm { v } , \mathfrak { V } , \mathfrak { k } , \mathfrak { V } , \mathfrak { V } , \mathfrak { V } \}$, and

$$
\begin{array}{r l} & C _ {\varepsilon} ^ {\mathbb {V}} = \frac {1}{\varepsilon} \int_ {\mathbf {R}} \varphi^ {2} (x) d x, \\ & C _ {\varepsilon} ^ {\mathbb {W}} = \frac {4 \pi}{\sqrt {3}} | \log \varepsilon | - 8 \int_ {\mathbf {R} _ {+}} \int_ {\mathbf {R}} \frac {x \varphi^ {\prime} (y) \varphi (y) \varphi^ {2} (y - x) \log y}{x ^ {2} - x y + y ^ {2}} d x d y, \\ & C _ {\varepsilon} ^ {\mathbb {X}} = - \frac {C _ {\varepsilon} ^ {\mathbb {Y}}}{4}. \end{array}\tag{2.4}
$$

The remaining trees are of course all equivalent to the tree$\updownarrow _ { \updownarrow }$and therefore are associated with the same constant. It is remarkable that$C _ { \varepsilon } ^ { \texttt { w } }$and$C _ { \varepsilon } ^ { \aleph }$turn out to exhibit the exact same logarithmic divergence but with opposite signs, save for the factor 4 that takes into account the difference in multiplicities between the two terms. It is also remarkable that, even though the constants$C _ { \varepsilon } ^ { \aleph }$and$C _ { \varepsilon } ^ { \aleph }$do depend on the choice of mollifier$\varphi _ { \cdot }$, the resulting processes$Y ^ { \tau }$do not.

As a consequence of this choice, note also that we have the identity

$$
\sum_ {\tau} \lambda^ {| \tau |} C _ {\varepsilon} ^ {\tau} = \lambda C _ {\varepsilon} ^ {\mathbf {V}},\tag{2.5}
$$

so that, at least formally, the process$h _ { \varepsilon }$solves (1.5) for the “correct” constant$C _ { \varepsilon }$ Before we state our convergence result, we introduce some more notation. For every $\tau ,$, we define an exponent$\alpha _ { \tau }$by

$$
\alpha_ {\bullet} = \frac {1}{2}, \quad \alpha_ {\mathsf {V}} = 1,
$$

and then, recursively, by

$$
\alpha_ {[ \tau_ {1}, \tau_ {2} ]} = (\alpha_ {\tau_ {1}} \wedge \alpha_ {\tau_ {2}}) + 1.
$$

(So we have for example$\begin{array} { r } { \alpha _ { \tt V } = \frac { 3 } { 2 } } \end{array}$and$\alpha _ { \tt V Y } = 2 . )$For$\tau \neq \bullet ,$, we then define the separable Frechet space´$\mathcal { X } _ { \tau }$as the closure of smooth functions under the system of seminorms

$$
\| X \| _ {\tau , \delta , T} = \sup _ {s, t \in [ - T, T ]} \left(\| X (t) \| _ {\mathcal {C} ^ {\alpha_ {\tau} - \delta}} + \frac {\| X (t) - X (s) \| _ {\infty}}{| t - s | ^ {\frac {1}{2} - \delta}}\right),\tag{2.6}
$$

where$T \in [ 1 , \infty )$and$\delta \in ( 0 , \frac { 1 } { 4 } )$. Similarly, we define$x _ { \bullet }$as the closure of smooth functions under the system of seminorms

$$
\| X \| _ {\bullet , \delta} = \sup _ {| t - s | \in (0, 1 ]} \left(\frac {\| X (t) - X (s) \| _ {\infty}}{| t - s | ^ {\frac {1}{4} - \delta} (1 + | t |)} + \frac {\| X (t) \| _ {\mathcal {C} ^ {\frac {1}{2} - \delta}}}{1 + | t |}\right),
$$

for$\delta \in ( 0 , \frac { 1 } { 4 } )$

With these definitions, our precise convergence result for the processes$Y _ { \varepsilon } ^ { \tau }$is the following, which we will prove at the end of Section 7.

Theorem 2.3 Let$Y _ { \varepsilon } ^ { \tau }$be as in (2.2) and let$\mathcal { X } _ { \tau }$be as above. Then,for every binary tree$\tau ,$, there exists a process$Y ^ { \tau }$such that$Y _ { \varepsilon } ^ { \tau }  Y ^ { \tau }$in probability in$\mathcal { X } _ { \tau }$

Remark 2.4 We believe that in the definition (2.6), we could actually have imposed time regularity of order$\alpha _ { \tau } / 2$instead of$1 / 2$

## 2.2 Treatment of the remainder

The truncation of (2.3) that turns out to be the shortest “viable” one is as follows. Setting$\bar { \mathcal { T } } = \{ \bullet , \vee , \vee , \vee , \vee , \vee , \vee , \vee , \vee , \vee \}$, we look for solutions to (1.5) of the form

$$
h _ {\varepsilon} (t) = \sum_ {\tau \in \tilde {\mathcal {T}}} \lambda^ {| \tau |} Y _ {\varepsilon} ^ {\tau} (t) + u _ {\varepsilon} (t) \stackrel {\mathrm{def}} {=} h _ {\varepsilon} ^ {\star} (t) + u _ {\varepsilon} (t),\tag{2.7}
$$

for a remainder$u _ { \varepsilon }$. In the sequel, since the processes$Y _ { \varepsilon } ^ { \tau }$mostly appear via their spatial derivatives, we set

$$
\bar {Y} _ {\varepsilon} ^ {\tau} \stackrel {\mathrm{def}} {=} \partial_ {x} Y _ {\varepsilon} ^ {\tau},\tag{2.8}
$$

as a shorthand. With this notation, we have the following result for$h _ { \varepsilon } ^ { \star }$:

Proposition 2.5 The process$h _ { \varepsilon } ^ { \star }$defined above is the stationary solution to

$$
\partial_ {t} h _ {\varepsilon} ^ {\star} = \partial_ {x} ^ {2} h _ {\varepsilon} ^ {\star} + \lambda (\partial_ {x} h _ {\varepsilon} ^ {\star}) ^ {2} + \xi_ {\varepsilon} - \lambda C _ {\varepsilon} ^ {\mathbf {V}} - \mathcal {R} _ {\varepsilon} ^ {\star},
$$

where the remainder term${ \mathcal { R } } _ { \varepsilon } ^ { \star }$is given by

$$
\mathcal{R}_{\varepsilon}^{\star} = \sum_{\substack{\tau ,\kappa \in \bar{\mathcal{T}}\\ [\tau ,\kappa ]\not\in\bar{\mathcal{T}}}}\lambda^{|\tau | + |\kappa | + 1}\bar{Y}_{\varepsilon}^{\tau}  \bar{Y}_{\varepsilon}^{\kappa}  .
$$

Proof. It follows from the definition of$Y _ { \varepsilon } ^ { \tau }$and from the fact that$\bullet \in \bar { \mathcal { T } }$that

$$
\partial_{t}h^{\star}_{\varepsilon} = \partial_{x}^{2}h^{\star}_{\varepsilon} + \sum_{\substack{\tau \in \bar{\mathcal{T}}\setminus \{\bullet \} \\ \tau = [\tau_{1},\tau_{2}]}}\lambda^{| \tau |}\bar{Y}^{\tau_{1}}_{\varepsilon}\bar{Y}^{\tau_{2}}_{\varepsilon} + \xi_{\varepsilon} - \sum_{\tau \in \bar{\mathcal{T}}}C^{\tau}_{\varepsilon}  .
$$

The claim now follows at once from the identity

$$
\lambda (\partial_ {x} h _ {\varepsilon} ^ {\star}) ^ {2} = \sum_ {\tau , \kappa \in \bar {\mathcal {T}}} \lambda^ {| \tau | + | \kappa | + 1} \bar {Y} _ {\varepsilon} ^ {\tau} \bar {Y} _ {\varepsilon} ^ {\kappa},
$$

noting that$| [ \tau , \kappa ] | = | \tau | + | \kappa | + 1$and that$\bar { \mathcal { T } } \setminus \{ \bullet \} \subset \{ [ \tau , \kappa ] \ : \ \tau , \kappa \in \bar { \mathcal { T } } \}$by inspection.□

As a consequence of Proposition 2.5, if we want$h _ { \varepsilon }$to satisfy (1.5), we should take$u _ { \varepsilon }$to be the solution to

$$
\partial_ {t} u _ {\varepsilon} = \partial_ {x} ^ {2} u _ {\varepsilon} + \lambda (\partial_ {x} u _ {\varepsilon}) ^ {2} + 2 \lambda \partial_ {x} u _ {\varepsilon} \partial_ {x} h _ {\varepsilon} ^ {\star} + \mathcal {R} _ {\varepsilon} ^ {\star}.\tag{2.9}
$$

Actually, it turns out to be advantageous to regroup the terms on the right hand side of this equation in a slightly different way, by isolating those terms that contain an occurrence of$Y _ { \varepsilon } ^ { \bullet }$. We thus write$h _ { \varepsilon } ^ { \star } = Y _ { \varepsilon } ^ { \bullet } + \bar { h } _ { \varepsilon } ^ { \star }$, as well as

$$
\mathcal {R} _ {\varepsilon} ^ {\star} = 2 \lambda^ {4} \bar {Y} _ {\varepsilon} ^ {\bullet} (\bar {Y} _ {\varepsilon} ^ {\vee \vee} + 4 \bar {Y} _ {\varepsilon} ^ {\vee}) + \bar {\mathcal {R}} _ {\varepsilon} ^ {\star},
$$

with

$$
\begin{array}{r l} \bar {\mathcal {R}} _ {\varepsilon} ^ {\star} = & \lambda^ {5} (2 \bar {Y} _ {\varepsilon} ^ {\vee} \bar {Y} _ {\varepsilon} ^ {\vee \vee} + 8 \bar {Y} _ {\varepsilon} ^ {\vee} \bar {Y} _ {\varepsilon} ^ {\vee \vee} + \bar {Y} _ {\varepsilon} ^ {\vee} \bar {Y} _ {\varepsilon} ^ {\vee}) + \lambda^ {6} (2 \bar {Y} _ {\varepsilon} ^ {\vee} \bar {Y} _ {\varepsilon} ^ {\vee \vee} + 8 \bar {Y} _ {\varepsilon} ^ {\vee} \bar {Y} _ {\varepsilon} ^ {\vee \vee}) \\ & + \lambda^ {7} (\bar {Y} _ {\varepsilon} ^ {\vee \vee} \bar {Y} _ {\varepsilon} ^ {\vee \vee} + 8 \bar {Y} _ {\varepsilon} ^ {\vee \vee} \bar {Y} _ {\varepsilon} ^ {\vee \vee} + 1 6 \bar {Y} _ {\varepsilon} ^ {\vee \vee} \bar {Y} _ {\varepsilon} ^ {\vee \vee}). \end{array}\tag{2.10}
$$

The precise form of$\bar { \mathcal { R } } _ { \varepsilon } ^ { \star }$is actually irrelevant. The important fact is that one should retain from this expression is that, by combining Theorem 2.3 with Proposition$\mathsf { A } . 9 .$ there is a limiting process$\bar { \mathcal { R } } ^ { \star }$such that$\bar { \mathcal { R } } _ { \varepsilon } ^ { \star }  \bar { \mathcal { R } } ^ { \star }$in probability in$\mathcal { C } ( \mathbf { R } , \mathcal { C } ^ { - \beta } )$for every$\beta > 0$

With these notations, (2.9) can be rewritten as

$$
\begin{array}{r} \partial_ {t} u _ {\varepsilon} = \partial_ {x} ^ {2} u _ {\varepsilon} + 2 \lambda \bar {Y} _ {\varepsilon} ^ {\bullet} (\partial_ {x} u _ {\varepsilon} + \lambda^ {3} \bar {Y} _ {\varepsilon} ^ {\mathbb {V}} + 4 \lambda^ {3} \bar {Y} _ {\varepsilon} ^ {\mathbb {X}}) \\ + \lambda (\partial_ {x} u _ {\varepsilon}) ^ {2} + 2 \lambda \partial_ {x} u _ {\varepsilon} \partial_ {x} \bar {h} _ {\varepsilon} ^ {\star} + \bar {\mathcal {R}} _ {\varepsilon} ^ {\star}. \end{array}\tag{2.11}
$$

Since, by Theorem$2 . 3 , \bar { h } _ { \varepsilon } ^ { \star }$is continuous with values in$\mathcal { C } ^ { 1 - \delta }$for every$\delta > 0$, it follows that if we are able to find a solution$u _ { \varepsilon }$taking values in$\mathcal { C ^ { \alpha } }$for some$\alpha > 1$ with a uniform bound as$\varepsilon \to 0$, there is no problem in making sense of the terms on the second line of this equation in the limit$\varepsilon \to 0$

The problem of course is the second term. Indeed, since$\bar { Y } ^ { \bullet } \in \mathcal { C } ^ { \gamma }$only for $\gamma < - \frac { 1 } { 2 }$, we would need$u _ { \varepsilon } ( t )$to converge in$\mathcal { C ^ { \alpha } }$for$\alpha > \frac { 3 } { 2 }$for this term to make sense in the limit (see Remark A.10 below). This however is hopeless since, by the usual maximal regularity results, the action of the heat semigroup allows us to gain only two spatial derivatives so that the best we can hope for is that$u _ { \varepsilon } ( t )$converges in$\mathcal { C ^ { \alpha } }$precisely for every$\alpha < \frac { 3 } { 2 }$only!

This is where the theory of rough paths comes into play. Denote by$v _ { \varepsilon }$the derivative of$u _ { \varepsilon }$, so that (2.11) becomes

$$
\partial_ {t} v _ {\varepsilon} = \partial_ {x} ^ {2} v _ {\varepsilon} + 2 \lambda \partial_ {x} (\bar {Y} _ {\varepsilon} ^ {\bullet} (v _ {\varepsilon} + \lambda^ {3} \bar {Y} _ {\varepsilon} ^ {\mathbb {W}} + 4 \lambda^ {3} \bar {Y} _ {\varepsilon} ^ {\mathbb {X}})) + \partial_ {x} F _ {\varepsilon} (v _ {\varepsilon}, t),\tag{2.12}
$$

where the nonlinearity$F _ { \varepsilon }$is given by

$$
F _ {\varepsilon} = \lambda v _ {\varepsilon} ^ {2} + 2 \lambda v _ {\varepsilon} \partial_ {x} \bar {h} _ {\varepsilon} ^ {\star} + \bar {\mathcal {R}} _ {\varepsilon} ^ {\star}.
$$

As already mentioned, this nonlinearity is expected to be$\mathrm { \ " { n i c e } } ^ { , }$, in the sense that we can use classical functional analysis to make sense of it as$\varepsilon  0 .$, so that we do not consider it for the moment and will treat it as a perturbation later on.

If the right hand side of (2.12) were well-posed in the limit$\varepsilon \to 0$, we would expect the solution$v _ { \varepsilon }$to look at small scales like the solution$\Phi _ { \varepsilon }$to

$$
\partial_ {t} \Phi_ {\varepsilon} = \partial_ {x} ^ {2} \Phi_ {\varepsilon} + \partial_ {x} ^ {2} Y _ {\varepsilon} ^ {\bullet},\tag{2.13}
$$

so we define$\Phi _ { \varepsilon }$by

$$
\Phi_ {\varepsilon , t} = \int_ {- \infty} ^ {t} P _ {t - s} \partial_ {x} ^ {2} Y _ {\varepsilon , s} ^ {\bullet} d s,\tag{2.14}
$$

where$P _ { t }$is the heat semigroup. Since$\partial _ { x } ^ { 2 } Y _ { \varepsilon , s } ^ { \bullet }$has zero average, this is well-defined as long as$Y _ { \varepsilon , s } ^ { \bullet }$does not grow too fast for large times.

The idea now is to try to solve (2.12) in a space of functions that are “controlled by$\Phi ^ { \prime \prime }$in the sense that there exists a function$v ^ { \prime }$such that the “remainder term”

$$
R _ {\varepsilon , t} ^ {v} (x, y) = \delta v _ {\varepsilon , t} (x, y) - v _ {\varepsilon , t} ^ {\prime} (x) \delta \Phi_ {\varepsilon , t} (x, y),\tag{2.15}
$$

satisfies a bound of the type$\| R _ { \varepsilon , t } ^ { v } \| _ { \alpha } < \infty .$, uniformly as$\varepsilon  0 .$, for some α$> \frac { 1 } { 2 }$ Here, we have made use of the shorthand notation$\delta v ( x , y ) = v ( y ) - v ( x )$and similarly for$\delta \Phi$. This notation will be used repeatedly in the sequel. What a bound like (2.15) tells us is that, at very small scales, v looks like some multiple of$\Phi .$ modulo a remainder term that behaves as if it was α-Holder for some¨$\alpha > \frac { 1 } { 2 }$. Note that this is a purely local property of the increments.

This suggests that, if we were able to show “by hand” that$\Phi _ { \varepsilon , t } \partial _ { x } Y _ { \varepsilon , t } ^ { \bullet }$converges to a limiting distribution as$\varepsilon  0$, then one may be able to use this knowledge to give a meaning to the expression$v \partial _ { x } Y ^ { \bullet }$for those functions v admitting a “derivative process” v<sup>0</sup> such that the remainder$R _ { t } ^ { v } ( x , y )$defined as in (2.15) satisfies $\| R _ { t } ^ { v } \| _ { \alpha } < \infty$for some$\alpha > \frac { 1 } { 2 }$. This is precisely what the theory of controlled rough paths [Gub04] allows us to do. For any fixed t, let$\mathbf { Y } _ { t }$be the function of two variables defined by

$$
\mathbf {Y} _ {\varepsilon , t} (x, y) = \int_ {x} ^ {y} \delta \Phi_ {\varepsilon , t} (x, z) d Y _ {\varepsilon , t} ^ {\bullet} (z).\tag{2.16}
$$

It is important to note that, for every t and every$\varepsilon , \ \mathbf { Y } _ { \varepsilon , t }$satisfies the algebraic relation

$$
\mathbf {Y} _ {\varepsilon , t} (x, z) - \mathbf {Y} _ {\varepsilon , t} (x, y) - \mathbf {Y} _ {\varepsilon , t} (y, z) = \delta \Phi_ {\varepsilon , t} (x, y) \delta Y _ {\varepsilon , t} ^ {\bullet} (y, z),\tag{2.17}
$$

for every x,$y , z \in S ^ { 1 }$. One can then show, and this is the content of Proposition 7.13 below, that there exists a process Y with values in$\mathcal { C } _ { 2 } ^ { \gamma }$such that$\mathbf Y _ { \varepsilon } \to \mathbf Y$in probability in$\mathcal { C } ( \mathbf { R } , \mathcal { C } _ { 2 } ^ { \gamma } )$for every$\gamma < 1$

We refer to Section 3 below for more details, but the gist of the theory of controlled rough paths is that one can use the process Y in order to define a “rough integral”$\begin{array} { r } { f _ { x } ^ { y } A _ { t } ( z ) d Y _ { t } ^ { \bullet } ( z ) } \end{array}$as a convergent limit of compensated Riemann sums for every smooth test function$\varphi$and for every function$A _ { t }$such that, for some$\delta > 0$ there exists$A _ { t } ^ { \prime } \in \mathcal { C } ^ { \delta }$and$R _ { t } ^ { \dot { A } } \in \mathcal { C } _ { 2 } ^ { 1 / 2 + \delta }$with

$$
R _ {t} ^ {A} (x, y) = \delta A _ {t} (x, y) - A _ {t} ^ {\prime} (x) \delta \Phi_ {t} (x, y).\tag{2.18}
$$

See Theorem 3.2 below for a precise formulation of this statement. It is important to note at this stage that the notation$f$used for the rough integral is really an abuse of notation. Indeed, it does in general depend not just on A and$Y .$, but also on a choice of Y satisfying (2.17), as well as on the choice of$A ^ { \prime }$in (2.18). It is only when Y is actually given by (2.16) that it coincides with the Riemann integral, independently of the choice of$A ^ { \prime } .$. See equation 3.10 below for more details.

Remark 2.6 A number of recent results have made use of the theory of rough paths to treat classes of stochastic PDEs, see for example [CF09, CFO11, GT10, Tei11]. In all of these cases, the theory of rough paths was used to deal with the lack of temporal regularity of the equations. In this article, as in [Hai11, HW10], we use it instead in order to deal with the lack of spatial regularity.

In this way, we can indeed make sense of the product$v _ { t } \partial _ { x } Y _ { t } ^ { \bullet }$as a distribution, provided that$v _ { t }$admits a sufficiently regular decomposition as in (2.18) for some “derivative process”$v _ { t } ^ { \prime } .$In a way, this is reminiscent of the technique of “two-scale convergence” developed in [Ngu89, All92]. The main differences are that it does not require any periodicity at the small scale and that it does not rely on any explicit small parameter ε, both of which make it particularly adapted to situations where the small-scale fluctuations are random. See however Section 2.4 below for an example with deterministic periodic data where the results of this article also apply.

The same theory can also be used in order to make sense of the term$\hat { Y } _ { t } ^ { \ast } \hat { Y } _ { t } ^ { \bullet }$in (2.12). It is indeed possible to show that$\bar { Y } _ { t } ^ { \ast }$is controlled by$\bar { Y } _ { t } ^ { \bullet }$in the sense that the process$R _ { t } ^ { \aleph }$defined by

$$
R _ {t} ^ {\mathbb {V}} (x, y) = \delta \bar {Y} _ {t} ^ {\mathbb {V}} (x, y) - \bar {Y} _ {t} ^ {\mathbb {V}} (x) \delta \Phi_ {t} (x, y),\tag{2.19}
$$

takes values in$C _ { 2 } ^ { \frac { 1 } { 2 } + \zeta }$for some$\zeta > 0$. Furthermore, the corresponding processes for$\varepsilon > 0$do converge to$R ^ { \aleph }$in that topology, which turns out to be surprisingly difficult to prove, see Theorem 7.4 below. In view of all of these convergence results, the space$\mathcal { X }$and the map$\Psi \colon \Omega  \mathcal X$appearing in Theorem 1.1 and Proposition 1.5 are then defined as follows:

Definition 2.7 Setting$\bar { \mathcal { T } } _ { 0 } = \{ \bullet , \vee , \vee , \vee , \vee \}$, the Frechet space ´ W is given by

$$
\mathcal {W} = \left(\bigoplus_ {\tau \in \bar {\mathcal {T}} _ {0}} \mathcal {X} _ {\tau}\right) \oplus \mathcal {C} (\mathbf {R}, \mathcal {C} _ {2} ^ {\frac {3}{4}}) \oplus \mathcal {C} (\mathbf {R}, \mathcal {C} _ {2} ^ {\frac {3}{4}}),
$$

and the map$\Psi \colon \Omega  \mathcal { W }$is given by the random variable

$$
\Psi = \left(\bigoplus_ {\tau \in \bar {\mathcal {T}} _ {0}} Y ^ {\tau}\right) \oplus \mathbf {Y} \oplus R ^ {\mathbb {X}}.\tag{2.20}
$$

The space$\mathcal { X } \subset \mathcal { W }$is then defined as the algebraic variety determined by the relations (2.17) and (2.19). Since X is closed (as a subset of W) and Ψ is the limit in probability of maps$\Psi _ { \varepsilon }$which map Ω into$x ,$, one automatically has$\Psi ( \omega ) \in \mathcal { X }$ for almost every ω.

We now have all the ingredients necessary to reformulate (2.12) as a fixed point map by considering its mild formulation. We will then turn this into a fixed point argument for (2.11), which is equivalent save for the constant Fourier mode. Using the variation of constants formula, we can rewrite solutions to (2.12) for every fixed realisation of$\{ Y ^ { \tau } \} _ { \tau \in \hat { T } }$and every fixed initial condition$v _ { 0 }$as

$$
v _ {\varepsilon} = \mathcal {K} _ {0} (v _ {\varepsilon}),
$$

where the map$\kappa _ { 0 }$is given by

$$
\begin{array}{r} (\mathcal {K} _ {0} v) _ {t} = P _ {t} v _ {0} + 2 \lambda \partial_ {x} \int_ {0} ^ {t} P _ {t - s} \Big ((v _ {s} + 4 \lambda^ {3} \bar {Y} _ {\varepsilon , s} ^ {\mathbb {V}}) \bar {Y} _ {\varepsilon , s} ^ {\bullet} \Big) d s \\ + \partial_ {x} \int_ {0} ^ {t} P _ {t - s} (\lambda^ {4} \bar {Y} _ {\varepsilon , s} ^ {\mathbb {V}} \bar {Y} _ {\varepsilon , s} ^ {\bullet} + F _ {\varepsilon} (v _ {\varepsilon}, s)) d s, \end{array}
$$

were$P _ { t }$denotes the heat semigroup, the kernel of which we will denote by$p _ { t }$. For any given smooth data$\{ Y ^ { \tau } \} _ { \tau \in \bar { \mathcal { T } } }$, the map$\kappa _ { 0 }$is well-defined as a map from the set of smooth functions v into itself. The problem with$\kappa _ { 0 }$is that it is not possible to extend it to sufficiently large functional spaces by performing a classical completion procedure. The idea is therefore to first extend its definition to smooth input data $\Psi = ( \{ Y ^ { \tau } \} _ { \tau \in \bar { \mathcal { T } } } , \mathbf { Y } , R ^ { \check { \mathtt { V } } } ) \in \mathcal { X } .$, and to smooth triples$V = ( v , v ^ { \prime } , R ^ { v } )$such that the additional algebraic relations (2.15) are satisfied, by setting

$$
\begin{array}{l} \mathcal {K} (v _ {0}, V, \Psi) _ {t} = P _ {t} v _ {0} + 2 \lambda \int_ {0} ^ {t} \oint_ {S ^ {1}} p _ {t - s} ^ {\prime} (\cdot - y) \left(v _ {s} (y) + 4 \lambda^ {3} \bar {Y} _ {s} ^ {\vee} (y)\right) d Y _ {s} ^ {\bullet} (y) d s \\ \quad + \partial_ {x} \int_ {0} ^ {t} P _ {t - s} \left(\lambda^ {4} \bar {Y} _ {s} ^ {\vee} \bar {Y} _ {s} ^ {\bullet} + F (v, \Psi , s)\right) d s, \end{array} \tag {2.2}\tag{2.21}
$$

where the “rough integral” R is defined as in (3.4) below and where we set as before

$$
F (v, \Psi , s) = \lambda v _ {s} ^ {2} + 2 \lambda v _ {s} \partial_ {x} \bar {h} ^ {\star} (\Psi) _ {s} + \bar {\mathcal {R}} ^ {\star} (\Psi) _ {s},\tag{2.22}
$$

with$h ^ { \star }$and$\bar { \mathcal { R } } ^ { \star }$given by (2.7) and (2.10) respectively. Actually, the precise definition of$f$really does not matter at this stage. Indeed, if we denote by$\mathcal { X } _ { s } \subset \mathcal { X }$ the set of smooth elements in X such that Y is given by (2.16) and$R ^ { \aleph }$is given by (2.19), then$f$coincides with the usual Riemann integral and therefore K coincides with$\kappa _ { 0 }$on$\mathcal { X } _ { s }$. Furthermore, by Proposition 3.3 below,$\mathcal { X } _ { s }$is dense in X and, as we will see in Theorem 2.9 below, K is the unique continuous extension of$\kappa _ { 0 }$to X. In this sense, we have not changed the classical notion of a smooth solution to (2.12) at all, but have simply extended it to a larger class of input data.

Remark 2.8 If Y is defined differently from (2.16), even$i f i t$is smooth, we obtain different solutions, see Section 2.3 below. While these different solutions may appear “unphysical” at first sight, they actually have a clear interpretation in terms of limiting points of solutions to the KPZ equation with highly oscillatory data, see Section 2.4 for an explicit example.

For fixed$\kappa > 0$(small enough as we will see shortly) and$T > 0$, denote now by$B _ { \star , T }$the closure of the space of smooth quadruples$V = ( m , v , v ^ { \prime } , R ^ { v } )$, where m is a real-valued function of time only, v and$v ^ { \prime }$are functions of time and space, and$R ^ { v }$is a function of time and two spatial variables, under the norm

$$
\begin{array}{c} \| m, v, v ^ {\prime}, R ^ {v} \| _ {\star , T} = \sup _ {t \in (0, T ]} t ^ {1 - 2 \kappa} (\| v _ {t} \| _ {\frac {1}{2} - \kappa} + \| v _ {t} ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}} + \| R _ {t} ^ {v} \| _ {\frac {1}{2} + 2 \kappa} + t ^ {\frac {3 \kappa - 1}{2}} \| v _ {t} \| _ {\infty}) \\ + \sup _ {0 <   s <   t \leq T} \frac {s ^ {1 - 2 \kappa}}{| t - s | ^ {2 \kappa}} \| v _ {t} - v _ {s} \| _ {\infty} + \sup _ {t \in (0, T ]} | m _ {t} |. \end{array}
$$

Here,$m _ { t }$is interpreted as the spatial mean of$u _ { t }$, so that the natural projection map $\pi \colon \mathcal { B } _ { \star , T } \to \mathcal { C } ( [ 0 , T ] , \mathcal { C } ^ { \frac { 3 } { 2 } - \kappa } )$recovering u from V is given by

$$
(\pi V) _ {t} = \mathcal {I} v _ {t} + m _ {t},
$$

where$\mathcal { T }$is the integration operator given by the Fourier multiplier$( 1 - \delta _ { k , 0 } ) / ( i k )$ We furthermore denote by$\mathcal { V } _ { \star , T }$the closed algebraic variety in X ⊕$B _ { \star , T }$determined by the additional relation (2.15). Note that$\mathcal { V } _ { \star , T }$is again a Polish space equipped with a natural metric given by the restriction of the product norm on $\mathcal { W } \oplus B _ { \star , T }$. We now use$\kappa$as a building block for the map$\hat { \mathcal { M } }$appearing in Proposition 1.5 in the following way. For any smooth element$( h _ { 0 } , \Psi , V ) \in \mathcal { C } ^ { \infty } \times \mathcal { V } _ { \star , T }$ and using furthermore the shorthand notation$V = ( m , v , v ^ { \prime } , R ^ { v } )$, we set

$$
\hat {\mathcal {M}} (h _ {0}, \Psi , V) = \left(\mathcal {J} (V, \Psi), \mathcal {K} (\partial_ {x} (h _ {0} - h _ {0} ^ {\star} (\Psi)), V, \Psi), \mathcal {K} ^ {\prime} (V, \Psi), R ^ {\mathcal {M}}\right),
$$

where$\kappa$is as in (2.21),$\kappa ^ { \prime }$is given by

$$
\mathcal {K} ^ {\prime} (V, \Psi) = 2 \lambda \big (v + 4 \lambda^ {3} \bar {Y} ^ {\mathbb {V}} + \lambda^ {3} \bar {Y} ^ {\mathbb {V}} \big),\tag{2.23}
$$

$R ^ { \mathcal { M } }$is defined by the relation (2.15), and

$$
\begin{array}{r l} & {\mathcal {J} (V, \Psi) _ {t} = \Pi_ {0} \big (h _ {0} - h _ {0} ^ {\star} (\Psi) \big) + \int_ {0} ^ {t} \Pi_ {0} F (v, \Psi , s) d s} \\ & {\qquad + \frac {\lambda}{\pi} \int_ {0} ^ {t} \oint_ {S ^ {1}} \Big (v _ {s} (y) + 4 \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {X}} (y) + \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {W}} (y) \Big) d Y _ {s} ^ {\bullet} (y) d s.} \end{array}
$$

(The latter expression is nothing but the constant mode of the right hand side of (2.21) before that expression was differentiated.)

At this stage of our construction, it seems that the choice (2.23) for$\kappa ^ { \prime }$is somewhat arbitrary. Intuitively, it should be the right choice though, since this is precisely the factor that appears in the second term of (2.12), so that one does expect it to describe the amplitude of the small-scale fluctuations of the solution. Mathematically, the fact that this is indeed the correct choice is seen by the fact that this is the only choice guaranteeing that the image of$\hat { \mathcal { M } }$lies again in$B _ { \star , T } ^ { } ,$ so that we can set up a fixed point argument. This is the content of the following result which, together with the convergence results already mentioned earlier in this section, forms the core of this article. The space$B _ { \Psi , T }$appearing in the statement is defined as in Proposition 1.5.

Theorem 2.9 For every$\kappa < \textstyle { \frac { 1 } { 1 2 } } ,$, every$T > 0$, and every$\beta > 2 \kappa ,$, the map$\hat { \mathcal { M } }$ extends uniquely to a locally uniformly continuous mapfrom$\mathcal { C } ^ { \beta } \times \mathcal { N } _ { \star , T }$to$B _ { \star , T }$

Furthermore,for every$\Psi \in { \mathcal { X } }$and every$h _ { 0 } \in \mathcal { C } ^ { \beta }$, there exists$T > \complement$depending only on the norms of Ψ and$h _ { 0 }$such that the map$V \mapsto { \hat { \mathcal { M } } } ( h _ { 0 } , \Psi , V )$is a strict contraction in a sufficiently small ball of$B _ { \Psi , T }$. Furthermore, the equation$V =$ $\hat { \mathcal { M } } ( h _ { 0 } , \Psi , V )$admits a unique solution in all of$B _ { \Psi , T }$

Proof. First, note that, since we defined$\mathcal { R } ^ { \mathcal { M } }$such that (2.15) holds, we ensure that, at least for smooth data,$\hat { \mathcal { M } } ( h _ { 0 } , \Psi , V ) \in \mathcal { B } _ { \Psi , T }$for every$( h _ { 0 } , \Psi , V ) \in \mathcal { C } ^ { \beta } \times \mathcal { V } _ { \star , T }$ The local uniform continuity of$\hat { \mathcal { M } }$is the hard part of this result, and this is obtained in Proposition 4.3 below.

The contraction properties and the existence of a unique fixed point for$\hat { \mathcal { M } }$ with its first two arguments fixed then follows from Theorem 4.8, noting that its assumptions are satisfied for every$\Psi$by the definition of the space X in which the input Ψ lies.□

At this point, it is legitimate to question whether such a complicated nonlinear construction is really necessary, or whether one could instead find fixed Banach spaces$\hat { B } _ { T }$and$\hat { \mathcal X }$such that$\hat { \mathcal { M } }$extends to a continuous map$\hat { \mathcal { X } } \times \hat { B } _ { T }  \hat { B } _ { T }$and has a fixed point for small enough time horizon$T .$

While it doesn’t seem easy to disprove such a statement at this level of generality, the results in [Lyo91] strongly suggest that it is not possible to find any such spaces. Indeed, the following is a straightforward extension of [Lyo91]:

Theorem 2.10 There exists no separable Banach space B supporting Wiener measure and such that the bilinearfunctional

$$
\mathcal {I} \colon (u, v) \mapsto \int_ {0} ^ {1} u (t) d v (t),
$$

defined on$\mathcal { H } = H ^ { 1 } ( [ 0 , 1 ] )$, extends to a continuousfunction on$B \times B .$

Proof. Note first that we can assume without loss of generality that$B \subset \mathcal { C } ( [ 0 , 1 ] )$ since larger spaces make it only harder for$\mathcal { T }$to be continuous. Also, by assumption,$\boldsymbol { B }$is the completion of H under some norm$\| \cdot \| _ { B }$. Assuming by contradiction that$\mathcal { T }$is continuous on$B \times B .$, it follows from Fernique’s theorem that $\textstyle \int { \mathcal { T } } ( u , v ) \mu ( d u , d v ) < \infty$, for every measure$\mu$on$B \times B$such that both of its marginals are given by Wiener measure.

Let$\Pi _ { N } \colon B \to \mathcal { H }$be the projection onto the first N Fourier modes which, since $B \subset \mathcal { C } ( [ 0 , 1 ] )$, is a bounded operator for every N. The construction in [Lyo91] then yields a measure$\mu$as above with the property that

$$
\int \mathcal {I} (\Pi_ {N} u, \Pi_ {N} v) \mu (d u, d v) \sim \log N,\tag{2.24}
$$

for$N$large. Since Fourier modes form an orthonormal basis of$\mathcal { H } ,$it follows from [Bog98, Thm 3.5.1] that$( \Pi _ { N } u , \Pi _ { N } v )  ( u , v )$µ-almost surely as$N \to \infty$. Since weak convergence implies tightness in separable Banach spaces, we conclude from Fernique’s theorem that

$$
\sup _ {N} \int \| \Pi_ {N} u \| _ {\mathcal {B}} \| \Pi_ {N} v \| _ {\mathcal {B}} \mu (d u, d v) <   \infty ,
$$

which is a contradiction to (2.24).

Since, for any fixed$t ,$both$Y _ { t } ^ { \bullet }$and$v _ { t }$in (2.21) have regularity properties identical to those of Brownian motion (actually, both$Y _ { t } ^ { \bullet }$and$\Phi _ { t }$are nothing but centred Brownian bridges), Theorem 2.10 leaves no doubt that the classical approach to making sense of (2.12) in the limit$\varepsilon \to 0$is doomed to failure.

We are now able to provide a proof of the results stated in the introduction:

ProofofProposition 1.5. The spaces$B _ { \star , T } , \mathcal { X }$and$\mathcal { V } _ { \star , T }$as well as the maps$\hat { \mathcal { M } }$and $\begin{array} { r } { h ^ { \star } = \sum _ { \tau \in \bar { T } } Y ^ { \tau } } \end{array}$were already defined, so that it suffices to verify that they satisfy the required properties.

Given an initial condition$h _ { 0 } \in \mathcal { C } ^ { \beta }$, we set$v _ { 0 } = \partial _ { x } { \left( h _ { 0 } - h _ { 0 } ^ { \star } \right) }$, so that$v _ { 0 } \in$ $\mathcal { C } ^ { \beta - 1 }$. We know from Theorem 2.9 that one can choose$T > 0$depending only on$\lVert \boldsymbol { v } _ { 0 } \rVert _ { \beta - 1 }$and$\| \Psi \| _ { \mathcal { W } }$such that the map$\hat { \mathcal { M } }$is a contraction in its last argument and we denote its fixed point by$\hat { S } _ { \mathrm { R } } ^ { T } ( h _ { 0 } , \Psi ) \in \mathcal { V } _ { \star , T }$. By performing the same continuation procedure as in the proof of the existence of a unique maximal solution for ordinary differential equations, we obtain an explosion time$T _ { \star } ( h _ { 0 } , \Psi )$, which is the supremum over all times$T$such that the fixed point problem in$B _ { \star , T }$has a solution. The fact that all Holder norms of the solution explode as¨$t  T _ { \star }$is an immediate consequence of the fact that the local existence time can be controlled in terms of the Holder norm of the initial condition. Furthermore, these solutions¨ are all unique by the same argument as in the proof of Theorem 4.8 below, and they agree on their common domains of definition.

The third property, namely the continuity of$\hat { S } _ { \mathrm { R } } ^ { T }$in a neighbourhood of$( h _ { 0 } , \Psi _ { 0 } )$ whenever$T < T _ { \star } ( h _ { 0 } , \Psi _ { 0 } )$also follows in the same way as in the classical theory of ODEs. This then immediately implies the lower semicontinuity of$T _ { \star }$, since its definition implies that one has$T _ { \star } ( h , \Psi ) > T$for every$( h , \Psi )$in such a neighbourhood. Finally, if we define$\Theta _ { t }$to be the canonical time-shift on$\mathcal { X }$(which is a continuous map for every$t \in \mathbf { R } )$, then the cocycle property follows immediately from the elementary properties of the integral and the heat semigroup.□

Proof of Theorem 1.1. We now define the map$S _ { \mathrm { R } }$by setting

$$
\mathcal {S} _ {\mathrm{R}} (h _ {0}, \Psi) _ {t} = h _ {\star} (\Psi) _ {t} + \bigl (\pi \hat {\mathcal {S}} _ {\mathrm{R}} (h _ {0}, \Psi) \bigr) _ {t},
$$

for$t < T _ { \star } ( h _ { 0 } , \Psi )$, and$S _ { \mathrm { R } } ( h _ { 0 } , \Psi ) _ { t } = \infty$for$t > T _ { \star } ( h _ { 0 } , \Psi )$. Since one necessarily has lim$\rvert _ { t  T _ { \star } } \lVert S _ { \mathrm { R } } ( h _ { 0 } , \Psi ) _ { t } \rVert _ { \frac { 1 } { 2 } - \beta } = + \infty$, the definition of the topology on $\bar { \mathcal { C } } ^ { \frac { 1 } { 2 } - \beta }$implies that the map$S _ { \mathrm { R } }$constructed in this way does indeed take values in $\mathcal { C } ( \mathbf { R } _ { + } , \bar { \mathcal { C } } ^ { \frac { 1 } { 2 } - \beta } )$

If we furthermore denote by$S _ { \mathrm { R } } ^ { T }$the restriction of$S _ { \mathrm { R } }$to the interval$[ 0 , T ]$, then it follows from Proposition 1.5 that$S _ { \mathrm { R } } ^ { T }$is continuous on the set$\{ ( h , \Psi ) : T _ { \star } ( h , \Psi ) >$ $T \}$. In particular, this is stronger than the claimed continuity property.

It remains to show that, for every fixed initial condition$h _ { 0 }$, one has$S _ { \mathrm { C H } } ( h _ { 0 } , \omega ) =$ $S _ { \mathrm { R } } ( h _ { 0 } , \Psi ( \omega ) )$almost surely. Fix$T > 0$, and let$S _ { T } ( h _ { 0 } ) = \{ \Psi \in \mathcal { X } : T _ { \star } ( h _ { 0 } , \Psi ) \leq$ $T \}$, which is the set of possible discontinuities of$S _ { \mathrm { R } } ( h _ { 0 } , \cdot )$. By construction, for every$\varepsilon > 0 , S _ { \mathrm { R } } ^ { T } ( h _ { 0 } , \Psi _ { \varepsilon } ( \omega ) )$almost surely agrees with the solution$h _ { \varepsilon }$to (1.5) up to time$T$. Since we know on the one hand that$\Psi _ { \varepsilon } \to \Psi$in probability, and on the other hand that$h _ { \varepsilon }$converges in probability to$\boldsymbol { S } _ { \mathrm { C H } } ( h _ { 0 } , \omega )$, the stated claim follows if we can show that${ \bf P } ( \Psi ( \omega ) \in S _ { T } ( h _ { 0 } ) ) = 0$for every$T > 0$and every initial condition$h _ { 0 } \in \mathcal { C } ^ { \beta }$

Assume by contradiction that there exists$h _ { 0 }$and$\kappa > 0$such that$\mathbf { P } ( \Psi ( \omega ) \in$ $S _ { T } ( h _ { 0 } ) ) \ge \kappa$. It follows from our construction that, for every$\Psi _ { 0 } \in S _ { T } ( h _ { 0 } )$and every$K > 0$, there exists a neighbourhood$V$of$\Psi _ { 0 }$in$\mathcal { X }$such that

$$
\sup _ {t \leq T} \| \mathcal {S} _ {\mathrm{R}} (h _ {0}, \Psi) \| _ {\beta} \geq K  , \quad \forall \Psi \in V  .
$$

Since$\Psi _ { \varepsilon } \to \Psi$in probability, we conclude that there exists$\varepsilon _ { 0 } > 0$such that

$$
\mathbf {P} (\sup _ {t \leq T} \| h _ {t, \varepsilon} \| _ {\beta} \geq K) \geq \frac {\kappa}{2},
$$

uniformly over all$\varepsilon ~ < \varepsilon _ { 0 }$. This on the other hand is ruled out by the fact that $h _ { \varepsilon }  h$in probability in$\mathcal { C } ( [ 0 , T ] , \mathcal { C } ^ { \beta } )$.□

To conclude this section, we give an explicit interpretation of the solution map $S _ { \mathrm { R } }$for arbitrary smooth data Ψ and we use the continuity of the solution map to provide a novel homogenisation result.

## 2.3 Smooth solutions

It is instructive to see what is the meaning of$S _ { \mathrm { R } } ( h _ { 0 } , \Psi )$for general smooth data $\Psi = ( \{ Y ^ { \tau } \} _ { \tau \in \bar { \mathcal { T } } } , \mathbf { Y } , R ^ { \check { \mathsf { V } } } ) \in \mathcal { X }$. Given such smooth data, we set

$$
\xi (x, t) \stackrel {\mathrm{def}} {=} \partial_ {t} Y _ {t} ^ {\bullet} (x) - \partial_ {x} ^ {2} Y _ {t} ^ {\bullet} (x),
$$

as well as

$$
H _ {t} (x) = \sum_ {\tau = [ \tau_ {1}, \tau_ {2} ] \in \bar {\mathcal {T}}} \lambda^ {| \tau |} \Bigl (\partial_ {t} Y _ {t} ^ {\tau} (x) - \partial_ {x} ^ {2} Y _ {t} ^ {\tau} (x) - \bar {Y} _ {t} ^ {\tau_ {1}} (x) \bar {Y} _ {t} ^ {\tau_ {2}} (x) \Bigr),\tag{2.25}
$$

which is some kind of “defect” by which the$Y ^ { \tau }$may fail to satisfy their constituent equations. Defining Φ as in (2.14) (but with$Y _ { \varepsilon } ^ { \bullet }$replaced by$Y ^ { \bullet } )$, we also define G to be the smooth function such that

$$
\mathbf {Y} _ {t} (x, y) = \int_ {x} ^ {y} \Phi_ {t} (z) d Y _ {t} ^ {\bullet} (z) + \int_ {x} ^ {y} G _ {t} (z) d z.
$$

Such a function always exists since Y satisfies (2.17) by definition of$\mathcal { X }$and since any two functions satisfying these relations always differ by an increment of a function of one variable.

With this notation, we then have the following result:

Theorem 2.11 Let$\Psi \in { \mathcal { X } }$be a smooth element, let$h _ { 0 } \in \mathcal { C } ^ { \infty }$, and let H, G and$\xi$ be as above. Then,$T _ { \star } ( h _ { 0 } , \Psi ) = + \infty$and$S _ { \mathrm { R } } ( h _ { 0 } , \Psi )$is the unique global solution to

$$
\partial_ {t} h _ {t} = \partial_ {x} ^ {2} h _ {t} + \lambda (\partial_ {x} h _ {t}) ^ {2} + 4 \lambda^ {2} G _ {t} \partial_ {x} (h _ {t} - J _ {t} (\Psi)) + H + \xi ,\tag{2.26}
$$

where$J _ { t } ( \Psi )$is thefunction given by

$$
J _ {t} (\Psi) = Y _ {t} ^ {\bullet} + \lambda Y _ {t} ^ {\vee} - \lambda^ {2} Y _ {t} ^ {\vee},
$$

with initial condition$h _ { 0 }$

Proof. By construction, we have

$$
h = u + \sum_ {\tau \in \bar {\mathcal {T}}} \lambda^ {| \tau |} Y ^ {\tau},
$$

where u solves the fixed point equation

$$
\begin{array}{l} u = (P _ {t} u _ {0}) (x) + 2 \lambda \int_ {0} ^ {t} \int_ {S ^ {1}} p _ {t - s} (x - y) (\partial_ {x} u _ {s} (y) + 4 \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {X}} (y)) d Y _ {t} ^ {\bullet} (y) d s \\ \quad + \int_ {0} ^ {t} P _ {t - s} (\lambda^ {4} \bar {Y} _ {s} ^ {\mathbb {W}} (y) \bar {Y} _ {s} ^ {\bullet} (y) + F (u, \Psi , s)) d s, \end{array} \tag {2.}\tag{2.27}
$$

where$\begin{array} { r } { u _ { 0 } = h _ { 0 } - \sum _ { \tau \in \bar { \mathcal { T } } } \lambda ^ { | \tau | } Y _ { 0 } ^ { \tau } } \end{array}$and F is as in (2.22). It then follows from (3.10) below and the fact that, by construction,$\partial _ { x } u _ { s } + 4 \lambda ^ { 3 } \bar { Y } _ { s } ^ { \bar { \psi } }$is a rough path controlled by Φ with derivative process$2 \lambda ( \partial _ { x } u _ { s } + 4 \lambda ^ { 3 } \bar { Y } _ { s } ^ { \sf X } + \lambda ^ { 3 } \bar { Y } _ { s } ^ { \sf X } + 2 \lambda ^ { 2 } \bar { Y } _ { s } ^ { \sf X } )$, that one has the identity

$$
\begin{array}{l} \int_ {S ^ {1}} p _ {t - s} (x - y) \big (\partial_ {x} u _ {s} (y) + 4 \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {V}} (y) \big) d Y _ {s} ^ {\bullet} (y) \\ = \int_ {S ^ {1}} p _ {t - s} (x - y) \big (\partial_ {x} u _ {s} (y) + 4 \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {V}} (y) \big) \partial_ {x} Y _ {s} ^ {\bullet} (y) d y \\ \quad + 2 \lambda \int_ {S ^ {1}} p _ {t - s} (x - y) \big (\partial_ {x} u _ {s} + 4 \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {V}} + \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {V}} + 2 \lambda^ {2} \bar {Y} _ {s} ^ {\mathbb {V}} \big) G _ {s} (y) d y \\ = \int_ {S ^ {1}} p _ {t - s} (x - y) \big (\partial_ {x} u _ {s} (y) + 4 \lambda^ {3} \bar {Y} _ {s} ^ {\mathbb {V}} (y) \big) \partial_ {x} Y _ {t} ^ {\bullet} (y) d y \\ \quad + 2 \lambda \int_ {S ^ {1}} p _ {t - s} (x - y) \partial_ {x} \big (h _ {s} - J _ {s} (\Psi) \big) G _ {s} (y) d y. \end{array}
$$

Similarly, it follows from (2.25) that

$$
\begin{array}{r l} & {\sum_ {\tau \in \bar {\mathcal {T}}} \lambda^ {| \tau |} Y _ {t} ^ {\tau} = \sum_ {\tau \in \bar {\mathcal {T}}} \lambda^ {| \tau |} P _ {t} Y _ {0} ^ {\tau} + \int_ {0} ^ {t} P _ {t - s} \Big (\Big (\sum_ {\tau \in \bar {\mathcal {T}}} \lambda^ {| \tau |} Y _ {s} ^ {\tau} \Big) ^ {2} - \bar {\mathcal {R}} ^ {\star} (\Psi) _ {s} \Big) d s} \\ & {\qquad + \int_ {0} ^ {t} P _ {t - s} H _ {s} d s.} \end{array}
$$

We can now “undo” the construction and recover a fixed point equation for h. Since the fixed point map for u was built precisely in such a way that h solves the KPZ equation, provided that the$Y ^ { \tau }$solve their constituent equations and that the rough integral is replaced by a usual Riemann integral, we recover the KPZ equation, except for the two correction terms involving H and G, thus yielding (2.26).

## 2.4 A new homogenisation result

To conclude this section, we present a new periodic homogenisation result for the heat equation with a strong time-varying potential, which illustrates the power of the techniques presented in this article. This equation has been studied extensively recently and several homogenisation results have been obtained for both the stochastic and the deterministic case [Bal10, Bal11, PP12], see also the monograph [CM94].

In this section, we show how to obtain a periodic homogenisation result in the situation where, in (1.1), the driving noise ξ is replaced by a space-time periodic function that is rescaled with the same exponents as space-time white noise. More precisely, we fix a periodic function$\varphi \colon S ^ { 1 } \  \ \mathbf { R }$with$\textstyle \int \varphi ( x ) d x \ = \ 0$and we consider the equation

$$
\partial_ {t} h ^ {(n)} = \partial_ {x} ^ {2} h ^ {(n)} + (\partial_ {x} h ^ {(n)}) ^ {2} + n ^ {3 / 2} \varphi (n x + c n ^ {2} t) - C _ {n},\tag{2.28}
$$

for n large, where$C _ { n }$a sequence of constants to be determined so that the solutions to (2.28) converge to a non-trivial limit. Of course, as in (1.3), this is equivalent to solving the heat equation with the potential$n ^ { 3 / 2 } \varphi ( n x + c n ^ { 2 } t )$

Similarly to what we did before, we write$\begin{array} { r } { C _ { n } = \sum _ { \tau \in \bar { T } } C _ { n } ^ { \tau } } \end{array}$and we define$Y _ { n } ^ { \tau }$ as the stationary (modulo constant Fourier mode) solutions to

$$
\partial_ {t} Y _ {n} ^ {\tau} = \partial_ {x} ^ {2} Y _ {n} ^ {\tau} + \partial_ {x} Y _ {n} ^ {\tau_ {1}} \partial_ {x} Y _ {n} ^ {\tau_ {2}} - C _ {n} ^ {\tau},\tag{2.29}
$$

where we want to specify the constants$C _ { n } ^ { \tau }$in such a way that the resulting expressions all converge to finite limits. It turns out to be straightforward to solve these equations in the following way. Set$\gamma _ { \bullet } = { \frac { 1 } { 2 } }$and then define recursively a family of exponents$\gamma _ { \tau }$by

$$
\gamma_ {[ \tau_ {1}, \tau_ {2} ]} = \gamma_ {\tau_ {1}} + \gamma_ {\tau_ {2}}.
$$

With this notation, we then make the ansatz

$$
Y _ {n} ^ {\tau} (t, x) = n ^ {- \gamma_ {\tau}} \varphi^ {\tau} (n x + c n ^ {2} t) + n ^ {2 - \gamma_ {\tau}} K ^ {\tau} t - C _ {n} ^ {\tau} t,\tag{2.30}
$$

for some periodic centred functions$\varphi ^ { \tau }$and constants$K ^ { \tau }$. We furthermore introduce the operator$G = ( c - \partial _ { x } ) ^ { - 1 }$, where c is as in (2.28). With this ansatz, we then immediately obtain the identity

$$
\varphi^ {\bullet} = G \partial_ {x} \varphi .
$$

Further inserting (2.30) into (2.29), we obtain for the remaining functions$\varphi ^ { \tau }$and constants$K ^ { \tau }$the recursion relations

$$
\partial_ {x} \varphi^ {[ \tau_ {1}, \tau_ {2} ]} = G \Pi_ {0} ^ {\perp} (\partial_ {x} \varphi^ {\tau_ {1}} \partial_ {x} \varphi^ {\tau_ {1}}), \qquad K ^ {[ \tau_ {1}, \tau_ {2} ]} = \Pi_ {0} (\partial_ {x} \varphi^ {\tau_ {1}} \partial_ {x} \varphi^ {\tau_ {1}}).
$$

It is now very easy to apply the results exposed in this section to obtain the following homogenisation result:

Theorem 2.12 With the same notations as above, set$\boldsymbol { C } _ { n } = n \boldsymbol { K } ^ { \vee } + 2 n ^ { 1 / 2 } \boldsymbol { K } ^ { \vee }$. Then, for every Holder continuous initial condition¨$h _ { 0 }$, the solution to (2.28) converges locally uniformly as n → ∞ to the solution h to

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + (\partial_ {x} h) ^ {2} + 4 \bar {K} \partial_ {x} h + K ^ {\mathbb {V}} + 4 K ^ {\mathbb {V}},
$$

where the constant K<sup>¯</sup> is given by$\bar { \cal K } = \Pi _ { 0 } ( \partial _ { x } \varphi ^ { \bullet } { \cal G } \partial _ { x } \varphi ^ { \bullet } )$. Iffurthermore$\varphi$is non-constant, then$\bar { K } \neq 0 i f$and only$i f c \ne 0$

Proof. The claim follows immediately from Theorem 2.11, as well as the continuity of$S _ { \mathrm { R } }$established in Proposition 1.5, provided that we can show that

$$
(\{Y _ {n} ^ {\tau} \} _ {\tau \in \bar {\mathcal {T}}}, \mathbf {Y} _ {n}, R _ {n} ^ {\aleph}) \to (\{Y ^ {\tau} \} _ {\tau \in \bar {\mathcal {T}}}, \mathbf {Y}, R ^ {\aleph}),
$$

in$x ,$, where$Y ^ { \bullet } = Y ^ { \vee } = Y ^ { \vee } = 0 , Y ^ { \vee } = K ^ { \vee } , Y ^ { \vee } = K ^ { \vee } , \mathbf { Y } _ { t } ( x , y ) = \bar { K } ( y - x ) .$ and$R ^ { \aleph } = 0$. By choosing$C _ { n } ^ { \vee } = n K ^ { \vee }$and$\vec { C } _ { n } ^ { \forall } = n ^ { 1 / 2 } K ^ { \vee }$, the convergence of the processes$Y ^ { \tau }$to the correct constants follows immediately from (2.30). Note that the scaling is precisely such that the convergence does indeed take place in$\mathcal { X } _ { \tau }$for each of the$Y _ { n } ^ { \tau } ,$, but it would not take place in any stronger Holder-type norm. The¨ reason why$K ^ { \check { \gamma } }$appears with a prefactor 2 in the statement of the theorem is that there are two trees isometric to$\gamma$in$\tau$

It remains to consider${ \bf Y } _ { n }$and$R _ { n } ^ { \aleph }$, which are both related to the process$\Phi _ { n }$ given as in (2.14). A straightforward calculation shows that

$$
\Phi_ {n} (t) = n ^ {- 1 / 2} \bar {\varphi} (n x + c n ^ {2} t), \quad \bar {\varphi} = G \partial_ {x} \varphi^ {\bullet}.
$$

Let now$\psi = \bar { \varphi } \partial _ { x } \varphi ^ { \bullet }$so that, at time$t = 0$, one has

$$
\begin{array}{c} \mathbf {Y} _ {n} (x, y) = \int_ {x} ^ {y} \psi (n z) d z - \frac {\bar {\varphi} (n x)}{n} (\varphi^ {\bullet} (n y) - \varphi^ {\bullet} (n x)) \\ = \bar {K} (y - x) + \mathcal {O} (| y - x | \wedge n ^ {- 1}). \end{array}
$$

Since the situation at time$t \neq 0$is the same, modulo a spatial translation, it shows that${ \bf Y } _ { n }$does indeed converge to Y in$\mathcal { C } ( \mathbf { R } , \mathcal { C } _ { 2 } ^ { 3 / 4 } )$. A similar calculation shows that $R _ { n } ^ { \ast } ( x , y ) = \mathcal { O } ( | y - x | \wedge n ^ { - 1 } )$, so that it does indeed converge to 0 in the same space.

For the last statement, an explicit calculation yields the identity

$$
\bar {K} = \sum_ {k \in {\bf Z}} \frac {c k ^ {2}}{(c ^ {2} + k ^ {2}) ^ {2}} | \varphi_ {k} | ^ {2},
$$

from which the claim follows at once.

## 3 Elements of rough path theory

In this section, we give a very short introduction to some of the elements of rough path theory needed for this work. For more details, see the original article [Lyo98] and the monographs [LQ02, LCL07, FV10b] or, for a simplified exposition covering most of the notions required for this work, see [Hai11]. We will mostly make use of the notations and terminology introduced by Gubinelli in [Gub04] since the estimates given in that work seem to be the ones that are most suitable for the present undertaking.

We denote by$\mathcal { C } _ { 2 } ( S ^ { 1 } , { \bf R } ^ { n } )$the space of continuous functions from${ \bf R } ^ { 2 }$into$\mathbf { R } ^ { n }$ that vanish on the diagonal and such that, for$f \in { \mathcal { C } } _ { 2 } ( S ^ { 1 } , \mathbf { R } ^ { n } )$, there exists$c \in \mathbf { R } ^ { n }$ such that the relations

$$
f (x + 2 \pi , y + 2 \pi) = f (x, y), \quad f (x, y + 2 \pi) = f (x, y) + c,
$$

hold for every$x , y \in \mathbf { R } ^ { n }$. We will often make an abuse of notation and write $f ( x , y )$for$x , y \in S ^ { 1 }$. Our convention in this case is that we take for x the unique representative in [0, 2π) for y the unique representative in$[ x , x + 2 \pi )$. The same convention is enforced whenever we write$\textstyle \int _ { x } ^ { y }$for$x , y \in S ^ { 1 }$

Usually, we will omit the base space$S ^ { 1 }$and the target space$\mathbf { R } ^ { n }$in our notations for the sake of simplicity. We also define a difference operator$\delta \colon { \mathcal { C } } \to { \mathcal { C } } _ { 2 }$by

$$
\delta X (x, y) = X (y) - X (x).
$$

A rough path on$S ^ { 1 }$then consists of two parts: a continuous function$X \in$ ${ \mathcal { C } } ( S ^ { 1 } , \mathbf { R } ^ { n } )$, as well as a continuous “area process$" \mathbf { X } \in \mathcal { C } _ { 2 } ( S ^ { 1 } , \mathbf { R } ^ { n \times n } )$such that the algebraic relations

$$
\mathbf {X} ^ {i j} (x, z) - \mathbf {X} ^ {i j} (x, y) - \mathbf {X} ^ {i j} (y, z) = \delta X ^ {i} (x, y) \delta X ^ {j} (y, z),\tag{3.1}
$$

hold for every triple of points$( x , y , z )$and every pair of indices$( i , j )$. One should think of X as postulating the value of the quantity

$$
\int_ {x} ^ {y} \delta X ^ {i} (x, z) d X ^ {j} (z) \stackrel {\mathrm{def}} {=} \mathbf {X} ^ {i j} (x, y),\tag{3.2}
$$

where we take the right hand side as a definition for the left hand side. (And not the other way around!) The aim of imposing (3.1) is to ensure that (3.2) does indeed behave like an integral when considering it over two adjacent intervals.

Remark 3.1 We see from (3.2) why X can not in general be a continuous function on$S ^ { 1 } \times S ^ { 1 }$, since there is no a priori reason to impose that$\begin{array} { r l } { \int _ { S ^ { 1 } } \delta X ^ { i } ( x , z ) d X ^ { j } ( z ) = } \end{array}$ 0.

Another important notion taken from [Gub04] is that of a path Y controlled by a rough path X. Given a rough path X, we say that a pair of functions$( Y , Y ^ { \prime } )$is a rough path controlled by X if the “remainder term” R given by

$$
R (x, y) \stackrel {\mathrm{def}} {=} \delta Y (x, y) - Y ^ {\prime} (x) \delta X (x, y),\tag{3.3}
$$

has better regularity properties than Y. Typically, we will assume that$\| Y \| _ { \alpha } < \infty$ and$\| Y ^ { \prime } \| _ { \alpha } <$∞ for some Holder exponent¨ α, but that$\| R \| _ { \beta } < \infty$for some$\beta > \alpha$ Here,$R _ { s , t } \in \mathbf { R } ^ { m }$and the second term is a matrix-vector multiplication.

Note that, a priori, there could be many distinct “derivative processes” Y<sup>0</sup> associated to a given path$Y$. However, if X is a typical sample path of Brownian motion and if we impose the bound$\| R \| _ { \beta } < \infty$for some$\begin{array} { r } { \beta > \frac { 1 } { 2 } } \end{array}$, then it was shown in [HP11] that there can be at most one derivative process$Y ^ { \prime }$associated to every$Y$

## 3.1 Integration of controlled rough paths.

It turns out that if (X, X) is a rough path taking values in$\mathbf { R } ^ { n }$and$Y$is a path controlled by X that also takes values in$\mathbf { R } ^ { n }$, then one can give a natural meaning to the expression$\textstyle \int \langle Y _ { t } , d X _ { t } \rangle$, provided that X and$Y$are sufficiently regular. The approximation$Y _ { t } \approx Y _ { s } + Y _ { s } ^ { \prime } \delta X _ { s , t }$suggested by (3.3) shows that it is reasonable to define the integral as the following limit of “second-order Riemann sums”:

$$
\int \left\langle Y (x), d X (x) \right\rangle = \lim _ {| \mathcal {P} | \rightarrow 0} \sum_ {[ x, y ] \in \mathcal {P}} \left(\left\langle Y (x), \delta X (x, y) \right\rangle + \operatorname{tr} Y ^ {\prime} (x) \mathbf {X} (x, y)\right),\tag{3.4}
$$

where$\mathcal { P }$denotes a partition of the integration interval, and$| \mathcal { P } |$is the length of its longest element.

With these notations at hand, we quote the following result, which is a slight reformulation of [Gub04, Prop 1]:

Theorem 3.2 Let$( X , \mathbf { X } )$satisfy (3.1) and let$( Y , Y ^ { \prime } )$be a rough path controlled by X with a remainder R given by (3.3). Assumefurthermore that

$$
\| X \| _ {\alpha} + \| \mathbf {X} \| _ {\beta} + \| Y ^ {\prime} \| _ {\bar {\alpha}} + \| R \| _ {\bar {\beta}} <   \infty ,\tag{3.5}
$$

for some exponents$\alpha , \bar { \alpha } , \beta , \bar { \beta } > 0 .$. Then, provided that$\alpha + \bar { \beta } > 1$and$\bar { \alpha } + \beta > 1$ the compensated Riemann sum in$_ { ( 3 . 4 ) }$converges. Furthermore, one has the bound

$$
\left| \int_ {x} ^ {y} \langle \delta Y (x, z), d X (z) \rangle - \operatorname{tr} Y ^ {\prime} (x) \mathbf {X} (x, y) \right| \lesssim | y - x | ^ {\gamma} \left(\| X \| _ {\alpha} \| R \| _ {\bar {\beta}} + \| \mathbf {X} \| _ {\beta} \| Y ^ {\prime} \| _ {\bar {\alpha}}\right)\tag{3.6}
$$

with$\gamma = ( \alpha + \bar { \beta } ) \wedge ( \bar { \alpha } + \beta )$,for some proportionality constant depending only on the dimensions ofthe quantities involved and the values ofthe exponents.

Actually, one has an even stronger statement. Let$\begin{array} { r } { \mathcal { C } ^ { \alpha , \beta } = \mathcal { C } ^ { \alpha } \oplus \mathcal { C } _ { 2 } ^ { \beta } } \end{array}$be the space of integrators (X, X) and let Y be the closed subset of$\mathcal { C } ^ { \alpha , \beta } \oplus \mathcal { C } ^ { { \bar { \alpha } } , { \bar { \beta } } }$(with elements of$\mathcal { V }$written as$( X , { \bf X } , Y ^ { \prime } , R ) )$defined by the algebraic relations (3.1) and (3.3), where (3.3) is interpreted as stating that there exists a function of one variable Y such that (3.3) holds for all pairs (x, y). Let furthermore$\mathcal { V } _ { g } \subset \mathcal { V }$be the set defined by the additional constraint

$$
\mathbf {X} ^ {i j} (x, y) + \mathbf {X} ^ {j i} (x, y) = \delta X ^ {i} (x, y) \delta X ^ {j} (x, y).\tag{3.7}
$$

(Note that this constraint is automatically satisfied if X is given by the left hand side of (3.2) for some smooth X.) Then, one has:

Proposition 3.3 The set$\mathcal { \textrm { y } } _ { g }$is dense in Y. Furthermore, provided that$\bar { \alpha } \leq \alpha .$ $\bar { \beta } \leq \beta _ { : }$, and$( \alpha + \bar { \beta } ) \wedge ( \bar { \alpha } + \beta ) > 1$, the map

$$
\mathcal {I} \colon (X, \mathbf {X}, Y, Y ^ {\prime}) \mapsto \left(X, \mathbf {X}, \int_ {0} ^ {\cdot} \langle \delta Y (0, z), d X (z) \rangle , \delta Y (0, \cdot)\right),\tag{3.8}
$$

defined on smooth elements of$\mathfrak { V } _ { g } .$, extends uniquely to the continuous map$\hat { \mathcal { I } } { : \mathcal { V } _ { g }  }$ $\mathcal { { V } } _ { g }$obtained by replacing the Riemann integral by R in the above expression.

Furthermore,$\hat { \mathcal { I } }$is uniformly Lipschitz continuous on bounded sets$o f { \mathcal { Y } } _ { g }$under the natural norm

$$
\| X, \mathbf {X}, Y ^ {\prime}, R ^ {Y} \| = \| Y ^ {\prime} \| _ {\bar {\alpha}} + \| R ^ {Y} \| _ {\bar {\beta}} + \| X \| _ {\alpha} + \| \mathbf {X} \| _ {\beta},
$$

and it is given by replacing R by$f$in (3.8).

Proof. The density of$\mathcal { Y } _ { g }$in$\mathcal { V }$was shown for example in [FV06]. For the uniform Lipschitz continuity of I<sup>ˆ</sup> on bounded sets, it suffices to retrace the proof of [Gub04, Theorem 1]. Since$\mathcal { { D } } _ { g }$is dense in$\mathcal { V } ,$, the uniqueness of the extension follows.

Note that this is not a corollary of Theorem 3.2. Indeed, the bound (3.6) only holds on the nonlinear space Y so that it is not possible to simply exploit the bilinearity of the integral, even though the bound obtained in [Gub04] shows that it behaves “as$\mathrm { i f } ^ { \dag }$the bound (3.6) was valid on all of$\mathcal { C } ^ { \alpha , \beta } \oplus \mathcal { C } ^ { { \bar { \alpha } } , { \bar { \beta } } }$□

Remark 3.4 We made a slight abuse of notation in (3.8) in order to improve the legibility of the expressions, by identifying on both sides of the equation elements $( X , \mathbf { X } , Y ^ { \prime } , R )$with the corresponding element$( X , \mathbf { X } , Y , Y ^ { \prime } )$, where$Y$is the (unique up to constants) function such that (3.3) holds. We also slightly jumbled the dimensions of the spaces (if X is n-dimensional then$Y$should also be so, but the integral is only one-dimensional), but the meaning should be obvious.

Remark 3.5 The bound (3.6) does behave in a very natural way under dilatations. Indeed, the integral is invariant under the transformation

$$
(Y, X, \mathbf {X}) \mapsto (\lambda^ {- 1} Y, \lambda X, \lambda^ {2} \mathbf {X}).\tag{3.9}
$$

The same is true for right hand side of (3.6), since under this dilatation, we also have$( Y ^ { \prime } , R ) \mapsto ( \lambda ^ { - 2 } Y ^ { \prime } , \lambda ^ { - 1 } R )$

Remark 3.6 It is straightforward to check that, if$( Y , Y ^ { \prime } )$is a rough path controlled by X, then so is$( f Y , f Y ^ { \prime } )$, for any smooth function f. As a consequence,$\operatorname { i f } \left( X , \mathbf { X } \right)$ and$( Y , Y ^ { \prime } )$satisfy the bounds (3.5), then Theorem 3.2 allows to make sense of the product$Y ( x ) { \frac { d X } { d x } }$as a distribution, even in situations when$\alpha < \textstyle { \frac { 1 } { 2 } }$, where such a product would not be well-defined in the classical sense.

Remark 3.7 One could argue that it would have been natural to impose the condition (3.7) from the beginning. The reasons for not doing so are that the integral$f$is well-defined without it and that non-geometric situations can arise naturally in the context of numerical approximations, see for example [HM10, HMW12].

It is clear from the definition (3.4) that if X is smooth and X is given by (3.2) (reading the definition from right to left), then$f$coincides with the usual Riemann integral. It is therefore instructive to see what happens if X is a smooth function but one sets

$$
\mathbf {X} ^ {i j} (x, y) = \int_ {x} ^ {y} \delta X ^ {i} (x, z) d X ^ {j} (z) + \int_ {x} ^ {y} F ^ {i j} (z) d z,
$$

for some continuous function F. It is then clear that (3.1) is still satisfied and that $\| \mathbf { X } \| _ { \beta } < \infty$provided that$\beta \leq 1$. Even the additional “geometric” constraint (3.7) is satisfied if$F$is antisymmetric. Given a smooth function$Y$, we can then choose for$Y ^ { \prime }$an arbitrary smooth function and the remainder term R given by (3.3) will still satisfy$\| R \| _ { \bar { \beta } } < \infty$for$\bar { \beta } \leq 1$. It is now straightforward to verify that the rough integral is well-posed and equals

$$
\int_ {x} ^ {y} \left\langle Y (z) d X (z) \right\rangle = \int_ {x} ^ {y} \left\langle Y (z), \frac {d X}{d z} (z) \right\rangle d z + \int_ {x} ^ {y} \operatorname{tr} Y ^ {\prime} (z) F (z) d z,\tag{3.10}
$$

where the right hand side is a usual Riemann integral. See for example the original article [Lyo98, Example 1.1.1] for a more detailed explanation on how to interpret this apparent discrepancy.

## 3.2 Heat kernel bounds

In this section, we obtain a number of sharp bounds on the interplay between the heat kernel on$S ^ { 1 }$and rough path valued functions. The reader who is interested in getting quickly to the heart of the matter can easily skip the proofs of these results, since they are not particularly formative and mostly consist of relatively straightforward estimates. However, Proposition 3.8 is one of the most important ingredients of the next section, so we prefer not to relegate these bounds to a mere appendix. Several of these bounds are close in spirit to those obtained in [HW10, Hai11], but both the norms employed here and the precise form of the bounds required for our arguments are quite different.

The following quantity will be very often used in the sequel, so we give it a name. Given a path$Y$controlled by a rough path$( X , \mathbf { X } )$and given$\kappa > 0$, we define the quantity

$$
\mathcal {K} ^ {\kappa} (Y, X) \stackrel {{\mathrm{def}}} {{=}} \| Y \| _ {\frac {1}{2} - \kappa} \| X \| _ {\frac {1}{2} - \kappa} + \| \mathbf {X} \| _ {1 - 2 \kappa} \| Y ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}} + \| R ^ {Y} \| _ {\frac {1}{2} + 2 \kappa} \| X \| _ {\frac {1}{2} - \kappa}.
$$

We also define, for${ \mathcal { C } } ^ { 1 }$functions$f \colon \mathbf { R }  \mathbf { R }$, the norm

$$
\| f \| := \sum_ {n \in \mathbf {Z}} \sqrt {1 + | n |} \sup _ {0 \leq t \leq 1} \left(| f (n + t) | + | f ^ {\prime} (n + t) |\right) <   \infty .\tag{3.11}
$$

We then have the following bound, which can be viewed as a refinement of [Hai11, Prop. 2.5]:

Proposition 3.8 Let$f \in \mathcal { C } ^ { 1 } ( \mathbf { R } , \mathbf { R } )$be such that$\| f \| < \infty ,$, let$\lambda \geq 1$, and let $\kappa \in ( 0 , \frac { 1 } { 2 } )$. Then, the bound

$$
\Big | \int_ {S ^ {1}} f (\lambda x) Y (x) d X (x) \Big | \lesssim \lambda^ {\kappa - \frac {1}{2}} | Y (0) | \| X \| _ {\frac {1}{2} - \kappa} + \lambda^ {2 \kappa - 1} \mathcal {K} ^ {\kappa} (Y, X),
$$

holds uniformly for all$\lambda > 1$, with a proportionality constant depending only on $\| f \| .$

Remark 3.9 One very important feature of this bound is that the first term on the right hand side only depends on$\left| Y ( 0 ) \right|$and not on$\| Y \| _ { \infty }$as in [Hai11]. This is achieved thanks to the control provided by the norm$\| \cdot \|$, which ensures that$f$ decays sufficiently fast at infinity. One place where this plays a crucial role is the proof of Corollary 3.13 below.

Proof. We use the same technique of proof as in [Hai11, Prop. 2.5], but we are more careful with our bounds and exploit the knowledge from (3.11) that f decays relatively fast at infinity. To shorten our notations, we set$Y _ { f } ( x ) = f ( \lambda x ) Y ( x )$and $Y _ { f } ^ { \prime } ( x ) = f ( \lambda x ) Y ^ { \prime } ( x )$, and we also set

$$
a _ {k} = \sup _ {0 \leq t \leq 1} \left(| f (k + t) | + | f ^ {\prime} (k + t) |\right).
$$

Setting$N = \lfloor 2 \pi \lambda \rfloor , \delta x = 2 \pi / N$and writing$x _ { k } = k \delta x .$, we have

$$
\left| \int_ {S ^ {1}} f (\lambda x) Y (x) d X (x) \right| \leq \sum_ {k = 0} ^ {N - 1} \left| \int_ {x _ {k}} ^ {x _ {k + 1}} Y _ {f} (x) d X (x) \right| \stackrel {\text { def }} {=} \sum_ {k = 0} ^ {N - 1} T _ {k}.
$$

Note furthermore that, for$x \in [ x _ { k } , x _ { k + 1 } ]$, one has$\lambda x \in [ k , k + 2 ]$so that, for every $\alpha \in ( 0 , 1 ]$, one has the bounds

$$
\| Y _ {f} \| _ {\alpha , k} \lesssim (a _ {k} + a _ {k + 1}) \big (\| Y \| _ {\alpha} + \lambda^ {\alpha} \| Y \| _ {\infty} \big),\tag{3.12a}
$$

$$
\| Y _ {f} ^ {\prime} \| _ {\alpha , k} \lesssim (a _ {k} + a _ {k + 1}) \big (\| Y ^ {\prime} \| _ {\alpha} + \lambda^ {\alpha} \| Y ^ {\prime} \| _ {\infty} \big),\tag{3.12b}
$$

$$
\| R ^ {Y _ {f}} \| _ {\alpha , k} \lesssim (a _ {k} + a _ {k + 1}) \big (\| R ^ {Y} \| _ {\alpha} + \lambda^ {\alpha} \| Y \| _ {\infty} \big),\tag{3.12c}
$$

where we denoted by$\| \cdot \| _ { \alpha , k }$the corresponding Holder seminorm restricted to the¨ interval$[ x _ { k } , x _ { k + 1 } ]$

It then follows from Theorem 3.2 that

$$
T _ {k} = f (\lambda x _ {k}) Y (x _ {k}) \delta X _ {k} + f (\lambda x _ {k}) Y ^ {\prime} (x _ {k}) \mathbf {X} _ {k} + R _ {k},\tag{3.13}
$$

where the remainder term$R _ { k }$is bounded by

$$
| R _ {k} | \lesssim \lambda^ {- \kappa - 1} (\| Y _ {f} ^ {\prime} \| _ {3 \kappa , k} \| \mathbf {X} \| _ {1 - 2 \kappa} + \| R ^ {Y _ {f}} \| _ {\frac {1}{2} + 2 \kappa , k} \| X \| _ {\frac {1}{2} - \kappa}).\tag{3.14}
$$

At this point, we note that the supremum norm of$Y$over the interval$[ x _ { k } , x _ { k + 1 } ]$is bounded by

$$
\left\| Y \right\| _ {\infty , k} \lesssim | Y (0) | + \left\| Y \right\| _ {\alpha} \lambda^ {- \alpha} (1 + | k |) ^ {\alpha},\tag{3.15}
$$

for any$\alpha \in ( 0 , 1 ]$. Using this identity with$\begin{array} { r } { \alpha = \frac { 1 } { 2 } - \kappa } \end{array}$and the fact that$( 1 + | \boldsymbol { k } | ) ^ { 1 / 2 } a _ { \boldsymbol { k } }$ is summable by assumption, we can combine (3.14) with (3.12), so that

$$
\sum_ {k = 0} ^ {N - 1} | R _ {k} | \lesssim \lambda^ {\kappa - \frac {1}{2}} | Y (0) | \| X \| _ {\frac {1}{2} - \kappa} + \lambda^ {2 \kappa - 1} (\| Y ^ {\prime} \| _ {\infty} \| \mathbf {X} \| _ {1 - 2 \kappa} + \| Y \| _ {\frac {1}{2} - \kappa} \| X \| _ {\frac {1}{2} - \kappa})
$$

$$
+ \lambda^ {- \kappa - 1} (\| \mathbf {X} \| _ {1 - 2 \kappa} \| Y ^ {\prime} \| _ {3 \kappa} + \| R ^ {Y} \| _ {\frac {1}{2} + 2 \kappa} \| X \| _ {\frac {1}{2} - \kappa}),
$$

which is actually slightly better than the desired bound. In order to conclude, it remains to bound the other two terms appearing in the right hand side of (3.13). To do so, we use again (3.15) to obtain

$$
\begin{array}{r l} & {| f (\lambda x _ {k}) Y (x _ {k}) \delta X _ {k} + f (\lambda x _ {k}) Y ^ {\prime} (x _ {k}) \mathbf {X} _ {k} | \lesssim (a _ {k} + a _ {k + 1}) \lambda^ {\kappa - \frac {1}{2}} | Y (0) | \| X \| _ {\frac {1}{2} - \kappa}} \\ & {\qquad + (a _ {k} + a _ {k + 1}) \lambda^ {2 \kappa - 1} (| k | ^ {\frac {1}{2} - \kappa} \| Y \| _ {\frac {1}{2} - \kappa} \| X \| _ {\frac {1}{2} - \kappa} + \| Y ^ {\prime} \| _ {\infty} \| \mathbf {X} \| _ {1 - 2 \kappa}),} \end{array}
$$

and the claim follows at once.

Remark 3.10 We think of κ as being a small parameter. As a consequence, this bound is especially strong in the case$Y ( 0 ) = 0$(or small), which will play a crucial role in the sequel.

Corollary 3.11 Let$p _ { t }$denote the heat kernel on$S ^ { 1 }$and let$p _ { t } ^ { ( k ) }$be its kth (spatial) derivative. Then, the bound

$$
\left| \int_ {S ^ {1}} p _ {t} ^ {(k)} (x - y) d X (y) \right| \lesssim t ^ {- \frac {1}{4} - \frac {k + \kappa}{2}} \| X \| _ {\frac {1}{2} - \kappa},
$$

holds uniformly over all$x .$

Proof. Setting$Y ( x ) = 1$, this is an immediate consequence of Proposition 3.8, using the fact that there exist functions$f _ { t }$such that, for every$k \geq 0 , \| f _ { t } ^ { ( k ) } \|$is uniformly bounded for$t \in ( 0 , 1 ]$, and such that

$$
p _ {t} ^ {(k)} (x) = t ^ {- \frac {1 + k}{2}} f _ {t} ^ {k} (t ^ {- 1 / 2} x).
$$

The claim then follows by setting$\lambda = t ^ { - 1 / 2 }$

Corollary 3.12 Let$p _ { t }$denote the heat kernel on$S ^ { 1 }$and let$p _ { t } ^ { ( k ) }$be its kth (spatial) derivative. Then, the bound

$$
\Big | \int_ {S ^ {1}} p _ {t} ^ {(k)} (z - y) Y (y) d X (y) \Big | \lesssim t ^ {- \frac {1}{4} - \frac {k + \kappa}{2}} | Y (z) | \| X \| _ {\frac {1}{2} - \kappa} + t ^ {- \frac {k}{2} - \kappa} \mathcal {K} ^ {\kappa} (Y, X),
$$

holds uniformly over all$z .$

Proof. This follows from Proposition 3.8 and the scaling properties of the heat kernel in the same way as Corollary 3.11. It furthermore suffices to translate the origin to$y = z$□

Corollary 3.13 Let$p _ { t }$denote the heat kernel on$S ^ { 1 }$and let$p _ { t } ^ { ( k ) }$be its kth (spatial) derivative. Then, the bound

$$
\begin{array}{c} \Big | \int_ {S ^ {1}} p _ {t} ^ {(k)} (z - y) \bigl (Y (y) - Y (x) \bigr) d X (y) \Big | \lesssim t ^ {- \frac {1}{4} - \frac {k + \kappa}{2}} | z - x | ^ {\frac {1}{2} - \kappa} \| Y \| _ {\frac {1}{2} - \kappa} \| X \| _ {\frac {1}{2} - \kappa} \\ + t ^ {- \frac {k}{2} - \kappa} \mathcal {H} ^ {\kappa} (Y, X), \end{array}
$$

holds uniformly over all x and$z .$

Proof. This is a particular case of Corollary 3.12, using the fact that$| Y ( z ) - Y ( x ) | \leq$ $| z - x | ^ { \frac { 1 } { 2 } - \kappa } \| Y \| _ { \kappa - \frac { 1 } { 2 } }$□

Actually, a similar bound also holds if we replace$p _ { t } ^ { ( k ) }$by a kind of “fractional derivative” as follows:

Proposition 3.14 Let$p _ { t }$denote the heat kernel on$S ^ { 1 }$, let$p _ { t } ^ { ( k ) }$be its kth (spatial) derivative, let$\kappa \in ( 0 , \frac { 1 } { 2 } )$, and let$\alpha \in [ \frac { 1 } { 2 } - \kappa , 1 ]$. Then, the bound

$$
\begin{array}{r l} & {\Big | \int_ {S ^ {1}} \frac {p _ {t} ^ {(k)} (z - y) - p _ {t} ^ {(k)} (z ^ {\prime} - y)}{| z - z ^ {\prime} | ^ {\alpha}} \big (Y (y) - Y (x) \big) d X (y) \Big |} \\ & {\qquad \lesssim t ^ {- \kappa - \frac {k + \alpha}{2}} \| Y \| _ {\frac {1}{2} - \kappa} \| X \| _ {\frac {1}{2} - \kappa} + t ^ {- \kappa - \frac {k + \alpha}{2}} \mathcal {K} ^ {\kappa} (Y, X),} \end{array}\tag{3.16}
$$

holds uniformly over all$z , z ^ { \prime }$and$x ,$such that$| x - z | \vee | x - z ^ { \prime } | \leq | z - z ^ { \prime } | .$, and over all$t \leq 1$

Proof. Denote the first term on the right hand side of (3.16) by$T _ { 1 }$and the second term by$T _ { 2 }$. As a shorthand, we also write

$$
\mathcal {I} \stackrel {\mathrm{def}} {=} \int_ {S ^ {1}} (p _ {t} ^ {(k)} (z - y) - p _ {t} ^ {(k)} (z ^ {\prime} - y)) (Y (y) - Y (x)) d X (y),
$$

so that we aim to show that

$$
| \mathcal {I} | \lesssim | z - z ^ {\prime} | ^ {\alpha} (T _ {1} + T _ {2}).\tag{3.17}
$$

With these notations, it follows immediately from Corollary 3.13 that

$$
| \mathcal {I} | \lesssim t ^ {\frac {\alpha + \kappa}{2} - \frac {1}{4}} | z - z ^ {\prime} | ^ {\frac {1}{2} - \kappa} T _ {1} + t ^ {\frac {\alpha}{2}} T _ {2}.\tag{3.18}
$$

This shows that (3.17) holds on the set$\{ | t | \le | z - z ^ { \prime } | ^ { 2 } \}$. On the other hand, we can write

$$
\mathcal {I} = \int_ {z} ^ {z ^ {\prime}} \oint_ {S ^ {1}} p _ {t} ^ {(k + 1)} (z ^ {\prime \prime} - y) \bigl (Y (y) - Y (x) \bigr) d X (y) d z ^ {\prime \prime}
$$

Applying again Corollary 3.13 (this time with$k + 1$instead of k) for the integrand and integrating over$z ^ { \prime \prime }$, we conclude that the bound

$$
| \mathcal {I} | \lesssim t ^ {\frac {\alpha + \kappa - 1}{2} - \frac {1}{4}} | z - z ^ {\prime} | ^ {\frac {3}{2} - \kappa} T _ {1} + t ^ {\frac {\alpha - 1}{2}} | z - z ^ {\prime} | T _ {2},\tag{3.19}
$$

holds. This in turn shows that (3.17) holds on the set$\{ | t | \geq | z - z ^ { \prime } | ^ { 2 } \}$}, so that the proof is complete.□

Corollary 3.15 Let$p _ { t } ^ { ( k ) }$be as above, let$\kappa \in ( 0 , \frac 1 2 )$, and let$\alpha \in [ \frac { 1 } { 2 } - \kappa , 1 ]$. Then, the bound

$$
\begin{array}{r l} & {\Big | \int_ {S ^ {1}} \frac {p _ {t} ^ {(k)} (z - y) - p _ {t} ^ {(k)} (z ^ {\prime} - y)}{| z - z ^ {\prime} | ^ {\alpha}} Y (y) d X (y) \Big |} \\ & {\qquad \lesssim t ^ {- \frac {1}{4} - \frac {k + \alpha + \kappa}{2}} \| Y \| _ {\infty} \| X \| _ {\frac {1}{2} - \kappa} + t ^ {- \kappa - \frac {k + \alpha}{2}} \mathcal {K} ^ {\kappa} (Y, X),} \end{array}
$$

holds uniformly over all$z , z ^ { \prime } ,$, and over all$t \leq 1$

Proof. The proof is the same as that of Proposition 3.14, but using Corollary 3.12 instead of Corollary 3.13.□

Combining both results, we also obtain

Corollary 3.16 Let$p _ { t } ^ { ( k ) }$be as above, let$\kappa , \delta \in ( 0 , \frac 1 2 )$, and let$\alpha \in [ \frac { 1 } { 2 } - \kappa , 1 ]$. Then, the bound

$$
\begin{array}{c} \Big | \int_ {S ^ {1}} \frac {p _ {t} ^ {(k)} (z - y) - p _ {t} ^ {(k)} (z ^ {\prime} - y)}{| z - z ^ {\prime} | ^ {\alpha}} Y (y)   d X (y) \Big | \lesssim t ^ {- \kappa - \frac {k + \alpha}{2}} \| Y \| _ {\frac {1}{2} - \kappa} \| X \| _ {\frac {1}{2} - \kappa} \\ + t ^ {- \kappa - \frac {k + \alpha}{2}} \mathcal {K} ^ {\kappa} (Y, X) + t ^ {- \frac {1}{4} - \frac {k + \alpha + \delta}{2}} \| Y \| _ {\infty} \| X \| _ {\frac {1}{2} - \delta}, \end{array}
$$

holds uniformly over all$z , z ^ { \prime } ,$, and over all$t \leq 1$

Proof. It suffices to write$Y ( y )$as$( Y ( y ) - Y ( x ) ) + Y ( x )$for x between z and$z ^ { \prime } .$ One then applies Proposition 3.14 to the first term and Corollary 3.15 to the second term.□

## 4 Fixed point argument

With these bounds at hand, we can now set up the spaces for our fixed point argument. Our aim is to provide a rigorous meaning for local solutions to equations of the type

$$
\partial_ {t} v _ {t} = \partial_ {x} ^ {2} v _ {t} + \partial_ {x} (G (v _ {t}, t) \partial_ {x} Y _ {t}) + \partial_ {x} F (v _ {t}, t),\tag{4.1}
$$

where$Y$is a fixed process taking values in$\mathcal { C } ^ { \frac { 1 } { 2 } - \overline { { \kappa } } }$for some$\bar { \kappa } > 0 \AA$, and$F$and$G$are sufficiently “nice” nonlinearities. The precise conditions on$F$and G will be spelled out in Section 4.3 below. For the moment, a typical example to keep in mind is

$$
G (v _ {t}, t) = v _ {t} + w _ {t}, \qquad F (v _ {t}, t) = v _ {t} ^ {2} + \bar {w} _ {t},\tag{4.2}
$$

for some fixed processes w and$\bar { w }$.

In full generality, such an equation simply does not make sense in the regularity class that we are interested in. However, it turns out that it is well-posed if we are able to find a sufficiently regular “cross-area” Y between Y and$\Phi .$, where Φ is given by the centred stationary solution to

$$
\partial_ {t} \Phi_ {t} = \partial_ {x} ^ {2} \Phi_ {t} + \partial_ {x} ^ {2} Y _ {t},\tag{4.3}
$$

and if, in the example (4.2), we assume that for every fixed$t > 0 , w _ { t }$is controlled by$( \Phi _ { t } , Y _ { t } )$. Indeed, if this is the case, then we can “guess” that the solution v to (4.1) will locally “look like” Φ, so that we will search for solutions belonging to a space of paths controlled by$\Phi$.

## 4.1 Preliminary computations

In this subsection, we consider the following setting. We assume that we are given processes$Y$and$Z$taking values in$\mathcal { C } ^ { \frac { 1 } { 2 } - \overline { { \kappa } } }$for some$\bar { \kappa } > 0 .$, and we define a process Φ by setting

$$
\Phi_ {t} = P _ {t} \Phi_ {0} + \int_ {0} ^ {t} \partial_ {x} ^ {2} P _ {t - s} Y _ {s} d s.
$$

We also assume that we are given a process Y such that, for every$t > 0$and every $x , y , z \in S ^ { 1 }$，

$$
\mathbf {Y} _ {t} (x, y) + \mathbf {Y} _ {t} (y, z) - \mathbf {Y} _ {t} (x, z) = \delta Y _ {t} (x, y) \delta Z _ {t} (y, z),\tag{4.4}
$$

and such that$\mathrm { s u p } _ { t < 1 } \| \mathbf { Y } _ { t } \| _ { 1 - 2 \bar { \kappa } } < \infty$. This allows to construct a rough path-valued process$\hat { Y }$with components$\hat { Y } _ { t } = ( Y _ { t } , Z _ { t } )$, and with the antisymmetric part of its area process given by Y. (Its symmetric part is canonically given by half of the increment squared, as in (3.7).) In the sequel, we will mostly use the case where $Z _ { t } = \Phi _ { t }$for Φ given by (4.3), but this is not essential, and it will be useful in Section 7 below to have the freedom to consider different choices of Z and Y.

We assume that, for almost every$t > 0 , v _ { t }$is controlled by$Z _ { t }$. With this notation fixed, we can then define a map M by

$$
\left(\mathcal {M} v\right) _ {t} (x) = \int_ {0} ^ {t} \oint_ {S ^ {1}} p _ {t - s} ^ {\prime} (x - y)   v _ {s} (y)   d Y _ {s} (y)   d s  .
$$

Here, the inner integral is to be interpreted in the sense of Theorem 3.2. The map M will be our main building block for providing a rigorous way of interpreting (4.1) in a “mild formulation”. However, it is important to remember that, as already noted in [Hai11], the notion of solution obtained in this way does depend on the choice of Y, which is not unique.

Our aim is to show that, provided that$\hat { Y }$and v are regular enough,$( \mathcal { M } v ) _ { t }$is controlled by$\Phi _ { t }$. In the light of Corollary 3.13 and Proposition 3.14, we set as a shorthand

$$
\mathcal {K} _ {s} ^ {\kappa} \stackrel {{\text { def }}} {{=}} \mathcal {K} ^ {\kappa} (v _ {s}, \hat {Y} _ {s})  ,
$$

and we define$R _ { t } ^ { \mathcal { M } }$to be the “remainder term” given by

$$
R _ {t} ^ {\mathcal {M}} (x, y) \stackrel {\mathrm{def}} {=} (\mathcal {M} v) _ {t} (y) - (\mathcal {M} v) _ {t} (x) - v _ {t} (x) \bigl (\Phi_ {t} (y) - \Phi_ {t} (x) \bigr).
$$

With these notations at hand, we obtain the following bound as a straightforward corollary of the previous section:

Proposition 4.1 For every$\kappa \in ( 0 , \frac { 1 } { 4 } )$and every$\bar { \kappa } \in ( 0 , \frac 1 2 )$, the bound

$$
\begin{array}{r l} & {\| R _ {t} ^ {\mathcal {M}} \| _ {\frac {1}{2} + 2 \kappa} \lesssim t ^ {- \frac {3 \kappa}{2}} \| v _ {t} \| _ {\infty} \| \Phi_ {0} \| _ {\frac {1}{2} - \kappa} + \int_ {0} ^ {t} (t - s) ^ {- 1 - \kappa - \frac {\bar {\kappa}}{2}} \| Y _ {s} \| _ {\frac {1}{2} - \bar {\kappa}} \| v _ {s} - v _ {t} \| _ {\infty} d s} \\ & {\qquad + \int_ {0} ^ {t} \Big ((t - s) ^ {- \frac {3}{4} - \kappa - \bar {\kappa}} \| v _ {s} \| _ {\frac {1}{2} - \bar {\kappa}} \| Y _ {s} \| _ {\frac {1}{2} - \bar {\kappa}} + (t - s) ^ {- \frac {3}{4} - \kappa - \bar {\kappa}} \mathcal {K} _ {s} ^ {\bar {\kappa}} \Big) d s,} \end{array}
$$

holds uniformly over$t \in ( 0 , T ]$for every$T > 0$

Proof. We have the identity

$$
\begin{array}{r l} & {R _ {t} ^ {\mathcal {M}} (x, y) = \int_ {0} ^ {t} \oint_ {S ^ {1}} (p _ {t - s} ^ {\prime} (y - z) - p _ {t - s} ^ {\prime} (x - z)) (v _ {s} (z) - v _ {t} (x)) d Y _ {s} (z) d s} \\ & {\qquad + v _ {t} (x) \big (P _ {t} \Phi_ {0} (y) - P _ {t} \Phi_ {0} (x) \big),} \end{array}
$$

where$P _ { t }$denotes the heat semigroup. Here, we have made use of the fact that$Y$ solves (4.3). We can rewrite this as

$$
R _ {t} ^ {\mathcal {M}} (x, y) = T _ {t} ^ {1} (x, y) + T _ {t} ^ {2} (x, y) + T _ {t} ^ {3} (x, y),
$$

with

$$
\begin{array}{r l} & T _ {t} ^ {1} (x, y) = \int_ {0} ^ {t} \oint_ {S ^ {1}} (p _ {t - s} ^ {\prime} (y - z) - p _ {t - s} ^ {\prime} (x - z)) (v _ {s} (z) - v _ {s} (x)) d Y _ {s} (z) d s, \\ & T _ {t} ^ {2} (x, y) = \int_ {0} ^ {t} (v _ {s} (x) - v _ {t} (x)) \oint_ {S ^ {1}} (p _ {t - s} ^ {\prime} (y - z) - p _ {t - s} ^ {\prime} (x - z)) d Y _ {s} (z) d s, \\ & T _ {t} ^ {3} (x, y) = v _ {t} (x) (P _ {t} \Phi_ {0} (y) - P _ {t} \Phi_ {0} (x)). \end{array}
$$

As a shorthand, we furthermore rewrite${ T _ { t } } ^ { i }$as

$$
T _ {t} ^ {i} (x, y) = \int_ {0} ^ {t} T _ {t, s} ^ {i} (x, y) d s, \qquad i = 1, 2.
$$

Setting$\begin{array} { r } { \alpha = \frac { 1 } { 2 } + 2 \kappa , } \end{array}$, it then follows from Proposition 3.14 that one has the inequality

$$
\| T _ {t, s} ^ {1} \| _ {\frac {1}{2} + 2 \kappa} \lesssim (t - s) ^ {- \frac {3}{4} - 2 \kappa} \| v _ {s} \| _ {\frac {1}{2} - \kappa} \| Y _ {s} \| _ {\frac {1}{2} - \kappa} + (t - s) ^ {- \frac {3}{4} - \kappa} \mathcal {K} _ {s}.\tag{4.5}
$$

On the other hand, it follows from Corollary 3.15 that

$$
\left\| T _ {t, s} ^ {2} \right\| _ {\frac {1}{2} + 2 \kappa} \lesssim (t - s) ^ {- 1 - \frac {3 \kappa}{2}} \left\| Y _ {s} \right\| _ {\frac {1}{2} - \kappa} \left\| v _ {s} - v _ {t} \right\| _ {\infty}.\tag{4.6}
$$

Finally, we have

$$
\| T _ {t} ^ {3} \| _ {\frac {1}{2} + 2 \kappa} \lesssim t ^ {- \frac {3 \kappa}{2}} \| v _ {t} \| _ {\infty} \| \Phi_ {0} \| _ {\frac {1}{2} - \kappa},\tag{4.7}
$$

as a consequence of the regularising properties of the heat equation. Collecting all of these bounds concludes the proof.□

In order to make the bound (4.6) integrable in s, we see that$\mathrm { i f }$we want to be able to set up a fixed point argument, we also need to obtain some time regularity estimates on$\mathcal { M } v$. We achieve this with the following bound:

Proposition 4.2 Let v be a smoothfunction and let$\tilde { v } \overset { d e f } { = } \mathcal { M } v$. Then, the bound

$$
\begin{array}{l} \| \tilde {v} _ {t} - \tilde {v} _ {s} \| _ {\infty} \lesssim \int_ {0} ^ {s} \int_ {s} ^ {t} ((q - r) ^ {- \frac {7}{4} - \frac {\kappa}{2}} \| v _ {r} \| _ {\infty} \| Y _ {r} \| _ {\frac {1}{2} - \kappa} + (q - r) ^ {- \frac {3}{2} - \kappa} \mathcal {K} _ {r} ^ {\kappa}) \\ \qquad + \int_ {s} ^ {t} (t - r) ^ {- \frac {3}{4} - \frac {\kappa}{2}} \| v _ {r} \| _ {\infty} \| Y _ {r} \| _ {\frac {1}{2} - \kappa} d r + \int_ {s} ^ {t} (t - r) ^ {- \frac {1}{2} - \kappa} \mathcal {K} _ {r} ^ {\kappa} d r. \end{array}\tag{4.8}
$$

holds.

Proof. In order to achieve such a bound, we write for$0 < s \leq t$

$$
\begin{array}{l} (\mathcal {M} v) _ {t} (x) - (\mathcal {M} v) _ {s} (x) = \int_ {0} ^ {s} \oint_ {S ^ {1}} (p _ {t - r} ^ {\prime} (y - z) - p _ {s - r} ^ {\prime} (y - z)) v _ {r} (z)   d Y _ {r} (z)   d r \\ \qquad + \int_ {s} ^ {t} \oint_ {S ^ {1}} p _ {t - r} ^ {\prime} (y - z) v _ {r} (z)   d Y _ {r} (z)   d r \\ \qquad = \int_ {0} ^ {s} \int_ {s} ^ {t} \oint_ {S ^ {1}} p _ {q - r} ^ {\prime \prime \prime} (y - z) v _ {r} (z)   d Y _ {r} (z)   d q   d r \\ \qquad + \int_ {s} ^ {t} \oint_ {S ^ {1}} p _ {t - r} ^ {\prime} (y - z) v _ {r} (z)   d Y _ {r} (z)   d r , \end{array}
$$

where we used the identity$\partial _ { t } p _ { t } ( x ) = p _ { t } ^ { \prime \prime } ( x )$to obtain the second identity. The claimed bound then follows in a straightforward way from Corollary 3.12.□

We can also obtain a bound on the Holder norm of¨$\mathcal { M } v$that is slightly better than the one that can be deduced from the bound on$R _ { t } ^ { \mathcal { M } }$. It follows indeed from Corollary 3.16 that, for every$\bar { \kappa } \in ( 0 , \kappa )$and every$\begin{array} { r } { \kappa < { \frac { 1 } { 2 } } } \end{array}$, one has the bound

$$
\begin{array}{r l} & {\left\| (\mathcal {M} v) _ {t} \right\| _ {\frac {1}{2} - \kappa} \lesssim \int_ {0} ^ {t} (t - s) ^ {- \frac {3}{4} - \frac {\kappa}{2}} \big (\left\| v _ {s} \right\| _ {\frac {1}{2} - \kappa} \left\| Y _ {s} \right\| _ {\frac {1}{2} - \kappa} + \mathcal {K} _ {s} ^ {\kappa} \big) d s} \\ & {\qquad + \int_ {0} ^ {t} (t - s) ^ {\frac {\kappa - \bar {\kappa}}{2} - 1} \left\| v _ {s} \right\| _ {\infty} \left\| Y _ {s} \right\| _ {\frac {1}{2} - \bar {\kappa}} d s.} \end{array}\tag{4.9}
$$

Finally, we obtain from Corollary 3.12 the following bound on the supremum norm of$\mathcal { M } v \colon$

$$
\left\| (\mathcal {M} v) _ {t} \right\| _ {\infty} \lesssim \int_ {0} ^ {t} \left((t - s) ^ {- \frac {3}{4} - \frac {\kappa}{2}} \| v _ {s} \| _ {\infty} \| Y _ {s} \| _ {\frac {1}{2} - \kappa} + (t - s) ^ {- \frac {1}{2} - \kappa} \mathscr {K} _ {s} ^ {\kappa}\right) d s.\tag{4.10}
$$

With these calculations at hand, we are now ready to build a norm in which we can solve (4.1) by a standard Banach fixed point argument.

## 4.2 Bounds on the fixed point map

We are now almost ready to tackle the problem of constructing local solutions to (4.1). In the remainder of this section, we will apply the results from the previous subsection with the special case$Z = \Phi$. We furthermore assume that there exists a process Y such that (4.4) holds, again with the choice$Z = \Phi$

The above calculations suggest the introduction of a collection of space-time norms controlling the various quantities appearing there for functions taking values in spaces of rough paths controlled by Φ. Given a pair of functions v and$v ^ { \prime }$in $\mathcal { C } ( [ 0 , T ] \times S ^ { 1 } )$, we define the corresponding “remainder” process$R _ { t }$as before by

$$
R _ {t} ^ {v} (x, y) \stackrel {\mathrm{def}} {=} v _ {t} (y) - v _ {t} (x) - v _ {t} ^ {\prime} (x) \big (\Phi_ {t} (y) - \Phi_ {t} (x) \big),\tag{4.11}
$$

where the process Φ is as in (4.3). We also define the derivative process of$\mathcal { M } v$to be given by$( \mathcal { M } v ) ^ { \prime } = v$

Withe these notations at hand, we fix a (small) value$\kappa > 0$and we define the norms

$$
\begin{array}{l l} \| v \| _ {1, T} \stackrel {{\text { def }}} {{=}} \sup _ {0 <   t \leq T} t ^ {\alpha} \| v _ {t} \| _ {\frac {1}{2} - \kappa}, & \| v \| _ {2, T} \stackrel {{\text { def }}} {{=}} \sup _ {0 <   t \leq T} t ^ {\alpha} \| v _ {t} ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}}, \\ \| v \| _ {3, T} \stackrel {{\text { def }}} {{=}} \sup _ {0 <   t \leq T} t ^ {\alpha} \| R _ {t} ^ {v} \| _ {\frac {1}{2} + 2 \kappa}, & \| v \| _ {4, T} \stackrel {{\text { def }}} {{=}} \sup _ {0 <   t \leq T} t ^ {\beta} \| v _ {t} \| _ {\infty}, \\ \| v \| _ {5, T} \stackrel {{\text { def }}} {{=}} \sup _ {0 <   s <   t \leq T} \frac {s ^ {\gamma}}{| t - s | ^ {\delta}} \| v _ {t} - v _ {s} \| _ {\infty}, & \| v \| _ {\star , T} \stackrel {{\text { def }}} {{=}} \sum_ {j = 1} ^ {5} \| v \| _ {j, T}, \end{array}
$$

where$\alpha , \beta , \gamma$, and$\delta$are exponents in (0, 1) that are at this stage still to be determined. We furthermore denote by$B _ { \star , T }$the closure of$\mathcal { C } ^ { \infty } ( [ 0 , T ] \times S ^ { 1 } )$under$\| \cdot \| _ { \star , T }$. Here, we made an abuse of notation, since these (semi-)norms really are norms on the pair of processes$( \boldsymbol { v } , \boldsymbol { v } ^ { \prime } )$and not just on$v .$However, it will always be clear from the context what$v ^ { \prime } \mathrm { i s } .$, so we will usually omit it from our notations.

Our main result in this section is the following:

Proposition 4.3 Assume that${ \cal Y } ,$Φ and Y are as in$( 4 . 3 )$and$( 4 . 4 )$and that, for some$\begin{array} { r } { \bar { \kappa } < \kappa , } \end{array}$

$$
\sup _ {t \leq 1} (\| \Phi_ {t} \| _ {\frac {1}{2} - \bar {\kappa}} + \| Y _ {t} \| _ {\frac {1}{2} - \bar {\kappa}} + \| \mathbf {Y} _ {t} \| _ {1 - 2 \bar {\kappa}}) <   \infty .\tag{4.12}
$$

Then,for every$\begin{array} { r } { \kappa < \frac { 1 } { 1 0 } , } \end{array}$, there exist choices ofα,$\beta , \gamma ,$, and δ in (0, 1) such that

$$
\| \mathcal {M} v \| _ {\star , T} \lesssim T ^ {\theta} \| v \| _ {\star , T},
$$

for some$\theta > 0 ,$, and all$T \leq 1$. Here, the proportionality constant only depends on the quantity appearing in (4.12).

Proof. In the sequel, we always take for granted that$\alpha , \beta , \gamma , \delta \in ( 0 , 1 )$. We will bound the various norms appearing in$\| \cdot \| _ { \star , T }$separately, using the results from the previous subsection. Noting that, by the definitions of$\| \cdot \| _ { \star , T }$and$\mathcal { H }$, we have the bound

$$
\mathcal {K} _ {t} \lesssim t ^ {- \alpha} \| v \| _ {\star , T}.
$$

As a consequence, we have from (4.9) that

$$
\| (\mathcal {M} v) _ {t} \| _ {\frac {1}{2} - 3 \kappa} \lesssim \| v \| _ {\star , T} \int_ {0} ^ {t} \left((t - s) ^ {\frac {\kappa - \bar {\kappa}}{2} - 1} s ^ {- \beta} + (t - s) ^ {- \frac {3}{4} - \frac {\kappa}{2}} s ^ {- \alpha}\right) d s,
$$

so that, provided that

$$
\kappa <   \frac {1}{8},\tag{4.13a}
$$

we obtain the bound

$$
\| \mathcal {M} v \| _ {1, T} \lesssim (T ^ {\alpha + \frac {\kappa - \bar {\kappa}}{2} - \beta} + T ^ {\frac {1}{4} - \frac {\kappa}{2}}) \| v \| _ {\star , T}.
$$

In order for this to be bounded by a positive power of$T _ { \mathbf { \delta } }$we impose the additional condition

$$
\alpha > \beta .\tag{4.13b}
$$

Since$( \mathcal { M } v ) _ { t } ^ { \prime } = v _ { t }$by definition, the bound on$\| \mathcal { M } v \| _ { 2 , T }$is somewhat trivial. Using the simple interpolation bound$\| u \| _ { \alpha } \lesssim \| u \| _ { \infty } ^ { ( \bar { \alpha } - \alpha ) / \bar { \alpha } } \| u \| _ { \bar { \alpha } } ^ { \alpha / \bar { \alpha } }$, which holds for $0 < \alpha < \bar { \alpha } < 1$, one has indeed the bound

$$
\begin{array}{c} \| \mathcal {M} v \| _ {2, T} = \sup _ {t \leq T} t ^ {\alpha} \| v _ {s} \| _ {\mathcal {C} ^ {3 \kappa}} \lesssim \sup _ {t \leq T} t ^ {\alpha} (\| v _ {t} \| _ {\infty} ^ {\frac {1 - 8 \kappa}{1 - 2 \kappa}} \| v _ {t} \| _ {\frac {1}{2} - \kappa} ^ {\frac {6 \kappa}{1 - 2 \kappa}} + \| v _ {t} \| _ {\infty}) \\ \lesssim (T ^ {(\alpha - \beta) \frac {1 - 8 \kappa}{1 - 2 \kappa}} + T ^ {\alpha - \beta}) \| v \| _ {\star , T}, \end{array}
$$

which is bounded by a positive power of$T ,$, since we assumed that$\alpha > \beta$

For the bound on$R _ { t }$, we make use of Proposition 4.1, which yields the bound

$$
\begin{array}{l} \| \mathcal {M} v \| _ {3, T} \lesssim \| v \| _ {\star , T} \sup _ {t \leq T} t ^ {\alpha} \int_ {0} ^ {t} \big ((t - s) ^ {- \frac {3}{4} - 2 \kappa} s ^ {- \alpha} + (t - s) ^ {\delta - 1 - \frac {3 \kappa}{2}} s ^ {- \gamma} \big) d s \\ \qquad + \| v \| _ {\star , T} T ^ {\alpha - \frac {3 \kappa}{2} - \beta}. \end{array}
$$

Provided that the additional condition

$$
\delta > \frac {3 \kappa}{2}\tag{4.13c}
$$

holds, we conclude that

$$
\| \mathcal {M} v \| _ {3, T} \lesssim (T ^ {\frac {1}{4} - 2 \kappa} + T ^ {\alpha + \delta - \gamma - \frac {3 \kappa}{2}} + T ^ {\alpha - \beta - \frac {3 \kappa}{2}}) \| v \| _ {\star , T},
$$

yielding the additional conditions

$$
\alpha + \delta > \gamma + \frac {3 \kappa}{2}, \quad \alpha > \beta + \frac {3 \kappa}{2}.\tag{4.13d}
$$

We now turn to the bound on$\| v _ { t } \| _ { \infty }$. It follows from (4.10) that

$$
\| (\mathcal {M} v) _ {t} \| _ {\infty} \lesssim \| v \| _ {\star , T} \int_ {0} ^ {t} \left((t - s) ^ {- \frac {\kappa}{2} - \frac {3}{4}} s ^ {- \beta} + (t - s) ^ {- \kappa - \frac {1}{2}} s ^ {- \alpha}\right) d s,
$$

which yields the bound

$$
\| \mathcal {M} v \| _ {4, T} \lesssim (T ^ {\frac {1}{4} - \frac {\kappa}{2}} + T ^ {\beta - \alpha + \frac {1}{2} - \kappa}) \| v \| _ {\star , T},
$$

so that we have the additional condition

$$
\beta > \alpha - \frac {1}{2} + \kappa .\tag{4.13e}
$$

The last bound turn out to be slightly less straightforward. Indeed, we obtain from Proposition 4.2 the bound

$$
\| (\mathcal {M} v) _ {t} - (\mathcal {M} v) _ {s} \| _ {\infty} \lesssim \| v \| _ {\star , T} \int_ {0} ^ {s} \int_ {s} ^ {t} \Bigl (\frac {(q - r) ^ {- \frac {7}{4} - \frac {\kappa}{2}}}{r ^ {\beta}} + \frac {(q - r) ^ {- \frac {3}{2} - \kappa}}{r ^ {\alpha}} \Bigr) d q d r
$$

$$
+ \| v \| _ {\star , T} \int_ {s} ^ {t} \frac {d r}{r ^ {\beta} (t - r) ^ {\frac {3}{4} + \frac {\kappa}{2}}} + \| v \| _ {\star , T} \int_ {s} ^ {t} \frac {d r}{r ^ {\alpha} (t - r) ^ {\frac {1}{2} + \kappa}}.\tag{4.14}
$$

In order to bound the first term, we make use of the inequality

$$
\int_ {s} ^ {t} \frac {d q}{(q - r) ^ {\zeta}} \lesssim \frac {| t - s |}{| s - r | ^ {\zeta}} \wedge | s - r | ^ {1 - \zeta} \leq | t - s | ^ {\delta} | s - r | ^ {1 - \delta - \zeta},
$$

which is valid for every$\zeta > 1 , \delta \in [ 0 , 1 ]$, and$r < s < t .$. In particular, this implies that

$$
\int_ {0} ^ {s} \int_ {s} ^ {t} \Big (\frac {(q - r) ^ {- \frac {7}{4} - \frac {\kappa}{2}}}{r ^ {\beta}} + \frac {(q - r) ^ {- \frac {3}{2} - \kappa}}{r ^ {\alpha}} \Big) d q d r \lesssim | t - s | ^ {\delta} \big (s ^ {\frac {1}{4} - \frac {\kappa}{2} - \beta - \delta} + s ^ {\frac {1}{2} - \kappa - \alpha - \delta} \big).
$$

A similar calculation allows to bound the terms on the second line of (4.14). Indeed, for$\zeta , \eta \in ( 0 , 1 ) , \delta \in [ 0 , 1 - \zeta ]$, and$s < t ,$, one has the bound

$$
\int_ {s} ^ {t} \frac {d r}{r ^ {\eta} (t - r) ^ {\zeta}} \lesssim | t - s | ^ {1 - \zeta} \bigl (s ^ {- \eta} \wedge | t - s | ^ {- \eta} \bigr) \lesssim | t - s | ^ {\delta} \bigl (1 \vee s ^ {1 - \zeta - \eta - \delta} \bigr).\tag{4.15}
$$

It follows from all of these considerations that, provided that

$$
\delta \leq \frac {1}{4} - \frac {\kappa}{2},\tag{4.13f}
$$

one obtains the bound

$$
\| \mathcal {M} v \| _ {5, T} \lesssim (T ^ {\gamma - \beta - \delta + \frac {1}{4} - \frac {\kappa}{2}} + T ^ {\gamma - \alpha - \delta + \frac {1}{2} - \kappa}) \| v \| _ {\star , T}.
$$

As a consequence, we impose the condition

$$
\gamma > \left(\beta + \delta - \frac {1}{4} + \frac {\kappa}{2}\right) \vee \left(\alpha + \delta - \frac {1}{2} + \kappa\right).\tag{4.13g}
$$

It now remains to check that the conditions (4.13a)–(4.13g) can be satisfied simultaneously for κ small enough. For example, we can set

$$
\alpha = 1 - 2 \kappa , \quad \beta = \frac {1 - \kappa}{2}, \quad \gamma = 1 - 2 \kappa , \quad \delta = 2 \kappa .\tag{4.16}
$$

With these definitions, it is straightforward to check that the conditions (4.13a)– (4.13g) are indeed satisfied, provided that one chooses$\kappa < \frac { 1 } { 1 0 }$□

Remark 4.4 It follows from the proof of Proposition 4.3 and from Proposition 3.3 that the map M is actually uniformly continuous on bounded sets.

## 4.3 Construction of solutions

We now have all the ingredients in place for the proof of our main uniqueness result. We define solutions to (4.1) as solutions to the fixed point problem

$$
v = \hat {\mathcal {M}} (v),\tag{4.17}
$$

where$\hat { \mathcal { M } }$is the nonlinear operator given by

$$
\big (\hat {\mathcal {M}} (v) \big) _ {t} = P _ {t} v _ {0} + \big (\mathcal {M} G (v., \cdot) \big) _ {t} + \partial_ {x} \int_ {0} ^ {t} P _ {t - s} F (v _ {s}, s) d s,\tag{4.18}
$$

where$P _ { t }$denotes the heat semigroup. For fixed$t > 0$, we will consider$( \hat { \mathcal { M } } ( v ) ) _ { t }$) as a path controlled by$\Phi _ { t }$and we define its derivative process as

$$
\big (\hat {\mathcal {M}} ^ {\prime} (v) \big) _ {t} = G (v _ {t}, t).
$$

We will assume in this section that the nonlinearity$F$can be split into two parts $F = F _ { 1 } + F _ { 2 }$, with different regularity properties. Our precise assumptions on$F _ { 1 }$ $F _ { 2 }$and$G$are summarised in the following three assumptions:

Assumption 4.5 For every$t > 0 ,$, the map$F _ { 1 } ( \cdot , t )$maps${ \mathcal { C } } ( S ^ { 1 } )$into itself. Furthermore, it satisfies the bounds

$$
\| F _ {1} (v, t) \| _ {\infty} \lesssim 1 + \| v \| _ {\infty} ^ {2}, \| F _ {1} (u, t) - F _ {1} (v, t) \| _ {\infty} \lesssim \| u - v \| _ {\infty} \left(1 + \| u \| _ {\infty} + \| v \| _ {\infty}\right),
$$

for all u and v in${ \mathcal { C } } ( S ^ { 1 } )$, with a proportionality constant that is uniform over bounded time intervals.

Assumption 4.6 There exists$\begin{array} { r } { \eta < \frac { 1 } { 2 } } \end{array}$such that, for every$t > 0$, the map$F _ { 2 } ( \cdot , t )$ maps${ \mathcal { C } } ( S ^ { 1 } )$into${ \mathcal { C } } ^ { - \eta }$. Furthermore, it satisfies the bounds

$$
\| F _ {2} (v, t) \| _ {- \eta} \lesssim 1 + \| v \| _ {\infty}, \quad \| F _ {2} (u, t) - F _ {2} (v, t) \| _ {- \eta} \lesssim \| u - v \| _ {\infty},
$$

for all u and v in${ \mathcal { C } } ( S ^ { 1 } )$, with a proportionality constant that is uniform over bounded time intervals.

Assumption 4.7 For every$t > 0 ,$, the map$G ( \cdot , t )$maps$\mathcal { C } ( S ^ { 1 } )$into itself. Furthermore,$i f ( v , v ^ { \prime } )$is controlled by$\Phi _ { t } ,$, then this is also the case for$G ( v , t )$, for some “derivative process$v _ { G ^ { \prime } ( v , v ^ { \prime } , t ) }$. Denote by$R _ { t } ^ { v }$the remainderfor$( \boldsymbol { v } , \boldsymbol { v } ^ { \prime } )$and by$R _ { t } ^ { G }$ the remainderfor$( G ( v , t ) , G ^ { \prime } ( v , v ^ { \prime } , t ) )$. Then, there exists$\kappa \in ( 0 , \frac { 1 } { 4 } )$such that,for every$\zeta \in ( 0 , \frac { 1 } { 2 } - \kappa )$, one has the bounds

$$
\| G (v, t) \| _ {\zeta} \lesssim 1 + \| v \| _ {\zeta}, \quad \| G (u, t) - G (v, t) \| _ {\zeta} \lesssim \| u - v \| _ {\zeta}.
$$

Furthermore,for the same$\kappa > 0 ,$, one has the bounds

$$
\left\| G (v, t) - G (v, s) \right\| _ {\infty} \lesssim | t - s | ^ {2 \kappa},
$$

$$
\begin{array}{c} \| G (v, t) - G (u, t) - G (v, s) + G (u, s) \| _ {\infty} \lesssim \| u - v \| _ {\infty}, \\ \| G ^ {\prime} (v, t) \| _ {\mathcal {C} ^ {3 \kappa}} \lesssim 1 + \| v ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}} + \| v \| _ {\mathcal {C} ^ {\frac {1}{2} - \kappa}} + \| R _ {t} ^ {v} \| _ {\frac {1}{2} + 2 \kappa}, \\ \| G ^ {\prime} (u, u ^ {\prime}, t) - G ^ {\prime} (v, v ^ {\prime}, t) \| _ {\mathcal {C} ^ {3 \kappa}} \lesssim \| u ^ {\prime} - v ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}} + \| u - v \| _ {\mathcal {C} ^ {\frac {1}{2} - \kappa}} + \| R _ {t} ^ {u} - R _ {t} ^ {v} \| _ {\frac {1}{2} + 2 \kappa}, \\ \| R _ {t} ^ {G (v)} \| _ {\frac {1}{2} + 2 \kappa} \lesssim 1 + \| v ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}} + \| v \| _ {\mathcal {C} ^ {\frac {1}{2} - \kappa}} + \| R _ {t} ^ {v} \| _ {\frac {1}{2} + 2 \kappa}, \\ \| R _ {t} ^ {G (u)} (u) - R _ {t} ^ {G (v)} (v) \| _ {\frac {1}{2} + 2 \kappa} \lesssim \| u ^ {\prime} - v ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}} + \| u - v \| _ {\mathcal {C} ^ {\frac {1}{2} - \kappa}} + \| R _ {t} ^ {u} - R _ {t} ^ {v} \| _ {\frac {1}{2} + 2 \kappa}, \end{array}
$$

with a proportionality constant that is uniform over bounded time intervals.

We now have all the necessary ingredients to solve (4.18) by a fixed point argument.

Theorem 4.8 Assume that there exist κ$< \frac { 1 } { 1 2 }$and$\eta < \frac { 1 } { 2 } - 2 I$κ such that Assumptions 4.5–4.7 hold. Assumefurthermore that$Y$, Φ and$\mathbf { Y }$are as in$( 4 . 3 )$and (4.4) and that the bound (4.12) holdsfor some$\bar { \kappa } \in ( 0 , \kappa )$

Then,for every initial condition$v _ { 0 } \in \mathcal { C } ^ { \zeta - 1 }$with$\zeta > 2 \kappa ,$, there exists a choice of exponents$\alpha , \beta , \gamma$and δ such that the nonlinear operator$\hat { \mathcal { M } }$maps$B _ { \star , T }$into itselffor every$T > 0 .$. Furthermore, there exists$T _ { \star } > 0$such that thefixed point equation$( 4 . I 7 )$admits a solution in$B _ { \star , T _ { \star } }$, and this solution is unique.

Proof. We choose$\alpha , \beta , \gamma$and$\delta$as in (4.16). With this choice, it suffices to show that there exists$T > 0$such that$\hat { \mathcal { M } }$maps some ball of$B _ { \star , T }$into itself and is a contraction there.

We first consider the first term in$\hat { \mathcal { M } }$, namely$P _ { t } \boldsymbol { v } _ { 0 }$. It follows from Proposition A.11 that one has the bounds

$$
\| P _ {t} v _ {0} \| _ {\frac {1}{2} + 2 \kappa} \lesssim t ^ {- \frac {3}{4}} \| v _ {0} \| _ {\zeta - 1}, \quad \| P _ {t} v _ {0} \| _ {\infty} \lesssim t ^ {\kappa - \frac {1}{2}} \| v _ {0} \| _ {\zeta - 1},
$$

as well as

$$
\begin{array}{r} \| P _ {t} v _ {0} - P _ {s} v _ {0} \| _ {\infty} = \| (P _ {t - s} - 1) P _ {s} v _ {0} \| _ {\infty} \lesssim | t - s | ^ {\delta} \| P _ {s} v _ {0} \| _ {2 \delta} \\ \lesssim | t - s | ^ {\delta} s ^ {\kappa - \delta - \frac {1}{2}} \| v _ {0} \| _ {\zeta - 1}. \end{array}\tag{4.19}
$$

Here, we made use of the fact that$\zeta > 2 \kappa$by assumption. Since, by our assumptions, we have$\alpha > { \frac { 3 } { 4 } } , \beta > { \frac { 1 } { 2 } } - \kappa$, and$\begin{array} { r } { \gamma > \frac { 1 } { 2 } + \delta - \kappa . } \end{array}$, it follows that we have the bound

$$
\| P. v _ {0} \| _ {\star , T} \lesssim T ^ {\theta} \| v _ {0} \| _ {\zeta - 1},
$$

for some$\theta > 0$. (Note that we consider the derivative process of$P _ { t } \boldsymbol { v } _ { 0 }$to be simply 0.)

In the next step, define a nonlinear map N by

$$
(\mathcal {N} v) _ {t} = \partial_ {x} \int_ {0} ^ {t} P _ {t - s} F (v _ {s}, s) d s.
$$

It then follows from Proposition A.11 and the assumptions on$F$that

$$
\begin{array}{l} \| (\mathcal {N} v) _ {t} \| _ {\frac {1}{2} + 2 \kappa} \lesssim \int_ {0} ^ {t} \left((t - s) ^ {- \kappa - \frac {3}{4}} \| F _ {1} (v _ {s}, s) \| _ {\infty} + (t - s) ^ {- \frac {\eta}{2} - \frac {3}{4} - \kappa} \| F _ {2} (v _ {s}, s) \| _ {- \eta}\right) d s \\ \lesssim (1 + \| v \| _ {\star , T}) ^ {2} \int_ {0} ^ {t} \left((t - s) ^ {- \kappa - \frac {3}{4}} s ^ {- 2 \beta} + (t - s) ^ {- \frac {\eta}{2} - \frac {3}{4} - \kappa} s ^ {- \beta}\right) d s \\ \lesssim (1 + \| v \| _ {\star , T}) ^ {2} \left(T ^ {\frac {1}{4} - \kappa - 2 \beta} + T ^ {\frac {1}{4} - \frac {\eta}{2} - \kappa - \beta}\right). \end{array} \tag {4.20a}
$$

Similarly, the supremum norm is bounded by

$$
\| (\mathcal {N} v) _ {t} \| _ {\infty} \lesssim (1 + \| v \| _ {\star , T}) ^ {2} \left(T ^ {\frac {1}{2} - 2 \beta} + T ^ {\frac {1}{2} - \frac {\eta}{2} - \beta}\right).\tag{4.20b}
$$

Regarding the time regularity bound, we have as in (4.19) the bound

$$
\begin{array}{l} \| (\mathcal {N} v) _ {t} - (\mathcal {N} v) _ {s} \| _ {\infty} \lesssim \int_ {s} ^ {t} \left((t - r) ^ {- \frac {1}{2}} \| F _ {1} (v _ {r}, r) \| _ {\infty} + (t - r) ^ {- \frac {\eta}{2} - \frac {1}{2}} \| F _ {2} (v _ {r}, r) \| _ {- \eta}\right) d r \\ \quad + | t - s | ^ {\delta} \int_ {0} ^ {s} (s - r) ^ {- \frac {1}{2} - \delta} \| F _ {1} (v _ {r}, r) \| _ {\infty} d r \\ \quad + | t - s | ^ {\delta} \int_ {0} ^ {s} (s - r) ^ {- \frac {\eta}{2} - \frac {1}{2} - \delta} \| F _ {2} (v _ {r}, r) \| _ {- \eta} d r. \end{array} \tag {4.21}
$$

Making use of the bound (4.15) and otherwise proceeding as before, we conclude that

$$
\left\| (\mathcal {N} v) _ {t} - (\mathcal {N} v) _ {s} \right\| _ {\infty} \lesssim | t - s | ^ {\delta} \big (1 + \| v \| _ {\star , T} \big) ^ {2} \Big (T ^ {\frac {1}{2} - 2 \beta - \delta} + T ^ {\frac {1}{2} - \frac {\eta}{2} - \beta - \delta} \Big).\tag{4.20c}
$$

Note here that, since$\kappa < \frac { 1 } { 1 2 }$by assumption, we have$\eta < 1 - 8 \kappa$. This ensures that the bound$\begin{array} { r } { \delta < \frac { 1 } { 2 } - \frac { \eta } { 2 } - \delta } \end{array}$, which is required in (4.15), does indeed hold.

Collecting the bounds from (4.20), it is lengthy but straightforward to check that, thanks to our assumptions on$\kappa , \eta _ { \mathrm { : } }$, and$\delta ,$there exists$\theta > 0$such that one does have the bound

$$
\| \mathcal {N} v \| _ {\star , T} \lesssim T ^ {\theta} (1 + \| v \| _ {\star , T}) ^ {2}.
$$

Similarly, one can verify in exactly the same way that one also has the bound

$$
\| \mathcal {N} u - \mathcal {N} v \| _ {\star , T} \lesssim T ^ {\theta} \| u - v \| _ {\star , T} (1 + \| u \| _ {\star , T} + \| v \| _ {\star , T}).
$$

Furthermore, the assumptions on the map$G$are set up precisely in such a way that one has

$$
\| G (v., \cdot) \| _ {\star , T} \lesssim 1 + \| v \| _ {\star , T}, \quad \| G (u., \cdot) - G (v., \cdot) \| _ {\star , T} \lesssim \| u - v \| _ {\star , T}.
$$

Combining this with Proposition 4.3, as well as the bounds on$\mathcal { N }$and$P _ { t } \boldsymbol { v } _ { 0 }$that we just obtained, we conclude that

$$
\begin{array}{r} \| \hat {\mathcal {M}} v \| _ {\star , T} \lesssim T ^ {\theta} (1 + \| v \| _ {\star , T}) ^ {2}, \\ \| \hat {\mathcal {M}} u - \hat {\mathcal {M}} v \| _ {\star , T} \lesssim T ^ {\theta} (1 + \| u \| _ {\star , T} + \| v \| _ {\star , T}) \| u - v \| _ {\star , T}. \end{array}\tag{4.22}
$$

It follows immediately that, for$T > 0$small enough, there exists a ball around the origin in$B _ { \star , T }$which is left invariant by$\hat { \mathcal { M } }$and such that$\hat { \mathcal { M } }$admits a unique fixed point in this ball.

The uniqueness of this fixed point in all of$B _ { \star , T }$now follows from the following argument. Denote by$T _ { \star }$and$v _ { \star }$the time horizon and fixed point that were just constructed and assume that there exists a fixed point$v \neq v _ { \star }$for$\hat { \mathcal { M } }$. Note now that, by the definition of the norm$\| \cdot \| _ { \star , T }$, the natural restriction operator from$B _ { \star , T _ { \star } }$to $B _ { \star , T }$is a contraction for every$T < T _ { \star }$. Since it follows from (4.22) that there exists some$T \in ( 0 , T _ { \star } )$) such that$\hat { \mathcal { M } }$is a contraction in the ball of radius$\lVert v \rVert _ { \star , T _ { \star } }$in$B _ { \star , T }$ this shows that on the interval$[ 0 , T ]$, v must agree with$v _ { \star }$. The uniqueness claim then follows by iterating this argument.□

Once we do have a unique solution to a PDE, we can perform the usual kind of bootstrapping argument to improve the regularity estimates provided “for free” by the fixed point argument. In our case, we can certainly not expect the solution v to be more regular than the process Φ, which in turn cannot be expected to be more regular than$Y$. However, it is possible to slightly improve the regularity estimates for the remainder term$R _ { t } ^ { v } ( x , y )$defined in (4.11). Our current bounds show that $\| R _ { t } ^ { v } \| _ { \frac { 1 } { 2 } + 2 \kappa } < \infty$, which is not a very good bound in general.

Given the (lack of) regularity of$F _ { 1 }$, we certainly do not expect$\| R _ { t } ^ { v } \| _ { 1 }$to be finite, but it turns out that this can be approached arbitrarily close:

Proposition 4.9 Let the assumptions of Theorem 4.8 hold, let v be the unique maximal solution to$( 4 . I 8 )$with lifetime$T _ { \star }$. Then,for$0 < s < t < T _ { \star }$, one has

$$
\left\| v _ {t} - v _ {s} \right\| _ {\infty} \lesssim | t - s | ^ {\gamma},\tag{4.23}
$$

for every$\begin{array} { r } { \gamma < \frac { 1 } { 4 } - \frac { \bar { \kappa } } { 2 } } \end{array}$. The proportionality constant is uniform over every compact time interval in$( 0 , T _ { \star } )$. Furthermore, one has

$$
\| R _ {t} ^ {v} \| _ {\bar {\gamma}} <   \infty ,
$$

for every$\bar { \gamma } < 1 - ( 2 \bar { \kappa } \vee \eta )$and every$t \in ( 0 , T _ { \star } )$

Proof. Since it is possible to concatenate solutions to (4.18), we can restart the solution at some positive time. As a consequence, since we know that the solution belongs to$B _ { \star , T }$, we can assume that$\lVert \boldsymbol { v } _ { t } \rVert _ { \frac { 1 } { 2 } - \kappa }$and$\| R _ { t } ^ { v } \| _ { \frac { 1 } { 2 } + 2 \kappa }$are bounded uniformly in time. Since we furthermore know that$v _ { t }$is controlled by$\Phi _ { t }$with remainder$R _ { t } ^ { v }$ we obtain that actually$\lVert \boldsymbol { v } _ { t } \rVert _ { \frac { 1 } { 2 } - \overline { { \kappa } } }$is bounded. Furthermore, since$v _ { t } ^ { \prime } = G ( v _ { t } , t )$by construction, we also have$\lVert \bar { v } _ { t } ^ { \prime } \rVert _ { \frac { 1 } { 2 } - \bar { \kappa } }$2uniformly bounded.

It then follows form (4.21) that

$$
\| \mathcal {N} v _ {t} - \mathcal {N} v _ {s} \| \lesssim | t - s | ^ {\gamma},
$$

provided that$\begin{array} { r } { \gamma < \frac { 1 } { 2 } - \frac { \eta } { 2 } } \end{array}$. It follows from Proposition 4.2 that a similar bound holds for the term$\boldsymbol { \mathcal { M } } \boldsymbol { G } ( \boldsymbol { v } _ { t } , t )$, provided that$\begin{array} { r } { \gamma < \frac { 1 } { 4 } - \frac { \bar { \kappa } } { 2 } } \end{array}$, so that the first bound follows.

For the second bound, it follows from Proposition A.11 that the bound holds for $\mathcal { N } v _ { t }$. To show that it also holds for$\boldsymbol { \mathcal { M } } \boldsymbol { G } ( \boldsymbol { v } _ { t } , t )$, it suffices to apply Proposition 4.1 by noting that the right hand side of that bound is integrable as soon as$\begin{array} { r } { \kappa < \frac { 1 } { 4 } - \bar { \kappa } . } \end{array}$ thanks to the bound (4.23).□

An important special case is given by the case when

$$
G (v, t) = v + w _ {t},
$$

for some fixed process w such that$w _ { t }$is controlled by$\Phi _ { t }$for every t with

$$
\sup _ {t \leq T} \| w _ {t} ^ {\prime} \| _ {\mathcal {C} ^ {3 \kappa}} <   \infty , \quad \sup _ {t \leq T} \| R _ {t} ^ {w} \| _ {\frac {1}{2} + 2 \kappa} <   \infty , \quad \sup _ {s, t \leq T} \frac {\| w _ {t} - w _ {s} \| _ {\infty}}{| t - s | ^ {\kappa}} <   \infty ,\tag{4.24}
$$

One then has:

Proposition 4.10 Let the assumptions ofTheorem 4.8 hold and let$G ( v , t ) = c v \mathrm { ~ + ~ }$ $w _ { t }$with w as above and$c \in \mathbf { R } .$. Let v be the unique maximal solution to$( 4 . I 8 )$with lifetime$T _ { \star }$. Then,for every$t \in ( 0 , T _ { \star } )$, one has the decomposition

$$
e ^ {- c \Phi_ {t} (x)} v _ {t} (x) = \int_ {0} ^ {x} e ^ {- c \Phi_ {t} (z)} w _ {t} (z) d \Phi_ {t} (z) + R _ {t} (x),\tag{4.25}
$$

with$R _ { t } \in \mathcal { C } ^ { \bar { \gamma } }$for every$\bar { \gamma } < 1 - ( 2 \bar { \kappa } \vee \eta )$

Remark 4.11 The rough integral appearing on the right hand side is well-posed since, by assumption,$w _ { t }$is controlled by$\Phi _ { t }$, so that the same is true for the integrand in (4.25).

Remark 4.12 It is not guaranteed that$\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } e ^ { - c \Phi _ { t } ( z ) } w _ { t } ( z ) d \Phi _ { t } ( z ) = 0 , } \end{array}$, so the two functions appearing in the right hand side of (4.25) are not necessarily periodic. This is irrelevant however, since one can easily rectify this by adding to each of them a suitable multiple of x.

Proof of Proposition 4.10. Setting$\tilde { v } _ { t } ( x ) ~ = ~ \int _ { 0 } ^ { x } e ^ { - c \Phi _ { t } ( z ) } w _ { t } ( z ) d \Phi _ { t } ( z )$, it follows from (4.24) and Theorem 3.2 that

$$
\delta \tilde {v} _ {t} (x, y) = e ^ {- c \Phi_ {t} (x)} w _ {t} (x) \delta \Phi_ {t} (x, y) + R _ {t} ^ {\tilde {v}} (x, y),\tag{4.26}
$$

with$\| R _ { t } ^ { \tilde { v } } \| _ { 1 - 2 \bar { \kappa } } < \infty$

On the other hand, we know from Proposition 4.9 that

$$
\delta v _ {t} (x, y) = \bigl (c v _ {t} (x) + w _ {t} (x) \bigr) \delta \Phi_ {t} (x, y) + R _ {t} ^ {v} (x, y),
$$

with$\| R _ { t } ^ { v } \| _ { \bar { \gamma } } < \infty$. In particular, this implies that

$$
v _ {t} (y) = v _ {t} (x) \big (1 + c \delta \Phi_ {t} (x, y) \big) + w _ {t} (x) \delta \Phi_ {t} (x, y) + R _ {t} ^ {v} (x, y)
$$

$$
= v _ {t} (x) e ^ {c \delta \Phi_ {t} (x, y)} + w _ {t} (x) \delta \Phi_ {t} (x, y) + \tilde {R} _ {t} ^ {v} (x, y),
$$

where we also have$\| \tilde { R } _ { t } ^ { v } \| _ { \bar { \gamma } } < \infty$. Multiplying both sides by$e ^ { - c \Phi _ { t } ( y ) }$and subtracting (4.26) from the resulting expression, we obtain the identity

$$
\begin{array}{r l} e ^ {- c \Phi_ {t} (y)} v _ {t} (y) - e ^ {- c \Phi_ {t} (x)} v _ {t} (x) = & \int_ {x} ^ {y} e ^ {- c \Phi_ {t} (z)} w _ {t} (z) d \Phi_ {t} (z) \\ & + e ^ {- c \Phi_ {t} (y)} \tilde {R} _ {t} ^ {v} (x, y) - R _ {\tilde {t}} ^ {\tilde {v}} (x, y). \end{array}
$$

It follows that the function$R _ { t }$defined in (4.25) satisfies the identity$\delta R _ { t } ( x , y ) =$ $e ^ { - c \Phi _ { t } ( y ) } \tilde { R } _ { t } ^ { v } ( x , y ) - R _ { t } ^ { \tilde { v } } ( x , y )$, so that the claim follows at once.□

## 5 Construction of the universal process

The aim of this section is to prove the convergence of the processes$Y _ { \varepsilon } ^ { \tau }$to some limiting processes$Y ^ { \tau }$. Actually, it turns out that the constant Fourier mode requires a separate treatment, so we only consider the centred processes$X _ { \varepsilon } ^ { \tau }$here, which were defined in (2.1). The aim of this section is to show that, for every binary tree τ, there exists a process$X ^ { \tau }$such that

$$
X ^ {\tau} = \lim _ {\varepsilon \to 0} X _ {\varepsilon} ^ {\tau},
$$

in a suitable sense, and to obtain quantitative estimates on$X ^ { \tau }$

## 5.1 Construction of$X ^ { \mathbb { Y } } .$

A crucial observation for the sequel is that, for$k \neq 0$, the covariance of the Fourier modes of$X _ { \varepsilon } ^ { \bullet }$is given by

$$
\mathbf {E} X _ {\varepsilon , k} ^ {\bullet} (s) X _ {\varepsilon , \ell} ^ {\bullet} (t) = \delta_ {k, - \ell} \frac {\varphi^ {2} (\varepsilon k)}{k ^ {2}} \exp (- k ^ {2} | t - s |).
$$

Since$X _ { \varepsilon }$and$X _ { \xi } ^ { \bullet }$will virtually always arise via their spatial derivatives, it will be convenient to introduce a notation for this. We therefore define${ \bar { X } } ^ { \tau } { \overset { \underset { \mathrm { d e f } } { } } { = } } \partial _ { x } X ^ { \tau }$as in (2.8), and similarly for$\bar { X } _ { \varepsilon } ^ { \tau }$, so that one has the identity

$$
\mathbf {E} \bar {X} _ {\varepsilon , k} ^ {\bullet} (s) \bar {X} _ {\varepsilon , \ell} ^ {\bullet} (t) = \delta_ {k, - \ell} \varphi^ {2} (\varepsilon k) \exp (- k ^ {2} | t - s |),\tag{5.1}
$$

provided that$k \neq 0$. This is where our convention (1.2) shows its advantage: this choice of normalisation for the driving noise ensures that we do not have any constant prefactor appearing in (5.1) so that, except for the constant mode, the space-time correlation function of$\bar { X } ^ { \bullet }$is precisely equal to the heat kernel.

With these notations at hand, the process$X _ { \varepsilon } ^ { \vee }$is given as the stationary solution to

$$
\partial_ {t} X _ {\varepsilon} ^ {\mathsf {V}} = \partial_ {x} ^ {2} X _ {\varepsilon} ^ {\mathsf {V}} + \Pi_ {0} ^ {\perp} | \bar {X} _ {\varepsilon} ^ {\bullet} | ^ {2},\tag{5.2}
$$

so that its Fourier modes are given for$k \neq 0$by the identity

$$
X _ {\varepsilon , k} ^ {\mathbf {V}} (t) = \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} \sum_ {\ell \in \mathbf {Z}} \bar {X} _ {\varepsilon , \ell} ^ {\bullet} (s) \bar {X} _ {\varepsilon , k - \ell} ^ {\bullet} (s) d s.\tag{5.3}
$$

We now show that$X _ { \varepsilon } ^ { \vee }$converges to a limiting process$X ^ { \vee }$in the following sense:

Proposition 5.1 There exists a process$X ^ { \mathbb { V } }$such that the weak convergence$X _ { \varepsilon } ^ { \tt V }$ $X ^ { \vee }$takes place in$\mathcal { C } ( [ - T , T ] , \mathcal { C } ^ { \alpha } ) \cap \mathcal { C } ^ { \beta } ( [ - T , T ] , \mathcal { C } )$for every$\alpha < 1$, every$\beta < \textstyle { \frac { 1 } { 2 } }$ and every$T > 0$

Before we proceed to the proof, we recall Wick’s theorem (sometimes also called Isserlis’s theorem) on the higher order moments of Gaussian random variables:

Proposition 5.2 Let T be afinite index set and let$\{ X _ { \alpha } \} _ { \alpha \in T }$be a collection ofreal or complex-valued centredjointly Gaussian random variables. Then,

$$
\mathbf {E} \prod_ {\alpha \in T} X _ {\alpha} = \sum_ {P \in \mathcal {P} (T)} \prod_ {\{\alpha , \beta \} \in P} \mathbf {E} X _ {\alpha} X _ {\beta}.
$$

ProofofProposition 5.1. The proof is an almost direct application of Proposition A.2 below. Indeed, writing$\mathbf { Z } _ { \star } = \mathbf { Z } \backslash \{ 0 \}$as a shorthand, we can set$\mathcal { J } = \mathbf { Z } _ { \star } ^ { 2 }$ and write elements in$\mathcal { J }$as$\kappa = ( k , \ell ) \in \mathcal { J }$. For$\kappa = ( k , \ell )$, we furthermore set $g _ { \kappa } ( x ) = \exp ( i k x )$and$C _ { \varepsilon } ( \kappa ) = \varphi ( \varepsilon \ell ) \varphi ( \varepsilon ( k - \ell ) )$. With this notation, the involution ι appearing in the assumptions is given by$( k , \ell )  ( - k , \ell )$

Since it follows from (5.3) and Proposition 5.2 that

$$
X _ {\varepsilon} ^ {\mathsf {V}} (x, t) = \sum_ {\kappa = (k, \ell) \in \mathcal {J}} g _ {\kappa} (x) C _ {\varepsilon} (\kappa) \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} \bar {X} _ {\ell} ^ {\bullet} (s) \bar {X} _ {k - \ell} ^ {\bullet} (s) d s ,
$$

we set

$$
f _ {\kappa} (t) = \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} \bar {X} _ {\ell} ^ {\bullet} (s) \bar {X} _ {k - \ell} ^ {\bullet} (s) d s,
$$

in order to be in the framework of Proposition A.2. It then follows from (5.1) that

$$
\mathbf {E} f _ {\kappa} (t) f _ {\bar {\kappa}} (s) = \delta_ {k, - \bar {k}} (\delta_ {\ell , - \bar {\ell}} + \delta_ {\ell - k, \bar {\ell}}) K _ {\kappa} (s, t),
$$

where the kernels$K _ { \kappa } ( s , t )$are given for$\kappa = ( k , \ell )$by

$$
\begin{array}{r} K _ {\kappa} (s, t) = \int_ {- \infty} ^ {t} \int_ {- \infty} ^ {s} e ^ {- k ^ {2} (t + s - r - r ^ {\prime}) - \ell^ {2} | r - r ^ {\prime} | - (k - \ell) ^ {2} | r - r ^ {\prime} |} d r d r ^ {\prime} \\ = \int_ {- \infty} ^ {t - s} \int_ {- \infty} ^ {0} e ^ {- k ^ {2} (t - s - r - r ^ {\prime}) - \ell^ {2} | r - r ^ {\prime} | - (k - \ell) ^ {2} | r - r ^ {\prime} |} d r d r ^ {\prime}. \end{array}
$$

Here we assumed$t > s$for simplicity, but the kernels are of course symmetric in s and t. A lengthy but straightforward calculation then shows that one has the identity

$$
K _ {\kappa} (s, t) = \frac {k ^ {2} e ^ {- (\ell^ {2} + (k - \ell) ^ {2}) | t - s |} - (\ell^ {2} + (k - \ell) ^ {2}) e ^ {- k ^ {2} | t - s |}}{k ^ {2} (k ^ {2} - \ell^ {2} - (k - \ell) ^ {2}) (k ^ {2} + \ell^ {2} + (k - \ell) ^ {2})} .\tag{5.4}
$$

It will be convenient in the sequel to introduce the shorthand notation

$$
\Delta_ {\kappa , \bar {\kappa}} = \delta_ {k, - \bar {k}} (\delta_ {\ell , - \bar {\ell}} + \delta_ {\ell - k, \bar {\ell}}), \quad \kappa = (k, \ell), \quad \bar {\kappa} = (\bar {k}, \bar {\ell}).
$$

With this notation, we then have, for$F _ { \kappa \eta }$as in Proposition A.2, the identity

$$
F _ {\kappa \eta} (t) \propto \Delta_ {\kappa , \eta} K _ {\kappa} (t, t) = \frac {\Delta_ {\kappa , \eta}}{k ^ {2} (k ^ {2} + \ell^ {2} + (k - \ell) ^ {2})} = \frac {\Delta_ {\kappa , \eta}}{2 k ^ {2} (k ^ {2} - k \ell + \ell^ {2})}.
$$

Using Proposition A.3 below, we furthermore obtain from (5.4) the bound

$$
\hat {F} _ {\kappa \eta} (s, t) \propto \Delta_ {\kappa , \eta} | K _ {\kappa} (s, t) - K _ {\kappa} (0, 0) | \leq F _ {\kappa \eta} \wedge \frac {\ell^ {2} + (k - \ell) ^ {2}}{k ^ {2} - k \ell + \ell^ {2}} | t - s | ^ {2}.
$$

In particular, for every$\beta \leq 1$, one has

$$
\hat {F} _ {\kappa \eta} (s, t) = \Delta_ {\kappa , \eta} | t - s | ^ {2 \beta} \frac {| \ell^ {2} + (k - \ell) ^ {2} | ^ {\beta} | k | ^ {2 \beta - 2}}{k ^ {2} - k \ell + \ell^ {2}}.
$$

Since furthermore the Lipschitz constant of$g _ { \kappa }$is given by$G _ { \kappa } = | k |$, the conditions (A.2) boil down to

$$
\sum_ {k \neq 0} | k | ^ {2 \alpha} \sum_ {\ell \neq 0} \frac {1}{k ^ {2} (k ^ {2} - k \ell + \ell^ {2})} <   \infty ,
$$

$$
\sum_ {k \neq 0} | k | ^ {2 \beta - 2} \sum_ {\ell \neq 0} \frac {| \ell^ {2} + (k - \ell) ^ {2} | ^ {\beta}}{k ^ {2} - k \ell + \ell^ {2}} <   \infty .
$$

Approximating the sum by an integral, one can check that

$$
\sum_ {\ell \neq 0} \frac {1}{k ^ {2} (k ^ {2} - k \ell + \ell^ {2})} \lesssim \frac {1}{k ^ {3}},
$$

so that the first condition is indeed satisfied as soon as$\alpha < 1$

Regarding the second condition, one similarly obtains

$$
\sum_ {\ell \in \mathbf {Z}} \frac {| \ell^ {2} + (k - \ell) ^ {2} | ^ {\beta}}{k ^ {2} - k \ell + \ell^ {2}} \lesssim \frac {1}{k ^ {1 - 2 \beta}},
$$

provided that$\beta < \textstyle { \frac { 1 } { 2 } }$(otherwise, the expression is not summable). As a consequence, the second condition reduces to$k ^ { 4 \beta - \hat { 3 } }$being summable, which is again the case if and only$\begin{array} { r } { \operatorname { i f } \beta < \frac { 1 } { 2 } } \end{array}$. This concludes the proof.□

Remark 5.3 It also follows from the proof that, for any fixed t,$X ^ { \mathsf { V } } ( t ) \notin H ^ { 1 }$almost surely, since one has$\begin{array} { r } { \mathbf { E } \big ( X _ { k } ^ { \vee } ( t ) \big ) ^ { 2 } \sim \frac { 1 } { k ^ { 3 } } } \end{array}$

Remark 5.4 In light of the construction just explained, we can understand how the limit$\textstyle \alpha = { \frac { 1 } { 8 } }$arises in (1.6). Indeed, it turns out that$\alpha > \frac { 1 } { 8 }$is precisely the borderline for which the right hand side in (5.2) converges to a limit for every fixed value of t. The reason why we can break through this barrier is that, instead of making sense of the right hand side for fixed t, we only need to make sense of its time integral. (This was already remarked in [GJ10, Ass11].)

If we use this trick and then continued with the classical tools as in [DPDT07], we would however hit another barrier at$\begin{array} { r } { \alpha = \frac { 1 } { 2 0 } } \end{array}$when the product$\bar { X } ^ { \bullet } \bar { X } ^ { \vee }$ceases to make sense classically (i.e. in the sense of Proposition$\mathbf { A . } 9 )$. Treating this term also “by hand” in order to overcome that barrier, it would not be too difficult to make sense of (1.6) for every$\alpha > 0$. The most difficult barrier to break is the passage from$\alpha > 0$to$\alpha = 0$since there are then infinitely many products that cease to make sense classically. More precisely, it will be clear from the remainder of this section that if τ is any tree of the form$\tau = [ \bullet , \bar { \tau } ]$, then the product$\bar { X } ^ { \bullet } \bar { X } ^ { \tau }$does not make sense classically.

## 5.2 A more systematic approach

We would now like to similarly construct a process$X ^ { \aleph }$that is the limit of$X _ { \varepsilon } ^ { \aleph }$as $\varepsilon \to 0$. For$k \neq 0 ,$, it follows from the definitions that

$$
\begin{array}{r l r} & & X _ {\varepsilon , k} ^ {\mathsf {V}} (t) = i \sum_ {\ell \in \mathbf {Z}} \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} (k - \ell) \bar {X} _ {\varepsilon , \ell} ^ {\bullet} (s) X _ {\varepsilon , k - \ell} ^ {\mathsf {V}} (s) d s \\ & & = i \sum_ {\ell + m + p = k} \int_ {- \infty} ^ {t} \int_ {- \infty} ^ {s} e ^ {- k ^ {2} (t - s) - (k - \ell) ^ {2} (s - r)} (k - \ell) \\ & & \times \bar {X} _ {\varepsilon , \ell} ^ {\bullet} (s) \bar {X} _ {\varepsilon , m} ^ {\bullet} (r) \bar {X} _ {\varepsilon , p} ^ {\bullet} (r) d r d s. \end{array}
$$

At this stage, it becomes clear that a somewhat more systematic approach to the estimation of the correlations is needed. In principle, one could try the same “brute force” approach as in Proposition 5.1 and obtain exact expressions for the correlations of$\hat { X } _ { \varepsilon } ^ { \forall }$, but it rapidly becomes clear that bounding the resulting expressions is a rather boring and not very instructive task. By the time we want to construct $X ^ { \aleph }$, a brute force approach is definitely out of the question. Instead, we will now provide a more systematic approach to estimating the correlations of$X _ { \varepsilon } ^ { \tau }$for more complicated trees τ.

Although the setting is quite different, our approach is inspired by the classical construction of Feynman diagrams in perturbative quantum field theory (see for example [Pol05] for an introduction), with the heat kernel playing the role of the propagator. We will associate to any given process$X ^ { \tau }$a number of “Feynman diagrams”, that turn out in our case to be graphs with certain properties. Each of these graphs encodes a multiple sum of a multiple integral that needs to be bounded in order to ascertain the convergence of the corresponding process$X _ { \varepsilon } ^ { \tau }$to a limit. The main achievement of this section is to describe a very simple “graphical” algorithm that provides a sufficient condition for this convergence which is not too difficult to check in practice.

| Symbol | Meaning |
| --- | --- |
| $\mathcal{E}(\tau)$ | Edges of $\tau$ |
| $\mathcal{V}(\tau)$ | Vertices of $\tau$ (including leaves) |
| $\ell(\tau)$ | Leaves of $\tau$ |
| $i(\tau)$ | Inner vertices of $\tau$ |
| $\mathcal{L}^{\tau}$ | Proper integer labelling of edges of the tree $\tau$ |
| $\mathcal{T}^{\tau}$ | Ordered real labelling of vertices of the tree $\tau$ |
| $\mathcal{P}^{\tau}$ | Pairings of two copies of the leaves of $\tau$ |
| $\mathcal{L}_{P}^{\tau}$ | Elements in $\mathcal{L}^{\tau} \times \mathcal{L}^{\tau}$ respecting the pairing $P$ |
| $S_{\tau}$ | Group of isometries of $\tau$ |

Table 1: Notations for various objects associated to a given tree$\tau .$

First, for a given binary tree$\tau \neq \bullet ,$we introduce the set${ \mathcal { L } } ^ { \tau }$of “proper” labellings of$\tau$which consists of all possible ways of associating to each edge e of τ a non-zero integer$L _ { e } \in \mathbf { Z } _ { \star }$, with the additional constraints that Kirchhoff’s law should be satisfied. In other words, for every node$v$that is neither the root nor a leaf, the sum of the labels of the two edges connecting v to its children should be equal to the label of the edge connecting v to its parent. For example, we have

![](images/page_49_image_4.jpg)

Given a labelling$L \in \mathcal { L } ^ { \tau }$, we also denote by$\varrho$the root vertex and by$\varrho ( L )$the sum of the labels of the edges attached to$\varrho .$(In the first example above, we would have$\varrho ( L ) = 7 . )$Each label of a proper labelling should be thought of as a “Fourier mode” and the reason behind Kirchhoff’s law is the way exponentials behave under multiplication. The precise meaning of this will soon become clear.

For a given binary tree$\tau ,$we denote by$\ell ( \tau )$the set of leaves and by$i ( \tau )$the set of inner vertices (the complement of$\ell ( \tau )$in the set$\mathcal { V } ( \tau )$of all vertices of τ). It will then be useful to introduce a labelling of the interior vertices of a binary tree by real numbers, which should this time be thought of as “times” instead of “Fourier modes”. Denoting by$\stackrel { 6 6 } { \mathop { \leq } } \underline { { \ Y } }$the canonical partial order of a rooted tree (i.e.$u \leq v$if u lies on the path from v to the root), we denote by${ \mathcal { T } } ^ { \tau }$the set of all labellings that associate to each vertex$v \in i ( \tau )$a real number$T _ { v } \in \mathbf { R }$with the constraints that $T _ { v } \leq T _ { \bar { v } } \mathrm { i f } \bar { v } \leq v .$. In our example, we have

$$
\bigvee_ {s} ^ {r} \in \mathcal {T} ^ {\forall},\tag{5.5}
$$

provided that$r \leq s$. We furthermore denote by$\mu _ { t } ^ { \tau }$the restriction of Lebesgue measure to the subset$\mathcal { T } _ { t } ^ { \tau }$of${ \mathcal { T } } ^ { \tau }$given by$\{ T _ { \varrho } \le t \}$. With this notation, the example shown in (5.5) belongs to$\mathcal { T } _ { t } ^ { \aleph }$, provided that$s \leq t .$A special case is given by$\tau = \bullet$ in which case we set$\mathcal { T } _ { t } ^ { \bullet } = \mathcal { T } ^ { \bullet } = \{ 0 \}$and$\mu _ { t } ^ { \bullet } = \delta _ { 0 }$

Denoting by$\hat { \iota } ( \tau ) = i ( \tau ) \setminus \{ \varrho \}$the set of those interior vertices of$\tau$that are not the root vertex, we define, for each$L \in \mathcal { L } ^ { \tau }$, a stochastic process$Z _ { L } ^ { \tau }$on $\{ ( t , T ) \in \mathbf { R } \times \mathcal { T } ^ { \tau } : T \in \mathcal { T } _ { t } ^ { \tau } \}$by

$$
Z _ {L} ^ {\tau} (t, T) = e ^ {- \varrho (L) ^ {2} (t - T _ {\varrho})} \left(\prod_ {v \in \hat {\iota} (\tau)} i L _ {e (v)} e ^ {- L _ {e (v)} ^ {2} | \delta T _ {e (v)} |}\right) \left(\prod_ {v \in \ell (\tau)} \bar {X} _ {L _ {e (v)}} ^ {\bullet} \left(T _ {v _ {\downarrow}}\right)\right),\tag{5.6}
$$

where$v _ { \downarrow }$denotes the parent of$v , e ( v )$denotes the edge$( v , v _ { \downarrow } )$, and$\delta T _ { e } = T _ { v } - T _ { u }$ for an edge$e = ( u , v )$

Even though the tree • has an empty edge set, we set${ \mathcal { L } } ^ { \bullet } \sim \mathbf { Z } .$<sub>?</sub> by convention, by specifying$\varrho ( L )$as an arbitrary value in$\mathbf { Z } _ { \star }$. With this convention in place, we also set

$$
Z _ {L} ^ {\bullet} (t, T) = X _ {\varrho (L)} ^ {\bullet} (t).
$$

Finally, for$L \in \mathcal { L } ^ { \tau }$, we write

$$
C _ {\varepsilon} (L) \stackrel {{\mathrm{def}}} {{=}} \prod_ {v \in \ell (\tau)} \varphi (\varepsilon L _ {e (v)}),\tag{5.7}
$$

with the additional convention$C _ { \varepsilon } ( L ) = \varphi ( \varepsilon \varrho ( L ) )$for$L \in \mathcal L ^ { \bullet }$

With all of these notations at hand, we then have the following identity:

Proposition 5.5 For every binary tree τ and every index$k \neq 0 ,$, one has the identity

$$
X^{\tau}_{\varepsilon ,k}(t) = \sum_{\substack{L\in \mathcal{L}^{\tau}\\ \varrho (L) = k}}C_{\varepsilon}(L)\int_{\mathcal{T}_{t}^{\tau}}Z^{\tau}_{L}(t,T)  \mu_{t}^{\tau}(dT)  .\tag{5.8}
$$

Proof. We proceed by induction over the set of all binary trees, taking as induction parameter the number of leaves of τ. The identity is true by definition if$\tau = \bullet$. If $\tau \neq \bullet .$, we can always write${ \boldsymbol { \tau } } = [ \kappa , { \bar { \kappa } } ]$, where κ and κ¯ are trees that have less leaves than τ, so that we assume that the identity (5.8) holds true when$\tau$is replaced by either κ or$\bar { \kappa } .$.

We then have the identity

$$
\begin{array}{r}X^{\tau}_{\varepsilon ,k}(t) = \sum_{\ell +m = k}\int_{s\leq t}e^{-k^{2}|t - s|}\bar{X}^{\kappa}_{\varepsilon ,\ell}(s)\bar{X}^{\bar{\kappa}}_{\varepsilon ,m}(s)ds\\ = \sum_{\ell +m = k}\sum_{\substack{L\in \mathcal{L}^{\kappa}\\ \varrho (L) = \ell}}\sum_{\substack{\bar{L}\in \mathcal{L}^{\bar{\kappa}}\\ \varrho (\bar{L}) = m}}C_{\varepsilon}(L)C_{\varepsilon}(\bar{L}) \end{array}
$$

$$
\times \int_ {s \leq t} (i \ell) (i m) e ^ {- k ^ {2} | t - s |} Z _ {L} ^ {\kappa} (s, T) Z _ {\bar {L}} ^ {\bar {\kappa}} (s, \bar {T}) \mu_ {s} ^ {\kappa} (d T) \mu_ {s} ^ {\bar {\kappa}} (d \bar {T}) d s,
$$

where we used the induction hypothesis and the fact that$k = \ell + m$to go from the first to the second line. Note now that one has the following simple facts:

• For${ \boldsymbol { \tau } } = [ \kappa , { \bar { \kappa } } ]$, there is a natural bijection$K \colon \mathcal { L } ^ { \kappa } \times \mathcal { L } ^ { \bar { \kappa } }  \mathcal { L } ^ { \tau }$as follows. Given$L \in \mathcal { L } ^ { \kappa }$and$\bar { L } \in \mathcal { L } ^ { \bar { \kappa } }$, one identifies the edges of κ and κ¯ with the corresponding subset of the edges of$\tau$and uses the labels$L$and$\bar { L }$to label them. One then labels the two edges connecting the root of$\tau$to κ and κ¯ by $\varrho ( L )$and$\varrho ( \bar { L } )$respectively. Note that thanks to our convention for$\mathcal { L } ^ { \bullet }$, this recipe also yields a bijection when one of the trees is the trivial tree.

• For${ \boldsymbol { \tau } } = [ \kappa , { \bar { \kappa } } ]$and$s \in \mathbf { R } .$, there is a natural map$\bar { K } _ { s } \colon \mathcal { T } _ { s } ^ { \kappa } \times \mathcal { T } _ { s } ^ { \bar { \kappa } }  \mathcal { T } _ { s } ^ { \tau }$ obtained by associating s to the root vertex of τ, but otherwise leaving the labels of the interior vertices of κ and κ¯ untouched. Furthermore, one has the disintegration

$$
\int_ {\mathcal {T} _ {t} ^ {\tau}} F (T) \mu_ {t} ^ {\tau} (d T) = \int_ {- \infty} ^ {t} \int_ {\mathcal {T} _ {s} ^ {\kappa}} \int_ {\mathcal {T} _ {s} ^ {\bar {\kappa}}} F (\bar {K} _ {s} (T, \bar {T})) \mu_ {s} ^ {\kappa} (d T) \mu_ {s} ^ {\bar {\kappa}} (d \bar {T}) d s,
$$

for every integrable function$F \colon  { \mathcal { T } } _ { t } ^ { \tau } \to \mathbf { R }$

As a consequence, we can rewrite the desired identity (5.8) as

$$
\begin{array}{l}X^{\tau}_{\varepsilon ,k}(t) = \sum_{\ell +m = k}\sum_{\substack{L\in \mathcal{L}^{\kappa}\\ \varrho (L) = \ell}}\sum_{\substack{\bar{L}\in \mathcal{L}^{\bar{\kappa}}\\ \varrho (\bar{L}) = m}}C_{\varepsilon}(K(L,\bar{L}))\\ \times \int_{s\leq t}Z^{\kappa}_{K(L,\bar{L})}(\bar{K}_{s}(T,\bar{T}))  \mu^{\kappa}_{s}(dT)  \mu^{\bar{\kappa}}_{s}(d\bar{T})  ds  . \end{array}
$$

However, it follows from the definition (5.6) of$Z$and from the definition of the isometry K that one has the identity

$$
Z _ {K (L, \bar {L})} ^ {\tau} (t, \bar {K} _ {s} (T, \bar {T})) = i k e ^ {- k ^ {2} | t - s |} Z _ {L} ^ {\kappa} (s, T) Z _ {\bar {L}} ^ {\bar {\kappa}} (s, \bar {T}),
$$

whenever${ \boldsymbol { \tau } } = [ \kappa , { \bar { \kappa } } ]$and$L _ { \varrho } + \bar { L } _ { \varrho } = k$. Our conventions are set up in such a way that this is true even if some of the trees involved are the trivial tree. Since one has furthermore the identity$C _ { \varepsilon } ( K ( L , \bar { L } ) ) = C _ { \varepsilon } ( L ) C _ { \varepsilon } ( \bar { L } )$, the claim follows.□

The computation of the correlations of$X _ { \varepsilon } ^ { \tau }$is thus reduced to the computation of the correlations of$Z _ { L } ^ { \tau }$, even though these then have to be integrated over$\mathcal { T } _ { t } ^ { \tau }$and summed over$L ,$, which is potentially no easy task.

In order to compute correlations of polynomials of Gaussian random variables, a useful notion is that of a pairing of a set$T$with$| T | \in 2 \mathbf { N }$. We first denote the set of all possible pairs of$T$by$S _ { 2 } ( T ) \stackrel { \mathrm { d e f } } { = } \{ A \subset T : | A | = 2 \}$. With this notation, the set of all pairings of$T$is given by

$$
\mathcal {P} (T) \stackrel {{\text { def }}} {{=}} \left\{P \subset \mathcal {S} _ {2} (T): \bigcup P = T \& p \cap q = \emptyset \forall p \neq q \in P \right\}.
$$

In other words,$\mathcal { P } ( T )$consists of all partitions of$T$that are made up of pairs. By definition,$\mathcal { P } ( T ) = \emptyset$whenever$| T |$is odd.

Since we want to estimate second moments of the processes$Z _ { L } ^ { \tau }$, the relevant notion of pairing arising from Wick’s theorem will be that of a pairing of two copies of the leaves of a binary tree τ. We thus introduce the shorthand notation

$$
\mathcal {P} ^ {\tau} = \mathcal {P} (\ell (\tau) \sqcup \ell (\tau)).
$$

See (5.12) below for a graphical representation of an element of${ \mathcal { P } } ^ { \tau }$for$\tau = \mathbb { Y }$

Definition 5.6 Given two labellings$L , \bar { L } \in \mathcal { L } ^ { \tau }$, we denote by$L \sqcup { \bar { L } }$the map

$$
(L \sqcup \bar {L}) \colon \mathcal {E} (\tau) \sqcup \mathcal {E} (\tau) \to \mathbf {Z},
$$

which restricts to$L$(respectively$\bar { L } )$on the first (respectively second) copy of${ \mathcal { E } } ( \tau )$ Here,${ \mathcal { E } } ( \tau )$denotes the set of edges of the binary tree$\tau .$

Definition 5.7 Given a pairing$P \in \mathcal { P } ^ { \tau }$and$L , \bar { L } \in \mathcal { L } ^ { \tau }$, we say that$L \sqcup { \bar { L } }$is adapted to the pairing$P \operatorname { i f }$

$$
(L \sqcup \bar {L}) _ {e (u)} + (L \sqcup \bar {L}) _ {e (v)} = 0, \quad \forall \{u, v \} \in P.\tag{5.9}
$$

We denote by$\mathcal { L } _ { P } ^ { \tau }$the set of all labellings of the form$L \sqcup { \bar { L } }$that are adapted to$P .$

Remark 5.8 Since$\begin{array} { r } { \varrho ( L ) = \sum _ { v \in \ell ( \tau ) } L _ { e ( v ) } } \end{array}$, it follows from the definition that one automatically has the identity$\varrho ( L ) + \varrho ( \bar { L } ) = 0 \mathrm { i f } L \sqcup \bar { L } \in \mathcal { L } _ { P } ^ { \tau }$. As a consequence, for every$\hat { L } = L \sqcup \bar { L } \in \mathcal { L } _ { P } ^ { \tau }$, the quantity$| \varrho ( \hat { L } ) |$is well-defined by$| \varrho ( \hat { L } ) | = | \varrho ( L ) | =$ $| \varrho ( \bar { L } ) |$

Given an inner node$u \in i ( \tau )$, we denote by$D ( u ) = \{ v \in \ell ( \tau ) : u \leq v \}$the set of its descendants. In the case where two copies of a tree are considered, we extend this definition in the natural way. A very important remark is the following:

Lemma 5.9 One has$\mathcal { L } _ { P } ^ { \tau } \neq \emptyset$ifand only if,for every inner node u$\iota \in i ( \tau ) \sqcup i ( \tau )$ there exists at least one pair$\{ v , { \bar { v } } \} \in P$such that$v \in D ( u )$and$\bar { v } \notin D ( u )$

Proof. To see that the condition is necessary, we note that if it fails, there exists at least one inner node u such that all of its descendants are paired together. It then follows from (5.9) and the definition of a proper labelling that$L _ { e ( u ) } = 0$, which is excluded.

To see sufficiency, we can construct$( L , { \bar { L } } )$as follows. First, we order the pairs in$P ,$so that each one is assigned a strictly positive integer$p ,$and we label the pth pair by$( 3 ^ { p } , - 3 ^ { p } )$. The claim now follows form the fact that a sum of the form $\scriptstyle \sum _ { p = 0 } ^ { n } a _ { p } 3 ^ { p }$with$a _ { p } \in \{ - 1 , 0 , 1 \}$vanishes if and only if all the$a _ { p }$vanish. (This can be seen by expressing the number$\textstyle \sum _ { p = 0 } ^ { n } ( a _ { p } + 1 ) 3 ^ { p }$in basis 3.)□

Remark 5.10 We can introduce an equivalence relation on nodes of τ by setting $u \sim v$if and only if$u _ { \downarrow } = v _ { \downarrow }$, i.e. if u and v share the same parent. As a consequence of Lemma 5.9, we then note that if$P \in \mathcal { P } ^ { \tau }$contains a pair$\{ u , v \}$with$u \sim v$, then $\mathcal { L } _ { P } ^ { \tau } = \emptyset$

The importance of knowing for which pairings$P$one has$\mathcal { L } _ { P } ^ { \tau } \neq \emptyset$is illustrated by the following result:

Lemma 5.11 Let τ be a binary tree and let L,$\bar { L } \in \mathcal { L } ^ { \tau } , T \in \mathcal { T } _ { t } ^ { \tau }$and$\bar { T } \in \mathcal { T } _ { \bar { t } } ^ { \tau }$ Then,$\mathbf { E } Z _ { L } ^ { \tau } ( t , T ) Z _ { \bar { L } } ^ { \tau } ( \bar { t } , \bar { T } ) \neq 0$ifand only ifthere exists at least one pairing$P \in \bar { \mathcal { P } } ^ { \tau }$ such that$L \sqcup { \bar { L } } \in { \mathcal { L } } _ { P } ^ { \tau }$

Proof. It follows from (5.6) that, up to a non-vanishing numerical factor (that still depends on$\tau , t , \bar { t } , T$and$\bar { T }$but is not random), one has

$$
Z _ {L} ^ {\tau} (t, T) Z _ {\bar {L}} ^ {\tau} (\bar {t}, \bar {T}) \propto \prod_ {u, v \in \ell (\tau)} \bar {X} _ {L _ {e (u)}} ^ {\bullet} (T _ {u _ {\downarrow}}) \bar {X} _ {\bar {L} _ {e (v)}} ^ {\bullet} (\bar {T} _ {v _ {\downarrow}}).
$$

Writing${ \hat { L } } = L \sqcup { \bar { L } }$and similarly${ \hat { T } } = T \sqcup { \bar { T } }$, it then follows from (5.2) that

$$
\mathbf {E} Z _ {L} ^ {\tau} (t, T) Z _ {\bar {L}} ^ {\tau} (\bar {t}, \bar {T}) \propto \sum_ {P \in \mathcal {P} ^ {\tau}} \prod_ {\{u, v \} \in P} \mathbf {E} \bar {X} _ {\hat {L} _ {e (u)}} ^ {\bullet} (\hat {T} _ {u _ {\downarrow}}) \bar {X} _ {\hat {L} _ {e (v)}} ^ {\bullet} (\hat {T} _ {v _ {\downarrow}}).\tag{5.10}
$$

This shows that the condition is necessary since, by (5.1), the terms in this product are all non-vanishing if and only if$\hat { L } \in \mathcal L _ { P } ^ { \tau }$. Its sufficiency is then a consequence of the positivity of (5.1).□

We finally introduce a notion of isometry of a tree τ that will be useful to identify terms that yield identical contributions.

Definition 5.12 Denote by$\mathcal { V } ( \tau ) = i ( \tau ) \sqcup \ell ( \tau )$the set of all vertices of τ. A bijection $\sigma { : \mathcal { V } ( \tau ) } \to \mathcal { V } ( \tau )$is called an isometry of$\tau \mathrm { i f } \ v \sim u$if and only if$\sigma ( u ) \sim \sigma ( v )$ with$^ { 6 6 } \sim \ '$as in Remark 5.10. In other words, it is an isometry if it preserves “family relations”. We denote by$S _ { \tau }$the group of all isometries of$\tau$.

Remark 5.13 Any isometry$\sigma$extends in a natural way to${ \mathcal { E } } ( \tau )$by$\sigma ( u , v ) =$ $( \boldsymbol { \sigma } ( u ) , \boldsymbol { \sigma } ( v ) )$, where the definition of an isometry ensures that the object on the right is again an edge of$\tau .$

Remark 5.14 The tree$\updownarrow _ { \updownarrow }$contains only one non-trivial isometry, which is the one that exchanges the two top leaves. The tree$\mathbb { V }$on the other hand contains many more isometries since one can also exchange the two branches attached to the root for example.

As a consequence, there are natural actions of$S _ { \tau }$on${ \mathcal { L } } ^ { \tau }$and${ \mathcal { T } } ^ { \tau }$by

$$
\left(\sigma L\right) _ {e} = L _ {\sigma^ {- 1} e}, \quad \left(\sigma T\right) (v) = T (\sigma^ {- 1} v),
$$

for$L \in \mathcal { L } ^ { \tau }$and$T \in \mathcal { T } ^ { \tau }$. There is also a natural action of$S _ { \tau } \times S _ { \tau }$on${ \mathcal { P } } ^ { \tau }$by

$$
\hat {\sigma} P = \left\{\left\{\hat {\sigma} u, \hat {\sigma} v \right\}: \left\{u, v \right\} \in P \right\},
$$

where we interpret elements in$S _ { \tau } \times S _ { \tau }$as bijections of$\ell ( \tau ) \sqcup \ell ( \tau )$. Note that$\mathcal { L } _ { P } ^ { \tau }$ is covariant under this action in the sense that, for$\sigma , { \bar { \sigma } } \in S _ { \tau } .$, one has

$$
L \sqcup \bar {L} \in \mathcal {L} _ {P} ^ {\tau} \quad \Leftrightarrow \quad (\sigma L) \sqcup (\bar {\sigma} \bar {L}) \in \mathcal {L} _ {(\sigma \times \bar {\sigma}) P} ^ {\tau}.
$$

For every binary tree τ, every$P \in \mathcal { P } ^ { \tau }$, and every$\hat { L } \in \mathcal L _ { P } ^ { \tau }$, we now define a quantity$\mathcal { K } ^ { \tau } ( P , \hat { L } ; \delta )$, which will be the basic building block for computing the correlations of$X _ { \varepsilon } ^ { \tau }$, by

$$
\begin{array}{l} \mathcal {K} ^ {\tau} (P, \hat {L}; \delta) \stackrel {{\text { def }}} {{=}} \int_ {\mathcal {T} _ {0} ^ {\tau}} \int_ {\mathcal {T} _ {\delta} ^ {\tau}} e ^ {- \varrho (\hat {L}) ^ {2} (\delta - T _ {\varrho} - \bar {T} _ {\bar {\varrho}})} \left(\prod_ {v \in \hat {t} (\tau) \sqcup \hat {t} (\tau)} \hat {L} _ {e (v)} e ^ {- \hat {L} _ {(v)} ^ {2} (\hat {T} _ {v _ {\downarrow}} - \hat {T} _ {v})}\right) \\ \times \left(\prod_ {\{u, v \} \in P} e ^ {- \hat {L} _ {e (v)} ^ {2} | \hat {T} _ {u _ {\downarrow}} - \hat {T} _ {v _ {\downarrow}} |}\right) \mu_ {\delta} ^ {\tau} (d T)   \mu_ {0} ^ {\tau} (d \bar {T}), \end{array} \tag {5}\tag{5.11}
$$

where we used the shorthand notation${ \hat { T } } = T \sqcup { \bar { T } }$and where we denoted by$\varrho$and $\bar { \varrho }$the two copies of the root of$\tau .$. For v belonging to one of the two copies of the original tree$\tau _ { \ast }$we again denote by$v _ { \downarrow }$its parent and by$e ( v )$the edge that connects it to its parent. On the second line, we could of course have written$\hat { L } _ { e ( u ) }$instead of $\hat { L } _ { e ( v ) }$since, by the definition of$\mathcal { L } _ { P } ^ { \tau }$, they only differ by a sign.

One then has the following fact:

$$
\text { Lemma   5.15   For   every   } \hat {\sigma} \in S _ {\tau} \times S _ {\tau}, \text {   one   has   } \mathcal {K} ^ {\tau} (\hat {\sigma} P, \hat {\sigma} \hat {L}; \cdot) = \mathcal {K} ^ {\tau} (P, \hat {L}; \cdot).
$$

Proof. It suffices to notice that the integrand is preserved under isometries, provided that one also applies it to$T \sqcup { \bar { T } }$. The claim now follows from the fact that isometries leave$\mu _ { t } ^ { \tau }$invariant.□

We are now almost ready to state the main result in this section. Before we do so however, we still need to introduce one final notation. Given a tree τ and a pairing $P \in \mathcal { P } ^ { \tau }$, we denote by$\ell _ { \ell } ^ { P } ( \tau )$the set of leaves in$\ell ( \tau ) \sqcup \ell ( \tau )$with the property that, for every$v \in \ell _ { \ell } ^ { P } ( \tau )$, there exists a pair$\{ u , \bar { u } \} \in P$such that$v \in \{ u , \bar { u } \}$and such that the parent of u is equal to the grandparent of u¯. (In terms of genealogy, $\ell _ { \ell } ^ { P } ( \tau )$contains all pairings between a nephew and his uncle.) For example, in the following pairing of the tree$\updownarrow ,$the set$\ell _ { \ell } ^ { \bar { P } } ( \tau )$consists of exactly two leaves that are distinguished by being filled with white:

![](images/page_54_image_13.jpg)

(5.12)

Given any two labellings$L , \bar { L } \in \mathcal { L } _ { P } ^ { \tau }$, we then write$L \stackrel { P } { \sim } \bar { L } \mathrm { i f } | L _ { e ( v ) } | = | \bar { L } _ { e ( v ) } |$for all$v \in \ell ( \tau ) \sqcup \ell ( \tau )$and furthermore$\bar { L } _ { e ( v ) } = \bar { L } _ { e ( v ) }$for all$v \in ( \ell ( \tau ) \sqcup \ell ( \tau ) ) \setminus \ell _ { \ell } ^ { P } ( \tau )$ In other words, L and L<sup>¯</sup> are only allowed to differ by changing the signs of the labels adjacent to$\ell _ { \ell } ^ { P } ( \tau )$. This allows to define a “symmetrised” kernel$\mathcal { K } _ { \mathrm { { s y m } } } ^ { \tau }$by

$$
\mathcal {K} _ {\text { sym }} ^ {\tau} (P, L; \delta) \stackrel {{\text { def }}} {{=}} \frac {1}{| [ L ] _ {P} |} \sum_ {\bar {L} \sim L} ^ {P} \mathcal {K} ^ {\tau} (P, \bar {L}; \delta)  ,
$$

where$[ L ] _ { P }$denotes the equivalence class of L under$\overset { P } { \sim }$and$\left| \cdot \right|$denotes its cardinality.

With this final notation at hand, the main result of this section is the following:

Theorem 5.16 For a given$\tau \in \mathcal { T } _ { 2 } \setminus \{ \bullet \}$, if there exist$\alpha > 0$and$\beta \in ( 0 , 1 )$such that, for every$P \in \mathcal { P } ^ { \tau } / ( S _ { \tau } \times S _ { \tau } )$

$$
\sum_ {\hat {L} \in \mathcal {L} _ {P} ^ {\tau}} \sup _ {\delta \in \mathbf {R}} | \varrho (\hat {L}) | ^ {2 \alpha} | \mathcal {K} _ {\mathrm{sym}} ^ {\tau} (P, \hat {L}; \delta) | <   \infty ,\tag{5.13a}
$$

$$
\sum_ {\hat {L} \in \mathcal {L} _ {P} ^ {\tau}} \sup _ {| \delta | \leq 1} \frac {| \mathcal {K} _ {\mathrm{sym}} ^ {\tau} (P , \hat {L} ; 0) - \mathcal {K} _ {\mathrm{sym}} ^ {\tau} (P , \hat {L} ; \delta) |}{\delta^ {2 \beta}} <   \infty  ,\tag{5.13b}
$$

then the sequence of processes$X _ { \varepsilon } ^ { \tau }$converges to a limit$X ^ { \tau }$in probability in $\mathcal { C } ( [ 0 , T ] , \mathcal { C } ^ { \gamma } ) \cap \mathcal { C } ^ { \delta } ( [ 0 , T ] , \mathcal { C } ) ,$, provided that$\gamma <$< α and$\delta < \beta .$

Proof. This is a rather straightforward application of Proposition A.2. Without loss of generality, we can assume that$\alpha \leq 1$, since otherwise it suffices to consider the appropriate derivative of$X _ { \varepsilon } ^ { \tau }$. We first introduce an equivalence relation ∼ on${ \mathcal { L } } ^ { \tau }$ by stipulating that$L \sim \bar { L }$if and only if$| L _ { e ( v ) } | = | \bar { L } _ { e ( v ) } |$for every$v \in \ell ( \tau )$and $\varrho ( L ) = \varrho ( \bar { L } )$). We then define a symetrised family of processes$F _ { L }$by

$$
F _ {L} (t) = \frac {1}{| [ L ] |} \sum_ {\bar {L} \in [ L ]} \int_ {\mathcal {T} _ {t} ^ {\tau}} Z _ {\bar {L}} ^ {\tau} (T) \mu_ {t} ^ {\tau} (d T),
$$

where we denote by [L] the equivalence class of L under$\sim _ { \ast }$. Writing furthermore $g _ { L } ( x ) = e ^ { i \varrho ( L ) x }$and noting that both$C _ { \varepsilon } ( L ) = C _ { \varepsilon } ( \bar { L } )$and$g _ { L } = g _ { \bar { L } }$for$L \sim \bar { L }$by definition, it then follows from Proposition 5.5 that

$$
X _ {\varepsilon} ^ {\tau} (x, t) = \sum_ {L \in \mathcal {L} ^ {\tau}} C _ {\varepsilon} (L) F _ {L} (t) g _ {L} (x),
$$

so that we are precisely in the framework considered in Proposition A.2, provided that we set${ \mathcal { J } } = { \mathcal { L } } ^ { \tau }$for our index set.

With these notations at hand, it then follows from (5.6), Proposition 5.2, and the definition of$\mathcal { K } ^ { \tau }$that

$$
\mathbf {E} F _ {L} (t) F _ {L ^ {\prime}} (t ^ {\prime}) = \frac {1}{| [ L ] | | [ L ^ {\prime} ] |} \sum_ {\stackrel {\bar {L} \in [ L ]} {\bar {L} ^ {\prime} \in [ L ^ {\prime} ]}} \sum_ {P \in \mathcal {P} ^ {\tau}} \mathbf {1} _ {\bar {L} \sqcup \bar {L} ^ {\prime} \in \mathcal {L} _ {P} ^ {\tau}} \mathcal {K} ^ {\tau} (P, \bar {L} \sqcup \bar {L} ^ {\prime}; t - t ^ {\prime})\tag{5.14}
$$

Note now that if$\bar { L } \sqcup \bar { L } ^ { \prime } \stackrel { P } { \sim } L \sqcup L ^ { \prime }$then, by the definition of$\sim ,$one also has$\bar { L } \sim L$ and$\bar { L } ^ { \prime } \sim L ^ { \prime }$. As a consequence, we can replace$\kappa$by${ \kappa } _ { \mathrm { s y m } }$in (5.14), so that the claim follows Proposition A.2, noting that we can restrict ourselves to equivalence classes of${ \mathcal { P } } ^ { \tau }$under isometries by Lemma 5.15.□

Remark 5.17 Of course, since$\mathcal { K } _ { \mathrm { { s y m } } } ^ { \tau }$is constructed from a finite number of copies of$\kappa ^ { \tau }$, we also have the same criterion with$\kappa ^ { \tau }$instead. However, it turns out that in some of the situations that we are lead to consider,$\kappa ^ { \tau }$fails to satisfy (5.13), while $\mathcal { K } _ { \mathrm { { s y m } } } ^ { \tau }$does, due to some cancellations.

## 5.3 Reduction to simpler trees

There is one situation in which the estimate of$K _ { \mathrm { s y m } } ^ { \tau } ( P , \cdot ; \cdot )$for one tree can benefit from bounds on a simpler tree. This is when we consider a tree$\bar { \tau }$of the form $\bar { \boldsymbol { \tau } } = [ \boldsymbol { \tau } , \bullet ]$and a pairing$\bar { P }$consisting of pairing the two copies of$\tau$according to some pairing$P \in \mathcal { P } ^ { \tau }$and then pairing the two remaining leaves. We denote by$\mathcal { P } _ { s } ^ { \bar { \tau } }$ the set of all such pairings.

In this case, we have:

Proposition 5.18 Let$\bar { \tau }$and$\bar { P } \in \mathcal { P } _ { s } ^ { \bar { \tau } }$be as above and assume that the bound $( 5 . I 3 a )$holdsfor$K _ { \mathrm { s v m } } ^ { \tau } ( P , \cdot ; \cdot )$with some$\alpha \geq 0 .$. Then, the bounds (5.13) holdfor ${ \mathcal { K } } _ { \mathrm { s y m } } ^ { \bar { \tau } } ( \bar { P } , \cdot ; \cdot )$with$\bar { \alpha } < \frac { 3 } { 2 } \wedge ( \alpha + \frac { 1 } { 2 } )$and$\hat { \beta } < \frac { 1 \wedge \hat { \alpha } } { 2 }$

Proof. Let$L \in \mathcal { L } _ { P } ^ { \tau }$be a labelling with$\varrho ( L ) = k$. Then, for every$m \in \mathbf { Z } _ { \star }$, we can construct a corresponding labelling$\bar { L } \in \mathcal L _ { \bar { P } } ^ { \bar { \tau } }$with$\varrho ( \bar { L } ) = m$by labelling the two paired copies of$\tau$according to$L ,$using the labels$( k , - k )$for the edges joining the roots of the copies of$\tau$to the roots of the copies of$\bar { \tau } .$, and assigning the labels $( m - k , k - m )$to the two remaining edges. With this notation, it follows from the definition of$\mathcal { K } _ { \mathrm { { s y m } } } ^ { \tau }$that we have the identity

$$
\mathcal {K} _ {\mathrm{sym}} ^ {\bar {\tau}} (\bar {P}, \bar {L}; \delta) = k ^ {2} \int_ {- \infty} ^ {0} \int_ {- \infty} ^ {\delta} \mathcal {K} _ {\mathrm{sym}} ^ {\tau} (P, L, s - s ^ {\prime}) e ^ {- (k - m) ^ {2} | s - s ^ {\prime} | - m ^ {2} (\delta - s - s ^ {\prime})} d s d s ^ {\prime}.
$$

In particular, it follows from Lemma$\mathrm { A } . 7$that

$$
\begin{array}{c} \mathcal {K} _ {\mathrm{sym}} ^ {\bar {\tau}} (\bar {P}, \bar {L}; 0) \lesssim \frac {k ^ {2} \| \mathcal {K} _ {\mathrm{sym}} ^ {\tau} (P , L ; \cdot) \| _ {\infty}}{m ^ {2} (k ^ {2} + m ^ {2})}  , \\ | \mathcal {K} _ {\mathrm{sym}} ^ {\bar {\tau}} (\bar {P}, \bar {L}; \delta) - \mathcal {K} _ {\mathrm{sym}} ^ {\bar {\tau}} (\bar {P}, \bar {L}; 0) | \lesssim (1 \wedge \delta m ^ {2}) \frac {k ^ {2} \| \mathcal {K} _ {\mathrm{sym}} ^ {\tau} (P , L ; \cdot) \| _ {\infty}}{m ^ {2} (k ^ {2} + m ^ {2})}  . \end{array}
$$

For$\alpha \geq 1$, the numerators of these expressions are summable by assumption, so that the corresponding bound holds. For$\alpha \leq 1$, we use the bound

$$
\frac {k ^ {2}}{m ^ {2} (k ^ {2} + m ^ {2})} \leq \frac {k ^ {2 \alpha}}{m ^ {2 + 2 \alpha}},
$$

so that the claim follows at once.

## 5.4 General summability criterion

In this section, we introduce a graphical criterion to verify whether$\mathcal { K } _ { \mathrm { s y m } } ^ { \tau }$satisfies the bounds of Theorem 5.16 for a given pairing$P \in \mathcal { P } ^ { \tau }$. Our criterion consists of two steps: in a first step, we associate to a given pair$( \tau , P )$a family of weighted graphs$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$. Elements of$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$all share the same underlying graph and only differ by the weights given to their edges. In a second step, we need to check that $\mathcal { G } _ { \kappa } ^ { \tau } ( P )$contains at least one element that can be reduced to a loop-free graph by a certain reduction procedure.

The weighted graphs in$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$are built in several steps in the following way.

1. Construction of the underlying graph. Informally, we build a graph$( { \mathcal { G } } , { \mathcal { E } } )$by taking two disjoint copies of$\tau ,$joining all the vertices that belong to the same pair of$P _ { \mathrm { { : } } }$, as well as the two roots, and then erasing all “superfluous” vertices that only have two incoming edges. We will also henceforth denote by$\tau \subset \mathcal { E }$the spanning tree given by the interior edges of the two copies of the original tree$\tau$, together with the new edge e¯ connecting the two roots.

Example 5.19 For a typical pairing ofthe tree$\updownarrow ,$, we obtain thefollowing graph, where some oriented pairing P is depicted on the left (with two nodes belonging to P ifthey are connected by a black arc) and the corresponding oriented graph$( { \mathcal { G } } , { \mathcal { E } } )$ is depicted on the right, with the spanning tree T drawn in grey and the glued edges in black:

![](images/page_57_image_5.jpg)

The distinguished edge e¯joining the two copies of the root vertex is drawn as a thicker grey line.

(5.15)

Formally, this can be achieved by setting$\mathcal { G } = ( \mathcal { V } ( \tau ) \sqcup \mathcal { V } ( \tau ) ) / \overset { P } { \approx }$and

$$
\mathcal {E} = \left\{(\varrho , \bar {\varrho}) \right\} \cup (\mathcal {E} (\tau) \sqcup \mathcal {E} (\tau)) / \stackrel {{P}} {{\approx}},
$$

where$\mathcal { V } ( \tau )$and${ \mathcal { E } } ( \tau )$are the vertex (resp. edge) set of$\tau$and$\varrho$and$\bar { \varrho }$are the two copies of the root. We will henceforth use the shorthand$\bar { e } = ( \varrho , \bar { \varrho } )$for the distinguished edge connecting the two roots, as this will sometimes play a special role.

Here, the equivalence relation$\overset { P } { \approx }$is defined on$\mathcal { V } ( \tau ) \sqcup \mathcal { V } ( \tau )$by setting$u \overset { P } { \approx } v _ { \downarrow }$ and$v \stackrel { P } { \approx } u _ { \downarrow }$for every pair$( u , v ) \in P$. This then induces a natural equivalence relation on the edge set by$( u , u _ { \downarrow } ) \overset { P } { \approx } ( v , v _ { \downarrow } )$. Since$\tau$is a binary tree, every vertex of the graph$( { \mathcal { G } } , { \mathcal { E } } )$constructed in this way is of degree exactly 3. It inherits the ordering of$\tau .$, but this ordering does not extend to the edges “glued” by$\stackrel { P } { \approx } ,$, since they are always glued in “opposite directions”. However, if we order the pairs in$P .$ then this naturally defines an ordering on all of E.

2. Temporarily weigh edges. Build a weighting$\bar { \mathcal { L } } _ { 0 } { : } \mathcal { E }  \mathbf { R }$of the graph by giving the weight κ to the edge e¯ connecting the two roots, the weight −1 to the remaining edges in T, and the weight 0 to the remaining edges in${ \mathcal { E } } \setminus { \mathcal { T } }$

3. Treat small loops. It turns out that occurrences of certain small loops (a pair of vertices connected by two edges) cause summability problems that have to be cured by a special procedure.

There are two types of such loops: either one of its edges belongs to$\tau$(let’s call these “type 1”), or both of its edges belong to$\mathcal { E } \setminus \mathcal { T } ( ^ { \bullet \bullet } \mathrm { t y p e ~ 2 ^ { \cdot \bullet } ) }$. Loops of the first kind are the only “dangerous” ones, and they are handled by the following special procedure. For each such loop, we shift a weight$\frac 1 3$into the loop from one of its adjacent edges. More precisely, we build a weight$\mathcal { L } _ { 0 }$from$\bar { \mathcal { L } } _ { 0 }$by performing the substitution

![](images/page_58_image_4.jpg)

Note that the small loop appearing in the example (5.15) is of type 1. It does not matter which one of the two adjacent edges we shift the weights to.

4. Finalise the weights of the edges. We now finally construct the family$\mathcal { G } _ { \kappa } ^ { \tau }$of weightings of the graph$( { \mathcal { G } } , { \mathcal { E } } )$. Denote by$\mathcal { L } _ { 0 } { : } \mathcal { E }  \mathbf { R }$the weighting obtained at the end of the previous step and denote by$W : { \mathcal { G } } \to \mathbf { R } _ { + }$the map defined by$\mathcal { W } ( v ) = 0$ for$v \in \bar { e }$and$\mathcal { W } ( v ) = 2$otherwise. In other words, we associate a weight 2 to every vertex except the two roots.

Define now$\mathcal { E } _ { 0 } = \emptyset$and$\mathcal { G } _ { 0 } = \emptyset$and recursively construct subsets$\mathcal { E } _ { n } ~ \subset ~ \mathcal { E }$ and$\mathcal { G } _ { n } \subset \mathcal { G }$in the following way. Assuming that${ \mathcal { E } } _ { n }$and${ \mathcal { G } } _ { n }$have already been constructed and that${ \mathcal { L } } _ { n }$has been defined, we pick an arbitrary vertex$v \in \mathcal G \setminus \mathcal G _ { n }$ and consider the set$E _ { v } ^ { n }$of edges attached to v that are not in${ \mathcal { E } } _ { n }$. We then choose an arbitrary function$W _ { n } { \colon } E _ { v } ^ { n } \ \to \ \mathbf { R } _ { + }$with$\begin{array} { r } { \sum _ { e \in E _ { \ast } ^ { n } } W _ { n } ( e ) = \mathcal { W } ( v ) } \end{array}$and we set $\mathscr { L } _ { n + 1 } = \mathscr { L } _ { n } + W _ { n } , \mathscr { E } _ { n + 1 } = \mathscr { E } _ { n } \cup E _ { v } ^ { n } , \mathscr { G } _ { n + 1 } = \mathscr { G } _ { n } \cup \{ v \}$. The construction terminates when$\mathcal { E } _ { n } = \mathcal { E }$, and we denote the weight constructed in this way by${ \mathcal { L } } .$

Loosely speaking, we distribute the weights$" 2 "$given by W among each vertex’s neighbouring edges, with the constraint that once the weight of a given vertex has been distributed, none of its adjacent edges can receive any more weight from its other vertex.

Definition 5.20 The set$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$consists of all the possible weightings$\mathcal { L } \colon \mathcal { E }  \mathbf { R }$ that can be obtained from the procedure outlined above and that are such that $\mathcal { L } ( e ) > 0$for all edges e belonging to a small loop.

Remark 5.21 Since it will usually be advantageous to have only positive weights left, and since the elements in the original spanning tree$\tau$have weight −1 before the vertex weights are distributed, it is usually be a good idea in Step 4 to traverse vertices in$\mathcal { G }$in a way that respects the ordering of$\tau .$, i.e. from the outside of$\tau$ towards the two root vertices.

The point of this construction is that it is quite straightforward to obtain a bound on$K _ { \mathrm { s v m } } ^ { \tau } ( P , \cdot , \cdot )$from the weights in$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$, but understanding why this is so requires a few notions of elementary graph theory, which we now present.

Given an arbitrary directed graph$( { \mathcal { G } } , { \mathcal { E } } )$, we write$e \to v$for an edge e entering a vertex$v \left( \mathbf { i } . \mathbf { e } . e = \left( u , v \right) \right.$for some$u \in { \mathcal { G } } )$) and$e \gets v$for an edge e exiting v (i.e. $e = ( v , u )$for some$u \in { \mathcal { G } } )$. With this notation, the integral cycle group${ \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$ of a graph is given by all labellings$L \colon { \mathcal { E } } \to \mathbf { Z }$such that, for each vertex$v \in \mathcal G$ Kirchhoff’s law is satisfied in the sense that

$$
\sum_ {e \to v} L _ {e} = \sum_ {e \leftarrow v} L _ {e}.
$$

Note that even though we used the fact that we specified an orientation to define ${ \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$, it really does not depend on it. Indeed, if we consider two different orientations on the same graph, we should identify elements in their respective cycle groups if they agree on those edges that do not change orientation and have opposite signs on those edges that do change orientation. We also introduce a notation for the set of nowhere vanishing elements of the cycle group:

$$
\mathcal {C} _ {\star} (\mathcal {G}, \mathcal {E}) = \left\{L \in \mathcal {C} (\mathcal {G}, \mathcal {E}): L _ {e} \neq 0 \forall e \in \mathcal {E} \right\}.
$$

The reason why we introduced this notation is the following fact:

Lemma 5.22 There is a canonical identification of$\mathcal { L } _ { P } ^ { \tau }$with${ \mathcal { C } } _ { \star } ( { \mathcal { G } } , { \mathcal { E } } )$, where$( { \mathcal { G } } , { \mathcal { E } } )$ is the graph associated to τ and$P$as in Step 1 above.

Proof. Elements$L \in \mathcal { L } _ { P } ^ { \tau }$are defined on$\mathcal { E } ( \tau ) \sqcup \mathcal { E } ( \tau )$with the canonical orientation that goes from the leaves to the roots, and they do satisfy Kirchho$\mathrm { f } \mathbf { \bar { s } }$law there. Furthermore, for any two edges$e , e ^ { \prime }$that are identified under$\overset { P } { \approx }$, one has$L _ { e } =$ $L _ { e ^ { \prime } }$. As a consequence, a choice of orientation on$P$corresponds to a choice of representative in each equivalence class of$\mathcal { E } ( \tau ) \sqcup \mathcal { E } ( \tau )$under$\overset { P } { \approx }$. Denoting this choice of representative by π, we then define an element$C \in \mathcal { C } _ { \star } ( \mathcal { G } , \mathcal { E } )$by $C _ { e } = L _ { \pi ( e ) }$for$e \neq \bar { e }$and$C _ { \bar { e } } = \pm | \varrho ( L ) |$|, with the sign determined in such a way that Kirchhoff’s law also holds at the roots.□

As an abelian group,${ \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$is isomorphic to$\mathbf { Z } ^ { n }$for some$n \geq 0 ,$, called the dimension of$\mathcal { C }$. An integral basis$B \subset \mathcal { C } ( \mathcal { G } , \mathcal { E } )$then consists of exactly n elements, with the property that every element of${ \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$can be written uniquely as

$$
L = \sum_ {B \in \mathcal {B}} L _ {B} B, \qquad L _ {B} \in \mathbf {Z}.
$$

In other words, an integral basis provides a decomposition that realises the isomorphism with$\mathbf { Z } ^ { n }$

We call an element$L$of the cycle group elementary if there exists a simple cycle of$\mathcal { G }$(i.e. one traversing each edge at most once) such that$L$takes the values$\pm 1$on the edges belonging to the cycle and 0 otherwise. There are exactly two elementary elements in${ \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$for each simple cycle, one for each orientation. Finally, for any spanning tree$\tau$of a graph$( { \mathcal { G } } , { \mathcal { E } } )$, we can construct a collection$B _ { T }$of elementary cycles by considering, for each edge$e \in { \mathcal { E } } \setminus { \mathcal { T } }$, the unique (modulo orientation) cycle passing through e that otherwise only traverses edges in$\tau .$. One then has the following classical result, which can be found for example in [GR01]:

Proposition 5.23 For each spanning tree${ \mathcal { T } } o f ( { \mathcal { G } } , { \mathcal { E } } )$, the collection$B _ { T }$forms an integral basis$o f { \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$

Let now$( \mathcal { G } , \mathcal { E } , \mathcal { L } )$be a weighted graph, i.e.$\mathcal { L }$is a real-valued function over the edge set$\mathcal { E } .$. We then introduce the following definition:

Definition 5.24 A weighted graph$( \mathcal { G } , \mathcal { E } , \mathcal { L } )$is summable if

$$
\sum_ {L \in \mathcal {C} _ {\star} (\mathcal {G}, \mathcal {E})} \prod_ {e \in \mathcal {E}} | L _ {e} | ^ {- \mathcal {L} _ {e}} <   \infty .
$$

With all of these definitions in place, we are now finally ready to state the criterion for the bounds on${ \kappa } _ { \mathrm { s y m } }$announced earlier.

Theorem 5.25 Let$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$be as above and let$\kappa \in ( 0 , 2 )$. Ifthere exists an element $o f \mathcal { G } _ { \kappa } ^ { \tau } ( P )$that is summable, then the kernel$K _ { \mathrm { s y m } } ^ { \tau } ( P , \cdot )$satisfies the bounds (5.13) with$\begin{array} { r } { \alpha = 2 - \frac { \kappa } { 2 } } \end{array}$and$\beta < \frac { 1 \wedge \alpha } { 2 }$

Proof. It follows from the definition (5.11) that one can rewrite$\mathcal { K } _ { \mathrm { { s y m } } } ^ { \tau }$in a natural way as

$$
\mathcal {K} _ {\mathrm{sym}} ^ {\tau} (P, L; \delta) = \int_ {- \infty} ^ {0} \int_ {- \infty} ^ {\delta} e ^ {L _ {\varrho} ^ {2} (\delta - s - s ^ {\prime})} \mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L; s - s ^ {\prime}) d s d s ^ {\prime}.
$$

Here, the fact that$\mathcal { F } _ { \mathrm { { s y m } } } ^ { \tau }$only depends on the difference between s and$s ^ { \prime }$is a consequence of the invariance of the integrand in (5.11) under translations, but this is not relevant. Both claimed bounds then follow at once from Lemma$\mathsf { A } . 7$if we are able to show that the constants$\begin{array} { r } { \mathcal { F } _ { \mathrm { { s y m } } } ^ { \tau } ( P , L ) \stackrel { \mathrm { d e f } } { = } \operatorname* { s u p } _ { \delta } | \mathcal { F } _ { \mathrm { { s y m } } } ^ { \tau } ( P , L ; \delta ) | } \end{array}$satisfy the summability condition

$$
\sum_ {L \in \mathcal {C} _ {\star} (\mathcal {G}, \mathcal {E})} | L _ {\bar {e}} | ^ {- \kappa} \mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L) <   \infty ,\tag{5.16}
$$

where we made the slight abuse of notation of considering$L$as an element in ${ \mathcal { C } } _ { \star } ( { \mathcal { G } } , { \mathcal { E } } )$instead of$\mathcal { L } _ { P } ^ { \tau }$, which is justified by Lemma 5.22.

Denote now$\bar { \mathcal { E } } = \mathcal { E } \setminus \{ \bar { e } \}$and${ \bar { \mathcal { T } } } = { \mathcal { T } } \backslash \{ { \bar { e } } \}$. It then follows from the expression (5.11) that$\mathcal { F } _ { \mathrm { s y m } } ^ { \tau } ( P , L , \eta )$can be written as

$$
\begin{array}{l} \mathcal {F} _ {\text { sym}} ^ {\tau} (P, L; \eta) = \frac {1}{| [ L ] _ {P} |} \sum_ {\bar {L} \stackrel {{P}} {{\sim}} L} \left(\prod_ {e \in \bar {\mathcal {T}}} \bar {L} _ {e}\right) \int \exp \left(- \sum_ {e \in \bar {\mathcal {E}}} | \bar {L} _ {e} | ^ {2} | \delta T _ {e} |\right) \mu_ {\eta} (d T) \\ \stackrel {{\mathrm{def}}} {{=}} \int \mathcal {G} _ {P} ^ {\tau} (L) \mu_ {\eta} (d T). \end{array} \tag {5}\tag{5.17}
$$

Here,$\mu _ { \eta }$is the measure on$\mathbf { R } ^ { \mathcal { G } }$which fixes the vertices adjacent to e¯ to 0 and$\eta$ respectively, and is given by Lebesgue measure, restricted to$\mathcal { T } _ { 0 } ^ { \tau } \times \mathcal { T } _ { \eta } ^ { \tau }$, for the remaining components. As before,$\delta T _ { e } = T _ { v } - T _ { u }$for any edge$e = ( u , v )$

Consider now the case when the graph contains loops of type 1. By Proposition 5.23, we can assume without loss of generality that the graph$( { \mathcal { G } } , { \mathcal { E } } )$, the cycle $L ,$and the collection of “times” T are locally given by the configuration

![](images/page_61_image_4.jpg)

(5.18)

with$r \leq s ,$and$k , m \in \mathbf { Z } ,$with$k + m \neq 0 .$. The left edge necessarily belongs to $\tau$, but the right edge could be either in$\tau$or not. With this notation, let us write M for the subset of$\mathcal { E }$containing the two edges that form the loop under consideration. It then follows from (5.17) that$\mathcal { G } _ { P } ^ { \tau }$can be factored as

$$
\mathcal {G} _ {P} ^ {\tau} (L) = \frac {1}{2} \mathcal {J} _ {k, m} (s - r) \mathcal {G} _ {P, M} ^ {\tau} (L),
$$

where he prefactor$\mathcal { I }$is given by

$$
\mathcal {J} _ {k, m} (s - r) \stackrel {\mathrm{def}} {=} (k + m) e ^ {- ((k + m) ^ {2} + m ^ {2}) | s - r |} + (k - m) e ^ {- ((k - m) ^ {2} + m ^ {2}) | s - r |},
$$

and the remainder$\mathcal { G } _ { P , M } ^ { \tau }$is given by

$$
\mathcal {G} _ {P, M} ^ {\tau} (L) = \frac {1}{| [ L ] _ {P} |} \sum_ {\bar {L} \stackrel {{P}} {{\sim}} L} \Big (\prod_ {e \in \bar {\mathcal {T}} \setminus M} \bar {L} _ {e} \Big) \exp \Big (- \sum_ {e \in \bar {\mathcal {E}} \setminus M} | \bar {L} _ {(u, v)} | ^ {2} | \delta T _ {e} | \Big)  .
$$

This follows from the fact that the configuration with m replaced by$- m$in (5.18) belongs to$[ L ] _ { P }$by the definition of$\stackrel { P } { \sim } { }$, and that the factor$\mathcal { G } _ { P , M } ^ { \tau } ( L )$does not depend on m. We then have the bound

Lemma 5.26 For every$\varepsilon \in [ 0 , 1 ]$, there exist constants c and$C$such that the bound

$$
| \mathcal {J} _ {k, m} (\delta) | \lesssim e ^ {- c (m ^ {2} + (k + m) ^ {2}) \delta} | k | ^ {\varepsilon} (| m | + | k + m |) ^ {1 - \varepsilon},
$$

holdsfor all$k , m \in \mathbf { Z } ,$with$| k | \neq | m |$and for all$\delta > 0$

Proof. Using the identity

$$
a c + b d = \frac {1}{2} ((a + b) (c + d) + (a - b) (c - d)),
$$

and the fact that$\displaystyle | e ^ { - x } - e ^ { - y } | \leq ( 1 \wedge | x - y | ) e ^ { - ( x \wedge y ) }$, we obtain the bound

$$
| \mathcal {J} _ {k, m} | \leq e ^ {- (k ^ {2} + 2 m ^ {2} - 2 | k m |) | s - r |} (2 | k | + | m | (1 \wedge 4 | k m | | s - r |)).
$$

At this stage, we make use of the fact that$\mathrm { s u p } _ { x > 0 } x e ^ { - a x } \leq 1 / a$and that there exists a constant$\begin{array} { r } { c > \frac { 1 } { 3 } } \end{array}$such that$k ^ { 2 } + 2 m ^ { 2 } - 2 | k m | > c ( k ^ { 2 } + m ^ { 2 } )$. This implies that

$$
| s - r | e ^ {- (k ^ {2} + 2 m ^ {2} - 2 | k m |) | s - r |} \lesssim \frac {e ^ {- \frac {1}{3} (k ^ {2} + m ^ {2}) | s - r |}}{k ^ {2} + m ^ {2}},
$$

so that we conclude that the bound

$$
\begin{array}{r l} & {| \mathcal {J} _ {k, m} | \lesssim e ^ {- c (m ^ {2} + (k + m) ^ {2}) | s - r |} \Big (| k | + | m | \Big (1 \wedge \frac {| k m |}{k ^ {2} + m ^ {2}} \Big) \Big)} \\ & {\quad \lesssim e ^ {- c (m ^ {2} + (k + m) ^ {2}) | s - r |} \big (| k | + | m | ^ {1 - \varepsilon} | k | ^ {\varepsilon} \big),} \end{array}
$$

holds for every$\varepsilon \in [ 0 , 1 ]$. This bound is equivalent to the one in the statement.

For any$L \in \mathcal { C } _ { \star } ( \mathcal { G } , \mathcal { E } )$, denote now by$S L \colon \mathcal { E } \mathrm { ~  ~ } \mathbf { R }$the function given by $\begin{array} { r } { S L _ { e } = \left| L _ { e } \right| + \left| L _ { e ^ { \prime } } \right| } \end{array}$if the two edges e and$e ^ { \prime }$are part of a loop of type 1, and $S L _ { e } = | L _ { e } |$otherwise. The above considerations show that with this notation, there exists a constant$c > 0$such that one then has the bound

$$
\begin{array}{r l} & {\mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L; \eta) \lesssim \int \left(\prod_ {e \in \bar {\mathcal {E}}} | \mathcal {S} L _ {e} | ^ {- \mathcal {L} _ {0} (e)} e ^ {- c (\mathcal {S} L) _ {e} ^ {2} | \delta T _ {e} |}\right) \mu_ {\eta} (d T)} \\ & {\qquad \lesssim \int_ {\mathbf {R} ^ {\tilde {\mathcal {G}}}} \left(\prod_ {e \in \bar {\mathcal {E}}} | \mathcal {S} L _ {e} | ^ {- \mathcal {L} _ {0} (e)} e ^ {- c (\mathcal {S} L) _ {e} ^ {2} | \delta T _ {e} |}\right) \prod_ {u \in \bar {\mathcal {G}}} d T _ {u},} \end{array}\tag{5.19}
$$

where$\mathcal { L } _ { 0 }$is the weighting constructed in Step 3. Here, the passage from the first to the second line is trivial since the integrand is positive by construction, so that integrating over a larger domain can only increase the value of the integral. (Here, we use the convention that$T _ { u } = 0$or$\eta$respectively for$u \in \bar { e } . )$

To conclude the proof, we note that a repeated application of Holder’s inequality¨ yields the bound

$$
\int_ {\mathbf {R}} \exp \left(- \sum_ {j = 1} ^ {n} a _ {j} | x - x _ {j} |\right) \lesssim \prod_ {j = 1} ^ {m} a _ {j} ^ {- \ell_ {j}},\tag{5.20}
$$

for any$a _ { 1 } , \dotsc , a _ { n } \in \mathbf { R }$and any exponents$\ell _ { j } > 0$with$\begin{array} { r } { \sum _ { j = 1 } ^ { n } \ell _ { j } = 1 } \end{array}$. We now fix an arbitrary order on$\bar { \mathcal { G } }$and we apply (5.20) repeatedly, every time integrating over the time variable associated to the corresponding element of$\bar { \mathcal { G } }$.

Each such integration corresponds exactly to one iteration of Step 4 of the construction of$\mathcal { L } \in \mathcal { G } _ { \kappa } ^ { \tau }$. This shows that, for any of the weights$\mathcal { L } \in \mathcal { G } _ { \kappa } ^ { \tau }$, one has indeed the bound

$$
\mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L) \leq \prod_ {e \in \bar {\mathcal {E}}} | \mathcal {S} L _ {e} | ^ {- \mathcal {L} (e)}.
$$

Since$| S L _ { e } | \geq | L _ { e } |$and since we only retain weights such that$\mathcal { L } ( e ) > 0$for e belonging to a loop, the claim then follows.□

## 5.5 On the summability of graphs

As a consequence of the results in the previous subsection, the construction of $X ^ { \tau }$is now reduced to verifying the existence of a summable graph in$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$for every pairing$P \in \mathcal { P } ^ { \tau }$. It is therefore useful to have a simple criterion to check the summability of a graph. This is achieved by the following algorithm:

Algorithm 1 Apply thefollowing operations successively, until the procedure sta bilises. Edges with weight 0 are removed and consecutive edges without intermedi ate branching point are merged:

![](images/page_63_image_6.jpg)

(5.21a)

![](images/page_63_image_8.jpg)

(5.21b)

Simple loops are erased, provided that their total weight is strictly greater than 1:

![](images/page_63_image_11.jpg)

(5.22)

Small loops are “flattened”, provided that their weights α and$\beta$add to a value strictly greater than 1:

![](images/page_63_image_14.jpg)

(5.23)

with$\gamma = \alpha + \beta - 1$if α ∨$\beta < 1$, γ = α ∧ β if α ∨ β > 1, and$\gamma < \alpha \wedge \beta$if $\alpha \vee \beta = 1$

The main result of this subsection is then the following.

Proposition 5.27 Let (G, E, L) be a weighted graph such that the application of Algorithm 1 yields a loop-free graph. Then,$( \mathcal { G } , \mathcal { E } , \mathcal { L } )$is summable.

Proof. Since, for a loop-free graph,${ \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$contains only one element (the one that associates 0 to every edge), it suffices to check that for each step of the algorithm, we can show that the original graph is summable, provided that the simplified graph is summable.

We define a function$F \colon \mathcal { C } ( \mathcal { G } , \mathcal { E } )  \mathbf { R }$by

$$
F (C) = \prod_ {e \in \mathcal {E}} (1 \vee | C _ {e} |) ^ {- \mathcal {L} _ {e}},\tag{5.24}
$$

so that we want to verify the summability of$F _ { \mathbf { \delta } }$. Consider now one of the steps of the algorithm and denote by$( \mathcal { G } , \mathcal { E } , \mathcal { L } )$the graph before the step and by$( \bar { \mathcal { G } } , \bar { \mathcal { E } } , \bar { \mathcal { L } } )$ the graph after the step. Similarly, we denote by$\bar { F }$the function associated as in (5.24) to the weighted graph$( \bar { \mathcal { G } } , \bar { \mathcal { E } } , \bar { \mathcal { L } } )$. Again, orientations do not matter, but it is convenient to fix an orientation for the sake of definiteness. We will therefore assume from now on that all the edges appearing in (5.21) and (5.23) are oriented from left to right.

For each of the operations appearing in Algorithm 1, there is an obvious projection operator

$$
\Pi \colon \mathcal {C} (\mathcal {G}, \mathcal {E}) \to \mathcal {C} (\bar {\mathcal {G}}, \bar {\mathcal {E}})  .
$$

For those edges unaffected by the merging / erasing operation, we identify ΠC with $C$in the obvious way. In the case of the merging operation (5.21a), if we denote by$f$and$f ^ { \prime }$the two edges being merged and by$\bar { f }$the resulting edge in$\bar { \mathcal { E } } ,$, we set $( \Pi C ) _ { \bar { f } } = C _ { f } = C _ { f ^ { \prime } }$. In the case of (5.21b) and (5.22) there is nothing to do since$\bar { \mathcal { E } }$ is identified with a subset of$\mathcal { E } .$In the case (5.23), denoting by$f , f ^ { \prime }$and$\bar { f }$the old and new edges as before, we set$( \Pi C ) _ { \bar { f } } = C _ { f } + C _ { f ^ { \prime } }$. (In all cases, the identification is very natural if we think of elements in${ \mathcal { C } } ( { \mathcal { G } } , { \mathcal { E } } )$as describing flows on the graph. It is also clear that ΠC then again describes a flow on the new graph.)

For the first two operations, the preservation of summability is now obvious, since Π is a bijection and one has the identity

$$
\bar {F} (\Pi C) = F (C).
$$

For the operation (5.22), observe that, denoting the flow in the loop by$k ,$one has the identity

$$
\sum_ {\mathcal {C} (\mathcal {G}, \mathcal {E})} F (C) = \sum_ {\bar {C} \in \mathcal {C} (\bar {\mathcal {G}}, \bar {\mathcal {E}})} \bar {F} (\bar {C}) \sum_ {k \in \mathbf {Z}} (1 \vee | k |) ^ {- \alpha}.
$$

Therefore, since$\alpha > 1$by assumption, it does follow that the summability of$F$ implies that of$\bar { F } .$.

Finally, for the operation (5.23), denote by$C _ { 0 }$the elementary cycle going through the two edges that are being merged so that any two elements in$\Pi ^ { - 1 } \bar { C }$ differ by an integer multiple of$C _ { 0 }$. With this notation, one then has the identity

$$
\begin{array}{l} \sum_ {\mathcal {C} (\mathcal {G}, \mathcal {E})} F (C) = \sum_ {\bar {C} \in \mathcal {C} (\bar {\mathcal {G}}, \bar {\mathcal {E}})} \sum_ {C \in \Pi^ {- 1} \bar {C}} F (C) \\ = \sum_ {\bar {C} \in \mathcal {C} (\bar {\mathcal {G}}, \bar {\mathcal {E}})} \bar {F} (\bar {C}) \sum_ {k \in \mathbf {Z}} \frac {(1 \vee | \bar {C} _ {\bar {f}} |) ^ {\gamma}}{(1 \vee | k |) ^ {\alpha} (1 \vee | \bar {C} _ {\bar {f}} - k |) ^ {\beta}}, \end{array}
$$

where as before$\bar { f }$is the new edge replacing the loop. It is straightforward to check that the conditions on$\alpha , \beta ,$, and$\gamma$given below (5.21b) are precisely the conditions guaranteeing that

$$
\sup _ {a \in \mathbf {Z}} \sum_ {k \in \mathbf {Z}} \frac {(1 \vee | a |) ^ {\gamma}}{(1 \vee | k |) ^ {\alpha} (1 \vee | a - k |) ^ {\beta}} <   \infty ,
$$

so that the summability of$\bar { F }$does indeed imply that of$F$, thus concluding the proof. □

Remark 5.28 It is clear from the proof that another allowed step would be to decrease the weight of any edge. In particular, edges with positive weights can also be contracted to a node. However, we will always consider weights in$\mathcal { G } _ { \kappa } ^ { \tau }$such that this step is unnecessary.

One may legitimately ask whether the criterion given in Proposition 5.27 is sharp. This is not known to the author and is probably not the case, even though the author is not aware of any counterexample. An obvious necessary condition for summability is that$\textstyle \sum _ { e \in { \mathcal { C } } } { \mathcal { L } } _ { e } > 1$for every elementary cycle$\mathcal { C } \subset \mathcal { T }$, but it is unfortunately easy to construct counterexamples showing that this naive condition is not sufficient, even within the class of homogeneous graphs of degree 3. (Take the tetrahedron and give each edge the same weight$\alpha \in ( \frac { 1 } { 3 } , \frac { 1 } { 2 } ) . )$

Before we proceed, we summarise the results of the preceding subsections in one convenient statement:

Proposition 5.29 Let τ be a binary tree with at least two interior vertices. Set $\kappa = 4$− 2α and,for any pairing$P \in \bar { \mathcal { P } } ^ { \tau }$, denote by$( { \mathcal { E } } , { \mathcal { G } } )$and$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$the graph and set ofweightings constructed in Section 5.4. If,for a given$P \in \bar { \mathcal { P } } ^ { \tau }$, there exists $\mathcal { L } \in \mathcal { G } _ { \kappa } ^ { \tau } ( P )$such that the application ofAlgorithm 1 allows to contract the graph to a point, then the bounds (5.13) do holdfor$K _ { \mathrm { s y m } } ^ { \tau } ( P , \cdot ; \cdot )$

Proof. This is just a combination of Theorem 5.25 with Proposition 5.27.□

## 5.6 Construction of$X ^ { \aleph }$

Were are now in a position to apply the abstract result of the previous two subsections to the construction of$X ^ { \aleph }$. If we discard pairings such that$\mathcal { L } _ { P } ^ { \tau }$is empty (by Remark 5.10, these are the pairings containing at least one of the two top pairs of leaves), it can be checked by inspection that the remainder of$P \in \mathcal { P } ^ { \tau } / ( S _ { \tau } \times S _ { \tau } )$ for$\tau = \mathbb { V }$consists of exactly three elements, which can be represented graphically as follows:

![](images/page_65_image_10.jpg)

(5.25)

Proposition 5.30 For every$P \in \mathcal P ^ { \check { \forall } }$, the bounds (5.13) hold for$\mathcal { K } _ { \mathrm { s y m } } ^ { \aleph } ( P , \cdot ; \cdot )$for every$\alpha < \frac { 3 } { 2 }$and every$\beta < \textstyle { \frac { 1 } { 2 } }$

As a consequence, there exists a process$X ^ { \aleph }$with sample paths that are almost surely continuous with values in$\mathcal { C ^ { \alpha } }$for every$\alpha < \frac { 3 } { 2 }$. Furthermore,$X _ { \varepsilon } ^ { \vee }  X ^ { \vee }$in probability in$\mathcal { C } ( [ - T , T ] , \mathcal { C } ^ { \alpha } ) \cap \mathcal { C } ^ { \beta } ( [ - T , T ] , \mathcal { C } ) f o r$every$\beta < \textstyle { \frac { 1 } { 2 } }$and every$T > 0 .$

Proof. The second claim follows from Theorem 5.16, so that it suffices to check that the bounds (5.13) hold for each of the pairings P depicted in (5.25). The first pairing is treated by Proposition 5.18, noting that the required bounds on${ \mathcal { K } } _ { \mathrm { { s y m } } } ^ { \vee }$were already obtained in the proof of Proposition 5.1.

The second pairing is treated by Proposition 5.29, noting that the following element belongs to$\mathcal { G } _ { 1 + \delta } ^ { \tau } ( P )$for every$\delta > 0 \AA$

![](images/page_66_image_4.jpg)

(5.26)

It is straightforward to verify that Algorithm 1 terminates and yields a loop-free graph.

Unfortunately, the last remaining pairing does not seem to be covered by Proposition 5.29, so we need to treat it “by hand”. A generic labelling for this pairing looks like the following:

![](images/page_66_image_8.jpg)

(5.27)

The kernel$K ^ { \tau }$associated to (5.27) can then be written as

$$
K ^ {\tau} (P, \hat {L}; t ^ {\prime} - t) = \mathcal {F} (k, \ell , m) \int_ {\mathcal {T} _ {t} ^ {\tau}} \int_ {\mathcal {T} _ {t ^ {\prime}} ^ {\tau}} \exp (- \mathcal {I} _ {k, \ell , m} (T, T ^ {\prime})) \mu_ {t} (d T) \mu_ {t ^ {\prime}} (d T ^ {\prime}),\tag{5.28}
$$

where the prefactor$\mathcal { F }$is given by

$$
\mathcal {F} (k, \ell , m) = (k + \ell) (k + m) (k + \ell + m) ^ {2},
$$

whereas the exponent I is given by$\mathcal { T } = \mathcal { T } _ { 1 } + \mathcal { T } _ { 2 }$with

$$
\mathcal {I} _ {1} = k ^ {2} | r - r ^ {\prime} | + (k + \ell) ^ {2} (s - r) + (k + m) ^ {2} (s ^ {\prime} - r ^ {\prime}) + \ell^ {2} | s ^ {\prime} - r | + m ^ {2} | r ^ {\prime} - s |,
$$

$$
\mathcal {I} _ {2} = (k + \ell + m) ^ {2} (t + t ^ {\prime} - s - s ^ {\prime}) .
$$

This time, we make use of Proposition A.8 in order to bound the integral of$\mathcal { T } _ { 1 }$, which yields the bound

$$
\int_ {- \infty} ^ {s} \int_ {- \infty} ^ {s ^ {\prime}} e ^ {- \mathcal {I} _ {1}} d r ^ {\prime} d r \lesssim \frac {e ^ {- (\ell^ {2} \wedge m ^ {2}) | s - s ^ {\prime} |}}{((k + \ell) ^ {2} + \ell^ {2}) ((k + m) ^ {2} + m ^ {2})}.
$$

As in the proof of Theorem 5.25, it follows from Lemma$\mathrm { A } . 7$that, in order to verify the assumptions of Theorem 5.16, it suffices to verify the summability of

$$
K _ {k \ell m} \stackrel {\mathrm{def}} {=} \frac {| k + \ell | | k + m | (k + \ell + m) ^ {1 - 2 \kappa}}{((k + \ell) ^ {2} + \ell^ {2}) ((k + m) ^ {2} + m ^ {2}) ((k + \ell + m) ^ {2} + (\ell^ {2} \wedge m ^ {2}))},
$$

for every$\kappa > 0$. Since this expression is symmetric in$( \ell , m )$, it suffices to check summability over$| \ell | > | m |$, say. In this case, one has the bound

$$
\begin{array}{r l} & K _ {k \ell m} \lesssim \frac {1}{(| k + \ell | + | \ell |) (| k + m | + | m |) (| k + \ell + m | + | m |) ^ {1 + 2 \kappa}} \\ & \quad \leq \frac {1}{| \ell | | k + m | ^ {\frac {\kappa}{2}} | m | ^ {1 + \frac {\kappa}{2}} | k + \ell + m | ^ {1 + \kappa}}. \end{array}
$$

Since, for every$\kappa > 0$and$a \in \mathbf { Z } _ { \star }$, one has the bound$\begin{array} { r } { \sum _ { \ell \notin \{ 0 , a \} } \frac { 1 } { | \ell | | \ell - a | ^ { 1 + \kappa } } \lesssim \frac { 1 } { | a | } } \end{array}$, it follows that

$$
\sum_ {\ell} K _ {k \ell m} \lesssim \frac {1}{| m | ^ {1 + \frac {\kappa}{2}} | k + m | ^ {1 + \frac {\kappa}{2}}} ,
$$

which is indeed summable in k and m for every$\kappa > 0$, and the claim follows.

## 5.7 Construction of$X ^ { \mathbb { V } }$

Since the tree$\mathbb { V }$has many symmetries, the calculations for this tree turn out to be easier than for the previous case, even though this is a larger tree. Discarding pairings such that$\mathcal { L } _ { P } ^ { \tau }$is empty, it can again be checked by inspection that the remainder of$P \in \mathcal { P } ^ { \tau } / ( S _ { \tau } \times S _ { \tau } )$consists of the following three elements:

![](images/page_67_image_11.jpg)

(5.29)

We have the following result:

Proposition 5.31 There exists a process$X ^ { \mathbb { V } }$with sample paths that are almost surely continuous with values in$\mathcal { C } ^ { \alpha } f o r$every$\alpha < 2 .$. Furthermore,$X _ { \varepsilon } ^ { \Psi }  X ^ { \Psi }$in probability in$\mathcal { C } ( [ - T , T ] , \mathcal { C } ^ { \alpha } ) \cap \mathcal { C } ^ { \beta } ( [ - T , T ] , \mathcal { C } ) f o r$every$\beta < \textstyle { \frac { 1 } { 2 } }$and every$T > 0 .$

Proof. For the three pairings shown in (5.29), the algorithm of Section 5.4 allows to verify that the following elements belongs to$\mathcal { G } _ { \kappa } ^ { \tau }$:

![](images/page_68_image_1.jpg)

In each case, we go through the vertices in Step 2 by ordering them from left to right and top to bottom. For each of these three elements, it is then straightforward to verify that Algorithm 1 indeed yields a loop-free graph for every$\kappa > 0$□

## 5.8 Construction of$X ^ { \aleph }$

This time, because of the lack of symmetry of$\updownarrow ,$, there are many more cases to consider. Indeed, if we discard again those pairings such that$\mathcal { L } _ { P } ^ { \tau }$is empty, it can be checked by inspection that the remainder of$P \in \mathcal { P } ^ { \tau } / ( S _ { \tau } \times \bar { S } _ { \tau } )$consists of 15 elements.

However, with the tools of the previous subsections at hand, it turns out to be relatively straightforward to show that the following holds, where$\mathcal { P } _ { s }$is as in Proposition 5.18.

Proposition 5.32 For every$\boldsymbol { P } \in \mathcal { P } ^ { \sharp } \setminus \mathcal { P } _ { s } ^ { \sharp }$and for every$\kappa > 0$, one has

$$
\sum_ {L \in \mathcal {L} _ {P} ^ {\aleph_ {\aleph}}} | \varrho (L) | ^ {- \kappa} \mathcal {F} _ {\text {sym}} ^ {\aleph_ {\aleph}} (P, L) <   \infty .
$$

Proof. We outline a systematic way of constructing an element in$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$for each pairing$P .$The spanning tree$\tau$underlying the graphs$( { \mathcal { G } } , { \mathcal { E } } )$associated to each pairing is given by a row of five edges, which we represent as

![](images/page_68_image_9.jpg)

(5.30)

with the distinguished edge e¯ being the one with weight κ. The remaining pairings now consist of all possible graphs built by adding edges to (5.30) in such a way that

• Every vertex is of degree exactly 3, which is a reflection of the fact that we only consider binary trees.

• There are no simple loops, i.e. loops of the kind (5.22), for otherwise one would have$\mathcal { L } _ { P } ^ { \tau } = \emptyset$by Remark 5.10.

• There is at least one edge other than e¯ connecting the left half of the graph to the right half, for otherwise one would have$\mathcal { L } _ { P } ^ { \tau } = \emptyset$by Lemma 5.9.

• There is no edge other than e¯ connecting the two vertices adjacent to e¯, for otherwise one would have$P \in \mathcal { P } _ { s } ^ { \tau }$

By inspection, one can then check that, modulo isometries, the set of all such graphs consists of 12 elements. We first consider the following 10 elements:

![](images/page_69_image_4.jpg)

(5.31)

Observe that, for each one of the graphs (G, E) appearing in this list, we have distinguished a subset$\hat { \mathcal { E } } \subset \mathcal { E }$of the edges by drawing it in boldface, and we have drawn the distinguished edge e¯ as a dashed line.

For each pairing, the weighting represented by these pictures gives weight 1 to edges in$\hat { \mathcal { E } }$and weight κ to e¯. One should furthermore think of it as giving weight 0 to the remaining dotted edges. However, whenever a small loop (whatever its type) followed by a dotted edge appears in one of these graphs, we weigh such a configuration as follows:

![](images/page_69_image_8.jpg)

(5.32)

We see that applying one step of Algorithm 1 to such a configuration results in two consecutive edges with weights$- { \frac { 1 } { 3 } }$and$\frac 1 3$respectively. As a consequence, by applying one more step of the algorithm, such a configuration does indeed behave for all practical purposes as if the loop was erased and all edges had weight 0. For each of the weightings represented in the figure, it is then a straightforward task to verify that, on the one hand they do belong to$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$for every$\kappa > 0$and, on the other hand, that Algorithm 1 does indeed yield a loop-free graph. This is because, in every single case, contracting the edges with weight 0 yields a graph with only two vertices that are joined by a number of edges, where one edge has weight κ and every other edge has weight 1.

The two remaining pairings require a slightly different weighting:

![](images/page_70_image_2.jpg)

In the first case, the two grey edges have weights$\frac { \kappa } { 2 }$and$1 - \textstyle { \frac { \kappa } { 2 } }$respectively, whereas the weights for all the other edges are as before. In the second case, the two grey edges have weights$- \frac { 2 } { 3 }$and$\mathit { \bar { \Psi } } _ { 3 }$respectively, whereas the dotted edges all have weights$\frac { 2 } { 3 }$.

Again, it can be checked in a straightforward way that in both cases, these weights do indeed belong to$\mathcal { G } _ { \kappa } ^ { \tau } ( P )$and that Algorithm 1 yields a loop-free graph in both cases.□

It follows almost immediately that$X _ { \varepsilon } ^ { \aleph }$converges to a limit taking “almost” values in$\mathcal { C } ^ { \frac { 3 } { 2 } }$. More precisely,

Proposition 5.33 There exists a process$X ^ { \aleph }$with sample paths that are almost surely continuous with values in$\mathcal { C ^ { \alpha } }$for every$\alpha < \frac { 3 } { 2 }$. Furthermore,$X _ { \varepsilon } ^ { \aleph }  X ^ { \aleph }$in probability in${ \mathcal { C } } ( [ 0 , T ] , { \mathcal { C } } ^ { \alpha } ) \cap { \mathcal { C } } ^ { \beta } ( [ 0 , T ] , { \mathcal { C } } )$for every$\beta < \textstyle { \frac { 1 } { 2 } }$

Proof. It follows from Proposition 5.32 and Theorem 5.25 that the bound (5.13) holds for every$\alpha < 2$and$\beta < \textstyle { \frac { 1 } { 2 } }$, provided that$\boldsymbol { P } \in \mathcal { P } ^ { \sharp } \setminus \mathcal { P } _ { s } ^ { \sharp }$

In view of Theorem 5.16, it thus suffices to show that a similar bound, but this time with$\alpha < \frac { 3 } { 2 }$, holds for$\boldsymbol { P } \in \mathcal { P } _ { s } ^ { \aleph }$. By Proposition 5.18, these pairings can be reduced to the study of the tree . Applying Proposition 5.30 then concludes the proof.□

## 6 Treatment of the constant Fourier mode

So far, we were concerned with the construction of the processes$X ^ { \tau }$defined as the limits of the processes$X _ { \varepsilon } ^ { \tau }$from (2.1). However, in order to define solutions to the original problem, we would really like to build a sequence of processes$Y ^ { \tau }$given by the limit as$\varepsilon \to 0$of$Y _ { \varepsilon } ^ { \tau }$defined recursively by

$$
\partial_ {t} Y _ {\varepsilon} ^ {\tau} = \partial_ {x} ^ {2} Y _ {\varepsilon} ^ {\tau} + \partial_ {x} Y _ {\varepsilon} ^ {\tau_ {1}} \partial_ {x} Y _ {\varepsilon} ^ {\tau_ {2}} - C _ {\varepsilon} ^ {\tau},\tag{6.1}
$$

for${ \tau } = [ { \tau } _ { 1 } , { \tau } _ { 2 } ]$and for constants$C _ { \varepsilon } ^ { \tau }$as in (2.4). Here, we start the recursion by setting$Y _ { \varepsilon } ^ { \bullet } ( t , x ) = X _ { \varepsilon } ^ { \bullet } ( t , x ) + \sqrt { 2 } B ( t )$, for B a standard Brownian motion which is a solution to the additive stochastic heat equation.

Since only spatial derivatives appear in the right hand side of the recursion relation (6.1), we see that$\Pi _ { 0 } ^ { \perp } Y _ { \varepsilon } ^ { \tau } = X _ { \varepsilon } ^ { \tau }$, so that it only remains to show that the constant Fourier modes of$Y _ { \varepsilon } ^ { \tau }$converge to a limiting real-valued stochastic process. The proof goes in two steps. In a first step, we define a family of constants$K _ { \varepsilon } ^ { \tau }$for $\tau = [ \tau _ { 1 } , \tau _ { 2 } ]$by

$$
K _ {\varepsilon} ^ {\tau} = \sum_ {k \in \mathbf {Z} _ {\star}} \mathbf {E} \bar {X} _ {\varepsilon , k} ^ {\tau_ {1}} \bar {X} _ {\varepsilon , - k} ^ {\tau_ {2}},
$$

and we show that the following convergence result holds.

Proposition 6.1 For every$\tau \in \{ \mathrm { v } , \mathrm { \psi } , \mathrm { \psi } , \mathrm { \psi } \}$, there exists a constant$\bar { K } ^ { \tau }$independent ofthe mollifier$\varphi$such that

$$
\lim _ {\varepsilon \to 0} (C _ {\varepsilon} ^ {\tau} - K _ {\varepsilon} ^ {\tau}) = \bar {K} ^ {\tau}.
$$

Proof. See Lemmas$6 . 3 { - } 6 . 5$below, noting that one has$K ^ { \check { \Psi } } = 0$so that the statement is trivial for$\tau = \mathbb { V }$□

Once this is established we see that, in order to establish convergence of the processes$Y _ { \varepsilon } ^ { \tau }$in (6.1), it is sufficient to establish it with$C _ { \varepsilon } ^ { \tau }$replaced by$K _ { \varepsilon } ^ { \tau }$. With this in mind, we define processes$F _ { \varepsilon } ^ { \tau }$by

$$
F _ {\varepsilon} ^ {\tau} (t) = \int_ {0} ^ {t} \sum_ {k \in \mathbf {Z} _ {\star}} \bar {X} _ {\varepsilon , k} ^ {\tau_ {1}} (s) \bar {X} _ {\varepsilon , - k} ^ {\tau_ {2}} (s) d s - K _ {\varepsilon} ^ {\tau} t.\tag{6.2}
$$

Since$F _ { \varepsilon } ^ { \tau } = \Pi _ { 0 } Y _ { \varepsilon } ^ { \tau } + ( C _ { \varepsilon } ^ { \tau } - K _ { \varepsilon } ^ { \tau } )$, the convergence of the processes$Y _ { \varepsilon } ^ { \tau }$to a limit is now equivalent to the convergence of$F _ { \varepsilon } ^ { \tau }$to a limit process$F ^ { \tau }$. This in turn is ensured by the following result.

Proposition 6.2 For every$\tau \in \{ \mathrm { v } , \mathrm { v } , \mathrm { v } , \mathrm { \check { v } } \}$, there exists a process$F ^ { \tau }$such that $F _ { \varepsilon } ^ { \tau } \to F ^ { \tau }$in probability. Furthermore,for every$\delta > 0$, one has$F ^ { \vee } \in { \mathcal { C } } ^ { \frac { 3 } { 4 } - \delta }$, and $\bar { F ^ { \tau } } \in \mathcal { C } ^ { 1 - \delta }$for every$\tau \in \{ \forall , \forall , \forall \}$

Proof. See Lemmas 6.6 and 6.10 below.

## 6.1 Convergence of the renormalisation constants

In this section, we show that one does indeed have$K _ { \varepsilon } ^ { \tau } - C _ { \varepsilon } ^ { \tau } \to K ^ { \tau }$as$\varepsilon \to 0$, for some constants$K ^ { \tau }$that do not depend on the choice of mollifier$\varphi .$. The simplest case is when$\tau = \Psi ,$, which is covered by the following lemma.

Lemma 6.3 The identity

$$
K _ {\varepsilon} ^ {\mathsf {V}} \approx C _ {\varepsilon} ^ {\mathsf {V}} + 1 = \frac {1}{\varepsilon} \int \varphi^ {2} (x) d x + 1,
$$

holds up to an error oforder$\mathcal { O } ( \varepsilon )$

Proof. By definition, we have the identity

$$
K _ {\varepsilon} ^ {\mathbf {V}} = \sum_ {k \in \mathbf {Z} _ {\star}} \varphi^ {2} (k \varepsilon) = \sum_ {k \in \mathbf {Z}} \varphi^ {2} (k \varepsilon) - 1.
$$

It now suffices to note that$\varepsilon \textstyle \sum _ { k } \varphi ^ { 2 } ( k \varepsilon )$is a Riemann sum approximation to the integral$\scriptstyle \int \varphi ^ { 2 } ( x )$dx. Since, on the whole of R, this approximation agrees with the trapezoidal rule, it is of second order, so that the claim follows.□

For$\tau = \mathbb { V }$on the other hand, it is much more difficult to get a handle on the corresponding constants. In principle, the precise value of$\check { K } _ { \varepsilon } ^ { \mathfrak { V } }$does not really matter, since the important fact is only that$\bar { K } _ { \varepsilon } ^ { \ Y } + 4 K _ { \varepsilon } ^ { \aleph }$is approximately constant as$\varepsilon  0$, but since it is possible to actually compute this constant, we state the result and sketch its proof.

Lemma 6.4 Let$\psi ( x ) = \varphi ( x ) \varphi ^ { \prime } ( x )$. Then, there exists a constant K independent $o f \varphi$such that one has the identity

$$
K _ {\varepsilon} ^ {\mathbb {V}} \approx \frac {4 \pi}{\sqrt {3}} | \log \varepsilon | - 8 \int_ {\mathbf {R} _ {+}} \int_ {\mathbf {R}} \frac {x \psi (y) \varphi^ {2} (y - x) \log y}{x ^ {2} - x y + y ^ {2}} d x d y + K,
$$

up to an error oforder$\mathcal { O } ( \sqrt { \varepsilon } \log \varepsilon )$

Proof. In the proof, we will denote by K a generic constant independent of$\varphi .$. We will not keep track of the precise value of$K$, so that it may change without warning from expression to expression.

Following the definition of$X _ { \varepsilon } ^ { \vee }$and using the correlation function of$\bar { X } _ { \varepsilon } ^ { \bullet }$, it is tedious but straightforward to check that for$k \neq 0 ,$, one has the identity

$$
\mathbf {E} | \bar {X} _ {\varepsilon , k} ^ {\mathsf {V}} | ^ {2} = \sum_ {m \not \in \{0, k \}} \frac {\varphi^ {2} (\varepsilon m) \varphi^ {2} (\varepsilon (k - m))}{k ^ {2} + m ^ {2} - k m} .
$$

(Here, we used again the shorthand$\bar { X } ^ { \tau } = \partial _ { x } X ^ { \tau } . )$Using the fact that the summand is symmetric under the substitution$( k , m )  ( - k$, −m) and treating separately the terms$m \in \{ 0 , k \}$, we thus obtain

$$
K _ {\varepsilon} ^ {\mathbb {W}} = \sum_ {k \in \mathbf {Z}} \mathbf {E} | \bar {X} _ {\varepsilon , k} ^ {\mathbb {V}} | ^ {2} = 2 \sum_ {k \geq 1} \sum_ {m \in \mathbf {Z}} \frac {\varphi^ {2} (\varepsilon m) \varphi^ {2} (\varepsilon (k - m))}{k ^ {2} - k m + m ^ {2}} - 4 \sum_ {k \geq 1} \frac {\varphi^ {2} (\varepsilon k)}{k ^ {2}} .\tag{6.3}
$$

Since the second term differs from$2 \pi ^ { 2 } / 3$only by an error of order$\mathcal { O } ( \varepsilon )$, we focus on the first term. Note now that for k large, we can interpret the inner sum as a Riemann sum so that, setting$\begin{array} { r } { \delta = \frac { 1 } { k } } \end{array}$, we have

$$
\begin{array}{r l} & {\sum_ {m \in \mathbf {Z}} \frac {\varphi^ {2} (\varepsilon m) \varphi^ {2} (\varepsilon (k - m))}{k ^ {2} - k m + m ^ {2}} = \frac {\delta}{k} \sum_ {m \in \mathbf {Z}} \frac {\varphi^ {2} (\varepsilon k \delta m) \varphi^ {2} (\varepsilon k (1 - \delta m))}{1 - \delta m + (\delta m) ^ {2}}} \\ & {\qquad = \frac {1}{k} \int_ {\mathbf {R}} \frac {\varphi^ {2} (\varepsilon k x) \varphi^ {2} (\varepsilon k (1 - x))}{1 - x + x ^ {2}} d x + \frac {G _ {\delta}}{k} + \mathcal {O} (\varepsilon^ {2} \wedge k ^ {- 2})} \\ & {\qquad \stackrel {\mathrm{def}} {=} C _ {\varepsilon} (k) + \frac {G _ {\delta}}{k} + \mathcal {O} (\varepsilon^ {2} \wedge k ^ {- 2}),} \end{array}
$$

Where$G _ { \delta }$is the error in the Riemann sum approximation:

$$
G _ {\delta} = \sum_ {m \in \mathbf {Z}} \frac {\delta}{1 - \delta m + (\delta m) ^ {2}} - \int_ {\mathbf {R}} \frac {d x}{1 - x + x ^ {2}}.
$$

Since$G _ { \delta } = \mathcal { O } ( \delta )$for$\delta \ll 1$, the term$G ( \delta ) / k$is summable, so that

$$
K _ {\varepsilon} ^ {\mathbb {W}} = 2 \sum_ {k \geq 1} C _ {\varepsilon} (k) + K + \mathcal {O} (\varepsilon).
$$

At this stage, we note that one has

$$
\int_ {\mathbf {R}} \frac {d x}{1 - x + x ^ {2}} = \frac {2 \pi}{\sqrt {3}},
$$

from which it follows immediately that

$$
C _ {\varepsilon} (k) = \frac {2 \pi}{\sqrt {3} k} + \mathcal {O} (\varepsilon),\tag{6.4}
$$

where the error is$\mathcal { O } ( \varepsilon )$, uniformly in k.

We now break the sum over$C _ { \varepsilon } ( k )$into two parts. We first obtain from (6.4) that

$$
2 \sum_ {k = 1} ^ {1 / \sqrt {\varepsilon}} C _ {\varepsilon} (k) = \frac {2 \pi}{\sqrt {3}} | \log \varepsilon | + \frac {4 \pi \gamma}{\sqrt {3}} + \mathcal {O} (\sqrt {\varepsilon}),
$$

where$\gamma$is the Euler-Mascheroni constant. For the remaining terms, we first note that$C _ { \varepsilon } ( k ) = 0$for$k > 4 / \varepsilon$because of the properties of$\varphi .$. We then write$y = \varepsilon k$ and we approximate the sum over k by an integral:

$$
2 \sum_ {k = 1 / \sqrt {\varepsilon}} ^ {4 / \varepsilon} C _ {\varepsilon} (k) = 2 \int_ {\sqrt {\varepsilon}} ^ {4} \int_ {\mathbf {R}} \frac {\varphi^ {2} (y x) \varphi^ {2} (y (1 - x))}{y (1 - x + x ^ {2})} d x d y + \mathcal {O} (\sqrt {\varepsilon}).
$$

Note that the error is of order$\sqrt { \varepsilon }$because, for fixed$x \in \mathbf { R }$, the variation of the integrand in y is of order$1 / { \sqrt { \varepsilon } }$. Integrating by parts over y, we see that this is equal to

$$
\begin{array}{l} \frac {2 \pi}{\sqrt {3}} | \log \varepsilon | + \mathcal {O} (\sqrt {\varepsilon} \log \varepsilon) \\ - 4 \int_ {\mathbf {R} _ {+}} \int_ {\mathbf {R}} \frac {(x \psi (y x) \varphi^ {2} (y (1 - x)) + (1 - x) \psi (y (1 - x)) \varphi^ {2} (y x)) \log y}{1 - x + x ^ {2}} d x d y. \end{array}
$$

The claim now follows from the symmetry of the integrand under the substitution $x \mapsto 1 - x$and by performing the change of variables yx$\mapsto x .$□

Finally, we show that$\vec { K _ { \varepsilon } ^ { \ddagger } }$can indeed be expressed in terms of$K _ { \varepsilon } ^ { \ C }$.

Lemma 6.5 One has 4$\begin{array} { r } { { \cal K } _ { \varepsilon } ^ { \ast } = - { \cal K } _ { \varepsilon } ^ { \ast \ast } - \frac { \pi ^ { 2 } } { 3 } + { \cal O } ( \varepsilon ) . } \end{array}$

Proof. By definition, one has the identity

$$
\dot {X} _ {\varepsilon , k} ^ {\mathbf {V}} (t) = \sum_ {\ell \in \mathbf {Z}} \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} \bar {X} _ {\varepsilon , \ell} ^ {\mathbf {V}} (s) \bar {X} _ {\varepsilon , k - \ell} ^ {\bullet} (s) d s,
$$

so that

$$
K _ {\varepsilon} ^ {\mathbf {\dot {x}}} = - \sum_ {k \in \mathbf {Z}} \sum_ {\ell \in \mathbf {Z}} k \ell \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} X _ {\varepsilon , \ell} ^ {\mathbf {\dot {V}}} (s) \bar {X} _ {\varepsilon , k - \ell} ^ {\bullet} (s) \bar {X} _ {\varepsilon , - k} ^ {\bullet} (t) d s.\tag{6.5}
$$

To estimate this quantity, the following calculation is helpful. For$s > 0$and $k , \ell \in \mathbf { Z } ,$set

$$
H _ {k, \ell} (s) = \mathbf {E} X _ {\varepsilon , \ell} ^ {\vee} (0) \bar {X} _ {\varepsilon , k - \ell} ^ {\bullet} (0) \bar {X} _ {\varepsilon , - k} ^ {\bullet} (s)  .
$$

For$k , \ell \neq 0$with$k \neq \ell ,$, one then has the identity

$$
H _ {k, \ell} (s) = \sum_ {m \in {\bf Z}} \int_ {- \infty} ^ {0} e ^ {\ell^ {2} r} {\bf E} \big (\bar {X} _ {\varepsilon , \ell - m} ^ {\bullet} (r) \bar {X} _ {\varepsilon , m} ^ {\bullet} (r) \bar {X} _ {\varepsilon , k - \ell} ^ {\bullet} (0) \bar {X} _ {\varepsilon , - k} ^ {\bullet} (s) \big) d r .
$$

One can check that the only non-vanishing terms in this sum are those with$m =$ $\ell - k$and with$m = k$, which yields

$$
\begin{array}{r} H _ {k, \ell} (s) = 2 \varphi^ {2} (\varepsilon k) \varphi^ {2} \big (\varepsilon (k - \ell) \big) \int_ {- \infty} ^ {0} e ^ {\ell^ {2} r + (k - \ell) ^ {2} r - k ^ {2} (s - r)} d r \\ = \frac {\varphi^ {2} (\varepsilon k) \varphi^ {2} \big (\varepsilon (k - \ell) \big)}{\ell^ {2} + k ^ {2} - k \ell} e ^ {- k ^ {2} s}. \end{array}
$$

Inserting this expression into (6.5), it follows that one has the identity

$$
K _ {\varepsilon} ^ {\ddot {\mathbf {x}}} = - \sum_ {k \in \mathbf {Z} _ {\star}} \sum_ {\ell \neq k} \frac {\ell \varphi^ {2} (\varepsilon k) \varphi^ {2} (\varepsilon (k - \ell))}{2 k (\ell^ {2} + k ^ {2} - k \ell)},
$$

which, by performing the substitution$\ell = k - m$, we can rewrite as

$$
K _ {\varepsilon} ^ {\ddot {\mathbf {v}}} = - \sum_ {k, m \in \mathbf {Z} _ {\star}} \frac {(k - m) \varphi^ {2} (\varepsilon k) \varphi^ {2} (\varepsilon m)}{2 k (k ^ {2} + m ^ {2} - k m)} .
$$

Performing a similar substitution in (6.3), we obtain

$$
K _ {\varepsilon} ^ {\mathbb {Y}} = \sum_ {k, m \in \mathbf {Z} _ {\star}} \frac {\varphi^ {2} (\varepsilon k) \varphi^ {2} (\varepsilon m)}{k ^ {2} + m ^ {2} - k m} - \sum_ {k \in \mathbf {Z} _ {\star}} \frac {\varphi^ {2} (\varepsilon k)}{k ^ {2}},
$$

so that we have the identity

$$
K _ {\varepsilon} ^ {\mathbb {Y}} + 4 K _ {\varepsilon} ^ {\mathbb {X}} = \sum_ {k, m \in \mathbf {Z} _ {\star}} \frac {2 m - k}{k} \frac {\varphi^ {2} (\varepsilon k) \varphi^ {2} (\varepsilon m)}{k ^ {2} + m ^ {2} - k m} - \frac {\pi^ {2}}{3} + \mathcal {O} (\varepsilon) \stackrel {{\text {def}}} {{=}} I _ {\varepsilon} - \frac {\pi^ {2}}{3} + \mathcal {O} (\varepsilon).
$$

At this stage, we note that, apart from the prefactor$( 2 m - k ) / k$, the summand is symmetric under the substitution$( k , m )  ( m , k )$. As a consequence, we can rewrite this sum as

$$
I _ {\varepsilon} = \frac {1}{2} \sum_ {k, m \in \mathbf {Z} _ {\star}} \left(\frac {2 m - k}{k} + \frac {2 k - m}{m}\right) \frac {\varphi^ {2} (\varepsilon k) \varphi^ {2} (\varepsilon m)}{k ^ {2} + m ^ {2} - k m}.\tag{6.6}
$$

Since one furthermore has the identity

$$
\frac {2 m - k}{k} + \frac {2 k - m}{m} = \frac {2 (m ^ {2} + k ^ {2} - k m)}{k m},
$$

the quantity in (6.6) is equal to$\begin{array} { r } { \big ( \sum _ { k \in \mathbf { Z } _ { \star } } \frac { \varphi ( k \varepsilon ) } { k } \big ) ^ { 2 } } \end{array}$. This vanishes identically since$\varphi$is even, thus concluding the proof.□

## 6.2 Convergence of the fluctuation processes

In this section, we show that the processes$F _ { \varepsilon } ^ { \tau }$defined in (6.2) have limits as$\varepsilon \to 0$ We start with the process$F ^ {  \forall }$:

Proposition 6.6 There exists a limiting process$F ^ {  \nu }$such that$F _ { \varepsilon } ^ { \tt V } \to F ^ { \tt V }$in probability in$\mathcal { C ^ { \alpha } }$for every$\textstyle \alpha < { \frac { 3 } { 4 } }$

Proof. From the definition of$F _ { \varepsilon } ^ { \vee }$and the expression for the correlation functions of$\bar { X } _ { \varepsilon } ^ { \bullet }$, it is straightforward to see that

$$
\begin{array}{r l} & {\mathbf {E} | F _ {\varepsilon} ^ {\mathsf {V}} (t) - F _ {\varepsilon} ^ {\mathsf {V}} (s) | ^ {2} = \sum_ {k \in \mathbf {Z} _ {\star}} \varphi^ {4} (k \varepsilon) \int_ {s} ^ {t} \int_ {s} ^ {t} e ^ {- k ^ {2} | r - r ^ {\prime} |} d r d r ^ {\prime}} \\ & {\qquad \lesssim \sum_ {k \in \mathbf {Z} _ {\star}} \int_ {s} ^ {t} \int_ {s} ^ {r ^ {\prime}} \frac {1}{| k | ^ {2 \alpha} | r - r ^ {\prime} | ^ {\alpha}} d r d r ^ {\prime}} \\ & {\qquad \lesssim \int_ {s} ^ {t} | s - r ^ {\prime} | ^ {1 - \alpha} d r ^ {\prime} \lesssim | t - s | ^ {2 - \alpha},} \end{array}
$$

provided that$\alpha > \frac { 1 } { 2 }$. The fact that the sequence is actually Cauchy then follows in the same way as in the proof of Proposition A.2 below.□

For the more complicated trees, a more systematic approach, very similar to the previous two sections, is required. We note that for a general tree τ with${ \tau } = [ { \tau } _ { 1 } , { \tau } _ { 2 } ]$ one has the identity

$$
\begin{array}{l}\mathbf {E} | F _ {\varepsilon} ^ {\tau} (t) - F _ {\varepsilon} ^ {\tau} (s) | ^ {2} = \sum_ {k, \ell \in \mathbf {Z} _ {\star}} \int_ {s} ^ {t} \int_ {s} ^ {t} \left( \right.\mathbf {E} \left(\bar {X} _ {\varepsilon , k} ^ {\tau_ {1}} (r) \bar {X} _ {\varepsilon , - k} ^ {\tau_ {2}} (r) \bar {X} _ {\varepsilon , \ell} ^ {\tau_ {1}} \left(r ^ {\prime}\right) \bar {X} _ {\varepsilon , - \ell} ^ {\tau_ {2}} \left(r ^ {\prime}\right)\right) d r d r ^ {\prime} - \mathbf {E} \left(\bar {X} _ {\varepsilon , k} ^ {\tau_ {1}} (r) \bar {X} _ {\varepsilon , - k} ^ {\tau_ {2}} (r)\right) \mathbf {E} \left(\bar {X} _ {\varepsilon , \ell} ^ {\tau_ {1}} \left(r ^ {\prime}\right) \bar {X} _ {\varepsilon , - \ell} ^ {\tau_ {2}} \left(r ^ {\prime}\right)\right) d r d r ^ {\prime}.\end{array}\tag{6.7}
$$

The reason why we can rewrite it in this way is that, by definition,

$$
K _ {\varepsilon} ^ {\tau} = \sum_ {\ell \in \mathbf {Z} _ {\star}} \mathbf {E} \big (\bar {X} _ {\varepsilon , \ell} ^ {\tau_ {1}} (r) \bar {X} _ {\varepsilon , - \ell} ^ {\tau_ {2}} (r) \big),
$$

which is independent of r by the stationarity of the processes$X _ { \varepsilon } ^ { \tau }$

As before, we can write this expectation as a sum over pairings of the tree τ and all cycles of the corresponding graph. Previously, we always restricted ourselves to cycles in$\mathcal { C } _ { \star } ( \mathcal { G } , \mathcal { E } ) \sim \mathcal { L } _ { P } ^ { \tau }$, which was defined as consisting of those cycles that associate a non-zero value to every edge. This time however, we are precisely interested in only those cycles that do associate the value 0 to the distinguished edge e¯. We therefore denote by$\mathcal { L } _ { P ; 0 } ^ { \tau }$the set of all cycles that associate the label 0 to the distinguished edge e¯ but not to any other edge.

Remark 6.7 For the pairing associated to the graph depicted in (5.26), the set$\mathcal { L } _ { P ; 0 } ^ { \tau }$ is empty. Indeed, any cycle giving the value 0 to the horizontal edge at the bottom of the graph also necessarily gives the value 0 to the horizontal edge at the top, but this is not allowed. In general, all pairings yielding graphs with a small loop touching e¯ are ruled out in this way.

In principle, the consequence of this is that we have to consider a potentially larger set of pairings than what we did in in Section 5. Recall indeed Lemma 5.11, which characterised the pairings yielding a non-empty set$\mathcal { L } _ { P } ^ { \tau }$as those pairings which contain at least one element connecting the two copies of τ. (Denote these pairings by$\hat { \mathcal { P } } ^ { \tau } . )$While the pairings that do not contain any such connection yield an empty set$\mathcal { L } _ { P } ^ { \tau }$, they would certainly not yield an empty set$\mathcal { L } _ { P ; 0 } ^ { \tau }$. In fact, pairings$P \in \mathcal P ^ { \tau } \backslash \hat { \mathcal P } ^ { \tau }$are precisely those with the property that every cycle of the corresponding graph belongs to$\mathcal { L } _ { P ; 0 } ^ { \tau } \dag .$Fortunately, we see that the pairings in $P \in { \mathcal { P } } ^ { \tau } \backslash { \hat { \mathcal { P } } } ^ { \tau }$are precisely those that appear in the second line of (6.7), so that their contribution to (6.7) vanishes. As a consequence, we still have the identity

$$
\mathbf {E} | F _ {\varepsilon} ^ {\tau} (t) - F _ {\varepsilon} ^ {\tau} (s) | ^ {2} = \sum_ {P \in \hat {\mathcal {P}} ^ {\tau}} \sum_ {L \in \mathcal {L} _ {P; 0} ^ {\tau}} C _ {\varepsilon} (L) \int_ {s} ^ {t} \int_ {s} ^ {t} \mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L; r - r ^ {\prime}) d r d r ^ {\prime},
$$

where$\mathcal { F } _ { \mathrm { { s y m } } } ^ { \tau }$is defined exactly as in Section 5.2 and where

$$
C _ {\varepsilon} (L) = \prod_ {e \in \mathcal {T}} \varphi^ {2} (\varepsilon L _ {e}).
$$

With this notation, we have the following result, which is the counterpart in this context to Theorem 5.16:

Proposition 6.8 Let τ be a non-trivial binary tree and assume that there exists $\alpha > 0$such that

$$
\left| \int_ {s} ^ {t} \int_ {s} ^ {t} \mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L; r - r ^ {\prime}) d r d r ^ {\prime} \right| \leq | t - s | ^ {2 \alpha} \mathcal {F} _ {\alpha} (P, L),\tag{6.8}
$$

for some constants$\mathcal { F } _ { \alpha } ( P , L )$) and every$s < t$with$| t - s | \leq 1$. Then,$i f$

$$
\sum_ {P \in \hat {\mathcal {P}} ^ {\tau}} \sum_ {L \in \mathscr {L} _ {P; 0} ^ {\tau}} \mathcal {F} _ {\alpha} (P, L) <   \infty ,
$$

there exists a process$F ^ { \tau }$such that$F _ { \varepsilon } ^ { \tau } \to F ^ { \tau }$in probability in$\mathcal { C } ^ { \bar { \alpha } }$for every$\bar { \alpha } < \alpha$

Proof. Using Kolmogorov’s continuity criterion, the proof is virtually identical to that of Proposition$\mathsf { A } . 2 .$□

It thus remains to provide a criterion for the summability of$\mathcal { F } _ { \alpha } ( P , L )$(which we can define as the smallest constant such that (6.8) holds) for a given pairing$P .$ For this, we proceed similarly to Section 5 but our construction is slightly different. Given a pairing$P \in \hat { \mathcal { P } } ^ { \tau }$and given$\kappa > 0$, we now construct a graph$( \hat { \mathcal { G } } , \hat { \mathcal { E } } )$and a set of weights$\mathcal { G } _ { \kappa } ^ { \tau } ( P ; 0 )$by following the same procedure as in Section 5.4. There are only two differences: first, instead of setting$\mathcal { W } ( v ) = 0$for$v \in \bar { e }$in Step 4, we actually set$\mathcal { W } ( v ) = \kappa$for these two vertices. Then, at the end of the algorithm, we erase the edge e¯, so that the graph$( \hat { \mathcal { G } } , \hat { \mathcal { E } } )$that we consider is actually given by $\hat { \mathcal { G } } = \mathcal { G }$and$\hat { \mathcal { E } } = \mathcal { E } \setminus \{ \bar { e } \}$

We then have the following result:

Proposition 6.9 For a given$P \in \hat { \mathcal { P } } ^ { \tau }$, let$\mathcal { G } _ { \kappa } ^ { \tau } ( P ; 0 )$and$( \hat { \mathcal { G } } , \hat { \mathcal { E } } )$be as above. Ifthere exists$\kappa < 2$such that there exists a summable element in$\mathcal { G } _ { \kappa } ^ { \tau } ( P ; 0 )$, then

$$
\sum_ {L \in \mathcal {L} _ {P; 0} ^ {\tau}} \mathcal {F} _ {\alpha} (P, L) <   \infty ,
$$

$$
f o r \alpha = 1 - \frac {\kappa}{2}.
$$

Proof. The proof is virtually identical to that of Theorem 5.25, so we only focus on those steps that actually differ. Note first that the reason for erasing the edge e¯ after the last step is that the set of cycles of$( { \mathcal { G } } , { \mathcal { E } } )$that give the value 0 to e¯ and non-zero values to all other edges are, by definition, in a one-to-one correspondence with all cycles of$( \hat { \mathcal { G } } , \hat { \mathcal { E } } )$that give non-zero values to all edges in$\hat { \mathcal { E } }$.

This immediately yields the claim for the case$\kappa = 0$since in that case the proof of Theorem 5.25 implies that

$$
\sum_ {L \in \mathcal {L} _ {P; 0} ^ {\tau}} \sup _ {\delta \in \mathbf {R}} | \mathcal {F} _ {\text { sym }} ^ {\tau} (P, L; \delta) | <   \infty ,
$$

so that we do indeed have the required bound with$\alpha = 1 . \operatorname { I f } \kappa > 0$, we use the fact that we only need a bound on the integrated quantity

$$
\int_ {s} ^ {t} \int_ {s} ^ {t} \mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L; r - r ^ {\prime}) d r d r ^ {\prime}.
$$

As a consequence, in the last step of the proof of Theorem 5.25, we should replace (5.19) by the bound

$$
\begin{array}{l} \left| \int_ {s} ^ {t} \int_ {s} ^ {t} \mathcal {F} _ {\mathrm{sym}} ^ {\tau} (P, L; r - r ^ {\prime}) d r d r ^ {\prime} \right| \\ \lesssim \int_ {s} ^ {t} \int_ {s} ^ {t} \int_ {\mathbf {R} ^ {\bar {\mathcal {G}}}} \Big (\prod_ {e \in \hat {\mathcal {E}}} | \mathcal {S} L _ {e} | ^ {- \mathcal {L} _ {0} (e)} e ^ {- c (\mathcal {S} L) _ {e} ^ {2} | \delta T _ {e} |} \Big) \left(\prod_ {u \in \bar {\mathcal {G}}} d T _ {u}\right) d T _ {v} d T _ {\bar {v}}, \end{array}
$$

where we denote by v and v¯ the two vertices adjacent to e¯. One then proceeds in exactly the same way, but noting that for$a > 0$one has the inequality

$$
\int_ {s} ^ {t} e ^ {- a ^ {2} | u - x |} d x \leq | t - s | ^ {\alpha} | a | ^ {2 - 2 \alpha} = \frac {| t - s | ^ {\alpha}}{| a | ^ {\kappa}},
$$

uniformly in u, provided that$\begin{array} { r } { \alpha = 1 - \frac { \kappa } { 2 } } \end{array}$as in the statement of the proposition. The claim then follows by repeatedly applying Holder’s inequality, just like in the proof¨ of Theorem 5.25.□

We now have the required tool to construct the remaining processes$F ^ { \tau }$. We have:

Proposition 6.10 For every$\tau \in \{ \updownarrow , \psi , \psi \}$, there exists a limiting process$F ^ { \tau }$such that$F _ { \varepsilon } ^ { \tau } \to F ^ { \tau }$in probability in$\mathcal { C ^ { \alpha } }$for every$\alpha < 1$

Proof. By Propositions 6.8 and 6.9, it suffices to exhibit an element in$\mathcal { G } _ { \kappa } ^ { \tau } ( P ; 0 )$for every pairing$P \in \hat { \mathcal { P } } ^ { \tau }$. In the case of$\tau = \mathbb { V }$, there are only two such pairings that yield a non-empty set$\mathcal { L } _ { P ; 0 } ^ { \tau }$

![](images/page_78_image_10.jpg)

(Note that we display the graphs$( \hat { \mathcal { G } } , \hat { \mathcal { E } } )$for which the edge e¯ has been removed, this is why the two root vertices now only have degree 2.) As before, dotted lines have weight 0, dashed lines have weight κ, and plain lines have weight 1. Again, the loop and its adjacent edge in the first graph have weights as in (5.32), so that after the application of Algorithm 1, it is indeed equivalent to having an edge with weight 0. It is easy to see that both of these graphs are summable for every$\kappa > 0$, thus yielding the claim for$\tau = \mathbb { V }$

In the case$\tau = \mathbb { V } ,$, we can even take$\kappa = 0$. Indeed, recalling that the summability of graphs improves by removing edges, we note that if the criterion of Proposition 5.29 is satisfied for a given pairing$P ,$, then the assumption of Proposition 6.9 is satisfied with$\kappa = 0$

In the case$\tau = \mathbb { Y }$, the only pairings for which we have not verified that the criterion of Proposition 5.29 is satisfied are those for which there is a pairing connecting the two roots. There are exactly three such pairings left (one for each pairing of$\gamma$. One can then check that the following weights do belong to$\mathcal { G } _ { \kappa } ^ { \tau } ( P ; 0 )$ with the same colour-coding conventions as before:

![](images/page_79_image_3.jpg)

Again, it is straightforward to verify that they are all summable, thus concluding the proof.□

## 7 Fine control of the universal process

The purpose of this section is to show that, for each fixed$t > 0$, the process$\bar { X } ^ { \aleph } ( t )$ is controlled (in the sense of controlled rough paths) by the process Φ. Recall that, by definition,$\bar { X } ^ { \dag }$is given by

$$
\bar {X} ^ {\mathbb {V}} (t) = \partial_ {x} \int_ {- \infty} ^ {t} P _ {t - s} (\bar {X} ^ {\bullet} (s) \bar {X} ^ {\mathbb {V}} (s)) d s,
$$

where$P _ { t }$denotes the heat semigroup. Recall furthermore that the process$\Phi$can be written as

$$
\Phi (t) = \partial_ {x} \int_ {- \infty} ^ {t} P _ {t - s} \bar {X} ^ {\bullet} (s) d s.
$$

Comparing these two expressions, this suggests that$\bar { X } ^ { \aleph } ( t )$is controlled by$\Phi ( t )$ with “derivative process” given by$\bar { X } ^ { \forall } ( t )$. The aim of this section is to prove this fact, which is a crucial ingredient of our proofs.

In order to prove this, we would like to show that, for every$t > 0$, it is possible to build a rough path over the pair$( X ^ { \bullet } ( t ) , { \bar { X } } ^ { \aleph } ( t ) )$. This would then enable us to apply the results from Section 4.1 to show that$\bar { X } ^ { \aleph } ( t )$is indeed controlled by Φ. Actually, we will show slightly less, namely that the “rough path norm” for the pair$( X _ { \varepsilon } ^ { \bullet } ( t ) , \bar { X } _ { \varepsilon } ^ { \vee } ( t ) )$, with a suitably defined “area process” has uniformly bounded moments as$\varepsilon \to 0$. It is clear from the proofs that one actually has convergence to a limiting rough path, but the rigorous proof of his fact would be slightly tricky so that we skip it since we do not really need it.

For this, we need to build the integral of$\bar { X } ^ { \forall } ( t )$against$X ^ { \bullet } ( t )$. More precisely, we would like to obtain control, as$\varepsilon \to 0$, of the quantity

$$
\int_ {x} ^ {y} (\bar {X} _ {\varepsilon} ^ {\vee} (t, z) - \bar {X} _ {\varepsilon} ^ {\vee} (t, x)) \bar {X} _ {\varepsilon} ^ {\bullet} (t, z) d z.\tag{7.1}
$$

Unfortunately, this turns out to be impossible: the above quantity diverges logarithmically for any pair x and$y !$Fortunately, this divergence is not too difficult to control: indeed it arises from an “infinite constant”, which we subtract. The quantity that we will thus attempt to control is given by

$$
\begin{array}{l} \mathbf {X} _ {t} ^ {\varepsilon} (x, y) \stackrel {{\text { def }}} {{=}} \int_ {x} ^ {y} (\bar {X} _ {\varepsilon} ^ {\vee} (t, z) - \bar {X} _ {\varepsilon} ^ {\vee} (t, x)) \bar {X} _ {\varepsilon} ^ {\bullet} (t, z) d z - \frac {y - x}{2 \pi} \int_ {0} ^ {2 \pi} \bar {X} _ {\varepsilon} ^ {\vee} (t, z) \bar {X} _ {\varepsilon} ^ {\bullet} (t, z) d z \\ = \int_ {x} ^ {y} (\Pi_ {0} ^ {\perp} (\bar {X} _ {\varepsilon} ^ {\vee} (t) \bar {X} _ {\varepsilon} ^ {\bullet} (t)) (z) - \bar {X} _ {\varepsilon} ^ {\vee} (t, x) \bar {X} _ {\varepsilon} ^ {\bullet} (t, z)) d z. \end{array} \tag {7.2}
$$

Using Fourier components, we have the identity

$$
\begin{array}{r l} & {\mathbf {X} _ {t} ^ {\varepsilon} (x, y) = \sum_ {k \in \mathbf {Z} _ {\star}} \sum_ {m \in \mathbf {Z}} \int_ {x} ^ {y} \bar {X} _ {\varepsilon , k - m} ^ {\mathbb {V}} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) e ^ {i k z} (1 - e ^ {- i (k - m) (z - x)}) d z} \\ & {\qquad - \sum_ {m \in \mathbf {Z}} \int_ {x} ^ {y} \bar {X} _ {\varepsilon , - m} ^ {\mathbb {V}} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) e ^ {i m (z - x)} d z.} \end{array}\tag{7.3}
$$

Note that, since$\mathbf { X } _ { t } ^ { \varepsilon }$differs from (7.1) only by a term of the form$( y - x ) K _ { \varepsilon } ( t )$for some process$K _ { \varepsilon }$, it automatically satisfies the required consistency relation$( 3 . 1 )$for every$\varepsilon > 0 .$, so that it is a perfectly valid area process for the pair$( X _ { \varepsilon } ^ { \bullet } ( t ) , \bar { X } _ { \varepsilon } ^ { \vee } ( t ) )$

Remark 7.1 The logarithmic divergence arising in the construction of$\mathbf { X } _ { t } ^ { \varepsilon }$is really the same logarithmic divergence$\bar { C } _ { \varepsilon } ^ { \breve { \breve { \nu } } }$arising in the construction of$Y ^ { \ast }$in the following sense.$\operatorname { I f } ,$instead of (7.7) below, we considered the same expression with $p ^ { \prime }$replaced by$p$(which is essentially the definition of$Y _ { \varepsilon , t } ^ { \aleph } )$, then the difference between the rough integral$\mathcal { f }$and the usual Riemann integral would precisely result in a term that is constant in space and that kills the divergence in such a way that the resulting expression converges.

Remark 7.2 In a somewhat vague sense, propositions 5.18 and 5.32 suggest that $X ^ { \aleph }$behaves “as$\mathrm { i f } ^ { \dag }$it was composed of one part with regularity$\mathcal { C } ^ { \frac { 3 } { 2 } - \overline { { \beta } } }$that is independent of$X ^ { \bullet }$and one dependent part with regularity$\mathcal { C } ^ { 2 - \beta }$. Indeed, the bound of Proposition 5.32 would yield$\mathcal { C } ^ { 2 - \beta }$regularity for arbitrary$\beta > 0$if it held for all pairings$R _ { \cdot }$, while Proposition 5.18 precisely treats only those pairings that would arise if$X ^ { \forall }$and$X ^ { \bullet }$were independent.

If we could really decompose$\grave { \mathbf { X } ^ { \nu } }$as the sum of two processes with these properties, then we could make sense of the limit${ \bf X } _ { t } ^ { \varepsilon }  { \bf X } _ { t }$in almost exactly the same way as in [FV10a]. Unfortunately, while this argument is undoubtedly appealing, it doesn’t seem obvious how to make it work in a direct way.

The main technical bound of this section is the following:

Proposition 7.3 For every$\bar { \kappa } > 0 ,$, one has the bound

$$
\sup _ {\varepsilon \in (0, 1 ]} \sup _ {t \in \mathbf {R}} \mathbf {E} \| \mathbf {X} _ {t} ^ {\varepsilon} \| _ {1 - 2 \bar {\kappa}} ^ {2} <   \infty .\tag{7.4}
$$

Proof. In view of the definition (7.9), this is the content of propositions 7.10 and 7.11 below.□

Furthermore, it follows immediately from (3.10) that, for any smooth function f and for every$\varepsilon > 0$, one has the identity

$$
\oint_ {S ^ {1}} f (z) \bar {X} _ {\varepsilon} ^ {\mathbb {V}} (t, z) d X _ {\varepsilon} ^ {\bullet} (t, z) = \int_ {S ^ {1}} f (z) \Pi_ {0} ^ {\perp} (\bar {X} _ {\varepsilon} ^ {\mathbb {V}} (t) \bar {X} _ {\varepsilon} ^ {\bullet} (t)) (z) d z,\tag{7.5}
$$

where we used$\mathbf { X } _ { t } ^ { \varepsilon }$as the “area process” required to give meaning to the rough integral on the left hand side. Setting

$$
R _ {\varepsilon , t} ^ {\mathbb {V}} (x, y) = \delta \bar {X} _ {\varepsilon , t} ^ {\mathbb {V}} (x, y) - \bar {X} _ {\varepsilon , t} ^ {\mathbb {V}} (x) \delta \Phi_ {\varepsilon , t} (x, y),
$$

we then have the following consequence of Proposition 7.3, which is the main result of this section:

Theorem 7.4 One has$R _ { \varepsilon } ^ { \ast }  R ^ { \ast }$in probability in$\mathcal { C } ( \mathbf { R } , \mathcal { C } _ { 2 } ^ { 1 - \delta } )$for every$\delta > 0$

Proof. It is crucial to note that, with$\mathbf { X } _ { t } ^ { \varepsilon }$given by (7.2), one has the identity

$$
\bar {X} _ {\varepsilon , t} ^ {\mathbb {V}} = P _ {t} \bar {X} _ {\varepsilon , 0} ^ {\mathbb {V}} + (\mathcal {M} \bar {X} _ {\varepsilon} ^ {\mathbb {V}}) _ {t} (x),\tag{7.6}
$$

where we define M as in Section 4.1 by

$$
\left(\mathcal {M} v\right) _ {t} (x) = \int_ {0} ^ {t} \oint_ {S ^ {1}} p _ {t - s} ^ {\prime} (x - y) v _ {s} (y) d X _ {\varepsilon , s} ^ {\bullet} (y) d s,\tag{7.7}
$$

where v is a rough path controlled by$\bar { X } _ { \varepsilon } ^ { \vee }$(in this case trivially with$v ^ { \prime } = 1$and no remainder) and where we use$\mathbf { X } _ { \varepsilon }$to define the rough integral between the two processes. The reason why$_ { ( 7 . 6 ) }$holds with M defined with a “rough integral” is that, if we replace$f$by R in the definition of M, then it follows from (7.5) that we do not change the resulting expression since$p _ { t - s } ^ { \prime }$integrates to 0.

We are now able to apply the results of Section 4.1 with$Y = X _ { \varepsilon } ^ { \bullet } , Z = \bar { X } _ { \varepsilon } ^ { \aleph }$and $\mathbf { Y } = \mathbf { X } _ { \varepsilon }$. Setting

$$
\mathcal {K} _ {\varepsilon , t} ^ {\kappa} \stackrel {\mathrm{def}} {=} (1 + \| \bar {X} _ {\varepsilon , t} ^ {\vee} \| _ {\frac {1}{2} - \kappa} + \| X _ {\varepsilon , t} ^ {\bullet} \| _ {\frac {1}{2} - \kappa}) ^ {2} + \| \mathbf {X} _ {\varepsilon , t} \| _ {1 - 2 \kappa},
$$

it follows from Proposition 4.1 with$\begin{array} { r } { \kappa = \frac { 1 - \delta } { 4 } } \end{array}$and$\bar { \kappa } = \kappa$that one has the bound

$$
\begin{array}{r l} & {\| R _ {\varepsilon , t} ^ {\mathbb {V}} \| _ {1 - \frac {\delta}{2}} \lesssim t ^ {\frac {3}{8} (\delta - 1)} \| \bar {X} _ {\varepsilon , t} ^ {\mathbb {V}} \| _ {\infty} \| \Phi_ {0} \| _ {\frac {1 + \delta}{4}} + \int_ {0} ^ {t} (t - s) ^ {\frac {\delta}{4} - 1 - \kappa} \mathcal {K} _ {\varepsilon , s} ^ {\kappa} d s} \\ & {\qquad + \int_ {0} ^ {t} (t - s) ^ {\frac {\delta - 5}{4} - \frac {\kappa}{2}} \| X _ {\varepsilon , s} ^ {\bullet} \| _ {\frac {1}{2} - \kappa} \| \bar {X} _ {\varepsilon , t} ^ {\mathbb {V}} - \bar {X} _ {\varepsilon , s} ^ {\mathbb {V}} \| _ {\infty} d s.} \end{array}\tag{7.8}
$$

Note now that since$\mathbf { X } _ { \varepsilon } , \bar { X } _ { \varepsilon } ^ { \aleph }$and$X _ { \varepsilon } ^ { \bullet }$are all random variables belonging to a finite combination of Wiener chaoses of fixed order, it follows from propositions 7.3 and 5.30 that, for every$p > 0$, every$\kappa \in ( 0 , \frac { 1 } { 4 } )$), and every time interval$[ a , b ]$, one has the bound

$$
\mathbf {E} \int_ {a} ^ {b} (\mathcal {K} _ {\varepsilon , s} ^ {\kappa}) ^ {p} d s <   \infty ,
$$

uniformly over$\varepsilon \in ( 0 , 1 ]$. As a consequence, the second term in (7.8) is bounded in probability, uniformly over bounded intervals, provided that we choose$\kappa < \delta$ and that one chooses$p$sufficiently large. Similarly, the third term is bounded in probability by Proposition 5.30. Since the first term is harmless (except at$t = 0 .$ but it suffices to change the origin of time to deal with that), we have shown that, for every$T > 0$, one has the bound

$$
\sup _ {\varepsilon \in (0, 1 ]} \mathbf {E} \sup _ {t \in [ - T, T ]} \| R _ {\varepsilon , t} ^ {\mathbb {V}} \| _ {1 - \frac {\delta}{2}} <   \infty .
$$

To show that one actually has convergence towards$R ^ { \aleph }$, note first that convergence in the supremum norm follows from propositions 5.30 and 5.33. Since one has the interpolation inequality

$$
\| R \| _ {1 - \delta} \leq \| R \| _ {1 - \frac {\delta}{2}} ^ {\frac {2 - 2 \delta}{2 - \delta}} \| R \| _ {\infty} ^ {\frac {\delta}{2 - \delta}},
$$

the claim then follows.

The remainder of this section is devoted to the proof that the bound (7.4) does indeed hold. We are going to exploit the translation invariance so that, for simplicity, we use the shorthand notation

$$
\mathbf {X} _ {t} ^ {\varepsilon} (\delta) \stackrel {\mathrm{def}} {=} \mathbf {X} _ {t} ^ {\varepsilon} (0, \delta).
$$

Performing the integrals in (7.3), one obtains the identity

$$
\begin{array}{r l} & {\mathbf {X} _ {t} ^ {\varepsilon} (\delta) = \sum_ {k, m \in \mathbf {Z} _ {\star}} \bar {X} _ {\varepsilon , k - m} ^ {\mathbb {V}} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) \Big (\frac {e ^ {i k \delta} - 1}{k} - \frac {e ^ {i m \delta} - 1}{m} \Big)} \\ & {\qquad - \sum_ {m \in \mathbf {Z} _ {\star}} \bar {X} _ {\varepsilon , - m} ^ {\mathbb {V}} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) \frac {e ^ {i m \delta} - 1}{m}} \\ & {\stackrel {\mathrm{def}} {=} \mathbf {X} _ {t} ^ {(1), \varepsilon} (\delta) + \mathbf {X} _ {t} ^ {(2), \varepsilon} (\delta).} \end{array}\tag{7.9}
$$

We first consider$\mathbf { X } _ { t } ^ { ( 1 ) }$and postpone the bounds on$\mathbf { X } _ { t } ^ { ( 2 ) }$to the end of this section. In order to bound$\mathbf { X } _ { t } ^ { ( 1 ) }$, we rewrite its second moment as

$$
\begin{array}{r l} \mathbf {E} (\mathbf {X} _ {t} ^ {(1), \varepsilon} (\delta)) ^ {2} = & \sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \mathbf {E} (\bar {X} _ {\varepsilon , k - m} ^ {\vee} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) \bar {X} _ {\varepsilon , - k - \bar {m}} ^ {\vee} (t) \bar {X} _ {\varepsilon , \bar {m}} ^ {\bullet} (t)) \\ & \times \Big (\frac {e ^ {i k \delta} - 1}{k} - \frac {e ^ {i m \delta} - 1}{m} \Big) \Big (\frac {1 - e ^ {- i k \delta}}{k} - \frac {e ^ {i \bar {m} \delta} - 1}{\bar {m}} \Big). \end{array}\tag{7.10}
$$

(In principle, one should have a$\bar { k }$appearing, but the expectation is non-zero only if $\begin{array} { r } { \bar { k } = - k . } \end{array}$, so that the sum of all indices appearing under the expectation vanishes.) At this stage, it is useful to note that one has the identity

$$
\mathbf {E} (\bar {X} _ {\varepsilon , k - m} ^ {\vee} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) \bar {X} _ {\varepsilon , - k - \bar {m}} ^ {\vee} (t) \bar {X} _ {\varepsilon , \bar {m}} ^ {\bullet} (t)) = \sum_ {P \in \mathcal {P} ^ {\vee}} \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L) \mathcal {F} ^ {\vee} (P, L),\tag{7.11}
$$

where, similarly to (5.17), we set

$$
\mathcal {F} ^ {\tau} (P, C) = \left(\prod_ {e \in \bar {\mathcal {T}}} C _ {e}\right) \int \exp \left(- \sum_ {e \in \bar {\mathcal {E}}} | C _ {e} | ^ {2} | \delta T _ {e} |\right) \mu_ {0} (d T),
$$

and where we denoted by$\mathcal { L } _ { P ; k , m , \bar { m } } ^ { \tau }$the set of all cycles in$\mathcal { L } _ { P } ^ { \tau }$such that the edge$\bar { e }$ has value$k$and such that the two edges in${ \mathcal { E } } \setminus { \mathcal { T } }$adjacent to e¯ have values m and m¯ respectively. (By convention, we orient e¯ from the edge with label m to the one with label m¯ .)

Here,$\mathcal { E }$and$\tau$are as before the set of edges and the spanning tree for the graph associated to the tree$\updownarrow _ { \updownarrow }$and the pairing$P$in exactly the same way as in Section 5.4. Also, just as in that section,$\bar { \mathcal { E } }$and$\bar { \tau }$denote the same sets, but with the distinguished edge e¯ removed.

Remark 7.5 Since, at least at this stage, we fix the labels$k ,$, m and$\bar { m } .$, we cannot necessarily replace${ \mathcal { F } } ^ { \tau }$by$\mathcal { F } _ { \mathrm { { s y m } } } ^ { \tau }$. This will be the source of some minor headache later on.

Inserting (7.11) into (7.10), we have the identity

$$
\mathbf {E} \big (\mathbf {X} _ {t} ^ {(1), \varepsilon} (\delta) \big) ^ {2} = \sum_ {P \in \mathcal {P} ^ {\vee}} \mathbf {X} _ {P} ^ {\varepsilon} (\delta)  .
$$

The quantity$\mathbf { X } _ { P } ^ { \varepsilon }$appearing in this decomposition is defined by

$$
\mathbf {X} _ {P} ^ {\varepsilon} (\delta) = \sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L) \mathcal {F} ^ {\ddagger} (P, L) \big (g _ {k} (\delta) - g _ {m} (\delta) \big) \big (g _ {- k} (\delta) - g _ {\bar {m}} (\delta) \big)  ,\tag{7.12}
$$

where we used the shorthand notation

$$
g _ {k} (\delta) \stackrel {\mathrm{def}} {=} \frac {e ^ {i k \delta} - 1}{k}.
$$

We now proceed to bounding${ \bf X } _ { P } ( \delta )$for each pairing$P .$.

Proposition 7.6 For every$\boldsymbol { P } \in \mathcal { P } _ { s } ^ { \aleph }$and every$\kappa > 0$, the bound

$$
\mathbf {X} _ {P} ^ {\varepsilon} (\delta) \lesssim \delta^ {2 - 2 \kappa},\tag{7.13}
$$

holds uniformly over$\varepsilon , \delta \in ( 0 , 1 ]$

Proof. It follows from Proposition A.3 below that one has the bound

$$
\left| g _ {k} (\delta) - g _ {m} (\delta) \right| \leq 2 | k - m | \delta^ {2}.
$$

Since one also has the trivial bound$| g _ { k } ( \delta ) | \le 2 / | k |$, it follows that one has for every $\kappa > 0$the bound

$$
\left| g _ {k} (\delta) - g _ {m} (\delta) \right| \lesssim \delta^ {2 - 2 \kappa} | k - m | ^ {1 - \kappa} \left(| k | ^ {- 1} + | m | ^ {- 1}\right) ^ {\kappa}.\tag{7.14}
$$

Furthermore, by the definition of$\mathcal { P } _ { s }$, every$P \in \mathcal { P } _ { s } ^ { \aleph }$is associated to a$\bar { P } \in \mathcal { P } ^ { \forall }$ such that the remaining pair in$P$connects the two leaves attached to the roots. Similarly, for every$L \in \mathcal { L } _ { P ; k , m , \bar { m } } ^ { \check { \Psi } }$there exists a cycle$\Pi L \in \mathcal { L } _ { \hat { P } } ^ { \aleph }$such that ΠL agrees with$L$on the common parts of the two graphs and such that$\bar { ( } \Pi L ) _ { \bar { e } } = k - m$ Furthermore, Π is a bijection between$\mathcal { L } _ { P ; k , m , \bar { m } } ^ { \aleph }$and the subset$\mathcal { L } _ { \hat { P } ; k - m } ^ { \aleph }$of$\mathcal { L } _ { \hat { P } } ^ { \aleph }$ that we just mentioned.

We also note that if$\boldsymbol { P } \in \mathcal { P } _ { s } ^ { \aleph }$, one has$\mathcal { L } _ { P ; k , m , \bar { m } } ^ { \check { \Psi } } = \emptyset$unless$\bar { m } = - m$, since otherwise the cycles in that set are not adapted to the pairing$P$. As a consequence, one has the identity

$$
\begin{array}{l} \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L) \mathcal {F} ^ {\aleph_ {\vee}} (P, C) \\ = (k - m) ^ {2} \delta_ {m, - \bar {m}} \sum_ {\bar {L} \in \mathcal {L} _ {\bar {P}; k - m} ^ {\aleph_ {\vee}}} \varphi (\varepsilon (k - m))   C _ {\varepsilon} (\bar {L})   \mathcal {K} _ {\text {sym}} ^ {\aleph_ {\vee}} (\bar {P}, \bar {L}; 0)  . \end{array}
$$

Combining this with the bound (7.14) and summing the resulting expression over k and m, we obtain, for every$\kappa > 0$the bound

$$
\mathbf{X}_{P}^{\varepsilon}(\delta)\lesssim \delta^{2 - 2\kappa}\sum_{\bar{L}\in \mathcal{L}_{\bar{P}}^{\aleph}}\sum_{\substack{m\in Z_{\star}\\ m\neq \bar{L}_{\bar{e}}}}|\bar{L}_{\bar{e}}|^{3 - \kappa}|\mathcal{K}_{\text{sym}}^{\aleph}(\bar{P},\bar{L};0)|(|m + \bar{L}_{\bar{e}}|^{-1 - \kappa} + |m|^{-1 - \kappa})  ,\tag{7.15}
$$

uniformly over ε and δ. Since, by Proposition 5.30, the quantity

$$
| \bar {L} _ {\bar {e}} | ^ {3 - \kappa} | \mathcal {K} _ {\mathrm{sym}} ^ {\vee} (\bar {P}, \bar {L}; 0) | ,
$$

is summable over$\mathcal { L } _ { \bar { P } } ^ { \aleph } .$, the second term in (7.15) satisfies the requested bound. The claim now follows from the fact that the first term is essentially identical to the second one, as can be seen by performing the substitution$m \mapsto m - { \bar { L } } _ { \bar { e } }$□

We now proceed to bound the terms corresponding to the remaining pairings, which we subdivide into three different classes. Recall that$\ell _ { \ell } ^ { P } ( \tau )$denotes the set of leaves that are part of a small loop of type 1. Denote furthermore by u and u¯ the two leaves that are attached to either of the roots of the two copies of$\updownarrow ,$. We then define$\mathcal { P } ^ { k } ( \mathbb { Y } )$with$k \in \{ 0 , 1 , 2 \}$as consisting of those pairings in$\mathcal { P } ^ { \aleph } \setminus \mathcal { P } _ { s } ^ { \aleph }$such that$| \{ u , \bar { u } \} \cap \ell _ { \ell } ^ { P } ( \check { \zeta } _ { \ell } ) | = k .$. We then have:

Proposition 7.7 For every$P \in \mathcal { P } ^ { 0 } ( \mathfrak { E } )$and every$\kappa > 0 ,$, there exists$C$such that the bound (7.13) holdsfor$\varepsilon \in ( 0 , 1 ]$

Proof. For such a pairing, one has the identity

$$
\sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L) \mathcal {F} ^ {\tau} (P, L) = \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L) \mathcal {F} _ {\text { sym }} ^ {\tau} (P, L),
$$

where as before we denote by$\mathcal { F } _ { \mathrm { { s y m } } } ^ { \tau }$the symmetrised version of$\mathcal { F } ^ { \tau }$under the equivalence relation${ \underset { \sim } { \ / { \sim } } } { \underset { \ / { \sim } } { \ / { \ / { \ / { \ / { \ / { \ / { \ / { \sim } } } } } } } } }$. (Here and below, we sometimes use τ instead of$\updownarrow _ { \updownarrow }$in order to make notations slightly less heavy.) Indeed, if$P \in \mathcal { P } ^ { 0 } ( \mathfrak { E } )$and$L \in \mathcal { L } _ { P ; k , m , \bar { m } } ^ { \tau } ,$ then$\bar { L } \in \mathcal L _ { P ; k , m , \bar { m } } ^ { \tau }$for every$\bar { L }$with$\bar { L } \stackrel { P } { \sim } L$, since none of the loops whose labels can change sign touches the distinguished edge e¯.

Recall furthermore that$| g _ { k } ( \delta ) | \le \delta$so that, for every$\kappa \in [ 0 , 1 ]$, one has the bound

$$
\begin{array}{r l r} & & {\delta^ {2 \kappa - 2} | (g _ {k} (\delta) - g _ {m} (\delta)) (g _ {- k} (\delta) - g _ {\bar {m}} (\delta)) | \lesssim | k | ^ {- 2 \kappa} + (| m | ^ {- 2 \kappa} \wedge | \bar {m} | ^ {- 2 \kappa})} \\ & & {\lesssim | k | ^ {- 2 \kappa} + | m | ^ {- \kappa_ {1}} | \bar {m} | ^ {- \kappa_ {2}},} \end{array}\tag{7.16}
$$

where$\kappa _ { 1 }$and$\kappa _ { 2 }$are any two positive exponents with$\kappa _ { 1 } + \kappa _ { 2 } = 2 \kappa$. Recalling the definition of$\mathbf { X } _ { P } ^ { \varepsilon }$, we see that the requested bound follows, provided that we are able to show that, for every pairing$P \in \mathcal { P } ^ { 0 } ( \mathfrak {k } )$and every$\kappa > 0$, one can find exponents $\kappa _ { 1 }$and$\kappa _ { 2 }$as above such that

$$
\sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} (| k | ^ {- 2 \kappa} + | m | ^ {- \kappa_ {1}} | \bar {m} | ^ {- \kappa_ {2}}) | \mathcal {F} _ {\text {sym}} ^ {\ddot {\vee} _ {\mathbb {Y}}} (P, L; 0) | <   \infty .
$$

It follows from Proposition 5.32 that

$$
\sum_ {k, m, \bar {m} \in {\bf Z} _ {\star}} \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} | k | ^ {- 2 \kappa} | \mathcal {F} _ {\mathrm{sym}} ^ {\ddot {\times}} (P, L; 0) | <   \infty ,\tag{7.17}
$$

for every$\kappa > 0$, so that it remains to show that

$$
\sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} | m | ^ {- \kappa_ {1}} | \bar {m} | ^ {- \kappa_ {2}} \mathcal {F} _ {\mathrm{sym}} ^ {\mathbb {V}} (P, L; 0) <   \infty .\tag{7.18}
$$

For$P \in \mathcal { P } ^ { 0 } ( \mathfrak { Y } _ { \mathfrak { c } } )$and$\kappa > 0$, we now define a set$\bar { \mathcal { G } } _ { \kappa } ^ { \tau , 0 } ( P )$of weightings by following the construction in Section 5.4. Comparing (7.18) and (7.17) we see that, in order to obtain a bound on (7.18), the only difference in the construction is that, in Step 2, we give weight 0 to the distinguished edge e¯, and weights$\kappa _ { 1 }$and$\kappa _ { 2 }$to the two edges adjacent to e¯ that do not belong to the spanning tree$\tau$.

Retracing the proof of Theorem 5.25 we see that, if we can exhibit an element in$\bar { \mathcal { G } } _ { \kappa } ^ { \tau , 0 } ( P )$such that Algorithm 1 yields a loop-free graph, then the bound (7.18) holds. It can be checked in a straightforward way that the following weightings do indeed belong to$\bar { \mathcal { G } } _ { \kappa } ^ { \tau , 0 } ( P )$

![](images/page_86_image_2.jpg)

Here, we use again the same convention as in the proof of Proposition 5.32. The only difference is that the dashed lines correspond to a weight 2κ if only one dashed line is present in a given graph, and κ if two such lines are present. Again, it is straightforward to verify that Algorithm 1 does indeed yield a loop-free graph for every$\kappa > 0$in each instance, thus proving the claim.□

We now turn to the set$\mathcal { P } ^ { 1 }$of pairings that have one small loop touching the distinguished edge. There are actually only two such pairings (modulo isometries), corresponding to the 8th and the 10th pairing in (5.31).

Proposition 7.8 For every$P \in \mathcal { P } ^ { 1 } ( \mathfrak { Y } _ { \mathfrak { c } } )$and every$\kappa > 0 ,$, the bound (7.13) holds uniformly over$\varepsilon , \delta \in ( 0 , 1 ]$

Proof. By the definition of$\mathcal { P } ^ { 1 }$, there is one small loop touching the distinguished edge. We can then fix our naming convention in such a way that the edge of this loop that doesn’t belong to the spanning tree$\tau$is the one labelled m. With this convention, we then introduce a “reflection ma$\cdots \mathcal { R } : \mathcal { L } _ { P ; k , m , \bar { m } } ^ { \tau } \to \mathcal { L } _ { P ; k , - m , \bar { m } } ^ { \tau } ,$ which is the bijection which changes the sign of m and adjust the label of the other edge of the small loop in such a way that no other label is changed. In other words, if we decompose elements in$\mathcal { L } _ { P ; k , m , \bar { m } } ^ { \tau }$with respect to the integral basis associated with the spanning tree$\tau _ { \cdot }$, then$\mathcal { R }$is the map that changes the sign of the coefficient in front of the elementary cycle spanning the small loop.

With this notation, although we cannot quite replace$\mathcal { F } ^ { \tau }$by$\mathcal { F } _ { \mathrm { { s y m } } } ^ { \tau }$in (7.12), we nevertheless have the identity

$$
\sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} \big (\mathcal {F} ^ {\mathbb {V} _ {\mathbb {V}}} (P, L) + \mathcal {F} ^ {\mathbb {V} _ {\mathbb {V}}} (P, \mathcal {R} L) \big) = 2 \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} \mathcal {F} _ {\mathrm{sym}} ^ {\mathbb {V} _ {\mathbb {V}}} (P, L),
$$

Using this identity, we can decompose (7.12) into a symmetric part and a remainder, which yields the expression

$$
\begin{array}{l} \mathbf {X} _ {P} ^ {\varepsilon} (\delta) = \sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \Big (\sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L)   \mathcal {F} _ {\mathrm{sym}} ^ {\ddot {\vee} _ {\dot {\vee}}} (P, L; 0) \Big) g _ {k} (\delta) \big (g _ {- k} (\delta) - g _ {\bar {m}} (\delta) \big) \\ \qquad - \sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \Big (\sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L)   \mathcal {F} ^ {\ddot {\vee} _ {\dot {\vee}}} (P, L; 0) \Big) g _ {m} (\delta) \big (g _ {- k} (\delta) - g _ {\bar {m}} (\delta) \big)  . \end{array}
$$

The first term in this identity is bounded by

$$
\sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} | \mathcal {F} _ {\mathrm{sym}} ^ {\ddagger} (P, L; 0) | | k | ^ {- 2 \kappa} \delta^ {2 - 2 \kappa},
$$

which in turn is bounded by$C \delta ^ { 2 - 2 \kappa }$by Proposition 5.32.

Similarly, the second term is bounded by

$$
\delta^ {2 - 2 \kappa} \sum_ {k, m, \bar {m} \in \mathbf {Z} _ {\star}} \Big | \sum_ {L \in \mathcal {L} _ {P; k, m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L) \mathcal {F} ^ {\ddot {\mathbb {V}}} (P, L; 0) \Big | | m | ^ {- 2 \kappa},\tag{7.19}
$$

which is not quite covered by Proposition 5.32 since the terms are weighted by a power of$m ,$, the label of the edge within the small loop, instead of$k ,$, the label of the distinguished edge.

Similarly to Proposition$7 . 7 ,$we now define a set$\bar { \mathcal { G } } _ { \kappa } ^ { \tau , 1 } ( P )$of weightings by again following the construction in Section 5.4. This time, in Step 2, we give weight 0 to the distinguished edge$\bar { e } ,$and we give instead an additional weight 2κ to the edge in${ \mathcal { E } } \setminus { \mathcal { T } }$adjacent to e¯ that belongs to a small loop of type 1. Since the kernel $\mathcal { F }$is not symmetrised under$\mathcal { R }$, another difference in the construction of$\bar { \mathcal { G } } _ { \kappa } ^ { \tau , 1 } ( P )$is that in Step 3, we do not treat the loop that touches$\bar { e } .$

Retracing once again the proof of Theorem 5.25 we see that, if we can exhibit an element in$\bar { \mathcal { G } } _ { \kappa } ^ { \tau , 1 } ( P )$such that Algorithm 1 yields a loop-free graph, then the quantity (7.19) is bounded by$C \delta ^ { 2 - 2 \kappa }$for some$C < \infty$, which is the desired bound. Note now that, in the proof of Proposition 5.32, the weightings that are exhibited for pairings in$\mathcal { P } ^ { 1 } ( \mathbb { \backslash } _ { \mathsf { V } } )$locally look like

![](images/page_88_image_1.jpg)

(7.20)

It is straightforward to check that under the rules for constructing$\bar { \mathcal { G } } _ { \kappa } ^ { \tau , 1 } ( P )$, these configurations can instead be weighted in the following way:

![](images/page_88_image_4.jpg)

(7.21)

Since Algorithm 1 has the same effect on both of these configurations, at least if κ is small enough (one can just replace them by one single edge with weight 2κ), the summability of (7.19) follows in the same way as before.□

Finally, we also have the bound

Proposition 7.9 For every$P \in \mathcal { P } ^ { 2 } ( \mathfrak { Y } _ { \mathfrak { c } } )$and every$\kappa > 0 ,$, the bound (7.13) holds uniformly over$\varepsilon , \delta \in ( 0 , 1 ]$

Proof. The proof is virtually identical to that of Proposition 7.8, so we only highlight the differences. We now have two small loops touching the distinguished edge, so that the expression for${ \bf X } _ { P } ^ { \varepsilon } ( \delta )$is broken into four terms, since each of the two loops can either be symmetrised or not. Then, as before, the symmetrised loops are associated to weightings as in the proof of Proposition 5.32, while the non-symmetrised loops are associated to weightings as in (7.21).□

Combining these results, we obtain the following result:

Proposition 7.10 For every$\bar { \kappa } > 0 _ { : }$, one has the bound

$$
\sup _ {\varepsilon \in (0, 1 ]} \sup _ {t \in \mathbf {R}} \mathbf {E} \| \mathbf {X} _ {t} ^ {(1), \varepsilon} \| _ {1 - \bar {\kappa}} ^ {2} <   \infty .
$$

Proof. Since$\mathbf { X } _ { t } ^ { ( 1 ) , \varepsilon }$belongs to a finite union of fixed Wiener chaoses, it follows from Propositions 7.6–7.9 that, for every$\kappa > 0$and every$p > 0$, the bound

$$
\mathbf {E} | \mathbf {X} _ {t} ^ {(1), \varepsilon} (x, y) | ^ {p} \lesssim | x - y | ^ {p (1 - \kappa)},
$$

holds uniformly in$\boldsymbol { \varepsilon } \in ( 0 , 1 ] , t \in \mathbf { R }$, and$x , y \in S ^ { 1 }$. The requested bound then follows from [Gub04, Cor. 4].□

We now consider the term$\mathbf { X } _ { t } ^ { ( 2 ) , \varepsilon } ( \delta )$which can be treated in a similar manner. One has:

Proposition 7.11 The conclusions ofProposition 7.10 holds, with (1) replaced by (2) throughout.

Proof. In the same way as before, it suffices to show that

$$
\mathbf {E} (\mathbf {X} _ {t} ^ {(2), \varepsilon} (\delta)) ^ {2} \lesssim \delta^ {2 - 2 \kappa},
$$

uniformly over$\varepsilon , \delta \in ( 0 , 1 ]$. In exactly the same way as before, we have the identity

$$
\mathbf {E} \big (\mathbf {X} _ {t} ^ {(2), \varepsilon} (\delta) \big) ^ {2} = \sum_ {m, \bar {m} \in \mathbf {Z} _ {\star}} \mathbf {E} \big (\bar {X} _ {\varepsilon , - m} ^ {\vee} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) \bar {X} _ {\varepsilon , - \bar {m}} ^ {\vee} (t) \bar {X} _ {\varepsilon , \bar {m}} ^ {\bullet} (t) \big) g _ {m} (\delta) g _ {\bar {m}} (\delta) ,\tag{7.22}
$$

with

$$
\mathbf {E} \big (\bar {X} _ {\varepsilon , - m} ^ {\vee} (t) \bar {X} _ {\varepsilon , m} ^ {\bullet} (t) \bar {X} _ {\varepsilon , - \bar {m}} ^ {\vee} (t) \bar {X} _ {\varepsilon , \bar {m}} ^ {\bullet} (t) \big) = \sum_ {P \in \mathcal {P} ^ {\tau}} \sum_ {L \in \mathcal {L} _ {P; m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L)   \mathcal {F} ^ {\tau} (P, L)\tag{7.23}
$$

Here, by analogy with the previous notations of this section, we denoted by$\mathcal { L } _ { P ; m , \bar { m } } ^ { \tau }$ the set of all cycles in$\mathcal { L } _ { P ; 0 } ^ { \tau }$such that the edge e¯ (and only that edge) has value 0 and the edges in$\mathcal { E } \backslash \mathcal { T }$adjacent to e¯ have values m and m¯ respectively.

Similarly to before, for any given$\kappa \in ( 0 , \frac { 1 } { 2 } ]$, and for any two positive exponents$\kappa _ { 1 }$and$\kappa _ { 2 }$with$\kappa _ { 1 } + \kappa _ { 2 } = 2 \kappa$, we have the bound$| g _ { m } ( \delta ) g _ { \bar { m } } ( \delta ) | \ \leq$ $\bar { \delta } ^ { 2 - 2 \kappa } | m | ^ { - \kappa _ { 1 } } | \bar { m } | ^ { - \kappa _ { 2 } }$, so that the statement reduces to the proof that

$$
\sum_ {m, \bar {m} \in \mathbf {Z} _ {\star}} \Big (\sum_ {L \in \mathcal {L} _ {P; m, \bar {m}} ^ {\tau}} C _ {\varepsilon} (L) \mathcal {F} ^ {\tau} (P, L) \Big) | m | ^ {- \kappa_ {1}} | \bar {m} | ^ {- \kappa_ {2}} <   \infty ,\tag{7.24}
$$

uniformly over$\varepsilon \in ( 0 , 1 ]$

The proof follows again the same lines as before. For every pairing$P \in \mathcal P ^ { \aleph }$ we construct a set$\hat { \mathcal { G } } _ { \kappa } ^ { \tau } ( P )$of weightings by following the construction in Section 5.4. Again, we give e¯ the weight 0, and weigh instead the two edges in${ \mathcal { E } } \setminus { \mathcal { T } }$adjacent to e¯ by$\kappa _ { 1 }$and$\kappa _ { 2 }$respectively. Note that, since the inner sum in (7.24) has m and m¯ fixed, we cannot symmetrise small loops that touch the distinguished edge. As a consequence, in Step 3 of the construction, we only treat those small loops that do not touch e¯. This however is not a problem, since the loops touching e¯ receive an additional weight$\kappa _ { i }$anyway, which has the same effect. Furthermore, since this time we restrict our sum to cycles that associate to e¯ the value 0, we remove the edge e¯ from the graph (G, E) before applying Algorithm 1.

Retracing the proof of Theorem 5.25 we see once again that if, for every pairing $P \in \mathcal { P } ^ { \tau }$, we can exhibit an element in$\hat { \mathcal { G } } _ { \kappa } ^ { \tau } ( P )$such that Algorithm 1 yields a loop free graph, then the requested bound holds. On the other hand, as far as the outcome of Algorithm 1 is concerned, deleting an edge (not contracting it!) is the same as giving it a weight larger than the largest weight in the graph. As a consequence, every weighting constructed in Propositions 7.7–7.9 also yields a weighting in $\hat { \mathcal { G } } _ { \kappa } ^ { \tau } ( P )$that is summable. Furthermore, pairings in$\mathcal { P } _ { s } ^ { \tau }$can be treated “by hand” in very much the same way as in Proposition 7.6.

There still remains one case to verify though. Previously, we only considered pairings such that there exists at least one pair connecting the two instances of the tree τ. This was precisely because any labelling compatible with a pairing that doesn’t have this property would associate 0 to the root vertex, which we always ruled out. This time however, this is precisely the situation that we are considering, so that we cannot make this restriction. As a consequence, we also have to consider the following pairing:

![](images/page_90_image_2.jpg)

(7.25)

Here, as before, the two dashed edges have weight κ, while the loops and the remaining edges are weighted in such a way that, after applying one step of Algorithm 1, they reduce to an edge with weight 1. This weighted graph is summable by applying Algorithm 1, which then concludes the proof in the same way as in Proposition 7.10.

Remark 7.12 The last step is the only step in the proof of Proposition 7.11 where the additional weight κ is actually needed. In all other cases, erasing e¯ significantly improves the summability properties of the resulting graphs, so that the resulting expressions would already have been summable with$g _ { m } ( \delta ) = \delta$. This shows that it is precisely the presence of the graph (7.25) that requires the projection operator $\Pi _ { 0 }$in the definition (7.2). Indeed, if we remove$\Pi _ { 0 }$from this expression, we see that the difference results in a term like (7.22), but with$g _ { m } ( \delta ) = \delta$, so that this last pairing would result in a logarithmic divergence.

## 7.1 Construction of the area process

To conclude the construction of the map Ψ, we show that the sequence of processes $\mathbf { Y } _ { \varepsilon }$defined by (2.16) does indeed have a limit as$\varepsilon \to 0$

Proposition 7.13 Let$\Phi _ { \varepsilon } , Y _ { \varepsilon } ^ { \bullet }$and$\mathbf { Y } _ { \varepsilon }$be given by (2.13) and (2.16). Then, there exists a process Y such that$\mathbf Y _ { \varepsilon } \to \mathbf Y$in probability in the space$\mathcal { C } ( \mathbf { R } , \mathcal { C } _ { 2 } ^ { 1 - \delta } )$for every$\delta > 0$

Proof. The argument is essentially the same as the one given in [Hai11], which in turn relies very heavily on the results in [FV10a, FV10b], so we only explain the main steps and refer to [Hai11] for more details.

Recall that, by definition, the Fourier components of$Y _ { \varepsilon } ^ { \bullet }$(for$k \neq 0 )$are given by

$$
Y _ {\varepsilon , k} ^ {\bullet} (t) = \sqrt {2} \varphi (k \varepsilon) \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} d W _ {k} (s),
$$

where the$W _ { k }$are independent normal complex-valued Wiener processes satisfying the reality condition$W _ { - k , t } = \bar { W } _ { k , t }$. Similarly, the Fourier components of$\Phi _ { \varepsilon }$<sub>ε</sub> are given by

$$
\Phi_ {\varepsilon , k} (t) = k ^ {2} \int_ {- \infty} ^ {t} e ^ {- k ^ {2} (t - s)} Y _ {k, s} ^ {\bullet} d s = \sqrt {2} \varphi (k \varepsilon) \int_ {- \infty} ^ {t} k ^ {2} (t - s) e ^ {- k ^ {2} (t - s)} d W _ {k} (s).
$$

An explicit calculation (boiling down to the fact that$\begin{array} { r } { \int _ { 0 } ^ { \infty } ( x - \frac { 1 } { 2 } ) e ^ { - 2 x } d x = 0 ) } \end{array}$ then shows that if we define a process$\tilde { \Phi } _ { \varepsilon }$by

$$
\Phi_ {\varepsilon} = \frac {1}{2} Y _ {\varepsilon} ^ {\bullet} + \tilde {\Phi} _ {\varepsilon},
$$

then, for everyfixed$t \in \mathbf { R }$, the processes$\tilde { \Phi } _ { \varepsilon } ( t )$and$Y _ { \varepsilon } ^ { \bullet } ( t )$are independent. It then follows from [FV10b] that${ \bf Y } _ { \varepsilon } ( t )  { \bf Y } ( t )$in probability in$\mathcal { C } _ { 2 } ^ { 1 - \delta }$for every$\delta > 0$ The convergence in$\mathcal { C } ( [ - T , T ] , \mathcal { C } _ { 2 } ^ { 1 - \delta } )$then follows from Kolmogorov’s continuity criterion by [FV10a, Theorem 1].□

We now finally have all the ingredients in place for the proof of Theorem 2.3.

ProofofTheorem 2.3. The case$\tau = \bullet$is standard, see for example [DPZ92]. The cases$\tau \in \{ \mathrm { v } , \mathrm { \backslash } , \mathrm { \backslash } \mathrm { \backslash } , \mathrm { \backslash } \mathrm { \backslash } \mathrm { \backslash } \}$follow by combining the results of Section 5, which yield the convergence of the processes$X ^ { \tau }$, with the results of Section 6, which furthermore yield the convergence of the constant Fourier modes of$Y ^ { \tau }$

The remaining cases are treated by induction. Assume that${ \tau } = [ { \tau } _ { 1 } , { \tau } _ { 2 } ]$with $\alpha _ { \tau _ { 1 } } \leq \alpha _ { \tau _ { 2 } }$. The case$\tau _ { 1 } = \bullet$will be treated separately. If$\tau _ { 1 } \neq \bullet$, then we have $\alpha _ { \tau _ { 1 } } \geq 1$and$\alpha _ { \tau _ { 2 } } > 1$(since the case of both being equal to 1 corresponds to the tree which was already covered). As a consequence, we can use the induction hypothesis, combined with Proposition A.9 to conclude that the term$\partial _ { x } Y _ { \varepsilon } ^ { \tau _ { 1 } } \partial _ { x } Y _ { \varepsilon } ^ { \tau _ { 2 } }$ converges to$\partial _ { x } Y ^ { \tau _ { 1 } } \partial _ { x } Y ^ { \tau _ { 2 } }$in$\bar { \mathcal { C } } ( \mathbf { R } , \mathcal { C } ^ { \alpha _ { \tau } - 2 - \delta } )$for every$\delta > 0$. The claim then follows from the definition of$Y ^ { \tau }$, combined with Proposition A.11.

It remains to treat the case when$\tau = [ \bullet , \bar { \tau } ]$with$\alpha _ { \bar { \tau } } > 1$. For these, we actually show a stronger statement, namely that,$\partial _ { x } Y _ { \varepsilon } ^ { \tau } \to \partial _ { x } Y ^ { \tau }$as a rough path controlled by$\Phi _ { \varepsilon }$with derivative process$\partial _ { x } Y _ { \varepsilon } ^ { \bar { \tau } }$. By the results of this section, this is true for $\tau = \mathbb { Y } _ { \ast } .$, so that it suffices to prove the statement for the remaining trees of this form. Again, there are two cases. If$\alpha _ { \bar { \tau } } \geq 1$, we view$\partial _ { x } Y _ { \varepsilon } ^ { \bar { \tau } }$as a rough path controlled by$\Phi _ { \varepsilon }$with vanishing derivative process, so that Proposition 4.1 yields the desired statement.$\operatorname { I f } { \bar { \tau } }$is itself of the form$\bar { \boldsymbol { \tau } } = [ \bullet , \kappa ]$, then we know by the induction hypothesis that$\partial _ { x } Y _ { \varepsilon } ^ { \bar { \tau } }$is controlled by$\Phi _ { \varepsilon }$with derivative process$\partial _ { x } Y _ { \varepsilon } ^ { \kappa }$and bounds that are uniform in ε. The claim then follows again from Proposition 4.1.□

## Appendix A Useful computations

## A.1 Wiener chaos

In this section, we assume that we work on a probability space$( \Omega , { \bf P } , { \mathcal { F } } )$equipped with a Gaussian structure. In other words, there exists a separable Hilbert space $\mathcal { H }$and an isometry$\iota \colon \mathcal { H }  L ^ { 2 } ( \Omega , \mathbf { P } )$such that$\iota ( h )$is a centred Gaussian random variable for every$h \in { \mathcal { H } }$

Denote now by$\mathcal { P } _ { k , m }$the set of all polynomials of degree k in m variables. We then write$\mathcal { T } _ { k }$for the closure in$L ^ { 2 } ( \Omega , { \bf P } )$of the set

$$
\left\{P \left(\iota \left(h _ {1}\right), \dots , \iota \left(h _ {m}\right)\right): P \in \mathcal {P} _ {k, m}, h _ {j} \in \mathcal {H}, m \geq 1 \right\}.
$$

Given a separable Banach space$B ,$we also write$\mathcal { T } _ { k } ( B )$for the same space, but where$P$is B-valued. The space$\mathcal { T } _ { k }$is the union of the nth Wiener chaoses for Ω with $n \leq k$. Since the precise definition of the nth Wiener chaos over a given Gaussian structure is only marginally relevant for this article, we refer to the monograph [Nua95] for more details.

A very useful fact is given by the following lemma, which follows from the hypercontractivity of the Ornstein-Uhlenbeck semigroup on$L ^ { 2 } ( \Omega )$[Nua95] and is also known as Nelson’s estimate:

Lemma A.1 Let$( \Omega , { \bf P } , { \mathcal { F } } )$be a Gaussian probability space, let B be a separable Banach space, and denote$\mathcal { T } _ { k } ( B )$as before. Then, for every$k , p \geq 1$there exist constants$C _ { k , p }$such that

$$
\mathbf {E} | F | ^ {2 p} \leq C _ {k, p} (\mathbf {E} | F | ^ {2}) ^ {p},
$$

for every every B-valued random variable$F \in \mathcal { T } _ { k } ( \mathcal { B } )$.

Our main application of this estimate is the following bound, which loosely speaking states that in the context of processes taking values in a fixed Wiener chaos, Sobolev regularity for a given index often implies Holder regularity for the same¨ index.

Proposition A.2 Let$\mathcal { J }$be a countable index set, let$T > 0$, and let$\{ g _ { \kappa } \} _ { \kappa \in \mathcal { I } }$be afamily ofLipschitz continuousfunctions such that.

$$
\left\| g _ {\kappa} \right\| _ {\infty} \leq 1, \quad \left\| g _ {\kappa} \right\| _ {1} \leq G _ {\kappa},
$$

for some$G _ { \kappa } \geq 1$. In general, we assume that the$g _ { \kappa }$are complex-valued and tha there is an involution$\iota \colon \mathcal { J }  \mathcal { J }$such that$g _ { \iota \kappa } = \bar { g } _ { \kappa }$

Let furthermore$\{ f _ { \kappa } \} _ { \kappa \in \mathcal { I } }$be a family of continuous stochastic processes belonging to$\mathcal { T } _ { k }$for somefixed value$k \in \mathbf { N } ,$and write

$$
F _ {\kappa \eta} (t) = \mathbf {E} f _ {\kappa} (t) f _ {\eta} (t), \quad \hat {F} _ {\kappa \eta} (s, t) = \mathbf {E} \big (f _ {\kappa} (t) - f _ {\kappa} (s) \big) \big (f _ {\eta} (t) - f _ {\eta} (s) \big).
$$

We also assume that$f _ { \iota \kappa } = \bar { f } _ { \kappa }$. Finally, let$\{ C _ { \varepsilon } \} _ { \varepsilon \in ( 0 , 1 ] }$be a family offunctions $C _ { \varepsilon } \colon \mathcal { J }  [ 0 , 1 ]$such that

• one has$C _ { \varepsilon } ( \kappa ) > C _ { \bar { \varepsilon } } ( \kappa ) f o r \varepsilon < \bar { \varepsilon } ,$

• for every$\varepsilon > 0 ,$, the set$\{ \kappa : C _ { \varepsilon } ( \kappa ) \neq 0 \}$is finite,

• for every$\kappa \in { \mathcal { J } }$, one has$\begin{array} { r } { \operatorname* { l i m } _ { \varepsilon \to 0 } C _ { \varepsilon } ( \kappa ) = 1 } \end{array}$

For every$\varepsilon > 0 ,$let$F _ { \varepsilon }$be the stochastic process defined by

$$
F _ {\varepsilon} (x, t) = \sum_ {\kappa \in \mathcal {J}} C _ {\varepsilon} (\kappa) f _ {\kappa} (t) g _ {\kappa} (x),\tag{A.1}
$$

and assume that there exists$\alpha \in ( 0 , 1 )$and$\beta \geq 0$such that

$$
\begin{array}{l} \sum_ {\kappa , \eta \in \mathcal {J}} \sup _ {t \in [ 0, T ]} | G _ {\kappa} | ^ {\alpha} | G _ {\eta} | ^ {\alpha} | F _ {\kappa \eta} (t) | <   \infty  , \\ \sum_ {\kappa , \eta \in \mathcal {J}} \sup _ {s, t \in [ 0, T ]} \frac {| \hat {F} _ {\kappa \eta} (s , t) |}{| t - s | ^ {2 \beta}} <   \infty  , \end{array}\tag{A.2}
$$

Then, for every$\gamma \ < \ \alpha$and$\delta \ < \ \beta ,$, there exists a process F taking values in $B _ { \gamma , \delta } \overset { d e f } { = } \mathcal { C } ( [ 0 , T ] , \mathcal { C } ^ { \gamma } ) \cap \mathcal { C } ^ { \delta } ( [ 0 , T ] , \mathcal { C } )$and such that$F _ { \varepsilon } \to F$in$L ^ { 2 } ( \Omega , \mathcal { P } , B _ { \gamma , \delta } )$

Proof. It suffices to show that our conditions imply that the sequence$\{ F _ { \varepsilon } \}$is Cauchy in$L ^ { 2 } ( \Omega , \mathcal { P } , B _ { \gamma , \delta } )$. Fix$0 < \varepsilon < \bar { \varepsilon }$and write$C _ { \varepsilon } ^ { \bar { \varepsilon } } ( \kappa )$as a shorthand for $C _ { \varepsilon } ( \kappa ) - C _ { \bar { \varepsilon } } ( \kappa )$, and similarly$F _ { \varepsilon } ^ { \bar { \varepsilon } } = F _ { \varepsilon } - F _ { \bar { \varepsilon } }$. By our assumption on$C _ { \varepsilon }$, we have $C _ { \varepsilon } ^ { \bar { \varepsilon } } ( \kappa ) \geq 0$for every κ.

We furthermore write

$$
F _ {\kappa \eta} \stackrel {{\text { def }}} {{=}} \sup _ {t \in [ 0, T ]} | F _ {\kappa \eta} (t) |  , \qquad \hat {F} _ {\kappa \eta} \stackrel {{\text { def }}} {{=}} \sup _ {s, t \in [ 0, T ]} \frac {| \hat {F} _ {\kappa \eta} (s , t) |}{| t - s | ^ {2 \beta}}  .
$$

An elementary calculation then shows that

$$
\begin{array}{l} \mathbf {E} | F _ {\varepsilon} ^ {\bar {\varepsilon}} (x, t) | ^ {2} = \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\eta) \mathbf {E} f _ {\kappa} (t) \bar {f} _ {\eta} (t) g _ {\kappa} (x) \bar {g} _ {\eta} (x) \\ \qquad = \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\eta) \mathbf {E} f _ {\kappa} (t) f _ {\iota \eta} (t) g _ {\kappa} (x) g _ {\iota \eta} (x) \\ \qquad = \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\iota \eta) F _ {\kappa \eta} (t) g _ {\kappa} (x) g _ {\eta} (x) \\ \qquad \leq \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\iota \eta) F _ {\kappa \eta}. \end{array}
$$

Similarly, we have the bound

$$
\begin{array}{c} \mathbf {E} | F _ {\varepsilon} ^ {\bar {\varepsilon}} (x, t) - F _ {\varepsilon} ^ {\bar {\varepsilon}} (y, t) | ^ {2} = \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\eta) F _ {\kappa \eta} (t) \big (g _ {\kappa} (x) - g _ {\kappa} (y) \big) \big (g _ {\eta} (x) - g _ {\eta} (y) \big) \\ \leq | x - y | ^ {2 \alpha} \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\eta) F _ {\kappa \eta} | G _ {\kappa} | ^ {\alpha} | G _ {\eta} | ^ {\alpha}, \end{array}
$$

as well as

$$
\begin{array}{l} \mathbf {E} | F _ {\varepsilon} ^ {\bar {\varepsilon}} (x, t) - F _ {\varepsilon} ^ {\bar {\varepsilon}} (x, s) | ^ {2} = \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\eta) \hat {F} _ {\kappa \eta} (s, t) g _ {\kappa} (x) g _ {\eta} (x) \\ \qquad \leq | t - s | ^ {2 \beta} \sum_ {\kappa , \eta \in \mathcal {J}} C _ {\varepsilon} ^ {\bar {\varepsilon}} (\kappa) C _ {\varepsilon} ^ {\bar {\varepsilon}} (\eta) | \hat {F} _ {\kappa \eta} |. \end{array}\tag{A.3}
$$

Making use of Lebesgue’s dominated convergence theorem, we deduce that there exists a sequence of constants$K _ { \bar { \varepsilon } }$with$\begin{array} { r } { \operatorname* { l i m } _ { \bar { \varepsilon } \to 0 } K _ { \bar { \varepsilon } } = 0 } \end{array}$such that the bounds

$$
\mathbf {E} | F _ {\varepsilon} ^ {\bar {\varepsilon}} (x, t) - F _ {\varepsilon} ^ {\bar {\varepsilon}} (y, t) | ^ {2} \leq K _ {\bar {\varepsilon}} | x - y | ^ {2 \alpha}, \quad \mathbf {E} | F _ {\varepsilon} ^ {\bar {\varepsilon}} (x, t) - F _ {\varepsilon} ^ {\bar {\varepsilon}} (x, s) | ^ {2} \leq K _ {\bar {\varepsilon}} | t - s | ^ {2 \beta},
$$

hold uniformly for$\varepsilon < \bar { \varepsilon } .$In particular, it follows from Lemma A.1 that bounds with the same homogeneity also hold for the pth moment for arbitrarily large$p .$ It then follows from a straightforward modification of Kolmogorov’s continuity criterion that

$$
\lim _ {\bar {\varepsilon} \to 0} \sup _ {\varepsilon <   \bar {\varepsilon}} \mathbf {E} \| F _ {\varepsilon} ^ {\bar {\varepsilon}} \| _ {\gamma , \delta} ^ {2} = 0  ,
$$

where$\| \cdot \| _ { \gamma , \delta }$is the norm in$B _ { \gamma , \delta }$. The claim now follows at once.

## A.2 Bounds on simple integrals

In this section, we collect a number of elementary bounds on various integrals that appear several times throughout the article. First, it will turn out to be useful to have bounds on expressions of the type

$$
\frac {b f (a t) - a f (b t)}{b - a},
$$

with$a , b ,$t in$\mathbf { R } _ { + }$, where$f \colon \mathbf { R } _ { + }  \mathbf { R }$is a smooth function.

We have the following:

Proposition A.3 For a, b, t, and f as above, one has the global bound

$$
\left| \frac {b f (a t) - a f (b t)}{b - a} - f (0) \right| \leq 2 a b t ^ {2} \| f ^ {\prime \prime} \| _ {\infty},\tag{A.4}
$$

where$\| \cdot \| _ { \infty }$denotes the supremum norm. Iffurthermore there exists a constant K such that$\begin{array} { r } { \operatorname* { s u p } _ { y \geq 0 } | f ( y ) - y f ^ { \prime } ( y ) | \leq K } \end{array}$, then

$$
\left| \frac {b f (a t) - a f (b t)}{b - a} \right| \leq K,\tag{A.5}
$$

independently of a, b, and t.

Proof. We assume without loss of generality that$b > a$(otherwise, just reverse the roles of a and b) and we set$\delta \stackrel { \mathrm { d e f } } { = } b - a$. One then has

$$
\frac {b f (a t) - a f (b t)}{b - a} = f (a t) - \frac {a}{\delta} \bigl (f (b t) - f (a t) \bigr),
$$

so that, writing |I| for the left hand side of (A.4),

$$
\mathcal {I} = a t \left(\frac {1}{a} \int_ {0} ^ {a} f ^ {\prime} (s t) d s - \frac {1}{\delta} \int_ {a} ^ {b} f ^ {\prime} (s t) d s\right).
$$

We now use the identity$\begin{array} { r } { f ^ { \prime } ( s t ) = f ^ { \prime } ( 0 ) + s \int _ { 0 } ^ { t } f ^ { \prime \prime } ( r s ) d r } \end{array}$r and then exchange the order of integrals, so that

$$
\mathcal {I} = a t \int_ {0} ^ {t} \left(\frac {1}{a} \int_ {0} ^ {a} s f ^ {\prime \prime} (r s) d s - \frac {1}{\delta} \int_ {a} ^ {b} s f ^ {\prime \prime} (r s) d s\right) d r.
$$

The first claim now follows by replacing the integrands by their suprema and using the triangle inequality.

To show the bound (A.5), we make use of the identity

$$
{\frac {b f (a t) - a f (b t)}{b - a}} = {\frac {a b}{b - a}} \int_ {a} ^ {b} {\frac {f (x t) - x t f ^ {\prime} (x t)}{x ^ {2}}} d x.
$$

Since$\textstyle \int _ { a } ^ { b } { \frac { d x } { x ^ { 2 } } } = { \frac { b - a } { a b } }$, the second claim then follows from the assumption.

Remark A.4 The constant 2 appearing in (A.4) could actually be improved to$\frac { 3 } { 2 }$.

Another extremely useful calculation is the following:

Lemma A.5 Let$a , b > 0$. Then,for every$t , t ^ { \prime } \in \mathbf { R } ,$, one has

$$
\begin{array}{r l} \int_ {- \infty} ^ {t} \int_ {- \infty} ^ {t ^ {\prime}} e ^ {- a | t - r | - a | t ^ {\prime} - r ^ {\prime} | - b | r - r ^ {\prime} |} d r ^ {\prime} d r & = \frac {a e ^ {- b | t - t ^ {\prime} |} - b e ^ {- a | t - t ^ {\prime} |}}{a (a ^ {2} - b ^ {2})} \\ & \leq \frac {1}{a (a + b)} \wedge \frac {e ^ {- (a \wedge b) | t - t ^ {\prime} |}}{a | a - b |}. \end{array}
$$

Proof. The first identity follows from a lengthy but straightforward calculation. The fact that both$\left| t - r \right|$and$\left| t ^ { \prime } - r ^ { \prime } \right|$have the same prefactor in the exponent is crucial for the result, otherwise, the expression is far lengthier.

To get the bound on the second line, we first use Proposition A.3 to bound the left hand side by$1 / a ( a + b )$(the constant K appearing there is equal to 1 in our case). It then suffices to observe that

$$
\left| a e ^ {- b \left| t - t ^ {\prime} \right|} - b e ^ {- a \left| t - t ^ {\prime} \right|} \right| \leq (a + b) e ^ {- (a \wedge b) \left| t - t ^ {\prime} \right|},
$$

to obtain the second bound.

Another very useful bound is given by

Lemma A.6 For every$s < t$and$u , v > 0$, one has

$$
\int_ {s} ^ {t} e ^ {- u | x - s | - v | x - t |} d x \leq \frac {4 e ^ {- (u \wedge v) t}}{u + v} \leq \frac {4}{u + v}.
$$

Proof. One has the identity

$$
\mathcal {I} \stackrel {\mathrm{def}} {=} \int_ {s} ^ {t} e ^ {- u | x - s | - v | x - t |} d x = e ^ {u s - v t} \int_ {s} ^ {t} e ^ {(v - u) x} d x = \frac {e ^ {- u (t - s)} - e ^ {- v (t - s)}}{v - u}.
$$

Assume now without loss of generality that$v > u$. It then follows from the above that

$$
\mathcal {I} \leq \frac {e ^ {- u (t - s)}}{v - u}.
$$

On the other hand, the integral can be estimated by the supremum of its integrand, times the length of the domain of integration, so that

$$
\mathcal {I} \leq (t - s) e ^ {- u (t - s)} = \frac {u (t - s) e ^ {- u (t - s)}}{u} \leq \frac {e ^ {- \frac {u}{2} (t - s)}}{u},
$$

where we made use of the fact that$x e ^ { - x } \leq e ^ { - x / 2 }$. Combining these bounds, we conclude that

$$
\mathcal {I} \leq \frac {e ^ {- \frac {u \wedge v}{2} (t - s)}}{(u \wedge v) \vee | u - v |}.
$$

The claim now follows from the fact that$( u \wedge v ) \vee | u - v | \geq ( u \vee v ) / 2 \geq ( u + v ) / 4 .$ □

Lemma A.7 Let$F { \colon } \mathbf R  \mathbf R$be such that there exist constants$K > 0$and$b \geq 0$ such that

$$
| F (s) | \leq K e ^ {- b | s |},
$$

and define

$$
\mathcal {K} (t - t ^ {\prime}) \stackrel {d e f} {=} \int_ {- \infty} ^ {t} \int_ {- \infty} ^ {t ^ {\prime}} F (s - s ^ {\prime}) e ^ {- a (t + t ^ {\prime} - s - s ^ {\prime})} d s ^ {\prime} d s.
$$

Then, one has the bound

$$
\left| \mathcal {K} (\delta) - \mathcal {K} (0) \right| \leq (1 \wedge a \delta) \left(\left| \mathcal {K} (0) \right| + \frac {4 K}{(a + b) ^ {2}}\right) \leq 5 K \frac {1 \wedge a \delta}{a (a + b)}.
$$

Proof. By definition, one has

$$
\mathcal {K} (\delta) - \mathcal {K} (0) = (e ^ {- a \delta} - 1) \mathcal {K} (0) + \int_ {0} ^ {\delta} \int_ {- \infty} ^ {0} F (s - s ^ {\prime}) e ^ {- a (\delta - s - s ^ {\prime})} d s ^ {\prime} d s,
$$

so that it suffices to bound the second term in this expression. Since$s > s ^ { \prime }$over the whole domain of integration, F is bounded by$K e ^ { - \bar { b } ( s - s ^ { \prime } ) }$, so that

$$
\left| \int_ {- \infty} ^ {0} F (s - s ^ {\prime}) e ^ {- a (\delta - s - s ^ {\prime})} d s ^ {\prime} \right| \leq \frac {K e ^ {- b s - a (\delta - s)}}{a + b}.
$$

The first bound now follows from Lemma$_ { \mathrm { A . 6 , } }$and the second bound follows from Lemma A.5.□

Proposition A.8 The bound

$$
\begin{array}{r l} & {\int_ {- \infty} ^ {s} \int_ {- \infty} ^ {s ^ {\prime}} \exp (- a | r - r ^ {\prime} | - b | r - s | - c | r ^ {\prime} - s ^ {\prime} | - d | r - s ^ {\prime} | - e | r ^ {\prime} - s |) d r ^ {\prime} d r} \\ & {\qquad \leq \frac {1 0 e ^ {- (d \wedge e) | s - s ^ {\prime} |}}{(b + d) (c + e) + a ((b + d) \wedge (c + e))},} \end{array}
$$

holds for every s,$\mathbf { \boldsymbol { s } } ^ { \prime } \in \mathbf { \mathbb { R } }$and every$a , b , c , d , e > 0 .$

Proof. Throughout, we denote the integrand by$I ( \boldsymbol { r } , \boldsymbol { r } ^ { \prime } )$and we write

$$
\mathcal {R} = \frac {e ^ {- \frac {d \wedge e}{2} | s - s ^ {\prime} |}}{(b + d) (c + e)}.
$$

We can (and will from now on) assume without loss of generality that$s ^ { \prime } > s ,$, since the case$s > s ^ { \prime }$is obtained by making the substitution$( r , s , b , d )  ( r ^ { \prime } , s ^ { \prime } , c , e )$and R is left unchanged by this. We decompose the integral over$r ^ { \prime }$into integrals over $( - \infty , r ] , [ r , s ]$, and$[ s , s ^ { \prime } ]$. The first one then yields

$$
\int_ {- \infty} ^ {r} I (r, r ^ {\prime}) d r ^ {\prime} = \frac {e ^ {- (b + c + e) | r - s | - d | r - s ^ {\prime} |}}{a + c + e},
$$

so that

$$
\int_ {- \infty} ^ {s} \int_ {- \infty} ^ {r} I (r, r ^ {\prime}) d r ^ {\prime} d r = \frac {e ^ {- d | s - s ^ {\prime} |}}{(a + c + e) (b + c + d + e)} \leq \mathcal {R}.
$$

In order to bound the second integral, we use the bound$| r ^ { \prime } - s ^ { \prime } | \leq | r ^ { \prime } - s |$, which allows us to use Lemma A.6. This yields the bound

$$
\int_ {r} ^ {s} I (r, r ^ {\prime}) d r ^ {\prime} \leq \frac {4 e ^ {- b | r - s | - d | r - s ^ {\prime} |}}{a + c + e},
$$

so that

$$
\int_ {- \infty} ^ {s} \int_ {r} ^ {s} I (r, r ^ {\prime}) d r ^ {\prime} \leq \frac {4 e ^ {- d | s - s ^ {\prime} |}}{(a + c + e) (b + d)} \leq 4 \mathcal {R}.
$$

Similarly, we can use Lemma A.6 for the last integral, so that

$$
\int_ {s} ^ {s ^ {\prime}} I (r, r ^ {\prime}) d r ^ {\prime} \leq \frac {4 e ^ {- b | r - s | - d | r - s ^ {\prime} |}}{a + c + e},
$$

yielding in the same way as before$\begin{array} { r } { \int _ { - \infty } ^ { s } \int _ { s } ^ { s ^ { \prime } } I ( r , r ^ { \prime } ) d r ^ { \prime } \leq 4 \mathcal { R } } \end{array}$. The claim now follows at once.□

## A.3 Function spaces

In this appendix, we collect a few useful facts about spaces of distributions with “negative Holder continuity”. Recall that if¨$\alpha , \beta > 0$and we have two functions $u \in \mathcal { C } ^ { \alpha }$and$v \in \mathcal { C } ^ { \beta }$, then the product uv satisfies$u v \in \mathcal { C } ^ { \alpha \wedge \beta }$. We would like to have a similar property for distributions in${ \mathcal { C } } ^ { - \alpha }$for some$\alpha > 0$

In full generality, the above bounds does of course not hold: white noise belongs to${ \mathcal { C } } ^ { - \alpha }$for every$\alpha > \frac { 1 } { 2 }$, but squaring it simply makes no sense whatsoever. However, one has the following:

Proposition A.9 Let$\alpha \in ( 0 , 1 )$and$\beta > \alpha$. Then, the bilinear map$( u , v ) \mapsto u v$ extends to a continuous mapfrom${ \mathcal { C } } ^ { - \alpha } \times { \mathcal { C } } ^ { \beta }$into${ \mathcal { C } } ^ { - \alpha }$

Proof. It suffices to show that, for u and v smooth, one has

$$
\int_ {x} ^ {y} u (z) v (z) d z \leq | x - y | ^ {1 - \alpha} \| u \| _ {- \alpha} \| v \| _ {\beta}.
$$

Writing U for a primitive of$u ,$, we can write

$$
\int_ {x} ^ {y} u (z) v (z) d z = \int_ {x} ^ {y} \delta v (x, z) d U (z) + v (x) \delta U (x, y).
$$

It then follows from Young’s theory of integration [You36] that the first quantity is bounded by$| x - y | ^ { 1 + \beta - \alpha } \| v \| _ { \beta } \| U \| _ { 1 - \alpha }$, provided that$\beta > \alpha$. Since the second quantity is bounded by$| x - y | ^ { 1 - \alpha } \| U \| _ { 1 - \alpha } \| v \| _ { \infty }$, the claim follows at once.□

Remark A.10 The condition$\beta > \alpha$is sharp. Indeed, it is possible to construct a counterexample showing that the multiplication operator cannot be extended to ${ \mathcal { C } } ^ { - { \frac { 1 } { 2 } } } \times { \mathcal { C } } ^ { \frac { 1 } { 2 } }$

Let us also collect the following properties of the heat semigroup:

Proposition A.11 Let$P _ { t }$denote the heat semigroup on$S ^ { 1 }$. Then,for every$\alpha < \beta$ with$\alpha > - 1$and$\beta - \alpha \leq 2 ,$, one has the bounds

$$
\| P _ {t} u \| _ {\beta} \lesssim t ^ {\frac {\alpha - \beta}{2}} \| u \| _ {\alpha}, \| P _ {t} u - u \| _ {\alpha} \lesssim t ^ {\frac {\beta - \alpha}{2}} \| u \| _ {\beta},
$$

where the proportionality constants are uniform over any interval$( 0 , T ]$with$T > 0$

Proof. The statements are standard for positive Holder exponents and follow imme-¨ diately from the scaling properties of the heat kernel. For negative exponents, they then follow from the fact that$P _ { t }$commutes with$\partial _ { x }$□

## References

[ACQ11] G. AMIR, I. CORWIN, and J. QUASTEL. Probability distribution of the free energy of the continuum directed random polymer in 1 + 1 dimensions. Comm. Pure Appl. Math. 64, no. 4, (2011), 466–537.

[All92] G. ALLAIRE. Homogenization and two-scale convergence. SIAM J. Math. Anal. 23, no. 6, (1992), 1482–1518.

[Ass02] S. ASSING. A pregenerator for Burgers equation forced by conservative noise. Comm. Math. Phys. 225, no. 3, (2002), 611–632.

[Ass11] S. ASSING. A rigorous equation for the Cole-Hopf solution of the conservative KPZ dynamics. ArXiv e-prints (2011). arXiv:1109.2886.

[Bal10] G. BAL. Homogenization with large spatial random potential. Multiscale Model. Simul. 8, no. 4, (2010), 1484–1510.

[Bal11] G. BAL. Convergence to homogenized or stochastic partial differential equations. Appl. Math. Res. Express. AMRX , no. 2, (2011), 215–241.

[BG97] L. BERTINI and G. GIACOMIN. Stochastic Burgers and KPZ equations from particle systems. Comm. Math. Phys. 183, no. 3, (1997), 571–607.

[Bog98] V. I. BOGACHEV. Gaussian measures, vol. 62 of Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 1998.

[BQS11] M. BALAZS´ , J. QUASTEL, and T. SEPPAL¨ AINEN¨ . Fluctuation exponent of the KPZ / stochastic Burgers equation. J. Amer. Math. Soc. 24, no. 3, (2011), 683–708.

[CCG00] E. A. CARLEN, M. C. CARVALHO, and E. GABETTA. Central limit theorem for Maxwellian molecules and truncation of the Wild expansion. Comm. Pure Appl. Math. 53, no. 3, (2000), 370–397.

[CF09] M. CARUANA and P. FRIZ. Partial differential equations driven by rough paths. J. Differential Equations 247, no. 1, (2009), 140–173.

[CFO11] M. CARUANA, P. K. FRIZ, and H. OBERHAUSER. A (rough) pathwise approach to a class of non-linear stochastic partial differential equations. Ann. Inst. H. Poincare Anal. Non Lin´ eaire´ 28, no. 1, (2011), 27–46.

[Cha00] T. CHAN. Scaling limits of Wick ordered KPZ equation. Comm. Math. Phys. 209, no. 3, (2000), 671–690.

[CM94] R. A. CARMONA and S. A. MOLCHANOV. Parabolic Anderson problem and intermittency. Mem. Amer. Math. Soc. 108, no. 518, (1994), viii+125.

[Col51] J. D. COLE. On a quasi-linear parabolic equation occurring in aerodynamics. Quart. Appl. Math. 9, (1951), 225–236.

[Cor12] I. CORWIN. The Kardar-Parisi-Zhang equation and universality class. Random Matrices: Theory and Appl. 1, (2012), 1130001.

[CQ10] I. CORWIN and J. QUASTEL. Crossover distributions at the edge of the rarefaction fan. ArXiv e-prints (2010). arXiv:1006.1338. To appear in Annals of Probability.

[DPDT07] G. D P , A. D , and L. T . A modified Kardar-Parisi Zhang model. Electron. Comm. Probab. 12, (2007), 442–453 (electronic).

[DPZ92] G. DA PRATO and J. ZABCZYK. Stochastic Equations in Infinite Dimensions, vol. 44 of Encyclopedia of Mathematics and its Applications. Cambridge University Press, 1992.

[FRW04] F. FLANDOLI, F. RUSSO, and J. WOLF. Some SDEs with distributional drift. II. Lyons-Zheng structure, Ito’s formula and semimartingale characterization.ˆ Random Oper. Stochastic Equations 12, no. 2, (2004), 145–184.

[FV06] P. FRIZ and N. VICTOIR. A note on the notion of geometric rough path. Probab. Theory Related Fields 136, no. 1, (2006), 395–416.

[FV10a] P. FRIZ and N. VICTOIR. Differential equations driven by Gaussian signals. Ann. IHP. (B) Prob. Stat. 46, no. 2, (2010), 369–413.

[FV10b] P. FRIZ and N. VICTOIR. Multidimensional Stochastic Processes as Rough Paths, vol. 120 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2010.

[GJ10] P. GONC¸ ALVES and M. JARA. Universality of KPZ equation. ArXiv e-prints (2010). arXiv:1003.4478.

[GR01] C. GODSIL and G. ROYLE. Algebraic graph theory, vol. 207 of Graduate Texts in Mathematics. Springer-Verlag, New York, 2001.

[GT10] M. GUBINELLI and S. TINDEL. Rough evolution equations. Ann. Probab. 38, no. 1, (2010), 1–75.

[Gub04] M. GUBINELLI. Controlling rough paths. J. Funct. Anal. 216, no. 1, (2004), 86–140.

[Hai11] M. HAIRER. Rough stochastic PDEs. Comm. Pure Appl. Math. 64, no. 11, (2011), 1547–1585.

[Hai12] M. HAIRER. Singular perturbations to semilinear stochastic heat equations. Probab. Theory Related Fields 152, (2012), 265–297.

[HM10] M. HAIRER and J. MAAS. A spatial version of the Ito-Stratonovich correction.ˆ ArXiv e-prints (2010). arXiv:1011.0966. To appear in Annals of Probability.

[HMW12] M. HAIRER, J. MAAS, and H. WEBER. Approximating rough stochastic PDEs. ArXiv e-prints (2012). arXiv:1202.3094.

[Hop50] E. HOPF. The partial differential equation$u _ { t } + u u _ { x } = \mu u _ { x x }$. Comm. Pure Appl. Math. 3, (1950), 201–230.

[HØUZ96] H. HOLDEN, B. ØKSENDAL, J. UBØE, and T. ZHANG. Stochastic partial differential equations. Probability and its Applications. Birkhauser Boston Inc.,¨ Boston, MA, 1996. A modeling, white noise functional approach.

[HP11] M. HAIRER and N. S. PILLAI. Regularity of laws and ergodicity of hypoelliptic SDEs driven by rough paths. ArXiv e-prints (2011). arXiv:1104.5218. To appear in Annals of Probability.

[HW10] M. HAIRER and H. WEBER. Rough Burgers-like equations with multiplicative noise. ArXiv e-prints (2010). arXiv:1012.1236. To appear in Probab. Theory Related Fields.

[IS11]T. IMAMURA and T. SASAMOTO. Replica approach to the KPZ equation with the half Brownian motion initial condition. Journal ofPhysics A: Mathematical and Theoretical 44, no. 38, (2011), 385001.

[Joh00] K. JOHANSSON. Shape fluctuations and random matrices. Comm. Math. Phys. 209, no. 2, (2000), 437–476.

[Kar85] M. KARDAR. Roughening by impurities at finite temperatures. Phys. Rev. Lett. 55, (1985), 2923–2923.

[KPZ86] M. KARDAR, G. PARISI, and Y.-C. ZHANG. Dynamic scaling of growing interfaces. Phys. Rev. Lett. 56, no. 9, (1986), 889–892.

[LBL08] C. LE BRIS and P.-L. LIONS. Existence and uniqueness of solutions to Fokker-Planck type equations with irregular coefficients. Comm. Partial Differential Equations 33, no. 7-9, (2008), 1272–1317.

[LCL07] T. J. LYONS, M. CARUANA, and T. LEVY´ . Differential equations driven by rough paths, vol. 1908 of Lecture Notes in Mathematics. Springer, Berlin, 2007. Lectures from the 34th Summer School on Probability Theory held in Saint-Flour, July 6–24, 2004, With an introduction concerning the Summer School by Jean Picard.

[LQ02] T. LYONS and Z. QIAN. System control and rough paths. Oxford Mathematical Monographs. Oxford University Press, Oxford, 2002. Oxford Science Publications.

[Lyo91] T. LYONS. On the nonexistence of path integrals. Proc. Roy. Soc. London Ser. A 432, no. 1885, (1991), 281–290.

[Lyo98] T. J. LYONS. Differential equations driven by rough signals. Rev. Mat. Iberoamericana 14, no. 2, (1998), 215–310.

[McK67] H. P. MCKEAN, JR. An exponential formula for solving Boltzmann’s equation for a Maxwellian gas. J. Combinatorial Theory 2, (1967), 358–382.

[Ngu89] G. NGUETSENG. A general convergence result for a functional related to the theory of homogenization. SIAM J. Math. Anal. 20, no. 3, (1989), 608–623.

[Nua95] D. NUALART. The Malliavin calculus and related topics. Probability and its Applications (New York). Springer-Verlag, New York, 1995.

[OW11] N. O’CONNELL and J. WARREN. A multi-layer extension of the stochastic heat equation. ArXiv e-prints (2011). arXiv:1104.3509.

[Pol05] M. POLYAK. Feynman diagrams for pedestrians and mathematicians. In Graphs and patterns in mathematics and theoretical physics, vol. 73 of Proc. Sympos. Pure Math., 15–42. Amer. Math. Soc., Providence, RI, 2005.

[PP12]E. P<sup>´</sup> ARDOUX and A. PIATNITSKI. Homogenization of a singular random one-dimensional PDE with time-varying coefficients. Ann. Probab. 40, no. 3, (2012), 1316–1356.

[RT07] F. RUSSO and G. TRUTNAU. Some parabolic PDEs whose drift is an irregular random noise in space. Ann. Probab. 35, no. 6, (2007), 2213–2262.

[SS09] T. SASAMOTO and H. SPOHN. Superdiffusivity of the 1D lattice Kardar-Parisi-Zhang equation. J. Stat. Phys. 137, no. 5-6, (2009), 917–935.

[SS10a] T. SASAMOTO and H. SPOHN. Exact height distributions for the KPZ equation with narrow wedge initial condition. Nuclear Phys. B 834, no. 3, (2010), 523–542.

[SS10b] T. SASAMOTO and H. SPOHN. One-dimensional Kardar-Parisi-Zhang equation: An exact solution and its universality. Phys. Rev. Lett. 104, (2010), 230602.

[Tei11] J. TEICHMANN. Another approach to some rough and stochastic partial differential equations. Stoch. Dyn. 11, no. 2-3, (2011), 535–550.

[TW08a] C. A. TRACY and H. WIDOM. A Fredholm determinant representation in ASEP. J. Stat. Phys. 132, no. 2, (2008), 291–300.

[TW08b] C. A. TRACY and H. WIDOM. Integral formulas for the asymmetric simple exclusion process. Comm. Math. Phys. 279, no. 3, (2008), 815–844.

[TW09] C. A. TRACY and H. WIDOM. Asymptotics in ASEP with step initial condition. Comm. Math. Phys. 290, no. 1, (2009), 129–154.

[Wil51] E. WILD. On Boltzmann’s equation in the kinetic theory of gases. Proc. Cambridge Philos. Soc. 47, (1951), 602–609.

[You36] L. C. YOUNG. An inequality of the Holder type, connected with Stieltjes¨ integration. Acta Math. 67, no. 1, (1936), 251–282.