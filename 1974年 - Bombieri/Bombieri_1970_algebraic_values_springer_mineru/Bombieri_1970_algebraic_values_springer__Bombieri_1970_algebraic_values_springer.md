# Algebraic Values of Meromorphic Maps

ENRICO BOMBIERI (Pisa)

## I. Introduction

In this paper we shall prove the following result.

Theorem A. Let $K$ be a number field and let $f = (f_1, \ldots, f_N)$ be meromorphic functions in $\mathbf{C}^d$, of finite order. Assume that

(i) $\operatorname{tr} \deg K(f) \geq d + 1$;

(ii) the partial derivatives $\partial/\partial z_{\alpha}, \alpha=1,\ldots,d$ map the ring $K[f]$ into itself.

Then the set $S$ of points $\zeta\in\mathbf{C}^{d}$ where $f(\zeta)$ is defined and $f(\zeta)\in K^{N}$, is contained in an algebraic hypersurface.

Remark 1. We shall prove a bit more than Theorem A. If the meromorphic functions $f_{j}$ are of order $\leq \rho$, then we get the bound

$$
d (d + 1) \rho [ K: \mathbf {Q} ] + 2 d
$$

for the degree of the hypersurface containing S (we can replace 2d by d, but we shall not prove this here).

Remark 2. Condition (ii) in Theorem A can be relaxed so to include the more general case in which $\partial/\partial z_{\alpha}$ maps $K(f)$ into itself.

For assuming that

$$
\frac {\partial f _ {i}}{\partial z _ {\alpha}} = P _ {i \alpha} (f) Q (f) ^ {- 1}
$$

where $P_{i\alpha}(T), Q(T) \in K[T]$ we define $f_{N+1} = Q(f)^{-1}$ and consider $\tilde{f} = (f_1, \ldots, f_{N+1})$. It is easy to check that

$$
\frac {\partial f _ {i}}{\partial z _ {\alpha}} \in K [ \tilde {f} ] \quad \text { for } i = 1, \dots , N + 1
$$

and the result of Theorem A still applies, but with the additional condition that $Q(f(\zeta)) \neq 0$.

Results in this range of ideas are not new. Theorem A was proved in case d=1 by Lang [5], after previous work by Schneider [10]; in this case the set S is a finite set of cardinality  $\leq20\rho[K:Q]$ . In the higher 19 Inventiones math., Vol. 10

dimensional case, Lang [5] showed that if S contains a subset of the type  $S_{1} \times \cdots \times S_{d}$  then min card  $S_{\alpha} \leq b \rho [K:Q]$ ; this result may be regarded as a special case of Theorem A, Remark 1. The condition for S to contain a product was clearly artificial and in the historical note in [5], Chapter IV, Lang remarks: “In extending Theorems 1, 2, 3, one has the following possibilities. First, a suggestion of Nagata, that the set S in Theorem 1 may be described as contained in a hypersurface (algebraic). This would be a good way of eliminating the unnatural condition that S be a product. (One would also need to bound the degree of the hypersurface.)” This is exactly what we do in our Theorem A.

