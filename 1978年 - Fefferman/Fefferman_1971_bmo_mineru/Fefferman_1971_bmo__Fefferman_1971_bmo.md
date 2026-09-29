## CHARACTERIZATIONS OF BOUNDED MEAN OSCILLATION

## BY CHARLES FEFFERMAN

## Communicated by M. H. Protter, December 14, 1970

BMO (bounded mean oscillation) is the Banach space of all functions $f \in L_{\mathrm{loc}}^{1}(R^{n})$ for which

$$
\left| \left| f \right| \right| _ {\mathrm{BMO}} = \sup _ {Q} \left(\frac {1}{| Q |} \int_ {Q} | f (x) - \operatorname{av} _ {Q} f | d x\right) <   \infty ,
$$

where the sup ranges over all cubes  $Q \subseteq R^{n}$ , and  $av_{Q} f$  is the mean of f over Q. See [5]. For convenience, we identify f and  $f'$  in BMO if  $f - f'$  is constant.

THEOREM 1. BMO is the dual of the Hardy space $H^{1}(R^{n})$. The inner product is given by $\langle f, g \rangle = \int_{R^{n}} f(x) g(x) dx$ for $f \in BMO$ and $g$ belonging to the dense subspace of $C^{\infty}$ rapidly decreasing functions in $H^{1}$.

Here, we regard $H^1$ as the space of $f \in L^1(R^n)$ whose Riesz transforms $R_j(f)$ are all in $L^1$. See [7].

THEOREM 2. A function belongs to BMO if and only if it can be written in the form $g_0 + \sum_{j=1}^{n} R_j(g_j)$ with $g_0, g_1, \cdots, g_n \in L^\infty(R^n)$.

Note that the usual definition

$$
R _ {j} (g) (x) = \lim _ {\epsilon \rightarrow 0; M \rightarrow \infty} \int_ {\epsilon <   | x - y | <   M} K _ {j} (x - y) f (y) d y
$$

with $K_{j}(y) = cy_{j} / |y|^{n + 1}$ need not make sense for all $g \in L^{\infty}$. (Consider $g(x) = \operatorname{sgn}(x)$ on the line.) Therefore, we define

$$
R _ {j} (g) (x) = \lim _ {\epsilon \rightarrow 0} \int_ {\epsilon <   | x - y |} \left[ K _ {j} (x - y) - K _ {j} ^ {0} (- y) \right] g (y) d y,
$$

where $K_{j}^{0}(y) = K_{j}(y)$ for $|y| > 1$ and $K_{j}^{0}(y) = 0$ for $|y| \leq 1$. This makes sense for all $g \in L^{\infty}$, and agrees with the usual definition up to an additive constant if $g$ has compact support. See [3, p. 105].

The main idea in proving Theorems 1 and 2 is to study the Poisson integral of a function in BMO. Recall that any function $f$ satisfying

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">AMS 1969 subject classifications. Primary 3067, 4635.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Key words and phrases. Bounded mean oscillation, Riesz transforms, maximal function, Poisson integral.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Copyright © 1971, American Mathematical Society</span></small>

$$
\int_ {R ^ {n}} \frac {| f (x) |}{(| x | + 1) ^ {n + 1}} d x <   \infty\tag{*}
$$

has a Poisson integral $u(x, t) = \mathrm{P.I.}(f)$ defined on $R_{+}^{n + 1} = R^n \times (0, \infty)$.

THEOREM 3. A function $f$ belongs to BMO if and only if (\*) holds and $\iint_{|x - x_0| < \delta; 0 < t < \delta} t|\nabla u(x, t)|^2 dx dt \leq C\delta^n$ for all $x_0 \in R^n$ and $\delta > 0$.

Theorems 1–3 and their proofs can be used to study  $H^{1}$ . For example,

THEOREM 4. Let $F = (u_0(x, t); u_1(x, t), \dots, u_n(x, t))$ be an $(n+1)$-tuple of harmonic functions on $R_+^{n+1}$, satisfying the Cauchy-Riemann equations of [7]. If the nontangential maximal function $u_0^*(x) \equiv \sup_{|x'| < t; t > 0} |u_0(x - x', t)|$ belongs to $L^1$, then $F$ is in $H^1$.

Different techniques enable us to replace  $L^{1}$  and  $H^{1}$  by  $L^{p}$  and  $H^{p}$,  $0 < p < \infty$. This generalizes a one-dimensional result of D. Burkholder, R. Gundy, and M. Silverstein (see [1] and [2]).

Further applications of Theorems 1–3 appear in [4] and [6]. [4] contains detailed proofs of the results stated here.

## REFERENCES

1. D. Burkholder and R. Gundy, Extrapolation and interpolation of quasi-linear operators on martingales, Acta Math. 124 (1970), 249–304.

2. D. Burkholder, R. Gundy and M. Silverstein, A maximal function characterization of the class  $H^{p}$  (to appear).

3. A. P. Calderón and A. Zygmund, On the existence of certain singular integrals, Acta Math. 88 (1952), 85–139. MR 14, 637.

4. C. Fefferman and E. M. Stein, (in prep.)

5. F. John and L. Nirenberg, On functions of bounded mean oscillation, Comm. Pure Appl. Math. 14 (1961), 785–799.

6. E. M. Stein, $L^p$ boundedness of certain convolution operators, Bull. Amer. Math. Soc. 77 (1971), 404-405.

7. E. M. Stein and G. Weiss, Introduction to Fourier analysis on euclidean spaces, Princeton, 1971.

UNIVERSITY OF CHICAGO, CHICAGO, ILLINOIS 60637