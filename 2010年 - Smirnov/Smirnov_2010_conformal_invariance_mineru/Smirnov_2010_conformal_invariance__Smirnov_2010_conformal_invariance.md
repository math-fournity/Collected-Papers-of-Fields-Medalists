# MULTI LINEAR FORMULATION OF DIFFERENTIAL GEOMETRY AND MATRIX REGULARIZATIONS

## JOAKIM ARNLIND, JENS HOPPE, AND GERHARD HUISKEN

ABSTRACT. We prove that many aspects of the differential geometry of embedded Riemannian manifolds can be formulated in terms of multi linear algebraic structures on the space of smooth functions. In particular, we find algebraic expressions for Weingarten's formula, the Ricci curvature and the Codazzi-Mainardi equations.

For matrix analogues of embedded surfaces we define discrete curvatures and Euler characteristics, and a non-commutative Gauss–Bonnet theorem is shown to follow. We derive simple expressions for the discrete Gauss curvature in terms of matrices representing the embedding coordinates, and a large class of explicit examples is provided. Furthermore, we illustrate the fact that techniques from differential geometry can carry over to matrix analogues by proving that a bound on the discrete Gauss curvature implies a bound on the eigenvalues of the discrete Laplace operator.

## CONTENTS

1. Introduction 1  
2. Preliminaries 3  
3. Nambu bracket formulation 4  
3.1. Construction of normal vectors 8  
3.2. The Codazzi-Mainardi equations 11  
3.3. Covariant derivatives 13  
3.4. Embedded surfaces 15  
4. Matrix regularizations 18  
4.1. Discrete curvature and the Gauss-Bonnet theorem 22  
4.2. Two simple examples 24  
4.3. Axially symmetric surfaces in $\mathbb{R}^3$ 27  
4.4. A bound on the eigenvalues of the matrix Laplacian 30  
Acknowledgments 33  
References 33

## 1. INTRODUCTION

It is generally interesting to study in what ways information about the geometry of a differentiable manifold  $\Sigma$  can be extracted as algebraic properties of the algebra of smooth functions  $C^{\infty}(\Sigma)$ . In case  $\Sigma$  is a Poisson manifold, this algebra has a second (apart from the commutative multiplication of functions) bilinear (non-associative) algebra structure, the Poisson bracket. The bracket is compatible with

the commutative multiplication via Leibniz rule, thus carrying the basic properties of a derivation.

On a surface  $\Sigma$ , with local coordinates  $u^{1}$  and  $u^{2}$ , one can define

$$
\{f, h \} = \frac {1}{\sqrt {g}} \left(\frac {\partial f}{\partial u ^ {1}} \frac {\partial h}{\partial u ^ {2}} - \frac {\partial h}{\partial u ^ {1}} \frac {\partial f}{\partial u ^ {2}}\right),
$$

where g is the determinant of the induced metric tensor, and one readily checks that  $\left(C^{\infty}(\Sigma),\{\cdot,\cdot\}\right)$  is a Poisson algebra. Having only this very particular combination of derivatives at hand, it seems at first unlikely that one can encode geometric information of  $\Sigma$  in Poisson algebraic expressions. Surprisingly, it turns out that many differential geometric quantities can be computed in a completely algebraic way, cp. Theorem 3.7 and Theorem 3.17. For instance, the Gaussian curvature of a surface embedded in  $R^{m}$  can be written as

$$
K = \sum_ {j, k, l = 1} ^ {m} \left(\frac {1}{2} \{\{x ^ {j}, x ^ {k} \}, x ^ {k} \} \{\{x ^ {j}, x ^ {l} \}, x ^ {l} \} - \frac {1}{4} \{\{x ^ {j}, x ^ {k} \}, x ^ {l} \} \{\{x ^ {j}, x ^ {k} \}, x ^ {l} \}\right),\tag{1.1}
$$

where  $x^{i}(u^{1}, u^{2})$  are the embedding coordinates of the surface.

For a general n-dimensional manifold  $\Sigma$ , we are led to consider Nambu brackets [Nam73], i.e. multi-linear alternating n-ary maps from  $C^{\infty}(\Sigma) \times \cdots \times C^{\infty}(\Sigma)$  to  $C^{\infty}(\Sigma)$ , defined by

$$
\left\{f _ {1}, \ldots , f _ {n} \right\} = \frac {1}{\sqrt {g}} \varepsilon^ {a _ {1} \dots a _ {n}} \left(\partial_ {a _ {1}} f _ {1}\right) \dots \left(\partial_ {a _ {n}} f _ {n}\right).
$$

In the case of surfaces, our initial motivation for studying the problem came from matrix regularizations of Membrane Theory. Classical solutions in Membrane Theory are 3-manifolds with vanishing mean curvature in $\mathbb{R}^{1,d}$. Considering one of the coordinates to be time, the problem can also be formulated in a dynamical way as surfaces sweeping out volumes of vanishing mean curvature. In this context, a regularization was introduced replacing the infinite dimensional function algebra on the surface by an algebra of $N\times N$ matrices [GH82]. If we let $T_{\alpha}$ be a linear map from smooth functions to hermitian $N_{\alpha}\times N_{\alpha}$ matrices, the main properties of the regularization are

$$
\begin{array}{l} \lim _ {\alpha \to \infty} | | T _ {\alpha} (f) T _ {\alpha} (g) - T _ {\alpha} (f g) | | = 0, \\ \lim _ {\alpha \to \infty} \left| \left| \frac {1}{i \hbar_ {\alpha}} [ T _ {\alpha} (f), T _ {\alpha} (h) ] - T _ {\alpha} (\{f, h \}) \right| \right| = 0, \end{array}
$$

where  $\hbar_{\alpha}$  is a real valued function tending to zero as  $N_{\alpha} \to \infty$  (see Section 4 for details), and therefore it is natural to regularize the system by replacing (commutative) multiplication of functions by (non-commutative) multiplication of matrices and Poisson brackets of functions by commutators of matrices.

Although we may very well consider  $T_{\alpha}(\frac{\partial f}{\partial u^{1}})$ , its relation to  $T_{\alpha}(f)$  is in general not simple. However, the particular combination of derivatives in  $T_{\alpha}(\{f,h\})$  is expressed in terms of a commutator of  $T_{\alpha}(f)$  and  $T_{\alpha}(h)$ . In the context of Membrane Theory, it is desirable to have geometrical quantities in a form that can easily be regularized, which is the case for any expression constructed out of multiplications and Poisson brackets. For instance, solving the equations of motion for the regularized membrane gives sequences of matrices that correspond to the embedding coordinates of the surface. Since the set of solutions contains regularizations of

surfaces of arbitrary topology, one would like to be able to compute the genus corresponding to particular solutions. The regularized form of  $(1.1)$  provides a way of resolving this problem.

The paper is organized as follows: In Section 2 we introduce the relevant notation by recalling some basic facts about submanifolds. In Section 3 we formulate several basic differential geometric objects in terms of Nambu brackets, and in Section 3.1 we provide a construction of a set of orthonormal basis vectors of the normal space. Section 3.2 is devoted to the study of the Codazzi-Mainardi equations and how one can rewrite them in terms of Nambu brackets. In Section 3.4 we study the particular case of surfaces, for which many of the introduced formulas and concepts are particularly nice and in which case one can construct the complex structure in terms of Poisson brackets.

In the second part of the paper, starting with Section 4, we study the implications of our results for matrix regularizations of compact surfaces. In particular, a discrete version of the Gauss-Bonnet theorem is derived in Section 4.1 and a proof that the discrete Gauss curvature bounds the eigenvalues of the discrete Laplacian is found in Section 4.4.

## 2. PRELIMINARIES

To introduce the relevant notations, we shall recall some basic facts about submanifolds, in particular Gauss' and Weingarten's equations (see e.g. [KN96a, KN96b] for details). For $n \geqslant 2$, let $\Sigma$ be a $n$-dimensional manifold embedded in a Riemannian manifold $M$ with $\dim M = n + p \equiv m$. Local coordinates on $M$ will be denoted by $x^1, \ldots, x^m$, local coordinates on $\Sigma$ by $u^1, \ldots, u^n$, and we regard $x^1, \ldots, x^m$ as being functions of $u^1, \ldots, u^n$ providing the embedding of $\Sigma$ in $M$. The metric tensor on $M$ is denoted by $\bar{g}_{ij}$ and the induced metric on $\Sigma$ by $g_{ab}$; indices $i, j, k, l, n$ run from 1 to $m$, indices $a, b, c, d, p, q$ run from 1 to $n$ and indices $A, B, C, D$ run from 1 to $p$. Furthermore, the covariant derivative and the Christoffel symbols in $M$ will be denoted by $\bar{\nabla}$ and $\bar{\Gamma}_{jk}^i$ respectively.

The tangent space $T\Sigma$ is regarded as a subspace of the tangent space $TM$ and at each point of $\Sigma$ one can choose $e_a = (\partial_a x^i)\partial_i$ as basis vectors in $T\Sigma$, and in this basis we define $g_{ab} = \bar{g}(e_a, e_b)$. Moreover, we choose a set of normal vectors $N_A$, for $A = 1, \ldots, p$, such that $\bar{g}(N_A, N_B) = \delta_{AB}$ and $\bar{g}(N_A, e_a) = 0$.

The formulas of Gauss and Weingarten split the covariant derivative in M into tangential and normal components as

(2.1)

$$
\bar {\nabla} _ {X} Y = \nabla_ {X} Y + \alpha (X, Y)\tag{2.2}
$$

$$
\bar {\nabla} _ {X} N _ {A} = - W _ {A} (X) + D _ {X} N _ {A}
$$

where $X, Y \in T\Sigma$ and $\nabla_X Y$, $W_A(X) \in T\Sigma$ and $\alpha(X, Y)$, $D_X N_A \in T\Sigma^\perp$. By expanding $\alpha(X, Y)$ in the basis $\{N_1, \ldots, N_p\}$ one can write (2.1) as

$$
\bar {\nabla} _ {X} Y = \nabla_ {X} Y + \sum_ {A = 1} ^ {p} h _ {A} (X, Y) N _ {A},\tag{2.3}
$$

and we set $h_{A,ab} = h_A(e_a, e_b)$. From the above equations one derives the relation

$$
h _ {A, a b} = - \bar {g} \big (e _ {a}, \bar {\nabla} _ {b} N _ {A} \big),\tag{2.4}
$$

as well as Weingarten's equation

$$
h _ {A} (X, Y) = \bar {g} \bigl (W _ {A} (X), Y \bigr),\tag{2.5}
$$

which implies that $(W_A)_b^a = g^{ac}h_{A,cb}$, where $g^{ab}$ denotes the inverse of $g_{ab}$.

From formulas (2.1) and (2.2) one obtains Gauss' equation, i.e. an expression for the curvature $R$ of $\Sigma$ in terms of the curvature $\bar{R}$ of $M$, as

$$
\begin{array}{r} g \big (R (X, Y) Z, V \big) = \bar {g} \big (\bar {R} (X, Y) Z, V \big) - \bar {g} \big (\alpha (X, Z), \alpha (Y, V) \big) \\ + \bar {g} \big (\alpha (Y, Z), \alpha (X, V) \big), \end{array}\tag{2.6}
$$

where $X, Y, Z, V \in T\Sigma$. As we shall later on consider the Ricci curvature, let us note that (2.6) implies

$$
\mathcal {R} _ {b} ^ {p} = g ^ {p d} g ^ {a c} \bar {g} \big (\bar {R} (e _ {c}, e _ {d}) e _ {b}, e _ {a} \big) + \sum_ {A = 1} ^ {p} \Big [ (W _ {A}) _ {a} ^ {a} (W _ {A}) _ {b} ^ {p} - (W _ {A} ^ {2}) _ {b} ^ {p} \Big ]\tag{2.7}
$$

where R is the Ricci curvature of  $\Sigma$  considered as a map  $T\Sigma \rightarrow T\Sigma$ . We also recall the mean curvature vector, defined as

$$
H = \frac {1}{n} \sum_ {A = 1} ^ {p} \big (\operatorname{tr} W _ {A} \big) N _ {A}.\tag{2.8}
$$

## 3. NAMBU BRACKET FORMULATION

In this section we will prove that one can express many aspects of the differential geometry of an embedded manifold  $\Sigma$  in terms of a Nambu bracket introduced on  $C^{\infty}(\Sigma)$ . Let  $\rho : \Sigma \to R$  be an arbitrary non-vanishing density and define

$$
\left\{f _ {1}, \ldots , f _ {n} \right\} = \frac {1}{\rho} \varepsilon^ {a _ {1} \dots a _ {n}} \left(\partial_ {a _ {1}} f _ {1}\right) \cdot \cdot \cdot \left(\partial_ {a _ {n}} f _ {n}\right)\tag{3.1}
$$

for all  $f_{1},\ldots,f_{n}\in C^{\infty}(\Sigma)$ , where  $\varepsilon^{a_{1}\cdots a_{n}}$  is the totally antisymmetric Levi-Civita symbol with  $\varepsilon^{12\cdots n}=1$ . Together with this multi-linear map,  $\Sigma$  is a Nambu-Poisson manifold.

The above Nambu bracket arises from the choice of a volume form on $\Sigma$. Namely, let $\omega$ be a volume form and define $\{f_1, \ldots, f_n\}$ via the formula

$$
\{f _ {1}, \dots , f _ {n} \} \omega = d f _ {1} \wedge \dots \wedge d f _ {n}.\tag{3.2}
$$

Writing  $\omega = \rho du^{1} \wedge \cdots \wedge du^{n}$  in local coordinates, and evaluating both sides of (3.2) on the tangent vectors  $\partial_{u^{1}}, \ldots, \partial_{u^{n}}$  gives

$$
\left\{f _ {1}, \dots , f _ {n} \right\} = \frac {1}{\rho} \det \left(\frac {\partial (f _ {1} , \dots , f _ {n})}{\partial (u ^ {1} , \dots , u ^ {n})}\right) = \frac {1}{\rho} \varepsilon^ {a _ {1} \dots a _ {n}} \left(\partial_ {a _ {1}} f _ {1}\right) \dots \left(\partial_ {a _ {n}} f _ {n}\right).
$$

To define the objects which we will consider, it is convenient to introduce some notation. Let  $x^{1}(u^{1},\ldots,u^{n}),\ldots,x^{m}(u^{1},\ldots,u^{n})$  be the embedding coordinates of  $\Sigma$  into M, and let  $n_{A}^{i}(u^{1},\ldots,u^{n})$  denote the components of the orthonormal vectors  $N_{A}$ , normal to  $T\Sigma$ . Using multi-indices  $I=i_{1}\cdots i_{n-1}$  and  $\vec{a}=a_{1}\cdots a_{n-1}$  we define

$$
\{f, \vec {x} ^ {I} \} \equiv \{f, x ^ {i _ {1}}, x ^ {i _ {2}}, \ldots , x ^ {i _ {n - 1}} \}
$$

$$
\{f, \vec {n} _ {A} ^ {I} \} \equiv \{f, n _ {A} ^ {i _ {1}}, n _ {A} ^ {i _ {2}}, \ldots , n _ {A} ^ {i _ {n - 1}} \},
$$

together with

$$
\partial_ {\vec {a}} \vec {x} ^ {I} \equiv (\partial_ {a _ {1}} x ^ {i _ {1}}) (\partial_ {a _ {2}} x ^ {i _ {2}}) \cdot \cdot \cdot (\partial_ {a _ {n - 1}} x ^ {i _ {n - 1}})
$$

$$
\left(\bar {\nabla} _ {\vec {a}} \vec {n} _ {A}\right) ^ {I} \equiv \left(\bar {\nabla} _ {a _ {1}} N _ {A}\right) ^ {i _ {1}} \left(\bar {\nabla} _ {a _ {2}} N _ {A}\right) ^ {i _ {2}} \dots \left(\bar {\nabla} _ {a _ {n - 1}} N _ {A}\right) ^ {i _ {n - 1}}
$$

$$
\bar {g} _ {I J} \equiv \bar {g} _ {i _ {1} j _ {1}} \bar {g} _ {i _ {2} j _ {2}} \cdot \cdot \cdot \bar {g} _ {i _ {n - 1} j _ {n - 1}}
$$

$$
g _ {\vec {a} \vec {c}} \equiv g _ {a _ {1} c _ {1}} g _ {a _ {2} c _ {2}} \cdot \cdot \cdot g _ {a _ {n - 1} c _ {n - 1}}.
$$

We now introduce the main objects of our study

(3.3)

$$
\mathcal {P} ^ {i J} = \frac {1}{\sqrt {(n - 1) !}} \{x ^ {i}, \vec {x} ^ {J} \} = \frac {1}{\sqrt {(n - 1) !}} \frac {\varepsilon^ {a \vec {a}}}{\rho} \left(\partial_ {a} x ^ {i}\right) \left(\partial_ {\vec {a}} \vec {x} ^ {J}\right)\tag{3.4}
$$

$$
\mathcal {S} _ {A} ^ {i J} = \frac {(- 1) ^ {n}}{\sqrt {(n - 1) !}} \frac {\varepsilon^ {a \vec {a}}}{\rho} \left(\partial_ {a} x ^ {i}\right) \left(\bar {\nabla} _ {\vec {a}} \vec {n} _ {A}\right) ^ {J}\tag{3.5}
$$

$$
\mathcal {T} _ {A} ^ {I j} = \frac {(- 1) ^ {n}}{\sqrt {(n - 1) !}} \frac {\varepsilon^ {\vec {a} a}}{\rho} \left(\partial_ {\vec {a}} \vec {x} ^ {I}\right) \left(\bar {\nabla} _ {a} N _ {A}\right) ^ {j}
$$

from which we construct

(3.6)

$$
\left(\mathcal {P} ^ {2}\right) ^ {i k} = \mathcal {P} ^ {i I} \mathcal {P} ^ {k J} \bar {g} _ {I J}\tag{3.7}
$$

$$
\left(\mathcal {B} _ {A}\right) ^ {i k} = \mathcal {P} ^ {i I} \left(\mathcal {T} _ {A}\right) ^ {J k} \bar {g} _ {I J}\tag{3.8}
$$

$$
\left(\mathcal {S} _ {A} \mathcal {T} _ {A}\right) ^ {i k} = \left(\mathcal {S} _ {A}\right) ^ {i I} \left(\mathcal {T} _ {A}\right) ^ {J k} \bar {g} _ {I J}.
$$

By lowering the second index with the metric $\bar{g}$, we will also consider $\mathcal{P}^2$, $\mathcal{B}_A$ and $\mathcal{T}_AS_A$ as maps $TM \to TM$. Note that both $\mathcal{S}_A$ and $\mathcal{T}_A$ can be written in terms of Nambu brackets, e.g.

$$
\mathcal {T} _ {A} ^ {I j} = \frac {(- 1) ^ {n}}{\sqrt {(n - 1) !}} \Big [ \{\vec {x} ^ {I}, n _ {A} ^ {j} \} + \{\vec {x} ^ {I}, x ^ {k} \} \bar {\Gamma} _ {k l} ^ {j} n _ {A} ^ {l} \Big ].
$$

Let us now investigate some properties of the maps defined above. As it will appear frequently, we define

$$
\gamma = \frac {\sqrt {g}}{\rho}.\tag{3.9}
$$

It is useful to note that (cp. Proposition 3.3)

$$
\gamma^ {2} = \sum_ {i, j, I, J = 1} ^ {m} \frac {1}{n !} \bar {g} _ {i j} \{x ^ {i}, \vec {x} ^ {I} \} \bar {g} _ {I J} \{x ^ {j}, \vec {x} ^ {J} \},
$$

and to recall the cofactor expansion of the inverse of a matrix:

Lemma 3.1. Let  $g^{ab}$  denote the inverse of  $g_{ab}$  and  $g = \det(g_{ab})$ . Then

