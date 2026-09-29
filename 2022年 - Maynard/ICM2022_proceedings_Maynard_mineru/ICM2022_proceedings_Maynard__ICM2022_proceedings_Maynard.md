# Counting primes

James Maynard

## Abstract

We survey techniques used to detect prime numbers in sets, highlighting the strengths and limitations of current techniques.

Mathematics Subject Classification 2020 Primary 11N05; Secondary 11N35, 11M06, 11N13

Keywords Prime numbers,sieve methods,Type I/II sums

## 1. Introduction

Many of the most notorious open problems about prime numbers can be phrased as variations of the following question.

Question. Given a set ofintegers A, how many primes are in$\mathcal { A } ?$

Depending on the context, ‘how many’ could be asking whether there exists at least one prime in A, whether there are infinitely many primes in A, or asking for a quantitative estimate for the number of primes up to some threshold.

For example, we have the following special cases:

$\mathcal { A } = \mathbb { Z }$. That there are infinitely many primes in A follows from Euclid’s proof of the infinitude of primes. An asymptotic formula for the primes in A less than � is given by the Prime Number Theorem, and asking for the smallest possible error term in such an asymptotic estimate is essentially a reformulation of the Riemann Hypothesis.

$\mathcal { A } = \{ p + 2 : p$prime}. Asking for infinitely many primes in A is the famous Twin Prime Conjecture, and an asymptotic formula for the number of primes in A is a conjecture of Hardy and Littlewood.

$\mathcal { A } = \{ 2 N - p : p$prime}, for some fixed integer$N \geq 2$. In this case A contain only a finite number of positive elements (and so a finite number of primes), but asking that it contains at least one prime for every$N \geq 2$is Goldbach’s conjecture.

The final two examples are two of Landau’s influential four problems on primes listed in his 1912 ICM address; all four remain unsolved.

In general we will focus on situations where we expect (from heuristics, numerical evidence, or other guesswork) that there should be primes in A, and the task is to try to prove this is indeed the case.

We know of no way to construct prime numbers theoretically, and therefore we typically need to use an indirect method to prove the existence of primes in a given set A. If we are unable to numerically test elements, then often the only way we know how to prove the existence of a single prime in a set A is to perform the a priori harder task of approximately counting the number of primes in A and showing there are many primes in A of a given size. For example, Vinogradov’s three primes theorem states that every suficiently large odd number can be written as the sum of three primes (this is now actually known for all$N \geq 7$ thanks to work of Helfgott [42]), but the only way we know how to prove this actually shows that there are ‘many’ ways to write a large odd integer � as the sum of three primes.

The ultimate goal in this area is to develop a flexible toolkit which can reduce the question of counting primes in sets A of interest to easier (but more technical) questions about the arithmetic structure of the set in question, and then to have a set of techniques which can investigate these questions.

## 2. Multiplicative number theory

Multiplicative number theory rests on utilising the following crucial property of the primes, which is essentially the Fundamental Theorem of Arithmetic.

Property. Prime numbers generate the positive integers via multiplication

This property allows us to define suitable multiplicative generating functions$( L -$ functions) which encode properties of the primes via the integers they generate. A reformulation of the Fundamental Theorem of Arithmetic is the identity (for$\operatorname { R e } ( s ) > 1 )$)

$$
\zeta (s) = \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {s}} = \prod_ {p} \left(1 - \frac {1}{p ^ {s}}\right) ^ {- 1}.
$$

Since we analytically understand the integers under addition quite well, we can obtain a good understanding (analytic continuation, controlled growth) of$\zeta ( s )$via the Dirichlet series representation on the left hand side. This understanding can then be translated into understanding about the primes. The infinitude of the primes follows from the fact that$\zeta ( s )$has a pole at $s = 1$, the Prime Number Theorem follows from (and is essentially equivalent to) the fact that $\zeta ( s )$has no zeros on the line$\operatorname { R e } ( s ) = 1$, and precise estimates for the count of primes are essentially equivalent to zero-free regions for$\zeta ( s )$within the critical strip$0 < \operatorname { R e } ( s ) < 1$ In all these cases the partial information we are interested in about primes becomes much easier to establish via translating it to a question about partial understanding of$\zeta ( s )$

Moreover, the techniques of multiplicative number theory extend well beyond just studying primes via$\zeta ( s )$, but to a whole zoo of diferent �-functions which encode diferent algebraic information about primes. Prime ideals generate all ideals of the ring of integers of a number field, and so prime ideals (and hence the splitting of rational primes) can be studied via the same techniques via Dedekind �-functions$\zeta _ { K } ( s )$(the analogue of$\zeta ( s )$for a number field �). Moreover, one can twist the$\zeta ( s )$by a Dirichlet character or the Archimedean character$n ^ { i t }$, or one can twist$\zeta _ { K } ( s )$by a Hecke character (or more generally twist an �-function by a suitable automorphic representation), to obtain further �-functions, which can study primes in arithmetic progressions, short intervals, the locations of prime ideals in lattices or similar questions.

Essentially the only method we have which is capable of ‘producing’ primes is using multiplicative number theory. Even though there are now a few ostensibly diferent proofs of the Prime Number Theorem, all known proofs rely fundamentally on the Fundamental Theorem of Arithmetic, and require multiplicative structure. Virtually all other results counting primes can be thought of as extensive elaborate manoeuvres which allow one to reduce to the situation of using multiplicative number theory to count primes.

## 2.1. Primes and zeros

The techniques of multiplicative number theory crucially allow one to understand multiplicative questions on the distribution of primes via the zeros of the corresponding �- functions. The duality between primes and zeros of$\zeta ( s )$is best seen through Riemann’s famous Explicit Formula for$\zeta ( s )$: for$x , T \geq 2$

$$
\sum_ {n <   x} \Lambda (n) = x - \sum_ {| \rho | <   T} \frac {x ^ {\rho}}{\rho} - \log (2 \pi \sqrt {1 - x ^ {- 2}}) + O \Big (\frac {x (\log x) ^ {3}}{T} \Big),\tag{2.1}
$$

where$\Lambda ( n )$is the Von-Mangold function and the sum is over all non-trivial zeros$\rho$of$\zeta ( s )$ (counted with multiplicity, although all zeros are believed to be simple). For every �-function (satisfying the expected meromorphicity and growth conditions) we get a corresponding explicit formula with one side representing primes and the other zeros of the �-function

The explicit formula points to unexpected deep structure within the sequence of primes; if the Riemann Hypothesis$( \mathrm { R e } ( \rho ) = 1 / 2$for all$\mathrm { \ n o n - t r i v i a l } \rho )$holds, then treating all terms apart from � trivially, we would obtain a smaller size error term than we would expect based on simple random model predictions (we expect that the presence of zeros alters efects such as the law of the iterated logarithm, for example). Indeed, the zeros of$\zeta ( s )$constrain the error term in the count of primes to fluctuate relatively less than we expect for other arithmetic sequences (such as twin primes) where we expect ‘random-like’ behaviour. Another example where this structure plays a role is the fact that the error term in the Prime Number Theorem can be self-improving; if we can show that

$$
\left| \pi (x) - \int_ {2} ^ {x} \frac {d t}{\log t} \right| \ll x ^ {1 / 2 + o (1)},
$$

then we know that the Riemann Hypothesis holds and the error term$x ^ { 1 / 2 + o ( 1 ) }$can be upgraded to the more precise$O ( x ^ { 1 / 2 } \log x )$. It would be interesting to see if the structure implied by zeros can be exploited meaningfully in other ways.

Similarly, since the error term in (2.1) disappears as$T \to \infty$, we see that knowing all zeros encodes all information about primes, and vice-versa. This observation is useless for most practical purposes, but it means that zeros of$\zeta ( s )$must also encode the distribution of primes in arithmetic progressions, and therefore encode information about zeros of Dirichlet �-functions too. This is partial justification for the idea that �-functions should be studied in families rather than individually. A spectacular example of this is Goldfeld and Gross-Zagier’s [29, 30, 34] joint resolution of the Gauss class number one problem by showing that an �-function attached to a suitable Elliptic curve had a triple zero at the central point, and this triple zero had a suitably strong influence on zeros of Dirichlet �-functions to prevent there being any particularly bad Siegel zeros.

## 2.2. Zero density estimates

Although the Riemann Hypothesis is the most important question for any given$L -$ function, often it would sufice for applications to primes to show a much weaker statement that ‘most’ zeros lie ‘close’ to the line$\operatorname { R e } ( s ) = 1 / 2$, rather than requiring that all zeros lie on this line. For example, under the Riemann Hypothesis we can show an asymptotic formula for primes in$[ x , x + x ^ { 1 / 2 } ( \log x ) ^ { 2 } ]$. If we let$N ( \sigma , T )$denote the number of zeros$\rho = \beta + i \gamma$ with$| \gamma | \le T$and$\beta \geq \sigma$then a bound$N ( \sigma , T ) \ll T ^ { 2 - 2 \sigma + o ( 1 ) }$(known as the ‘Density Hypoth esis’) would allow us to deduce an asymptotic formula for primes in$[ x , x + x ^ { 1 / 2 + o ( 1 ) } ]$, which is almost as short as what we obtain under the Riemann Hypothesis. Unfortunately the Density Hypothesis is open in general, but a classical result of Huxley [44] shows$N ( \sigma , T ) \ll$ $T ^ { 1 2 ( 1 - \sigma ) / 5 + o ( 1 ) }$, which implies an asymptotic formula for the number of primes in$[ x , x +$ $x ^ { 7 / 1 2 + o ( 1 ) } ]$, and is essentially the best known result (Heath-Brown [36] used sieve methods to remove the$o ( 1 ) . )$

In many counting problems for the primes which are directly related to zeros, the limitation in our results is due to a limitation in our understanding of zeros near the 3/4-line (such as the example above of primes in short intervals), or near the 1-line (such as issues with Siegel zeros or the least quadratic non-residue). For example, if we knew that there were no zeros$\rho$with$0 . 7 4 \leq \mathrm { R e } ( \rho ) \leq 0 . 7 6$(or if there were ‘few’ such zeros), then we would improve on our understanding of primes in short intervals. The typical way to bound such zeros is to detect them via large values of a Dirichlet polynomial (see [47, Chapter 10]). The key limitation of our zero density estimates for the past 50 years reduces to the following question.

Question 1. Can we show

$$
\operatorname{meas} \left\{t \in [ T, 2 T ]: \left| \sum_ {n = T ^ {2 / 5}} ^ {2 T ^ {2 / 5}} n ^ {i t} \right| > T ^ {1 / 1 0} \right\} \ll T ^ {3 / 5 - \delta}
$$

for somefixed positive constant$\delta ?$

