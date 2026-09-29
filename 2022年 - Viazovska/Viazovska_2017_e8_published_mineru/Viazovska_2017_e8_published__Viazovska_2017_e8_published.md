# The sphere packing problem in dimension 8

By Maryna S. Viazovska

## Abstract

In this paper we prove that no packing of unit balls in Euclidean space $\mathbb { R } ^ { 8 }$has density greater than that of the$E _ { 8 }$-lattice packing.

## 1. Introduction

The sphere packing constant measures which portion of d-dimensional Euclidean space can be covered by nonoverlapping unit balls. More precisely, let$\mathbb { R } ^ { d }$be the Euclidean vector space equipped with distance$\| \cdot \|$and Lebesgue measure$\operatorname { V o l } ( \cdot )$. For$\boldsymbol { x } \in \mathbb { R } ^ { d }$and$r \in \mathbb { R } _ { > 0 } ,$, we denote by$B _ { d } ( x , r )$the open ball in$\mathbb { R } ^ { d }$with center x and radius$r .$Let$X \subset \mathbb { R } ^ { d }$be a discrete set of points such that$\| x - y \| \geq 2$for any distinct$x , y \in X$. Then the union

$$
\mathcal {P} = \bigcup_ {x \in X} B _ {d} (x, 1)
$$

is a sphere packing. If X is a lattice in$\mathbb { R } ^ { d }$, then we say that$\mathcal { P }$is a lattice sphere packing. The finite density of a packing$\mathcal { P }$is defined as

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

For which dimensions do we know the exact value of$\Delta _ { d } ?$Trivially, in dimension 1 we have$\Delta _ { 1 } = 1$. It has long been known that a best packing in dimension 2 is the familiar hexagonal lattice packing, in which each disk is touching six others. The first proof of this result was given by A. Thue at the beginning ot twentieth century [18]. However, his proof was considered by some experts incomplete. A rigorous proof was given by L. Fejes T´oth in 1940s [10]. The density of the hexagonal lattice packing is$\frac { \pi } { \sqrt { 1 2 } }$, therefore $\textstyle \Delta _ { 2 } = { \frac { \pi } { \sqrt { 1 2 } } } \approx 0 . 9 0 6 9 0$. The packing problem in dimension 3 turned out to be more dificult. Johannes Kepler conjectured in his essay$^ { 6 6 } \mathrm { O n }$the six-cornered snowflake” (1611) that no arrangement of equally sized spheres filling space has density greater than$\frac { \pi } { \sqrt { 1 8 } }$. This density is attained by the face-centered cubic packing and also by uncountably many nonlattice packings. The Kepler conjecture was famously proven by T. Hales in 1998 [11], and therefore we know that$\Delta _ { 3 } = \textstyle { \frac { \pi } { \sqrt { 1 8 } } } \approx 0 . 7 4 0 4 8$. In 2015 Hales and his 21 coauthors published a complete formal proof of the Kepler conjecture that can be verified by automated proof checking software. Before now, the exact values of the sphere packing constants in all dimensions greater than 3 have been unknown. A list of conjectural best packings in dimensions less than 10 can be found in [6]. Upper bounds for the sphere packing constants$\Delta _ { d }$as d$\leq 3 6$are given in [4]. Surprisingly enough, these upper bounds and known lower bounds on$\Delta _ { d }$are extremely close in dimensions$d = 8$and$d = 2 4$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">c 2017 Department of Mathematics, Princeton University.</span></small>

The main result of this paper is the proof that

$$
\Delta_ {8} = \frac {\pi^ {4}}{3 8 4} \approx 0. 2 5 3 6 7.
$$

This is the density of the$E _ { 8 }$-lattice sphere packing. Recall that the$E _ { 8 }$-lattice $\Lambda _ { 8 } \subset \mathbb { R } ^ { 8 }$is given by

$$
\Lambda_ {8} = \left\{\left(x _ {i}\right) \in \mathbb {Z} ^ {8} \cup \left(\mathbb {Z} + \frac {1}{2}\right) ^ {8} \mid \sum_ {i = 1} ^ {8} x _ {i} \equiv 0 (\mathrm{mod} 2) \right\}.
$$

Up to isometry,$\Lambda _ { 8 }$is the unique positive-definite, even, unimodular lattice of rank 8. The name derives from the fact that it is the root lattice of the$E _ { 8 }$root system. The minimal distance between two points in$\Lambda _ { 8 }$is${ \sqrt { 2 } } .$. The E<sub>8</sub>-lattice sphere packing is the packing of unit balls with centers at$\scriptstyle { \frac { 1 } { \sqrt { 2 } } } \Lambda _ { 8 }$. Our main result is

Theorem 1. No packing of unit balls in Euclidean space$\mathbb { R } ^ { 8 }$has density greater than that of the$E _ { 8 } - l a t t i c e$packing.

Furthermore, our proof of Theorem 1 combined with arguments given in [4, §8] implies that the E<sub>8</sub>-lattice sphere packing is the unique periodic packing of maximal density.

The paper is organized as follows. In Section 2 we explain the idea of the proof of Theorem 1 and describe the methods we use. In Section 3 we give a brief overview of the theory of modular forms. In Section 4 we construct supplementary radial functions a,$b : \mathbb { R } ^ { 8 } \to i \mathbb { R }$, which are eigenfunctions of the Fourier transform and have double zeroes at almost all points of$\Lambda _ { 8 } .$This construction is crucial for our proof of Theorem 1. Finally, in Section 5 we complete the proof.

## 2. Linear programming bounds

Our proof of Theorem 1 is based on linear programming bounds. This technique was successfully applied to obtain upper bounds in a wide range of discrete optimization problems such as error-correcting codes [7], equal weight quadrature formulas [8], and spherical codes [13], [16]. In exceptional cases linear programming bounds are optimal [5]. However, in general linear programming bounds are not sharp, and it is an open question how big the errors of such bounds can be. It is known [2] that the linear programming bounds for the minimal number of points in an equal weight quadrature formula on the sphere$S ^ { d }$are asymptotically optimal up to a constant depending on d. Linear programming bounds can also be applied to the sphere packing problem. Kabatiansky and Levenshtein [13] deduced upper bounds for sphere packing from their results on spherical codes.

In 2003 Cohn and Elkies [4] developed linear programming bounds that apply directly to sphere packings. Using their new method they improved the previously known upper bounds for the sphere packing constant in dimensions from 4 to 36. The most striking results obtained by this technique are upper bounds for dimensions 8 and 24. For example, their upper bound for$\Delta _ { 8 }$was only 1.000001 times greater than the lower bound, which is given by the density of the$E _ { 8 }$sphere packing. This bound can be improved even further by more extensive computer computations.

We explain the Cohn–Elkies linear programming bounds in more detail. To this end we recall a few definitions from Fourier analysis. The Fourier transform of an$L ^ { 1 }$function$f : \mathbb { R } ^ { d }  \mathbb { C }$is defined as

$$
\mathcal {F} (f) (y) = \widehat {f} (y) := \int_ {\mathbb {R} ^ {d}} f (x) e ^ {- 2 \pi i x \cdot y} d x, \quad y \in \mathbb {R} ^ {d},
$$

where$\begin{array} { r } { x \cdot y = \frac { 1 } { 2 } \| x \| ^ { 2 } + \frac { 1 } { 2 } \| y \| ^ { 2 } - \frac { 1 } { 2 } \| x - y \| ^ { 2 } } \end{array}$is the standard scalar product in $\mathbb { R } ^ { d } . \mathrm { ~ A ~ } C ^ { \infty }$function$f : \mathbb { R } ^ { d }  \mathbb { C }$is called a Schwartz function if it tends to zero as$\| x \|  \infty$faster then any inverse power of$\lVert x \rVert$, and the same holds for all partial derivatives of$f .$. The set of all Schwartz functions is called the Schwartz space. The Fourier transform is an automorphism of this space. We will also need the following wider class of functions. We$\operatorname { s a y }$that a function $f : \mathbb { R } ^ { d }  \mathbb { C }$is admissible if there is a constant$\delta > 0$such that$| f ( x ) |$and$| { \widehat { f } } ( x ) |$ are bounded above by a constant times$( 1 + | x | ) ^ { - d - \delta }$. The following theorem is the key result of [4]:

Theorem 2 (Cohn, Elkies [4]). Suppose that$f : \mathbb { R } ^ { d }  \mathbb { R }$is an admissible function, is not identically zero, and satisfies

$$
f (x) \leq 0 f o r \| x \| \geq 1\tag{1}
$$

and

$$
\widehat {f} (x) \geq 0 \text {   for   all   } x \in \mathbb {R} ^ {d}.\tag{2}
$$

Then the density of d-dimensional sphere packings is bounded above by

$$
\frac {f (0)}{\widehat {f} (0)} \cdot \frac {\pi^ {\frac {d}{2}}}{2 ^ {d} \Gamma (\frac {d}{2} + 1)} = \frac {f (0)}{\widehat {f} (0)} \cdot \mathrm{Vol}   B _ {d} \left(0, \frac {1}{2}\right).
$$

