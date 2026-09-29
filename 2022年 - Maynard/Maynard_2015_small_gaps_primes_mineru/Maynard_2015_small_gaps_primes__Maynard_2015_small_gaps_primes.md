# SMALL GAPS BETWEEN PRIMES

JAMES MAYNARD

Abstract. We introduce a refinement of the GPY sieve method for studying prime k-tuples and small gaps between primes. This refinement avoids previous limitations of the method, and allows us to show that for each$k ,$the prime k-tuples conjecture holds for a positive proportion of admissible k-tuples. In particular, lim in$\dot { \phantom { } _ { n } } ( p _ { n + m } - p _ { n } ) < \infty$for every integer m. We also show that lim in$( p _ { n + 1 } - p _ { n } ) \leq 6 0 0$, and, if we assume the Elliott-Halberstam conjecture, that lim in$\dot { \zeta } _ { n } ( p _ { n + 1 } - p _ { n } ) \leq 1 2$and lim in$\displaystyle \mathrm { f } _ { n } ( p _ { n + 2 } - p _ { n } ) \leq 6 0 0$

## 1. Introduction

We say that a set$\mathcal { H } = \{ h _ { 1 } , \ldots , h _ { k } \}$of distinct non-negative integers is ‘admissible’ if, for every prime$p ,$there is an integer$a _ { p }$such that$a _ { p } \not \equiv h$(mod$p )$for all$h \in { \mathcal { H } }$. We are interested in the following conjecture.

Conjecture (Prime k-tuples conjecture). Let$\mathcal { H } = \{ h _ { 1 } , \ldots , h _ { k } \}$be admissible. Then there are infinitely many integers n such that all of$n + h _ { 1 } , . . . , n + h _ { k }$are prime.

When$k > 1$no case of the prime k-tuples conjecture is currently known. Work on approximations to the prime k-tuples conjecture has been very successful in showing the existence of small gaps between primes, however. In their celebrated paper [5], Goldston, Pintz and Yıldırım introduced a new method for counting tuples of primes, and this allowed them to show that

$$
\liminf _ {n} \frac {p _ {n + 1} - p _ {n}}{\log p _ {n}} = 0.\tag{1.1}
$$

The recent breakthrough of Zhang [9] managed to extend this work to prove

$$
\liminf _ {n} (p _ {n + 1} - p _ {n}) \leq 7 0   0 0 0   0 0 0,\tag{1.2}
$$

thereby establishing for the first time the existence of infinitely many bounded gaps between primes. Moreover, it follows from Zhang’s theorem the that number of admissible sets of size 2 contained in$[ 1 , x ] ^ { 2 }$which satisfy the prime 2-tuples conjecture is$\gg x ^ { 2 }$for large x. Thus, in this sense, a positive proportion of admissible sets of size 2 satisfy the prime 2-tuples conjecture. The recent polymath project [7] has succeeded in reducing the bound (1.2) to 4680, by optimizing Zhang’s arguments and introducing several new refinements.

The above results have used the ‘GPY method’ to study prime tuples and small gaps between primes, and this method relies heavily on the distribution of primes in arithmetic progressions. Given$\theta > 0$, we say the primes have ‘level of distribution$\theta ^ { , 1 } \mathrm { i f } ,$for every$A > 0$ we have

$$
\sum_ {q \leq x ^ {\theta}} \max _ {(a, q) = 1} \left| \pi (x; q, a) - \frac {\pi (x)}{\varphi (q)} \right| \ll_ {A} \frac {x}{(\log x) ^ {A}}.\tag{1.3}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>We note that diferent authors have given slightly diferent names or definitions to this concept. For the purposes of this paper, (1.3) will be our definition of the primes having level of distribution θ.</span></small>

The Bombieri-Vinogradov theorem establishes that the primes have level of distribution θ for every$\theta < 1 / 2$, and Elliott and Halberstam [1] conjectured that this could be extended to every $\theta < 1$. Friedlander and Granville [2] have shown that (1.3) cannot hold with$x ^ { \theta }$replaced with $x / ( \log x ) ^ { B }$for any fixed B, and so the Elliott-Halberstam conjecture is essentially the strongest possible result of this type.

The original work of Goldston, Pintz and Yıldırım showed the existence of bounded gaps between primes if (1.3) holds for some$\theta > 1 / 2$. Moreover, under the Elliott-Halberstam conjecture one had lim inf$_ { n } ( p _ { n + 1 } - p _ { n } ) \leq 1 6$. The key breakthrough of Zhang’s work was in establishing that a slightly weakened form of (1.3) holds for some$\theta > 1 / 2$

If one looks for bounded length intervals containing two or more primes, then the GPY method fails to prove such strong results. Unconditionally we are only able to improve upon the trivial bound from the prime number theorem by a constant factor [4], and even assuming the Elliott-Halberstam conjecture, the best available result [5] is

$$
\operatorname * {l i m i n f} _ {n} \frac {p _ {n + 2} - p _ {n}}{\log p _ {n}} = 0.\tag{1.4}
$$

The aim of this paper is to introduce a refinement of the GPY method which removes the barrier of$\theta = 1 / 2$to establishing bounded gaps between primes, and allows us to show the existence of arbitrarily many primes in bounded length intervals. This answers the second and third questions posed in [5] on extensions of the GPY method (the first having been answered by Zhang’s result). Our new method also has the benefit that it produces numerically superior results to previous approaches.

Theorem 1.1. Let$m \in \mathbb { N } .$. We have

$$
\liminf _ {n} (p _ {n + m} - p _ {n}) \ll m ^ {3} e ^ {4 m}.
$$

Terence Tao (private communication) has independently proven Theorem 1.1 (with a slightly weaker bound) at much the same time. He uses a similar method; the steps are more-or-less the same but the calculations are done diferently. We will indicate some of the diferences in our proofs as we go along.

We see that the bound in Theorem 1.1 is quite far from the conjectural bound of approximately m log m predicted by the prime m-tuples conjecture.

Our proof naturally generalizes (but with a weaker upper bound) to many subsequences of the primes which have a level of distribution$\theta > 0$. For example, we can show corresponding results where the primes are contained in short intervals$[ N , \dot { N } + N ^ { 7 / 1 2 + \epsilon } ]$for any$\epsilon > 0$or in an arithmetic progression modulo$q \ll ( \log N ) ^ { A }$. In particular, our method gives results for simultaneously prime values of linear functions, which might have specific interest. Given k distinct linear functions$L _ { i } ( n ) = a _ { i } n + b _ { i } ( 1 \leq i \leq k )$with positive integer coeficients such that the product function$\begin{array} { r } { \Pi ( n ) = \prod _ { i = 1 } ^ { k } L _ { i } ( n ) } \end{array}$has no fixed prime divisor, the method presented here shows that there are infinitely many integers n such that at least$( 1 / 4 + o _ { k \to \infty } ( 1 ) )$log k of the $L _ { i } ( n )$are prime.

Theorem 1.2. Let m$\in \mathbb { N } .$. Let$r \in \mathbb { N }$be suficiently large depending on$m ,$and let$\mathcal { A } =$ $\{ a _ { 1 } , a _ { 2 } , \ldots , a _ { r } \}$be a set of r distinct integers. Then we have

$$
\frac {\# \left\{\left\{h _ {1} , \dots , h _ {m} \right\} \subseteq \mathcal {A} : f o r i n f i n i t e l y m a n y n a l l o f n + h _ {1} , \dots , n + h _ {m} a r e p r i m e \right\}}{\# \left\{\left\{h _ {1} , \dots , h _ {m} \right\} \in \mathcal {A}\right)} \gg_ {m} 1.
$$

$$
\# \{\{h _ {1}, \dots , h _ {m} \} \subseteq \mathcal {A} \}
$$

Thus a positive proportion of admissible m-tuples satisfy the prime m-tuples conjecture for every m, in an appropriate sense.

Theorem 1.3. We have

$$
\liminf _ {n} (p _ {n + 1} - p _ {n}) \leq 6 0 0.
$$

We emphasize that the above result does not incorporate any of the technology used by Zhang to establish the existence of bounded gaps between primes. The proof is essentially elementary, relying only on the Bombieri-Vinogradov theorem. Naturally, if we assume that the primes have a higher level of distribution, then we can obtain stronger results.

Theorem 1.4. Assume that the primes have level of distribution θ for every$\theta < 1$. Then

$$
\begin{array}{l} \operatorname * {l i m i n f} _ {n} (p _ {n + 1} - p _ {n}) \leq 1 2, \\ \operatorname * {l i m i n f} _ {n} (p _ {n + 2} - p _ {n}) \leq 6 0 0. \end{array}
$$

Although the constant 12 of Theorem 1.4 appears to be optimal with our method in its current form, the constant 600 appearing in Theorem 1.3 and Theorem 1.4 is certainly not optimal. By performing further numerical calculations our method could produce a better bound, and also most of the ideas of Zhang’s work (and the refinements produced by the polymath project) should be able to be combined with this method to reduce the constant further. We comment that the assumption of the Elliott-Halberstam conjecture allows us to improve the bound on Theorem 1.1 to$O ( m ^ { 3 } e ^ { 2 m } )$.

## 2. An improved GPY sieve method

We first give an explanation of the key idea behind our new approach. The basic idea of the GPY method is, for a fixed admissible set$\mathcal { H } = \{ h _ { 1 } , \ldots , h _ { k } \}$, to consider the sum

$$
S (N, \rho) = \sum_ {N \leq n <   2 N} \left(\sum_ {i = 1} ^ {k} \chi_ {\mathbb {P}} \left(n + h _ {i}\right) - \rho\right) w _ {n}.\tag{2.1}
$$

Here$\chi _ { \mathbb { P } }$is the characteristic function of the primes,$\rho > 0$and$w _ { n }$are non-negative weights. If we can show that$S ( N , \rho ) > 0$then at least one term in the sum over n must have a positive contribution. By the non-negativity of$w _ { n }$, this means that there must be some integer$n \in$ $[ N , 2 N ]$such that at least$\lfloor \rho + 1 \rfloor$of the$n + h _ { i }$are prime. (Here ⌊x⌋ denotes the largest integer less than or equal to x.) Thus if$S ( N , \rho ) > 0$for all large N, there are infinitely many integers n for which at least$\lfloor \rho + 1 \rfloor$of the$n + h _ { i }$are prime (and so there are infinitely many bounded length intervals containing$\lfloor \rho + 1 \rfloor$primes).

The weights$w _ { n }$are typically chosen to mimic Selberg sieve weights. Estimating (2.1) can be interpreted as a ‘k-dimensional’ sieve problem. The standard Selberg k-dimensional weights (which can be shown to be essentially optimal in other contexts) are

$$
w_{n} = \Big(\sum_{\substack{d|\prod_{i = 1}^{k}(n + h_{i})\\ d <   R}}\lambda_{d}\Big)^{2},\qquad \lambda_{d} = \mu (d)(\log R / d)^{k}.\tag{2.2}
$$

With this choice we find that we just fail to prove the existence of bounded gaps between primes if we assume the Elliott-Halberstam conjecture. The key new idea in the paper of Goldston, Pintz and Yıldırım [5] was to consider more general sieve weights of the form

$$
\lambda_ {d} = \mu (d) F (\log R / d),\tag{2.3}
$$

for a suitable smooth function F. Goldston, Pintz and Yıldırım chose$F ( x ) = x ^ { k + l }$for suitable $l \in \mathbb { N } .$, which has been shown to be essentially optimal when k is large. This allows us to gain a factor of approximately 2 for large k over the previous choice of sieve weights. As a result we just fail to prove bounded gaps using the fact that the primes have exponent of distribution θ for any$\theta < 1 / 2$, but succeed in doing so if we assume they have level of distribution$\theta > 1 / 2$

The new ingredient in our method is to consider a more general form of the sieve weights

$$
w _ {n} = \Big (\sum_ {d _ {i} | n + h _ {i} \forall i} \lambda_ {d _ {1}, \dots , d _ {k}} \Big) ^ {2}.\tag{2.4}
$$

Using such weights with$\lambda _ { d _ { 1 } , \dots , d _ { k } }$is the key feature of our method. It allows us to improve on the previous choice of sieve weights by an arbitrarily large factor, provided that k is sufficiently large. It is the extra flexibility gained by allowing the weights to depend on the divisors of each factor individually which gives this improvement.

The idea to use such weights is not entirely new. Selberg [8, Page 245] suggested the possible use of similar weights in his work on approximations to the twin prime problem, and Goldston and Yıldırım [6] considered similar weights in earlier work on the GPY method, but with the support restricted to$d _ { i } < R ^ { 1 / k }$for all i.

We comment that our choice of$\lambda _ { d _ { 1 } , \dots , d _ { k } }$will look like

$$
\lambda_ {d _ {1}, \dots , d _ {k}} \approx \left(\prod_ {i = 1} ^ {k} \mu (d _ {i})\right) f (d _ {1}, \dots , d _ {k}),\tag{2.5}
$$

for a suitable smooth function f. For our precise choice of$\lambda _ { d _ { 1 } , \dots , d _ { k } }$(given in Proposition 4.1) we find it convenient to give a slightly diferent form of$\lambda _ { d _ { 1 } , \dots , d _ { k } }$, but weights of the form (2.5) should produce essentially the same results.

## 3. Notation

We shall view k as a fixed integer, and$\mathcal { H } = \{ h _ { 1 } , \ldots , h _ { k } \}$as a fixed admissible set. In particular, any constants implied by the asymptotic notation o, O or ≪ may depend on k and H. We will let N denote a large integer, and all asymptotic notation should be interpreted as referring to the limit$N \to \infty$

All sums, products and suprema will be assumed to be taken over variables lying in the natural numbers$\mathbb { N } = \{ 1 , 2 , \dots \}$unless specified otherwise. The exception to this is when sums or products are over a variable$p ,$, which instead will be assumed to lie in the prime numbers$\mathbb { P } = \{ 2 , 3 , \hdots , \}$

Throughout the paper, ϕ will denote the Euler totient function,$\tau _ { r } ( n )$the number of ways of writing n as a product of r natural numbers and$\mu$the Moebius function. We will let$\epsilon$be a fixed positive real number, and we may assume without further comment that ǫ is suficiently small at various stages of our argument. We let$p _ { n }$denote the$n ^ { t h }$prime, and #A denote the number of elements of a finite set A. We use ⌊x⌋ to denote the largest integer$n \leq x ,$and ⌈x⌉ the smallest integer$n \geq x$. We let$( a , b )$be the greatest common divisor of integers a and b. Finally,$[ a , b ]$will denote the closed interval on the real line with endpoints$a$and$^ { b , }$except for in Section 5 where it will denote the least common multiple of integers a and b instead.

## 4. Outline of the proof

We will find it convenient to choose our weights$w _ { n }$to be zero unless n lies in a fixed residue class$\nu _ { 0 }$(mod W), where$\begin{array} { r } { W = \prod _ { p \leq D _ { 0 } } p } \end{array}$. This is a technical modification which removes some minor complications in dealing with the efect of small prime factors. The precise choice of $D _ { 0 }$is unimportant, but it will sufice to choose

$$
D _ {0} = \log \log \log N,\tag{4.1}
$$

so certainly$W \ll ( \log \log N ) ^ { 2 }$by the prime number theorem. By the Chinese remainder theorem, we can choose$\nu _ { 0 }$such that$\nu _ { 0 } + h _ { i }$is coprime to W for each i since H is admissible. When$n \equiv \nu _ { 0 }$(mod W), we choose our weights$w _ { n }$of the form (2.4). We now wish to estimate the sums

(4.2)

$$
S_{1} = \sum_{\substack{N\leq n <   2N\\ n\equiv v_{0}\pmod {W}}}\left(\sum_{d_{i}|n + h_{i}\forall i}\lambda_{d_{1},\ldots ,d_{k}}\right)^{2},\tag{4.3}
$$

$$
S_{2} = \sum_{\substack{N\leq n <   2N\\ n\equiv v_{0}\pmod{W}}}\Bigl (\sum_{i = 1}^{k}\chi_{\mathbb{P}}(n + h_{i})\Bigr)\Biggl (\sum_{d_{i}|n + h_{i}\forall i}\lambda_{d_{1},\ldots ,d_{k}}\Biggr)^{2}.
$$

We evaluate these sums using the following proposition.

Proposition 4.1. Let the primes have exponent of distribution$\theta > 0 _ { : }$, and let$R = N ^ { \theta / 2 - \delta }$for some smallfixed$\delta > 0$. Let$\lambda _ { d _ { 1 } , \dots , d _ { k } }$be defined in terms ofafixed smoothfunction F by

$$
\lambda_{d_{1},\ldots ,d_{k}} = \Bigl (\prod_{i = 1}^{k}\mu (d_{i})d_{i}\Bigr)\sum_{\substack{r_{1},\ldots ,r_{k}\\ d_{i}|r_{i}\forall i\\ (r_{i},W) = 1\forall i}}\frac{\mu(\prod_{i = 1}^{k}r_{i})^{2}}{\prod_{i = 1}^{k}\varphi(r_{i})} F\left(\frac{\log r_{1}}{\log R},\ldots ,\frac{\log r_{k}}{\log R}\right),
$$

whenever$\textstyle ( \prod _ { i = 1 } ^ { k } d _ { i } , W ) = 1$, and let$\lambda _ { d _ { 1 } , . . . , d _ { k } } = 0$otherwise. Moreover, let F be supported on $\begin{array} { r } { \mathcal { R } _ { k } = \{ ( x _ { 1 } , \dotsc , x _ { k } ) \in [ 0 , 1 ] ^ { k } : \sum _ { i = 1 } ^ { k } x _ { i } \leq 1 \} } \end{array}$. Then we have

$$
S _ {1} = \frac {(1 + o (1)) \varphi (W) ^ {k} N (\log R) ^ {k}}{W ^ {k + 1}} I _ {k} (F),
$$

$$
S _ {2} = \frac {(1 + o (1)) \varphi (W) ^ {k} N (\log R) ^ {k + 1}}{W ^ {k + 1} \log N} \sum_ {m = 1} ^ {k} J _ {k} ^ {(m)} (F),
$$

provided$I _ { k } ( F ) \neq 0$and$J _ { k } ^ { ( m ) } ( F ) \neq 0$for each m, where

$$
I _ {k} (F) = \int_ {0} ^ {1} \dots \int_ {0} ^ {1} F (t _ {1}, \ldots , t _ {k}) ^ {2} d t _ {1} \ldots d t _ {k},
$$

$$
J _ {k} ^ {(m)} (F) = \int_ {0} ^ {1} \dots \int_ {0} ^ {1} \left(\int_ {0} ^ {1} F (t _ {1}, \ldots , t _ {k}) d t _ {m}\right) ^ {2} d t _ {1} \ldots d t _ {m - 1} d t _ {m + 1} \ldots d t _ {k}.
$$

We recall that if$S _ { 2 }$is large compared to$S _ { 1 } .$, then using the GPY method we can show that there are infinitely many integers n such that several of the$n + h _ { i }$are prime. The following proposition makes this precise.

Proposition 4.2. Let the primes have level of distribution$\theta \ > \ 0 .$. Let$\delta \ > \ 0$and$\mathcal { H } =$ $\{ h _ { 1 } , \ldots , h _ { k } \}$be an admissible set. Let$I _ { k } ( F )$and$J _ { k } ^ { ( m ) } ( F )$be given as in Proposition 4.1, and let$S _ { k }$denote the set of Riemann-integrable functions${ \cal F } : [ 0 , 1 ] ^ { k }$R supported on $\begin{array} { r } { \mathcal { R } _ { k } = \{ ( x _ { 1 } , \dotsc , x _ { k } ) \in [ 0 , 1 ] ^ { k } : \sum _ { i = 1 } ^ { k } x _ { i } \leq 1 \} } \end{array}$with$I _ { k } ( F ) \neq 0$and$J _ { k } ^ { ( m ) } ( F ) \neq 0 .$for each m. Let

$$
M _ {k} = \sup _ {F \in \mathcal {S} _ {k}} \frac {\sum_ {m = 1} ^ {k} J _ {k} ^ {(m)} (F)}{I _ {k} (F)}, \quad r _ {k} = \left\lceil \frac {\theta M _ {k}}{2} \right\rceil .
$$

Then there are infinitely many integers n such that at least$r _ { k }$of the$n + h _ { i } ( 1 \leq i \leq k )$are prime. In particular, lim in$\begin{array} { r } { \mathrm { f } _ { n } ( p _ { n + r _ { k } - 1 } - p _ { n } ) \leq \operatorname* { m a x } _ { 1 \leq i , j \leq k } ( h _ { i } - h _ { j } ) } \end{array}$

ProofofProposition 4.2. We let$S = S _ { 2 } - \rho S _ { 1 }$, and recall that from Section 2 that if we can show$S > 0$for all large N, then there are infinitely many integers n such that at least$\lfloor \rho + 1 \rfloor$ of the$n + h _ { i }$are prime.

We put$R = N ^ { \bar { \theta } / 2 - \delta }$for a small$\delta > 0$. By the definition of$M _ { k } .$, we can choose$F _ { 0 } \in S _ { k }$such that$\begin{array} { r } { \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F _ { 0 } ) > ( M _ { k } - \delta ) I _ { k } ( F _ { 0 } ) > 0 } \end{array}$. Since$F _ { 0 }$is Riemann-integrable, there is a smooth function$F _ { 1 }$such that$\begin{array} { r } { \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F _ { 1 } ) > ( M _ { k } - 2 \delta ) I _ { k } ( F _ { 1 } ) > 0 } \end{array}$. Using Proposition 4.1, we can then choose$\lambda _ { d _ { 1 } , \dots , d _ { k } }$such that

