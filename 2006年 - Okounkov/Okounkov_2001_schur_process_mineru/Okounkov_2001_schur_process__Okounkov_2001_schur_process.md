# Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram

Andrei Okounkov and Nikolai Reshetikhin∗

## Abstract

Schur process is a time-dependent analog of the Schur measure on partitions studied in [16]. Our first result is that the correlation functions of the Schur process are determinants with a kernel that has a nice contour integral representation in terms of the parameters of the process. This general result is then applied to a particular specialization of the Schur process, namely to random 3-dimensional Young diagrams. The local geometry of a large random 3-dimensional diagram is described in terms of a determinantal point process on a 2-dimensional lattice with the incomplete beta function kernel (which generalizes the discrete sine kernel). A brief discussion of the universality of this answer concludes the paper.

## 1 Introduction

## 1.1 Schur measure and Schur process

## 1.1.1

This paper is a continuation of [16]. The Schur measure, introduced in [16], is a measure on partitions λ which weights a partitions λ proportionally to $s _ { \lambda } ( X ) s _ { \lambda } ( Y )$, where$s _ { \lambda }$is the Schur function and X and Y are two sets of variables.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>∗</sup>Department of Mathematics, University of California at Berkeley, Evans Hall #3840, Berkeley, CA 94720-3840. E-mail: okounkov@math.berkeley.edu, reshetik@math.berkeley.edu</span></small>

Here we consider a time-dependent version of the Schur measure which we call the Schur process, see Definition 2. This is a measure on sequences {<sup>λ(t)</sup>} <sup>such</sup> <sup>that</sup>

$$
\operatorname{Prob} (\{\lambda (t) \}) \propto \prod \mathsf {S} ^ {(t)} (\lambda (t), \lambda (t + 1)),
$$

where the time-dependent weight$\mathsf { S } ^ { ( t ) } ( \lambda , \mu )$is a certain generalization of a skew Schur function. It is given by a suitably regularized infinite minor of a certain Toeplitz matrix. This determinants can be also interpreted as a Karlin-McGregor non-intersection probability [12]. The distribution of each individual λ(t) is then a Schur measure with suitable parameters.

In this paper, we consider the Schur process only in discrete time, although a continuous time formulation is also possible, see Section 2.2.11.

The idea to make the Schur measure time dependent was inspired, in part, by the paper [10] which deals with some particular instances of the general concept of the Schur processes introduced here. For another development of the ideas of [10], see the paper [18] which appeared after the results of the present paper were obtained.

## 1.1.2

Our main interest in this paper are the correlation functions of the Schur process which, by definition, are the probabilities that the random set

$$
\mathfrak {S} (\{\lambda (t) \}) = \left\{(t, \lambda (t) _ {i} - i + \frac {1}{2}) \right\}, \quad t, i \in Z,
$$

contains a given set$U \subset \mathbb { Z } \times ( \mathbb { Z } + { \frac { 1 } { 2 } } )$

Using the same infinite wedge machinery as in [16] we prove that the correlation functions of the Schur process have a determinantal form

$$
\operatorname{Prob} \left(U \subset \mathfrak {S} (\{\lambda (t) \})\right) = \det \left(K (u _ {i}, u _ {j})\right) _ {u _ {i}, u _ {j} \in U},
$$

and give an explicit contour integral representation for the correlation kernel K, see Theorem 1. This theorem is a generalization of Theorem 2 in [16].

## 1.2 Asymptotics

## 1.2.1

The contour integral representation for correlation kernel is particularly convenient for asymptotic investigations. Only very elementary means, namely residue calculus and basic saddle-point analysis are needed to derive the asymptotics.

## 1.2.2

We illustrate this in Section 3 by computing explicitly the correlation functions asymptotics for 3-dimensional Young diagram in the bulk of their limit shape. Three-dimensional diagrams, also known as plane partition, is an old subject which has received recently a lot of attention. More specifically, the measure on 3D diagrams π such that

$$
\mathrm{Prob} (\pi) \propto q ^ {| \pi |}, \quad 0 <   q <   1,\tag{1}
$$

where$| \pi |$is the volume of$\pi ,$is a particular specialization of the Schur process for which the time parameter has the meaning of an extra spatial dimension. $\operatorname { A s } q \to 1$, a typical partition, suitably scaled, approaches a limit shape which was described in [3] and can be seen in Figure 7 below. The existence of this limit shape and some of its properties were first established by A. Vershik [19], who used direct combinatorial methods.

It is well known that 3D diagrams are in bijection with certain rhombi tiling of the plane, see for example Section 2.3.6 below. Local statistics of random domino tilings have been the subject of intense recent studies, see for example [2, 4, 5, 13] and the survey [14].

The authors of [5] computed local correlations for domino tilings with periodic boundary conditions and conjectured that the same formula holds in the thermodynamic limit for domino tilings of more general regions, see Conjecture 13.5 in [5].

From the point of view of statistical mechanics, the argument behind this conjecture can be the belief that in the thermodynamic limit and away from the boundary the local correlations depend only on macroscopic parameters, such as the density of tiles of a given kind. In particular, in the case of 3D diagrams the densities of rhombi of each of the 3 possible kinds are uniquely fixed by the tilt of the limit shape at the point in question.

## 1.2.3

In this paper, we approach the local geometry of random 3D diagrams using the general exact formulas for correlation functions of the Schur process. For 3D diagrams, these general formulas specialize to contour integrals involving the quantum dilogarithm function (24), see Corollary 1.

We compute the q  1 limit of the correlation kernel explicitly. The result turns out to be the discrete incomplete beta kernel, see Theorem 2. One can show, see Section 3.1.12, that this kernel is a specialization of the kernel of [5] when one of the parameters vanishes in agreement with Conjecture 13.5 of [5].

The incomplete beta kernel is also a bivariate generalization of the discrete sine kernel which appeared in [1] in the situation of the Plancherel specialization of the Schur measure, see also [10].

## 1.3 Universality

Although we focus on one specific asymptotic problem, our methods are both very basic and completely general. They should apply, therefore, with little or no modification in a much wider variety of situations yielding the same or analogous results. In other words, both the methods and the results should be universal in a large class of asymptotic problems.

As explained in Section 3.2.3, this universality should be especially robust for the equal time correlations, in which case the discrete sine kernel should appear. This is parallel to the situation with random matrices [9].

## 1.4 Acknowledgments

We are grateful to R. Kenyon and A. Vershik for fruitful discussions. A.O. was partially supported by NSF grant DMS-0096246 and a Sloan foundation fellowship. N. R. was partially supported by NSF grant DMS-0070931. Both authors were partially supported by CRDF grant RM1-2244.

## 2 Schur process

## 2.1 Configurations

## 2.1.1

Recall that a partition is a sequence

$$
\lambda = \left(\lambda_ {1} \geq \lambda_ {2} \geq \lambda_ {3} \geq \dots \geq 0\right)
$$

of integers such that$\lambda _ { i } = 0$for$i \gg 0$. The zero, or empty, partition is denoted by . The book [15] is a most comprehensive reference on partitions and symmetric functions.

Schur process is a measure on sequences

$$
\{\lambda (t) \}, \quad t \in \mathbb {Z},
$$

where each$\lambda ( t )$is a partition and$\lambda ( t ) = \varnothing$for$| t | \gg 0$. We call the variable t the time, even though it may have a diferent interpretation in applications.

## 2.1.2

An example of such an object is a plane partition which, by definition, is a 2-dimensional array of nonnegative numbers

$$
\pi = (\pi_ {i j}), \quad i, j = 1, 2, \ldots ,
$$

that are nonincreasing as function of both i and$j$and such that

$$
| \pi | = \sum \pi_ {i j}
$$

is finite. The plot of the function

$$
(x, y) \mapsto \pi_ {\lceil x \rceil , \lceil y \rceil}, \quad x, y > 0,
$$

is a 3-dimensional Young diagram with volume$| \pi |$. For example, Figure 1 shows the 3D diagram corresponding to the plane partition

$$
\pi = \left( \begin{array}{c c c c} 5 & 3 & 2 & 1 \\ 4 & 3 & 1 & 1 \\ 3 & 2 & 1 \\ 2 & 1 \end{array} \right),\tag{2}
$$

where the entries that are not shown are zero.

![](images/page_5_image_0.jpg)

Figure 1: A 3-dimensional diagram$\pi$

We associate to$\pi$the sequence$\{ \lambda ( t ) \}$of its diagonal slices, that is, the sequence of partitions

$$
\lambda (t) = (\pi_ {i, t + i}), \quad i \geq \max (0, - t).\tag{3}
$$

It is easy to see that a configuration$\{ \lambda ( t ) \}$corresponds to a plane partition if and only if it satisfies the conditions

