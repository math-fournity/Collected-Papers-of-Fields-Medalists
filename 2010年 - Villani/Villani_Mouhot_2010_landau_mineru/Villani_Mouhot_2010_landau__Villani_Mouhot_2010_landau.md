# LANDAU DAMPING

## C. MOUHOT AND C. VILLANI

Abstract. In this note we present the main results from the recent work [9], which for the first time establish Landau damping in a nonlinear context.

Keywords. Landau damping; plasma physics; astrophysics; Vlasov–Poisson equation.

## 1. Introduction

The “standard model” of classical plasma physics is the Vlasov–Poisson–Landau equation [13, 6], here written with periodic boundary conditions and in adimensional units:

$$
\frac {\partial f}{\partial t} + v \cdot \nabla_ {x} f + F [ f ] \cdot \nabla_ {v} f = \frac {\log \Lambda}{2 \pi \Lambda} Q _ {L} (f, f),\tag{1}
$$

where$f = f ( t , x , v )$is the electron distribution function$( t \geq 0 , v \in \mathbb { R } ^ { 3 } , x \in \mathbb { T } ^ { 3 } =$ $\mathbb { R } ^ { 3 } / \mathbb { Z } ^ { 3 } )$,

$$
F [ f ] (t, x) = - \iint \nabla W (x - y) f (t, y, w) d w d y\tag{2}
$$

is the self-induced force,$W ( x ) = 1 / | x |$is the Coulomb interaction potential, and$Q _ { L }$ is the Landau collision operator, described for instance in [12]. The parameter Λ is very large, ranging typically from$1 0 ^ { 2 }$to$1 0 ^ { 3 0 }$

On very large time scales (say$O ( \Lambda / \log \Lambda ) )$, dissipative phenomena play a non-negligeable role, and the entropy increase is supposed to force the (slow) convergence to a Maxwellian distribution. Thanks to the recent progress on hypocoercivity, this mechanism is now rather well understood, as soon as global smoothness estimates are available (see [11] and the references therein).

Ten years after devising this collisional scenario, Landau [6] formulated a much more subtle prediction: the stability of homogeneous equilibria satisfying certain conditions — for instance any function of$| v |$, not necessarily Gaussian — on much shorter time scales (say$O ( 1 ) )$, by means of purely conservative mechanisms. This phenomenon, called Landau damping, is a property of the (collisionless) Vlasov equation, obtained by setting$\Lambda = \infty$in (1). This is a theoretical cornerstone of the classical plasma physics (among a large number of references let us mention [1]). Similar damping phenomena also occur in other domains of physics.

The Landau damping has been since long understood at the linearized level [3, 8, 10], but the study of the full (nonlinear) equation poses important conceptual and technical problems. As a consequence, up to now the only existing results were proving existence of some damped solutions with prescribed behavior as$t \to \pm \infty$ [2, 5]. We fill this gap in a recent work [9], whose main result we shall now describe.

## 2. Main result

If f is a function defined on$\mathbb { T } ^ { d } \times \mathbb { R } ^ { d }$, we note, for any$k \in  { \mathbb { Z } ^ { d } }$and$\eta \in \mathbb { R } ^ { d }$, 

$$
\widehat {f} (k, v) = \int_ {\mathbb {T} ^ {d}} f (x, v) e ^ {- 2 i \pi k \cdot x} d x, \quad \widetilde {f} (k, \eta) = \iint_ {\mathbb {T} ^ {d} \times \mathbb {R} ^ {d}} f (x, v) e ^ {- 2 i \pi k \cdot x} e ^ {- 2 i \pi \eta \cdot v} d v d x.
$$

We also set, for$\lambda , \mu , \beta > 0$

$$
\| f \| _ {\lambda , \mu , \beta} = \sup _ {k, \eta} \Bigl (| \widetilde {f} (k, \eta) | e ^ {2 \pi \lambda | \eta |} e ^ {2 \pi \mu | k |} \Bigr) + \iint_ {\mathbb {T} ^ {d} \times \mathbb {R} ^ {d}} | f (x, v) | e ^ {2 \pi \beta | v |} d v d x.\tag{3}
$$