Without loss of generality we can assume that a function$f$in Theorem 2 is radial; i.e., its value at each point depends only on the distance between the point and the origin [4, p. 695]. For a radial function$f _ { 0 } : \mathbb { R } ^ { d }  \mathbb { R }$, we will denote by$f _ { 0 } ( r )$the common value of$f _ { 0 }$on vectors of length r. Henceforth we assume$d = 8$. The Poisson summation formula implies

$$
\sum_ {\ell \in \frac {1}{\sqrt {2}} \Lambda_ {8}} f (\ell) = 2 ^ {4} \sum_ {\ell \in \sqrt {2} \Lambda_ {8}} \widehat {f} (\ell).
$$

Hence, if a function f satisfies conditions (1) and (2), then

$$
\frac {f (0)}{\widehat {f} (0)} \geq 2 ^ {4}.
$$

We say that an admissible function$f : \mathbb { R } ^ { 8 }$R is optimal if it satisfies (1), (2) and$f ( 0 ) / \widehat { f } ( 0 ) = 2 ^ { 4 }$

The main step in our proof of Theorem 1 is the explicit construction of an optimal function. It will be convenient for us to scale this function by$\sqrt { 2 }$

Theorem 3. There exists a radial Schwartz function$g : \mathbb { R } ^ { 8 }  \mathbb { R }$that satisfies

(3)

$$
g (x) \leq 0 f o r \| x \| \geq \sqrt {2},\tag{4}
$$

$$
\widehat {g} (x) \geq 0 \text {for all} x \in \mathbb {R} ^ {8},\tag{5}
$$

$$
g (0) = \widehat {g} (0) = 1.
$$

Moreover, the values$g ( x )$and${ \widehat { g } } ( x )$do not vanish for all vectors x with$\| { x } \| ^ { 2 }$∈/ $2 \mathbb { Z } _ { > 0 }$

Theorem 2 applied to the optimal function$f ( x ) = g ( { \sqrt { 2 } } x )$immediately implies Theorem 1. Additionally, the function g satisfies the conclusions of [4, Conj. 8.1]. This implies the uniqueness of the densest periodic sphere packing in$\mathbb { R } ^ { 8 }$

Let us briefly explain our strategy for the proof of Theorem 3. First, we observe that conditions (3)–(5) imply additional properties of the function g.

Suppose that there exists a Schwartz function g such that conditions$( 3 ) \AA { - } ( 5 )$ hold. The Poisson summation formula states

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

Therefore, we deduce that$g ( \ell ) = \widehat { g } ( \ell ) = 0$for all$\ell \in \Lambda _ { 8 } \backslash \{ 0 \}$. Moreover, the first derivatives$\begin{array} { r } { \frac { d } { d r } g ( r ) } \end{array}$and$\begin{array} { r } { \frac { d } { d r } \widehat { g } ( r ) } \end{array}$also vanish at all$\Lambda _ { 8 } \mathrm { - l a t t i c e }$points of length bigger than${ \sqrt { 2 } } .$. We will say that g and$\widehat g$have double zeroes at these points. This property gives us a hint on constructing the function g explicitly.

In Section 5 a function g satisfying (3)–(5) is given in a closed form. Namely, it is defined as an integral transform (Laplace transform) of a modular form of a certain kind. The next section is a brief introduction to the theory of modular forms.

## 3. Modular forms

Let H be the upper half-plane$\{ z \in \mathbb { C } \mid \operatorname { I m } \left( z \right) > 0 \}$. The modular group $\Gamma ( 1 ) : = \mathrm { P S L } _ { 2 } ( \mathbb { Z } )$acts on H by linear fractional transformations

$$
\left( \begin{array}{c c} a & b \\ c & d \end{array} \right) z := \frac {a z + b}{c z + d}.
$$

Let N be a positive integer. The level N principal congruence subgroup of Γ(1) is

$$
\Gamma (N) := \left\{\left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \in \Gamma (1) \mid \left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \equiv \left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right) \bmod N \right\}.
$$

A subgroup$\Gamma \subset \Gamma ( 1 )$is called a congruence subgroup if$\Gamma ( N ) \subset \Gamma$for some $N \in  { \mathbb { N } }$. An important example of a congruence subgroup is

$$
\Gamma_ {0} (N) := \bigl \{\bigl ( \begin{array}{c c} a & b \\ c & d \end{array} \bigr) \in \Gamma (1) \big | c \equiv 0 \bmod N \bigr \}.
$$

Let$z \in \mathbb { H } , k \in \mathbb { Z }$, and$( \mathbf { \Sigma } _ { c } ^ { a } \mathbf { \Sigma } _ { d } ^ { b } ) \in \mathrm { S L _ { 2 } } ( \mathbb { Z } )$. The automorphy factor of weight k is defined as

$$
j _ {k} (z, \left( \begin{array}{c c} a & b \\ c & d \end{array} \right)) := (c z + d) ^ {- k}.
$$

The automorphy factor satisfies the chain rule

$$
j _ {k} (z, \gamma_ {1} \gamma_ {2}) = j _ {k} (z, \gamma_ {2}) j _ {k} (\gamma_ {2} z, \gamma_ {1}).
$$

Let$F$be a function on H and$\gamma \in \mathrm { P S L } _ { 2 } ( \mathbb { Z } )$. Then the slash operator acts on $F$by

$$
(F | _ {k} \gamma) (z) := j _ {k} (z, \gamma) F (\gamma z).
$$

The chain rule implies

$$
F | _ {k} \gamma_ {1} \gamma_ {2} = (F | _ {k} \gamma_ {1}) | _ {k} \gamma_ {2}.
$$

A (holomorphic) modular form of integer weight k and congruence subgroup Γ is a holomorphic function$f : \mathbb { H } \to \mathbb { C }$such that

(1)$f | _ { k } \gamma = f$for all$\gamma \in \Gamma ;$; and

(2) for each$\alpha \in \Gamma ( 1 )$, the function$f | _ { k } \alpha$has Fourier expansion

$$
f | _ {k} \alpha (z) = \sum_ {n = 0} ^ {\infty} c _ {f} \left(\alpha , \frac {n}{n _ {\alpha}}\right) e ^ {2 \pi i \frac {n}{n _ {\alpha}} z}
$$

for some$n _ { \alpha } \in \mathbb { N }$and Fourier coeficients$c _ { f } ( \alpha , m ) \in \mathbb { C }$

Let$M _ { k } ( \Gamma )$be the space of modular forms of weight k for the congruence subgroup Γ. A key fact in the theory of modular forms is that the spaces $M _ { k } ( \Gamma )$are finite dimensional.

We consider several examples of modular forms. For an even integer$k \geq 4$ we define the weight k Eisenstein series as

$$
E _ {k} (z) := \frac {1}{2 \zeta (k)} \sum_ {(c, d) \in \mathbb {Z} ^ {2} \backslash (0, 0)} (c z + d) ^ {- k}.\tag{9}
$$

Since the sum converges absolutely, it is easy to see that$E _ { k } \in M _ { k } ( \Gamma ( 1 ) )$. The Eisenstein series possesses the Fourier expansion

$$
E _ {k} (z) = 1 + \frac {2}{\zeta (1 - k)} \sum_ {n = 1} ^ {\infty} \sigma_ {k - 1} (n) e ^ {2 \pi i n z},\tag{10}
$$

where$\begin{array} { r } { \sigma _ { k - 1 } ( n ) = \sum d \vert n \ : d ^ { k - 1 } } \end{array}$. In particular, we have

$$
\begin{array}{l} E _ {4} (z) = 1 + 2 4 0 \sum_ {n = 1} ^ {\infty} \sigma_ {3} (n) e ^ {2 \pi i n z}, \\ E _ {6} (z) = 1 - 5 0 4 \sum_ {n = 1} ^ {\infty} \sigma_ {5} (n) e ^ {2 \pi i n z}. \end{array}
$$

The infinite sum (9) does not converge absolutely for$k = 2$. On the other hand, the expression (10) converges to a holomorphic function on the upper half-plane, and therefore we set

$$
E _ {2} (z) := 1 - 2 4 \sum_ {n = 1} ^ {\infty} \sigma_ {1} (n) e ^ {2 \pi i n z}.\tag{11}
$$

This function is not modular, but it satisfies

$$
z ^ {- 2} E _ {2} \left(\frac {- 1}{z}\right) = E _ {2} (z) - \frac {6 i}{\pi} \frac {1}{z}.\tag{12}
$$

The proof of this identity can be found in [19, §2.3]. The weight two Eisenstein series$E _ { 2 }$is an example of a quasimodular form [19, §5.1].

Another example of modular forms we consider are theta functions [19, §3.1]. We define three theta functions (so-called “Thetanullwerte”) as

$$
\theta_ {0 0} (z) = \sum_ {n \in \mathbb {Z}} e ^ {\pi i n ^ {2} z},
$$

$$
\theta_ {0 1} (z) = \sum_ {n \in \mathbb {Z}} (- 1) ^ {n} e ^ {\pi i n ^ {2} z},
$$

$$
\theta_ {1 0} (z) = \sum_ {n \in \mathbb {Z}} e ^ {\pi i (n + \frac {1}{2}) ^ {2} z}.
$$

