# The connective constant of the honeycomb lattice equals$\sqrt { 2 + { \sqrt { 2 } } }$

Hugo Duminil-Copin and Stanislav Smirnov

## Abstract

We provide the first mathematical proof that the connective constant of the hexagonal lattice is equal to${ \sqrt { 2 + { \sqrt { 2 } } } } .$. This value has been derived non rigorously by B. Nienhuis in 1982, using Coulomb gas approach from theoretical physics. Our proof uses a parafermionic observable for the self avoiding walk, which satisfies a half of the discrete Cauchy-Riemann relations. Establishing the other half of the relations (which conjecturally holds in the scaling limit) would also imply convergence of the self-avoiding walk to SLE(8/3).

## 1 Introduction

A famous chemist P. Flory [3] proposed to consider self-avoiding (i.e. visiting every vertex at most once) walks on a lattice as a model for polymer chains. Self-avoiding walks turned out to be a very interesting object, leading to rich mathematical theories and challenging questions, see [4].

Denote by$c _ { n }$the number of n-step self-avoiding walks on the hexagonal lattice H started from some fixed vertex, e.g. the origin. Elementary bounds on$c _ { n }$(for instance ${ \sqrt { 2 } } ^ { n } \leq c _ { n } \leq 3 \cdot 2 ^ { n - 1 } )$guarantee that$c _ { n }$grows exponentially fast. Since a$( n + m )$)-step self-avoiding walk can be uniquely cut into a n-step self-avoiding walk and a parallel translation of a m-step self-avoiding walk, we infer that

$$
c _ {n + m} \leq c _ {n} c _ {m},
$$

from which it follows that there exists$\mu \in ( 0 , + \infty )$such that

$$
\mu := \lim _ {n \to \infty} c _ {n} ^ {\frac {1}{n}}.
$$

The positive real number$\mu$is called the connective constant of the hexagonal lattice.

Using Coulomb gas formalism, B. Nienhuis [8, 9] proposed physical arguments for$\mu$ to have the value$\sqrt { 2 + { \sqrt { 2 } } }$. We rigorously prove this statement. While our methods are diferent from those applied by Nienhuis, they are similarly motivated by considerations of vertex operators in the$O ( n )$model. Our methods do not directly apply to the square lattice, for which the value of the connective constant is diferent and currently unknown.

Theorem 1 For the hexagonal lattice,

$$
\mu = \sqrt {2 + \sqrt {2}}.
$$

It will be convenient to consider walks between mid-edges of H, i.e. centers of edges of H (the set of mid-edges will be denoted by H). We will write$\gamma : a  E$if a walk$\gamma$ starts at a and ends at some mid-edge of$E \subset H$. In the case$E = \{ b \}$, we simply write $\gamma : a  b$. The length$\ell ( \gamma )$of the walk is the number of vertices visited by$\gamma .$

We will work with the partition function

$$
Z (x) = \sum_ {\gamma : a \to H} x ^ {\ell (\gamma)} \quad \in (0, + \infty ].
$$

This sum does not depend on the choice of$^ { a , }$and is increasing in x. Establishing the identity$\mu = \sqrt { 2 + \sqrt { 2 } }$is equivalent to showing that$Z ( x ) = + \infty$for$x > 1 / { \sqrt { 2 + { \sqrt { 2 } } } }$and $Z ( x ) < + \infty$for$x < 1 / { \sqrt { 2 + { \sqrt { 2 } } } }$. To this end, we analyze walks restricted to bounded domains and weighted depending on their winding. The modified sum can be defined as a parafermionic observable arising from a disorder operator. Such observables exist for other models, see [1, 2, 11].

The paper is organized as follows. In Section 2, the parafermionic observable is introduced and its key property is derived. Section 3 contains the proof of Theorem 1. Section 4 discusses conformal invariance conjectures for self-avoiding walks. To simplify formulæ, below we set$x _ { c } : = 1 / \sqrt { 2 + \sqrt { 2 } }$and$j = \mathrm { e } ^ { \mathrm { i } 2 \pi / 3 }$

## 2 Parafermionic observable

A (hexagonal lattice) domain$\Omega \subset H$is a union of all mid-edges emanating from a given collection of vertices$V ( \Omega )$(see Fig. 1): a mid-edge z belongs to Ω if at least one end-point of its associated edge is in Ω, it belongs to ∂Ω if only one of them is in Ω. We further assume Ω to be simply connected, i.e. having a connected complement.

