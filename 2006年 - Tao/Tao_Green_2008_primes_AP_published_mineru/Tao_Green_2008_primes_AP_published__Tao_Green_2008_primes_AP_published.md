# The primes contain arbitrarily long arithmetic progressions

By Ben Green and Terence Tao\*

## Abstract

We prove that there are arbitrarily long arithmetic progressions of primes. There are three major ingredients. The first is Szemer´edi’s theorem, which asserts that any subset of the integers of positive density contains progressions of arbitrary length. The second, which is the main new ingredient of this paper, is a certain transference principle. This allows us to deduce from Szemer´edi’s theorem that any subset of a suficiently pseudorandom set (or measure) of positive relative density contains progressions of arbitrary length. The third ingredient is a recent result of Goldston and Yıldırım, which we reproduce here. Using this, one may place (a large fraction of) the primes inside a pseudorandom set of “almost primes” (or more precisely, a pseudorandom measure concentrated on almost primes) with positive relative density.

## 1. Introduction

It is a well-known conjecture that there are arbitrarily long arithmetic progressions of prime numbers. The conjecture is best described as “classical”, or maybe even “folklore”. In Dickson’s History it is stated that around 1770 Lagrange and Waring investigated how large the common diference of an arithmetic progression of L primes must be, and it is hard to imagine that they did not at least wonder whether their results were sharp for all L.

It is not surprising that the conjecture should have been made, since a simple heuristic based on the prime number theorem would suggest that there are$\gg N ^ { 2 } / \log ^ { k }$N k-tuples of primes$p _ { 1 } , \ldots , p _ { k }$in arithmetic progression, each $p _ { i }$being at most N. Hardy and Littlewood [24], in their famous paper of 1923, advanced a very general conjecture which, as a special case, contains the hypothesis that the number of such k-term progressions is asymptotically

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*While this work was carried out the first author was a PIMS postdoctoral fellow at the University of British Columbia, Vancouver, Canada. The second author was a Clay Prize Fellow and was supported by a grant from the Packard Foundation.</span></small>

$C _ { k } N ^ { 2 } / \log ^ { k } { N }$for a certain explicit numerical factor$C _ { k } > 0$(we do not come close to establishing this conjecture here, obtaining instead a lower bound $( \gamma ( k ) + o ( 1 ) ) N ^ { 2 } / \log ^ { k } { N }$for some very small$\gamma ( k ) > 0 )$

The first theoretical progress on these conjectures was made by van der Corput [42] (see also [8]) who, in 1939, used Vinogradov’s method of prime number sums to establish the case$k = 3 .$, that is to say that there are infinitely many triples of primes in arithmetic progression. However, the question of longer arithmetic progressions seems to have remained completely open (except for upper bounds), even for$k = 4$. On the other hand, it has been known for some time that better results can be obtained if one replaces the primes with a slightly larger set of almost primes. The most impressive such result is due to Heath-Brown [25]. He showed that there are infinitely many 4-term progressions consisting of three primes and a number which is either prime or a product of two primes. In a somewhat diferent direction, let us mention the beautiful results of Balog [2], [3]. Among other things he shows that for any m there are m distinct primes$p _ { 1 } , \ldots , p _ { m }$such that all of the averages${ \frac { 1 } { 2 } } ( p _ { i } + p _ { j } )$ are prime.

The problem of finding long arithmetic progressions in the primes has also attracted the interest of computational mathematicians. At the time of writing the longest known arithmetic progression of primes is of length 23, and was found in 2004 by Markus Frind, Paul Underwood, and Paul Jobling:

$$
5 6 2 1 1 3 8 3 7 6 0 3 9 7 + 4 4 5 4 6 7 3 8 0 9 5 8 6 0 k; \quad k = 0, 1, \dots , 2 2.
$$

An earlier arithmetic progression of primes of length 22 was found by Moran, Pritchard and Thyssen [32]:

$$
1 1 4 1 0 3 3 7 8 5 0 5 5 3 + 4 6 0 9 0 9 8 6 9 4 2 0 0 k; \quad k = 0, 1, \dots , 2 1.
$$

Our main theorem resolves the above conjecture.

Theorem 1.1. The prime numbers contain infinitely many arithmetic progressions of length k for all k.

In fact, we can say something a little stronger:

Theorem 1.2 (Szemer´edi’s theorem in the primes). Let A be any subset of the prime numbers of positive relative upper density; thus

$$
\limsup _ {N \to \infty} \pi (N) ^ {- 1} | A \cap [ 1, N ] | > 0,
$$

where$\pi ( N )$denotes the number of primes less than or equal to N. Then A contains infinitely many arithmetic progressions of length k for all k.

If one replaces “primes” in the statement of Theorem 1.2 by the set of all positive integers$\mathbb { Z } ^ { + }$, then this is a famous theorem of Szemer´edi [38]. The special case$k = 3$of Theorem 1.2 was recently established by the first author [21] using methods of Fourier analysis. In contrast, our methods here have a more ergodic theory flavour and do not involve much Fourier analysis (though the argument does rely on Szemer´edi’s theorem which can be proven by either combinatorial, ergodic theory, or Fourier analysis arguments). We also remark that if the primes were replaced by a random subset of the integers, with density at least$N ^ { - 1 / 2 + \varepsilon }$on each interval [1, N], then the$k = 3$case of the above theorem would be established as in [30].

Acknowledgements. The authors would like to thank Jean Bourgain, Enrico Bombieri, Tim Gowers, Bryna Kra, Elon Lindenstrauss, Imre Ruzsa, Roman Sasyk, Peter Sarnak and Kannan Soundararajan for helpful conversations. We are particularly indebted to Andrew Granville for drawing our attention to the work of Goldston and Yıldırım, and to Dan Goldston for making the preprint [17] available. We are also indebted to Yong-Gao Chen and his students, Bryna Kra, Victoria Neale, Jamie Radclife, Lior Silberman and Mark Watkins for corrections to earlier versions of the manuscript. We are particularly indebted to the anonymous referees for a very thorough reading and many helpful corrections and suggestions, which have been incorporated into this version of the paper. Portions of this work were completed while the first author was visiting UCLA and Universit´e de Montr´eal, and he would like to thank these institutions for their hospitality. He would also like to thank Trinity College, Cambridge for support over several years.

## 2. An outline of the proof

Let us start by stating Szemer´edi’s theorem properly. In the introduction we claimed that it was a statement about sets of integers with positive upper density, but there are other equivalent formulations. A “finitary” version of the theorem is as follows.

Proposition 2.1 (Szemer´edi’s theorem ([37], [38])). Let N be a positive integer and let$\mathbb { Z } _ { N } : = \mathbb { Z } / N \mathbb { Z } . ^ { 1 }$Let$\delta > 0$be a fixed positive real number, and let $k \geqslant 3$be an integer. Then there is a minimal$N _ { 0 } ( \delta , k ) < \infty$with the following property. If$N \geqslant N _ { 0 } ( \delta , k )$and$A \subseteq \mathbb { Z } _ { N }$is any set of cardinality at least$\delta N$ then A contains an arithmetic progression of length k.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Z<sub>N</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Z<sub>N</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">[−N, N],</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>We will retain this notation throughout the paper; thus will never refer to the N-adics. We always assume for convenience that N is prime. It is very convenient to work in , rather than the more traditional since we are free to divide by 2, 3, . . . , k2, 3, . . . , k and it is possible to make linear changes of variables without worrying about the ranges of summation. There is a slight price to pay for this, in that one must now address some “wraparound” issues when identifying with a subset of the integers, but these will beZ<sub>N</sub> easily dealt with.</span></small>

Finding the correct dependence of$N _ { 0 }$on δ and k (particularly δ) is a famous open problem. It was a great breakthrough when Gowers [18], [19] showed that

$$
N _ {0} (\delta , k) \leqslant 2 ^ {2 ^ {\delta^ {- c _ {k}}}},
$$

where$c _ { k }$is an explicit constant (Gowers obtains$c _ { k } = 2 ^ { 2 ^ { k + 9 } } )$. It is possible that a new proof of Szemer´edi’s theorem could be found, with suficiently good bounds that Theorem 1.1 would follow immediately. To do this one would need something just a little weaker than

$$
N _ {0} (\delta , k) \leqslant 2 ^ {c _ {k} \delta^ {- 1}}\tag{2.1}
$$

(there is a trick, namely passing to a subprogression of common diference $2 \times 3 \times 5 \times \cdots \times w ( N )$for appropriate$w ( N )$, which allows one to consider the primes as a set of density essentially log log N/ log N rather than 1/ log N; we will use a variant of this$^ { 6 \cdot 6 } W { \cdot } \mathrm { t r i c k } ^ { 3 }$later in this paper to eliminate local irregularities arising from small divisors). In our proof of Theorem 1.2, we will need to use Szemer´edi’s theorem, but we will not need any quantitative estimates on$N _ { 0 } ( \delta , k )$

Let us state, for contrast, the best known lower bound which is due to Rankin [35] (see also Lacey-Laba [31]):

$$
N _ {0} (\delta , k) \geqslant \exp (C (\log 1 / \delta) ^ {1 + \lfloor \log_ {2} (k - 1) \rfloor}).
$$

At the moment it is clear that a substantial new idea would be required to obtain a result of the strength (2.1). In fact, even for$k = 3$the best bound is$N _ { 0 } ( \delta , 3 ) \leqslant 2 ^ { C \delta ^ { - 2 } \log ( 1 / \delta ) }$, a result of Bourgain [6]. The hypothetical bound (2.1) is closely related to the following very open conjecture of Erd˝os:

Conjecture 2.2 (Erd˝os conjecture on arithmetic progressions). Suppose that$A ~ = ~ \{ a _ { 1 } ~ < ~ a _ { 2 } ~ < ~ . ~ . ~ . \}$is an infinite sequence of integers such that $\textstyle \sum 1 / a _ { i } = \infty$. Then A contains arbitrarily long arithmetic progressions.

This would imply Theorem 1.1.

We do not make progress on any of these issues here. In one sentence, our argument can be described instead as a transference principle which allows us to deduce Theorems 1.1 and 1.2 from Szemer´edi’s theorem, regardless of what bound we know for$N _ { 0 } ( \delta , k )$; in fact we prove a more general statement in Theorem 3.5 below. Thus, in this paper, we must assume Szemer´edi’s theorem. However with this one (rather large!)$\mathrm { c a v e a t ^ { 2 } }$our paper is self-contained.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>We will also require some standard facts from analytic number theory such as the prime number theorem, Dirichlet’s theorem on primes in arithmetic progressions, and the classica zero-free region for the Riemann ζ-function (see Lemma A.1).</span></small>

Szemer´edi’s theorem can now be proved in several ways. The original proof of Szemer´edi [37], [38] was combinatorial. In 1977, Furstenberg made a very important breakthrough by providing an ergodic-theoretic proof [10]. Perhaps surprisingly for a result about primes, our paper has at least as much in common with the ergodic-theoretic approach as it does with the harmonic analysis approach of Gowers. We will use a language which suggests this close connection, without actually relying explicitly on any ergodic-theoretical concepts.<sup>3</sup> In particular we shall always remain in the finitary setting of$\mathbb { Z } _ { N }$ in contrast to the standard ergodic theory framework in which one takes weak limits (invoking the axiom of choice) to pass to an infinite measure-preserving system. As will become clear in our argument, in the finitary setting one can still access many tools and concepts from ergodic theory, but often one must incur error terms of the form$o ( 1 )$when one does so.

Here is another form of Szemer´edi’s theorem which suggests the ergodic theory analogy more closely. We use the conditional expectation notation $\mathbb { E } ( f | x _ { i } \in B )$to denote the average of$f$as certain variables$x _ { i }$range over the set$B ,$and$o ( 1 )$for a quantity which tends to zero as$N  \infty$(we will give more precise definitions later).

Proposition 2.3 (Szemer´edi’s theorem, again). Write$\nu _ { \mathrm { c o n s t } } : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$ for the constant function$\nu _ { \mathrm { c o n s t } } \equiv 1$. Let$0 < \delta \leqslant 1$and$k \geqslant 1$be fixed. Let N be a large integer parameter, and let$f : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$be a nonnegative function obeying the bounds

$$
0 \leqslant f (x) \leqslant \nu_ {\mathrm{const}} (x) \text {   for   all   } x \in \mathbb {Z} _ {N}\tag{2.2}
$$

and

$$
\mathbb {E} (f (x) | x \in \mathbb {Z} _ {N}) \geqslant \delta .\tag{2.3}
$$

Then we have

$$
\mathbb {E} (f (x) f (x + r) \dots f (x + (k - 1) r) | x, r \in \mathbb {Z} _ {N}) \geqslant c (k, \delta) - o _ {k, \delta} (1)
$$

for some constant$c ( k , \delta ) > 0$which does not depend on f or N.

Remark. Ignoring for a moment the curious notation for the constant function$\nu _ { \mathrm { c o n s t } }$, there are two main diferences between this and Proposition 2.1.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x1 + x3 = 2x2, x2 + x4 = 2x3</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>It has become clear that there is a deep connection between harmonic analysis (as applied to solving linear equations in sets of integers) and certain parts of ergodic theory. Particularly exciting is the suspicion that the notion of a k-step nilsystem, explored in many ergodictheoretical works (see e.g. [27], [28], [29], [44]), might be analogous to a kind of “higher order Fourier analysis” which could be used to deal with systems of linear equations that cannot be handled by conventional Fourier analysis (a simple example being the equations x<sub>1</sub> + x<sub>3</sub> = 2x<sub>2</sub>, x<sub>2</sub> + x<sub>4</sub> = 2x<sub>3</sub>, which define an arithmetic progression of length 4). We will not discuss such speculations any further here, but sufice it to say that much is left to be understood.</span></small>

One is the fact that we are dealing with functions rather than sets: however, it is easy to pass from sets to functions, for instance by probabilistic arguments. Another diference, if one unravels the E notation, is that we are now asserting the existence of$\gg N ^ { 2 }$arithmetic progressions, and not just one. Once again, such a statement can be deduced from Proposition 2.1 with some combinatorial trickery (of a less trivial nature this time — the argument was first worked out by Varnavides [43]). A direct proof of Proposition 2.3 can be found in [40]. A formulation of Szemer´edi’s theorem similar to this one was also used by Furstenberg [10]. Combining this argument with the one in Gowers gives an explicit bound on$c ( k , \delta )$of the form$c ( k , \delta ) \geqslant \exp ( - \exp ( \delta ^ { - c _ { k } } ) )$for some $c _ { k } > 0$

Now let us abandon the notion that ν is the constant function. We say that$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$is a measure<sup>4</sup> if

$$
\mathbb {E} (\nu) = 1 + o (1).\tag{2.4}
$$

We are going to exhibit a class of measures, more general than the constant function$\nu _ { \mathrm { c o n s t } }$, for which Proposition 2.3 still holds. These measures, which we will call pseudorandom, will be ones satisfying two conditions called the linear forms condition and the correlation condition. These are, of course, defined formally below, but let us remark that they are very closely related to the ergodic-theory notion of weak-mixing. It is perfectly possible for a “singular” measure — for instance, a measure for which$\mathbb { E } ( \nu ^ { 2 } )$grows like a power of log N — to be pseudorandom. Singular measures are the ones that will be of interest to us, since they generally support rather sparse sets. This generalisation of Proposition 2.3 is Theorem 3.5 below.

Once Theorem 3.5 is proved, we turn to the issue of finding primes in AP. A possible choice for ν would be Λ, the von Mangoldt function (this is defined to equal log p at$\begin{array} { r } { p ^ { m } , m = 1 , 2 , \dots } \end{array}$, and 0 otherwise). Unfortunately, verifying the linear forms condition and the correlation condition for the von Mangoldt function (or minor variants thereof) is strictly harder than proving that the primes contain long arithmetic progressions; indeed, this task is comparable in dificulty to the notorious Hardy-Littlewood prime tuples conjecture, for which our methods here yield no progress.

However, all we need is a measure ν which (after rescaling by at most a constant factor) majorises Λ pointwise. Then, (2.3) will be satisfied with $f = \Lambda$. Such a measure is provided to$\mathrm { u s ^ { 5 } }$by recent work of Goldston and

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Z<sub>N</sub> ,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Vconst</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>The term normalized probability density might be more accurate here, but measure has the advantage of brevity. One may think of ν<sub>const</sub> as the uniform probability distribution on and ν as some other probability distribution which can concentrate on a subset ofZ<sub>N</sub> of very small density (e.g. it may concentrate on the “almost primes” in[1, N]).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>Actually, there is an extra technicality which is caused by the very irregular distribution of primes in arithmetic progressions to small moduli (there are no primes congruent to 4(mod 6),</span></small>

Yıldırım [17] concerning the size of gaps between primes. The proof that the linear forms condition and the correlation condition are satisfied is heavily based on their work, so much so that parts of the argument are placed in an appendix.

The idea of using a majorant to study the primes is by no means new — indeed in some sense sieve theory is precisely the study of such objects. For another use of a majorant in an additive-combinatorial setting, see [33], [34].

It is now timely to make a few remarks concerning the proof of Theorem 3.5. It is in the first step of the proof that our original investigations began, when we made a close examination of Gowers’ arguments. If$f : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$ is a function then the normalised count of k-term arithmetic progressions

$$
\mathbb {E} (f (x) f (x + r) \dots f (x + (k - 1) r) | x, r \in \mathbb {Z} _ {N})\tag{2.5}
$$

is closely controlled by certain norms$\| \cdot \| _ { U ^ { d } }$, which we would like to call the Gowers uniformity norms.<sup>6</sup> They are defined in §5. The formal statement of this fact can be called a generalised von Neumann theorem. Such a theorem, in the case$\nu = \nu _ { \mathrm { c o n s t } }$, was proved by Gowers [19] as a first step in his proof of Szemer´edi’s theorem, using$k { - } 2$applications of the Cauchy-Schwarz inequality. In Proposition 5.3 we will prove a generalised von Neumann theorem relative to an arbitrary pseudorandom measure ν. Our main tool is again the Cauchy-Schwarz inequality. We will use the term Gowers uniform loosely to describe a function which is small in some$U ^ { d }$norm. This should not be confused with the term pseudorandom, which will be reserved for measures on$\mathbb { Z } _ { N }$

Sections 6–8 are devoted to concluding the proof of Theorem 3.5. Very roughly the strategy will be to decompose the function$f$under consideration into a Gowers uniform component plus a bounded “Gowers anti-uniform” object (plus a negligible error). The notion<sup>7</sup> of Gowers anti-uniformity is captured using the dual norms$( U ^ { d } ) ^ { * }$, whose properties are laid out in §6.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>W</sup> <sup>=</sup> p<w(N) <sup>p</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">w(N)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">W-trick,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">n ≡ 1(mod W)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">for example). We get around this using something which we refer to as the which basically consists of restricting the primes to the arithmetic progression , where and  tends slowly to infinity with N. Although this looks like a trick, it is actually an extremely important feature of that part of our argument which concerns primes.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>Analogous objects have recently surfaced in the genuinely ergodic-theoretical work of Host and Kra [27], [28], [29] concerning nonconventional ergodic averages, thus enhancing the connection between ergodic theory and additive number theory.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>We note that Gowers uniformity, which is a measure of “randomness”, “uniform distribution”, or “unbiasedness” in a function should not be confused with the very diferent notion of uniform boundedness. Indeed, in our arguments, the Gowers uniform functions will be highly unbounded, whereas the Gowers anti-uniform functions will be uniformly bounded. Anti-uniformity can in fact be viewed as a measure of “smoothness”, “predictability”, “structure”, or “almost periodicity”.</span></small>

The contribution of the Gowers-uniform part to the count (2.5) will be neg-$\mathrm { l i g i b l e } ^ { 8 }$by the generalised von Neumann theorem. The contribution from the Gowers anti-uniform component will be bounded from below by Szemer´edi’s theorem in its traditional form, Proposition 2.3.

## 3. Pseudorandom measures

In this section we specify exactly what we mean by a pseudorandom measure on$\mathbb { Z } _ { N }$. First, however, we set up some notation. We fix the length k of the arithmetic progressions we are seeking.$N = | \mathbb { Z } _ { N } |$will always be assumed to be prime and large (in particular, we can invert any of the numbers$1 , \ldots , k$ in$\mathbb { Z } _ { N } )$, and we will write$o ( 1 )$for a quantity that tends to zero as$N  \infty$ We will write$O ( 1 )$for a bounded quantity. Sometimes quantities of this type will tend to zero (resp. be bounded) in a way that depends on some other, typically fixed, parameters. If there is any danger of confusion as to what is being proved, we will indicate such dependence using subscripts, thus for instance $O _ { j , \varepsilon } ( 1 )$) denotes a quantity whose magnitude is bounded by$C ( j , \varepsilon )$for some quantity$C ( j , \varepsilon ) > 0$depending only on$j , \varepsilon .$. Since every quantity in this paper will depend on$k ,$however, we will not bother indicating the k dependence throughout. As is customary we often abbreviate$O ( 1 ) X$and$o ( 1 ) X$as$O ( X )$ and$o ( X )$respectively for various nonnegative quantities$X$

If A is a finite nonempty set (for us A is usually just$\mathbb { Z } _ { N } )$and$f : A  \mathbb { R }$ is a function, we write$\mathbb { E } ( f ) : = \mathbb { E } ( f ( x ) | x \in A )$for the average value of$f ;$that is to say

$$
\mathbb {E} (f) := \frac {1}{| A |} \sum_ {x \in A} f (x).
$$

Here, as is usual, we write$| A |$for the cardinality of the set$A .$More generally, $P ( x )$is any statement concerning an element of A which is true for at least one$x \in A$, we define

$$
\mathbb {E} (f (x) | P (x)) := \frac {\sum_ {x \in A : P (x)} f (x)}{| \{x \in A : P (x) \} |}.
$$

This notation extends to functions of several variables in the obvious manner. We now define two notions of randomness for a measure, which we term the linear forms condition and the correlation condition.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>Using the language of ergodic theory, we are essentially claiming that the Gowers anti-uniform functions form a characteristic factor for the expression (2.5). The point is that even though f is not necessarily bounded uniformly, the fact that it is bounded pointwise by a pseudorandom measure ν allows us to conclude that the projection of to the Gowers anti-uniform component is bounded, at which point we can invoke the standard Szemer´edi theorem.</span></small>

Definition 3.1 (Linear forms condition). Let$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$be a measure. Let$m _ { 0 } , t _ { 0 }$and$L _ { 0 }$be small positive integer parameters. Then we say that ν satisfies the$( m _ { 0 } , t _ { 0 } , L _ { 0 } )$-linear forms condition if the following holds. Let$m \leqslant$ $m _ { 0 }$and$t \leqslant t _ { 0 }$be arbitrary, and suppose that$( L _ { i j } ) _ { 1 \leqslant i \leqslant m , 1 \leqslant j \leqslant t }$are arbitrary rational numbers with numerator and denominator at most$L _ { 0 }$in absolute value, and that$b _ { i } , \ 1 \leqslant \ i \leqslant m$, are arbitrary elements of$\mathbb { Z } _ { N }$. For$1 \ \leqslant \ i$ $\leqslant m$, let$\psi _ { i } : \mathbb { Z } _ { N } ^ { t } \to \mathbb { Z } _ { N }$be the linear forms$\begin{array} { r } { \psi _ { i } ( { \bf x } ) = \sum _ { i = 1 } ^ { t } L _ { i j } x _ { j } + b _ { i } } \end{array}$, where $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { t } ) \in \mathbb { Z } _ { N } ^ { t }$, and where the rational numbers$L _ { i j }$are interpreted as elements of$\mathbb { Z } _ { N }$in the usual manner (assuming N is prime and larger than $L _ { 0 } )$. Suppose that as i ranges over$1 , \ldots , m$, the t-tuples$( L _ { i j } ) _ { 1 \leqslant j \leqslant t } \in \mathbb { Q } ^ { t }$are nonzero, and no t-tuple is a rational multiple of any other. Then we have

$$
\mathbb {E} \left(\nu (\psi_ {1} (\mathbf {x})) \dots \nu (\psi_ {m} (\mathbf {x})) \mid \mathbf {x} \in \mathbb {Z} _ {N} ^ {t}\right) = 1 + o _ {L _ {0}, m _ {0}, t _ {0}} (1).\tag{3.1}
$$

Note that the rate of decay in the$o ( 1 )$term is assumed to be uniform in the choice of$b _ { 1 } , \ldots , b _ { m }$

Remarks. It is the parameter$m _ { 0 }$, which controls the number of linear forms, that is by far the most important, and will be kept relatively small. It will eventually be set equal to$k \cdot 2 ^ { k - 1 }$. Note that the$m = 1$case of the linear forms condition recovers the measure condition (2.4). Other simple examples of the linear forms condition which we will encounter later are

$$
\mathbb {E} (\nu (x) \nu (x + h _ {1}) \nu (x + h _ {2}) \nu (x + h _ {1} + h _ {2}) \mid x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N}) = 1 + o (1)\tag{3.2}
$$

(here$( m _ { 0 } , t _ { 0 } , L _ { 0 } ) = ( 4 , 3 , 1 ) )$;

$$
\mathbb {E} \left(\nu \left(x + h _ {1}\right) \nu \left(x + h _ {2}\right) \nu \left(x + h _ {1} + h _ {2}\right) \mid h _ {1}, h _ {2} \in \mathbb {Z} _ {N}\right) = 1 + o (1)\tag{3.3}
$$

for all$x \in \mathbb { Z } _ { N }$(here$( m _ { 0 } , t _ { 0 } , L _ { 0 } ) = ( 3 , 2 , 1 ) )$and

$$
\begin{array}{l} \mathbb {E} \bigg (\nu ((x - y) / 2) \nu ((x - y + h _ {2}) / 2) \nu (- y) \nu (- y - h _ {1}) \\ \quad \times \nu ((x - y ^ {\prime}) / 2) \nu ((x - y ^ {\prime} + h _ {2}) / 2) \nu (- y ^ {\prime}) \nu (- y ^ {\prime} - h _ {1}) \\ \quad \quad \times \nu (x) \nu (x + h _ {1}) \nu (x + h _ {2}) \nu (x + h _ {1} + h _ {2})   \Big |   x, h _ {1}, h _ {2}, y, y ^ {\prime} \in \mathbb {Z} _ {N} \bigg) \\ = 1 + o (1) \end{array}\tag{3.4}
$$

(here$( m _ { 0 } , t _ { 0 } , L _ { 0 } ) = ( 1 2 , 5 , 2 ) )$. For those readers familiar with the Gowers uniformity norms$U ^ { k - 1 }$(which we shall discuss in detail later), the example (3.2) demonstrates that$\nu$is close to 1 in the$U ^ { 2 }$norm (see Lemma 5.2). Similarly, the linear forms condition with appropriately many parameters implies that$\nu$ is close to 1 in the$U ^ { d }$norm, for any fixed$d \geqslant 2$. However, the linear forms condition is much stronger than simply asserting that$\| \nu - 1 \| _ { U ^ { d } }$is small for various d.

For the application to the primes, the measure ν will be constructed using truncated divisor sums, and the linear forms condition will be deduced from some arguments of Goldston and Yıldırım. From a probabilistic point of view, the linear forms condition is asserting a type of joint independence between the “random variables”$\nu ( \psi _ { j } ( \mathbf { x } ) )$; in the application to the primes, ν will be concentrated on the “almost primes”, and the linear forms condition is then saying that the events${ \bf \ddot { \boldsymbol { \psi } } } _ { j } ( { \bf x } )$is almost prime” are essentially independent of each other as$j$varies.<sup>9</sup>

Definition 3.2 (Correlation condition). Let$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$be a measure, and let m<sub>0</sub> be a positive integer parameter. We say that ν satisfies the$m _ { 0 ^ { - } }$ correlation condition if for every$1 < m \leqslant$m<sub>0</sub> there exists a weight function $\tau = \tau _ { m } : \mathbb { Z } _ { N } \longrightarrow \mathbb { R } ^ { + }$which obeys the moment conditions

$$
\mathbb {E} (\tau^ {q}) = O _ {m, q} (1)\tag{3.5}
$$

for all$1 \leqslant q < \infty$and is such that

$$
\mathbb {E} (\nu (x + h _ {1}) \nu (x + h _ {2}) \dots \nu (x + h _ {m}) \mid x \in \mathbb {Z} _ {N}) \leqslant \sum_ {1 \leqslant i <   j \leqslant m} \tau (h _ {i} - h _ {j})\tag{3.6}
$$

for all$h _ { 1 } , \ldots , h _ { m } \in \mathbb { Z } _ { N }$(not necessarily distinct).

Remarks. The condition (3.6) may look a little strange, since if ν were to be chosen randomly then we would expect such a condition to hold with $1 + o ( 1 )$on the right-hand side, at least when$h _ { 1 } , \ldots , h _ { m }$are distinct. Note that one cannot use the linear forms condition to control the left-hand side of (3.6) because the linear components of the forms$x + h _ { j }$are all the same. The correlation condition has been designed with the primes in mind,<sup>10</sup> because in that case we must tolerate slight “arithmetic” nonuniformities. Observe, for example, that the number of$p \leqslant$N for which$p - h$is also prime is not bounded above by a constant times$N / \log ^ { 2 } N$if h contains a very large number of prime factors, although such exceptions will of course be very rare and one still expects to have moment conditions such as (3.5). It is phenomena like this which prevent us from assuming an$L ^ { \infty }$bound for τ . While$m _ { 0 }$will be restricted to be small (in fact, equal to$2 ^ { k - 1 } )$, it will be important for us that there is no upper bound required on$q$(which we will eventually need to be a very large function of k, but still independent of N of course). Since the correlation condition is an upper bound rather than an asymptotic, it is fairly easy to obtain; we shall prove it using the arguments of Goldston and Yıldırım (since we are using those methods in any case to prove the linear forms condition), but these upper bounds could also be obtained by more standard sieve theory methods.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>This will only be true after first eliminating some local correlations in the almost primes arising from small divisors. This will be achieved by a simple “W-trick” which we will come to later in this paper.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">{1, . . . , N}</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>10</sup>A simpler, but perhaps less interesting, model case occurs when one is trying to prove Szemer´edi’s theorem relative to a random subset of of density 1/ log N (cf. [30]). The pseudorandom weight ν would then be a Bernoulli random variable, with each equalν(x) to log N with independent probability 1/ log N and equal to 0 otherwise. In such a case, we can (with high probability) bound the left-hand side of (3.6) more cleanly by O(1) (and even obtain the asymptotic when the h<sub>j</sub> are distinct, and by otherwise.1 + o(1))hO(log<sup>m</sup> N)</span></small>

Definition 3.3 (Pseudorandom measures). Let$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$be a measure. We say that ν is k-pseudorandom if it satisfies the$( k { \cdot } 2 ^ { k - 1 } , 3 k { - } 4 , k )$-linear forms condition and also the$2 ^ { k - 1 }$-correlation condition.

Remarks. The exact values$k \cdot 2 ^ { k - 1 } , 3 k - 4 , k , 2 ^ { k - 1 }$of the parameters chosen here are not too important; in our application to the primes, any quantities which depend only on k would sufice. It can be shown that if$C = C _ { k } > 1$is any constant independent of N and if$S \subseteq \mathbb { Z } _ { N }$is chosen at random, each$x \in \mathbb { Z } _ { N }$ being selected to lie in S independently, at random with probability$1 / \log ^ { C } N$ then (with high probability) the measure$\nu = \log ^ { C } N \mathbf { 1 } _ { S }$is k-pseudorandom, and the Hardy-Littlewood prime tuples conjecture can be viewed as an assertion that the von Mangoldt function is essentially of this form (once one eliminates the obvious obstructions to pseudorandomness coming from small prime divisors). While we will of course not attempt to establish this conjecture here, in §9 we will construct pseudorandom measures which are concentrated on the almost primes instead of the primes; this is of course consistent with the so-called “fundamental lemma of sieve theory”, but we will need a rather precise variant of this lemma due to Goldston and Yıldırım.

The function$\nu _ { \mathrm { c o n s t } } \equiv 1$is clearly k-pseudorandom for any k. In fact the pseudorandom measures are star-shaped around the constant measure:

Lemma 3.4. Let ν be a k-pseudorandom measure. Then

