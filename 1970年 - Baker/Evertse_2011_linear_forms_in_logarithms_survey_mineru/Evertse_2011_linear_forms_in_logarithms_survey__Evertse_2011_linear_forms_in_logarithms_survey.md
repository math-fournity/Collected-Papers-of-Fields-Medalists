# LINEAR FORMS IN LOGARITHMS

# JAN-HENDRIK EVERTSE

## April 2011

## Literature:

T.N. Shorey, R. Tijdeman, Exponential Diophantine equations, Cambridge University Press, 1986; reprinted 2008.

## 1. Linear forms in logarithms and applications

We start with recalling some results from transcendence theory and then work towards lower bounds for linear forms in logarithms which are of crucial importance in efectively solving Diophantine equations.

We start with a transcendence result proved independently by the Russian Gel’fond and the German Schneider in 1934.

Theorem 1.1. (Gel’fond, Schneider, 1934) Let$\alpha , \beta$be algebraic numbers in C, with α$\neq 0 ,$, 1 and$\beta \notin \mathbb { Q }$. Then$\alpha ^ { \beta }$is transcendental.

Here,$\alpha ^ { \beta } : = e ^ { \beta \log \alpha }$, where$\textstyle e ^ { z } = \sum _ { n = 0 } ^ { \infty } z ^ { n } / n !$and log$\alpha = \log | \alpha | + i \arg ( \alpha )$. The argument of$\alpha$is determined only up to a multiple of 2π. Thus, log α and hence$\alpha ^ { \beta }$are multi-valued. The theorem holds for any choice of value of arg α.

Corollary 1.2. Let$\beta$be an algebraic number in C with$i \beta \notin \mathbb { Q }$. Then$e ^ { \pi \beta }$is transcendental.

Proof.$e ^ { \pi \beta } = e ^ { \pi i \cdot ( - i \beta ) } = ( - 1 ) ^ { - i \beta }$

Given a subring R of$\mathbb { C } \ ( \mathrm { e . g . , ~ \mathbb { Z } , ~ \mathbb { Q } }$, field of algebraic numbers), we say that complex numbers$\theta _ { 1 } , \ldots , \theta _ { m }$are called linearly independent over R if the equation$x _ { 1 } \theta _ { 1 } + \cdot \cdot \cdot + x _ { m } \theta _ { m } = 0$has no solution$( x _ { 1 } , \ldots , x _ { m } ) \in R ^ { m } \setminus \{ \mathbf { 0 } \}$

Corollary 1.3. Let$\alpha , \beta$be algebraic numbers from C diferent from 0, 1 such that log α, log$\beta$are linearly independent over$\mathbb { Q }$. Then for all non-zero algebraic numbers γ, δ from C we have γ log$\alpha + \delta \log \beta \neq 0$

Proof. Assume γ log$\alpha + \delta$log$\beta = 0$. Then log$\alpha = - ( \delta / \gamma )$log β, hence$\alpha =$ $\beta ^ { - \delta / \gamma }$. By Theorem 1.1 this is possible only if$a : = \delta / \gamma \in \mathbb { Q }$. But then, log$\alpha - a \log \beta = 0$, contrary to our assumption.✷

We now come to Baker’s generalization to linear forms in an arbitrary number of logarithms of algebraic numbers.

Theorem 1.4. (A. Baker, 1966) Let$\alpha _ { 1 } , \ldots , \alpha _ { m }$be algebraic numbers from C diferent from 0, 1 such that log$\alpha _ { 1 } , \ldots , \log \alpha _ { m }$are linearly independent over $\mathbb { Q }$. Then for every tuple$\left( \beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { m } \right)$of algebraic numbers from C diferent from$( 0 , 0 , \ldots , 0 )$we have

$$
\beta_ {0} + \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {m} \log \alpha_ {m} \neq 0.
$$

For applications to Diophantine problems, it is important that not only the above linear form is non-zero, but also that we have a strong enough lower bound for the absolute value of this linear form. We give a special case, where $\beta _ { 0 } = 0$and$\beta _ { 1 } , \ldots , \beta _ { m }$are rational integers.

Theorem 1.5. (A. Baker, 1975) Let$\alpha _ { 1 } , \ldots , \alpha _ { m }$be algebraic numbers from C diferent from 0, 1. Further, let$b _ { 1 } , \ldots , b _ { m }$be rational integers such that

$$
b _ {1} \log \alpha_ {1} + \dots + b _ {m} \log \alpha_ {m} \neq 0.
$$

Then

$$
\left| b _ {1} \log \alpha_ {1} + \dots + b _ {m} \log \alpha_ {m} \right| \geqslant (e B) ^ {- C},
$$

where$B : = \operatorname* { m a x } ( | b _ { 1 } | , . . . , | b _ { m } | )$and$C$is an efectively computable constant depending only on m and on$\alpha _ { 1 } , \ldots , \alpha _ { m }$

It is possible to get rid of the logarithms. Then Theorem 1.5 leads to the following:

Corollary 1.6. Let$\alpha _ { 1 } , \ldots , \alpha _ { m }$be algebraic numbers from C diferent from 0, 1 and let$b _ { 1 } , \ldots , b _ { m }$be rational integers such that