For a self-avoiding walk$\gamma$between mid-edges a and b (not necessarily the start and the end), we define its winding$\mathrm { W } _ { \gamma } ( a , b )$as the total rotation of the direction in radians when$\gamma$is traversed from a to$b ,$see Fig. 1.

Our main tool is given by the following

Definition 1 The parafermionic observable for$a \in \partial \Omega , z \in \Omega$, is defined by

$$
F (z) = F (a, z, x, \sigma) = \sum_ {\gamma \subset \Omega : a \to z} \mathrm{e} ^ {- \mathrm{i} \sigma \mathrm{W} _ {\gamma} (a, z)} x ^ {\ell (\gamma)}.
$$

Lemma 1$I f x = x _ { c }$and$\textstyle \sigma = { \frac { 5 } { 8 } }$, then$F$satisfies the following relation for every vertex $v \in V ( \Omega )$

$$
(p - v) F (p) + (q - v) F (q) + (r - v) F (r) = 0,\tag{1}
$$

where$p , q , r$are the mid-edges of the three edges adjacent to$v$.

![](images/page_2_image_0.jpg)

Figure 1: Left. A domain Ω with boundary mid-edges labeled by small black squares, and vertices of V(Ω) labeled by circles. Right. Winding of a curve$\gamma$

Note that with$\sigma = 5 / 8$, the complex weight$\mathrm { e } ^ { - \mathrm { i } \sigma \mathrm { W } _ { \gamma } ( a , z ) }$can be interpreted as a product of terms λ or$\bar { \lambda }$per left or right turn of$\gamma$drawn from a to z, with

$$
\lambda = \exp \left(- \mathrm{i} \frac {5}{8} \cdot \frac {\pi}{3}\right) = \exp \left(- \mathrm{i} \frac {5 \pi}{2 4}\right).
$$

Proof We start by choosing notation so that$p , q$and$r$follow counter-clockwise around v. Note that the left-hand side of (1) can be expanded into the sum of contributions$c ( \gamma )$ of all possible walks$\gamma$finishing at$p , q$or r. For instance, if a walk ends at the mid-edge $p ,$its contribution will be given by

$$
c (\gamma) = (p - v) \cdot \mathrm{e} ^ {- \mathrm{i} \sigma \mathrm{W} _ {\gamma} (a, p)} x _ {c} ^ {\ell (\gamma)}.
$$

One can partition the set of walks$\gamma$finishing at$p , q$or r into pairs and triplets of walks in the following way, see Fig 2:

• If a walk$\gamma _ { 1 }$visits all three mid-edges$p , q , r .$, it means that the edges belonging to $\gamma _ { 1 }$form a disjoint self-avoiding path plus (up to a half-edge) a self-avoiding loop from v to$v .$One can associate to$\gamma _ { 1 }$the walk passing through the same edges, but exploring the loop from v to v in the other direction. Hence, walks visiting the three mid-edges can be grouped in pairs.

• If a walk$\gamma _ { 1 }$visits only one mid-edge, it can be associated to two walks$\gamma _ { 2 }$and$\gamma _ { 3 }$ that visit exactly two mid-edges by prolonging the walk one step further (there are two possible choices). The reverse is true: a walk visiting exactly two mid-edges is naturally associated to a walk visiting only one mid-edge by erasing the last step. Hence, walks visiting one or two mid-edges can be grouped in triplets.

If one can prove that the sum of contributions to (1) of each pair or triplet vanishes, then their total sum is zero, and (1) holds.

Let$\gamma _ { 1 }$and$\gamma _ { 2 }$be two associated walks as in the first case. Without loss of generality, we may assume that$\gamma _ { 1 }$ends at$q$and$\gamma _ { 2 }$ends at r. Note that$\gamma _ { 1 }$and$\gamma _ { 2 }$coincide up to the mid-edge p, and then follow an almost complete loop in two opposite directions. It follows that

