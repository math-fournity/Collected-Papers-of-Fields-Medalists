# A version of Baker’s theorem on linear forms in logarithms

Adam J Harper

1st December 2010

## Abstract

We reproduce a proof of a fairly weak version of Baker’s theorem on linear forms in the logarithms of algebraic numbers. We try to motivate the argument by analogy with a proof that Euler’s number e is transcendental.

## 1 Introduction

In 1966, Baker proved a landmark result about linear forms in the logarithms of algebraic numbers, which helped to earn him the Fields Medal in 1970. The following is a somewhat weak version of that result:

Baker’s Theorem 1 (A. Baker, 1966). Let$\alpha _ { 1 } , . . . , \alpha _ { n }$be non-zero algebraic numbers for which log$\alpha _ { 1 } , . . . , \log { \alpha _ { n } } ,$2πi are linearly independent over$\mathbb { Q }$. Then

$$
\beta_ {1} \log \alpha_ {1} + \ldots + \beta_ {n} \log \alpha_ {n} \neq 0
$$

for any algebraic numbers$\beta _ { 1 } , . . . , \beta _ { n }$that are not all zero.

This is weak in that, firstly, the theorem remains true if we just suppose that log$\alpha _ { 1 } , . . . , \log { \alpha _ { n } }$are linearly independent over$\mathbb { Q } .$, with no reference to 2πi. (Baker asserted this in his original paper, and published a proof slightly later.) Moreover one can say, not just that the linear combination is non-zero, but that it is bounded away from zero in an efective way (as Baker did in his original paper). However, the theorem as stated admits a slightly more transparent proof.

Baker’s theorem is ubiquitous in (transcendental) number theory, and has been discussed in many places, but it seems to be a commonly held view that the proof is rather mysterious and unintuitive. In this note we will attempt to dispel that view. To that end, we recall the following broad outline of a proof that Euler’s number e is transcendental:

• Argue by contradiction, supposing that

$$
a _ {n} e ^ {n} + a _ {n - 1} e ^ {n - 1} + \ldots + a _ {1} e + a _ {0} = 0
$$

for some$n \in \mathbb { N }$and$a _ { i } \in \mathbb { Z } { \mathrm { ~ ( w i t h ~ } } a _ { n } \neq 0 { \mathrm { ) } }$ • Because of the properties of the exponential function, there is a large class of “nice” functions$F ( i )$that approximate$e ^ { i }$very well for$i = 0 , 1 , . . . , n$ (For example, one can choose$\begin{array} { r } { F ( i ) = \sum _ { k = 0 } ^ { m } f ^ { ( k ) } ( i ) } \end{array}$for a suitable high degree polynomial$f ,$where m is a parameter. Note that$F ( i )$satisfies$F ^ { \prime } ( i ) \approx F ( i )$ if$f$is chosen suitably.)

• For suitable choice of$F ,$we can arrange that

$$
a _ {n} F (n) + a _ {n - 1} F (n - 1) + \ldots + a _ {1} F (1) + a _ {0} \approx a _ {n} e ^ {n} + a _ {n - 1} e ^ {n - 1} + \ldots + a _ {1} e + a _ {0} = 0
$$

is a non-zero rational with fairly small denominator. But it is clearly impossible to approximate zero very well by a non-zero rational with small denominator.

Note that the slightly complicated construction of an approximating function F replaces e.g. the appeal to the series expansion of$e ^ { x }$in the proof that$e$is irrational.

At a very high level, the proof that e is transcendental may be described in the following way: if$e$were algebraic, it would satisfy a “simple” polynomial equation (i.e. one of bounded degree and bounded height of coeficients), and this contradicts the analytic properties of the function$e ^ { x }$, because rational numbers are “fairly well spaced”. We stress here that the key work in the proof is in determining functional properties of$e ^ { x }$

We will see that, at this rather high level of inspection, the proof of Baker’s Theorem is precisely analogous to the proof that$e$is transcendental. Firstly we suppose, for a contradiction, that

$$
\beta_ {1} \log \alpha_ {1} + \ldots + \beta_ {n} \log \alpha_ {n} = 0
$$