$$
\alpha_ {1} ^ {b _ {1}} \dots \alpha_ {m} ^ {b _ {m}} \neq 1.
$$

Then

$$
| \alpha_ {1} ^ {b _ {1}} \dots \alpha_ {m} ^ {b _ {m}} - 1 | \geqslant (e B) ^ {- C ^ {\prime}},
$$

where again$B : = \operatorname* { m a x } ( | b _ { 1 } | , \ldots , | b _ { m } | )$and where$C ^ { \prime }$is an efectively computable constant depending only on m and on$\alpha _ { 1 } , \ldots , \alpha _ { m }$

Proof. For the logarithm of a complex number z we choose log$z = \log | z | +$ iarg z with$- \pi < \arg z \leqslant \pi$. With this choice of log we have log$( 1 + w ) =$ $\scriptstyle \sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n - 1 } w ^ { n } / n$for$w \in \mathbb { C }$with$| w | < 1$. Using this power series expansion, one easily shows that

$$
| \log (1 + w) | \leqslant 2 | w | \text {   if   } | w | \leqslant 1 / 2.
$$

We apply this with$w : = \alpha _ { 1 } ^ { b _ { 1 } } \cdot \cdot \cdot \alpha _ { m } ^ { b _ { m } } - 1$$\mathrm { I f } \ | w | > 1 / 2$we are done, so we suppose that$| w | \leqslant 1 / 2$. We have to estimate from below$\left| \log ( 1 + w ) \right|$

Recall that the complex logarithm is additive only modulo 2πi. That is,

$$
\log (1 + w) = b _ {1} \log \alpha_ {1} + \dots + b _ {m} \log \alpha_ {m} + 2 k \pi i
$$

for some$k \in \mathbb { Z }$. We can apply Theorem 1.5 since$2 k \pi i = 2 k \log ( - 1 )$. Thus, we obtain

$$
| \log (1 + w) | \geqslant \left(e \max (B, | 2 k |)\right) ^ {- C _ {1}}
$$

where$C _ { 1 }$is an efectively computable constant depending only on m and $\alpha _ { 1 } , \ldots , \alpha _ { m }$. Since$| \log ( 1 + w ) | \leqslant 2 | w | \leqslant 1$we have

$$
\left| 2 k \pi i \right| \leqslant 1 + \sum_ {j = 1} ^ {m} \left| \log \alpha_ {j} \right| \cdot \left| b _ {j} \right| \leqslant \left(1 + \sum_ {j = 1} ^ {m} \log | \alpha_ {j} |\right) B.
$$

Hence$| k | \leqslant C _ { 2 } B$, say, and$| \log ( 1 + w ) | \geqslant ( e C _ { 2 } B ) ^ { - C _ { 1 } }$. This implies$| w | \geqslant$ ${ \scriptstyle \frac { 1 } { 2 } } ( e C _ { 2 } B ) ^ { - C _ { 1 } } \geq ( e B ) ^ { - C ^ { \prime } }$for a suitable$C ^ { \prime }$, as required.✷

For completeness, we give a completely explicit version of Corollary 1.6 in the case that$\alpha _ { 1 } , \ldots , \alpha _ { m }$are integers. The height of a rational number$a = x / y$ with$x , y \in \mathbb { Z }$coprime, is defined by$H ( a ) : = \operatorname* { m a x } ( | x | , | y | )$

Theorem 1.7. (Matveev, 2000) Let$a _ { 1 } , \ldots , a _ { m }$be non-zero rational numbers and let$b _ { 1 } , \ldots , b _ { m }$be integers such that

$$
a _ {1} ^ {b _ {1}} \dots a _ {m} ^ {b _ {m}} \neq 1.
$$

Then$| a _ { 1 } ^ { b _ { 1 } } \cdot \cdot \cdot a _ { m } ^ { b _ { m } } - 1 | \geqslant ( e B ) ^ { - C ^ { \prime } }$, where

$$
\begin{array}{l} B = \max (| b _ {1} |, \ldots , | b _ {m} |), \\ C ^ {\prime} = \frac {1}{2} e \cdot m ^ {4. 5} 3 0 ^ {m + 3} \prod_ {j = 1} ^ {m} \max \big (1, \log H (a _ {j}) \big). \end{array}
$$

To illustrate the power of this result we give a quick application.

Corollary 1.8. let$a , b$be integers with a$\geqslant 2 , b \geqslant 2$. Then there is an efectively computable number$C _ { 1 } > 0$, depending only on$a , b ,$such that for any two positive integers m, n,

$$
\left| a ^ {m} - b ^ {n} \right| \geqslant \frac {\max \left(a ^ {m} , b ^ {n}\right)}{\left(e \max (m , n)\right) ^ {C _ {1}}}.
$$

Consequently, for any non-zero integer k, there exists an efectively computable number$C _ { 2 }$, depending on a, b, k such that if m, n are positive integers with $a ^ { m } - b ^ { n } = k$, then m,$n \leqslant C _ { 2 }$

Proof. Let m, n be positive integers. Put$B : = \operatorname* { m a x } ( m , n )$. Assume without loss of generality that$a ^ { m } \geqslant b ^ { n }$. By Corollary 1.6 or Theorem 1.7 we have

$$
\left| 1 - b ^ {n} a ^ {- m} \right| \geqslant (e B) ^ {- C _ {1}},
$$