$$
\begin{array}{l} S = \frac {\varphi (W) ^ {k} N (\log R) ^ {k}}{W ^ {k + 1}} \Big (\frac {\log R}{\log N} \sum_ {j = 1} ^ {k} J _ {k} ^ {(m)} (F _ {1}) - \rho I _ {k} (F _ {1}) + o (1) \Big) \\ \geq \frac {\varphi (W) ^ {k} N (\log R) ^ {k} I _ {k} (F _ {1})}{W ^ {k + 1}} \Big (\Big (\frac {\theta}{2} - \delta \Big) \Big (M _ {k} - 2 \delta \Big) - \rho + o (1) \Big). \end{array}\tag{4.4}
$$

If$\rho = \theta M _ { k } / 2 - \epsilon$then, by choosing δ suitably small (depending on$\epsilon )$, we see that$S > 0$for all large N. Thus there are infinitely many integers n for which at least$\lfloor \rho + 1 \rfloor$of the$n + h _ { i }$ are prime. Since$\lfloor \rho + 1 \rfloor = \lceil \theta M _ { k } / 2 \rceil$if ǫ is suitably small, we obtain Proposition 4.2.

Thus, if the primes have a fixed level of distribution θ, to show the existence of many of the $n + h _ { i }$being prime for infinitely many$n \in \mathbb { N }$we only require a suitable lower bound for$M _ { k }$ The following proposition establishes such a bound for diferent values of k.

Proposition 4.3. Let$k \in \mathbb { N } ,$, and M<sub>k</sub> be as given by Proposition 4.2. Then

(1) We have$M _ { 5 } > 2 .$

(2) We have${ M } _ { 1 0 5 } > 4 .$

(3) If k is suficiently large, we have$M _ { k } > \log k - 2 \log \log k - 2$

We now prove Theorems 1.1, 1.2, 1.3 and 1.4 from Propositions 4.2 and 4.3.

First we consider Theorem 1.3. We take$k = 1 0 5$. By Proposition 4.3, we have$M _ { 1 0 5 } > 4 .$ By the Bombieri-Vinogradov theorem, the primes have level of distribution$\theta = 1 / 2 - \epsilon$for every$\epsilon > 0$. Thus, if we take ǫ suficiently small, we have$\theta M _ { 1 0 5 } / 2 > 1$. Therefore, by Proposition 4.2, we have lim inf$\begin{array} { r } { ( p _ { n + 1 } - p _ { n } ) \le \operatorname* { m a x } _ { 1 \le i , j \le 1 0 5 } ( h _ { i } - h _ { j } ) } \end{array}$for any admissible set $\mathcal { H } = \{ h _ { 1 } , . . . , h _ { 1 0 5 } \}$. By computations performed by Thomas Engelsma (unpublished), we can choose<sup>2</sup> H such that$0 \leq h _ { 1 } < . . . < h _ { 1 0 5 }$and$h _ { 1 0 5 } - h _ { 1 } = 6 0 0$. This gives Theorem 1.3.

If we assume the Elliott-Halberstam conjecture then the primes have level of distribution $\theta = 1 - \epsilon$. First we take$k = 1 0 5$, and see that$\theta M _ { 1 0 5 } / 2 > 2$for ǫ suficiently small (since $M _ { 1 0 5 } > 4 )$. Therefore, by Proposition 4.2, lim$\begin{array} { r } { \operatorname* { i n f } _ { n } ( p _ { n + 2 } - p _ { n } ) \le \operatorname* { m a x } _ { 1 \le i , j \le 1 0 5 } ( h _ { i } - h _ { j } ) } \end{array}$. Thus, choosing the same admissible set H as above, we see lim$\mathrm { i n f } _ { n } ( p _ { n + 2 } - p _ { n } ) \leq 6 0 0$under the Elliott-Halberstam conjecture.

Next we take$k = 5$and$\mathcal { H } = \{ 0 , 2 , 6 , 8 , 1 2 \}$, with$\theta = 1 - \epsilon$again. By Proposition 4.3 we have$M _ { 5 } ~ > ~ 2$, and so$\theta M _ { 5 } / 2 > 1$for ǫ suficiently small. Thus, by Proposition 4.2, lim in$\mathrm { f } _ { n } ( p _ { n + 1 } - p _ { n } ) \leq 1 2$under the Elliott-Halberstam conjecture. This completes the proof of Theorem 1.4.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Explicitly, we can take H = {0, 10, 12, 24, 28, 30, 34, 42, 48, 52, 54, 64, 70, 72, 78, 82, 90, 94, 100, 112, 114, 118, 120, 124, 132, 138, 148, 154, 168, 174, 178, 180, 184, 190, 192, 202, 204, 208, 220, 222, 232, 234, 250, 252, 258, 262, 264, 268, 280, 288, 294, 300, 310, 322, 324, 328, 330, 334, 342, 352, 358, 360, 364, 372, 378, 384, 390, 394, 400, 402, 408, 412, 418, 420, 430, 432, 442, 444, 450, 454, 462, 468, 472, 478, 484, 490, 492, 498, 504, 510, 528, 532, 534, 538, 544, 558, 562, 570, 574, 580, 582, 588, 594, 598, 600}. This set was obtained from the website http://math.mit.edu/<sub>˜</sub>primegaps/ maintained by Andrew Sutherland.</span></small>

Finally, we consider the case when k is large. For the rest of this section, any constants implied by asymptotic notation will be independent of k. By the Bombieri-Vinogradov theorem, we can take$\theta = 1 / 2 - \epsilon$. Thus, by Proposition 4.3, we have for k suficiently large

$$
\frac {\theta M _ {k}}{2} \geq \Bigl (\frac {1}{4} - \frac {\epsilon}{2} \Bigr) \Bigl (\log k - 2 \log \log k - 2 \Bigr).\tag{4.5}
$$

We choose$\epsilon = 1 / k$, and see that$\theta M _ { k } / 2 > m { \mathrm { ~ i f ~ } } k \geq C m ^ { 2 } e ^ { 4 m }$for some absolute constant C (independent of m and$k )$. Thus, for any admissible set$\mathcal { H } = \{ h _ { 1 } , . . . , h _ { k } \}$with$k \geq C m ^ { 2 } e ^ { 4 m }$ at least$m + 1$of the$n + h _ { i }$must be prime for infinitely many integers n. We can choose our set$\mathcal { H }$to be the set$\{ p _ { \pi ( k ) + 1 } , \ldots , p _ { \pi ( k ) + k } \}$of the first k primes which are greater than$k .$ This is admissible, since no element is a multiple of a prime less than k (and there are k elements, so it cannot cover all residue classes modulo any prime greater than k.) This set has diameter$p _ { \pi ( k ) + k } - p _ { \pi ( k ) + 1 } \ll k \log k$. Thus lim inf$\phantom { } _ { \ i } ( p _ { n + m } - p _ { n } ) \ll k \log k \ll m ^ { 3 } e ^ { 4 m }$if we take $k = \lceil C m ^ { 2 } e ^ { 4 m } \rceil$. This gives Theorem 1.1.

We can now establish Theorem 1.2 by a simple counting argument. Given m, we let $k = \lceil C m ^ { 2 } e ^ { 4 m } \rceil$as above. Therefore if$\{ h _ { 1 } , \ldots , h _ { k } \}$is admissible, then there exists a subset $\{ h _ { 1 } ^ { \prime } , \ldots , h _ { m } ^ { \prime } \} \subseteq \{ h _ { 1 } , \ldots , h _ { k } \}$with the property that there are infinitely many integers n for which all of the$n + h _ { i } ^ { \prime }$are prime$( 1 \leq i \leq m )$