for some algebraic numbers$\beta _ { 1 } , . . . , \beta _ { n }$that are not all zero. In fact, without loss of generality (after possibly relabelling the$\alpha _ { i }$, and dividing through by a non-zero $\beta _ { i } )$we may suppose that

$$
\beta_ {1} \log \alpha_ {1} + \ldots + \beta_ {n - 1} \log \alpha_ {n - 1} - \log \alpha_ {n} = 0.
$$

We do not try to (directly) contradict this relation, which in particular is not a polynomial relation. Instead, going slightly beyond what happens in the proof that e is transcendental, we will indirectly construct a function$\phi ( z )$that vanishes, together with several of its derivatives, at many integer points$z .$. The putative expression for log$\alpha _ { n }$as a combination of log$\alpha _ { 1 } , . . . , \log { \alpha _ { n - 1 } }$is input into this construction, and implies that$\phi ( z )$vanishes rather more than might be expected.

Having done this, we analyse the functional properties of$\phi ( z )$. The so-called “extrapolation procedure” for doing this involves repeatedly playing of an analytic result, obtained by complex variable methods, against the fact (roughly— see $\ S \ S 3 - 4 )$that$\phi ( z )$takes algebraic values at integer z and therefore either vanishes at such z, or is efectively bounded away from zero there. The extrapolation method is, perhaps, the most novel ingredient of Baker’s proof, and he wrote himself that it would “...probably be capable of considerable development for it applies in principle to many other auxiliary functions...”.

Finally, the extrapolation procedure reveals that$\phi ( z )$must actually vanish at an enormous number of integer points. Because of the construction of$\phi ( z )$, this implies a linear dependence over Q between log$\alpha _ { 1 } , . . . , \log { \alpha _ { n } }$and 2πi, which is a contradiction.

We conclude this introduction by recalling that the special case of Baker’s theorem where$n = 2$was proved rather earlier, by Gelfond and by Schneider independently in 1934. The author has not been able to view Schneider’s argument, but it certainly seems fair to describe Baker’s method as being a generalisation of Gelfond’s method. In his book [3], Gelfond describes his argument as using “...the idea of analytic-arithmetic continuation.” The author believes that to be a fitting description.

## 2 Construction of the auxiliary function$\phi ( z )$

We now launch into the construction of the auxiliary function$\phi ( z )$, which we want to vanish, along with many of its derivatives, at a number of integer points. Our account from this point on is a hybrid of Baker’s original article [1], and Chapter 2 of his book [2] on this subject, with just a few changes to the exposition. We have a parameter$h \in \mathbb { R }$, which at the end of the proof will be taken to be large in a way depending on the$\alpha _ { i } ,$the$\beta _ { i } .$, and n.

Recall the hypothesis that we wish to contradict, namely that

$$
\beta_ {1} \log \alpha_ {1} + \ldots + \beta_ {n - 1} \log \alpha_ {n - 1} - \log \alpha_ {n} = 0
$$

for some algebraic numbers$\beta _ { 1 } , . . . , \beta _ { n - 1 }$. Exponentiating, this becomes

$$
\alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}} \alpha_ {n} ^ {- 1} = 1,
$$

but this is not much more helpful, because the purpose of proving the theorem is to understand how algebraic powers of algebraic numbers behave. On the other hand, we can say things about integer powers of algebraic numbers, which motivates the following choice of auxiliary function:

$$
\phi (z) := \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} z} \dots \alpha_ {n} ^ {\lambda_ {n} z}, \quad z \in \mathbb {C},
$$

where$L = [ h ^ { 2 - 1 / ( 4 n ) } ]$, and the$p ( \lambda _ { 1 } , . . . , \lambda _ { n } )$are integers not all of which are zero, with absolute values at most$e ^ { h ^ { 3 } }$, such that

$$
\frac {d ^ {m}}{d z ^ {m}} \phi (z) = 0 \forall 0 \leq m \leq h ^ {2}, z \in \{1, 2,..., h \}.
$$