$$
g g ^ {b a} = \frac {1}{(n - 1) !} \varepsilon^ {a a _ {1} \dots a _ {n - 1}} \varepsilon^ {b b _ {1} \dots b _ {n - 1}} g _ {a _ {1} b _ {1}} g _ {a _ {2} b _ {2}} \dots g _ {a _ {n - 1} b _ {n - 1}}.\tag{3.10}
$$

Proposition 3.2. For  $X \in TM$  it holds that

(3.11)

$$
\mathcal {P} ^ {2} (X) = \gamma^ {2} \bar {g} (X, e _ {a}) g ^ {a b} e _ {b}\tag{3.12}
$$

$$
\mathcal {B} _ {A} (X) = - \gamma^ {2} \bar {g} (X, \bar {\nabla} _ {a} N _ {A}) g ^ {a b} e _ {b}\tag{3.13}
$$

$$
\mathcal {S} _ {A} \mathcal {T} _ {A} (X) = \gamma^ {2} (\det W _ {A}) \bar {g} (X, \bar {\nabla} _ {a} N _ {A}) h _ {A} ^ {a b} e _ {b},
$$

and for $Y\in T\Sigma$ one obtains

(3.14)

$$
\mathcal {P} ^ {2} (Y) = \gamma^ {2} Y\tag{3.15}
$$

$$
\mathcal {B} _ {A} (Y) = \gamma^ {2} W _ {A} (Y)\tag{3.16}
$$

$$
\mathcal {S} _ {A} \mathcal {T} _ {A} (Y) = - \gamma^ {2} (\det W _ {A}) Y.
$$

Proof. Let us provide a proof for equations (3.11) and (3.14); the other formulas can be proved analogously.

$$
\begin{array}{r l} & {\mathcal {P} ^ {2} (X) = \mathcal {P} ^ {i I} \mathcal {P} ^ {j J} \bar {g} _ {I J} \bar {g} _ {j k} X ^ {k} \partial_ {i} = \frac {\varepsilon^ {a \vec {a}} \varepsilon^ {c \vec {c}}}{\rho^ {2} (n - 1) !} (\partial_ {a} x ^ {i}) (\partial_ {\vec {a}} x ^ {I}) (\partial_ {c} x ^ {j}) (\partial_ {\vec {c}} x ^ {J}) \bar {g} _ {I J} \bar {g} _ {j k} X ^ {k} \partial_ {i}} \\ & {\qquad = \frac {\varepsilon^ {a \vec {a}} \varepsilon^ {c \vec {c}}}{\rho^ {2} (n - 1) !} g _ {a _ {1} c _ {1}} \dots g _ {a _ {n - 1} c _ {n - 1}} (\partial_ {a} x ^ {i}) (\partial_ {c} x ^ {j}) \bar {g} _ {j k} X ^ {k} \partial_ {i}} \\ & {\qquad = \gamma^ {2} g ^ {a c} (\partial_ {a} x ^ {i}) (\partial_ {c} x ^ {j}) \bar {g} _ {j k} X ^ {k} \partial_ {i} = \gamma^ {2} \bar {g} (X, e _ {c}) g ^ {c a} e _ {a}.} \end{array}
$$

Choosing a tangent vector $Y = Y^{c}e_{c}$ gives immediately that $\mathcal{P}^2 (Y) = \gamma^2 Y$.

For a map $\mathcal{B}: TM \to TM$ we denote the trace by $\operatorname{Tr} \mathcal{B} \equiv \mathcal{B}_i^i$ and for a map $W: T\Sigma \to T\Sigma$ we denote the trace by $\operatorname{tr} W \equiv W_a^a$.

Proposition 3.3. It holds that

(3.17)

$$
\frac {1}{n} \operatorname{Tr} \mathcal {P} ^ {2} = \gamma^ {2}\tag{3.18}
$$

$$
\mathrm{Tr} \mathcal {B} _ {A} = \gamma^ {2} \mathrm{tr} W _ {A}\tag{3.19}
$$

$$
\frac {1}{n} \operatorname{Tr} \mathcal {S} _ {A} \mathcal {T} _ {A} = - \gamma^ {2} (\det W _ {A}).
$$

Remark 3.4. For a hypersurface (with normal $N = n^i\partial_i$) in $\mathbb{R}^{n + 1}$,

$$
\begin{array}{r l} & {\det W = (- 1) ^ {n} \frac {\{x ^ {i _ {1}} , \ldots , x ^ {i _ {n}} \} \{n _ {i _ {1}} , \ldots , n _ {i _ {n}} \}}{\{x ^ {k _ {1}} , \ldots , x ^ {k _ {n}} \} \{x _ {k _ {1}} , \ldots , x _ {k _ {n}} \}}} \\ & {\qquad = \frac {1}{\gamma n !} \varepsilon^ {i _ {1} \dots i _ {n} i} \{n _ {i _ {1}}, \ldots , n _ {i _ {n}} \} n _ {i},} \end{array}\tag{3.20}
$$

the signed ratio of infinitesimal volumes swept out on  $S^{n}$  (by N), resp  $\Sigma$  (which can easily be obtained directly by simply writing out the determinant of the second fundamental form,  $h = \det(-\partial_{a}x^{i}\partial_{b}n_{i})$ ); in fact, all the symmetric functions of the principal curvatures are related to ratios of products of two Nambu brackets (cp. the paragraph after Proposition 3.11). Namely, the k'th symmetric curvature is given by

$$
(- 1) ^ {k} \frac {\{x ^ {i _ {1}} , \ldots , x ^ {i _ {n}} \} \{n _ {i _ {1}} , \ldots , n _ {i _ {k}} , x _ {i _ {k + 1}} , \ldots , x _ {i _ {n}} \}}{\{x ^ {k _ {1}} , \ldots , x ^ {k _ {n}} \} \{x _ {k _ {1}} , \ldots , x _ {k _ {n}} \}}.\tag{3.21}
$$

A direct consequence of Propositions 3.2 and 3.3 is that one can write the projection onto  $T\Sigma$ , as well as the mean curvature vector, in terms of Nambu brackets.

Proposition 3.5. The map

$$
\gamma^ {- 2} \mathcal {P} ^ {2} = \frac {n}{\mathrm{Tr} \mathcal {P} ^ {2}} \mathcal {P} ^ {2}: T M \to T \Sigma\tag{3.22}
$$

is the orthogonal projection of TM onto  $T\Sigma$ . Furthermore, the mean curvature vector can be written as

$$
H = \frac {1}{\mathrm{Tr} \mathcal {P} ^ {2}} \sum_ {A = 1} ^ {p} \big (\mathrm{Tr} \mathcal {B} _ {A} \big) N _ {A}.
$$

Proposition 3.2 tells us that $\gamma^{-2}\mathcal{B}_A$ equals the Weingarten map $W_{A}$, when restricted to $T\Sigma$. What is the geometrical meaning of $\mathcal{B}_A$ acting on a normal vector? It turns out that the maps $\mathcal{B}_A$ also provide information about the covariant derivative in the normal space. If one defines $(D_X)_{AB}$ through

$$
D _ {X} N _ {A} = \sum_ {B = 1} ^ {p} (D _ {X}) _ {A B} N _ {B}
$$

for $X \in T\Sigma$, then one can prove the following relation to the maps $\mathcal{B}_A$.

Proposition 3.6. For $X \in T\Sigma$ it holds that

$$
\bar {g} \big (\mathcal {B} _ {B} (N _ {A}), X \big) = \gamma^ {2} \big (D _ {X} \big) _ {A B}.\tag{3.23}
$$

Proof. For a vector $X = X^{a}e_{a}$, it follows from Weingarten's formula (2.2) that

$$
\left(D _ {X}\right) _ {A B} = \bar {g} \left(\bar {\nabla} _ {X} N _ {A}, N _ {B}\right).
$$

On the other hand, with the formula from Proposition 3.2, one computes

$$
\begin{array}{r l} & {\bar {g} \big (\mathcal {B} _ {B} (N _ {A}), X \big) = - \gamma^ {2} \bar {g} \big (N _ {A}, \bar {\nabla} _ {a} N _ {B} \big) g ^ {a b} g _ {b c} X ^ {c} = - \gamma^ {2} \bar {g} \big (N _ {A}, \bar {\nabla} _ {X} N _ {B} \big)} \\ & {\qquad = - \gamma^ {2} (D _ {X}) _ {B A} = \gamma^ {2} (D _ {X}) _ {A B}.} \end{array}
$$

The last equality is due to the fact that $D$ is a covariant derivative, which implies that $0 = D_X\bar{g}(N_A,N_B) = \bar{g}(D_XN_A,N_B) + \bar{g}(N_A,D_XN_B)$.

Thus, one can write Weingarten's formula as

$$
\gamma^ {2} \bar {\nabla} _ {X} N _ {A} = - \mathcal {B} _ {A} (X) + \sum_ {B = 1} ^ {p} \bar {g} \big (\mathcal {B} _ {B} (N _ {A}), X \big) N _ {B},\tag{3.24}
$$

and since $h_A(X,Y) = \gamma^{-2}\bar{g}(\mathcal{B}_A(X),Y)$ Gauss' formula becomes

$$
\bar {\nabla} _ {X} Y = \nabla_ {X} Y + \frac {1}{\gamma^ {2}} \sum_ {A = 1} ^ {p} \bar {g} \big (\mathcal {B} _ {A} (X), Y \big) N _ {A}.\tag{3.25}
$$

Let us now turn our attention to the curvature of  $\Sigma$ . Since Nambu brackets involve sums over all vectors in the basis of  $T\Sigma$ , one can not expect to find expressions for quantities that involve a choice of tangent plane, e.g. the sectional curvature (unless  $\Sigma$  is a surface). However, it turns out that one can write the Ricci curvature as an expression involving Nambu brackets.

Theorem 3.7. Let R be the Ricci curvature of  $\Sigma$ , considered as a map  $T\Sigma \to T\Sigma$ , and let R denote the scalar curvature. For any  $X \in T\Sigma$  it holds that

(3.26)

$$
\mathcal {R} (X) = \frac {1}{\gamma^ {4}} \big (\mathcal {P} ^ {2} \big) ^ {i k} \big (\mathcal {P} ^ {2} \big) ^ {l m} \bar {R} _ {i j k l} X ^ {j} \partial_ {m} + \frac {1}{\gamma^ {4}} \sum_ {A = 1} ^ {p} \Big [ (\mathrm{Tr} \mathcal {B} _ {A}) \mathcal {B} _ {A} (X) - \mathcal {B} _ {A} ^ {2} (X) \Big ]\tag{3.27}
$$

$$
R = \frac {1}{\gamma^ {4}} \big (\mathcal {P} ^ {2} \big) ^ {i k} \big (\mathcal {P} ^ {2} \big) ^ {j l} \bar {R} _ {i j k l} + \frac {1}{\gamma^ {4}} \sum_ {A = 1} ^ {p} \Big [ \big (\mathrm{Tr} \mathcal {B} _ {A} \big) ^ {2} - \mathrm{Tr} \mathcal {B} _ {A} ^ {2} (X) \Big ],
$$

where $\bar{R}$ is the curvature tensor of $M$.

Proof. The Ricci curvature of $\Sigma$ is defined as

$$
\mathcal {R} _ {b} ^ {p} = g ^ {a c} g ^ {p d} g \big (R (e _ {c}, e _ {d}) e _ {b}, e _ {a} \big)
$$

and from Gauss' equation (2.6) it follows that

$$
\mathcal {R} _ {b} ^ {p} = g ^ {p d} g ^ {a c} \bar {g} \big (\bar {R} (e _ {c}, e _ {d}) e _ {b}, e _ {a} \big) + g ^ {a c} g ^ {p d} \sum_ {A = 1} ^ {p} \Big (h _ {A, b d} h _ {A, a c} - h _ {A, b c} h _ {A, a d} \Big).
$$

Since $(W_A)_b^a = g^{ac}h_{A,cb}$ one obtains

$$
\mathcal {R} _ {b} ^ {p} = g ^ {a c} g ^ {p d} \bar {g} \big (\bar {R} (e _ {c}, e _ {d}) e _ {b}, e _ {a} \big) + \sum_ {A = 1} ^ {p} \Big [ \big (\operatorname{tr} W _ {A} \big) (W _ {A}) _ {b} ^ {p} - (W _ {A} ^ {2}) _ {b} ^ {p} \Big ],
$$

and as $\mathcal{B}_A(X) = \gamma^2 W_A(X)$ for any $X\in T\Sigma$, and $\mathrm{Tr}\mathcal{B}_A = \gamma^2\mathrm{tr}W_A$, one has

$$
\mathcal {R} (X) = g ^ {a c} g ^ {p d} \bar {g} \big (\bar {R} (e _ {c}, e _ {d}) e _ {b}, e _ {a} \big) X ^ {b} e _ {p} + \frac {1}{\gamma^ {4}} \sum_ {A = 1} ^ {p} \Big [ \big (\mathrm{Tr} \mathcal {B} _ {A} \big) \mathcal {B} _ {A} (X) - \mathcal {B} _ {A} ^ {2} (X) \Big ].
$$

By expanding the first term as

$$
\begin{array}{r l} & g ^ {a c} g ^ {p d} X ^ {b} \bar {R} _ {i j k l} (\partial_ {a} x ^ {i}) (\partial_ {b} x ^ {j}) (\partial_ {c} x ^ {k}) (\partial_ {d} x ^ {l}) (\partial_ {p} x ^ {m}) \partial_ {m} \\ & = \frac {1}{g ^ {2} (n - 1) ! ^ {2}} \varepsilon^ {p \vec {p}} \varepsilon^ {d \vec {d}} g _ {\vec {p} \vec {d}} \varepsilon^ {a \vec {a}} \varepsilon^ {c \vec {c}} g _ {\vec {a} \vec {c}} X ^ {b} \bar {R} _ {i j k l} (\partial_ {a} x ^ {i}) (\partial_ {b} x ^ {j}) (\partial_ {c} x ^ {k}) (\partial_ {d} x ^ {l}) (\partial_ {p} x ^ {m}) \partial_ {m} \\ & = \ldots = \frac {1}{\gamma^ {4}} (\mathcal {P} ^ {2}) ^ {i k} (\mathcal {P} ^ {2}) ^ {l m} \bar {R} _ {i j k l} X ^ {j} \partial_ {m} \end{array}
$$

one obtains the desired result.

3.1. Construction of normal vectors. The results in Section 3 involve Nambu brackets of the embedding coordinates and the components of the normal vectors. In this section we will prove that one can replace sums over normal vectors by sums of Nambu brackets of the embedding coordinates, thus providing expressions that do not involve normal vectors.

It will be convenient to introduce yet another multi-index; namely, we let  $\alpha = i_{1} \ldots i_{p-1}$  consist of p - 1 indices all taking values between 1 and m.

Proposition 3.8. For any value of the multi-index  $\alpha$ , the vector

$$
Z _ {\alpha} = \frac {1}{\gamma (n ! \sqrt {(p - 1) !})} \bar {g} ^ {i j} \varepsilon_ {j k _ {1} \dots k _ {n} \alpha} \{x ^ {k _ {1}}, \ldots , x ^ {k _ {n}} \} \partial_ {i},\tag{3.28}
$$

where  $\varepsilon_{i_{1}\cdots i_{m}}$  is the Levi-Civita tensor of M, is normal to  $T\Sigma$ , i.e.  $\bar{g}(Z_{\alpha}, e_{a}) = 0$  for  $a = 1, 2, \ldots, n$ . For hypersurfaces (p = 1), equation (3.28) defines a unique normal vector of unit length.

Proof. To prove that  $Z_{\alpha}$  are normal vectors, one simply notes that

$$
\gamma \big (n! \sqrt {(p - 1) !} \big) \bar {g} (Z _ {\alpha}, e _ {a}) = \frac {1}{\rho} \varepsilon^ {a _ {1} \dots a _ {n}} \varepsilon_ {j k _ {1} \dots k _ {n} \alpha} \big (\partial_ {a} x ^ {j} \big) \big (\partial_ {a _ {1}} x ^ {k _ {1}} \big) \cdot \cdot \cdot \big (\partial_ {a _ {n}} x ^ {k _ {n}} \big) = 0,
$$

since the  $n+1$  indices  $a, a_{1}, \ldots, a_{n}$  can only take on n different values and since  $(\partial_{a}x^{j})(\partial_{a_{1}}x^{k_{1}})\cdots(\partial_{a_{n}}x^{k_{n}})$  is contracted with  $\varepsilon_{jk_{1}\ldots k_{n}\alpha}$  which is completely antisymmetric in  $j, k_{1}, \ldots, k_{n}$ . Let us now calculate  $|Z|^{2} \equiv \bar{g}(Z, Z)$  when p = 1. Using

that $^{1}$

$$
\varepsilon_ {i k _ {1} \dots k _ {n}} \varepsilon^ {i l _ {1} \dots l _ {n}} = \delta_ {[ k _ {1}} ^ {[ l _ {1}} \cdot \cdot \cdot \delta_ {k _ {n} ]} ^ {l _ {n} ]}
$$

one obtains

$$
\begin{array}{r l} & {| Z | ^ {2} = \frac {1}{\gamma^ {2} n ! ^ {2}} \bar {g} _ {l _ {1} l _ {1} ^ {\prime}} \dots \bar {g} _ {l _ {n} l _ {n} ^ {\prime}} \varepsilon_ {i k _ {1} \dots k _ {n}} \varepsilon^ {i l _ {1} \dots l _ {n}} \{x ^ {k _ {1}}, \ldots , x ^ {k _ {n}} \} \{x ^ {l _ {1} ^ {\prime}}, \ldots , x ^ {l _ {n} ^ {\prime}} \}} \\ & {\quad = \frac {1}{\gamma^ {2} n ! ^ {2}} \bar {g} _ {l _ {1} l _ {1} ^ {\prime}} \dots \bar {g} _ {l _ {n} l _ {n} ^ {\prime}} \delta_ {[ k _ {1}} ^ {[ l _ {1}} \dots \delta_ {k _ {n} ]} ^ {[ l _ {n} ]} \{x ^ {k _ {1}}, \ldots , x ^ {k _ {n}} \} \{x ^ {l _ {1} ^ {\prime}}, \ldots , x ^ {l _ {n} ^ {\prime}} \}} \\ & {\quad = \frac {1}{\gamma^ {2} n !} \{x ^ {l _ {1}}, \ldots , x ^ {l _ {n}} \} \bar {g} _ {l _ {1} l _ {1} ^ {\prime}} \dots \bar {g} _ {l _ {n} l _ {n} ^ {\prime}} \{x ^ {l _ {1} ^ {\prime}}, \ldots , x ^ {l _ {n} ^ {\prime}} \}} \\ & {\quad = \frac {1}{\gamma^ {2} n !} (n - 1)! \mathrm{Tr} \mathcal {P} ^ {2} = \frac {1}{\gamma^ {2} n !} (n - 1)! n \gamma^ {2} = 1,} \end{array}
$$

which proves that Z has unit length.

If the codimension is greater than one,  $Z_{\alpha}$  defines more than p non-zero normal vectors that do not in general fulfill any orthonormality conditions. In principle, one can now apply the Gram-Schmidt orthonormalization procedure to obtain a set of p orthonormal vectors. However, it turns out that one can use  $Z_{\alpha}$  to construct another set of normal vectors, avoiding explicit use of the Gram-Schmidt procedure; namely, introduce

$$
\mathcal {Z} _ {\alpha} ^ {\beta} = \bar {g} (Z _ {\alpha}, Z ^ {\beta}),
$$

and consider it as a matrix over multi-indices  $\alpha$  and  $\beta$ . As such, the matrix is symmetric (with respect to  $\bar{g}_{\alpha\beta} \equiv \bar{g}_{i_{1}j_{1}} \cdots \bar{g}_{i_{p-1}j_{p-1}}$ ) and we let  $E_{\alpha}^{\beta}, \mu_{\alpha}$  denote orthonormal eigenvectors (i.e.  $\bar{g}_{\delta\sigma} E_{\alpha}^{\delta} E_{\beta}^{\sigma} = \delta_{\alpha\beta}$ ) and their corresponding eigenvalues. Using these eigenvectors to define

$$
\hat {N} _ {\alpha} = E _ {\alpha} ^ {\beta} Z _ {\beta}
$$

one finds that $\bar{g} (\hat{N}_{\alpha},\hat{N}_{\beta}) = \mu_{\alpha}\delta_{\alpha \beta}$, i.e. the vectors are orthogonal.

Proposition 3.9. For  $Z_{\alpha}^{\beta} = \bar{g}_{ij} Z_{\alpha}^{i} Z^{j\beta}$  it holds that

(3.29)

$$
\mathcal {Z} _ {\alpha} ^ {\delta} \mathcal {Z} _ {\delta} ^ {\beta} = \mathcal {Z} _ {\alpha} ^ {\beta}\tag{3.30}
$$

$$
\mathcal {Z} _ {\alpha} ^ {\alpha} = p.
$$

Proof. Both statements can be easily proved once one has the following result

$$
Z _ {\alpha} ^ {i} Z ^ {j \alpha} = \bar {g} ^ {i j} - \frac {1}{\gamma^ {2}} \big (\mathcal {P} ^ {2} \big) ^ {i j},\tag{3.31}
$$

which is obtained by using that

$$
\varepsilon_ {k k _ {1} \dots k _ {n} \alpha} \varepsilon^ {l l _ {1} \dots l _ {n} \alpha} = (p - 1)! \left(\delta_ {[ k} ^ {[ l} \delta_ {k _ {1}} ^ {l _ {1}} \dots \delta_ {k _ {n} ]} ^ {l _ {n} ]}\right).
$$

Formula (3.30) is now immediate, and to obtain (3.29) one notes that since  $Z_{\alpha} \in T\Sigma^{\perp}$  it holds that  $\mathcal{P}^{2}(Z_{\alpha}) = 0$ , due to the fact that  $P^{2}$  is proportional to the projection onto  $T\Sigma$ . ☐

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\delta_{[k}^{[i}}\delta_{l]}^{j]} = \delta_{k}^{i}\delta_{l}^{j} - \delta_{l}^{i}\delta_{k}^{j}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$ In our convention, no combinatorial factor is included in the anti-symmetrization; for instance,  $\delta_{[k}^{[i}}\delta_{l]}^{j]} = \delta_{k}^{i}\delta_{l}^{j} - \delta_{l}^{i}\delta_{k}^{j}$ .</span></small>