$$
\ell (\gamma_ {1}) = \ell (\gamma_ {2}) \qquad \text {and} \qquad \left\{ \begin{array}{l} \mathrm{W} _ {\gamma_ {1}} (a, q)   =   \mathrm{W} _ {\gamma_ {1}} (a, p)   +   \mathrm{W} _ {\gamma_ {1}} (p, q)   =   \mathrm{W} _ {\gamma_ {1}} (a, p)   -   \frac {4 \pi}{3} \\ \mathrm{W} _ {\gamma_ {2}} (a, r)   =   \mathrm{W} _ {\gamma_ {2}} (a, p)   +   \mathrm{W} _ {\gamma_ {2}} (p, r)   =   \mathrm{W} _ {\gamma_ {1}} (a, p)   +   \frac {4 \pi}{3} \end{array} \right..
$$

In order to evaluate the winding of$\gamma _ { 1 }$between p and q above, we used the fact that a is on the boundary and Ω is simply connected. We conclude that

$$
\begin{array}{c} c (\gamma_ {1}) + c (\gamma_ {2}) = (q - v) \mathrm{e} ^ {- \mathrm{i} \sigma \mathrm{W} _ {\gamma_ {1}} (a, q)} x _ {c} ^ {\ell (\gamma_ {1})} + (r - v) \mathrm{e} ^ {- \mathrm{i} \sigma \mathrm{W} _ {\gamma_ {2}} (a, r)} x _ {c} ^ {\ell (\gamma_ {2})} \\ = (p - v) \mathrm{e} ^ {- \mathrm{i} \sigma \mathrm{W} _ {\gamma_ {1}} (a, p)} x _ {c} ^ {\ell (\gamma_ {1})} \left(j \bar {\lambda} ^ {4} + \bar {j} \lambda^ {4}\right) = 0 \end{array}
$$

where the last equality holds since$j \bar { \lambda } ^ { 4 } = - i$by our choice of$\lambda = \exp ( - \mathrm { i } 5 \pi / 2 4 )$

Let$\gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 }$be three walks matched as in the second case. Without loss of generality, we assume that$\gamma _ { 1 }$ends at$p$and that$\gamma _ { 2 }$and$\gamma _ { 3 }$extend$\gamma _ { 1 }$to q and r respectively. As before, we easily find that