We let$\mathcal { A } _ { 2 }$denote the set formed by starting with the given set$\mathcal { A } = \{ a _ { 1 } , \ldots \ldots , a _ { r } \}$, and for each prime$p \leq k$in turn removing all elements of the residue class modulo$p$which contains the fewest integers. We see that$\begin{array} { r } { \# \mathcal { A } _ { 2 } \geq r \prod _ { p \leq k } ( 1 - 1 / p ) \gg _ { m } r . } \end{array}$. Moreover, any subset of$\mathcal { A } _ { 2 }$ of size k must be admissible, since it cannot cover all residue classes modulo$p$for any prime $p \leq k$. We let$s = \# \mathcal { R } _ { 2 }$, and since r is taken suficiently large in terms of$m ,$, we may assume that$s > k$

We see there are$\binom { s } { k }$sets$\mathcal { H } \subseteq \mathcal { A } _ { 2 }$of size k. Each of these is admissible, and so contains at least one subset$\{ \dot { h } _ { 1 } ^ { \prime } , \ldots , h _ { m } ^ { \prime } \} \subseteq \mathcal { A } _ { 2 }$which satisfies the prime m-tuples conjecture. Any admissible set$\mathcal { B } \subseteq \mathcal { A } _ { 2 }$of size m is contained in$\binom { s - m } { k - m }$sets$\mathcal { H } \subseteq \mathcal { A } _ { 2 }$of size k. Thus there are at least${ \binom { s } { k } } { \binom { s - m } { k - m } } ^ { - 1 } \gg _ { m } s ^ { m } \gg _ { m } r ^ { m }$admissible sets$\mathcal { B } \subseteq \mathcal { A } _ { 2 }$of size m which satisfy the prime m-tuples conjecture. Since there are${ \binom { r } { m } } \leq r ^ { m }$sets$\{ h _ { 1 } , \ldots , h _ { m } \} \subseteq { \mathcal { A } }$, Theorem 1.2 holds.

We are left to establish Propositions 4.1 and 4.3.

## 5. Selberg sieve manipulations

In this section we perform initial manipulations towards establishing Proposition 4.1. These arguments are multidimensional generalizations of the sieve arguments of [3]. In particular, our approach is based on the elementary combinatorial ideas of Selberg. The aim is to introduce a change of variables to rewrite our sums$S _ { 1 }$and$S _ { 2 }$in a simpler form.

Throughout the rest of the paper we assume that the primes have a fixed level of distribution $\theta ,$and$R \overset { \cdot } { = } N ^ { \theta / 2 - \delta }$. We restrict the support of$\lambda _ { d _ { 1 } , \dots , d _ { k } }$to tuples for which the product$\begin{array} { r } { d = \prod _ { i = 1 } ^ { k } d _ { i } } \end{array}$ is less than R and also satisfies$( d , W ) = 1$and$\mu ( d ) ^ { 2 } = 1$. We note that the condition$\mu ( d ) ^ { 2 } = 1$ implies that$( d _ { i } , d _ { j } ) = 1$for all$i \neq j$

Lemma 5.1. Let

$$
y_{r_{1},\ldots ,r_{k}} = \Bigl (\prod_{i = 1}^{k}\mu (r_{i})\varphi (r_{i})\Bigr)\sum_{\substack{d_{1},\ldots ,d_{k}\\ r_{i}|d_{i}\forall i}}\frac{\lambda_{d_{1},\ldots,d_{k}}}{\prod_{i = 1}^{k}d_{i}}.
$$

Let$\begin{array} { r } { y _ { m a x } = \operatorname* { s u p } _ { r _ { 1 } , . . . , r _ { k } } | y _ { r _ { 1 } , . . . , r _ { k } } | . } \end{array}$Then

$$
S _ {1} = \frac {N}{W} \sum_ {r _ {1}, \ldots , r _ {k}} \frac {y _ {r _ {1} , \ldots , r _ {k}} ^ {2}}{\prod_ {i = 1} ^ {k} \varphi (r _ {i})} + O \Big (\frac {y _ {m a x} ^ {2} \varphi (W) ^ {k} N (\log R) ^ {k}}{W ^ {k + 1} D _ {0}} \Big).
$$

Proof. We expand out the square, and swap the order of summation to give

$$
S_{1} = \sum_{\substack{N\leq n <   2N\\ n\equiv v_{0}\pmod{W}}}\Big(\sum_{d_{i}|n + h_{i}\forall i}\lambda_{d_{1},\ldots ,d_{k}}\Big)^{2} = \sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}}}\lambda_{d_{1},\ldots ,d_{k}}\lambda_{e_{1},\ldots ,e_{k}}\sum_{\substack{N\leq n <   2N\\ n\equiv v_{0}\pmod{W}\\ [d_{i},e_{i}]|n + h_{i}\forall i}}1.\tag{5.1}
$$

We recall that here, and throughout this section, we are using [a, b] to denote the least common multiple of a and$b .$

By the Chinese remainder theorem, the inner sum can be written as a sum over a single residue class modulo$\begin{array} { r } { q = W \prod _ { i = 1 } ^ { k } [ d _ { i } , e _ { i } ] . } \end{array}$, provided that the integers$W , [ d _ { 1 } , e _ { 1 } ] , \dots , [ d _ { k } , e _ { k } ]$are pairwise coprime. In this case the inner sum is$N / q + O ( 1 )$. If the integers are not pairwise coprime then the inner sum is empty. This gives

$$
S_{1} = \frac{N}{W}\sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}}}^{\prime}\frac{\lambda_{d_{1},\ldots,d_{k}}\lambda_{e_{1},\ldots,e_{k}}}{\prod_{i = 1}^{k}[d_{i},e_{i}]} +O\Big(\sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}}}^{\prime}|\lambda_{d_{1},\ldots ,d_{k}}\lambda_{e_{1},\ldots ,e_{k}}|\Big),\tag{5.2}
$$

where$\sum ^ { \prime }$is used to denote the restriction that we require W,$[ d _ { 1 } , e _ { 1 } ] , \ldots , [ d _ { k } , e _ { k } ]$to be pairwise coprime. To ease notation we will put$\lambda _ { m a x } = \operatorname* { s u p } _ { d _ { 1 } , \dots , d _ { k } } | \lambda _ { d _ { 1 } , \dots , d _ { k } } |$. We now see that since$\lambda _ { d _ { 1 } , \dots , d _ { k } }$ is non-zero only when$\textstyle \prod _ { i = 1 } ^ { k } d _ { i } < R$, the error term contributes

$$
\ll \lambda_ {m a x} ^ {2} \bigl (\sum_ {d <   R} \tau_ {k} (d) \bigr) ^ {2} \ll \lambda_ {m a x} ^ {2} R ^ {2} (\log R) ^ {2 k},\tag{5.3}
$$

which will be negligible.

In the main sum we wish to remove the dependencies between the$d _ { i }$and the$e _ { j }$variables. We use the identity

$$
\frac {1}{[ d _ {i} , e _ {i} ]} = \frac {1}{d _ {i} e _ {i}} \sum_ {u _ {i} | d _ {i}, e _ {i}} \varphi (u _ {i})\tag{5.4}
$$

to rewrite the main term as

$$
\frac{N}{W}\sum_{u_{1},\ldots ,u_{k}}\Bigl (\prod_{i = 1}^{k}\varphi (u_{i})\Bigr)\sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}\\ u_{i}|d_{i},e_{i}\forall i}}^{\prime}\frac{\lambda_{d_{1},\ldots,d_{k}}\lambda_{e_{1},\ldots,e_{k}}}{(\prod_{i = 1}^{k}d_{i})(\prod_{i = 1}^{k}e_{i})}.\tag{5.5}
$$

We recall that$\lambda _ { d _ { 1 } , \dots , d _ { k } }$is supported on integers$d _ { 1 } , \ldots , d _ { k }$with$( d _ { i } , W ) ~ = ~ 1$for each i and $( d _ { i } , d _ { j } ) = 1$for all$i \neq j .$Thus we may drop the requirement that W is coprime to each of the$[ d _ { i } , e _ { i } ]$from the summation, since these terms have no contribution. Similarly, we may drop the requirement that the$d _ { i }$variables are all pairwise coprime, and the requirement that the$e _ { i }$variables are all pairwise coprime. Thus the only remaining restriction coming from the pairwise coprimality of$W , [ d _ { 1 } , e _ { 1 } ] , \dots , [ d _ { k } , e _ { k } ]$is that$( d _ { i } , e _ { j } ) = 1$for all$i \neq j$

We can remove the requirement that$( d _ { i } , e _ { j } ) = 1$by multiplying our expression by$\textstyle \sum _ { s _ { i , j } \mid d _ { i } , e _ { j } } \mu ( s _ { i , j } )$ We do this for all$i , j$with$i \neq j .$. This transforms the main term to

$$
\frac{N}{W}\sum_{u_{1},\ldots ,u_{k}}\Bigl (\prod_{i = 1}^{k}\varphi (u_{i})\Bigr)\sum_{s_{1,2},\ldots ,s_{k,k - 1}}\bigl (\prod_{\substack{1\leq i,j\leq k\\ i\neq j}}\mu (s_{i,j})\bigr)\sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}\\ u_{i}|d_{i},e_{i}\forall i\\ s_{i,j}|d_{i},e_{j}\forall i\neq j}}\frac{\lambda_{d_{1},\ldots,d_{k}}\lambda_{e_{1},\ldots,e_{k}}}{(\prod_{i = 1}^{k}d_{i})(\prod_{i = 1}^{k}e_{i})}.\tag{5.6}
$$

We can restrict the$s _ { i , j }$to be coprime to$u _ { i }$and$u _ { j }$, because terms with$s _ { i , j }$not coprime to$u _ { i }$or $u _ { j }$make no contribution to our sum. This is because$\lambda _ { d _ { 1 } , . . . , d _ { k } } = 0$unless$( d _ { i } , d _ { j } ) = 1$. Similarly we can further restrict our sum so that$s _ { i , j }$is coprime to$s _ { i , a }$and$s _ { b , j }$for all$a \neq j$and$b \neq i$. We denote the summation over$s _ { 1 , 2 } , \ldots , s _ { k , k - 1 }$with these restrictions by$\Sigma ^ { * }$

We now introduce a change of variables to make the estimation of the sum more straightforward. We let

$$
y_{r_{1},\ldots ,r_{k}} = \Bigl (\prod_{i = 1}^{k}\mu (r_{i})\varphi (r_{i})\Bigr)\sum_{\substack{d_{1},\ldots ,d_{k}\\ r_{i}|d_{i}\forall i}}\frac{\lambda_{d_{1},\ldots,d_{k}}}{\prod_{i = 1}^{k}d_{i}}.\tag{5.7}
$$

This change is invertible. For$d _ { 1 } , \ldots , d _ { k }$with$\textstyle \prod _ { i = 1 } ^ { k } d _ { i }$square-free we find that

$$
\begin{array}{c}\sum_{\substack{r_{1},\ldots ,r_{k}\\ d_{i}|r_{i}\forall i}}\frac{y_{r_{1},\ldots,r_{k}}}{\prod_{i = 1}^{k}\varphi(r_{i})} = \sum_{\substack{r_{1},\ldots ,r_{k}\\ d_{i}|r_{i}\forall i}}\Bigl (\prod_{i = 1}^{k}\mu (r_{i})\Bigr)\sum_{\substack{e_{1},\ldots ,e_{k}\\ r_{i}|e_{i}\forall i}}\frac{\lambda_{e_{1},\ldots,e_{k}}}{\prod_{i = 1}^{k}e_{i}}\\ \\ = \sum_{e_{1},\ldots ,e_{k}}\frac{\lambda_{e_{1},\ldots,e_{k}}}{\prod_{i = 1}^{k}e_{i}}\sum_{\substack{r_{1},\ldots ,r_{k}\\ d_{i}|r_{i}\forall i\\ r_{i}|e_{i}\forall i}}\prod_{i = 1}^{k}\mu (r_{i}) = \frac{\lambda_{d_{1},\ldots,d _{k}}}{\prod_{i = 1}^{k}\mu_{i}(d_{i})d_{i}}. \end{array}\tag{5.8}
$$

Thus any choice of$y _ { r _ { 1 } , \ldots , r _ { k } }$supported on$r _ { 1 } , \ldots , r _ { k }$, with the product$\begin{array} { r } { r = \prod _ { i = 1 } ^ { k } r _ { i } } \end{array}$square-free and satisfying$r \textless R$and$( r , W ) = 1$, will give a suitable choice of$\lambda _ { d _ { 1 } , \dots , d _ { k } }$. We let$y _ { m a x } =$ $\mathbf { s u p } _ { r _ { 1 } , . . . , r _ { k } } | y _ { r _ { 1 } , . . . , r _ { k } } |$. Now, since$\begin{array} { r } { d / \varphi ( d ) = \sum _ { e | d } 1 / \varphi ( e ) } \end{array}$for square-free$d ,$we find by taking$r ^ { \prime } =$ $\textstyle \prod _ { i = 1 } ^ { k } r _ { i } / d _ { i }$that

$$
\begin{aligned} \lambda_{max} & \leq \sup_{\substack{d_{1},\ldots ,d_{k}\\ \prod_{i = 1}^{k}d_{i}\text{square - free}}}y_{max}\Bigl (\prod_{i = 1}^{k}d_{i}\Bigr)\sum_{\substack{r_{1},\ldots ,r_{k}\\ d_{i}|r_{i}\forall i\\ \prod_{i = 1}^{k}r_{i} <   R\\ \prod_{i = 1}^{k}r_{i}\text{square - free}}}\Bigl (\prod_{i = 1}^{k}\frac{\mu(r_{i})^{2}}{\varphi(r_{i})}\Bigr) \\ & \leq y_{max}\sup_{\substack{d_{1},\ldots ,d_{k}\\ \prod_{i = 1}^{k}d_{i}\text{square - free}}}\Bigl (\prod_{i = 1}^{k}\frac{d_{i}}{\varphi(d_{i})}\Bigr)\sum_{\substack{r^{\prime} <   R / \prod_{i = 1}^{k}d_{i}\\ (r^{\prime},\prod_{i = 1}^{k}d_{i}) = 1}}\frac{\mu(r^{\prime})^{2}\tau_{k}(r^{\prime})}{\varphi(r^{\prime})}\\ & \leq y_{max}\sup_{d_{1},\ldots ,d_{k}}\sum_{d|\prod_{i = 1}^{k}d_{i}}\frac{\mu(d)^{2}}{\varphi(d)}\sum_{\substack{r^{\prime} <   R / \prod_{i = 1}^{k}d_{i}\\ (r^{\prime},\prod_{i = 1}^{k}d_{i}) = 1}}\frac{\mu(r^{\prime})^{2}\tau_{k}(r^{\prime})}{\varphi(r^{\prime})}\\ & \leq y_{max}\sum_{u <   R}\frac{\mu(u)^{2}\tau_{k}(u)}{\varphi(u)}\ll y_{max}(\log R)^{k}. \end{aligned}\tag{5.9}
$$

In the last line we have taken$u = d r ^ { \prime }$, and used the fact$\tau _ { k } ( d \boldsymbol { r } ^ { \prime } ) \geq \tau _ { k } ( \boldsymbol { r } ^ { \prime } )$. Hence the error term $O ( \lambda _ { m a x } ^ { 2 } R ^ { 2 } ( \log N ) ^ { 2 k } )$is of size$O ( y _ { m a x } ^ { 2 } R ^ { 2 } ( \log N ) ^ { 4 k } )$

Substituting our change of variables (5.7) into the main term (5.6), and using the above estimate for the error term, we obtain

$$
S_{1} = \frac{N}{W}\sum_{u_{1},\ldots ,u_{k}}\Bigl (\prod_{i = 1}^{k}\varphi (u_{i})\Bigr)\sum_{s_{1,2},\ldots ,s_{k,k - 1}}^{*}\bigl (\prod_{\substack{1\leq i,j\leq k\\ i\neq j}}\mu (s_{i,j})\bigr)\Bigl (\prod_{i = 1}^{k}\frac{\mu(a_{i})\mu(b_{i})}{\varphi(a_{i})\varphi(b_{i})}\Bigr)y_{a_{1},\ldots ,a_{k}}y_{b_{1},\ldots ,b_{k}}\tag{5.10}
$$

$$
+ O \left(y _ {\max} ^ {2} R ^ {2} (\log R) ^ {4 k}\right),
$$

where$\begin{array} { r } { a _ { j } = u _ { j } \prod _ { i \neq j } s _ { j , i } } \end{array}$and$\begin{array} { r } { b _ { j } = u _ { j } \prod _ { i \neq j } s _ { i , j } } \end{array}$. In these expressions we have used the fact that we have restricted$s _ { i , j }$to be coprime to the other terms in the expression for$a _ { i }$and$b _ { j }$. For the same reason we may rewrite$\mu ( a _ { j } )$as$\begin{array} { r } { \mu ( u _ { j } ) \prod _ { i \neq j } \mu ( s _ { i , j } ) } \end{array}$, and similarly for$\varphi ( a _ { j } ) , \mu ( b _ { j } )$and $\varphi ( b _ { j } )$. This gives us

$$
S_{1} = \frac{N}{W}\sum_{u_{1},\ldots ,u_{k}}\Bigl (\prod_{i = 1}^{k}\frac{\mu(u_{i})^{2}}{\varphi(u_{i})}\Bigr)\sum_{s_{1,2},\ldots ,s_{k,k - 1}}^{*}\Bigl (\prod_{\substack{1\leq i,j\leq k\\ i\neq j}}\frac{\mu(s_{i,j})}{\varphi(s_{i,j})^{2}}\Bigr)y_{a_{1},\ldots ,a_{k}}y_{b_{1},\ldots ,b_{k}} + O\Bigl (y_{max}^{2}R^{2}(\log R)^{4k}\Bigr).\tag{5.11}
$$