In a moment we will show that we can find such integers$p ( \lambda _ { 1 } , . . . , \lambda _ { n } )$, and the reader should note that the fact that we can do so with L smaller than$h ^ { 2 }$by a power of h, which exploits our (to be contradicted) hypothesis about the$\alpha _ { i } .$, is crucial to the subsequent argument.

Actually it is not too hard to find such integers, just a little fiddly. Because of our (to be contradicted) hypothesis, we can equivalently write

$$
\phi (z) := \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1},..., \lambda_ {n}) e ^ {(\lambda_ {1} + \lambda_ {n} \beta_ {1}) z \log \alpha_ {1} +... + (\lambda_ {n - 1} + \lambda_ {n} \beta_ {n - 1}) z \log \alpha_ {n - 1}},
$$

and we will be done if we can choose the$p ( \lambda _ { 1 } , . . . , \lambda _ { n } )$such that

$$
\sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} z} \dots \alpha_ {n} ^ {\lambda_ {n} z} (\lambda_ {1} + \lambda_ {n} \beta_ {1}) ^ {m _ {1}} \dots (\lambda_ {n - 1} + \lambda_ {n} \beta_ {n - 1}) ^ {m _ {n - 1}}
$$

vanishes for all$0 \leq m _ { 1 } + . . . + m _ { n - 1 } \leq h ^ { 2 }$and all$z \in \{ 1 , 2 , . . . , h \}$. Now if d is an upper bound for the degrees of the minimal polynomials of$\alpha _ { 1 } , . . . , \alpha _ { n } , \beta _ { 1 } , . . . , \beta _ { n - 1 }$ and$a _ { 1 }$is the leading coeficient in the minimal polynomial of$\alpha _ { 1 }$, we have for example that

$$
(a _ {1} \alpha_ {1}) ^ {j} = \sum_ {s = 0} ^ {d - 1} a _ {1, s} ^ {(j)} \alpha_ {1} ^ {s} \quad \forall j \in \mathbb {N} \cup \{0 \},
$$

for certain integers$a _ { 1 , s } ^ { ( j ) }$. So multiplying through by$( a _ { 1 } . . . a _ { n } ) ^ { L z } b _ { 1 } ^ { m _ { 1 } } . . . b _ { n - 1 } ^ { m _ { n - 1 } }$, where$a _ { i }$ is the leading coeficient in the minimal polynomial of$\alpha _ { i } .$, similarly for$b _ { i }$, we see we would be done if

$$
\sum_ {s _ {1} = 0} ^ {d - 1} \dots \sum_ {s _ {n} = 0} ^ {d - 1} \sum_ {t _ {1} = 0} ^ {d - 1} \dots \sum_ {t _ {n - 1} = 0} ^ {d - 1} \alpha_ {1} ^ {s _ {1}} \dots \alpha_ {n} ^ {s _ {n}} \beta_ {1} ^ {t _ {1}} \dots \beta_ {n - 1} ^ {t _ {n - 1}} \left(\sum_ {\mu_ {1} = 0} ^ {m _ {1}} \dots \sum_ {\mu_ {n - 1} = 0} ^ {m _ {n - 1}} \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1},..., \lambda_ {n}) \cdot \right.
$$

$$
\cdot (\prod_ {i = 1} ^ {n} a _ {i} ^ {L z - \lambda_ {i} z} a _ {i, s _ {i}} ^ {(\lambda_ {i} z)}) (\prod_ {j = 1} ^ {n - 1} \binom{m _ {j}}{\mu_ {j}} (b _ {j} \lambda_ {j}) ^ {m _ {j} - \mu_ {j}} \lambda_ {n} ^ {\mu_ {j}} b _ {j, t _ {j}} ^ {(\mu_ {j})})
$$

vanished for all$0 \leq m _ { 1 } + . . . + m _ { n - 1 } \leq h ^ { 2 }$and all$z \in \{ 1 , 2 , . . . , h \}$

