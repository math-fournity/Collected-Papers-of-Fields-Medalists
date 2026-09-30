# The sphere packing problem in dimension 8

Maryna S. Viazovska

April 5, 2017

In this paper we prove that no packing of unit balls in Euclidean space$\mathbb { R } ^ { 8 }$ has density greater than that of the$E _ { 8 }$-lattice packing.

Keywords: Sphere packing, Modular forms, Fourier analysis AMS subject classification: 52C17, 11F03, 11F30

## 1 Introduction

The sphere packing constant measures which portion of d-dimensional Euclidean space can be covered by non-overlapping unit balls. More precisely, let$\mathbb { R } ^ { d }$be the Euclidean vector space equipped with distance$\| \cdot \|$and Lebesgue measure$\operatorname { V o l } ( \cdot )$. For$\boldsymbol { x } \in \mathbb { R } ^ { d }$and $r \in \mathbb { R } _ { > 0 }$we denote by$B _ { d } ( x , r )$the open ball in$\mathbb { R } ^ { d }$with center$x$and radius r. Let $X \subset \mathbb { R } ^ { d }$be a discrete set of points such that$\| x - y \| \geq 2$ for any distinct$x , y \in X$. Then the union

$$
\mathcal {P} = \bigcup_ {x \in X} B _ {d} (x, 1)
$$

is a sphere packing. If X is a lattice in$\mathbb { R } ^ { d }$then we say that$\mathcal { P }$is a lattice sphere packing. The finite density of a packing P is defined as

$$
\Delta_ {\mathcal {P}} (r) := \frac {\mathrm{Vol} (\mathcal {P} \cap B _ {d} (0 , r))}{\mathrm{Vol} (B _ {d} (0 , r))}, \quad r > 0.
$$

We define the density of a packing$\mathcal { P }$as the limit superior

$$
\Delta_ {\mathcal {P}} := \limsup _ {r \to \infty} \Delta_ {\mathcal {P}} (r).
$$

The number we want to know is the supremum over all possible packing densities

$$
\Delta_{d}:= \sup_{\substack{\mathcal{P}\subset \mathbb{R}^{d}\\ \text{sphere packing}}}\Delta_{\mathcal{P}},
$$

called the sphere packing constant.

For which dimensions do we know the exact value of$\Delta _ { d } ?$Trivially, in dimension 1 we have$\Delta _ { 1 } = 1$. It has long been known that a best packing in dimension 2 is the familiar hexagonal lattice packing, in which each disk is touching six others. The first proof of this result was given by A. Thue at the beginning ot twentieth century [18]. However, his proof was considered by some experts incomplete. A rigorous proof was given by L. Fejes Tóth in 1940s [10]. The density of the hexagonal lattice packing is$\frac { \pi } { \sqrt { 1 2 } }$, therefore$\Delta _ { 2 } = \textstyle { \frac { \pi } { \sqrt { 1 2 } } } \approx 0 . 9 0 6 9 0$. The packing problem in dimension 3 turned out to be more dificult. Johannes Kepler conjectured in his essay “On the six-cornered snowflake” (1611) that no arrangement of equally sized spheres filling space has density greater than$\frac { \pi } { \sqrt { 1 8 } }$. This density is attained by the face-centered cubic packing and also by uncountably many non-lattice packings. The Kepler conjecture was famously proven by T. Hales in 1998 [11] and therefore we know that$\Delta _ { 3 } = { \frac { \pi } { \sqrt { 1 8 } } } \approx 0 . 7 4 0 4 8$. In 2015 Hales and his 21 coauthors published a complete formal proof of the Kepler conjecture that can be verified by automated proof checking software. Before now, the exact values of the sphere packing constants in all dimensions greater than 3 have been unknown. A list of conjectural best packings in dimensions less than 10 can be found in [6]. Upper bounds for the sphere packing constants$\Delta _ { d }$as$d \leq 3 6$are given in [4]. Surprisingly enough, these upper bounds and known lower bounds on$\Delta _ { d }$are extremely close in dimensions$d = 8$ and$d = 2 4$

The main result of this paper is the proof that

$$
\Delta_ {8} = \frac {\pi^ {4}}{3 8 4} \approx 0. 2 5 3 6 7.
$$

This is the density of the$E _ { 8 }$-lattice sphere packing. Recall that the E<sub>8</sub>-lattice$\Lambda _ { 8 } \subset \mathbb { R } ^ { 8 }$ is given by

$$
\Lambda_ {8} = \{(x _ {i}) \in \mathbb {Z} ^ {8} \cup (\mathbb {Z} + \frac {1}{2}) ^ {8} | \sum_ {i = 1} ^ {8} x _ {i} \equiv 0 (\mathrm{mod} 2) \}.
$$

$\Lambda _ { 8 }$is the unique up to isometry positive-definite, even, unimodular lattice of rank 8. The name derives from the fact that it is the root lattice of the$E _ { 8 }$root system. The minimal distance between two points in$\Lambda _ { 8 }$is$\sqrt { 2 }$. The$E _ { 8 }$-lattice sphere packing is the packing of unit balls with centers at$\scriptstyle { \frac { 1 } { \sqrt { 2 } } } \Lambda _ { 8 }$. Our main result is

Theorem 1. No packing of unit balls in Euclidean space$\mathbb { R } ^ { 8 }$has density greater than that of the$E _ { 8 } - l a t t i c e$packing.

Furthermore, our proof of Theorem 1 combined with arguments given in [4, Section 8] implies that the$E _ { 8 } – \mathrm { l a t t i c e }$sphere packing is the unique periodic packing of maximal density.

The paper is organized as follows. In Section 2 we explain the idea of the proof of Theorem 1 and describe the methods we use. In Section 3 we give a brief overview of the theory of modular forms. In Section 4 we construct supplementary radial functions$a , b : \mathbb { R } ^ { 8 } \to i \mathbb { R }$, which are eigenfunctions of the Fourier transform and have double zeroes at almost all points of$\Lambda _ { 8 }$. This construction is crucial for our proof of Theorem 1. Finally, in Section 5 we complete the proof.

## 2 Linear programming bounds

Our proof of Theorem 1 is based on linear programming bounds. This technique was successfully applied to obtain upper bounds in a wide range of discrete optimization problems such as error-correcting codes [7], equal weight quadrature formulas [8], and spherical codes [13, 16]. In exceptional cases linear programming bounds are optimal [5]. However, in general linear programming bounds are not sharp and it is an open question how big the errors of such bounds can be. It is known [2] that the linear programming bounds for the minimal number of points in an equal weight quadrature formula on the sphere$S ^ { d }$are asymptotically optimal up to a constant depending on$d .$Linear programming bounds can also be applied to the sphere packing problem. Kabatiansky and Levenshtein [13] deduced upper bounds for sphere packing from their results on spherical codes.

In 2003 Cohn and Elkies [4] developed linear programming bounds that apply directly to sphere packings. Using their new method they improved the previously known upper bounds for the sphere packing constant in dimensions from 4 to 36. The most striking results obtained by this technique are upper bounds for dimensions 8 and 24. For example, their upper bound for$\Delta _ { 8 }$was only 1.000001 times greater than the lower bound, which is given by the density of the$E _ { 8 }$sphere packing. This bound can be improved even further by more extensive computer computations.

We explain the Cohn–Elkies linear programming bounds in more detail. To this end we recall a few definitions from Fourier analysis. The Fourier transform of an$L ^ { 1 }$function$f : \mathbb { R } ^ { d } \to \mathbb { C }$ is defined as

$$
\mathcal {F} (f) (y) = \widehat {f} (y) := \int_ {\mathbb {R} ^ {d}} f (x) e ^ {- 2 \pi i x \cdot y} d x, \quad y \in \mathbb {R} ^ {d}
$$

where$x \cdot y = { \textstyle { \frac { 1 } { 2 } } } \| x \| ^ { 2 } + { \textstyle { \frac { 1 } { 2 } } } \| y \| ^ { 2 } - { \textstyle { \frac { 1 } { 2 } } } \| x - y \| ^ { 2 }$is the standard scalar product in$\mathbb { R } ^ { d }$. A$C ^ { \infty }$ function$f : \mathbb { R } ^ { d } \to \mathbb { C }$ is called a Schwartz function if it tends to zero as$\| x \| \to \infty$ faster then any inverse power of$\lVert x \rVert$, and the same holds for all partial derivatives of$f .$ The set of all Schwartz functions is called the Schwartz space. The Fourier transform is an automorphism of this space. We will also need the following wider class of functions. We say that a function$f : \mathbb { R } ^ { d } \to \mathbb { C }$ is admissible if there is a constant$\delta > 0$such that $| f ( x ) |$and$| { \widehat { f } } ( x ) |$are bounded above by a constant times$( 1 + | x | ) ^ { - d - \delta }$. The following theorem is the key result of [4]:

Theorem 2. (Cohn, Elkies$[ 4 ] )$Suppose that$f : \mathbb { R } ^ { d } \to \mathbb { R }$ is an admissible function, is not identically zero, and satisfies:

$$
f (x) \leq 0$ for$\| x \| \geq 1$\tag{1}
$$

and

$$
\widehat {f} (x) \geq 0 \text {   for   all   } x \in \mathbb {R} ^ {d}.\tag{2}
$$