The group Γ(1) is generated by the elements$\begin{array} { r } { T = \left( \begin{array} { l } { 1 } \\ { 0 } \end{array} \frac { 1 } { 1 } \right) } \end{array}$and$S = \left( \begin{array} { c } { { 0 } } \\ { { - 1 0 } } \end{array} \right)$. These elements act on the fourth powers of the theta functions in the following way

(13)

$$
z ^ {- 2} \theta_ {0 0} ^ {4} \left(\frac {- 1}{z}\right) = - \theta_ {0 0} ^ {4} (z),\tag{14}
$$

$$
z ^ {- 2} \theta_ {0 1} ^ {4} \left(\frac {- 1}{z}\right) = - \theta_ {1 0} ^ {4} (z),\tag{15}
$$

$$
z ^ {- 2} \theta_ {1 0} ^ {4} \left(\frac {- 1}{z}\right) = - \theta_ {0 1} ^ {4} (z),
$$

and

(16)

$$
\theta_ {0 0} ^ {4} (z + 1) = \theta_ {0 1} ^ {4} (z),\tag{17}
$$

$$
\theta_ {0 1} ^ {4} (z + 1) = \theta_ {0 0} ^ {4} (z),\tag{18}
$$

$$
\theta_ {1 0} ^ {4} (z + 1) = - \theta_ {1 0} ^ {4} (z).
$$

Moreover, these three theta functions satisfy the Jacobi identity

$$
\theta_ {0 1} ^ {4} + \theta_ {1 0} ^ {4} = \theta_ {0 0} ^ {4}.\tag{19}
$$

The theta functions$\theta _ { 0 0 } ^ { 4 } , \theta _ { 0 1 } ^ { 4 }$, and$\theta _ { 1 0 } ^ { 4 }$belong to$M _ { 2 } ( \Gamma ( 2 ) )$.

A weakly-holomorphic modular form of integer weight k and congruence subgroup Γ is a holomorphic function$f : \mathbb { H } \to \mathbb { C }$such that

(1)$f | _ { k } \gamma = f$for all$\gamma \in \Gamma$;

(2) for each$\alpha \in \Gamma ( 1 )$, the function$f | _ { k } \alpha$has Fourier expansion

$$
f | _ {k} \alpha (z) = \sum_ {n = n _ {0}} ^ {\infty} c _ {f} \left(\alpha , \frac {n}{n _ {\alpha}}\right) e ^ {2 \pi i \frac {n}{n _ {\alpha}} z}
$$

for some$n _ { 0 } \in \mathbb { Z }$and$n _ { \alpha } \in \mathbb { N }$

For an m-periodic holomorphic function$f$and$n \in { \frac { 1 } { m } } \mathbb { Z }$, we will denote the n-th Fourier coeficient of$f$by$c _ { f } ( n )$so that

$$
f (z) = \sum_ {n \in \frac {1}{m} \mathbb {Z}} c _ {f} (n) e ^ {2 \pi i n z}.
$$

We denote the space of weakly-holomorphic modular forms of weight k and group Γ by$M _ { k } ^ { ! } ( \Gamma )$. The spaces$M _ { k } ^ { ! } ( \Gamma )$are infinite dimensional. Probably the most famous weakly-holomorphic modular form is the elliptic j-invariant

$$
j := \frac {1 7 2 8 E _ {4} ^ {3}}{E _ {4} ^ {3} - E _ {6} ^ {2}}.
$$

This function belongs to$M _ { 0 } ^ { ! } ( \Gamma ( 1 ) )$and has the Fourier expansion

$$
\begin{array}{c} j (z) = q ^ {- 1} + 7 4 4 + 1 9 6 8 8 4   q + 2 1 4 9 3 7 6 0   q ^ {2} \\ + 8 6 4 2 9 9 9 7 0   q ^ {3} + 2 0 2 4 5 8 5 6 2 5 6   q ^ {4} + O (q ^ {5}), \end{array}
$$

where$q = e ^ { 2 \pi i z }$. Using a simple computer algebra system such as PARI GP or Mathematica one can compute the first hundred terms of this Fourier expansion within a few seconds. An important question is to find an asymptotic formula for$c _ { j } ( n )$, the n-th Fourier coeficient of$j .$. Using the Hardy–Ramanujan circle method [17, pp. 460–461] or the nonholomorphic Poincar´e series [15], one can show that

$$
c _ {j} (n) = \frac {2 \pi}{\sqrt {n}} \sum_ {k = 1} ^ {\infty} \frac {A _ {k} (n)}{k} I _ {1} \left(\frac {4 \pi \sqrt {n}}{k}\right) \qquad n \in \mathbb {Z} _ {> 0},\tag{20}
$$

where

$$
A_{k}(n) = \sum_{\substack{h\bmod k\\ (h,k) = 1}}e^{\frac{-2\pi i}{k} (nh + h^{\prime})},\quad hh^{\prime}\equiv -1(\bmod k),
$$

and$I _ { \alpha } ( x )$denotes the modified Bessel function of the first kind defined as in [1, §9.6]. A similar convergent asymptotic expansion holds for the Fourier coeficients of any weakly holomorphic modular form [12, pp. 660–662], [3, Props. 1.10 and 1.12]. Such a convergent expansion implies efective estimates for the Fourier coeficients.

For a comprehensive introduction to the theory of modular forms, we refer the reader to [19] and [9].

## 4. Fourier eigenfunctions with double zeroes at lattice points

In this section we construct two radial Schwartz functions$a , b : \mathbb { R } ^ { 8 } \to i \mathbb { R }$ such that

(21)

$$
\mathcal {F} (a) = a,\tag{22}
$$

$$
\mathcal {F} (b) = - b,
$$

which double zeroes at all$\Lambda _ { 8 } .$-vectors of length greater than$\sqrt { 2 }$. Recall that each vector of$\Lambda _ { 8 }$has length$\sqrt { 2 n }$for some$n \in \mathbb { N } _ { \geq 0 }$. We define a and b so that their values are purely imaginary because this simplifies some of our computations. We will show in Section 5 that an appropriate linear combination of functions a and b satisfies conditions (3)–(5).

First, we will define the function a. To this end we consider the following weakly holomorphic modular forms:

(23)

$$
\varphi_ {- 2} := \frac {- 1 7 2 8 E _ {4} E _ {6}}{E _ {4} ^ {3} - E _ {6} ^ {2}},\tag{24}
$$

$$
\varphi_ {- 4} := \frac {1 7 2 8 E _ {4} ^ {2}}{E _ {4} ^ {3} - E _ {6} ^ {2}}.
$$

The modular form$E _ { 4 } ^ { 3 } - E _ { 6 } ^ { 2 }$does not vanish in the upper half-plane, hence$\varphi _ { - 2 }$ and$\varphi _ { - 4 }$have no poles in H. Analogously to (20), the Fourier coeficients of $\varphi _ { - 2 }$and$\varphi _ { - 4 }$satisfy

$$
c _ {\varphi_ {\kappa}} (n) = 2 \pi n ^ {\frac {\kappa - 1}{2}} \sum_ {k = 1} ^ {\infty} \frac {A _ {k} (n)}{k} I _ {1 - \kappa} \left(\frac {4 \pi \sqrt {n}}{k}\right), \qquad n \in \mathbb {Z} _ {> 0}, \kappa = - 2, - 4.\tag{25}
$$

We define

(26)

$$
\phi_ {- 4} := \varphi_ {- 4},\tag{27}
$$

$$
\phi_ {- 2} := \varphi_ {- 4} E _ {2} + \varphi_ {- 2},\tag{28}
$$

$$
\phi_ {0} := \varphi_ {- 4} E _ {2} ^ {2} + 2 \varphi_ {- 2} E _ {2} + j - 1 7 2 8.
$$

The function$\phi _ { 0 } ( z )$is not modular; however, the identity (12) implies the following transformation rule:

$$
\phi_ {0} \left(\frac {- 1}{z}\right) = \phi_ {0} (z) - \frac {1 2 i}{\pi} \frac {1}{z} \phi_ {- 2} (z) - \frac {3 6}{\pi^ {2}} \frac {1}{z ^ {2}} \phi_ {- 4} (z).\tag{29}
$$

Moreover, we have

(30)

$$
\phi_ {- 2} = - 3 D (\varphi_ {- 4}) + 3 \varphi_ {- 2},\tag{31}
$$

$$
\phi_ {0} = 1 2 D ^ {2} (\varphi_ {- 4}) - 3 6 D (\varphi_ {- 2}) + 2 4 j - 1 7 8 5 6,
$$

where${ \begin{array} { r } { D f ( z ) = { \frac { 1 } { 2 \pi i } } { \frac { d } { d z } } f ( z ) } \end{array} }$. These identities combined with (20) and (25) give the asymptotic formula for the Fourier coeficients$c _ { \phi _ { - 4 } } ( n ) , c _ { \phi _ { - 2 } } ( n )$, and$c _ { \phi _ { 0 } } ( n )$ The first several terms of the corresponding Fourier expansions are

(32)