$$
\nu_ {1 / 2} := (\nu + \nu_ {\mathrm{const}}) / 2 = (\nu + 1) / 2
$$

is also a k-pseudorandom measure (though possibly with slightly diferent bounds in the$O ( )$and o() terms).

Proof. It is clear that$\nu _ { 1 / 2 }$is nonnegative and has expectation$1 + o ( 1 )$. To verify the linear forms condition (3.1), we simply replace ν by$( \nu + 1 ) / 2$in the definition and expand as a sum of$2 ^ { m }$terms, divided by$2 ^ { m }$. Since each term can be verified to be$1 + o ( 1 )$by the linear forms condition (3.1), the claim follows. The correlation condition is verified in a similar manner. (A similar result holds for$( 1 - \theta ) \nu + \theta \nu _ { \mathrm { c o n s t } }$for any$0 \leqslant \theta \leqslant 1$, but we will not need to use this generalization.)□

The following result is one of the main theorems of the paper. It asserts that for the purposes of Szemer´edi’s theorem (and ignoring o(1) errors), there is no distinction between a k-pseudorandom measure ν and the constant measure ν<sub>const</sub>.

Theorem 3.5 (Szemer´edi’s theorem relative to a pseudorandom measure). Let$k \geqslant 3$and$0 < \delta \leqslant 1$be fixed parameters. Suppose that ν :$\mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$ is k-pseudorandom. Let$f : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$be any nonnegative function obeying the bound

$$
0 \leqslant f (x) \leqslant \nu (x) \text {   for   all   } x \in \mathbb {Z} _ {N}\tag{3.7}
$$

and

$$
\mathbb {E} (f) \geqslant \delta .\tag{3.8}
$$

Then

$$
\mathbb {E} (f (x) f (x + r) \dots f (x + (k - 1) r) | x, r \in \mathbb {Z} _ {N}) \geqslant c (k, \delta) - o _ {k, \delta} (1)\tag{3.9}
$$

where$c ( k , \delta ) > 0$is the same constant which appears in Proposition 2.3. (The decay rate$o _ { k , \delta } ( 1 )$, on the other hand, decays significantly more slowly than that in Proposition 2.3, and depends of course on the decay rates in the linear forms and correlation conditions.)

We remark that while we do not explicitly assume that N is large in Theorem 3.5, we are free to do so since the conclusion (3.9) is trivial when$N =$ $O _ { k , \delta } ( 1 )$. We certainly encourage the reader to think of N as being extremely large compared to other quantities such as k and$\delta ,$and to think of$o ( 1 )$errors as being negligible.

The proof of this theorem will occupy the next few sections, §4–8. Interestingly, the proof requires no Fourier analysis, additive combinatorics, or number theory; the argument is instead a blend of quantitative ergodic theory arguments with some combinatorial estimates related to Gowers uniformity and sparse hypergraph regularity. From §9 onwards we will apply this theorem to the specific case of the primes, by establishing a pseudorandom majorant for (a modified version of) the von Mangoldt function.

## 4. Notation

We now begin the proof of Theorem 3.5. Thoughout this proof we fix the parameter$k \geqslant 3$and the probability density ν appearing in Theorem 3.5. All our constants in the$O ( )$and$o ( )$notation are allowed to depend on k (with all future dependence on this parameter being suppressed), and are also allowed to depend on the bounds implicit in the right-hand sides of (3.1) and (3.5). We may take N to be suficiently large with respect to k and δ since (3.9) is trivial otherwise.

We need some standard$L ^ { q }$spaces.

Definition 4.1. For every$1 \leqslant q < \infty$and$f : \mathbb { Z } _ { N } \to \mathbb { R }$, we define the L<sup>q</sup> norms as

$$
\| f \| _ {L ^ {q}} := \mathbb {E} (| f | ^ {q}) ^ {1 / q}
$$

with the usual convention that$\| f \| _ { L ^ { \infty } } : = \operatorname* { s u p } _ { x \in \mathbb { Z } _ { N } } | f ( x ) |$. We let$L ^ { q } ( \mathbb { Z } _ { N } )$be the Banach space of all functions from$\mathbb { Z } _ { N }$to R equipped with the$L ^ { q }$norm; of course since$\mathbb { Z } _ { N }$is finite these spaces are all equal to each other as vector spaces, but the norms are only equivalent up to powers of N. We also observe that$L ^ { 2 } ( \mathbb { Z } _ { N } )$is a real Hilbert space with the usual inner product

$$
\langle f, g \rangle := \mathbb {E} (f g).
$$

If Ω is a subset of$\mathbb { Z } _ { N }$, we use$\mathbf { 1 } _ { \Omega } : \mathbb { Z } _ { N }$R to denote the indicator function of Ω, thus$\mathbf { 1 } _ { \Omega } ( x ) = 1 { \mathrm { ~ i f ~ } } x \in \Omega$and$\mathbf { 1 } _ { \Omega } ( x ) = 0$otherwise. Similarly if$P ( x )$is a statement concerning an element$x \in \mathbb { Z } _ { N }$, we write${ \mathbf 1 } _ { P ( x ) }$for$\mathbf { 1 } _ { \{ x \in \mathbb { Z } _ { N } : P ( x ) \} } ( x )$

In our arguments we shall frequently be performing linear changes of variables and then taking expectations. To facilitate this we adopt the following definition. Suppose that A and B are finite, nonempty sets and that$\Phi : A  B$ is a map. Then we say that Φ is a uniform cover of B$b y$A if Φ is surjective and all the fibers$\{ \Phi ^ { - 1 } ( b ) : b \in B \}$have the same cardinality (i.e. they have cardinality$| A | / | B | )$. Observe that if Φ is a uniform cover of B by A, then for any function$f : B \to \mathbb { R }$we have

$$
\mathbb {E} (f (\Phi (a)) | a \in A) = \mathbb {E} (f (b) | b \in B).\tag{4.1}
$$

## 5. Gowers uniformity norms, and a generalized von Neumann theorem

As mentioned in earlier sections, the proof of Theorem 3.5 relies on splitting the given function f into a Gowers uniform component and a Gowers anti-uniform component. We will come to this splitting in later sections, but for this section we focus on defining the notion of Gowers uniformity, introduced in [18], [19]. The main result of this section will be a generalized von Neumann theorem (Proposition 5.3), which basically asserts that Gowers uniform functions are negligible for the purposes of computing sums such as (3.9).

Definition 5.1. Let d$\geqslant 0$be a dimension.<sup>11</sup> We let$\{ 0 , 1 \} ^ { d }$be the standard discrete d-dimensional cube, consisting of d-tuples$\omega = ( \omega _ { 1 } , \ldots , \omega _ { d } )$where $\omega _ { j } \in \{ 0 , 1 \}$for$j = 1 , \ldots , d .$If$h = ( h _ { 1 } , \ldots , h _ { d } ) \in \mathbb { Z } _ { N } ^ { d }$we define$\omega \cdot h : =$ $\omega _ { 1 } h _ { 1 } + . . . + \omega _ { d } h _ { d } . \mathrm { ~ I f ~ } ( f _ { \omega } ) _ { \omega \in \{ 0 , 1 \} ^ { d } }$is a$\{ 0 , 1 \} ^ { d _ { - } }$tuple of functions in$L ^ { \infty } ( \mathbb { Z } _ { N } )$, we define the d-dimensional Gowers inner product$\langle ( f _ { \omega } ) _ { \omega \in \{ 0 , 1 \} ^ { d } } \rangle _ { U ^ { d } }$by the formula

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">d = k − 1,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>11</sup>In practice, we will have  where k is the length of the arithmetic progressions under consideration.</span></small>

$$
\langle (f _ {\omega}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} := \mathbb {E} \left(\prod_ {\omega \in \{0, 1 \} ^ {d}} f _ {\omega} (x + \omega \cdot h) \Bigg | x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {d}\right).\tag{5.1}
$$

Henceforth we shall refer to a configuration$\{ x + \omega \cdot h : \omega \in \{ 0 , 1 \} ^ { d } \}$as a cube of dimension d.

Example. When$d = 2 .$, we have

$$
\begin{array}{l} \langle f _ {0 0}, f _ {1 0}, f _ {0 1}, f _ {1 1} \rangle_ {U ^ {d}} \\ \qquad = \mathbb {E} (f _ {0 0} (x) f _ {1 0} (x + h _ {1}) f _ {0 1} (x + h _ {2}) f _ {1 1} (x + h _ {1} + h _ {2}) \mid x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N}). \end{array}
$$

We recall from [19] the positivity properties of the Gowers inner product (5.1) when d$\geqslant 1$(the$d = 0$case being trivial). First suppose that$f _ { \omega }$does not depend on the final digit$\omega _ { d }$of$\omega ,$thus$f _ { \omega } = f _ { \omega _ { 1 } , \dots , \omega _ { d - 1 } }$. Then we may rewrite (5.1) as

$$
\begin{array}{l} \langle (f _ {\omega}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} = \mathbb {E} \bigg (\prod_ {\omega^ {\prime} \in \{0, 1 \} ^ {d - 1}} f _ {\omega^ {\prime}} (x + \omega^ {\prime} \cdot h ^ {\prime}) f _ {\omega^ {\prime}} (x + h _ {d} + \omega^ {\prime} \cdot h ^ {\prime}) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad x \in \mathbb {Z} _ {N}, h ^ {\prime} \in \mathbb {Z} _ {N} ^ {d - 1}, h _ {d} \in \mathbb {Z} _ {N} \bigg), \end{array}
$$

where we write$\omega ^ { \prime } : = ( \omega _ { 1 } , \ldots , \omega _ { d - 1 } )$and$h ^ { \prime } : = ( h _ { 1 } , \ldots , h _ { d - 1 } )$. This can be rewritten further as

$$
\langle (f _ {\omega}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} = \mathbb {E} \bigg (\left| \mathbb {E} \big (\prod_ {\omega^ {\prime} \in \{0, 1 \} ^ {d - 1}} f _ {\omega^ {\prime}} (y + \omega^ {\prime} \cdot h ^ {\prime}) | y \in \mathbb {Z} _ {N} \big) \right| ^ {2} \Bigg | h ^ {\prime} \in \mathbb {Z} _ {N} ^ {d - 1} \bigg),\tag{5.2}
$$

so in particular we have the positivity property$\langle ( f _ { \omega } ) _ { \omega \in \{ 0 , 1 \} ^ { d } } \rangle _ { U ^ { d } } \geqslant 0$when$f _ { \omega }$ is independent of$\omega _ { d }$. This proves the positivity property

$$
\langle (f) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} \geqslant 0\tag{5.3}
$$

when$d \geqslant 1$. We can thus define the Gowers uniformity norm$\| f \| _ { U ^ { d } }$of a function$f : \mathbb { Z } _ { N } \to \mathbb { R }$by the formula

$$
\| f \| _ {U ^ {d}} := \langle (f) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} ^ {1 / 2 ^ {d}} = \mathbb {E} \left(\prod_ {\omega \in \{0, 1 \} ^ {d}} f (x + \omega \cdot h) \mid x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {d}\right) ^ {1 / 2 ^ {d}}.\tag{5.4}
$$

When$f _ { \omega }$does depend on$\omega _ { d } ,$(5.2) must be rewritten as

$$
\begin{array}{l} \langle (f _ {\omega}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} = \mathbb {E} \bigg (\mathbb {E} \big (\prod_ {\omega^ {\prime} \in \{0, 1 \} ^ {d - 1}} f _ {\omega^ {\prime}, 0} (y + \omega^ {\prime} \cdot h ^ {\prime}) | y \in \mathbb {Z} _ {N} \big) \\ \qquad \qquad \qquad \times   \mathbb {E} \big (\prod_ {\omega^ {\prime} \in \{0, 1 \} ^ {d - 1}} f _ {\omega^ {\prime}, 1} (y + \omega^ {\prime} \cdot h ^ {\prime}) | y \in \mathbb {Z} _ {N} \big) \bigg | h ^ {\prime} \in \mathbb {Z} _ {N} ^ {d - 1} \bigg). \end{array}
$$

From the Cauchy-Schwarz inequality in the h<sup></sup> variables, we thus see that

$$
| \langle (f _ {\omega}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} | \leqslant \langle (f _ {\omega^ {\prime}, 0}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} ^ {1 / 2} \langle (f _ {\omega^ {\prime}, 1}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} ^ {1 / 2},
$$

similarly if we replace the role of the$\omega _ { d }$digit by any of the other digits. Applying this Cauchy-Schwarz inequality once in each digit, we obtain the Gowers Cauchy-Schwarz inequality

$$
| \langle (f _ {\omega}) _ {\omega \in \{0, 1 \} ^ {d}} \rangle_ {U ^ {d}} | \leqslant \prod_ {\omega \in \{0, 1 \} ^ {d}} \| f _ {\omega} \| _ {U ^ {d}}.\tag{5.5}
$$

From the multilinearity of the inner product, and the binomial formula, we then obtain the inequality

$$
\left| \left\langle (f + g) _ {\omega \in \{0, 1 \} ^ {d}} \right\rangle_ {U ^ {d}} \right| \leqslant \left(\left\| f \right\| _ {U ^ {d}} + \left\| g \right\| _ {U ^ {d}}\right) ^ {2 ^ {d}}
$$

whence we obtain the Gowers triangle inequality

$$
\| f + g \| _ {U ^ {d}} \leqslant \| f \| _ {U ^ {d}} + \| g \| _ {U ^ {d}}.
$$

(cf. [19, Lemmas 3.8 and 3.9]).

Example. Continuing the$d = 2$example, we have

$$
\| f \| _ {U ^ {2}} := \mathbb {E} (f (x) f (x + h _ {1}) f (x + h _ {2}) f (x + h _ {1} + h _ {2}) \mid x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N}) ^ {1 / 4}
$$

and the Gowers Cauchy-Schwarz inequality then states

$$
\begin{array}{c} | \mathbb {E} (f _ {0 0} (x) f _ {1 0} (x + h _ {1}) f _ {0 1} (x + h _ {2}) f _ {1 1} (x + h _ {1} + h _ {2}) | x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N}) | \\ \leqslant \| f _ {0 0} \| _ {U ^ {2}} \| f _ {1 0} \| _ {U ^ {2}} \| f _ {0 1} \| _ {U ^ {2}} \| f _ {1 1} \| _ {U ^ {2}}. \end{array}
$$

Applying this with$f _ { 1 0 } , f _ { 0 1 } , f _ { 1 1 }$set equal to Kronecker delta functions, one can easily verify that

$$
f _ {0 0} \equiv 0 \text { whenever } \| f _ {0 0} \| _ {U ^ {2}} = 0.
$$

This, combined with the preceding discussion, shows that the$U ^ { 2 }$norm is indeed a genuine norm. This can also be seen by the easily verified identity

$$
\| f \| _ {U ^ {2}} = \big (\sum_ {\xi \in \mathbb {Z} _ {N}} | \widehat {f} (\xi) | ^ {4} \big) ^ {1 / 4}
$$

(cf. [19, Lemma 2.2]), where the Fourier transform$\hat { f } : \mathbb { Z } _ { N } \to \mathbb { C }$of$f$is defined by the formula<sup>12</sup>

$$
\widehat {f} (\xi) := \mathbb {E} (f (x) e ^ {- 2 \pi i x \xi / N} | x \in \mathbb {Z} _ {N}).
$$

for any$\xi \in \mathbb { Z } _ { N }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">k = 3</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>12</sup>The Fourier transform of course plays a hugely important rˆole in the k = 3 theory, and provides some very useful ideas to then think about the higher k theory, but will not be used in this paper except as motivation.</span></small>

We return to the study of general$U ^ { d }$norms. Since

$$
\| \nu_ {\mathrm{const}} \| _ {U ^ {d}} = \| 1 \| _ {U ^ {d}} = 1,\tag{5.6}
$$

we see from (5.5) that

$$
\left| \left\langle \left(f _ {\omega}\right) _ {\omega \in \{0, 1 \} ^ {d}} \right\rangle_ {U ^ {d}} \right| \leqslant \| f \| _ {U ^ {d}} ^ {2 ^ {d - 1}}
$$

where$f _ { \omega } : = 1$when$\omega _ { d } = 1$and$f _ { \omega } : = f$when$\omega _ { d } = 0$. But the left-hand side can easily be computed to be$\| f \| _ { U ^ { d - 1 } } ^ { 2 ^ { d - 1 } }$, and thus we have the monotonicity relation

$$
\| f \| _ {U ^ {d - 1}} \leqslant \| f \| _ {U ^ {d}}\tag{5.7}
$$

for all$d \geqslant 2$. Since the$U ^ { 2 }$norm was already shown to be strictly positive, we see that the higher norms$U ^ { d } , d \geqslant 2$, are also. Thus the$U ^ { d }$norms are genuinely norms for all$d \geqslant 2$. On the other hand, the$U ^ { 1 }$norm is not actually a norm, since one can compute from (5.4) that$\| f \| _ { U ^ { 1 } } = | \mathbb { E } ( f ) |$and thus$\| f \| _ { U ^ { 1 } }$ may vanish without$f$itself vanishing.

From the linear forms condition one can easily verify that$\| \nu \| _ { U ^ { d } } = 1 + o ( 1 )$ (cf. (3.2)). In fact more is true, namely that pseudorandom measures ν are close to the constant measure$\nu _ { \mathrm { c o n s t } }$in the$U ^ { d }$norms; this is of course consistent with our aim of deducing Theorem 3.5 from Theorem 2.3.

Lemma 5.2. Suppose that ν is k-pseudorandom (as defined in$D e f i n i -$ tion 3.3). Then

$$
\left\| \nu - \nu_ {\mathrm{const}} \right\| _ {U ^ {d}} = \left\| \nu - 1 \right\| _ {U ^ {d}} = o (1)\tag{5.8}
$$

for all$1 \leqslant d \leqslant k - 1$

Proof. By (5.7) it sufices to prove the claim for$d = k - 1$. Raising to the power$2 ^ { k - 1 }$, it sufices from (5.4) to show that

$$
\mathbb {E} \bigg (\prod_ {\omega \in \{0, 1 \} ^ {k - 1}} (\nu (x + \omega \cdot h) - 1)   \bigg |   x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1} \bigg) = o (1).
$$

The left-hand side can be expanded as

$$
\sum_ {A \subseteq \{0, 1 \} ^ {k - 1}} (- 1) ^ {| A |} \mathbb {E} \left(\prod_ {\omega \in A} \nu (x + \omega \cdot h) \Bigg | x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right).\tag{5.9}
$$

Let us look at the expression

$$
\mathbb {E} \bigg (\prod_ {\omega \in A} \nu (x + \omega \cdot h) \Bigg | x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1} \bigg)\tag{5.10}
$$

for some fixed$A \subseteq \{ 0 , 1 \} ^ { k - 1 }$. This is of the form

$$
\mathbb {E} \left(\nu (\psi_ {1} (\mathbf {x})) \dots \nu (\psi_ {| A |} (\mathbf {x})) \mid \mathbf {x} \in \mathbb {Z} _ {N} ^ {k}\right),
$$

where$\mathbf { x } : = ( x , h _ { 1 } , \dots , h _ { k - 1 } )$and the$\psi _ { 1 } , . . . , \psi _ { | A | }$are some ordering of the $| A |$linear forms$x + \omega \cdot h , \omega \in A$. It is clear that none of these forms is a rational multiple of any other. Thus we may invoke the$( 2 ^ { k - 1 } , k , 1 )$-linear forms condition, which is a consequence of the fact that ν is k-pseudorandom, to conclude that the expression (5.10) is$1 + o ( 1 )$

Referring back to (5.9), one sees that the claim now follows from the binomial theorem$\begin{array} { r } { \sum _ { A \subseteq \{ 0 , 1 \} ^ { k - 1 } } ( - 1 ) ^ { | A | } = ( 1 - 1 ) ^ { 2 ^ { k - 1 } } = 0 } \end{array}$□

It is now time to state and prove our generalised von Neumann theorem, which explains how the expression (3.9), which counts k-term arithmetic progressions, is governed by the Gowers uniformity norms. All of this, of course, is relative to a pseudorandom measure ν.

Proposition 5.3 (Generalised von Neumann). Suppose that ν is k-pseudorandom. Let$f _ { 0 } , \ldots , f _ { k - 1 } \in L ^ { 1 } ( \mathbb { Z } _ { N } )$be functions which are pointwise bounded by$\nu + \nu _ { \mathrm { c o n s t } }$, or in other words

$$
\left| f _ {j} (x) \right| \leqslant \nu (x) + 1 \text {   for   all   } x \in \mathbb {Z} _ {N}, 0 \leqslant j \leqslant k - 1.\tag{5.11}
$$

Let$c _ { 0 } , \ldots , c _ { k - 1 }$be a permutation of some k consecutive elements of$\{ - k +$ $1 , \ldots , - 1 , 0 , 1 , \ldots , k - 1 \}$(in practice we will take$c _ { j } : = j )$. Then

$$
\mathbb {E} \left(\prod_ {j = 0} ^ {k - 1} f _ {j} (x + c _ {j} r) \mid x, r \in \mathbb {Z} _ {N}\right) = O \left(\inf _ {0 \leqslant j \leqslant k - 1} \| f _ {j} \| _ {U ^ {k - 1}}\right) + o (1).
$$

Remark. This proposition is standard when$\nu = \nu _ { \mathrm { c o n s t } }$(see for instance$[ 1 9 .$ Th. 3.2] or, for an analogous result in the ergodic setting, [13, Th. 3.1]). The novelty is thus the extension to the pseudorandom ν studied in Theorem 3.5. The reason we have an upper bound of$\nu ( x ) + 1$instead of$\nu ( x )$is because we shall be applying this lemma to functions$f _ { j }$which roughly have the form $f _ { j } \ = \ f - \mathbb { E } ( f | B )$, where$f$is some function bounded pointwise by$\nu ,$and B is a σ-algebra such that$\mathbb { E } ( \nu | B )$is essentially bounded (up to$o ( 1 )$errors) by 1, so that we can essentially bound$| f _ { j } |$by$\nu ( x ) + 1$; see Definition 7.1 for the notation used here. The techniques are inspired by similar Cauchy-Schwarz arguments relative to pseudorandom hypergraphs in [20]. Indeed, the estimate here can be viewed as a kind of “sparse counting lemma” that utilises a regularity hypothesis (in the guise of$U ^ { k - 1 }$control on one of the$f _ { j } )$to obtain control on an expression which can be viewed as a weighted count of arithmetic progressions concentrated in a sparse set (the support of$\nu )$. See [20], [30] for some further examples of such lemmas.

Proof. By replacing ν with$( \nu + 1 ) / 2$(and by dividing$f _ { j }$by 2), and using Lemma 3.4, we see that we may in fact assume without loss of generality that we can improve (5.11) to

$$
\left| f _ {j} (x) \right| \leqslant \nu (x) \text {   for   all   } x \in \mathbb {Z} _ {N}, 0 \leqslant j \leqslant k - 1.\tag{5.12}
$$

For similar reasons we may assume that ν is strictly positive everywhere.

By permuting the$f _ { j }$and$c _ { j } .$, if necessary, we may assume that the infimum

$$
\inf _ {0 \leqslant j \leqslant k - 1} \| f _ {j} \| _ {U ^ {k - 1}}
$$

is attained when$j = 0$. By shifting x by$c _ { 0 } r$if necessary we may assume that $c _ { 0 } = 0$. Our task is thus to show

$$
\mathbb {E} \left(\prod_ {j = 0} ^ {k - 1} f _ {j} (x + c _ {j} r) \mid x, r \in \mathbb {Z} _ {N}\right) = O \left(\| f _ {0} \| _ {U ^ {k - 1}}\right) + o (1).\tag{5.13}
$$

The proof of this will fall into two parts. First of all we will use the Cauchy-Schwarz inequality$k - 1$times (as is standard in the proof of theorems of this general type). In this way we will bound the left-hand side of (5.13) by a weighted sum of$f _ { 0 }$over$( k - 1 )$-dimensional cubes. After that, we will show using the linear forms condition that these weights are roughly 1 on average, which will enable us to deduce (5.13).

Before we give the full proof, let us first give the argument in the case $k = 3$, with$c _ { j } : = j$. This is conceptually no easier than the general case, but the notation is substantially less fearsome. Our task is to show that

$$
\mathbb {E} \big (f _ {0} (x) f _ {1} (x + r) f _ {2} (x + 2 r) \mid x, r \in \mathbb {Z} _ {N} \big) = O \big (\| f _ {0} \| _ {U ^ {2}} \big) + o (1).
$$

It is convenient to reparametrise the progression$( x , x + r , x + 2 r )$as$( y _ { 1 } + y _ { 2 }$ $y _ { 2 } / 2 , - y _ { 1 } )$. The fact that the first coordinate does not depend on$y _ { 1 }$and the second coordinate does not depend on$y _ { 2 }$will allow us to perform Cauchy-Schwarz in the arguments below without further changes of variable. Since N is a large prime, we are now faced with estimating the quantity

$$
J _ {0} := \mathbb {E} \left(f _ {0} \left(y _ {1} + y _ {2}\right) f _ {1} \left(y _ {2} / 2\right) f _ {2} (- y _ {1}) \mid y _ {1}, y _ {2} \in \mathbb {Z} _ {N}\right).\tag{5.14}
$$

We estimate$f _ { 2 }$in absolute value by ν and bound this by

$$
\left| J _ {0} \right| \leqslant \mathbb {E} \left(\left| \mathbb {E} \left(f _ {0} \left(y _ {1} + y _ {2}\right) f _ {1} \left(y _ {2} / 2\right) \mid y _ {2} \in \mathbb {Z} _ {N}\right) \mid \nu (- y _ {1}) \mid y _ {1} \in \mathbb {Z} _ {N}\right). \right.
$$

Using Cauchy-Schwarz and (2.4), we can bound this by

$$
(1 + o (1)) \mathbb {E} \big (| \mathbb {E} (f _ {0} (y _ {1} + y _ {2}) f _ {1} (y _ {2} / 2) \mid y _ {2} \in \mathbb {Z} _ {N}) | ^ {2} \nu (- y _ {1}) \mid y _ {1} \in \mathbb {Z} _ {N} \big) ^ {1 / 2}
$$

which we rewrite as$( 1 + o ( 1 ) ) J _ { 1 } ^ { 1 / 2 }$, where

$$
J _ {1} := \mathbb {E} \left(f _ {0} \left(y _ {1} + y _ {2}\right) f _ {0} \left(y _ {1} + y _ {2} ^ {\prime}\right) f _ {1} \left(y _ {2} / 2\right) f _ {1} \left(y _ {2} ^ {\prime} / 2\right) \nu (- y _ {1}) \mid y _ {1}, y _ {2}, y _ {2} ^ {\prime} \in \mathbb {Z} _ {N}\right).
$$

We now estimate$f _ { 1 }$in absolute value by$\nu ,$and thus bound

$$
J _ {1} \leqslant \mathbb {E} \left(| \mathbb {E} \left(f _ {0} \left(y _ {1} + y _ {2}\right) f _ {0} \left(y _ {1} + y _ {2} ^ {\prime}\right) \nu (- y _ {1}) \mid y _ {1} \in \mathbb {Z} _ {N}\right) | \nu \left(y _ {2} / 2\right) \nu \left(y _ {2} ^ {\prime} / 2\right) \mid y _ {2}, y _ {2} ^ {\prime} \in \mathbb {Z} _ {N}\right).
$$

Using Cauchy-Schwarz and (2.4) again, we bound this by$1 + o ( 1 )$times

$$
\mathbb {E} \big (| \mathbb {E} (f _ {0} (y _ {1} + y _ {2}) f _ {0} (y _ {1} + y _ {2} ^ {\prime}) \nu (- y _ {1}) | y _ {1} \in \mathbb {Z} _ {N}) | ^ {2} \nu (y _ {2} / 2) \nu (y _ {2} ^ {\prime} / 2) \mid y _ {2}, y _ {2} ^ {\prime} \in \mathbb {Z} _ {N} \big) ^ {1 / 2}.
$$

Putting all this together, we conclude the inequality

$$
| J _ {0} | \leqslant (1 + o (1)) J _ {2} ^ {1 / 4},\tag{5.15}
$$

where

$$
\begin{array}{c} J _ {2} := \mathbb {E} \big (f _ {0} (y _ {1} + y _ {2}) f _ {0} (y _ {1} + y _ {2} ^ {\prime}) f _ {0} (y _ {1} ^ {\prime} + y _ {2}) f _ {0} (y _ {1} ^ {\prime} + y _ {2} ^ {\prime}) \nu (- y _ {1}) \nu (- y _ {1} ^ {\prime}) \nu (y _ {2} / 2) \nu (y _ {2} ^ {\prime} / 2) \\ \big | y _ {1}, y _ {1} ^ {\prime}, y _ {2}, y _ {2} ^ {\prime} \in \mathbb {Z} _ {N} \big). \end{array}
$$

If it were not for the weights involving$\nu , J _ { 2 }$would be the$U ^ { 2 }$norm of$f _ { 0 } ,$and we would be done. If we reparametrise the cube$( y _ { 1 } + y _ { 2 } , y _ { 1 } ^ { \prime } + y _ { 2 } , y _ { 1 } + y _ { 2 } ^ { \prime } , y _ { 1 } ^ { \prime } + y _ { 2 } ^ { \prime } )$ by$( x , x + h _ { 1 } , x + h _ { 2 } , x + h _ { 1 } + h _ { 2 } )$, the above expression becomes

$$
J _ {2} = \mathbb {E} \left(f _ {0} (x) f _ {0} \left(x + h _ {1}\right) f _ {0} \left(x + h _ {2}\right) f _ {0} \left(x + h _ {1} + h _ {2}\right) W \left(x, h _ {1}, h _ {2}\right) \mid x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N}\right)
$$

where$W ( x , h _ { 1 } , h _ { 2 } )$is the quantity

$$
W (x, h _ {1}, h _ {2}) := \mathbb {E} \big (\nu (- y) \nu (- y - h _ {1}) \nu ((x - y) / 2) \nu ((x - y - h _ {2}) / 2) \mid y \in \mathbb {Z} _ {N} \big).\tag{5.16}
$$

In order to compare$J _ { 2 }$to$\| f _ { 0 } \| _ { U ^ { 2 } } ^ { 4 }$, we must compare$W$to 1. To that end it sufices to show that the error

$$
\mathbb {E} \left(f _ {0} (x) f _ {0} \left(x + h _ {1}\right) f _ {0} \left(x + h _ {2}\right) f _ {0} \left(x + h _ {1} + h _ {2}\right) \left(W \left(x, h _ {1}, h _ {2}\right) - 1\right) \mid x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N}\right)
$$

is suitably small (in fact it will be$o ( 1 ) )$. To achieve this we estimate$f _ { 0 }$ in absolute value by$\nu$and use Cauchy-Schwarz one last time to reduce to showing that

$$
\begin{array}{c} \mathbb {E} \big (\nu (x) \nu (x + h _ {1}) \nu (x + h _ {2}) \nu (x + h _ {1} + h _ {2}) (W (x, h _ {1}, h _ {2}) - 1) ^ {n} \\ \Big | x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N} \big) = 0 ^ {n} + o (1) \end{array}
$$

for$n = 0 , 2$. Expanding the$W - 1$term, it sufices to show that

$$
\mathbb {E} \left(\nu (x) \nu \left(x + h _ {1}\right) \nu \left(x + h _ {2}\right) \nu \left(x + h _ {1} + h _ {2}\right) W \left(x, h _ {1}, h _ {2}\right) ^ {q} \mid x, h _ {1}, h _ {2} \in \mathbb {Z} _ {N}\right) = 1 + o (1)
$$

for$q = 0 , 1 , 2$. But this follows from the linear forms condition (for instance, the case$q = 2$is just (3.5)).

We turn now to the proof of (5.13) in general. As one might expect in view of the above discussion, this consists of a large number of applications of Cauchy-Schwarz to replace all the functions$f _ { j }$with$\nu ,$and then applications of the linear forms condition. In order to expedite these applications of Cauchy-Schwarz we shall need some notation. Suppose that$0 \leqslant d \leqslant k - 1$, and that we have two vectors$y = ( y _ { 1 } , \dots , y _ { k - 1 } ) \in \mathbb { Z } _ { N } ^ { k - 1 }$and$y ^ { \prime } = ( y _ { k - d } ^ { \prime } , \ldots , y _ { k - 1 } ^ { \prime } ) \in \mathbb { Z } _ { N } ^ { d }$ of length k − 1 and d respectively. For any set$S \subseteq \{ k - d , \ldots , k - 1 \}$, we define the vector$y ^ { ( S ) } = ( y _ { 1 } ^ { ( S ) } , \ldots , y _ { k - 1 } ^ { ( S ) } ) \in \mathbb { Z } _ { N } ^ { k - 1 }$as