Then the density of d-dimensional sphere packings is bounded above by

$$
\frac {f (0)}{\widehat {f} (0)} \cdot \frac {\pi^ {\frac {d}{2}}}{2 ^ {d} \Gamma (\frac {d}{2} + 1)} = \frac {f (0)}{\widehat {f} (0)} \cdot \operatorname{Vol} B _ {d} (0, \frac {1}{2}).
$$

Without loss of generality we can assume that a function$f$in Theorem 2 is radial, i. e. its value at each point depends only on the distance between the point and the origin [4, p. 695]. For a radial function$f _ { 0 } : \mathbb { R } ^ { d } \to \mathbb { R }$ we will denote by$f _ { 0 } ( r )$the common value of$f _ { 0 }$on vectors of length r. Henceforth we assume$d = 8$. The Poisson summation formula implies

$$
\sum_ {\ell \in \frac {1}{\sqrt {2}} \Lambda_ {8}} f (\ell) = 2 ^ {4} \sum_ {\ell \in \sqrt {2} \Lambda_ {8}} \widehat {f} (\ell).
$$

Hence, if a function f satisfies conditions (1) and (2) then

$$
\frac {f (0)}{\widehat {f} (0)} \geq 2 ^ {4}.
$$

We$\operatorname { s a y }$that an admissible function$f : \mathbb { R } ^ { 8 } \to \mathbb { R }$ is optimal if it satisfies (1), (2) and $f ( 0 ) / \widehat { f } ( 0 ) = 2 ^ { 4 }$

The main step in our proof of Theorem 1 is the explicit construction of an optimal function. It will be convenient for us to scale this function by$\sqrt { 2 }$

Theorem 3. There exists a radial Schwartz function$g : \mathbb { R } ^ { 8 } \to \mathbb { R }$which satisfies:

$$
g (x) \leq 0$ for$\| x \| \geq \sqrt { 2 }$,\tag{3}
$$

$$
\widehat {g} (x) \geq 0 \text {   for   all   } x \in \mathbb {R} ^ {8},\tag{4}
$$

$$
g (0) = \widehat {g} (0) = 1.\tag{5}
$$

Moreover, the values$g ( x )$and${ \widehat { g } } ( x )$do not vanish for all vectors x with$\| x \| ^ { 2 } \notin 2 \mathbb { Z } _ { > 0 }$

Theorem 2 applied to the optimal function$f ( x ) = g ( { \sqrt { 2 } } x )$immediately implies Theorem 1. Additionally, the function$g$satisfies the conclusions of [4, Conjecture 8.1]. This implies the uniqueness of the densest periodic sphere packing in R<sup>8</sup>.

Let us briefly explain our strategy for the proof of Theorem 3. First, we observe that conditions (3)–(5) imply additional properties of the function$g .$Suppose that there exists a Schwartz function$g$such that the conditions (3)–(5) hold. The Poisson summation formula states

$$
\sum_ {\ell \in \Lambda_ {8}} g (\ell) = \sum_ {\ell \in \Lambda_ {8}} \widehat {g} (\ell).\tag{6}
$$

Since$\| \ell \| \geq \sqrt { 2 }$for all$\ell \in \Lambda _ { 8 } \backslash \{ 0 \}$, conditions (3) and (5) imply

$$
\sum_ {\ell \in \Lambda_ {8}} g (\ell) \leq g (0) = 1.\tag{7}
$$

On the other hand, conditions (4) and (5) imply

$$
\sum_ {\ell \in \Lambda_ {8}} \widehat {g} (\ell) \geq \widehat {g} (0) = 1.\tag{8}
$$

Therefore, we deduce that$g ( \ell ) = \widehat { g } ( \ell ) = 0$for all$\ell \in \Lambda _ { 8 } \backslash \{ 0 \}$. Moreover, the first derivatives$\begin{array} { r } { \frac { d } { d r } g ( r ) } \end{array}$and$\begin{array} { r } { \frac { d } { d r } \widehat { g } ( r ) } \end{array}$also vanish at all$\Lambda _ { 8 }$-lattice points of length bigger than $\sqrt { 2 }$. We will say that$g$and$\widehat g$have double zeroes at these points. This property gives us a hint on constructing the function g explicitly.

In Section 5 a function g satisfying (3)–(5) is given in a closed form. Namely, it is defined as an integral transform (Laplace transform) of a modular form of a certain kind. The next section is a brief introduction to the theory of modular forms.

## 3 Modular forms

Let H be the upper half-plane$\{ z \in \mathbb { C } \mid \operatorname { I m } \left( z \right) > 0 \}$. The modular group$\Gamma ( 1 ) : = \mathrm { P S L } _ { 2 } ( \mathbb { Z } )$ acts on H by linear fractional transformations

$$
\left( \begin{array}{c c} a & b \\ c & d \end{array} \right) z := \frac {a z + b}{c z + d}.
$$

Let$N$be a positive integer. The level N principal congruence subgroup of$\Gamma ( 1 )$is

$$
\Gamma (N) := \left\{\left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \in \Gamma (1) \big | \left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \equiv \left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right) \bmod N \right\}.
$$

A subgroup$\Gamma \subset \Gamma ( 1 )$is called a congruence subgroup if$\Gamma ( N ) \subset \Gamma$ for some$N \in \mathbb { N }$.. An important example of a congruence subgroup is

$$
\Gamma_ {0} (N) := \left\{\left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \in \Gamma (1) \big | c \equiv 0 \bmod N \right\}.
$$

Let$z \in \mathbb { H } , k \in \mathbb { Z }$, and${ \left( \begin{array} { l } { a } \end{array} \right) } \in \operatorname { S L } _ { 2 } ( \mathbb { Z } )$. The automorphy factor of weight k is defined as

$$
j _ {k} (z, \left( \begin{array}{c c} a & b \\ c & d \end{array} \right)) := (c z + d) ^ {- k}.
$$

The automorphy factor satisfies the chain rule

$$
j _ {k} (z, \gamma_ {1} \gamma_ {2}) = j _ {k} (z, \gamma_ {2}) j _ {k} (\gamma_ {2} z, \gamma_ {1}).
$$

Let$F$be a function on H and$\gamma \in \mathrm { P S L } _ { 2 } ( \mathbb { Z } )$. Then the slash operator acts on$F$by

$$
(F | _ {k} \gamma) (z) := j _ {k} (z, \gamma) F (\gamma z).
$$

The chain rule implies

$$
F | _ {k} \gamma_ {1} \gamma_ {2} = (F | _ {k} \gamma_ {1}) | _ {k} \gamma_ {2}.
$$

A (holomorphic) modular form of integer weight k and congruence subgroup Γ is a holomorphic function$f : \mathbb { H } \to \mathbb { C }$such that:

1.$f | _ { k } \gamma = f$for all$\gamma \in \Gamma$and

2. for each$\alpha \in \Gamma ( 1 )$the function$f | _ { k } \alpha$has Fourier expansion

$$
f | _ {k} \alpha (z) = \sum_ {n = 0} ^ {\infty} c _ {f} (\alpha , \frac {n}{n _ {\alpha}}) e ^ {2 \pi i \frac {n}{n _ {\alpha}} z}
$$

for some$n _ { \alpha } \in \mathbb { N }$and Fourier coeficients$c _ { f } ( \alpha , m ) \in \mathbb { C }$

Let$M _ { k } ( \Gamma )$be the space of modular forms of weight k for the congruence subgroup Γ. A key fact in the theory of modular forms is that the spaces$M _ { k } ( \Gamma )$are finite dimensional.

We consider several examples of modular forms. For an even integer$k \geq 4$we define the weight k Eisenstein series as

$$
E _ {k} (z) := \frac {1}{2 \zeta (k)} \sum_ {(c, d) \in \mathbb {Z} ^ {2} \backslash (0, 0)} (c z + d) ^ {- k}.\tag{9}
$$

Since the sum converges absolutely, it is easy to see that$E _ { k } \in M _ { k } ( \Gamma ( 1 ) )$. The Eisenstein series possesses the Fourier expansion

$$
E _ {k} (z) = 1 + \frac {2}{\zeta (1 - k)} \sum_ {n = 1} ^ {\infty} \sigma_ {k - 1} (n) e ^ {2 \pi i n z},\tag{10}
$$

where$\begin{array} { r } { \sigma _ { k - 1 } ( n ) = \sum _ { d \mid n } d ^ { k - 1 } } \end{array}$. In particular, we have

$$
\begin{array}{l} {E _ {4} (z) = 1 + 2 4 0 \sum_ {n = 1} ^ {\infty} \sigma_ {3} (n) e ^ {2 \pi i n z},} \\ {E _ {6} (z) = 1 - 5 0 4 \sum_ {n = 1} ^ {\infty} \sigma_ {5} (n) e ^ {2 \pi i n z}.} \end{array}
$$

The infinite sum (9) does not converge absolutely for$k \ = \ 2$. On the other hand, the expression (10) converges to a holomorphic function on the upper half-plane and therefore we set

$$
E _ {2} (z) := 1 - 2 4 \sum_ {n = 1} ^ {\infty} \sigma_ {1} (n) e ^ {2 \pi i n z}.\tag{11}
$$

This function is not modular, but it satisfies