$$
\phi_ {- 4} (z) = q ^ {- 1} + 5 0 4 + 7 3 7 6 4 q + 2 6 9 5 0 4 0 q ^ {2} + 5 4 7 5 5 7 3 0 q ^ {3} + O \left(q ^ {4}\right),\tag{33}
$$

$$
\phi_ {- 2} (z) = 7 2 0 + 2 0 3 0 4 0 q + 9 4 1 7 6 0 0 q ^ {2}
$$

$$
+ 2 2 3 4 7 3 6 0 0 q ^ {3} + 3 5 6 6 7 8 2 0 8 0 q ^ {4} + O (q ^ {5}),\tag{34}
$$

$$
\begin{array}{c} \phi_ {0} (z) = 5 1 8 4 0 0 q + 3 1 1 0 4 0 0 0 q ^ {2} + 8 7 0 9 1 2 0 0 0 q ^ {3} \\ + 1 5 6 9 7 1 5 2 0 0 0 q ^ {4} + O (q ^ {5}), \end{array}
$$

where$q = e ^ { 2 \pi i z }$. For$x \in \mathbb { R } ^ { 8 }$, we define

$$
\begin{array}{l} a (x) := \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i \| x \| ^ {2} z} d z + \int_ {1} ^ {i} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i \| x \| ^ {2} z} d z \\ \qquad - 2 \int_ {0} ^ {i} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i \| x \| ^ {2} z} d z + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i \| x \| ^ {2} z} d z. \end{array}\tag{35}
$$

We observe that the contour integrals in (35) converge absolutely and uniformly for$x \in \mathbb { R } ^ { 8 }$. Indeed,$\phi _ { 0 } ( z ) = O ( e ^ { - 2 \pi i z } )$as Im$( z ) \to \infty$. Therefore,$a ( x )$is well defined. Now we prove that a satisfies condition (21).

Proposition 1. The function a defined by (35) belongs to the Schwartz space and satisfies

$$
\widehat {a} (x) = a (x).
$$

Proof. First, we prove that a is a Schwartz function. From (20), (25), and (31) we deduce that the Fourier coeficients of$\phi _ { 0 }$satisfy

$$
| c _ {\phi_ {0}} (n) | \leq 2 e ^ {4 \pi \sqrt {n}}, \quad n \in \mathbb {Z} _ {> 0}.
$$

Thus, there exists a positive constant C such that

$$
| \phi_ {0} (z) | \leq C e ^ {- 2 \pi \mathrm{Im} z} \quad \text { for } \mathrm{Im} z > \frac {1}{2}.
$$

We estimate the first summand in the right-hand side of (35). For$r \in \mathbb { R } _ { \geq 0 }$1 we have

$$
\left| \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z \right| = \left| \int_ {i \infty} ^ {- 1 / (i + 1)} \phi_ {0} (z) z ^ {- 4} e ^ {\pi i r ^ {2} (- 1 / z - 1)} d z \right|
$$

$$
\leq C _ {1} \int_ {1 / 2} ^ {\infty} e ^ {- 2 \pi t} e ^ {- \pi r ^ {2} / t} d t \leq C _ {1} \int_ {0} ^ {\infty} e ^ {- 2 \pi t} e ^ {- \pi r ^ {2} / t} d t = C _ {2} r K _ {1} (2 \sqrt {2} \pi r),
$$

where$C _ { 1 }$and$C _ { 2 }$are some positive constants and$K _ { \alpha } ( x )$is the modified Bessel function of the second kind defined as in [1, §9.6]. This estimate also holds for the second and third summand in (35). For the last summand, we have

$$
\left| \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i r ^ {2} z} d z \right| \leq C \int_ {1} ^ {\infty} e ^ {- 2 \pi t} e ^ {- \pi r ^ {2} t} d t = C _ {3} \frac {e ^ {\pi (r ^ {2} + 2)}}{r ^ {2} + 2}.
$$

Therefore, we arrive at

$$
| a (r) | \leq 4 C _ {2} r K _ {1} (2 \sqrt {2} \pi r) + 2 C _ {3} \frac {e ^ {- \pi (r ^ {2} + 2)}}{r ^ {2} + 2}.
$$

It is easy to see that the left-hand side of this inequality decays faster than any inverse power of r. Analogous estimates can be obtained for all derivatives $\begin{array} { r } { \frac { d ^ { k } } { d r ^ { k } } a \left( r \right) } \end{array}$

Now we show that a is an eigenfunction of the Fourier transform. We recall that the Fourier transform of a Gaussian function is

$$
\mathcal {F} (e ^ {\pi i \| x \| ^ {2} z}) (y) = z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})}.\tag{36}
$$

Next, we exchange the contour integration with respect to the z variable and Fourier transform with respect to the x variable in (35). This can be done since the corresponding double integral converges absolutely. In this way we obtain

$$
\begin{array}{l} \widehat {a} (y) = \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z \\ \qquad + \int_ {1} ^ {i} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z \\ \qquad - 2 \int_ {0} ^ {i} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) z ^ {- 4} e ^ {\pi i \| y \| ^ {2} (\frac {- 1}{z})} d z. \end{array}
$$

Now we make a change of variables$\begin{array} { r } { w = \frac { - 1 } { z } } \end{array}$. We obtain

$$
\begin{array}{l} \widehat {a} (y) = \int_ {1} ^ {i} \phi_ {0} \left(1 - \frac {1}{w - 1}\right) \left(\frac {- 1}{w} + 1\right) ^ {2} w ^ {2} e ^ {\pi i \| y \| ^ {2} w} d w \\ \qquad + \int_ {- 1} ^ {i} \phi_ {0} \left(1 - \frac {1}{w + 1}\right) \left(\frac {- 1}{w} - 1\right) ^ {2} w ^ {2} e ^ {\pi i \| y \| ^ {2} w} d w \\ \qquad - 2 \int_ {i \infty} ^ {i} \phi_ {0} (w) e ^ {\pi i \| y \| ^ {2} w} d w + 2 \int_ {i} ^ {0} \phi_ {0} \left(\frac {- 1}{w}\right) w ^ {2} e ^ {\pi i \| y \| ^ {2} w} d w. \end{array}
$$

Since$\phi _ { 0 }$is 1-periodic, we have

$$
\begin{array}{l} \widehat {a} (y) = \int_ {1} ^ {i} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i \| y \| ^ {2} z} d z + \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i \| y \| ^ {2} z} d z \\ \qquad + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i \| y \| ^ {2} z} d z - 2 \int_ {0} ^ {i} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i \| y \| ^ {2} z} d z \\ \qquad = a (y). \end{array}
$$

This finishes the proof of the proposition.

Next, we check that a has double zeroes at all$\Lambda _ { 8 ^ { - } }$-lattice points of length greater then${ \sqrt { 2 } }$

Proposition 2. For$r > { \sqrt { 2 } }$, we can express$a ( r )$in the following form:

$$
a (r) = - 4 \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z.\tag{37}
$$

Proof. We denote the right-hand side of (37) by$d ( r )$. It is easy to see that$d ( r )$is well defined. Indeed, from the transformation formula (29) and the expansions (34)–(32), we obtain

$$
\begin{array}{l l} \phi_ {0} \left(\frac {- 1}{i t}\right) = O (e ^ {- 2 \pi / t}) & \text {as} t \to 0, \\ \phi_ {0} \left(\frac {- 1}{i t}\right) = O (t ^ {- 2} e ^ {2 \pi t}) & \text {as} t \to \infty . \end{array}
$$

Hence, the integral (37) converges absolutely for$r > { \sqrt { 2 } }$. We can write

$$
\begin{array}{l} d (r) = \int_ {- 1} ^ {i \infty - 1} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z \\ \qquad + \int_ {1} ^ {i \infty + 1} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z. \end{array}
$$

From (29) we deduce that if$r > { \sqrt { 2 } } .$, then

$$
\phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} \rightarrow 0 \quad \mathrm{as} \operatorname{Im} (z) \rightarrow \infty
$$

Therefore, we can deform the paths of integration and rewrite

$$
\begin{array}{r l} & {d (r) = \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad - 2 \int_ {0} ^ {i} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {i} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z} \\ & {\qquad + \int_ {1} ^ {i} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z.} \end{array}
$$

Now from (29) we find

$$
\begin{array}{l} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} - 2 \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} + \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} \\ = \phi_ {0} (z + 1) (z + 1) ^ {2} - 2 \phi_ {0} (z) z ^ {2} + \phi_ {0} (z - 1) (z - 1) ^ {2} \\ \qquad - \frac {1 2 i}{\pi} (\phi_ {- 2} (z + 1) (z + 1) - 2 \phi_ {- 2} (z) z + \phi_ {- 2} (z - 1) (z - 1)) \\ \qquad - \frac {3 6}{\pi^ {2}} (\phi_ {- 4} (z + 1) - 2 \phi_ {- 4} (z) + \phi_ {- 4} (z - 1)) \\ = 2 \phi_ {0} (z). \end{array}
$$

Thus, we obtain