$$
\ell (\gamma_ {2}) = \ell (\gamma_ {3}) = \ell (\gamma_ {1}) + 1 \qquad \mathrm{and} \qquad \left\{ \begin{array}{l l} \mathrm{W} _ {\gamma_ {2}} (a, r) = \mathrm{W} _ {\gamma_ {2}} (a, p) + \mathrm{W} _ {\gamma_ {2}} (p, q) = \mathrm{W} _ {\gamma_ {1}} (a, p) - \frac {\pi}{3} \\ \mathrm{W} _ {\gamma_ {3}} (a, r) = \mathrm{W} _ {\gamma_ {3}} (a, p) + \mathrm{W} _ {\gamma_ {3}} (p, r) = \mathrm{W} _ {\gamma_ {1}} (a, p) + \frac {\pi}{3} \end{array} \right.
$$

Plugging these values into the respective contributions, we obtain

$$
c (\gamma_ {1}) + c (\gamma_ {2}) + c (\gamma_ {3}) = (p - v) \mathrm{e} ^ {- \mathrm{i} \sigma \mathrm{W} _ {\gamma_ {1}} (a, p)} x _ {c} ^ {\ell (\gamma_ {1})} \left(1 + x _ {c} j \bar {\lambda} + x _ {c} \bar {j} \lambda\right) = 0.
$$

Above is the only place where we use that x takes its critical value, i.e.$x _ { c } ^ { - 1 } = { \sqrt { 2 + { \sqrt { 2 } } } } =$ (2 cos <sup>π</sup> ).

The claim of the lemma follows readily by summing over all pairs and triplets. 

![](images/page_3_image_11.jpg)

Figure 2: Left: a pair of walks visiting all the three mid-edges emanating from v and difering by rearranged connections at v. Right: a triplet of walks, one visiting one mid-edge, the two others visiting two mid-edges, and obtained by prolonging the first one through v.

Remark 1 Coeficients in (1) are three cube roots of unity multiplied by$p - v ,$, so its left-hand side can be seen as a discrete dz-integral along an elementary contour on the dual lattice. The fact that the integral of the parafermionic observable along discrete contours vanishes suggests that it is discrete holomorphic and that self-avoiding walks have a conformally invariant scaling limit, see Section$\it 4 .$

## 3 Proof of Theorem 1

Counting argument in a strip domain. We consider a vertical strip domain$S _ { T }$ composed of$T$strips of hexagons, and its finite version$S _ { T , L }$cut at heights$\pm L$at angles $\pm \pi / 3$, see Fig. 3. Namely, position a hexagonal lattice H of meshsize 1 in$\mathbb { C } \operatorname { s o }$that there exists a horizontal edge e with mid-edge a being 0. Then

$$
V (S _ {T}) = \{z \in V (\mathbb {H}): 0 \leq \operatorname{Re} (z) \leq \frac {3 T + 1}{2} \},
$$

$$
V (S _ {T, L}) = \{z \in V (S _ {T}): | \sqrt {3} \operatorname{Im} (z) - \operatorname{Re} (z) | \leq 3 L \}.
$$

Denote by$\alpha$the left boundary of$S _ { T }$, by$\beta$the right one. Symbols ε and$\bar { \varepsilon }$denote the top and bottom boundaries of$S _ { T , L }$. Introduce the following (positive) partition functions:

$$
A _ {T, L} ^ {x} := \sum_ {\gamma \subset S _ {T, L}: a \to \alpha \backslash \{a \}} x ^ {\ell (\gamma)}, B _ {T, L} ^ {x} := \sum_ {\gamma \subset S _ {T, L}: a \to \beta} x ^ {\ell (\gamma)}, E _ {T, L} ^ {x} := \sum_ {\gamma \subset S _ {T, L}: a \to \varepsilon \cup \overline {{\varepsilon}}} x ^ {\ell (\gamma)}.
$$

In the next lemma, we deduce from relation (1) a global identity without the complex weights.

![](images/page_4_image_7.jpg)

Figure 3: Domain$S _ { T , L }$and boundary intervals α,$\beta , \varepsilon$and$\bar { \varepsilon } .$

Lemma 2 For critical$\boldsymbol { x } = \boldsymbol { x } _ { c } ,$the following identity holds

$$
1 = c _ {\alpha} A _ {T, L} ^ {x _ {c}} + B _ {T, L} ^ {x _ {c}} + c _ {\varepsilon} E _ {T, L} ^ {x _ {c}},\tag{2}
$$

with positive coeficients$c _ { \alpha } = \cos \left( { \frac { 3 \pi } { 8 } } \right)$and$\begin{array} { r } { c _ { \varepsilon } = \cos \left( \frac { \pi } { 4 } \right) } \end{array}$

Proof Sum the relation (1) over all vertices in$V ( S _ { T , L } )$. Values at interior mid-edges disappear and we arrive at the identity

$$
0 = - \sum_ {z \in \alpha} F (z) + \sum_ {z \in \beta} F (z) + j \sum_ {z \in \varepsilon} F (z) + \bar {j} \sum_ {z \in \bar {\varepsilon}} F (z).\tag{3}
$$

The symmetry of our domain implies that$F ( \bar { z } ) = \bar { F } ( z )$, where ¯x denotes the complex conjugate of x. Observe that the winding of any self-avoiding walk from a to the bottom part of α is −π while the winding to the top part is π. Thus

$$
\begin{array}{l} \sum_ {z \in \alpha} F (z) = F (a) + \sum_ {z \in \alpha \setminus \{a \}} F (z) = F (a) + \frac {1}{2} \sum_ {z \in \alpha \setminus \{a \}} (F (z) + F (\bar {z})) \\ \qquad = 1 + \frac {\mathrm{e} ^ {- \mathrm{i} \sigma \pi} + \mathrm{e} ^ {\mathrm{i} \sigma \pi}}{2} A _ {T, L} ^ {x} = 1 - \cos \left(\frac {3 \pi}{8}\right) A _ {T, L} ^ {x} = 1 - c _ {\alpha} A _ {T, L} ^ {x}. \end{array}
$$

Above we have used the fact that the only walk from a to a is a trivial one of length 0, and so$F ( a ) = 1$. Similarly, the winding from a to any half-edge in$\beta$(resp. ε and ¯ε) is 0 (resp.$\frac { 2 \pi } { 3 }$and$- \frac { 2 \pi } { 3 } )$, therefore

$$
\sum_ {z \in \beta} F (z) = B _ {T, L} ^ {x} \quad \mathrm{and} \quad j \sum_ {z \in \varepsilon} F (z) + \bar {j} \sum_ {z \in \bar {\varepsilon}} F (z) = \cos \left(\frac {\pi}{4}\right) E _ {T, L} ^ {x} = c _ {\varepsilon} E _ {T, L} ^ {x}.
$$

The lemma follows readily by plugging the last three formulæ into (3).

Observe that sequences$( A _ { T , L } ^ { x } ) _ { L > 0 }$and$( B _ { T , L } ^ { x } ) _ { L > 0 }$are increasing in$L$and are bounded for$x \leq x _ { c }$thanks to (2) and their monotonicity in x. Thus they have limits

$$
A _ {T} ^ {x} := \lim _ {L \to \infty} A _ {T, L} ^ {x} = \sum_ {\gamma \subset S _ {T}: a \to \alpha \setminus \{a \}} x ^ {\ell (\gamma)}, \quad B _ {T} ^ {x} := \lim _ {L \to \infty} B _ {T, L} ^ {x} = \sum_ {\gamma \subset S _ {T}: a \to \beta} x ^ {\ell (\gamma)}.
$$

Identity (2) then implies that$( E _ { T , L } ^ { x _ { c } } ) _ { L > 0 }$decreases and converges to a limit$\begin{array} { l l } { E _ { T } ^ { x _ { c } } } & { = } \end{array}$ $\mathrm { l i m } _ { L \to \infty } E _ { T , L } ^ { x _ { c } }$. Passing to a limit in (2), we arrive at

$$
1 = c _ {\alpha} A _ {T} ^ {x _ {c}} + B _ {T} ^ {x _ {c}} + c _ {\varepsilon} E _ {T} ^ {x _ {c}}.\tag{4}
$$

Proof of Theorem 1 We start by proving that$Z ( x _ { c } ) = + \infty$, and hence$\mu \geq \sqrt { 2 + \sqrt { 2 } }$ Suppose that for some$T , E _ { T } ^ { x _ { c } } > 0$. As noted before,$E _ { T , L } ^ { x _ { c } }$decreases in$L$and so

$$
Z (x _ {c}) \geq \sum_ {L > 0} E _ {T, L} ^ {x _ {c}} \geq \sum_ {L > 0} E _ {T} ^ {x _ {c}} = + \infty ,
$$

which completes the proof.

Assuming on the contrary that$E _ { T } ^ { x _ { c } } = 0$for all$T _ { \ast }$, we simplify (4) to

$$
1 = c _ {\alpha} A _ {T} ^ {x _ {c}} + B _ {T} ^ {x _ {c}}.\tag{5}
$$

Observe that a walk$\gamma$entering into the count of$A _ { T + 1 } ^ { x _ { c } }$and not into$A _ { T } ^ { x _ { c } }$has to visit some vertex adjacent to the right edge of$S _ { T + 1 }$. Cutting$\gamma$at the first such point (and adding half-edges to the two halves), we uniquely decompose it into two walks crossing$S _ { T + 1 }$ (these walks are usually called bridges), which together are one step longer than$\gamma$. We conclude that

$$
A _ {T + 1} ^ {x _ {c}} - A _ {T} ^ {x _ {c}} \leq x _ {c} \left(B _ {T + 1} ^ {x _ {c}}\right) ^ {2}.\tag{6}
$$

Combining (5) for two consecutive values of$T$with (6), we can write

$$
\begin{array}{r l} & 0 = 1 - 1 = (c _ {\alpha} A _ {T + 1} ^ {x _ {c}} + B _ {T + 1} ^ {x _ {c}}) - (c _ {\alpha} A _ {T} ^ {x _ {c}} + B _ {T} ^ {x _ {c}}) \\ & \quad = c _ {\alpha} (A _ {T + 1} ^ {x _ {c}} - A _ {T} ^ {x _ {c}}) + B _ {T + 1} ^ {x _ {c}} - B _ {T} ^ {x _ {c}} \leq c _ {\alpha} x _ {c} (B _ {T + 1} ^ {x _ {c}}) ^ {2} + B _ {T + 1} ^ {x _ {c}} - B _ {T} ^ {x _ {c}}, \end{array}
$$

and so

$$
c _ {\alpha} x _ {c} \left(B _ {T + 1} ^ {x _ {c}}\right) ^ {2} + B _ {T + 1} ^ {x _ {c}} \geq B _ {T} ^ {x _ {c}}.
$$

It follows easily by induction, that

$$
B _ {T} ^ {x _ {c}} \geq \min [ B _ {1} ^ {x _ {c}}, 1 / (c _ {\alpha} x _ {c}) ] / T
$$

for every$T \geq 1$, and therefore

$$
Z (x _ {c}) \geq \sum_ {T > 0} B _ {T} ^ {x _ {c}} = + \infty .
$$

This completes the proof of the estimate$\mu \geq x _ { c } ^ { - 1 } = \sqrt { 2 + \sqrt { 2 } }$

It remains to prove the opposite inequality$\mu \leq x _ { c } ^ { - 1 }$. To estimate the partition function from above, we will decompose self-avoiding walks into bridges. A bridge of width$T$is a self-avoiding walk in$S _ { T }$from one side to the opposite side, defined up to vertical translation. The partition function of bridges of width T is$B _ { T } ^ { x }$, which is at most 1 by (4). Noting that a bridge of width T has length at least$T _ { i }$, we obtain for$x < x _ { c }$

$$
B _ {T} ^ {x} \leq \left(\frac {x}{x _ {c}}\right) ^ {T} B _ {T} ^ {x _ {c}} \leq \left(\frac {x}{x _ {c}}\right) ^ {T}.
$$

Thus, for$x < x _ { c } ,$the series$\textstyle \sum _ { T > 0 } B _ { T } ^ { x }$converges and so does the product$\textstyle \prod _ { T > 0 } ( 1 + B _ { T } ^ { x } )$ Let us assume for the moment the following fact: any self-avoiding walk can be canonically decomposed into a sequence of bridges of widths$T _ { - i } < \cdots < T _ { - 1 }$and$T _ { 0 } > \cdots > T _ { j }$, and, if one fixes the starting mid-edge and the first vertex visited, the decomposition uniquely determines the walk. Such decomposition was first introduced by Hammersley and Welsh in [5] (for a modern treatment, see Section 3.1 of [4]). Applying the decomposition to walks starting at a (the first visited vertex is 0 or -1), we can estimate

$$
Z(x)\leq 2\sum_{\substack{T_{-i} <   \dots <  T_{-1}\\ T_{j} <   \dots <  T_{0}}}\left(\prod_{k = -i}^{j}B_{T_{k}}^{x}\right) = 2\prod_{T > 0}(1 + B_{T}^{x})^{2} <   \infty .
$$

The factor 2 is due to the fact that there are two possibilities for the first vertex once we fix the starting mid-edge. Therefore,$Z ( x ) < + \infty$whenever$x < x _ { c }$and$\mu \leq x _ { c } ^ { - 1 } = \sqrt { 2 + \sqrt { 2 } }$

![](images/page_7_image_0.jpg)

Figure 4: Left: Decomposition of a half-plane walk into four bridges with widths$8 > 3 >$ $1 > 0$. The first bridge corresponds to the maximal bridge containing the origin. Note that the decomposition contains one bridge of width 0. Right: The reverse procedure. If the starting mid-edge and the first vertex are fixed, the decomposition is unambiguous.

To complete the proof of the theorem it only remains to prove that such a decomposition into bridges does exist. Once again, this fact is well-known [4, 5], but we include the proof for completeness.

First assume that$\tilde { \gamma }$is a half-plane self-avoiding walk, meaning that the start of$\tilde { \gamma }$ has extremal real part: we prove by induction on the width$T _ { 0 }$that the walk admits a canonical decomposition into bridges of widths$T _ { 0 } > \cdots > T _ { j }$. Without loss of generality, we assume that the start has minimal real part. Out of the vertices having the maximal real part, choose the one visited last, say after n steps. The n first vertices of the walk form a bridge$\tilde { \gamma } _ { 1 }$of width$T _ { 0 }$, which is the first bridge of our decomposition when prolonged to the mid-edge on the right of the last vertex. We forget about the$( n + 1 )$)-th vertex, since there is no ambiguity in its position. The consequent steps form a half-plane walk$\tilde { \gamma } _ { 2 }$of width$T _ { 1 } < T _ { 0 }$. Using the induction hypothesis, we know that$\tilde { \gamma } _ { 2 }$admits a decomposition into bridges of widths$T _ { 1 } > \cdots > T _ { j }$The decomposition of$\tilde { \gamma }$is created by adding$\tilde { \gamma } _ { 1 }$ before the decomposition of$\tilde { \gamma } _ { 2 }$