$$
z ^ {- 2} E _ {2} \Big (\frac {- 1}{z} \Big) = E _ {2} (z) - \frac {6 i}{\pi} \frac {1}{z}.\tag{12}
$$

The proof of this identity can be found in [20, Section 2.3]. The weight two Eisenstein series$E _ { 2 }$is an example of a quasimodular form [20, Section 5.1].

Another example of modular forms we consider are theta functions [20, Section 3.1]. We define three theta functions (so-called “Thetanullwerte”) as

$$
\begin{array}{l} \theta_ {0 0} (z) = \sum_ {n \in \mathbb {Z}} e ^ {\pi i n ^ {2} z}, \\ \theta_ {0 1} (z) = \sum_ {n \in \mathbb {Z}} (- 1) ^ {n} e ^ {\pi i n ^ {2} z}, \\ \theta_ {1 0} (z) = \sum_ {n \in \mathbb {Z}} e ^ {\pi i (n + \frac {1}{2}) ^ {2} z}. \end{array}
$$

The group$\Gamma ( 1 )$is generated by the elements$\begin{array} { r } { T = \left( \begin{array} { l } { 1 } \\ { 0 } \end{array} \frac { 1 } { 1 } \right) } \end{array}$and$S = \left( \begin{array} { c } { { 0 } } \\ { { - 1 0 } } \end{array} \right)$. These elements act on the fourth powers of the theta functions in the following way

$$
z ^ {- 2} \theta_ {0 0} ^ {4} \Big (\frac {- 1}{z} \Big) = - \theta_ {0 0} ^ {4} (z),\tag{13}
$$

$$
z ^ {- 2} \theta_ {0 1} ^ {4} \Big (\frac {- 1}{z} \Big) = - \theta_ {1 0} ^ {4} (z),\tag{14}
$$

$$
z ^ {- 2} \theta_ {1 0} ^ {4} \Big (\frac {- 1}{z} \Big) = - \theta_ {0 1} ^ {4} (z),\tag{15}
$$

and

$$
\theta_ {0 0} ^ {4} (z + 1) = \theta_ {0 1} ^ {4} (z),
$$

$$
\theta_ {0 1} ^ {4} (z + 1) = \theta_ {0 0} ^ {4} (z),\tag{16}
$$

(17)

$$
\theta_ {1 0} ^ {4} (z + 1) = - \theta_ {1 0} ^ {4} (z).\tag{18}
$$

Moreover, these three theta functions satisfy the Jacobi identity

$$
\theta_ {0 1} ^ {4} + \theta_ {1 0} ^ {4} = \theta_ {0 0} ^ {4}.\tag{19}
$$

The theta functions$\theta _ { 0 0 } ^ { 4 } , \theta _ { 0 1 } ^ { 4 }$, and$\theta _ { 1 0 } ^ { 4 }$belong to$M _ { 2 } ( \Gamma ( 2 ) )$

A weakly-holomorphic modular form of integer weight k and congruence subgroup Γ is a holomorphic function$f : \mathbb { H } \to \mathbb { C }$such that:

1.$f | _ { k } \gamma = f$for all$\gamma \in \Gamma$

2. for each$\alpha \in \Gamma ( 1 )$the function$f | _ { k } \alpha$has Fourier expansion

$$
f | _ {k} \alpha (z) = \sum_ {n = n _ {0}} ^ {\infty} c _ {f} (\alpha , \frac {n}{n _ {\alpha}}) e ^ {2 \pi i \frac {n}{n _ {\alpha}} z}
$$

for some$n _ { 0 } \in \mathbb { Z }$and$n _ { \alpha } \in \mathbb { N }$

For an m-periodic holomorphic function f and$\textstyle n \in { \frac { 1 } { m } } \mathbb { Z }$we will denote the n-th Fourier coeficient of f by$c _ { f } ( n )$so that

$$
f (z) = \sum_ {n \in \frac {1}{m} \mathbb {Z}} c _ {f} (n) e ^ {2 \pi i n z}.
$$

We denote the space of weakly-holomorphic modular forms of weight k and group Γ by $M _ { k } ^ { ! } ( \Gamma )$. The spaces$M _ { k } ^ { ! } ( \Gamma )$are infinite dimensional. Probably the most famous weaklyholomorphic modular form is the elliptic j-invariant

$$
j := \frac {1 7 2 8 E _ {4} ^ {3}}{E _ {4} ^ {3} - E _ {6} ^ {2}}.
$$

This function belongs to$M _ { 0 } ^ { ! } ( \Gamma ( 1 ) )$and has the Fourier expansion

$$
j (z) = q ^ {- 1} + 7 4 4 + 1 9 6 8 8 4 q + 2 1 4 9 3 7 6 0 q ^ {2} + 8 6 4 2 9 9 9 7 0 q ^ {3} + 2 0 2 4 5 8 5 6 2 5 6 q ^ {4} + O (q ^ {5})
$$

where$q = e ^ { 2 \pi i z }$. Using a simple computer algebra system such as PARI GP or Mathematica one can compute the first hundred terms of this Fourier expansion within a few seconds. An important question is to find an asymptotic formula for$c _ { j } ( n )$, the n-th Fourier coeficient of$j$. Using the Hardy-Ramanujan circle method [17, p. 460 – 461] or the non-holomorphic Poincaré series [15] one can show that

$$
c _ {j} (n) = \frac {2 \pi}{\sqrt {n}} \sum_ {k = 1} ^ {\infty} \frac {A _ {k} (n)}{k} I _ {1} \left(\frac {4 \pi \sqrt {n}}{k}\right) \qquad n \in \mathbb {Z} _ {> 0}\tag{20}
$$

where

$$
A_{k}(n) = \sum_{\substack{h\bmod k\\ (h,k) = 1}}e^{\frac{-2\pi i}{k} (nh + h^{\prime})},\quad hh^{\prime}\equiv -1(\bmod k),
$$

and$I _ { \alpha } ( x )$denotes the modified Bessel function of the first kind defined as in [1, Section$9 . 6 ]$. A similar convergent asymptotic expansion holds for the Fourier coeficients of any weakly holomorphic modular form [12, p.660 – 662], [3, Propositions 1.10 and 1.12]. Such a convergent expansion implies efective estimates for the Fourier coeficients.

For a comprehensive introduction to the theory of modular forms we refer the reader to [20] and [9].

## 4 Fourier eigenfunctions with double zeroes at lattice points

In this section we construct two radial Schwartz functions$a , b : \mathbb { R } ^ { 8 } \to i \mathbb { R }$ such that

$$
\mathcal {F} (a) = a\tag{21}
$$

$$
\mathcal {F} (b) = - b\tag{22}
$$

which have double zeroes at all$\Lambda _ { 8 }$-vectors of length greater than${ \sqrt { 2 } }$. Recall that each vector of$\Lambda _ { 8 }$ has length$\sqrt { 2 n }$ for some$n \in \mathbb { N } _ { \geq 0 }$. We define a and b so that their values are purely imaginary because this simplifies some of our computations. We will show in Section 5 that an appropriate linear combination of functions a and b satisfies conditions (3)–(5).

First, we will define the function a. To this end we consider the following weakly holomorphic modular forms:

$$
\varphi_ {- 2} := \frac {- 1 7 2 8 E _ {4} E _ {6}}{E _ {4} ^ {3} - E _ {6} ^ {2}},\tag{23}
$$

$$
\varphi_ {- 4} := \frac {1 7 2 8 E _ {4} ^ {2}}{E _ {4} ^ {3} - E _ {6} ^ {2}}.\tag{24}
$$

The modular form$E _ { 4 } ^ { 3 } - E _ { 6 } ^ { 2 }$does not vanish in the upper half-plane, hence$\varphi _ { - 2 }$and$\varphi _ { - 4 }$ have no poles in H. Analogously to (20), the Fourier coeficients of$\varphi _ { - 2 }$and$\varphi _ { - 4 }$satisfy

$$
c _ {\varphi_ {\kappa}} (n) = 2 \pi n ^ {\frac {\kappa - 1}{2}} \sum_ {k = 1} ^ {\infty} \frac {A _ {k} (n)}{k} I _ {1 - \kappa} \left(\frac {4 \pi \sqrt {n}}{k}\right) \qquad n \in \mathbb {Z} _ {> 0}, \kappa = - 2, - 4.\tag{25}
$$

We define

$$
\phi_ {- 4} := \varphi_ {- 4},\tag{26}
$$

$$
\phi_ {- 2} := \varphi_ {- 4} E _ {2} + \varphi_ {- 2},\tag{27}
$$

$$
\phi_ {0} := \varphi_ {- 4} E _ {2} ^ {2} + 2 \varphi_ {- 2} E _ {2} + j - 1 7 2 8.\tag{28}
$$

The function$\phi _ { 0 } ( z )$is not modular; however the identity (12) implies the following transformation rule:

$$
\phi_ {0} \left(\frac {- 1}{z}\right) = \phi_ {0} (z) - \frac {1 2 i}{\pi} \frac {1}{z} \phi_ {- 2} (z) - \frac {3 6}{\pi^ {2}} \frac {1}{z ^ {2}} \phi_ {- 4} (z).\tag{29}
$$

Moreover, we have