But this can be achieved just by choosing the$p ( \lambda _ { 1 } , . . . , \lambda _ { n } )$to solve a system of $M \leq ( h ^ { 2 } + 1 ) ^ { n - 1 } h d ^ { 2 n - 1 }$integer linear equations, namely the equations that the inner bracket should equal zero for each choice of$m _ { 1 } , . . . , m _ { n - 1 } , z , s _ { 1 } , . . . , s _ { n } , t _ { 1 } , . . . , t _ { n - 1 }$ If h is large enough, then we have$( L + 1 ) ^ { n } \geq h ^ { 2 n - 1 / 4 } \geq 2 M$variables$p ( \lambda _ { 1 } , . . . , \lambda _ { n } )$ so we can certainly find a non-trivial solution. Moreover, an easy induction shows that$| a _ { i , s } ^ { ( j ) } | , | b _ { i , t } ^ { ( j ) } | \leq C ^ { j }$, where C depends on the$\alpha _ { i }$and$\beta _ { i }$only; and therefore one has

$$
| \prod_ {i = 1} ^ {n} a _ {i} ^ {L z - \lambda_ {i} z} a _ {i, s _ {i}} ^ {(\lambda_ {i} z)} | \leq K ^ {L z} \leq K ^ {L h}, \quad | \prod_ {j = 1} ^ {n - 1} \binom {m _ {j}} {\mu_ {j}} (b _ {j} \lambda_ {j}) ^ {m _ {j} - \mu_ {j}} \lambda_ {n} ^ {\mu_ {j}} b _ {j, t _ {j}} ^ {(\mu_ {j})} | \leq (K L) ^ {h ^ {2}},
$$

for a suitable constant K depending on the$\alpha _ { i }$, the$\beta _ { i }$, and on n only. So the estimates on the size of the$p ( \lambda _ { 1 } , . . . , \lambda _ { n } )$can be obtained using the following famous (but easily proved) result:

Siegel’s Lemma 1 (C. Siegel, 1929, and others). If$N > M > 0$are integers, then the system of equations

$$
\sum_ {j = 1} ^ {N} u _ {i, j} x _ {j} = 0, \quad 1 \leq i \leq M
$$

has a non-trivial solution in integers x with absolute values at most

$$
1 + (N \max _ {i, j} | u _ {i, j} |) ^ {M / (N - M)}.
$$

## 3 Easy estimates on$\phi ( z )$

Having constructed$\phi ( z )$, we begin to analyse its properties as a function of the complex variable z. In the first place, we have

$$
\begin{array}{l} \left| \log^ {m _ {1}} \alpha_ {1}... \log^ {m _ {n - 1}} \alpha_ {n - 1} \sum_ {\lambda_ {1} = 0} ^ {L}... \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1},..., \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} z}... \alpha_ {n} ^ {\lambda_ {n} z} (\lambda_ {1} + \lambda_ {n} \beta_ {1}) ^ {m _ {1}}... (\lambda_ {n - 1} + \lambda_ {n} \beta_ {n - 1}) ^ {m _ {n - 1}} \right| \\ \qquad \leq e ^ {h ^ {3}} (K L) ^ {h ^ {2}} K ^ {L | z |}, \quad 0 \leq m _ {1} +... + m _ {n - 1} \leq h ^ {2}, \end{array}
$$

where K depends only on$\alpha _ { i } , \beta _ { i } , n$, as before. It follows that, for$0 \leq m \leq h ^ { 2 }$but for$a l l z \in \mathbb { C }$一，

$$
| \frac {d ^ {m}}{d z ^ {m}} \phi (z) | \leq K ^ {h ^ {3} + L | z |}
$$

for suitable (diferent) K depending on$\alpha _ { i } , \beta _ { i } , n$only. Note the appearance of$L$ which we arranged to be a power of h slightly smaller than$h ^ { 2 }$, in this estimate.

Our other (fairly) easy estimate will encode, in a useful way, the fact that $\textstyle { \frac { d ^ { m } } { d z ^ { m } } } \phi ( z )$takes (up to various multipliers involving the log$\alpha _ { i } )$algebraic values when z is an integer, and that algebraic numbers are fairly well spaced. Thus if$0 \le$ $m _ { 1 } + . . . + m _ { n - 1 } \leq h ^ { 2 }$, and$z \in \mathbb { N }$, then the number