If the walk is a reverse half-plane self-avoiding walk, meaning that the end has extremal real part, we set the decomposition to be the decomposition of the reverse walk in the reverse order. If$\gamma$is a self-avoiding walk in the plane, one can cut the trajectory into two pieces$\gamma _ { 1 }$and$\gamma _ { 2 } \colon$the vertices of$\gamma$up to the first vertex of maximal real part, and the remaining vertices. The decomposition of$\gamma$is given by the decomposition of$\gamma _ { 1 }$(with widths$T _ { - i } < \cdots < T _ { - 1 } )$plus the decomposition of$\gamma _ { 2 }$(with widths$T _ { 0 } > \cdots > T _ { j } )$

Once the starting mid-edge and the first vertex are given, it is easy to check that the decomposition uniquely determines the walk by exhibiting the reverse procedure, see Fig. 4 for the case of half-plane walks.

Remark 2 The proof provides bounds for the number of bridges from a to the right side

of the strip of width T, namely,

$$
\frac {c}{T} \leq B _ {T} ^ {x _ {c}} \leq 1.
$$

In paragraphs 3.3.3 and 3.4.3 of$[ 6 ]$, precise behaviors are conjectured for the number of self-avoiding walks between two points on the boundary of a domain, which yields the following (conjectured) estimate:

$$
\sum_ {\gamma \subset S _ {T}: 0 \to T + \mathrm{i} y T} x _ {c} ^ {\ell (\gamma)} \approx T ^ {- 5 / 4} H (0, 1 + \mathrm{i} y) ^ {5 / 4}
$$

where H is the boundary derivative of the Poisson kernel. Integrating with respect to$y ,$ we obtain that$B _ { T } ^ { x _ { c } }$should decay as$T ^ { - 1 / 4 }$when$T$goes to infinity. Similar estimates are conjectured for walks in$S _ { T }$from 0 to iyT.

## 4 Conjectures

In [8, 9], Nienhuis proposed a more precise asymptotical behavior for the number of self-avoiding walks:

$$
c _ {n} \sim A n ^ {\gamma - 1} \sqrt {2 + \sqrt {2}} ^ {n},\tag{7}
$$

with$\gamma = 4 3 / 3 2$. Here the symbol ∼ means that the ratio of two sides is of the order$n ^ { o ( 1 ) }$ or perhaps even tends to a constant. Moreover, Nienhuis gave arguments in support of Flory’s prediction that the mean-square displacement$\langle | \gamma ( n ) | ^ { 2 } \rangle$satisfies

$$
\langle | \gamma (n) | ^ {2} \rangle = \frac {1}{c _ {n}} \sum_ {\gamma n - \mathrm{stepSAW}} | \gamma (n) | ^ {2} = n ^ {2 \nu + o (1)},\tag{8}
$$