$$
\phi_ {- 2} = - 3 D (\varphi_ {- 4}) + 3 \varphi_ {- 2},\tag{30}
$$

$$
\phi_ {0} = 1 2 D ^ {2} (\varphi_ {- 4}) - 3 6 D (\varphi_ {- 2}) + 2 4 j - 1 7 8 5 6,\tag{31}
$$

where${ \begin{array} { r } { D f ( z ) = { \frac { 1 } { 2 \pi i } } { \frac { d } { d z } } f ( z ) } \end{array} }$. These identities combined with (20) and (25) give the asymptotic formula for the Fourier coeficients$c _ { \phi _ { - 4 } } ( n ) , c _ { \phi _ { - 2 } } ( n )$, and$c _ { \phi _ { 0 } } ( n )$. The first several terms of the corresponding Fourier expansions are

$$
\phi_ {- 4} (z) = q ^ {- 1} + 5 0 4 + 7 3 7 6 4 q + 2 6 9 5 0 4 0 q ^ {2} + 5 4 7 5 5 7 3 0 q ^ {3} + O \left(q ^ {4}\right),\tag{32}
$$

$$
\phi_ {- 2} (z) = 7 2 0 + 2 0 3 0 4 0 q + 9 4 1 7 6 0 0 q ^ {2} + 2 2 3 4 7 3 6 0 0 q ^ {3} + 3 5 6 6 7 8 2 0 8 0 q ^ {4} + O \left(q ^ {5}\right),\tag{33}
$$

$$
\phi_ {0} (z) = 5 1 8 4 0 0 q + 3 1 1 0 4 0 0 0 q ^ {2} + 8 7 0 9 1 2 0 0 0 q ^ {3} + 1 5 6 9 7 1 5 2 0 0 0 q ^ {4} + O \left(q ^ {5}\right),\tag{34}
$$

where$q = e ^ { 2 \pi i z }$. For$x \in \mathbb { R } ^ { 8 }$we define

$$
\begin{array}{l} a (x) := \int_ {- 1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z + 1} \Big) (z + 1) ^ {2} e ^ {\pi i \| x \| ^ {2} z} d z + \int_ {1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z - 1} \Big) (z - 1) ^ {2} e ^ {\pi i \| x \| ^ {2} z} d z \\ - 2 \int_ {0} ^ {i} \phi_ {0} \Big (\frac {- 1}{z} \Big) z ^ {2} e ^ {\pi i \| x \| ^ {2} z} d z + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i \| x \| ^ {2} z} d z. \end{array}\tag{35}
$$

We observe that the contour integrals in (35) converge absolutely and uniformly for $x \in \mathbb { R } ^ { 8 }$. Indeed,$\phi _ { 0 } ( z ) = O ( e ^ { - 2 \pi i z } )$as Im$( z ) \to \infty$. Therefore,$a ( x )$is well defined. Now we prove that a satisfies condition (21).

Proposition 1. The function a defined by (35) belongs to the Schwartz space and satisfies

$$
\widehat {a} (x) = a (x).
$$

Proof. First, we prove that a is a Schwartz function. From (20), (25), and (31) we deduce that the Fourier coeficients of$\phi _ { 0 }$satisfy

$$
| c _ {\phi_ {0}} (n) | \leq 2 e ^ {4 \pi \sqrt {n}} n \in \mathbb {Z} _ {> 0}.
$$

Thus, there exists a positive constant$C$such that

$$
| \phi_ {0} (z) | \leq C e ^ {- 2 \pi \mathrm{Im} z} \quad \text { for } \mathrm{Im} z > \frac {1}{2}.
$$

We estimate the first summand in the right-hand side of (35). For$r \in \mathbb { R } _ { \geq 0 }$we have

$$
\left| \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z \right| = \left| \int_ {i \infty} ^ {- 1 / (i + 1)} \phi_ {0} (z) z ^ {- 4} e ^ {\pi i r ^ {2} (- 1 / z - 1)} d z \right| \leq
$$

$$
C _ {1} \int_ {1 / 2} ^ {\infty} e ^ {- 2 \pi t} e ^ {- \pi r ^ {2} / t} d t \leq C _ {1} \int_ {0} ^ {\infty} e ^ {- 2 \pi t} e ^ {- \pi r ^ {2} / t} d t = C _ {2} r K _ {1} (2 \sqrt {2} \pi r)
$$

where$C _ { 1 }$and$C _ { 2 }$are some positive constants and$K _ { \alpha } ( x )$is the modified Bessel function of the second kind defined as in [1, Section 9.6]. This estimate also holds for the second and third summand in (35). For the last summand we have

$$
\left| \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i r ^ {2} z} d z \right| \leq C \int_ {1} ^ {\infty} e ^ {- 2 \pi t} e ^ {- \pi r ^ {2} t} d t = C _ {3} \frac {e ^ {\pi (r ^ {2} + 2)}}{r ^ {2} + 2}.
$$

Therefore, we arrive at

$$
| a (r) | \leq 4 C _ {2} r K _ {1} (2 \sqrt {2} \pi r) + 2 C _ {3} \frac {e ^ {- \pi (r ^ {2} + 2)}}{r ^ {2} + 2}.
$$

It is easy to see that the left hand side of this inequality decays faster then any inverse power of r. Analogous estimates can be obtained for all derivatives$\textstyle { \frac { d ^ { k } } { d r ^ { k } } } a ( r )$

Now we show that a is an eigenfunction of the Fourier transform. We recall that the Fourier transform of a Gaussian function is

$$
\mathcal {F} (e ^ {\pi i \| x \| ^ {2} z}) (y) = z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})}.\tag{36}
$$

Next, we exchange the contour integration with respect to z variable and Fourier transform with respect to x variable in (35). This can be done, since the corresponding double integral converges absolutely. In this way we obtain

$$
\begin{array}{l} \widehat {a} (y) = \int_ {- 1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z + 1} \Big) (z + 1) ^ {2} z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z + \int_ {1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z - 1} \Big) (z - 1) ^ {2} z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z \\ - 2 \int_ {0} ^ {i} \phi_ {0} \Big (\frac {- 1}{z} \Big) z ^ {2} z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z. \end{array}
$$

Now we make a change of variables$\begin{array} { r } { w = \frac { - 1 } { z } } \end{array}$. We obtain

$$
\begin{array}{l} \widehat {a} (y) = \int_ {1} ^ {i} \phi_ {0} \Big (1 - \frac {1}{w - 1} \Big) (\frac {- 1}{w} + 1) ^ {2} w ^ {2} e ^ {\pi i \| y \| ^ {2} w} d w \\ \qquad + \int_ {- 1} ^ {i} \phi_ {0} \Big (1 - \frac {1}{w + 1} \Big) (\frac {- 1}{w} - 1) ^ {2} w ^ {2} e ^ {\pi i \| y \| ^ {2} w} d w \\ \qquad - 2 \int_ {i \infty} ^ {i} \phi_ {0} (w) e ^ {\pi i \| y \| ^ {2} w} d w + 2 \int_ {i} ^ {0} \phi_ {0} \Big (\frac {- 1}{w} \Big) w ^ {2} e ^ {\pi i \| y \| ^ {2} w} d w. \end{array}
$$

Since$\phi _ { 0 }$is 1-periodic we have

$$
\begin{array}{l} \widehat {a} (y) = \int_ {1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z - 1} \Big) (z - 1) ^ {2} e ^ {\pi i \| y \| ^ {2} z} d z + \int_ {- 1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z + 1} \Big) (z + 1) ^ {2} e ^ {\pi i \| y \| ^ {2} z} d z \\ \qquad + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i \| y \| ^ {2} z} d z - 2 \int_ {0} ^ {i} \phi_ {0} \Big (\frac {- 1}{z} \Big) z ^ {2} e ^ {\pi i \| y \| ^ {2} z} d z \\ \qquad = a (y). \end{array}
$$

This finishes the proof of the proposition.

Next, we check that a has double zeroes at all Λ -lattice points of length greater then $\sqrt { 2 }$

Proposition 2. For$r > { \sqrt { 2 } }$we can express$a ( r )$in the following form

$$
a (r) = - 4 \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z.\tag{37}
$$

Proof. We denote the right hand side of (37) by$d ( r )$. It is easy to see that$d ( r )$is welldefined. Indeed, from the transformation formula (29) and the expansions (34)–(32) we obtain

$$
\begin{array}{r l} & {\phi_ {0} \Big (\frac {- 1}{i t} \Big) = O (e ^ {- 2 \pi / t}) \quad \mathrm{as} t \to 0} \\ & {\phi_ {0} \Big (\frac {- 1}{i t} \Big) = O (t ^ {- 2} e ^ {2 \pi t}) \quad \mathrm{as} t \to \infty} \end{array}
$$

Hence, the integral (37) converges absolutely for$r > { \sqrt { 2 } }$. We can write

$$
\begin{array}{l} d (r) = \int_ {- 1} ^ {i \infty - 1} \phi_ {0} \Big (\frac {- 1}{z + 1} \Big) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i \infty} \phi_ {0} \Big (\frac {- 1}{z} \Big) z ^ {2} e ^ {\pi i r ^ {2} z} d z \\ + \int_ {1} ^ {i \infty + 1} \phi_ {0} \Big (\frac {- 1}{z - 1} \Big) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z. \end{array}
$$