Theorem 1 (nonlinear Landau damping for general interaction). Let d$\geq 1$, and $f ^ { 0 } : \mathbb { R } ^ { d }  \mathbb { R } _ { + }$an analytic velocity profile. Let$W :  { \mathbb { T } } ^ { d } \to  { \mathbb { R } }$be an interaction potential. For any$k \in \mathbb { Z } ^ { d } , \ \xi \in \mathbb { C }$, we set

$$
\mathcal {L} (k, \xi) = - 4 \pi^ {2} \widehat {W} (k) \int_ {0} ^ {\infty} e ^ {2 \pi | k | \xi^ {*} t} | \widetilde {f} ^ {0} (k t) | | k | ^ {2} t d t.
$$

We assume that there is$\lambda > 0$such that, for ǫ small enough,

$$
\sup _ {\eta \in \mathbb {R} ^ {d}} | \widetilde {f} ^ {0} (\eta) | e ^ {2 \pi \lambda | \eta |} \leq C _ {0},\tag{4}
$$

$$
\sum_ {n \in \mathbb {N} ^ {d}} \frac {\lambda^ {n}}{n !} \| \nabla_ {v} ^ {n} f ^ {0} \| _ {L ^ {1} (d v)} \leq C _ {0},\tag{5}
$$

$$
\inf _ {k \in \mathbb {Z} ^ {d}} \inf _ {0 \leq \Re \xi <   \lambda} \left| \mathcal {L} (k, \xi) - 1 \right| \geq \kappa > 0\tag{6}
$$

$$
\exists \gamma \geq 1; \forall k \in \mathbb {Z} ^ {d}; \quad | \widehat {W} (k) | \leq \frac {C _ {W}}{| k | ^ {1 + \gamma}}.
$$

Then as soon as$0 < \lambda ^ { \prime } < \lambda , 0 < \mu ^ { \prime } < \mu , \beta > 0 , r \in \mathbb { N }$, there are$\varepsilon > 0$and$C > 0$, depending on$d , \gamma , \lambda , \lambda ^ { \prime } , \mu , \mu ^ { \prime } , C _ { 0 } , \kappa , C _ { W } , \beta , r ,$such that if$f _ { i } \geq 0$satisfies

$$
\delta := \| f _ {i} - f ^ {0} \| _ {\lambda , \mu , \beta} \leq \varepsilon ,\tag{7}
$$

then the unique solution of the nonlinear Vlasov equation

$$
(8) \frac {\partial f}{\partial t} + v \cdot \nabla_ {x} f + F [ f ] \cdot \nabla_ {v} f = 0, \qquad F [ f ] (t, x) = - \iint \nabla W (x - y) f (t, y, w) d w d y,
$$

defined for all times and such that$f ( 0 , \cdot ) = f _ { i }$, satisfies

$$
\left\| \rho (t, \cdot) - \rho_ {\infty} \right\| _ {C ^ {r} (\mathbb {T} ^ {d})} \leq C   \delta   e ^ {- 2 \pi \lambda^ {\prime} | t |},\tag{9}
$$

where$\begin{array} { r } { \rho ( t , x ) = \int f ( t , x , v ) d v , \rho _ { \infty } = \int \int f _ { i } ( x , v ) } \end{array}$dv dx. Futhermore, there are analytic profiles$f _ { + \infty } ( v ) , f _ { - \infty } ( v )$such that

$$
f (t, \cdot) \xrightarrow {t \to \pm \infty} f _ {\pm \infty} \quad w e a k l y
$$

$$
\int f (t, x, \cdot) d x \xrightarrow {t \to \pm \infty} f _ {\pm \infty} \quad \text {strongly} (i n C ^ {r} (\mathbb {R} _ {v} ^ {d})),
$$

these convergences being also$O ( \delta e ^ { - 2 \pi \lambda ^ { \prime } | t | } )$

This theorem, entirely constructive, is almost optimal, as the following comments show.