$$
y _ {i} ^ {(S)} := \left\{ \begin{array}{l l} y _ {i} & \text { if } i \not \in S \\ y _ {i} ^ {\prime} & \text { if } i \in S. \end{array} \right.
$$

The set$S$thus indicates which components of$y ^ { ( S ) }$come from$y ^ { \prime }$rather than$y$

Lemma 5.4 (Cauchy-Schwarz). Let$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$be any measure. Let $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { k - 1 } : \mathbb { Z } _ { N } ^ { k - 1 } \to \mathbb { Z } _ { N }$be functions of$k - 1$variables$y _ { 1 } , \ldots , y _ { k - 1 }$such that$\phi _ { i }$does not depend on y<sub>i</sub> for 1$\leqslant i \leqslant k - 1$. Suppose that$f _ { 0 } , f _ { 1 } , \dotsc , f _ { k - 1 } \in$ $L ^ { 1 } ( \mathbb { Z } _ { N } )$are functions satisfying$| f _ { i } ( x ) | \leqslant \nu ( x )$for all$x \in \mathbb { Z } _ { N }$and for each$i ,$ $0 \leqslant i \leqslant k - 1$. For each$0 \leqslant d \leqslant k - 1$, define the quantities

$$
\begin{array}{l} J _ {d} := \mathbb {E} \bigg (\prod_ {S \subseteq \{k - d, \dots , k - 1 \}} \big (\prod_ {i = 0} ^ {k - d - 1} f _ {i} (\phi_ {i} (y ^ {(S)})) \big) \big (\prod_ {i = k - d} ^ {k - 1} \nu^ {1 / 2} (\phi_ {i} (y ^ {(S)})) \big) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{5.17}
$$

and

$$
P _ {d} := \mathbb {E} \bigg (\prod_ {S \subseteq \{k - d, \dots , k - 1 \}} \nu (\phi_ {k - d - 1} (y ^ {(S)})) \Bigg | y \in \mathbb {Z} _ {N} ^ {k - 1}, y ^ {\prime} \in \mathbb {Z} _ {N} ^ {d} \bigg).\tag{5.18}
$$

Then, for any$0 \leqslant d \leqslant k - 2 .$, we have the inequality

$$
\left| J _ {d} \right| ^ {2} \leqslant P _ {d} J _ {d + 1}.\tag{5.19}
$$

Remarks. The appearance of$\nu ^ { 1 / 2 }$in (5.17) may seem odd. Note, however, that since$\phi _ { i }$does not depend on the$i ^ { t h }$variable, each factor of ν<sup>1/2</sup> in (5.17)$\nu ^ { 1 / 2 }$ occurs twice. If one takes$k = 3$and

$$
\phi_ {0} (y _ {1}, y _ {2}) = y _ {1} + y _ {2}, \quad \phi_ {1} (y _ {1}, y _ {2}) = y _ {2} / 2, \quad \phi_ {2} (y _ {1}, y _ {2}) = - y _ {1},\tag{5.20}
$$

then the above notation is consistent with the quantities$J _ { 0 } , J _ { 1 } , J _ { 2 }$defined in the preceding discussion.

Proof of Lemma 5.4. Consider the quantity$J _ { d } .$Since$\phi _ { k - d - 1 }$does not depend on$y _ { k - d - 1 }$, we may take all quantities depending on$\phi _ { k - d - 1 }$outside of the$y _ { k - d - 1 }$average. This allows us to write

$$
J _ {d} = \mathbb {E} \big (G (y, y ^ {\prime}) H (y, y ^ {\prime}) \mid y _ {1}, \ldots , y _ {k - d - 2}, y _ {k - d}, \ldots , y _ {k - 1}, y _ {k - d} ^ {\prime}, \ldots , y _ {k - 1} ^ {\prime} \in \mathbb {Z} _ {N} \big),
$$

where

$$
G (y, y ^ {\prime}) := \prod_ {S \subseteq \{k - d, \dots , k - 1 \}} f _ {k - d - 1} \left(\phi_ {k - d - 1} \left(y ^ {(S)}\right)\right) \nu^ {- 1 / 2} \left(\phi_ {k - d - 1} \left(y ^ {(S)}\right)\right)
$$

and

$$
H (y, y ^ {\prime}) := \mathbb {E} \bigg (\prod_ {S \subseteq \{k - d, \ldots , k - 1 \}} \prod_ {i = 0} ^ {k - d - 2} f _ {i} (\phi_ {i} (y ^ {(S)})) \prod_ {i = k - d - 1} ^ {k - 1} \nu^ {1 / 2} (\phi_ {i} (y ^ {(S)}))   \bigg |   y _ {k - d - 1} \in \mathbb {Z} _ {N} \bigg)
$$

(note we have multiplied and divided by several factors of the form $\dot { \nu } ^ { 1 / 2 } ( \phi _ { k - d - 1 } ( y ^ { ( S ) } ) )$. Now apply Cauchy-Schwarz to give

$$
\begin{array}{l} | J _ {d} | ^ {2} \leqslant \mathbb {E} \big (| G (y, y ^ {\prime}) | ^ {2} \mid y _ {1}, \ldots , y _ {k - d - 2}, y _ {k - d}, \ldots , y _ {k - 1}, y _ {k - d} ^ {\prime}, \ldots , y _ {k - 1} ^ {\prime} \in \mathbb {Z} _ {N} \big) \\ \qquad \times \mathbb {E} \big (| H (y, y ^ {\prime}) | ^ {2} \mid y _ {1}, \ldots , y _ {k - d - 2}, y _ {k - d}, \ldots , y _ {k - 1}, y _ {k - d} ^ {\prime}, \ldots , y _ {k - 1} ^ {\prime} \in \mathbb {Z} _ {N} \big). \end{array}
$$

Since$| f _ { k - d - 1 } ( x ) | \leqslant \nu ( x )$for all$x ,$one sees from (5.18) that

$$
\mathbb {E} \big (| G (y, y ^ {\prime}) | ^ {2} \mid y _ {1}, \ldots , y _ {k - d - 2}, y _ {k - d}, \ldots , y _ {k - 1}, y _ {k - d} ^ {\prime}, \ldots , y _ {k - 1} ^ {\prime} \in \mathbb {Z} _ {N} \big) \leqslant P _ {d}
$$

(note that the$y _ { k - d - 1 }$averaging in (5.18) is redundant since$\phi _ { k - d - 1 }$does not depend on this variable). Moreover, by writing in the definition of$H ( y , y ^ { \prime } )$ and expanding the square, replacing the averaging variable$y _ { k - d - 1 }$with the new variables$y _ { k - d - 1 } , y _ { k - d - 1 } ^ { \prime } .$, one sees from (5.17) that

$$
\mathbb {E} \big (| H (y, y ^ {\prime}) | ^ {2} \mid y _ {1}, \dots , y _ {k - d - 2}, y _ {k - d}, \dots , y _ {k - 1}, y _ {k - d} ^ {\prime}, \dots , y _ {k - 1} ^ {\prime} \in \mathbb {Z} _ {N} \big) = J _ {d + 1}.
$$

The claim follows.

Applying the above lemma$k - 1$times, we obtain in particular that

$$
\left| J _ {0} \right| ^ {2 ^ {k - 1}} \leqslant J _ {k - 1} \prod_ {d = 0} ^ {k - 2} P _ {d} ^ {2 ^ {k - 2 - d}}.\tag{5.21}
$$

Observe from (5.17) that

$$
J _ {0} = \mathbb {E} \left(\prod_ {i = 0} ^ {k - 1} f _ {i} \left(\phi_ {i} (y)\right) \mid y \in \mathbb {Z} _ {N} ^ {k - 1}\right).\tag{5.22}
$$

Proof of Proposition 5.3. We will apply (5.21), observing that (5.22) can be used to count configurations$( x , x + c _ { 1 } r , \ldots , x + c _ { k - 1 } r )$by making a judicious choice of the functions$\phi _ { i }$. For$y = \left( y _ { 1 } , \ldots , y _ { k - 1 } \right)$, take

$$
\phi_ {i} (y) := \sum_ {j = 1} ^ {k - 1} \left(1 - \frac {c _ {i}}{c _ {j}}\right) y _ {j}
$$

for$i = 0 , \ldots , k - 1$. Then$\phi _ { 0 } ( y ) = y _ { 1 } + \cdot \cdot \cdot + y _ { k - 1 } , \phi _ { i } ( y )$does not depend on $y _ { i }$and, as one can easily check, for any y we have$\phi _ { i } ( y ) = x + c _ { i } r$where

$$
r = - \sum_ {i = 1} ^ {k - 1} \frac {y _ {i}}{c _ {i}}.
$$

Note that (5.20) is simply the case$k = 3 , c _ { j } = j$of this more general construction. Now the map$\Phi : \mathbb { Z } _ { N } ^ { k - 1 } \to \mathbb { Z } _ { N } ^ { 2 }$defined by

$$
\Phi (y) := \left(y _ {1} + \dots + y _ {k - 1}, \frac {y _ {1}}{c _ {1}} + \frac {y _ {2}}{c _ {2}} + \dots + \frac {y _ {k - 1}}{c _ {k - 1}}\right)
$$

is a uniform cover, and so

$$
\mathbb {E} \bigg (\prod_ {j = 0} ^ {k - 1} f _ {j} (x + c _ {j} r) \Big | x, r \in \mathbb {Z} _ {N} \bigg) = \mathbb {E} \bigg (\prod_ {i = 0} ^ {k - 1} f _ {i} (\phi_ {i} (y)) \Big | y \in \mathbb {Z} _ {N} ^ {k - 1} \bigg) = J _ {0}\tag{5.23}
$$

thanks to (5.22) (this generalises (5.14)). On the other hand we have$P _ { d } =$ $1 + o ( 1 )$for each$0 \leqslant d \leqslant k - 2$, since the k-pseudorandom hypothesis on ν implies the$( 2 ^ { d } , k - 1 + d , k )$-linear forms condition. Applying (5.21) we thus obtain

$$
J _ {0} ^ {2 ^ {k - 1}} \leqslant (1 + o (1)) J _ {k - 1}\tag{5.24}
$$

(this generalises (5.15)). Fix$y \ \in \ \mathbb { Z } _ { N } ^ { k - 1 }$. As S ranges over all subsets of $\{ 1 , \ldots , k - 1 \} , \ \phi _ { 0 } ( y ^ { ( S ) } )$ranges over a$( k - 1 )$-dimensional cube$\{ x + \omega \cdot h :$ $\omega \in \{ 0 , 1 \} ^ { k - 1 } \}$where$x = y _ { 1 } + \cdot \cdot \cdot + y _ { k - 1 }$and$h _ { i } = y _ { i } ^ { \prime } - y _ { i } , i = 1 , \ldots , k - 1$ Thus we may write

$$
J _ {k - 1} = \mathbb {E} \left(W (x, h) \prod_ {\omega \in \{0, 1 \} ^ {k - 1}} f _ {0} (x + \omega \cdot h) \mid x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right)\tag{5.25}
$$

where the weight function$W ( x , h )$is given by

$$
\begin{aligned} W(x,h) = & \mathbb{E}\bigg(\prod_{\omega \in \{0,1\}^{k - 1}}\prod_{i = 1}^{k - 1}\nu^{1 / 2}(\phi_{i}(y + \omega h))\bigg|  y_{1},\ldots ,y_{k - 2}\in \mathbb{Z}_{N}\bigg)\\ = & \mathbb{E}\bigg(\prod_{i = 1}^{k - 1}\prod_{\substack{\omega \in \{0,1\}^{k - 1}\\ \omega_{i} = 0}}\nu (\phi_{i}(y + \omega h))\bigg|  y_{1},\ldots ,y_{k - 2}\in \mathbb{Z}_{N}\bigg) \end{aligned}
$$

(this generalises (5.16)). Here, ωh$\epsilon \ Z _ { N } ^ { k - 1 }$is the vector with components $( \omega h ) _ { j } : = \omega _ { j } h _ { j }$for$1 \leqslant j \leqslant k - 1$, and$y \in \overset { \cdot \cdot } { \mathbb { Z } } _ { N } ^ { k - 1 }$is the vector with components $y _ { j }$for$1 \leqslant j \leqslant k - 2$and$y _ { k - 1 } : = x - y _ { 1 } - . . . - y _ { k - 2 }$. Now by the definition of the$U ^ { k - 1 }$norm we have

$$
\mathbb {E} \left(\prod_ {\omega \in \{0, 1 \} ^ {k - 1}} f _ {0} (x + \omega \cdot h) \Bigg | x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right) = \| f _ {0} \| _ {U ^ {k - 1}} ^ {2 ^ {k - 1}}.
$$

To prove (5.13) it therefore sufices, by (5.23), (5.24) and (5.25), to prove that

$$
\mathbb {E} \left(\left(W (x, h) - 1\right) \prod_ {\omega \in \{0, 1 \} ^ {k - 1}} f _ {0} (x + \omega \cdot h) \mid x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right) = o (1).
$$

Using (5.12), it sufices to show that

$$
\mathbb {E} \left(\left| W (x, h) - 1 \right| \prod_ {\omega \in \{0, 1 \} ^ {k - 1}} \nu (x + \omega \cdot h) \mid x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right) = o (1).
$$

Thus by Cauchy-Schwarz it will be enough to prove

Lemma 5.5 (ν covers its own cubes uniformly). For$n = 0 , 2$2

$$
\mathbb {E} \left(| W (x, h) - 1 | ^ {n} \prod_ {\omega \in \{0, 1 \} ^ {k - 1}} \nu (x + \omega \cdot h) \mid x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right) = 0 ^ {n} + o (1).
$$

Proof. Expanding out the square, it then sufices to show that

$$
\mathbb {E} \left(W (x, h) ^ {q} \prod_ {\omega \in \{0, 1 \} ^ {k - 1}} \nu (x + \omega \cdot h) \mid x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right) = 1 + o (1)
$$

for$q = 0 , 1 , 2$. This can be achieved by three applications of the linear forms condition, as follows:

$q = 0$. Use the$( 2 ^ { k - 1 } , k , 1 )$-linear forms property with variables$x , h _ { 1 } , \ldots , h _ { k - 1 }$ and forms

$$
x + \omega \cdot h, \quad \omega \in \{0, 1 \} ^ {k - 1}.
$$

$q = 1$. Use the$( 2 ^ { k - 2 } ( k + 1 ) , 2 k - 2 , k )$-linear forms property with variables$x ,$ $h _ { 1 } , \ldots , h _ { k - 1 } , y _ { 1 } , \ldots , y _ { k - 2 }$and forms

$$
\begin{array}{c} \phi_ {i} (y + \omega h),   \omega \in \{0, 1 \} ^ {k - 1},    \omega_ {i} = 0, 1 \leqslant i \leqslant k - 1; \\ x + \omega \cdot h,   \omega \in \{0, 1 \} ^ {k - 1}. \end{array}
$$

$q = 2$. Use the$( k \cdot 2 ^ { k - 1 } , 3 k - 4 , k )$-linear forms property with variables$x ,$ $h _ { 1 } , \ldots , h _ { k - 1 } , y _ { 1 } , \ldots , y _ { k - 2 } , y _ { 1 } ^ { \prime } , \ldots , y _ { k - 2 } ^ { \prime }$and forms

$$
\begin{array}{c} \phi_ {i} (y + \omega h),   \omega \in \{0, 1 \} ^ {k - 1},    \omega_ {i} = 0, 1 \leqslant i \leqslant k - 1; \\ \phi_ {i} (y ^ {\prime} + \omega h),   \omega \in \{0, 1 \} ^ {k - 1},    \omega_ {i} = 0, 1 \leqslant i \leqslant k - 1; \\ x + \omega \cdot h,   \omega \in \{0, 1 \} ^ {k - 1}. \end{array}
$$

Here of course we adopt the convention that$y _ { k - 1 } = x - y _ { 1 } - . . . - y _ { k - 2 }$and $y _ { k - 1 } ^ { \prime } = x - y _ { 1 } ^ { \prime } - . . . - y _ { k - 2 } ^ { \prime }$. This completes the proof of the lemma, and hence of Proposition$5 . 3$□

## 6. Gowers anti-uniformity

Having studied the$U ^ { k - 1 }$norm, we now introduce the dual$( U ^ { k - 1 } ) ^ { * }$norm, defined in the usual manner as

$$
\left\| g \right\| _ {\left(U ^ {k - 1}\right) ^ {*}} := \sup \left\{\left| \langle f, g \rangle \right|: f \in U ^ {k - 1} \left(\mathbb {Z} _ {N}\right), \| f \| _ {U ^ {k - 1}} \leqslant 1 \right\}.\tag{6.1}
$$

We say that$g$is Gowers anti-uniform if$\| g \| _ { ( U ^ { k - 1 } ) ^ { * } } = O ( 1 )$and$\| g \| _ { L ^ { \infty } } = O ( 1 )$ If$g$is Gowers anti-uniform, and if$| \langle f , g \rangle |$is large, then$f$cannot be Gowers uniform (have small Gowers norm) since

$$
| \langle f, g \rangle | \leqslant \| f \| _ {U ^ {k - 1}} \| g \| _ {(U ^ {k - 1}) ^ {*}}.
$$

Thus Gowers anti-uniform functions can be thought of as “obstructions to Gowers uniformity”. The$( U ^ { k - 1 } ) ^ { * }$are well-defined norms for$k \geqslant 3$since$U ^ { k - 1 }$ is then a genuine norm (not just a seminorm). In this section we show how to generate a large class of Gowers anti-uniform functions, in order that we can decompose an arbitrary function f into a Gowers uniform part and a bounded Gowers anti-uniform part in the next section.

Remark. In the$k = 3$case we have the explicit formula

$$
\| g \| _ {(U ^ {2}) ^ {*}} = \big (\sum_ {\xi \in \mathbb {Z} _ {N}} | \widehat {g} (\xi) | ^ {4 / 3} \big) ^ {3 / 4} = \| \widehat {g} \| _ {4 / 3}.\tag{6.2}
$$

We will not, however, require this fact except for motivational purposes.

A basic way to generate Gowers anti-uniform functions is the following. For each function$F \in L ^ { 1 } ( \mathbb { Z } _ { N } )$, define the dual function DF of F by

$$
\mathcal {D} F (x) := \mathbb {E} \left(\prod_ {\omega \in \{0, 1 \} ^ {k - 1}: \omega \neq 0 ^ {k - 1}} F (x + \omega \cdot h) \Bigg | h \in \mathbb {Z} _ {N} ^ {k - 1}\right)\tag{6.3}
$$

where$0 ^ { k - 1 }$denotes the element of$\{ 0 , 1 \} ^ { k - 1 }$consisting entirely of zeroes.

Remark. Such functions have arisen recently in work of Host and Kra [28] in the ergodic theory setting (see also [1]).

The next lemma, while simple, is fundamental to our entire approach; it asserts that if a function majorised by a pseudorandom measure ν is not Gowers uniform, then it correlates<sup>13</sup> with a bounded Gowers anti-uniform function. Boundedness is the key feature here. The idea in proving Theorem 3.5 will then be to project out the influence of these bounded Gowers anti-uniform functions (through the machinery of conditional expectation) until one is only left with a Gowers uniform remainder, which can be discarded by the generalised von Neumann theorem (Proposition 5.3).

Lemma 6.1 (Lack of Gowers uniformity implies correlation). Let ν be a k-pseudorandom measure, and let$F \in L ^ { 1 } ( \mathbb { Z } _ { N } )$be any function. Then there exist the identities

$$
\langle F, \mathcal {D} F \rangle = \| F \| _ {U ^ {k - 1}} ^ {2 ^ {k - 1}}\tag{6.4}
$$

and

$$
\left\| \mathcal {D} F \right\| _ {(U ^ {k - 1}) ^ {*}} = \left\| F \right\| _ {U ^ {k - 1}} ^ {2 ^ {k - 1} - 1}.\tag{6.5}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>13</sup>This idea was inspired by the proof of the Furstenberg structure theorem [10], [13]; a key point in that proof being that if a system is not (relatively) weakly mixing, then it must contain a nontrivial (relatively) almost periodic function, which can then be projected out via conditional expectation. A similar idea also occurs in the proof of the Szemer´edi regularity lemma [38].</span></small>

If furthermore we assume the bounds

$$
| F (x) | \leqslant \nu (x) + 1 f o r a l l x \in \mathbb {Z} _ {N},
$$

then we have the estimate

$$
\| \mathcal {D} F \| _ {L ^ {\infty}} \leqslant 2 ^ {2 ^ {k - 1} - 1} + o (1).\tag{6.6}
$$

Proof. The identity (6.4) is clear just by expanding both sides using (6.3), (5.4). To prove (6.5) we may of course assume$F$is not identically zero. By (6.1) and (6.4) it sufices to show that

$$
| \langle f, \mathcal {D} F \rangle | \leqslant \| f \| _ {U ^ {k - 1}} \| F \| _ {U ^ {k - 1}} ^ {2 ^ {k - 1} - 1}
$$

for arbitrary functions$f .$But by (6.3) the left-hand side is simply the Gowers inner product$\langle ( f _ { \omega } ) _ { \omega \in \{ 0 , 1 \} ^ { k - 1 } } \rangle _ { U ^ { k - 1 } }$, where$f _ { \omega } : = f$when$\omega = 0$and$f _ { \omega } : = F$ otherwise. The claim then follows from the Gowers Cauchy-Schwarz inequality (5.5).

Finally, we observe that (6.6) is a consequence of the linear forms condition. Bounding$F$by$2 ( \nu + 1 ) / 2 = 2 \nu _ { 1 / 2 }$, it sufices to show that

$$
\mathcal {D} \nu_ {1 / 2} (x) \leqslant 1 + o (1)
$$

uniformly in the choice of$x \in \mathbb { Z } _ { N }$. The left-hand side can be expanded using (6.3) as

$$
\mathbb {E} \bigg (\prod_ {\omega \in \{0, 1 \} ^ {k - 1}: \omega \neq 0 ^ {k - 1}} \nu_ {1 / 2} (x + \omega \cdot h)   \bigg |   h \in \mathbb {Z} _ {N} ^ {k - 1} \bigg).
$$

By the linear forms condition (3.1) (and Lemma 3.4) this expression is$1 + o ( 1 )$ (this is the only place in the paper that we appeal to the linear forms condition in the nonhomogeneous case where some$b _ { i } \neq 0 .$; here, all the$b _ { i }$are equal to x). Note that (3.3) corresponds to the$k = 3$case of this application of the linear forms condition.□

Remarks. Observe that if$P : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$is any polynomial on$\mathbb { Z } _ { N }$of degree at most$k - 2$, and$F ( x ) = e ^ { 2 \pi i P ( x ) / N }$, then$\mathcal { D } { \cal F } = { \cal F } ; { } ^ { 1 4 }$this is basically a reflection of the fact that taking$k - 1$successive diferences of P yields the zero function. Hence by the above lemma$\| F \| _ { ( U ^ { k - 1 } ) ^ { * } } \leqslant 1$, and thus$F$ is Gowers anti-uniform. One should keep these “polynomially quasiperiodic” functions$e ^ { 2 \pi i P ( x ) / N }$in mind as model examples of functions of the form$\mathcal { D } \boldsymbol { F }$ while bearing in mind that they are not the only examples<sup>15</sup>. For some further discussion on the role of such polynomials of degree$k - 2$in determining Gowers uniformity especially in the$k = 4$case, see [18], [19]. Very roughly speaking, Gowers uniform functions are analogous to the notion of “weakly mixing” functions that appear in ergodic theory proofs of Szemer´edi’s theorem, whereas Gowers anti-uniform functions are somewhat analogous to the notion of “almost periodic” functions. When$k = 3$there is a more precise relation with linear exponentials (which are the same thing as characters on$\mathbb { Z } _ { N } )$. When $\nu = 1$, for example, one has the explicit formula

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>14</sup>To make this assertion precise, one has to generalise the notion of dual function to complex-valued functions by inserting an alternating sequence of conjugation signs; see [19].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>15</sup>The situation again has an intriguing parallel with ergodic theory, in which the rˆole of the Gowers anti-uniform functions of order k − 2 appears to be played by k − 2-step nilfactorsk−2 (see [28], [29], [44]), which may contain polynomial eigenfunctions of order but cank − 2, also exhibit slightly more general behaviour; see [14] for further discussion.</span></small>

$$
\mathcal {D} F (x) = \sum_ {\xi \in \mathbb {Z} _ {N}} | \widehat {F} (\xi) | ^ {2} \widehat {F} (\xi) e ^ {2 \pi i x \xi / N}.\tag{6.7}
$$

Suppose for the sake of argument that$F$is bounded pointwise in magnitude by 1. By splitting the set of frequencies$\mathbb { Z } _ { N }$into the sets$S : = \{ \xi : | \widehat { F } ( \xi ) | \geqslant \epsilon \}$ and$\mathbb { Z } _ { N } \backslash S$one sees that it is possible to write

$$
\mathcal {D} F (x) = \sum_ {\xi \in S} a _ {\xi} e ^ {2 \pi i x \xi / N} + E (x),
$$

where$| a _ { \xi } | \leqslant 1$and$\| E \| _ { L ^ { \infty } } \leqslant \epsilon$. Also, we have$| S | \leqslant \epsilon ^ { - 2 }$. Thus$\mathcal { D } \boldsymbol { F }$is equal to a linear combination of a few characters plus a small error.

Once again, these remarks concerning the relation with harmonic analysis are included only for motivational purposes.

Let us refer to a function of the form$\mathcal { D } \boldsymbol { F }$, where F is pointwise bounded $\nu + 1$, as a basic Gowers anti-uniform function. Observe from (6.6) that if N is suficiently large, then all basic Gowers anti-uniform functions take values in the interval$I : = [ - 2 ^ { 2 ^ { k - 1 } } , 2 ^ { 2 ^ { k - 1 } } ]$

The following is a statement to the efect that the measure ν is uniformly distributed with respect not just to each basic Gowers anti-uniform function (which is a special case of (6.5)), but also to the algebra generated by such functions.

Proposition 6.2 (Uniform distribution with respect to basic Gowers anti-uniform functions). Suppose that ν is k-pseudorandom. Let$K \geqslant 1$be a fixed integer, let$\Phi : I ^ { K }  \mathbb { R }$be a fixed continuous function, let$\mathcal { D } { \cal F } _ { 1 } , \ldots , \mathcal { D } { \cal F } _ { K }$ be basic Gowers anti-uniform functions, and define the function$\psi : \mathbb { Z } _ { N } \to \mathbb { R }$ by

$$
\psi (x) := \Phi (\mathcal {D} F _ {1} (x), \dots , \mathcal {D} F _ {K} (x)).
$$

Then we have the estimate

$$
\langle \nu - 1, \psi \rangle = o _ {K, \Phi} (1).
$$

Furthermore if Φ ranges over a compact set$E \subset C ^ { 0 } ( I ^ { K } )$of the space$C ^ { 0 } ( I ^ { K } )$ of continuous functions on$I ^ { K }$(in the uniform topology) then the bounds here are uniform in Φ (i.e. one can replace${ o _ { K , \Phi } ( 1 ) }$with${ o } _ { K , E } ( 1 )$in this case).

Remark. In light of the previous remarks, we see in particular that$\nu$is uniformly distributed with respect to any continuous function of polynomial phase functions such as$e ^ { 2 \pi i P ( x ) / N }$, where P has degree at most$k - 2$

Proof. We will prove this result in two stages, first establishing the result for$\Phi$polynomial and then using a Weierstrass approximation argument to deduce the general case. Fix$K \geqslant 1$, and let$F _ { 1 } , \dots , F _ { K } \in L ^ { 1 } ( \mathbb { Z } _ { N } )$be fixed functions obeying the bounds

$$
F _ {j} (x) \leqslant \nu (x) + 1 \text {   for   all   } x \in \mathbb {Z} _ {N}, 1 \leqslant j \leqslant K.
$$

By replacing$\nu$by$( \nu + 1 ) / 2$, dividing the$F _ { j }$by two, and using Lemma 3.4 as before, we may strengthen this bound without loss of generality to

$$
\left| F _ {j} (x) \right| \leqslant \nu (x) \text {   for   all   } x \in \mathbb {Z} _ {N}, 1 \leqslant j \leqslant K.\tag{6.8}
$$

Lemma 6.3. Let$d \geqslant 1$. For any polynomial P of K variables and degree d with real coeficients (independent$o f N )$

$$
\left\| P \left(\mathcal {D} F _ {1}, \dots , \mathcal {D} F _ {K}\right) \right\| _ {\left(U ^ {k - 1}\right) ^ {*}} = O _ {K, d, P} (1).
$$

Remark. It may seem surprising that that there is no size restriction on $K$or$d ,$since we are presumably going to use the linear forms or correlation conditions and we are only assuming those conditions with bounded parameters. However while we do indeed restrict the size of m in (3.6), we do not need to restrict the size of$q$in (3.5).

Proof. By linearity it sufices to prove this when$P$is a monomial. By enlarging K to at most$d K$and repeating the functions$F _ { j }$as necessary, we see that it in fact sufices to prove this for the monomial$P ( x _ { 1 } , \dots , x _ { K } ) = x _ { 1 } \dots x _ { K }$ Recalling the definition of$( U ^ { k - 1 } ) ^ { * }$, we are thus required to show that

$$
\left\langle f, \prod_ {j = 1} ^ {K} \mathcal {D} F _ {j} \right\rangle = O _ {K} (1)
$$

for all$f : \mathbb { Z } _ { N } \to \mathbb { R }$satisfying$\| f \| _ { U ^ { k - 1 } } \leqslant 1$. By (6.3) the left-hand side can be expanded as

$$
\mathbb {E} \bigg (f (x) \prod_ {j = 1} ^ {K} \mathbb {E} \big (\prod_ {\omega \in \{0, 1 \} ^ {k - 1}: \omega \neq 0 ^ {k - 1}} F _ {j} (x + \omega \cdot h ^ {(j)}) \mid h ^ {(j)} \in \mathbb {Z} _ {N} ^ {k - 1} \big)   \bigg |   x \in \mathbb {Z} _ {N} \bigg).
$$

We can make the change of variables$h ^ { ( j ) } = h + H ^ { ( j ) }$for any$h \in \mathbb { Z } _ { N } ^ { k - 1 }$, and then average over$h ,$to rewrite this as

$$
\mathbb {E} \left(f (x) \prod_ {j = 1} ^ {K} \mathbb {E} \left(\prod_ {\omega \in \{0, 1 \} ^ {k - 1}: \omega \neq 0 ^ {k - 1}} F _ {j} (x + \omega \cdot H ^ {(j)} + \omega \cdot h) \right. \right.
$$

$$
\left| H ^ {(j)} \in \mathbb {Z} _ {N} ^ {k - 1}\right) \Bigg | x \in \mathbb {Z} _ {N}; h \in \mathbb {Z} _ {N} ^ {k - 1} \Bigg).
$$

Expanding the$j$product and interchanging the expectations, we can rewrite this in terms of the Gowers inner product as

$$
\mathbb {E} \left(\langle (f _ {\omega , H}) _ {\omega \in \{0, 1 \} ^ {k - 1}} \rangle_ {U ^ {k - 1}} \mid H \in (\mathbb {Z} _ {N} ^ {k - 1}) ^ {K}\right)
$$

where$H : = ( H ^ { ( 1 ) } , \ldots , H ^ { ( K ) } ) , f _ { 0 , H } : = f ,$and$f _ { \omega , H } : = g _ { \omega \cdot H }$for$\omega \neq 0 ^ { k - 1 }$, where $\omega \cdot H : = ( \omega \cdot H ^ { ( 1 ) } , \dots , \omega \cdot H ^ { ( K ) } )$and

$$
g _ {u ^ {(1)}, \dots , u ^ {(K)}} (x) := \prod_ {j = 1} ^ {K} F _ {j} (x + u ^ {(j)}) \text {   for   all   } u ^ {(1)}, \dots , u ^ {(K)} \in \mathbb {Z} _ {N}.\tag{6.9}
$$

By the Gowers-Cauchy-Schwarz inequality (5.5) we can bound this as

$$
\mathbb {E} \bigg (\| f \| _ {U ^ {k - 1}} \prod_ {\omega \in \{0, 1 \} ^ {k - 1}: \omega \neq 0 ^ {k - 1}} \| g _ {\omega \cdot H} \| _ {U ^ {k - 1}}   \bigg |   H \in (\mathbb {Z} _ {N} ^ {k - 1}) ^ {K} \bigg).
$$

So to prove the claim it will sufice to show that

$$
\mathbb {E} \bigg (\prod_ {\omega \in \{0, 1 \} ^ {k - 1}: \omega \neq 0 ^ {k - 1}} \| g _ {\omega \cdot H} \| _ {U ^ {k - 1}}   \bigg |   H \in (\mathbb {Z} _ {N} ^ {k - 1}) ^ {K} \bigg) = O _ {K} (1).
$$

By H¨older’s inequality it will sufice to show that

$$
\mathbb {E} \big (\| g _ {\omega \cdot H} \| _ {U ^ {k - 1}} ^ {2 ^ {k - 1} - 1} \mid H \in (\mathbb {Z} _ {N} ^ {k - 1}) ^ {K} \big) = O _ {K} (1)
$$

for each$\omega \in \{ 0 , 1 \} ^ { k - 1 } \backslash 0 ^ { k - 1 }$

Fix ω. Since$2 ^ { k - 1 } - 1 \leqslant 2 ^ { k - 1 }$, another application of H¨older’s inequality shows that it in fact sufices to show that

$$
\mathbb {E} \big (\| g _ {\omega \cdot H} \| _ {U ^ {k - 1}} ^ {2 ^ {k - 1}} \mid H \in (\mathbb {Z} _ {N} ^ {k - 1}) ^ {K} \big) = O _ {K} (1).
$$

Since$\omega \neq 0 ^ { k - 1 }$, the map$H \mapsto \omega \cdot H$is a uniform covering of$\mathbb { Z } _ { N } ^ { K }$by$( \mathbb { Z } _ { N } ^ { k - 1 } ) ^ { K }$ Thus by (4.1) we can rewrite the left-hand side as

$$
\mathbb {E} \left(\left\| g _ {u ^ {(1)}, \dots , u ^ {(K)}} \right\| _ {U ^ {k - 1}} ^ {2 ^ {k - 1}} \mid u ^ {(1)}, \dots , u ^ {(K)} \in \mathbb {Z} _ {N}\right).
$$

Expanding this out using (5.4) and (6.9), we can rewrite the left-hand side as

$$
\mathbb {E} \bigg (\prod_ {\tilde {\omega} \in \{0, 1 \} ^ {k - 1}} \prod_ {j = 1} ^ {K} F _ {j} (x + u ^ {(j)} + h \cdot \tilde {\omega})   \bigg |   x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}, u ^ {(1)}, \ldots , u ^ {(K)} \in \mathbb {Z} _ {N} \bigg).
$$

This factorises as

$$
\mathbb {E} \left(\prod_ {j = 1} ^ {K} \mathbb {E} \left(\prod_ {\tilde {\omega} \in \{0, 1 \} ^ {k - 1}} F _ {j} (x + u ^ {(j)} + h \cdot \tilde {\omega}) \mid u ^ {(j)} \in \mathbb {Z} _ {N}\right) \Bigg | x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right).
$$

Applying (6.8), we reduce this to show that

$$
\mathbb {E} \left(\mathbb {E} \left(\prod_ {\tilde {\omega} \in \{0, 1 \} ^ {k - 1}} \nu (x + u + h \cdot \tilde {\omega}) \mid u \in \mathbb {Z} _ {N}\right) ^ {K} \mid x \in \mathbb {Z} _ {N}, h \in \mathbb {Z} _ {N} ^ {k - 1}\right) = O _ {K} (1).
$$

We can make the change of variables$y : = x + u$, and then discard the redundant x averaging, to reduce to showing that

$$
\mathbb {E} \left(\mathbb {E} \big (\prod_ {\tilde {\omega} \in \{0, 1 \} ^ {k - 1}} \nu (y + h \cdot \tilde {\omega}) \mid y \in \mathbb {Z} _ {N} \big) ^ {K} \Big | h \in \mathbb {Z} _ {N} ^ {k - 1}\right) = O _ {K} (1).
$$

Now we are ready to apply the correlation condition (Definition 3.2). This${ \mathrm { i s } } ,$ in fact, the only time we will use that condition. It gives

$$
\mathbb {E} \left(\prod_ {\tilde {\omega} \in \{0, 1 \} ^ {k - 1}} \nu (y + h \cdot \tilde {\omega}) \mid y \in \mathbb {Z} _ {N}\right) \leqslant \sum_ {\tilde {\omega}, \tilde {\omega} ^ {\prime} \in \{0, 1 \} ^ {k - 1}: \tilde {\omega} \neq \tilde {\omega} ^ {\prime}} \tau (h \cdot (\tilde {\omega} - \tilde {\omega} ^ {\prime}))
$$

where, recall,$\tau$is a weight function satisfying$\mathbb { E } ( \tau ^ { q } ) = O _ { q } ( 1 )$for all q. Applying the triangle inequality in$L ^ { K } ( \mathbb { Z } _ { N } ^ { k - 1 } )$, it thus sufices to show that

$$
\mathbb {E} \big (\tau (h \cdot (\tilde {\omega} - \tilde {\omega} ^ {\prime})) ^ {K} \mid h \in \mathbb {Z} _ {N} ^ {k - 1} \big) = O _ {K} (1)
$$

for all distinct$\tilde { \omega } , \tilde { \omega } ^ { \prime } \in \{ 0 , 1 \} ^ { k - 1 }$. But the map$h \mapsto h \cdot ( \tilde { \omega } - \tilde { \omega } ^ { \prime } )$is a uniform covering of$\mathbb { Z } _ { N }$by$( \mathbb { Z } _ { N } ) ^ { k - 1 }$, so by (4.1) the left-hand side is just$\mathbb { E } ( \tau ^ { K } )$, which is$O _ { K } ( 1 )$□

Proof of Proposition 6.2. Let Φ, ψ be as in the proposition, and let$\varepsilon > 0$ be arbitrary. From (6.6) we know that the basic Gowers anti-uniform functions $\mathcal { D } { \cal F } _ { 1 } , \ldots , \mathcal { D } { \cal F } _ { K }$take values in the compact interval$I : = [ - 2 ^ { 2 ^ { k - 1 } } , 2 ^ { 2 ^ { k - 1 } } ]$introduced earlier. By the Weierstrass approximation theorem, we can thus find a polynomial$P$(depending only on$K$and ε) such that

$$
\| \Phi (\mathcal {D} F _ {1}, \ldots , \mathcal {D} F _ {K}) - P (\mathcal {D} F _ {1}, \ldots , \mathcal {D} F _ {K}) \| _ {L ^ {\infty}} \leqslant \varepsilon
$$

and thus by (2.4) and by taking absolute values inside the inner product, we have

$$
| \langle \nu - 1, \Phi (\mathcal {D} F _ {1}, \dots , \mathcal {D} F _ {K}) - P (\mathcal {D} F _ {1}, \dots , \mathcal {D} F _ {K}) \rangle | \leqslant (2 + o (1)) \varepsilon .
$$

On the other hand, from Lemma 6.3, Lemma 5.2 and (6.1) we have

$$
\langle \nu - 1, P (\mathcal {D} F _ {1}, \dots , \mathcal {D} F _ {K}) \rangle = o _ {K, \varepsilon} (1)
$$

since P depends on K and$\varepsilon .$. Combining the two estimates we thus see that for N suficiently large (depending on K and$\varepsilon )$

$$
| \langle \nu - 1, \Phi (\mathcal {D} F _ {1}, \dots , \mathcal {D} F _ {K}) \rangle | \leqslant 4 \varepsilon
$$

(for instance). Since$\varepsilon > 0$was arbitrary, the claim follows. It is clear that this argument also gives the uniform bounds when Φ ranges over a compact set (by covering this compact set by finitely many balls of radius ε in the uniform topology).□

Remarks. The philosophy behind Proposition 6.2 and its proof is that $( U ^ { k - 1 } ) ^ { * }$respects, to some degree, the algebra structure of the space of functions on$\mathbb { Z } _ { N }$. However,$\| \cdot \| _ { ( U ^ { k - 1 } ) ^ { * } }$is not itself an algebra norm even in the model case$k = 3$, as can be seen from (6.2) by recalling that$\| g \| _ { ( U ^ { 2 } ) ^ { * } } = \| \widehat { g } \| _ { 4 / 3 }$. Note, however, that$\| g \| _ { ( U ^ { 2 } ) ^ { * } } \leqslant \| g \| _ { A }$, where$\| g \| _ { A } : = \| { \widehat { g } } \| _ { 1 }$is the Wiener norm. From Young’s inequality we see that the Wiener norm is an algebra norm, that is to say$\| g h \| _ { A } \leqslant \| g \| _ { A } \| h \| _ { A }$. Thus while the$( U ^ { 2 } ) ^ { * }$norm is not an algebra norm, it is at least majorised by an algebra norm.

Now (6.7) easily implies that if$0 \leqslant F ( x ) \leqslant \nu _ { \mathrm { c o n s t } } ( x )$then$\| \widehat { \mathcal { D } F } \| _ { 1 } \leqslant 1$, and so in this case we really have identified an algebra norm (the Weiner norm) such that if$\| f \| _ { U ^ { 2 } }$is large then$f$correlates with a bounded function with small algebra norm. The$( U ^ { k - 1 } ) ^ { * }$norms can thus be thought of as combinatorial variants of the Wiener algebra norm which apply to more general values of k than the Fourier case$k = 3$. (See also [40] for a slightly diferent generalization of the Wiener algebra to the case$k > 3 . )$1

For the majorant ν used to majorise the primes, it is quite likely that $\| { \mathcal { D } } F \| _ { A } = O ( 1 )$whenever$0 \leqslant F ( x ) \leqslant \nu ( x )$, which would allow us to use the Wiener algebra$A$in place of$( U ^ { 2 } ) ^ { * }$in the$k = 3$case of the arguments here. To obtain this estimate, however, requires some serious harmonic analysis related to the restriction phenomenon (the paper [23] may be consulted for further information). Such a property does not seem to follow simply from the pseudorandomness of$\nu ,$and generalisation to$U ^ { k - 1 } , k > 3 .$, seems very dificult (it is not even clear what the form of such a generalisation would be).

For these reasons, our proof of Proposition 6.2 does not mention any algebra norms explicitly.

## 7. Generalised Bohr sets and σ-algebras

To use Proposition 6.2, we shall associate a σ-algebra to each basic Gowers anti-uniform function, such that the measurable functions in each such algebra can be approximated by a function of the type considered in Proposition 6.2. We begin by setting our notation for σ-algebras.

Definition 7.1. A σ-algebra B in$\mathbb { Z } _ { N }$is any collection of subsets of$\mathbb { Z } _ { N }$ which contains the empty set$\varnothing$and the full set$\mathbb { Z } _ { N }$, and is closed under complementation, unions and intersections. As$\mathbb { Z } _ { N }$is a finite set, we will not need to distinguish between countable and uncountable unions or intersections. We define the atoms of a σ-algebra to be the minimal nonempty elements of B (with respect to set inclusion); it is clear that the atoms in$\boldsymbol { B }$form a partition of$\mathbb { Z } _ { N }$, and$\boldsymbol { B }$consists precisely of arbitrary unions of its atoms (including the empty union$\varnothing )$. A function$f \in L ^ { q } ( \mathbb { Z } _ { N } )$is said to be measurable with respect to a σ-algebra B if all the level sets$\{ f ^ { - 1 } ( \{ x \} ) : x \in \mathbb { R } \}$of$f$lie in$B ,$or equivalently if$f$is constant on each of the atoms of$\boldsymbol { B }$.

We define$L ^ { q } ( \mathcal { B } ) \subseteq L ^ { q } ( \mathbb { Z } _ { N } )$to be the subspace of$L ^ { q } ( \mathbb { Z } _ { N } )$consisting of B-measurable functions, equipped with the same$L ^ { q }$norm. We can then define the conditional expectation operator$f \mapsto \mathbb { E } ( f | B )$to be the orthogonal projection of$L ^ { 2 } ( \mathbb { Z } _ { N } )$to$L ^ { 2 } ( B )$; this is of course also defined on all the other$L ^ { q } ( \mathbb { Z } _ { N } )$ spaces since they are all the same vector space. An equivalent definition of conditional expectation is

$$
\mathbb {E} (f | \mathcal {B}) (x) := \mathbb {E} (f (y) | y \in \mathcal {B} (x))
$$

for all$x \in \mathbb { Z } _ { N }$, where$B ( x )$is the unique atom in B which contains x. It is clear that conditional expectation is a linear self-adjoint orthogonal projection on$L ^ { 2 } ( \mathbb { Z } _ { N } )$, is a contraction on$L ^ { q } ( \mathbb { Z } _ { N } )$for every$1 \leqslant q \leqslant \infty$, preserves non-negativity, and also preserves constant functions. Also, if$B ^ { \prime }$is a subalgebra of B then$\mathbb { E } ( \mathbb { E } ( f | B ) | B ^ { \prime } ) = \mathbb { E } ( f | B ^ { \prime } )$

If$\boldsymbol { B } _ { 1 } , \dots , \boldsymbol { B } _ { K }$are σ-algebras, we use$\bigvee _ { j = 1 } ^ { K } \mathcal { B } _ { j } = \mathcal { B } _ { 1 } \lor . . . \lor \mathcal { B } _ { K }$to denote the$\sigma { \mathrm { - a l g e b r a } }$generated by these algebras, or in other words the algebra whose atoms are the intersections of atoms in$\boldsymbol { B } _ { 1 } , \dots , \boldsymbol { B } _ { K }$. We adopt the usual convention that when$K = 0$, the join$\vee _ { j = 1 } ^ { K } B _ { j }$is just the trivial σ-algebra$\{ \varnothing , \mathbb { Z } _ { N } \}$

We now construct the basic σ-algebras to be used. We view the basic Gowers anti-uniform functions as generalizations of complex exponentials, and the atoms of the σ-algebras used can be thought of as “generalised Bohr sets”.

Proposition 7.2 (Each function generates a σ-algebra). Let ν be a k-pseudorandom measure, let$0 < \varepsilon < 1$and$0 < \eta < 1 / 2$be parameters, and let$G \in L ^ { \infty } ( \mathbb { Z } _ { N } )$be function taking values in the interval$I : = [ - 2 ^ { 2 ^ { k - 1 } } , 2 ^ { 2 ^ { k - 1 } } ]$ Then there exists a σ-algebra$B _ { \varepsilon , \eta } ( G )$with the following properties:

• (G lies in its own σ-algebra) For any σ-algebra B,

$$
\left\| G - \mathbb {E} (G | \mathcal {B} \vee \mathcal {B} _ {\varepsilon , \eta} (G)) \right\| _ {L ^ {\infty} (\mathbb {Z} _ {N})} \leqslant \varepsilon .\tag{7.1}
$$

• (Bounded complexity)$B _ { \varepsilon , \eta } ( G )$is generated by at most$O ( 1 / \varepsilon )$atoms.

• (Approximation by continuous functions of G) IfA is any atom in$B _ { \varepsilon , \eta } ( G )$ then there exists a continuous function$\Psi _ { A } : I  [ 0 , 1 ]$such that

$$
\left\| \left(\mathbf {1} _ {A} - \Psi_ {A} (G)\right) (\nu + 1) \right\| _ {L ^ {1} \left(\mathbb {Z} _ {N}\right)} = O (\eta).\tag{7.2}
$$

Furthermore,$\Psi _ { A }$lies in a fixed compact set$E = E _ { \varepsilon , \eta }$of$C ^ { 0 } ( I )$(which is independent of F, ν, N, or A).

Proof. Observe from Fubini’s theorem and (2.4) that

$$
\begin{array}{r l} \int_ {0} ^ {1} \sum_ {n \in \mathbb {Z}} \mathbb {E} \big (\mathbf {1} _ {G (x) \in [ \varepsilon (n - \eta + \alpha), \varepsilon (n + \eta + \alpha) ]} (\nu (x) + 1) \mid x \in \mathbb {Z} _ {N} \big) d \alpha \\ & = 2 \eta \mathbb {E} (\nu (x) + 1 | x \in \mathbb {Z} _ {N}) = O (\eta) \end{array}
$$

and hence by the pigeonhole principle there exists$0 \leqslant \alpha \leqslant 1$such that

$$
\sum_ {n \in \mathbb {Z}} \mathbb {E} \bigl (\mathbf {1} _ {G (x) \in [ \varepsilon (n - \eta + \alpha), \varepsilon (n + \eta + \alpha) ]} (\nu (x) + 1) \mid x \in \mathbb {Z} _ {N} \bigr) = O (\eta).\tag{7.3}
$$

We now set$B _ { \varepsilon , \eta } ( G )$to be the σ-algebra whose atoms are the sets$G ^ { - 1 } ( [ \varepsilon ( n + \alpha )$ $\varepsilon ( n + 1 + \alpha ) ) )$for$n \in \mathbb { Z }$. This is well-defined since the intervals$[ \varepsilon ( n + \alpha )$ $\varepsilon ( n + 1 + \alpha ) )$tile the real line.

It is clear that if B is an arbitrary σ-algebra, then on any atom of$B \vee$ $B _ { \varepsilon , \eta } ( G )$, the function G takes values in an interval of diameter$\varepsilon ,$which yields (7.1). Now we verify the approximation by continuous functions property. Let $A : = G ^ { - 1 } ( [ \varepsilon ( n + \alpha ) , \varepsilon ( n + 1 + \alpha ) ) )$be an atom. Since G takes values in$I ,$ we may assume that$n = O ( 1 / \varepsilon )$, since$A$is empty otherwise; note that this already establishes the bounded complexity property. Let$\psi _ { \eta } : \mathbb { R }  [ 0 , 1 ]$be a fixed continuous cutof function which equals 1 on$[ \eta , 1 - \eta ]$and vanishes outside of$[ - \eta , 1 + \eta ]$, and define$\begin{array} { r } { \Psi _ { A } ( x ) : = \psi _ { \eta } ( \frac { x } { \varepsilon } - n - \alpha ) } \end{array}$. Then it is clear that $\Psi _ { A }$ranges over a compact subset$E _ { \varepsilon , \eta }$of$C ^ { 0 } ( I )$(because n and α are bounded). Furthermore from (7.3) it is clear that we have (7.2). The claim follows.

We now specialise to the case when the functions$G$are basic Gowers anti-uniform functions.

Proposition 7.3. Let ν be a k-pseudorandom measure. Let$K \geqslant 1$be any fixed integer and let$\mathcal { D } F _ { 1 } , \ldots , \mathcal { D } F _ { K } \in L ^ { \infty } ( \mathbb { Z } _ { N } )$be basic Gowers anti-uniform functions. Let$0 < \varepsilon < 1$and$0 < \eta < 1 / 2$be parameters, and let$B _ { \varepsilon , \eta } ( \mathcal { D } { F } _ { j } )$ $j = 1 , \ldots , K$, be constructed as in Proposition 7.2. Let$\boldsymbol { B } : = B _ { \varepsilon , \eta } ( \mathcal { D } \boldsymbol { F } _ { 1 } ) \vee . . . \vee$ $B _ { \varepsilon , \eta } ( D F _ { K } )$. Then if$\eta < \eta _ { 0 } ( \epsilon , K )$is suficiently small and$N > N _ { 0 } ( \epsilon , K , \eta )$is suficiently large,

$$
\left\| \mathcal {D} F _ {j} - \mathbb {E} \left(\mathcal {D} F _ {j} | \mathcal {B}\right) \right\| _ {L ^ {\infty} \left(\mathbb {Z} _ {N}\right)} \leqslant \varepsilon \text {   for   all   } 1 \leqslant j \leqslant K.\tag{7.4}
$$

Furthermore there exists a set Ω which lies in B such that

$$
\mathbb {E} ((\nu + 1) \mathbf {1} _ {\Omega}) = O _ {K, \varepsilon} (\eta^ {1 / 2})\tag{7.5}
$$

and such that

$$
\| (1 - \mathbf {1} _ {\Omega}) \mathbb {E} (\nu - 1 | \mathcal {B}) \| _ {L ^ {\infty} (\mathbb {Z} _ {N})} = O _ {K, \varepsilon} (\eta^ {1 / 2}).\tag{7.6}
$$

Remark. We strongly recommend that here and in subsequent arguments the reader pretend that the exceptional set Ω is empty; in practice we shall be able to set η small enough that the contribution of Ω to our calculations will be negligible.

Proof. The claim (7.4) follows immediately from (7.1). Now we prove (7.5) and (7.6). Since each of the$B _ { \varepsilon , \eta } ( \mathcal { D } { F } _ { j } )$is generated by$O ( 1 / \varepsilon )$atoms, we see that B is generated by$O _ { K , \varepsilon } ( 1 )$atoms. Call an atom A of B small if $\mathbb { E } ( ( \nu + 1 ) \mathbf { 1 } _ { A } ) \leqslant \eta ^ { 1 / 2 }$, and let Ω be the union of all the small atoms. Then clearly Ω lies in B and obeys (7.5). To prove the remaining claim (7.6), it sufices to show that

$$
\frac {\mathbb {E} ((\nu - 1) \mathbf {1} _ {A})}{\mathbb {E} (\mathbf {1} _ {A})} = \mathbb {E} (\nu - 1 | A) = o _ {K, \varepsilon , \eta} (1) + O _ {K, \varepsilon} (\eta^ {1 / 2})\tag{7.7}
$$

for all atoms A in B which are not small. However, by definition of “small” we have

$$
\mathbb {E} ((\nu - 1) \mathbf {1} _ {A}) + 2 \mathbb {E} (\mathbf {1} _ {A}) = \mathbb {E} ((\nu + 1) \mathbf {1} _ {A}) \geqslant \eta^ {1 / 2}.
$$

Thus to complete the proof of (7.7) it will sufice (since η is small and N is large) to show that

$$
\mathbb {E} ((\nu - 1) \mathbf {1} _ {A}) = o _ {K, \varepsilon , \eta} (1) + O _ {K, \varepsilon} (\eta).\tag{7.8}
$$

On the other hand, since A is the intersection of K atoms$A _ { 1 } , \ldots , A _ { K }$from $B _ { \varepsilon , \eta } ( { \mathscr D } F _ { 1 } ) , \dots , B _ { \varepsilon , \eta } ( { \mathscr D } F _ { K } )$respectively, we see from Proposition 7.2 and an easy induction argument (involving H¨older’s inequality and the triangle inequality) that we can find a continuous function$\Psi _ { A } : I ^ { K }  [ 0 , 1 ]$such that

$$
\left\| (\nu + 1) \left(\mathbf {1} _ {A} - \Psi_ {A} \left(\mathcal {D} F _ {1}, \dots , \mathcal {D} F _ {K}\right)\right) \right\| _ {L ^ {1} \left(\mathbb {Z} _ {N}\right)} = O _ {K} (\eta).
$$

Thus, in particular

$$
\left\| (\nu - 1) \left(\mathbf {1} _ {A} - \Psi_ {A} \left(\mathcal {D} F _ {1}, \dots , \mathcal {D} F _ {K}\right)\right) \right\| _ {L ^ {1} \left(\mathbb {Z} _ {N}\right)} = O _ {K} (\eta).
$$

Furthermore one can easily ensure that$\Psi _ { A }$lives in a compact set$E _ { \varepsilon , \eta , K }$of $C ^ { 0 } ( I ^ { K } )$. From this and Proposition 6.2 we have

$$
\mathbb {E} ((\nu - 1) \Psi_ {A} (\mathcal {D} F _ {1}, \ldots , \mathcal {D} F _ {K})) = o _ {K, \varepsilon , \eta} (1)
$$

since N is assumed large depending on$K , \varepsilon , \eta _ { ; }$and the claim (7.8) now follows from the triangle inequality.□

Remarks. This σ-algebra B is closely related to the (relatively) compact σ-algebras studied in the ergodic theory proof of Szemer´edi’s theorem, see for instance [10], [13]. In the case$k = 3$they are closely connected to the Kronecker factor of an ergodic system, and for higher k they are related to (k − 2)-step nilsystems; see e.g. [28], [44].

## 8. A Furstenberg tower, and the proof of Theorem 3.5

We now have enough machinery to deduce Theorem 3.5 from Proposition 2.3. The key proposition is the following decomposition, which splits an arbitrary function into Gowers uniform and Gowers anti-uniform components (plus a negligible error).

Proposition 8.1 Generalised Koopman-von Neumann structure theorem). Let ν be a k-pseudorandom measure, and let$f \in L ^ { 1 } ( \mathbb { Z } _ { N } )$be a non-negative function satisfying$0 \leqslant f ( x ) \leqslant \nu ( x )$for all$x \in \mathbb { Z } _ { N }$. Let$0 < \varepsilon \ll 1$ be a small parameter, and assume$N > N _ { 0 } ( \varepsilon )$is suficiently large. Then there exists a σ-algebra B and an exceptional set$\Omega \in B$such that

• (smallness condition)

$$
\mathbb {E} (\nu \mathbf {1} _ {\Omega}) = o _ {\varepsilon} (1);\tag{8.1}
$$

• (ν is uniformly distributed outside$o f \Omega )$

$$
\| (1 - \mathbf {1} _ {\Omega}) \mathbb {E} (\nu - 1 | \mathcal {B}) \| _ {L ^ {\infty}} = o _ {\varepsilon} (1)\tag{8.2}
$$

and

• (Gowers uniformity estimate)

$$
\left\| \left(1 - \mathbf {1} _ {\Omega}\right) (f - \mathbb {E} (f | \mathcal {B})) \right\| _ {U ^ {k - 1}} \leqslant \varepsilon^ {1 / 2 ^ {k}}.\tag{8.3}
$$

Remarks. As in the previous section, the exceptional set Ω should be ignored on a first reading. The ordinary Koopman-von Neumann theory in ergodic theory asserts, among other things, that any function$f$on a measurepreserving system$( X , B , T , \mu )$can be orthogonally decomposed into a “weakly mixing part”$f - \mathbb { E } ( f | B )$(in which$f - \mathbb { E } ( f | B )$is asymptotically orthogonal to its shifts$T ^ { n } ( f - \mathbb { E } ( f | B ) )$on the average) and an “almost periodic part”$\mathbb { E } ( f | B )$ (whose shifts form a precompact set); here B is the Kronecker factor, i.e. the σ-algebra generated by the almost periodic functions (or equivalently, by the eigenfunctions of T). This is somewhat related to the$k = 3$case of the above proposition, hence our labeling of that proposition as a generalised Koopmanvon Neumann theorem. A slightly more quantitative analogy for the$k = 3$ case would be the assertion that any function bounded by a pseudorandom measure can be decomposed into a Gowers uniform component with small Fourier coeficients, and a Gowers anti-uniform component which consists of only a few Fourier coeficients (and in particular is bounded). For related ideas see [5], [21], [23].

Proof of Theorem 3.5 assuming Proposition 8.1. Let f, δ be as in Theorem 3.5, and let$0 < \varepsilon \ll \delta$be a parameter to be chosen later. Let B be as in the above decomposition, and write$f _ { U } : = ( 1 - \mathbf { 1 } _ { \Omega } ) ( f - \mathbb { E } ( f | B ) )$and $f _ { U ^ { \perp } } : = ( 1 - \mathbf { 1 } _ { \Omega } ) \mathbb { E } ( f | B )$(the subscript U stands for Gowers uniform, and$U ^ { \perp }$ for Gowers anti-uniform). Observe from (8.1), (3.7), (3.8) and the measurability of Ω that

$$
\mathbb {E} (f _ {U ^ {\perp}}) = \mathbb {E} ((1 - \mathbf {1} _ {\Omega}) f) \geqslant \mathbb {E} (f) - \mathbb {E} (\nu \mathbf {1} _ {\Omega}) \geqslant \delta - o _ {\varepsilon} (1).
$$

Also, by (8.2) we see that$f _ { U ^ { \bot } }$is bounded above by$1 + o _ { \varepsilon } ( 1 )$. Since$f$is nonnegative,$f _ { U ^ { \bot } }$is also. We may thus<sup>16</sup> apply Proposition 2.3 to obtain

$$
\begin{array}{c} \mathbb {E} \big (f _ {U ^ {\perp}} (x) f _ {U ^ {\perp}} (x + r) \ldots f _ {U ^ {\perp}} (x + (k - 1) r) \mid x, r \in \mathbb {Z} _ {N} \big) \\ \geqslant c (k, \delta) - o _ {\varepsilon} (1) - o _ {k, \delta} (1). \end{array}
$$

On the other hand, from (8.3) we have$\| f _ { U } \| _ { U ^ { k - 1 } } \leqslant \varepsilon ^ { 1 / 2 ^ { k } }$; since$( 1 - { \bf 1 } _ { \Omega } ) f$is bounded by ν and$f _ { U ^ { \bot } }$is bounded by$1 + o _ { \varepsilon } ( 1 )$, we thus see that$f _ { U }$is pointwise bounded by$\nu + 1 + o _ { \varepsilon } ( 1 )$. Applying the generalised von Neumann theorem (Proposition 5.3) we thus see that

$$
\mathbb {E} \big (f _ {0} (x) f _ {1} (x + r) \dots f _ {k - 1} (x + (k - 1) r) \mid x, r \in \mathbb {Z} _ {N} \big) = O (\varepsilon^ {1 / 2 ^ {k}}) + o _ {\varepsilon} (1)
$$

whenever each$f _ { j }$is equal to$f _ { U }$or$f _ { U ^ { \bot } }$, with at least one$f _ { j }$equal to$f _ { U }$. Adding these two estimates together we obtain

$$
\begin{array}{c} \mathbb {E} (\tilde {f} (x) \tilde {f} (x + r) \ldots \tilde {f} (x + (k - 1) r) | x, r \in \mathbb {Z} _ {N}) \\ \geqslant c (k, \delta) - O (\varepsilon^ {1 / 2 ^ {k}}) - o _ {\varepsilon} (1) - o _ {k, \delta} (1), \end{array}
$$

where$\tilde { f } : = f _ { U } + f _ { U ^ { \perp } } = ( 1 - { \bf 1 } _ { \Omega } ) f$. But since$0 \leqslant ( 1 - \mathbf { 1 } _ { \Omega } ) f \leqslant f$we obtain

$$
\mathbb {E} (f (x) f (x + r) \dots f (x + (k - 1) r) | x, r \in \mathbb {Z} _ {N}) \geqslant c (k, \delta) - O (\varepsilon^ {1 / 2 ^ {k}}) - o _ {\varepsilon} (1) - o _ {k, \delta} (1).
$$

Since$\varepsilon$can be made arbitrarily small (as long as N is taken suficiently large), the error terms on the right-hand side can be taken to be arbitrarily small by choosing N suficiently large depending on k and δ. The claim follows.□

To complete the proof of Theorem 3.5, it sufices to prove Proposition 8.1. To construct the σ-algebra B required in the proposition, we will use the philosophy laid out by Furstenberg in his ergodic structure theorem (see [10], [13]), which decomposes any measure-preserving system into a weakly-mixing extension of a tower of compact extensions. In our setting, the idea is roughly speaking as follows. We initialise B to be the trivial σ-algebra${ \cal B } = \{ \emptyset , \mathbb { Z } _ { N } \}$ If the function$f - \mathbb { E } ( f | B )$is already Gowers uniform (in the sense of (8.3)), then we can terminate the algorithm. Otherwise, we use the machinery of dual functions, developed in$\ S 6 ,$, to locate a Gowers anti-uniform function$\mathcal { D } F _ { 1 }$which has some nontrivial correlation with$f ,$and add the level sets of$\mathcal { D } \boldsymbol { F } _ { 1 }$to the σ-algebra$B ;$the nontrivial correlation property will ensure that the$L ^ { 2 }$norm of$\mathbb { E } ( f | B )$increases by a nontrivial amount during this procedure, while the pseudorandomness of$\nu$will ensure that$\mathbb { E } ( f | B )$remains uniformly bounded. We then repeat the above algorithm until$f - \mathbb { E } ( f | B )$becomes suficiently

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 + o<sub>ε</sub>(1),</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>16</sup>There is an utterly trivial issue which we have ignored here, which is that f is notU⊥ bounded above by 1 but by and that the density is bounded below byδ − o<sub>ε</sub>(1) rather than δ. One can easily get around this by modifying by  before applying<sup>f</sup><sub>U⊥</sub>o<sub>ε</sub>(1) Proposition 2.3, incurring a net error of  at the end since f is bounded.o<sub>ε</sub>(1)U⊥</span></small>

Gowers uniform, at which point we terminate the algorithm. In the original ergodic theory arguments of Furstenberg this algorithm was not guaranteed to terminate, and indeed one required the axiom of choice (in the guise of Zorn’s lemma) in order to conclude<sup>17</sup> the structure theorem. However, in our setting we can terminate in a bounded number of steps (in fact in at most$2 ^ { 2 ^ { k } } / \varepsilon + 2$ steps), because there is a quantitative$L ^ { 2 } \mathrm { . }$increment to the bounded function E(f|B) at each stage.

Such a strategy will be familiar to any reader acquainted with the proof of Szemer´edi’s regularity lemma [39]. This is no coincidence: there is in fact a close connection between regularity lemmas such as those in [20], [22], [39] and ergodic theory of the type we have brushed up against in this paper. Indeed there are strong analogies between all of the known proofs of Szemer´edi’s theorem, despite the fact that they superficially appear to use very diferent techniques.

We turn to the details. To prove Proposition 8.1, we will iterate the following somewhat technical proposition, which can be thought of as a$\sigma -$ algebra variant of Lemma 6.1.

Proposition 8.2 (Iterative step). Let ν be a k-pseudorandom measure, and let$f \in L ^ { 1 } ( \mathbb { Z } _ { N } )$be a nonnegative function satisfying$0 \leqslant f ( x ) \leqslant \nu ( x ) \ f o r$ all$x \in \mathbb { Z } _ { N }$. Let$0 < \eta \ll \varepsilon \ll 1$1 be small numbers, and let$K \geqslant 0$be an integer. Suppose that$\eta < \eta _ { 0 } ( \varepsilon , K )$is suficiently small and that$N > N _ { 0 } ( \varepsilon , K , \eta )$is suficiently large. Let$F _ { 1 } , \dots , F _ { K } \in L ^ { 1 } ( \mathbb { Z } _ { N } )$be a collection of functions obeying the pointwise bounds

$$
\left| F _ {j} (x) \right| \leqslant \left(1 + O _ {K, \varepsilon} \left(\eta^ {1 / 2}\right)\right) (\nu (x) + 1)\tag{8.4}
$$

for all$1 \leqslant j \leqslant K$and$x \in \mathbb { Z } _ { N }$. Let$\boldsymbol { B } _ { K }$be the σ-algebra

$$
\mathcal {B} _ {K} := \mathcal {B} _ {\varepsilon , \eta} (\mathcal {D} F _ {1}) \vee \dots \vee \mathcal {B} _ {\varepsilon , \eta} (\mathcal {D} F _ {K})\tag{8.5}
$$

where$B _ { \varepsilon , \eta } ( \mathcal { D } { F } _ { j } )$is as in Proposition 7.2, and suppose that there exists a set $\Omega _ { K }$in$\mathbb { Z } _ { N }$obeying

• (smallness bound)

(8.6)

$$
\mathbb {E} ((\nu + 1) \mathbf {1} _ {\Omega_ {K}}) = O _ {K, \varepsilon} (\eta^ {1 / 2})
$$

and

• (uniform distribution bound)

$$
\| (1 - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (\nu - 1 | \mathcal {B} _ {K}) \| _ {L ^ {\infty} (\mathbb {Z} _ {N})} = O _ {K, \varepsilon} (\eta^ {1 / 2}).\tag{8.7}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">k,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">k,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>17</sup>For the specific purpose of k-term recurrence, i.e. finding progressions of length k, one only needs to run Furstenberg’s algorithm for a finite number of steps depending on  and so Zorn’s lemma is not needed in this application. We thank Bryna Kra for pointing out this subtlety.</span></small>

Set

$$
F _ {K + 1} := (1 - \mathbf {1} _ {\Omega_ {K}}) (f - \mathbb {E} (f | \mathcal {B} _ {K}))\tag{8.8}
$$

and suppose that$F _ { K + 1 }$obeys the non-Gowers-uniformity estimate

$$
\left\| F _ {K + 1} \right\| _ {U ^ {k - 1}} > \varepsilon^ {1 / 2 ^ {k}}.\tag{8.9}
$$

Then there exist the estimates

$$
\| (1 - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (f | \mathcal {B} _ {K}) \| _ {L ^ {\infty} (\mathbb {Z} _ {N})} \leqslant 1 + O _ {K, \varepsilon} (\eta^ {1 / 2}),\tag{8.10}
$$

(E$( f \vert B _ { K } )$is bounded outside$\Omega _ { K } )$and

$$
\left| F _ {K + 1} (x) \right| \leqslant \left(1 + O _ {K, \varepsilon} \left(\eta^ {1 / 2}\right)\right) (\nu (x) + 1).\tag{8.11}
$$

Furthermore, if$B _ { K + 1 }$is the σ-algebra

$$
\mathcal {B} _ {K + 1} := \mathcal {B} _ {K} \vee \mathcal {B} _ {\varepsilon , \eta} (\mathcal {D} F _ {K + 1}) = \mathcal {B} _ {\varepsilon , \eta} (\mathcal {D} F _ {1}) \vee \dots \vee \mathcal {B} _ {\varepsilon , \eta} (\mathcal {D} F _ {K + 1})\tag{8.12}
$$

then there exists a set$\Omega _ { K + 1 } \supseteq \Omega _ { K }$obeying

• (smallness bound)

$$
\mathbb {E} ((\nu + 1) \mathbf {1} _ {\Omega_ {K + 1}}) = O _ {K, \varepsilon} (\eta^ {1 / 2});\tag{8.13}
$$

• (uniform distribution bound)

$$
\| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (\nu - 1 | \mathcal {B} _ {K + 1}) \| _ {L ^ {\infty} (\mathbb {Z} _ {N})} = O _ {K, \varepsilon} (\eta^ {1 / 2});\tag{8.14}
$$

such that

• (energy increment property)

$$
\| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (f | \mathcal {B} _ {K + 1}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} \geqslant \| (1 - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (f | \mathcal {B} _ {K}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} + 2 ^ {- 2 ^ {k} + 1} \varepsilon .\tag{8.15}
$$

Remark. If we ignore the exceptional sets$\Omega _ { K } , \Omega _ { K + 1 }$, this proposition asserts the following: if$f$is not “relatively weakly mixing” with respect to the σ-algebra$\boldsymbol { B } _ { K }$, in the sense that the component$f - \mathbb { E } ( f | B _ { K } )$of f which is orthogonal to$\boldsymbol { B } _ { K }$is not Gowers-uniform, then we can refine$\boldsymbol { B } _ { K }$to a slightly more complex σ-algebra$B _ { K + 1 }$such that the$L ^ { 2 } ( \mathbb { Z } _ { N } )$norm (energy) of$\mathbb { E } ( f | B _ { K + 1 } )$is larger than$E ( f | B _ { K } )$by some quantitative amount. Furthermore, ν remains uniformly distributed with respect to$B _ { K + 1 }$

Proof of Proposition 8.1 assuming Proposition 8.2. Fix ε, and let$K _ { 0 }$be the smallest integer greater than$2 ^ { 2 ^ { k } } / \varepsilon + 1$; this quantity will be the upper bound for the number of iterations of an algorithm which we shall give shortly. We need a parameter$0 < \eta \ll \varepsilon$to be chosen later (we assume$\eta < \eta _ { 0 } ( \varepsilon , K _ { 0 } )$; we assume$N > N _ { 0 } ( \eta , \varepsilon )$is suficiently large).

To construct B and Ω we shall, for some$K \in [ 0 , K _ { 0 } ]$, iteratively construct a sequence of basic Gowers anti-uniform functions$\mathcal { D } \boldsymbol { F } _ { 1 } , \ldots , \mathcal { D } \boldsymbol { F } _ { K }$on$\mathbb { Z } _ { N }$together with exceptional sets$\Omega _ { 0 } \subseteq \Omega _ { 1 } \subseteq . . . \subseteq \Omega _ { K } \subseteq \mathbb { Z } _ { N }$in the following manner.

• Step 0. Initialise$K = 0$and$\Omega _ { 0 } : = \varnothing$. (We will later increment the value of K.)

• Step 1. Let$\boldsymbol { B } _ { K }$and$F _ { K + 1 }$be defined by (8.5) and (8.8) respectively. Thus for instance when$K = 0$we will have$\boldsymbol { \mathcal { B } } _ { 0 } = \{ \boldsymbol { \emptyset } , \mathbb { Z } _ { N } \}$and$F _ { 1 } = f - \mathbb { E } ( f )$ Observe that in the$K = 0$case, the estimates (8.4), (8.6), (8.7) are trivial (the latter bound following from (2.4)). As we shall see, these three estimates will be preserved throughout the algorithm.

• Step 2. If the estimate (8.9) fails, or in other words

$$
\| F _ {K + 1} \| _ {U ^ {k - 1}} \leqslant \varepsilon^ {1 / 2 ^ {k}},
$$

then we set$\Omega : = \Omega _ { K }$and$\boldsymbol { B } : = \boldsymbol { B } _ { K }$, and successfully terminate the algorithm.

• Step 3. If instead (8.9) holds, then we define$B _ { K + 1 }$by (8.12). (Here we of course need$K \leqslant K _ { 0 }$, but this will be guaranteed by Step 4 below.) We then invoke Proposition 8.2 to locate an exceptional set$\Omega _ { K + 1 } \supset \Omega _ { K }$ in$B _ { K + 1 }$obeying the conditions<sup>18</sup> (8.13), (8.14) for which we have the energy increment property (8.15). Also, we have (8.11).

• Step 4. Increment K to$K + 1 ;$observe from construction that the estimates (8.4), (8.6), (8.7) will be preserved when doing so. If we now have$K > K _ { 0 }$, then we terminate the algorithm with an error; otherwise, return to Step 1.

Remarks. The integer K indexes the iteration number of the algorithm; thus we begin with the zeroth iteration when$K = 0 ,$, then the first iteration when$K = 1$, etc. It is worth noting that apart from${ \cal O } _ { K , \varepsilon } ( \eta ^ { 1 / 2 } )$error terms, none of the bounds we will encounter while executing this algorithm will actually depend on K. As we shall see, this algorithm will terminate well before K reaches$K _ { 0 }$(in fact, for the application to the primes, the Hardy-Littlewood prime tuples conjecture implies that this algorithm will terminate at the first step$K = 0 )$.

Assuming Proposition 8.2, we see that this algorithm will terminate after finitely many steps with one of two outcomes: either it will terminate successfully in Step 2 for some$K \leqslant K _ { 0 } .$, or else it will terminate with an error in Step 4 when K exceeds$K _ { 0 }$. Assume for the moment that the former case occurs. Then it is clear that at the successful conclusion of this algorithm, we will have generated a σ-algebra$\boldsymbol { B }$and an exceptional set Ω with the properties required for Proposition 8.1, with error terms of${ \cal O } _ { K , \varepsilon } ( \eta ^ { 1 / 2 } )$instead of$o _ { \varepsilon } ( 1 )$ if$N > N _ { 0 } ( \eta , K , \varepsilon )$. But by making η decay suficiently slowly to zero, we can replace the${ \cal O } _ { K , \varepsilon } ( \eta ^ { 1 / 2 } )$bounds by$o _ { \varepsilon } ( 1 )$; note that the dependence of the error terms on K will not be relevant since K is bounded by$K _ { 0 }$, which depends only on ε.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">00</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">K,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>18</sup>Of course, the constants in the O() bounds are diferent at each stage of this iteration, but we are allowing these constants to depend on and K will ultimately be bounded by K<sub>0</sub>, which depends only on ε and k.</span></small>

To conclude the proof of Proposition 8.1 it will thus sufice to show that the above algorithm does not terminate with an error. Suppose for a contradiction that the algorithm ran until the$K _ { 0 } ^ { \mathrm { t h } }$iteration before terminating with an error in Step 4. Then if we define the energies$E _ { K }$for$0 \leqslant K \leqslant K _ { 0 } + 1$by the formula

$$
E _ {K} := \left\| \left(1 - \mathbf {1} _ {\Omega_ {K}}\right) \mathbb {E} (f | \mathcal {B} _ {K}) \right\| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2},
$$

we see from (8.15) that

$$
E _ {K + 1} \geqslant E _ {K} + 2 ^ {- 2 ^ {k} + 1} \varepsilon \text { for   all } 0 \leqslant K \leqslant K _ {0}\tag{8.16}
$$

(for instance). Also, by (8.10),

$$
0 \leqslant E _ {K} \leqslant 1 + O _ {K, \varepsilon} (\eta^ {1 / 2}) \text { for   all } 0 \leqslant K \leqslant K _ {0}.
$$

If$\eta < \eta _ { 0 } ( K , \varepsilon )$is suficiently small, these last two statements contradict one another for$K = K _ { 0 }$. Thus the above algorithm cannot reach the$K _ { 0 } ^ { \mathrm { t h } }$iteration, and instead terminates successfully at Step 2. This completes the proof of Proposition 8.1.□

The only remaining task is to prove Proposition 8.2.

Proof of Proposition 8.2. Let$\nu , f , K , \varepsilon , \eta , F _ { 1 } , \ldots , F _ { K } , F _ { K + 1 } , \mathcal { B } _ { K } , \Omega _ { K }$ $B _ { K + 1 }$be as in the proposition. We begin by proving the bounds (8.10), (8.11). From (8.7) we have

$$
\| (1 - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (\nu | \mathcal {B} _ {K}) \| _ {L ^ {\infty}} \leqslant 1 + O _ {K, \varepsilon} (\eta^ {1 / 2});
$$

since$f$is nonnegative and bounded pointwise by$\nu ,$we obtain (8.10). The bound (8.11) then follows from (8.10) and (8.8), where we again use that $f$is nonnegative and bounded pointwise by$\nu .$This shows in particular that $\mathcal { D } \boldsymbol { F } _ { 1 } , \ldots , \mathcal { D } \boldsymbol { F } _ { K _ { 1 } + 1 }$are basic Gowers anti-uniform functions (up to multiplicative errors of$1 + O _ { K _ { 1 } , \varepsilon } ( \eta ^ { 1 / 2 } )$, which are negligible).

Applying Lemma 6.1 (scaling out the multiplicative error of$1 + O _ { K , \varepsilon } ( \eta ^ { 1 / 2 } ) )$1 and using (8.4) and (8.11) we conclude that

$$
\left\| \mathcal {D} F _ {j} \right\| _ {L ^ {\infty} \left(\mathbb {Z} _ {N}\right)} \leqslant 2 ^ {2 ^ {k - 1} - 1} + O _ {K, \varepsilon} \left(\eta^ {1 / 2}\right) \text {   for   all   } 0 \leqslant j \leqslant K + 1,\tag{8.17}
$$

since we are assuming N to be large depending on$K , \varepsilon , \eta$

We now apply Proposition 7.3 (absorbing the multiplicative errors of$1 +$ ${ \cal O } _ { K , \varepsilon } ( \eta ^ { 1 / 2 } ) )$to conclude that we may find a set Ω in$B _ { K + 1 }$such that

$$
\mathbb {E} ((\nu + 1) \mathbf {1} _ {\Omega}) = O _ {K, \varepsilon} (\eta^ {1 / 2})
$$

and

$$
\| (1 - \mathbf {1} _ {\Omega}) \mathbb {E} (\nu - 1 | \mathcal {B} _ {K + 1}) \| _ {L ^ {\infty}} = O _ {K, \varepsilon} (\eta^ {1 / 2}).
$$

If we then set$\Omega _ { K + 1 } : = \Omega _ { K } \cup \Omega$, we can verify (8.13) and (8.14) from (8.6) and (8.7).

It remains to verify (8.15), the energy increment property, that is to say the statement

$$
\| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (f | \mathcal {B} _ {K + 1}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} \geqslant \| (1 - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (f | \mathcal {B} _ {K}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} + 2 ^ {- 2 ^ {k} + 1} \varepsilon .\tag{8.18}
$$

To do this we exploit the hypothesis$\| F _ { K + 1 } \| _ { U ^ { k - 1 } } > \varepsilon ^ { 1 / 2 ^ { k } }$, which was (8.9). By Lemma 6.1 and the definition (8.8),

$$
\left| \left\langle \left(1 - \mathbf {1} _ {\Omega_ {K}}\right) \left(f - \mathbb {E} \left(f | \mathcal {B} _ {K}\right)\right), \mathcal {D} F _ {K + 1} \right\rangle \right| = \left| \left\langle F _ {K + 1}, \mathcal {D} F _ {K + 1} \right\rangle \right| = \| F _ {K + 1} \| _ {U ^ {k - 1}} ^ {2 ^ {k - 1}} \geqslant \varepsilon^ {1 / 2}.
$$

On the other hand, from the bounds (8.4), (8.6) and (8.17) we have

$$
\begin{array}{l} \big | \left\langle (\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) (f - \mathbb {E} (f | \mathcal {B} _ {K})), \mathcal {D} F _ {K + 1} \right\rangle \big | \\ \qquad \leqslant \| \mathcal {D} F _ {K + 1} \| _ {\infty} \mathbb {E} \big ((\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) | f - \mathbb {E} (f | \mathcal {B} _ {K}) | \big) \\ \qquad = O _ {K, \varepsilon} (1) \mathbb {E} \big ((\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) (\nu + 1) \big) = O _ {K, \varepsilon} (\eta^ {1 / 2}), \end{array}
$$

while from (7.1) and (8.10) we have

$$
\begin{array}{l} \big | \left\langle (1 - \mathbf {1} _ {\Omega_ {K + 1}}) (f - \mathbb {E} (f | \mathcal {B} _ {K})), \mathcal {D} F _ {K + 1} - \mathbb {E} (\mathcal {D} F _ {K + 1} | \mathcal {B} _ {K + 1}) \right\rangle \big | \\ \leqslant \| \mathcal {D} F _ {K + 1} - \mathbb {E} (\mathcal {D} F _ {K + 1} | \mathcal {B} _ {K + 1}) \| _ {\infty} \mathbb {E} \big ((1 - \mathbf {1} _ {\Omega_ {K + 1}}) | f - \mathbb {E} (f | \mathcal {B} _ {K}) | \big) \\ \leqslant O (\varepsilon) \mathbb {E} \big ((1 - \mathbf {1} _ {\Omega_ {K + 1}}) (\nu + 1) \big) = O (\epsilon). \end{array}
$$

By the triangle inequality we thus have

$$
\left| \left\langle (1 - \mathbf {1} _ {\Omega_ {K + 1}}) (f - \mathbb {E} (f | \mathcal {B} _ {K})), \mathbb {E} (\mathcal {D} F _ {K + 1} | \mathcal {B} _ {K + 1}) \right\rangle \right| \geqslant \varepsilon^ {1 / 2} - O _ {K, \varepsilon} (\eta^ {1 / 2}) - O (\varepsilon).
$$

But since$( 1 - \mathbf { 1 } _ { \Omega _ { K + 1 } } ) , \mathbb { E } ( \mathcal { D } F _ { K + 1 } | \mathcal { B } _ { K + 1 } )$, and$\mathbb { E } ( f \vert B _ { K } )$are all measurable in $B _ { K + 1 }$, we can replace f by$\mathbb { E } ( f | B _ { K + 1 } )$, and so

$$
\begin{array}{c} | \left\langle (1 - \mathbf {1} _ {\Omega_ {K + 1}}) (\mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K})), \mathbb {E} (\mathcal {D} F _ {K + 1} | \mathcal {B} _ {K + 1}) \right\rangle | \\ \geqslant \varepsilon^ {1 / 2} - O _ {K, \varepsilon} (\eta^ {1 / 2}) - O (\varepsilon). \end{array}
$$

By the Cauchy-Schwarz inequality and (8.17) we obtain

$$
\begin{array}{c} \| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) (\mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K})) \| _ {L ^ {2} (\mathbb {Z} _ {N})} \\ \geqslant 2 ^ {- 2 ^ {k - 1} + 1} \varepsilon^ {1 / 2} - O _ {K, \varepsilon} (\eta^ {1 / 2}) - O (\varepsilon). \end{array}\tag{8.19}
$$