From (29) we deduce that if$r > { \sqrt { 2 } }$then$\phi _ { 0 } \left( { \textstyle { \frac { - 1 } { z } } } \right) z ^ { 2 } e ^ { \pi i r ^ { 2 } z } \to 0$as Im$( z ) \to \infty$. Therefore, we can deform the paths of integration and rewrite

$$
\begin{array}{l} d (r) = \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z \\ - 2 \int_ {0} ^ {i} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {i} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z \\ + \int_ {1} ^ {i} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z. \end{array}
$$

Now from (29) we find

$$
\begin{array}{r l} & {\phi_ {0} \Big (\frac {- 1}{z + 1} \Big) (z + 1) ^ {2} - 2 \phi_ {0} \Big (\frac {- 1}{z} \Big) z ^ {2} + \phi_ {0} \Big (\frac {- 1}{z - 1} \Big) (z - 1) ^ {2} =} \\ & {\phi_ {0} (z + 1) (z + 1) ^ {2} - 2 \phi_ {0} (z) z ^ {2} + \phi_ {0} (z - 1) (z - 1) ^ {2}} \\ & {- \frac {1 2 i}{\pi} \Big (\phi_ {- 2} (z + 1) (z + 1) - 2 \phi_ {- 2} (z) z + \phi_ {- 2} (z - 1) (z - 1) \Big)} \\ & {- \frac {3 6}{\pi^ {2}} \Big (\phi_ {- 4} (z + 1) - 2 \phi_ {- 4} (z) + \phi_ {- 4} (z - 1) \Big) =} \\ & {2 \phi_ {0} (z).} \end{array}
$$

Thus, we obtain

$$
\begin{array}{l} d (r) = \int_ {- 1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z + 1} \Big) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i} \phi_ {0} \Big (\frac {- 1}{z} \Big) z ^ {2} e ^ {\pi i r ^ {2} z} d z \\ + \int_ {1} ^ {i} \phi_ {0} \Big (\frac {- 1}{z - 1} \Big) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i r ^ {2} z} d z = a (r). \end{array}
$$

This finishes the proof.

Finally, we find another convenient integral representation for a and compute values of$a ( r )$at$r = 0$and$r = { \sqrt { 2 } }$

Proposition 3. For$r \geq 0$we have

$$
\begin{array}{l} a (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \left(\frac {3 6}{\pi^ {3} (r ^ {2} - 2)} - \frac {8 6 4 0}{\pi^ {3} r ^ {4}} + \frac {1 8 1 4 4}{\pi^ {3} r ^ {2}} \right. \\ \left. + \int_ {0} ^ {\infty} \left(t ^ {2} \phi_ {0} \left(\frac {i}{t}\right) - \frac {3 6}{\pi^ {2}} e ^ {2 \pi t} + \frac {8 6 4 0}{\pi} t - \frac {1 8 1 4 4}{\pi^ {2}}\right) e ^ {- \pi r ^ {2} t} d t\right). \end{array}\tag{38}
$$

The integral converges absolutely for all$r \in \mathbb { R } _ { \geq 0 }$

Proof. Suppose that$r > { \sqrt { 2 } } .$. Then by Proposition 2

$$
a (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} \phi_ {0} (i / t) t ^ {2} e ^ {- \pi r ^ {2} t} d t.
$$

From (34)–(29) we obtain

$$
\phi_ {0} (i / t) t ^ {2} = \frac {3 6}{\pi^ {2}} e ^ {2 \pi t} - \frac {8 6 4 0}{\pi} t + \frac {1 8 1 4 4}{\pi^ {2}} + O (t ^ {2} e ^ {- 2 \pi t}) \quad \mathrm{as} t \to \infty .\tag{39}
$$

For$r > { \sqrt { 2 } }$we have

$$
\int_ {0} ^ {\infty} \left(\frac {3 6}{\pi^ {2}} e ^ {2 \pi t} + \frac {8 6 4 0}{\pi} t + \frac {1 8 1 4 4}{\pi^ {2}}\right) e ^ {- \pi r ^ {2} t} d t = \frac {3 6}{\pi^ {3} (r ^ {2} - 2)} - \frac {8 6 4 0}{\pi^ {3} r ^ {4}} + \frac {1 8 1 4 4}{\pi^ {3} r ^ {2}}.\tag{40}
$$

Therefore, the identity (38) holds for$r > { \sqrt { 2 } }$.

On the other hand, from the definition (35) we see that$a ( r )$is analytic in some neighborhood of$[ 0 , \infty )$. The asymptotic expansion (39) implies that the right hand side of (38) is also analytic in some neighborhood of$[ 0 , \infty )$. Hence, the identity (38) holds on the whole interval$[ 0 , \infty )$. This finishes the proof of the proposition.□

From the identity (38) we see that the values$a ( r )$are in iR for all$r \in \mathbb { R } _ { \geq 0 }$. In particular, we have

Proposition 4. We have

$$
a (0) = \frac {- i 8 6 4 0}{\pi} \qquad a (\sqrt {2}) = 0 \qquad a ^ {\prime} (\sqrt {2}) = \frac {i 7 2 \sqrt {2}}{\pi}.\tag{41}
$$

Proof. These identities follow immediately from the previous proposition.

Now we construct function b. To this end we consider the modular form

$$
h := 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {0 1} ^ {4}}{\theta_ {1 0} ^ {8}}.\tag{42}
$$

It is easy to see that$h \in M _ { - 2 } ^ { ! } ( \Gamma _ { 0 } ( 2 ) )$. Indeed, first we check that$h | _ { - 2 \gamma } = h$for all $\gamma \in \Gamma _ { 0 } ( 2 )$. Since the group$\Gamma _ { 0 } ( 2 )$is generated by elements$\left( \begin{array} { l l } { 1 } & { 0 } \\ { 2 } & { 1 } \end{array} \right)$and$\textstyle { \binom { 1 } { 0 } } { \frac { 1 } { 1 } } \dotsc$it sufices to check that h is invariant under their action. This follows immediately from (13)–(18) and (42). Next we analyze the poles of h. It is known [14, Chapter I Lemma 4.1] that $\theta _ { 1 0 }$has no zeros in the upper-half plane and hence h has poles only at the cusps. At the cusp i∞ this modular form has the Fourier expansion

$$
h (z) = q ^ {- 1} + 1 6 - 1 3 2 q + 6 4 0 q ^ {2} - 2 5 5 0 q ^ {3} + O \left(q ^ {4}\right).
$$

Let$I = { \bigl ( } { } _ { 0 } ^ { 1 } _ { 1 } ^ { 0 } { \bigr ) } , T = { \bigl ( } { } _ { 0 } ^ { 1 } _ { 1 } ^ { 1 } { \bigr ) }$, and$\begin{array} { r } { S = \left( \begin{array} { l l } { 0 } & { - 1 } \\ { 1 } & { 0 } \end{array} \right) } \end{array}$be elements of$\Gamma ( 1 )$. We define the following three functions

$$
\psi_ {I} := h - h | _ {- 2} S T,\tag{43}
$$

$$
\psi_ {T} := \psi_ {I} | _ {- 2} T,\tag{44}
$$

$$
\psi_ {S} := \psi_ {I} | _ {- 2} S.\tag{45}
$$

More explicitly, we have

$$
\psi_ {I} = 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {0 1} ^ {4}}{\theta_ {1 0} ^ {8}} + 1 2 8 \frac {\theta_ {0 1} ^ {4} - \theta_ {1 0} ^ {4}}{\theta_ {0 0} ^ {8}},\tag{46}
$$

$$
\psi_ {T} = 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {0 1} ^ {4}}{\theta_ {1 0} ^ {8}} + 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {1 0} ^ {4}}{\theta_ {0 1} ^ {8}},
$$

(47)

$$
\psi_ {S} = - 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {1 0} ^ {4}}{\theta_ {0 1} ^ {8}} - 1 2 8 \frac {\theta_ {1 0} ^ {4} - \theta_ {0 1} ^ {4}}{\theta_ {0 0} ^ {8}}.\tag{48}
$$

The Fourier expansions of these functions are

$$
\psi_ {I} (z) = q ^ {- 1} + 1 4 4 - 5 1 2 0 q ^ {1 / 2} + 7 0 5 2 4 q - 6 2 6 6 8 8 q ^ {3 / 2} + 4 2 6 5 6 0 0 q ^ {2} + O \left(q ^ {5 / 2}\right),\tag{49}
$$

$$
\psi_ {T} (z) = q ^ {- 1} + 1 4 4 + 5 1 2 0 q ^ {1 / 2} + 7 0 5 2 4 q + 6 2 6 6 8 8 q ^ {3 / 2} + 4 2 6 5 6 0 0 q ^ {2} + O \left(q ^ {5 / 2}\right),\tag{50}
$$

$$
\psi_ {S} (z) = - 1 0 2 4 0 q ^ {1 / 2} - 1 2 5 3 3 7 6 q ^ {3 / 2} - 4 8 3 2 8 7 0 4 q ^ {5 / 2} - 1 0 5 9 0 7 8 1 4 4 q ^ {7 / 2} + O \left(q ^ {9 / 2}\right).\tag{51}
$$