Comments on the assumptions: The periodic boundary conditions of course are debatable; in any case, the counterexamples of Glassey and Schaefer [4] show that some confinement mechanism — or at least a limitation on the wavelength — is mandatory. Condition (4) quantitatively expresses the analyticity of the profile$f ^ { 0 }$ without which we could not hope for an exponential convergence. The inequality (5) is a linear stability condition, roughly optimal, covering all physically interesting cases: in particular the (attractive) Newton interaction for wavelengths shorter than the Jeans unstability length; and the (repulsive) Coulomb interaction around radially symmetric profiles${ \bf { \bar { f } } } ^ { 0 }$, for all wavelengths. On the other hand, condition (6) shows up only in the nonlinear stability; it is satisfied by Coulomb and Newton interactions as a limit case. As for the condition (7), its perturbative nature is natural in view of theoretical speculations and numerical studies in the subject.

## Comments on the conclusions:

(1) The large-time convergence is based on a reversible, purely deterministic mechanism, without any Lyapunov functional neither variational interpretation. The asymptotic profiles$f _ { \pm \infty }$eventually keep the memory of the initial datum and the interaction. This convergence “for no reason” was not really expected, since the quasilinear theory of Landau damping [1, Vol. II, Section 9.1.2] predicts convergence only after taking average on statistical ensembles.

(2) This result can be interpreted in the spirit of the KAM theorem: for the linear Vlasov equation, convergence is forced by an infinity of invariant subspaces, which make the model “completely integrable”; as soon as one adds a nonlinear coupling, the invariance goes away but the convergence remains.

(3) Given a stable equilibrium profile$f ^ { 0 }$, we see that an entire neighborhood — in analytic topology — of$f ^ { 0 }$is filled by homoclinic or (in general) heteroclinic trajectories. Only infinite dimension allows this remarkable behavior of the nonlinear Vlasov equation.

(4) The large time convergence of the distribution function holds only in the weak sense; the norms of velocity derivatives grow quickly in large time, which reflects a filamentation in phase space, and a transfer of energy (or information) from low to high frequencies (“weak turbulence”).

(5) It is this transfer of information to small scales which allows to reconcile the reversibility of the Vlasov–Poisson equation with the seemingly irreversible large-time behavior. Let us note that the “dual” mechanism of transfer of energy to large scales, also called radiation, was extensively studied in the setting of Hamiltonian systems.

Much more comments, both from the mathematical and the physical sides, can be found in [9].

## 3. Linear stability

The linear stability is the first step of our study; it only requires a reduced technical investment.

After linearization around a homogeneous equilibrium$f ^ { 0 }$, the Vlasov equation becomes

$$
\frac {\partial h}{\partial t} + v \cdot \nabla_ {x} h - (\nabla W * \rho) \cdot \nabla_ {v} f ^ {0} = 0, \quad \rho = \int h d v.\tag{10}
$$

It is well-known that this equation decouples into an infinite number of independent equations governing the modes of$\rho \colon$for all$k \in  { \mathbb { Z } ^ { d } }$and$t \geq 0$,

$$
\widehat {\rho} (t, k) - \int_ {0} ^ {t} K ^ {0} (t - \tau , k) \widehat {\rho} (\tau , k) d \tau = \widetilde {h} _ {i} (k, k t),\tag{11}
$$

where$h _ { i }$is the initial datum, and$K ^ { 0 }$an integral kernel depending on$f ^ { 0 }$:

$$
K ^ {0} (t, k) = - 4 \pi^ {2} \widehat {W} (k) \widetilde {f} ^ {0} (k t) | k | ^ {2} t.\tag{12}
$$

Then from classical results on Volterra equations we deduce that for all$k \neq 0$the decay of${ \widehat { \rho } } ( t , k )$as$t \to \infty$is essentially controlled by the worst of two convergence rates:

• the convergence rate of the source term in the right-hand side of (11), which depends only on the regularity of the initial datum in the velocity variable;