From Proposition 3.9 it follows that an eigenvalue of $\mathcal{Z}$ is either 0 or 1, which implies that $\hat{N}_{\alpha} = 0$ or $\bar{g} (\hat{N}_{\alpha},\hat{N}_{\alpha}) = 1$, and that the number of non-zero vectors is $\mathrm{Tr}\mathcal{Z} = \mathcal{Z}_{\alpha}^{\alpha} = p$. Hence, the $p$ non-zero vectors among $\hat{N}_{\alpha}$ constitute an orthonormal basis of $T\Sigma^{\perp}$, and it follows that one can replace any sum over normal vectors $N_{A}$ by a sum over the multi-index of $\hat{N}_{\alpha}$. As an example, let us work out some explicit expressions in the case when $M = \mathbb{R}^m$.

Proposition 3.10. Assume that  $M = R^{m}$  and that all repeated indices are summed over. For any  $X \in T\Sigma$  one has

(3.32)

$$
\sum_ {A = 1} ^ {p} \big (\mathrm{Tr} \mathcal {B} _ {A} \big) \mathcal {B} _ {A} (X) ^ {i} = \frac {1}{(n - 1) ! ^ {2}} \Pi^ {j k} \{\{x ^ {j}, \vec {x} ^ {J} \}, \vec {x} ^ {J} \} \{x ^ {i}, \vec {x} ^ {I} \} \{X ^ {k}, \vec {x} ^ {I} \}\tag{3.33}
$$

$$
\sum_ {A = 1} ^ {p} \mathcal {B} _ {A} ^ {2} (X) ^ {i} = \frac {1}{(n - 1) ! ^ {2}} \Pi^ {j k} \{x ^ {i}, \vec {x} ^ {I} \} \{\{x ^ {j}, \vec {x} ^ {J} \} \{X ^ {k}, \vec {x} ^ {J} \}, \vec {x} ^ {I} \}\tag{3.34}
$$

$$
\sum_ {A = 1} ^ {p} \big (\mathrm{Tr} \mathcal {B} _ {A} \big) N _ {A} ^ {i} = \frac {(- 1) ^ {n}}{(n - 1) !} \Pi^ {i k} \{\{x ^ {k}, \vec {x} ^ {I} \}, \vec {x} ^ {I} \}
$$

where

$$
\Pi^ {i j} = \delta^ {i j} - \frac {1}{\gamma^ {2}} \left(\mathcal {P} ^ {2}\right) ^ {i j}\tag{3.35}
$$

is the projection onto the normal space.

Proof. Let us prove formula (3.32); the other formulas can be proven analogously. One rewrites

$$
\begin{array}{r} \big (\mathrm{Tr} \mathcal {B} _ {A} \big) \mathcal {B} _ {A} (X) ^ {i} = \frac {1}{(n - 1) ! ^ {2}} \{x ^ {j}, \vec {x} ^ {J} \} \{\vec {x} ^ {J}, n _ {A} ^ {j} \} \{x ^ {i}, \vec {x} ^ {I} \} \{\vec {x} ^ {I}, n _ {A} ^ {k} \} X ^ {k} \\ = \frac {1}{(n - 1) ! ^ {2}} n _ {A} ^ {j} n _ {A} ^ {k} \{\vec {x} ^ {J}, \{x ^ {j}, \vec {x} ^ {J} \} \} \{x ^ {i}, \vec {x} ^ {I} \} \{\vec {x} ^ {I}, X ^ {k} \} \end{array}
$$

since  $n_{A}^{j}\{x^{j},\vec{x}^{J}\}=n_{A}^{k}X^{k}=0$ , due to the fact that  $N_{A}$  is a normal vector. By replacing  $n_{A}^{j}n_{A}^{k}$  with  $\hat{N}_{\alpha}^{j}\hat{N}_{\alpha}^{k}$  and using the fact that

$$
\hat {N} _ {\alpha} ^ {i} \hat {N} _ {\alpha} ^ {j} = \delta^ {i j} - \frac {1}{\gamma^ {2}} \big (\mathcal {P} ^ {2} \big) ^ {i j}
$$

one obtains

$$
\big (\operatorname{Tr} \mathcal {B} _ {A} \big) \mathcal {B} _ {A} (X) ^ {i} = \frac {1}{(n - 1) ! ^ {2}} \Pi^ {j k} \{\{x ^ {j}, \vec {x} ^ {J} \}, \vec {x} ^ {J} \} \{x ^ {i}, \vec {x} ^ {I} \} \{X ^ {k}, \vec {x} ^ {I} \}.
$$

For hypersurfaces in  $R^{n+1}$ , the “Theorema Egregium” states that the determinant of the Weingarten map, i.e. the “Gaussian curvature”, is an invariant (up to a sign when  $\Sigma$  is odd-dimensional) under isometries (this is in fact also true for hypersurfaces in a manifold of constant sectional curvature). From Proposition 3.3 we know that one can express  $\det W_{A}$  in terms of  $Tr S_{A} T_{A}$ .

Proposition 3.11. Let $\Sigma$ be a hypersurface in $\mathbb{R}^{n + 1}$ and let $W$ denote the Weingarten map with respect to the unit normal

$$
Z = \frac {1}{\gamma n !} \bar {g} ^ {i j} \varepsilon_ {j k K} \{x ^ {k}, \vec {x} ^ {K} \}.
$$

Then one can write det W as

$$
\begin{array}{r l} \det W = - \frac {1}{\gamma (\gamma n !) ^ {n + 1}} \sum \varepsilon_ {i l L} \varepsilon_ {j _ {1} k _ {1} K _ {1}} \dots \varepsilon_ {j _ {n - 1} k _ {n - 1} K _ {n - 1}} \\ & \times \{x ^ {i}, \{x ^ {k _ {1}}, \vec {x} ^ {K _ {1}} \}, \ldots , \{x ^ {k _ {n - 1}}, \vec {x} ^ {K _ {n - 1}} \} \} \{\vec {x} ^ {J}, \{x ^ {l}, \vec {x} ^ {L} \} \}. \end{array}
$$

In fact, one can express all the elementary symmetric functions of the principle curvatures in terms of Nambu brackets as follows: The elementary symmetric functions of the eigenvalues of W is given (up to a sign) as the coefficients of the polynomial  $\det(W-t11)$ . Since  $\mathcal{B}(X)=0$  for all  $X\in T\Sigma^{\perp}$  and  $\mathcal{B}(X)=\gamma^{2}W(X)$  for all  $X\in T\Sigma$ , it holds that

$$
- t \det (W - t \mathbb {1} _ {n}) = \det (\gamma^ {- 2} \mathcal {B} - t \mathbb {1} _ {n + 1}) = \frac {1}{\gamma^ {2 (n + 1)}} \det (\mathcal {B} - t \gamma^ {2} \mathbb {1} _ {n + 1})
$$

which implies that the coefficient of $t^k$ in $\det(W - t\mathbb{1})$ is given by the coefficient of $t^{k + 1}$ in $-\det(\mathcal{B} - t\gamma^2\mathbb{1})\gamma^{2(n - k)}$.

3.2. The Codazzi-Mainardi equations. When studying the geometry of embedded manifolds, the Codazzi-Mainardi equations are very useful. In this section we reformulate these equations in terms of Nambu brackets.

The Codazzi-Mainardi equations express the normal component of  $\bar{R}(X,Y)Z$  in terms of the second fundamental forms; namely

$$
\begin{array}{l} \bar {g} \big (\bar {R} (X, Y) Z, N _ {A} \big) = \big (\nabla_ {X} h _ {A} \big) (Y, Z) - \big (\nabla_ {Y} h _ {A} \big) (X, Z) \\ + \sum_ {A = 1} ^ {p} \Big [ \bar {g} (D _ {X} N _ {B}, N _ {A}) h _ {B} (Y, Z) - \bar {g} (D _ {Y} N _ {B}, N _ {A}) h _ {B} (X, Z) \Big ], \end{array}\tag{3.36}
$$

for $X,Y,Z\in T\Sigma$ and $A = 1,\ldots ,p$. Defining

$$
\begin{array}{l} \mathcal {W} _ {A} (X, Y) = (\nabla_ {X} W _ {A}) (Y) - (\nabla_ {Y} W _ {A}) (X) \\ \qquad + \sum_ {B = 1} ^ {p} \left[ \bar {g} (D _ {X} N _ {B}, N _ {A}) W _ {B} (Y) - \bar {g} (D _ {Y} N _ {B}, N _ {A}) W _ {B} (X) \right] \end{array}\tag{3.37}
$$

one can rewrite the Codazzi-Mainardi equations as follows.

Proposition 3.12. Let $\Pi$ denote the projection onto $T\Sigma^{\perp}$. Then the Codazzi-Mainardi equations are equivalent to

$$
\mathcal {W} _ {A} (X, Y) = - (\mathbb {1} - \Pi) \big (\bar {R} (X, Y) N _ {A} \big)\tag{3.38}
$$

for $X,Y\in T\Sigma$ and $A = 1,\ldots ,p$