For$x \in \mathbb { R } ^ { 8 }$define

$$
\begin{array}{l} b (x) := \int_ {- 1} ^ {i} \psi_ {T} (z)   e ^ {\pi i \| x \| ^ {2} z}   d z + \int_ {1} ^ {i} \psi_ {T} (z)   e ^ {\pi i \| x \| ^ {2} z}   d z \\ - 2 \int_ {0} ^ {i} \psi_ {I} (z)   e ^ {\pi i \| x \| ^ {2} z}   d z - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z)   e ^ {\pi i \| x \| ^ {2} z}   d z. \end{array}\tag{52}
$$

Now we prove that b satisfies condition (22).

Proposition 5. The function b defined by (52) belongs to the Schwartz space and satisfies

$$
\widehat {b} (x) = - b (x).
$$

Proof. Here, we repeat the arguments used in the proof of Proposition 1. First we show that b is a Schwartz function. We have

$$
\begin{array}{l} \int_ {- 1} ^ {i} \psi_ {T} (z)   e ^ {\pi i r ^ {2} z}   d z = \int_ {0} ^ {i + 1} \psi_ {I} (z)   e ^ {\pi i r ^ {2} (z - 1)}   d z = \\ \int_ {i \infty} ^ {- 1 / (i + 1)} \psi_ {I} \Big (\frac {- 1}{z} \Big)   e ^ {\pi i r ^ {2} (- 1 / z - 1)}   z ^ {- 2}   d z = \int_ {i \infty} ^ {- 1 / (i + 1)} \psi_ {S} (z)   z ^ {- 4}   e ^ {\pi i r ^ {2} (- 1 / z - 1)}   d z. \end{array}
$$

There exists a positive constant$C$such that

$$
| \psi_ {S} (z) | \leq C e ^ {- \pi \operatorname{Im} z} \quad \mathrm{for} \operatorname{Im} z > \frac {1}{2}.
$$

Thus, as in the proof of Proposition 1 we estimate the first summand in the left-hand side of (52)

$$
\left| \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z \right| \leq C _ {1} r K _ {1} (2 \pi r).
$$

We combine this inequality with analogous estimates for the other three summands and obtain

$$
| b (r) | \leq C _ {2} r K _ {1} (2 \pi r) + C _ {3} \frac {e ^ {- \pi (r ^ {2} + 1)}}{r ^ {2} + 1}.
$$

Here$C _ { 1 } , C _ { 2 }$, and$C _ { 3 }$are some positive constants. Similar estimates hold for all derivatives$\begin{array} { r } { \frac { d ^ { k } } { d ^ { k } r } b ( r ) } \end{array}$

Now we prove that b is an eigenfunction of the Fourier transform. We use identity (36) and interchange contour integration in z and Fourier transform in x. Thus we obtain

$$
\begin{array}{l} \mathcal {F} (b) (x) = \int_ {- 1} ^ {i} \psi_ {T} (z)   z ^ {- 4}   e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})}   d z + \int_ {1} ^ {i} \psi_ {T} (z)   z ^ {- 4}   e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})}   d z \\ - 2 \int_ {0} ^ {i} \psi_ {I} (z)   z ^ {- 4}   e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})}   d z - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z)   z ^ {- 4}   e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})}   d z. \end{array}
$$

We make the change of variables$\begin{array} { r } { w = \frac { - 1 } { z } } \end{array}$and arrive at

$$
\begin{array}{l} \mathcal {F} (b) (x) = \int_ {1} ^ {i} \psi_ {T} \Big (\frac {- 1}{w} \Big)   w ^ {2}   e ^ {\pi i \| x \| ^ {2} w}   d w + \int_ {- 1} ^ {i} \psi_ {T} \Big (\frac {- 1}{w} \Big)   w ^ {2}   e ^ {\pi i \| x \| ^ {2} w}   d w \\ - 2 \int_ {i \infty} ^ {i} \psi_ {I} \Big (\frac {- 1}{w} \Big)   w ^ {2}   e ^ {\pi i \| x \| ^ {2} w}   d w - 2 \int_ {i} ^ {0} \psi_ {S} \Big (\frac {- 1}{w} \Big)   w ^ {2}   e ^ {\pi i \| x \| ^ {2} w}   d w. \end{array}
$$

Now we observe that the definitions (43)–(45) imply

$$
\begin{array}{r l} & {\psi_ {T} | _ {- 2} S = - \psi_ {T},} \\ & {\psi_ {I} | _ {- 2} S = \psi_ {S},} \\ & {\psi_ {S} | _ {- 2} S = \psi_ {I}.} \end{array}
$$

Therefore, we arrive at

$$
\begin{array}{l} \mathcal {F} (b) (x) = \int_ {1} ^ {i} - \psi_ {T} (z) e ^ {\pi i \| x \| ^ {2} z} d z + \int_ {- 1} ^ {i} - \psi_ {T} (z) e ^ {\pi i \| x \| ^ {2} z} d z \\ \qquad + 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) e ^ {\pi i \| x \| ^ {2} z} d z + 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i \| x \| ^ {2} w} d w. \end{array}
$$

Now from (52) we see that

$$
\mathcal {F} (b) (x) = - b (x).
$$

Now we regard the radial function b as a function on$\mathbb { R } _ { > 0 }$. We check that b has double roots at$\Lambda _ { 8 }$-points

Proposition 6. For$r > { \sqrt { 2 } }$function$b ( r )$can be expressed as

$$
b (r) = - 4 \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {i \infty} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z.\tag{53}
$$

Proof. We denote the right hand side of (53) by$c ( r )$. First, we check that$c ( r )$is well-defined. We have

$$
\begin{array}{r} \psi_ {I} (i t) = O (t ^ {2} e ^ {- \pi / t}) \quad \mathrm{as} t \to 0, \\ \psi_ {I} (i t) = O (e ^ {2 \pi t}) \quad \mathrm{as} t \to \infty . \end{array}
$$

Therefore, the integral (53) converges for$r > \sqrt { 2 }$. Then we rewrite it in the following way:

$$
c (r) = \int_ {- 1} ^ {i \infty - 1} \psi_ {I} (z + 1) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i \infty} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {1} ^ {i \infty + 1} \psi_ {I} (z - 1) e ^ {\pi i r ^ {2} z} d z.
$$

From the Fourier expansion (49) we know that$\psi _ { I } ( z ) = e ^ { - 2 \pi i z } + O ( 1 )$as Im$( z ) \to \infty$ By assumption$r ^ { 2 } > 2$, hence we can deform the path of integration and write

$$
\int_ {- 1} ^ {i \infty - 1} \psi_ {I} (z + 1) e ^ {\pi i r ^ {2} z} d z = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z,\tag{54}
$$

$$
\int_ {1} ^ {i \infty + 1} \psi_ {I} (z - 1) e ^ {\pi i r ^ {2} z} d z = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z.\tag{55}
$$

We have

$$
\begin{array}{l} c (r) = \int_ {- 1} ^ {i} \psi_ {T} (z)   e ^ {\pi i r ^ {2} z}   d z + \int_ {1} ^ {i} \psi_ {T} (z)   e ^ {\pi i r ^ {2} z}   d z - 2 \int_ {0} ^ {i} \psi_ {I} (z)   e ^ {\pi i r ^ {2} z}   d z \\ \qquad + 2 \int_ {i} ^ {i \infty} (\psi_ {T} (z) - \psi_ {I} (z))   e ^ {\pi i r ^ {2} z}   d z. \end{array}\tag{56}
$$

Next, we check that the functions$\psi _ { I } , \psi _ { T }$, and$\psi _ { S }$satisfy the following identity:

$$
\psi_ {T} + \psi_ {S} = \psi_ {I}.\tag{57}
$$

Indeed, from definitions (43)-(45) we get

$$
\begin{array}{c} \psi_ {T} + \psi_ {S} = (h - h | _ {- 2} S T) | _ {- 2} T + (h - h | _ {- 2} S T) | _ {- 2} S \\ = h | _ {- 2} T - h | _ {- 2} S T ^ {2} + h | _ {- 2} S - h | _ {- 2} S T S. \end{array}
$$

Note that$S T ^ { 2 } S$belongs to$\Gamma _ { 0 } ( 2 )$. Thus, since$h \in M _ { - 2 } ^ { ! } \Gamma _ { 0 } ( 2 )$we get

$$
\psi_ {T} + \psi_ {S} = h | _ {- 2} T - h | _ {- 2} S T S.
$$

Now we observe that$T$and$S T S ( S T ) ^ { - 1 }$are also in$\Gamma _ { 0 } ( 2 )$. Therefore,

$$
\psi_ {T} + \psi_ {S} = h | _ {- 2} T - h | _ {- 2} S T S = h - h | _ {- 2} S T = \psi_ {I}.
$$

Combining (56) and (57) we find

$$
\begin{array}{l} c (r) = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z \\ \qquad - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) e ^ {\pi i r ^ {2} z} d z \\ \qquad = b (r). \end{array}
$$

At the end of this section we find another integral representation of$b ( r )$for$r \in \mathbb { R } _ { \geq 0 }$ and compute special values of b.

Proposition 7. For$r \geq 0$we have