Strictly speaking, this implies (8.15) thanks to Pythagoras’s theorem, but the presence of the exceptional sets$\Omega _ { K }$and$\Omega _ { K + 1 }$means that we have to exercise caution, especially since we have no$L ^ { 2 }$control on$\nu .$

Recalling that$\mathbb { E } ( f | \mathcal { B } _ { K } ) \le 1 + O _ { \varepsilon , K } ( \eta ^ { 1 / 2 } )$outside$\Omega _ { K }$(cf. (8.10)), we observe that if$\eta < \eta _ { 0 } ( \varepsilon , K )$is suficiently small then

$$
\begin{array}{c} \| (\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (f | \mathcal {B} _ {K}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} \leqslant 2 \| \mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}} \| _ {2} ^ {2} \\ \leqslant 2 \| \mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}} \| _ {1} \leqslant 2 \mathbb {E} \mathbf {1} _ {\Omega_ {K + 1}}, \end{array}
$$

which, by (8.6), is${ \cal O } _ { K , \varepsilon } ( \eta ^ { 1 / 2 } )$. By the triangle inequality (and (8.10)) we thus see that to prove (8.15) it will sufice to prove

$$
\begin{array}{l} \| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (f | \mathcal {B} _ {K + 1}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} \\ \qquad \geqslant \| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (f | \mathcal {B} _ {K}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} + 2 ^ {- 2 ^ {k} + 2} \varepsilon - O _ {K, \varepsilon} (\eta^ {1 / 2}) - O (\varepsilon^ {3 / 2}), \end{array}
$$