$$
\dots \prec \lambda (- 2) \prec \lambda (- 1) \prec \lambda (0) \succ \lambda (1) \succ \lambda (2) \succ \dots ,\tag{4}
$$

where$\lambda \succ \mu$means that λ and$\mu$interlace, that is,

$$
\lambda_ {1} \geq \mu_ {1} \geq \lambda_ {2} \geq \mu_ {2} \geq \lambda_ {3} \geq \dots .
$$

In particular, the configuration λ(t) corresponding to the diagram (2) is

$$
(2) \prec (3, 1) \prec (4, 2) \prec (5, 3, 1) \succ (3, 1) \succ (2, 1) \succ (1).
$$

## 2.1.3

The mapping

$$
\lambda \mapsto \mathfrak {S} (\lambda) = \{\lambda_ {i} - i + \frac {1}{2} \} \subset \mathbb {Z} + \frac {1}{2}
$$

is a bijection of the of the set of partitions and the set$\mathfrak { S }$of subsets${ \mathfrak { S } } \subset \mathbb { Z } + { \frac { 1 } { 2 } }$ such that

$$
| \mathfrak {S} \setminus (\mathbb {Z} + \frac {1}{2}) _ {<   0} | = | (\mathbb {Z} + \frac {1}{2}) _ {<   0} \setminus \mathfrak {S} | <   \infty .
$$

The mapping

$$
\{\lambda (t) \} \mapsto \mathfrak {S} (\{\lambda (t) \}) = \{(t, \lambda (t) _ {i} - i + \frac {1}{2}) \} \subset \mathbb {Z} \times (\mathbb {Z} + \frac {1}{2}),\tag{5}
$$

identifies the configurations of the Schur process with certain subsets of$\mathbb { Z } \times$ $( \mathbb { Z } + { \frac { 1 } { 2 } } )$. In other words, the mapping (5) makes the Schur process a random point field on$\mathbb { Z } \times ( \mathbb { Z } + { \frac { 1 } { 2 } } )$

For example, the subset$\mathfrak { S } ( \{ \lambda ( t ) \} )$corresponding to the 3D diagram from Figure 1 is shown in Figure 2. One can also visualize$\mathfrak { S } ( \{ \lambda ( t ) \} )$as a collection of nonintersecting paths as in Figure 2.

![](images/page_6_chart_4.jpg)

Figure 2: Point field and nonintersecting paths corresponding to the diagram in Figure 1

## 2.2 Probabilities

## 2.2.1

Schur process, the formal definition of which is given in Definition 2 below, is a measure on sequences$\{ \lambda ( t ) \}$such that

$$
\mathrm{Prob} (\{\lambda (t) \}) \propto \prod_ {t \in \mathbb {Z}} \mathsf {S} ^ {(t)} (\lambda (t), \lambda (t + 1)),
$$

where$\mathsf { S } ^ { ( t ) } ( \mu , \lambda )$is a certain time-dependent transition weight between the partition$\mu$and λ which will be defined presently.

The coeficient$\mathsf { S } ^ { ( t ) } ( \mu , \lambda )$is a suitably regularized infinite minor of a certain Toeplitz matrix. It can be viewed as a generalization of the Jacobi-Trudy determinant for a skew Schur function or as a form of Karlin-McGregor non-intersection probability [12].

## 2.2.2

Let a function

$$
\phi (z) = \sum_ {k \in \mathbb {Z}} \phi_ {k} z ^ {k},
$$

be nonvanishing on the unit circle$| z | = 1$with winding number 0 and geometric mean 1. These two conditions mean that log$\phi$is a well defined function with mean 0 on the unit circle. For simplicity, we additionally assume that $\phi$is analytic in some neighborhood of the unit circle. Many of the results below hold under weaker assumptions on$\phi$as can be seen, for example, by an approximation argument. We will not pursue here the greatest analytic generality.

## 2.2.3

Given two subsets

$$
X = \{x _ {i} \}, Y = \{y _ {i} \} \in \mathfrak {S},
$$

we wish to assign a meaning to the following infinite determinant:

$$
\det \left(\phi_ {y _ {i} - x _ {j}}\right).\tag{6}
$$

We will see that, even though there is no canonical way to evaluate this determinant, diferent regularizations difer by a constant which depends only on$\phi$and not on$X$and$Y$.

Since our goal is to define probabilities only up to a constant factor, it is clear that diferent regularizations lead to the same random process.

## 2.2.4

The function$\phi$admits a Wiener-Hopf factorization of the form

$$
\phi (z) = \phi^ {+} (z) \phi^ {-} (z)
$$

where the functions

$$
\phi^ {\pm} (z) = 1 + \sum_ {k \in \pm \mathbb {N}} \phi_ {k} ^ {\pm} z ^ {k}
$$

are analytic and nonvanishing in some neighborhood of the interior (resp., exterior) of the unit disk.

There is a special case when the meaning of (6) in unambiguous, namely, if$\phi ^ { - } ( z ) = 1 \ : ( \mathrm { o r } \ : \phi ^ { + } ( z ) = 1 )$then the matrix is almost unitriangular and the determinant in (6) is essentially a finite determinant. This determinant is then a Jacobi-Trudy determinant for a skew Schur function

$$
\det \left(\phi_ {\lambda_ {i} - \mu_ {j} + j - i} ^ {+}\right) = s _ {\lambda / \mu} (\phi^ {+}),
$$

where$s _ { \lambda / \mu } ( \phi ^ { + } )$is the skew Schur function$s _ { \lambda / \mu }$specialized so that

$$
h _ {k} = \phi_ {k} ^ {+},\tag{7}
$$

where$h _ { k }$are the complete homogeneous symmetric functions. Note that

$$
s _ {\lambda / \mu} (\phi^ {+}) = 0, \quad \mu \not \subset \lambda .\tag{8}
$$

## 2.2.5

Definition 1. We define the transition weight by the following formula

$$
S _ {\phi} (\mu , \lambda) = \sum_ {\nu} s _ {\mu / \nu} (\phi^ {-}) s _ {\lambda / \nu} (\phi^ {+}),\tag{9}
$$

where$s _ { \lambda / \nu } ( \phi ^ { + } )$is defined by (7) and$s _ { \mu / \nu } ( \phi ^ { - } )$is the skew Schur function$s _ { \mu / \nu }$ specialized so that

$$
h _ {k} = \phi_ {- k} ^ {-}.
$$

Note that if the determinant det$\left( \phi _ { \lambda _ { i } - \mu _ { j } + j - i } \right)$were unambiguously defined and satisfied the Cauchy-Binet formula then it would equal (9) because

$$
\left(\phi_ {i - j}\right) = \left(\phi_ {i - j} ^ {+}\right) \left(\phi_ {i - j} ^ {-}\right).
$$

Also note that because of (8) the sum in (9) is finite, namely, it ranges over all ν such that$\nu \subset \mu , \lambda$

## 2.2.6

In what follows, we will assume that the reader is familiar with the basics of the infinite wedge formalism, see for example Chapter 14 of the book [11] by V. Kac. An introductory account of this formalism, together with some probablistic applications, can be found in the lectures [17]. We will use the notation conventions of the appendix to [16] summarized for the reader’s convenience in the appendix to this paper.

Consider the following vertex operators

$$
\Gamma_ {\pm} (\phi) = \exp \left(\sum_ {k = 1} ^ {\infty} (\log \phi) _ {\mp k} \alpha_ {\pm k}\right),
$$

where$( \log \phi ) _ { k }$denotes the coeficient of$z ^ { k }$in the Laurent expansion of log$\phi ( z )$. In particular, if the algebra of symmetric functions is specialized as in (7) then

$$
(\log \phi) _ {k} = \frac {p _ {k}}{k}, \quad k = 1, 2, 3, \ldots ,
$$

where$p _ { k }$is the kth power-sum symmetric function.

It is well known, see for example Exercise 14.26 in [11], that the matrix coeficient of the operators$\Gamma _ { \pm }$are the skew Schur functions, namely

$$
(\Gamma_ {-} (\phi) v _ {\mu}, v _ {\lambda}) = s _ {\lambda / \mu} (\phi^ {+}).
$$

It follows that

$$
\mathsf {S} _ {\phi} (\mu , \lambda) = \left(\Gamma_ {-} (\phi) \Gamma_ {+} (\phi) v _ {\mu}, v _ {\lambda}\right).\tag{10}
$$

It is clear from the commutation relation

$$
\Gamma_ {+} (\phi) \Gamma_ {-} (\phi) = e ^ {\sum k (\log \phi) _ {k} (\log \phi) _ {- k}} \Gamma_ {-} (\phi) \Gamma_ {+} (\phi)\tag{11}
$$