where$C _ { 1 }$is an efectively computable number depending only on$a , b .$. Multiplying with$a ^ { m }$gives our first assertion.

Now let m, n be positive integers with$a ^ { m } - b ^ { n } = k$. Put again$B : =$ $\operatorname* { m a x } ( m , n )$. Then since$a , b \geqslant 2$

$$
| k | \geqslant 2 ^ {B} \cdot (e B) ^ {- C _ {1}}.
$$

This proves that B is bounded above by an efectively computable number depending on$a , b , k$✷

In 1844, Catalan conjectured that the equation in four unknowns,

$$
x ^ {m} - y ^ {n} = 1 \text { in } x, y, m, n \in \mathbb {Z} \text { with } x, y, m, n \geqslant 2
$$

has only one solution, namely$3 ^ { 2 } - 2 ^ { 3 } = 1$. In 1976, as one of the striking consequences of the results on linear forms in logarithms mentioned above, Tijdeman proved that there is an efectively computable constant C, such that for every solution$( x , y , m , n )$of Catalan’s equation, one has$x ^ { m } , y ^ { n } \leqslant C$ The constant C can be computed but it is extremely large. Several people tried to prove Catalan’s conjecture, on the one hand by reducing Tijdeman’s constant C using sharper linear forms in logarithm estimates, on the other hand by showing that$x ^ { m } , y ^ { n }$have to be very large as long as$( x ^ { m } , y ^ { n } ) \neq ( 3 ^ { 2 } , 2 ^ { 3 } )$ and finally using heavy computations. This didn’t lead to success. In 2000 Mihailescu managed to prove Catalan’s conjecture by an algebraic method which is completely independent of linear forms in logarithms.

We give another application. Consider the sequence$\{ a _ { n } \}$with$a _ { n } \ = \ 2 ^ { n }$ for$n = 0 , 1 , 2 , \ldots$Note that$a _ { n + 1 } - a _ { n } = a _ { n }$. Similarly, we may consider the increasing sequence$\{ a _ { n } \}$of numbers which are all composed of primes from$\{ 2 , 3 \} , \ \mathrm { i . e . , ~ } 1 , 2 , 3 , 4 , 6 , 8 , 9 , 1 2 , 1 6 , 1 8 , 2 4 , 2 7 , 3 2 , . .$. and ask how the gap $a _ { n + 1 } - a _ { n }$compares with$a _ { n } { \mathrm { ~ a s ~ } } n \to \infty$. More generally, we may take a finite set of primes and ask this question about the sequence of consecutive integers composed of these primes.

Theorem 1.9. (Tijdeman, 1974) Let$S = \{ p _ { 1 } , \ldots . p _ { t } \}$be a finite set of distinct primes, and let$a _ { 1 } < a _ { 2 } < a _ { 3 } < \cdots$be the sequence of consecutive positive integers composed of primes from S. Then there are efectively computable positive numbers$c _ { 1 } , c _ { 2 }$, depending on$t , p _ { 1 } , \ldots , p _ { t } ,$, such that

$$
a _ {n + 1} - a _ {n} \geqslant \frac {a _ {n}}{c _ {1} (\log a _ {n}) ^ {c _ {2}}} \text {   for   } n = 1, 2, \dots .
$$

Proof. We have$a _ { n } = p _ { 1 } ^ { k _ { 1 } } \cdot \cdot \cdot p _ { t } ^ { k _ { t } }$, and$a _ { n + 1 } = p _ { 1 } ^ { l _ { 1 } } \cdot \cdot \cdot p _ { t } ^ { l _ { t } }$with non-negative integers$k _ { i } , l _ { i }$. By Corollary 1.6,

$$
\left| \frac {a _ {n + 1}}{a _ {n}} - 1 \right| = | p _ {1} ^ {l _ {1} - k _ {1}} \dots p _ {t} ^ {l _ {t} - k _ {t}} - 1 | \geqslant (e B) ^ {- C},
$$

where$B : = \operatorname* { m a x } ( | l _ { 1 } - k _ { 1 } | , \ldots , | l _ { t } - k _ { t } | )$. First note that

$$
k _ {i} \leqslant \frac {\log a _ {n}}{\log p _ {i}} \leqslant \frac {\log a _ {n}}{\log 2} \mathrm{for} i = 1, \ldots , t.
$$

Next,$a _ { n + 1 } \leqslant a _ { n } ^ { 2 }$. So

$$
l _ {i} \leqslant \frac {\log a _ {n + 1}}{\log p _ {i}} \leqslant \frac {\log a _ {n} ^ {2}}{\log 2} \text { for } i = 1, \dots , t.
$$

Hence$B \leqslant 2 \log a _ { n } /$log 2. It follows that$a _ { n + 1 } - a _ { n } \geqslant a _ { n } ( 2 e \log a _ { n } / \log 2 ) ^ { - C }$. ✷

Most results in Diophantine approximation that have been proved for algebraic numbers in C have an analogue for p-adic numbers. We can define $p { \cdot }$adic exponentiation, p-adic logarithms, etc., and this enables us to formulate analogues for Theorem 1.1– Theorem 1.7 in the p-adic setting. We give an analogue of Corollary 1.6 in the case that$\alpha _ { 1 } , \ldots , \alpha _ { m }$are rational numbers. There is a more general version for algebraic$\alpha _ { 1 } , \ldots , \alpha _ { m }$but this is more dificult to state.