We see that there is no contribution from$s _ { i , j }$with$( s _ { i , j } , W ) ~ \neq ~ 1$because of the restricted support of y. Thus we only need to consider$s _ { i , j } = 1$or$s _ { i , j } > D _ { 0 }$. The contribution when $s _ { i , j } > D _ { 0 }$is

$$
\ll \frac{y_{max}^{2}N}{W}\Big(\sum_{\substack{u <   R\\ (u,W) = 1}}\frac{\mu(u)^{2}}{\varphi(u)}\Big)^{k}\Big(\sum_{s_{i,j} > D_{0}}\frac{\mu(s_{i,j})^{2}}{\varphi(s_{i,j})^{2}}\Big)\Big(\sum_{s\geq 1}\frac{\mu(s)^{2}}{\varphi(s)^{2}}\Big)^{k^{2} - k - 1}\ll \frac{y_{max}^{2}\varphi(W)^{k}N(\log R)^{k}}{W^{k + 1}D_{0}}.\tag{5.12}
$$

Thus we may restrict our attention to the case when$s _ { i , j } = 1 \forall i \neq j .$This gives

$$
S _ {1} = \frac {N}{W} \sum_ {u _ {1}, \ldots , u _ {k}} \frac {y _ {u _ {1} , \ldots , u _ {k}} ^ {2}}{\prod_ {i = 1} ^ {k} \varphi (u _ {i})} + O \left(\frac {y _ {m a x} ^ {2} \varphi (W) ^ {k} N (\log R) ^ {k}}{W ^ {k + 1} D _ {0}} + y _ {m a x} ^ {2} R ^ {2} (\log R) ^ {4 k}\right).\tag{5.13}
$$

We recall that$R ^ { 2 } = N ^ { \theta - 2 \delta } \leq N ^ { 1 - 2 \delta }$and$W \ll N ^ { \delta }$, and so the first error term dominates. This gives the result.

We now consider$S _ { 2 }$. We write$\begin{array} { r } { S _ { 2 } = \sum _ { m = 1 } ^ { k } S _ { 2 } ^ { ( m ) } } \end{array}$, where

$$
S_{2}^{(m)} = \sum_{\substack{N\leq n <   2N\\ n\equiv v_{0}\pmod{W}}}\chi_{\mathbb{P}}(n + h_{m})\Big(\sum_{\substack{d_{1},\ldots ,d_{k}\\ d_{i}|n + h_{i}\forall i}}\lambda_{d_{1},\ldots ,d_{k}}\Big)^{2}.\tag{5.14}
$$

We now estimate${ S } _ { 2 } ^ { ( m ) }$in a similar way to our treatment of$S _ { 1 }$.

Lemma 5.2. Let

$$
y^{(m)}_{r_{1},\ldots ,r_{k}} = \Bigl (\prod_{i = 1}^{k}\mu (r_{i})g(r_{i})\Bigr)\sum_{\substack{d_{1},\ldots ,d_{k}\\ r_{i}|d_{i}\forall i\\ d_{m} = 1}}\frac{\lambda_{d_{1},\ldots,d_{k}}}{\prod_{i = 1}^{k}\varphi(d_{i})},
$$

where g is the totally multiplicative function defined on primes by$g ( p ) = p - 2$. Let$y _ { m a x } ^ { ( m ) } =$ $\begin{array} { r } { \operatorname* { s u p } _ { r _ { 1 } , \ldots , r _ { k } } | y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) } | . } \end{array}$. Then for any fixed$A > 0$we have

$$
S _ {2} ^ {(m)} = \frac {N}{\varphi (W) \log N} \sum_ {r _ {1}, \dots , r _ {k}} \frac {(y _ {r _ {1} , \dots , r _ {k}} ^ {(m)}) ^ {2}}{\prod_ {i = 1} ^ {k} g (r _ {i})} + O \left(\frac {(y _ {\max} ^ {(m)}) ^ {2} \varphi (W) ^ {k - 2} N (\log N) ^ {k - 2}}{W ^ {k - 1} D _ {0}}\right) + O \left(\frac {y _ {\max} ^ {2} N}{(\log N) ^ {A}}\right).
$$

Proof. We first expand out the square and swap the order of summation to give

$$
S_{2}^{(m)} = \sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}}}\lambda_{d_{1},\ldots ,d_{k}}\lambda_{e_{1},\ldots ,e_{k}}\sum_{\substack{N\leq n <   2N\\ n\equiv \nu_{0}\pmod {W}\\ [d_{i},e_{i}]]n + h_{i}\forall i}}\chi_{\mathbb{P}}(n + h_{m}).\tag{5.15}
$$

As with$S _ { 1 }$, the inner sum can be written as a sum over a single residue class modulo$q =$ $\textstyle W \prod _ { i = 1 } ^ { k } [ d _ { i } , e _ { i } ]$, provided that W,$[ d _ { 1 } , e _ { 1 } ] , \ldots , [ d _ { k } , e _ { k } ]$are pairwise coprime. The integer$n + { \boldsymbol { h } } _ { m }$ will lie in a residue class coprime to the modulus if and only if$d _ { m } = e _ { m } = 1$. In this case the inner sum will contribute$X _ { N } / \varphi ( q ) + { \cal O } ( E ( N , q ) )$, where

(5.16)

$$
\begin{array}{l}E(N,q) = 1 + \sup_{(a,q) = 1}\bigg|\sum_{\substack{N\leq n <   2N\\ n\equiv a\pmod{q}}}\chi_{\mathbb{P}}(n) - \frac{1}{\varphi(q)}\sum_{N\leq n <   2N}\chi_{\mathbb{P}}(n)\bigg|,\\ X_{N} = \sum_{N\leq n <   2N}\chi_{\mathbb{P}}(n). \end{array}\tag{5.17}
$$

If either one pair of$W , [ d _ { 1 } , e _ { 1 } ] , \dots , [ d _ { k } , e _ { k } ]$share a common factor, or if either$d _ { m }$or$e _ { m }$are not 1, then the contribution of the inner sum is zero. Thus we obtain

$$
S_{2}^{(m)} = \frac{X_{N}}{\varphi(W)}\sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}\\ e_{m} = d_{m} = 1}}^{\prime}\frac{\lambda_{d_{1},\ldots,d_{k}}\lambda_{e_{1},\ldots,e_{k}}}{\prod_{i = 1}^{k}\varphi([d_{i},e_{i}])} +O\Big(\sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}}}|\lambda_{d_{1},\ldots ,d_{k}}\lambda_{e_{1},\ldots ,e_{k}}|E(N,q)\Big),\tag{5.18}
$$

where we have written$\begin{array} { r } { q = W \prod _ { i = 1 } ^ { k } [ d _ { i } , e _ { i } ] . } \end{array}$

Q<sub>We</sub> <sub>first</sub> <sub>deal</sub> <sub>with</sub> <sub>the</sub> <sub>contribution</sub> <sub>from</sub> <sub>the</sub> <sub>error</sub> <sub>terms.</sub> <sub>From</sub> <sub>the</sub> <sub>support</sub> <sub>of</sub>$\lambda _ { d _ { 1 } , \dots , d _ { k } }$, we see that we only need to consider square-free q with$q < R ^ { 2 } W$. Given a square-free integer$r ,$ there are at most$\tau _ { 3 k } ( r )$choices of$d _ { 1 } , \dotsc , d _ { k } , e _ { 1 } , \dotsc , e _ { k }$for which W$\textstyle \prod _ { i = 1 } ^ { k } [ d _ { i } , e _ { i } ] = r$. We also recall from (5.9) that$\lambda _ { m a x } \ll y _ { m a x } ( \log R ) ^ { k }$. Thus the error term contributes

$$
\ll y _ {m a x} ^ {2} (\log R) ^ {2 k} \sum_ {r <   R ^ {2} W} \mu (r) ^ {2} \tau_ {3 k} (r) E (N, r).\tag{5.19}
$$

By Cauchy-Schwarz, the trivial bound$E ( N , q ) \ll N / \varphi ( q )$, and our hypothesis that the primes have level of distribution θ, this contributes for any fixed$A > 0$

$$
\ll y _ {m a x} ^ {2} (\log R) ^ {2 k} \Bigl (\sum_ {r <   R ^ {2} W} \mu (r) ^ {2} \tau_ {3 k} ^ {2} (r) \frac {N}{\varphi (r)} \Bigr) ^ {1 / 2} \Bigl (\sum_ {r <   R ^ {2} W} \mu (r) ^ {2} E (N, r) \Bigr) ^ {1 / 2} \ll \frac {y _ {m a x} ^ {2} N}{(\log N) ^ {A}}.\tag{5.20}
$$

We now concentrate on the main sum. As in the treatment of$S _ { 1 }$in the proof of Lemma 5.1, we rewrite the conditions$( d _ { i } , e _ { j } ) = 1$by multiplying our expression by$\textstyle \sum _ { s _ { i , j } \mid d _ { i } , e _ { j } } \mu ( s _ { i , j } )$. Again we may restrict$s _ { i , j }$to be coprime to$u _ { i } , u _ { j } , s _ { i , a }$and$s _ { b , j }$for all$a \neq j$and$b \neq i .$. We denote the summation subject to these restrictions by$\sum ^ { * }$. We also split the$\varphi ( [ d _ { i } , e _ { i } ] )$terms by using the equation (valid for square-free$d _ { i } , e _ { i } )$

$$
\frac {1}{\varphi ([ d _ {i} , e _ {i} ])} = \frac {1}{\varphi (d _ {i}) \varphi (e _ {i})} \sum_ {u _ {i} | d _ {i}, e _ {i}} g (u _ {i}),\tag{5.21}
$$

where$g$is the totally multiplicative function defined on primes by$g ( p ) = p - 2$. This gives us a main term of

$$
\frac{X_{N}}{\varphi(W)}\sum_{u_{1},\ldots ,u_{k}}\Bigl (\prod_{i = 1}^{k}g(u_{i})\Bigr)\sum_{s_{1,2},\ldots ,s_{k,k - 1}}^{*}\bigl (\prod_{\substack{1\leq i,j\leq k\\ i\neq j}}\mu (s_{i,j})\bigr) \sum_{\substack{d_{1},\ldots ,d_{k}\\ e_{1},\ldots ,e_{k}\\ u_{i}|d_{i},e_{i}\forall i\\ s_{i,j}|d_{i},e_{j}\forall i\neq j\\ d_{m} = e_{m} = 1}}\frac{\lambda_{d_{1},\ldots,d_{k}}\lambda_{e_{1},\ldots,e_{k}}}{\prod_{i = 1}^{k}\varphi(d_{i})\varphi(e_{i})}.\tag{5.22}
$$

We have now separated the dependencies between the$e$and$d$variables, so again we make a substitution. We let

$$
y^{(m)}_{r_{1},\ldots ,r_{k}} = \Bigl (\prod_{i = 1}^{k}\mu (r_{i})g(r_{i})\Bigr)\sum_{\substack{d_{1},\ldots ,d_{k}\\ r_{i}|d_{i}\forall i\\ d_{m} = 1}}\frac{\lambda_{d_{1},\ldots,d_{k}}}{\prod_{i = 1}^{k}\varphi(d_{i})}.\tag{5.23}
$$

We note$y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) } = 0$unless$r _ { m } = 1$. Substituting this into (5.22), we obtain a main term of

$$
\frac{X_{N}}{\varphi(W)}\sum_{u_{1},\ldots ,u_{k}}\bigl (\prod_{i = 1}^{k}\frac{\mu(u_{i})^{2}}{g(u_{i})}\bigr)\sum_{s_{1,2},\ldots ,s_{k,k - 1}}^{*}\bigl (\prod_{\substack{1\leq i,j\leq k\\ i\neq j}}\frac{\mu(s_{i,j})}{g(s_{i,j})^{2}}\bigr)y_{a_{1},\ldots ,a_{k}}^{(m)}y_{b_{1},\ldots ,b_{k}}^{(m)},\tag{5.24}
$$

where$\begin{array} { r } { a _ { j } = u _ { j } \prod _ { i \neq j } s _ { j , i } } \end{array}$and$\begin{array} { r } { b _ { j } = u _ { j } \prod _ { i \neq j } s _ { i , j } } \end{array}$for each$1 \leq j \leq k$. As before, we have replaced $\mu ( a _ { j } )$with$\begin{array} { r } { \mu ( u _ { j } ) \prod _ { i \neq j } \mu ( s _ { j , i } ) } \end{array}$(and similarly for$g ( a _ { j } ) , \mu ( b _ { j } )$and$g ( b _ { j } ) )$. This is valid since terms with$a _ { j }$or$b _ { j }$Q<sub>not</sub> <sub>square-free</sub> <sub>make</sub> <sub>no</sub> <sub>contribution.</sub>

We see the contribution from$s _ { i , j } \neq 1$is of size

$$
\begin{aligned} & \ll \frac{(y_{max}^{(m)})^{2}N}{\varphi(W)\log N}\Big(\sum_{\substack{u <   R\\ (u,W) = 1}}\frac{\mu(u)^{2}}{g(u)}\Big)^{k - 1}\Big(\sum_{s}\frac{\mu(s)^{2}}{g(s)^{2}}\Big)^{k(k - 1) - 1}\sum_{s_{i,j} > D_{0}}\frac{\mu(s_{i,j})^{2}}{g(s_{i,j})^{2}}\\ & \ll \frac{(y_{max}^{(m)})^{2}\varphi(W)^{k - 2}N(\log R)^{k - 1}}{W^{k - 1}D_{0}\log N}. \end{aligned}\tag{5.25}
$$

Thus we find that

$$
S _ {2} ^ {(m)} = \frac {X _ {N}}{\varphi (W)} \sum_ {u _ {1}, \dots , u _ {k}} \frac {\left(y _ {u _ {1} , \dots , u _ {k}} ^ {(m)}\right) ^ {2}}{\prod_ {i = 1} ^ {k} g \left(u _ {i}\right)} + O \left(\frac {\left(y _ {\max} ^ {(m)}\right) ^ {2} \varphi (W) ^ {k - 2} N (\log R) ^ {k - 2}}{D _ {0} W ^ {k - 1}}\right) + O \left(\frac {y _ {\max} ^ {2} N}{(\log N) ^ {A}}\right).\tag{5.26}
$$

Finally, by the prime number theorem,$X _ { N } ~ = ~ N / \log N + O ( N / ( \log N ) ^ { 2 } )$. This error term contributes

$$
\ll \frac{(y_{max}^{(m)})^{2}N}{\varphi(W)(\log N)^{2}}\Big(\sum_{\substack{u <   R\\ (u,W) = 1}}\frac{\mu(u)^{2}}{g(u)}\Big)^{k - 1}\ll \frac{(y_{max}^{(m)})^{2}\varphi(W)^{k - 2}N(\log R)^{k - 3}}{W^{k - 1}},\tag{5.27}
$$

which can be absorbed into the first error term of (5.26). This completes the proof.

Remark. In ourproofofLemma 5.2 we only really require$\lambda _ { d _ { 1 } , \dots , d _ { k } }$to be supported on$d _ { 1 } , \ldots , d _ { k }$ satisfying$\textstyle \prod _ { i \neq j } d _ { i } < R$for all j instead of$\textstyle \prod _ { i = 1 } ^ { k } d _ { i } < R$. For$k \geq 3 ,$, the numerical benefit of this extension is small and so we do not consider itfurther.

Remark. As our result relies on the Bombieri-Vinogradov theorem, the implied constant in the error term is not efectively computable. However, ifwe restrict the$\lambda _ { d _ { 1 } , \dots , d _ { k } }$to be supported on$d _ { i }$which are coprime to the largest prime factor of a possible exceptional modulus of a primitive character then we can make this error term (and all others in this paper) efective at the cost of a negligible error.

We now relate our new variables$y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) }$to the$y _ { r _ { 1 } , \ldots , r _ { k } }$variables from$S _ { 1 }$.