$$
\begin{array}{l} d (r) = \int_ {- 1} ^ {i} \phi_ {0} \left(\frac {- 1}{z + 1}\right) (z + 1) ^ {2} e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i} \phi_ {0} \left(\frac {- 1}{z}\right) z ^ {2} e ^ {\pi i r ^ {2} z} d z \\ \qquad + \int_ {1} ^ {i} \phi_ {0} \left(\frac {- 1}{z - 1}\right) (z - 1) ^ {2} e ^ {\pi i r ^ {2} z} d z + 2 \int_ {i} ^ {i \infty} \phi_ {0} (z) e ^ {\pi i r ^ {2} z} d z = a (r). \end{array}
$$

This finishes the proof.

Finally, we find another convenient integral representation for a and compute values of$a ( r )$at$r = 0$and$r = { \sqrt { 2 } }$

Proposition 3. For$r \geq 0$, we have

(38)

$$
\begin{array}{l} a (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \bigg (\frac {3 6}{\pi^ {3} (r ^ {2} - 2)} - \frac {8 6 4 0}{\pi^ {3} r ^ {4}} + \frac {1 8 1 4 4}{\pi^ {3} r ^ {2}} \\ \qquad + \int_ {0} ^ {\infty} \left(t ^ {2} \phi_ {0} \left(\frac {i}{t}\right) - \frac {3 6}{\pi^ {2}} e ^ {2 \pi t} + \frac {8 6 4 0}{\pi} t - \frac {1 8 1 4 4}{\pi^ {2}}\right) e ^ {- \pi r ^ {2} t} d t \bigg). \end{array}
$$

The integral converges absolutely for all$r \in \mathbb { R } _ { > 0 }$

Proof. Suppose that$r > { \sqrt { 2 } } .$. Then by Proposition 2,

$$
a (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} \phi_ {0} (i / t) t ^ {2} e ^ {- \pi r ^ {2} t} d t.
$$

From (34)–(29) we obtain

$$
\phi_ {0} (i / t) t ^ {2} = \frac {3 6}{\pi^ {2}} e ^ {2 \pi t} - \frac {8 6 4 0}{\pi} t + \frac {1 8 1 4 4}{\pi^ {2}} + O (t ^ {2} e ^ {- 2 \pi t}) \quad \text { as } t \to \infty .\tag{39}
$$

For$r > { \sqrt { 2 } }$, we have

$$
(4 0) \int_ {0} ^ {\infty} \left(\frac {3 6}{\pi^ {2}} e ^ {2 \pi t} + \frac {8 6 4 0}{\pi} t + \frac {1 8 1 4 4}{\pi^ {2}}\right) e ^ {- \pi r ^ {2} t} d t = \frac {3 6}{\pi^ {3} (r ^ {2} - 2)} - \frac {8 6 4 0}{\pi^ {3} r ^ {4}} + \frac {1 8 1 4 4}{\pi^ {3} r ^ {2}}.
$$

Therefore, the identity (38) holds for$r > { \sqrt { 2 } } .$

On the other hand, from the definition (35) we see that$a ( r )$is analytic in some neighborhood of$[ 0 , \infty )$. The asymptotic expansion (39) implies that the right-hand side of (38) is also analytic in some neighborhood of$[ 0 , \infty )$. Hence, the identity (38) holds on the whole interval$[ 0 , \infty )$. This finishes the proof of the proposition.

From the identity (38) we see that the values$a ( r )$are in iR for all$r \in \mathbb { R } _ { \geq 0 }$. In particular,

Proposition 4. We have

$$
a (0) = \frac {- i 8 6 4 0}{\pi}, \qquad a (\sqrt {2}) = 0, \qquad a ^ {\prime} (\sqrt {2}) = \frac {i 7 2 \sqrt {2}}{\pi}.\tag{41}
$$

Proof. These identities follow immediately from the previous proposition.

Now we construct function b. To this end we consider the modular form

$$
h := 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {0 1} ^ {4}}{\theta_ {1 0} ^ {8}}.\tag{42}
$$

It is easy to see that$h \in M _ { - 2 } ^ { ! } ( \Gamma _ { 0 } ( 2 ) )$. Indeed, first we check that$h | _ { - 2 \gamma } = h$ for all$\gamma \in \Gamma _ { 0 } ( 2 )$. Since the group$\Gamma _ { 0 } ( 2 )$is generated by elements$\left( \begin{array} { l l } { 1 } & { 0 } \\ { 2 } & { 1 } \end{array} \right)$and $\textstyle { \binom { 1 } { 0 } } _ { 1 } ^ { 1 } \big )$, it sufices to check that h is invariant under their action. This follows immediately from (13)–(18) and (42). Next we analyze the poles of h. It is known [14, Ch. I, Lemma 4.1] that$\theta _ { 1 0 }$has no zeros in the upper-half plane and hence h has poles only at the cusps. At the cusp i∞, this modular form has the Fourier expansion

$$
h (z) = q ^ {- 1} + 1 6 - 1 3 2 q + 6 4 0 q ^ {2} - 2 5 5 0 q ^ {3} + O (q ^ {4}).
$$

Let$I = { \bigl ( } { } _ { 0 } ^ { 1 } _ { 1 } ^ { 0 } { \bigr ) } , T = { \bigl ( } { } _ { 0 } ^ { 1 } _ { 1 } ^ { 1 } { \bigr ) }$, and$\boldsymbol { S } = \left( \begin{array} { l l } { 0 } & { - 1 } \\ { 1 } & { 0 } \end{array} \right)$be elements of$\Gamma ( 1 )$. We define the following three functions:

(43)

$$
\psi_ {I} := h - h | _ {- 2} S T,\tag{44}
$$

$$
\psi_ {T} := \psi_ {I} | _ {- 2} T,\tag{45}
$$

$$
\psi_ {S} := \psi_ {I} | _ {- 2} S.
$$

More explicitly, we have

(46)

$$
\psi_ {I} = 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {0 1} ^ {4}}{\theta_ {1 0} ^ {8}} + 1 2 8 \frac {\theta_ {0 1} ^ {4} - \theta_ {1 0} ^ {4}}{\theta_ {0 0} ^ {8}},\tag{47}
$$

$$
\psi_ {T} = 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {0 1} ^ {4}}{\theta_ {1 0} ^ {8}} + 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {1 0} ^ {4}}{\theta_ {0 1} ^ {8}},\tag{48}
$$

$$
\psi_ {S} = - 1 2 8 \frac {\theta_ {0 0} ^ {4} + \theta_ {1 0} ^ {4}}{\theta_ {0 1} ^ {8}} - 1 2 8 \frac {\theta_ {1 0} ^ {4} - \theta_ {0 1} ^ {4}}{\theta_ {0 0} ^ {8}}.
$$

The Fourier expansions of these functions are

(49)

$$
\begin{array}{c} \psi_ {I} (z) = q ^ {- 1} + 1 4 4 - 5 1 2 0 q ^ {1 / 2} + 7 0 5 2 4 q - 6 2 6 6 8 8 q ^ {3 / 2} \\ + 4 2 6 5 6 0 0 q ^ {2} + O (q ^ {5 / 2}), \end{array}\tag{50}
$$

$$
\begin{array}{c} \psi_ {T} (z) = q ^ {- 1} + 1 4 4 + 5 1 2 0 q ^ {1 / 2} + 7 0 5 2 4 q + 6 2 6 6 8 8 q ^ {3 / 2} \\ + 4 2 6 5 6 0 0 q ^ {2} + O (q ^ {5 / 2}), \end{array}\tag{51}
$$

$$
\begin{array}{c} \psi_ {S} (z) = - 1 0 2 4 0 q ^ {1 / 2} - 1 2 5 3 3 7 6 q ^ {3 / 2} - 4 8 3 2 8 7 0 4 q ^ {5 / 2} \\ - 1 0 5 9 0 7 8 1 4 4 q ^ {7 / 2} + O (q ^ {9 / 2}). \end{array}
$$

For$x \in \mathbb { R } ^ { 8 }$, define

$$
\begin{array}{l} b (x) := \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i \| x \| ^ {2} z} d z + \int_ {1} ^ {i} \psi_ {T} (z) e ^ {\pi i \| x \| ^ {2} z} d z \\ - 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i \| x \| ^ {2} z} d z - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) e ^ {\pi i \| x \| ^ {2} z} d z. \end{array}\tag{52}
$$

Now we prove that b satisfies condition (22).

Proposition 5. The function b defined by (52) belongs to the Schwartz space and satisfies

$$
\widehat {b} (x) = - b (x).
$$

Proof. Here, we repeat the arguments used in the proof of Proposition 1. First we show that b is a Schwartz function. We have

$$
\begin{array}{r l} & {\int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z = \int_ {0} ^ {i + 1} \psi_ {I} (z) e ^ {\pi i r ^ {2} (z - 1)} d z} \\ & {= \int_ {i \infty} ^ {- 1 / (i + 1)} \psi_ {I} \left(\frac {- 1}{z}\right) e ^ {\pi i r ^ {2} (- 1 / z - 1)} z ^ {- 2} d z = \int_ {i \infty} ^ {- 1 / (i + 1)} \psi_ {S} (z) z ^ {- 4} e ^ {\pi i r ^ {2} (- 1 / z - 1)} d z.} \end{array}
$$