since we can absorb the error terms$- O _ { K , \varepsilon } ( \eta ^ { 1 / 2 } ) { - } O ( \varepsilon ^ { 3 / 2 } )$into the$2 ^ { - 2 ^ { k } + 2 } \varepsilon$term by choosing ε suficiently small depending on$k ,$, and η suficiently small depending on$K , \varepsilon .$

We write the left-hand side as

$$
\left\| \left(1 - \mathbf {1} _ {\Omega_ {K + 1}}\right) \mathbb {E} (f | \mathcal {B} _ {K}) + \left(1 - \mathbf {1} _ {\Omega_ {K + 1}}\right) (\mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K}) \right\| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2}
$$

which can be expanded using the cosine rule as

$$
\begin{array}{r l} & {\| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (f | \mathcal {B} _ {K}) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2} + \| (1 - \mathbf {1} _ {\Omega_ {K + 1}}) (\mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K})) \| _ {L ^ {2} (\mathbb {Z} _ {N})} ^ {2}} \\ & {\qquad + 2 \left\langle (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (f | \mathcal {B} _ {K}), (1 - \mathbf {1} _ {\Omega_ {K + 1}}) (\mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K})) \right\rangle .} \end{array}
$$

Therefore by (8.19) it will sufice to show the approximate orthogonality relationship

$$
\left\langle (1 - \mathbf {1} _ {\Omega_ {K + 1}}) \mathbb {E} (f | \mathcal {B} _ {K}), (1 - \mathbf {1} _ {\Omega_ {K + 1}}) (\mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K})) \right\rangle = O _ {K, \varepsilon} (\eta^ {1 / 2}).
$$

Since$( 1 - \mathbf { 1 } _ { \Omega _ { K + 1 } } ) ^ { 2 } = ( 1 - \mathbf { 1 } _ { \Omega _ { K + 1 } } )$, this can be rewritten as

$$
\left\langle \left(1 - \mathbf {1} _ {\Omega_ {K + 1}}\right) \mathbb {E} (f | \mathcal {B} _ {K}), \mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K}) \right\rangle .
$$

Now note that$( 1 - \mathbf { 1 } _ { \Omega _ { K } } ) \mathbb { E } ( f | B _ { K } )$is measurable with respect to$\boldsymbol { B } _ { K }$, and hence orthogonal to$\mathbb { E } ( f | B _ { K + 1 } ) - \mathbb { E } ( f | B _ { K } )$, since$\boldsymbol { B } _ { K }$is a sub-σ-algebra of$B _ { K + 1 }$ Thus the above expression can be rewritten as

$$
\left\langle (\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (f | \mathcal {B} _ {K}), \mathbb {E} (f | \mathcal {B} _ {K + 1}) - \mathbb {E} (f | \mathcal {B} _ {K}) \right\rangle .
$$

Again, since the left-hand side is measurable with respect to$B _ { K + 1 }$, we can rewrite this as

$$
\langle (\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) \mathbb {E} (f | \mathcal {B} _ {K}), f - \mathbb {E} (f | \mathcal {B} _ {K}) \rangle .
$$

Since$\mathbb { E } ( f | \mathcal { B } _ { K } ) ( x ) \leqslant 2 \mathrm { ~ i f ~ } \eta < \eta _ { 0 } ( \varepsilon , K )$is suficiently small and$x \notin \Omega _ { K }$(cf. (8.10)), we may majorise this by

$$
2 \mathbb {E} \big ((\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) | f - \mathbb {E} (f | \mathcal {B} _ {K}) | \big).
$$

Since we are working with the assumption that$0 \leqslant f ( x ) \leqslant \nu ( x )$, we can bound this in turn by

$$
2 \mathbb {E} \left(\left(\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}\right) (\nu + \mathbb {E} (\nu | \mathcal {B} _ {K}))\right).
$$

Since$\mathbb { E } ( \nu | B _ { K } ) ( x ) \leqslant 2$for$x \notin \Omega _ { K }$(cf. (8.7)) this is no more than

$$
4 \mathbb {E} \big ((\mathbf {1} _ {\Omega_ {K + 1}} - \mathbf {1} _ {\Omega_ {K}}) (\nu + 1) \big),
$$

which is${ \cal O } _ { K , \varepsilon } ( \eta ^ { 1 / 2 } )$as desired by (8.6). This concludes the proof of Proposition 8.2, and hence Theorem 3.5.□

## 9. A pseudorandom measure which majorises the primes

Having concluded the proof of Theorem 3.5, we are now ready to apply it to the specific situation of locating arithmetic progressions in the primes. As in almost any additive problem involving the primes, we begin by considering the von Mangoldt function Λ defined by$\Lambda ( n ) = \log p$if$n = p ^ { m }$and 0 otherwise. Actually, for us the higher prime powers$p ^ { 2 } , p ^ { 3 } , \ldots$. will play no role whatsoever and will be discarded very shortly.

From the prime number theorem we know that the average value of$\Lambda ( n )$ is$1 + o ( 1 )$. In order to prove Theorem 1.1 (or Theorem 1.2), it would sufice to exhibit a measure$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$, such that$\nu ( n ) \geqslant c ( k ) \Lambda ( n )$for some$c ( k ) > 0$ which depends only on k, and which is k-pseudorandom. Unfortunately, such a measure cannot exist because the primes (and the von Mangoldt function) are concentrated on certain residue classes. Specifically, for any integer $q > 1$, Λ is only nonzero on those$\phi ( q )$residue classes$a ( { \bmod { q } } )$for which$( a , q )$ = 1, whereas a pseudorandom measure can easily be shown to be uniformly distributed across all q residue classes; here of course$\phi ( q )$is the Euler totient function. Since$\phi ( q ) / q$can be made arbitrarily small, we therefore cannot hope to obtain a pseudorandom majorant with the desired property$\nu ( n ) \geqslant c ( k ) \Lambda ( n )$

To get around this dificulty we employ a device which we call the Wtrick,<sup>19</sup> which efectively removes the arithmetic obstructions to pseudorandomness arising from the very small primes. Let$w = w ( N )$be any function tending slowly<sup>20</sup> to infinity with N, so that$1 / w ( N ) = o ( 1 )$, and let $\begin{array} { r } { W = \prod _ { p \leqslant w ( N ) } p } \end{array}$be the product of the primes up to$w ( N )$. Define the modified von Mangoldt function$\tilde { \Lambda } : \mathbb { Z } ^ { + } \to \mathbb { R } ^ { + }$by

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>19</sup>The reader will observe some similarity between this trick and the use of σ-algebras in the previous section to remove non-Gowers-uniformity from the system. Here, of course, the precise obstruction to non-Gowers-uniformity in the primes is very explicit, whereas the exact structure of the σ-algebras constructed in the previous section are somewhat mysterious. In the specific case of the primes, we expect (through such conjectures as the Hardy-Littlewood prime tuple conjecture) that the primes are essentially uniform once the obstructions from small primes are removed, and hence the algorithm of the previous section should in fact terminate immediately at the K = 0 iteration. However we emphasise that our argumentK = 0 does not give (or require) any progress on this very dificult prime tuple conjecture, as we allow K to be nonzero.</span></small>