with$\nu = 3 / 4$. Despite the precision of the predictions (7) and (8), the best rigorously known bounds are very far apart and almost 50 years old (see [4] for an exposition). The derivation of these exponents seems to be one of the most challenging problems in probability.

It was shown by G. Lawler, O. Schramm and W. Werner in [6] that$\gamma$and ν could be computed if the self-avoiding walk would posses a conformally invariant scaling limit. More precisely, let$\Omega \neq \mathbb { C }$be a simply connected domain in the complex plane C with two points a and b on the boundary. For$\delta > 0$, we consider the discrete approximation given by the largest finite domain$\Omega _ { \delta }$of δH included in Ω, and$a _ { \delta }$and$b _ { \delta }$to be the vertices of $\Omega _ { \delta }$closest to a and b respectively. A probability measure$\mathbb { P } _ { x , \delta }$is defined on the set of self-avoiding trajectories$\gamma$between$a _ { \delta }$and$b _ { \delta }$that remain in$\Omega _ { \delta }$by assigning to$\gamma$a weight proportional to$x ^ { \ell ( \gamma ) }$. We obtain a random curve denoted$\gamma _ { \delta }$. Conjectured conformal invariance of self-avoiding walks can be stated as follows, see [6]:

Conjecture 1 Let Ω be a simply connected domain (not equal to$\mathbb { C } )$with two distinct points a, b on its boundary. For$\boldsymbol { x } = \boldsymbol { x } _ { c }$, the law$o f \gamma _ { \delta }$in$\left( \Omega _ { \delta } , a _ { \delta } , b _ { \delta } \right)$converges when$\delta \to 0$ to the (chordal) Schramm-Loewner Evolution with parameter$\kappa = 8 / 3$in Ω from a to b.

As discussed in [7, 10], to prove convergence of a random curve to SLE it is suficient to find a discrete observable with a conformally covariant scaling limit.

Thus it would sufice to show that a normalized version of$F _ { \delta }$has a conformally invariant scaling limit, which can be achieved by showing that it is holomorphic and has prescribed boundary values.

As discussed in [11], the winding of an interface leading to a boundary edge z is uniquely determined, and coincides with the winding of the boundary itself. Thus one can say that$F _ { \delta }$satisfies a discrete version of the following Riemann boundary value problem (a homogeneous version of the Riemann-Hilbert-Privalov BVP):

$$
\mathrm{Im} \left(F (z) \cdot (\mathrm{tangentto} \partial \Omega) ^ {5 / 8}\right) = 0, z \in \partial \Omega ,\tag{9}
$$

with a singularity at a. Note that the problem above has conformally covariant solutions (as$( d z ) ^ { 5 / 8 } \mathrm { - f o r m s ) }$, and so is well defined even in domains with fractal boundaries.