Proof. Since $h_A(X,Y) = \bar{g}(W_A(X),Y)$ (by Weingarten's equation) one can rewrite (3.36) as

$$
\bar {g} \big (\mathcal {W} _ {A} (X, Y), Z \big) = \bar {g} \big (\bar {R} (X, Y) Z, N _ {A} \big),\tag{3.39}
$$

and since $\bar{g} (\bar{R} (X,Y)Z,N_A) = -\bar{g} (\bar{R} (X,Y)N_A,Z)$ this becomes

$$
\bar {g} \big (\mathcal {W} _ {A} (X, Y) + \bar {R} (X, Y) N _ {A}, Z \big) = 0.\tag{3.40}
$$

That this holds for all  $Z \in T\Sigma$  is equivalent to saying that

$$
(\mathbb {1} - \Pi) \big (\mathcal {W} _ {A} (X, Y) + \bar {R} (X, Y) N _ {A} \big) = 0,\tag{3.41}
$$

from which (3.38) follows since $\mathcal{W}_A(X,Y)\in T\Sigma$.

Note that since  $\gamma^{-2}P^{2}$  is the projection onto  $T\Sigma$  one can write (3.38) as

$$
\gamma^ {2} \mathcal {W} _ {A} (X, Y) = - \mathcal {P} ^ {2} (\bar {R} (X, Y) N _ {A}).\tag{3.42}
$$

Since both  $W_{A}$  and  $D_{X}$  can be expressed in terms of  $B_{A}$ , one obtains the following expression for  $W_{A}$ :

Proposition 3.13. For $X, Y \in T\Sigma$ one has

$$
\begin{array}{l} \gamma^ {2} \mathcal {W} _ {A} (X, Y) = \big (\bar {\nabla} _ {X} \mathcal {B} _ {A} \big) (Y) - \big (\bar {\nabla} _ {Y} \mathcal {B} _ {A} \big) (X) \\ \qquad - \frac {1}{\gamma^ {2}} \Big [ \big (\nabla_ {X} \gamma^ {2} \big) \mathcal {B} _ {A} (Y) - \big (\nabla_ {Y} \gamma^ {2} \big) \mathcal {B} _ {A} (X) \Big ] \\ \qquad + \frac {1}{\gamma^ {2}} \sum_ {B = 1} ^ {p} \Big [ \bar {g} \big (\mathcal {B} _ {A} (N _ {B}), X \big) \mathcal {B} _ {B} (Y) - \bar {g} \big (\mathcal {B} _ {A} (N _ {B}), Y \big) \mathcal {B} _ {B} (X) \Big ]. \end{array}
$$

As the aim is to express the Codazzi-Mainardi equations in terms of Nambu brackets, we will introduce maps  $C_{A}$  that is defined in terms of  $W_{A}$  and can be written as expressions involving Nambu brackets.

Definition 3.14. The maps  $\mathcal{C}_{A}: C^{\infty}(\Sigma) \times \cdots \times C^{\infty}(\Sigma) \to T\Sigma$  are defined as

$$
\mathcal {C} _ {A} (f _ {1}, \ldots , f _ {n - 2}) = \frac {1}{2 \rho} \varepsilon^ {a b a _ {1} \dots a _ {n - 2}} \mathcal {W} _ {A} (e _ {a}, e _ {b}) (\partial_ {a _ {1}} f _ {1}) \dots (\partial_ {a _ {n - 2}} f _ {n - 2})\tag{3.43}
$$

for $A = 1, \ldots, p$ and $n \geqslant 3$. When $n = 2$, $\mathcal{C}_A$ is defined as

$$
\mathcal {C} _ {A} = \frac {1}{2 \rho} \varepsilon^ {a b} \mathcal {W} _ {A} (e _ {a}, e _ {b}).
$$

Proposition 3.15. Let $\{g_1, g_2\}_f \equiv \{g_1, g_2, f_1, \ldots, f_{n-2}\}$. Then

$$
\begin{array}{r l} & {\mathcal {C} _ {A} (f _ {1}, \ldots , f _ {n - 2}) ^ {i} = \left\{\gamma^ {- 2} (\mathcal {B} _ {A}) _ {k} ^ {i}, x ^ {k} \right\} _ {f} + \frac {1}{\gamma^ {2}} \left\{x ^ {j}, x ^ {l} \right\} _ {f} \left[ \bar {\Gamma} _ {j k} ^ {i} (\mathcal {B} _ {A}) _ {l} ^ {k} - (\mathcal {B} _ {A}) _ {k} ^ {i} \bar {\Gamma} _ {j l} ^ {k} \right]} \\ & {\qquad - \frac {1}{\gamma^ {2}} \sum_ {B = 1} ^ {p} \Big [ \left\{n _ {A} ^ {k}, x ^ {l} \right\} _ {f} (\mathcal {B} _ {B}) _ {l} ^ {i} + \bar {\Gamma} _ {l j} ^ {k} \left\{x ^ {l}, x ^ {m} \right\} _ {f} n _ {A} ^ {j} (\mathcal {B} _ {B}) _ {m} ^ {i} \Big ] (n _ {B}) _ {k}.} \end{array}
$$

Remark 3.16. In case $\Sigma$ is a hypersurface, the expression for $\mathcal{C} \equiv \mathcal{C}_1$ simplifies to

$$
\mathcal {C} (f _ {1}, \ldots , f _ {n - 2}) ^ {i} = \left\{\gamma^ {- 2} \mathcal {B} _ {k} ^ {i}, x ^ {k} \right\} _ {f} + \frac {1}{\gamma^ {2}} \left\{x ^ {j}, x ^ {l} \right\} _ {f} \left[ \bar {\Gamma} _ {j k} ^ {i} \mathcal {B} _ {l} ^ {k} - \mathcal {B} _ {k} ^ {i} \bar {\Gamma} _ {j l} ^ {k} \right],
$$

since $D_X N = 0$.

It follows from Proposition 3.12 that we can reformulate the Codazzi-Mainardi equations in terms of $\mathcal{C}_A$:

Theorem 3.17. For all $f_1, \ldots, f_{n-2} \in C^\infty(\Sigma)$ it holds that

$$
\gamma^ {2} \mathcal {C} _ {A} (f _ {1}, \ldots , f _ {n - 2}) = (\mathcal {P} ^ {2}) _ {j} ^ {i} \Big [ \{x ^ {k}, \bar {\Gamma} _ {k j ^ {\prime}} ^ {j} \} _ {f} - \{x ^ {k}, x ^ {l} \} _ {f} \bar {\Gamma} _ {l j ^ {\prime}} ^ {m} \bar {\Gamma} _ {k m} ^ {j} \Big ] n _ {A} ^ {j ^ {\prime}} \partial_ {i},\tag{3.44}
$$

for $A = 1, \ldots, p$, where $\{g_1, g_2\}_f = \{g_1, g_2, f_1, \ldots, f_{n-2}\}$.

Proof. As noted previously, one can write the Codazzi-Mainardi equations as

$$
\gamma^ {2} \mathcal {W} _ {A} (X, Y) = - \mathcal {P} ^ {2} \big (\bar {R} (X, Y) N _ {A} \big).
$$

That the above equation holds for all $X, Y \in T\Sigma$ is equivalent to saying that

$$
\gamma^ {2} \frac {1}{2 \rho} \varepsilon^ {a b a _ {1} \dots a _ {n - 2}} \mathcal {W} _ {A} (e _ {a}, e _ {b}) = - \frac {1}{2 \rho} \varepsilon^ {a b a _ {1} \dots a _ {n - 2}} \mathcal {P} ^ {2} \big (\bar {R} (e _ {a}, e _ {b}) N _ {A} \big)
$$

for all values of $a_1, \ldots, a_{n-2} \in \{1, \ldots, n\}$; furthermore, this is equivalent to

$$
\gamma^ {2} \mathcal {C} _ {A} (f _ {1}, \ldots , f _ {n - 2}) = - \frac {1}{2 \rho} \varepsilon^ {a b a _ {1} \dots a _ {n - 2}} \mathcal {P} ^ {2} \big (\bar {R} (e _ {a}, e _ {b}) N _ {A} \big) (\partial_ {a _ {1}} f _ {1}) \dots (\partial_ {a _ {n - 2}} f _ {n - 2})
$$

for all $f_1, \ldots, f_{n-2} \in C^\infty(\Sigma)$. It is now straightforward to show that

$$
\begin{array}{r l} & {- \frac {1}{2 \rho} \varepsilon^ {a b a _ {1} \dots a _ {n - 1}} \big (\bar {R} (e _ {a}, e _ {b}) N _ {A} \big) ^ {i} (\partial_ {a _ {1}} f _ {1}) \cdot \cdot \cdot (\partial_ {a _ {n - 2}} f _ {n - 2})} \\ & {\qquad = \Big (\{x ^ {k}, \bar {\Gamma} _ {k j} ^ {i} \} _ {f} - \{x ^ {k}, x ^ {l} \} _ {f} \bar {\Gamma} _ {l j} ^ {m} \bar {\Gamma} _ {k m} ^ {i} \Big) n _ {A} ^ {j},} \end{array}
$$

which proves the statement.

If $M$ is a space of constant curvature (in which case $\bar{g}(\bar{R}(X,Y)Z,N_A) = 0$), then Theorem 3.17 states that

$$
\mathcal {C} _ {A} (f _ {1}, \ldots , f _ {n - 2}) = 0\tag{3.45}
$$

for all $f_{1},\ldots ,f_{n - 2}\in C^{\infty}(\Sigma)$. Furthermore, if $M = \mathbb{R}^{m}$, then (3.44) becomes

$$
\gamma^ {2} \left\{\gamma^ {- 2} (\mathcal {B} _ {A}) _ {k} ^ {i}, x ^ {k} \right\} _ {f} - \sum_ {B = 1} ^ {p} \Big [ \left\{n _ {A} ^ {k}, x ^ {l} \right\} _ {f} (\mathcal {B} _ {B}) _ {l} ^ {i} \Big ] (n _ {B}) _ {k} = 0.\tag{3.46}
$$

3.3. Covariant derivatives. Equation (3.25) tells us that knowing $\bar{\nabla}_XY$, for $X, Y \in T\Sigma$, one can compute $\nabla_X Y$ through the formula

$$
\nabla_ {X} Y = \bar {\nabla} _ {X} Y - \frac {1}{\gamma^ {2}} \sum_ {A = 1} ^ {p} \bar {g} \big (\mathcal {B} _ {A} (X), Y \big) N _ {A},
$$

which requires explicit knowledge about the normal vectors. Are there other quantities involving  $\nabla$  that can be computed solely in terms of the embedding coordinates? We will now show that the two derivations

(3.47)

$$
D ^ {I} (u) \equiv \frac {1}{\gamma \sqrt {(n - 1) !}} \{u, \vec {x} ^ {I} \}\tag{3.48}
$$

$$
\mathcal {D} ^ {i} (u) \equiv \bar {g} _ {I J} D ^ {I} (x ^ {i}) D ^ {J} (u),
$$

can be considered as analogues of covariant derivatives on  $\Sigma$ . Their indices are lowered by the ambient metric  $\bar{g}_{ij}$ . Let us start by showing that several standard formulas involving covariant derivatives with contracted indices also hold for our newly defined derivations.

Proposition 3.18. For $u, v \in C^{\infty}(\Sigma)$ it holds that

(3.49)

$$
\nabla u = \mathcal {D} ^ {i} (u) \partial_ {i} = D _ {I} (u) D ^ {I} (x ^ {i}) \partial_ {i}\tag{3.50}
$$

$$
g \big (\nabla u, \nabla v \big) = \mathcal {D} _ {i} (u) \mathcal {D} ^ {i} (v) = D _ {I} (u) D ^ {I} (v)\tag{3.51}
$$

$$
\Delta (u) = \mathcal {D} _ {i} \mathcal {D} ^ {i} (u) = D _ {I} D ^ {I} (u)\tag{3.52}
$$

$$
\left| \nabla^ {2} u \right| ^ {2} = \mathcal {D} _ {i} \mathcal {D} ^ {j} (u) \mathcal {D} _ {j} \mathcal {D} ^ {i} (u) = D _ {I} D ^ {J} (u) D _ {J} D ^ {I} (u)
$$

Proof. The most convenient way of proving the above identities is to work in a coordinate system where  $u^{1},\ldots,u^{n}$  are normal coordinates. In particular, this implies that  $\Gamma_{bc}^{a}=0$ , which is equivalent to  $\bar{g}_{ij}(\partial_{a}x^{i})\partial_{bc}^{2}x^{j}=0$ . Let us now prove formula (3.52) for the operators  $D^{I}$ .

Let us first note that in normal coordinate one obtains

$$
\left| \nabla^ {2} u \right| ^ {2} \equiv \left(\nabla_ {a} \nabla_ {b} u\right) \left(\nabla_ {c} \nabla_ {d} u\right) g ^ {a c} g ^ {b d} = g ^ {a c} g ^ {b d} \left(\partial_ {a b} ^ {2} u\right) \left(\partial_ {c d} ^ {2} u\right).
$$

We now compute

$$
\begin{array}{r l} & D _ {I} D ^ {J} (u) D _ {J} D ^ {I} (u) = \frac {1}{\gamma^ {2} (n - 1) ! ^ {2}} \{\gamma^ {- 1} \{u, \vec {x} ^ {J} \}, \vec {x} ^ {K} \} \bar {g} _ {K I} \{\gamma^ {- 1} \{u, \vec {x} ^ {I} \}, \vec {x} ^ {L} \} \bar {g} _ {L J} \\ & = \frac {1}{g ^ {2} (n - 1) ! ^ {2}} \varepsilon^ {a \vec {a}} \partial_ {a} \big (\varepsilon^ {p \vec {p}} (\partial_ {p} u) (\partial_ {\vec {p}} \vec {x} ^ {J}) \big) \big (\partial_ {\vec {a}} \vec {x} ^ {K} \big) \bar {g} _ {K I} \varepsilon^ {c \vec {c}} \partial_ {c} \big (\varepsilon^ {q \vec {q}} (\partial_ {q} u) (\partial_ {\vec {q}} \vec {x} ^ {I}) \big) \big (\partial_ {\vec {c}} \vec {x} ^ {L} \big) \bar {g} _ {L J} \end{array}
$$

The terms involving  $\partial_{a}\partial_{\vec{p}}\vec{x}^{J}$  and  $\partial_{c}\partial_{\vec{q}}\vec{x}^{I}$  vanish since they appear in combinations such as  $(\partial_{a}\partial_{\vec{p}}\vec{x}^{J})(\partial_{\vec{c}}\vec{x}^{L})\bar{g}_{LJ}$  which is zero due to the presence of a normal coordinate system. Thus,

$$
\begin{array}{r} D _ {I} D ^ {J} (u) D _ {J} D ^ {I} (u) = \frac {1}{g ^ {2} (n - 1) ! ^ {2}} \varepsilon^ {a \vec {a}} \varepsilon^ {q \vec {q}} g _ {\vec {a} \vec {q}} \varepsilon^ {p \vec {p}} \varepsilon^ {c \vec {c}} g _ {\vec {p} \vec {c}} (\partial_ {a p} ^ {2} u) (\partial_ {c q} ^ {2} u) \\ = g ^ {a q} g ^ {p c} (\partial_ {a p} ^ {2} u) (\partial_ {c q} ^ {2} u) = | \nabla^ {2} u | ^ {2}. \end{array}
$$

The other formulas can be proved analogously.

By definition, the curvature tenor of  $\Sigma$  arises when one commutes two covariant derivatives. In light of Theorem 3.7, one may ask if there is a similar Nambu bracket relation which gives rise to the Ricci curvature. A particular example that introduces curvature is the following

$$
(\nabla^ {a} u) \nabla_ {a} \nabla_ {b} \nabla^ {b} u = (\nabla^ {a} u) \nabla_ {b} \nabla_ {a} \nabla^ {b} u - g (\mathcal {R} (\nabla u), \nabla u).\tag{3.53}
$$

Since  $(\nabla^{a}u)\nabla_{a}\nabla_{b}\nabla^{b}u=g(\nabla u,\nabla\Delta u)$ , it follows from Proposition 3.18 that one can write it as

$$
(\nabla^ {a} u) \nabla_ {a} \nabla_ {b} \nabla^ {b} u = \mathcal {D} _ {i} (u) \mathcal {D} ^ {i} \mathcal {D} _ {j} \mathcal {D} ^ {j} (u) = D _ {I} (u) D ^ {I} D _ {J} D ^ {J} (u),\tag{3.54}
$$

and the term in  $(3.53)$  involving the Ricci curvature is written in terms of Nambu brackets through Theorem 3.7. Using the relation

$$
\Delta \big (| \nabla u | ^ {2} \big) = 2 \big (\nabla^ {a} u \big) \nabla^ {b} \nabla_ {a} \nabla_ {b} u + 2 | \nabla^ {2} u | ^ {2},\tag{3.55}
$$

and (3.52) one obtains

$$
\begin{array}{r l r} & & {\left(\nabla^ {a} u\right) \nabla^ {b} \nabla_ {a} \nabla_ {b} u = \frac {1}{2} \mathcal {D} _ {i} \mathcal {D} ^ {i} \left(\mathcal {D} _ {j} (u) \mathcal {D} ^ {j} (u)\right) - \mathcal {D} _ {i} \mathcal {D} ^ {j} (u) \mathcal {D} _ {j} \mathcal {D} ^ {i} (u)} \\ & & {= \mathcal {D} _ {i} (u) \mathcal {D} ^ {j} \mathcal {D} _ {j} \mathcal {D} ^ {i} (u) + [ [ \mathcal {D} _ {i}, \mathcal {D} ^ {j} ] ] (u) \mathcal {D} _ {i} \mathcal {D} ^ {j} (u),} \end{array}
$$

where  $[D^{i}, D^{j}]$  denotes the commutator with respect to composition of operators. Thus, we arrive at the following result:

Proposition 3.19. Let $\mathcal{R}$ be the Ricci curvature of $\Sigma$ and let $u\in C^{\infty}(\Sigma)$. Then it holds that

$$
\begin{array}{r l} & {\mathcal {D} _ {i} (u) \mathcal {D} ^ {i} \mathcal {D} _ {j} \mathcal {D} ^ {j} (u) = \mathcal {D} _ {i} (u) \mathcal {D} ^ {j} \mathcal {D} _ {j} \mathcal {D} ^ {i} (u) + [ [ \mathcal {D} _ {i}, \mathcal {D} ^ {j} ] ] (u) \mathcal {D} _ {i} \mathcal {D} ^ {j} (u) - g (\mathcal {R} (\nabla u), \nabla u)} \\ & {D _ {I} (u) D ^ {I} D _ {J} D ^ {J} (u) = D _ {I} (u) D ^ {J} D _ {J} D ^ {I} (u) + [ [ D _ {I}, D ^ {J} ] ] (u) D _ {I} D ^ {J} (u) - g (\mathcal {R} (\nabla u), \nabla u).} \end{array}
$$

Note that it follows from Theorem 3.7 that the term  $g(\mathcal{R}(\nabla u), \nabla u)$  can be written in terms of Nambu brackets. If the formulas in Proposition 3.19 are integrated, one arrives at expressions whose index structure closely resembles that of equation (3.53). Namely, by partial integration one obtains

$$
\int \Big (D _ {I} (u) D ^ {J} D _ {J} D ^ {I} (u) + \left[ \left[ D _ {I}, D ^ {J} \right] (u) D _ {I} D ^ {J} (u)\right) \sqrt {g} = \int D _ {I} (u) D _ {J} D ^ {I} D ^ {J} (u) \sqrt {g},
$$

which implies

$$
\int D ^ {I} (u) D _ {I} D ^ {J} D _ {J} (u) \sqrt {g} = \int \Bigl (D _ {I} (u) D _ {J} D ^ {I} D ^ {J} (u) - g (\mathcal {R} (\nabla u), \nabla u) \Bigr) \sqrt {g}.\tag{3.56}
$$

Note that since the operators  $D^{I}$  contain a factor of  $\gamma^{-1}$ , the integration is actually performed with respect to  $\rho$ , as  $\gamma^{-1}\sqrt{g} = \rho$ .

The derivations  $D^{I}$  and  $D^{i}$  have indices of the ambient space M; do they exhibit any tensorial properties? The object  $\mathcal{D}^{i}(u)$  transforms as a tensor in the ambient space M, i.e.

$$
\begin{array}{r l} & {\mathcal {D} _ {y} ^ {i} (u) = \frac {1}{\gamma^ {2} (n - 1) !} \{u, \vec {y} ^ {I} \} \bar {g} _ {I J} (y) \{y ^ {i}, \vec {y} ^ {J} \}} \\ & {\quad = \frac {1}{\gamma^ {2} (n - 1) !} \frac {\partial y ^ {i}}{\partial x ^ {k}} \{u, \vec {x} ^ {I} \} \bar {g} _ {I J} (x) \{x ^ {k}, \vec {x} ^ {J} \} = \frac {\partial y ^ {i}}{\partial x ^ {k}} \mathcal {D} _ {x} ^ {k} (u),} \end{array}
$$

but this does not hold for the next order derivative  $\mathcal{D}^{i}\mathcal{D}^{j}(u)$  due to the second derivatives on the embedding functions. One can however “covariantize” this object by adding extra terms.

Proposition 3.20. Define $\nabla^{ij}$ acting on $u\in C^{\infty}(\Sigma)$ as

$$
\nabla^ {i j} (u) = \frac {1}{2} \Big (\mathcal {D} ^ {i} \mathcal {D} ^ {j} (u) + \mathcal {D} ^ {j} \mathcal {D} ^ {i} (u) - \mathcal {D} ^ {u} \big (\mathcal {D} ^ {i} (x ^ {j}) \big) \Big),\tag{3.57}
$$

where $\mathcal{D}^u (f) = \frac{1}{\gamma^2(n - 1)!}\{f,\vec{x}^I\} \bar{g}_{IJ}\{u,\vec{x}^J\}$. Then $\nabla^{ij}(u)$ transforms as a tensor in $M$, i.e.

$$
\nabla_ {y} ^ {i j} (u) = \frac {\partial y ^ {i}}{\partial x ^ {k}} \frac {\partial y ^ {j}}{\partial x ^ {l}} \nabla_ {x} ^ {k l} (u),
$$

and for all $X, Y \in T\Sigma$ it holds that

$$
\nabla_ {i j} (u) X ^ {i} Y ^ {j} = \left(\nabla_ {a} \nabla_ {b} u\right) X ^ {a} Y ^ {b}.
$$

In particular, this implies that $\bar{g}_{ij}\nabla^{ij}(u) = \Delta (u)$ and $\bar{g}_{ij}\bar{g}_{kl}\nabla^{ik}(u)\nabla^{jl}(u) = |\nabla^2 u|^2$.

3.4. Embedded surfaces. Let us now turn to the special case when  $\Sigma$  is a surface. For surfaces, the tensors P,  $S_{A}$  and  $T_{A}$  are themselves maps from TM to TM, and  $S_{A}$  coincides with  $T_{A}$ . Moreover, since the second fundamental forms can be considered as  $2 \times 2$  matrices, one has the identity

$$
2 \det W _ {A} = \left(\operatorname{tr} W _ {A}\right) ^ {2} - \operatorname{tr} W _ {A} ^ {2},
$$

which implies that the scalar curvature can be written as

$$
R = \frac {1}{\gamma^ {4}} \big (\mathcal {P} ^ {2} \big) ^ {i k} \big (\mathcal {P} ^ {2} \big) ^ {j l} \bar {R} _ {i j k l} + 2 \sum_ {A = 1} ^ {p} \det W _ {A}.
$$

Thus, defining the Gaussian curvature K to be one half of the above expression (which also coincides with the sectional curvature), one obtains

$$
K = \frac {1}{2 \gamma^ {4}} \big (\mathcal {P} ^ {2} \big) ^ {i k} \big (\mathcal {P} ^ {2} \big) ^ {j l} \bar {R} _ {i j k l} - \frac {1}{2 \gamma^ {2}} \sum_ {A = 1} ^ {p} \mathrm{Tr} \mathcal {S} _ {A} ^ {2},\tag{3.58}
$$

which in the case when  $M = R^{m}$  becomes

$$
K = - \frac {1}{2 \gamma^ {2}} \sum_ {A = 1} ^ {p} \sum_ {i, j = 1} ^ {m} \{x ^ {i}, n _ {A} ^ {j} \} \{x ^ {j}, n _ {A} ^ {i} \},\tag{3.59}
$$

and by using the normal vectors  $Z_{\alpha}$  the expression for K can be written as

$$
\begin{array}{l} K = - \frac {1}{8 \gamma^ {4} (p - 1) !} \sum \varepsilon_ {j k l I} \varepsilon_ {i m n I} \{x ^ {i}, \{x ^ {k}, x ^ {l} \} \} \{x ^ {j}, \{x ^ {m}, x ^ {n} \} \} \\ = \frac {1}{\gamma^ {4}} \bigg (\frac {1}{2} \{\{x ^ {j}, x ^ {k} \}, x ^ {k} \} \{\{x ^ {j}, x ^ {l} \}, x ^ {l} \} - \frac {1}{4} \{\{x ^ {j}, x ^ {k} \}, x ^ {l} \} \{\{x ^ {j}, x ^ {k} \}, x ^ {l} \} \bigg). \end{array}\tag{3.60}
$$

To every Riemannian metric on $\Sigma$ one can associate an almost complex structure $\mathcal{J}$ through the formula

$$
\mathcal {J} (X) = \frac {1}{\sqrt {g}} \varepsilon^ {a c} g _ {c b} X ^ {b} e _ {a},
$$

and since on a two dimensional manifold any almost complex structure is integrable, $\mathcal{J}$ is a complex structure on $\Sigma$. For $X \in TM$ one has

$$
\mathcal {P} (X) = - \frac {1}{\gamma \sqrt {g}} \bar {g} (X, e _ {a}) \varepsilon^ {a b} e _ {b},\tag{3.61}
$$

and it follows that one can express the complex structure in terms of $\mathcal{P}$.

Theorem 3.21. Defining $\mathcal{J}_M(X) = \gamma \mathcal{P}(X)$ for all $X \in TM$ it holds that $\mathcal{J}_M(Y) = \mathcal{J}(Y)$ for all $Y \in T\Sigma$. That is, $\gamma \mathcal{P}$ defines a complex structure on $T\Sigma$.

Let us now turn to the Codazzi-Mainardi equations for surfaces. In this case, the map  $C_{A}$  becomes a tangent vector and one can easily see in Proposition 3.15 that the sum in the expression for  $C_{A}$  can be written in a slightly more compact form, namely

$$
\begin{array}{r l} & {\mathcal {C} _ {A} = \left\{\gamma^ {- 2} (\mathcal {B} _ {A}) _ {k} ^ {i}, x ^ {k} \right\} \partial_ {i} + \frac {1}{\gamma^ {2}} \left\{x ^ {j}, x ^ {l} \right\} \left[ \bar {\Gamma} _ {j k} ^ {i} (\mathcal {B} _ {A}) _ {l} ^ {k} - (\mathcal {B} _ {A}) _ {k} ^ {i} \bar {\Gamma} _ {j l} ^ {k} \right]} \\ & {\qquad + \frac {1}{\gamma^ {2}} \sum_ {B = 1} ^ {p} \mathcal {B} _ {B} \mathcal {S} _ {A} (N _ {B}).} \end{array}
$$

Thus, for surfaces embedded in  $R^{m}$  the Codazzi-Mainardi equations become

$$
\sum_ {j, k = 1} ^ {m} \left\{\gamma^ {- 2} \{x ^ {i}, x ^ {j} \} \{x ^ {j}, n _ {A} ^ {k} \}, x ^ {k} \right\} \partial_ {i} + \frac {1}{\gamma^ {2}} \sum_ {B = 1} ^ {p} \mathcal {B} _ {B} \mathcal {S} _ {A} (N _ {B}) = 0,
$$

and in $\mathbb{R}^3$ one has

$$
\sum_ {j, k = 1} ^ {3} \left\{\gamma^ {- 2} \{x ^ {i}, x ^ {j} \} \{x ^ {j}, n ^ {k} \}, x ^ {k} \right\} = 0.\tag{3.62}
$$

Let us note that one can rewrite these equations using the following result:

Proposition 3.22. For $M = \mathbb{R}^m$ and $i = 1, \ldots, m$ it holds that

$$
\sum_ {j, k = 1} ^ {m} \left\{f \left\{x ^ {i}, x ^ {j} \right\} \left\{x ^ {j}, n ^ {k} \right\}, x ^ {k} \right\} = \sum_ {j, k = 1} ^ {m} \left\{f \left\{x ^ {i}, x ^ {j} \right\} \left\{x ^ {j}, x ^ {k} \right\}, n ^ {k} \right\}\tag{3.63}
$$

for any normal vector $N = n^i\partial_i$ and any $f\in C^{\infty}(\Sigma)$.

Proof. We start by recalling that for any $g \in C^{\infty}(\Sigma)$ it holds that $\sum_{i=1}^{m} \{g, x^i\} n^i = 0$, since it involves the scalar product $\bar{g}(e_a, N)$. Moreover, one also has

$$
\begin{array}{r} \sum_ {k = 1} ^ {m} \{x ^ {k}, n ^ {k} \} = \sum_ {k = 1} ^ {m} \frac {1}{\rho} \varepsilon^ {a b} (\partial_ {a} x ^ {k}) (\partial_ {b} n ^ {k}) = \sum_ {k = 1} ^ {m} \frac {1}{\rho} \varepsilon^ {a b} \Big (\partial_ {b} (n ^ {k} \partial_ {a} x ^ {k}) - n ^ {k} \partial_ {a b} ^ {2} x ^ {k} \Big) \\ = - \sum_ {k = 1} ^ {m} \frac {1}{\rho} \varepsilon^ {a b} n ^ {k} \partial_ {a b} ^ {2} x ^ {k} = 0, \end{array}
$$

which implies that $\sum_{k=1}^{m}\{x^k, gn^k\} = 0$ for all $g \in C^\infty(\Sigma)$. By using the above identities together with the Jacobi identity, one obtains

$$
\begin{array}{r l} \left\{f \{x ^ {i}, x ^ {j} \} \{x ^ {j}, n ^ {k} \}, x ^ {k} \right\} = & f \{x ^ {i}, x ^ {j} \} \left\{\{x ^ {j}, n ^ {k} \}, x ^ {k} \right\} + \{x ^ {j}, n ^ {k} \} \left\{f \{x ^ {i}, x ^ {j} \}, x ^ {k} \right\} \\ & = - f \{x ^ {i}, x ^ {j} \} \left\{\{x ^ {k}, x ^ {j} \}, n ^ {k} \right\} - n ^ {k} \left\{x ^ {j}, \{f \{x ^ {i}, x ^ {j} \}, x ^ {k} \} \right\} \\ & = - f \{x ^ {i}, x ^ {j} \} \left\{\{x ^ {k}, x ^ {j} \}, n ^ {k} \right\} + n ^ {k} \left\{f \{x ^ {i}, x ^ {j} \}, \{x ^ {k}, x ^ {j} \} \right\} \\ & = - f \{x ^ {i}, x ^ {j} \} \left\{\{x ^ {k}, x ^ {j} \}, n ^ {k} \right\} - \{x ^ {k}, x ^ {j} \} \left\{f \{x ^ {i}, x ^ {j} \}, n ^ {k} \right\} \\ & = \left\{f \{x ^ {i}, x ^ {j} \} \{x ^ {j}, x ^ {k} \}, n ^ {k} \right\}. \end{array}
$$

Hence, one can rewrite the Codazzi-Mainardi equations for a surface in $\mathbb{R}^3$ as

$$
\sum_ {j, k = 1} ^ {3} \left\{\gamma^ {- 2} (\mathcal {P} ^ {2}) ^ {i k}, n ^ {k} \right\} = 0,\tag{3.64}
$$

and it is straight-forward to show that

$$
\sum_ {i, j, k = 1} ^ {3} \left(\partial_ {c} x ^ {i}\right) \left\{\gamma^ {- 2} (\mathcal {P} ^ {2}) ^ {i k}, n ^ {k} \right\} = \frac {1}{\rho} \varepsilon^ {a b} \nabla_ {a} h _ {b c},
$$

thus reproducing the classical form of the Codazzi-Mainardi equations.

Is it possible to verify (3.64) directly using only Poisson algebraic manipulations? It turns out that the Codazzi-Mainardi equations in  $R^{3}$  is an identity for arbitrary Poisson algebras, if one assumes that a normal vector is given by  $\frac{1}{2\gamma}\varepsilon_{ijk}\{x^{j},x^{k}\}\partial_{i}$ .

Proposition 3.23. Let $\{\cdot, \cdot\}$ be an arbitrary Poisson structure on $C^{\mathcal{L}}(\Sigma)$. Given $x^{1}, x^{2}, x^{3} \in C^{\mathcal{L}}(\Sigma)$ it holds that

$$
\sum_ {j, k, l, n = 1} ^ {3} \frac {1}{2} \varepsilon_ {k l n} \left\{\gamma^ {- 2} \{x ^ {i}, x ^ {j} \} \{x ^ {j}, x ^ {k} \}, \gamma^ {- 1} \{x ^ {l}, x ^ {n} \} \right\} = 0
$$

for $i = 1,2,3$ , where

$$
\gamma^ {2} = \{x ^ {1}, x ^ {2} \} ^ {2} + \{x ^ {2}, x ^ {3} \} ^ {2} + \{x ^ {3}, x ^ {1} \} ^ {2}.
$$

Proof. Let u, v, w be a cyclic permutation of 1, 2, 3. In the following we do not sum over repeated indices u, v, w. Denoting by  $CM^{i}$  the i'th component of the

Codazzi-Mainardi equation, one has

$$
\begin{array}{l} \mathrm{CM} ^ {u} = - \left\{\gamma^ {- 2} \big (\{x ^ {u}, x ^ {v} \} ^ {2} + \{x ^ {w}, x ^ {u} \} ^ {2} \big), \gamma^ {- 1} \{x ^ {v}, x ^ {w} \} \right\} \\ \quad + \left\{\gamma^ {- 2} \{x ^ {u}, x ^ {v} \} \{x ^ {v}, x ^ {w} \}, \gamma^ {- 1} \{x ^ {u}, x ^ {v} \} \right\} + \left\{\gamma^ {- 2} \{x ^ {u}, x ^ {w} \} \{x ^ {w}, x ^ {v} \}, \gamma^ {- 1} \{x ^ {w}, x ^ {u} \} \right\} \\ \quad = - \left\{1 - \gamma^ {- 2} \{x ^ {v}, x ^ {w} \} ^ {2}, \gamma^ {- 1} \{x ^ {v}, x ^ {w} \} \right\} + \gamma^ {- 1} \{x ^ {u}, x ^ {v} \} \left\{\gamma^ {- 1} \{x ^ {v}, x ^ {w} \}, \gamma^ {- 1} \{x ^ {u}, x ^ {v} \} \right\} \\ \quad + \gamma^ {- 1} \{x ^ {u}, x ^ {w} \} \left\{\gamma^ {- 1} \{x ^ {w}, x ^ {v} \}, \gamma^ {- 1} \{x ^ {w}, x ^ {u} \} \right\} \\ \quad = \frac {1}{2} \bigl \{\gamma^ {- 1} \{x ^ {v}, x ^ {w} \}, \gamma^ {- 2} \bigl (\gamma^ {2} - \{x ^ {v}, x ^ {w} \} ^ {2} \bigr) \bigr \} = 0. \end{array}
$$

Let us end by noting that these results generalize to arbitrary hypersurfaces in $\mathbb{R}^{n + 1}$. Namely,

$$
\begin{array}{r l} & {\{\gamma^ {- 2} \big \{x ^ {i}, \vec {x} ^ {J} \big \} \{\vec {x} ^ {J}, n ^ {k} \}, x ^ {k} \big \} _ {f} = \{\gamma^ {- 2} \big \{x ^ {i}, \vec {x} ^ {J} \big \} \{\vec {x} ^ {J}, x ^ {k} \}, n ^ {k} \big \} _ {f},} \\ & {(\partial_ {c} x ^ {i}) \big \{\gamma^ {- 2} (\mathcal {P} ^ {2}) ^ {i k}, n ^ {k} \big \} _ {f} = - \frac {1}{\rho} \varepsilon^ {a b a _ {1} \dots a _ {n - 2}} (\nabla_ {a} h _ {b c}) (\partial_ {a _ {1}} f _ {1}) \cdot \cdot \cdot (\partial_ {a _ {n - 2}} f _ {n - 2}),} \end{array}
$$

and

$$
\varepsilon_ {k l L} \left\{\gamma^ {- 2} \{x ^ {i}, \vec {x} ^ {J} \} \{\vec {x} ^ {J}, x ^ {k} \}, \gamma^ {- 1} \{x ^ {l}, \vec {x} ^ {L} \} \right\} _ {f} = 0
$$

for arbitrary  $x^{1},\ldots,x^{n+1}\in C^{\infty}(\Sigma)$ .

## 4. MATRIX REGULARIZATIONS

In physics, “fuzzy spaces” have been used for a long time to regularize quantum theories and to model non-commutativity, originating in the study of a quantum theory of surfaces (membranes) sweeping out 3-manifolds of vanishing mean curvature). The main idea was to replace smooth functions on a surface by sequences of matrices, approximating the Poisson algebra of functions with increasing accuracy as the matrix dimension grows. Since the expressions for geometric quantities derived in Section 3 uses only the Poisson algebraic structure of the function algebra, it is natural to study their matrix analogues in this context.

Let us start by introducing some notation. Let  $N_{1}, N_{2}, \ldots$  be a strictly increasing sequence of positive integers and let  $T_{\alpha}$ , for  $\alpha = 1, 2, \ldots$ , be linear maps from  $C^{\infty}(\Sigma)$  to hermitian  $N_{\alpha} \times N_{\alpha}$  matrices. Moreover, let  $\hbar : R \to R$  be a strictly positive decreasing function such that  $\lim_{N \to \infty} N\hbar(N)$  converges, and set  $\hbar_{\alpha} = \hbar(N_{\alpha})$ . Introduce the operators

$$
\partial^ {f} (h) = \{f, h \}
$$

as well as the matrix operators

$$
\hat {\partial} _ {\alpha} ^ {f} (X) = \frac {1}{i \hbar_ {\alpha}} [ X, T _ {\alpha} (f) ],
$$

and write

$$
\begin{array}{l} \partial^ {f _ {1} \dots f _ {k}} (h) = \partial^ {f _ {1}} \partial^ {f _ {2}} \dots \partial^ {f _ {k}} (h) \\ \hat {\partial} _ {\alpha} ^ {f _ {1} \dots f _ {k}} (X) = \hat {\partial} _ {\alpha} ^ {f _ {1}} \hat {\partial} _ {\alpha} ^ {f _ {2}} \dots \hat {\partial} _ {\alpha} ^ {f _ {k}} (X). \end{array}
$$

Let us now define what is meant by a matrix regularization of compact surface.

Definition 4.1. Let $N_1, N_2, \ldots$ be a strictly increasing sequence of positive integers, let $\{T_\alpha\}$ for $\alpha = 1, 2, \ldots$ be linear maps from $C^\infty(\Sigma, \mathbb{R})$ to hermitian $N_\alpha \times N_\alpha$ matrices and let $\hbar(N)$ be a real-valued strictly positive decreasing function such that $\lim_{N \to \infty} N\hbar(N) < \infty$. Furthermore, let $\omega$ be a symplectic form on $\Sigma$ and let $\{\cdot, \cdot\}$ denote the Poisson bracket induced by $\omega$.

If for all integers $1 \leqslant l \leqslant k$, $\{T_{\alpha}\}$ has the following properties for all $f, f_1, \ldots, f_k, h \in C^{\infty}(\Sigma)$

(4.1)

$$
\lim _ {\alpha \to \infty} | | T _ {\alpha} (f) | | <   \infty ,\tag{4.2}
$$

$$
\lim _ {\alpha \rightarrow \infty} | | T _ {\alpha} (f h) - T _ {\alpha} (f) T _ {\alpha} (h) | | = 0,\tag{4.3}
$$

$$
\lim _ {\alpha \rightarrow \infty} \left|\left| \hat {\partial} _ {\alpha} ^ {f _ {1} \dots f _ {l}} (T _ {\alpha} (f)) - T _ {\alpha} (\partial^ {f _ {1} \dots f _ {l}} (f)) \right|\right| = 0\tag{4.4}
$$

$$
\lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} T _ {\alpha} (f) = \int_ {\Sigma} f \omega ,
$$