$$
\widetilde {\Lambda} (n) := \left\{ \begin{array}{l l} \frac {\phi (W)}{W} \log (W n + 1) & \text {when Wn + 1 is prime} \\ 0 & \text {otherwise.} \end{array} \right.
$$

Note that we have discarded the contribution of the prime powers since we ultimately wish to count arithmetic progressions in the primes themselves. This W-trick exploits the trivial observation that in order to obtain arithmetic progressions in the primes, it sufices to do so in the modified primes$\{ n \in \mathbb { Z }$: $W n + 1$is prime} (at the cost of reducing the number of such progressions by a polynomial factor in$W$at worst). We also remark that one could replace $W n + 1$here by$W n + b$for any integer$1 \leqslant b < W$coprime to W without afecting the arguments which follow.

Observe that if$w ( N )$is suficiently slowly growing$( w ( N ) \ll \log \log N$ will sufice here) then by Dirichlet’s theorem concerning the distribution of the primes in arithmetic progressions<sup>21</sup> such as$\{ n : n \equiv 1 ( { \bmod { W } } ) \}$we have $\begin{array} { r } { \sum _ { n \leqslant N } \widetilde \Lambda ( n ) = N ( 1 + o ( 1 ) ) } \end{array}$. With this modification, we can now majorise the primes by a pseudorandom measure as follows:

Proposition 9.1. Write$\epsilon _ { k } : = 1 / 2 ^ { k } ( k + 4 ) !$, and let N be a suficiently large prime number. Then there is a k-pseudorandom measure$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$ such that$\nu ( n ) \geqslant k ^ { - 1 } 2 ^ { - k - 5 } \widetilde { \Lambda } ( n )$for all$\epsilon _ { k } N \leqslant n \leqslant 2 \epsilon _ { k } N$

Remark. The purpose of$\epsilon _ { k }$is to assist in dealing with wraparound issues, which arise from the fact that we are working on$\mathbb { Z } _ { N }$and not on$[ - N , N ]$ Standard sieve theory techniques (in particular the “fundamental lemma of sieve theory”) can come very close to providing such a majorant, but the error terms on the pseudorandomness are not of the form$o ( 1 )$but rather something like$O ( 2 ^ { - 2 ^ { C k } } )$or so. This unfortunately does not quite seem to be good enough for our argument, which crucially relies on$o ( 1 )$type decay, and so we have to rely instead on recent arguments of Goldston and Yıldırım.

Proof of Theorem 1.1 assuming Proposition 9.1. Let N be a large prime number. Define the function$f \in L ^ { 1 } ( \mathbb { Z } _ { N } )$by setting$f ( n ) : = k ^ { - 1 } 2 ^ { - k - 5 } \tilde { \Lambda } ( n )$ for$\epsilon _ { k } N \leqslant n \leqslant 2 \epsilon _ { k } N$and$f ( n ) = 0$otherwise. From Dirichlet’s theorem we

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>20</sup>Actually, it will be clear at the end of the proof that we can in fact take w to be a suficiently large number independent of depending only on k. However it will bek. convenient for now to make w slowly growing in N in order to take advantage of theo(1) notation.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∑N≤n≤2N Λ(n) > N</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>21In</sup> <sup>fact,</sup> <sup>all</sup> <sup>we</sup> <sup>need</sup> <sup>is</sup> <sup>that</sup> N-n-2N <sup>Λ(</sup>  <sup>n)</sup> <sup></sup> <sup>N.</sup> <sup>Thus</sup> <sup>one</sup> <sup>could</sup> <sup>avoid</sup> <sup>appealing</sup> <sup>to</sup> the theory of Dirichlet L-functions by replacing n ≡ 1(mod W) by n ≡ b(mod W), for somen ≡ 1n ≡ b(mod W) b coprime to W chosen using the pigeonhole principle.</span></small>

observe that

$$
\mathbb {E} (f) = \frac {k ^ {- 1} 2 ^ {- k - 5}}{N} \sum_ {\epsilon_ {k} N \leqslant n \leqslant 2 \epsilon_ {k} N} \tilde {\Lambda} (n) = k ^ {- 1} 2 ^ {- k - 5} \epsilon_ {k} (1 + o (1)).
$$

We now apply Proposition 9.1 and Theorem 3.5 to conclude that

$$
\mathbb {E} \big (f (x) f (x + r) \dots f (x + (k - 1) r) \mid x, r \in \mathbb {Z} _ {N} \big) \geqslant c (k, k ^ {- 1} 2 ^ {- k - 5} \epsilon_ {k}) - o (1).
$$

Observe that the degenerate case$r = 0$can only contribute at most$\begin{array} { r } { O ( \frac { 1 } { N } \log ^ { k } N ) } \end{array}$ $= o ( 1 )$to the left-hand side and can thus be discarded. Furthermore, every progression counted by the expression on the left is not just a progression in $\mathbb { Z } _ { N }$, but a genuine arithmetic progression of integers since$\epsilon _ { k } < 1 / k$. Since the right-hand side is positive (and bounded away from zero) for suficiently large $N$, the claim follows from the definition of$f$and$\tilde { \Lambda } .$.□

Thus to obtain arbitrarily long arithmetic progressions in the primes, it will sufice to prove Proposition 9.1. This will be the purpose of the remainder of this section (with certain number-theoretic computations being deferred to §10 and the appendix).

To obtain a majorant for$\tilde { \Lambda } ( n )$, we begin with the well-known formula

$$
\Lambda (n) = \sum_ {d | n} \mu (d) \log (n / d) = \sum_ {d | n} \mu (d) \log (n / d) _ {+}
$$

for the von Mangoldt function, where$\mu$is the M¨obius function, and$\log ( x ) _ { + }$ denotes the positive part of the logarithm, that is to say, max$( \log ( x ) , 0 )$. Here and in the sequel$d$is always understood to be a positive integer. Motivated by this, we define

Definition 9.2 (Goldston–Yıldırım truncated divisor sum). Let R be a parameter (in applications it will be a small power of$N )$. Define

$$
\Lambda_{R}(n):= \sum_{\substack{d|n\\ d\leqslant R}}\mu (d)\log (R / d) = \sum_{d|n}\mu (d)\log (R / d)_{+}.
$$

These truncated divisor sums have been studied in several papers, most notably the works of Goldston and Yıldırım [15], [16], [17] concerning the problem of finding small gaps between primes. We shall use a modification of their arguments for obtaining asymptotics for these truncated primes to prove that the measure ν defined below is pseudorandom.

Definition 9.3. Let$R : = N ^ { k ^ { - 1 } 2 ^ { - k - 4 } }$, and let$\epsilon _ { k } : = 1 / 2 ^ { k } ( k + 4 ) !$. We define the function$\nu : \mathbb { Z } _ { N } \to \mathbb { R } ^ { + }$by

$$
\nu (n) := \left\{ \begin{array}{l l} \frac {\phi (W)}{W} \frac {\Lambda_ {R} (W n + 1) ^ {2}}{\log R} & \text { when } \epsilon_ {k} N \leqslant n \leqslant 2 \epsilon_ {k} N \\ 1 & \text { otherwise } \end{array} \right.
$$

for all$0 \leqslant n < N$, where we identify$\{ 0 , \ldots , N - 1 \}$with$\mathbb { Z } _ { N }$in the usual manner.

This ν will be our majorant for Proposition 9.1. We first verify that it is indeed a majorant.

Lemma 9.4.$\nu ( n ) \geqslant 0$for all$n \ \in \ \mathbb { Z } _ { N } .$, and furthermore,$\nu ( n ) \geqslant$ $k ^ { - 1 } 2 ^ { - k - 5 } \widetilde { \Lambda } ( n )$for all$\epsilon _ { k } N \leqslant n \leqslant 2 \epsilon _ { k } N$(if N is suficiently large depending on k).

Proof. The first claim is trivial. The second claim is also trivial unless $W n + 1$is prime. From the definition of R, we see that$W n + 1 > R$if N is suficiently large. Then the sum over$d | W n + 1 , d \leqslant R$, in (9.2) in fact consists of just the one term$d = 1$. Therefore$\Lambda _ { R } ( W n + 1 )$= log R, which means that $\begin{array} { r } { \nu ( n ) = \frac { \phi ( W ) } { W } \log R \geqslant k ^ { - 1 } 2 ^ { - k - 5 } \widetilde { \Lambda } ( n ) } \end{array}$by construction of R and N (when w(N) is suficiently slowly growing in N).□

We will have to wait a while to show that ν is actually a measure$( \mathrm { i . e . }$. it verifies (2.4)). The next proposition will be crucial in showing that ν has the linear forms property.

Proposition 9.5 (Goldston-Yıldırım). Let$m ,$t be positive integers. For each$1 \leqslant i \leqslant m$, let$\begin{array} { r } { \psi _ { i } ( \mathbf { x } ) : = \sum _ { j = 1 } ^ { t } L _ { i j } x _ { j } + b _ { i } } \end{array}$, be linear forms with integer coeficients$L _ { i j }$such that$| L _ { i j } | \leqslant \sqrt { w ( N ) } / 2$for all$i = 1 , \ldots m$and$j = 1 , \dots , t .$ Assume that the t-tuples$( L _ { i j } ) _ { j = 1 } ^ { t }$are never identically zero, and that no two t-tuples are rational multiples of each other. Write$\theta _ { i } : = W \psi _ { i } + 1$. Suppose that B is a product$\textstyle \prod _ { i = 1 } ^ { t } I _ { i } \subset \mathbb { R } ^ { t }$of t intervals$I _ { i } ,$each of which has length at least$R ^ { 1 0 m }$. Then (if the function w$( N )$is suficiently slowly growing in N)

$$
\mathbb {E} (\Lambda_ {R} (\theta_ {1} (\mathbf {x})) ^ {2} \dots \Lambda_ {R} (\theta_ {m} (\mathbf {x})) ^ {2} | \mathbf {x} \in B) = (1 + o _ {m, t} (1)) \left(\frac {W \log R}{\phi (W)}\right) ^ {m}.
$$

Remarks. We have attributed this proposition to Goldston and Yıldırım, because it is a straightforward generalisation of [17, Prop. 2]. The W-trick makes much of the analysis of the so-called singular series (which is essentially just$( W / \phi ( W ) ) ^ { m }$here) easier in our case, but to compensate we have the slight extra dificulty of dealing with forms in several variables.

To keep this paper as self-contained as possible, we give a proof of Proposition 9.5. In §10 the reader will find a proof which depends on an estimation of a certain contour integral involving the Riemann ζ-function. This is along the lines of [17, Prop. 2] but somewhat diferent in detail. The aforementioned integral is precisely the same as one that Goldston and Yıldırım find an asymptotic for. We recall their argument in the appendix.

Much the same remarks apply to the next proposition, which will be of extreme utility in demonstrating that ν has the correlation property (Definition 3.2).

Proposition 9.6 (Goldston-Yıldırım). Let m - 1 be an integer, and let B be an interval of length at least$R ^ { 1 0 m }$. Suppose that$h _ { 1 } , \ldots , h _ { m }$are distinct integers satisfying$| h _ { i } | \leqslant N ^ { 2 }$for all 1$\leqslant i \leqslant m$, and let$\Delta$denote the integer

$$
\Delta := \prod_ {1 \leqslant i <   j \leqslant m} | h _ {i} - h _ {j} |.
$$

Then (for N suficiently large depending on m, and with the function$w ( N )$ suficiently slowly growing in N)

$$
\begin{array}{l} \mathbb {E} (\Lambda_ {R} (W (x + h _ {1}) + 1) ^ {2} \ldots \Lambda_ {R} (W (x + h _ {m}) + 1) ^ {2} | x \in B) \\ \leqslant (1 + o _ {m} (1)) \left(\frac {W \log R}{\phi (W)}\right) ^ {m} \prod_ {p | \Delta} (1 + O _ {m} (p ^ {- 1 / 2})). \end{array}\tag{9.1}
$$

Here and in the sequel,$p$is always understood to be prime.

Assuming both Proposition 9.5 and Proposition 9.6, we can now conclude the proof of Proposition 9.1. We begin by showing that$\nu$is indeed a measure.

Lemma 9.7. The measure ν constructed in Definition 9.3 obeys the estimate$\mathbb { E } ( \nu ) = 1 + o ( 1 )$

Proof. Apply Proposition 9.5 with$m : = t : = 1 , \psi _ { 1 } ( x _ { 1 } ) : = x _ { 1 }$and$B : =$ $[ \epsilon _ { k } N , 2 \epsilon _ { k } N ]$(taking N suficiently large depending on$k ,$of course). Comparing with Definition 9.3 we thus have

$$
\mathbb {E} (\nu (x) \mid x \in [ \epsilon_ {k} N, 2 \epsilon_ {k} N ]) = 1 + o (1).
$$

But from the same definition we clearly have

$$
\mathbb {E} (\nu (x) \mid x \in \mathbb {Z} _ {N} \backslash [ \epsilon_ {k} N, 2 \epsilon_ {k} N ]) = 1.
$$

Combining these two results confirms the lemma.

Now we verify the linear forms condition, which is proven in a spirit similar to the above lemma.

Proposition 9.8. The function ν satisfies the$( k \cdot 2 ^ { k - 1 } , 3 k - 4 , k )$-linear forms condition.

Proof. Let$\begin{array} { r } { \psi _ { i } ( { \bf x } ) = \sum _ { j = 1 } ^ { t } L _ { i j } x _ { j } + b _ { i } } \end{array}$be linear forms of the type which are featured in Definition 3.1. That is to say, we have$m \leqslant k \cdot 2 ^ { k - 1 } , t \leqslant 3 k - 4 ,$ the$L _ { i j }$are rational numbers with numerator and denominator at most k in absolute value, and none of the t-tuples$( L _ { i j } ) _ { j = 1 } ^ { t }$is zero or is equal to a rational multiple of any other. We wish to show that

$$
\mathbb {E} (\nu (\psi_ {1} (\mathbf {x})) \dots \nu (\psi_ {m} (\mathbf {x})) | \mathbf {x} \in \mathbb {Z} _ {N} ^ {t}) = 1 + o (1).\tag{9.2}
$$

We may clear denominators and assume that all the$L _ { i j }$are integers, at the expense of increasing the bound on$L _ { i j }$to$| L _ { i j } | \leqslant ( k + 1 ) !$. Since$w ( N )$is growing to infinity in N, we may assume that$( k + 1 ) ! < \sqrt { w ( N ) } / 2$by taking N suficiently large. This is required in order to apply Proposition 9.5 as we have stated it.

The two-piece definition of$\nu$in Definition 9.3 means that we cannot apply Proposition 9.5 immediately; the following localization argument is needed.

We chop the range of summation in (9.2) into$Q ^ { t }$almost equal-sized boxes, where$Q = Q ( N )$is a slowly growing function of$N$to be chosen later. Thus let

$$
B _ {u _ {1}, \dots , u _ {t}} = \left\{\mathbf {x} \in \mathbb {Z} _ {N} ^ {t}: x _ {j} \in \left[ \lfloor u _ {j} N / Q \rfloor , \lfloor (u _ {j} + 1) N / Q \rfloor), j = 1, \dots , t \right. \right\},
$$

where the$u _ { j }$are to be considered (mod Q). Observe that up to negligible multiplicative errors of$1 + o ( 1 )$(arising because the boxes do not quite have equal sizes) the left-hand side of (9.2) can be rewritten as

$$
\mathbb {E} \left(\mathbb {E} \left(\nu \left(\psi_ {1} (\mathbf {x})\right) \dots \nu \left(\psi_ {m} (\mathbf {x})\right) \mid \mathbf {x} \in B _ {u _ {1}, \dots , u _ {t}}\right) \mid u _ {1}, \dots , u _ {t} \in \mathbb {Z} _ {Q}\right).
$$

Call a t-tuple$( u _ { 1 } , \ldots , u _ { t } ) \in \mathbb { Z } _ { Q } ^ { t }$nice if for every$1 \leqslant i \leqslant m$, the set$\psi _ { i } ( B _ { u _ { 1 } , \dots , u _ { t } } )$ is either completely contained in the interval$[ \epsilon _ { k } N , 2 \epsilon _ { k } N ]$or is completely disjoint from this interval. From Proposition 9.5 and Definition 9.3 we observe that

$$
\mathbb {E} \left(\nu \left(\psi_ {1} (\mathbf {x})\right) \dots \nu \left(\psi_ {m} (\mathbf {x})\right) \mid \mathbf {x} \in B _ {u _ {1}, \dots , u _ {t}}\right) = 1 + o _ {m, t} (1)
$$

whenever$( u _ { 1 } , \ldots , u _ { t } )$is nice, since we can replace<sup>22</sup> each of the$\nu ( \psi _ { i } ( \mathbf x ) )$factors by either$\frac { \phi ( W ) } { W \log R } \Lambda _ { R } ^ { 2 } ( \theta _ { i } ( { \bf x } ) )$or 1, and$N / Q$will exceed$R ^ { 1 0 m }$for Q suficiently slowly growing in N, by definition of R and the upper bound on$m$. When $( u _ { 1 } , \ldots , u _ { t } )$is not nice, then we can crudely bound ν by$\begin{array} { r } { 1 + \frac { \phi ( W ) } { W \log R } \Lambda _ { R } ^ { 2 } ( \theta _ { i } ( \mathbf { x } ) ) } \end{array}$ multiply out, and apply Proposition 9.5 again to obtain

$$
\mathbb {E} \left(\nu \left(\psi_ {1} (\mathbf {x})\right) \dots \nu \left(\psi_ {m} (\mathbf {x})\right) \mid \mathbf {x} \in B _ {u _ {1}, \dots , u _ {t}}\right) = O _ {m, t} (1) + o _ {m, t} (1).
$$

We shall shortly show that the proportion of nonnice t-tuples$( u _ { 1 } , \ldots , u _ { t } )$in $\mathbb { Z } _ { Q } ^ { t }$is at most$O _ { m , t } ( 1 / Q )$, and thus the left-hand side of (9.2) is$1 + o _ { m , t } ( 1 ) +$ $\dot { O _ { m , t } } ( 1 / Q )$, and the claim follows when$Q$is suficiently slowly growing in$N .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ψ<sub>i</sub>(x)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Z → ZN</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>22</sup>There is a technical issue here due to the failure of the quotient map Z → Z<sub>N</sub> to be a bijection. More specifically, the functions  only take values in the interval[<sub>k</sub>N, 2<sub>k</sub>N] modulo and so strictly speaking one needs to subtract a multiple of N from in theψ<sub>i</sub> formula below. However, because of the relatively small dimensions of the box B<sub>u ,...,u</sub> , the1 t multiple of one needs to subtract is independent of x, and so it can be absorbed into thex, constant term b<sub>i</sub> of the afine-linear form ψ<sub>i</sub> and thus be harmless.</span></small>

It remains to verify the claim about the proportion of nonnice t-tuples. Suppose$( u _ { 1 } , \ldots , u _ { t } )$is not nice. Then there exist$1 \leqslant i \leqslant$m and$\mathbf { x } , \mathbf { x } ^ { \prime } \in$ $B _ { u _ { 1 } , \ldots , u _ { t } }$such that$\psi _ { i } ( \mathbf { x } )$lies in the interval$[ \epsilon _ { k } N , 2 \epsilon _ { k } N ]$, but$\psi _ { i } ( \mathbf { x } ^ { \prime } )$does not. But from the definition of$B _ { u _ { 1 } , \ldots , u _ { t } }$(and the boundedness of the$L _ { i j } )$we have

$$
\psi_ {i} (\mathbf {x}), \psi_ {i} (\mathbf {x} ^ {\prime}) = \sum_ {j = 1} ^ {t} L _ {i j} \lfloor N u _ {j} / Q \rfloor + b _ {i} + O _ {m, t} (N / Q).
$$

Thus we must have

$$
a \epsilon_ {k} N = \sum_ {j = 1} ^ {t} L _ {i j} \lfloor N u _ {j} / Q \rfloor + b _ {i} + O _ {m, t} (N / Q)
$$

for either$a = 1$or$a = 2$. Dividing by$N / Q$, we obtain

$$
\sum_ {j = 1} ^ {t} L _ {i j} u _ {j} = a \epsilon_ {k} Q + b _ {i} Q / N + O _ {m, t} (1) \pmod {Q}.
$$

Since$( L _ { i j } ) _ { j = 1 } ^ { t }$is nonzero, the number of t-tuples$( u _ { 1 } , \ldots , u _ { t } )$which satisfy this equation is at most$O _ { m , t } ( Q ^ { t - 1 } )$. Letting a and i vary we thus see that the proportion of nonnice t-tuples is at most$O _ { m , t } ( 1 / Q )$as desired (the m and t dependence is irrelevant since both are functions of k).□

In a short while we will use Proposition 9.6 to show that ν satisfies the correlation condition (Definition 3.2). Prior to that, however, we must look at the average size of the “arithmetic” factor$\begin{array} { r } { \prod _ { p \vert \Delta } ( 1 + O _ { m } ( p ^ { - 1 / 2 } ) ) } \end{array}$appearing in that proposition.

Lemma 9.9. Let m - 1 be a parameter. There is a weight function$\tau =$ $\tau _ { m } : \mathbb { Z } \to \mathbb { R } ^ { + }$such that$\tau ( n ) \geqslant 1$for all$n \neq 0$, and such that for all distinct $h _ { 1 } , \ldots , h _ { j } \in [ \epsilon _ { k } N , 2 \epsilon _ { k } N ]$2

$$
\prod_ {p \mid \Delta} (1 + O _ {m} (p ^ {- 1 / 2})) \leqslant \sum_ {1 \leqslant i <   j \leqslant m} \tau (h _ {i} - h _ {j}),
$$

where$\Delta$is as defined in Proposition 9.6, and such that$\mathbb { E } ( \tau ^ { q } ( n ) | 0 < | n | \leqslant N )$ $= O _ { m , q } ( 1 )$for all$0 < q < \infty$

Proof. We observe that

$$
\prod_ {p \mid \Delta} (1 + O _ {m} (p ^ {- 1 / 2})) \leqslant \prod_ {1 \leqslant i <   j \leqslant m} \left(\prod_ {p \mid h _ {i} - h _ {j}} (1 + p ^ {- 1 / 2})\right) ^ {O _ {m} (1)}.
$$

By the arithmetic mean-geometric mean inequality (absorbing all constants into the$O _ { m } ( 1 )$factor) we can thus take$\begin{array} { r } { \tau _ { m } ( n ) : = \bar { O } _ { m } ( 1 ) \prod _ { p \mid n } ( \bar { 1 } + p ^ { - 1 / 2 } ) ^ { O _ { m } ( 1 ) } } \end{array}$ for all$n \neq 0$. (The value of$\tau$at 0 is irrelevant for this lemma since we are taking all the$h _ { i }$to be distinct.) To prove the claim, it thus sufices to show that

$$
\mathbb {E} \left(\prod_ {p | n} (1 + p ^ {- 1 / 2}) ^ {O _ {m} (q)} \mid 0 <   | n | \leqslant N\right) = O _ {m, q} (1) \text {   for   all   } 0 <   q <   \infty .
$$

Since$( 1 + p ^ { - 1 / 2 } ) ^ { O _ { m } ( q ) }$is bounded by$1 + p ^ { - 1 / 4 }$for all but$O _ { m , q } ( 1 )$primes$p ,$ we have

$$
\mathbb {E} \left(\prod_ {p | n} (1 + p ^ {- 1 / 2}) ^ {O _ {m} (q)} \mid 0 <   | n | \leqslant N\right) \leqslant O _ {m, q} (1) \mathbb {E} \left(\prod_ {p | n} (1 + p ^ {- 1 / 4}) \mid 0 <   n \leqslant N\right).
$$

But$\textstyle \prod _ { p \mid n } ( 1 + p ^ { - 1 / 4 } ) \leqslant \sum _ { d \mid n } d ^ { - 1 / 4 }$, and hence

$$
\begin{array}{c} \mathbb {E} \bigg (\prod_ {p | n} (1 + p ^ {- 1 / 2}) ^ {O _ {m} (q)}   \bigg |   0 <   | n | \leqslant N \bigg) \leqslant O _ {m, q} (1) \frac {1}{2 N} \sum_ {1 \leqslant | n | \leqslant N} \sum_ {d | n} d ^ {- 1 / 4} \\ \leqslant O _ {m, q} (1) \frac {1}{2 N} \sum_ {d = 1} ^ {N} \frac {N}{d} d ^ {- 1 / 4}, \end{array}
$$

which is$O _ { m , q } ( 1 )$as desired.

□

We are now ready to verify the correlation condition.

Proposition 9.10. The measure ν satisfies the$2 ^ { k - 1 }$-correlation condition.

Proof. Let us begin by recalling what it is we wish to prove. For any $1 \leqslant m \leqslant 2 ^ { k - 1 }$and$h _ { 1 } , \ldots , h _ { m } \in \mathbb { Z } _ { N }$we must show a bound

$$
\mathbb {E} \big (\nu (x + h _ {1}) \nu (x + h _ {2}) \dots \nu (x + h _ {m}) \mid x \in \mathbb {Z} _ {N} \big) \leqslant \sum_ {1 \leqslant i <   j \leqslant m} \tau (h _ {i} - h _ {j}), \tag {9.3}
$$

where the weight function$\tau = \tau _ { m }$is bounded in$L ^ { q }$for all$q .$

Fix m,$h _ { 1 } , \ldots , h _ { m }$. We shall take the weight function constructed in Lemma 9.9 (identifying Z<sub>N</sub> with the integers between$- N / 2$and$+ N / 2 )$, and set

$$
\tau (0) := \exp (C m \log N / \log \log N)
$$

for some large absolute constant$C .$From the previous lemma we see that $\mathbb { E } ( \tau ^ { q } ) = O _ { m , q } ( 1 )$for all$q ,$since the addition of the weight$\tau ( 0 )$at$0$only contributes$o _ { m , q } ( 1 )$at most.

We first dispose of the easy case when at least two of the$h _ { i }$are equal. In this case we bound the left-hand side of (9.2) crudely by$\| \nu \| _ { L ^ { \infty } } ^ { m }$. But from Definitions 9.2, 9.3 and by standard estimates for the maximal order of the divisor function$d ( n )$we have the crude bound$\| \nu \| _ { L ^ { \infty } } \ll \exp ( C \log N / \log \log N )$, and the claim follows thanks to our choice of$\tau ( 0 )$

Suppose then that the$h _ { i }$are distinct. Since, in (9.3), our aim is only to get an upper bound, there is no need to subdivide$\mathbb { Z } _ { N }$into intervals as we did in the proof of Proposition 9.8. Write

$$
g (n) := \frac {\phi (W)}{W} \frac {\Lambda_ {R} ^ {2} (W n + 1)}{\log R} \mathbf {1} _ {[ \epsilon_ {k} N, 2 \epsilon_ {k} N ]} (n).
$$

Then by construction of ν (Definition 9.3), we have

$$
\begin{array}{l} \mathbb {E} \big (\nu (x + h _ {1}) \ldots \nu (x + h _ {m}) \mid x \in \mathbb {Z} _ {N} \big) \\ \qquad \leqslant \mathbb {E} \big ((1 + g (x + h _ {1})) \ldots (1 + g (x + h _ {m})) \mid x \in \mathbb {Z} _ {N} \big). \end{array}
$$

The right-hand side may be rewritten as

$$
\sum_ {A \subseteq \{1, \dots , m \}} \mathbb {E} \left(\prod_ {i \in A} g (x + h _ {i}) \Bigg | x \in \mathbb {Z} _ {N}\right)
$$

(cf. the proof of Lemma 3.4). Observe that for$i , j \in A$we may assume$| h _ { i } - h _ { j } |$ $\leqslant \epsilon _ { k } N$, since the expectation vanishes otherwise. By Proposition 9.6 and Lemma 9.9, we therefore have

$$
\mathbb {E} \bigg (\prod_ {i \in A} g (x + h _ {i})   \Big |   x \in \mathbb {Z} _ {N} \bigg) \leqslant \sum_ {1 \leqslant i <   j \leqslant m} \tau (h _ {i} - h _ {j}) + o _ {m} (1).
$$

Summing over all A, and adjusting the weights$\tau$by a bounded factor (depending only on m and hence on$k )$, we obtain the result.□

Proof of Proposition 9.1. This is immediate from Lemmas 9.4 and$9 . 7 ,$ Propositions 9.8, and 9.10 and the definition of k-pseudorandom measure, which is Definition 3.3.□

## 10. Correlation estimates for$\Lambda _ { R }$

To conclude the proof of Theorem 1.1 it remains to verify Propositions 9.5 and 9.6. That will be achieved in this section, with the assumption of an estimate (Lemma 10.4) for a certain class of contour integrals involving the ζ-function. The proof of that estimate is given in the preprint [17], and will be repeated in the appendix for the sake of completeness. The techniques of this section are also rather close to those in [17]. We are greatly indebted to Dan Goldston for sharing this preprint with us.

The linear forms condition for$\Lambda _ { R }$. We begin by proving Proposition 9.5. Recall that for each$1 \leqslant i \leqslant m$we have a linear form$\begin{array} { r } { \psi _ { i } ( { \bf x } ) = \sum _ { i = 1 } ^ { t } L _ { i j } x _ { j } + b _ { i } } \end{array}$ in t variables$x _ { 1 } , \ldots , x _ { t }$. The coeficients$L _ { i j }$satisfy$| L _ { i j } | \leqslant \sqrt { w ( N ) } / 2$, where $w ( N )$is the function, tending to infinity with N, which we used to set up the W-trick. We assume that none of the t-tuples$( L _ { i j } ) _ { j = 1 } ^ { t }$are zero or are rational multiples of any other. Define$\theta _ { i } : = W \psi _ { i } + 1$

Let$\begin{array} { r } { B : = \prod _ { j = 1 } ^ { t } I _ { j } } \end{array}$be a product of intervals$I _ { j } { \mathrm { . } }$each of length at least $R ^ { 1 0 m }$. We wish to prove the estimate

$$
\mathbb {E} \bigl (\Lambda_ {R} (\theta_ {1} (\mathbf {x})) ^ {2} \dots \Lambda_ {R} (\theta_ {m} (\mathbf {x})) ^ {2} \mid \mathbf {x} \in B \bigr) = (1 + o _ {m, t} (1)) \left(\frac {W \log R}{\phi (W)}\right) ^ {m}.
$$

The first step is to eliminate the role of the box B. We can use Definition 9.2 to expand the left-hand side as

$$
\mathbb{E}\bigg(\prod_{i = 1}^{m}\sum_{\substack{d_{i},d_{i}^{\prime}\leqslant R\\ d_{i},d_{i}^{\prime}|\theta_{i}(\mathbf{x})}}\mu (d_{i})\mu (d_{i}^{\prime})\log \frac{R}{d_{i}}\log \frac{R}{d_{i}^{\prime}}\bigg|  \mathbf{x}\in B\bigg)
$$

which we can rearrange as

$$
\sum_ {d _ {1}, \ldots , d _ {m}, d _ {1} ^ {\prime}, \ldots , d _ {m} ^ {\prime} \leqslant R} \bigg (\prod_ {i = 1} ^ {m} \mu (d _ {i}) \mu (d _ {i} ^ {\prime}) \log \frac {R}{d _ {i}} \log \frac {R}{d _ {i} ^ {\prime}} \bigg) \mathbb {E} \bigg (\prod_ {i = 1} ^ {m} \mathbf {1} _ {d _ {i}, d _ {i} ^ {\prime} | \theta_ {i} (\mathbf {x})}   \Bigg |   \mathbf {x} \in B \bigg).\tag{10.1}
$$

Because of the presence of the M¨obius functions we may assume that all the $d _ { i } , \ d _ { i } ^ { \prime }$are square-free. Let$D : = [ d _ { 1 } , \ldots , d _ { m } , d _ { 1 } ^ { \prime } , \ldots , d _ { m } ^ { \prime } ]$be the least common multiple of the$d _ { i }$and$d _ { i } ^ { \prime } ;$thus$D \leqslant R ^ { 2 m }$. Observe that the expression $\Pi _ { i = 1 } ^ { m } \mathbf { 1 } _ { d _ { i } , d _ { i } ^ { \prime } | \theta _ { i } ( \mathbf { x } ) }$is periodic with period$D$in each of the components of$\mathbf { x } ,$and can thus be safely defined on$\mathbb { Z } _ { D } ^ { t }$. Since B is a product of intervals of length at least$R ^ { 1 0 m }$, we thus see that

$$
\mathbb {E} \bigg (\prod_ {i = 1} ^ {m} \mathbf {1} _ {d _ {i}, d _ {i} ^ {\prime} | \theta_ {i} (\mathbf {x})}   \Bigg |   \mathbf {x} \in B \bigg) = \mathbb {E} \bigg (\prod_ {i = 1} ^ {m} \mathbf {1} _ {d _ {i}, d _ {i} ^ {\prime} | \theta_ {i} (\mathbf {x})}   \Bigg |   \mathbf {x} \in \mathbb {Z} _ {D} ^ {t} \bigg) + O _ {m, t} (R ^ {- 8 m}).
$$

The contribution of the error term$O _ { m } ( R ^ { - 8 m } )$to (10.1) can be crudely estimated by$O _ { m , t } ( R ^ { - 6 m } \log ^ { 2 m } R )$, which is easily acceptable. Our task is thus to show that

$$
\begin{array}{l} \sum_ {d _ {1}, \ldots , d _ {m}, d _ {1} ^ {\prime}, \ldots , d _ {m} ^ {\prime} \leqslant R} \bigg (\prod_ {i = 1} ^ {m} \mu (d _ {i}) \mu (d _ {i} ^ {\prime}) \log \frac {R}{d _ {i}} \log \frac {R}{d _ {i} ^ {\prime}} \bigg) \mathbb {E} \bigg (\prod_ {i = 1} ^ {m} \mathbf {1} _ {d _ {i}, d _ {i} ^ {\prime} | \theta_ {i} (\mathbf {x})}   \Big |   \mathbf {x} \in \mathbb {Z} _ {D} ^ {t} \bigg) \\ = (1 + o _ {m, t} (1)) \left(\frac {W \log R}{\phi (W)}\right) ^ {m}. \end{array}\tag{10.2}
$$

To prove (10.2), we shall perform a number of standard manipulations (as in $\big [ 1 7 \big ] \big )$to rewrite the left-hand side as a contour integral of an Euler product, which in turn can be rewritten in terms of the Riemann ζ-function and some other simple factors. We begin by using the Chinese remainder theorem (and the square-free nature of$d _ { i } , d _ { i } ^ { \prime } )$to rewrite

$$
\mathbb {E} \bigg (\prod_ {i = 1} ^ {m} \mathbf {1} _ {d _ {i}, d _ {i} ^ {\prime} | \theta_ {i} (\mathbf {x})}   \Bigg |   \mathbf {x} \in \mathbb {Z} _ {D} ^ {t} \bigg) = \prod_ {p | D} \mathbb {E} \bigg (\prod_ {i: p | d _ {i} d _ {i} ^ {\prime}} \mathbf {1} _ {\theta_ {i} (\mathbf {x}) \equiv 0 (\mathrm{mod} p)}   \Bigg |   \mathbf {x} \in \mathbb {Z} _ {p} ^ {t} \bigg).
$$

Note that the restriction that$p$divides D can be dropped since the multiplicand is 1 otherwise. In particular, if$X _ { d _ { 1 } , \dots , d _ { m } } ( p ) : = \{ 1 \leqslant i \leqslant m : p | d _ { i } \}$and

$$
\omega_ {X} (p) := \mathbb {E} \bigg (\prod_ {i \in X} \mathbf {1} _ {\theta_ {i} (\mathbf {x}) \equiv 0 (\mathrm{mod} p)}   \bigg |   \mathbf {x} \in \mathbb {Z} _ {p} ^ {t} \bigg)\tag{10.3}
$$

for each subset$X \subseteq \{ 1 , \dots , m \}$, then

$$
\mathbb {E} \bigg (\prod_ {i = 1} ^ {m} \mathbf {1} _ {d _ {i}, d _ {i} ^ {\prime} | \theta_ {i} (\mathbf {x})}   \bigg |   \mathbf {x} \in \mathbb {Z} _ {D} ^ {t} \bigg) = \prod_ {p} \omega_ {X _ {d _ {1}, \ldots , d _ {m}} (p) \cup X _ {d _ {1} ^ {\prime}, \ldots , d _ {m} ^ {\prime}} (p)} (p).
$$

We can thus write the left-hand side of (10.2) as

$$
\begin{array}{l} \sum_ {d _ {1}, \ldots , d _ {m}, d _ {1} ^ {\prime}, \ldots , d _ {m} ^ {\prime} \in \mathbb {Z} ^ {+}} \\ \left(\prod_ {i = 1} ^ {m} \mu (d _ {i}) \mu (d _ {i} ^ {\prime}) (\log \frac {R}{d _ {i}}) _ {+} (\log \frac {R}{d _ {i} ^ {\prime}}) _ {+}\right) \prod_ {p} \omega_ {X _ {d _ {1}}, \ldots , d _ {m} (p) \cup X _ {d _ {1} ^ {\prime}}, \ldots , d _ {m} ^ {\prime} (p)} (p). \end{array}
$$

To proceed further, we need to express the logarithms in terms of multiplicative functions of the$d _ { i } , d _ { i } ^ { \prime } .$. To this end, we introduce the vertical line contour$\Gamma _ { 1 }$ parametrised by

$$
\Gamma_ {1} (t) := \frac {1}{\log R} + i t; - \infty <   t <   + \infty\tag{10.4}
$$

and observe the contour integration identity

$$
\frac {1}{2 \pi i} \int_ {\Gamma_ {1}} \frac {x ^ {z}}{z ^ {2}} d z = (\log x) _ {+}
$$

valid for any real$x > 0$. The choice of$\displaystyle { \frac { 1 } { \log R } }$for the real part of$\Gamma _ { 1 }$is not currently relevant, but will be convenient later when we estimate the contour integrals that emerge (in particular,$R ^ { z }$is bounded on$\Gamma _ { 1 } .$, while$1 / z ^ { 2 }$is not too large). Using this identity, we can rewrite the left-hand side of (10.2) as

$$
(2 \pi i) ^ {- 2 m} \int_ {\Gamma_ {1}} \dots \int_ {\Gamma_ {1}} F (z, z ^ {\prime}) \prod_ {j = 1} ^ {m} \frac {R ^ {z _ {j} + z _ {j} ^ {\prime}}}{z _ {j} ^ {2} z _ {j} ^ {\prime 2}} d z _ {j} d z _ {j} ^ {\prime}\tag{10.5}
$$

where there are 2m contour integrations in the variables$z _ { 1 } , \ldots , z _ { m } , z _ { 1 } ^ { \prime } , \ldots , z _ { m } ^ { \prime }$ on$\Gamma _ { 1 } , z : = ( z _ { 1 } , \dots , z _ { m } )$and$z ^ { \prime } : = ( z _ { 1 } ^ { \prime } , \dots , z _ { m } ^ { \prime } )$, and

$$
F (z, z ^ {\prime}) := \sum_ {d _ {1}, \dots , d _ {m}, d _ {1} ^ {\prime}, \dots , d _ {m} ^ {\prime} \in \mathbb {Z} ^ {+}} \left(\prod_ {j = 1} ^ {m} \frac {\mu (d _ {j}) \mu (d _ {j} ^ {\prime})}{d _ {j} ^ {z _ {j}} d _ {j} ^ {\prime z _ {j} ^ {\prime}}}\right) \prod_ {p} \omega_ {X _ {d _ {1}, \dots , d _ {m}} (p) \cup X _ {d _ {1} ^ {\prime}, \dots , d _ {m} ^ {\prime}} (p)} (p).\tag{10.6}
$$

We have changed the indices from i to$j$to avoid conflict with the square root of −1. Observe that the summand in (10.6) is a multiplicative function of

$D = [ d _ { 1 } , \ldots , d _ { m } , d _ { 1 } ^ { \prime } , \ldots , d _ { m } ^ { \prime } ]$and thus we have (formally, at least) the Euler product representation$\begin{array} { r } { F ( z , z ^ { \prime } ) = \prod _ { p } E _ { p } ( z , z ^ { \prime } ) } \end{array}$, where

$$
E _ {p} (z, z ^ {\prime}) := \sum_ {X, X ^ {\prime} \subseteq \{1, \dots , m \}} \frac {(- 1) ^ {| X | + | X ^ {\prime} |} \omega_ {X \cup X ^ {\prime}} (p)}{p ^ {\sum_ {j \in X} z _ {j} + \sum_ {j \in X ^ {\prime}} z _ {j} ^ {\prime}}}.\tag{10.7}
$$

From (10.3) we have$\omega _ { \emptyset } ( p ) \ = \ 1$and$\omega _ { X } ( p ) ~ \leqslant ~ 1$, and so$E _ { p } ( z , z ^ { \prime } ) ~ = ~ 1 +$ $O _ { \sigma } ( 1 / p ^ { \sigma } )$when$\Re ( z _ { j } ) , \Re ( z _ { j } ^ { \prime } ) > \sigma$(we obtain more precise estimates below). Thus this Euler product is absolutely convergent to$F ( z , z ^ { \prime } )$in the domain $\{ \Re ( z _ { j } ) , \Re ( z _ { i } ^ { \prime } ) > 1 \}$at least.

To proceed further we need to exploit the hypothesis that the linear parts of$\psi _ { 1 } , \ldots , \psi _ { m }$are nonzero and not rational multiples of each other. This will be done via the following elementary estimates on$\omega _ { X } ( p )$

Lemma 10.1 (Local factor estimate).$I f p \leqslant w ( N )$, then$\omega _ { X } ( p ) = 0$for all nonempty$X ;$in particular,$E _ { p } = 1$when$p \leqslant w ( N )$. If instead$p > w ( N )$ then$\omega _ { X } ( p ) = p ^ { - 1 }$when$| X | = 1$and$\omega _ { X } ( p ) \leqslant p ^ { - 2 }$when$| X | \geqslant 2$

Proof. The first statement is clear, since the maps$\theta _ { j } : \mathbb { Z } _ { p } ^ { t } \to \mathbb { Z } _ { p }$are identically 1 when$p \leqslant w ( N )$. The second statement (when$p > w ( N )$and $| X | = 1 )$is similar since in this case$\theta _ { j }$uniformly covers$\mathbb { Z } _ { p }$. Now suppose $p > w ( N )$and$| X | = 2$. We claim that none of the s pure linear forms$W ( \psi _ { i } - b _ { i } )$ is a multiple of any other (mod$p )$. Indeed, if this were so then we should have $L _ { i j } L _ { i ^ { \prime } j } ^ { - 1 } \equiv \lambda ( { \bmod { p } } )$for some λ, and for all$j = 1 , \ldots , t .$. But if$a / q$and$a ^ { \prime } / q ^ { \prime }$ are two rational numbers in lowest terms, with$| a | , | a ^ { \prime } | , q , q ^ { \prime } < \sqrt { w ( N ) } / 2$, then clearly$a / q \not \equiv a ^ { \prime } / q ^ { \prime } ( \mathrm { m o d } p )$unless$a = a ^ { \prime } , q = q ^ { \prime }$. It follows that the two pure linear forms$\psi _ { i } - b _ { i }$and$\psi _ { i ^ { \prime } } - b _ { i ^ { \prime } }$are rational multiples of one another, contrary to assumption. Thus the set of$\mathbf { x } \in ( \mathbb { Z } / p \mathbb { Z } ) ^ { t }$for which$\theta _ { i } ( \mathbf { x } ) \equiv 0 ( { \bmod { p } } )$for all $i \in X$is contained in the intersection of two skew afine subspaces of$( \mathbb { Z } / p \mathbb { Z } ) ^ { t }$ and as such has cardinality at most$p ^ { t - 2 }$□

This lemma implies, in comparision with (10.7), that

$$
\begin{array}{l}E_{p}(z,z^{\prime}) = 1 - \mathbf{1}_{p > w(N)}\sum_{j = 1}^{m}(p^{-1 - z_{j}} + p^{-1 - z_{j}^{\prime}} - p^{-1 - z_{j} - z_{j}^{\prime}})\\ +\mathbf{1}_{p > w(N)}\sum_{\substack{X,X^{\prime}\subseteq \{1,\ldots ,m\} \\ |X\cup X^{\prime}|\geqslant 2}}\frac{O(1 / p^{2})}{p^{\sum_{j\in X}z_{j} + \sum_{j\in X^{\prime}}z_{j}^{\prime}}}, \end{array}\tag{10.8}
$$

where the$O ( 1 / p ^ { 2 } )$numerator does not depend on$z , z ^ { \prime } .$. To take advantage of this expansion, we factorise$E _ { p } = E _ { p } ^ { ( 1 ) } E _ { p } ^ { ( 2 ) } E _ { p } ^ { ( 3 ) }$, where

$$
\begin{array}{l} E _ {p} ^ {(1)} (z, z ^ {\prime}) := \frac {E _ {p} (z , z ^ {\prime})}{\prod_ {j = 1} ^ {m} (1 - \mathbf {1} _ {p > w (N)} p ^ {- 1 - z _ {j}}) (1 - \mathbf {1} _ {p > w (N)} p ^ {- 1 - z _ {j} ^ {\prime}}) (1 - \mathbf {1} _ {p > w (N)} p ^ {- 1 - z _ {j} - z _ {j} ^ {\prime}}) ^ {- 1}} \\ E _ {p} ^ {(2)} (z, z ^ {\prime}) := \prod_ {j = 1} ^ {m} (1 - \mathbf {1} _ {p \leqslant w (N)} p ^ {- 1 - z _ {j}}) ^ {- 1} (1 - \mathbf {1} _ {p \leqslant w (N)} p ^ {- 1 - z _ {j} ^ {\prime}}) ^ {- 1} (1 - \mathbf {1} _ {p \leqslant w (N)} p ^ {- 1 - z _ {j} - z _ {j} ^ {\prime}}) \\ E _ {p} ^ {(3)} (z, z ^ {\prime}) := \prod_ {i = 1} ^ {m} (1 - p ^ {- 1 - z _ {j}}) (1 - p ^ {- 1 - z _ {j} ^ {\prime}}) (1 - p ^ {- 1 - z _ {j} - z _ {j} ^ {\prime}}) ^ {- 1}. \end{array}
$$

Writing$\begin{array} { r } { G _ { j } : = \prod _ { p } E _ { p } ^ { ( j ) } } \end{array}$for$j = 1 , 2 , 3$, one thus has$F = G _ { 1 } G _ { 2 } G _ { 3 }$(at least for $\Re ( z _ { j } ) , \Re ( z _ { j } ^ { \prime } )$suficiently large). Introducing the Riemann ζ-function$\zeta ( s ) : =$ $\textstyle \prod _ { p } ( 1 - { \frac { 1 } { p ^ { s } } } ) ^ { - 1 }$, we then have

$$
G _ {3} (z, z ^ {\prime}) = \prod_ {j = 1} ^ {m} \frac {\zeta (1 + z _ {j} + z _ {j} ^ {\prime})}{\zeta (1 + z _ {j}) \zeta (1 + z _ {j} ^ {\prime})}\tag{10.9}
$$

and so in particular$G _ { 3 }$can be continued meromorphically to all of$\mathbb { C } ^ { 2 m }$. As for the other two factors, we have the following estimates which allow us to continue these factors a little bit to the left of the imaginary axes.

Definition 10.2. For any$\sigma > 0$, let$\mathcal { D } _ { \sigma } ^ { m } \subseteq \mathbb { C } ^ { 2 m }$denote the domain

$$
\mathcal {D} _ {\sigma} ^ {m} := \left\{z _ {j}, z _ {j} ^ {\prime}: - \sigma <   \Re (z _ {j}), \Re (z _ {j} ^ {\prime}) <   1 0 0, j = 1, \dots , m \right\}.
$$

If$G = G ( z , z ^ { \prime } )$is an analytic function of 2m complex variables on$\mathcal { D } _ { \sigma } ^ { m }$, we define the$C ^ { k } ( \mathcal { D } _ { \sigma } ^ { m } )$norm of$G$for any integer$k \geqslant$0 as

$$
\begin{array}{l} \| G \| _ {C ^ {k} (\mathcal {D} _ {\sigma} ^ {m})} \\ := \sup _ {a _ {1}, \ldots , a _ {m}, a _ {1} ^ {\prime}, \ldots , a _ {m} ^ {\prime}} \big \| \big (\frac {\partial}{\partial z _ {1}} \big) ^ {a _ {1}} \dots \big (\frac {\partial}{\partial z _ {m}} \big) ^ {a _ {m}} \big (\frac {\partial}{\partial z _ {1} ^ {\prime}} \big) ^ {a _ {1} ^ {\prime}} \dots \big (\frac {\partial}{\partial z _ {m} ^ {\prime}} \big) ^ {a _ {m} ^ {\prime}} G \big \| _ {L ^ {\infty} (\mathcal {D} _ {\sigma} ^ {m})} \end{array}
$$

where$a _ { 1 } , \hdots , a _ { m } , a _ { 1 } ^ { \prime } , \hdots , a _ { m } ^ { \prime }$range over all nonnegative integers with total sum at most k.

Lemma 10.3. The Euler products$\begin{array} { r } { \prod _ { p } E _ { p } ^ { ( j ) } \ f o r j = 1 , 2 } \end{array}$are absolutely convergent in the domain$\mathcal { D } _ { 1 / 6 m } ^ { m }$. In particular,$G _ { 1 } , G _ { 2 }$can be continued analytically to this domain. Furthermore, we have the estimates

$$
\begin{array}{c} \| G _ {1} \| _ {C ^ {m} (\mathcal {D} _ {1 / 6 m} ^ {m})} \leqslant O _ {m} (1), \\ \| G _ {2} \| _ {C ^ {m} (\mathcal {D} _ {1 / 6 m} ^ {m})} \leqslant O _ {m, w (N)} (1), \\ G _ {1} (0, 0) = 1 + o _ {m} (1), \\ G _ {2} (0, 0) = (W / \phi (W)) ^ {m}. \end{array}
$$

Remark. The choice$\sigma = 1 / 6 m$is of course not best possible, but in fact any small positive quantity depending on m would sufice for our argument here. The dependence of$O _ { m , w ( N ) } ( 1 )$on$w ( N )$is not important, but one can easily obtain (for instance) growth bounds of the form$w ( N ) ^ { O _ { m } ( w ( N ) ) }$

Proof. First consider$j = 1$. From (10.8) and Taylor expansion we have the crude bound$E _ { p } ^ { ( 1 ) } ( z , z ^ { \prime } ) = 1 + O _ { m } ( p ^ { - 2 + 4 / 6 m } )$in$\begin{array} { r } { \mathcal { D } _ { 1 / 6 m } ^ { m } , } \end{array}$which gives the desired convergence and also the$C ^ { m } ( D _ { 1 / 6 m } ^ { m } )$bound on$G _ { 1 } ;$the estimate for $G _ { 1 } ( 0 , 0 )$also follows since the Euler factors$E _ { p } ^ { ( 1 ) } ( z , z ^ { \prime } )$are identically 1 when $p \leqslant w ( N )$. The bounds for$G _ { 2 }$are easy since this is just a finite Euler product involving at most$w ( N )$terms; the formula for$G _ { 2 } ( 0 , 0 )$follows from direct calculation since$\begin{array} { r } { \frac { \phi ( W ) } { W } = \prod _ { p < w ( n ) } ( 1 - \frac { 1 } { p } ) } \end{array}$□

To estimate (10.5), we now invoke the following contour integration lemma.

Lemma 10.4 ([17]). Let R be a positive real number. Let$G = G ( z , z ^ { \prime } )$ be an analytic function of 2m complex variables on the domain$\mathcal { D } _ { \sigma } ^ { m }$for some $\sigma > 0$, and suppose that

$$
\| G \| _ {C ^ {m} (\mathcal {D} _ {\sigma} ^ {m})} = \exp (O _ {m, \sigma} (\log^ {1 / 3} R)).\tag{10.10}
$$

Then

$$
\begin{array}{l} \frac {1}{(2 \pi i) ^ {2 m}} \int_ {\Gamma_ {1}} \dots \int_ {\Gamma_ {1}} G (z, z ^ {\prime}) \prod_ {j = 1} ^ {m} \frac {\zeta (1 + z _ {j} + z _ {j} ^ {\prime})}{\zeta (1 + z _ {j}) \zeta (1 + z _ {j} ^ {\prime})} \frac {R ^ {z _ {j} + z _ {j} ^ {\prime}}}{z _ {j} ^ {2} z _ {j} ^ {\prime 2}} d z _ {j} d z _ {j} ^ {\prime} \\ = G (0, \ldots , 0) \log^ {m} R + \sum_ {j = 1} ^ {m} O _ {m, \sigma} (\| G \| _ {C ^ {j} (\mathcal {D} _ {\sigma} ^ {m})} \log^ {m - j} R) + O _ {m, \sigma} (e ^ {- \delta \sqrt {\log R}}) \end{array}
$$

for some$\delta = \delta ( m ) > 0$

Proof. While this lemma is essentially in [17], we shall give a complete proof in the appendix for the sake of completeness.□

We apply this lemma with$G : = G _ { 1 } G _ { 2 }$and$\sigma : = 1 / 6 m$. From Lemma 10.3 and the Leibniz rule we have the bounds

$$
\| G \| _ {C ^ {j} \left(\mathcal {D} _ {1 / 6 m} ^ {m}\right)} \leqslant O _ {j, m, w (N)} (1) \text {   for   all   } 0 \leqslant j \leqslant m,
$$

and in particular we obtain (10.10) by choosing$w ( N )$to grow suficiently slowly in N. Also we have$\begin{array} { r } { G ( 0 , 0 ) = ( 1 + o _ { m } ( 1 ) ) ( \frac { W } { \phi ( W ) } ) ^ { m } } \end{array}$from that lemma. We conclude (again taking w(N) suficiently slowly growing in$N )$that the quantity in (10.5) is$\begin{array} { r } { ( 1 + o _ { m } ( 1 ) ) ( \frac { W \log R } { \phi ( W ) } ) ^ { m } } \end{array}$, as desired. This concludes the proof of Proposition 9.5.□

Higher order correlations for$\Lambda _ { R }$. We now prove Proposition 9.6, using arguments very similar to those used to prove Proposition 9.5. The main diferences here are that the number of variables t is just equal to 1, but on the other hand all the linear forms are equal to each other,$\psi _ { i } ( x _ { 1 } ) = x _ { 1 }$. In particular, these linear forms are now rational multiples of each other and so Lemma 10.1 no longer applies. However, the arguments before that lemma are still valid; thus we can still write the left-hand side of (9.1) as an expression of the form (10.5) plus an acceptable error, where F is again defined by (10.6) and$E _ { p }$is defined by (10.7); the diference now is that$\omega _ { X } ( p )$is the quantity

$$
\omega_ {X} (p) := \mathbb {E} \bigg (\prod_ {i \in X} \mathbf {1} _ {W (x + h _ {i}) + 1 \equiv 0 (\mathrm{mod} p)}   \Bigg |   x \in \mathbb {Z} _ {p} \bigg).
$$

Again we have$\omega _ { \emptyset } ( p ) = 1$for all p. The analogue of Lemma 10.1 is as follows.

Lemma 10.5. If$p \ \leqslant \ w ( N )$, then$\omega _ { X } ( p ) = 0$for all nonempty$X ;$in particular,$E _ { p } = 1$when$p \leqslant w ( N )$. If instead$p > w ( N )$, then$\omega _ { X } ( p ) = p ^ { - 1 }$ when$| X | = 1$and$\omega _ { X } ( p ) \leqslant p ^ { - 1 }$when$| X | \geqslant 2$. Furthermore,$i f \left| X \right| \geqslant 2$then $\omega _ { X } ( p ) = 0$unless p divides$\begin{array} { r } { \Delta : = \prod _ { 1 \leqslant i < j \leqslant s } | h _ { i } - h _ { j } | } \end{array}$

Proof. When$p \leqslant w ( N )$then$W ( x + h _ { i } ) + 1 \equiv 1 ( \mathrm { m o d } p )$and the claim follows. When$p > w ( N )$and$| X | \geqslant 1 , \omega _ { X } ( p )$is equal to$1 / p$when the residue classes$\{ h _ { i } ( \mathrm { m o d } p ) : i \in X \}$are all equal, and zero otherwise, and the claim again follows.□

In light of this lemma, the analogue of (10.8) is now

$$
E _ {p} (z, z ^ {\prime}) = 1 - \mathbf {1} _ {p > w (N)} \sum_ {j = 1} ^ {m} (p ^ {- 1 - z _ {j}} + p ^ {- 1 - z _ {j} ^ {\prime}} - p ^ {- 1 - z _ {j} - z _ {j} ^ {\prime}}) + \mathbf {1} _ {p > w (N), p | \Delta} \lambda_ {p} (z, z ^ {\prime})\tag{10.11}
$$

where$\lambda _ { p } \big ( z , z ^ { \prime } \big )$is an expression of the form

$$
\lambda_{p}(z,z^{\prime}) = \sum_{\substack{X,X^{\prime}\subseteq \{1,\ldots ,m\} \\ |X\cup X^{\prime}|\geqslant 2}}\frac{O(1 / p)}{p^{\sum_{j\in X}z_{j} + \sum_{j\in X^{\prime}}z_{j}^{\prime}}}
$$

and the$O ( 1 / p )$quantities do not depend on$z , z ^ { \prime }$. We can thus factorise

$$
E _ {p} = E _ {p} ^ {(0)} E _ {p} ^ {(1)} E _ {p} ^ {(2)} E _ {p} ^ {(3)},
$$

where

$$
\begin{array}{l} E _ {p} ^ {(0)} = 1 + \mathbf {1} _ {p > w (N), p | \Delta} \lambda_ {p} (z, z ^ {\prime}) \\ E _ {p} ^ {(1)} = \frac {E _ {p}}{E _ {p} ^ {(0)} \prod_ {j = 1} ^ {m} (1 - \mathbf {1} _ {p > w (N)} p ^ {- 1 - z _ {j}}) (1 - \mathbf {1} _ {p > w (N)} p ^ {- 1 - z _ {j} ^ {\prime}}) (1 - \mathbf {1} _ {p > w (N)} p ^ {- 1 - z _ {j} - z _ {j} ^ {\prime}}) ^ {- 1}} \\ E _ {p} ^ {(2)} = \prod_ {j = 1} ^ {m} (1 - \mathbf {1} _ {p \leqslant w (N)} p ^ {- 1 - z _ {j}}) ^ {- 1} (1 - \mathbf {1} _ {p \leqslant w (N)} p ^ {- 1 - z _ {j} ^ {\prime}}) ^ {- 1} (1 - \mathbf {1} _ {p \leqslant w (N)} p ^ {- 1 - z _ {j} - z _ {j} ^ {\prime}}) \end{array}
$$

$$
E _ {p} ^ {(3)} = \prod_ {j = 1} ^ {m} (1 - p ^ {- 1 - z _ {j}}) (1 - p ^ {- 1 - z _ {j} ^ {\prime}}) (1 - p ^ {- 1 - z _ {j} - z _ {j} ^ {\prime}}) ^ {- 1}.
$$

Write$\begin{array} { r } { G _ { j } \ = \ \prod _ { p } E _ { p } ^ { ( j ) } } \end{array}$. Then, as before,${ \cal F } ~ = ~ G _ { 0 } G _ { 1 } G _ { 2 } G _ { 3 }$and$G _ { 3 }$is given by$( 1 0 . 9 )$as before. As for$G _ { 0 } , G _ { 1 } , G _ { 2 }$, we have the following analogue of Lemma 10.3.

Lemma 10.6. Let$0 < \sigma < 1 / 6 m$. Then the Euler products$\begin{array} { r } { \prod _ { p } E _ { p } ^ { ( l ) } } \end{array}$for $l = 0 , 1 , 2$are absolutely convergent in the domain$\mathcal { D } _ { \sigma } ^ { m }$. In particular,$G _ { 0 } , G _ { 1 }$ $G _ { 2 }$can be continued analytically to this domain. Furthermore, we have the estimates

$$
\| G _ {0} \| _ {C ^ {r} \left(\mathcal {D} _ {\sigma} ^ {m}\right)} \leqslant O _ {m} \left(\frac {\log R}{\log \log R}\right) ^ {r} \prod_ {p | \Delta} (1 + O _ {m} \left(p ^ {2 m \sigma - 1}\right)) \quad f o r 0 \leqslant r \leqslant m,\tag{10.12}
$$

(10.13)

$$
\| G _ {0} \| _ {C ^ {m} (\mathcal {D} _ {1 / 6 m} ^ {m})} \leqslant \exp (O _ {m} (\log^ {1 / 3} R)),
$$

$$
\left\| G _ {1} \right\| _ {C ^ {m} (\mathcal {D} _ {1 / 6 m} ^ {m})} \leqslant O _ {m} (1),
$$

$$
\left\| G _ {2} \right\| _ {C ^ {m} (\mathcal {D} _ {1 / 6 m} ^ {m})} \leqslant O _ {m, w (N)} (1),\tag{10.14}
$$

$$
G _ {0} (0, 0) = \prod_ {p | \Delta} (1 + O _ {m} (p ^ {- 1 / 2})),
$$

$$
G _ {1} (0, 0) = 1 + o _ {m} (1),
$$

$$
G _ {2} (0, 0) = (W / \phi (W)) ^ {m}.
$$

Proof. The estimates for$G _ { 1 }$and$G _ { 2 }$proceed exactly as in Lemma 10.3 (the additional factors of$\lambda _ { p } \big ( z , z ^ { \prime } \big )$which appear in both the numerator and denominator of$E _ { p } ^ { ( 1 ) }$cancel to first order, and thus do not present any new dificulties); it is the estimates for$G _ { 0 }$which are the most interesting.

We begin by proving (10.12). Fix l. First observe that$\begin{array} { r } { G _ { 0 } = \prod _ { p | \Delta } E _ { p } ^ { ( 0 ) } } \end{array}$ Now the number of primes dividing$\Delta$is at most$O ( \log \Delta / \log \log \Delta )$. Using the crude bound

$$
\Delta = \prod_ {1 \leqslant i <   j \leqslant m} | h _ {i} - h _ {j} | \leqslant N ^ {m ^ {2}} \leqslant R ^ {O _ {m} (1)},\tag{10.15}
$$

we thus see that the number of factors in the Euler product for$G _ { 0 }$is $O _ { m } \big ( \frac { \log R } { \log \log R } \big )$. Upon diferentiating r times for any$0 \leqslant r \leqslant$m using the Leibniz rule, one gets a sum of$O _ { m } ( ( \log R /$log log$R ) ^ { r } )$terms, each of which consists of$O _ { m } { \left( \log R / \right. }$log log$R )$factors, each of which is equal to some derivative of $1 + \lambda _ { p } ( z , z ^ { \prime } )$of order between 0 and$r .$On$\mathcal { D } _ { \sigma } ^ { m }$, each factor is bounded by $1 + \bar { O _ { m } } ( p ^ { 2 m \sigma - 1 } )$(in fact, the terms containing a nonzero number of derivatives will be much smaller since the constant term 1 is eliminated). This gives (10.12).

Now we prove (10.13). In light of (10.12), it sufices to show that

$$
\prod_ {p \mid \Delta} (1 + O _ {m} (p ^ {2 m \sigma - 1})) \leqslant \exp (O _ {m} (\log^ {1 / 3} R)).
$$

Taking logarithms and using the hypothesis$\sigma < 1 / 6 m$(and (10.15)), we reduce to showing

$$
\sum_ {p \mid \Delta} p ^ {- 2 / 3} \leqslant O (\log^ {1 / 3} \Delta).
$$

But there are at most$O ( \log \Delta /$log log Δ) primes dividing$\Delta ,$hence the lefthand side can be crudely bounded by

$$
\sum_ {1 \leqslant n \leqslant O (\log \Delta / \log \log \Delta)} n ^ {- 2 / 3} = O (\log^ {1 / 3} \Delta)
$$

as desired.

The bound (10.14) now follows from the crude estimate$E _ { p } ^ { ( 0 ) } ( z , z ^ { \prime } ) = 1 +$ $O _ { m } ( p ^ { - 1 / 2 } )$□

We now apply Lemma 10.4 with$\sigma : = 1 / 6 m$and$G : = G _ { 0 } G _ { 1 } G _ { 2 }$. Again by the Leibniz rule we have the bound (10.10), and furthermore

$$
\| G \| _ {C ^ {r} (\mathcal {D} _ {\sigma} ^ {m})} \leqslant O _ {m} (1) O _ {m, w (N)} (1) \left(\frac {\log R}{\log \log R}\right) ^ {r} \prod_ {p | \Delta} \left(1 + O _ {m} (p ^ {- 1 / 2})\right)
$$

for all$0 \leqslant r \leqslant m$. From Lemma 10.6 and Lemma 10.4 we can then estimate (10.5) as

$$
\begin{array}{l} \leqslant (1 + o _ {m} (1)) \left(\frac {W}{\phi (W)}\right) ^ {m} \log^ {m} R \prod_ {p | \Delta} \Big (1 + O _ {m} (p ^ {- 1 / 2}) \Big) \\ \qquad + O _ {m, w (N)} \left(\frac {\log^ {m} R}{\log \log R}\right) \prod_ {p | \Delta} \Big (1 + O _ {m} (p ^ {- 1 / 2}) \Big) + O _ {m} (e ^ {- \delta \sqrt {\log R}}). \end{array}
$$

The claim (9.1) then follows by choosing$w ( N )$(and hence W) suficiently slowly growing in N (and hence in$R )$. Proposition 9.6 follows.□

Remark. It should be clear that the above argument not only gives an upper bound for the left-hand side of (9.1), but in fact gives an asymptotic, by working out$G _ { 0 } ( 0 , 0 )$more carefully; this is discussed in detail (in the$W = 1$ case) in [17].

## 11. Further remarks

In this section we discuss some extensions and refinements of our main result. First of all, notice that our proof actually shows that there is some constant$\gamma ( k )$such that the number of k-term progressions of primes, all less than N, is at least$( \gamma ( k ) + o ( 1 ) ) N ^ { 2 } / \log ^ { k } N$. This is because the error term in (3.9) does not actually need to be$o ( 1 )$, but merely less than$\textstyle { \frac { 1 } { 2 } } c ( k , \delta ) + o ( 1 )$(for instance). Working backwards through the proof, this eventually reveals that the quantity$w ( N )$does not actually need to be growing in N, but can instead be a fixed number depending only on k (although this number will be very large because our final bounds o(1) decayed to zero extremely slowly). Thus W can be made independent of$N$, and so the loss incurred by the W-trick when passing from primes to primes equal to 1 mod$W$is bounded uniformly in N. Nevertheless the bound we obtain on$\gamma ( k )$is extremely poor, in part because of the growth of constants in the best known bounds$c ( k , \delta )$on Szemer´edi’s theorem in [19], but also because we have not attempted to optimise the decay rate of the$o ( 1 )$factors and hence will need to take$w ( N )$to be extremely large. In the other direction, standard sieve theory arguments show that the number of k-term progressions of primes all less than N is at most$O _ { k } ( N ^ { 2 } / \log ^ { k } N )$，and so the lower bounds are only of by a constant depending on k.

As remarked earlier, our method also extends to prove Theorem 1.2, namely that any subset of the primes with positive relative upper density contains a k-term arithmetic progression. The only significant$\mathrm { c h a n g e ^ { 2 3 } }$to the proof is that one must use the pigeonhole principle to replace the residue class$n \equiv 1 ( { \bmod { W } } )$by a more general residue class$n \equiv b ( { \bmod { W } } )$for some b coprime to W, since the set A in Theorem 1.2 does not need to obey a Dirichlet-type theorem in these residue classes. However it is easy to verify that this does not significantly afect the rest of the argument, and we leave the details to the reader.

Applying Theorem 1.2 to the set of primes$p \equiv 1 ( { \bmod { 4 } } )$, we obtain the previously unknown fact that there are arbitrarily long progressions consisting of numbers which are the sum of two squares. For this problem, more satisfactory results were known for small k than was the case for the primes. Let S be the set of sums of two squares. It is a simple matter to show that there are infinitely many 4-term arithmetic progressions in S. Indeed, Heath-Brown [26] observed that the numbers$( n - 1 ) ^ { 2 } + ( n - 8 ) ^ { 2 } , ( n - 7 ) ^ { 2 } + ( n + 4 ) ^ { 2 }$2 $( n + 7 ) ^ { 2 } + ( n - 4 ) ^ { 2 }$and$( n + 1 ) ^ { 2 } + ( n + 8 ) ^ { 2 }$always form such a progression; in fact, he was able to prove much more, in particular finding an asymptotic for the number of 4-term progressions in S, all of whose members are at most N (weighted by$r ( n )$, the number of representations of n as the sum of two squares).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N<sub>1</sub>, N<sub>2</sub>, . . . → ∞</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N<sub>j</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>23</sup>Also, since we are only assuming positivity of the upper density and not the lower density, we only have good density control for an infinite sequence of integers, which may not be prime. However one can easily use Bertrand’s postulate (for instance) to make the prime, giving up a factor of  at most.O(1)</span></small>

It is reasonably clear that our method will produce long arithmetic progressions for many sets of primes for which one can give a lower bound which agrees with some upper bound coming from a sieve, up to a multiplicative constant. Invoking Chen’s famous theorem [7] to the efect that there are $\gg N / \log ^ { 2 } N$primes$p \leqslant N$for which$p + 2$is a prime or a product of two primes, we ought to be able to adapt our arguments to show that there are arbitrarily long arithmetic progressions$p _ { 1 } , \ldots , p _ { k }$of primes, such that each$p _ { i } + 2$ is either prime or the product of two primes; indeed there should be$N / \log ^ { 2 k } N$ such progressions with entries less than N. Whilst we do not$\mathrm { \ p l a n ^ { 2 4 } }$to write a detailed proof of this fact, we will in [23] give a proof of the case$k = 3$using harmonic analysis.

The methods in this paper suggest a more general “transference princi-$\mathrm { p l e } ^ { \prime \prime }$, in that if a type of pattern (such as an arithmetic progression) is forced to arise infinitely often within sets of positive density, then it should also be forced to arise infinitely often inside the prime numbers, or more generally inside any subset of a pseudorandom set (such as the “almost primes”) of positive relative density. Thus, for instance, one is led to conjecture a Bergelson-Leibman type result (cf. [4]) for primes. That is, one could hope to show that if$F _ { i } : \mathbb { N }  \mathbb { N }$ are polynomials with$F ( 0 ) = 0$, then there are infinitely many configurations $( a + F _ { 1 } ( d ) , \dots , a + F _ { k } ( d ) )$in which all k elements are prime. This however seems to require some$\mathrm { m o d i f i c a t i o n ^ { 2 5 } }$to our current argument, in large part because of the need to truncate the step parameter d to be at most a small power of N. In a similar spirit, the work of Furstenberg and Katznelson [11] on multidimensional analogues of Szemer´edi’s theorem, combined with this transference principle, now suggests that one should be able to show<sup>26</sup> that the Gaussian primes in Z[i] contain infinitely many constellations of any prescribed shape, and similarly for other number fields. Furthermore, the later work of Furstenberg and Katznelson [12] on density Hales-Jewett theorems suggests that one could also show that for any finite field$F ,$the monic irreducible polynomials in$F [ t ]$contain afine subspaces over F of arbitrarily high dimension. Again, these results would require nontrivial modifications to our argument for a number of reasons, not least of which is the fact that the characteristic factors for these more advanced generalizations of Szemer´edi’s theorem are much less well understood.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1  b < W</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">b, b + 2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ΛR(Wn + 1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">W;</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Λ<sub>R</sub>(Wn + b)Λ<sub>R</sub>(Wn + b + 2)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>24</sup>Very briefly, the idea is to replace the function Λ<sub>R</sub>(Wn + 1) in the definition of the pseudorandom measure ν with a variant such as for some for which are both coprime to one can use Chen’s theorem and the pigeonhole principle to locate a b for which this majorant will capture a large number of Chen primes. We leave the details to the reader.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>25</sup>Note added in press: such a result has been obtained by the second author and T. Ziegler, to appear in Acta Math.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>26</sup>Note added in press: such a result has been obtained by the second author, J. d’Analyse Math´ematique 99 (2006), 109–176.</span></small>

## Appendix A. Proof of Lemma 10.4

In this appendix we prove Lemma 10.4, which was essentially proved in [17], but for the sake of self-containedness we provide a complete proof here (following very closely the approach in [17]).

Throughout this section,$R \geqslant 2 , m \geqslant 1$, and$\sigma > 0$will be fixed. We shall use$\delta > 0$to denote various small constants, which may vary from line to line (the previous interpretation of$\delta$as the average value of a function$f$will now be irrelevant). We begin by recalling the classical zero-free region for the Riemann$\zeta$function.

Lemma A.1 (Zero-free region). The classical zero free region$\mathcal { Z }$is the closed region

$$
\mathcal {Z} := \{s \in \mathbb {C}: 1 0 \geqslant \Re s \geqslant 1 - \frac {\beta}{\log (| \Im s | + 2)} \}
$$

for some small$0 ~ < ~ \beta ~ < ~ 1$. Then if$\beta$is suficiently small,$\zeta$is nonzero and meromorphic in$\mathcal { Z }$with a simple pole at 1 and no other singularities. Furthermore, the bounds

$$
\zeta (s) - \frac {1}{s - 1} = O (\log (| \Im s | + 2)); \quad \frac {1}{\zeta (s)} = O (\log (| \Im s | + 2))
$$

for all$s \in { \mathcal { Z } }$

Proof. See Titchmarsh [41, Ch. 3].

Fix$\beta$in the above lemma; we may take$\beta$to be small enough that$\mathcal { Z }$ is contained in the region where$1 - \sigma < \Re ( s ) < 1 0 1$. We will allow all our constants in the$O ( )$notation to depend on$\beta$and$\sigma ,$and omit explicit mention of these dependencies from our subscripts.

In addition to the contour$\Gamma _ { 1 }$defined in (10.4), we will need the two further contours$\Gamma _ { 0 }$and$\Gamma _ { 2 }$, defined by

$$
\begin{array}{l} \Gamma_ {0} (t) := - \frac {\beta}{\log (| t | + 2)} + i t, \qquad - \infty <   t <   \infty , \\ \Gamma_ {2} (t) := 1 + i t, \quad - \infty <   t <   \infty . \end{array}\tag{A.1}
$$

Thus$\Gamma _ { 0 }$is the left boundary of$\mathcal { Z } - 1$(which therefore lies to the left of the origin), while$\Gamma _ { 1 }$and$\Gamma _ { 2 }$are vertical lines to the right of the origin. The usefulness of$\Gamma _ { 2 }$for us lies in the simple observation that$\zeta ( 1 + z + z ^ { \prime } )$has no poles when$z \in \mathcal { Z } - 1$and$z ^ { \prime } \in \Gamma _ { 2 }$, but we will not otherwise attempt to estimate any integrals on$\Gamma _ { 2 }$

We observe the following elementary integral estimates.

Lemma A.2. Let$A , B$be fixed constants with$A > 1$. Then there are the bounds

(A.2)

$$
\int_ {\Gamma_ {0}} \log^ {B} (| z | + 2) \left| \frac {R ^ {z} d z}{z ^ {A}} \right| \leqslant O _ {A, B} (e ^ {- \delta \sqrt {\log R}});\tag{A.3}
$$

$$
\int_ {\Gamma_ {1}} \log^ {B} (| z | + 2) \left| \frac {R ^ {z} d z}{z ^ {2}} \right| \leqslant O _ {B} (\log R).
$$

Here$\delta = \delta ( A , B , \beta ) > 0$is a constant independent of R.

Proof. We first bound the left-hand side of (A.2). Substitute in the parametrisation (A.1). Since$\Gamma _ { 0 } ^ { \prime } ( t ) = { \cal O } ( 1 )$and$| z | \gg | t | + \beta$we have, for any $T \geqslant 2$

$$
\begin{array}{r l} & {\int_ {\Gamma_ {0}} \log^ {B} (| z | + 2) \left| \frac {R ^ {z} d z}{z ^ {A}} \right| \leqslant O _ {B} (\int_ {0} ^ {\infty} R ^ {- \beta / (\log (| t | + 2))} \frac {\log^ {B} (| t | + 2)}{(| t | + \beta) ^ {A}} d t)} \\ & {\qquad \leqslant O _ {B} (\log^ {B} T \int_ {0} ^ {T} R ^ {- \beta / \log (t + 2)} d t + \int_ {T} ^ {\infty} \frac {\log^ {B} t}{t ^ {A}} d t)} \\ & {\qquad \leqslant O _ {A, B} (T \log^ {B} T \exp (- \beta \log R / \log T) + T ^ {1 - A} \log^ {B} T).} \end{array}
$$

Choosing$T = \exp ( \sqrt { \beta \log R / 2 } )$one obtains the claimed bound. The bound $\mathrm { ( A . 3 ) }$is much simpler, and can be obtained by noting that$R ^ { z }$is bounded on$\Gamma _ { 1 }$, and substituting in (10.4) splitting the integrand up into the ranges $| t | \leqslant 1 / \log R$and$| t | > 1 / \log R$□

The next lemma is closely related to the case$m = 1$of Lemma 10.4.

Lemma A.3. Let$f ( z , z ^ { \prime } )$be analytic in$\mathcal { D } _ { \sigma } ^ { 1 }$and suppose that

$$
| f (z, z ^ {\prime}) | \leqslant \exp (O _ {m} (\log^ {1 / 3} R))
$$

uniformly in this domain. Then the integral

$$
I := \frac {1}{(2 \pi i) ^ {2}} \int_ {\Gamma_ {1}} \int_ {\Gamma_ {1}} f (z, z ^ {\prime}) \frac {\zeta (1 + z + z ^ {\prime})}{\zeta (1 + z) \zeta (1 + z ^ {\prime})} \frac {R ^ {z + z ^ {\prime}}}{z ^ {2} z ^ {\prime 2}} d z d z ^ {\prime}
$$

obeys the estimate

$$
\begin{array}{l} I = f (0, 0) \log R + \frac {\partial f}{\partial z ^ {\prime}} (0, 0) \\ \qquad + \frac {1}{2 \pi i} \int_ {\Gamma_ {1}} f (z, - z) \frac {d z}{\zeta (1 + z) \zeta (1 - z) z ^ {4}} + O _ {m} (e ^ {- \delta \sqrt {\log R}}) \end{array}
$$

for some$\delta = \delta ( \sigma , \beta ) > 0$independent of R.

Proof. We observe from Lemma A.1 that we have enough decay of the integrand in the domain$\mathcal { D } _ { \sigma } ^ { 1 }$to interchange the order of integration, and to shift contours in either one of the variables$z , z ^ { \prime }$while keeping the other fixed, without any dificulties when$\Im ( z ) , \Im ( z ^ { \prime } )  \infty ;$the only issue is to keep track of when the contour passes through a pole of the integrand. In particular we can shift the$z ^ { \prime }$contour from$\Gamma _ { 1 }$to$\Gamma _ { 2 }$, since we do not encounter any of the poles of the integrand while doing so. Let us look at the integrand for each fixed$z ^ { \prime } \in \Gamma _ { 2 }$, viewing it as an analytic function of z. We now attempt to shift the z contour of integration to$\Gamma _ { 0 }$. In so doing the contour passes just one pole, a simple one at$z = 0$. The residue there is$\begin{array} { r } { \frac { 1 } { 2 \pi i } \int _ { \Gamma _ { 2 } } f ( 0 , z ^ { \prime } ) \frac { R ^ { z ^ { \prime } } } { z ^ { \prime 2 } } d z ^ { \prime } } \end{array}$, and so we have$I = I _ { 1 } + I _ { 2 }$, where

$$
\begin{array}{l} I _ {1} := \frac {1}{2 \pi i} \int_ {\Gamma_ {2}} f (0, z ^ {\prime}) \frac {R ^ {z ^ {\prime}}}{z ^ {\prime 2}} d z ^ {\prime} \\ I _ {2} := \frac {1}{(2 \pi i) ^ {2}} \int_ {\Gamma_ {2}} \int_ {\Gamma_ {0}} f (z, z ^ {\prime}) \frac {\zeta (1 + z + z ^ {\prime}) R ^ {z + z ^ {\prime}}}{\zeta (1 + z) \zeta (1 + z ^ {\prime}) z ^ {2} z ^ {\prime 2}} d z d z ^ {\prime}. \end{array}
$$

To evaluate$I _ { 1 }$, we shift the$z ^ { \prime }$contour of integration to$\Gamma _ { 0 }$. Again there is just one pole, a double one at$z ^ { \prime } = 0$. The residue there is$f ( 0 , 0 )$log$R +$ $\begin{array} { r } { \frac { \partial \bar { f _ { } } } { \partial z ^ { \prime } } ( 0 , 0 ) } \end{array}$, and so

$$
\begin{array}{r l} & I _ {1} = f (0, 0) \log R + \frac {\partial f}{\partial z ^ {\prime}} (0, 0) + \frac {1}{2 \pi i} \int_ {\Gamma_ {0}} f (0, z ^ {\prime}) \frac {R ^ {z ^ {\prime}}}{z ^ {\prime 2}} d z ^ {\prime} \\ & \qquad = f (0, 0) \log R + \frac {\partial f}{\partial z ^ {\prime}} (0, 0) + O _ {m} (e ^ {- \delta \sqrt {\log R}}), \end{array}
$$

for some$\delta > 0$, the latter step being a consequence of our bound on$f$and (A.2) (in the case$B = 0 )$.

To estimate$I _ { 2 } ,$we first swap the order of integration and, for each fixed$z ,$ view the integrand as an analytic function of$z ^ { \prime } .$. We move the$z ^ { \prime }$contour from $\Gamma _ { 2 }$to$\Gamma _ { 0 } .$, this again being allowed since we have suficient decay in vertical strips as$| \Im z ^ { \prime } |  \infty$. In so doing we pass exactly two simple poles, at$z ^ { \prime } = - z$ and$z ^ { \prime } = 0$. The residue at the first is exactly

$$
\frac {1}{2 \pi i} \int_ {\Gamma_ {0}} f (z, - z) \frac {d z}{\zeta (1 + z) \zeta (1 - z) z ^ {4}},
$$

which is one of the terms appearing in our formula for$I .$

The residue at$z ^ { \prime } = 0$is

$$
\int_ {\Gamma_ {0}} f (z, 0) \frac {R ^ {z}}{z ^ {2}} d z,
$$

which is$O ( e ^ { - \delta { \sqrt { \log R } } } )$for some$\delta > 0$by (A.2). The value of$I _ { 2 }$is the sum of these two quantities and the integral over the new contour$\Gamma _ { 0 }$, which is

$$
\int_ {\Gamma_ {0}} \int_ {\Gamma_ {0}} f (z, z ^ {\prime}) \frac {\zeta (1 + z + z ^ {\prime}) R ^ {z + z ^ {\prime}}}{\zeta (1 + z) \zeta (1 + z ^ {\prime}) z ^ {2} z ^ {\prime 2}} d z d z ^ {\prime}.\tag{A.4}
$$

In this integrand we have$| f | ~ = ~ \exp ( { \cal O } _ { m } ( \log ^ { 1 / 3 } R ) )$and, by Lemma A.1, $1 / | \zeta ( 1 + z ) | \ll \log ( | \Im z | + 2 )$and$1 / | \zeta ( 1 + z ^ { \prime } ) | \ll \log ( | \Im z ^ { \prime } | + 2 )$. Assume that$\beta < 1 / 1 0$, as we obviously may. We claim that

$$
| \zeta (1 + z + z ^ {\prime}) | \ll (1 + | z | + | z ^ {\prime} |) ^ {1 / 4} \ll (1 + | z |) ^ {1 / 4} (1 + | z ^ {\prime} |) ^ {1 / 4}\tag{A.5}
$$

for all$z , z ^ { \prime } \in \Gamma _ { 0 }$. Once this is proven it follows from (A.2), applied with $A = 7 / 4$and$A = 2$, that the integral$\left( \mathrm { { A . 4 } } \right)$is bounded by$\hat { O _ { m } } ( e ^ { - \delta \sqrt { \log R } } )$for some$\delta > 0$. Now if$1 / 2 \leqslant \sigma \leqslant 1$and$\vert t \vert ~ \geqslant ~ 1 / 1 0 0$we have the convexity bound$| \zeta ( \sigma + i t ) | \ll _ { \epsilon } | t | ^ { 1 - \sigma + \epsilon }$(cf. [41, Ch. V]), and so (A.5) is indeed true provided that$| \mathbb { S } ( z + z ^ { \prime } ) | \geqslant 1 / 1 0 0$. However since$z , z ^ { \prime } \in \Gamma _ { 0 }$one may see that if$| \mathbb { S } ( z ) | , | \mathbb { S } ( z ^ { \prime } ) | \leqslant t$then$| z + z ^ { \prime } | \gg 1 / \log ( t + 2 )$. It follows from Lemma A.1 that (A.5) holds when$| \mathbb { S } ( z + z ^ { \prime } ) | \leqslant 1 / 1 0 0$as well.

Thus we now have estimates for$I _ { 1 }$and$I _ { 2 }$up to errors of$O _ { m } ( e ^ { - \delta \sqrt { \log R } } )$ Putting all of this together completes the proof of the lemma.□

Proof of Lemma 10.4. Let$G = G ( z , z ^ { \prime } )$be an analytic function of 2m complex variables on the domain$\mathcal { D } _ { \sigma } ^ { m }$obeying the derivative bounds (10.10). We will allow all our implicit constants in the$O ( )$notation to depend on m, $\beta , \sigma$. We are interested in the integral

$$
I (G, m) := \frac {1}{(2 \pi i) ^ {2 m}} \int_ {\Gamma_ {1}} \dots \int_ {\Gamma_ {1}} G (z, z ^ {\prime}) \prod_ {j = 1} ^ {s} \frac {\zeta (1 + z _ {j} + z _ {j} ^ {\prime})}{\zeta (1 + z _ {j}) \zeta (1 + z _ {j} ^ {\prime})} \frac {R ^ {z _ {j} + z _ {j} ^ {\prime}}}{z _ {j} ^ {2} z _ {j} ^ {\prime 2}} d z _ {j} d z _ {j} ^ {\prime},
$$

and wish to prove the estimate

$$
I (G, m) := G (0, \dots , 0) (\log R) ^ {m} + \sum_ {j = 1} ^ {m} O (\| G \| _ {C ^ {j} \left(\mathcal {D} _ {\sigma} ^ {s}\right)} (\log R) ^ {m - j}) + O \left(e ^ {- \delta \sqrt {\log R}}\right).
$$

The proof is by induction on m. The case$m = 1$is a swift deduction from Lemma A.3, the only issue being an estimation of the term

$$
\frac {1}{2 \pi i} \int_ {\Gamma_ {0}} G (z _ {1}, - z _ {1}) \frac {d z _ {1}}{\zeta (1 + z _ {1}) \zeta (1 - z _ {1}) z _ {1} ^ {4}}.
$$

It is not hard to check (using Lemma A.1) that

$$
\int_ {\Gamma_ {0}} \left| \frac {d z _ {1}}{\zeta (1 + z _ {1}) \zeta (1 - z _ {1}) z _ {1} ^ {4}} \right| = O (1),\tag{A.6}
$$

and so this term is$O ( \operatorname* { s u p } _ { z \in { \mathcal { D } } _ { \sigma } ^ { 1 } } | G ( z ) | ) = O ( \| G \| _ { C ^ { 1 } ( { \mathcal { D } } _ { \sigma } ^ { 1 } ) } )$ σ

Suppose then that we have established the result for$m \geqslant 1$and wish to deduce it for$m + 1$. Applying Lemma A.3 in the variables$z _ { m + 1 } , z _ { m + 1 } ^ { \prime }$, we get

$$
\begin{array}{l} I (G, m + 1) \\ = \frac {\log R}{(2 \pi i) ^ {2 m}} \int_ {\Gamma_ {1}} \dots \int_ {\Gamma_ {1}} G (z _ {1}, \ldots , z _ {m}, 0, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime}, 0) \prod_ {j = 1} ^ {m} \frac {\zeta (1 + z _ {j} + z _ {j} ^ {\prime})}{\zeta (1 + z _ {j}) \zeta (1 + z _ {j} ^ {\prime})} \frac {R ^ {z _ {j} + z _ {j} ^ {\prime}}}{z _ {j} ^ {2} z _ {j} ^ {\prime 2}} d z _ {j} d z _ {j} ^ {\prime} \\ \quad + \frac {1}{(2 \pi i) ^ {2 m}} \int_ {\Gamma_ {1}} \dots \int_ {\Gamma_ {1}} H (z _ {1}, \ldots , z _ {m}, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime}) \prod_ {j = 1} ^ {m} \frac {\zeta (1 + z _ {j} + z _ {j} ^ {\prime})}{\zeta (1 + z _ {j}) \zeta (1 + z _ {j} ^ {\prime})} \frac {R ^ {z _ {j} + z _ {j} ^ {\prime}}}{z _ {j} ^ {2} z _ {j ^ {\prime 2}}} d z _ {j} d z _ {j} ^ {\prime} \\ \quad + O (e ^ {- \delta \sqrt {\log R}}) \\ = I (G (z _ {1}, \ldots , z _ {m}, 0, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime}, 0), m) \log R + I (H, m) + O (e ^ {- \delta \sqrt {\log R}}) \end{array}
$$