$$
b (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \left(\frac {1 4 4}{\pi r ^ {2}} + \frac {1}{\pi (r ^ {2} - 2)} + \int_ {0} ^ {\infty} \left(\psi_ {I} (i t) - 1 4 4 - e ^ {2 \pi t}\right) e ^ {- \pi r ^ {2} t} d t\right).\tag{58}
$$

The integral converges absolutely for all$r \in \mathbb { R } _ { \geq 0 }$

Proof. The proof is analogous to the proof of Proposition 3. First, suppose that$r > { \sqrt { 2 } }$ Then by Proposition 6

$$
b (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} \psi_ {I} (i t) e ^ {- \pi r ^ {2} t} d t.
$$

From (49) we obtain

$$
\psi_ {I} (i t) = e ^ {2 \pi t} + 1 4 4 + O (e ^ {- \pi t}) \quad \mathrm{as} t \to \infty .\tag{59}
$$

For$r > { \sqrt { 2 } }$we have

$$
\int_ {0} ^ {\infty} \left(e ^ {2 \pi t} + 1 4 4\right) e ^ {- \pi r ^ {2} t} d t = \frac {1}{\pi (r ^ {2} - 2)} + \frac {1 4 4}{\pi r ^ {2}}.\tag{60}
$$

Therefore, the identity (38) holds for$r > { \sqrt { 2 } }$

On the other hand, from the definition (52) we see that$b ( r )$is analytic in some neighborhood of$[ 0 , \infty )$. The asymptotic expansion (59) implies that the right hand side of (58) is also analytic in some neighborhood of$[ 0 , \infty )$. Hence, the identity (58) holds on the whole interval [0, ∞). This finishes the proof of the proposition.□

We see from (58) that$b ( r ) \in i \mathbb { R }$far all$r \in \mathbb { R } _ { \geq 0 }$. Another immediate corollary of this proposition is

Proposition 8. We have

$$
b (0) = 0 \qquad b (\sqrt {2}) = 0 \qquad b ^ {\prime} (\sqrt {2}) = 2 \sqrt {2} \pi i.\tag{61}
$$

## 5 Proof of Theorem 3

Finally, we are ready to prove Theorem 3.

Theorem 4. The function

$$
g (x) := \frac {\pi i}{8 6 4 0} a (x) + \frac {i}{2 4 0 \pi} b (x)
$$

satisfies conditions (3)–(5). Moreover, the values$g ( x )$and${ \widehat { g } } ( x )$do not vanish for all vectors x with$\| x \| ^ { 2 } \notin 2 \mathbb { Z } _ { > 0 }$

Proof. First, we prove that (3) holds. By Propositions 2 and 6 we know that for$r > { \sqrt { 2 } }$

$$
g (r) = \frac {\pi}{2 1 6 0} \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} A (t) e ^ {- \pi r ^ {2} t} d t\tag{62}
$$

where

$$
A (t) = - t ^ {2} \phi_ {0} (i / t) - \frac {3 6}{\pi^ {2}} \psi_ {I} (i t).
$$

Our goal is to show that$A ( t ) < 0$for$t \in ( 0 , \infty )$. The function$A ( t )$is plotted in Figure 1.

Figure 1: Plot of the functions$A(t)$, $A _ { 0 } ^ { ( 2 ) } ( t ) = - \frac { 3 6 8 6 4 0 } { \pi ^ { 2 } } t ^ { 2 } e ^ { - \pi / t }$, and$A _ { \infty } ^ { ( 1 ) } ( t ) = - \frac { 7 2 } { \pi ^ { 2 } } e ^ { 2 \pi t } + \frac { 8 6 4 0 } { \pi } t - \frac { 2 3 3 2 8 } { \pi ^ { 2 } }$.

![](images/page_18_image_11.jpg)

We observe that we can compute the values of$A ( t )$for$t \in ( 0 , \infty )$ with any given precision. Indeed, from identities (29) and (45) we obtain the following two presentations for A(t)

$$
\begin{array}{r l} & {A (t) = - t ^ {2} \phi_ {0} (i / t) + \frac {3 6}{\pi^ {2}} t ^ {2} \psi_ {S} (i / t),} \\ & {A (t) = - t ^ {2} \phi_ {0} (i t) + \frac {1 2}{\pi} t \phi_ {- 2} (i t) - \frac {3 6}{\pi^ {2}} \phi_ {- 4} (i t) - \frac {3 6}{\pi^ {2}} \psi_ {I} (i t).} \end{array}
$$

For an integer$n \geq 0$let$A _ { 0 } ^ { ( n ) }$and$A _ { \infty } ^ { ( n ) }$be the functions such that

$$
A (t) = A _ {0} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n / t}) \quad \mathrm{as} t \to 0,\tag{63}
$$

$$
A (t) = A _ {\infty} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n t}) \quad \mathrm{as} t \to \infty .\tag{64}
$$

For each$n \geq 0$we can compute these functions from the Fourier expansions (34)–(32), (49), and (51). For example, from (32)–(34) and (49) we compute

$$
\begin{array}{r} A _ {\infty} ^ {(6)} (t) = - \frac {7 2}{\pi^ {2}} e ^ {2 \pi t} - \frac {2 3 3 2 8}{\pi^ {2}} + \frac {1 8 4 3 2 0}{\pi^ {2}} e ^ {- \pi t} - \frac {5 1 9 4 3 6 8}{\pi^ {2}} e ^ {- 2 \pi t} + \frac {2 2 5 6 0 7 6 8}{\pi^ {2}} e ^ {- 3 \pi t} - \frac {2 5 0 5 8 3 0 4 0}{\pi^ {2}} e ^ {- 4 \pi t} + \frac {8 6 9 9 1 6 6 7 2}{\pi^ {2}} e ^ {- 5 \pi t} \\ + t (\frac {8 6 4 0}{\pi} + \frac {2 4 3 6 4 8 0}{\pi} e ^ {- 2 \pi t} + \frac {1 1 3 0 1 1 2 0 0}{\pi} e ^ {- 4 \pi t}) - t ^ {2} (5 1 8 4 0 0 e ^ {- 2 \pi t} + 3 1 1 0 4 0 0 0 e ^ {- 4 \pi t}). \end{array}
$$

From (32)–(34) and (51) we compute

$$
A _ {0} ^ {(6)} (t) = t ^ {2} (- \frac {3 6 8 6 4 0}{\pi^ {2}} e ^ {- \pi / t} - 5 1 8 4 0 0 e ^ {- 2 \pi / t} - \frac {4 5 1 2 1 5 3 6}{\pi^ {2}} e ^ {- 3 \pi / t} - 3 1 1 0 4 0 0 0 e ^ {- 4 \pi / t} - \frac {1 7 3 9 8 3 3 3 4 4}{\pi^ {2}} e ^ {- 5 \pi / t}).
$$

Moreover, from the convergent asymptotic expansion for the Fourier coeficients of a weakly holomorphic modular form [3, Proposition 1.12] we find that the n-th Fourier coeficient$c _ { \psi _ { I } } ( n )$of$\psi _ { I }$satisfies

$$
| c _ {\psi_ {I}} (n) | \leq e ^ {4 \pi \sqrt {n}} \quad n \in \frac {1}{2} \mathbb {Z} _ {> 0}.\tag{65}
$$

Similar inequalities hold for the Fourier coeficients of$\psi _ { S } , \phi _ { 0 } , \phi _ { - 2 }$, and$\phi _ { - 4 } \mathrm { : }$

$$
| c _ {\psi_ {S}} (n) | \leq 2 e ^ {4 \pi \sqrt {n}} \qquad n \in \frac {1}{2} \mathbb {Z} _ {> 0},\tag{66}
$$

$$
| c _ {\phi_ {0}} (n) | \leq 2 e ^ {4 \pi \sqrt {n}} \qquad n \in \mathbb {Z} _ {> 0},\tag{67}
$$

$$
| c _ {\phi_ {- 2}} (n) | \leq e ^ {4 \pi \sqrt {n}} \qquad n \in \mathbb {Z} _ {> 0},\tag{68}
$$

$$
| c _ {\phi_ {- 4}} (n) | \leq e ^ {4 \pi \sqrt {n}} \qquad n \in \mathbb {Z} _ {> 0}.\tag{69}
$$

Therefore, we can estimate the error terms in the asymptotic expansions (63) and (64) of A(t)

$$
\left| A (t) - A _ {0} ^ {(m)} (t) \right| \leq (t ^ {2} + \frac {3 6}{\pi^ {2}}) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n / t},
$$

$$
\left| A (t) - A _ {\infty} ^ {(m)} (t) \right| \leq (t ^ {2} + \frac {1 2}{\pi} t + \frac {3 6}{\pi^ {2}}) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n t}.
$$

For an integer$m \geq 0$we set

$$
R _ {0} ^ {(m)} := (t ^ {2} + \frac {3 6}{\pi^ {2}}) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n / t},
$$

$$
R _ {\infty} ^ {(m)} := (t ^ {2} + \frac {1 2}{\pi} t + \frac {3 6}{\pi^ {2}}) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n t}.
$$

Using interval arithmetic we check that