$\bullet e ^ { - \lambda t }$, where λ is the largest positive real number such that the Fourier–Laplace transform (in the t variable) of$K ^ { 0 }$does not approach the value 1 in the strip $\{ 0 \leq \Re z \leq \lambda \} \subset \mathbb { C }$. The problem lies in finding suficient conditions on$f ^ { 0 }$to guarantee the strict positivity of λ.

Since Landau, this study is traditionally performed thanks to the Laplace transform inversion formula; however, with a view to the nonlinear study, we prefer a more elementary and constructive approach, based on the plain Fourier inversion formula.

With this method we establish the linear Landau damping, under conditions (5) and (4), for any interaction W such that$\nabla W \in L ^ { 1 } (  { \mathbb { T } } ^ { d } )$, and any analytical initial condition (without any size restriction in this linear context). We recover as particular cases all the results previously established on the linear Landau damping [3, 8, 10]; but we also cover for instance Newton interaction. Indeed, condition (5) is satisfied as soon as any one of the following conditions is satisfied:

(a)$\forall k \in \mathbb { Z } ^ { d } , \forall z \in \mathbb { R } , \widehat { W } ( k ) \geq 0 , z \phi _ { k } ^ { \prime } ( z ) \leq 0 .$, where$\phi _ { k }$is the “marginal” of$f ^ { 0 }$ along the direction k, defined by

$$
\phi_ {k} (z) = \int_ {\frac {k z}{| k |} + k ^ {\perp}} f ^ {0} (w) d w;
$$

$$
\text {(b)} 4 \pi^ {2} \left(\max _ {k \neq 0} | \widehat {W} (k) |\right) \left(\sup _ {| \sigma | = 1} \int_ {0} ^ {\infty} | \widetilde {f} ^ {0} (r \sigma) | r d r\right) <   1.
$$

We refer to [9, Section 3] for more details.

## 4. Nonlinear stability

To establish the nonlinear stability, we start by introducing analytic norms which are “hybrid” (based on the size of derivatives in the velocity variable, and on the size of Fourier coeficients in the position variable) and “gliding” (the norm will change with time to take into account the transfer to small velocity scales). Five indices

provide all the necessary flexibility:

$$
\left\| f \right\| _ {\mathcal {Z} _ {\tau} ^ {\lambda_ {1} (\mu , \gamma); p}} = \sum_ {k \in \mathbb {Z} ^ {d}} \sum_ {n \in \mathbb {N} ^ {d}} e ^ {2 \pi \mu | k |} (1 + | k |) ^ {\gamma} \frac {\lambda^ {n}}{n !} \left\| \left(\nabla_ {v} + 2 i \pi \tau k\right) ^ {n} \widehat {f} (k, v) \right\| _ {L ^ {p} (d v)}.\tag{13}
$$

(By default$\gamma = 0 . )$A tedious injection theorem“à la Sobolev” compares these norms to more traditional ones, such as the$\| f \| _ { \lambda , \mu , \beta }$norms appearing in (3).

The$\mathcal { Z }$norms enjoy remarkable properties with respect to composition and product. The parameter$\tau$partly compensates for filamentation. Finally, the hybrid nature of these norms is well adapted to the geometry of the problem. If$f$depends only on$x ,$, the norm (13) coincides with the norm$\mathcal { F } ^ { \lambda \tau + \mu , \gamma }$defined by

$$
\| f \| _ {\mathcal {F} ^ {\lambda \tau + \mu , \gamma}} = \sum_ {k \in \mathbb {Z} ^ {d}} | \widehat {f} (k) | e ^ {2 \pi (\lambda \tau + \mu) | k |} (1 + | k |) ^ {\gamma}.\tag{14}
$$

(We also use the “homogeneous” version$\dot { \mathcal { F } } ^ { \lambda \tau + \mu , \gamma }$where the mode$k = 0$is removed.)

Then the Vlasov equation is solved by a Newton scheme, whose first step is the solution of the linearized equation around$f ^ { 0 }$:

$$
f ^ {n} = f ^ {0} + h ^ {1} + \ldots + h ^ {n},\tag{15}
$$