Theorem 1.10. (Yu, 1986) Let p be a prime number, let$a _ { 1 } , \ldots , a _ { m }$be non-zero rational numbers which are not divisible by$p .$. Further, let$b _ { 1 } , \ldots , b _ { m }$be

integers such that

$$
a _ {1} ^ {b _ {1}} \dots a _ {m} ^ {b _ {m}} \neq 1.
$$

Put$B : = \operatorname* { m a x } ( | b _ { 1 } | , \ldots , | b _ { m } | )$. Then

$$
| a _ {1} ^ {b _ {1}} \dots a _ {m} ^ {b _ {m}} - 1 | _ {p} \geqslant (e B) ^ {- C}
$$

where$C$is an efectively computable number depending on$p ,$m and$a _ { 1 } , \ldots , a _ { m }$

For$m = 1$there is a sharper result which can be proved by elementary means (Exercise 6a). But for m$\geqslant 2$the proof is very dificult.

## 2. The effective Siegel-Mahler-Lang Theorem

Let K be an algebraic number field and let Γ be a finitely generated, multi-plicative subgroup of$K ^ { * } , \mathrm { i . e . }$, there are$\gamma _ { 1 } , \dotsc , \gamma _ { t } \in \Gamma$such that every element of Γ can be expressed as

$$
\zeta \gamma_ {1} ^ {z _ {1}} \dots \gamma_ {t} ^ {z _ {t}}
$$

where$\zeta$is a root of unity in$K .$, and$z _ { 1 } , \ldots , z _ { t }$are integers. Further, let$a , b$be non-zero elements from K and consider the equation

$$
a x + b y = 1 \text { in } x, y \in \Gamma .\tag{2.1}
$$

In 1979, Győry gave an efective proof of the Siegel-Mahler-Lang Theorem.

Theorem 2.1. (Győry, 1979) Equation (2.1) has only finitely many solutions, and its set of solutions can be determined efectively.

The idea of the proof is to express a solution$( x , y )$of (2.1) as

$$
x = \zeta_ {1} \gamma_ {1} ^ {b _ {1}} \dots \gamma_ {t} ^ {b _ {t}}, y = \zeta_ {2} \gamma_ {1} ^ {b _ {1} ^ {\prime}} \dots \gamma_ {t} ^ {b _ {t} ^ {\prime}}
$$

with$\zeta _ { 1 } , \zeta _ { 2 } \in U _ { K } , b _ { i } , b _ { i } ^ { \prime } \in \mathbb { Z }$. By combining Corollary 1.6 and a generalization of Theorem 1.10 for algebraic numbers instead of the rational numbers$a _ { 1 } , \ldots , a _ { m }$ in the statement of that lemma, Győry shows that for every solution$( x , y )$of (2.1) one has max$( | b _ { 1 } | , \dots , | b _ { t } ^ { \prime } | ) \leqslant C$, where$C$is efectively computable in terms of$K , \gamma _ { 1 } , \ldots , \gamma _ { t }$. Then one can find all solutions of (2.1) by checking for each$\zeta _ { 1 } , \zeta _ { 2 } \in U _ { K }$and$b _ { i } , b _ { i } ^ { \prime } \leqslant C$whether$a x + b y = 1$holds.

We prove two special cases of Theorem 2.1, namely the case that$a , b \in \mathbb { Q }$ and Γ is contained in$\mathbb { Q } ^ { * }$, and the case that$a , b$lie in an algebraic number field $K$and Γ is the group of units of the ring of integers of$K$.

As has been explained before, if$a , b \in \mathbb { Q }$and Γ is contained in$\mathbb { Q } ^ { * }$, then Eq. (2.1) can be reduced to an S-unit equation. There are rational numbers $\gamma _ { 1 } , \ldots , \gamma _ { t }$such that all elements of Γ are of the shape$\pm \gamma _ { 1 } ^ { z _ { 1 } } \cdots \gamma _ { t } ^ { z _ { t } }$. Let$S =$ $\{ p _ { 1 } , \ldots , p _ { t } \}$be the prime numbers occurring in the prime factorizations of the numerators and denominators of$a , b , \gamma _ { 1 } , \ldots , \gamma _ { t }$. Then$a , b , \gamma _ { 1 } , \ldots , \gamma _ { t }$lie in the multiplicative group of S-units

$$
\mathbb {Z} _ {S} ^ {*} = \{\pm p _ {1} ^ {z _ {1}} \dots p _ {t} ^ {z _ {t}}: z _ {1}, \ldots , z _ {t} \in \mathbb {Z} \}.
$$

Hence if$( x , y )$is a solution to (2.1), the numbers ax, by are S-units. So instead of (2.1), we may as well consider

$$
x + y = 1 \text { in } x, y \in \mathbb {Z} _ {S} ^ {*}.\tag{2.2}
$$

Theorem 2.2. Let$S ~ = ~ \{ p _ { 1 } , . . . , p _ { t } \}$be a finite set of primes. Then (2.2) has only finitely many solutions, and its set of solutions can be determined efectively.