that diferent ordering prescriptions in (10), which produce diferent regularizations of (6), all difer by a constant independent of$\mu$and λ.

## 2.2.7

Now suppose that for any half-integer$m \in \mathbb { Z } + { \frac { 1 } { 2 } }$we choose, independently, a function

$$
\phi [ m ] (z) = \sum_ {k \in \mathbb {Z}} \phi_ {k} [ m ] z ^ {k}
$$

as above so that the series

$$
\sum_ {m \in \mathbb {Z}} \log \phi [ m ] (z)
$$

converges absolutely and uniformly in some neighborhood of the unit disk. This assumption is convenient but can be weakened. The functions$\phi [ m ]$will be the parameters of the Schur process.

Definition 2. The probabilities of the Schur process are given by

$$
\operatorname{Prob} (\{\lambda (t) \}) = \frac {1}{Z} \prod_ {m \in \mathbb {Z} + 1 / 2} \mathsf {S} _ {\phi [ m ]} \left(\lambda (m - \frac {1}{2}), \lambda (m + \frac {1}{2})\right),
$$

where the transition weight$\mathsf { S } _ { \phi }$is defined in Definition 1 and Z is the normalizing factor (partition function)

$$
Z = \sum_ {\{\lambda (t) \}} \prod_ {m \in \mathbb {Z} + 1 / 2} \mathsf {S} _ {\phi [ m ]} \left(\lambda (m - \frac {1}{2}), \lambda (m + \frac {1}{2})\right).
$$

## 2.2.8

It follows from (10) that Z is given by the following matrix coeficient

$$
Z = \left(\prod_ {m \in \mathbb {Z} + 1 / 2} ^ {\leftarrow} \Gamma_ {-} (\phi [ m ])   \Gamma_ {+} (\phi [ m ])   v _ {\emptyset}, v _ {\emptyset}\right)  ,\tag{12}
$$

where$\overleftarrow { \prod }$denotes the time-ordered product, that is, the product in which operators are ordered from right to left in the increasing time order.

Using (11) and the following consequence of (43)

$$
\Gamma_ {+} (\phi) v _ {\emptyset} = v _ {\emptyset}.\tag{13}
$$

we compute the matrix coeficient (12) as follows

$$
Z = \exp \left(\sum_ {m _ {1} <   m _ {2}} \sum_ {k} k (\log \phi [ m _ {1} ]) _ {k} (\log \phi [ m _ {2} ]) _ {- k}\right).
$$

Our growth assumptions on the functions$\phi [ m ]$ensure the convergence of$Z$

## 2.2.9

It is clear from the vertex-operator description that

$$
\operatorname{Prob} (\lambda (t) = \mu) \propto s _ {\mu} \left(\prod_ {m <   t} \phi^ {+} [ m ]\right) s _ {\mu} \left(\prod_ {m > t} \phi^ {-} [ m ]\right),\tag{14}
$$

where, for example, the first factor is the image of the Schur function under the specialization that sets$h _ { k }$to the coeficient of$z ^ { k }$in the product of $\phi ^ { + } [ m ] ( z )$over$m < t$

This means that the distribution of each individual$\lambda ( t )$is a Schur measure [16] with parameters (14).

## 2.2.10

More generally, the restriction of the Schur process to any subset of times is again a Schur process with suitably modified parameters. Specifically, let a subset

$$
\left\{t _ {k} \right\} \subset \mathbb {Z}, \quad k \in \mathbb {Z},
$$

be given and consider the restriction of the Schur process to this set, that is, consider the process

$$
\{\widetilde {\lambda} (k) \} = \{\lambda (t _ {k}) \}.
$$

It follows from the vertex operator description that this is again a Schur process with parameters

$$
\widetilde {\phi} [ l ] = \prod_ {t _ {l - \frac {1}{2}} <   m <   t _ {l + \frac {1}{2}}} \phi [ m ], \quad l, m \in \mathbb {Z} + \frac {1}{2}.
$$