$$
\left\{ \begin{array}{l} \partial_ {t} h ^ {1} + v \cdot \nabla_ {x} h ^ {1} + F [ h ^ {1} ] \cdot \nabla_ {v} f ^ {0} = 0 \\ h ^ {1} (0, \cdot) = f _ {i} - f ^ {0} \end{array} \right.\tag{16}
$$

$$
n \geq 1, \quad \left\{ \begin{array}{l} \partial_ {t} h ^ {n + 1} + v \cdot \nabla_ {x} h ^ {n + 1} + F [ f ^ {n} ] \cdot \nabla_ {v} h ^ {n + 1} + F [ h ^ {n + 1} ] \cdot \nabla_ {v} f ^ {n} = - F [ h ^ {n} ] \cdot \nabla_ {v} h ^ {n} \\ h ^ {n + 1} (0, \cdot) = 0. \end{array} \right.
$$

In a first step, we establish the short-time analytic regularity of$h ^ { n } ( \tau , \cdot )$in the norm$\mathcal { Z } _ { \tau } ^ { \lambda , ( \mu , \gamma ) ; 1 }$; this step, in the spirit of a Cauchy–Kowalevskaya theorem, is performed thanks to the identity

$$
\left. \frac {d}{d t} ^ {+} \right| _ {t = \tau} \| f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda (t), \mu (t); p}} \leq - \frac {K}{1 + \tau} \| \nabla f \| _ {\mathcal {Z} _ {\tau} ^ {\lambda (\tau), \mu (\tau); p}},\tag{17}
$$

where$\lambda ( t ) = \lambda - K t , \mu ( t ) = \mu - K t .$

In a second step, we establish uniform in time estimates on each$h ^ { n }$, now with a partly Eulerian and partly Lagrangian method, integrating the equation along the characteristics$( X _ { \tau , t } ^ { n } , V _ { \tau , t } ^ { n } )$created by the force$F [ f ^ { n } ]$. (Here$\tau$is the initial time, t the current time,$( x , v )$the initial conditions,$( X ^ { n } , V ^ { n } )$the current conditions.) The smoothness of these characteristics is expressed by controls in hybrid norm on the operators$\Omega _ { t , \tau } ^ { n } ( x , v ) = ( X _ { t , \tau } ^ { n } , V _ { t , \tau } ^ { n } ) ( x + v ( t - \tau ) , v )$, which compare the perturbed dynamics to the unperturbed one; these are informally called scattering operators.

Then we propagate a number of estimates along the scheme; the most important are (slightly simplifying)

(18)

$$
\sup _ {\tau \geq 0} \left\| \int_ {\mathbb {R} ^ {d}} h ^ {n} (\tau , \cdot , v) d v \right\| _ {\mathcal {F} ^ {\lambda_ {n} \tau + \mu_ {n}}} \leq \delta_ {n},\tag{19}
$$

$$
\sup _ {t \geq \tau \geq 0} \left\| h ^ {n} \big (\tau , \Omega_ {t, \tau} ^ {n} \big) \right\| _ {\mathcal {Z} _ {\tau - \frac {b t}{1 + b}} ^ {\lambda_ {n} (1 + b), \mu_ {n}; 1}} \leq \delta_ {n}, \qquad b = b (t) = \frac {B}{1 + t},\tag{20}
$$

$$
\left\| \Omega_ {t, \tau} ^ {n} - \operatorname{Id} \right\| _ {\mathcal {Z} _ {\tau - \frac {b t}{1 + b}} ^ {\lambda_ {n} (1 + b), (\mu_ {n}, \gamma); \infty}} \leq C \left(\sum_ {k = 1} ^ {n} \frac {\delta_ {k} e ^ {- 2 \pi (\lambda_ {k} - \lambda_ {n + 1}) \tau}}{2 \pi (\lambda_ {k} - \lambda_ {n + 1}) ^ {2}}\right) \min \{t - \tau ; 1 \}.
$$