$$
X := (a _ {1}... a _ {n}) ^ {L z} b _ {1} ^ {m _ {1}}... b _ {n - 1} ^ {m _ {n - 1}} \sum_ {\lambda_ {1} = 0} ^ {L}... \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1},..., \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} z}... \alpha_ {n} ^ {\lambda_ {n} z} (\lambda_ {1} + \lambda_ {n} \beta_ {1}) ^ {m _ {1}}... (\lambda_ {n - 1} + \lambda_ {n} \beta_ {n - 1}) ^ {m _ {n - 1}}
$$

is an algebraic integer with degree at most$d ^ { 2 n - 1 }$(by the Tower Law for field extensions, and since algebraic integers form a ring). Now arguing in a Liouvilleesque way, either$X = 0$or the norm of X is at least 1. But any conjugate of X has absolute value at most$K ^ { h ^ { 3 } + L z }$, arguing exactly as above, so either$X = 0$or $| X | \geq K ^ { - d ^ { 2 n - 2 } ( h ^ { 3 } + L z ) }$. This obviously implies that for$0 \leq m \leq h ^ { 2 }$, and any$z \in \mathbb { N }$, we have

$$
\frac {d ^ {m}}{d z ^ {m}} \phi (z) = \sum_ {m _ {1} + \ldots + m _ {n - 1} = m} f _ {m _ {1}, \ldots , m _ {n - 1}} (z),
$$

where we have

$$
f _ {m _ {1}, \ldots , m _ {n - 1}} (z) = 0 \quad \mathrm{or} \quad | f _ {m _ {1}, \ldots , m _ {n - 1}} (z) | \geq K ^ {- h ^ {3} - L z}
$$

for suitable (diferent) K depending on$\alpha _ { i } , \beta _ { i } , n$only.

## 4 The extrapolation argument

By construction, we know that$\phi ( z )$vanishes for$z \in \{ 1 , 2 , . . . , h \}$. In this section we will argue, using the information that we also have about the derivatives of φ, and the bounds in §3, that actually$\phi ( z )$must vanish for$z \in \{ 1 , 2 , . . . , ( L + 1 ) ^ { n } \}$ (or even for a larger set of$z { \mathrm { ~ v a l u e s } } )$. This will swiftly imply Baker’s Theorem.

We need one key lemma, which is squarely complex-analytic. Rather than presenting a version that is highly tailored to our situation, it seems more revealing to state and prove a somewhat general version.

Baker’s Lemma 1. Let$f : \mathbb { C } \to \mathbb { C }$be holomorphic, let$\epsilon > 0$, and let$A , B , C , T , U$ be large real numbers. Suppose that$C \gg T / ( A \log A ) + U B A ^ { \epsilon }$, and that

$$
1. | \frac {d ^ {m}}{d z ^ {m}} f (z) | \leq e ^ {T + U | z |} \forall 0 \leq m \leq C, z \in \mathbb {C};
$$

$$
2. \frac {d ^ {m}}{d z ^ {m}} f (z) = 0 \forall 0 \leq m \leq C, z \in \{1, 2,..., [ A ] \}.
$$

Then$\begin{array} { r } { | \frac { d ^ { m } } { d z ^ { m } } f ( z ) | \leq e ^ { - 2 ( T + U z ) } } \end{array}$for all$0 \leq m \leq C / 2$and all$z \in \{ 1 , 2 , . . . , [ A B ] \}$

We will prove this using the elegant argument from Baker’s book [2], which exploits the maximum-modulus principle. However, we caution that this makes it appear that the exact vanishing of the derivatives in condition (2) is essential, and in fact that is not the case. (Indeed, the argument in Baker’s paper [1], proving a quantitative version of his theorem, does not assume such vanishing.)

Fix any$0 \leq m \leq C / 2$, and let$\begin{array} { r } { g ( z ) = \frac { d ^ { m } } { d z ^ { m } } f ( z ) } \end{array}$, so we are aiming to show that $| g ( z ) | \leq e ^ { - 2 ( T + U z ) }$for$z \in \{ 1 , 2 , . . . , [ A B ] \}$. Because of assumption (2), we see that