where $||\cdot ||$ denotes the operator norm and $\hbar_{\alpha} = \hbar (N_{\alpha})$, then we call the pair $(T_{\alpha},\hbar)$ a $C^k$-convergent matrix regularization of $(\Sigma ,\omega)$. If $(T_{\alpha},\hbar_{\alpha})$ is $C^k$-convergent for all $k\geqslant 0$ then $(T_{\alpha},\hbar_{\alpha})$ is called a smooth matrix regularization of $(\Sigma ,\omega)$.

In the following, when we speak of a matrix regularization without any reference to the degree of convergence, we shall always mean a  $C^{1}$ -convergent matrix regularization.

Remark 4.2. In some cases, a $C^1$-convergent matrix regularization is automatically a smooth matrix regularization. For instance, if it holds that for any $f, h \in C^\infty(\Sigma)$ there exists $A_k(f, h) \in C^\infty(\Sigma)$ such that

$$
\frac {1}{i \hbar_ {\alpha}} [ T _ {\alpha} (f), T _ {\alpha} (h) ] = \sum_ {k} c _ {k, \alpha} (f, h) T _ {\alpha} \big (A _ {k} (f, h) \big),
$$

for some  $c_{k,\alpha}(f,h) \in \mathbb{R}$ , then  $C^{k}$ -convergence implies  $C^{k+1}$ -convergence. The matrix regularizations for the sphere and the torus in Section 4.2 both fall into this category. Hence, they are examples of smooth matrix regularizations. Note that one can easily destroy the smoothness of a matrix regularization by slightly deforming it, see Example 4.16.

Definition 4.3. A sequence $\{\hat{f}_{\alpha}\}$ of $N_{\alpha} \times N_{\alpha}$ matrices converges to $f$ (or $C^0$-converges to $f$) if

$$
\lim _ {\alpha \to \infty} \left| \left| \hat {f} _ {\alpha} - T _ {\alpha} (f) \right| \right| = 0.\tag{4.5}
$$

Moreover, for any integer $k \geqslant 1$, a sequence $\{\hat{f}_{\alpha}\}$ of $N_{\alpha} \times N_{\alpha}$ matrices $C^k$-converges to $f$ if in addition

$$
\lim _ {\alpha \rightarrow \infty} \left|\left| \hat {\partial} _ {\alpha} ^ {f _ {1} \dots f _ {l}} (\hat {f} _ {\alpha}) - T _ {\alpha} \big (\partial^ {f _ {1} \dots f _ {l}} (f) \big) \right|\right| = 0,
$$

for all $1 \leqslant l \leqslant k$ and $f_1, \ldots, f_l \in C^\infty(\Sigma)$. If $\{\hat{f}_\alpha\}$ is $C^k$-convergent for all positive $k$ then we say that $\{\hat{f}_\alpha\}$ is a smooth sequence.

Remark 4.4. If the matrix regularization is  $C^{k}$ -convergent, it is clear that the matrix sequence  $T_{\alpha}(f)$  is  $C^{k}$ -convergent. It is however easy to construct, even in a smooth matrix regularization,  $C^{0}$ -convergent sequences that are not  $C^{1}$ -convergent; see Example 4.15.

Definition 4.5. A $C^k$-convergent matrix regularization $(T_{\alpha},\hbar)$ is called unital if the sequence $\{\mathbb{1}_{N_{\alpha}}\}$$C^k$-converges to the constant function 1.

Remark 4.6. Although unital matrix regularizations seem natural, and all our examples fall into this category, it is easy to construct examples of non-unital matrix regularizations. Namely, let  $(T_{\alpha}, \hbar)$  be a matrix regularization and consider the map  $\tilde{T}^{\alpha}$  defined by

$$
\tilde {T} ^ {\alpha} (f) = \left( \begin{array}{c c c} & & 0 \\ & T _ {\alpha} (f) & \vdots \\ 0 & \dots & 0 \end{array} \right).
$$

Then $(\tilde{T}^{\alpha},\hbar)$ is a matrix regularization which is not unital, since

$$
\lim _ {\alpha \to \infty} \left| \left| \tilde {T} ^ {\alpha} (1) - \mathbb {1} _ {N _ {\alpha} + 1} \right| \right| \geqslant 1.
$$

Proposition 4.7. Let  $(T_{\alpha}, \hbar)$  be a unital matrix regularization. Then

$$
\lim _ {\alpha \to \infty} 2 \pi N _ {\alpha} \hbar_ {\alpha} = \int_ {\Sigma} \omega .\tag{4.6}
$$

Proof. Let us use formula (4.4) with f = 1.

$$
\begin{array}{l} \int_ {\Sigma} \omega = \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} T _ {\alpha} (1) = \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} \left[ T _ {\alpha} (1) + \mathbb {1} _ {N _ {\alpha}} - \mathbb {1} _ {N _ {\alpha}} \right] \\ = \lim _ {\alpha \to \infty} \left(2 \pi \hbar_ {\alpha} N _ {\alpha} + 2 \pi \hbar_ {\alpha} \operatorname{Tr} (T _ {\alpha} (1) - \mathbb {1} _ {N _ {\alpha}})\right) = \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} N _ {\alpha} \end{array}
$$

since

$$
\lim _ {\alpha \to \infty} | 2 \pi \hbar_ {\alpha} \operatorname{Tr} (T _ {\alpha} (1) - \mathbb {1} _ {N _ {\alpha}}) | \leqslant \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} N _ {\alpha} | | T _ {\alpha} (1) - \mathbb {1} _ {N _ {\alpha}} | | = 0,
$$

due to the fact that the matrix regularization is unital.

Proposition 4.8. Let $(T_{\alpha},\hbar_{\alpha})$ be a $C^k$-convergent matrix regularization and assume that $\hat{f}_{\alpha}$ and $\hat{h}_{\alpha}C^{k}$-converge to $f,h\in C^{\infty}(\Sigma)$ respectively. Then it holds that $a\hat{f}_{\alpha} + b\hat{h}_{\alpha}C^{k}$-converges to $af + bh$, for any $a,b\in \mathbb{R}$, and $\hat{f}_{\alpha}\hat{h}_{\alpha}C^{k}$-converges to $fh$. Furthermore, it holds that

(4.7)

$$
\lim _ {\alpha \rightarrow \infty} \left|\left| \hat {f} _ {\alpha} \right|\right| = \lim _ {\alpha \rightarrow \infty} | | T _ {\alpha} (f) | |\tag{4.8}
$$

$$
\lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} \left(\hat {f} _ {\alpha} \hat {h} _ {\alpha}\right) = \int_ {\Sigma} f h \omega .
$$

Proof. The fact that  $a\hat{f} + b\hat{h} C^{k}$ -converges to  $af + bh$  follows directly from linearity of the maps  $T_{\alpha}$ . To prove (4.7) one uses the reverse triangle inequality to deduce

$$
\lim _ {\alpha \to \infty} \left| | | \hat {f} _ {\alpha} | | - | | T _ {\alpha} (f) | | \right| \leqslant \lim _ {\alpha \to \infty} \left| \left| \hat {f} _ {\alpha} - T _ {\alpha} (f) \right| \right| = 0,
$$