There exists a positive constant C such that

$$
| \psi_ {S} (z) | \leq C e ^ {- \pi \operatorname{Im} z} \quad \mathrm{for} \operatorname{Im} z > \frac {1}{2}.
$$

Thus, as in the proof of Proposition 1, we estimate the first summand in the left-hand side of (52):

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
\begin{array}{l} \mathcal {F} (b) (x) = \int_ {- 1} ^ {i} \psi_ {T} (z) z ^ {- 4} e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})} d z + \int_ {1} ^ {i} \psi_ {T} (z) z ^ {- 4} e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})} d z \\ - 2 \int_ {0} ^ {i} \psi_ {I} (z) z ^ {- 4} e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})} d z - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) z ^ {- 4} e ^ {\pi i \| x \| ^ {2} (\frac {- 1}{z})} d z. \end{array}
$$

We make the change of variables$\begin{array} { r } { w = \frac { - 1 } { z } } \end{array}$and arrive at

$$
\begin{array}{l} \mathcal {F} (b) (x) = \int_ {1} ^ {i} \psi_ {T} \left(\frac {- 1}{w}\right) w ^ {2} e ^ {\pi i \| x \| ^ {2} w} d w + \int_ {- 1} ^ {i} \psi_ {T} \left(\frac {- 1}{w}\right) w ^ {2} e ^ {\pi i \| x \| ^ {2} w} d w \\ - 2 \int_ {i \infty} ^ {i} \psi_ {I} \left(\frac {- 1}{w}\right) w ^ {2} e ^ {\pi i \| x \| ^ {2} w} d w - 2 \int_ {i} ^ {0} \psi_ {S} \left(\frac {- 1}{w}\right) w ^ {2} e ^ {\pi i \| x \| ^ {2} w} d w. \end{array}
$$

Now we observe that the definitions (43)–(45) imply

$$
\psi_ {T} | _ {- 2} S = - \psi_ {T},
$$

$$
\psi_ {I} | _ {- 2} S = \psi_ {S},
$$

$$
\psi_ {S} | _ {- 2} S = \psi_ {I}.
$$

Therefore, we arrive at

$$
\begin{array}{l} \mathcal {F} (b) (x) = \int_ {1} ^ {i} - \psi_ {T} (z) e ^ {\pi i \| x \| ^ {2} z} d z + \int_ {- 1} ^ {i} - \psi_ {T} (z) e ^ {\pi i \| x \| ^ {2} z} d z \\ \qquad + 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) e ^ {\pi i \| x \| ^ {2} z} d z + 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i \| x \| ^ {2} w} d w. \end{array}
$$

Now from (52) we see that

$$
\mathcal {F} (b) (x) = - b (x).
$$

Now we regard the radial function b as a function on$\mathbb { R } _ { \geq 0 }$. We check that b has double roots at Λ -points.

Proposition 6. For$r > { \sqrt { 2 } } .$, the function$b ( r )$can be expressed as

$$
b (r) = - 4 \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {i \infty} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z.\tag{53}
$$

Proof. We denote the right-hand side of (53) by$c ( r )$. First, we check that $c ( r )$is well defined. We have

$$
\begin{array}{r l} \psi_ {I} (i t) = O (t ^ {2} e ^ {- \pi / t}) & \mathrm{as} t \to 0, \\ \psi_ {I} (i t) = O (e ^ {2 \pi t}) & \mathrm{as} t \to \infty . \end{array}
$$

Therefore, the integral (53) converges for$r > { \sqrt { 2 } } .$. Then we rewrite it in the following way:

$$
c (r) = \int_ {- 1} ^ {i \infty - 1} \psi_ {I} (z + 1) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i \infty} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {1} ^ {i \infty + 1} \psi_ {I} (z - 1) e ^ {\pi i r ^ {2} z} d z.
$$

From the Fourier expansion (49) we know that$\psi _ { I } ( z ) ~ = ~ e ^ { - 2 \pi i z } + O ( 1 )$as Im$( z ) \to \infty$. By assumption,$r ^ { 2 } > 2$. Hence we can deform the path of integration and write

(54)

$$
\int_ {- 1} ^ {i \infty - 1} \psi_ {I} (z + 1) e ^ {\pi i r ^ {2} z} d z = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z,\tag{55}
$$

$$
\int_ {1} ^ {i \infty + 1} \psi_ {I} (z - 1) e ^ {\pi i r ^ {2} z} d z = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {i} ^ {i \infty} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z.
$$

We have

$$
\begin{array}{l} c (r) = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z \\ \qquad + 2 \int_ {i} ^ {i \infty} (\psi_ {T} (z) - \psi_ {I} (z)) e ^ {\pi i r ^ {2} z} d z. \end{array}\tag{56}
$$

Next, we check that the functions$\psi _ { I } , \psi _ { T }$, and$\psi _ { S }$satisfy the following identity:

$$
\psi_ {T} + \psi_ {S} = \psi_ {I}.\tag{57}
$$

Indeed, from definitions (43)–(45), we get

$$
\begin{array}{c} \psi_ {T} + \psi_ {S} = (h - h | _ {- 2} S T) | _ {- 2} T + (h - h | _ {- 2} S T) | _ {- 2} S \\ = h | _ {- 2} T - h | _ {- 2} S T ^ {2} + h | _ {- 2} S - h | _ {- 2} S T S. \end{array}
$$

Note that$S T ^ { 2 } S$belongs to$\Gamma _ { 0 } ( 2 )$. Thus, since$h \in M _ { - 2 } ^ { ! } \Gamma _ { 0 } ( 2 )$we get

$$
\psi_ {T} + \psi_ {S} = h | _ {- 2} T - h | _ {- 2} S T S.
$$

Now we observe that T and$S T S ( S T ) ^ { - 1 }$are also in$\Gamma _ { 0 } ( 2 )$. Therefore,

$$
\psi_ {T} + \psi_ {S} = h | _ {- 2} T - h | _ {- 2} S T S = h - h | _ {- 2} S T = \psi_ {I}.
$$

Combining (56) and (57) we find

$$
\begin{array}{l} c (r) = \int_ {- 1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z + \int_ {1} ^ {i} \psi_ {T} (z) e ^ {\pi i r ^ {2} z} d z - 2 \int_ {0} ^ {i} \psi_ {I} (z) e ^ {\pi i r ^ {2} z} d z \\ - 2 \int_ {i} ^ {i \infty} \psi_ {S} (z) e ^ {\pi i r ^ {2} z} d z \\ = b (r). \end{array}
$$

At the end of this section we find another integral representation of$b ( r )$ for$r \in \mathbb { R } _ { \geq 0 }$and compute special values of b.

Proposition 7. For$r \geq 0$, we have

$$
b (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \left(\frac {1 4 4}{\pi r ^ {2}} + \frac {1}{\pi (r ^ {2} - 2)} + \int_ {0} ^ {\infty} \left(\psi_ {I} (i t) - 1 4 4 - e ^ {2 \pi t}\right) e ^ {- \pi r ^ {2} t} d t\right).\tag{58}
$$

The integral converges absolutely for all$r \in \mathbb { R } _ { \geq 0 }$

Proof. The proof is analogous to the proof of Proposition 3. First, suppose that$r > { \sqrt { 2 } }$. Then, by Proposition 6,

$$
b (r) = 4 i \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} \psi_ {I} (i t) e ^ {- \pi r ^ {2} t} d t.
$$

From (49) we obtain

$$
\psi_ {I} (i t) = e ^ {2 \pi t} + 1 4 4 + O (e ^ {- \pi t}) \quad \mathrm{as} t \to \infty .\tag{59}
$$

For$r > { \sqrt { 2 } } .$, we have

$$
\int_ {0} ^ {\infty} \left(e ^ {2 \pi t} + 1 4 4\right) e ^ {- \pi r ^ {2} t} d t = \frac {1}{\pi (r ^ {2} - 2)} + \frac {1 4 4}{\pi r ^ {2}}.\tag{60}
$$

Therefore, the identity (38) holds for$r > { \sqrt { 2 } }$

On the other hand, from the definition (52) we see that$b ( r )$is analytic in some neighborhood of$[ 0 , \infty )$. The asymptotic expansion (59) implies that the right-hand side of (58) is also analytic in some neighborhood of$[ 0 , \infty )$. Hence, the identity (58) holds on the whole interval$[ 0 , \infty )$. This finishes the proof of the proposition.

We see from (58) that$b ( r ) \in \ i \mathbb { R }$for all$r \in \mathbb { R } _ { \geq } 0$. Another immediate corollary of this proposition is

Proposition 8. We have

$$
b (0) = 0 \qquad b (\sqrt {2}) = 0 \qquad b ^ {\prime} (\sqrt {2}) = 2 \sqrt {2} \pi i.\tag{61}
$$

## 5. Proof of Theorem 3

Finally, we are ready to prove Theorem 3.

Theorem 4. The function

$$
g (x) := \frac {\pi i}{8 6 4 0} a (x) + \frac {i}{2 4 0 \pi} b (x)
$$

satisfies conditions$( 3 ) \AA - ( 5 )$. Moreover, the values$g ( x )$and${ \widehat { g } } ( x )$do not vanish for all vectors x with$\| x \| ^ { 2 } \notin 2 \mathbb { Z } _ { > 0 }$

Proof. First, we prove that (3) holds. By Propositions 2 and 6 we know that for$r > { \sqrt { 2 } }$2

$$
g (r) = \frac {\pi}{2 1 6 0} \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} A (t) e ^ {- \pi r ^ {2} t} d t,\tag{62}
$$

