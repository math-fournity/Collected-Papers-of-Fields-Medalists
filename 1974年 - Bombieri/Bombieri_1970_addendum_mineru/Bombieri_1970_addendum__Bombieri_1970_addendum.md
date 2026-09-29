## Werk

Titel: Inventiones Mathematicae

Verlag: Springer

Jahr: 1970

Kollektion: Mathematica

Werk Id: PPN356556735\_0011

PURL: http://resolver.sub.uni-goettingen.de/purl?PID=PPN356556735\_0011 | LOG\_0020

## Terms and Conditions

The Goettingen State and University Library provides access to digitized documents strictly for noncommercial educational, research and private purposes and makes no warranty with regard to their use for other purposes. Some of our collections are protected by copyright. Publication and/or broadcast in any form (including electronic) requires prior written permission from the Goettingen State- and University Library.

Each copy of any part of this document must contain there Terms and Conditions. With the usage of the library's online system to access or download a digitized document you accept the Terms and Conditions.

Reproductions of material on the web site may not be made for or donated to other repositories, nor may be further reproduced without written permission from the Goettingen State- and University Library.

For reproduction requests and permissions, please contact us. If citing materials, please give proper attribution of the source.

## Contact

# Addendum to My Paper "Algebraic Values of Meromorphic Maps"

ENRICO BOMBIERI (Pisa)

## I. Introduction

In my previous paper [1] the following result is crucial (notations are as in [1]):

Existence Theorem. Let V be a plurisubharmonic function in  $C^{n}$ . There exists  $F(z)$  holomorphic in  $C^{n}$  and not identically zero, such that

$$
\int_ {C ^ {n}} | F | ^ {2} e ^ {- V} (1 + | z |) ^ {- 3 n} \omega_ {n} <   + \infty .
$$

In the proof of this theorem we make use of the fact that if V is plurisubharmonic in an open set  $\Omega$  then the set of points at which  $e^{-V}$  is not summable is closed in  $\Omega$  and of measure zero. It has been brought to my attention that a proof of this latter assertion does not seem to be available in the literature and it is the purpose of this short note to elucidate this point.

Following the notation of [1] we write

$$
\frac {1}{\pi} \partial \bar {\partial} V = T
$$

and denote by $\Theta(\|T\|; r, a)$ the average mass of $T$ in the ball $B(r, a)$ of radius $r$ and center $a$. The function $\Theta(\|T\|; r, a)$ is monotone nondecreasing for $r < \text{dist}(a, \partial\Omega)$; in particular

$$
\Theta (\| T \|; a) = \lim _ {r \rightarrow 0} \Theta (\| T \|; r, a)
$$

exists. $\Theta(\|T\|; a)$ is also called the Lelong number of $T$ at the point $a$. We note also the inequality

$$
\begin{array}{r l} \left(1 - \frac {| a |}{r}\right) ^ {2 n - 2} & \Theta (\| T \|; r - | a |, 0) \leq \Theta (\| T \|; r, a) \\ & \leq \left(1 + \frac {| a |}{r}\right) ^ {2 n - 2} \Theta (\| T \|; r + | a |, 0) \end{array}
$$

(see [1], Lemma 6) which will be used later in the proof of Lemma 1. 12 a Inventiones math., Vol. 11

We shall prove

Theorem 1. There exists a constant $\gamma(n) > 0$ depending only on the dimension $n$, with the property that if

$$
\Theta (\| T \|; a) <   \gamma (n)
$$

then $e^{-V(z)}$ is summable in some neighborhood of $z = a$.

Note that one has trivially  $\Theta(\|T\|; a)=0$  almost everywhere hence  $e^{-V}$  is locally summable outside a set closed in  $\Omega$  and of measure zero, as was asserted in [1]. Actually much more than this is true and the existence Theorem gives at once:

Theorem 2. Let $V$ be a plurisubharmonic function in $\mathbf{C}^n$. Then $e^{-V}$ is locally summable outside a complex analytic hypersurface of $\mathbf{C}^n$.

It is possible to show that $e^{-V}$ is not summable at every point for which

$$
\Theta (\| T \|; a) > 2 n,
$$

by using the argument of [1], (ii) of Lemma 7 together with the fact that one can represent $V(z)$ locally by a Newtonian potential modulo harmonic functions. Combining this result with a local version of our Existence Theorem one gets the following statement of independent interest:

Structure Theorem. For every positive $c$ the set of points at which

$$
\Theta (\| T \|; a) > c
$$

is locally contained in a complex analytic hypersurface. In particular, this set has a locally finite $(2n - 2)$-dimensional Hausdorff measure.

The Structure Theorem and Theorem 1 give immediately a local version of Theorem 2, namely:

Theorem 2A. Let $V$ be a plurisubharmonic function in an open set $\Omega$. Then $e^{-V}$ is locally summable in $\Omega \setminus N$, where $N$ is closed in $\Omega$ and locally contained in a complex analytic hypersurface.

## II. Proof of Theorem 1

Let $T = \frac{1}{\pi} \partial \bar{\partial} V$ and let

$$
d \| T \| = i T \wedge \omega_ {n}
$$

be the associated positive Radon measure. We shall examine the summability of  $e^{-V}$  at the origin; the problem is clearly local so we may assume that V is defined in the ball  $|z|<1$ . The Newtonian potential

$$
P _ {\varepsilon} (z) = - \frac {(n - 2) !}{4 \pi^ {n - 1}} \int_ {| \zeta | <   \varepsilon} \frac {1}{| z - \zeta | ^ {2 n - 2}} d \| T \| (\zeta)
$$