since  $\hat{f}_{\alpha}$  is assumed to converge to f. Let us continue by proving that  $\hat{f}_{\alpha}\hat{h}_{\alpha} C^{0}$ -converges to fh, i.e.

$$
\begin{array}{l} \lim _ {\alpha \to \infty} \left| \left| \hat {f} _ {\alpha} \hat {h} _ {\alpha} - T _ {\alpha} (f h) \right| \right| = \lim _ {\alpha \to \infty} \left| \left| \hat {f} _ {\alpha} \hat {h} _ {\alpha} - \hat {f} _ {\alpha} T _ {\alpha} (h) + \hat {f} _ {\alpha} T _ {\alpha} (h) - T _ {\alpha} (f h) \right| \right| \\ \leqslant \lim _ {\alpha \to \infty} \Big (\left| \left| \hat {f} _ {\alpha} \right| \right| \left| \left| \hat {h} _ {\alpha} - T _ {\alpha} (h) \right| \right| + \left| \left| \hat {f} _ {\alpha} T _ {\alpha} (h) - T _ {\alpha} (f) T _ {\alpha} (h) + T _ {\alpha} (f) T _ {\alpha} (h) - T _ {\alpha} (f h) \right| \right| \Big) \\ \leqslant \lim _ {\alpha \to \infty} \Big (\left| \left| \hat {f} _ {\alpha} \right| \right| \left| \left| \hat {h} _ {\alpha} - T _ {\alpha} (h) \right| \right| + \left| \left| \hat {f} _ {\alpha} - T _ {\alpha} (f) \right| \right| | | T _ {\alpha} (h) | | + | | T _ {\alpha} (f) T _ {\alpha} (h) - T _ {\alpha} (f h) | | \Big) \\ = 0, \end{array}
$$

since both  $\{\hat{f}_{\alpha}\}$  and  $\{\hat{h}_{\alpha}\}$  are  $C^{0}$ -convergent sequences and  $||\hat{f}_{\alpha}||$  is bounded by (4.7). Using the face that  $\hat{f}_{\alpha}\hat{h}_{\alpha}$$C^{0}$ -converges to fg, it is easy to prove (4.8) by computing

$$
\begin{array}{c} \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} \hat {f} _ {\alpha} \hat {h} _ {\alpha} = \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} \left(\hat {f} _ {\alpha} \hat {h} _ {\alpha} - T _ {\alpha} (f h) + T _ {\alpha} (f h)\right) \\ = \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} T _ {\alpha} (f h)) = \int_ {\Sigma} f h \omega . \end{array}
$$

Finally, we proceed by induction to show that  $\hat{f}_{\alpha}\hat{h}_{\alpha}$$C^{k}$ -converges to fh. Thus, assume that, for some  $0 \leqslant l < k$ ,  $\hat{u}_{\alpha}\hat{v}_{\alpha}$$C^{l}$ -converges to uv whenever  $\hat{u}_{\alpha}$  and  $\hat{v}_{\alpha}$$C^{l}$ -converges to u and v respectively. Since

$$
\hat {\partial} _ {\alpha} ^ {f _ {1}} (\hat {f} _ {\alpha} \hat {h} _ {\alpha}) = (\hat {\partial} _ {\alpha} ^ {f _ {1}} \hat {f} _ {\alpha}) \hat {h} _ {\alpha} + \hat {f} _ {\alpha} \hat {\partial} _ {\alpha} ^ {f _ {1}} \hat {h} _ {\alpha}
$$

we can use the induction hypothesis (together with the assumption that  $\hat{f}_{\alpha}, \hat{h}_{\alpha} C^{k>l}$ -converges) to conclude that  $\hat{\partial}_{\alpha}^{f_{1}}(\hat{f}_{\alpha}\hat{h}_{\alpha}) C^{l}$ -converges, which implies that  $\hat{f}_{\alpha}\hat{h}_{\alpha} C^{l+1}$ -converges. Hence, it follows that  $\hat{f}_{\alpha}\hat{h}_{\alpha} C^{k}$ -converges to fh. ☐

The above result allows one to easily construct sequences of matrices converging to any sum of products of functions and Poisson brackets. Namely, simply substitute for every factor in every term of the sum, a sequence converging to that function, where Poisson brackets of functions may be replaced by commutators of matrices. Proposition 4.8 then guarantees that the matrix sequence obtained in this way converges to the sum of the products of the corresponding functions, as long as the appropriate level of convergence is assumed.

Proposition 4.9. Let  $(T_{\alpha}, \hbar)$  be a matrix regularization and let  $\{\hat{f}_{\alpha}\}$  be a sequence converging to f. Then  $\lim_{\alpha \to \infty} ||\hat{f}_{\alpha}|| = 0$  if and only if f = 0.

Proof. From Proposition 4.8 it follows directly that if $\hat{f}_{\alpha}$ converges to 0 then

$$
\lim _ {\alpha \to \infty} | | \hat {f} _ {\alpha} | | = \lim _ {\alpha \to \infty} | | T _ {\alpha} (0) | | = 0.
$$

Now, assume that $\lim_{\alpha \to \infty}||\hat{f}_{\alpha}|| = 0$. Then it holds that

$$
\int f ^ {2} \omega = \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} \operatorname{Tr} \hat {f} _ {\alpha} ^ {2} \leqslant \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} N _ {\alpha} | | \hat {f} _ {\alpha} ^ {2} | | \leqslant \lim _ {\alpha \to \infty} 2 \pi \hbar_ {\alpha} N _ {\alpha} | | \hat {f} _ {\alpha} | | ^ {2} = 0,
$$

from which we conclude that $f = 0$.

Proposition 4.10. Let  $(T_{\alpha}, \hbar)$  be a matrix regularization and assume that  $\{\hat{f}_{\alpha}\} C^{k}$ -converges to f. Then  $\{\hat{f}_{\alpha}^{\dagger}\} C^{k}$ -converges to f.

Proof. Due to the fact that $||A|| = ||A^\dagger ||$ one sees that

$$
\begin{array}{l} \lim _ {\alpha \to \infty} \left| \left| \hat {\partial} _ {\alpha} ^ {f _ {1} \dots f _ {k}} (\hat {f} _ {\alpha} ^ {\dagger}) - T _ {\alpha} \big (\partial^ {f _ {1} \dots f _ {k}} (f) \big) \right| \right| = \lim _ {\alpha \to \infty} \left| \left| \hat {\partial} _ {\alpha} ^ {f _ {1} \dots f _ {k}} (\hat {f} _ {\alpha} ^ {\dagger}) ^ {\dagger} - T _ {\alpha} \big (\partial^ {f _ {1} \dots f _ {k}} (f) \big) \right| \right| \\ = \lim _ {\alpha \to \infty} \left| \left| \hat {\partial} _ {\alpha} ^ {f _ {1} \dots f _ {k}} (\hat {f} _ {\alpha}) - T _ {\alpha} \big (\partial^ {f _ {1} \dots f _ {k}} (f) \big) \right| \right| = 0, \end{array}
$$

since $\{\hat{f}_{\alpha}\} C^{k}$-converges to $f$.

Proposition 4.11. Let $(T_{\alpha},\hbar)$ be a unital matrix regularization and assume that $f$ is a nowhere vanishing function and that $\{\hat{f}_{\alpha}\} C^k$-converges to $f$. If $\hat{f}_{\alpha}^{-1}$ exists and $||\hat{f}_{\alpha}^{-1}||$ is uniformly bounded for all $\alpha$, then $\{\hat{f}_{\alpha}^{-1}\} C^k$-converges to $1 / f$.

Proof. Let us first show that $\hat{f}_{\alpha}^{-1}C^{0}$-converges to $1 / f$; one calculates

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \left| \left| \hat {f} _ {\alpha} ^ {- 1} - T _ {\alpha} (1 / f) \right| \right| \leqslant \underset {\alpha \to \infty} {\lim} \left| \left| \hat {f} _ {\alpha} ^ {- 1} \right| \right| \left| \left| \mathbb {1} _ {N _ {\alpha}} - \hat {f} _ {\alpha} T _ {\alpha} (1 / f) \right| \right|} \\ & {\quad = \underset {\alpha \to \infty} {\lim} \left| \left| \hat {f} _ {\alpha} ^ {- 1} \right| \right| \left| \left| \mathbb {1} _ {N _ {\alpha}} - \hat {f} _ {\alpha} T _ {\alpha} (1 / f) + T _ {\alpha} (1) - T _ {\alpha} (1) \right| \right|} \\ & {\quad \leqslant \underset {\alpha \to \infty} {\lim} \left| \left| \hat {f} _ {\alpha} ^ {- 1} \right| \right| \left(\left| | \mathbb {1} _ {N _ {\alpha}} - T _ {\alpha} (1) | \right| + \left| \left| \hat {f} _ {\alpha} T _ {\alpha} (1 / f) - T _ {\alpha} (1) \right| \right|\right)} \\ & {\quad = 0,} \end{array}
$$

since the matrix regularization is unital and  $\left|\left|\hat{f}_{\alpha}^{-1}\right|\right|$  is assumed to be uniformly bounded. Let us now proceed by induction and assume that  $\hat{f}_{\alpha}^{-1}$  is  $C^{l}$ -convergent  $(0 \leqslant l < k)$ . For arbitrary  $h \in C^{\infty}(\Sigma)$  it holds that

$$
[ \hat {f} _ {\alpha} ^ {- 1}, T _ {\alpha} (h) ] = - \hat {f} _ {\alpha} ^ {- 1} [ \hat {f} _ {\alpha}, T _ {\alpha} (h) ] \hat {f} _ {\alpha} ^ {- 1},
$$

and since  $\hat{f}_{\alpha}$  is  $C^{k}$ -convergent, the above sequence is  $C^{l}$ -convergent by Proposition 4.8 which implies that  $\hat{f}_{\alpha}^{-1}$  is  $C^{l+1}$ -convergent. Hence, it follows by induction that  $\hat{f}_{\alpha}^{-1}$  is  $C^{k}$ -convergent. ☐

4.1. Discrete curvature and the Gauss-Bonnet theorem. Let us now consider a surface  $\Sigma$  embedded in M via the embedding coordinates  $x^{1},\ldots,x^{m}$ , with a symplectic form

$$
\omega = \rho (u ^ {1}, u ^ {2}) d u ^ {1} \wedge d u ^ {2},
$$

inducing the Poisson bracket  $\{f,h\}=\frac{1}{\rho}\varepsilon^{ab}(\partial_{a}f)(\partial_{b}h)$ , and let  $(T_{\alpha},\hbar_{\alpha})$  be a matrix regularization of  $(\Sigma,\omega)$ . Furthermore, we let  $\{\hat{\gamma}_{\alpha}\}$  be a  $C^{2}$ -convergent sequence converging to  $\gamma=\sqrt{g}/\rho$  (and we assume that  $\{\hat{\gamma}_{\alpha}^{-1}\}$  exists and converges to  $1/\gamma$ ), and we set  $X_{\alpha}^{i}=T_{\alpha}(x^{i})$  as well as  $N_{A\alpha}^{i}=T_{\alpha}(n_{A}^{i})$  for  $i=1,\ldots,m$ . Moreover, given the metric  $\bar{g}_{ij}$  and the Christoffel symbols  $\bar{\Gamma}_{jk}^{i}$  of M, we let  $\{\hat{G}_{ij,\alpha}\}$  and  $\{\hat{\Gamma}_{jk,\alpha}^{i}\}$  denote sequences converging to  $\bar{g}_{ij}$  and  $\Gamma_{jk}^{i}$  respectively. To avoid excess of notation, we shall often suppress the index  $\alpha$  whenever all matrices are considered at a fixed (but arbitrary)  $\alpha$ .

Since most formulas in Section 3 are expressed in terms of the tensors  $P_{j}^{i}$  and  $(\mathcal{S}_{A})_{j}^{i}$  (in the case of surfaces), we introduce their matrix analogues

$$
\begin{array}{r l r} & & {\hat {\mathcal {P}} _ {j} ^ {i} = \frac {1}{i \hbar} [ X ^ {i}, X ^ {j ^ {\prime}} ] \hat {G} _ {j ^ {\prime} j}} \\ & & {(\hat {\mathcal {S}} _ {A}) _ {j} ^ {i} = \frac {1}{i \hbar} [ X ^ {i}, N _ {A} ^ {j ^ {\prime}} ] \hat {G} _ {j ^ {\prime} j} + \frac {1}{i \hbar} [ X ^ {j}, X ^ {k} ] \hat {\Gamma} _ {k l} ^ {j ^ {\prime}} N _ {A} ^ {l} \hat {G} _ {j ^ {\prime} j},} \end{array}
$$

as well as their squares

$$
(\hat {\mathcal {P}} ^ {2}) _ {j} ^ {i} = (\hat {\mathcal {P}} _ {k} ^ {i}) ^ {\dagger} \hat {\mathcal {P}} _ {j} ^ {k} \quad \mathrm{and} \quad (\hat {\mathcal {S}} _ {A} ^ {2}) _ {j} ^ {i} = (\hat {\mathcal {S}} _ {A k} ^ {i}) ^ {\dagger} \hat {\mathcal {S}} _ {A j} ^ {k},
$$

and corresponding trace

$$
\hat {\mathrm{tr}} \hat {\mathcal {P}} ^ {2} = \sum_ {i = 1} ^ {m} (\hat {\mathcal {P}} ^ {2}) _ {i} ^ {i} \quad \text {and} \quad \hat {\mathrm{tr}} \hat {\mathcal {S}} _ {A} ^ {2} = \sum_ {i = 1} ^ {m} (\hat {\mathcal {S}} _ {A} ^ {2}) _ {i} ^ {i}.
$$

(The ordinary trace of a matrix X will be denoted by  $\operatorname{Tr} X$ .) From Proposition 4.8 it follows that one can easily construct matrix sequences converging to the geometric objects in Section 3, as long as the appropriate type of convergence is assumed. Let us illustrate this by investigating matrix sequences related to the curvature of  $\Sigma$  and the Gauss-Bonnet theorem.

Definition 4.12. Let $(T_{\alpha},\hbar)$ be a matrix regularization of $(\Sigma ,\omega)$, let $K$ be the Gaussian curvature of $\Sigma$ and let $\chi$ be the Euler characteristic of $\Sigma$. A Discrete Curvature of $\Sigma$ is a matrix sequence $\{\hat{K}_1,\hat{K}_2,\hat{K}_3,\ldots \}$ converging to $K$, and a Discrete Euler Characteristic of $\Sigma$ is a sequence $\{\hat{\chi}_1,\hat{\chi}_2,\hat{\chi}_3,\ldots \}$ such that $\lim_{\alpha \to \infty}\hat{\chi}_{\alpha} = \chi$.

From the classical Gauss-Bonnet theorem, it is immediate to derive a discrete analogue for matrix regularizations.

Theorem 4.13. Let  $(T_{\alpha}, \hbar)$  be a matrix regularization of  $(\Sigma, \omega)$ , and let  $\{\hat{K}_{1}, \hat{K}_{2}, \ldots\}$  be a discrete curvature of  $\Sigma$ . Then the sequence  $\hat{\chi}_{1}, \hat{\chi}_{2}, \ldots$  defined by

$$
\hat {\chi} _ {\alpha} = \hbar_ {\alpha} \mathrm{Tr} \left[ \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \right],\tag{4.9}
$$

is a discrete Euler characteristic of $\Sigma$.

Proof. To prove the statement, we compute $\lim_{\alpha \to \infty} \hat{\chi}_{\alpha}$ and show that it is equal to $\chi(\Sigma)$. Thus

$$
\lim _ {\alpha \to \infty} \hat {\chi} _ {\alpha} = \lim _ {\alpha \to \infty} \frac {1}{2 \pi} 2 \pi \hbar_ {\alpha} \operatorname{Tr} \left[ \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \right],
$$

and by using Proposition 4.8 we can write

$$
\lim _ {\alpha \to \infty} \hat {\chi} _ {\alpha} = \frac {1}{2 \pi} \int_ {\Sigma} K \frac {\sqrt {g}}{\rho} \omega = \frac {1}{2 \pi} \int_ {\Sigma} K \frac {\sqrt {g}}{\rho} \rho d u d v = \frac {1}{2 \pi} \int_ {\Sigma} K \sqrt {g} d u d v = \chi (\Sigma),
$$

where the last equality is the classical Gauss-Bonnet theorem.

Theorem 4.14. Let $(T_{\alpha},\hbar)$ be a unital matrix regularization of $(\Sigma ,\omega)$ and let $\hat{R}_{ijkl}$, for each $i,j,k,l = 1,\dots,m$, be a sequence converging to the component of the curvature tensor of $M$. Then the sequence $\hat{K}$ defined by

$$
\hat {K} = \hat {\gamma} ^ {- 4} (\hat {\mathcal {P}} ^ {2}) ^ {i k} (\hat {\mathcal {P}} ^ {2}) ^ {j l} \hat {R} _ {i j k l} - \frac {1}{2} \sum_ {A = 1} ^ {p} \big (\hat {\gamma} ^ {\dagger} \big) ^ {- 1} \big (\hat {\mathrm{tr}} \hat {\mathcal {S}} _ {A} ^ {2} \big) \hat {\gamma} ^ {- 1},
$$

is a discrete curvature of  $\Sigma$ . Thus, a discrete Euler characteristic is given by

$$
\hat {\chi} = \hbar \operatorname{Tr} \left(\hat {\gamma} ^ {- 3} (\hat {\mathcal {P}} ^ {2}) ^ {i k} (\hat {\mathcal {P}} ^ {2}) ^ {j l} \hat {R} _ {i j k l}\right) - \frac {\hbar}{2} \sum_ {A = 1} ^ {p} \operatorname{Tr} \left[ \hat {\gamma} ^ {- 1} \widehat {\mathrm{tr}} \hat {\mathcal {S}} _ {A} ^ {2} \right].\tag{4.10}
$$

Proof. By using the way of constructing matrix sequences given through Proposition 4.8, the result follows immediately from Theorem 3.7. $\square$

In the case $M = \mathbb{R}^m$ it follows from the results in Section 3.4 that when $(T_{\alpha},\hbar)$ is a $C^2$-convergent matrix regularization, then the sequence

$$
\begin{array}{r l} \hat {K} _ {\alpha} = \frac {1}{\hbar_ {\alpha} ^ {4}} \sum_ {j, k, l = 1} ^ {m} & \left(\frac {1}{2} \big (\hat {\gamma} _ {\alpha} ^ {\dagger} \big) ^ {- 2} \big [ [ X _ {\alpha} ^ {j}, X _ {\alpha} ^ {k} ], X _ {\alpha} ^ {k} \big ] \big [ [ X _ {\alpha} ^ {j}, X _ {\alpha} ^ {l} ], X _ {\alpha} ^ {l} \big ] \hat {\gamma} _ {\alpha} ^ {- 2} \right. \\ & \left. - \frac {1}{4} \big (\hat {\gamma} _ {\alpha} ^ {\dagger} \big) ^ {- 2} \big [ [ X _ {\alpha} ^ {j}, X _ {\alpha} ^ {k} ], X _ {\alpha} ^ {l} \big ] \big [ [ X _ {\alpha} ^ {j}, X _ {\alpha} ^ {k} ], X _ {\alpha} ^ {l} \big ] \hat {\gamma} _ {\alpha} ^ {- 2}\right). \end{array}\tag{4.11}
$$

converges to the Gaussian curvature of  $\Sigma$ .

## 4.2. Two simple examples.

## 4.2.1. The round fuzzy sphere. For the sphere embedded in $\mathbb{R}^3$ as

$$
\vec {x} = (x ^ {1}, x ^ {2}, x ^ {3}) = (\cos \varphi \sin \theta , \sin \varphi \sin \theta , \cos \theta)\tag{4.12}
$$

with the induced metric

$$
(g _ {a b}) = \left( \begin{array}{c c} 1 & 0 \\ 0 & \sin^ {2} \theta \end{array} \right),\tag{4.13}
$$