where$\delta > 0$and$\boldsymbol { H } : \mathcal { D } _ { \sigma } ^ { m }  \mathbb { C }$is the function

$$
\begin{array}{c} {H (z _ {1}, \ldots , z _ {m}, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime}) := \frac {\partial G}{\partial z _ {m + 1} ^ {\prime}} (z _ {1}, \ldots , z _ {m}, 0, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime}, 0)} \\ {+ \frac {1}{2 \pi i} \int_ {\Gamma_ {0}} G (z _ {1}, \ldots , z _ {m}, z _ {m + 1}, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime}, - z _ {m + 1}) \frac {d z _ {m + 1}}{\zeta (1 + z _ {m + 1}) \zeta (1 - z _ {m + 1}) z _ {m + 1} ^ {4}}.} \end{array}
$$

The error term$O ( e ^ { - \delta { \sqrt { \log R } } } )$, which we claim here, arises by using (10.10) and several applications of$\left( \mathrm { { A . 3 } } \right)$

Now both of the functions

$$
G (z _ {1}, \ldots , z _ {m}, 0, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime}, 0)
$$

and

$$
H (z _ {1}, \ldots , z _ {m}, z _ {1} ^ {\prime}, \ldots , z _ {m} ^ {\prime})
$$

are analytic on$\mathcal { D } _ { \sigma } ^ { m }$and (appealing to$\left( \mathrm { A . 6 } \right) )$we have