differs from  $V(z)$  in  $|z|<\varepsilon$  only by a harmonic function, so that we shall consider the equivalent problem of the summability of  $P_{\varepsilon}(z)$  at the origin.

Lemma 1. If $|a| < \varepsilon$ and $r < \varepsilon$ we have

$$
\int_ {| z - a | <   r} | \nabla P _ {\varepsilon} (z) | \omega_ {n} (z) \leq c _ {1} \Theta (\| T \|; 3 \varepsilon , 0) r ^ {2 n - 1}.
$$

Proof. We have

$$
| \nabla P _ {\varepsilon} (z) | \leq c _ {2} \int_ {| \zeta | <   \varepsilon} \frac {1}{| z - \zeta | ^ {2 n - 1}} d \| T \| (\zeta)
$$

because $d\| T\|$ is a positive measure. Hence

$$
\begin{array}{l} \int_ {| z - a | <   r} | V P _ {\varepsilon} (z) |   \omega_ {n} (z) \leq c _ {2} \int_ {| z - a | <   r} \int_ {| \zeta | <   \varepsilon} \frac {1}{| z - \zeta | ^ {2 n - 1}} d \| T \| (\zeta)   \omega_ {n} (z) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}
$$

Next, one checks easily that

$$
\int_ {| z - a | <   r} \frac {\omega_ {n} (z)}{| z - \zeta | ^ {2 n - 1}} \leq c _ {3} r (t + 1) ^ {- 2 n + 1}
$$

where

$$
t = \frac {1}{r} | \zeta - a |;
$$

for if  $t \geq 2$  then  $|z - \zeta| \geq r(t - 1)$ , while if t < 2 then  $|z - a| < r$  is contained in  $|z - \zeta| < 3r$  and the computation again becomes obvious. We deduce the bound

$$
\begin{array}{l} I \leq c _ {3} r \int_ {| \zeta - a | <   2 \varepsilon} \left(1 + \frac {1}{r} | \zeta - a |\right) ^ {- 2 n + 1} d \| T \| (\zeta) \\ = c _ {3} r \int_ {0} ^ {2 \varepsilon / r} (1 + t) ^ {- 2 n + 1} d \| T \| B (r t, a) \\ = \frac {c _ {3} r}{\left(1 + \frac {2 \varepsilon}{r}\right) ^ {2 n - 1}} \| T \| B (2 \varepsilon , a) + c _ {3} r (2 n - 1) \int_ {0} ^ {2 \varepsilon / r} \frac {\| T \| B (r t , a)}{(1 + t) ^ {2 n}} d t. \end{array}
$$

Finally

$$
\begin{array}{r l} \| T \| B (r t, a) & = \frac {\pi^ {n - 1}}{(n - 1) !} (r t) ^ {2 n - 2} \Theta (\| T \|; r t, a) \\ & \leq \frac {\pi^ {n - 1}}{(n - 1) !} (r t) ^ {2 n - 2} \Theta (\| T \|; 2 \varepsilon , a) \\ & \leq c _ {4} (r t) ^ {2 n - 2} \Theta (\| T \|; 3 \varepsilon , 0) \end{array}
$$

12 b Inventiones math., Vol. 11

the last inequality being one noted earlier. Combining this estimate with the bound already obtained for I, Lemma 1 follows.

Lemma 2 (John and Nirenberg). Let $U(z)$ be a summable function in $|z| < 2R$, such that

$$
\int_ {| z - a | <   r} | \nabla U (z) | \omega_ {n} (z) \leq \gamma r ^ {2 n - 1}
$$

for every $a, r$ satisfying $|a| < R, r < R$.

Then we have

$$
\min _ {k} \int_ {| z | <   \frac {1}{2} R} \exp \left(c _ {5} \gamma^ {- 1} | U (z) - k |\right) \omega_ {n} (z) \leq c _ {6} R ^ {2 n},
$$

where $c_{5}, c_{6}$ depend only on $n$.

Proof. This is a special case of a famous result of John and Nirenberg [2]; a simple proof of Lemma 2 has been found recently by Trudinger [3]. Combining Lemmas 1 and 2 we get that $\exp\bigl(-c_5\gamma^{-1}P_\varepsilon(z)\bigr)$, and hence $\exp\bigl(-c_5\gamma^{-1}V(z)\bigr)$, is summable in $|z|<\varepsilon/2$ with $\gamma$ given by

$$
\gamma = c _ {1} \Theta (\| T \|; 3 \varepsilon , 0).
$$

Finally assume $\Theta(\|T\|; 0) < c_5 / c_1 = \gamma(n)$. Then there exists $\varepsilon > 0$ such that $\Theta(\|T\|; 3\varepsilon, 0) < c_5 / c_1$ and $\exp(-V(z))$ will be summable in a neighborhood of the origin; this completes the proof of Theorem 1.

## References

1. Bombieri, E.: Algebraic values of meromorphic maps. Inventiones Math. 10, 267–287 (1970).

2. John, F., Nirenberg, L.: On functions of bounded mean oscillation. Comm. Pure Appl. Math. 14, 415-426 (1961).

3. Trudinger, N.S.: On embeddings into Orlicz spaces and some applications. J. Math. Mech. 17, 473-483 (1967).

E. Bombieri

Istituto Matematico “Leonida Tonelli”
Università di Pisa
Via Derna 1
I-56100 Pisa