Proof. Let$( x , y )$be a solution of (2.2). We may write$x = u / w , y = v / w$ where$u , v , w$are integers with$\operatorname* { g c d } ( u , v , w ) = 1$. Then

$$
u + v = w.\tag{2.3}
$$

The integers$u , v , w$are composed of primes from$S _ { ; }$and moreover, no prime divides two numbers among$u , v ,$, w since$u , v ,$, w are coprime. After reordering the primes$p _ { 1 } , \ldots , p _ { t } .$, we may assume that

$$
u = \pm p _ {1} ^ {b _ {1}} \dots p _ {r} ^ {b _ {r}}, \quad v = \pm p _ {r + 1} ^ {b _ {r + 1}} \dots p _ {s} ^ {b _ {s}}, \quad w = \pm p _ {s + 1} ^ {b _ {s + 1}} \dots p _ {t} ^ {b _ {t}},
$$

where$0 \leqslant r \leqslant s \leqslant t$and the$b _ { i }$are non-negative integers (empty products are equal to 1; for instance if$r = 0$then$u = \pm 1 )$). We have to prove that $B : = \operatorname* { m a x } ( b _ { 1 } , \ldots , b _ { t } )$is bounded above by an efectively computable number depending only on$p _ { 1 } , \ldots , p _ { t }$. By symmetry, we may assume that$B = b _ { t }$. Then using$- ( u / v ) - 1 = - ( w / v )$we obtain

$$
0 <   | \pm p _ {1} ^ {b _ {1}} \dots p _ {r} ^ {b _ {r}} p _ {r + 1} ^ {- b _ {r + 1}} \dots p _ {s} ^ {- b _ {s}} - 1 | _ {p _ {t}} = | w / v | _ {p _ {t}} = p _ {t} ^ {- b _ {t}} = p _ {t} ^ {- B}.
$$

From Theorem 1.10 we obtain that$| \cdot \cdot \cdot | _ { p _ { t } } \geqslant ( e B ) ^ { - C }$, where C is efectively computable in terms of$p _ { 1 } , \ldots , p _ { t }$. Hence

$$
(e B) ^ {- C _ {2}} \leqslant p _ {t} ^ {- B}.
$$

So indeed, B is bounded above by an efectively computable number depending on$p _ { 1 } , \ldots , p _ { t }$✷

Remark. In his PhD-thesis from 1988, de Weger gave a practical algorithm, based on strong linear forms in logarithms estimates and the LLL-basis reduction algorithm, to solve equations of the type (2.2). As a consequence, he showed that the$x + y = z$has precisely 545 solutions in positive integers$x , y , z$ with$x \leqslant y .$, all of the shape$2 ^ { b _ { 1 } } 3 ^ { b _ { 2 } } 5 ^ { b _ { 3 } } 7 ^ { b _ { 4 } } 1 1 ^ { b _ { 5 } } 1 3 ^ { b _ { 6 } }$with$b _ { i } \in \mathbb { Z }$

## Theorem 2.3. Let$a , b \in K ^ { * }$. Then the equation

$$
a x + b y = 1 \text { in } x, y \in \mathcal {O} _ {K} ^ {*}\tag{2.4}
$$

has only finitely many solutions and its set of solutions can be determined efectively.

Corollary 2.4. Let$F ( X , Y ) = a _ { 0 } X ^ { d } + a _ { 1 } X ^ { d - 1 } Y + \cdot \cdot \cdot + a _ { d } Y ^ { d }$be a binary form in$\mathbb { Z } [ X , Y ]$such that$F ( X , 1 )$has at least three distinct roots in C, and let m be a non-zero integer. Then the equation

$$
F (x, y) = m \text { in } x, y \in \mathbb {Z}
$$

has only finitely many solutions, and its set of solutions can be determined efectively.

Corollary 2.5. Let$f ( X ) \in \mathbb { Z } [ X ]$be a polynomial without multiple zeros and n an integer$\geqslant 2$. Assume that f has at least two zeros in C if n$\geqslant 3$and at least three zeros in$\mathbb { C } \ i f \ n = 2$. Then the equation

$$
y ^ {n} = f (x) \text { in } x, y \in \mathbb {Z}
$$

has only finitely many solutions, and its set of solutions can be determined efectively.

In Frits’ lecture notes on the Siegel-Mahler Theorem it was explained how the equations in Corollaries 2.4 and 2.5 can be reduced to (2.4).

In the proof of Theorem 2.3 we need some facts on units. Suppose the number field K has degree d. Then K has precisely d distinct embeddings in $\mathbb { C } .$, which can be divided into real embeddings (of which the image lies in R) and complex embeddings (with image in C but not in R). Further, the complex embeddings occur in complex conjugate pairs$\sigma , { \overline { { \sigma } } }$, where$\overline { { \sigma } } ( x ) : = \overline { { \sigma ( x ) } }$for $x \in K$. Suppose that K has precisely$r _ { 1 }$real embeddings, and precisely$r _ { 2 }$ pairs of complex conjugate embeddings, where$r _ { 1 } + 2 r _ { 2 } = d . \nonumber$. We renumber the embeddings such that$\sigma _ { 1 } , \ldots , \sigma _ { r _ { 1 } }$are the real embeddings of$K$, and$\sigma _ { r _ { 1 } + r _ { 2 } + i } =$ $\overline { { \sigma _ { r _ { 1 } + i } } }$for$i = 1 , \ldots , r _ { 2 }$