$$
\frac {g (z)}{(z - 1) ^ {[ C / 2 ]} (z - 2) ^ {[ C / 2 ]} \dots (z - [ A ]) ^ {[ C / 2 ]}}
$$

is a holomorphic function. Thus, by the maximum modulus principle applied on a circle about the origin with radius$A ^ { 1 + \epsilon } B$, for$z \in \{ 1 , 2 , . . . , [ A B ] \}$we have

$$
| g (z) | \leq \max _ {| w | = A ^ {1 + \epsilon} B} \left(| g (w) | \frac {| z - 1 | ^ {[ C / 2 ]} . . . | z - [ A ] | ^ {[ C / 2 ]}}{| w - 1 | ^ {[ C / 2 ]} . . . | w - [ A ] | ^ {[ C / 2 ]}}\right) \leq e ^ {- (\epsilon / 2) \log A [ A ] [ C / 2 ]} \max _ {| w | = A ^ {1 + \epsilon} B} | g (w) |.
$$

Using the assumption (1), and that$A C \gg ( T / \log A ) + U A ^ { 1 + \epsilon } B$, the result follows.

Q.E.D.

This lemma is applied to the functions$f _ { m _ { 1 } , . . . , m _ { n - 1 } }$appearing at the end of$\ S 3$ where the hypotheses are satisfied with$T = h ^ { 3 } \log K , U = L$log$K , B = h ^ { 1 / 8 n }$, etc. (The reader should note that the various estimates we derived for φ in previous sections were actually derived separately for each function$f _ { m _ { 1 } , . . . , m _ { n - 1 } } )$. Because of the dichotomy established at the end of$\ S 3$, the conclusion of the lemma is untenable unless the derivatives of$f _ { m _ { 1 } , . . . , m _ { n - 1 } }$vanish for z on the wide range supplied. Thus, iteratively applying the lemma$O ( n ^ { 2 } )$times, the claim that

$$
\phi (z) = 0 \quad \forall z \in \{1, 2,..., (L + 1) ^ {n} \}
$$

follows.

## 5 Conclusion of the proof

Recall that we had

$$
\phi (z) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} z} \dots \alpha_ {n} ^ {\lambda_ {n} z}, \quad z \in \mathbb {C},
$$

and we now know that$\phi ( 1 ) = \phi ( 2 ) = . . . = \phi ( ( L + 1 ) ^ { n } ) = 0$. This means that the vector of numbers$p ( \lambda _ { 1 } , . . . , \lambda _ { n } )$is a non-trivial element of the kernel of a certain $( L + 1 ) ^ { n } \times ( L + 1 ) ^ { n }$matrix, which must therefore have determinant zero.

But this matrix is clearly a Vandermonde matrix, so the vanishing of its determinant implies that

$$
\alpha_ {1} ^ {\lambda_ {1}}... \alpha_ {n} ^ {\lambda_ {n}} = \alpha_ {1} ^ {\lambda_ {1} ^ {\prime}}... \alpha_ {n} ^ {\lambda_ {n} ^ {\prime}}
$$

for some distinct tuples of integers$\left( \lambda _ { 1 } , . . . , \lambda _ { n } \right)$and$\left( \lambda _ { 1 } ^ { \prime } , . . . , \lambda _ { n } ^ { \prime } \right)$. This contradicts the assumption that log$\alpha _ { 1 } , . . . , \log \alpha _ { n } .$, 2πi are linearly independent over$\mathbb { Q }$

Q.E.D.

Again, it is perhaps worth pointing out that there are other ways to end this proof that are more “robust” than relying on the appearance of a Vandermonde determinant. In contrast, the extrapolation argument set out in$\ S 4$is fundamental to Baker’s approach.

## References

[1] A. Baker. Linear forms in the logarithms of algebraic numbers. Mathematika 13, pp 204-216. 1966

[2] A. Baker. Transcendental number theory. Reissue published by Cambridge University Press. 1990

[3] A. O. Gelfond. Transcendental and Algebraic Numbers. Translated by L. Boron. Dover publ., New York. 1960