Lemma 5.3.$I f r _ { m } = 1$then

$$
y _ {r _ {1}, \dots , r _ {k}} ^ {(m)} = \sum_ {a _ {m}} \frac {y _ {r _ {1} , \dots , r _ {m - 1} , a _ {m} , r _ {m + 1} , \dots , r _ {k}}}{\varphi (a _ {m})} + O \left(\frac {y _ {\max} \varphi (W) \log R}{W D _ {0}}\right).
$$

Proof. We assume throughout the proof that$r _ { m } = 1$. We first substitute our expression (5.8) into the definition (5.23). This gives

$$
y^{(m)}_{r_{1},\ldots ,r_{k}} = \Bigl (\prod_{i = 1}^{k}\mu (r_{i})g(r_{i})\Bigr)\sum_{\substack{d_{1},\ldots ,d_{k}\\ r_{i}|d_{i}\forall i\\ d_{m} = 1}}\Bigl (\prod_{i = 1}^{k}\frac{\mu(d_{i})d_{i}}{\varphi(d_{i})}\Bigr)\sum_{\substack{a_{1},\ldots ,a_{k}\\ d_{i}|a_{i}\forall i}}\frac{y_{a_{1},\ldots,a_{k}}}{\prod_{i = 1}^{k}\varphi(a_{i})}.\tag{5.28}
$$

We swap the summation of the d and a variables to give

$$
y^{(m)}_{r_{1},\ldots ,r_{k}} = \Bigl (\prod_{i = 1}^{k}\mu (r_{i})g(r_{i})\Bigr)\sum_{\substack{a_{1},\ldots ,a_{k}\\ r_{i}|a_{i}\forall i}}\frac{y_{a_{1},\ldots,a_{k}}}{\prod_{i = 1}^{k}\varphi(a_{i})}\sum_{\substack{d_{1},\ldots ,d_{k}\\ d_{i}|a_{i},r_{i}|d_{i}\forall i\\ d_{m} = 1}}\prod_{i = 1}^{k}\frac{\mu(d_{i})d_{i}}{\varphi(d_{i})}.\tag{5.29}
$$

We can now evaluate the sum over$d _ { 1 } , \ldots , d _ { k }$explicitly. This gives

$$
y^{(m)}_{r_{1},\ldots ,r_{k}} = \Big(\prod_{i = 1}^{k}\mu (r_{i})g(r_{i})\Big)\sum_{\substack{a_{1},\ldots ,a_{k}\\ r_{i}|a_{i}\forall i}}\frac{y_{a_{1},\ldots,a_{k}}}{\prod_{i = 1}^{k}\varphi(a_{i})}\prod_{i\neq m}\frac{\mu(a_{i})r_{i}}{\varphi(a_{i})}.\tag{5.30}
$$

We see that from the support of$y _ { a _ { 1 } , \ldots , a _ { k } }$that we may restrict the summation over$a _ { j }$to$( a _ { j } , W ) =$ 1. Thus either$a _ { j } = r _ { j }$or$a _ { j } > D _ { 0 } r _ { j }$. For$j \neq m$, the total contribution from$a _ { j } \neq r _ { j }$is

$$
\ll y_{max}\bigl (\prod_{i = 1}^{k}g(r_{i})r_{i}\bigr)\bigl (\sum_{\substack{a_{j} > D_{0}r_{j}\\ r_{j}|a_{j}}}\frac{\mu(a_{j})^{2}}{\varphi(a_{j})^{2}}\bigr)\bigl (\sum_{\substack{a_{m} <   R\\ (a_{m},W) = 1}}\frac{\mu(a_{m})^{2}}{\varphi(a_{m})}\bigr)\prod_{\substack{1\leq i\leq k\\ i\neq j,m}}\bigl (\sum_{r_{i}|a_{i}}\frac{\mu(a_{i})^{2}}{\varphi(a_{i})^{2}}\bigr)\tag{5.31}
$$

$$
\ll \bigl (\prod_ {i = 1} ^ {k} \frac {g (r _ {i}) r _ {i}}{\varphi (r _ {i}) ^ {2}} \bigr) \frac {y _ {m a x} \varphi (W) \log R}{W D _ {0}} \ll \frac {y _ {m a x} \varphi (W) \log R}{W D _ {0}}.
$$

Thus we find that the main contribution is when$a _ { j } = r _ { j }$for all$j \neq m$. We have

$$
y _ {r _ {1}, \dots , r _ {k}} ^ {(m)} = \left(\prod_ {i = 1} ^ {k} \frac {g (r _ {i}) r _ {i}}{\varphi (r _ {i}) ^ {2}}\right) \sum_ {a _ {m}} \frac {y _ {r _ {1} , \dots , r _ {m - 1} , a _ {m} , r _ {m + 1} , \dots , r _ {k}}}{\varphi (a _ {m})} + O \left(\frac {y _ {\max} \varphi (W) \log R}{W D _ {0}}\right).\tag{5.32}
$$

We note that$g ( p ) p / \varphi ( p ) ^ { 2 } = 1 + O ( p ^ { - 2 } )$. Thus, since the contribution is zero unless$\textstyle \prod _ { i = 1 } ^ { k } r _ { i }$is coprime to W, we see that the product in the above expression may be replaced by$1 + O ( D _ { 0 } ^ { - 1 } )$ This gives the result.

## 6. Smooth choice of y

We now choose suitable values for our y variables, and complete the proof of Proposition 4.1.

We first give some comments to motivate our choice of the y variables, which we believe should be close to optimal. We wish to choose y so as to maximize the ratio of the main terms of$S _ { 2 }$and$S _ { 1 }$. If we use Lagrangian multipliers to maximize this ratio (treating all error terms as zero) we arrive at the condition that

$$
\lambda y _ {r _ {1}, \dots , r _ {k}} = \left(\prod_ {i = 1} ^ {k} \frac {\varphi (r _ {i})}{g (r _ {i})}\right) \sum_ {m = 1} ^ {k} \frac {g (r _ {m})}{\varphi (r _ {m})} y _ {r _ {1}, \dots , r _ {m - 1}, 1, r _ {m + 1}, \dots , r _ {k}} ^ {(m)}\tag{6.1}
$$

for some fixed constant$\lambda .$The y terms are supported on integers free of small prime factors, and for most integers r free of small prime factors we have$g ( r ) \approx \varphi ( r ) \approx r ,$, and so the above condition reduces to

$$
\lambda y _ {r _ {1}, \dots , r _ {k}} \approx \sum_ {m = 1} ^ {k} y _ {r _ {1}, \dots , r _ {m - 1}, 1, r _ {m + 1}, \dots , r _ {k}} ^ {(m)}.\tag{6.2}
$$

This condition looks smooth (it has no dependence on the prime factorization of the$r _ { i } )$, and should be able to be satisfied if$y _ { r _ { 1 } , \ldots , r _ { k } }$is a smooth function of the$r _ { i }$variables. Motivated by the above, when the product$\begin{array} { r } { r = \prod _ { i = 1 } ^ { k } r _ { i } } \end{array}$satisfies$( r , W ) = 1$and$\mu ( r ) ^ { 2 } = 1$we choose

$$
y _ {r _ {1}, \dots , r _ {k}} = F \left(\frac {\log r _ {1}}{\log R}, \dots , \frac {\log r _ {k}}{\log R}\right),\tag{6.3}
$$

for some smooth function$F : \mathbb { R } ^ { k }  \mathbb { R } .$, supported on$\begin{array} { r } { \mathcal { R } _ { k } = \{ ( x _ { 1 } , \ldots , x _ { k } ) \in [ 0 , 1 ] ^ { k } : \sum _ { i = 1 } ^ { k } x _ { i } \le } \end{array}$ 1}. As previously required, we set$y _ { r _ { 1 } , \ldots , r _ { k } } = 0$P <sub>if</sub> <sub>the</sub> <sub>product</sub> <sub>r</sub> <sub>is</sub> <sub>either</sub> <sub>not</sub> <sub>coprime</sub> <sub>to</sub> <sub>W</sub> <sub>or</sub> <sub>is</sub> not square-free. With this choice of$y _ { \ast }$we can obtain suitable asymptotic estimates for$S _ { 1 }$and $S _ { 2 }$

We will use the following Lemma to estimate our sums$S _ { 1 }$and$S _ { 2 }$with this choice of$y .$.

Lemma 6.1. Let$A _ { 1 } , A _ { 2 } , L > 0$. Let γ be a multiplicative function satisfying

$$
0 \leq \frac {\gamma (p)}{p} \leq 1 - A _ {1},
$$

and

$$
- L \leq \sum_ {w \leq p \leq z} \frac {\gamma (p) \log p}{p} - \log z / w \leq A _ {2}
$$

for any$2 \leq w \leq z .$. Let g be the totally multiplicative function defined on primes by$g ( p ) =$ $\gamma ( p ) / ( p - \gamma ( p ) )$. Finally, let$G : [ 0 , 1 ] \to \mathbb { R }$be smooth, and let$\begin{array} { r } { G _ { m a x } = \mathbf { s u p } _ { t \in [ 0 , 1 ] } ( | G ( t ) | + | G ^ { \prime } ( t ) | ) } \end{array}$ Then

$$
\sum_ {d <   z} \mu (d) ^ {2} g (d) G \left(\frac {\log d}{\log z}\right) = \mathfrak {S} \log z \int_ {0} ^ {1} G (x) d x + O _ {A _ {1}, A _ {2}} (\mathfrak {S} L G _ {m a x}),
$$

where

$$
\mathfrak {S} = \prod_ {p} \left(1 - \frac {\gamma (p)}{p}\right) ^ {- 1} \left(1 - \frac {1}{p}\right).
$$

Here the constant implied by the$\cdot \boldsymbol { O } ^ { \prime }$term is independent ofG and$L .$

Proof. This is [3, Lemma$^ { 4 ] , }$, with$\kappa = 1$and slight changes to the notation.

We now finish our estimations of$S _ { 1 }$and${ S } _ { 2 } ^ { ( m ) }$, completing the proof of Proposition 4.1. We first estimate$S _ { 1 }$

Lemma 6.2. Let$y _ { r _ { 1 } , \ldots , r _ { k } }$be given in terms of a smooth function F by (6.3), with F supported on$\begin{array} { r } { \mathcal { R } _ { k } = \{ ( x _ { 1 } , . . . , x _ { k } ) \in [ 0 , 1 ] ^ { k } : \sum _ { i = 1 } ^ { k } x _ { i } \leq 1 \} } \end{array}$. Let

$$
F _ {m a x} = \sup _ {(t _ {1}, \dots , t _ {k}) \in [ 0, 1 ] ^ {k}} | F (t _ {1}, \dots , t _ {k}) | + \sum_ {i = 1} ^ {k} | \frac {\partial F}{\partial t _ {i}} (t _ {1}, \dots , t _ {k}) |.
$$

Then we have

$$
S _ {1} = \frac {\varphi (W) ^ {k} N (\log R) ^ {k}}{W ^ {k + 1}} I _ {k} (F) + O \left(\frac {F _ {\max} ^ {2} \varphi (W) ^ {k} N (\log R) ^ {k}}{W ^ {k + 1} D _ {0}}\right),
$$

where

$$
I _ {k} (F) = \int_ {0} ^ {1} \dots \int_ {0} ^ {1} F (t _ {1}, \dots , t _ {k}) ^ {2} d t _ {1} \dots d t _ {k}.
$$

Proof. We substitute our choice (6.3) of y into our expression of$S _ { 1 }$in terms of$y _ { r _ { 1 } , \ldots , r _ { k } }$given by Lemma 5.1. This gives

$$
S_{1} = \frac{N}{W}\sum_{\substack{u_{1},\ldots ,u_{k}\\ (u_{i},u_{j}) = 1\forall i\neq j\\ (u_{i},W) = 1\forall i}}\Bigl (\prod_{i = 1}^{k}\frac{\mu(u_{i})^{2}}{\varphi(u_{i})}\Bigr)F\Bigl (\frac{\log u_{1}}{\log R},\ldots ,\frac{\log u_{k}}{\log R}\Bigr)^{2} + O\Bigl (\frac{F_{max}^{2}\varphi(W)^{k}N(\log R)^{k}}{W^{k + 1}D_{0}}\Bigr).\tag{6.4}
$$

We note that two integers a and b with$( a , W ) = ( b , W ) = 1$but$( a , b ) \neq 1$must have a common prime factor which is greater than$D _ { 0 }$. Thus we can drop the requirement that$( u _ { i } , u _ { j } ) = 1$, at the cost of an error of size

$$
\begin{array}{l}\ll \frac{F_{max}^{2}N}{W}\sum_{p > D_{0}}\sum_{\substack{u_{1},\ldots ,u_{k} <   R\\ p|u_{i},u_{j}\\ (u_{i},W) = 1\forall i}}\prod_{i = 1}^{k}\frac{\mu(u_{i})^{2}}{\varphi(u_{i})}\\ \\ \ll \frac{F_{max}^{2}N}{W}\sum_{p > D_{0}}\frac{1}{(p - 1)^{2}}\Big(\sum_{\substack{u <   R\\ (u,W) = 1}}\frac{\mu(u)^{2}}{\varphi(u)}\Big)^{k}\ll \frac{F_{max}^{2}\varphi(W)^{k}N(\log R)^{k}}{W^{k + 1}D_{0}}. \end{array}\tag{6.5}
$$

Thus we are left to evaluate the sum

$$
\sum_{\substack{u_{1},\ldots ,u_{k}\\ (u_{i},W) = 1\forall i}}\Bigl (\prod_{i = 1}^{k}\frac{\mu(u_{i})^{2}}{\varphi(u_{i})}\Bigr)F\Bigl (\frac{\log u_{1}}{\log R},\ldots ,\frac{\log u_{k}}{\log R}\Bigr)^{2}.\tag{6.6}
$$

We can now estimate this sum by k applications of Lemma 6.1, dealing with the sum over each$u _ { i }$in turn. For each application we take

(6.7)

$$
\gamma (p) = \left\{ \begin{array}{l l} 1, & p \nmid W, \\ 0, & \text {otherwise}, \end{array} \right.\tag{6.8}
$$

$$
L \ll 1 + \sum_ {p | W} \frac {\log p}{p} \ll \log D _ {0},
$$

and$A _ { 1 }$and$A _ { 2 }$fixed constants of suitable size. This gives

$$
\sum_{\substack{u_{1},\ldots ,u_{k}\\ (u_{i},W) = 1\forall i}}\Bigl (\prod_{i = 1}^{k}\frac{\mu(u_{i})^{2}}{\varphi(u_{i})}\Bigr)F\Bigl (\frac{\log u_{1}}{\log R},\ldots ,\frac{\log u_{k}}{\log R}\Bigr)^{2} = \frac{\varphi(W)^{k}(\log R)^{k}}{W^{k}} I_{k}(F)\\ +O\Bigl (\frac{F_{max}^{2}\varphi(W)^{k}(\log D_{0})(\log R)^{k - 1}}{W^{k}}\Bigr).\tag{6.9}
$$

We now combine (6.9) with (6.4) and (6.5) to obtain the result.

Lemma 6.3. Let$y _ { r _ { 1 } , \ldots , r _ { k } } ,$, F and$F _ { m a x }$be as described in Lemma 6.2. Then we have

$$
S _ {2} ^ {(m)} = \frac {\varphi (W) ^ {k} N (\log R) ^ {k + 1}}{W ^ {k + 1} \log N} J _ {k} ^ {(m)} (F) + O \Bigl (\frac {F _ {m a x} ^ {2} \varphi (W) ^ {k} N (\log R) ^ {k}}{W ^ {k + 1} D _ {0}} \Bigr),
$$

where

$$
J _ {k} ^ {(m)} (F) = \int_ {0} ^ {1} \dots \int_ {0} ^ {1} \left(\int_ {0} ^ {1} F \left(t _ {1}, \dots , t _ {k}\right) d t _ {m}\right) ^ {2} d t _ {1} \dots d t _ {m - 1} d t _ {m + 1} \dots d t _ {k}.
$$

Proof. The estimation of${ S } _ { 2 } ^ { ( m ) }$is similar to the estimation of$S _ { 1 }$. We first estimate$y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) }$. We recall that$y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) } = 0$unless$r _ { m } = 1$and$\begin{array} { r } { r = \prod _ { i = 1 } ^ { k } r _ { i } } \end{array}$satisfies$( r , W ) = 1$and$\mu ( r ) ^ { 2 } = 1$, in which case$y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) }$is given in terms of$y _ { r _ { 1 } , \ldots , r _ { k } }$by Lemma 5.3. We first concentrate on this case when$y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) } \neq 0$. We substitute our choice (6.3) of y into our expression from Lemma 5.3. This gives