The following fact is well known.

Lemma 2.6. Let ε be a unit of${ \mathcal { O } } _ { K }$. Then

$$
N _ {K / \mathbb {Q}} (\varepsilon) = \prod_ {i = 1} ^ {d} \sigma_ {i} (\varepsilon) = \pm 1.
$$

Proof. Exercise.

To study the units of${ \mathcal { O } } _ { K }$, it is useful to consider the absolute values of their conjugates. Clearly, for$\varepsilon \in { \mathcal { O } } _ { K } ^ { * }$we have

$$
| \sigma_ {r _ {1} + r _ {2} + i} (\varepsilon) | = | \sigma_ {r _ {1} + i} (\varepsilon) | \mathrm{for} i = 1 \dots r _ {2},
$$

$$
\prod_ {i = 1} ^ {r _ {1}} | \sigma_ {i} (\varepsilon) | \prod_ {i = r _ {1} + 1} ^ {r _ {1} + r _ {2}} | \sigma_ {i} (\varepsilon) | ^ {2} = 1,
$$

so$| \sigma _ { i } ( \varepsilon ) | \ ( i = 1 , \ldots , r _ { 1 } + r _ { 2 } - 1 )$determine$| \sigma _ { i } ( \varepsilon ) | \ ( i = r _ { 1 } + r _ { 2 } , \ldots , d )$

The following lemma is a more precise version of Dirichlet’s Unit Theorem.

Lemma 2.7. Let$r : = r _ { 1 } + r _ { 2 } - 1$and define the map

$$
L: \mathcal {O} _ {K} ^ {*} \to \mathbb {R} ^ {r}: \varepsilon \mapsto (\log | \sigma_ {1} (\varepsilon), \dots , \log | \sigma_ {r} (\varepsilon) |).
$$

Then L is a group homomorphism. The kernel of L is the group$U _ { K }$of roots $o f$unity of K and the image of L is a lattice of rank r in$\mathbb { R } ^ { r }$.

Choose units$\varepsilon _ { 1 } , \ldots , \varepsilon _ { r }$such that$L ( \varepsilon _ { 1 } ) , \dots , L ( \varepsilon _ { r } )$form a basis of the lattice $L ( { \mathcal { O } } _ { K } ^ { * } )$. Then every$\varepsilon \in { \mathcal { O } } _ { K } ^ { * }$can be expressed uniquely as

$$
\zeta \varepsilon_ {1} ^ {b _ {1}} \dots \varepsilon_ {r} ^ {b _ {r}} \text { with } \zeta \in U _ {K}, b _ {1}, \ldots , b _ {r} \in \mathbb {Z}.\tag{2.5}
$$

Further, the matrix

$$
M := \left( \begin{array}{c c c} \log | \sigma_ {1} (\varepsilon_ {1}) | & \dots & \log | \sigma_ {1} (\varepsilon_ {r}) | \\ \vdots & & \vdots \\ \log | \sigma_ {r} (\varepsilon_ {1}) | & \dots & \log | \sigma_ {r} (\varepsilon_ {r}) | \end{array} \right)\tag{2.6}
$$

is invertible.

We deduce a consequence.

Lemma 2.8. There is a constant$C > 0$with the following property.$I f \varepsilon i s$ any unit$o f { \mathcal { O } } _ { K }$, and$b _ { 1 } , \ldots , b _ { r }$are the corresponding integers defined by (2.4),

then

$$
\max (| b _ {1} |, \dots , | b _ {r} |) \leqslant C \cdot \max _ {1 \leqslant i \leqslant d} \log | \sigma_ {i} (\varepsilon) |.
$$

Proof. Let b$\mathbf { \Psi } : = ( b _ { 1 } , \dots , b _ { r } ) ^ { T }$(column vector). Then$L ( \varepsilon ) = M \mathbf { b }$, hence$\mathbf { b } =$ $M ^ { - 1 } L ( \varepsilon )$. Writing$M ^ { - 1 } = \left( a _ { i j } \right)$, we obtain

$$
b _ {i} = \sum_ {j = 1} ^ {r} a _ {i j} \sigma_ {j} (\varepsilon) (i = 1, \dots , r).
$$

Applying the triangle inequality, we get

$$
\max _ {1 \leqslant i \leqslant r} | b _ {i} | \leqslant \left(\max _ {1 \leqslant i \leqslant r} \sum_ {j = 1} ^ {r} | a _ {i j} |\right) \cdot \max _ {1 \leqslant j \leqslant r} | \sigma_ {j} (\varepsilon) |.
$$

Proof of Theorem 2.3. Let$( x , y )$be a solution of (2.3). There are$\zeta _ { 1 } , \zeta _ { 2 } \in$ $U _ { K }$, as well as integers$a _ { 1 } , \dotsc , a _ { r } , b _ { 1 } , \dotsc , b _ { r }$, such that

$$
x = \zeta_ {1} \varepsilon_ {1} ^ {a _ {1}} \dots \varepsilon_ {r} ^ {a _ {r}}, y = \zeta_ {2} \varepsilon_ {1} ^ {b _ {1}} \dots \varepsilon_ {r} ^ {b _ {r}}.
$$

Thus