Notice, in (18), the linear increase in the regularity of the spatial density, which comes at the same time as the deterioration of regularity in the v variable. In (19), the additional time-shift in the indices by the function$b ( t )$will be crucial to absorb error terms coming from the composition; the constant B itself is determined by the previous small-time estimates. Finally, in (20), notice the uniform in t control, and the improved estimates in the limit cases$t \longrightarrow \tau$and$\tau \longrightarrow \infty ;$; also this is important for handling error terms. The constants$\lambda _ { n }$and$\mu _ { n }$decrease at each stage of the scheme, converging — not too fast — to positive limits$\lambda _ { \infty } , \mu _ { \infty } ;$; at the same time, the constants$\delta _ { n }$converge extremely fast to 0, which guarantees “by retroaction” the uniformity of the constants in the right-hand side of (20).

The estimates (20) are obtained by repeated application of fixed point theorems in analytic norms. Another crucial ingredient to go from stage n to stage$n + 1$is the mechanism of regularity extortion, which we shall now describe in a simplified version. Given two distribution functions$f$and${ \overline { { f } } } .$, depending on$t , x , v$, let us define

$$
\sigma (t, x) = \int_ {0} ^ {t} \int_ {\mathbb {R} ^ {d}} \left(F [ f ] \cdot \nabla_ {v} \overline {{f}}\right) (\tau , x - v (t - \tau), v) d v d \tau .
$$

This quantity can be interpreted as follows: if particles distributed according to $f$exert a force on particles distributed according to${ \overline { { f } } } .$, then$\sigma$is the variation of density$\int f d v$caused by the reaction of$\overline { { f } }$on$f .$We show that if$\overline { { f } }$has a high gliding regularity, then the regularity of$\sigma$in large time is better than what would be expected:

$$
\left\| \sigma (t, \cdot) \right\| _ {\dot {\mathcal {F}} ^ {\lambda t + \mu}} \leq \int_ {0} ^ {t} K (t, \tau) \left\| F [ f (\tau , \cdot) ] \right\| _ {\mathcal {F} ^ {\lambda \tau + \mu , \gamma}} d \tau ,\tag{21}
$$

where

$$
K (t, \tau) = \left[ \sup _ {0 \leq s \leq t} \left(\frac {\left\| \nabla_ {v} \overline {{f}} (s , \cdot) \right\| _ {\mathcal {Z} _ {s} ^ {\overline {{\lambda}} , \overline {{\mu}} ; 1}}}{1 + s}\right) \right] (1 + \tau) \sup _ {k \neq 0, \ell \neq 0} \frac {e ^ {- 2 \pi (\overline {{\lambda}} - \lambda) | k (t - \tau) + \ell \tau |} e ^ {- 2 \pi (\overline {{\mu}} - \mu) | \ell |}}{1 + | k - \ell | ^ {\gamma}}.
$$

The kernel$K ( t , \tau )$has integral$O ( t )$as$t \to \infty$, which would let us fear a violent unstability; but it is also more and more concentrated on discrete times$\tau = k t / ( k -$ $\ell ) { }$; this is the efect of plasma echoes, discovered and experimentally observed in the sixties [7]. The stabilizing role of the echo phenomenon, related to the Landau damping, is uncovered in our study.

Then we analyze the nonlinear response due to echoes. If$\gamma > 1$, from (21) one deduces that the response is subexponential, and therefore can be controlled by an arbitrarily small loss of gliding regularity, at the price of a gigantic constant, which later will be absorbed by the ultrafast convergence of the Newton scheme. In the end, part of the gliding regularity of$\overline { { f } }$has been converted into a large-time decay.

When$\gamma = 1$, a finer strategy is needed. To handle this case, we work on the response mode by mode, that is, estimating the size of${ \widehat { \rho } } ( t , k )$for all$k ,$via an infinite system of inequalities. Then we are able to take advantage of the fact that echoes occurring at diferent frequencies are asymptotically rather well separated. For instance, in dimension 1, the dominant echo occurring at time t and frequency $k$corresponds to$\tau = k t / ( k + 1 )$