it is well known that one can construct a matrix regularization from representations of  $su(2)$ . Namely, let  $S_{1}, S_{2}, S_{3}$  be hermitian  $N \times N$  matrices such that  $[S^{j}, S^{k}] = i \epsilon^{jk} {}_{l} S^{l}, (S^{1})^{2} + (S^{2})^{2} + (S^{3})^{2} = (N^{2} - 1)/4$ , and define

$$
X ^ {i} = \frac {2}{\sqrt {N ^ {2} - 1}} S ^ {i}.\tag{4.14}
$$

Then there exists a map $T^{(N)}$ (which can be defined through expansion in spherical harmonics) such that $T^{(N)}(x^i) = X^i$ and $(T^{(N)},\hbar = 2 / \sqrt{N^2 - 1})$ is a unital matrix regularization of $(S^2,\sqrt{g} d\theta \wedge d\varphi)$ [GH82]. A unit normal of the sphere in $\mathbb{R}^3$ is given by $N\in T\mathbb{R}^3$ with $N = x^{i}\partial_{i}$, which gives $N^i = X^i$, and one can compute the discrete curvature as

$$
\hat {K} _ {N} = - \frac {1}{\hbar^ {2}} \sum_ {i <   j = 1} ^ {m} \mathrm{Tr} [ X ^ {i}, X ^ {j} ] ^ {2} = \mathbb {1} _ {N}\tag{4.15}
$$

which gives the discrete Euler characteristic

$$
\hat {\chi} _ {N} = \hbar \operatorname{Tr} \hat {K} _ {N} = \hbar N = \frac {2 N}{\sqrt {N ^ {2} - 1}},\tag{4.16}
$$

converging to 2 as $N\to \infty$

4.2.2. The fuzzy Clifford torus. The Clifford torus in  $S^{3}$  can be regarded as embedded in  $R^{4}$  through

$$
\vec {x} = (x ^ {1}, x ^ {2}, x ^ {3}, x ^ {4}) = \frac {1}{\sqrt {2}} (\cos \varphi_ {1}, \sin \varphi_ {1}, \cos \varphi_ {2}, \sin \varphi_ {2}),
$$

with the induced metric

$$
(g _ {a b}) = \frac {1}{2} \left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right),
$$

and two orthonormal vectors, normal to the tangent plane of the surface in  $T R^{4}$ , can be written as

$$
N _ {\pm} = x ^ {1} \partial_ {1} + x ^ {2} \partial_ {2} \pm x ^ {3} \partial_ {3} \pm x ^ {4} \partial_ {4}.
$$

To construct a matrix regularization for the Clifford torus, one considers the  $N \times N$  matrices g and h with non-zero elements

$$
\begin{array}{l l} g _ {k k} = \omega^ {k - 1} & \text {for} k = 1, \ldots , N \\ h _ {k, k + 1} = 1 & \text {for} k = 1, \ldots , N - 1 \\ h _ {N, 1} = 1, \end{array}
$$

where  $\omega = \exp(i2\theta)$  and  $\theta = \pi/N$ . These matrices satisfy the relation  $hg = \omega gh$ . The map  $T^{(N)}$  is then defined on the Fourier modes

$$
Y _ {\vec {m}} = e ^ {i \vec {m} \cdot \vec {\varphi}} = e ^ {i m _ {1} \varphi_ {1} + i m _ {2} \varphi_ {2}}
$$

as

$$
T ^ {(N)} (Y _ {\vec {m}}) = \omega^ {\frac {1}{2} m _ {1} m _ {2}} g ^ {m _ {1}} h ^ {m _ {2}},
$$

and the pair $(T^{(N)},\hbar = \sin \theta)$ is a unital matrix regularization of the Clifford torus with respect to $\sqrt{g} d\varphi_1\wedge d\varphi_2$ [FFZ89, Hop89]. Thus, using this map one finds that

$$
X ^ {1} = T (x ^ {1}) = \frac {1}{\sqrt {2}} T (\cos \varphi_ {1}) = \frac {1}{2 \sqrt {2}} (g ^ {\dagger} + g)
$$

$$
X ^ {2} = T (x ^ {2}) = \frac {1}{\sqrt {2}} T (\sin \varphi_ {1}) = \frac {i}{2 \sqrt {2}} (g ^ {\dagger} - g)
$$

$$
X ^ {3} = T (x ^ {3}) = \frac {1}{\sqrt {2}} T (\cos \varphi_ {2}) = \frac {1}{2 \sqrt {2}} (h ^ {\dagger} + h)
$$

$$
X ^ {4} = T (x ^ {4}) = \frac {1}{\sqrt {2}} T (\sin \varphi_ {2}) = \frac {i}{2 \sqrt {2}} (h ^ {\dagger} - h)
$$

which implies that $N_{\pm}^{1} = X^{1}$, $N_{\pm}^{2} = X^{2}$, $N_{\pm}^{3} = \pm X^{3}$ and $N_{\pm}^{4} = \pm X^{4}$. By a straightforward computation one obtains

$$
- \frac {1}{\hbar^ {2}} \sum_ {i, j = 1} ^ {4} [ X ^ {i}, X ^ {j} ] ^ {2} = 2 1
$$

and therefore

$$
\frac {1}{2 \hbar^ {2}} \sum_ {i, j = 1} ^ {4} [ X ^ {i}, N _ {+} ^ {j} ] [ X ^ {j}, N _ {+} ^ {i} ] = - \frac {1}{2 \hbar^ {2}} \sum_ {i, j = 1} ^ {4} [ X ^ {i}, X ^ {j} ] ^ {2} = \mathbb {1},
$$

and since $[X^1,X^2] = [X^3,X^4 ] = 0$ it follows that

$$
\frac {1}{2 \hbar^ {2}} \sum_ {i, j = 1} ^ {4} [ X ^ {i}, N _ {-} ^ {j} ] [ X ^ {j}, N _ {-} ^ {i} ] = \frac {1}{2 \hbar^ {2}} \sum_ {i, j = 1} ^ {4} [ X ^ {i}, X ^ {j} ] ^ {2} = - \mathbb {1}.
$$

This implies that the discrete curvature vanishes, i.e.

$$
\hat {K} _ {N} = \frac {1}{2 \hbar^ {2}} \sum_ {i, j = 1} ^ {4} [ X ^ {i}, N _ {+} ^ {j} ] [ X ^ {j}, N _ {+} ^ {i} ] + \frac {1}{2 \hbar^ {2}} \sum_ {i, j = 1} ^ {4} [ X ^ {i}, N _ {-} ^ {j} ] [ X ^ {j}, N _ {-} ^ {i} ] = \mathbb {1} - \mathbb {1} = 0,
$$

which immediately gives $\hat{\chi}_N = 0$.

The following two examples will show that even in the smooth matrix regularization of the torus it is easy to find sequences that are not smooth, and that the regularization can be deformed into a non-smooth matrix regularization.

Example 4.15. Let  $(T_{\alpha}, \hbar_{\alpha})$  be the matrix regularization of the Clifford torus as in Section 4.2.2. For each N, define the matrix

$$
\hat {\theta} = \mathrm{diag} (\hbar^ {s}, 0, \dots , 0),
$$

for some fixed $0 < s \leqslant 1$. Clearly, it holds that

$$
\lim _ {\alpha \to \infty} \left| \left| \hat {\theta} - T _ {\alpha} (0) \right| \right| = \lim _ {\alpha \to \infty} \left| \left| \hat {\theta} \right| \right| = 0,
$$

i.e.  $\hat{\theta}$$C^{0}$ -converges to 0. Let us show that  $\hat{\theta}$  does not  $C^{1}$ -converge to 0. If  $\hat{\theta}$$C^{1}$ -converges to 0, then it must hold that

$$
\lim _ {\alpha \rightarrow \infty} \left|\left| \frac {1}{i \hbar} [ \hat {\theta}, T _ {\alpha} (f) ] - T _ {\alpha} (\{0, f \}) \right|\right| = \lim _ {\alpha \rightarrow \infty} \left|\left| \frac {1}{i \hbar} [ \hat {\theta}, T _ {\alpha} (f) ] \right|\right| = 0
$$

for all $f \in C^{\infty}(\Sigma)$. For $H = 2\sqrt{2} T_{(N)}(x^{3}) = h + h^{\dagger}$ one computes the eigenvalues of $A = \frac{1}{i\hbar} [\hat{\theta}, H]$ to be

$$
\lambda_ {1} = i \sqrt {2} \hbar^ {s - 1} \quad \lambda_ {2} = - i \sqrt {2} \hbar^ {s - 1} \quad \lambda_ {3} = \dots = \lambda_ {N} = 0.
$$

Hence, the norm of $A$ does not tend to 0, which implies that $\hat{\theta}$ is not $C^1$-convergent.

Example 4.16. Let  $(T_{\alpha}, \hbar_{\alpha})$  be the matrix regularization of the Clifford torus as in Section 4.2.2. For each N, define the matrix

$$
\hat {\theta} = \mathrm{diag} (\hbar^ {s}, 0, \dots , 0),
$$

for some fixed  $1 < s \leqslant 2$ . Let us now deform the fuzzy torus to obtain a  $C^{1}$ -convergent matrix regularization that is not  $C^{2}$ -convergent. Defining

$$
S _ {\alpha} (f) = T _ {\alpha} (f) + \mu (f) \hat {\theta},
$$

where $\mu : C^{\infty}(\Sigma) \to \mathbb{R}$ is an arbitrary linear functional, one can readily check that $(S_{\alpha}, \hbar_{\alpha})$ is a $C^1$-convergent matrix regularization of the Clifford torus. Let us now prove that $(S_{\alpha}, \hbar_{\alpha})$ is not a $C^2$-convergent matrix regularization, and let us for definiteness choose $\mu$ to be the evaluation map at $\varphi_1 = \varphi_2 = 0$.

In a $C^2$-convergent matrix regularization it holds that

$$
\lim _ {\alpha \rightarrow \infty} \left|\left| - \frac {1}{\hbar^ {2}} \big [ [ S _ {\alpha} (u), S _ {\alpha} (v) ], S _ {\alpha} (w) \big ] - S _ {\alpha} \big (\{\{u, v \}, w \} \big) \right|\right| = 0,
$$

for all $u, v, w \in C^{\infty}(\Sigma)$. Choosing $u = 2\sqrt{2}\cos \varphi_{2}$ and $v = w = 2\sqrt{2}\sin \varphi_{2}$ gives $S_{\alpha}(u) = h^{\dagger} + h + 2\sqrt{2}\hat{\theta}$, $S_{\alpha}(v) = i(h^{\dagger} - h)$ and $\{u, v\} = 0$. Thus

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \left| \left| - \frac {1}{\hbar^ {2}} \big [ [ S _ {\alpha} (u), S _ {\alpha} (v) ], S _ {\alpha} (w) \big ] - S _ {\alpha} \big (\{\{u, v \}, w \} \big) \right| \right|} \\ & {\qquad = \underset {\alpha \to \infty} {\lim} \frac {2 \sqrt {2}}{\hbar^ {2}} \left| \left| \big [ [ \hat {\theta}, i (h ^ {\dagger} - h) ], i (h ^ {\dagger} - h) \big ] \right| \right| = \underset {\alpha \to \infty} {\lim} 2 \sqrt {2} \big (2 + \sqrt {6} \big) \hbar^ {s - 2},} \end{array}
$$

which does not converge to 0. Hence, $(S_{\alpha},\hbar_{\alpha})$ is a $C^1$-convergent, but not $C^2$-convergent, matrix regularization of the Clifford torus.

4.3. Axially symmetric surfaces in  $R^{3}$ . Recall the classical description of general axially symmetric surfaces:

$$
\begin{array}{r l} & {\vec {x} = \left(f (u) \cos v, f (u) \sin v, h (u)\right)} \\ & {\vec {n} = \frac {\pm 1}{\sqrt {h ^ {\prime} (u) ^ {2} + f ^ {\prime} (u) ^ {2}}} \left(h ^ {\prime} (u) \cos v, h ^ {\prime} (u) \sin v, - f ^ {\prime} (u)\right),} \end{array}\tag{4.17}
$$

which implies

$$
\left(g _ {a b}\right) = \left( \begin{array}{c c} f ^ {\prime 2} + h ^ {\prime 2} & 0 \\ 0 & f ^ {2} \end{array} \right) \qquad \left(h _ {a b}\right) = \frac {\pm 1}{\sqrt {h ^ {\prime 2} + f ^ {\prime 2}}} \left( \begin{array}{c c} h ^ {\prime} f ^ {\prime \prime} - h ^ {\prime \prime} f ^ {\prime} & 0 \\ 0 & - f h ^ {\prime} \end{array} \right),
$$

where  $h_{ab}$  are the components of the second fundamental form. The Euler characteristic can be computed as

$$
\chi = \frac {1}{2 \pi} \int K \sqrt {g} = - \int_ {u _ {-}} ^ {u _ {+}} \frac {h ^ {\prime} (h ^ {\prime} f ^ {\prime \prime} - h ^ {\prime \prime} f ^ {\prime})}{(f ^ {\prime 2} + h ^ {\prime 2}) ^ {3 / 2}} d u = - \frac {f ^ {\prime}}{\sqrt {f ^ {\prime 2} + h ^ {\prime 2}}} \Bigg | _ {u _ {-}} ^ {u _ {+}},\tag{4.18}
$$

which is equal to zero for tori (due to periodicity) and equal to +2 for spherical surfaces  $f'(u_{\pm}) = \mp\infty$  if u = h).

While a general procedure for constructing matrix analogues of surfaces embedded in  $R^{3}$  was obtained in  $[ABH^{+}09b, ABH^{+}09a]$  (cp. also [Arn08b]), let us restrict now to  $h(u) = u = z$ , hence describe the axially symmetric surface  $\Sigma$  as a level set, C = 0, of

$$
C (\vec {x}) = \frac {1}{2} \big (x ^ {2} + y ^ {2} - f ^ {2} (z) \big),\tag{4.19}
$$

to carry out the construction in detail, and make the resulting formulas explicit. Defining

$$
\left\{F (\vec {x}), G (\vec {x}) \right\} _ {\mathbb {R} ^ {3}} = \nabla C \cdot (\nabla F \times \nabla G),\tag{4.20}
$$

one has

$$
\{x, y \} = - f f ^ {\prime} (z), \quad \{y, z \} = x, \quad \{z, x \} = y,\tag{4.21}
$$

respectively

$$
[ X, Y ] = i \hbar f f ^ {\prime} (Z), [ Y, Z ] = i \hbar X, [ Z, X ] = i \hbar Y\tag{4.22}
$$

for the “quantized” (“non-commutative”) surface. In terms of the parametrization given in (4.17), the above Poisson bracket is equivalent to

$$
\{F (u, v), G (u, v) \} = \varepsilon^ {a b} (\partial_ {a} F) (\partial_ {b} G)\tag{4.23}
$$

where $\partial_1 = \partial_v$ and $\partial_2 = \partial_u$. By finding matrices of increasing dimension satisfying (4.22), one can construct a map $T_{\alpha}$ having the properties (4.2) and (4.3) of a matrix regularization restricted to polynomial functions in $x, y, z$ (cp. [Arn08a]).

For the round 2-sphere, $f(z) = 1 - z^2$, (4.22) gives the Lie algebra $su(2)$, and its celebrated irreducible representations satisfy

$$
X ^ {2} + Y ^ {2} + Z ^ {2} = \mathbb {1} \quad \mathrm{if} \quad \hbar = \frac {2}{\sqrt {N ^ {2} - 1}}.\tag{4.24}
$$

When $f$ is arbitrary, one can still find finite dimensional representations of (4.22) as follows: rewrite (4.22) as

(4.25)

$$
[ Z, W ] = \hbar W\tag{4.26}
$$

$$
[ W, W ^ {\dagger} ] = - 2 \hbar f f ^ {\prime} (Z)
$$

implying that  $z_{i}-z_{j}=\hbar$  whenever  $W_{ij}\neq0$  and Z diagonal. Assuming  $W=X+iY$  with non-zero matrix elements  $W_{k,k+1}=w_{k}$  for  $k=1,\ldots,N-1$ , one thus obtains (with  $w_{0}=w_{N}=0$ )

$$
\begin{array}{r l} & Z _ {k k} = \frac {\hbar}{2} (N + 1 - 2 k) \\ & w _ {k} ^ {2} - w _ {k - 1} ^ {2} = - 2 \hbar f f ^ {\prime} (\hbar (N + 1 - 2 k) / 2) \equiv Q _ {k}, \end{array}
$$

which implies that

$$
w _ {k} ^ {2} = \sum_ {l = 1} ^ {k} Q _ {l}
$$

and the only non-trivial problem is to find the analogue of (4.24). To this end, define

$$
\hat {f} ^ {2} = X ^ {2} + Y ^ {2} = \frac {1}{2} \big (W W ^ {\dagger} + W ^ {\dagger} W \big),\tag{4.27}
$$

with W given as above. As Z has pairwise different eigenvalues, the diagonal matrix given in (4.27) can be thought of as a function of Z; hence as  $\hat{f}^{2}(Z)$ . It then trivially holds that

$$
\hat {C} = X ^ {2} + Y ^ {2} - \hat {f} ^ {2} (Z) = 0,\tag{4.28}
$$

for the representation defined above. The quantization of  $\hbar$  comes through the requirement that  $\hat{f}^{2}$  should correspond to  $f^{2}$ . While for the round 2-sphere  $\hat{f}^{2}$  equals  $f^{2}$ , provided  $\hbar$  is chosen as in (4.24), it is easy to see that in general they can not coincide, as

$$
\begin{array}{r l} & {\left[ X ^ {2} + Y ^ {2} - f (Z) ^ {2}, W \right] = \left[ (W W ^ {\dagger} + W ^ {\dagger} W) / 2 - f (Z) ^ {2}, W \right]} \\ & {\qquad = \frac {1}{2} W [ W ^ {\dagger}, W ] + \frac {1}{2} [ W ^ {\dagger}, W ] W - f (Z) [ f (Z), W ] - [ f (Z), W ] f (Z)} \\ & {\qquad = \dots = f (Z) \big (\hbar f ^ {\prime} (Z) W - [ f (Z), W ] \big) + \big (\hbar f ^ {\prime} (Z) W - [ f (Z), W ] \big) f (Z)} \end{array}
$$

with off-diagonal elements

$$
\left(f (z _ {k}) + f (z _ {k - 1})\right) \left(\hbar f ^ {\prime} (z _ {k}) - \left(f (z _ {k}) - f (z _ {k - 1})\right)\right)
$$

that are in general non-zero (hence  $X^{2} + Y^{2} + f^{2}(Z)$  is usually not even a Casimir, except in leading order).

How it does work is perhaps best illustrated by a non-trivial example, $f(z) = 1 - z^4$:

$$
\begin{array}{r} w _ {k} ^ {2} = \frac {\hbar^ {4}}{2} \Big ((N + 1) ^ {3} k - 3 (N + 1) ^ {2} k (k + 1) + \\ 2 (N + 1) k (k + 1) (2 k + 1) - 2 k ^ {2} (k + 1) ^ {2} \Big) \end{array}\tag{4.29}
$$

$$
\begin{array}{c} \hat {f} _ {k} ^ {2} = \frac {1}{2} (w _ {k} ^ {2} + w _ {k - 1} ^ {2}) = \frac {\hbar^ {4}}{4} \Big ((N + 1) ^ {3} (2 k - 1) - 6 (N + 1) ^ {2} k ^ {2} \\ \qquad \qquad \qquad + 4 (N + 1) k (2 k ^ {2} + 1) - 4 k ^ {2} (k ^ {2} + 1) \Big) \end{array}
$$

(note that $w_0^2 = w_N^2 = 0$ is explicit in (4.29)) so that