$$
\begin{array}{l} y _ {r _ {1}, \ldots , r _ {k}} ^ {(m)} = \sum_ {(u, W \prod_ {i = 1} ^ {k} r _ {i}) = 1} \frac {\mu (u) ^ {2}}{\varphi (u)} F \big (\frac {\log r _ {1}}{\log R}, \ldots , \frac {\log r _ {m - 1}}{\log R}, \frac {\log u}{\log R}, \frac {\log r _ {m + 1}}{\log R}, \ldots , \frac {\log r _ {k}}{\log R} \big) \\ \qquad + O \Big (\frac {F _ {m a x} \varphi (W) \log R}{W D _ {0}} \Big). \end{array}\tag{6.10}
$$

We can see from this that$y _ { m a x } ^ { ( m ) } \ll \varphi ( W ) F _ { m a x } ( \log R ) / W$. We now estimate the sum over u in (6.10). We apply Lemma 6.1 with

(6.11)

$$
\gamma (p) = \left\{ \begin{array}{l l} 1, & p \nmid W \prod_ {i = 1} ^ {k} r _ {i}, \\ 0, & \text { otherwise }, \end{array} \right.\tag{6.12}
$$

$$
L\ll 1 + \sum_{p|W\prod_{i = 1}^{k}r_{i}}\frac{\log p}{p}\ll \sum_{p <   \log R}\frac{\log p}{p} +\sum_{\substack{p|W\prod_{i = 1}^{k}r_{i}\\ p > \log R}}\frac{\log\log R}{\log R}\ll \log \log N,
$$

and with$A _ { 1 } , A _ { 2 }$suitable fixed constants. This gives us

$$
y _ {r _ {1}, \dots , r _ {k}} ^ {(m)} = (\log R) \frac {\varphi (W)}{W} \left(\prod_ {i = 1} ^ {k} \frac {\varphi (r _ {i})}{r _ {i}}\right) F _ {r _ {1}, \dots , r _ {k}} ^ {(m)} + O \left(\frac {F _ {\max} \varphi (W) \log R}{W D _ {0}}\right),\tag{6.13}
$$

where

$$
F _ {r _ {1}, \ldots , r _ {k}} ^ {(m)} = \int_ {0} ^ {1} F \Bigl (\frac {\log r _ {1}}{\log R}, \ldots , \frac {\log r _ {m - 1}}{\log R}, t _ {m}, \frac {\log r _ {m + 1}}{\log R}, \ldots , \frac {\log r _ {k}}{\log R} \Bigr) d t _ {m}.\tag{6.14}
$$

Thus we have shown that if$r _ { m } = 1$and$\begin{array} { r } { r = \prod _ { i = 1 } ^ { k } r _ { i } } \end{array}$satisfies$( r , W ) = 1$and$\mu ( r ) ^ { 2 } = 1$then $y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) }$is given by (6.13), and otherwise$y _ { r _ { 1 } , \ldots , r _ { k } } ^ { ( m ) } = 0$. We now substitute this into our expression

from Lemma 5.2, namely

$$
S _ {2} ^ {(m)} = \frac {N}{\varphi (W) \log N} \sum_ {r _ {1}, \dots , r _ {k}} \frac {\left(y _ {r _ {1} , \dots , r _ {k}} ^ {(m)}\right) ^ {2}}{\prod_ {i = 1} ^ {k} g \left(r _ {i}\right)} + O \left(\frac {\left(y _ {\max} ^ {(m)}\right) ^ {2} \varphi (W) ^ {k - 2} N (\log N) ^ {k - 2}}{W ^ {k - 1} D _ {0}}\right) + O \left(\frac {y _ {\max} ^ {2} N}{(\log N) ^ {A}}\right).\tag{6.15}
$$

We obtain

$$
S_{2}^{(m)} = \frac{\varphi(W)N(\log R)^{2}}{W^{2}\log N}\sum_{\substack{r_{1},\ldots ,r_{k}\\ (r_{i},W) = 1\forall i\\ (r_{i},r_{j}) = 1\forall i\neq j\\ r_{m} = 1}}\Bigl (\prod_{i = 1}^{k}\frac{\mu(r_{i})^{2}\varphi(r_{i})^{2}}{g(r_{i})r_{i}^{2}}\Bigr)(F_{r_{1},\ldots ,r_{k}}^{(m)})^{2} + O\Bigl (\frac{F_{max}^{2}\varphi(W)^{k}N(\log R)^{k}}{W^{k + 1}D_{0}}\Bigr).\tag{6.16}
$$

We remove the condition that$( r _ { i } , r _ { j } ) = 1$in the same way we did when considering$S _ { 1 }$. Instead of (6.5), this introduces an error which is of size

$$
\ll \frac{\varphi(W)N(\log R)^{2}F_{max}^{2}}{W^{2}\log N}\bigl (\sum_{p > D_{0}}\frac{\varphi(p)^{4}}{g(p)^{2}p^{4}}\bigr)\bigl (\sum_{\substack{r <   R\\ (r,W) = 1}}\frac{\mu(r)^{2}\varphi(r)^{2}}{g(r)r^{2}}\bigr)^{k - 1}\\ \ll \frac{F_{max}^{2}\varphi(W)^{k}N(\log N)^{k}}{W^{k + 1}D_{0}}.\tag{6.17}
$$

Thus we are left to evaluate the sum

$$
\sum_{\substack{r_{1},\ldots ,r_{m - 1},r_{m + 1},\ldots ,r_{k}\\ (r_{i},W) = 1\forall i}}\Bigl (\prod_{\substack{1\leq i\leq k\\ i\neq j}}\frac{\mu(r_{i})^{2}\varphi(r_{i})^{2}}{g(r_{i})r_{i}^{2}}\Bigr)(F_{r_{1},\ldots ,r_{k}}^{(m)})^{2}.\tag{6.18}
$$

We estimate this by applying Lemma 6.1 to each summation variable in turn. In each case we take

(6.19)

$$
\gamma (p) = \left\{ \begin{array}{l l} 1 - \frac {p ^ {2} - 3 p + 1}{p ^ {3} - p ^ {2} - 2 p + 1}, & p \nmid W \\ 0, & \text {otherwise}, \end{array} \right.\tag{6.20}
$$

$$
L \ll 1 + \sum_ {p | W} \frac {\log p}{p} \ll \log D _ {0},
$$

and$A _ { 1 } , A _ { 2 }$suitable fixed constants. This gives

$$
S _ {2} ^ {(m)} = \frac {\varphi (W) ^ {k} N (\log R) ^ {k + 1}}{W ^ {k + 1} \log N} J _ {k} ^ {(m)} + O \Bigl (\frac {F _ {m a x} ^ {2} \varphi (W) ^ {k} N (\log N) ^ {k}}{W ^ {k + 1} D _ {0}} \Bigr),\tag{6.21}
$$

where

$$
J _ {k} ^ {(m)} = \int_ {0} ^ {1} \dots \int_ {0} ^ {1} \left(\int_ {0} ^ {1} F (t _ {1}, \dots , t _ {k}) d t _ {m}\right) ^ {2} d t _ {1} \dots d t _ {m - 1} d t _ {m + 1} \dots d t _ {k},\tag{6.22}
$$

as required.

Remark. If$\begin{array} { r } { F ( t _ { 1 } , . . . , t _ { k } ) = G ( \sum _ { i = 1 } ^ { k } t _ { i } ) } \end{array}$for some function$G ,$then$I _ { k } ( F )$and$J _ { k } ^ { ( m ) } ( F )$simplify to $\begin{array} { r } { I _ { k } ( F ) = \int _ { 0 } ^ { 1 } G ( t ) ^ { 2 } t ^ { k - 1 } d t / ( k - 1 ) ! } \end{array}$and$\begin{array} { r } { J _ { k } ^ { ( m ) } ( F ) = \int _ { 0 } ^ { 1 } ( \int _ { t } ^ { 1 } G ( \nu ) d \nu ) ^ { 2 } t ^ { k - 2 } d t / ( k - 2 ) ! } \end{array}$for each m, which is equivalent to the results obtained using the original GPY method using weights given by (2.3).

Remark. Tao gives an alternative approach to arrive at his equivalent ofProposition 4.1. His approach is to define$\lambda _ { d _ { 1 } , \dots , d _ { k } }$in terms of a suitable smooth function$f ( t _ { 1 } , \ldots , t _ { k } )$as in (2.5). He then estimates the corresponding sums directly using Fourier integrals. This is somewhat similar to the original paper ofGoldston, Pintz and Yıldırım [5]. Ourfunction F corresponds to$f ( t _ { 1 } , \ldots , t _ { k } )$diferentiated with respect to each coordinate.

## 7. Choice of smooth weight for large$k$

In this section we establish part (3) of Proposition 4.3. Our argument here is closely related to that of Tao, who uses a probability theory proof.

We let$S _ { k }$denote the set of Riemann-integrable functions$F : [ 0 , 1 ] ^ { k } \to \mathbb { R }$supported on $\begin{array} { r } { \mathcal { R } _ { k } = \{ ( x _ { 1 } , . . . , x _ { k } ) \in [ 0 , 1 ] ^ { k } : \sum _ { i = 1 } ^ { k } x _ { i } \le 1 \} } \end{array}$with$I _ { k } ( F ) \ne 0$and$J _ { k } ^ { ( m ) } ( F ) \neq 0$for each m. We would like to obtain a lower bound for

$$
M _ {k} = \sup _ {F \in \mathcal {S} _ {k}} \frac {\sum_ {m = 1} ^ {k} J _ {k} ^ {(m)} (F)}{I _ {k} (F)}.\tag{7.1}
$$

Remark. Let$\mathcal { L } _ { k }$denote the linear operator defined by

$$
\mathcal {L} _ {k} F (u _ {1}, \dots , u _ {k}) = \sum_ {m = 1} ^ {k} \int_ {0} ^ {1 - \sum_ {i \neq m} u _ {i}} F (u _ {1}, \dots , u _ {m - 1}, t _ {m}, u _ {m + 1}, \dots , u _ {k}) d t _ {m}\tag{7.2}
$$

whenever$( u _ { 1 } , \ldots , u _ { k } ) \ \in \ { \mathcal { R } } _ { k }$, and zero otherwise. We expect that if F maximizes the ratio $\textstyle \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F ) / I _ { k } ( F )$, then F is an eigenfunction for$\mathcal { L } _ { k }$, and the corresponding eigenvalue is the value of ratio at F. Unfortunately the author has not been able to solve the eigenvalue equationfor$\mathcal { L } _ { k }$when$k > 2$

We obtain a lower bound for$M _ { k }$by constructing a function$F = F _ { k }$which makes the ratio $\textstyle \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F ) / I _ { k } ( F )$large provided k is large. We choose$F$to be of the form

$$
F (t _ {1}, \ldots , t _ {k}) = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {k} g (k t _ {i}), & \text { if } \sum_ {i = 1} ^ {k} t _ {i} \leq 1, \\ 0, & \text { otherwise }, \end{array} \right.\tag{7.3}
$$

for some smooth function$g : [ 0 , \infty ]  \mathbb { R } .$, supported on [0, T]. We see that with this choice F is symmetric, and so$J _ { k } ^ { ( m ) } ( F )$is independent of m. Thus we only need to consider$J _ { k } = J _ { k } ^ { ( 1 ) } ( F )$ Similarly we write$I _ { k } \stackrel { \cdot } { = } I _ { k } ( F )$.

The key observation is that if the center of mass$\begin{array} { r }  \int _ { 0 } ^ { \infty } u g ( u ) ^ { 2 } d u / \int _ { 0 } ^ { \infty } g ( u ) ^ { 2 } d \ \end{array}$du of$g ^ { 2 }$is strictly less than 1, then for large k we expect that the constraints$\textstyle \sum _ { i = 1 } ^ { k } t _ { i } \ \leq \ 1$to be able to be P<sub>dropped at the cost of only a small error. This is because (by concentration of measure)</sub> the main contribution to the unrestricted integrals$\begin{array} { r } { I _ { k } ^ { \prime } \ = \ \int _ { 0 } ^ { \infty } \cdot \cdot \cdot \cdot \int _ { 0 } ^ { \infty } \prod _ { i = 1 } ^ { k } g ( k t _ { i } ) ^ { 2 } d t _ { 1 } \dots d t _ { k } } \end{array}$and $\begin{array} { r } { J _ { k } ^ { \prime } = \int _ { 0 } ^ { \infty } \cdot \cdot \cdot \cdot \int _ { 0 } ^ { \infty } ( \int _ { 0 } ^ { \infty } \prod _ { i = 1 } ^ { k } g ( k t _ { i } ) d t _ { 1 } ) ^ { 2 } d t _ { 2 } \dots d t _ { k } } \end{array}$should come primarily from when$\textstyle \sum _ { i = 1 } ^ { k } t _ { i }$is close to the center of mass. Therefore we would expect the contribution when$\textstyle \sum _ { i = 1 } ^ { k } t _ { i } > 1$to be small if the center of mass is less than 1, and so$I _ { k }$and$J _ { k }$are well approximated by$I _ { k } ^ { \prime }$and$J _ { k } ^ { \prime }$ in this case.

To ease notation we let$\begin{array} { r } { \gamma = \int _ { u \geq 0 } g ( u ) ^ { 2 } d u } \end{array}$, and restrict our attention to g such that$\gamma > 0$. We have

$$
I _ {k} = \int_ {\mathcal {R} _ {k}} \dots \int F (t _ {1}, \dots , t _ {k}) ^ {2} d t _ {1} \dots d t _ {k} \leq \left(\int_ {0} ^ {\infty} g (k t) ^ {2} d t\right) ^ {k} = k ^ {- k} \gamma^ {k}.\tag{7.4}
$$

We now consider$J _ { k }$. Since squares are non-negative, we obtain a lower bound for$J _ { k }$if we restrict the outer integral to$\textstyle \sum _ { i = 2 } ^ { k } t _ { i } < 1 - T / k$. This has the advantage that, by the support of $^ { g , }$there are no further restrictions on the inner integral. Thus

$$
J_{k}\geq \int \limits_{\substack{t_{2},\ldots ,t_{k}\geq 0\\ \sum_{i = 2}^{k}t_{i}\leq 1 - T / k}}\Bigl (\int_{0}^{T / k}\Bigl (\prod_{i = 1}^{k}g(kt_{i})\Bigr)dt_{1}\Bigr)^{2}dt_{2}\dots dt_{k}.\tag{7.5}
$$

We write the right hand side of (7.5) as$J _ { k } ^ { \prime } - E _ { k }$, where

(7.6)