$$
a \zeta_ {1} \varepsilon_ {1} ^ {a _ {1}} \cdot \cdot \cdot \varepsilon_ {r} ^ {a _ {r}} + b \zeta_ {2} \varepsilon_ {1} ^ {b _ {1}} \cdot \cdot \cdot \varepsilon_ {r} ^ {b _ {r}} = 1.
$$

We assume without loss of generality that$B : = \operatorname* { m a x } ( | a _ { 1 } | , \ldots , | b _ { r } | ) = | b _ { r } |$. We estimate from above and below,

$$
\Lambda_ {i} := | \sigma_ {i} (a) \sigma (\zeta_ {1}) \sigma_ {i} (\varepsilon_ {1}) ^ {a _ {1}} \dots \sigma_ {i} (\varepsilon_ {r}) ^ {a _ {r}} - 1 | = | \sigma_ {i} (b) \sigma_ {i} (y) |
$$

for a suitable choice of$i .$

In fact, let$| \sigma _ { i } ( y ) |$be the smallest, and$| \sigma _ { j } ( y ) |$the largest among$| \sigma _ { 1 } ( y ) | , \dots , | \sigma _ { d } ( y ) |$|. Then by Lemma 2.6,

$$
\left| \sigma_ {i} (y) \right| ^ {d - 1} \left| \sigma_ {j} (y) \right| \leqslant 1
$$

and subsequently by Lemma 2.8,

$$
| \sigma_ {i} (y) | \leqslant | \sigma_ {j} (y) | ^ {- 1 / (d - 1)} \leqslant e ^ {- B / C (d - 1)}.
$$

This leads to

$$
\Lambda_ {i} \leqslant | \sigma_ {i} (\beta) | e ^ {- B / C (d - 1)}.
$$

By Corollary 1.6 we have$\left| \Lambda _ { i } \right| \geqslant ( e B ) ^ { - C ^ { \prime } }$for some efectively computable number$C ^ { \prime }$depending on$a , \varepsilon _ { 1 } , \ldots , \varepsilon _ { r }$and the finitely many roots of unity of$K$. We infer

$$
(e B) ^ {- C ^ {\prime}} \leqslant | \sigma_ {i} (a) | e ^ {- B / C (d - 1)}
$$

and this leads to an efectively computable upper bound for B.

Remark. There are practical algorithms to solve equations of the type (2.4) which work well as long as the degree of the field K, and the fundamental units of the ring of integers of$K$, are not too large. These algorithms are again based on linear forms in logarithms estimates and the LLL-algorithm. For instance, in 2000 Wildanger determined all solutions of the equation$x + y = 1$ in$x , y \in { \mathcal { O } } _ { K } ^ { * }$, with$K = \mathbb { Q } ( \cos ( 2 \pi / 1 9 ) )$). The number field K has degree 9 and all its embeddings are real. Thus, the unit group$\mathcal { O } _ { K } ^ { * }$has rank 8.

## 3. Exercises

Exercise 1. Let$p _ { 1 } , \ldots , p _ { s } , p _ { s + 1 } , \ldots , p _ { t }$be distinct prime numbers. Let$A$be the set of positive integers composed of primes from$p _ { 1 } , \ldots , p _ { s }$, and$B$the set of positive integers composed of primes from$p _ { s + 1 } , \ldots , p _ { t }$

(a) Prove that there exist positive numbers$c _ { 1 } , c _ { 2 }$, efectively computable in terms of$p _ { 1 } , \ldots , p _ { t }$such that

$$
| x - y | \geqslant \frac {\max (x , y)}{c _ {1} (\log \max (x , y)) ^ {c _ {2}}} \text { for   all } x \in A, y \in B.
$$

(b) Given a non-zero integer a, denote by$P ( a )$the largest prime number dividing a, with$P ( \pm 1 ) : = 1$. Prove that

$$
\lim _ {x \in A, y \in B, \max (| x |, | y |) \to \infty} P (x - y) = \infty .
$$

Exercise 2. Let$f ( X ) = X ^ { 2 } - A X - B$be a polynomial with coeficients $A , B \in \mathbb { Z }$. Let$\alpha , \beta$be the two zeros of f in C. Assume that f is irreducible, and that$\alpha / \beta$is not a root of unity. Let the sequence$U = \{ u _ { n } \} _ { n = 0 } ^ { \infty }$in$\mathbb { Z }$be given by

$$
u _ {n} = A u _ {n - 1} + B u _ {n - 2} (n \geqslant 0)
$$

and initial values$u _ { 0 } , u _ { 1 } \in \mathbb { Z }$, not both 0.

(a) Prove that$M : = \operatorname* { m a x } ( | \alpha | , | \beta | ) > 1$

(b) Prove that there are non-zero algebraic numbers$\gamma _ { 1 } , \gamma _ { 2 }$such that$u _ { n } =$ $\gamma _ { 1 } \alpha ^ { n } + \gamma _ { 2 } \beta ^ { n }$for$n \geqslant 0$

(c) Prove that there is an efectively computable number C such that$u _ { n } \neq$ 0 for$n \geqslant C$

(d) Prove that there are efectively computable positive numbers$c _ { 1 } , c _ { 2 }$such that$| u _ { n } | \geqslant M ^ { n } / c _ { 1 } n ^ { c _ { 2 } }$for$n \geqslant C$