$$
\left(X ^ {2} + Y ^ {2} + Z ^ {4}\right) _ {k k} = \hbar^ {4} \bigg [ \frac {(N + 1) ^ {4}}{1 6} - \frac {(N + 1) ^ {3}}{4} + k (N + 1) - k ^ {2} \bigg ].\tag{4.30}
$$

Expressing the last two terms via  $Z^{2}$  (note that the cancellation of  $k^{3}$  and  $k^{4}$  terms shows the absence of  $Z^{3}$  and higher corrections) one finds

$$
\begin{array}{r} X ^ {2} + Y ^ {2} + Z ^ {4} + \hbar^ {2} Z ^ {2} = \hbar^ {4} \frac {(N + 1) ^ {2}}{1 6} \Big ((N + 1) ^ {2} - 4 (N + 1) + 4 \Big) \mathbb {1} \\ = \hbar^ {4} \frac {(N ^ {2} - 1) ^ {2}}{1 6} \mathbb {1}, \end{array}
$$

which equals 1 if $\hbar$ is chosen as $2 / \sqrt{N^2 - 1}$. Note that this is the same expression for $\hbar$ then for the round sphere, $f^2 = 1 - z^2$ (cp. (4.24)).

A more elegant way to derive the quantum Casimir (cp. also [Roc91, GPS09])

$$
Q = X ^ {2} + Y ^ {2} + Z ^ {4} + \hbar^ {2} Z ^ {2}\tag{4.31}
$$

is to calculate

$$
\begin{array}{r} \left[ X ^ {2} + Y ^ {2} + Z ^ {4}, W \right] = \left[ (W W ^ {\dagger} + W ^ {\dagger} W) / 2 + Z ^ {4}, W \right] \\ = \dots = \hbar^ {2} [ W, Z ^ {2} ], \end{array}
$$

which determines the terms proportional to  $\hbar$  in the Casimir.

Due to the general formula

$$
\hat {K} = - \frac {1}{8 \hbar^ {4}} \varepsilon_ {j k l} \varepsilon_ {i p q} (\hat {\gamma} ^ {\dagger}) ^ {- 2} \big [ X ^ {i}, [ X ^ {k}, X ^ {l} ] \big ] \big [ X ^ {j}, [ X ^ {p}, X ^ {q} ] \big ] \hat {\gamma} ^ {- 2}\tag{4.32}
$$

one obtains, for the axially symmetric surfaces discussed above,

$$
\hat {K} = \hat {\gamma} ^ {- 2} \left((f f ^ {\prime}) ^ {2} (Z) + \frac {1}{2 \hbar} [ W, f f ^ {\prime} (Z) ] W ^ {\dagger} + \frac {1}{2 \hbar} W ^ {\dagger} [ W, f f ^ {\prime} (Z) ]\right) \hat {\gamma} ^ {- 2}\tag{4.33}
$$

with

$$
\hat {\gamma} ^ {2} = \frac {1}{2} \big (W W ^ {\dagger} + W ^ {\dagger} W \big) + (f f ^ {\prime}) ^ {2} (Z) = f (Z) ^ {2} \big (f ^ {\prime} (Z) ^ {2} + \mathbb {1} \big) + O (\hbar),\tag{4.34}
$$

giving

$$
\hat {K} = - \left(f ^ {\prime} (Z) ^ {2} + \mathbb {1}\right) ^ {- 2} f (Z) ^ {- 1} f ^ {\prime \prime} (Z) + O (\hbar)\tag{4.35}
$$

and for $f(z)^{2} = 1 - z^{4}$ one has

(4.36)

$$
\hat {K} = \big (4 Z ^ {6} + \mathbb {1} - Z ^ {4} \big) ^ {- 2} \big (6 Z ^ {2} - 2 Z ^ {6} \big) + O (\hbar)\tag{4.37}
$$

$$
\hat {\gamma} ^ {2} = \mathbb {1} - Z ^ {4} + 4 Z ^ {6} + O (\hbar).
$$

Note that (cp. (4.25)) $z_{j} - z_{j - 1} = \hbar$ for arbitrary $f$, and that (due to the axial symmetry) $\hat{K}$ and $\hat{\gamma}^2$ are diagonal matrices, so that

$$
\hat {\chi} = \hbar \operatorname{Tr} \left(\sqrt {\hat {\gamma} ^ {2}} \hat {K}\right),
$$

in this case simply being a Riemann sum approximation of $\int K\sqrt{g}$, indeed converges to 2, the Euler characteristic of spherical surfaces.

4.4. A bound on the eigenvalues of the matrix Laplacian. As we have shown, many of the objects in differential geometry can be expressed in terms of Nambu brackets. Let us now illustrate, in the case of surfaces, that some of the techniques used to prove classical theorems can be implemented for matrix regularizations. In particular, let us prove that a lower bound on the discrete Gaussian curvature induces a lower bound for the eigenvalues of the discrete Laplacian. For simplicity, we shall consider the case when  $M = R^{m}$  and, in the following, all repeated indices are assumed to be summed over the range  $1, \ldots, m$ .

Let us start by introducing the matrix analogue of the operator  $D^{i}$ :

$$
\hat {D} _ {\alpha} ^ {i} (X) = \frac {1}{i \hbar_ {\alpha}} \hat {\gamma} _ {\alpha} ^ {- 1} [ X, X _ {\alpha} ^ {i} ].
$$

These operators obey a rule of “partial integration”, namely

$$
\mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (X) Y\right) = - \mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (Y) X\right),\tag{4.38}
$$

which is in analogy with the fact that

$$
\int_ {\Sigma} \big (\gamma D ^ {i} (f) h \big) \omega = - \int_ {\Sigma} \big (\gamma D ^ {i} (h) f \big) \omega .
$$

In view of Proposition 3.18, it is natural to make the following definition:

Definition 4.17. Let  $(T_{\alpha}, \hbar_{\alpha})$  be a matrix regularization of  $(\Sigma, \omega)$ . The Discrete Laplacian on  $\Sigma$  is a sequence  $\{\hat{\Delta}_{\alpha}\}$  of linear maps defined as

$$
\hat {\Delta} _ {\alpha} (X) = \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (X) = - \frac {1}{\hbar_ {\alpha} ^ {2}} \hat {\gamma} _ {\alpha} ^ {- 1} \big [ \hat {\gamma} _ {\alpha} ^ {- 1} [ X, X _ {\alpha} ^ {j} ], X _ {\alpha} ^ {j} \big ],
$$

where $X$ is a $N_{\alpha} \times N_{\alpha}$ matrix. An eigenmatrix sequence of $\hat{\Delta}_{\alpha}$ is a convergent sequence $\{\hat{u}_{\alpha}\}$ such that $\hat{\Delta}_{\alpha}(\hat{u}_{\alpha}) = \lambda_{\alpha}\hat{u}_{\alpha}$ for all $\alpha$ and $\lim_{\alpha \to \infty} \lambda_{\alpha} = \lambda$.

Proposition 4.18. A $C^2$-convergent eigenmatrix sequence of $\hat{\Delta}_{\alpha}$ converges to an eigenfunction of $\Delta$ with eigenvalue $\lambda = \lim_{\alpha \to \mathcal{O}} \lambda_{\alpha}$.

Proof. Given the assumption that  $\hat{u}_{\alpha}$  is a  $C^{2}$ -convergent matrix sequence converging to u, we want to prove that  $\Delta u - \lambda u = 0$ . By Proposition 4.10 this is equivalent to proving that  $\lim_{\alpha \to \infty} ||T_{\alpha}(\Delta u - \lambda u)|| = 0$ . One obtains

$$
\begin{array}{l} \lim _ {\alpha \to \infty} | | T _ {\alpha} (\Delta u - \lambda u) | | = \lim _ {\alpha \to \infty} \left| \left| T _ {\alpha} (\Delta u) - \hat {\Delta} _ {\alpha} \hat {u} _ {\alpha} + \hat {\Delta} _ {\alpha} \hat {u} _ {\alpha} - \lambda T _ {\alpha} (u) + \lambda \hat {u} _ {\alpha} - \lambda \hat {u} _ {\alpha} \right| \right| \\ \leqslant \lim _ {\alpha \to \infty} \left(\left| \left| T _ {\alpha} (\Delta u) - \hat {\Delta} _ {\alpha} \hat {u} _ {\alpha} \right| \right| + | \lambda | | | - T _ {\alpha} (u) + \hat {u} _ {\alpha} | | + \left| \left| \hat {\Delta} _ {\alpha} \hat {u} _ {\alpha} - \lambda \hat {u} _ {\alpha} \right| \right|\right) \\ = \lim _ {\alpha \to \infty} \left| \left| \hat {\Delta} _ {\alpha} \hat {u} _ {\alpha} - \lambda \hat {u} _ {\alpha} \right| \right| \leqslant \lim _ {\alpha \to \infty} \left(\left| \left| \hat {\Delta} _ {\alpha} \hat {u} _ {\alpha} - \lambda_ {\alpha} \hat {u} _ {\alpha} \right| \right| + | \lambda - \lambda_ {\alpha} | | | \hat {u} _ {\alpha} | |\right) = 0, \end{array}
$$

since $\hat{\Delta}_{\alpha}\hat{u}_{\alpha} - \lambda_{\alpha}\hat{u}_{\alpha} = 0$ and $\lambda_{\alpha}$ converges to $\lambda$.

The way curvature is introduced in the classical proof of the bound on the eigenvalues, is through the commutation of covariant derivatives. Let us state the corresponding result for matrix regularizations.

Proposition 4.19. Let $(T_{\alpha},\hbar_{\alpha})$ be a $C^2$-convergent matrix regularization of $(\Sigma ,\omega)$. If $\{\hat{u}_{\alpha}\}$ is a $C^3$-convergent matrix sequence then

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \Big | \Big | \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) - \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})} \\ & {\qquad - [ [ \hat {D} _ {\alpha} ^ {i}, \hat {D} _ {\alpha} ^ {j} ] ] (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) + \hat {K} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \Big | \Big | = 0,} \end{array}
$$

where  $[\cdot,\cdot]$  denotes the commutator with respect to composition of maps.

Proof. The result follows immediately from Proposition 3.19 and Proposition 4.8. Note that in the case of surfaces it holds that  $R_{ab} = Kg_{ab}$ , where K is the Gaussian curvature of  $\Sigma$ . ☐

A useful corollary is the following:

Proposition 4.20. Let $(T_{\alpha},\hbar_{\alpha})$ be a $C^2$-convergent matrix regularization of $(\Sigma ,\omega)$. If $\{\hat{u}_{\alpha}\}$ is a $C^2$-convergent matrix sequence then

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) =} \\ & {\quad \underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) - \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right)} \end{array}
$$

Proof. It follows from Proposition 4.19 that for a $C^3$-convergent sequence $\hat{u}_{\alpha}$ it holds that

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) - \hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \right.} \\ & {\qquad \left. - \hat {\gamma} _ {\alpha} [ [ \hat {D} _ {\alpha} ^ {i}, \hat {D} _ {\alpha} ^ {j} ] ] (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) + \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) = 0.} \end{array}
$$

Due to the appearance of a trace, the above holds even for  $C^{2}$ -convergent sequences, since e.g.

$$
\hbar_ {\alpha} \operatorname{Tr} \hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) = - \hbar_ {\alpha} \operatorname{Tr} \hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}),
$$

and the latter expression only requires  $C^{2}$ -convergence. Thus, one obtains

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) = \underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \right.} \\ & {\quad + \left. \hat {\gamma} _ {\alpha} [ [ \hat {D} _ {\alpha} ^ {i}, \hat {D} _ {\alpha} ^ {j} ] ] (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) - \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right)} \\ & {\quad = \underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) - \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right),} \end{array}
$$

by using equation (4.38).

Proposition 4.21. Let $(T_{\alpha},\hbar_{\alpha})$ be a matrix regularization of $(\Sigma ,\omega)$. If $\{\hat{u}_{\alpha}\}$ is a $C^2$-convergent matrix sequence then

$$
\lim _ {\alpha \to \infty} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) \geqslant \frac {1}{2} \lim _ {\alpha \to \infty} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\Delta} _ {\alpha} (\hat {u} _ {\alpha})\right) ^ {2}.
$$

Proof. By using the fact that $|\nabla^2 u|^2 \geqslant \frac{1}{2} (\Delta u)^2$ (for 2-dimensional manifolds) one obtains

$$
\begin{array}{l} \lim _ {\alpha \to \infty} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) = \frac {1}{2 \pi} \int_ {\Sigma} | \nabla^ {2} u | ^ {2} \omega \geqslant \frac {1}{4 \pi} \int_ {\Sigma} (\Delta u) ^ {2} \omega \\ = \lim _ {\alpha \to \infty} \frac {1}{2} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\Delta} _ {\alpha} (\hat {u} _ {\alpha})\right) ^ {2}, \end{array}
$$

since  $\hat{u}_{\alpha}$  is assumed to  $C^{2}$ -converge to u.

Theorem 4.22. Let $(T_{\alpha},\hbar_{\alpha})$ be a $C^2$-convergent matrix regularization of $(\Sigma ,\omega)$ and let $\{\hat{u}_{\alpha}\}$ be a $C^2$-convergent eigenmatrix sequence of $\hat{\Delta}_{\alpha}$ with eigenvalues $\{-\lambda_{\alpha}\}$. If $\hat{K}_{\alpha}\geqslant \kappa \mathbb{1}_{N_{\alpha}}$ for some $\kappa \in \mathbb{R}$ and all $\alpha >\alpha_0$, then $\lim_{\alpha \to \infty}\lambda_{\alpha}\geqslant 2\kappa$.

Proof. Let $\{\hat{u}_{\alpha}\}$ be a hermitian eigenmatrix sequence of $\hat{\Delta}_{\alpha}$ with eigenvalues $\{-\lambda_{\alpha}\}$. First, one rewrites

$$
\begin{array}{r l} \mathrm{Tr} \hat {\gamma} _ {\alpha} \hat {\Delta} _ {\alpha} (\hat {u} _ {\alpha}) ^ {2} = & \mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha})\right) \\ = & - \lambda_ {\alpha} \mathrm{Tr} \left(\hat {u} _ {\alpha} \hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) = \lambda_ {\alpha} \mathrm{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right). \end{array}\tag{4.39}
$$

Then, one makes use of Proposition 4.20 to write

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \hat {\gamma} _ {\alpha} \hat {\Delta} _ {\alpha} (\hat {u} _ {\alpha}) ^ {2} = - \underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right)} \\ & {\quad = \underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \left(- \hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) + \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right)} \\ & {\quad = \underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {j} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} \hat {D} _ {\alpha} ^ {j} (\hat {u} _ {\alpha}) + \hat {\gamma} _ {\alpha} \hat {K} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right).} \end{array}
$$

Using the assumption that $\hat{K}_{\alpha} \geqslant \kappa \mathbb{1}$ together with Proposition 4.21 one obtains

$$
\begin{array}{r l} & {\underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \hat {\gamma} _ {\alpha} \hat {\Delta} _ {\alpha} (\hat {u} _ {\alpha}) ^ {2} \geqslant \underset {\alpha \to \infty} {\lim} \hbar_ {\alpha} \operatorname{Tr} \left(\frac {1}{2} \hat {\gamma} _ {\alpha} \hat {\Delta} _ {\alpha} (\hat {u} _ {\alpha}) ^ {2} + \kappa \hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right)} \\ & {\quad = \underset {\alpha \to \infty} {\lim} \left(\frac {1}{2} \lambda_ {\alpha} + \kappa\right) \hbar_ {\alpha} \operatorname{Tr} \big (\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \big),} \end{array}
$$

where  $(4.39)$  has been used. One can now compare the above inequality with  $(4.39)$  to obtain

$$
\frac {1}{2} (\lambda - 2 \kappa) \lim _ {\alpha \to \infty} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) \geqslant 0.
$$

Since

$$
\lim _ {\alpha \to \infty} \hbar_ {\alpha} \operatorname{Tr} \left(\hat {\gamma} _ {\alpha} \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha}) \hat {D} _ {\alpha} ^ {i} (\hat {u} _ {\alpha})\right) = \frac {1}{2 \pi} \int_ {\Sigma} \gamma | \nabla u | ^ {2} \omega \geqslant 0,
$$

due to the fact that  $\gamma$  is a positive function, it follows that  $\lambda \geqslant 2\kappa$ .

Although the above proof depends on the fact that the matrix regularization is associated to a surface (and therefore, the results of differential geometry can be employed), we believe that, under suitable conditions on the matrix algebra, there exists a proof that is independent of this correspondence.

(Jens Hoppe) DEPARTMENT OF MATHEMATICS, KTH, S-10044 STOCKHOLM, SWEDEN E-mail address: hoppe@math.kth.se

(Gerhard Huisken) MAX PLANCK INSTITUTE FOR GRAVITATIONAL PHYSICS, AM MÜHLENBERG, D-14476 GOLM, GERMANY

## ACKNOWLEDGMENTS

J.A. would like to thank the Institut des Hautes Études Scientifiques for hospitality and H. Shimada for discussions on matrix regularizations, while J.H. thanks M. Bordemann for many discussions on related topics (and for switching talks at the October 2009 AEI workshop “Membranes, Minimal Surfaces and Matrix Limits”).

## REFERENCES

[ABH $^{+}$ 09a] J. Arnlind, M. Bordemann, L. Hofer, J. Hoppe, and H. Shimada. Fuzzy Riemann surfaces. JHEP, 06:047, 2009. hep-th/0602290.

[ABH $^{+}$ 09b] Joakim Arnlind, Martin Bordemann, Laurent Hofer, Jens Hoppe, and Hidehiko Shimada. Noncommutative Riemann surfaces by embeddings in  $R^{3}$ . Comm. Math. Phys., 288(2):403–429, 2009.

[Arn08a] Joakim Arnlind. Graph Techniques for Matrix Equations and Eigenvalue Dynamics. PhD thesis, Royal Institute of Technology, 2008.

[Arn08b] Joakim Arnlind. Representation theory of $C$-algebras for a higher-order class of spheres and tori. J. Math. Phys., 49(5):053502, 13, 2008.

[FFZ89] D. B. Fairlie, P. Fletcher, and C. K. Zachos. Trigonometric structure constants for new infinite-dimensional algebras. Phys. Lett. B, 218(2):203-206, 1989.

[GPS09] T. R. Govindarajan, P. Padmanabhan, and T. Shreecharan. Beyond fuzzy spheres. arXiv:0906.1660, 2009.

[GH82] Jens Hoppe. Quantum Theory of a Massless Relativistic Surface and a Two-dimensional Bound State Problem. PhD thesis, Massachusetts Institute of Technology, 1982. http://dspace.mit.edu/handle/1721.1/15717.

[Hop89] Jens Hoppe. Diffeomorphism groups, quantization, and SU(∞). Internat. J. Modern Phys. A, 4(19):5235-5248, 1989.

[KN96a] Shoshichi Kobayashi and Katsumi Nomizu. Foundations of differential geometry. Vol. I. Wiley Classics Library. John Wiley & Sons Inc., New York, 1996. Reprint of the 1963 original, A Wiley-Interscience Publication.

[KN96b] Shoshichi Kobayashi and Katsumi Nomizu. Foundations of differential geometry. Vol. II. Wiley Classics Library. John Wiley & Sons Inc., New York, 1996. Reprint of the 1969 original, A Wiley-Interscience Publication.

[Nam73] Yoichiro Nambu. Generalized Hamiltonian dynamics. Phys. Rev. D (3), 7:2405-2412, 1973.

[Roc91] M. Rocek. Representation theory of the nonlinear SU(2) algebra. Phys. Lett., B255:554-557, 1991.

(Joakim Arnlind) MAX PLANCK INSTITUTE FOR GRAVITATIONAL PHYSICS, AM MÜHLENBERG 1, D-14476 GOLM, GERMANY