The bound$T ^ { 3 / 5 + o ( 1 ) }$follows quickly from straightforward bounds for the$4 ^ { t h }$or$6 ^ { t h }$ mean value of the Dirichlet polynomial. Improving on the$6 ^ { t h }$moment bound is related to bounding the$6 ^ { t h }$moment of$\zeta ( 1 / 2 + i t )$, but it is not unreasonable to hope that this question might be easier to study.

Even if we cannot improve our current zero-density bounds on the number of zeros, an alternative approach might be to see what this might imply for the distribution of zeros of $\zeta ( s )$. (Ultimately one might hope to obtain a putative classification which either contradicts other known properties or demonstrates that there are still primes in short intervals with this distribution of zeros.)

Question 2. Imagine that$| \pi ( x + x ^ { 7 / 1 2 - \epsilon } ) - \pi ( x ) - x ^ { 7 / 1 2 - \epsilon } / \log x | \gg x ^ { 7 / 1 2 - \epsilon }$/log�for some large �. What does this imply about the distribution ofthe zeros of$\zeta ( s ) ?$

We know that there must be roughly$T ^ { 3 / 5 }$zeros of height � with real part very close to$3 / 4$for$T \approx x ^ { 5 / 1 2 }$, and moreover it must be the case that these zeros$\rho = \beta + i \gamma$have the fact that the fractional part of$2 \pi \gamma$log � is quite strongly biased modulo 1. Moreover, we speculate that there should be much more prescriptive constraints on the vertical distribution such zeros - roughly that they occur in small clusters whose imaginary parts are roughly in an arithmetic progression. Obtaining a precise classification of this sort seems dificult (it appears related to the inverse Littlewood problem in additive combinatorics/harmonic analysis), but a suitably strong classification would open up a new manner to potentially rule out conspiracies preventing primes in short intervals. A proof-of-concept in this direction is recent work with Pratt .

Theorem 3 (Conditional improvement to zero density estimates). Assume that the zeros of �(�) lie onfinitely many vertical lines. Then

$$
\# \{p \in [ x, x + x ^ {1 3 / 2 4 + \epsilon} ] \} = (1 + o _ {\epsilon} (1)) \frac {x ^ {1 3 / 2 4 + \epsilon}}{\log x}.
$$

The point here is that the hypothesis still allows for the possibility of vertical arithmetic progressions of zeros, and so one of the potential limitations is actually less of an issue. We can obtain improvements on the classical exponent 7/12 (and improvements on zero-density estimates) by studying the vertical patterns of zeros of �(�), albeit under rather strong assumptions.

In a very diferent direction, following work of Matomäki-Radziwiłł [54], if one is interested in the Möbius function (and is happy with weaker quantitative bounds), then we can restrict attention to Dirichlet polynomials which factor in many ways (expanding on earlier ideas of [10], [49] and [8]). This allows one to overcome the issues raised here for primes, and obtain stronger results about the Möbius function in short intervals [56] as well as almost-all short intervals [54].

## 2.3. Limits to multiplicative techniques

In general the multiplicative theory for counting primes points to a rich structure encoded by the zeros and a powerful set of techniques. Unfortunately there are some issues with this from a practical point of view:

(1) Multiplicative techniques rely on the presence of multiplicative structure in the problem. In situations which are less structured (particularly when there is addition polluting multiplicative objects like in the Twin Prime Conjecture), we do not know how to make use of multiplicative techniques. Even when they can be of use, it require a lot of work to massage problems into a suitable form that the powerful multiplicative techniques can apply to.

(2) In the absence of the conjectured strong control over zeros, our estimates are often limited in their range of applicability, particularly with uniformity of esti mates with respect to underlying parameters such as conductor or degree of number field.

(3) The multiplicative methods tend to either give strong asymptotic formulae or fai to give any non-trivial bound whatsoever. The strength of the analytic approach means that it is not well-suited to answering ‘soft’ questions with a wide degre of flexibility.

As an example of the final two points, Hooley’s [43] proof of the Artin primitive root conjecture under the Generalised Riemann Hypothesis for suitable Dedekind �-functions relied crucially on the upper bound

$$
\sum_ {q \sim Q} \pi^ {*} (x; q) \ll \frac {x}{Q \log x} + Q x ^ {1 / 2} (\log x) ^ {O (1)},
$$

where$\pi ^ { * } ( x ; q )$counts primes$p < x$with$p \equiv 1$(mod �) and for which 2 is a$q ^ { t h }$power (mod �). (In fact, an upper bound of the form$\scriptstyle o _ { Q \to \infty } ( \pi ( x ) )$for$Q < x ^ { 1 / 2 } ( \log x ) ^ { - A }$would have suficed.) The only way we know how to prove an upper bound of this type is by proving an asymptotic formula of the form$\pi ^ { * } ( x ; q ) = \pi ( x ) / ( q \varphi ( q ) ) + O ( x ^ { 1 / 2 } \log x )$via GRH, which is a much stronger statement. Unconditional techniques based on multiplicative number theory can capture the condition of being a$q ^ { t h }$power, but only with error terms that degrade quickly with �. (By contrast, other techniques such as sieve methods can be very flexible at producing upper bounds, but appear poorly suited to capturing the more algebraic$q ^ { t h }$power condition.)

Question 4. Can oneproduce a non-trivial upper boundfor${ \scriptstyle \sum _ { q \sim x ^ { 1 / 2 - \epsilon } } } \pi ^ { * } ( x ; q )$uncondition$a l l y ?$

## 3. Sieve methods

Sieve methods take a diferent, combinatorial approach to studying primes, based on the following simple property:

Property. Primes are integers � which have no divisors smaller than$\sqrt { n }$other than 1.

Thus primes are examples of numbers with no small divisors, and more generally one can look at integers � with no divisors (other than 1) less than some quantity �. This formulation naturally suggests that one can count such numbers in a set A via inclusionexclusion:

$$
\sum_{\substack{n\in \mathcal{A}\\ p|n\Rightarrow p > z}}1 = \sum_{\substack{d\\ p|d\Rightarrow p\leq z}}\mu (d)\sum_{\substack{n\in \mathcal{A}\\ d|n}}1.
$$

Let us restrict attention from now on to sets$\mathcal { A } \subseteq [ x , 2 x ]$for some large value �, so that all elements have roughly the same size.

Unfortunately even if one had very good estimates for the size of the set${ \mathcal { A } } _ { d }$of multiples of � in$\mathcal { A } \subset [ x , 2 x ]$, there would be$2 ^ { \pi ( z ) }$diferent integers � in the sum and so any error terms would accumulate and dominate the hope of a main term unless � was very small (such as if$z \leq \log x )$. The first key insight in of sieve methods is that one can use positivity to truncate the inclusion-exclusion process and avoid the presence of$d \mathrm { { s } }$which are too large, at the cost of a small amount of precision. The basic arithmetic information required to make this work is then a moderate understanding of inner sums above, namely the size of the sets $\mathcal { A } _ { d } = \{ n \in \mathcal { A } : d | n \}$

Let$g ( d )$be a multiplicative function which we think of as an approximation to the density of elements of A which are a multiple of �. We assume that$g ( p ) < 1 - \epsilon$(so that there are no prime factors which are too common) and that$g ( p ) \approx \kappa / p$for some fixed constant $\kappa > 0$on average by assuming for$2 \leq w$

$$
\sum_ {p \leq w} g (p) \log p = \kappa \log w + O (1).\tag{3.1}
$$

The key arithmetic input for sieve methods is then an estimate for every$A > 0$

$$
\sum_ {d <   x ^ {\gamma}} | \# \mathcal {A} _ {d} - g (d) \# \mathcal {A} | \ll_ {A} \frac {\# \mathcal {A}}{(\log x) ^ {A}}\tag{3.2}
$$

for some given fixed$\gamma > 0$. The larger we are able to take �, the better we are able to understand $\mathcal { A }$in arithmetic progressions and the more powerful the conclusions of our sieve methods will be. In most situations of interest we expect (3.2) to hold for a suitable function$g$and reasonably large constant$\gamma \in ( 0 , 1 )$, so (3.2) should be thought of as a reasonably mild constraint when$\gamma$is small.

The basic point of sieve methods is that for any set which does satisfy an estimate like (3.2) we can make the inclusion-exclusion argument much more accurate. This is known as the ‘fundamental lemma’ (see, for example, [28, Corollary 6.10]).

Lemma 5 (Fundamental Lemma of Sieve Methods). Let � be a multiplicative function as above. Then we havefor any$\eta , \gamma > 0$

$$
\sum_{\substack{n\in \mathcal{A}\\ p|n\Rightarrow p > x^{\eta}}}1 = (1 + O_{\kappa}(e^{-\gamma /\eta}))\prod_{p\leq x^{\eta}}\Big(1 - g(p)\Big)\# \mathcal{A} + O(E),
$$

where

$$
E = \sum_ {d <   x ^ {\gamma}} \left| \# \mathcal {A} _ {d} - g (d) \# \mathcal {A} \right|.
$$

One should think of the case when$\mathcal { A }$satisfies (3.2) with some fixed$\gamma > 0$, and$\eta$is taken as a suficiently small fixed constant. The key point of the fundamental lemma is then that one can still obtain good asymptotic estimates for the number of elements in A with no prime factors less than � even when$z$is as large as$x ^ { \eta }$, provided we have a relatively modest estimate for the distribution of$\mathcal { A }$in arithmetic progressions.