Exercise 3. Let$A , B , C$be integers such that$C \neq 0$and

$$
X ^ {3} - A X ^ {2} - B X - C = (X - \alpha_ {1}) (X - \alpha_ {2}) (X - \alpha_ {3}),
$$

where$\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } \in \mathbb { C }$, and none of the quotients$\alpha _ { i } / \alpha _ { j } \ ( 1 \le i < j \le 3 )$is a root of unity. Consider the linear recurrence sequence$U = \{ u _ { n } \} _ { n = 0 } ^ { \infty } , \mathrm { g i v e n }$by

$$
u _ {n} = A u _ {n - 1} + B u _ {n - 2} + C u _ {n - 3} (n \geqslant 3)
$$

and initial values$u _ { 0 } , u _ { 1 } , u _ { 2 } \in \mathbb { Z }$, not all zero.

(a) Prove that there exist algebraic numbers$\gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 }$such that

$$
u _ {n} = \gamma_ {1} \alpha_ {1} ^ {n} + \gamma_ {2} \alpha_ {2} ^ {n} + \gamma_ {3} \alpha_ {3} ^ {n} \mathrm{for} n \geqslant 0.
$$

(b) Prove that$| \alpha _ { 1 } | = | \alpha _ { 2 } | = | \alpha _ { 3 } |$cannot hold.

(c) Prove that there exists an efectively computable number$C ,$depending on$A , B , C$, such that if n is a non-negative integer with$u _ { n } = 0$then $n < C .$

Exercise 4. In 1995, Laurent, Mignotte and Nesterenko proved the following explicit estimate for linear forms in two logarithms. Let$a _ { 1 } , a _ { 2 }$be two positive rational numbers$\neq 1$. Further, let$b _ { 1 } , b _ { 2 }$be non-zero integers. Suppose that $\Lambda : = b _ { 1 } \log a _ { 1 } - b _ { 2 } \log a _ { 2 } \neq 0$. Then

$$
\begin{array}{l} \log | \Lambda | \geqslant \\ - 2 2 \left(\max \left\{\log \left(\frac {| b _ {1} |}{\log H (a _ {2})} + \frac {| b _ {2} |}{\log H (a _ {1})}\right) + 0. 0 6, 2 1 \right\}\right) ^ {2} \log H (a _ {1}) \log H (a _ {2}). \end{array}
$$

Using this estimate, compute an upper bound$C ,$such that for all positive integers$m , n$with$9 7 ^ { m } - 8 9 ^ { n } = 8$we have$m , n \leqslant C$

Hint. Use$| \log ( 1 + z ) | \leqslant 2 | z | { \mathrm { ~ i f ~ } } | z | \leqslant { \frac { 1 } { 2 } }$

Exercise 5. In this exercise you are asked to apply the estimate of Laurent, Mignotte and Nesterenko to more advanced equations.

(a) Prove that the equation

$$
x ^ {n} - 2 y ^ {n} = 1 \text { in   unknowns } x, y \text { with } x \geqslant 2, y \geqslant 2
$$

has no solutions if$n > 1 0 0 0 0$

Hint. Applying Laurent-Mignotte-Nesterenko to an appropriate linear form in two logarithms you will get a lower estimate depending on n and$x , y$. But you can derive also an upper estimate which depends on $n , x , y$. Comparing the two estimates leads to an upper bound for n independent of$x , y$

(b) Let$a , b , c$be positive integers. Prove that there is a number$C ,$efectively computable in terms of$a , b , c ,$such that the equation

$$
a x ^ {n} - b y ^ {n} = c
$$

has no solutions if$n > C$. In the case$a = b$you may give an elementary proof, without using the result of Laurent-Mignotte-Nesterenko.

(c) Let k be a fixed integer$\geqslant 2$. Prove that the equation

$$
y ^ {z} = \binom{x}{k} \text {   in   integers   } x, y, z \text {   with   } x > 0, y \geqslant 2, z \geqslant 3
$$

has only finitely many solutions.

Exercise 6. In this exercise, you are asked to prove a very simple case of Theorem 1.10 and to apply this to certain Diophantine equations.

(a) Let a be an integer, and$p \textrm { a }$prime, such that$| a | _ { p } \leqslant p ^ { - 1 } { \mathrm { ~ i f ~ } } p > 2$and $| a | _ { 2 } \leqslant 2 ^ { - 2 } { \mathrm { ~ i f ~ } } p = 2$. Prove that for any positive integer b we have

$$
\left| (1 + a) ^ {b} - 1 \right| _ {p} = \left| a b \right| _ {p} \geqslant 1 / a b.
$$

Hint. You may either prove that$| { \binom { b } { k } } a ^ { k } | _ { p } < | a b | _ { p }$for$k \geqslant 2$or write $b = u p ^ { t }$where u is an integer not divisible by p and t a non-negative integer, and use induction on t.

(b) Let p be a prime$\geqslant 5$. Using (a), prove that the equation$p ^ { x } - 2 ^ { y } = 1$ has no solutions in integers$x \geqslant 2 , y \geqslant 2$. Prove also that the equation $2 ^ { x } - p ^ { y } = 1$has no solutions in integers$x \geq 2 , y \geqslant 2$