In practice, straight trajectories in (21) must be replaced by characteristics (this reflects the fact that$\overline { { f } }$also exerts a force on$f )$, which is a source of considerable technical dificulties. Among the tools used to overcome them, let us mention a second mechanism of regularity extortion, acting in short time and close in spirit to velocity-averaging lemmas; here is a simplified version of it:

$$
\left\| \sigma (t, \cdot) \right\| _ {\dot {\mathcal {F}} ^ {\lambda t + \mu}} \leq \int_ {0} ^ {t} \left\| F [ f (\tau , \cdot) ] \right\| _ {\mathcal {F} ^ {\lambda [ \tau - b (t - \tau) ] + \mu , \gamma}} \left\| \nabla f (\tau , \cdot) \right\| _ {\mathcal {Z} _ {\tau - b t / (1 + b)} ^ {\lambda (1 + b), (\mu , 0); 1}} d \tau .\tag{22}
$$

We see in (22) that the regularity of$\sigma$is better than that of$F [ f ]$, with a gain that degenerates as$t \to \infty \ \mathrm { o r } \ \tau \to t$

## References

[1] Akhiezer, A., Akhiezer, I., Polovin, R., Sitenko, A., and Stepanov, K. Plasma electrodynamics. Vol. I: Linear theory, Vol. II: Non-linear theory and fluctuations. Pergamon Press, 1975 (Enlglish Edition). Translated by D. ter Haar.

[2] Caglioti, E., and Maffei, C. Time asymptotics for solutions of Vlasov–Poisson equation in a circle. J. Statist. Phys. 92, 1-2 (1998), 301–323.

[3] Degond, P. Spectral theory of the linearized Vlasov–Poisson equation. Trans. Amer. Math. Soc. 294, 2 (1986), 435–453.

[4] Glassey, R., and Schaeffer, J. On time decay rates in Landau damping. Comm. Partial Diferential Equations 20, 3-4 (1995), 647–676.

[5] Hwang, J.-H., and Velazquez, J. On the existence of exponentially decreasing solutions of the nonlinear landau damping problem. Preprint, 2008.

[6] Landau, L. On the vibration of the electronic plasma. J. Phys. USSR 10 (1946), 25. English translation in JETP 16, 574. Reproduced in Collected papers of L.D. Landau, edited and with an introduction by D. ter Haar, Pergamon Press, 1965, pp. 445–460; and in Men of Physics: L.D. Landau, Vol. 2, Pergamon Press, D. ter Haar, ed. (1965).

[7] Malmberg, J., Wharton, C., Gould, R., and O’Neil, T. Plasma wave echo experiment. Phys. Rev. Letters 20, 3 (1968), 95–97.

[8] Maslov, V. P., and Fedoryuk, M. V. The linear theory of Landau damping. Mat. Sb. (N.S.) 127(169), 4 (1985), 445–475, 559.

[9] Mouhot, C., and Villani, C. On the landau damping. Available online at http://arxiv.org/abs/0904.2760. Preprint, 2009.

[10] Saenz, A. W. Long-time behavior of the electic potential and stability in the linearized Vlasov theory. J. Mathematical Phys. 6 (1965), 859–875.

[11] Villani, C. Hypocoercivity. To appear in Mem. Amer. Math. Soc.

[12] Villani, C. A review of mathematical topics in collisional kinetic theory. In Handbook of mathematical fluid dynamics, Vol. I. North-Holland, Amsterdam, 2002, pp. 71–305.

[13] Vlasov, A. A. On the oscillation properties of an electron gas. Zh. Eksper. Teoret. Fiz. 8 (1938), 291–318.

Clément Mouhot

University of Cambridge DAMTP, Centre for Mathematical Sciences Wilberforce Road Cambridge CB3 0WA ENGLAND On leave from: ENS Paris & CNRS DMA, UMR CNRS 8553 45 rue d’Ulm F 75320 Paris cedex 05 FRANCE

e-mail: Clement.Mouhot@ens.fr

Cédric Villani

ENS Lyon & Institut Universitaire de France UMPA, UMR CNRS 5669 46 allée d’Italie 69364 Lyon Cedex 07 FRANCE

e-mail: cvillani@umpa.ens-lyon.fr