The case of a finite set$\{ t _ { k } \}$is completely analogous and can be dealt with formally by allowing infinite values of$t _ { k } { } ^ { \ ' }$s.

## 2.2.11

The restriction property from Section 2.2.10 forms a natural basis for considering the Schur process in continuous time.

For this we need a function$\mathcal { L } ( z , s )$of a continuous variable$s \in \mathbb { R }$which will play the role of the density of log φ. The restriction$\{ \lambda ( t _ { k } ) \}$of the process$\lambda ( t ) , t \in \mathbb { R }$, to any discrete set of times$\{ t _ { k } \}$is the Schur process with parameters

$$
\phi [ m ] (z) = \exp \left(\int_ {t _ {m - \frac {1}{2}}} ^ {t _ {m + \frac {1}{2}}} \mathcal {L} (z, s) d s\right), \quad m \in \mathbb {Z} + \frac {1}{2}.
$$

## 2.2.12

Let$q \in ( 0 , 1 )$and consider the probability measure${ \mathfrak { M } } _ { q }$on the set of all 3D diagrams such that

$$
\operatorname{Prob} (\pi) \propto q ^ {| \pi |}.
$$

We claim that there exists a particular choice of the parameters of the Schur process which yield this measure under the correspondence (3). Concretely, set

$$
\phi_ {3 D} [ m ] (z) = \left\{ \begin{array}{l l} (1 - q ^ {| m |} z) ^ {- 1}, & m <   0, \\ (1 - q ^ {| m |} z ^ {- 1}) ^ {- 1}, & m > 0, \end{array} \right. \quad m \in \mathbb {Z} + \frac {1}{2}.\tag{15}
$$

It is well known that if the algebra of the symmetric functions is specialized so that

$$
h _ {k} = c ^ {k}, \quad k = 1, 2, \ldots ,
$$

for some constant$c ,$then

$$
s _ {\lambda / \mu} = \left\{ \begin{array}{l l} c ^ {| \lambda | - | \mu |}, & \mu \prec \lambda , \\ 0, & \mu \not \prec \lambda . \end{array} \right.
$$

Therefore, we have

$$
\begin{array}{l} \mathsf {S} _ {\phi_ {3 D} [ m ]} \left(\lambda (m - \frac {1}{2}), \lambda (m + \frac {1}{2})\right) = \\ \left\{ \begin{array}{l l} q ^ {m (| \lambda (m - \frac {1}{2}) | - | \lambda (m + \frac {1}{2}) |)}  , & m <   0,   \lambda (m - \frac {1}{2}) \prec \lambda (m + \frac {1}{2}) \quad \text { or } \\ & m > 0,   \lambda (m - \frac {1}{2}) \succ \lambda (m + \frac {1}{2})  , \\ 0  , & \text { otherwise }  . \end{array} \right. \end{array}
$$

It follows that for the specialization (15) the Schur process is supported on configurations of the shape (4) and the weight of a configuration (4) is proportional to

$$
q ^ {\sum | \lambda (t) |} = q ^ {| \pi |}.
$$

In particular, the partition function Z becomes

$$
\begin{array}{r l} & Z _ {3 D} = \exp \left(\sum_ {m _ {1}, m _ {2} = 1 / 2} ^ {\infty} \sum_ {k} \frac {q ^ {k (m _ {1} + m _ {2})}}{k}\right) = \\ & \prod_ {m _ {1}, m _ {2}} (1 - q ^ {m _ {1} + m _ {2}}) ^ {- 1} = \prod_ {n = 1} ^ {\infty} (1 - q ^ {n}) ^ {- n}, \end{array}
$$

which is the well-known generating function, due to McMahon, for 3D diagrams.

## 2.3 Correlation functions

## 2.3.1

Definition 3. Given a subset$U \subset \mathbb { Z } \times ( \mathbb { Z } + { \frac { 1 } { 2 } } )$, define the corresponding correlation function by

$$
\rho (U) = \operatorname{Prob} \left(U \subset \mathfrak {S} (\{\lambda (t) \})\right).
$$

These correlation functions depend on the parameters$\phi [ m ]$of the Schur process.

In this section we show that

$$
\rho (U) = \det \left(K (u _ {i}, u _ {j})\right) _ {u _ {i}, u _ {j} \in U},\tag{16}
$$

for a certain kernel K which will be computed explicitly.

## 2.3.2

Suppose that

$$
U = \left\{u _ {1}, \dots , u _ {n} \right\}, \quad u _ {i} = \left(t _ {i}, x _ {i}\right) \in \mathbb {Z} \times \left(\mathbb {Z} + \frac {1}{2}\right),
$$

and the points$u _ { i }$are ordered so that

$$
t _ {1} \leq t _ {2} \leq t _ {3} \dots \leq t _ {n}.
$$

For convenience, we set$t _ { 0 } = - \infty$. From (10) and (41) it is clear that

$$
\rho (U) = \frac {1}{Z} \left(R _ {U} v _ {\emptyset}, v _ {\emptyset}\right),\tag{17}
$$

where$R _ { U }$is the following operator

$$
R _ {U} = \prod_ {m > t _ {n}} ^ {\leftarrow} \Gamma_ {-} (\phi [ m ]) \Gamma_ {+} (\phi [ m ]) \prod_ {i = 1.. n} ^ {\leftarrow} \left(\psi_ {x _ {i}} \psi_ {x _ {i}} ^ {*} \prod_ {t _ {i - 1} <   m <   t _ {i}} ^ {\leftarrow} \Gamma_ {-} (\phi [ m ]) \Gamma_ {+} (\phi [ m ])\right)
$$

## 2.3.3

Define the operator

$$
\Psi_ {x} (t) = \mathrm{Ad} \left(\prod_ {m > t} \Gamma_ {+} (\phi [ m ]) \prod_ {m <   t} \Gamma_ {-} (\phi [ m ]) ^ {- 1}\right) \cdot \psi_ {x},
$$

where Ad denotes the action by conjugation, and define the operator$\Psi _ { x } ^ { * } ( t )$ similarly. Note the ordering of the vertex operators inside the Ad symbol is immaterial because the vertex operators commute up to a central element.

It follows from (17), (13), and (12) that

$$
\rho (U) = \left(\overleftarrow {\prod} \Psi_ {x _ {i}} (t _ {i}) \Psi_ {x _ {i}} ^ {*} (t _ {i}) v _ {\emptyset}, v _ {\emptyset}\right).
$$

Now we apply Wick formula in the following form

Lemma 1 (Wick formula). Let$\begin{array} { r } { A _ { i } \ = \ \sum _ { k } a _ { i , k } \psi _ { k } } \end{array}$and$\begin{array} { r } { A _ { i } ^ { * } ~ = ~ \sum _ { k } a _ { i , k } ^ { * } \psi _ { k } ^ { * } } \end{array}$ Then

$$
\left(\prod A _ {i}   A _ {i} ^ {*}   v _ {\emptyset}, v _ {\emptyset}\right) = \det \left(K _ {A} (i, j)\right),\tag{18}
$$

where

$$
K _ {A} (i, j) = \left\{ \begin{array}{l l} (A _ {i}   A _ {j} ^ {*}   v _ {\emptyset}, v _ {\emptyset})  , & i \geq j  , \\ - (A _ {j} ^ {*}   A _ {i}   v _ {\emptyset}, v _ {\emptyset})  , & i <   j  . \end{array} \right.
$$

Proof. Both sides of (18) are linear in$a _ { i , k }$and$a _ { i , k } ^ { * } { : }$, therefore it sufices to verify (18) for some linear basis in the space of possible$A _ { i } \mathrm { ^ { * } s }$and$A _ { j } ^ { * } \mathrm { { ^ { s } } }$. A convenient linear basis is formed by the series (19) as the parameter z varies. Using the canonical anticommutation relation satisfied by$\psi ( z )$and$\psi ^ { * } ( z )$ one then verifies (18) directly.□

We obtain the formula (16) with

$$
K ((t _ {1}, x _ {1}), (t _ {2}, x _ {2})) = \left\{ \begin{array}{l l} \big (\Psi_ {x _ {1}} (t _ {1})   \Psi_ {x _ {2}} ^ {*} (t _ {2})   v _ {\emptyset}, v _ {\emptyset} \big)  , & t _ {1} \geq t _ {2}  , \\ - \big (\Psi_ {x _ {2}} ^ {*} (t _ {2})   \Psi_ {x _ {1}} (t _ {1})   v _ {\emptyset}, v _ {\emptyset} \big)  , & t _ {1} <   t _ {2}  . \end{array} \right.
$$

Note that for$t _ { 1 } \neq t _ { 2 }$the operators$\Psi _ { x _ { 1 } } ( t _ { 1 } )$and$\Psi _ { x _ { 2 } } ^ { * } ( t _ { 2 } )$do not, in general, anticommute so the time ordering is important. However, for$t _ { 1 } = t _ { 2 }$and $x _ { 1 } \neq x _ { 2 }$, these operators do anticommute, so at equal time the ordering is immaterial.

## 2.3.4

A convenient generating function for the kernel K can be obtained as follows. Set

$$
\psi (z) = \sum_ {k \in \mathbb {Z} + 1 / 2} z ^ {k}   \psi_ {k}  , \quad \psi^ {*} (z) = \sum_ {k \in \mathbb {Z} + 1 / 2} z ^ {- k}   \psi_ {k} ^ {*}  .\tag{19}
$$

Set also

$$
\Psi (t, z) = \operatorname{Ad} \left(\prod_ {m > t} \Gamma_ {+} (\phi [ m ]) \prod_ {m <   t} \Gamma_ {-} (\phi [ m ]) ^ {- 1}\right) \cdot \psi (z),
$$

and define$\Psi ^ { * } ( t , z )$similarly.

We have from (42)

$$
\begin{array}{r l} & {\mathrm{Ad} (\Gamma_ {\pm} (\phi)) \cdot \psi (z) = \phi^ {\mp} (z ^ {- 1}) \psi (z),} \\ & {\mathrm{Ad} (\Gamma_ {\pm} (\phi)) \cdot \psi^ {*} (z) = \phi^ {\mp} (z ^ {- 1}) ^ {- 1} \psi (z).} \end{array}
$$

and therefore

$$
\Psi (t, z) = \Phi (t, z) \psi (z), \quad \Psi^ {*} (t, z) = \Phi (t, z) ^ {- 1} \psi (z),
$$

where

$$
\Phi (t, z) = \frac {\prod_ {m > t} \phi^ {-} [ m ] (z ^ {- 1})}{\prod_ {m <   t} \phi^ {+} [ m ] (z ^ {- 1})}.\tag{20}
$$

Finally, it is obvious from the definitions that

$$
\begin{array}{r l} & {(\psi (z) \psi^ {*} (w) v _ {\emptyset}, v _ {\emptyset}) = \frac {\sqrt {z w}}{z - w}, | z | > | w |,} \\ & {- (\psi^ {*} (w) \psi (z) v _ {\emptyset}, v _ {\emptyset}) = \frac {\sqrt {z w}}{z - w}, | z | <   | w |.} \end{array}
$$

Putting it all together, we obtain the following

Theorem 1. We have

$$
\rho (U) = \det \left(K (u _ {i}, u _ {j})\right) _ {u _ {i}, u _ {j} \in U},
$$

where the kernel K is determined by the following generating function

$$
\begin{array}{l} \mathsf {K} _ {t _ {1}, t _ {2}} (z, w) = \sum_ {x _ {1}, x _ {2} \in \mathbb {Z} + \frac {1}{2}} z ^ {x _ {1}}   w ^ {- x _ {2}}   K ((t _ {1}, x _ {1}), (t _ {2}, x _ {2}))  , \\ = \frac {\sqrt {z w}}{z - w}   \frac {\Phi (t _ {1} , z)}{\Phi (t _ {2} , w)}  . \end{array}\tag{21}
$$

(22)

Here the function$\boldsymbol { \mathrm { { } } } ^ { \mathrm { { } } } \dot { \boldsymbol { \mathrm { { } } } } ( t , z )$is defined by (20), and (21) is the expansion of (22) in the region$| z | > | w |$if$t _ { 1 } \geq t _ { 2 }$and$| z | < | w | \ i f t _ { 1 } < t _ { 2 }$

## 2.3.5

In the special case of the measure${ \mathfrak { M } } _ { q }$on the 3D diagrams the function (20) specializes to the following function

$$
\Phi_ {3 D} (t, z) = \frac {\prod_ {m > \max (0 , - t)} (1 - q ^ {m} / z)}{\prod_ {m > \max (0 , t)} (1 - q ^ {m} z)}, \quad m \in \mathbb {Z} + \frac {1}{2}.\tag{23}
$$

Consider the following function

$$
(z; q) _ {\infty} = \prod_ {n = 0} ^ {\infty} (1 - q ^ {n} z).\tag{24}
$$

For various reasons, in particular because of the relation (28), this function is sometimes called the quantum dilogarithm function [6].

It is clear that the function (23) has the following expression in terms of the quantum dilogarithm

$$
\Phi_ {3 D} (t, z) = \left\{ \begin{array}{l l} \frac {(q ^ {1 / 2} / z ; q) _ {\infty}}{(q ^ {1 / 2 + t} z ; q) _ {\infty}}, & t \geq 0  , \\ \frac {(q ^ {1 / 2 - t} / z ; q) _ {\infty}}{(q ^ {1 / 2} z ; q) _ {\infty}}, & t \leq 0  . \end{array} \right.
$$

## 2.3.6

In order to make a better connection with the geometry of 3D diagrams, let us introduce a diferent encoding of diagrams by subsets in the plane. Given a plane partition

$$
\pi = (\pi_ {i j}), \quad i, j = 1, 2, \ldots ,
$$

we set

$$
\widetilde {\mathfrak {S}} (\pi) = \left\{(j - i, \pi_ {i j} - (i + j - 1) / 2) \right\}, \quad i, j = 1, 2, \ldots .
$$

There is a well-known correspondence between 3D diagrams and tilings of the plane by rhombi. Namely, the tiles are the images of the faces of the 3D diagram under the projection

$$
(x, y, z) \mapsto (t, h) = (y - x, z - (x + y) / 2).\tag{25}
$$

The tiling corresponding to the diagram in Figure 1 is shown in Figure 3.

![](images/page_17_chart_8.jpg)

Figure 3: Horizontal tiles of the tiling corresponding to diagram in Figure 1

It is clear that under this correspondence the horizontal faces of a 3D diagram are mapped to the horizontal tiles and that the positions of the horizontal tiles uniquely determine the tiling and the diagram π. The set

$$
\widetilde {\mathfrak {S}} (\pi) \subset \mathbb {Z} \times \frac {1}{2} \mathbb {Z}
$$

is precisely the set of the centers of the horizontal tiles. It is also clear that if λ(t) corresponds to the diagram π, then

$$
(t, h) \in \widetilde {\mathfrak {S}} (\pi) \Leftrightarrow (t, x + | t | / 2) \in \mathfrak {S} (\{\lambda (t) \}).
$$

Theorem 1 specializes, therefore, to the following statement

Corollary 1. For any set$\{ ( t _ { i } , h _ { i } ) \}$, we have

$$
\operatorname{Prob} \left(\{(t _ {i}, h _ {i}) \} \subset \widetilde {\mathfrak {S}} (\pi)\right) = \det \left[ K _ {3 D} ((t _ {i}, h _ {i}), (t _ {j}, h _ {j})) \right],
$$

where the kernel$K _ { 3 D }$is given by the following formula

$$
\begin{array}{r l} & K _ {3 D} ((t _ {1}, h _ {1}), (t _ {2}, h _ {2})) = \\ & \frac {1}{(2 \pi i) ^ {2}} \int_ {| z | = 1 \pm \epsilon} \int_ {| w | = 1 \mp \epsilon} \frac {1}{z - w} \frac {\Phi_ {3 D} (t _ {1} , z)}{\Phi_ {3 D} (t _ {2} , w)} \frac {d z d w}{z ^ {h _ {1} + \frac {| t _ {1} | + 1}{2}} w ^ {- h _ {2} - \frac {| t _ {2} | - 1}{2}}}. \end{array}\tag{26}
$$

Here the function$\Phi _ { 3 D } ( t , z )$is defined by (23),$0 < \epsilon \ll 1$, and one picks the plus sign if$t _ { 1 } \geq t _ { 2 }$and the negative sign otherwise.

## 3 Asymptotics

## 3.1 The local shape of a large 3D diagram

## 3.1.1

Our goal in this section is to illustrate how suitable is the formula (22) for asymptotic analysis. In order to be specific, we work out one concrete example, namely the local shape of a 3D diagram distributed according to the measure${ \mathfrak { M } } _ { q }$as$q \to 1$. Our computations, however, will be of a very abstract and general nature and applicable to a much wider variety of specialization.

The reader will notice that the passage to the asymptotics in (22) is so straightforward that even the saddle-point analysis is needed in only a very weak form, namely as the statement that

$$
\int_ {\gamma} e ^ {M S (x)} d x \rightarrow 0, \quad M \rightarrow + \infty ,\tag{27}
$$

provided the function$S ( x )$is smooth and$\Re S ( x ) < 0$for all but finitely many points$x \in \gamma$

## 3.1.2

Let$q = e ^ { - r }$and$r  + 0$. We begin with the following

Lemma 2. We have the following convergence in probability

$$
r ^ {3} | \pi | \rightarrow 2 \zeta (3), r \rightarrow + 0,
$$

where$| \pi |$is the volume of a 3D diagram$\pi$sampled from the measure${ \mathfrak { M } } _ { q }$

Proof. First consider the expectation of$| \pi |$

$$
\mathsf {E} | \pi | = \frac {q \frac {d}{d q} Z _ {3 D}}{Z _ {3 D}} = \sum_ {n \geq 1} \frac {n ^ {2} q ^ {n}}{1 - q ^ {n}} = \sum_ {n, k \geq 1} n ^ {2} q ^ {n k} = \sum_ {k} \frac {q ^ {k} (1 + q ^ {k})}{(1 - q ^ {k}) ^ {3}} \sim \frac {2 \zeta (3)}{r ^ {3}}.
$$

Similarly, the variance of$| \pi |$behaves like

$$
\mathrm{Var} | \pi | = q \frac {d}{d q} \mathsf {E} | \pi | = o (r ^ {- 6}),
$$

whence$\mathrm { V a r } ( r ^ { 3 } | \pi | ) \to 0$, which concludes the proof.

## 3.1.3

It follows that as$r ~  ~ + 0$the typical 3D diagram$\pi ,$scaled by$r$in all directions, approaches the suitably scaled limit shape for typical 3D diagrams of a large volume described in [3]. Below we will also see this limit shape appear from our calculations.

We are interested in the$r ~  ~ + 0$limiting local structure of$\pi$in the neighborhood of various points in the limit shape. In other words, we are interested in the limit of the kernel (26) as

$$
r t _ {i} \rightarrow \tau , r h _ {i} \rightarrow \chi ,
$$

where the variables$\tau$and$\chi$describe the global position on the limit shape, in such a way that the relative distances

$$
\Delta t = t _ {1} - t _ {2}, \quad \Delta h = h _ {1} - h _ {2},
$$

remain fixed. This limit is easy to obtain by a combination of residue calculus with saddle-point argument. Since the measure${ \mathfrak { M } } _ { q }$is obviously symmetric with respect to the reflection$t \mapsto - t$, we can without loss of generality assume that$\tau \geq 0$in our computations.

## 3.1.4

We have the following$r  + 0$asymptotics:

$$
\ln (z; q) _ {\infty} \sim r ^ {- 1} \int_ {0} ^ {z} \frac {\ln (1 - w)}{w} d w = - r ^ {- 1} \mathrm{dilog} (1 - z),\tag{28}
$$

where

$$
\operatorname{dilog} (1 - z) = \sum_ {n} \frac {z ^ {n}}{n ^ {2}}, \quad | z | \leq 1,
$$

analytically continued with a cut along$( 1 , + \infty )$

Introduce the following function

$$
S (z; \tau , \chi) = - (\tau / 2 + \chi) \ln z - \mathrm{dilog} (1 - 1 / z) + \mathrm{dilog} (1 - e ^ {- \tau} z)
$$

and recall that we made the assumption that$\tau \geq 0$. The function$S ( z ; \tau , \chi )$ is analytic in the complex plane with cuts along$( 0 , 1 )$and$( e ^ { \tau } , + \infty )$

As$r  + 0$, the exponentially large term in the integrand in (26) is

$$
\exp \left(\frac {1}{r} (S (z; \tau , \chi) - S (w; \tau , \chi))\right).\tag{29}
$$

The saddle-point method suggests, therefore, to look at the critical points of the function$S ( z ; \tau , \chi )$. Since

$$
z \frac {d}{d z} S (z; \tau , \chi) = - \tau / 2 - \chi - \log (1 - 1 / z) (1 - e ^ {- \tau} z),
$$

the critical points of$S$are the roots of the quadratic polynomial

$$
(1 - 1 / z) (1 - e ^ {- \tau} z) = e ^ {- \tau / 2 - \chi}.
$$

The two roots of this polynomial are complex conjugate if

$$
\left| e ^ {\tau / 2} + e ^ {- \tau / 2} - e ^ {- \chi} \right| <   2,\tag{30}
$$

which can be expressed equivalently as

$$
- 2 \ln \left(2 \cosh \frac {\tau}{4}\right) <   \chi <   - 2 \ln \left(2 \sinh \frac {\tau}{4}\right).\tag{31}
$$

In the case when the roots are complex conjugate they lie on the circle

$$
\gamma = \{| z | = e ^ {\tau / 2} \}
$$

As we shall see below, the inequality (30) describes precisely the possible values of$( \tau , \chi )$that correspond to the bulk of the limit shape.

## 3.1.5

The following elementary properties of the function$S ( z ; \tau , \chi )$

$$
\begin{array}{c} {S (\bar {z}; \tau , \chi) = \overline {{S (z ; \tau , \chi)}},} \\ {S (z; \tau , \chi) + S (e ^ {\tau} / z; \tau , \chi) = - (\tau / 2 + \chi) \tau ,} \end{array}
$$

imply that on the circle$\gamma$the real part of S is constant, namely,

$$
\Re S (z; \tau , \chi) = - (\tau / 2 + \chi) \tau / 2, \quad z \in \gamma .
$$

On$\gamma$we also have

$$
z \frac {d}{d z} S (z; \tau , \chi) = 3 \tau / 2 - \chi - \ln | e ^ {\tau} - z | ^ {2}, \quad z \in \gamma ,
$$

From this it is clear that when the critical points of$S$are complex conjugate, they are the points of intersection of two following circles

$$
\left\{z _ {c}, \bar {z} _ {c} \right\} = \left\{| z | = e ^ {\tau / 2} \right\} \cap \left\{| z - e ^ {\tau} | = e ^ {3 \tau / 4 - \chi / 2} \right\}.\tag{32}
$$

This is illustrated in Figure 4 which also shows the vector field

$$
\nabla \left(\Re S (z; \tau , \chi)\right) = \frac {z ^ {2}}{e ^ {\tau}} \frac {d}{d z} S (z), \quad z \in \gamma .
$$

## 3.1.6

Now we are prepared to do the asymptotics in (26). We can deform the contours of the integration in (26) as follows

$$
K _ {3 D} ((t _ {i}, h _ {i}), (t _ {j}, h _ {j})) = \frac {1}{(2 \pi i) ^ {2}} \int_ {(1 \pm \epsilon) \gamma} d z \int_ {(1 \mp \epsilon) \gamma} d w \quad \dots
$$

where dots stand for the same integrand as in (26),$0 < \epsilon \ll 1$, and we pick the plus sign if$t _ { 1 } \geq t _ { 2 }$and the negative sign otherwise.

Now we define the contours$\gamma _ { > } , \gamma _ { < } , \gamma _ { + } , \gamma _ { - }$. This definition will be illustrated by Figure 5. The contour$\gamma _ { > }$is the circle$| z | = e ^ { \tau / 2 }$slightly deformed in the direction of the gradient of S, see Figure 4. Similarly, the contour $\gamma _ { < }$is the same circle$| z | = e ^ { \tau / 2 }$slightly pushed in the opposite direction. The

![](images/page_22_image_0.jpg)

Figure 4: Gradient of$\Re S ( z )$on the circle$\gamma = \{ | z | = e ^ { \tau / 2 } \}$

![](images/page_22_image_2.jpg)

Figure 5: Contours$\gamma _ { > } ( \mathrm { d a s h e d } )$$\gamma _ { < } ( \mathrm { d o t t e d } )$, and$\gamma _ { \pm }$

contours$\gamma _ { \pm }$are the arcs of the circle$| z | = e ^ { \tau / 2 }$between$\bar { z } _ { c }$and$z _ { c } ,$oriented toward$z _ { c } .$

Deforming the contours, and picking the residue at$z = w$, we obtain

$$
K _ {3 D} ((t _ {i}, h _ {i}), (t _ {j}, h _ {j})) = \int^ {(1)} + \int^ {(2)},
$$

where

$$
\int^ {(1)} = \frac {1}{(2 \pi i) ^ {2}} \int_ {\gamma_ {<  }} d z \int_ {\gamma_ {>}} d w \quad \dots
$$

with the same integrand in as in (26) and

$$
\int^ {(2)} = \frac {1}{2 \pi i} \int_ {\gamma_ {\pm}} \frac {(q ^ {1 / 2 + t _ {2}} w ; q) _ {\infty}}{(q ^ {1 / 2 + t _ {1}} w ; q) _ {\infty}} \frac {d w}{w ^ {\Delta h + \Delta t / 2 + 1}},
$$

where we choose$\gamma _ { + } \operatorname { i f } t _ { 1 } \geq t _ { 2 }$and$\gamma _ { - }$otherwise. As we shall see momentarily,

$$
\int^ {(1)} \rightarrow 0, r \rightarrow + 0,
$$

while$\boldsymbol { \int } ^ { ( 2 ) }$has a simple limit.

## 3.1.7

It is obvious that

$$
\int^ {(2)} \rightarrow \frac {1}{2 \pi i} \int_ {\gamma_ {\pm}} (1 - e ^ {- \tau} w) ^ {\Delta t} \frac {d w}{w ^ {\Delta h + \Delta t / 2 + 1}}, r \rightarrow + 0.
$$

The change of variables$w = e ^ { \tau } w ^ { \prime }$makes this integral a standard incomplete beta function integral:

$$
\int^ {(2)} \rightarrow \frac {e ^ {- \tau (\Delta h + \Delta t / 2)}}{2 \pi i} \int_ {e ^ {- \tau} \gamma_ {\pm}} (1 - w) ^ {\Delta t} \frac {d w}{w ^ {\Delta h + \Delta t / 2 + 1}}, r \rightarrow + 0.
$$

Now notice that the prefactor e$- \tau ( \Delta h + \Delta t / 2 )$will cancel out of any determinant with this kernel, so it can be ignored. We, therefore, make the following

Definition 4. Introduce the following incomplete beta function kernel

$$
\mathsf {B} _ {\pm} (k, l; z) = \frac {1}{2 \pi i} \int_ {\bar {z}} ^ {z} (1 - w) ^ {k} w ^ {- l - 1} d w,
$$

where the path of the integration crosses$( 0 , 1 )$for the plus sign and$( - \infty , 0 )$ for the minus sign.

## 3.1.8

It is also obvious from our construction that the function$\Re S ( z )$reaches its maximal value on the contour$\gamma _ { < }$<sub><</sub> precisely at the points$z _ { c }$and$\bar { z } _ { c }$. The same points are the minima of the function$S ( z )$on the contour$\gamma _ { > }$. The behavior of the integral$\boldsymbol { \int } ^ { ( 1 ) }$is thus determined by the term (29) and, by the basic principle (27), the limit of$\boldsymbol { \int } ^ { ( 1 ) }$vanishes.

## 3.1.9

We can summarize our discussion as follows. Set$z _ { * } = e ^ { - \tau } z _ { c } ,$, in other words,

$$
\left\{z _ {*}, \bar {z} _ {*} \right\} = \left\{\left| z \right| = e ^ {- \tau / 2} \right\} \cap \left\{\left| z - 1 \right| = e ^ {- \tau / 4 - \chi / 2} \right\}, \quad \Im z _ {*} > 0.\tag{33}
$$

It is convenient to extend the meaning of$z _ { * }$to denote the point on the circle $| z | = e ^ { - \tau / 2 }$which is the closest point to the circle$| z - 1 | = e ^ { - \tau / 4 - \chi / 2 }$in case when the two circles do not intersect. In other words, we complement the definition (33) by setting

$$
z _ {*} = \left\{ \begin{array}{l l} e ^ {- \tau / 2}, & e ^ {- \chi / 2} <   e ^ {\tau / 4} - e ^ {- \tau / 4}, \\ - e ^ {- \tau / 2}, & e ^ {- \chi / 2} > e ^ {\tau / 4} + e ^ {- \tau / 4}. \end{array} \right.\tag{34}
$$

We have established the following

Theorem 2. Let$U = \{ ( t _ { i } , h _ { i } ) \}$and suppose that as$r  + 0$

$$
r t _ {i} \rightarrow \tau \geq 0, r h _ {i} \rightarrow \chi , i = 1, 2, \ldots ,
$$

in such a way that the diferences

$$
\Delta t _ {i j} = t _ {i} - t _ {j}, \quad \Delta h _ {i j} = h _ {i} - h _ {j},
$$

remain fixed. Then, as$r  + 0$

$$
\mathrm{Prob} \{U \subset \widetilde {\mathfrak {S}} (\pi) \} \to \det \left[ \mathtt {B} _ {\pm} \left(\Delta t _ {i j}, \Delta h _ {i j} + \frac {\Delta t _ {i j}}{2}; z _ {*}\right) \right],
$$

where the point$z _ { * } = z _ { * } ( \tau , \chi )$is defined in (33)and (34) and the choice of the plus sign corresponds to$\Delta t _ { i j } = t _ { i } - t _ { j } \geq 0$

Remark 1. These formulas can be transformed, see Section 3.1.12, into a double integral of form considered in [5], Proposition 8.5 and Conjecture 13.5.

Remark 2. Observe that the limit correlation are trivial in the cases covered by (34). In other words, they are nontrivial unless the inequality (30) is satisfied. This means that the inequality (30) describes the values of$( \tau , \chi )$ that correspond to the bulk of the limit shape.

## 3.1.10

In particular, denote by$\rho _ { * } ( \tau , \chi )$the limit of 1-point correlation function

$$
K _ {3 D} ((t, h), (t, h)) \to \rho_ {*} (\tau , \chi), r t \to \tau , r h \to \chi .
$$

This is the limiting density of the horizontal tiles at the point$( \tau , \chi )$. We have the following

Corollary 2. The limiting density of horizontal tiles is

$$
\rho_ {*} (\tau , \chi) = \frac {\theta_ {*}}{\pi},
$$

where$\theta _ { * } = \arg z _ { * }$(see Figure 5), that is,

$$
\theta_ {*} = \arccos \left(\cosh \frac {\tau}{2} - \frac {e ^ {- \chi}}{2}\right).\tag{35}
$$

The level sets of the density as functions of$\tau$and$\chi$are plotted in Figure 6. More precisely, Figure 6 shows the curves

$$
\theta_ {*} (\tau , \chi) = \frac {k \pi}{8}, \quad k = 0, \dots , 8.
$$

The knowledge of density$\rho _ { * }$is equivalent to the knowledge of the limit shape, see Sections 3.1.13 and 3.1.14. We point out, however, that additional analysis is needed to prove the convergence to the limit shape in a suitable metric as in [3].

![](images/page_26_image_0.jpg)

Figure 6: Level sets of the density of horizontal tiles

## 3.1.11

Corollary 2 can be generalized as follows:

Corollary 3. The equal time correlations are given by the discrete sine kernel, that is,$i f t _ { 1 } = t _ { 2 } = . .$. then

$$
\mathrm{Prob} \{U \subset \widetilde {\mathfrak {S}} (\pi) \} \to \det \left[ \frac {\sin (\theta_ {*} (h _ {i} - h _ {j}))}{\pi (h _ {i} - h _ {j})} \right],
$$

as$r  + 0$

## 3.1.12

The incomplete beta kernel$\mathsf { B } _ { \pm }$can be transformed into a double integral of the form considered in [5] as follows.

Using the following standard integral

$$
\frac {1}{2 \pi i} \int_ {| z | = \alpha} \frac {z ^ {- k - 1}   d z}{1 - \beta z} = \left\{ \begin{array}{l l} \beta^ {k}, & k \geq 0,   | \alpha \beta | <   1  , \\ - \beta^ {k}, & k <   0,   | \alpha \beta | > 1  , \\ 0  , & \text { otherwise }  , \end{array} \right.
$$

we can replace the condition

$$
| w - 1 | \lessgtr e ^ {- \tau / 4 - \chi / 2},
$$

in the definition of$\mathtt { B } _ { \pm } ( k , l ; z _ { * } )$by an extra integral. We obtain

$$
\mathsf{B}_{\pm}(k,l;z_{*}) = \frac{1}{(2\pi i)^{2}}\iint_{\substack{|w| = e^{-\tau /2}\\ |z| = e^{\tau /4 + \chi /2}}}\frac{z^{-k - 1}w^{-l - 1}}{1 - z + zw}  dz  dw  ,\tag{36}
$$

where the plus sign corresponds to$k \geq 0$

## 3.1.13

Let$z ( \tau , \chi )$denote the z-coordinate of the point on the limit shape corresponding to the point$( \tau , \chi )$. This function can be obtained by integrating the density$\rho _ { * } ( \tau , \chi )$as follows.

Consider a tiling such as the one in the Figure 3 and the corresponding 3D diagram, which for the tiling in Figure 3 is shown in Figure 1. It is clear that the z-coordinate of the face corresponding to a given horizontal tile equals the number of holes (that is, positions not occupied by a horizontal tile) below it. It follows that

$$
z (\tau , \chi) = \int_ {- \infty} ^ {\chi} (1 - \rho_ {*} (\tau , s)) d s.\tag{37}
$$

Here, of course, the lower limit of integration can be any number between $- \infty$and the lower boundary of the limit shape given by the equation (31).

Integrating (35) we obtain the following formula

$$
z (\tau , \chi) = \frac {1}{\pi} \int_ {0} ^ {\pi - \theta_ {*}} \frac {s \sin s d s}{\cos s + \cosh \frac {\tau}{2}}.\tag{38}
$$

This integral can be evaluated in terms of the dilogarithm function. From (25) we can now compute the other two coordinates as follows

$$
x (\tau , \chi) = z (\tau , \chi) - \chi - \frac {\tau}{2}, y (\tau , \chi) = z (\tau , \chi) - \chi + \frac {\tau}{2},\tag{39}
$$

which gives a parametrization of the limit shape. A plot of the limit shape is shown in Figure 7

## 3.1.14

To make the connection to the parametrization of the limit shape given in [3], let us now substitute for$\rho _ { * }$in the integral (37) the formula (36). After

![](images/page_28_image_0.jpg)

Figure 7: The limit shape

a simple coordinate change we obtain

$$
\rho_ {*} (\tau , \chi) = \frac {1}{4 \pi^ {2}} \iint_ {0} ^ {2 \pi} \frac {d u d v}{1 + e ^ {\chi / 2 + \tau / 4 + i u} + e ^ {\chi / 2 - \tau / 4 + i v}}.
$$

Integrating this in$\chi$we obtain

$$
z (\tau , \chi) = \frac {1}{2 \pi^ {2}} \iint_ {0} ^ {2 \pi} \ln \left| 1 + e ^ {\chi / 2 + \tau / 4 + i u} + e ^ {\chi / 2 - \tau / 4 + i v} \right| d u d v.
$$

This together with (39) is equivalent to following parametrization of the limit shape found in [3]

$$
(x, y, z) = (f (A, B, C) - 2 \ln A, f (A, B, C) - 2 \ln B, f (A, B, C) - 2 \ln C),
$$

where A,$B , C > 0$and

$$
f (A, B, C) = \frac {1}{2 \pi^ {2}} \iint_ {0} ^ {2 \pi} \ln \left| A + B e ^ {i u} + C e ^ {i v} \right| d u d v.
$$

This parametrization is manifestly symmetric in x, y, and z. However, it involves integrals that are more complicated to evaluate than the parametrization (38).

Note that the shape considered in [3] difers from our by a factor of 2 due to diferent scaling conventions.

## 3.2 Universality

## 3.2.1

The reader has surely noticed that all that we really needed for the asymptotics is to be able to deform the contours of integration as in Figure 5 so that the points of the intersection of$\gamma _ { > }$and$\gamma _ { < }$the minima of the function $\Re S ( z )$on one curve and the maxima — on the other. The intersection points are then forced to be the critical points of the function$S ( z )$

It is clear that this principle is very general and applicable in a potentially very large variety of situations, such as, for example, in the case of Plancherel measure, see below. In particular, the existence of contours of a certain kind is a property which is preserved under small perturbations.

## 3.2.2

One such perturbation would be to consider anisotropic partitions. The anisotropy in the t-direction is especially easy to introduce: one just should replace$q ^ { | m | }$in (15) by$q ^ { V ( m ) }$for some function V.

## 3.2.3

Observe that the asymptotics of the equal time correlations are especially easy to obtain in our approach. This is because

$$
\operatorname{Res} _ {z = w} \frac {d z}{z - w} \frac {\Phi (t _ {1} , z)}{\Phi (t _ {2} , w)} = 1, \quad t _ {1} = t _ {2},
$$

and hence the analog of the integral$\boldsymbol { \int } ^ { ( 2 ) }$becomes simply the integral

$$
\int^ {(2)} = \frac {1}{2 \pi i} \int_ {\gamma_ {\pm}} \frac {d w}{w ^ {\Delta x + 1}},
$$

which leads to the discrete sine kernel in the variable$\Delta x$

## 3.2.4

Let us illustrate these general remarks by briefly discussing the asymptotics for the poissonized Plancherel measure [1]. It corresponds to the following specialization of the Schur process

$$
\phi_ {\mathrm{Planch}} [ m ] = \left\{ \begin{array}{l l} e ^ {\sqrt {\alpha} z}, & m = - \frac {1}{2}, \\ e ^ {\sqrt {\alpha} z ^ {- 1}}, & m = \frac {1}{2}, \\ 1, & \mathrm{otherwise}, \end{array} \right.
$$

where$\alpha > 0$is the poissonization parameter. In particular, only the partition $\lambda ( 0 )$is nontrivial. The correlation kernel at$t = 0$specializes to

$$
K _ {\mathrm{Planch}} (x, y) = \frac {1}{(2 \pi i) ^ {2}} \iint \frac {z ^ {- x - 1 / 2} w ^ {y - 1 / 2}}{z - w} e ^ {\sqrt {\alpha} (z - z ^ {- 1} - w + w ^ {- 1})} d z d w,
$$

which can be expressed in terms of Bessel functions of the argument$2 \sqrt { \alpha }$ see [1, 8].

## 3.2.5

The$\alpha \longrightarrow \infty$asymptotics of the kernel$K _ { \mathrm { P l a n c h } }$is easy to obtain from the classical asymptotics of the Bessel functions, see [1]. It is, however, instructive to see how this can be done even more quickly in our framework. Assume that

$$
\frac {x}{\sqrt {\alpha}}, \frac {y}{\sqrt {\alpha}} \rightarrow \xi
$$

in such a way that$\Delta = x - y$remains fixed. The critical points of the action

$$
S _ {\mathrm{Planch}} = z - z ^ {- 1} - \frac {\xi}{2} \ln z
$$

are complex precisely when$| \xi | < 2$, in which case they are the points$e ^ { \pm i \theta }$ where

$$
\theta = \arccos (\xi / 2).
$$

So, the same argument as we employed above immediately yields the following formula from [1].

$$
K _ {\mathrm{Planch}} (x, y) \rightarrow \frac {\sin \theta \Delta}{\pi \Delta}.
$$

## 3.2.6

Of course, a finer analysis (which was carried out in [1]) is needed to justify depoissonization in the asymptotics. In our situation, a similar problem is to pass from the$q \to 1$asymptotics of the measure${ \mathfrak { M } } _ { q }$to the asymptotics of the uniform measures on partitions of a given volume N as$N  \infty$. In other words, further work is needed to verify the equivalence of ensembles in the asymptotics.

## 3.2.7

Similarly, finer analysis is needed to work with the asymptotics at the edges of the limit shapes where one expects to see the Airy kernel appear. In the edge scaling, the following equivalent version of the formula (22)

$$
K ((t _ {1}, x _ {1}), (t _ {2}, x _ {2})) = \sum_ {m = 1 / 2} ^ {\infty} [ z ^ {x _ {1} + m} w ^ {- x _ {2} - m} ] \frac {\Phi (t _ {1} , z)}{\Phi (t _ {2} , w)},\tag{40}
$$

may be helpful because, by analogy to the situation with the Plancherel measure [1, 8], one could expect to see this sum to become the integral representing the Airy kernel

$$
\frac {\operatorname{Ai} (x) \operatorname{Ai} ^ {\prime} (y) - \operatorname{Ai} ^ {\prime} (x) \operatorname{Ai} (y)}{x - y} = \int_ {0} ^ {\infty} \operatorname{Ai} (x + s) \operatorname{Ai} (y + s) d s.
$$

Further discussion of the Airy-type asymptotics of the integrals of the form (22), (26) can be found in [17].

## 3.2.8

Recently, the techniques of this paper were used in [7] to prove that, indeed, the boundary of a random 3D Young diagram converges to the Airy process.

## A Summary of the infinite wedge formulas

Let the space V be spanned by k,$k \in \mathbb { Z } + \frac { 1 } { 2 }$. The space$\Lambda ^ { \frac { \infty } { 2 } } V$is, by definition, spanned by vectors

$$
v _ {S} = \underline {{s _ {1}}} \wedge \underline {{s _ {2}}} \wedge \underline {{s _ {3}}} \wedge \dots ,
$$

where$S = \{ s _ { 1 } > s _ { 2 } > . . . \} \subset \mathbb { Z } + { \frac { 1 } { 2 } }$is such a subset that both sets

$$
S _ {+} = S \setminus \left(\mathbb {Z} _ {\leq 0} - \frac {1}{2}\right), \quad S _ {-} = \left(\mathbb {Z} _ {\leq 0} - \frac {1}{2}\right) \setminus S
$$

are finite. We equip$\Lambda ^ { \frac { \infty } { 2 } } V$with the inner product in which the basis$\{ v _ { S } \}$is orthonormal. In particular, we have the vectors

$$
v _ {\lambda} = \underline {{\lambda_ {1} - \frac {1}{2}}} \wedge \underline {{\lambda_ {2} - \frac {3}{2}}} \wedge \underline {{\lambda_ {4} - \frac {5}{2}}} \wedge \dots ,
$$

where λ is a partition. The vector

$$
v _ {\emptyset} = \underline {{- \frac {1}{2}}} \wedge \underline {{- \frac {3}{2}}} \wedge \underline {{- \frac {5}{2}}} \wedge \dots
$$

is called the vacuum vector.

The operator$\psi _ { k }$is the exterior multiplication by$\underline { { k } }$

$$
\psi_ {k} (f) = \underline {{k}} \wedge f.
$$

The operator$\psi _ { k } ^ { * }$is the adjoint operator. These operators satisfy the canonical anti-commutation relations

$$
\psi_ {k} \psi_ {k} ^ {*} + \psi_ {k} ^ {*} \psi_ {k} = 1,
$$

all other anticommutators being equal to 0. We have

$$
\psi_ {k} \psi_ {k} ^ {*}   v _ {S} = \left\{ \begin{array}{l l} v _ {S}  , & k \in S  , \\ 0  , & k \notin S  . \end{array} \right.\tag{41}
$$

The operators$\alpha _ { n }$defined by

$$
\alpha_ {n} = \sum_ {k \in \mathbb {Z} + \frac {1}{2}} \psi_ {k - n}   \psi_ {k} ^ {*}, \quad n = \pm 1, \pm 2, \ldots ,
$$

satisfy the Heisenberg commutation relations

$$
[ \alpha_ {n}, \alpha_ {m} ] = n \delta_ {n, - m},
$$

see the formula. Clearly,$\alpha _ { n } ^ { * } = \alpha _ { - n }$. It is clear from definitions that

$$
[ \alpha_ {n}, \psi (z) ] = z ^ {n} \psi (z), [ \alpha_ {n}, \psi^ {*} (w) ] = - w ^ {n} \psi^ {*} (w)\tag{42}
$$

and also that

$$
\alpha_ {n}   v _ {\emptyset} = 0  , \quad n \leq 0  .\tag{43}
$$

## References

[1] A. Borodin, A. Okounkov, and G. Olshanski, On asymptotics of the Plancherel measures for symmetric groups, J. Amer. Math. Soc. 13 (2000), no. 3, 481–515.

[2] R. Burton and R. Pemantle, Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impendances, Ann. Prob. 21 (1993), 1329–1371.

[3] R. Cerf and R. Kenyon, The low-temperature expansion of the Wulf crystal in the 3D Ising model, preprint (2001).

[4] H. Cohn, N. Elkies, and J. Propp, Local statistics for random domino tilings of the Aztec diamond, Duke Math. J. 85 (1996), no. 1, 117–166.

[5] H. Cohn, R. Kenyon, and J. Propp, A variational principle for domino tilings, math.CO/0008220.

[6] L. Faddeev and R. Kashaev, Quantum dilogarithm, hep-th/9310070.

[7] P. Ferrari and H. Spohn, Step fluctuations for a faceted crystal, condmat/0212456.

[8] K. Johansson, Discrete orthogonal polynomials and the Plancherel measure, math.CO/9906120.

[9] K. Johansson, Universality of the local spacing distribution in certain ensembles of Hermitian Wigner matrices, math.ph/0006020.

[10] K. Johansson, Non-intersecting paths, random tilings, and random matrices, math.PR/0011250.

[11] V. Kac, Infinite dimensional Lie algebras, Cambridge University Press.

[12] S. Karlin and G. McGregor, Coincidence probabilities, Pacific J. Math 9 (1959), 1141–1164.

[13] R. Kenyon, Local statistics of lattice dimers, Ann. Inst. H. Poincar´e, Prob. et Stat. 33 (1997), 591–618.

[14] R. Kenyon, The planar dimer model with a boundary: a survey, to appear in Proceedings CRM.

[15] I. G. Macdonald, Symmetric functions and Hall polynomials, Clarendon Press, 1995.

[16] A. Okounkov, Infinite wedge and random partitions, Selecta Math., New Ser., 7 (2001), 57–81, math.RT/9907127.

[17] A. Okounkov, Symmetric functions and random partitions, Symmetric functions 2001: Surveys of Developments and Perspectives, edited by S. Fomin, Kluwer Academic Publishers, 2002.

[18] M. Praehofer and H. Spohn, Scale Invariance of the PNG Droplet and the Airy Process, math.PR/0105240.

[19] A. Vershik, talk at the 1997 conference on Formal Power Series and Algebraic Combinatorics, Vienna.