As noted in Remark 1, relation (1) amounts to saying that discrete contour integrals of$F _ { \delta }$vanish. So any (subsequential) scaling limit of$F _ { \delta }$would have to be holomorphic. Unfortunately, relation (1) alone, is unsuficient to deduce the existence of such a limit, unlike in the Ising case [2]. The reason is that for a domain with$E$edges, (1) imposes $\approx { \scriptstyle { \frac { 2 } { 3 } } } E$relations (one per vertice) for$E$values of$F _ { \delta }$, making it impossible to reconstruct $F _ { \delta }$from its boundary values. So$F _ { \delta }$is not exactly holomorphic, it can be rather thought of as a divergence-free vector field, which seems to have non-trivial curl. However, we expect that in the limit the curl vanishes, which is equivalent to$F _ { \delta } ( z )$having the same limit regardless of the orientation of the edge z.

The Riemann BVP (9) is easily solved, and we arrive at the following conjecture:

Conjecture 2 Let Ω be a simply connected domain (not equal to$\mathbb { C } )$, let$z \in \Omega$, and let a, b be two distinct points on the boundary of Ω. We assume that the boundary of Ω is smooth near b. For$\delta > 0$, let$F _ { \delta }$be the holomorphic observable in the domain$\left( \Omega _ { \delta } , a _ { \delta } \right)$ approximating$( \Omega , a )$, and let$z _ { \delta }$be the closest point in$\Omega _ { \delta }$to$z .$. Then

$$
\lim _ {\delta \rightarrow 0} \frac {F _ {\delta} (z _ {\delta})}{F _ {\delta} (b _ {\delta})} = \left(\frac {\phi^ {\prime} (z)}{\phi^ {\prime} (b)}\right) ^ {5 / 8}\tag{10}
$$

where$\Phi$is a conformal map from Ω to the upper half-plane mapping a to ∞ and b to$\it 0 .$

The right-hand side of (10) is well-defined, since the conformal map$\phi$is unique up to multiplication by a real factor. Proving this conjecture would be a major step toward Conjecture 1 and the derivation of critical exponents.

Acknowledgements. The authors would like to thank G. Slade for useful comments on the manuscript, and G. Lawler for suggesting Remark 2. This research was supported by the EU Marie-Curie RTN CODY, the ERC AG CONFRA, as well as by the Swiss FNS. The second author was partially supported by the Chebyshev Laboratory (Department of Mathematics and Mechanics, St.-Petersburg State University) under RF governement grant 11.G34.31.0026

## References

[1] J. Cardy and Y. Ikhlef, Discretely holomorphic parafermions and integrable loop models, J. Phys. A 42(10), 102001 11 pages (2009).

[2] D. Chelkak and S. Smirnov, Universality in the 2D Ising model and conformal invariance of fermionic observables. Invent. Math., to appear. Preprint, arXiv:0910.2045 (2009).

[3] P. Flory, Principles of Polymer Chemistry, Cornell University Press. ISBN: 0-8014-0134-8 (1953).

[4] N. Madras and G. Slade, Self-avoiding walks, Probability and its Applications. Birkh¨auser Boston, Inc. Boston, MA (1993).

[5] J. M. Hammersley and D. J. A. Welsh, Further results on the rate of convergence to the connective constant of the hypercubical lattice. Quart. J. Math. Oxford Ser. (2) 13 108–110 (1962).

[6] G. Lawler, O. Schramm and W. Werner, On the scaling limit of planar self-avoiding walk. Fractal Geometry and applications: a jubilee of Benoˆıt Mandelbrot, Part 2, 339–364. Proc. Sympos. Pure. Math. 72, Part 2, Amer. Math. Soc. Providence, RI (2004).

[7] G. Lawler, O. Schramm and W. Werner, Conformal invariance of planar loop-erased random walks and uniform spanning trees. Ann. Probab., 32(1B) 939–995 (2004).

[8] B. Nienhuis, Exact critical point and critical exponents of O(n) models in two dimensions. Phys. Rev. Lett. 49 1062–1065 (1982).

[9] B. Nienhuis, Critical behavior of two-dimensional spin models and charge asymmetry in the Coulomb gas. J. Stat. Phys. 34 731–761 (1984).

[10] S. Smirnov, Towards conformal invariance of 2D lattice models. International Congress of Mathematicians, Eur. Math. Soc., Z¨urich, Vol. II 1421–1451 (2006).

[11] S. Smirnov, Discrete complex analysis and probability. Rajendra Bhatia (ed.) et al., Proceedings of the International Congress of Mathematicians (ICM), Hyderabad, India, August 19–27, 2010, Volume I: Plenary lectures. New Delhi, World Scientific. (2010).