$$
\begin{aligned} J_{k}^{\prime} & = \int \dots \int \Bigl (\int_ {0} ^ {T / k}\Bigl (\prod_ {i = 1}^{k}g(kt_{i})\Bigr)dt_{1}\Bigr)^{2}dt_{2}\dots dt_{k}\\ & = \Bigl (\int_ {0}^{\infty}g(kt_{1})dt_{1}\Bigr)^{2}\Bigl (\int_ {0}^{\infty}g(kt)^{2}dt\Bigr)^{k - 1} = k^{-k - 1}\gamma^{k - 1}\Bigl (\int_ {0}^{\infty}g(u)du\Bigr)^{2},\\ E_{k} & = \int \dots \int \limits_{\substack{t_{2},\ldots ,t_{k}\geq 0\\ \sum_{i = 2}^{k}t_{i} > 1 - T / k}}\Bigl (\int_ {0}^{T / k}\Bigl (\prod_ {i = 1}^{k}g(kt_{i})\Bigr)dt_{1}\Bigr)^{2}dt_{2}\dots dt_{k}\\ & = k^{-k - 1}\Bigl (\int_ {0}^{\infty}g(u)du\Bigr)^{2}\int \dots \int \limits_{\substack{u_{2},\ldots ,u_{k}\geq 0\\ \sum_{i = 2}^{k}u_{i} > k - T}}\Bigl (\prod_ {i = 2}^{k}g(u_{i})^{2}\Bigr)du_{2}\dots du_{k}. \end{aligned}\tag{7.7}
$$

First we wish to show the error integral$E _ { k }$is small. We do this by comparison with a second moment. We expect the bound (7.13) for$E _ { k }$to be small if the center of mass of$g ^ { 2 }$is strictly less than$( k - T ) / ( k - 1 )$). Therefore we introduce the restriction on$g$that

$$
\mu = \frac {\int_ {0} ^ {\infty} u g (u) ^ {2} d u}{\int_ {0} ^ {\infty} g (u) ^ {2} d u} <   1 - \frac {T}{k}.\tag{7.8}
$$

To simplify notation, we put$\eta = ( k - T ) / ( k - 1 ) - \mu > 0$. If$\textstyle \sum _ { i = 2 } ^ { k } u _ { i } > k - T$then$\textstyle \sum _ { i = 2 } ^ { k } u _ { i } >$ $( k - 1 ) ( \mu + \eta )$, and so we have

$$
1 \leq \eta^ {- 2} \left(\frac {1}{k - 1} \sum_ {i = 2} ^ {k} u _ {i} - \mu\right) ^ {2}.\tag{7.9}
$$

Since the right hand side of (7.9) is non-negative for all$u _ { i } ,$, we obtain an upper bound for$E _ { k }$ if we multiply the integrand by$\eta ^ { - 2 } ( \sum _ { i = 2 } ^ { k } u _ { i } / ( k - 1 ) - \mu ) ^ { 2 }$, and then drop the requirement that $\begin{array} { r } { \sum _ { i = 1 } ^ { k } u _ { i } > k - T } \end{array}$. This gives us

$$
E _ {k} \leq \eta^ {- 2} k ^ {- k - 1} \left(\int_ {0} ^ {\infty} g (u) d u\right) ^ {2} \int_ {0} ^ {\infty} \dots \int_ {0} ^ {\infty} \left(\frac {\sum_ {i = 2} ^ {k} u _ {i}}{k - 1} - \mu\right) ^ {2} \left(\prod_ {i = 2} ^ {k} g \left(u _ {i}\right) ^ {2}\right) d u _ {2} \dots d u _ {k}.\tag{7.10}
$$

We expand out the inner square. All the terms which are not of the form$u _ { j } ^ { 2 }$we can calculate explicitly as an expression in$\mu$and γ. We find

$$
\int_ {0} ^ {\infty} \dots \int_ {0} ^ {\infty} \left(\frac {2 \sum_ {2 \leq i <   j \leq k} u _ {i} u _ {j}}{(k - 1) ^ {2}} - \frac {2 \mu \sum_ {i = 2} ^ {k} u _ {i}}{k - 1} + \mu^ {2}\right) \left(\prod_ {i = 2} ^ {k} g (u _ {i}) ^ {2}\right) d u _ {2} \dots d u _ {k} = \frac {- \mu^ {2} \gamma^ {k - 1}}{k - 1}.\tag{7.11}
$$

For the$u _ { j } ^ { 2 }$terms we see that$u _ { j } ^ { 2 } g ( u _ { j } ) ^ { 2 } \leq T u _ { j } g ( u _ { j } ) ^ { 2 }$from the support of$g .$Thus

$$
\int_ {0} ^ {\infty} \dots \int_ {0} ^ {\infty} u _ {j} ^ {2} \left(\prod_ {i = 2} ^ {k} g (u _ {i}) ^ {2}\right) d u _ {2} \dots d u _ {k} \leq T \gamma^ {k - 2} \int_ {0} ^ {\infty} u _ {j} g (u _ {j}) ^ {2} d u _ {j} = \mu T \gamma^ {k - 1}.\tag{7.12}
$$

This gives

$$
E _ {k} \leq \eta^ {- 2} k ^ {- k - 1} \left(\int_ {0} ^ {\infty} g (u) d u\right) ^ {2} \left(\frac {\mu T \gamma^ {k - 1}}{k - 1} - \frac {\mu^ {2} \gamma^ {k - 1}}{k - 1}\right) \leq \frac {\eta^ {- 2} \mu T k ^ {- k - 1} \gamma^ {k - 1}}{k - 1} \left(\int_ {0} ^ {\infty} g (u) d u\right) ^ {2}.\tag{7.13}
$$

Since$( k - 1 ) \eta ^ { 2 } \geq k ( 1 - T / k - \mu ) ^ { 2 }$and$\mu \leq 1$, we find that putting together (7.4), (7.5), (7.6) and (7.13), we obtain

$$
\frac {k J _ {k}}{I _ {k}} \geq \frac {\left(\int_ {0} ^ {\infty} g (u) d u\right) ^ {2}}{\int_ {0} ^ {\infty} g (u) ^ {2} d u} \left(1 - \frac {T}{k (1 - T / k - \mu) ^ {2}}\right).\tag{7.14}
$$

To maximize our lower bound (7.14), we wish to maximize$\int _ { 0 } ^ { T } g ( u ) d u$subject to the constraints that$\int _ { 0 } ^ { T } g ( u ) ^ { 2 } d u = \gamma$and$\int _ { 0 } ^ { T } u g ( u ) ^ { 2 } d u = \mu \gamma$. Thus we wish to maximize the expression

$$
\int_ {0} ^ {T} g (u) d u - \alpha \left(\int_ {0} ^ {T} g (u) ^ {2} d u - \gamma\right) - \beta \left(\int_ {0} ^ {T} u g (u) ^ {2} d u - \mu \gamma\right)\tag{7.15}
$$

with respect to$\alpha , \beta$and the function$g .$. By the Euler-Lagrange equation, this occurs when $\begin{array} { r } { \frac { \partial } { \partial g } ( g ( t ) \dot { - } \alpha g ( t ) ^ { 2 } - \dot { \beta } t g ( t ) ^ { 2 } ) = 0 } \end{array}$for all$t \in [ 0 , T ]$. Thus we see that

$$
g (t) = \frac {1}{2 \alpha + 2 \beta t} \qquad \mathrm{for} 0 \leq t \leq T.\tag{7.16}
$$

Since the ratio we wish to maximize is unafected if we multiply g by a positive constant, we restrict our attention to functions$g$is of the form$1 / ( 1 + A t )$for$t \in [ 0 , T ]$and for some constant$A > 0$. With this choice of$g$we find that

(7.17)

$$
\int_ {0} ^ {T} g (u) d u = \frac {\log (1 + A T)}{A}, \quad \int_ {0} ^ {T} g (u) ^ {2} d u = \frac {1}{A} \left(1 - \frac {1}{1 + A T}\right),\tag{7.18}
$$

$$
\int_ {0} ^ {T} u g (u) ^ {2} d u = \frac {1}{A ^ {2}} \left(\log (1 + A T) - 1 + \frac {1}{1 + A T}\right).
$$

We choose T such that$1 + A T = e ^ { A }$(which is close to optimal). With this choice we find that$\mu = 1 / ( 1 - e ^ { - A } ) - A ^ { - 1 }$and$T \le e ^ { A } / A$. Thus$1 - T / k - \mu \geq A ^ { - 1 } ( 1 - A / ( e ^ { A } - 1 ) - e ^ { A } / k )$ Substituting$( 7 . 1 7 )$into$( 7 . 1 4 )$, and then using these expressions, we find that

$$
\frac {k J _ {k}}{I _ {k}} \geq \frac {A}{1 - e ^ {- A}} \left(1 - \frac {T}{k (1 - T / k - \mu) ^ {2}}\right) \geq A \left(1 - \frac {A e ^ {A}}{k (1 - A / (e ^ {A} - 1) - e ^ {A} / k) ^ {2}}\right),\tag{7.19}
$$

provided the right hand side is positive. Finally, we choose$A = \log k - 2$log log$k > 0$. For k suficiently large we have

$$
1 - \frac {T}{k} - \mu \geq A ^ {- 1} \Big (1 - \frac {(\log k) ^ {3}}{k} - \frac {1}{(\log k) ^ {2}} \Big) > 0,\tag{7.20}
$$

and so$\mu < 1 - T / k$, as required by our constraint (7.8). This choice of A gives

$$
M _ {k} \geq \frac {k J _ {k}}{I _ {k}} \geq (\log k - 2 \log \log k) \left(1 - \frac {\log k}{(\log k) ^ {2} + O (1)}\right) \geq \log k - 2 \log \log k - 2\tag{7.21}
$$

when k is suficiently large.

## 8. Choice of weight for small k

In this section we establish parts (1) and (2) of Proposition 4.3. In order to get a suitable lower bound for$M _ { k }$when k is small, we will consider approximations to the optimal function F of the form

$$
F (t _ {1}, \ldots , t _ {k}) = \left\{ \begin{array}{l l} P (t _ {1}, \ldots , t _ {k}), & \text { if } (t _ {1}, \ldots , t _ {k}) \in \mathcal {R} _ {k} \\ 0, & \text { otherwise }, \end{array} \right.\tag{8.1}
$$

for polynomials P. By the symmetry of$\textstyle \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F )$and$I _ { k } ( F )$, we restrict our attention to polynomials which are symmetric functions of$t _ { 1 } , \ldots , t _ { k }$. (If F satisfies$\mathcal { L } _ { k } F = \lambda F$then $F _ { \sigma } = F ( \sigma ( t _ { 1 } ) , \ldots , \sigma ( t _ { k } ) )$also satisfies this for every permutation$\sigma$of$t _ { 1 } , \ldots , t _ { k }$. Thus the symmetric function which is the average of$F _ { \sigma }$over all such permutations would satisfy this eigenfunction equation, and so we expect there to be an optimal function which is symmetric.) Any such polynomial can be written as a polynomial expression in the power sum polynomials $\begin{array} { r } { P _ { j } = \sum _ { i = 1 } ^ { k } t _ { i } ^ { j } } \end{array}$

Lemma 8.1. Let$\begin{array} { r } { P _ { j } = \sum _ { i = 1 } ^ { k } t _ { i } ^ { j } } \end{array}$denote the$j ^ { t h }$symmetric power sum polynomial. Then we have

$$
\int_ {\mathcal {R} _ {k}} \dots \int (1 - P _ {1}) ^ {a} P _ {j} ^ {b} d t _ {1} \dots d t _ {k} = \frac {a !}{(k + j b + a) !} G _ {b, j} (k),
$$

where

$$
G_{b,j}(x) = b!\sum_{r = 1}^{b}\binom {x}{r}\sum_{\substack{b_{1},\ldots ,b_{r}\geq 1\\ \sum_{i = 1}^{r}b_{i} = b}}\prod_{i = 1}^{r}\frac{(jb_{i})!}{b_{i}!}
$$

is a polynomial of degree b which depends only on b and$j .$

Proof. We first show by induction on k that

$$
\int_ {\mathcal {R} _ {k}} \dots \int \left(1 - \sum_ {i = 1} ^ {k} t _ {i}\right) ^ {a} \prod_ {i = 1} ^ {k} t _ {i} ^ {a _ {i}} d t _ {1} \dots d t _ {k} = \frac {a ! \prod_ {i = 1} ^ {k} a _ {i} !}{(k + a + \sum_ {i = 1} ^ {k} a _ {i}) !}.\tag{8.2}
$$

We consider the integration with respect to$t _ { 1 }$. The limits of integration are 0 and$\textstyle 1 - \sum _ { i = 2 } ^ { k } t _ { i }$ for$( t _ { 2 } , \ldots , t _ { k } ) \in { \mathcal { R } } _ { k - 1 }$. By substituting$\nu = t _ { 1 } / ( 1 - \textstyle \sum _ { i = 2 } ^ { k } t _ { i } )$we find

$$
\begin{array}{c} \int_ {0} ^ {1 - \sum_ {i = 2} ^ {k} t _ {i}} \Big (1 - \sum_ {i = 1} ^ {k} t _ {i} \Big) ^ {a} \Big (\prod_ {i = 1} ^ {k} t _ {i} ^ {a _ {i}} \Big) d t _ {1} = \Big (\prod_ {i = 2} ^ {k} t _ {i} ^ {a _ {i}} \Big) \Big (1 - \sum_ {i = 2} ^ {k} t _ {i} \Big) ^ {a + a _ {1} + 1} \int_ {0} ^ {1} (1 - v) ^ {a} v ^ {a _ {1}} d v \\ = \frac {a ! a _ {1} !}{(a + a _ {1} + 1) !} \Big (\prod_ {i = 2} ^ {k} t _ {i} ^ {a _ {i}} \Big) \Big (1 - \sum_ {i = 2} ^ {k} t _ {i} \Big) ^ {a + a _ {1} + 1}. \end{array}\tag{8.3}
$$

Here we used the beta function identity$\begin{array} { r } { \int _ { 0 } ^ { 1 } t ^ { a } ( 1 - t ) ^ { b } d t = a ! b ! / ( a + b + 1 ) ! } \end{array}$in the last line. We now see (8.2) follows by induction.

By the binomial theorem,

$$
P_{j}^{b} = \sum_{\substack{b_{1},\ldots ,b_{k}\\ \sum_{i = 1}^{k}b_{i} = b}}\frac{b!}{\prod_{i = 1}^{k}b_{i}!}\prod_{i = 1}^{k}t_{i}^{jb_{i}}.\tag{8.4}
$$

Thus, applying (8.2), we obtain

$$
\int \limits_{\mathcal{R}_{k}}\dots \int (1 - P_{1})^{a}P_{j}^{b}dt_{1}\dots dt_{k} = \frac{b!a!}{(k + a + jb)!}\sum_{\substack{b_{1},\ldots ,b_{k}\\ \sum_{i = 1}^{k}b_{i} = b}}\prod_{i = 1}^{k}\frac{(jb_{i})!}{b_{i}!}.\tag{8.5}
$$

For computations b will be small, and so we find it convenient to split the summation depending on how many of the$b _ { i }$are non-zero. Given an integer r, there are$\binom { k } { r }$ways of choosing r of$b _ { 1 } , \ldots , b _ { k }$to be non-zero. Thus

$$
\sum_{\substack{b_{1},\ldots ,b_{k}\\ \sum_{i = 1}^{k}b_{i} = b}}\prod_{i = 1}^{k}\frac{(jb_{i})!}{b_{i}!} = \sum_{r = 1}^{b}\binom {k}{r}\sum_{\substack{b_{1},\ldots ,b_{r}\geq 1\\ \sum_{i = 1}^{r}b_{i} = b}}\prod_{i = 1}^{r}\frac{(jb_{i})!}{b_{i}!}.\tag{8.6}
$$

This gives the result.