where

$$
A (t) = - t ^ {2} \phi_ {0} (i / t) - \frac {3 6}{\pi^ {2}} \psi_ {I} (i t).
$$

![](images/page_19_image_0.jpg)

Figure 1. Plot of the functions A(t),$\begin{array} { r } { A _ { 0 } ^ { ( 2 ) } ( t ) = - \frac { 3 6 8 6 4 0 } { \pi ^ { 2 } } t ^ { 2 } e ^ { - \pi / t } . } \end{array}$ and$\begin{array} { r } { A _ { \infty } ^ { ( 1 ) } ( t ) = - \frac { 7 2 } { \pi ^ { 2 } } e ^ { 2 \pi t } + \frac { 8 6 4 0 } { \pi } t - \frac { 2 3 3 2 8 } { \pi ^ { 2 } } . } \end{array}$

Our goal is to show that$A ( t ) < 0$for$t \in ( 0 , \infty )$. The function$A ( t )$is plotted in Figure 1. We observe that we can compute the values of$A ( t )$for $t \in ( 0 , \infty )$with any given precision. Indeed, from identities (29) and (45) we obtain the following two presentations for$A ( t )$

$$
\begin{array}{l} A (t) = - t ^ {2} \phi_ {0} (i / t) + \frac {3 6}{\pi^ {2}} t ^ {2} \psi_ {S} (i / t), \\ A (t) = - t ^ {2} \phi_ {0} (i t) + \frac {1 2}{\pi} t \phi_ {- 2} (i t) - \frac {3 6}{\pi^ {2}} \phi_ {- 4} (i t) - \frac {3 6}{\pi^ {2}} \psi_ {I} (i t). \end{array}
$$

For an integer$n \geq 0$, let$A _ { 0 } ^ { ( n ) }$and$A _ { \infty } ^ { ( n ) }$be the functions such that

(63)

$$
A (t) = A _ {0} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n / t}) \mathrm{as} t \to 0,\tag{64}
$$

$$
A (t) = A _ {\infty} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n t}) \quad \mathrm{as} t \to \infty .
$$

For each$n \geq 0$, we can compute these functions from the Fourier expansions (32)–(34), (49), and (51). For example, from (32)–(34) and (49) we compute

$$
\begin{array}{l} A _ {\infty} ^ {(6)} (t) = - \frac {7 2}{\pi^ {2}} e ^ {2 \pi t} - \frac {2 3 3 2 8}{\pi^ {2}} + \frac {1 8 4 3 2 0}{\pi^ {2}} e ^ {- \pi t} - \frac {5 1 9 4 3 6 8}{\pi^ {2}} e ^ {- 2 \pi t} + \frac {2 2 5 6 0 7 6 8}{\pi^ {2}} e ^ {- 3 \pi t} \\ \qquad - \frac {2 5 0 5 8 3 0 4 0}{\pi^ {2}} e ^ {- 4 \pi t} + \frac {8 6 9 9 1 6 6 7 2}{\pi^ {2}} e ^ {- 5 \pi t} \\ \qquad + t \left(\frac {8 6 4 0}{\pi} + \frac {2 4 3 6 4 8 0}{\pi} e ^ {- 2 \pi t} + \frac {1 1 3 0 1 1 2 0 0}{\pi} e ^ {- 4 \pi t}\right) \\ \qquad - t ^ {2} \left(5 1 8 4 0 0 e ^ {- 2 \pi t} + 3 1 1 0 4 0 0 0 e ^ {- 4 \pi t}\right). \end{array}
$$

From (32)–(34) and (51) we compute

$$
\begin{array}{r} A _ {0} ^ {(6)} (t) = t ^ {2} \Big (- \frac {3 6 8 6 4 0}{\pi^ {2}} e ^ {- \pi / t} - 5 1 8 4 0 0 e ^ {- 2 \pi / t} - \frac {4 5 1 2 1 5 3 6}{\pi^ {2}} e ^ {- 3 \pi / t} \\ - 3 1 1 0 4 0 0 0 e ^ {- 4 \pi / t} - \frac {1 7 3 9 8 3 3 3 4 4}{\pi^ {2}} e ^ {- 5 \pi / t} \Big). \end{array}
$$

Moreover, from the convergent asymptotic expansion for the Fourier coeficients of a weakly holomorphic modular form [3, Prop. 1.12], we find that the n-th Fourier coeficient$c _ { \psi _ { I } } ( n )$of$\psi _ { I }$satisfies

$$
| c _ {\psi_ {I}} (n) | \leq e ^ {4 \pi \sqrt {n}}, \qquad n \in \frac {1}{2} \mathbb {Z} _ {> 0}.\tag{65}
$$

Similar inequalities hold for the Fourier coeficients of$\psi _ { S } , \phi _ { 0 } , \phi _ { - 2 }$, and$\phi _ { - 4 } \mathrm { : }$

(66)

$$
| c _ {\psi_ {S}} (n) | \leq 2 e ^ {4 \pi \sqrt {n}}, \qquad n \in \frac {1}{2} \mathbb {Z} _ {> 0},\tag{67}
$$

$$
| c _ {\phi_ {0}} (n) | \leq 2 e ^ {4 \pi \sqrt {n}}, \qquad n \in \mathbb {Z} _ {> 0},\tag{68}
$$

$$
| c _ {\phi_ {- 2}} (n) | \leq e ^ {4 \pi \sqrt {n}}, \qquad n \in \mathbb {Z} _ {> 0},\tag{69}
$$

$$
| c _ {\phi_ {- 4}} (n) | \leq e ^ {4 \pi \sqrt {n}}, \qquad n \in \mathbb {Z} _ {> 0}.
$$

Therefore, we can estimate the error terms in the asymptotic expansions (63) and (64) of A(t)

$$
\left| A (t) - A _ {0} ^ {(m)} (t) \right| \leq \left(t ^ {2} + \frac {3 6}{\pi^ {2}}\right) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n / t},
$$

$$
\left| A (t) - A _ {\infty} ^ {(m)} (t) \right| \leq \left(t ^ {2} + \frac {1 2}{\pi} t + \frac {3 6}{\pi^ {2}}\right) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n t}.
$$

For an integer$m \geq 0$, we set

$$
R _ {0} ^ {(m)} := \left(t ^ {2} + \frac {3 6}{\pi^ {2}}\right) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n / t},
$$

$$
R _ {\infty} ^ {(m)} := \left(t ^ {2} + \frac {1 2}{\pi} t + \frac {3 6}{\pi^ {2}}\right) \sum_ {n = m} ^ {\infty} 2 e ^ {2 \sqrt {2} \pi \sqrt {n}} e ^ {- \pi n t}.
$$

Using interval arithmetic we check that

$$
\left| R _ {0} ^ {(6)} (t) \right| \leq \left| A _ {0} ^ {(6)} (t) \right| \quad \text { for } t \in (0, 1 ],
$$

$$
\left| R _ {\infty} ^ {(6)} (t) \right| \leq \left| A _ {\infty} ^ {(6)} (t) \right| \quad \text { for } t \in [ 1, \infty),
$$

$$
A _ {0} ^ {(6)} (t) <   0 \qquad \mathrm{for} t \in (0, 1 ],
$$

$$
A _ {\infty} ^ {(6)} (t) <   0 \qquad \text { for } t \in [ 1, \infty).
$$

Thus, we see that$A ( t ) < 0$for$t \in ( 0 , \infty )$. Then identity (62) implies (3).

Next, we prove (4). By Propositions 3 and 7 we know that for$r > 0$2

$$
\widehat {g} (r) = \frac {\pi}{2 1 6 0} \sin (\pi r ^ {2} / 2) ^ {2} \int_ {0} ^ {\infty} B (t) e ^ {- \pi r ^ {2} t} d t,\tag{70}
$$

where

$$
B (t) = - t ^ {2} \phi_ {0} (i / t) + \frac {3 6}{\pi^ {2}} \psi_ {I} (i t).
$$

This function can also be written as

$$
\begin{array}{l} {B (t) = - t ^ {2} \phi_ {0} (i / t) - \frac {3 6}{\pi^ {2}} t ^ {2} \psi_ {S} (i / t),} \\ {B (t) = - t ^ {2} \phi_ {0} (i t) + \frac {1 2}{\pi} t \phi_ {- 2} (i t) - \frac {3 6}{\pi^ {2}} \phi_ {- 4} (i t) + \frac {3 6}{\pi^ {2}} \psi_ {I} (i t).} \end{array}
$$

Our aim is to prove that$B ( t ) > 0$for$t \in ( 0 , \infty )$. A plot of$B ( t )$is given in Figure 2. For$n \geq 0$, let$B _ { 0 } ^ { ( n ) }$and$B _ { \infty } ^ { ( n ) }$be the functions such that