$$
\left\| H \right\| _ {C ^ {j} (\mathcal {D} _ {\sigma} ^ {m})} = O _ {m} \big (\left\| G \right\| _ {C ^ {j + 1} (\mathcal {D} _ {\sigma} ^ {m + 1})} \big)
$$

for$0 \leqslant j \leqslant m$. Using the inductive hypothesis, we therefore obtain

$$
I (G, m + 1)
$$

$$
\begin{array}{l} I (G, m + 1) \\ = G (0, \ldots , 0) (\log R) ^ {m + 1} + \sum_ {j = 1} ^ {m} O _ {m} (\| G (\cdot , 0, \cdot , 0) \| _ {C ^ {j} (\mathcal {D} _ {\sigma} ^ {m})} (\log R) ^ {m + 1 - j}) \\ \quad + H (0, \ldots , 0) (\log R) ^ {m} + \sum_ {j = 1} ^ {m} O _ {m} (\| H \| _ {C ^ {j} (\mathcal {D} _ {\sigma} ^ {m})} (\log R) ^ {m - j}) + O (e ^ {- \delta \sqrt {\log R}}) \\ = G (0, \ldots , 0) (\log R) ^ {m + 1} + \sum_ {j = 1} ^ {m} O _ {m} (\| G \| _ {C ^ {j} (\mathcal {D} _ {\sigma} ^ {m + 1})} (\log R) ^ {m + 1 - j}) \\ \quad + H (0, \ldots , 0) (\log R) ^ {m} + \sum_ {j = 1} ^ {m} O _ {m} (\| G \| _ {C ^ {j + 1} (\mathcal {D} _ {\sigma} ^ {m + 1})} (\log R) ^ {m - j}) + O (e ^ {- \delta \sqrt {\log R}}) \\ = G (0, \ldots , 0) (\log R) ^ {m + 1} + \sum_ {j = 1} ^ {m + 1} O _ {m} (\| G \| _ {C ^ {j} (\mathcal {D} _ {\sigma} ^ {m + 1})} (\log R) ^ {m + 1 - j}) + O (e ^ {- \delta \sqrt {\log R}}), \end{array}
$$

which is what we wanted to prove.

Centre for Mathematical Sciences<sub>,</sub> Cambridge CB3 0WA<sub>,</sub> England E-mail address: b.j.green@dpmms.cam.ac.uk

University of California at Los Angeles<sub>,</sub> Los Angeles<sub>,</sub> CA E-mail address: tao@math.ucla.edu

## References

[1] I. Assani, Pointwise convergence of ergodic averages along cubes, preprint.

[2] A. Balog, Linear equations in primes, Mathematika 39 (1992) 367–378.

[3], Six primes and an almost prime in four linear equations, Canadian J. Math. 50 (1998), 465–486.

[4] V. Bergelson and A. Leibman, Polynomial extensions of van der Waerden’s and Szemer´edi’s theorems, J. Amer. Math. Soc. 9 (1996), 725–753.

[5] J. Bourgain, A Szemer´edi-type theorem for sets of positive density in$\mathbb { R } ^ { k } .$Israel J. Math. 54 (1986), 307–316.

[6]———, On triples in arithmetic progression, GAFA 9 (1999), 968–984.

[7] J.-R. Chen, On the representation of a larger even integer as the sum of a prime and the product of at most two primes, Sci. Sinica 16 (1973), 157–176.

[8] S. Chowla, There exists an infinity of 3-combinations of primes in A. P., Proc. Lahore Philos. Soc. 6 (1944), 15–16.

[9] P. Erdos˝ and P. Turan´ , On some sequences of integers, J. London Math. Soc. 11 (1936), 261–264.

[10] H. Furstenberg, Ergodic behavior of diagonal measures and a theorem of Szemer´edi on arithmetic progressions, J. Analyse Math. 31 (1977), 204–256.

[11] H. Furstenberg and Y. Katznelson, An ergodic Szemer´edi theorem for commuting transformations, J. Analyse Math. 34 (1978), 275–291.

[12], A density version of the Hales-Jewett theorem, J. Analyse Math. 57 (1991), 64–119.

[13] H. Furstenberg, Y. Katznelson, and D. Ornstein, The ergodic theoretical proof of Szemer´edi’s theorem, Bull. Amer. Math. Soc. 7 (1982), 527–552.

[14] H. Furstenberg and B. Weiss, A mean ergodic theorem for$\begin{array} { r } { 1 / N \sum _ { n = 1 } ^ { N } f ( T ^ { n } x ) g ( T ^ { n ^ { 2 } } x ) , } \end{array}$ in Convergence in Ergodic Theory and Probability (Columbus OH 1993), 193–227, Ohio State Univ. Math. Res. Inst. Publ. 5, de Gruyter, Berlin, 1996.

[15] D. Goldston and C. Y. Yıldırım, Higher correlations of divisor sums related to primes, I: Triple correlations, Integers 3 (2003), 66pp.

[16], Higher correlations of divisor sums related to primes, III: Small gaps between primes, Proc. London Math. Soc. 95 (2007), 653–686.

[17]Small gaps between primes, I, preprint; http://front.math.ucdavis.edu/0504336.

[18] W. T. Gowers, A new proof of Szemer´edi’s theorem for arithmetic progressions of length four, GAFA 8 (1998), 529–551.

[19] ———, A new proof of Szemer´edi’s theorem, GAFA 11 (2001), 465–588.

[20], Hypergraph regularity and the multidimensional Szemer´edi theorem, Ann. of Math. 166 (2007), 897–946.

[21] B. J. Green, Roth’s theorem in the primes, Ann. of Math. 161 (2005), 1609–1636.

[22] B. J. Green, A Szemer´edi-type regularity lemma in abelian groups, with applications, GAFA 15 (2005), 340–376.

[23] B. J. Green and T. Tao, Restriction theory of the Selberg sieve, with applications, J. Th´eor. Nombres Bordeaux 18 (2006), 147–182.

[24] G. H. Hardy and J. E. Littlewood, Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes, Acta Math. 44 (1923), 1–70.

[25] D. R. Heath-Brown, Three primes and an almost-prime in arithmetic progression, J. London Math. Soc. 23 (1981), 396–414.

[26] D. R. Heath-Brown, Linear relations amongst sums of two squares, in Number Theory and Algebraic Geometry (to Peter Swinnerton-Dyer on his 75th birthday), London Math. Soc. Lecture Note Ser. 303, Cambridge Univ. Press, Cambridge (2003).

[27] B. Host and B. Kra, Convergence of Conze-Lesigne averages, Ergodic Theory Dynam. Systems 21 (2001), 493–509.

[28], Nonconventional ergodic averages and nilmanifolds, Ann. of Math. 161 (2005), 397–488.

[29] ———, Convergence of polynomial ergodic averages, Israel J. Math. 149 (2005), 1–19.

[30] Y. Kohayakawa, T. -Luczak, and V. Rodl ¨ , Arithmetic progressions of length three in subsets of a random set, Acta Arith. 75 (1996), 133–163.

[31] I. -Laba and M. Lacey, On sets of integers not containing long arithmetic progressions, unpublished; Available at http://www.arxiv.org/pdf/math.CO/0108155.

[32] A. Moran, P. Pritchard, and A. Thyssen, Twenty-two primes in arithmetic progression, Math. Comp. 64 (1995), 1337–1339.

[33] O. Ramare´, On Snirel’man’s constant, Ann. Scuola Norm. Pisa 21 (1995), 645–706.

[34] O. Ramare´ and I. Z. Ruzsa, Additive properties of dense subsets of sifted sequences, J. Th´eor. Nombres Bordeaux 13 (2001), 559–581.

[35] R. Rankin, Sets of integers containing not more than a given number of terms in arithmetical progression, Proc. Royal Soc. Edinburgh Sect. A 65 (1960/1961), 332–344.

[36] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.

[37] E. Szemeredi ´ , On sets of integers containing no four elements in arithmetic progression, Acta Math. Acad. Sci. Hungar. 20 (1969), 89–104.

[38], On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 199–245.

[39], Regular partitions of graphs, in Proc. Colloque Inter. CNRS (J.-C. Bermond, J.-C. Fournier, M. Las Vergnas, D. Sotteau, eds.) 399–401, CNRS, Paris (1978).

[40] T. Tao, A quantitative ergodic theory proof of Szemer´edi’s theorem, Electronic J. Combinatorics 13 (2006), 49 pp.

[41] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, second edition, Oxford University Press, New York, 1986.

[42] J. G. van der Corput, Uber Summen von Primzahlen und Primzahlquadraten,<sup>¨</sup> Math. Ann. 116 (1939), 1–50.

[43] P. Varnavides, On certain sets of positive density, J. London Math. Soc. 34 (1959), 358–360.

[44] T. Ziegler, Universal characteristic factors and Furstenberg averages, J. Amer. Math. Soc. 20 (2007), 53–97.

[45], A non-conventional ergodic theorem for a nilsystem, Ergodic Theory Dynam. Systems 25 (2005), 1357–1370.