It is straightforward to extend Lemma 8.1 to more general combinations of the symmetric power polynomials. In this paper we will concentrate on the case when P is a polynomial expression in only$P _ { 1 }$and$P _ { 2 }$for simplicity. We comment the polynomials$G _ { b , j }$are not problematic to calculate numerically for small values of b. We now use Lemma 8.1 to obtain a manageable expression for$I _ { k } ( F )$and$J _ { k } ^ { ( m ) } ( F )$with this choice of$P$.

Lemma 8.2. Let F be given in terms ofa polynomial P by (8.1). Let P be given in terms ofa polynomial expression in the symmetric power polynomials$\textstyle P _ { 1 } = \sum _ { i = 1 } ^ { k } t _ { i }$and$\begin{array} { r } { P _ { 2 } = \sum _ { i = 1 } ^ { k } t _ { i } ^ { 2 } } \end{array}$by $\begin{array} { r } { P = \sum _ { i = 1 } ^ { d } a _ { i } ( 1 - P _ { 1 } ) ^ { b _ { i } } P _ { 2 } ^ { c _ { i } } } \end{array}$for constants$a _ { i } \in \mathbb { R }$and non-negative integers$b _ { i } , c _ { i }$. Then for each $1 \leq m \leq k$we have

$$
\begin{array}{c} I _ {k} (F) = \sum_ {1 \leq i, j \leq d} a _ {i} a _ {j} \frac {(b _ {i} + b _ {j}) ! G _ {c _ {i} + c _ {j} , 2} (k)}{(k + b _ {i} + b _ {j} + 2 c _ {i} + 2 c _ {j}) !}, \\ J _ {k} ^ {(m)} (F) = \sum_ {1 \leq i, j \leq d} a _ {i} a _ {j} \sum_ {c _ {1} ^ {\prime} = 0} ^ {c _ {i}} \sum_ {c _ {2} ^ {\prime} = 0} ^ {c _ {j}} \binom {c _ {i}} {c _ {1} ^ {\prime}} \binom {c _ {j}} {c _ {2} ^ {\prime}} \frac {\gamma_ {b _ {i} , b _ {j} , c _ {i} , c _ {j} , c _ {1} ^ {\prime} , c _ {2} ^ {\prime}} G _ {c _ {1} ^ {\prime} + c _ {2} ^ {\prime} , 2} (k - 1)}{(k + b _ {i} + b _ {j} + 2 c _ {i} + 2 c _ {j} + 1) !}, \end{array}
$$

where

$$
\gamma_ {b _ {i}, b _ {j}, c _ {i}, c _ {j}, c _ {1} ^ {\prime}, c _ {2} ^ {\prime}} = \frac {b _ {i} ! b _ {j} ! (2 c _ {i} - 2 c _ {1} ^ {\prime}) ! (2 c _ {j} - 2 c _ {2} ^ {\prime}) ! (b _ {i} + b _ {j} + 2 c _ {i} + 2 c _ {j} - 2 c _ {1} ^ {\prime} - 2 c _ {2} ^ {\prime} + 2) !}{(b _ {i} + 2 c _ {i} - 2 c _ {1} ^ {\prime} + 1) ! (b _ {j} + 2 c _ {j} - 2 c _ {2} ^ {\prime} + 1) !},
$$

and where G is the polynomial given by Lemma 8.1.

Proof. We first consider$I _ { k } ( F )$. We have, using Lemma 8.1,

$$
\begin{array}{l} I _ {k} (F) = \int_ {\mathcal {R} _ {k}} \dots \int P ^ {2} d t _ {1} \ldots d t _ {k} = \sum_ {1 \leq i, j \leq d} a _ {i} a _ {j} \int_ {\mathcal {R} _ {k}} \dots \int (1 - P _ {1}) ^ {b _ {i} + b _ {j}} P _ {2} ^ {c _ {i} + c _ {j}} d t _ {1} \ldots d t _ {k} \\ = \sum_ {1 \leq i, j \leq d} a _ {i} a _ {j} \frac {(b _ {i} + b _ {j}) ! G _ {c _ {i} + c _ {j} , 2} (k)}{(k + b _ {i} + b _ {j} + 2 c _ {i} + 2 c _ {j}) !}. \end{array}\tag{8.7}
$$

We now consider$J _ { k } ^ { ( m ) } ( F )$. Since F is symmetric in$t _ { 1 } , \ldots , t _ { k }$we see that$J _ { k } ^ { ( m ) } ( F )$is independent of$m ,$and so it sufices to only consider$J _ { k } ^ { ( 1 ) } ( F )$. We have

$$
\begin{array}{l} \int_ {0} ^ {1 - \sum_ {i = 2} ^ {k} t _ {i}} (1 - P _ {1}) ^ {b} P _ {2} ^ {c} d t _ {1} = \sum_ {c ^ {\prime} = 0} ^ {c} \binom {c} {c ^ {\prime}} \Big (\sum_ {i = 2} ^ {k} t _ {i} ^ {2} \Big) ^ {c ^ {\prime}} \int_ {0} ^ {1 - \sum_ {i = 2} ^ {k} t _ {i}} \Big (1 - \sum_ {i = 1} ^ {k} t _ {i} \Big) ^ {b} t _ {1} ^ {2 c - 2 c ^ {\prime}} d t _ {1} \\ = \sum_ {c ^ {\prime} = 0} ^ {c} \binom {c} {c ^ {\prime}} (P _ {2} ^ {\prime}) ^ {c ^ {\prime}} (1 - P _ {1} ^ {\prime}) ^ {b + 2 c - 2 c ^ {\prime} + 1} \int_ {0} ^ {1} (1 - u) ^ {b} u ^ {2 c - 2 c ^ {\prime}} d u \\ = \sum_ {c ^ {\prime} = 0} ^ {c} \binom {c} {c ^ {\prime}} (P _ {2} ^ {\prime}) ^ {c ^ {\prime}} (1 - P _ {1} ^ {\prime}) ^ {b + 2 c - 2 c ^ {\prime} + 1} \frac {b ! (2 c - 2 c ^ {\prime}) !}{(b + 2 c - 2 c ^ {\prime} + 1) !}, \end{array}\tag{8.8}
$$

where$\textstyle P _ { 1 } ^ { \prime } = \sum _ { i = 2 } ^ { k } t _ { i }$and$\begin{array} { r } { P _ { 2 } ^ { \prime } = \sum _ { i = 2 } ^ { k } t _ { i } ^ { 2 } } \end{array}$. Thus

$$
\begin{array}{l} \left(\int_ {0} ^ {1} F d t _ {1}\right) ^ {2} = \left(\sum_ {i = 1} ^ {d} a _ {i} \int_ {0} ^ {1 - \sum_ {j = 2} ^ {k} t _ {j}} (1 - P _ {1}) ^ {b _ {i}} P _ {2} ^ {c _ {i}} d t _ {1}\right) ^ {2} \\ = \sum_ {1 \leq i, j \leq d} a _ {i} a _ {j} \sum_ {c _ {1} ^ {\prime} = 0} ^ {c _ {i}} \sum_ {c _ {2} ^ {\prime} = 0} ^ {c _ {j}} \binom {c _ {i}} {c _ {1} ^ {\prime}} \binom {c _ {j}} {c _ {2} ^ {\prime}} (P _ {2} ^ {\prime}) ^ {c _ {1} ^ {\prime} + c _ {2} ^ {\prime}} (1 - P _ {1} ^ {\prime}) ^ {b _ {i} + b _ {j} + 2 c _ {i} + 2 c _ {j} - 2 c _ {1} ^ {\prime} - 2 c _ {2} ^ {\prime} + 2} \\ \times \frac {b _ {i} ! b _ {j} ! (2 c _ {i} - 2 c _ {1} ^ {\prime}) ! (2 c _ {j} - 2 c _ {2} ^ {\prime}) !}{(b _ {i} + 2 c _ {i} - 2 c _ {1} ^ {\prime} + 1) ! (b _ {j} + 2 c _ {j} - 2 c _ {2} ^ {\prime} + 1) !}. \end{array}\tag{8.9}
$$

Applying Lemma 8.1 again, we see that

$$
\int_ {\mathcal {R} _ {k - 1}} \dots \int (1 - P _ {1} ^ {\prime}) ^ {b} (P _ {2} ^ {\prime}) ^ {c ^ {\prime}} d t _ {2} \dots d t _ {k} = \frac {b !}{(k + b + c - 1) !} G _ {c, 2} (k - 1).\tag{8.10}
$$

Combining (8.9) and (8.10) gives the result.

We see from Lemma 8.2 that$I _ { k } ( F )$and$\textstyle \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F )$can both be expressed as quadratic forms in the coeficients$\mathbf { a } = ( a _ { 1 } , \ldots , a _ { d } )$of$P .$Moreover, these will be positive definite real quadratic forms. Thus in particular we find that

$$
\frac {\sum_ {m = 1} ^ {k} J _ {k} ^ {(m)} (F)}{I _ {k} (F)} = \frac {\mathbf {a} ^ {T} A _ {2} \mathbf {a}}{\mathbf {a} ^ {T} A _ {1} \mathbf {a}},\tag{8.11}
$$

for two rational symmetric positive definite matrices$A _ { 1 } , A _ { 2 }$, which can be calculated explicitly in terms of k for any choice of the exponents$b _ { i } , c _ { i }$. Maximizing expressions of this form has a known solution.

Lemma 8.3. Let$A _ { 1 } , A _ { 2 }$be real, symmetric positive definite matrices. Then

$$
\frac {\mathbf {a} ^ {T} A _ {2} \mathbf {a}}{\mathbf {a} ^ {T} A _ {1} \mathbf {a}}
$$

is maximized when a is an eigenvector of$A _ { 1 } ^ { - 1 } A _ { 2 }$corresponding to the largest eigenvalue of $A _ { 1 } ^ { - 1 } A _ { 2 }$. The value ofthe ratio at its maximum is this largest eigenvalue.

Proof. We see that multiplying a by a non-zero scalar doesn’t change the ratio, so we may assume without loss of generality that$\mathbf { a } ^ { T } A _ { 1 } \mathbf { a } = 1$. By the theory of Lagrangian multipliers, $\mathbf { a } ^ { T } A _ { 2 } \mathbf { a }$is maximized subject to$\mathbf { a } ^ { T } A _ { 1 } \mathbf { a } = 1$when

$$
L (\mathbf {a}, \lambda) = \mathbf {a} ^ {T} A _ {2} \mathbf {a} - \lambda (\mathbf {a} ^ {T} A _ {1} \mathbf {a} - 1)\tag{8.12}
$$

is stationary. This occurs when (using the symmetricity of$A _ { 1 } , A _ { 2 } )$

$$
0 = \frac {\partial L}{\partial a _ {i}} = ((2 A _ {2} - 2 \lambda A _ {1}) \mathbf {a}) _ {i},\tag{8.13}
$$

for each i. This implies that (recalling that$A _ { 1 }$is positive definite so invertible)

$$
A _ {1} ^ {- 1} A _ {2} \mathbf {a} = \lambda \mathbf {a}.\tag{8.14}
$$

It then is clear that$\mathbf { a } ^ { T } A _ { 1 } \mathbf { a } = \lambda ^ { - 1 } \mathbf { a } ^ { T } A _ { 2 } \mathbf { a }$

Proof of parts (1) and (2) of Proposition 4.3. To establish Proposition 4.3 we rely on some computer calculation to calculate a lower bound for$M _ { k }$. We let F be given in terms of a polynomial P by (8.1). We let P be given by a polynomial expression in$\begin{array} { r } { P _ { 1 } = \sum _ { i = 1 } ^ { k } t _ { i } } \end{array}$and $\begin{array} { r } { P _ { 2 } ~ = ~ \sum _ { i = 1 } ^ { k } t _ { i } ^ { 2 } } \end{array}$which is a linear combination of all monomials$( 1 - P _ { 1 } ) ^ { b } P _ { 2 } ^ { c }$with$b + 2 c \ \leq$ 11. There are 42 such monomials, and with$k = 1 0 5$we can calculate the$4 2 \times 4 2$rational symmetric matrices$A _ { 1 }$and$A _ { 2 }$corresponding to the coeficients of the quadratic forms$I _ { k } ( F )$ and$\textstyle \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F )$. We then find<sup>3</sup> that the largest eigenvalue of$A _ { 1 } ^ { - 1 } A _ { 2 }$is

$$
\lambda \approx 4. 0 0 2 0 6 9 7 \dots > 4.\tag{8.15}
$$

Thus$M _ { 1 0 5 } ~ > ~ 4$. This verifies part (2) of Proposition 4.3. We comment that by taking a rational approximation to the corresponding eigenvector, we can verify this lower bound by calculating the ratio$\textstyle \sum _ { m = 1 } ^ { k } J _ { k } ^ { ( m ) } ( F ) / I _ { k } ( F )$using only exact arithmetic.

For part (1) of Proposition 4.3, we take$k = 5$and

$$
P = (1 - P _ {1}) P _ {2} + \frac {7}{1 0} (1 - P _ {1}) ^ {2} + \frac {1}{1 4} P _ {2} - \frac {3}{1 4} (1 - P _ {1}).\tag{8.16}
$$

With this choice we find that

$$
M _ {5} \geq \frac {\sum_ {m = 1} ^ {k} J _ {k} ^ {(m)} (F)}{I _ {k} (F)} = \frac {1 4 1 7 2 5 5}{7 0 8 2 1 6} > 2.\tag{8.17}
$$

This completes the proof of Proposition 4.3.

## 9. Acknowledgements

The author would like to thank Andrew Granville, Roger Heath-Brown, Dimitris Koukoulopoulos and Terence Tao for many useful conversations and suggestions.

The work leading to this paper was started whilst the author was a D.Phil student at Oxford and funded by the EPSRC (Doctoral Training Grant EP/P505216/1), and was finished when the author was a CRM-ISM postdoctoral fellow at the Universit´e de Montr´eal.

## References

[1] P. D. T. A. Elliott and H. Halberstam. A conjecture in prime number theory. In Symposia Mathematica, Vol. IV (INDAM, Rome, 1968/69), pages 59–72. Academic Press, London, 1970.

[2] J. Friedlander and A. Granville. Limitations to the equi-distribution of primes. I. Ann. of Math. (2), 129(2):363–382, 1989.

[3] D. A. Goldston, S. W. Graham, J. Pintz, and C. Y. Yıldırım. Small gaps between products of two primes. Proc. Lond. Math. Soc. (3), 98(3):741–774, 2009.

[4] D. A. Goldston, J. Pintz, and C. Y. Yıldırım. Primes in tuples. III. On the diference$p _ { n + \nu } - p _ { n }$. Funct. Approx. Comment. Math., 35:79–89, 2006.

[5] D. A. Goldston, J. Pintz, and C. Y. Yıldırım. Primes in tuples. I. Ann. ofMath. (2), 170(2):819–862, 2009.

$^ 3 \mathrm { A n }$ancillary Mathematica <sup>R</sup> file detailing these computations is available alongside this paper at www.arxiv.org.

[6] D. A. Goldston and C. Y. Yıldırım. Higher correlations of divisor sums related to primes. III. Small gaps between primes. Proc. Lond. Math. Soc. (3), 95(3):653–686, 2007.

[7] D. H. J. Polymath. A new bound for gaps between primes. Preprint.

[8] A. Selberg. Collected papers. Vol. II. Springer-Verlag, Berlin, 1991. With a foreword by K. Chandrasekharan.

[9] Y. Zhang. Bounded gaps between primes. Ann. of Math.(2), to appear.

Centre de recherches mathematiques´ , Universite de´ Montreal´ , Pavillon Andre´-Aisenstadt, 2920 Chemin

de la tour, Room 5357, Montreal´ (Quebec´ ) H3T 1J4 E-mail address: maynardj@dms.umontreal.ca