An immediate consequence is that$\mathcal { A }$contains$O ( \# \mathcal { R } / ( \log x ) ^ { \kappa } )$primes, and we expect that in most situations this should be the correct order of magnitude for the number of primes in${ \mathcal { A } } .$For example, returning to some of Landau’s problems mentioned in Section 1, we find that there are$O ( x / ( \log x ) ^ { 2 } )$twin primes less than �, and that there are$O ( x ^ { 1 / 2 } / \log x )$ prime values of$n ^ { 2 } + 1$which are less than �, and both estimates are conjectured to be sharp up to the multiplicative constant. We also immediately obtain that$\mathcal { A }$contains ‘many’ elements with a bounded number of prime factors as soon as it satisfies something like (3.2). The fact that sieve methods can very flexibly give upper bounds of the right order of magnitude in a wide variety of situations is a very valuable fact when used inside more complicated arguments.

The fundamental lemma essentially produces optimal bounds (with care, the$O _ { \kappa } ( e ^ { - \gamma / \eta } )$ error term can usually be handled satisfactorily), and so the sieving process of ‘small’ primes less than$x ^ { \eta }$is almost perfect, and as if the small primes were behaving independently of one another. This can therefore also be used just as a preliminary sieving stage, where we first remove all ‘small’ prime factors$\leq x ^ { \eta }$perfectly via an application of the Fundamental Lemma, leaving us to be more careful in trying to handle the about the${ \cal O } ( 1 / \eta )$‘large’ prime factors (bigger than$x ^ { \eta } )$of elements of$\mathcal { A }$. Although the behaviour of the small primes is

essentially that of independence and the same for all sets A satisfying (3.2), the distribution of the large prime factors in general will vary according to the set. Understanding how much control we have on these large prime factors from (3.2) is still something of a poorly understood art in general, and often the best sieving procedure is tailored to the question at hand.

## 3.1. Arranging the large prime factors

In general, for any set A satisfying (3.2), and � suficiently large we will have that

$$
\sum_{\substack{n\in \mathcal{A}\\ p|n\Rightarrow p\geq x^{\eta}}}1\leq \Big(F(\kappa ,\eta ,\gamma) + o(1)\Big)\# \mathcal{A}\prod_{p\leq x^{\eta}}\Big(1 - g(p)\Big),\\ \sum_{\substack{n\in \mathcal{A}\\ p|n\Rightarrow p\geq x^{\eta}}}1\geq \Big(f(\kappa ,\eta ,\gamma) + o(1)\Big)\# \mathcal{A}\prod_{p\leq x^{\eta}}\Big(1 - g(p)\Big),
$$

for some functions$0 \le f ( \kappa , \eta , \gamma ) \le F ( \kappa , \eta , \gamma )$depending only on the constant � in (3.2), th ‘sieve dimension’ � from (3.1) and from the sieving threshold of$x ^ { \eta }$

When$\kappa = 1$(the most common sieving situation) we are in the situation of the ‘linear sieve’ , somewhat remarkably we know the optimal values of the functions.

Lemma 6 (Optimality of the linear sieve). Let � satisfy (3.1) with$\kappa = 1$and$g ( p ) < 1 - \epsilon$ Then there arefunctions$F ( s ) , f ( s )$such that we have thefollowing.

(1) For any set A satisfying (3.2), we have

$$
\sum_{\substack{n\in \mathcal{A}\\ p|n = p\geq x^{\eta}}}1\leq \Big(F(\gamma /\eta) + o(1)\Big)\# \mathcal{A}\prod_{p\leq x^{\eta}}\Big(1 - g(p)\Big),\\ \sum_{\substack{n\in \mathcal{A}\\ p|n = p\geq x^{\eta}}}1\geq \Big(f(\gamma /\eta) + o(1)\Big)\# \mathcal{A}\prod_{p\leq x^{\eta}}\Big(1 - g(p)\Big).
$$

(2) There are sets$\mathcal { A } ^ { + } , \mathcal { A } ^ { - } \subseteq [ x , 2 x ]$which satisfy (3.2) and$g ^ { \pm }$which satisfy (3.1) and$g ^ { \pm } ( p ) < 1 - \epsilon$such that

$$
\sum_{\substack{n\in \mathcal{A}^{+}\\ p|n\Rightarrow p\geq x^{\eta}}}1 = \Big(F(\gamma /\eta) + o(1)\Big)\# \mathcal{A}^{+}\prod_{p\leq x^{\eta}}\Big(1 - g^{+}(p)\Big),
$$

$$
\sum_{\substack{n\in \mathcal{A}^{-}\\ p|n\Rightarrow p\geq x^{\eta}}}1 = \Big(f(\gamma /\eta) + o(1)\Big)\# \mathcal{A}^{-}\prod_{p\leq x^{\eta}}\Big(1 - g^{-}(p)\Big).
$$

This technical looking statement says that for any A satisfying a linear sieving problem, we know the optimal upper and lower bounds for the number of sieved elements of the set, based purely on the distribution of A in arithmetic progressions to modulus$x ^ { \gamma }$. We can take$\mathcal { A } ^ { \pm } = \left\{ n \in [ x , x + x ^ { \gamma + \epsilon } : \lambda ( n ) = \mp 1 \right\}$and$g ^ { \pm } ( p ) = 1 / p$, where$\lambda ( n )$is the Liouville function$( \lambda ( n ) = - 1$if � has an odd number of prime factors, and$\lambda ( n ) = 1$otherwise) and this gives the functions$F , f ,$, which can be written explicitly as solutions to a delay-diferential equation. Thus for the basic problem of understanding the consequences of (3.2), we have an essentially complete answer.

Although the linear sieve is essentially optimal, when the sieving dimension is greater than one we have a much poorer understanding of optimality and what we can hope to achieve. The linear sieve bounds are proven using a ‘combinatorial sieve’, and combinatorial sieves tend to produce the best bounds when � is reasonably small. When � gets larger, however, it typically turns out that Selberg’s sieve performs better. However, in no circumstance do we have anything like the complete understanding of the picture that we would like.

Question 7. What are the optimal sieve functions for high-degree sieves? What do the extremal sets look like?

For example, the upper bound for the number of prime �-tuplets less than � is larger than the expected truth by$2 ^ { k } k !$. Although the parity phenomenon would prevent us from obtaining a bound smaller than$2 ^ { k }$times the expected truth, it is very unclear what sort of bound an optimal �-dimensional sieve could hope to prove in this situation. The key innovation in [61] was a new high-dimensional variant of Selberg’s sieve tailored to the application at hand, which allowed for notable progress on the sieving problem of bounded gaps between primes (see Section 4). Although this doesn’t appear to help with the direct upper and lower bounds, it indicates that there is potentially a lot left to be understood about high-dimensional sieves.

Question 8. What other arithmeticfeatures ofsets A ofinterest can be exploited to produc improved sieving bounds?

If there is extra arithmetic information which could distinguish sets A from extremal sets, this could then be incorporated into the sieving assumptions to hopefully produce better bounds.

For example, Chen’s twist [9] was a key innovation used by Chen to show that there are infinitely many primes$p$with$p + 2$having at most two prime factors, and this exploited the fact that the situation could be viewed as fixing the prime factorisation of either � of$n + 2$ and viewing it as a sieve problem to produce bounds which are better than what the standard linear sieve would imply. High dimensional sieves often have similar features where they can be viewed as (� − 1)-dimensional sieving problems or �-dimensional ones, and mixing these perspectives allows one to do slightly better than typical situations [60]. In a diferent direction, the ‘interval sieve’ asks for bounds when we know that A is just an interval - it is known in this case [18,31] that the optimal sieve functions are closely linked to the presence of Siegel zeros, and so in many situations this limits what we can hope to achieve.

## 3.2. Limitations of sieve methods and the parity phenomenon

We saw above that the extremal sets$\mathcal { A } ^ { \pm }$for the linear sieve were given in terms of numbers with an odd or even number of prime factors. This is an example of a fundamental limitation of sieve methods based purely on arithmetic information of the from (3.2): the parity phenomenon. Roughly, this says that sieve methods cannot distinguish between numbers with an even number of prime factors and an odd number of prime factors.

For example, all sieve upper and lower bounds are based on using sieve weights which are short divisor sums

$$
w_{n} = \sum_{\substack{d|n\\ d <   x^{\gamma}}}\lambda_{d}.
$$

Thus, recalling that$\lambda ( n ) = - 1$if� has an odd number ofprime factors, and$\lambda ( n ) = 1$otherwise, we see

$$
\sum_{n\in \mathcal{A}}w_{n}\Big(\frac{1\pm\lambda(n)}{2}\Big) = \frac{1}{2}\sum_{n\in \mathcal{A}}w_{n} + O\Big(\sum_{d <   x^{\gamma}}|\lambda_{d}| \Big|\sum_{\substack{n\in \mathcal{A}\\ d|n}}\lambda (n)\Big|\Big).
$$

For most sets$\mathcal { A }$of interest, it is believed that the inner sums on the right had side should always be very small, meaning that the same total weight is put on numbers with an even number of prime factors as those with an odd number of prime factors (although actually proving this is almost as hard as proving an asymptotic formula for primes in A).

Because the weight is equidistributed between numbers with an even and an odd number of prime factors, it means that any upper bound sieve for primes will be of by a factor of at least 2 (the weight placed upon primes can be at most the total weight of numbers with an odd number of prime factors, which in turn is at most half the total weight). It also means that we cannot hope to obtain a non-trivial lower bound for the number of primes in a set A by just using pure sieve methods.

In various situations, this elementary loss of a factor of 2 from sieve methods is intimately linked to the possible presence of Siegel zeros (which would cause certain residue classes to have double the expected number of primes of a certain size.) For example, the Brun-Titchmarsh Theorem [69] (proven using sieve methods), states that

$$
\pi (x; q, a) \leq \frac {2 x}{\varphi (q) \log (x / q)}.
$$

When � is fairly large relative to �, this is of by a factor of roughly 2 from the expected asymptotic, but improving the constant 2 to$2 - \delta$in this regime would rule out the possibility of a Siegel zero.

## 4. Side-stepping limitations of sieve methods

Although sieve methods alone cannot directly produce primes, sometimes this apparent limitation can be sidestepped. For example, consider the following result ([61, 62, 71, 82] and unpublished work of Tao).

Theorem 9 (Bounded gaps between primes). Let � be a positive integer. Then

$$
\liminf _ {n} (p _ {n + k} - p _ {n}) <   \infty
$$

In the special case when$k = 1$, we can take the finite constant to be 246; for general $k$we can take the bound to be$O ( e ^ { 3 . 8 1 5 k } )$thanks to work of Baker-Irving [3].

This result manifestly says something about prime numbers, but ultimately only relies on arithmetic information of the form (3.2), in this case the Bombieri-Vinogradov

Theorem. The reason this result isn’t prevented from saying something by the parity phenomenon is because it sidesteps some of the issues via the pigeonhole principle, which then avoids the need to specify exactly which quantities are taking prime values. More specifically, the proof of Theorem 9 relies on considering the quantity

$$
S = \sum_ {n \sim x} \Bigl (\sum_ {i = 1} ^ {K} \mathbf {1} _ {\mathbb {P}} (n + h _ {i}) - k \Bigr) w _ {n}
$$

for some suitable fixed constants$h _ { 1 } < . . < h _ { K }$(chosen such that$\textstyle \prod _ { i = 1 } ^ { K } ( n + h _ { i } )$is not always a multiple of a fixed prime$p )$and some non-negative sieve weight$w _ { n }$tailored to the situation at hand. Since$w _ { n } \geq 0$, showing that$S > 0$implies that there is some$n \sim x$for which at least $k + 1$of$n + h _ { 1 } , \ldots , n + h _ { K }$are simultaneously prime, and hence there are$k + 1$primes all contained in an interval of length$h _ { K } - h _ { 1 }$. The fact that we do not have any control over which of the diferent$n + h _ { i }$are prime, merely the fact that several of them are prime is what allows us to sidestep the parity phenomenon issue.

Another example of proving the existence of primes in a set by sidestepping the usual obstacles is due to Elkies [15].

Theorem 10 (Elkies’ Theorem). Let$E / \mathbb { Q }$be an elliptic curve. Then there are infinitely many supersingular primesfor �.

The proof actually only relies on Dirichlet’s theorem on primes in arithmetic progressions; all the non-trivial content of the proof is showing that there are polynomials$P _ { \ell }$ encoding$E _ { p }$having complex multiplication by a suitable order (this happens if$p$divides the numerator of$P _ { \ell } ( j ( E ) )$and −ℓ is a quadratic non-residue (mod �)). Carefully choosing a sequence of$\ell { \boldsymbol { \mathrm { s } } }$then shows that there must be infinitely many distinct such$p ^ { \prime } \mathbf { s }$. Thus this is an example where we started with what seemed a dificult counting problem, but by focusing on a special subsequence we were able to reduce to a much counting problem for primes.

One result about primes which relies on sieving procedures but is not directly limited by the parity phenomenon is that of large gaps between primes. In this case it is again fruitful to focus on a special case; if we have a long string of consecutive integers$n , n + 1 , \ldots , n + y$ all with a small prime factor$\leq ( \log n ) / 2$, then certainly we have a long gap between primes. The fact we only search for factors ≤ log � limits our approach (we expect we cannot find gaps between primes less than � bigger than$( \log x ) ( \log \log x ) ^ { 2 + o ( 1 ) }$in this way), but enables us to understand the situation by looking at � in residue classes (mod$\textstyle \prod _ { p \leq ( \log x ) / 2 } p )$, and choosing a convenient residue class to make all the consecutive integers composite. This indirect approach therefore allows us to avoid directly counting primes. The current record is [19,20,63]

Theorem 11 (Large gaps between primes).

$$
\sup _ {p _ {n} \leq X} (p _ {n + 1} - p _ {n}) \gg \frac {(\log x) (\log \log x) (\log \log \log \log x)}{\log \log \log x},
$$

This improves upon an old bound of Erdős-Rankin [17, 72]. The key input for this bound was a version of Theorem 9 showing the existence of certain residue classes containing unusually many small primes - this exploited the fact that sieve results (when successful) ar often very flexible and uniform with respect to other parameters.

The parity phenomenon issue applies equally to estimating primes or estimating sums involving the Liouville function$\lambda ( n )$. It is therefore somewhat remarkable that Tao [74] was able to avoid this for the 2-point Chowla conjecture.

Theorem 12 (Logarithmically average 2-point Chowla).

$$
\sum_ {n <   x} \frac {\lambda (n) \lambda (n + 1)}{n} = o (\log x)
$$

The key property that is exploited here is the multiplicativity of$\lambda ;$by using$\lambda ( n p ) =$ $- \lambda ( n )$and averaging over small primes$p _ { \cdot }$, the problem is turned from a binary problem (which we might expect to be limited by the parity phenomenon) to a ternary one (where we might hope to use a version of the circle method and not be limited by the parity phenomenon). Unfortunately the subsequent steps appear only able to handle very small primes$p ,$, which appears to stop this idea applying to questions about the primes.

## 5. Primes in arithmetic progressions and extending the level of distribution

Most results using sieve methods rely crucially on an estimate of the form (3.2), and the strength of the final results is determined by how large we can take the constant$\gamma$to be. Natural questions are how far we can push the constant$\gamma$for a given set${ \mathcal { A } } ,$, and whether we really need the full strength of (3.2) or whether we can produce a weaker, but more technical result which would still sufice for intended applications.

How far we can extend these estimates naturally depends on the particular set$\mathcal { A }$ in question. For simplicity we will focus on the case when$\mathcal { A }$is closely related to the set of primes (A could be shifted primes, like in the Twin Prime problem, for example) since this is a common case which appears regularly. In this situation, (3.2) is asking us to understand primes in arithmetic progressions, and typically the basic tool used is the Bombieri-Vinogradov Theorem [4,77].

Theorem 13 (Bombieri-Vinogradov Theorem). Let$\epsilon , A > 0 .$. Then we have

$$
\sum_ {q \leq x ^ {1 / 2 - \epsilon}} \sup _ {(a, q) = 1} \left| \pi (x; a, q) - \frac {\pi (x)}{\varphi (q)} \right| \ll_ {\epsilon , A} \frac {x}{(\log x) ^ {A}}.
$$

This asserts that the set of primes shifted by a constant satisfies a strong form of (3.2) for any$\gamma < 1 / 2$. From the point of view of sieve methods (where we typcially only need estimates ‘on average’ over arithmetic progressions) this is typically an unconditional substitute for the Generalised Riemann Hypothesis. We expect, however, that one should be able to go much further [16].

Conjecture 1 (Elliott-Halberstam Conjecture). Let$\epsilon , A > 0$. Then we have

$$
\sum_ {q \leq x ^ {1 - \epsilon}} \sup _ {(a, q) = 1} \left| \pi (x; q, a) - \frac {\pi (x)}{\varphi (q)} \right| \ll_ {\epsilon , A} \frac {x}{(\log x) ^ {A}}.
$$

Increasing the arithmetic information available to the sieve method in question naturally produces stronger results; under the Elliott-Halberstam conjecture. For example, the bound 246 of the case$k = 1$of Theorem 9 can be improved to 12 [61], and we can obtain an upper bound for twin primes which is a factor of only 2 larger than the expected truth.

Unfortunately in this formulation we do not know how to extend the Bombieri-Vinogradov Theorem to moduli beyond$x ^ { 1 / 2 }$- this is often known as the ‘square-root barrier’, and the dificulty of the problem increases dramatically at this point where it goes beyond the region of the Generalised Riemann Hypothesis. However, if we ask for a slightly more technical version of these results on primes in arithmetic progressions, then one can do better. The pioneering work of Fouvry and Bombieri-Friedlander-Iwaniec [5–7,22] produced various results accounting for moduli as large as$x ^ { 4 / 7 - o ( 1 ) }$. This was recently extended [58] to larger moduli still.

Theorem 14 (Beyond$x ^ { 1 / 2 }$barrier for nice coeficients). Let$\lambda ( n )$be ‘triply wellfactorable and$\epsilon , A > 0$. Then we have

$$
\sum_ {q \leq x ^ {3 / 5 - \epsilon}} \lambda (q) \left(\pi (x; q, a) - \frac {\pi (x)}{\varphi (q)}\right) \ll_ {a, \epsilon , A} \frac {x}{(\log x) ^ {A}}.
$$

For simplicity we will not go into the precise definition of ‘triply well factorable’ (it roughly means that$\lambda ( q )$can be decomposed into a triple-convolution of sequences of any predetermined sizes). The key point here is that one can take any$\gamma < 3 / 5$so we can consider very large moduli, and at the same time the technical weakenings (triply well factorable sequences and a dependency on the residue class) are suficient for various applications to sieve methods. For example, Iwaniec [45] showed that the linear sieve weights can be modified to become ‘well-factorable’, which then makes linear sieve estimates amenable to such results. Working a bit harder, one can show that the linear sieve weights then cancel with the error term for primes in arithmetic progressions up to moduli of size$x ^ { 7 / 1 2 }$. Moreover, recent work of Lichtman [51] shows one can modify the linear sieve construction itself to exploit newer equidistribution results profitably (the linear sieve is only optimal at exploiting the information (3.2)).

The spectacular work of Zhang [82] on bounded gaps between primes was an important application of breaking the square-root barrier (even though now we do not need such strong results to prove bounded gaps between primes), and similarly the work of Adleman-Fouvry-Heath-Brown [1,23] on Fermat’s last Theorem relied crucially on ideals going beyond the$x ^ { 1 / 2 }$barrier (although now we know Fermat’s Last Theorem in full [75,80].) Even in the absence of a headline application, it still feels a fundamental and central problem in analytic number theory to concretely go beyond the Bombieri-Vinogradov range.

Question 15. Can we showfor any �, �

$$
\sum_{\substack{q\leq x^{1 / 2 + \delta}\\ (q,a) = 1}}\left|\pi (x;q,a) - \frac{\pi(x)}{\varphi(q)}\right|\ll_{a,A}\frac{x}{(\log x)^{A}}?
$$

for some fixed$\delta > 0 ?$

The work of Bombieri-Friedlander-Iwaniec [5–7] covered most terms which occur when performing a combinatorial decomposition of the primes, leaving one only to deal with products of � integers of size roughly$x ^ { 1 / j }$for$j \in \{ 4 , 5 , 6 \}$. The recent work [57] handles the case$j = 5$, but only obtains partial results for$j = 4$and$j = 6$, which remain to be handled. In particular, we highlight the case$j = 4$, which appears to clearly need new ideas

Question 16. Can one obtain a non-trivial estimatefor

$$
\sum_{q\leq x^{1 / 2 + \delta}}\Big|\sum_{\substack{n_{1},n_{2},n_{3},n_{4}\in [x^{1 / 4},2x^{1 / 4}]\\ (n_{1}n_{2}n_{3}n_{4},q) = 1}}\Big(\mathbf{1}_{n_{1}n_{2}n_{3}n_{4}\equiv 1 (\text{mod} q)} - \frac{1}{\varphi(q)}\Big)\Big|?
$$

## 6. Bilinear estimates

Although basic sieve methods relying only on information about$\mathcal { A }$in arithmetic progressions cannot detect primes because of the parity barrier, it is known that if you incorporate extra ‘bilinear’ information into the method, then you can count primes; this ultimately goes back to the pioneering work of Vinogradov [78]. For example, by inclusion-exclusion on the largest prime factor, for$\mathcal { A } \subseteq [ x , 2 x ]$, we have

$$
\# \{p \in \mathcal {A} \} = S (\mathcal {A}, z) - \sum_ {z <   p <   x ^ {1 / 2}} S (\mathcal {A} _ {p}, p).
$$

When � is a small power of �, basic sieve methods can get good upper and lower bounds for $S ( \mathcal { A } , z )$. The sum over primes counts products$p m \in \mathcal A$where$p$and � are both larger than �, and the power of bilinear sums is they can estimate the number of such products in A with very little arithmetic information requried beyond both factors are of moderate size.

To state things more precisely, it is often easiest to compare the set A of interest with a simpler set$\mathcal { B }$where we know how to count primes using techniques from multiplicative number theory, but is expected to have similar distributional properties. For example, if$\mathcal { A } =$ $[ x , x + x ^ { \theta } ]$is a short interval, then we might take$\mathcal { B } = [ x , x + x \exp ( - \sqrt { \log x } ) ]$to be a long interval. A slight extension of (3.2) is then

$$
\sum_ {m \sim M} \alpha_ {m} \sum_ {n \in \mathcal {I}} \left(\mathbf {1} _ {n m \in \mathcal {A}} - \frac {\# \mathcal {A}}{\# \mathcal {B}} \mathbf {1} _ {n m \in \mathcal {B}}\right) \ll_ {A} \frac {\# \mathcal {A}}{(\log x) ^ {A}}\tag{6.1}
$$

for any 1-bounded sequence$\alpha _ { m }$, constant �, interval I and any$M < x ^ { \gamma }$. With this formulation, we can consider similar variants, in particular the estimate

$$
\sum_ {m \sim M} \sum_ {n} \alpha_ {n} \beta_ {m} \left(\mathbf {1} _ {n m \in \mathcal {A}} - \frac {\# \mathcal {A}}{\# \mathcal {B}} \mathbf {1} _ {m n \in \mathcal {B}}\right) \ll_ {A} \frac {\# \mathcal {A}}{(\log x) ^ {A}}\tag{6.2}
$$

for all 1-bounded sequences$\alpha _ { n } , \beta _ { m }$

We call (6.1) a ‘Type I’ estimate, and (6.2) a ‘Type II’ or ‘bilinear’ estimate for A.

One should interpret the condition (6.2) as saying that we can obtain an asymptotic formula for products with some prescribed prime factorisation, provided these factorisations always contain a divisor of a convenient size.

Naturally, (6.2) is typically much harder to establish, and proving a non-trivial Type II estimate is normally the key technical dificulty which needs to be overcome if wanting to prove the existence of primes in some set A. For example, if we can establish fairly good Type I estimates for the sets mentioned in the introduction, but we currently do not know how to estimate Type II sums for most of the outstanding open problems on primes.

Question 17 (Type II estimates for twin primes). Can one estimate a Type II sum associated to Twin Primes, such as

$$
\sum_ {n \sim N} \sum_ {m \sim M} \alpha_ {n} \beta_ {m} \Lambda (n m + 2)
$$

for arbitrary 1-bounded sequences$\alpha _ { n } , \beta _ { m } ?$

One might also try to reduce both prime variables to bilinear terms, but sums such

as

$$
\sum_{n\sim N}\sum_{\substack{m\sim M\\ nm + 2 = rs}}\sum_{r\sim R}\sum_{s\sim S}\alpha_{n}\beta_{m}\gamma_{r}\delta_{s}
$$

also appear infeasible to handle. (The natural Cauchy-Schwarz argument leads to conditions like$n _ { 1 } s _ { 2 } - s _ { 2 } n _ { 1 } = d$for some$d | 2 n _ { 2 } - 2 n _ { 1 }$, and little appears to have been gained.)

Note that (6.2) cannot be expected to hold if A has a lot of multiplicative structure in the sense that information about � tells us a lot about which$m { \mathrm { : } } { \mathrm { s } }$can have ��$\in \mathcal { A }$. This is to be expected - if A contained only numbers with an even number of prime factors, for example, then we couldn’t hope to produce primes and so we expect that we can’t produce good Type II estimates. In this case the parity of the number of prime factors of � would dictate the parity of the number of prime factors of �, and so by choosing$\alpha _ { n } , \beta _ { m }$to account for these we would give a counterexample to the bound (6.2). Indeed, (6.2) can be thought of as ruling out such multiplicative conspiracies, so that the arithmetic nature of � and � over products ��$\in \mathcal { A }$are ‘independent on average’.

Although (6.2) is ruling out a certain amount of multiplicative structure within A, somewhat perversely we are typically only able to estimate Type II terms efectively if A has some diferent multiplicative structure which we are able to exploit to show that the factors �, � behave somewhat independently of one another. For example, after some initial massaging one typically attempts to prove a Type II estimate via Cauchy-Schwarz to eliminate one of the unknown sets of coeficients (there is typically little lost in doing this, since we cannot rule out$\begin{array} { r } { \alpha _ { n } = \mathrm { s g n } \big ( \sum _ { m } \beta _ { m } \mathbf { 1 } _ { n m \in \mathcal { A } } \big ) \big ) } \end{array}$, leaving us to estimate a quantity like

$$
\# \{n \sim x / M: m _ {1} n \in \mathcal {A}, m _ {2} n \in \mathcal {A} \}.\tag{6.3}
$$

If we can estimate this quantity reasonably accurately (and the diagonal terms with$m _ { 1 } = m _ { 2 }$ do not dominate), then we should be optimistic of obtaining a Type II estimate. It is precisely the dificulty of estimating quantities like (6.3) which limits our ability to apply Type I/II methods.

## 6.1. Type I/II ranges to primes

We first introduce some general notation to talk about sets where we can estimate the bilinear Type II sums in certain ranges at least.

Definition (Type I/II ranges). Given${ \mathcal { A } } , { \mathcal { B } } \subseteq [ x , 2 x ]$

• We say that A satisfies a Type I range of [0<sub>, �</sub>] if (6.1) holds for all choices of $M \leq x ^ { \gamma }$(for all$A > 0 ,$, all intervals I and all 1-bounded sequences$\alpha _ { m } . )$

• We say that$\mathcal { A } \subseteq [ x , 2 x ]$satisfies a Type II range of [�, �] if (6.1) holds for all choices of$M \in [ x ^ { \alpha } , x ^ { \beta } ]$(for all$A > 0$and all 1-bounded sequences$\alpha _ { m } , \beta _ { n } . \beta _ { \ell }$

We typically suppress mentioning B, since we assume that B is a simple set like [�, 2�] in which we can count primes well.

Since we think of${ \mathcal { A } } \subseteq [ x , 2 x ]$, we see that by switching the roles of �, � if A satisfies a Type II range of$[ \alpha , \beta ]$then it also has a Type II range of$[ 1 - \beta + \epsilon , 1 - \alpha - \epsilon ]$for any $\epsilon > 0$

A key basic result, is that if we have ‘enough’ Type I/II arithmetic information, then we can count primes in$\mathcal { A }$

Lemma 18 (Vaughan’s identity). Let A satisfy a Type I range of$[ 0 , \gamma ]$and a Type II range $o f [ \alpha , \alpha + \beta ] . \ I f \beta + \gamma > 1$then we have

$$
\# \{p \in \mathcal {A} \} = \frac {\# \mathcal {A}}{\# \mathcal {B}} \# \{p \in \mathcal {B} \} (1 + o (1)).
$$

(This formulation is somewhat diferent to typical statements of Vaughan’s identity. Ignoring some minor technical considerations to do with separating variables and removing log-coeficients, it follows from choosing$U = x ^ { \alpha } , V = x ^ { 1 - \alpha - \beta }$in [11, Chapter 24], for example.)

Therefore, if the length of the Type I range plus the length of the Type II range is bigger than 1, we can obtain an asymptotic formula for primes in${ \mathcal { A } } .$. Unfortunately, if A satisfies some Type I/II estimates but the combined lengths are not bigger than 1 we cannot necessarily obtain an asymptotic formula for primes and the precise Type I/II regions when we can produce primes becomes a more subtle arithmetic-combinatorial question.

Although we are only considering sets B which are ‘simple’ (and so contain many primes), essentially the same arguments allow us to show that conclusions of Lemma 18 hold even if B is a more complicated set. Thus in principle these techniques can show diferent sets A, B contain the roughly same number of primes, even if we are unable to establish precisely how many primes there are in either set. In this way the results are ‘independent of the Prime Number Theorem, but are not ‘producing’ primes.

For many applications, we merely wish to prove the existence of primes in A. Therefore even if we do not have suficient Type I/II ranges to obtain an asymptotic formula, we might still be able to obtain a non-trivial lower bound for the number of primes in A. Methods to do this were gradually developed [39,46] culminating in Harman’s sieve [35]. This allowed one to exploit positivity to drop inconvenient terms and obtain a lower bound of the correct order of magnitude, provided one still had suitably large Type I and Type II ranges. Given this, the strategy for proving the existence of primes in A then becomes the following:

(1) Establish a Type I estimate in as large a range as possible.

(2) Establish a Type II estimate in as large a range as possible.

(3) Use a sieve decomposition to verify the Type I/II information established is suficient to obtain a non-trivial lower bound for primes in A

With this is mind, we define the upper and lower bound functions$L ( \alpha , \beta , \gamma )$and$U ( \alpha , \beta , \gamma )$ we obtain from an optimal translation of this arithmetic information.

Definition (Optimal constants in Harman’s sieve). For givenfixed constants$\alpha , \beta , \gamma \in [ 0 , 1 ]$ and$\mathcal { B } = [ x , 2 x ]$:

• Let$L _ { x } ( \alpha , \beta , \gamma )$denote the infimum of$\pi ( \mathcal { A } )$log$x / \# \mathcal { R }$over all sets$\mathcal { A } \subseteq [ x , 2 x ]$ satisfying a Type I range$[ 0 , \gamma ]$and a Type II range$[ \alpha , \alpha + \beta ]$. Let$L ( \alpha , \beta , \gamma ) =$ lim inf$\dot { \mathbf { \Phi } } _ { x \to \infty } L _ { x } ( \alpha , \beta , \gamma )$

• Let$U _ { x } ( \alpha , \beta , \gamma )$denote the supremum of$\pi ( \mathcal { A } ) \log x / \# \mathcal { A }$over all set$\mathcal { A } \subseteq [ x , 2 x ]$ satisfying a Type I range [0, �] and a Type II range$[ \alpha , \alpha + \beta ]$. Let$\begin{array} { r l } { { U } ( \alpha , \beta , \gamma ) = } & { { } } \end{array}$ lim$\begin{array} { r } { \operatorname* { s u p } _ { x \to \infty } U _ { x } ( \alpha , \beta , \gamma ) } \end{array}$

Clearly$0 \le L ( \alpha , \beta , \gamma ) \le U ( \alpha , \beta , \gamma )$. Moreover, assuming that$\gamma > 0$we have that $U ( \alpha , \beta , \gamma ) \ll 1$from Lemma 5.$\mathrm { I f } \gamma > 1 / 2$then we know that$L ( \alpha , \beta , \gamma )$and$U ( \alpha , \beta , \gamma )$will be continuous functions on$[ 0 , 1 ] ^ { 3 }$; we expect them to be piecewise smooth and continuous everywhere.

In many problems, we are most interested in showing the existence of primes in$\mathcal { A }$, which would follow if A satisfied (6.1) and (6.2) for some$\alpha , \beta , \gamma$such that$L ( \alpha , \beta , \gamma ) > 0$ Therefore a crucial open question is the following.

Question 19. For which choices of$\alpha , \beta , \gamma$do we have$L ( \alpha , \beta , \gamma ) > 0 ?$

The machinery of Harman’s sieve allows one to compute a numerical lower bound for$L ( \alpha , \beta , \gamma )$(or an upper bound for$U ( \alpha , \beta , \gamma ) )$) for given constants �,$\beta , \gamma$in terms of various multidimensional integrals, but the lower bound is not guaranteed before time to be positive. It is slightly unsatisfying that the computations often have to rely on a moderate amount of explicit numerical calculation of integrals and the decompositions need to be done by hand, but empirically this typically works well. If one has a moderately large constant � for the Type I range, then in practice we can often succeed in showing a positive lower bound even when$\beta$is as small as$1 / 2 0$or$1 / 3 0$, and often (but not always) an argument which produces a non-trivial Type II range will produce one of an adequate length. It is the empirical fact that one can get a non-trivial lower bound via Harman’s sieve even with quite limited Type II ranges which makes it very applicable.

That said, it would be desirable to have a much better understanding of the optimal ways to apply Harman’s sieve, the optimal constants which come out, and what sort of sets we would need to distinguish ourselves from if we wanted to produce stronger results.

Question 20. Given constants$\alpha , \beta , \gamma ,$, what are the optimal values$L ( \alpha , \beta , \gamma )$) and$U ( \alpha , \beta , \gamma ) ?$ What are the sets which achieve these maxima and minima?

Work-in-progress [21] makes some first steps to understanding optimality in Harman’s sieve, but the general picture appears to be arithmetically quite subtle (much more so than for the linear sieve bounds) and combinatorially quite involved.

If we have some non-trivial arithmetic information about${ \mathcal { A } } ,$, but we know that A doesn’t contain the expected number of primes, then we know that this must be compensated by A also containing a diferent number of products of � primes, for some small value of �.

## 7. Primes in thin sets

One particularly challenging situation which encompasses many important situations is when the set$\mathcal { A }$in question contains$O ( x ^ { 1 - \theta } )$elements in$[ x , 2 x ]$for some fixed $\theta > 0$. In this case$\mathcal { A }$is a sparse subset of the integers, and there are limitations on what sort of Type I and Type II information one could hope to establish even in the most optimistic scenarios.

Trivially,$\# \mathcal { R } _ { d }$is an integer, and so we can only hope for the approximation$\# \mathcal { R } _ { d } \approx$ $g ( d ) \# \mathcal { R }$to be accurate when$d < \# \mathcal { R }$, which limits our Type I range to$\gamma \leq 1 - \theta$. Similarly, for typical$n \sim N$there should be roughly$\sharp \mathcal { A } / N$choices of$m \sim x / N$with$m n \in \mathcal { A }$, and so we can only hope to obtain a non-trivial estimate for$\begin{array} { r } { \sum _ { m : m n \in \mathcal { A } } \beta _ { m } } \end{array}$if$N < \# \mathcal { A }$. This limits our Type II range to$\alpha \geq \theta$. Finally, if we attempt to estimate our Type II sums by following the standard Cauchy-Schwarz strategy of estimating

$$
\# \{n \sim N: m _ {1} n \in \mathcal {A}, m _ {2} n \in \mathcal {A} \},\tag{7.1}
$$

then (for generic$m _ { 1 } , m _ { 2 } )$we would expect this count to be roughly$N \# \mathcal { H } ^ { 2 } / x ^ { 2 }$. For this to be typically greater than 1, this would limit us to$N > x ^ { 2 } / \mathcal { A } ^ { 2 } = x ^ { 2 \theta }$, and so$\alpha + \beta < 1 - 2 \theta$in our Type II range. Thus if$\mathcal { A } \subseteq [ x , 2 x ]$with$\# \mathcal { R } = x ^ { 1 - \theta }$, in the absence of more sophisticated methods we expect to be limited to a Type I range of$[ 0 , x ^ { 1 - \theta } ]$and a Type II range of $[ x ^ { \theta } , x ^ { 1 - 2 \theta } ]$. In particular, this range would be suficient to obtain an asymptotic formula via Vaughan’s identity if$\# \mathcal { R } > x ^ { 3 / 4 }$, but we would expect to fail to obtain any Type II information at all$\mathrm { i f } \# \mathcal { R } < x ^ { 2 / 3 }$

In various favourable situations we can obtain Type I and Type II estimates of this strength.

(1) Let$\mathcal { A } = \left\{ n \sim x : \ \| \alpha n + \beta \| < n ^ { - \theta } \right\}$for given irrationals$\alpha , \beta ,$, corresponding to the question of inhomogeneous Diophantine approximation by primes. In this situation$\# \mathcal { A } = x ^ { 1 - \theta + o ( 1 ) }$and it follows from work of Vaughan [76] that one can obtain a Type I range$[ 0 , 1 - \theta ]$and a Type II range$[ \theta , 1 - 2 \theta ]$], therefore covering essentially the full range.

(2) Let$N ( x _ { 1 } + x _ { 2 } { \sqrt [ { n } ] { a } } + \cdot \cdot \cdot + x _ { n - k } { \sqrt [ { n } ] { a ^ { n - k - 1 } } } )$be the incomplete norm form associated to the Kummer extension$\mathbb { Q } ( { \sqrt [ n ] { a } } )$, and A be the value set of � on$[ 1 , x ^ { 1 / n } ] ^ { n }$ Since � is a degree � polynomial in$n - k$variables, A contains roughly$x ^ { 1 - k / n }$ in [�, 2�] and so is a thin set of integers. In [65] we obtain a Type I range $[ 0 , 1 - k / n ]$and a Type II range$[ k / n , 1 - 2 k / n ]$, therefore corresponding to the optimistic basic estimates above.

Jia [48] showed that provided$\theta < 9 / 2 8$then Harman’s sieve can produce a lower bound of the correct order of magnitude for the number of primes in a set A satisfying a Type I estimate $[ 0 , 1 - \theta ]$and a Type II estimate [�, 1 − 2�].

In some situations one can exploit extra structure of the problem to obtain slightly wider Type II estimates. One might hope to obtain cancellations in the error terms$E ( m _ { 1 } , m _ { 2 } )$ occurring in estimating #$\{ n \sim N : m _ { 1 } n \in \mathcal { A } , m _ { 2 } n \in \mathcal { A } \}$, for example, which might allow one to have a Type II range beyond 1 − 2�.

(1) Let$\mathcal { A } = \{ n \in [ x , x + x ^ { 1 - \theta } ] \}$, so we are investigating primes in short intervals. In Section 2 we saw that we can use zero-density methods to obtain an asymptotic formula for$\theta < 5 / 1 2$(note that$5 / 1 2 > 1 / 3$, so this is much sparser than the examples above). By using Dirichlet polynomials, we can actually obtain non-trivial arithmetic information for this problem whenever$\theta > 1 / 2$(although we can only obtain Type II style estimates for coeficients of special types corresponding to convolutions of 3 rather than 2 sequences). By combining these estimates for triple convolutions (and more) with Harman’s sieve we can unconditionally show the existence of primes in intervals$[ x , x + x ^ { 0 . 5 2 5 + o ( 1 ) } ]$[2], which is only an exponent only slightly worse than what we would obtain under the Riemann Hypothesis. The most powerful arithmetic input is Watt’s mean value Theorem [79] - it would be very desirable to have some new arithmetic estimates which could apply to these short interval problems, but currently our techniques do not seem able to go beyond Watt’s work.

(2) Let$\mathcal { A } = \{ a ^ { 3 } + 2 b ^ { 3 } : a , b < x ^ { 1 / 3 } \}$. After switching to prime ideals, Heath-Brown [38] is essentially able to classify those$m _ { 1 } , m _ { 2 }$for which there is an � with $m _ { 1 } n , m _ { 2 } n \in \mathcal { A }$since such � can be given explicitly in terms of$m _ { 1 } , m _ { 2 }$, and then obtain suitable cancellations over these special pairs$m _ { 1 } , m _ { 2 }$. This enables him to obtain a Type II range$[ 1 / 3 , 1 / 2 ]$, which is suficient for obtaining an asymptotic formula for primes represented by$a ^ { 3 } + 2 b ^ { 3 }$, even though this only contains$x ^ { 2 / 3 }$ elements in [1, �]. Li [50] is able to generalise this to further restrict � to be small, allowing him to handle sets even sparser than this.

(3) Let$\mathcal { A } = \{ n \sim x : \| \alpha n \| < x ^ { - 1 / 3 + \epsilon } \}$. Then A contains$x ^ { 2 / 3 }$integers of size �, but nevertheless Matomäki [53] (building on [40]) was able to show that A still contained primes by establishing non-trivial arithmetic information in wider ranges. Again, to establish these wider ranges she needed to consider trilinear sums.

In a slightly diferent direction in [64] Type II estimates were deduced by exploiting a very nice Fourier structure in the underlying set. This is an example where the set doesn’t have obvious ‘linear structure’ (such as short intervals, or the distribution of �� modulo one), and doesn’t lack obvious multiplicative structure which makes it more feasible to estimate (7.1), but nevertheless non-trivial arithmetic information can be established (in this case within the Hardy-Littlewood circle method). It would be interesting to add to this example.

We mention in passing the recent work of Heath-Brown-Li [41] on primes of the form $X ^ { 2 } + p ^ { 4 }$and Merikoski [67] on$X ^ { 2 } + ( Y ^ { 2 } + 1 ) ^ { 2 }$and Xiao [81] on primes of the form$f ( a , b ^ { 2 } )$ for binary quadratic forms � all generalising the work of Friedlander-Iwaniec on$X ^ { 2 } + Y ^ { 4 }$ [27].

Even with these proof-of-concept results that in principle one can establish some sort of non-trivial arithmetic information with fairly general coeficient sequences in some sparse sets, all approaches seem to break down completely when considering sets containing fewer than$x ^ { 1 / 2 }$elements in [�, 2�].

Question 21. Is there a plausible way to adapt Type I/II machinery to apply to very sparse sets with$x ^ { 1 / 2 - \epsilon }$elements in [�, 2�]?

Without some advance in this direction, we do seem to have any means of counting primes in intervals of length smaller than$x ^ { 1 / 2 }$, and thereby addressing Legendre’s conjecture on the existence of a prime between consecutive squares. Of course, we expect there to be primes in much shorter intervals (as short as$( \log x ) ^ { 2 + o ( 1 ) } ,$), but going beyond$x ^ { 1 / 2 }$seems out of reach for now, even if we assume the Riemann Hypothesis and things like Montgomery’s Pair Correlation Conjecture [68].

## 8. Further arithmetic information

Even ifthe Type I/Type II arithmetic information in insuficient for generating primes (or asymptotic formulae for primes), we can sometimes remedy the situation by incorporating further arithmetic information into the method.

For example, we mentioned in Section 7 that for the problem of primes in short intervals or for small values of$\alpha p$modulo one it was important that there was additional flexibility to consider triple convolutions of sequences, rather than just bilinear sums. Often we find that the size of factors of terms produced in a decomposition of the primes is the key feature - when terms factor in a convenient manner one can produce much stronger results.

As well as higher order convolutions (corresponding to assuming some factorisation properties of the sequences$\alpha _ { n }$or$\beta _ { m } )$we can also exploit the fact that sometimes we are able to produce stronger results if some of the sequences involved are just the constant 1. For

example, we have Linnik’s identity [52]

$$
\frac {\Lambda (n)}{\log n} = - \sum_ {j = 1} ^ {\infty} \frac {(- 1) ^ {j}}{j} \tau_ {j} ^ {\prime} (n)
$$

where$\tau _ { j } ^ { \prime } ( n )$counts representations of � as the product of$j$integers all bigger than 1. In principle this allows us to understand primes in$\mathcal { A }$by understanding the average of$\tau _ { j } ^ { \prime } ( n )$for $n \in \mathcal { A }$. Understanding$\tau _ { j } ^ { \prime } ( n )$is similar to understanding �-fold convolutions in${ \mathcal { A } } ,$, therefore generalising our linear and bilinear sums. Moreover, in this formulation the coeficients of each of the$j$factors is just 1 rather than some unknown sequence. This additional flexibility of only needing to consider smooth coeficient sequences is dificult to exploit unless some of the variables are very long like in the case of Type I estimates (and for practical applications Heath-Brown’s identity [36] is often more convenient to use), but is crucial in some situations. For example, the recent work [57–59] on primes in arithmetic progressions crucially relied on estimates for the divisor function in arithmetic progressions and for$\tau _ { 3 } ( n )$in arithmetic progressions [24,25,37].

One further comment is that the coeficients which naturally occur from Buchstab iterations are the indicator function of products of primes, where each prime is of a roughly fixed size. This means that rather than requiring estimates like (6.2) for arbitrary sequences, we only really require this when$\alpha _ { n }$and$\beta _ { m }$look like the indicator function of primes, or products of primes. In the ground-breaking work of Friedlander-Iwaniec on$X ^ { 2 } + Y ^ { 4 }$representing primes [26,27] the fact that the coeficients satisfied a suitable Siegel-Walfisz Theorem was crucial, and so the Type II estimates were only valid for this reduced class of coeficients.

One simple observation is that$\tau _ { j } ( n )$are the coeficients of the degree � �-function $\zeta ( s ) ^ { j }$. There is a general principle that often estimates which can be obtained in a direct manner for �(�) can be also obtained in a more complicated manner for the Fourier coeficients of suitable cusp forms via the spectral theory of automorphic forms. It is therefore compelling to speculate whether this would allow for further ‘higher degree’ arithmetic information to be incorporated.

Question 22. Can one use coeficients of other higher degree �-functions to aid counting primes?

Work of Drappeau-Maynard [14] made crucial use of the Sato-Tate distribution of Kloosterman sums to enable an estimation of a sum over primes, where arithmetic properties ofthe underlying sequence essentially reduced the sieve dimension. Since Fourier coeficients have similar distributional features one might hope that this simple example could be indicative of a wider approach.

## 9. Choice of lift and comparison sets

When attempting to count primes in A using the Type I/II sums strategy, one wants to understand a sum

$$
\sum_ {p \in \mathcal {A}} a _ {p}
$$

overprimes, and we study this by gaining arithmetic information (such as Type I/II estimates) for a sequence$a _ { n }$over integers$n \in \mathcal { A }$. We therefore choose a$l i f t$of the sequence$a _ { p }$supported on primes to the sequence$a _ { n }$supported on integers which hopefully is more amenable to estimation. In many contexts there is a natural choice of$a _ { n }$which works well$( \mathbf { e } . \mathbf { g } . a _ { p } = 1$and $a _ { n } = 1 )$, but one could imagine other choices also being worthy of consideration (or perhaps multiple diferent lifts). For example, if one could understand the sums with$a _ { n } = 2 / \tau ( n )$, then one would have a lift of the sequence$a _ { p } = 1$which would remain closer to the primes, and it would be correspondingly easier to detect primes given the same basic arithmetic information (it would be reducing the sieve dimension). So far our estimates appear to have been limited to the simplest possible choices, but it is natural to ask if this is really necessary.

Question 23. Are there situations where other lifts$a _ { n }$ofthe sequence$a _ { p }$can aid estimating primes?

As a very basic proof-of-concept, in some situations it is easier to lift$a _ { p } = 1$to $a _ { n } = \theta ( n )$where$\theta ( n )$is a sieve weight ensuring that$a _ { n }$behaves as if it is supported only on small prime factors. But ideally we would find a non-trivial way to lift to a sequence sensitive to all prime factors of$n ,$not just small ones.

In (6.1) and (6.2) we compare arithmetic counts in a set$\mathcal { A }$to a simpler set${ \mathcal { B } } .$, but the choice of B is left to the application at hand. In most cases B is a truly simple set (such as an interval) where something like the Prime Number Theorem can be applied directly. However, in some cases it is advantageous (or important) to have more complicated comparison sets (or one could generalise to a weighted sequence). For example, in looking at primes in arithmetic progressions to large moduli, it is useful to compare the indicator function of the residue class $\mathbf { 1 } _ { n \equiv a { \mathrm { ~ ( m o d ~ } } q _ { 1 } q _ { 2 } { ) } }$not with the basic choice of 1 (or$\mathbf { 1 } _ { ( n , q _ { 1 } q _ { 2 } ) = 1 } )$, but with the ‘intermediate complexity’ sequences${ \bf 1 } _ { n \equiv a { \mathrm { ~ ( m o d ~ } } q _ { 1 } ) }$. This allows us to use additive Fourier analysis to show that$\scriptstyle { \mathbf { 1 } } _ { n \equiv a }$(mod$q _ { 1 } q _ { 2 } ) \approx \mathbf { 1 } _ { n \equiv a { \mathrm { ~ ( m o d ~ } } q _ { 1 } { \mathrm { ) } } }$in some average sense, and then use multiplicative Fourier analysis (Dirichlet characters) to show that${ \bf 1 } _ { n \equiv a { \mathrm { ~ ( m o d ~ } } q _ { 1 } ) } \approx 1$. Therefore we are going through a two-step approximation process, and exploiting in a crucial manner that$\mathbb { Z } / q _ { 1 } \mathbb { Z }$is a subgroup of$\mathbb { Z } / q _ { 1 } q _ { 2 } \mathbb { Z }$

Question 24. When is it helpful to use more complicated intermediate comparison sequences B?

It would be very interesting if we could weaken the requirement that$\mathbb { Z } / q _ { 1 } q _ { 2 } \mathbb { Z }$has a suitably sized subgroup for the arguments to apply.

In various works Drappeau [12, 13] has shown that it can be valuable to retain various possible secondary main terms in applications of Linnik’s dispersion method, which corresponds to it being somewhat advantageous to choose a more complicated comparison set B. (A similar feature was used in [65] to help account for Siegel-zero issues.) These can be thought of as examples of intermediate sequences B which are taking into account the possible causes of fluctuations of the number of primes in A.

## 10. Abelian quadratic limitations

One limitation in many methods for counting primes is that we cannot rule out zeros of �-functions very close to the line$\operatorname { R e } ( s ) = 1$, and so even in the simplest situations such as counting primes in [1, �] we cannot obtain an error term better than some exponential log factor.

One curious feature is that often the more involved counting arguments (such as Type I/II estimates) actually come with much stronger error terms (such as giving a power saving) whenever the estimate can be achieved. For example, the classical exponential sum bound shows that

$$
\sum_ {n <   x} \Lambda (n) e (n \alpha) \ll x ^ {1 - \epsilon}
$$

unless$\alpha \approx a / q$for some$q < x ^ { 2 \epsilon } ( \log x ) ^ { O ( 1 ) }$, in which case the possible existence of a Siegel zero would prevent a power-saving estimate.

Similarly, the error term in the Titchmarsh divisor problem ofestimating$\scriptstyle \sum _ { p < x } \tau ( p -$ 1) is fundamentally limited by the possible existence of Siegel-zeros (see [13]), but for the analogue of this problem with (normalised) Fourier coeficients of Holomorphic cusp forms of$\mathrm { P S L } _ { 2 } ( \mathbb { Z } )$, we obtain a power-saving estimate$\begin{array} { r } { \sum _ { p < x } a ( p - 1 ) < x ^ { 3 9 1 / 3 9 2 + o ( 1 ) } } \end{array}$due to work of Pitt [70].

The ‘Higher order Fourier analysis’ pioneered by Green and Tao [32] involves looking at sums over primes twisted by nilsequences. Again, it is the case that it is ultimately easier to obtain quantitative cancellation for nilsequences when the nilsequence is suitably far from a rational phase; the limits of the results stem from possible zeros of Dirichlet �-functions (see, for example, the discussion after [33, Theorem 1]). Other examples of this occur in the more recent work [55,73] where the ultimately key limitations to estimates are when a nilsequence is ‘close’ to encoding a rational phase, reducing to the classical situation.

In a slightly diferent direction, for many situations involving higher degree$L -$ functions it is known that the issue of zeros very close to � = 1 cannot arise; Siegel zeros are essentially only a phenomenon which could arise for quadratic Dirichlet �-functions, and so we can have better results in these more complicated scenarios (unless quadratic Dirichlet character could be lurking under the surface, such as if we consider a Dedekind �-function for a number field with an index 2 - so quadratic - subfield).

In all these cases estimates for primes which at first sight seem harder that the classical setting actually avoid the limitations from the well-known obstacles and so prove to actually be easier in some sense.

## Acknowledgments

The author is supported by a Royal Society Wolfson Merit Award, and this project ha received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 851318).

## References

[1] L. M. Adleman and D. R. Heath-Brown, The first case of Fermat’s last theorem. Invent. Math. 79 (1985), no. 2, 409–416

[2]R. C. Baker, G. Harman, and J. Pintz, The diference between consecutive primes. II. Proc. London Math. Soc. (3) 83 (2001), no. 3, 532–562

[3]R. C. Baker and A. J. Irving, Bounded intervals containing many primes. Math. Z. 286 (2017), no. 3-4, 821–841

[4]E. Bombieri, On the large sieve. Mathematika 12 (1965), 201–225

[5]E. Bombieri, J. B. Friedlander, and H. Iwaniec, Primes in arithmetic progressions to large moduli. Acta Math. 156 (1986), no. 3-4, 203–251

[6]E. Bombieri, J. B. Friedlander, and H. Iwaniec, Primes in arithmetic progressions to large moduli. II. Math. Ann. 277 (1987), no. 3, 361–393

[7]E. Bombieri, J. B. Friedlander, and H. Iwaniec, Primes in arithmetic progressions to large moduli. III. J. Amer. Math. Soc. 2 (1989), no. 2, 215–224

[8]J. Bourgain, P. Sarnak, and T. Ziegler, Disjointness of Moebius from horocycle flows. In From Fourier analysis and number theory to Radon transforms and geometry, pp. 67–83, Dev. Math. 28, Springer, New York, 2013

[9] J.-R. Chen, On the representation of a larger even integer as the sum of a prime and the product of at most two primes. Sci. Sinica 16 (1973), 157–176

[10] H. Daboussi and H. Delange, On multiplicative arithmetical functions whose modulus does not exceed one. J. London Math. Soc. (2) 26 (1982), no. 2, 245–264

[11]H. Davenport, Multiplicative number theory. Second edn., Graduate Texts in Mathematics 74, Springer-Verlag, New York-Berlin, 1980

[12] S. Drappeau, Théorèmes de type Fouvry-Iwaniec pour les entiers friables. Compos. Math. 151 (2015), no. 5, 828–862

[13] S. Drappeau, Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method. Proc. Lond. Math. Soc. (3) 114 (2017), no. 4, 684–732

[14] S. Drappeau and J. Maynard, Sign changes of Kloosterman sums and exceptional characters. Proc. Amer. Math. Soc. 147 (2019), no. 1, 61–75

[15] N. Elkies, The existence of infinitely many supersingular primes for every elliptic curve over Q. Invent. Math. 89 (1987), no. 3, 561–567

[16] P. D. T. A. Elliott and H. Halberstam, A conjecture in prime number theory. In Symposia Mathematica, Vol. IV (INDAM, Rome, 1968/69), pp. 59–72, Academic Press, London, 1970

[17] P. Erdös, The diference of consecutive primes. Duke Math. J. 6 (1940), 438–441

[18] K. Ford, Large prime gaps and progressions with few primes. Riv. Math. Univ. Parma (N.S.) 12 (2021), no. 1, 41–47

[19] K. Ford, B. Green, S. Konyagin, J. Maynard, and T. Tao, Long gaps between primes. J. Amer. Math. Soc. 31 (2018), no. 1, 65–105

[20] K. Ford, B. Green, S. Konyagin, and T. Tao, Large gaps between consecutive prime numbers. Ann. ofMath. (2) 183 (2016), no. 3, 935–974

[21] K. Ford and J. Maynard, An optimal Harman sieve. In preparation.

[22] E. Fouvry, Autour du théorème de Bombieri-Vinogradov. Acta Math. 152 (1984), no. 3-4, 219–244

[23] E. Fouvry, Théorème de Brun-Titchmarsh: application au théorème de Fermat. Invent. Math. 79 (1985), no. 2, 383–407

[24] E. Fouvry, E. Kowalski, and P. Michel, On the exponent of distribution of the ternary divisor function. Mathematika 61 (2015), no. 1, 121–144

[25] J. B. Friedlander and H. Iwaniec, Incomplete Kloosterman sums and a divisor problem. Ann. ofMath. (2) 121 (1985), no. 2, 319–350

[26] J. B. Friedlander and H. Iwaniec, Asymptotic sieve for primes. Ann. ofMath. (2) 148 (1998), no. 3, 1041–1065

[27] J. B. Friedlander and H. Iwaniec, The polynomial$X ^ { 2 } + Y ^ { 4 }$captures its primes. Ann. ofMath. (2) 148 (1998), no. 3, 945–1040

[28] J. B. Friedlander and H. Iwaniec, Opera de cribro. American Mathematical Society Colloquium Publications 57, American Mathematical Society, Providence, RI, 2010

[29] D. Goldfeld, The class number of quadratic fields and the conjectures of Birch and Swinnerton-Dyer. Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 3 (1976), no. 4, 624–663

[30] D. Goldfeld, Gauss’s class number problem for imaginary quadratic fields. Bull. Amer. Math. Soc. (N.S.) 13 (1985), no. 1, 23–37

[31] A. Granville, Sieving intervals and siegel zeros. Preprint. Available at https://arxiv.org/abs/2010.01211

[32] B. Green and T. Tao, Linear equations in primes. Ann. of Math. (2) 171 (2010), no. 3, 1753–1850

[33] B. Green and T. Tao, The Möbius function is strongly orthogonal to nilsequences. Ann. ofMath. (2) 175 (2012), no. 2, 541–566

[34] B. Gross and D. Zagier, Heegner points and derivatives of �-series. Invent. Math. 84 (1986), no. 2, 225–320

[35] G. Harman, Prime-detecting sieves. London Mathematical Society Monographs Series 33, Princeton University Press, Princeton, NJ, 2007

[36] D. R. Heath-Brown, Prime numbers in short intervals and a generalized Vaughan identity. Canadian J. Math. 34 (1982), no. 6, 1365–1377

[37] D. R. Heath-Brown, The divisor function$d _ { 3 } ( n )$in arithmetic progressions. Acta Arith. 47 (1986), no. 1, 29–56

[38] D. R. Heath-Brown, Primes represented by$x ^ { 3 } + 2 y ^ { 3 }$. Acta Math. 186 (2001), no. 1, 1–84

[39] D. R. Heath-Brown and H. Iwaniec, On the diference between consecutive primes. Invent. Math. 55 (1979), no. 1, 49–69

[40] D. R. Heath-Brown and C. Jia, The distribution of �� modulo one. Proc. London Math. Soc. (3) 84 (2002), no. 1, 79–104

[41] D. R. Heath-Brown and X. Li, Prime values of$a ^ { 2 } + p ^ { 4 }$. Invent. Math. 208 (2017), no. 2, 441–499

[42] H. Helfgott, The ternary goldbach problem. Annals of Mathematic Studies to appear

[43] C. Hooley, On Artin’s conjecture. J. Reine Angew. Math. 225 (1967), 209–220

[44] M. Huxley, On the diference between consecutive primes. Invent. Math. 15 (1972), 164–170

[45] H. Iwaniec, A new form of the error term in the linear sieve. Acta Arith. 37 (1980), 307–320

[46] H. Iwaniec and M. Jutila, Primes in short intervals. Ark. Mat. 17 (1979), no. 1, 167–176

[47]H. Iwaniec and E. Kowalski, Analytic number theory. American Mathematical Society Colloquium Publications 53, American Mathematical Society, Providence, RI, 2004

[48] C. Jia, On the distribution of �� modulo one. II. Sci. China Ser. A 43 (2000), no. 7, 703–721

[49] I. Kátai, A remark on a theorem of H. Daboussi. Acta Math. Hungar. 47 (1986), no. 1-2, 223–225

[50] X. Li, Prime values of a sparse polynomial sequence. Duke Math J. to appear

[51] J. Lichtman, A modification of the linear sieve, and the count of twin primes. Preprint. Availble at https://arxiv.org/abs/2109.02851

[52] Y. Linnik, The dispersion method in binary additive problems. American Mathematical Society, Providence, R.I., 1963

[53] K. Matomäki, The distribution of �� modulo one. Math. Proc. Cambridge Philos. Soc. 147 (2009), no. 2, 267–283

[54] K. Matomäki and M. Radziwiłł, Multiplicative functions in short intervals. Ann. ofMath. (2) 183 (2016), no. 3, 1015–1056

[55]K. Matomäki, X. Shao, T. Tao, and J. Teräväinen, Higher uniformity of arithmeti functions in short intervals I. All intervals. Preprint. Available at https://arxiv.org/abs/2204.03754

[56] K. Matomäki and J. Teräväinen, On the möbius function in all short intervals. J. Eur. Math. Soc. to appear

[57] J. Maynard, Primes in arithmetic progressions to large moduli i: Fixed residue classes. Mem. Amer. Math. Soc. to appear

[58] J. Maynard, Primes in arithmetic progressions to large moduli ii: Well-factorable estimates. Mem. Amer. Math. Soc. to appear

[59] J. Maynard, Primes in arithmetic progressions to large moduli iii: Unifrorm residue classes. Mem. Amer. Math. Soc. to appear

[60] J. Maynard, 3-tuples have at most 7 prime factors infinitely often. Math. Proc. Cambridge Philos. Soc. 155 (2013), no. 3, 443–457

[61] J. Maynard, Small gaps between primes. Ann. ofMath. (2) 181 (2015), no. 1, 383–413

[62] J. Maynard, Dense clusters of primes in subsets. Compos. Math. 152 (2016), no. 7, 1517–1554

[63] J. Maynard, Large gaps between primes. Ann. ofMath. (2) 183 (2016), no. 3, 915–933

[64] J. Maynard, Primes with restricted digits. Invent. Math. 217 (2019), no. 1, 127–218

[65] J. Maynard, Primes represented by incomplete norm forms. Forum Math. Pi 8 (2020), e3, 128

[66] J. Maynard and K. Pratt, Half-isolated zeros and zero density estimates. In preparation

[67]J. Merikoski, The polynomials$X ^ { 2 } + ( Y ^ { 2 } + 1 ) ^ { 2 }$and$X ^ { 2 } + ( Y ^ { 3 } + Z ^ { 3 } ) ^ { 2 }$also capture their primes. Preprint. Available at https://arxiv.org/abs/2112.03617.

[68] H. L. Montgomery, The pair correlation of zeros of the zeta function. In Analytic number theory (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972), pp. 181–193, 1973

[69] H. L. Montgomery and R. C. Vaughan, The large sieve. Mathematika 20 (1973), 119–134

[70] N. Pitt, On an analogue of Titchmarsh’s divisor problem for holomorphic cusp forms. J. Amer. Math. Soc. 26 (2013), no. 3, 735–776

[71] D. H. J. Polymath, Variants of the Selberg sieve, and bounded intervals containing many primes. Res. Math. Sci. 1 (2014), Art. 12, 83

[72] R. A. Rankin, The Diference between Consecutive Prime Numbers. J. London Math. Soc. 11 (1936), no. 4, 242–245

[73] X. Shao and J. Teräväinen, The Bombieri-Vinogradov theorem for nilsequences. Discrete Anal. (2021), Paper No. 21, 55

[74] T. Tao, The logarithmically averaged Chowla and Elliott conjectures for two-point correlations. Forum Math. Pi 4 (2016), e8, 36

[75] R. Taylor and A. Wiles, Ring-theoretic properties of certain Hecke algebras. Ann. ofMath. (2) 141 (1995), no. 3, 553–572

[76] R. C. Vaughan, On the distribution of �� modulo 1. Mathematika 24 (1977), no. 2, 135–141

[77] A. I. Vinogradov, The density hypothesis for Dirichet �-series. Izv. Akad. Nauk SSSR Ser. Mat. 29 (1965), 903–934

[78] I. M. Vinogradov, The method oftrigonometrical sums in the theory ofnumbers. Dover Publications, Inc., Mineola, NY, 2004

[79] N. Watt, Kloosterman sums and a mean value for Dirichlet polynomials. J. Number Theory 53 (1995), no. 1, 179–210

[80] A. Wiles, Modular elliptic curves and Fermat’s last theorem. Ann. ofMath. (2) 141 (1995), no. 3, 443–551

[81]S. Y. Xiao, Prime values of$f ( a , b ^ { 2 } )$and$f ( a , p ^ { 2 } )$, f quadratic. Preprint. Available at https://arxiv.org/abs/2111.04136

[82] Y. Zhang, Bounded gaps between primes. Ann. of Math. (2) 179 (2014), no. 3, 1121–1174

## James Maynard

Mathematical Institute, Oxford, England OX1 4AU, james.alexander.maynard@gmail.com