$$
\begin{array}{l} \left| R _ {0} ^ {(6)} (t) \right| \leq \left| A _ {0} ^ {(6)} (t) \right| \quad \text { for } t \in (0, 1 ], \\ \left| R _ {\infty} ^ {(6)} (t) \right| \leq \left| A _ {\infty} ^ {(6)} (t) \right| \quad \text { for } t \in [ 1, \infty), \\ A _ {0} ^ {(6)} (t) <   0 \quad \text { for } t \in (0, 1 ], \\ A _ {\infty} ^ {(6)} (t) <   0 \quad \text { for } t \in [ 1, \infty). \end{array}
$$

Thus, we see that$A ( t ) < 0$for$t \in ( 0 , \infty )$. Then identity (62) implies (3).

Next, we prove (4). By Propositions 3 and 7 we know that for$r > 0$

$$
\widehat {g} (r) = \frac {\pi}{2 1 6 0} \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} B (t) e ^ {- \pi r ^ {2} t} d t\tag{70}
$$

where

$$
B (t) = - t ^ {2} \phi_ {0} (i / t) + \frac {3 6}{\pi^ {2}} \psi_ {I} (i t).
$$

This function can also be written as

$$
\begin{array}{r l} & B (t) = - t ^ {2} \phi_ {0} (i / t) - \frac {3 6}{\pi^ {2}} t ^ {2} \psi_ {S} (i / t), \\ & B (t) = - t ^ {2} \phi_ {0} (i t) + \frac {1 2}{\pi} t \phi_ {- 2} (i t) - \frac {3 6}{\pi^ {2}} \phi_ {- 4} (i t) + \frac {3 6}{\pi^ {2}} \psi_ {I} (i t). \end{array}
$$

Our aim is to prove that$B ( t ) > 0$for$t \in ( 0 , \infty )$. A plot of$B ( t )$is given in Figure 2.

Figure 2: Plot of the functions$B(t)$,$\begin{array} { r } { B _ { 0 } ^ { ( 2 ) } ( t ) = \frac { 3 6 8 6 4 0 } { \pi ^ { 2 } } t ^ { 2 } e ^ { - \pi / t } } \end{array}$, and$\begin{array} { r } { B _ { \infty } ^ { ( 1 ) } ( t ) = \frac { 8 6 4 0 } { \pi } t - \frac { 2 3 3 2 8 } { \pi ^ { 2 } } } \end{array}$

![](images/page_20_chart_11.jpg)

For$n \geq 0$let$B _ { 0 } ^ { ( n ) }$and$B _ { \infty } ^ { ( n ) }$be the functions such that

$$
\begin{array}{r l} & B (t) = B _ {0} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n / t}) \quad \mathrm{as} t \to 0, \\ & B (t) = B _ {\infty} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n t}) \quad \mathrm{as} t \to \infty . \end{array}
$$

We find

$$
\begin{array}{r} B _ {\infty} ^ {(6)} (t) = - \frac {1 2 9 6 0}{\pi^ {2}} - \frac {1 8 4 3 2 0}{\pi^ {2}} e ^ {- \pi t} - \frac {1 1 6 6 4 0}{\pi^ {2}} e ^ {- 2 \pi t} - \frac {2 2 5 6 0 7 6 8}{\pi^ {2}} e ^ {- 3 \pi t} + \frac {5 6 5 4 0 1 6 0}{\pi^ {2}} e ^ {- 4 \pi t} - \frac {8 6 9 9 1 6 6 7 2}{\pi^ {2}} e ^ {- 5 \pi t} \\ + t (\frac {8 6 4 0}{\pi} + \frac {2 4 3 6 4 8 0}{\pi} e ^ {- 2 \pi t} + \frac {1 1 3 0 1 1 2 0 0}{\pi} e ^ {- 4 \pi t}) - t ^ {2} (5 1 8 4 0 0 e ^ {- 2 \pi t} + 3 1 1 0 4 0 0 0 e ^ {- 4 \pi t}) \end{array}
$$

and

$$
B _ {0} ^ {(6)} (t) = t ^ {2} (\frac {3 6 8 6 4 0}{\pi^ {2}} e ^ {- \pi / t} - 5 1 8 4 0 0 e ^ {- 2 \pi / t} + \frac {4 5 1 2 1 5 3 6}{\pi^ {2}} e ^ {- 3 \pi / t} - 3 1 1 0 4 0 0 0 e ^ {- 4 \pi / t} + \frac {1 7 3 9 8 3 3 3 4 4}{\pi^ {2}} e ^ {- 5 \pi / t}).
$$

The estimates (65)–(69) imply that

$$
\left| B (t) - B _ {0} ^ {(6)} (t) \right| \leq R _ {0} ^ {(6)} (t) \quad \text { for } t \in (0, 1 ]
$$

and

$$
\left| B (t) - B _ {\infty} ^ {(6)} (t) \right| \leq R _ {\infty} ^ {(6)} (t) \quad \text { for } t \in [ 1, \infty).
$$

Using interval arithmetic we verify that

$$
\begin{array}{l} \left| R _ {0} ^ {(6)} (t) \right| \leq \left| B _ {0} ^ {(6)} (t) \right| \quad \text {for} t \in (0, 1 ], \\ \left| R _ {\infty} ^ {(6)} (t) \right| \leq \left| B _ {\infty} ^ {(6)} (t) \right| \quad \text {for} t \in [ 1, \infty), \\ B _ {0} ^ {(6)} (t) > 0 \quad \text {for} t \in (0, 1 ], \\ B _ {\infty} ^ {(6)} (t) > 0 \quad \text {for} t \in [ 1, \infty). \end{array}
$$

Now identity (70) implies (4).

Finally, the property (5) readily follows from Proposition 4 and Proposition 8. This finishes the proof of Theorems 4 and 3. □

## Acknowledgments

I thank Andriy Bondarenko for sharing his ideas, for fruitful discussions, and for his support. Also I am grateful to Danilo Radchenko for his valuable ideas and his help with numerical computations. I am most grateful to J. Kramer, J. M. Sullivan, G. M. Ziegler, and anonymous referees for their valuable comments and suggestions on the manuscript.

## References

[1] M. Abramowitz, I. Stegun, Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, Applied Mathematics Series 55 (10th ed.), New York, USA: United States Department of Commerce, National Bureau of Standards; Dover Publications, 1964.

[2] A. Bondarenko, D. Radchenko, M. Viazovska, On optimal asymptotic bounds for spherical designs, Annals of Math. 178 (2)(2013), pp. 443–452.

[3] J. Bruinier, Borcherds products on O(2,l) and Chern classes of Heegner divisors, Springer Lecture Notes in Mathematics 1780 (2002).

[4] H. Cohn, N. Elkies, New upper bounds on sphere packings I, Annals of Math. 157 (2003) pp. 689–714.

[5] H. Cohn, A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (1) (2007), pp. 99–148.

[6] J. H. Conway and N. J. A. Sloane, What Are All the Best Sphere Packings in Low Dimensions?, Discrete Comput. Geom. (László Fejes Tóth Festschrift), 13 (1995), pp. 383–403.

[7] P. Delsarte, Bounds for unrestricted codes, by linear programming, Philips Res. Rep. 27 (1972), pp. 272–289.

[8] P. Delsarte, J. M. Goethals, and J. J. Seidel, Spherical codes and designs, Geom. Dedicata, 6 (1977), pp. 363–388.

[9] F. Diamond, J. Shurman, A First Course in Modular Forms, Springer New York, 2005.

[10] L. Fejes Tóth, Über die dichteste Kugellagerung, Math. Z. 48 (1943), pp. 676–684.

[11] T. Hales, A proof of the Kepler conjecture, Annals of Math. 162 (3) (2005), pp. 1065–1185.

[12] D. Hejhal, The Selberg trace formula for PSL(2, R), Vol. 2, Springer Lecture Notes in Mathematics 1001 (1983).

[13] G. A. Kabatiansky and V. I. Levenshtein, Bounds for packings on a sphere and in space, Problems of Information Transmission 14 (1978), pp. 1–17.

[14] D. Mumford, Tata Lectures on Theta I, Birkhäuser, 1983.

[15] H. Petersson, Ueber die Entwicklungskoefizienten der automorphen Formen, Acta Mathematica, Bd. 58 (1932), pp. 169–215.

[16] F. Pfender, G. M. Ziegler, Kissing numbers, sphere packings, and some unexpected proofs, Notices of the AMS 51 (8) (2004) pp. 873–883.

[17] H. Rademacher and H. S. Zuckerman, On the Fourier coeficients of certain modular forms of positive dimension, Annals of Math. (2) 39 (1938), pp. 433–462.

[18] A. Thue, Über die dichteste Zusammenstellung von kongruenten Kreisen in einer Ebene, Norske Vid. Selsk. Skr. No.1 (1910), pp. 1–9.

[19] V. A. Yudin, Lower bounds for spherical designs, Izv. Ross. Akad. Nauk Ser. Mat. 61 (1997), pp. 211–233. English transl., Izv. Math. 6 (1997), pp. 673–683.

[20] D. Zagier, Elliptic Modular Forms and Their Applications, In: The 1-2-3 of Modular Forms, (K. Ranestad, ed.) Norway, Springer Universitext, 2008.

Berlin Mathematical School

Str. des 17. Juni 136

10623 Berlin

and

Humboldt University of Berlin

Rudower Chaussee 25

12489 Berlin

Email address: viazovska@gmail.com