$$
\begin{array}{r l} {B (t) = B _ {0} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n / t})} & {\mathrm{as} t \to 0,} \\ {B (t) = B _ {\infty} ^ {(n)} (t) + O (t ^ {2} e ^ {- \pi n t})} & {\mathrm{as} t \to \infty .} \end{array}
$$

![](images/page_21_chart_8.jpg)

Figure 2. Plot of the functions B(t),$\begin{array} { r } { B _ { 0 } ^ { ( 2 ) } ( t ) = \frac { 3 6 8 6 4 0 } { \pi ^ { 2 } } t ^ { 2 } e ^ { - \pi / t } } \end{array}$，and$\begin{array} { r } { B _ { \infty } ^ { ( 1 ) } ( t ) = \frac { 8 6 4 0 } { \pi } t - \frac { 2 3 3 2 8 } { \pi ^ { 2 } } } \end{array}$

We find

$$
\begin{array}{l} B _ {\infty} ^ {(6)} (t) = - \frac {1 2 9 6 0}{\pi^ {2}} - \frac {1 8 4 3 2 0}{\pi^ {2}} e ^ {- \pi t} - \frac {1 1 6 6 4 0}{\pi^ {2}} e ^ {- 2 \pi t} - \frac {2 2 5 6 0 7 6 8}{\pi^ {2}} e ^ {- 3 \pi t} \\ \qquad + \frac {5 6 5 4 0 1 6 0}{\pi^ {2}} e ^ {- 4 \pi t} - \frac {8 6 9 9 1 6 6 7 2}{\pi^ {2}} e ^ {- 5 \pi t} \\ \qquad + t \left(\frac {8 6 4 0}{\pi} + \frac {2 4 3 6 4 8 0}{\pi} e ^ {- 2 \pi t} + \frac {1 1 3 0 1 1 2 0 0}{\pi} e ^ {- 4 \pi t}\right) \\ \qquad - t ^ {2} (5 1 8 4 0 0 e ^ {- 2 \pi t} + 3 1 1 0 4 0 0 0 e ^ {- 4 \pi t}) \end{array}
$$

and

$$
\begin{array}{r l} B _ {0} ^ {(6)} (t) = t ^ {2} \left(\frac {3 6 8 6 4 0}{\pi^ {2}} e ^ {- \pi / t} - 5 1 8 4 0 0 e ^ {- 2 \pi / t} \right. & \\ \left. + \frac {4 5 1 2 1 5 3 6}{\pi^ {2}} e ^ {- 3 \pi / t} - 3 1 1 0 4 0 0 0 e ^ {- 4 \pi / t} + \frac {1 7 3 9 8 3 3 3 4 4}{\pi^ {2}} e ^ {- 5 \pi / t}\right). \end{array}
$$

The estimates (65)–(69) imply that

$$
\left| B (t) - B _ {0} ^ {(6)} (t) \right| \leq R _ {0} ^ {(6)} (t) \quad \text { for } t \in (0, 1 ]
$$

and

$$
\left| B (t) - B _ {\infty} ^ {(6)} (t) \right| \leq R _ {\infty} ^ {(6)} (t) \quad \text { for } t \in [ 1, \infty).
$$

Using interval arithmetic, we verify that

$$
\begin{array}{r l} \left| R _ {0} ^ {(6)} (t) \right| \leq \left| B _ {0} ^ {(6)} (t) \right| & \text {for} t \in (0, 1 ], \\ \left| R _ {\infty} ^ {(6)} (t) \right| \leq \left| B _ {\infty} ^ {(6)} (t) \right| & \text {for} t \in [ 1, \infty), \\ B _ {0} ^ {(6)} (t) > 0 & \text {for} t \in (0, 1 ], \\ B _ {\infty} ^ {(6)} (t) > 0 & \text {for} t \in [ 1, \infty). \end{array}
$$

Now identity (70) implies (4).

Finally, property (5) readily follows from Propositions 4 and 8. This finishes the proof of Theorems 4 and 3.

Acknowledgments. I thank Andriy Bondarenko for suggesting that I work on this problem. Also I am grateful to Danilo Radchenko for his valuable ideas and his help with numerical computations. I am most grateful to J. Kramer, A. Mellit, J. M. Sullivan, G. M. Ziegler, and anonymous referees for their valuable comments and suggestions on the manuscript.

## References

[1] M. Abramowitz and I. Stegun, Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, Appl. Math. Ser. 55, Dover Publ., New York, 1964. Zbl 0171.38503.

[2] A. Bondarenko, D. Radchenko, and M. Viazovska, Optimal asymptotic bounds for spherical designs, Ann. of Math. 178 (2013), 443–452. MR 3071504. Zbl 1270.05026. https://doi.org/10.4007/annals.2013.178.2.2.

[3] J. H. Bruinier, Borcherds Products on O(2, l) and Chern Classes of Heegner Divisors, Lecture Notes in Math. 1780, Springer-Verlag, New York, 2002. MR 1903920. Zbl 1004.11021. https://doi.org/10.1007/b83278.

[4] H. Cohn and N. Elkies, New upper bounds on sphere packings. I, Ann. of Math. 157 (2003), 689–714. MR 1973059. Zbl 1041.52011. https://doi.org/10.4007/annals.2003.157.689.

[5] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007), 99–148. MR 2257398. Zbl 1198.52009. https://doi.org/10.1090/S0894-0347-06-00546-7.

[6] J. H. Conway and N. A. Sloane, What are all the best sphere packings in low dimensions?, Discrete Comput. Geom. 13 (1995), 383–403. MR 1318784. Zbl 0844.52013. https://doi.org/10.1007/BF02574051.

[7] P. Delsarte, Bounds for unrestricted codes, by linear programming, Philips Res. Rep. 27 (1972), 272–289. MR 0314545. Zbl 0348.94016.

[8] P. Delsarte, J. M. Goethals, and J. J. Seidel, Spherical codes and designs, Geometriae Dedicata 6 (1977), 363–388. MR 0485471. Zbl 0376.05015. https://doi.org/10.1007/BF03187604.

[9] F. Diamond and J. Shurman, A First Course in Modular Forms, Graduate Texts in Math. 228, Springer-Verlag, New York, 2005. MR 2112196. Zbl 1062. 11022.

[10] L. Fejes, Uber die dichteste Kugellagerung, <sup>¨</sup> Math. Z. 48 (1943), 676–684. MR 0009129. Zbl 0027.34102. https://doi.org/10.1007/BF01180035.

[11] T. C. Hales, A proof of the Kepler conjecture, Ann. of Math. 162 (2005), 1065–1185. MR 2179728. Zbl 1096.52010. https://doi.org/10.4007/annals.2005.162.1065.

[12] D. A. Hejhal, The Selberg Trace Formula for PSL(2, R). Vol. 2, Lecture Notes in Math. 1001, Springer-Verlag, New York, 1983. MR 0711197. Zbl 0543.10020. https://doi.org/10.1007/BFb0061302.

[13] V. I. Levenshtein, Bounds for codes ensuring error correction and synchronization, Problemy Peredaˇci Informacii 5 (1969), 3–13. MR 0305908. Zbl 0261. 94016.

[14] D. Mumford, Tata Lectures on Theta. I, Progr. Math. 28, Birkh¨auser, Boston, 1983. MR 0688651. Zbl 0509.14049. https://doi.org/10.1007/978-1-4899-2843-6.

[15] H. Petersson, Uber die Entwicklungskoefizienten der automorphen Formen,<sup>¨</sup> Acta Math. 58 (1932), 169–215. MR 1555346. Zbl 0003.35002. https://doi.org/10.1007/BF02547776.

[16] F. Pfender and G. M. Ziegler, Kissing numbers, sphere packings, and some unexpected proofs, Notices Amer. Math. Soc. 51 (2004), 873–883. MR 2145821. Zbl 1168.52305.

[17] H. Rademacher and H. S. Zuckerman, On the Fourier coeficients of certain modular forms of positive dimension, Ann. of Math. 39 (1938), 433–462. MR 1503417. Zbl 0019.02201. https://doi.org/10.2307/1968796.

[18] A. Thue, Uber die dichteste Zusammenstellung von kongruenten Kreisen in einer<sup>¨</sup> Ebene, Norske Vid. Selsk. Skr. 1 (1910), 1–9. JFM 41.0594.19.

[19] D. Zagier, Elliptic modular forms and their applications, in The 1-2-3 of Modular Forms, Universitext, Springer-Verlag, New York, 2008, pp. 1–103. MR 2409678. Zbl 1259.11042. https://doi.org/10.1007/978-3-540-74119-0 1.

(Received: April 8, 2016) (Revised: December 18, 2016)

Berlin Mathematical School and Humboldt University of Berlin,

Berlin<sub>,</sub> Germany

Current address : Ecole Polytechnique F <sup>´</sup> ed<sup>´</sup> erale de Lausanne, <sup>´</sup>

Lausanne<sub>,</sub> Switzerland

E-mail : viazovska@gmail.com