While the previous techniques used methods in one complex variable, using the cartesian product structure of  $C^{d}$  (hence the condition  $S = S_{1} \times \cdots \times S_{d}$  in Lang's result), we work directly in  $C^{d}$  and we borrow powerful tools from the theory of holomorphic functions of several complex variables. In particular, we use Lelong's theory of plurisubharmonic functions and positive currents, together with Carleman's estimates and existence theorems for the  $\bar{\partial}$  operator in  $C^{d}$ , as given in Andreotti and Vesentini [1] and in the book [4] by Hörmander. In our context, only the elementary theory of [4] is needed.

It is a pleasure to thank here Serge Lang for several enlightening discussions on this subject, and Norberto Kerzman of New York University for useful conversations on the theory of functions of several complex variables.

## II. Positive (1, 1)-Currents in $\mathbf{C}^n$

We shall review here some fundamental properties of positive  $(1,1)$ -currents in  $C^{n}$ ; actually, the results of this section can be generalized to  $(p,p)$ -currents without much difficulty.

Our notation is as follows. $\mathcal{D}(\Omega)$ denotes the space of $C^\infty$ differential forms of type $(n - 1, n - 1)$ with compact support in $\Omega$; also given

$$
\phi = \sum \phi^ {\alpha \bar {\beta}} (d z _ {1} \wedge d \bar {z} _ {1} \wedge \dots \wedge d z _ {n} \wedge d \bar {z} _ {n}) _ {\alpha , \bar {\beta}} ^ {\hat {}}
$$

where the symbol $\hat{\alpha},\bar{\beta}$ means that the differentials $dz_{\alpha},d\overline{z}_{\beta}$ are omitted, one defines the comass $\| \phi \|$ of $\phi$ at a point $z$ by

$$
\| \phi \| = 2 ^ {n - 1} \sup _ {\alpha , u} \left| \sum_ {p q} u _ {\alpha p} \bar {u} _ {\alpha q} \phi^ {p \bar {q}} \right|
$$

where the sup is taken over $\alpha=1,2,\ldots,n$ and $u=(u_{\alpha p})$ with $u\in SU(n)$. It is easily seen that the comass $\|\ \|$ is equivalent to $|\phi|=\sup_{p,q}|\phi^{p\bar{q}}|$; however the comass has the advantage of being invariant by unitary transformations and leads to a much nicer dual norm in the space of currents.

If $\phi \in \mathcal{D}(\Omega)$ we define

$$
\| \phi \| _ {\Omega} = \sup _ {\Omega} \| \phi \|;
$$

this norm is equivalent to the sup norm of the coefficients of  $\phi$ .

Let

$$
T = \sum t _ {\alpha \bar {\beta}} d z _ {\alpha} \wedge d \bar {z} _ {\beta}
$$

be a (1, 1)-current. Given a non-negative continuous function $f(z)$ with compact support in $\mathbf{C}^n$, one defines

$$
\| T \| (f) = \sup _ {\phi} | T (\phi) |
$$

where the sup is taken over all $\phi$ satisfying $\| \phi \| \leq f$ everywhere. If $\| T\| (f) < + \infty$ for each $f$ then $\| T\|$ is extended by linearity to a positive distribution in $\mathbf{C}^n$ which we can identify to a Radon measure, again denoted by $d\| T\|$.

Let $\omega$ be the differential form

$$
\omega = \frac {i}{2} \sum d z _ {\alpha} \wedge d \bar {z} _ {\alpha}
$$

and define

$$
\omega_ {k} = \frac {1}{k !} \omega^ {k}, \quad k = 1, 2, \dots , n;
$$

note that

$$
\| \omega_ {n - 1} \| = 1 \quad \text {   at   every   point   of   } \mathbf {C} ^ {n}.
$$

Let $T$ be a (1, 1)-current and assume that the distribution

$$
\left(\sum t _ {\alpha \bar {\beta}} w _ {\alpha} \overline {{{w}}} _ {\beta}\right) \wedge \omega_ {n}
$$

defines a positive measure for every $w \in \mathbf{C}^n$; then we shall say that the current $T$ is positive. In particular this implies that $T$ is hermitian so that $t_{\alpha \bar{\beta}} = \bar{t}_{\beta \bar{\alpha}}$.

Proposition 1. If $T$ is a positive (1, 1)-current we have

$$
d \| T \| = i T \wedge \omega_ {n - 1} = 2 \left(\sum t _ {\alpha \bar {\alpha}}\right) \wedge \omega_ {n}.
$$

Proof. This follows from the fact that  $\omega_{n}$  is  $SU(n)$ -invariant and  $\|\omega_{n-1}\|=1$  everywhere; see for example [2], p.652.

If $T$ is positive then $d \| T \|$ is a positive Radon measure in $\mathbf{C}^n$. If $\Omega$ is an open set in $\mathbf{C}^n$, then we define

$$
\| T \| \Omega = \int_ {\Omega} d \| T \|;
$$

$\| T\| \Omega$ is also called the mass of the current $T$ over $\Omega$. Let $B(r,a)$ denote the ball $|z - a| < r$ in $\mathbf{C}^n$; the average mass $\Theta (\| T\| ;r,a)$ of $T$ in $B(r,a)$ is by definition the quantity

$$
\Theta (\| T \|; r, a) = \frac {(n - 1) !}{\pi^ {n - 1} r ^ {2 n - 2}} \| T \| B (r, a).
$$

The density of $T$ at the point $a$ is given by

$$
\Theta (\| T \|; a) = \lim _ {r \rightarrow 0} \Theta (\| T \|; r, a)
$$

provided the limit exists; more generally, one may define the upper and lower densities  $\Theta^{*}$ ,  $\Theta_{*}$  by considering the upper and the lower limit as  $r \to 0$ .

A current $T$ is $\overline{\partial}$-closed if $\overline{\partial} T = 0$; here $\overline{\partial} T$ is defined by

$$
\bar {\partial} T (\phi) = - T (\bar {\partial} \phi)
$$

for $\phi$ a $C^\infty$ differential form with compact support. If $\Omega$ is an open subset of $\mathbf{C}^n$ we say that $T$ is $\overline{\partial}$-closed in $\Omega$ if

$$
\overline {{{{\partial}}}} T (\phi) = 0
$$

for $\phi$ a $C^\infty$ differential form with compact support in $\Omega$.

Proposition 2. Let $T$ be a $\overline{\partial}$-closed positive (1, 1)-current.

Then $\Theta(\|T\|; r, a)$ is monotone non-decreasing in $r$. In particular, the density $\Theta(\|T\|; a)$ exists and is finite for every $a \in \mathbf{C}^n$.

Proof. (See [8], p. 73 and [2], pp. 621 and 652.)

The differential form $\frac{1}{2\pi} \partial \overline{\partial} \log |z|$ in $\mathbf{C}^n - \{0\}$ has a positive definite Levi form; hence the current

$$
i T \wedge \left(\frac {i}{2 \pi} \partial \bar {\partial} \log | z |\right) ^ {n - 1}
$$

is a positive measure in $\mathbf{C}^n -\{0\}$. It follows that Proposition 2 will be proved if we show that

$$
\int_ {B (R, a) \setminus B (r, a)} i T \wedge \left(\frac {i}{2 \pi} \partial \overline {{\partial}} \log | z |\right) ^ {n - 1} = \Theta (\| T \|; R, a) - \Theta (\| T \|; r, a)
$$

for $0 < r < R < +\infty$, because the integral is non-negative.

We have  $\bar{\partial}T=0$ , hence there exists a  $(1,0)$ -current S such that

$$
i T = \bar {\partial} S;
$$

we may consider $S$ defined by

$$
S (\bar {\partial} \phi) = - i T (\phi),
$$

which is a consistent definition because T is  $\bar{\partial}$ -closed. Now

$$
\bar {\partial} S \wedge \left(\frac {i}{2 \pi} \partial \bar {\partial} \log | z |\right) ^ {n - 1} = \bar {\partial} \left[ S \wedge \left(\frac {i}{2 \pi} \partial \bar {\partial} \log | z |\right) ^ {n - 1} \right]
$$

hence by Stokes' theorem we get

$$
\begin{array}{l} \int_ {B (R, a) \setminus B (r, a)} i T \wedge \left(\frac {i}{2 \pi} \partial \bar {\partial} \log | z |\right) ^ {n - 1} \\ = \int_ {\partial B (R, a)} S \wedge \left(\frac {i}{2 \pi} \partial \bar {\partial} \log | z |\right) ^ {n - 1} - \int_ {\partial B (r, a)} S \wedge \left(\frac {i}{2 \pi} \partial \bar {\partial} \log | z |\right) ^ {n - 1}. \end{array}
$$

On $\partial B(r, a)$ we have $|z| = r = \text{const}$ and one computes easily

$$
\left(\frac {i}{2 \pi} \partial \bar {\partial} \log | z |\right) ^ {n - 1} = \frac {(n - 1) !}{\pi^ {n - 1} r ^ {2 n - 2}} \omega_ {n - 1} \quad \text { on } \quad \partial B (r, a).
$$

It follows that

$$
\begin{array}{r l} \int_ {\partial B (r, a)} S \wedge \left(\frac {i}{2 \pi} \partial \overline {{\partial}} \log | z |\right) ^ {n - 1} & = \frac {(n - 1) !}{\pi^ {n - 1} r ^ {2 n - 2}} \int_ {\partial B (r, a)} S \wedge \omega_ {n - 1} \\ & = \int_ {B (r, a)} i T \wedge \omega_ {n - 1} \\ & = \int_ {B (r, a)} d \| T \| \end{array}
$$

because $\overline{\partial}\omega = 0$ hence $\overline{\partial}(iT\wedge \omega_{n - 1}) = S\wedge \omega_{n - 1}$, and because of Proposition 1.

## III. Majorization of Holomorphic Functions

We recall that a real valued function V in  $C^{n}$  is plurisubharmonic if it is locally summable, upper semicontinuous and if its restriction to every complex line in  $C^{n}$  is subharmonic for the Laplace operator. This last condition means simply that

$$
T = \partial \overline {{\partial}} V
$$

is a positive current in $\mathbf{C}^n$.

A very important class of plurisubharmonic functions is obtained as follows. Let F be a holomorphic function in  $C^{n}$ ; then

$$
T = \partial \bar {\partial} V = \frac {1}{\pi} \partial \bar {\partial} \log | F |
$$

is a positive (1, 1)-current and

$$
V = \frac {1}{\pi} \log | F |
$$

is plurisubharmonic. The current i T is represented explicitly by

$$
i T (\phi) = \int_ {W} \phi
$$

where W is the divisor in  $C^{n}$  defined by the equation

$$
F (z) = 0;
$$

see for instance [8], p.72.

In particular, we have

$$
\operatorname{supp} (T) = W.
$$

The associated Radon measure  $d \parallel T \parallel$  is the volume measure on W; hence

$$
\begin{array}{r l} \| T \| (f) & = \int_ {\mathbf {C} ^ {n}} f d \| T \| \\ & = \int_ {W} f d \sigma \end{array}
$$

where  $d\sigma$  is the volume element on W. Note also that the current T is determined by the divisor W associated to F.

Proposition 2 of Section II shows that the density $\Theta(\|T\|; a)$ is everywhere defined because $T = \partial \overline{\partial} V$ is clearly $\overline{\partial}$-closed. We have the following additional properties of the function $\Theta(\|T\|; r, a)$.

Proposition 3. Let $F$ be holomorphic in $\mathbf{C}^{n}$ and let $T$ be the positive, $\bar{\partial}$-closed, (1, 1)-current

$$
T = \frac {1}{\pi} \partial \bar {\partial} \log | F |.
$$

Then we have:

(i) $\Theta(\|T\|; a)$ is the order of zero of $a$ for $F(z)$; in particular $\Theta(\|T\|; a) = 0$ for $F(a) \neq 0$.

(ii) If $F(z)$ is a polynomial of degree $m$ in $\mathbf{C}^n$ then for every $a \in \mathbf{C}^n$ we have

$$
\lim _ {r \rightarrow \infty} \Theta (\| T \|; r, a) = m.
$$

(iii) If $\Theta(\|T\|; r, a) \leq m$ for some $a$ and every $r$, then $F(z) = 0$ is an algebraic hypersurface of degree $\leq m$.

Proof. Let W be the divisor  $F(z)=0$ . For  $a\in C^{n}$  let  $C_{a}$  be the analytic tangent cone of W at a; in other words, if  $P_{m}(z)$  is the first homogeneous non-zero form of degree m in the Taylor expansion of  $F(z)$  in a neighborhood of a, then  $C_{a}$  is the cone defined by the equation

$$
P _ {m} (z) = 0.
$$

The associated (1, 1)-current

$$
\Gamma_ {a} = \frac {1}{\pi} \partial \overline {{{{\partial}}}} \log | P _ {m} (z) |
$$

has the property that

$$
\begin{array}{r l} \Theta (\| T \|; a) & = \Theta (\| \Gamma_ {a} \|; 0) \\ & = \Theta (\| \Gamma_ {a} \|; r, 0) \end{array}
$$

for every $r$; see [2], Theorems 5.4.3 and 4.3.19. Then the result (i) follows from this equation and (ii).

The result (ii) is proved in [7]; see also [6], p. 397.

The result (iii) is a very special case of a theorem of Stoll [11]; it follows also easily from the results and methods of [6], especially (57) of Theorem 5.

We shall apply the results obtained so far to obtain a generalization of Schwartz' lemma for holomorphic functions in  $C^{n}$ . Classically, this states that if  $F(z)$  is holomorphic in an open set containing  $B(R,0)$ , and if  $F(z)$  has a zero of order m at the origin then

$$
| F (w) | \leq \left(\frac {| w |}{R}\right) ^ {m} \max _ {| z | = R} | F (z) |
$$

for $|w| < R$.

Our result is more simply stated in terms of the function $\log |F(z)|$.

Proposition 4. Let $F(z)$ be holomorphic in $|z| \leq R$, let $\tau$ be a positive real number, $0 < \tau < 1$, and let $T = \frac{1}{\pi} \partial \bar{\partial} \log |F(z)|$ be the associated positive (1, 1)-current.

Then for $|w| < \tau R / 6n$ we have

$$
\log | F (w) | \leq \max _ {| z | = R} \log | F (z) | - (1 - \tau) \Theta (\| T \|; | w |, 0) \log \frac {\tau R / 6 n}{| w |}.
$$

Proof. Let $d \| T \| = iT \wedge \omega_{n-1}$ be the positive Radon measure introduced at the beginning of this section. We have

$$
d \| T \| = \frac {1}{2 \pi} \Delta \log | F (z) | \wedge \omega_ {n}
$$

where  $\Delta$  is the Laplace operator in  $C^{n}$ . Assume  $n \geq 2$  (the case n = 1 of Proposition 4 being easy to prove and well-known) and consider the potential

$$
U (z) = - \frac {(n - 2) !}{2 \pi^ {n - 1}} \int_ {| \zeta | <   R / 3} \frac {d \| T \|}{| \zeta - z | ^ {2 n - 2}}.
$$

We have

$$
\frac {1}{2 \pi} \Delta U (z) \wedge \omega_ {n} = \left\{ \begin{array}{c l} d \| T \| & \text { if } | z | <   R / 3 \\ 0 & \text { if } | z | > R / 3 \end{array} \right.
$$

hence one gets

$$
\Delta [ \log | F (z) | - U (z) ] \wedge \omega_ {n} \geq 0
$$

in $|z| < R$. It follows that the function $\log |F(z)| - U(z)$ is subharmonic, hence satisfies the maximum principle. If $|w| < R/3$ we find

$$
\begin{array}{l} \log | F (w) | \leq \max _ {| z | = R} \log | F (z) | \\ - \frac {(n - 2) !}{2 \pi^ {n - 1}} \min _ {| z | = R} \int_ {| \zeta | <   R / 3} \left(\frac {1}{| \zeta - w | ^ {2 n - 2}} - \frac {1}{| \zeta - z | ^ {2 n - 2}}\right) d \| T \| \end{array}
$$

and we need a lower bound for the integral. The measure $d \| T \|$ is positive hence if $|w| < R/3$ we get

$$
\begin{array}{l} \int_ {| \zeta | <   R / 3} \left(\frac {1}{| \zeta - w | ^ {2 n - 2}} - \frac {1}{| \zeta - z | ^ {2 n - 2}}\right) d \| T \| \\ \geq \int_ {| \zeta | <   R / 3} \left[ \frac {1}{(| \zeta | + | w |) ^ {2 n - 2}} - \frac {1}{(R - | \zeta |) ^ {2 n - 2}} \right] d \| T \| \\ = \int_ {0} ^ {R / 3} \left[ \frac {1}{(t + | w |) ^ {2 n - 2}} - \frac {1}{(R - t) ^ {2 n - 2}} \right] d \| T \| B (t, 0) \\ = \left[ \frac {1}{\left(\frac {R}{3} + | w |\right) ^ {2 n - 2}} - \frac {1}{\left(\frac {2}{3} R\right) ^ {2 n - 2}} \right] \cdot \| T \| B \left(\frac {R}{3}, 0\right) \\ + (2 n - 2) \int_ {0} ^ {R / 3} \left[ \frac {1}{(t + | w |) ^ {2 n - 1}} + \frac {1}{(R - t) ^ {2 n - 1}} \right] \cdot \| T \| B (t, 0) d t \\ \geq (2 n - 2) \int_ {0} ^ {R / 3} \frac {\| T \| B (t , 0)}{(t - | w |) ^ {2 n - 1}} d t. \end{array}
$$

Hence we obtain the useful inequality

$$
\begin{array}{l} \log | F (w) | \leq \max _ {| z | = R} \log | F (z) | \\ - \int_ {0} ^ {R / 3} \left(\frac {t}{t + | w |}\right) ^ {2 n - 2} \frac {\Theta (\| T \| ; t , 0)}{t + | w |} d t. \end{array}
$$

By Proposition 2, $\Theta (\| T\| ;t,0)$ is non-decreasing as a function of $t$, in particular $\Theta (\| T\| ;t,0)\geq \Theta (\| T\| ;|w|,0)$

if $t \geq |w|$. It follows that

$$
\begin{array}{l} \int_ {0} ^ {R / 3} \left(\frac {t}{t + | w |}\right) ^ {2 n - 2} \frac {\Theta (\| T \| ; t , 0)}{t + | w |} d t \\ \geq \Theta (\| T \|; | w |, 0) \int_ {| w |} ^ {R / 3} \frac {t ^ {2 n - 2}}{(t + | w |) ^ {2 n - 1}} d t \\ = \Theta (\| T \|; | w |, 0) \int_ {1} ^ {R / 3 | w |} \left(\frac {t}{t + 1}\right) ^ {2 n - 2} \frac {d t}{t}. \end{array}
$$

It is easy to show that if $0 < \tau < 1$ then

$$
\int_ {1} ^ {x} \left(\frac {t}{t + 1}\right) ^ {2 n - 2} \frac {d t}{t} \geq (1 - \tau) \log \frac {\tau x}{2 n}
$$

and this inequality completes the proof of Proposition 4.

## IV. Entire Functions of Given Growth

In this section we give a proof of the

Existence Theorem. Let $V$ be a plurisubharmonic function in $\mathbf{C}^n$.

There exists $F(z)$ holomorphic in $\mathbf{C}^n$ and not identically zero, such that

$$
\int_ {\mathbf {C} ^ {n}} | F | ^ {2} e ^ {- V} (1 + | z | ^ {2}) ^ {- 3 n} \omega_ {n} <   + \infty .
$$

Remarks. It is essential, for the applications we have in mind, that the plurisubharmonic function V should be allowed to take the value  $-\infty$ . In particular, the function F will vanish at every point where  $e^{-V}$  is not a summable function.

The example V=const shows that the exponent 3n cannot be lowered below n.

Our proof is obtained by an application of the powerful theory of $L^2$ estimates and existence theorems for the $\overline{\partial}$ operator, given by Hörmander in his by now classical paper [3]. In fact, a rather similar existence theorem, but assuming $V \in C^2(\mathbf{C}^n)$, was obtained by Hörmander; see [4], Theorem 4.4.4. We shall use the approach followed in [4], pp. 116-117.

Proof. We use the following notations.

$\Omega$ is an open set in $\mathbf{C}^n$;

$L_{(p,q)}^2 (\Omega ,V)$ is the Hilbert space of $(p,q)$-forms

$$
f = \sum_{\substack{|I| = p\\ |J| = q}}f_{I,J}  dz_{I}\wedge d\overline{z}_{J},
$$

with the weighted norm

$$
\| f \| _ {\Omega , V} ^ {2} = \int_ {\Omega} \sum | f _ {I, J} | ^ {2} e ^ {- V} \omega_ {n};
$$

analogously, $L_{(p,q)}^2 (\Omega ,\mathrm{loc})$ is the Fréchet space of $(p,q)$-forms with coefficients $f_{I,J}$ locally in $L^2$.

The key result is

Hörmander's Theorem. Let $\Omega$ be a pseudoconvex open set in $\mathbf{C}^n$ and let $V$ be plurisubharmonic in $\Omega$. Let $f \in L_{(p,q)}^2(\Omega, V) \cap L_{(p,q)}^2(\Omega, \text{loc})$ where $q \geq 1$, and assume that

$$
\overline {{{\partial}}} f = 0.
$$

Then there exists $U \in L_{(p,q - 1)}^2(\Omega, V + 2\log (1 + |z|^2))$ such that

$$
\overline {{{{\partial}}}} U = f
$$

and

$$
\int_ {\Omega} | U | ^ {2} e ^ {- V} (1 + | z | ^ {2}) ^ {- 2} \omega_ {n} \leq \int_ {\Omega} | f | ^ {2} e ^ {- V} \omega_ {n}.
$$

For a proof of this result, see [3], Theorem 2.2.1' and [4], Theorem 4.4.2 (this last reference shows how to eliminate the condition of strict plurisubharmonicity appearing in [3], Theorem 2.2.1').

It is clear that there exists a bounded polycilinder  $\Omega_{0}$  such that  $e^{-V}$  is summable in  $\Omega_{0}$ , because the set of points where  $e^{-V}$  is not summable is closed and of measure 0. After a translation and a linear change of variables we may assume that  $\Omega_{0}$  is the polycilinder

$$
\Omega_ {0} = \{z: | z _ {1} | <   1, \dots , | z _ {n} | <   1 \}.
$$

Let $\Omega_{k}, k = 1, \ldots, n$ be the unbounded polycilinder

$$
\Omega_ {k} = \{z: | z _ {k + 1} | <   1, \dots , | z _ {n} | <   1 \};
$$

we have

$$
\Omega_ {0} \subset \Omega_ {1} \subset \dots \subset \Omega_ {n} = \mathbf {C} ^ {n}
$$

and each $\Omega_{k}$ is a pseudoconvex domain. We define

$$
W = \log (1 + | z | ^ {2})
$$

and note that W is plurisubharmonic.

We claim that there exists $F_{k}$ holomorphic in $\Omega_{k}$, such that

$$
F _ {k} (0) = 1,
$$

$$
\| F _ {k} \| _ {\Omega_ {k}, V + 3 k W} <   + \infty ;
$$

then $F_{n}(z)$ will satisfy the statement of our Existence Theorem.

If $k = 0$, we take

$$
F _ {0} (z) = 1 \quad \text { in } \Omega_ {0}
$$

and  $\|F_{0}\|_{\Omega_{0},V}<+\infty$  simply means that  $e^{-V}$  is summable in  $\Omega_{0}$ , which is true. Now, assuming that  $F_{k-1}(z)$  has been already constructed, we shall use Hörmander's theorem to construct  $F_{k}(z)$  such that

$$
\bar {\partial} F _ {k} = 0 \quad \text { in } \Omega_ {k},
$$

and

$$
\left\| F _ {k} \right\| _ {\Omega_ {k}, V + 3 k W} <   + \infty ,
$$

$$
F _ {k} (z) = F _ {k - 1} (z) \quad \text { on } \Omega_ {k} \cap \{z _ {k} = 0 \};
$$

this last condition will ensure that $F_{k}(0) = 1$.

We follow here an idea of Martineau [9].

Let $\psi(\zeta)$ be a function of one complex variable $\zeta$, which is 1 in the disk $|\zeta|<\frac{1}{2},0$ in $|\zeta|>1$, and is of class $C^1$ and satisfies $|\overline{\partial}\psi|\leq4$ everywhere. Then we define $\psi_k$ in $\Omega_k$ by

$$
\psi_ {k} (z) = \psi \left(z _ {k}\right).
$$

Note that

$$
\operatorname{supp} \psi_ {k} \subset \Omega_ {k - 1},
$$

$$
z _ {k} ^ {- 1} \overline {{{\partial}}} \psi_ {k} \in C _ {(0, 1)} (\Omega_ {k}).
$$

Let

$$
f = z _ {k} ^ {- 1} F _ {k - 1} \bar {\partial} \psi_ {k}
$$

which is defined in $\Omega_{k}$, with $\operatorname{supp} f \subset \Omega_{k-1}$; we have $\bar{\partial}f = 0$ and

$$
| f | \leq 8 | F _ {k - 1} |,
$$

hence recalling that $\| F_{k - 1}\|_{\Omega_{k - 1},V + 3(k - 1)W} <   + \infty$ we find

$$
\| f \| _ {\Omega_ {k}, V + 3 (k - 1) W} <   + \infty .
$$

By Hörmander's theorem, there exists v such that

$$
\overline {{{{\partial}}}} v = f
$$

and

$$
\| v \| _ {\Omega_ {k}, V + (3 k - 1) W} \leq \| f \| _ {\Omega_ {k}, V + 3 (k - 1) W} <   + \infty .
$$

The differential form $f$ is continuous, hence $v$ is continuous too (see [4], Theorem 4.2.5). We assert that

$$
F _ {k} (z) = \psi_ {k} (z) F _ {k - 1} (z) - z _ {k} v (z)
$$

has the required properties.

Clearly, $F_{k}(z)$ is defined in $\Omega_{k}$ because $\operatorname{supp} \psi_{k} \subset \Omega_{k-1}$. Also,

$$
\overline {{{{\partial}}}} F _ {k} = F _ {k - 1} \overline {{{{\partial}}}} \psi_ {k} - z _ {k} \overline {{{{\partial}}}} v = 0,
$$

hence $F_{k}$ is holomorphic in $\Omega_{k}$. It is also obvious that

$$
F _ {k} = F _ {k - 1} \quad \text { on } \Omega_ {k} \cap \{z _ {k} = 0 \},
$$

because v is continuous. Finally,

$$
\begin{array}{r l} & {\| F _ {k} \| _ {\Omega_ {k}, V + 3 k W} \leq \| \psi_ {k} F _ {k - 1} \| _ {\Omega_ {k}, V + 3 k W} + \| z _ {k} v \| _ {\Omega_ {k}, V + 3 k W}} \\ & {\quad \leq \| F _ {k - 1} \| _ {\Omega_ {k - 1}, V + 3 (k - 1) W} + \| v \| _ {\Omega_ {k}, V + (3 k - 1) W}} \end{array}
$$

and this is bounded because of the inductive assumption on $F_{k-1}$ and our previous estimate of the norm of $v$.

This completes the proof.

## V. Auxiliary Lemmas

In this section we use the following notation. If K is a number field and  $\alpha\in K$ , a denominator  $d=\text{den}(\alpha)$  for  $\alpha$  is the smallest positive natural integer such that  $d\alpha$  is an integer in K. We let

$$
\| \alpha \| = \max _ {\sigma} | \sigma \alpha |
$$

where  $\sigma$  ranges over all embeddings of K into C. We define also

$$
\operatorname{size} (\alpha) = \max _ {\sigma} (\log d, \log | \sigma \alpha |)
$$

where $d = \mathrm{den}(\alpha)$. We have the fundamental inequality

$$
- 2 [ K: \mathbf {Q} ] \text { size } (\alpha) \leq \log | \sigma \alpha |
$$

and in fact one even has

$$
- [ K: \mathbf {Q} ] \log \mathrm{den} (\alpha) - ([ K: \mathbf {Q} ] - 1) \text {   size } (\alpha) \leq \log | \sigma \alpha |.
$$

If $P = \sum a_{j} T^{j}, j = (j_{1}, \ldots, j_{d}), T^{j} = T_{1}^{j_{1}} \ldots T_{d}^{j_{d}}$ is a polynomial $P \in K[T_{1}, \ldots, T_{d}]$ we write

$$
\| P \| = \max _ {j} \| a _ {j} \|,
$$

while

$$
| P | = \max _ {j} | a _ {j} |,
$$

and

$$
\operatorname{size} (P) = \max (\deg P, \log \| P \|).
$$

Lemma 1. Let $K$ be a number field. Let $f_1, \ldots, f_N$ be functions of $d$ complex variables, holomorphic at a point $\zeta$ and such that the ring $K[f] = K[f_1, \ldots, f_N]$ is mapped into itself by the partial derivatives $D_\alpha = \partial/\partial z_\alpha$, $\alpha = 1, \ldots, d$. Assume also that $f(\zeta) \in K^N$.

There exists a number $C_1 = C_1(f, \zeta)$ having the following property. If $Q = Q(T_1, \ldots, T_N)$ is a polynomial with coefficients in $O_K$, the ring of integers of $K$, of total degree $\deg Q \leq r$, and if

$$
D ^ {k} = D _ {1} ^ {k _ {1}} \dots D _ {d} ^ {k _ {d}}
$$

is a differential operator of order  $|k|=k_{1}+\cdots+k_{d}$ , then

$$
\left\| D ^ {k} (Q (f)) (\zeta) \right\| \leq \| Q \| (r + | k |) ^ {| k |} C _ {1} ^ {| k | + r}.
$$

Furthermore,

$$
\mathrm{den} D ^ {k} (Q (f)) (\zeta) \leq C _ {1} ^ {| k | + r}.
$$

Proof. This is Lemma 1 of [5], Chapter IV, § 2, p. 34 except for the fact that we have $(r + |k|)^{|k|}$ instead of $r^{|k|}|k|$. Note that the statement of this result in [5] assumes implicitly that $f(\zeta)\in K^{N}$; see [5], Lemma 1, Chapter IV, § 2, p. 23 for a precise statement and proof in case $d = 1$. The improved constant $(r + |k|)^{|k|}$ follows from the argument given in [5].

Lemma 2. Let $K$ be a number field. Let

$$
A X = 0
$$

be a system of r linear equations in n unknowns  $X=(x_{j}), j=1,\ldots,n$ , where  $A=(a_{ij}), i=1,2,\ldots,r, j=1,\ldots,n$  is a  $r \times n$  matrix with coefficients in  $O_{K}$ , the ring of integers of K.

If $n > r$ there exists a non-trivial solution $X$ in $O_K$ such that

$$
\| X \| \leq C _ {2} (C _ {2 n} \| A \|) ^ {r / (n - r)}
$$

where $C_2 = C_2(K)$, $\| X\| = \max_j\| x_j\|$ and $\| A\| = \max_{ij}\| a_{ij}\|$.

Proof. This is a well-known result of Siegel, easily proved using Dirichlet's box principle. See for instance [5], Chapter I, § 2, Lemma 2.

Let $K$ be a number field, let $f = (f_1, \ldots, f_N)$ be meromorphic functions in $\mathbf{C}^d$, of finite order $^1 \leq \rho$, such that the partial derivatives $\partial/\partial z_\alpha$ map the ring $K[f]$ into itself, and such that $\operatorname{tr} \deg K(f) \geq d + 1$. Thus we may assume that $f_1, f_2, \ldots, f_{d+1}$ are algebraically independent over $K$.

Let $S$ be a finite set of points $\zeta_i, i = 1, 2, \ldots, m$ such that $f(\zeta)$ is defined and $f(\zeta) \in K^N$ for $\zeta \in S$. Writing (j) for $(j_1, \ldots, j_{d+1})$ consider the auxiliary

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$h(z)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">≤ρ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">≤ρ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$|h(z)| = O(R^{\rho + \varepsilon})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">≤ρ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  An entire function  $h(z)$  is of finite order  $\leq\rho$  if  $\max_{|z|=R}\log|h(z)|=O(R^{\rho+\varepsilon})$ ; a quotient of two entire functions of order  $\leq\rho$  is meromorphic of order  $\leq\rho$ .</span></small>

function

$$
F (z) = \sum_ {(j) <   J} a _ {(j)} f _ {1} ^ {j _ {1}} \dots f _ {d + 1} ^ {j _ {d + 1}}
$$

where $(j) < J$ means $0 \leq j_{\lambda} < J$ for $\lambda = 1, \ldots, d + 1$. We want to choose the coefficients $a_{(j)}$ not all 0 and in $O_K$, such that

$$
D ^ {\lambda} F (\zeta) = 0
$$

for $|\lambda| < L$, $\zeta \in S$, where $D^{\lambda}$ is the differential operator $D^{\lambda} = D_{1}^{\lambda_{1}} \ldots D_{d}^{\lambda_{d}}$ and $D_{\alpha} = \partial/\partial z_{\alpha}$. Also we want $\|a_{(j)}\|$ not too large.

In the following estimates we shall use the symbol  $\ll$  to denote estimates uniform with respect to L, for fixed f, S and K. We shall use also the symbols  $O(\cdots)$ ,  $o(\cdots)$  with the same meaning.

Lemma 3. If $J^{d + 1} = [mL^d\log L]$ we can choose the coefficients $a_{(j)}$ not all 0 and in $O_K$, such that

$$
D ^ {\lambda} F (\zeta) = 0
$$

for $|\lambda| < L, \zeta \in S$, and moreover

$$
\operatorname{size} \left(a _ {(j)}\right) \ll L.
$$

Proof. By Lemma 1, we have

$$
\left\| D ^ {\lambda} f _ {1} ^ {d _ {1}} \dots f _ {d + 1} ^ {j _ {d + 1}} (\zeta) \right\| \leq ((d + 1) J + L) ^ {L} C _ {1} ^ {(d + 1) J + L}
$$

for $\zeta \in S$, $|\lambda| < L$ and $(j) < J$. It is also clear that there is a common denominator $\Delta$ for $D^{\lambda}f_{1}^{j_{1}}\ldots f_{d+1}^{j_{d+1}}(\zeta)$ satisfying

$$
\Delta \leq C _ {1} ^ {(d + 1) J + L};
$$

here $C_1$ depends only on $f, S$ but is independent of $L$ and $J$.

Solving the system $D^{\lambda}F(\zeta) = 0$ amounts to solving a system of $m\left( \begin{array}{c}L + d\\ d \end{array} \right)$ linear equations

$$
\sum a _ {(j)} \left(\Delta \cdot D ^ {\lambda} f _ {1} ^ {j _ {1}} \dots f _ {d + 1} ^ {J d + 1} (\zeta)\right) = 0
$$

in the $J^{d+1}$ unknowns $a_{(j)}$. The coefficients are in $O_K$ and satisfy

$$
\left\| \Delta \cdot D ^ {\lambda} f _ {1} ^ {j _ {1}} \dots f _ {d + 1} ^ {j _ {d + 1}} (\zeta) \right\| \leq ((d + 1) J + L) ^ {L} C _ {1} ^ {2 (d + 1) J + 2 L},
$$

therefore by Lemma 2 we can find $a_{(j)} \in O_K$ not all 0 and solution of the system, such that

$$
\operatorname{size} \left(a _ {(j)}\right) = \log \| a _ {(j)} \| \ll \frac {r}{n - r} \{L \log (L + J) + J \}
$$

where $r = m\binom{L + d}{d}$ and $n = J^{d + 1}$. We take $J$ such that

$$
J ^ {d + 1} = [ m L ^ {d} \log L ];
$$

then $\frac{r}{n - r} \ll \frac{1}{\log L}$ and Lemma 3 is proved.

We define $s = s(L)$ to be the integer with this property:

$$
D ^ {\sigma} F (\zeta) = 0
$$

for $|\sigma| < s$, $\zeta \in S$, while there exists $\zeta' \in S$ and $\sigma'$ with $|\sigma'| = s$, such that

$$
D ^ {\sigma^ {\prime}} F (\zeta^ {\prime}) \neq 0.
$$

It is clear that

$$
L \leq s <   + \infty ,
$$

by our construction of $F(z)$; in fact $s = +\infty$ would imply $F(z)$ identically 0, contradicting the algebraic independence of $f_1, \ldots, f_{d+1}$.

Let $g(z)$ be an entire function of order $\leq \rho$ such that $g f_j$ is entire for $j = 1, \ldots, d + 1$, of order $\leq \rho$, and let

$$
G _ {s} (z) = g (z) ^ {(d + 1) J} F (z).
$$

Lemma 4. There exists $\sigma'$ with $|\sigma'| = s$ and $\zeta' \in S$ such that

$$
\log | D ^ {\sigma^ {\prime}} G _ {s} (\zeta^ {\prime}) | \geq - ([ K: \mathbf {Q} ] - 1) s \log s + O (s).
$$

Proof. We have

$$
D ^ {\sigma^ {\prime}} G _ {s} (\zeta^ {\prime}) = g (\zeta^ {\prime}) ^ {(d + 1) J} D ^ {\sigma^ {\prime}} F (\zeta^ {\prime})
$$

because $D^{\sigma}F(\zeta') = 0$ for $|\sigma| < s$. Now $\xi = D^{\sigma'} F(\zeta')$ is $\xi \in K$ and is not 0 for some $\sigma'$ with $|\sigma'| = s$ and some $\zeta' \in S$, by definition of $s$. Hence

$$
\begin{array}{c} \log | D ^ {\sigma^ {\prime}} G _ {s} (\zeta^ {\prime}) | = (d + 1) J \log | g (\zeta^ {\prime}) | + \log | \xi | \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq O (J) - ([ K: \mathbf {Q} ] - 1) \text {size} (\xi) + O (\log \operatorname{den} (\xi)); \end{array}
$$

Lemma 4 now follows from Lemmas 1 and 3.

## VI. Proof of Theorem A

We define $T_{s}$ to be the positive (1, 1)-current

$$
T _ {s} = \frac {1}{\pi s} \partial \bar {\partial} \log | G _ {s} (z) |,
$$

where  $G_{s}(z)$  is the entire function constructed at the end of the previous section. The Cauchy inequality for holomorphic functions of several variables gives easily

$$
\log | D ^ {\sigma^ {\prime}} G _ {s} (\zeta^ {\prime}) | \leq s \log s + O (s) + \max _ {| z | = r} \log | G _ {s} (z) |
$$

for every fixed $r > |\zeta'|$.

We apply Proposition 4 and noting that

$$
\Theta (\| s T _ {s} \|; r, 0) = \Theta (\| T _ {s} \|; r, 0) \cdot s
$$

we get

$$
\begin{array}{r l} \log | D ^ {\sigma^ {\prime}} G _ {s} (\zeta^ {\prime}) | & \leq s \log s + O (s) + \max _ {| z | = R} \log | G _ {s} (z) | \\ & - (1 - \tau) \Theta (\| T _ {s} \|; r, 0) s \log \frac {\tau R}{2 n r}. \end{array}
$$

On $|z| = R \log |G(z)|$ is bounded by $O(JR^{\rho + \varepsilon})$, by Lemma 3 and because $g, g f_j$ are entire of order $\leq \rho$. Taking

$$
R = s ^ {\kappa}
$$

where

$$
\kappa <   \frac {1}{(d + 1) \rho},
$$

we see that $\max_{|z|=R} \log |G_s(z)| = o(s \log s)$ for large $R$. We conclude that for fixed $r > |\zeta'$| and $\kappa < \frac{1}{(d+1) \rho}$ and $\tau > 0$ one has the bound

$$
\begin{array}{r l} \log | D ^ {\sigma^ {\prime}} G _ {s} (\zeta^ {\prime}) | & \leq s \log s + o (s \log s) \\ & - (1 - \tau) \kappa \Theta (\| T _ {s} \|; r, 0) [ s \log s + O (s) ]. \end{array}
$$

Comparison with the lower bound given in Lemma 4 gives

Lemma 5. The current $T_{s} = \frac{1}{\pi s} \partial \overline{\partial} \log |G_{s}(z)|$ has the following properties.

(i) $\Theta (\| T_s\| ;r,0)\leq [(d + 1)\rho +o(1)][K:\mathbf{Q}]$ for $s\to +\infty$ and every fixed $r$

(ii) $\Theta (\| T_s\| ;\zeta)\geq 1$ for $\zeta \in S$

Proof. We have just proved (i); inequality (ii) follows from $\Theta(\|s T_s\|; \zeta) \geq s$, which one proves using Proposition 3, (i) and the fact that $D^\sigma G_s(\zeta) = 0$ for $|\sigma| < s$, $\zeta \in S$ by construction of $G_s$.

Inequality (i) of Lemma 5 shows that the norms $\| T_s\| \Omega$ are uniformly bounded as $s\to +\infty$, for every compact subset $\Omega$ of $\mathbf{C}^d$; by the Alaoglu-Bourbaki theorem we can take a weak limit $T$ of the sequence $T_{s}$, possibly by taking a subsequence. The limit current $T$ is again positive, $\partial$ and $\overline{\partial}$-closed; we assert also that

$$
\| T _ {s} \| \Omega \rightarrow \| T \| \Omega
$$

for every compact subset $\Omega$ of $\mathbf{C}^d$. In fact, by Proposition 1 we have

$$
\| T _ {s} \| \Omega = i T _ {s} (\varphi_ {\Omega} \omega_ {n - 1})
$$

where  $\varphi_{\Omega}$  is the characteristic function of the set  $\Omega$ ; our assertion then follows because of weak convergence, noting that  $\varphi_{\Omega}\omega_{n-1}$  is independent of s.

It is clear that this implies

$$
\Theta (\| T _ {s} \|; r, a) \rightarrow \Theta (\| T \|; r, a)
$$

for every $r, a$. But then

$$
\varlimsup_ {s \rightarrow \infty} \Theta (\| T _ {s} \|; \zeta) \leq \Theta (\| T \|; \zeta).
$$

In fact

$$
\begin{array}{r l} \Theta (\| T \|; r, \zeta) & = \lim _ {s \to \infty} \Theta (\| T _ {s} \|; r, \zeta) \\ & \geq \varlimsup_ {s \to \infty} \Theta (\| T _ {s} \|; \zeta), \end{array}
$$

the last inequality coming from Proposition 2; letting $r \to 0$ we get what we want, because $T$ is $\overline{\partial}$-closed, hence Proposition 2 applies again.

Thus we have proved

Lemma 6. There exists a positive, $\partial$- and $\bar{\partial}$-closed current $T$ of type (1, 1) with the following properties.

(i) $\Theta (\| T\| ;r,a)\leq (d + 1)\rho [K:\mathbf{Q}]$ for every $r,a$

(ii) $\Theta (\| T\| ;\zeta)\geq 1$ for $\zeta \in S$

Proof. Only (i) requires some explanation in case  $a \neq 0$ . The general case follows by noting that  $B(r - |a|, 0) \subseteq B(r, a) \subseteq B(r + |a|, 0)$ , which gives easily

$$
\begin{array}{r l} \left(1 - \frac {| a |}{r}\right) ^ {2 n - 2} \Theta (\| T \|; r - | a |, 0) & \leq \Theta (\| T \|; r, a) \\ & \leq \left(1 + \frac {| a |}{r}\right) ^ {2 n - 2} \Theta (\| T \|; r + | a |, 0), \end{array}
$$

and letting $r \to +\infty$. The result now follows from Proposition 2.

In order to prove Theorem A, it is enough to show that if a set S is such that a current satisfying Lemma 6 exists, then S lies in a algebraic hypersurface of degree  $\leqq d(d+1)\rho[K:\mathbf{Q}]+2d$ .

By making a translation, we may suppose that the function of r

$$
\frac {1}{r} \Theta (\| T \|; r, 0)
$$

is summable at the origin. Consider the potential

$$
V (z) = \frac {(n - 2) !}{2 \pi^ {n - 1}} \int_ {\zeta \in \mathbb {C} ^ {n}} \left(\frac {1}{| \zeta | ^ {2 n - 2}} - \frac {1}{| \zeta - z | ^ {2 n - 2}}\right) d \| T \|;
$$

20 Inventiones math, Vol. 10

the integral is convergent by (i) of Lemma 6 and because $\frac{1}{r}\Theta (\| T\| ;r,0)$ is summable at $r = 0$ (see for instance [6], Theorem 1, pp. 380-381). The potential $V(z)$ verifies

$$
\frac {1}{2 \pi} \Delta V (z) \wedge \omega_ {n} = d \| T \|
$$

hence  $V(z)$  is subharmonic in  $C^{d}$ . But in fact, a fundamental theorem of Lelong [6], Theorem 3, p. 387 (the theorem is stated with the condition that supp(T) does not contain the origin, but in fact the weaker condition that  $\frac{1}{r}\Theta(\|T\|; r, 0)$  be summable at r=0 suffices) shows that

$$
\frac {1}{\pi} \partial \overline {{{{\partial}}}} V (z) = T.
$$

Hence  $V(z)$  is plurisubharmonic.

Lemma 7. The function  $V(z)$  has the following properties.

(i) $V(z)\leq [1 + o(1)]\Theta (\| T\| ;\infty ,0)\log |z|$ as $|z|\to +\infty$

(ii) $V(z)\leq -\left[1 + o(1)\right]\Theta (\| T\| ;\zeta)\log \frac{1}{|z - \zeta|}$ as $z\to \zeta$

Proof. Let $\Theta (\infty) = \Theta (\| T\| ;\infty ,0)$. We have

$$
\frac {1}{| \zeta | ^ {2 n - 2}} - \frac {1}{| \zeta - z | ^ {2 n - 2}} \ll \frac {| z |}{| \zeta | ^ {2 n - 1}}
$$

for $|\zeta| > |z|$. Hence

$$
V (z) \leq \frac {(n - 2) !}{2 \pi^ {n - 1}} \int_ {| \zeta | <   | z |} \frac {1}{| \zeta | ^ {2 n - 2}} d \| T \| + O \left(| z | \int_ {| \zeta | > | z |} \frac {1}{| \zeta | ^ {2 n - 1}} d \| T \|\right).
$$

We have

$$
\begin{array}{r l} \int_ {| \zeta | > | z |} \frac {1}{| \zeta | ^ {2 n - 1}} d \| T \| & = \int_ {| z |} ^ {\infty} \frac {1}{t ^ {2 n - 1}} d \| T \| B (t, 0) \\ & = - \frac {1}{| z | ^ {2 n - 1}} \| T \| B (| z |, 0) + (2 n - 1) \int_ {| z |} ^ {\infty} \frac {\| T \| B (t , 0)}{t ^ {n}} d t \\ & = O \left(\frac {1}{| z |}\right), \end{array}
$$

because $\| T\| B(t,0)\leq \frac{\pi^{n - 1}}{(n - 1)!} t^{2n - 2}\Theta (\infty)$ , and $\int \limits_{|z|}^{\infty}t^{-2}dt = O\left(\frac{1}{|z|}\right).$

In the same way we have

$$
\begin{array}{r l} \int_ {| \zeta | <   | z |} \frac {1}{| \zeta | ^ {2 n - 2}} d \| T \| = & \int_ {0} ^ {| z |} \frac {1}{t ^ {2 n - 2}} d \| T \| B (t, 0) \\ & \leq \frac {\| T \| B (| z | , 0)}{| z | ^ {2 n - 2}} + (2 n - 2) \int_ {0} ^ {| z |} \frac {\| T \| B (t , 0)}{t ^ {2 n - 1}} d t \\ & = O (1) + (2 n - 2) \int_ {1} ^ {| z |} \frac {\pi^ {n - 1}}{(n - 1) !} \frac {\Theta (\| T \| ; t , 0)}{t} d t \\ & \leq (2 n - 2) \frac {\pi^ {n - 1}}{(n - 1) !} \Theta (\infty) \log | z | + O (1) \end{array}
$$

for $|z| > 1$. These two estimates together prove statement (1).

The proof of (ii) is very similar. We have, for $\zeta_0 \neq 0$

$$
V (z) = - \frac {(n - 2) !}{2 \pi^ {n - 1}} \int_ {| \zeta - \zeta_ {0} | <   1} \frac {1}{| \zeta - z | ^ {2 n - 2}} d \| T \| + O (1)
$$

as $z\to \zeta_0$ .We have

$$
\frac {1}{| \zeta - z | ^ {2 n - 2}} \geq \frac {1}{(| \zeta - \zeta_ {0} | + | z - \zeta_ {0} |) ^ {2 n - 2}}
$$

so we have to get a lower bound for

$$
\int_ {| \zeta - \zeta_ {0} | <   1} \frac {1}{(| \zeta - \zeta_ {0} | + | z - \zeta_ {0} |) ^ {2 n - 2}} d \| T \|.
$$

This integral is

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {1}{(t + | z - \zeta_ {0} |) ^ {2 n - 2}} d \| T \| B (t, \zeta_ {0}) \\ = O (1) + (2 n - 2) \int_ {0} ^ {1} \frac {\| T \| B (t , \zeta_ {0})}{(t + | z - \zeta_ {0} |) ^ {2 n - 1}} d t \\ \geq O (1) + \frac {2 \pi^ {n - 1}}{(n - 2) !} \Theta (\| T \|; \zeta_ {0}) \int_ {0} ^ {1} \frac {t ^ {2 n - 2}}{(t + | z - \zeta_ {0} |) ^ {2 n - 1}} d t. \end{array}
$$

Finally

$$
\begin{array}{r l} & \int_ {0} ^ {1} \frac {t ^ {2 n - 2}}{(t + \alpha) ^ {2 n - 1}} d t = \int_ {\alpha} ^ {1 + \alpha} \frac {(t - \alpha) ^ {2 n - 2}}{t ^ {2 n - 1}} d t \\ & \quad = \int_ {\alpha} ^ {1 + \alpha} \frac {d t}{t} + O \left(\alpha \int_ {\alpha} ^ {1 + \alpha} \frac {d t}{t ^ {2}}\right) = \log \frac {1}{\alpha} + O (1), \end{array}
$$

and (ii) of Lemma 7 is proved.

20\*

Now we apply the Existence Theorem, for the plurisubharmonic function $\kappa V(z)$, where $\kappa$ is a constant $\kappa > 2d$. We obtain that there exists $F(z)$ entire in $\mathbf{C}^d$ and not identically 0, such that

$$
\int_ {\mathbf {C} ^ {d}} | F | ^ {2} e ^ {- \kappa V} (1 + | z | ^ {2}) ^ {- 3 d} \omega_ {d} <   + \infty .
$$

From $\kappa > 2d$ and (ii) of Lemma 7 we see that $e^{-\kappa V}$ is not summable at every point $\zeta$ where $\Theta(\|T\|; \zeta) \geq 1$. On the other hand, the integral is finite; hence $F(z)$ vanishes at every point where $\Theta(\|T\|; \zeta) \geq 1$. Moreover, for large $z$, we have

$$
| F | ^ {2} e ^ {- \kappa V} (1 + | z | ^ {2}) ^ {- 3 d} \geq | F | ^ {2} | z | ^ {- \kappa \Theta (\infty) - 6 d - \varepsilon}
$$

for every fixed $\varepsilon > 0$. Again, we deduce

$$
\int_ {\mathbf {C} ^ {d}} | F | ^ {2} (1 + | z |) ^ {- \kappa \Theta (\infty) - 6 d - \varepsilon} \omega_ {d} <   + \infty
$$

and $F$ is entire. It follows that $F$ is a polynomial of degree at most

$$
\frac {1}{2} [ \kappa \Theta (\infty) + 6 d + \varepsilon ] - d,
$$

by the classical argument used to prove Liouville's theorem. Letting $\varepsilon \to 0$ and $\kappa \to 2d$ and using Lemma 6, we see that we have found a polynomial $P(z)$, not identically zero, vanishing on $S$ and of degree $\leq d(d + 1)\rho [k:\mathbf{Q}] + 2d$. Clearly one may multiply $P(z)$ by an arbitrary non-zero constant, hence one may suppose

$$
| P | = 1.
$$

We had the condition that S was a finite set of points  $\zeta$ , at which  $f(\zeta)$  was defined and  $f(\zeta) \in K^{N}$ . The finiteness condition is easily removed, because the space of polynomials P of given degree with norm  $|P| = 1$  is compact, and because the bound we have obtained on the degree of P does not depend on S. This completes the proof of Theorem A.

## References

1. Andreotti, A., Vesentini, E.: Carleman estimates for the Laplace-Beltrami equation on complex manifolds. Publ. I.H.E.S. 25, 81–130 (1965).

2. Federer, H.: Geometric measure theory. Berlin-Heidelberg-New York: Springer 1969.

3. Hörmander, L.: $L^2$ estimates and existence theorems for the $\overline{\partial}$ operator. Acta Math. 113, 89-152 (1965).

4. - An introduction to complex analysis in several variables. Princeton: Van Nostrand Co. 1966.

5. Lang, S.: Introduction to transcendental numbers. Reading, Mass.: Addison-Wesley 1966.